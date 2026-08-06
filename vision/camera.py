import cv2



class Camera:


    def __init__(self):

        self.cap = None



    def iniciar(self):


        self.cap = cv2.VideoCapture(0)


        if not self.cap.isOpened():

            print(
                "No se pudo abrir la cámara"
            )

            return False



        print(
            "Cámara iniciada"
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