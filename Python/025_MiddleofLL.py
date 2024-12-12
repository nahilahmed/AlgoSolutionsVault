class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle_of_linked_list(head):
    """
    Find the middle node of a singly linked list.
    If there are two middle nodes, return the second one.
    :param head: ListNode, the head of the linked list
    :return: ListNode, the middle node
    """
    curr = head
    node_count = 0
    while curr is not None:
        node_count += 1
        curr = curr.next

    if node_count == 1:
        return head
    
    middle_node = int(node_count/2 + 1)

    curr = head
    current_node_count = 0
    while curr is not None:
        current_node_count += 1
        if current_node_count == middle_node:
            return curr
        else:
            curr = curr.next
        

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
    # Edge case test inputs
    test_cases = [
        [],                          # Empty list
        [1],                         # Single node
        [1, 2],                      # Two nodes
        [1, 2, 3, 4, 5],             # Odd number of nodes
        [1, 2, 3, 4],                # Even number of nodes
        [7, 7, 7, 7, 7],             # All nodes with same values
        list(range(1, 1001)),        # Large list
    ]

    for i, values in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        head = build_linked_list(values)

        print("Input Linked List:")
        print_linked_list(head)

        middle_node = find_middle_of_linked_list(head)

        print("Middle Node:")
        if middle_node:
            print(middle_node.val)
        else:
            print("Linked list is empty.")
        print("-" * 40)