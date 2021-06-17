docker run --rm -it \
--network='host' \
-v `pwd`/data:/knapsack-app/data \
-v `pwd`/scripts:/knapsack-app/scripts \
knapsackapp:latest \
streamlit run scripts/app.py