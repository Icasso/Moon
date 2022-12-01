import asyncio

import streamlit as st

from Service.IndexService import index_price
from config import load_config

load_config()

st.title("Project - Moon")

status = st.empty()
symbol = st.selectbox('Currency', ("BTC", "ETH", "SOL"))

asyncio.run(index_price(symbol))
