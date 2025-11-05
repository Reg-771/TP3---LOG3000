from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire. Il lie les opérateurs aux fonctions correspondantes.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Calcule le résultat d'une expression de calcul avec un seul opérateur.
    lève ValueError si l'expression est vide, mal formatée, ou si les opérandes ne sont pas des nombres.

    Arguments:
        str expr: chaîne de caractères représentant l'expression à calculer.

    Retour:
        float: Résultat du calcul de l'expression.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Supprime les espaces.
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Trouve la position de l'opérateur.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifie que l'opérateur a été trouvé et qu'il n'est pas au début ou à la fin.
    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]


    try:
        # Convertit les opérandes en float.
        a = float(left)
        b = float(right)
    except ValueError:
        #Les opérandes ne sont pas des nombres valides.
        raise ValueError("operands must be numbers")
    # Effectue le calcul en appelant la fonction appropriée.
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Page d'accueil de l'application.

    Gère les requêtes GET et POST. Pour les requêtes POST, elle récupère l'expression
    depuis le formulaire, calcule le résultat et l'affiche.

    Pour les requêtes GET, elle affiche simplement la page d'accueil.

    Retour:
        str: Page HTML rendue.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            #Affiche l'erreur si le calcul échoue.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Lance l'application Flask en mode debug.
    app.run(debug=True)