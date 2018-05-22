import os.path
from aqt import mw
from .shots import deckbrowser

class MarkIn():
    def __init__(self):
        self.registry = [deckbrowser.DeckBrowserShot]
        self.config = mw.addonManager.getConfig(__name__)
    
    def load(self):
        for Shot in self.registry:
            shot = Shot()
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
