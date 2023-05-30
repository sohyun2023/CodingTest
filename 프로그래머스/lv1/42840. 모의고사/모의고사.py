def solution(answers):
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    
    answer=[]
    
    score=[0,0,0]
    
    for i in range(len(answers)):
        ione,itwo,ithree=i%5,i%8,i%10
        if answers[i]==one[ione]:
            score[0]=score[0]+1
        if answers[i]==two[itwo]:
            score[1]=score[1]+1
        if answers[i]==three[ithree]:
            score[2]=score[2]+1
            
    for idx, num in enumerate(score):
        if num==max(score):
            answer.append(idx+1)
            
    return answer