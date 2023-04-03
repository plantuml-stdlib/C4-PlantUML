# Themes

![Theme sample](https://www.plantuml.com/plantuml/png/hLRHRzks4txtNt5r-qCTG8dnGzkN0G7gsDwQmauyosttCC0uYMU9A4Lg91N76FQ_xqXRLknqw83r9J6FlE_x-F5uudldqVgcKhqNlgIAOFnstMZfIS36cWfAxsltqt1eSNjLI5ysMUF8vaPxqlugDzMmLgW3mANpGibiE7vxkGYXJ_FPi4BdoGuZikkza3fNZQ0V0yf2nvo1KfEzgiCEUkc7-o_hnNIPtj-jxp-jPhTtqy55xpMii73WchesreCsu6hCoO7KmCf0OqKmoD2H0BCFDLgGLL9BNK0W8-DtDRa4jgNCIn16l_OjO8k6UbSPInTNm8otcsFO4bZweo764IsbeeAqI0x_mTEZXoqRiK-24Xru0nc1e8tK97eZ8QQAAjAUzpBePvX_vSJZ_li9lDhmO6oKiTUlfhFfV7gtMlzypt_6zxFx9SzdnNws__BDctUJqRkGuqgiwNegYzAdKf18mtXmmJDxPIiMTjsoGTxI_Quff80BEVsBe6v9AYf3jzDvWEOzjN96ooMVIwj3CS8_JgH-f-XwWguaCPEQjPoW1_3XZw4mtdSKFI-z8ZZw2K9YOR62ZR5mgprPJHvkK7yD5P7kdAUgrrkGTKOFyiPvKv5DO7pyrHz16mQpYMUUSNQoF-Kw9gAACS0yDutshiywzj3h6mu8jBj1_d_6EXVGlu0_Um3GwHriALjZNVFYBvJ1gAwLpD5Be_iS-eWFc41Qso1-_daSOXDIye5bH6dEyzeS3XSGK8iOFl9cxSON8nPvokngPBYKfnLTBh2WmDwofhcLjKzWf8j6eGtXXJKFKf03LEhRB9j6vq4wAkbtu0qx6Orqy20nf4WBl5_8hDawiiyKLIQJYWvspEEWrJH-cS1lMA6L-bGBA5d5fkUQp947i_dNsjmpSNi18EX1vdGkRv8D17eCxIOSm-5dK9F-EeEJiJUM78JM29OAwRoDHmfISrbMyNS2PRmhW8ql8RSaI7k9oYMXhCWvKARW0VdywfbHXtlDJibGiOlRRnVEnF0os-MTEFSTXu8f31nlAnRk-bddOb5_7Sj--kW7LA5KQnS3J3IzdFFuSEK2yweaa94K5SnbReqp6m_Jnxn4NH3iCnds2UP1MuVAc7fZiQApEztP7igphOAS0-t-dfeFc9d6ToMG7Azo0jwYTXYTwEplBKazQHVTfVtao0Nk3wlL8kM5f-jSZTzTqnPz1xUdMz-5LfsPhaL4kAu1791YyBGWMiBORnFuo5_LOIJlJZDE7H0w1VyDQ7t3oPtixhASWYu9XOjlbDYljbPwSk1D83hmJ6x637d4VEBMMP6b3Ek0BaCqOdH2JklnJCDfNkEuFZhwTBvQx86wpPoadrLbvrFtbUDkDP-TUzLDC_p-pJER_ZAzc_1RPsEC9ml2ubRllpNjimaUhk1_uS2bqOEBw5buL7MpFFpSJlVUiygcKdy3 "Theme sample")

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
  - [Write custom themes](#write-custom-themes)
    - [Following variables could be set in a theme, additional to the skinparams and styles](#following-variables-could-be-set-in-a-theme-additional-to-the-skinparams-and-styles)
- samples
  - [📄 C4 Model Diagrams](samples/C4CoreDiagrams.md#c4-model-diagrams)

## Use theme

Similar to PlantUML themes supports C4-PlantUML `C4_...` specific themes too (sometimes based on existing PlantUML themes).

Additional to the standard themes with skinparam and style definitions requires C4-PlantUML corresponding variable definitions.
Therefore we started with the convention that all C4-PlantUML compatible themes start with `C4_...` in the name
(e.g. theme [`C4_united`](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_united.puml)
bases on the [`united`](https://raw.githubusercontent.com/plantuml/plantuml/master/themes/puml-theme-united.puml) theme
and contains all additional required C4-PlantUML settings that it can be directly used in all C4-PlantUML diagrams).

E.g. in order to invoke theme `C4_united` from a remote repository, you have to use the following directive:

```plantuml
!theme C4_united from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

In order to invoke a local theme `C4_foo`, you have to use the following directive:

```plantuml
!theme C4_foo from /path/to/themes/folder
```

(It is planed that included themes can be loaded via `!theme C4_united from <C4/themes>` too, but this requires a PlantUML extension with is missing atm)

```plantuml
@startuml

!theme C4_united from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes

!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

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

![Theme sample](https://www.plantuml.com/plantuml/png/hL5Dxz8m6B_lKzHv6ScVBHXEdfWJmOINnGqvBjtsA4twqhHFin3ZT_Sf8FW1tALPV-_foYDt69HCadTu0GMiMdP12uIH_N16iGkYzH-Bml4f_odm4lhWmGr68sZC1wCAAxcE3dEFenHzKItdTRmwxNU5uXx15JTdJn523pACy7zSgMb52YuqkDpUDjJWlD4P7vNGRomjuoayEex6fREakP9GTPzCq2DtrsnO4AdXoafWTooTiLy9e-_fd4tGTznQOfwXPwMrKWmSXT4fNLNltrZPrFbXtPB40VkGBzZ-UnMnKaepUHQNUOQ6qIpBYQA2H14ZsqaWWcCe54ZAybJnzwDaXdUGV1uq0fDl8F-EUzKwUV0nRzksTKEiI7gYBviDeATVY4TysdybIRCzdhilksFPVZrikjrwipvypcR92lGObFm3 "Theme sample")

## List of available C4-themes

### C4_blue

C4_blue theme is the original theme and need no activation.

Theme [C4_blue](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_blue.puml) can be activated with

```plantuml
!theme C4_blue from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/hO-noeD048Hxdq8VGBUn-Yj_99s150afmwaR5VRMutQEaBVFcMT8DSF0zy5q1XUHl1GLLlPSzkrZbCJbC-w-N85WVqJHlPfbmvh6P1odNS6APjez1N5wuBLXbcsalgqlntGx3-ITWIDzlLPKcqwIPlwDD6JYJLSs_8kSX3qhx9vj0o-iSnEEIrrkEJy0)

### C4_brown

Theme [C4_brown](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_brown.puml) can be activated with

```plantuml
!theme C4_brown from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/hOyn2eD044LxJw47q6ciKXaadO4K2Id3gXCLPcUNcLaajy-QCwJwdm_lmU_Kd5ZoL5IseiUoRr-ZX9tBjmHVhcPHJm3YzcRPR4rZKfGfi25RCmKFaHmVVAqsqpP2tzQtOtfS1_1E3GL-OYsgZITAC_v76ZFnWJkgdOakX3wp-ios0HVakOd7fowtd5y0)


### C4_green

Theme [C4_green](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_green.puml) can be activated with

```plantuml
!theme C4_green from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/hO-noeD048Hxdq8VGBUn-Yj_99s150afmwaJ5VREOtUFaBVFcMT8DSF0zy5qQauiUIugM-5HzkrZ4I2KJzbzkPf5_ICIzsgMpTOq9eLCUp04QwRTKsGN3hvMctaRgM_hop7TpWDvfmQXhrYBQWiJfnc_aSPClEaAjN_c4yDdLk_PDc11c9juVEfoo_a1)

### C4_sandstone

Theme [C4_sandstone](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_sandstone.puml) can be activated with

```plantuml
!theme C4_sandstone from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/hS-noeD03C3ntQVG1z0iJj_aXtIpqA6bOpczL8KaTrnobBvzppv3fuJ0_mSPr5oop5GrjY5ZFVOFTUBLWc3zJ87hpIpg7q1ohsxTRSjpLanB44EnRWaCaPmSHglcQPzXxDlBSRgT9s2dXWc-k5RDBWjbZxz1OodUS4MrVw8J8PTMxqMRS4NnNJp-6ifMvWS0)

### C4_superhero

Theme [C4_superhero](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_superhero.puml) can be activated with

```plantuml
!theme C4_superhero from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/hS-noeD03C3ntQVG1z0iJj_aXtIpqA6bOparzOJaxaXobBvzppv3fuJ0_mSPr9nOPgeQyyXOZ_r3SqBnAB5-IkJQcoNz0n3twhRTV9wpeYmn60RhbiYGo8N3QDLMscSO-_Pod6xd2TYfeS0NrwhPmq9vnT-WgHHlkABQFz69a4khzw9Dk65OktJyDPIjp0y0)

### C4_united

Theme [C4_united](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_united.puml) can be activated with

```plantuml
!theme C4_united from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/hSyngiCm3CRnFQT83f1eoVIcF4At53gqT2nEh2O6sJ7MPqflNwTdw2GX-Fz0Wy8aP2zLWuqzrsF_oC61RVrCkwyt8EeVKJAlRdNOyfoLqx87S42tx9wYc700hSAAcsdisyjnkfqdyaR1YRwoLeqBYsJBlq5ZATvqPSM_o4dObrRlHPjuvM2xU3mrbAtC3m00)

### C4_violet

Theme [C4_violet](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_violet.puml) can be activated with

```plantuml
!theme C4_violet from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/hS_12i8m383X-vvYUu0jbvqyJOQt2HuKZz9jSIiaRMbInRUtzHay9GJ-3pA8cgY9gMfqHyPwx1ylwmcrVaRFzQuQv00GpRlRhEvfJe9nyKxHQRTuXa365Q0LNSdECFRjfPnkvmdOY6A4donLOzr2QSN_e24N7xYYw97eHCYvbNlM9jpGhLqeJmrvo_CB)

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

