import pandas as pd
df = pd.read_excel("lojas.xlsx")
df.to_json("lojas.json", orient="records", force_ascii=False, indent=2)
