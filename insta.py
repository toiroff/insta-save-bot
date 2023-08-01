import requests
import json
def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "fb217df651msh8a5ae9307ae3548p19a9cdjsn3a6d89d56f64",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    rest = json.loads(response.text)


    dict = {}
    if 'Type' in rest:
        if rest['Type'] == 'Post-Image':
            dict['type'] = 'post-image'
            dict['title'] = rest['title']
            dict['media'] = rest['media']
            return dict

        elif rest['Type'] == 'Image':
            dict['type'] = 'image'
            dict['title'] = rest['title']
            dict['media'] = rest['media']
            return dict


        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'

            dict['media'] = rest['media']
            return dict

        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['title'] = rest['title']
            dict['media'] = rest['media']
            return dict

    else:
        return ('Bad')




