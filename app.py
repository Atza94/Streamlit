import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

st.title("Scrocco anch'io! :meat_on_bone:")
st.header(':red[La nascita di una rivoluzione!]')
st.subheader('_Quanto è importante scroccare i pasti nella società neo-capitalista?_')

img=Image.open("assets/uomofucile.jpg")
st.image(img)
st.caption("La reazione del borghese medio quando provi a prendergli le briciole di cornetto dal piatto al bar :broken_heart:")

df=pd.DataFrame(
    np.random.rand(31,6)
)

#base plot stream e matplot
x=[1,2,3,4,5]
y=[1,2,3,4,5]

red=plt.figure()
plt.plot(x,y)
st.pyplot(red)

#radio, checkbox, audio, foto 



