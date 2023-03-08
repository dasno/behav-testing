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


@given(u'unpublished content item is created.')
def step_impl(context):
    pass


@when(u'user selects "Submit for publication".')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method-1")
    time.sleep(0.2)
    context.driver.find_element(By.CSS_SELECTOR, ".label-state-private > span:nth-child(2)").click()
    time.sleep(0.2)
    context.driver.find_element(By.ID, "workflow-transition-submit").click()
  


@then(u'content item will change it\'s review state to pending.')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Pending review"
    logout(context)


@given(u'user is a reviewer.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    time.sleep(0.3)
    context.driver.find_element(By.ID, "personaltools-login").click()
    time.sleep(0.3)
    context.driver.find_element(By.ID, "__ac_name").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsreviewer")
    context.driver.find_element(By.ID, "__ac_password").click()
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsreviewer")
    time.sleep(0.3)
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()


@given(u'content item with pending review status has been created.')
def step_impl(context):
    pass


@when(u'user opens list of content items.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/folder_contents")


@then(u'user will see that content item (green color).')
def step_impl(context):
    elements = context.driver.find_elements(By.LINK_TEXT, "Test Method")
    assert len(elements) > 0
    assert context.driver.find_element(By.LINK_TEXT, "Test Method").text == "Test Method"
    assert context.driver.find_element(By.CSS_SELECTOR, ".state-pending > .review_state").text == "pending"
    logout(context)


@given(u'content item has been created.')
def step_impl(context):
    pass


@given(u'that content item has pending rewiew status.')
def step_impl(context):
    pass


@given(u'user has that content item opened.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method-1")


@when(u'he selects "Publish" option from sidebar menu.')
def step_impl(context):
    time.sleep(0.2)
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").click()
    time.sleep(0.2)
    context.driver.find_element(By.ID, "workflow-transition-publish").click()


@then(u'content item will change it\'s state to published.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/folder_contents")
    elements = context.driver.find_elements(By.LINK_TEXT, "Test Method")
    assert len(elements) > 0
    assert context.driver.find_element(By.LINK_TEXT, "Test Method").text == "Test Method"
    assert context.driver.find_element(By.CSS_SELECTOR, ".type-method > .review_state").text == "published"
    logout(context)


@given(u'content item was created.')
def step_impl(context):
    pass


@given(u'it was not published or sent to review.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method-1")
    time.sleep(0.2)
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").click()
    time.sleep(0.2)
    context.driver.find_element(By.ID, "workflow-transition-reject").click()


@when(u'user open list of content items of a certain type.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/folder_contents")


@then(u'user can\'t see that content item.')
def step_impl(context):
    elements = context.driver.find_elements(By.LINK_TEXT, "Test Method")
    assert len(elements) == 0