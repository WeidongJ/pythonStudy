import pickle

d = dict(name='bob', age=20, score=88)
print(d)
print(pickle.dumps(d))
# with open('dump.txt', 'wb') as f:
#     pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    print(pickle.load(f))

print(ord("A"))
print(chr(65))
