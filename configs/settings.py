import os

class Config:
    BASE_URL ="http://www.029tec.com"
    API_BASE_URL = BASE_URL
    TEST_USERNAME = os.getenv("MES_USERNAME", "xhran")
    TEST_PASSWORD = os.getenv("MES_PASSWORD", "123456")
    API_TIMEOUT = 10