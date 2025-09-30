from selenium.webdriver.common.by import By

class VendorLocators:
    """供应商管理页面元素定位器"""
    # 搜索区域
    SEARCH_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入供应商编码'])[1]")
    SEARCH_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入供应商名称'])[1]")
    SEARCH_BUTTON = (By.XPATH,"//button[.//span[text()='搜索']]")
    CLEAR_SEARCH_BUTTON = (By.XPATH, "//button[.//span[text()='重置']]")

    #表单元素
    VENDOR_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入供应商编码'])[2]")
    VENDOR_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入供应商名称'])[2]")
    ABBREVIATION_INPUT = (By.XPATH, "(//input[@placeholder='请输入供应商简称'])[2]")
    RATING_INPUT = (By.XPATH, "//input[@placeholder='请输入供应商评分']")

    ADD_CONFIRM_BUTTON = (By.XPATH, "(//button//span[text()='确 定'])[2]")#新增页面的确定键
    EDIT_CONFIRM_BUTTON = (By.XPATH, "(//button//span[text()='确 定'])[2]")#修改页面的确定键
    DELETE_CONFIRM_BUTTON = (By.XPATH, "(//button//span[contains(text(),'确定')])[2]")#删除单位页面的确定键


    CHECKBOX = (By.XPATH, "(//span//span[@class='el-checkbox__inner'])[2]")#复选框
    # 操作按钮
    ADD_BUTTON = (By.XPATH, "//button[.//span[text()='新增']]")
    EDIT_BUTTON = (By.XPATH, "(//button//span[text()='修改'])[1]")
    DELETE_BUTTON = (By.XPATH, "(//button//span[text()='删除'])[1]")

    # 表格元素
    TABLE_ROWS = (By.XPATH, "//tr[@class ='el-table__row']")
    NO_DATA_TEXT = (By.XPATH, "//span[text()='暂无数据']")


