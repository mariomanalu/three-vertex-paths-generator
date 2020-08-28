print("Welcome to the complete bipartite path generator program!")
def ask():
    answer = input("Would you like to know the definition of complete bipartite graph? [y/n]")

    if answer == "y":
        print("A complete bipartite graph is a bipartite graph where every vertex of the first set is adjacent to every vertex of the second set")
    elif answer == "n":
        pass
    else:
        print("Unknown command. Please enter y or n")
        ask()

ask()

def enter_size_of_sets_and_verify():
    size_of_first_set = int(input("Enter the number of vertices in the first subset: "))
    size_of_second_set = int(input("Enter the number of vertices in the second subset: "))

    if size_of_first_set + size_of_second_set < 3:
        print("There is no path of length three vertices in a graph of vertices less than 3")
        enter_size_of_sets_and_verify()
    else:
        pass

enter_size_of_sets_and_verify()

first_set = []
second_set = []
set_of_three_vertex_paths = []

for i in range(size_of_first_set):
    first_set.append("V" + str(i + 1))

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

print(set_of_three_vertex_paths)
print(len(set_of_three_vertex_paths))
