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


if __name__ == "__main__":
        st.set_page_config(
        page_title="ポケモンリーグサイト",
        page_icon="🎮",
        initial_sidebar_state="expanded"
        )
        
        st.title('ポケモンリーグ')
        st.write('これは名も無い８人のトレーナの戦い・・・')
        st.write('最強のポケモントレーナーを決めるリーグがここに始まる・・・')
        
        tab1, tab2,tab3,tab4 = st.tabs(["リーグ成績", "スクリム成績","トレーナープロフィール","リーグルール"])
        with tab1:
            pass
        
        with tab2:
            pass
        
        with tab3:
            option = st.selectbox(
                'トレーナー',
                ('あべるむ','アリー','エタ', 'カイト','TOM','モモ','ゆきの')
            )

            st.write("Traner's name:", option)
            if option == 'あべるむ':
                col1, col2 = st.columns([1,1])

                with col1:

                    values = np.array([80, 66, 96, 58, 68])
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
                with col2:
                    st.text('歯茎を見せたら止まらない。')

            if option == 'エタ':
                values = np.array([31, 50, 22, 32, 99])
                labels = ["知力","判断力","育成力","メンタル","運"]
                col1, col2 = st.columns([1,1])

                with col1:
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
                    ax.set_rlim([min(rgrids), max(rgrids)])
                    ax.set_title("トレーナースキル", pad=20)
                    st.pyplot(fig)
                with col2:
                    st.text('企画でいっぱいいっぱいw')
            
        with tab4:
            st.header('ルール')
            st.text('ポケモンバトルノーマルルールを採用。')
            st.text('3vs3でポケモンを全てが瀕死にした方が勝利。')
            st.text('参加トレーナ間の総当たり戦を行う。')
            st.text('勝利数の多さで順位を決定する。')
            st.text('勝利数が同数の場合以下の成績により順位を決定する。')
            st.text('得失点差（倒したポケモン数と倒されたポケモンの差）。')
            st.text('得点（倒したポケモンの数）。')
            st.text('禁止ポケモンはなし。')
            

