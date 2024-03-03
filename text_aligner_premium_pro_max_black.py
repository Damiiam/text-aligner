def align(txt:str, n:int, symbol:str = ' ') -> list[str]:
    cls: list[str] = lambda t: [*filter(lambda c: len(c) and c != '\t', t.split(' '))] # quita espacios duplicados y \t entre palabras
    
    lines: list[str] = cls(txt)
    n = max(max(map(len, lines)), n) # n no sera mas chico que la longitud de la palabra mas larga
    
    return chunker(str.join(' ', lines), n, symbol).splitlines()

def fill(t:str, m:int, u:int, symbol:str = ' ', i:int = 0):
    w, _, z = t.partition(' ')
    
    return t if w == t else w.ljust(len(w) + m + (0 | ((i < u) and 1)), symbol) + fill(z, m, u, symbol, i + 1)

def chunker(t:str, n:int, symbol:str = ' ', i:int = 0, sl:int = 0) -> str:
    sl = (0 < t.find('\n') < n and t.find('\n')) or n # maneja los saltos de linea
    
    if len(t) <= sl: cut, txt = 0, t
    else: cut = 0 | (not any(map(str.isspace, t[sl - 1:sl + 1])) and len(t[:sl].split(' ')[-1])); txt = t[:sl-cut].strip()
    
    # s: cant. de espacios - a: cant. de simbolos por linea - m: cant. minima de simbolos por espacio - u: umbral
    s = len(txt.split(' ')) - 1; a = n - (len(txt) - s); m = 0 | (s and a // s); u = 0 | (s and a % s)
    
    return f'{fill(txt, m, u, symbol)}\n' + (chunker(t[sl-cut:].strip(), n, symbol, i + n, sl) if t != txt else '')

if __name__ == '__main__':
    
    txt = '''  La    historia de la ópera tiene una duración      relativamente corta dentro del contexto de 
    la historia de la  música en  \t   general apareció en 1597, fecha en que se creó la primera ópera.    '''
    # txt = 'La      historia       de la ópera tiene una duración         relativamente corta  '
    chars = 15
    symbol = '.' # Simbolo a agregar entre palabras

    list(map(print, align(txt, chars, symbol)))