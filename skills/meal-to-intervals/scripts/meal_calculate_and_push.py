#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path
from urllib import parse, request, error


def parse_args():
    p = argparse.ArgumentParser(description="Calculate meal nutrition and push to intervals.icu endpoint")
    p.add_argument("--input", required=True, help="Meal JSON path")
    p.add_argument("--intervals-base-url", required=True)
    p.add_argument("--intervals-endpoint", required=True)
    p.add_argument("--intervals-token", required=True)
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def fetch_openfoodfacts(name: str):
    q = parse.quote(name)
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={q}&search_simple=1&action=process&json=1&page_size=1"
    with request.urlopen(url, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8", errors="ignore"))

    products = data.get("products", [])
    if not products:
        raise ValueError(f"No nutrition match found for: {name}")

    nutr = products[0].get("nutriments", {})
    # per 100g fallbacks
    kcal = nutr.get("energy-kcal_100g") or nutr.get("energy-kcal")
    protein = nutr.get("proteins_100g")
    fat = nutr.get("fat_100g")
    carbs = nutr.get("carbohydrates_100g")

    if kcal is None:
        raise ValueError(f"Missing kcal data for: {name}")

    return {
        "calories_100g": float(kcal),
        "protein_100g": float(protein or 0),
        "fat_100g": float(fat or 0),
        "carbs_100g": float(carbs or 0),
    }


def calc_item(item):
    name = item["name"].strip()
    grams = float(item["grams"])
    if grams <= 0:
        raise ValueError(f"Invalid grams for {name}")

    n = fetch_openfoodfacts(name)
    ratio = grams / 100.0
    return {
        "name": name,
        "grams": grams,
        "caloriesKcal": round(n["calories_100g"] * ratio, 2),
        "proteinG": round(n["protein_100g"] * ratio, 2),
        "fatG": round(n["fat_100g"] * ratio, 2),
        "carbsG": round(n["carbs_100g"] * ratio, 2),
        "source": "OpenFoodFacts",
    }


def build_payload(meal):
    results = [calc_item(i) for i in meal["items"]]
    totals = {
        "caloriesKcal": round(sum(i["caloriesKcal"] for i in results), 2),
        "proteinG": round(sum(i["proteinG"] for i in results), 2),
        "fatG": round(sum(i["fatG"] for i in results), 2),
        "carbsG": round(sum(i["carbsG"] for i in results), 2),
    }
    return {
        "mealName": meal["meal_name"],
        "mealTime": meal["meal_time"],
        "totals": totals,
        "items": results,
    }


def post_intervals(url, token, payload):
    req = request.Request(url, method="POST", data=json.dumps(payload, ensure_ascii=False).encode("utf-8"))
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    try:
        with request.urlopen(req, timeout=30) as resp:
            return True, resp.status, resp.read().decode("utf-8", errors="ignore")
    except error.HTTPError as e:
        return False, e.code, e.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return False, -1, str(e)


def main():
    a = parse_args()
    p = Path(a.input)
    if not p.exists():
        print("input file not found", file=sys.stderr)
        sys.exit(1)

    meal = json.loads(p.read_text(encoding="utf-8"))
    for key in ("meal_name", "meal_time", "items"):
        if key not in meal:
            print(f"missing field: {key}", file=sys.stderr)
            sys.exit(2)

    payload = build_payload(meal)

    if a.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        print("Dry run OK")
        return

    url = a.intervals_base_url.rstrip("/") + "/" + a.intervals_endpoint.lstrip("/")
    ok, code, body = post_intervals(url, a.intervals_token, payload)
    print(json.dumps({"ok": ok, "status": code, "body": body[:500]}, ensure_ascii=False, indent=2))
    if not ok:
        sys.exit(3)


if __name__ == "__main__":
    main()
