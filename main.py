from fastapi import FastAPI
from eduone_mail.app.core.views import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title='Email Service',
    openapi_url="/email/openapi.json",
    docs_url="/email/docs",
    redoc_url=None,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
