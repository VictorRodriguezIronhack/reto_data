import streamlit as st
from PIL import Image
from tools import functions as func
import pandas as pd
import seaborn as sns

consume_data = pd.read_csv("./data/consume_data.csv")
refill_data = pd.read_csv("./data/refill_data.csv")

st.write("""
# Cobify fuel analysis
""")

"This is a data analysis for cobify interview data analyst position."
"I will compare and analyze two fuels (SP98 and E10) to decide which one is better for Cobify."
# st.text(""" """)

imagen = Image.open("images/cobify.png")
st.image(imagen)

st.subheader("Basic notions that i've got doing this research:")
st.write("""
- Cars after year 2000 can use E10 fuel with no problems. I asume that Cobify have all their car fleet newer than this year. If this is not the case, initially they should use SP98 or we can check each car using pages like this one: https://www.gov.uk/check-vehicle-e10-petrol
- I've analized both fuels in Spain. In the API phase, i got some E10 prices but there are too few gas stations that sell it. Focusing my analysis in Spain, i'll recommend to use SP98 due to lack of availability of this fuel.
""")
"After doing this clarifications, i will proceed with my analysis of both fuels."
st.subheader("Analysis:")
""

"#### Countplot of both gas consumes:"

histplot_1 = Image.open("images/histplot1.png")
st.image(histplot_1)

st.table(func.stats_df(consume_data))

"We can see that SP98 gas has a bigger standard deviation consume, we can estimate much better what will be the consume with E10 gas. Also, E10 has a slighly higher consume mean."

"#### Scatterplots of both gas correlations between speeds vs distance and consume:"

scatterplot_1 = Image.open("images/scatterplot1.png")
st.image(scatterplot_1)

"We can see that SP98 has several more performance around 4 lt/100km than E10 but also has several high consume trips."

scatterplot_2 = Image.open("images/scatterplot2.png")
st.image(scatterplot_2)

"In this plot we can see that every high consume is produce by low speeds and SP98 has a higher consume mean at low speeds."

"#### In the left side we have SP98 consumes vs sunny, rainy and snowy days. On the right side, the same but with E10 data. Also, with a red line it's define each gas type consume mean:"

main_scatterplot = Image.open("images/main_scatterplot.png")
st.image(main_scatterplot)

"During this analysis, we confirmed that outside temperature and type of day (sunny, rainy and snowy) are correlated."

st.write("""Now we can confirm that depending on the temperature outside we have a different gas performance. Findings:
- It's clear that in sunny days both fuels perform better (under consume mean), due to the outside temperature
- In rainy days, performance get worse, being around each fuel consume mean.
- And in snowy days, this fuels has their worst performance due to low temperatures getting way over their consume means.
""")
"We can see a slightlty better performance of E10 fuel in sunny getting almost every consume under fuel mean."

scatterplot_3 = Image.open("images/scatterplot3.png")
st.image(scatterplot_3)


st.subheader("Comparision:")

left_column, right_column = st.beta_columns(2)

with left_column:
    "#### SP98 fuel:"
    st.write("""
    - A
    - B
    - C
    """)

with right_column:
    "#### E10 fuel:"
    st.write("""
    - Less standard deviation. Easier to predict it's consume.
    - Slightly better performance in sunny days.
    - Lower consume at low speeds.
    - Lower price.
    - More environmental friendly.
    """)

st.subheader("Conlusion:")

st.write("""
- A
- B
- C
""")

st.subheader("Recommendations:")

st.write("""
- A
- B
- C
""")