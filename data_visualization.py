# Data Visualization with Plotly
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [120, 135, 150, 170, 190, 210],
    'Profit': [30, 35, 40, 45, 55, 65]
})

# Line chart
fig1 = px.line(df, x='Month', y='Sales', title='Sales Trend', markers=True)
fig1.show()

# Bar chart
fig2 = px.bar(df, x='Month', y='Sales', title='Profit by Month', color='Profit')
fig2.show()

# Scatter plot
fig3 = px.scatter(df, x='Sales', y='Profit', title='Sales vs Profit', size='Profit')
fig3.show()
