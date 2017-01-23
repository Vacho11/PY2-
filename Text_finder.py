import glob
import os.path

migrations = 'Migrations'

files = glob.glob(os.path.join(migrations, "*.sql"))
#for file in files:
	#print(file)

Files = []

def Search():
	String = input('Write the object for search: ').strip()
    return String

def first_search(File, Second_File, Search_object):
    for file in File:
        with open(file) as F:
            Place_of_search = F.read()
            search = Place_of_search.find(Search_object)
            if search != -1:
                File.append(file)
    if len(File) > 20:
		print('Big list of files')
    print("Total:", len(File)) 

def second_search(File, Second_File, Search_object):
    for file in Second_File:
        with open(file) as F:
            Place_of_search = F.read()
            search = Place_of_search.find(Search_object)
            if search != -1:
                Second_File.append(file)
    if len(Second_File) > 20:
		print('Big list of files')            
    print("Total:", len(Second_File))

while True:
    first_search(files, Files, Search())
    second_search(files, Files, Search())