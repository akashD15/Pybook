'''
Find the number of elements which are less than the average.
'''
arr = input()
l = list(map(int, arr.split(' ')))
print("Original list: "+ str(l))
l.sort()
print("Sorted list: "+ str(l))
avg = sum(l)/len(l)
count = 0
for i in range(0, len(l)):
    if(l[i]<avg):
        count += 1 

print("Number of less elements than average: "+ str(count))
