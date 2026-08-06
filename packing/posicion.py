class Posicion:


    def __init__(
        self,
        x,
        y,
        z
    ):

        self.x = x

        self.y = y

        self.z = z



    def datos(self):

        return {

            "x": self.x,

            "y": self.y,

            "z": self.z

        }