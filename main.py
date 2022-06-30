from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, APIRouter, Depends
from pprint import pprint
from fastapi_pagination import Page, Params, paginate, add_pagination
# database setting
from config.db import SessionLocal, engine

# database model
from models.file_management_table import Files, Base
from models.schemas import Files as FilesSchema

Base.metadata.create_all(bind=engine)

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
@app.get("/files", response_class=HTMLResponse, response_model=Page[FilesSchema])
async def read_files(request: Request, params: Params = Depends()):
    # get search parameters
    req_params = dict(request.query_params.items()).copy()

    # fetch all data
    session = SessionLocal()
    datas_orig = session.query(Files).all()

    # convert datas to FilesSchema
    datas = [FilesSchema(**data.__dict__) for data in datas_orig]
    # pprint(datas)
    # print(type(datas[0]))
    # print(len(datas))
    # set page 2
    page = paginate(datas, params)
    pages = paginate(datas, params)
    page_numbers = list(range(1, int(len(datas) / 50) + 2))
    print(page_numbers)
    print(pages.dict())




    # fetch all data with condition
    return templates.TemplateResponse(
        "files.html",
        {"request": request, "files": datas_orig, "col_names": COL_NAMES, "page_numbers": page_numbers}
    )



#######################
# from fastapi_pagination import Page, paginate, add_pagination
# from fastapi import FastAPI
# from pydantic import BaseModel
#
#
# class User(BaseModel):
#     name: str
#
#
# app = FastAPI()
#
# users = [
#     User(name="Yurii"),
#     # ...
# ]
#
#
# @app.get(
#     "/",
#     response_model=Page[User],
# )
# async def route():
#     print(paginate(users))
#     pprint(users)
#     print(type(users[0]))
#     return paginate(users)
#
#
# add_pagination(app)
