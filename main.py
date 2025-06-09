import requests
import time
import csv

REST_URL_SIMPLE = ""
REST_URL_COMPLEX = ""

def test_rest(endpoint, consulta_tipo, n=30):
    resultados = []
    for i in range(n):
        inicio = time.time()
        resposta = requests.get(endpoint)
        fim = time.time()
        tempo = (fim - inicio) * 1000
        tamanho = len(resposta.content)
        resultados.append({
            "api": "REST",
            "consulta_tipo": consulta_tipo,
            "tempo_ms": tempo,
            "tamanho_bytes": tamanho
        })
    return resultados


resultados = []
resultados += test_rest(REST_URL_SIMPLE, "simples")
resultados += test_rest(REST_URL_COMPLEX, "complexa")


with open("resultados_rest.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["api", "consulta_tipo", "tempo_ms", "tamanho_bytes"])
    writer.writeheader()
    writer.writerows(resultados)

print("Testes REST finalizados e resultados salvos em resultados_rest.csv")