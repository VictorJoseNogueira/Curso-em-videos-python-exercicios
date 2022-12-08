def notas(* n, sit=False):
    '''
    --> função para verificar notas de alunos
    :param nota: uma ou mais notas dos alunos(aceita varias)
    :param sit: valor opcional mostra a situação do aluno
    :return: dicionario  '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/ len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'razoavel'
        else:
            r['situação'] = 'ruim'
    return  r

resp = notas(2, 5, 3, 7, 8, 1, 3, 0, 6, 8, 9, 10, sit=True)
print(resp)
help(notas)