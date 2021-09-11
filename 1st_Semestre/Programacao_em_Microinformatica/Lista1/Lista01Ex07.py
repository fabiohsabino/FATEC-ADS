'''
7.	Implemente um programa para ler o preço do litro do combustível
de um carro, ler o desempenho do veículo (km/l) e a distância entre
duas cidades (km), e informar quantos litros, e quanto
dinheiro vai ser gasto para fazer uma viagem entre as duas cidades.
'''
print("Programa para cálculo de despesas com combustível. Informe os"
      "dados necessários")
precoLitro = float(input("Preço do litro do combustível >> R$ "))
desempenho = float(input("Desempenho do veículo >> "))
distancia = float(input("Distância entre as cidades >> "))

litros = distancia / desempenho
gasto = litros * precoLitro

print(f"Serão necessários {litros:.1f} litros de combustível "
      f"e R$ {gasto:.2f}")