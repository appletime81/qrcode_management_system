from typing import List, Union
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import Page, paginator, add_pagination, Params, LimitOffsetPage, paginate
from fastapi import FastAPI, Request, APIRouter
from pprint import pprint
from models.file_management_table import files
from config.db import conn

file_management = APIRouter()
app = FastAPI()
templates = Jinja2Templates(directory="templates")


# read_files variables
COL_NAMES = ["ip位置", "資料夾", "檔名", "建立日期"]


# index page
@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    msg = "金利德金屬股份有限公司資料庫系統"
    return templates.TemplateResponse(
        "index.html", {"request": request, "welcome_str": msg}
    )


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    msg = "金利德金屬股份有限公司資料庫系統"
    return templates.TemplateResponse(
        "index.html", {"request": request, "welcome_str": msg}
    )


# get all files
@app.get("/files", response_class=HTMLResponse)
async def read_files(request: Request):
    # get search parameters
    params = dict(request.query_params.items())

    # fetch all data
    print(type(conn.execute(files.select()).fetchall()))
    print(paginate(conn.execute(files.select()).fetchall()))

    # fetch all data with condition
    return templates.TemplateResponse(
        "files.html",
        {"request": request, "files": conn.execute(files.select()).fetchall(), "col_names": COL_NAMES},
    )


# add_pagination(app)
