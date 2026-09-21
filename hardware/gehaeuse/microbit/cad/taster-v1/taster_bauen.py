"""Hoehenverstellbarer Taster fuer micro:bit-Taster A/B unter einem Holzdeckel.

Baut in Fusion vier Koerper (alle Masse in mm):
  Stoessel_links   Fuss unter dem Holz + Druckzapfen + Gewindebolzen Tr10x2 (fuehrt im runden Loch)
  Stoessel_rechts  gespiegelte Variante (Rahmenwand liegt auf der anderen Seite)
  Kontermutter     Sechskantmutter Tr10x2, dient als einstellbarer Anschlag ueber dem Holz
  Kappe            Drehknopf mit Sackloch-Innengewinde, Druckrichtung: Dach auf dem Bett

Lokales Koordinatensystem des Stoessels: Ursprung = Mitte des Holzausschnitts, Z = 0 an der
Oberkante des Fusses, Z waechst nach aussen (durch das Holz hindurch zur Kappe).

Skript ist wiederholbar: raeumt zuerst die Geometrie des aktiven Dokuments ab und exportiert
am Ende die STL-Dateien in den Ordner, in dem dieses Skript liegt.

Ausfuehren: in Fusion ein LEERES Design-Dokument oeffnen (das Skript loescht dessen Inhalt!),
dann Dienstprogramme > Add-Ins > Skripte > Skript hinzufuegen > diese Datei > Ausfuehren.
Parameter aendern = Werte im Block P unten anpassen und das Skript neu laufen lassen.
"""
import math
import os
import adsk.core
import adsk.fusion

# ------------------------------------------------------------------ Parameter (mm)
P = dict(
    loch_d=10.4,        # Holz: RUNDER Fuehrungsausschnitt, Durchmesser (Bolzen Ø10 hat 0.2 je Seite Spiel)
    fuehr_r=4.9,        # Radius der Haltearme im Loch (Loch-Radius minus 0.3)
    taster=6.0,         # ANNAHME: Kantenlaenge der Tasterflaeche (X und Y) - nachmessen!
    tasche_zu=1.2,      # Luft rund um den Taster in der Fussaussparung (gesamt)
    fuss_t=0.8,         # Dicke des Fusses unter dem Holz
    u_min=-3.0,         # Fuss: Ausdehnung zur Rahmenwand hin (u = Koordinate zur Innenseite)
    u_max=6.5,          # Fuss: Ausdehnung von der Wand weg (ueberlappt das Loch)
    y_halb=6.2,         # Fuss: halbe Laenge in Y (ueberlappt das Loch)
    dach=1.0,           # Fussoberkante -> Unterseite Bolzen (Dach ueber dem Taster)
    zapfen_d=3.0,       # Druckzapfen unter dem Dach: drueckt auf die Tastermitte
    zapfen_l=0.5,       # Laenge des Druckzapfens (haelt das Dach 0.5 ueber dem Taster)
    d_taster=0.05,      # ANNAHME: Taster-Oberkante liegt so tief unter der Holzunterseite
    stab_d=10.0,        # Gewindebolzen Nenndurchmesser (Tr10x2)
    pitch=2.0,          # Steigung = Leerweg bei einer Umdrehung zurueck
    holz_min=4.0,       # kleinste Holzdicke, fuer die der Bolzen ausgelegt ist
    holz_max=9.0,       # groesste Holzdicke
    mutter_h=3.0,       # Hoehe der Kontermutter
    mutter_af=15.0,     # Schluesselweite der Kontermutter
    eingriff_min=4.0,   # kleinste Gewindeeingriffslaenge der Kappe bei dickstem Holz
    pilot_d=8.0,        # glatter Fuehrungszapfen am Bolzenende (statt Fase)
    pilot_h=0.8,
    kappe_d=16.0,       # Aussendurchmesser der Kappe
    kappe_dach=1.5,     # Dicke des Kappendachs
    gew_spiel=0.15,     # Versatz der Innengewindeflanken (Druckspiel)
    x_rechts=25.0,      # Ablageplatz der rechten Variante in Fusion (nur Layout)
    x_kappe=50.0,       # Ablageplatz der Kappe (nur Layout)
    x_mutter=75.0,      # Ablageplatz der Kontermutter (nur Layout)
)
GEW = 'TR10x2'
NEW = adsk.fusion.FeatureOperations.NewBodyFeatureOperation
JOIN = adsk.fusion.FeatureOperations.JoinFeatureOperation
CUT = adsk.fusion.FeatureOperations.CutFeatureOperation


def einsink():
    """Wie tief der Stoessel in Ruhe (auf dem Taster liegend) unter der Holzunterseite sitzt."""
    return P['d_taster'] + P['dach'] - P['zapfen_l']


def kappe_z(t):
    """Unterkante der Kappe im Stoessel-Koordinatensystem bei Holzdicke t
    (Kappe liegt auf der Kontermutter, diese ist um 'pitch' vom Holz abgeruckt)."""
    return t + einsink() + P['pitch'] + P['mutter_h']


def mutter_z(t):
    return t + einsink() + P['pitch']


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


def gewinde(root, face, innen, klasse):
    tf = root.features.threadFeatures
    ti = tf.createThreadInfo(innen, 'ISO Metric Trapezoidal Threads', GEW, klasse)
    inp = tf.createInput(face, ti)
    inp.isFullLength = True
    inp.isModeled = True
    return tf.add(inp)


def druckspiel(bau, name, max_breite):
    """Gewindeflaechen der Innenbohrung (alles Nicht-Ebene schmaler als max_breite) nach aussen versetzen."""
    b = bau.body(name)
    fl = []
    for f in b.faces:
        if f.geometry.objectType == adsk.core.Plane.classType():
            continue
        bb = f.boundingBox
        if (bb.maxPoint.x - bb.minPoint.x) * 10.0 < max_breite:
            fl.append(f)
    ofs = bau.root.features.offsetFacesFeatures
    ofs.add(ofs.createInput(fl, vi(-P['gew_spiel'])))
    return len(fl)


def stoessel(bau, name, x_off, sx):
    """sx = +1: Fuss ragt nach +X (linker Taster, Rahmenwand liegt bei -X);
       sx = -1: gespiegelt (rechter Taster)."""
    p = P
    root = bau.root
    n = p['taster'] / 2.0 + p['tasche_zu'] / 2.0  # halbe Aussparung
    e = p['dach']
    r_f = p['fuehr_r']

    def X(u):
        return x_off + sx * u

    # 1) Fuss (L-Form) unter dem Holz; Aussparung fuer den Taster: u < n und y < n
    fuss = [(n, -p['y_halb']), (p['u_max'], -p['y_halb']), (p['u_max'], p['y_halb']),
            (p['u_min'], p['y_halb']), (p['u_min'], n), (n, n)]
    sk = bau.sketch(-p['fuss_t'])
    bau.poly(sk, [(X(u), y) for u, y in fuss])
    ex = bau.extrude(sk, p['fuss_t'], NEW)
    ex.bodies.item(0).name = name

    # 2) Haltearme: L-Form ueber dem Fuss (bis e + 0.1), spaeter auf den Kreis im Loch gekuerzt
    arm = [(n, -6.0), (6.0, -6.0), (6.0, 6.0), (p['u_min'], 6.0), (p['u_min'], n), (n, n)]
    sk = bau.sketch(-0.1)
    bau.poly(sk, [(X(u), y) for u, y in arm])
    bau.extrude(sk, e + 0.2, JOIN, bau.body(name))

    # 3) alles ueber dem Fuss (z > 0) ausserhalb r_f wegschneiden -> Arme passen ins runde Loch
    sk = bau.sketch(0.0)
    bau.circle(sk, x_off, 0, 2 * r_f)
    bau.circle(sk, x_off, 0, 30.0)
    ring = None
    for i in range(sk.profiles.count):
        if sk.profiles.item(i).profileLoops.count == 2:
            ring = i
    bau.extrude(sk, e + 0.1, CUT, bau.body(name), profile_index=ring)

    # 4) Gewindebolzen: Dach bei z = e, Gewinde bis z_t, dann glatter Fuehrungszapfen bis z_s
    z_t = kappe_z(p['holz_max']) + p['eingriff_min']
    z_s = z_t + p['pilot_h']
    sk = bau.sketch(e)
    bau.circle(sk, x_off, 0, p['stab_d'])
    bau.extrude(sk, z_t - e, JOIN, bau.body(name))
    sk = bau.sketch(z_t - 0.1)
    bau.circle(sk, x_off, 0, p['pilot_d'])
    bau.extrude(sk, p['pilot_h'] + 0.1, JOIN, bau.body(name))

    # 5) Druckzapfen unter dem Dach (drueckt auf die Tastermitte)
    sk = bau.sketch(e - p['zapfen_l'])
    bau.circle(sk, x_off, 0, p['zapfen_d'])
    bau.extrude(sk, p['zapfen_l'] + 0.1, JOIN, bau.body(name))

    # 6) Gewinde nur am Bolzen
    fl = cyl_faces(bau.body(name), p['stab_d'] / 2.0)
    if len(fl) != 1:
        raise RuntimeError('%s: %d Zylinderflaechen fuer Gewinde (erwartet 1)' % (name, len(fl)))
    gewinde(root, fl[0], False, '7e')
    return z_s


def kappe(bau, name, x_off, z_s):
    p = P
    root = bau.root
    bohr_t = z_s - kappe_z(p['holz_min'])       # Tiefe der Sacklochbohrung
    H = bohr_t + p['kappe_dach']
    d_bohr = p['stab_d'] - p['pitch']            # Kern-Durchmesser Innengewinde

    sk = bau.sketch(0)
    bau.circle(sk, x_off, 0, p['kappe_d'])
    ex = bau.extrude(sk, H, NEW)
    ex.bodies.item(0).name = name

    sk = bau.sketch(p['kappe_dach'])
    bau.circle(sk, x_off, 0, d_bohr)
    bau.extrude(sk, bohr_t, CUT, bau.body(name))

    # Fase am Bettrand (Elefantenfuss) - aussen unten
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
        raise RuntimeError('Kappe: %d Bohrungsflaechen (erwartet 1)' % len(fl))
    gewinde(root, fl[0], True, '7H')
    druckspiel(bau, name, p['kappe_d'] - 2.0)
    return H


def mutter(bau, name, x_off):
    p = P
    root = bau.root
    d_bohr = p['stab_d'] - p['pitch']
    r = p['mutter_af'] / math.sqrt(3.0)          # Eckenradius des Sechskants
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
    gewinde(root, fl[0], True, '7H')
    druckspiel(bau, name, p['mutter_af'] - 1.0)


def run(_context):
    app = adsk.core.Application.get()
    des = adsk.fusion.Design.cast(app.activeProduct)
    if des is None:
        raise RuntimeError('Kein aktives Design')
    root = des.rootComponent
    reset(des)
    bau = Bau(root, des)
    z_s = stoessel(bau, 'Stoessel_links', 0.0, +1)
    stoessel(bau, 'Stoessel_rechts', P['x_rechts'], -1)
    H = kappe(bau, 'Kappe', P['x_kappe'], z_s)
    mutter(bau, 'Kontermutter', P['x_mutter'])
    print('Bolzen-Oberkante z_s = %.2f, Kappenhoehe = %.2f, Einsinken in Ruhe = %.2f' % (z_s, H, einsink()))
    for b in root.bRepBodies:
        bb = b.boundingBox
        print('  %-16s X %7.2f..%7.2f  Y %6.2f..%6.2f  Z %6.2f..%6.2f  V=%.1f mm3' % (
            b.name, bb.minPoint.x * 10, bb.maxPoint.x * 10, bb.minPoint.y * 10, bb.maxPoint.y * 10,
            bb.minPoint.z * 10, bb.maxPoint.z * 10, b.volume * 1000))
    erwartet = set(['Stoessel_links', 'Stoessel_rechts', 'Kappe', 'Kontermutter'])
    streu = [b.name for b in root.bRepBodies if b.name not in erwartet]
    print('  Koerper:', root.bRepBodies.count, '| Streukoerper:', streu if streu else 'keine')
    if streu or root.bRepBodies.count != 4:
        return

    ordner = os.path.dirname(os.path.abspath(__file__))
    namen = {'Stoessel_links': 'stoessel_links.stl', 'Stoessel_rechts': 'stoessel_rechts.stl',
             'Kappe': 'kappe.stl', 'Kontermutter': 'kontermutter.stl'}
    em = des.exportManager
    for b in root.bRepBodies:
        ziel = os.path.join(ordner, namen[b.name])
        opt = em.createSTLExportOptions(b, ziel)
        opt.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
        opt.isBinaryFormat = True
        em.execute(opt)
        print('  STL:', ziel)
