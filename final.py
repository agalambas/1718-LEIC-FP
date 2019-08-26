# 86372 ALEXANDRE GALAMBAS
# FUNDAMENTOS DA PROGRAMACAO - PROJETO 2

from itertools import permutations
from part1_sol import e_palavra

# TAD palava_potencial
# cria_palavra_potencial: cad. caracteres x tuplo de letras -> palavra_potencial
def cria_palavra_potencial(cad, tup):

    def cria_palavra_potencial_erro(tipo):
        if tipo == 1:
            raise ValueError('cria_palavra_potencial:argumentos invalidos.')
        elif tipo == 2:
            raise ValueError('cria_palavra_potencial:a palavra nao e valida.')

    if not isinstance(cad, str) or not isinstance(tup, tuple):
        cria_palavra_potencial_erro(1)
    for letra in tup:
        if not ord('A') <= ord(letra) <= ord('Z'):
            cria_palavra_potencial_erro(1)

    for letra in cad:
        if not ord('A') <= ord(letra) <= ord('Z'):
            cria_palavra_potencial_erro(1)
        if letra not in tup:
            cria_palavra_potencial_erro(2)
        i = tup.index(letra)
        tup = tup[:i] + tup[i+1:]

    return cad

# palavra_tamanho: palavra_potencial -> inteiro
def palavra_tamanho(pot):
    return len(pot);

# e_palavra_potencial: universal -> logico
def e_palavra_potencial(uni):
    if not isinstance(uni, str):
        return False
    for letra in uni:
        if not ord('A') <= ord(letra) <= ord('Z'):
            return False
    return True

# palavras_potenciais_iguais: palavra_potencial x palavra_potencial -> logico
def palavras_potenciais_iguais(pot1, pot2):
    return pot1 == pot2

# palavra_potencial_menor: palavra_potencial x palavra_potencial -> logico
def palavra_potencial_menor(pot1, pot2):
    if palavras_potenciais_iguais(pot1, pot2):
        return False

    dim1 = palavra_tamanho(pot1)
    dim2 = palavra_tamanho(pot2)

    if dim1 < dim2:
        dim = dim1
    else:
        dim = dim2

    for i in range(dim):
        if not pot1[i] == pot2[i]:
            return pot1[i] < pot2[i]

    return dim1 < dim2

# palavra_potencial_para_cadeia: palavra_potencial -> cad. caracteres
def palavra_potencial_para_cadeia(pot):
    cad = ''
    for letra in pot:
        cad += letra
    return cad

# TAD conjunto_palavras
class conjunto_palavras:
    def __init__(self):
        self.pots = {}
        self.dim = 0

# cria_conjunto_palavras: -> conjunto_palavras
def cria_conjunto_palavras():
    return conjunto_palavras();

# numero_palavras: conjunto_palavras -> inteiro
def numero_palavras(conj):
    return conj.dim

# subconjunto_por_tamanho: conjunto_palavras x inteiro -> lista
def subconjunto_por_tamanho(conj, dim):
    if dim not in conj.pots:
        return []
    return conj.pots[dim]

# acrescenta_palavra: conjunto_palavras x palavra_potencial ->
def acrescenta_palavra(conj, pot):
    if not e_conjunto_palavras(conj) or not e_palavra_potencial(pot):
        raise ValueError('acrescenta_palavra:argumentos invalidos.')

    dim = palavra_tamanho(pot)
    sconj = subconjunto_por_tamanho(conj, dim)
    if dim not in conj.pots:
        conj.pots[dim] = [pot]
        conj.dim += 1
    elif pot not in sconj:
        i = 0
        while i<len(sconj) and not palavra_potencial_menor(pot, sconj[i]):
            i += 1
        conj.pots[dim].insert(i,pot)
        conj.dim += 1

# e_conjunto_palavras: universal -> logico
def e_conjunto_palavras(uni):
    return isinstance(uni, conjunto_palavras)

# conjuntos_palavras_iguais: conjunto_palavras x conjunto_palavras -> logico
def conjuntos_palavras_iguais(conj1, conj2):
    iguais = True
    if not numero_palavras(conj1) == numero_palavras(conj2) or\
       not sorted(conj1.pots.keys()) == sorted(conj2.pots.keys()):
       iguais = False
    else:
       for dim in conj1.pots:
           if not subconjunto_por_tamanho(conj1, dim) == subconjunto_por_tamanho(conj2, dim):
               iguais = False

    return iguais

# conjunto_palavras_para_cadeia: conjunto_palavras -> cad. caracteres
def conjunto_palavras_para_cadeia(conj):
    cad = ''
    for dim in sorted(conj.pots.keys()):
        cad_aux = ''
        for pot in subconjunto_por_tamanho(conj, dim):
             cad_aux += palavra_potencial_para_cadeia(pot) + ', '
        cad += str(dim) + '->[' + cad_aux[:-2] + '];'

    return '[' + cad[:-1] + ']'

# TAD jogador
class jogador:
    def __init__(self, cad):
        self.nome = cad
        self.pontos = 0
        self.palavras_validas = cria_conjunto_palavras()
        self.palavras_invalidas = cria_conjunto_palavras()

# cria_jogador: cad. caracteres -> jogador
def cria_jogador(nome):
    if not isinstance(nome, str):
        raise ValueError('cria_jogador:argumento invalido.')
    return jogador(nome)

# jogador_nome: jogador -> cad. caracteres
def jogador_nome(jog):
    return jog.nome

# jogador_pontuacao: jogador -> inteiro
def jogador_pontuacao(jog):
    return jog.pontos

# jogador_palavras_validas: jogador -> conjunto_palavras
def jogador_palavras_validas(jog):
    return jog.palavras_validas

# jogador_palavras_invalidas: jogador -> conjunto_palavras
def jogador_palavras_invalidas(jog):
    return jog.palavras_invalidas

# adiciona_palavra_valida: jogador x palavra_potencial ->
def adiciona_palavra_valida(jog, pot):
    if not e_jogador(jog) or not e_palavra_potencial(pot):
        raise ValueError('adiciona_palavra_valida:argumentos invalidos.')
    if pot not in subconjunto_por_tamanho(jogador_palavras_validas(jog), palavra_tamanho(pot)):
        acrescenta_palavra(jogador_palavras_validas(jog), pot)
        jog.pontos += palavra_tamanho(pot)

# adiciona_palavra_valida: jogador x palavra_potencial ->
def adiciona_palavra_invalida(jog, pot):
    if not e_jogador(jog) or not e_palavra_potencial(pot):
        raise ValueError('adiciona_palavra_invalida:argumentos invalidos.')
    if pot not in subconjunto_por_tamanho(jogador_palavras_invalidas(jog), palavra_tamanho(pot)):
        acrescenta_palavra(jogador_palavras_invalidas(jog), pot)
        jog.pontos -= palavra_tamanho(pot)

# e_jogador: universal -> logico
def e_jogador(uni):
    return isinstance(uni, jogador)

# jogador_para_cadeia: jogador -> cad. caracteres
def jogador_para_cadeia(jog):
    return 'JOGADOR ' + jog.nome +\
           ' PONTOS=' + str(jog.pontos) +\
           ' VALIDAS=' + conjunto_palavras_para_cadeia(jog.palavras_validas) +\
           ' INVALIDAS=' + conjunto_palavras_para_cadeia(jog.palavras_invalidas)

# funcoes adicionais
# gera_todas_palavras_validas: tuplo de letras -> conjunto_palavras
def gera_todas_palavras_validas(tup):
    conj_aux = ()
    for i in range(len(tup)):
        conj_aux += tuple(permutations(tup, i+1))

    conj = cria_conjunto_palavras()
    for el in conj_aux:
        el = ''.join(el)
        if e_palavra(el):
            acrescenta_palavra(conj, cria_palavra_potencial(el, tup))

    return conj

# guru_mj: tuplo de letras ->
def guru_mj(tup):

    print('Descubra todas as palavras geradas a partir das letras:\n' + str(tup))

    jogadores = ()
    jog = 0
    print('Introduza o nome dos jogadores (-1 para terminar)...')

    while True:
        nome = input('JOGADOR ' + str(jog+1) + ' -> ')
        if nome != '-1':
            jogadores += (cria_jogador(nome),)
            jog += 1
        else:
            break

    total_jog = jog
    jog = 0
    num_jogada = 1
    todas_palavras = gera_todas_palavras_validas(tup)
    num_palavras_restantes = numero_palavras(todas_palavras)
    palavras_restantes = []
    for dim in todas_palavras.pots:
        palavras_restantes += subconjunto_por_tamanho(todas_palavras, dim)
    todas_palavras = palavras_restantes[:]

    while num_palavras_restantes > 0:

        print('JOGADA ' + str(num_jogada) + ' - Falta descobrir ' + str(num_palavras_restantes) + ' palavras')
        palavra = input('JOGADOR ' + jogadores[jog].nome + ' -> ')
        palavra = cria_palavra_potencial(palavra, tup)
        if palavra in todas_palavras:
            if palavra in palavras_restantes:
                adiciona_palavra_valida(jogadores[jog], palavra)
                palavras_restantes.remove(palavra)
                num_palavras_restantes -= 1
            palavra += ' - palavra VALIDA'
        else:
            adiciona_palavra_invalida(jogadores[jog], palavra)
            palavra += ' - palavra INVALIDA'
        print(palavra)

        num_jogada += 1
        jog = (jog+1) % total_jog

    maior_pontuacao = float('-inf')
    for jog in jogadores:
        pontuacao = jogador_pontuacao(jog)
        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            vencedor = jog.nome
            empate = False
        elif pontuacao == maior_pontuacao:
            empate = True

    if empate:
        print('FIM DE JOGO! O jogo terminou em empate.')
    else:
        print('FIM DE JOGO! O jogo terminou com a vitoria do jogador ' + vencedor + ' com ' + str(maior_pontuacao) + ' pontos.')

    for jog in jogadores:
        print(jogador_para_cadeia(jog))
