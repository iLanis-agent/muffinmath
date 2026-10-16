import json, math

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def well_word(n):
    return "well" if n == 1 else "wells"

def batter_truth(flour, sugar):
    if flour <= 0:
        raise ValueError("the flour must be above zero")
    if sugar <= 0:
        raise ValueError("the sugar must be above zero")
    ratio = tenths(sugar / flour)
    if ratio < 0.3:
        band = "lean and breakfast-leaning"
    elif ratio <= 0.5:
        band = "a true muffin"
    else:
        band = "cupcake territory wearing a muffin paper"
    return (f"{fixed1(flour)} cups of flour carrying {fixed1(sugar)} cups of sugar "
            f"reads {fixed1(ratio)} cups of sugar per cup of flour, {band} honestly.")

def stir_truth(strokes):
    if strokes <= 0:
        raise ValueError("the stroke count must be above zero")
    one = strokes == 1
    s = "stroke" if one else "strokes"
    if strokes <= 12:
        verdict = ("stops" if one else "stop") + " at just-combined, tender crumb"
    elif strokes <= 20:
        verdict = ("works" if one else "work") + " a little past just-combined, still tender"
    else:
        verdict = ("works" if one else "work") + " the batter to tunnels and peaky tops"
    return f"{strokes} {s} {verdict} honestly."

def scoop_truth(batter, wells):
    if batter <= 0:
        raise ValueError("the batter must be above zero")
    if wells <= 0:
        raise ValueError("the well count must be above zero")
    need = tenths(wells / 3)
    diff = tenths(batter - need)
    if diff > 0:
        verdict = f"covers {wells} {well_word(wells)} with {fixed1(diff)} cups to spare"
    elif diff == 0:
        verdict = f"covers {wells} {well_word(wells)} exactly, not a spoonful left"
    else:
        verdict = f"comes up {fixed1(-diff)} cups short of {wells} {well_word(wells)}"
    return f"{fixed1(batter)} cups of batter {verdict} honestly."

cases = []

def add(fn_name, args):
    try:
        fn = {"batterTruth": batter_truth, "stirTruth": stir_truth, "scoopTruth": scoop_truth}[fn_name]
        cases.append({"fn": fn_name, "args": args, "result": fn(*args)})
    except ValueError as e:
        cases.append({"fn": fn_name, "args": args, "error": str(e)})

# batterTruth
add("batterTruth", [2, 0.75])    # 0.4 true muffin
add("batterTruth", [2, 0.5])     # 0.25 -> 0.3 rounded -> true muffin (edge, judges rounded)
add("batterTruth", [2, 0.4])     # 0.2 lean
add("batterTruth", [2, 1.25])    # 0.625 -> 0.6 cupcake
add("batterTruth", [1, 0.5])     # 0.5 edge -> true muffin
add("batterTruth", [3, 1.8])     # 0.6 cupcake
add("batterTruth", [0, 1])       # error
add("batterTruth", [2, 0])       # error
# stirTruth
add("stirTruth", [12])           # just-combined
add("stirTruth", [1])            # singular stroke
add("stirTruth", [16])           # a little past
add("stirTruth", [20])           # edge -> a little past
add("stirTruth", [24])           # tunnels
add("stirTruth", [0])            # error
# scoopTruth
add("scoopTruth", [4, 12])       # exact
add("scoopTruth", [4.5, 12])     # 0.5 spare
add("scoopTruth", [3.5, 12])     # 0.5 short
add("scoopTruth", [1, 1])        # singular well, 0.7 spare
add("scoopTruth", [0.3, 1])      # exact single
add("scoopTruth", [2, 8])        # 0.7 short
add("scoopTruth", [0, 12])       # error
add("scoopTruth", [4, 0])        # error

with open("expected.json", "w") as f:
    json.dump(cases, f, indent=2)
    f.write("\n")
print(f"{len(cases)} cases written")
for c in cases:
    print(c["fn"], c["args"], "->", c["result"] if "result" in c else "ERR: " + c["error"])
