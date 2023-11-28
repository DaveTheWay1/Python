class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num, *nums):
        self.result += num
        print(self.result)
        # the below for loop will not run if there is no nums
        for n in nums:
            self.result += n
            print(self.result)
        return self

    def subtract(self, num, *nums):
        self.result -= num
        print(self.result)
        # the below for loop will not run if there is no nums
        for n in nums:
            self.result -= n
            print(self.result)
        return self
md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
# .result
print(x)	
# should print 5