import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt   # 👈 Se importa matplotlib para mostrar el gráfico

df = sns.load_dataset("tips")  # Carga un dataset incluido
sns.barplot(x="day", y="total_bill", data=df)
plt.show() 
