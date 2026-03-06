# Meal Schema (for meal-to-intervals)

## Input JSON

```json
{
  "meal_name": "午餐",
  "meal_time": "2026-02-26T12:30:00+08:00",
  "items": [
    {"name": "chicken breast", "grams": 150},
    {"name": "white rice", "grams": 180},
    {"name": "broccoli", "grams": 100}
  ],
  "wellness": {
    "weight": 70.2,
    "restingHR": 56,
    "sleepSecs": 25200
  }
}
```

- `meal_name` 必填
- `meal_time` 必填（ISO-8601）
- `items[].name` 必填
- `items[].grams` 必填
- `wellness` 可选

## Intervals Event Payload（自动生成）

```json
{
  "category": "NOTE",
  "start_date_local": "2026-02-26T12:30:00",
  "name": "🍽 午餐",
  "description": "Calories: ..."
}
```

POST 目标：
`/api/v1/athlete/{athlete_id}/events`

## Wellness Update（重点）

开启 `--update-wellness` 后，会 PUT 到：
`/api/v1/athlete/{athlete_id}/wellness/{YYYY-MM-DD}`

并自动写入营养汇总字段（默认映射）：
- 热量：`caloriesKcal -> kcalConsumed`
- 蛋白：`proteinG -> protein`
- 脂肪：`fatG -> fatTotal`
- 碳水：`carbsG -> carbohydrates`

如果你账户字段名不一样，可在 `config.json` 设置映射：

```json
{
  "intervals_icu": {
    "wellness_nutrition_field_map": {
      "caloriesKcal": "yourCaloriesField",
      "proteinG": "yourProteinField",
      "fatG": "yourFatField",
      "carbsG": "yourCarbField"
    }
  }
}
```
