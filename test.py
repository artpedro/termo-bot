class Termo():
    
    def __init__(self,path_palavras=str):
        #Construtor que recebe o caminho para o arquivo txt com as palavras e adiciona todas elas
        #ao atributo words em formato de lista
        self.words = []
        with open(path_palavras,'r') as text:
            for i in text:
                self.words.append(i[:-1])
    
    def filter(self,size=int):
        #Filtra self.words para abarcar somente palavras de tamanho size

        self.size = size
        self.words = [i for i in self.words if len(i)==size and self.words]
        

    def makeDic(self,index=int):
        #Devolve um dicionário com a chave sendo uma letra e o valor sendo a quantidade
        #de vezes que ela parece na posição index das palavras em self.words

        dic = {}
        indic = {}
        for j in self.words:
            if j[index] not in dic:
                dic[j[index]] = 1
            else:
                dic[j[index]] = dic[j[index]]+1
        return dic
    
    def findBestLetter(self,index=int):
        #Devolve uma lista com todas as letras presentes na posição index das palavras em ordem de maior
        #frequência para menor frequência

        score = self.makeDic(index)
        #score ta vindo com palavras de mesma freq, contoranr isso
        tscore = []
        iscore = {}
        for i,j in score.items():
            #iscore = inverted score word
            iscore[j] = i
        #print(score,score.values())
        for i in sorted(score.values(),reverse= True):
            #print (i)
            #tscore = lista com as letras em ordem de frequencia
            #ordena os valores da score decrescente, caminha por eles adicionando
            if iscore[i] not in tscore:
                tscore.append(iscore[i])
            
        #print('\niscore'+ str(iscore))
        #print('\ntscore' + str(tscore))
        return tscore
    
    def scoreTable(self):
        #Retorna um dicionário contendo a posição na palavra como chave e
        #uma lista das letra e suas pontuação como valor
         
        self.dicScoreTable = {}
        for i in range(self.size):
            self.dicScoreTable[i] = self.findBestLetter(i)    
        #print(self.dicScoreTable)
        for i in self.dicScoreTable:
            score = 10
            for j in range(len(self.dicScoreTable[i])):
                self.dicScoreTable[i][j] = [self.dicScoreTable[i][j],score]
                if score != 0:
                    score -= 1            
                
        return self.dicScoreTable
    def assignScore(self):
        scoredWords = []
        for word in self.words:
            score = 0
            for letter in word:
                pass

test2 = Termo('Lista-de-Palavras.txt')
test2.filter(5)
print(test2.scoreTable())
print('oi')
