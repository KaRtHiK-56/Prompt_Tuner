import streamlit as st
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Tuner", page_icon="🤖")
with st.sidebar:
    st.text("PROMPT TUNER")
    st.image(r"C:\Users\Devadarsan\Desktop\Karthik_projects\Prompt_Tuner\tuner.jpg")

st.title("🦜 LLM Prompt Tuner 🛠️ ")
st.text("Prompt tuner helps in tuning your propmt for specific usecases.")
text = st.text_area("Please enter your prompt here:")
configuration = st.selectbox(
    "Please select the configuration of the prompt to be designed:",
    ("Proper Wordings", "Accuracy", "Improved performance"),
)


def prompt(text, configuration):
    
    """
    this fucntion is used to create the redefined version if the prompt entered by the user.
    it takes 2 parameters text and configuration and uses that to create a redefined prompt using the LLM.
    
    """

    print("The user input is ", text)
    print("The configuration is ", configuration)
    prompt = """
**Objective:**
Transform the manually entered user prompt {text} into a more refined and effective prompt using {configuration} style.

**Instructions:**

1. **Analyze the User Prompt {text}:**
   - Review the manually entered user prompt{text} using {configuration} style.

2. **Extract Core Intent:**
   - Determine the main purpose or goal of the prompt. What is the user seeking to achieve or learn?

3. **Identify Context and Details:**
   - Note any relevant background information or specific details that should be included to provide clarity.

4. **Clarify and Specify:**
   - Adjust the prompt to remove any ambiguities. Be as specific as possible to focus on the desired outcome.

5. **Enhance Precision and Language:**
   - Refine the wording to make the prompt clear, concise, and aligned with the intended purpose.

6. **Formulate the Refined Prompt:**
   - Combine the clarified intent, context, and precise language into a polished prompt.

---

**Template Example:**

**User Input:**
- [Enter the manually entered user prompt here]

**Refined Prompt:**
1. **Core Intent:** [Describe the main goal or question]
2. **Context:** [Include relevant background or specifics]
3. **Desired Output:** [Specify the expected type of response]
4. **Clarification:** [Eliminate any vague terms or ambiguities]

**Final Refined Prompt:**

**Refinement:** [Adjust the wording for clarity and precision]

"""

    llm = Ollama(model="llama3", temperature=0)
    prompt = PromptTemplate.from_template(template=prompt)
    prompt = prompt.format(text=text, configuration=configuration)
    response = llm(prompt)
    return response


if text is not None:
    submit = st.button("Tune Prompt")

    if submit:
        st.write(prompt(text, configuration))
