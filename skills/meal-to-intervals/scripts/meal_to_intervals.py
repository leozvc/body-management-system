#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path
from urllib import parse, request, error
from datetime import datetime

BASE_URL = "https://intervals.icu/api/v1"

# 每100g标准营养（优先使用，避免OpenFoodFacts误命中）
FOOD_OVERRIDE_100G = {
    "egg": {"calories": 143, "protein": 12.6, "fat": 9.5, "carbs": 1.1},
    "chicken breast": {"calories": 165, "protein": 31.0, "fat": 3.6, "carbs": 0.0},
    "chicken thigh": {"calories": 209, "protein": 26.0, "fat": 10.9, "carbs": 0.0},
    "white rice": {"calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28.2},
    "whole wheat bread": {"calories": 250, "protein": 10.7, "fat": 3.6, "carbs": 43.0},
    "broccoli": {"calories": 34, "protein": 2.8, "fat": 0.4, "carbs": 6.6},
    "tomato": {"calories": 18, "protein": 0.9, "fat": 0.2, "carbs": 3.9},
    "potato": {"calories": 77, "protein": 2.0, "fat": 0.1, "carbs": 17.0},
    "cooking oil": {"calories": 884, "protein": 0.0, "fat": 100.0, "carbs": 0.0},
    "water": {"calories": 0.0, "protein": 0.0, "fat": 0.0, "carbs": 0.0},
    "instant noodles": {"calories": 470, "protein": 9.0, "fat": 17.0, "carbs": 70.0},
    "beef ball": {"calories": 180, "protein": 12.0, "fat": 12.0, "carbs": 7.0},
    "beef shank": {"calories": 200, "protein": 30.0, "fat": 7.0, "carbs": 0.0},
    "pork chive dumplings": {"calories": 220, "protein": 9.0, "fat": 7.0, "carbs": 30.0},
    "mcdonald's cheeseburger": {"calories": 257, "protein": 12.7, "fat": 11.0, "carbs": 28.0},
}

ALIASES = {
    "鸡蛋": "egg",
    "全麦面包": "whole wheat bread",
    "全麦吐司": "whole wheat bread",
    "米饭": "white rice",
    "白米饭": "white rice",
    "鸡胸肉": "chicken breast",
    "鸡腿肉": "chicken thigh",
    "西兰花": "broccoli",
    "番茄": "tomato",
    "土豆": "potato",
    "食用油": "cooking oil",
    "水": "water",
    "饮用水": "water",
    "矿泉水": "water",
    "方便面": "instant noodles",
    "泡面": "instant noodles",
    "牛肉丸": "beef ball",
    "牛肉丸子": "beef ball",
    "牛腱子": "beef shank",
    "韭菜肉饺子": "pork chive dumplings",
    "韭菜饺子": "pork chive dumplings",
    "麦当劳吉士汉堡": "mcdonald's cheeseburger",
    "吉士汉堡": "mcdonald's cheeseburger",
    "麦当劳汉堡": "mcdonald's cheeseburger",
}


def parse_args():
    p = argparse.ArgumentParser(description="Calculate meal nutrition and write to Intervals.icu")
    p.add_argument("--input", required=True, help="Meal JSON path")
    p.add_argument("--config", default="", help="Path to config.json")
    p.add_argument("--mode", choices=["event_note", "wellness_only"], default="event_note")
    p.add_argument("--update-wellness", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def load_config(config_arg: str):
    path = Path(config_arg) if config_arg else Path(__file__).resolve().parent.parent / "config.json"
    if not path.exists():
        raise FileNotFoundError(f"config file not found: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    api_key = data["intervals_icu"]["api_key"]
    athlete_id = data["intervals_icu"]["athlete_id"]
    if not api_key or not athlete_id:
        raise ValueError("api_key/athlete_id missing in config")
    return api_key, athlete_id, data


def canonical_name(name: str):
    n = name.strip().lower()
    return ALIASES.get(n, n)


def fetch_openfoodfacts(name: str):
    q = parse.quote(name)
    url = (
        "https://world.openfoodfacts.org/cgi/search.pl"
        f"?search_terms={q}&search_simple=1&action=process&json=1&page_size=1"
    )
    with request.urlopen(url, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8", errors="ignore"))

    products = data.get("products", [])
    if not products:
        raise ValueError(f"No nutrition match for {name}")

    nutr = products[0].get("nutriments", {})
    kcal = nutr.get("energy-kcal_100g") or nutr.get("energy-kcal")
    protein = nutr.get("proteins_100g") or 0
    fat = nutr.get("fat_100g") or 0
    carbs = nutr.get("carbohydrates_100g") or 0

    if kcal is None:
        raise ValueError(f"kcal missing for {name}")

    return {
        "calories_100g": float(kcal),
        "protein_100g": float(protein),
        "fat_100g": float(fat),
        "carbs_100g": float(carbs),
        "source": "OpenFoodFacts",
    }


def nutrition_per_100g(name: str):
    c = canonical_name(name)
    if c in FOOD_OVERRIDE_100G:
        n = FOOD_OVERRIDE_100G[c]
        return {
            "calories_100g": float(n["calories"]),
            "protein_100g": float(n["protein"]),
            "fat_100g": float(n["fat"]),
            "carbs_100g": float(n["carbs"]),
            "source": "LocalOverride",
        }
    return fetch_openfoodfacts(c)


def calc_item(item):
    raw_name = item["name"].strip()
    name = canonical_name(raw_name)
    grams = float(item["grams"])
    if grams <= 0:
        raise ValueError(f"Invalid grams for {raw_name}")

    n = nutrition_per_100g(raw_name)
    r = grams / 100.0
    return {
        "name": raw_name,
        "matchedName": name,
        "grams": grams,
        "caloriesKcal": round(n["calories_100g"] * r, 2),
        "proteinG": round(n["protein_100g"] * r, 2),
        "fatG": round(n["fat_100g"] * r, 2),
        "carbsG": round(n["carbs_100g"] * r, 2),
        "source": n["source"],
    }


def normalize_meal_time(ts: str):
    dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def build_result(meal):
    items_in = meal.get("items", [])
    items = [calc_item(x) for x in items_in] if items_in else []
    totals = {
        "caloriesKcal": round(sum(x["caloriesKcal"] for x in items), 2),
        "proteinG": round(sum(x["proteinG"] for x in items), 2),
        "fatG": round(sum(x["fatG"] for x in items), 2),
        "carbsG": round(sum(x["carbsG"] for x in items), 2),
    }
    return {
        "mealName": meal.get("meal_name", "健康数据更新"),
        "mealTime": normalize_meal_time(meal["meal_time"]),
        "totals": totals,
        "items": items,
        "wellness": meal.get("wellness", {}),
    }


def _basic_auth_token(username, password):
    import base64
    return base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")


def intervals_request(method, url, api_key, payload=None):
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
    req = request.Request(url, method=method, data=data)
    req.add_header("Authorization", "Basic " + _basic_auth_token("API_KEY", api_key))
    req.add_header("Content-Type", "application/json")

    try:
        with request.urlopen(req, timeout=30) as resp:
            return True, resp.status, resp.read().decode("utf-8", errors="ignore")
    except error.HTTPError as e:
        return False, e.code, e.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return False, -1, str(e)


def build_event_payload(result):
    t = result["totals"]
    lines = [
        f"Calories: {t['caloriesKcal']} kcal",
        f"Protein: {t['proteinG']} g",
        f"Fat: {t['fatG']} g",
        f"Carbs: {t['carbsG']} g",
        "",
        "Items:",
    ]
    if result["items"]:
        for i in result["items"]:
            lines.append(
                f"- {i['name']} ({i['matchedName']}) {int(i['grams'])}g | {i['caloriesKcal']} kcal | P{i['proteinG']} F{i['fatG']} C{i['carbsG']} | {i['source']}"
            )
    else:
        lines.append("- (no meal items, wellness-only update)")

    return {
        "category": "NOTE",
        "start_date_local": result["mealTime"],
        "name": f"🍽 {result['mealName']}",
        "description": "\n".join(lines),
    }


def build_wellness_payload(result, meal_wellness: dict, cfg: dict):
    # 允许在 config.json 里自定义字段映射，避免不同账户字段名不一致
    # 默认映射（若字段不被服务器接受，改 config 覆盖）
    default_map = {
        "caloriesKcal": "kcalConsumed",
        "proteinG": "protein",
        "fatG": "fatTotal",
        "carbsG": "carbohydrates",
    }
    custom_map = cfg.get("intervals_icu", {}).get("wellness_nutrition_field_map", {})
    if isinstance(custom_map, dict):
        default_map.update(custom_map)

    # 常见健康字段别名（中文/驼峰/下划线）
    wellness_aliases = {
        "体重": "weight", "weight": "weight", "tempweight": "tempWeight",
        "体脂": "bodyFat", "bodyfat": "bodyFat",
        "静息心率": "restingHR", "resting_hr": "restingHR", "restinghr": "restingHR", "tempsleephr": "tempRestingHR",
        "hrv": "hrv", "hrvsdnn": "hrvSDNN",
        "血氧": "spO2", "spo2": "spO2",
        "呼吸": "respiration", "respiration": "respiration",
        "压力": "stress", "stress": "stress",
        "步数": "steps", "steps": "steps",
        "睡眠时长": "sleepSecs", "sleepsecs": "sleepSecs", "sleep_secs": "sleepSecs",
        "睡眠评分": "sleepScore", "sleepscore": "sleepScore", "sleep_score": "sleepScore",
        "睡眠质量": "sleepQuality", "sleepquality": "sleepQuality",
        "睡眠平均心率": "avgSleepingHR", "avgsleepinghr": "avgSleepingHR",
        "热量": "kcalConsumed", "kcal": "kcalConsumed", "kcalconsumed": "kcalConsumed",
        "碳水": "carbohydrates", "carbohydrates": "carbohydrates",
        "蛋白": "protein", "protein": "protein",
        "脂肪": "fatTotal", "fattotal": "fatTotal",
        "饮水": "hydration", "hydration": "hydration", "饮水量": "hydrationVolume", "hydrationvolume": "hydrationVolume",
        "血糖": "bloodGlucose", "bloodglucose": "bloodGlucose",
        "乳酸": "lactate", "lactate": "lactate",
        "收缩压": "systolic", "systolic": "systolic",
        "舒张压": "diastolic", "diastolic": "diastolic",
        "心情": "mood", "mood": "mood",
        "动机": "motivation", "motivation": "motivation",
        "酸痛": "soreness", "soreness": "soreness",
        "疲劳": "fatigue", "fatigue": "fatigue",
        "准备度": "readiness", "readiness": "readiness",
        "受伤": "injury", "injury": "injury",
        "评论": "comments", "备注": "comments", "comments": "comments",
        "vo2max": "vo2max", "腰围": "abdomen", "abdomen": "abdomen",
        "baevskysi": "baevskySI", "ramp": "rampRate", "ramprate": "rampRate",
        "atl": "atl", "atlload": "atlLoad", "ctl": "ctl", "ctlload": "ctlLoad",
        "经期": "menstrualPhase", "menstrualphase": "menstrualPhase", "经期预测": "menstrualPhasePredicted", "menstrualphasepredicted": "menstrualPhasePredicted"
    }

    allowed_fields = {
        "abdomen","atl","atlLoad","avgSleepingHR","baevskySI","bloodGlucose","bodyFat","carbohydrates",
        "comments","ctl","ctlLoad","diastolic","fatTotal","fatigue","hrv","hrvSDNN","hydration",
        "hydrationVolume","injury","kcalConsumed","lactate","menstrualPhase","menstrualPhasePredicted",
        "mood","motivation","protein","rampRate","readiness","respiration","restingHR","sleepQuality",
        "sleepScore","sleepSecs","soreness","spO2","steps","stress","systolic","tempRestingHR",
        "tempWeight","vo2max","weight"
    }

    payload = {}
    rejected = []
    if isinstance(meal_wellness, dict):
        for k, v in meal_wellness.items():
            kk = wellness_aliases.get(str(k).strip().lower(), k)
            if kk in allowed_fields:
                payload[kk] = v
            else:
                rejected.append(k)

    # 仅在有餐食条目时自动回填营养总量，避免 wellness-only 场景被 0 覆盖
    if result.get("items"):
        for src_key, dst_key in default_map.items():
            payload[dst_key] = result["totals"][src_key]

        # 若识别到饮水条目，自动把克数换算成升，写入 hydrationVolume 健康字段
        # 约定：1g 水 ≈ 1ml
        water_grams = sum(
            float(i.get("grams", 0))
            for i in result["items"]
            if str(i.get("matchedName", "")).lower() == "water"
        )
        if water_grams > 0:
            payload["hydrationVolume"] = round(water_grams / 1000.0, 3)

    if rejected:
        print(json.dumps({"warn": "unsupported wellness fields ignored", "fields": rejected}, ensure_ascii=False), file=sys.stderr)

    return payload


def main():
    a = parse_args()
    meal_path = Path(a.input)
    if not meal_path.exists():
        print("input file not found", file=sys.stderr)
        sys.exit(1)

    meal = json.loads(meal_path.read_text(encoding="utf-8"))
    if "meal_time" not in meal:
        print("missing field: meal_time", file=sys.stderr)
        sys.exit(2)

    if a.mode == "event_note" and "items" not in meal:
        print("missing field: items (event_note mode)", file=sys.stderr)
        sys.exit(2)

    if a.mode == "wellness_only" and "wellness" not in meal:
        print("missing field: wellness (wellness_only mode)", file=sys.stderr)
        sys.exit(2)

    api_key, athlete_id, cfg = load_config(a.config)
    result = build_result(meal)
    event_payload = build_event_payload(result)

    if a.dry_run:
        out = {"nutrition": result, "eventPayload": event_payload}
        # 约定：event_note 默认也会同步 wellness（可通过输入 wellness 扩展更多健康字段）
        if a.mode in ("event_note", "wellness_only") or a.update_wellness:
            out["wellnessPayload"] = build_wellness_payload(result, result.get("wellness", {}), cfg)
        print(json.dumps(out, ensure_ascii=False, indent=2))
        print("Dry run OK")
        return

    ok1, code1, body1 = True, 200, "skipped"
    response = {}

    if a.mode == "event_note":
        event_url = f"{BASE_URL}/athlete/{athlete_id}/events"
        ok1, code1, body1 = intervals_request("POST", event_url, api_key, event_payload)
        response["event_write"] = {"ok": ok1, "status": code1, "body": body1[:500]}

    # 约定：event_note 默认也会同步 wellness，确保健康字段持续累计
    if a.mode in ("event_note", "wellness_only") or a.update_wellness:
        date_key = datetime.fromisoformat(result["mealTime"]).date().isoformat()
        wellness_url = f"{BASE_URL}/athlete/{athlete_id}/wellness/{date_key}"
        wellness_payload = build_wellness_payload(result, result.get("wellness", {}), cfg)
        ok2, code2, body2 = intervals_request("PUT", wellness_url, api_key, wellness_payload)
        response["wellness_update"] = {
            "ok": ok2,
            "status": code2,
            "payload": wellness_payload,
            "body": body2[:500],
        }

    print(json.dumps(response, ensure_ascii=False, indent=2))
    if a.mode == "event_note" and not ok1:
        sys.exit(3)


if __name__ == "__main__":
    main()
