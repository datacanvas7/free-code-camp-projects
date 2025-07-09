from demographic_data_analyzer import calculate_demographic_data

if __name__ == '__main__':
    results = calculate_demographic_data()

    print("Race Count:")
    print(results['race_count'])

    print("\nAverage Age of Men:", results['average_age_men'])

    print("\nPercentage with Bachelors:", results['percentage_bachelors'])

    print("\nPercentage with higher education earning >50K:", 
          results['higher_education_rich'])

    print("\nPercentage without higher education earning >50K:", 
          results['lower_education_rich'])

    print("\nMinimum work hours:", results['min_work_hours'])

    print("\nPercentage of minimal workers earning >50K:", 
          results['rich_percentage'])

    print("\nCountry with highest percentage of >50K earners:", 
          results['highest_earning_country'])

    print("Percentage:", results['highest_earning_country_percentage'])

    print("\nTop occupation in India for >50K earners:", 
          results['top_IN_occupation'])