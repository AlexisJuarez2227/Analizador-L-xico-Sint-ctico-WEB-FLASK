
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNARleftSUMARESTAleftMULTDIVrightUMINUSAND ASIGNAR CADENA CIN COMA COMDOB CORDER CORIZQ COUT DISTINTO DIV ENDL ENTERO GET IDENTIFICADOR IGUAL INCLUDE INT LLADER LLAIZQ MAYORDER MAYORIGUAL MAYORIZQ MAYORQUE MENORIGUAL MENORQUE MIENTRAS MINUSMINUS MODULO MULT NAMESPACE NOT NUMERAL OR PARA PARDER PARIZQ PLUSPLUS POTENCIA PUNTOCOMA RESTA RETURN SI SINO STD SUMA USING VOIDdeclaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMAdeclaracion : expresionexpresion : expresion SUMA expresion\n                 | expresion RESTA expresion\n                 | expresion MULT expresion\n                 | expresion DIV expresion\n                 | expresion POTENCIA expresion\n                 | expresion MODULO expresionexpresion : RESTA expresion %prec UMINUSexpresion : PARIZQ expresion PARDER\n                 | LLAIZQ expresion LLADER\n                 | CORIZQ expresion CORDERexpresion : ENTEROexpresion : CADENAexpresion : IDENTIFICADOR'
    
_lr_action_items = {'IDENTIFICADOR':([0,4,5,6,7,10,11,12,13,14,15,16,],[2,18,18,18,18,18,18,18,18,18,18,18,]),'RESTA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,],[4,-15,12,4,4,4,4,-13,-14,4,4,4,4,4,4,4,-9,-15,12,12,12,12,-3,-4,-5,-6,12,12,-10,-11,-12,]),'PARIZQ':([0,4,5,6,7,10,11,12,13,14,15,16,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'LLAIZQ':([0,4,5,6,7,10,11,12,13,14,15,16,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'CORIZQ':([0,4,5,6,7,10,11,12,13,14,15,16,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'ENTERO':([0,4,5,6,7,10,11,12,13,14,15,16,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'CADENA':([0,4,5,6,7,10,11,12,13,14,15,16,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'$end':([1,2,3,8,9,17,18,23,24,25,26,27,28,29,30,31,32,],[0,-15,-2,-13,-14,-9,-15,-3,-4,-5,-6,-7,-8,-10,-11,-12,-1,]),'ASIGNAR':([2,],[10,]),'SUMA':([2,3,8,9,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,],[-15,11,-13,-14,-9,-15,11,11,11,11,-3,-4,-5,-6,11,11,-10,-11,-12,]),'MULT':([2,3,8,9,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,],[-15,13,-13,-14,-9,-15,13,13,13,13,13,13,-5,-6,13,13,-10,-11,-12,]),'DIV':([2,3,8,9,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,],[-15,14,-13,-14,-9,-15,14,14,14,14,14,14,-5,-6,14,14,-10,-11,-12,]),'POTENCIA':([2,3,8,9,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,],[-15,15,-13,-14,-9,-15,15,15,15,15,-3,-4,-5,-6,15,15,-10,-11,-12,]),'MODULO':([2,3,8,9,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,],[-15,16,-13,-14,-9,-15,16,16,16,16,-3,-4,-5,-6,16,16,-10,-11,-12,]),'PARDER':([8,9,17,18,19,23,24,25,26,27,28,29,30,31,],[-13,-14,-9,-15,29,-3,-4,-5,-6,-7,-8,-10,-11,-12,]),'LLADER':([8,9,17,18,20,23,24,25,26,27,28,29,30,31,],[-13,-14,-9,-15,30,-3,-4,-5,-6,-7,-8,-10,-11,-12,]),'CORDER':([8,9,17,18,21,23,24,25,26,27,28,29,30,31,],[-13,-14,-9,-15,31,-3,-4,-5,-6,-7,-8,-10,-11,-12,]),'PUNTOCOMA':([8,9,17,18,22,23,24,25,26,27,28,29,30,31,],[-13,-14,-9,-15,32,-3,-4,-5,-6,-7,-8,-10,-11,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,4,5,6,7,10,11,12,13,14,15,16,],[3,17,19,20,21,22,23,24,25,26,27,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> IDENTIFICADOR ASIGNAR expresion PUNTOCOMA','declaracion',4,'p_declaracion_asignar','analizadores.py',195),
  ('declaracion -> expresion','declaracion',1,'p_declaracion_expr','analizadores.py',199),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_operaciones','analizadores.py',203),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_operaciones','analizadores.py',204),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion_operaciones','analizadores.py',205),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_operaciones','analizadores.py',206),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_operaciones','analizadores.py',207),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_operaciones','analizadores.py',208),
  ('expresion -> RESTA expresion','expresion',2,'p_expresion_uminus','analizadores.py',223),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_grupo','analizadores.py',227),
  ('expresion -> LLAIZQ expresion LLADER','expresion',3,'p_expresion_grupo','analizadores.py',228),
  ('expresion -> CORIZQ expresion CORDER','expresion',3,'p_expresion_grupo','analizadores.py',229),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','analizadores.py',233),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','analizadores.py',237),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion_nombre','analizadores.py',241),
]
