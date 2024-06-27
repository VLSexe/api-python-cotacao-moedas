from selenium import webdriver
import time
import re
from valida_erros import valida_erro



def busca_cripto(pesquisa):
    browser = webdriver.Chrome('chromedriver.exe')
    time.sleep(10)
    browser.get('https://www.google.com/search?q=' + pesquisa)
    try:
        cripto = browser.find_element_by_xpath(r"//div[@class='dQnYeb KWnk8d']").get_attribute("innerHTML")
        cripto = re.findall(r'<input class="cilsF a61j6" value="(.*?)"', cripto)
        valid = valida_erro(moeda=cripto)
        time.sleep(10)
        if(valid[0] == '200'):
            valid = valida_erro(moeda=cripto)
        for m in cripto:
            valid.append(m)
        return valid

    except:
        moeda = ''
        valid = valida_erro(moeda = moeda)
        return valid 
    