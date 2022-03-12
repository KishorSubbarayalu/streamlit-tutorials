
# Load packages
import streamlit as st
import pandas as pd

# ****************************************************************************

# Set title of the application ; Text - title

title = "Welcome to Streamlit App"
st.title(title)

# Text - markdown

mdtext = 'Streamlit is **_really_ cool :sunglasses:**.'
st.markdown(mdtext)

# Text - header

head = 'Machine Learning'
st.header(head)

cc = """This application has popular supervised and unsupervised machine
           learning alogorithms."""
st.caption(cc)

# Text - subheader

st.subheader('Supervised')
st.subheader('Un-Supervised')

# Text - code
code = '''def function():
     print("Print Function")'''
st.code(code, language='python')

# Simple text
st.text('Below is the latex expression')

# Text - Latex expressions
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
     
# ****************************************************************************

num = 1234

string = "I Live in Canada!"

df = pd.DataFrame({
     'X': [1, 2, 3, 4],
     'Y': [10, 20, 30, 40],
 })

st.write(num, string, df)

# ****************************************************************************

table = {
            'id' : [1,2,3,4],
            'name' : ['kishor','Arun','Prabav','Arul'],
            'age' : [25,27,23,29]                
        }

st.subheader('Dataframe:')

dataframe = pd.DataFrame(table)
st.dataframe(dataframe)

ordf = pd.read_csv('data/OnlineRetail.csv')
st.dataframe(ordf, width=1000, height=300)

st.subheader('Table:')

st.table(table)

st.subheader('Metrics:')

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

json_text = {"menu": {
              "id": "file",
              "value": "File",
              "popup": {
                "menuitem": [
                  {"value": "New", "onclick": "CreateNewDoc()"},
                  {"value": "Open", "onclick": "OpenDoc()"},
                  {"value": "Close", "onclick": "CloseDoc()"}
                ]
              }
            }}

st.subheader('JSON format:')

st.json(json_text)




























