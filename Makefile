.PHONY: check modules evals links junk

check: modules evals links junk

modules:
	python3 scripts/check_modules.py

evals:
	python3 scripts/check_evals.py

links:
	python3 scripts/check_doc_links.py

junk:
	python3 scripts/check_no_paste_junk.py
