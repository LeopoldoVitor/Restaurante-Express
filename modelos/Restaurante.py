from modelos.Avaliacao import Avaliacao
import os

class Restaurante:

    listRestaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.listRestaurantes.append(self)

    @property
    def ativo(self):
        return 'ativado' if self._ativo else 'desativado'
    
    @property
    def media_avaliacoes(self):
        return round((sum(avaliacao._nota for avaliacao in self._avaliacoes) / len(self._avaliacoes)), 1) if self._avaliacoes else '-'
        
    def find_restaurant(restaurant_name):
         this_restaurant = next((r for r in Restaurante.listRestaurantes if r._nome == restaurant_name.title()), None)
         return this_restaurant
    
    def give_feedback():
        os.system('clear')
        for restaurant in Restaurante.listRestaurantes:
            if restaurant._ativo:
                print(f'{restaurant._nome}')
            
        chosen_restaurant = input('Digite o nome do restaurante que deseja dar feedback: ')
        this_restaurant = Restaurante.find_restaurant(chosen_restaurant)
        if this_restaurant:
            name = input('Digite seu nome: ')
            score = float(input('Digite a nota de 1 a 5: '))
            if 0 < score <= 5:
                this_restaurant.get_feedback(name, score)
                print(f'Feedback enviado com sucesso para o restaurante {this_restaurant._nome}')
            else:
                print('Nota inválida')
    
    def get_feedback(self, nome, nota):
        avaliacao = Avaliacao(nome, nota)
        self._avaliacoes.append(avaliacao)

    def __str__(self):
        return f'{self._nome.ljust(15)} | {self._categoria.ljust(15)} | {self.media_avaliacoes.ljust(15)} | {self.ativo}'