web: python blockrsite/manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3 --log-level info --settings=settings.prod
scheduler: python blockrsite/manage.py celeryd -B -E --settings=settings.prod
