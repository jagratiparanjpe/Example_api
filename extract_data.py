from helper import helper
import covid_api
import argparse

# required arg

parser = argparse.ArgumentParser()

parser.add_argument('--inputfile', required=True, help="input file path")

args = parser.parse_args()
inputfile = args.inputfile

header = ['date', 'iso', 'num_confirmed', 'num_deaths', 'num_recovered']
outputFileName = "Covid_Data.xlsx"
url = 'https://covid-api.com/api/reports?'

file_data = []
for date, iso in helper.read_config_file(inputfile):
    file_data.append(covid_api.get_iso_data(date, iso, url))

if len(file_data) > 0:
    helper.generate_excel_file(outputFileName,header,file_data)
    print("File is generated")

