import re

def normalize_phone(phone_number):
  pattern = r"[^\d+]"
  replacement = "" 
  pattern1 = r"^38" 
  replacement1 = "+38" 
  pattern2 = r"^0"
  replacement2 = "+380"
  modified_phone_n = re.sub(pattern, replacement, phone_number)
  modified_phone_n2 = re.sub(pattern1, replacement1, modified_phone_n)
  modified_phone_n3 = re.sub(pattern2, replacement2, modified_phone_n2)
  return modified_phone_n3

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)