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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![LAYOUT_TOP_DOWN Sample - open link](https://www.plantuml.com/plantuml/svg/JL1BJyCm3BxtLvXnQ2TjBGDEd5O6WiCU5UkOE5Lfwz58QH8bBjM4-E-u0ZQYI9RyFVpPSq_2KTUgu4BgIdKrGaDa_LsIED77xvAQhkmykifeGarnPTh4Ag47pTHJhMIPB6wdsT3QhPR9ntKykuclk5SiM2AaHXVROK2GXB0s11gnnXfAh0GR0pNI0tzg46eyY4uHX4cmJDyskxp8DrdniDclet4GPEYyqP6eMwadC4g7AZqvGSQDni7sw0dRujvqkXRk65Mp2OHRqLg5uHW-0-1tYXJrM1R2MlRPOmcfjKfMWgJH8sujBYUGRhDu_PYpn27mKh1wNGnOgfJfFGmtuT06-21MCANbu99dGTvB8dH0iaN5ipnd-_fD5z4Fo3w_D0Q35rH_MvrZxJmhkJxdURPbra0weMUR9oIEqUDG3iwq_oLpr3LV_Xi= "LAYOUT_TOP_DOWN Sample")](https://www.plantuml.com/plantuml/uml/JL1BJyCm3BxtLvXnQ2TjBGDEd5O6WiCU5UkOE5Lfwz58QH8bBjM4-E-u0ZQYI9RyFVpPSq_2KTUgu4BgIdKrGaDa_LsIED77xvAQhkmykifeGarnPTh4Ag47pTHJhMIPB6wdsT3QhPR9ntKykuclk5SiM2AaHXVROK2GXB0s11gnnXfAh0GR0pNI0tzg46eyY4uHX4cmJDyskxp8DrdniDclet4GPEYyqP6eMwadC4g7AZqvGSQDni7sw0dRujvqkXRk65Mp2OHRqLg5uHW-0-1tYXJrM1R2MlRPOmcfjKfMWgJH8sujBYUGRhDu_PYpn27mKh1wNGnOgfJfFGmtuT06-21MCANbu99dGTvB8dH0iaN5ipnd-_fD5z4Fo3w_D0Q35rH_MvrZxJmhkJxdURPbra0weMUR9oIEqUDG3iwq_oLpr3LV_Xi=)

`LAYOUT_LEFT_RIGHT()` rotates the flow visualization to _from Left to Right_ and directed relations like `Rel_Left()`, `Rel_Right()`, `Rel_Up()` and `Rel_Down()` are rotated too.

```plantuml
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![LAYOUT_LEFT_RIGHT Sample - open link](https://www.plantuml.com/plantuml/svg/JL1DJy905BptLwnue2JGYdhoH6qGJ40RA1fFpRPzoYRxbTrN6sByxxwD2Exb9Mzctipip2Dts2aPNGZToAu5jaUq_YvD7U-J3u7xhkuykCPe18r9OrHg9TT1C_7OIb6d-Usa2AlTUfL-NYVJc-IATbLE4YuqkCG6WsYLlJtlocerVoYhpUDYMSQZA2h0UQDZtYgXnsoGXIayEex63KRHzk0HL7LlEjroTuYRwPWDjrnP2SCH-ueOlPDFt4DTSMlfpYlKBBDMYeQZC7f0g_nopB9jaJpDIv8uO9IKhL_oW6LIcjwpKDGpD8nQMauKrKaKvCNANY22OoWKIFBobEtxc2x6Nv3k76a4HXkGVwtEiNQUb3INPLbiYHL89_HyPW58CNe8uzqPzLyo0ztIT_u0 "LAYOUT_LEFT_RIGHT Sample")](https://www.plantuml.com/plantuml/uml/JL1DJy905BptLwnue2JGYdhoH6qGJ40RA1fFpRPzoYRxbTrN6sByxxwD2Exb9Mzctipip2Dts2aPNGZToAu5jaUq_YvD7U-J3u7xhkuykCPe18r9OrHg9TT1C_7OIb6d-Usa2AlTUfL-NYVJc-IATbLE4YuqkCG6WsYLlJtlocerVoYhpUDYMSQZA2h0UQDZtYgXnsoGXIayEex63KRHzk0HL7LlEjroTuYRwPWDjrnP2SCH-ueOlPDFt4DTSMlfpYlKBBDMYeQZC7f0g_nopB9jaJpDIv8uO9IKhL_oW6LIcjwpKDGpD8nQMauKrKaKvCNANY22OoWKIFBobEtxc2x6Nv3k76a4HXkGVwtEiNQUb3INPLbiYHL89_HyPW58CNe8uzqPzLyo0ztIT_u0)

`LAYOUT_LANDSCAPE()` rotates the default flow visualization to _from Left to Right_ like `LAYOUT_LEFT_RIGHT()` additional **directed relations** like Rel_Left(), Rel_Right(), Rel_Up() and Rel_Down() **are not rotated** anymore.

```plantuml
@startuml LAYOUT_LANDSCAPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![LAYOUT_LANDSCAPE Sample - open link](https://www.plantuml.com/plantuml/svg/NP91RwCm48Nl_8hPxA54Ic6xxMbFfH2r1vgY6BRg2JdWDfQCRTd3ecgr_tt72KsZSh7utioRDuPRZzpXE2WeivUdfcxBR5EmFAlMmFXWbOY-ITsfiHUmHxJ-LvewFYLl4lVZRlJ2TKQZq9XqPaYjuZfuNNhibTob-Srb5L3pMAP_VYPNryaFOcrEBLnguH9BnL7qTNAyZA9AE6zqpFj1wXKiid1AZuwZSOjbnDuzYg6zCwFkkNkFkwiLN1m3NopXRmJqdCR4azYrt5hoUHOxoAnLikCeZLuGoh-l86DLibdNrE84K51u_9q7BLFAJ1x2dXxG02rfEPKCeq99iw2U9A9mW78GYcPvolPlJXVZKIIVkOp4Q2lKnrQViHfFdNG-r7N5g2eKdTHFctk156CIuNXrPZXl-HZALWjskg2ODVGAZJqZHI25cVGPAmChnIkUiMrWM_csnpbssrXo1xAamFQOiWr61reGdLq33sO7NXAVdGC_61w4BGadU_RmzDoMw_lrfWXV_rReddwD_m== "LAYOUT_LANDSCAPE Sample")](https://www.plantuml.com/plantuml/uml/NP91RwCm48Nl_8hPxA54Ic6xxMbFfH2r1vgY6BRg2JdWDfQCRTd3ecgr_tt72KsZSh7utioRDuPRZzpXE2WeivUdfcxBR5EmFAlMmFXWbOY-ITsfiHUmHxJ-LvewFYLl4lVZRlJ2TKQZq9XqPaYjuZfuNNhibTob-Srb5L3pMAP_VYPNryaFOcrEBLnguH9BnL7qTNAyZA9AE6zqpFj1wXKiid1AZuwZSOjbnDuzYg6zCwFkkNkFkwiLN1m3NopXRmJqdCR4azYrt5hoUHOxoAnLikCeZLuGoh-l86DLibdNrE84K51u_9q7BLFAJ1x2dXxG02rfEPKCeq99iw2U9A9mW78GYcPvolPlJXVZKIIVkOp4Q2lKnrQViHfFdNG-r7N5g2eKdTHFctk156CIuNXrPZXl-HZALWjskg2ODVGAZJqZHI25cVGPAmChnIkUiMrWM_csnpbssrXo1xAamFQOiWr61reGdLq33sO7NXAVdGC_61w4BGadU_RmzDoMw_lrfWXV_rReddwD_m==)

## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype, ?details)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```plantuml
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![LAYOUT_WITH_LEGEND Sample - open link](https://www.plantuml.com/plantuml/svg/JL1DJy905BptLwnue2JGYdhoHAq4J40RAH9FpRPzoYRxbTrN6sByxxwD2Exb9Mzctipip2Dts2aPNGZToAu5jaUq_YvD7U-J3u7xhkuykCPe18r9OrHg9TT1C_7OIb6d-Usa2AljUfL-NYVJc-IATbLE4YuqkCG6WsYLlJrloshtM2whrNmnVtg8Hr5KWFD6nxnLGe_P80jJU7GSZHkCeit18wZgtdIwvUuGDzCn6swuiXA68_OLCNedexY7kkBMqfqTr2opLeg6ep1wGAlySiooJP4ypKkIE60KbQrVyu1bKfhUiz3KCpICQbfE5DL95EJ5obuWWcCe54ZoyfJj-vWknb-GxXnf14Ol8FzQdMDjFIbfBikos10ha4xe-Sm2a6Bq4CQxC-g_P0QwfV_y0G== "LAYOUT_WITH_LEGEND Sample")](https://www.plantuml.com/plantuml/uml/JL1DJy905BptLwnue2JGYdhoHAq4J40RAH9FpRPzoYRxbTrN6sByxxwD2Exb9Mzctipip2Dts2aPNGZToAu5jaUq_YvD7U-J3u7xhkuykCPe18r9OrHg9TT1C_7OIb6d-Usa2AljUfL-NYVJc-IATbLE4YuqkCG6WsYLlJrloshtM2whrNmnVtg8Hr5KWFD6nxnLGe_P80jJU7GSZHkCeit18wZgtdIwvUuGDzCn6swuiXA68_OLCNedexY7kkBMqfqTr2opLeg6ep1wGAlySiooJP4ypKkIE60KbQrVyu1bKfhUiz3KCpICQbfE5DL95EJ5obuWWcCe54ZoyfJj-vWknb-GxXnf14Ol8FzQdMDjFIbfBikos10ha4xe-Sm2a6Bq4CQxC-g_P0QwfV_y0G==)

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![SHOW_LEGEND Sample - open link](https://www.plantuml.com/plantuml/svg/JL5DJy904BtlhnZnG4cW5VNaoLe97029BN9ijkqgc-nNTgSsnFZVdGO4zlAIUH_p9liSa7jijO9yyROhbxFvRFqAETTE2NOZJQtQHi0UqOMd9F6yYxyaxjkg3SBNrg0m6DTM9qvnqyTC0ZPALadsEDdqe-rgcNpVnzE7-8vcPKOMBetmiICnOnlXWpKHRxGqOnYaFSg0dgFrWn7B3m65BbziQnhk3r4z7SFmM6uuWXy6zCwHKIUgaZj7EJjHGUgSaZL7QSs0Hjdj6D9y4wzd1Lcy02e5gu-ivrAbR1UWloa0Mg2372U9RXLAsWL59n651vHQADeLgDllgLs4Hv9oJZ8YsRjG_rTTQcq3EGaNHR79ITMBpkmbPYwGQdIYXqzlzRM5NNrJD69_ "SHOW_LEGEND Sample")](https://www.plantuml.com/plantuml/uml/JL5DJy904BtlhnZnG4cW5VNaoLe97029BN9ijkqgc-nNTgSsnFZVdGO4zlAIUH_p9liSa7jijO9yyROhbxFvRFqAETTE2NOZJQtQHi0UqOMd9F6yYxyaxjkg3SBNrg0m6DTM9qvnqyTC0ZPALadsEDdqe-rgcNpVnzE7-8vcPKOMBetmiICnOnlXWpKHRxGqOnYaFSg0dgFrWn7B3m65BbziQnhk3r4z7SFmM6uuWXy6zCwHKIUgaZj7EJjHGUgSaZL7QSs0Hjdj6D9y4wzd1Lcy02e5gu-ivrAbR1UWloa0Mg2372U9RXLAsWL59n651vHQADeLgDllgLs4Hv9oJZ8YsRjG_rTTQcq3EGaNHR79ITMBpkmbPYwGQdIYXqzlzRM5NNrJD69_)

Legend labels and details can be defined via `\n` in `$legendTest` arguments too.

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml
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

[![SHOW_LEGEND Sample, $legendText defines legend details - open link](https://www.plantuml.com/plantuml/svg/hLHDRzj64BthLumP1n41cMhgvb90G1I9QHp8aY79JGu1X26veXPPxXAxIyL4aV_U6PAIPSj5BxaGt8-PUU_DcttlF5fV5Qht1bAZzy9wa1v-IBy3p3BffT6ewAWeK6UWf1Q0DgyAeJrSJPVnRBo--JlUtCmdi_jfF0gYOHG5u0rKJe0oAIfLzoxa5bxlqKfCbDY81-cywmVFWuEm1t0XTQggJC3hNFZDCMQFgX8lXGmdVsmcHdiaP3OgcSc5K4wSfjfvNxe_XqEBFwASc5K9WRD4rnEBYBWDIuMQLRXoFbCoeQHNTxnrVpiRxd-Ftbv7lxrOI6ToIyfTAf7J_reyTD9zqv29BTrqu7Ua0oP20GkO2KgW79XjUz340S6mDVI31DFll4uFTGAGheqUG21allFWP2OoS3iiHNFQPGoXDywoM0dkp1hpOx8Zvc00brjQJ8moTdGPp-BRUBxUV5pGPxAOBPPqdkJjQV3g-lhTTFoEOvfIevYBhxZsYjVzS73AUdGE_Pi-nnk-e9Mf_AbSHgiQi5ECAIs5QkYWgtNAU3n5TXp6o-NYon4yc_C_3rQ-Lc8qHRSJsOpMPmIQ_C1-RM2IOxLv0hP5c342p5bvhBmfqCl6uy_wJ5kdyvD9HnQhIOZIcfA6J19LjAA9wZfuIfQn37yDO-FzWN7OwwrgvqMn-M0gdQ6j--bRCjOD3OBLmiC7rD-bpeCG_g7v0JXwfr-OHD8OObdI_Tjc0UEo97J1vDK0lc91awfvUMVDdbhkk8coa9wRNoMEidUUFrPBscgmhNJQwYHzpKz7MZbILbW7UuaS8osq04YhlKn5yrASmklSH_WaGHZVtJ0uHPtXl8pgC-vn05D3rooSZiGZtl_1nL0eST3stutEvoli_Jpe6p_uVfTcuvejbeskRIqMug0pjBSPnSeRovgHRJgPKjeuGg50Ouk63M328tFKQ02OfjHEJt_UedROWAQLy6b4e7fagYVzUohMlHEE4JHk6y3drM8-_BHUtwqUcRP633dHPivJdPXdafznFMHzD3APX1xJPvbFVCxc_4GMdiL_nVDfF-ozf-pqoluB "SHOW_LEGEND Sample, $legendText defines legend details")](https://www.plantuml.com/plantuml/uml/hLHDRzj64BthLumP1n41cMhgvb90G1I9QHp8aY79JGu1X26veXPPxXAxIyL4aV_U6PAIPSj5BxaGt8-PUU_DcttlF5fV5Qht1bAZzy9wa1v-IBy3p3BffT6ewAWeK6UWf1Q0DgyAeJrSJPVnRBo--JlUtCmdi_jfF0gYOHG5u0rKJe0oAIfLzoxa5bxlqKfCbDY81-cywmVFWuEm1t0XTQggJC3hNFZDCMQFgX8lXGmdVsmcHdiaP3OgcSc5K4wSfjfvNxe_XqEBFwASc5K9WRD4rnEBYBWDIuMQLRXoFbCoeQHNTxnrVpiRxd-Ftbv7lxrOI6ToIyfTAf7J_reyTD9zqv29BTrqu7Ua0oP20GkO2KgW79XjUz340S6mDVI31DFll4uFTGAGheqUG21allFWP2OoS3iiHNFQPGoXDywoM0dkp1hpOx8Zvc00brjQJ8moTdGPp-BRUBxUV5pGPxAOBPPqdkJjQV3g-lhTTFoEOvfIevYBhxZsYjVzS73AUdGE_Pi-nnk-e9Mf_AbSHgiQi5ECAIs5QkYWgtNAU3n5TXp6o-NYon4yc_C_3rQ-Lc8qHRSJsOpMPmIQ_C1-RM2IOxLv0hP5c342p5bvhBmfqCl6uy_wJ5kdyvD9HnQhIOZIcfA6J19LjAA9wZfuIfQn37yDO-FzWN7OwwrgvqMn-M0gdQ6j--bRCjOD3OBLmiC7rD-bpeCG_g7v0JXwfr-OHD8OObdI_Tjc0UEo97J1vDK0lc91awfvUMVDdbhkk8coa9wRNoMEidUUFrPBscgmhNJQwYHzpKz7MZbILbW7UuaS8osq04YhlKn5yrASmklSH_WaGHZVtJ0uHPtXl8pgC-vn05D3rooSZiGZtl_1nL0eST3stutEvoli_Jpe6p_uVfTcuvejbeskRIqMug0pjBSPnSeRovgHRJgPKjeuGg50Ouk63M328tFKQ02OfjHEJt_UedROWAQLy6b4e7fagYVzUohMlHEE4JHk6y3drM8-_BHUtwqUcRP633dHPivJdPXdafznFMHzD3APX1xJPvbFVCxc_4GMdiL_nVDfF-ozf-pqoluB)

Legend details can be deactivated via `SHOW_LEGEND($details=None())`

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml
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

[![SHOW_LEGEND Sample, hide details with $details=None() - open link](https://www.plantuml.com/plantuml/svg/hLJVRzf847xdhvWugGeICUtbyd8IKYcuRI824P1h7ogXiRsOLTUxrkwQnZhrVxyPsn0IShgNlbZU7pFpVTzyin-SH-lBN7NUGcBqJbWFqiDFwRU0QIgzD1eL7UKvwXIKr0BGPcKkj8VBoIAQZbOtVqVhczbu-Z29Xa4u2CC0l87I2L0cGQMgpfdSm9iTMecn4clnA9rttU1bSD3h09n9dQWo5V0c4tvzYDcXAiLh8OFnd-knqHu9cGqBPd8cb1F7gRRU5-wlmS3Ypp0ZPcLCu2pHzSGY96w3Gg5c5IwTJvMCAUdbFMyzt4q7kp_2zrVXkrSBwLHkIBaB9JBwNud7Lhhl6bAnePiE_9Pqm5WeO05JGGcK0xDf3keu81YsWcuGO_A3ryc-JW3IDT5z28JCjXwSJ4KARek5g4_RZ3teZD8qKe8xiyBiaEo0EUZ3nOOMOwEC7Lv4q-WkcgtMd-Rq6S-dymMTnrbp6fnVNLrFHjSSKvSQHbnyoRMNlExs-iUiXwVGl-jJlBrNj3AbFvRBQ5K1jeenfOLGDHrqbKuOZwV8biDeiPX_FO1dS_xdmT9NIWmdwBOYdTBwX42T7zYlDKnoh3RFm3O8KqQ06IkFfJSvUbbx_4MVQUjuVbBfo68L2L5OKz2GIQAALjHHRGUFoJAMmUzXRBpVC-vrEilAUP6lFvfIfsYhRlAUZ7L3Ws2ryF0HzG-fiw07_z3y01oyqyrDB6aCiIZe_bszW55H4BfWVDw7RvZJf6fUtbkpevOxRgBCfUVcbx6ZxAtd3zNYfXfiIfqqEabVyTEHb8wK5TR1JYB7I0iD0D9g9nDHlnJ7y5ht4Jv944RtDmnEKMSuBwEwnHtsOMBeceNZaNZ2-p-u60eb3fh-k-7fVFKwl_RwHe--swPPktgBPQDh6ukvsEiCpMr6iVJ6icPacrQcX3OEK2ZGsBnc0nZpo1mqwWCc2RNJqv-tg1tMe6abV18Ig0wPwbd_delru8HZ1BNR-d2xdCy6NrQh--KJqyQ8FKwqdl5Kn-Q5v2TSzrcVZ4mceSVqHUOZdxCvlv25fz7dQ3RfNhHJCPoPnheVg1Wzkly2 "SHOW_LEGEND Sample, hide details with $details=None()")](https://www.plantuml.com/plantuml/uml/hLJVRzf847xdhvWugGeICUtbyd8IKYcuRI824P1h7ogXiRsOLTUxrkwQnZhrVxyPsn0IShgNlbZU7pFpVTzyin-SH-lBN7NUGcBqJbWFqiDFwRU0QIgzD1eL7UKvwXIKr0BGPcKkj8VBoIAQZbOtVqVhczbu-Z29Xa4u2CC0l87I2L0cGQMgpfdSm9iTMecn4clnA9rttU1bSD3h09n9dQWo5V0c4tvzYDcXAiLh8OFnd-knqHu9cGqBPd8cb1F7gRRU5-wlmS3Ypp0ZPcLCu2pHzSGY96w3Gg5c5IwTJvMCAUdbFMyzt4q7kp_2zrVXkrSBwLHkIBaB9JBwNud7Lhhl6bAnePiE_9Pqm5WeO05JGGcK0xDf3keu81YsWcuGO_A3ryc-JW3IDT5z28JCjXwSJ4KARek5g4_RZ3teZD8qKe8xiyBiaEo0EUZ3nOOMOwEC7Lv4q-WkcgtMd-Rq6S-dymMTnrbp6fnVNLrFHjSSKvSQHbnyoRMNlExs-iUiXwVGl-jJlBrNj3AbFvRBQ5K1jeenfOLGDHrqbKuOZwV8biDeiPX_FO1dS_xdmT9NIWmdwBOYdTBwX42T7zYlDKnoh3RFm3O8KqQ06IkFfJSvUbbx_4MVQUjuVbBfo68L2L5OKz2GIQAALjHHRGUFoJAMmUzXRBpVC-vrEilAUP6lFvfIfsYhRlAUZ7L3Ws2ryF0HzG-fiw07_z3y01oyqyrDB6aCiIZe_bszW55H4BfWVDw7RvZJf6fUtbkpevOxRgBCfUVcbx6ZxAtd3zNYfXfiIfqqEabVyTEHb8wK5TR1JYB7I0iD0D9g9nDHlnJ7y5ht4Jv944RtDmnEKMSuBwEwnHtsOMBeceNZaNZ2-p-u60eb3fh-k-7fVFKwl_RwHe--swPPktgBPQDh6ukvsEiCpMr6iVJ6icPacrQcX3OEK2ZGsBnc0nZpo1mqwWCc2RNJqv-tg1tMe6abV18Ig0wPwbd_delru8HZ1BNR-d2xdCy6NrQh--KJqyQ8FKwqdl5Kn-Q5v2TSzrcVZ4mceSVqHUOZdxCvlv25fz7dQ3RfNhHJCPoPnheVg1Wzkly2)

## SHOW_FLOATING_LEGEND(?alias, ?hideStereotype, ?details) and LEGEND()

`LAYOUT_WITH_LEGEND()` and SHOW_LEGEND(?hideStereotype)` adds the legend at the bottom right of the picture like below and additional whitespace is created.

```plantuml
@startuml Layout With Whitespace Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![Layout With Whitespace Sample - open link](https://www.plantuml.com/plantuml/svg/LP1FJuGm4CNl_HIL4vkunNydJwj0z82wWHYEfBGJ8IcbeLDrlxrJDzbTJftvpNlJbzbvb0k6oV1A7kQ0l1rnuEqm8dWd5V16Jiu0kngjCa437n2TVyooHVw8BzA6FdXOr6mHB0erJvapqiQDMu_QZ7sMFspt4Ns-LTdtdRYz5pV4kfmiShIm24TYnlQm-Dccyfednv8_9HjsKgKz3KuTVqweHL239L5py0XJgWWTIvwlh7fbBIwj9zoLlvW2JUWL_AmkBzMi1jFLCMDCewGndcY4HSmN0z0rpeo0NhCwXedV1ASb_cFMl7wqNLM-bEz5kc4xi9eEyWS= "Layout With Whitespace Sample")](https://www.plantuml.com/plantuml/uml/LP1FJuGm4CNl_HIL4vkunNydJwj0z82wWHYEfBGJ8IcbeLDrlxrJDzbTJftvpNlJbzbvb0k6oV1A7kQ0l1rnuEqm8dWd5V16Jiu0kngjCa437n2TVyooHVw8BzA6FdXOr6mHB0erJvapqiQDMu_QZ7sMFspt4Ns-LTdtdRYz5pV4kfmiShIm24TYnlQm-Dccyfednv8_9HjsKgKz3KuTVqweHL239L5py0XJgWWTIvwlh7fbBIwj9zoLlvW2JUWL_AmkBzMi1jFLCMDCewGndcY4HSmN0z0rpeo0NhCwXedV1ASb_cFMl7wqNLM-bEz5kc4xi9eEyWS=)

Therefore a floating legend can be added via SHOW_FLOATING_LEGEND(), positioned with Lay_Distance() and existing whitespace is reused like below.

- `SHOW_FLOATING_LEGEND(?alias, ?hideStereotype): shows the legend in the drawing area
- `LEGEND()`: is the default alias of the created floating legend and can be used in Lay_Distance() call

```plantuml
@startuml Compact Legend Layout Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![Compact Legend Layout Sample - open link](https://www.plantuml.com/plantuml/svg/RP5HJy8m58NV-okwnSGjaKtK9nCJa4qqcK26niUcT0MMb6xfRbN-lRSC1ajyMTllddFFxJfgW1kmEqMyKWjb2qct07Np6CU6_qIR4hPsPHjfHAL1QeX4jOjhnRNp31eeLBcA9m-3XKEVxrdyVHSDxwDRP6o25bvgQQBQ1H2oaAQfTC1lgDzkwTWFIISBLbZeJlJPnoD8iTKeMkuRaBj086gtTDAp5ZrhScdjC4j_8P1OmJMYPtLwgIQvL2ntCxff15UgGUfWukPp0-3lE3C4HP_bRXWNO-k2mm4JRssrW19ldANJT9O48V6C16iqzTUgub3g3LDo8tNX4m-_9prPliw_s4is7t-ypQRiw3ur2Kd6zomfyH6ra1q-n0ynbbnJxwgbz8dwRG3ZHd8VI_-sFif3hFTw7_cfzGWRuQF-0G== "Compact Legend Layout Sample")](https://www.plantuml.com/plantuml/uml/RP5HJy8m58NV-okwnSGjaKtK9nCJa4qqcK26niUcT0MMb6xfRbN-lRSC1ajyMTllddFFxJfgW1kmEqMyKWjb2qct07Np6CU6_qIR4hPsPHjfHAL1QeX4jOjhnRNp31eeLBcA9m-3XKEVxrdyVHSDxwDRP6o25bvgQQBQ1H2oaAQfTC1lgDzkwTWFIISBLbZeJlJPnoD8iTKeMkuRaBj086gtTDAp5ZrhScdjC4j_8P1OmJMYPtLwgIQvL2ntCxff15UgGUfWukPp0-3lE3C4HP_bRXWNO-k2mm4JRssrW19ldANJT9O48V6C16iqzTUgub3g3LDo8tNX4m-_9prPliw_s4is7t-ypQRiw3ur2Kd6zomfyH6ra1q-n0ynbbnJxwgbz8dwRG3ZHd8VI_-sFif3hFTw7_cfzGWRuQF-0G==)

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![LAYOUT_AS_SKETCH Sample - open link](https://www.plantuml.com/plantuml/svg/NL1FIyCm5B_dKppdOHrihLDFdbRBSE2cnNQAfvAsqGNI92IlbY5-Tr_OT68k3zxlxyl28tVOTmhMwUlZjgpIeYhkbsMsWe9tLWbs9dMZ-bR03j7wcoHnV8ZV9UxwklV2DKQZq1WtfakiuZfupJosIjP9TZtBmsgxMISVb_7yAhwWNPMHX4ijN6o9pDZ_v6Z2M2wSDphYRIVr54PfcDAZusZSQCAAlKVHLRUcrort-wYPJs5yA3oUm2S3UhynqI3gYbjBFY-YXjHQ9HkEqkWHhRBpAQH57ZyiIv8u0LGKDizPm5AbpE0XtEa13T2HbXEbwnLAoe9oa8Z20SfEAChorEths2x20qW-Hng1x4cedwjEjRQUb3HNPPaNn0gaN_HaSoUGQWmYZ3Tdkh-IXT1j-Crl "LAYOUT_AS_SKETCH Sample")](https://www.plantuml.com/plantuml/uml/NL1FIyCm5B_dKppdOHrihLDFdbRBSE2cnNQAfvAsqGNI92IlbY5-Tr_OT68k3zxlxyl28tVOTmhMwUlZjgpIeYhkbsMsWe9tLWbs9dMZ-bR03j7wcoHnV8ZV9UxwklV2DKQZq1WtfakiuZfupJosIjP9TZtBmsgxMISVb_7yAhwWNPMHX4ijN6o9pDZ_v6Z2M2wSDphYRIVr54PfcDAZusZSQCAAlKVHLRUcrort-wYPJs5yA3oUm2S3UhynqI3gYbjBFY-YXjHQ9HkEqkWHhRBpAQH57ZyiIv8u0LGKDizPm5AbpE0XtEa13T2HbXEbwnLAoe9oa8Z20SfEAChorEths2x20qW-Hng1x4cedwjEjRQUb3HNPPaNn0gaN_HaSoUGQWmYZ3Tdkh-IXT1j-Crl)

Additional styles and the footer text can be changed with SET_SKETCH_STYLE():

- `SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)`:
  Enables the modification of different sketch styles and footer.

The possible font name(s) depend on the output format (e.g. PNG uses fonts which are installed on the server and SVG fonts have to be installed on the client).
Additional is it possible to define comma separated fall back fonts (if the diagrams are exported as SVG. Atm
PNG does not support fallback fonts based on a PlantUML [bug](https://forum.plantuml.net/14842/specify-fall-back-fonts-is-not-working), but this could be fixed in one of the following versions)

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![LAYOUT_AS_SKETCH with custom style png Sample - open link](https://www.plantuml.com/plantuml/svg/VLFRQjj047ttLqpLG1IGxQJjKy4GLvW4chYcgoJaIQoaiRtrNiJkA8uf_VVEnjT2MxsiD7FEd3Cxe-j0qbDdTE-TihNk6eGbKHi-3uTUhWSBHSkkwWBwsbb2IuFQcM6hfOsSVg16gsgOV-hFOkZX_cxuyc5mzN5moR4oPufK5lsWZG8zCIbAyNLIvBUbA9xl9kbPjSYTTdwKQBLOKgKxJ38ucpDl5z-7rj9RPVVeHlgLnsQBTOJ-QPiU9MA5L2-FYG9VQPJa7YLX0tFdeL6Xxa9GpYONlTuvpAOtiEOk8Qh23stAsXXrTGafRLfLIwqt8AsZ9VejH0NW-sWk_j9Ep4-bmL5ohBDL4Ozx5IvOoNhrLYl0lO0RhgtgB7T6rI2aZS4CZf_ylfHwLJdf6n2JVMgA7MPGTpwe5tu9ZEppcDJyr7YKT1r1Sj1XE-pcFyx_vUZ4q9z-JkpitHpDnExlni_V7efoB7QQASTcw8EpgMoCiXaautYgG5wIyymHcq1eoY-kipphJLfVPN0kf6ardb_0pnxmSzYkT8rLATkMwpnX1UEsrTm-nGbpA7-VmLZC1jD9mHIFmFi9zuzvp8srTkktSVe0v81tkvKCCPqcnLfGy0No5W4fWvgr0dlxjNENqZR9TNQmsEntrFkkZhOU0ZFvl2sAcM1K11sonp8to1j1Qup7t3jpIhb6s_1Fz1i= "LAYOUT_AS_SKETCH with custom style png Sample")](https://www.plantuml.com/plantuml/uml/VLFRQjj047ttLqpLG1IGxQJjKy4GLvW4chYcgoJaIQoaiRtrNiJkA8uf_VVEnjT2MxsiD7FEd3Cxe-j0qbDdTE-TihNk6eGbKHi-3uTUhWSBHSkkwWBwsbb2IuFQcM6hfOsSVg16gsgOV-hFOkZX_cxuyc5mzN5moR4oPufK5lsWZG8zCIbAyNLIvBUbA9xl9kbPjSYTTdwKQBLOKgKxJ38ucpDl5z-7rj9RPVVeHlgLnsQBTOJ-QPiU9MA5L2-FYG9VQPJa7YLX0tFdeL6Xxa9GpYONlTuvpAOtiEOk8Qh23stAsXXrTGafRLfLIwqt8AsZ9VejH0NW-sWk_j9Ep4-bmL5ohBDL4Ozx5IvOoNhrLYl0lO0RhgtgB7T6rI2aZS4CZf_ylfHwLJdf6n2JVMgA7MPGTpwe5tu9ZEppcDJyr7YKT1r1Sj1XE-pcFyx_vUZ4q9z-JkpitHpDnExlni_V7efoB7QQASTcw8EpgMoCiXaautYgG5wIyymHcq1eoY-kipphJLfVPN0kf6ardb_0pnxmSzYkT8rLATkMwpnX1UEsrTm-nGbpA7-VmLZC1jD9mHIFmFi9zuzvp8srTkktSVe0v81tkvKCCPqcnLfGy0No5W4fWvgr0dlxjNENqZR9TNQmsEntrFkkZhOU0ZFvl2sAcM1K11sonp8to1j1Qup7t3jpIhb6s_1Fz1i=)

SVG with fallback fonts MS Gothic,Comic Sans MS,Comic Sans,Chalkboard SE,Comic Neue,cursive,sans-serif

[![LAYOUT_AS_SKETCH with custom style svg Sample - open link](https://www.plantuml.com/plantuml/svg/VLFRRjf047tdAwPkf1Z9GDBsgH9Ig8KIgK1HRHBboLhR0spPYxKx3a5L_xspuLfLhL_MdZbdpfcTyPqduQZLglDEcagrDSAQgF6V1mCdjlsLf7LRjXvTPGsXeNvbzQ1HmWHEprEjP3b8F_Nc8RIOJWOl7_gt7_it72jIfWXfqFMR8D39ndcHVHtdwKEHvS-JSNnLhbAhh1j6IgxMLAeMemIkbimxn8-XhN16cYEw5cxZiDvZBQ5xsgU7KRP1gjRdH8wlD8nIXuAmXgLrK4jVjTvBQw9kftCDyzazRBbB2AhmG-cYqbhUta1CkqPMGgaT26DfZMuFaHxuFkekS_zkA21cGkCmEbVQwsIFHnqkMOfgyrRDmpI3UwukgoIrMbQG2HE22Pm_-NqjrAQqmjMiUKpDiCK4gjPv-S8ldf4z7fHSNbeFahObY4uwRET_ll_bvyBEdsukp1ozdAs4tYUZvs-Bl1Xb1ysOOtDqtffOr5gQ1A9HEAKd9yYwO73d2NNnnRQ6PxsBgzi4hZEX6uNNNVZP0NvEsnLliIn4qt2T9onXr3IAcwSmOGwbxnCOPVF-R9mpnI7mViBqCGsvaL9s-pPEvu4iy6utWY6wLIHP2tA-FjuY8AbHiPPdRxyExcBQ9xdE0HQQ_OxgsDNPri8pay-7F9zdZ0gWK_PSvXvv7sYBuLWwgoyfTsXg_eb-0m== "LAYOUT_AS_SKETCH with custom style svg Sample")](https://www.plantuml.com/plantuml/uml/VLFRRjf047tdAwPkf1Z9GDBsgH9Ig8KIgK1HRHBboLhR0spPYxKx3a5L_xspuLfLhL_MdZbdpfcTyPqduQZLglDEcagrDSAQgF6V1mCdjlsLf7LRjXvTPGsXeNvbzQ1HmWHEprEjP3b8F_Nc8RIOJWOl7_gt7_it72jIfWXfqFMR8D39ndcHVHtdwKEHvS-JSNnLhbAhh1j6IgxMLAeMemIkbimxn8-XhN16cYEw5cxZiDvZBQ5xsgU7KRP1gjRdH8wlD8nIXuAmXgLrK4jVjTvBQw9kftCDyzazRBbB2AhmG-cYqbhUta1CkqPMGgaT26DfZMuFaHxuFkekS_zkA21cGkCmEbVQwsIFHnqkMOfgyrRDmpI3UwukgoIrMbQG2HE22Pm_-NqjrAQqmjMiUKpDiCK4gjPv-S8ldf4z7fHSNbeFahObY4uwRET_ll_bvyBEdsukp1ozdAs4tYUZvs-Bl1Xb1ysOOtDqtffOr5gQ1A9HEAKd9yYwO73d2NNnnRQ6PxsBgzi4hZEX6uNNNVZP0NvEsnLliIn4qt2T9onXr3IAcwSmOGwbxnCOPVF-R9mpnI7mViBqCGsvaL9s-pPEvu4iy6utWY6wLIHP2tA-FjuY8AbHiPPdRxyExcBQ9xdE0HQQ_OxgsDNPri8pay-7F9zdZ0gWK_PSvXvv7sYBuLWwgoyfTsXg_eb-0m==)

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![HIDE_STEREOTYPE Sample - open link](https://www.plantuml.com/plantuml/svg/JL3BJiCm4BpdAqmvD9NQX08dJWqbeaWKeYO5SOgSPA6M_9Az8QeG_yvQb1PVLjgPsPdnmYDts2iPdGdTohu3jaEq_YPD7H-I3u6xlkazkDPe18r9QrHg9TT1C_FOIT6ao-jP4LRRzMFwUPdChv8BsjLBad2XmIKs64IhXxkyBgjyapzNRqKUJwAe0EUDZdcdX9woKHQcyEWu6ZUQHENU8wZwrlIwusuVj_Cf6vTSMGdZ2VkA6BsZIpn0KtDhwSuhD2opLegMep1wHAlb-PHbPP4yvHL9733AoTOlou1bKfh1ir3JCpICEbfE5DLB5EJ5ga4WWcCe54ZoyfJj-v0knb-GxXne14ORa7-jJh6sdfGqLrLLbCGAf2DwEdCFI3462EFT6VLViW3TqMV-00== "HIDE_STEREOTYPE Sample")](https://www.plantuml.com/plantuml/uml/JL3BJiCm4BpdAqmvD9NQX08dJWqbeaWKeYO5SOgSPA6M_9Az8QeG_yvQb1PVLjgPsPdnmYDts2iPdGdTohu3jaEq_YPD7H-I3u6xlkazkDPe18r9QrHg9TT1C_FOIT6ao-jP4LRRzMFwUPdChv8BsjLBad2XmIKs64IhXxkyBgjyapzNRqKUJwAe0EUDZdcdX9woKHQcyEWu6ZUQHENU8wZwrlIwusuVj_Cf6vTSMGdZ2VkA6BsZIpn0KtDhwSuhD2opLegMep1wHAlb-PHbPP4yvHL9733AoTOlou1bKfh1ir3JCpICEbfE5DLB5EJ5ga4WWcCe54ZoyfJj-v0knb-GxXne14ORa7-jJh6sdfGqLrLLbCGAf2DwEdCFI3462EFT6VLViW3TqMV-00==)

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

[![Predefined sprites Sample - open link](https://www.plantuml.com/plantuml/svg/XOxD2i8m48JlVOhOau9Dj7hor9-hGa5wbhHPRI1DGxArh-zM50KFddOOPh-PBA3qEFQ6EGyAhjg2Oi5vZH3OMVREGBJGjZMZ0jOXkd0Gmik9tpHsOpC6yErW4IpoTkY5CzBEj2IWCheHvJwfPgi-7SKzvTiTtv1tAUb5KfNdZi9HL84FWrtEj7pDufekosDI4xNyBcFkcPy3BxNwHXHlHF4NaNuOAK4oi8e6FG0= "Predefined sprites Sample")](https://www.plantuml.com/plantuml/uml/XOxD2i8m48JlVOhOau9Dj7hor9-hGa5wbhHPRI1DGxArh-zM50KFddOOPh-PBA3qEFQ6EGyAhjg2Oi5vZH3OMVREGBJGjZMZ0jOXkd0Gmik9tpHsOpC6yErW4IpoTkY5CzBEj2IWCheHvJwfPgi-7SKzvTiTtv1tAUb5KfNdZi9HL84FWrtEj7pDufekosDI4xNyBcFkcPy3BxNwHXHlHF4NaNuOAK4oi8e6FG0=)

### Using HIDE_PERSON_SPRITE()

```plantuml
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![HIDE_PERSON_SPRITE Sample - open link](https://www.plantuml.com/plantuml/svg/PL3DJy8m5B_thwXuO2ImYNhon9oBa0WkREfnwROgJVgLzis56FztNmE2YRsyvFq-NnSUc8DUIRfSFUHraM_BvqrT5jjLbTEIAIivkH2wbNt7wGx0-hiaSMo8FmJi-gRttBL60zSGjqObLZ8Tt6OUEYcQ9BkT5M7ridvAFg_Z-KryXRiwGmaJchlO8fcG_zdHX922Eszqn3ebz9IEqZ251yV0kD64b7iFNDNtfjSTS_kedK_f-51vFA5VXE8x1KK3RsfcBVgyyOQcrahHCX16Zt2LNKvfMXRn9gzGuZZ5gdJzcWKibT8CdePBFGL3yKpBaA9w2GApQ3K80Eue2CKbPddizdri5y41H9yZ3K6ovVBtgdEj5uzAdCkgAafa1T89FTiySi0Q0m_ZtHdrLxBWkWl_-GC= "HIDE_PERSON_SPRITE Sample")](https://www.plantuml.com/plantuml/uml/PL3DJy8m5B_thwXuO2ImYNhon9oBa0WkREfnwROgJVgLzis56FztNmE2YRsyvFq-NnSUc8DUIRfSFUHraM_BvqrT5jjLbTEIAIivkH2wbNt7wGx0-hiaSMo8FmJi-gRttBL60zSGjqObLZ8Tt6OUEYcQ9BkT5M7ridvAFg_Z-KryXRiwGmaJchlO8fcG_zdHX922Eszqn3ebz9IEqZ251yV0kD64b7iFNDNtfjSTS_kedK_f-51vFA5VXE8x1KK3RsfcBVgyyOQcrahHCX16Zt2LNKvfMXRn9gzGuZZ5gdJzcWKibT8CdePBFGL3yKpBaA9w2GApQ3K80Eue2CKbPddizdri5y41H9yZ3K6ovVBtgdEj5uzAdCkgAafa1T89FTiySi0Q0m_ZtHdrLxBWkWl_-GC=)

### Using SHOW_PERSON_SPRITE()

```plantuml
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![SHOW_PERSON_SPRITE Sample - open link](https://www.plantuml.com/plantuml/svg/PL7BJiCm4BpxAvPoI2gr2QyJfvQg0YGeKHFW63d9bbXoRClU4274lxEXvI5XMLffPtPsnbu4afxwJaD-y_1SPkjj_h0fysnxMwmXbvtJA8wKgNNV8BH4BbocgPT3ygAexQi-eA-j8JIKrBPBdPPcL9i7QhIgqjN5F1jRZ_TtwUjPSdgUd72lNF68L0PzufWiH1h1nX8On0ORgB2MB0pKgW1ygKLeS2TxJJ3mMWZEAqAOEFJ1cWb4gVZlFfuAaNqHOjbqoinWiXoh2kGbMJ-PYlmj47RbbUrD8_rRN9_E8Dg7ZgRmBe3FZzLumAgKph7ECrQmT4whMf9Y0znQ7SzWcMV9PbtmY4VWi73_j1gnfTPs232-5OUnm0_b95Cw3gHu5nISYj03gGurxmhixUFWBgOzo3e76eDYY_exrQ-jny2JN6-A8ikPDP9-q5-PQoIsCU1OTjvsVqSMQ9hnHpu1 "SHOW_PERSON_SPRITE Sample")](https://www.plantuml.com/plantuml/uml/PL7BJiCm4BpxAvPoI2gr2QyJfvQg0YGeKHFW63d9bbXoRClU4274lxEXvI5XMLffPtPsnbu4afxwJaD-y_1SPkjj_h0fysnxMwmXbvtJA8wKgNNV8BH4BbocgPT3ygAexQi-eA-j8JIKrBPBdPPcL9i7QhIgqjN5F1jRZ_TtwUjPSdgUd72lNF68L0PzufWiH1h1nX8On0ORgB2MB0pKgW1ygKLeS2TxJJ3mMWZEAqAOEFJ1cWb4gVZlFfuAaNqHOjbqoinWiXoh2kGbMJ-PYlmj47RbbUrD8_rRN9_E8Dg7ZgRmBe3FZzLumAgKph7ECrQmT4whMf9Y0znQ7SzWcMV9PbtmY4VWi73_j1gnfTPs232-5OUnm0_b95Cw3gHu5nISYj03gGurxmhixUFWBgOzo3e76eDYY_exrQ-jny2JN6-A8ikPDP9-q5-PQoIsCU1OTjvsVqSMQ9hnHpu1)

### Using SHOW_PERSON_SPRITE(sprite)

```plantuml
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml
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

[![SHOW_PERSON_SPRITE(sprite) Sample - open link](https://www.plantuml.com/plantuml/svg/ZL3BJiCm4BpdAqmvD4XjJ84JfvQe0YGAKPF2CNAJBRNab-mDKONuTzPGMiG9NrRUcTsPdMb0uR7JAZcHfb5T2soBwC8rvrxqsQl4RRVk0lZ66WI3MMCrTqgOE3CEs2gvvldLk8YjrUA1lrraaylid7frJYD26l2P-n9eOKC_PeCewFyFdToBi8LMIzFo7u6nTM02D9sNk1E-sKg41ZiF5sD9iu5h4H3yyPoz7C-jrjRihVm5LwJCXLBVS5BUFRtKnNnPFZtMPR6yh-RfWAXrD5Y_UW1J7wG7PqbIW0_Mf29Q7R71B5OPq0kqdl1oHvPqVMCxqmg_Ivl9Y0rBePs2uHbxJnYzGrXf3-jQE4TxNc3DPiufsGYKrWoebP-EsAmiiiTvHICU6CND5izvn6PAsJwmQ38mj8mYT88ekbCeIOjLlKJAXg7Ke4WhaBUFlRiKlq7QiwV5mvQWVguwsgAmGjIxgwgY95Oa7T3Zcbj0ij53B1jlzU-HAPYMalu4 "SHOW_PERSON_SPRITE(sprite) Sample")](https://www.plantuml.com/plantuml/uml/ZL3BJiCm4BpdAqmvD4XjJ84JfvQe0YGAKPF2CNAJBRNab-mDKONuTzPGMiG9NrRUcTsPdMb0uR7JAZcHfb5T2soBwC8rvrxqsQl4RRVk0lZ66WI3MMCrTqgOE3CEs2gvvldLk8YjrUA1lrraaylid7frJYD26l2P-n9eOKC_PeCewFyFdToBi8LMIzFo7u6nTM02D9sNk1E-sKg41ZiF5sD9iu5h4H3yyPoz7C-jrjRihVm5LwJCXLBVS5BUFRtKnNnPFZtMPR6yh-RfWAXrD5Y_UW1J7wG7PqbIW0_Mf29Q7R71B5OPq0kqdl1oHvPqVMCxqmg_Ivl9Y0rBePs2uHbxJnYzGrXf3-jQE4TxNc3DPiufsGYKrWoebP-EsAmiiiTvHICU6CND5izvn6PAsJwmQ38mj8mYT88ekbCeIOjLlKJAXg7Ke4WhaBUFlRiKlq7QiwV5mvQWVguwsgAmGjIxgwgY95Oa7T3Zcbj0ij53B1jlzU-HAPYMalu4)

### Using SHOW_PERSON_PORTRAIT()

```plantuml
@startuml SHOW_PERSON_PORTRAIT() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![SHOW_PERSON_PORTRAIT() Sample - open link](https://www.plantuml.com/plantuml/svg/RL5BJuGm4BxpAyRLPDba1LqzcPY86wCcwf85zKWAZBjDIjkqWsHZ_EzEnTT13hJCVFCzXWjFmb7VAIXkLizLVhKkLWzLlbgNw-osZ6TGYCugZFQaRbJV8co9h3zBKoU6P2DfszUzHzSOJQWfQKoNMYLqO3pqr2fPfylJmpoK7k_lqjT5SdoI776jMlA8a1fTOXaSHV_hHr6EpXiTYxQJUWwJB9pIanDat6GM5JjFs5MNfjUjSBkuEPx3T3GzdS5R1FpyICK3rfMmbdcUiORCMYKRGTBe2PUM-tF8YZnvk2fvn26mMRX_MePUffGPF8Ii7iW01xM28LslIB8Mb8CaGWSaErIivTdR-vUxcCOcytp1k1bDGRw00FkP3wGFd3LFji2OBNUyTP8GQ8iwlC1XGq9lM4o9dUafpB2X5iI6qtqlQkHZgV5x91kfECZ1U3kVZB15CB96zRtUt_qyUex0vqrPvWMZ0kYd-vld6edtCM0uNfpf_evSe6xvrtu0 "SHOW_PERSON_PORTRAIT() Sample")](https://www.plantuml.com/plantuml/uml/RL5BJuGm4BxpAyRLPDba1LqzcPY86wCcwf85zKWAZBjDIjkqWsHZ_EzEnTT13hJCVFCzXWjFmb7VAIXkLizLVhKkLWzLlbgNw-osZ6TGYCugZFQaRbJV8co9h3zBKoU6P2DfszUzHzSOJQWfQKoNMYLqO3pqr2fPfylJmpoK7k_lqjT5SdoI776jMlA8a1fTOXaSHV_hHr6EpXiTYxQJUWwJB9pIanDat6GM5JjFs5MNfjUjSBkuEPx3T3GzdS5R1FpyICK3rfMmbdcUiORCMYKRGTBe2PUM-tF8YZnvk2fvn26mMRX_MePUffGPF8Ii7iW01xM28LslIB8Mb8CaGWSaErIivTdR-vUxcCOcytp1k1bDGRw00FkP3wGFd3LFji2OBNUyTP8GQ8iwlC1XGq9lM4o9dUafpB2X5iI6qtqlQkHZgV5x91kfECZ1U3kVZB15CB96zRtUt_qyUex0vqrPvWMZ0kYd-vld6edtCM0uNfpf_evSe6xvrtu0)

### Using SHOW_PERSON_OUTLINE()

> This call requires PlantUML version >= v1.2021.4!

```plantuml
@startuml SHOW_PERSON_OUTLINE() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Container.puml

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

[![SHOW_PERSON_OUTLINE() Sample - open link](https://www.plantuml.com/plantuml/svg/RL5BIyD04BxdLunLQ0erqUf94AobgA1jCAaUmoOPsuNDxh8xCHJnlpjhV1tC8RkP-UPxJAuy2KTTgo2_NJ-NsV8nNw_AzQQulrijumdaehKAemEfQzKr23iYwo_Ir8a-sKhQTLNdqTL64sfAQjEcLWaT28yzDKfMwUByE0kbpSDz-ZfBJi-I4wwL2nuHKgDBB8EZw5_vAChGUQDZqRHIJs4q3wVqv0GPDvf4-TuJjkMrwNGZt3wkJwSm7ZoF9_0M0Jy_Id6FLIciPPvdh61khPAr86dqY4kBmodCyonPBGiUSGZi5HwU5g4tLyhq7a9K3sI0Srh1aBPJ95aBYbuIeGEIBIhMykpj_SjTJ4EJURvWt8p685z0WFtC1z87peed6s3CZZlUEaa8j4CTNk2m9g6tBAR4tdGKPjXG0sBBwRuNDV2nrF0za0rK7EHek5sE1jWi67b4zRtUt_riF4VWyxOeifnH0VJJ_SrpWyJxw34SBywqVqUkK3VXptu0 "SHOW_PERSON_OUTLINE() Sample")](https://www.plantuml.com/plantuml/uml/RL5BIyD04BxdLunLQ0erqUf94AobgA1jCAaUmoOPsuNDxh8xCHJnlpjhV1tC8RkP-UPxJAuy2KTTgo2_NJ-NsV8nNw_AzQQulrijumdaehKAemEfQzKr23iYwo_Ir8a-sKhQTLNdqTL64sfAQjEcLWaT28yzDKfMwUByE0kbpSDz-ZfBJi-I4wwL2nuHKgDBB8EZw5_vAChGUQDZqRHIJs4q3wVqv0GPDvf4-TuJjkMrwNGZt3wkJwSm7ZoF9_0M0Jy_Id6FLIciPPvdh61khPAr86dqY4kBmodCyonPBGiUSGZi5HwU5g4tLyhq7a9K3sI0Srh1aBPJ95aBYbuIeGEIBIhMykpj_SjTJ4EJURvWt8p685z0WFtC1z87peed6s3CZZlUEaa8j4CTNk2m9g6tBAR4tdGKPjXG0sBBwRuNDV2nrF0za0rK7EHek5sE1jWi67b4zRtUt_riF4VWyxOeifnH0VJJ_SrpWyJxw34SBywqVqUkK3VXptu0)

## (C4 styled) Sequence diagram specific layout options

- **SHOW_ELEMENT_DESCRIPTIONS(?show)**: show or hide (hidden is default) all element/participant related descriptions
- **SHOW_FOOT_BOXES(?show)**: show or hide (hidden is default) all element/participant related foot boxes
- **SHOW_INDEX(?show)**: show or hide (hidden is default) the relationship (call) related index (sequence number)

show is defined with `$show=true` and hide is defined with `$show=false`

### SHOW_ELEMENT_DESCRIPTIONS(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Sequence.puml

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

[![SHOW_ELEMENT_DESCRIPTIONS() Sample - open link](https://www.plantuml.com/plantuml/svg/LL5BJzj04BxxLqpJGnmfsALmwedKjG2910kRShJMte6ij2zsnxLGrV_EB0qDtSj8C_EzPYyYYK2JqTadPKSzIOGzaO_VoZA8kNXIj9-6AM8OdIMqL8pEb5uBcp0daQHMGrcTdpIfTR-zANzzBKxFYY_Swrjydj2EMFZ4dxLNjmzzVLDlwrtN_wZRwkwwwQvlTss-oh86GtGs5z8ekuR59bKLAGXoOS6D1ftN2BGN1E8unCWj11-Sd4QAYrNMlaH2qtztavKYlEJZwHgMhJ2CNguou5Tn4g4iXdp6eHVUC_q33h3nNgjHa78sALQVrx1fcs9NTmm921mCjZ-hDDjexUO8wIvim04VnGjUCPCcbNnsioB20AGCQjPApfQWB0Y8Xwk0LE8f20FlLllQodm5U_56EM2YbupXF4A2UmJu3N-o_xSFSNFwgyVM3igibzsXVZ_eCUbzP3DShxgkQNahBVsR7cakaTZ6ZAay1cS-GYxGIlxHLm== "SHOW_ELEMENT_DESCRIPTIONS() Sample")](https://www.plantuml.com/plantuml/uml/LL5BJzj04BxxLqpJGnmfsALmwedKjG2910kRShJMte6ij2zsnxLGrV_EB0qDtSj8C_EzPYyYYK2JqTadPKSzIOGzaO_VoZA8kNXIj9-6AM8OdIMqL8pEb5uBcp0daQHMGrcTdpIfTR-zANzzBKxFYY_Swrjydj2EMFZ4dxLNjmzzVLDlwrtN_wZRwkwwwQvlTss-oh86GtGs5z8ekuR59bKLAGXoOS6D1ftN2BGN1E8unCWj11-Sd4QAYrNMlaH2qtztavKYlEJZwHgMhJ2CNguou5Tn4g4iXdp6eHVUC_q33h3nNgjHa78sALQVrx1fcs9NTmm921mCjZ-hDDjexUO8wIvim04VnGjUCPCcbNnsioB20AGCQjPApfQWB0Y8Xwk0LE8f20FlLllQodm5U_56EM2YbupXF4A2UmJu3N-o_xSFSNFwgyVM3igibzsXVZ_eCUbzP3DShxgkQNahBVsR7cakaTZ6ZAay1cS-GYxGIlxHLm==)

### SHOW_FOOT_BOXES(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Sequence.puml

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

[![SHOW_FOOT_BOXES() Sample - open link](https://www.plantuml.com/plantuml/svg/LL79JiCm4BtdAuPoQ2gLXEt4YL8LE02jI0hS8YSUg2Lls1CYXFXtnb0sNqOQlzK-ZIG2zKPdEyfskfS86o8VJyeoYA5uKhJfspvYw9mbj5HqpfHU2viuUv6aLcqvFzvRfTNw-gfyEImEZefztZKLFlTeEonyqi-go-LzSxvSritPyc5HvPCiMs68pkP26cMdC9gbgI85GIwC9bdr6WbDS-PwAqLupRk3AOmhORp6yIG3FdDE9PJ5a0_ODi9xLhd75cRUQzK9KiwEU3NVdSAiMXKtYvef0O53mlNTFDtDj7P3XDGn0ZdWWbumnFIQ53j1FIWY343Ae6QloCd6e2m8YDk689Lu2iB0TzHcOMK-WOtub6mnoKlcS1yXmJq2lC5xzX-zhPlJbnz7spgpNtQB-lkPVfkk8uVXULdNgufH2VHp-ojpWSGn1apZCJZpbtAALlBlV00= "SHOW_FOOT_BOXES() Sample")](https://www.plantuml.com/plantuml/uml/LL79JiCm4BtdAuPoQ2gLXEt4YL8LE02jI0hS8YSUg2Lls1CYXFXtnb0sNqOQlzK-ZIG2zKPdEyfskfS86o8VJyeoYA5uKhJfspvYw9mbj5HqpfHU2viuUv6aLcqvFzvRfTNw-gfyEImEZefztZKLFlTeEonyqi-go-LzSxvSritPyc5HvPCiMs68pkP26cMdC9gbgI85GIwC9bdr6WbDS-PwAqLupRk3AOmhORp6yIG3FdDE9PJ5a0_ODi9xLhd75cRUQzK9KiwEU3NVdSAiMXKtYvef0O53mlNTFDtDj7P3XDGn0ZdWWbumnFIQ53j1FIWY343Ae6QloCd6e2m8YDk689Lu2iB0TzHcOMK-WOtub6mnoKlcS1yXmJq2lC5xzX-zhPlJbnz7spgpNtQB-lkPVfkk8uVXULdNgufH2VHp-ojpWSGn1apZCJZpbtAALlBlV00=)

### SHOW_INDEX(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Sequence.puml

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

[![SHOW_INDEX() Sample - open link](https://www.plantuml.com/plantuml/svg/LL79JiCm4BtdAuPoQ2gr2Tk94wLKWCHIaRBS8YUUKalUi2T42F7lZA5byMMayLljaqWYK6TqjgDigpk9i2RoyRWiW-YBPqNhhkaYXjPPGaj5wqpfjR29CuaajMhAsT5aaLRtrrVbwq6nVrZiyQwkyAL3ssBXatvMNTm-rfStP_EdV9Hb2mpHsLn8e-mO1jCqLQGWo8N1AAlU8g6fJrrdfGXlURi_Xc4bZDSu76N0PyQ1XB8OyXwRMdZFAe_OmDHxhLf1oja1hsQxOvXMY-9clcHAGE1ySFqmItTJhLqV8TMBG0wucnSCCPqcnKwmx1KH1Y1bKBDNv6H3K1O4n4qva4ey1s5W6xMUMvcFO2s-91jCyf8vt4T8S2k0T_Z8_gCtTNFwzkDe6sVso-vGRv_fj-bzv30yBvRBHSMe1Fgv_PKvH-8OFQQn2ixyfPoWbVmndm== "SHOW_INDEX() Sample")](https://www.plantuml.com/plantuml/uml/LL79JiCm4BtdAuPoQ2gr2Tk94wLKWCHIaRBS8YUUKalUi2T42F7lZA5byMMayLljaqWYK6TqjgDigpk9i2RoyRWiW-YBPqNhhkaYXjPPGaj5wqpfjR29CuaajMhAsT5aaLRtrrVbwq6nVrZiyQwkyAL3ssBXatvMNTm-rfStP_EdV9Hb2mpHsLn8e-mO1jCqLQGWo8N1AAlU8g6fJrrdfGXlURi_Xc4bZDSu76N0PyQ1XB8OyXwRMdZFAe_OmDHxhLf1oja1hsQxOvXMY-9clcHAGE1ySFqmItTJhLqV8TMBG0wucnSCCPqcnKwmx1KH1Y1bKBDNv6H3K1O4n4qva4ey1s5W6xMUMvcFO2s-91jCyf8vt4T8S2k0T_Z8_gCtTNFwzkDe6sVso-vGRv_fj-bzv30yBvRBHSMe1Fgv_PKvH-8OFQQn2ixyfPoWbVmndm==)

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Component.puml
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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.13.0/C4_Component.puml

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

[![Sample with PlantUML elements - open link](https://www.plantuml.com/plantuml/svg/NP3DRi8m48JlUOebgbIG82bjJvMGI21g3oP5_8XZPCS6eYQsPM-Wl7tjGX7qvjtzPdRMOulKODlKGIVBavHaHK98CIT9lYeoaisoVBM44Go3JYNBkkK2zeZQliMneSTeL-6-PQqLfbGIXSIeL4siQogzvS0YhoiMJru7SzzQpqXyU8w6Bz6JwnKJrMWblKZx_S6rxZeJtOTmelG9ohzksBj7vBRQ_KB-SOFruO5HAvPxgiKerBJyeZjn9vwoBcU9qqvJIDpa4MYDmaYArK60FKcatx1L1cuLFJYwO--yEKNgo_0c5sVfsJZz5-GAkoGBKHVhovN_3ccDuC1EZl8GkK3dk0j1kOMjKSrblBYE_TADgL1OGELNB3y-DmN9thDyskq5Oo6v--CV "Sample with PlantUML elements")](https://www.plantuml.com/plantuml/uml/NP3DRi8m48JlUOebgbIG82bjJvMGI21g3oP5_8XZPCS6eYQsPM-Wl7tjGX7qvjtzPdRMOulKODlKGIVBavHaHK98CIT9lYeoaisoVBM44Go3JYNBkkK2zeZQliMneSTeL-6-PQqLfbGIXSIeL4siQogzvS0YhoiMJru7SzzQpqXyU8w6Bz6JwnKJrMWblKZx_S6rxZeJtOTmelG9ohzksBj7vBRQ_KB-SOFruO5HAvPxgiKerBJyeZjn9vwoBcU9qqvJIDpa4MYDmaYArK60FKcatx1L1cuLFJYwO--yEKNgo_0c5sVfsJZz5-GAkoGBKHVhovN_3ccDuC1EZl8GkK3dk0j1kOMjKSrblBYE_TADgL1OGELNB3y-DmN9thDyskq5Oo6v--CV)

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
