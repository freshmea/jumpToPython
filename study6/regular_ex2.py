import re

p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p.sub('\g<phone> \g<name>', 'park 010-1234-1234'))

s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())       # greedy
print(re.match('<.*>', s).group())
print(re.match('<.*?>', s).group())     # non-greedy
print(re.match('<.+?>', s).group())     # non-greedy
# print(re.match('<.??>', s).group())     # non-greedy
# print(re.match('<.{1,2}}>', s).group())     # non-greedy

p = re.compile('.+(?=:)')
m = p.search('http://google.com')
print(m.group())

