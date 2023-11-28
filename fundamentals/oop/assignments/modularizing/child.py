import parent
# * with this import alone.. if we run python3 child.py
# * the imported file runs
# output:
# 25
# Anna
# hello
# print(locals())
# * Namespace refers to which variables, functions, 
# * and classes are accessible to us at any given time during a program’s execution
# * see what variables are in your current namespace

# * print(__name__) with this on the parent and running child.py
# output:
# parent

# * with 
# * if __name__ == "__main__":
# *    print("the file is being executed directly")
# * else:
# *    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
# * in the parent.py part of the import
# output:
# The file is being executed because it is imported by another file. The file is called:  parent
