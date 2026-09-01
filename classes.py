class lojagamer:
    #iniciando
    def __init__(self):
        self.loja_gamer=""
        self.nome=""
        self.comprar=""
        self.estoque={"Mouse":True , "Teclado":True ,"Monitor":True, "Cadeira":False}

    #saudacao
    def saudação(self):
        print(f"Olá {self.nome}, bem-vindo a nossa loja no qual se chama {self.loja_gamer}")
        self.comprar=str(input("Deseja comprar alguma coisa? Nosso estoque: Mouse,Teclado, Monitor, Cadeira."))
    
    #verifica estoque
    def verificando(self):
        if self.comprar in self.estoque:
            if self.estoque[self.comprar]==True:
                print(f"Aqui está o produto: {self.comprar}")
            else:
                print("Infelizmente não temos esse item :C ")


entrar_loja=str(input("Você avista uma loja em meio a neblina, entrar? \n -S \n -N \n"))


if entrar_loja==("-N"):
    print("Ok")
else:
    print("Que ótimo!")
    nome=str(input("Qual seu nome?"))
    loja=lojagamer()
    loja.loja_gamer="CHRONUS"
    loja.nome=nome
    loja.saudação()
    loja.verificando()