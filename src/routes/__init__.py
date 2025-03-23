from fastapi import APIRouter

router = APIRouter()

# 如果您有其他路由文件，也需要在这里导入它们
# from .user_routes import router as user_router
# from .auth_routes import router as auth_router

# 然后将它们包含到主路由中
# router.include_router(user_router)
# router.include_router(auth_router)