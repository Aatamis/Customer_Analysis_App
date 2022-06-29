import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('C:/Users/hp/Desktop/Customer_Analysis/The_Predicition_Model_2', 'rb'))

st.title("NHEF Customer On-Boarding Tool")
st.subheader("Instructions")
st.write("As you already know, the NHEF has a low barrier of entry for our clients. In order to assist the Sales & Credit Departments, the Investments unit has a developed a tool to identify customers that may require extra attention early on. Simply fill in this form at the time of onboarding and our system will indicate if the two units should place more emphasis on marketing and payment reminders to the customer in question. As we have a small team, the goal of this app is to ensure that efforts are placed where they need to be.")

st.subheader('GOOD LUCK!')

## For gender
gen_display = ('Female', 'Male')
gen_options = list(range(len(gen_display)))
gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

## For Marital Status
mar_display = ('No', 'Yes')
mar_options = list(range(len(mar_display)))
mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])


## No of dependets
dep_display = ('No','One','Two','More than Two')
dep_options = list(range(len(dep_display)))
dep = st.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])

## For Housing
Housing_display = ('Own','rent')
Housing_options = list(range(len(Housing_display)))
Housing = st.selectbox("Do you rent or own?",Housing_options, format_func=lambda x: Housing_display[x])

## For emp status
emp_display = ('Job','Business')
emp_options = list(range(len(emp_display)))
emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

## For Estate status
prop_display = ('Chibombo','Emerald Park','Riverdale')
prop_options = list(range(len(prop_display)))
prop = st.selectbox("Estate",prop_options, format_func=lambda x: prop_display[x])

## Applicant Monthly Income
income = st.number_input("Applicant's Monthly Income(ZMW)",value=0)

## Co-Applicant Monthly Income
co_mon_income = st.number_input("Co-Applicant's Monthly Income(ZMW)",value=0)

## Loan AMount
Plot_price = st.number_input("Plot Price",value=0)

#Any other debt
debt_display = ('No', 'Yes')
debt_options = list(range(len(mar_display)))
debt = st.selectbox("Any other debt?", debt_options, format_func=lambda x: debt_display[x])

## loan duration
dur_display = ['12 Months','24 Months','36 Months','48 Months','60 Months']
dur_options = range(len(dur_display))
dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])

if st.button("Submit"):
    duration = 0
    if dur == 0:
        duration = 12
    if dur == 1:
        duration = 24
    if dur == 2:
        duration = 36
    if dur == 3:
        duration = 48
    if dur == 4:
        duration = 60

features = [[gen, mar, dep, Housing, emp, income, co_mon_income, Plot_price, dur, debt, prop]]
print(features)

prediction = model.predict(features)

lc = [str(i) for i in prediction]
ans = int("".join(lc))
if ans == 0:
    st.error(
            "According to our Calculations, this customer's account does not need to be extensively monitored."
            )
else:
    st.success(
            "We predict this customer will need to be monitored closely."
            )







