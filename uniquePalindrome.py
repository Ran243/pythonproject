def unique(y): 
      
    # insert the list to the set 
    list_set = set(y) 
    # convert the set to the list 
    
    for x in list_set: 
        reverseString = reversed (x)
        if list(x) == list(reverseString):
            print (x)
        else:
            continue

file_content = "akdfadskj snns racecar ada"

x = file_content.split()
unique(x)


