from selenium.webdriver.common.by import By

class ItemRecptLocators:
    """仓库设置页面元素定位器"""
    # 搜索区域
    SEARCH_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入入库单编号'])[1]")
    SEARCH_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入入库单名称'])[1]")
    SEARCH_BUTTON = (By.XPATH, "//button[.//span[text()='搜索']]")
    CLEAR_SEARCH_BUTTON = (By.XPATH, "//button[.//span[text()='重置']]")

    # 操作按钮
    ADD_BUTTON = (By.XPATH, "//button[.//span[text()='新增']]")
    EDIT_BUTTON = (By.XPATH, "(//button//span[text()='修改'])[1]")
    DELETE_BUTTON = (By.XPATH, "(//button//span[text()='删除'])[1]")

    # 表单元素remark
    ITEMRECPT_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入入库单编号'])[2]")
    ITEMRECPT_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入入库单名称'])[2]")
    ITEMRECPT_POCODE = (By.XPATH, "(//input[@placeholder='请输入采购订单号'])")
    ITEMRECPT_DATE_INPUT = (By.XPATH, "(//input[@placeholder='请选择入库日期'])[2]")

    NOTICECODE_SELECT = (By.XPATH, "//input[@placeholder='请选择到货通知单']/following-sibling::div/button[@type='button']")
    NOTICECODE_SELECT_STATUS = (By.XPATH, "(//input[@placeholder='请选择单据状态'])")
    NOTICECODE_STATUS = (By.XPATH, "//li//span[text()='草稿']")
    NOTICECODE_CODE = (By.XPATH, "//input[@placeholder='请输入通知单编号']")
    NOTICECODE_SEARCH = (By.XPATH, "(//button[.//span[text()='搜索']])[2]")
    SELECT_NOTICECODE_BUTTON = (By.XPATH, "//td[contains(@class, 'is-center')]//label[@role='radio']")
    SELECT_NOTICECODE_CONFIRM = (By.XPATH, "//button//span[text()='确 定']")

    VENDOR_SELECT = (By.XPATH, "//input[@placeholder='请选择供应商']/following-sibling::div/button[@type='button']")
    VENDOR_NAME = (By.XPATH, "(//input[@placeholder='请输入供应商名称'])[2]")
    VENDOR_SEARCH = (By.XPATH, "(//button[.//span[text()='搜索']])[2]")
    SELECT_VENDOR_BUTTON = (By.XPATH, "//td[contains(@class, 'is-center')]//label[@role='radio']")
    SELECT_VENDOR_CONFIRM = (By.XPATH, "//button//span[text()='确 定']")

    ADD_SAVE_BUTTON = (By.XPATH, "//button//span[text()='保 存']")  # 新增页面的保 存键
    EDIT_SAVE_BUTTON = (By.XPATH, "(//button//span[text()='保 存'])")  # 修改页面的保 存键
    DELETE_CONFIRM_BUTTON = (By.XPATH, "(//button//span[contains(text(),'确定')])[2]")  # 删除页面的确定键

    CHECKBOX = (By.XPATH, "(//span//span[@class='el-checkbox__inner'])[2]")  # 复选框

    # 表格元素
    TABLE_ROWS = (By.XPATH, "//tr[@class ='el-table__row']")
    NO_DATA_TEXT = (By.XPATH, "//span[text()='暂无数据']")


