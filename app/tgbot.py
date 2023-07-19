import requests


def send_messege(doktornik, xamshiranik, xona, bemorism):
    token = "6331128208:AAE7zj1VCI5lo1XWR7XwnisOlGE5q447ujU"
    chat_id = "-756061713"
    msg = f"{xona.id}ga {doktornik} bilan {xamshiranik} borsin. {bemorism}ni korishga"
    url = "https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chat_id + "&parse_mode=HTML&text=" + msg
    requests.get(url)
