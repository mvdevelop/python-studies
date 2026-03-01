
# 4️⃣ App Web ultra rápido com Flask

from flask import Flask, render_template_string, request

app = Flask(__name__)

template = """
<form method="post">
    Nome: <input name="nome">
    <button type="submit">Enviar</button>
</form>

{% if nome %}
    <h1>Olá {{ nome }}!</h1>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    nome = None
    if request.method == "POST":
        nome = request.form["nome"]
    return render_template_string(template, nome=nome)

app.run(debug=True)

# 🔥 Interface web funcional em minutos.
