from behave import given, when, then
from calc.calculator import Calculator

@given(u'I enter "{expr}"')
def step_impl(context, expr):
    context.expr = expr

@when(u'I press "=" button')
def step_impl(context):
    calc = Calculator()
    context.answer = calc.evalString(context.expr)
    
@then(u'I get the answer "{answer}"')
def step_impl(context, answer):
    assert context.answer == answer
