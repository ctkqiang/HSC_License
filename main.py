# 导入必要的FastAPI组件
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.routes.routes import router

# 创建FastAPI应用实例
app = FastAPI()


# 添加CORS中间件，允许跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,  # 允许携带凭证
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有请求头
)

# 注册API路由和静态文件
app.include_router(router, prefix="/api")  # 添加API路由，前缀为/api
app.mount("/static", StaticFiles(directory="public"), name="static")  # 挂载静态文件目录
templates = Jinja2Templates(directory="public")  # 设置模板目录


# 定义根路由，返回主页HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
