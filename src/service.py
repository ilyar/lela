import requests

class Lingualeo:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.session = requests.Session()

    def auth(self):
        url = "https://lingualeo.com/api/auth"
        values = {
            "type": "mixed",
            "credentials": {
                "email": self.email,
                "password": self.password
            }
        }
        extra_headers = {
            "Referer": "https://lingualeo.com/en/"
        }
        try:
            return self.get_content(url, values, extra_headers)
        except Exception as e:
            return e

    def add_word(self, word_set_id: int, word: str):
        word = word.lower()
        translate = self.get_translates(word)
        if translate["is_exist"] is not None:
            return "Already exists: {}".format(word)
        else:
            self.set_word(word_set_id, translate)
            return "Add word: {}".format(word)

    def set_word(self, word_set_id: int, translate):
        url = "https://api.lingualeo.com/SetWords"
        values = {
            "apiVersion": "1.0.1",
            "op": "actionWithWords {action: add}",
            "data": [
                {
                    "action": "add",
                    "mode": "0",
                    "wordIds": [translate["word_id"]],
                    "valueList": {
                        "wordSetId": word_set_id,
                        "wordValue": translate["word"],
                        "translation": {
                            "id": translate["translate_id"],
                            "tr": translate["translate_value"],
                            "main": 1,
                            "selected": 1
                        }
                    }
                }
            ],
            "userData": {"nativeLanguage": "lang_id_src"},
            "iDs": [{}]
        }
        try:
            return self.get_content(url, values)
        except Exception as e:
            return str(e)

    def get_translates(self, word):
        word = word.lower()
        url = "https://api.lingualeo.com/getTranslates"
        try:
            result = self.get_content(url, {"apiVersion": "1.0.1", "text": word, "iDs": [{}]})
            translate = result["translate"][0]
            return {
                "word_id": result["word_id"],
                "is_exist": translate["is_user"],
                "word": word,
                "translate_id": translate["id"],
                "translate_value": translate["translate_value"],
            }
        except Exception as e:
            return str(e)

    def get_content(self, url, values, extra_headers=None):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Origin": "https://lingualeo.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        if extra_headers:
            headers.update(extra_headers)
        response = self.session.post(url, json=values, headers=headers)
        return response.json()
