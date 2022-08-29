import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas.'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    total_sentencas = separa_sentencas(texto)

    '''Calcula caracteres em cada sentença.'''
    caracteres_sentenca = 0
    for i in range(len(total_sentencas)):
        caracteres_sentenca = caracteres_sentenca + len(total_sentencas[i])

    total_frases = []
    for i in range(len(total_sentencas)):
        frases = separa_frases(total_sentencas[i])
        total_frases.extend(frases)
        
    '''Calcula caracteres em cada frase'''
    caracteres_frases = 0
    for i in range(len(total_frases)):
        caracteres_frases = caracteres_frases + len(total_frases[i])

    total_palavras = []
    for i in range(len(total_frases)):
        palavras = separa_palavras(total_frases[i])
        total_palavras.extend(palavras)
        
    palavras_unicas = n_palavras_unicas(total_palavras)
    palavras_diferentes = n_palavras_diferentes(total_palavras)

    '''Calcula o tamanho médio de palavras.'''
    quantidade_caracteres = 0
    for i in range(len(total_palavras)):
        quantidade_caracteres = quantidade_caracteres + len(total_palavras[i])
        
    tamanho_medio_palavras = quantidade_caracteres / len(total_palavras)

    '''Relação Type-Token.'''
    type_token = palavras_diferentes / len(total_palavras)

    '''Relação Hapax Legomana.'''
    hapax_legomana = palavras_unicas / len(total_palavras)

    '''Tamanho médio de sentença.'''
    tamanho_sentenca = caracteres_sentenca / len(total_sentencas)

    '''Complexidade de sentença.'''
    complexidade_sentenca = len(total_frases) / len(total_sentencas)

    '''Tamanho médio de frase.'''
    tamanho_frase = caracteres_frases / len(total_frases)

    return [tamanho_medio_palavras, type_token, hapax_legomana, tamanho_sentenca, complexidade_sentenca, tamanho_frase]
    
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    somatorio = 0
    for i in range(len(as_a)):
        somatorio = somatorio + abs(as_a[i] - as_b[i])
        
    similaridade = (somatorio / 6)
    
    return similaridade

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_assinaturas = []
    for i in range(len(textos)):
        lista_assinaturas.append(calcula_assinatura(textos[i]))

    lista_similaridades = []
    for j in range(len(lista_assinaturas)):
        lista_similaridades.append(compara_assinatura(lista_assinaturas[j], ass_cp))

    similaridade = lista_similaridades[0]
    indice = 1
    for k in range(len(textos)):
        if lista_similaridades[k] < similaridade:
            similaridade = atual
            indice = k + 1
    
    return indice

def principal():
    assinatura_b = le_assinatura()
    lista_textos = le_textos()
    texto_infectado = avalia_textos(lista_textos, assinatura_b)

    print("O autor do texto ", texto_infectado," está infectado com COH-PIAH")
