import re

text = "apple,banana,orange,grape"
pattern = r"an"

split_result = re.split(pattern, text)
print("Split result:", split_result)
