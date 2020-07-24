https://leetcode-cn.com/problems/divisor-game/

## 1025. Divisor Game

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

- Choosing any x with 0 < x < N and N % x == 0.

- Replacing the number N on the chalkboard with N - x.

Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.
 

**Example 1:**

**Input**: 2

**Output**: true

**Explanation**: Alice chooses 1, and Bob has no more moves.

**Example 2:**

**Input**: 3

**Output**: false

**Explanation**: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

**Note:**

1 <= N <= 1000


## 1025. 除数博弈

爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

- 选出任一 x，满足 0 < x < N 且 N % x == 0 。
- 用 N - x 替换黑板上的数字 N 。
- 
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

 

**示例 1**：

**输入**：2

**输出**：true

**解释**：爱丽丝选择 1，鲍勃无法进行操作。

**示例 2：**

**输入**：3

**输出**：false

**解释**：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。

**提示：**

1 <= N <= 1000

## 题目解析 -- 找规律法

从题目中来看，两个玩家Bob和Alice都是需要赢的，故每个人都会选择对自己最有利的选项，e.g. N为4且Alice先选，则一定会选择1来让自己赢下比赛，Bob同理。而题目中主要时需要Alice赢得比赛，故Alice先手的情况下需要选择能让自己赢的选择。

从执行的操作中来看，发现不了任何的逻辑规律，所以我们利用列举法来列举几个例子来寻找规律。

<table>
    <tr>
        <th>N</th>
        <th>x</th>
        <th>解析</th>
        <th>结果(Alice是否可以赢)</th>
    </tr>
    <tr>
        <td>1</td>
        <td>-</td>
        <td>Alice没有数可以选择(0《x《1)</td>
        <td>False</td>
    </tr>
    <tr>
        <td>2</td>
        <td>1</td>
        <td>新的N为2-1=1，将结果带入到N=1中且Bob先手，则Bob失败</td>
        <td>True</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1</td>
        <td>新的N为3-1=2，将结果带入到N=2中且Bob先手，则Alice失败</td>
        <td>False</td>
    </tr>
    <tr>
        <td rowspan="2">4</td>
        <td>1</td>
        <td>新的N为4-1=3, 将结果带入到N=3中且Bob先手，则Alice失败</td>
        <td rowspan="2">True</td>
    </tr>
    <tr>
        <td>2</td>
        <td>新的N为4-2=2, 将结果带入到N=2中且Bob先手，则Alice赢</td>
    </tr>
    <tr>
        <td>5</td>
        <td>1</td>
        <td>新的N为5-1=4，将结果带入到N=4中且Bob先手，则Alice失败</td>
        <td>False</td>
    </tr>
    <tr>
        <td rowspan="3">6</td>
        <td>1</td>
        <td>新的N为6-1=5, 将结果带入到N=5中且Bob先手，则Alice赢</td>
        <td rowspan="3">True</td>
    </tr>
    <tr>
        <td>2</td>
        <td>新的N为6-2=4, 将结果带入到N=4中且Bob先手，则Alice失败</td>
    </tr>
    <tr>
        <td>3</td>
        <td>新的N为6-3=3, 将结果带入到N=3中且Bob先手，则Alice赢</td>
    </tr>
</table>

因为篇幅问题不再列举，但从上述举例中可以看出两种情况

- 当N为偶数时，先手人Alice肯定赢
- 当N为奇数时，先手人Alice肯定输

基于此，我们假设该情况成立，则需要取证明其的成立性。

1. N=1和N=2时结论一定成立
2. 当N>2时，假设N<=k时该结论成立，则N=k+1时：
   - 若N为奇数且N%x为0，则x只可能是奇数，此时新的N为N=N-x必为偶数（奇数减去奇数为偶数），则k+1-x<=k一定成立，故轮到Bob时一定是偶数。根据刚才的假设N<=k且N为偶数时先手人必定赢，故此时无论Alice拿什么x，Bob一定会赢，所以Alice一定处于必败的状态。
   - 若N为偶数，x可能为奇数也可能为偶数且必定存在一个奇数1，所以当Alice减去任意一个奇数时，k+1-x<=k一定成立，故轮到Bob时一定是奇数。根据刚才的假设N<=k且N为奇数时先手人必定失败，故此时无论Bob拿什么x，Bob一定会输，所以Alice一定处于必胜的状态。

通过上述的反推，证明我们刚才的假设一定成立。

## 解题方法 -- 动态规划

从上述表格可以看出，每一个N所对应的结果都跟之前计算的某个N的结果有关联，故该题目也可以用动态规划来计算。

1. 定义状态

    F(N)为其最优解，最优解的意思为当为N时Alice是否可以赢，0表示False，1表示True。

2. 定义状态转移方程

    F(N) = True 当1<j<i-1中存在 i%j==0 && f(i-j)== False

    否则 F(N) = False

3. 定义初始值，边界值
   
    初始值：F(1) = False, F(2) = True

    边界值： 3<=i<N

4. 定义顺序

    正序







