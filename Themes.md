# Themes

![Theme sample](https://www.plantuml.com/plantuml/png/hLPRRzis57xNhpXrEzG657jRqpqC2537rjOKTknPJhk70GP57Tj4AL8ZAJl6iF--Gzri9Tq5wFBWY8Syt_dEbNnd7JEko6JmmkqnGvXSRmeb7AQmDJg3lNEv_N4qCkmut0ctBvB2ek5QELHko7KsoYLJ7k3AkbIAP3IvlbfwqSDyDigOTMX69R8DNWZ5PP7YLu8UlX_-CFoMH9i9QJ2Xq0npxq4GlrzysYoZLRoutomUrhEx-wW_25x3ckqis2BFjN6WDDYSSRGW510pK8pSxYVCai-w4XKgHIE54ce7tWFKxfIZ3U6u5tmFgLQlNGjOep5rohJ1mH38ujss5Hi4WxyNQ7rCQvCITwZIiFuF3XyT72aGbHBicGMd8K58SKl-fS4uJID9GLIEVEdt4iO_asBhVo-4LrjQJBJKvkPLD8lcqVrwyzE2VYQBsM95-yckskszVFFcxNJyrklOFSln9XAxlOj5Ycdir_q1xLJCraJifh46l37tcqAl0jRhz0QUtGfboOpPa-8UsljKqnclLfINXWU55Vzs8tOdYJTJPlUOpcZT7tJGFVZe_p6XdJkR29nmacg_SH1ImNQ6PR3L1kweB8r21xTCVVOL4PyebraGBD5OhVgyi4vdQ4AOj5-zCJHYqDiovmbfXrMMyrAHoL86Z7DTA6Sfa445lRabGShCgS-_8wod17e3-2C0-clvze-OR5YUq-5FcC0upwNWp0cjA4wz3-p0GeXpuydFFqwyR8fI78X6IOrcW1CSwWQaIavBSMitQHnVZebarp9LBC75j2tnQibswAqtLcDkHEv26AjT8PalqzxIw0EL3JM6b5-siYqKzzIP5Exa-u0NPI0j70JpAi80-Gk9qKSQ6yyOPJeH4kjmpCj5msdoCeHVMSOe4bqk84LM3ZrR99Qur3dxBzpiCt8L0UhTW-3ubDuqwQVCCJzkV1hgJyyc_cK6dRMZSMB1ZqQQ83jXdIbJIaE4oZ8hlqC_AwXNW1LKLznWIWaKJDAeeh92Qq7g7ItGyU6pGDLzJP4IlcANTrykdAccOmOkXyqvSlyI8HyK0YwxbORmpVF9DGZ-RCi-UdHzp9YG6riAo51qDQTrtNBUyfhI8agZr3zpmOssUkiWUkHxfgZwAas2lS2ikPrH2LDjZP_xtPw-2BilpxeAE0bQ_ow23opHXJkNGDYsSWYKAsLP6Obp-0EQOnVZujoq3nQjj_r-lLx6TB1xhcgnVpxJAVhoQ6LkS-z7TQ8lHaG5rmo06gaKTWkYCLZEsn0-qAqwgeotsQn6SOLmoU1hW3Qtf7ocVMwMBkWAMMghDugVLqT3xUjlJM-ejZEzdJHHy9WNqNfIP371Mi0hBoqnpaIUr6ENGrUli7usj-RZ-NfP0xNETDIVLMKJf_CjHzEA7ZnFOdLn2GxgDyyi-Zcwdz9RPwkryzSNlQnKTTSqpoOu3E4Rdt2goFwWZDd5eyhlJgu_Djl1Es99Jwg_00== "Theme sample")

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

!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/v2.6.0/C4_Container.puml

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

![Theme sample](https://www.plantuml.com/plantuml/png/fL5DJy904BttLwnuAGcqIem7JzIAO898R95ZixIZRB9VsPtQ4ED_TnOGlBkNIUQzUVFUxDWZTzWg6KKNk0K5BB-fMYqG6lRkZ69RHEllqjJnBlaGk6qthGTN6usWCQcDIgtaEYWCFJPIRDByPhWChTNpF5NS8xXqh-nfXT2rR1luf-hdABbDhgXLvJJ1XGQNs7s69JXlTCmR9VI0zR9GXKV7qRXUFofsP4TLzwRL3NUxkBucKi6LbS0EMA_FlY96xwGSTx2fkBN4NCE6PTPAKNCKHlUebLyEM5OiayMaf147R9HSi-UtF62PbARpB2Jp30sZM9OJHRKIHLXPTWBfF0o50acxF5dyFfgCyG2Ipf56OFGAyZVSsTRAqoJLMLak2s85qWazoqm1oKO7eOIl_JiI5RENTVKuVydAfyMqca-cayL3t8_6e1iwx0y= "Theme sample")

## List of available C4-themes

### C4_blue

C4_blue theme is the original theme and need no activation.

Theme [C4_blue](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_blue.puml) can be activated with

```plantuml
!theme C4_blue from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/fO_12i8m44Jl_Ohs0veLAHuyLOgt5Zme7YLDrxQmIKDse_Zt9lw2fna6vWtJikWWqL9HoO8MowvvZ1InV8RDbek8voD0q6yrhxB4CJ86ipb19yfi5Znfb-iroqJh25rJNt9q6tgmcWK3_BXSLAip52Vy4_hQguFQWK-D3roHvKHqfhJWXE-9rkECRb8-NsgJI_e5)

### C4_brown

Theme [C4_brown](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_brown.puml) can be activated with

```plantuml
!theme C4_brown from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/fO-z2i9048JxFCNb0N8h4Yoi8i4kWeLYAPTaJG9xFzpk6NnxBxw2rGm3ymtJi9WeoL9HoemMLLi_--XNfrxHMpMB13u2HBFgQP4vzOan3ju9Ej63jn38kArViOoqzD3MrNMBxfSEh67123ym5-NY1aeZ_Wbzx_L1xo3anWTko78YEbDUSCAFJEjmGZVgi7rgiilw1G==)


### C4_green

Theme [C4_green](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_green.puml) can be activated with

```plantuml
!theme C4_green from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/fO-n3e9044HxlW8-W5jZY8KLXjX1Og6nD0UiGBAtN6xtDFwzXxzWDPD9vasc5hL1ewEiq1aTvatrc08Yvy-mkdnMzN842FPjfaNds4V1CAoio6g6rO4dork_51rfwQ6foiiMtReMd1N503-mPCN20yKH_uI-zkPWTk1JumDN53qHdIajiCezqLgSa4VZjqzrSac_)

### C4_sandstone

Theme [C4_sandstone](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_sandstone.puml) can be activated with

```plantuml
!theme C4_sandstone from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/fO_12i8m44Jl_Ohs0veLAHuyLOgt5Zme7YLjrhQGR49se_Ztflw2fna6vWtJikWeoTcYaWKTbbtpO4s6nHEMp-XTkOW4FW94_LRpAaiQ4sESF0cIgCax25RJngXPZ5r7w9hwiaMteGUdMJ323yv5jT9aay4_eQ-zEgWTXDpum1LPJjQURLuWuNkczJWZ6HMsNsrsMRy=)

### C4_superhero

Theme [C4_superhero](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_superhero.puml) can be activated with

```plantuml
!theme C4_superhero from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/fOyx3i8m44Jxd28vGBm8HHHKGH5Ta2X0bCWuInnf_P5t3UBsE5o1QaPJl9dfMNIIxAXgnAB3UkZkd2CcYodKpnHSRKKYxm6IVgjv4PiVcJ6Pu0MzA1CSHD9-PRGi4oqF6Bhsl4RNqmXEis227vohPl66yeH_GbzRjLCRA3FD1ox8SY0wKcdmmhT26t56Fwcu_kgBA_e5)

### C4_united

Theme [C4_united](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_united.puml) can be activated with

```plantuml
!theme C4_united from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/fO_12i8m44Jl_Ohs0veLAHuyLOgt5Zme7YLjrZQmIKDse_Ztflw2fna6vWtJikWeoL5HoO8Eowvv96y5JVcCgoiNaS17WAZVQhQof34nncdrWbxKj3e8fFq6g5aCsH6wfhviqMtemMaMZF0ZSr5PFr4o-2VqjLS7jOEG6n-u8ik9w4nvmGlVCwt76RrHOJlLPfVr2m==)

### C4_violet

Theme [C4_violet](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/puml-theme-C4_violet.puml) can be activated with

```plantuml
!theme C4_violet from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes
```

![](https://www.plantuml.com/plantuml/png/fO-z2i9048JxF4No0BaL2HPMaM0NmKAnb4ko9WTxFzpkHNnxBxw2rGm3ymtJikWeoL9HoO8MowvvhiOJIlcAtfQBIE0ZGDHlDHjPqf0Ou-YTe1CrUWk1jDi0DSj4Pe2kgQzRTB_qO3KBHlYHkQYC6obD-2TqtQk3sa78ZG_SaEL4TAQyu8GVcTRZZ6vIOJlLPfVr2m==)

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

