import json
from pstats import SortKey
data='{"clr":"purple","f":"apple"}'


parsed=json.loads(data)

print(parsed)
print(parsed['clr'])

print(data)

print(type(parsed))


stud={
"sid":101,
"name" :"harry"  ,
"sub":['c','cpp','php','python'],
"sem":(1,2,3,4),
"val":False ,
"age":23
}

jd=json.dumps(stud)
print(jd)


sk=json.dumps(stud,sort_keys=True)
print(sk)