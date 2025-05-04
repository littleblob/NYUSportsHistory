# NYUSportsHistory
Data Viz Files for NYU Sports History Project

This project visualizes the coverage of men's and women's sports in NYU’s Washington Square Campus student newspaper, the Washington Square Bulletin, subsequently the Washington Square News, beginning im 1933. Using Plotly, it produces an interactive bubble chart showing how often various sports were mentioned over time for both men and women, aggregated by month.

Overview

📅 Date Range: 1933 – Present (aggregated monthly)

🧑‍🤝‍🧑 Gender Split: Separate plots for men's and women's sports

🔵 Bubble Size: Number of mentions per sport, per month

🎨 Color-Coded: Each sport gets a unique color

🖼️ Branding: Styled with NYU colors and includes NYU logo

Project Structure:
DataViz
├── Data/
│   ├── WSB_MenSportAnalysis_viz.csv
│   └── WSB_WomenSportAnalysis_viz.csv
├── NYU_Short_RGB_White.png
├── chart.html
└── wsbdataviz.py

Setup
1. Clone the repository
git clone https://github.com/littleblob/NYUSportsHistory.git
cd NYUSportsHistory
2. Install dependencies
Ensure you have Python 3.7+ and install required packages:
pip install pandas plotly

Data
1. WSB_MenSportAnalysis_viz.csv: Contains columns such as Sport and Date of mention for men's sports. Also contains additional qualitative data such as placement of mention, intersections with other stories of interest, and notes.
2. WSB_WomenSportAnalysis_viz.csv: Contains columns such as Sport and Date of Mention for women's sports. Also contains additional qualitative data such as placement of mention, intersections with other stories of interest, and notes.
3. Data is grouped by sport and by month using Pandas' crosstab and PeriodIndex.

Output
1. chart.html: An interactive HTML file containing the final visualization.
2. Two vertically stacked bubble charts for men's and women's sports.
3. Legends rendered as HTML annotations within the chart.
4. Embedded NYU logo at the bottom right.


