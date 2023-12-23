import streamlit as st

st.image('https://my9oso6gqm.github.io/mrz.jpg', width=100)

st.markdown(r'''
Logica matematica, teoria dei numeri, calcolo mentale, giganti sistemi di equazioni, errori nei libri di matematica, liste.
''')

st.markdown(r'''
# 07:34 23-12-2023

Ascoltando: Galantis - Bang banng! (My neurodivergent anthem) [https://youtube.com/watch?v=CquFFychvTo](https://youtube.com/watch?v=CquFFychvTo).

A parte che facebook stamane mi propina le pubblicità del National Reconnaissance Office, quello che gestisce i satelliti spia per la CIA ma anche per l'NSA. Ma ppperchè?

Il task per le 9:
''')

st.image('https://github.com/my9oso6gqm/streamlit/blob/main/streamofconsciousness/documenti/231220230711.jpg')

st.markdown(r'''
È unire questo:

```python

# Codice per interrogare ib

from ibapi.client import *
from ibapi.wrapper import *

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self) 
        self.data = []
        
    def nextValidId(self, orderId: int):
        
        mycontract = Contract()
        mycontract.symbol = "AAPL"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"        
            
   
        self.reqHistoricalData(orderId, mycontract, '20231126 15:59:00 US/Eastern', '1 D', '1 hour', 'TRADES', 0, 1, 0, [])

    def historicalData(self, reqId, bar):
        self.data.append([bar.date, bar.close])
        app.disconnect()

app = IBapi()
app.connect('127.0.0.1', 7497, 100)
app.run()
```

Con questo:

```python

# Codice per piazzare un ordine

from ibapi.client import *
from ibapi.wrapper import *

class TestApp(EClient, EWrapper):
  def __init__(self):
    EClient.__init__(self, self)

  def nextValidId(self, orderId: OrderId):

    mycontract = Contract()
    mycontract.symbol = "AAPL"
    mycontract.secType = "STK"    
    mycontract.exchange = "SMART"
    mycontract.currency = "USD"

    self.reqContractDetails(orderId, mycontract)

  def contractDetails(self, reqId: int, contractDetails: ContractDetails):
    print(contractDetails.contract)

    myorder = Order()
    myorder.orderId = reqId
    myorder.action = "BUY"
    myorder.tif = "GTC"
    myorder.orderType = "LMT"
    myorder.lmtPrice = 1440.80
    myorder.totalQuantity = 1

    self.placeOrder(myorder.orderId, contractDetails.contract, myorder)


  def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
    print(f"openOrder. orderId: {orderId}, contract: {contract}, order: {order}")

  def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
    print(f"orderId: {orderId}, status: {status}, filled: {filled}, remaining: {remaining}, avgFillPrice: {avgFillPrice}, permId: {permId}, parentId: {parentId}, lastFillPrice: {lastFillPrice}, clientId: {clientId}, whyHeld: {whyHeld}, mktCapPrice: {mktCapPrice}")

  def execDetails(self, reqId: int, contract: Contract, execution: Execution):
    print(f"reqId: {reqId}, contract: {contract}, execution: {execution}")

app = TestApp()
app.connect("127.0.0.1", 7497, 100)
app.run()
```

Voi come fareste? In sostanza noi si tratta d'altro che trovare le parti simili e toglierle o da una o dall'altra parte, facendo qualche aggiustamento.

E poi mettere giù un modello tipo:
''')

st.latex(r'\text{SMA} = \frac{P_1+P_2+P_n}{n}')

st.markdown(r'''
Per fare qualche previsione. Sta notte ho letto degli altri modi carini per implementarlo su dei libri (Doing math with python e il Python for finance).

E mettiamo tutto su un quaderno Google colab aggiungendo l'interrogazione di yh finance per chi non usa ib.

Ah! Come si avvicina Babbo Natale secondo il NORAD:
''')

st.image('https://raw.githubusercontent.com/my9oso6gqm/streamlit/main/streamofconsciousness/documenti/231220230729.jpg')


st.markdown(r'''
# 22:09 22-12-2023
Chiudono deboli le Borse europee nell'ultima seduta prima della pausa natalizia, nonostante il dato sull'inflazione Pce negli Stati Uniti rafforzi l'ottimismo sulle prossime mosse di politica monetaria.  
ilsole''')


st.markdown(r'''
# 23:24 21-12-2023
Nuovo stop alla lunga serie positiva dei listini europei sulle prospettive di tagli ai tassi d’interesse da parte delle banche centrali già a partire dal 2024. 
Si muove rialzo a Wall Street, dopo che Dow Jones e Nasdaq Composite, ieri, hanno vissuto la peggiore giornata da ottobre, lo S&P 500 da settembre.  
ilsole
''')

st.markdown(r'''
# 10:26 21-12-2023
Aperta una posizione buy da python su ibkr, non si poteva chiudere quello che ho fatto da app dopo capite il perchè(1).  

Ascoltando: [https://youtube.com/watch?v=fCj2p1Ugwdo](https://youtube.com/watch?v=fCj2p1Ugwdo).

```python
from ibapi.client import *
from ibapi.wrapper import *

class TestApp(EClient, EWrapper):
  def __init__(self):
    EClient.__init__(self, self)

  def nextValidId(self, orderId: OrderId):

    mycontract = Contract()
    mycontract.symbol = "AAPL"
    mycontract.secType = "STK"    
    mycontract.exchange = "SMART"
    mycontract.currency = "USD"

    self.reqContractDetails(orderId, mycontract)

  def contractDetails(self, reqId: int, contractDetails: ContractDetails):
    print(contractDetails.contract)

    myorder = Order()
    myorder.orderId = reqId
    myorder.action = "BUY"
    myorder.tif = "GTC"
    myorder.orderType = "LMT"
    myorder.lmtPrice = 1440.80
    myorder.totalQuantity = 1

    self.placeOrder(myorder.orderId, contractDetails.contract, myorder)


  def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
    print(f"openOrder. orderId: {orderId}, contract: {contract}, order: {order}")

  def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
    print(f"orderId: {orderId}, status: {status}, filled: {filled}, remaining: {remaining}, avgFillPrice: {avgFillPrice}, permId: {permId}, parentId: {parentId}, lastFillPrice: {lastFillPrice}, clientId: {clientId}, whyHeld: {whyHeld}, mktCapPrice: {mktCapPrice}")

  def execDetails(self, reqId: int, contract: Contract, execution: Execution):
    print(f"reqId: {reqId}, contract: {contract}, execution: {execution}")

app = TestApp()
app.connect("127.0.0.1", 7497, 100)
app.run()
```

La cosa interessante è che appare anche sul tws:
''')

st.image('https://my9oso6gqm.github.io/tmp/211220230954.png')

st.markdown(r'''
Che nell'app:
''')
         
st.image('https://my9oso6gqm.github.io/tmp/211220230957.jpg')

st.markdown(r'''
Questo mi risparmia di mettere giù una dashboard per il controllo manuale in python. Tra l'altro ibkr mette prioritarie le operazioni da tws e app che le api, salva culo incorporated(1).

Comunque come dicevo la parte interessante è l'analisi.

Ora scarico i dati e faccio un modello di media mobile semplice con una finestra di 5.

M = (x_1 + x_2 + x_3 + x_4 + x_5) / 5.

O:
''')

st.latex(r'''\frac{x_1 + x_2 + x_3 + x_4 + x_5}{5}''')

st.markdown(r'''
Che in python diventa:

```python
a = x_1 + x_2 + x_3 + x_4 + x_5
b = a / 5
```

Esiste una comoda funzione per farlo con una riga ma preferisco fare le cose a manina quando ho tempo.

Il modello lo possiamo formalizzare con una sommatoria. Ma perchè complicarci la vita in modo formale?
''')

st.latex(r'''\frac{1}{k}\sum_{i=n-k+1}^{n}p_{i}''')

st.markdown(r'''
Beh, guardate come diventa in python puro lavorando formalmente, molto piu semplice!

```python
a = [10,2,3,4,5]
b = 0

for x in a:
    b = b + x

y = b/5
```

E qui una seconda analisi, questo è lo stocastico con il metodo Monte Carlo (Usando numpy e non a manina):

```python
S0 = 100
r = 0.05
sigma = 0.25
T = 2.0
I = 10000
ST1 = S0 * np.exp((r - 0.5 * sigma ** 2) * T +
sigma * math.sqrt(T) * npr.standard_normal(I))
```

Vado a dormire 6 ore. A dopo!
''')

st.markdown(r'''
# 07:39 21-12-2023
Ma che noia che Instagram richieda l'uso dell'app per cambiare le impostazioni. Ma soprattutto quale diamine di workaround devo inventarmi per far girare vscode in un docker??? Vabbe, vado a chiudere una posizione buy con python che avevo aperto dall'app di ibkr sul Nikkei.
''')

st.markdown(r"""
# 22:46 20-12-2023
Piazzare un buy o un sell in ibkr [https://ibkrcampus.com/trading-lessons/python-placing-orders/](https://ibkrcampus.com/trading-lessons/python-placing-orders/).
""")

st.markdown(r"""
# 22:17 20-12-2023
Borse europee ingessate, ma tiene banco risiko tlc  
La conferma che la battaglia contro l’inflazione stia dando i suoi frutti arriva stavolta dal Regno Unito, ma questo non è bastato ad accendere le Borse europee che chiudono fiacche la seduta, con la sola eccezione di Londra, che guadagna oltre l'1%.  

Wall Street in rialzo dopo la pubblicazione di dati economici positivi.  

ilsole
""")

st.markdown(r"""
# 09:02 20-12-2023
Gayle - Ur just horny [https://youtube.com/watch?v=DWvuD31VG6Q](https://youtube.com/watch?v=DWvuD31VG6Q).
""")

st.markdown(r"""
# 08:52 20-12-2023
Vado a dormire. Ho tribulato un po' nella speranza di aprire e chiudere un ordine e invece la solita interrogazione delle varie chiusure. Però adesso del NYSE!!! 
""")

st.image('https://my9oso6gqm.github.io/tmp/201220230840.jpg')

st.markdown(r"""
Dopo cerco di aprire e chiudere un ordine e fare un'analisi oltre la media mobile.  
Yep, questo codice ha dei bei salti.
""")

st.markdown(r"""
# 06:53 20-12-2023
Il gruppo hacker russo Lockbit ha rivendicato l’attacco ransomware che negli ultimi dieci giorni ha investito pubbliche amministrazioni in Italia che si avvalgono dei servizi di Westpole.  
ilsole
""")
