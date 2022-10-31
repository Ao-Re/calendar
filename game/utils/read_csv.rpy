init: 
  $import csv
  python:
    def read_csv():
      f = open("schedule.csv")
      csv_f = csv.reader(f)
      

