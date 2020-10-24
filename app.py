from flask import Flask, render_template, request
import forecast

app = Flask(__name__)


@app.route('/')
def result():
    city = request.args.get('city')
    day = request.args.get('day')
    if city is None:
        return render_template('temp1.j2')
    if day is None:
        data = forecast.Forecast(city, 6)
    else:
        data = forecast.Forecast(city, day)
    data.make_content()
    print(data.content)
    if data.content != []:
        return render_template('result.j2', forecast=data.content, city=city)
    else:
        return render_template('error_template.j2', city=city)


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
