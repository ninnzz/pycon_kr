#
# Language quirks, anti patterns
#

## Dictionary merging
a = {'name': 'john', 'age': 25}
b = {'weight': 55, 'height': 160}
c = {**a, **b}
print(a)
print(b)
print(c)

## Else on for loop
# Usual implementation
chars = ['a', 'b', 'c', 'd', 'e', 'f']
look_for = 'n'
found = False

for c in chars:
    if look_for == c:
        print('Found you!')
        found = True
        break
if not found:
    print('Not found "{}"'.format(look_for))

# Use Else
for c in chars:
    if look_for == c:
        print('Found you!')
        break
else:
    print('Not found "{}"'.format(look_for))

## Avoid using map(), filter(), etc
num = [1, 2, 3]
doubles = map(lambda x: x * 2, num)

num = [1, 2, 3]
doubles = [x * 2 for x in num]