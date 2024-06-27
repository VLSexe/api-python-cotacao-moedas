import time
from com_robo import check_fila, robo_id
from execute import option



while True:

    try:
        parametro = check_fila()

        fila_check = "Fila vazia."
        fila_check2= "Erro de Comunicação com a API"

        if fila_check in parametro:
            print(parametro)
        
        elif fila_check2 in parametro:
            print("Erro inesperado!")
            print(parametro)

        else:
            print("Pedido encontrado na fila\n")
            option(parametro)
        
        time.sleep(1)

    except KeyboardInterrupt:
        print('Não é permitido interromper o trabalho!')

    except Exception as e:
        try:
            print(e)
        except:
            print("Erro encontrado no robô!")            