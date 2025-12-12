import requests

def get_currency_rate(base, target):
    url = f"https://api.frankfurter.app/latest?from={base}&to={target}"

    try:
        response = requests.get(url)
        data = response.json()

        if "rates" not in data:
            return {"error": "Falha ao obter taxa"}

        #pegar valor da moeda desejada
        rate = data["rates"].get(target)

        if rate is None:
            return {"error": "Moeda inválida"}

        return {"rate": rate}

    except Exception as e:
        return {"error": str(e)}
