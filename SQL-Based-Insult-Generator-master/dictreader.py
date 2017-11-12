import fileinput
import sys
import MySQLdb

infile = open("halfdict.txt")
db = MySQLdb.connect("localhost", "root", "", "phraser")
cursor = db.cursor()

def check(line, d):
    depth = d
    inline = line
    
    with db:
        if not "x" in inline[-depth:]:
            depth +=1
            check(inline, depth)
        elif "x" in inline[-depth:]:
            if "N" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'noun')" %inline.replace(' ', '')[:-depth].upper())
            if "p" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'plural')" %inline.replace(' ', '')[:-depth].upper())
            if "h" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'noun_phrase')" %inline.replace(' ', '')[:-depth].upper())
            if "V" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'verb_participle')" %inline.replace(' ', '')[:-depth].upper())
            if "t" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'verb_transitive')" %inline.replace(' ', '')[:-depth].upper())
            if "i" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'verb_intransitive')" %inline.replace(' ', '')[:-depth].upper())
            if "A" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'adjective')" %inline.replace(' ', '')[:-depth].upper())
            if "v" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'adverb')" %inline.replace(' ', '')[:-depth].upper())
            if "C" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'conjunction')" %inline.replace(' ', '')[:-depth].upper())
            if "P" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'preposition')" %inline.replace(' ', '')[:-depth].upper())
            if "!" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'interjection')" %inline.replace(' ', '')[:-depth].upper())
            if "r" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'pronoun')" %inline.replace(' ', '')[:-depth].upper())
            if "D" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'definite_article')" %inline.replace(' ', '')[:-depth].upper())
            if "I" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'indefinite_article')" %inline.replace(' ', '')[:-depth].upper())
            if "o" in inline[-depth:]:
                cursor.execute("insert into word(word, type) values('%s', 'nominative')" %inline.replace(' ', '')[:-depth].upper())
        else:  print "undefined word"
    print inline.replace(' ', '')[:-depth].upper()   
                    
    
def main():
    print "test"
    rowNums = 0
    line = infile.readline()
    while line:
        inline = infile.readline()
        check(inline, 2)
        rowNums += 1
    cursor.close()
    print rowNums

    
if __name__ == '__main__':
    main()  
