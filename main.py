import GUI
import sys

if __name__ == "__main__":
    app = GUI.QApplication(sys.argv)
    window = GUI.MainWindow()
    window.show()
    
    sys.exit(app.exec())