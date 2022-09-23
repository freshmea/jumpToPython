# .^$*+?{}[]/|() 정규표현식의 메타문자
# [a-c] = [abc]
# [a-z] = [abcdefghijklmnopqrxtuwyz]
import re
p = re.compile('ab*')
p = re.compile('[a-z]+')
m = p.match("python")
print(m)
m = p.match("3 python 3")
print(m)
m = p.search("python")
print(m)
m = p.search("3 python 3")
print(m)
m = p.findall("life is too short")
print(m)
m = p.finditer("life is too short")
print(m)
for i in m:
    print(i.group())