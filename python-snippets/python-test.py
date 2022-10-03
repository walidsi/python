x = 'abcdef'
i = 'a'

# while i in x[:1]:
#     print(i)


def list_skills(val, list=[]):
    list.append(val)
    return list

list1 = list_skills('Node')
list2 = list_skills('java', [])
list3 = list_skills('React')

print('%s' % list1)
print('%s' % list2)
print('%s' % list3)

array1 = [1,2,3,4,5]
array2 = array1
array2[0] = 0
print(array1)

l=[1,2,3,4,5]
m = map(lambda x: x**2, l)
print(list(m))

class Welcome:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Welcome to ', self.name)

cw = Welcome('Turing')
cw.say_hello()

# 'The {} side {1} {2}'.format('bright', 'of', 'life')

l1 = [1,2,3,4]
l2 = [5,6,7]

result = l1.append(l2)
print(result)

print([i.lower() for i in 'TURING'])

array = ['Welcome', 'To', 'Turing']
print('-'.join(array))

inputs = ['NodeJs', 'React', 'Java']

# for i in inputs:
#     inputs.append(i.lower())

# print(inputs)

skills = ['Node', 'React', 'Python', 'Vue']
skills.insert(3, 'C')
print(skills)

data = [1, 2, 3, 4, 5]
data.pop()
print(data)
data.pop(2)
print(data)

d = {40: 'john', 50:'hatem'}
print(d)

print('Welcome to TURING'.capitalize())

