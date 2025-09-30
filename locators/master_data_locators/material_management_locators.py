from selenium.webdriver.common.by import By

class MaterialLocators:
    """物料管理页面元素定位器"""
    # 搜索区域
    SEARCH_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入物料编码'])[1]")
    SEARCH_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入物料名称'])[1]")
    SEARCH_BUTTON = (By.XPATH,"//button[.//span[text()='搜索']]")
    CLEAR_SEARCH_BUTTON = (By.XPATH, "//button[.//span[text()='重置']]")

    #表单元素
    MATERIAL_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入物料编码'])[2]")
    MATERIAL_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入物料名称'])[2]")
    MATERIAL_SPECIFICATION_INPUT = (By.XPATH, "//textarea[@placeholder='请输入规格型号']")
    UNIT_SELECT = (By.XPATH, "//label[text()='单位']/following-sibling::div//input[@placeholder='请选择单位']")
    CATEGORY_SELECT = (By.XPATH, "//label[text()='物料/产品分类']/following-sibling::div//input[@class='vue-treeselect__input']")

    ADD_CONFIRM_BUTTON = (By.XPATH, "(//button[.//span[text()='确 定']])[2]")#新增物料页面的确定键
    EDIT_CONFIRM_BUTTON = (By.XPATH, "(//button[.//span[text()='确 定']])[3]")#修改物料页面的确定键
    DELETE_CONFIRM_BUTTON = (By.XPATH, "(//button[.//span[contains(text(),'确定')]])[2]")#删除物料页面的确定键
    CLOSE_BUTTON = (By.XPATH, "//button[.//span[text()='关 闭']]")

    BATCH_MANAGEMENT_SWITCH = (By.XPATH,"//label[contains(text(), '批次管理')]/following-sibling::div//div[@role='switch']")
    CHECKBOX = (By.XPATH, "(//span//span[@class='el-checkbox__inner'])[2]")#复选框
    # 操作按钮
    ADD_BUTTON = (By.XPATH, "//button[.//span[text()='新增']]")
    EDIT_BUTTON = (By.XPATH, "(//button//span[text()='修改'])[1]")
    DELETE_BUTTON = (By.XPATH, "(//button//span[text()='删除'])[1]")

    # 表格元素
    TABLE_ROWS = (By.XPATH, "//tr[@class ='el-table__row']")
    NO_DATA_TEXT = (By.XPATH, "//span[text()='暂无数据']")

