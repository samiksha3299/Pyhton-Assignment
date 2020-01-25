def get_info(x):
    G=datastore["office"].get(x,{})
    print(G)

def get_detail_info(x):
    

datastore={
    "office":{
        "medical":
        [
            {"room-number":100,"use":"reception","sq-ft":50,"price":75},
            {"room-number":101,"use":"waiting","sq-ft":250,"price":75},
            {"room-number":102,"use":"examination","sq-ft":125,"price":150},
            {"room-number":103,"use":"examtion","sq-ft":125,"price":150},
            {"room-number":104,"use":"office","sq-ft":150,"price":100},
        ],    
        "parking":
            {"location":"premium","style":"covered","price":750}
     }       
        
    }
        
#print(datastore)
#v=datastore.get("office",{})
#a=datastore.get("office",{}).get("medical",{})
#b=datastore.get("parking",{}).get("parking",{})
#print(b)


G=input("enter dict name")
get_info(G)



                    
