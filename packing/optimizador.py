from packing.posicion import Posicion



class Optimizador:


    def __init__(
        self,
        contenedor
    ):


        self.contenedor = contenedor


        self.cajas = []


        self.resultado = []



    def agregar_caja(
        self,
        caja
    ):


        self.cajas.append(
            caja
        )



    def calcular(self):


        self.resultado.clear()



        # ordenar por volumen mayor a menor

        cajas_ordenadas = sorted(

            self.cajas,

            key=lambda c:
            c.largo *
            c.ancho *
            c.alto,

            reverse=True

        )



        puntos = [

            (
                0,
                0,
                0
            )

        ]



        for caja in cajas_ordenadas:



            colocado = False



            for punto in puntos:



                x,y,z = punto



                orientaciones = [

                    (
                        caja.largo,
                        caja.ancho
                    ),


                    (
                        caja.ancho,
                        caja.largo
                    )

                ]



                for largo,ancho in orientaciones:



                    if self.cabe(

                        x,

                        y,

                        z,

                        largo,

                        ancho,

                        caja.alto

                    ):



                        posicion = Posicion(

                            x,

                            y,

                            z

                        )



                        self.resultado.append(

                            {

                            "caja": caja,

                            "posicion": posicion,

                            "largo_usado": largo,

                            "ancho_usado": ancho

                            }

                        )



                        # crear nuevos espacios

                        puntos.append(

                            (

                                x+largo,

                                y,

                                z

                            )

                        )



                        puntos.append(

                            (

                                x,

                                y+ancho,

                                z

                            )

                        )



                        puntos.append(

                            (

                                x,

                                y,

                                z+caja.alto

                            )

                        )



                        colocado=True


                        break



                if colocado:

                    break



            if not colocado:


                print(

                    "No cabe:",

                    caja.nombre()

                )



    def cabe(

        self,

        x,

        y,

        z,

        largo,

        ancho,

        alto

    ):


        if (

            x+largo >

            self.contenedor.largo

        ):

            return False



        if (

            y+ancho >

            self.contenedor.ancho

        ):

            return False



        if (

            z+alto >

            self.contenedor.alto

        ):

            return False



        # revisar colisiones

        for item in self.resultado:



            otra = item["caja"]

            pos = item["posicion"]



            if not (

                x+largo <= pos.x or

                pos.x+otra.largo <= x or

                y+ancho <= pos.y or

                pos.y+otra.ancho <= y or

                z+alto <= pos.z or

                pos.z+otra.alto <= z

            ):


                return False



        return True




    def obtener_resultado(self):


        return self.resultado




    def reporte(self):


        datos=[]



        for i,item in enumerate(

            self.resultado,

            start=1

        ):


            caja=item["caja"]

            pos=item["posicion"]



            datos.append(

                {


                "caja":

                f"Caja {i}",



                "dimensiones":

                caja.dimensiones(),



                "posicion":

                pos.datos(),



                "capa":

                int(
                    pos.z /
                    caja.alto
                )+1


                }

            )



        return datos