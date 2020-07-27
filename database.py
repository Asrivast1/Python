import json
# Coursera Assignment
input = '''[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''
info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name']) # It returns the value stored inside the tags
    print('Id', item['id']) # I dunno, it seems very much similar to info[]
    print('Attribute', item['x'])