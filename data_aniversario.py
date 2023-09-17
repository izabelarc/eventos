import datetime

data = datetime.date.today()
print(f"O dia de hoje é: {data.day}/{data.month}/{data.year}")

dia = int(input("Digite o dia do seu aniversário: "))
mes = int(input("Digite o mês do seu aniversário: "))
ano = int(input("Digite o ano do seu aniversário: "))
print(f"{dia}/{mes}/{ano}")