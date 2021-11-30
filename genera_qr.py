import qrcode
img = qrcode.make('http://www.ganimides.ucm.cl/haraya/inicio.htm')
f = open('hola_haraya.png','wb')
img.save(f)
f.close()
