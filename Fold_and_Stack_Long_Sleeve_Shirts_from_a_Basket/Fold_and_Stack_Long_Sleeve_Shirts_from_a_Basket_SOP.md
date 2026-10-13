# Fold and Stack Long-Sleeve Shirts from a Basket SOP (1x Episode: 4 Shirts)

One episode pulls four long-sleeve shirts out of a laundry basket one at a time, shakes each one
out, flattens it, folds the sleeves and sides in, folds it in half, and stacks the four folded shirts
square in one stack with their collars lined up. Then the empty basket is set aside.

Each shirt comes out of the basket by the **basket-side gripper**, which lifts it straight up and
lays it on the fold area. Both grippers then take the shirt by its two shoulder points, lift it, and
give it one short shake so the body and both sleeves hang straight. They lay it down face down,
collar toward the front edge, and flatten it: sleeves drawn straight out, body smooth.

Each side of the shirt gets two folds, sleeve first, then side. The left gripper folds the left
sleeve down along the left side of the body, then folds the left side in on the **fold line**, so the
sleeve ends up inside. The right gripper does the same on the right. Both grippers then lift the
shoulders and lay them back onto the hem. The **stack-side gripper** carries the folded shirt to the
stack and lays it square on the one below, collar over collar.

The order never changes: pull, shake out, flatten, sleeve and side folds, half fold, stack. One shirt
is out of the basket at a time, and it is on the stack before the next one comes out. After the
fourth shirt is on the stack, the basket-side gripper sets the empty basket aside.

The table is set up in one of two ways. The basket, the stack spot, and the aside spot move with the
config; the fold area is in the same place in both.

* **Config L:** the basket is in the back-left corner, the stack spot in the back-right corner, and
  the aside spot in the front-left corner.
* **Config R:** the basket is in the back-right corner, the stack spot in the back-left corner, and
  the aside spot in the front-right corner.

Where a step depends on the setup it says so on an **IF** line: look at the table and follow the
line that matches.

What stays constant across all sessions:

* **Start position:** the basket is at the back-left (**Config L**) or the back-right
  (**Config R**). One config per episode, chosen before recording and never changed mid-episode.
* **Basket-side rule:** the gripper on the basket's side pulls every shirt out of the basket and sets
  the empty basket aside: the left gripper in Config L, the right gripper in Config R.
* **Stack-side rule:** the gripper on the other side carries every folded shirt to the stack: the
  right gripper in Config L, the left gripper in Config R. No arm reaches across the table to the
  basket or to the stack.
* **Fixed roles:** everything else is the same in both configs. The left gripper flattens and folds
  the left sleeve and the left side. The right gripper flattens and folds the right sleeve and the
  right side. Both grippers shake the shirt out, lay it down, and fold it in half.

## Setup

Complete both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole tabletop: the basket, the fold area at the center of the
   table, the stack spot, and the aside spot for this episode's config.
3. The inside of the basket can be seen down to its floor, so every shirt in it can be seen.
4. The whole fold area is in frame, with room around it for both sleeves of a shirt laid straight
   out to the sides.
5. Both arms are at home with grippers open.
6. The tabletop holds nothing except the basket and robot hardware. The fold area, the stack spot,
   and the aside spot are bare.
7. Nothing blocks the paths between the basket, the fold area, the stack spot, and the aside spot.
8. Each arm reaches the whole fold area. The basket-side arm reaches the floor of the basket and the
   aside spot. The stack-side arm reaches the stack spot. No arm leans out or stretches to a joint
   limit to get there.
9. With a shirt held up by both shoulder points, the hem and both cuffs hang clear of the tabletop.

### Materials checklist

1. One **laundry basket**, empty except for the shirts, with low walls and a firm **rim** a gripper
   can pinch. The basket is light enough when empty to slide on the table with one gripper.
2. The basket sits flat on the table in the back corner for this episode's config:
   * **Config L:** back-left corner
   * **Config R:** back-right corner
3. Four **long-sleeve shirts** lie loose in the basket, crumpled as they come from the wash. None is
   folded, rolled, or knotted around another.
4. All four shirts are about the same size, dry, clean, and right side out, both sleeves right side
   out. Any buttons are done up. No shirt has tears or open seams.
5. Every shirt has a **collar** that can be seen once the shirt is laid flat.
6. The **fold area** at the center of the table is bare and big enough for one shirt laid flat with
   both sleeves straight out.
7. The **stack spot** for this episode's config is bare:
   * **Config L:** back-right corner
   * **Config R:** back-left corner
8. The **aside spot** for this episode's config is bare and big enough for the basket:
   * **Config L:** front-left corner
   * **Config R:** front-right corner

### Workspace layout

* **Basket:** the back-left corner (**Config L**) or the back-right corner (**Config R**). It stays
  where it is until the fourth folded shirt is on the stack. Only the gripper on that side reaches it.
* **Fold area:** the center of the table. Each shirt is shaken out over it, flattened, and folded
  here, one at a time. Both arms reach all of it.
* **Stack spot:** the back corner on the other side from the basket, where the four folded shirts go
  in one stack. Only the gripper on that side reaches it.
* **Aside spot:** the front corner on the basket's side, where the empty basket ends the episode.

The fold area stays the same for every episode; the basket, the stack spot, and the aside spot move
with the config.

### Arm assignments

* **Left gripper:** holds the left shoulder point for the shake and the lay-down, flattens the left
  sleeve and the left bottom corner, and folds the left sleeve and the left side in. In Config L it
  also pulls each shirt out of the basket and sets the empty basket aside. In Config R it also carries
  each folded shirt to the stack.
* **Right gripper:** holds the right shoulder point for the shake and the lay-down, flattens the right
  sleeve and the right bottom corner, and folds the right sleeve and the right side in. In Config R it
  also pulls each shirt out of the basket and sets the empty basket aside. In Config L it also carries
  each folded shirt to the stack.
* **Both grippers:** shake the shirt out, lay it down, and fold it in half together, one on each
  shoulder.
* Wherever one gripper works, the other works clear of it. The two grippers never crowd the same
  spot.

## Vocabulary

* **Shirt:** one long-sleeve shirt. There are four in an episode and they are worked one at a time.
* **Left and right:** always as seen from the front edge, for the shirt, the basket, and the table.
  The **left shoulder** of a held shirt is the one on the left as seen from the front edge.
* **Next shirt:** the shirt lying on top in the basket, the one with the most of it showing. If two
  are level, either one.
* **Basket-side gripper:** the gripper on the basket's side: the left gripper in Config L, the right
  gripper in Config R.
* **Stack-side gripper:** the gripper on the stack spot's side: the right gripper in Config L, the
  left gripper in Config R.
* **Rim:** the top edge of the basket wall. The **front rim** is the rim along the wall facing the
  front edge.
* **Collar:** the band around the neck opening.
* **Shoulder point:** the top corner of the shirt where the shoulder seam meets the sleeve. There is a
  **left shoulder point** and a **right shoulder point**.
* **Held shirt:** a shirt hanging from the left gripper at the left shoulder point and the right
  gripper at the right shoulder point, front facing the front edge, the shoulders spread out flat
  between the grippers, the hem and both cuffs hanging free.
* **Shake:** with the shirt held, both grippers drop a hand's width together and lift straight back
  up at once, one short move, so the body and sleeves fall straight.
* **Face down:** the shirt lies with its front on the table and its back showing.
* **Cuff:** the end of a sleeve, at its opening. There is a **left cuff** and a **right cuff**.
* **Bottom corner:** one of the two corners where the hem meets a side of the shirt. There is a
  **left bottom corner** and a **right bottom corner**.
* **Fold line:** a straight line from one end of the collar straight back to the hem. There is a
  **left fold line** and a **right fold line**. Each side is folded in on its own fold line.
* **Side panel:** the part of the body between a fold line and the side of the shirt. There is a
  **left side panel** and a **right side panel**.
* **Flat:** the shirt lies face down on the fold area, collar toward the front edge, hem toward the
  back, both sleeves straight out to the sides from the shoulders, the body smooth with no fold
  across it, and no corner, sleeve, or hem folded under.
* **Strip:** the shirt once both sleeves and both sides are folded in: a long flat piece, the width of
  the collar, running from the shoulders at the front to the hem at the back, with both sleeves
  folded inside.
* **Folded shirt:** the strip folded in half, shoulders laid on the hem. The **fold edge** is the edge
  at the front where the strip bends over. The **open edge** is the back edge, where the shoulders and
  the hem lie on each other. The collar lies on top, at the open edge.
* **Stack:** the folded shirts in one pile on the stack spot, each laid square on the one below it,
  fold edges toward the front edge.
* **Square on the stack:** a folded shirt sits right on top of the one below it, its edges in line
  with that one's edges on all four sides, nothing hanging over on one side.
* **Collars lined up:** every folded shirt in the stack has its collar at the back, on top, right over
  the collar of the shirt below it.
* **Lift away:** raise the gripper or item straight up until there is daylight under it, before
  anything moves sideways.
* **Carry level:** move the item across at one height, without turning or swinging it.
* **Settled:** the item stays put when the gripper lifts away, with nothing sliding, springing
  open, or falling.
* **Let-go point:** a gripper opens only at one of these: the basket-side gripper once the pulled
  shirt lies on the fold area; the left gripper on the fold area once a left sleeve, corner, or side
  lies where it was laid; the right gripper the same on the right; both grippers once the shirt is
  laid on the fold area or the shoulders lie on the hem; the stack-side gripper once the folded shirt
  lies on the stack spot or square on the stack; the basket-side gripper once the basket sits on the
  aside spot.

## Steps

Run Steps 1 to 6 four times, once per shirt. Then run Step 7 and Step 8 once each. One shirt is out
of the basket at a time, and it is on the stack before the next one comes out.

Steps 1, 6, and 7 depend on the config: the IF lines say which gripper pulls the shirt out, which
carries it to the stack, and where the basket goes. Steps 2 to 5 are the same in both configs.

Any grasp or fold may be retried. If a gripper slips off or a corner lands in the wrong place, the
gripper opens, takes the same point again, and lays it again. Nothing is ever forced to save a retry.

### Step 1: Pull the next shirt out of the basket

**Goal:** the next shirt lies on the fold area, out of the basket, and the other shirts are still in
the basket.

* **IF the basket is at the back-left (Config L):** the **left gripper** pulls the shirt out. The
  **right gripper** waits clear of the basket.
* **IF the basket is at the back-right (Config R):** the **right gripper** pulls the shirt out. The
  **left gripper** waits clear of the basket.

Then, in both:

* The **basket-side gripper** pinches the **next shirt** on a part that lies on top, clear of the
  other shirts.
* The **basket-side gripper** lifts it straight up, slowly, until the whole shirt hangs clear of the
  rim.
* The **basket-side gripper** carries it to the fold area and lowers it until it lies on the table.
  It may lie bunched.
* The **basket-side gripper** opens and lifts away.

Take only the next shirt. If a second shirt comes up with it, the **basket-side gripper** lowers both
back into the basket before they clear the rim, opens, and takes the next shirt again. Never drag a
shirt over the rim and never tip or hold the basket.

**Check:** one shirt lies on the fold area. The other shirts are still in the basket. The basket has
not moved.

### Step 2: Shake the shirt out

**Goal:** the shirt is a **held shirt**, shaken out, body and both sleeves hanging straight.

#### 2.1 Take the shoulder points

* The **left gripper** pinches the **left shoulder point** of the shirt.
* The **right gripper** pinches the **right shoulder point**.
* The **left gripper** and the **right gripper** lift together until the hem and both cuffs hang
  clear of the table, front facing the front edge.

If the shirt hangs with its back toward the front edge, the **left gripper** and the **right
gripper** lay it back down on the fold area, open, and take the shoulder points again.

#### 2.2 Shake once

* The **left gripper** and the **right gripper** give the shirt one **shake** together.
* The **left gripper** and the **right gripper** keep hold of the shoulder points.

If a sleeve is still caught inside the body or twisted after the shake, the **left gripper** and the
**right gripper** give one more shake. Never flick the shirt, swing it, or shake it by a sleeve or
the hem.

**Check:** the shirt is a held shirt: front facing the front edge, shoulders spread between the
grippers, body and both sleeves hanging straight, nothing caught inside out.

### Step 3: Flatten the shirt

**Goal:** the shirt is **flat** on the fold area, face down, collar toward the front edge.

#### 3.1 Lay it down

* The **left gripper** and the **right gripper** bring the shirt down until the hem touches the back
  of the fold area.
* The **left gripper** and the **right gripper** keep moving toward the front edge as they come down,
  so the shirt lays down onto its front, hem first and collar last.
* With the collar on the table toward the front edge, the **left gripper** and the **right gripper**
  open and lift away.

#### 3.2 Smooth it out

* The **left gripper** pinches the **left cuff** and draws the left sleeve straight out to the left,
  then lays it down flat.
* The **right gripper** pinches the **right cuff** and draws the right sleeve straight out to the
  right, then lays it down flat.
* The **left gripper** pinches the **left bottom corner** and draws it a little toward the back, so
  the left half of the body lies smooth.
* The **right gripper** pinches the **right bottom corner** and draws it a little toward the back, so
  the right half of the body lies smooth.

A wrinkle that stays may be smoothed out by the gripper on its side, closed and lying flat, stroked
from the middle of the shirt outward.

**Check:** the shirt is flat: face down, collar toward the front edge, hem toward the back, both
sleeves straight out to the sides, no corner, sleeve, or hem folded under, and no fold across the
body.

If the shirt is face up, twisted, or bunched, the **left gripper** and the **right gripper** take the
two shoulder points again, lift the shirt until the hem hangs free, and lay it down again.

### Step 4: Fold the sleeves and sides in

**Goal:** the shirt is a **strip**: each sleeve folded down along its side panel, each side folded in
on its fold line over the sleeve.

#### 4.1 Fold the left sleeve

* The **left gripper** pinches the **left cuff**, lifts it, and carries it toward the back, so the
  sleeve bends at the shoulder.
* The **left gripper** lays the sleeve straight down on the **left side panel**, along the side of the
  body, cuff toward the hem.
* The **left gripper** opens and lifts away.

#### 4.2 Fold the left side

* The **left gripper** pinches the **left bottom corner**, lifts it, and carries it to the right over
  the shirt.
* The **left gripper** lays it down so the left side panel bends over along the left fold line, with
  the left sleeve folded inside, the crease running straight from the left end of the collar to the
  hem.
* The **left gripper** opens and lifts away.

#### 4.3 Fold the right sleeve

* The **right gripper** pinches the **right cuff**, lifts it, and carries it toward the back, so the
  sleeve bends at the shoulder.
* The **right gripper** lays the sleeve straight down on the **right side panel**, along the side of
  the body, cuff toward the hem.
* The **right gripper** opens and lifts away.

#### 4.4 Fold the right side

* The **right gripper** pinches the **right bottom corner**, lifts it, and carries it to the left over
  the shirt.
* The **right gripper** lays it down so the right side panel bends over along the right fold line,
  with the right sleeve folded inside, the crease running straight from the right end of the collar
  to the hem.
* The **right gripper** opens and lifts away.

While the left gripper folds, the **right gripper** waits clear of the fold area; while the right
gripper folds, the **left gripper** waits clear of it.

**Check:** the shirt is a strip the width of the collar, with two straight creases running side by
side from the collar to the hem. Both sleeves lie inside the folds, with no cuff or sleeve sticking
out past a crease or past the hem.

If a sleeve lies crooked or off its side panel, the gripper on that side lifts the cuff and lays it
again before the side is folded. If a crease runs crooked or does not meet the collar, the gripper on
that side lifts the bottom corner and lays it again. If the left side opened during the right folds,
the **left gripper** folds it in again.

### Step 5: Fold the shirt in half

**Goal:** a **folded shirt**: the shoulders laid on the hem, fold edge toward the front edge, collar
on top at the back.

* The **left gripper** pinches the strip at its left shoulder corner and the **right gripper** at its
  right shoulder corner, at the front end of the strip.
* The **left gripper** and the **right gripper** lift the shoulders and carry them level toward the
  back, over the top of the strip.
* The **left gripper** and the **right gripper** lay the shoulders down on the hem, shoulder corners
  on the bottom corners.
* The **left gripper** and the **right gripper** open and lift away.

**Check:** the folded shirt lies flat, the shoulder edge on top of the hem edge, corners on corners,
the fold edge straight across the front, the collar on top at the back. No sleeve, cuff, or corner
sticks out from between the layers.

If the shoulders landed off the hem or crooked, the **left gripper** and the **right gripper** take
the shoulder corners again, lift them a little, and lay them again on the hem.

### Step 6: Put the folded shirt on the stack

**Goal:** the folded shirt lies **square on the stack**, fold edge toward the front edge, **collars
lined up**.

* **IF the basket is at the back-left (Config L):** the **right gripper** pinches the folded shirt at
  the middle of its fold edge, lifts it a little, and carries it level to the right, to the stack spot
  at the back-right. The **left gripper** waits clear of the stack.
* **IF the basket is at the back-right (Config R):** the **left gripper** pinches the folded shirt at
  the middle of its fold edge, lifts it a little, and carries it level to the left, to the stack spot
  at the back-left. The **right gripper** waits clear of the stack.

Then, in both:

* The **stack-side gripper** brings the folded shirt down, open edge first, and lays it flat as it
  comes down, fold edge toward the front edge and collar at the back.
* The **stack-side gripper** puts the first folded shirt in the middle of the bare stack spot, and
  each one after it square on top of the stack, its collar right over the collar below.
* The **stack-side gripper** opens and lifts away.
* Go back to Step 1 for the next shirt. After the fourth shirt, go on to Step 7.

Carry the folded shirt low and keep it folded. Never drag it across the table and never drop it onto
the stack.

**Check:** the folded shirt lies square on the stack, fold edge toward the front edge, collar over the
collar below, still folded, and **settled**. The stack below it has not moved.

If it landed off square or its collar is not over the collar below, the **stack-side gripper** lifts
it a little by the middle of the fold edge and lays it again. Never push the whole stack.

### Step 7: Set the empty basket aside

**Goal:** the empty basket sits on the aside spot.

* **IF the basket is at the back-left (Config L):** the **left gripper** moves the basket to the aside
  spot at the front-left. The **right gripper** waits clear of the basket.
* **IF the basket is at the back-right (Config R):** the **right gripper** moves the basket to the
  aside spot at the front-right. The **left gripper** waits clear of the basket.

Then, in both:

* The **basket-side gripper** pinches the **front rim** at its middle.
* The **basket-side gripper** slides the basket straight toward the front edge, flat on the table,
  until it sits on the aside spot.
* The **basket-side gripper** opens and lifts away.

Set the basket aside only once it is empty and the fourth folded shirt is on the stack. Never lift,
tip, or turn the basket.

**Check:** the basket sits flat on the aside spot, empty. The stack has not moved.

### Step 8: End the episode

**Goal:** recording ends with four folded shirts in one stack and the empty basket on the aside spot.

* Look once across the table: four folded shirts square in one stack, collars lined up at the back,
  the fold area bare, and the empty basket on the aside spot.
* Return both arms home with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are open, and neither holds anything.

**Expected state:** the stack and the basket are still, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Unfold each shirt from the stack and shake it out. Check it is right side out, both sleeves right
   side out, and any buttons are done up.
2. Put the basket back in the back corner for the next episode's config: back-left (Config L) or
   back-right (Config R).
3. Crumple the four shirts loosely into the basket, none folded, rolled, or knotted around another.
4. Check the basket: no cracked wall, no broken rim, and it still sits flat.
5. Replace anything damaged: a shirt that is torn, stained, or damp; a shirt with an open seam or a
   loose button; or a basket that is cracked or rocks.
6. Clear and wipe the fold area. Make sure the stack spot and the aside spot for the next episode's
   config are bare.
7. Run both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The
visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation
label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain several violations; tag each
one separately. Keep the episode with its violation tags. Do not delete it just because a rule was
broken.

Tag a violation only when something is forced, the order is broken, or the episode moves on with a
fault left in place.

### Violations

**Violation: Config misaligned**

* **Visible cue:** what the arms do does not match the config on the table: the gripper on the other
  side pulls a shirt out of the basket or moves the basket; the basket-side gripper carries a folded
  shirt to the stack; the stack is built somewhere other than the stack spot for the config; the
  basket is set aside somewhere other than the aside spot for the config; a gripper reaches across
  the table to the basket or the stack; or the wrong IF line is followed.
* **SOP rule broken:** Steps 1, 6, and 7, the basket-side rule and the stack-side rule (the gripper on
  the basket's side pulls the shirts and sets the basket aside, the gripper on the other side stacks,
  and the IF line followed is the one for the config on the table).
* **Coaching note:** look where the basket is before the first pull, then follow that config's IF
  lines in Steps 1, 6, and 7.

**Violation: Wrong order, or two shirts worked at once**

* **Visible cue:** the shirt is laid down without a shake; a fold starts before the shirt is flat; a
  side is folded before its sleeve; the right side is worked before the left; the shirt is folded in
  half before both sleeves and sides are in; or a second shirt comes out of the basket before the
  last one is on the stack.
* **SOP rule broken:** Steps 1 to 6, pull, shake out, flatten, sleeve and side folds (left sleeve,
  left side, right sleeve, right side), half fold, then stack, in that order, one shirt at a time.
* **Coaching note:** finish the shirt on the stack before you touch the next one.

**Violation: Two shirts pulled out together**

* **Visible cue:** a second shirt comes out over the rim with the next shirt, hangs off it, or falls
  onto the table or the rim, and the episode moves on.
* **SOP rule broken:** Step 1, only the next shirt comes out; a second shirt that comes up with it is
  lowered back into the basket before it clears the rim.
* **Coaching note:** lift slowly. If two come up, put both back and take the top one again.

**Violation: Shirt dragged over the rim**

* **Visible cue:** the shirt is pulled out sideways so it drags over the rim, catches on the rim, or is
  pulled while part of it is still under another shirt.
* **SOP rule broken:** Step 1, the basket-side gripper pinches a part that lies on top and lifts the
  shirt straight up until the whole shirt hangs clear of the rim.
* **Coaching note:** straight up first, all the way clear, then across.

**Violation: Basket moved before it is empty**

* **Visible cue:** the basket slides, tips, or lifts while a shirt is pulled out, or a gripper holds,
  leans on, or steadies the basket before Step 7.
* **SOP rule broken:** Step 1, the basket stays where it is until the fourth folded shirt is on the
  stack, and no gripper touches it before then.
* **Coaching note:** pull the shirt, not the basket. If the basket moves, you are pulling too hard or
  too low.

**Violation: Shake done the wrong way**

* **Visible cue:** the shake is skipped; the shirt is shaken by one gripper, by a sleeve, a cuff, or
  the hem; it is flicked, swung, or slapped on the table; or it is shaken more than twice.
* **SOP rule broken:** Step 2.2, both grippers hold the shoulder points and give one short shake
  together, with one more only if a sleeve is still caught or twisted.
* **Coaching note:** one gripper on each shoulder, drop a hand's width, lift back up.

**Violation: Shirt not held by both shoulder points**

* **Visible cue:** the shirt is lifted, shaken, or laid down by one gripper only, by a sleeve, the
  collar, or the hem, or it hangs with its back toward the front edge and is laid down that way.
* **SOP rule broken:** Steps 2.1 and 3.1, the left gripper holds the left shoulder point and the right
  gripper the right shoulder point, front facing the front edge, from the lift to the lay-down.
* **Coaching note:** find the collar first, then one gripper on each shoulder point.

**Violation: Shirt laid down the wrong way**

* **Visible cue:** the shirt is laid face up, collar toward the back or a side, dropped onto the
  table, or laid outside the fold area.
* **SOP rule broken:** Step 3.1, the shirt is laid face down on the fold area, hem first and collar
  last, collar toward the front edge.
* **Coaching note:** hem down at the back, then move toward the front as it goes down.

**Violation: Fold started on a shirt not flat**

* **Visible cue:** a sleeve or side is folded while a sleeve is not straight out, a corner, a sleeve,
  or the hem is folded under, the shirt is twisted, or there is a fold across the body.
* **SOP rule broken:** Step 3.2, both sleeves are drawn straight out and both bottom corners drawn
  smooth, so the shirt is flat before any fold starts.
* **Coaching note:** sleeves out, corners back, look at the whole shirt before you fold.

**Violation: Sleeve or side folded the wrong way**

* **Visible cue:** a sleeve is laid across the back of the body instead of down its side panel; a
  sleeve is folded by the elbow instead of the cuff; a side is folded from the middle of the body or
  by the hem instead of the bottom corner; a sleeve or side is folded by the other side's gripper; or
  both sides are folded at once.
* **SOP rule broken:** Step 4, each sleeve is folded by its cuff straight down onto its side panel,
  then its side is folded by the bottom corner over it, each by its own gripper, left then right.
* **Coaching note:** cuff down the side, then the corner over it, one side at a time, each with its
  own gripper.

**Violation: Crease crooked or off the fold line**

* **Visible cue:** a side crease runs crooked, does not meet the end of the collar, or makes the strip
  wider at one end, and the episode moves on to the next fold.
* **SOP rule broken:** Steps 4.2 and 4.4, each side bends over on its fold line, the crease running
  straight from the end of the collar to the hem; a crooked crease is laid again before moving on.
* **Coaching note:** line the crease up with the end of the collar. If it is crooked, lay the corner
  again.

**Violation: Sleeve left sticking out**

* **Visible cue:** after the side fold, a sleeve or cuff sticks out past its crease or past the hem,
  lies bunched or twisted inside the fold, or is left unfolded, and the episode moves on.
* **SOP rule broken:** Steps 4.1 to 4.4, each sleeve lies straight on its side panel and ends up inside
  the side fold, nothing past the crease or the hem.
* **Coaching note:** lay the sleeve straight down the side panel. If it shows after the side fold, open
  the side and lay the sleeve again.

**Violation: Half fold done the wrong way**

* **Visible cue:** the hem is folded onto the shoulders instead of the shoulders onto the hem; the
  strip is folded from the side instead of end to end; the half fold is made by one gripper; or the
  shoulders land off the hem or crooked and the episode moves on.
* **SOP rule broken:** Step 5, both grippers take the shoulder corners, carry them back over the
  strip, and lay them on the hem, corners on corners.
* **Coaching note:** one gripper on each shoulder corner, back over the top, corners on corners.

**Violation: Folded shirt carried the wrong way**

* **Visible cue:** the folded shirt is carried by an open edge or a corner instead of the middle of
  the fold edge; it is dragged across the table; it is carried high or swung; or it opens up on the
  way.
* **SOP rule broken:** Step 6, the stack-side gripper pinches the middle of the fold edge, lifts it a
  little, and carries it level and low, still folded.
* **Coaching note:** middle of the fold edge, low and level.

**Violation: Folded shirt dropped onto the stack**

* **Visible cue:** the stack-side gripper opens above the stack so the folded shirt falls the last
  part of the way, lands opened, or slides off; or a gripper opens anywhere other than at a let-go
  point.
* **SOP rule broken:** Step 6, the folded shirt is brought down and laid flat before the gripper
  opens, and a gripper opens nowhere but at a let-go point.
* **Coaching note:** all the way down, lay it flat, then let go.

**Violation: Folded shirt not square on the stack**

* **Visible cue:** a folded shirt hangs over the one below on one side, sits turned, or the first one
  is put off the middle of the stack spot, and the next shirt comes out of the basket.
* **SOP rule broken:** Step 6, each folded shirt lies square on the stack, and an off-square one is
  lifted and laid again.
* **Coaching note:** edges on edges. If it is off, lift it and lay it again.

**Violation: Collars not lined up**

* **Visible cue:** a folded shirt is stacked with its collar toward the front or a side, or its collar
  sits off the collar below, and the episode moves on.
* **SOP rule broken:** Step 6, every folded shirt goes on fold edge toward the front edge, collar at
  the back, right over the collar below.
* **Coaching note:** fold to the front, collar over collar.

**Violation: Stack pushed or slid**

* **Visible cue:** a gripper pushes, slides, or squares the whole stack, or slides a folded shirt
  along the top of the stack instead of lifting it and laying it again.
* **SOP rule broken:** Step 6, an off-square shirt is fixed by lifting it a little by the middle of
  the fold edge and laying it again; the stack is never pushed.
* **Coaching note:** lift it and lay it again. Nothing gets pushed.

**Violation: Basket set aside the wrong way**

* **Visible cue:** the basket is set aside while a shirt is still in it or before the fourth folded
  shirt is on the stack; it is lifted, tipped, turned, or pulled by a corner instead of the middle of
  the front rim; or it stops short of the aside spot or bumps the stack.
* **SOP rule broken:** Step 7, once the basket is empty and the fourth shirt is stacked, the
  basket-side gripper slides it straight forward by the middle of the front rim, flat on the table,
  onto the aside spot.
* **Coaching note:** last shirt stacked first, then the front rim, slide it straight forward.

**Violation: Arms swapped roles or crowded the same spot**

* **Visible cue:** the right gripper flattens or folds the left sleeve or side; the left gripper
  flattens or folds the right sleeve or side; the idle gripper works over the fold area while the
  other folds; or the two grippers work the same spot, touch each other, or one has to move before
  the other can reach.
* **SOP rule broken:** Steps 3 to 5, the left gripper flattens and folds the left sleeve and side, the
  right gripper the right sleeve and side, and the other gripper waits clear while one folds.
* **Coaching note:** left does the left, right does the right. Neither one does the other's work.

**Violation: Item dropped or something knocked over**

* **Visible cue:** a shirt falls onto the tabletop or the floor on the way from the basket; a gripper
  strikes the basket; the stack is knocked over or out of place; or the two arms strike each other.
* **SOP rule broken:** Steps 1 to 7, each item stays on a clear path, the shirts not yet worked stay
  in the basket, and a gripper opens only at a let-go point.
* **Coaching note:** check the path and the landing spot before you move.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with fewer than four shirts in the stack, a shirt still in the
  basket or on the fold area, the basket not on the aside spot, or the stack not square; or either arm
  is away from home, a gripper is closed, or an arm does something else after homing.
* **SOP rule broken:** Step 8, look once across the table, return both arms home with grippers open,
  then stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

These failures are not caused by how the task was run. Log them as system issues, throw the episode
away, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Bad shirt:** a torn shirt, an open seam, a loose button, or a sleeve that was staged inside out.
  Replace or fix it before the next episode.
* **Bad basket:** a cracked wall, a broken rim, or a basket that rocks or will not slide flat.
  Replace it before the next episode.
* **Shirt too long for the arms:** a held shirt's hem or cuffs touch the table at full lift.

## Annotation subtasks (from SOP)

1. Pull the next shirt out of the basket
2. Take the shoulder points
3. Shake the shirt out
4. Lay the shirt down on the fold area
5. Smooth the shirt out
6. Fold the left sleeve
7. Fold the left side
8. Fold the right sleeve
9. Fold the right side
10. Fold the shoulders back onto the hem
11. Put the folded shirt on the stack
12. Set the empty basket aside
13. Return both arms home and end the episode
