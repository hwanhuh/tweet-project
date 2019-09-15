def main():
    #유저를 읽음
    f = open("C:\\test\\cp949\\user.txt", "r")
    a = {}
    l = 0
    while True:
        user_id = f.readline()
        user_id = user_id[0:-1]
        if not user_id:
            break
        f.readline()
        name = f.readline()
        name = name[0:-1]
        tmp = user_id
        tmpn = name
        a[tmp] = tmpn
        l = l + 1
        f.readline()


    #단어를 읽음 유저-트윗수 대응관계
    f = open('C:\\test\\cp949\\word.txt', 'r')
    wdic = {}
    cntw = {}
    j = 0
    while True:
        user_id = f.readline()
        user_id = user_id[0:-1]
        if not user_id:
            break
        f.readline()
        wd = f.readline()
        wd = wd[0:-1]
        tmpi = user_id
        tmpw = wd
        if tmpw in wdic:
            wdic[tmpw] = wdic[tmpw] + [tmpi]
        else:
            wdic[tmpw] = [tmpi]
        j = j + 1
        f.readline()

    #단어를 읽음2  단어-갯수 대응
    f = open('C:\\test\\cp949\\word.txt', 'r')
    wcdic = {}
    cnti = {}
    j = 0
    while True:
        user_id = f.readline()
        user_id = user_id[0:-1]
        if not user_id:
            break
        f.readline()
        wd = f.readline()
        wd = wd[0:-1]
        tmpi = user_id
        tmpw = wd
        if tmpi in wcdic:
            wcdic[tmpi] = wcdic[tmpi] + [tmpw]
        else:
            wcdic[tmpi] = [tmpw]
        j = j + 1
        f.readline()

    # 친구를 읽음
    f = open('C:\\test\\cp949\\friend.txt', 'r')
    fdic = {}
    k = 0
    while True:
        user_id = f.readline()
        user_id = user_id[0:-1]
        if not user_id:
            break
        fi = f.readline()
        fi = fi[0:-1]
        tmpi = user_id
        tmpf = fi
        if tmpi in fdic:
            if not tmpf in fdic[tmpi]:
                fdic[tmpi] = fdic[tmpi] + [tmpf]
            else:
                k = k - 1
        else:
            fdic[tmpi] = [tmpf]
        k = k + 1
        f.readline()

    while True:
        print('0. Read data files')
        print('1. display statistics')
        print('2. Top 5 most tweeted words')
        print('3. Top 5 most tweeted users')
        print('4. Find all users who tweeted a word (e.g, 연세대)')
        print('5. Find all people who are friends of the above users')
        print('6. Delete all mentions of a word')
        print('7. Delete all users who mentioned a word')
        print('8. Find strongly connected components')
        print('9. Find shortest path')
        print('99. Quit')


        #워드에 저장된 정보를 횟수-그 횟수의 단어들 로 저장
        wcnt = []
        wc2= {}
        for tmp in wdic:
            tmpn = len(wdic[tmp])
            wcnt = wcnt + [tmpn]
            if tmpn in wc2:
                wc2[tmpn]=wc2[tmpn]+[tmp]
            else:
                wc2[tmpn]=[tmp]
        wcnt.sort()
        wwmin = wcnt[0]
        wwmax = wcnt[len(wcnt) - 1]

        #워드에 저장된 정보를 횟수-그 횟수의 유저들 로 저장
        wccnt=[]
        wc3={}
        for tmp in wcdic:
            tmpn = len(wcdic[tmp])
            wccnt = wccnt + [tmpn]
            if tmpn in wc3:
                wc3[tmpn] = wc3[tmpn] + [tmp]
            else:
                wc3[tmpn] = [tmp]
        wccnt.sort()
        wmin = wccnt[0]
        wmax = wccnt[len(wccnt) - 1]

        #친구에 저장된 정보를 저장
        fcnt=[]
        for tmp in fdic:
            tmpn=len(fdic[tmp])
            fcnt = fcnt +[tmpn]
        fcnt.sort()
        fmin=fcnt[0]
        fmax=fcnt[len(fcnt)-1]


        i=input()
        if i=='0':
            print('Total users:%s'%l)
            print('Total friendship records:%s'%k)
            print('Total tweets:%s\n'%j)
        elif i=='1':
            print('Average number of friends:%f'%(k/l))
            print('Minimum friends:%s'%fmin)
            print('Maximum number of friends:%s\n'%fmax)
            print('Average tweets per user:%f'%(j/l))
            print('Minium tweets per user:%s'%wmin)
            print('Maximum tweets per user:%s\n'%wmax)
        elif i=='2':
            print('Top 5 most tweeted words is')
            for i in range (1,6):
                wmax1 = wcnt[len(wcnt) - i]
                tmpn1=wmax1
                print(wc2[tmpn1])
        elif i=='3':
            tmp3 = []
            tmpout = []
            print('Top 5 most tweeted users is\n')
            for i in range(1, 6):
                wmax1 = wccnt[len(wccnt) - i]
                tmpn1 = wmax1
                for tmp in wc3[tmpn1]:
                    if len(tmpout) < 5:
                        tmpout=tmpout+[tmp]
                        tmp3 = tmp3 + [tmp]
            for tmp in tmpout:
                print('%s'%a[tmp])
            print('')
        elif i=='4':
            tmpword=input()
            if tmpword in wdic:
                print('Users who tweeted a word is')
                for tmp in wdic[tmpword]:
                    print('%s'%a[tmp])
                tmp4=wdic[tmpword]
                print('')
            else:
                print('Users who tweeted %s not exist' % tmpword)
        elif i=='5':
            tmplist=[]
            tmpout=[]
            tmplist=tmp4+tmp3
            for tmp in tmplist:
                tmpout=tmpout+fdic[tmp]
            print('People who is friend of the above user are')
            for tmp in tmpout:
                print('%s'%a[tmp])
        elif i=='6':
            tmpword=input()
            if tmpword in wdic:
                tmp=wdic[tmpword]
                j=j-len(tmp)
                for tmpw in tmp:
                    wcdic[tmpw].remove(tmpword)
                print('Delete all mentions of a word %s complete.\n'%tmpword)
            else:
                print('%s not exist'%tmpword)
        elif i=='7':
            tmpword = input()
            tmp=wdic[tmpword]
            tmpl=[]
            for item in tmp:
                if item in wcdic:
                    tmpl = tmpl + wcdic[item]
                    j=j-len(wcdic[item])
                    del wcdic[item]
            tmpl2=list(set(tmpl))
            for tmpw in tmpl2:
                for tmpu in tmp:
                    if tmpu in wdic[tmpw]:
                        wdic[tmpw].remove(tmpu)
            tmpl=[]
            for tmpu in tmp:
                tmpl=tmpl+fdic[tmpu]
                k=k-len(fdic[tmpu])
            tmpl2 = list(set(tmpl))
            for tmpu in tmpl2:
                for tmpu1 in tmp:
                    if tmpu1 in fdic[tmpu]:
                        fdic[tmpu].remove(tmpu1)
                        k=k-1
            print('Delete all users who mentioned a word %s complete.\n'%tmpword)
        elif i=='8':
            print('Strongly connected component is\n')
        elif i=='9':
            print('Shortest path is\n')
        elif i=='99':
            break

main()
