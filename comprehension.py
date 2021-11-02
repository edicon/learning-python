# This Python file uses the following encoding: utf-8
'''
list comprehension
'''

# set: no order, unique value
d1={'1','2','3'}
d2={'one','two','three'}
# un ordered, 실행할 때마다, 순서(order) 다름
print(d1, d2)
# list: order
# d1=['color','shape','fruit']
# d2=['red','circle','apple']

z = zip(d1, d2)
print(z)

for k,v in z:
  print(k,v)

d3={k:v for (k,v) in zip(d1,d2)}
print (d3)
# Output: {'fruit': 'circle', 'shape': 'red', 'color': 'apple'}
