
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/buscarcep", methods=["POST"])
def buscarcep():

    cep = request.form.get("cep")

    # Consulta a API do ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url, timeout=10)

    if resposta.status_code == 200:

        dados = resposta.json()

        if "erro" in dados:
            mensagem = "CEP não encontrado!"
            return render_template(
                "index.html",
                mensagem=mensagem,
                cep=cep
            )

        return render_template(
            "index.html",
            endereco=dados,
            cep=cep
        )

    mensagem = "Erro ao consultar o serviço ViaCEP."

    return render_template(
        "index.html",
        mensagem=mensagem,
        cep=cep
    )


if __name__ == "__main__":
    app.run(debug=True)
