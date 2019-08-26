# FUNDAMENTOS DA PROGRAMACAO
# 86372 ALEXANDRE GALAMBAS
# PROJETO 1


# <artigo_def> ::= A | O
def artigo_def(cad):
    return cad in ('A','O')

# <vogal_palavra> ::= <artigo_def> | E
def vogal_palavra(cad):
    return artigo_def(cad) or\
            cad == 'E'

# <vogal> ::= I | U | <vogal_palavra>
def vogal(cad):
    return cad in ('I','U') or\
            vogal_palavra(cad)

# <ditongo_palavra> ::= AI | AO | EU | OU
def ditongo_palavra(cad):
    return cad in ('AI','AO','EU','OU')

# <ditongo> ::= AE | AU | EI | OE | OI | IU | <ditongo_palavra>
def ditongo(cad):
    return cad in ('AE','AU','EI','OE','OI','IU') or\
            ditongo_palavra(cad)

# <par_vogais> ::= <ditongo> | IA | IO
def par_vogais(cad):
    return cad in ('IA','IO') or\
            ditongo(cad)

# <consoante_freq> ::= D | L | M | N | P | R | S | T | V
def consoante_freq(cad):
    return cad in ('D','L','M','N','P','R','S','T','V')

# <consoante_terminal> ::= L | M | R | S | X | Z
def consoante_terminal(cad):
    return cad in ('L','M','R','S','X','Z')

#<consoante_final> ::= N | P | <consoante_terminal>
def consoante_final(cad):
    return cad in ('N','P') or\
            consoante_terminal(cad)

# <consoante> ::= B | C | D | F | G | H | J | L | M | N | P | Q | R | S | T | V | X | Z
def consoante(cad):
    return cad in ('B','C','D','F','G','H','J','L','M','N','P','Q','R','S','T','V','X','Z')

# <par_consoantes> ::= BR | CR | FR | GR | PR | TR | VR | BL | CL | FL | GL | PL
def par_consoantes(cad):
    return cad in ('BR','CR','FR','GR','PR','TR','VR','BL','CL','FL','GL','PL')

# <monossilabo_2> ::= AR | IR | EM | UM |
# <vogal_palavra>S | <ditongo_palavra> | <consoante_freq><vogal>
def monossilabo_2(cad):
    c0 = cad[0]
    c1 = cad[1]
    return cad in ('AR','IR','EM','UM') or\
            (vogal_palavra(c0) and c1 == 'S') or\
            ditongo_palavra(cad) or\
            (consoante_freq(c0) and vogal(c1))

# <monossilabo_3> ::= <consoante><vogal><consoante_terminal> |
# <consoante><ditongo> | <par_vogais><consoante_terminal>
def monossilabo_3(cad):
    c0 = cad[0]
    c1 = cad[1]
    c2 = cad[2]
    return (consoante(c0) and vogal(c1) and consoante_terminal(c2)) or\
            (consoante(c0) and ditongo(c1+c2)) or\
            (par_vogais(c0+c1) and consoante_terminal(c2))

# <monossilabo> ::= <vogal_palavra> | <monossilabo_2> | <monossilabo_3>
def monossilabo(cad, dim):
    if dim == 1:
        return vogal_palavra(cad)
    elif dim == 2:
        return monossilabo_2(cad)
    elif dim == 3:
        return monossilabo_3(cad)
    else:
        return False

# <silaba_2> ::= <par_vogais> | <consoante><vogal> | <vogal><consoante_final>
def silaba_2(cad):
    c0 = cad[0]
    c1 = cad[1]
    return par_vogais(cad) or\
            (consoante(c0) and vogal(c1)) or\
            (vogal(c0) and consoante_final(c1))

# <silaba_3> ::= QUA | QUE | QUI | GUE | GUI |
# <vogal>NS | <consoante><par_vogais> | <consoante><vogal><consoante_final> |
# <par_vogais><consoante_final> | <par_consoantes><vogal>
def silaba_3(cad):
    c0 = cad[0]
    c1 = cad[1]
    c2 = cad[2]
    return cad in ('QUA','QUE','QUI','GUE','GUI') or\
            (vogal(c0) and c1+c2 == 'NS') or\
            (consoante(c0) and par_vogais(c1+c2)) or\
            (consoante(c0) and vogal(c1) and consoante_final(c2)) or\
            (par_vogais(c0+c1) and consoante_final(c2)) or\
            (par_consoantes(c0+c1) and vogal(c2))

# <silaba_4> ::= <par_vogais>NS | <consoante><vogal>NS | <consoante><vogal>IS |
# <par_consoantes><par_vogais> | <consoante><par_vogais><consoante_final>
def silaba_4(cad):
    c0 = cad[0]
    c1 = cad[1]
    c2 = cad[2]
    c3 = cad[3]
    return (par_vogais(c0+c1) and c2+c3 == 'NS') or\
            (consoante(c0) and vogal(c1) and c2+c3 in ('NS','IS')) or\
            (par_consoantes(c0+c1) and par_vogais(c2+c3)) or\
            (consoante(c0) and par_vogais(c1+c2) and consoante_final(c3))

# <silaba_5> ::= <par_consoantes><vogal>NS
def silaba_5(cad):
    c0 = cad[0]
    c1 = cad[1]
    c2 = cad[2]
    c3 = cad[3]
    c4 = cad[4]
    return par_consoantes(c0+c1) and vogal(c2) and c3+c4 == 'NS'

# <silaba_final> ::= <monossilabo_2> | <monossilabo_3> | <silaba_4> | <silaba_5>
def silaba_final(cad, dim):
    if dim == 2:
        return monossilabo_2(cad)
    elif dim == 3:
        return monossilabo_3(cad)
    elif dim == 4:
        return silaba_4(cad)
    elif dim == 5:
        return silaba_5(cad)
    else:
        return False

# <silaba>::= <vogal> | <silaba_2> | <silaba_3> | <silaba_4> |<silaba_5>
def silaba(cad, dim):
    if dim == 1:
        return vogal(cad)
    elif dim == 2:
        return silaba_2(cad)
    elif dim == 3:
        return silaba_3(cad)
    elif dim == 4:
        return silaba_4(cad)
    elif dim == 5:
        return silaba_5(cad)
    else:
        return False

# <palavra> ::= <monossilabo> | <silaba>*<silaba_final>
def palavra(cad):

    def dim_maiorque_5(dim):
        if dim>5:
            return 5
        else:
            return dim

    def palavra_silaba_final(cad, i):
        if i==1:
            return 0
        if silaba_final(cad, i):
            return i
        else:
            return palavra_silaba_final(cad[1:],i-1)

    def palavra_silaba(cad, i, dim):
        if i == 0:
            return False
        elif silaba(cad[dim-i:], i):
            if i == dim:
                return True
            dim -= i
            i = dim_maiorque_5(dim)
            return palavra_silaba(cad[:dim], i, dim)
        else:
            return palavra_silaba(cad, i-1, dim)

    # Verifica se a palavra e' um monossilabo
    dim = len(cad)
    if dim <= 3 and monossilabo(cad, dim):
        return True

    # procura e retira a silaba final da palavra
    i = dim_maiorque_5(dim)
    dim_final = palavra_silaba_final(cad[dim-i:], i)

    if dim_final == 0:
        return False
    elif dim_final == dim:
        return True

    # retira as silabas da palavra desde o fim
    dim -= dim_final
    i = dim_maiorque_5(dim)
    return palavra_silaba(cad[:dim], i, dim)

# e_silaba: cad. caracteres -> booleano
def e_silaba(cad):
    if not isinstance(cad, str):
        raise ValueError('e_silaba:argumento invalido')
    else:
        dim = len(cad)
        return silaba(cad, dim)

# e_monossilabo: cad. caracteres -> booleano
def e_monossilabo(cad):
    if not isinstance(cad, str):
        raise ValueError('e_monossilabo:argumento invalido')
    else:
        dim = len(cad)
        return monossilabo(cad, dim)

# e_palavra: cad. caracteres -> booleano
def e_palavra(cad):
    if not isinstance(cad, str):
        raise ValueError('e_palavra:argumento invalido')
    else:
        return palavra(cad)
