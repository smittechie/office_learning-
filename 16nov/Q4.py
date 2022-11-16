# Dictionary Values Mean
import statistics
test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10}

a = test_dict.values()
print(a)
b= statistics.mean(a)
print(b)