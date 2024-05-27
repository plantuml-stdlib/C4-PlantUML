# Themes

![Theme sample](https://www.plantuml.com/plantuml/png/hLPRZnet57wVNt52KWMaMKYQpKkbbSB2jDa85igGf0-LaCTp02iUUs9xO57L_zxZkS7ifXUfsGTsVEppdUzSxNVMCUEAJ0RFt1upXCdrfb32OGfRepFOEvVRdqOZmux3dN3x8Yai6gwLG-M6N6UZN3Bb0QwiIwL8HfFhgwKNVPpFHeSVXwzV3L-DIcWRF1EAooB5xuHAL2UameH2Cyoz3q7yVl5viunMyU9-i_YudjtTH_r1y1BMR6V15dckZGEbmUQCemMXWAY1OkHuFs6MlDQLg50f6YcKK3km3WrgTyhHXd3S2xw7LAkNhWMiqPWwPThWO0XayMxRYWs2mQy5MX_LsgJ47QeqhF-3mmS7Huf4fGHxPi5fI11It99_QJ1EqqXI59KZN_gzXF4lfDZwtmlXnPOM4osrkNaHpQ9vTB_U_BoWdybYjbZHVhAhTdlFtxnvEns_zJfsptAyYSHkxsAHOXhxTNz0EnMpDH6xQQm1Rypzhj2hWFKwlO5djq9PCcFsfBY7zZxLTCQh5UMbuK5XnR_TYDr9uisKsJscCrht1nrq3pxwFYQqSsSJWHDEKlKt3a8gsCwm3BRQm1tLfL7eu9QfBxuYuXFbCWk29HghLPyNrkaCJGYJzgitXaOCUblcF27jiCfoNYeoMSg0SQuBvIm5CgYWDxSaI9avzVbhmdfCe3U0FmAWlvPl_uZ9XkKv7VwC2OppN0hEdD2AujJxm0uiX3WtdlpyqyJBfYZ5WMYKr6WAEC6Xxa2gvBGKjtQJnl7bc4XsBLF54bnCsnAlbco7tdfZDUP6v2w4iTeLalaoxIsDFb3PK6D8-Mqhsq9nJvr9uKw-3tXH1jB2GJ2l8WoGlv0OVQIvyOHHfXCXiGx7l5mqd2RFG_YDPOmYqUK2KcJbsBD5OebBdRF_miq-8LSHeDuz28wFwKsJVieSy-F6fw7-z6pYNsVGMJiQ9nRyRAG9iXFMcJAbD4IeBBFoE_IpWde5M45rnGscb43198qgAYkq5gJUqG8T7pu9LDtN52dXAtPvz-t2cMewPk1os9mZzoyHya4XuB9RQGZVF9rSW-3FjkoZ1zV7Z0cviQM034LNSrhNBUSjhoajeZHA_JCNt6YhjmwY1xvdYgglqYJO2yoQsncLCDNM-BdVxUcBiFlohAk0aw3rxoBum19Tk7C9X6qhXq2vKfQLaJY7Fw0vTZ4kpatxqQBrjj-lrykO3dRFLItspsSwHLyUhSnjxlseJlJ5YAZWcW5G8vN2Ra4q1ijv6y87kbL7bV4sczKehX0k6VmVeCqjAPzfdvkb2xf2bjhgbUBdrT5G-_fRqnkgxKnl9qqKFEP5j1uLMKom5l3AIqkCCv57zTZbqDKhh9_DhVbulbxMGAqp7VKdLTd4wNpBqRIY5y-ZM5rSWeFwpJEBVedkf_JMsMhj_FL5JojLtJNDkmaEG_Z19vmgiZyeOtRnglAxa-jFpNRmZbZIa-el "Theme sample")

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
(e.g. theme [`C4_united`](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes/puml-theme-C4_united.puml)
bases on the [`united`](https://raw.githubusercontent.com/plantuml/plantuml/master/themes/puml-theme-united.puml) theme
and contains all additional required C4-PlantUML settings that it can be directly used in all C4-PlantUML diagrams).

E.g. in order to invoke theme `C4_united` from a remote repository, you have to use the following directive:

```plantuml
!theme C4_united from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes
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

!theme C4_united from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes

!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![Theme sample](https://www.plantuml.com/plantuml/png/hL7BJi905DttAyQwAGcqQ5ovebO44mHYYooReRtA9FFApAsDCVwxTm3H3t0sDvdpkEVCJ3noXvsIKNI1Ur30YfkwqmAXPQ_EABP7jFusonplqpU1-sxNUN2DqGWQqyQep4gkWyF8Ool5BYjkHkjmjNbQPE_NwTKu7MS7QqyxX6vary8_sLBMWYHSQ72fFRHOW_D69xnLGWzPd8SfF3gEniM3gFpm2Ag-CvrkkVj8cYiYbLnP2Uo8nGFs6J4wP-UaXrtDhINc5dOijrQAXgCmEgQhudB8ydATBgSLIHmmoiQUNeg0vLAQthDGpJCqZ7fPJXJLIHHXPTKBH70CXG99kpn5_3g5JF08ai-9Hc3q3FAdt6-iZISbpNbLhKjY1T8P_RMP0LAC7i88d_jN4fNprRP-MApowd4vgnVJsNHvdmoY2UYM7lOR "Theme sample")

## List of available C4-themes

### C4_blue

C4_blue theme is the original theme and need no activation.

Theme [C4_blue](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes/puml-theme-C4_blue.puml) can be activated with

```plantuml
!theme C4_blue from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO_12i8m44Jl_Ohq0vgjqfEdIl5MmOFYKP9sRGkRD6GtYdzlwZTucc5WtZ0jYucI71MbpEXGTSt3KaBrZAjJiqZW0q0qRpqjCYUR6EEmUa4lUbWT139-grSi8oqMkgQwRD7jtCDhhtUrhk47vg9S_41fn3zHGwvyu8eiHw8JvGalVC-u7YVqemxRgJQxh5y=)

### C4_brown

Theme [C4_brown](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes/puml-theme-C4_brown.puml) can be activated with

```plantuml
!theme C4_brown from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO-z2i9048Hxdo9vWDn6IMKL2NOHB1HBoS-Q1FRsZjizWs_lnMUmcc5Wlc5gqIvejBJBTKQBMLCz--1Mpbx1sMnMzN842DrgfaNds4V1C3XMP3M3i-2fuwrVY8wqzD1KnNMBxfSMtWUpBqq9FxBiyeK7YYF-YUfJvGCt53qHdIbDiCeZuLgSa4VZjrTrSac_)


### C4_green

Theme [C4_green](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes/puml-theme-C4_green.puml) can be activated with

```plantuml
!theme C4_green from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO-z2i9048JxFCNb0N8R9PLL9DX5i50i9Jzh4jZR7BTxYc_lnMUmcc5Wlc5gqIveT9JbEgD3qrIFAI2oUORLcLdLom4WT6yxBJh7FWg6OML5LZki3ZnrlFKBqP6M7fggk6pHxTp2QsztfItXHvOiNtYWEEAVg3vLFd15qIFHYT84gzmJhiK9URH-UrKdb_GB)

### C4_sandstone

Theme [C4_sandstone](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes/puml-theme-C4_sandstone.puml) can be activated with

```plantuml
!theme C4_sandstone from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO_12i8m44Jl_Ohs0vfKwSbJfNYhu47nA6cpjeND9cGtYdzlwZTucc5WtZ0TYucI71QLBE2WxDi76x8idg1yHk_AHIJmGUjetcfUPKbZOeYJ9m4IDNcd0nhQ63MBnNNKVLjVjkXs7lHhhtQDQlIFpaMrqeJ9mf-e8LS--WeiHyGJvWaIlcVS03EGLM5xrcMNzGi=)

### C4_superhero

Theme [C4_superhero](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes/puml-theme-C4_superhero.puml) can be activated with

```plantuml
!theme C4_superhero from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO-z3e9048HxdW8UW5iqL5OOOeU9XSRImB5o97i_kTtJ-FOUFeFLJARuPgPZ6QCaIqKb1YsMVVlW530QZBvyHczB8nBu0137jrfMCMbAZ55x9-X4QMyXqEWsHiqoqpf1tzQNBRgT1tZjrQvH3VpeN5IhqvHc_1Cr3zKVk2BBaUX4kS89tpDkm0NThCBshCikwnS=)

### C4_united

Theme [C4_united](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes/puml-theme-C4_united.puml) can be activated with

```plantuml
!theme C4_united from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes
```

![](https://www.plantuml.com/plantuml/png/hO_12i8m44Jl_Ohq0vfKwSbJfNYhu47nA6spje7DDcGtYdzlwZTucc5WtZ0jon0bUInAMS23wff78YTWrJEkNYqYWG_6nE6jPoTB6XD3d5OI8D7Jwat0WJP0nMBHZQPhgiiMtSwzUUtrhjQr-Q6vA1rDc2pyYHfovMEkm794F66U8E5xnlKm0raTjbjjTbc_)

### C4_violet

Theme [C4_violet](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes/puml-theme-C4_violet.puml) can be activated with

```plantuml
!theme C4_violet from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/themes
```

![](https://www.plantuml.com/plantuml/png/hOzB3e9044Jtd08Em3GQLgumn1qaBZGk3PyM9kdvPBe7u-qTF8EhgbHIhr8Don0a6ieAMT5WtjRFJJj2oL_1cNmLyNm22CDRBLhME4R6C3ahQ4LDpe2dmUw0acKcFK9RbzSzklSTR4Trg5G5FpHdXROJnHd_HFMfye4Rifo9BfGchF0ZuJfSqCxAxxUQv99-0G==)

## Matt Weagle themes

Matt Weagle published a set of impressive themes based on ColorBrewer and Seaborn palettes (thank you Matt).

https://github.com/mweagle/C4-PlantUML-Themes contains an overview of all his themes.

They can be simply invoked like the `cb_seq_YlOrBr_9` theme

```plantuml
@startuml
!theme cb_seq_YlOrBr_9 from https://raw.githubusercontent.com/mweagle/C4-PlantUML-Themes/main/palettes

!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.10.0/C4_Container.puml

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

![Matt theme sample - cb_div_BrBG_11](https://www.plantuml.com/plantuml/png/ZL7BJiCm4BpxAqovf19D2k82fuPI2b9fAnAeE4LEib1BVc5lY13YtraBQ7l4bvLsPcTdrfE0mcEd5Jl2BMZWJLq5UAkUrSfV-Ug2ltYh-HRHXSiiyw9FNoLkkxeBu1jh40ocZTMPxa6yAiYcvwEr4WOVxnUZCWg6J0jfCYSK849Wx4YQHdKj_4FKHINoDWhOAbaVYcVlP-dfE1rJhvhI2Eq0dxeOXAt11siIqMffJlWWZrK6z0Aj7mnPyH4GT7LbEzCA_v4qfqGgX7OA-0ys6F9Fnkdjb9CUwaeuHymDr3ntJib6eBHcGAtfyGdFYtMwd9Kque6JDtx_D8rOhfJj0u_H0aVBAPSJHD6TGXbNbhsamtYEKeEYNO4iVlsQJF0799rV6e7i0THVkBsjnq2JL6_BSbqGAv9sw5vc3aWsUeWbVktX22jkLvlgPh7Aoxlbl5hCvhFbTJ9a4p0j7VOR "Matt theme sample - cb_div_BrBG_11")

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

[![](https://www.plantuml.com/plantuml/svg/hLPjRzf84FxkNp5mgKAanj1JxZvKeLTUd0I9afn3UkedjDXZM7NPfRjhqbpL_zxPDQy14ZZTIWdsUfvvPfuPU_QZiKpRV2A2e7JoOB0_nWb27SgjYy588yfo49n2ekGCjGLkuP7RCR0qvPOhoGGzcaoOJ45mYS3qA9-Wj73UZgDkez_v70qwlLRteHtLos4r3CjW5UG6GQY42V4Kb7W6RsPCSpOKEC3lt5XJAJy7byy2W5CeMHyTXNR5jR5zD1OohIRmPeHsiFGoOoB7NKwg7c_8rzpJAcFlnaMui2cXCBZNScpjrBolLZLx34UaI3waf3J9P2dxa3IfJWMJJjTpOrF1XzNMnVcTsthurAtEVW_VrSBQYagcF7CwNsujk6l4VRYzWlvDz2a2PtJIl7tejHlnbq7pUj2wxTx6OHZ2cCtGYJj4I36ZOgJ09HJ1SsjGP7J3V0aJ9fqPHUnjZ7qIQDwI4t9UaShXMIuiU1qDF8vvGYNN6uvR5-6KiZi3mdGoC5-vd3BD9WPSCnGkDp2-RqYWHAF5XMiYMrIjiDRuBUUQpAaRjzA4lwWlhMRI41NfN5utMbdyTk6NUzg8uzj_rX_zwPVlQOrKeeGqMpby5kIG9Lz7MkMKq2xfc86C2axsGccINlbchko8k_uiRjVDfPFxwE-7gDUArkoSrXPNlRVJPfjWhOFelItKJylBEd8lTAQKXQ7wJWqtvYdwUxhTZ_4v2vwXVxMvAv1MZqMwmRBWS4ybGvbWTsxPL3f5tVAYh1SWs86v9dMdJPK-DPTIpu5RYUz3Nr49vfZDNjXBzvpgCDWDCafhZUtW23S4UKQs0nDZXjfT_2TDbkXZT5c2YYHVK-WKFdSQSD__qete-bLtBsfswHllGw0tCV23sj-zNSa-uC_WiZh7lgJXSTgt-Opl4k0GvUVOOtHVqBqKv6jYjr6mfnMfdzbBLSsIY8qSoAcQEe2_0jWVBC3FTOc9-iFMsffDHmpp4fU9oEapTEZefg6_IDbFdjL7Sk7f_vd9EtYAR-iTQgDafI5uWc-Xx7yfbVbsKmrfa_xJLi0IosUC9WZT1q6COe4gh1evZMLfUSBS6GfYHsUi1zANr-H9WiPaEPsjcCyGmBdms2Nxfei6GQQMljzdWLC5ZAAfJwsIWieWOrpakd0ab9h2krgj1fON9w5YRSNOxjr3mrfw4Nov04Y5mFsvDnKKdGPXPG_lwKZ0xOvKnoY4SfajKKuIWFwOvibyc2f96mRf8HqdtGGnZeZcCubEaxD3dZaJ_DyYrNhz64LV4ov6CrNIk48whXYdQFaBF58HN0Cxc8_jGwnutUdj3vXmcLiw1Gdg6mtkCBPDxuxC1cQSmNIif0S7zpSqOBlHTTHhLyw2ZwGSDUql)](https://www.plantuml.com/plantuml/uml/hLPjRzf84FxkNp5mgKAanj1JxZvKeLTUd0I9afn3UkedjDXZM7NPfRjhqbpL_zxPDQy14ZZTIWdsUfvvPfuPU_QZiKpRV2A2e7JoOB0_nWb27SgjYy588yfo49n2ekGCjGLkuP7RCR0qvPOhoGGzcaoOJ45mYS3qA9-Wj73UZgDkez_v70qwlLRteHtLos4r3CjW5UG6GQY42V4Kb7W6RsPCSpOKEC3lt5XJAJy7byy2W5CeMHyTXNR5jR5zD1OohIRmPeHsiFGoOoB7NKwg7c_8rzpJAcFlnaMui2cXCBZNScpjrBolLZLx34UaI3waf3J9P2dxa3IfJWMJJjTpOrF1XzNMnVcTsthurAtEVW_VrSBQYagcF7CwNsujk6l4VRYzWlvDz2a2PtJIl7tejHlnbq7pUj2wxTx6OHZ2cCtGYJj4I36ZOgJ09HJ1SsjGP7J3V0aJ9fqPHUnjZ7qIQDwI4t9UaShXMIuiU1qDF8vvGYNN6uvR5-6KiZi3mdGoC5-vd3BD9WPSCnGkDp2-RqYWHAF5XMiYMrIjiDRuBUUQpAaRjzA4lwWlhMRI41NfN5utMbdyTk6NUzg8uzj_rX_zwPVlQOrKeeGqMpby5kIG9Lz7MkMKq2xfc86C2axsGccINlbchko8k_uiRjVDfPFxwE-7gDUArkoSrXPNlRVJPfjWhOFelItKJylBEd8lTAQKXQ7wJWqtvYdwUxhTZ_4v2vwXVxMvAv1MZqMwmRBWS4ybGvbWTsxPL3f5tVAYh1SWs86v9dMdJPK-DPTIpu5RYUz3Nr49vfZDNjXBzvpgCDWDCafhZUtW23S4UKQs0nDZXjfT_2TDbkXZT5c2YYHVK-WKFdSQSD__qete-bLtBsfswHllGw0tCV23sj-zNSa-uC_WiZh7lgJXSTgt-Opl4k0GvUVOOtHVqBqKv6jYjr6mfnMfdzbBLSsIY8qSoAcQEe2_0jWVBC3FTOc9-iFMsffDHmpp4fU9oEapTEZefg6_IDbFdjL7Sk7f_vd9EtYAR-iTQgDafI5uWc-Xx7yfbVbsKmrfa_xJLi0IosUC9WZT1q6COe4gh1evZMLfUSBS6GfYHsUi1zANr-H9WiPaEPsjcCyGmBdms2Nxfei6GQQMljzdWLC5ZAAfJwsIWieWOrpakd0ab9h2krgj1fON9w5YRSNOxjr3mrfw4Nov04Y5mFsvDnKKdGPXPG_lwKZ0xOvKnoY4SfajKKuIWFwOvibyc2f96mRf8HqdtGGnZeZcCubEaxD3dZaJ_DyYrNhz64LV4ov6CrNIk48whXYdQFaBF58HN0Cxc8_jGwnutUdj3vXmcLiw1Gdg6mtkCBPDxuxC1cQSmNIif0S7zpSqOBlHTTHhLyw2ZwGSDUql)
