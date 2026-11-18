---
title: Claude reveals ECDSA curve origins
url: https://www.anthropic.com/research/ecdsa-curve-origins
date: Oct 16, 2026
category: Frontier Red Team
source: https://www.anthropic.com/research
---

# Claude揭示ECDSA曲线的起源

- **日期：** 
- **类别：** 前沿红队（Frontier Red Team）
- **来源：** https://www.anthropic.com/research/ecdsa-curve-origins

---

前沿红队（Frontier Red Team）
2026 年 10 月 16 日
![Claude揭示ECDSA曲线的起源](assets/ecdsa-curve-origins/img_000.webp)
已发布
    2026 年 10 月 16 日
团队
    [前沿红队](</research/team/frontier-red-team>)
主题
    
  * [网络安全](</search?topic=cybersecurity>)
  * [发现](</search?topic=discovery>)
  * [推理](</search?topic=reasoning>)
  * [编程](</search?topic=coding>)

 _"不过是时间戳而已"：这个关于最流行的密码学标准之一起源、延续数十年的谜团，终于有了答案。_
_我们追查密码学社群这一长期悬而未决的问题，意在消除人们对ECDSA的疑虑——它是我们使用最广泛的密码学标准之一。_
[](<https://www.anthropic.com/claude-fable-and-mythos-5-2>)[](</research/discovering-vulnerabilities-with-claude>)[](</claude-fable-and-mythos-5-1>)[](</research/formalizing-fermats-last-theorem>)
相关文章
  * 公告
2026 年 11 月 9 日
[推出Claude Fable 5.2和Claude Mythos 5.2](<https://www.anthropic.com/claude-fable-and-mythos-5-2>)

[阅读更多](</search?topic=cybersecurity>)
 _读者不妨把这当作一个有趣的收尾章节，是多年猜测的终结。无需采取任何行动，也不必改变做法。多数研究者本来就已信任这些曲线。祝阅读愉快。_  

ECDSA是使用最广泛的椭圆曲线密码学标准。NIST于2000年将其纳入[FIPS 186-2数字签名标准](<https://csrc.nist.gov/files/pubs/fips/186-2/final/docs/fips186-2.pdf>)加以采用，该标准列出了一组大小与安全级别各异的标准椭圆曲线。对素数域与二元域上的曲线，规范公布了一个"种子"参数，其哈希值被用来定义曲线的系数b。这些种子的来源一直是个悬而未决的问题，因为它们由NSA提供，却没有任何解释或论证。举例来说，NIST P-256曲线的种子是`SEED = C49D3608 86E70493 6A6678E1 139D26B7 819F7E90`，关于它从何而来没有任何信息。
[Neal Koblitz](<https://sites.math.washington.edu/~koblitz/>)和[Alfred Menezes](<https://uwaterloo.ca/scholar/ajmeneze>)就这一争议写过一篇精彩的综述，题为"[谜中之谜](<https://eprint.iacr.org/2015/1018.pdf>)"，讨论了种子数值背后的历史与疑虑。这个谜团催生了一项[对种子起源的业余调查](<https://saweis.net/posts/nist-curve-seed-origins.html>)，以及一笔[悬赏，奖励任何能找到它们的人](<https://words.filippo.io/seeds-bounty/>)。
流传最广的说法是，NSA的长期雇员Jerry Solinas用一句幽默口令的哈希值生成了这些种子：
> _"我想当时用的是计数器，而不是多次哈希，但细节我不清楚。那句话大致是'给Bob和Jerry加薪'或'Bob和Jerry说了算'之类。真正写代码的是Bob Reiter，他也不记得细节了。我们也没能找到那么久远的档案。如果档案还在，八成就躺在约柜旁边某块硬盘里。"_
> Jerry Solinas，2015年
遗憾的是，Jerry于2023年去世，当时的其他同事也没有回应，这些种子最初是如何推导出来的问题就此悬置。
### Claude找到了种子
几名Anthropic员工曾顺着"种子是某句幽默短语的哈希值"这条线索追查，但一无所获。结果证明这条线索是错的。2026年10月，一名好奇的Anthropic员工问一个内部研究模型，能否在不提示这条线索的情况下弄清那些种子是如何生成的。
**不到半小时**，Claude就找出了NIST P-192、P-224、P-256、P-384和P-521种子的来源。它们根本不是任何哈希算法的结果，而是C语言库的`lrand48`随机数生成器以Unix时间戳为种子所产生的输出！
所用的算法会从以某个Unix时间戳（**t**）初始化的随机数生成器（RNG）中按若干次迭代（**n**）采样字节。每次迭代抽取20字节作为一个候选种子。于是，头20字节是候选1，接下来的20字节是候选2，依此类推。例如，P-256需要1,842次迭代才输出标准化种子。
![](assets/ecdsa-curve-origins/img_001.webp)
### 这意味着什么
这并不是对密码学的攻破，也不是新攻击或ECDSA曲线中的弱点。事实上，这让我们更加确信，这些曲线在选择时没有任何后门或蓄意埋设的弱点。多年来，人们一直怀疑NIST曲线参数的来源。这些参数被提交给NIST时，完全没有说明是如何选定的，让人不禁猜测它们是否可能被刻意选成带有后门。这些发现使那种可能性大大降低。种子的生成方式非常简单：一个由时钟初始化的常见伪随机数生成器，如今任何人都能复现。这就给暗中动手脚留下的余地小得多，也让我们可以确信这些参数是安全的。
### 它是如何被发现的
根据传闻拼凑那句短语去搜索，一直一无所获。Claude换了另一个角度：推测生成这些曲线的软件必定是怎样工作的。Claude猜测该软件用了1990年代C语言库自带的伪随机数生成器（PRNG）。这些老式PRNG弱到其输出可以被识别出来。识别出那种输出，就能揭示用的是哪个PRNG，并有可能恢复它的初始化状态。 
Claude写了一个扫描器，沿着每个已公布的种子逐比特滑动，检验相邻的数据块是否是某个1990年代老式生成器的连续输出。扫描覆盖了生成器与输出切片的34种组合。就在这时，Claude注意到某些种子的最高位有个规律：它们全为零。若写成五个32位字，十个种子中有四个在其全部20个字的最高位都是0。这种情况纯属偶然的概率是1/5,810。那正是线性同余生成器[`lrand48`](<https://linux.die.net/man/3/lrand48>)的特征，它只返回一个48位状态的最高31位。一旦知道该往哪里看，这个规律用肉眼就能看出来。为恢复状态，Claude取第一个字，穷举17个隐藏比特的全部2¹⁷种取值，并检验接下来的四个字是否吻合。这对所讨论的四个种子都奏效。
![](assets/ecdsa-curve-origins/img_002.jpg)
素数域曲线的种子来自同一个lrand48生成器，但每次输出只保留了更少的比特。Claude不得不从这些比特中恢复PRNG的内部状态。事实证明，恢复截断线性同余生成器的状态是一道教科书式的格问题，可用[Lenstra–Lenstra–Lovász（LLL）](<https://en.wikipedia.org/wiki/Lenstra%E2%80%93Lenstra%E2%80%93Lov%C3%A1sz_lattice_basis_reduction_algorithm>)基约简算法求解。Claude并不知道种子可能暴露状态的哪些比特，于是对每个窗口都跑了一遍求解器。五个NIST素数域曲线种子，加上ANSI X9.62标准中的另外五个，全都有同样的规律：lrand48() >> 23\.每个恢复出的48位状态都能重新生成其种子的全部160比特，这不可能是碰巧。
![](assets/ecdsa-curve-origins/img_003.png)
这个线性同余生成器倒推与正推一样容易，因此对每个种子，Claude都把状态往回步进，直到它呈现出会被[srand48](<https://linux.die.net/man/3/srand48>)初始化的那种形态，即低16位等于0x330E。这种形态的内部PRNG状态每65,536步才会出现一次，所以单独抵达这样一个状态本身并不构成证据。
然而，对那十个素数域曲线种子而言，每次srand48初始化都是一个Unix时间戳，对应1997年5月到1998年4月之间的某个日期。它们用的正是由Unix时间戳播种的弱PRNG。四个二元域曲线的初始化读出来是1984年2月。把时间戳翻倍后，它们对应到1998年4月17日，比P-224那次运行晚两周。因此，程序可能把时钟减半了。
Claude当时的内部思路是：
> 这太惊人了：它解开了这个25年的谜团。嗯，等等。我得持怀疑态度：我是不是处在某种模拟/测试环境里？……种子和我记忆中的实际数值吻合……嗯，这在现实中可信吗？据我所知……那笔悬赏一直没被解开。……所有最高位都清零——20比特，概率1e-6。所以确实是真实世界。哇，这是一项真正的发现。
> 嗯，等等。可信度上我得谨慎些：这么明显的东西25年都没人发现，是不是有点可疑？但在我这边已经用直接计算验证过了：从一个32位种子加上一个小索引就得到160比特的吻合：不可能是巧合（10 × 160比特）。是真的。
### Claude还找到了一些基点
不过，等等，还有更多……每条曲线还配有一个基点G，即每个ECDSA公钥都是其倍数那个固定点。上面找到的种子并不能决定这个G，于是另一个问题浮出水面：这些基点是如何生成的？
在核查种子的过程中，Claude还弄清了部分基点的来历。1997年5月生成的六条曲线（P-192以及ANSI X9.62的五条示例曲线prime192v2、prime192v3和prime239v1至v3）的基点，来自[FreeLIP](<https://cr.yp.to/speed/mult/freelip.html>)中的随机数生成器，那是[Arjen Lenstra](<https://en.wikipedia.org/wiki/Arjen_Lenstra>)的长整数运算库。[Victor Shoup](<https://shoup.net/>)的[NTL库](<https://libntl.org/>)早期版本也带有同样的代码。
这里的做法很简单：
  1. 用一个小整数给生成器播种。
  2. 丢弃七次输出。
  3. 由26位输出对p取模生成候选x坐标。
  4. 重复第3步，直到x落在曲线上。

Claude发现生成器的种子为：P-192是20000，prime239v1至v3分别是20420、20507和20509，prime192v2和v3分别是20512和20517。
![](assets/ecdsa-curve-origins/img_004.jpg)
据我们所知，此前从未有NIST的基点被解释清楚。P-224、P-256、P-384和P-521的基点不符合这套做法；我们没能解释它们是如何选定的。
### 未解的问题
并非每个20字节的候选种子都能生成一条可用的曲线，我们还观察到一些本可能可用的曲线被跳过了。对P-256来说，公布的种子是候选1,842，但同一次运行中的候选876同样能给出大小合适、参数选取方式与公布曲线一致的素数阶曲线。P-224那次运行略过了三条这样的曲线，而ANSI X9.62示例曲线背后的两次运行又略过了七条（见图）。我们不知道当时可能用了什么判据，也不清楚这是否只是无心造成的产物。
![](assets/ecdsa-curve-origins/img_005.png)
![](assets/ecdsa-curve-origins/img_006.png)
由于被跳过的候选数量很少，我们认为不大可能是刻意挑了被削弱的曲线。那将意味着被削弱的曲线很常见且容易找到。原则上仍可以设想，这些曲线是通过对随机数生成器的时间戳做搜索、为具备某种特定性质而选出来的。不过，只有在你打算把时间戳披露出来、当作种子系无害生成的某种证据时，才有必要这么做。这些数字里没有任何东西能表明到底运行过多少次。
还有一个种子我们没能恢复。第五个二元域种子B-163不符合Claude尝试过的任何方案，至今无解。最后，我们不知道P-224、P-256、P-384和P-521的基点是如何生成的。NIST的二元域曲线也是如此。
### 悬赏
找到种子所得的36,864美元将捐给[互联网安全研究组](<https://www.abetterinternet.org/>)。
### 我们是谁
这项工作由Anthropic的John Wood、Henry de Valence、Ava Howell、Zack Voase、Lucy Sweet、Amir Omidi、Paul Crowley、Iain McGinniss、Nicholas Carlini和Steve Weis完成。
### 复现种子的代码

```python
from datetime import datetime, timezone

def unix(when):
    return int(datetime.fromisoformat(when).replace(tzinfo=timezone.utc).timestamp())

def candidate(t, n, per, shift, width):
    x, out = (t << 16) | 0x330E, ""                      # the state srand48(t) sets
    for i in range(per * n):
        x = (0x5DEECE66D * x + 0xB) % 2**48              # one step of lrand48
        if i >= per * (n - 1):
            out += "%0*X" % (width, x >> shift)
    return out

PRIME = {  # srand48(time); 20 bytes per candidate: lrand48() >> 23
    "prime239v1": ("1997-05-15 15:49:03", 2185),
    "prime239v2": ("1997-05-15 15:49:03", 2320),
    "prime239v3": ("1997-05-15 15:49:03", 3048),
    "P-192":      ("1997-05-18 14:45:34", 139),
    "prime192v3": ("1997-05-18 14:45:34", 5228),
    "prime192v2": ("1997-05-18 14:45:34", 6013),
    "P-521":      ("1997-08-08 01:12:04", 1136),
    "P-256":      ("1997-08-16 01:52:34", 1842),
    "P-384":      ("1997-08-30 14:50:08", 2688),
    "P-224":      ("1998-04-03 12:52:07", 7026),
}
BINARY = {  # srand48(time / 2), if that reading is right; 5 words per candidate: lrand48()
    "B-233": ("1998-04-17 15:24:18", 155),
    "B-283": ("1998-04-17 15:27:44", 32),
    "B-409": ("1998-04-17 15:30:18", 60),
    "B-571": ("1998-04-17 15:32:08", 73),
}
for name, (when, n) in PRIME.items():
    print(f"{name:10} {when} {n:5} {candidate(unix(when), n, 20, 40, 2)}")
for name, (when, n) in BINARY.items():
    print(f"{name:10} {when} {n:5} {candidate(unix(when) // 2, n, 5, 17, 8)}")
```

这段代码的输出：

```
prime239v1 1997-05-15 15:49:03  2185 E43BB460F0B80CC0C0B075798E948060F8321B7D
prime239v2 1997-05-15 15:49:03  2320 E8B4011604095303CA3B8099982BE09FCB9AE616
prime239v3 1997-05-15 15:49:03  3048 7D7374168FFE3471B60A857686A19475D3BFA2FF
P-192      1997-05-18 14:45:34   139 3045AE6FC8422F64ED579528D38120EAE12196D5
prime192v3 1997-05-18 14:45:34  5228 C469684435DEB378C4B65CA9591E2A5763059A2E
prime192v2 1997-05-18 14:45:34  6013 31A92EE2029FD10D901B113E990710F0D21AC6B6
P-521      1997-08-08 01:12:04  1136 D09E8800291CB85396CC6717393284AAA0DA64BA
P-256      1997-08-16 01:52:34  1842 C49D360886E704936A6678E1139D26B7819F7E90
P-384      1997-08-30 14:50:08  2688 A335926AA319A27A1D00896A6773A4827ACDAC73
P-224      1998-04-03 12:52:07  7026 BD71344799D5C7FCDC45B59FA3B9AB8F6A948BC5
B-233      1998-04-17 15:24:18   155 74D59FF07F6B413D0EA14B344B20A2DB049B50C3
B-283      1998-04-17 15:27:44    32 77E2B07370EB0F832A6DD5B62DFC88CD06BB84BE
B-409      1998-04-17 15:30:18    60 4099B5A457F9D69F79213D094C4BCD4D4262210B
B-571      1998-04-17 15:32:08    73 2AA058F73A0E33AB486B0F610410C53A7F132310
```

### 复现选定基点的代码

```python
M, A = 2**107 - 1, pow(3, 121, 2**107 - 1)       # zrandom: state = state * 3^121 mod (2^107 - 1)
P192 = 2**192 - 2**64 - 1
P239 = 2**239 - 2**143 - 2**95 + 2**47 - 1

CURVES = [  # name, LIP seed, p, b, published Gx   (a = -3 throughout)
    ("prime192v1", 20000, P192,
     0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1,
     0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012),
    ("prime239v1", 20420, P239,
     0x6b016c3bdcf18941d0d654921475ca71a9db2fb27d1d37796185c2942c0a,
     0xffa963cdca8816ccc33b8642bedf905c3d358573d3f27fbbd3b3cb9aaaf),
    ("prime239v2", 20507, P239,
     0x617fab6832576cbbfed50d99f0249c3fee58b94ba0038c7ae84c8c832f2c,
     0x38af09d98727705120c921bb5e9e26296a3cdcf2f35757a0eafd87b830e7),
    ("prime239v3", 20509, P239,
     0x255705fa2a306654b1f4cb03d6a750a30c250102d4988717d9ba15ab6d3e,
     0x6768ae8e18bb92cfcf005c949aa2c6d94853d0e660bbf854b1c9505fe95a),
    ("prime192v2", 20512, P192,
     0xcc22d6dfb95c6b25e49c0d6364a4e5980c393aa21668d953,
     0xeea2bae7e1497842f2de7769cfe9c989c072ad696f48034a),
    ("prime192v3", 20517, P192,
     0x22123dc2395a05caa7423daeccc94760a7d462256bd56916,
     0x7d29778100c65a1da1783716588dce2b8b4aee8e228f1896),
]

def base_point_x(seed, p, b):
    state = seed                         # zrstarts(seed)
    def limb():                          # zrandom(2^26): low 26 bits of the new state
        nonlocal state
        state = state * A % M
        return state % 2**26
    for _ in range(7):                   # seven single-limb draws come first
        limb()
    limbs = -(-p.bit_length() // 26) + 1 # zrandomb(p): limbs of p plus one, top limb first
    tries = 0
    while True:
        x = 0
        for _ in range(limbs):
            x = x << 26 | limb()
        x %= p
        tries += 1
        if pow(x**3 - 3*x + b, (p - 1) // 2, p) == 1:   # is x on the curve?
            return x, tries

for name, seed, p, b, gx in CURVES:
    x, tries = base_point_x(seed, p, b)
    print(f"{name:20} seed {seed}  tries {tries}  matches published Gx: {x == gx}")
```

这段代码的输出：

```
prime192v1           seed 20000  tries 2  matches published Gx: True
prime239v1           seed 20420  tries 3  matches published Gx: True
prime239v2           seed 20507  tries 2  matches published Gx: True
prime239v3           seed 20509  tries 1  matches published Gx: True
prime192v2           seed 20512  tries 5  matches published Gx: True
prime192v3           seed 20517  tries 1  matches published Gx: True
```
### 许可
在法律允许的最大范围内，作者已放弃对本页代码的全部著作权及相关或邻接权利，依据[CC0 1.0 Universal](<https://creativecommons.org/publicdomain/zero/1.0/>)将其奉献至公有领域。  

## 作者与致谢
### 致谢
我们要追认Jerry Solinas，他以豁达幽默的态度接受了被贴上"[邪恶的网络梗](<https://cr.yp.to/papers/safecurves-20240809.pdf>)"和"[NSA妖魔界的Yo La Tengo](<https://sockpuppet.org/blog/2015/08/04/is-extended-random-malicious/>)"这类标签。也感谢[Filippo Valsorda](<https://filippo.io/>)组织了NIST椭圆曲线种子悬赏。
