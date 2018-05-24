import os.path
from aqt import mw, qt
from .shots import deckbrowser, overview

class MarkIn():
    config = mw.addonManager.getConfig(__name__)
    registry = [deckbrowser(), overview()]

    def load(self):
        if self.config['debug'] == True:
            action = qt.QAction('markin', mw)
            action.triggered.connect(lambda: self.inject())
            action.addShortcut('Ctrl+L')
            mw.form.menuTools.addAction(action)
        else:
            self.inject()
    
    def inject(self):
        for shot in self.registry:
            html = self.read(shot.name())
            
            if html != None:
                shot.inject(html)

    def read(self, shotName):
        html = None
        file = os.path.join(self.config['directory'], shotName + ".html")

        if os.path.isfile(file):
            with open(file, 'r') as stream:
                html = stream.read()
            
        return html
