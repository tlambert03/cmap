"""Color palette from Tableau.

https://public.tableau.com/views/TableauColors/ColorPaletteswithRGBValues
# TODO: more refs
"""
# fmt: off

__license__ = "UNKNOWN"

# this is the same as Vega's "category10"
Tableau10 = [
    ( 31, 119, 180),    # 1F77B4
    (255, 127,  14),    # FF7F0E
    ( 44, 160,  44),    # 2CA02C
    (214,  39,  40),    # D62728
    (148, 103, 189),    # 9467BD
    (140,  86,  75),    # 8C564B
    (227, 119, 194),    # E377C2
    (127, 127, 127),    # 7F7F7F
    (188, 189,  34),    # BCBD22
    ( 23, 190, 207),    # 17BECF
]

Tableau10_Light = [
    (174, 199, 232),    # AEC7E8
    (255, 187, 120),    # FFBB78
    (152, 223, 138),    # 98DF8A
    (255, 152, 150),    # FF9896
    (197, 176, 213),    # C5B0D5
    (196, 156, 148),    # C49C94
    (247, 182, 210),    # F7B6D2
    (199, 199, 199),    # C7C7C7
    (219, 219, 141),    # DBDB8D
    (158, 218, 229),    # 9EDAE5
]


Tableau10_Medium = [
    (114, 158, 206),    # 729ECE
    (255, 158,  74),    # FF9E4A
    (103, 191,  92),    # 67BF5C
    (237, 102,  93),    # ED665D
    (173, 139, 201),    # AD8BC9
    (168, 120, 110),    # A8786E
    (237, 151, 202),    # ED97CA
    (162, 162, 162),    # A2A2A2
    (205, 204,  93),    # CDCC5D
    (109, 204, 218),    # 6DCCDA
]

ColorBlind10 = [
    (  0, 107, 164),    # 006BA4
    (255, 128,   0),    # FF8000
    (171, 171, 171),    # ABABAB
    ( 89,  89,  89),    # 595959
    ( 95, 158, 209),    # 5F9ED1
    (200,  82,   0),    # C85200
    (137, 137, 137),    # 898989
    (162, 200, 236),    # A2C8EC
    (255, 188, 121),    # FFBC79
    (207, 207, 207),    # CFCFCF
]


# this is the same as Vega's "category20"
Tableau20 = [
    ( 31, 119, 180),    # 1F77B4
    (174, 199, 232),    # AEC7E8
    (255, 127,  14),    # FF7F0E
    (255, 187, 120),    # FFBB78
    ( 44, 160,  44),    # 2CA02C
    (152, 223, 138),    # 98DF8A
    (214,  39,  40),    # D62728
    (255, 152, 150),    # FF9896
    (148, 103, 189),    # 9467BD
    (197, 176, 213),    # C5B0D5
    (140,  86,  75),    # 8C564B
    (196, 156, 148),    # C49C94
    (227, 119, 194),    # E377C2
    (247, 182, 210),    # F7B6D2
    (127, 127, 127),    # 7F7F7F
    (199, 199, 199),    # C7C7C7
    (188, 189,  34),    # BCBD22
    (219, 219, 141),    # DBDB8D
    ( 23, 190, 207),    # 17BECF
    (158, 218, 229),    # 9EDAE5
]

# these seem to come from Vega's "category20b" and "category20c"
# but I haven't found them in the Tableau docs

Tableau20b = [
    (57, 59, 121),      # 393B79
    (82, 84, 163),      # 5254A3
    (107, 110, 207),    # 6B6ECF
    (156, 158, 222),    # 9C9EDE
    (99, 121, 57),      # 637939
    (140, 162, 82),     # 8CA252
    (181, 207, 107),    # B5CF6B
    (206, 219, 156),    # CEDB9C
    (140, 109, 49),     # 8C6D31
    (189, 158, 57),     # BD9E39
    (231, 186, 82),     # E7BA52
    (231, 203, 148),    # E7CB94
    (132, 60, 57),      # 843C39
    (173, 73, 74),      # AD494A
    (214, 97, 107),     # D6616B
    (231, 150, 156),    # E7969C
    (123, 65, 115),     # 7B4173
    (165, 81, 148),     # A55194
    (206, 109, 189),    # CE6DBD
    (222, 158, 214)     # DE9ED6
]

Tableau20c = [
    (49, 130, 189),     # 3182BD
    (107, 174, 214),    # 6BAED6
    (158, 202, 225),    # 9ECAE1
    (198, 219, 239),    # C6DBEF
    (230, 85, 13),      # E6550D
    (253, 141, 60),     # FD8D3C
    (253, 174, 107),    # FDAE6B
    (253, 208, 162),    # FDD0A2
    (49, 163, 84),      # 31A354
    (116, 196, 118),    # 74C476
    (161, 217, 155),    # A1D99B
    (199, 233, 192),    # C7E9C0
    (117, 107, 177),    # 756BB1
    (158, 154, 200),    # 9E9AC8
    (188, 189, 220),    # BCBDDC
    (218, 218, 235),    # DADAEB
    (99, 99, 99),       # 636363
    (150, 150, 150),    # 969696
    (189, 189, 189),    # BDBDBD
    (217, 217, 217)     # D9D9D9
]

Traffic_Light = [
    (177,   3,  24),    # B10318
    (219, 161,  58),    # DBA13A
    ( 48, 147,  67),    # 309343
    (216,  37,  38),    # D82526
    (255, 193,  86),    # FFC156
    (105, 183, 100),    # 69B764
    (242, 108, 100),    # F26C64
    (255, 221, 113),    # FFDD71
    (159, 205, 153),    # 9FCD99
]
