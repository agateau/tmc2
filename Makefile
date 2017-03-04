all: run

clean:
	-rm -rf venv

venv:
	virtualenv --python python3 venv
	. venv/bin/activate && pip install -r requirements.txt

run: venv
	. venv/bin/activate && ./main.py

shell:
	. venv/bin/activate && exec $$SHELL
