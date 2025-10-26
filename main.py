from src.utils import read_json
from src.external_api import convert_to_rub

operations = read_json("data/operations.json")

# Находим первую операцию не в рублях
for op in operations:
    if op.get("operationAmount", {}).get("currency", {}).get("code") != "RUB":
        test_op = op
        break

print("Исходная операция:", test_op)
print("\nКонвертируем...")

rub_amount = convert_to_rub(test_op)
print(f"\nРезультат в рублях: {rub_amount:.2f}")
