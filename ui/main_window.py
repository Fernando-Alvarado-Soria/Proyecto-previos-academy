from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QGroupBox,
    QMessageBox
)

from PyQt6.QtCore import Qt

from ui.plano_contenedor import PlanoContenedor
from ui.controles_capas import ControlesCapas

from modelos.contenedor import Contenedor
from packing.optimizador import Optimizador


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "SICCO - Sistema Inteligente de Cubicación de Contenedores"
        )

        self.resize(
            1400,
            800
        )

        self.cajas = []

        self.resultado = []

        self.sistema = None

        self.crear_interfaz()

    def crear_interfaz(self):

        central = QWidget()

        self.setCentralWidget(
            central
        )

        principal = QVBoxLayout(
            central
        )

        titulo = QLabel(
            "SICCO\nSistema Inteligente de Cubicación de Contenedores"
        )

        titulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        titulo.setStyleSheet(
            """
            font-size:22px;
            font-weight:bold;
            """
        )

        principal.addWidget(
            titulo
        )

        zona = QHBoxLayout()

        # =========================
        # CAMARA
        # =========================

        grupo_cam = QGroupBox(
            "WEBCAM / ESCANEO ARUCO"
        )

        cam_layout = QVBoxLayout()

        self.lbl_cam = QLabel(
            "Área de captura\n\nCámara activa"
        )

        self.lbl_cam.setMinimumSize(
            300,
            300
        )

        self.lbl_cam.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.lbl_cam.setStyleSheet(
            """
            background:#202020;
            color:white;
            font-size:18px;
            """
        )

        cam_layout.addWidget(
            self.lbl_cam
        )

        grupo_cam.setLayout(
            cam_layout
        )

        zona.addWidget(
            grupo_cam
        )

        # =========================
        # LISTA
        # =========================

        grupo_lista = QGroupBox(
            "LISTA DE CARGA"
        )

        lista_layout = QVBoxLayout()

        self.lista = QListWidget()

        lista_layout.addWidget(
            self.lista
        )

        grupo_lista.setLayout(
            lista_layout
        )

        zona.addWidget(
            grupo_lista
        )

        # =========================
        # PLANO
        # =========================

        grupo_plano = QGroupBox(
            "PLANO DEL CONTENEDOR"
        )

        plano_layout = QVBoxLayout()

        self.plano = PlanoContenedor()

        plano_layout.addWidget(
            self.plano
        )

        self.controles_capas = ControlesCapas(
            self.plano
        )

        plano_layout.addWidget(
            self.controles_capas
        )

        grupo_plano.setLayout(
            plano_layout
        )

        zona.addWidget(
            grupo_plano
        )

        principal.addLayout(
            zona
        )

        # =========================
        # BOTONES
        # =========================

        controles = QHBoxLayout()

        controles.addWidget(
            QLabel("Contenedor:")
        )

        self.combo = QComboBox()

        self.combo.addItems(
            [
                "40FT",
                "20FT"
            ]
        )

        self.combo.currentTextChanged.connect(
            self.cambiar_contenedor
        )

        controles.addWidget(
            self.combo
        )

        optimizar = QPushButton(
            "OPTIMIZAR"
        )

        optimizar.clicked.connect(
            self.optimizar
        )

        controles.addWidget(
            optimizar
        )

        limpiar = QPushButton(
            "LIMPIAR"
        )

        limpiar.clicked.connect(
            self.limpiar
        )

        controles.addWidget(
            limpiar
        )

        salir = QPushButton(
            "SALIR"
        )

        salir.clicked.connect(
            self.close
        )

        controles.addWidget(
            salir
        )

        principal.addLayout(
            controles
        )

    # =========================
    # CONECTAR SISTEMA
    # =========================

    def conectar_sistema(
        self,
        sistema
    ):

        self.sistema = sistema

    # =========================
    # AGREGAR CAJA
    # =========================

    def agregar_caja(
        self,
        caja
    ):

        self.cajas.append(
            caja
        )

        numero = len(
            self.cajas
        )

        self.lista.addItem(
            f"Caja {numero}   {caja.dimensiones()}"
        )

    # =========================
    # CONTENEDOR
    # =========================

    def cambiar_contenedor(
        self,
        texto
    ):

        self.plano.set_contenedor(
            texto
        )

    # =========================
    # OPTIMIZAR
    # =========================

    def optimizar(self):

        if not self.cajas:

            QMessageBox.warning(
                self,
                "SICCO",
                "No hay cajas"
            )

            return

        contenedor = Contenedor(
            self.combo.currentText()
        )

        optimizador = Optimizador(
            contenedor
        )

        for caja in self.cajas:

            optimizador.agregar_caja(
                caja
            )

        optimizador.calcular()

        self.resultado = optimizador.obtener_resultado()

        self.plano.dibujar_cajas(
            self.resultado
        )

        self.controles_capas.actualizar_capas()

    # =========================
    # LIMPIAR
    # =========================

    def limpiar(self):

        self.cajas.clear()

        self.resultado.clear()

        self.lista.clear()

        self.plano.limpiar()