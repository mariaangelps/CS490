
"""
Maria Angel Palacios Sarmiento
CS490 - 103
Homework 1 - Student Info Submission
"""
import requests 
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