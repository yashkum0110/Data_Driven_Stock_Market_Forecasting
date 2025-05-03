# Data_Driven_Stock_Market_Forecasting
<h1 align="center">📈 Stock Forecast App</h1>

<p align="center">
  A Streamlit web application for predicting stock prices using the Prophet library.
</p>

<p align="center">
  <a href="YOUR_GITHUB_REPO_URL">
    <img src="https://img.shields.io/badge/View%20on%20GitHub-blue?logo=github" alt="GitHub Repo">
  </a>
  <a href="YOUR_STREAMLIT_APP_URL" target="_blank">
    <img src="https://img.shields.io/badge/Live%20Demo-brightgreen?logo=streamlit" alt="Streamlit App">
  </a>
</p>

<br>

<h2>✨ Key Features</h2>

<ul>
  <li><b>Stock Selection:</b> Input a stock symbol to get its prediction.</li>
  <li><b>Historical Data:</b> Downloads historical stock data from Yahoo Finance.</li>
  <li><b>Data Visualization:</b> Displays raw stock data (Open and Close prices) with an interactive chart.</li>
  <li><b>Prophet Forecasting:</b> Uses the Prophet library to predict future stock prices.</li>
  <li><b>Forecast Horizon:</b> Predict stock prices for a user-defined number of years (1 to 4).</li>
  <li><b>Forecast Visualization:</b>  Visualizes the predicted stock prices, including trend and seasonality components.</li>
  <li><b>Interactive Charts:</b> Uses Plotly for interactive visualizations.</li>
  <li><b>Error Handling:</b> Robust error handling for invalid stock symbols or data issues.</li>
</ul>

<h2>🚀 How to Run</h2>

<ol>
  <li><b>Clone the repository:</b>
    <code>git clone YOUR_GITHUB_REPO_URL</code>
  </li>
  <li><b>Navigate to the project directory:</b>
    <code>cd your_project_directory</code>
  </li>
  <li><b>Install the required dependencies:</b>
    <code>pip install -r requirements.txt</code>
  </li>
  <li><b>Run the Streamlit application:</b>
    <code>streamlit run app.py</code>
  </li>
  <li>Open your web browser and navigate to the address displayed in the terminal (usually <code>http://localhost:8501</code>).</li>
</ol>

<h2>🛠️ Technologies Used</h2>

<ul>
  <li><b>Python:</b> The primary programming language.</li>
  <li><b>Streamlit:</b>  For building the interactive web application.</li>
  <li><b>Prophet:</b>  For time series forecasting.</li>
  <li><b>Pandas:</b>  For data manipulation.</li>
  <li><b>yfinance:</b> To download historical stock data.</li>
  <li><b>Plotly:</b> For interactive data visualization.</li>
</ul>

<h2>📂 File Structure</h2>

<pre>
your_project_directory/
├── app.py           # The main Streamlit application file
├── requirements.txt # List of Python dependencies
├── README.md        # This README file
</pre>

<h2>💡 Code Explanation</h2>

<p>
  The <code>app.py</code> script creates a Streamlit application that predicts stock prices. Here's a breakdown:
</p>

<ol>
    <li><b>Imports:</b>
        <p>
            Imports necessary libraries: <code>streamlit</code>, <code>datetime</code>, <code>pandas</code>, <code>yfinance</code>, <code>prophet</code>, <code>plotly</code>.
        </p>
    </li>
    <li><b>Constants:</b>
        <p>
             Defines <code>START</code> date as '2015-01-01' and <code>TODAY</code> as the current date.
        </p>
    </li>
    <li><b>App Title and Input:</b>
        <p>
            Sets the title of the app and takes user input for the stock symbol and the number of years to predict.
        </p>
    </li>
    <li><b>Data Loading:</b>
        <p>
          The <code>load_data(ticker)</code> function downloads historical stock data from Yahoo Finance using <code>yfinance</code> and caches the data using <code>@st.cache_data</code> for efficiency.  It handles potential multi-level column names.
        </p>
    </li>
    <li><b>Data Display:</b>
        <p>
            Displays the raw data using <code>st.write()</code> and plots the "Open" and "Close" prices using <code>plotly.graph_objects</code>.
        </p>
    </li>
    <li><b>Forecasting with Prophet:</b>
         <p>
            A Prophet model is trained on the 'Date' and 'Close' price data. The <code>make_future_dataframe</code> method creates a dataframe for future predictions, and <code>m.predict(future)</code> generates the forecast.
         </p>
    </li>
    <li><b>Forecast Output:</b>
        <p>
            The forecast data is displayed, and the forecast is plotted using <code>plot_plotly</code>.  The trend and seasonality components of the forecast are also displayed using <code>m.plot_components</code> and <code>st.pyplot</code>.
        </p>
    </li>
    <li><b>Error Handling:</b>
        <p>
            A <code>try...except</code> block handles potential errors during data loading or processing, displaying an error message to the user.
        </p>
    </li>
</ol>

<h2>🖼️ Screenshots</h2>

<p align="center">
  [Add your application screenshots here!]
</p>

<h2>🧑‍💻 Author</h2>

<p>
  [Your Name / GitHub Username]
</p>

<p align="center">
  Feel free to contribute to this project! 😊
</p>
