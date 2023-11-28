class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, value):
        new_node = SLNode(value) 
        # * (JIM) starting with "Jim", new_node is set to the class SLNode with the arg of Jim
        # * (DWIGHT) new_node is set to SLNode. dwight is passed in so the value is dwight
        # * (ANDY) new_node is being set to Andy as it is passed in as the value.
        current_head = self.head
        # * (JIM) current_head being set to self.head which  is still None (line 8) since jim is our first
        # * (DWIGHT) since we had already ran this function with the value "Jim", we have jim as the current self.head.
        # * therefore when current_head is set to self.head it is referencing "Jim"
        # * (ANDY) current_head is being set to self.head. our previous value was "Dwight" so currently the self.head is 
        # * still dwight so current_head referrs to dwight
        new_node.next = current_head
        # * (JIM) new_node.next is set to current_head which is still None as stated above.
        # * (DWIGHT) new_node.next is being set to the current head. as said above, jim is our current_head.
        # * therefore "Jim" is being set to be referenced as the new_node.next. "Jim" is the new next
        # * (ANDY) new_node.next is being set to current head. as stated previously, "Dwight" is the current head
        # * therefore "Dwight" becomes the new new_node.next
        self.head = new_node
        # * (JIM) self.head is set to new_node which is currently holding the value of "Jim" and next as "None"
        # * (DWIGHT) self.head is being set to the new_node, new_node has the value of "Dwight".
        # * therefore dwight is the new self.head. output: Dwight Jim
        # * (Andy) self.head is being set to new_node. since we passed "Andy", "Andy" is the new self.head. output: Andy Dwight Jim
        return self
    
    def print_values(self):
        runner = self.head
        # * runner is self.head. with add_to_function being run being this print_values function,
        # * self.head refernces new_node which then references the class SLNode with attributes value and next
        while (runner != None):
            # * while loop, while runner does not equal none
            print(runner.value)
            # * display runner.value. This works because as stated above runner eventually leads to reference SLNode
            # * which containts attributes value and next hence why we can use dot notation with here to acces the value
            runner = runner.next
            # * we then set runner to equal runner.next so that the loop may continue.
            # * this is because there is only one value. as we did in the function above, everything else we set
            # * to the value next so its necessary for the runner to be set to next so the loop may run
            # * as stated for line 40, dot notation works here as runner eventually references SLNode which has the attributes
            # * value and next
        return self
    
    def add_to_back(self, value):
        if self.head == None:
            self.add_to_front(value)
            return self
        # * the above if loop is if the list were empty. 
        # * this would make it so that the back goes to the front.
        new_node = SLNode(value)
        # * (FUN) new_node is set to reference SLNode with "fun!" being passed in.
        runner = self.head
        # * (FUN) we current have "linked lists" as the value and "are" as the next
        # * so when we set  runner to self.head we are referencing "linked lists"
        while (runner.next != None):
            # * (FUN) as we start with self.head, runner.next is not empty
            # * (FUN) since we have "are" as our current next
            print(f'''
            runner.value: {runner.value}
            runner.next.value: {runner.next.value}
            ''')
            runner = runner.next
            # * (FUN) by then setting the runner as runner.next we are essentially
            # * setting runner to "are". this is so that the while loop may properly run
            # * as we go through the while loop to check if runner.next != None 
            # * when we've set our new runner to "are", we see that runner is None as there is 
            # * nothing currnely there.
        runner.next = new_node
        # * runner.next is currently none so by getting runner.next and setting it to new_node
        # * we are setting runner.next to reference ("fun!") which will in turn add "fun!" to the end of the list
        return self
    # output:
    # Andy
    # Dwight
    # Jim
    def remove_from_front(self):
        removed_value =  self.head.value
        self.head = self.head.next
        print(f"removed value: {removed_value}")
        print(f"new self.head: {self.head.value}")
        return self




my_list = SList()

my_list.add_to_front("Jim").add_to_front("Dwight").add_to_front("Andy").remove_from_front().print_values()
# my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").add_to_back("but take some getting used to").print_values()

# output:
# runner.value: Linked lists
# runner.next.value: are
            

# runner.value: Linked lists
# runner.next.value: are
            

# runner.value: are
# runner.next.value: fun!
            
# Linked lists
# are
# fun!
# but take some getting used to

# * NINJA BONUS: complete the remove_from_front method