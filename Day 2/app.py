import hashlib



Data =[str(input('data 1'),input('data 2'),input('data 3'),input('data 4'))]

for i in Data:
    
    hashed =hashlib.sha256(Data.encode()).hexdigest()
    print(hashed) 
    
    
