word1 = "ab"
word2 = "pqrst"
result = ''

for i in range(min(len(word1), len(word2))):
    result += word1[i]
    result += word2[i]
if len(word1)>len(word2):
    result += word1[i+1:]

if len(word1)<len(word2):
    result += word2[i+1:]