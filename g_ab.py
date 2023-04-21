# Analizador de cadenas de la forma a^n b^n

# Se importan las funciones necesarias para generar los analizadores
import ply.lex as lex
import ply.yacc as yacc

# Se definen los tokens
tokens = ['A', 'B']

# Se le asigna a cada token una expresión y se registra su número de ocurrencias
def t_A(token):
    r'a'
    token.lexer.tokens['A'] += 1
    return token

def t_B(token):
    r'b'
    token.lexer.tokens['B'] += 1
    return token

# Se define la función para identificar errores lexicográficos
def t_error(token):
    print(f"Carácter no válido '{token.value[0]}'")
    token.lexer.skip(1)

# Se definen las reglas de la gramática
def p_ab(p):
    """
    ab : A ab B
        | A B
    """

# Se define la función para identificar errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")

# Se cronstruyen los analizadores
lexer = lex.lex()
lexer.tokens = {'A': 0, 'B': 0}
parser = yacc.yacc()

# Se define la función que evaluará la cadena
def evaluar(cadena):
    lexer.tokens = {'A': 0, 'B': 0}
    resultado = parser.parse(cadena, lexer=lexer)
    if lexer.tokens['A'] == lexer.tokens['B']:
        print(f"Es válida")
    else:
        print(f"No es válida")

# Se ingresa la expresión a analizar
print ("|--------------------------------------------------------------|")
print ("|              Acepta cadenas de la forma a^n b^n              |")
print ("|--------------------------------------------------------------|")
Flag=True
while(Flag):
    cadena= input("Ingrese la cadena que desea analizar -> ")
    evaluar(cadena)
    next= input("¿Desea evaluar otra cadena? (S/N) -> ")
    if next in ('N', 'n'):
        Flag=False