#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import datetime
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import streamlit as st
import numpy as np
from scipy.special import comb
from scipy.special import perm
import time
from PIL import Image

def rader_c(values):
        labels = ["知力","判断力","育成力","メンタル","運"]

        # 多角形を閉じるためにデータの最後に最初の値を追加する。
        radar_values = np.concatenate([values, [values[0]]])
        # プロットする角度を生成する。
        angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
        # メモリ軸の生成
        rgrids = [0, 20, 40, 60, 80, 100]

        fig = plt.figure(facecolor="w")
        # 極座標でaxを作成
        ax = fig.add_subplot(1, 1, 1, polar=True)
        # レーダーチャートの線を引く
        ax.plot(angles, radar_values)
        #　レーダーチャートの内側を塗りつぶす
        ax.fill(angles, radar_values, alpha=0.2)
        # 項目ラベルの表示
        ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)
        # 円形の目盛線を消す
        ax.set_rgrids([])
        # 一番外側の円を消す
        ax.spines['polar'].set_visible(False)
        # 始点を上(北)に変更
        ax.set_theta_zero_location("N")
        # 時計回りに変更(デフォルトの逆回り)
        ax.set_theta_direction(-1)

        # 多角形の目盛線を引く
        for grid_value in rgrids:
            grid_values = [grid_value] * (len(labels)+1)
            ax.plot(angles, grid_values, color="gray",  linewidth=0.5)

        # メモリの値を表示する
        for t in rgrids:
            # xが偏角、yが絶対値でテキストの表示場所が指定される
            ax.text(x=0, y=t, s=t)

        # rの範囲を指定
        ax.set_rlim([min(rgrids), max(rgrids)])
        ax.set_title("トレーナースキル", pad=20)
        st.pyplot(fig)    

if __name__ == "__main__":
        st.set_page_config(
        page_title="ポケモンリーグサイト",
        page_icon="🎮",
        initial_sidebar_state="expanded"
        )
        
        st.title('ポケモンリーグ')
        st.write('これは名も無い８人のトレーナの戦い・・・')
        st.write('最強のポケモントレーナーを決めるリーグがここに始まる・・・')
        
        st.subheader('新着情報')
        st.write('12/24 22:00- : リア充爆破しろ！クリスマス杯')
        
        tab1, tab2,tab3 = st.tabs(["リザルト","トレーナープロフィール","リーグルール"])
        with tab1:
            ResultTab = st.selectbox(
                '試合成績',
                ('リーグ成績','スクリム成績','クリスマス杯')
            )
            
            if ResultTab == 'リーグ成績':
                df = pd.read_csv('PokemonLeague.csv')
#                 df.index = df['トレーナー名']
                df = df.sort_values(['勝','得失点','得点'],ascending=False)
                df.index = np.arange(1, len(df)+1)
                st.table(df)
                
            if ResultTab == 'スクリム成績':
                df = pd.read_csv('scrim.csv')
#                 df.index = df['トレーナー名']
                st.table(df.sort_values('勝',ascending=False))
    
            if ResultTab == 'クリスマス杯':
#                 df = pd.read_csv('chiristmas.csv')
                    st.text('1:Tom、2:アリー、3:kaito、4:ですぺにゃ、5:あべるむ、6:もも、7:ゆきの')
#                     image = Image.open('chiristmas.jpg')
#                     st.image(image,use_column_width=True)
        
        with tab2:
            option = st.selectbox(
                'トレーナー',
                ('あべるむ','アリー','エタ', 'カイト','TOM','モモ','ゆきの')
            )

            st.write("Traner's name:", option)
#              ["知力","判断力","育成力","メンタル","運"]
            if option == 'あべるむ':
                col1, col2 = st.columns([1,1])
                values = np.array([90, 65, 80, 65, 70])
#                 st.balloons()
                with col1:
#                     image = Image.open('averm.png')
                    st.text('トレーナー紹介')
                    st.text('''
                    弱いやつは逃さない！
                    相手の所作で相手の経験が浅いか見抜く初心者センサー。
                    最低限の知識も持ち合わせていないトレーナーは門前払いだ一昨日きやがれ。
                    効率的な育成で繰り出すポケモンはどれもトップランク。
                    出した歯茎は止まらない！
                    ''')
#                     st.image(image,use_column_width=True)
                    
                with col2:
                    rader_c(values)

            if option == 'エタ':
                values = np.array([10, 50, 10, 90, 5])
                col1, col2 = st.columns([1,1])

                with col1:
                    st.text('トレーナー紹介')
                    st.text('''
                    ポケモンより企画に力を入れて本末転倒。
                    聖なるこの夜にリア中を爆破できればこれ以上望むことはない！
                    リア充を妬み、リア中を憎み、リア充を忌み嫌う、
                    タイプはあくを超えて、ゴミクズ野郎！
                    正確、人格、もう絶望！
                    ''')
                with col2:
                    rader_c(values)
                    
            if option == 'カイト':
                values = np.array([60, 85, 45, 60, 50])
                col1, col2 = st.columns([1,1])

                with col1:
                    st.text('トレーナー紹介')
                    st.text('''
                    でかーい！だけじゃないんです。
                    繊細なポケモン選択と戦術でいまやランクはマスターボール級！
                    実力はお墨付き！
                    見た目はケッキング、頭脳はミュウツー！
                    マスターボールランク・ダイナマイトボディ・ポケモンマスター
                    ''')
                with col2:
                    rader_c(values)

            if option == 'ゆきの':
                col1, col2 = st.columns([1,1])
                values = np.array([60, 50, 80, 30, 70])
#                 st.snow()
                with col1:
                    st.text('トレーナー紹介')
                    st.text('''
                    そのポケモンからは、
                    どんな美しい変幻自在の技を見せてくれるのか！
                    妖艶なるポケモンマスター！
                    ''')
 
                with col2:
                    rader_c(values)
            
            if option == 'アリー':
                col1, col2 = st.columns([1,1])
                values = np.array([90, 75, 85, 70, 70])
                
                with col1:
                    st.text('トレーナー紹介')
                    st.text('''
                    スクリムは準備が間に合わないながらも、豊富な知識でバトルを支配！
                    種族値、努力値、個体値、そんなの基本中の基本でしょ？
                    クイーン・オブ・ポケモンマスター
                    ''')
 
                with col2:
                    rader_c(values)

            if option == 'TOM':
                col1, col2 = st.columns([1,1])
                values = np.array([99, 80, 99, 60, 90])
                
                with col1:
                    st.text('トレーナー紹介')
                    st.text('''
                    スクリム６勝無敗の完全勝利、クリスマス杯も無敗で優勝！
                    マスカーニャの速度は誰にも止められない！
                    相手のサイクルも地割れでメンタルをかち割る！
                    優しいお昼の講師の姿には想像できない夜のゲームマスター！
                    ''')
 
                with col2:
                    rader_c(values)

            if option == 'モモ':
                col1, col2 = st.columns([1,1])
                values = np.array([40, 80, 80, 55, 75])
                
                with col1:
                    st.text('トレーナー紹介')
                    st.text('''
                    インファイトの強さはトップクラス。
                    基本はインファイトでゴリ押しでも、
                    タイプを使い分けて変則投球もできるんです。
                    技巧派ポケモントレーナー！
                    ''')
 
                with col2:
                    rader_c(values)

        with tab3:
            st.header('ルール')
            st.text('ポケモンバトルノーマルルールを採用。')
            st.text('3vs3でポケモンを全てが瀕死にした方が勝利。')
            st.text('参加トレーナ間の総当たり戦を行う。')
            st.text('勝利数の多さで順位を決定する。')
            st.text('勝利数が同数の場合以下の成績により順位を決定する。')
            st.text('得失点差（倒したポケモン数と倒されたポケモンの差）。')
            st.text('得点（倒したポケモンの数）。')
            st.text('禁止ポケモンはランクマッチルールに従います。')
            

