# #     names:  'L1' - 'L20'  for linear maps
# #             'D1' - 'D13'  for diverging maps
# #             'C1' - 'C11'  for cyclic maps
# #             'R1' - 'R4'   for rainbow maps
# #             'I1' - 'I3'   for isoluminant maps
# #
# #     maps for the red-green colour blind (Protanopia/Deuteranopia)
# #             'CBL1' - 'CBL4'
# #             'CBD1' - 'CBD2'
# #             'CBC1' - 'CBC2'
# #     maps for the blue-yellow colour blind (Tritanopia)
# #             'CBTL1' - 'CBTL4'
# #             'CBTD1'
# #             'CBTC1' - 'CBTC2'
# #
# # Keyword - argument options
# #           'N' - Number of values in the colour map. Defaults to 256.
# #       'shift' - Fraction of the colour map length N that the colour map is
# #                 to be cyclically rotated, may be negative.  (Should only be
# #                 applied to cyclic colour maps!). Defaults to 0.
# #     'reverse' - If set to 1/true reverses the colour map. Defaults to 0.


# def create_colorcet(matlab_file: str) -> None:
#     import json
#     from pathlib import Path

#     HERE = Path(__file__).parent

#     colormaps = {}
#     current_data = []
#     aliases = []

#     def _add(_name, _info):
#         tags = []
#         code_name = f"CET_{_name}"
#         if _name.startswith("CBT"):
#             tags = ["colorblind", "tritanopia"]
#             _name = _name[3:]
#         elif _name.startswith("CB"):
#             tags = ["colorblind", "protanopia", "deuteranopia"]
#             _name = _name[2:]
#         if _name.startswith("D"):
#             cat = "diverging"
#         elif _name.startswith(("R", "I")):
#             cat = "miscellaneous"
#         elif _name.startswith("C"):
#             cat = "cyclic"
#         elif _name.startswith("L"):
#             cat = "sequential"
#         colormaps[code_name] = {
#             "info": _info,
#             "data": f"cmap.data.colorcet.{code_name}:data",
#             "category": cat,
#         }
#         if tags:
#             colormaps[code_name]["tags"] = tags
#         # to be format by black
#         (HERE / f"{code_name}.py").write_text(f"data = {repr(current_data)}")
#         current_data.clear()
#         aliases.clear()

#     name = None
#     info = ""
#     in_map = False
#     t = Path(matlab_file).read_text()
#     for line in t.splitlines():
#         if line.startswith("map = ["):
#             in_map = True
#             line = line.split("map = [")[1]
#         if in_map:
#             if "];" in line:
#                 line = line.split("];")[0]
#                 in_map = False
#             current_data.append([float(x) for x in line.split()])
#             continue

#         if line.startswith("case"):
#             if name is not None:
#                 _add(name, info)
#             info = ""
#             _, name, *rest, _ = line.split("'")
#             aliases = [f"CET_{i}" for i in rest if i.strip()]
#         if line.startswith("descriptorname"):
#             aliases.append(line.split(" = '")[1].split("'")[0])
#         if line.startswith("description"):
#             info = line.split(" = '")[1].split("'")[0]

#     if name is not None:
#         _add(name, info)

#     record = {
#         "authors": ["Peter Kovesi"],
#         "source": "https://colorcet.com",
#         "license": "CC-BY-4.0",
#         "namespace": "colorcet",
#         "colormaps": colormaps,
#     }
#     (HERE / "record.json").write_text(json.dumps(record, indent=2))


# if __name__ == "__main__":
#     import sys

#     create_colorcet(sys.argv[1])
