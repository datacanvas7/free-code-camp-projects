import pandas as pd

def calculate_demographic_data(print_data=True):
    # Define column names (since the file has no header)
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ]

    # Load the data with proper column names and handle whitespace
    df = pd.read_csv(
        'adult.data',
        header=None,
        names=column_names,
        skipinitialspace=True,  # Important for clean data
        na_values='?'           # Handle missing values marked as ?
    )

    # Question 1: How many people of each race are represented?
    race_count = df['race'].value_counts()

    # Question 2: Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Question 3: Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Question 4: Percentage with advanced education earning >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((higher_education & (df['salary'] == '>50K')).mean() * 100 / higher_education.mean(), 1)

    # Question 5: Percentage without advanced education earning >50K
    lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_rich = round((lower_education & (df['salary'] == '>50K')).mean() * 100 / lower_education.mean(), 1)

    # Question 6: Minimum hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # Question 7: Percentage working minimal hours with >50K
    num_min_workers = (df['hours-per-week'] == min_work_hours).sum()
    rich_percentage = round(((df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')).sum() * 100 / num_min_workers, 1)

    # Question 8: Country with highest percentage of >50K earners
    country_stats = (df[df['salary'] == '>50K']['native-country'].value_counts() / 
                    df['native-country'].value_counts() * 100).sort_values(ascending=False)
    highest_earning_country = country_stats.index[0]
    highest_earning_country_percentage = round(country_stats.iloc[0], 1)

    # Question 9: Top occupation in India for >50K earners
    top_IN_occupation = df[(df['native-country'] == 'India') & 
                          (df['salary'] == '>50K')]['occupation'].value_counts().index[0]

    # Return all answers in a dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }