class Shot():
    def name(self):
        return self.__class__.__name__
        
    def inject(self, html):
        pass

class overview(Shot):
    def inject(self, html):
        from aqt.overview import Overview
        Overview._body += html

class deckbrowser(Shot):
    def inject(self, html):
        from aqt.deckbrowser import DeckBrowser
        DeckBrowser._body += html