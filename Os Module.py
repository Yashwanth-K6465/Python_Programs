import os

#List present working directory
print(os.getcwd())   

#List the directories
print(os.listdir(r'C:\Users\ky\Desktop\Test'))

#Changing the directory
os.chdir(r'C:\Users\ky\Desktop\Test')
print(os.getcwd())

#Method to call only specific extension files from a directory
for root,directory,files in os.walk(os.getcwd()):
    for f in files:
        if '.csv' in f:
            print(f)
            
#Method to call all file starting with specific character
for root,directory,files in os.walk(os.getcwd()):
    for f in files:
        if f[0]=='Z' or f[0]=='N':
            print(f)

#Method to call all the file along with their location
for root,directory,file in os.walk(os.getcwd()):
    for f in file:
        if '.txt' in f:
         print(root+'\\'+f)

'''Arguments used along with os.walk(): 
                 os.walk(top, topdown=True, onerror=None, followlinks=False)
1) top: This is the root directory from which the walk begins. It's a string representing the path to the starting directory.
2) topdown (Optional, Default: True): This boolean parameter controls the order in which directories are visited.
      True: The walk starts at the top directory and visits its subdirectories recursively (pre-order traversal). This is the default.
      False: The walk visits subdirectories first and then the top directory (post-order traversal).
3) onerror (Optional, Default: None): This is a function that will be called if an error occurs during the walk (e.g., permission denied). 
   The function receives an OSError instance as its argument. If onerror is None, the walk will continue, but the error will be reported.
4) followlinks (Optional, Default: False): This boolean parameter determines whether symbolic links to directories should be followed.
    True: Symbolic links to directories will be followed, meaning the walk will enter the linked directory.
    False: Symbolic links to directories will be ignored.   
'''
            
#To create a Directory/Directories
os.makedirs('Hello')
os.makedirs('A/B/C/D')

#To remove directory/directories
os.removedirs('Hello')
os.removedirs('A/B/C/D')

#To execute unox/shell script
os.system("./my_script.sh")

#To check if directory/file exists in current working directory
print(os.path.exists(r'C:\Users\ky\Desktop\Test'))
print(os.path.isfile(r"C:\Users\ky\Desktop\Test\Nolan Performance testing\View Results Tree.jmx"))
print(os.path.isdir(r"C:\Users\ky\Desktop\Test\Nolan Performance testing"))

#To get the environment variables
print(os.environ.get('PATH'))

#This will return the absolute path of the file
abs_path = os.path.abspath("my_file.txt")
print(abs_path) # Output: /current/working/directory/my_file.txt

#This will return base name from the path
filename = os.path.basename("/path/to/my_file.txt")
print(filename)  # Output: my_file.txt

# A dictionary-like object that provides access to environment variables
home_dir = os.environ.get("HOME")  # Get the HOME environment variable (Unix-like)
path_var = os.environ.get("PATH")
print(home_dir)
print(path_var)

#To print the name of the operating system
print(os.name)

# This will split the file with root and extensions seperately 
path=r"C:\Users\ky\Desktop\Python Practise"
for file in os.listdir(path):
    print(os.path.splitext(file))
    
# Extracts the directory part of a path
dirname = os.path.dirname("/path/to/file.txt") # Output: /path/to

# To joinng multiple paths
path = r"\Users\ky\Desktop\Helaoe\jELE"
path1 = r"Python Practise"

combined_path = os.path.join("C:", path1, path[1:]) #path[1:] removes the first \
print(combined_path) # Output : C:\Python Practise\Users\ky\Desktop\Helaoe\jELE
