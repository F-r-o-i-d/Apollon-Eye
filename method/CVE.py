from bs4 import BeautifulSoup
import requests
from method.Theme import *


class CVE_Scanner:
    def __init__(self, server) -> None:
        pass
        urll ="https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword="
        req = requests.get(urll + server)
        round = 0
        continuePrintCVE = ""
        if("There are <b>0</b> CVE Records that match your search." in req.text):
            alert("No cve detected !")
        else:
            soup = BeautifulSoup(req.text, features="lxml")
            for row in soup.findAll('table')[2].findAll('tr'):
                round += 1
                if(continuePrintCVE != True):
                    if(round > 10):
                        choice = input(" [ - ] WOuld you like to continue ? y/N").lower()
                        if(choice == "y"):
                            continuePrintCVE = True
                        else:
                            continuePrintCVE = False
                if(continuePrintCVE != False):
                    try:
                        first_column = row.findAll('td')[0].contents
                        third_column = row.findAll('td')[1].contents
                        print(FormatText(f"""
        \t\t\t{first_column[0].contents} %%desco%% # {third_column[0]} %%descc%%
                    """))
                    except:
                        pass