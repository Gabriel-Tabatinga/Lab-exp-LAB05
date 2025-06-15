import requests
import time
import csv

GRAPHQL_URL = ""

QUERY_SIMPLES = """
query {
  usuario(id: 1) {
    nome
    email
  }
}
"""

QUERY_COMPLEXA = """
query {
  usuario(id: 1) {
    nome
    email
    posts {
      id
      titulo
      comentarios {
        id
        texto
      }
    }
  }
}
"""

def test_graphql(query, consulta_tipo, n=30):
    resultados = []
    headers = {"Content-Type": "application/json"}
    for i in range(n):
        inicio = time.time()
        resposta = requests.post(
            GRAPHQL_URL,
            json={"query": query},
            headers=headers
        )
        fim = time.time()
        tempo = (fim - inicio) * 1000
        tamanho = len(resposta.content)
        resultados.append({
            "api": "GraphQL",
            "consulta_tipo": consulta_tipo,
            "tempo_ms": tempo,
            "tamanho_bytes": tamanho
        })
    return resultados

resultados = []
resultados += test_graphql(QUERY_SIMPLES, "simples")
resultados += test_graphql(QUERY_COMPLEXA, "complexa")

with open("resultados_graphql.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["api", "consulta_tipo", "tempo_ms", "tamanho_bytes"])
    writer.writeheader()
    writer.writerows(resultados)

print("Testes GraphQL finalizados e resultados salvos em resultados_graphql.csv")