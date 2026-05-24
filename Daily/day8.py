# code 

# reusable functions, variables

# Main Program = script
# Program from which functions are being imported = module

# import example:

# from day6 import numbers, largest number

# In above example, day 6 is the module, and this file i.e., day8.py is the script

####################################################

print("name of file", __name__) # if i run this file, it will say: "name of file __main__" #### if i run 

if __name__ == "__main__":    # name is a variable but not user defined. It is a special varibale defined by python
    print(" this file is running direcly")
else:
    print("this file is running due to import in another main file")