.PHONY: run etl ask

run:
	hypercorn api.app:app --bind 127.0.0.1:5000 --reload

etl:
	curl -X GET http://127.0.0.1:5000/etl

ask:
	curl -X POST http://127.0.0.1:5000/chat-message \
		-H "Content-Type: application/json" \
		-d '{"question": "Qual é a distribuição dos casos de tuberculose por situação de encerramento?"}'
