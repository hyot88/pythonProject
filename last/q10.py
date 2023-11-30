class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList

    def sum(self):
        result = 0
        for num in self.numberList:
            result += num
        return result

    def avg(self):
        total = self.sum()
        return total / len(self.numberList)


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())
