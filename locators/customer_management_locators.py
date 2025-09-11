from selenium.webdriver.common.by import By

class CustomerLocators:
    """客户管理页面元素定位器"""
    # 搜索区域
    SEARCH_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入客户编码'])[1]")
    SEARCH_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入客户名称'])[1]")
    SEARCH_BUTTON = (By.XPATH,"//button[contains(@class, 'el-button--primary') and contains(@class, 'el-button--mini')]//span[text()='搜索']")
    CLEAR_SEARCH_BUTTON = (By.XPATH, "//button[.//span[text()='重置']]")

    #表单元素
    CUSTOMER_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入客户编码'])[2]")
    CUSTOMER_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入客户名称'])[2]")
    CUSTOMER_SPECIFICATION_INPUT = (By.XPATH, "//textarea[@placeholder='请输入规格型号']")
    UNIT_SELECT = (By.XPATH, "//label[text()='单位']/following-sibling::div//input[@class='el-input__inner']")
    CATEGORY_SELECT = (By.XPATH, "//label[text()='物料/产品分类']/following-sibling::div//input[@class='vue-treeselect__input']")

    ADD_CONFIRM_BUTTON = (By.XPATH, "(//button//span[text()='确 定'])[2]")#新增物料页面的确定键
    EDIT_CONFIRM_BUTTON = (By.XPATH, "(//button//span[text()='确 定'])[2]")#修改物料页面的确定键
    DELETE_CONFIRM_BUTTON = (By.XPATH, "(//button//span[contains(text(),'确定')])[2]")#删除物料页面的确定键
    CLOSE_BUTTON = (By.XPATH, "//button//span[text()='关 闭']")

    BATCH_MANAGEMENT_SWITCH = (By.XPATH,"//label[contains(text(), '批次管理')]/following-sibling::div//div[@role='switch']")
    CHECKBOX = (By.XPATH, "(//span//span[@class='el-checkbox__inner'])[2]")#复选框
    # 操作按钮
    ADD_BUTTON = (By.XPATH, "//button[contains(@class, 'el-button--primary') and .//span[text()='新增']]")
    EDIT_BUTTON = (By.XPATH, "(//button//span[text()='修改'])[1]")
    DELETE_BUTTON = (By.XPATH, "(//button//span[text()='删除'])[1]")

    # 表格元素
    TABLE_ROWS = (By.CSS_SELECTOR, "tr.el-table__row")
    TABLE_CELLS =(By.TAG_NAME, "td")
    NO_DATA_TEXT = (By.XPATH, "//span[text()='暂无数据']")
    ROW_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

