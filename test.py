def merge_dicts(*dict_args):
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key-value pairs in latter dictionaries.
    """
    result = {}
    for d in dict_args:
        for k in d:
            if k not in result:
                result[k] = d[k]
            else:
                result[k] += d[k]
                
class Termo():
    
    def __init__(self,path_palavras=str):
        #Construtor que recebe o caminho para o arquivo txt com as palavras e adiciona todas elas
        #ao atributo words em formato de lista
        self.untreatWords = []
        with open(path_palavras,'r') as text:
            for i in text:
                self.untreatWords.append(i[:-1])
    
    def filter(self,size=int):
        #Filtra self.words para abarcar somente palavras de tamanho size

        self.size = size
    
        for word in self.untreatWords:
            if '-' in word:
                self.untreatWords.remove(word)
          
        self.words = [i for i in self.untreatWords if ((len(i)==size))]
        self.words = list(set(self.words))
        
    def makeDic(self,index=int):
        #Devolve um dicionário com a chave sendo uma letra e o valor sendo a quantidade
        #de vezes que ela parece na posição index das palavras em self.words

        dic = {}
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
        self.scoreTable = {}
        for i in range(self.size):
            #montar dicScoreTable com todas as posições como chaves e letras em ordem crescente de freq como valores
            self.dicScoreTable[i] = self.findBestLetter(i)
        for i in self.dicScoreTable:
            self.scoreTable[i] = {}
            score = 20
            for j in self.dicScoreTable[i]:
                if j not in self.scoreTable[i]:
                    self.scoreTable[i][j] = score
                    if score != 0:
                        score -= 1
        return self.scoreTable
    
    def assignScore(self):
        self.scoredWords = {}
        for word in self.words:
                self.scoredWords[word] = 0
        for index in range(self.size):
            for word in self.words:
                score = 0
                if word[index] in self.scoreTable[index]:    
                    score = self.scoreTable[index][word[index]]
                self.scoredWords[word] += score
        return self.scoredWords
    
    def findBestWord(self):
        iscoredWords  = {}
        for i,j in self.scoredWords.items():
            #iscore = inverted score word
            iscoredWords[j] = i
        

         

test2 = Termo('Lista-de-Palavras.txt')
test2.filter(5)
freq0 = test2.makeDic(0)
freq1 = test2.makeDic(1)
freq2 = test2.makeDic(2)
freq3 = test2.makeDic(3)
freq4 = test2.makeDic(4)

def merge_dicts(*dict_args):
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key-value pairs in latter dictionaries.
    """
    result = {}
    for d in dict_args:
        for k in d:
            if k not in result:
                result[k] = d[k]
            else:
                result[k] += d[k]
        
    return result

print(merge_dicts(freq0,freq1,freq2,freq3,freq4))
