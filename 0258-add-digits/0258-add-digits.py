class Solution:
    def addDigits(self, num: int) -> int:
        #use whileloop
        while num >= 10:
            sum = 0
            for digit in str(num):
                sum += int(digit)
            num = sum
        return num


        