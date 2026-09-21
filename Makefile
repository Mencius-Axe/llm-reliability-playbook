.PHONY: check modules evals links junk tests

check: modules evals links junk tests

tests:
	PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v

modules:
	python3 scripts/check_modules.py

evals:
	python3 scripts/check_evals.py

links:
	python3 scripts/check_doc_links.py

junk:
	python3 scripts/check_no_paste_junk.py
