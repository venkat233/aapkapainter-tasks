# Write a code that prints out the first occurrence of a duplicate in a given array of integers
l = [1,2,3,2,1]
for i in range(1, len(l)):
    if l[i] in l[:i]:
        print(l[i])
        break