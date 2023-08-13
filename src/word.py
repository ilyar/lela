import spacy
import re
from spellchecker import SpellChecker


def collect_unique_english_words(file_path):
    nlp = spacy.load("en_core_web_sm")
    spell = SpellChecker()
    unique_words = set()
    latex_command_pattern = re.compile(r'\\[a-zA-Z]+|[^a-zA-Z\s]')
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line_without_commands = latex_command_pattern.sub('', line)
            doc = nlp(line_without_commands)
            for token in doc:
                if token.is_alpha and len(token.lemma_) > 2:
                    lemma = token.lemma_.lower()
                    if not spell.unknown([lemma]):
                        unique_words.add(lemma)

    return list(unique_words)
