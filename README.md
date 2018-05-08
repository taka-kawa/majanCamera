# 牌の記述

m\*:マンズの*  
p\*:筒子の*  
s\*:ソウズの*  
(e,s,w,n):(東、南、西、北)  
haku:白  
hatsu:發  
chun:中  

---

*には1~9までの数字が入る



# API

## エンドポイント

### http://t_kawa:8080/api/v1/detection

- 牌を検出する
- 形式
  - HTTPメソッド:POST
  - request内容:image(ロンした形)

参考画像

![mahjongyaku6](https://user-images.githubusercontent.com/26706103/39664511-34a62df8-50bf-11e8-810d-15e9c8db15c4.jpg)



response内容例
~~~json
{"pis": [{"name": "hatsu", "xmin": 0.9443261623382568, "ymin": 0.885155200958252, "xmax": 1.0, "ymax": 0.9668492078781128, "conf": 0.9989991784095764}, {"name": "s1", "xmin": 0.5105834603309631, "ymin": 0.8831236362457275, "xmax": 0.5721703171730042, "ymax": 0.9696668386459351, "conf": 0.997262716293335}, {"name": "s4", "xmin": 0.3231615722179413, "ymin": 0.8854721784591675, "xmax": 0.38519981503486633, "ymax": 0.9683240652084351, "conf": 0.9962512850761414}, {"name": "p4", "xmin": 0.635847806930542, "ymin": 0.88599693775177, "xmax": 0.6967763900756836, "ymax": 0.9691020250320435, "conf": 0.9940372705459595}, {"name": "s6", "xmin": 0.576220691204071, "ymin": 0.8850948810577393, "xmax": 0.6364890933036804, "ymax": 0.9626741409301758, "conf": 0.9926861524581909}, {"name": "p6", "xmin": 0.7003210783004761, "ymin": 0.8853741884231567, "xmax": 0.762068510055542, "ymax": 0.9672133922576904, "conf": 0.9854868650436401}, {"name": "haku", "xmin": 0.1347847580909729, "ymin": 0.8846403956413269, "xmax": 0.19850048422813416, "ymax": 0.9663597941398621, "conf": 0.982799232006073}, {"name": "s2", "xmin": 0.19977118074893951, "ymin": 0.8849960565567017, "xmax": 0.25998181104660034, "ymax": 0.9642751216888428, "conf": 0.9816431403160095}, {"name": "p6", "xmin": 0.8863188624382019, "ymin": 0.8842339515686035, "xmax": 0.9464882016181946, "ymax": 0.9646909236907959, "conf": 0.9564278721809387}, {"name": "p8", "xmin": 0.7609726190567017, "ymin": 0.876449704170227, "xmax": 0.823549747467041, "ymax": 0.9607722759246826, "conf": 0.9172372817993164}, {"name": "p1", "xmin": 0.26350435614585876, "ymin": 0.8850215077400208, "xmax": 0.32111355662345886, "ymax": 0.9661094546318054, "conf": 0.6761854290962219}], "image_id": 1}
~~~

response構造

~~~json
{
  "pis":[
         {"name":"hatsu", "xmin":0.3, "ymin":0.2, "xmax":0.1, "ymax":0.1, "conf":0.5},
         {"name":"hatsu", "xmin":0.3, "ymin":0.2, "xmax":0.1, "ymax":0.1, "conf":0.5},
         {"name":"hatsu", "xmin":0.3, "ymin":0.2, "xmax":0.1, "ymax":0.1, "conf":0.5},
         {"name":"hatsu", "xmin":0.3, "ymin":0.2, "xmax":0.1, "ymax":0.1, "conf":0.5},
         {"name":"hatsu", "xmin":0.3, "ymin":0.2, "xmax":0.1, "ymax":0.1, "conf":0.5},
         {"name":"hatsu", "xmin":0.3, "ymin":0.2, "xmax":0.1, "ymax":0.1, "conf":0.5},
         {"name":"hatsu", "xmin":0.3, "ymin":0.2, "xmax":0.1, "ymax":0.1, "conf":0.5},
         {"name":"hatsu", "xmin":0.3, "ymin":0.2, "xmax":0.1, "ymax":0.1, "conf":0.5},
         {"name":"hatsu", "xmin":0.3, "ymin":0.2, "xmax":0.1, "ymax":0.1, "conf":0.5},
         {"name":"hatsu", "xmin":0.3, "ymin":0.2, "xmax":0.1, "ymax":0.1, "conf":0.5},
        ]
 "image_id":画像のid番号(修正が必要な場合にこのidを使ってどの画像が間違えていたか修正)
}
~~~



# 現状の課題

1. 牌の認識精度
   - 訓練画像のバリエーションを増やす
     - ノイズを加える
     - 3Dモデル
   - 横向きの認識
2. ポン・チー・カンをどうするか
3. 点計算
4. ミスを修正して学習