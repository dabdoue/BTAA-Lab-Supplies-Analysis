# BTAA Lab Supplies Data Analysis

The repository contains the code and frontend for analyzing the lab supplies purchasing data from BTAA. 

There are 3 tools:

1. School Usage Analysis
   1. Shows school usage data from each school by both volume and cost
2. Market Basket Analysis
   1. Shows historical price data of items in Market Basket
   2. Also shows what items were consistently in market basket across all years of data
3. Fisher School Price Comparison
   1. For items in Fisher's Hotlist, shows comparisons of what Fisher quoted for sales, price, and quantity purchased, and compares to data from each school as well as the sum of this data.

School Usage Analysis can take over 1 minute to run as the data loading process takes a long time, however the other tools run in a few seconds.

It is built on a basic flask app. Files are uploaded using flask and stored on the server until the next time a tool is run. Once the analysis is complete, the files are downloaded to the client's machine as a zip file containing the file(s) used as input as well as the output file(s). If there were any errors during processing, an errors.txt file is also included in the zip file, which can hopefully be used by maintainer to address issues. At very minimum, the creation time of the file can help link to logging messages on the server.

To run, simply run `flask run`

To run so that all devices on the same network can access the application, run `flask run --host=0.0.0.0` - this will make the application accessible by going to the server's IP address, then the port of the application (by default 5000). (ex: http://10.192.XX.XXX:5000)

### Requirements

In a conda environment, run `conda install flask numpy pandas openpyxl`
