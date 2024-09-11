import requests,os, pyfiglet, sys
from bs4 import BeautifulSoup
from colorama import Style, Fore, init
### [PGX] - NINGUN SISTEMA ES SEGURO ###
### Laxybuz ###
init(autoreset=True)
r=pyfiglet.figlet_format("Laxybuz")

so=os.name
if so == 'nt':
 os.system('cls')
else:
 os.system('clear')
file=sys.argv[0]
exe=f'python {file}'
print(f"{Fore.RED}{Style.BRIGHT}{r}")
url = 'https://www.sistemaspnp.com/cedula/resultado.php'
ci = input("Cedula De Identidad -> ")
data = { "cedula": ci }
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
x = requests.post(url, data=data, headers=headers)
xy=len(x.text)

if int(xy) == 1623:
 print(f"{Fore.RED}{Style.BRIGHT}{ci} No se encontro en la base de datos\n")
else:
 print(f'{Fore.GREEN}{Style.BRIGHT}ENCONTRADO EN LA BASE DE DATOS\n')

soup = BeautifulSoup(x.text, 'html.parser')
y = soup.find_all('p')
for tag in y:
  x=tag.text
  r=x.find('búsqueda')
  if r != -1:
   pass
  else:
   split=str(x).split(':')
   n=len(split[0])
   if n > 0:
    b=split[0]
    d1=split[1:][0]
    print(f"{Fore.GREEN}{Style.BRIGHT}{b}->{Fore.WHITE}{d1} ")
input('\n')
os.system(exe)

