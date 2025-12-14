from scraper import Scraper , Pessoa


def exibir(dados,usuario):
    print(f"\n{usuario.nome}, Veja o clima de sua regiao:_ {usuario.localidade}")
    print("\n📍 Cidade:", dados["name"])
    print("🌡 Temperatura:", dados["temperature"]["celsius"], "°C")
    data = dados["timestamp"].split("T")[0]
    print("🕒 Atualizado em:", data)
    print("🌬 Vento:", dados["wind"]["speed"]["kph"], "km/h")
    print("🧭 Direção do vento:", dados["wind"]["sector_enum"])


def main():
    
    nome = str(input("Digite seu primeiro nome: ")).strip().title()
    
    cidade = input("Digite sua cidade (ex: salvador, jequie): ").strip().lower()
    
    usuario = Pessoa(nome,cidade)
    
    scraper = Scraper(cidade)

    scraper.Requisicao()
    
    dados = scraper.dados_extraidos()
    
    exibir(dados,usuario)




main()

