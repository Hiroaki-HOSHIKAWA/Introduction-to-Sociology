import numpy as np
import matplotlib.pyplot as plt

# a_n : n日目の未感染者の割合
# b_n : n日目の感染者の割合
# b_n : n日目の回復者の割合
a_n,b_n,c_n = [0.99],[0.01],[0.0]

# beta : 感染力(>0)
# gamma : 回復率(0~1)
# delta : 再感染率(0~1)
beta, gamma, delta = 1.0,0.3,0.02

# シミュレート日数
N = 100

def run():
    a_n_last,b_n_last,c_n_last = a_n[0], b_n[0], c_n[0]
    for n in range(N-1):
        a_n_new = a_n_last - beta*a_n_last*b_n_last + delta*c_n_last
        b_n_new = b_n_last + beta*a_n_last*b_n_last - gamma*b_n_last
        c_n_new = c_n_last + gamma*b_n_last - delta*c_n_last

        a_n.append(a_n_new)
        b_n.append(b_n_new)
        c_n.append(c_n_new)

        a_n_last,b_n_last,c_n_last = a_n_new,b_n_new,c_n_new

def plot():
    n = np.arange(1,N+1)
    plt.plot(n,np.array(b_n))
    plt.savefig("graph1.png",format="png",dpi=300)

if __name__ == "__main__":
    run()
    plot()
