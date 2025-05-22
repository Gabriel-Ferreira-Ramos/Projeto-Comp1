import os

tabela_periodica = {
    "H": {
"nome": "Hidrogênio",
"massa_atomica": 1.008,
"numero_protons": 1,
"numero_eletrons": 1,
"simbolo": "H",
"numero_atomico": 1,
"grupo": 1,
"periodo": 1
},
"He": {
"nome": "Hélio",
"massa_atomica": 4.0026,
"numero_protons": 2,
"numero_eletrons": 2,
"simbolo": "He",
"numero_atomico": 2,
"grupo": 18,
"periodo": 1
},
"Li": {
"nome": "Lítio",
"massa_atomica": 6.94,
"numero_protons": 3,
"numero_eletrons": 3,
"simbolo": "Li",
"numero_atomico": 3,
"grupo": 1,
"periodo": 2
},
"Be": {
"nome": "Berílio",
"massa_atomica": 9.0122,
"numero_protons": 4,
"numero_eletrons": 4,
"simbolo": "Be",
"numero_atomico": 4,
"grupo": 2,
"periodo": 2
},
"B": {
"nome": "Boro",
"massa_atomica": 10.81,
"numero_protons": 5,
"numero_eletrons": 5,
"simbolo": "B",
"numero_atomico": 5,
"grupo": 13,
"periodo": 2
},
"C": {
"nome": "Carbono",
"massa_atomica": 12.011,
"numero_protons": 6,
"numero_eletrons": 6,
"simbolo": "C",
"numero_atomico": 6,
"grupo": 14,
"periodo": 2
},
"N": {
"nome": "Nitrogênio",
"massa_atomica": 14.007,
"numero_protons": 7,
"numero_eletrons": 7,
"simbolo": "N",
"numero_atomico": 7,
"grupo": 15,
"periodo": 2
},
"O": {
"nome": "Oxigênio",
"massa_atomica": 15.999,
"numero_protons": 8,
"numero_eletrons": 8,
"simbolo": "O",
"numero_atomico": 8,
"grupo": 16,
"periodo": 2
},
"F": {
"nome": "Flúor",
"massa_atomica": 18.998,
"numero_protons": 9,
"numero_eletrons": 9,
"simbolo": "F",
"numero_atomico": 9,
"grupo": 17,
"periodo": 2
},
"Ne": {
"nome": "Neônio",
"massa_atomica": 20.18,
"numero_protons": 10,
"numero_eletrons": 10,
"simbolo": "Ne",
"numero_atomico": 10,
"grupo": 18,
"periodo": 2
},
"Np": {
"nome": "Neptunium",
"massa_atomica": 236.98,
"numero_protons": 93,
"numero_eletrons": 93,
"simbolo": "Np",
"numero_atomico": 93,
"grupo": 7,
"periodo": 7
},
"Pu": {
"nome": "Plutónio",
"massa_atomica": 244.05,
"numero_protons": 94,
"numero_eletrons": 94,
"simbolo": "Pu",
"numero_atomico": 94,
"grupo": 8,
"periodo": 7
},
"Am": {
"nome": "Armerício",
"massa_atomica": 242.93,
"numero_protons": 95,
"numero_eletrons": 95,
"simbolo": "Am",
"numero_atomico": 95,
"grupo": 9,
"periodo": 7
},
"Cm": {
"nome": "Cúrio",
"massa_atomica": 247.09,
"numero_protons": 96,
"numero_eletrons": 96,
"simbolo": "Cm",
"numero_atomico": 96,
"grupo": 10,
"periodo": 7
},
"Bk": {
"nome": "Berquélio",
"massa_atomica": 247.07,
"numero_protons": 97,
"numero_eletrons": 97,
"simbolo": "Bk",
"numero_atomico": 97,
"grupo": 11,
"periodo": 7
},
"Cf": {
"nome": "Califórnio",
"massa_atomica": 250.51,
"numero_protons": 98,
"numero_eletrons": 98,
"simbolo": "Cf",
"numero_atomico": 98,
"grupo": 12,
"periodo": 7
},
"Es": {
"nome": "Einstênio",
"massa_atomica": 252.97,
"numero_protons": 99,
"numero_eletrons": 99,
"simbolo": "Es",
"numero_atomico": 99,
"grupo": 13,
"periodo": 7
},
"Fm": {
"nome": "Férmio",
"massa_atomica": 256.89,
"numero_protons": 100,
"numero_eletrons": 100,
"simbolo": "Fm",
"numero_atomico": 100,
"grupo": 14,
"periodo": 7
},
"Md": {
"nome": "Mendelévio",
"massa_atomica": 258.78,
"numero_protons": 101,
"numero_eletrons": 101,
"simbolo": "Md",
"numero_atomico": 101,
"grupo": 15,
"periodo": 7
},
"No": {
"nome": "Nobéli",
"massa_atomica": 260.67,
"numero_protons": 102,
"numero_eletrons": 102,
"simbolo": "No",
"numero_atomico": 102,
"grupo": 16,
"periodo": 7
},
"Lr": {
"nome": "Laurê",
"massa_atomica": 264.86,
"numero_protons": 103,
"numero_eletrons": 103,
"simbolo": "Lr",
"numero_atomico": 103,
"grupo": 17,
"periodo": 7
},
"Rf": {
"nome": "Rutherfórdio",
"massa_atomica": 266.32,
"numero_protons": 104,
"numero_eletrons": 104,
"simbolo": "Rf",
"numero_atomico": 104,
"grupo": 4,
"periodo": 7
},
"Db": {
"nome": "Dúbni",
"massa_atomica": 268.14,
"numero_protons": 105,
"numero_eletrons": 105,
"simbolo": "Db",
"numero_atomico": 105,
"grupo": 5,
"periodo": 7
},
"Sg": {
"nome": "Seabór",
"massa_atomica": 270.48,
"numero_protons": 106,
"numero_eletrons": 106,
"simbolo": "Sg",
"numero_atomico": 106,
"grupo": 6,
"periodo": 7
},
"Bh": {
"nome": "Bóhrio",
"massa_atomica": 270.92,
"numero_protons": 107,
"numero_eletrons": 107,
"simbolo": "Bh",
"numero_atomico": 107,
"grupo": 7,
"periodo": 7
},
"Hs": {
"nome": "Hássio",
"massa_atomica": 275.38,
"numero_protons": 108,
"numero_eletrons": 108,
"simbolo": "Hs",
"numero_atomico": 108,
"grupo": 8,
"periodo": 7
},
"Mt": {
"nome": "Meitnério",
"massa_atomica": 278.13,
"numero_protons": 109,
"numero_eletrons": 109,
"simbolo": "Mt",
"numero_atomico": 109,
"grupo": 9,
"periodo": 7
},
"Ds": {
"nome": "Darmstádtio",
"massa_atomica": 282.57,
"numero_protons": 110,
"numero_eletrons": 110,
"simbolo": "Ds",
"numero_atomico": 110,
"grupo": 10,
"periodo": 7
},
"Rg": {
"nome": "Roentgênio",
"massa_atomica": 283.08,
"numero_protons": 111,
"numero_eletrons": 111,
"simbolo": "Rg",
"numero_atomico": 111,
"grupo": 11,
"periodo": 7
},
"Cn": {
"nome": "Copernício",
"massa_atomica": 286.09,
"numero_protons": 112,
"numero_eletrons": 112,
"simbolo": "Cn",
"numero_atomico": 112,
"grupo": 12,
"periodo": 7
},
"Nh": {
"nome": "Nihônio",
"massa_atomica": 287.99,
"numero_protons": 113,
"numero_eletrons": 113,
"simbolo": "Nh",
"numero_atomico": 113,
"grupo": 13,
"periodo": 7
},
"Fl": {
"nome": "Fleróvio",
"massa_atomica": 290.21,
"numero_protons": 114,
"numero_eletrons": 114,
"simbolo": "Fl",
"numero_atomico": 114,
"grupo": 14,
"periodo": 7
},
"Mc": {
"nome": "Moscóvio",
"massa_atomica": 291.54,
"numero_protons": 115,
"numero_eletrons": 115,
"simbolo": "Mc",
"numero_atomico": 115,
"grupo": 15,
"periodo": 7
},
"Lv": {
"nome": "Livermório",
"massa_atomica": 292.47,
"numero_protons": 116,
"numero_eletrons": 116,
"simbolo": "Lv",
"numero_atomico": 116,
"grupo": 16,
"periodo": 7
},
"Ts": {
"nome": "Tenesso",
"massa_atomica": 293.73,
"numero_protons": 117,
"numero_eletrons": 117,
"simbolo": "Ts",
"numero_atomico": 117,
"grupo": 17,
"periodo": 7
},
"Og": {
"nome": "Oganessônio",
"massa_atomica": 295.21,
"numero_protons": 118,
"numero_eletrons": 118,
"simbolo": "Og",
"numero_atomico": 118,
"grupo": 18,
"periodo": 7
},
}

def menuPrincipal():
    print(" ------------------------------ \nEscolha uma das alternativas \nMostrar Elemento (1)")

def exibirElemento(elemento_escolido):
    print(tabela_periodica[elemento_escolido])


def main():

    menuPrincipal()
    a = int(input())
    os.system('clear')
    
    while a != 1:
        menuPrincipal()
        a = int(input())
        os.system('clear')

    if a == 1:
        elemento = input("Qual elemento você quer?\n")
        exibirElemento(elemento_escolido=elemento)


main()