import streamlit as st

st.markdown("""
# Ciao
Mirror al mio [what's new](https://my9oso6gqm.github.io/liste/whats-new.htm).
""")

st.markdown("""
## Tasso d'interesse annuale effettivo
11-12-2023 16:43
\\
\\
Tasso d'interesse annuale effettivo da un investimento di 1 anno:
""")
st.latex(r"""
i = \frac{V(t + 1) - V(t)}{V(t)}
""")

st.markdown("""
## Prova
11-12-2023 12:00
\\
\\
Lorem ipsum dolor sit amet.
""")

st.markdown(r"""
## Prova
11-12-2023 12:00
\begin{gather*}
a_1=b_1+c_1\\
a_2=b_2+c_2-d_2+e_2
\end{gather*}
""")
