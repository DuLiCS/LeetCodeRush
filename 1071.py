'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        flag = 1
        result = ""


        if len(str1) == len(str2):
            return str1 if str1 == str2 else ""

        else:
            if len(str1) >= len(str2):
                lstr = str1
                sstr = str2
            else:
                lstr = str2
                sstr = str1

            if len(lstr) % len(sstr) == 0:
                cnt = int(len(lstr) / len(sstr))
                for k in range(cnt):
                    if lstr == sstr*(k+1):
                        return sstr
            for i in range(len(sstr)):
                divisor = sstr[0:i+1]

                if len(lstr) % (i + 1) == 0:
                    cnt = len(lstr) / (i + 1)
                    for j in range(int(cnt)):
                        if divisor == lstr[(i + 1) * j:(i + 1) * j + i + 1]:
                            result = divisor
                            flag = 1
                            continue
                        else:
                            flag = 0
                            break

                else:
                    continue

                if flag == 1:
                    return result
            if flag == 0:
                return ""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) >= len(str2):
            lstr, sstr = str1, str2
        else:
            lstr, sstr = str2, str1
        if len(lstr) % len(sstr) == 0:
            cnt = int(len(lstr) / len(sstr))
            for k in range(cnt):
                if lstr == sstr * (k + 1):
                    return sstr
        else:
            for i in range(len(sstr)):
                if len(sstr)%(len(sstr) - i) == 0:
                    cnt = int(len(sstr) / (len(sstr) - i))
                    for j in range(int(cnt)):
                        divisor = sstr[cnt * j : cnt * j + len(sstr) - i]
                        if sstr == divisor * (j + 1):
                            if len(lstr) % len(divisor) == 0:
                                cnt = int(len(lstr) / len(divisor))
                                for k in range(cnt):
                                    if lstr == divisor * (k + 1):
                                        return divisor



        return ""
'''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 确定lstr为较长的字符串，sstr为较短的字符串
        if len(str1) >= len(str2):
            lstr, sstr = str1, str2
        else:
            lstr, sstr = str2, str1

        # 如果lstr的长度是sstr的整数倍，尝试是否sstr * k == lstr
        if len(lstr) % len(sstr) == 0:
            if lstr == sstr * (len(lstr) // len(sstr)):
                return sstr
        # 否则从sstr中尝试找到可能的gcd字符串
        for i in range(1, len(sstr)):
            divisor = sstr[:len(sstr) - i]
            if len(sstr) % len(divisor) == 0 and len(lstr) % len(divisor) == 0:
                if sstr == divisor * (len(sstr) // len(divisor)) and lstr == divisor * (len(lstr) // len(divisor)):
                    return divisor

        return ""



class SolutionRecursion:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1 if str1 else str2

        if str1 + str2 != str2 + str1:
            return ""

        if str1.startswith(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        if str2.startswith(str1):
            return self.gcdOfStrings(str1, str2[len(str1):])

        return ""



str1 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
str2 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"

str3 = "ABC"
str4 = "ABCABC"
sol = Solution()
result = sol.gcdOfStrings(str1, str2)

solr = SolutionRecursion()
result = solr.gcdOfStrings(str1, str2)

print("NULL" if result == "" else result)
