print ("Enter the number of rows
       ")
rows = int(input())
 

k = 0
for i in range(1, rows + 1): 
     
    for j in range (1, (rows - i) + 1): 
        print(end = " ") 
	  
        
    while k != (2 * i - 1):
        print("*", end = "")
        k = k + 1
    k = 0
	  
    
    print()  
 

k = 2
m = 1
for i in range(1, rows): 
     
    for j in range (1, k):
        print(end = " ") 
    k = k + 1
	  
     
    while m <= (2 * (rows - i) - 1): 
        print("*", end = "") 
        m = m + 1
    m = 1
	
    
    print()

