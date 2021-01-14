import requests
pload = {'username':'Olivia','password':'123'}
#r = requests.post('https://httpbin.org/post',data = pload)
r = requests.post('https://colab.research.google.com/')

print(r.http)

# print(r.text)
