import streamlit as st
from Cohere_Hacakathon import *

#Headings for Web Application
st.title('💻 Twitter Helper!')
st.subheader('Helps you increase your tweets engagement with your audience')

flavor_text = """
 Are you a Influncer, Content Creator or even a daily user on Twitter, want to boost your traffic and reach your audience effictivily,
 then this app is made for you to reach your maximum potential
 You here have 2 options available and one is still under development

 1. Type your tweet that you want to share with your followers! 
 2. Then, Our application uses a finetuned model traiend on thousands of words to provide you with Hashtags suggestions and Acoounts to mention for your next tweet.\n
 3. Take a few Hashtags, throw them into your tweet, and repeat! Enjoy! \n
 
 """

with st.expander("Click here for Instructions"):
     st.markdown(flavor_text)

background_info = """
This app was made with :heart: by Ahmed Hossam and Yasien Essam. 

Two biomedical engineers with an entrepreneurial spirit and a burning desire to make cool stuff with NLP and generative models! 

The classification and generation tasks are done using [Cohere](https://cohere.ai), as this app is a submission to a 
hackathon hosted by [lablab.ai](https://lablab.ai). Thanks to both for the resources to build this cool app!
"""

with st.expander("How was this made?"):
    st.markdown(background_info)


#Picking what NLP task you want to do
option = st.selectbox('Category Service',("Generate Hashtags", "Tweet Summrization","Twitter Handle")) #option is stored in this variable

if option == "Generate Hashtags":
    input = st.text_area('Enter text', height=100)
    if st.button('Generate !'):
        with st.container():
            hashtag_col, mention_col = st.columns(2)
            with hashtag_col:
                output = get_hashtag(input)
                Hashtag = '<p style="font-family:Courier; color:#9AEBA3; font-size: 30px;">Hashtag</p>'
                st.markdown(Hashtag, unsafe_allow_html=True)
                for out in output:
                    st.text(str(out))

            with mention_col:
                Mentions = '<p style="font-family:Courier; color:#9AEBA3; font-size: 30px;">Mentions</p>'
                st.markdown(Mentions, unsafe_allow_html=True)
                st.text(get_mention(output[0]))     

    else:
        st.write('Waiting for your input')

elif option == "Tweet Summrization":
   input = st.text_area('Enter text', height=100)
   if st.button('Summarize !'):
        summary = f'<p style="font-family:SansSerif; color:#9AEBA3; font-size: 20px;">{text_summary(input)}</p>'
        st.markdown(summary,unsafe_allow_html=True)

elif option == "Twitter Handle":
    st.subheader('Future Implementation Awaiting Twitter API Approval !')