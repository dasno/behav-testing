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


@given(u'user is on the method edit page.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method-1/edit")

@when(u'user selects Relations tab.')
def step_impl(context):
    context.driver.find_element(By.ID, "autotoc-item-autotoc-2").click()


@then(u'user is on the relation modification form.')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, "#formfield-form-widgets-related_methods > .horizontal")
    assert len(elements) > 0
    logout(context)


@given(u'some method already exists.')
def step_impl(context):
    pass


@given(u'user is on method relation modification form.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method-1/edit#autotoc-item-autotoc-2")


@when(u'user inputs name of his desired tool.')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#formfield-form-widgets-tools .path-wrapper .glyphicon").click()
    context.driver.find_element(By.ID, "s2id_autogen12").send_keys("Combine")
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-relateditems-result-title").click()
    context.driver.find_element(By.ID, "form-buttons-save").click()


@when(u'user selects it and click Save.')
def step_impl(context):
    pass


@then(u'related tool has been added to the method.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method-1/edit#autotoc-item-autotoc-2")
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".pattern-relateditems-item-title")
    assert len(elements) > 0
    logout(context)


@given(u'is at edit method\'s relations form.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method-1/edit#autotoc-item-autotoc-2")


@when(u'user clicks on small x in the top left corner of tool and clicks Save.')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".select2-search-choice-close").click()
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'reference to that tool has been removed.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test-method-1/edit#autotoc-item-autotoc-2")
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".pattern-relateditems-item-title")
    assert len(elements) == 0
    logout(context)


@given(u'user is consumer.')
def step_impl(context):
    pass


@given(u'method is created and published.')
def step_impl(context):
    pass


@given(u'published method references a tool.')
def step_impl(context):
    pass


@when(u'user clicks to list of methods.')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Methods").click()


@when(u'selects said method.')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Combinatorial Testing").click()


@when(u'clicks on referenced too.')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".contenttype-tool").click()


@then(u'page of that tool will open.')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").text == "Testos / Combine"