class tabela_hash:
    def __init__(self, n):
        self.n = n
        self.tabela_hash = [None] * 10 # Criando o vetor do primeiro nivel com tamanho 10

        for i in range(10):
            self.tabela_hash[i] = [[] for _ in (n//10)] 
            #Dentro do vetor de primeiro nivel criamos um vetor de segundo nivel com tamanho n/10 em cada posicao
            # Cada espaço dos vetores de segundo nivel são listas vazias
            
    def hash1(self, chave):
        return hash(chave) % self.n # Definindo função hash do primeiro nivel, usamos a funcao hash() de python para facilitar

    
    def hash2(self, chave):
        return hash(chave) % (self.n//10) # Definindo a função hash do segundo nivel
    
    def inserir(self, chave, valor):
        self.tabela_hash[self.hash1(chave)][self.hash2(chave)].append((chave, valor))
        # Adicionando o novo elemento na posicao adequada do vetor de segundo nivel adequado

    def buscar(self, chave):
        for c,v in self.tabela_hash[self.hash1(chave)][self.hash2(chave)]: # Buscando no vetor adequado
            if c == chave: # Compara chave dos elementos do vetor com a chave do elemento sendo buscado para casos de colisão
                return v
        return None