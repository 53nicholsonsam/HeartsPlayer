warning: LF will be replaced by CRLF in .ipynb_checkpoints/main-checkpoint.ipynb
.
The file will have its original line endings in your working directory
diff --git a/.ipynb_checkpoints/main-checkpoint.ipynb b/.ipynb_checkpoints/main-
checkpoint.ipynb
index 78cebb7..54c0e6b 100644
--- a/.ipynb_checkpoints/main-checkpoint.ipynb
+++ b/.ipynb_checkpoints/main-checkpoint.ipynb
@@ -2,17 +2,16 @@
  "cells": [
   {
    "cell_type": "code",
-   "execution_count": 1,
+   "execution_count": 40,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
-      "['4d', '8h', '3d', '12s', '5h', '5c', '9c', '6s', '8c', '3s', '3c', '2d'
, '9h']\n",
-      "['6d', '11c', '5s', '1d', '6c', '11h', '10s', '8s', '7d', '1c', '5d', '4
s', '4c']\n",
-      "['13c', '11s', '12c', '10c', '10d', '8d', '3h', '4h', '6h', '7s', '12d',
 '2s', '2h']\n",
-      "['11d', '1s', '13s', '10h', '13d', '7h', '9s', '12h', '13h', '9d', '1h',
 '7c', '2c']\n"
+      "['03d', '13h', '11d', '05h', '08h', '08c', '13c', '05d', '08d', '09c', '
01s', '12h', '03s']\n",
+      "['03d', '13h', '11d', '05h', '08h', '08c', '13c', '05d', '08d', '09c', '
01s', '12h', '03s']\n",
+      "['01s', '03d', '03s', '05d', '05h', '08c', '08d', '08h', '09c', '11d', '
12h', '13c', '13h']\n"
      ]
     }
    ],
@@ -26,8 +25,8 @@
     "deck=[]\n",
     "for item in Suits:\n",
     "  for num in Numbers:\n",
-    "    deck.append(str(num)+item) #Creating the cards here\n",
-    "#print(deck)\n",
+    "    #print (num)\n",
+    "    deck.append(str(num).zfill(2)+item) #Creating the cards here\n",
     "indexdeck=list(range(1,53)) #Need to index the deck so that we can deal it
\n",
     "temptodict=[] \n",
     "for i in range(0,len(indexdeck)): #Sew up the index and the card so that w
e can deal\n",
@@ -63,11 +62,43 @@
     "  player4hand.append(deckwindex[Player4deal[ii]])\n",
     "  #Players now each have a hand of 13 cards\n",
     "print(player1hand)\n",
-    "print(player2hand)\n",
-    "print(player3hand)\n",
-    "print(player4hand)"
+    "#print(player2hand)\n",
+    "#print(player3hand)\n",
+    "#print(player4hand)\n",
+    "\n",
+    "###Organizing the player's hands\"###\n",
+    "hands=[player1hand,player2hand,player3hand,player4hand]\n",
+    "\n",
+    "#print(hands)\n",
+    "def takesecond(elem):\n",
+    "    return[item.split()[-1] for item in elem]\n",
+    "print (takesecond(player1hand))\n",
+    "#print(order)\n",
+    "player1hand=sorted(player1hand, key=takesecond)\n",
+    "player2hand=sorted(player2hand, key=lambda n: n.split()[-1])\n",
+    "player3hand=sorted(player3hand, key=lambda n: n.split()[-1])\n",
+    "player4hand=sorted(player4hand, key=lambda n: n.split()[-1])\n",
+    "#print(order)\n",
+    "print(player1hand)\n",
+    "#print(player2hand)\n",
+    "#print(player3hand)\n",
+    "#print(player4hand)"
    ]
   },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "metadata": {},
+   "outputs": [],
+   "source": []
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "metadata": {},
+   "outputs": [],
+   "source": []
+  },
   {
    "cell_type": "code",
    "execution_count": null,

