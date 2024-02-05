import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import os


def askCsv(smartDf, df):
    prompt = st.text_area("Ask your csv file : ")
    if st.button("Submit"):
        if prompt:
            with st.spinner("Generating response ..."):
                st.write(smartDf.chat(prompt))
        else:
            st.warning("Please enter a Prompt. ")


def main():
    load_dotenv()
    openAiToken = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(api_token=openAiToken)
    st.title("csv-analyzer")
    uploaded_file = st.file_uploader("csv you want to analyze", type="csv", key="csv_uploader")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        smartDf = SmartDataframe(df, config={"llm": llm})
        st.write(df.head(10))
        askCsv(smartDf, df)


if __name__ == "__main__":
    main()