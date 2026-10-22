import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="The Best Company",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

team = pd.read_csv(BASE_DIR / "004 data.csv")
topics = pd.read_csv(BASE_DIR / "004 topics.csv")

# Team display order
team_order = [
    "john smith",
    "tarit agarkar",
    "amar bhat",
    "alberto lock",
    "nadiya conwell",
    "nalin jindal",
    "kudret fanpe",
    "will stacy",
    "chandresh bhat",
    "adley patel",
    "laura mendez",
    "batsa kionvoi"
]

team["full_name"] = (
    team["first name"].str.strip().str.lower()
    + " "
    + team["last name"].str.strip().str.lower()
)

team["display_order"] = team["full_name"].map(
    {name: i for i, name in enumerate(team_order)}
)

team = team.sort_values("display_order", na_position="last")

# CSS styling
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff;
    }

    [data-testid="stSidebar"] {
        background-color: #e8edf3;
    }

    .company-title {
        font-size: 32px;
        font-weight: bold;
        color: #26364b;
        margin-bottom: 12px;
    }

    .company-description {
        font-size: 14px;
        line-height: 1.8;
        color: #344256;
        margin-bottom: 25px;
    }

    .team-title {
        font-size: 25px;
        font-weight: bold;
        color: #26364b;
        margin-bottom: 20px;
    }

    .member-name {
        font-size: 20px;
        font-weight: bold;
        color: #26364b;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .member-role {
        font-size: 13px;
        color: #344256;
        margin-bottom: 15px;
    }

    .team-card {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }

    div[data-testid="stImage"] img {
        object-fit: cover;
    }
</style>
""", unsafe_allow_html=True)


# Sidebar navigation
st.sidebar.title("☰ Menu")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Contact Us"],
    label_visibility="collapsed"
)


# Home page
# Home page
if page == "Home":

    st.markdown(
        '<div class="company-title">The Best Company</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="company-description">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat
        nulla pariatur. Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="team-title">♧ Our Team</div>',
        unsafe_allow_html=True
    )

    # Display team members in 4 rows of 3
    members = team.to_dict("records")

    for start in range(0, len(members), 3):
        cols = st.columns(3)

        for index, (col, member) in enumerate(
            zip(cols, members[start:start + 3]),
            start=start
        ):
            with col:
                name = (
                    f"{str(member['first name']).strip().title()} "
                    f"{str(member['last name']).strip().title()}"
                )

                st.markdown(
                    f'<div class="member-name">{name}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="member-role">{member["role"]}</div>',
                    unsafe_allow_html=True
                )

                image_number = index + 1
                image_path = BASE_DIR / f"{image_number}.png"

                if image_path.exists():
                    st.image(str(image_path), width=180)
                else:
                    st.warning(f"Image not found: {image_number}.png")

# Contact Us page
elif page == "Contact Us":

    st.markdown(
        '<div class="company-title">Contact Us</div>',
        unsafe_allow_html=True
    )

    st.write("Get in touch with our team.")

    with st.form("contact_form"):

        email = st.text_input("Your Email")

        topic = st.selectbox(
            "Topic",
            topics["topic"].dropna().tolist()
        )

        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if email and message:
                st.success("Your message has been submitted!")
            else:
                st.error("Please fill in all fields.")
                    # Contact Us page
elif page == "Contact Us":
                    st.markdown(
                        '<div class="company-title">Contact Us</div>',
                        unsafe_allow_html=True
                    )

                    st.write("Get in touch with our team.")

                    with st.form("contact_form"):

                        name = st.text_input("Your Name")

                        email = st.text_input("Your Email")

                        topic = st.selectbox(
                            "Topic",
                            topics["topic"].dropna().tolist()
                        )

                        message = st.text_area("Your Message")

                        submitted = st.form_submit_button("Submit")

                        if submitted:
                            if name and email and message:
                                st.success("Your message has been submitted!")
                            else:
                                st.error("Please fill in all fields.")
