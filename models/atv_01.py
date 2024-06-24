import sys
import os 
from models.avaliacao import Avaliacao # importando classe!! 

class Item_audio: # classe Pai
    def __init__(self, nome, duracao, tipo):
        self._nome = nome
        self._duracao = float(duracao)
        self._tipo = tipo


class PodCast(Item_audio): # sub classe
    podcasts = []
    def __init__(self, nome, duracao, espisodio, anfitriao):
        super().__init__(nome, duracao, 'PodCast')
        self._episodio = espisodio
        self._anfitriao = anfitriao
        self._avaliacao = []
        PodCast.podcasts.append(self)

    def receber_avaliacao(self, ouvinte, nota):
        avaliacao = Avaliacao(ouvinte, nota)
        self._avaliacao.append(avaliacao)

    @classmethod
    def listar_podcast(cls):
        print(f'{"Podcast".ljust(25)} | {"Anfitrião".ljust(25)} | {"Duração".ljust(25)} | {"episodio".ljust(25)} | {"Nota"}')
        for podcast in cls.podcasts:
            print(f'{podcast._nome.ljust(25)} | {podcast._anfitriao.ljust(25)} | {podcast._duracao} | {podcast._episodio} | {podcast.media_avaliacao}' ) 
        
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
    

class AudioBook(Item_audio):
    audio_books = []
    def __init__(self, nome, duracao, autor):
        super().__init__(nome, duracao, "AudioBook")
        self._autor = autor
        self._avaliacao = []
        AudioBook.audio_books.append(self)

    def receber_avaliacao(self, ouvinte, nota):
        avaliacao = Avaliacao(ouvinte, nota)
        self._avaliacao.append(avaliacao)

    @classmethod
    def listar_audiobook(cls):
        print(f'{"AudioBook".ljust(25)} | {"Autor".ljust(25)} | {"Duração".ljust(25)} | {"Nota"}')
        for audiobook in cls.audio_books:
            print(f'{audiobook._nome.ljust(25)} | {audiobook._autor.ljust(25)} | {audiobook._duracao} | {audiobook.media_avaliacao}')


    
        
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


class Musica(Item_audio): #sub classe
    musicas = []
    def __init__(self,nome, cantor, categoria, duracao):
        super().__init__(nome,duracao, 'Música')
        self._cantor = cantor
        self._categoria = categoria.upper() # todas a letras maiusculas 
        self._logo = categoria.upper() # não aparece para o usuario
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

def inserir_audio():
    '''INSERE A MUSICA ATRAES DAS ENTRADAS DO USUSARIO'''
    subtitulo("INSIRA SEU AÚDIO")
    nome = str(input('Digite o nome do aúdio: '))
    tipo = str(input('Digite o tipo do aúdio (Musica, PodCast, AudioBook): '))
    duracao = float(input('Digite a duração do aúdio: '))

    if tipo.upper() == "MUSICA":
        musica = nome
        cantor = str(input('Digite o cantor da música: '))
        categoria = str(input('Digite a categoria da música: '))
        musica = Musica(nome,cantor,categoria,duracao)
        while True:
            ''' CRIANDO O INPUT DA NOTA COM TRATAMENTO PARA ERRO '''
            try:
                nota = float(input("Nota para a Música"))
                musica.receber_avaliacao('Anônimo', nota)
                break
            except ValueError as e: 
                print('Erro Tente Novamente!!')
                input("tecle para tentar novamente.")
        print('Música adicionada com sucesso!\n')
        input("Clique e volte ao menu")
        menu()
    elif tipo.upper() == "PODCAST":
        pod = nome
        anfitriao = str(input("Digite nome do anfitrião: "))
        episodio = int(input("Digite o episódio: "))
        pod = PodCast(nome, duracao, episodio, anfitriao)
        while True:
            ''' CRIANDO O INPUT DA NOTA COM TRATAMENTO PARA ERRO '''
            try:
                nota = float(input("Nota para Podcast"))
                pod.receber_avaliacao('Anônimo', nota)
                break
            except ValueError as e: 
                print('Erro Tente Novamente!!')
                input("tecle para tentar novamente.")
        print('Podcast adicionado com sucesso!\n')
        input("Clique e volte ao menu")
        menu()
    elif tipo.upper() == "AUDIOBOOK":
        book = nome
        autor = str(input("Digite nome do autor: "))
        book = AudioBook(nome, duracao, autor)
        while True:
            ''' CRIANDO O INPUT DA NOTA COM TRATAMENTO PARA ERRO '''
            try:
                nota = float(input("Nota para o AudioBook"))
                book.receber_avaliacao('Anônimo', nota)
                break
            except ValueError as e: 
                print('Erro Tente Novamente!!')
                input("tecle para tentar novamente.")
        print('AudioBook adicionado com sucesso!\n')
        input("Clique e volte ao menu")
        menu()




def listar():
    '''LISTAR AS MUSICAS '''
    print('1- Listar Musicas \n 2- Listar Podcast \n 3- Listar Audiobook')
    try: 
        escolha = int(input("O que deseja listar: "))
        if escolha == 1:
            subtitulo("LISTANDO MÚSICAS")
            Musica.listar_musicas()
            input('Tecle para voltar ao menu')
            menu()
        if escolha == 2:
            subtitulo("LISTANDO PODCAST")
            PodCast.listar_podcast()
            input('Tecle para voltar ao menu')
            menu()
        if escolha == 3:
            subtitulo("LISTANDO AudioBooks")
            AudioBook.listar_audiobook()
            input('Tecle para voltar ao menu')
            menu()
        
    except:
        opcao_invalida()

def menu():
    '''LISTAR OPÇOES NO MENU PRINCIPAL'''
    subtitulo('Menu Principal')
    print(' 1 - Menu \n 2 - Inserir Item de aúdio \n 3- Listar aúdios \n 4- Encerrar App')
    try :
        escolha = int(input("Escolha entre as opções: "))
        if escolha == 1:
            menu()
        elif escolha == 2:
            inserir_audio()
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
