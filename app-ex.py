from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    prod = [
        ['Refrigerante', 4.50],
        ['Pizza', 2.50],
        ['Suco', 24.90],
        ['Salgado', 5.50],
        ['Lanche', 18.50]
    ]

    return render_template(
        'index-ex.html',
        ttitulo = 'Produtos',
        prod = prod
    )

if __name__ == "__main__":
    app.run()