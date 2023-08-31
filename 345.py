# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels_charact = 'aeiouAEIOU'
#         vowels = str(vowels_charact)
#         cnt = 0
#         vol_cnt = 0
#         for char in s:
#             if char in vowels:
#                 cnt += 1
#         stop_num = cnt / 2 if cnt % 2 == 0 else (cnt - 1) / 2
#         list_s = list(s)
#         for i in range(len(s)):
#             if s[i] in vowels:
#                 for j in range(len(s)):
#                     if s[-(j + 1)] in vowels:
#                         temp = list_s[i]
#                         list_s[i] = list_s[-(j + 1)]
#                         list_s[-(j + 1)] = temp
#                         vol_cnt += 1
#                         if vol_cnt == stop_num:
#                             return ''.join(list_s)
#
#         return ''.join(list_s)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_char = "aeiouAEIOU"
        vowels = str(vowel_char)
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while s_list[left] not in vowels and left != right:
                left += 1

            while s_list[right] not in vowels and left != right:
                right -= 1

            temp = s_list[left]
            s_list[left] = s_list[right]
            s_list[right] = temp
            left += 1
            right -= 1

        return ''.join(s_list)





class Solution1:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        stack = [c for c in s if c in vowels]
        result = []

        for c in s:
            if c in vowels:
                result.append(stack.pop())
            else:
                result.append(c)

        return ''.join(result)





s = "leetcode"
sol = Solution1()
result = sol.reverseVowels(s)
print(result)

