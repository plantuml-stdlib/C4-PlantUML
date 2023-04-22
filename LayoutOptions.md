# Layout Options

C4-PlantUML comes with some layout options.

- [📄 C4-PlantUML](README.md#c4-plantuml)
- [📄 Layout Options](#layout-options)
  - [Layout Guidance and Practices](#layout-guidance-and-practices)
    - [Overall Guidance](#overall-guidance)
    - [Layout Practices](#layout-practices)
  - [LAYOUT_TOP_DOWN() or LAYOUT_LEFT_RIGHT() or LAYOUT_LANDSCAPE()](#layout_top_down-or-layout_left_right-or-layout_landscape)
  - [LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype, ?details)](#layout_with_legend-or-show_legendhidestereotype-details)
  - [SHOW_FLOATING_LEGEND(?alias, ?hideStereotype, ?details) and LEGEND()](#show_floating_legendalias-hidestereotype-details-and-legend)
  - [LAYOUT_AS_SKETCH() and SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)](#layout_as_sketch-and-set_sketch_stylebgcolor-fontcolor-warningcolor-fontname-footerwarning-footertext)
  - [HIDE_STEREOTYPE()](#hide_stereotype)
  - [HIDE_PERSON_SPRITE(), SHOW_PERSON_SPRITE(?sprite), SHOW_PERSON_PORTRAIT() and SHOW_PERSON_OUTLINE()](#hide_person_sprite-show_person_spritesprite-show_person_portrait-and-show_person_outline)
    - [Using HIDE_PERSON_SPRITE()](#using-hide_person_sprite)
    - [Using SHOW_PERSON_SPRITE()](#using-show_person_sprite)
    - [Using SHOW_PERSON_SPRITE(sprite)](#using-show_person_spritesprite)
    - [Using SHOW_PERSON_PORTRAIT()](#using-show_person_portrait)
    - [Using SHOW_PERSON_OUTLINE()](#using-show_person_outline)
- [📄 Themes](Themes.md#themes)
- samples
  - [📄 C4 Model Diagrams](samples/C4CoreDiagrams.md#c4-model-diagrams)

## Layout Guidance and Practices

PlantUML uses [Graphviz](https://www.graphviz.org/) for its graph visualization. Thus the rendering itself is done automatically for you - that it one of the biggest advantages of using PlantUML.

...and also sometimes one of the biggest disadvantages, if the rendering is not what the user intended.

### Overall Guidance

1. Be minimal in the use of all directed relations - introduce the fewest possible directed `Rel_` and `Lay_` statements that achieve the desired layout. One way to do this is to immediately remove any of these you experiment with when they don't actually affect the layout at all. And of course you will remove the ones that affect it the layout in a negative way.
2. With dynamic rendering tools (e.g. VS Code plugin) do NOT trust the first rendering as it is shifty when adding code because you do not know exactly when it grabs the current unsaved code. Wait for a bit or close and reopen preview panel.

### Layout Practices

These are intended to correlate to the layout engine’s algorithm, but have (as of this writing) been determined by trial and error - not a code review.

Please read through all practices before starting.

1. Create all components, containers and boundaries first - in order top to bottom or left to right.
2. Use `Rel` (directionless) to create initial relationships.
3. If layout is not as desired, modify **some** Rel statements to contain direction `Rel_{direction}` to force shape layouts.
4. If the layout is not as desired, sparingly add `Lay_{direction}` to force any layouts that `Rel_{direction}` does not correct.
5. For both `Lay_{direction}` and `Rel_{direction}` statements used above:
   1. Exhaust attempts to get a working layout with `Rel_{direction}` before adding `Lay_{direction}`
   2. Try to introduce the fewest possible directed statements (of either type) that result in the desired layout.
   3. Immediately back out any directed statements that do not change the layout at all.
   4. Order inner objects first when it creates the desired result (enclosing objects tend to follow suit when child objects are ordered).
   5. When ordering multiple objects, only specify one relationship and, if possible in the same direction. For example if you want entity1 => entity2 => entity3, then `Rel_R(entity1,entity2)` and `Rel_R(entity2, entity3)` is the minimum possible statements and they all specify the same direction.
   6. Try NOT to apply directed statements to both inner elements and enclosing elements to force relationships that aren't working out.
   7. Make all orderings at the same nesting level whenever possible.
   8. Do NOT create duplicated, opposite direction statements in an attempt to force or ensure relationships as it does not affect the results. For instance if you have `Lay_R(entity1,entity2)` which is not working as desired and then also add the opposing one as `Lay_L(entity2,entity1)` - it does not help with forcing layouts to be as you want them. It might help to use `Lay_L` **instead of** `Lay_R`, but not both together.
6. Do not create an "All enclosing" boundary - the code for processing relationships seems to struggle with relationships inside this. Additionally, `SHOW_FLOATING_LEGEND()` will not display inside the All enclosing boundary.
7. Legend statements must come after at least one usage of each of the elements you want the legend to contain.

## LAYOUT_TOP_DOWN() or LAYOUT_LEFT_RIGHT() or LAYOUT_LANDSCAPE()

With the two macros `LAYOUT_TOP_DOWN()` and `LAYOUT_LEFT_RIGHT()` it is possible to easily change the flow visualization of the diagram. `LAYOUT_TOP_DOWN()` is the default.

```plantuml
@startuml LAYOUT_TOP_DOWN Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![LAYOUT_TOP_DOWN Sample](https://www.plantuml.com/plantuml/png/JL1BIyD04BxdLuprq1JQn1RnuAanYXxw23QrU0gRP6eNDhlBxiHGnF_k16lhiZ0mtsE-cRaduQXjL70bTQNQ6k50PFrz73lHHH-I3ctPUdILqOIQeieqiLL2zvg9frh9Cavl9rdVsYuNyUSikejkk5Mah11Ieujixn_4GrWP0erOOmqbLe9zWGxI0tyw8DIu5wqY6CR18dbVR_CYNsV5utgt2aT1aA7pHeUYRgGUmo3fg_Ja11at60MReoTiYWVJwbguOrXDnp3SYCOg78xWAm1-vqXXXsKXh6MV7PQGMAja9KWQFU1MUZs6P9D5gwUS9GvX5arX-PRsMAAKwJpq9-7G1lWULZ2buU2IPq7UII9qGB91nRCyP_i-fGlf5sIV4ut1u1NLtrQNM5lFIgulUPvjcDMJpkZ5vXc9OtJObxqppN_977NDb_y1 "LAYOUT_TOP_DOWN Sample")

`LAYOUT_LEFT_RIGHT()` rotates the flow visualization to *from Left to Right* and directed relations like `Rel_Left()`, `Rel_Right()`, `Rel_Up()` and `Rel_Down()` are rotated too.

```plantuml
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![LAYOUT_LEFT_RIGHT Sample](https://www.plantuml.com/plantuml/png/JL1BJy904BxtLwnue2JGYZ4UF54R11FG1eh6KxDjHzbaNzcTsX3ZVtSs8hYNIUPxpiuySeUTaj65q8tiMc1xHEllqjJnFlaGkE_gpeDhZ4RGc3H6fLPo7JGJZwqKTPhVJ8gmsgrNwUTrSfjSqQhAIS651fVOu1-jihVdNLcjvWzbjNbSBCju54K5E6zqp5ibz9WDiZ25HyVHkC4esXuyWghkJQTRxWvnCnspuPOhAs4uObyHetVAYNkeAsuj-Rn2pJ9hfMWu2gC7jCelnopR5idJl2I90tQTJDdw9GzO9gNfFGjtUeQ6qP6M4qLr4WLbiR8NYE0O2WMIiZnr-pwsY_4N99yZZS1e0_BlgdEjdISbpMLP5bjY1T89FTii0Ab63s6yEwF-IsQWM_hE7m== "LAYOUT_LEFT_RIGHT Sample")

`LAYOUT_LANDSCAPE()` rotates the default flow visualization to *from Left to Right* like `LAYOUT_LEFT_RIGHT()` additional **directed relations** like Rel_Left(), Rel_Right(), Rel_Up() and Rel_Down() **are not rotated** anymore.

```plantuml
@startuml LAYOUT_LANDSCAPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![LAYOUT_LANDSCAPE Sample](https://www.plantuml.com/plantuml/png/NP91RwCm48Nl_8hPxA54Ig6jLdlOKrc8sWDDKGojzeGSS1jBnhRieQXQxN_VSKBJg5milZVpvetXrYDtE0uAokpFOrEtPROfM9vLQs1yi4f4twJkrDWBs2DQ_ojD7P-ILudxSJTwuJgZKMXCEZEaLd4Tl2uzzahkqlp7PHLGyr2cRpV9p-IAK9jJ1vTQkCHIRHHz7HmlewWIpXiTytwGUWMBB9pIe-Det68PiNUFOcX_cr7ttBt7tVKABevvBvRmDm9wJcFYIUnQRYtvF8iTPDOgsN6KHYy8vTzNaB4gsQnhQd42Rf9hU7ZAWvOfPIOFOKqFQ81sj9nAXb6Xf5bGJn9HE40v24MpF6NxDwUByIYIprn6OhGLwcEhprYDfquwx-kwObGLYaxgfysTG8enYN2yE3ESjtmCPQi5ErrGp1fwXSQUaIAGmapwZ9M1bU85pzWsiArytUCSksqikGDPKc1xJDa6emCjYCwkWGUp0o-9pyw17mmFmfQ4apsxVtnko_NTUbE4htyhT4-_ndy= "LAYOUT_LANDSCAPE Sample")

## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype, ?details)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```plantuml
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![LAYOUT_WITH_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL1FJy8m5B_lKrGyC1BOX1WFdfYJW0dWueR4qz9jJsdIjKtxvaACtztNY60lBtc_lwzpXznYryhWIgXQTWsm0w9nzt5iUHzz23nqLUV0rbeXA8ngtSP6SkKr4uUD55MStauolzfjrl7dBBgBRcXLfgJWGe6DZFSFridRywuezq_5gbmlbeljOpWAWWoiqohaJIlKc0qIFuL3or7RmIZ8ZmwXBHzqfnfkZs4z7RDXpbiZOJXYNm6ZTmuAUwXARWpvxA5YYJ5Ir1o5LWDQfTTZbkHPj5qK9B70Pj6KRLvJZoLIwjunVwXZg1bTQJXHsawYe2nMz08HB4FHWgGiHzs-J-r2_0N9vqGZC7W1-NVLfTREaPBcgYYod5YUT4OlDaj0gj637-zMj_ybSr0D_USF "LAYOUT_WITH_LEGEND Sample")

Instead of a static legend (activated with `LAYOUT_WITH_LEGEND()`) a calculated legend can be activated with `SHOW_LEGEND(?hideStereotype, ?details)`.

The calculated legend has following differences:

- only relevant elements are listed
- custom tags/styles are supported
- stereotypes can remain visible (with `SHOW_LEGEND(false)`)
- details can be displayed in different sizes via the `$details` argument
  - `$details = Small()` .. default; details are displayed with a smaller size compared to the legend labels
  - `$details = Normal()` .. details and labels are displayed with same size
  - `$details = None()` .. only the labels are displayed
  - if `$legendText` contains `\n` then the text before is the label and the text behind the details
- **`SHOW_LEGEND()` has to be last call in the diagram**

```plantuml
@startuml SHOW_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![SHOW_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL5DJy904BtlhnZnG4cW5MCyUB9M0WV0ne8ScssxoYRxbTsf3J7-TwS1WRsyPDx7lCa-1-GUMwsWMBpjokLiFbk_Gi6rKuBTI5EhjX6mHtJXAKayx-8lYVksQeFmjJKe3CQrrObJtFGnau2DabMIFKpoVhHTBPFl-_WnlgDHcP63IoDyx4ZBM2vyi2RYZPPc38EqHndGSxH-C6B58Q3GvOjjJSFz8QgdOnWUkmr7yCE0tZaowaHLSkSePoSgI9rJikOehHdGABiTGrhayNgs8OiNS1zFOVMHzLogbEq2z2S5G0jqZ-CaqQr2IRjWqqb4uG6b5efs1UhsUseNuP6ad9ECIFOkrFzLbrhRG4x2nMQJ5wJgHMVs4ZCNI3KwqSEdj_hQmgv-AHgnFm== "SHOW_LEGEND Sample")

Legend labels and details can be defined via `\n` in `$legendTest` arguments too.

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml
!endif
' $legendText with \n defines the label and details of the legend entry ("backend container" is label, "eight sided shape" is details) 
AddElementTag("backendContainer", $fontColor=$ELEMENT_FONT_COLOR, $bgColor="#335DA5", $shape=EightSidedShape(), $legendText="backend container\neight sided shape")
' $legendText without \n defines only a label 
AddRelTag("async", $textColor=$ARROW_FONT_COLOR, $lineColor=$ARROW_COLOR, $lineStyle=DashedLine(), $legendText="async call")
' if no $legendText defined, $tag is automatically the label and all additional displayed properties are the details
AddRelTag("sync/async", $textColor=$ARROW_FONT_COLOR, $lineColor=$ARROW_COLOR, $lineStyle=DottedLine())

System_Boundary(c1, "Internet Banking") {
    Container(mobile_app, "Mobile App", "C#, Xamarin", "Provides a limited subset of the Internet banking functionality to customers via their mobile device")
    Container(backend_api, "API Application", "Java, Docker Container", "Provides Internet banking functionality via API", $tags="backendContainer")
}
System_Ext(banking_system, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

Rel(mobile_app, backend_api, "Uses", "async, JSON/HTTPS", $tags="async")
Rel_Neighbor(backend_api, banking_system, "Uses", "sync/async, XML/HTTPS", $tags="sync/async")

SHOW_LEGEND()
@enduml
```

![SHOW_LEGEND Sample, $legendText defines legend details](https://www.plantuml.com/plantuml/png/hLHDRzj64BtpLumP1nK1cMgRfeS20g98RED0bWn9Rdi880p95RN8SfVONIecYlxtpf2KB5ikUkc5u7xCp7jltkm7vz7wkbJ1Tv0PVH3MW_JmJVezO9vBBur6HKTbYJe79RK0j4LT2ktXPhPAvfFDxU_9zdOndJ_Cad4OZ-8u16-WTWAKoL2f9hYIEtXxG2inLM8h7gNpRX2-30wZ0E1AwapLkO2tXV3RKym1LIrU2nbDVzfEZVP8o6nSCPChePmuJxNtldA_Z4OMlyK5CQjJ0cU9hYSMCN4RLGergt3ZVAvaIablxddhuMu-ElmO_nn__seTdSiT2NUjH47_6_7OA_T5GovsTDE1tvCCc0e5h5ykA85oO7RTGHi7XC8sC0XJpBxoEZlM2K6wBde8eP35teEJkSZ1xR4IxMcVCO9WakU94joO3HQdP2VCuH2kTxIO6cNi-3gP9tV9OhFzTKcVwNA-ND5vMdIduPjtxzxF9kyvfYqrJhZuccklUJs8XkUinvVGl-XBlD4hMfdQdyjbj6e0UyMOqagebWwwHcUCnrDaps6oMYt_E85dR_xhmTetIendwFOYdzFwWa2R7zYkBKmoh3RFm7O8SqQ01IkFjJSbUjbQ_4MVQUjyV7Bfo64D2L5PKz6CIQAALhHHVGVFoJAMqV_3s7X_P1m5mRfnNfJRZwRMETfcaFr0nhgbER1QUFY8-glKHHZ1NpG-02Vl34gJIff2h2gwVzSkO59LX2wSlXd2drZIe6fUtbjpe9OxRg8ifUVcrwcZxBtdJzNIhXhiQfrrEadVyCkHrOwK5TR1GIB7I0iT0DBg83FHFXJdy7ht4Jv942RtjmnEKMSuBwFwZ0SSmipGDGld8_64zpzmCHHA77RzT-FB-Og2lu_w9ez-qAVPkdQBPQDhEukbEEeCtMr6iVR6icPacrwcZ3PEK2ZGsB9b0vZoo9mq6W9c6RNJqv-tg1sse6abV1OJg81CzQn_pyLwSC8nWjPjG_YyNYv6dpQR-_KJqyw84IVQBdYgK_D2yWkknwnFHYQJq5lw8lEPpzcSdyZ2y-ItP34RHC47oawlx3y= "SHOW_LEGEND Sample, $legendText defines legend details")

Legend details can be deactivated via `SHOW_LEGEND($details=None())`

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml
!endif
' $legendText with \n defines the label and details of the legend entry ("backend container" is label, "eight sided shape" is details) 
AddElementTag("backendContainer", $fontColor=$ELEMENT_FONT_COLOR, $bgColor="#335DA5", $shape=EightSidedShape(), $legendText="backend container\neight sided shape")
' $legendText without \n defines only a label 
AddRelTag("async", $textColor=$ARROW_FONT_COLOR, $lineColor=$ARROW_COLOR, $lineStyle=DashedLine(), $legendText="async call")
' if no $legendText defined, $tag is automatically the label and all additional displayed properties are the details
AddRelTag("sync/async", $textColor=$ARROW_FONT_COLOR, $lineColor=$ARROW_COLOR, $lineStyle=DottedLine())

System_Boundary(c1, "Internet Banking") {
    Container(mobile_app, "Mobile App", "C#, Xamarin", "Provides a limited subset of the Internet banking functionality to customers via their mobile device")
    Container(backend_api, "API Application", "Java, Docker Container", "Provides Internet banking functionality via API", $tags="backendContainer")
}
System_Ext(banking_system, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

Rel(mobile_app, backend_api, "Uses", "async, JSON/HTTPS", $tags="async")
Rel_Neighbor(backend_api, banking_system, "Uses", "sync/async, XML/HTTPS", $tags="sync/async")

SHOW_LEGEND($details=None())
@enduml
```

![SHOW_LEGEND Sample, hide details with $details=None()](https://www.plantuml.com/plantuml/png/hLHDR-984BtpAogUH0CICRix7uULa8O1pquY0X6GdJsCXCfsOrffTrlTRH9hjFzzgsn3ICXgBdEnt1zLzTwhL_t9URI-p5NdBIH6xuJr83qyIBy5J5FffT6ew2ZFKQUWf1Q0DYjpeJrSJXRHTBIw-ZjQNyt6qxj9D0p2GHW6u0sKJe0o2IfLTSxa1YvsQ2N6Igp5etJUTOENmK6l0t0cTQBALC159lpw4BD3LOhNGWRZz-knqHu9cGqBPd8cb1F7gRRU5-xFmS3YGvWHip8cS9ReUc8H4hT1eL2p2fVEfqh6bFJobhVkRgQ3tH_Xn_2tL-leL6v8k7CbClfVYSTMkUyQKh6XcmxybcJ0M2XW_L912PG3isaEwZWW5BQ2RX1ZSi_hP5yd0EcQw3u4GcPR3qwc8WMtnKBKfst67dH6QHefmOrPONP8Ti0SzE5yGuknKSOEpwDfT1FDLkilS_gCvzFvWixZh3aDthnxzs4o-i0nTQbXnCMNN7l9wswlVynwU0hzkpx5stj5ArFwOxcCLXLWgnXJMWXLqq5NwOJnU8fiEOmMY_ct0tZsvlyUB7sbn722RYlIAQrF2DJvWUrQmoJ3QlCCR8CmPGIOiV9OUfEZbxN5N_IPjex79vME75QH48Kr1SsO9AfeHHtLTl2OB6CP_1h6nlizurwdiwoS5_dwiobrYhRg9h-JiQve3gmM7ZwZlfSw2thmWyO7uE2TRcvYILE8HK7tR-e5Z8g2q0NZDttu1tCQLCtBMsjsr7B7JPIvzDpyCdQKlVNyeLhSL8DDgPD69-ahVZcIqf6omZhOIUGOQQ41G5hjP2BgX-8ONki-mYS9mkZsYi4fwWpdPLJNkCC-J0nTit0y4azuVuABeL3YeEc_6vxELw_pxrxVwD5tspHhLs-nR7HjOp4NUvsXkSqebjvOreniqygKqCO12WKQczTi06CUcOD6VS0aeNPw-lCMjSCQDAs4Jq82rI5JFUlVSx7kd72Ce7PR7wwNyzdWwsfrktnYsXYnnudMCvxgsBoG_8JhFkkJaSaaz9Q-o7paSpRdLxBmDFehcaswv-rK36UciUudAaQFxdy= "SHOW_LEGEND Sample, hide details with $details=None()")

## SHOW_FLOATING_LEGEND(?alias, ?hideStereotype, ?details) and LEGEND()

`LAYOUT_WITH_LEGEND()` and SHOW_LEGEND(?hideStereotype)` adds the legend at the bottom right of the picture like below and additional whitespace is created.

```plantuml
@startuml Layout With Whitespace Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![Layout With Whitespace Sample](https://www.plantuml.com/plantuml/png/LP11JyCm38Nl-HMXfqvYAKA80wUDje93WQaLwh5A4ujMIjEeSO3zUnmcTTifzkVtd2VlFCe5msHu9OzpGDwEEF1s616yamfu8oTdWDsCLfcWWG-8pZzbsI9_n1TfGnyyB6gs21Q5cgVC6MdZngr7RSO-on-sXuW-twhi-ruyYZj2NKuEELfOX2CjOmTO_6nJUSkJKydtoOQjghIdmThnvuHQ13LO4ZL7Zp2bYj2fvFcLLLzPYqlhYhlo5rEW2Rs2dzNbfPhLOBewPenfb3J64usmYFbY03h6cH7GrwoEOU8tmMc9_vWrhnzjLvKlvNkHRjWEhAQ3_04= "Layout With Whitespace Sample")

Therefore a floating legend can be added via SHOW_FLOATING_LEGEND(), positioned with Lay_Distance() and existing whitespace is reused like below.

- `SHOW_FLOATING_LEGEND(?alias, ?hideStereotype): shows the legend in the drawing area
- `LEGEND()`: is the default alias of the created floating legend and can be used in Lay_Distance() call

```plantuml
@startuml Compact Legend Layout Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![Compact Legend Layout Sample](https://www.plantuml.com/plantuml/png/RP5VIyCm5CNVyodI8jY2QrN41q7ONEiKwZOsnSUGfTaMoDAItFhdstkpRjqAlZJ9xvvpxaqpTC0jD3jD0cM4Raf9jm2rUqXJox-JZO9jisgSjA8o80qaejgbjUR6UmOEIgrMwVXkCFVeuwr8lswJ--GQ4HkZWoiZRLBxV4BcqhhAHFoAXksMZiAOTB9eXONkH9z2F88KMuEYvQy3kOi4edPBnprhsRDcvzOEi_m78eaLN1DwKkVdQhAGcYtyZ7uQmRLsI3tC_7n-0FmR9uQWxBE57yQtQUgImnwJODqO0GflNEIJV9f5CGciXCOQ6gvrnK6P3TDo8qqPaW2_HprPlim-sNCn6xs_JYViu3w6nAJWlonJ-8P6o0xlszzWMt99WukMqaSQjWqOjvA7MFet-Y2FiTxBFl1Zz123y57_00== "Compact Legend Layout Sample")

## LAYOUT_AS_SKETCH() and SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)

C4-PlantUML can be especially helpful during up-front design sessions.
One thing which is often ignored is the fact, that these software architecture sketches are just sketches.

Without any proof

- if they are technically possible
- if they can fulfill all requirements
- if they keep what they promise

More often these sketches are used by many people as facts and are manifested into their documentations.
With `LAYOUT_AS_SKETCH()` you can make a difference.

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH Sample](https://www.plantuml.com/plantuml/png/NL1FIyCm5B_dKppdOHrihHlYmTDg6GxSjDXEyLIoDhf0ceJarJB4x-uBcvkOouFt-_iozyWTTgs2LVhsj2chjAYAXqMPBQ7WhLM2NKXTgwuHi4Eq_ZP97E_Z3ucxRjjvuMgZKMYCQzCcLd4Tl2OU6oMtINOzoSDgirubdxFu9hwYLPMHWaijN6o9ozZ_u6Z4M2wSDphYJIlr60PfcDAZusZSOCIAlKVHLdUcqmrt-wYUZc5uw3iSmHS3UgUOg1VRYbjBFgzY2wcrIjOSfT43McMNOqYBF7vSb2Hn0cRn5DOlMS1IfKpl8Ppf0GtGZPOJfUqKIig2ifU8mW7ALYZAyjJj-zWkmWD8FaSQWUnPgD-hphKsdfGqbsMP5yGAf1DwjhaNI3Lw4SQxC-rVoLpe9lpc3m== "LAYOUT_AS_SKETCH Sample")

Additional styles and the footer text can be changed with SET_SKETCH_STYLE():

- `SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)`:
  Enables the modification of different sketch styles and footer.

The possible font name(s) depend on the output format (e.g. PNG uses fonts which are installed on the server and SVG fonts have to be installed on the client).
Additional is it possible to define comma separated fall back fonts (if the diagrams are exported as SVG. Atm
PNG does not support fallback fonts based on a PlantUML [bug](https://forum.plantuml.net/14842/specify-fall-back-fonts-is-not-working), but this could be fixed in one of the following versions)

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH with custom style png Sample](https://www.plantuml.com/plantuml/png/VLFRQjj047ttLqpLG1HGv2IKFXGCSOL9e8bhkaf2diHA6iTRxqNiZkAQqd_lR7mjjDNBIZDdpZcpCxeE93trHW_UATlelaLO47NXqt3evIf_KRJewpwWRvmbj9GtpWmxBMsiEG_KQbKFYm_dinXwkByRlbxb7_CB3bK5LqXbqUTTv1-8ILc9BvEokAr4-NmtIK_gby9fvqU9LYyBgdMFIGOdSwxRndUXbVHMsHswbNxfiTrW7Q5_sgH7YLWYDOj3eiGVD4eAZvAmXRdpqAhGz24ePvEpmU0KPjCRM76J45NXkpPLOuowl82KrfrgfDPhaDRH0lq6eWBmTRHdVsadvgVIu2Wvy6nKnEDEXGbhsIpVk0BS2xXXRjLaXJEg0I5j36Pm-EJtXTJBsadVWfZiKbFiCOEczq6zyajWv3bFISsFZKT9rnCaUnssmsx-u_nVZeuC_UddoCxEpS5CxFvk_FpreQp6OgkPSco6FZYRojOecq4oZgSAv2KvppLY7GXDzTdrbcUzJflB34w5D9t6qpFuEG1-zjkLhh2kPDSnpnFMCEuwpUrJd327YlSPZCKidqvABl48L_abt3yMCJVMsgtUnka3a0DUxKuonFIQ56j1oHV8MmIa36hM2kpjrzPTIfiaysnXiTblg7TT7Mmz1AxayxOiPu9H4RJF7cXka3U2LXYFkNVckEGQRSi_qMy= "LAYOUT_AS_SKETCH with custom style png Sample")

SVG with fallback fonts MS Gothic,Comic Sans MS,Comic Sans,Chalkboard SE,Comic Neue,cursive,sans-serif

![LAYOUT_AS_SKETCH with custom style svg Sample](https://www.plantuml.com/plantuml/svg/VLFRQjj047ttLqpLW1LGv2IKFXGCSOLneBPhAYKXJs8bZUEjzo9sHt5DwRztDhwMqkfbfPapvvpP6Trv4euwhNhlfAbLro2iY5h_QJ1mOfE-I5frLUVHrTOG6afhgmUj4YRKN7bgbAm6sOUhHGWzpAQ3rzlqOthDeJBZ2Y4DkhGD_BryN9Jvbt6HtPTvyJmTnnVLIsQLTSD8oPSLLQh3A86B9TVjuuVGHZWZpG7T2BTssEombj0zxTB3A5yZrQjJei0VD8moXuAmWQLrq4XVTzvBQwBBNgyFY_a4Djma15NuhdHPQorlhY6cRIjheTGMXB6qGhU3I0zy7Sqbr_xTK43CXSPXT6BQwUIF1nsch4IzVcFpCCjXmkooJZAhPGsvC26OmEcJtrT2hIihNCEQXzGSEqoWxfoNh_pY6Nd5SvBBS-j1qdO4qL67xVpFzx_ydDdvqysPcOENavNG-tJq_FMXA4VvNZFcs0ATjoOMZPOcWMWKJkd92R8k6DnwGbr-jftXMM_Z-YQ1VYvqgx1_2JzxmCznk-8DLgLeM-PvmWf6RQkuUGeJvb3sFe5HlaZduu9B7C9jUWEpnopaHahPpTiudGUomAlT2eReJf5aBIZu-dYBWAH6nLgUlVtQkujfbsIUFImq-mtLeQkJhGVFbNpU5yKYPrG07RCdcWdoFj06mx5qLf-NtA5f-2Vw3G== "LAYOUT_AS_SKETCH with custom style svg Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![HIDE_STEREOTYPE Sample](https://www.plantuml.com/plantuml/png/JL1BIyD04BxdLwprq1JQn1RnuAcn1YjO3KsgU0gRPBGB-s9tOYZYVtSMgtKl0_CzPvSUkSDUoUXCw5Rs7R0zelNNQUhuaBmBtFTDxy6rHYDeJ5gZKYkv3fgPnqwA9brTpegmscqUqez5SfLSqAfUaO8B3IwnmJzQtz_cTLdbs_ofUYtoU1951JXlTCmx9VIKZR8mXKV7qRZH92eF7a7LDwRN7NU7k9rFsRZaoaeOJzXdnEZzfSG3D3MtbdnUe66PjLAq78NH8rgjpgSiAulaCQz8ue0jaZdRFAy2babf1i_2bPwXONIYvKHHlKH1MQmQ128uXaA1f2nFtRwExMBy0SddI2CmseBylUfKQ-T9INDTLKL9h43wGqysTu1KOu0mtfnH_oLBq1rzvZS= "HIDE_STEREOTYPE Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

![Predefined sprites Sample](https://www.plantuml.com/plantuml/png/XOxD2i8m48JlVOhOau9Df8W7J_svAXIaPudDQWDf6fADVNsteYXuyBJ3CFlD506bnpWOvZmek6eBYWNdDK9W9pau0yb2syv41Qn7T64lX9SJlsdiuoK6yDre4IpoRXo4CzBEj2oWCleYwctMp5PxF8XxpdTyGzQvfWz9JPuxoYP90pwCTZd3oZLBMxgiJ4bDLF8xZBbdVWwyrEeRKRqHrLz4_c7a12d0AXhq00== "Predefined sprites Sample")

### Using HIDE_PERSON_SPRITE()

```plantuml
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![HIDE_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL3DJy8m5B_thwXuO2Im2J4UF34d4HB1XGqzBjrMfKc_qhwv4EF_xcj0CB6NbxpVv-lS0tFGAKcNgyT5bI-snSkcAlBjgbpGWYahERaIkf5To-aUmFhx976iZpy4xBkwyzmrHWFN43T69LOo7Tmc7befwYIxdUHXjLi_9v-p-2w-mLMLeO89pLriaKl8_-XeH4ZEdJSwOgqIUam7QPZ2WsDWt614YeC7hge7q-cMkKFKJCTqU6my7D4lGl6TWwAUrnMp5dtUU4rJQwLe60YZ1xZAhiSqBV9uioXHuZYTnLEwViq2baffUa_3ePw2eNYbPKXHdGI1MRJi1G1t58JY4hCyTli-jOlW2ABFYOOWsNBvUzMbriwZ4kUoBFC2MO5qHYysJnomHi_3U7T6_PNCkMx3V_u0 "HIDE_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE()

```plantuml
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![SHOW_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL5DIyD04BtlhnZheIcqYHRnuAcn51Mq3Ksqnx19fdPXixliJWmY_dSdMZ_0PM5Wtfitx-qk0abFNQiXlztiocorpJVhCi-sTyKASjawZU94cLft3SA1o8Mh9F6oZvyL7Rgg2-XhQmWDnRLj4wUb6THcWHgjgcHvCSk6rkF3VV8oZo_ZCswLIvwGog2F7NE5ICQmjWG6iS46Agmbwm8TL02-T41eS2yxJT3pLWZEAq8OEVJ1cX6C4_7VV3GH8liaHB9fbPd2A1sg2kGbMJ-QYFmr4BRbjUrC8_rhL9zFOVoLUJo1Dm5yVgn6FLQbT8vrTbX1wfnMjIJ51hYrF9r2ccVnUbNmY4UOn-VmyBGSi5HhsmSOdeh3ME1tSf8fBGTIl0iAJaNeWLIBcdS5zlP-T1VH5yWwHng3OelwEzMlhSV0arnlYoBBcJMGVj1VcHiajj7ZKFRUjdz75cYQuKS-00== "SHOW_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE(sprite)

```plantuml
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml
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

![SHOW_PERSON_SPRITE(sprite) Sample](https://www.plantuml.com/plantuml/png/ZL3BJiCm4BpdAqmvD9NQ62h4WHCbgYWIZwW9S8pSPA6M_9Az8QeG_ywQlX0dV5bvPtPcTgy32e-TLic9D8tgMc1hH1UkEFUYpzubhhjL5y0trY0Op1ghkLF2n9b9m5R95Syl9aLiFJ_SyuzfTfcTKQlEQK980pvpF_ejlD6FsI0A-l_39lSYhA7LqhHyhp-n3ao0flCIDy8tQudGOETXEf4q6xWM0S4VjzdPyTngRSqkob_mcPovK6eB9-NYwRKkvilowR4kY-LTDKy7HArZmFhT0vZwO3qO9Ka1FbYJYXXrp0QpM6L0Bz1wmiiDHTBrZUrCA_mcRSx7R5WAxHGCH-mpOVGEnqfxMDN2ET9vXHMREQTa8r1QCw1MVZfcixB87kSLZNXWq-oSFRpa4PifPVl0OiZ0q38weHD4qPr2ILwiwYNIRHXA3Ogy0cNxsgLBSGkIpeuM5rk2sczrZ4N72j5lKLL5IQn8Eg17cLj0Yj53B6_UwjyZrs1QklGt "SHOW_PERSON_SPRITE(sprite)")

### Using SHOW_PERSON_PORTRAIT()

```plantuml
@startuml SHOW_PERSON_PORTRAIT() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![SHOW_PERSON_PORTRAIT() Sample](https://www.plantuml.com/plantuml/png/RL5DIyGm4BttLuohi5rOMrt4Wo1O5r51tRAjUYnfE-u6qYGaKyiY_dSdrg-3ENJIcJVlpPjSU1AE-av1SRDwhlAhTR5wgFBLkbndjsKyWq9qLc6q9tMZ-XPXIsJzMPewCIGRITk-xZswncX2JKbZkjGgeGFZeQTMoJfTdXpc8VLuVvU-BfBJv8XJrP8xXDJe4ilOAFfVFefoTDxeMBITr7EOP25AJqwGSPDPLEmyOLTTcbwtmktYvdWEqt7cwGpU8k3p8nKFM5V2MkPvnXeoQvLi14cZ9vnQxiyXA_BauQha5eUmI8xX_caPQfbIPl0Gh7eW0-pJ2ePqlIB9Mb0EaWWTaEnGiPRdsTw_fejfB3BF5uoBqHJa2mYmd_v0-i1PSsSBZDbonLid2O6sgCC773Oaz8R5bDYPda8F3zI2sB2xxqMDV2mr_eza8nKREHXlvvCHjWY3h55zh_TtFu-UBN2yASkyO5G0_LH__LmZyJu63E75cUvlomNgbf_s0m== "SHOW_PERSON_PORTRAIT()")

### Using SHOW_PERSON_OUTLINE()

> This call requires PlantUML version >= v1.2021.4!

```plantuml
@startuml SHOW_PERSON_OUTLINE() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![SHOW_PERSON_OUTLINE() Sample](https://www.plantuml.com/plantuml/png/RL5DJyCm3BttLvY1j4uQBKo80n8IOve02RQATd2iqjPiaT8aIbog2V7VSIXV1tAeK_lvFJ_dofDmrBKAyjlrSvaj7_FrgbnlYlkxrJAUG2vQgp0waBfMNOEm8xB-8asTw9Ejf5rNTHvTRJIXfgGsRMgLq87ms5EZP9KkpewpaDeytAUli-GyEU5KkU0E8JMwn38sYlvLZw8CdJSw5aqhzHH6yn2b9oV8kD4aolUUi2slJQSRuVPnVJg5yJ3oU09l4V3vKOfxh4fXBVCyOmLpQvMi1KcZHvnQ74vXdcV9QbbmYqEO9QVmyBG8jRbIflSGd7eW0spJ2eQqdIB9Mb3qaWWTa6nHiPRdsTw_fejfA3BF5uoBqHZa2mYmd_v0-i1PSMS3ZDbnnLid2O5sgCC77DOaz9R5bDYRZa8F3zI0sBAxxqKDV2mr_0za0nKREHfkbwC1DWk3FABwNk_lVZQUBN2yBOeiPrG0_LH__TmWyJvw3E75cVPlonNg9hpi1m== "SHOW_PERSON_OUTLINE()")
