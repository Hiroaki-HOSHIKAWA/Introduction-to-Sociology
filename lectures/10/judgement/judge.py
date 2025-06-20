import numpy as np


def NashEquilibrium_Judgement(benefit_table,action_num):

    '''
    利得表 (benefit_table)
    プレイヤーの行動数 (action_num)
    '''

    for i in range(action_num):
        for j in range(action_num):
            # 現在のA,Bの行動とその利得
            current_action = benefit_table[i,j]
            # Bが変わらない時のAの取り得る行動とその利得
            possible_actions_a = benefit_table[:,j]
            # Aが変わらない時のBの取り得る行動とその利得
            possible_actions_b = benefit_table[i,:]

            flag = True
            # Aが行動を変えた時にAの利得が上昇するかどうか
            for action in possible_actions_a:
                if action[0] > current_action[0]:
                    flag = False
            # Bが行動を変えた時にBの利得が上昇するかどうか
            for action in possible_actions_b:
                if action[1] > current_action[1]:
                    flag = False
            print(f"current :{current_action} NE = {flag}")



    return 0

def ParetianOptimum(benefit_table,action_num):

    '''
    利得表 (benefit_table)
    プレイヤーの行動数 (action_num)
    '''

    for i in range(action_num):
        for j in range(action_num):
            # 現在のA,Bの行動とその利得
            # i := Aの行動
            # j := Bの行動
            current_action = benefit_table[i,j]
            #現在の行動を除くすべての取り得る行動
            possible_actions = np.array(
                [benefit_table[ii,jj] for ii in range(action_num) for jj in range(action_num) if i!=ii or j!=jj]
            )

            flag = True
            for after in possible_actions:
                # 行動を変えた場合にすべてのプレイヤーについて利得が増えるまたは現状維持(減らない)
                if current_action[0] <= after[0] and current_action[1] <= after[1]:
                    flag &= False
            
            print(f"current :{current_action} PO = {flag}")
            

    return 0
if __name__ == "__main__":
    '''
    (A,B)   |Bの行動1   |Bの行動2
    -----------------------------
    Aの行動1 |(a_1,b_1) |(a_1,b_2)
    -----------------------------
    Aの行動2 |(a_2,b_1) |(a_2,b_2)
    '''

    # プレイヤーの行動の数
    N = 2

    # プレイヤーの行動と行動に対する利得を表にしたもの
    BenefitTable = np.array([
        [[3,3],[0,1]],
        [[1,0],[1,1]]
    ])

    NashEquilibrium_Judgement(BenefitTable,N)
    ParetianOptimum(BenefitTable,N)