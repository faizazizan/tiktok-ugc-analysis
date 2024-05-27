import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Replace this URL with your CSV file's raw GitHub URL
csv_url = 'https://raw.githubusercontent.com/faizazizan/tiktok-ugc-analysis/main/github-ugc.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_url)

# Drop the first column
df = df.iloc[:, 1:]

# Add a numbered column
df.insert(0, 'Number', range(1, len(df) + 1))

# Handle non-string and NaN values in 'Price Range'
df['Price Range'] = df['Price Range'].astype(str).str.split('-').str[0].str.strip()
df['Price Range'] = pd.to_numeric(df['Price Range'], errors='coerce')

# Define custom labels for the price ranges
custom_labels = {
    0: 'Less than $50',
    50: 'Between $50 and $100',
    100: 'Between $100 and $150'
}

# Apply the custom labels
df['Price Range Labels'] = df['Price Range'].map(lambda x: custom_labels.get(x, 'Other'))

# Page Title
st.title("UGC Data Analysis Dashboard")

# Add YouTube video below the header
st.video("https://youtu.be/GL1Zs82Vg7s")

# Display Raw Data
st.subheader("Raw Data")
st.write(df)

# Distribution of Video Types
st.subheader("Distribution of Video Types")
video_type_counts = df['Video Type'].value_counts()
st.bar_chart(video_type_counts)

# Distribution of Selling Points
st.subheader("Distribution of Selling Points")
selling_point_distribution = df['Selling Point'].value_counts()
st.bar_chart(selling_point_distribution)

# Distribution of Hook Types
st.subheader("Distribution of Hook Types")
hook_type_counts = df['Hook Type'].value_counts()
st.bar_chart(hook_type_counts)

# Distribution of Categories
st.subheader("Distribution of Categories")
category_counts = df['Category'].value_counts()
st.bar_chart(category_counts)

# Distribution of Price Ranges
st.subheader("Distribution of Price Ranges")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(x='Price Range Labels', data=df, palette='viridis', order=custom_labels.values(), ax=ax)
ax.set_xlabel('Price Range')
ax.set_ylabel('Count')
ax.set_title('Distribution of Price Ranges')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Conclusion
st.markdown("---")
st.markdown("Created by [Faiz Azizan](https://faizazizan.com) ❤️")
