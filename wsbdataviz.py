import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly
from plotly.subplots import make_subplots
import plotly.colors
import base64
import plotly.io as pio

pd.options.plotting.backend = "plotly"

#Create DataFrames
MensSports = pd.read_csv("Data/WSB_MenSportAnalysis_viz.csv")
WomensSports = pd.read_csv("Data/WSB_WomenSportAnalysis_viz.csv")

# Format the dates as datetime
MensSports["Date of mention"] = pd.to_datetime(MensSports["Date of mention"])
WomensSports["Date of mention"] = pd.to_datetime(WomensSports["Date of Mention"])

# Aggregate mentions by month
MSout = pd.crosstab(MensSports['Sport'], pd.PeriodIndex(MensSports['Date of mention'], freq='M')) 
MSNew = MSout.transpose()  # Transpose data to display by sport
MSNew.index = MSNew.index.to_timestamp()  # Convert PeriodIndex to Timestamp for Plotly
MSNew["date"] = MSNew.index  # Keep a column version of date for x-axis

WSout = pd.crosstab(WomensSports['Sport'], pd.PeriodIndex(WomensSports['Date of Mention'], freq='M'))
WSNew = WSout.transpose().to_timestamp()
WSNew["date"] = WSNew.index

# Get a list of colors (can handle 10–20+ sports)
mens_colors = plotly.colors.qualitative.Bold
womens_colors = plotly.colors.qualitative.Bold

# Map each sport to a unique color
men_sports = [col for col in MSNew.columns if col != 'date']
women_sports = [col for col in WSNew.columns if col != 'date']

# Set up color maps (use different color sets for each subplot)
men_color_map = {sport: mens_colors[i % len(mens_colors)] for i, sport in enumerate(men_sports)}
women_color_map = {sport: womens_colors[i % len(womens_colors)] for i, sport in enumerate(women_sports)}

# Global sizeref (so sizes scale well)
global_men_max = MSNew[men_sports].max().max()
global_women_max = MSNew[men_sports].max().max()

men_sizeref = 2. * global_men_max / (40.**2)
women_sizeref = 2. * global_women_max / (40.**2)


# Create the scatterplot
fig = go.Figure()

# Create subplots

fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    subplot_titles=("Men's Sports Coverage", "Women's Sports Coverage"))

# Men's sports bubble plot
for sport in men_sports:
      # Coerce all values to numeric, replace NaNs with 0, ensure consistent type
    size_vals = pd.to_numeric(MSNew[sport], errors='coerce').fillna(0)
    mask = size_vals > 0
    filtered_dates = MSNew.loc[mask, "date"]
    filtered_sizes = size_vals[mask]

    fig.add_trace(
        go.Scatter(
            x=filtered_dates,
            y=[sport] * len(filtered_dates),
            mode='markers',
            name=sport,
            marker=dict(
                # size=size_vals,
                size=filtered_sizes,
                sizemode='area',
                sizeref=men_sizeref,
                sizemin=4,
                color=men_color_map[sport],
                line=dict(width=0.5, color='gray')
            ),
            customdata=list(zip([sport] * len(filtered_dates), filtered_sizes)),
            hovertemplate="%{x|%b %Y}<br>Sport: %{customdata[0]}<br>Mentions: %{customdata[1]}<extra></extra>"
        ),
        row=1, col=1
    )

# Women's sports bubble plot
for sport in women_sports:
      # Coerce all values to numeric, replace NaNs with 0, ensure consistent type
    size_vals = pd.to_numeric(WSNew[sport], errors='coerce').fillna(0)
    # Find valid data points with size > 0
    mask = size_vals > 0
    filtered_dates = WSNew.loc[mask, "date"]
    filtered_sizes = size_vals[mask]

    fig.add_trace(
        go.Scatter(
            # x=WSNew["date"],
            x=filtered_dates,
            # y=[sport]*len(WSNew),
            y=[sport] * len(filtered_dates),
            mode='markers',
            name=sport,
            marker=dict(
                # size=size_vals,
                size=filtered_sizes,
                sizemode='area',
                sizeref=women_sizeref,
                sizemin=4,
                color=women_color_map[sport],
                line=dict(width=0.5, color='gray')
            ),
            customdata=list(zip([sport] * len(filtered_dates), filtered_sizes)),
            hovertemplate="%{x|%b %Y}<br>Sport: %{customdata[0]}<br>Mentions: %{customdata[1]}<extra></extra>"
        ),
        row=2, col=1
    )
fig.update_layout(
    height=900,
    title_text="Sports Coverage in the Washington Square Student Newspaper from 1933 (aggregated by month)",
    showlegend=False,   
)
# format the charts
fig.update_yaxes(title_text=None, showticklabels=False, row=1, col=1, showgrid=False)
fig.update_yaxes(title_text=None, showticklabels=False, row=2, col=1, showgrid=False)
fig.update_xaxes(title_text="Date")
fig.update_xaxes(tickfont=dict(color='lavender', family='Arial'))
fig.update_xaxes(title_font=dict(color='lavender', family='Arial'))
fig.update_layout(
    autosize=True,
    margin=dict(l=160, r=195, t=120, b=120),
    plot_bgcolor='midnightblue',     # plot area background
    paper_bgcolor='midnightblue', # entire figure background
    title_font_family='Arial', 
    xaxis=dict(
        showticklabels=True,
        tickfont=dict(color='lavender', family='Arial')
    ),
)

# Formatting the title
fig.update_layout(
    title=dict(
        # Title text color
        font=dict(color='lavender', size=18),
        pad=dict(t=10, b=20)  
    )
)

# Convert NYU Logo to base64 so python can read it
with open("NYU_Short_RGB_White.png", "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode()

# Add converted image to the chart at the bottom
fig.update_layout(  
        images=[dict(
        source="data:image/png;base64," + logo_base64,
        xref="paper", yref="paper",
        x=1.15, y=-.15, # this sets the location
        sizex=0.08, sizey=0.08,   # this sets the size
        xanchor="right", yanchor="bottom", # somehow this keeps it from flying off of the page
        layer="below"
    )]
)

# Generate legends
def generate_legend_html(title, color_map):
    legend_lines = [f"<span style='font-size:10px; font-family:Arial; color:lavender'><b>{title}:</b></span><br>"]
    for sport, color in color_map.items():
        legend_lines.append(
            f"<span style='font-size:9px; font-family:Arial; color:{color}'>● {sport}</span><br>"
        )
    return ''.join(legend_lines)

# Generate the HTML legend text
men_legend_html = generate_legend_html("Men’s Sports Legend", men_color_map)
women_legend_html = generate_legend_html("Women’s Sports Legend", women_color_map)

# Add men's sports annotation for the legend
fig.add_annotation(
    text=men_legend_html,
    xref="paper", yref="paper",
    xanchor='left',
    x=1.04, y=1,
    showarrow=False,
    align="left",
    font=dict(color="white", family="NYU Perstare", size=8),
    bgcolor="rgba(0,0,0,0.5)",
    bordercolor="white",
    borderwidth=1
)

# Add women's sports annotation for the legend
fig.add_annotation(
    text=women_legend_html,
    xref="paper", yref="paper",
    xanchor='left',
    x=1.03, y=0.03,
    showarrow=False,
    align="left",
    font=dict(color="white", family="NYU Perstare", size=8),
    bgcolor="rgba(0,0,0,0.5)",
    bordercolor="white",
    borderwidth=1
)

# Format subplots
fig.update_annotations(font=dict(color='goldenrod', family='Arial'), font_size=14, borderpad=15)

# Display the chart    
fig.show()

# Write the chart to a shareable html file
fig.write_html("chart.html")

