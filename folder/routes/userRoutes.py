import pdb
from flask import Blueprint, render_template, redirect, render_template_string, request, jsonify, url_for, send_file
from folder.models.formModel import UserDetails, EducationalBackground
import json, codecs, pdfkit, os, time
import pymongo
from folder.functions import PdfConvert


client = pymongo.MongoClient()
db = client["test_form"]
test_form = db["test"]

user = Blueprint("user", __name__)

@user.route("/")
def test():
    return redirect(url_for("user.fillform"))

@user.route("/fillform", methods=["GET", "POST"])
def fillform():
    if request.method == "POST":
        info = request.form
        data = {}
        for i in info.keys():
            data[i] = info.get(i)
        #data.pop("csrf_token")
        data = json.dumps(data)
        data = bytes(data,encoding="utf-8")        
        return redirect(url_for("user.getResume", token=data.hex()))
        #return render_template("resume.html",data=data)
    if request.method == "GET":
        form = UserDetails()
        eduForm = EducationalBackground()

        return render_template("form2.html", form=form, eduForm=eduForm)

@user.route("/getDetail/<token>",methods=["GET"])
def getResume(token):
    #data = bytes(token)
    data = codecs.decode(token, "hex").decode("utf-8")
    data = json.loads(str(data))
    test_form.insert_one(data)
    download_route = f"""http://127.0.0.1:5000{url_for("user.getResume", token=token)}"""
    data.pop("_id")
    data_keys = [i for i in data.keys()]
    #create a loop for how it would be shown, esspecially those with text areas to be listed as points
    
    return render_template("page2.html", data=data, download = download_route)

@user.route("/download/<filename>")
def download(filename):
    route = (request.args.get("route"))
    PdfConvert.html_to_pdf(route, filename)
    #tic = time.perf_counter()
    return send_file(f"../resumes/{filename}.pdf", as_attachment=True, download_name="oau_cv.pdf") #, time.sleep(5), 
    
    
