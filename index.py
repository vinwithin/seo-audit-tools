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

@app.route('/', methods=['GET'])
def index() :
    data = read_csv()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)