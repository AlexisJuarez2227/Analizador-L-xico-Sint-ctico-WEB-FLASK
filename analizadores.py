from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def lexical_analysis(code):
    result = []
    keywords = {'int', 'for', 'if', 'else', 'while', 'return', 'system.out.println'}  # Puedes agregar más palabras reservadas aquí
    lines = code.split('\n')
    for line_number, line in enumerate(lines, start=1):
        index = 0
        while index < len(line):
            token_detected = False
            for keyword in keywords:
                if line[index:].startswith(keyword) and (index + len(keyword) == len(line) or not line[index + len(keyword)].isalnum()):
                    result.append((line_number, index, 'Palabra reservada', keyword))
                    index += len(keyword)
                    token_detected = True
                    break
            if token_detected:
                continue

            char = line[index]
            if char in [';', '{', '}', '(', ')']:
                tipo = 'Punto y coma' if char == ';' else 'Llave' if char in ['{', '}'] else 'Paréntesis'
                result.append((line_number, index, tipo, char))
                index += 1
            elif char.isdigit():
                result.append((line_number, index, 'Número', char))
                index += 1
            else:
                index += 1
    return result

def syntactic_analysis(code):
    result = []
    correct_keyword = 'system.out.println'
    keywords = {'for', 'if', 'else', 'while', 'return'}  # Puedes agregar más palabras reservadas aquí
    lines = code.split('\n')
    for line_number, line in enumerate(lines, start=1):
        stripped_line = line.strip()
        if stripped_line.startswith('system.out.'):
            if stripped_line.startswith(correct_keyword):
                result.append((line_number, correct_keyword, True))
            else:
                result.append((line_number, stripped_line.split('(')[0], False))
        elif 'system' in stripped_line or '.out' in stripped_line:
            result.append((line_number, stripped_line.split('(')[0], False))
        else:
            tokens = stripped_line.split()
            for token in tokens:
                if token in keywords:
                    result.append((line_number, token.capitalize(), True))
                elif any(keyword in token for keyword in keywords):
                    result.append((line_number, token.capitalize(), False))
                    break
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    code = ""
    lexical_result = []
    syntactic_result = []
    if request.method == 'POST':
        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            with open(file_path, 'r') as f:
                code = f.read()
        elif 'code' in request.form and request.form['code'].strip() != '':
            code = request.form['code']
        else:
            return "No file selected or code provided"
        
        lexical_result = lexical_analysis(code)
        syntactic_result = syntactic_analysis(code)
        
    return render_template_string("""
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
                border-radius: 5px.
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Analizador Léxico y Sintáctico</h1>
            <form method="POST" enctype="multipart/form-data">
                <label for="file">Subir Archivo:</label>
                <input type="file" name="file"><br><br>
                <label for="code">O ingresa el código aquí:</label><br>
                <textarea name="code" placeholder="Ingresa tu código aquí...">{{ code }}</textarea><br>
                <button type="submit">Analizar</button>
            </form>

            <div class="result">
                <h2>Análisis Léxico</h2>
                <div>
                    {% if lexical_result %}
                        <pre>{{ lexical_result | join('\\n') }}</pre>
                    {% endif %}
                </div>
            </div>

            <div class="result">
                <h2>Análisis Sintáctico</h2>
                <div>
                    {% if syntactic_result %}
                        <pre>{{ syntactic_result | join('\\n') }}</pre>
                    {% endif %}
                </div>
            </div>
        </div>
    </body>
    </html>
    """, code=code, lexical_result=lexical_result, syntactic_result=syntactic_result)

if __name__ == '__main__':
    app.run(debug=True)
