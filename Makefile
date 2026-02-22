.PHONY: check protocol evals

check: protocol evals

protocol:
	python scripts/check_protocol_structure.py

evals:
	python scripts/check_evals_schema.py
