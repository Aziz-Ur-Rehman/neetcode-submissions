class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def sumofsqaures(num):
            res = 0

            while num:
                digit = num%10
                digit = digit**2
                res += digit
                num = num//10
            return res


        while n not in visited:
            visited.add(n)
            n = sumofsqaures(n)

            if n==1:
                return True
        return False