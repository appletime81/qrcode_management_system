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
    search_filename_datas = list()
    search_folder_datas = list()
    search_date_datas = list()
    pprint(req_params)

    # get extension from search parameters
    extension = req_params.get("extension", "all")
    search_filename = None if not req_params.get("filename", None) or req_params.get("filename") == "None" else req_params.get("filename")
    search_folder = None if not req_params.get("foldername", None) or req_params.get("foldername") == "None" else req_params.get("foldername")
    search_date = None if not req_params.get("date", None) or req_params.get("date") == "None" else req_params.get("date")
    print(search_date)

    # 給定分頁參數大小預設值
    params.size = 25

    # fetch all data
    session = SessionLocal()
    if extension == "all":
        datas_orig = session.query(Files)
    else:
        datas_orig = session.query(Files).filter(Files.file_name.contains(extension)).all()

    if search_filename:
        print("search_filename:", search_filename)
        search_filename_datas = datas_orig.filter(Files.file_name.contains(req_params.get("params"))).all()
    if search_folder:
        print("search_folder:", search_folder)
        search_folder_datas = datas_orig.filter(Files.root_path.contains(req_params.get("params"))).all()
    if search_date:
        print("search_date:", search_date)
        search_date_datas = datas_orig.filter(Files.data_insert_date.contains(req_params.get("params"))).all()

    # unique data with search_filename_datas and search_folder_datas and search_date_datas
    if search_filename or search_folder or search_date:
        datas_orig = list(set(search_filename_datas + search_folder_datas + search_date_datas))

    if not search_filename and not search_folder and not search_date:
        try:
            datas_orig = datas_orig.all()
        except AttributeError:  # 'list' object has no attribute 'all'
            pass

    # convert datas to FilesSchema
    datas = [FilesSchema(**data.__dict__) for data in datas_orig]
    datas = paginate(datas, params)
    datas_dict = datas.dict()
    page_number_list = list(range(1, int(len(datas_orig) / params.size) + 2))  # 總頁數

    return templates.TemplateResponse(
        "files.html",
        {
            "request": request,
            "files": datas_dict.get("items"),
            "col_names": COL_NAMES,
            "page_numbers": page_number_list,
            "current_page": datas_dict.get("page"),
            "every_page_size": params.size,
            "extension": extension,
            "params": req_params.get("params"),
            "search_filename": search_filename,
            "search_folder": search_folder,
            "search_date": search_date,
        },
    )
