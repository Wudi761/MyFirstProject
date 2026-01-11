np = list(map(int, (input().split())))
sp = set()
for i in np:
    if i in sp:
        print(i,"YES")
    
    else: 
        print(i,"NO")
        sp.add(i)    
    


