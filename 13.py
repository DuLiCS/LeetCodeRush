class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        characterIndex = 0
        result = 0
        while characterIndex < len(s):
            if characterIndex == len(s) - 1:
                result += romanDict[s[characterIndex]]
                return result
            if s[characterIndex] == 'I' and (s[characterIndex + 1] == 'V' or s[characterIndex + 1] == 'X'):
                result += romanDict[s[characterIndex + 1]] - romanDict[s[characterIndex]]
                characterIndex += 2
            elif s[characterIndex] == 'X' and (s[characterIndex + 1] == 'L' or s[characterIndex + 1] == 'C'):
                result += romanDict[s[characterIndex + 1]] - romanDict[s[characterIndex]]
                characterIndex += 2
            elif s[characterIndex] == 'C' and (s[characterIndex + 1] == 'D' or s[characterIndex + 1] == 'M'):
                result += romanDict[s[characterIndex + 1]] - romanDict[s[characterIndex]]
                characterIndex += 2
            else:
                result += romanDict[s[characterIndex]]
                characterIndex += 1

        return result

    def romanToInt1(self, s: str) -> int:
        romanDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        preNum = 0
        total = 0
        for character in s[::-1]:
            value = romanDict[character]
            if value < preNum:
                total -= value
            else:
                total += value

            preNum = value

        return total






s = "LVIII"
solution = Solution()
print(solution.romanToInt(s))