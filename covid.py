import pandas as pd
import tkinter as tk


covid_data = pd.read_csv('covid_data_age_range.csv')

def calculate_risk(age, gender, country):
    
    country_data = covid_data[covid_data['Country'] == country]
    
 
    if len(country_data[country_data['Age Range'] == age]) == 0 or len(country_data[(country_data['Age Range'] == age) & (country_data['Gender'] == gender)]) == 0:
        print("Error: Data for the given age and gender is not available for the selected country.")
        return
    
 
    total_deaths = country_data['Deaths'].sum()
    total_cases = country_data['Confirmed'].sum()
    mortality_rate = total_deaths / total_cases
    
   
    age_data = country_data[country_data['Age Range'] == age]
    gender_data = age_data[age_data['Gender'] == gender]
    age_gender_deaths = gender_data['Deaths'].sum()
    age_gender_cases = gender_data['Confirmed'].sum()
    age_gender_mortality_rate = age_gender_deaths / age_gender_cases

    risk = age_gender_mortality_rate / mortality_rate * 100
    
    return risk


window = tk.Tk()
window.title("COVID-19 Mortality Risk Calculator")
window.geometry("700x500")


label = tk.Label(window, text="COVID-19 Mortality Risk Calculator", font=(90))
label.pack(pady=10)
country_label = tk.Label(window, text="Select a country:", font=(50))
country_label.pack(pady=30)
countries = covid_data['Country'].unique()

country_var = tk.StringVar()
country_dropdown = tk.OptionMenu(window, country_var, *countries)
country_dropdown.pack()

age_label = tk.Label(window, text="Select an age group:",font=(50))
age_label.pack(pady=30)
ages = covid_data['Age Range'].unique()
age_var = tk.StringVar()
age_dropdown = tk.OptionMenu(window, age_var, *ages)
age_dropdown.pack()

sex_label = tk.Label(window, text="Select a sex:", font=(50))
sex_label.pack(pady=20)
sex_var = tk.StringVar()
sex_dropdown = tk.OptionMenu(window, sex_var, "Male", "Female")
sex_dropdown.pack()

# Define a function to calculate the risk and display the result
def calculate_and_display_risk():
    age = age_var.get()
    gender = sex_var.get()
    country = country_var.get()
    risk = calculate_risk(age, gender, country)
    if risk is not None:
        result_label.config(text='The risk of mortality is {:.2f}%.'.format(risk))
    else:
        result_label.config(text='Error: Data for the given age and gender is not available for the selected country.')

# Create a button to calculate the risk
calculate_button = tk.Button(window, text="Calculate", command=calculate_and_display_risk, font=70)
calculate_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="",font=(50))
result_label.pack(pady=10)

# Run the tkinter event loop
window.mainloop()
