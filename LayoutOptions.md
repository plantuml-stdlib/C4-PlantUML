# Layout Options

PlantUML uses [Graphviz](https://www.graphviz.org/) for its graph visualization. Thus the rendering itself is done automatically for you - that it one of the biggest advantages of using PlantUML.

...and also sometimes one of the biggest disadvantages, if the rendering is not what the user intended.

For this reason, C4-PlantUML also comes with some layout options.

## LAYOUT_TOP_DOWN() or LAYOUT_LEFT_RIGHT() or LAYOUT_LANDSCAPE()

With the two macros `LAYOUT_TOP_DOWN()` and `LAYOUT_LEFT_RIGHT()` it is possible to easily change the flow visualization of the diagram. `LAYOUT_TOP_DOWN()` is the default.

```plantuml
@startuml LAYOUT_TOP_DOWN Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

/' Not needed because this is the default '/
LAYOUT_TOP_DOWN()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_TOP_DOWN Sample](https://www.plantuml.com/plantuml/png/NP1DJyCm38Rl-HLc7DP9ezKG9quh0y5X7nNhc3XLQUknI6aI9IxLXFZlkDhO454aI_Rhruyz3IGzjOs6UVg-skH5ligAnzLs2MlPE8tYIfbAjpN2diY5-oJniei_5EtRiWteAsi83SMLRH9PUoNDfsvTcypkRZ8j3MqMyqHBma2SAcQibigWZnsF528Pmj8I6CGQQoYnakm9j5S1-DCUeSQTR3N1C17_0AEH41dwO4qawqQPCGpIFgf0NfBrWv5O7m9XKppOrjJI7w9gCeRXSQ_X2Bu4y3iZHHsMXNIEVRPOGkgSLfKaPSs0KxFhCQJhB5u-vTpY4MxZ2IpUPdqjrTfs0VfpCBG5leMJB6aONF4io3j5X1v8DQXvLc2sxnDTHCSY-vnaN1Ilg7-tkc1j0dToVCdpRCsgNdIkNcoUaHYZmpxil6t-japHr7pv7m00 "LAYOUT_TOP_DOWN Sample")

`LAYOUT_LEFT_RIGHT()` rotates the flow visualization to *from Left to Right* and directed relations like `Rel_Left()`, `Rel_Right()`, `Rel_Up()` and `Rel_Down()` are rotated too.

```plantuml
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_LEFT_RIGHT()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_LEFT_RIGHT Sample](https://www.plantuml.com/plantuml/png/PL1DIyD05BplhrZheIdKX8edJusXjaAhfKaLJs6RFEt2Vh7xrb34_-uBhLPmBmDlvhsPsMb0uJ5gnPVvwzEsgfUp-whUFCmN5I-5TWhOXJIDYYtmFQ8BjrdcHPU-Izp7NGpW6siG3AQDrPbelHJcGqKNi-BcQgs4mUrgcIc14916TK5g8Gtur94fO_zSan5ZQ_31caIqMfen7-Gzoe1UeFM34IiF0K7NTpQQLlX3qap6V7WCEnpnJyRf_Vea7UnguHpTUO4TpvrJiX4ehHdGgBWSyxnSfu-pYbOyyEjqmbVFHS_bIjakyBvZu6Wv5NI293egbEJ5gquYWkSeDIZo2fJjwvGkmID9Tquo8ja6r4-hSwnje4t2HLMjIrBreb_sV6OEI34wwE7DM_rtPGgcfU_y1W00 "LAYOUT_LEFT_RIGHT Sample")

`LAYOUT_LANDSCAPE()` rotates the default flow visualization to *from Left to Right* like `LAYOUT_LEFT_RIGHT()` additional **directed relations** like Rel_Left(), Rel_Right(), Rel_Up() and Rel_Down() **are not rotated** anymore.

```plantuml
@startuml LAYOUT_LANDSCAPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_LANDSCAPE()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")

System(S,"S")
System(SU,"S Up")
System(SD,"S Down")
System(SL,"S Left")
System(SR,"S Right")

Rel_Up(S, SU, "Up")
Rel_Down(S, SD, "Down")
Rel_Left(S, SL, "Left")
Rel_Right(S, SR, "Right")

SHOW_LEGEND()

@enduml
```

![LAYOUT_LANDSCAPE Sample](https://www.plantuml.com/plantuml/png/NOzFRvj04CNlV8gjUmYM75kfUkef5ApaG1nae55FQ0sJUANzizeTXAAgtxqpCNQiSa7lDxFllRcFA0EEHeio-_tSDbsPxOewpwgjgANn6f8lolPw740S4NtyiTa4EQtV51x7mnWXzCuYM5ptpcoybfQzRYCEMXqs-VVRYb7xL6wCZ0Y1K9VJ2waiXBMdtIJvFpXT9aa58JgRoi4eknABZFygOf3emcAPrEzaPhgVRhI33EzfVxSIDwU-Dqln9n7qNMBI2GwTz9vyNk0WCk-rwYKgPnU4ygyhaTNLUhTjw4a0yMrz9vv-vJpBj7PJ57nc5EW4tUWbhPXHew8iqKmA4O90PK1JLgHkV-TsAPw6v3ElqJ3PWpvVzLchZH0vxx5fgfgsUEao_RHv08maWN-lmPdh9-VGUhLWULOjIT7wAr8mATnahrZ9h8HNl69xPdlrTiIvTjTwSXTrouNPaHaRVT22A8kPiza7Bucpc3aRdWPx6bpiwyVdbwxSFcntHKho7kmm6lqF "LAYOUT_LANDSCAPE Sample")

## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```plantuml
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_WITH_LEGEND()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_WITH_LEGEND Sample](https://www.plantuml.com/plantuml/png/PL1DJy905BplhrZnG4cm3SQJ9sebO0BOs2Bnr2pjKpRPh-o-sX3ZV_Sr89YubqdUp7ipizE0mcEh5L-cRy-Rije-bOjgEPlFre-y4DefO5VIrAfjWEyHNRXF4Y-w-4FYljsr0Nnj3OB1kBOw4OsNmdogrhL9TdUJAs5mirecIY04f56LaLf80pvsvChOVzjen5WEFbWJYKPBC-Q3j4SPq0kqVZ1YnI4WwEh1jgOH_X3Lap4V7jCEH_oBSNfdewY3NIMSepjRsF7KEILhWTAQ0Osowp5FYpnUpqfQyS1lumbVlMOzbofbky3xae6ZvTJG2PBeLg4aBrvs4X4yHwb1aLUWRD-dT14UIRfpaX79Na3zjhh4sWJQ95oKPLwGgXUTsSkPEI35wA27Ts_rtvKfc8R-ymS0 "LAYOUT_WITH_LEGEND Sample")

Instead of a static legend (activated with `LAYOUT_WITH_LEGEND()`) a calculated legend can be activated with `SHOW_LEGEND(?hideStereotype)`.

The calculated legend has following differences:
* only relevant elements are listed
* custom tags/styles are supported
* stereotypes can remain visible (with `SHOW_LEGEND(false)`)
* **`SHOW_LEGEND()` has to be last call in the diagram**

```plantuml
@startuml SHOW_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")

SHOW_LEGEND()
@enduml
```

![SHOW_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL5Dgzf05DtFhxYr2oDeWgMhhfgceWkreObr6IR9RHsOZs7cXY3b_VTtWpurcqlEn-4Svdia6MWm6ghThtEptsmtnvzGIUCrYa_ATdhe4Iv4FdxBiY37z9-Yoz0E4KFdBA6bj7CcyrhQAMOLgTUgpOglgtA2JeTzPcGa30mr1JkaiXXIpreXIWpHsKJsHjabpFBfgaX1aWkpXQYkR3JD3pVONePhqgsNCBzrco_Wlm3-7f79Y6qZlUUSCxQGUwzL9qavEsEe-Bo4l2hJuwPcIq3uagxXyAUOk5nhDqQO9aKW1xp7IvQOGPFo6g4U5H4686LGAukHkxtTsoLq8pddBcDI_4RziUfPwnJPoNTNrsN5gadqO9ynMwJ8lpYTly6PLujuUQLa8Tu1 "SHOW_LEGEND Sample")

## SHOW_FLOATING_LEGEND(?alias, ?hideStereotype) and LEGEND()

`LAYOUT_WITH_LEGEND()` and SHOW_LEGEND(?hideStereotype)` adds the legend at the bottom right of the picture like below and additional whitespace is created.

```plantuml
@startuml Layout With Whitespace Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(a, "Person A")
Container(b, "Container B", "techn")
System(c, "System C")
Container(d, "Container D", "techn")
Container_Ext(e, "Ext. Container E", "techn")

Rel_R(a, b, "calls")
Rel_D(b, c, "uses")
Rel_D(c, d, "uses")
Rel_R(d, e, "updates")

SHOW_LEGEND()
@enduml
```

![Layout With Whitespace Sample](https://www.plantuml.com/plantuml/png/LSwnReCm40RWtK_XCZbI0qkdJca1jGDjew2A4HdxL91iOzbdjNdx7eb4meJlk_y_SOWe0oPhU2FFSqBUJJZoRfmGefSAU2kjDy0U9gTCqi17H1-VYoB8t_o7icb84OAQ7OB3NCssy4QwvU8-eZRJK9HF--D2tnzDOML424HzIGqvEGYvfonZHmXnTa8-ykpwv2_PZgqfCT1YdVXhHYE26Xs5sZCTjK8HNP-yt5JrfbhTLrVkwpyKG1lwvloMhk_Jx0IcFot_E90gQKmaNR0I98emHRWPWTuObGbWCQybNfYrxrzTtzHlzMSbTkm0JYTh_W40 "Layout With Whitespace Sample")

Therefore a floating legend can be added via SHOW_FLOATING_LEGEND(), positioned with Lay_Distance() and existing whitespace is reused like below.

- `SHOW_FLOATING_LEGEND(?alias, ?hideStereotype): shows the legend in the drawing area
- `LEGEND()`: is the default alias of the created floating legend and can be used in Lay_Distance() call

```plantuml
@startuml Compact Legend Layout Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(a, "Person A")
Container(b, "Container B", "techn")
System(c, "System C")
Container(d, "Container D", "techn")
Container_Ext(e, "Ext. Container E", "techn")

Rel_R(a, b, "calls")
Rel_D(b, c, "uses")
Rel_D(c, d, "uses")
Rel_R(d, e, "updates")

SHOW_FLOATING_LEGEND()
Lay_Distance(LEGEND(), e, 1)
@enduml
```

![Compact Legend Layout Sample](https://www.plantuml.com/plantuml/png/RP7VQ-em5CVVyrUavS9juTwMmPu60vtjtA1JqOqzXfWURLXC9Jbb-j_lr6gri9Ss-Nn_d3OPUPGEcvrXWRRAD2Nm2d7l7zBKoUzagx5greq7fsgBO35HzIxzqavL7gjqSlz_OQJ5ZxSYXGFf9PG4nOJCKbjmoRwjPcm1pjSsalzus2tvE8nPRulM9FGx_XJI5a5LbaoheqVOHOfGj-IJGRGSHBFRQ8z5Vi08IA5tmg_k_DRDbc34ilt6DL4bZV54MvX5H1H1EeWh8r0EsJ8Y02tRbn9Fc0MRnYhKzCT5FirdMHIpm04spl9mOsg9scw5WItOCcG1FIz-jdgPVuhdOZv-VvrDnJbzAObP8OyYqtHzLa6FJ-FlQ2pxouC_7UMFFEm62Eb0XYJzMdssnwGFki_yKZsY8hhK7m00 "Compact Legend Layout Sample")

## LAYOUT_AS_SKETCH() and SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)

C4-PlantUML can be especially helpful during up-front design sessions.
One thing which is often ignored is the fact, that these software architecture sketches are just sketches.

Without any proof

* if they are technically possible
* if they can fulfill all requirements
* if they keep what they promise

More often these sketches are used by many people as facts and are manifested into their documentations.
With `LAYOUT_AS_SKETCH()` you can make a difference.

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_AS_SKETCH()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_AS_SKETCH Sample](https://www.plantuml.com/plantuml/png/NL1DI_D04BxlhvYtxw4fj0aLJvuQGx5Wgy6aYgUmILQxi1_BxeHGnF_kBDLMp6N8pFFnFBiAo3qEMi4sVttSrqrUDTNzkYusK77jb63_fEdKq0iu8BfmasMUZ-cxnCFG3a7upXeK1jFEwimfRgBM8c2lP9iLruiohlQxRQPvGE5frHJ4uD88dph2ClRNE9anLWeVh4buhwMPmoIFKmRq7AsVp5Xr937TtDh1zDmVasuvX-afxtG67mpeEziaesWRxXpfl8WMSkUKx3XAQoQqAlxF8Q_Az65T4yKBk4gNi7ikuYrNoeu1Oiq0Q84wEauGFIYKv0NrA95Q0Kej57a5olRvdIx1qv5qJh0Od3q9zTFg4ciVY4bpKzTbHQW8EbylCdS20_sAEDwyrRyfAs7w-9fV "LAYOUT_AS_SKETCH Sample")

Additional styles and the footer text can be changed with SET_SKETCH_STYLE():

* `SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)`:
  Enables the modification of differnt sketch styles and footer.

The possible font name(s) depend on the output format (e.g. PNG uses fonts which are installed on the server and SVG fonts have to be installed on the client).
Additional is it possible to define comma separated fall back fonts (if the diagrams are exported as SVG. Atm
PNG does not support fallback fonts based on a PlantUML [bug](https://forum.plantuml.net/14842/specify-fall-back-fonts-is-not-working), but this could be fixed in one of the following versions)

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

SET_SKETCH_STYLE($bgColor="lightblue", $fontColor="darkblue", $warningColor="darkred", $footerWarning="Sketch", $footerText="Created for discussion")

' PNG with font jlm_cmmi10 (typically another font is used)
' SET_SKETCH_STYLE($fontName="jlm_cmmi10")

' SVG with fallback fonts MS Gothic,Comic Sans MS, Comic Sans, Chalkboard SE, Comic Neue, cursive, sans-serif (typically without "MS Gothic")
SET_SKETCH_STYLE($fontName="MS Gothic,Comic Sans MS,Comic Sans,Chalkboard SE,Comic Neue,cursive,sans-serif")

LAYOUT_AS_SKETCH()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

PNG with font `jlm_cmmi10`

![LAYOUT_AS_SKETCH with custom style png Sample](https://www.plantuml.com/plantuml/png/VL9TQzim57tFhxZp2ad1JTQnfq6WcGajhCt2xBRqoSZoJQD57qQwMXR6_lkkcgJEO5jUP9rxFiv5kGeaF4MZ1s-KbJgs26kYBdoSJBpOZfyLhMCJ0thfBA6biNHcqcbXa-OYKAjLCoa-N2mJT7ztEp4Y47g6we8LGbdquoxv3yfvLPUVvrLnKvVLq-ryTDOy5quxFysqUbvJeoDcEPojM7V0Zz1MUAliaTqAl_7OxhcEqnxtusbMRf3akXzK-8EcMU5H4BQmSXvQ5MGCGJcRdGy6GrWkhc7BIq9AXM_QrD8OTVaEHhJhb1HQxq1OHslqUueA40EsvtzP9yqNmk0qwttsAUN3COKD6o4tBru1xaguPcybyy8P9Q4KDe4vz5V-NWkzQPpmBPJpusY14NEGqGVrdJy2Coy2UhKwBPuYNIJ8NdEupX3-r_nVZKuA_TddfCwnJLycRNyxU_foNzMpyf0vOco9FZWx4grHDeTibauLo0jodZNbBX2Q-fEBjXL-DvANEGnBOJgDmtFuEG3-lVwxHbjiQj5rxFE83SowJlFwb5wOeU9j3hDoELxCAvPuXFVZIxXxAD9ifhNRlZod3q0Ef3ETO8g9cXHdGRLLHEY1b47DMO6x_Jgq6z5-o3u7MbhsA-hZLdsj-y1AFc-gQbaoYqbzwTxc6Ydm5TEnyiwSIgxGjj7etm00 "LAYOUT_AS_SKETCH with custom style png Sample")

SVG with fallback fonts MS Gothic,Comic Sans MS,Comic Sans,Chalkboard SE,Comic Neue,cursive,sans-serif

![LAYOUT_AS_SKETCH with custom style svg Sample](https://www.plantuml.com/plantuml/svg/VP9lQzim4CRVvrFSl49TS9DrxDKWqCo45jPcONPR-ih8ygNHeZz6EYqBOzzz9vBK6MFB6rbtpptFxr2k0mbFqUZH6sMbZXt2cgWF7oSJBxRZ5qNhsCQ0NZfBQ6aidPdqMjWqSnceqwgTb1ykbwdqS7ytCI8GUYur9Ky8PT6F--G_gkPrKtsUr-LjKzNFT_Fyh7qfdNP-ccdrigPMHymAE5lntA5-B6s5jyeUrPtm6u_TNkiuxMdVdcRL1ackXqQDFsYQbHu5OGShvw5JGSOGbBFPnMXq3il53MnvIKYfy4sRHXgZhjv1JhjUIQ7r3eHrj4Q_bwW0CM1tmRD_BvGK2s5mcWrE-vpgyPZ3bgsG6qZQ0FSLtB2xaaNfZ99G2PkA1GnN_buBlMcTy1rd7biBZ5Y0Z3wex_mHM7aPqAlLANgAT94WUyrXdFzn_uld1ETFcXEO8yk0adQ_cpr_UQYRMNN8pBcsH1-SpKLdb2qWcwLJ1VA2d4-0kq1ecayksaxuNIwl2ZYlXEardb_0pn7mx_NVbM-nRKJViyyJjZ3hUytBKtfXBfLl2vXLo_5YNlE8HtW_leBxnpBrPbgxRNfEfW5o89tf1KjCrAGu2-gj8a8Ff0ngpWhCzkj0bzE-oJu7MLhsA-hZLWFMG-19Fc_hUbcnYaK3z61pWnJuYkbOUMTEHwxHTj7etm00 "LAYOUT_AS_SKETCH with custom style svg Sample")

All available (PNG) fonts can be displayed with

```plantuml
@startuml
listfonts
@enduml
```

## HIDE_STEREOTYPE()

To enable a layout without `<<stereotypes>>` and legend.
This can be enabled with `HIDE_STEREOTYPE()`.

```plantuml
@startuml HIDE_STEREOTYPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

HIDE_STEREOTYPE()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![HIDE_STEREOTYPE Sample](https://www.plantuml.com/plantuml/png/NL1DIyD05BplhrZheIdKX8edJuqrMC5gQ5B5KzWcJxkmN-o-DHJnl_j2gnNtCl1ctfkPdGSK7gDMV7b_MpHLNQoBf_grB7Wbj5F0pgHfLUo0xn1TkCuoB_hqNU8kRcC0trg3O31jhSv4vwKm7ogwc2skBaeb36vM3vaI205fr2n8BQG1dpgoPEoVPp9Xh0GVh4b4fwMPyb4-e0pe1Le_ch1g7n1qSsEZwOJV9-rioiU7gEC9_sIStgzBqiEs4SxHdHVOyjmv9Lk1qfeHZHRdKvvNPVfOrBJYWL-cCxvwNWnShfJj0nyQ1ewMKpqdIAAZGabUlEub8dYEKeCYhq3Plexf4ZoGTESe8vAjGVsqEiNQ1DeaNDPrMP5g4FsofpDtW1IZXm7UlDL_L-PWElhCRm00 "HIDE_STEREOTYPE Sample")


## HIDE_PERSON_SPRITE(), SHOW_PERSON_SPRITE(?sprite), SHOW_PERSON_PORTRAIT() and SHOW_PERSON_OUTLINE()

With the macros `HIDE_PERSON_SPRITE()`, `SHOW_PERSON_SPRITE()` and `SHOW_PERSON_PORTRAIT()` it is possible to change the person related default sprite or person layout itself. `SHOW_PERSON_SPRITE()` is the default.

- **HIDE_PERSON_SPRITE()**: deactivates the default sprite
- **SHOW_PERSON_SPRITE()**: activates the default sprite "person"
- **SHOW_PERSON_SPRITE($sprite)**: activates a specific sprite as default sprite
- **SHOW_PERSON_PORTRAIT()**: activates portrait instead of a rectangle
- **SHOW_PERSON_OUTLINE()**: activates person outline instead of a rectangle

"person" and "person2" are predefined sprites which can be used as default sprite too.

```plantuml
@startuml predefined sprites Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

![Predefined sprites Sample](https://www.plantuml.com/plantuml/png/XOxDIiKm48NtUOfuLrxmDY2kNFLdgr2GhYLjHXj89c5cGb_VH2m8BbpDOVZupkbPB4c9GMS21nyUmMdEv0LOlzcO0wWxZrie3lGkaldP6B97z-bbBsjXe2sX04gtfMXoiDXiDnON_6gcfzlSNilhYucM1QY-tgU4OciJTRcoIir0dF2-oOO7VLdgrSEbfgEM_1scypVVW9zq_QqOJyNuh-An4MUygXxGrK5V "Predefined sprites Sample")


**Using HIDE_PERSON_SPRITE()**

```plantuml
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

HIDE_PERSON_SPRITE()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![HIDE_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL1TgzD047tVNp7MXvj2Ry8LdtowCGPRi3KqgJw6JJBQXVrOTYU48lvtPsbj1VCoPCwPyx6laMIWsMZOxZxLVLCVsw-7lcsEkww6LXglKRnHTjJpX70cyl53KGIvv3yLdUTXZXX6PmajvQCpXTVI9hNdI9DMGr6zVsxIwhJ_KXWP2GEl-eelfB8OSizS8VwtpjP2D1YYivcSZB8RM9LfgaX1aWkhjMWlaT3q7zri9naksVYoWQThugSr_1B0tzqeMt3efVUiynq7ABtNQfIad5tngdgxWR9jyaFTyKb0U9U_mFvRbR1IQxT4I4KZa0DkwILJpAn9iHTqYoB20AGCQlQAdEttBLr6Lv1rRZG6nH7rtrQFMAU8CVbjkwvfcPL8T_GXynafyY-cyICuy-_9AzeflUSV "HIDE_PERSON_SPRITE Sample")

**Using SHOW_PERSON_SPRITE()**

```plantuml
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

/' Not needed because this is the default with sprite "person" '/
SHOW_PERSON_SPRITE()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![SHOW_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL5DQzmm4BthLqpTWxsmiKdfgQUuPcaApSQidUPeP6lI5UX3I6DCAFtl7JLfjb1V1i-yz-QzqKqY6Mcr1eRR-yUfFvo6--CqzAUlum46QOD1yKwxnQmAuKmKqgUcYNAhVsWwh_EQC2xU4Jgg5s-ROAJBQbU9bD5pqtsywdFhuUvROsKYZDoQEcP8xJ3MWR52D2KSFO53LAXWnaMoBj1P9z29AuB29xaQWestGWfH4q8HC2Rl2YWRyR_vQYT4_mTGIMMrsqFHvgeJHKa-5ZinFBCXEttsgrCoFbVBzHxAbypb3duAuE_DQhNXFCaGMESHPsX3C7gHfDa0jxhtUsY7lZuUHgP4X0_rDTnzx_AiDSPl2VAf4f07lbEG3B4SIFCk63aLOGJI5WtlIkpjrwkxYbw6hFCAuw4ueVcRwcBh8J6Jw-quzWEZCkXjUf7vWfJu5tDvYjx-Ixb1f_AB_0O0 "SHOW_PERSON_SPRITE Sample")

**Using SHOW_PERSON_SPRITE(sprite)**

```plantuml
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
!define osaPuml https://raw.githubusercontent.com/Crashedmind/PlantUML-opensecurityarchitecture2-icons/master
!include osaPuml/Common.puml
!include osaPuml/User/all.puml

SHOW_PERSON_SPRITE("osa_user_green_architect")

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![SHOW_PERSON_SPRITE(sprite) Sample](https://www.plantuml.com/plantuml/png/ZL1DQzj04BthLspTGnIm9H9wwYckC4sXIOGbDqUnbYRnmduiCxCOK_hVEzieTkcfkYmpx-EzqHsnHaxE5X-C7ssQG1sO8tskQzJ7wjNm8UqJ0Ox1CtYknk3gQBNFcXNnPCs-RZwjshpQFNoldIO6bDNGY48R3rZ5F_uJlCYa0kbMvl-8QL3J0IPd_5I_-wz214ym9ZHyqZWU3CF82U5sPKHBS_xbcZckRe9pmSzL_WLtabnhQz_Wehj_UXxQpRPxUXowTlkjtvGBeGwvuF2A07uuHo-kYw85fE1BdQikrMATNqECcWCAtfs8mGrVGlAJnbCvtYpLLQTTj71rhNuMIhxppogFi1zqZEBp37krZj6QKRC9VY6hvkDIhRksUjpq8a5GjzMDUlZHP6njRJYIoYL9SL1ZS54BnINBHh9KVpJCW8gD0ojP9Dr-pUrAVWF5PwRbmxPWtw-wrDeHKCwxx_ks4rOcdT6BpLTWaX7oyuB1_Isv0pybPty3 "SHOW_PERSON_SPRITE(sprite)")

**Using SHOW_PERSON_PORTRAIT()**

```plantuml
@startuml SHOW_PERSON_PORTRAIT() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

SHOW_PERSON_PORTRAIT()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

' if a person is combined with a sprite then the rectangle layout is used again
Person(person, "Person with sprite", $sprite="person2")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![SHOW_PERSON_PORTRAIT() Sample](https://www.plantuml.com/plantuml/png/RL1BQzj04BxhLqpTGcHm919wAXIYcj0KcbXOIdCKAsbYB-nZsPd5cDB_tbcKHm_LGRixyptccnjY5JbP0ztTxcbeR_VTxc5eT_j-t_peopLqoWQ3nGVj9fDcX2Dpe2zr7TMfEcW-fZ4HniaxHiVLv6qTZ79PyP9uDdgijvylsrnwlFzPMqMCKKh3LXXAEunL46nH_D--A5gCv5sfPglT1bPDFZLnLEpZQbrqPsAqmpUVtApYkPokDd2np7onXjy5oFTcLPvm75G8elE48pGX63qfrjwjfBJzk86cQwk7srue4U6wkeBxNzlSQupn9u8SbO0zICwW16AJOIrUq9yqCqPWRT685ybiVrwcAtbfYiuBJ9h51UXdK10mvmDDMNCKvWo2EKg7GjICm4Tq-GSH9rRk86P6dNtYp4aaU7MGTA-BMlJ4QdalOekK1FcqtBwk5jXr7cIFvdMzx_jv9AGS_AxlsqvG6VJMVS_p7PdaYVbuZjx-Ixb1DoTh_W80 "SHOW_PERSON_PORTRAIT()")

**Using SHOW_PERSON_OUTLINE()**

> This call requires PlantUML version >= v1.2021.4!

```plantuml
@startuml SHOW_PERSON_OUTLINE() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

SHOW_PERSON_OUTLINE()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

' if a person is combined with a sprite then the rectangle layout is used again
Person(person, "Person with sprite", $sprite="person2")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![SHOW_PERSON_OUTLINE() Sample](https://www.plantuml.com/plantuml/png/RL5BQzj04BxhLqpTWcLm919wAXJY6jCK4bj4SdCK8sbYB-nZsHqXJEb_xopAeuVeeDNEV8_vHhUHCV1eDDHtXwUssZtMXtrxE3Rtl_QxV0Kr6gyf-wHihyU1uCpiuxUo33WL9yNdiHiZXTvP9ij5xqpfDTeaU1LvqAehjr-lgbGwFjoN1YDJa5Ax5GOgIw7mWiso3zsphA8GdSrnCCgkOR59fueSa5rOhBBw8dgc_U56Es2uvFtr6fRpoCiL_Cb0dZUdVAAkHUz5vuaws7YlLO-id5r8QVjv3PkwAlQxHYY1uAQuXeVVszJRQEsc22bf17OWCJqAn8oQbNX1CocMOC3Aa1QlABFzVPakvxafEYymQMPBKC-0u2db0nMJPYVC0GHpbaxqGJ41dycc5mJg6Ur9p3HUtCY9CqR1uqdIlIvgrXEh-JwBpL8IvClyzNqnmsxI88-aNzVxlfzZb0XotZLDLGigWTwwxtb-4aUvKZgUWpF_Ksx93kdF_WC0 "SHOW_PERSON_OUTLINE()")
