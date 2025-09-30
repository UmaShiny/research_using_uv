# Reading Research Article About Financial Trading No.1 EN

# Artificial intelligence techniques
in financial trading: A systematic literature review

Fatima Dakalbab, Manar Abu Talib b, Qassim Nasir, Tracy Saroufil

[](https://www.sciencedirect.com/science/article/pii/S1319157824001046)

---

## Abstract

- AIの利用が金融市場で加速している
- AI技術による金融取引のアプローチを研究する体系的文献レビュー

## 1. Introduction

- 株価の予測は，以下の性質から複雑なシステムを必要であると知られる
    - 非線形（non-linear）
    - 非定常（non-stationary）
    - 時変（time-variant）
- また，以下の変動要因に敏感である
    - 経済ニュース
    - 政治的な出来事
    - 国際的な影響

## 2. Background

### 2.1 Japanese candlesticks

- 株価チャート方式は３つに大別される
    1. ラインチャート（Line charts）→ 西洋産
    2. バーチャート（Bar charts）→ 西洋産
    3. ローソク足チャート（Candlestick charts）→ 日本産
- ローソク足チャートの歴史
    - ラインチャートやバーチャートより約１世紀早く，日本で確立
    - 1700年代、米の価格・供給・需要には関係があったが，本間という日本人は，商人の感情が市場に大きな影響を与えることを観察した
- ローソク足チャートの特性
    - ローソク足が、価格変動のボリュームを明確な色でグラフィカルに表示することによって感情を示すことができる
        
        ![](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr1_lrg.jpg)
        
    - ローソク足チャートによって、トレーダーは研究された市場の価格の遷移を分析することができる
    - 時間間隔は，1min，5min，30min，1hourなど
    - 株価が軟調な場合は赤か塗りつぶし，堅調な場合は緑か白抜きで表現される
    - 1分足より，5分足の方が，より遷移の象徴が正確になり，いい結果をもたらす

### **2.2. Trading analysis types**

- トレーダーは，市場の動きやパターンの評価のために，様々な手法を採用している
- １つ以上の手法を組み合わせたりして，予測を行う（下図は分析手法の樹形図）
    
    ![](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr2_lrg.jpg)
    
- **ファンダメンタル分析手法（Fundamental analysis approach）**
    - 市場に影響を与える経済ニュースの分析
    - 経済指標を用いた金融証券の内在的価値の見積り
    - カレンダー
        - 市場に影響を与える経済データや重要なイベントの追跡を維持する
        - イベントと世界市場との関連性を説明する
        - リスク管理と長期的な計画を立てることをたすける
    - ファンダメンタル分析は、経済分析に重点を置いており、市場関連ニュースのセンチメントに基づき、財務諸表を調査し、かなりの調査が必要である
- **テクニカル分析手法（Technical analysis approach）**
    - 統計的手法と，１年以上の各取引日の終値の価格変動を描いたチャートに基づく手法
    - 利活用ができそうな価格変動パターンと市場トレンドを発見する
    - この手法のねらい
        1. 金融証券の価格系列から取引戦略を構築するための非線形パターンの抽出
        2. 重要な市場の動きの捕捉
        3. 価格の不規則な揺らぎの無視
    - テクニカル分析は、価格チャート、統計指標（移動平均、相対力指数、移動平均収束乖離など）、オシレーターなどを用いて値動きを予測する

|  | ファンダメンタル分析 | テクニカル分析 |
| --- | --- | --- |
| 目的 | 資産が過小評価されているか過大評価されているかを判断するための市場価値の決定 | 市場に参入／購入または撤退／売却する適切な取引時間を決定 |
| 概念 | センチメントに従い、市場経済に集中する | 統計的指標を用いて価格動向を調査し、将来の値動きを予測する。 |
| 依存 | ニュース，経済，財務状態 | ローソク足チャート，テクニカル指標 |
| 機能 | トレード，投資 | トレード |
| 使用方法 | 過去と現在のデータの広範な調査が必要 | 過去の履歴データからなる情報 |
| 単位時間 | 長期 | 短期 |

### **2.3. Algorithmic trading**

- アルゴリズム取引（Algorithmic trading）とは
    - 複雑なアルゴリズムを使って取引プロセスを自動化する取引のこと
    - 学習，推論，意思決定によって特徴付けられる
    - コンピュータの性能が向上するにつれ人気が高まる
    - 人間のブローカーとは異なり，現代のコンピュータの計算能力や強度を利用する
        - その迅速で正確なオペレーションが注目され、取引コストを最小限に抑え、取引の精度と変動性を高めている
    - トレーダーはバックテストと呼ばれるプロセスを使って、過去のデータを使って戦略やモデルのパフォーマンスを分析できる
        - バックテストにより、トレーダーはモデルや戦術を微調整し、強化できる
- アルゴリズム取引は、あらかじめ決められた戦略に従うモデルを採用している
    - これらのモデルには、現在の価格と前日のレンジに応じて利食いと損切りのアクションを作成するといった、基本的でありながら成功する戦術を含めることができる
    - 堅牢で複雑なモデルの開発もAIのアプローチで可能となった
    - これらのモデルは、様々な市場環境にわたって慎重にバックテストされた方法論に対応している。
        - オーバーフィッティングの最小化と，最適なパラメタを達成するために重みを微調整する機械学習モデルの検証とテストに対応する
        - バックテストは、リアルタイムのデータを使った模擬取引によって継続されることが多い
- このアルゴリズムが効果的であり続ければ、取引に導入され、その実行可能性を評価するために常に監視される可能性が高い
    - パフォーマンスが低下した場合、システムは適応して再展開し、開発者は理想的なアクションを達成するまで、段階的にアップデートと最適化を行うことができる。

## **3. Literature review**

- 金融市場を**AI**を用いて調査した論文は複数実施されている
    - [**When quantitative  trading meets machine learning: A pilot survey](https://ieeexplore.ieee.org/document/7538632)**
    Yelin Li, Junjie Wu, Hui Bu
        - 価格動向(price trends)，予測(forecasting)，ポートフォリオ選択(portfolio selection)を含む視点から取り組むクオンツトレーディング([quantitative trading](https://www.oanda.jp/lab-education/panrolling/%E4%B8%8A%E7%B4%9A%E8%80%85/4400/))
        - ニューラルネットワーク(NN)，サポートベクタマシン(SVC)，ウェーブレット解析([wavelet analysis](https://www.osaka-kyoiku.ac.jp/~ashino/pdf/wavelet.pdf))，ポートフォリオ選択を学習するためのテキストマイニング(text mining)といった手法を用いて，株式市場における価格予測を分類する
    
    - [**Literature review: machine learning techniques applied to financial market prediction](https://www.sciencedirect.com/science/article/abs/pii/S095741741930017X)**
    B.M. Henrique, V.A. Sobreiro, H. Kimura
        - 金融市場価値の予測のための機械学習アプローチに焦点を当てた書誌的分析([bibliographic analysis](https://www.sciencedirect.com/topics/computer-science/bibliographic-analysis))を行った
        - 57の論文を分析し、その結果、価格予測に最もよく使われるモデルはサポートベクタマシンとニューラルネットワークであることを明らかにした
        - 著者らによれば、この研究課題は依然として重要であり、発展途上市場のデータを使うことは研究の機会を提供する
    
    - [**Stock market movement forecast: a systematic review](https://www.sciencedirect.com/science/article/abs/pii/S0957417420302888?via%3Dihub)**
    O. Bustos, A. Pomares-Quimbaya
        - 株式市場のトレンド予測を徹底して実施した
        - 2014年から2018年までの予測方法を，分類し，特徴付けして，比較した結果，テクニカル指標は市場予測において重要なことを示した
        - アンサンブルモデルによる予測が高性能であることを示した
        - データセットの不足に起因して，ディープラーニングモデルが従来の手法を超えなかったと主張している
    
    - [**Artificial Intelligence Applied to Stock Market Trading: A Review](https://ieeexplore.ieee.org/abstract/document/9350582)**
    Fernando G. D. C. Ferreira; Amir H. Gandomi; Rodrigo T. N. Cardoso
        - 1995年から2019年までの、株式市場取引におけるAIを調査した広範な研究を対象に、[**Stock market movement forecast: a systematic review**](https://www.sciencedirect.com/science/article/abs/pii/S0957417420302888?via%3Dihub)とは異なる評価を行っている
        - 株式市場で利用されるAIアプローチを次の4つに分類した
            1. ポートフォリオ最適化（portfolio optimization）
            2. AIを使った株式市場予測（stock market prediction using AI）
            3. 金融センチメント分析（financial sentiment analysis）
            4. 2つ以上の方法論の組み合わせ（combinations of two or more methodologies）
    
    - [**A Comprehensive Comparative Study of Artificial Neural Network (ANN) and Support Vector Machines (SVM) on Stock Forecasting**](https://link.springer.com/article/10.1007/s40745-021-00344-x)
    Akshit Kurani, Pavan Doshi, Aarya Vakharia & Manan Shah
        - 人工ニューラルネットワーク（Artificial Neural Networks：ANN）とサポートベクタマシン（Support Vector Machine：SVM）が人気の機械学習手法であるとした

- トレーディングに**深層学習と深層強化学習**（Deep Reinforcement Learning）技術を使った研究も複数実施されている．ディープラーニングは、世界中の予測不可能な金融市場、特に株式市場をモデル化し予測するための有力な手法として急速に台頭してきた
    - [**Deep reinforcement learning for trading—a critical survey](https://www.mdpi.com/2306-5729/6/11/119)**
     Adrian Millea
        - 暗号通貨市場におけるDRLアプリケーションの概要を発表した
        - 筆者によると，最も一般的に使われるモデルは畳み込みニューラルネットワーク（Convolutional Neural Network：CNN）
        - パフォーマンス指標として，シャープレシオ（Sharpe ratio）がよく採用される
    
    - [**Stock market forecasting using deep learning and technical analysis: a systematic review**](https://ieeexplore.ieee.org/document/9220868?denied=)
    Audeliano Wolian Li, Guilherme Sousa Bastos
        - 徹底的な株式市場における深層学習とテクニカル分析の文献レビュー
        - 次の4つの領域に焦点を当てた体系的な研究
            1. 価格予測アプローチ（price forecasting approach）
            2. トレーディング戦略（trading strategy）
            3. 利益評価と対策（profit evaluation and measures）
            4. リスクマネジメント（risk management）
        - 最も採用されるモデルはLSTM
    
    - [**Deep Learning Techniques for Stock Market Prediction in the European Union: A Systematic Review](https://ieeexplore.ieee.org/abstract/document/9458031)**
    Argyrios P. Ketsetsis; Christos Kourounis; Georgios Spanos; Konstantinos M. Giannoutakis; Pavlos Pavlidis; Dimitris Vazakidis
        - 欧州株式市場におけるディープラーニング技術を分析したシステマティック・レビューを発表した。

- **FinTech**は、アクセシビリティ，効率性，インクルージョン（[Inclusion](https://www.gmo-pg.com/blog/articles/article-0115/)）を向上させる新しいデジタル・ソリューションによって従来の金融サービスを変革する．
FinTechの急成長は、モバイル決済からロボット・アドバイザー（[robot advisor](https://www.smbcnikko.co.jp/terms/japan/ro/J0682.html)）まで、消費者と組織の金融取引と投資の処理方法を変え続けている
    - [**Artificial intelligence and fintech: an overview of opportunities and risks for banking, investments, and microfinance](https://onlinelibrary.wiley.com/doi/10.1002/jsc.2404)**
    A. Ashta, H. Herrmann
        - 銀行，投資，マイクロファイナンス（[microfinance](https://job.career-tasu.jp/finance/articles/039/)）を含む金融部門におけるAI活用の機会とリスクについて議論するレビューを紹介している
        - AIが金融業界にどのような変革をもたらすのか、また金融機関がこの技術を統合する際に考慮しなければならないことは何かについて概観している
    
    - [**An overview of the artificial intelligence applications in fintech and regtech**](https://link.springer.com/chapter/10.1007/978-981-33-6811-8_15)
    G. Bayramoğlu
        - FinTechと[RegTech](https://www.nri.com/jp/knowledge/glossary/regtech.html)（規制技術）の両方におけるAIの応用分野を調査した
        - AIがFinTechに与える影響と規制当局（政府当局？）に対するメリットについて議論している
        - FinTechに関連するリスクと，FinTechの潜在的な可能性を損なわずに，どのようにRegTechがFinTechを規制するのに役立つかを強調している
        - AIを活用したFinTechとRegTechの素晴らしい世界と，それが金融サービスに対してどのような革命をもたらしつつあるかについて洞察を提供している
    
- いくつかの研究は、主要な巨大領域である金融に焦点を当て、AIと機械学習がいくつかの要因から金融にどのような影響を及ぼしているかを考察している
    - [**Artificial intelligence techniques in finance and financial markets: A survey of the literature](https://onlinelibrary.wiley.com/doi/abs/10.1002/jsc.2403)**
    Carlo Milana, Arvind Ashta
        - 金融と金融市場におけるAIの応用に関するこの文献レビューの著者は、この産業がもたらすであろう利益と障害についての洞察を示している
        - 市場付加価値、リスク管理、長期的成長に対するAIの影響を評価するために、ファジー集合定性比較分析（fuzzy set qualitative comparison analysis）やアブダクティブ学習ネットワーク（abductive learning networks）など、さまざまな研究やアプローチを検証している
        
    - [**Machine learning in finance: a topic modeling approach**](https://onlinelibrary.wiley.com/doi/10.1111/eufm.12326)
    Saqib Aziz, Michael Dowling, Helmi Hammami, Anke Piepenbrink
        - 金融におけるAIに関する記事の頻度分布を時系列で調査し、最近関心が急上昇していることを明らかにした
        - データサイエンスのトピックモデリング技法（[topic modeling technique](https://blog.since2020.jp/glossary/topic_analysis/)）を研究に採用して，機械学習と金融の研究の構造に関する徹底的かつトレンドに基づいた知識を構築している
        - 15の一貫した研究テーマを発見し，それらを4つグループに分類すると同時に，その手法の限界を認識している
        
    - [**Deep Learning for Financial Engineering**](https://link.springer.com/article/10.1007/s10614-022-10260-8)
    M. Y. Chen, A. K. Sangaiah, T. H. Chen, E. D. Lughofer, and E. Egrioglu,
        - 金融工学という分野横断的な分野と，ディープラーニングを含む様々な定量分析分野をどのようにうまく統合してきたかを探求している
    
    - [**Machine Learning in Economics and Finance**](https://link.springer.com/article/10.1007/S10614-021-10094-W)
    P. Gogas and T. Papadimitriou
        - 経済学と金融における機械学習の実用的な使い方について検討している
        - 最近のMLアーキテクチャの改良により、マクロ経済学やミクロ経済学のアプリケーションのような、データセットが本質的に小さい分野でのML技術の採用がどのように可能になったかについて述べている
        - 経済学に新鮮で実質的な経験的洞察をもたらす機械学習アルゴリズムの斬新で独創的な使用法を強調している
        - 経済・金融要因の予測から株式市場全体のモデリングに及ぶ，17の研究から成る
        
    - [**Applications of artificial intelligence in business management, e-commerce and finance**](https://www.sciencedirect.com/science/article/abs/pii/S2214785321048136)
    H. Pallathadka, E.H. Ramirez-Asis, T.P. Loli-Poma, K. Kaliyaperumal, R.J.M. Ventayen, M. Naved
        - 電子商取引（e-commerce）と金融におけるAIの応用について概観している
        - この研究では，AIが顧客体験（customer experience），サプライチェーン管理（supply chain management），業務効率（operational efficiency），製品品質管理（product quality control）の改善にどのように利用されているかを強調している
        - 最も一般的に使用されている2つのAIアプローチである，機械学習と深層学習の違いについても論じている
        
- 書誌分析のレビューを提供することに焦点を当てた2つの研究
    - [**Artificial intelligence and machine learning in finance: Identifying foundations, themes, and research clusters from bibliometric analysis**](https://www.sciencedirect.com/science/article/abs/pii/S0275531922000344)
    J. W. Goodell, S. Kumar, W. M. Lim, and D. Pattnaik
        - 金融における機械学習と人工知能の書誌分析による評価を行った
        - 出版物、ジャーナル、著者、組織、国の書誌構造を評価することで、ファイナンス研究におけるAIとMLの概念形成を明らかにしようとした
        - 書誌分析を4ステップにアプローチを分け，結果を報告した
            1. 評価の目的と範囲の設定
            2. 分析技法を選択する
            3. 分析データを収集する
            4. 分析を実行する
        - 本レポートでは、金融におけるAIと機械学習に関する研究を徹底的に調査し、主要テーマと研究クラスタを浮き彫りにしている
        
    - [**Artificial intelligence and machine learning in finance: a bibliometric review**](https://www.sciencedirect.com/science/article/abs/pii/S0275531922000344)
    S. Ahmed, M.M. Alshater, A. El Ammari, H. Hammami
        - 逆に、本レポートは、AIと機械学習の金融への応用に関する文献の別の書誌学的評価を提供している
        - 彼らは、文献、著者、ジャーナル、機関、国など、文献の最も重要な科学的アクターを調査するために、計量書誌学とサイエントロメトリー（scientometric）の方法論を用いた
        - 著者らは、VOSviewerとRStudioを用いて、キーワードの共起、要因分析、傾向分析、共著、書誌的結合を行った。
        
- 金融取引におけるAIの応用に関する本SLRは，いくつかの欠かせない側面を通じて，既存の最先端のレビューとは一線を画しており，ダイナミックに進化するこの分野の学術的・実践的理解に対するユニークな貢献を強調する
    1. 広範かつ包括的
        - 株式・暗号通貨・為替といった特定の金融市場，深層学習などの特定のAIメソッドに集中する従来の調査とは異なり，本SLRは，さまざまな金融取引における，市場機械学習・深層学習・強化学習などの広範囲なAI技術をカバーしている
        - このような包括的なアプローチにより、本レビューは、金融取引におけるAIの応用について、最先端の応用と学際的な発展に重点を置きながら、より徹底的な概観を提供することができる
    2. 根拠と概念の明確さ
        - はじめに，本SLRでは，ローソク足チャートや取引分析への様々なアプローチといった，金融取引の基本的な考え方と技術の説明から始まる
        - 続いて，アルゴリズム取引の概念を濃縮して説明する
        - 本SLRは、アクセシビリティと包括性を保証し、読者にその後の取引市場におけるAIの探求を完全に理解するための強固な理論的基礎を提供することで際立っている
    3. 徹底的な分析とデータ収集
        - 2015年から2023年までの143件の論文を注意深く調査し、金融取引市場、取引される資産の種類、採用されたAIモデルとアプローチ、取引分析の種類、システムの特徴と出力、データセットとそのソース、モデル性能を評価するための指標、出版物の種類、論文の時系列分布など、いくつかの分野で有意義な情報を抽出した
        - この精密なデータ収集工程が，パターン・標準的な手順・注目すべき結果を特定することで，金融取引における最新のAI活用の詳細な外観を作成することができる
    4. ギャップの特定と今後の提言
        - 既存知識の合成に加え，この体系的な研究が本質的な研究ギャップ（[research gaps](https://www.enago.jp/academy/identifying-research-gaps/)）を明らかにし，今後の研究の方向性を示唆する
        - 私たちのSLRは、AIと金融取引の交差点にある、まだ代表的でない分野でのアイデアや調査を奨励し、将来の研究を指導します
        
- 本稿の目的は、金融取引で使用されるAI技術を体系的なアプローチでのレビュー
    - 2015年から2023年にかけて発表された研究を徹底的に分析し、最も人気のあるAI技術と、トレーダーがより良い意思決定を行うために資産価格パターンを予測する上で、その利点をどのように最大限に活用しているかを明らかにした
    - 本SLRが伝えたかった第一のメッセージは、金融取引市場で使用されている最先端のAIアプリケーションを特定することで、共通のアプローチ、手法、結果を強調できるということだった
    - この収集データは、過去10年間の取引におけるAIの使用における研究パターンを特定するのに役立った
    - この研究で収集されたデータは、文献のギャップと、この分野における研究の将来の方向性を含む提言に光を当てた
    - これは理想的には、将来の科学者がこの分野で新たな研究対象を発見し、現在の研究のギャップや欠陥を埋めるための実行可能な解決策を見つけるのに役立つ

## 4. Methodology

この調査では，次のSystematic Literature Reviewに基づいた手法で行っている

- [Guidelines for performing systematic literature reviews in software engineering](https://www.researchgate.net/profile/Barbara-Kitchenham/publication/302924724_Guidelines_for_performing_Systematic_Literature_Reviews_in_Software_Engineering/links/61712932766c4a211c03a6f7/Guidelines-for-performing-Systematic-Literature-Reviews-in-Software-Engineering.pdf)
S. Kitchenham, B. and Charters,
    - 次の３フェーズに分かれており，各フェースはいくつかのステージから成る
        1. 計画（planning）
            - 「計画」フェーズが包含する6つのステージ
                1. 研究対象の定義
                2. 検索戦略の開発
                3. 研究の選択プロセスを特定
                4. 品質評価ガイドラインの確立
                5.  データ抽出手法の確立
                6. 収集したデータの統合
        2. 実行（conducting）
        3. 報告（reporting）

以下の図（Fig. 3）のようにSLRが実施された

![Fig. 3. The Stages of Performing Systematic Literature Review](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr3_lrg.jpg)

Fig. 3. The Stages of Performing Systematic Literature Review

目標を設定し，それを中心にリサーチクエスチョン（[research question](https://www.enago.jp/academy/how-to-develop-good-research-question-types-examples/)）を組み立て，さらにそれを絞り込んでいった

検索戦略（[search strategy](https://kotobank.jp/word/%E6%A4%9C%E7%B4%A2%E6%88%A6%E7%95%A5-1702629)）とは，適切な検索語句を選択することであり，その検索語句を利用すれば，本調査に関連する記事を発見することができる

調査手法を下の図（Fig. 4）に示す

![Fig. 4. Applied Research Methodology](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr4_lrg.jpg)

Fig. 4. Applied Research Methodology

### 4.1. Research questions

調査する目的は

- 金融取引においてAIがどのように活用されているのか
- どのような主要な機械学習アルゴリズムが採用されているのか
- その精度はどの程度なのか
- 提示されたデータに対してどのような学習モデルが受け入れられるのか
- そしてどのモデルがトレーダーに最もリターンをもたらすのか

としており，金融取引の自動化の側面にも目を向けたい

1. **RQ１：**
    1. **調査対象となる取引市場の種類は何か？**
    2. **どの資産を検討しているか？**
2. **RQ２：**
    1. **ファンダメンタルまたはテクニカルな取引分析アプローチが考慮されているか？**
    2. **その場合、どのようなテクニカル指標を使用しているか？**
    3. **ファンダメンタル分析の情報源は何か？**
    4. **提案されているソリューションは自動化をサポートしていますか？**
3. **RQ３：**
    1. **どの種類のAIアプローチが採用されているか？**
    2. **どのようなしゅほうが使われているのか？**
4. **RQ４：**
    1. **モデルの性能に関するテストと評価の指標は？**

### 4.2. Search strategy

本調査で使用した検索方法についての詳しい説明は以下を参照されたい

1. Search terms
    
    検索語句は次の3つの要素によって決定される
    
    1. 主要な検索語句を決定するためにリサーチクエスチョンを利用する
    2. 新鮮な語句は専門的なリソースから発見する
    3. 検索結果を限定するためにブール演算子（ANDとOR）を使用する
    
    以下は，実際に使用した検索語句である
    
    - “AI” **OR** “Artificial intelligence” **AND** “trading” **OR** “AI-based trading”
    - “Machine learning” **AND** “trading”
    - “Deep learning” **AND** “trading”
    - “Deep neural network” **AND** “trading”
    - “High-frequency trading” **AND** “artificial intelligence” **OR** “AI”
    - “High-frequency trading” **AND** “machine learning”
    - “Reinforcement learning” **OR** “transfer learning” **AND** “trading”
    
2. Survey resources
    
    必要な研究論文を見つけるため，以下のデジタルライブラリを参照した
    
    - IEEE Explorer
    - Springer
    - Elsevier Science Direct
    - ACM Digital Library
    - MDPI
    
3. Search phase
    
    [上記](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-1-EN-20c42b38f4bb81e5b565e90a2b501f24?pvs=21)の検索条件を用いて、関連する電子図書館から研究論文を検索した
    
    次の段階では，組み入れ／除外の基準について説明する
    
    組み入れと除外の基準に基づいて，この調査では143のソースを用いた
    

### 4.3. Study selection

検索条件を用いて，およそ940の論文のリストを入手した

しかしながら，これらの論文を精査し、本研究に関連するものだけが残るようにした結果、2015年から2023年までに発表された論文は143本になった

付録Aの Figure 21 は，選択された論文の年度ごとの分布を示している

![Fig. 21. Distribution of Selected Papers per Year](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr21_lrg.jpg)

Fig. 21. Distribution of Selected Papers per Year

以下は，濾過（filtration）と選択のプロセスについての説明である

1. 様々なライブラリや著者から集めた重複記事を削除する
2. 包含基準と除外基準を用いて、不要な論文を削除し、包含基準に合致する論文を残す
3. 品質評価ガイドラインに従って出版物を収録し、質の高い論文を維持する
4. 類似記事の検索を続け、これらの新しい記事についてステップ3と4を繰り返す

Table 4 では，組み入れ／除外フェーズで用いた基準について示す

除外基準

- 次の内容を含まない機械学習の論文
    - 金融資産価格予測
    - センチメント分析
    - ポートフォリオ最適化
- 機械学習を価格予測に用いていない論文
- 査読を受けていない出版物

包含基準

- 機械学習が次に関係している
    - 価格／トレンド予測
    - ニュース
    - ソーシャルメディアのセンチメントモニタリング
    - ポートフォリオ最適化
- 機械学習を用いる場合と機械学習を用いない場合で，手法の比較をしている
- 2015年に発表された記事のみを考慮
- ジャーナルや学会の記事のみを含める

### 4.4. Quality assessment rules（QARs）

**QAR１：研究目的は認知されているか**

**QAR２：取引資産は特定されているか**

**QAR３：取引戦略と取引アプローチの種類は定義されているか**

**QAR４：提案手法の利点は十分に説明されているか**

**QAR５：提案手法の限界について十分に説明されているか**

**QAR６：提案手法は十分に設計され，正当化できるのか**

**QAR７：評価指標とテスト結果は報告されているか**

**QAR８：その提案手法の評価指標は適しているか**

**QAR９：その評価指標は他の手法と比較されているか**

**QAR１０：全体を通して，その研究は学術界や産業界を豊かにするか**

最終的にQARは、研究課題に対する回答として得られた論文の受容性を評価するために採用される

10個のQARが設けられ，それぞれが１ポイントを獲得し，合計１０ポイントとなる

以下の公式は，スコアの算出方法である

- 完全に回答している（completely responded）：1.00
- 平均以上（above average）：0.75
- 平均（average）：0.50
- 平均以下（below average）：0.25
- 回答しなかった（non answered）：0.00

論文のスコアは，この合計で算出される

論文のスコアが５ポイント以上となれば検討の対象となり，そうでなければ除外される

付録Aの Table 9 には，選択された研究トン分とそのQARスコアが示されている

### 4.5. Data extraction strategy

完成した論文リストは、このレベルの一連のリサーチクエスチョンに取り組むために必要な情報を抽出するために利用された

また，以下のデータ

- 論文ID
- 論文タイトル
- 出版年
- 出版タイプ
- 出版元
- RQ1
    - 取引タイプ
    - 金融資産
- RQ2
    - AIアプローチ
    - モデル
    - 自動化
- RQ3
    - 分析タイプ
    - テクニカル指標
    - ファンダメンタル分析元
- RQ4
    - 評価指標
    - テスト
    - 時間枠
    - データセット
- RQ5
    - 今後の課題

を各論文から検索した

また，すべての論文がリサーチクエスチョンに対応しているわけではないことも特筆に値する

以下の情報は，選択された研究論文から取得された

1. 金融市場の取引（株式市場，為替，暗号通貨，将来の指数（[future index](https://www.sciencedirect.com/topics/economics-econometrics-and-finance/index-futures)）など）
2. 取引された資産の種類
3. AIアプローチ（機械学習、深層学習、強化学習など）を利用し、モデルを実施する
4. 使用する取引分析の種類（ファンダメンタル分析、テクニカル分析、取引戦略）。
5. システムの特徴と出力（正確な価格の予測，トレンドの予測，アクションの自動化）
6. 利用したデータセット，ソース，選択された時間枠
7. 収益性とモデルのパフォーマンスの評価指標
8. 出版物の種類（ジャーナル・会議・ワークショップ）
9. 出版物の名前
10. 長年にわたる論文の流通

### 4.6. Synthesis of extracted data

選択した出版物から検索したデータから、RQに答える証拠を集めるために、いくつかのアプローチを採用した

以下のセクションでは、各リサーチクエスチョンに使用した合成技術について説明する

RQ1～RQ3についてはナラティブ・シンセシス・アプローチ（[narrative synthesis approach](https://unimelb.libguides.com/whichreview/narrativesynthesis)）を採用し、各リサーチクエスチョンに関する様々な知見間の統計的比較を行うためにデータを集計した

RQ4の場合、検索されたデータには、評価指標の種類のような定性的なものもあれば、期間のような定量的なものもあった

そのため、結果の比較には二項対立の結果を用いた。最後に、RQ5については、質的データ統合戦略の一つとされる相互翻訳アプローチ（Kitchenham, 2007）を用いて、今後の方向性や困難な点を様々な形で記述した

## 5. Results and discussion

このセクションでは，SLRの結果と調査結果を提供する

この考察は，研究で提起されたリサーチクエスチョンに基づいて整理されている．

分析結果の詳細について説明する前に，読者を後のセクションへと案内するための結果の構造の運類について表現している Fig 5 を提供する

![Fig. 5. Taxonomy of the Results and Discussion](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr5_lrg.jpg)

Fig. 5. Taxonomy of the Results and Discussion

### 5.1. Trading market types and asset types

研究者によって研究される取引市場に対する本SLRの調査においては，選ばれた論文を分析して，Fig 6 によって，市場ごとの頻度を表しているヒストグラムをプロットした．

![Fig. 6. Frequency Histogram of the Studied Trading Markets](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr6_lrg.jpg)

Fig. 6. Frequency Histogram of the Studied Trading Markets

 本SLRの調査結果は、研究者が8つの異なる金融市場を幅広く研究していることを明らかにした

株式市場は、研究者の間で最も広く研究されている市場に浮上した

これに続き，外国為替（[FOREX](https://www.ig.com/jp/ig-academy/introducing-the-financial-markets/what-is-forex)＝FOReign EXchange）市場や暗号通貨取引も文献において大きな注目を集めている

この3つの市場は、この分野における研究努力の主要な焦点として際立っている

さらに、2つの市場を組み合わせて調査した研究論文を6本確認した

それらの組合せはとして，

- 株価指数先物　と　商品先物市場
- 株式市場　　　と　商品先物市場
- 株式市場　　　と　上場投資信託（ETF）
- 株式市場　　　と　債券市場
- 株式市場　　　と　暗号通貨取引

などがある（Taghian et al. 2022）

研究者は、多様な取引市場を分析することで、各市場特有のダイナミクス、パターン、戦略を洞察することを目指している

 このような広い範囲によって、さまざまな資産クラスとその相互関係を包括的に理解することができ、より強固で適応性の高い取引モデルの開発が容易になる

株式市場、外国為替市場、暗号通貨取引で使用される取引資産について分析した結果、以下のような知見が得られた

Table 5に詳細を示すように、さまざまな資産を分類し、その頻度を調べた

---

Table 5. Frequency of Stock Assets Utilized.

**Category**

**Major Stock Indices**

**Miscella-neous**

**Stock**

S&P 500

30 Dow

Nasdaq

CSI300 index

FTSE index

DJI

Nifty

SEE and SZSI

NYSE

BSE SENSEX

OMXS30

VN-index

Shanghai Composite Index

EuroStoxx50

Moscow Stock Exchange index

**Percentage**

BATS

RTS Index

HDI

EuroStoxx50

Shanghai Composite Index

**Percentege**

**Freq.**

21

8

8

4

3

3

3

5

2

2

1

1

1

1

1

**61%**

1

1

1

1

1

**6%**

**Category**

**Other
Companies**

**Exchanges and Banks**

****

****

****

****

**Tech Companies**

**Stock**

IBM

RDSB

CICI Bank

AXP

KSS

ULVR

**Percentage**

China stock market

Indian stock price NSE

Taiwan stock index futures

Taiwan Stock Exchange

B3 - Brazil Stock Exchange

**Percentage**

GOOGL

TSLA

MSFT

AMZN

Meta Platform

**Percentage**

**Freq.**

1

1

1

1

1

1

6%

6

2

2

1

1

**11%**

7

6

1

1

1

**16%**

---

この分類プロセスでは、資産を主要株価指数、取引所、銀行、ハイテク企業、雑多な事業体といった明確なグループに分類した

調査結果は、選択された研究論文におけるこれらの資産の普及に光を当てた

表は、選択した研究論文で利用された株価指数の頻度を示している

これらの指数のうち、21の研究出版物がS&P500株価指数を最もよく使われる指数としている

そして，NasdaqとDow Jones Industrial Average（30 DOW）に関する8本の調査記事が続く

CSI300・FTSE・DJI・Nifty・SSE SZSE・NYSEは，調査された研究記事で異なる間隔で言及された他の主要な株価指数の一つであり、記事が世界の株式市場を幅広く表現していることに加勢している

ハイテク企業の分析は，本調査のハイライトの一つである

分析の結果、株式市場実験を行う研究者の間で、ハイテク企業株の利用頻度が高いことが示された

最も多く利用されたハイテク企業は、テスラ（TSLA）、アップル（AAPL）、グーグル（GOOGL）だった

グーグルを取り上げた研究は7件で、アップルを取り上げた研究は6件、テスラを取り上げた研究は1件だった

Amazon（AMZN）、Meta Platforms、Microsoft（MSFT）は、利用されたいくつかの重要なハイテク企業である

特定の銀行や証券取引所もこの調査で注目された

注目すべき例はインドのNSE株価と中国の株式市場で、それぞれ2本と6本の研究記事で取り上げている

台湾証券取引所、B3-ブラジル証券取引所、台湾株価指数先物は、カバーする国際金融市場の幅を大幅に広げた

金融リサーチの予測は主に主要株価指数、ハイテク企業、取引所、銀行に焦点を当て、その割合は61%、16%、11%である

外国為替市場では、取引には通貨ペアが含まれる

 Fig. 7は、研究者によって研究された、最も頻繁に取引されている通貨ペアを示している

![Fig. 7. FOREX Currency Pairs Frequency Distribution.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr7_lrg.jpg)

Fig. 7. FOREX Currency Pairs Frequency Distribution.

この図から、調査記事で最も多く利用されている通貨ペアは、EUR/USD・GBP/USD・EUR/GBPであることがわかる

Fig. 8 は、FOREX 市場における各通貨の利用をさらに探るために、選択した研究論文における通貨頻度の分布を円グラフで表したものである

![Fig. 8. Currency Trading Frequency.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr8_lrg.jpg)

Fig. 8. Currency Trading Frequency.

この図は

米ドル（USD）、ユーロ（EUR）、ポンド（GBP）が最もよく研究された通貨であり、それぞれ研究論文の26％、22％、13％を占めていることを強調している

一方、シンガポール・ドル（SGD）と中国人民元（CNY）は、外国為替市場で最も研究されていない通貨のひとつであった

暗号通貨市場において、Fig. 9は選択された研究論文で利用されたデジタル通貨の分布の概要を示している

![Fig. 9. [Cryptocurrency](https://www.sciencedirect.com/topics/economics-econometrics-and-finance/cryptocurrency) Frequency Distribution.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr9_lrg.jpg)

Fig. 9. [Cryptocurrency](https://www.sciencedirect.com/topics/economics-econometrics-and-finance/cryptocurrency) Frequency Distribution.

ビットコイン（BTC）、イーサリアム（ETH）、ライトコイン（LTC）が最も多く、それぞれ19本、9本、8本の研究論文に登場した

 暗号通貨ペア取引所について研究した研究者がいることは特筆に値する

例えば、

- [**Using machine learning for cryptocurrency trading**](https://ieeexplore.ieee.org/abstract/document/8780358)
J. Sun, Y. Zhou, and J. Lin
- [**Impact of real-world market conditions on returns of deep learning based trading strategies**](https://ieeexplore.ieee.org/abstract/document/9590955)
M. Corletto, M. Kissel, and K. Diepold

にあるように、暗号通貨取引におけるAI技術の応用において、いくつかの研究論文がBTC-USDTペアを実装している

研究者は、各市場におけるこれらの特定の取引資産を調査することにより、そのユニークな特性、市場行動、潜在的な取引戦略に関する洞察を得ることを目的としている

この詳細な分析により、各市場の状況において、より的を絞った効果的なAIベースの取引モデルの開発が可能になる。

### 5.2. **Trading analysis methods**

このリサーチ・クエスチョンでは、さまざまな取引分析をAI技術と組み合わせて実施することを目指す

Fig. 10は、取引市場においてAIを導入する際に利用される取引分析タイプの頻度に関する洞察を提供する

![Fig. 10. Trading Analysis Methods Implemented in Selected Research Articles.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr10_lrg.jpg)

Fig. 10. Trading Analysis Methods Implemented in Selected Research Articles.

図によると、テクニカル分析、取引戦略、ファンダメンタル分析が、機械学習技術と組み合わせて実施される主な分析手法である

その中でも、テクニカル分析が最も広く利用されており、選択された論文の71%に登場している

一方、ファンダメンタル分析は研究論文の12%で採用されており、テクニカル分析よりも普及していないことがわかる

さらに、テクニカル分析とファンダメンタルズ分析を組み合わせた研究論文も5％あった

さらに、研究論文の1%ほどの部分集合（subset：サブセット）は、特定の取引戦略に焦点を当てると同時に、ファンダメンタル分析の領域に属するニュースの影響についても研究している。

 ニュースのセンチメントとその取引判断への影響を組み入れることは特に価値がある

 また、テクニカル分析を導入した取引戦略に焦点を当てた論文も1％あった

ファンダメンタル分析のためにニュースデータを入手する場合、最も広く使われている情報源はBloomberg・Thompson Reuters' news sentiment・Yahoo Financialsなどである

これらの情報源は、ニュースが金融市場に与える影響を研究・分析するために必要な情報を研究者に提供している

さまざまな取引分析タイプをAI技術とともに使用することは、取引戦略を強化するための研究者の多様なアプローチを反映している

テクニカル分析が主流である一方、ファンダメンタル分析、トレーディング戦略、そしてこれらの手法を組み合わせることで、トレーディング市場の様々な側面を探求するAI技術の統合が示される

選択した研究論文で使用されたテクニカル指標の頻度を分析するために、Fig. 11を示す

![Fig. 11. Technical Analysis Indicators Types Frequency.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr11_lrg.jpg)

Fig. 11. Technical Analysis Indicators Types Frequency.

図では、テクニカル指標を大きく3つのタイプに分類している

1. Momentum/Oscillator
2. Trend
3. Volume/Volatility

また、各テクニカル指標の出現頻度をTable 6に示す

---

Table 6. Methods Implemented in Each Indicator Type.

**Indicator**

Momentum/Oscillator

Trend

Volume/Volatility

Others：sentiment, valuation, Strategy

**Frequency**

67

41

22

21

**Method**

RSI, MACD, CCI, etc.

MA, SMA, EMA, etc.

OBV, ATR, PVI, NVI, etc.

ISE, P/CF, stop loss strategy, etc.

---

モメンタム指標（Momentum indicators）は、資産価格の強弱を評価するためによく使われる

これらの指標は、物価の上昇率や下落率を特定するのに役立つ

選択した論文で頻繁に使用されたモメンタム指標には、

- 移動平均収束ダイバージェンス（Moving Average Convergence Divergence：MACD）
- 相対力指数（Relative Strength Index：RSI）
- コモディティ・チャネル指数（Commodity Channel Index：CCI）

がある

これらの指標は、値動きの勢い（momentum）を洞察し、トレーダーが十分な情報に基づいた意思決定を行うのに役立つ

トレンド指標（Trend indicators）は、トレンドの方向性を判断するために利用される

これらの指標は、市場が上昇トレンドにあるのか下降トレンドにあるのかを見極めるのに役立つ

選択した論文で一般的に採用されているトレンド指標には、

- 移動平均 （Moving Average：MA）
- 単純移動平均（Simple Moving Average：SMA）
- 指数移動平均（Exponential Moving Average：EMA）

があり，これらの指標は、トレンドの方向性や反転の可能性について貴重な情報を提供します

これらの指標は、トレンドの方向性や反転の可能性について貴重な情報を提供する

出来高指標（Volume indicators）は、資産の強気・弱気を見極める上で極めて重要である

アナリストが市場の売り買いの圧力を判断するのに役立つ

出来高指標は、特定の証券（security）の活動や参加者のレベルを測るものである

研究者が採用する出来高指標の例としては、

- オン・バランス・ボリューム（On Balance Volume：OBV）
- アベレージ・トゥルー・レンジ（Average True Range：ATR）
- ポジティブ・ボリューム・インディケーター（Positive Volume Indicator：PVI）
- ネガティブ・ボリューム・インディケーター（Negative Volume Indicator：NVI）

などがあり，これらの指標は、トレーダーが市場参加者の感情や心情を理解するのに役立つ

ボラティリティ指標（[Volatility](https://money-voyage.mizuho-sc.com/articles/83) indicators）は、特定の市場のボラティリティが高い時期や低い時期を特定するのに役立つ

トレーダーがリスクレベルと潜在的な価格変動を評価するのに役立つ

研究者が採用するボラティリティ指標には

- アベレージ・トゥルー・レンジ（[ATR](https://www.avatrade.co.jp/about/kojiro/kojiro13)）
- ボリンジャーバンド
- 標準偏差

などがある

選ばれた論文にある様々なテクニカル指標は、値動きと市場力学を分析することの重要性を示している

モメンタム、トレンド、出来高、ボラティリティの各指標を取り入れることで、研究者は市場行動に対する洞察を深め、より多くの情報に基づいた取引判断を下すことを目指している

一般にOHLC（Open、High、Low、Close）と呼ばれる市場情報は、どのモデルにとっても主要なインプットである

- Open：資産の初期価格
- Close：資産の最終価格
- High：到達したピーク価格
- Low：資産の市場活動中に観測された最低価格

データの粒度は、価格が収集される時間枠によって異なり、年単位、月単位、週単位、日単位、時間単位から分単位まで様々である

データの粒度の選択は、意図する予測目標に依存する

長期投資の場合、月次や週次など粒度の低いデータを選択することで、シグナルを平滑化し、ノイズを減らし、データセットサイズを小さくすることで計算要件を最小化することができる

逆に、短期投資や日中のスキャルピング戦略（[scalping strategies](https://www.investopedia.com/articles/trading/05/scalping.asp)）には、より粒度の高いデータが有効である

しかし、粒度の高いデータは、モデルによる追加的な信号の捕捉を可能にするものの、より多くのノイズをもたらすことに注意することが重要である

したがって、ノイズと信号の比率のバランスを取ることが重要になる

市場価格データに加えて、研究者は一般的に様々な取引分析タイプを予測モデルに組み込んでいる

テクニカル分析では、モデルを訓練するためのインプットとして、主要市場価格に加えて、投資計画に沿った特定の指標を含める

一方、ファンダメンタルズ分析を採用する研究者もおり、これはニュース記事をウェブスクレイピングして価格に影響を与える要因を特定するものである

彼らはこのニュースデータと市場情報を組み合わせてモデルを作成する

もう1つのアプローチは、テクニカル分析とファンダメンタル分析を市場データとともに活用することである

これらのモデルのアウトプットは研究者によって異なるが、最終的な目標は収益性を最大化することである

 研究者の中には、過去のデータを使ったモデルの予測に基づいて、買い、売り、保有などの行動をとるのに最も適した時期を決定する戦略を採用する者もいる

また、上昇トレンドであれ下降トレンドであれ、全体的なトレンドを予測することに重点を置くものもあれば、ロング、ショート、ポジションのホールドなど、トレーダーが推奨するポジションを予測することを目的とするものもある

あるいは、価格の予測に重点を置いたり、成功率や利益率を重視したりするモデルもある

Fig. 12は、インプットとアウトプットとしてのモデルのさまざまなアプローチを示している

![Fig. 12. Utilizing Trading Analysis in AI.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr12_lrg.jpg)

Fig. 12. Utilizing Trading Analysis in AI.

これらのモデルの中には、予測された行動を直接実行することで自動化を取り入れたものもある

Fig. 13は、自動化を導入し、完全に機能する取引システムを開発した論文の割合を示している

![Fig. 13. The Percentage of Automated Solutions of Selected Research Articles.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr13_lrg.jpg)

Fig. 13. The Percentage of Automated Solutions of Selected Research Articles.

興味深いことに、調査した研究論文の半数以上は、ソリューションに自動化を採用していなかった

モデルによって予測された行動を自動化した研究論文は、全体のわずか16％に過ぎない

しかし、22％のソリューションはエージェント・ベースのシステム（[agent-based system](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%83%BB%E3%83%99%E3%83%BC%E3%82%B9%E3%83%BB%E3%83%A2%E3%83%87%E3%83%AB)）を導入しており、モデルは取引環境との相互作用を通じて学習し、パフォーマンスを向上させている

このアプローチは、リアルタイムのフィードバックに基づく適応的な意思決定を可能にする

### 5.3. **AI approach and algorithm techniques**

本研究の重要な発見の1つは、金融取引分野で最も一般的に採用されているAI技術を特定すること

特徴抽出、前処理、分析を含む実験のさまざまな段階を通じて、文献に記載されている方法論と実装を徹底的に検討した

Fig. 14は、金融市場の取引に使われるAIのアプローチを分類したもので、分類、回帰、深層学習、強化学習、深層強化学習の5種類に分類できる

![Fig. 14. AI Type Implementation by Selected Research Articles.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr14_lrg.jpg)

Fig. 14. AI Type Implementation by Selected Research Articles.

各アプローチについて、金融取引への応用とともに以下に説明する

- **分類**（**Classification**）
    
    本調査でレビューした記事の10％は、データをあらかじめ決められたクラスやカテゴリーに分類することを含む分類技術を使用していた
    
    これらのアルゴリズムは、トレーディングにおいて、資産の値動きを予測する能力に基づいて、可能性のある取引を「買い」または「売り」のグループに分類するために使用される可能性がある
    
- **回帰**（**Regression**）
    
    回帰法は、株価の将来価格のような連続的な結果を予測するために、選ばれた論文の2%で使われている
    
    回帰分析は、採用率が低いにもかかわらず、市場の価格パターンや変動に関する本質的な洞察を提供することができる
    
- **深層学習（Deep Learning）**
    
    深層学習アルゴリズムは膨大な量の非構造化データを処理できるため、複雑な取引パターンの特定、値動きの予測、市場心理の分析に特に役立つ
    
- 強化学習（**Reinforcement Learning**）
    
    記事の29％がこの手法を使っており、アルゴリズムが試行錯誤を経て最良の行動方針を見つけ、総報酬を最大化するように訓練されている
    
    これらのアルゴリズムは、市場のパフォーマンスに応じて動的に戦略を変更することにより、取引における長期的な利益を最適化することができる
    
- **深層強化学習（Deep Reinforcement Learning）**
    
    この戦略も研究の29％で使われており、強化学習の意思決定能力とディープラーニングのパターン認識能力を組み合わせたものだ
    
    その結果、変化する市場環境に適応できる自律的な取引システムを構築するのに最適である
    

これらの結果は、この領域では、深層学習、強化学習、およびそれらの組み合わせが、分類や回帰の手法よりも好まれ、より適切であると考えられていることを示している

このようなアプローチが好まれるのは、金融市場がいかに複雑で、環境の変化を理解し適応できる高度なAI手法がいかに求められているかを強調している

Fig. 15は、金融取引市場で長年にわたって使用されてきた手法の分布について、さらなる洞察を与えてくれる

![Fig. 15. Distribution of AI Implementation Types per Year.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr15_lrg.jpg)

Fig. 15. Distribution of AI Implementation Types per Year.

それによると、深層強化学習は2019年に注目を集め始め、2020年には研究者の間で最も高い人気を獲得することが明らかになった

一方、強化学習は2018年と2021年に最もよく使われたアプローチだったが、2022年にはディープラーニングに追い抜かれた

Fig. 16は、金融取引市場を予測するためのAI技術とアルゴリズムの概要を示している

![Fig. 16. AI Techniques utilized in Financial Trading Markets.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr16_lrg.jpg)

Fig. 16. AI Techniques utilized in Financial Trading Markets.

我々の研究では、調査した研究論文から40近くの主要な手法を特定した

これらの手法は、以下の4つのアプローチに大別できる

- 統計的時系列分析
    - 統計的時系列のカテゴリーには、移動平均を用いた自己回帰のようなアルゴリズムがある
    - コピュラ統計的手法（[copula statistical method](https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%94%E3%83%A5%E3%83%A9_(%E7%B5%B1%E8%A8%88%E5%AD%A6))）は、リスク分析や金融モデリングに頻繁に応用されている
        - 主に多くの確率変数間の関係をシミュレートするために使用される
        - 変数の周辺分布はわかっているが、依存構造が複雑すぎて従来の統計手法では表現できない場合、コピュラ関数を使えば変数間の複雑な相互作用をモデル化することができる
        - コピュラは、AIの文脈で使用できる統計的時系列分析ツールである
        - しかし、これはAIに特化した技術ではなく、統計分析ツールである
        - 機械学習、深層学習、強化学習などのAIアプローチと組み合わせることで、金融取引のモデリングや予測能力を向上させることができる
- 古典的機械学習
    - 古典的な機械学習における分類、アンサンブル、回帰、クラスタリングにアルゴリズムを分類した
- 深層学習
    - 深層学習技術は、金融取引において大きな注目を集めており、畳み込みニューラルネットワーク（convolutional neural networks）、リカレントニューラルネットワーク（recurrent neural networks）、生成的敵対ネットワーク（generative adversarial networks）などのニューラルネットワークアルゴリズムがある
    - 特に、LSTM（Long Short-Term Memory：長期短期記憶）ネットワークは、時間依存性を捉えることができるため、その利用が広まっている
- 強化学習
    - 強化学習アプローチは、金融取引の予測においても注目されている。
    - 強化学習アルゴリズムは、オンポリシー（[on-policy](https://qiita.com/abmushi/items/83a639506fcbc4050ce8)）またはオフポリシー（[off-policy](https://qiita.com/abmushi/items/83a639506fcbc4050ce8)）のどちらかのポリシーに基づくことができる
    - 注目すべきアルゴリズムには、[Deep Q Network](https://ai-kenkyujo.com/programming/kyoukagakusyu/deep-q-network-toha/)（DQN）、[Deep Deterministic Policy Gradient](https://qiita.com/shionhonda/items/ec05aade07b5bea78081#ddpg)（DDGP）、アクター・クリティック・アルゴリズム（[actor-critic algorithms](https://deus-ex-machina-ism.com/?p=58446)）などがある
        - これらの強化学習技術は、取引環境との相互作用から学習することにより、効果的な取引戦略を開発するために適用されている

多くの研究論文が、複数のアルゴリズムを組み合わせたハイブリッド・アプローチを実装していることは特筆に値する

例えば、(Yuan et al., 2020)では、DQNとソフト・アクター・クリティック([SAC](https://qiita.com/ku2482/items/fb79d8209f1162d9f141))を用いたProximal Policy Optimization([PPO](https://qiita.com/pocokhc/items/1a68dc661eaa98dcacb2))のハイブリッド実装が利用された

- [**Using Data Augmentation Based Reinforcement Learning for Daily Stock Trading](https://www.mdpi.com/2227-7390/13/3/347)**
Y. Yuan, W. Wen, and J. Yang

特徴選択はクラスタリング技術を用いて行われ、Twin-Delayed Deep Deterministic Policy Gradient（TD3）が採用された(Park and Lee, 2021)

- [**Practical algorithmic trading using state representation Learning and imitative reinforcement Learning](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9611246&utm_source=sciencedirect_contenthosting&getft_integrator=sciencedirect_contenthosting)**　
D.Y. Park, K.H. Lee

さらに、ある論文では、[finBERT](https://book.st-hakky.com/purpose/japanese-bert-model-sentiment-analysis-fine-tuning-training/)として知られる変換モデルを利用し、ニュースヘッドラインのセンチメントを研究することでファンダメンタル分析を組み込んでいる

これと並行して、LSTM、CNN、多層パーセプトロン（MLP）アルゴリズムが予測に採用された（Passalis et al.）

- [**Learning sentiment-Aware trading strategies for bitcoin leveraging deep Learning-based financial news analysis](https://link.springer.com/chapter/10.1007/978-3-030-79150-6_59)**
N. Passalis, S. Seficha, A. Tsantekidis, A. Tefas

これらの多様な手法とハイブリッド・アプローチは、統計的手法、機械学習、深層学習、強化学習手法を包含する、金融取引におけるAIアプリケーションの進化する性質を浮き彫りにしている

これらの手法の選択と組み合わせは、具体的な研究目的と分析対象の金融市場の特性によって異なる

### 5.4. Performance metrics and evaluation

AIパイプラインのワークフローにおいて、モデル性能の評価は極めて重要なステップである

このリサーチクエスチョンでは、提案された手法やテクニックの効率を測定・評価するために一般的に採用されているパフォーマンス指標を調査することを目的としている

よく知られたAI評価指標のいくつかは、特にモデル予測の品質を評価するために設計されている

Fig. 17は、AIモデルの性能をテストするために使用される評価指標の頻度に関する洞察を提供する

![Fig. 17. Frequency of AI Evaluation Metrics.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr17_lrg.jpg)

Fig. 17. Frequency of AI Evaluation Metrics.

図によると、分類の中で最も一般的に採用されているメトリクスは

- accuracy
- recall
- [F-measure](https://atmarkit.itmedia.co.jp/ait/articles/2210/24/news034.html)

などである

多くの研究論文がこれらの評価方法を2つ以上組み合わせて採用していることに注目するべき

さらに、いくつかの研究者は、彼らの提案するアプローチのパフォーマンスを、単に売買を行うゼロインテリジェンス戦略（[zero-intelligence strategy](https://capital.com/zero-intelligence-trader-definition)）と比較している

この比較は、伝統的なバイ・アンド・ホールド戦略（[buy-and-hold strategy](https://www.smbcnikko.co.jp/terms/japan/ha/J0367.html)）に対するAIアプローチの優位性を浮き彫りにしている

最も広く使われている評価指標は、回帰指標に分類される二乗平均平方根誤差（Root Mean Square Error：RMSE）である。

しかし、研究者にとっては、財務的な観点からもモデルを評価することが不可欠である

この点に対処するため、財務パフォーマンスを評価するために最も一般的に使用されているパフォーマンス指標をTable 7に示す

---

Table 7. Frequency of Investment Performance Metrics.

**Investment performance**

Sharpe Ratio

Rate of Return（RoR）

Maximum Drawdown

Total return

Total profit（Net profit）

Yield volatility

Average profit

Profit and loss diagram

Sortino Ratio

# of transactions

Cumulative returns

Loss percentage

**Freq.** 

53

37

30

30

26

23

16

16

14

13

12

6

**%**

18

12

10

10

9

8

5

5

5

4

4

2

---

---

**Investment performance**

Return on Investment（ROI）

Value at Risk（VaR）

Winning Rate

Information ratio

Maximum Capital

Calmar Ratio

Sterling ratio

# of positions/actions

Minimum Capital

Excess return rate

Accumulated portfolio value

Kolmogorov-Smirnov statistics

**Freq.**

4

3

3

3

2

2

2

2

1

1

1

1

**%**

1

11

1

1

1

1

1

1

0

0

0

0

---

指標には，以下の指標が含まれる

- シャープレシオ（Sharpe Ratio）
- 収益率（Rate of Return：RoR）
- 最大ドローダウン（Maximum Drawdown）
- トータルリターン（Total return）

これらの指標は、提案されたモデルのリスク調整後リターン、全体的な収益性、財務的な実行可能性についての洞察を提供する

AIと財務の両方の観点から評価指標を採用することで、予測精度と、提案された戦略に関連する財務上の利益または損失の両方を包含する、モデルのパフォーマンスの包括的な評価が保証されます

取引戦略のパフォーマンスを検証するには、いくつかの著名なテスト手法がある

- バックテスト（Backtesting）
    - 広く利用されている強固な評価方法
    - 過去の追加データで予測モデルのパフォーマンスをテストする
    - トレーダーは実際の資金をリスクにさらすことなく、戦略の有効性を評価できる
    - モデルが過去にどの程度のパフォーマンスを示したかについての貴重な洞察を提供する
- フォワードテスト（forward testing）
    - 新しいデータが入手可能になると、取引戦略をリアルタイムで再現可能
    - 実際の資金を使わずに実際の取引状況をシミュレートするため、ペーパートレーディング（paper trading）とも呼ばれる
    - トレーダーに，バックテストで使用される過去のデータに由来しない追加の分析サンプルを提供する

バックテストとフォワードテストの両方が一般的に採用されているが、文献ではバックテストの方がより広く採用されている

(Kim, Aug.2021）に代表されるように、約28の論文が取引戦略を検証するためにバックテストを行っている

- [**Adaptive trading system integrating machine learning and back-testing: korean bond market case](https://www.sciencedirect.com/science/article/abs/pii/S0957417421002086)** 
M. Kim

一方、（Żbikowski, 2016）で実証されているように、戦略を評価するためにフォワードテストを利用した研究論文は5本程度と少なかった

- [**Application of Machine Learning Algorithms for Bitcoin Automated Trading](https://link.springer.com/chapter/10.1007/978-3-319-30315-4_14)**
K. Żbikowski

これらのテスト手法は、トレーディング戦略のパフォーマンスと実行可能性を評価する上で重要な役割を果たし、トレーダーに過去とリアルタイムの条件下での有効性に関する貴重な洞察を提供します

調査中、研究者がデータを得るために利用するデータセットの情報源を30個特定した

Table 8は、選択した研究論文におけるこれらの情報源とその利用頻度の一覧である

---

Table 8. Frequency of Dataset Source.

**Source of Dataset**

Yahoo Finance

Investing.com

tushare

Dukascopy bank

kaggle

Metatrader

Bloomberg

Google Finance

Wharton Research Data Services

Binance

Thomason Reuters

Wind Database

Shanghai Stock Exchange

Nasdaq

Taiwan Stock Exchange

**Freq.**

18

5

4

4

4

4

3

3

2

2

2

2

2

2

2

**Source of Dataset**

International Settlements Triennial Central Bank

FactSet Research Systems

SpeedLab AG

Bombay Stock Exchange

AlphaVantage service

kaiko

Bitstamp

Global-View Forex Forum

Bincentive

National Stock Exchange

Market Watch

Binance

CoinMarketCap

Fxtree

**Freq.**

1

1

1

1

1

1

1

1

1

1

1

1

1

1

---

この表から、以下のことが分かる

- Yahoo Financeは市場データを入手するための信頼できる一般的な情報源である
    - その包括的なカバー範囲と入手可能性から、研究者の間で人気が高い
- Tushareは、4つの研究論文で利用されている
    - ウェブクローリング技術を使って過去の金融データを収集する中国の情報源である
    - 金融市場を研究するための貴重なデータソースとしての意義を浮き彫りにしている
- BloombergとGoogle Financeは、過去の財務データを入手するための評判の良い情報源である
    - 広範な財務情報を提供しており、この分野の研究からは信頼できるとみなされている

様々なデータソースの利用は、研究に必要なデータセットを得る上での研究者の多様なニーズと好みを反映している

特定のデータソースの選択は、データのカバー率、信頼性、アクセス性、特定の研究要件などの要因によって決まる。

全体的に、Yahoo Finance、Tushare、Bloomberg、Google Financeは、過去の市場や金融データを取得するための文献で頻繁に言及されている著名なソースの一つ

市場危機の影響を調べるために、使用したデータセットの年レンジを調査した

 Fig. 18は、選択された研究論文のデータセットがカバーしている年についての洞察である。

![Fig. 18. Year Period Range of Selected Dataset.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr18_lrg.jpg)

Fig. 18. Year Period Range of Selected Dataset.

この図から、ほとんどの論文が4年または1年の市場データを採用していることがわかる

このことは、市場のトレンドやパターンを分析するために、研究者が比較的最近のデータに注目することが多いことを示している

さらに、より長期的な展望を示唆する10年レンジを考慮した論文もある。

しかし、注目すべきは、データセットの時間範囲を大幅に広げた論文がいくつかあったことである

例えば、(Hirchoua et al., May 2021)は、包括的な歴史的視点を反映し、1960年から2019年の範囲を考慮した

- [**Deep reinforcement learning based trading agents: risk curiosity driven learning for financial rules-based policy**](https://www.sciencedirect.com/science/article/abs/pii/S0957417420311970)
B. Hirchoua, B. Ouhbi, B. Frikh

さらに、(AbdelKawy et al., 2021)と(Pendharkar and Cusatis, 2018)は、それぞれ1980年から2020年までと1976年から2016年までの40年間のデータセットを利用している

- [**A synchronous deep reinforcement learning model for automated multi-stock trading**](https://link.springer.com/article/10.1007/s13748-020-00225-z)
R. AbdelKawy, W.M. Abdelmoez, A. Shoukry
- [**Trading financial indices with reinforcement learning agents**](https://www.sciencedirect.com/science/article/abs/pii/S0957417418301209)
P.C. Pendharkar, P. Cusatis

これらの論文は、長期的なトレンドを把握し、より広い時間軸で危機の影響を調査することを目的としている

Fig. 19は、データセット範囲の開始年と終了年を示しており、選択された論文の対象期間を視覚的に表している

![Fig. 19. Selected Dataset Year Range.](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr19_lrg.jpg)

Fig. 19. Selected Dataset Year Range.

この可視化は、研究者が分析に選んだ特定の期間を理解するのに役立つ

さらに、FIg. 20は主要な危機イベントの年表であり、重大な市場危機の発生を示している。

![Fig. 20. Timeline of Crisis Events that Effected US Stock Market Provided by Sabrina Jiang ([Williams, 2022](https://www.sciencedirect.com/science/article/pii/S1319157824001046#b0755)).](https://ars.els-cdn.com/content/image/1-s2.0-S1319157824001046-gr20_lrg.jpg)

Fig. 20. Timeline of Crisis Events that Effected US Stock Market Provided by Sabrina Jiang ([Williams, 2022](https://www.sciencedirect.com/science/article/pii/S1319157824001046#b0755)).

このタイムラインは、市場価格に影響を与えることが知られている危機を含む期間を考慮して、研究者がどのようにデータセットの範囲を選択するかを観察するために使用することができる

データセットの年数を選択することで、研究者は関心のある特定の期間に焦点を当てることができ、市場危機の影響やその期間内のトレンドに関する洞察を得ることができる

## 6. Conclusion

この体系的な文献レビューでは、AI技術による金融取引のアプローチを研究した

金融取引市場にAI技術を導入した143の科学的研究論文をレビューしている

そこで、金融取引市場と資産タイプ、AI技術とともに考慮される取引分析タイプ、取引市場で利用されるAI技術、提案されたモデルの推定と性能指標といった観点から論文をレビューし、いくつかの知見と見解を示す

選ばれた研究論文は2015年から2023年の間に発表されたもので、このレビューは4つのRQに対応している

- 第１ののRQの結果は、AIの応用に利用される8つの金融市場を特定したことである
    - 最も広く研究されている市場は、それぞれ株式市場、外国為替市場、暗号通貨取引である
    - S&P株は株式市場で最も活用されている資産であり、FOREXの通貨ペアはEUR/USDである
    - 暗号通貨に関しては、最も使われているデジタル通貨はBTCである
- 第２のRQは、テクニカル分析の指標はファンダメンタル分析よりも望ましいというもの
    - また、ファンダメンタルズ分析は、取引戦略以上に採用されている
    - さらに、テクニカル指標の中で最も使用されているのは、モメンタム／オシレーター、特にRSIである
    - その上、AIにおけるこれらの分析方法は、モデルに与えられる市場情報であり、取引テクニカル指標、ファンダメンタル分析、またはその両方のタイプの入力として使用される
    - また、興味深い発見は、これらのソリューションのうち、取引プロセスを完全に自動化しているのはわずか16％しかないということだ
- 第３のRQに目を移すと、予測モデルの構築に広く実装されているAIアプローチはディープラーニングであり、30％の論文で利用されており、強化学習と深層強化学習がそれぞれ29％の論文で利用されている
    - 私たちは、これらのアプローチの年ごとの分布を提供し、このドメインにおける40の主要なAI技術を特定した
- 第４のRQは、これらのアプローチの評価を、モデルの性能評価と投資評価の2つの側面から提示した
    - RMSE、Accuracy、recall、F-measureは、最も一般的に使用されるモデル評価指標である
    - Sharpe ratio、rate of return、maximum drawdown、total returnは、最もよく利用される投資評価である
    - さらに、Yahoo Financeは、研究者が市場情報を入手するための最も広範なデータセットソースである
    - 調査した時系列データでは、4年と1年のデータ範囲が最も多かった
    - ここでは、価格に影響を与えた世界的な危機を含む年を紹介した

金融市場はその巨大な次元とさまざまな社会的影響から、非常に頻繁に利用され、危険な行為に対して脆弱であると考えられている

その結果、研究者はモデルのリスク制御行動にもっと焦点を当て、より多くのリスク回避選択を行えるよう、危機検出器を追加構築することを推奨する

さらに、この研究では、最適なモデルのトレーニング期間を決定するためのアプローチを構築する必要があることを発見した

最後に、今後の課題として、ファンダメンタル分析とテクニカル分析の両方を予測モデルに組み込んだ自動金融取引システムを開発し、研究発表に記載された手法のひとつと比較する予定である