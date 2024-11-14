'''
Find the number of elements which are less than the median.
'''

arr = input()
l = list(map(int, arr.split(' ')))
print("Original list: "+ str(l))
l.sort()
print("Sorted list: "+ str(l))
mid = len(l) // 2
res = (l[mid] + l[~mid]) / 2
count = 0
for i in range(0, len(l)):
    if(l[i]<res):
        count += 1 

print("Number of less elements than median: "+ str(count))
