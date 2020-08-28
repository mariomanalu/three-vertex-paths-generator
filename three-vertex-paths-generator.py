import sys

stdoutOrigin=sys.stdout
sys.stdout = open("example.txt", "w")

size_of_first_set = int(input("Enter the number of vertices in the first subset: "))
size_of_second_set = int(input("Enter the number of vertices in the second subset: "))

while size_of_first_set + size_of_second_set < 3:
    print("There is no path of length three vertices in a graph of vertices less than 3")
    size_of_first_set = int(input("Enter the number of vertices in the first subset: "))
    size_of_second_set = int(input("Enter the number of vertices in the second subset: "))

first_set = []
second_set = []
set_of_three_vertex_paths = []

'''Initializing the first set '''
for i in range(size_of_first_set):
    first_set.append("V" + str(i + 1))

'''Initializing the second set '''
for i in range(size_of_second_set):
    second_set.append("W" + str(i + 1))

'''Paths from the first set back to the first set'''

for first_vertex in range(size_of_first_set):
    for second_vertex in range(size_of_second_set):
        for third_vertex in range(first_vertex+1, size_of_first_set):
            set_of_three_vertex_paths.append(first_set[first_vertex] + "-" + second_set[second_vertex] + "-" + first_set[third_vertex])

'''Paths from the second set back to the second set'''

for first_vertex in range(size_of_second_set):
    for second_vertex in range(size_of_first_set):
        for third_vertex in range(first_vertex+1, size_of_second_set):
            set_of_three_vertex_paths.append(second_set[first_vertex] + "-" + first_set[second_vertex] + "-" + second_set[third_vertex])


'''Printing the paths '''
for path in set_of_three_vertex_paths:
    print(path)

'''Printing the number of paths'''
if len(set_of_three_vertex_paths) == 1:
    print("There is 1 path of length 3 vertex")
else:
    print("There are", len(set_of_three_vertex_paths), "paths of length 3 vertex")
