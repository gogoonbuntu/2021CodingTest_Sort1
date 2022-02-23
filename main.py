N, K = input().split()

arrayA = sorted(list(map(int, input().split())))
arrayB = sorted(list(map(int, input().split())), reverse=True)
print(arrayA, arrayB)
for i in range(int(K)):
	arrayA[i] = arrayB[i]

print(sum(arrayA))