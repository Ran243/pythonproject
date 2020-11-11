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


lst = ["1" , "22", "1", "233", "44344", "34343", "22"]
unique(lst)