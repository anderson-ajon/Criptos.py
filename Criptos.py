import requests
import os
import time
import winsound
from datetime import datetime
from colorama import Fore, Back, Style, init
init()

# Variáveis de iniialização
contador = 0
ultimo_volume = None  # guarda o volume anterior
traço = 60
decimais = 8
#cripto = 'DG'
cripto = input("Digite a cripto (BTC, ETH, DOGE, LTC, ADA, XRP, DG): ").upper()

while True:
    #winsound.Beep(1000, 500)  # frequência (Hz), duração (ms)
    #winsound.MessageBeep()
    
    inicio = datetime.now()

    os.system("cls")  # Windows
    #os.system("pause")  # Windows

    contador += 1
    print(f"Execução #{contador}")

    print("Início:", inicio.strftime("%H:%M:%S"))    

    #url = f"https://www.mercadobitcoin.net/api/{cripto}/ticker/".format(cripto)
    url = f"https://www.mercadobitcoin.net/api/{cripto}/ticker/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    #print(url)

    #print(f"Solicitação {cripto} em andamento".format(cripto)) 
    #print(Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + f"-------------------- Solicitação {cripto} em andamento -------------------" + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + f" Solicitação {cripto} em andamento ".center(traço,"-") + Style.RESET_ALL)

    response = requests.get(url,headers=headers,timeout=5)

    dados = response.json()

    ticker = dados["ticker"]
    
    volume_atual = float(ticker["vol"])
    
    # comparação de volume
    #if ultimo_volume is not None and volume_atual != ultimo_volume:
    #    winsound.Beep(1000, 500)
    #    valor_alt = "Alterado!"
    #else:
    #    valor_alt = "Inalterado!"
        
    # aqui o if já terminou   

    valor_alt = " * * * * * "
    dif = 0.0
    dif_texto = ""
    
    if ultimo_volume is not None:

        diferenca = volume_atual - ultimo_volume        

        if diferenca > 0:
            #winsound.Beep(1200, 400)
            winsound.Beep(800,500)
            valor_alt = "Alterado"
            dif = diferenca
            #print(Fore.GREEN + f"Volume aumentou ↑ +{diferenca:.4f}" + Style.RESET_ALL)
            dif_texto = Fore.GREEN + f"Volume aumentou ↑ +{dif:.{decimais}f}" + Style.RESET_ALL

        elif diferenca < 0:
            #winsound.Beep(1200, 400)
            winsound.Beep(1000,500)
            valor_alt = "Alterado"
            dif = diferenca
            #print(Fore.RED + f"Volume diminuiu ↓ {diferenca:.4f}" + Style.RESET_ALL)
            dif_texto = Fore.RED + f"Volume diminuiu ↓ {dif:.{decimais}f}" + Style.RESET_ALL

        else:
            #print("Volume não mudou")
            valor_alt = "Inalterado"
            #dif = float("0.00":.{decimais}f)
            dif = 0.0
            dif_texto = f"{dif:.{decimais}f}"

    else:
        print("Primeira leitura de volume")

    
    ultimo_volume = volume_atual
    
    print("-" * traço)
    #print("Preço atual:", Back.YELLOW + Fore.BLACK + ticker["last"] + Style.RESET_ALL)
    print("Preço atual:", Back.YELLOW + Fore.BLACK + f"  {float(ticker['last']):.{decimais}f} " + Style.RESET_ALL)

    print("-" * traço)

    print("Preço Compra:", Back.GREEN + Fore.LIGHTWHITE_EX + f" {float(ticker['buy']):.{decimais}f} " + Style.RESET_ALL, end=" | ")
    print("Preço Venda:", Back.RED + Fore.LIGHTWHITE_EX + f" {float(ticker['sell']):.{decimais}f} " + Style.RESET_ALL)

    print("-" * traço)

    #print("Menor do dia:", ticker["low"], end=" | ")
    print("Menor do dia:", f" {float(ticker['low']):.{decimais}f} ", end=" | ")
    #print("Maior do dia:", ticker["high"])    
    print("Maior do dia:", f"{float(ticker['high']):.{decimais}f} ")    

    print("-" * traço)

    print("Volume:", volume_atual, end=" | ")
    print(valor_alt, end=" | ")
    #print("Diferença:", dif)    
    print("Diferença:", dif_texto)

    print("-" * traço)
    #print("Data:", ticker["date"])

    timestamp = ticker["date"]
    data = datetime.fromtimestamp(timestamp)

    print("Data:", data.strftime("%d/%m/%Y %H:%M:%S"))

    print("-" * traço)

    fim = datetime.now()
    print("Fim:", fim.strftime("%H:%M:%S"))

    tempo_execucao = fim - inicio

    #print(Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + "Tempo de execução:", tempo_execucao, end=" | ")
    #print("Tempo (s):", tempo_execucao.total_seconds(), Style.RESET_ALL)

    #print(Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + "Tempo de execução:", tempo_execucao, end=" | ")
    #print("Tempo (s):", str(tempo_execucao.total_seconds()).ljust(80, "-"), Style.RESET_ALL)

    #texto = f"Tempo de execução: {tempo_execucao} | Tempo (s): {tempo_execucao.total_seconds():.2f}"
    texto = f"Tempo de execução: {tempo_execucao} | Tempo (s): {tempo_execucao.total_seconds()} "
    
    print(
        Back.LIGHTBLUE_EX +
        Fore.LIGHTWHITE_EX +
        texto.ljust(traço, "-") +
        Style.RESET_ALL
    )

    #time.sleep(60)  # 60 segundos
    time.sleep(300)  # 300 segundos   
