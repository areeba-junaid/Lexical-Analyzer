import re
class Pattern:
    
    def is_keyword(self,lexeme):
            keyword_array = ['if', 'other', 'otherwise', 'for', 'while', 'go', 'func', 'return', 'int', 'float', 'string', 'bool','print']
            if lexeme in keyword_array:
                return True
               
    def is_operator(self,lexeme):
            operator_array= ['+','-','*','%','/','^','==','!=','<=','>=','>','<','&&','||','!',"="]
            if lexeme in operator_array:
               return True

    def punctuation(self,lexeme):
            punctuator_array= ['"',"'",'(',')',']','[' ,';','.',",","\n",':','<','>']
            if lexeme in punctuator_array:
                return True

    def is_float(self,lexeme):
        is_match = re.search("^[+-][\d]+\.[\d]+$|^[\d]+\.[\d]+$|^\.[\d]+$|^[+-]\.[\d]+$",lexeme)
        if is_match:
                return True
                
            
    def identifier(self,lexeme):
            is_match = re.search("^\$[a-zA-Z0-9]+$", lexeme)
            if is_match:
                return True
                  
    def integer(self,lexeme):
            is_match = re.search("^[+-][\d]+$|^[\d]+$",lexeme)
            if is_match:
                return True
        
    def string_constant(self, lexeme):
            is_match = re.search("(\\\[tvrafb\\\]|.)", lexeme)
            if is_match:
                return True

    def is_comment (seld,lexeme):
            comment=['#','##']  
            if lexeme in comment:
                return True
    def character(self,lexeme):
        is_match = re.search("^'[a-z0-9]{1}+|[\n\t\b]{1}", lexeme)
        if is_match:
                print("The string is a valid integer")
        else:
                print("SYNTAX ERROR: string is not a valid integer")
          


