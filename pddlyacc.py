from ply import yacc
from pddllex import tokens
from pddl.domain.domain import Domain
from pddl.domain.requirements import Requirements
from pddl.domain.types import Type, Variables
from pddl.predicate import Predicate, PredicateGroup, ConditionGroup, QuantifyGroup, GroupType
from pddl.domain.action import *

from pddl.problem.problem import Problem
from pddl.problem.objects import ProblemObjects
from pddl.problem.init import Init
from pddl.problem.goal import Goal

print(tokens)


def p_pddl(p):
    """pddl : LPAREN DEFINE domain RPAREN
            | LPAREN DEFINE problem RPAREN"""
    p[0] = p[3]


def p_domain(p):
    """domain :  domain_def requirements_def types_def predicates_def action_def"""
    p[0] = Domain(p[1], p[2],p[3], p[4], p[5])


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
        t.insert(0,Type([p[1]], p[3]))
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
        preds.insert(0,p[1])
        p[0] = preds


def p_predicate(p):
    """predicate : LPAREN NAME param_list RPAREN
                 | LPAREN NOT predicate RPAREN"""

    if p[2] == '-':
        pred = p[3]
        p[3].negation = True
    else:
        pred = Predicate(p[2], p[3])
    p[0] = pred

def p_empty(p):
    'empty : '
    pass


def p_mixed_predicate_list(p):
    """mixed_predicate_list : mixed_predicate
                      | mixed_predicate mixed_predicate_list
                      """
    if len(p) == 2:
        if p[1]:
            p[0] = [p[1]]
    elif len(p) == 3:
        m_p = p[2]
        m_p.insert(0,p[1])
        p[0] = m_p


def p_predicate_group(p):
    """predicate_group :  OR mixed_predicate_list
                        | AND mixed_predicate_list
                        | WHEN mixed_predicate mixed_predicate
                        | quantify_group"""
    spec = p[1]
    if spec in ['and', 'or']:
        if spec == 'and':
            type = GroupType.AND
        elif spec == 'or':
            type = GroupType.OR
        m_p = p[2]
        p[0] = PredicateGroup(type, m_p)
    elif spec == 'when':
        p[0] = ConditionGroup(GroupType.WHEN, p[3], p[2])

    if len(p) == 2:
        p[0] = p[1]

def p_quantify_group(p):
    """quantify_group :  FORALL LPAREN param_list RPAREN mixed_predicate
                       | EXISTS LPAREN param_list RPAREN mixed_predicate """
    spec = p[1]
    if spec in ['forall', 'exists']:
        params = p[3]
        if isinstance(p[5], (QuantifyGroup, ConditionGroup)):
            raise Exception("Wrong Syntax for quantifying: " + p)
        if spec == 'forall':
            type = GroupType.FORALL
        else:
            type = GroupType.EXISTS
        p[0] = QuantifyGroup(type, p[5], params)


def p_mixed_predicate(p):
    """mixed_predicate : LPAREN NAME mixed_list RPAREN
                       | LPAREN NOT mixed_predicate RPAREN
                       | LPAREN predicate_group RPAREN
                       | LPAREN EQUALS var_list RPAREN
                       """
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 5:
        if p[2] == 'not':
            pred = p[3]
            pred.negation = True
            p[0] = pred
        elif p[2] == '=':
            p[0] = Predicate('=', p[3])
        else:
            p[0] = Predicate(p[2], p[3]['var'], p[3]['const'])


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
        t.insert(0,Variables([p[1]], p[3]))
        p[0] = t


def p_action_def(p):
    """action_def : LPAREN ACTION NAME parameter_def precondition_def effect_def RPAREN"""
    p[0] = Action(p[3], p[4], p[5], p[6])


def p_parameter_def(p):
    """parameter_def : ACT_PARAM LPAREN param_list RPAREN"""
    p[0] = p[3]


def p_precondition_def(p):
    """precondition_def :  ACT_PRE mixed_predicate
                        |  ACT_PRE LPAREN OR mixed_predicate_list RPAREN
                        |  ACT_PRE LPAREN AND mixed_predicate_list RPAREN"""
    if len(p) == 3:
        p[0] = [p[2]]
    else:
        if p[3] == 'or':
            type = GroupType.OR
        else:
            type = GroupType.AND

        p[0] = PredicateGroup(type, p[4])


def p_effect_def(p):
    """effect_def : ACT_EFF mixed_predicate
                  | ACT_EFF LPAREN AND mixed_predicate_list RPAREN"""
    if len(p) == 2:
        p[0] = [p[2]]
    else:
        p[0] = p[4]


###############
####PROBLEM####
###############


def p_problem(p):
    """problem : problem_def pb_domain_def objects_def init_def goal_def"""
    p[0] = Problem(p[1], p[2], p[3], p[4], p[5])


def p_problem_def(p):
    """problem_def : LPAREN PROBLEM NAME RPAREN"""
    p[0] = p[3]


def p_pb_domain_def(p):
    """pb_domain_def : LPAREN PB_DOMAIN NAME RPAREN"""
    p[0] = p[3]


def p_objects_def(p):
    """objects_def : LPAREN OBJECTS type_list RPAREN """
    p[0] = p[3]


def p_init_def(p):
    """init_def : LPAREN INIT mixed_predicate_list RPAREN"""
    p[0] = p[3]



def p_goal_def(p):
    """goal_def :  LPAREN GOAL mixed_predicate RPAREN"""
    p[0] = p[3]

###############
#####UTILS#####
###############
def p_constant_list(p):
    """constant_list : NAME
                     | NAME constant_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        consts = p[2]
        consts.insert(0,p[1])
        p[0] = consts


def p_mixed_list(p):
    """mixed_list : VARIABLE
                  | NAME
                  | VARIABLE mixed_list
                  | NAME mixed_list"""
    m_l = []
    if len(p) == 2:
        m_l = {'var': [], 'const': []}
    else:
        m_l = p[2]
    if p[1][0] == '?':
        m_l['var'].insert(0, p[1])
    else:
        m_l['const'].insert(0, p[1])
    p[0] = m_l


def p_var_list(p):
    """var_list : VARIABLE
                | VARIABLE var_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        vars = p[2]
        vars.insert(0, p[1])
        p[0] = vars


def p_error(p):
    print(f'Syntax error in input {p}')


parser = yacc.yacc()
