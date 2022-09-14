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

Nesting in Dictionaries and list
Nesting is like putting folders into one folder.
    travel_log = {
        "France" : ["Paris","Lille","Dijon"],#dictionary in a list
        "Germany": ["Berlin","Hamburg","Stuttgart"]
    }
Nesting distionary into 
     travel_log = {
        "France" :{"cities_visited": ["Paris","Lille","Dijon"],
        "total_visits":12},
        "Germany":{"cities_visited": ["Berlin","Hamburg","Stuttgart"],
        "total_visits": 10}
    }


Nesting a dictionary inside a list
  travel_log = [
        {
        "country":"France" ,
         "cities_visited": ["Paris","Lille","Dijon"],"total_visits":12
         },
        {
        "country":"Germany" ,
         "cities_visited": ["Berlin","Hamburg","Stuttgart"],"total_visits": 10
         }
    ]