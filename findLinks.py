import re

#p = re.compile(r'<[a-z]+\s.*href="(http.*)">')
p = re.compile(r'<[a-z]+\s[^>]*href="(http[^>]*)">')
with open("FSTTCSAP.html","r") as f:
  ls = f.read()
  m = p.finditer(ls)
  for x in m:
    print(x.group(1))

