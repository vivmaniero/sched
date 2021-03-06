#!/usr/bin/env python3

# "THE BEER-WARE LICENSE" (Revision 42):
#
# As long as you retain this notice you can do whatever you want with this stuff.
# If we meet some day, and you think this stuff is worth it, you can buy me a
# beer in return.   
#
# -- grtcdr

import subprocess
import requests

def read_config():
    config = {'username': '', 'password': '', 'class': ''}
    with open('credentials.conf', 'r') as reader:
        for line in reader:
            entry = line.split(':', 1)
            key = entry[0].split()
            value = entry[1].split()
            if key[0] == 'username':
                config['username'] = value[0]
            elif key[0] == 'password':
                config['password'] = value[0]
            elif key[0] == "class":
                config['class'] = value[0]
        return config

config = read_config()

# -------------------- FIRST FORM

auth_url = 'https://esprit-tn.com/ESPOnline/Online/default.aspx'
payload = { 
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__EVENTVALIDATION': '/wEdAA1fByEQgXYMM2HBHEe7WK24D4zZrxX92uOlyIx1SyGTQokHj7KsGQZ9KI/q0cgR79eMO7fmjkJSfq6Zbgk2kTWn5BPdHG87XtyblNclsuAS8LvwPnslbtZbTzH+LM3KrmKoScikkrtCyMBYLZBZxv2YCNTGu6fpAlK5HiRhQ3QX7uQuDNsn18Vb/yPhT9ZPmVoNeSKFy2zxLVV4+zExdQxF5O2yeRHTM5Q6txDv+t953Rsahgpohlzzax1rmqU36I8bifdujSibODz2lHN+RHz65cGlq/w92chUS7cjKZ5WN/IUEbMK1wJPMmUOGacsXlc=',
    '__VIEWSTATE': '/wEPDwUJNDE1NjEwODA3D2QWAmYPZBYCAgMPZBYCAgUPDxYCHgRUZXh0BQkyMDIxLzIwMjJkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUSY3RsMDAkSW1hZ2VCdXR0b24xT+ExykuWiw1aqegOBldh/KoZ1rhItcsHE7VloclpAWg=',
    '__VIEWSTATEGENERATOR':  '717FCBFE',
    'ctl00$ContentPlaceHolder1$TextBox3': config['username'],
    'ctl00$ContentPlaceHolder1$Button3': 'Suivant'
}


session = requests.session()
# Submit the username
session.post(auth_url, data=payload)

# -------------------- SECOND FORM

auth_url = 'https://esprit-tn.com/ESPOnline/Online/default.aspx'
payload = { 
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__EVENTVALIDATION': '/wEdAA7t0UblTq7vyhbvAmQ3+XRYD4zZrxX92uOlyIx1SyGTQokHj7KsGQZ9KI/q0cgR79eMO7fmjkJSfq6Zbgk2kTWn5BPdHG87XtyblNclsuAS8LvwPnslbtZbTzH+LM3KrmKoScikkrtCyMBYLZBZxv2Y4YHt2yH9TCYlNrTCCQccHuaXknurQIHyJEMAivskpdkfOLtcwEziInaQqEgDH0GiDXkihcts8S1VePsxMXUMReTtsnkR0zOUOrcQ7/rfed0bGoYKaIZc82sda5qlN+iPG4n3bo0omzg89pRzfkR8+v768YqmYrRmR4Rddm8U+250AJHdFVmJSIGJz9NEWbCe',
    '__VIEWSTATE': '/wEPDwUJNDE1NjEwODA3D2QWAmYPZBYCAgMPZBYEAgUPDxYCHgRUZXh0BQkyMDIxLzIwMjJkZAIJD2QWAgIQD2QWEAIBDw8WAh4HVmlzaWJsZWhkZAIDDw8WBB8ABQoxOTFKTVQyMDQwHwFoZGQCBw8PFgIfAWdkZAIJDw8WAh8BZ2RkAgsPDxYCHgdFbmFibGVkZ2RkAg0PDxYCHwFnZGQCDw8PFgIfAWdkZAIRDw8WAh8BaGRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBRJjdGwwMCRJbWFnZUJ1dHRvbjGnb4LFia208Rgym4FSeWK1wIZC7QwUsmt16onxmcDyJQ==',
    '__VIEWSTATEGENERATOR':  '717FCBFE',
    'ctl00$ContentPlaceHolder1$TextBox7': config['password'],
    'ctl00$ContentPlaceHolder1$ButtonEtudiant':  'Connexion'
}

# Submit the password
session.post(auth_url, data=payload)

# Access the student's schedule
session.post('https://esprit-tn.com/ESPOnline/Etudiants/Emplois.aspx');

auth_url = 'https://esprit-tn.com/ESPOnline/Etudiants/Emplois.aspx'
payload = { 
    '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$GridView1$ctl02$lnkDownload',
    '__EVENTARGUMENT': '',
    '__EVENTVALIDATION': '/wEdABz/zrnCieAhrekfa2+ObM2mgUFlgNU1eucH/1aaMMUqPsMryMCq3/P59ehg5ciZwIpp1ew8hAHIXK34b81Ck5La4ERivuWrAAAJ/TngHis4y1QE65Et791vRPApOuB2KKzyELoaVBYZ5lCMCBuY1b7xhwD00lUg+ZsfW/SMCojCg+PaLSWTqffsOD0fDP39tFl9ytyWhO9cTpKzXAHBngJgBt/tiYKTggtmnQo6TrcfeLPj6wDPW5NcREM0evu2PLV4/fQv1ZUdypuvV0QLrb82eW4pXEnaB7Z5htNN8O1fslCQzpE3sfcsoVCZZQdaSGgU5y+egtwbO1G33K2gXLJkL3BfHJKslhhV+Tf9NMSDw5Cv/NXu7WwgjM1sxla2e0s7QzYVdj7fL60ouBk7/yAgkHQ2L4xw8mprV5anPKpSv9eIrVEfGKxpNPuvJEOulQV65I/D9OFwH6Hk0jdWTcON+7Tnsdu1FPLW1qMAywji5+uYi2JYO39Q9nWAQGZle2ZiJG9zNVd57tQUCekklS4j1Efjz2QLZHq6avTtT+c8khLnzi0SFHoWMtTK8JK9CoTSR12hBcD8MJH2eqA9zWcyHEOCAfLxir/s8TFYDGzw8/ARcZTEjO7NIvr/+ejkN6M=',
    '__VIEWSTATE': '/wEPDwULLTEyMDA3Mjc3MTIPZBYCZg9kFgICAw9kFgYCAQ8PFgIeBFRleHQFPUJFTiBBTEkgICAgICAgICAgICAgICAgICAgICAgICBUYWhhIEF6aXogICAgICAgICAgICAgICAgICAgICBkZAIDDw8WAh8ABQMzQTNkZAIwD2QWAgIBDzwrABEDAA8WBB4LXyFEYXRhQm91bmRnHgtfIUl0ZW1Db3VudAIMZAEQFgAWABYADBQrAAAWAmYPZBYaAgEPZBYGZg8PFgIfAAUmRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMDItMDUtMjAyMi5wZGZkZAIBD2QWAgIBDw8WAh4PQ29tbWFuZEFyZ3VtZW50BYsBQzpcVXNlcnNcQWRtaW5pc3RyYXRvclxEb2N1bWVudHNcVmlzdWFsIFN0dWRpbyAyMDEwXFByb2plY3RzXEVzcHJpdF8wOF8wNl8xOVxFU1BPbmxpbmVcRVNQT25saW5lXERPQ1xFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAwMi0wNS0yMDIyLnBkZmRkAgIPZBYCAgEPDxYCHwMFiwFDOlxVc2Vyc1xBZG1pbmlzdHJhdG9yXERvY3VtZW50c1xWaXN1YWwgU3R1ZGlvIDIwMTBcUHJvamVjdHNcRXNwcml0XzA4XzA2XzE5XEVTUE9ubGluZVxFU1BPbmxpbmVcRE9DXEVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDAyLTA1LTIwMjIucGRmZGQCAg9kFgZmDw8WAh8ABSZFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAwNy0wMi0yMDIyLnBkZmRkAgEPZBYCAgEPDxYCHwMFiwFDOlxVc2Vyc1xBZG1pbmlzdHJhdG9yXERvY3VtZW50c1xWaXN1YWwgU3R1ZGlvIDIwMTBcUHJvamVjdHNcRXNwcml0XzA4XzA2XzE5XEVTUE9ubGluZVxFU1BPbmxpbmVcRE9DXEVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDA3LTAyLTIwMjIucGRmZGQCAg9kFgICAQ8PFgIfAwWLAUM6XFVzZXJzXEFkbWluaXN0cmF0b3JcRG9jdW1lbnRzXFZpc3VhbCBTdHVkaW8gMjAxMFxQcm9qZWN0c1xFc3ByaXRfMDhfMDZfMTlcRVNQT25saW5lXEVTUE9ubGluZVxET0NcRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMDctMDItMjAyMi5wZGZkZAIDD2QWBmYPDxYCHwAFJkVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDA3LTAzLTIwMjIucGRmZGQCAQ9kFgICAQ8PFgIfAwWLAUM6XFVzZXJzXEFkbWluaXN0cmF0b3JcRG9jdW1lbnRzXFZpc3VhbCBTdHVkaW8gMjAxMFxQcm9qZWN0c1xFc3ByaXRfMDhfMDZfMTlcRVNQT25saW5lXEVTUE9ubGluZVxET0NcRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMDctMDMtMjAyMi5wZGZkZAICD2QWAgIBDw8WAh8DBYsBQzpcVXNlcnNcQWRtaW5pc3RyYXRvclxEb2N1bWVudHNcVmlzdWFsIFN0dWRpbyAyMDEwXFByb2plY3RzXEVzcHJpdF8wOF8wNl8xOVxFU1BPbmxpbmVcRVNQT25saW5lXERPQ1xFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAwNy0wMy0yMDIyLnBkZmRkAgQPZBYGZg8PFgIfAAUmRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMTEtMDQtMjAyMi5wZGZkZAIBD2QWAgIBDw8WAh8DBYsBQzpcVXNlcnNcQWRtaW5pc3RyYXRvclxEb2N1bWVudHNcVmlzdWFsIFN0dWRpbyAyMDEwXFByb2plY3RzXEVzcHJpdF8wOF8wNl8xOVxFU1BPbmxpbmVcRVNQT25saW5lXERPQ1xFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAxMS0wNC0yMDIyLnBkZmRkAgIPZBYCAgEPDxYCHwMFiwFDOlxVc2Vyc1xBZG1pbmlzdHJhdG9yXERvY3VtZW50c1xWaXN1YWwgU3R1ZGlvIDIwMTBcUHJvamVjdHNcRXNwcml0XzA4XzA2XzE5XEVTUE9ubGluZVxFU1BPbmxpbmVcRE9DXEVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDExLTA0LTIwMjIucGRmZGQCBQ9kFgZmDw8WAh8ABSZFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAxNC0wMi0yMDIyLnBkZmRkAgEPZBYCAgEPDxYCHwMFiwFDOlxVc2Vyc1xBZG1pbmlzdHJhdG9yXERvY3VtZW50c1xWaXN1YWwgU3R1ZGlvIDIwMTBcUHJvamVjdHNcRXNwcml0XzA4XzA2XzE5XEVTUE9ubGluZVxFU1BPbmxpbmVcRE9DXEVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDE0LTAyLTIwMjIucGRmZGQCAg9kFgICAQ8PFgIfAwWLAUM6XFVzZXJzXEFkbWluaXN0cmF0b3JcRG9jdW1lbnRzXFZpc3VhbCBTdHVkaW8gMjAxMFxQcm9qZWN0c1xFc3ByaXRfMDhfMDZfMTlcRVNQT25saW5lXEVTUE9ubGluZVxET0NcRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMTQtMDItMjAyMi5wZGZkZAIGD2QWBmYPDxYCHwAFJkVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDE4LTA0LTIwMjIucGRmZGQCAQ9kFgICAQ8PFgIfAwWLAUM6XFVzZXJzXEFkbWluaXN0cmF0b3JcRG9jdW1lbnRzXFZpc3VhbCBTdHVkaW8gMjAxMFxQcm9qZWN0c1xFc3ByaXRfMDhfMDZfMTlcRVNQT25saW5lXEVTUE9ubGluZVxET0NcRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMTgtMDQtMjAyMi5wZGZkZAICD2QWAgIBDw8WAh8DBYsBQzpcVXNlcnNcQWRtaW5pc3RyYXRvclxEb2N1bWVudHNcVmlzdWFsIFN0dWRpbyAyMDEwXFByb2plY3RzXEVzcHJpdF8wOF8wNl8xOVxFU1BPbmxpbmVcRVNQT25saW5lXERPQ1xFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAxOC0wNC0yMDIyLnBkZmRkAgcPZBYGZg8PFgIfAAUmRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMjEtMDItMjAyMi5wZGZkZAIBD2QWAgIBDw8WAh8DBYsBQzpcVXNlcnNcQWRtaW5pc3RyYXRvclxEb2N1bWVudHNcVmlzdWFsIFN0dWRpbyAyMDEwXFByb2plY3RzXEVzcHJpdF8wOF8wNl8xOVxFU1BPbmxpbmVcRVNQT25saW5lXERPQ1xFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAyMS0wMi0yMDIyLnBkZmRkAgIPZBYCAgEPDxYCHwMFiwFDOlxVc2Vyc1xBZG1pbmlzdHJhdG9yXERvY3VtZW50c1xWaXN1YWwgU3R1ZGlvIDIwMTBcUHJvamVjdHNcRXNwcml0XzA4XzA2XzE5XEVTUE9ubGluZVxFU1BPbmxpbmVcRE9DXEVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDIxLTAyLTIwMjIucGRmZGQCCA9kFgZmDw8WAh8ABSZFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAyNC0wMS0yMDIyLnBkZmRkAgEPZBYCAgEPDxYCHwMFiwFDOlxVc2Vyc1xBZG1pbmlzdHJhdG9yXERvY3VtZW50c1xWaXN1YWwgU3R1ZGlvIDIwMTBcUHJvamVjdHNcRXNwcml0XzA4XzA2XzE5XEVTUE9ubGluZVxFU1BPbmxpbmVcRE9DXEVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDI0LTAxLTIwMjIucGRmZGQCAg9kFgICAQ8PFgIfAwWLAUM6XFVzZXJzXEFkbWluaXN0cmF0b3JcRG9jdW1lbnRzXFZpc3VhbCBTdHVkaW8gMjAxMFxQcm9qZWN0c1xFc3ByaXRfMDhfMDZfMTlcRVNQT25saW5lXEVTUE9ubGluZVxET0NcRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMjQtMDEtMjAyMi5wZGZkZAIJD2QWBmYPDxYCHwAFJkVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDI1LTA0LTIwMjIucGRmZGQCAQ9kFgICAQ8PFgIfAwWLAUM6XFVzZXJzXEFkbWluaXN0cmF0b3JcRG9jdW1lbnRzXFZpc3VhbCBTdHVkaW8gMjAxMFxQcm9qZWN0c1xFc3ByaXRfMDhfMDZfMTlcRVNQT25saW5lXEVTUE9ubGluZVxET0NcRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMjUtMDQtMjAyMi5wZGZkZAICD2QWAgIBDw8WAh8DBYsBQzpcVXNlcnNcQWRtaW5pc3RyYXRvclxEb2N1bWVudHNcVmlzdWFsIFN0dWRpbyAyMDEwXFByb2plY3RzXEVzcHJpdF8wOF8wNl8xOVxFU1BPbmxpbmVcRVNQT25saW5lXERPQ1xFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAyNS0wNC0yMDIyLnBkZmRkAgoPZBYGZg8PFgIfAAUmRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMjgtMDItMjAyMi5wZGZkZAIBD2QWAgIBDw8WAh8DBYsBQzpcVXNlcnNcQWRtaW5pc3RyYXRvclxEb2N1bWVudHNcVmlzdWFsIFN0dWRpbyAyMDEwXFByb2plY3RzXEVzcHJpdF8wOF8wNl8xOVxFU1BPbmxpbmVcRVNQT25saW5lXERPQ1xFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAyOC0wMi0yMDIyLnBkZmRkAgIPZBYCAgEPDxYCHwMFiwFDOlxVc2Vyc1xBZG1pbmlzdHJhdG9yXERvY3VtZW50c1xWaXN1YWwgU3R1ZGlvIDIwMTBcUHJvamVjdHNcRXNwcml0XzA4XzA2XzE5XEVTUE9ubGluZVxFU1BPbmxpbmVcRE9DXEVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDI4LTAyLTIwMjIucGRmZGQCCw9kFgZmDw8WAh8ABSZFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAyOC0wMy0yMDIyLnBkZmRkAgEPZBYCAgEPDxYCHwMFiwFDOlxVc2Vyc1xBZG1pbmlzdHJhdG9yXERvY3VtZW50c1xWaXN1YWwgU3R1ZGlvIDIwMTBcUHJvamVjdHNcRXNwcml0XzA4XzA2XzE5XEVTUE9ubGluZVxFU1BPbmxpbmVcRE9DXEVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDI4LTAzLTIwMjIucGRmZGQCAg9kFgICAQ8PFgIfAwWLAUM6XFVzZXJzXEFkbWluaXN0cmF0b3JcRG9jdW1lbnRzXFZpc3VhbCBTdHVkaW8gMjAxMFxQcm9qZWN0c1xFc3ByaXRfMDhfMDZfMTlcRVNQT25saW5lXEVTUE9ubGluZVxET0NcRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMjgtMDMtMjAyMi5wZGZkZAIMD2QWBmYPDxYCHwAFJkVtcGxvaSBkdSB0ZW1wcyBTZW1haW5lIDMxLTAyLTIwMjIucGRmZGQCAQ9kFgICAQ8PFgIfAwWLAUM6XFVzZXJzXEFkbWluaXN0cmF0b3JcRG9jdW1lbnRzXFZpc3VhbCBTdHVkaW8gMjAxMFxQcm9qZWN0c1xFc3ByaXRfMDhfMDZfMTlcRVNQT25saW5lXEVTUE9ubGluZVxET0NcRW1wbG9pIGR1IHRlbXBzIFNlbWFpbmUgMzEtMDItMjAyMi5wZGZkZAICD2QWAgIBDw8WAh8DBYsBQzpcVXNlcnNcQWRtaW5pc3RyYXRvclxEb2N1bWVudHNcVmlzdWFsIFN0dWRpbyAyMDEwXFByb2plY3RzXEVzcHJpdF8wOF8wNl8xOVxFU1BPbmxpbmVcRVNQT25saW5lXERPQ1xFbXBsb2kgZHUgdGVtcHMgU2VtYWluZSAzMS0wMi0yMDIyLnBkZmRkAg0PDxYCHgdWaXNpYmxlaGRkGAEFI2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkR3JpZFZpZXcxDzwrAAwBCAIBZATyI51nwY91iY2GOSUq03Uspmg3DYy5J3nZL7V95dQm',
    '__VIEWSTATEGENERATOR':  'B1920FD1',
}

# Save this week's schedule to disk
response = session.post(auth_url, data=payload)
open("schedule.pdf", "wb").write(response.content)

# Leave the rest to sched_extract.sh
proc = subprocess.Popen(["bash", "sched_extract.sh", config['class']], stdout=subprocess.PIPE)
out, err = proc.communicate()
