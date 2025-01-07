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

