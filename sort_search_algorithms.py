import random
def is_sorted(nums_to_search):
    for index in range(len(nums_to_search)-1):
        if nums_to_search[index] > nums_to_search[index + 1]:
            return False
    return True

def bogo_sort(nums_to_search):
    """
    bogo _sort method : shuffle numbers till the numbers
    are sorted
    Return sorted numbers in ascending order
    Args:
        nums_to_search (list): numbers to be sorted
    """
    while not is_sorted(nums_to_search):
        random.shuffle(nums_to_search)

    return(nums_to_search)

def selection_sort(nums_to_search):
    """_summary_

    Args:
        nums_to_search (lists): List of random numbers to sort
    """
    sorted_numbers = []
    for i in range(len(nums_to_search)):
        index_min_to = index_min(nums_to_search)
        sorted_numbers.append(nums_to_search.pop(index_min_to))
        print("%-45s %-25s" % (nums_to_search, sorted_numbers))
    
    return sorted_numbers
    
def index_min(nums_to_search):
    
    min_num = 0
    for i in range(len(nums_to_search)):
        if nums_to_search[i] < nums_to_search[min_num] :
            min_num = i
    
    return min_num   

def recursion(nums_to_sum):
    """
    Recursion algorithm: in this example perform recurrion sum
    """
    if not nums_to_sum:
        return 0
    print("Calling sum(%s)" % nums_to_sum[1:])
    remaining_recursion = recursion(nums_to_sum[1:])
    print("Call to sum(%s) returning %d + %d " %(nums_to_sum,nums_to_sum[0] , remaining_recursion))
    return nums_to_sum[0]+ remaining_recursion
    
def merge_sort(nums_to_search):
    if len(nums_to_search) <= 1:
        return nums_to_search
    
    # split numbers into half
    mid_number = len(nums_to_search)//2
    left_half = nums_to_search[:mid_number]
    right_half = nums_to_search[mid_number:]
    
    left_values = merge_sort(left_half)
    right_values = merge_sort(right_half)
    
    left_index = 0
    right_index = 0
    sorted_values = []
       
    #print("%15s %-15s" % (left_values,right_values))
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
     
    while  left_index < len(left_values):
        sorted_values.append(left_values[left_index])
        left_index +=1
            
    while right_index < len(right_values):
        sorted_values.append(right_values[right_index])
        right_index += 1
           
    return sorted_values
    
def quick_sort(nums_to_search):
    
    if len(nums_to_search) <= 1:
        return nums_to_search
    
    pivot = nums_to_search[0]
    less_than_pivot = []
    greater_than_pivot = []
    
    for val in nums_to_search[1:]:
        if val <= pivot:
            less_than_pivot.append(val)
        else :
            greater_than_pivot.append(val) 
     
    #print("%15s %1s %-20s" % (less_than_pivot,pivot, greater_than_pivot))      
    return quick_sort(less_than_pivot)  + [pivot] + quick_sort(greater_than_pivot)

def main():
    algo_type = int(input("Enter sort _agoritm : "))
    nums_to_sort_search = [random.randint(0, 100)  for _ in range(10)]
    
    fun_map = {1 : bogo_sort,
               2 : selection_sort,
               3 : recursion,
               4 : merge_sort}
    result =(fun_map.get(algo_type,quick_sort)(nums_to_sort_search))
    
if __name__=="__main__":
    main()