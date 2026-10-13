# Fold a Napkin into a Pocket and Put the Utensils Inside SOP (1x Episode: 1 Napkin, 3 Utensils)

One episode folds one cloth napkin into a **silverware pocket** and puts three clean utensils inside
it. The episode ends when the knife, the fork, and the spoon sit in the pocket, eating ends in and
handle ends sticking out of the **mouth**.

The napkin starts flat and square on the work area. The left gripper and the right gripper fold it
in half, front to back, so the **front crease** is at the front edge and becomes the bottom of the
pocket. The left gripper and the right gripper fold the **top layer** back over itself into a
**cuff**. The left gripper and the right gripper **turn the napkin over**. The left gripper folds the
left side in, and the right gripper folds the right side in over it, to thirds. The left gripper and
the right gripper turn the napkin back over.
The side folds now lie underneath and close the pocket's sides, the cuff lies on top, and the mouth
faces the back.

In Config L, the left gripper slides the knife, the fork, and the spoon into the mouth one at a time,
eating end first, while the right gripper holds the mouth open. In Config R, the right gripper slides
them in while the left gripper holds the mouth open.

The order never changes: half fold, cuff, turn over, left side, right side, turn back, knife, fork,
spoon. Every fold and both turns stay on the table. The napkin is never lifted into the air.

The table is set up in one of two ways. Only the utensil spot moves; the napkin and the work area are
in the same place in both.

* **Config L:** the utensil spot is in the back-left corner.
* **Config R:** the utensil spot is in the back-right corner.

Where a step depends on the setup it says so on an **IF** line: look at the table and follow the line
that matches.

What stays constant across all sessions:

* **Start position:** the utensil spot is at the back-left (**Config L**) or the back-right
  (**Config R**). One config per episode, chosen before recording and never changed mid-episode.
* **Utensil-side rule:** in Config L the left gripper picks up all three utensils and puts them in
  the pocket, and the right gripper holds the mouth open. In Config R the right gripper picks up all
  three utensils and puts them in the pocket, and the left gripper holds the mouth open. No arm
  reaches across the table to the utensil spot.
* **Fixed roles:** everything else is the same in both configs. The left gripper and the right
  gripper make the half fold, the
  cuff, and both turns, one at each end. The left gripper folds the left side in. The right gripper
  folds the right side in.

## Setup

Complete both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole tabletop: the napkin on the work area, the whole turn space
   behind it, and the utensil spot for this episode's config.
3. All four corners of the napkin are in frame, with clear table around each one.
4. Both arms are at home with grippers open.
5. The tabletop holds nothing except the napkin, the three utensils on the utensil spot, and robot
   hardware.
6. Nothing blocks the path between the utensil spot and the work area.
7. Each arm reaches the whole work area, the whole turn space, and the utensil spot on its own side.
   It does not lean out or stretch to a joint limit to get there.

### Materials checklist

1. One **napkin**: a square cloth napkin about 40 cm a side, plain, the same on both sides, clean,
   dry, and pressed flat, with no tears and no loose threads.
2. The napkin lies flat and square in the middle of the **work area**, its sides in line with the
   table edges. No corner is folded under and there is no fold across it.
3. Three **utensils**: one dinner knife, one dinner fork, and one dinner spoon, all about the same
   length, clean and dry, with no bent tines or handles.
4. The three utensils lie flat on the **utensil spot**, side by side with a small gap between them,
   each pointing front to back with its **eating end** toward the front edge and its **handle end**
   toward the back. From left to right: knife, fork (tines up), spoon (bowl up).
5. The **utensil spot** for this episode's config:
   * **Config L:** back-left corner
   * **Config R:** back-right corner
6. The **turn space** behind the napkin is bare and at least as deep as the folded napkin.

### Workspace layout

* **Work area:** the center of the table, toward the front edge. The napkin starts here, is folded
  here, and ends here as the pocket. Both arms reach all of it.
* **Turn space:** the bare table just behind the work area. The napkin lies here after the first turn
  and for the side folds, then turns back onto the work area.
* **Utensil spot:** the back-left corner (**Config L**) or the back-right corner (**Config R**), where
  the three utensils start. Only the left gripper reaches it in Config L, and only the right gripper
  in Config R.

The work area and the turn space stay the same for every episode; only the utensil spot moves with the
config.

### Arm assignments

* **Left gripper:** folds the left side in. In Config L it also puts the three utensils in the pocket.
  In Config R it holds the mouth open.
* **Right gripper:** folds the right side in. In Config R it also puts the three utensils in the
  pocket. In Config L it holds the mouth open.
* **Left gripper and right gripper together:** make the half fold, the cuff, and both turns, the left
  gripper at the left end and the right gripper at the right end.
* Wherever the left gripper works alone, the right gripper waits clear of the napkin, and the other
  way round. The two grippers never crowd
  the same spot.

## Vocabulary

* **Left and right:** always as seen from the front edge.
* **Half fold:** the napkin folded in half, front to back. It has two layers. The **front crease** is
  where the napkin bends over, at the front. The **open edges** are the two loose edges at the back.
* **Bottom layer:** the half of the napkin that stays on the table in the half fold.
* **Top layer:** the half that is folded back onto it. Its back edge stops a little short of the
  bottom layer's back edge, so a thin strip of the bottom layer shows behind it.
* **Cuff:** the back part of the top layer, folded forward onto itself so its edge lies across the
  middle of the napkin. The **cuff crease** is where it bends, toward the back.
* **Mouth:** the opening of the pocket, along the cuff crease, between the top layer and the bottom
  layer. The utensils go in here.
* **Turn over:** the left gripper and the right gripper pinch one end of the napkin, the left gripper
  at the left corner and the right gripper at the right corner, lift that end, carry it up and over
  the napkin, and lay it down on the far side. The other end stays on the table, like turning a page.
  The napkin ends up face down, in front or behind where it was.
* **Thirds:** the width of the napkin split into three equal parts, judged by eye.
* **Side fold:** a side of the napkin folded in to the middle, one third wide. The left side folds in
  first; the right side folds over it, its edge on the left side's crease.
* **Pocket:** the finished napkin: one third wide, the front crease at the front edge, the cuff on
  top, the side folds underneath, the mouth across the back.
* **Utensils:** the knife, the fork, and the spoon.
* **Eating end:** the blade of the knife, the tines of the fork, the bowl of the spoon.
* **Handle end:** the other end, the end of the handle.
* **Handle middle:** the middle of a utensil's handle. The left gripper or the right gripper picks up
  a utensil only here.
* **In the pocket:** a utensil lies inside the mouth, between the top layer and the bottom layer,
  eating end toward the front crease and handle end sticking out of the mouth toward the back.
* **Open the mouth:** the gripper that holds the mouth (the right gripper in Config L, the left
  gripper in Config R) pinches the cuff crease near the end of the mouth on its own side, top layer
  only, and lifts it a little, so the mouth opens.
* **Waits clear:** the left gripper or the right gripper, when it has nothing to do, stays up and away
  from the napkin, the utensils, and the other gripper, but does not go home.
* **Lift away:** raise the gripper or item straight up until there is daylight under it, before
  anything moves sideways.
* **Carry level:** move the item across at one height, without turning, swinging, or shaking it.
* **Settled:** the item stays put when the gripper lifts away, with nothing sliding, springing open,
  or falling.
* **Let-go point:** the left gripper or the right gripper opens only at one of these: the left gripper
  and the right gripper together once a fold or a turn lies down
  on the table; the left gripper once the left side lies folded in; the right gripper once the right
  side lies folded in; the gripper putting the utensils in (left in Config L, right in Config R) once
  a utensil lies in the pocket; the gripper holding the mouth (right in Config L, left in Config R)
  once the spoon is in and the cuff crease lies back down.

## Steps

Run Steps 1 to 7 once, in order.

Only Step 6 depends on the config: each bullet there names the gripper for Config L and the gripper
for Config R. Every other step is the same in both configs.

Any fold may be retried. If the left gripper or the right gripper slips off or lays a corner in the
wrong place, that same gripper opens, takes the same point again, and lays it again. Nothing is ever forced to save a retry.

### Step 1: Fold the napkin in half

**Goal:** a **half fold**, the front crease along the front, the top layer a little short of the back.

* The **left gripper** pinches the front-left corner of the napkin. The **right gripper** pinches the
  front-right corner.
* The **left gripper** and the **right gripper** lift the front edge a little and carry it toward the
  back, low over the napkin.
* The **left gripper** and the **right gripper** lay the front edge down just short of the back edge,
  so a thin strip of the bottom layer shows behind it.
* The **left gripper** and the **right gripper** open and lift away.

**Check:** the front crease runs straight left to right. The top layer's sides lie on the bottom
layer's sides. A thin, even strip of the bottom layer shows behind the top layer from end to end.

If the strip is uneven or the sides do not match, the **left gripper** and the **right gripper** take
the top layer's back corners again, lift them a little, and lay them again.

### Step 2: Fold the cuff

**Goal:** a **cuff** across the top layer, its edge across the middle of the napkin.

* The **left gripper** pinches the back-left corner of the top layer only. The **right gripper**
  pinches the back-right corner of the top layer only.
* The **left gripper** and the **right gripper** lift the top layer's back edge a little and carry it
  toward the front, low over the top layer.
* The **left gripper** and the **right gripper** lay the edge down across the middle of the napkin.
* The **left gripper** and the **right gripper** open and lift away.

Fold the top layer only. The bottom layer stays flat on the table.

**Check:** the cuff crease runs straight left to right. The cuff's edge lies straight across the middle.
The bottom layer still lies flat behind the cuff crease.

If the cuff is crooked or its edge is far from the middle, the **left gripper** and the **right
gripper** take the cuff's edge at both ends, lift it a little, and lay it again. If the bottom layer
came up with the cuff, the **left gripper** and the **right gripper** open the cuff and fold it again.

### Step 3: Turn the napkin over

**Goal:** the napkin lies face down in the **turn space**, the cuff underneath, the front crease at the
back.

* The **left gripper** pinches the left end of the front crease. The **right gripper** pinches the
  right end.
* The **left gripper** and the **right gripper** lift the front crease, carry it up and over the
  napkin toward the back, and lay it down in the turn space. The open edges stay on the table the
  whole time.
* The **left gripper** and the **right gripper** open and lift away.

**Check:** the napkin lies flat in the turn space, the plain back of the bottom layer on top, the
front crease at the back. The cuff cannot be seen. No layer has slid out from the others.

If the cuff or the half fold came open, the **left gripper** and the **right gripper** turn the napkin
back over onto the work area and run Steps 1 to 3 again.

### Step 4: Fold the sides in

**Goal:** the napkin is one third wide, both sides folded in.

#### 4.1 Fold in the left side

* The **left gripper** pinches the left side at its middle, through all the layers.
* The **left gripper** lifts it a little, carries it to the right, and lays it down so the crease is
  one third in from the left.
* The **left gripper** opens and lifts away.
* The **right gripper** waits clear of the napkin.

#### 4.2 Fold in the right side

* The **right gripper** pinches the right side at its middle, through all the layers.
* The **right gripper** lifts it a little, carries it to the left over the left side fold, and lays
  the right side down on the left side's crease.
* The **right gripper** opens and lifts away.
* The **left gripper** waits clear of the napkin.

**Check:** the napkin is one third wide. Both creases run straight front to back. The right side lies on
the left crease. Nothing sticks out at the front or the back.

If the left crease runs crooked, the **left gripper** lifts the left side and lays it again. If the
right crease runs crooked or the width is not a third, the **right gripper** lifts the right side and
lays it again. If the left side opened while the right side was folded, the **left gripper** runs 4.1 again.

### Step 5: Turn the napkin back over

**Goal:** the **pocket** lies on the work area, the cuff on top, the front crease at the front, the
mouth across the back.

* The **left gripper** pinches the left end of the back edge, through all the layers. The **right
  gripper** pinches the right end.
* The **left gripper** and the **right gripper** lift the back edge, carry it up and over the napkin
  toward the front edge, and lay it down on the work area. The front end stays on the table the whole
  time.
* The **left gripper** and the **right gripper** open and lift away.

**Check:** the pocket lies flat on the work area, one third wide. The cuff is on top, the front crease
is at the front, and the mouth runs across the back. Neither side fold shows from above.

If a side fold opened, the **left gripper** and the **right gripper** turn the napkin back into the
turn space. The **left gripper** fixes the left side fold or the **right gripper** fixes the right side
fold. Then the **left gripper** and the **right gripper** turn it back again.

If the cuff came open, the **left gripper** and the **right gripper** take the cuff's edge at both
ends and lay it again across the middle.

### Step 6: Put the utensils in the pocket

**Goal:** the knife, the fork, and the spoon are all **in the pocket**, handle ends lined up at the
mouth.

Each bullet names the gripper for both configs. Follow the one that matches the table.

* **IF the utensil spot is at the back-left (Config L):** the **left gripper** puts the utensils in.
  The **right gripper** holds the mouth open.
* **IF the utensil spot is at the back-right (Config R):** the **right gripper** puts the utensils in.
  The **left gripper** holds the mouth open.

#### 6.1 Open the mouth

* **Config L:** the **right gripper** pinches the cuff crease near the right end of the mouth, top
  layer only. **Config R:** the **left gripper** pinches it near the left end of the mouth, top layer
  only.
* **Config L:** the **right gripper** lifts it a little, so the mouth opens. **Config R:** the **left
  gripper** lifts it a little.
* **Config L:** the **right gripper** keeps hold until the spoon is in. **Config R:** the **left
  gripper** keeps hold until the spoon is in.

#### 6.2 Put in the knife

* **Config L:** the **left gripper** pinches the knife at its **handle middle** and lifts it away from
  the utensil spot. **Config R:** the **right gripper** does the same.
* **Config L:** the **left gripper** carries it level to the mouth, still pointing front to back,
  eating end toward the front edge. **Config R:** the **right gripper** does the same.
* **Config L:** the **left gripper** slides the eating end into the mouth, low over the bottom layer,
  and pushes it in toward the front crease until the left gripper is just behind the mouth.
  **Config R:** the **right gripper** does the same, until the right gripper is just behind the mouth.
* **Config L:** the **left gripper** lays the knife flat, opens, and lifts away. **Config R:** the
  **right gripper** does the same.

#### 6.3 Put in the fork

* **Config L:** the **left gripper** pinches the fork at its handle middle, lifts it away, and carries
  it level to the mouth. **Config R:** the **right gripper** does the same.
* **Config L:** the **left gripper** slides it into the mouth on top of the knife, tines up, until the
  left gripper is just behind the mouth. **Config R:** the **right gripper** does the same.
* **Config L:** the **left gripper** lays the fork flat, opens, and lifts away. **Config R:** the
  **right gripper** does the same.

#### 6.4 Put in the spoon

* **Config L:** the **left gripper** pinches the spoon at its handle middle, lifts it away, and
  carries it level to the mouth. **Config R:** the **right gripper** does the same.
* **Config L:** the **left gripper** slides it into the mouth on top of the fork, bowl up, until the
  left gripper is just behind the mouth. **Config R:** the **right gripper** does the same.
* **Config L:** the **left gripper** lays the spoon flat, opens, and lifts away. **Config R:** the
  **right gripper** does the same.
* **Config L:** the **right gripper** lays the cuff crease back down, opens, and lifts away.
  **Config R:** the **left gripper** does the same.

Take one utensil at a time. Never pick a utensil up by its eating end, never push a utensil in handle
end first, and never drop it into the mouth.

**Check:** all three utensils are in the pocket: knife, fork, spoon from bottom to top, eating ends
inside, handle ends sticking out of the mouth and lined up. The pocket has not moved and no fold has
opened.

If a utensil went in over the cuff or under the bottom layer: in Config L the **left gripper** pulls it
out by the handle middle, the **right gripper** opens the mouth again, and the **left gripper** puts it
in again; in Config R the **right gripper** pulls it out, the **left gripper** opens the mouth again,
and the **right gripper** puts it in again.

### Step 7: End the episode

**Goal:** recording ends with three utensils in the pocket.

* Look once across the table: the pocket flat on the work area, all three utensils in it, the utensil
  spot bare.
* Return both arms home with grippers open. Homing is the last thing the arms do.
* Stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the three utensils out of the pocket.
2. Check the utensils are clean, dry, and not bent. Lay them back on the utensil spot for the next
   episode's config: knife, fork, spoon from left to right, each pointing front to back, eating ends
   toward the front edge.
3. Unfold the napkin, shake it out, and smooth it flat. Press it if the folds still show.
4. Lay the napkin back flat and square in the middle of the work area, nothing folded under.
5. Replace anything damaged: a napkin that is torn, stained, damp, or has loose threads; a bent
   utensil.
6. Make sure the turn space behind the work area is bare.
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

* **Visible cue:** what the arms do does not match the config on the table: the right gripper puts the
  utensils in during Config L or the left gripper during Config R; the left gripper holds the mouth in
  Config L or the right gripper in Config R; the left gripper or the right gripper reaches across the
  table to the utensil spot; or the wrong IF line is followed.
* **SOP rule broken:** Step 6, the utensil-side rule (in Config L the left gripper puts all three
  utensils in and the right gripper holds the mouth open, in Config R the right gripper puts them in
  and the left gripper holds the mouth open, no arm reaches across the table to the utensil spot, and
  the IF line followed is the one for the config on the table).
* **Coaching note:** look where the utensil spot is before the first pick, then follow that config's
  IF line in Step 6.

**Violation: Wrong order**

* **Visible cue:** the cuff is folded before the half fold; the napkin is turned over before the cuff
  is in; the sides are folded before the first turn; the right side is folded before the left; a
  utensil goes in before the second turn; or the utensils go in in an order other than knife, fork,
  spoon.
* **SOP rule broken:** Steps 1 to 6, half fold, cuff, turn over, left side, right side, turn back,
  then knife, fork, spoon, in that order.
* **Coaching note:** one fold at a time, always in the same order.

**Violation: Half fold done the wrong way**

* **Visible cue:** the back edge is folded onto the front; the napkin is folded side to side or corner
  to corner; the fold is made by the left gripper alone or the right gripper alone; the front edge is
  laid on or past the back edge with no strip showing; or the napkin is lifted into the air to fold
  it.
* **SOP rule broken:** Step 1, the left gripper and the right gripper pinch the front corners, carry
  the front edge low toward the back, and lay it just short of the back edge.
* **Coaching note:** front corners to the back, low over the napkin, stop just short.

**Violation: Half fold crooked**

* **Visible cue:** the front crease runs crooked, the top layer's sides do not lie on the bottom
  layer's sides, or the strip behind the top layer is uneven, and the cuff is folded.
* **SOP rule broken:** Step 1, the front crease runs straight, the sides match, an even strip shows
  behind, and a crooked half fold is laid again before moving on.
* **Coaching note:** look at both sides and the strip. If they are off, lay it again.

**Violation: Cuff folded the wrong way**

* **Visible cue:** both layers are folded together; the cuff is folded under instead of over; the cuff
  is folded by the left gripper alone or the right gripper alone; or the cuff is folded toward the
  back instead of toward the front.
* **SOP rule broken:** Step 2, the left gripper and the right gripper pinch the back corners of the
  top layer only and carry its back edge low toward the front.
* **Coaching note:** top layer only, the left gripper on the back-left corner and the right gripper on
  the back-right.

**Violation: Cuff crooked or not to the middle**

* **Visible cue:** the cuff crease runs crooked, or the cuff's edge stops far short of the middle or
  goes far past it, and the napkin is turned over.
* **SOP rule broken:** Step 2, the cuff crease runs straight and the cuff's edge lies across the
  middle; a crooked or short cuff is laid again before moving on.
* **Coaching note:** edge across the middle, crease straight. If not, lay it again.

**Violation: Napkin turned over the wrong way**

* **Visible cue:** the napkin is turned by its open edges in Step 3 or by its front end in Step 5; it
  is turned side to side; it is lifted off the table and flipped in the air; it is turned by the left
  gripper alone or the right gripper alone; or it is dropped or thrown into place.
* **SOP rule broken:** Steps 3 and 5, the left gripper and the right gripper pinch the two corners of
  one end of the napkin, lift that end up and over, and lay it down on the far side while the other
  end stays on the table.
* **Coaching note:** like turning a page. One end stays down, the other goes over.

**Violation: Fold came open during a turn**

* **Visible cue:** the cuff, the half fold, or a side fold opens or slides out during a turn, and the
  episode moves on without fixing it.
* **SOP rule broken:** Steps 3 and 5, every fold stays closed through the turn; a fold that opens is
  fixed and the turn is done again before moving on.
* **Coaching note:** pinch through all the layers. If a fold opens, fix it and turn again.

**Violation: Side folded the wrong way**

* **Visible cue:** the left side is folded by the right gripper or the right side by the left gripper;
  both sides are folded at once; a side is pinched by the top layer only so the layers split; or a
  side is folded front to back instead of in toward the middle.
* **SOP rule broken:** Steps 4.1 and 4.2, the left gripper folds the left side in to the right, then
  the right gripper folds the right side in to the left over it, each pinched through all the layers.
* **Coaching note:** left side with the left gripper first, then right side with the right gripper,
  through all the layers.

**Violation: Sides not in thirds**

* **Visible cue:** the napkin is not one third wide, the right side does not lie on the left crease, a
  crease runs crooked, or a layer sticks out at the front or back, and the napkin is turned back over.
* **SOP rule broken:** Steps 4.1 and 4.2, the napkin is one third wide with the right side on the left
  crease and both creases straight; a side that is off is laid again before moving on.
* **Coaching note:** right side on the left crease. If it is off, lay it again.

**Violation: Mouth opened the wrong way**

* **Visible cue:** the gripper holding the mouth (right in Config L, left in Config R) pinches both
  layers; it lifts the cuff high or pulls it back so the cuff opens; it lets go before the spoon is
  in; or no gripper holds the mouth open and the gripper putting the utensils in (left in Config L,
  right in Config R) forces the utensils under the cuff crease.
* **SOP rule broken:** Step 6.1, the right gripper in Config L or the left gripper in Config R pinches
  the cuff crease near the end of the mouth on its own side, top layer only, lifts it a little, and
  keeps hold until the spoon is in.
* **Coaching note:** top layer only, just a little lift, hold it until the spoon is in.

**Violation: Utensil picked up or carried the wrong way**

* **Visible cue:** a utensil is picked up by its blade, tines, bowl, or handle end instead of the
  handle middle; it is dragged across the table or the napkin; it is turned on the way; or it is
  carried high or swung.
* **SOP rule broken:** Steps 6.2 to 6.4, the left gripper in Config L or the right gripper in Config R
  pinches each utensil at its handle middle and carries it level, still pointing front to back.
* **Coaching note:** handle middle, low and level, no turning.

**Violation: More than one utensil moved at once**

* **Visible cue:** the left gripper or the right gripper picks up two or three utensils together, or
  pushes a second utensil along with the first.
* **SOP rule broken:** Steps 6.2 to 6.4, the utensils go in one at a time.
* **Coaching note:** one utensil per trip.

**Violation: Utensil put in the wrong way**

* **Visible cue:** a utensil goes in handle end first; the fork or the spoon goes in upside down; a
  utensil goes in under the one before instead of on top; or a utensil is laid on the table and pushed
  in from there.
* **SOP rule broken:** Steps 6.2 to 6.4, each utensil slides in eating end first, low over the bottom
  layer, on top of the one before, fork tines up and spoon bowl up.
* **Coaching note:** eating end first, each one on top of the last.

**Violation: Utensil not in the pocket**

* **Visible cue:** a utensil lies on top of the cuff, under the bottom layer, inside a side fold, or
  out of the mouth on the table, and the episode moves on.
* **SOP rule broken:** Steps 6.2 to 6.4, each utensil goes in the mouth, between the top layer and the
  bottom layer; a utensil that misses is pulled out and put in again.
* **Coaching note:** look for the mouth before you slide. If it misses, pull it out and go again.

**Violation: Utensil not in far enough**

* **Visible cue:** a utensil stops with its gripper well behind the mouth, so it sticks out much
  further than the others, or the handle ends are not lined up, and the next utensil goes in.
* **SOP rule broken:** Steps 6.2 to 6.4, each utensil is pushed in until the left gripper (Config L)
  or the right gripper (Config R) is just behind the mouth, handle ends lined up.
* **Coaching note:** push in until the left gripper (Config L) or the right gripper (Config R) reaches
  the mouth.

**Violation: Utensil dropped into the pocket**

* **Visible cue:** the left gripper in Config L or the right gripper in Config R opens above the mouth
  so the utensil falls the last part of the way, or opens before the utensil is in; or the left
  gripper or the right gripper opens anywhere other than at a let-go point.
* **SOP rule broken:** Steps 6.2 to 6.4, each utensil is slid in and laid flat before the left gripper
  (Config L) or the right gripper (Config R) opens, and neither gripper opens anywhere but at a let-go
  point.
* **Coaching note:** slide it all the way in, lay it flat, then let go.

**Violation: Pocket forced**

* **Visible cue:** a utensil is pushed through a side fold or the front crease; the push drags the
  whole pocket along the table; or the cuff or a side fold is pulled open to make room.
* **SOP rule broken:** Steps 6.2 to 6.4, each utensil slides into the open mouth without force and the
  pocket stays where it is.
* **Coaching note:** if it catches, pull back a little and slide in again. Never force it.

**Violation: Napkin slid on the table**

* **Visible cue:** a pull or a push slides the whole napkin across the table, out of the work area or
  the turn space, or off the table edge, and the episode moves on; or the left gripper or the right
  gripper drags the napkin to put it back.
* **SOP rule broken:** Steps 1 to 5, every fold and both turns stay on the work area and the turn
  space; folds are lifted and laid, not pulled.
* **Coaching note:** lift a little and lay it. Never drag the napkin.

**Violation: Arms swapped roles or crowded the same spot**

* **Visible cue:** the right gripper folds the left side or the left gripper folds the right side; the
  left gripper or the right gripper alone makes a fold or a turn meant for both; the left gripper
  works over the napkin while the right gripper folds alone, or the other way round; or the two
  grippers work the same spot, touch each other, or one has to move before the other can reach.
* **SOP rule broken:** Steps 1 to 6, the left gripper and the right gripper make the half fold, the
  cuff, and both turns, the left gripper at the left end and the right gripper at the right end; the
  left gripper folds the left side and the right gripper the right side; and whichever of the two is
  not working waits clear.
* **Coaching note:** left does the left, right does the right. Neither one does the other's work.

**Violation: Item dropped or something knocked over**

* **Visible cue:** a utensil falls onto the table or the floor; the utensils on the utensil spot are
  knocked apart; the napkin falls off the table; or the two arms strike each other.
* **SOP rule broken:** Steps 1 to 6, each item stays on a clear path, the utensils not yet put in stay
  on the utensil spot, and the left gripper or the right gripper opens only at a let-go point.
* **Coaching note:** check the path and the landing spot before you move.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a utensil outside the pocket or still on the utensil spot, a
  fold open, or the right gripper (Config L) or the left gripper (Config R) still holding the cuff; or
  either arm is away from home, a gripper is closed, or an arm does something else after homing.
* **SOP rule broken:** Step 7, look once across the table, return both arms home with grippers open,
  then stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

These failures are not caused by how the task was run. Log them as system issues, throw the episode
away, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Bad napkin:** a torn napkin, loose threads that catch on a gripper, or a napkin too stiff or too
  small to make a pocket that holds the utensils. Replace it before the next episode.
* **Bad utensil:** a bent utensil, or one too wide to fit in the pocket. Replace it before the next
  episode.

## Annotation subtasks (from SOP)

1. Fold the napkin in half, front to back
2. Fold the cuff on the top layer
3. Turn the napkin over
4. Fold in the left side
5. Fold in the right side
6. Turn the napkin back over
7. Open the mouth
8. Put the knife in the pocket
9. Put the fork in the pocket
10. Put the spoon in the pocket
11. Return both arms home and end the episode
