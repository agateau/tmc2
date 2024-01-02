all: venv compile_trans

clean:
	-rm -rf venv

venv:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run: venv
	. venv/bin/activate && app/main.py

shell:
	. venv/bin/activate && cd app && exec $$SHELL

compile_trans:
	pwd
	ls -l
	. venv/bin/activate && cd app && pybabel compile -d translations

update_trans:
	. venv/bin/activate && cd app && pybabel extract -F babel.cfg -o translations/messages.pot .
	. venv/bin/activate && cd app && pybabel update -d translations -i translations/messages.pot
