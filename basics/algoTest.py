'A simple list/ array sorting algo'

alist = [int(x) for x in input("enter numbers separated by ',': ").split(",")]
'''
- leave the first element in its position
- loop iterate from second element (range(1,end_of_list))
- i is usd to traverse the list and j for grabbing elements. 
- switch positions if the left element is greater than j ([j-1], [i] = [i], [j-1])
- increment j
- good idea to make sure that the element grabber j is > 0. Add to while loop if necessary. 
'''
def sort(some_list):
    for i in range(1,len(some_list)):
        j = i
        while some_list[j-1] > some_list[j] and some_list[j-1]>0 :
            some_list[j-1],some_list[j] = some_list[j], some_list[j-1]
            j = j-1
    return some_list

'return min value'
def min(some_list):
    return f'The minimum value is {some_list[0]}'

'return max value'
def max(some_list):
    return f'The maximum value is {some_list[-1]}'

print(alist)
print(sort(alist))
print(min(alist))
print(max(alist))