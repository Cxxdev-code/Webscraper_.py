# 🌦️ Weather Scraper CLI (Brasil)

Projeto em **Python** que realiza **web scraping** para obter informações climáticas atuais de cidades brasileiras diretamente do site **climaeradar.com.br**, exibindo os dados via **terminal (CLI)**.

O objetivo do projeto é **estudo e prática de Web Scraping**, organização de código com **POO**, uso de **requests, BeautifulSoup, regex e JSON**, sem uso de API oficial, Flask ou Selenium.

---

## 📌 Funcionalidades

* 🔎 Busca automática do clima pela cidade informada
* 🌡 Temperatura atual em Celsius
* 🌬 Velocidade e direção do vento
* 🕒 Data da última atualização
* 🧱 Código organizado em classes (`Scraper` e `Pessoa`)
* 💻 Execução 100% pelo terminal

---

## 🛠️ Tecnologias utilizadas

* Python 3.10+
* requests
* beautifulsoup4
* regex (`re`)
* JSON
* Programação Orientada a Objetos (POO)

---

## 📂 Estrutura do projeto

```
Tempo/
│
├── app.py          # Arquivo principal (CLI)
├── scraper.py     # Classes Scraper e Pessoa
├── venv/           # Ambiente virtual
└── README.md
```

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/Cxxdev-code/Webscraper_.py.git
cd Webscraper_.py
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

3. Instale as dependências:

```bash
pip install requests beautifulsoup4
```

4. Execute o programa:

```bash
python app.py
```

---

## 🧪 Exemplo de saída

```
Caina, Veja o clima de sua região: salvador

📍 Cidade: Salvador
🌡 Temperatura: 28 °C
🕒 Atualizado em: 2025-12-14
🌬 Vento: 25 km/h
🧭 Direção do vento: East
```

---

## 🎯 Objetivo educacional

Este projeto foi desenvolvido com foco em:

* Aprender **Web Scraping na prática**
* Entender páginas com **dados dinâmicos embutidos em `<script>`**
* Extração de dados usando **Regex**
* Boas práticas de separação de responsabilidades

---
---

## 🚀 Próximos passos (ideias)

* [ ] Salvar dados em JSON
* [ ] Histórico de clima
* [ ] Interface gráfica (Tkinter)
* [ ] API com Flask/FastAPI
* [ ] Cache de requisições

---

## 👤 Autor

**Caina Henrique**
Desenvolvedor Back-End Júnior (Python)

---

⭐ Se este projeto te ajudou, deixe uma estrela!
