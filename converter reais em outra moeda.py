print("Escolha a opção para converter reais em: ")
print("1. Dolar")
print("2. Euro")
print("3. Ienes")     

choice = input("Escolha uma opção (1, 2 ou 3): ")

dolar_base = 4.99
euro_base = 5.38
iene_base = 0.0033

while True:

  if choice == "1":
    reais = float(input("Quantos reais serão convertidos em doláres? "))
    conversao_dolar = round(reais / 4.99 , 2)  
    print("O valor {} convertido em doláres equivale a {}".format(reais, conversao_dolar))
  elif choice == "2":
    reais = float(input("Quantos reais serão convertidos em euros? "))
    conversao_euro = round(reais / 5.38 , 2)    
    print("O valor {} convertido em euros equivale a {}".format(reais, conversao_euro))
  elif choice == "3":
    reais = float(input("Quantos reais serão convertidos em ienes? "))
    conversao_ienes = round(reais / 0.0033 , 2)    
    print("O valor {} convertido em ienes equivale a {}".format(reais, conversao_ienes))
  else:
    print("Essa opção não existe, por favor escolha uma opção válida.")
    choice = input("Escolha uma opção (1, 2 ou 3): ")
