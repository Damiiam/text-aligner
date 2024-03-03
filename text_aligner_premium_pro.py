def text_aligner(txt: str, n: int, symbol: str = ' ') -> list[str]:
    cls: list[str] = lambda t: [c for c in t.split(' ') if c] # Quita espacios duplicados entre palabras
    
    lines = cls(txt)
    n = max(max(map(len, lines)), n) # n no sera mas chico que la longitud de la palabra mas larga
    txt = str.join(' ', lines)
    
    i: int = 0; txt_len: int = len(txt) - 1; res: list = []
    
    if not txt_len: res.append(txt)

    while txt_len and i < txt_len:
        chunk: str = txt[i:i + n]
        
        do_extract: bool = (i + n + 1) < txt_len and not any(map(str.isspace, txt[i + n - 1:][:2]))
        to_extract: int = len(chunk.split(' ')[-1])
        words = cls(chunk[:-to_extract] if do_extract else chunk)
        
        l, s = sum(map(len, words)), len(words) - 1
        if s:
            d, r = int((n - l) / s), ((n - l) % s)
            spcs = [d + 1 if i < r else d for i in range(s)] # Cantidad de simbolos por espacio
            words = [w.ljust(len(w) + spcs[i], symbol) for i, w in enumerate(words[:-1])] + [words[-1]]
        
        res.append(str.join('', words))

        i += (n - to_extract) if do_extract else n
    
    return res


if __name__ == '__main__':
    
    txt = '  La    historia de la ópera tiene una duración      relativamente corta dentro del contexto de la historia de la música en     general apareció en 1597, fecha en que se creó la primera ópera.    '
    # txt = 'La      historia       de la ópera tiene una duración         relativamente corta  '
    chars = 6
    symbol = '.' # Simbolo para agregar entre cada palabra

    list(map(print, text_aligner(txt, chars, symbol)))