from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QHBoxLayout
)



class ControlesCapas(QWidget):


    def __init__(
        self,
        plano
    ):

        super().__init__()


        self.plano = plano

        self.total_capas = 1


        self.crear_interfaz()



    def crear_interfaz(self):


        layout = QHBoxLayout()



        self.btn_anterior = QPushButton(
            "◀ CAPA"
        )


        self.btn_siguiente = QPushButton(
            "CAPA ▶"
        )


        self.lbl_capa = QLabel(
            "CAPA 1 / 1"
        )


        self.btn_anterior.clicked.connect(
            self.capa_anterior
        )


        self.btn_siguiente.clicked.connect(
            self.capa_siguiente
        )



        layout.addWidget(
            self.btn_anterior
        )


        layout.addWidget(
            self.lbl_capa
        )


        layout.addWidget(
            self.btn_siguiente
        )


        self.setLayout(
            layout
        )



    def actualizar_capas(self):


        capas = []


        for item in self.plano.cajas:


            caja = item["caja"]

            posicion = item["posicion"]


            capa = int(
                posicion.z /
                caja.alto
            ) + 1


            capas.append(
                capa
            )



        if capas:

            self.total_capas = max(
                capas
            )

        else:

            self.total_capas = 1



        self.plano.capa_actual = 1


        self.actualizar_texto()



    def actualizar_texto(self):


        self.lbl_capa.setText(

            f"CAPA "
            f"{self.plano.capa_actual}"
            f" / "
            f"{self.total_capas}"

        )



    def capa_anterior(self):


        if self.plano.capa_actual > 1:


            self.plano.capa_actual -= 1


            self.plano.update()


            self.actualizar_texto()



    def capa_siguiente(self):


        if self.plano.capa_actual < self.total_capas:


            self.plano.capa_actual += 1


            self.plano.update()


            self.actualizar_texto()