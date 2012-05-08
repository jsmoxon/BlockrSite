web: python blockr/manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3 --log-level info --settings=settings.prod
scheduler: python blockr/manage.py celeryd -B -E --settings=settings.prod
