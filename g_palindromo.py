# Analizador de expresiones palíndromas

# Se importan las funciones necesarias para generar los analizadores
import ply.lex as lex
import ply.yacc as yacc

# Se define el token 
tokens = ['CADENA']

# Se le asigna al token un expresión regular
t_CADENA= r'[a-zA-Z ]+'

# Se define la función para identificar errores lexicográficos
def t_error(token):
    print(f"Carácter no válido '{token.value[0]}'")
    token.lexer.skip(1)

# Se define la regla que debe cumplir la expresión para satisfacer la gramática
def p_palindromo(p):
    """
    palindromo : CADENA
               | CADENA palindromo
    """
    cadena = p[1].replace(' ', '')
    if cadena == cadena[::-1]:
        print(f"Es un palíndromo")
    else:
        print(f"No es un palíndromo")

# Se define la función para identificar errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis en entrada")

# Se cronstruyen los analizadores
lexer = lex.lex()
parser = yacc.yacc()

# Se define la función que evaluará la cadena
def evaluar(cadena):
    resultado = parser.parse(cadena, lexer=lexer)
    return resultado

# Se ingresa la expresión a analizar
print ("|------------------------------------------|")
print ("|      Acepta expresiones palíndromas      |")
print ("|------------------------------------------|")
Flag=True
while(Flag):
    cadena= input("Ingrese la cadena que desea analizar -> ")
    evaluar(cadena)
    next= input("¿Desea evaluar otra cadena? (S/N) -> ")
    if next in ('N', 'n'):
        Flag=False