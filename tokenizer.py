class tokens:
        
        id_dict={}
        count=0
        token_str=""
                    
        def operator_type(self,operator):
            if operator=='==':
                return "eq-op"
            elif operator=='=':
                return "assign-op"
            elif operator=='!=':
                return "noteq-op"
            elif operator=='>=':
                return "greater-eq-op"
            elif operator=='<=':
                return "smaller-eq-op"
            elif operator=='>':
                return "greater-op"
            elif operator=='<':
                return "smaller-op"
            elif operator=='*':
                return "mul-op"
            elif operator=='/':
                return "div-op"
            elif operator=='%':
                return "mod-op"
            elif operator=='+':
                return "add-op"
            elif operator=='-':
                return "sub-op"
            elif operator=='^':
                return "pow-op"
            elif operator=='&&':
                return "and-op"
            elif operator=='||':
                return "or-op"
            elif operator=='!':
                return "not-op"
            else :
                return "error"
            
        def punctuation_type(self,punctuation):
            if punctuation==';':
                return "semicolon"
            if punctuation==',':
                return "comma"
            elif punctuation=='.':
                return "dot"
            elif punctuation==':':
                return "colon"
            elif punctuation=='[':
                return "open_bracket"
            elif punctuation==']':
                return "close-bracket"
            elif punctuation=='(':
                return "open-simple-braces"
            elif punctuation==')':
                return "close-simple-braces"
            elif punctuation=='<':
                return "open-angle-bracket"
            elif punctuation=='>':
                return "close-angle-bracket"
            elif punctuation==':':
                return "close-angle-bracket"
            elif punctuation==':':
                return "close-angle-bracket"
            elif punctuation=='"':
                return "double-quotes"
            elif punctuation=="'":
                return "single-quotes"
            else :
                return "error"

        def get_identifier (self,key):
            if (key in self.id_dict ):
                type = self.id_dict[key]
                return type
            else:
                self.count=self.count+1
                value="id"+str(self.count)
                self.id_dict[key] = value
                return value

        def create_token(self,Table):
            line=1
            for i in range (0,len(Table)): 
                type=False
                if (Table[i][0]=='operator'):
                    type =self.operator_type(Table[i][1])     
                elif (Table[i][0]=='punctuation'):
                    type = self.punctuation_type(Table[i][1])
                elif (Table[i][0]=='identifier'):
                    type=self.get_identifier(Table[i][1])
                elif (Table[i]==['\n']):
                    if (Table [i-1]!=['\n'] and i>0):
                        self.token_str= self.token_str + ' line ' + str(line) + "\n"
                    line = line + 1
                    continue
                if(type):   
                  self.token_str=self.token_str +'('+ type + ',' + Table[i][1] +')'
                else:
                  self.token_str=self.token_str + '('+ Table[i][0] +',' + Table[i][1] + ')'
            self.token_str=self.token_str + " line " + str(line) + "\n"
            print("\nThe Token Generated are :\n",self.token_str)
                

        
        

