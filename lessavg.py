'''
Find the number of elements which are less than the average.
'''
n = int(input())
arr = input()
l = list(map(int, arr.split(' ')))
count = 0
avg = sum(l)/len(l)
for i in range(0,len(l)):
    if(l[i]<avg):
        count += 1
        
print (count)
