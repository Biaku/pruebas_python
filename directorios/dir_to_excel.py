import os
import xlsxwriter
import time

"""
Este script recorre un directorio y lo pasa a un formato en excel
correspondiente a la entrega recepcion 2018 especifico

REQUIERE: pip install XlsxWriter
"""
start_time = time.time()

path = 'C:\\Users\\rhprincipal\\Dropbox\\JefaturaRH'

workbook = xlsxwriter.Workbook('E) RESPALDOS DE INFORMACIÓN EN MEDIOS MAGNÉTICOS (OTRO4).xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'ARCHIVO O PROGRAMA')
worksheet.write('B1', 'TIPO')
worksheet.write('C1', 'DISPOSITIVO ALMACENAMIENTO')
worksheet.write('D1', 'SOFTWARE DESARROLLO')
worksheet.write('E1', 'EQUIPO DE RESGUARDO')
worksheet.write('F1', 'RESGUARDANTE')
worksheet.write('G1', 'USUARIO')
worksheet.write('H1', 'ESPACIO EN MB')
worksheet.write('I1', 'COMENTARIOS')

row = 1
col = 0

error_log = open('error_log.txt', 'w')
for root, dirs, files in os.walk(path):
    for file in files:
        full_path = '{}\\{}'.format(root, file)
        name, ext = os.path.splitext(full_path)
        try:
            size = os.path.getsize(full_path) / 1024 / 1024
        except FileNotFoundError as error:
            error_log.write(str(error))
            error_log.write('\n')
            size = 0

        # row, col, data
        worksheet.write(row, 0, file)  # ARCHIVO O PROGRAMA
        worksheet.write(row, 1, ext)  # TIPO
        worksheet.write(row, 2, '')  # DISPOSITIVO ALMACENAMIENTO
        worksheet.write(row, 3, '')  # SOFTWARE DESARROLLO
        worksheet.write(row, 4, '')  # EQUIPO DE RESGUARDO
        worksheet.write(row, 5, '')  # RESGUARDANTE
        worksheet.write(row, 6, '')  # USUARIO
        worksheet.write(row, 7, size)  # ESPACIO EN MB
        worksheet.write(row, 8, full_path)  # COMENTARIOS
        row += 1

workbook.close()
error_log.close()
print("--- %s seconds ---" % (time.time() - start_time))
