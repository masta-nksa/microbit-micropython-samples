"""Taster Version 2: Fuehrungshuelse mit Klemmmutter, Stoessel und Knopf.

Baut in Fusion fuenf Koerper (alle Masse in mm):
  Huelse_links / Huelse_rechts   Rohr mit Aussengewinde Tr12x2, unten flacher L-Fuss mit
                                 Taster-Aussparung (liegt unter dem Holz), oben Lippe
  Stoessel                       Zylinder, gleitet in der Huelse; Druckstift unten,
                                 Hals mit Gewinde M5x0.8 oben
  Knopf                          Drehknopf, sitzt auf dem Hals (Hub einstellbar)
  Klemmmutter                    Sechskantmutter Tr12x2, zieht die Huelse gegen das Holz

Funktionsprinzip: Huelse von unten durch das runde Holzloch stecken, Klemmmutter von oben
festziehen -> Huelse sitzt fest im Holz (jede Holzdicke bis holz_max). Der Stoessel gleitet
in der Huelse (lange Fuehrung) und wird von der Feder des Tasters gegen die Lippe gedrueckt.

Lokales Koordinatensystem der Huelse: Ursprung = Mitte des Holzlochs, Z = 0 = Oberkante des
Fusses = Holzunterseite, Z waechst nach aussen. Der Stoessel hat sein eigenes Z (0 = Unterkante
Koerper, Stift ragt nach -Z).

Das Skript loescht den Inhalt des aktiven Dokuments (wiederholbar) und exportiert am Ende die
STL-Dateien in den Ordner dieses Skripts. Huelse und Stoessel werden dabei kopfueber
gedreht exportiert (Druckrichtung: Lippe bzw. Hals auf dem Bett, keine Stuetzen).

Ausfuehren: in Fusion ein LEERES Design-Dokument oeffnen, Dienstprogramme > Add-Ins > Skripte >
Skript hinzufuegen > diese Datei > Ausfuehren. Parameter im Block P anpassen und neu laufen lassen.
"""
import math
import os
import struct
import adsk.core
import adsk.fusion

# ------------------------------------------------------------------ Parameter (mm)
P = dict(
    gew_d=12.0,         # Huelse: Aussengewinde Tr12x2 (Nenndurchmesser)
    pitch=2.0,
    loch_spiel=0.4,     # Holzloch = gew_d + loch_spiel  (12.4)
    huelse_l=15.0,      # Laenge der Huelse ab Holzunterseite (Holzdicke + Mutter + Reserve)
    holz_max=9.0,       # groesste Holzdicke (nur Kontrollrechnung)
    bohr_d=7.2,         # Fuehrungsbohrung
    lippe_t=2.0,        # Dicke der oberen Lippe
    lippe_d=5.4,        # Loch in der Lippe (Hals geht hindurch)
    taster=6.0,         # ANNAHME: Kantenlaenge der Tasterflaeche - nachmessen!
    tasche_zu=1.2,      # Luft rund um den Taster in der Fussaussparung (gesamt)
    fuss_t=0.8,         # Dicke des Fusses
    u_min=-3.0,         # Fuss: Ausdehnung zur Rahmenwand hin
    u_max=7.8,          # Fuss: Ausdehnung von der Wand weg (muss Loch-Radius + 1.5 ueberragen)
    y_halb=7.8,         # Fuss: halbe Laenge in Y
    d_taster=0.05,      # ANNAHME: Taster-Oberkante liegt so tief unter der Holzunterseite
    koerper_d=6.8,      # Stoessel: Fuehrungskoerper (0.2 Spiel je Seite in der Bohrung)
    hals_d=4.2,         # Stoessel: glatter Hals durch die Lippe (duenner als Kern der Knopfbohrung)
    gew_hals_d=5.0,     # Stoessel: Gewindehals M5x0.8 fuer den Knopf
    stift_d=3.0,        # Druckstift auf den Taster
    stift_l=0.9,        # Laenge des Druckstifts (haelt den Koerper 0.9 ueber dem Taster)
    luft_lippe=0.4,     # Ruhespiel Koerper <-> Lippe (Toleranz fuer hoeheren Taster, = Rattern)
    hals_gew_start=1.0, # Gewindebeginn ueber der Lippenoberkante (Ruhelage)
    hals_gew_l=4.7,     # Laenge des Gewindehalses (Knopf muss bis Luft 0 aufsitzen koennen)
    knopf_luft=0.7,     # Voreinstellung: Hub = Abstand Knopf-Unterseite <-> Huelsenoberkante
    knopf_d=14.0,
    knopf_dach=2.0,
    knopf_bohr_t=6.0,
    mutter_h=4.0,
    mutter_af=17.0,     # Schluesselweite
    gew_spiel=0.15,     # Druckspiel Tr12x2-Innengewinde (Versatz je Flanke)
    gew_spiel_m5=0.15,  # Druckspiel M5-Innengewinde im Knopf
    x_huelse_r=30.0, x_stoessel=60.0, x_knopf=80.0, x_mutter=105.0,   # Ablage in Fusion (Layout)
)
NEW = adsk.fusion.FeatureOperations.NewBodyFeatureOperation
JOIN = adsk.fusion.FeatureOperations.JoinFeatureOperation
CUT = adsk.fusion.FeatureOperations.CutFeatureOperation
TR = 'ISO Metric Trapezoidal Threads'
ISO = 'ISO Metric profile'


def loch_d():
    return P['gew_d'] + P['loch_spiel']


def koerper_l():
    """Laenge des Stoesselkoerpers: Ruhelage auf dem Taster, 'luft_lippe' unter der Lippe."""
    z_b = P['stift_l'] - P['d_taster']                       # Koerper-Unterkante in Ruhe (Huelsen-Z)
    return P['huelse_l'] - P['lippe_t'] - P['luft_lippe'] - z_b


def ruhe_z():
    """Huelsen-Z der Koerper-Unterkante in Ruhe (Stift liegt auf dem Taster)."""
    return P['stift_l'] - P['d_taster']


def hals_l1():
    """Laenge des glatten Halses zwischen Koerper und Gewindehals."""
    return (P['huelse_l'] + P['hals_gew_start']) - (ruhe_z() + koerper_l())


def mm(v):
    return v / 10.0


def vi(v):
    return adsk.core.ValueInput.createByString('%g mm' % v)


def pt(x, y, z=0.0):
    return adsk.core.Point3D.create(x / 10.0, y / 10.0, z / 10.0)


class Bau(object):
    def __init__(self, root, des):
        self.root = root
        self.des = des
        self._planes = {}

    def plane(self, z):
        key = round(z, 4)
        if key not in self._planes:
            if abs(z) < 1e-9:
                self._planes[key] = self.root.xYConstructionPlane
            else:
                pin = self.root.constructionPlanes.createInput()
                pin.setByOffset(self.root.xYConstructionPlane, vi(z))
                self._planes[key] = self.root.constructionPlanes.add(pin)
        return self._planes[key]

    def sketch(self, z):
        return self.root.sketches.add(self.plane(z))

    def poly(self, sk, pts):
        ls = sk.sketchCurves.sketchLines
        for i in range(len(pts)):
            a, b = pts[i], pts[(i + 1) % len(pts)]
            ls.addByTwoPoints(pt(*a), pt(*b))

    def circle(self, sk, x, y, d):
        sk.sketchCurves.sketchCircles.addByCenterRadius(pt(x, y), d / 20.0)

    def extrude(self, sk, dist, op, ziel=None, profile_index=None):
        if sk.profiles.count == 0:
            raise RuntimeError('Skizze %s ohne Profil' % sk.name)
        if profile_index is None:
            if sk.profiles.count != 1:
                raise RuntimeError('Skizze %s hat %d Profile (erwartet 1)' % (sk.name, sk.profiles.count))
            prof = sk.profiles.item(0)
        else:
            prof = sk.profiles.item(profile_index)
        ei = self.root.features.extrudeFeatures.createInput(prof, op)
        ei.setDistanceExtent(False, vi(dist))
        if ziel is not None:
            ei.participantBodies = [ziel]
        return self.root.features.extrudeFeatures.add(ei)

    def ring_index(self, sk):
        for i in range(sk.profiles.count):
            if sk.profiles.item(i).profileLoops.count == 2:
                return i
        raise RuntimeError('kein Ringprofil in ' + sk.name)

    def body(self, name):
        b = self.root.bRepBodies.itemByName(name)
        if b is None:
            raise RuntimeError('Koerper fehlt: ' + name)
        return b


def reset(des):
    tl = des.timeline
    guard = 0
    while tl.count > 0 and guard < 2000:
        guard += 1
        ent = tl.item(tl.count - 1).entity
        if ent is None:
            break
        try:
            ent.deleteMe()
        except Exception:
            break
    root = des.rootComponent
    for coll in (root.bRepBodies, root.sketches, root.constructionPlanes):
        for j in range(coll.count - 1, -1, -1):
            try:
                coll.item(j).deleteMe()
            except Exception:
                pass


def cyl_faces(b, r_mm, tol=0.03):
    out = []
    for f in b.faces:
        g = f.geometry
        if g.objectType == adsk.core.Cylinder.classType() and abs(g.radius * 10.0 - r_mm) < tol:
            out.append(f)
    return out


def gewinde(root, faces, innen, typ, desig, klasse):
    tf = root.features.threadFeatures
    ti = tf.createThreadInfo(innen, typ, desig, klasse)
    inp = tf.createInput(faces[0] if len(faces) == 1 else faces, ti)
    inp.isFullLength = True
    inp.isModeled = True
    return tf.add(inp)


def druckspiel(bau, name, max_breite, betrag):
    """Nicht-ebene Flaechen schmaler als max_breite (= Innengewinde) nach aussen versetzen."""
    b = bau.body(name)
    fl = []
    for f in b.faces:
        if f.geometry.objectType == adsk.core.Plane.classType():
            continue
        bb = f.boundingBox
        if (bb.maxPoint.x - bb.minPoint.x) * 10.0 < max_breite:
            fl.append(f)
    ofs = bau.root.features.offsetFacesFeatures
    ofs.add(ofs.createInput(fl, vi(-betrag)))


def huelse(bau, name, x_off, sx):
    """sx = +1: Fuss ragt nach +X (linker Taster, Rahmenwand bei -X); sx = -1: gespiegelt."""
    p = P
    root = bau.root
    L = p['huelse_l']
    n = p['taster'] / 2.0 + p['tasche_zu'] / 2.0

    def X(u):
        return x_off + sx * u

    # 1) Rohr von z = 0 bis L
    sk = bau.sketch(0)
    bau.circle(sk, x_off, 0, p['gew_d'])
    ex = bau.extrude(sk, L, NEW)
    ex.bodies.item(0).name = name

    # 2) Fuss (L-Form): 0.1 ueber z = 0 hinaus, damit er mit dem Rohr verschmilzt
    fuss = [(n, -p['y_halb']), (p['u_max'], -p['y_halb']), (p['u_max'], p['y_halb']),
            (p['u_min'], p['y_halb']), (p['u_min'], n), (n, n)]
    sk = bau.sketch(-p['fuss_t'])
    bau.poly(sk, [(X(u), y) for u, y in fuss])
    bau.extrude(sk, p['fuss_t'] + 0.1, JOIN, bau.body(name))

    # 3) Ueberstand des Fusses oberhalb z = 0 ausserhalb des Rohrs wegschneiden
    sk = bau.sketch(0)
    bau.circle(sk, x_off, 0, p['gew_d'])
    bau.circle(sk, x_off, 0, 60.0)
    bau.extrude(sk, 0.3, CUT, bau.body(name), profile_index=bau.ring_index(sk))

    # 4) Fuehrungsbohrung bis unter die Lippe, Lippenloch
    sk = bau.sketch(-0.5)
    bau.circle(sk, x_off, 0, p['bohr_d'])
    bau.extrude(sk, L - p['lippe_t'] + 0.5, CUT, bau.body(name))
    sk = bau.sketch(L - p['lippe_t'] - 0.1)
    bau.circle(sk, x_off, 0, p['lippe_d'])
    bau.extrude(sk, p['lippe_t'] + 0.2, CUT, bau.body(name))

    # 5) Aussengewinde
    fl = cyl_faces(bau.body(name), p['gew_d'] / 2.0)
    if not fl:
        raise RuntimeError('%s: keine Zylinderflaeche fuer das Aussengewinde' % name)
    gewinde(root, fl, False, TR, 'TR12x2', '7e')


def stoessel(bau, name, x_off):
    p = P
    root = bau.root
    Lb = koerper_l()
    l1 = hals_l1()

    sk = bau.sketch(0)
    bau.circle(sk, x_off, 0, p['koerper_d'])
    ex = bau.extrude(sk, Lb, NEW)
    ex.bodies.item(0).name = name

    sk = bau.sketch(-p['stift_l'])
    bau.circle(sk, x_off, 0, p['stift_d'])
    bau.extrude(sk, p['stift_l'] + 0.1, JOIN, bau.body(name))

    sk = bau.sketch(Lb - 0.1)
    bau.circle(sk, x_off, 0, p['hals_d'])
    bau.extrude(sk, l1 + 0.2, JOIN, bau.body(name))

    z_ts = Lb + l1
    sk = bau.sketch(z_ts)
    bau.circle(sk, x_off, 0, p['gew_hals_d'])
    bau.extrude(sk, p['hals_gew_l'], JOIN, bau.body(name))

    fl = cyl_faces(bau.body(name), p['gew_hals_d'] / 2.0, tol=0.02)
    if len(fl) != 1:
        raise RuntimeError('Stoessel: %d Gewindehals-Flaechen (erwartet 1)' % len(fl))
    gewinde(root, fl, False, ISO, 'M5x0.8', '6g')
    return z_ts + p['hals_gew_l']


def knopf(bau, name, x_off):
    p = P
    root = bau.root
    H = p['knopf_dach'] + p['knopf_bohr_t']
    d_bohr = 4.134                                # Kerndurchmesser M5x0.8 (Innengewinde)

    sk = bau.sketch(0)
    bau.circle(sk, x_off, 0, p['knopf_d'])
    ex = bau.extrude(sk, H, NEW)
    ex.bodies.item(0).name = name

    sk = bau.sketch(p['knopf_dach'])
    bau.circle(sk, x_off, 0, d_bohr)
    bau.extrude(sk, p['knopf_bohr_t'], CUT, bau.body(name))

    b = bau.body(name)
    bottom = None
    for f in b.faces:
        if f.geometry.objectType == adsk.core.Plane.classType():
            bb = f.boundingBox
            if abs(bb.maxPoint.z * 10.0) < 1e-3 and abs(bb.minPoint.z * 10.0) < 1e-3:
                bottom = f
    if bottom is not None:
        ci = root.features.chamferFeatures.createInput2()
        edges = adsk.core.ObjectCollection.create()
        for ed in bottom.edges:
            edges.add(ed)
        ci.chamferEdgeSets.addEqualDistanceChamferEdgeSet(edges, vi(0.8), True)
        root.features.chamferFeatures.add(ci)

    fl = cyl_faces(bau.body(name), d_bohr / 2.0, tol=0.02)
    if len(fl) != 1:
        raise RuntimeError('Knopf: %d Bohrungsflaechen (erwartet 1)' % len(fl))
    gewinde(root, fl, True, ISO, 'M5x0.8', '6H')
    druckspiel(bau, name, p['knopf_d'] - 2.0, p['gew_spiel_m5'])
    return H


def mutter(bau, name, x_off):
    p = P
    root = bau.root
    d_bohr = p['gew_d'] - p['pitch']
    r = p['mutter_af'] / math.sqrt(3.0)
    pts = [(x_off + r * math.cos(math.radians(60 * i)), r * math.sin(math.radians(60 * i))) for i in range(6)]
    sk = bau.sketch(0)
    bau.poly(sk, pts)
    ex = bau.extrude(sk, p['mutter_h'], NEW)
    ex.bodies.item(0).name = name

    sk = bau.sketch(0)
    bau.circle(sk, x_off, 0, d_bohr)
    bau.extrude(sk, p['mutter_h'], CUT, bau.body(name))

    fl = cyl_faces(bau.body(name), d_bohr / 2.0, tol=0.02)
    if len(fl) != 1:
        raise RuntimeError('Mutter: %d Bohrungsflaechen (erwartet 1)' % len(fl))
    gewinde(root, fl, True, TR, 'TR12x2', '7H')
    druckspiel(bau, name, p['mutter_af'] - 1.0, p['gew_spiel'])


def stl_kopfueber(pfad):
    """Binaere STL um 180 Grad um die X-Achse drehen und auf z = 0 setzen (Druckrichtung)."""
    with open(pfad, 'rb') as f:
        d = f.read()
    n = struct.unpack('<I', d[80:84])[0]
    tris = []
    zmin = None
    for i in range(n):
        v = list(struct.unpack('<12f', d[84 + i * 50:84 + i * 50 + 48]))
        w = [v[0], -v[1], -v[2]]
        for k in (3, 6, 9):
            w += [v[k], -v[k + 1], -v[k + 2]]
            zmin = w[-1] if zmin is None else min(zmin, w[-1])
        tris.append(w)
    out = bytearray(d[:80]) + struct.pack('<I', n)
    for w in tris:
        for k in (5, 8, 11):
            w[k] -= zmin
        out += struct.pack('<12f', *w) + b'\x00\x00'
    with open(pfad, 'wb') as f:
        f.write(bytes(out))


def run(_context):
    app = adsk.core.Application.get()
    des = adsk.fusion.Design.cast(app.activeProduct)
    if des is None:
        raise RuntimeError('Kein aktives Design')
    root = des.rootComponent
    reset(des)
    bau = Bau(root, des)
    huelse(bau, 'Huelse_links', 0.0, +1)
    huelse(bau, 'Huelse_rechts', P['x_huelse_r'], -1)
    z_top = stoessel(bau, 'Stoessel', P['x_stoessel'])
    H = knopf(bau, 'Knopf', P['x_knopf'])
    mutter(bau, 'Klemmmutter', P['x_mutter'])
    print('Loch im Holz: %.1f mm | Huelse %.1f lang | Stoesselkoerper %.2f | Hals %.2f | Stoessel gesamt %.2f | Knopf %.1f hoch'
          % (loch_d(), P['huelse_l'], koerper_l(), hals_l1(), z_top + P['stift_l'], H))
    for b in root.bRepBodies:
        bb = b.boundingBox
        print('  %-14s X %7.2f..%7.2f  Y %6.2f..%6.2f  Z %6.2f..%6.2f  V=%.1f mm3' % (
            b.name, bb.minPoint.x * 10, bb.maxPoint.x * 10, bb.minPoint.y * 10, bb.maxPoint.y * 10,
            bb.minPoint.z * 10, bb.maxPoint.z * 10, b.volume * 1000))
    erwartet = set(['Huelse_links', 'Huelse_rechts', 'Stoessel', 'Knopf', 'Klemmmutter'])
    streu = [b.name for b in root.bRepBodies if b.name not in erwartet]
    print('  Koerper:', root.bRepBodies.count, '| Streukoerper:', streu if streu else 'keine')
    if streu or root.bRepBodies.count != 5:
        return

    ordner = os.path.dirname(os.path.abspath(__file__))
    namen = {'Huelse_links': ('huelse_links.stl', True), 'Huelse_rechts': ('huelse_rechts.stl', True),
             'Stoessel': ('stoessel.stl', True), 'Knopf': ('knopf.stl', False),
             'Klemmmutter': ('klemmmutter.stl', False)}
    em = des.exportManager
    for b in root.bRepBodies:
        datei, drehen = namen[b.name]
        ziel = os.path.join(ordner, datei)
        opt = em.createSTLExportOptions(b, ziel)
        opt.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
        opt.isBinaryFormat = True
        em.execute(opt)
        if drehen:
            stl_kopfueber(ziel)
        print('  STL:', ziel, '(kopfueber)' if drehen else '')
