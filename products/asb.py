import pandas as pd

df = pd.read_json("products\merge.json")

print(df.fields[0]['가격'])
print(df.fields[0]['운영체제'])
print(df.fields[0]['화면크기'])
print(df.fields[0]['해상도'])
print(df.fields[0]['스레드수'])
print(df.fields[0]['메모리용량'])
print(df.fields[0]['저장용량'])
print(df.fields[0]['GPU종류'])
print(df.fields[0]['TGP'])
print(df.fields[0]['무게'])
