# three-vertex-paths-generator
This repo contains a Python script that finds all three vertex paths in a complete bipartite graph.

# Code background
I applied for a research project in the field of Extremal Graph Theory. One of the requirement was to answer the following question: **What is the maximum number of three vertex path in a bipartite graph of size n?**

My strategy was first to draw a couple of complete bipartite graph of different sizes and write out the three vertex paths. As the size of the graph grows, I was more prone to mistakes. So, I wrote this python script to automate the task of generating all three vertex paths given a graph of size n. This is the genesis of my fondness of Python.

# Assumption
1. This Python script assumes that the paths of the form V1-W1-V2, where V1 and V2 are two arbitrary vertices of a set and W1 is an arbitrary vertex of the other set, is the same as the paths of the form V2-W1-V1.

2. This Python script also assumes that the number of vertices is at least 3, which I think is a sensible assumption since any graph of vertices less than 3 has no path of length 3 vertex trivially.

3. I define path as walk that does not visit one or more vertices more than once. Therefore, V1-W1-V1 is not path, by this definition.

# Definitions
1. Complete bipartite graph: bipartite graph where every vertex of the first set is adjacent to every vertex of the second set

#Runtime
Each of three nested for loop in line 26 - 29 has to go over a list, which takes up **n** time for each for loop. Therefore, ***O(n^3)***
