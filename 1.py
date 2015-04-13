def eurjpy14a():
     hh[-1]=hh[-1]+1;yg[-1]=800*2;v40[-1]=64;v78[-1]=v78[-1]+1;
     if hh5[-1]>105: bb[-1]=0;bb2[-1]=1;
     if hh6[-1]>105: bb1[-1]=0;bb12[-1]=1;
     massiv=eurjp[-20-1:-1];ma[-1]=max(massiv);
     inn4[-1]=massiv.index(ma[-1]);mi[-1]=min(massiv);inn3[-1]=massiv.index(mi[-1]);massiv=eurjp[-20*2-1:-1];maa=max(massiv);
     inna4[-1]=massiv.index(maa);mia=min(massiv);inna3[-1]=massiv.index(mia);
     if len(eurjp)<800*2: yg[-1]=len(eurjp)-1;
     massiv=eurjp[-yg[-1]-1:-1]; ma1=max(massiv);inn41[-1]=massiv.index(ma1);mi1=min(massiv);inn31[-1]=massiv.index(mi1);
     if (eurjp[-1-yg[-1]+inn41[-1]]/eurjp[-1]>1.01)or(eurjp[-1]/eurjp[-1-yg[-1]+inn31[-1]]>1.01): v40[-1]=78;
     if ((v1[-1]==1)and(eurjp[-1]/eurjp[-hh3[-1]-1]>1.0016)and(hh1[-1]>2)):
      cancel();f6.append(0);t6.append(0);vu.append(11);hh1[-1]=0;v1[-1]=0;v6[-1]=0;cc1.append(0);cc.append(0);yt[-1]=0;ct[-1]=0;
     if ((v1[-1]==2)and(eurjp[-1]/eurjp[-hh3[-1]-1]<0.9984)and(hh1[-1]>2)):
      cancel();f6.append(0);t6.append(0);vu.append(22);hh1[-1]=0;v1[-1]=0;v6[-1]=0;cc1.append(0);cc.append(0);yt[-1]=0;ct[-1]=0;
     if ((eurjp[-1]/eurjp[-hh10[-1]]>1.0017)and(hh1[-1]>v40[-1])and(f6[-1]==1)and(v1[-1]!=1)):
      vv.append(0);vu.append(20);cancel();
      cancel();create("buy");hh3.append(1);yt[-1]=0;hh10.append(1);hh1[-1]=0;bb1[-1]=0;bb[-1]=0;v78[-1]=100;f6.append(0);t6.append(1);v1[-1]=2;ct[-1]=0;
      if ((hh60[-1]==1+1)and(bb12[-1]==0)): yt[-1]=2;
     if ((eurjp[-1]/eurjp[-hh10[-1]]<0.9983)and(hh1[-1]>v40[-1])and(t6[-1]==1)and(v1[-1]!=2)):
      vv.append(0);vu.append(10);cancel();
      cancel();create("sell");hh3.append(1);yt[-1]=0;hh1[-1]=0;hh10.append(1);bb1[-1]=0;bb[-1]=0;v78[-1]=100;f6.append(1);t6.append(0);v1[-1]=1;ct[-1]=0;
      if ((hh50[-1]==1+1)and(bb2[-1]==0)): yt[-1]=1;
     if (eurjp[-1-hh6[-1]]/eurjp[-1]>1.0001)and(bb1[-1]==1)and(hh6[-1]<6): st1[-1]=0;
     if (bb[-1]==1)and(eurjp[-1]/eurjp[-1-hh5[-1]]>1.0001)and(hh5[-1]<6): st[-1]=0;
     if (eurjp[-1-hh6[-1]]/eurjp[-1]>1.00019)and(bb1[-1]==1)and(hh6[-1]<13): stt1[-1]=0;
     if (bb[-1]==1)and(eurjp[-1]/eurjp[-1-hh5[-1]]>1.00019)and(hh5[-1]<13): stt[-1]=0;
     if (eurjp[-1-hh6[-1]]/eurjp[-1]>1.0003)and(bb1==1)and(hh6[-1]<71): sst1=0;
     if (bb[-1]==1)and(eurjp[-1]/eurjp[-1-hh5[-1]]>1.0003)and(hh5[-1]<71): sst=0;
     if ((eurjp[-1]/eurjp[-1-yg[-1]+inn31[-1]]<1.014)and(bb[-1]==1)and((hh50[-1]>52)or(hh50[-1]<2))and(((hh5[-1]==5)and(st[-1]==1))or((hh5[-1]==12)and(stt[-1]==1))))and(v78[-1]>70):
      if (f6[-1]!=1)and(((hh4[-1]>ae[-1])and(((hh4[-1]-hh6[-1])>aq[-1])or(hh6[-1]>aq[-1]))and(((hh4[-1]-hh5[-1])>aq[-1])or(hh5[-1]>aq[-1])))):
       dunno[-1]=1;v78[-1]=0;  
     if ((eurjp[-1-yg[-1]+inn41[-1]]/eurjp[-1]<1.014)and(bb1[-1]==1)and((hh60[-1]>52*ak)or(hh60[-1]<2))and(((hh5[-1]==5)and(st1[-1]==1))or((hh6[-1]==12)and(stt1[-1]==1))))and(v78[-1]>70):
      if (t6[-1]!=1)and(((hh4[-1]>ae[-1])and(((hh4[-1]-hh5[-1])>aq[-1])or(hh5[-1]>aq[-1]))and(((hh4[-1]-hh6[-1])>aq[-1])or(hh6[-1]>aq[-1])))):
       dunno[-1]=2;v78[-1]=0;
