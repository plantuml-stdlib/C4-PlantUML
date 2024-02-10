# Themes

![Theme sample](https://www.plantuml.com/plantuml/png/hLPRRzis57xNhpXrEzG657jRquSD2537rjOKTknPJhk70GP57Tj4AL8ZAJl6iF--Gzri9Tq5MFFWY8Syt_dEbNnd7JEko6JmmkqnGvXSRmeb7AQmDJg3lNEv_N4qCkmut0ctBvB2ek5QELHko7KsoYLJ7k3AkbIAP3IvlbfwqSDyDZfyF_nX-EseHBR12w6uB5ByEg14T48QJ2Wqmznx4CJl5vysosWLB-utYuVrxEu-wW-2rx1cEmkso7Dj72WDDcSSBGW5n0mK8xVx2RFaiwv4XKhHIA64se5rQ52xKuusXEDUy3saMhrsBM2DnjGfqmO7Go2BTzjMR10C_bwWzJ6jJKhSeKh3-ZyuV7Hmf41KIh1d5fo61275BVcN1kCqZIG5KJdofTzB6FzCYgt_lH1URManqLARcrVHB9f7z-lDJmlwcIncYnNj9xjgj_VopPktq_5RhsFtBCURIEpsBXOffh5VzmUqKp5R4x6RnXhmnjnl2hqAMA_J6tXsAvGbCsPFYdjexrDDPxnQKLuQ7XHM_DkDs9qataoPtMCwetL_q47tuAElOq8xTpOHEE4arNxZ8AI2xGpBOAiDt55P6eKERfdwx2iYFb4kio1Oeh5QzNbXdSxGX31fltfZQCIWjsNE4z8EgopdfIAJfGmOvxfGpb8WWmfwSqk2b9bJdtz7M4y9z0RmHm3qr_Bj7p7Pi3odmvymWN6UIy6P4rfHd7eVs8654EV6avz_d7ZP5AKu48sI6iq09pZK3KYLd9RYrcxIEBuS4yckPQfOWejfM-BLaktGMs-injo8t8KmLhj2Cb-clQNH1oeRQWmflsnbMoZkgJCftCdt0I_AG5eu2EPLX07o5nAZZpGsdZ7AT28ark6Obuk6q-Hb2B-oZ54akbn0YgmSUhP8B76fS_PVkDbdv2e2rBi7mV4flMdIJvbZVjpuDDIVdatyommwQqVZn88VZJH1Ti8wKwQKXWYLPLP-XtvMKAy0AwYkkC6K4YYOf555PONMWjGxMg3ZmsU1glkQ8YLynIxllbmuKqt735mEctFa_YL2FYW4N7Oh3U6RvvDh4FpPbdtqwFgOCI4tjXIGeUXgJkkwvRpbDQL5b4QfV-Q26strra7qoFTCKVLLcWHxWLbpEwCIfjeQF_UxFNqHTb-UTHLm4hJ-NGGVMA8BTow1i6tb42XNoh8o4kVm1pJ7BiR5kMaVB5fl-_rwlOpfOFTSrMB_VAPJzENHojpcte_gH5-CY0gk6G0rKYdi5aHZi9ot8NoWMtLK6M-pMOtY2k6ImVy1sjoIyfdskLcwe2jagQtUA7vU7GsrhxyrlQ7QplHsqaJ1Orv4wqcHnGHh0Q-yjCGu4tbIZrqENRt2-jdSce_dwsKDr3hJKNzMbKsSphSSJIjwy3o9rSKbEAZVFBFev-X-Ic-ThTRENr_qibBLNTCyc-0mX6zymgaY-uCoPXUFAhyxkVxOR0VlY2KzgVu2 "Theme sample")

- [📄 C4-PlantUML](README.md#c4-plantuml)
- [📄 Layout Options](LayoutOptions.md#layout-options)
- [📄 Themes](#themes)
  - [Use theme](#use-theme)
  - [List of available C4-themes](#list-of-available-c4-themes)
    - [C4_blue](#c4_blue)
    - [C4_brown](#c4_brown)
    - [C4_green](#c4_green)
    - [C4_sandstone](#c4_sandstone)
    - [C4_superhero](#c4_superhero)
    - [C4_united](#c4_united)
    - [C4_violet](#c4_violet)
  - [Matt Weagle themes](#matt-weagle-themes)
  - [Write custom themes](#write-custom-themes)
    - [Following variables could be set in a theme, additional to the skinparams and styles](#following-variables-could-be-set-in-a-theme-additional-to-the-skinparams-and-styles)
    - [(C4 styled) Sequence diagram and themes](#c4-styled-sequence-diagram-and-themes)
- samples
  - [📄 C4 Model Diagrams](samples/C4CoreDiagrams.md#c4-model-diagrams)

## Use theme

Similar to PlantUML themes supports C4-PlantUML `C4_...` specific themes too (sometimes based on existing PlantUML themes).

Additional to the standard themes with skinparam and style definitions requires C4-PlantUML corresponding variable definitions.
Therefore we started with the convention that all C4-PlantUML compatible themes start with `C4_...` in the name
(e.g. theme [`C4_united`](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes/puml-theme-C4_united.puml)
bases on the [`united`](https://raw.githubusercontent.com/plantuml/plantuml/master/themes/puml-theme-united.puml) theme
and contains all additional required C4-PlantUML settings that it can be directly used in all C4-PlantUML diagrams).

E.g. in order to invoke theme `C4_united` from a remote repository, you have to use the following directive:

```plantuml
!theme C4_united from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes
```

In order to invoke a local theme `C4_foo`, you have to use the following directive:

```plantuml
!theme C4_foo from /path/to/themes/folder
```

Starting with PlantUML v1.2023.8 the C4 themes can be invoked via C4-Stdlib or calculated paths too:

```plantuml
' theme from C4-Stdlib
!theme C4_united from <C4/themes>

' another alternative: theme with calculated from
!RELATIVE_INCLUDE = "https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master"
!theme C4_united from %get_variable_value("RELATIVE_INCLUDE")/themes
```

Following simple sample uses the C4_united theme from the official remote repository path.

```plantuml
@startuml

!theme C4_united from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes

!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

Person(admin, "Administrator")
System_Boundary(c1, "Sample System") {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")

SHOW_FLOATING_LEGEND()
@enduml
```

![Theme sample](https://www.plantuml.com/plantuml/png/hL79JiCm4BtdAqovf599QDKBd0YX5AGk4GbmZ9nae9QyoPuGLOX_ProMyW7uCfBVCk_PLnwvmrx9A3h17IXW-RpkjK3es8ipYkqGhRzCKyU7v5NWhczw3wur6a5ZqXgLMibrS3Zps4dHfFdyh0XNZ-jL-ZPBBfBpzE3iQONGhUmx-1zNIfgJWWiDBh673WKuRtJCEoNqX8soC8L7nz6uqJWgznv1rTUcrnrt-xYT4gdaoafWNzXepDuZHkVNEHwWgRcrn7o6XcNMIj5o54QFw2e_dR2iB9BDeYA90pPBfcpzb0Siaz8CdeLcdg5XLCjoegXUeWWhgq4WWcCe54ZQvIdYntV86Bz0ylcc4HWzWFmfTuprw4b9ywwgYf9OWVIB7csMW1HZW332r_wLHENTzhc-NMspwdwph5UBvM9p4u-ZAz0TFUmd "Theme sample")

## List of available C4-themes

### C4_blue

C4_blue theme is the original theme and need no activation.

Theme [C4_blue](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes/puml-theme-C4_blue.puml) can be activated with

```plantuml
!theme C4_blue from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO-z2i9048JxF4No0BaLIQDL9DWbOA5OoYLPay3U3xTxYc_ldSzWDSF0VCEqB3f8D5HKigB1iciU8qKidy6PSXNnV0G8-gsMJTOuHiOmEIjeHKtEW2TjSxrccMaReMlgIuvkGm-llJge7VouN5IRdIZE-1-eJuqFN97bH7Icj625xudMuu9sLZvVQfDB-WK=)

### C4_brown

Theme [C4_brown](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes/puml-theme-C4_brown.puml) can be activated with

```plantuml
!theme C4_brown from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO-z2i9048JxF4No0BaLIQDL9DX5i50i9Jzh4jZREsxt3Bwz5v_1QeQ1-OQfHRkWqL9Mw8mMywPwzi6jdB-2i_ciwkK84BhLJ8lEiO-2ON2io6e6Py5Jnrk_51rfwQ6fokiMtIyjlFVcO7Rm0qjMB3nG7F4_K9yQ7xYXw8deJ6c1LHw9rkA4F1g_VQgJI_e5)


### C4_green

Theme [C4_green](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes/puml-theme-C4_green.puml) can be activated with

```plantuml
!theme C4_green from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO-z2i9048JxF4No0BaLIQDL9DWbOA5OIdxM9B2tTzpkARwz5v_1QeQ1-OQfHVkWqL9Mw88MywPwp06HysTmDbzKlHm1GlysywfB7A9W61qhifhHMV3KyzOlHITQ1sYgyh95jww5rzuSp0v-OCcAbKUA4_u7wbFZ0rSKFH6TAIsmoZtHMfoH9-EtJtLoIRy=)

### C4_sandstone

Theme [C4_sandstone](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes/puml-theme-C4_sandstone.puml) can be activated with

```plantuml
!theme C4_sandstone from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO_12i8m44Jl_Ohs0vg8zAAdIl7MWWV5ewJDsXOscv3TAFwzgT_WQOQ1USEqB2PASbXKie23iciURCYoU8Bo6Rqh5v70HwsZUQjvbIMDYI5EdWH8rEIT3cXeOzGi5jTHTqrzsQBRqElNNXtKJl_WN5GhJPWi_0SQSkEZhy1oGZnZNY3XUwRrC0DP5RPVRNPPlm==)

### C4_superhero

Theme [C4_superhero](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes/puml-theme-C4_superhero.puml) can be activated with

```plantuml
!theme C4_superhero from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO-z3e9048HxdW8UW5jZQBJ243j8B3IM1ewL8zdxoUsUnhVty1ciPZB5DpCjonWbMIegCMYnx9e7fu3HOFJbCtfR6f70Hu0uljMoYabJOepQEq4dIdiBWKQtCMgMcTO9kgQ-RD5jwE6rLmUrWn-SYsfrcjAC_u7ccVe3LsGv4PqfDpZXUwRrkA2RLTX-jTbb_G8=)

### C4_united

Theme [C4_united](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes/puml-theme-C4_united.puml) can be activated with

```plantuml
!theme C4_united from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO_12i8m44Jl_Ohs0veLwKLFbUAjWWV5ezHcRGERRSXk5F_Ur6_mDCF0l65QqI5gybHKEgF7iclkYPsYBPznyUMi6cGF48UtcPpEwP44uxYm8giP5m-11bu1jQWbzu2kgSzhT3tryDgQdTd0Zon5vNYaPF4_q90R7xYWw87eI7c1LMwPrkE4R4rOJxNPPVq2)

### C4_violet

Theme [C4_violet](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes/puml-theme-C4_violet.puml) can be activated with

```plantuml
!theme C4_violet from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/themes
```

![](https://www.plantuml.com/plantuml/png/hOzB2i9044JtESNa09aMoKPNaU0kWWl5fUJJ9WCz7wPx8jxUYMTmLKL1lQ8QbZvAibIKig15rTRFrNX2KQ_ehLf40Xy1Ol_Miv4b3OanZju9Ej6Zjn2eTnkWOfd83D3MrNMBxfSErhq-w1tyo5oKnesK9lmFDEJ61sx8SY8wKrvmmezCwt16D-cmdMgoo_e5)

## Matt Weagle themes

Matt Weagle published a set of impressive themes based on ColorBrewer and Seaborn palettes (thank you Matt).

https://github.com/mweagle/C4-PlantUML-Themes contains an overview of all his themes.

They can be simply invoked like the `cb_seq_YlOrBr_9` theme

```plantuml
@startuml
!theme cb_seq_YlOrBr_9 from https://raw.githubusercontent.com/mweagle/C4-PlantUML-Themes/main/palettes

!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.9.0/C4_Container.puml

Person(admin, "Administrator")
System_Boundary(c1, "Sample System") {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")

SHOW_FLOATING_LEGEND()
@enduml
```

![Matt theme sample - cb_div_BrBG_11](https://www.plantuml.com/plantuml/png/ZL7BJiCm4BpxAqovf5AR0E82fuPIMgJILYG5SOgSPA6M_CBU4274lxCM1Nh4bvLsPcTdrfE0mcEd5Jl27MZWJLq5UAsUrDfV-Ug2Ftkh-GxHXSiiyw9FNoJkkheBu1jh40ocZTMPxa6yACYcv-ED4WQtTyjn6GL3feKqcHCA424mTYHDexeM_Y7geX9v6mTibQmFnREti_GYFQ5MDQK9MW4-TJ47su0FrYIYrTAC-22FLGRq0gqV35dn7X1qTMKxqmh_dZIdH2g4TWhuDpOOyW_6wVqg9ptKbN2Ec8zGyzmv9Hk1qfe1jQR78vuNctGrAsd40pzBJ_dTmpHYkLAs3pmc2nmjfrXE44Lt2cLSMVQIxk8vIWsATWMo-BatcU0tI3fx6e7i7jHFk3zRsq2JL1TbkIc85Kc_w9_C791iz11B_Dd34LOire_LpNATbxUhURMSpMUhwsJ89c1QEkmN "Matt theme sample - cb_div_BrBG_11")

## Write custom themes

You can create your own theme on your local file system. You can duplicate any existing theme to create your own one.

By default, a theme file is named `puml-theme-C4_foo.puml` where `C4_foo` is the name of the theme.

In contrast to the normal themes (with skinparams and/or styles) the corresponding color,... variables have to overwritten too (e.g. that the legend is updated... details see below).

If you have any interesting theme, you can also propose a pull request so that we integrate this theme into the C4-PlantUML standard library.

### Following variables could be set in a theme, additional to the skinparams and styles

- stereotype and technology font size

```plantuml
!$STEREOTYPE_FONT_SIZE ?= 12
!$TECHN_FONT_SIZE ?= 12
```

- default text color of all elements

```plantuml
!$ELEMENT_FONT_COLOR ?= "#FFFFFF"
```

- arrow related colors and text size

```plantuml
!$ARROW_COLOR ?= "#666666"
!$ARROW_FONT_COLOR ?= $ARROW_COLOR
!$ARROW_FONT_SIZE ?= 12
```

- (default) boundary related colors and style

```plantuml
!$BOUNDARY_COLOR ?= "#444444"
!$BOUNDARY_BG_COLOR ?= "transparent"
!$BOUNDARY_BORDER_STYLE ?= "dashed"
```

- person related colors

```plantuml
!$PERSON_FONT_COLOR ?= $ELEMENT_FONT_COLOR
!$PERSON_BG_COLOR ?= "#08427B"
!$PERSON_BORDER_COLOR ?= "#073B6F"
```

- external person related colors

```plantuml
!$EXTERNAL_PERSON_FONT_COLOR ?= $ELEMENT_FONT_COLOR
!$EXTERNAL_PERSON_BG_COLOR ?= "#686868"
!$EXTERNAL_PERSON_BORDER_COLOR ?= "#8A8A8A"
```

- system related colors

```plantuml
!$SYSTEM_FONT_COLOR ?= $ELEMENT_FONT_COLOR
!$SYSTEM_BG_COLOR ?= "#1168BD"
!$SYSTEM_BORDER_COLOR ?= "#3C7FC0"
```

- external system related colors

```plantuml
!$EXTERNAL_SYSTEM_FONT_COLOR ?= $ELEMENT_FONT_COLOR
!$EXTERNAL_SYSTEM_BG_COLOR ?= "#999999"
!$EXTERNAL_SYSTEM_BORDER_COLOR ?= "#8A8A8A"
```

- system boundary related colors and style

```plantuml
!$SYSTEM_BOUNDARY_COLOR ?= $BOUNDARY_COLOR
!$SYSTEM_BOUNDARY_BG_COLOR ?= $BOUNDARY_BG_COLOR
!$SYSTEM_BOUNDARY_BORDER_STYLE ?= $BOUNDARY_BORDER_STYLE
```

- enterprise boundary related colors and style

```plantuml
!$ENTERPRISE_BOUNDARY_COLOR ?= $BOUNDARY_COLOR
!$ENTERPRISE_BOUNDARY_BG_COLOR ?= $BOUNDARY_BG_COLOR
!$ENTERPRISE_BOUNDARY_BORDER_STYLE ?= $BOUNDARY_BORDER_STYLE
```

- container related colors

```plantuml
!$CONTAINER_FONT_COLOR ?= $ELEMENT_FONT_COLOR
!$CONTAINER_BG_COLOR ?= "#438DD5"
!$CONTAINER_BORDER_COLOR ?= "#3C7FC0"
```

- external container related colors

```plantuml
!$EXTERNAL_CONTAINER_FONT_COLOR ?= $ELEMENT_FONT_COLOR
!$EXTERNAL_CONTAINER_BG_COLOR ?= "#B3B3B3"
!$EXTERNAL_CONTAINER_BORDER_COLOR ?= "#A6A6A6"
```

- container boundary related colors and style

```plantuml
!$CONTAINER_BOUNDARY_COLOR ?= $BOUNDARY_COLOR
!$CONTAINER_BOUNDARY_BG_COLOR ?= $BOUNDARY_BG_COLOR
!$CONTAINER_BOUNDARY_BORDER_STYLE ?= $BOUNDARY_BORDER_STYLE
```

- component related colors

```plantuml
!$COMPONENT_FONT_COLOR ?= "#000000"
!$COMPONENT_BG_COLOR ?= "#85BBF0"
!$COMPONENT_BORDER_COLOR ?= "#78A8D8"
```

- external component related colors

```plantuml
!$EXTERNAL_COMPONENT_FONT_COLOR ?= $COMPONENT_FONT_COLOR
!$EXTERNAL_COMPONENT_BG_COLOR ?= "#CCCCCC"
!$EXTERNAL_COMPONENT_BORDER_COLOR ?= "#BFBFBF"
```

- node related colors

```plantuml
!$NODE_FONT_COLOR ?= "#000000"
!$NODE_BG_COLOR ?= "#FFFFFF"
!$NODE_BORDER_COLOR ?= "#A2A2A2"
```

- legend colors and sizes

```plantuml
!$LEGEND_TITLE_COLOR ?= "#000000"
!$LEGEND_FONT_COLOR ?= "#FFFFFF"
!$LEGEND_BG_COLOR ?= "transparent"
!$LEGEND_BORDER_COLOR ?= "transparent"
!$LEGEND_DARK_COLOR ?= "#66622E"
!$LEGEND_LIGHT_COLOR ?= "#khaki"

!$LEGEND_DETAILS_SMALL_SIZE ?= 10
!$LEGEND_DETAILS_NORMAL_SIZE ?= 14
```

- legend related texts

```plantuml
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
' transparent is ignored, produces smaller legends
' !$LEGEND_DASHED_TRANSPARENT_BOUNDARY ?= "dashed, transparent"
!$LEGEND_DASHED_TRANSPARENT_BOUNDARY ?= "dashed"
```

- sketch related colors, font and texts

```plantuml
!$SKETCH_BG_COLOR ?= "#EEEBDC"
!$SKETCH_FONT_COLOR ?= ""
!$SKETCH_WARNING_COLOR ?= "red"

!$SKETCH_FONT_NAME ?= "Comic Sans MS"

!$SKETCH_FOOTER_WARNING ?= "Warning:"
!$SKETCH_FOOTER_TEXT ?= "Created for discussion, needs to be validated"
```

- size of rectangle shape corner markers

```plantuml
!$ROUNDED_BOX_SIZE ?= 25
!$EIGHT_SIDED_SIZE ?= 18
```

### (C4 styled) Sequence diagram and themes

All sequence diagram specific renderings (like sequence-lifeline-color...) can be directly defined via skinparams and styles.
The advantage is that no separate variable definitions are required anymore.
(But the disadvantage is that all themes have to define there own skinparams and styles.)

A theme could contain e.g. following definitions, skinparams and styles

```plantuml
' $BOUNDARY_BG_COLOR... have to be defined in theme itself that it can be used in styles,...
' (no default values which are defined in C4.puml) 
' If skinparams and styles are defined with concrete values no variables are required 
!$BOUNDARY_BG_COLOR ?= "transparent"
!$BOUNDARY_COLOR ?= "#444444"
!$ARROW_COLOR ?= "#666666"

' replace transparent with concrete background that it can be used as font color too
!if ($BOUNDARY_BG_COLOR == "transparent")
  !$SEQUENCE_BG_COLOR = white
!else
  !$SEQUENCE_BG_COLOR = $BOUNDARY_BG_COLOR
!endif

' "C4 styled" default is no foot boxes
hide footbox
' "C4 styled" default is that lifeline is arrow color
skinparam SequenceLifelineBorderColor $ARROW_COLOR

skinparam SequenceGroupBodyBackgroundColor $SEQUENCE_BG_COLOR
skinparam SequenceGroupFontColor $BOUNDARY_COLOR
skinparam SequenceGroupBackgroundColor $BOUNDARY_COLOR
skinparam SequenceGroupHeaderFontColor $SEQUENCE_BG_COLOR
skinparam SequenceGroupBorderColor $BOUNDARY_COLOR

skinparam SequenceReferenceBackgroundColor $SEQUENCE_BG_COLOR
skinparam SequenceReferenceFontColor $BOUNDARY_COLOR
skinparam SequenceReferenceHeaderBackgroundColor $BOUNDARY_COLOR
' VIA STYLE
' skinparam SequenceReferenceHeaderFontColor $SEQUENCE_BG_COLOR
<style>
referenceHeader {
  fontcolor $SEQUENCE_BG_COLOR
}
</style>
skinparam SequenceReferenceBorderColor $BOUNDARY_COLOR

skinparam SequenceDividerBackgroundColor $SEQUENCE_BG_COLOR
skinparam SequenceDividerFontColor $BOUNDARY_COLOR
skinparam SequenceDividerBorderColor $BOUNDARY_COLOR

' VIA STYLE
' skinparam SequenceDelayFontColor green
<style>
sequenceDiagram {
  delay {
    FontColor $BOUNDARY_COLOR
  }
}
</style>
```

Following sample could be used as starting point for custom themes with sequence diagram support:

[![](https://www.plantuml.com/plantuml/svg/hLPfRziu4FskNp7sfeW3D79saIwmHToj3-K0t3Yhs5tqaq5B8vieJQeavJIxw7_laF9zv5WiWSGIDM_Up9kHXX-DPTeMKn44bQE1mVu4fmWDgBRFXsEDAAj1S0o9aZFK5hY51sudmDAKMwua4_HeEcKo1S4b0jFZOehImcadZhhD_itdQ7Xps-uEEb6Z6jR3i0fMGM4GX4gO48z1XMVmPiOqPoE1G_pEZJMrwZQuUX8074F5-kWej4kkZUsZiP1fDOKtOxJ3fPSP4mNkSrBtU4E-vfvM6NitBiA5JGM5mOEM4sjpyxvUr-mX79CYnOYIqYIJfUn3qgIU2oQThgV6feAFwktpqpktDVZKhSz-2_y8prPCCkMPa_bYPy5TC-v3xnBwrz6d29pHKQitkEqquo_3rjMmtUlsuZ0COS9cwBGT8QIOKIrIu1BAsBarA3AwORw22PFEZ0BsDiO-2ZHloGavhqdbyAmG5hoC1XucFA6Awmt7xVCmf-HEW30t6PYlNEPCiwa1rmkbomsCRnlI9z5eSU6Qo1P5AwqrVYku9dDgnfqquKzgIwkPD4H5CbVNZLOMlvpxvPusuxZtz_gZt_toBQsHAfIGPYk7Mq6EMF9rh5L12UsJZXd8gDvaBvGcwPNlvTgUk1jRSRjchXpTHtyDejjsj6RdjBQuQhszDhi4Qnr4hssfVbfTrf5xeJEbB8pKTsgu2K_HtzFjOOpFMV0C_PlDNO6qUYZJ3PO5Xtig6Se4ktFBbj8fwhONPRq0mHxC5QcRjrJws5fAFGVk97u8VKabc6CsU-4WtJRLos3No2YjDRONHxWXo1RP7aoC6MftyPyqMQ9VeyiIL2Rvd4B7yFcc2VVzBzs8hfzrzwHc5xxnFWHw4mF_Klkxjoiv1FmHNDJdsASqV9ts7JxZ-mHuYV9px6jqNz0z5UHpOdTGiCSLgH_PIrNDaeYD7SYfcZg0lm8u72p0ZtM9YVh3pjgPJQ-OvHKk4r7GP-Ybavjc_Y9bFtbM7yc5f_zb9E-XAJ-jTwYDahMcu0c-XQh_fKpcsoqreatwJri1IooVCHeWT1y4COe5ghHg5ZILfUK9SoSeY1sTiHv87rvJ90aQanLqic8-GG3dmcENx9ikcWJ9BNs-Jm8d2XX5Gvyw9GMLGSQuA7JfI2YLmwzdPsTWUNaEAjTEZ9tRUsXQI--1hnO0gH2uF_UYWgAp8ApiuJsT2BZTa-e4XL0kioNAIGBGdz0ucSzI9Md383samwGR8COHqNWcqMbmtf1dpWJ_fqorqNYDeiy95wF9bJIka8uhnXmjVu97Ae9hO2_cOuSGArvtU7i7KouBIuSWGNsZmPt5TkdTWTd0Z3F89qfwS71_JVEr6rr5jvtQIV2HbAEc_Ga=)](https://www.plantuml.com/plantuml/uml/hLPfRziu4FskNp7sfeW3D79saIwmHToj3-K0t3Yhs5tqaq5B8vieJQeavJIxw7_laF9zv5WiWSGIDM_Up9kHXX-DPTeMKn44bQE1mVu4fmWDgBRFXsEDAAj1S0o9aZFK5hY51sudmDAKMwua4_HeEcKo1S4b0jFZOehImcadZhhD_itdQ7Xps-uEEb6Z6jR3i0fMGM4GX4gO48z1XMVmPiOqPoE1G_pEZJMrwZQuUX8074F5-kWej4kkZUsZiP1fDOKtOxJ3fPSP4mNkSrBtU4E-vfvM6NitBiA5JGM5mOEM4sjpyxvUr-mX79CYnOYIqYIJfUn3qgIU2oQThgV6feAFwktpqpktDVZKhSz-2_y8prPCCkMPa_bYPy5TC-v3xnBwrz6d29pHKQitkEqquo_3rjMmtUlsuZ0COS9cwBGT8QIOKIrIu1BAsBarA3AwORw22PFEZ0BsDiO-2ZHloGavhqdbyAmG5hoC1XucFA6Awmt7xVCmf-HEW30t6PYlNEPCiwa1rmkbomsCRnlI9z5eSU6Qo1P5AwqrVYku9dDgnfqquKzgIwkPD4H5CbVNZLOMlvpxvPusuxZtz_gZt_toBQsHAfIGPYk7Mq6EMF9rh5L12UsJZXd8gDvaBvGcwPNlvTgUk1jRSRjchXpTHtyDejjsj6RdjBQuQhszDhi4Qnr4hssfVbfTrf5xeJEbB8pKTsgu2K_HtzFjOOpFMV0C_PlDNO6qUYZJ3PO5Xtig6Se4ktFBbj8fwhONPRq0mHxC5QcRjrJws5fAFGVk97u8VKabc6CsU-4WtJRLos3No2YjDRONHxWXo1RP7aoC6MftyPyqMQ9VeyiIL2Rvd4B7yFcc2VVzBzs8hfzrzwHc5xxnFWHw4mF_Klkxjoiv1FmHNDJdsASqV9ts7JxZ-mHuYV9px6jqNz0z5UHpOdTGiCSLgH_PIrNDaeYD7SYfcZg0lm8u72p0ZtM9YVh3pjgPJQ-OvHKk4r7GP-Ybavjc_Y9bFtbM7yc5f_zb9E-XAJ-jTwYDahMcu0c-XQh_fKpcsoqreatwJri1IooVCHeWT1y4COe5ghHg5ZILfUK9SoSeY1sTiHv87rvJ90aQanLqic8-GG3dmcENx9ikcWJ9BNs-Jm8d2XX5Gvyw9GMLGSQuA7JfI2YLmwzdPsTWUNaEAjTEZ9tRUsXQI--1hnO0gH2uF_UYWgAp8ApiuJsT2BZTa-e4XL0kioNAIGBGdz0ucSzI9Md383samwGR8COHqNWcqMbmtf1dpWJ_fqorqNYDeiy95wF9bJIka8uhnXmjVu97Ae9hO2_cOuSGArvtU7i7KouBIuSWGNsZmPt5TkdTWTd0Z3F89qfwS71_JVEr6rr5jvtQIV2HbAEc_Ga=)
