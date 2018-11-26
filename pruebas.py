#import sys , os, glob
#from PIL import Image
#cont =0
# 
#### Configuracion
#diri = "C:\\Users\\rhprincipal\\Documents\\djangosis\\rh\\media\\fotos_empleados\\" #directorio donde tendremos nuestras imagenes
#qualityimg = 70 #calidad de salida de las imagenes
#### termina configuracion
#print ("comprimiendo...")
#for img in glob.glob(diri+'*.jpg') + glob.glob(diri+'*.png')+glob.glob(diri+'*.gif'):
#    try:
#        namefile =os.path.basename(img)
#        #splitname =  os.path.splitext(namefile)
#        #namefile = splitname[0]
#        #extens = splitname[1]
#        i = Image.open(img)
#        i.save(diri+"comp\\"+namefile,quality=qualityimg)
#    except ValueError:
#        print (ValueError)
#        cont=cont +1
#if cont >0:
#    print ("Algunos archivos no se puedieron comprimir")
#else:
#    print ("todos los ficheros fueron comprimidos con exito")

import datetime

hora = datetime.datetime(2018,3,7,18,21,50)
dat = {
	'x':{
	'empleado':'121',
	'fecha':'asdasd'
	}
}
print(dat['x']['empleado'])