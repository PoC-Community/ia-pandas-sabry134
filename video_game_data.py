# Python
import matplotlib.pyplot as plt

top_games = data.groupby('Name')['Global_Sales'].sum().sort_values(ascending=False)

top_games = top_games[:10]

plt.figure(figsize=(10,5))
plt.barh(top_games.index, top_games.values, color='skyblue')
plt.xlabel('Global Sales (in millions)')
plt.title('Top 10 Games by Global Sales')
plt.gca().invert_yaxis()
plt.show()