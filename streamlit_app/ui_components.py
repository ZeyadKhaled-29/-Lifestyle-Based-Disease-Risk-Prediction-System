import streamlit as st
import plotly.graph_objects as go

def info_box(title, text, icon="ℹ️"):
    st.markdown(f"""
    <div style="
        background-color:#ffffff;
        padding:15px;
        border-radius:10px;
        margin-bottom:15px;
        border-left:5px solid #4c6ef5;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e1e4e8;
    ">
        <h4 style="margin-top:0px; margin-bottom:5px; color:#1f2d3d;">{icon} {title}</h4>
        <p style="margin:0px; color:#3c4858; font-size: 14px;">{text}</p>
    </div>
    """, unsafe_allow_html=True)

def create_gauge_chart(probability, disease_name):
    """Creates a beautiful speedometer chart for risk probability."""
    # Determine color based on risk (Green -> Yellow -> Red)
    if probability < 0.3:
        color = "#00cc96" # Green
    elif probability < 0.7:
        color = "#FFA15A" # Orange
    else:
        color = "#EF553B" # Red

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = probability * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"{disease_name} Risk", 'font': {'size': 20}},
        number = {'suffix': "%", 'font': {'size': 40, 'color': color}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#e1e4e8",
            'steps': [
                {'range': [0, 30], 'color': "rgba(0, 204, 150, 0.1)"},
                {'range': [30, 70], 'color': "rgba(255, 161, 90, 0.1)"},
                {'range': [70, 100], 'color': "rgba(239, 85, 59, 0.1)"}
            ],
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    return fig