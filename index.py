from flask import Flask, render_template
import csv


app=Flask(__name__)

def read_csv():
    data = []
    with open('report-seo_audit.csv', newline='', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def read_suggestion():
    data = []
    with open('report-seo_tool_suggestions.csv', newline='', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

@app.route('/', methods=['GET'])
def index() :
    data = read_csv()
    data_suggestion = read_suggestion()
    return render_template('index.html', data=data, data_suggestion=data_suggestion)

if __name__ == '__main__':
    app.run(debug=True)