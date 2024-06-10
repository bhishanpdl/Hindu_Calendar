# Hindu Calendar
Steps
- Download raw html from website: [AstroIca.com](https://www.astroica.com/vedic-astrology/tithi-calculator.php#resultTable) for required months.
- Parse these raw html using pd.read_html and get csv for each months
- Combine all the months and get final data with three columns: tithi, start_time, end_time.
