#real API response --- JSON structure=dictionary
user_data={"id":101,"name":"kavi","age":21,"skills":["python","sql,power BI"]}
print(user_data["name"])
print(user_data["skills"][0])

#pandas - columns rename
import pandas as pd
df=pd.DataFrame({"nm":["kavi","priya"],"ag":[21,22]})
df.rename(columns={"nm":"name","ag":"age"},inplace=True)
print(df)

#value mapping-category encode
#ML string to number conversion
grade_map={"A+":4,"A":6,"B":6,"C":5,"F":9}
grades=["A+","B","A","C","F"]
encoded=[grade_map[g] for g in grades]
print(encoded)

#word frequency counter ---->sentiment analysis,text mining
text="i will be a good job holder in my interview and a impressive person"
freq={}
for word in text.split():
    freq[word]=freq.get(word,0)+1
print(freq)


'''dictionary
       |
    JSON Parsing        <--    API data handle
       |
    pandas mapping      <--    Data cleaning
       |
    Label encoding      <--    ML preprocessing
       |
    MLP word count      <--    Text analysis
    '''