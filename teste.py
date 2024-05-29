import os, time
os.system("cls")
# [ ] = LISTA, ( ) = TUPLA, { } = DICIONÁRIOS

telefones = {
            ("Carlos", "54 99999999"), 
            ("Pedro", "54 999999888"), 
            ("Maria", "54 9898989899")
    
}
pesquisa = input("Informe o nome a ser pesquisado: ")
print(telefone.get(pesquisa, "Registrado não encontrado!"))

pesquisa = input("Informe o nome a ser deletado: ")
print( telefones.pop(pesquisa, "Registro não encontrado!"))

print(telefones)
try: 
    print(telefones[pesquisa])
except:
    print("Registro Não encontrado!")

#print(telefone.get(pesquisa, "Registrado não encontrado!"))