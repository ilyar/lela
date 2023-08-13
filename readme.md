<div align="center">
  <h1><code>lela</code></h1>
  <p>
    <strong>Learn the language</strong>
  </p>
</div>

Feature:

- Extract words from text
- Load words to Lingualeo

## Usage

### Setup

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

```dotenv
EMAIL="...."
PASSWORD="...."
```

### Run

```bash
python src/lela.py <path/to/file.txt> <number_of_wordset_by_lingualeo> 
```
