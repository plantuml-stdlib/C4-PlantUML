# Themes (WIP), Changeable Styles

WIP: C4-PlantUML offers no finished themes (atm).
It is possible to define/use custom themes.

- [📄 C4-PlantUML](README.md#c4-plantuml)
- [📄 Layout Options](#layout-options)
- [📄 Themes (WIP), Changeable Styles](#themes-wip-changeable-styles)
  - [Overall Guidance](#overall-guidance)
  - [List of available C4-themes](#list-of-available-c4-themes)
  - [How to write custom theme](#how-to-write-custom-theme)
    - [Following variables could be set in theme definitions too](#following-variables-could-be-set-in-theme-definitions-too)
- samples
  - [📄 Core Diagrams](samples/C4CoreDiagrams.md#c4-model-diagrams)

## Overall Guidance

WIP ...

```plantuml
@startuml
!theme C4_FirstTest from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

Person_Ext(customer, "Customer", "A customer of Widgets Limited.")

Enterprise_Boundary(c0, "Widgets Limited") {
    Person(csa, "Customer Service Agent", "Deals with customer enquiries.")
    System(ecommerce, "E-commerce System", "Allows customers to buy widgts online via the widgets.com website.")
    System(fulfilment, "Fulfilment System", "Responsible for processing and shipping of customer orders.")
}

System_Ext(taxamo, "Taxamo", "Calculates local tax (for EU B2B customers) and acts as a front-end for Braintree Payments.")
System_Ext(braintree, "Braintree Payments", "Processes credit card payments on behalf of Widgets Limited.")
System_Ext(post, "Jersey Post", "Calculates worldwide shipping costs for packages.")

Rel_R(customer, csa, "Asks questions to", "Telephone")
Rel_R(customer, ecommerce, "Places orders for widgets using")
Rel(csa, ecommerce, "Looks up order information using")
Rel_R(ecommerce, fulfilment, "Sends order information to")
Rel_D(fulfilment, post, "Gets shipping charges from")
Rel_D(ecommerce, taxamo, "Delegates credit card processing to")
Rel_L(taxamo, braintree, "Uses for credit card processing")
Lay_D(customer, braintree)

SHOW_LEGEND()
@enduml
```

![Theme sample](//www.plantuml.com/plantuml/png/hL9DRnen4BtlhvXm0gc4gigffuIFfAfeY_AX797n3c35Qsyyun1KzRztZ0auDCSY3lPwtdipRzubiGeS6rkTyHeRXD75_De4udiaXcNm3QoPM_ew60IrELyPNiT590pQEqR7vzetWzOgbpZwnBKrYy7eeZzBdnv-J0UD8iOms95JTMQSjh76_qCglOvyqtgNC6qQeffX8E_carVkwaZi6moVe3FQ7pjoleAt1_1BU3Jr2fbWQXh3M9ztUbKrSOoX3OPmFlJHrIfik_gpG4-AEptuNO7yicXNaogqu0x3Yz48Lojqd9J7g2p1HgOzje3kEPfWa99ouhhR4cFJHR50tZKARj9_k-nVTsDOwpTq829W3ukuXOtqo0JUMUCGNem2iHuskVDaB6nmGORnH70PxTBO1XqB-VNXKYZU8edLP1OMOUa3jC5h939k1ShLG6lJjkdYbuN3eSQmc-rFLMMgtMvOlQh62-dzxf3eHyhgQ1KZWVLQMP0Qw2QXoGCClmoFe_PsUaepWP9_IgdZFigtL3qCoZWEY31JspH2aY-r5sy58lflSMfbbYT30XsmDWnQXHhQN96yXGMkbLr-7A1Ig_MK_FoEWN0BCxcTZBhnmTQo7JpwfwMAiiDAFwbLpaPrYtP-MuGwf-sAdWYU8n8Rxr884lyzMcpNtg7WJc5bi6PMQQIyfAoupmd4jDQCph4kOLFlHJIs6GZ62R9HgO4I9we5w5syxj3Lz06Q_HuwVXV7lOato5Iuj5P1h4dBRmweGl2Gi35QN2a-MMOHteFgz13BCY8FXDcRZ-62dQgjQ1yjFg1xalbllnxdqydDvEUuswikPV3OsBy0 "Theme sample")

## List of available C4-themes

Atm we have no finished C4-themes....

## How to write custom theme

WIP ...

The sample theme C4_FirstTest [puml-theme-C4_FirstTest.puml](themes/puml-theme-C4_FirstTest.puml)  is stored in the themes folder

### Following variables could be set in theme definitions too

``` plantuml
!$ELEMENT_FONT_COLOR ?= "#FFFFFF"
!$ARROW_COLOR ?= "#666666"
!$BOUNDARY_COLOR ?= "#444444" 
!$BOUNDARY_BG_COLOR ?= "transparent" 
!$LEGEND_FONT_COLOR ?= "#FFFFFF" 
!$LEGEND_TITLE_COLOR ?= "#000000" 
!$LEGEND_DARK_COLOR ?= "#66622E" 
!$LEGEND_LIGHT_COLOR ?= "#khaki" 
!$SKETCH_BG_COLOR ?= "#EEEBDC"  
!$SKETCH_FONT_COLOR ?= "" 
!$SKETCH_WARNING_COLOR ?= "red" 
!$SKETCH_FONT_NAME ?= "Comic Sans MS" 
!$LEGEND_SHADOW_TEXT ?= "shadow" 
!$LEGEND_NO_SHADOW_TEXT ?= "no shadow" 
!$LEGEND_NO_FONT_BG_TEXT ?= "last text and back color" 
!$LEGEND_NO_FONT_TEXT ?= "last text color" 
!$LEGEND_NO_BG_TEXT ?= "last back color" 
!$LEGEND_NO_LINE_TEXT ?= "last line color" 
!$LEGEND_ROUNDED_BOX ?= "rounded box" 
!$LEGEND_EIGHT_SIDED ?= "eight sided" 
!$LEGEND_DOTTED_LINE ?= "dotted" 
!$LEGEND_DASHED_LINE ?= "dashed" 
!$LEGEND_BOLD_LINE ?= "bold" 
!$LEGEND_BOUNDARY ?= "boundary" 
!$LEGEND_DASHED_BOUNDARY ?= "dashed" 
'$LEGEND_DASHED_TRANSPARENT_BOUNDARY ?= "dashed, transparent" 
!$LEGEND_DASHED_TRANSPARENT_BOUNDARY ?= "dashed" 
!$SKETCH_FOOTER_WARNING ?= "Warning:" 
!$SKETCH_FOOTER_TEXT ?= "Created for discussion, needs to be validated" 
!$STEREOTYPE_FONT_SIZE ?= 12 
!$TECHN_FONT_SIZE ?= 12 
!$ROUNDED_BOX_SIZE ?= 25 
!$EIGHT_SIDED_SIZE ?= 18 
!$ARROW_FONT_SIZE ?= 12 
!$LEGEND_DETAILS_SMALL_SIZE ?= 10 
!$LEGEND_DETAILS_NORMAL_SIZE ?= 14 
!$COMPONENT_FONT_COLOR ?= "#000000" 
!$COMPONENT_BG_COLOR ?= "#85BBF0" 
!$COMPONENT_BORDER_COLOR ?= "#78A8D8" 
!$EXTERNAL_COMPONENT_FONT_COLOR ?= $COMPONENT_FONT_COLOR 
!$EXTERNAL_COMPONENT_BG_COLOR ?= "#CCCCCC" 
!$EXTERNAL_COMPONENT_BORDER_COLOR ?= "#BFBFBF" 
!$CONTAINER_FONT_COLOR ?= $ELEMENT_FONT_COLOR 
!$CONTAINER_BG_COLOR ?= "#438DD5" 
!$CONTAINER_BORDER_COLOR ?= "#3C7FC0" 
!$EXTERNAL_CONTAINER_FONT_COLOR ?= $ELEMENT_FONT_COLOR 
!$EXTERNAL_CONTAINER_BG_COLOR ?= "#B3B3B3" 
!$EXTERNAL_CONTAINER_BORDER_COLOR ?= "#A6A6A6" 
!$PERSON_FONT_COLOR ?= $ELEMENT_FONT_COLOR 
!$PERSON_BG_COLOR ?= "#08427B" 
!$PERSON_BORDER_COLOR ?= "#073B6F" 
!$EXTERNAL_PERSON_FONT_COLOR ?= $ELEMENT_FONT_COLOR 
!$EXTERNAL_PERSON_BG_COLOR ?= "#686868" 
!$EXTERNAL_PERSON_BORDER_COLOR ?= "#8A8A8A" 
!$SYSTEM_FONT_COLOR ?= $ELEMENT_FONT_COLOR 
!$SYSTEM_BG_COLOR ?= "#1168BD" 
!$SYSTEM_BORDER_COLOR ?= "#3C7FC0" 
!$EXTERNAL_SYSTEM_FONT_COLOR ?= $ELEMENT_FONT_COLOR 
!$EXTERNAL_SYSTEM_BG_COLOR ?= "#999999" 
!$EXTERNAL_SYSTEM_BORDER_COLOR ?= "#8A8A8A" 
!$NODE_FONT_COLOR ?= "#000000" 
!$NODE_BG_COLOR ?= "#FFFFFF" 
!$NODE_BORDER_COLOR ?= "#A2A2A2"

```

