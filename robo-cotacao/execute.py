from cripto import busca_cripto
from moeda import busca_moeda
from com_robo import robo_id



def option(parametro):
    robo = robo_id
    par = parametro['parametros']
    code = parametro['code']
    item = par['how_can_i_help_you']

    if item == 'Dolar':
        dolar (code, robo)
    elif item == 'Euro':
        euro(code, robo)
    elif item == 'Bitcoin':
        bitcoin(code, robo)
    elif item == 'Ether':
        ether(code, robo)

def dolar(code, robo):
    cotacao_dolar = busca_moeda(pesquisa='cotação dólar')
    if(cotacao_dolar[0] == '200'):
        print(cotacao_dolar)
    else:
        print(cotacao_dolar)
        print('Erro na automação! Tente novamente mais tarde.')

def euro(code, robo):
    cotacao_euro = busca_moeda(pesquisa='cotação euro')
    if(cotacao_euro[0] == '200'):
        print(cotacao_euro)
    else:
        print(cotacao_euro)
        print('Erro na automação! Tente novamente mais tarde.')

def bitcoin(code, robo):
    cotacao_bit = busca_cripto(pesquisa='cotação bitcoin')
    if(cotacao_bit[0] == '200'):
        print(cotacao_bit)
    else:
        print(cotacao_bit)
        print('Erro na automação! Tente novamente mais tarde.')

def ether(code, robo):
    cotacao_ether = busca_cripto(pesquisa='ether hoje')
    if(cotacao_ether[0] == '200'):
        print(cotacao_ether)
    else:
        print(cotacao_ether)
        print('Erro na automação! Tente novamente mais tarde.')


"""
#EXEMPLO PARA POSTMAN

{
    "code": "teste",
    "parametros": {
        "how_can_i_help_you": "Bitcoin"
    }
}

"""