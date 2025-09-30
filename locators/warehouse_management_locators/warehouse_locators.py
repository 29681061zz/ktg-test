from selenium.webdriver.common.by import By

class WareHouseLocators:
    """仓库设置页面元素定位器"""
    # 搜索区域
    SEARCH_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入工作站编码'])[1]")
    SEARCH_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入工作站名称'])[1]")
    SEARCH_BUTTON = (By.XPATH,"//button[.//span[text()='搜索']]")
    CLEAR_SEARCH_BUTTON = (By.XPATH, "//button[.//span[text()='重置']]")

    # 操作按钮
    ADD_BUTTON = (By.XPATH, "//button[.//span[text()='新增']]")
    EDIT_BUTTON = (By.XPATH, "(//button//span[text()='修改'])[1]")
    DELETE_BUTTON = (By.XPATH, "(//button//span[text()='删除'])[1]")

    #表单元素
    WORKSTATION_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入工作站编码'])[2]")
    WORKSTATION_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入工作站名称'])[2]")
    WORKSTATION_LOCATION = (By.XPATH, "//input[@placeholder='请输入工作站地点']")
    WORKSHOP_SELECT = (By.XPATH, "(//input[@placeholder='请选择车间'])[2]")
    PROCESS_SELECT = (By.XPATH, "(//input[@placeholder='请选择工序'])[2]")

    ADD_SAVE_BUTTON = (By.XPATH, "//button//span[text()='保 存']")#新增页面的保 存键
    EDIT_SAVE_BUTTON = (By.XPATH, "//button//span[text()='保 存']")#修改页面的保 存键
    DELETE_CONFIRM_BUTTON = (By.XPATH, "(//button//span[contains(text(),'确定')])[2]")#删除页面的确定键

    CHECKBOX = (By.XPATH, "(//span//span[@class='el-checkbox__inner'])[2]")#复选框

    # 表格元素
    TABLE_ROWS = (By.XPATH, "//tr[@class ='el-table__row']")
    NO_DATA_TEXT = (By.XPATH, "//span[text()='暂无数据']")


