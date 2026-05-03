clientes = ["João", "Maria", "Pedro", "Ana"]

for cliente in clientes:
   print(cliente)



# André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.
contador = 0

while contador <= 10:
   print("Processando dados...")
   contador += 1



# Marcos está desenvolvendo um programa para exibir uma mensagem de boas-vindas repetidamente no console, como parte de uma campanha de marketing de sua plataforma chamada Buscante. Ele quer garantir que a mensagem seja exibida 5 vezes.

# Ajude Marcos a escrever um programa que exiba a mensagem: "Bem-vindo ao Buscante!" o número exato de vezes que ele precisa.
contador = 1

while contador <=5:
   print("Bem-vindo ao Buscante!")
   contador += 1


for i in range(5):  # o range cria números automaticamente, é utilizado para sequência de números
   print("Bem-vindo ao Buscante!")



# Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.
numeros = [10, 20, 30, 40, 50]

soma = 0
for numero in numeros:  # Pega um valor da lista por vez (numero = 10 -> soma = 10, numero = 20 -> soma = 30, ... soma = 150)
    soma += numero

print(f"A soma total das receitas é: {soma}")



# Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos. Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".
projetos = ("website", "jogo", "análise de dados", None, "aplicativo móvel")

for projeto in projetos:  # Vai olhar um item por vez
   if projeto is None:    # is None é usado para verificar se o valor é vazio ou ausente
      print("Projeto ausente")
   else:
      print(projeto)



# Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrado. Após encontrar o livro, o programa deve parar imediatamente a busca, sem verificar os livros restantes.
livros = ["1994", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
   if livro == "O Hobbit":
      print("Livro encontrado: O Hobbit")
      break  # O break é usado para sair do loop imediatamente após encontrar o livro



# Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".
estoque = 5

while estoque > 0:
   estoque -= 1
   print(f"Venda realizada! Estoque restante: {estoque}")
print("Estoque esgotado :/")



# Crie um programa que utilize um laço for para exibir as seguintes mensagens:

# Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
# Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
# Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".
for segundos in range(10, 0, -1):  # range(início, fim, passo) - início = 10, fim = 0 (não incluído), passo = -1 (diminuindo)
   if segundos % 2 == 0:
      print(f"Faltam apenas {segundos} - Não perca essa oportunidade!")
   else:
      print(f"A contagem continua: {segundos} segundos restantes.")
print("Aproveite a promoção agora!")



# Crie um programa que ajude Ana a exibir somente os livros que possuem estoque disponível, no formato: "Livro disponível: ".
livros =  [
   {"titulo": "1984", "estoque": 5},
   {"titulo": "Dom Casmurro", "estoque": 0},
   {"titulo": "O Pequeno Príncipe", "estoque": 3},
   {"titulo": "O Hobbit", "estoque": 0},
   {"titulo": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
   if livro["estoque"] > 0:  # Pega o número de estoque do livro e verifica se é maior que 0
      print(f"Livro disponível: {livro['titulo']}")  # Pega o título 



# João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

# O nome de usuário deve ter pelo menos 5 caracteres.
# A senha deve ter pelo menos 8 caracteres.
# João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

# Crie um programa que implemente essa lógica usando um laço while.
while True:  # Sempre verdadeiro, nunca para sozinho
   nome_usuario = input("Digite seu nome de usuário: ")
   senha = input("Digite sua senha: ")

   if len(nome_usuario) < 5:  # O len significa "length" (comprimento), é usado para contar o número de caracteres em uma string
      print("O nome de usuário deve ter pelo menos cinco caracteres.")
      continue

   if len(senha) < 8:
      print("A senha deve ter pelo menos oito caracteres.")
      continue
   
   print("Cadastro realizado com sucesso!")
   break
