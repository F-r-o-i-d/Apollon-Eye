import requests
import googlesearch
import time

class SensitiveSearch:
    def __init__(self, target):
        self.target = target
        self.dork = ['filetype: "pdf"',
                "filetype: ovpn",
                "filetype: env",
                "filetype: bak",
                "intile: Login inurl:admin"]
    def __GetSearchResult(self, search):
        result = []
        try:
            for x in googlesearch.search(search, num_results=10):
                result.append(x)
        except:
            time.sleep(5)
        return result
    def run(self):
        info = []
        for x in self.dork:
            x += " site:" + self.target
            for d in self.__GetSearchResult(x):
                print("[ + ] " + d)
                info.append(d)

        return info

d = SensitiveSearch("www.starbucks.com")
print(d.run())
