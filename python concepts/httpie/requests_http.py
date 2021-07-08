# This is httpie is an module which is to be installed from pip
# To install we give pip install httpie

# we can than use this to request the site for data by giving

# This is request module is also pip install
# where the httpie is build over the request module


import requests

parameter = {'page': 2, 'count': 25}
req = requests.get('https://httpbin.org/get', params=parameter)

print(req)  # This will print us the response code in return

print(dir(req))  # This is used to see all the methods and function present in req

print(req.headers)  # This is used to print the header of the html

print(req.text)  # The content of the request will be printed

print(req.url)  # The will return us the url of the response

print(req.status_code)  # This will print the status code of the request

print(req.ok)  # This is will return us whether the request made is OK or NOT OK

print('----------------')

parameter = {'username': 'akhshy', 'password': 'akhshy123'}
# we can submit form data to the server
req = requests.post('https://httpbin.org/post', data=parameter)

print(req.text)

print(req.json())  # This will parse the data that comes back to JSON format

req_dict = req.json()

# This will take the dict with the form value in it and print the data
print(req_dict['form'])


# We can also use the auth in the request and see how it works
req = requests.get(
    'https://httpbin.org/basic-auth/akhshy/akhshy123', auth=('akhshy', 'akhshy123'))

print(req.text)

print('--------------------')

req = requests.get(
    'https://httpbin.org/basic-auth/akhshy/akhshy123', auth=('akhshy', 'akhshy123'), timeout=3)
# The third arg will tell the request handler to timeout once when it takes more than 3 sec to give response

print(req.text)

print('----------------------')

# This is an delayer server response by httpbin which delays by 5 but timeouts in 3 second

req = requests.get('http://httpbin.org/delay/5', timeout=3)

print(req.text)     # This will return us an error of timeout
