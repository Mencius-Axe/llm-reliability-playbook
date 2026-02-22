.PHONY: check protocol evals

check: protocol evals links

protocol:
	python3 scripts/check_protocol_structure.py

evals:
	python3 scripts/check_evals_schema.py

links:
	python3 scripts/check_doc_links.py
