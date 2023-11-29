from operator import itemgetter

data = [('안효성', 10.25),
        ('임호연', 15.78),
        ('박태용', 13.62)]

result = sorted(data, key=itemgetter(1))
print(result)