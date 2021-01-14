import re
"""
FUNCTIONS
    compile(pattern, flags=0)
       
    escape(pattern)
      
    findall(pattern, string, flags=0)
      
    finditer(pattern, string, flags=0)
      
    fullmatch(pattern, string, flags=0)
      
    match(pattern, string, flags=0)
     
    purge()
      
    search(pattern, string, flags=0)
      
    split(pattern, string, maxsplit=0, flags=0)
     
    sub(pattern, repl, string, count=0, flags=0)
     
    
    subn(pattern, repl, string, count=0, flags=0)

    template(pattern, flags=0)
"""
exampleString="""Rohan is 16 years old Grandfather's of Mohan is 102 years old."""
age= re.findall('\d{1,3}',exampleString)
print(age)
name= re.findall('[A-Z][a-z]*',exampleString)
print(name)
