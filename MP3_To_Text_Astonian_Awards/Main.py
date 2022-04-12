from distutils.log import error
import sys
import requests
import pprint
import os
import json
from time import sleep
from Assembly import Assembly


media_url = input("Please enter the link to the media? ")
auth_key = "25344f88969c441da505e719d5081ea4"

test = Assembly(auth_key)
response_upload_link = test.upload_audio_by_url(media_url)
print(response_upload_link.json())

script_id = response_upload_link.json()["id"]
response_status = test.receive_transcript(script_id)
print(response_status.json["status"])
print(response_status["error"])
print(response_status["text"])

filename = r"./Coding Projects/Python Projects/Astonian Awards/MP3_To_Text_Astonian_Awards/Rickroll.mp3"
response_upload = test.upload_audio_local_file(filename)
json_output = response_upload.json()
transcript_id = json_output.json["id"]
