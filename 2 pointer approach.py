m = ["ankit", "mohit", "arpit", "shobhit"]
n = []
i = 0
j = len(m) - 1

while i <= j:
    if i == j:
        n.append(m[i][::-1])    # append the reversed middle element
    else:
        n.append(m[i][::-1])    # append the reversed first element
        n.append(m[j][::-1])    # append the reversed last element
    i += 1
    j -= 1

print(n)
