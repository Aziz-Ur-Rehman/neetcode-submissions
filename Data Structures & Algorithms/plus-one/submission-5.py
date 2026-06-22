class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        if digits[-1] + 1 < 9:
            digits[-1] += 1
        else:
            digits[-1] = (digits[-1] + 1) % 10
            carry = 1
        if carry:
            for i in range(len(digits)-2,-1,-1):
                if digits[i] + carry <= 9:
                    digits[i] = digits[i] + carry
                    carry = 0
                    break
                else:
                    digits[i] = (digits[i] + carry) % 10
                    carry = 1
        
            if carry:
                digits.insert(0, carry)


        return digits