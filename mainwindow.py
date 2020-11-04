from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from swarm import Swarm

class MainWindow (QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.swarm = Swarm()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

    @Slot()
    def action_abrir_archivo(self):
        # print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if  self.swarm.abrir(ubicacion):
            QMessageBox.information(
              self,
              "Exito",
              "Se abrio el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo" + ubicacion
            )


    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.swarm.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )


    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.swarm))
        
    @Slot()
    def click_agregar(self):
        iid = self.ui.id_spinBox.value()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(iid, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.swarm.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        iid = self.ui.id_spinBox.value()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(iid, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.swarm.agregar_inicio(particula)

   