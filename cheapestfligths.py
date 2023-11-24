Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
... 
... def findCheapestPrice(n, flights, src, dst, k):
...     dp = [[float('inf')] * (k + 2) for _ in range(n)]
...     dp[src][0] = 0
...     paths = [[[] for _ in range(k + 2)] for _ in range(n)]
...     paths[src][0] = [src]
... 
...     for i in range(1, k + 2):
...         for u, v, w in flights:
...             if dp[u][i - 1] + w < dp[v][i]:
...                 dp[v][i] = dp[u][i - 1] + w
...                 paths[v][i] = paths[u][i - 1] + [v]
... 
...     min_cost = min(dp[dst])
...     min_path = paths[dst][dp[dst].index(min_cost)]
... 
...     return min_path, min_cost if min_cost < float('inf') else -1
... 
... # Read the dataset
... df = pd.read_csv('/content/flights.csv')
... 
... # Convert the dataframe to a list of lists
... flights = df.values.tolist()
... 
... # Determine the number of cities from the dataset
... n = max(max(df['source']), max(df['destination'])) + 1
... 
... src = int(input("Enter the source city: "))
... dst = int(input("Enter the destination city: "))
... k = int(input("Enter the maximum number of stops: "))
... 
... path, cost = findCheapestPrice(n, flights, src, dst, k)
... 
... if cost != -1:
...     print(f"Cheapest flight from city {src} to {dst} with at most {k} stops is {path} with a total cost of {cost}.")
... else:
...     print(f"No valid path found from city {src} to {dst} with at most {k} stops.")
