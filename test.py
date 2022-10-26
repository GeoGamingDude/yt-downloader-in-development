import os
current_directory = os.getcwd()
end_directory = "\Downloads\Videos"
current_directory.replace("\dist", "")
end_directory = current_directory + end_directory
print(end_directory)