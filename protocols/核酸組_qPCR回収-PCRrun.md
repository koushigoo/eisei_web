# qPCR回収-PCRまで

## ワークフロー

```mermaid
graph LR
    回収-->PCR-->解析
```

## Materials & Recipes

| Material            | Cat. No. | Misc. |
| ------------------- | -------- | ----- |
| CellAmp Direct      | TaKaRa#  |       |
| One-step RT-PCR Kit | TaKaRa#  |       |

## Protocol

### 回収

- [ ] Processing Bufferを常温で融解する
- [ ] DNase Iを添加する

| Reagent           | Volume( 1 well) | Volume ( 18+2  well) |
| ----------------- | --------------- | -------------------- |
| Processing Buffer | 10 μL           | 200 μL               |
| MilliQ water      | 10 μL           | 200 μL               |
| Dnase I           | 0.2 μL          | 4 μL                 |

- [ ] 96wellプレートを遠心分離する
- [ ] 上清を吸引する。wellを1周するように、きちんと吸い切る。
- [ ] DNaseを添加したProcessing Bufferを20 μLずつ添加する
- [ ] 5 min静置する
- [ ] 全量を新しいチューブ or プレートに移す
- [ ] 75℃, 5 minインキュベートする
- [ ] -80℃で保存する（~1w程度保管可能)

### RT-qPCR

#### master mix調製

| Reagent          | μL/1 well | μL/(36+4) well |
| ---------------- | --------- | -------------- |
| 1液(2x Buffer)   | 5         | 200            |
| 2液(Ex Taq)      | 0.16      | 6.4            |
| 3液(PrimeScript) | 0.16      | 6.4            |
| Primer(5 μM F+R) | 0.4       | 16             |
| Total            | 5.72      | 228.8          |
| (サンプル)       | 4.28      |                |

- [ ] GR (14Bの場合）、GAPDHそれぞれに対して上のようにMaster Mixを調製する
備考：余ったら次回に使い回せるので、-20℃保存を推奨

#### PCR

- [ ] 回収したRNAを室温(or 氷上)で融解する
- [ ] 上で調製したMaster Mix 5.72 μLを0.1 mL PCRプレートに添加する
- [ ] RNAサンプルにMilliQ water 80 μLずつ添加し、ピペッティングにて混和する
- [ ] RNAサンプル 4.28 μLをPCRプレートの壁面に付けていく
- [ ] フィルムを貼付する
- [ ] プレート遠心機にて壁面の液を落とす
- [ ] PCRの機械にセットする
- [ ] PCRを行う

#### 解析

- [ ] [qPCR解析](link)を参照し、解析を行う
- [ ] 慣れてきたら（ルーチンワークであれば）　～～～～なんか書く
