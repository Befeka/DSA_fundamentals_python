def binary_search(lst, target):
    """ Returns the index of target
    from the input sorted list 
    if present or returns none using 
    binary search algorithm"""
    
    
    first = 0 
    last = len(lst) - 1
        
    while first <= last:
        mid_point = (first + last)//2
        if target == lst[mid_point]:
            return mid_point
        elif lst[mid_point] < target:
            first = mid_point  + 1
        else :
            last = mid_point - 1
            
    return None

def verify(index):
    if index is not None:
        print("Target is found at index : ", index)
    else :
        print("Target is not present in the list")
        

def main():
    target = 0
    
    numbers = [nums for nums in range(50)]
    
    index = binary_search(numbers, target)
    
    verify(index)
    
if __name__== "__main__":
    main()