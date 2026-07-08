maths = int(input("Entar marks: "))
eng = int(input("Entar marks: "))
swa = int(input("Entar marks: "))
sci = int(input("Entar marks: "))
sos = int(input("Entar marks: "))

def total_marks(maths,eng,swa,sci,sos):
    total=maths + eng + swa + sci + sos
    return total

print(total_marks(maths,eng,swa,sci,sos))

def average(maths,eng,swa,sci,sos):
    marks = (maths + eng + swa + sci + sos)//5
    return marks

print(average(maths,eng,swa,sci,sos))

def grade(maths,eng,swa,sci,sos):
    total = total_marks(maths, eng, swa, sci, sos)
    
    if total > 79:
        gpa='A'
    elif total >= 60:
        gpa='B'
    elif total >= 49:
        gpa='C'
    elif total >= 40:
        gpa='D'
    else:
        gpa='E'
    return gpa

print(grade(maths,eng,swa,sci,sos))
    