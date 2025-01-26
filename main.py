import streamlit as st
import LangChain_helper as lh
st.title('Restaurant name Generator')
cuisine= st.sidebar.selectbox("Pick a Cuisine",("Pakistani","Italian","Arabic","Mexican","American"))


if cuisine:
    response=lh.generate_restaurantname_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items=response['menuitems'].strip().split(',')
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)



