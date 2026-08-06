class Caja:

    contador = 1


    def __init__(
        self,
        largo,
        ancho,
        alto
    ):

        self.id = Caja.contador

        Caja.contador += 1


        self.largo = largo

        self.ancho = ancho

        self.alto = alto



    def nombre(self):

        return f"Caja {self.id}"



    def volumen(self):

        return (
            self.largo *
            self.ancho *
            self.alto
        )



    def dimensiones(self):

        return (
            f"{self.largo} x "
            f"{self.ancho} x "
            f"{self.alto} cm"
        )