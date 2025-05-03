import streamlit as st
import pandas as pd
from datetime import datetime

FILENAME = "作業記録.csv"

st.title("🌾 農作業記録アプリ")

# 入力フォーム
date = st.date_input("日付", datetime.today())
crop = st.text_input("作物名")
task = st.text_input("作業内容")
duration = st.number_input("作業時間（分）", min_value=0)
memo = st.text_area("メモ")

if st.button("✅ 記録を保存"):
    new_record = pd.DataFrame([[date, crop, task, duration, memo]],
                              columns=["日付", "作物", "作業内容", "作業時間", "メモ"])

    try:
        df = pd.read_csv(FILENAME)
        df = pd.concat([df, new_record], ignore_index=True)
    except FileNotFoundError:
        df = new_record

    df.to_csv(FILENAME, index=False)
    st.success("記録を保存しました！")

# 記録の一覧表示
st.subheader("📋 記録一覧")
try:
    df = pd.read_csv(FILENAME)
    st.dataframe(df)
except FileNotFoundError:
    st.info("まだ記録はありません。")
