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
- **Plotly, Plotly Express, Subplots, & Graph Objects**
- **Base64 Encoding** (for logo embedding)
- **CSV data input** (historical sports coverage data)
- **Visual Studio Code or comparable product** 

## 📁 File Structure

```
project/
├── Data/
│   ├── WSB_MenSportAnalysis_viz.csv
│   └── WSB_WomenSportAnalysis_viz.csv
├── NYU_Short_RGB_White.png
├── chart.html
└── wsbdataviz.py.py
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
python wsbdataviz.py
```

### 4. View the output

Open `chart.html` in any web browser.

## 📊 Inputs
1. WSB_MenSportAnalysis_viz.csv: Contains columns such as Sport and Date of mention for men's sports. Also contains additional qualitative data such as placement of mention, intersections with other stories of interest, and notes.
2. WSB_WomenSportAnalysis_viz.csv: Contains columns such as Sport and Date of Mention for women's sports. Also contains additional qualitative data such as placement of mention, intersections with other stories of interest, and notes.
3. Data is grouped by sport and by month using Pandas' crosstab and PeriodIndex.
4. Each CSV must include a date column (`Date of mention` or `Date of Mention`) and a `Sport` column.
5. The source data file for Washington Square newspaper sports mentions currently lives in shared Dual Degree Intern Google drive. To run updates to the visualization as new data is collected, simply save each sheet to the csv files enumerated in Inputs 1 and 2. If for any reason, you decide to change the names of the csv files, you must also change them in the code on lines 13 and 14 where the data frame is created. The name of the source file on the Google drive should not effect this. 

## 📤 Output
1. chart.html: An interactive HTML file containing the final visualization.
2. Two vertically stacked bubble charts for men's and women's sports, color-coded and labeled by sport.
3. Legends rendered as HTML annotations within the chart.
4. Embedded NYU logo at the bottom right.

## 🎨 Customization

- 🎨 Modify color palettes using [`plotly.colors.qualitative`](https://plotly.com/python/discrete-color/). Color is set for each chart on line 32.
- 🧩 Adjust chart size, legends, layout, and font by modifying the properties delineated in the fig.update functions beginning at line 128.
- 📅 Play with different aggregations by Month or Year adjusting the parameters of 'freq =' on lines 21 and 26.
- 🎓 Change out the logo by adding a new .PNG file to line 161. Please note the the file must be .PNG in order to properly convert to base64 using this method. Other file types will require a more complex workaround.

## 📜 License

This project is for academic and visualization purposes and not for commercial use. Contact the project maintainer for inquiries about distribution or reuse.


