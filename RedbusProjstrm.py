import streamlit as st
import mysql.connector
import pandas as pd
import base64
from streamlit_lottie import st_lottie
import pandas as pd
import json

def loadlottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
    
lottiefile =loadlottiefile("C:/Users/mraja/OneDrive/Desktop/ani/bus.json")


# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

image_path = "C:/Users/mraja/OneDrive/Desktop/ani/im.jpg"

encoded_image = get_base64_image(image_path)

ap_set=set()
df_ap=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/AP_bus.csv")
for i,r in df_ap.iterrows():
    ap_set.add(r["Bus_Routes_Name"])
ap_list=list(ap_set)

him_set=set()
df_him=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/Hima_bus.csv")
for i,r in df_him.iterrows():
    him_set.add(r["Bus_Routes_Name"])
him_list=list(him_set)

tel_set=set()
df_tel=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/Telangana_bus.csv")
for i,r in df_tel.iterrows():
    tel_set.add(r["Bus_Routes_Name"])
tel_list=list(tel_set)

kad_set=set()
df_kad=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/kadamba_bus.csv")
for i,r in df_kad.iterrows():
    kad_set.add(r["Bus_Routes_Name"])
kad_list=list(kad_set)

kl_set=set()
df_kl=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/kerala.csv")
for i,r in df_kl.iterrows():
    kl_set.add(r["Bus_Routes_Name"])
kl_list=list(kl_set)

nb_set=set()
df_nb=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/Northbengal_bus.csv")
for i,r in df_nb.iterrows():
    nb_set.add(r["Bus_Routes_Name"])
nb_list=list(nb_set)

up_set=set()
df_up=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/UP_bus.csv")
for i,r in df_up.iterrows():
    up_set.add(r["Bus_Routes_Name"])
up_list=list(up_set)

west_set=set()
df_west=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/Westbengal_bus.csv")
for i,r in df_west.iterrows():
    west_set.add(r["Bus_Routes_Name"])
west_list=list(west_set)

ra_set=set()
df_ra=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/Rajastan_bus.csv")
for i,r in df_ra.iterrows():
    ra_set.add(r["Bus_Routes_Name"])
ra_list=list(ra_set)

jk_set=set()
df_jk=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/Jharkand_bus.csv")
for i,r in df_jk.iterrows():
    jk_set.add(r["Bus_Routes_Name"])
jk_list=list(jk_set)

wb_set=set()
df_wb=pd.read_csv("C:/Users/mraja/Music/GUVIproj redbus/Redbus_10_States/WB_bus_details.csv")
for i,r in df_wb.iterrows():
    wb_set.add(r["Bus_Routes_Name"])
wb_list=list(wb_set)

    

st.set_page_config(page_title="Redbus Home", page_icon="🚌", layout="wide")

# Sidebar menu
st.sidebar.title("Online travel - Redbus")

page=st.sidebar.radio('Main Menu ',["Home", "Bus Info", "About"])


st.markdown(
    """
    <style>
    .main-heading {
        font-size: 40px;
        color: red;
        text-align:center;
    }
    .sub-heading {
        font-size: 20px;
        color: #fa8231;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Home page content
if page == "Home":
    st_lottie(
            lottiefile,
            speed=3,
            loop=True,
            height=300,
            width=1000,
            key=None
        )
    st.markdown("<h1 class='main-heading'>Welcome to Redbus</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .custom-image {
        height: 300px; 
        width:1000px
        }
        </style>
        """,
        unsafe_allow_html=True
        )
    st.markdown('<img src="https://mobisoftinfotech.com/assets/images/og-images/Bus-Booking-Software-And-Tracking-App.png" class="custom-image">', unsafe_allow_html=True)
    
        
    
    st.markdown("<h1 class='main-heading'>Go By Redbus Have a Green Life</h1>", unsafe_allow_html=True)
   
    st.markdown(
        """
        <style>
        .custom-image {
        height: 300px; 
        width:1000px
        }
        </style>
        """,
        unsafe_allow_html=True
    )
       
    st.markdown("<h2 class='sub-heading'>Book Your Bus Soon </h2>", unsafe_allow_html=True)
    
    # Design layout with columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<img src="https://media.gettyimages.com/id/165612440/vector/city-bus-vector-silhouette.jpg?s=612x612&w=0&k=20&c=0JTmw9_CqwnjQXxlFB0_LM52iT-mSEhQnpVE4FGrZNs=" class="custom-image">', unsafe_allow_html=True)
        st.markdown("<h3>Safe Travel</h3>", unsafe_allow_html=True)
        st.write("Travel safely with top-rated bus operators.")
      
    with col2:
        st.markdown('<img src="https://cdni.iconscout.com/illustration/premium/thumb/buying-tickets-on-train-online-illustration-download-in-svg-png-gif-file-formats--bus-booking-planning-trip-holding-smartphones-with-applications-pack-e-commerce-shopping-illustrations-7690026.png?f=webp" class="custom-image">', unsafe_allow_html=True)
        st.markdown("<h3>Easy Booking</h3>", unsafe_allow_html=True)
        st.write("Book your bus tickets effortlessly with just a few clicks.")

    with col3:
        st.markdown('<img src="https://static.vecteezy.com/system/resources/previews/021/708/463/original/affordable-pricing-icon-vector.jpg" class="custom-image">', unsafe_allow_html=True)
        st.markdown("<h3>Affordable Pricing</h3>", unsafe_allow_html=True)
        st.write("Find the best deals on bus tickets with competitive pricing.")
        
    
# Bus Info page
elif page == "Bus Info":
    st.markdown(
    """
    <style>
    .main {
        background-color:#660322;
     }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.title(":blue[Bus Information:]")
    st.write("Explore available bus routes, ratings, and prices")
    # Select bus route
    state=st.selectbox('Select the State:', ["Andhara Pradesh","Telangana","Himachal Pradesh","Jharkhand","Kerala","kadamba",
                                             "North bengal","Rajasthan", "West Bengal", "Uttar Pradesh"])
    
    fare=st.radio('Select the  Price:', ['Below 500', '500-1000', '1000-2000', 'Above 2000'],index=None)
    
    star=st.radio('Select the Rating: ',['More than 4 star','More than 3 star','More than 2 star','Less than 2 star'],index=0)

    star_condition = {
        'More than 4 star': '> 4',
        'More than 3 star': '> 3',
        'More than 2 star': '> 2',
        'Less than 2 star': '< 2'
    }

    if state=="West Bengal":
        z=st.selectbox("List of Routes",west_list,index=None)
        
        if fare=='Below 500':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount< 500 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df) 

        if fare=='500-1000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 500 and 1000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)   

        if fare=='1000-2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 1000 and 2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]}  order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)  

        if fare=='Above 2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount>=2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df) 

    if state=="Andhara Pradesh":
        z=st.selectbox("List of Routes",ap_list,index=None)
        
        if fare=='Below 500':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount< 500 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df) 

        if fare=='500-1000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 500 and 1000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)   

        if fare=='1000-2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 1000 and 2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]}  order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)  

        if fare=='Above 2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount>=2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)

    if state=="Himachal Pradesh":
        z=st.selectbox("List of Routes",him_list,index=None)
        
        if fare=='Below 500':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount< 500 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df) 

        if fare=='500-1000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 500 and 1000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)   

        if fare=='1000-2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 1000 and 2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]}  order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)  

        if fare=='Above 2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount>=2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)

    if state=="Telangana":
        z=st.selectbox("List of Routes",tel_list,index=None)
        
        if fare=='Below 500':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount< 500 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df) 

        if fare=='500-1000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 500 and 1000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)   

        if fare=='1000-2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 1000 and 2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]}  order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)  

        if fare=='Above 2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount>=2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)

    if state=="Jharkhand":
        z=st.selectbox("List of Routes",jk_list,index=None)
        
        if fare=='Below 500':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount< 500 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df) 

        if fare=='500-1000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 500 and 1000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)   

        if fare=='1000-2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 1000 and 2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]}  order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)  

        if fare=='Above 2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount>=2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)

    if state=="Kerala":
        z=st.selectbox("List of Routes",kl_list,index=None)
        
        if fare=='Below 500':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount< 500 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df) 

        if fare=='500-1000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 500 and 1000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)   

        if fare=='1000-2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 1000 and 2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]}  order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)  

        if fare=='Above 2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount>=2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)

    if state=="kadamba":
        z=st.selectbox("List of Routes",kad_list,index=None)
        
        if fare=='Below 500':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount< 500 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df) 

        if fare=='500-1000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 500 and 1000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)   

        if fare=='1000-2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 1000 and 2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]}  order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)  

        if fare=='Above 2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount>=2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)

    if state=="North bengal":
        z=st.selectbox("List of Routes",nb_list,index=None)
        
        if fare=='Below 500':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount< 500 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df) 

        if fare=='500-1000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 500 and 1000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)   

        if fare=='1000-2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 1000 and 2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]}  order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)  

        if fare=='Above 2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount>=2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)

    if state=="Rajasthan":
        z=st.selectbox("List of Routes",ra_list,index=None)
        
        if fare=='Below 500':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount< 500 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df) 

        if fare=='500-1000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 500 and 1000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)   

        if fare=='1000-2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 1000 and 2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]}  order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)  

        if fare=='Above 2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount>=2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)

    if state=="Uttar Pradesh":
        z=st.selectbox("List of Routes",up_list,index=None)
        
        if fare=='Below 500':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount< 500 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df) 

        if fare=='500-1000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 500 and 1000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)   

        if fare=='1000-2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount between 1000 and 2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]}  order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])  
            st.dataframe(df)  

        if fare=='Above 2000':
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="SQLraven#2024",
                database='myprojdatabase'
                )
            cursor = conn.cursor()
            query = f'''SELECT * FROM redbus_routes WHERE amount>=2000 and bus_routes_name= "{z}" and star_rating {star_condition[star]} order by amount desc'''
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description]) 
            st.dataframe(df)


# About page
elif page == "About":
    st.markdown(
    f"""
    <style>
    .main {{
        background-image: url("data:image/jpeg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    st.title(":red[About Us:]")
    st.markdown("<p style='color: black;font-size:22px'>RedBus is India’s largest online bus ticketing platform that has transformed bus travel in the country by bringing ease and convenience to millions of Indians who travel using buses.Founded in 2006, redBus is part of India’s leading online travel company MakeMyTrip Limited (NASDAQ: MMYT). By providing widest choice, superior customer service, lowest prices and unmatched benefits, redBus has served over 18 million customers. RedBus has a global presence with operations across Indonesia, Singapore, Malaysia, Colombia and Peru apart from India.</p>", unsafe_allow_html=True)
    st.subheader(":red[**We aim to provide a seamless and hassle-free travel experience**:]")

    st.markdown("<h2 style='color:#1d25b8;text-align:right'>Developed By :</h2>",unsafe_allow_html=True)
    st.markdown("<h3 style='color:#1d25b8;text-align:right'>Rajalakshmi Mathaiyan</h3>",unsafe_allow_html=True)
    

    




