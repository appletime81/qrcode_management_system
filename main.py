from typing import List, Union
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, APIRouter
from pprint import pprint
from models.file_management_table import files
from config.db import conn

file_management = APIRouter()
app = FastAPI()
templates = Jinja2Templates(directory="templates")


# read_files variables
FILE_CLASS = []



# index page
@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    msg = "金利德金屬股份有限公司資料庫系統"
    return templates.TemplateResponse("index.html", {"request": request, "welcome_str": msg})

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    msg = "金利德金屬股份有限公司資料庫系統"
    return templates.TemplateResponse("index.html", {"request": request, "welcome_str": msg})


# get all files
@app.get("/files", response_class=HTMLResponse)
async def read_files(request: Request):
    print(request.query_params.values())
    print(type(conn.execute(files.select()).fetchall()))
    return templates.TemplateResponse("files.html",
                                      {"request": request, "files": conn.execute(files.select()).fetchall()})


