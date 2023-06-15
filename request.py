import requests

id=input("Enter a ID: ")

URL1='http://127.0.0.1:4000/destination_details/'+id
URL2='http://127.0.0.1:4000/destinations'

r=requests.get(url=URL1)
print(r.json())

print('#############################################')
print('#############################################')
print('#############################################')

print(requests.get(url=URL2).json()) 