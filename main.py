import streamlit as st
import openai
import os
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)



# @st.cache_data(show_spinner=False)
# def is_open_ai_key_valid(openai_api_key) -> bool:
#     if not openai_api_key:
#         st.error("Please enter your OpenAI API key in the sidebar!")
#         return False
#     try:
#         openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": "test"}],
#             api_key=openai_api_key,
#         )
#     except Exception as e:
#         st.error(f"{e.__class__.__name__}: {e}")
#         logger.error(f"{e.__class__.__name__}: {e}")
#         return False
#     return True

def load_api():
    api_key_input = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="Paste your OpenAI API key here (sk-...)",
        help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
        value=os.environ.get("OPENAI_API_KEY", None)
        or st.session_state.get("OPENAI_API_KEY", ""),
    )
    btn = st.button("Add")
    if btn:
        st.session_state["OPENAI_API_KEY"] = api_key_input

if __name__ == "__main__":
    st.write("Hello")
    st.write("OK")
    st.write("how about this?")

    load_api()

    openai_api_key = st.session_state.get("OPENAI_API_KEY")

    if not openai_api_key:
        st.warning(
            "Enter your OpenAI API key in the sidebar. You can get a key at"
            " https://platform.openai.com/account/api-keys."
        )
    else:
        chat = ChatOpenAI(openai_api_key = openai_api_key)

        # llm = OpenAI()

        template = "tanslates {input_language} to {output_language}"
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = "{text}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

        chain = LLMChain(llm=chat, prompt=chat_prompt)
        res = chain.run(input_language="English", output_language="Korean", text = "I love programming.")
        st.write(res)
    # else:
    #     openai.api_key = openai_api_key

    # uploaded_file = st.file_uploader(
    #     "Upload a pdf, docx, or txt file",
    #     type=["pdf", "docx", "txt"],
    #     help="Scanned documents are not supported yet!",
    # )

    # if not uploaded_file:
    #     st.stop()

    # try:
    #     file = read_file(uploaded_file)
    # except Exception as e:
    #     display_file_read_error(e)

    # chunked_file = chunk_file(file, chunk_size=300, chunk_overlap=0)

    # if not is_file_valid(file):
    #     st.stop()


    # if not is_open_ai_key_valid(openai_api_key):
    #     st.stop()

    # response = openai.ChatCompletion.create(
    #     model = "gpt-3.5-turbo",
    #     messages = [{"role": "user", "content": "Hello"}]
    #     )

    # st.write(response)

    