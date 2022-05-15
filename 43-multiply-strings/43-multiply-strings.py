class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        first = num1[::-1]
        second = num2[::-1]
        
        def sumResults(results):
            answer = results.pop()
            
            for result in results:
                newAnswer = []
                carry = 0
                
                for digit1, digit2 in zip_longest(result, answer, fillvalue = 0):
                    curSum = digit1 + digit2 + carry
                    carry = curSum//10
                    newAnswer.append(curSum%10)
                if carry > 0:
                    newAnswer.append(carry)
                answer = newAnswer
            return answer     
        
        def multiplyDigit(digit2, numZero, first):
            currRes = [0]*numZero
            carry = 0
            
            for digit1 in first:
                multiplication = int(digit1) * int(digit2) + carry
                carry = multiplication//10
                currRes.append(multiplication%10)
            if carry > 0:
                currRes.append(carry)
            return currRes
        
        results = []
        for index, digit in enumerate(second):
            result = multiplyDigit(digit, index, first)
            results.append(result)
        answer = sumResults(results)
        return ''.join([str(digit) for digit in reversed(answer)])
        
        