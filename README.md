# NYUSportsHistory
Data Viz Files for NYU Sports History Project

This project visualizes the coverage of men's and women's sports in NYU’s Washington Square Campus student newspaper, the Washington Square Bulletin, subsequently the Washington Square News, beginning im 1933. Using Plotly, it produces an interactive bubble chart showing how often various sports were mentioned over time for both men and women, aggregated by month.

Overview

📅 Date Range: 1933 – Present (aggregated monthly)

🧑‍🤝‍🧑 Gender Split: Separate plots for men's and women's sports

🔵 Bubble Size: Corresponds to number of mentions per sport per month

🎨 Color-Coded: Each sport gets a unique color

🖼️ Branding: Styled with NYU colors and includes NYU logo

 💾 Outputs a shareable HTML file (`chart.html`)

## 🛠️ Technologies Used

- **Python** (Pandas, Plotly)
- **Plotly Express & Graph Objects**
- **Base64 Encoding** (for logo embedding)
- **CSV data input** (historical sports coverage data)

## 📁 File Structure

```
project/
├── Data/
│   ├── WSB_MenSportAnalysis_viz.csv
│   └── WSB_WomenSportAnalysis_viz.csv
├── NYU_Short_RGB_White.png
├── chart.html
└── sports_coverage_visualization.py
```

## 🚀 How to Run

### 1. Clone the repository
```bash   
git clone https://github.com/littleblob/NYUSportsHistory.git
cd NYUSportsHistory
```

### 2. Install dependencies

```bash
pip install pandas plotly
```

### 3. Run the script

```bash
python sports_coverage_visualization.py
```

### 4. View the output

Open `chart.html` in any web browser.

## 📊 Inputs
1. WSB_MenSportAnalysis_viz.csv: Contains columns such as Sport and Date of mention for men's sports. Also contains additional qualitative data such as placement of mention, intersections with other stories of interest, and notes.
2. WSB_WomenSportAnalysis_viz.csv: Contains columns such as Sport and Date of Mention for women's sports. Also contains additional qualitative data such as placement of mention, intersections with other stories of interest, and notes.
3. Data is grouped by sport and by month using Pandas' crosstab and PeriodIndex.
4. Each CSV must include a date column (`Date of mention` or `Date of Mention`) and a `Sport` column.

## 📤 Output
1. chart.html: An interactive HTML file containing the final visualization.
2. Two vertically stacked bubble charts for men's and women's sports, color-coded and labeled by sport.
3. Legends rendered as HTML annotations within the chart.
4. Embedded NYU logo at the bottom right.

## 🎨 Customization

- 🎨 Modify color palettes using [`plotly.colors.qualitative`](https://plotly.com/python/discrete-color/)
- 🧩 Adjust chart size, legends, layout, and font in the script
- 📅 Extend for weekly/daily aggregations if desired

## 📜 License

This project is for academic and visualization purposes and not for commercial use. Contact the project maintainer for inquiries about distribution or reuse.


