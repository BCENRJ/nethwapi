import requests
import os

class YaDiscUploader:
    def __init__(self, token: str):
        self.token = token
    
    # Method to GET - URL for uploading
    def get_upload_url(self, file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload?'
        headers = {'Accept': 'application/json', 'Authorization': self.token}
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(url=url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return data['href']
        else:
            return 'There is a problem with get_upload_url method in YaDiscUploader Class'

    # Method to PUT upload to self recieved URL
    def upload(self,  my_file):
        file_name = os.path.basename(my_file)
        result = requests.put(url=self.get_upload_url(file_name), data=open(my_file, 'rb'))
        if result.status_code == 201:
            return 'Successfully Uploaded'
        else:
            return 'There is a problem with upload method in YaDiscUploader'
       
           
if __name__ == '__main__':
    path_to_file = os.path.join(os.getcwd(), 'for_yandex.txt')
    # Paste Your Ya Disk Token
    token = 'OAuth ' 
    uploader = YaDiscUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
