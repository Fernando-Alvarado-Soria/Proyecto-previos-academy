import cv2
from cv2 import aruco


from modelos.catalogo import Catalogo



class DetectorAruco:


    def __init__(self):


        self.diccionario = aruco.getPredefinedDictionary(
            aruco.DICT_5X5_100
        )


        self.parametros = aruco.DetectorParameters()


        self.detector = aruco.ArucoDetector(

            self.diccionario,

            self.parametros

        )


        self.catalogo = Catalogo()



    def detectar(
        self,
        frame
    ):


        gris = cv2.cvtColor(

            frame,

            cv2.COLOR_BGR2GRAY

        )


        esquinas, ids, rechazados = self.detector.detectMarkers(

            gris

        )


        encontrados = []



        if ids is not None:


            for i, marcador in enumerate(ids):


                numero = int(
                    marcador[0]
                )



                datos = self.catalogo.buscar_aruco(

                    numero

                )



                encontrados.append(

                    {

                    "id": numero,

                    "datos": datos,

                    "esquinas": esquinas[i]

                    }

                )



            aruco.drawDetectedMarkers(

                frame,

                esquinas,

                ids

            )



        return encontrados