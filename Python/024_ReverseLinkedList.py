class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list.
    :param head: ListNode, the head of the linked list
    :return: ListNode, the new head of the reversed linked list
    """
    # Placeholder for your implementation
    prev = None
    curr = head
    post = curr.next

    if post is None:
        return head
    
    while post is not None:
        if curr != head:
            post = curr.next
        
        curr.next = prev
        prev = curr
        curr = post

    new_head = prev

    return new_head
    
    

def print_linked_list(head):
    """
    Utility function to print the linked list.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print("->".join(map(str, result)))

def build_linked_list(values):
    """
    Utility function to create a linked list from a list of values.
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    # Example usage
    values = [1, 2, 3, 4, 5]  # Example linked list
    head = build_linked_list(values)

    print("Original linked list:")
    print_linked_list(head)

    # Call the reverse function
    reversed_head = reverse_linked_list(head)

    print("Reversed linked list:")
    print_linked_list(reversed_head)