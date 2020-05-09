#/usr/bin/python3
#coding: utf-8


import requests, os ,signal ,pytesseract
from PIL import Image

# variable global
url = "https://http2.mlstatic.com/globo-metalico-frase-te-amo-color-rojo-D_NQ_NP_845102-MLC29362312075_022019-O.webp"

#definiendo salida del sistema
def def_handler(sig, frame):
   sys.exit(0)
signal.signal(signal.SIGINT, def_handler)

def makeRequest():
   s = requests.session()
   respuesta = s.get(url)
  
# descargo imagen
   descarga_imagen = s.get(url)

#abrir imagen
   f = open("imagen.jpg", "wb")
   f.write(descarga_imagen.content)
   f.close()

# transformando imagen a string
   valor_palabra = pytesseract.image_to_string(Image.open('imagen.jpg'))
   os.remove("imagen.jpg")

   print ("\n----------------------> %s\n" % valor_palabra )



#definir flujo inicial
if __name__ == '__main__':
   makeRequest()
