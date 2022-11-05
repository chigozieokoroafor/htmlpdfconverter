import os
#os.remove("new.pdf")
path = "./resumes"
if os.path.exists(path):
    print(os.path.abspath(path))