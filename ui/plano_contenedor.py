from PyQt6.QtWidgets import QWidget

from PyQt6.QtGui import (
    QPainter,
    QPen,
    QBrush,
    QColor,
    QFont
)

from PyQt6.QtCore import (
    Qt,
    QRectF
)



class PlanoContenedor(QWidget):


    def __init__(self):

        super().__init__()


        self.tipo_contenedor = "40FT"


        self.cajas = []


        self.capa_actual = 1


        self.setMinimumSize(
            700,
            500
        )



    def set_contenedor(
        self,
        tipo
    ):

        self.tipo_contenedor = tipo

        self.update()



    def dibujar_cajas(
        self,
        cajas
    ):

        self.cajas = cajas

        self.capa_actual = 1

        self.update()



    def cambiar_capa(
        self,
        capa
    ):

        self.capa_actual = capa

        self.update()



    def limpiar(self):

        self.cajas.clear()

        self.update()



    def paintEvent(
        self,
        event
    ):


        painter = QPainter(self)



        painter.fillRect(
            self.rect(),
            Qt.GlobalColor.white
        )



        painter.setPen(
            Qt.GlobalColor.black
        )


        painter.setFont(
            QFont(
                "Arial",
                16,
                QFont.Weight.Bold
            )
        )


        painter.drawText(
            20,
            35,
            f"CONTENEDOR {self.tipo_contenedor}"
        )



        painter.setFont(
            QFont(
                "Arial",
                12
            )
        )


        painter.drawText(

            20,

            65,

            f"CAPA  ACTUAL: {self.capa_actual}"

        )



        if self.tipo_contenedor=="40FT":

            largo = 60

        else:

            largo = 30



        ancho = 12



        escala = 8



        x0 = 80

        y0 = 130



        painter.setPen(
            QPen(
                Qt.GlobalColor.black,
                3
            )
        )


        painter.setBrush(
            QBrush(
                QColor(
                    240,
                    240,
                    240
                )
            )
        )


        painter.drawRect(

            QRectF(

                x0,

                y0,

                largo*escala,

                ancho*escala

            )

        )



        for item in self.cajas:


            caja = item["caja"]

            posicion = item["posicion"]



            capa = int(
                posicion.z /
                caja.alto
            ) + 1



            if capa != self.capa_actual:

                continue



            x = (

                x0 +

                posicion.x *

                escala

            )


            y = (

                y0 +

                posicion.y *

                escala

            )



            w = caja.largo * escala

            h = caja.ancho * escala



            painter.setBrush(

                QBrush(

                    QColor(
                        120,
                        180,
                        240
                    )

                )

            )



            painter.setPen(

                QPen(

                    Qt.GlobalColor.blue,

                    2

                )

            )



            painter.drawRect(

                QRectF(

                    x,

                    y,

                    w,

                    h

                )

            )



            painter.setPen(
                Qt.GlobalColor.black
            )


            painter.setFont(

                QFont(

                    "Arial",

                    10,

                    QFont.Weight.Bold

                )

            )


            painter.drawText(

                QRectF(

                    x,

                    y,

                    w,

                    h

                ),

                Qt.AlignmentFlag.AlignCenter,

                caja.nombre()

            )