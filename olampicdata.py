import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
csv_file_path = r'C:\Users\Amit\Desktop\CSV\dataset_olympics.csv'  # Replace with your CSV file path
data = pd.read_csv(csv_file_path)

# Q1: Rate between Male to Female participants
male_count = data[data['Sex'] == 'M']['ID'].nunique()
female_count = data[data['Sex'] == 'F']['ID'].nunique()
male_to_female_rate = male_count / female_count


# Q3: Number of participants per year
participants_per_year = data.groupby('Year')['ID'].nunique()

# Q4: Most participants winning Gold Medal per year
gold_medal_winners = data[data['Medal'] == 'Gold']
most_gold_medal_year = gold_medal_winners.groupby('Year')['ID'].nunique().idxmax()

# Q5: Most popular sport
most_popular_sport = data['Sport'].value_counts().idxmax()

# Create pie charts
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Q1: Rate between Male to Female participants
axes[0, 0].pie([male_count, female_count], labels=['Male', 'Female'], autopct='%1.1f%%')
axes[0, 0].set_title('Male to Female Participation Rate')


# Q3: Number of participants per year
axes[1, 0].pie(participants_per_year, labels=participants_per_year.index, autopct='%1.1f%%')
axes[1, 0].set_title('Participants per Year')

# Q4: Most participants winning Gold Medal per year
gold_medal_counts = gold_medal_winners.groupby('Year')['ID'].nunique()
axes[1, 1].pie(gold_medal_counts, labels=gold_medal_counts.index, autopct='%1.1f%%')
axes[1, 1].set_title('Gold Medal Winners per Year')

# Adjust layout
plt.tight_layout()
plt.show()

