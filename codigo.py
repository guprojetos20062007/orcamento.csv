import csv

def gerar_orcamento():
    print("=== ORÇAMENTO DE ALUGUEL - IMOBILIÁRIA R.M ===\n")

    tipo = input("Qual tipo de imóvel você quer? (apartamento / casa / estúdio): ").strip().lower()

    if tipo == "apartamento":
        aluguel = 700
        quartos = int(input("Quantos quartos? (1 ou 2): "))
        if quartos == 2:
            aluguel += 200

        garagem = input("Quer incluir garagem? (s/n): ").strip().lower()
        if garagem == "s":
            aluguel += 300

        criancas = input("Você tem crianças? (s/n): ").strip().lower()
        if criancas == "n":
            desconto = aluguel * 0.05
            aluguel -= desconto

    elif tipo == "casa":
        aluguel = 900
        quartos = int(input("Quantos quartos? (1 ou 2): "))
        if quartos == 2:
            aluguel += 250

        garagem = input("Quer incluir garagem? (s/n): ").strip().lower()
        if garagem == "s":
            aluguel += 300

    elif tipo == "estúdio" or tipo == "studio":
        aluguel = 1200
        vagas = int(input("Quantas vagas de estacionamento você quer? (2 vagas por R$250, +R$60 por vaga extra): "))
        if vagas >= 2:
            aluguel += 250
        if vagas > 2:
            extras = vagas - 2
            aluguel += extras * 60

    else:
        print("Tipo de imóvel inválido. Tente novamente.")
        return

    valor_contrato = 2000
    parcelas = int(input("Quer dividir o valor do contrato em quantas vezes? (1 a 5): "))
    if parcelas < 1 or parcelas > 5:
        parcelas = 5
    valor_parcela = valor_contrato / parcelas

    print("\n=== RESULTADO DO ORÇAMENTO ===")
    print(f"Imóvel: {tipo.capitalize()}")
    print(f"Valor do aluguel por mês: R$ {aluguel:.2f}")
    print(f"Valor total do contrato: R$ {valor_contrato:.2f}")
    print(f"Parcelado em {parcelas}x de R$ {valor_parcela:.2f}")

    with open("orcamento.csv", "w", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq)
        escritor.writerow(["Mês", "Valor do Aluguel"])
        for mes in range(1, 13):
            escritor.writerow([mes, f"R$ {aluguel:.2f}"])

    print("\nArquivo 'orcamento.csv' criado com as 12 parcelas do aluguel.")

if __name__ == "__main__":
    gerar_orcamento()
