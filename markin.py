import os.path
from aqt import mw
from .shots import deckbrowser, overview

class MarkIn():
    def __init__(self):
        self.config = mw.addonManager.getConfig(__name__)
        self.registry = [
            deckbrowser(),
            overview()
        ]
    
    def load(self):
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
