from ast import literal_eval

cards = []
with open("Model/Cards.txt", "r") as file:
    try:
        lista = literal_eval(file.read())
    except:
        raise Exception("Erro no banco de dados. Não foi possível converter numero.")
    file.close()
cards = lista

class cardcontrol:
    def add_card(self, card, locale):
        cards.append({"number": card.getnumber(),
                       "cvv": card.getccv(),
                       "date": card.getdate(),
                       "funds": card.getfunds()
                       })
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        lista.append({"number": card.getnumber(),
                      "cvv": card.getccv(),
                      "date": card.getdate(),
                      "funds": card.getfunds()
                      })
        with open(locale, "w") as file:
            file.write(str(lista))
            file.close()

    def getcards(self):
        return cards

    def get_by_number(self, number):
        for i in range(len(cards)):
            if cards[i]["number"] == str(number):
                return cards[i]
                break
        else:
            return []

    def update(self, number, funds, locale):
        for i in range(len(cards)):
            if cards[i]["number"] == number:
                cards[i]["funds"] = funds
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        for i in range(len(lista)):
            if lista[i]["number"] == number:
                lista[i]["funds"] = funds
        file = open(locale, "w")
        file.write(str(lista))
        file.close()

    def delete(self, number, locale):
        for i in range(len(cards)):
            if cards[i]["number"] == number:
                cards.pop(i)
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
            file.close()
        for i in range(len(lista)):
            if lista[i]["number"] == number:
                lista.pop(i)
        with open(locale, "w") as file:
            file.write(str(lista))
            file.close()