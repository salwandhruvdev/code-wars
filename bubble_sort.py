'''

'''
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

n = int(raw_input().strip()) #get rid of end spaces
a = map(int, raw_input().strip().split(' '))
counter = 0
sorted_list = sorted(a)
while a != sorted_list:
    for i in xrange(0,len(a)-1):
        if a[i] > a[i+1]:
            swap(a, i, i+1)
            counter += 1
print ("Array is sorted in {} swaps.".format(counter))
print ("First Element: {}".format(a[0]))
print ("Last Element: {}".format(a[len(a)-1]))
