# Reading Research Article About Financial Trading No.3 EN

# **Deep-learning-based stock market prediction incorporating ESG sentiment and technical indicators**

Haein Lee, Jang Hyun Kim & Hae Sun Jung 

[Deep-learning-based stock market prediction incorporating ESG sentiment and technical indicators](https://www.nature.com/articles/s41598-024-61106-2)

---

## Abstract

---

持続可能性が現代企業の発展において極めて重要な要素として浮上するにつれ、環境・社会・ガバナンス（ESG：Environmental, Social, and Governance）情報を財務評価に統合することが不可欠となっている

ESG指標は、企業の持続可能な慣行やガバナンスの有効性を評価する上で重要な指標となり、投資家の信頼や将来の成長性に影響を与え、最終的には株価に影響を与える

本研究では、ニュースから抽出したESGセンチメント指数をテクニカル指標と組み合わせ、S&P500指数を予測する革新的なアプローチを提案する

ディープラーニングモデルを活用し、最適なウィンドウサイズを探索することで、評価指標である平均絶対誤差（MAPE）を通じて最適なモデルを探索する

さらに、アブレーション・テスト（[ablation test](https://cvml-expertguide.net/terms/dl/misc/ablation/)）により、ESGの影響とS&P500指数との因果関係を明らかにしている

実験結果は、ESGセンチメントを考慮した場合、テクニカル指標や過去のデータのみに依存した場合と比較して、予測精度が向上することを示している

この包括的な手法は、短期的な変動を考慮するテクニカル指標と、長期的な効果をもたらすESG情報を統合することで、株価予測の優位性を高めている

さらに、投資家や金融市場の専門家に貴重な洞察を提供し、金融資産のESGを考慮する必要性を検証し、投資戦略や意思決定プロセスを開発するための新たな視点を導入している

## Introduction

---

サステナビリティは、現代企業の発展を形作る上で極めて重要な世界的な潮流である

持続可能な慣行がますます重視される中、環境・社会・ガバナンス（ESG）指標を統合して企業の業績を評価することは不可欠となっている[[1](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21),[2](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

ESG指標は、企業のESGパフォーマンスを測定し、業務慣行に関する貴重な洞察を提供する[[3](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

企業が持続可能なビジネスモデルを採用し、社会的責任を果たし、効果的なガバナンスを維持していれば、投資家はその企業に高い信頼を置き、将来の成長可能性を肯定的に評価できる[[4](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

このような将来の成長可能性に対するポジティブな認識は、企業の株価上昇につながる

その結果、ESG指標は投資家の意思決定に大きな影響を与え[[5](https://www.tandfonline.com/doi/full/10.1080/1226508X.2019.1643059)] 、企業に持続可能な慣行を積極的に採用し、ESG指標を改善するよう促すと同時に、持続可能な事業戦略が投資家と企業の双方にメリットをもたらすことを実証している

持続可能性とESG指標の相互関連と投資家の選択への影響は、財務評価にESG基準を組み込むことの重要性を高め、企業の責任と投資戦略の橋渡しをすることを浮き彫りにしている

さらに、金融市場がこうしたシフトに対応して進化する中、ESG指数を組み合わせてS&P500指数を予測することは、ESG要因が投資選択に影響を与えるようになっている状況を考慮した革新的なアプローチとなり得る[[6](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

ここでS&P500を予測対象としたのは、この指数が米国の経済状況や企業の健全性を表す重要な指標とされ、世界の株式市場の動向を反映するために用いられることがあるからである[7,8]

投資家の間では、企業のESGパフォーマンスが株価にどのような影響を与えるかを理解することへの関心が高まっており、金融領域におけるESG指標の重要性が高まっていることが浮き彫りになっている[[9](https://onlinelibrary.wiley.com/doi/abs/10.1111/FMII.12114),[10](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

ESG指標に加え、テクニカル指標も財務分析において重要な役割を果たしている[[11](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

これらの指標は、特定資産の過去の値動きや売買高などのヒストリカルデータを用いて算出され、過去の価格パターンやトレンドを考慮し、将来の動きを予測するために極めて重要である[[12](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

金融分析におけるテクニカル指標の基本的な重要性を考えると、ESG指標との統合は、本研究で提案された包括的なアプローチに代表されるように、大きな可能性を示している

したがって、S&P500指数を予測するテクニカル指標にESG情報を組み込んだ研究は、投資家や金融市場の専門家に革新的な方法論と貴重な洞察を提供することができる

この包括的なアプローチは、株式行動の予測に役立ち、投資戦略の策定や意思決定に新たな局面をもたらすことが期待される

実験では、S&P500指数の終値を予測するために18のテクニカル特徴を利用した

さらに、LexisNexisのニュースデータのセンチメント分析を通じて得られたESG関連のセンチメント情報をテクニカル指標と統合し、S&P500指数の将来値を予測する回帰モデルに適用し、平均絶対値誤差（MAPE）を評価指標として用いた

その結果、著者らは様々なウィンドウ・サイズとパラメータで検証を行い、最適な結果を得た

さらに、アブレーション・テストを実施することで、ESGのセンチメント情報を考慮することが、テクニカル指標や過去の価格データのみを使用するよりも効果的であることが検証された

## **Related works**

---

### Previous research on stock price prediction considering news text sentiment analysis

過去数年間に行われた研究では、ニュースセンチメントと株価の相関関係を調査するために多大な努力が払われてきた

ZubairとCios[[13](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]は、7年間にわたってロイター通信からニュースを収集し、Harvard General Inquirerを使って日次ベースでセンチメント分析を行った

著者らは、平滑化のためにカルマンフィルターを利用し、S&P500指数とセンチメントスコアの間に強い相関関係があることを明らかにした

KhedrとYaseen[[14](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]は、企業の配当、株式配当、株式合併に関するニュース記事からセンチメント指数を導き出した

筆者らは、オープン、クローズ、高値、安値などの数値データ属性を採用し、センチメント分析のためにナイーブベイズを組み込んだ2段階の手法を実装し、株価予測において89.80％の精度を達成した

LiとPan[15]は、今後の株式市場の動向を検出するために、ニュースデータと株式データの両方を修正し、アンサンブル法を導入した結果、ベースラインモデルと比較して平均二乗誤差（MSE）が57.55％減少した

最終的に、これらの研究は、ニュースデータ、センチメント分析、株価予測の間のダイナミックな相互作用を強調し、この分野で達成された様々なアプローチと重要な進歩を紹介している

### **Exploring the influence of ESG on the stock performance**

先行研究では、ESG要素が企業の評価と好感度の両方に影響し、株価に好影響を与える可能性があることが実証されている[[16](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21),[17](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

AlareeniとHamdan[[6](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]は、2009年から2018年にかけてS&P500指数に採用された企業を対象に、4869日間にわたるESG開示と企業業績指標の統計分析を行い、ESG開示が企業業績指標にプラスの影響を与えることを明らかにした

Minutoloら[[18](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]は、2009年から2015年にかけてS&P500に含まれる467社を対象に企業パフォーマンスを調査し、ESGがすべてのモデルにおいてトービンのqと総資産利益率（ROA）にプラスの影響を与えることを明らかにしたが、その効果は企業規模によって異なる

ギランら[19]は、コーポレート・ファイナンスに焦点を当て、ESGと企業の社会的責任（CSR）を検証した

この研究は、ESGとCSR活動が、企業の市場特性だけでなく、リスク、業績、価値とも密接に関連していることを強調している

Zhengら[20]は、ESGパフォーマンスが、特にメディアの注目度とアナリストのカバレッジを媒介として、上場企業の企業価値を有意に高めたと報告している

ESG要因は企業にとって極めて重要なリスク要因である

企業は、ESGと風評リスクを考慮し、社会的責任ある行動を取るよう努める

Stellnerら[21] は、優れたCSRパフォーマンスが信用リスクを低減するかどうかを調査し、その国のESGパフォーマンスが企業の社会的パフォーマンスと信用リスクの関係を緩和することを発見した

さらに、この包括的な検証は、企業の株価と全体的な企業価値を形成する上で、ESG評価が極めて重要な役割を果たすことを強調している

この認識により、企業はESG情報を統合することで社会的責任や環境への影響を強化する戦略を採用しようと努力しており、こうした努力はニュース記事を通じて世間に反映される。

さらに、この情報が一般に公開されれば、最終的に企業価値、ひいては株価に影響を与えることになる

### **Leveraging technical indicators in asset price prediction**

研究者たちは、資産パフォーマンスを予測する試みにおいて、さまざまなテクニカル指標を考案し、検討してきた

XuとKeselj[[22](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]は、11業種の株式データと金融関連のツイートを収集した

株価データを効果的に予測するため、著者らはAD、ADX、EMA、KAMA、MA、MACD、RSI、PSAR、SMAなどのテクニカル指標を算出した（Table 1）

---

Table 1 Descriptions of technical indicators employed in previous research.

| Indicator | Description |
| --- | --- |
| Simple Moving Average (SMA)
単純移動平均 | Provides a smoothing effect on price data over a designated time frame
指定した時間枠の価格データにスムージング効果を与える |
| Exponential Moving Average (EMA)
指数移動平均 | Provides a smoother perspective of price trends, emphasizing recent data
最近のデータに重点を置き、価格動向をよりスムーズに見通すことができる |
| Chaikin Accumulation/Distribution Line (AD)
チャイキン蓄積 / 分配ライン | Measures cumulative buying and selling pressure for predicting price trends
価格動向を予測するための累積的な買い圧力と売り圧力の測定 |
| Average Directional Movement Index (ADX)
平均方向性指数 | Mean directional movement indicator
平均方向指示器 |
| Kaufman Adaptive Moving Average (KAMA)
カウフマン適応移動平均 | Adapts to changing market conditions, aiding in identifying optimal entry and exit points
変化する市場環境に適応し、最適なエントリーポイントとエグジットポイントの特定をサポート |
| Moving Average Convergence/Divergence (MACD)
移動平均収束/発散 | Convergence and divergence of moving averages
移動平均の収束と乖離 |
| Relative Strength Index (RSI)
相対力指数 | Evaluates asset’s overbought or oversold conditions, guiding potential reversals
資産の買われすぎ、売られすぎの状態を評価し、反転の可能性を導く |
| Parabolic Stop and Reverse (PSAR)
パラボリック・ストップ・アンド・リバース | Offers dynamic stop-loss levels, crucial for risk management
リスク管理に不可欠なダイナミックなストップロス・レベルを提供 |
| Momentum (MOM)
モメンタム | Measure the rate of change
変化率を測定する |
| Rate of Change (ROC)
変化率 | Measure the percentage change in price from a previous period to the current period
前期から当期への価格変動率を測定する |
| Signal
シグナル | Provide partial visual smoothing of technical indicators and detect trend reversals and crossovers
テクニカル指標を部分的に視覚的に平滑化し、トレンドの反転やクロスオーバーを検出します |
| Stochastic RSI
ストキャスティクスRSI | Combination of the RSI and Stochastic indicator
RSIとストキャスティクス指標の組み合わせ |
| Stochastic Oscillator
ストキャスティクスオシレーター | Relative position of prices over a given period
一定期間における価格の相対的位置 |

---

HoseinzadeとHaratizadeh[[23](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]は、特徴抽出を用いて市場の先物予測性能を向上させた

具体的には、MOM、ROC、EMAなどのテクニカル指標を採用したアーキテクチャを設計した

さらに、著者らはヒストリカル・データを組み入れ、その結果、F値のパフォーマンスが9%向上した

Assisら[[24](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]は、テクニカル分析ライブラリ（TA-Lib）を利用してテクニカル指標を計算し、潜在的特徴を捕捉するために制限付きボルツマンマシンを採用し、サポートベクターマシンによって金融時系列データを分析した

その結果、テクニカル指標を使用しない場合と比較して、実験結果はより高い精度を示した

Jung ら[[25](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]は、RSI、SMA、EMA、MACD、シグナル、ストキャスティッ ク RSI、ストキャスティック・オシレーターの各指標を用い、テクニカル指標と センチメント指標を組み合わせてビットコイン価格の動向を予測した

その結果、11のテクニカル指標を考慮することが有効であることがわかり、GBoostは90.57%の予測性能を示した

まとめると、株価予測は様々な領域にまたがっており、研究者は正確な予測のために様々な変数を探求する必要がある

株式データからテクニカル指標を計算し、センチメント指標を利用するアプローチは、予測精度を大幅に向上させ、包括的な金融知識を得て情報に基づいた意思決定を行うための強固な基盤を提供している

## **Method**

---

このセクションでは、実験の流れを説明する

まず、実験のためのデータを収集した

その後、無関係なテキストデータを除去するための前処理が行われた

第三に、テクニカル指標はS&P500のデータセットから、センチメント指標はESG関連のニュースデータから作成した

処理されたデータを組み合わせた後、スケーリングされたデータは、将来の価格を予測するためのディープラーニングモデルの入力データとして調整された

さらに、各入力機能の有効性を評価するため、アブレーションテストを実施した

実験手順をFig. 1に示す

![Fig. 1. Flowchart for predicting S&P 500 index.](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41598-024-61106-2/MediaObjects/41598_2024_61106_Fig1_HTML.png?as=webp)

Fig. 1. Flowchart for predicting S&P 500 index.

### Data collection

S&P500指数は、株式市場全体の動向を把握・監視するために使用され、米国の金融市場の健全性を表す指標のひとつとされている[[26](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

S&P500は米国の主要企業500社を指数化したもので、個別企業の株価ではなく市場全体の動きを反映している

加えて、S&P500には様々な産業やセクターの企業が含まれている

したがって、様々な業種のデータを含めて株価予測モデルを構築することは、汎用性のある一般化モデルを設計することに等しい

さらに、個別企業の株式は内部要因の影響も考慮しなければならないが、S&P500は市場全体の認識の影響を受ける[27]

その結果、ESG情報とS&P500種株価指数を統合した株価予測モデルを構築することで、投資家や関連研究者に対し、市場全体のサステナビリティ情報の重要性と影響力を強調することができる

実験は2016年1月1日から2023年7月31日までの２つのデータセットを集めて行われた

1. LexisNexisを通じて、"ESG "という検索語を使った14,049のニュース記事を収集した．LexisNexisデータベースへのアクセスには、機関アクセスなどの有料購読が必要な場合があります
2. S&P500指数のヒストリカル・データ（日付、終値、始値、高値、安値、取引量、ボラティリティなどの情報を含む）をinvesting.comから入手した

### **Feature engineering**

先行研究に基づき、著者らはTA-libモジュールを用いて株価に影響を与えることが示されている様々なテクニカル指標を入手した[[28](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21),[29](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

選ばれた特徴は以下の通りである

---

opening price

Low price

SMA_5

MACD

Stochastic RSI_fastd

WilliamR

closing price

trading volume

SMA_20

signal

Stochastic Oscillator Index_slowk

ROC

high price

RSI

EMA

Stocjastic RSI_fastk

Stochastic Oscillator Index_slowd

Momentum

始値、終値、高値、安値、出来高、RSI、SMA_5、SMA_20、EMA、MACD、シグナル、ストキャスティクスRSI_fastk、ストキャスティクスRSI_fastd、ストキャスティクス・オシレーター指数_slowk、ストキャスティクス・オシレーター指数_slowd、ストキャスティクス・オシレーター指数_slowd、WilliamR、モメンタム、ROC

---

これらのテクニカル指標に関する詳細な説明は以下の通り

- **Opening Price**

始値は，取引セッションの開始時の株価であり、その日の最初の取引を示す
高値は特定の取引期間内の株式取引の最高値を表し、安値は最低値を意味する

- **Trading Volume**

市場の動きを反映する取引高は、特定の期間に取引された株式や契約の数である

- **RSI**

RSIはモメンタムオシレーターで、値動きの速さと変化を測定し、買われすぎや売られすぎの状態を識別するのに役立つ

- SMAs

SMAは、指定された期間の終値の平均です。例えば、SMA_5とSMA_20は、それぞれ5日と20日の移動平均を表します

- **EMA**

 EMAは直近の価格変動により多くのウェイトを置き、より適切に反応する[30]

- **MACD**

MACDはモメンタム指標で、証券価格の2本の移動平均の相互作用を示すことで、トレンドに追随します

- **Signal**

シグナルライン、すなわちMACDラインから派生した移動平均線は、トレーダーや投資家にとって価値ある売買シグナルを生成する上で重要な役割を果たす[[31](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

- **Stochastic RSI_fastk and Stochastic RSI_fastd**

RSIとストキャスティクス・オシレーターの両方に基づいて計算されたストキャスティクスRSI_fastkとストキャスティクスRSI_fastdは、価格反転の可能性のあるポイントを効果的に把握し、予測の精度を高めます[[32](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

- **stochastic oscillator indices_slowk and stochastic oscillator indices_slowd**

滑らかさを確保するため、確率発振器の指標_slowkと確率発振器の指標_slowdは確率発振器の補助的な構成要素とみなされた

- **William’s %R, commonly referred to as Williams R**

分析のもう一つの重要な側面は、William’s %R（一般にWilliams R）である
このモメンタム指標は、市場の状況が買われ過ぎか売られ過ぎかを評価し、市場センチメントの包括的な理解に貢献する[[33](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

- **Momentum**

モメンタムの概念は、価格の変化率を測定するために使用することができる

モメンタムは、株価の変化率を数値化することで、価格の変化率に関する洞察を提供する

- **ROC**

ROCはモメンタムに似た指標で、特定期間の価格変動を計算し、価格変動の程度を洞察するものである[[34](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

### **Sentiment index calculation using financial bidirectional encoder representations from transformers (FinBERT)**

ニュースデータに対して、ストップワード除去（stopwords removal）やレマタイゼーション（lemmatization）を含む前処理を行った後、FinBERTを使用してセンチメント分析を行った

FinBERT は、文脈を双方向に考慮してテキストを符号化することで、自然言語処理と理解のための効果的な言語モデルである BERT アーキテクチャに基づいて構築されている[[35](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

FinBERTは、BERTの事前学習済みモデルを金融データで再学習することで、ドメイン知識に特化している

FinBERTは、金融ニュース、レポート、ウェブ投稿などの金融関連のテキストを入力として受け取り、テキストのセンチメントを分析・予測し、ポジティブ、ネガティブ、ニュートラルのいずれかに分類する

データのスコアは、否定的な感情を0、肯定的な感情を1とした（式 (1) ）

$$
Sentiment\ Score=\frac{M_{tpos}-M_{tneg}}{M_{tpos}+M_{tneg}}
$$

(1)

Wuらの研究[[36](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]を参照すると、センチメントの測定は、特定のデータセットにおける否定的な投稿と肯定的な投稿の数の差として計算された

ここで、 $M_{tops}$は「$t$日目のポジティブなニュース記事の数」を表し、 $M_{tneg}$は「$t$日目のネガティブな記事の数」を表す

センチメント・インデックスの値の範囲は $-1$ から $1$ の間であった[[25](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

センチメント・インデックスの値が $-1$ に近づけば、その日のニュースがネガティブなトーンであることを示唆する

逆に $1$ に近づけば、ニュース全体がポジティブなトーンであることを示す

フレームワークへの入力として選択された特徴を採用する前に、これらの値の範囲を0から1の間で標準化するために min–max scaler が適用された

### Window size

その後、複数のデータセットが生成され、それぞれが異なるハイパーパラメータ・ウィンドウに対応する

ウィンドウ・サイズは、時系列データを処理し予測するための株価予測における基本的な概念である[[37](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21),[38](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

ウィンドウ・サイズは一定の単位期間を定義し、このウィンドウ内のデータを将来の株価予測に使用する

したがって、株価予測モデルのパフォーマンスを向上させるためには、適切なウィンドウ・サイズを選択することが極めて重要である。本研究では、3つのウィンドウサイズを用いて実験を行った： 3、4、5である（Fig. 2）

![Fig. 2. Window size illustration.](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41598-024-61106-2/MediaObjects/41598_2024_61106_Fig2_HTML.png?as=webp)

Fig. 2. Window size illustration.

最後に、訓練データセットとテストデータセットを8：2の比率で分割した。検証データセットはトレーニングデータセットの20%で構成される

### **Deep learning models**

双方向リカレントニューラルネットワーク（Bi-RNN）は、シーケンスの先行コンテキストと後続コンテキストの両方を考慮できるリカレントニューラルネットワークの一種である

この双方向性により、異なる時間方向のパターンを捉えることができる[[39](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

さらに、株価の変動には短期的な要因も影響するため、リカレント層を持つRNN構造は、こうした変化を捉えることに長けており、時系列モデルとしての応用に適している

さらに、Bi-RNNは様々なタイプの時系列データに適用できる柔軟な構造を持っており、パターン処理に有用である

これとは対照的に、双方向長期短期記憶ネットワーク（Bi-LSTM）は、LSTMセルを組み込んだRNNをさらに強化したものである[[40](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

長期的な依存関係を学習するのが得意で、時系列予測のような逐次的なデータを含むタスクに特に効果的である[[41](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

## Results

---

本研究の結果は、ウィンドウサイズ（3、4、5）とパラメーターの様々な組み合わせを用いた実験によって得られた。バッチサイズは2、4、6、8の組み合わせとされ、隠れサイズは32と64、レイヤー数は4、6、8、エポック数は10に固定され、すべての可能なシナリオを探索した

使用したモデルはBi-RNNとBi-LSTMである

性能は、式(2)を用いて計算されるMAPEを用いて評価された（Eq. (2) ）

$$
MAPE=\frac{1}{n}\sum^{n}_{t=1}|\frac{A_t-F_t}{A_T}|\times100
$$

ここで， $A_t$ は実際の値、 $F_t$ は時刻 $t$ での予測値、$n$ はオブザベーションの総数

MAPE値の範囲は0～100%で、0%に近いほどモデルの予測精度が高いことを示す[[42](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

その結果、ウィンドウサイズ3、バッチサイズ64、隠れサイズ64と32、レイヤー数2のBi-LSTMモデルが、テストデータにおいてMAPE値3.05%と最高の性能を示した（Table 2）

---

Table 2. **Results of each regressor (MAPE, %).**

Window size

3

4

5

Model

Bi-RNN

4.65

6.85

5.07

Bi-LSTM

3.05

3.2

3.55

---

さらに、S&P500の実際の値の範囲を変換して可視化するために、Bi-LSTMモデルの各ウィンドウサイズに対して逆変換を行い、その結果を比較した（Fig. 3）

![Fig. 2. Comparison of Bi-LSTM results based on window size with the actual S&P 500 closing value.](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41598-024-61106-2/MediaObjects/41598_2024_61106_Fig3_HTML.png?as=webp)

Fig. 2. Comparison of Bi-LSTM results based on window size with the actual S&P 500 closing value.

その後、入力された特徴の有効性を検証するためにアブレーションテスト（ablation test）が行われた

アブレーションテストは、因果関係を調べるために用いられる方法である

この方法は、特定の要素や変数を取り除いてテストし、それがシステムにどのような影響を与えるかを確認するものである[[43](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

著者らは窓の大きさを3、4、5に固定し、テストを3つのケース（すなわち、「価格のみ」、「価格とテクニカル指標」、「価格、テクニカル指標、ESGセンチメント指数」）に分けた

その結果、ESGセンチメントとテクニカル・データおよび価格データを組み合わせることで、価格データのみに頼るよりも優れたパフォーマンスが得られることが明らかになった

結論として、Bi-LSTMモデルの最適な性能は、3つの入力をすべて統合したときに達成された

これらの結果は、S&P500指数の予測モデルのパフォーマンスとESG情報の間に因果関係があることをアブレーション・テストによって検証したものである

MAPE値の具体的な結果はTable 3に示す

---

**Table 3 Ablation test results based on different input features (MAPE, %).**

| Input features | Bi-LSTM |
| --- | --- |
| Only Price (window size = 3) | 3.81 |
| Only Price (window size = 4) | 4.24 |
| Only Price (window size = 5) | 4.87 |
| Price and technical indicators (window size = 3) | 3.75 |
| Price and technical indicators (window size = 4) | 3.51 |
| Price and technical indicators (window size = 5) | 3.48 |
| Price, technical indicators, and ESG sentiment index (window size = 3) | 3.05 |
| Price, technical indicators, and ESG sentiment index (window size = 4) | 3.2 |
| Price, technical indicators, and ESG sentiment index (window size = 5) | 3.55 |

---

これらの結果を視覚的に表したものをFig. 4に示す

---

![](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41598-024-61106-2/MediaObjects/41598_2024_61106_Fig4_HTML.png?as=webp)

Fig. 4.Visualization of the ablation test results.

---

## Discussion

---

サステナビリティは、現代ビジネスを形作る重要なグローバルトレンドとして台頭しており、企業業績を評価するためにESG指標を統合する必要がある

ESG指標は、業務慣行に関する貴重な洞察を提供し、企業が持続可能な慣行と効果的なガバナンスを採用する場合、投資家の信頼と意思決定に大きく影響する

持続可能性、ESG指標と投資家の選択との結びつきが強まっていることから、ESG基準を財務評価に組み込むことの重要性が強調され、それによって企業の責任と投資戦略が融合することになる[[1](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21),[2](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

こうした理解のもと、企業はESG情報を統合することで社会的責任や環境への影響を高める戦略を採用しようと努力しており、こうした努力はニュース記事を通じて世間に反映される

こうしたメディアを通じた露出は、最終的に企業価値、ひいては株価に影響を与える可能性がある

金融市場の進化がこのような変化に適応している中、S&P500指数の予測にESG指標を統合することは、このような進化するトレンドに沿った先進的な戦略である[[6](https://www.notion.so/Reading-Research-Article-About-Financial-Trading-No-3-EN-20c42b38f4bb818cb905fc3fbe3e81a6?pvs=21)]

さらに、価格動向分析のためのファンダメンタル・テクニカル指標とESG指標を統合することは、長期的な価格変動と短期的な価格動向の両方を大きく考慮する包括的なアプローチを構成する

加えて、先行研究における機械学習の応用は、S&P500の予測におけるESG指標とテクニカル指標の相互作用を包括的に分析するための高度なアルゴリズムの活用の可能性を十分に活用しておらず、先行研究は機械学習が提供する可能性を十分に追求していない可能性があることを示している

これらの制約を克服するために、著者らはLexisNexisのニュースデータにFinBERTを適用して得られたセンチメント・スコアと、S&P500指数のヒストリカル・データから取得した18のテクニカル指標にディープラーニング・モデルを適用した

その後、フレームワークの性能評価指標としてMAPEが用いられた

様々なパラメータでクロスバリデーションを行った結果、Bi-LSTMモデルは、ウィンドウサイズ3、バッチサイズ64、隠れサイズ32と64、レイヤー数2を採用した場合、テストデータセットで3.05という優れたMAPEを示した

さらに、本研究で実施されたアブレーション・テストにより、S&P500指数予測に対する選択された入力特徴の強さが実証された

具体的には、テクニカル指標や価格情報とともにESG情報を組み込んだセンチメント・インデックスを考慮することで、最高のパフォーマンスが得られた

したがって、S&P500指数を予測するためにESG指標とテクニカル指標を統合することは、実用上重要な意味を持つ

ESG基準が株価予測に有利な要因として台頭するにつれ、企業は業務慣行や持続可能性への取り組みを評価するようになる

さらに、ESG指標の影響力を認識する投資家は、持続可能性と効果的なガバナンスを優先する企業を信頼することで、情報に基づいた意思決定を行うことができる

持続可能性への配慮、ESG指標、投資家の選択の間のこのような相互作用は、ESG要素を財務評価に統合し、企業責任を投資戦略と整合させる必要性を浮き彫りにしている

さらに、この研究は金融市場のトレンドと一致しており、株式市場の行動を予測するためにESGとテクニカル指標を組み合わせる可能性を示している

ディープラーニング・モデルは、ESGとテクニカル指標間の複雑なつながりを総合的に検証する革新的な機会を提供し、S&P500の正確な予測につながります

## **Limitations of the study**

この研究にはいくつかの限界がある

第一に、この調査結果は、S&P 500のデータセットに依存しているため、金融市場全体の複雑なダイナミクスを包括的に表していない可能性がある

今後の研究では、より広範な金融市場のデータを取り入れることで、これらの結果を検証し、拡張する必要がある。

第二に、この分析で使用したセンチメント・インデックスはニュース・データのみから導き出されたものであり、これが潜在的な限界である

したがって、ESGに関連する多様なテキストデータの統合を模索することで、より包括的でロバストな分析を行うことができるだろう

第三に、ESGに注目する価値は業種によって異なる。したがって、今後の研究では、株式市場全体ではなく、業界グループ別に銘柄を予測する試みが考えられる

## References

1. Egorova, A. A., Grishunin, S. V. & Karminsky, A. M. [The impact of ESG factors on the performance of information technology companies](https://www.sciencedirect.com/science/article/pii/S1877050922000412). *Procedia Comput. Sci.* **199**, 339–345 (2022).
2. Lee, H., Lee, S. H., Lee, K. R. & Kim, J. H. [ESG discourse analysis through BERTopic: Comparing news articles and academic papers](https://www.researchgate.net/profile/Haein-Lee-17/publication/370402973_ESG_Discourse_Analysis_Through_BERTopic_Comparing_News_Articles_and_Academic_Papers/links/644e035e97449a0e1a699d29/ESG-Discourse-Analysis-Through-BERTopic-Comparing-News-Articles-and-Academic-Papers.pdf?origin=journalDetail&_tp=eyJwYWdlIjoiam91cm5hbERldGFpbCJ9). *Comput., Mater. Continua* **75**(3), 6023–6037 (2023).
3. Lee, H., Lee, S. H., Park, H., Kim, J. H. & Jung, H. S. [ESG2PreEM: Automated ESG grade assessment framework using pre-trained ensemble models.](https://www.cell.com/heliyon/fulltext/S2405-8440(24)02435-6) *Heliyon* **10**(4), e26404 (2024).
4. Aybars, A., Ataünal, L., & Gürbüz, A. O. ESG and financial performance: impact of environmental, social, and governance issues on corporate performance. In *Handbook of Research on anagerial Thinking in Global Business Economics,* 520–536 (IGI Global, 2019).
5. In, S. Y., Rook, D. & Monk, A. [Integrating alternative data (also known as ESG data) in investment decision making](https://www.tandfonline.com/doi/full/10.1080/1226508X.2019.1643059). *Glob. Econ. Rev.* **48**(3), 237–260 (2019).
6. Alareeni, B. A. & Hamdan, A. [ESG impact on performance of US S&P 500-listed firms.](https://www.emerald.com/insight/content/doi/10.1108/cg-06-2020-0258/full/html) *Corp. Gov.: Int. J. Bus. Soc.* **20**(7), 1409–1428 (2020).
7. Huang, R. D. & Kracaw, W. A. [Stock market returns and real activity: a note](https://www.jstor.org/stable/2327683?seq=1). *J. Financ.* **39**(1), 267–273 (1984).
8. Fama, E. F. [Stock returns, real activity, inflation, and money.](https://www.jstor.org/stable/1806180) *Am. Econ. Rev.* **71**(4), 545–565 (1981).
9. Scatigna, M., Xia, F. D., Zabai, A., & Zulaica, O. Achievements and challenges in ESG markets. *BIS Quarterly Review*, *December* (2021).
10. Kiesel, F. & Lücke, F. [ESG in credit ratings and the impact on financial markets.](https://onlinelibrary.wiley.com/doi/abs/10.1111/FMII.12114) *Financ. Mark. Inst. Instrum.* **28**(3), 263–290 (2019).
11. Peng, Y., Albuquerque, P. H. M., Kimura, H. & Saavedra, C. A. P. B. [Feature selection and deep neural networks for stock price direction forecasting using technical analysis indicators.](https://www.sciencedirect.com/science/article/pii/S266682702100030X) *Mach. Learn. Appl.* **5**, 100060 (2021).
12. Shynkevich, Y., McGinnity, T. M., Coleman, S. A., Belatreche, A. & Li, Y. [Forecasting price movements using technical indicators: Investigating the impact of varying input window length.](https://www.sciencedirect.com/science/article/abs/pii/S0925231217311074) *Neurocomputing* **264**, 71–88 (2017).
13. Zubair, S., & Cios, K. J. Extracting news sentiment and establishing its relationship with the s&p 500 index. In *2015 48th Hawaii International Conference on System Sciences,* 969–975 (IEEE, 2015).
14. Khedr, A. E. & Yaseen, N. [Predicting stock market behavior using data mining technique and news sentiment analysis](https://www.mecs-press.org/ijisa/ijisa-v9-n7/IJISA-V9-N7-3.pdf). *Int. J. Intell. Syst. Appl.* **9**(7), 22 (2017).
15. Li, Y., & Pan, Y. A novel ensemble deep learning model for stock prediction based on stock prices and news. *Int. J. Data Sci. Anal.*, 1–11 (2022).
16. Bauer, R., Guenster, N. & Otten, R. [Empirical evidence on corporate  governance in Europe: The effect on stock returns, firm value and 
performance.](https://link.springer.com/article/10.1057/palgrave.jam.2240131) *J. Asset Manag.* **5**, 91–104 (2004).
17. Chen, R. C., Hung, S. W. & Lee, C. H. [Does corporate value affect the relationship between corporate social responsibility and stock returns?](https://www.tandfonline.com/doi/abs/10.1080/20430795.2016.1272947). *J. Sustain. Finance Invest.* **7**(2), 188–196 (2017).
18. Minutolo, M. C., Kristjanpoller, W. D. & Stakeley, J. [Exploring environmental, 
social, and governance disclosure effects on the S&P 500 financial performance.](https://onlinelibrary.wiley.com/doi/abs/10.1002/bse.2303) *Bus. Strateg. Environ.* **28**(6), 1083–1095 (2019).
19. Gillan, S. L., Koch, A. & Starks, L. T. [Firms and social responsibility: A review of ESG and CSR research in corporate finance.](https://www.sciencedirect.com/science/article/abs/pii/S0929119921000092) *J. Corp. Finan.* **66**, 101889 (2021).
20. Zheng, Y., Wang, B., Sun, X. & Li, X. [ESG performance and corporate value: Analysis from the stakeholders’ perspective.](https://www.frontiersin.org/journals/environmental-science/articles/10.3389/fenvs.2022.1084632/full) *Front. Environ. Sci.* **10**, 1084632 (2022).
21. Stellner, C., Klein, C. & Zwergel, B. [Corporate social responsibility and Eurozone corporate bonds: The moderating role of country sustainability.](https://www.sciencedirect.com/science/article/abs/pii/S0378426615001788) *J. Bank. Finance* **59**, 538–549 (2015).
22. Xu, Y., & Keselj, V. Stock prediction using deep learning and sentiment analysis. In *2019 IEEE international conference on big data (big data)*, 5573–5580 (IEEE, 2019).
23. Hoseinzade, E. & Haratizadeh, S. CNNpred: [CNN-based stock market prediction using a diverse set of variables.](https://www.sciencedirect.com/science/article/abs/pii/S0957417419301915) *Expert Syst. Appl.* **129**, 273–285 (2019).
24. Assis, C. A., Pereira, A. C., Carrano, E. G., Ramos, R., & Dias, W. Restricted Boltzmann machines for the prediction of trends in financial time series. In *2018 International Joint Conference on Neural Networks (IJCNN)*, 1–8 (IEEE, 2018).
25. Jung, H. S., Lee, S. H., Lee, H. & Kim, J. H. [Predicting bitcoin trends through machine learning using sentiment analysis with technical indicators.](https://openurl.ebsco.com/EPDB%3Agcd%3A9%3A3406649/detailv2?sid=ebsco%3Aplink%3Ascholar&id=ebsco%3Agcd%3A162102178&crl=c&link_origin=scholar.google.com) *Comput. Syst. Sci. Eng.* **46**(2), 2231–2246 (2023).
26. Ademi, B. & Klungseth, N. J. [Does it pay to deliver superior ESG performance? Evidence from US S&P 500 companies.](https://www.emerald.com/insight/content/doi/10.1108/jgr-01-2022-0006/full/html) *J. Glob. Responsib.* **13**(4), 421–449 (2022).
27. Chu, Q. C., Hsieh, W. L. G. & Tse, Y. [Price discovery on the S&P
 500 index markets: An analysis of spot index, index futures, and SPDRs.](https://www.sciencedirect.com/science/article/abs/pii/S1057521999000034)
 *Int. Rev. Financ. Anal.* **8**(1), 21–34 (1999).
28. Pieterse, B. Comparing the returns of technical analysis strategies with market index returns (Master's thesis, University of Pretoria (South Africa)) (2021).
29. Hajimiri, H. [Use of genetic algorithm in algorithmic trading to optimize
 technical analysis in the international stock market (Forex).](https://www.ssoar.info/ssoar/handle/document/80955) *J. Cyberspace Stud.* **6**(1), 21–29 (2022).
30. Rosillo, R., De la Fuente, D. & Brugos, J. A. L. [Technical analysis and the Spanish stock exchange: testing the RSI, MACD, momentum and stochastic rules using Spanish market companies](https://www.tandfonline.com/doi/abs/10.1080/00036846.2011.631894). *Appl. Econ.* **45**(12), 1541–1550 (2013).
31. Yazdi, S. H. M. & Lashkari, Z. H. [Technical analysis of Forex by MACD Indicator.](https://c.mql5.com/forextsd/forum/219/Technical%20analysis%20of%20Forex%20by%20MACD%20Indicator.pdf) *Int. J. Human. Manag. Sci. (IJHMS)* **1**(2), 159–165 (2013).
32. Vaiz, J. S. & Ramaswami, M. [A study on technical indicators in stock price movement prediction using decision tree algorithms.](https://d1wqtxts1xzle7.cloudfront.net/51057076/Z05120207212-libre.pdf?1482736903=&response-content-disposition=inline%3B+filename%3DA_Study_on_Technical_Indicators_in_Stock.pdf&Expires=1747279704&Signature=Y2DUrINmGRdXfrVSkNs4nFiQyXCWLekGOTiKwj6R-p7Z8pmgTENm8RhoeRguok6rl~X73Sz1Rp0g4bLEpFzgwlo8sslgS4mkI~lRglwciaFqk9DEvOvyfZuU4UDLVBWUnU9QAA2MwndjN57-PEuUEB15bH9y7f8wKknDFoZlH1NRXjfthIwpjE8jjUY0Y9SDSFtk0ICbmOv9YZZuniaM44b5Y-NT-b3p71iORtlzT0iCGmAPjumXY9aRNwy4bhO1sVWe28QWNM6bEjaMcEBuTACC1WzJGO~uA1GZCMlUUwES-MpRUI5T0ZlzRzN84iQX3TcjTS23ehTP3sCfsJTlRw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA) *Am. J. Eng. Res. (AJER)* **5**(12), 207–212 (2016).
33. Zhai, Y., Hsu, A., & Halgamuge, S. K. Combining news and technical indicators in daily stock price trends prediction. In *Advances in Neural Networks–ISNN 2007: 4th International Symposium on Neural Networks*, 1087–1096 (Springer, 2007).
34. Huang, J. Z., Huang, W. & Ni, J. [Predicting bitcoin returns using high-dimensional technical indicators.](https://www.sciencedirect.com/science/article/pii/S2405918818300928) *J. Finance Data Sci.* **5**(3), 140–155 (2019).
35. Araci, D. Finbert: Financial sentiment analysis with pre-trained language models. Preprint at [https://doi.org/10.48550/arXiv.1908.10063](https://doi.org/10.48550/arXiv.1908.10063) (2019).
36. Wu, S., Liu, Y., Zou, Z. & Weng, T. H. S_I_LSTM: [stock price prediction based on multiple data sources and sentiment analysis.](https://www.tandfonline.com/doi/full/10.1080/09540091.2021.1940101) *Connect. Sci.* **34**(1), 44–62 (2022).
37. Rajabi, S., Roozkhosh, P. & Farimani, N. M. [MLP-based Learnable Window Size for Bitcoin price prediction](https://www.sciencedirect.com/science/article/abs/pii/S1568494622006366). *Appl. Soft Comput.* **129**, 109584 (2022).
38. Das, G., Lin, K. I., Mannila, H., Renganathan, G., & Smyth, P. Rule Discovery from time series. *In KDD*, 16–22 (1998).
39. Schuster, M. & Paliwal, K. K. [Bidirectional recurrent neural networks.](https://ieeexplore.ieee.org/abstract/document/650093) *IEEE Trans. Signal Process.* **45**(11), 2673–2681 (1997).
40. Lee, H., Jung, H. S., Lee, S. H. & Kim, J. H. [Robust sentiment classification of metaverse services using a pre-trained language model with soft voting.](https://koreascience.kr/article/JAKO202330043204946.page) *KSII Trans. Internet Inf. Syst.* **17**(9), 2334–2347 (2023).
41. Hochreiter, S. & Schmidhuber, J. [Long short-term memory.](https://ieeexplore.ieee.org/abstract/document/6795963) *Neural Comput.* **9**(8), 1735–1780 (1997).
42. De Myttenaere, A., Golden, B., Le Grand, B. & Rossi, F. [Mean absolute percentage error for regression models.](https://www.sciencedirect.com/science/article/abs/pii/S0925231216003325) *Neurocomputing* **192**, 38–48 (2016).
43. Huang, S., Wang, D., Wu, X., & Tang, A. Dsanet: Dual self-attention network for multivariate time series forecasting. In *Proceedings of the 28th ACM international conference on information and knowledge management*, 2129–2132 (ACM, 2019).