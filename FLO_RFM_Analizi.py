############################ İŞ PROBLEMİ ###############################

# Online ayakkabı mağazası olan FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama
# stratejileri belirlemek istiyor. Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu
# davranışlardaki öbeklenmelere göre gruplar oluşturulacak.

######################## Veri Seti Hikayesi ############################

# Veri seti Flo’dan son alışverişlerini 2020 - 2021 yıllarında OmniChannel (hem online hem offline alışveriş yapan)
# olarak yapan müşterilerin geçmiş alışveriş davranışlarından elde edilen bilgilerden oluşmaktadır.

# 12 Değişken - 19.945 Gözlem - 2.7MB

# DEĞİŞKENLER

# master_id Eşsiz                   = Müşteri Numarası
# order_channel                     = Alışveriş yapılan platforma ait hangi kanalın kullanıldığı
                                      # (Android, ios, Desktop, Mobile)
# last_order_channel                = En son alışverişin yapıldığı kanal
# first_order_date                  = Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date                   = Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online            = Müşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline           = Müşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online       = Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline      = Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline = Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online  = Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12       = Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi


import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 400)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

df1 = pd.read_csv("DATASETS/flo_data_20k.csv")
df = df1.copy()

# İlk 10 Gözlem
df.head(10)

#                              master_id order_channel last_order_channel first_order_date last_order_date last_order_date_online last_order_date_offline  order_num_total_ever_online  order_num_total_ever_offline  customer_value_total_ever_offline  customer_value_total_ever_online       interested_in_categories_12
# 0  cc294636-19f0-11eb-8d74-000d3a38a36f   Android App            Offline       2020-10-30      2021-02-26             2021-02-21              2021-02-26                         4.00                          1.00                             139.99                            799.38                           [KADIN]
# 1  f431bd5a-ab7b-11e9-a2fc-000d3a38a36f   Android App             Mobile       2017-02-08      2021-02-16             2021-02-16              2020-01-10                        19.00                          2.00                             159.97                           1853.58  [ERKEK, COCUK, KADIN, AKTIFSPOR]
# 2  69b69676-1a40-11ea-941b-000d3a38a36f   Android App        Android App       2019-11-27      2020-11-27             2020-11-27              2019-12-01                         3.00                          2.00                             189.97                            395.35                    [ERKEK, KADIN]
# 3  1854e56c-491f-11eb-806e-000d3a38a36f   Android App        Android App       2021-01-06      2021-01-17             2021-01-17              2021-01-06                         1.00                          1.00                              39.99                             81.98               [AKTIFCOCUK, COCUK]
# 4  d6ea1074-f1f5-11e9-9346-000d3a38a36f       Desktop            Desktop       2019-08-03      2021-03-07             2021-03-07              2019-08-03                         1.00                          1.00                              49.99                            159.99                       [AKTIFSPOR]
# 5  e585280e-aae1-11e9-a2fc-000d3a38a36f       Desktop            Offline       2018-11-18      2021-03-13             2018-11-18              2021-03-13                         1.00                          2.00                             150.87                             49.99                           [KADIN]
# 6  c445e4ee-6242-11ea-9d1a-000d3a38a36f   Android App        Android App       2020-03-04      2020-10-18             2020-10-18              2020-03-04                         3.00                          1.00                              59.99                            315.94                       [AKTIFSPOR]
# 7  3f1b4dc8-8a7d-11ea-8ec0-000d3a38a36f        Mobile            Offline       2020-05-15      2020-08-12             2020-05-15              2020-08-12                         1.00                          1.00                              49.99                            113.64                           [COCUK]
# 8  cfbda69e-5b4f-11ea-aca7-000d3a38a36f   Android App        Android App       2020-01-23      2021-03-07             2021-03-07              2020-01-25                         3.00                          2.00                             120.48                            934.21             [ERKEK, COCUK, KADIN]
# 9  1143f032-440d-11ea-8b43-000d3a38a36f        Mobile             Mobile       2019-07-30      2020-10-04             2020-10-04              2019-07-30                         1.00                          1.00                              69.98                             95.98                [KADIN, AKTIFSPOR]

# Eksik Değerler
df.isnull().sum()

# master_id                            0
# order_channel                        0
# last_order_channel                   0
# first_order_date                     0
# last_order_date                      0
# last_order_date_online               0
# last_order_date_offline              0
# order_num_total_ever_online          0
# order_num_total_ever_offline         0
# customer_value_total_ever_offline    0
# customer_value_total_ever_online     0
# interested_in_categories_12          0
# dtype: int64

# Verinin Betimlenmesi
df.describe([0.01, 0.05, 0.1, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]).T
#                                    count   mean    std   min    1%    5%   10%    25%    50%    75%     90%     95%     99%      max
# order_num_total_ever_online       19945.00   3.11   4.23  1.00  1.00  1.00  1.00   1.00   2.00   4.00    7.00   10.00   20.00   200.00
# order_num_total_ever_offline      19945.00   1.91   2.06  1.00  1.00  1.00  1.00   1.00   1.00   2.00    4.00    4.00    7.00   109.00
# customer_value_total_ever_offline 19945.00 253.92 301.53 10.00 19.99 39.99 59.99  99.99 179.98 319.97  519.95  694.22 1219.95 18119.14
# customer_value_total_ever_online  19945.00 497.32 832.60 12.99 39.99 63.99 84.99 149.98 286.46 578.44 1082.04 1556.73 3143.81 45220.13

# Genel Bilgi
df.info()
# #   Column                             Non-Null Count  Dtype
# ---  ------                             --------------  -----
#  0   master_id                          19945 non-null  object
#  1   order_channel                      19945 non-null  object
#  2   last_order_channel                 19945 non-null  object
#  3   first_order_date                   19945 non-null  object
#  4   last_order_date                    19945 non-null  object
#  5   last_order_date_online             19945 non-null  object
#  6   last_order_date_offline            19945 non-null  object
#  7   order_num_total_ever_online        19945 non-null  float64
#  8   order_num_total_ever_offline       19945 non-null  float64
#  9   customer_value_total_ever_offline  19945 non-null  float64
#  10  customer_value_total_ever_online   19945 non-null  float64
#  11  interested_in_categories_12        19945 non-null  object
# dtypes: float64(4), object(8)


# Omnichannel, müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Her bir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.

# Toplam Alışveriş Sayısı (On + Off)

df["total_order_num"] = df["order_num_total_ever_offline"] + \
                        df["order_num_total_ever_online"]

# 0        5.00
# 1       21.00
# 2        5.00
# 3        2.00
# 4        2.00
#          ...
# 19940    3.00
# 19941    2.00
# 19942    3.00
# 19943    6.00
# 19944    2.00
# Name: total_order_num, Length: 19945, dtype: float64

# Toplam Ödenen Ücret (On + Off)

df["total_price"] = df["customer_value_total_ever_offline"] + \
                             df["customer_value_total_ever_online"]

# 0        939.37
# 1       2013.55
# 2        585.32
# 3        121.97
# 4        209.98
#           ...
# 19940    401.96
# 19941    390.47
# 19942    632.94
# 19943   1009.77
# 19944    261.97
# Name: total_price, Length: 19945, dtype: float64

# Tarih ifade edip object olan değişkenlerin tipini date'e çevirelim.

df.dtypes
# first_order_date              object
# last_order_date               object
# last_order_date_online        object
# last_order_date_offline       object

# Çözüm 1

for col in df.columns:
    if "date" in col:
        df[col] = df[col].apply(pd.to_datetime)

# Çözüm 2

contains_date =  df.columns[df.columns.str.contains("date")]
df[contains_date] = df[contains_date].apply(pd.to_datetime)

# first_order_date               datetime64[ns]
# last_order_date                datetime64[ns]
# last_order_date_online         datetime64[ns]
# last_order_date_offline        datetime64[ns]

# Alışveriş kanallarındaki müşteri sayısının,
# toplam alınan ürün sayısının ve toplam harcamaların dağılımına bakalım.

df.groupby("order_channel").agg({"master_id": ["count"],
                                 "total_order_num" : ["sum"],
                                  "total_price": ["sum"]}).head()

#              master_id total_order_num total_price
#                   count             sum         sum
# order_channel
# Android App        9495        52269.00  7819062.76
# Desktop            2735        10920.00  1610321.46
# Ios App            2833        15351.00  2525999.93
# Mobile             4882        21679.00  3028183.16


# En fazla kazancı getiren ilk 10 müşteri :
df.groupby("master_id").agg({"total_price": "sum"}).\
    sort_values("total_price", ascending=False).head(10)

#                                     total_price
# master_id
# 5d1c466a-9cfd-11e9-9897-000d3a38a36f     45905.10
# d5ef8058-a5c6-11e9-a2fc-000d3a38a36f     36818.29
# 73fd19aa-9e37-11e9-9897-000d3a38a36f     33918.10
# 7137a5c0-7aad-11ea-8f20-000d3a38a36f     31227.41
# 47a642fe-975b-11eb-8c2a-000d3a38a36f     20706.34
# a4d534a2-5b1b-11eb-8dbd-000d3a38a36f     18443.57
# d696c654-2633-11ea-8e1c-000d3a38a36f     16918.57
# fef57ffa-aae6-11e9-a2fc-000d3a38a36f     12726.10
# cba59206-9dd1-11e9-9897-000d3a38a36f     12282.24
# fc0ce7a4-9d87-11e9-9897-000d3a38a36f     12103.15

# En fazla siparişi veren ilk 10 müşteri :
df.groupby("master_id").agg({"total_order_num": "sum"}).\
    sort_values("total_order_num", ascending=False).head(10)

#                                      total_order_num
# master_id
# 5d1c466a-9cfd-11e9-9897-000d3a38a36f           202.00
# cba59206-9dd1-11e9-9897-000d3a38a36f           131.00
# a57f4302-b1a8-11e9-89fa-000d3a38a36f           111.00
# fdbe8304-a7ab-11e9-a2fc-000d3a38a36f            88.00
# 329968c6-a0e2-11e9-a2fc-000d3a38a36f            83.00
# 73fd19aa-9e37-11e9-9897-000d3a38a36f            82.00
# 44d032ee-a0d4-11e9-a2fc-000d3a38a36f            77.00
# b27e241a-a901-11e9-a2fc-000d3a38a36f            75.00
# d696c654-2633-11ea-8e1c-000d3a38a36f            70.00
# a4d534a2-5b1b-11eb-8dbd-000d3a38a36f            70.00

# Ön Hazırlık Sürecini Fonksiyonlaştıralım.

def pre_data(dataframe):
    # Total Price
    dataframe["total_price"] = dataframe["customer_value_total_ever_offline"] + \
                            dataframe["customer_value_total_ever_online"]
    # Total Order
    dataframe["total_order_num"] = dataframe["order_num_total_ever_offline"] + \
                                 dataframe["order_num_total_ever_online"]
    # Object to datetime
    for col in dataframe.columns:
        if "date" in col:
            dataframe[col] = dataframe[col].apply(pd.to_datetime)
    return dataframe

pre_data(df).head(10)


# Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını
# analiz tarihi olarak alalım.
df["last_order_date"].max()
today_date = dt.datetime(2021, 6, 1)

# Müşteri özelinde Recency, Frequency ve Monetary metriklerini hesaplayarak
# rfm adında yeni bir DataFrame oluşturalım.
rfm = df.groupby('master_id').agg({"last_order_date": lambda last_order_date: (today_date - last_order_date.max()).days,
                             "total_order_num": lambda total_order_num: total_order_num,
                             "total_price": lambda total_price: total_price})

# Değişken isimlerini Recency, Frequency ve Monetary olarak değiştirelim.
rfm.columns =  ["recency", "frequency", "monetary"]
rfm.head()

#                                      recency  frequency  monetary
# master_id
# 00016786-2f5a-11ea-bb80-000d3a38a36f       10       5.00    776.07
# 00034aaa-a838-11e9-a2fc-000d3a38a36f      298       3.00    269.47
# 000be838-85df-11ea-a90b-000d3a38a36f      213       4.00    722.69
# 000c1fe2-a8b7-11ea-8479-000d3a38a36f       27       7.00    874.16
# 000f5e3e-9dde-11ea-80cd-000d3a38a36f       20       7.00   1620.33


# RF Skorunun Hesaplanması

# Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevirelim.
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydedelim.

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels= [5, 4, 3, 2, 1])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels= [1, 2, 3, 4, 5])
#rank(method="first") // İlk gördüğünü ilk sınıfa ata
rfm["frequncy_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

# recency_score ve frequency_score’u tek bir değişken olarak ifade ederek RF_SCORE olarak kaydedelim.

rfm["RF_SCORE"] = (rfm["recency_score"].astype(str) +
                    rfm["frequncy_score"].astype(str))

rfm.head()

# RF Skorunun Segment Olarak Tanımlanması

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm['segment'] = rfm['RF_SCORE'].replace(seg_map, regex=True)

# master_id
# 00016786-2f5a-11ea-bb80-000d3a38a36f              champions
# 00034aaa-a838-11e9-a2fc-000d3a38a36f            hibernating
# 000be838-85df-11ea-a90b-000d3a38a36f                at_Risk
# 000c1fe2-a8b7-11ea-8479-000d3a38a36f              champions
# 000f5e3e-9dde-11ea-80cd-000d3a38a36f              champions
#                                                ...
# fff1db94-afd9-11ea-b736-000d3a38a36f                at_Risk
# fff4736a-60a4-11ea-8dd8-000d3a38a36f    potential_loyalists
# fffacd34-ae14-11e9-a2fc-000d3a38a36f                at_Risk
# fffacecc-ddc3-11e9-a848-000d3a38a36f        loyal_customers
# fffe4b30-18e0-11ea-9213-000d3a38a36f                at_Risk
# Name: segment, Length: 19945, dtype: object

# Sırada Aksiyon Almak Var :)

# Segmentlerin recency, frequnecy ve monetary ortalamalarını bir bakalım.
rfm[["segment", "recency", "frequency", "monetary"]].\
    groupby("segment").agg(["mean", "count"])

#                    recency       frequency       monetary
#                        mean count      mean count     mean count
# segment
# about_to_sleep       114.03  1643      2.41  1643   361.65  1643
# at_Risk              242.33  3152      4.47  3152   648.33  3152
# cant_loose           235.16  1194     10.72  1194  1481.65  1194
# champions             17.14  1920      8.97  1920  1410.71  1920
# hibernating          247.43  3589      2.39  3589   362.58  3589
# loyal_customers       82.56  3375      8.36  3375  1216.26  3375
# need_attention       113.04   806      3.74   806   553.44   806
# new_customers         17.98   673      2.00   673   344.05   673
# potential_loyalists   36.87  2925      3.31  2925   533.74  2925
# promising             58.69   668      2.00   668   334.15   668


# Aksiyon 1 :
# FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri
# tercihlerinin üstünde. Bu nedenle markanın tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak
# iletişime geçmek isteniliyor. Sadık müşterilerinden(champions, loyal_customers) ve kadın kategorisinden alışveriş
# yapan kişiler özel olarak iletişim kurulacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına kaydediniz.

special_segments = rfm[rfm["segment"].isin(["champions", "loyal_customers"])].index

spe_cust = df[(df["master_id"].isin(special_segments)) &
              (df["interested_in_categories_12"].str.contains("KADIN"))]["master_id"]

spe_cust.to_csv("new_brand_cust.csv", index=False)
spe_cust.shape


# Aksiyon 2 :
# B. Erkek ve Çocuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte
# iyi müşteri olan ama uzun süredir alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni
# gelen müşteriler özel olarak hedef alınmak isteniyor. Uygun profildeki müşterilerin id'lerini csv dosyasına kaydediniz.

special_segments2 = rfm[rfm["segment"].isin(["cant_loose", "hibernating", "new_customers"])].index

spe_cust2 = df[(df["master_id"].isin(special_segments2)) &
               ((df["interested_in_categories_12"].str.contains("ERKEK"))|
                (df["interested_in_categories_12"].str.contains("COCUK")))]["master_id"]

spe_cust2.to_csv("discount_cust.csv", index=False)
spe_cust2.shape
