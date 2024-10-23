import streamlit as st
import pandas as pd

# データの読み込み
df = pd.read_csv('./data/all_patch_note.csv')

# '変更前' と '変更後' を数値に変換できるものは数値にし、それ以外はそのままにする
df['変更前'] = pd.to_numeric(df['変更前'], errors='coerce').fillna(df['変更前'])
df['変更後'] = pd.to_numeric(df['変更後'], errors='coerce').fillna(df['変更後'])


'''
# LOLの過去パッチノートのデータ探索
簡易的にこのページでデータ探索ができます。
詳しいcsvは下記から取得してください
https://github.com/pannacotta326/lol_patch_notes/tree/main/data
中身を見ればわかりますが、あまり推奨されないやり方で取得しています。
また取得の仕方が未熟なため間違ったデータや、取得しきれていないデータがあります。
ご了承ください。
再配布は禁止です。

#### ①チャンプ別、頻出変更項目ランキング  
厳密にはキャラクター以外の項目も少し入っている。  
変更が多い項目はそのキャラクターの勝率を左右する項目であったり、  
ゲームにおいて調整の影響が強い項目といえる。  
  
#### ②特定のステータスが沢山変更されたチャンピオン  
キャラクターごとの勝利コンセプトによって必要なステータスは異なる。  
各ステータスが大事なキャラクターや戦闘スタイルがわかれば、  
そのステータスを強化するアイテムが強いときに、  
どんなキャラクターが強くなるか予想ができる。  
  
#### ③チャンプ別のパッチ遍歴  
不健全な強化や、使用方法が開拓された際、多くの場合はすぐに大きな変更が加わわる。  
過去のゲーム環境(流行りの戦略)を分析するときに、特定のキャラクターが原因を特定できる。  
  
#### ④パッチバージョンごとの変更内容  
過去のパッチノートにアクセスするのはとても労力がいるので、簡単に表示できるようにした。  
'''

# ① 頻出変更項目ランキング
st.sidebar.header('①チャンプ別、頻出変更項目ランキング')

# 頻出した変更対象をランキングで表示
select_cat_ranking = st.sidebar.selectbox('①の変更対象を選択', df['変更対象'].unique())
select_cat_rank_df = df[df['変更対象'] == select_cat_ranking]

st.header(f"①{select_cat_ranking} の頻出変更項目ランキング")
select_cat_count_rank_df = select_cat_rank_df['変更概要'].value_counts().reset_index()
select_cat_count_rank_df.columns = ['変更概要', '頻度',]
st.table(select_cat_count_rank_df)

# ② 変更部分ごとの頻出度順のデータ表示
st.sidebar.header('②特定のステータスが沢山変更されたチャンピオン')
select_change_part = st.sidebar.selectbox('②の変更部分を選択', df['変更部分'].unique())
select_change_part_df = df[df['変更部分'] == select_change_part]

select_change_part_count_df = select_change_part_df['変更対象'].value_counts().reset_index()
select_change_part_count_df.columns = ['変更対象', '頻度']

st.header(f"②{select_change_part}が沢山変更されたチャンピオン")
st.table(select_change_part_count_df)

st.subheader(f"{select_change_part} の集計対象")
# 選択された変更部分に基づいた詳細情報も表示
st.write(select_change_part_df[['パッチバージョン', '変更対象', '変更概要', '変更前', '変更後']])

# ③ 選択した変更対象のパッチ遍歴
st.sidebar.header('③チャンプ別のパッチ遍歴')
select_cat_trans = st.sidebar.selectbox('③の変更対象を選択', df['変更対象'].unique())
select_cat_trans_df = df[df['変更対象'] == select_cat_trans]

st.header(f"②{select_cat_trans} のパッチ遍歴")
st.write(select_cat_trans_df[['パッチバージョン', '変更概要', '変更部分', '変更前', '変更後']])

# ④ パッチバージョンごと表示
st.sidebar.header('④パッチバージョンごとの変更内容')
select_ver_patch = st.sidebar.selectbox('④見たいパッチバージョンを選択', df['パッチバージョン'].unique())
select_ver_patch_df = df[df['パッチバージョン'] == select_ver_patch]

st.header(f"パッチ {select_ver_patch} の変更内容")
st.write(select_ver_patch_df[['変更対象', '変更概要', '変更部分', '変更前', '変更後']])
