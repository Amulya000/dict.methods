# book={
# 1: "python programming",
# 2: 'core pythone programming',
# 3.4: 'advance python programing',
# 'p': "python"
# }
# print(book[1])
# print(book['p'])
# print(book[33])

# h={1: 2, 2:3.3, 3: "python", 4: (2,3),5: {5,6}, 6:[2,3],7: "", 8: {1: "python"}}
# print(h[1],type(h[1]))
# print(h[2],type(h[4]))
# print(h,type(h))
# print(h.keys())
# print(h.values())
# print(h.items())

# h={1:"", 2:"python", 3:7, 4:6.2, 5:[1,4], 6:(2,3), 7:{1,2}, 8:{3: "world"}}
# print(h.get(2))
# print(h.get(10))
# print(h[10])
# h.pop(2)
# print(h)
# h.popitem()
# print(h)


# h={1:"", 2:"python", 3:7, 4:6.2, 5:[1,4], 6:(2,3), 7:{1,2}, 8:{3: "world"}}
# h.clear()
# print(h)
# a=[1,2,3,4,5]
# print(dict.fromkeys(a,'pass'))


# h={1:"", 2:"python", 3:7, 4:6.2, 5:[1,4], 6:(2,3), 7:{1,2}, 8:{3: "world"}}
# h.update({3: 'hi'})
# print(h)
# h.update({10: 2})
# print(h)
# h.setdefault(3,5)
# print(h)
# h.setdefault(10,'hi')
# print(h)