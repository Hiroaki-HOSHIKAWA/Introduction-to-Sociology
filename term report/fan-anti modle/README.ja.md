# ファン・アンチ モデル

## 定義

### パラメーター

- ファン値 : $f$
    -  $-1<f< 1$
    - $f \approx -1 \implies$ 完全なアンチ
    - $f \approx 1 \implies$ 完全なファン
    - $f = 0 \implies$　中立

- 対象の振る舞い : $b$
    - $-1<b<1$
    - $b \approx -1 \implies$ 社会的に悪な振る舞い
        - 不倫
        - 差別発言
    - $b \approx 1 \implies$ 社会的に善な振る舞い
        - 慈善活動
    
### 関数

対象の行動に対する反応を $R$ とおくと,  $R$ は自身のファン度合い(ファン値) $f$ と対象の行動がどれぐらい社会的に善または悪かの度合い $b$ によって決まると仮定すると

$$
    R = R(b,f)
$$

とかける.

$$
R(b,f) = \tanh(\alpha f + \beta(1-f^2)), (\alpha,\beta \in \mathbb{R})
$$

と定義すると[^by-chat-gpt]

[^by-chat-gpt]: この式はChat GPTに提案されたものです。
