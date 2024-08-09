# auvery Task pandas Data Cleaning
This is a sample task implementation for auvery. This is the sample code for the auvery blog post on [data cleaning with pandas in auvery](https://auvery.de/blog-posts/data-cleaning-mit-pandas).

This tasks takes the following CSV-File as an Input Parameter. It cleans the data and creates a JSON as a task result.

```csv
OrderID,CustomerID,OrderDate,Amount,ItemCount
1001,2001,2024-01-05 14:30,59.99,3
1002,2002,2024/02/10 09:20,15.99,1
1003,2003,,22.49,
1004,2004,2024-03-15 16:45,34.99,2
1005,2005,March 20, 2024,27.99,1
1006,2006,2024-04-01 12:00,,5
1007,2007,2024-04-05 18:30,49.99,2
1008,2008,2024-05-10 08:15,19.99,
1009,2009,2024/05/15 13:25,79.99,4
1010,2010,,99.99,3
```

## Input Parameter, Results and Errors
The following table show the input parameters, the results and the errors cases of the auvery Task.

| Name             | Input Parameter \| Result \| Error | Data Type | Environment Variable Name |
|------------------|------------------------------------|-----------|---------------------------|
| CSV File Path    | Input Parameter                    | File      | AUV_IN_CSV_FILE_PATH      |
| JSON File Path   | Result                             | Object    | AUV_OUT_JSON_FILE_PATH    |
| Error Read File  | Error                              | String    | AUV_ERR_CSV_ERROR         |
| Error Clean Data | Error                              | String    | AUV_ERR_CSV_ERROR         |

## Useful commands for local development
Find a list of useful commands that you can use when working in a local environment.

```bash
# Build docker image locally
docker build -t auvery-task-clean-orders .

# Run task locally
docker run --rm \
  -e AUV_IN_CSV_FILE_PATH=/data/input/orders.csv \
  -e AUV_OUT_JSON_FILE_PATH=/data/output/orders_clean.json \
  -e AUV_ERR_CSV_ERROR=/data/output/csv_error.txt \
  -e AUV_ERR_CLEANING_ERROR=/data/output/cleaning_error.txt \
  -v $(pwd)/input:/data/input \
  -v $(pwd)/output:/data/output \
  auvery-task-clean-orders
```