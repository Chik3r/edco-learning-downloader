import requests
import json
import os

print("Enter your token. (From the URL for any of the images, example URL: https://cdn.edcolearning.ie/Image?bookId=book194&...&token=TOKEN_HERE&device=WebApp)")
token = input("> ")

print("Enter the cookies sent with the GetPages request.")
cookies = input("> ")

# Get all pages via the POST request
# cookies = {
#     'ASP.NET_SessionId': 'forqr5dwbczui35qclrvw2cp',
#     'ARRAffinity': '776843fe20a803280ba2df556e4fb9a18d95357c92bbf5e1869cbfc03e7784d4',
#     'ARRAffinitySameSite': '776843fe20a803280ba2df556e4fb9a18d95357c92bbf5e1869cbfc03e7784d4',
#     'edcobid': '1d5f45b0-80a7-4ca4-937f-52255e3dedca',
#     '.ASPXAUTH': 'D2304F4F2214CA9992C1FEF0D3E01363224B6E6A0B9539D4A2D8115C784616E013482439706C56B7F5408BECFE6BEBE45D5599F8B7C428BED128DABDE76CD5C6651503F624767629CC1A1B12D15384D2658B09B2EB6D65DF130135E3B0F01C426206193F2EA103893A8B7A88461AD23A5DC314C71FC4555E915CB591562DAD1A71C2DEC5ED36B23A03C63E2F61D112208ED804FC4FE07932A360508F9E0D0FCDF9603523F880142E405D4410A89E49EB42D1ABF6E66E8516DE5A94804F773D388582260ED4E87AC4EB071B30D4AD9AE38DF27410D43BBDE710BB45E4A94E00A857FCB0E53290A6AB90F73017AAC2AEC6B8B9A73C956D0CAC65117418597F796A4890BC4AD95BD22C42A6CD013785F847A8F04BA1FC7E0B9E23CB949221A5EC7D54627A1E65DDB6118646E62054D50851F868600E209DE0AE9FC967D675BC16F92235C881747C173C4209C089F1ABCC977FB73C5922F4FE69AAC089AB196587BF88457F690E3A00E82584C371C76424C03F1473C3C26923C415FADA178948BCF5F1569BBA070E332BD63A1C4143E4B2D964A8D5869666CC5FA277A89F692B94704D101571E84E93F545FBEEDDD4DFD2601F8150A4'
# }
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': cookies
}

print("Enter the book id")
id = input("> ")
data = {
    'bookId': id
}

response = requests.post('https://www.edcolearning.ie/Book/GetPages', headers=headers, data=data)
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
