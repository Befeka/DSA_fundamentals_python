def recursive_binary_search(lst,target):
    """Returns true if the target is 
     is in the list otherwise returns false 
     using recursive method"""
     
    if len(lst) == 0 :
        return False
    else:
        mid_point = len(lst)//2
        if lst[mid_point] == target:
            return True
        
        if lst[mid_point] > target :
            return recursive_binary_search(lst[:mid_point],target)
        else:
            return recursive_binary_search(lst[mid_point +1:],target)
    
def verify(result):
    print("Target found : ", result)
    
def main():
    
    target = 55

    numbers = [num for num in range(50)]

    result = recursive_binary_search(numbers,target)
    verify(result)
if __name__ == "__main__":
    main()