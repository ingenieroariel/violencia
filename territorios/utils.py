
"""
Generates tuple
"""
def gen_rangos_cantidad():
    tupla = '('
    i = 0
    for c in range(5, 305, 5):
        tupla = tupla + "('%i-%i', '%i-%i')," % (i, c, i, c)
        i = c + 1
    tupla = tupla + ')'
    return eval(tupla)
