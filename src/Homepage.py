import streamlit as st

def main():
    st.set_page_config(
        page_title="Multipage App",
        page_icon=":100:",
    )

    st.title("Welcome to gpt-fun!")
    st.header("Unlocking Possibilities with AI")
    # st.write("Here you can experiment with the power of cutting-edge AI technology. This platform offers a range of diverse projects, each harnessing the capabilities of GPT-related innovations. Whether you're looking to get a medical diagnosis based on your symptomes, communicate with your pdfs, or even talk with a youtube video, we have you covered.")
    st.markdown(
        """
        Here you can experiment with the power of cutting-edge AI technology. This platform offers a range of diverse projects, each harnessing the capabilities of GPT-related innovations. Whether you're looking to get a medical diagnosis based on your symptomes, communicate with your pdfs, or even talk with a youtube video, we have you covered.

        **How It Works**

        1. **Explore Projects**: Navigate through the sidebar to discover an array of projects, each designed for specific AI-related tasks. These projects were created with the purpose of making your life easier.

        2. **Project Details**: Click on a project to learn more about its unique functionality. We've provided comprehensive descriptions to ensure you understand what each project offers.

        3. **Customization**: Many projects feature a central text box, allowing you to input specifications, questions, or instructions. 

        4. **Enhance with documents**: Certain projects offer even more possibilities. When you click on specific projects, you'll find additional options in the sidebar. For example, you may input a YouTube video URL to leverage AI's capabilities to talk with your youtube videos.

        5. **Results at Your Fingertips**: These AI-driven projects swiftly process your inputs and provide outputs that are both impressive and highly valuable. Whether you're a content creator, a researcher, or anyone seeking AI-powered solutions, you're bound to find what you need.

        Are you ready to harness the power of AI like never before? Explore these projects, unleash your creativity, and discover the potential that AI brings to your work. 
        """
    )
    
    st.sidebar.success("Select a page above.")

if __name__=="__main__":
    main()