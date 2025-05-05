#Uso da Bliblioteca Python Colorama#
#Antes de dar o import, tem que fazer a instalação da biblioteca!
#Cole o comando no terminal do VS Code! Exemplo: "pip install colorama"

#E depois de ter feito a instalação, agora só basta da o import!
import colorama

print(colorama.Fore.RED + 'Este texto é vermelho' + colorama.Style.RESET_ALL)
print(colorama.Fore.GREEN + 'Este texto é verde' + colorama.Style.RESET_ALL)
print(colorama.Back.YELLOW + 'Fundo amarelo' + colorama.Style.RESET_ALL)
print(colorama.Style.BRIGHT + 'Texto em negrito' + colorama.Style.RESET_ALL)
print(colorama.Style.RESET_ALL + 'Resetando estilos para o padrão')

#Principais constantes disponíveis:
#Cores de texto (Fore)
#Fore.RED
# Fore.GREEN
# Fore.YELLOW
# Fore.BLUE
# Fore.MAGENTA
# Fore.CYAN
# Fore.WHITE
# Fore.BLACK
# Fore.RESET

#Cores de fundo (Back)
#Back.RED
# Back.GREEN
# Back.YELLOW
# Back.BLUE
# Back.MAGENTA
# Back.CYAN
# Back.WHITE
# Back.RESET

#Estilos (Style):
#Style.DIM – texto apagado
#Style.NORMAL – normal
#Style.BRIGHT – negrito/brilhante
#Style.RESET_ALL – reseta cor e estilo
