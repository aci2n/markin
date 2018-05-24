import re
import os
import base64

class HtmlProcessor:
    fileRe = re.compile(r'file:///([^"]+)')

    def escape(self, html):
        return html.replace('%', '%%')

    def fetchContents(self, file):
        contents = None

        if os.path.isfile(file):
            with open(file, 'rb') as stream:
                contents = stream.read()

        return contents

    def makeDataUrl(self, contents, ext):
        data = base64.b64encode(contents).decode()
        prefix = ''

        if ext == '.png':
            prefix = 'data:image/png;base64,'

        return prefix + data

    def replaceFileUrl(self, match):
        url = match.group(0)
        file = match.group(1)
        result = url
        contents = self.fetchContents(file)

        if contents != None:
            result = self.makeDataUrl(contents, os.path.splitext(file)[1])
            
        return result

    def injectLocalResources(self, html):
        return self.fileRe.sub(self.replaceFileUrl, html)

    def process(self, html):
        return self.escape(self.injectLocalResources(html))