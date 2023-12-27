f = open("devops/streamofconsciousness/input.txt", "r")
testo = f.read()
f.close()
testo1 = "\nst.markdown{r'''\n" + testo + "\n''')\n\n"
s = open("stream.py", "r")
righe = s.readlines()
righe[8] += testo1
s = open("devops/streamofconsciousness/stream.py", "w")
s.writelines(righe)
s.close()
