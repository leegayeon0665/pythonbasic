def totalScore(s1,s2,s3):
    hap = s1+s2+s3
    return hap

def averageScore(s1,s2,s3):
    return(s1+s2+s3)/3

def passfail(s1,s2,s3):
    avg = (s1+s2+s3)/3
    if avg >=60 and s1>=40 and s2>=40 and s3>=40:
        return "Pass"
    else:
        return "Fail"
    
if __name__ == '__main__':
    print(totalScore(100,34,56))

