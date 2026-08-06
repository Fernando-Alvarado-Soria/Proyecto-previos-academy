class CatalogoCajas:


    def __init__(self):

        self.cajas = {

            1: {

                "nombre":"Caja 1",

                "largo":10,

                "ancho":8,

                "alto":5

            },


            2: {

                "nombre":"Caja 2",

                "largo":15,

                "ancho":10,

                "alto":8

            },


            3: {

                "nombre":"Caja 3",

                "largo":20,

                "ancho":12,

                "alto":10

            }

        }



    def obtener(
        self,
        id_aruco
    ):

        return self.cajas.get(
            id_aruco,
            None
        )



    def agregar(
        self,
        id_aruco,
        largo,
        ancho,
        alto
    ):


        self.cajas[id_aruco]={

            "nombre":
            f"Caja {id_aruco}",

            "largo":
            largo,

            "ancho":
            ancho,

            "alto":
            alto

        }