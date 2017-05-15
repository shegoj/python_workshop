#!/usr/bin/python

__author__ = "Segun Ojewale"
__version__ = "$Revision: beta $"
__date__ = "$Date: 2016/07/05 $"
__copyright__ = "..."
__license__ = "..."


# Import modules for CGI handling 
import cgi, cgitb,re,sys 

# define Exceptions

class TranslationException (Exception): pass


class DigitsTranslation ():

    ''' digits dict'''

    digits_map ={
        1: 'okan',
        2: 'eji',
        3: 'eta',
        4: 'erin',
        5: 'arun',
        6: 'efa',
        7: 'eje',
        8: 'ejo',
        9: 'esan',
        10: 'ewa',
        11: 'ookanla',
        12: 'ejila',
        13: 'etala',
        14: 'erinla',
        15: 'eedogun',
        20: 'ogun',
        30: 'ogbon',
        40:'ogoji',
        50:'aadota',
        200:'igba',
        300: 'oodunrun',
        400: 'irinwo',
        #500: 'eedegbeta',


    }

    #  X_LESS_THAN_200 = "DIN NI IGBA"  #X DIN NI IGBA
    X_MORE_THAN = " LE NI"
    X_LESS_THAN = " DIN NI"

    # 200s Translations
    TWO_HUNDREDS_MUL = " Egbe "
    PRE_TWO_HUNDREDS_MUL = " Eedegbe "

    # 20s Translations
    TWENTY_MUL = " OGO LONA "
    PRE_TWENTY_MUL = " AADO LONA "

    # ThOUSANDS AND MILLIONS
    THOUSAND_MILL = ("EGBERUN " ,"EGBERUN LONA EGBERUN ")
    THOUS_MILL_ADD_JOIN_PT = 11 # point to start adding 'LONA' to million and thousand. e.g milionu lona metala, milionu kan

    #  LINKERS
    LONA = " LONA "
    AND_LINK = " ati "

    # eta = Meta , arun = Marun etc
    M_PREFIX = "m"

    # Digit holders
    MILLION_DIGIT = 0
    THOUSAND_DIGIT = 0
    OTHER_DIGIT = 0




    def __init__(self):
        pass
    

    #  Rounder to the nearest 10s, 100s etc
    
    def figure_rounder (self, digit, rounder, REM_CHK = 5):
        rem = digit % rounder

        if rem < REM_CHK:
            round_value = int(digit / rounder) * rounder
        else:
            round_value = int((digit + rounder) / rounder) * rounder

        return  round_value

    def translation_engine (self, digit, m_prefix = False):
        
        unit_joiner = None
        unit_in_yoruba = ""
        ten_in_yoruba = ""
        hundreds_in_yoruba = ""
        unit = 0
        multiples_of_twenty = 1

        result = None

        if digit in self.digits_map:    # quick lookup in case entry exists in map

            if m_prefix and digit > 1 and digit < 20:
                return self.M_PREFIX + self.digits_map[digit]  ## instead of saying eji, say Meji, Meta, Merin etc
            else:
                return self.digits_map[digit]

        if digit < 194:

            unit = digit % 10
            tens = self.figure_rounder (digit, 10) # round to the nearest tens

            if tens < digit : #
                unit_joiner = self.X_MORE_THAN

            elif tens > digit:
                unit = tens - digit
                unit_joiner = self.X_LESS_THAN

            ten_in_yoruba = self.digits_map [tens] if tens in self.digits_map else None

            if ten_in_yoruba is None:  # use 20 multiple rule
                multiples_of_twenty = tens // 20

                if (tens % 20) == 0:
                    ten_in_yoruba = self.TWENTY_MUL

                else:
                    multiples_of_twenty += 1
                    ten_in_yoruba = self.PRE_TWENTY_MUL

                ten_in_yoruba = ten_in_yoruba + self.digits_map[multiples_of_twenty]
            # print("multiple of twenty for digit {} is {}".format(digit, multiples_of_twenty))

            if unit != 0 :
                unit_in_yoruba = self.M_PREFIX  + self.digits_map[unit]

            result = "{} {} {}".format(unit_in_yoruba, unit_joiner, ten_in_yoruba)

        elif digit < 200:
            digit_proximity = 200
            diff_proximity = digit_proximity - digit
            unit_joiner = self.X_LESS_THAN
            ten_in_yoruba =  self.digits_map [digit_proximity]
            unit_in_yoruba = self.M_PREFIX + self.digits_map[diff_proximity]

            result = "{} {} {}".format(unit_in_yoruba, unit_joiner, ten_in_yoruba)

        else:  # this applies to values north of 200
            base_analyser = 200  # this will be use for digit division etc

            hundreds_ = digit // 100
            hundreds = (digit // 100) * 100  # get the Hundredths only
            unit_joiner = ''
            unit = digit - (hundreds_ * 100)  # GET TENS AND UNITS

            hundreds_in_yoruba = self.digits_map[
                hundreds] if hundreds in self.digits_map else None  # Lookup mapping table, see if there is a match

            if hundreds_in_yoruba is None:  # If no match,  use 200 multiple rule i.e EGBE OR EEDEGBE FOR 500 and above

                multiples_of_two_hundred = digit // base_analyser
                remainder_ = digit % base_analyser

                if remainder_ == 0:
                    hundreds_in_yoruba = self.TWO_HUNDREDS_MUL
                else:
                    hundreds_in_yoruba = self.PRE_TWO_HUNDREDS_MUL
                    multiples_of_two_hundred += 1

                hundreds_in_yoruba = hundreds_in_yoruba + self.digits_map[multiples_of_two_hundred]

            # print("passing on {} {} {}".format(hundreds, base_analyser, unit))

            if unit != 0:
                unit_in_yoruba = self.translation_engine(unit, True)
                unit_joiner = self.X_MORE_THAN  # SET `LE NI`

            result = "{} {} {}".format(hundreds_in_yoruba, unit_joiner, unit_in_yoruba)

        return result


    # A wrapper around main translation function. This is for thousands and millions translation
    def tm_wrapper (self, digit, the_type = 'T'):

        value_ = ""
        joiner = ""

        if the_type == 'T':  # thousand
            value_ = self.THOUSAND_MILL [0]
        else:
            value_ = self.THOUSAND_MILL[1]

        joiner = self.LONA if digit > self.THOUS_MILL_ADD_JOIN_PT else ""
        digit_translation = self.translation_engine(digit, True)
	
	# special case for 1M and 1TH, can do a better fix than this :-)
        if digit_translation.strip().lower() == 'okan':
          digit_translation = digit_translation.replace("okan","kan")
        value_ += joiner + digit_translation

        return value_

    def processInput (self, digit):

        self.MILLION_DIGIT = digit // 1000000
        self.THOUSAND_DIGIT = ((digit % 1000000) // 1000)
        self.OTHER_DIGIT =  ((digit % 1000000) %  1000)
        
        million_exists = False
        thousands_exists = False
        
        MIL= ""
        TH = ""
        others = ""

        
        #translate()
        
        if self.MILLION_DIGIT != 0 :
            million_exists = True
            MIL= self.tm_wrapper(self.MILLION_DIGIT, 'M')
        
        if self.THOUSAND_DIGIT  != 0:
            thousands_exists = True
            TH = self.tm_wrapper(self.THOUSAND_DIGIT, 'T')
            if million_exists :
                TH = self.AND_LINK +  TH
                
        if self.OTHER_DIGIT  != 0:
            others = self.translation_engine(self.OTHER_DIGIT)
            if thousands_exists or million_exists :
                others = self.AND_LINK +  others

        #print("{} :=>  {} {} {} ".format(digit, self.MILLION_DIGIT, self.THOUSAND_DIGIT, self.OTHER_DIGIT))
        #print("{} ".format(MIL + TH + others))

        #return digit, apply_fluency(MIL + TH + others)
        return apply_fluency(MIL + TH + others)
        


def apply_fluency (translation):

    #apply_fluencyed_translation = re.sub("(OGO LONA M?\w)", "OGO", "%s" % translation)
    translation = translation.upper()
    translation = re.sub("(NONE)", r'', "%s" % translation)
    translation = re.sub("(OGO LONA M?\w)", "OGO", "%s" % translation)
    translation = re.sub("(AADO LONA M?\w)", "AADO", "%s" % translation)
    translation = re.sub("(EGBE M?\w)", "EGBE", "%s" % translation)
    translation = re.sub("(\s\s)", r' ', "%s" % translation) ## replace double spaces with single
    translation = re.sub("(NI)\s+(I)", r"N'\2", "%s" % translation) # 
    translation = re.sub("(NI)\s+([A,E,O])", r"L'\2", "%s" % translation) # 
    translation = translation.strip()

    return translation


################# Now lets wrap it in HTML ####################

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
numeral = form.getvalue('numeral')
#numeral = sys.argv [1]

value_ = ""

try:
    translate_ = DigitsTranslation()
    numeral_without_comma = numeral.replace(',','') 
    figure_ = int (numeral_without_comma)
    value_ = translate_.processInput(figure_)

except (Exception) as e:
    value_ = "TRY"

######## lets do a simple web template

template = """
<HEAD>
<TITLE></TITLE>
</HEAD>
<BODY BGCOLOR="WHITE">
<CENTER>
<H1>A Simple Arabic Numerals to Yourba Translator</H1>
  <IMG SRC="http://adwlab-team5.wikispaces.com/file/view/Bata_Drms.jpg/275832498/Bata_Drms.jpg" height="200" width="200">
  <H4>By Segun Oje</H4><br> 
This is just a quick job so not 100% yet.
Thanks to Kola Olatubosun for a quick crash course on the subject

<BR><BR>

<form action="simple.py">
  <b>Enter Digit:</b> <input type="text" name="numeral" value="{}" autocomplete="off" maxlength="8"><br>
  <br><input type="submit" value="Translate">
</form>

<br><br><br> <b>{} : {}</b>

</CENTER>
<br><br><br> <a href="/simple.txt">check source code if you are curious</a>

</BODY>
</HTML>

"""


print ("Content-type:text/html\r\n\r\n ")
print (template.format(numeral, numeral, value_))
