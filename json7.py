import json  
d={"Name":" Abhishek","Designation": "CEO of navgurukul","Gender": "male","Age": 29}
#with open("prerna.json","w") as  file:
a=open("prerna.json","w")
json.dump(d,a,indent=4)