import requests
import json

def pedir_imc(nombre,estatura,peso):
    try:
        url = "http://192.168.1.135:8000/imc/calculador/{}/{}/{}".format(nombre,peso,estatura)
        payload = {}
        headers= {}
        response = requests.request("GET", url, headers=headers, data = payload)
        respuesta = json.loads(response.text)
        print(response.text.encode('utf8'))
        return respuesta["imc"]
    except Exception as e:
        return str(e)