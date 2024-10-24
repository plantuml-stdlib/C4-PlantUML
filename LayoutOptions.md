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
  - [(C4 styled) Sequence diagram specific layout options](#c4-styled-sequence-diagram-specific-layout-options)
    - [SHOW_ELEMENT_DESCRIPTIONS(?show)](#show_element_descriptionsshow)
    - [SHOW_FOOT_BOXES(?show)](#show_foot_boxesshow)
    - [SHOW_INDEX(?show)](#show_indexshow)
  - [Optional support of additional PlantUML elements](#optional-support-of-additional-plantuml-elements)
    - [List of supported PlantUML elements](#list-of-supported-plantuml-elements)
- [📄 Themes (different styles and languages)](Themes.md#themes)
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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![LAYOUT_TOP_DOWN Sample](https://www.plantuml.com/plantuml/png/JL1BJyCm3BxtLvXnQ2TjBKESEAqC18SzAjOnSQhIrgEHqYHANAe9yTznnTY88bdoz_1dppq9HrshWYkfAzNL20sHzVT9uaGVVqXgkhBpw2gZ2JN5bMaJguGUD5DFjP9bihYRPaDhjrecdxVnR1RVSAzOi4H8ZIwsmu0W2M5j23HYZJMKM0as1cga1_xK8DHu49qY29DWcRvlTdcHRxBYSRDVH-CWoD1veoDHjr9FO9GELNfoWemRZOFjqHEsnOFfT2tSCQfc4mYtehKAmp5y1S3l72dgiIo4jUopnn9IQvMi14cZHznQN4yWtMRn-YbdYKFWfM3rjXYmL2dJUnXkmg4Dy46iO4hBmINFWhoNHEY0P8kAPtdEzdrA5z4lo3ud6eF1Awg_hIwnTfwLN5_oFDioQo2TqOlDCnB7w74e1sVQ_v8vwfel_mC= "LAYOUT_TOP_DOWN Sample")

`LAYOUT_LEFT_RIGHT()` rotates the flow visualization to _from Left to Right_ and directed relations like `Rel_Left()`, `Rel_Right()`, `Rel_Up()` and `Rel_Down()` are rotated too.

```plantuml
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![LAYOUT_LEFT_RIGHT Sample](https://www.plantuml.com/plantuml/png/JL3BJiCm4BpdAqmvD9NQX29Ed1gYqYAr43KfY5Fa90krv9Vi3L65-7VM0bfyMMbdPcV62u_SOQzaT25qA_iEs07H-jiqTNn8tWKU-gRtu5gZ4JGchL6fbLm7pSnZ9qMJvZUp8gpssqtwSPtCvyaLxUgS95neS8aD1j4cUttQL_LcUL_LkuVLkeedKLI0yqR7l5D2Jzae2rDuT1oD6qsYykWHL7rdUjrnTupR-PIDIwwiXF64VKQCtiad7g2fkRLqvmKQbbahHSjH63sYLNuvPLbP98_BYYGE62Lbs-SyO9cKPl0i5FKC3QEMbXD5zH85UR5g48ZW60e5ahmyPVlwJHVZ3qXtVca4HZkGVwtEiVQUb3JNLLMKn0ga4te-imAa60E4yUQC-YzPWExeExy1 "LAYOUT_LEFT_RIGHT Sample")

`LAYOUT_LANDSCAPE()` rotates the default flow visualization to _from Left to Right_ like `LAYOUT_LEFT_RIGHT()` additional **directed relations** like Rel_Left(), Rel_Right(), Rel_Up() and Rel_Down() **are not rotated** anymore.

```plantuml
@startuml LAYOUT_LANDSCAPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![LAYOUT_LANDSCAPE Sample](https://www.plantuml.com/plantuml/png/NP91RwCm48Nl_8hPxA54Ic6psbDFPI5g3pH5CMor9-I0srWojcKFYwfL_tl72KsZSh7utioRDuPRZzpXE2Weix-FJTsMsRPWULPjWF71AX5zaxfJOo_WW6ZzJPewFYKl4W_ZVlJ2TKQZq9XqPaYjuZfuNNlibTod-Q_hAg3ceKp__KpMw-G7iJQd5YwrS8cbuYZwEZbUHb4bd3SwvlqWzGeMMJYbHyVHkCKoOgyUnT3-DgFkkNkDk_KAhaw1hvRmFm9wpcFYIUnRRYtvF8azPDOgsN6KHYy8vTzNaB4gsMvgQd42A2Wy_Cc3bYbb9WzXJmzeW9Qqd4g6KQ6aML1F4b4uG3a8HRCyPNkRqyLu4ibdBYCnsWdriTLdhCPJ9vttTLqngWf5P_NJvauWnPX4E9wT6IvRFeQorOATBoXc3Rr2Ooz84KXX9dt1oi1AyOmNR1VOJhuSS8xTDfRSWImfi3sbR8FHaHP4PzV0WzcHbyHdvy2FXaTXHyBPdjq_FhNbvcwpBSBNlnMwfr_Z7G== "LAYOUT_LANDSCAPE Sample")

## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype, ?details)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```plantuml
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![LAYOUT_WITH_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL1DJy905BptLwnue2JGYl7aYLe9c00IMoIUcctxb4tsAxklDiJuttqR4TpBIzxCl9dPcKVki5CokXAwaLqBx81e_NsQEjud7m8FNTrvS8tH21gJngZKIgw3PkAnbQ9Eyxl9DgnswrNwUPjCfyaDxQgS95neS8aD1j4gUtlUbTN-gLnMg_bYldcCHr6q1UUDZdchX1wpGHQcyEWu6ZSOHSNH8wZgmNIwvUuODzCn6nPSMGd34VkA6BspKTn3NN5hwSuUQfPPAqN3KHWze5L-FMPPiKqsyv8a3XX5PUlNF62PbARtB3Jr30sZcfOJHNKI1NcniXU8u1WA1PAyF6NxFgMByHUaEoSQWT4BoBzMbrWxJqgQoxBS5iGAf3DwERC0f1WzXF7kZFelcO5kwJz_00== "LAYOUT_WITH_LEGEND Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![SHOW_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL5DJy904BtlhnZnG4cW5UF9axKIE00sjiYnsRQhRB9VsPtQ4ED_TneGtCjBvdtCc-nJGEwnqmgArUk-MY-MY-qB55mx9TYDD8tgMW47H1SUayJpFlwKUEZgBWZVM8F2ODnOdJZ5pH0p2zWgMIVPmomVHhlDElcwZ-Vp-8vcLKOMBetmiICnOxdmmPg8jrgQAOpI0ML0pz7wqOGLnu12Ly-sCottnwYPJs5yAZUUm3S3UfV8g1TrnPsZdBse8NLEoOQZj6P4e-ns2ccHnzj5IHOlW4h1vZqRk5GfsmSORWg05kWWnqcYEuMITa7PIqJX0QKMYdO5wlPpRXVXYQISiun8zYRKtrNNMhj0Ji9LMUO5gGRHXRt6B0LIZLuCyE6j_czX_xufch1V "SHOW_LEGEND Sample")

Legend labels and details can be defined via `\n` in `$legendTest` arguments too.

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml
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

![SHOW_LEGEND Sample, $legendText defines legend details](https://www.plantuml.com/plantuml/png/hLHDRzj64BthLumP1nK1cQgRv590G1I9QHp8aY79JGu1X26veXPPxXAxIyL4qV-U6PAIPSj5BxaGt8-PUU_DcttlF5fV5Qht6wH6xuNr83tya7u7c6NIIwDHqL5HeCv0IIq0RLuLGdkucYxZsNXzytUykPbFPlVJU1H4moWAm1ked01bKbIgxbt8BRpUevMOAB4H3z9vrm-U1mTX3-12wbHLcO3NkV2ROymULILU2XbEtcucHdiaP3OgcSc5K4wSfjfvNxe_XqEBFwASc5K9WRD4rnEBYBWDIuMQLRXoFbCoeQHNTxnrVpiRxl-8hg-Ztryif3Ev9UKkbSZfVoqUEkc-QSZ4bcuwy3lI0HEXW0NC12LG3iosFMZYW63O6lf1WkbtNgU7EW58rqOF810ottbmCXCPk1sMeZdjCeRG6sTPh0HtPetvCTaHSp20ooqj9aOPExgCP_5jF5zlFYxeCrdC5aiwJ_BsD7ZrvisxwVWTnpIbHZ4NNt7j5Q_xuU2KzUWS-ZTzZZTyGIjJ-LEvZ5OrOASOKreArT11L-kKyNYAx3YCbyl5boDuDkT_7gnyhSHeYcudiXcjpmWq-O7zsi0anshp16oBC6C4cBFoM7bJe9UDnv_rcRPEvoUJZYnMan2bDIKDcIIgQ4KJrNNmb2nZ6VuQniRx0-EmrrlLpejYyy5KEaDRzzDhCjOD3OBLmiC7rD-bpeCG_g7v0JXwfr-OHD8OObdI_Tjc0UEo97J1vDK0lc91awfvUMVDdbhkk8coa9wRNoMEidUUFrPBscgmhNJQwYHzpKz7MZbILbW7UuaS8osq04YhlKn5yrASmklSH_WaGHZVtJ0uHPtXl8pgC-vn05D3rooSZiGZtl_1nL0eST3stutEvoli_NlGDtxm_IxDnZLRB1jTsrein45dQ6ypYfKtbZKZstGofRHnX4A1nXOD6y24H-QeqG0mJQcTdlwyHUsm0KqhuTE8GFN8L4_wzrIiUoSS8sZSDe3FgyLy-6czlbizCcsD67AYpPodEZ7F93_ZUiZwQ6Go2JscppAV-9pD-OaiF8l_YkVJVjXxJzdfbVq9 "SHOW_LEGEND Sample, $legendText defines legend details")

Legend details can be deactivated via `SHOW_LEGEND($details=None())`

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml
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

![SHOW_LEGEND Sample, hide details with $details=None()](https://www.plantuml.com/plantuml/png/hLJVRzf847xdhvWugGuaOffhyt8IKYcuRI824P1h7ogXiRsOLTUxrkwQnZhT_zuPsn0IShgNlbZU7pFpVTzyin-SH-lBN7N-WCJedR0Uf8UVqcy1qrHwQJGgEifpr2aegGMWpSfSQ0-NaqKq7Qrk_exMDxFnz64I3ODm48O1U0Eb4w1CWafLdJEvWJSxj19Z9TRYKJhlki7BuA3N0JYJEb5bAk1D9lpw4BD3LOhNGWRZz-knqHu9cGqBPd8cb1F7gRRU5-wlmS3Ypp0ZPcLCu2pHzSGY96w3Gg5c5IwTJvMCAUdbFMyzt4q7kp_3gwlmxQk5T2etfDo54XdzhyHZAzrt3QdOq4q7VaiwO2mKi82fe0JAWTaq1tKS40nRGJU8CVd1wsHV9m3fckW-149cMmzEfY85jyL2rATjnXvqHcaQAS6TMM5sI7R07FJXOaEBiL763Y-YQNGNpLRhJtFwZEVJ-OBEuwmv3SxVlRkUZAuvfYurZBZuacilUTtjzOzP3q-XVzUdU7klQ6LAVooNqQe2R1LZIWkXQZheAfqm7a-HBOVHOZ7_UW3FvlpFWwMlb1XEq6r5EgNr2O4wFx1VQvZaM6sUWMqGfem0CrOUIszozBBs-8i-qzRn_AJIaSKg4gAmfg0XaqGLhQYZsWuUasKiWz_3s7Y_PzphT9QLyo9VVpIbJj5MtUIAZ7L3Ws2ryF0HzG-fiw07_z3y01oyqyrDB6aCiIZe_bszW55H4BfWVDw7RvZJf6fUtbkpevOxRgBCfUVcbx6ZxAtd3zNYfXfiIfqqEabVyTEHb8wK5TR1JYB7I0iD0D9g9nDHlnJ7y5ht4Jv944RtDmnEKMSuBwEwnHtsOMBeceNZaNZ2-p-u60eb3fh-k-7fVFKw_-xrZHvzjqspTlKMoqRNDXPpiTSPcjkCOkcDPSt8DgrC2MqSe52WiNdD1Z3caJber0TC4cgdfpzlKJkiGTDA-2GaK1qorRF-FHVhmGd726gtzU5sEPyDlgnMzyidfeqHUvneFUEfZiqBoK-uxhC-6PbCGe_fYyn7FcTpVY4BJwFFqMpIlMYdOZWpZNK_K35wT7y1 "SHOW_LEGEND Sample, hide details with $details=None()")

## SHOW_FLOATING_LEGEND(?alias, ?hideStereotype, ?details) and LEGEND()

`LAYOUT_WITH_LEGEND()` and SHOW_LEGEND(?hideStereotype)` adds the legend at the bottom right of the picture like below and additional whitespace is created.

```plantuml
@startuml Layout With Whitespace Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![Layout With Whitespace Sample](https://www.plantuml.com/plantuml/png/LP11JyCm38Nl-HMXfqvYAKESE0tQ2Wu5fbQenofDB5efJQF60VRlSPZKRQVOdzzpdhptA1SCa-6LFCu1UJlYmDjXHF1EAk2Dd9m1TZDQPO86FY0w_vXbY_mHNwGDVV2mgDaYM1HgdZ9df8qRjnwr6ViiVzWU8lfygxBlUx7RYJjYNKuMELfOX2CnOmTO_6nJUSkJKycVaWrRLMbFWxNZpmcr26gm96gE7c5A5Q5JoVChgxwo5fVM5NVbBwP04te5FwlBIpMhmNHrp1ZJA6cC9nfX4VF507IDCoEWhraTmyHlWjCI_p5hNZ_QhYfVolSYtR0zM4q7-GC= "Layout With Whitespace Sample")

Therefore a floating legend can be added via SHOW_FLOATING_LEGEND(), positioned with Lay_Distance() and existing whitespace is reused like below.

- `SHOW_FLOATING_LEGEND(?alias, ?hideStereotype): shows the legend in the drawing area
- `LEGEND()`: is the default alias of the created floating legend and can be used in Lay_Distance() call

```plantuml
@startuml Compact Legend Layout Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![Compact Legend Layout Sample](https://www.plantuml.com/plantuml/png/RP5HJy8m58NV-okwnSGjaKsCJoOc89jeCeM0niUcT0MMb6vfRrN-lRSC1ajyMTllddFFxJgom0sudI91fOLofQHRWCO-fAdXFyccWgrREIkDg3L83OceTscZkFQUWOLILQjqSZ-OU_JvLgJVTybmcDmYOnEqy4fBapG-W92vDBRM4R-XORkbup0cdInQOQ4xqQSGZo35LgDekRSWTv50r6xff6SjUzRiqjfXblz29B62QqBFwlnIJHPIiOMVqKyZk58MgOUPdyyFWB_Zp12KVRRmm_WOrvGS3fW4QwS5L7ZZ8f_cxraKay18S4RJSArg3fNUC2KtKfSX2V1xqfFbo-oBFHUpySVh-vGTtQScCIdudcKLFg8MiiE7-276aciQNBMKFjAm3M3SI1vYwT_MHtcCzLxl8p-r7c4ZVDG_ "Compact Legend Layout Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH Sample](https://www.plantuml.com/plantuml/png/NL1BIyD04BxdLwprq1JQn8edJusXMB3LO5B5KzWaertO5xiJGn7_kxEqjk9U1kPxpYuySeUzacoTlJrjgpehw_9XMUKhLd9b9KGNGhUoxu3j4As_JLF7X-H3uAvlUW-kDHf1Oz8QbLh9TV2QUUoaQDByPbQ4rNQpJZ-la_aykQ9TdPE42mqkiKIEel_9yIIA2d3Uw9XtIkWf6sLX2e-Eet6ZILJkFOAgxqolE-xsSJkVil6Xy7Z2lY96xnGJ3z3Kt5hoUOM6PTPAqN8KHezebLzEMLOMoUEo8ea3HaNPvYKFM2Qb6JmBTtg6Xj6HbXD5zH85PR5g48ZW60e5ah8yTVi-jeln09BFaKPWz0pozwfphQqd9SrLLHKbiGBfX9vjxW6fnW1Xl3kZ_aeMeBlmcpy= "LAYOUT_AS_SKETCH Sample")

Additional styles and the footer text can be changed with SET_SKETCH_STYLE():

- `SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)`:
  Enables the modification of different sketch styles and footer.

The possible font name(s) depend on the output format (e.g. PNG uses fonts which are installed on the server and SVG fonts have to be installed on the client).
Additional is it possible to define comma separated fall back fonts (if the diagrams are exported as SVG. Atm
PNG does not support fallback fonts based on a PlantUML [bug](https://forum.plantuml.net/14842/specify-fall-back-fonts-is-not-working), but this could be fixed in one of the following versions)

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH with custom style png Sample](https://www.plantuml.com/plantuml/png/VLFRQjj047ttLqpLG1HGxBZqgM28Aum3JLpJLHBo95RIsDvwBs9t5DUK_djduskXhLvMcZbdpfcTqMqWwQapklTEsLft3SAAg0sV1WClD_sbebLNTG5zxIoXfNxjpA3LqaRETQ16gsgGVxoUnz3Zm_tWzKD_EEpVSApCcIALHTzleq1FJ8fIV9aK-LqfYfVxINfHBNEddHybMYrNLEaEammk5ipRnm-XZVHMsGEwaNxjiTbX7Q5_tgL7YLWZrQjJei0VD4foZvAmWONpqAXGTo4ePvEhNkyIvhCfRBXBYAhmNPkoDaODRo2bRQjggVKMf7MqGh-3g01y7ytLNzg9-PaqE4fETNOgukcWmWKhMQ_VQWLu433bsghEScTK3KBQ6CpWzCdlAwdNbPE-0J4vf6ROOGPrvuDwvPV0o6iUargS6u-IhYD8ZZfiXztyn_c_79qP-jFFcPs3cvEPsFtz-ENhOr6EnLupvTWSVN0sbOrHDeDa74yLo4jodZbY6mXD-TbrbcUzJUjX1fT2cbRZvHNyx04_n-rADrYLicsvpZDMC6vRpUrJd327ylSPZCMyFviKJF48l9_my9J7t5XhjtaRfmz03dYtMyaGqsbIh0K5No1l4P0og5ahiBTVUtSfxP9SPm-BpNv3VUZgPEinC9FFkwAO2qP5q35xAZD5tWZQO3mMtfbpoYtQXd-Ytm== "LAYOUT_AS_SKETCH with custom style png Sample")

SVG with fallback fonts MS Gothic,Comic Sans MS,Comic Sans,Chalkboard SE,Comic Neue,cursive,sans-serif

![LAYOUT_AS_SKETCH with custom style svg Sample](https://www.plantuml.com/plantuml/svg/VLDTRzf047pdLspTI36I0w7gKoMaK0iHgOIYsacK9-jiBt3bFgoxTIYg-j-x5p1GLQrVpjwTsPczNTzv4evQhNhlfAbKMoDiY1h_QJXqOZTOIzgqPUlHLTOG6XfKLWyR9KpWt7YgbIo7wSURPGWzFio7hny6ez7WbcD5oXGX3Rf14mHwsJGliY_JFBqlilnbFeslodLgbNNZICdrXahLOfJ0rOfvntWNsWbdfEdGjN1RX_K1QmdTyo4zZh8jKhKv9tByGUCeTIW8QrXP1xNqLUkzj2RgzthNi5pCOCTTGb25xqeNbTPoT0inxHjP2QNs88ob3Re3H7hW-wZxpFsxeO1O28tZw5pfe9CzTJfSiXJLzgsQXuSCPbnTLabgjQmW4oO44pX_ylj6g6rfXQjPiqijiCK4gjPv-Seldf4tF2YvkhGU96rB49rqsCx_VF_BpuMTFzrScEcydAs4tkUJbw-FUJ79ZfennvRel3MngBKq2KIJS4fFJf1rmU3U4-hYisqDpteVLwC4hZEX6uNNVVZP0tvEsnNli2n4qt2TPonXqZIAcwSmOGwbxnEOPCl1OfepnI7mViB3Knfo4wNixcsSpWDPuDrk14DqgqYo5kHyVRn5G5AZOYtFtduTtSLqI7AT8omq-mrLrzNPrgDd9f_tURxC61L0f-ovp0nv7sY7uLWvgoyfTsXg_eb-0m== "LAYOUT_AS_SKETCH with custom style svg Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![HIDE_STEREOTYPE Sample](https://www.plantuml.com/plantuml/png/JL3BJiCm4BpdAqmvD9NQX29Ed1f2H94eH4qAuXGvoK8j-ILxGrGX_fsrA0LVLjgPsPdnoYDtE2WPdGdToQ47jaUq_ZfD7H-JTu7xeHqykCve18r9PrHg9TT1i_3OIz6c-TMY3AlTvY7zk4oMo-I2TarE4YuqkCG6WsXzVriqLLriYwVwjIpYMHILuBpHCU-Lq7CsoS8K7Xr7uoQpg3fu1DNSc47tt1tYRZbdquehAs4wOvyHetToYKTe6sujtNc1bcNMIj5n54PFQ9MVprbMbSbZKPF40QESRFES1ooJqeoUXPgUeM7KqNAYg46Y82zMZm8H74EXG9ANfsnVntGn_e1qvqWZCDg2_6tr5sldIKbpNTTbHQn0Eg5_P-u0ASO8ORmve_vBLg1x-inl "HIDE_STEREOTYPE Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

![Predefined sprites Sample](https://www.plantuml.com/plantuml/png/XOxD2i8m48JlVOhOau9DRF7agJzNXOBqB6cpsa2QXcHhNz-jA0eUFEqmp7upUK3fSHeCSnuKNBK5nOBp6Y6minoSWMYbRMSc1Qn7TE4WX9SplsdiftOAuBlH8bZatJW8PwHTQ4b0PNGhgdrIBrPpEefxnjEKxyYxLFGYgSfpH-4egi67qQuNMh5bSKEN5J6fcLf-bp7tp2-1bzfy8yeteloBo3wCZ20vM4M37W== "Predefined sprites Sample")

### Using HIDE_PERSON_SPRITE()

```plantuml
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![HIDE_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL3DJy8m5B_thwXuO2ImYV7aYJaN8H5SsD3ZqcrLclGhxPiBCVxllWO44tjvoVjzlYuyC0UzadIvUiph8j-MBvkwBBQhAgSbKrPoSYLqA_kEqps0zVT9ujWGVmZOzqtlkMkD1guXRerAh6GwkCqyT58qINOtAy9gjtvEFc_Z-Jo-mLsTeOG9pLriaKp8_-neGaZ1dJSwOfqIUaf7QPZ2WsDWt6X2oeC7hke7q-kEkKFKpgTqVAmydj0lGl6TWwA1DpMp5dtUU4DJQwLe6GYZHxZAhgSqBOjuarSeSPnYLRf-pGAMIca6JyEbdeAXUAPbI56z185Pj1e407SKXE8Iipns-pwrY-08ei-9XY3PSlbxrQNMpgCIvxAgYX9PWNH6BpPF7B36mCDuTqRzbIouxi9__W0= "HIDE_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE()

```plantuml
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![SHOW_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL5HIyCm47xFhpZdmpgOhHEVV7AEuGItbRLpZoLjJnT8av1SBKFyxrwTRe8XS73VTzzzNt8VI7fg6mtPOhqhqlacMw-ABDqyvNF8PECqYWjbAjtM27iY5-wInCikVbEqRyiseA-i8JGKLxP9d9QcLxiAL6jL9hFRgxHlRPVFoVjDF9d4rzmhPZmYbK4VEoOBaGnXPGaCOeqrb5X95WRQgm1yQOzGuwjiDK77Qo4uhmXXuD07QmOmJCH_zz58YFIR4CcwKMOCWsbVLI0loVh1I6I7GDWK3xOrjVI7g9gCONWCFHp1Xm0-9wjHXsKXdMET7POmTKwhIf9Y0zoQNOvXcgNnQfxpY4VWiB1ycVNOL6lR1UZVYiDOu8ToaYaD1rAy2t9EHUY1L8EQTmNszldZBg8Zo3e_D0R51lLlghEjRU19heiyJpDczQGJUfPvH68R7VRbrTlcxyWzchh_aIy= "SHOW_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE(sprite)

```plantuml
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml
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

![SHOW_PERSON_SPRITE(sprite) Sample](https://www.plantuml.com/plantuml/png/ZL3BJiCm4BpdAqmv4AGsfeWJfvQe0YHeeoR0CNAJBRNab-mDKONuTzRqXJZXoyexipkpCmaeF7PQ9MVIDAfhWMqGNRZbt8i-UvUuwLPT0DzOWs0mQwpcJWaJPqO1MoLNFByP5R7rylp4FwwpyJYxebwTquYG1dpcVWHQMDEFsI0A-lz39_SYRA3LqhJy832o3ao0flCIjy8t6udGOEVXUYHfDd0j0e8_dRENuxdLsfgzbR_W2obpeTGEJig7nLjTp9RbObwNnVAncgK3ejRHOFtk0Knzb1vS9aa1FbYJYcXro0RJM6L0Bz1wmiijMTBrdUrCA_msRSP3Tb4AxHHSNBBFXD4xXfNsiAg5SxJd3LPiwfoIZK1fpO1Q-VcGJSiYcyyg6l70A6xs_9f7RAgKxGEB9WD3ooX29uYYEuMIj5ZLIwHi64eDYhG2UVlQkqjn1zAUFIqUjWHrkEfaYy8AKU-XgegIM95qH4zhxW79HW-nhBtLlqScO5fA-Xi= "SHOW_PERSON_SPRITE(sprite)")

### Using SHOW_PERSON_PORTRAIT()

```plantuml
@startuml SHOW_PERSON_PORTRAIT() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![SHOW_PERSON_PORTRAIT() Sample](https://www.plantuml.com/plantuml/png/RL5BIyD04BxdLunLQ0eriSMJ81YBgA0sD56FOPECxS9cTzcT68hutvqrlWxcaDtCVFCz9XUUXAE-Kr3Sh9-h_6fJh1-gVBqfDzbj6S-W49rL61r8tQY-HTWHMN-MfauCoLRIhgzxZwuncb1JqfWkjKhem7ZigLMoJbUdntaeFTxVfQ_BPB58JhXMhNX4I8qkiGoEel_reoX7vusEHTj9FOT95axfoGaoRZABYhqdxAfBq-jMk7tSBEOm7KrFP_0M0Jy_Kl60TIMiPPvdh26pLib6a3HwmgNLuHoo8ayUhaeUSGXi5kwVLg6NAMK63o6h1pB0GQrWIDShagm5vI29q0793XLhUVRs_kKkfh79F5ymRaPJa2yWm7xc0-a3PysJBJ1cnnrldIG4sg4EBt3OaD1R5bDYRteACsoe1R7bTD-B6lbOQlmUoKOg3d8qtiud8smPZ6nGVQ_tTp-FdYFmULEMUS6e0Fhf_kQvHk9z31YE5sUwloCNg5l-jHy= "SHOW_PERSON_PORTRAIT()")

### Using SHOW_PERSON_OUTLINE()

> This call requires PlantUML version >= v1.2021.4!

```plantuml
@startuml SHOW_PERSON_OUTLINE() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Container.puml

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

![SHOW_PERSON_OUTLINE() Sample](https://www.plantuml.com/plantuml/png/RL5BIyD04BxdLunLQ0eriU994AobgA1jQ58zXaqojWkRtMLtOYZYVtVM-3gOGtOpyyttc5nx4ewwLa5-jtuki-KcNw_AzRPuk5yjumdaehKAeoEfQzKr27iYwo_Jr8a-sKdQTrNdqTL64sfAQjEcLWaT24yzDKfMwUBYD0kbxUD3-dgUp6R96TVA1Oy8gT4bbi5HzAzy56NelD6nQ5gffp2QXrDwSeAC6qsY_E09s_B6TBeHxX3NiocC1y_Z2Rn5mC-FKjnZLGfhcUSPAvXRgsGjI1ezujBYU0hpF4jMou97709xXSUdHUZDbJAzXn3L0ndWd5OmfEqKITQ2efT4w81aYugrF7jx_t8Nqz1adYyODwCno1SGO3_pWVI1i-B91XYpvuwtJX82xL675pYiIUWTYobnC1s56JRKWDXnkkz53NmiDNmFP0CL1paPRbUZ0NOUZ6nGVQ_tTpzRpn7ul2kAB6TK0FrqV_FS8l4-UWp7YpFjtv5hr4tuiny= "SHOW_PERSON_OUTLINE()")

## (C4 styled) Sequence diagram specific layout options

- **SHOW_ELEMENT_DESCRIPTIONS(?show)**: show or hide (hidden is default) all element/participant related descriptions
- **SHOW_FOOT_BOXES(?show)**: show or hide (hidden is default) all element/participant related foot boxes
- **SHOW_INDEX(?show)**: show or hide (hidden is default) the relationship (call) related index (sequence number)

show is defined with `$show=true` and hide is defined with `$show=false`

### SHOW_ELEMENT_DESCRIPTIONS(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Sequence.puml

SHOW_ELEMENT_DESCRIPTIONS()

Person(admin, "Administrator", "People that administrates the products")
System_Boundary(c1, 'Sample')
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
' in a sequence diagram Boundary_End() has to be used instead of  { }
Boundary_End()
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![SHOW_ELEMENT_DESCRIPTIONS() Sample](https://www.plantuml.com/plantuml/png/LL5BJzj04BxxLqp38OuKxARYn8dKjG2910kRShJMte6ijA_kZckXgl-zisqWT2yZpSptchsA909DHcUVb1tr914EH3vUbcKGS_6Yw30DKyGmEajegHYTARqMDc7E8qcjXhAwE6zIwt5tL_xyKcmsnMVkzIt-cD2EMFZ4dxKtzqzzVLVlwdtNVwlRwk6swMxlzss-oh86GtGs5z8ekuR5DbKLAGXoOS6D1ftN27GG1E8qnCWj11-Sd4QAYrNMlaP2qtzravKYlERZPWtBLXX6BrSPyAiuYL0MGpxZq0llcVu91zXwhzKeI3cR5AkpDMpRfjZN7KC20WU3tVSgpRPQkpb2kWiRSC17yO9NpAH99P_Th8Wm02c3chMIioKe2mBYyIeWbNW9mi2RrRwsCb_1GVob733HIyPm7Y71FGFyWj_P_zl7k3dzqsDhHsNMonvGlntqbFGniXckDrtNjBoLbjwd9vfh9BOnOohFmPcFa2kqad_q3m== "SHOW_ELEMENT_DESCRIPTIONS() Sample")

### SHOW_FOOT_BOXES(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Sequence.puml

SHOW_FOOT_BOXES()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample')
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
' in a sequence diagram Boundary_End() has to be used instead of  { }
Boundary_End()
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![SHOW_FOOT_BOXES() Sample](https://www.plantuml.com/plantuml/png/LL4xJyCm4DxpAuuoD9LAGX4J4wKgC02jI0fiaHCVr99Vs1SYXFZldA6yl9nq_fxsQIGHg3SwsrEsqxr4s1BvU5AMGGp5aw9jt_OHG-SieQMYSwRqMjZ4EOWajMhBnV71EgqsrrVbor4ncnM7l6igVExHTbZuf9zLbwlxvdorgfkprSEooYTPjiOGdSs5DCfEOJHFKqKAWbmOJRBgDHAQviprLehmcdUpAOmhORp6yIG3FWjE9PJ5a0_ODi9xLhd75kRUQzK9KiwEUBNOdyAyMXStovef0O53mlNT8jtDjNP3XDGn0ZdWWbumnFIQ53j1FIWY343Ae6QloCd6e2m8YBk689Lu2iB0TzHcQMK-WQtub6mnoKlcS1yXmJq2lC5xzX-zgvlJbnz7spcpNtQB-lkPVfjk8eVXULdNwufH2VHp-ojpWSGn1apZCJZpbtAALlBlV00= "SHOW_FOOT_BOXES() Sample")

### SHOW_INDEX(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Sequence.puml

SHOW_INDEX()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample')
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
' in a sequence diagram Boundary_End() has to be used instead of  { }
Boundary_End()
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![SHOW_INDEX() Sample](https://www.plantuml.com/plantuml/png/LL79JiCm4BtdAuPoQ2gLX29Ed2Yb0YIMYhJ0BNBYQMl96_Q4227-dJ6KpPUHnc-rJoE9G9tHsPwohUuamfR8nvEo3A8lDegsNTD53AspX9QArfdIQs4Jvo2IrAefPyS7YxHQtLoNBqV5P58SygwkyBb3ssBXatvMNTuzrbUtv_EdV9Hb2mpHsLn8e-mO1jCqLQGWo8N1AAjU8w6fprndfGYlUJiPmx0InciSZZBWC-D0GbaCUOzDBRndbKTiOEgzLgqWvUo0LxFzCKohHN4xNp8b870-k7cOfRkfrgwFaEf580VSpGk6c4wJOYTOzee80v0ogDahSh8XA0i2uguSI2KsGHZuZbhFhSn7i1MVaWqcUSaSxYCak3N06xnd_z6xkZbz-N6qdJFxPVUelv_fj-agSXYUbylbec9K0ltS_ifS876C7jDO1sV-KaxHIlwO3m== "SHOW_INDEX() Sample")

## Optional support of additional PlantUML elements

More often a full support of all PlantUML elements are requested.  
They can be set via the new optional `baseShape="...."` argument of the calls

- `System(..., ?baseShape)`,
- `System_Ext(..., ?baseShape)`,
- `Container(..., ?baseShape)`,
- `Container_Ext(..., ?baseShape)`,
- `Component(..., ?baseShape)`,
- `Component_Ext(..., ?baseShape)`

The already specified `...Db...()` and `...Queue...()` calls are not extended.

But based on the additional (internal) overhead it has to be explicit enabled
via `ENABLE_ALL_PLANT_ELEMENTS`. It can be set with following 2 options

- `!ENABLE_ALL_PLANT_ELEMENTS = 1` directly in the scripts file
  BEFORE the first C4\_\* file is loaded, like e.g.

```plantuml
@startuml
!ENABLE_ALL_PLANT_ELEMENTS = 1
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Component.puml
...
@enduml
```

- or via additional command line parameter `-DENABLE_ALL_PLANT_ELEMENTS=1`

If `ENABLE_ALL_PLANT_ELEMENTS` is not set, the diagrams displays the requested "PlantUML element"
but the style is not correct displayed.

**A simple sample with additional "PlantUML elements":**

```plantuml
@startuml
!ENABLE_ALL_PLANT_ELEMENTS = 1
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.11.0/C4_Component.puml

Component(comp, "Copy component")

Component(config, "Config component", $baseShape="package")

ComponentDb(dbA, "DB A")
' alternative syntax for ComponentDb() with $baseShape="database"
Component(dbB, "DB B", $baseShape="database")

Rel_U(comp, config, "Configured by")
Rel_L(comp, dbA, "Reads from")
Rel_R(comp, dbB, "Writes to")

SHOW_LEGEND()
@enduml
```

![Sample with PlantUML elements](https://www.plantuml.com/plantuml/png/NP3DRi8m48JlUOebgbIG82bLJvMGI21g3oP5_8XZPCS6eYQsPM-Wl7tjGX5my-v-CplhiKLgi6tge9FbIKgo8Y6ac9CaNnKPoMPPlbh228P1fv9btN81UqHjt-FOq6Eqgt3VijOAKog9Gc9KgYRMDPNUSc2HrnMB9s-3kM-jPoG-l4R3OVJYUiL4DLf9Bz9-Vt2jkyv4zo6SA7s2yhyRzkuHkQrsVv1_t61zU6BKYkMUQZ4ADIs_wKxSYQUiordYjDCK4ZTv1bgZC99YTH1WJnBf3soLWLj53uxks3jlJf7wChp9nLbwDauVWbnXbsGXwc9zkVBXaDO83kpaA0-H2tIEkn2KMzWQrLp6Y-lOBzsO2eK5L7x5ylDhKv3i8ykdtLum5fAxF_u5)

### List of supported PlantUML elements

| PlantUML element | Support  | Comment                                                                                                               |
| ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| rectangle        | &#x2705; | already supported (works even without ENABLE_ALL_PLANT_ELEMENTS)                                                      |
| database         | &#x2705; | already supported (works even without ENABLE_ALL_PLANT_ELEMENTS)                                                      |
| queue            | &#x2705; | already supported (works even without ENABLE_ALL_PLANT_ELEMENTS)                                                      |
| node             | &#x274C; | **should not be used**, already defined for Node() (works even without ENABLE_ALL_PLANT_ELEMENTS)                     |
| person           | &#x274C; | **should not be used**, already defined for Person() (works even without ENABLE_ALL_PLANT_ELEMENTS)                   |
|                  |          |                                                                                                                       |
| actor            | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| agent            | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| artifact         | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| boundary         | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| card             | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| circle           | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| cloud            | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| collections      | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| control          | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| entity           | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| file             | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| folder           | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| frame            | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| hexagon          | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| interface        | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| label            | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| package          | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| stack            | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| storage          | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| usecase          | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| usecase/         | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
|                  |          |                                                                                                                       |
| actor/           | &#x274C; | requires ENABLE_ALL_PLANT_ELEMENTS, not working (font color not changed to $bkColor) - and/or conflict with existing? |

If `ENABLE_ALL_PLANT_ELEMENTS` is not set, the diagrams displays the requested "PlantUML element"
but the style is not correct.
