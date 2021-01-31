with open('newfile.txt','w') as file_object:
    file_object.writelines('Test')

file_object = open('newfile2.txt','w')

file_object.writelines('testtest')

file_object.close()

# JS OBJECT NOTATION


import json

print(json.dumps(['Welcome', "to", "GeeksforGeeks"])) 

