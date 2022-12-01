import asyncio
import json

import pandas as pd
import streamlit as st

import websockets


async def index_price(symbol):
    columns = [col.empty() for col in st.columns(1)]
    async with websockets.connect("wss://ws.okx.com:8443/ws/v5/public") as websocket:
        await websocket.send(json.dumps({
            "op": "subscribe",
            "args": [
                {
                    "channel": "tickers",
                    "instId": symbol + "-USDT"
                }
            ]
        }))
        async for message in websocket:
            message_json = json.loads(message)
            for col in columns:
                await asyncio.sleep(0.1)
                if 'data' in message_json:
                    chart_data = pd.DataFrame(
                        message_json['data']
                    )
                    col.dataframe(chart_data)
