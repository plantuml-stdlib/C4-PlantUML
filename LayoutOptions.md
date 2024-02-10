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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![LAYOUT_TOP_DOWN Sample](https://www.plantuml.com/plantuml/png/JL1BJyCm3BxtLvXnM2TjBPkum6cb83ZiKR6EYLELjXwBb2PHub9DYF-EAyP65CcIluS_U-v9E6eR5Ln9NQcsHZWGMNyVnqvqqOUaGrks7brbDA6cg39DR9NGlMRYgLQoZDFRITQtjij5_3cBxg8RRXKfAuJKw2BR-mVn45Q6G2FMM4E9bM1Ve8Fqm9yE23NkHQi8Xd6mIDxNsxp8rrdnkDwjmb4GPEYyqQ6e6wd7C4ZwAZqvGSODHi7cw0cRui6qkXRk65RJCGmteh4AXoFu2e3VELBOOLa8QzbdXoKarYfP2P963xYLNeyXsMJHwYbdYKEOHLDOlgKzbYXbEW_zIJYq0Rw75KnfEBZaMP1taWWTa6nGyIpFsRvFwKBw1TddH6CmU4NrjzKbrjQpakjBdcSRPlMaCtgnUKRY61tsPUzCyryoHrtpvNy0 "LAYOUT_TOP_DOWN Sample")

`LAYOUT_LEFT_RIGHT()` rotates the flow visualization to _from Left to Right_ and directed relations like `Rel_Left()`, `Rel_Right()`, `Rel_Up()` and `Rel_Down()` are rotated too.

```plantuml
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![LAYOUT_LEFT_RIGHT Sample](https://www.plantuml.com/plantuml/png/JL1BJy904BxtLwnue2JGYl6Y9sg3O0BQGD5uQhRjA9liAxjJ6sByxyv61FSooNpFsPb7xh1JCheGkf5T2soFQFrTcZhU9ny2zrtTUN2DqGWQayQer4gkWsRYiPMYJlERIH5Mk_Kg_RnERfChMbKvARZGu18R_ADLzlQyAwlL_A6iDe-BPHcFegW0vusEUQk47hD15gRmw3WQDnX5suD7KDMzwNJBtI5kfcCst79b9Gn7x2jYz4uvSGzrnQqbdrUeMMQj50r7OVI0Lldbc6NR8dcQboHnmAwJALk_v07Bf3IzP-5Epz0mEj9oegXEeg0iLlO24Hn3eK1IbgTktyTsCVw2v7Ea4HXjGFvTTQwrywIakIpBOakiG3gXPvi58DNe8OntPzH_oGnqIz_v0m== "LAYOUT_LEFT_RIGHT Sample")

`LAYOUT_LANDSCAPE()` rotates the default flow visualization to _from Left to Right_ like `LAYOUT_LEFT_RIGHT()` additional **directed relations** like Rel_Left(), Rel_Right(), Rel_Up() and Rel_Down() **are not rotated** anymore.

```plantuml
@startuml LAYOUT_LANDSCAPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![LAYOUT_LANDSCAPE Sample](https://www.plantuml.com/plantuml/png/NP91RwCm48Nl_8hPxA54Ig6jzh9xAWjHUw0fYg7Ldf03RcF9s9Oz55Mh_UyxJcWQbOl5zsRUl37SUkGEnq51cVrvREgsp3O5oxDg3OmFLedeczIT6di1UqJhVwMfurFoAd4_xaOlN6Sq2er9PuRKAgw3rwN7NibTcl-uh09g7ihqxIRvcLmHQdFgu58BbrYgZQAlW-Db55N2UQDZtWzIhs2HXLDwT1oDMomZzkvH3ErlC-gUk_Uukrx1nJ7lnHB-Ha3FQKmyYLtBhIMVPx63p5ebEuxIw0MX_FiACbObctLDBKx0JN8D3qzvq3AbpEGXhEa13T2EbbF9C2gKD0lgII8A1oW7eMYMfsp_vdGn7aNocSj8ZBP2VMpr6Qlnr4ddVLrNZAf2qKdzjBaJI34c4OuNPuRpbe-XRBLWfmkAMKElqDWpKWHIc4cViJAmKhpW6Ti6jfMlUvnZjuqbTo1B2coFATjWTA05qTary61su2NnsJdmW-51s99micVtZyzjkRvRRuhmzM-5xkdN-0y= "LAYOUT_LANDSCAPE Sample")

## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype, ?details)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```plantuml
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![LAYOUT_WITH_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL1FJy8m5B_lKrGyC1BOX7ZH4tCIC05St91uMhhjAKswjcdVN8Znk_iQ4Upb9U_tztNka5liMXbS2LNBhW5sG3JkFeujxwCFWOUkwXpOMYi4XL6jszX8hhncuh2HeehJsqdcLxlDElwSHNVH3QtAb1HSAB2HyVx1EdbxtXNb_gbObUl5Sh5z34T1a85rMeMyQOKQiq7Yft1eEMex60NvqI6qvOFkLCFjCQodOpRCUMia34ViAs3qpa5X3rN9ZI6VFLGiCKQAcgFGQa2hz7hCaZoBjek291ROB9gopMlgiKHAtJlc3tKCDQCh3ITAsqaKbCMANY22PIXQa9JbgDltgLs8lo3vd6W41YyW_wwwrDevKj9S5KMM4ykJpkZ5PWb8DNhmuztgzhza3ggX__m1 "LAYOUT_WITH_LEGEND Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![SHOW_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL5DJy904BtlhnZnG4cW5UD5JzPAu03OM91ZisrNsMI_iZkr8SR_xZGWi9UNpFkODzddWDnZgnKKYxTTkPpDP-jNABXsIh0RQMhLDWBsY2uy9OddNVmbSTzMRH2-jWQ5mRYsEd6Acpvc4h1HiagoXqdUZxQhPV9z7p_6TpGgCt9mQOIF7MaPouKFraIyqTACOP3sA0DwZjOFHgmu11IwVB6jQRW_HFLq3CDZj-48VXZGEqT6dQXAxXpbx4G5gNDArXobDGCQPRTZI8iyNiysPF42xkCfh3wodakLibs0_gG0Q87kSPmakbKeQHTiEeaeFA3KGj6kGDr-J-qYF9AKSv8HoTw5-h_gKciRo4cus6poWbIzwCnUOkO2gKOdUlZqLbzRsDKlHIFs1m== "SHOW_LEGEND Sample")

Legend labels and details can be defined via `\n` in `$legendTest` arguments too.

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml
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

![SHOW_LEGEND Sample, $legendText defines legend details](https://www.plantuml.com/plantuml/png/hLHDRzj64BtpLumP1nK1cMgRvj020g98RED0bWn9Rdi880p95RN8SfVONIecYlxtpf2KB5ikUkc5u7xCp7jltkm7vz7wkbJ1Tv0PVH3MW_JmJVezO9vBBur6HKTbYJe79RK0j4LT2ktXPhPAvfFDxU_9zdOndJ_Cad4OZ-8u16-WTWAKoL2f9hYIEtXxG2inLM8h7gNpRX2-30wZ0E1AwapLkO2tXV3RKym1LIrU2nbDVzfEZVP8o6nSCPChePmuJxNtldA_Z4OMlyK5CQjJ0cU9hYSMCN4RLGergt3ZVAvaIablxddhuMu-ElmO_nn__seTdSiT2NUjH47_6_7OA_T5GovsTDE1tvCCc0e5h5ykA85oO7RTGHi7XC8sC0XJpBxoEZlM2K6wBde8eP35teEJkSZ1xR4IxMcVCO9WakU94joO3HQdP2VCuH2kTxIO6cNi-3gP9tV9OhFzTKcVwNA-ND5vMdIduPjtxzxF9kyvfYqrJhZuccklUJs8XkUinvVGl-XBlD4hMfdQdyjbj6e0UyMOqagebWwwHcUCnrDaps6oMYt_E85dR_xhmTetIendwFOYdzFwWa2R7zYkBKmoh3RFm7O8SqQ01IkFjJSbUjbQ_4MVQUjyV7Bfo64D2L5PKz6CIQAALhHHVGVFoJAMqV_3s7X_P1m5mRfnNfJRZwRMETfcaFr0nhgbER1QUFY8-glKHHZ1NpG-02Vl34gJIff2h2gwVzSkO59LX2wSlXd2drZIe6fUtbjpe9OxRg8ifUVcrwcZxBtdJzNIhXhiQfrrEadVyCkHrOwK5TR1GIB7I0iT0DBg83FHFXJdy7ht4Jv942RtjmnEKMSuBwFwZ0SSmipGDGld8_64zpzmCHHA77RzT-FB-Og2lu_w9ez-qAVPkdQBPQDhEukbEEeCtMr6iVR6icPacrwcZ3PEK2ZGsB9b0vZoo9mq6W9c6RNJqv-tg1sse6abV1OJg81CzQn_pyLwSC8nWjPjG_YyNYv6dpQR-_KJqyw84IVQBdYgK_D2yWkknwnFHYQJq5lw8lEPpzcSdyZ2y-ItP34RHC47oawlx3y= "SHOW_LEGEND Sample, $legendText defines legend details")

Legend details can be deactivated via `SHOW_LEGEND($details=None())`

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml
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

![SHOW_LEGEND Sample, hide details with $details=None()](https://www.plantuml.com/plantuml/png/hLJVRzf847xdhvYuYGeICNVNzg4d8PM2Uqr4809olOTAQ6mlPfNrhhMx9h6g-zzlnZQ4X9pwqXVB-sDclk-RR_QJysXzcQlEMqYCtWdhGNfua7uBcARIIwDHqL6Ueqv1IIq0RLRcGdkud2oYwMXrzNUqlfgDftUJQ1Y4Wp0Cm1iedG1b4bIgwfp93Lpiq4gCbLYBH-cywmOlWuDU1-1CwaILgO2BJFZr8MQ7gXIlXGp6xzTZepqICXiMpEHCA2UEKsszBzoVWu75Xp0ZPcLCu2pHzSGY96w3Gg5c5IwTJvMCAUdbBM_TtKm7kp_2Z-5lhzRHgToGSETAPFI_4e-jSjyrf693DntuBSc0iL30-gM24YW7PjCSr750A6m5tI36v9xNoRvE0D8rqNq8XCos7fnCHGfkYuMeJzkCFUYCqZHIWXkpmkoGx80vwCFvXXPZeumTdaVJw2QQhTPVvlGPpwVp1Pt7MNCQl7dtxiDaz85ZwbB3Y8ilkVQIrzrU_vZry1JwTtsAj_UALgRqnt8PhIh0LZ6cj12gfeEkqWdZyHJPSXWj5lDl1_3ipVyzMFfAYU44tLQaKrgV4AZp0zkrXac6rUOPs0PXoWWmO-Mnz2P7BskBl-WpRHsFJoeTEQmY8Gfh2fenILJHYZggxU0nMSOo-3MCZVTxnhrEPravB_BrPrFg56tLJNudOrtH75WjF7n6VIzr5lJW1uqFmC4xtTp4agOGYuBktzGB61K5eGl6R_hm3-Oqg9gNjzRigEMEcoXpwRdvPUmeU-lvGxMugGQRKYUDJj9N_78afIDbXNMmayWnqa83WBJQoKJK3yKnlDPzX4yIXD7j5ODJr1dEowYkSOTzc1YwPk5u99xm_WGNGw74GTD_DpoThrxdtxs-qQFljcdMhjvYsUZQnc8kzZf3SvjHBBsnh1dPffKfeOq350eqDg_P0COyCWUD-e19GktqzESjQeSrQ5e9duG4gaEcUjQ_vsBTEU4OGUssFbmlvxF1rzNgTld4j35YZnEjPppLiNaX-GdNVTOd8vD9w2rzaVd8vspEhsJXQVHND9jqpzkf6CvCOzrFL8mUtVy0 "SHOW_LEGEND Sample, hide details with $details=None()")

## SHOW_FLOATING_LEGEND(?alias, ?hideStereotype, ?details) and LEGEND()

`LAYOUT_WITH_LEGEND()` and SHOW_LEGEND(?hideStereotype)` adds the legend at the bottom right of the picture like below and additional whitespace is created.

```plantuml
@startuml Layout With Whitespace Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![Layout With Whitespace Sample](https://www.plantuml.com/plantuml/png/LP11JyCm38Nl-HMXfqvYAK9SuBJHLd0eCBL2FLPfOj5AQHer3h1_ZyEaRZl5_loUy-ITHxbWc0olv74EoDiH1zuE8u9tKW5lvEGCi9lHAXCqy07H-QSiM-IF-29jw8E7HSqMmQ9GyvGv8stSkFMepTXd-SFs4D7dMvLztuj7SKUeoyaXHmkBSAHbx02BdsqgRtboAla-sR1LbVOqM3l-d52Be0PBekRe4QPK4JgLFB-owYjhSMbTSLV-OWeqeLVmixgyLBCQJ5V7Z36DaiPueX4MCLyCGCSuCmBwcjKnJFmcE2tn7xFczQFjglAbV2_I3Tk1rNIGFm== "Layout With Whitespace Sample")

Therefore a floating legend can be added via SHOW_FLOATING_LEGEND(), positioned with Lay_Distance() and existing whitespace is reused like below.

- `SHOW_FLOATING_LEGEND(?alias, ?hideStereotype): shows the legend in the drawing area
- `LEGEND()`: is the default alias of the created floating legend and can be used in Lay_Distance() call

```plantuml
@startuml Compact Legend Layout Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![Compact Legend Layout Sample](https://www.plantuml.com/plantuml/png/RP5VIyCm5CNVyodI8jY2QrLyKH0srpg5kerDyJ5aQRO5ihGaj_xvzjwiMxU2Bqtok-USUzCC7N0BpKwJG1cXcrBIBK3j7jBKykzaes3Rh1edhQWCI0E9g7PfhRdnde63KgjLEhuRp3twU2lIhzlaFhb6nCReuCf8czG-dv2vjAuo4R-YORkbep0cdInQOQ4xqQSGZo35rg1e-Uj0xYA1gDtISSzQzgpPkRN3BF-1I685ruIUrFcvcYoaPWi_evz6SAqTKWypFvyV0F_6YI4e-spXX_5jchhaiCSaM3T6WC8R5_aadsPHJ08heR66XcjTSL1cmxJSI5E69C3lKK-MBxDFzbpCHk-lqmaxk8yXCIduByiKlg4HiiFxzZVObbpIuAAbz966RGF6hUGXblwDFiXZhFUo3_mOFSGWVDG_ "Compact Legend Layout Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH Sample](https://www.plantuml.com/plantuml/png/NL1FJy8m5B_tKppnm4XW4-95Jyo5I2BeueR6qrAsAaswjcdVN8Znk_iQ48ozlEJz_hxEFNA7NQjWbRuzRSegBQhYOL5cIoXuQvLW5rBNgci4x12jlqqIn_luG-AkstPUkDfe51hZshI9LLm7hud7HibjabrFyh3Qh5V9voo-YQzeLMMau58B5rlYClO_E1enbWldZOvuqqezXa4QflJeE1et6B5Yxr6qrPtfTCFTFggdOnWU-Wv7yCM0tYacwiMsujQIpwlOGcgjaZL7QVI0Ljdb6D8YZnyN9KcSW5ayXVLB5h1KATDx26TwG0Dqe-L4QJk5ahAWx2MYS82o5OgoF7NxFhQBy02Ipv5687iMwlUgSwsD9oNDPLdc1R42wOIURUu5KerUXF7kJFjNCXUw2R_v0m== "LAYOUT_AS_SKETCH Sample")

Additional styles and the footer text can be changed with SET_SKETCH_STYLE():

- `SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)`:
  Enables the modification of different sketch styles and footer.

The possible font name(s) depend on the output format (e.g. PNG uses fonts which are installed on the server and SVG fonts have to be installed on the client).
Additional is it possible to define comma separated fall back fonts (if the diagrams are exported as SVG. Atm
PNG does not support fallback fonts based on a PlantUML [bug](https://forum.plantuml.net/14842/specify-fall-back-fonts-is-not-working), but this could be fixed in one of the following versions)

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH with custom style png Sample](https://www.plantuml.com/plantuml/png/VLFRQjj047ttLqpLG1HGv2JqfGL3N64IQEAQhfAG9x6Inl7MUn6xexYczDyx6ryBRVMoqioPSyxiZAu3IK-zqODtoZQwRn4MH5tuD1nwkSfV52twkW_e6sS9BUMDCyDEInjhpWErMjN3uiFvB8OUxk-6hrVvn_o2GrN15L9Pz7aN-GTYKbRYowGiRYjHFjzDqfFwfN3Q-L6YrSk2QjrZai79dEksyLre9RrLTeTkfLzwR3TOH-YVDkbH8fP8pUAGAF47ZPB2eoHiOUuyj2eqVGZAsUHiC3Y5sVG6LjmaH5NuhatL6ACkBo2bTQSQgVKQf7MqGB-1g01y7UtPNzg9-QaqE4eEF1iLyRXJOS9QDiithW3t0cwOMpLPuOngG4WRWnaSFlbz8VMoTjAt82Qxr1HxpA3fVL2l_18OUSvJKlDZur7IzGJ9NeVji9l_EF-NeoD3V_evihDpSp0JkxyRFtzzAAkns6gc79kX3ywciZNAPf2Cuwa2UKdESurO1q9JVNQzvLclq-OoWrCXJQVnz0n-3e2V_NQbAwmhsNNCyuGrZBjES_iK9yoXudq6Op7BfvEIIpp2LNu9zuz5p8srTgktSVe0v81NkvCCCRqcnLfGyWNo5W4fWvgr0dlxjNMNqYR9F5jORFORwbrN1riFWIlvl2tBcM1K1Esp1veRv8sW5SPZxfqvBhb6s_9Fz1i= "LAYOUT_AS_SKETCH with custom style png Sample")

SVG with fallback fonts MS Gothic,Comic Sans MS,Comic Sans,Chalkboard SE,Comic Neue,cursive,sans-serif

![LAYOUT_AS_SKETCH with custom style svg Sample](https://www.plantuml.com/plantuml/svg/VLFRQjj047ttLqpLW1LGv2JqfGL3N64SgEsQIad8arX9utZhlOZTKLnJ-k-TZQ-bj7fPQURCEMTsHdUUXADEgzuxQMhLDGWhejP_6WoSsAGlabPTrNbqjJM4XjBQwa6hX0arLvuQ9Qj1zk5g4K8Fi-dWzJRzc5vpgCouGaY3Bcq3VoyV5sN-PLnazsLUF4_7yKNrabbbtJ1IycL5bUemIk1YoNNx-26q4Sv8Sq0tmgqTDZki9NHFk_GmojT8zUgKAF073QFCeI1iO6aTDDBNdVVIckYor-l3OZw13JS9GHM-ArtMMikRQuXfsyfQABK5OIojqEqWqWDVHtF9jNyt511peN4OdPXsEldZGOSfAr6ltzWyp7AOCBkiayngMKCkJ0WcSFhazvLGwyeArx3c8JN73XEeE-VbAxzuHbxndEJot7gGj1r1TDHXE__p_Iy_PtR-T7Dcvk3bP2NqFXqzVtqeob6-rumvja3dhOb5ewL981g5KtfoWgmB1hUUK9UVRMTurjkulacWdmlTAknVmiyUy7FShdY3LIdQbdcUi89HsofkdiA4EPIzJs2KBzBvkE0IXt2Rti3iCGkvaL9sypPEvu4iy6gtWY6wKoHP2mg-FjuY8AbHiPPdRx_sxcBQ9Pbd3mlDVaDrwEfawy5p9P_tHR786HL0n-o9PeAy3xJ1S2oTrUSbTsWQ_eb-0m== "LAYOUT_AS_SKETCH with custom style svg Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![HIDE_STEREOTYPE Sample](https://www.plantuml.com/plantuml/png/JL1BIyD04BxdLwprq1JQn1OlUcgimGfMGvCgdi8c6Ut2ljYT68hutvt5QjtBm7pFsQL7xh1NCZeJkfLz1soFQFrrcZe-9Ey2zttJUt2jqGWQazQer4gkWsRciPEYILUNioAiTfk7z6EHN2KNjAfNfE12Wqjiy8_MzxTvNLRvDd-gNeiydaHH0SuR7VDE2JrbeonCuT5nD6uqYSg3Hr3rZUbrnzqXRkTJDYwviXB64_OPCNf_AV40JSsj9PyNQ5XchHGjHs7qY5QhyodBoY9vp2kIE62BPCuspwk0PLAQmRDmfMTe69reEL5KBr5G5gi6WGYEeL0WASjJjwzZknX_GF8vqWYCjY1_hphLsdbIqbnNLL4IAv3-q9FD7I3L622CDsVKVyaIT4UV-Gq= "HIDE_STEREOTYPE Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

![Predefined sprites Sample](https://www.plantuml.com/plantuml/png/XOxD2i8m48JlVOhOau9Df7ZHKt-k2WNfMMApsa2QXcHZNz-jA0eUFEqmp7upHK3fCGw6EGyAhjg2Oi5vZH3OIGxEGBBGjZDH0UiHNTWBuUN4RnhxU8a1V3TQ18ky6mVXZBGpBGkeZBw8UfirizKU3-AUyntVa7MkwKDIa-UEiadIW0-ZNSwmSitIbYuhKr8JbVmEO-wPdmCljVf6L6z4zHUHVnWvGGgmYWOz00== "Predefined sprites Sample")

### Using HIDE_PERSON_SPRITE()

```plantuml
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![HIDE_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL3DJy8m5B_thwXuO2Im2V6Y9-OaGYAuiA77fTkgDEbNsZSNOlpVVGq89lRoalVxV9rxO0uw9UbozRYeyiMsUDbKHRvTbGjQC6Kb9rT2Dx9hETq3M7-V98xryOU0VLTtdhl6QE0QuiQen4gcWzl4Goj5dMItapoiTkldv7CMtyKtkAeoL32XkOijSWdv7nsD2CcvyqP7h5L2Z-aW3LDuS0oC6un8SV30LVLWEjqoTuYQwPWEZus78_f5ABvpKDJpkcBMeiyRhsbghHGD0s7q05VPzPYcHHvl5YLA7AUpU4hNhrd0KYbDxsaur5Cm5A-q32cgao0mYvQz0E2EWb1SOfR7Rj-dTX4SGVGvqH0aMov_hxhKsdbKuboMPLuWAv3EwCNcYGFMw7aOxywelv8vrstupny= "HIDE_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE()

```plantuml
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![SHOW_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL5DIyD04BtlhnZheIcqYHOlUceiHGLjGnFjCMoIgLtOx2wx4uE8_zs9rWzmMHYOz-RDUxkBGD9Jrsh8RpUxCbjjyyswpBFjNR62NBPEepXHfjPTWt0WSk4gIRpiusT5Xwxg0lhQ6a93SMtRn6bf1hLPe4QhAbbUpBAXzVXmdxpCuyluZ5lbaYUaCkXZnrmXaZ6iBO51RB212cl9ka075O0l7H0QtCjE4_Iy5OBpYX163dsmPWJZHFmt7qs4o3u9aMnQPQOmIeUg0db9reyc8dyDX6rvRJlJIFyQrUTJ67zb7a_WJG2V7wjHZrKfdMET7LQGEgTLBKcn0MujJwUGvbcyNXKyuX7cyJayF2q7BDNQzW66f-8m5lYTd6HAou4KxuA2Kn5w8DMYvbs1lRqVtKNq1RBEaSQWsAB-JlLhwp7m9DVReiXoPWsa7_HNvWQ9RVGubBstxT-H1Pfc-94F "SHOW_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE(sprite)

```plantuml
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml
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

![SHOW_PERSON_SPRITE(sprite) Sample](https://www.plantuml.com/plantuml/png/ZL3BJiCm4BpdAqmvD9NQ62ekSA945KNY4JK1Zf6RBDIINx8tH1NYtrdJ5-A4BollpCxCxdL0uR7JAZcHfb5T2soDwC8LvrxqsRl4TRVg0lZ66WI3MMCrTqgOE3C9s2gvuld5f8YjvuTx_Z7DBhCpQjKvJGXfm6VkHx-5D_en6qH1_t_Ov5w4DRHQcfRlzIVMWGdGT5xYHlXcBH4Qx3nC9v9c0zSY8FZZDZixdbkjhTb5-Gi-apCNIctXf5mylTR5V5a-FTPbiRohvkc0g7KCMBzx05CVh0UZ92d01sjI4QEEsM0Mgmpe1LfFUBcXIBg-iPrfXT-apVcO3KkXdOBXY7qcZDxXM6aFgreuHpgli68pvvHi14fh1jJAJyTiLXRPuxoY4GzicfspXvSyOZEbR1zO31aOMaOdT88ekbCeoOjLlKIw3KEfGP5Ne6nVktGfRa7IsT7YOajG-wsEiUXO8VejggeeYHL91_GeSmj8CNg8vSrR_Nla6anBb_u6 "SHOW_PERSON_SPRITE(sprite)")

### Using SHOW_PERSON_PORTRAIT()

```plantuml
@startuml SHOW_PERSON_PORTRAIT() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![SHOW_PERSON_PORTRAIT() Sample](https://www.plantuml.com/plantuml/png/RL5DJyCm3BttLvY1j4uQBKnSG4AYJ0YGW5LhWMELjcQBb2PHub9DYF-EG_awa4ETsi_l-JaNdeIZlbDGtAoUg_ngNQmUgdorBjVPRHdFe12TLHZjITselaNO4bb_bgPE3Cb6qhQlUu-kCPfGKzAOBhLAwC1uwAbLiawN9uTvI3tUtwMlY-GqEU9KjUGE8JMwn38sYlwNZw8SdJSw5cqdzHmcMOZIanDat6GM5JjFs5MNfjUjSBkuEPx3T9nvEeEt2FZyICK3rfMmbdcUiORCMYKRGTBe2QUM-tF8YZnvk2gvnI4iacEuVrg6MgQK6Jm4gnx80FkqWY5ThqYo5fI3948793jKhELvjlUlwM8QYypp1UDYD0Nv0WBifp-GFd3MtDa2OxPSyTP9Gg0jwl01Xmq9lM4n9NQcfz330xKWDkpkUr4Z7qkD_oFPICL63iRR-MI4BS8WQrJVw_tTpwDd2nnloZ8l61L0FzLVFzT8l8y1GtXnfllRSe6wvQVz00== "SHOW_PERSON_PORTRAIT()")

### Using SHOW_PERSON_OUTLINE()

> This call requires PlantUML version >= v1.2021.4!

```plantuml
@startuml SHOW_PERSON_OUTLINE() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

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

![SHOW_PERSON_OUTLINE() Sample](https://www.plantuml.com/plantuml/png/RL5DJyCm3BttLvY1j4uQBKnSG49YJ1CWmLRH3evLsfejKff4YKir8Vux3kNhG0vrQZ-_v-TSUHAEkbP1Vhj-BhFbOxvUbUjDSN-tMiOJo4Lh5KO7KjUgQn1sHDPVfAaJVRALjEkgpgEhZIRKbDIcJQqIEX0UUsgKhDB5sN4MKfk7-_Hrbfmd9vmg5zmXf4QNMCP6qR_gKPIXyqR7eccbdi9e7gBqv0GPDvf4-TuJjkMrwNGZt3wkJwSm7aOUJ-0j0Zu_Id6FLIciPPvdh61khPAr86dqY5EBmodCyonPBGjkSGYpv1GUdXQXDbVAz1w2KmzaW6rQmP2sKoHP2ufU4g43aYqgrl8ys_lNT34DHURvWd4n6eDy0G7sqnz87pWhxco0CJkkUEia8T0ETVY0mvg4thAO4dlJKUZXWHeGMtRtlQY1ZwM6_u5ie68ZHyFjSZJ0Pc6GHrJVw_tTpyQp1OwtHP7bZ0gWd-gldniataUF8Rmuq_vjkKBTX9Vz00== "SHOW_PERSON_OUTLINE()")

## (C4 styled) Sequence diagram specific layout options

- **SHOW_ELEMENT_DESCRIPTIONS(?show)**: show or hide (hidden is default) all element/participant related descriptions
- **SHOW_FOOT_BOXES(?show)**: show or hide (hidden is default) all element/participant related foot boxes
- **SHOW_INDEX(?show)**: show or hide (hidden is default) the relationship (call) related index (sequence number)

show is defined with `$show=true` and hide is defined with `$show=false`

### SHOW_ELEMENT_DESCRIPTIONS(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Sequence.puml

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

![SHOW_ELEMENT_DESCRIPTIONS() Sample](https://www.plantuml.com/plantuml/png/LL5BJzj04BxxLqp38OuKx89wQK-ahWL895ZObAErzWvafNrrTuo5KFzxPzlGm5v6cfdlCTzUH1A19gEpJygEUf88Uo8VlvLb47Fnf6W_3LF4C3fBQAaOdIcz5ZPXJYD9hOQo-dBQfDRzzgPyFY--5f-vrRVuQq8xOk4JVTPUtJxqzKszhNTT_wDkgxlhfhk-tRNvAiiQ3D7PN4YZx1eMcrHLf238XGKt6dHU8z1U48ZZ42Et47nmSXefBbPP-n89JV_TJLQAy9AFPsjOji8mUhdAW5_5XmXbCUGp3htmdkaVS82DzrgDWfIpIR4wMSEcROfTtJ4a89mNPx3zMQNPHcitHqYni047d8aNl68cJIhvx6P5X0586TIibPmjGLaG40-fW5JYAGW3RrRxsify1NlnbtB0H2yPm_S82UuHu1L-Pn-t3-Vcz4-FhHsKMI-xG_qMwF7I-yXck5vrNTFoLbhwFptIN2AnZHbJUGpEl8TSe9Nyety0 "SHOW_ELEMENT_DESCRIPTIONS() Sample")

### SHOW_FOOT_BOXES(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Sequence.puml

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

![SHOW_FOOT_BOXES() Sample](https://www.plantuml.com/plantuml/png/LL4xJyCm4DxpAuuoD9LA0eW59afLO01QaHJO8YS-g2M_i2z42F7VEKDvUJdf_3tjqqWYK6zqjgDiftk9i27oyQGiWnYA9qMRlkqZXivPGaj5vqpfjR29inT9QjMMywEzLLgjhw_AbyFYkDZdLLFXSu-smy8d-QowNDutvyjbtPmj7nPLFico5OReR2waKNOAercQAb8GvC9eabMlaT0qPwwtKeJNl3kOmhWInciSJpBWC-TGGbaC-O1j8xndbNjiOUQzLfqWvUo8L_FTASogLN6pg9aI40wB0xY-cwUxcTPkY90gHY07tCyBXfXUas8dg0T5X0586TJi5JdP69G50N7R4AGIJq4O-8xQBApC9x0Hdv8j9dd97EuZ9BX7W3Tup_wZjtLp-lBZQ5jdzijkKNy_qs_JTUGmF2_hUbKnAe5-RdzbBf0une1fF0Pd_b9EqKh-dGy= "SHOW_FOOT_BOXES() Sample")

### SHOW_INDEX(?show)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Sequence.puml

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

![SHOW_INDEX() Sample](https://www.plantuml.com/plantuml/png/LL79JiCm4BtdAuPoQ2gr2I0kSAAK2f1OAbAMM-J4Ksh96_Q4227-dJ6qBBwCD7whVH991EgCpdQKRNKd4TP4FXwNPH1zyQnetJLTnD0wIsYfQ9qflHOsSIQHf5PDEJkSBDBg_lggV3qeZeezNjKLldHeMonyai-gYzl7-lBcRFwKZx9iWI4wcmjfb1t3O9gcYXG4kJ0OPTLR93JrgUki5E4jR_V7CAo4yHg7empup3YFK1P3tcDJ2-zPvH4Rc7glLIj8EJlWrMnt3DDgKTpCbqm920V5Fbm_pDBTL6lNHqZj8f03hkO5GqodIR4JB7j5X0586TJi5JdP49G50N5J3gGIpq4Os4QjvrRc8rYBBya6axna3lSH4jmAu1q-il_eJTsSllqusiQP_R8xrDjd-crw7paCpulbSb4nAe5-Rdzbpf4uHezfh88pVoadQ2L_p2S= "SHOW_INDEX() Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Component.puml
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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Component.puml

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

![Sample with PlantUML elements](https://www.plantuml.com/plantuml/png/NP3DRi8m48JlUOebgbIG86chNbe9YGIYzc1In8yuHdPi86fYM_O6ojlNBXG1D-_kDxEp7bca1jkc3ZfPdgGaAn92YXb9ycMHaMoQvSi53E4vw5Ioh5ikO8UexNiS6tg8jXNkMjPQOKebKKYCIjN4kgRIMmuiyhfYyVXrCFEjrPJ4-vVeBNfohMAi6gsarsY_FhZKNUUX-n2EbJv2-TyDUxU8t5JRFyW_hh0-F31gnM97jHY6cfRVT2jkn1FMvInnsaaAYPiy0grH64cnsWkmHudq1pRAmBMY1mTtwuqtfqXz6LxbuYmz6QTtGIwmIp8NTR4wNtbtI6i41tPqb8V86Jh5dGlABMoCQixZ-MNibwvDXS82AhzYyVcrBaZsaUMJRYyO2SdT7_y2)

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
| package          | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| stack            | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| storage          | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| usecase          | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
| usecase/         | &#x2611; | requires ENABLE_ALL_PLANT_ELEMENTS                                                                                    |
|                  |          |                                                                                                                       |
| actor/           | &#x274C; | requires ENABLE_ALL_PLANT_ELEMENTS, not working (font color not changed to $bkColor) - and/or conflict with existing? |
| label            | &#x274C; | requires ENABLE_ALL_PLANT_ELEMENTS, not working (font color not changed to $bkColor)                                  |

If `ENABLE_ALL_PLANT_ELEMENTS` is not set, the diagrams displays the requested "PlantUML element"
but the style is not correct.
