// Muffin Math engine - batter ratio, stirring and scooping honesty.
// Every norm is a labeled kitchen norm; the app never judges doneness or safety.

function assertPositive(value, label) {
  if (!Number.isFinite(value) || value <= 0) {
    throw new Error(label + " must be above zero");
  }
}

function tenths(x) {
  return Math.floor(x * 10 + 0.5) / 10;
}

function fixed1(x) {
  return tenths(x).toFixed(1);
}

function wellWord(n) {
  return n === 1 ? "well" : "wells";
}

// Labeled norm: past half a cup of sugar per cup of flour, a muffin is a cupcake.
function batterTruth(flourCups, sugarCups) {
  assertPositive(flourCups, "the flour");
  assertPositive(sugarCups, "the sugar");
  const ratio = tenths(sugarCups / flourCups);
  let band;
  if (ratio < 0.3) {
    band = "lean and breakfast-leaning";
  } else if (ratio <= 0.5) {
    band = "a true muffin";
  } else {
    band = "cupcake territory wearing a muffin paper";
  }
  return fixed1(flourCups) + " cups of flour carrying " + fixed1(sugarCups) +
    " cups of sugar reads " + fixed1(ratio) + " cups of sugar per cup of flour, " + band + " honestly.";
}

// Labeled norm: muffin batter wants 10 to 12 strokes, just until combined.
function stirTruth(strokes) {
  assertPositive(strokes, "the stroke count");
  const one = strokes === 1;
  const s = one ? "stroke" : "strokes";
  let verdict;
  if (strokes <= 12) {
    verdict = (one ? "stops" : "stop") + " at just-combined, tender crumb";
  } else if (strokes <= 20) {
    verdict = (one ? "works" : "work") + " a little past just-combined, still tender";
  } else {
    verdict = (one ? "works" : "work") + " the batter to tunnels and peaky tops";
  }
  return strokes + " " + s + " " + verdict + " honestly.";
}

// Labeled norm: a standard muffin well takes a third of a cup of batter.
function scoopTruth(batterCups, wells) {
  assertPositive(batterCups, "the batter");
  assertPositive(wells, "the well count");
  const need = tenths(wells / 3);
  const diff = tenths(batterCups - need);
  let verdict;
  if (diff > 0) {
    verdict = "covers " + wells + " " + wellWord(wells) + " with " + fixed1(diff) + " cups to spare";
  } else if (diff === 0) {
    verdict = "covers " + wells + " " + wellWord(wells) + " exactly, not a spoonful left";
  } else {
    verdict = "comes up " + fixed1(-diff) + " cups short of " + wells + " " + wellWord(wells);
  }
  return fixed1(batterCups) + " cups of batter " + verdict + " honestly.";
}

if (typeof module !== "undefined") {
  module.exports = { batterTruth, stirTruth, scoopTruth, tenths, fixed1 };
}
