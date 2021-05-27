from ply import yacc

from pddllex import tokens
from pddl.domain import Domain
from pddl.requirements import Requirements
from pddl.types import Types
from pddl.predicate import Predicate
from pddl.action import *

print(tokens)


def p_pddl(p):
    """pddl : LPAREN DEFINE domain RPAREN
            | LPAREN DEFINE problem RPAREN"""
    p[0] = p[3]


def p_domain(p):
    """domain :  domain_def requirements_def types_def predicates_def action_def"""
    p[0] = Domain(p[1], p[2], p[4], p[5])


def p_domain_def(p):
    """domain_def : LPAREN DOMAIN NAME  RPAREN"""
    p[0] = p[3]


def p_requirements_def(p):
    """requirements_def : LPAREN REQS REQ_STRIPS REQ_TYPING RPAREN"""
    p[0] = Requirements([p[2], p[3]])


def p_types_def(p):
    """types_def : LPAREN  TYPES type_list  RPAREN"""


def p_type_list(p):
    """type_list : NAME MINUS NAME
                 | NAME type_list
                 | NAME MINUS NAME type_list"""


def p_predicates_def(p):
    """predicates_def : LPAREN PREDICATES predicate_list RPAREN"""


def p_predicate_list(p):
    """predicate_list : predicate
                      | predicate  predicate_list"""


def p_predicate(p):
    """predicate : LPAREN NAME param_list RPAREN
                 | LPAREN NOT predicate RPAREN"""


def p_act_predicate_list(p):
    """act_predicate_list : act_predicate
                      | act_predicate  act_predicate_list"""


def p_act_predicate(p):
    """act_predicate : LPAREN NAME var_list RPAREN
                 | LPAREN NOT act_predicate RPAREN"""


def p_param_list(p):
    """param_list : VARIABLE MINUS NAME
                | VARIABLE param_list
                | VARIABLE MINUS NAME param_list"""


def p_action_def(p):
    """action_def : LPAREN ACTION NAME parameter_def precondition_def effect_def RPAREN"""


def p_parameter_def(p):
    """parameter_def : ACT_PARAM LPAREN param_list RPAREN"""


def p_var_list(p):
    """var_list : VARIABLE
                | VARIABLE var_list"""


def p_precondition_def(p):
    """precondition_def :  ACT_PRE predicate
                        |  ACT_PRE LPAREN AND act_predicate_list RPAREN"""
    print(p[1])


def p_effect_def(p):
    """effect_def : ACT_EFF predicate
                  | ACT_EFF LPAREN AND act_predicate_list RPAREN"""


def p_problem(p):
    """problem : """


def p_error(p):
    print(f'Syntax error in input {p}')

parser = yacc.yacc()
