import pandas as pd

df = pd.read_csv("notas_alunos.csv")

media = (df["nota_1"]+df["nota_2"])/2

df ["media"]= media

df.loc[df['media'] >= 7,'situação'] = "aprovado"
df.loc[df['media'] < 7 ,'situação'] = "reprovado"
df.loc[df['faltas'] >= 5 ,'situação'] = "reprovado"

mediat = df['media'].max()
faltam = df['faltas'].max()
mediag = df['media'].sum()

mediag = (mediag)/4


df.to_csv("alunos_situacao.csv") 
print("a media geral é ",mediag)
print("o maior numero de faltas teve ", faltam, "faltas")
print("a maior media é ", mediat)