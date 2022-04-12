
from urllib import response
import requests
import os


class Assembly:
    
    base_URL = "https://api.assemblyai.com/v2/"
    
    def __init__(self,auth_key):
        self.auth_key = auth_key
        
    def headers(self, auth_key):
        return{"authorization": auth_key}
        
    def upload_audio_by_url(self, url_link, speaker_labels=True):
        request_text = {
            "audio_link" : url_link,
            "speaker" : speaker_labels
        }
        
        response = requests.post(self.base_URL + "transcript", headers = self.headers, json=request_text)
        return response
    
    def upload_audio_local_file(self, audio_file_pathway, audio_chuck_size=52, speaker_labels=True):
        if not os.path.exists(audio_file_pathway) or not os.path.isfile(audio_file_pathway):
            print("The file you intended has not been found.")
            return
        
        def read_file(file_path, audio_chunk_size=audio_chuck_size):
            with open(file_path, mode="rb") as _file:
                while True:
                    data = file_path.read(audio_chunk_size)
                    if not data:
                        break
                    yield data 
        audio_data = read_file(audio_file_pathway)
        headers = self.headers
        headers["content-type"] = "application/json"
        upload_response = response.get(self.base_URL+"upload/", headers=headers, data = audio_data)        
        
        response = self.upload_audio_by_url(upload_response.json()["upload.url"],speaker_labels=speaker_labels)
        return response
        
    def receive_transcript(self, transcript_id):
        response = requests.get(self.base_URL+"transcipt/"+transcript_id, headers = self.headers)
        return response.json