import os
import shutil
import subprocess

folder = os.getcwd()

if not "{{cookiecutter.writing_docs}}" == "yes":
    shutil.rmtree(os.path.join(folder, "docs"))
    os.remove(os.path.join(folder, "mkdocs.yml"))

if "{{cookiecutter.package_manager}}" == "pip":
    os.remove(os.path.join(folder, "environment.yml"))
else:
    os.remove(os.path.join(folder, "requirements.txt"))
    os.remove(os.path.join(folder, "requirements-dev.txt"))

message = "initial commit from gh:zehengl/cookiecutter-streamlit"

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", message])
