
class Config:
    BASE_URL ="http://www.029tec.com"
    DASHBOARD_URL = BASE_URL + "/index"

    BROWSER = "edge"  # 浏览器类型: chrome, firefox, edge
    HEADLESS =False     # 无头模式
    WINDOW_SIZE = "1920,1080"  #窗口大小

    REPORT_PATH = "./reports"  # 测试报告路径
    REPORT_TITLE = "苦糖果MES系统自动化测试报告"  # 报告标题