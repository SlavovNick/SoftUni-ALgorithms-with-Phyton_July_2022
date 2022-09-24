def reverse_array(a, z, array):
    if a == z or a  > z  or z  < a :
        return
    array[a], array[z] = array[z], array[a]
    reverse_array(a + 1 , z - 1 , array)

array = [int(x) for x in input().split()]
reverse_array(0, len(array)- 1, array)
print(*array, sep=' ')