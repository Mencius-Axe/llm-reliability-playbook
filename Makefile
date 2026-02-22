.PHONY: check protocol evals

check: protocol evals links

protocol:
	python scripts/check_protocol_structure.py

evals:
	python scripts/check_evals_schema.py

links:
	python scripts/check_doc_links.py
