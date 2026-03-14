import dictionary as d
import richWord as rw



class MultiDictionary:

    def __init__(self):
       self.dictionary = d.Dictionary()

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        path= f"resources/{language.capitalize()}.txt"
        self.dictionary.loadDictionary(path)
        results=[]
        for w in words:
            rich_word = rw.RichWord(w)
            if w in self.dictionary.dict:
                rich_word.corretta = True
            else:
                rich_word.corretta=False
            results.append(rich_word)
        return results

    def searchWordLinear(self, words, language):
        path = f"resources/{language.capitalize()}.txt"
        self.dictionary.loadDictionary(path)
        results = []
        for w in words:
            rich_word = rw.RichWord(w)
            trovata = False
            # Scorre tutto il dizionario elemento per elemento [cite: 135]
            for word_dict in self.dictionary.dict:
                if word_dict == w:
                    trovata = True
                    break
            rich_word.corretta = trovata
            results.append(rich_word)
        return results

    def searchWordDichotomic(self, words, language):
        path = f"resources/{language.capitalize()}.txt"
        self.dictionary.loadDictionary(path)
        results = []
        dict_list = self.dictionary.dict  # La lista deve essere ordinata

        for w in words:
            rich_word = rw.RichWord(w)
            low = 0
            high = len(dict_list) - 1
            trovata = False

            while low <= high:
                mid = (low + high) // 2  # Trova il punto centrale
                if dict_list[mid] == w:
                    trovata = True
                    break
                elif dict_list[mid] < w:
                    low = mid + 1  # Cerca nella metà successiva [cite: 142]
                else:
                    high = mid - 1  # Cerca nella metà precedente [cite: 141]

            rich_word.corretta = trovata
            results.append(rich_word)
        return results