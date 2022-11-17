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
        
    def makeDic(self,index=None):
        #Devolve um dicionário com a chave sendo uma letra e o valor sendo a quantidade
        #de vezes que ela parece na posição index das palavras em self.words.
        #Se index for omitida, conta quantas vezes a letra aperece em todas as palavras
        if index != None:
            dic = {}
            for j in self.words:
                if j[index] in dic:
                    dic[j[index]] += 1
                else:
                    dic[j[index]] = 1
            return dic
        else:
            dic = {}
            for i in self.words:
                for j in i:
                    if j in dic:
                        dic[j] +=1
                    else:
                        dic[j] = 1
            return dic

        
    def findBestLetter(self,index=None):
        #Devolve uma lista com todas as letras presentes na posição index das palavras em ordem de maior
        #frequência para menor frequência.
        #Se o index for omitido, encontra as melhores letras em todas as posições
        if index != None:
            score = self.makeDic(index)
            
            tscore = []
            invertedScore = {}
            for i,j in score.items():
                invertedScore[j] = i

            for i in sorted(score.values(),reverse= True):
                if invertedScore[i] not in tscore:
                    tscore.append(invertedScore[i])
            return tscore
        else:
            score = self.makeDic()
            tscore = []
            invertedScore = {}
            for i,j in score.items():
                invertedScore[j] = i

            for i in sorted(score.values(),reverse= True):
                if invertedScore[i] not in tscore:
                    tscore.append(invertedScore[i])
            return tscore

    def generateIndexScoreTable(self):
        #Retorna um dicionário contendo a posição na palavra como chave e
        #uma lista das letra e suas pontuação como valor
         
        dicScoreTable = {}
        self.indexScoreTable = {}
        for i in range(self.size):
            #montar dicScoreTable com todas as posições como chaves e letras em ordem crescente de freq como valores
            dicScoreTable[i] = self.findBestLetter(i)
        for i in dicScoreTable:
            self.indexScoreTable[i] = {}
            score = 28
            for j in dicScoreTable[i]:
                if j not in self.indexScoreTable[i]:
                    self.indexScoreTable[i][j] = score
                    if score != 0:
                        score -= 1
        return self.indexScoreTable

    def generateGeneralScoreTable(self):
        
        self.generalScoreTable = {}
        scoreTable = self.findBestLetter()
        for i in scoreTable:
            score = 60
            for j in scoreTable:
                if j not in self.generalScoreTable:
                    self.generalScoreTable[j] = score
                    if score != 0:
                        score -= 1
        return self.generalScoreTable

    def assignScore(self):
        self.indexScoredWords = {}
        self.generalScoredWords = {}
        for word in self.words:
            self.indexScoredWords[word] = 0
            self.generalScoredWords[word] = 0
        for index in range(self.size):
            for word in self.words:
                score = 0
                if word[index] in self.indexScoreTable[index]:    
                    score = self.indexScoreTable[index][word[index]]
                self.indexScoredWords[word] += score

        for word in self.words:
            for letter in word:
                score = 0
                if letter in self.generalScoreTable:
                    score = self.generalScoreTable[letter]
                self.generalScoredWords[word] += score
        #self.scoredWords = merge_dicts(self.indexScoredWords,self.generalScoredWords)
        self.scoredWords = self.generalScoredWords
        
        return self.scoredWords
    
    def findBestFirstWord(self):
        
        iscoredWords  = {}
        tscoredWords = []
        for i,j in self.scoredWords.items():
            #iscore = inverted score word
            iscoredWords[j] = i
        for i in sorted(self.scoredWords.values(),reverse= True):
            if iscoredWords[i] not in tscoredWords:
                tscoredWords.append(iscoredWords[i])
        return tscoredWords    



         

test2 = Termo('Lista-de-Palavras.txt') #Inicializando o termo

test2.filter(5) #Filtrando somente as palavras de 5 letras

print('Melhores letras')
print(test2.findBestLetter()) #Encontrando as letras mais presentes

print('Pontuação das letras em cada posição')
print(test2.generateIndexScoreTable())

print('Pontuação das letras no geral')
print(test2.generateGeneralScoreTable())

print('Pontuação das palavras')
print(test2.assignScore())

print('Melhores palavras')
print(test2.findBestWord())










#print(merge_dicts(freq0,freq1,freq2,freq3,freq4))
