## Keys associated with Values in Dictionary

from collections import defaultdict

test_dict = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]}

result = defaultdict(list)
for key, value in test_dict.items():
    for ele in value:
        result[ele].append(key)

print(str(dict(result)))