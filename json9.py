import json
dic={"shopping_list":{"chaco":"15","biscuits":"50","diary_milk":"30","ice_cream":"20"}}
# d={}
# for i in dic:
#     d=dic[i]
#     user=(input("kon sa item khareedna hai"))
#     for j in d.values():
#         if user in d:
#             user1=int(input("kitna item chahiye"))
#             res=(int(j)-user1)
#         break
#     d[user]=res
# print(d)
# with open("aj.json","w") as file:
#     json.dump(d,file,indent=2)
d={}
for i in dic:
    d=dic[i]
    user=(input("kon sa item khareedna hai"))
    for j in d:
        if user==j:
            if user in d:
                user1=int(input("kitna item chahiye"))
                res=(int(d[j])-user1)
            break
    d[user]=str(res)
print(d)
with open("aj.json","w") as file:
    json.dump(d,file,indent=2)
 