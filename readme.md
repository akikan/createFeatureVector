# はじめに
データサイエンティストのために

特徴量の選択は実に重要な要素である。<br>
しかし、特徴量一つごとに特徴量化するプログラムを書くのは大変手間であるし、そんなところに時間を使うのは勿体ない。<br>
<br>
そんな時間を減らすためにプログラムを作成した。<br>
<br>

特徴量にしなくてはいけないものにはいくつか種類があると思う。（他にあったら順次追加していく）<br>
・ 連続値<br>
・ 複数選択肢がある中で一つだけを選ぶもの<br>
・ 複数選択肢がある中で複数を選ぶもの<br>
・ 文章などのテキストデータ<br>
<br>
本プログラムではテキストデータ以外の3つを簡略化する。<br>
以下に使用例を記述する。<br>

## 前提（読み込み）
本プログラムを使用するためにいくつかやっておいてほしいことがあるので先に記述しておく。<br>
以下のようなsample.csvがある前提で話す。<br>
``` sample.csv
値段,形状,色,味
100,丸い,赤い,甘い；酸っぱい
200,楕円,黄色い,酸っぱい
300,丸い,黒い,甘い

```

``` usage.py
import csv
import column2feature as C2F

csvfile = "sample.csv"
f = open(csvfile,"r", encoding="utf-8")
reader = csv.reader(f)
next(reader)
data=[]
for row in reader:
	temp = []
	for cell in row:
		temp.append(cell)			
	data.append(temp)
f.close()

#data[1][3]が2列4行目を表すような配列に変換する
data = C2F.row2column(data)
```
csvの列単位で操作するために転置行列を作成する<br>
上記のusage.pyで行っている操作を例に示すと以下のようになる。<br>
data=[[1,2,3],<br>
	  [4,5,6],<br>
	  [7,8,9]]<br>

        ↓
	C2F.row2column
        ↓  

data=[[1,4,7],<br>
	  [2,5,8],<br>
	  [3,6,9]]<br>
<br>

## 連続値の場合
Column2Stdardizationという関数を用意した。<br>
連続値の列を引数として与えると標準化が施された列、標準化を行う際に使用した平均と標準偏差、そしてが返ってくる<br>
（※標準化とは平均が0、分散が1にする操作のこと）<br>
これを前提の項で用意したような配列にappendすることで特量化が完了する。<br>
いかに使用例を示す。<br>
```
featureVectors=[]
temp, _, _ = C2F.Column2Stdardization(data[0])
featureVectors.append(temp)
```

## 複数の選択肢から一つを選択する場合
Choice2Feature関数に該当する値を持つ列を引数として与える。<br>
例として以下のような列を用意する<br>
['丸い','楕円','丸い']<br>
この列を与えると<br>
[[1,0,1],<br>
 [0,1,0]]<br>
のようなリストが返ってくる<br>
1つ目の行が'丸い'が選択肢を示していて<br>
2つ目の行が'楕円'が選択肢を示している<br>
見方としては列単位でみる。<br>
1列目は丸いが選ばれていることを示し、楕円が選ばれていないことを示している。<br>
2列目は丸いが選ばれていないことを示し、楕円が選ばれていることを示している。<br>
前提の項で用意したような配列にextendすることで特徴量化が完了する。<br>

```
featureVectors.extend(C2F.Choice2Feature(data[1]))
```


## 複数の選択肢から複数選択する場合
Flag2Feature関数に該当する列と選択肢のリストを用意する。<br>
例として以下のような列を用意する(別にセミコロン区切りになっていなくても単語同士が何かで区切られていればいい)<br>
['甘い；酸っぱい','酸っぱい','甘い']と<br>
['甘い','酸っぱい']#選択肢の列<br>
この列を与えると<br>
[[1,0,1],<br>
 [1,1,0]]<br>
のようなリストが返ってくる<br>
1つ目の行が'甘い'が選択肢を示していて<br>
2つ目の行が'酸っぱい'が選択肢を示している<br>
見方としては列単位でみる。<br>
1列目は甘いが選ばれていることを示し、酸っぱいが選ばれていないことを示している。<br>
2列目は甘いが選ばれていないことを示し、酸っぱいが選ばれていることを示している。<br>
前提の項で用意したような配列にextendすることで特徴量化が完了する。<br>


## usage
```
import csv
import column2feature as C2F

csvfile = "sample.csv"
f = open(csvfile,"r", encoding="utf-8")
reader = csv.reader(f)
next(reader)
data=[]
for row in reader:
	temp = []
	for cell in row:
		temp.append(cell)		
	data.append(temp)
f.close()

data = C2F.row2column(data)

featureVectors=[]
temp, _, _ = C2F.Column2Stdardization(data[0])
featureVectors.append(temp)
featureVectors.extend(C2F.Choice2Feature(data[1]))
featureVectors.extend(C2F.Choice2Feature(data[2]))
featureVectors.extend(C2F.Flag2Feature(data[3],['甘い','酸っぱい']))

featureVectors = C2F.column2row(featureVectors)
print(featureVectors)


```
