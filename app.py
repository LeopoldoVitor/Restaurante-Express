import os
from actions import Actions

REGISTER = 1 
LISTS = 2
ACTIVATE = 3 

def invalid_option():
    os.system('clear')
    print('Opção inválida')
    input('Pressione qualquer tecla para voltar ao menu principal ')

def main():
    print('''
      Sabor Express 
      ''')
    
    while True:
        print('''
1. Cadastrar Restaurante''')
        print('2. Listar Restaurante')
        print('3. alternar estado do Restaurante')
        print('4. Sair \n')

        try:
            option_chosen = int(input('Escolha uma opção: '))

            if option_chosen == REGISTER:
                Actions.register_restaurant()
            elif option_chosen == LISTS:
                Actions.lists_restaurants()
            elif option_chosen == ACTIVATE:
                Actions.state_change()
            elif option_chosen == 4:
                os.system('clear')
                print('Encerrando...')
                break
            else:
                invalid_option()
        except:
            invalid_option()

if __name__ == '__main__':
    main()