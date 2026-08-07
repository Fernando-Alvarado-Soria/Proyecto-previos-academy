import cv2



class Camera:


    def __init__(self, indice=0):

        self.cap = None

        self.indice = indice



    def iniciar(self):


        self.cap = cv2.VideoCapture(self.indice)


        if not self.cap.isOpened():

            print(
                f"No se pudo abrir la cámara con índice {self.indice}"
            )

            return False



        print(
            f"Cámara iniciada con índice {self.indice}"
        )


        return True




    def leer(self):


        if self.cap is None:

            return None



        ret, frame = self.cap.read()



        if not ret:

            return None



        return frame





    def detener(self):


        if self.cap:


            self.cap.release()
