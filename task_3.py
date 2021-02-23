. shop = {"first": {
    "customer": "Mrs. Green",
    "item": "soap",
    "number": 3
},
	 "second": {
         "customer": "Mr. Black",
         "item": "soks",
         "number": 2
     },
    "third": {
         "customer": "Mrs. Brown",
         "item": "pencil",
         "number": 12
     },
}
dict1 = ["first", "second", "third"]
new_list, new_list2, new_list3 = (shop[dict1[0]]), (shop[dict1[1]]), (shop[dict1[2]])
list_1, list_2, list_3 = list(new_list.values()), list(new_list2.values()), list(new_list3.values()) 
print([list_1, list_2, list_3])
