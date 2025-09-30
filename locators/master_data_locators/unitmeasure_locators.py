from selenium.webdriver.common.by import By

class UnitmeasureLocators:
    """计量单位页面元素定位器"""
    # 搜索区域

    SEARCH_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入单位编码'])[1]")
    SEARCH_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入单位名称'])[1]")
    SEARCH_BUTTON = (By.XPATH,"//button[.//span[text()='搜索']]")
    CLEAR_SEARCH_BUTTON = (By.XPATH, "//button[.//span[text()='重置']]")

    #表单元素
    UNIT_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入单位编码'])[2]")
    UNIT_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入单位名称'])[2]")
    MAIN_UNIT_YES = (By.XPATH, "//label[text()='是否是主单位']/../div//span[text()='是']/../span/span")
    MAIN_UNIT_NO = (By.XPATH, "//label[text()='是否是主单位']/../div//span[text()='否']/../span/span")
    SELECT_MAIN_UNIT = (By.XPATH,"//input[@placeholder='请选择主单位']")
    CONVERSION_INPUT = (By.XPATH,"//input[@placeholder='请输入与主单位换算比例']")

    ADD_CONFIRM_BUTTON = (By.XPATH, "//button//span[text()='确 定']")#新增单位页面的确定键
    EDIT_CONFIRM_BUTTON = (By.XPATH, "//button//span[text()='确 定']")#修改单位页面的确定键
    DELETE_CONFIRM_BUTTON = (By.XPATH, "(//button//span[contains(text(),'确定')])[2]")#删除单位页面的确定键


    CHECKBOX = (By.XPATH, "(//span//span[@class='el-checkbox__inner'])[2]")#复选框
    # 操作按钮
    ADD_BUTTON = (By.XPATH, "//button[.//span[text()='新增']]")
    EDIT_BUTTON = (By.XPATH, "(//button//span[text()='修改'])[1]")
    DELETE_BUTTON = (By.XPATH, "(//button//span[text()='删除'])[1]")

    # 表格元素
    TABLE_ROWS = (By.XPATH, "//tr[@class ='el-table__row']")
    NO_DATA_TEXT = (By.XPATH, "//span[text()='暂无数据']")


