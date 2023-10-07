"""
# even and odd number tast by using method

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
"""
"""
#same task by using data structures

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

res = list()

odd_numbers = list1[1::2]
even_numbers = list2[0::2]

print("odd numbers",odd_numbers)
print("even numbers", even_numbers)

res.extend(odd_numbers)
res.extend(even_numbers)

print(res)
"""
"""
#data structure task 3
list = [34, 54, 67, 89, 11, 43, 94]

print("remove element index 4 in the list")
list.pop(4)
print(list)

print("adding element to index 2")
list.insert(2, 11)
print(list)

print("adding element to last")
list.append(11)
print(list)
"""
'''
#slice list and reverse
list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_1 = list[0:3]
chunk_1_reverse = chunk_1[::-1]

chunk_2 = list[3:6]
chunk_2_reverse = chunk_2[::-1]

chunk_3 = list[6:]
chunk_3_reverse = chunk_3[::-1]

print("Chunk 1",chunk_1)
print("After reversed",chunk_1_reverse)

print("Chunk 2",chunk_2)
print("After reversed",chunk_2_reverse)

print("Chunk 3",chunk_3)
print("After reversed",chunk_3_reverse)

'''
'''
#othes way to slice the list
list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

length = len(list)
x  = int(length/3)
start = 0
end = x

for i in range(3):
        
    index = slice(start, end)

    new_list = list[index]

    print("chunk", i, new_list)

    print("reversed", list(reversed(new_list)))

    start = end
    end += x

'''
def yes(name : str, age: int):
    print(name, age)

yes("buddhika", 23)


def demo(*xyz):
    for i in xyz:
        print(i)

demo(1,2,3)

class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self,capacity):
        return f"the seating capacity of {self.name} is {capacity} passengers"
    
class bus(vehicle):
    def seating_capacity(self, capacity):
        return super().seating_capacity(capacity = 50)