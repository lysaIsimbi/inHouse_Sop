from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.dimensions import ColumnDimension


tasks = [
    {
        "number": 5,
        "task": "Fold cutlery into a napkin",
        "assignee": "Lysa",
        "description": (
            "Place a napkin flat, fold it into a secure pocket, arrange a knife, fork, "
            "and spoon together, and insert them into the pocket with the handles aligned. "
            "Straighten the napkin and place the completed setting in the finished area."
        ),
        "mode": "Tabletop",
        "arms": "Bimanual",
        "time": "2–4 min",
    },
    {
        "number": 15,
        "task": "Load dishwasher",
        "assignee": "Lysa",
        "description": (
            "Open the dishwasher, remove loose food residue from the dirty items, and load "
            "plates, bowls, cups, and cutlery into their designated racks or basket. Keep "
            "items separated, make sure the spray arms are not blocked, and close the door."
        ),
        "mode": "In situ",
        "arms": "Bimanual",
        "time": "2–4 min",
    },
    {
        "number": 16,
        "task": "Load washing machine with clothes sorted by color",
        "assignee": "Lysa",
        "description": (
            "Separate the clothes into light, dark, and colored groups. Select one group, "
            "open the washing-machine door, load the garments evenly without overfilling the "
            "drum, check that no fabric is trapped in the door, and close the door securely."
        ),
        "mode": "In situ",
        "arms": "Bimanual",
        "time": "3–5 min",
    },
    {
        "number": 17,
        "task": "Unload clothes from the washing machine",
        "assignee": "Lysa",
        "description": (
            "After the cycle is complete, place a laundry basket beside the machine, open the "
            "door, remove the garments one at a time, and place them in the basket. Check the "
            "drum and door seal for remaining items, then leave the machine tidy."
        ),
        "mode": "In situ",
        "arms": "Bimanual",
        "time": "2–4 min",
    },
    {
        "number": 23,
        "task": "Load supermarket shelves",
        "assignee": "Queen / Lysa (co-assigned)",
        "description": (
            "Move products from the stock container to the correct shelf sections, grouping "
            "matching items together. Place older stock at the front when applicable, turn "
            "labels forward, avoid overfilling, and align the products neatly."
        ),
        "mode": "In situ",
        "arms": "Bimanual",
        "time": "2–4 min",
    },
    {
        "number": 32,
        "task": "Brush and shelve shoes",
        "assignee": "Lysa",
        "description": (
            "Pick up each shoe, hold it securely, and brush dust and loose dirt from the upper, "
            "edges, and sole. Match each cleaned pair and place it neatly on the designated "
            "shelf with the toes facing forward."
        ),
        "mode": "Tabletop",
        "arms": "Bimanual",
        "time": "3–5 min",
    },
]


wb = Workbook()
ws = wb.active
ws.title = "Lysa - In situ"

headers = ["Number", "Task", "Assigned to", "Description", "Mode", "Arms", "Episode time"]
ws.append(headers)
for task in tasks:
    ws.append([
        task["number"], task["task"], task["assignee"], task["description"],
        task["mode"], task["arms"], task["time"],
    ])

navy = "203864"
light_blue = "D9EAF7"
white = "FFFFFF"
gray = "D9E1F2"
thin = Side(style="thin", color="A6A6A6")

for cell in ws[1]:
    cell.fill = PatternFill("solid", fgColor=navy)
    cell.font = Font(color=white, bold=True)
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)

for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    fill = PatternFill("solid", fgColor=light_blue if row[0].row % 2 == 0 else white)
    for cell in row:
        cell.fill = fill
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
        cell.alignment = Alignment(vertical="top", wrap_text=True)
    row[0].alignment = Alignment(horizontal="center", vertical="top")
    for idx in (4, 5, 6):
        row[idx].alignment = Alignment(horizontal="center", vertical="top", wrap_text=True)

widths = {"A": 9, "B": 33, "C": 24, "D": 85, "E": 14, "F": 12, "G": 17}
for col, width in widths.items():
    ws.column_dimensions[col].width = width

ws.row_dimensions[1].height = 28
for row_num in range(2, ws.max_row + 1):
    ws.row_dimensions[row_num].height = 88

ws.freeze_panes = "A2"
ws.auto_filter.ref = ws.dimensions
ws.sheet_view.showGridLines = False
ws.page_setup.orientation = "landscape"
ws.page_setup.paperSize = ws.PAPERSIZE_A3
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 1
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.oddFooter.center.text = "Extracted from: New tasks generated - Sorted Tasks.pdf"
ws.oddFooter.right.text = "Page &P of &N"
ws.print_title_rows = "1:1"
ws.sheet_properties.outlinePr.summaryBelow = True

wb.save("Lysa_in_situ_tasks_completed.xlsx")

