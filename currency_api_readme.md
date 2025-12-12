# 📘 Documentação do Sistema de Conversão de Moedas

## 📌 Sobre o Projeto

Este sistema foi desenvolvido para **consultar taxas de câmbio em tempo
real**, salvar no banco de dados e permitir a visualização via interface
web ou API.

------------------------------------------------------------------------

## 🧩 Tecnologias Utilizadas

-   **Python 3**
-   **Django**
-   **Django REST Framework**
-   **Requests**
-   **SQLite ou PostgreSQL**
-   **HTML + CSS (Frontend)**

------------------------------------------------------------------------

## 📥 Instalação e Configuração

### 1️⃣ Clonar o repositório

    git clone seu_repositorio.git
    cd seu_repositorio

### 2️⃣ Criar e ativar o ambiente virtual

    python -m venv venv
    venv/Scripts/activate   # Windows
    source venv/bin/activate  # Linux/Mac

### 3️⃣ Instalar as dependências

    pip install -r requirements.txt

### 4️⃣ Aplicar migrações

    python manage.py migrate

### 5️⃣ Rodar o servidor

    python manage.py runserver

------------------------------------------------------------------------

## 🌍 URLs da Aplicação

### 🏠 **Home (Frontend)**

Interface para consultar taxas:

    http://127.0.0.1:8000/

------------------------------------------------------------------------

### 💾 **Salvar taxa consultada**

    http://127.0.0.1:8000/currency/fetch/?base=USD&target=EUR

Retorno esperado (JSON):

``` json
{
  "message": "Taxa salva com sucesso",
  "rate": 0.92,
  "id": 10
}
```

------------------------------------------------------------------------

### 📡 **API de taxas**

Busca dados no banco usando filtros GET:

    http://127.0.0.1:8000/api/rates/?base=USD&target=EUR

------------------------------------------------------------------------

## 🧠 Lógica da Aplicação

### 💼 Model: `CurrencyRate`

``` python
class CurrencyRate(models.Model):
    base_currency = models.CharField(max_length=10)
    target_currency = models.CharField(max_length=10)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
```

📌 **O que faz:** - Armazena cada conversão consultada. - Guarda moeda
base, moeda alvo, taxa e data da consulta.

------------------------------------------------------------------------

## 🔧 Services: `get_currency_rate`

``` python
def get_currency_rate(base, target):
    url = f"https://api.frankfurter.app/latest?from={base}&to={target}"
```

📌 **O que faz:** - Envia requisição à API Frankfurter. - Retorna
**rate**, ou mensagem de erro.

------------------------------------------------------------------------

## 🌐 View: `fetch_and_save_rate`

``` python
def fetch_and_save_rate(request):
```

📌 **O que faz:** - Recebe base e target via GET. - Chama o service. -
Salva no banco. - Retorna JSON para o frontend.

------------------------------------------------------------------------

## 🎨 Frontend

### `HomeView`

📌 Renderiza o formulário e envia POST para salvar taxa.

### `CurrencyListView`

📌 Lista as taxas salvas\
📌 **Paginação a cada 15 registros**

------------------------------------------------------------------------

## 📦 API (DRF)

### Serializer

``` python
class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = "__all__"
```

### View API

``` python
class RateListAPIView(generics.ListAPIView):
    serializer_class = CurrencyRateSerializer
```

📌 Permite filtrar:

    ?base=USD
    ?target=EUR

------------------------------------------------------------------------

## ✔️ Finalização

A aplicação está pronta para uso e expansão.
