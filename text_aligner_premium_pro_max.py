def align(txt:str, n:int, symbol:str = ' ') -> list[str]:
    cls: list[str] = lambda t: [c for c in t.split(' ') if c] # Quita espacios duplicados entre palabras
    
    lines = cls(txt)
    n = max(max(map(len, lines)), n) # n no sera mas chico que la longitud de la palabra mas larga
    
    return chunker(str.join(' ', lines), n, symbol).splitlines()

def fill(t:str, a:int, b:int, symbol:str = ' ', i:int = 0):
    w, _, z = t.partition(' ')
    
    return t if w == t else w.ljust(len(w) + a + (0 | ((i < b) and 1)), symbol) + fill(z, a, b, symbol, i + 1)

def chunker(t:str, n:int, symbol:str = ' ', i = 0) -> str:
    if len(t) <= n: cut, txt = 0, t
    else:
        cut = 0 | (not any(map(str.isspace, t[n - 1:n + 1])) and len(t[:n].split(' ')[-1]))
        txt = t[:n-cut].strip()
    
    a, b, s = 0, 0, len(txt.split(' ')) - 1
    if s: a, b = int((n - (len(txt) - s)) / s), (n - (len(txt) - s)) % s
    
    return f'{fill(txt, a, b, symbol)}\n' + (chunker(t[n-cut:].strip(), n, symbol, i + n) if t != txt else '')

if __name__ == '__main__':
    
    txt = '  La    historia de la ópera tiene una duración      relativamente corta dentro del contexto de la historia de la música en     general apareció en 1597, fecha en que se creó la primera ópera.    '
    # txt = 'La      historia       de la ópera tiene una duración         relativamente corta  '
    chars = 19
    symbol = ' ' # Simbolo a agregar entre palabras

    list(map(print, align(txt, chars, symbol)))