from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys
import time

def logout(context):
    
    context.driver.get("http://localhost:8080/VALU3S")
    time.sleep(0.2)
    context.driver.find_element(By.XPATH, "//ul[2]/li/a/span[2]").click()
    time.sleep(0.2)
    context.driver.find_element(By.ID, "personaltools-logout").click()


@given(u'user is an administrator.')
def step_impl(context):
    
    context.driver.get("http://localhost:8080/VALU3S")
    time.sleep(0.3)
    context.driver.find_element(By.ID, "personaltools-login").click()
    time.sleep(0.3)
    context.driver.find_element(By.ID, "__ac_name").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").click()
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsadmin")
    time.sleep(0.3)
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()


@given(u'user is at methods page.')
def step_impl(context):
    pass


@when(u'user clicks "Add new" in side panel and selects method.')
def step_impl(context):
  
    context.driver.get("http://localhost:8080/VALU3S")
    time.sleep(0.2)
    context.driver.find_element(By.XPATH, "//li[4]/a/span[2]").click()
    time.sleep(0.2)
    context.driver.find_element(By.LINK_TEXT, "Method").click()
  

@then(u'Method creation form shows up.')
def step_impl(context):
 
    assert context.driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").text == "Add Method"
    logout(context)


@given(u'is on method creation form.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++method")


@when(u'user fills out form with correct information and clicks "Save".')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Test Method")
    context.driver.find_element(By.ID, "form-widgets-method_purpose").click()
    context.driver.find_element(By.ID, "form-widgets-method_purpose").send_keys("Test method")
    context.driver.switch_to.frame(3)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>test method<br data-mce-bogus=\"1\"></p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(2)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>test method<br data-mce-bogus=\"1\"></p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(1)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    context.driver.switch_to.default_content()
    context.driver.execute_script("window.scrollTo(0,2550)")
    context.driver.switch_to.frame(1)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>test method<br data-mce-bogus=\"1\"></p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'method is created.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/folder_contents")
    time.sleep(0.3)
    elements = context.driver.find_elements(By.LINK_TEXT, "Test Method")
    assert len(elements) > 0
    logout(context)


@given(u'at least one method exists.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/++add++method")
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Test Method")
    context.driver.find_element(By.ID, "form-widgets-method_purpose").click()
    context.driver.find_element(By.ID, "form-widgets-method_purpose").send_keys("Test method")
    context.driver.switch_to.frame(3)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>test method<br data-mce-bogus=\"1\"></p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(2)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>test method<br data-mce-bogus=\"1\"></p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(1)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    context.driver.switch_to.default_content()
    context.driver.execute_script("window.scrollTo(0,2550)")
    context.driver.switch_to.frame(1)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>test method<br data-mce-bogus=\"1\"></p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.find_element(By.ID, "form-buttons-save").click()


@given(u'user is on page of specific method.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method")
    


@when(u'user clicks on "Edit" button in the sidebar.')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    


@then(u'edit method form will show up.')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").text == "Edit Method"
    logout(context)


@given(u'user is on the method edit form.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method/edit")


@when(u'user changes one or more fields and cliks "Save".')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").clear()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("edited")
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'Method has been modified.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/folder_contents")
    elements = context.driver.find_elements(By.LINK_TEXT, "edited")
    assert len(elements) > 0
    logout(context)


@given(u'user is on home page.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/")


@when(u'user selects "Contents" from the side bar.')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//li[@id='contentview-folderContents']/a/span").click()


@then(u'user is on content page.')
def step_impl(context):
    assert("http://localhost:8080/VALU3S/folder_contents" in context.driver.current_url)
    logout(context)


@given(u'user is on content page.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/folder_contents")


@given(u'user in in a folder where specific item is located.')
def step_impl(context):
    pass


@when(u'user clicks on checkbox next to method and clicks on delete icon and confirms.')
def step_impl(context):
    context.driver.find_element(By.ID, "select6InputCheckbox").click()
    context.driver.find_element(By.CSS_SELECTOR, ".glyphicon-trash").click()
    context.driver.find_element(By.CSS_SELECTOR, ".applyBtn").click()


@then(u'item is deleted.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/folder_contents")
    elements = context.driver.find_elements(By.LINK_TEXT, "edited")
    assert len(elements) == 0
    logout(context)



@given(u'user is on the method creation from.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    time.sleep(0.2)
    context.driver.find_element(By.XPATH, "//li[4]/a/span[2]").click()
    time.sleep(0.2)
    context.driver.find_element(By.LINK_TEXT, "Method").click()


@when(u'user don\'t fill in the title of a method and saves.')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
    


@then(u'Prompt shows up.')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".portalMessage")
    assert len(elements) > 0
    context.driver.find_element(By.CSS_SELECTOR, ".portalMessage").click()
    assert context.driver.find_element(By.CSS_SELECTOR, "dd").text == "There were some errors."
    logout(context)


@given(u'a method has been created.')
def step_impl(context):
    pass


@when(u'user goes to a methods page.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method-1")


@then(u'created method shoud be visible as unpublished (red).')
def step_impl(context):
   assert context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Private"
   logout(context)


