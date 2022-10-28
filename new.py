import requests

# shift option f, auto formats code


r = requests.get("https://coreyms.com")
print(r.status_code)
