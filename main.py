import streamlit as st
import openai
import os

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


if __name__ == "__main__":
    st.write("Hello")
    st.write("OK")
    st.write("how about this?")

    api_key_input = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="Paste your OpenAI API key here (sk-...)",
        help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
        value=os.environ.get("OPENAI_API_KEY", None)
        or st.session_state.get("OPENAI_API_KEY", ""),
    )

    st.session_state["OPENAI_API_KEY"] = api_key_input


    openai_api_key = st.session_state.get("OPENAI_API_KEY")

    if not openai_api_key:
        st.warning(
            "Enter your OpenAI API key in the sidebar. You can get a key at"
            " https://platform.openai.com/account/api-keys."
        )


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

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": "Hello"}]
        )

    st.write(response)