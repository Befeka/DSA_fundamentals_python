def linear_search(lst, target):
    """
    Return the index position of the target
    if target is found ,else return none
    """
    for i in range(len(lst)):
        
        if lst[i] == target:
            return i
        
    return None
    
def verify(index):
    if index is not None:
        print("Target found at index ", index)
    else:
        print("Target is not in list")
        
def main():
    target = 16
    numbers = [b for b in range(50)]
    print(numbers)
    index = linear_search(numbers, target)
    print(index)
    verify(index)
    
    
if __name__ == "__main__":
    main()