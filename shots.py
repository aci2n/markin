import os.path
from .html import HtmlProcessor

class Shot:
    htmlProcessor = HtmlProcessor()

    def name(self):
        return self.__class__.__name__

    def extendBody(self, view, html):
        view._body += self.htmlProcessor.process(html)

class overview(Shot):
    def inject(self, html):
        from aqt.overview import Overview
        super().extendBody(Overview, html)

class deckbrowser(Shot):
    def inject(self, html):
        from aqt.deckbrowser import DeckBrowser
        super().extendBody(DeckBrowser, html)