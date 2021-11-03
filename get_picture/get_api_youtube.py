import requests

API_KEY = 'AIzaSyALrKc3-W0u_Ku-J2OpyjnqFhV5wKlwKGs'
video_id= ['7cmvABXyUC0']
url = "https://www.googleapis.com/youtube/v3/video?id="+video_id+"&part=statistic&key="+API_KEY
response = requests.get(url).json()
print(response)