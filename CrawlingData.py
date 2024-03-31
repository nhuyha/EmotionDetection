import requests
import os

def download_images(query, count):
    API_KEY = "...API..."
    # Use API pexels.com
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={count}"
    headers = {"Authorization": API_KEY}
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if not os.path.exists(query):
        os.makedirs(query)
    
    for idx, photo in enumerate(data['photos']):
        photo_url = photo['src']['large']
        img_data = requests.get(photo_url).content
        with open(f"{query}/image_{idx+1}.jpg", 'wb') as f:
            f.write(img_data)

if __name__ == "__main__":
    query = "....." # topic of images
    count = "Number"  # the number of images
    download_images(query, count)
