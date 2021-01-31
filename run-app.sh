docker run --rm -it \
--network='host' \
-v `pwd`/scripts:/forecast-app/scripts \
forecastapp:latest \
streamlit run scripts/app.py