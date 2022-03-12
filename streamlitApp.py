
# Load packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ****************************************************************************

selectbox = st.sidebar.radio(
    "Which element you want to see?",
    ("Text elements", "Data elements", "Chart elements","Input elements")
)

# ****************************************************************************

# Set title of the application ; Text - title

if selectbox == "Text elements":

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

if selectbox == "Data elements":

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

# ****************************************************************************

if selectbox == "Chart elements":
    
    
    ordf = pd.read_csv('data/OnlineRetail.csv')
    
    st.line_chart(ordf['UnitPrice'])
    
    bar_data = ordf[ordf['InvoiceNo'] == 536365].loc[:,['StockCode','Quantity']]
    
    fig, ax = plt.subplots()
    ax.set_title('Quantity purchased for each Products')
    ax.set_xlabel('Product Codes')
    ax.set_ylabel('Quantity')
    ax.bar('StockCode','Quantity',data = bar_data)
    st.pyplot(fig)
    
    bar_dict = pd.DataFrame(data = np.array(bar_data['Quantity']),
                            index = np.array(bar_data['StockCode']))
    
    st.bar_chart(bar_dict) 
    st.area_chart(bar_dict)
    
    df_map = pd.read_csv('data/canadacities.csv')
    df_map = df_map[df_map['province_name'] == 'Nova Scotia'].loc[:,['lat','lon']]
    
    
    st.map(df_map)

# ****************************************************************************

if selectbox == "Input elements":

    st.subheader("Input Widgets:")
    
    if st.button("hit like!"):
        st.write("you liked this content")
    else:
        pass
    
    name = st.text_input("Name")
    st.write(name)
    
    address = st.text_area("Enter your address")
    st.write(address)
    
    st.date_input("enter a date")
    
    st.time_input("enter a time")
    
    if st.checkbox("Accept the T&C",value = True):
        st.write("Thank you")
    
    v1 = st.radio("Colours",["r","g","b"],index = 1)
    v2 = st.selectbox("Colours",["r","g","b"],index = 0)
    
    st.write(v1,v2)
    
    v3 = st.multiselect("Colours",["r","g","b"])
    st.write(v3)
    
    st.slider("age",min_value = 18,max_value=60,value = 30,step = 2)
    
    st.number_input("numbers",min_value = 18,max_value=60,value = 30,step = 2)

# ****************************************************************************


