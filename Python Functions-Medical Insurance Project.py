# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output_message = print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars")
  return estimated_cost, output_message

def diff_in_insurance_cost(insurance_cost_of_person1, insurance_cost_of_person2):
  diff_insurance_cost = insurance_cost_of_person1 - insurance_cost_of_person2
  difference_statement = print("The difference in insurance cost is " + str(diff_insurance_cost) + " dollars")
  return difference_statement


# Estimate Maria's insurance cost
maria_insurance_cost, maria_output_message = calculate_insurance_cost(28, 0, 26.2, 3, 0, "Maria")


# Estimate Omar's insurance cost 
omar_insurance_cost, omar_output_message = calculate_insurance_cost(35, 1, 22.2, 0, 1, "Omar")


#Estimate Nana's insurance cost
nana_insurance_cost = calculate_insurance_cost(24, 1, 25, 0, 0, "Nana")


#difference in insurance cost
insurance_cost_diff = diff_in_insurance_cost(omar_insurance_cost, maria_insurance_cost)
