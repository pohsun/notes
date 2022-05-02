#Private 

# Ph.D Defense: Presenter Notes

[<<< Slides >>>](https://www.icloud.com/keynote/0PXt3U4wGlZLag-4gAtkH1cmA\#pchen_PhDDefense)

$B^{+}$介子衰變到 $K^{\ast+}(892)\mu^{+}\mu^{-}$的角分佈分析 -- 使用2012年CMS質心質量8TeV質子對撞資料

---
# The CMS experiment

---
# The b to sll

## Motivation 1

* B meson decay to $K^{\ast{}}\mu{}\mu{}$ is a typical FCNC process. In SM, such decay is mediated by EWK penguin and WW-box diagrams as shown in the plots

* By introducing additional terms from NP to the loop diagrams, the characteristics of the decay might be changed. Hence the loop serves as a good candidate for indirect search for NP.

    * If there's any NP, the energy scale could be labelled by q2.

## Motivation 2

* There are two anomalies seen from B0 to KstMM.

    * One is 2.7 sigma muon forward-backward asymmetry by Belle in 2009. This is interesting since the trend has no zero-crossing point, which is not compatible with SM prediction. 
        * But this anomaly is gone with new LHCb result in 2013.
    
    * But the LHCb result also introduced the 3.7 sigma anomaly in form-factor independent P5' measurement. Cross checks by Belle, ATLAS, and CMS are done but there is no conclusion so far.
    
*  Anyway, some interesting stuff may hide behind the b to sll loop at low q2 scale. Due to isospin asymmetry, it is expected to see some effect in charged B decay channel as well.

----

## Data and Simulation

* Let's start with the basic materials.

* For the data, pp collision at CM energy of 8TeV collected by CMS in 2012 is used, the corresponding luminosity is 19.98 /fb.
    * As a rough selection, we focus on DoubleMu3pt triggered events to ensure a dimuon vertex at low mass region.

* For simulation samples, 
    * B+ is produced with PYTHIA and EvtGen force the decay.
    * For signal channel, around 1900 times as the data size is generated.
    * While for the background, naively the $B\to J/\psi K^{\ast}$ and $B\to \psi'K^{\ast}$ decays are considered. They're named as peaking background in the presentation.
    * We also look into $J/\psi + X$ inclusive sample in case of any other background from some B decay.

## B+ candidate Reconstruction

* Here's how a B meson candidates is build. The B meson decay chain could be read from left to right, for reconstruction, we start from right to left.
* A two step vertexing strategy is used.
* In the first step we build Kshort from opposite charged pions, and picked the candidate which is has Kshort mass and away from beamspot.
* In the second step, two muons, a pion track, and the Kshort candidate are fitted to a B vertex.
    * For the muon and dimuon part, the cuts are based on the 2012 soft muon selection and the trigger conditions. Slightly tighter cut points prevent us from turn-on effects. There's also a loose colinearity cut $\cos{}\alpha_{BS}$ applied to the dimuon candidate.
    * The vertexing probability for a good B candidate is required to be greater than 1%, and the invariant mass of refitted Kshort-pion system have to be consistent with a Kstar.

## Resonance rejection
* For the treatment of peaking background source, as you could see in the upper left plot, the X-axis is the dimuon mass and B candidate mass servers as the Y-axis. We have a huge contribution from peaking background. The projection on dimuon mass in the colored signal region around the two resonance is shown below.
* Thus, on the top of preselection, the event-by-event resonance rejection cut is introduced to distinguishes signal from background. However, there seems to be still a tail from $J/\psi K^{\ast}$ channel.

## Anti-radiation

* For convenience, the scatter plot with resonance rejection cut shows up again at left hand side, the spectrum below is the projection on B mass. The radiation tail is quite clear.
* So, here comes the so-called anti-radiation cut, which, as you could see on the top right plot, wipes out a slanted area. The radiation tail is removed as shown in the dimuon mass plots.
* The B mass spectrum with AR cut applied will be shown in the final fit.

## Optimized cut

* Additional selection criteria is optimized with FOM scanning.

* Given reasonable signal-to-background ratio and sufficient signal MC sample. The FOM is chosen as S over sqrt of S+B. S stands for expected signal yields estimated from signal MC, while B stands for the background yields estimated from data sidebands.

* The scanning plots are provided in backup slides, here we show only the optimized cut value.

## Lambda_b free

In this plot, we could see tiny contribution in peaking region from possible Lambda_b contamination. It's is safe to merge it into combinatorial background.

## Data-MC comparison

* Here we show data-MC comparison of some kinematic properties in the $J/\psi$ control region. In general a nice agreement is presented. We're confident with the estimated properties from MC samples.

----

## q2 Binning

* In order to reveal more information in the loop, events are categorized with the dimuon mass squared, or q2, which directly connects to the mass of intermediate particles.

* The definition of q2 bins is inspired from the $K^{\ast{}0}\mu\mu$ analysis. However, due to limited yields as we'll see soon, less bins are used in the range of interest.

* Out of the 5 bins, the measurement is performed in only non-resonance bins, since the theoretical prediction is invalid with the presence of resonance.

## Coordinate and Observables

* Tha decay could be described by 3 angles, $\theta_{K}$, $\theta_{l}$, and $\phi$ as defined on the plot.
* Assuming negligible dependence on $\phi$, the differential cross section is described as a function of $cos\theta_{K}$ and $cos\theta_{l}$. The formula is parametrized with $F_{L}$, $A_{FB}$, $F_{S}$, and $A_{S}$.
    * In particular, $A_{FB}$ and $F_{L}$ reflects the physics in the loop.
* S-wave contribution is expected to be tiny from the neutral B experience.
* P-wave term has to be non-negative, which lead to a triangular allowed space.

### Fit model

* Here's the full model for final 3-dimensional extended ML fit to mass spectrum, $\cos\theta_{K}$ and $\cos\theta_{l}$. 

* The first line in the formula is the signal part, the mass spectrum and angular axes are confirmed to be more-of-less uncorrelated. 

    * For the mass spectrum, $S^M$, it's modeled with a double Gaussian with shared mean. It is determined with signal MC and then fixed in the 3-D fit.

    * Angular part is theoretical as introduced earlier, 

    * And there's an angular efficiency correction term to extract pure physics information from detector effects.

* The second line is the combinatorial background part, all three axes is assumed to be uncorrelated.

    * Mass distribution is a free float exponential function to be determined in the 3-D fit.

    * While the angular distribution is modeled with some analytic models fixed from data sidebands.

* No background terms from peaking background is considered since the estimated yields from MC is negligible.

### Efficiency 1

* Let's look into the components one-by-one.

* Here's the efficiency map determined from private and official MC. Private MC is generated with exactly the same coefficients as the official MC, the only difference is that the generator level pt and eta filters are removed so that acceptance could be measured. Then we multiply the acceptance with reconstruction efficiency to form a measured efficiency.

* The modeling of smooth efficiency map is performed in 2 steps.

    * In the first step, the correlation term, C is set to zero, and the PDF to individual axes is decided.

    * Then the two PDFs are fixed, the second fitting is applied to tackle with the correlation and overall normalization.

    * Correlation C is verified to be small.

* Bad match between fitting and measured is visual effect.

## Efficiency 2

* It's always hard to see if a 2-D model is fine or not, so here are the 1-D projection of the map.

## Efficiency 3

* And also the ratio of fit model to the measured efficiency. In general we have extremely good modeling.

## Closure test

* To verify this efficiency modeling method, we built the efficiency map in $J/\psi{}K^{\ast}$ CR, and generate the expected angular distribution from the map and unfiltered private MC.
* Good consistency is seen between sideband subtracted data and MC.

## B mass fit regions

* Before introducing the result of signal shape and background angular shape. I have to define the signal region and sidebands in the mass spectrum.

* The nominal fit range is 4.76 to 5.80 GeV, a large sideband region is included for a more stable background description.
    
    * In fact, the efficiency map is confined also in this region.

* The sideband data, those data points in the orange area, are used to determine the angular distribution of background.

## Signal shape in B mass

* So, here are the signal shapes. They're fixed in the 3-D fit.

## High stat validation

* Given all parts for signal term is at hand. We test the validity of fitter with signal only PDF.
* The bias of $A_{FB}$ and $F_{L}$ values between RECO and GEN level information with large statistics is tiny. This bias will be quoted as a source of systematic uncertainty.
* The impact from $\phi$ is proven to be negligible.

## Ensemble test

* On the other hand, the behavior with low statistics is also studied with randomly picked subsamples. The distribution of measured value centers at the desired mean with reasonable shape. Some deformation due to hitting physical boundary is confirmed.

## Combinatorial background shape in angular axes

* Then we show the combinatorial background distribution. The data points on the plots comes from only the symmetric sidebands around the B mass peak. The shapes are also fixed in the 3-D fit.
* There were a lot of alternative method to define the shape. In the end, we still have no sufficient information to know if the shape depend on B mass or not. A post-fit cross check will be shown soon to validate this method in the signal region. 
* Now we have all needed components ready.

## Ensemble test with background

* Before moving to the final fit. We fit to cocktail toys to validate the fitter with the presence of background term. The cocktail toy consists os randomly picked signal MC events and pure toy background.

* Still we have good agreement, and, as expected, additional uncertainties introduced by background.

## Final fit: Bmass

* The projection on $K^{\ast{}}\mu{}\mu{}$ spectrum of the 3-D fit is shown here.

    * The background distributions are finely described with exponential function.

    * The signal peaks are clear, however the yields is limited.

* We successfully find the central value but always fail to see statistical error from usual `MINOS` approximation. We'll come back to this point soon.

## Final fit: cosThetaK

* Conti. with previous page, the projection on $\cos{}\theta_{K}$.

## Final fit: cosThetaL

* And then the projection plots on $\cos{}\theta_{l}$.

## Post-fit: cosThetaK

* To be more careful, here are the post-fit plot in signal region projected on $\cos{}\theta_{K}$. 

* The normalization of each components is scaled based on the integral.

* Good match in post-fit plots validates the background angular distribution derived from sidebands.

## Post-fit: cosThetaL

* The same plots projected on $\cos\theta_{l}$

----

## Stat uncertainty

* Now we're back to statistical issue.

    * The commonly used method works based on asymptotic property of likelihood fit, however, the low yields violates the assumption. Hence may not be a proper tool.

    * In addition, the procedure may still hit the physical boundary while looking for the uncertainty for $A_{FB}$ and $F_{L}$. This effect is common  in the low stat case when a mean value is close to the boundary.
    * "Anything could happen" in low stat.

* Statistics committee suggested us to run **profiled Feldman-Cousins' method** to make reasonable estimation. In a nutshell, F-C method is a frequentist method based on Neyman-Pearson confidence belt with likelihood ratio ordering.

## Neyman construction



## Interval building



## Profiled toy production

* On the top of ordinary F-C method, **profiled** method is suggested to handle the uncertainty from nuisance parameters. It simply takes profiled fit result in toy generation step.

* For example. If we want to generate toys with true $A_{FB}$ of 0.3. We run the fitter with $A_{FB}$ fixed to 0.3 to profile the nuisance parameters, and then generate toys with profiled fit results.

## F-C result: FL

* Here's the confidence belts of $F_{L}$ for each bin. Dashed line is the central value measured from fitter. The statistical uncertainty ranges in the crossing points between solid and dashed lines.

    * For each "true value", 500 sets of toys are generated to build the belt. It seems 500 sets is sufficient to create a stable belt.

    * As you could imagine, the belts deform as the measured value is close to the physical boundary. With the help of such feature, the estimated uncertainty sits always in the physically allowed region.

## F-C result: AFB

* Then here are the uncertainties of $A_{FB}$.

## Coverage test

* To ensure we're in the right track, it's strongly suggested by the experts to perform a coverage test to ensure the correct implementation of F-C method, which tests if the derived error bar covers, in our case, $1\sigma$ or not.

* We used 2000 sets of toys to run the test, and there's no underestimation.

    * Overcoverage in the case of low stat or close to boundary is studied and known effect of F-C method. It doesn't mean there's something wrong, just reflects the fact that F-C method is a conservative strategy.

----

## Syst Unc 1

* DONE with statistical part. Let me talk about uncertainties.
* Follow the bullets.

## Syst Unc 2

* Follow the bullets.

## Syst Unc summary

* Here are the summary of systematic uncertainties obtained from each source.

* Main contributors varies bin-by-bin.

    * Follow the bullets.

* In general, the measurements are dominated by statistical uncertainties. Systematic uncertainties are relatively small.

## Result

* We summarize the analysis result in this page and compare with the SM calculation.

    * There are 2 horizontal bars at each side of the vertical error bars, the inner one represents statistical only error and the outer one represents total error.

    * For the SM prediction, There's no prediction in the 3rd bin since the calculation procedure is not valid where there's a resonance.

* We're in agreement with the SM predictions.

## Summary

* In a summary...

----
# Pixel upgrade

I really have to thank to my colleague Yu-Wei Kao, who shared part of the task and took a lot of good pictures.

## The upgrade plan
* The LHC is planned to run for decades, and it is upgraded from time to time to reach higher energy and luminosity. The accompanied detectors have to upgrade their parts to cater to the environment. The phase-1 pixel upgrade is planned in 2000s to work in LHC Run-2 environment.
* The new pixel detector has additional layers in both barrel and endcap as shown in the figure. NTUHEP participate the pixel module production task for barrel layer-3.

## The module

* Here the **parts breakdown illustration** of a module, we first look at the bare module

    * The bump-bounded silicon sensor and ROCs is the core of the module. When a charged track fly through the reversely biased silicon sensor, electron-hole pairs are created and the drift current could be measured. The current is recorded in the buffer of corresponding ROC for later data collection.
    * The High Density Interconnect is wire-bounded to ROCs. It's is responsible for offering bias voltage to silicon sensor, power supply to ROCs, and collecting data from ROCs.
    * The bare module together with the HDI are glued to the base strip and fixed to a holder. The holder and the base strip are good conductor so the module could be cooled to a stable working temperature.

## X-ray calibration

* I was assigned to setup and run X-ray tests, which includes calibration, property measurement under exposure, and efficiency measurement.
* Let's begin with calibration. It determines the relation between the calibration voltage in analog unit and the energy deposit.
* The calibration takes advantage of characteristic spectrum of secondary emission produced from metal targets.  The emitted photon at certain energy converted to corresponding number of e-h pair in pixel, so the measured pulseheight will be a peak. So the desired relation to the measured pulse height could be decided.
* The setup is shown in the figure. A module is fixed a L-shaped cooling frame. In the center of the box, the metal targets are on the 4 faces of the cube. The cube is mount on the goniometer. By rotating the cube, the target metal is altered so the measurement could be done in on run.
* There could be some noisy pixels so the result spectrum is not clean, in such case, those noisy pixels are masked to prevent from biasing the result.

Zinc, Molybdenum, Silver, Tin
## High rate test 1

* The property under exposure is also measured. The metal targets are removed and the modules are rotated by 90 degrees to have direct exposure from the X-ray source.
* The rate of ...

## High rate test 2

## Summary



