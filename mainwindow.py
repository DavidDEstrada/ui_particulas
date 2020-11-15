from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
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

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_iid)

        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)
    @Slot()
    def dibujar(self):
        for particula in self.swarm:

            pen = QPen()
            pen.setWidth(2)

            r = particula.red
            g = particula.green
            b = particula.blue
            color = QColor(r, g ,b)
            pen.setColor(color)

            self.scene.addEllipse(particula.origen_x, particula.origen_y,3,3, pen)
            self.scene.addEllipse(particula.destino_x, particula.destino_y,3,3, pen)
            self.scene.addLine(particula.origen_x + 3, particula.origen_y + 3, particula.destino_x, particula.destino_y, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()




    @Slot()
    def buscar_iid(self):
        iid = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.swarm:
            if iid == str(particula.iid):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                iid_widget = QTableWidgetItem(str(particula.iid))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                

                self.ui.tabla.setItem(0, 0, iid_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)
               
                encontrado = True

                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el id "{iid}" no fue encontrada'
            )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen x", "Origen y", "Destino x", "Destino y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.swarm))
        row = 0
        for particula in self.swarm:

            iid_widget = QTableWidgetItem(str(particula.iid))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))
                

            self.ui.tabla.setItem(row, 0, iid_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row+= 1
    
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

   