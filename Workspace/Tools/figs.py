import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Output bundles, resolved relative to the repo root (this file lives in Workspace/Tools/).
ROOT=Path(__file__).resolve().parents[2]
MOD=ROOT/"content/modules/encodings"
SNK=ROOT/"content/snacks/charts-are-encodings"
for d in (MOD,SNK): d.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.size":12,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","axes.facecolor":"white"})

cats=["A","B","C","D","E"]; vals=[3,7,5,9,2]

# 1. Same numbers, four magnitude channels (core page)
fig,axs=plt.subplots(1,4,figsize=(12,3.2))
ax=axs[0]; ax.scatter(cats,vals,s=60,color="#333"); ax.set_ylim(0,10); ax.set_title("position")
ax=axs[1]; ax.bar(cats,vals,color="#777",width=.4); ax.set_ylim(0,10); ax.set_title("length")
ax=axs[2]; ax.scatter(cats,[1]*5,s=[v*90 for v in vals],color="#333"); ax.set_ylim(0,2); ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.set_title("area")
ax=axs[3]
grays=[str(0.9-0.08*v) for v in vals]
ax.bar(cats,[1]*5,color=grays,width=.7,edgecolor="#999"); ax.set_ylim(0,2); ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.set_title("color (luminance)")
fig.suptitle("The same five numbers (A=3, B=7, C=5, D=9, E=2), four different channels",y=1.03)
fig.tight_layout(); fig.savefig(f"{MOD}/four-channels.png",dpi=150,bbox_inches="tight"); plt.close(fig)

# 2. Line vs dot, same data (snack)
x=np.arange(1,9); y=np.array([4,6,5,8,7,9,6,7])
fig,axs=plt.subplots(1,2,figsize=(10,3.4),sharey=True)
axs[0].plot(x,y,"-o",color="#2266aa"); axs[0].set_title("line chart"); axs[0].set_ylim(0,10)
axs[1].scatter(x,y,color="#2266aa"); axs[1].set_title("dot chart")
for a in axs: a.set_xticks(x)
fig.tight_layout(); fig.savefig(f"{SNK}/line-vs-dot.png",dpi=150,bbox_inches="tight"); plt.close(fig)

# 3. Dot / lollipop / bar (snack)
fig,axs=plt.subplots(1,3,figsize=(11,3.2),sharey=True)
axs[0].scatter(cats,vals,color="#2266aa",s=55); axs[0].set_title("dot chart"); axs[0].set_ylim(0,10)
axs[1].vlines(cats,0,vals,color="#2266aa",lw=2); axs[1].scatter(cats,vals,color="#2266aa",s=55); axs[1].set_title("“lollipop” chart")
axs[2].bar(cats,vals,color="#2266aa",width=.55); axs[2].set_title("bar chart")
fig.tight_layout(); fig.savefig(f"{SNK}/dot-lollipop-bar.png",dpi=150,bbox_inches="tight"); plt.close(fig)

# 4. Alphabetical vs value-sorted (snack)
rng=np.random.default_rng(7)
names=["Almond","Brazil","Cashew","Chestnut","Hazel","Hickory","Macadamia","Pecan","Pine","Pistachio","Walnut","Peanut"]
v=np.round(rng.uniform(1,9,len(names)),1)
fig,axs=plt.subplots(1,2,figsize=(11,3.6),sharey=True)
axs[0].bar(names,v,color="#777",width=.6); axs[0].set_title("alphabetical order")
order=np.argsort(-v)
axs[1].bar(np.array(names)[order],v[order],color="#777",width=.6); axs[1].set_title("sorted by value")
for a in axs: a.tick_params(axis="x",rotation=60)
fig.tight_layout(); fig.savefig(f"{SNK}/alpha-vs-sorted.png",dpi=150,bbox_inches="tight"); plt.close(fig)
print("done")
