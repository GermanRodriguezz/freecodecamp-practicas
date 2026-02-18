def caesar(text,shift,encrypt=True):
    if not isinstance(shift, int):
        if shift < 1 or shift > 25:
            return 'Shift must be an integer value'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # cifrado César . Esta es una de las técnicas más sencillas para cifrar texto y
    #  consiste en sustituir cada letra del texto plano por la letra que se encuentra
    #  en un número fijo de posiciones en el alfabeto. Por ejemplo, con un 
    # desplazamiento de 5, ase reemplazaría por f, b por , g y así sucesivamente.

    # puede extraer parte de una cadena mediante el corte de cadenas:
    # fcc = 'freeCodeCamp'
    # print(fcc[8:]) esto imprime la cadena fcc apartir de la 8va posicion
    # muestra en pantalla 'Camp'

#aca lo que hacemos es ver si hay que descifrar o cifrar
# si encrypt es true no hace nada, encripta de manera normal con el slicing
# si encrypt es false entonces descifra la cadena modificando a shift de manera que la cadena quede normal
    if not encrypt :
        shift = -shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    alphabet += alphabet.upper()
    shifted_alphabet += shifted_alphabet.upper()

    translation_table = str.maketrans(alphabet,shifted_alphabet)
    print(translation_table)
    #El translate()método toma como argumento la tabla de traducción generada por str.maketrans(). 
    # Se invoca en una cadena y devuelve una copia de la cadena original, 
    # donde los caracteres se han reemplazado según la tabla de traducción:
    #t = str.maketrans('lk', 'br')
    #sentence = 'The tent gave in to the leaks.'
    #print(sentence.translate(t))
    # Output: The tent gave in to the bears.
    # reemplazo las LK por BR por eso al imprimir se imprime BEARS
    return text.translate(translation_table)

def encrypt(text,shift):
    return caesar(text,shift)

def decrypt(text,shift):
    return caesar(text,shift,False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text,13)
print(decrypted_text)