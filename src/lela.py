from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env
import os
import word
import service
import sys

if len(sys.argv) < 3:
    print("Usage: python lela.py <file_path> <word_set_id>")
    sys.exit(1)

file_path = sys.argv[1]
word_set_id = int(sys.argv[2])

lingualeo = service.Lingualeo(os.getenv('EMAIL'), os.getenv('PASSWORD'))
lingualeo.auth()
words = word.collect_unique_english_words(file_path)
for word in words:
    status = lingualeo.add_word(word_set_id, word)
    print(status)
