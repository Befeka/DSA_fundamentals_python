import random

def merge_sort(list):
    """
    Sort the imput list in ascending order
    Returns a new sorted list 
    Divide: Find the midpoint of the list and divide into sublists
    Concure: Recursively sort the sublists in the above step
    Combine: Merge the sorted list from the above step
    Takes O(n * log n) times
    Args:
        list (list): Unsorted list
    """
    
    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublist
    Takes =O( log n ) times
    Returns two sublists left, right
    Args:
        list (list): Unsorted list
        
    """
    
    midpoint = len(list) //2
    left = list[:midpoint]
    right = list[midpoint:]
    
    return left, right

def merge(left,right):
    """
    Merges two lists, sorting them in the process
    Takes O(n) times 
    Returns a new merged list 
    Args:
        left (list): left sublist
        right (list): right sublist
    
    """
    
    mlst = []
    l = 0
    r = 0
    
    while l < len(left) and r < len(right):
    
        if left[l] < right[r]:
            mlst.append(left[l])
            l += 1
        else:
            mlst.append(right[r])
            r += 1
            
    while l < len(left) :
        mlst.append(left[l])
        l += 1
        
    while r < len(right):   
        mlst.append(right[r])
        r += 1
        
    return mlst

def main():
    input_list = [random.randint(0, 200) for i in range(50)]
    
    sorted_list = merge_sort(input_list)
    print(verify(input_list))
    print(verify(sorted_list))
    
def verify(slist) :
    n = len(slist)
    if n < 2:
        return True
    
    return slist[0] <= slist[1] and verify(slist[1:])


if __name__ == "__main__":
    main()