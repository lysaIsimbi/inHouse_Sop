# Unpack a Student Bag SOP (1x Episode: 1 Bag)

Unpack **one student bag** in one recorded episode using the two-arm tabletop robot. The bag starts
closed and loaded, lying flat on its back at the back center of the table. Inside it are four items: a
book, a lunchbox, a pencil case, and a water bottle.

The order never changes: open the bag, take the four items out one at a time and lay each one out on
the table, then set the empty bag beside the items.

The right gripper takes every item out and lays it out. The left gripper holds the bag open while the
items come out, then moves the empty bag. Neither arm reaches across the table.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the full tabletop: the bag at the back center, the layout row across
   the front middle and front right, and the bag spot at the front-left.
3. The whole top face of the bag is in frame, with the main zip visible from end to end.
4. Both arms are at home with grippers open.
5. The table is clear except for the bag and the items inside it, and robot hardware.
6. The left arm can reach the left half of the bag, the top handle, and the bag spot. The right arm can
   reach the right half of the bag, the inside of the bag, and the whole layout row. Neither arm
   stretches out to reach any of these.

### Materials checklist

1. Lay one student bag flat at the back center of the table, back panel down and front panel up. The
   top of the bag, with its top handle, points toward the back edge. The base points toward the front
   edge.
2. Load the main compartment, from the bottom up:
   - the **book** lies flat on the back panel, cover up;
   - the **lunchbox** lies flat on the book, lid up, toward the base;
   - the **pencil case** lies flat on the book, zip up, toward the top, beside the lunchbox;
   - the capped **water bottle** lies on its side along the right side of the compartment, cap toward
     the top.
3. Zip the main zip shut. The pull sits at its **closed end**, at the left side of the base.
4. Check that the zip has a loop tab big enough for either gripper to pinch.
5. The front of the table is empty: no tape, no labels, nothing on the layout row or the bag spot.

### Workspace layout

- **Bag start spot:** the back center of the table. The bag lies here while it is opened and emptied.
- **Layout row:** a row across the front of the table, starting at the front middle and going to the
  right. The items are laid out here in the order they come out.
- **Bag spot:** the front-left of the table, just left of the first item in the layout row.

### Arm assignments

- **Left gripper:** starts the zip, holds the bag open while the items come out, and moves the empty
  bag to the bag spot.
- **Right gripper:** finishes the zip, takes every item out of the bag, and lays each one out on the
  layout row.

## Vocabulary

- **Main compartment:** the big compartment under the main zip. All four items are in it.
- **Track:** the line of teeth the zip pull runs along. The main track runs up the left side of the
  bag, across the top, and down the right side. It has a **closed end** at the left of the base, where
  the pull sits when the bag is shut, and an **open end** at the right of the base, where it sits when
  the bag is open.
- **Loop tab:** the fabric loop on the zip pull. It is the only part of the zip a gripper pinches.
- **Draw:** a gripper pinches the loop tab and pulls it along the track in one smooth motion.
- **Hand-over point:** the middle of the top of the track. The draw passes from the left gripper to the
  right gripper here.
- **Hand over:** passing the loop tab from one gripper to the other. The giving gripper holds still for
  half a second, the other gripper pinches the tab, and only then does the giving gripper let go.
- **Anchor:** a closed gripper pressed down on the bag, away from the track, so the bag stays flat and
  still. An anchor does not move while the other gripper works.
- **Front panel:** the top face of the bag while it lies on its back. Once the zip is fully open, it is
  joined to the bag only at the base.
- **Hold open:** the left gripper pinches the top-left corner of the front panel, lifts it up and toward
  the front edge until the inside of the bag shows, and keeps it there without moving.
- **Bottom-right corner:** the corner of the book nearest the front-right of the table. It is the only
  part of the book the right gripper takes.
- **Lay out:** the right gripper lowers an item flat onto the table until it rests, then lets go. Each
  item goes to the right of the item before it, with a clear gap, and no item touches another.
- **Top handle:** the fabric loop sewn to the top of the bag.
- **Settled:** the item stays still when the gripper lets go, with nothing rocking, sliding, or rolling.

## Steps

Run Steps 1 to 7 once for one bag, then end the episode with Step 8. Every item is lifted straight up
until it is clear of the bag, carried flat, and lowered until it rests before the gripper lets go. One
item moves at a time. The items come out top first: pencil case, lunchbox, bottle, book.

### Step 1: Open the bag

**Goal:** the zip pull sits at the open end and the track is open along its whole length.

#### 1.1 Draw to the hand-over point

- With the **right gripper** closed, anchor the bag on its right side, away from the track.
- With the **left gripper**, pinch the loop tab at the closed end, at the left of the base.
- With the **left gripper**, draw the tab up the left side to the hand-over point, then hold still for
  half a second.

#### 1.2 Finish the draw

- With the **right gripper**, lift off the anchor and pinch the tab. Then let go with the **left
  gripper**.
- With the **left gripper** closed, anchor the bag on its left side, away from the track.
- With the **right gripper**, draw the tab across the top and down the right side until it reaches the
  open end and stops. Let go and lift away.
- Lift the **left gripper** off the bag.

**Check:** the pull sits at the open end and the track is open from end to end. If the pull stopped
short, take the loop tab again with the right gripper and draw it the rest of the way.

### Step 2: Hold the bag open

**Goal:** the inside of the bag shows and all four items can be reached.

- With the **left gripper**, pinch the top-left corner of the front panel.
- With the **left gripper**, lift it up and toward the front edge until the inside of the bag shows.
- With the **left gripper**, keep this hold, without moving, until the book is out in Step 6.

**Check:** the pencil case, the lunchbox, the bottle, and the book all show. If the front panel falls
back, take the corner again with the left gripper and lift it open again.

### Step 3: Take out the pencil case

**Goal:** the pencil case lies flat at the front middle, zip up. It is the first item in the layout
row.

- With the **left gripper**, keep holding the bag open.
- With the **right gripper**, pinch the pencil case across its two long sides.
- With the **right gripper**, lift it straight up until it is clear of the bag.
- With the **right gripper**, carry it flat to the front middle of the table and lay it out zip up.

**Check:** the pencil case lies flat and settled at the front middle. If it lies crooked or on its
side, lift it with the right gripper and lay it out again.

### Step 4: Take out the lunchbox

**Goal:** the lunchbox lies flat to the right of the pencil case, lid up.

- With the **left gripper**, keep holding the bag open.
- With the **right gripper**, pinch the lunchbox across its two short sides.
- With the **right gripper**, lift it straight up off the book until it is clear of the bag.
- With the **right gripper**, carry it lid up and flat, and lay it out to the right of the pencil case.

**Check:** the lunchbox lies flat, lid up, and settled, with a clear gap to the pencil case, and the lid
is still shut. If it touches the pencil case, lift it with the right gripper and lay it out again.

### Step 5: Take out the bottle

**Goal:** the bottle lies on its side to the right of the lunchbox.

- With the **left gripper**, keep holding the bag open.
- With the **right gripper**, pinch the bottle around its body below the cap.
- With the **right gripper**, lift it straight up until it is clear of the bag.
- With the **right gripper**, carry it on its side and lay it out to the right of the lunchbox, cap
  toward the back edge.

**Check:** the bottle lies settled on its side with a clear gap to the lunchbox. If it rolls into the
lunchbox or away from the row, lift it with the right gripper and lay it out again.

### Step 6: Take out the book

**Goal:** the book lies flat to the right of the bottle, cover up, and the bag is empty.

- With the **left gripper**, keep holding the bag open.
- With the **right gripper**, pinch the book at its bottom-right corner, through the full thickness of
  the book.
- With the **right gripper**, lift it straight up until it is clear of the bag.
- With the **right gripper**, carry it flat and cover up, and lay it out to the right of the bottle.
- With the **left gripper**, let go of the front panel and lift away.

**Check:** the book lies flat and settled with a clear gap to the bottle, and nothing is left in the
bag. If the book touches the bottle, lift it with the right gripper and lay it out again.

### Step 7: Set the empty bag beside the items

**Goal:** the empty bag lies flat on the bag spot, just left of the pencil case.

- With the **left gripper**, pinch the top handle at its middle.
- With the **left gripper**, lift straight up until the whole bag hangs clear of the table.
- With the **left gripper**, carry the bag to the bag spot at the front-left.
- With the **left gripper**, lower until the base touches the table. Keep lowering while moving toward
  the back edge, so the bag lies down on its back panel with its top toward the back edge.
- With the **left gripper**, let go and lift away. The **right gripper** waits clear of the items.

**Check:** the bag lies flat on its back panel at the bag spot, beside the pencil case without touching
it, and no item has moved. If the bag lies on an item or on its front panel, lift it again by the top
handle with the left gripper and set it down again.

### Step 8: End the episode

**Goal:** recording ends with four items laid out in a row and the empty bag beside them.

- Look once across the table: four items in the row, each flat and apart, and the bag beside the
  pencil case.
- With **both grippers** open, return both arms home.
- Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

1. Lay the bag flat at the back center, back panel down, top toward the back edge.
2. Put the book in flat on the back panel, cover up.
3. Put the lunchbox on the book toward the base, lid up, and the pencil case on the book toward the
   top, zip up.
4. Lay the bottle on its side along the right side of the compartment, cap toward the top.
5. Draw the zip to its closed end at the left of the base.
6. Check that the layout row and the bag spot are empty.
7. Check that the loop tab is attached and the zip runs freely. Replace anything torn or leaking.
8. Run both Setup checklists before the next episode.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

- the **start timestamp** in the video;
- the **violation name** from the list below; and
- the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an
annotation label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain multiple violations; tag each
separately. Retain the episode in training data with its violation tags. Do not delete a recorded
episode solely because it contains a violation.

### Violations

**Violation: Wrong order**
- **Visible cue:** an item is taken out before the zip is fully open, an item is taken out before the
  bag is held open, or the bag is moved before all four items are out.
- **SOP rule broken:** Steps 1 to 7 (open the bag, hold it open, take the four items out, then set the
  empty bag beside them, in that order).
- **Coaching note:** open, empty, then move the bag. One fixed order, every episode.

**Violation: Items out of order**
- **Visible cue:** the items do not come out as pencil case, lunchbox, bottle, book, or an item is
  pulled out from under another item.
- **SOP rule broken:** Steps 3 to 6 (pencil case, then lunchbox, then bottle, then book, always the
  item on top first).
- **Coaching note:** take what is on top.

**Violation: Zip opened in the wrong way**
- **Visible cue:** the right gripper starts the draw, the left gripper finishes it, or the draw starts
  from the open end of the track.
- **SOP rule broken:** Step 1 (the left gripper starts at the closed end, and the right gripper
  finishes at the open end).
- **Coaching note:** left starts at the closed end, right finishes.

**Violation: Bad hand-over of the loop tab**
- **Visible cue:** the left gripper lets go before the right gripper has the tab, the left gripper is
  still moving when the right gripper pinches, or the hand-over happens far from the top middle of the
  track.
- **SOP rule broken:** Step 1 (at the hand-over point the left gripper holds still for half a second,
  the right gripper pinches, and only then does the left gripper let go).
- **Coaching note:** stop, hold, pass, then let go.

**Violation: Zip not fully opened**
- **Visible cue:** the pull stops short of the open end and the episode moves on.
- **SOP rule broken:** Step 1 (draw the pull to the open end until it stops).
- **Coaching note:** run it to the stop before you reach inside.

**Violation: Zip touched anywhere but the loop tab**
- **Visible cue:** a gripper pinches the pull body, the zip tape, or the fabric beside the track.
- **SOP rule broken:** Step 1 (the loop tab is the only part of the zip a gripper pinches).
- **Coaching note:** tab only, every time.

**Violation: Bag not anchored during the draw**
- **Visible cue:** no gripper is on the bag while the other draws, and the bag slides or twists; or the
  anchor sits on the track or moves.
- **SOP rule broken:** Step 1 (one gripper anchors the bag away from the track while the other draws,
  and the anchor does not move).
- **Coaching note:** one gripper on the tab, the other still on the bag.

**Violation: Bag not held open**
- **Visible cue:** the right gripper reaches into a bag that nobody holds open; the left gripper takes
  the front panel anywhere but its top-left corner; or the left gripper lets go or moves before the book
  is out and the front panel falls onto an item or onto the right gripper.
- **SOP rule broken:** Steps 2 to 6 (the left gripper holds the top-left corner of the front panel up
  and still until the book is out).
- **Coaching note:** open first, and keep the hold until the bag is empty.

**Violation: Wrong arm did the work**
- **Visible cue:** the left gripper takes an item out or lays one out, the right gripper holds the bag
  open or moves the bag, or an arm reaches across the table.
- **SOP rule broken:** Steps 2 to 7 (the left gripper holds the bag open and moves the empty bag; the
  right gripper takes out and lays out every item).
- **Coaching note:** left holds and moves the bag, right handles the items.

**Violation: Item taken by the wrong part**
- **Visible cue:** the pencil case is taken by its zip or across its short sides; the lunchbox by its
  lid or across its long sides; the bottle by its cap; the book by its spine, by one cover, or by any
  corner other than the bottom-right.
- **SOP rule broken:** Steps 3 to 6 (pencil case across its long sides, lunchbox across its short sides,
  bottle around its body below the cap, book at its bottom-right corner through its full thickness).
- **Coaching note:** land on the grip point, or set it down and take it again.

**Violation: More than one item moved at once**
- **Visible cue:** two items come out together, or the right gripper picks a new item while still
  holding one.
- **SOP rule broken:** Steps 3 to 6 (one item at a time, laid out and let go before the next one is
  picked).
- **Coaching note:** one item per trip.

**Violation: Item dragged out**
- **Visible cue:** an item is slid out over the side of the bag, pulled across the other items, or
  dragged along the table with no space under it.
- **SOP rule broken:** Steps 3 to 6 (lift each item straight up until it is clear of the bag before
  carrying it).
- **Coaching note:** up first, then across.

**Violation: Item turned or tilted in the air**
- **Visible cue:** the lunchbox is tilted or carried lid down, the pencil case is turned on its side,
  the book hangs off level from its corner, the bottle is swung end over end, or the right gripper
  changes its hold in the air.
- **SOP rule broken:** Steps 3 to 6 (carry each item flat, the way it will be laid out).
- **Coaching note:** pick it the way it lands. Do not turn it in the air.

**Violation: Dropped from above**
- **Visible cue:** the right gripper opens above the table and the item falls the rest of the way, or
  an item falls back into the bag or onto the table during the carry.
- **SOP rule broken:** Steps 3 to 6 (lower each item until it rests, then let go).
- **Coaching note:** take it all the way down before you open.

**Violation: Item laid out in the wrong place**
- **Visible cue:** an item is laid out anywhere other than to the right of the item before it, the
  first item is not at the front middle, an item is laid on the bag or on the bag spot, or the row goes
  to the left.
- **SOP rule broken:** Steps 3 to 6 (the pencil case at the front middle, then each item to the right of
  the one before it, in one row).
- **Coaching note:** one row, going right, in the order the items come out.

**Violation: Items touching or stacked**
- **Visible cue:** an item is laid out touching another item, partly on top of it, or with no gap, and
  the episode moves on.
- **SOP rule broken:** Steps 3 to 6 (each item lies with a clear gap to the item before it, and no item
  touches another).
- **Coaching note:** leave a clear gap every time.

**Violation: Item not laid flat**
- **Visible cue:** the pencil case lies on its side, the lunchbox lies lid down or on its side, the book
  lies cover down or on its edge, or the bottle is stood up or left rolling.
- **SOP rule broken:** Steps 3 to 6 (pencil case zip up, lunchbox lid up, book cover up, bottle on its
  side, cap toward the back edge, each one settled).
- **Coaching note:** flat and still before you let go.

**Violation: Item left in the bag**
- **Visible cue:** the bag is lifted in Step 7 with an item still inside, or an item falls out of the
  bag while it is carried.
- **SOP rule broken:** Steps 3 to 7 (all four items are out and laid out before the bag is moved).
- **Coaching note:** look inside before you lift the bag.

**Violation: Bag moved while being emptied**
- **Visible cue:** the bag slides, turns, or lifts off the table while it is opened or while items come
  out, and it ends up away from the back center.
- **SOP rule broken:** Steps 1 to 6 (the bag stays flat at the back center until it is empty).
- **Coaching note:** the items come out of the bag, the bag stays put.

**Violation: Bag moved the wrong way**
- **Visible cue:** the bag is taken by a shoulder strap, a side, the zip, or the front panel instead of
  the top handle; it is dragged across the table; or it is carried by both grippers.
- **SOP rule broken:** Step 7 (the left gripper pinches the top handle at its middle, lifts the bag
  clear of the table, and carries it to the bag spot).
- **Coaching note:** top handle, lift, carry.

**Violation: Bag not set beside the items**
- **Visible cue:** the bag is set down away from the front-left, on top of an item, touching the pencil
  case, on its front panel, or standing up, and the episode moves on.
- **SOP rule broken:** Step 7 (the bag lies flat on its back panel at the bag spot, top toward the back
  edge, just left of the pencil case).
- **Coaching note:** base down first, then lay it back, beside the row.

**Violation: Item knocked out of place**
- **Visible cue:** a gripper or the bag knocks an item already laid out so that it moves, rolls, or
  turns over, and it is not set back.
- **SOP rule broken:** Steps 4 to 7 (an item stays where it was laid out).
- **Coaching note:** keep the grippers and the bag clear of the row.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops with an item out of the row or the bag not at the bag spot; an arm is
  not home; a gripper is closed; or an arm does something after homing.
- **SOP rule broken:** Step 8 (look once across the table, return both arms home with grippers open,
  then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than
tagging them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- The zip jams or its pull comes off the track under a straight draw.
- The loop tab is missing or torn off when the draw begins.
- An item is bad: a lunchbox lid that falls open, a leaking bottle, or a broken top handle.

## Annotation subtasks (from SOP)

1. Anchor the bag for the zip
2. Draw the zip to the hand-over point and hand the tab to the right gripper
3. Draw the zip to its open end
4. Hold the bag open
5. Move the pencil case from the bag to the front middle
6. Move the lunchbox from the bag to the layout row
7. Move the bottle from the bag to the layout row
8. Move the book from the bag to the layout row
9. Carry the empty bag by its top handle and set it beside the items
10. Look across the table, return both arms home, and end the episode
