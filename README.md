# C4-PlantUML

![Container diagram for Internet Banking System](https://www.plantuml.com/plantuml/png/0/bLLDZzis4BtxLqoTGnr0kqQ0ddgArpQwcwntrSZRJK_2Y1hRH2XI82axHj7_tg6i3yiEajGdQJJpvl7D6_gzysXzLQZHBr8BLUK4E-zBz_jqQl5mkvL-LsML8okCzgJzhJ3557ChKUzLLLRJ-MytiKBjNrQFKuMUdETGEkTib9hiRHcmVuLASs710E1t11kZb3b8lGN5IO0wXy5dQHq_6U36e8n0fOwCqJ6yRi1V7sT_Fx-iq_Lpd2wUNvycR_lOB4cJZylr_9w3JUZrONsVFYx_M3ujE3ZoqYl6RK4XbxYrM31H2mzySAl9mntgBu5pSdIUYj4e9kkCdeZAULEGZM3UFOrdq8R1REf3PLmTmO45XR8kH5N708KmbVPkp3nEqEaT1tAqnubunrYN1CPluPyHyA_ZEpbGbc9PSl8hPJ0hIoK5Ucdqc4CVS8yH9AKDv5T_pKDiGKhkcKPDZJtWfO1cnFKuGhZhcxK7ZsTCSjZPbOmzJlYpefiOjnIwjrqJOMNf8vZfRQNGXd1ipLxcv827-kqk6_PAe8vA-cDmWQXg8Hti9OOIQO7F2var1pRc5QF2P59H8yUgVcavpTz4y1aBP2M6NDY7XVIKWwionroQcVqCDtT5xaG0SjfBGPVq5jaaHuyPEWfZQ1u3c-JFHnYyUsEPMrW-iBILpblarY0rkxAefnl1ZfDpm8fT9IpbF3w9oaN1LEGSBy-MNyYBsokPCXHVIEUiamn-ZH--RPk5uJJRrmrq-u4-GH86vjR_TjPUVlKJAb2grDK1XblUhFYzMQk0lsRfPGtDExAImXfdDXwMNyKEDJliLCcmPvWDWnwLCVM6TvWkzlPCsc31PjA20zqfpXG6p4pb-p57tRf6mFFG3klpzYAFFf4wknBwnNnnv4Bl-_KwJZXnc7TQe-_d38nTfvxQfKyajxlCd5q39xXsoHkaEZWSUziGtL6B23uapq_Jy-RdBVzNPNh7sJsntl93b4-4kOEDDKLzwnmiBo7VIIOWDy2Bktbxpe1vfiU5ZHA6TK0t8LfZz4Gk73VaCAohNBXXk_R9QXqtGDrX1kLNlck52VNJHftF_EVOYlEUI_alwpy0 "Container diagram for Internet Banking System")

C4-PlantUML combines the benefits of [PlantUML](http://en.plantuml.com/) and the [C4 model](https://c4model.com/) for providing a simple way of describing and communicate software architectures - especially during up-front design sessions - with an intuitive language using open source and platform independent tools.

C4-PlantUML includes macros, stereotypes, and other goodies (like VSCode Snippets) for creating C4 diagrams with PlantUML.

* [Getting Started](#getting-started)
* [Supported Diagram Types](#supported-diagram-types)
* [Snippets for Visual Studio Code](#snippets-for-visual-studio-code)
* [Layout Options](#layout-options)
* [Samples](#advanced-samples)
* [Background](#background)
* [License](#license)

>### Update notice
>Supports PlantUML version 1.2019.6

## Getting Started

At the top of your C4 PlantUML `.puml` file, you need to include the `C4_Context.puml`, `C4_Container.puml` or `C4_Component.puml` file found in the `root` of this repo.

To be independent of any internet connectifity, you can also download the files found in the `root` and reference it locally with

```c#
!include path/to/C4_Container.puml
```

Just remember to change the `!include` statements inside the top of the files.

If you want to use the always up-to-date version in this repo, use the following:

```c#
!include https://raw.githubusercontent.com/adrianvlupu/C4-PlantUML/latest/C4_Container.puml
```

Now let's create a C4 Container diagram:

After you have included `C4_Container.puml` you can use the defined macro definitions for the C4 elements: `Person`, `Person_Ext`, `System`, `System_Ext`, `Container`, `Relationship`, `Boundary`, and `System_Boundary`

```csharp
@startuml C4_Elements
!include https://raw.githubusercontent.com/adrianvlupu/C4-PlantUML/latest/C4_Container.puml

Person(personAlias, "Label", "Optional Description")
Container(containerAlias, "Label", "Technology", "Optional Description")
System(systemAlias, "Label", "Optional Description")

Rel(personAlias, containerAlias, "Label", "Optional Technology")
@enduml
```

![C4_Elements](http://www.plantuml.com/plantuml/png/xLXhKziu5FtkNw663oqpOGcq1PODcUPX2hCXOV8Ojaix6H4hYQUEv96KGdQx_tqbsH5EX5Phf_2fOWQCTU-vvrx9HuyFZ4FA5_F8UmsQ92AKYOSTP_EyLm6QX1W1l-rV-Pt1wBmhVZMxxMuFx9ohvWcaFbz68Pxcn1pupOjEWjY__DC71uUUnxw6E8OKpe4mWek83z03hqVX5CyHvc0iVY6QDRkdCBu90pu3XvLAvlqSFbmXnk0KzSE_43XuNybwKJJc44yZ1FxsW6XzWOe8NyRed62UU1og7ZQ30RaNoO49Z1Zo_id2r2abzoc4AYlOEL9DlP5Gvjji00bcSgfMxyW21v0kQxKLlmqM5iuL8y86ZtUggRSDGWD4RU_bY28GG3P3WQJv6hJXaYnulY6EY63Shd_g3WUZUd_K_zqVD2yoAT_1yTSfbSccF7pVRxIQ6OiPnC4z3Jb7672wGEO4aTbru1o1KfFCmp7eGyp0LR_a9NC5J0YHVweJ8kUF37D6KL2xWHIBUfvMzsL73JGfWXm5mfo286JZ1MCXmMM04GeOu0JS8V0DHc4WhRnN20UFAUfyLxaEkjUZLlUc8_nYvKiu9u9nACTOm6xQj_tpmQXt-V5Y028quTA5XjCPptY8mZUIMH6Yl1zlwhXyWqOY0yZA08qYU8UYtSo7K3exIz-MmDeCX0oaVcv0-I1dvDF0u3Rf_MAF83BheGZAbDaiZ7CcAbn7Aqu7vHNeuHezNTApKcaNh8op7TeFd4hokYovmd0qdk6judt6-_jL9hxZqmsXhDscy5-g-xA_jhzVMgk1u3QXP5uMPYGprYbjiwiCIdjxjTAk4qCdPeAPDXfrhMuDySc_IHsKjqdGx9CCgtjxag4RokJfCDBWQ-WT9Bx0EqAB55DaxSOgMjIdQwfZ52okm7H3RblaJUAj8iMLmcfKkBLzQUtOv1xRYLf2Eo5CXkuqDietB5A-uRMHu73xujcGOnj5EtqdWCbjcAjixI9baqkqaLvx-yBPiT64subQGbiW70pRkShNAr8-kRanS-pzWFhPmOLuMIjepyEDOP9qP_AuWmONA8fHxWEOSDRge639RggrOEzs5WO1mbzQUwfZpMVey1a-uTDp-FIUy6axVDgfZpekZacCJa4Ti53j41cPy7j8nSEISJJ_HPXSqt0EwHAW2Cc37pi5WvbX248CcCII7lr571FA1MB6wHgHM0I0EDZqPUdUEbg2CS5OFA40S0Au8ymbvWW7mXOkWX3XiSZ3_uReyeu4oxBSwC-06l5m32CL5nEyz_WcLeJA0fA5GK9Cp0drJ2RhmGFq3KKabfa8I2ZAKlJmVktt-jtEgF5nTNAldBmxF6xeVl-FWT_hrDiZm_3eHFvem_wd_i2_olGV71oTD5eca67ugsfvxmeinsFv-H1Sgvc7TttIDUyhbAdJeB5n8jseY7bohXo_RHoTMq_ow46Gmp0QlI1dFGfEyYTr-MCbdqp_b-2iPvQLwjlcyNcpugxp2t8sPxkxpjlVeznS3Yv6RV-ZtsbvCwaRJAVeHMYAS93S7NZVpy1Q4_yFX17uxdslRioCMce1abcgJ7HsDjjLoRDE6vMeISDKHTT1jQ4DL3k9X5HQvgNBQ-2dGfzN3nNX7BSXIORhDnKECFaG83QcJwD-nf_noi8IOPFlo7_WEJWRocEGDv2B9k0Cf-FrrQZco88f1vEy2LQKk1d1u5kqycxosrRU6QxujQ6ccFFs4DmcVlPBlk9xm2R170fgb87xaCz23FZBxGh7EhXb7pZOsEKLsUJz9fp6aO0KXBKHfEDPo0KPLbuv21OALpubjwNxB4aLC0uda-ARnQPOzEgN7R-NsRszUtlIQht_GRitNSSNMQHrEkwzHVxb-UVoB9oC2gUuUfoVPn7NMc3gfpvrcmALzruTPEThLiJoy305lJ2X3V4to1MNVJEX_CglNNEAlyx29llpc63vd9LzxUGM_CowySQzSA1T44SB1k9YouGcQrac-gQionWPPTz6lA-kknqXYndnFddVQ9nNVf1uw-os4--TYceMnTOvM1NxM9odMYVFfjW_5LjO6UEWhT8fy5owdi8_jwxhF0nTDtYyiAxRoScM7ZYJIL9Fc9NQwl0X7hen3uaSxvQ42jL_ucBySPNIWsouglqhYSXq-Hz0wQ4hcKt_DxhNGz4wOOE52V58Ho1yG3XOpAD_0G00 "C4_Elements")

In addition to this, it is also possible to define a system or component boundary.

Take a look a look at the following sample of a C4 Container Diagram:

```csharp
@startuml Basic Sample
!include https://raw.githubusercontent.com/adrianvlupu/C4-PlantUML/latest/C4_Container.puml

Person(admin, "Administrator")
System_Boundary(c1, "Sample System") {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![Basic Sample](http://www.plantuml.com/plantuml/png/xLXhRziw4ltkNy7hV6W3E8sJFfhDEaRzK1vOnmaiPRDtsy9Wf74iN9aKIBgkTzl_laD9PcGpMa7sRJvT1aWKSURCcI5r-FWa5HLgFejghqYFHrn8VDWhRRNQRm5CGWR46JZNpj0Rdz_WhzxDu6P4ziwJLaCaLosZa3rMnFIStkKmHNIl_ksGe-DQJVuHifWAEYDeHEUHyk2xwaJX8vi1KyJ7No3oPWj1u_imK5Dot6pcti_ezskGaZw26_u7oD7xPjvBWAyeUuo0_BT6iBc82bmjOpZdJAKUnqcFdDA0Bp0vCg6HXDhFF4n72Bx889AoahqFIKlUQ2ZxRJx0psSvjLeFVCu2AfRjzehV1ei2paqhmWQFTqbBtdQv240KlTSZ2YIWSWg1flcA3EYIprMr8OuuCXvqVh-vyyOTT-p-m_5wbxcK7wZ_nwFGoMOy7CVfzdivYobbmKA4IW4ZIip1dY0wko6T0Qdt-2pqYKkP9DTklPRE5JBXNFzfJT2E-3hCcO2WVKy5mtgUjWvrHvlq15050PeB4eJIdqiPSjOW322GH77o0EGRZS90MzL-0nOyfMZoNUNgtToE-pVtG_IB4r-k59yXhXvZXDsq7pZdtdXqTN7faGWcIhk8y76gSXvO-6uwAqAe-l5cZilNCCOCg6mG64Vq0QBzt8TGFplBtjR9sWoaacH-vO3wGS_8vu79vxJtQt44p6m44TKfosaOLqmKNSShJaUD5UZn6ZrJqhDwVP-iZFCTne-SQlAcB9N2AF2dRATuNzZXOKlYTtow8PJjpndyrzQXxcyV7jRNQe3S9eBF6cZ6SsETqRQx6gH-SD2kxvTYcCHiCDl6eAxLhOkV_EkLW_Qs2Tfzcc7hu40pB8UoUPOO6V0rz27W5_Z0nJR5nAoBi7OlwlCrDJ6sB2vYba7kNkHDulrjYgk5rQfmV_VI5cFp1IiWMXow7C9cM9h6HldkjYdVtQsLuDtknIj2Zeie5jCl1R2vtLKgss2Rikabsafli7lXYh5XeWg85eSkW2XXEAXKlj4svTER6pl7qUxr-p_WA5w55IpEenp39bcUoTCEcbn254Fb0nWw6tL8OFb-fhNauFCq309WN_i7ISUQprs9pzqpFgCIdz4pFeCIdq7canmNVHx3AUaG6IOxHCadQa45FYobWjaRDBaLuOoA9O48zC5FdX9lQXcIa16fiRI7EuzZBXGYvfnkWSSOWB9WqrTcU-jeINpE63v1G1GdgYJC5LF00hIbyo04vcCUpZSGomSUB1jwepyboOY7FesIk8opWwStSKAeWP0o359YVAwIPpvP3nx0DuXuh3D1I8fbsVRmVkkCt9lXk7knEhatJzuTV-oQVkTVdZCQTWPZo_33YVunXkxlhkTSv_gFZZwSTFisa6NujwHLlIieE1xhpuUpTji-l9kJhdrVaPYM6dGtJgGR5R5FpisFRxiVpWjFyl0ToJ4QZL-Ginc5Kl8d7VrJI3wT_Y_2sKoO8gflUn_FUytoEhyWPtksbzTvztkK-ollSZnmBfnXlpRLkY5DYhK87e45wTr1xSSPMMluluT6v4VjHsjZPhGp2vBEqiJ4P5TakofvtccZ4crjcAdeEgWnB08rJfXGafPzwVAAE9dGLzN3X725sv0qmxMRYZ8m_H20zCNpg5_O5xQoA8YmoNViV5SLEEUKnuQsaNTBe2ISYUScereX2_Cvs-GDs6x4hGWstsqhNqv-vygNXDlXsj1Gh7XxI3wdViMNVDll0NkSAOhKX2IBK4r3HjJBxGfz4xnW7-XjxFAssUJz7Pty226Hi36Ymf-62id8nie1MQIu-9JUbXxAD5KY5PrCjjyizd3HwrmDdL5kz_RkxKc___vFshsPEhx88ctIATzR_BKyLr-UqScgS8PhnldNBE962spzDATkMw2gtgkJ_7pDYrWL7aRGToUq8VuskTrbtoHKNVcDQqNnDraKoVuivam_vsNVE9KBVcxTU5s-SC0-YQEv9F5souGXMx1CkBQiwnWvPTz5lAzlRuOeYpdnFddVxPut_oJnDjdj9jvxpQGLABR9eL2nF-9vgd_oonJxByL6ApCEbbKs1NwLhcVmlrhNJHv5kfvrlxok5vF3bfqtQJ0BaK2ze_-6KWcgkC0RyCrDkt-4HYwTQILB--hxwPURMxaMy32cSOoMz_10Ed4SXNwogwpZgzvUWtJSspT3nqCN0UJupH6v_cTFztMYY2yacKiafGLGqwPeCfj7AjGXFPHR1OAeS0OHnf98yMT6yhLAEn4dCyFEsWYYLN9FjEuaI1tlqlDkNRJIHgRt2UO2bCH_GV_Hryzvbq_0Wlai-Xy0 "Basic Sample")

## Supported Diagram Types

* System Context & System Landscape diagrams
  * Import: `!include https://raw.githubusercontent.com/adrianvlupu/C4-PlantUML/latest/C4_Context.puml`
  * Macros: `Person`, `Person_Ext`, `System`, `System_Ext`, `SystemDb`, `SystemDb_Ext`, `Boundary`, `System_Boundary`, `Enterprise_Boundary`
* Container diagram
  * Import: `!include https://raw.githubusercontent.com/adrianvlupu/latest/C4_Container.puml`
  * Additional Macros: `Container`, `ContainerDb`, `Container_Boundary`
* Component diagram
  * Import: `!include https://raw.githubusercontent.com/adrianvlupu/C4-PlantUML/latest/C4_Component.puml`
  * Additional Macros: `Component`, `ComponentDb`
* Dynamic diagram
  * Import: `!include https://raw.githubusercontent.com/adrianvlupu/C4-PlantUML/latest/C4_Dynamic.puml`
  * Additional Macros: `RelIndex`, `increment`, `setIndex`
* Deployment diagram
  * Import: `!include https://raw.githubusercontent.com/adrianvlupu/C4-PlantUML/latest/C4_Deployment.puml`
  * Additional Macros: `Deployment_Node`

Take a look at each of the [C4 Model Diagram Samples](samples/C4CoreDiagrams.md).

## Snippets for Visual Studio Code

Because the PlantUML support inside of Visual Studio Code is excellent with the [PlantUML extension](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml), you can also find VS Code snippets for C4-PlantUML at [.vscode/C4.code-snippets](.vscode/C4.code-snippets).

Project level snippets are now supported in [VSCode 1.28](https://code.visualstudio.com/updates/v1_28#_project-level-snippets).
Just include the `C4.code-snippets` file in the `.vscode` folder of your project.

It is possible to save them directly inside VS Code: [Creating your own snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_creating-your-own-snippets).

![C4-PlantUML Snippets Video](images/vscode_c4plantuml_snippets.gif)

## Layout Options

C4-PlantUML also comes with some layout options to make it easy and reuseable to create nice and useful diagrams:

* [LAYOUT_TOP_DOWN() or LAYOUT_LEFT_RIGHT()](LayoutOptions.md#layout_top_down-or-layout_left_right)
* [LAYOUT_WITH_LEGEND()](LayoutOptions.md#layout_with_legend)
* [LAYOUT_AS_SKETCH()](LayoutOptions.md#layout_as_sketch)

## Advanced Samples

The following advanced samples are reproductions with C4-PlantUML from official [C4 model samples](https://c4model.com/#examples) created by [Simon Brown](http://simonbrown.je/).

The core diagram samples from [c4model.com](https://c4model.com/#coreDiagrams) are available [here](samples/C4CoreDiagrams.md).

### techtribes.js

Source: [C4_Container Diagram Sample - techtribesjs.puml](samples/C4_Container%20Diagram%20Sample%20-%20techtribesjs.puml)

![techtribesjs](https://www.plantuml.com/plantuml/png/0/ZLLDSziu3BthLs1zgJAZjTkatSpigKwS9csTZqRoPdhIK19iiwL8BKd5yNJwtmjIiYp5tSdwO54W2Bm7F53lZMNQrgM0aSLyRJNFq7mpe-0FBdDH5mXhQolpzsIYsMQyudPTPxL1dIjfKTfnhie9ApHdyb7KLJqvV_lddM3IBgxd4y4i6akcz9oy6PUennMb2bv1BUbWIG70hX6MIWYruN85Wfo0oG86srmRMYcWn21KpeJOKemEuM62O3xzUhj8qkJsBftTFjo4Hy6hrZIDq_ZpHN9-HRRMzF0nkKhd5vSNDpCo1i4TQgDaUl5aGoQLt9QgDgaZ7S5ekZF0WWoZezOvPAkLnXKHBZhFplBSjIYvvCPgPZcbsRaFhBiZGRmr5ilqJDMoO7eRvc-YVgV6rAgZ7m7Gp_zrTGWtcAMigiZx0JEOLfNWkGyz8jCdziWYY2ljQdxzpta4YIff6qx7Jsv_wlfXNBsrSOL_vBY12bKbC88cSmIj12B0HtgGuPlAw1zjFeQbLgNldMyNEC0H59pqGs-klnyJC9XRvKaEaC-oKAD8YunmtAFmcEdGZ5cMCOCEtlKs_ZA7T-Dt3TgOmg0vmEUVK6AP4Oirfr9Gyk_cETwC5IldVidjLPs1nagrB0wWXKikqFYEKDeFz09DVnoA3zFavBW7no3J-HguBF09pUzeIcN-5NJWHZawZY3uivwYaYirEuFZyV60f2_iVHnFffOMIyJ2G9W9jGA2RSsHBwxT8Dh3b65T5QH7fxP5izff0KwTbr54Y9GowXoeg5fvqb4RT5YdTbIz3e1Koy3aQongGQAdPd67uMSdOZTGTiDj0o5fLkJHssuk6DfjiWmt7Kq2C3fpJySk87qSZEXU-3H3nd6vIfAxcFozz_CvVS7zTxFwtqVycMwx9sDMjArp1TjexafhbU_hb_daq-oCHh1IsiB9oUk_sjnTd87gzh6Uk-tarFFe2Md3DRfkMfKhqIOxFdtzvhI5dIxsydW1UE6K-WBwVhW1_eUE_87V8O73SlrVElkeUyLTadvtWgQvN2fTDfVjVcQwilL5q8NQgzEv3Y9aghPGrHdTiZGGz57oyy5fQ3c-47KdQnzqDqorSLSp3Re7rnlsVYZ7TSwswNrtO-vBJLllKHRqDVm5 "techtribesjs")

### Message Bus and Microservices

Source: [C4_Container Diagram Sample - message bus.puml](samples/C4_Container%20Diagram%20Sample%20-%20message%20bus.puml)

![messagebus](https://www.plantuml.com/plantuml/png/0/bLN1Sjem4BtxAxRqa6Gc2Msdfvv2W6dQaa0mcKnFdhKiG1DPqaWoAUdqtxkoZR49CqsvOArNxxrzkmjNpgFrHIwXbtFdSCNJmlMYTq8nMMGSrjuRzwNVj_XykH9-NT1hRfbMdYj_oNJUnymAL1jPcA8__7mnawZym-saBz5pvocK32aRXUBsqX1HT0A5eeiv0O1VSrXgAVMpK2kGb0IeCkYy5jRHamOY1gaPIhabZ4RXQuB8FGbbq68EpnRDeyZy6Zvz-D2Av_ZhjYet5Y-yV1bD1Z-d3ujaCPqbe-dZtUbPT5A71d4I_nWlXZSKgqEFtnOtoMJyTNmtec0KpRXrMfsomdcTStiEm-QfDu1Tk4UfyTPvdYVNkb0Pskqf-qWfkspuffRQvkY5Lhqp-1r5G9-clbCqffqzC4OALcLJ_3jkq34hZ3-7WLeL4cq83uA_hX7XWfavAYe-62mi6AkNGlAWhaktkv9GppU2yJPtN8LslESG6nkQUAsr3y45zSveGLtKIq36o6vgjMraW6YNUiXS3sD2uqPOTQ_WccQJZdDCK-5lxqiQYyePRNq9JkbqdPZuXkR7lSQrFEIIpbP9yrsiNTEyIBVXUsXv66HGGQiKZcUGeSUIhG43KrYZ7Jz2Y4KcV8ji4Cvjek7x_kNTU14UPrPlH4PasgvG2LTwS_5C8IXX0jCIcP3qU8HhbEuRbgNjNer8SOgkv9jQP9B3nqyid6AlBNTlQmhXx-qh2VREjHbkj_7zf0MEE_DUoBmD3I21bqCXvRvXZQcOmLgp__4siEoT3QT0FWuJi3_MMbhr0QQwyFMaq2QWXpLkw2UFbemhdX7VdoYQSzdQwch_7e8Q-hvPB6Pna4L9oRnQpYChys2oSeIEcGoX_bK0GxTLx1o-nzExVWTuScGDAnqnLvbh2j01vP6diMPFtDFjIjNhoztTga0QRKKfjWLwrh5WZz8TjThUiekY-Z4QNG_h4hhRV6m5toQY0tEuMF-6A36Ei1yCzK4f5VK1MtVowXirLtadck2Mp3_2ra6Yn2lIJVzQVm40 "messagebus")

## Background

[PlantUML](http://en.plantuml.com/) is an open source project that allows you to create UML diagrams.
Diagrams are defined using a simple and intuitive language.
Images can be generated in PNG, in SVG or in LaTeX format.

PlantUML was created to allow the drawing of UML diagrams, using a simple and human readable text description.
Because it does not prevent you from drawing inconsistent diagrams, it is a drawing tool and not a modeling tool.
It is the most used text-based diagram drawing tool with [extensive support into wikis and forums, text editors and IDEs, use by different programming languages and documentation generators](http://en.plantuml.com/running).

The [C4 model](https://c4model.com/) for software architecture is an "abstraction-first" approach to diagramming, based upon abstractions that reflect how software architects and developers think about and build software.
The small set of abstractions and diagram types makes the C4 model easy to learn and use.
C4 stands for context, containers, components, and code — a set of hierarchical diagrams that you can use to describe your software architecture at different zoom levels, each useful for different audiences.

The C4 model was created as a way to help software development teams describe and communicate software architecture, both during up-front design sessions and when retrospectively documenting an existing codebase.

More information can be found here:

* [The C4 model for software architecture](https://c4model.com/)
* [REAL WORLD PlantUML - Sample Gallery](https://real-world-plantuml.com/)
* [Visualising and documenting software architecture cheat sheets](http://www.codingthearchitecture.com/2017/04/27/visualising_and_documenting_software_architecture_cheat_sheets.html)
* [PlantUML and Structurizr - Create models not diagrams](http://www.codingthearchitecture.com/2016/12/08/plantuml_and_structurizr.html)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details