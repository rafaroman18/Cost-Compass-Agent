import csv
import io
import os 
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, "..", "..", "Step 1 - Data and domain") + os.sep
DB = os.path.join(HERE, "ref.db")
if os.path.exists(DB):
    os.remove(DB)
con = sqlite3.connect(DB)
c = con.cursor()

def rd(p, enc="cp1252"):
    return list(csv.reader(io.TextIOWrapper(open(B + p, "rb"), encoding=enc), delimiter=";"))[1:]

num = lambda s: None if s.strip() in ("", "..") else float(s.replace(",", "."))
strip = lambda s: re.sub(r"^\d\d ", "", s)

# IPV Table (Housing)
c.execute("CREATE TABLE ipv(ccaa TEXT, medida TEXT, periodo TEXT, valor REAL)")
for terr, ccaa, tipo, med, per, v in rd("Housing/IPV por CCAA 2020_2026.csv"):
    c.execute("INSERT INTO ipv VALUES(?,?,?,?)", ("Nacional" if ccaa == "" else strip(ccaa), med, per, num(v)))

# EPA Table (Employment)
c.execute("CREATE TABLE epa(sexo TEXT, ccaa TEXT, edad TEXT, periodo TEXT, tasa REAL)")
for sx, reg, age, per, v in rd("Employment/Tasa paro por CCAA por edad por sexo por trimestres 2020_2026.csv"):
    c.execute("INSERT INTO epa VALUES(?,?,?,?,?)", (sx, strip(reg), age, per, num(v)))

# IPC Table (Prices)
c.execute("CREATE TABLE ipc(grupo_codigo TEXT, grupo TEXT, periodo TEXT, indice REAL)")
for g, tp, per, v in rd("Prices/IPC - indice general por grupos - 2020_2026.csv"):
    m = re.match(r"^(\d\d) (.*)$", g)
    c.execute("INSERT INTO ipc VALUES(?,?,?,?)", (m.group(1) if m else "00", m.group(2) if m else g, per.replace("M", "-"), num(v)))

# PVPC Table (Energy)
c.execute("CREATE TABLE pvpc(territorio TEXT, mes TEXT, valor REAL)")
seen = set()
for id_, name, gid, geo, val, dt in csv.reader(open(B + "Energy/PVPC - 2020_2026.csv", encoding="utf-8"), delimiter=";"):
    if id_ == "id":
        continue
    k = (geo, dt[:7])
    if k in seen or dt[:7] == "2026-11":   # duplicates and the partial month are dropped
        continue
    seen.add(k)
    c.execute("INSERT INTO pvpc VALUES(?,?,?)", (geo, dt[:7], float(val)))
con.commit()
for t in ("ipv", "epa", "ipc", "pvpc"):
    print(t, c.execute(f"SELECT count(*) FROM {t}").fetchone()[0], "rows")
