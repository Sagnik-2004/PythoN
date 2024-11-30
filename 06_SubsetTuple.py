def subsets(s):
    n = len(s)
    result = []
    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i // (2 ** j)) % 2 == 1:
                subset.append(s[j])
        result.append(subset)
    return result

myList=(2,4,6,8)

sbts=subsets(myList)

# Print all subsets
print("All subsets:")
for subset in sbts:
    print(subset)
