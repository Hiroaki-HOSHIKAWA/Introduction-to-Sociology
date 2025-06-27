import numpy as np

class Simulator(object):
    def __init__(self):
        self.alpha :float = 0.0
        self.beta :float = 0.0

        # プレイヤー人数
        self.player_number: int  = 0

        # 反復回数
        self.iteration_count: int = 0

        # 現在時刻
        self.current_time: int = 0

        # ファン値 f 
        # f[x][y]は時刻xにおけるプレイヤーyのファン値を表す
        self.fan : np.ndarray = np.array([[0,0]])
    
    def R(self,f,b):
        return np.tanh(
            self.alpha * f
            + self
            .beta * b * (1-np.pow(f,2))
        )
    
    def setup(self,alpha,beta,player_number,iteration_count):
        """
        player_number := プレイヤー人数
        iteration_count := 反復回数
        """
        self.alpha = alpha
        self.beta = beta
        self.player_number = player_number
        self.iteration_count = iteration_count
        self.fan = np.zeros(shape=(self.iteration_count,self.player_number))

        # 時刻0(初期状態)におけるf値生成
        # 分布は平均が0で-1<x<1に99％が含まれるようにスケーリングしたもの
        self.fan[0] = self.__scaled_random_normal__()
    
    def __scaled_random_normal__(self):
        # P(-2.5728 < X < 2.5728) = 0.99
        sigma = 1 / 2.5728
        return np.random.normal(loc=0,scale=sigma,size=self.player_number)

def run():
    return 0

if __name__ == "__main__":
    run()