web: python blockrsite/manage.py run_gunicorn -b "0.0.0.0:$PORT"
worker: python blockrsite/manage.py celeryd -B -E --loglevel=INFO
