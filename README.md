# C4-PlantUML

![Container diagram for Internet Banking System](http://www.plantuml.com/plantuml/png/pPLlRzis4CRVwrCStBVsxAHjcXMEKVzfi1RrvatUMg0jYhDqbebGf43ISTobttqKJQjIQ2FTaAAJtzXtl8S_FZoTNsY3ognp7kah9WfKc4DAIrnpCwSRC-Gi4pa90ma9GwgsQgEmUCjIiuBJNgyMp_5cIbfZHZ7xJ73oj9vKb1WK6IVuEmBxn5QJfDaMT2c5sHMSkenUOIetJ6ImHAuf-b9J6IebDrvXBBbKyEZCFIvIAeNHklwNGqJz_aAkHOfgEnZiwPeCnuXxmGPtC9wunqL7KgMaZiLZi-K4AUeLfSSe2r9Q2iSOydZXI_TK665qXCbLfihp-bpl_Cdfir68s7lsU7HsUOp5TWWfWVpJzu4wEoy_8TJviFmSWz9RRIX_Q9QJaxFpqIHaUJn-TZdktMlGzu7wsJtVP52A1XUeVxm_5Sh_mvxmpX8hZaoGUcYS9u_F9vEd_yQY7qfZP056ma8Q8oqHAorYKaGhbXBe2YBYb958GR5iPQBR2sWyzlVSBeBRwBRlXyp0Ps0tD5pAl-fLQjyOzJM-nGPkmQvXNDnVSr1RN-DFkwkjBBKfIxxZZmmpd61SvLA6MNaLIwdWbIWboLWNXRsZ368d7LLT0wsBY_5QMwD8VH0V10mXyJz1Bi6i21Qsj0qRPbR-KCXT3319xBKOtOBQS4TT2JHt2L3UxrW-jg3-3-O4Jdp7D0JUqWA6HS5PWeP9ozhjzZNxJCzFJWVlN-CrjY4kLAay_MlyiTyjSuDkrvrgGfnTMqHt86siGEBS9640HUh25U1YxzLis89c8rku3Iq-OL64V34hltLcc5796VB5YMA5QSDGP6kEwWxYJCbhbf86vFmmpt8jN2CZPsOBHbgZdSyQhXcM9KoLTB1GSgD97M3N1ORSKxbW_03o-54Rtc6EYecZgC1PpWobeDSBRL7byflHTS2Uxq1IkcO9XVG-NvdlHuqxmyH_RvuW_lqDx3DtZX0RgKZ3MfC2HHdJHg7b0oQMKkMkmTgmidKfuDgi856KaZ0CkMwNZKzQ0vUP_K4c-Ic4hUX2luUpL_VryKGcLwIgT_fOgzpZixFMxXRIsVLs0v5QBvaTc0sybvqfCku7XTjklY9Wmi-cAKkKr79fuELDih9LvCTL2yA_HRSNvSZsaUPMTYEnL9ZJdV5Klo7aVDzLYGrK9wrT5A0T7-PhIxMhoTG6er1eT9xukphAwPNtf7ivw7G6-vSUdfVO5tzgqirh-sK-dyLVRwdLhDO5_hVAMilN15hH7gUXxMUSJTkOgwxTyj7zKMz5qeRNyM-_TWEMslOFebUziltE0R4_25CDIoLpDvCtYXdIO6Hp0wy_6OqFkMQLEusEyzen2QjDdJ9JQhQY-Y9R5G05HMlDH7Q89PxEPtMMkf1rhTbNeN4rhQvtxztqJMZU2wkvpddq3m00 "Container diagram for Internet Banking System")

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
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml
```

Now let's create a C4 Container diagram:

After you have included `C4_Container.puml` you can use the defined macro definitions for the C4 elements: `Person`, `Person_Ext`, `System`, `System_Ext`, `Container`, `Relationship`, `Boundary`, and `System_Boundary`

```csharp
@startuml C4_Elements
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

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
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

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
  * Import: `!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Context.puml`
  * Macros: `Person`, `Person_Ext`, `System`, `System_Ext`, `Boundary`, `System_Boundary`, `Enterprise_Boundary`
* Container diagram
  * Import: `!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml`
  * Additional Macros: `Container`, `Container_Boundary`
* Component diagram
  * Import: `!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Component.puml`
  * Additional Macros: `Component`

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

![techtribesjs](http://www.plantuml.com/plantuml/png/pLLjZzCu4FxUNp7Q-t8dTRSlPRTxQAdeYmg7ZXEtBSS7G2iddYO6nyxP3jroyD_FiRCbRXeT813dIebgpppppEEPoKDjY395nk74O9mQnIBKR_H9Hxzb8YUAP41nGmfkrdXhffmb8aDX8BOFL3MhhIBv2qPD2iD-lxQVaTkdg3L9SCNU8mpEwuSAOqD4mX7-wO1TAuk9qknoN4fXlCFGdUYKKBbb8e4DuHex7sieKwNajaAOIouL_7JXbjifaPgxTVoFnnXTNKMo49IetMHonoxaqCQutmXmGEEUMsvt9XL5rRQ_CZkEG8bEaRQnp55fAJp71fyAUEbMI2FOdP7uRQBAVAkp_kMzuNZMfDWVZsONopOkja9G2S9llW-fYyloroHrEIr_RQJqJXlClZMNmU3YShPeSXdDnyjv_py5-ZwaVdNhimIYn928w1-kJq3b_o9FS6Un1ITCeFhMTEwDBXUByo-Hw8UoCJ878o6InaZBY9KICIawAQC8Ua-Ymp51GK6n93MT3myWMFR_sXh1Xyw7gsh8JAeJy4F37_bMtn_T5KPWuqjiuWnymVXzVyqDty36P-jzzvBQ8ylSy-_iAm1E7ZoO2YbscImqFDUeJk3Og2CQo9tPJM7D3Y2IH6523D8zHk2wFpxcIpCcc3QAb8eVzmzCZc1y-hgVlT7mSkN4U7q2mNVE0iK3NrRk4I2ym0YcUSvPx6Ay4htUbMRlyVvWE7dvXBmZNLZbYea4dlurxy9QPjOGncUthwzwfTsartjblM3AkTngA2dgigBUCTn2ZZBds0LFiUik1ONf0hwpBxlnHaRsYIO-WusI6PWKWSkOS2Wpwm9b2JFs7n4KVbk3jiobLIdi6A9XYz4DoNENNjLMBhjhv2uj2x6ejiCCd-vMV_uEvsVdZOHMDXBgHWhk3Hbc4IgTijpk4FvM7wOK4PgKve-OULn4e32NLQ97s2laDpHgtisIsRU_qv3rSheU3O_prKXKd08J56zH7mcsiQ2-QHfg_I6j64ueZtOWbHI9NCnWU3Pi4SlVuVLgrPkMqsI3I3Ny776PW4tVw5_SFPejeZd6J4ZzDs-gy3ot754rAnF6C9T2Iuvb1HymybuQSYLTnjqgRdWbZb1LbI054D1nYhJWIC6gmexHB3mVEpm3ckijC-PWZ7YTlPlnvw6JvzBgap2J5b7eChDowbQFg3pjX2CBJaydTnq2zos6rLIZ3WLzl5u_MttIyAGJpgwl1Ga7sDS3LGxEsRTBvNkDXFh2StUvLQoyTID3F5lNlIUBsRph2X56e_v52tgjFneH0aDVhWsRupspPGhBKZGobhmaeGmCn_t1kCwYAYmuVVxiix9qlVk5gOP1cic-kDClj0opRTNy6-HkGrMTKWLxX6RVnS34HghC5LDjbZWgxGNK2E3RgeuVu4QoC90N4MSnn9AY7nNCICNmIsFvXgo5sa-RGZEHbCFI9R8Vc6q1wlXLQPo-J1cbA5vVdzQd-aCKjCXuvry0 "techtribesjs")

### Message Bus and Microservices

Source: [C4_Container Diagram Sample - message bus.puml](samples/C4_Container%20Diagram%20Sample%20-%20message%20bus.puml)

![messagebus](http://www.plantuml.com/plantuml/png/pPPjJzj84CVV-rECqhVD9JmKk0gY9W6khKeVS4vzGH5QUmTdnMPtjRiEpHryzzkrZV76Jgz8hSH6YfIPyNz-EpCCVcCiqJPVSEWbB4k8k54yxKNcXWb5D5a0nMkISpl3xtRCMIOMA2oaxWjr8-fM4_MLKJk7xU6mOL-GxsTe3CamPlyWRBrgEZMcbeYC8_mRWJknqqHfLmfFfR3b0zk5nym9bRTCP71DkC7elg4orbhULWfJoQM65tl5AInUgTDQwzzt4HqU9Z8NbEZLQFH05p9i8Xws4gnXx1Qdi4wafgWtsMExuWYKc3dIJPGAjP6YPWnvAk7JueGOWNL2qfjC-_jMlk71xlR-f8qutD-Px9rkOd4JWbeGVlLxeFOE_ASDTJ3sdqrGPcKiBdurozRMti7akCsoCzq_dGx_jq2_1-hFulnKWIYn927cETIdGda-vGbxbZfnmWJgNuspktDmVFpgAILw1ZHFMFNUQQK2Ao6Hraft3URhogI8vemYc9eyufYXeA1PDhVHtH44n_sUkI2uY-uEgyqqgZnGRfhILUw7slKmJK5CEPUZ8g2Sij9UpaRhsI2cB57vRDq7vtBa9NzKZmtqZewckN6NHlrDV1CmXhJwsOF6qYQcjdS_3E_4jTGBugi65t51Szc3uB-J5zcgfg5RPAmKPwaNSIo3mQ5n_NczjJswU4-MnAIQAViInYBBET6NXmFl7Wq69JZdylQHqlXsBeWW6OAT8zEWjBnc77iG3gU38ahzW2b6lMGfjdbUGgmq4nbCfBHhDBCvWf9CM93NGD8KZG5NdneFs6EvsaHrs9KfaxVngW66IMv2idEI9CoUVLa7qaGO9RKjC9BSCE6PS8d2cWw2HQb_vIBRoS_HAxchTnVdF4zMQ-cd6eb50y9VcZE3jDWL1OokrLIkbJJOnLC7RIx9EAVCTXDDNmp--7WoMuFwhEMIKKSbTKO4CqKt-hVE1CHhbMzGAUFCiYweCYe0gXPWE477bJ5a-gH9olrhLxg65LkfqJnvL6WI48HzwaOuMyLVFdHd9rMhd8V24hLnsOjPvlnnUkeM4WfpcJwrapJPs4GF4RAUB55KZaxYPfc093AtrN23dHCBSx94zwKK2gIRM-cbelkehds_xxnAmMlFTlItGHDIlPtDFiUFFBt81_VFt_trTjOVjVwC7sGK9NP3Xy7NDWkJ4BCIwKju7t_wE6WbRENeVpWvdGNOCGfgwch8KFmh9h5CRz3-MBIwKdCl1EhrNVBYSe_PkiIQfQ59fLEsiPmfjhx-ZoVJ9b-JmgcrjyDFihM4oZ5ueaWxUyYquOgzACpMoE_ZmcUgT4nqfhkOCqfHN9xtrtRI6yUUBtZq7m00 "messagebus")

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