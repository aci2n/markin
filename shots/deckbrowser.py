from aqt.deckbrowser import DeckBrowser
from .shot import Shot

class DeckBrowserShot(Shot):
    def name(self):
        return 'deckbrowser'

    def inject(self, html):
        DeckBrowser._body = """
<center>
<table cellspacing=0 cellpading=3>
%(tree)s
</table>

<br>
%(stats)s
%(countwarn)s

""" + html + """
</center>
"""