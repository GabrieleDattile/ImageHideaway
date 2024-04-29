import os
import struct
from PIL import Image

def nascondi_apk_nel_fileimmagine(percorso_fileimmagine, percorso_fileapk):
    # Apri il file immagine
    immagine = Image.open(percorso_fileimmagine)

    # Leggi il file APK
    with open(percorso_fileapk, 'rb') as fileapk:
        datiapk = fileapk.read()

    # Calcola la dimensione del file APK
    dimensioneapk = len(datiapk)

    # Calcola il numero di pixel nell'immagine
    pixel = immagine.width * immagine.height

    # Calcola la dimensione in byte necessaria per memorizzare la dimensione del file APK
    byte_dimensioneapk = struct.pack('I', dimensioneapk)

    # Calcola il numero di byte di riempimento necessari
    byte_riempimento = (pixel - (dimensioneapk + len(byte_dimensioneapk))) % pixel

    # Inserisci la dimensione del file APK nei dati pixel
    for i in range(len(byte_dimensioneapk)):
        immagine.putpixel((i, 0), byte_dimensioneapk[i])

    # Inserisci i dati APK nei dati pixel
    for i in range(dimensioneapk):
        immagine.putpixel((i % immagine.width, i // immagine.height), datiapk[i])

    # Inserisci i byte di riempimento nei dati pixel
    for i in range(byte_riempimento):
        immagine.putpixel((dimensioneapk + i, 0), 0)

    # Salva l'immagine modificata
    immagine.save(percorso_fileimmagine)

def main():
    while True:
        percorso_fileimmagine = input("Inserisci il percorso del file immagine: ")
        percorso_fileapk = input("Inserisci il percorso del file APK: ")

        if os.path.exists(percorso_fileimmagine) and os.path.exists(percorso_fileapk):
            nascondi_apk_nel_fileimmagine(percorso_fileimmagine, percorso_fileapk)
            print("APK nascosto con successo nel file immagine!")
            break
        else:
            print("Uno o entrambi i file non esistono. Riprova.")

if __name__ == "__main__":
    main()
