Heyya!
i conducted a research during my masters program on the various noise-models in mobile environments to simulate the behaviour of these noise models under both static and adaptive privacy amplification.<br/>
<hr>
Upon conductiing these research i was able to confirm that the Gaussian bosonic performed poorest hwereas the phase flip was the best interms of privacy amplification in quantum noise channels. kindly feel free to probe or review what i have done and also add to this existing body of knowlege.

i dont mind if you can fork my repo and continue the study.
My reasearch is the first to state that the gaussian bosonic is the weakest and the phase flip is the bestb in terms of prvacy amplification in quantum channels, this is the novelty of the research conducted.
<br>
<br>
What the Results Show (Noise Monsters One by One)
1.	Bit-Flip Monster (X):
o	Errors grow smoothly as noise gets bigger.
o	At first, mistakes are few, but past a “knee” (about 8–10% noise), mistakes blow up fast.
o	Randomness drops steadily → fewer secrets to keep.
o	Adaptive method (smart fixing) works well when noise is small, but when noise is big, both methods end up the same.
2.	Phase-Flip Monster (Z):
o	Looks like no errors at all (QBER = 0).
o	But that’s sneaky! The mistakes hide in another “secret test mode” (the X-basis).
o	If you only check one side, you think everything is perfect, but spies actually know more than you think.
3.	Bit-Phase Flip Monster (Y):
o	This is the nastiest one — it messes up both the bit and the phase.
o	Errors rise quickly, and secrecy drops super fast.
o	Adaptive helps only at very tiny noise; past 9% noise, both methods collapse.
4.	Depolarizing Monster:
o	Like rolling dice — random mix of all errors.
o	Errors rise steadily but not too harsh.
o	Randomness drops evenly.
o	Adaptive is useful until ~15% noise, then drops to minimum secrets (~256 bits).
5.	Amplitude Damping Monster:
o	This one pushes “1s” into “0s” (like messages always fading into silence).
o	Errors grow slowly at first, but secrets still shrink.
o	Adaptive helps until ~12% noise, then both methods level off.
6.	Generalized Amplitude Damping (Hot Monster):
o	Similar to damping, but sometimes “0s” jump up into “1s” too.
o	Same story: adaptive helps at first, then crashes after ~18% noise.
7.	Phase Damping Monster:
o	Looks perfect (QBER ≈ 0), but secretly ruins the hidden phase.
o	If you don’t check with the X-basis, you think it’s fine but you’re tricked.
8.	Non-Markovian Monster (Memory Monster):
o	Sometimes it’s noisy, sometimes it suddenly gets clean again.
o	Errors go up and down like a roller coaster.
o	Secrets don’t fall smoothly but in steps — sometimes Alice and Bob get lucky breaks.
9.	Collective/Correlated Monster:
o	Errors come in bursts, like the monster attacks a bunch of bits at once.
o	This is harsh — adaptive only helps a little at the very beginning; then everything drops to minimum secrets quickly.
10.	Gaussian Bosonic Monster:
•	Like static fuzz on the radio.
•	At first, not so bad — then suddenly BOOM! errors explode.
•	Randomness crashes to almost nothing fast.
•	Adaptive helps only in a tiny low-noise window.
11.	Polarization Mode Dispersion (PMD Monster):
•	Imagine your walkie-talkie twisting words slowly.
•	Errors rise, sometimes dip a little when things line up, but then rise again.
•	Secrets drop step by step and collapse around 18% noise.
12.	Photon-Number Splitting Monster (PNS):
•	Sneakiest one — doesn’t add errors at all!
•	But secretly copies part of the message to the spy.
•	QBER looks perfect, but secrecy is actually broken if you don’t measure carefully.
________________________________________
Super-Simple Takeaways
•	More noise = more mistakes = fewer secrets.
•	Smart adaptive fixing helps when things are not too noisy, but once noise is too big, both smart and static methods end up at the same safe minimum.
•	Some monsters are sneaky (Phase Flip, Phase Damping, PNS): they look harmless but secretly leak secrets.
•	Worst monsters: Y-noise (hits both sides), Gaussian noise (explodes fast), and Correlated noise (attacks in bursts).
•	Best survival strategy: Always check both “views” (Z and X basis), adapt fixing when possible, and expect to give up extra bits when noise is high.
