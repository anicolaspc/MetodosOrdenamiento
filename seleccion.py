vec = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(vec, end="   ")
print()
for i in range(0, len(vec) - 1):
    print()
    aux1 = i
    for j in range(i + 1, len(vec)):
        if vec[i] > vec[j]:
            i = j
    aux = vec[i]
    vec[i] = vec[aux1]
    vec[aux1] = aux
    print(vec, end="   ")
    print(f"hubo cambio entre {vec[i]} y {vec[aux1]}")

print()
print(vec, end="   ")
