import pdb
from flask import Blueprint, render_template, redirect, render_template_string, request, jsonify, url_for, send_file
from folder.models.formModel import UserDetails, EducationalBackground
import json, codecs, pdfkit, os, time
import pymongo
from folder.functions import PdfConvert


client = pymongo.MongoClient()
db = client["test_form"]
test_form = db["test"]

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/")
def test():
    return render_template_string("<h1>This is the test page</h1>"), 200

@user.route("/fillform", methods=["GET", "POST"])
def fillform():
    if request.method == "POST":
        info = request.form
        data = {}
        for i in info.keys():
            data[i] = info.get(i)
        data.pop("csrf_token")
        data = json.dumps(data)
        data = bytes(data,encoding="utf-8")        
        return redirect(url_for("user.getResume", token=data.hex()))
        #return render_template("resume.html",data=data)
    if request.method == "GET":
        form = UserDetails()
        eduForm = EducationalBackground()

        return render_template("forms.html", form=form, eduForm=eduForm)

@user.route("/getDetail/<token>",methods=["GET"])
def getResume(token):
    #data = bytes(token)
    data = codecs.decode(token, "hex").decode("utf-8")
    data = json.loads(str(data))
    test_form.insert_one(data)
    download_route = f"""http://127.0.0.1:5000{url_for("user.getResume", token=token)}"""
    data.pop("_id")
    data_keys = [i for i in data.keys()]
    #print(route)
    #PdfConvert.html_to_pdf(route, data["fullname"])
    return render_template("resume.html", data=data, download = download_route, keys=data_keys)

@user.route("/download/<filename>")
def download(filename):
    route = (request.args.get("route"))
    PdfConvert.html_to_pdf(route, filename)
    tic = time.perf_counter()
    return send_file(f"../resumes/{filename}.pdf", as_attachment=True, download_name="oau_cv.pdf") #, time.sleep(5), 
    toc = time.perf_counter()
    PdfConvert.delete_files(filename)
    
