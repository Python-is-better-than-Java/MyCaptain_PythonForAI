# Displaying all positive numbers in a list
n = int(input("Enter number of terms: "))
listin = []
listout = []
for i in range(0, n):
    listin.append(int(input("Enter list element " + str(i + 1) + ": ")))
print(listin)

for j in range(0, n):
    if (listin[j] > 0):
        listout.append(listin[j])
print(listout)
