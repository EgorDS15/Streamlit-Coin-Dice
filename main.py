import streamlit as st
import numpy as np


# Code for throwing coin
def throw_coin(bet):
    side = ['Head', 'Tail']
    if st.sidebar.button("Throw!"):
        res = np.random.choice(side, p=[0.5, 0.5])
        if (bet == 'Head') & (res == 'Head'):
            st.write(res)
            st.write("Fuck! You\'re winner!")
            st.image('files\\win.gif')
            st.balloons()
        elif (bet == 'Tail') & (res == 'Tail'):
            st.write(res)
            st.write("Fuck! You\'re winner!")
            st.image('files\\win.gif')
            st.balloons()
        else:
            st.write(res)
            st.write("LOOOSER!")
            st.image('files\\loose.gif')


# Return AI score in dice game
def ai_throw(x):
    return (np.random.randint(1, 7, x)).sum()


# Return user score in dice game
def my_throw(x):
    return (np.random.randint(1, 7, x)).sum()


# Compare AI and user scores
def dices(n):
    ai = ai_throw(n)
    me = my_throw(n)
    st.write("AI score\n", ai)
    if ai < me:
        st.write("You win, Bitch!")
    elif ai > me:
        st.write("Daaamn! You\'re so fckn looser!")
    else:
        st.write("Same result! Play again!")
    st.write("Your score ", me)


st.header("Let\'s play some shit!")
dice_type = st.sidebar.selectbox("Choose game", ("coin", "dice"))


def games():
    if dice_type == 'coin':
        st.image('files\\choose.gif')
        coin_bet = st.sidebar.radio("Choose your side", ["Head", "Tail"])
        return throw_coin(coin_bet)
    else:
        st.image('files\\hangover-math.gif')
        dices_count = st.sidebar.slider("How much dices?", 1, 5, 1)
        # ai_dice = ai_throw(dices_count)
        # st.write("AI score\n", ai_dice)
        if st.sidebar.button("Throw!"):
            return dices(dices_count)


if __name__ == '__main__':
    print(games())
