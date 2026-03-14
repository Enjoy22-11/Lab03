import time
import multiDictionary as md


class SpellChecker:

    def __init__(self):
        self.multi_dict = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        # 1. Pulizia iniziale comune a tutti i test
        testo_pulito = replaceChars(txtIn)
        words = testo_pulito.lower().split()

        # --- TEST 1: Using Contains (Python built-in) ---
        start_c = time.time()
        res_c = self.multi_dict.searchWord(words, language)
        end_c = time.time()
        self.print_results(res_c, "contains", end_c - start_c)

        # --- TEST 2: Using Linear Search ---
        start_l = time.time()
        res_l = self.multi_dict.searchWordLinear(words, language)
        end_l = time.time()
        self.print_results(res_l, "Linear search", end_l - start_l)

        # --- TEST 3: Using Dichotomic Search ---
        start_d = time.time()
        res_d = self.multi_dict.searchWordDichotomic(words, language)
        end_d = time.time()
        self.print_results(res_d, "Dichotomic search", end_d - start_d)

    # Metodo ausiliario per non ripetere i print 3 volte

    def print_results(self, results, method_name, elapsed_time):
        print(f"------------------------------")
        print(f"Using {method_name}")
        errate = 0
        for r in results:
            if not r.corretta:
                print(r)
                errate += 1
        print(f"Numero di errori: {errate}")
        print(f"Time elapsed: {elapsed_time}")
        print(f"------------------------------")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
