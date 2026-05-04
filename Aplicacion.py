import sys
from PyQt5 import QtWidgets
from interfaz.interfaz import MyApp


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
