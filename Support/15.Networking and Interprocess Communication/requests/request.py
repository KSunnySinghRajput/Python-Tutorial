"""
Method	                    Description
delete(url, args)	        Sends a DELETE request to the specified url
get(url, params, args)	    Sends a GET request to the specified url
head(url, args)	            Sends a HEAD request to the specified url
patch(url, data, args)	    Sends a PATCH request to the specified url
post(url, data, json, args)	Sends a POST request to the specified url
put(url, data, args)	    Sends a PUT request to the specified url
request(method, url, args)	Sends a request of the specified method to the specified url

example
1.url:- https://api.github.com/ or  http://api.github.com/ 
2.args:-
3.params:-
4.json={'key':'value'}
"""
import requests
pload = {'username':'Olivia','password':'123'}
#r = requests.post('https://httpbin.org/post',data = pload)
r = requests.post('https://colab.research.google.com/')

print(r.http)

# print(r.text)

'''
response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
json_response['data']
json_response['headers']['Content-Type']

response = requests.get('https://api.github.com/')
'''

