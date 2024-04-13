import random
from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide a s linked list into
      sublist containing a single node
    - Repeatedly merge the sublists to produce 
      sorted sublist until one remains
    
    Returns sorted linked list
    Runs in O(kn log n) times 
    Args:
        linked_list (node): linked list object
    """
    
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list 
    
    l_half, r_half = split(linked_list)
    left = merge_sort(l_half)
    right = merge_sort(r_half)
    
    return merge(left,right)

def split(lk_list):
    """
    Divide the unsorted list at midpoint into sublists
    Return sublists 
    Runs in O(log n)

    Args:
        linked_list (Node): unsorted linked list
    """
    if lk_list == None or lk_list.head == None:
        left_half = lk_list
        right_half = None
        
        return left_half,right_half
    else :
        size = lk_list.size()
        mid = size//2
        mid_node = lk_list.node_at_index(mid-1)
        left_half = lk_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half,right_half 
        
def merge(left,right):
    """
    Merges to linked lists,sorting data in the nodes
    Retuns a new, merged list
    Runs in O(n)
    Args:
        left (linked list): left half of splited linked list
        right (linked list): right half of splited linked list
    """
    # Create a new linked list that contains nodes from
    # merging left and right
    merged = LinkedList()
    
    # Add a fake head that is discarded later
    merged.add(0)
    
    # Set current to the head of the linked list
    current = merged.head
    
    # Obtain head nodes for left and right linked lists 
    left_head = left.head
    right_head = right.head
    
    while left_head or right_head:
        # If the head node of the left is NOne, we're past the tail
        # Add the tail node from the right to merged linked list 
        if left_head is None :
            current.next_node = right_head
            # Call next on the right to set loop condition to False
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on the left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node Obtain node data to perform comparision operations 
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on the right is less than or equalleft, set current to right node
            else :
                current.next_node = right_head
                # Move current to next node
                right_head = right_head.next_node
        # Move current to the next node
        current = current.next_node   
        # Discard fake head and set firts merged node as head     
    head = merged.head.next_node
    merged.head = head 
    
    return merged

def main() :
    l = LinkedList()
    [l.add(random.randint(0, 200)) for i in range(10)]
    print(l)
    sorted_linked_list = merge_sort(l)
    print(sorted_linked_list)
    
if __name__ == "__main__":
    main()
    
