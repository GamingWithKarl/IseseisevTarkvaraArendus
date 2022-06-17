# Pildilaadija (võtab need internetist)

import requests

#Faili download funktsioon
def download_files(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream = True) as r:
        print("Downloading...")
        with open("C:/Users/karlk/Desktop/" + local_filename, 'wb') as f:
            print("Writing data to a file.")
            for chunk in r.iter_content(chunk_size = 8192):
                f.write(chunk)
    f.close()
    print("Download complete")
    print("File saved as "+ local_filename)

while 1:
    print("Welcome to the image downloader --- By Karl_Karulin")
    image_url = input(str("Image url: "))
    download_files(image_url)
    print("")