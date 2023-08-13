venv:
	python3 -m venv venv
	. venv/bin/activate; if [ -f requirements.txt ]; \
then pip install -r requirements.txt; \
python -m spacy download en_core_web_sm; \
fi

freeze: venv
	. venv/bin/activate; pip freeze > requirements.txt

clean:
	rm -rf venv

src/%: venv
	. venv/bin/activate; python src/$*.py

lela: src/lela
