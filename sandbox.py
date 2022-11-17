

#____________________________________________________________________________________

# import os, sys
# targetFile = open('List.txt', 'w')
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         targetFile.write(os.path.join(root, name).replace('\\', '/').replace('./', '')+chr(13))
# targetFile.close()

# import os #os module imported here
# location = os.getcwd() # get present working directory location here
# counter = 0 #keep a count of all files found
# csvfiles = [] #list to store all csv files found at location
# filebeginwithhello = [] # list to keep all files that begin with 'hello'
# otherfiles = [] #list to keep any other file that do not match the criteria

# for file in os.listdir(location):
#     try:
#         if file.endswith("aaa"):
#             print ("py file found:\t", file)
#             csvfiles.append(str(file))
#             counter = counter+1

#         elif file.startswith("te") and file.endswith(".py"): 
#             print ("csv file found:\t", file)
#             csvfiles.append(str(file))
#             counter = counter+1

#         elif file.startswith("DZ"):
#             print ("DZ files found: \t", file)
#             filebeginwithhello.append(file)
#             counter = counter+1

#         else:
#             otherfiles.append(file)
#             counter = counter+1
#     except Exception as e:
#         raise e
#         print ("No files found here!")

# print ("Total files found:\t", counter)




# import os, sys
# targetFile = open('List.txt', 'w')
# targetFile2 = open('List2.txt', 'w')

# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         if '2' in name:                                     # поиск в имени
#             targetFile2.write(os.path.join(root, name).replace('\\', '/').replace('./', '')+chr(13))
#         targetFile.write(os.path.join(root, name).replace('\\', '/').replace('./', '')+chr(13))
# targetFile.close()
# targetFile2.close()

# import os, sys
# targetFile = open('List.txt', 'w')
# a = []

# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         if 'DZ' in name:                                     # первая очередь
#             a.append(os.path.join(root, name))
#         elif '62' in name:                                  # вторая очередь
#             a.append(os.path.join(root, name))
#         else:
#             a.append(os.path.join(root, name))

# print(*a, file=targetFile, sep="\n")
# targetFile.close()




n = 5678
print(n // 10 % 10)

