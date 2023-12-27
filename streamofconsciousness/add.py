f = open("streamlit/streamofconsciousness/input.txt", "r")
testo = f.read()
f.close()
testo1 = "\nst.markdown{r'''\n" + testo + "\n''')\n\n"
s = open("streamlit/streamofconsciousness/stream.py", "r")
righe = s.readlines()
righe[8] += testo1
s = open("streamlit/streamofconsciousness/stream.py", "w")
s.writelines(righe)
s.close()
