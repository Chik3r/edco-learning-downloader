import requests
import json
import os

token = ""

# Get all pages via the POST request
cookies = {
    'ASP.NET_SessionId': '',
    'ARRAffinity': '',
    'ARRAffinitySameSite': '',
    'edcobid': '',
    '.ASPXAUTH': ''
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
data = {
    'bookId': 'book23'
}

response = requests.post('https://www.edcolearning.ie/Book/GetPages', headers=headers, cookies=cookies, data=data)
#print(response.text)

# Iterate over 'Pages' in response JSON
for page in response.json()['Pages']:
    bookId = page['PartitionKey']
    pageId = page['RowKey']
    chapterId = page['ChapterId']
    imagesJson = page["ImagesJson"]

    # Parse images as json and return a list of 'fileName' values
    imageList = [image['fileName'] for image in json.loads(imagesJson)]

    for i, image in enumerate(imageList):
        url = f"https://cdn.edcolearning.ie/Image?bookId={bookId}&chapterId={chapterId}&pageId={pageId}&fileName={image}&token={token}&device=WebApp"
        print("Downloading: " + url)

        filePath = f"{bookId}/{chapterId}-{pageId}-{i}.jpg"
        os.makedirs(os.path.dirname(filePath), exist_ok=True)


        # Download image
        r = requests.get(url, allow_redirects=True)

        # Check if response is not valid and stop
        if r.status_code != 200:
            print("Error: " + r.status_code)
            exit()

        # Save image
        with open(filePath, 'wb') as f:
            f.write(r.content)
