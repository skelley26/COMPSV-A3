# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next 
        return removed_node.value
    
    def peek(self):
        if self.top:
            return self.top.value 
        else:
            return None
        
    def print_stack(self):
        current = self.top
        if not current:
            print("Stack is empty")
            return
        while current:
            print(f"-{current.value}")
            current = current.next

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()
    #stores data here

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            redo_stack = Stack() #This took a while to get for some reason

            print(f"Action performed: {action}")
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            action = undo_stack.pop()
            if action is None:
                print("Nothing to undo.")
            else:
                redo_stack.push(action)
                print(f"undid action: {action}")
            

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            action = redo_stack.push()
            if action is None:
                print("No actions to redo.")
            else:
                undo_stack.pop(action)


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()
            
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()