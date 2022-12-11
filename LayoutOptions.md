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
- samples
  - [📄 Core Diagrams](samples/C4CoreDiagrams.md#c4-model-diagrams)

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![LAYOUT_TOP_DOWN Sample](https://www.plantuml.com/plantuml/png/JL1BJyCm3BxtLvXnM2TjBPlWmccb83ZiKR6EYLELjXwBb2PHub9DYF-EAyP65CcIluS_U-v9E6eR5Ln9NQcsHZWGMNyVnqvqqOUaGrks7brbDA6cg39DR9NGlMRYgLQoZDFRITQtjij5_3cBxg8RRXKfAuJKw2BR-mVn45Q6G2FMM4E9bM1Ve8Fqm9yE23NkHQi8Xd6mIDxNsxp8rrdnkDwjmb4GPEYyqQ6e6wd7C4ZwAZqvGSODHi7cw0cRui6qkXRk65RJCGmteh4AXoFu2e3VELBOOLa8QzbdXoKarYfP2P963xYLNeyXsMJHwYbdYKEOHLDOlgKzbYXbEW_zIJYq0Rw75KnfEBZaMP1taWWTa6nGyIpFsRvFwKBw1TddH6CmU4NrjzKbrjQpakjBdcSRPlMaCtgnUKRY61tsPUzCyryoHrtpvNy0 "LAYOUT_TOP_DOWN Sample")

`LAYOUT_LEFT_RIGHT()` rotates the flow visualization to *from Left to Right* and directed relations like `Rel_Left()`, `Rel_Right()`, `Rel_Up()` and `Rel_Down()` are rotated too.

```plantuml
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![LAYOUT_LEFT_RIGHT Sample](https://www.plantuml.com/plantuml/png/JL1BJy904BxtLwnue2JGYj6B9sg3O0BQGD5uQhRjA9liAxjJ6sByxyv61FSooNpFsPb7xh1JCheGkf5T2soFQFrTcZhU9ny2zrtTUN2DqGWQayQer4gkWsRYiPMYJlERIH5Mk_Kg_RnERfChMbKvARZGu18R_ADLzlQyAwlL_A6iDe-BPHcFegW0vusEUQk47hD15gRmw3WQDnX5suD7KDMzwNJBtI5kfcCst79b9Gn7x2jYz4uvSGzrnQqbdrUeMMQj50r7OVI0Lldbc6NR8dcQboHnmAwJALk_v07Bf3IzP-5Epz0mEj9oegXEeg0iLlO24Hn3eK1IbgTktyTsCVw2v7Ea4HXjGFvTTQwrywIakIpBOakiG3gXPvi58DNe8OntPzH_oGnqIz_v0m== "LAYOUT_LEFT_RIGHT Sample")

`LAYOUT_LANDSCAPE()` rotates the default flow visualization to *from Left to Right* like `LAYOUT_LEFT_RIGHT()` additional **directed relations** like Rel_Left(), Rel_Right(), Rel_Up() and Rel_Down() **are not rotated** anymore.

```plantuml
@startuml LAYOUT_LANDSCAPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![LAYOUT_LANDSCAPE Sample](https://www.plantuml.com/plantuml/png/NP91RwCm48Nl_8hPxA54Ig6jTYzxAWjHUw0fYg7Ldf03RcF9s9Oz55Mh_UyxJcWQbOl5zsRUl37SUkGEnq51cVrvREgsp3O5oxDg3OmFLedeczIT6di1UqJhVwMfurFoAd4_xaOlN6Sq2er9PuRKAgw3rwN7NibTcl-uh09g7ihqxIRvcLmHQdFgu58BbrYgZQAlW-Db55N2UQDZtWzIhs2HXLDwT1oDMomZzkvH3ErlC-gUk_Uukrx1nJ7lnHB-Ha3FQKmyYLtBhIMVPx63p5ebEuxIw0MX_FiACbObctLDBKx0JN8D3qzvq3AbpEGXhEa13T2EbbF9C2gKD0lgII8A1oW7eMYMfsp_vdGn7aNocSj8ZBP2VMpr6Qlnr4ddVLrNZAf2qKdzjBaJI34c4OuNPuRpbe-XRBLWfmkAMKElqDWpKWHIc4cViJAmKhpW6Ti6jfMlUvnZjuqbTo1B2coFATjWTA05qTary61su2NnsJdmW-51s99micVtZyzjkRvRRuhmzM-5xkdN-0y= "LAYOUT_LANDSCAPE Sample")

## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype, ?details)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```plantuml
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![LAYOUT_WITH_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL1FJy8m5B_lKrGyC1BOXEZ54tCIC05St91uMhhjAKswjcdVN8Znk_iQ4Upb9U_tztNka5liMXbS2LNBhW5sG3JkFeujxwCFWOUkwXpOMYi4XL6jszX8hhncuh2HeehJsqdcLxlDElwSHNVH3QtAb1HSAB2HyVx1EdbxtXNb_gbObUl5Sh5z34T1a85rMeMyQOKQiq7Yft1eEMex60NvqI6qvOFkLCFjCQodOpRCUMia34ViAs3qpa5X3rN9ZI6VFLGiCKQAcgFGQa2hz7hCaZoBjek291ROB9gopMlgiKHAtJlc3tKCDQCh3ITAsqaKbCMANY22PIXQa9JbgDltgLs8lo3vd6W41YyW_wwwrDevKj9S5KMM4ykJpkZ5PWb8DNhmuztgzhza3ggX__m1 "LAYOUT_WITH_LEGEND Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![SHOW_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL5DJy904BtlhnZnG4cW5QCNJzPAu03OM91ZisrNsMI_iZkr8SR_xZGWi9UNpFkODzddWDnZgnKKYxTTkPpDP-jNABXsIh0RQMhLDWBsY2uy9OddNVmbSTzMRH2-jWQ5mRYsEd6Acpvc4h1HiagoXqdUZxQhPV9z7p_6TpGgCt9mQOIF7MaPouKFraIyqTACOP3sA0DwZjOFHgmu11IwVB6jQRW_HFLq3CDZj-48VXZGEqT6dQXAxXpbx4G5gNDArXobDGCQPRTZI8iyNiysPF42xkCfh3wodakLibs0_gG0Q87kSPmakbKeQHTiEeaeFA3KGj6kGDr-J-qYF9AKSv8HoTw5-h_gKciRo4cus6poWbIzwCnUOkO2gKOdUlZqLbzRsDKlHIFs1m== "SHOW_LEGEND Sample")

Legend labels and details can be defined via `\n` in `$legendTest` arguments too.

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml
!endif
' $legendText with \n defines the label and details of the legend entry ("backend container" is label, "eight sided shape" is details) 
AddElementTag("backendContainer", $fontColor=$ELEMENT_FONT_COLOR, $bgColor="#335DA5", $shape=EightSidedShape(), $legendText="backend container\neight sided shape")
' $legendText without \n defines only a label 
AddRelTag("async", $textColor=$ARROW_COLOR, $lineColor=$ARROW_COLOR, $lineStyle=DashedLine(), $legendText="async call")
' if no $legendText defined, $tag is automatically the label and all additional displayed properties are the details
AddRelTag("sync/async", $textColor=$ARROW_COLOR, $lineColor=$ARROW_COLOR, $lineStyle=DottedLine())

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

![SHOW_LEGEND Sample, $legendText defines legend details](https://www.plantuml.com/plantuml/png/hLHDRzj64BthLumP1n41cMgQ-590G1I9RHp8aY79QGy1X26veXPPxXAxIyL4aV-U6PAIPSj1BxqGt8-PUU_Dc_tWF5fV5Qht1bAZzy9wa1w-Ixy3p3BffT6ewAWeK6UWf1Q0DgyAeJrSJPVnRBo--H9lRkQJsVqq7WNHC8e2y0Og9q2P59MgUnTo2w_tQ2KcIcp4WtJUzOFdmK7O0xYGEbLL9k1rBlpc6BD7LOcNGeQJzvk9qHu9cOrAPd8Xb1EdgNRUb-wFuT3YzoWdPbL2u2pHzSGY8cx3Kg5c5QwSpvHCAEdL7M_Ttyw6-z-Zw-Yt5-leJ6v9k4ibSlfVYuTEkQyQCh6bcmxyZcJ0H2XW_J912PG3isqFcZWW5BQ6Vf1W-etNwQ5E0DArqGC8XCnt7fpCH0PkXwLeJhkC8VJ6MHOhmOrPOtvCTiGS3E1oIuk9KSQEBkDPV1lFrvi_5_IPB6QB9PqdUNiQl7htxdewlkQOfjGevk8hhhtYTJySdB8UdKF_gi_nXYzePIf_AfVHgWRi56DAIw4QEkXgdJ8UJv4TX_5okVZx29wz-Sk3bQ-L64tHxKGse_KPWIO_i5qRc6HORPw0RH5cZ01pLXuhRmhqih7uipxJrkduPDAHmseIehIcf1cJH1MjQAAw3fwIPIp3_uUnyVx0EEprLhNpejXyD9NEqDRzz2qPwuRcm6hXuIFgRrBdGGZ_qlW07BtJBqmYQGgnBEd-RRE0SLaIkc3oQW3_O463gdbvPysUMkwuYRAGdfjV9OwoTvu_LalQQh2jTDhg97tDBqTQEL9MM0TxYHmZBRG0IAkzJ4NpK9p2wzn7-2H16D_TC3X5dU6yZEepxd40KqFNB9oEn2FU_y35K2XnqFRVZSxdA-pzEEWRF_X-bsRZcYsMZQvjBHRYe3Eqjnd5oXlBcf5jEfbIsZX2eK1ZYuODOC8ZSzHe09Ycr4vFVzwYTjY0ffNmQKIWUcIg9_rxAjQz4uuHD6uRmEVLOZxyj5xVhHwPjaOCET5cpbETc6UIdt4zP7qqCfc4tj9dcKzypkRyH1QUnN_5ysa_x7sWxFJA_WG= "SHOW_LEGEND Sample, $legendText defines legend details")

Legend details can be deactivated via `SHOW_LEGEND($details=None())`

```plantuml
@startuml
' convert it with additional command line argument -DRELATIVE_INCLUDE="./.." to use locally
!if %variable_exists("RELATIVE_INCLUDE")
  !include %get_variable_value("RELATIVE_INCLUDE")/C4_Container.puml
!else
  !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml
!endif
' $legendText with \n defines the label and details of the legend entry ("backend container" is label, "eight sided shape" is details) 
AddElementTag("backendContainer", $fontColor=$ELEMENT_FONT_COLOR, $bgColor="#335DA5", $shape=EightSidedShape(), $legendText="backend container\neight sided shape")
' $legendText without \n defines only a label 
AddRelTag("async", $textColor=$ARROW_COLOR, $lineColor=$ARROW_COLOR, $lineStyle=DashedLine(), $legendText="async call")
' if no $legendText defined, $tag is automatically the label and all additional displayed properties are the details
AddRelTag("sync/async", $textColor=$ARROW_COLOR, $lineColor=$ARROW_COLOR, $lineStyle=DottedLine())

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

![SHOW_LEGEND Sample, hide details with $details=None()](https://www.plantuml.com/plantuml/png/hLHDR-984BtpAofEHWiICVELoqf8mu1t9X612CZE7YAXijsOrhIxhUus4skq_tsgR4D8o6elSx7S7rNrtgjN_SbvjBxCLUSFI8pU2Uj1UlWX_HOmJQMNHgEYepn7dOAIMW3QhCo5zd0vMKJJqUhwxsXzFHjFxoVHC0W7OHY0Dr0w0Seag5JLEPCRUBD3Ap5MOYqUfVEk6xmC3deTW3Ef4rMc0jvamgyFCJjKfNWjP33-k1uRxP6GsR1W9cT2EN6SQkjzuVuS32p-23DYLiO4pX9TJon2uZOe56fMuTBvLCcOabxUyTRzxNImUnzUXMzVhQDJkI7XBfJ8w7yb7blb7ZIaOaCt7VWjoO2nKC3wfO8IA0TcqnpKSK0eR0NT8CRaEw-JVPq0f6kY-n08cMqzE9cA5DmM2r6VjXbxq1cbQQG4DsQ5sI7P0NFGXuiDBSP66JkyYARHRJHRhV-QqsSydyuNT1vdpMbm_k73rMHqnJ5rgM74nPTSUydhRgz_p7fu2lr1d-BjlQALAVsnN4Qh2h1LZ2ajXAhfeAjqmdWyHROSHel5_Di1F7lpFm-Mlb9YE46t5UcKrYS4wlp0TgrXac6rUGQsGPWo0inOUIozoT7Bsk8l-anRn-EJIaSEgqY8mfg2PamILRIYZcexU4oMiGn-3sFZ_PvnhzDPLiwBVFtPb3f5MtMJTsIiQve3guM7pwY_Ivq5FVX9umDmy4utDx6aASIYeFktzG96HK7eWl5v7_x1d0PLy_BEcXsrt74JPIuzDx-C7MLlFN-e5ZVLO5FgfD59-efVZgHqfAom3dOIEKPQQ02GLZkPYFgXE8RNke_mIO8mkhjcS8ewmtaPrGtki0yJGzSi78_44zx_mSLGA77GzDyDJ-Uhr_bths_qwBjjchMhjrWskhQnc8kzpj3SPXHBRonhHhPfPKfeum250etDQpQ0CO_CGQC-O99GEptzUOlQOGsQLi8d8O7gaAcUzU-vMFTEE4PGkwqFDylvRF1rjRfRFZ5jZDZZHEiPJtLiNaX-mdMVzSd8P19wIrzaFl8vc_ChMNWQVObca-v5EnN3cMci-ucAqQFx2m== "SHOW_LEGEND Sample, hide details with $details=None()")

## SHOW_FLOATING_LEGEND(?alias, ?hideStereotype, ?details) and LEGEND()

`LAYOUT_WITH_LEGEND()` and SHOW_LEGEND(?hideStereotype)` adds the legend at the bottom right of the picture like below and additional whitespace is created.

```plantuml
@startuml Layout With Whitespace Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![Layout With Whitespace Sample](https://www.plantuml.com/plantuml/png/LP11JyCm38Nl-HMXfqvYAK9muRJHLd0eCBL2FLPfOj5AQHer3h1_ZyEaRZl5_loUy-ITHxbWc0olv74EoDiH1zuE8u9tKW5lvEGCi9lHAXCqy07H-QSiM-IF-29jw8E7HSqMmQ9GyvGv8stSkFMepTXd-SFs4D7dMvLztuj7SKUeoyaXHmkBSAHbx02BdsqgRtboAla-sR1LbVOqM3l-d52Be0PBekRe4QPK4JgLFB-owYjhSMbTSLV-OWeqeLVmixgyLBCQJ5V7Z36DaiPueX4MCLyCGCSuCmBwcjKnJFmcE2tn7xFczQFjglAbV2_I3Tk1rNIGFm== "Layout With Whitespace Sample")

Therefore a floating legend can be added via SHOW_FLOATING_LEGEND(), positioned with Lay_Distance() and existing whitespace is reused like below.

- `SHOW_FLOATING_LEGEND(?alias, ?hideStereotype): shows the legend in the drawing area
- `LEGEND()`: is the default alias of the created floating legend and can be used in Lay_Distance() call

```plantuml
@startuml Compact Legend Layout Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![Compact Legend Layout Sample](https://www.plantuml.com/plantuml/png/RP5VIyCm5CNVyodI8jY2QrNqHH0srpg5kerDyJ5aQRO5ihGaj_xvzjwiMxU2Bqtok-USUzCC7N0BpKwJG1cXcrBIBK3j7jBKykzaes3Rh1edhQWCI0E9g7PfhRdnde63KgjLEhuRp3twU2lIhzlaFhb6nCReuCf8czG-dv2vjAuo4R-YORkbep0cdInQOQ4xqQSGZo35rg1e-Uj0xYA1gDtISSzQzgpPkRN3BF-1I685ruIUrFcvcYoaPWi_evz6SAqTKWypFvyV0F_6YI4e-spXX_5jchhaiCSaM3T6WC8R5_aadsPHJ08heR66XcjTSL1cmxJSI5E69C3lKK-MBxDFzbpCHk-lqmaxk8yXCIduByiKlg4HiiFxzZVObbpIuAAbz966RGF6hUGXblwDFiXZhFUo3_mOFSGWVDG_ "Compact Legend Layout Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH Sample](https://www.plantuml.com/plantuml/png/NL1FJy8m5B_tKppnm4XW4w8NJyo5I2BeueR6qrAsAaswjcdVN8Znk_iQ48ozlEJz_hxEFNA7NQjWbRuzRSegBQhYOL5cIoXuQvLW5rBNgci4x12jlqqIn_luG-AkstPUkDfe51hZshI9LLm7hud7HibjabrFyh3Qh5V9voo-YQzeLMMau58B5rlYClO_E1enbWldZOvuqqezXa4QflJeE1et6B5Yxr6qrPtfTCFTFggdOnWU-Wv7yCM0tYacwiMsujQIpwlOGcgjaZL7QVI0Ljdb6D8YZnyN9KcSW5ayXVLB5h1KATDx26TwG0Dqe-L4QJk5ahAWx2MYS82o5OgoF7NxFhQBy02Ipv5687iMwlUgSwsD9oNDPLdc1R42wOIURUu5KerUXF7kJFjNCXUw2R_v0m== "LAYOUT_AS_SKETCH Sample")

Additional styles and the footer text can be changed with SET_SKETCH_STYLE():

- `SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)`:
  Enables the modification of differnt sketch styles and footer.

The possible font name(s) depend on the output format (e.g. PNG uses fonts which are installed on the server and SVG fonts have to be installed on the client).
Additional is it possible to define comma separated fall back fonts (if the diagrams are exported as SVG. Atm
PNG does not support fallback fonts based on a PlantUML [bug](https://forum.plantuml.net/14842/specify-fall-back-fonts-is-not-working), but this could be fixed in one of the following versions)

```plantuml
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![LAYOUT_AS_SKETCH with custom style png Sample](https://www.plantuml.com/plantuml/png/VLFRQjj047ttLqpLG1HGv2IqBmL3N64IQEAQhfAG9x6Inl7MUn6xexYczDyx6ryBRVMoqioPSyxiZAu3IK-zqODtoZQwRn4MH5tuD1nwkSfV52twkW_e6sS9BUMDCyDEInjhpWErMjN3uiFvB8OUxk-6hrVvn_o2GrN15L9Pz7aN-GTYKbRYowGiRYjHFjzDqfFwfN3Q-L6YrSk2QjrZai79dEksyLre9RrLTeTkfLzwR3TOH-YVDkbH8fP8pUAGAF47ZPB2eoHiOUuyj2eqVGZAsUHiC3Y5sVG6LjmaH5NuhatL6ACkBo2bTQSQgVKQf7MqGB-1g01y7UtPNzg9-QaqE4eEF1iLyRXJOS9QDiithW3t0cwOMpLPuOngG4WRWnaSFlbz8VMoTjAt82Qxr1HxpA3fVL2l_18OUSvJKlDZur7IzGJ9NeVji9l_EF-NeoD3V_evihDpSp0JkxyRFtzzAAkns6gc79kX3ywciZNAPf2Cuwa2UKdESurO1q9JVNQzvLclq-OoWrCXJQVnz0n-3e2V_NQbAwmhsNNCyuGrZBjES_iK9yoXudq6Op7BfvEIIpp2LNu9zuz5p8srTgktSVe0v81NkvCCCRqcnLfGyWNo5W4fWvgr0dlxjNMNqYR9F5jORFORwbrN1riFWIlvl2tBcM1K1Esp1veRv8sW5SPZxfqvBhb6s_9Fz1i= "LAYOUT_AS_SKETCH with custom style png Sample")

SVG with fallback fonts MS Gothic,Comic Sans MS,Comic Sans,Chalkboard SE,Comic Neue,cursive,sans-serif

![LAYOUT_AS_SKETCH with custom style svg Sample](https://www.plantuml.com/plantuml/svg/VLFRQjj047ttLqpLW1LGv2IqBmL3N64SgEsQIad8arX9utZhlOZTKLnJ-k-TZQ-bj7fPQURCEMTsHdUUXADEgzuxQMhLDGWhejP_6WoSsAGlabPTrNbqjJM4XjBQwa6hX0arLvuQ9Qj1zk5g4K8Fi-dWzJRzc5vpgCouGaY3Bcq3VoyV5sN-PLnazsLUF4_7yKNrabbbtJ1IycL5bUemIk1YoNNx-26q4Sv8Sq0tmgqTDZki9NHFk_GmojT8zUgKAF073QFCeI1iO6aTDDBNdVVIckYor-l3OZw13JS9GHM-ArtMMikRQuXfsyfQABK5OIojqEqWqWDVHtF9jNyt511peN4OdPXsEldZGOSfAr6ltzWyp7AOCBkiayngMKCkJ0WcSFhazvLGwyeArx3c8JN73XEeE-VbAxzuHbxndEJot7gGj1r1TDHXE__p_Iy_PtR-T7Dcvk3bP2NqFXqzVtqeob6-rumvja3dhOb5ewL981g5KtfoWgmB1hUUK9UVRMTurjkulacWdmlTAknVmiyUy7FShdY3LIdQbdcUi89HsofkdiA4EPIzJs2KBzBvkE0IXt2Rti3iCGkvaL9sypPEvu4iy6gtWY6wKoHP2mg-FjuY8AbHiPPdRx_sxcBQ9Pbd3mlDVaDrwEfawy5p9P_tHR786HL0n-o9PeAy3xJ1S2oTrUSbTsWQ_eb-0m== "LAYOUT_AS_SKETCH with custom style svg Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![HIDE_STEREOTYPE Sample](https://www.plantuml.com/plantuml/png/JL1BIyD04BxdLwprq1JQn1QzU6gimGfMGvCgdi8c6Ut2ljYT68hutvt5QjtBm7pFsQL7xh1NCZeJkfLz1soFQFrrcZe-9Ey2zttJUt2jqGWQazQer4gkWsRciPEYILUNioAiTfk7z6EHN2KNjAfNfE12Wqjiy8_MzxTvNLRvDd-gNeiydaHH0SuR7VDE2JrbeonCuT5nD6uqYSg3Hr3rZUbrnzqXRkTJDYwviXB64_OPCNf_AV40JSsj9PyNQ5XchHGjHs7qY5QhyodBoY9vp2kIE62BPCuspwk0PLAQmRDmfMTe69reEL5KBr5G5gi6WGYEeL0WASjJjwzZknX_GF8vqWYCjY1_hphLsdbIqbnNLL4IAv3-q9FD7I3L622CDsVKVyaIT4UV-Gq= "HIDE_STEREOTYPE Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

![Predefined sprites Sample](https://www.plantuml.com/plantuml/png/XOxD2i8m48JlVOhOau9DfEZ5Kt-k2WNfMMApsa2QXcHZNz-jA0eUFEqmp7upHK3fCGw6EGyAhjg2Oi5vZH3OIGxEGBBGjZDH0UiHNTWBuUN4RnhxU8a1V3TQ18ky6mVXZBGpBGkeZBw8UfirizKU3-AUyntVa7MkwKDIa-UEiadIW0-ZNSwmSitIbYuhKr8JbVmEO-wPdmCljVf6L6z4zHUHVnWvGGgmYWOz00== "Predefined sprites Sample")

### Using HIDE_PERSON_SPRITE()

```plantuml
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![HIDE_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL3DJy8m5B_thwXuO2Im2T6B9-OaGYAuiA77fTkgDEbNsZSNOlpVVGq89lRoalVxV9rxO0uw9UbozRYeyiMsUDbKHRvTbGjQC6Kb9rT2Dx9hETq3M7-V98xryOU0VLTtdhl6QE0QuiQen4gcWzl4Goj5dMItapoiTkldv7CMtyKtkAeoL32XkOijSWdv7nsD2CcvyqP7h5L2Z-aW3LDuS0oC6un8SV30LVLWEjqoTuYQwPWEZus78_f5ABvpKDJpkcBMeiyRhsbghHGD0s7q05VPzPYcHHvl5YLA7AUpU4hNhrd0KYbDxsaur5Cm5A-q32cgao0mYvQz0E2EWb1SOfR7Rj-dTX4SGVGvqH0aMov_hxhKsdbKuboMPLuWAv3EwCNcYGFMw7aOxywelv8vrstupny= "HIDE_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE()

```plantuml
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![SHOW_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL5DIyD04BtlhnZheIcqYHQzU6eiHGLjGnFjCMoIgLtOx2wx4uE8_zs9rWzmMHYOz-RDUxkBGD9Jrsh8RpUxCbjjyyswpBFjNR62NBPEepXHfjPTWt0WSk4gIRpiusT5Xwxg0lhQ6a93SMtRn6bf1hLPe4QhAbbUpBAXzVXmdxpCuyluZ5lbaYUaCkXZnrmXaZ6iBO51RB212cl9ka075O0l7H0QtCjE4_Iy5OBpYX163dsmPWJZHFmt7qs4o3u9aMnQPQOmIeUg0db9reyc8dyDX6rvRJlJIFyQrUTJ67zb7a_WJG2V7wjHZrKfdMET7LQGEgTLBKcn0MujJwUGvbcyNXKyuX7cyJayF2q7BDNQzW66f-8m5lYTd6HAou4KxuA2Kn5w8DMYvbs1lRqVtKNq1RBEaSQWsAB-JlLhwp7m9DVReiXoPWsa7_HNvWQ9RVGubBstxT-H1Pfc-94F "SHOW_PERSON_SPRITE Sample")

### Using SHOW_PERSON_SPRITE(sprite)

```plantuml
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml
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

![SHOW_PERSON_SPRITE(sprite) Sample](https://www.plantuml.com/plantuml/png/ZL3BJiCm4BpdAqmvD9NQ62guSA945KNY4JK1Zf6RBDIINx8tH1NYtrdJ5-A4BollpCxCxdL0uR7JAZcHfb5T2soDwC8LvrxqsRl4TRVg0lZ66WI3MMCrTqgOE3C9s2gvuld5f8YjvuTx_Z7DBhCpQjKvJGXfm6VkHx-5D_en6qH1_t_Ov5w4DRHQcfRlzIVMWGdGT5xYHlXcBH4Qx3nC9v9c0zSY8FZZDZixdbkjhTb5-Gi-apCNIctXf5mylTR5V5a-FTPbiRohvkc0g7KCMBzx05CVh0UZ92d01sjI4QEEsM0Mgmpe1LfFUBcXIBg-iPrfXT-apVcO3KkXdOBXY7qcZDxXM6aFgreuHpgli68pvvHi14fh1jJAJyTiLXRPuxoY4GzicfspXvSyOZEbR1zO31aOMaOdT88ekbCeoOjLlKIw3KEfGP5Ne6nVktGfRa7IsT7YOajG-wsEiUXO8VejggeeYHL91_GeSmj8CNg8vSrR_Nla6anBb_u6 "SHOW_PERSON_SPRITE(sprite)")

### Using SHOW_PERSON_PORTRAIT()

```plantuml
@startuml SHOW_PERSON_PORTRAIT() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![SHOW_PERSON_PORTRAIT() Sample](https://www.plantuml.com/plantuml/png/RL5DJyCm3BttLvY1j4uQBKnmGKAYJ0YGW5LhWMELjcQBb2PHub9DYF-EG_awa4ETsi_l-JaNdeIZlbDGtAoUg_ngNQmUgdorBjVPRHdFe12TLHZjITselaNO4bb_bgPE3Cb6qhQlUu-kCPfGKzAOBhLAwC1uwAbLiawN9uTvI3tUtwMlY-GqEU9KjUGE8JMwn38sYlwNZw8SdJSw5cqdzHmcMOZIanDat6GM5JjFs5MNfjUjSBkuEPx3T9nvEeEt2FZyICK3rfMmbdcUiORCMYKRGTBe2QUM-tF8YZnvk2gvnI4iacEuVrg6MgQK6Jm4gnx80FkqWY5ThqYo5fI3948793jKhELvjlUlwM8QYypp1UDYD0Nv0WBifp-GFd3MtDa2OxPSyTP9Gg0jwl01Xmq9lM4n9NQcfz330xKWDkpkUr4Z7qkD_oFPICL63iRR-MI4BS8WQrJVw_tTpwDd2nnloZ8l61L0FzLVFzT8l8y1GtXnfllRSe6wvQVz00== "SHOW_PERSON_PORTRAIT()")

### Using SHOW_PERSON_OUTLINE()

> This call requires PlantUML version >= v1.2021.4!

```plantuml
@startuml SHOW_PERSON_OUTLINE() Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.5.0/C4_Container.puml

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

![SHOW_PERSON_OUTLINE() Sample](https://www.plantuml.com/plantuml/png/RL5DJyCm3BttLvY1j4uQBKnmGK9YJ1CWmLRH3evLsfejKff4YKir8Vux3kNhG0vrQZ-_v-TSUHAEkbP1Vhj-BhFbOxvUbUjDSN-tMiOJo4Lh5KO7KjUgQn1sHDPVfAaJVRALjEkgpgEhZIRKbDIcJQqIEX0UUsgKhDB5sN4MKfk7-_Hrbfmd9vmg5zmXf4QNMCP6qR_gKPIXyqR7eccbdi9e7gBqv0GPDvf4-TuJjkMrwNGZt3wkJwSm7aOUJ-0j0Zu_Id6FLIciPPvdh61khPAr86dqY5EBmodCyonPBGjkSGYpv1GUdXQXDbVAz1w2KmzaW6rQmP2sKoHP2ufU4g43aYqgrl8ys_lNT34DHURvWd4n6eDy0G7sqnz87pWhxco0CJkkUEia8T0ETVY0mvg4thAO4dlJKUZXWHeGMtRtlQY1ZwM6_u5ie68ZHyFjSZJ0Pc6GHrJVw_tTpyQp1OwtHP7bZ0gWd-gldniataUF8Rmuq_vjkKBTX9Vz00== "SHOW_PERSON_OUTLINE()")
