.PHONY: run etl

run:
	hypercorn api.app:app --bind 127.0.0.1:5000 --reload

etl:
	curl -X GET http://127.0.0.1:5000/etl
