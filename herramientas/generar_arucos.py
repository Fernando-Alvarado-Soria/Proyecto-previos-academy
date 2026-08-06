import cv2
import os


from cv2 import aruco



# ============================
# CONFIGURACION
# ============================


ids = [

    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17

]


tamaño = 300


carpeta = "arucos"



# ============================
# CREAR CARPETA
# ============================


if not os.path.exists(carpeta):

    os.makedirs(carpeta)



# ============================
# DICCIONARIO ARUCO 5X5
# ============================


diccionario = aruco.getPredefinedDictionary(

    aruco.DICT_5X5_100

)



# ============================
# GENERAR
# ============================


for id_marcador in ids:


    marcador = aruco.generateImageMarker(

        diccionario,

        id_marcador,

        tamaño

    )


    nombre = (

        f"{carpeta}/aruco_{id_marcador}.png"

    )


    cv2.imwrite(

        nombre,

        marcador

    )


    print(

        "Generado:",

        nombre

    )



print(
    "GENERACION TERMINADA"
)