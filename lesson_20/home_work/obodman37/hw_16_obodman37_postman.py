import requests
import json

url = "https://restful-booker.herokuapp.com/auth"

payload = json.dumps({
  "username": "admin",
  "password": "password123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
token = response.json()["token"]
print("1. POST - Auth - CreateToken")
print(response.text)
print(50 * '~')


url = "https://restful-booker.herokuapp.com/booking"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print("2. GET - Booking - GetBookingIds")
print(response.text)
print(50 * '~')


url = "https://restful-booker.herokuapp.com/booking/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
bookID = response.json()[0]['bookingid']

print("3. GET - Booking - GetBooking")
print(response.text)
print(50 * '~')


url = "https://restful-booker.herokuapp.com/booking?Content-Type=application/json&Accept=application/json"

payload = json.dumps({
  "firstname": "Jim",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print("4. POST - Booking - CreateBooking")
print(response.text)
print(50 * '~')


url = f"https://restful-booker.herokuapp.com/booking/{bookID}"

payload = json.dumps({
  "firstname": "James",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
})
headers = {
  'Cookie': f'token={token}',
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print("5. PUT - Booking - UpdateBooking")
print(response.text)
print(50 * '~')

url = f"https://restful-booker.herokuapp.com/booking/{bookID}"

payload = json.dumps({
  "firstname": "James",
  "lastname": "Brown"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Cookie': f'token={token}'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print("6. PATCH - Booking - PartialUpdateBooking")
print(response.text)
print(50 * '~')

url = f"https://restful-booker.herokuapp.com/booking/{bookID}"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Cookie': f'token={token}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print("7. DELETE - Booking - DeleteBooking")
print(response.text)
print(50 * '~')