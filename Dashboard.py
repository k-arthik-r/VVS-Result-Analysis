import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import pandas as pd


st.set_page_config(page_title="VVS", layout="wide", initial_sidebar_state="collapsed")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

df = pd.read_csv("Student.csv")
specified_columns = ['Name', 'Language', 'English', 'Maths', 'Science', 'Social', 'Percentage', 'Result',  'Gender', 'Section',]
new_df = df[specified_columns].copy()

result_counts = df['Result'].value_counts()
result_gender = df['Gender'].value_counts()
numOfStudents = len(df)

st.title("Vidyavardhaka School Result Analysis")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)



st.text("")

col0_1, col0_2, col0_3 = st.columns([8, 2, 2])

with col0_2:
    if st.button("Section A Analysis"):
        switch_page("Section_A")

with col0_3:
    if st.button("Section B Analysis"):
        switch_page("Section_B")   
    


col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    st.subheader("Overall Results")
    fig = px.pie(values=result_counts.values, names=result_counts.index, hole=0.5, color_discrete_sequence=['#F6995C', '#FDFFAB'])
    fig.update_traces(text = result_counts.index, textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Student Details")
    container = st.container(border=True)
    container.write(f"**Total Number of Students: {numOfStudents}**")

    col2_1, col2_2 = st.columns((2))
    
    with col2_1:
        container2_1 = st.container(border=True)
        container2_1.write("**Boys**")
        container2_1.write(f"**{result_gender['Male']}**")

    with col2_2:
        container2_2 = st.container(border=True)
        container2_2.write("**Girls**")
        container2_2.write(f"**{result_gender['Female']}**")

    with col2_1:
        container2_1 = st.container(border=True)
        container2_1.write("**Total Number of Pass**")
        container2_1.write(f"**{result_counts['Pass']}**")

    with col2_2:
        container2_2 = st.container(border=True)
        container2_2.write("**Total Number of Fails**")
        container2_2.write(f"**{result_counts['Fail']}**")


st.subheader("Overall Grades")

# col3_1, col3_2, col3_3, col3_4, col3_5, col3_6 = st.columns((6))
# col3list = [col3_1, col3_2, col3_3, col3_4, col3_5, col3_6]

students_90_above = df[df['Percentage'] >= 90]
num_students_90_above = len(students_90_above)

students_80_above = df[(df['Percentage'] >= 80) & (df['Percentage'] < 90)]
num_students_80_above = len(students_80_above)

students_70_above = df[(df['Percentage'] >= 70) & (df['Percentage'] < 80)]
num_students_70_above = len(students_70_above)

students_60_above = df[(df['Percentage'] >= 60) & (df['Percentage'] < 70)]
num_students_60_above = len(students_60_above)

students_40_above = df[(df['Percentage'] >= 40) & (df['Percentage'] < 60)]
num_students_40_above = len(students_40_above)

students_40_below = df[df['Percentage'] < 40]
num_students_40_below = len(students_40_below)


# for i in col3list:
#     with i:
#         container = st.container(border=True)

#         if i is col3_1:
#             container.write("**S Grade**")
#             container.write(f"**{num_students_90_above}**")

#         if i is col3_2:
#             container.write("**A Grade**")
#             container.write(f"**{num_students_80_above}**")

#         if i is col3_3:
#             container.write("**B Grade**")
#             container.write(f"**{num_students_70_above}**")

#         if i is col3_4:
#             container.write("**C Grade**")
#             container.write(f"**{num_students_60_above}**")

#         if i is col3_5:
#             container.write("**D Grade**")
#             container.write(f"**{num_students_40_above}**")

#         if i is col3_6:
#             container.write("**X Grade**")
#             container.write(f"**{num_students_40_below}**")

st.text("")
st.text("")


dfg = pd.DataFrame(
    [
        { "Grade" : "S", "Number of Students": num_students_90_above},
        { "Grade" : "A", "Number of Students": num_students_80_above},
        { "Grade" : "B", "Number of Students": num_students_70_above},
        { "Grade" : "C", "Number of Students": num_students_60_above},
        { "Grade" : "D", "Number of Students": num_students_40_above},
        { "Grade" : "X", "Number of Students": num_students_40_below}

    ]
)

st.dataframe(dfg, use_container_width=True, hide_index=True)

st.text("")
st.text("")
st.text("")

col4= st.columns((1))

with col4[0]:
    st.subheader("Conmaprision of Average score between Section A and Section B")
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    avg_scores = df.groupby('Section')[numeric_columns].mean().reset_index()
    avg_scores_melted = avg_scores.melt(id_vars='Section', var_name='Subject', value_name='Average Score')
    fig_line_section = px.line(avg_scores_melted, x='Subject', y='Average Score', color='Section',
                            labels={'Average Score': 'Average Score', 'Subject': 'Subject', 'Section': 'Section'})
    st.plotly_chart(fig_line_section, use_container_width=True)
    # st.subheader("Comparison of Average score between Section A and Section B")
    # avg_scores_pivoted = avg_scores_melted.pivot(index='Subject', columns='Section', values='Average Score')
    # st.line_chart(avg_scores_pivoted, use_container_width=True,)


def barChart(lan):
    pass_sub = df[df['Pass/Fail'] == 'Pass']
    pass_count = pass_sub.groupby('Section').size()
    sections = ['A', 'B']
    pass_count = pass_count.reindex(sections, fill_value=0).reset_index(name='Pass Count')
    if pass_count.iloc[0]['Pass Count'] > pass_count.iloc[1]['Pass Count']:
        colors = ['#5463FF', '#FF6B6B']
    elif pass_count.iloc[0]['Pass Count'] < pass_count.iloc[1]['Pass Count']:
        colors = ['#FF6B6B', '#5463FF']
    else:
        colors = ['#6BCB77', '#6BCB77']
    fig = px.bar(pass_count, x='Section', y='Pass Count', 
             title=f'{lan}',
             labels={'Pass Count': 'Pass Count', 'Section': 'Section'},
             color='Section',
             color_discrete_sequence = colors)
    fig.update_layout(yaxis=dict(range=[0, 40]))

    st.plotly_chart(fig, use_container_width=True)

st.subheader("Subject Wise Result Analysis")

col5_1, col5_2, col5_3 = st.columns(3)

with col5_1:
    df['Pass/Fail'] = df['Language'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    barChart(lan = "Language")

with col5_2:
    df['Pass/Fail'] = df['English'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    barChart(lan = "English")   

with col5_3:
    df['Pass/Fail'] = df['Maths'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    barChart(lan = "Maths")

with col5_1:
    df['Pass/Fail'] = df['Science'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    barChart(lan = "Science")  

with col5_2:
    df['Pass/Fail'] = df['Social'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    barChart(lan = "Social Science") 

st.subheader("Leader Board")

pass_students_section_a = df[(df['Result'] == 'Pass')]
pass_students_section_a_sorted = pass_students_section_a.sort_values(by='Percentage', ascending=False)
top_3_students = pass_students_section_a_sorted[['Name', 'Percentage']].head(3)

fail_students_section_a = df[(df['Result'] == 'Fail')]
fail_students_section_a_sorted = fail_students_section_a.sort_values(by='Percentage')
bottom_3_students = fail_students_section_a_sorted[['Name', 'Percentage']].head(3)

col7, col8 = st.columns(2)

with col7:
    container7_1 = st.container(border=True)
    container7_1.write(f"Rank {0+1}")
    container7_1.write(f"**{top_3_students.iloc[0]['Name']}**")   
    container7_1.write(f"**{top_3_students.iloc[0]['Percentage']}**")

    container7_2 = st.container(border=True)
    container7_2.write(f"Rank {0+2}")
    container7_2.write(f"**{top_3_students.iloc[1]['Name']}**")   
    container7_2.write(f"**{top_3_students.iloc[1]['Percentage']}**")

    container7_3 = st.container(border=True)
    container7_3.write(f"Rank {0+3}")
    container7_3.write(f"**{top_3_students.iloc[2]['Name']}**")   
    container7_3.write(f"**{top_3_students.iloc[2]['Percentage']}**")

with col8:
    container8_1 = st.container(border=True)
    container8_1.write(f"Rank {numOfStudents - 2}")
    container8_1.write(f"**{bottom_3_students.iloc[2]['Name']}**")   
    container8_1.write(f"**{bottom_3_students.iloc[2]['Percentage']}**")

    container8_2 = st.container(border=True)
    container8_2.write(f"Rank {numOfStudents - 1}")
    container8_2.write(f"**{bottom_3_students.iloc[1]['Name']}**")   
    container8_2.write(f"**{bottom_3_students.iloc[1]['Percentage']}**")

    container8_3 = st.container(border=True)
    container8_3.write(f"Rank {numOfStudents}")
    container8_3.write(f"**{bottom_3_students.iloc[0]['Name']}**")   
    container8_3.write(f"**{bottom_3_students.iloc[0]['Percentage']}**")

with st.expander('Student Details'):
    # st.write(new_df.style.background_gradient(cmap="Blues"))
    st.dataframe(new_df, use_container_width=True, hide_index=True)

csv = new_df.to_csv(index=False).encode('utf-8')
st.download_button('Download Student Data', data=csv, file_name="StudentData.csv", mime="text/csv")

