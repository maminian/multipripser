run blah.py
ax2.cla()
ax2.hist(errs,bins=np.linspace(-eps,eps,40))
ax2.grid()
ax2.cla()
ax2.hist(errs,bins=np.linspace(-eps,eps,40))
ax2.set_yscale('log')
ax2.set_ylim([10**1,10**7])
ax2.set_xticks([-eps,-eps/2,0,eps/2,eps])
ax2.xaxis.grid(c='k')
%history -f blah2.py
