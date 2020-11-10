from Classes.functions import Function
from Classes.print import Print
from Classes.variables import Assign
from Classes.math import Operators
from Classes.classes import Class
from Classes.conditions import Condition
from Classes.importStatement import ImportStatement
from Classes.loops import Loop
from Classes.builtInFunctions import BuiltInFunctions
from Classes.comments import Comments
from Classes.indentation import Indentation
from Classes.underscores import Underscores
from Classes.braces import Braces

function = Function()
printStatement = Print()
assign = Assign()
operators = Operators()
classes = Class()
condition = Condition()
importStatement = ImportStatement()
loop = Loop()
builtInFunctions = BuiltInFunctions()
comments = Comments()
indentation = Indentation()
underscores = Underscores()
braces = Braces()

def count_keywords(keyword,codeInfo,*args,**kwargs):
    if function.isFunction(keyword):
        function.increase_functions_count(codeInfo)
    if printStatement.isPrint(keyword):
        codeInfo.print_statements += 1
    if assign.isAnAssignOperator(keyword):
        codeInfo.assign_operations += 1
    if operators.isAnOperator(keyword):
        codeInfo.math_operations += 1
    if classes.isClass(keyword):
        codeInfo.classes += 1
    if condition.isCondition(keyword):
        codeInfo.conditional_blocks += 1
    if classes.isClassProperty(keyword):
        codeInfo.classes_properties += 1
    if importStatement.isAnImport(keyword):
        codeInfo.import_statements += 1
    if loop.isForLoop(keyword):
        codeInfo.for_loops += 1
    if loop.isWhileLoop(keyword):
        codeInfo.while_loops += 1
    if builtInFunctions.isBuiltInFunction(keyword):
        codeInfo.python_built_in_functions += 1
    if comments.isComment(keyword):
        codeInfo.comments += 1
    if indentation.isAnIndentation(keyword):
        codeInfo.line_indentation += 1
    if underscores.isAnUnderscore(keyword):
        codeInfo.used_underscores += 1
    if underscores.isDoubleUnderscores(keyword):
        codeInfo.double_underscore_used += 1
    if braces.isBrackets(keyword):
        codeInfo.number_of_lists += 1
    if braces.isCurlyBraces(keyword):
        codeInfo.number_of_dictionaries += 1
