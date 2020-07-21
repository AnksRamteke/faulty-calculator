# set - it only retains unqiue value and neglect duplicate value

s = set()
# print(type(s))

# s_from_list = set ([1,2,3,4,6])
# print(type(s_from_list))

# s.add(1)
# s.add(1)
# s.add(2)
# print(s)

# s.add(1)
# s.add(2)
# s1 = s.union({1,2,3})
# print(s)


# s.add(1)
# s.add(2)
# s1 = s.intersection({1,2,3})
# print(s,s1)

# print(len(s))

# print(type(s))

# print(min(s))
# print(max(s))



s.add(1)
s.add(2)
s1 = {4,6}
print(s.isdisjoint(s1))