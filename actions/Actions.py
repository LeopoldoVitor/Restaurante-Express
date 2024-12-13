import os
from modelos.Restaurante import Restaurante

def register_restaurant():
    while True:
        os.system('clear')
        print('Cadastre seu restaurante')
        name_restaurant = input('Digite o nome do restaurante: ')
        restaurant_class = input('Digite a categoria do restaurante: ')

        restaurant =  Restaurante(name_restaurant, restaurant_class)
        print(f'O restaurante { restaurant._nome } foi cadastrado com sucesso \n')
        yes_no = input('Deseja cadastrar outro restaurante? s/n ')
        if yes_no != 's':
            break
    back_to_menu()

def lists_restaurants():
    os.system('clear')
    if Restaurante.listRestaurantes:
        print(f'{'Nome'.ljust(15)} | {'Categoria'.ljust(15)} | {'Nota'.ljust(15)} | {'Status'}')

        for restaurant in Restaurante.listRestaurantes:
            print(restaurant)
              
        yes_no = input('quer avaliar um restaurante? s/n  ')
        if yes_no == 's':
            if True in [r._ativo for r in Restaurante.listRestaurantes]:
                Restaurante.give_feedback()
            else:
                input('Nenhum restaurante ativo')           
    else:
        input('Nenhum restaurante cadastrado')
    back_to_menu()

def state_change():
    os.system('clear')
    if Restaurante.listRestaurantes:
        for restaurant in Restaurante.listRestaurantes:
            print(f'{restaurant._nome} | {restaurant.ativo}')
            
        chosen_restaurant = input('Digite o nome do restaurante que deseja alternar o estado (ativar/desativar): ')
        this_restaurant = Restaurante.find_restaurant(chosen_restaurant)
        if this_restaurant:
            this_restaurant._ativo = not this_restaurant._ativo
            print(f'O restaurante {this_restaurant._nome} foi {this_restaurant.ativo} com sucesso')
        else:
            print('Restaurante não encontrado')
    else:
        input('Nenhum restaurante cadastrado')

    back_to_menu()

def back_to_menu():
    input('Pressione qualquer tecla para voltar ao menu principal ')
    os.system('clear')
