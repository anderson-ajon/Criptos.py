import requests
import os
import time
from datetime import datetime
from colorama import Fore, Back, Style, init
init()

contador = 0

while True:        
    inicio = datetime.now()

    os.system("cls")  # Windows
    #os.system("pause")  # Windows

    contador += 1
    print(f"Execução #{contador}")

    print("Início:", inicio.strftime("%H:%M:%S"))

    cripto = 'DG'

    #url = f"https://www.mercadobitcoin.net/api/{cripto}/ticker/".format(cripto)
    url = f"https://www.mercadobitcoin.net/api/{cripto}/ticker/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    #print(url)

    #print(f"Solicitação {cripto} em andamento".format(cripto)) 
    print(Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + f"-------------- Solicitação {cripto} em andamento -------------" + Style.RESET_ALL)

    response = requests.get(url,headers=headers,timeout=5)

    dados = response.json()

    ticker = dados["ticker"]
    
    print("--------------------------------------------------------")
    print("Preço atual:", Back.YELLOW + Fore.BLACK + ticker["last"] + Style.RESET_ALL)
    print("--------------------------------------------------------")
    print("Preço Compra:", Back.GREEN + Fore.LIGHTWHITE_EX + ticker["buy"] + Style.RESET_ALL, end=" | ")
    print("Preço Venda:", Back.RED + Fore.LIGHTWHITE_EX + ticker["sell"] + Style.RESET_ALL)
    print("--------------------------------------------------------")
    print("Maior do dia:", ticker["high"], end=" | ")
    print("Menor do dia:", ticker["low"])
    print("--------------------------------------------------------")
    print("Volume:", ticker["vol"])
    print("--------------------------------------------------------")
    #print("Data:", ticker["date"])

    timestamp = ticker["date"]
    data = datetime.fromtimestamp(timestamp)

    print("Data:", data.strftime("%d/%m/%Y %H:%M:%S"))
    print("--------------------------------------------------------")

    fim = datetime.now()
    print("Fim:", fim.strftime("%H:%M:%S"))

    tempo_execucao = fim - inicio
    print(Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + "Tempo de execução:", tempo_execucao, end=" | ")
    print("Tempo (s):", tempo_execucao.total_seconds(), Style.RESET_ALL)

    #time.sleep(60)  # 60 segundos
    time.sleep(300)  # 300 segundos
    

    #{'ticker': {'high': '0.00147000', 'low': '0.00112003',
    #'vol': '948002.45927968', 'last': '0.00129998', 'buy': '0.00112300',
    #'sell': '0.00145887', 'open': '0.00145990', 'date': 1770039666,
    #'pair': 'BRLDG'}}



