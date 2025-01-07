import random
import os
import sys
import platform

def resource_path(relative_path): #usado pra localizar o caminho absoluto da lista de palavras, para o caso de usar o PyInstaller, para criar um exe 
    try:
        # O PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def importar_Palavras(Nome_Arquivo):
    palavras = []
    caminho_arquivo = resource_path(Nome_Arquivo)
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                palavra = linha.strip().lower()
                palavras.append(palavra)
        return palavras
    except FileNotFoundError:
        print(f"Erro: Arquivo '{Nome_Arquivo}' não encontrado.")
        return [] # Retorna uma lista vazia em caso de erro    

def limpa_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def jogo():
    def reiniciarJogo():
        reiniciar = input("Deseja jogar novamente? (s/n): ").lower()
        if reiniciar == "s":
            jogo()
            return
        else:
            print("Obrigado por jogar!")
            return
    limpa_tela()
    
    palavras = importar_Palavras("Palavras.txt")
    if not palavras: # Verifica se a lista de palavras está vazia (erro ao carregar arquivo)
      return # Sai da função Main se o arquivo não foi carregado

    palavraSecreta = random.choice(palavras)
    letrasAcertadas = ""
    tentativas = 0
    limiteTentativas = (len(palavraSecreta)) + 5

    print(f"Dica: a palavra têm {len(palavraSecreta)} letras")
    print("Algumas palavras podem conter caracteres especiais. acentuação(~`^) e traços(-)")
    print(f"Você têm {limiteTentativas} tentativas.")

    while True:
        chute = input("Chute uma letra: ").lower()
    
        if chute in palavraSecreta:
            letrasAcertadas += chute
        palavraFormada = ""
        for Letra in palavraSecreta:
            if Letra in letrasAcertadas:
                palavraFormada += Letra
            else:
                palavraFormada += "_"
        tentativas += 1
        limiteTentativas -= 1
        print("palavraFormada: " + palavraFormada)
        print(f"Tentativas restantes: {limiteTentativas}")

        if limiteTentativas == 0:
            print("Você fez o número máximo de tentativas!")
            print(f"A palavra era: {palavraSecreta}") # Mostra a palavra secreta quando perde
            reiniciarJogo()
            return

        if palavraFormada == palavraSecreta:
            limpa_tela()
            print("Parabéns, você acertou a palavra secreta!!!")
            print("Palavra secreta: " + palavraSecreta)
            print("Número de tentativas: ", tentativas)
            reiniciarJogo()
            return

jogo()
