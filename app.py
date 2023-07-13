import streamlit as st
import base64
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

image_path = Image.open('FMCC/img_2.jpg')
 # --- HIDE STREAMLIT STYLE ---


st.set_page_config(page_title="FMCC", page_icon="⚧",layout="wide")
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

selected = option_menu(None, ["Home", "Give a Feedback"], 
    icons=['house', 'cloud-upload'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#9575DE"},
        "nav-link-selected": {"background-color": "#6554AF"},
    }
)

if selected == "Home":
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()


    img = get_img_as_base64("FMCC/woman.jpg")

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: center;
    background-repeat: repeat;
    background-attachment: local;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)



    background_color = "#E2D1F9"
    opacity = 0.8
    text_color = "#317773"
    textalign ="center"
    border_radius = 2
    def html_heading(text, background_color, opacity, text_color, font_size, border_radius):
        html_code = f'''
            <h1 style="background-color:{background_color}; opacity:{opacity}; color:{text_color};
            font-size:{font_size}px; border-radius:{border_radius}px;text-align:{textalign};">{text}</h1>
        '''
        return html_code


    col1,col2 = st.columns ([0.6,0.4],gap="small")
    with col1:
        heading_text = "  🧶 FMCC"
        font_size = 75
        html_code = html_heading(heading_text, background_color, opacity, text_color, font_size, border_radius)
        st.markdown(html_code, unsafe_allow_html=True)

        font_size = 30
        heading_text = "  Sustainable style, inclusive expression"
        html_code = html_heading(heading_text, background_color, opacity, text_color, font_size, border_radius)
        st.markdown(html_code, unsafe_allow_html=True)

        font_size = 25
        heading_text = "  Hello there! Your voice matters to Feed my colourful corner."
        html_code = html_heading(heading_text, background_color, opacity, text_color, font_size, border_radius)
        st.markdown(html_code, unsafe_allow_html=True)

        font_size = 25
        textalign ="center"
        heading_text = "  Embrace a world where sustainability meets self-expression."
        html_code = html_heading(heading_text, background_color, opacity, text_color, font_size, border_radius)
        st.markdown(html_code, unsafe_allow_html=True)

        font_size = 18
        textalign ="center"
        heading_text = """ FMCC's mission is to advocate for a gender-neutral, sustainable society. We gather feedback and amplify voices, urging brands to allocate dedicated sections for gender-neutral products in stores. Let's collaborate in shaping a diverse marketplace where individuals can express themselves freely and sustainably."""
        html_code = html_heading(heading_text, background_color, opacity, text_color, font_size, border_radius)
        st.markdown(html_code, unsafe_allow_html=True)

        font_size = 20
        textalign ="center"
        heading_text = "Inspire change, voice your feedback with pride."
        html_code = html_heading(heading_text, background_color, opacity, text_color, font_size, border_radius)
        st.markdown(html_code, unsafe_allow_html=True)
    
    st.write("[Learn More About Gender Neutral Products >](https://ethicalunicorn.com/2019/02/13/why-gender-neutral-clothing-is-the-future-of-sustainable-fashion/https://ethicalunicorn.com/2019/02/13/why-gender-neutral-clothing-is-the-future-of-sustainable-fashion/)")
    st.write("---")


if selected == "Give a Feedback":
    background_color = "#9575DE"
    opacity = 0.8
    text_color = "#2B2730"
    textalign ="center"
    border_radius = 2
    font_size = 20
    heading_text = "Unveiling diversity: Supporting gender neutrality."
    def html_heading(text, background_color, opacity, text_color, font_size, border_radius):
        html_code = f'''
            <h1 style="background-color:{background_color}; opacity:{opacity}; color:{text_color};
            font-size:{font_size}px; border-radius:{border_radius}px;text-align:{textalign};">{text}</h1>
        '''
        return html_code
    html_code = html_heading(heading_text, background_color, opacity, text_color, font_size, border_radius)
    #st.markdown(html_code, unsafe_allow_html=True)
    with st.container():
        image_column, text_column = st.columns((0.4, 0.6))
    with image_column:
        heading_text = "Unveiling diversity: Supporting gender neutrality."
        st.markdown(html_code, unsafe_allow_html=True)
        st.image(image_path)
    with text_column:
        with st.container():
            #st.title("Share your Views")
            with st.form(key='Personal_Details',clear_on_submit=True):

                with st.expander("Add Personal Details",expanded=True):
                    col1,col2,col3 = st.columns([1,1,1])
                    with col1:
                        Your_name = st.text_input("Your Name",placeholder="Type your Name here",key=str)
                    with col2:
                        Your_Phone = st.text_input("Phone Number",placeholder="Add your contact",key=int)
                    with col3:
                        Your_Email = st.text_input("Email_ID",placeholder="Type your Email")

                with st.expander("Add Brand Details",expanded=True):
                    col1,col2= st.columns([1,1])
                    with col1:
                        Select_type =st.selectbox('Select Type of Product', options=["Topwear","Bottomwear","Accessories","Footwear","Others"])
                        Rating =st.selectbox('Product Rating:star2:', options=["1","2","3","4","5"])
                    with col2:
                        options = ["Zara","H&M","AND","Forever 21","Mango","Vero Moda","Allen Solly",
                                    "Van Heusen","Levi's","Tommy Hilfiger","Marks & Spencer","Global Desi",
                                    "Biba","Max Fashion","Pantaloons","Lifestyle","Shoppers Stop","Central",
                                    "Westside","Max Fashion","Reliance Trends","Bata","Adidas","Nike","Reebok","Puma",
                                    "Woodland","Skechers","Red Chief","Liberty Shoes","Other"]
                        selected_option = st.selectbox("Select your Brand",[None]+ options,help="Unable to find your Brand Select Others and Type your Brand")
                        if selected_option == "Other":
                                other_option = st.text_input("Enter your custom option")
                        if selected_option == "Other":
                                st.write("You have Selected: " + other_option)
                        elif selected_option is not None:
                            st.write("You have selected: " + selected_option)
                        Invoice = st.text_input("Invoice number",placeholder="Add your Invoice Details")
                    
                with st.expander("Add your Review",expanded=True):
                     st.caption('I hereby declare my support for gender neutrality my plea to the brand to establish a designated section for gender neutral products in their stores. By embracing inclusivity and sustainability, the brand commitment to inclusivity fosters an expressive shopping experience, contributing to a more sustainable society.')
                     support =st.radio('', options=['Agree', 'Disagree'], horizontal=True)
                     Feedback = st.text_area("Write your Review",max_chars=100,placeholder="Share your Review")
                     submit_feedback  =st.form_submit_button("Submit")
                if submit_feedback:
                    st.success("Hello {},Thank You for Your Feedback".format(Your_name)) 
				
                

                        
        #st.subheader("How To Add A Contact Form To Your Streamlit App")
        
      


   
    



 
    
