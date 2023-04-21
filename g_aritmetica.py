# Analizador expresiones aritméticas simples

# Se importan las funciones necesarias para generar los analizadores
import ply.yacc as yacc
from ply.lex import lex

# Se definen los tokens
tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'POTENCIA',
    'PARENTESIS_IZQUIERDO',
    'PARENTESIS_DERECHO',
)

# Se le asigna a cada token una expresión regular 
t_NUMERO = r'\d+'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_POTENCIA= r'\^'
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'

# Se define la función para identificar errores lexicográficos
def t_error(t):
    print(f"Caracter inválido '{t.value[0]}'")
    t.lexer.skip(1)

# Se definen las reglas de la gramática para la estructura de cada expresión 
def p_expression_SUMA(p):
    'expression : expression SUMA term'
    p[0] = p[1] + p[3]

def p_expression_RESTA(p):
    'expression : expression RESTA term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_MULTIPLICACION(p):
    'term : term MULTIPLICACION factor'
    p[0] = p[1] * p[3]

def p_term_DIVISION(p):
    'term : term DIVISION factor'
    p[0] = p[1] / p[3]

def p_term_POTENCIA(p):
    'term : term POTENCIA factor'
    p[0] = p[1] ** p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMERO'
    p[0] = int(p[1])

def p_factor_expr(p):
    'factor : PARENTESIS_IZQUIERDO expression PARENTESIS_DERECHO'
    p[0] = p[2]

# Se define la función para identificar errores sintácticos
def p_error(p):
    print(f"Error de sintaxis en '{p.value}'")
    
# Se cronstruyen los analizadores
lexer = lex()   
parser = yacc.yacc()

# Se ingresa la expresión a analizar
print ("|--------------------------------------------------------------------------------------|")
print ("| Evalúa expresiones aritméticas de enteros que contengan operadores (), +, -, *, /, ^ |")
print ("|--------------------------------------------------------------------------------------|")
Flag=True
while(Flag):
    cadena= input("Ingrese la expresión aritmética -> ")
    lexer.input(cadena)
    result = parser.parse()
    print(result)
    next= input("¿Desea evaluar otra expresión? (S/N) -> ")
    if next in ('N', 'n'):
        Flag=False

