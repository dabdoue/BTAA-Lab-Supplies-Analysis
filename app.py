import fisher_school_price_comparison
import tracking_market_baskets
import school_usage_analysis
import os
from flask import *
from werkzeug.utils import secure_filename
from io import BytesIO
from zipfile import ZipFile

ready_to_delete = False

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + "/uploads"

def check_success(success):
    if success != "True":
        with open("errors.txt", "w") as f:
            f.write("There were errors with the data.\nYou can show this message to someone in IT for support\n")
            f.write("Error:\n" + str(success) + "\n")
            f.write(
                "Please ensure you have correct input data and try again")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_analysis_type', methods=['POST'])
def get_analysis_type():
    analysis_type = request.form['analysis_type']
    print(analysis_type)
    return analysis_type


@app.route('/get_school_usage_file_dirs', methods=['POST'])
def get_school_usage_file_dirs():
    dir = os.getcwd()
    if ("uploads" not in os.getcwd()):
        dir = os.path.join(os.getcwd(), "uploads")
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    f = request.files['file']
    f.save(os.path.join(
        app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    
    check_success(school_usage_analysis.school_usage_analysis())
    
    stream = BytesIO()
    with ZipFile(stream, 'w') as zf:
        for file in os.listdir(os.getcwd()):
            zf.write(file, os.path.basename(file))
    stream.seek(0)
    
    return send_file(
        stream,
        as_attachment=True,
        download_name='school_usage_analysis.zip'
    )

    


@app.route('/get_market_basket_file_dirs', methods=['POST'])
def get_market_basket_file_dirs():
    dir = os.getcwd()
    if ("uploads" not in os.getcwd()):
        dir = os.path.join(os.getcwd(), "uploads")
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    f = request.files['file']
    f.save(os.path.join(
        app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

    check_success(tracking_market_baskets.tracking_market_baskets())

    stream = BytesIO()
    with ZipFile(stream, 'w') as zf:
        for file in os.listdir(os.getcwd()):
            zf.write(file, os.path.basename(file))
    stream.seek(0)

    # other_thing()
    
    # os.chdir('../templates')
    # print(os.getcwd())
    # return redirect('/')
    return send_file(
        stream,
        as_attachment=True,
        download_name='market_basket_analysis.zip'
    )


@app.route('/success')
def success():
    return render_template('success.html')


# def other_thing():
#     return render_template('index.html')


@app.route('/get_fisher_file_dirs', methods=['POST'])
def get_fisher_file_dirs():
    dir = os.getcwd()
    if ("uploads" not in os.getcwd()):
        dir = os.path.join(os.getcwd(), "uploads")
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    f1 = request.files['file1']
    f1.save(os.path.join(
        app.config['UPLOAD_FOLDER'], secure_filename(f1.filename)))
    f2 = request.files['file2']
    f2.save(os.path.join(
        app.config['UPLOAD_FOLDER'], secure_filename(f2.filename)))

    year = request.form['year']
    check_success(fisher_school_price_comparison.fisher_school_price_comparison(
        year))

    # fisher_school_price_comparison.fisher_school_price_comparison()

    stream = BytesIO()
    with ZipFile(stream, 'w') as zf:
        for file in os.listdir(os.getcwd()):
            zf.write(file, os.path.basename(file))
    stream.seek(0)

    return send_file(
        stream,
        as_attachment=True,
        download_name='fisher_school_price_comparison.zip'
    )


if "__name__" == "__main__":
    app.run()
