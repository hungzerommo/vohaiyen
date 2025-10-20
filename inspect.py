from pathlib import Path
path = Path("index.html")
data = path.read_bytes()
needle = b"secretToggle.textContent = secretToggleDefaultText"
idx = data.find(needle)
print(idx)
print(data[idx:idx+120])
