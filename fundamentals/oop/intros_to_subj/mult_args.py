def varargs(arg1, *args):
    print("Got ", arg1, " and ", args)
varargs("one") 			
# output: Got one and ()
varargs("one", "two") 	        
# output: Got one and ('two',)
varargs("one", "two", "three")  
# output: Got one and ('two', 'three')

# * the above, all except args 1, appear in a tuple. 
# * this happens when using an artisek and when the number
# * of args don't match the required parameters.

# * if you want to access them individually and outside a tuple

def varargs(arg1, *args):
    print(" ")
    print("for loop")
    for a in args:
        print(a)
varargs("one", "two", "three") 
# output: 
# two 
# three
# * the for loop goes through args hence why it does not display one