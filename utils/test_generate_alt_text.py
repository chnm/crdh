"""Self-check for the alt-text scanner. Run: python utils/test_generate_alt_text.py"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("gat", Path(__file__).with_name("generate-alt-text.py"))
gat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gat)

ok = "A long enough description of a map with cities and roads."
assert gat.weak_reason(ok, set()) is None
assert gat.weak_reason("alt-text", set()) == "missing"
assert gat.weak_reason("", set()) == "missing"
assert gat.weak_reason(ok, {ok.lower()}) == "duplicate"
assert gat.weak_reason("Fells Point in Baltimore", set()) == "short"
assert gat.weak_reason("Two newtwork graphs of the northeastern culsters", set()) == "typo"
assert gat.fix_typos("Two Newtwork graphs of the culsters") == "Two Network graphs of the clusters"
assert gat.new_alt({"reason": "typo", "alt": "Newtwork graph"}, "") == "Network graph"
assert gat.new_alt({"reason": "short", "alt": "Map of Paris"}, "Red dots mark bridges.") == "Map of Paris. Red dots mark bridges."
assert gat.new_alt({"reason": "missing", "alt": "alt-text"}, "A chart.") == "A chart."

html = '<img src="/x.png" alt="">\n<img\n  :src="s"\n  :alt="a"\n>\n<img src="/y.png" class="c">'
assert [gat.SRC_RE.search(m.group(0)).group(1) for m in gat.HTML_IMG_RE.finditer(html)] == ["/y.png"]

assert gat.clean('"A map of Paris"\n') == "A map of Paris."
assert gat.clean('Clipping warning "Lynch law is threatened."') == 'Clipping warning "Lynch law is threatened."'
assert gat.clean("**Alt text:** Two graphs") == "Two graphs."
print("ok")
