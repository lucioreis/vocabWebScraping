import sys
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl


class Client(QWebEnginePage):
    """docstring for Client"""
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.loadFinished.connect(self.on_page_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def on_page_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print("Load Finished")

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()
