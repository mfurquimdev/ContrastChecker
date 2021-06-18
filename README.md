# Checker for palette

This project is a simple checker for a palette whether the colors have enough contrast to pass the [Web Acessibility in Mind](https://webaim.org/resources/contrastchecker/) test.

It uses the rabbitmq as a broker, celery to process the requests asynchronously, and redis as a database.
