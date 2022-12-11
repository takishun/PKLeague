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
        
        tab1, tab2,tab3 = st.tabs(["リザルト","トレーナープロフィール","リーグルール"])
        with tab1:
            ResultTab = st.selectbox(
                'ランキング',
                ('リーグ成績','スクリム成績')
            )
            
            if ResultTab == 'リーグ成績':
                df = pd.read_csv('PokemonLeague.csv')
#                 df.index = df['トレーナー名']
                df = df.sort_values(['勝','得失点','得点'],ascending=False)
                df.index = np.arange(1, len(df)+1)

                st.table(df)
                
                
            if ResultTab == 'スクリム成績':
                df = pd.read_csv('PokemonLeague.csv')
#                 df.index = df['トレーナー名']
                st.table(df.sort_values('勝',ascending=False))                
        
        with tab2:
            option = st.selectbox(
                'トレーナー',
                ('あべるむ','アリー','エタ', 'カイト','TOM','モモ','ゆきの')
            )

            st.write("Traner's name:", option)
#              ["知力","判断力","育成力","メンタル","運"]
            if option == 'あべるむ':
                col1, col2 = st.columns([1,1])
                values = np.array([80, 66, 96, 58, 68])
                st.balloons()
                with col1:
                    image = Image.open('averm.png')
                    st.text('歯茎を見せたら止まらない。')
                    st.image(image,use_column_width=True)
                    
                with col2:
                    rader_c(values)

            if option == 'エタ':
                values = np.array([50, 50, 30, 90, 5])
                col1, col2 = st.columns([1,1])

                with col1:
                    st.text('企画でいっぱいいっぱいw')
                    
                with col2:
                    rader_c(values)
                    
            if option == 'カイト':
                values = np.array([60, 75, 45, 60, 50])
                col1, col2 = st.columns([1,1])

                with col1:
                    st.text('見た目はカビゴン')                    
                with col2:
                    rader_c(values)

            if option == 'ゆきの':
                col1, col2 = st.columns([1,1])
                values = np.array([60, 50, 80, 25, 70])
                st.snow()
                with col1:
                    st.text('Yukinon Game！　読み方はお任せする・・・')
 
                with col2:
                    rader_c(values)
            
            if option == 'アリー':
                col1, col2 = st.columns([1,1])
                values = np.array([60, 60, 60, 70, 70])
                
                with col1:
                    st.text('たぶん1番の常識人')
 
                with col2:
                    rader_c(values)

            if option == 'TOM':
                col1, col2 = st.columns([1,1])
                values = np.array([80, 80, 80, 60, 40])
                
                with col1:
                    st.text('ガチ勢')
 
                with col2:
                    rader_c(values)

            if option == 'モモ':
                col1, col2 = st.columns([1,1])
                values = np.array([40, 80, 80, 55, 75])
                
                with col1:
                    st.text('いいやつ')
 
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
            

