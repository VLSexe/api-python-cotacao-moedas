import time


def valida_erro(moeda):
    if moeda:
        erro_type = ['200', 'OK']
    else:
        erro_type = ['400', 'ERRO']
        
    return erro_type