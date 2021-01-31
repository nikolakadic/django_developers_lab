from python_syntax import hello_world
from collections import deque

hello_world(2,3)


skup_1 = {1,2,3,4,5,6,66,6,6,6,6}

lista = [1,2,33,3,3,3,3,3,3]

skup_2 = set(lista)

tuple_1 = (1,2,3,4)

# tuple_1[2] = 5

print(skup_2)

stek = []

stek.append(4)

print(stek)

stek.pop()

red = deque([2,3,5,6,7])

red.append(5)

print(red.popleft())

# data types

dict_1 = {
    "name":"Nikola",
    "age":23
}

print(dict_1["age"])