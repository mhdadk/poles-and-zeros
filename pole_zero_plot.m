sys = zpk([0,-0.5i,0.5i],[-0.5 + 1.5i,-0.5 - 1.5i],1);
pzmap(sys);
xlim([-3,3]);
ylim([-3,3]);