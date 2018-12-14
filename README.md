# C4-PlantUML

![Container diagram for Internet Banking System](http://www.plantuml.com/plantuml/png/pPLjZzCu4CVVzrECojlssbrWsKFTYZwmEX2zwrrw1n8WD4ccgOLZHxQpfHnyztDSDoJhLjp3eYChhTePpzy__psPFj46bIbptj7lcIXGOGufhR7aPaKVp8IpJEGa32Js7wd6ggt2uYLBpGREXyD6FCSF2z8QCuhOHuApXysaeiIWo3Z1dnsmJsGrIPfTGTTIc7t1kSle3QPooqG6Q-IQEf-RW6WmHltVH2PAoQrNc4ak5ToxS8-BL4fXjAd_-TYnHgDObY95jHkF3tHjXbF4ms23MnWFtEEYKwbIKgVYaTbnWXJrXj9Jb0KfBOLZ37cyyBLxQemmEiNaVQQgy_hSyFB1-QDfY3XyT7zwSNsAnROPAO7ytRU1khYi_aAeoqdrTmfAxxIX_AvPpiukBgVpaEN-xD7rRFXLWxuDr8_kEMrG-E9z3_vubE_4dk3E4YkEJ92wQvm7zo_dyuV_qAB_ZyR80eo4M1eZBH6hB69IT3Oi9T0rH8TJHY85nRADwNowWjPZlw_i8lZK-JJoGsRiCx0V6YxbN_KwTMYCvXhVOcEtODymBkwlEQXjhl6dtTVMbjgK9T_pTmmpd61MvrA6MNKLQwdWcQWaoLWNXRsZ328dtQcx1hfNLxDIMwD8lH5l14mWyLz1hi5i269RseCjCnj_AEGk1fWazbgCxa9ZkAEk1Tgx12Ylzonlkz3y1NC2PxvZMW8lAOP9KN2Me67IiWu68yq-qkEpy_7hvtY3FOWALIal_fYz7Gsgt7WmSAUQ4sSt5j4TI1iha3WtIHX0aRfm3HWVl5fEkj1kP0ktfVWT5aN85x7gKt-96LMS8L-KA5QO7an4Ld9Kjn2NIjwmb3GWvyTvrgLmZOoScHqOQOrsFckuOLYLC5NHGQpaLfCwmguB3BaNCcRy2FBiNWzUOOwAYPEem5dE3AMWorXRLBd-s-WwOC_t82dTi8H2Uf-lpVUZnfrXxZ-tJn3z-W8EcLj7Y8nKfA7Kf41HnhHHQFc0YRLKkMkm7cniNGfOcWqaYb8IXY7NlQhnIMlWChDVo2G_XB0rNUZtPFdiQtqybybxKlKxVQfLlkApizRkTeGkHhk1IAsNp0xC5jxJ_W8PzuF2RRVQ433XPzE29KfgkJRmz4EoiLNanrKNmfz5jnVbo0wHzbPs8x5McDEjyTIy8UJyq5M93TGdRLmKO2nBywMbUlLawe5HA3GwJ_nTdUJqoWVIWnpq--F3Im-FA-ohtpNfzhNzj5ejeo-tr6rNwmB_NMMZvHi2tSu1fwNjPvnDsvYhRjpooVrHxqJIW-VHBpyF0fR6zdUYLx-oe_uHiTy8Kmrh9NCtaxUA6T9WP7i3hp-VpewvPfNxhOxpsX49gqtzAbDfTZlDHROg00gAIir4TembMgoMJPQca7MjtLTDumAjWNVlrU95QDuJgrdc_2y0 "Container diagram for Internet Banking System")

C4-PlantUML combines the benefits of [PlantUML](http://en.plantuml.com/) and the [C4 model](https://c4model.com/) for providing a simple way of describing and communicate software architectures - especially during up-front design sessions - with an intuitive language using open source and platform independent tools.

C4-PlantUML includes macros, stereotypes, and other goodies (like VSCode Snippets) for creating C4 diagrams with PlantUML.

* [Getting Started](#getting-started)
* [Supported Diagram Types](#supported-diagram-types)
* [Snippets for Visual Studio Code](#snipptes-for-visual-studio-code)
* [Layout Options](#layout-options)
* [Samples](#advanced-samples)
* [Background](#background)
* [License](#license)

## Getting Started

At the top of your C4 PlantUML `.puml` file, you need to include the `C4_Context.puml`, `C4_Container.puml` or `C4_Component.puml` file found in the `root` of this repo.

To be independent of any internet connectifity, you can also download the files found in the `root` and reference it locally with

```c#
!include path/to/C4_Container.puml
```

Just remember to change the `!include` statements inside the top of the files.

If you want to use the always up-to-date version in this repo, use the following:

```c#
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/release/1-0/C4_Container.puml
```

Now let's create a C4 Container diagram:

After you have included `C4_Container.puml` you can use the defined macro definitions for the C4 elements: `Person`, `Person_Ext`, `System`, `System_Ext`, `Container`, `Relationship`, `Boundary`, and `System_Boundary`

```csharp
@startuml C4_Elements
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/release/1-0/C4_Container.puml

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
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/release/1-0/C4_Container.puml

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
  * Import: `!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/release/1-0/C4_Context.puml`
  * Macros: `Person`, `Person_Ext`, `System`, `System_Ext`, `SystemDb`, `SystemDb_Ext`, `Boundary`, `System_Boundary`, `Enterprise_Boundary`
* Container diagram
  * Import: `!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/release/1-0/C4_Container.puml`
  * Additional Macros: `Container`, `ContainerDb`, `Container_Boundary`
* Component diagram
  * Import: `!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/release/1-0/C4_Component.puml`
  * Additional Macros: `Component`, `ComponentDb`

Take a look at each of the [C4 Model Diagram Samples](samples/C4CoreDiagrams.md).

## Snippets for Visual Studio Code

Because the PlantUML support inside of Visual Studio Code is excellent with the [PlantUML extension](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml), you can also find VS Code snippets for C4-PlantUML at [.vscode/C4.code-snippets](.vscode/C4.code-snippets).

Project level snippets are now supported in [VSCode 1.28](https://code.visualstudio.com/updates/v1_28#_project-level-snippets).
Just include the `C4.code-snippets` file in the `.vscode` folder of your project.

It is possible to save them directly inside VS Code: [Creating your own snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_creating-your-own-snippets).

![C4-PlantUML Snippets Video](images/vscode_c4plantuml_snippets.gif)

## Layout Options

C4-PlantUML also comes with some layout options to make it easy and reuseable to create nice and useful diagrams:

* [LAYOUT_TOP_DOWN or LAYOUT_LEFT_RIGHT](LayoutOptions.md#layout_top_down-or-layout_left_right)
* [LAYOUT_WITH_LEGEND](LayoutOptions.md#layout_with_legend)
* [LAYOUT_AS_SKETCH](LayoutOptions.md#layout_as_sketch)

## Advanced Samples

The following advanced samples are reproductions with C4-PlantUML from official [C4 model samples](https://c4model.com/#examples) created by [Simon Brown](http://simonbrown.je/).

The core diagram samples from [c4model.com](https://c4model.com/#coreDiagrams) are available [here](samples/C4CoreDiagrams.md).

### techtribes.js

Source: [C4_Container Diagram Sample - techtribesjs.puml](samples/C4_Container%20Diagram%20Sample%20-%20techtribesjs.puml)

![techtribesjs](http://www.plantuml.com/plantuml/png/pLLjRzis4FxkNt78lco04x-uYRCYDUeNk5sn3btihX_Q8g34iyIM8ZMIgkEk_U-ZICKJBGjRaHOT3KWGUVVSSm_lpe-r8SeK6U_ezqpaH94CA6v8mSqQRysKiqHaA0p4ze6gPhLL97_5g4bXsE_NzZDo-nor9Wcks4U4mNdzK65iY4WumbyTi6jbCL6QNOvBAOnt6BeJdH8gjqmai25SO-TpdI0n92BwVY1JfUIsGfXBBXNySE6MsocHchjr_C_7qhgwYcGXA56xoUIENSYXZN6_4U20nWEttEvCAeggRNzbTXo14fqYRMEPez9IU8uDFXNmqgs0HhWx8_7xH9NvLcVzomV3yQn9iJyUpIwMRLnicQ4IXDzy6r8Nb-MlIUfoMlxQIEcTDfXzRIw3mSNbRD7aCfgFb_F-lmhqRKZzx5QxGCt6-zxwX5J-9_A4TnPRSC84ggzDvy7eSh4u_nA9lYiR8tCm4Y9fZBICM2aHawAJCegWzoGw71CK51HBKjFvz0Y2PR_NrWW-TJvTLKDcKfs07nh-oBVw_kYkC08RNs8JP-0Bnk_xQsxu1ZO-M--xbzGUMUQUVsTV0N3owD5KIB7BPA7XfKPr0iT67T50xink2cjs094a2XDYaEun0jVzyJ5VcZ71j56aLFouVs1o1CDWd1h58jHdxpIyNZantfv0y3zdWUA1Bolt211UOGJJFESiTZ7UY5xlIhEF-70mdBn-HZwGBgnonKG2p_-OTs4jCsi8uxFRjrUzqcxIwxsnNZ3bN6urb1HrML4V66uXHvbpx8Ads7MNWi9q0J_Obzru9oFxH1EVmKR934oAm6LCE9IPTO6oX1dxHGI5NzQWBNDfLGexXcZOOdH3yjobLxMLo-uQkKlBGYogxJ33vxlLxx_2-Tbv8w6LZOIwaO9xGuPPX4gdBBSxXB_NXob5X2Qb-HDcdXOHACnbbUWHzWhv3OsQTxDazktlD6IzdAv7m-DyDH8Lfy04nLlKHu9jBAXlcePQlqahXXFAenr89KKY5pCOdWrRnF9tUBrQzQRbDDaWKWq_HbmcODCt-YTtZsQBQ8un4rB_oPiglCmjHrJDoeGnpANGacDPmGUCl9U6N4cNSRUA6rw98rHL9KW117IS8YquKh2gi6Cq2y_73i-0vdhBZ3aO8rvdxsRyUUZakRJw9CoaHHIwpAoSkjKZAayxuSY2qzF9NOV0GujXDTMeGq6VhjSlLlzeUDAfpQvxW0G3x1v0bODpzkrI-LuZeRxmt5rk5IjltSWGpzPrxzbYDk-wGeJHg7_HWbxhZqQ4mD2NQyFcUCzicSAo58sC9Iz9A0F3SNymhhEe2WjENxxuJrcwtltIL8CWpMHVtUaNMeRPjcj-_znjgAfJgc1FqEox69ZOI9MvOghD4aUbjO2Q0NnRrV13t4WM1l8YuYo6M5Bqeu8PgHX-QIpVaBLG-sbJQ2QISbYwHFO3ior07RygZTFNAQCKnTlhq_fKVuo25Xd_6m00 "techtribesjs")

### Message Bus and Microservices

Source: [C4_Container Diagram Sample - message bus.puml](samples/C4_Container%20Diagram%20Sample%20-%20message%20bus.puml)

![messagebus](http://www.plantuml.com/plantuml/png/pPPjRzis4CVV-rCStBVnx3mqoOh4gEqaQukc3v67laY3W18l4X6P94ZAgRVqku-K55aofMx6MY0qOC2yq_z-l3iVzLeReaosI7lwdd5955a0nJkIfMQEtymaPJ5V83SGsIzKDQy7HUGNHaq2UwDHRNz1lbsYrYJ6WFs5iFkoRbGO6SBZ5E7l7jWLM4qKPYNnGd1JFB2NMtH2g7XWF8OxachiVQy34aD2el-Vo4GfyL0gp4Gg5Bmup5U-uvJytRh-zxPZdPo48kEKgDLu_4JNPEWY7da1DZ0EyfNlJeMYgBhs0xDA4IZH2T8kIebA2rumUZoby4M-AWn_TqgY-rYvyvQsqV71tj7KHnmTxKyFBxfOR9kXuYIz_JLGXyVkuqCTJzod2qgljC75psRPtJqydfxvBFkpeulPw5yJz6kWVizNTuByFzvpo4-9ydpIqwnPPCK9uwX-Dix1_l7PsSjjKlGCQBQuBvpH20b6G2YC4VOOpEML2TvB64NG5NalnHWv1SNYnFGUJw6nxE-vTOB7tkD9EPd6fGMAILEOYlbGcPwwgU5JzEKuToYwhDWlUiDxjk5JfAXujgg3DLdoWh-tlXJxfwUpJDj3e_hAltAOG5J-x4DjQ1DTxRS_36_vdL0Buh86rq5ESzE7nktaH7RBRcWNcKYPiiY9M9RXy4JR-hpQtHjVloDBeYF5fDc12O-pbAYRaw4pZuV30ZnDnSEQKhjoBWWdCO99a2cGIjon5FlGR4uBHQJy0LE0QiaYz7bs893AtR9J8Sm6pJn1a89n0-8EI1IXrc3pK-41MwVB9whSRdKHtCSh6nYccMwINP4mPERoyoQG8bnBeKoE4MQQSSU4I-H6jn0i2lrRw-a7lqAdP8_UdfohB5njX9yf90OrS7Veb6ca-Qp8OLIb9ZCbXSOsdigfEoMJZ3BJJZHxCVpjm_by0-gJ4aj6BPLGCU5CvzKOFDWj84whU8EAMCeCQuCgl1f0vG1iTj1PkTba-gX8bBhNhcW3Ap12eTwwLMZe4LHrwa2uN0MVtxT79sMfh8N24fMsqVDUJjDrzrGb91GI4MrRIHfs5j51D5dFbyXBGpjnBKr0Gf6Pihd19CH0GfPelwH4ZhIxb4xAtY5LxWS3QvKINZcsqpyrwYRLc_dyKx3cwVUSy-3gxHzlveEnzpT-af6Kc8uAWyjjt0n2z8f7E_0k-FXXw0NqOWpUdr_C6zW1SgghR8Yc-1SC0n7Te_cnQ7ca-bneg5TdoVB3hQErYTLJGyDIfoXZqLDiS_oVJMTrlZg5LVEdmtzayuIADjXIn8_UPEeuOh_NY5QFx_oQpvJX66yDTvqmIf7VN0qsPj9hovujqdy0 "messagebus")

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