Run main.py to run api calls on sites specified in "sites_to_call.py"

Main does three things:
1. TestCallTime.py loads the site, and makes every call found in StandardFindarCalls.py NREP times
2. Plot report generates pngs of the data summary (optional step)
3. concat_df_to_csv.py concatenates all the dataframes into one large report for the web app.

Run plotter/dashboard/main.py to launch the dashboard on the pre-existing datafram stored in 
plotter/dashboard/data

