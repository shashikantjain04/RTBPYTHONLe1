import re

new = ["test, she said ABC" ]

print (new)
new1 = re.sub('[A-Z]','', str, new)

print (new1)

