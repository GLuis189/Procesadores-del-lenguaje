
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSrightUPLUSUMINUSEQUALS FLOAT FLOAT_VAL ID INT INT_VAL MINUS PLUS SEMICOLON\n    program : statement\n            | empty\n    \n    statement : content SEMICOLON\n              | content SEMICOLON statement\n    \n    content : declare\n            | assign\n            | expression\n    \n    declare : INT ID\n            | FLOAT ID\n    \n    assign : ID EQUALS expression\n    \n    expression : INT_VAL\n                | FLOAT_VAL\n                | expression PLUS expression\n                | expression MINUS expression \n                | PLUS expression %prec UPLUS\n                | MINUS expression %prec UMINUS\n    \n    empty :\n    '
    
_lr_action_items = {'$end':([0,1,2,3,15,23,],[-17,0,-1,-2,-3,-4,]),'INT':([0,15,],[8,8,]),'FLOAT':([0,15,],[10,10,]),'ID':([0,8,10,15,],[9,18,20,9,]),'INT_VAL':([0,13,14,15,16,17,19,],[11,11,11,11,11,11,11,]),'FLOAT_VAL':([0,13,14,15,16,17,19,],[12,12,12,12,12,12,12,]),'PLUS':([0,7,11,12,13,14,15,16,17,19,21,22,24,25,26,],[13,16,-11,-12,13,13,13,13,13,13,-15,-16,-13,-14,16,]),'MINUS':([0,7,11,12,13,14,15,16,17,19,21,22,24,25,26,],[14,17,-11,-12,14,14,14,14,14,14,-15,-16,-13,-14,17,]),'SEMICOLON':([4,5,6,7,11,12,18,20,21,22,24,25,26,],[15,-5,-6,-7,-11,-12,-8,-9,-15,-16,-13,-14,-10,]),'EQUALS':([9,],[19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,15,],[2,23,]),'empty':([0,],[3,]),'content':([0,15,],[4,4,]),'declare':([0,15,],[5,5,]),'assign':([0,15,],[6,6,]),'expression':([0,13,14,15,16,17,19,],[7,21,22,7,24,25,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','e_p2.py',74),
  ('program -> empty','program',1,'p_program','e_p2.py',75),
  ('statement -> content SEMICOLON','statement',2,'p_statement','e_p2.py',81),
  ('statement -> content SEMICOLON statement','statement',3,'p_statement','e_p2.py',82),
  ('content -> declare','content',1,'p_content','e_p2.py',88),
  ('content -> assign','content',1,'p_content','e_p2.py',89),
  ('content -> expression','content',1,'p_content','e_p2.py',90),
  ('declare -> INT ID','declare',2,'p_declare','e_p2.py',96),
  ('declare -> FLOAT ID','declare',2,'p_declare','e_p2.py',97),
  ('assign -> ID EQUALS expression','assign',3,'p_assign','e_p2.py',103),
  ('expression -> INT_VAL','expression',1,'p_expression','e_p2.py',109),
  ('expression -> FLOAT_VAL','expression',1,'p_expression','e_p2.py',110),
  ('expression -> expression PLUS expression','expression',3,'p_expression','e_p2.py',111),
  ('expression -> expression MINUS expression','expression',3,'p_expression','e_p2.py',112),
  ('expression -> PLUS expression','expression',2,'p_expression','e_p2.py',113),
  ('expression -> MINUS expression','expression',2,'p_expression','e_p2.py',114),
  ('empty -> <empty>','empty',0,'p_empty','e_p2.py',121),
]