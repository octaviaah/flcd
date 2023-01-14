%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%token INTEGER
%token WORD
%token CHARACTER
%token IF
%token ELSE
%token FOR
%token WHILE
%token RETURN
%token CIN
%token COUT
%token OR
%token AND

%token IDENTIFIER
%token CONSTANT

%token ATRIB
%token EQ
%token NE
%token LT
%token LTE
%token GT
%token GTE
%token NOT

%left '+' '-' '/' '*' '%'

%token ADD
%token SUB
%token DIV
%token MUL
%token MOD
%token ADDEQ
%token SUBEQ
%token DIVEQ
%token MULEQ

%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET


%token COMMA
%token DOT
%token SEMI_COLON
%token COLON
%token SPACE

%token READ_OP
%token WRITE_OP

%start program

%%
program : stmtlist
	;
declaration :  type IDENTIFIER
	    ;
type :  INTEGER | WORD | typeTemp
	   ;
typeTemp : /*Empty*/ | OPEN_RIGHT_BRACKET CONSTANT CLOSED_RIGHT_BRACKET 
	 ;
cmpdstmt : OPEN_CURLY_BRACKET stmtlist CLOSED_CURLY_BRACKET
	 ;
stmtlist :  stmt stmtTemp
	 ;
stmtTemp : /*Empty*/ | stmtlist
	 ;
stmt :  simplstmt SEMI_COLON | structstmt
     ;
simplstmt :  assignstmt | iostmt | declaration
	 ; 
structstmt :  cmpdstmt | ifstmt | whilestmt | forstmt
	   ;
ifstmt :  IF OPEN_ROUND_BRACKET boolean_condition CLOSED_ROUND_BRACKET stmtlist tempIf
       ;
tempIf : /*Empty*/ | ELSE stmtlist
       ;
forstmt :  FOR forheader cmpdstmt
       ;	
forheader :  OPEN_ROUND_BRACKET INTEGER assignstmt SEMI_COLON OPEN_ROUND_BRACKET boolean_condition CLOSED_ROUND_BRACKET SEMI_COLON assignstmt CLOSED_ROUND_BRACKET
	  ;
whilestmt :  WHILE OPEN_ROUND_BRACKET boolean_condition CLOSED_ROUND_BRACKET cmpdstmt
	  ;
assignstmt :  IDENTIFIER ATRIB expression
	   ;
expression : arithmetic2 arithmetic1
	   ;
arithmetic1 : ADD arithmetic2 arithmetic1 | SUB arithmetic2 arithmetic1 | /*Empty*/
	    ;
arithmetic2 : multiply2 multiply1
	    ;
multiply1 : MUL multiply2 multiply1 | DIV multiply2 multiply1 | /*Empty*/ 
	  ;
multiply2 : OPEN_ROUND_BRACKET expression CLOSED_ROUND_BRACKET | CONSTANT | IDENTIFIER | IndexedIdentifier
	  ;
IndexedIdentifier :  IDENTIFIER OPEN_RIGHT_BRACKET CONSTANT CLOSED_RIGHT_BRACKET
		  ;
iostmt :  CIN READ_OP IDENTIFIER | COUT WRITE_OP IDENTIFIER | COUT WRITE_OP CONSTANT
      ; 
condition : expression GT expression |
	 expression GTE expression | 
	 expression LT expression |
	 expression LTE expression | 
	 expression EQ expression |
	 expression NE expression
	  ;
boolean_condition : condition boolean_cond_temp
		  ;
boolean_cond_temp : /*Empty*/ | AND boolean_condition | OR boolean_condition
	;
%%
yyerror(char *s)
{
	printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
	if(argc>1) yyin :  fopen(argv[1], "r");
	if(argc>2 && !strcmp(argv[2], "-d")) yydebug: 1;
	if(!yyparse()) fprintf(stderr, "\tO.K. \n");
}