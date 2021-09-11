from urllib.request import urlopen
from time import time, sleep


while True:
    sleep(600 - time() % 600)
    url = "URL"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    Prim_index = html.find("YourSearch")
    End_index = Prim_index + len("YourSearch")
    Info = html[Prim_index:End_index]
    print(Info)
