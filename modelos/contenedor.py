class Contenedor:


    def __init__(
        self,
        tipo="40FT"
    ):


        self.tipo = tipo


        if tipo == "40FT":

            self.largo = 60

            self.ancho = 12

            self.alto = 13


        else:

            self.largo = 30

            self.ancho = 12

            self.alto = 13



    def volumen(self):

        return (

            self.largo *
            self.ancho *
            self.alto

        )