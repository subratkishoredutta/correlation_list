def corrlist(limit,source_data):
    i=0
    j=0
    highcorr=list()
    corlist=list(source_data)
    cordict=dict()
    for i in range(0,len(corlist)):
        cordict[i]= corlist[i]
    
    correlation=source_data.corr()
    n = limit
    for i in range(0,len(cordict)):
        for j in range(1,len(cordict)):
            if (correlation[cordict[i]][cordict[j]] > n) :
                if (cordict[i]!=cordict[j]) and ((cordict[j],cordict[i]) in highcorr)==False :
                    highcorr.append((cordict[i],cordict[j]))
    return(highcorr) 
    print(highcorr)
