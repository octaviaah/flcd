
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     INTEGER = 258,
     WORD = 259,
     CHARACTER = 260,
     IF = 261,
     ELSE = 262,
     FOR = 263,
     WHILE = 264,
     RETURN = 265,
     CIN = 266,
     COUT = 267,
     OR = 268,
     AND = 269,
     IDENTIFIER = 270,
     CONSTANT = 271,
     ATRIB = 272,
     EQ = 273,
     NE = 274,
     LT = 275,
     LTE = 276,
     GT = 277,
     GTE = 278,
     NOT = 279,
     ADD = 280,
     SUB = 281,
     DIV = 282,
     MUL = 283,
     MOD = 284,
     ADDEQ = 285,
     SUBEQ = 286,
     DIVEQ = 287,
     MULEQ = 288,
     OPEN_CURLY_BRACKET = 289,
     CLOSED_CURLY_BRACKET = 290,
     OPEN_ROUND_BRACKET = 291,
     CLOSED_ROUND_BRACKET = 292,
     OPEN_RIGHT_BRACKET = 293,
     CLOSED_RIGHT_BRACKET = 294,
     COMMA = 295,
     DOT = 296,
     SEMI_COLON = 297,
     COLON = 298,
     SPACE = 299,
     READ_OP = 300,
     WRITE_OP = 301
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


