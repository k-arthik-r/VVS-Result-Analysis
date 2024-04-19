import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="VVS", layout="wide", initial_sidebar_state="collapsed")

with open('styleA.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

df = pd.read_csv("./students.csv")
section_a = df[df['Section'] == 'A']
specified_columns = ['Name', 'Language', 'English', 'Maths', 'Science', 'Social', 'Percentage', 'Result',  'Gender']
new_df = section_a[specified_columns].copy()


st.title("Section A Analysis")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

st.text("")

col0_1, col0_2, col0_3 = st.columns([8, 2, 2])

with col0_3:
    if st.button("Dashboard"):
        switch_page("Dashboard")  

st.subheader("Subject Wise Result Analysis")

subjects = ['Maths', 'Science', 'Social', 'Language']

def pie(subject):
    pass_students = section_a[(section_a[subject] >= 40)]
    fail_students = section_a[(section_a[subject] < 40)]
    
    pass_count = len(pass_students)
    fail_count = len(fail_students)
    
    title = f'{subject}'

    labels = ['Pass', 'Fail']
    values = [pass_count, fail_count]
    fig = px.pie(names=labels, values=values, title=title, hole=0.5)
    fig.update_traces(text = labels, textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

col1_1, col1_2, col1_3,col1_4, col1_5 = st.columns((5))

with col1_1:
    df['Pass/Fail'] = df['Language'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    pie(subject = "Language")

with col1_2:
    df['Pass/Fail'] = df['English'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    pie(subject = "English")   

with col1_3:
    df['Pass/Fail'] = df['Maths'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    pie(subject = "Maths")

with col1_4:
    df['Pass/Fail'] = df['Science'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    pie(subject = "Science")  

with col1_5:
    df['Pass/Fail'] = df['Social'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    pie(subject = "Social") 

length_section_A = len(df[df['Section'] == 'A'])
section_A_counts = df[df['Section'] == 'A']['Result'].value_counts()
section_A_gender = df[df['Section'] == 'A']['Gender'].value_counts()

# Calculate the average marks for each subject in Section A
average_marks = []
subjects = [ 'Language', 'English', 'Maths', 'Science', 'Social']
for subject in subjects:
    avg_mark = section_a[subject].mean()
    average_marks.append(avg_mark)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.subheader("Section A Results")
    fig = px.pie(values=section_A_counts.values, names=section_A_counts.index, hole=0.5)
    fig.update_traces(text = section_A_counts.index, textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Student Details")
    st.text("")
    st.text("")
    st.text("")
    container = st.container(border=True)
    container.write(f"**Total Number of Students: {length_section_A}**")

    col1_1, col1_2 = st.columns((2))
    
    with col1_1:
        container2_1 = st.container(border=True)
        container2_1.write("**Boys**")
        container2_1.write(f"**{section_A_gender['Male']}**")

    with col1_2:
        container2_2 = st.container(border=True)
        container2_2.write("**Girls**")
        container2_2.write(f"**{section_A_gender['Female']}**")

    with col1_1:
        container2_1 = st.container(border=True)
        container2_1.write("**Total Number of Pass**")
        container2_1.write(f"**{section_A_counts['Pass']}**")

    with col1_2:
        container2_2 = st.container(border=True)
        container2_2.write("**Total Number of Fails**")
        container2_2.write(f"**{section_A_counts['Fail']}**")

st.text("")
st.subheader("Grades")

col3_1, col3_2, col3_3, col3_4, col3_5, col3_6 = st.columns(6)
col3list = [col3_1, col3_2, col3_3, col3_4, col3_5, col3_6]

# Calculate the number of students in each grade range for Section A
students_90_above = section_a[section_a['Percentage'] >= 90]
num_students_90_above = len(students_90_above)

students_80_above = section_a[(section_a['Percentage'] >= 80) & (section_a['Percentage'] < 90)]
num_students_80_above = len(students_80_above)

students_70_above = section_a[(section_a['Percentage'] >= 70) & (section_a['Percentage'] < 80)]
num_students_70_above = len(students_70_above)

students_60_above = section_a[(section_a['Percentage'] >= 60) & (section_a['Percentage'] < 70)]
num_students_60_above = len(students_60_above)

students_40_above = section_a[(section_a['Percentage'] >= 40) & (section_a['Percentage'] < 60)]
num_students_40_above = len(students_40_above)

students_40_below = section_a[section_a['Percentage'] < 40]
num_students_40_below = len(students_40_below)

# Display the grades in each column
for i in col3list:
    with i:
        container = st.container(border=True)

        if i is col3_1:
            container.write("**S Grade**")
            container.write(f"**{num_students_90_above}**")

        if i is col3_2:
            container.write("**A Grade**")
            container.write(f"**{num_students_80_above}**")

        if i is col3_3:
            container.write("**B Grade**")
            container.write(f"**{num_students_70_above}**")

        if i is col3_4:
            container.write("**C Grade**")
            container.write(f"**{num_students_60_above}**")

        if i is col3_5:
            container.write("**D Grade**")
            container.write(f"**{num_students_40_above}**")

        if i is col3_6:
            container.write("**X Grade**")
            container.write(f"**{num_students_40_below}**")

st.text("")
st.text("")
st.text("")

col3, col4 = st.columns(2, gap="medium")

with col3:
    st.subheader("Subject Wise Average Marks")
    st.text("")
    st.text("")
    st.text("")
    col3_1, col3_2 = st.columns((2))
    
    with col3_1:
        container2_1 = st.container(border=True)
        container2_1.write("**Language**")
        container2_1.write(f"**{average_marks[0]}**")

    with col3_2:
        container2_2 = st.container(border=True)
        container2_2.write("**English**")
        container2_2.write(f"**{average_marks[1]}**")

    with col3_1:
        container2_1 = st.container(border=True)
        container2_1.write("**Maths**")
        container2_1.write(f"**{average_marks[2]}**")

    with col3_2:
        container2_2 = st.container(border=True)
        container2_2.write("**Science**")
        container2_2.write(f"**{average_marks[3]}**")

    with col3_1:
        container2_1 = st.container(border=True)
        container2_1.write("**Social Science**")
        container2_1.write(f"**{average_marks[4]}**")

with col4:
    st.subheader("Graphical Analysis")
    fig = px.bar(x=subjects, y=average_marks, labels={'x': 'Subject', 'y': 'Average Marks'})
    st.plotly_chart(fig, use_container_width=True)


st.subheader("Leader Board")

pass_students_section_a = df[(df['Section'] == 'A') & (df['Result'] == 'Pass')]
pass_students_section_a_sorted = pass_students_section_a.sort_values(by='Percentage', ascending=False)
top_3_students = pass_students_section_a_sorted[['Name', 'Percentage']].head(3)

fail_students_section_a = df[(df['Section'] == 'A') & (df['Result'] == 'Fail')]
fail_students_section_a_sorted = fail_students_section_a.sort_values(by='Percentage')
bottom_3_students = fail_students_section_a_sorted[['Name', 'Percentage']].head(3)

col5, col6 = st.columns(2)

with col5:
    container5_1 = st.container(border=True)
    container5_1.write(f"Rank {0+1}")
    container5_1.write(f"**{top_3_students.iloc[0]['Name']}**")   
    container5_1.write(f"**{top_3_students.iloc[0]['Percentage']}**")

    container5_2 = st.container(border=True)
    container5_2.write(f"Rank {0+2}")
    container5_2.write(f"**{top_3_students.iloc[1]['Name']}**")   
    container5_2.write(f"**{top_3_students.iloc[1]['Percentage']}**")

    container5_3 = st.container(border=True)
    container5_3.write(f"Rank {0+3}")
    container5_3.write(f"**{top_3_students.iloc[2]['Name']}**")   
    container5_3.write(f"**{top_3_students.iloc[2]['Percentage']}**")

with col6:
    container6_1 = st.container(border=True)
    container6_1.write(f"Rank {length_section_A - 2}")
    container6_1.write(f"**{bottom_3_students.iloc[2]['Name']}**")   
    container6_1.write(f"**{bottom_3_students.iloc[2]['Percentage']}**")

    container6_2 = st.container(border=True)
    container6_2.write(f"Rank {length_section_A - 1}")
    container6_2.write(f"**{bottom_3_students.iloc[1]['Name']}**")   
    container6_2.write(f"**{bottom_3_students.iloc[1]['Percentage']}**")

    container6_3 = st.container(border=True)
    container6_3.write(f"Rank {length_section_A}")
    container6_3.write(f"**{bottom_3_students.iloc[0]['Name']}**")   
    container6_3.write(f"**{bottom_3_students.iloc[0]['Percentage']}**")

with st.expander('Student Details'):
    st.write(new_df.style.background_gradient(cmap="Blues"))

csv = new_df.to_csv(index=False).encode('utf-8')
st.download_button('Download Section A Student Data', data=csv, file_name="StudentData_A.csv", mime="text/csv")