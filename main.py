list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

odd_list = []
list3 = []


def odd_number():
    for i in list1:
        if i % 2 == 1:  # Use the modulo operator to check for odd numbers
            odd_list.append(i)

def even_number():
    list3.extend(list2[1::2])
    return list3

odd_number()
even_number()

print("Odd Numbers :", odd_list)
print("Even Numbers :", list3)
print("Final List :", odd_list+list3)