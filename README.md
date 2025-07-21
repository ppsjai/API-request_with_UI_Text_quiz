# API-request_with_UI_Text_quiz
How do we able to request API with our UI to interact our quiz-game and Request error code are in a separate file
There are 5 files in our python available and each how do we are interacting a file with  1 to another with our class method
# And i have taken API request in open trivia data base for this program you can go for there or there are plenty of  other website there

if you generate a different question if this happen means refer this docs
to avoid exampleword&#039; --> in our output text if it happens refer this  html tag
to test open browser go and search for HTML escape website and
search for html escape option and paste the text to change the word format into a normal format
for example this is the word---> exampleword&#039;
website name free-formatter.com or any-kind of website for our API request

Some Useful HTML Character Entities
Result	Description	            Name	Number
        non-breaking space	    &nbsp;	&#160;
<	    less than	            &lt;	&#60;
>	    greater than	        &gt;	&#62;
&	    ampersand	            &amp;	&#38;
"	    double quotation mark	&quot;	&#34;
'	    single quotation mark	&apos;	&#39;
¢	    cent	                &cent;	&#162;
£	    pound	                &pound;	&#163;
¥	    yen	                    &yen;	&#165;
€	    euro	                &euro;	&#8364;
©	    copyright	            &copy;	&#169;
®	    registered trademark	&reg;	&#174;
™	    trademark	            &trade;	&#8482;

in our quiz brain file
to change html escape
q_text = html.unescape(self.current_question.text)
user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ") # variable update
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Interface creation
1.theme color
2.padding 20,20
3.text, font
4.height 250 , width 300
--------------------------------------------------------------------------------------------------------------------
now applying grid
always rows will come first and then column
    0                   1
-----------------|---------------------|
                 |  score              |0 score(0,1)
-----------------|---------------------|
                 |                     |
         image   |  text was here      |   image text(1,0)
                 |                     |1
                 |                     |
                 |                     |
                 |                     |
                 |                     |
-----------------|---------------------|
   check button  | wrong button        |2  checkbutton(2,0)
                 |                     |   wrong button(2,1)
-----------------|---------------------|
