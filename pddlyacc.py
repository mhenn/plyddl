from ply import yacc

from pddllex import tokens
from pddl.domain import Domain
from pddl.requirements import Requirements
from pddl.types import Type, Variables
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
    p[0] = p[3]


def p_type_list(p):
    """type_list : NAME MINUS NAME
                 | NAME type_list
                 | NAME MINUS NAME type_list"""
    if len(p) == 4:
        p[0] = [Type([p[1]],p[3])]
    elif len(p) == 3:
        t = p[2]
        t[-1].add(p[1])
        p[0] = t
    elif len(p) == 5:
        t = p[4]
        t.append(Type([p[1]], p[3]))
        p[0] = t


def p_predicates_def(p):
    """predicates_def : LPAREN PREDICATES predicate_list RPAREN"""
    p[0] = p[3]

def p_predicate_list(p):
    """predicate_list : predicate
                      | predicate  predicate_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        preds = p[2]
        preds.append(p[1])
        p[0] = preds


def p_predicate(p):
    """predicate : LPAREN NAME param_list RPAREN
                 | LPAREN NOT predicate RPAREN"""

    pred = None
    if p[2] == '-':
        pred = p[3]
        p[3].negation = True
    else:
        pred = Predicate(p[2], p[3])
    p[0] = pred

def p_mixed_predicate_list(p):
    """mixed_predicate_list : mixed_predicate
                      | mixed_predicate  mixed_predicate_list"""


def p_mixed_predicate(p):
    """mixed_predicate : LPAREN NAME mixed_list RPAREN
                 | LPAREN NOT mixed_predicate RPAREN"""


def p_param_list(p):
    """param_list : VARIABLE MINUS NAME
                | VARIABLE param_list
                | VARIABLE MINUS NAME param_list"""
    if len(p) == 4:
        p[0] = [Variables([p[1]], p[3])]
    elif len(p) == 3:
        t = p[2]
        t[-1].add(p[1])
        p[0] = t
    elif len(p) == 5:
        t = p[4]
        t.append(Variables([p[1]], p[3]))
        p[0] = t


def p_action_def(p):
    """action_def : LPAREN ACTION NAME parameter_def precondition_def effect_def RPAREN"""


def p_parameter_def(p):
    """parameter_def : ACT_PARAM LPAREN param_list RPAREN"""
    p[0] = p[3]


def p_precondition_def(p):
    """precondition_def :  ACT_PRE mixed_predicate
                        |  ACT_PRE LPAREN AND mixed_predicate_list RPAREN"""


def p_effect_def(p):
    """effect_def : ACT_EFF predicate
                  | ACT_EFF LPAREN AND mixed_predicate_list RPAREN"""


###############
####PROBLEM####
###############


def p_problem(p):
    """problem : problem_def pb_domain_def objects_def init_def goal_def"""


def p_problem_def(p):
    """problem_def : LPAREN PROBLEM NAME RPAREN"""


def p_pb_domain_def(p):
    """pb_domain_def : LPAREN PB_DOMAIN NAME RPAREN"""


def p_objects_def(p):
    """objects_def : LPAREN OBJECTS type_list RPAREN """


def p_init_def(p):
    """init_def : LPAREN INIT mixed_predicate_list RPAREN"""


def p_goal_def(p):
    """goal_def :  LPAREN GOAL mixed_predicate RPAREN
                |  LPAREN GOAL LPAREN AND mixed_predicate_list RPAREN RPAREN"""


###############
#####UTILS#####
###############
def p_constant_list(p):
    """constant_list : NAME
                     | NAME constant_list"""


def p_mixed_list(p):
    """mixed_list : VARIABLE
                  | NAME
                  | VARIABLE mixed_list
                  | NAME mixed_list"""


def p_var_list(p):
    """var_list : VARIABLE
                | VARIABLE var_list"""


def p_error(p):
    print(f'Syntax error in input {p}')


parser = yacc.yacc()
