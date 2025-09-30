from selenium.webdriver.common.by import By

class WareHouseLocators:
    """仓库设置页面元素定位器"""
    # 搜索区域
    SEARCH_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入仓库编码'])[1]")
    SEARCH_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入仓库名称'])[1]")
    SEARCH_BUTTON = (By.XPATH,"//button[.//span[text()='搜索']]")
    CLEAR_SEARCH_BUTTON = (By.XPATH, "//button[.//span[text()='重置']]")

    # 操作按钮
    ADD_BUTTON = (By.XPATH, "//button[.//span[text()='新增']]")
    EDIT_BUTTON = (By.XPATH, "(//button//span[text()='修改'])[1]")
    DELETE_BUTTON = (By.XPATH, "(//button//span[text()='删除'])[1]")

    #表单元素remark
    WAREHOUSE_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入仓库编码'])[2]")
    WAREHOUSE_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入仓库名称'])[2]")
    WAREHOUSE_AREA = (By.XPATH, "//input[@placeholder='请输入面积']")
    WAREHOUSE_LOCATION = (By.XPATH, "(//textarea[@placeholder='请输入内容'])[1]")
    WAREHOUSE_REMARK = (By.XPATH, "(//textarea[@placeholder='请输入内容'])[2]")

    ADD_SAVE_BUTTON = (By.XPATH, "//button//span[text()='确 定']")#新增页面的保 存键
    EDIT_SAVE_BUTTON = (By.XPATH, "//button//span[text()='确 定']")#修改页面的保 存键
    DELETE_CONFIRM_BUTTON = (By.XPATH, "(//button//span[contains(text(),'确定')])[2]")#删除页面的确定键

    CHECKBOX = (By.XPATH, "(//span//span[@class='el-checkbox__inner'])[2]")#复选框

    # 表格元素
    TABLE_ROWS = (By.XPATH, "//tr[@class ='el-table__row']")
    NO_DATA_TEXT = (By.XPATH, "//span[text()='暂无数据']")


