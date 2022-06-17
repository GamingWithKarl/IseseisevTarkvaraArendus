# Pildilaadija (võtab need internetist)
#Importitakse requests.
import requests

#Faili download funktsioon
def download_files(url):
    #Võetakse fail url'ist.
    local_filename = url.split('/')[-1]

    #Võetakse fail url'ist ja laetakse alla.
    with requests.get(url, stream = True) as r:
        print("Downloading...")
        #Kirjutatakse pildi andmed faili ning pantakse Desktopi peale.
        with open("C:/Users/karlk/Desktop/" + local_filename, 'wb') as f:
            print("Writing data to a file.")
            #Pantakse chuck size (tähendab, kui kiiresti faili saadakse salvestada) Mida suurem, seda parem :)
            for chunk in r.iter_content(chunk_size = 8192):
                #Kirjutatakse faili peale.
                f.write(chunk)

    #Pantakse failiedastus kinni.
    f.close()

    #Kuvatakse "Download complete" ja antakse kasutajale teada genereetitud parool.
    print("Download complete")
    print("File saved as "+ local_filename)

#Parooli algloop
while 1:
    #Prinditakse tervituskiri
    print("Welcome to the image downloader --- By Karl_Karulin")
    #Küsitakse kasutajalt url'i ja prinditakse välja =I
    image_url = input(str("Image url: "))
    download_files(image_url)
    print("")

# Dokumentatsioon

#Programmi kasutatakse tavaliselt piltide alla laadimiseks. Koodiga on hea viis masiivselt pilte alla laadida.
#Erilist pointi koodil aga pole, kuna paljudel operatsioonisüsteemidel on piltide allalaadimine sisse ehitatud (ka browseritel näiteks).

#Mida kood teeb?
#Kood võtab kasutaja url'i ning vaatab, kas url'i sees on kas .png, .jpg või muu pildisalvestul laiend.
#Kui see on olemas, siis requests library laeb selle ilusti alla. Koodi sees on ka chuck_size changer (niiet saad kas aeglustada või kiirendada salvestamist (mida suurem on, seda paremat arvutit vaja on.)