

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import streamlit as st





st.text("Pizza Sales Dashboard")

path = "Data Model - Pizza Sales.xlsx"
df = pd.read_excel(path, index_col="order_details_id")





df.drop(columns='order_id', axis=1, inplace=True)








df["order_time"] = pd.to_datetime(df.order_time, format='%H:%M:%S')


df["hours"] = df["order_time"].dt.hour




df["order_month"] = df["order_date"].dt.month


df["order_year"] = df["order_date"].dt.year
df["order_day"] = df["order_date"].dt.day




df["order_day"] = df["order_day"].replace([1,2,3,4,5,6,7], ['Thursday','Friday','Saturday','Sunday','Monday','Tuesday','Wednesday'])




df["order_month"] = df["order_month"].replace([1,2,3,4,5,6,7,8,9,10,11,12], ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])








top_10_pizza = df["pizza_name"].value_counts().iloc[:15]



plt.figure(figsize=(20,10),facecolor= '#73726b')
sns.countplot(y= 'pizza_name' , data = df, palette="winter", order= df["pizza_name"].value_counts().iloc[:11].index)

plt.xticks(fontsize=20)

plt.yticks(fontsize=25)
plt.title("Top 10 Pizza By Sales", fontsize=30)
plt.xlabel("")
plt.ylabel("Pizza Name", fontsize=20)
plt.show()




plt.figure(figsize=(25,15),facecolor= '#9cc276')
sns.countplot(data=df, x= "order_month" ,palette="hot", hue=df["pizza_category"], order=df["order_month"].value_counts().iloc[:].index)
plt.legend(prop={'size': 20})
plt.xticks(fontsize=20)

plt.yticks(fontsize=25)
plt.title("Category", fontsize=30)
plt.xlabel("")
plt.ylabel("Pizza Name", fontsize=25)
plt.show()




pie_new_df = df["pizza_size"].value_counts().rename_axis('size').reset_index(name='value')




plt.figure(figsize=(7,10),facecolor= '#dae3d1')
plt.pie(x = pie_new_df["value"], shadow=True ,textprops={'fontsize':'12'} , explode= [0.15, 0, 0, 0, 0] , labels= pie_new_df["size"], autopct='%.0f%%' )

plt.yticks(fontsize=25)
plt.title("Pizza Size", fontsize=30)

plt.show()




new_df_hour = pd.DataFrame(df["hours"].value_counts())
x = new_df_hour.index
y = new_df_hour['hours']




plt.figure(figsize=(15,10),facecolor= '#9cc276')

# sns.countplot(data=df, x= 'hours', palette='crest')
sns.barplot(x = x, y= y , )
plt.xticks(fontsize=15)

plt.yticks(fontsize=15)
plt.title("Rush Hours", fontsize=25)
plt.xlabel("Time",fontsize=15)
plt.ylabel("Coustomer", fontsize=15)



plt.show()




from wordcloud import WordCloud
plt.figure(figsize=(25,20))
text = " ".join(cat for cat in df.pizza_ingredients)

word_cloud = WordCloud(
        width=3000,
        height=2000,
        random_state=1,
        background_color="black",
        colormap="Pastel1",
        ).generate(text)

plt.imshow(word_cloud)

plt.show()

