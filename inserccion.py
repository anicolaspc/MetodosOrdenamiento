vec = [3, 8, 2, 1, 4, 2]
print(vec, end="   ")
print()
for i in range(0, len(vec)):
    for j in range(i, 0, -1):
        if(vec[j] < vec[j - 1]):
            aux = vec[j]
            vec[j] = vec[j - 1]
            vec[j - 1] = aux
            print(vec, end="   ")
            print(f"Hubo cambio en {vec[j]} y {vec[j - 1]}")
