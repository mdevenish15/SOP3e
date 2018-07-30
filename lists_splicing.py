numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# splice a section from the list
splice1 = numbers[2:6]
print(splice1)

# splice from beginning
splice2 = numbers[:5]
print(splice2)

# splice from end
splice3 = numbers[7:]
print(splice3)

# splice with steps
splice4 = numbers[1:5:2]
print(splice4)

# copy list
splice5 = numbers[:]
print(splice5)

# splice list from end of list
splice6 = numbers[-3:]
print(splice6)