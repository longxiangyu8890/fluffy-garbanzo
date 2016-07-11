def need_swap(var1, var2):
    if var1 > var2:
        return True
    return False

def swap(var1, var2):
    print "swap"
    tmp = var1
    var1 = var2
    var2 = tmp

array = [6, 7, 3, 8, 9, 1, 0]
# len - 1 bubble
for i in range(1, len(array)):#n-1 travers is ok
    for j in range(0, len(array)-i):#one traverse
        if need_swap(array[j], array[j + 1]):
            #swap(array[j], array[j + 1] )
            tmp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = tmp
    print "sort ",i,"array is :", array

print "the last array is :", array
