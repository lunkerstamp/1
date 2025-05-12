import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('数据.xls')
country_names = input("请输入要分析的多个国家名称（用英文逗号隔开）: ")
countries = [country.strip() for country in country_names.split(',')]
selected_data = data[data['Country Name'].isin(countries)]

if selected_data.empty:
    print(f"未找到 {country_names} 这些国家的数据，请检查输入是否正确。")
else:
    year_input = input(f"请输入要分析的年份（1960-2024）（用英文逗号隔开）: ")
    years = [int(year.strip()) for year in year_input.split(',')]

    years = [str(year) for year in years]
    filtered_data = selected_data[selected_data[years].notnull().any(axis=1)]

    if filtered_data.empty:
        print(f"{country_names} 这些国家中未找到 {year_input} 年份的数据，请检查输入是否正确。")
    else:
        print(filtered_data[years].describe())

        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        for year in years:
            sns.histplot(filtered_data[year].dropna(), kde=True, color='skyblue', alpha=0.6, label=year)
        plt.title(f"{country_names} 在 {year_input} 年份人口超过100万的城市群中的人口（占总人口的百分比）分布")
        plt.xlabel('百分比')
        plt.ylabel('频率')
        plt.legend()
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(10, 6))
        for country in countries:
            country_data = filtered_data[filtered_data['Country Name'] == country]
            for year in years:
                x = country_data.index[country_data[year].notnull()]
                y = country_data[year].dropna()
                if not x.empty and not y.empty:
                    sns.lineplot(x=x, y=y, label=f"{country} - {year}")
        plt.title(f"{country_names} 在 {year_input} 年份人口超过100万的城市群中的人口（占总人口的百分比）随时间变化")
        plt.xlabel('年份')
        plt.ylabel('百分比')
        plt.legend()
        plt.tight_layout()
        plt.show()