##quip##
quip is a simple, lightweight CSS post-processor that provides variable substitution while allowing you to design the way you want, with the tools you want

##Setup##
* Step 1: Move quip to your CSS Folder
	
	Place quip.py in the root folder of your project or css folder. It will automatically hunt down all your css files
* Step 2: Write a simple definitions file: quip.css
	
	Place quip.css in the same folder as quip.py and define some simple sytax:

	variable = value

	variable can be whatever you want, this is what you will put in your css.
	
	value can be whatever you want
	
	Here is a list of examples

		normalText = #999999
		normalBorder = 1px solid #cccccc
		normalRoundedBorder = border-radius:10px; -webkit-border-radius:10px; -moz-border-radius:10px; 

* Step 3: Write Valid CSS

	Write Valid CSS inserting valid comments to denote the substitutions.	

		h1{font-color:/*normalText*/;}		 		
		.myClass{font-color:/*normalText*/;}		 			
		div{			
		  border:/*normalBorder*/;		
		  /*normalRoundedBorder*/
		}

 			
* Step 4: Run quip

	Run quip from the command line:
	 			
		$ python quip.py
	 			
	Quip will find and process your css files. You will now have:
	 			
		h1{font-color:#999999/*normalText*/;}
		.myClass{font-color:#999999/*normalText*/;}
		div{
		  border:1px solid #cccccc/*normalBorder*/;
		  border-radius:10px; -webkit-border-radius:10px; -moz-border-radius:10px;/*normalRoundedBorder*/
		}

	You're Done!
	
	You can re-run quip at any time. Change a defintion, edit your css. Repeat Step 4 whenever you want.
		
##About:##
quip is a project of Robin Wallar [@freshwinded](http://twitter.com/freshwinded)

License: You may use quip under either the MIT License or the GNU General Public License (GPL) Version 2
