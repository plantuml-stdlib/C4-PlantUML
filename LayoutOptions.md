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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![LAYOUT_TOP_DOWN Sample](https://www.plantuml.com/plantuml/png/JL1BIyD04BxdLuprq1JQn1P1yDGOHGzz19jQF8LDChKBczrbTs8eudztWhLrMHYOxp7VpDoJSDGsAhYIkb9jZN0Wilu-ZfteeWz9XxPiFRhAQ49DKMMQs2gXUyt4Kwra6QUtawnlRPUB-7CMtKKtt2fILWYfqKMszm_Y8QmCWKQiiOOIAy6-G0VfWJyT46hSYrOH3EDWaRoljtcHhxFYSRrRXQCWoD1veqDHDrAFOP3qLNfoWemRZ8BDqHCsnODfTItSCQocOnXkH6CL3aVm5G2_SwImmx8GrhBF3aj8h5Mo4YID7d0hlHv3iicYrLFE4eSmYwQmV4jxB57AT1xwat1e0tmFAvZIS739io3l914w8DcWubcUitsVqeNq2xBFYSPWy8hgRwjBhArd9TUNFCyspEf9P_HYyup4CJhiozwPvhzaZhhco_y0 "LAYOUT_TOP_DOWN Sample")

`LAYOUT_LEFT_RIGHT()` rotates the flow visualization to *from Left to Right* and directed relations like `Rel_Left()`, `Rel_Right()`, `Rel_Up()` and `Rel_Down()` are rotated too.

```plantuml
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![LAYOUT_LEFT_RIGHT Sample](https://www.plantuml.com/plantuml/png/JL1BIyD04BxdLwprq1JQn8eWU6eCjHLQ3MsgU0gRPBGB-s9tOYZYVtSMQ-jU1kPxpiuySeUTaj65q8tiMc1xHEllqjJnFlaGkE_gpeDhZ4RGc3H6fLPo7JGJZwqKTPhVJ8gmsgrNwUTrSfjSqQhAIS651fVOu1-jihVdNLcjvWzbjNbSBCju54K5E6zqp5ibz9WDiZ25HyVHkC4esXuyWghkJQTRxWvnCnspuPOhAs4uObyHetVAYNkeAsuj-Rn2pJ9hfMWu2gC7jCelnopR5idJl2I90tQTJDdw9GzO9gNfFGjtUeQ6qP6M4qLr4WLbiR8NYE0O2WMIiZnr-pwsY_4N99yZZS1e0_BlgdEjdISbpMLP5bjY1T89FTii0Ab63s6yEwF-IsQWM_hE7m== "LAYOUT_LEFT_RIGHT Sample")

`LAYOUT_LANDSCAPE()` rotates the default flow visualization to *from Left to Right* like `LAYOUT_LEFT_RIGHT()` additional **directed relations** like Rel_Left(), Rel_Right(), Rel_Up() and Rel_Down() **are not rotated** anymore.

```plantuml
@startuml LAYOUT_LANDSCAPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![LAYOUT_LANDSCAPE Sample](https://www.plantuml.com/plantuml/png/NP91RwCm48Nl_8hPxA54Ig6jLbffJsKXQWyqHJ6qsXDom6qi6TkoXw9gjVzznmbDetAn-DxCcpU6Mu_SuJWeABC_ZqtTbjccO7bMhO7nmIeHVPEwKsClO8ze_QyqTNnANYNknzteXUkCHg4nwSoGMiLryBhqs2kvI_CVbrL0pKEPljqaFvChGcrE7LnguH9BjL7qTN2yZA9AE6zqpFj1wXKiid1AZuwZSOjbnDuzYg7zRKRTS_SUTzShk3ZclLZ2tmZeEOs99x5hkRNayonsa5chPCTH6hqWb7zVGSQgPBEkgSK9k4ckuU4f3rgcb9ayX3Kze07QqN8g6KQ5acP1FKb4uG3b81JDyfJjtvmkngD8FdCPYT5Mg8-jFcCrdZhflA_hYb5LA3gfdpPt0Yd69CBnuinmtl8nbAqMx7H1CMle5HfxHef02ZFfCrO6LeeNF6FRmBRoTOzpxBQnv0vaIO7jCMKRZ0wq83gx1XxC3hmaFZi7VZ0y25iIJlRi_l6vBTTtwqqHllwjq3tz6ly1 "LAYOUT_LANDSCAPE Sample")

## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype, ?details)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```plantuml
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![LAYOUT_WITH_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL1VIyCm47_lfuZpOHrihHk2uDDg7PkmpM8xXqybRKyNI9EGN2r3_EvUS6xcvU1-VozpXznYryhWIgXQTWsm0w9nzt5iUHzz23nqLUV0rbeXA8ngtSP6SkKr4uUD55MStauolzfjrl7dBBgBRcXLfgJWGe6DZFSFridRywuezq_5gbmlbeljOpWAWWoiqohaJIlKc0qIFuL3or7RmIZ8ZmwXBHzqfnfkZs4z7RDXpbiZOJXYNm6ZTmuAUwXARWpvxA5YYJ5Ir1o5LWDQfTTZbkHPj5qK9B70Pj6KRLvJZoLIwjunVwXZg1bTQJXHsawYe2nMz08HB4FHWgGiHzs-J-r2_0N9vqGZC7W1-NVLfTREaPBcgYYod5YUT4OlDaj0gj637-zMj_ybSr0D_USF "LAYOUT_WITH_LEGEND Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![SHOW_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL5DQy904BtlhvZQWn4qgQLGwAbfAdfG6ngjnx19jdLXlzYTD4ZfV-y4hRgN1_C-vWtx791xRBM2Ol6sAvUp-Mpz2WNNJWbs8qsjsaR07j65foJnl8k_9ExRgWt2rzQWC1ZNLYTESTF7J08sIbP9zZ39-z5sjKo-x-F7-8v6PKOEBetmiICjOxdmmPg8DrgQCGpI7cL0pz7wmOWLXu12bo-sDGttXwYUZc5ux3OSmGy3UkV8g1DLoPsZd9se87LEoPgZj6P0e-ns36cHn-lPXYnUm7qyXTL7rdEfKhOBq9yK02tGFOwJHBSA9Us2JISHXGUKMYZQ5QZRxwbTX4UISauo8jcxKFzNNMfj0pa95vjDNf2g5vtPIynS8DNeH0-Vtkfh2xlwfMZ4_W0= "SHOW_LEGEND Sample")

Legend labels and details can be defined via `\n` in `$legendTest` arguments too.

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml
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

![SHOW_LEGEND Sample, $legendText defines legend details](https://www.plantuml.com/plantuml/png/hLHDRzj64BtpLumP1nK1cMgR1WKA28WYiOq3MJ8akUqXW30aLzGYorrYTwcOAFhVEqDIicovwAKNWlinC--zURCVd4Vhwr85tq5cz45O3zB3D-dtW7aklJGQ5HsL9UeSbDG2q1PrARI7czagcKysjxydszl5TFumIyPXF8hZ4Bo1sWbG9aEbck1Axk3j0Qt4L8cjU9JEkq7uCZYC0e0hgJDLvmBU5i9lJp47LBLuBMGq_MaxDTeZ8RDnnKokX7BYFDNU-yhzCXfP_1ONnAnE2PmbkfvOnCHjL2dKhCADyxcIAIMzkUUjXxlvwF1Z_7Fy_QjrT2vt9Dor4WNzRyHZhzmN3RdOqKq7VayoO2eKi7wve0JAWTbr1sqS40hRm21CCVlAw-nO9mJfkkWXX48MUmzEvY87jyTAjATznWY2IPudId1ZDbYSafqmXqEutj5YQfInu-jadjmbYytsroLzfilvSaNdQT6TXc_UlNi_cxpdcBRKEE7YQwwzvlKW6fwp7bz2_w8lyKQlQ6LgVowNqQe1x1LZIYkXMZhe6fqn7a-HFOV9QhNyumIUlVcl1slVA36UeTkBV4xh2m9jVc2xjZ39iDey0ziXp1a15gmyrjwKw6LhyHTzfgtpyScb8uSr94HbJKKp9eagMj56zHqy9yjOHlyFO-FzaN4K1El6UL5kFvfQvsYRGVO36UkMvi1guU4ZwgzI5s44Vz7u09oyCoXDAcaAiQhe_bsxW4bL4Rfm-cO8Vs99WwfvUM_DWLhkk8cob9wRNwUEilUUFrLBksgmgtNMwIHzmoz7LZjILbW71uaS8orq04YhWyn4-r2Sm-lTH_WaGPZStp8uHPtXl8pgCnvm23D3rooSZyGJtl_0nL0eSTZrtuqlvoiA_ZxgcppwGPzcwzejbeskxIoMugWpTBSPnTeRovgHRNgPCjeuGQ50OykM3M3A8tFIQ0YOPTHEJt_UedROWgQLy5bCe08orRF-FHVhmGd725gt3U7pUhaOVTfixjTFJ3iZHfnek-2fJiqBoI-u7hC-6PbCGc_fYyndFcTpVY8BpvFVaiLi40KVA3kzily0 "SHOW_LEGEND Sample, $legendText defines legend details")

Legend details can be deactivated via `SHOW_LEGEND($details=None())`

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml
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

![SHOW_LEGEND Sample, hide details with $details=None()](https://www.plantuml.com/plantuml/png/hLJVRzf847xdhvYuYGeICNVNLfLEGYe5zvg8G0JaUW-LqDXUp2hhNMjtJM9Lzx_VZ6q82JdrfI-MzyVCVDytt-mdvz7wCbUTjv0OlHFMW_Jm8FqMC4sbbqQZegCyHvs2abe0sgpCXVPmELb4qz7gwkzeVJKRJ-ycqJ081s4OW3TGEW7A9AXKrJcJ6xZOePKOAx4MZz9vrmrU1WUz3i2Pr8agKm4NcV3hGymELIbU2ncCtw_7HdiaP3OicCcPK4uSfzfwNxW_1mEB3s56pCgOm5cYwub5IDm6XKBDAbmwdoePKzBBMzwwkvaETd-47yFVNgsZKxaXuSwLoEX_9HvRvRvhICM6RZhmMv81Ow60zKi59L0EpAOvgEE0KDWAka6CoJslatsT0AHheliG29bjFJYPYXJS5WjHdxOPUz0PfMca13TcXTaXsG5pq8Vp3It6HXaxF8-cqKqqMws_pEapda_d2pgFi-OqUFFktOV9w0F7rAM64HTVSkqbhxkz_Z7huIdqx_eKR-yLhKpfZ-KoMbM0hM9CQI5KJGTTfHF6uocovJ1QBERV3k3Pc_zxiFIL4iC9kgr8fxG-8L3d1xPh3PCCgyqpi0t2b15WnifZwKsENjOMVz5dsZeUdrGwSbX5GXJM53HZagYY5NLKsy5Zienby6iO6-_tZ7kTph9oNkJhpwRKATggc_nEnhgYER1QUFYC-bxgBEZ13neVW8Dtkhc99KqX5WNTlwaNC2eAGXUCt_JX7ynfK3KlRwtPKSiTDr7cqdFpozXHzjRpXsfnKmqsfKuQdQIl-EL8IaVA2kjW9v5Zf8K606crauce7ufZUAtx29ya2AFRAmQdg3ESbr5TumxxC35qpSBnI3pX_GakXaA9WwR_RdWwNxtEltjzeqVVRTEiNRt5ij6rZSLSx7M6vZQZM7fZMJEoJIjJGXi7A1HeR5wp0OnvP0uQzG6JXDhfwSzRr0vhqBGIFWa9L8TCzQn_pyMwSy8nWjfjVRXUpcU3hwlLxVA9QMF47YTQptYgO_D2yXEk-wnFHYQJq5lw8lEHpzcSNyd2q-YlQ3RfdhTJCPoPnhgVg1Wzkly1 "SHOW_LEGEND Sample, hide details with $details=None()")

## SHOW_FLOATING_LEGEND(?alias, ?hideStereotype, ?details) and LEGEND()

`LAYOUT_WITH_LEGEND()` and SHOW_LEGEND(?hideStereotype)` adds the legend at the bottom right of the picture like below and additional whitespace is created.

```plantuml
@startuml Layout With Whitespace Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![Layout With Whitespace Sample](https://www.plantuml.com/plantuml/png/LP11IyGm48Nl-HMnfowugOWWUDgrBNgekhH8ZoLD1bj8qz1CrFttJbpexfuoyyrxayViFCe5msHu9OzpGDwEEF1s616yamfu8oTdWDsCLfcWWG-8pZzbsI9_n1TfGnyyB6gs21Q5cgVC6MdZngr7RSO-on-sXuW-twhi-ruyYZj2NKuEELfOX2CjOmTO_6nJUSkJKydtoOQjghIdmThnvuHQ13LO4ZL7Zp2bYj2fvFcLLLzPYqlhYhlo5rEW2Rs2dzNbfPhLOBewPenfb3J64usmYFbY03h6cH7GrwoEOU8tmMc9_vWrhnzjLvKlvNkHRjWEhAQ3_04= "Layout With Whitespace Sample")

Therefore a floating legend can be added via SHOW_FLOATING_LEGEND(), positioned with Lay_Distance() and existing whitespace is reused like below.

- `SHOW_FLOATING_LEGEND(?alias, ?hideStereotype): shows the legend in the drawing area
- `LEGEND()`: is the default alias of the created floating legend and can be used in Lay_Distance() call

```plantuml
@startuml Compact Legend Layout Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![Compact Legend Layout Sample](https://www.plantuml.com/plantuml/png/RP5VIyCm5CNVyodI8jY2QrK4GH0srpg5kerDyJ5aQRO5ihGaj_xvzjwiMxU2Bqtok-USUzCC7N0BpKwJG1cXcrBIBK3j7jBKykzaes3Rh1edhQWCI0E9g7PfhRdnde63KgjLEhuRp3twU2lIhzlaFhb6nCReuCf8czG-dv2vjAuo4R-YORkbep0cdInQOQ4xqQSGZo35rg1e-Uj0xYA1gDtISSzQzgpPkRN3BF-1I685ruIUrFcvcYoaPWi_evz6SAqTKWypFvyV0F_6YI4e-spXX_5jchhaiCSaM3T6WC8R5_aadsPHJ08heR66XcjTSL1cmxJSI5E69C3lKK-MBxDFzbpCHk-lqmaxk8yXCIduByiKlg4HiiFxzZVObbpIuAAbz966RGF6hUGXblwDFiXZhFUo3_mOFSGWVDG_ "Compact Legend Layout Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH Sample](https://www.plantuml.com/plantuml/png/NL1VIyCm47_FfpZdmphOMZS4mQVLCXouQR6TubF9skW2QHAIgsM8tzqBcvkObuFx_RtCFNA7NQjWbRuzRSegBQhYOL5cIoXuQvLW5rBNgci4x12jlqqIn_luG-AkstPUkDfe51hZshI9LLm7hud7HibjabrFyh3Qh5V9voo-YQzeLMMau58B5rlYClO_E1enbWldZOvuqqezXa4QflJeE1et6B5Yxr6qrPtfTCFTFggdOnWU-Wv7yCM0tYacwiMsujQIpwlOGcgjaZL7QVI0Ljdb6D8YZnyN9KcSW5ayXVLB5h1KATDx26TwG0Dqe-L4QJk5ahAWx2MYS82o5OgoF7NxFhQBy02Ipv5687iMwlUgSwsD9oNDPLdc1R42wOIURUu5KerUXF7kJFjNCXUw2R_v0m== "LAYOUT_AS_SKETCH Sample")

Additional styles and the footer text can be changed with SET_SKETCH_STYLE():

- `SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)`:
  Enables the modification of different sketch styles and footer.

The possible font name(s) depend on the output format (e.g. PNG uses fonts which are installed on the server and SVG fonts have to be installed on the client).
Additional is it possible to define comma separated fall back fonts (if the diagrams are exported as SVG. Atm
PNG does not support fallback fonts based on a PlantUML [bug](https://forum.plantuml.net/14842/specify-fall-back-fonts-is-not-working), but this could be fixed in one of the following versions)

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH with custom style png Sample](https://www.plantuml.com/plantuml/png/VLFRQjj047ttLqpLG1HGv2GK2WL3N64IQEAQhfAG9x6Inl7MUn6xexYczDyx6ryBRVMoqioPSyxiZAu3IK-zqODtoZQwRn4MH5tuD1nwkSfV52twkW_e6sS9BUMDCyDEInjhpWErMjN3uiFvB8OUxk-6hrVvn_o2GrN15L9Pz7aN-GTYKbRYowGiRYjHFjzDqfFwfN3Q-L6YrSk2QjrZai79dEksyLre9RrLTeTkfLzwR3TOH-YVDkbH8fP8pUAGAF47ZPB2eoHiOUuyj2eqVGZAsUHiC3Y5sVG6LjmaH5NuhatL6ACkBo2bTQSQgVKQf7MqGB-1g01y7UtPNzg9-QaqE4eEF1iLyRXJOS9QDiithW3t0cwOMpLPuOngG4WRWnaSFlbz8VMoTjAt82Qxr1HxpA3fVL2l_18OUSvJKlDZur7IzGJ9NeVji9l_EF-NeoD3V_evihDpSp0JkxyRFtzzAAkns6gc79kX3ywciZNAPf2Cuwa2UKdESurO1q9JVNQzvLclq-OoWrCXJQVnz0n-3e2V_NQbAwmhsNNCyuGrZBjES_iK9yoXudq6Op7BfvEIIpp2LNu9zuz5p8srTgktSVe0v81NkvCCCRqcnLfGyWNo5W4fWvgr0dlxjNMNqYR9F5jORFORwbrN1riFWIlvl2tBcM1K1Esp1veRv8sW5SPZxfqvBhb6s_9Fz1i= "LAYOUT_AS_SKETCH with custom style png Sample")

SVG with fallback fonts MS Gothic,Comic Sans MS,Comic Sans,Chalkboard SE,Comic Neue,cursive,sans-serif

![LAYOUT_AS_SKETCH with custom style svg Sample](https://www.plantuml.com/plantuml/svg/VLFRQjj047ttLqpLW1LGv2GK2WL3N64SgEsQIad8arX9utZhlOZTKLnJ-k-TZQ-bj7fPQURCEMTsHdUUXADEgzuxQMhLDGWhejP_6WoSsAGlabPTrNbqjJM4XjBQwa6hX0arLvuQ9Qj1zk5g4K8Fi-dWzJRzc5vpgCouGaY3Bcq3VoyV5sN-PLnazsLUF4_7yKNrabbbtJ1IycL5bUemIk1YoNNx-26q4Sv8Sq0tmgqTDZki9NHFk_GmojT8zUgKAF073QFCeI1iO6aTDDBNdVVIckYor-l3OZw13JS9GHM-ArtMMikRQuXfsyfQABK5OIojqEqWqWDVHtF9jNyt511peN4OdPXsEldZGOSfAr6ltzWyp7AOCBkiayngMKCkJ0WcSFhazvLGwyeArx3c8JN73XEeE-VbAxzuHbxndEJot7gGj1r1TDHXE__p_Iy_PtR-T7Dcvk3bP2NqFXqzVtqeob6-rumvja3dhOb5ewL981g5KtfoWgmB1hUUK9UVRMTurjkulacWdmlTAknVmiyUy7FShdY3LIdQbdcUi89HsofkdiA4EPIzJs2KBzBvkE0IXt2Rti3iCGkvaL9sypPEvu4iy6gtWY6wKoHP2mg-FjuY8AbHiPPdRx_sxcBQ9Pbd3mlDVaDrwEfawy5p9P_tHR786HL0n-o9PeAy3xJ1S2oTrUSbTsWQ_eb-0m== "LAYOUT_AS_SKETCH with custom style svg Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![HIDE_STEREOTYPE Sample](https://www.plantuml.com/plantuml/png/JL1BIyD04BxdLwprq1JQn1P1yDHOWnMiXYPLF8LDCjg5VR4xCHJnlpkBrRgNWVcUiqkFt66lP7GcT2lx3jWUqVhhD7LyIDu5xlkcz-1Qen4q9grHgPLS1ytCOoT5awukPqLOxJOFwSSYkKekQ5MlIC651fVOu1-jxs_pkgpoRVvKlHPvF8cY0fmtEkQT4dhAHbcOmgFZQDne4fK7Zw3g6zFhZhj3tCwdR5noPIMC9-mpOlJ-Kk81cffRIpulqB3CMYbQZiBe4QrMvrEMbKNoc5SaSS0MoPnjdbS1owGqWsVXIi_GC3hHSgAeNgAWB5OD0X4SGw50KfQdRb_7TZ7-WEHpf14ORK7-NdMgjVEafBckgg8aLY3zeIUREq2gCK0ORywe_v8bw8u-yni= "HIDE_STEREOTYPE Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

![Predefined sprites Sample](https://www.plantuml.com/plantuml/png/XOxD2i8m48JlVOhOau9Df0Y2f_vS5GhIiyHcjO4q3Sd6lhvRKHGyUDfXcFrcYe3IOnmCSnuKNBK5nOBp6Y6manoSWMIXRMUY0jOZkh0Nmik9tpJsyH83-6wq21PvDmx26MbdMXPG6NqHzJPhPgiz7iGzvpk-8UjSquUa9iyTPPEa0Hz6kvnXvPgbBLrMfgGcAlaTnjmpFmTUQlMDgDw8wYyY_p1oWXHW5Grw00== "Predefined sprites Sample")

### Using HIDE_PERSON_SPRITE()

```plantuml
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![HIDE_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL1RIyCm57xFhuZpOHrihHk2uDDg7MxWPbaxVInf6rqWDv9Jon3_koTiRe9vEN2-wydS0tFGAKcNgyT5bI-snSkcAlBjgbpGWYahERaIkf5To-aUmFhx976iZpy4xBkwyzmrHWFN43T69LOo7Tmc7befwYIxdUHXjLi_9v-p-2w-mLMLeO89pLriaKl8_-XeH4ZEdJSwOgqIUam7QPZ2WsDWt614YeC7hge7q-cMkKFKJCTqU6my7D4lGl6TWwAUrnMp5dtUU4rJQwLe60YZ1xZAhiSqBV9uioXHuZYTnLEwViq2baffUa_3ePw2eNYbPKXHdGI1MRJi1G1t58JY4hCyTli-jOlW2ABFYOOWsNBvUzMbriwZ4kUoBFC2MO5qHYysJnomHi_3U7T6_PNCkMx3V_u0 "HIDE_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE()

```plantuml
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![SHOW_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL7lIyCm4FsUl-AS7zR1rkeG13-jZg62RcMjxcD9sviBf4b8hXOH_tUlEd-08N1mxzsxzv958EcfQpNajvjTcQss-MPTvjdshbX1BbkdKPmeK-kkGJWGkN2L95xsyREYGrTr0Nrj3Q6XkBPjuhGqWzeiKADLbImlPjdGUdouJrxcyMLyngrooHDI6VInOwuGoHZMbi0WDjX0XRLaNQ232i2N3WWDxcMd2NhU2i5vHGWZXpvOCu9n8lwRZoP2P9-4I3QjCbCOfKDLWRmawqSJaRy6mhQyjfrff7-DwlCfZByoZoVm9e3FZzMenwgKph7E3Yj8dTEgbgJO0BUMfrD8yonUhmeUyGZp-1mUdfO3bcfj-m33Kt4O2_nEJZAbvK2ATq71gGWza6fHywx0tjwFxYBw0bddI6DGR55_f_grzHXuakjjKMGvimRI3_ehSuF4DdeSojxRzk_80aqp_CW7 "SHOW_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE(sprite)

```plantuml
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml
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

![SHOW_PERSON_SPRITE(sprite) Sample](https://www.plantuml.com/plantuml/png/ZL1DIyD04BtdLwprq1JQh1P1y6GDnGf-X2RgCMoJqIxi5xiJGn7_kxFsIpovbs7dlNdlpLm751uxhP8JQHhLjS3MY2vSSUv5dxrBN7UhBe1lh44mc3LMSwU4YJEJWAsIAvvVJ8hOUdwuvn_Jx38xerQTquIG1dpcVlHRUACViq4KzF-7JUv5M4EhfMdvNdzY7PW0JUSbReHlrXAXmSx3T29fDd0j0e8_RhEpuxdLsffTbB_WCpbpeTGMJih5qsjTp9VbqsDT5ikxQfuEY5h7WFMx1p3rmNemIf82VB0c5J7gc0rciSg0Ng3rX9SRYgJh6zkPLlXDsfoFsR0KsYaOZjXdmkWTZfNsiAg5SwJp2YisSqx9Hg2qPa2j_7JCPcMHFSuh6l70fjavUtZ98pPJolQ1nP21eMLqGYU8eZk5ahnOrKkasp2K6XHv1ShsjKkNuXOadHqjBhO4jT_g68kE5QBVeggAabYHT42FChU05AE7MDwyrRz7hi6qTEbl "SHOW_PERSON_SPRITE(sprite)")

### Using SHOW_PERSON_PORTRAIT()

```plantuml
@startuml SHOW_PERSON_PORTRAIT() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![SHOW_PERSON_PORTRAIT() Sample](https://www.plantuml.com/plantuml/png/RL5DIyGm4BttLuohi5rOMrq4GH2iYwYWRjbMFPQq7NS3QHAIgMKH_xiJwzV173hfp9ltvaqkF0b7VQUWk5azL_dLkbWzLFbgNQwpspAUGI4wgp3QaxfHVOkm9RB-B4sT69ADf6rVznvTOpIXfgGnNMgLq87nq5EhP9qkJmxpa7gylqjV5ybfSiIfQiaTGcfqYMLi5Fql7qKvEczqBDfEwZbCiX2b9oV8kCaiAdQUiAikJQzRuNPnSpo7wJZpT0Pl4V3vaOe7h2jXBVCyOmsPjKesWgJH4qujz-UG5NdoS5LoYqDO9CTm_xGCjKmfCtW8LZsG0VPf1KEwNf5aBIW7IOGEI7QeMClpREzVqyKq5fdd2yR5Q0ho1GJOJtyWVU2ikRC5ncovugsJX41RrE433XiIUiDYIknCJw671sf1RDZTzw96FfOQ_qUoaOgD78otyya8MuH1rgY-r_kxdqVF5ZZUb6LUC2g0Vgg_VgwHU1y3Xl3YJFUtvG9roq_x0G== "SHOW_PERSON_PORTRAIT()")

### Using SHOW_PERSON_OUTLINE()

> This call requires PlantUML version >= v1.2021.4!

```plantuml
@startuml SHOW_PERSON_OUTLINE() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Container.puml

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

![SHOW_PERSON_OUTLINE() Sample](https://www.plantuml.com/plantuml/png/RL7VIyCm47xlNt5EOHtCLeSW289p31LqAxRJnvAsvnP8av1SBKFytxrOVpsOXrvwzztttNUvyYGSTQs2_7RzN6RBntozAjURulvkjOmda8lMAemEfAvLro3iYAo_I5Cd-cGhQTTLdKTN6qseAQbDcrebT20yzjGeMQMBi-Cif3OFz-dhB3bFJZXLBhX3I8qkiOoDed_LeoX3vusEHTDAFONHF4JfoGaoRZI9yhqdRCjhq-b6k7rSdqvXF8mydi1R17n-bE8Ugr9OoppFMC7SMYLhGTBe4QSMXrEOvrcoMXRSuX1coIayF2r2RQwKwJq4fnx80DkqWY5jfqYo5XIz948795jKhELvjlUlwM8QYipp1UDYD0Rv0WBifp-GFd1MtDa0OtPSyTP9Gg0Twl01XpK9lMKn9VQcez330pKWjkpkUr437qiD_mFPGCL6ZeRRvMY0pS8WZwY-r_kxdurd2nnlYoBB6HL0FzLVFpT8l8yUGtXnfltRSeMw2I_x0G== "SHOW_PERSON_OUTLINE()")

## (C4 styled) Sequence diagram specific layout options

- **SHOW_ELEMENT_DESCRIPTIONS(?show)**: show or hide (hidden is default) all element/participant related descriptions
- **SHOW_FOOT_BOXES(?show)**: show or hide (hidden is default) all element/participant related foot boxes
- **SHOW_INDEX(?show)**: show or hide (hidden is default) the relationship (call) related index (sequence number)

show is defined with `$show=true` and hide is defined with `$show=false`

### SHOW_ELEMENT_DESCRIPTIONS(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Sequence.puml

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

![SHOW_ELEMENT_DESCRIPTIONS() Sample](https://www.plantuml.com/plantuml/png/LL5BJzj04BxxLqp38OuKx88gLUg9rBK0YGGBctAqrjw1hBIlxewn4Ef_xsmR6jZBI3FpFURRYqWYq6HqzadPKKyIOK_auxUo368kdXJjfs6A64Pd2IqLepEbry8cp6aagTLGLbzEczIwtzwKp-V5r-8pj_eMVqreHonyei_Qgzk7lhwfj_Mkwt_KRNLttNJNjxisNsLPWo4wcmjfb5t3OfEgYXG4kR3WHeFEQmJQ2m9n76Ba5e8FJauZnSKgQryYeUc_kybA4LxoyMmDorOOHYzN6V2h-12XB8Pyng4NtZFz0mwmyLwhKP1oDYbM9slOj4sngpk618JpuWosFwiqssZjvWWf5ZRWW3FnWbVCf4abdzsiY300AOEQjPAp9IWB0k8X5P1AF0LXuCrgNrkPhs0l_b8EcEWbO_WU8S4z0hp2x-pZzk7SdFxfiRM3CkjbTwZV0ZrUUX_P3DUhhcjQtafB_wT7caiajZ5ZAe_1cVUG2xIIV_GF "SHOW_ELEMENT_DESCRIPTIONS() Sample")

### SHOW_FOOT_BOXES(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Sequence.puml

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

![SHOW_FOOT_BOXES() Sample](https://www.plantuml.com/plantuml/png/LL79JiCm4BtdAuPoQ2gL110I4YTALU00j28fS8kSUA2Ml65FY13Ytnb3sNmPQVnM-pII2DGRdUqes-bU8co8V3mfoo26uadHfc_xYA5pbj1IqJbJUYriukn5abgrvVneRvLMw-khykMmE2xsUTLK-DoZxR3mIJwhBfVtpVboMJTdouT5bK-oR8KXEfiBQPITmcYMfeeK1BamccJLQoGqpPdhhHJXDUyEfZ2kXF4QnvCC-Cmvb50MGpvWsmZlMUKUMvXvhrKdI3axujLyTmgpQbNSB6gc18J3uW2kx-RfRgQr6oAaYX780VVpWY6crwJO2Uf14M40KWOrUqLEDWPbGK3SDWIfn5CG1hwZDWihymbinATaYqbUCeVx20dk4U0DthF_w6tTdBxyEDhMcVsoMzJVp_JRT1qv3C_BkbvLZ4gWdzjVcGiaZZ5W6e_1cR-KKxIIV-S3 "SHOW_FOOT_BOXES() Sample")

### SHOW_INDEX(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.7.0/C4_Sequence.puml

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

![SHOW_INDEX() Sample](https://www.plantuml.com/plantuml/png/LL5PImCn47xVNp7MXswXtLKH19-ijQZWKTnwl2tPpTG6SfdCkeZutvrewv6NWSbt9YUHHA3Ew6n7sLPt4c5DvEDnMGRH5y-ArbtJHGojiuIMYjQPqcjX4sSIIMhLbBF3oIAjxg-lojU3ugZOurLTuKk7jiN29_cikhXzh2zlpkPF-IZB5XYYixcGHjan3APfgaX1a0k3KLQzHK9JdxhEIX7UydP_3CDA6AznECg0pupp26Knv3qsjV2ULHwnWQdtMhM2bBC3Nirsnp2j5iNDVCcKW71GxCFrmopTJRLsVOJKBW8vu6fUCCHqcXGxmR9NH1Y0b47DNf6J3K5P410tvK0gyHo4WMtKUcvbFeAr-99iCCbBvd0V8S6j0DxX8_kFtjJDwTkFessSsI-xGxrzfj-czv73yBnOBXSLenBev_PNvXo9O_IOnYeuyvToWbRontm2 "SHOW_INDEX() Sample")

