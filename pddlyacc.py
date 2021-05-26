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
    """types_def : LPAREN  TYPES type_loop  RPAREN"""


def p_type_list(p):
    """type_loop : NAME - NAME
                 | NAME type_list
                 | NAME - NAME type_list"""


def p_predicates_def(p):
    """predicates_def : LPAREN PREDICATES predicate_list RPAREN"""


def p_predicate_list(p):
    """predicate_list : LPAREN predicate RPAREN
                      | LPAREN predicate RPAREN predicate_list"""


def p_predicate(p):
    """predicate : NAME var_list"""


def p_var_list(p):
    """var_list : VARIABLE - NAME
                | VARIABLE var_list
                | VARIABLE - NAME var_list"""


def p_action_def(p):
    """action_def : LPAREN ACTION NAME parameter_def precondition_def effect_def RPAREN"""


def p_parameter_def(p):
    """parameter_def : ACT_PARAM LPAREN var_list RPAREN"""


def p_precondition_def(p):
    """"""


def effect_def(p):
    """"""


def p_problem(p):
    """problem : """


def p_error(p):
    print("Syntax error in input!!")

parser = yacc.yacc()
