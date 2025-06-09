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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![LAYOUT_TOP_DOWN Sample](https://www.plantuml.com/plantuml/png/JL1BJyCm3BxtLvXnQ2TjBKESEAqC18SzAjOnSQhIrgEHqYHANAe9yTznnTY88bdoz_1dppq9HrshWYkfAzNL20sHzVT9uaGVVqXgkhBpw2gZ2JN5bMaJguGUD5DFjP9bihYRPaDhjrecdxVnx3Q-uLwnO8cG6briXm514iBQ46Z46cieiH9i3DH83_ofGQZn83f542R1CdtVxF8YtsJ5usQ_ZiP1aA7pHaUYRgMUm2WTglJa11at6WVReoTiYmVJwLguOrJD9X1kHMiLXcFu2e3VELBKOra8QzbdZoMarYfP2P96ZxYrk9v0kitYzLFE4eV0Iy7gRJ5WgLAczp3SX4CRu8DOmPIMWqkU1NalYT01oHOLp_ASxVkKBg9Va7rED0Q3LrH_MrrYxJmhkRxaURPbra0wenURPoIEqUDG3iwq_oLpr3LV_WS= "LAYOUT_TOP_DOWN Sample")

`LAYOUT_LEFT_RIGHT()` rotates the flow visualization to _from Left to Right_ and directed relations like `Rel_Left()`, `Rel_Right()`, `Rel_Up()` and `Rel_Down()` are rotated too.

```plantuml
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![LAYOUT_LEFT_RIGHT Sample](https://www.plantuml.com/plantuml/png/JL1DJy905BptLwnue2JG2l7aYKeGJ40RMZIUcctxb4tsAxklDiJuttqR4TpBIzxCl9dPkKVki5CokXAwaLqBx81e_LsQEjud7m8FNTrvS8tH21gJngZKIgw3PkAnbQ9E5xUJFApssqtwEKkci-I6TjM295neS8aD1j4cUtlUbzLc-L1MkyVLken7KPI3yqR7l5L2ZzaW2rDuT1oD6uoYukWHL7LlEjroTuoRwPWD2wwiXE68VKMCtjadxg6kkBLqvnLgbbahHSDH63sWrU9wpB8YJvwM9KaSC4hAjY-BW6LIcjwpKDGpD8nQMauKrKaKvCNANY22OoWKIFBobEtxb2x6Nv3kd6W4HZkGVwqkiVQUb3JNPPaNn0gaCtevimAa63s4yUwC-Y-PWsxfEty0 "LAYOUT_LEFT_RIGHT Sample")

`LAYOUT_LANDSCAPE()` rotates the default flow visualization to _from Left to Right_ like `LAYOUT_LEFT_RIGHT()` additional **directed relations** like Rel_Left(), Rel_Right(), Rel_Up() and Rel_Down() **are not rotated** anymore.

```plantuml
@startuml LAYOUT_LANDSCAPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![LAYOUT_LANDSCAPE Sample](https://www.plantuml.com/plantuml/png/NP91RwCm48Nl_8hPxA54Ig6jUkgfB4JjWQOeXbPxGWwuZILZM_PGLAtsl-yueMcqN2o-D_FcZU7U8tSu3WhAxFTpKxTbjYbOdbLhO7omIaG_fExKs0lO8rf_bwQEJycxnFsu6xrmdT4eD2QT6LAhk0vUbnvx9NTfVdjP1TGybUd7JN9zarmHQtDguL8BbrWgZgB_9yVBAAg4yqR7l1-aNi4Y2wVqw3WQjrX6xDEZ6DfVPjGzTvznTxs2YsFWYoNyYO2UqvXu4hkMMqi-hs87cRLATXobqGj2-SyLPAnADkkQMfm02WfFBtdGCgNCv27iwG4Dq9AMKyamAfGq2-f98We7A0UXQ9QdR7_dT34UHVAPoqYCja9zRVKTg_7KIUTZNLUCgaBHIVssUH18CIOHZZTdXlEMhw5ijM2d2ufPGw_Gs3DI15AOIP-nCh1IlE4PsmQsbUzxd6EtZILt84iAR8yfss1qe0NHsJNmO7RW9V7PEV23uK7Oad2oPu_FhssvVbXlYl3rxuNkwTVu1m== "LAYOUT_LANDSCAPE Sample")

## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype, ?details)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```plantuml
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![LAYOUT_WITH_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL1DJy905BptLwnue2JGYl7aYLe9c00IMoIUcctxb4tsAxklDiJuttqR4TpBIzxCl9dPcKVki5CokXAwaLqBx81e_NsQEjud7m8FNTrvS8tH21gJngZKIgw3PkAnbQ9Eyxl9DgnswrNwUPjCRvCRsbKvIRZGu18R3A9LzlQyAwlzKxciLlF5VFCOZw9e2yuR7VDM2JrcWonCuT5nD6umYegZHr3LW-bqozqnRgPZDYouiXA68_OLCNfdexY7kkBMqfqzr2opLeg6ep1wGAlyUiooOfjivYL9732AojQlUS0oAKtlMMZg6Hf6DIqdYkea2l9YPIyGmJ4K2YHvUShsVKeNuoz8Tquq0gCNa7-jBh5sdfGqbsMvBOWLI6VqScO1I35w2EFT6VLVCWFTqd_-00== "LAYOUT_WITH_LEGEND Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![SHOW_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL5DJy904BtlhnZnG4cW5UB9axKIE00s5kJORDjLDjclx4vjYF6_Emq8xEKbypxcJVOv8FVOQWN5ycrVhkQB-UOL2gwT4knEcbgrZO03eWjFIU9v5tz9FBHL6uIlhK5XCAwjJfpYfe-P16oKh9BiSPBtezrwbNpFukaiVg1PcP65IoDyx4ZCM2vyi2RYZPPc38EqHndGSxH-C6B5CQ3GvOjjJSFzCQgdOnYUoWr7yCE0tYKowaHLSkSePoygI9rJikOehHdGABiVGrhayMQ-9OiNGALW_P7rNAgKxGBqDmL02tIGuoJHhK99ks3RIKJX0QKMYdO5wlPxRXVXYQISiun8zYxK_rNNMhj0JiBbTfiNfEf55_OQin18DJhHmwUt-jR2Rhuf6h4_ "SHOW_LEGEND Sample")

Legend labels and details can be defined via `\n` in `$legendTest` arguments too.

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml
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

![SHOW_LEGEND Sample, $legendText defines legend details](https://www.plantuml.com/plantuml/png/hLHDRziu4BtxLqpK5BK0Hzv-NHOmKDTMjoaSEx2TtHuA62E9bebIf41IReIY_xqpakmuSHPxsOiWVipCUs_Uy8FpQ7rLgDuhI8tU2-j1UlWX_GumowINHgEYew90dO6IMW3Ql2g4zd0rNSQpyVhwxtXpFP_CxgRnA8Y6KHI0Dr0v0Sgag5JTkv1RUBb7Ap5HOYFkfVEk7pmD3i8Um8NKgQeo0IzpuJV7c3sgIZmNCfoysqoCzaZ8R5GoamkXd3XDjVE-T7yEXnP_H3angn82Puck9nOHSHkM2ZMhSELyfcH2IQzkUUlkPZRSlubUlud-UBQGpkIMbBjK8gV_jRZlfFkc8HDRkkd0xqW7J8G25Z0Jb40vCDlse8a3Wc5hw0S9fjzvdHxg121T6ps0GCXyvy79J6JWTbYAvhJB649ld6Mn4joPDUR7P4VCmG0kjxIO66Niw3AUnJVnVBtvjA3FP35RBEayoTlJuCNRj--du_SSqvGQnLnynRLNlEw7WrFMetFet_Gvtl0PhKpbJ-KoMjM0dM9CQIbKGmTThLF6uocoup1UBXV_7C6pEV_rOELh9KPJT3kHpMXzHg393-pN1YOvLfj7O5k46IF0d9N7ofi2lMmy_gJFj7KwFvbqPB6QX2YjAMd89555AvgeheEdP1dByFzXRBm_C0vxlLNjl2Ws7qsbCxHrFtrDnhgcGR1QUFY8-hlKUH32JveVWADt-eL998qXbYNTlsaMC2vBGXTCNWpWAnOqgPgNjzRigUMEcoWBwRdvLU8eU-VvOxMahGRRIgUjJjBN_7IabIDbXNMmbyWnqa8BWBJQorGqByKflCvzX4yIXF7jDODJr1dEowY-u1u7C3LqpSBfI3pW_GzS38KI1st_tUXyliBUhuE-yRtlTsashjbYsUZQrc8X3Zf3UvjHhBonh1dPffCffOqZ50eqjcZO02OyCaUD1e1fIktqzESjQeSDQ5e9dqO4gaUcUjI_nsBTEU4OGUEs0NnPBUR3p-lrxUg1QMl4a1DjvZpLYNaY-HdNGzO78vD9w35zald4vspEpsJXMVnNF9_smzu7oawlx6y= "SHOW_LEGEND Sample, $legendText defines legend details")

Legend details can be deactivated via `SHOW_LEGEND($details=None())`

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml
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

![SHOW_LEGEND Sample, hide details with $details=None()](https://www.plantuml.com/plantuml/png/hLHDRzf04BtpAoPkge94J3ylbP1AmMrJ4OY0j3rKGcDxCQkkTwtTDOrLzRztnZQ4X5Izz69vFsRclJTlzftpQ7sPgyupI8pU2Uj1UlWf_HOmJQMNHgEYepn7dOAIMW3QhCo5zd0nMKJJqUhoIxI-d8sdDvDe68I3C0p06oYT06KILAhgdCaDFDsXbHWhiHQtqddN3Hu61xqEm9dKYIfJ0KypuTU7c1sgKZmMCXY_Ne-DzaZ8R5WmapEXd3XEjVM-S6y70ui_muoObJ61iqJN4ukGk0qAXPfLk70-LJAcf1VNl7LpDHtiNeOlNeRF7osaKxaXvSwLoEX_9MvRwRvhICM6RZhmMz81Ow601Km59L0EpAOvgEE0ODWAka6CoGzU9_iw0KZNHFSX43BRUd0o5IcuBHQYFcqpzg0pIjD82UxC2hD3iWFce0_d6rgCZJ9sU1vDewjejbf_cDDdF9_E5tGUPyrfyEJLgpUJqHkEgKiD8ow-vDfBNdTx_MFMmrFet_KftjuZMfdI7yjbjAe0MyMOqaAecWwwIYUCnrDaos6qMCo_7i2pEVzwiFIL4iC9kgr8fxG-8L3d1_Ph3PCSgyqzi0t2b15WnifZwKsENjOUVz1dsZgUdrGwibX5GXJM53HaagYY5NLKsy5Zienby7yO6-_tZ7kTph9oNkJhzwRKATggcxmWOrtI85WjFBn7_KFgBEZ1BveVW8Dtkhc99OqX5WNTlweNC2eAGXUCd_JX6-OqgPgNrzRigEMEcoXpwRdvPUmeU-lvGxMugGQRKYUDJj9N_7GafIDbXNMmayWnqa83WBJQoKJKByKnlDPzX4yIXD7r9ODJr1dEowW-umxxC35qpSBnIDpX_GSkXaA9WwR_RdWwNxtExxs-qQtljcdMhjvYsUZQnc8kzZf3SvjHBBsnh1dPffKfeOq350eqDg_P0COyCWUD-e19GktqzESjQeSrQ5e9duG4gaEckjU_-sBTEE4OGUssFdnUpcU3JwlLzVAEQMF47YTQptYgO_D0yXEk-wntHYQJq6Fw8FEHpzcSdyZ2q-XZD9jqpzkf6CvCOzrtL8mUtJy= "SHOW_LEGEND Sample, hide details with $details=None()")

## SHOW_FLOATING_LEGEND(?alias, ?hideStereotype, ?details) and LEGEND()

`LAYOUT_WITH_LEGEND()` and SHOW_LEGEND(?hideStereotype)` adds the legend at the bottom right of the picture like below and additional whitespace is created.

```plantuml
@startuml Layout With Whitespace Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![Layout With Whitespace Sample](https://www.plantuml.com/plantuml/png/LP11JyCm38Nl-HMXfqvYAKoSE0tQ2Wu5fbQenofDB5efJQF60VRlSPZKRQVOdzzpdhptA1SCa-6LFCu1UJlYmDjXHF1EAk2Dd9m1TZDQPO86FY0w_vXbY_mHNwGDVV2mgDaYM1HgdZ9df8qRjnwr6ViiVzWU8lfygxBldRZVYJjYNKuMELfOX2CnOmTO_6nJUSkJKycVaWrRLMbFWxNZpmcr26gm96gE7c5A5Q5JoVChgxwo5fVM5NVbBwP04te5FwlBIpMhmNHrp1ZJA6cC9nfX4VF507IDCoEWhraTmyHlWjCI_p5hNZ_QhYfVolSYtR0zM4q7-GC= "Layout With Whitespace Sample")

Therefore a floating legend can be added via SHOW_FLOATING_LEGEND(), positioned with Lay_Distance() and existing whitespace is reused like below.

- `SHOW_FLOATING_LEGEND(?alias, ?hideStereotype): shows the legend in the drawing area
- `LEGEND()`: is the default alias of the created floating legend and can be used in Lay_Distance() call

```plantuml
@startuml Compact Legend Layout Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![Compact Legend Layout Sample](https://www.plantuml.com/plantuml/png/RP5HJy8m58NV-okwnSGjaKs8JoOc89jeCe4CZOzDwGeiATtItQhyUsyP39RuihRVFUUUstNS03TWzufufHRA5fBk0EhcCOuD_ucs9UpisZRIY4g3r129QX_NYcld6JHGg78TJny6IuS-txFuUnGDHz4zCZP52o-rD57j0WXPIjDKEk1tr6-tTEA7f9C5Qonq9_hiun6as6aKhGuDo7qW4BLREkrPYvurkRPscAM_44Yiu1hHYpgzLfDSAfQx6TqqWYlL87KmSVEv0V1tN1Y2eizoDuoBiNN1uOY9jx5QG8atpj9PEa-2a7X6WZMQ-XjLSIZrbYcvbRhmYOVVivwiNXTVx2LRJ3xUvZDsSf-RX2JZ1vQK-8XQo0uVuuSOIswfTzDI-aJzDe1n8xcFfNzRd-GXrdkzJ_pSUeoDy57_00== "Compact Legend Layout Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH Sample](https://www.plantuml.com/plantuml/png/NL1BIyD04BxdLuprq1JQn1PFdXf3iM2hmQIAfx19LhkmBtOdXYB-TsTfjU9U1kPxpYuzCeUzah39NXztLPsLTNc_gl8rb4nPoQCBeLlPTnpsYDRVfAbZG_8kSDytlUUkDHgvngGrAhMIwU0ryzX9qQJvzQm8gzrsatuialaYkQ9TdPE42SrTOeaSHV-JuqaK5TnvesFMAQ6dCCh251uTG-D6awWyUEIglZMzxfWxnEry2kDZuV44FYEWzniJ3xofcRNayy8RoAoLecKeZ1xHAh-SGbOMoSEg8edZG4LX-vm7B9FI31x2dHxG01rf6L5KBr5G5bI3GEGEK2WkASjJjwzJknYF8FcSQ0H6Jrp-N7MkjVEafBckgg8aLY3zecUREuvKO-1Xl3cZ_agMN7VXDxy1 "LAYOUT_AS_SKETCH Sample")

Additional styles and the footer text can be changed with SET_SKETCH_STYLE():

- `SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)`:
  Enables the modification of different sketch styles and footer.

The possible font name(s) depend on the output format (e.g. PNG uses fonts which are installed on the server and SVG fonts have to be installed on the client).
Additional is it possible to define comma separated fall back fonts (if the diagrams are exported as SVG. Atm
PNG does not support fallback fonts based on a PlantUML [bug](https://forum.plantuml.net/14842/specify-fall-back-fonts-is-not-working), but this could be fixed in one of the following versions)

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH with custom style png Sample](https://www.plantuml.com/plantuml/png/VLFRQjj047ttLqpLG1HGx2JqgM28Aum3JLpJLHBo95RIsDvwBs9t5DU4_djduskXhLvMcZbdpfcTqMqWwQapklT1sLft3SAIg0sV1mClr_s5ecLNTG5zxIoXfNxjpA3LqaREPQ16gsgGVxgSnT3Zm_tWzQP_VTE_ubYPCqKgYxxVHe6U61Ub-3ekyhjI52_tu_IiMkHEEpzCj5eigT8T9XcSpPctY-z3Q-cjidjq8_tAOxF5EaB_l4qF4x52gfV7H84_QPZa7YLX0tFdeL6Xxa9GpYONlTuvpAOJM7EN45NXXpPbROowleAKDgsgfTORaDRH4lqMeWBmVJGNVsadvgVIu30vrjcgYAUz2XUiPBrwhnNWGS24QwiwovrHDGXfOp23uoU_BwLULKxw1iHudvfYXndKdG_gbLy28ozvJ6f-QZnAkeuWEUYm7NRp7-V_SdHYw4y_9tRsRevcOlVtevTlZqKv4ZlDb6CpzC7PL3P6sGoIKJnL82_9UUQ8JI0qvHVNMPxr9gslCpWNqhGQpo_WhGVy7BOhNMDLohRbEizOmQXjDRTFSS8SoZzcC1Ap_dHSCCKZy7x2mrCUSoEjtVfzd3u0EU3TRYL3JAT9iHOKV86yHK3Ae6QjmDv-xTobj4rodHqiDliTzRwhewt7m4m-xufY9XWLGOViiSm4UIDeZV6OUsTEARTe6_w9VWC= "LAYOUT_AS_SKETCH with custom style png Sample")

SVG with fallback fonts MS Gothic,Comic Sans MS,Comic Sans,Chalkboard SE,Comic Neue,cursive,sans-serif

![LAYOUT_AS_SKETCH with custom style svg Sample](https://www.plantuml.com/plantuml/svg/VLFRQjj047ttLqpLG6IGxIJqgM28Aum3TLnJoGbv4YjfR6-z5x4xYcj2_xspyRMKLYyhpPmpvypEwDwJSDHgrVaWJQNQ6c5DrFZFWu4Js_vAqhejMu-kieRGKB-oUj0eOGAdvwbMiXoadthp45eyJWUlT_tRk_uDnugKAK8QTFqc27IoSLvaNyTv-b1a-Sjq75-LgzGgwuQHagirbQh5A86h9VCEyMDeAvoHveYkXTiuhFTOI-YUz-bXb6sGglKvaUDF6aQfGq5Omz8wgAMlMk-bDL6tqxc6-Mm2M-uIWYhyKBgej9QtDn3Jhf6LK6e7mbXQezj3f0U-ZxhBtByR2eYPq3YCpfNsEjdJKOTBbgBQl5Vpy9Z1XAlBAacjbXLameHW0kTFVbyBjIcjS3Lh7bCpR361gdLUllABPsIF1oMNbzQ3f6q9efCEs_cVxt_vkR3pfviBCqSlPokXz-devTiYBqRPGJFcs1oTjoOMjPOcWMWKJkd92R8k6DnvGbryiQtXMU_YwZQ1wqpeHk5r5zuwmCzfk-8jbeLe6gxpZ2MCcaPnynGcpA7qOmAZRDwVZNEcE0JUJtXyIaDkf9JTle_JUI0BlDkDO8Xk5KdMWfolZxS8I6fKhENPsw-3kvZsIQvpW8LclwCwTdMsjV3CvFCXp-SPemBeb3sNcI3l0sqn74jdzINb7atDFz5l "LAYOUT_AS_SKETCH with custom style svg Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![HIDE_STEREOTYPE Sample](https://www.plantuml.com/plantuml/png/JL3BJiCm4BpdAqmvD9NQX5QSE3MKY29HY9eKn2boaeLQyalsXgX2_3jhKLfyMMbdPcV6Iu_SOQzaT25qA_iEs1xH-fiqTNn8FWJk-wRtu5gZ4JGchL6fbLm7pSnZ9qMJhgvdHLZjDe_fvoAPBv8hsjKhad2XmIKs64JhXxkyBgjycpzNRqKUJwAe0EUDZdcdX9woKHQcyEWu6ZUQHEN18wZwrlIwu-uGj_Cf6vTSMGdZ2VkA6BsJIpn0KtDhwSuhD2opLegMep1wHAlLvPHbPP4yvHL9733AoJOlgu1bKfh1ir3JCpICEbfE5DLB5EJ5ga4WWcCe54ZoyfJj-vWknb-GxXnf14PRa7-jph5sdfGqrrLLbCGAf1DwFdCFI3462EFT6VLViWJTqMV-00== "HIDE_STEREOTYPE Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

![Predefined sprites Sample](https://www.plantuml.com/plantuml/png/XOxD2i8m48JlVOhOau9Dj7Zor9-hGa5wbjYiDf2c8TdOrtShYe87JpiCizzC4L1wZ8DXpeE2gxQWM71U8mHsaeCpa2oqxKnKm7f45_P2U3dncyO-Nc80tuqMmIBlna4u8-rCom8geo-YtcNDRBN7WxZdV9lp3NddcbuaLNdkA9ma3VWmskLCAzSiRUcoCYKrKSllCkQU-JdmKgjlHFL6L7yH-OUH4wG0gsZG0m== "Predefined sprites Sample")

### Using HIDE_PERSON_SPRITE()

```plantuml
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![HIDE_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL3DJy8m5B_thwXuO2ImYV7aYJaN8H5SsD3ZqcrLclGhxPiBCVxllWO44tjvoVjzlYuyC0UzadIvUiph8j-MBvkwBBQhAgSbKrPoSYLqA_kEqps0zVT9ujWGVmZOzqtlkMkD1guXRerAh6GwkCqyT58qINOtAy9gjtvEFc_Z-MryWxiwGmaJchlO8fcG_zdHX922Eszqn3ebz9IEqZ251yV0kD64b0SFNDKFfjSTSuUedK_f-5XvFA5VXE8x1qK3RsfcBVgyyOQcrahHCX16Zt2LNKzfMXRn9gzGuZZ5gdJzcWKibT8CdePBFGL3yKpBaA9w2GApQ3K80Eue2CKbPddizdrg5y4HH9yJ3K6ovVBtgakjdKSbpcLL5IMo0kcCNcoUE62DWOVnxepwArbmtON__04= "HIDE_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE()

```plantuml
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![SHOW_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL7BQiCm4BphAxRf8GuaTXDwwYbf24sXJKpiDaSZsvj684j2MjU4qd_lkaqVK25Os9cTdP7cWQIdjj6GhRVx8btjikscoDBTVRw2J3PEexXGfj9jZN0aSk4cIRpiuXT5nxPi0_hA6a93SMMRn6bfUhL9e5ghCbbUJzA-zVJuaBpEukailk9UiUGHgGpws35PY6G86qjW46kieSHAiZ3GKGNWIqU46W-orGGThuNWl2A4WKCVh1d0C17_tKSZ8T9FGYJhHfan31PzLO6y9Ei78v6T0c5JtDhMrDAVecewXk5NwE48tWJm-R4QTLWMqZdMsMC92-UqgYGfDi2jvUKO5baQRrOvZtW43WkFpyiUMsXjkm3zMt4O2_nGJZAbuK2ATq7EgGWza6fGywx0tjxFxYBw0bddJ6DGx51_f_grzHHuakiwpzECMJtf1_sLkKDY6ntsvU1jytTaZgRkV-G3 "SHOW_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE(sprite)

```plantuml
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml
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

![SHOW_PERSON_SPRITE(sprite) Sample](https://www.plantuml.com/plantuml/png/ZL1DJy904BttLwnui2RGLUB94zWGDL5eQ95ZixI3RB9VsPtQ4ED_TrOHZ2VtCjbvR-QzUPE0mcEdLN8cJQEw5jWEqOLRphteirU9ksxJ1V2DDGW6iyPgxfGmSMOKi5Lom_ERKH5Rg-Sd_ZREhiVP5VNgd4Q4DE0pzoNGmfP-p0PHqFyVEhaNOGUjbgRbFm8Zwy04Q3elSIzyivC83NOUnYD9iu5h4H3ywPo37C-jrjOShFm5LwJCXLBVS58-BDPrCLkMYtbT5il7QfOEY5f7W_Mh1p3rKNfmcIG5-61DAgBL8HjCOvK1lK3h2I_tP4dNTxOphV3xjBaUiejIQAVWufAz9upUCQoqXqqjdACzQzYmgNDADWAbDGDgvUT3DYsBR3whQCG3exZPyqiUiQbIjWyicWmCBQC8dI2AxXHAqc9LBv6oOIWrAD8AvEtZu2x5Rv3s76Zni2MedwjEjYYi4FKUggeeYHL9H_IqvXwGRFGGozPR_Nja0gQbf3y1 "SHOW_PERSON_SPRITE(sprite)")

### Using SHOW_PERSON_PORTRAIT()

```plantuml
@startuml SHOW_PERSON_PORTRAIT() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![SHOW_PERSON_PORTRAIT() Sample](https://www.plantuml.com/plantuml/png/RL7VIyCm47xlNt5EOHtCLeTFWc0TeeAwibPzB6bxRe4q2SdLCiJ_tOjrweDzQDAxxxuVrqjFmb7VAIXkLozLVhqkLezLlbgNw-okZ6TGYCugZ0waRbJV8co9h3zFKoU6P2DfszUzHzSOJQWfQKoNMYLqO3psr2fPfykpupoKdXxkqxT5Shf8JhXMBNb4I8qkiGoEel_reoX7vusEHTj9FOT95axfoGaoRZABYfqdxAehq-jMk5tSdCvXEfgUpk0z0dv-fE81wqfOopmlM4DchPAD86dqX4lBmpbaHPuyNfSyuX3OB3myBqClKyeC7a9M3sI0Wrh1aAvN95aBoa4IeGEI7IhMykpjuzjTJ6EJURvXt8oc85z1WFtA1z87pfedMs3CbZlUEaa8j4KTNk2m8Q4tBAR4plGKPjXG2sB3wVQB6lbOQlmUoKOg3d8qtYuc8smHZAnHxTVxkvydpn7ul2tBl61K0FrqV_FS8F4-1Wp7gpFTtv5Br2t_say= "SHOW_PERSON_PORTRAIT()")

### Using SHOW_PERSON_OUTLINE()

> This call requires PlantUML version >= v1.2021.4!

```plantuml
@startuml SHOW_PERSON_OUTLINE() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Container.puml

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

![SHOW_PERSON_OUTLINE() Sample](https://www.plantuml.com/plantuml/png/RL5BIyD04BxdLunLQ0erqU994AobgA1jQ58zXaqojWkRtMLtOYZYVtVM-3gOGtOpyyttc5nx4ewwLa5-jtuki-KcNw_AzRPuk5yjumdaehKAeoEfQzKr27iYwo_Jr8a-sKdQTrNdqTL64sfAQjEcLWaT24yzDKfMwUBYD0kbxUD3-ZfBpcV96TVA1Oy8gT4bbi5HzAzy56NelD6nQ5gffp2QXrDwSeAC6qsY_E09s_B6TBeHxX3NvrCO3vx74tYBW9yVfRZ7gXJMCiypLZ2tLibQa3HwnAN5yHJcUPQibWMFE0Js2ezFYz2RAsLw3o6g1pB0EQrWIDifagm5HI-9q0795XLhUVRs_kKkfg79F5ymRaPZa2yWm7xc0-a3PyMJ3J1cpnrldIG4sgCEBt1Oaz0x5bFYO3eACsoe0R7ZTD-B6lXOQlWUo0Og3d8otAv60smMZ6nGVQ_tTpzRpn7ul2kAB6TK0FrqV_FS8l4-UWp7YpFjtv5hr4tuiny= "SHOW_PERSON_OUTLINE()")

## (C4 styled) Sequence diagram specific layout options

- **SHOW_ELEMENT_DESCRIPTIONS(?show)**: show or hide (hidden is default) all element/participant related descriptions
- **SHOW_FOOT_BOXES(?show)**: show or hide (hidden is default) all element/participant related foot boxes
- **SHOW_INDEX(?show)**: show or hide (hidden is default) the relationship (call) related index (sequence number)

show is defined with `$show=true` and hide is defined with `$show=false`

### SHOW_ELEMENT_DESCRIPTIONS(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Sequence.puml

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

![SHOW_ELEMENT_DESCRIPTIONS() Sample](https://www.plantuml.com/plantuml/png/LL5BJzj04BxxLqp38OuKx89wwedKM814WeLDELfhxq1MsXUxurgewd_lB0qDx6MacVbUinUHHA39wEoBigEU9CAUoCVlPHd4N3mhsa_3536CpX9QAaPdIg-5JPZJI5AheQo-dJQfzR2zBN-T5sVdnLVkzIs-J6X7B7pYpzhhkyU-lgstzQxhB-kskhzfkfkxNPkligp149tDXJJAhc6nILL52e9SM72ZGUSr0kq5WJWECN8BmGSdfv7YOfMrhv7Gz3_SPAK8h_bujePbAmoZbwiC-5MSH2YB8Pznw8NtJF-80soyrseKf9nDYjN96ZPjK-pgZY41WOF1zcULPXkjtHmXtOKDEE2ZUC4hPjAaaizkLaGOW9H1pLh9sHAK1G7nS1MGIZm7OU3TQbzRcQzWBzue1qpqaZ6SHqXmJm2_uK_sUViGDwT_UcpjeCnwsJtgzuCUapv4DiFrkkkQbhVIql_faUOAYMtCcCfJSEOZv0Ajv1_z2m== "SHOW_ELEMENT_DESCRIPTIONS() Sample")

### SHOW_FOOT_BOXES(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Sequence.puml

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

![SHOW_FOOT_BOXES() Sample](https://www.plantuml.com/plantuml/png/LL79JiCm4BtdAuPoQ2gr2I1Ed2XLWGFGYeJb5Zdnb5hoXZqXGeX_PmnbysMayLljqqWYK6zqjgTiftk9i2NoyQGiWnYA9qNRlkqZXivPGaj5vqpfjR29CuiajMhBnV5idLPtrrVbor5nU5GSyAwfyBb7ss7XatvMNQuUclFLgcxELe_BAfzasHf3T3ONqYWxXT4yJHKf279XDCcgrqXecZFNMod2QzuTJc5S2UCrZYSPy5bmAg4iXdp0jX7Uiye3jZ3tNgjEa79snAl5_XJcrRguMTPC2GWS4gxl5-bkhhKR8gIE4SW15_I28QRNfDW9wa4HOG1I1ZLxHKus1cL1GDmr1Ad4Kn06lgCsIolp2Mp5fsIBILuoX_i82Mu3y0RlsN_qhcvENtuSRUVCVjajwkzd-crw5paCpykwNbUCIg2Vsr-P2oIECM0Qc-3CNyefMic_ym4= "SHOW_FOOT_BOXES() Sample")

### SHOW_INDEX(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Sequence.puml

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

![SHOW_INDEX() Sample](https://www.plantuml.com/plantuml/png/LL79JiCm4BtdAuPoQ2gLX29Ed2Yb0YGe5IcKM-J40xNa3Nj2X13_pXXQ5bz66h_LFeqa0dL6PtlAjhgJ21iY7q_ACeY-U5QqwPekOcYT9RHKjCwKNWkRE0UHf5PDEJi-MARL_Srr-NfKJ8wAGzxL5RvqQ5iiVDBFgilRTNsrE9y_vgCiMsA8pkP26cN7C9YcgI85GIuCHbdr5WbDVUOwAqLuozl968QLC5xZS9G1dna74ifYo7jiQk4zgwonWQdtMhM2bBC3Nitsnp2jbiLYlc9AGE1ySFCmItTJhLqV8TMBG0wucnSCCPqcnKwmwXKH1Y1bKBDNv6H3K1O4n6qva4ey1s5W5xMUMvcFO2E-91jCyf8vt4T8S4y0x_2H_KTlw-RqxSVHjixibzsXtZtJRzFxo65uNgvMoufH2VHp-ojpWSGnUapZAJZpbtAALlB7V08= "SHOW_INDEX() Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Component.puml
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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.12.0/C4_Component.puml

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

![Sample with PlantUML elements](https://www.plantuml.com/plantuml/png/NP3DRi8m48JlUOfjLAaWGL9GJvMGI21g3oP5_8XZPCS6eYQsPM-Wl7tjGX5my-v-CplhiKLgi6tgu2dBavHaHK98CIT9lYeoaisoVBM44Go2fqgMTSi5x16rVOzZGu_Hhi9zorehJAaa2ebHgPfOrrHwoxv5NbSidhprvxwrdf7uC8m6m-ZLzOg9QhIINgJz_k1QTvo9xa4uKVe4vNytxDuZSblj_Y3_kC5wyCoe5SizrM8KQbf-qvsu4qzPXxF4QQSf96xo0hH6OIJ5wY30dYJI7zWg0xUABXpTiNVUd2BrPNYJYxFqR9m-1Bd2Bib2rCNwSkN38QqH7DZ9KHuY5-WSTo4ejx0rghcC5zUnNxen5GeBgFoAvUVNfY3PHvPFEzrWB2HtV_mB)

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
