from flask import Flask, request, render_template_string
import ply.lex as lex
import ply.yacc as yacc

app = Flask(__name__)

# Analizador Léxico
# Lista de tokens
reservada = (
    'INCLUDE', 'USING', 'NAMESPACE', 'STD', 'COUT', 'CIN', 'GET', 'CADENA',
    'RETURN', 'VOID', 'INT', 'ENDL',
)
tokens = reservada + (
    'IDENTIFICADOR', 'ENTERO', 'ASIGNAR', 'SUMA', 'RESTA', 'MULT', 'DIV', 'POTENCIA', 'MODULO',
    'MINUSMINUS', 'PLUSPLUS', 'SI', 'SINO', 'MIENTRAS', 'PARA',
    'AND', 'OR', 'NOT', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL', 'IGUAL', 'DISTINTO',
    'NUMERAL', 'PARIZQ', 'PARDER', 'CORIZQ', 'CORDER', 'LLAIZQ', 'LLADER',
    'PUNTOCOMA', 'COMA', 'COMDOB', 'MAYORDER', 'MAYORIZQ',
)

# Reglas de Expresiones Regulares para token de Contexto simple
t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'%'
t_POTENCIA = r'(\*{2}|\^)'
t_ASIGNAR = r'='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = r';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_COMDOB = r'\"'

def t_INCLUDE(t):
    r'include'
    return t

def t_USING(t):
    r'using'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_STD(t):
    r'std'
    return t

def t_COUT(t):
    r'cout'
    return t

def t_CIN(t):
    r'cin'
    return t

def t_GET(t):
    r'get'
    return t

def t_ENDL(t):
    r'endl'
    return t

def t_SINO(t):
    r'else'
    return t

def t_SI(t):
    r'if'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_VOID(t):
    r'void'
    return t

def t_MIENTRAS(t):
    r'while'
    return t

def t_PARA(t):
    r'for'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_MAYORDER(t):
    r'<<'
    return t

def t_MAYORIZQ(t):
    r'>>'
    return t

def t_DISTINTO(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una linea")

t_ignore = ' \t'

def t_error(t):
    estado = f"** Token no valido en la Linea {t.lineno:4} Valor {t.value:16} Posicion {t.lexpos:4}"
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba_lexico(data):
    global resultado_lexema
    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema = []
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = f"Linea {tok.lineno:4} Tipo {tok.type:16} Valor {tok.value:16} Posicion {tok.lexpos:4}"
        resultado_lexema.append(estado)
    return resultado_lexema

# Analizador Sintáctico
resultado_gramatica = []

precedence = (
    ('right', 'ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)

nombres = {}

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMA'
    nombres[t[1]] = t[3]

def p_declaracion_expr(t):
    'declaracion : expresion'
    t[0] = t[1]

def p_expresion_operaciones(t):
    '''expresion : expresion SUMA expresion
                 | expresion RESTA expresion
                 | expresion MULT expresion
                 | expresion DIV expresion
                 | expresion POTENCIA expresion
                 | expresion MODULO expresion'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        t[0] = t[1] ** t[3]

def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]

def p_expresion_grupo(t):
    '''expresion : PARIZQ expresion PARDER
                 | LLAIZQ expresion LLADER
                 | CORIZQ expresion CORDER'''
    t[0] = t[2]

def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = t[1]

def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0

def p_error(t):
    if t:
        resultado = f"Error sintáctico de tipo {t.type} en el valor {t.value}"
        print(resultado)
    else:
        resultado = "Error sintáctico"
        print(resultado)
    resultado_gramatica.append(resultado)

# Instanciamos el analizador sintáctico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item.strip():
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append("Estructura correcta")
            else:
                resultado_gramatica.append("Error sintáctico en la estructura")
        else:
            resultado_gramatica.append("Línea vacía")

    print("Resultado: ", resultado_gramatica)
    return resultado_gramatica

# Plantilla HTML
html_template = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Analizador Léxico y Sintáctico</title>
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #2c3e50;
            color: #ecf0f1;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #34495e;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            max-width: 900px;
            width: 100%;
        }
        h1 {
            color: #1abc9c;
            text-align: center;
            margin-bottom: 20px;
            font-size: 2.5em;
        }
        textarea {
            width: 100%;
            height: 200px;
            padding: 15px;
            border: none;
            border-radius: 5px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 16px;
            resize: vertical;
            margin-bottom: 15px;
            background-color: #ecf0f1;
            color: #2c3e50;
        }
        button {
            display: block;
            width: 100%;
            padding: 15px;
            background-color: #1abc9c;
            color: #fff;
            border: none;
            border-radius: 5px;
            font-size: 18px;
            cursor: pointer;
            margin-top: 10px;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #16a085;
        }
        .result {
            margin-top: 30px;
        }
        .result h2 {
            color: #1abc9c;
            border-bottom: 2px solid #16a085;
            padding-bottom: 5px;
            font-size: 1.5em;
        }
        .result div {
            background-color: #2c3e50;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 15px;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
        }
        .result pre {
            white-space: pre-wrap;
            word-wrap: break-word;
            margin: 0;
            background-color: #ecf0f1;
            color: #2c3e50;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Analizador Léxico y Sintáctico</h1>
        <form action="/analizar" method="post">
            <textarea name="codigo" placeholder="Ingresa tu código aquí...">{{ codigo }}</textarea>
            <button type="submit">Analizar</button>
        </form>

        <div class="result">
            <h2>Análisis Léxico</h2>
            <div>
                {% if resultado_lexico %}
                    <pre>{{ resultado_lexico | join('\\n') }}</pre>
                {% endif %}
            </div>
        </div>

        <div class="result">
            <h2>Análisis Sintáctico</h2>
            <div>
                {% if resultado_sintactico %}
                    <pre>{{ resultado_sintactico | join('\\n') }}</pre>
                {% endif %}
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/analizar', methods=['POST'])
def analizar():
    codigo = request.form['codigo']
    resultado_lexico = prueba_lexico(codigo)
    resultado_sintactico = prueba_sintactica(codigo)
    return render_template_string(html_template, codigo=codigo, resultado_lexico=resultado_lexico, resultado_sintactico=resultado_sintactico)

if __name__ == '__main__':
    app.run(debug=True)
