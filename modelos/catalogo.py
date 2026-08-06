import json



class Catalogo:


    def __init__(self):

        self.cajas=[]


        self.cargar()



    def cargar(self):


        try:


            with open(

                "datos/cajas.json",

                "r"

            ) as archivo:


                self.cajas = json.load(
                    archivo
                )


        except Exception as e:


            print(
                "Error cargando catalogo:",
                e
            )



    def buscar_aruco(
        self,
        aruco
    ):


        for caja in self.cajas:


            if caja["aruco"] == aruco:

                return caja



        return None