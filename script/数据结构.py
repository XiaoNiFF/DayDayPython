vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
[x*y for x in vec1 for y in vec2]

[vec1[i]*vec2[i] for i in range(len(vec1))]