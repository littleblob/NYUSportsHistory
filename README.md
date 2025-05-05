# NYUSportsHistory
Data Viz Files for NYU Sports History Project

This project visualizes the coverage of men's and women's sports in NYU’s Washington Square Campus student newspaper, the Washington Square Bulletin, subsequently the Washington Square News, beginning im 1933. Using Plotly, it produces an interactive bubble chart showing how often various sports were mentioned over time for both men and women, aggregated by month.

Overview

📅 Date Range: 1933 – Present (aggregated monthly)

🧑‍🤝‍🧑 Gender Split: Separate plots for men's and women's sports

🔵 Bubble Size: Number of mentions per sport, per month

🎨 Color-Coded: Each sport gets a unique color

🖼️ Branding: Styled with NYU colors and includes NYU logo

 💾 Outputs a shareable HTML file (`chart.html`)

📁 File Structure

├── Data/
│   ├── WSB_MenSportAnalysis_viz.csv
│   └── WSB_WomenSportAnalysis_viz.csv
├── NYU_Short_RGB_White.png
├── chart.html
└── sports_coverage_visualization.py

Setup
1. Clone the repository
```bash   
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

This project visualizes the frequency of mentions for men's and women's sports in NYU's Washington Square Campus student newspaper beginning in 1933, based on monthly aggregation of article mentions. The output is a dynamic, interactive bubble chart created with Plotly.

🏆 Features

- 📅 Aggregates sports coverage by **month**
- 🧑‍🤝‍🧑 Separate visual tracks for **Men’s** and **Women’s** sports
- 🟣 Color-coded bubbles sized by frequency of mention
- 🖼️ Embeds NYU logo and customized legends
-

🛠️ Technologies Used

- Python(Pandas, Plotly)
- Plotly Express & Graph Objects**
- Base64 Encoding** (for logo embedding)
- **CSV data input** (historical sports coverage data)



📊 Inputs

- `WSB_MenSportAnalysis_viz.csv`: Dataset containing mentions of men’s sports.
- `WSB_WomenSportAnalysis_viz.csv`: Dataset containing mentions of women’s sports.
- Each CSV must include a date column (`Date of mention` or `Date of Mention`) and a `Sport` column.

📤 Output

- `chart.html`: A fully interactive HTML file showing two vertically stacked bubble charts, one for men's sports and one for women's, color-coded and labeled with custom legends.

🚀 How to Run

1. Install dependencies

pip install pandas plotly


2. Run the script

python wsbdataviz.py


3. View the output

Open `chart.html` in any web browser.

🎨 Customization

- 🎨 Modify color palettes using [`plotly.colors.qualitative`](https://plotly.com/python/discrete-color/)
- 🧩 Adjust chart size, legends, layout, and font in the script
- 📅 Extend for weekly/daily aggregations if desired

📜 License

This project is for academic and visualization purposes and not for commercial use. Contact the project maintainer for inquiries about distribution or reuse.

