import requests


# Request the user for their username that will be used to log into the SSO
username = raw_input("Enter your username: ")

# Request the user for their password that will be used to log into the SSO
# NOTE: This is not the most efficient since it is echoing the password back to the screen
#       I just used this as a very simple example
password = raw_input("Enter your password: ")

# Ask the user for the URL to be fetched using the SSO credentials (Make sure you use http:// before)
url = raw_input("Enter the URL to fetch using SSO: ")

print "Attempting to fetch: "+url+" using username name: "+username
s = requests.session()

s.get('https://sso.cisco.com/autho/forms/CECLogin.html')

# Generate the post data
data = {
    'userid': username,
    'password': password
}

r = s.post('https://sso.cisco.com/autho/login/loginaction.html', data=data)

headers2 = {'X-Requested-With': 'XMLHttpRequest', 'Referer': r.url}
r = s.get(url)

# Display the information associated with the retrieved web page
print (r.url)
print (r.status_code)
print (r.content)

