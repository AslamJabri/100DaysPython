Dictionaries 
It is very similar to the actual dictionary where it is like key value pairs.
   dict =  {"key":"value","key2":"value2"}
The accessing of values is somewhat similar to list
    print(dict["key"])
for addiding a item into dict programatically and this can also be used for editing the entry in dictionary
    dict["new value"]="This is a new value"
we can also wipe the dictionary
    dict = {}
for creating empty dictionary
    dict = {}
looping in dictionary
    for key in dict:
        print(key)#this gives us the keys in dictionary
        print(dict[key])#gives the value in the dictionary