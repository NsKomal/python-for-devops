#import requests
#result = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#details = (result.json())
#for i in range(10):
#   print(details[i]['id'] ,';', details[i]['user']['id'])

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york" 
    }
# Keys to extract
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict["salary"])