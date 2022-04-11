import json 
dic={'4': 5,'6': 7,'1': 3,'2': 4}
s=list(dic.values())
#print(s)
s.sort()
#print(s)
dict1={}
for i in s:
    for j in dic:
        if i ==dic[j]:
            dict1[i]=i
            k=json.dumps(dict1)
print(k)
print(type(k))
    
