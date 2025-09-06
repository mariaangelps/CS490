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
    "discord_username": "@MariaAngelP",
    "favorite_cartoon": "Brandy and Mr. Whiskers",
    "favorite_language": "Python",
    "movie_or_game_or_book": "The Age of Adaline",
    "section": "103"
}
#Sending the GET request
parameters = {"UCID": "mp352", "section": "103"}
response = requests.get(url, params=parameters)
print("GET:", response.json())

#sending the DELETE request
parameters = {"UCID": "mp352", "section": "103"}
response = requests.delete(url, params=parameters)
print(response.json())

#sending the POST request
response = requests.post(url, json=data)
print(response.json())



