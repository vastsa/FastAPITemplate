import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from Extensions.logger import logger
from Plugins import Test
from SQLConfig import models
from SQLConfig.database import engine

app = FastAPI(
    title="FastApi快速开发模板",
    version='1',
)

# 挂载静态资源文件夹
app.mount('/static', StaticFiles(directory='Static'), name='static')
# 挂载Jinja2模板文件夹
tmp = Jinja2Templates(directory='Templates')
# 挂载路由
app.include_router(Test.view, tags=['测试接口'])

# 后台api允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def index():
    """
    首页
    """
    return RedirectResponse(url='/docs')


if __name__ == '__main__':
    """
    启动项目
    """
    logger.info('Web项目启动')
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True, debug=True, workers=10)
