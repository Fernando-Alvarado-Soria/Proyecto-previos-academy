import sys
import cv2
import time


from PyQt6.QtWidgets import QApplication


from ui.main_window import MainWindow


from vision.camera import Camera
from vision.detector_aruco import DetectorAruco


from modelos.caja import Caja





class SistemaSICCO:


    def __init__(self, ventana, indice_camara=0):


        self.ventana = ventana


        self.camara = Camera(

            indice_camara

        )


        self.detector = DetectorAruco()



        # memoria de cajas capturadas

        self.ids_registrados = []



        # control de tiempo

        self.ultimo_id = None

        self.tiempo_ultimo = 0





    def iniciar(self):


        if not self.camara.iniciar():


            print(
                "Error al iniciar cámara"
            )


            return



        print(
            "SICCO listo - Escaneo automático"
        )



        self.procesar()





    def procesar(self):


        while True:



            frame = self.camara.leer()



            if frame is None:

                break



            encontrados = self.detector.detectar(

                frame

            )



            if encontrados:



                objeto = encontrados[0]



                numero = objeto["id"]


                datos = objeto["datos"]



                if datos:



                    texto = (

                        f"ARUCO {numero}  "

                        f"{datos['largo']}x"

                        f"{datos['ancho']}x"

                        f"{datos['alto']} cm"

                    )



                    cv2.putText(

                        frame,

                        texto,

                        (20,40),

                        cv2.FONT_HERSHEY_SIMPLEX,

                        0.8,

                        (0,255,0),

                        2

                    )



                    self.registrar_caja(

                        numero,

                        datos

                    )



            cv2.imshow(

                "SICCO CAMARA",

                frame

            )



            tecla=cv2.waitKey(1)



            if tecla==27:

                break



        self.camara.detener()


        cv2.destroyAllWindows()






    def registrar_caja(

        self,

        numero,

        datos

    ):



        tiempo_actual=time.time()



        # evitar repetir inmediatamente


        if (

            numero == self.ultimo_id

            and

            tiempo_actual-self.tiempo_ultimo < 3

        ):


            return




        self.ultimo_id = numero


        self.tiempo_ultimo = tiempo_actual




        # evitar cajas repetidas


        if numero in self.ids_registrados:


            return




        caja = Caja(

            datos["largo"],

            datos["ancho"],

            datos["alto"]

        )



        self.ventana.agregar_caja(

            caja

        )



        self.ids_registrados.append(

            numero

        )



        print(

            "Caja registrada:",

            numero

        )








def main():



    indice_camara = 0

    if len(sys.argv) > 1:

        try:

            indice_camara = int(sys.argv[1])

        except ValueError:

            print(
                "Uso: python main.py [indice_camara]"
            )

            return



    app = QApplication(
        sys.argv[:1]
    )



    ventana = MainWindow()



    sistema = SistemaSICCO(

        ventana,

        indice_camara

    )



    ventana.conectar_sistema(

        sistema

    )



    ventana.show()



    sistema.iniciar()



    sys.exit(

        app.exec()

    )







if __name__=="__main__":

    main()
