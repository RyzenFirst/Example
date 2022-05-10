import streamlit as st
import pandas as pd
import numpy as np
def print_hello(name='World'):
    st.write(f"## Hello, {name}")
print_hello()

df=pd.DataFrame(dict(x=[1,2,3,4], y=[4,3,2,1]))
st.line_chart(df)

#if __name__=='__main__':s
#    print_hello()

