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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![LAYOUT_TOP_DOWN Sample](https://www.plantuml.com/plantuml/png/JL1BJyCm3BxtLvXnQ2TjxOOuSLeP20vxLAnZubIbhKSZfKcKk5GJuh_ZYi688bdoz_1dBpm9HrshWYkfAzNL20sHzNT9uaGVlqjgkhBpw2gZ2JN5bMaJguGUD5DFjP9bihoTPaDhlrub7pVnV1RFk5SiMIAaHXVROK2GXB0n11gnnXfAh0GR0pNI0tzg46eyYauHX4cmIj-s-xp8jrdni3ried4GPEYyqP6eMwadC4g7AZqvGSQDni7kv0dRujvqkXRk55Np2OGxqLg5uHW-0-3t5odgiIo4jUnpm19IQvMi14cZHznQNayWtMNnvZ5dYKFWfM3zkXomL2dJUnXkmg4Dy46iO4hBmINFWhoNHEY0P8kAPtdEzdLE5z4Fo3vd6eF12whVhIwnzfwLN9_pFDinQo3zeHUR9oIEqUDGZiwq_oKBr3LV_Xi= "LAYOUT_TOP_DOWN Sample")

`LAYOUT_LEFT_RIGHT()` rotates the flow visualization to _from Left to Right_ and directed relations like `Rel_Left()`, `Rel_Right()`, `Rel_Up()` and `Rel_Down()` are rotated too.

```plantuml
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![LAYOUT_LEFT_RIGHT Sample](https://www.plantuml.com/plantuml/png/JL1DJy905BptLwnue2JGWl7aYTeWc80IMZIUcctxb4tsAxklDiJuttqR4TpBIzxCl9dPkKVki5CokXAwaLqBx81e_LsQEjud7m8FNTrvS8tH21gJngZKIgw3PkAnbQ9Eyzl9DgpsctNwUPFCficKTbLE4YuqkCG6WsYTlJtlosgzU2YhtUDoLSQZADg2yqR7l5L2ZzaW2rDuT1oD6uoYukWHL7LlEjroTuoRsPWD2wwiXE68VKMCtjadxg6kkBLqvnLgbbahHSDH63sWLNuzPbcnJPuM9KaSC4hADYzvm38fJUzPAEeP6aOjBIUAwYGAyc9bBn31CHGA97bvolPzIXVZBqXtJZG2ent8lrQNM7jFIfghijmMn0gaCtevimIa63s4yUwC-Y-PWsxfEty0 "LAYOUT_LEFT_RIGHT Sample")

`LAYOUT_LANDSCAPE()` rotates the default flow visualization to _from Left to Right_ like `LAYOUT_LEFT_RIGHT()` additional **directed relations** like Rel_Left(), Rel_Right(), Rel_Up() and Rel_Down() **are not rotated** anymore.

```plantuml
@startuml LAYOUT_LANDSCAPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![LAYOUT_LANDSCAPE Sample](https://www.plantuml.com/plantuml/png/NP91RwCm48Nl_8hPxA54Ig5TzTHJMOZQ0qrH3AtsX1nm6ql6jkoXgAhsl-yueMcqN2o-D_FcZU7E8tSu3WhAxCzJKxTbjYbOdbLhO7omIaG_fExKs0lO8rf_cwQEJycRnFsu6xrmdT4eD2QT6LAhk0vUbnvx9NTfVdDP1TGybkdxh-JwAhaYrkRKmgKMBh5K74N_JuwNKLG9vusEUJz8lO955axfqN4qRh6Cs8T7CRI_pQXxxZxYxde55yV05qluZ82UqvXu4hkMMqi-Bs87cRLATXobqGj2-SyLPAnADkkQMfm02WgFptdGCgNCv27iwG4Dq9AMKyamAfGq2-f98We7A0UXQ9QdR7_dT34UHVAPoqYCja9zRVKTg_7KIUT3NLUCgaBHIVsskHT8CIOHZbTdXlEMhw5ijM2d2ufPGw_Gs3DI15AOIP-nCh1IlE8PsmQsbMzxd6EtZILt84iAR8yfss1qe0NHsJNmO7RW9V7PEV23uK7Oad2oPmzFBssvlbzlYl3rxuJkwTVu1m== "LAYOUT_LANDSCAPE Sample")

## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype, ?details)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```plantuml
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![LAYOUT_WITH_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL1DJy905BptLwnue2JGWl7aYLe9c00IMoIUcctxb4tsAxklDiJuttqRKTpBIzxCl9dPkKVki5CokXAwaLqBx8Xe_LsQEjudxmAFNTrvS8tH21gJngZKIgw3PkAnbQ9Eyzl9BgpsctNwSPFCficKTbLE4YuqkCG6WsYTlJxjo-hmMAwgzMAvs3x4eoZQWVD6nxnLGe_P80jJU7GSZHkCekBa4LHrRphTSdUAczcO3Gkkh8JXY7r6ZDwVKTn3NN5hwSu1QfPPAqN3KHWze5L-FMPPiKksYv8a3XX5PPkNF62PbARtB3Jr30sZcfOJHNKI1NcniXU8u1WA1PAyF6NxEgUByGUaEsSQWT4poDzMbrXxJqgQgxBS5SGAf3_qScO9I35w2EFD6VLVCWVTqdz-0m== "LAYOUT_WITH_LEGEND Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![SHOW_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL5DJy904BtlhnZnG4cW1UF9axKIE00s5kJORDjLDjclx4vjYF6_Emq8xEKbypxcJVOv8FVOQWN5ycrVhkQB-UOL2gwT4knEcbgrZO03eWjFIU9v5tz9FBHL6uIlhK5XCAwjJfpYfe-P16oKh9BiSPBtezrwbNm_nBDfFALPcP65IoDyx4ZCM2vyi2RYZPPc38EqHndGSxH-C6B5CQ3GvOjjJSFzCQfdOnYUoWr7yCE0tYKowaHLSkSePoygI9rJikOehHdGABiVGrhayMQ-9OiNGALW_P7rNAgKxGBqDmL02tIGuoJHhK99ks3RIKJX0QKMYdO5wlPxRXVXYQISiun8zYxK_rNNMhj0JiBbTfiNfEf55_OQin18DJhHmwUt-jR2Rhuf6h4_ "SHOW_LEGEND Sample")

Legend labels and details can be defined via `\n` in `$legendTest` arguments too.

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml
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

![SHOW_LEGEND Sample, $legendText defines legend details](https://www.plantuml.com/plantuml/png/hLHDRziu4BtxLqpK56i1Zjnksyi21khQscqAnmviPzj30MCaqJ9HYXH8oerGx7_V6Kbsd3X5Bxq8uiVClFVc3TyxZzPNXUhz0QdHUs4zI0_VfTy1PfdqqcXKT5GKg3DGKWj0crU5q1wkfijuDbvV_njlhkUJsTqq7WNHC8e2y0Og9q2P59MgUnTo2o_tQ2KcIcp4lNJUzOEdmK7O0xYGEbLL9k1bBlpc6BD7LOddGeQJjvk9qHu9cOrAPd8Xb1EdgNRUb-wluT3YzoWdPbL2u2pHzSGY8cx3Kg5c5QwSpvHCAEdLBM_TtSo6-p-Zrw-YLyyMqfdSadANIkJqlnRtdNHVDMHYIpST-1tfW8bGm09cWX8e1sRR7ZHnG31i3VqWmVGRhzD3dG2aQwC740YPxpmucOaCt0vBqPns6KFeZRCiLe8xiyRycEo8EHZ0vPOM4wEC7Lt6i_WcdgytVo_eCrdC5aiwJ_BsD7ZnvisxwVWTnpIbHZ4NNt7j5Q_xuU2KzUWS-bTzZZTyHYjJ-LEvZ5OrOASOKreArT11L-kKyNYAx3YCbyl5voDuDkTF3rQ-Lc8qHRSJsOpMPmIQ_C1-RM2IOxLv1BP5c342p5bvhBmfqCl6uq_wJ5kdyvD9HnQhIOZIcfA6J19LjAA9wZfuIfQn37yFO-FzWN7OwwrgvqMn-M0gdQ6j--bhCjOr3OBLmiC7rD-apeCGVj3y01ozqozC8caCiIpf_aspW75P4hfWyc80Nx2WITMylBLcJortt4HPIC_Dhn97sJlF7wibRJNOLZfjTPA-vgSZhHmfAwo3lKIEaHPQ0AJLNgQYUIbEuNNk8toI88nlhncSeivmNaRr2VSuWAcXQnPEH-81xozmCHHA7BJzTwFp-Gfx_ntqZUzzlqkpSSqMoqRNjXOBST0PsjkCOkMDPSt8DfrCAMqSeL2WiKN31Z3XaJbgD01CKsgdfpzlKJjiGDDA-3GYK3qorQF-FHRhpWd721gt3U3JQZ4VVbolRrSFJ5iZXfneC-UfJimJoS-u7h8-69bCGe_faymdFcTpVYGBp-9_ulcq7_RUKtPwPVy7 "SHOW_LEGEND Sample, $legendText defines legend details")

Legend details can be deactivated via `SHOW_LEGEND($details=None())`

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml
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

![SHOW_LEGEND Sample, hide details with $details=None()](https://www.plantuml.com/plantuml/png/hLHDRzf04BtpAoPkge94J3ylbP1AmMrJ4OY0j3rKGcDxCQkkTwtTDOrLzRztnZQ4X5Izz69vFsRclJTlzftpQ7sPgyupI8pU2Uj1UlWf_HOmJQMNHgEYepn7dOAIMW3QhCo5zd0nMKJJqUhoIxI-d8sdDvDe68I3C0p06oYT06KILAhgdCaDFDsXbHWhiHQtqddN3Hu61xqEm9dKYIfJ0KypuTU7c1sgKZmMCXY_Ne-DzaZ8R5WmapEXd3XEjVM-S6y70ui_muoObJ61iqJN4ukGk0qAXPfLk70-LJAcf1VNl7LpDHtiNeOldeVF7osaKxaXvSwLoEX_9MvRwRvhICM6RZhmMz81Ow601Km59L0EpAOvgEE0ODWAka6CoGzU9_iw0KZNHFSX43BRUd0o5IcuBHQYFcqpzg0pIjD82UxC2hD3iWFce0_d6rgCZJ9sU1vDewjejbf_cDDdF9_E5tGUPyrfyEJLgpUJqHkEgKiD8ow-vDfBNdTx_MFMmrFet_KftjuZMfdI7yjbjAe0MyMOqaAecWwwIYUCnrDaos6qMCo_7i2pEVzwiFIL4iC9kgr8fxG-8L3d1_Ph3PCSgyqzi0t2b15WnifZwKsENjOUVz1dsZgUdrGwibX5GXJM53HaagYY5NLKsy5Zienby7yO6-_tZ7kTph9oNkJhzwRKATggcxmWOrtI85WjFBn7_KFgBEZ1BveVW8Dtkhc99OqX5WNTlweNC2eAGXUCd_JX6-OqgPgNrzRigEMEcoXpwRdvPUmeU-lvGxMugGQRKYUDJj9N_7GafIDbXNMmayWnqa83WBJQoKJKByKnlDPzX4yIXD7r9ODJr1dEowW-umxxC35qpSBnIDpX_GSkXaA9WwR_RdWwNxtExxs-qQtljcdMhjvYsUZQnc8kzZf3SvjHBBsnh1dPffKfeOq350eqDg_P0COyCWUD-e19GktqzESjQeSrQ5e9duG4gaEckjU_-sBTEE4OGUssFdnUpcU3JwlLzVAEQMF47YTQptYgO_D0yXEk-wntHYQJq6Fw8FEHpzcSdyZ2q-XZD9jqpzkf6CvCOzrtL8mUtJy= "SHOW_LEGEND Sample, hide details with $details=None()")

## SHOW_FLOATING_LEGEND(?alias, ?hideStereotype, ?details) and LEGEND()

`LAYOUT_WITH_LEGEND()` and SHOW_LEGEND(?hideStereotype)` adds the legend at the bottom right of the picture like below and additional whitespace is created.

```plantuml
@startuml Layout With Whitespace Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![Layout With Whitespace Sample](https://www.plantuml.com/plantuml/png/LP11JyCm38Nl-HMXfqvYwK2SE0tQ2Wu5fbMenofDB5efJQF60VRlSPZKhQVOdzzpdhptA6SCe-6LF4q1UJDWpvj-GF1EAk2r79q1TZDOPO86tYCw_vXbi_mHNwGDNV0mgyaYM1Hg6ZDdf8qRjnwr6ReiVzWU8lfygxBlUt6t4pjYRKuMELYOXICnOmUO_MHJUSkJSycVaWrRL6b7WwNZpmcr2Agt9AfF7c5C5Q5poVELLQ-inRLrmMtvYodGX5x1B-hoMisEODfZp1ZJA6cC9nfX4VF507ID2oEWr-mOmyHlWjCI_p6hNp-QjYfVolSYtR0zM4q7-GC= "Layout With Whitespace Sample")

Therefore a floating legend can be added via SHOW_FLOATING_LEGEND(), positioned with Lay_Distance() and existing whitespace is reused like below.

- `SHOW_FLOATING_LEGEND(?alias, ?hideStereotype): shows the legend in the drawing area
- `LEGEND()`: is the default alias of the created floating legend and can be used in Lay_Distance() call

```plantuml
@startuml Compact Legend Layout Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![Compact Legend Layout Sample](https://www.plantuml.com/plantuml/png/RP5HJy8m58NV-okwnSGjaGsCJoOc89jeCe4CZOzDwGeiATtItQhyUsyP39RuihRVFUUUstNS03TWzufufHRA5fBk0EhcCOuD_ucs9UpisZRIY4g3r129QX_NYcld6JHGg78TJny6IuS-txFu-puQ3QCXCZP52o-rD57j0WXPIjDKEk1tr6-tTEA7f9C5Qonq9_hiun6as6aKhGuDo7qW4BLREkrPYvurkRPscAM_44Yiu1hHYpgzLfDSAfQx6TqqWYlL87KmSVEv0V1tN1Y2eizoDuoBiNN1uOY9jx5QG8atpj9PEa-2a7X6WZMQ-XjLSIZrbYcvbRhmYOVVivwiNXTVx2LRJ3xUvZDsSf-RX2JZ1vQK-8XQo0uVuqSOIswfTzDI-aJzDe1n8xcFfNzRd-GXrdkzJ_pSUeoDy57_00== "Compact Legend Layout Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH Sample](https://www.plantuml.com/plantuml/png/NL1BIyD04BxdLuprq1JQf1LFdXf3iM2hmQIAfx19LhkmBtOdXYB-TsTfjU9U1kPxpYuzCeUzah39NXztLPsLTNc_gl8rb4nPoQCBeLlPTnpsYDRVfAbZG_8kSDytlUUkDHgvngGrAhMIwU0ryzX9qQJvzQm8gzrsatvS9OjvCgTTdPE42SrTOeaSHV-JuqaK5TnvesFMAQ6dCCh251uTG-D6awWyUEIglZMzxfWxnErY2kDZuV44FYEWzniJ3xofcRNayy8RoAoLecKeZ1xHAh-SGbOMoSEg8edZG4LX-vm7B9FI31x2dHxG01rf6L5KBr5G5bI3GEGEK2WkASjJjwzJknYF8FcSQ0H6Jrp-N7MkjVEafBckgg8aLY3zecUREuvKO-1Xl3cZ_agMN7VXDxy1 "LAYOUT_AS_SKETCH Sample")

Additional styles and the footer text can be changed with SET_SKETCH_STYLE():

- `SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)`:
  Enables the modification of different sketch styles and footer.

The possible font name(s) depend on the output format (e.g. PNG uses fonts which are installed on the server and SVG fonts have to be installed on the client).
Additional is it possible to define comma separated fall back fonts (if the diagrams are exported as SVG. Atm
PNG does not support fallback fonts based on a PlantUML [bug](https://forum.plantuml.net/14842/specify-fall-back-fonts-is-not-working), but this could be fixed in one of the following versions)

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH with custom style png Sample](https://www.plantuml.com/plantuml/png/VLFRQjj047ttLqpLG6HGxAJqgM28Aum3JLpJbHFo95RIEDvwBs9t5DUK_djduskXhLvMcZbdpfcTqMqWwQapklTEsLft3SAAg0sVXaClDuCNHQkkwWBwsbb2IuFQcM6hfOsSgq2DLjKm_tWrZw75m_tmzSFWvdfmpR4oPufK5lsWZG8zCIbAyMLIv7UbA9xl9-b5zP8xxVmeqUfbHPNkCCdWOicyVVmGsaXlbJsW6-dN7fiTrX7wfrrwb8WrKhqw9GhyGQCazoW96rWw3uqATHU2SZRfztgNC9zDOSDTGbI5xzgKjJ7gvXfIshQgbbflGLf7A_GxY0h0zz7q_z9EpC-amL5oghDJ4Oy75IvOoNhzLYl0Wu0frrPrbZkZQX3Inc06fqz-Nqczhfpq3OZ98JN33ZEeEn_KAxy4HbxncDJot7YKT1r1SjHXE-pcFyx_vUZCq9z-pkmSt9pCnExlnyzV5qKv5dlDb6DpzC7PL3P6sGoISJnL82_9UUQ8RI0qvMVNMPxrDgrlChWKqhGQB_lmimVy7BShtM1LohRbEazOmRXjDRTFSS8SojzdC1RpmMnICCKZy7x2msCUSsEjtUPjd3u0EU3TRYL3JAT9iHOKV86yHK3Ae6QjmDv-xTsbj4jodJqiDliDzQ6hawr5O2QVTqKn5uoAe6FsL6QAl16qmNWilJFdb5kq3Vz4lm4= "LAYOUT_AS_SKETCH with custom style png Sample")

SVG with fallback fonts MS Gothic,Comic Sans MS,Comic Sans,Chalkboard SE,Comic Neue,cursive,sans-serif

![LAYOUT_AS_SKETCH with custom style svg Sample](https://www.plantuml.com/plantuml/svg/VLFRQjj047ttLqpLG1HGV2bzAXZY2fD0RTTKSaAUn4eQnrllHUoEufhIV-ziRDakfTNBIZFdp3cpCxhp91orMlNUILEfjaRO43N-qs3WnAx_8cdJbgr7Lrb3QAXVMJreb321S-kfLh8Sf1zlbo6qciy6hn_wes5_oB4YPOgG1bs_2GAzR9eNsPTfdZuKMVuycyPNvKjgbNNZICcN3PMgnIY1gpNpZl4kj1FEIDEXQ-6s3ki3rXAwfqDw76LRf6fpJkJuWyPHwb0Grh2s3chfgzPxQKrqq-jTmt9n3plk4e8gV5UwgBIMeo74j6za9PJQWp2MDkWE4Ec1xwE-OUxV3GN4GcWSH-TA1vtiiTFXagMejc_LFCmpkEVgiafIgsK5cJ0XcC3vazytGcrBArpDcbrgWIqcKBNEorT-yOoyvK79zQNr86bRWkYamtR-v_jVVYxi_EdcmapdvMmbz3wRF7zTvSKaEsh675kYyzR4ejRI911DmYazEK7M1ODxJwYBpxOrFEjzN8qIkCw4RXHUty3F7l1psgvuXsKXceRhF649awPHt3o52NCeVP_095ls5zESAGw1znFcZsd8JPIokxTnEWzaWNUx4GpHhIB9Mf3pzV4M0KcDYhKyU_jrT1VJ8SbrZh3Gx3TKNLTdMolFJ3uVydoPCIg0JjbpcNlaVQ0TXcFjhBwatA6f-IVw3G== "LAYOUT_AS_SKETCH with custom style svg Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![HIDE_STEREOTYPE Sample](https://www.plantuml.com/plantuml/png/JL3BJiCm4BpdAqmvD9NQf4MSE3MKY29HY9eKn2boaeLQyalsXgX2_3jhKLfyMMbdPcV6Iu_SOQzaT25qA_iEs1xH-fiqTNn8FWJk-wRtu5gZ4JGchL6fbLm7pSnZ9qMJhgvdHLZjDe_fvrMoc2TpsjKhad2XmIKs64JhXxkyBgjycpzNRqKUJwAe0EUDZdcdX9woKHQcyEWu6ZUQHEN18wZwrlIwu-uGjuif6vTSMGdZ2VkA6BsJIpn0KtDhwSuhD2opLegMep1wHAlLvPHbPP4yvHL9733AoJOlgu1bKfh1ir3JCpICEbfE5DLB5EJ5ga4WWcCe54ZoyfJj-vWknb-GxXnf14PRa7-jph5sdfGqrrLLbCGAf1DwFdCFI3462EFT6VLViWJTqMV-00== "HIDE_STEREOTYPE Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

![Predefined sprites Sample](https://www.plantuml.com/plantuml/png/XOxD2i8m48JlVOhOau9DQl7agJzNXOBqB6cpsa2QXcHhNz-jA0eUFEqmp7upUK3fSHeCSnuKNBK5nOBp6Y6minoSWMYbRMSc1Qn7TE4WX9SplsdiftOAuBlH8bZatJW8PwHTQ4b0PNGhgdrIBrPpEefxndSfJycxLFGYgSfpH-4egi67qQuNMh5bSKEN5J6fcLf-bp7tp2-1bzfy8yeteloBo3wCZ20vM4M37W== "Predefined sprites Sample")

### Using HIDE_PERSON_SPRITE()

```plantuml
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![HIDE_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL3DJy8m5B_thwXuO2ImWV7aYJaN8H5SsDJZqcrLclGhxPiBCVxllWO44tjvoVjzlYuzC0UzadIrViZh8j-LpzkwB7RhAgSbKrPoSYLqA_kEqps0zNT9ujWGVmZOzqtlkMkD1guXRerAh6GwkCqyT58qINOxAyBgPVEKVDx4YtaynrsTeOG9pLriaKp8_-neGaZ1dJSwOfqIUaf7QPZ2WsDWt6X2oeC7hkfxq-kEkKFKBgPqVAmydj0lGl6TWwA1DpMp5dtUU4DJQwLe6GYZHxZAhgSqBOjucrSeSPnYLRfvpGAMIca6JyEbdeAXUAPbI56z185Pj1e407SKXE8Iipns-pwrY-08ei-9XY3PSVbxrQNMYqSbpbLL5IMo0kcCNcmUEM2DWOVnxepwArbotON__04= "HIDE_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE()

```plantuml
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![SHOW_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL5HIyCm47xFhpZdGplOsYa--RGvXWewozhfOqdRqmRI92HNYuZ_tQjJ9nW21_Tzzztt9Sj0qbFVQSXl7fxARBFB7xPbdkrkYmtaidCQnOaojUuRX9R8XSiqzN98NXIrVTK7zBKrX8QIsdQfqzACQlD0ZLPLkhwOPsDhVt-NlfudPujamRropIDI6VI9Ox8GQGHRIs0G6soWmbgoC52h0l2b5g71PzbhWe7NGd1U4SB4eG_MJ21AnN_tyLI8x8iGowPJPWQJrLXL82_9-ibKv6-1i2klR6yQwT_Y-cm6qI5qD8Lt0Nn-hSO3LgLqZdMUi8ALSrhLaXGRuDRwT0QhF4kscu97F0A7XVl7zOYjjBP3WF6jE8m5VYWdcT9n8CMxeE1KX1v8TQXvLs1l7z_kOZg0hFDDOr3iKF-aEjhQ1vxaUbCKMSwiaVIB7cMkaTZ6W6DvzhRxEx94qum_yWa= "SHOW_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE(sprite)

```plantuml
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml
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

![SHOW_PERSON_SPRITE(sprite) Sample](https://www.plantuml.com/plantuml/png/ZL1DJy904BttLwnui2RGHUF9azWGCL5eQDLZixG3RB9VsPtQ4ED_TrOGZ2VtCjbvR-QzUNS1XSTEg-HCcaPrBR0jeWktd7lHPnk9ssxL1V2DDGW6iyPgxfGmSMOKi5LonVERKH5RByzF_FqwknfdO-hLEOq8QS1dxbkWXJNzc0sYeFy_T78lmXPQBKtBVmH6re49q7HUuaxuPYiH6kmyN8yapGQkHK3mftCESZotMbjpiF8NV25bBfJQmqavMxpLnNHPBkPrMImVgsaw86eT3TOR3s3ge_JWCaaAyC6QL4IhGpQOn2e3Ue7M4rxko9AkxsrdMk5tQNCrP1Ubq4x1nINxI1YzOrXf3wjQE4Txtc359iufsGYKrWoebPyFsQGiilcqeX4FZE9cpwzvn2PAsJwmQ38mj8mYT88ekbCeIOjLlKJAXg7Ke4WhaBVFWxiKzo3jET3YOKjGFrUTR55O8UhDggeeYHL9H_IqvW6GRFGGozfR_Nla3anBINy1 "SHOW_PERSON_SPRITE(sprite)")

### Using SHOW_PERSON_PORTRAIT()

```plantuml
@startuml SHOW_PERSON_PORTRAIT() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![SHOW_PERSON_PORTRAIT() Sample](https://www.plantuml.com/plantuml/png/RL5BIyD04BxdLunLQ0erKV4a2COYAgWDJRJ7i4d6Tc6pk-nE34NyxywQ-ZYOGtOpyyttc5nv4exwJa5njrnN-SsgM3vL-N9LhhBxCfv18JghC3gGkb5zYx0biluYJPqOaesaRL_t7brZDA6cf35TQfNGWV7OKwjadIxEZ_DGUdvyID_EajEJv8HhrO97XDJe4ilWAFfVFufoTDxeMBITr7EOPE6KdfmWuoQpgDXvmgwwDhrkXTl5pUaSfgFfwGpU8-3dHoeUiAw4jSopnXeoQvLi14cZ9rnQ7CuXA_BawQRa4OV0Pk7nPH5wcL9cy12oUY037DGAXdIz8ibQK0wI21sGx52nbcTl7tjtCOrDvjd3k1bDGRw20FkL3wGFd3LFji2OBNUyTP8GQ8iwlC1XGq9lM4o9dUafpB2X5iI6qtqlQkHZgV5x91kfECZHUBkSZB2pO6I5wdkzl_jvzXo1pxkop0j61T1FzpVFBHBlOy1ml3hJ_HsvGjtoh_q4 "SHOW_PERSON_PORTRAIT()")

### Using SHOW_PERSON_OUTLINE()

> This call requires PlantUML version >= v1.2021.4!

```plantuml
@startuml SHOW_PERSON_OUTLINE() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![SHOW_PERSON_OUTLINE() Sample](https://www.plantuml.com/plantuml/png/RL7VIyCm47xlNt5EOHtCLiKdGN2EeO9knNRwMDBst09f4fAhPOZ_knSxdG_seKdlllj-N6yy2KTTgo2_NxsMsU8vNotBrRfuV5WkuWdaehKAeoEfQzKr25iYww_Ir8a-sKZQTbNdqTL64sfAQjEcLWaT24yzDKfMwVpoD0kbzTDZ-dwHd9ybPrmhvpmYf4QNM0P7qR_oKPIXyqR7eccbdi9e5axfoGaoRZI9yfqdRCjRq-b6k5rSdqzXF7WUJ-0Z0dv-bU8Ugr9OopolMC7CMYLhGTBe4PVcnrEOvLcoN1GyuX3OApozp4DlffJfFOIe7iW0vxI28MsdIB8M5BqaGWSaMrIivTdRvzvTJ4EJUVOmRaPZa6yWm7xd0-a3PyMJ3J1conrldIG4sg8EBt1Oaz0R5bDYPpeACsoe0R7XT3-B6lXOQlWUo0Og3d8otAv70-mY67b6zRFUmtxMdYFmULyKMSwe0Fhj7lBS8V4-UWp7cpFjtv4Rr4tuiry= "SHOW_PERSON_OUTLINE()")

## (C4 styled) Sequence diagram specific layout options

- **SHOW_ELEMENT_DESCRIPTIONS(?show)**: show or hide (hidden is default) all element/participant related descriptions
- **SHOW_FOOT_BOXES(?show)**: show or hide (hidden is default) all element/participant related foot boxes
- **SHOW_INDEX(?show)**: show or hide (hidden is default) the relationship (call) related index (sequence number)

show is defined with `$show=true` and hide is defined with `$show=false`

### SHOW_ELEMENT_DESCRIPTIONS(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Sequence.puml

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

![SHOW_ELEMENT_DESCRIPTIONS() Sample](https://www.plantuml.com/plantuml/png/LL5BJzj04BxxLqp38OuKRAXwwedKM814WeLDELfhxq1MsXUxurgewd_lB0qDx6MacVbUinUHHA39wEoBigEU9CAUoCVlPHd4N3mhsa_3536CpX9QAaPdIg-5JPZJI5AheQo-dJQfzR2zBNzzBSxFYZFkzIs-J6X7B7pYpzhhkyU-lgstzQxhB-kskhzfkfkxNPkligp149tDXJJAhc6nILL52e9SM72ZGUSr0kq5WJWECN8BmGSdfv7YOfMrhv7Gz3_SPAK8h_bulePbAmoZbwiC-5MSH2YB8Pznw8NtJF-80soyrseKf9nDYjN96ZPjK-pgZY41WOF1zcULPXkjtHmXtOKDEE2ZUC4hPjAaaizkLaGOW9H1pLh9sHAK1G7nS1MGIZm7OU3TQbzRcQzWBzue1qpqaZ6SHqXmJm2_uK_sUViGDwT_UcpjeCnwsJtgzuCUapv4DiFrkkkQbhVIql_faUOAYMtCcCfJSEOZv0Ajv1_z2m== "SHOW_ELEMENT_DESCRIPTIONS() Sample")

### SHOW_FOOT_BOXES(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Sequence.puml

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

![SHOW_FOOT_BOXES() Sample](https://www.plantuml.com/plantuml/png/LL79JiCm4BtdAuPoQ2gr2I1Ed2XLWGFGYeJb5Zdnb5hoXZqXGeX_PmnbysMayLljqqWYK6zqjgTiftk9i2NoyQGiWnYA9qNRlkqZXivPGaj5vqpfjR29CuiajMhBnV5idLPtrrVbor5nU50SyAwfyBb7ss7XatvMNQuUclFLgcxELe_BAfzasHf3T3ONqYWxXT4yJHKf279XDCcgrqXecZFNMod2QzuTJc5S2UCrZYSPy5bmAg4iXdp0jX7Uiye3jZ3tNgjEa79snAl5_XJcrRguMTPC2GWS4gxl5-bkhhKR8gIE4SW15_I28QRNfDW9wa4HOG1I1ZLxHKus1cL1GDmr1Ad4Kn06lgCsIolp2Mp5fsIBILuoX_i82Mu3y0RlsN_qhcvENtuSRUVCVjajwkzd-crw5paCpykwNbUCIg2Vsr-P2oIECM0Qc-3CNyefMic_ym4= "SHOW_FOOT_BOXES() Sample")

### SHOW_INDEX(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Sequence.puml

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

![SHOW_INDEX() Sample](https://www.plantuml.com/plantuml/png/LL79JiCm4BtdAuPoQ2gL110dJfHI0H8j5IcKM-J40xNa3Nj2X13_pXXQ5bz66h_LFeia0dL6PtlAjhgJ21iY7q_BCeY-U5QqwPekOcYT9RHKjCwKNWkRE0UHf5PDEJqvMARL_VocV3qkZWwBGzxL5RvqQ5iiVDBFgglRTNszk9WzvgCiMsA8pkP26cN7C9YagI85GIuCHbdr5WbDVUuwAqLuozkZCGmhORp6uIW3FbCE99J5aFVOrC9xLbbZ0nFljMe5AMS7l9hkZs5IBOl5RCMKWC3vOFumJNSJhLqV8TMBG0wucnSCCPqcnKwmwXKH1Y1bKBDNv6H3K1O4n6qva4ey1s5W5xMUMPcFO2E-91jCyf8vt4T8S4y0x_2H_KTlw-RqxSVHjixibzsXtZtJRzFxo65uNgrMoufH2VHp-ojpYSGnUapZAJZpbtA6LlB7V08= "SHOW_INDEX() Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Component.puml
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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Component.puml

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

![Sample with PlantUML elements](https://www.plantuml.com/plantuml/png/NP3DRi8m48JlUOebgbIG886gfqf8912r1vDM_8XZPCS6eYQsPM-Wl7tjGX5my-v-CplhYKLgi6tge9FbIKgo8Y6a-299lYeoaispVBM4COo2JYNBkkK2zeZQliMneSTeL-6-PQqLfbGIXSIeL4siQogzvS0YhoiMJry7NxwrdfFuy1ADXj7GzOgfQhIINgJz_k1QTvs9xaCuLVe4vNytxDqZSblj_Y3_kC7wyCIe5SizrM8SQbf-qvsu4yzObxF4QMSf96xo3BH6OIJ5wY30dYJI7zWg0xUA7XpTiNVUd2BrPNYJYxFqR9m-1Bd2Bib2rCNwSkN38QqH7DZ9KHuY5-WSTo4ejx0rghcC5zUnNxen5GeBgFoAvSVdfY3PUvRFkhrW8YHtV_mB)

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
