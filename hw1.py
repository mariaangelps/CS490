import requests 
"""
Maria Angel Palacios Sarmiento
CS490 - 103
Homework 1 - Student Info Submission
"""


url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

#data that will be sent in JSON format
data = {
    "UCID": "mp352",
    "first_name": "Maria Angel",
    "last_name": "Palacios Sarmiento",
    "github_username": "mariaangelps",
    "discord_username": "MariaAngelP",
    "favorite_cartoon": "Brandy and Mr. Whiskers",
    "favorite_language": "Python",
    "movie_or_game_or_book": "The Age of Adaline",
    "section": "103"
}

#Sending the GET request -> checking if record already exists

request= requests.get(url, params={"UCID": "mp352", "section": "103"})
if request.status_code == 200:
    print("Record already exists.")
else:
    print("Record does not exist. Proceeding to create a new record.")
    request= requests.post(url, json=data)
    print("POST:", request.json())

#sending the GET request to confirm the changes
parameters = {"UCID": "mp352", "section": "103"}
response = requests.get(url, params=parameters)
print("GET:", response.json())

#sending PUT requests 
data_update = data.copy()
data_update["favorite_language"] = "JavaScript"
response = requests.put(url, json=data_update)
print("PUT:", response.json())

#sending another GET request to confirm the changes
parameters = {"UCID": "mp352", "section": "103"}
response = requests.get(url, params=parameters)
print("GET:", response.json())

"""
#sending the DELETE request
parameters = {"UCID": "mp352", "section": "103"}
response = requests.delete(url, params=parameters)
print(response.json())

#sending another POST request to confirm the changes
response = requests.post(url, json=data)
print(response.json())

"""