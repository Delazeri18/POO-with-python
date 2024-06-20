import sys
import os 
from models.avaliacao import Avaliacao # importando classe!! 

class Musica:
    musicas = []
    def __init__(self, nome, cantor, categoria, duracao):
        self._nome = nome.title() # função para manter a primeira letra maiuscula (colocando o '_' ele não pode ser alterado dps de criado.)
        self._cantor = cantor
        self._categoria = categoria.upper() # todas a letras maiusculas 
        self._logo = categoria.upper() # não aparece para o usuario
        self._duracao = duracao
        self._avaliacao = [] # infomações não manipulada assim que intancia o objeto. 
        Musica.musicas.append(self) 

    def receber_avaliacao(self, ouvinte, nota):
        avaliacao = Avaliacao(ouvinte, nota)
        self._avaliacao.append(avaliacao)
    
    @classmethod # metodo da classe
    def listar_musicas(cls):
        print(f'{"Música".ljust(25)} | {"Cantor".ljust(25)} | {"Categoria".ljust(25)} | {"Duração".ljust(25)} | {"Nota"}')
        for musica in cls.musicas:
            print(f'{musica._nome.ljust(25)} | {musica._cantor.ljust(25)} | {musica._categoria.ljust(2)}{musica.logo.ljust(21)} | {musica.duracao_tratada.ljust(25)} | {musica.media_avaliacao}' ) 
            # não pode colocar o _ para uma propriedade

    @property # forma de como aquele atributo será lido, usado para operaçoes matematicas e entre outras coisas. 
    def logo(self): # nome da função deve ser o mesmo do atributo da classe
        if self._logo == "HIP HOP":
            return '🎧'
        elif self._logo == "PAGODE":
            return '🥁'
        elif self._logo == "GOSPEL":
            return '🪽'
        elif self._logo == "JAZZ":
            return '🎷'
        elif self._logo == "FUNK":
            return '🎭'
        elif self._logo == "ROCK":
            return '🎸'
        elif self._logo == "SERTANEJO":
            return '👒'
        else: 
            return '🎵'    

   
    # forma de como aquele atributo será lido, usado para operaçoes matematicas e entre outras coisas. 
    @property
    def media_avaliacao(self):
        ''' TIRANDO MEDIA DAS AVALIACOES  '''
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao) #pega todas as avalicoes e pega apenas as notas e some.
        quantidade_notas = len(self._avaliacao)
        media = round(soma/quantidade_notas, 1)
        return media
    
    @property
    def duracao_tratada(self):
        ''' TRATANDO A ENTRADA DE DURAÇÃO '''
        minutos = int(self._duracao)
        sec = int((self._duracao - minutos)*100)
        return f"{minutos}:{sec:2}"

def subtitulo(texto):
    ''' ESTILOS '''
    os.system('cls')
    traco = '-'*6
    print(f'{traco} {texto} {traco}\n')

def opcao_invalida():
    ''' MENSAGEM DE OPÇÃO INVÁLIDA '''
    print('Escolha uma opção válida')
    input('tecle para voltar ao menu')
    menu()


def Finalizar_app():
    ''' MESNSAGEM DE APP FINALIZADO '''
    subtitulo('Finalizando App!!')
    sys.exit

def inserir_musica():
    '''INSERE A MUSICA ATRAES DAS ENTRADAS DO USUSARIO'''
    subtitulo("INSIRA SUA MÚSICA")
    nome = str(input('Digite o nome da música: '))
    nomes = nome
    cantor = str(input('Digite o cantor da música: '))
    categoria = str(input('Digite a categoria da música: '))
    duracao = float(input('Digite a duração da música: '))
    nomes = Musica(nome,cantor,categoria,duracao)
    
    while  True:
        ''' CRIANDO O INPUT DA NOTA COM TRATAMENTO PARA ERRO '''
        try:
            nota = float(input("Nota para a Música"))
            nomes.receber_avaliacao('Anônimo', nota)
            break
        except ValueError as e: 
            print('Erro Tente Novamente!!')
            input("tecle para tentar novamente.")
    print('Adicionada com Sucesso!!')
    input('Tecle para voltar ao menu')
    menu()


def listar():
    '''LISTAR AS MUSICAS '''
    subtitulo("LISTANDO MÚSICAS")
    Musica.listar_musicas()
    input('Tecle para voltar ao menu')
    menu()

def menu():
    '''LISTAR OPÇOES NO MENU PRINCIPAL'''
    subtitulo('Menu Principal')
    print(' 1 - Menu \n 2 - Inserir Música \n 3- Listar Músicas \n 4- Encerrar App')
    try :
        escolha = int(input("Escolha entre as opções: "))
        if escolha == 1:
            menu()
        elif escolha == 2:
            inserir_musica()
        elif escolha == 3:
            listar()
        elif escolha == 4:
            Finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' TELA INICIAL '''
    subtitulo('BEM VINDO AO APP!!')
    input("Tecle para ir ao menu")
    menu()
