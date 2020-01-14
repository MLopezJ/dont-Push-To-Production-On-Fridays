
posterUp =   '|￣￣￣￣￣￣￣￣￣￣￣|'
posterDwon = '|______________________|'
warningMessage = "     Don't push\n     to production"
welcomeMessage = "Happy Friday!!" #weekend its almost here
lineBreak = '\n'
rabbit = " (\__/) ||\n (•ㅅ•) ||\n/ 　  づ"

def drawing():
    drawing = ''
    drawing += welcomeMessage + lineBreak
    drawing += lineBreak
    drawing += posterUp + lineBreak
    drawing += warningMessage +lineBreak
    drawing += posterDwon + lineBreak
    drawing += rabbit + lineBreak
    print(drawing)


    return drawing
    
drawing()