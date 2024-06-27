from urllib import response
import requests
import urllib3
import socket
import re
from links import l_api



#robo_name = str(socket.gethostname())
#robo_id_s = re.findall(r'\d{3}', robo_name)
#robo_id = str(robo_id_s[0])
robo_id='1'


def check_fila():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        headers = {
            'Content-Type': 'application/json',
            'robo-id': ""+robo_id+""
        }
        url = l_api

        response = requests.get(
            url,
            headers = headers,
            verify = False
        )

        j= response.json()
        return j
        
    except:
        j = 'Erro de Comunicação com a API'
        print(j)
        return j