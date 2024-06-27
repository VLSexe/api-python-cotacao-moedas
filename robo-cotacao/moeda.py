from selenium import webdriver
import time
import re
from valida_erros import valida_erro



def busca_moeda(pesquisa):
    browser = webdriver.Chrome('chromedriver.exe')
    time.sleep(10)
    browser.get('https://www.google.com/search?q=' + pesquisa)
    try:
        moeda = browser.find_element_by_xpath(r"//div[@class='dDoNo ikb4Bb gsrt']").get_attribute("innerHTML")
        moeda = re.findall(r'<span class="DFlfde SwHCTb" data-precision="\d" data-value="(.*?)">', moeda)
        valid = valida_erro(moeda)
        time.sleep(10)
        if(valid[0] == '200'):
            valid = valida_erro(moeda)
        for m in moeda:
            valid.append(m)
        return valid

    except:
        moeda = ''
        valid = valida_erro(moeda)
        return valid 