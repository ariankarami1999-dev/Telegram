<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/HLcs_ptFCR9u9XlF9jkPeYB_CkfX3UQrExjZRUVqT-VBL1vAgcKIbWlVLXLA_FT9_2fOVrN7kWat0Y7yirNIQ9t82_FzNEAqUX3mPcMfsTxWiu31pIzIAM5poGm5TG2xcYCsS1pjDr0GaHNiE2sT8qlvccD2TnGyopnKOyDasRI4AgCdr6Mqg6dy3hiZaH5qctAP77tEO9zXaqKZj0IRokXrxMWOwRXp-RHFKJsRuUEY3qCbJweaoDuN1796f8bS9jLk8UHTHuyupy1mTwPv6-iGzanHFdpDtuRZmXzbp5GAWnw3VN-XjbS0x0Zan22m0OO_ToSNt-zq8ubUU8_t7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 01:37:44</div>
<hr>

<div class="tg-post" id="msg-92910">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تجمع عظامة العراق يقيم وقفة استنكارية في ساحة التحرير وسط العاصمة العراقية بغداد احتجاجا على رفع سعر صرف الدولار مما ادى الى ارتفاع اسعار اللحوم</div>
<div class="tg-footer">👁️ 468 · <a href="https://t.me/naya_foriraq/92910" target="_blank">📅 01:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92909">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTLTexDJAuPpx0joYlcz3WpL4gy6aqWrdYxztt7LSpO9O9tWM6ZkBV1101QlDkm8tw-jK2zlNf9lmTjl5NdCbV9udC0PYopv2WdY_gFbbpZAuOcShvtQWlwAtzJEQ_eNnHCla58C9VNn-tv2C-j-7ILvXk71qTfHqLpFFX5GFHD_PtK2vQHS32kkITcuX1aOaPVyhF38d3FHoEh0Wk4-vnFnFM8rCenbnj0hPc4BFaW4_eJJBE0ZGJlAoWf6Avre2SINYuoC7w8lq-bPUBSgzL8TCH_aaRWSiG9je7aEJjSsO6fVNLBOPMihNIwcdGEB1EYWs5XD1710PqzeSbMiow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:لن ننسَ يوم 7 أكتوبر أبدًا. ولن ننسَ الضحايا أبدًا. وسنظل دائمًا في مواجهة قوى الإرهاب والشر.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/naya_foriraq/92909" target="_blank">📅 00:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92905">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUdabG1pq6fLXLCYCdNJPXeD03p_ckxpuo9E2c11vAcweIyMy07O0YrYbUOZiCLkHThpouaXx9P1uSFWJ_LTASFmaKFW7JJG8rEypA4_Ifx5VLYN96lPhzSp60A9bGHreHsYxj2Jf8kPJ3wMVC2jfmL7YeEw7o3M7A7ntgP6sOkVXs20_ZZMu8uqan4ZON_PbsVQC1B8oU0Z9iZsh8M-WJF6jUvAQYnXZAkymo6C2yOgWf72_-iTw3NVHhgIQOC5Nf3IJzs_jOOY6WDCD3Yc4_B4bFVOXay3GWM1b-jbOfTprjIzJoHpNztUJEyuq2Wv3CpEpbqT2SDI7JR06eVbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpMjrlXPU_YAFGRvYzzWSGyeOfJ4x2hCjkiniaeV238BQtwxgfNMx3DGxNxhf9rHiYRG5ST9k9H4CT18RyCRvEAjI9yELaIwH2CVei3KqxrCs_0P83bO5CT8uAsQ5UgQQIS9maVIZr6igGUDRyyR4tL2glGNuVkfXBjpEZCOrdQL9Jti-hnjHz_sBkus4M5YlxCzpA4aVntQWW_c7X4-y01bj8HJ_-APsNBJs2LUzo_FSQvn-r9q89469pTjwJpFgjb37cxhpYd8-hcI8B0Rbof3S_CKOfeFE9nABeKjx7ZwAroUTUWQSHf8xdMMGTpxi0stdJcFkU7eMBzqKWb2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMxykF5LPnbM-5xhb_lqy_VioT_Y3h-sTs7AndQtYyEypWFPX8hlw95mwfBLb3HPUxj1H6USEEy-N6jMndr5yyLI0UojjYdIisYX7uik_8jd219dVg_le5rT1hpzhG2QVApPTRERzdbB6cm8kwXHzZ6ly66A2vBRNaShvIyT506JMI4X21ufDRVnxJ5YYLbE1MoO4oVAYZPl0LwDyf3TVT5wPR8JNEi3FRA1IRCaOWQpnVhuMIJZxTK9sGq5q3IJVyQnh-2i8SzeIdp50jdkvPpw_b6N84xda_r05MwXGdZzEqU7q7LhYnDL_HiPr3jl8taojkhqoQfh0YjRSmeIXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeffef5d6f.mp4?token=OkAoF_v5r6vVcI8pfst4LlEI0mzE9Qe1vivLF-2Gf3XpNQV42_M6OHe6maOiWqdgTLBS32wAfTne6oV9eXDEV40XoSN-WafL0T2La4Onm48D-ropCmRTEa-t5bDvKZxymRF7K-ILKnpYz6iLvDcKG13GZbJYV6lqoFdPiS8nD0G_DtnVYLB37Ujvhl0CnSgyh40BeUeIncBY5SGY-X1tQmS1TV-uKVbjxvlJyPp23wy_2sxgi5J3KRoO0CFFquYqOmMZbiXISP2eQwBuHY5HiOWr_PgNN90oFQaIeGp3MfEzGQ8tQxZxMxbJqEJlC9qvMDbjDPld5INW5VaWwDAAAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeffef5d6f.mp4?token=OkAoF_v5r6vVcI8pfst4LlEI0mzE9Qe1vivLF-2Gf3XpNQV42_M6OHe6maOiWqdgTLBS32wAfTne6oV9eXDEV40XoSN-WafL0T2La4Onm48D-ropCmRTEa-t5bDvKZxymRF7K-ILKnpYz6iLvDcKG13GZbJYV6lqoFdPiS8nD0G_DtnVYLB37Ujvhl0CnSgyh40BeUeIncBY5SGY-X1tQmS1TV-uKVbjxvlJyPp23wy_2sxgi5J3KRoO0CFFquYqOmMZbiXISP2eQwBuHY5HiOWr_PgNN90oFQaIeGp3MfEzGQ8tQxZxMxbJqEJlC9qvMDbjDPld5INW5VaWwDAAAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🫡
مظاهرات جماهيرية واسعة في محافظة واسط العراقية تستذكر يوم العبور 7 اكتوبر وتقوم بحرق أعلام امريكا والكيان الصهيوني .</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/92905" target="_blank">📅 23:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92903">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCjCslxmMhkvouObe6EkBxzbS1a235M7vbyXv1OocVJCivogGLuvc1-Ul8xPaoeKuoNdVJ8yeJUaKsBHtWCjyAC3WIWkIueAFri2PyaQvhY1M43ye_3CuPkJew1UK5JW8uDergs-KI1-9QjD3liIcLFV7BNikaKh_QsyT2AFEpkp_sMO6FC60JS-Jq76elrdxgLt5KzAR3GcQQJK7vpSMOgq2CfDanrMTfDrqY5jY382qLgFobjKWdu86JyhiBpB0T-ww0TixVFwOg9bGGd9OJ_raXbLPL2pbsS77t18FKS4fvgXUXdmloYgQ6vCCszGBlJLxt4_yJ7mCGt5ZkJWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سماع دوي انفجارات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92903" target="_blank">📅 23:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92901">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IdIdZsO4qwmxsD8aLsWuy4QVmFvpslCHnkcxogo8syBZHL3z8SjM8PAVCrbgUnMHP0WnqoIGc9q-OecmnAn2X7xevPPg2ctW1obKHdCKodIelwj2Bt_Uc_gIlOSNo5NiMlTTxjetkVv6kbFWMUJ9xbuNesCv1LvXJ524RIL73vZRbEc0BoVUH-Itdk0Ry7uYZ5Su-l8GfEYkHbDXgL2IqDMBJeKpYWOAtjZefGunzRiIONeusMXtBTnFRms6HyUDCBvUTBS3oRfhs9ZjO8pifiKKyCGdO79DTHoA7g0PO_Xso1z5KVJI-qa3zMeyiXUUoQ1orBbFHeSGGo5oL4KSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GL2GPLEwPvsi-dPh6LI5tkx2RVneGyyTeKW_t6hfGYOeFUjWDFo-NZhoXRudoV9gFd2Q0ScYAejy1wUfFG8e0daV4sBKoWu2wRp2RrPZX7qdL5XnGqTDWpIHSnEkg4rmnC001fE2wEcMLvxh6SYrZiL_S-ESX2lbewaGxLqfdicFTKc74pQBWBJiBZ5V_7aTep_ZkukmAhelCz9kPuiggxIH0bruTtEAFRvzijKPyp7EnEKunpgsvX76qYzIBZ53liI8zCe8OFGFhV87ODnqyCVRSCKeWlap_E07DR4Vs9EBjTALkqdEZu2fBXoBdVKsLfD2PqZoJEfa-L0wPRspGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
اهالي محافظة النجف ينتفضون ضد قرار سعر الصرف الجديد.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/92901" target="_blank">📅 23:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92900">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇸🇦
🇾🇪
تعليق الدراسة في جازان غدًا الخميس خوفا من الهجمات اليمنية.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/92900" target="_blank">📅 22:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92899">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
خدمة أبحاث الكونغرس:
فقدت أو تضررت 81 طائرة عسكرية أمريكية في عملية "الغضب الملحمي".</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/92899" target="_blank">📅 22:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92898">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
سماع دوي انفجارات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92898" target="_blank">📅 22:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92897">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇨🇳
تعرضت سفينة الحاويات الصينية لهجوم بمقذوف حربي في البحر الاحمر.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92897" target="_blank">📅 22:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92896">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
🇪🇬
القوات الامنية العراقية
تلقي القبض على الاعلامية المصرية (مها سراج) بسبب مخالفتها النشر ومخالفتها الاقامة وتحريضها على الاقتتال الداخلي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92896" target="_blank">📅 21:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92895">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
مشاهد لطرد التحشيدات التابعة للعدو السعودي من مديريتي المعافر والمواسط بمحافظة تعز - 7 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92895" target="_blank">📅 21:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92894">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇸🇦
🇾🇪
الطيران السعودي: وفاة شخصين في مطار أبها وإصابة 28 آخرين جراء القصف اليمني.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92894" target="_blank">📅 21:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92893">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇸🇦
🇾🇪
الطيران السعودي:
وفاة شخصين في مطار أبها وإصابة 28 آخرين جراء القصف اليمني.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92893" target="_blank">📅 21:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92892">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhP5k4rERMiMsv0xtxve2gRk7WH5m-lWMN0klH_9X_p5Hz4RWti7iNVAl4MO5DRKKO-FWCZeDBIsiWoFMmQIC9VexKjR5zmk1rs1aURYUM03f25ZJq3SYfkbfSxUbrsD4mPG5aG4f3EiMJZrZwx8-7UsOAr589n9fVTm-ttJG_JympEw9xpkuKtyKlGYZogap_1tbuE0V4gM1kdJCWrt5vNP_XmQDgOISGDCD0MXp19-ZppiBwx0m27vQi1EcrOYNcM7iP6TOuGLfMmtx_gxp3DDYxNjVVMcS0tAw4GudrG6jopImbCIUAvVs2nXE14D7V-Swq49AnxSr5scVLfXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب حسين مؤنس:
الدولار الذي نحتاجه يجب أن نُنتجه داخل العراق، عبر تطوير القطاع الخاص، ونقل الموظفين تدريجيًا من القطاع الحكومي إلى القطاع الخاص، وزيادة الإنتاج والتصدير، لا أن نعالج عجز الاقتصاد برفع سعر الصرف، بما يؤدي إلى إضعاف الدينار العراقي وتقليص القدرة الشرائية للمواطنين.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92892" target="_blank">📅 21:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92891">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hw26Gz8rgNB6lFFij6L78RX4w_m0Qlhzy02wFRdiUreh9_Gthz8iPqHiJP3eU-rB_qglqQFeKWaLKFEaE4xKIotI3QDzEvxFnNA8PjIvAStSBxOfK47KD00a98lSmCGTBrG8mPxlf6UZIdw_X8gBYEordGzD6cJ9c262CVUs6cB7VI8Ab3iFd6ENywQnlPBMzztlIux8qfW8CnznrPSOcdVMQHbLhHkDNEBf50_bTYJhY99muhSLlBC3QrQXgY4ToF12UIcsg1eU-Ie8hGX5Ch8FLmNCIHc0wrirCnJupCA3Vc3QFaUsHs7TF6_ur7DVxS4q18Awcc_qUiYmBoA39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
🇮🇶
اسعار الصرف في بورصة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92891" target="_blank">📅 21:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92890">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d69d0e9c4.mp4?token=hoHRpRjtvUZQxR2qRcasUtgm_0IbgHWR-MuuXlki8Wp7EJmTQlvYgfD6T2rkWD71FHYrmCJdUGW25SEPOrP6T0GD4qYFOFwqlW_U_fMlJ95tMOQPgnX9_DzCAYsPFv9GL2TeUPmqzChVCjugzf6iZzwjepTmYN5WfHU8h4RJsV7tCmOZ_pU74rCnJMmjtLH3a35HxUT1Dqp9fQGbcHUcyTIC1Qd0jSvv9w-47PIQUdyyq4N6WkQwVc4AgcfOpsCOCciCsKPPrZW2-JfRNYGLAznm-EN_1OBJju0IYYtX3-tR3xpqwHU2jB0AVJg2l-2CYcynu8XrliiNpudXB4y0XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d69d0e9c4.mp4?token=hoHRpRjtvUZQxR2qRcasUtgm_0IbgHWR-MuuXlki8Wp7EJmTQlvYgfD6T2rkWD71FHYrmCJdUGW25SEPOrP6T0GD4qYFOFwqlW_U_fMlJ95tMOQPgnX9_DzCAYsPFv9GL2TeUPmqzChVCjugzf6iZzwjepTmYN5WfHU8h4RJsV7tCmOZ_pU74rCnJMmjtLH3a35HxUT1Dqp9fQGbcHUcyTIC1Qd0jSvv9w-47PIQUdyyq4N6WkQwVc4AgcfOpsCOCciCsKPPrZW2-JfRNYGLAznm-EN_1OBJju0IYYtX3-tR3xpqwHU2jB0AVJg2l-2CYcynu8XrliiNpudXB4y0XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب حول الطاعون:
روسيا لا تصدر الكثير من التصريحات.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92890" target="_blank">📅 20:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92889">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3c5f1702.mp4?token=qqwmZf5RUEySPfSByre9f6Jb4Od0crZUujS7UEJ5V0p6ClJRwcfHVo7YnEWKwkHSllS_eJLf9kTrce18Qfpz_qMAUn5JP__ILainoMooU_FiXY8X-UoI-SguQm5FsVLWlL8RPKnIep-JuWmDsc1uO6aFDeMo3z87qefwazPshcZj4FgbSjIMm1h3BgJkkZ_2xVODMzfBCLK-5B2l_TdRomxGvw3KEMmwiwPfz-AzL2sBX8jA7BCHTfCSbGCNO6xQdleJ00fzmBtrweaybM-WmJ35ZFhMKCQlgXTtJVhk3mdGqVorh2E9hN5FPfjhaTHgmKR-i5lXOjv07NhmkY7nBEGFt8Ts_ay6dGMikJyQpmPa9Fh7WVKJP2JJfhoRWl4Og7LZRNMANEjGW1DoAk-43FbxyG0yzQ8ovG8C-WYDzRJMu0j84NE7secB99C6zHSB77Hl_ISjBCr9B1QddxwoPXQfkwMW6j0pnk0zC9QZvi43ILHav4piuKiKLlwGSgzFjWSN-lJKiUNSPgyjJ6gTuu9EfiHZQ4nxoorE9_-azxLIyiSC7kYI1Qi2WPmIyBDnl4Nzei5JcDRPBr38Hj4f3XO-0JiLNoAULm0Oh-oMQbeLQ8qWJQ_PUROznuG2pbHN4Ed44KiT_aFO-YgZnuA_8gtBMs2Z5G5xUq2zqAFPuk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3c5f1702.mp4?token=qqwmZf5RUEySPfSByre9f6Jb4Od0crZUujS7UEJ5V0p6ClJRwcfHVo7YnEWKwkHSllS_eJLf9kTrce18Qfpz_qMAUn5JP__ILainoMooU_FiXY8X-UoI-SguQm5FsVLWlL8RPKnIep-JuWmDsc1uO6aFDeMo3z87qefwazPshcZj4FgbSjIMm1h3BgJkkZ_2xVODMzfBCLK-5B2l_TdRomxGvw3KEMmwiwPfz-AzL2sBX8jA7BCHTfCSbGCNO6xQdleJ00fzmBtrweaybM-WmJ35ZFhMKCQlgXTtJVhk3mdGqVorh2E9hN5FPfjhaTHgmKR-i5lXOjv07NhmkY7nBEGFt8Ts_ay6dGMikJyQpmPa9Fh7WVKJP2JJfhoRWl4Og7LZRNMANEjGW1DoAk-43FbxyG0yzQ8ovG8C-WYDzRJMu0j84NE7secB99C6zHSB77Hl_ISjBCr9B1QddxwoPXQfkwMW6j0pnk0zC9QZvi43ILHav4piuKiKLlwGSgzFjWSN-lJKiUNSPgyjJ6gTuu9EfiHZQ4nxoorE9_-azxLIyiSC7kYI1Qi2WPmIyBDnl4Nzei5JcDRPBr38Hj4f3XO-0JiLNoAULm0Oh-oMQbeLQ8qWJQ_PUROznuG2pbHN4Ed44KiT_aFO-YgZnuA_8gtBMs2Z5G5xUq2zqAFPuk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الاسواق المحلية في محافظة كركوك شمالي العراق تعاني من خلو المتبضعين بعد القرارات الاقتصادية الاخيرة المتعلقة بتغير سعر الصرف.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92889" target="_blank">📅 20:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92888">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
النائب سوزان السعد:
اللجنة المالية النيابية كانت تعلم بقرار رفع سعر صرف الدولار، رفع سعر صرف الدولار قد يكون محاولة لجس نبض الشارع قبل إقرار الموازنة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92888" target="_blank">📅 20:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92887">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
تمكنت قواتنا المسلحة _بفضل الله تعالى_ من استهداف 11 تجمعاً من تحشيدات العدو السعودي خلال الـ24  ساعة الماضية في مناطق جنوبي باب المندب والسقيّا ورأس العارة والمضاربة بـ11 صاروخاً بالستياً خلفت عشرات القتلى والجرحى بينهم قادة وتدمير عدد كبير من الآليات.
وفي نفس السياق قامت قواتنا بتتبع ورصد السرية التابعة لما يسمى اللواء الثالث عشر عمالقة والتي قامت بدهس الأسرى وتم استهدافها أثناء تجمعها بصاروخ باليستي وكانت الإصابة دقيقة _بفضل الله_ وخلفت أكثر من 30 بين قتيل وجريح.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92887" target="_blank">📅 20:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92886">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
البنك المركزي العراقي:
قرار تعديل سعر الصرف عملية تحوطية استثنائية لاستدامة احتياجات التمويل للموازنة، شراء الدولار من السوق الموازية هدفة إدخال مواد خارج الضوابط الجمركية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92886" target="_blank">📅 20:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92885">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPc5SUIyjqn2nhg5_hJHEKIQWBruzMaPPQ8IJmSYugf48Hf_7_iCFHCuzPnDh7STBbKgVkR0Zvxb5CiH29lGFkQDldab47CBcsXKUbdgi0mEOACbOOPdVMRpHLIQUkwh9q30D770YCd6onTyYvGY1ySWXynCKuTU2N6sYpaSQ2U_qR4SxOngq8G6ss-OtiMEFcOQpycEVfNc7EwilPLgfixOvoFxpdCA-i9wrukANTCCnkJGjWEJhpYClZaJu5hrzs1zxKDxLbSzoC4vFLx1gVBvjukMUlPAxmwEKb45jIAfT_T1QyNw_WEiaLSGfK7YCqQ-BrdckVjH5-0TuHAPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
البصرة تنتفض ضد قرار سعر الصرف الجديد.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92885" target="_blank">📅 20:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92884">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع
: ‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 156 غارة جوية وصاروخاً استهدف بها الأعيان المدنية في العاصمة صنعاء ومحافظات تعز وصعدة والجوف ومأرب وعمران وذلك من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وجيزان.
‏ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 1798 غارة جوية وصاروخاً.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92884" target="_blank">📅 20:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92883">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇫🇷
‏إعلام فرنسي
: فرنسا ستسحب 10 ملايين برميل من احتياطيات الديزل.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92883" target="_blank">📅 20:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92882">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cfk7Y6q3sxXrHCRu1dae8fnBzowQS53EjAZX1t01Q04iap-0o65X9buta01v7GUbLXZHuHGkH793xaIDzPBPUThZI_pagaN0J7RTO93IIisUJbZA_KuAUA819qkHCAKDoPWkKuvPzDezSv0pPpL2Z0-YXiXmUPle0aGjwI1NvO98QaTKm56QwuXgBV7VRxgQ__Cyzn2e_Z792jtOO3JNsof3qSjcJs8BR747pIuPoW3XrgHus3RVn4rsHZEN199p_tGJaEiEUgHP3bbPvz0PI_0YpIC7lYGLhvFgL1fvsv5-7Fo79odaQEoGMmOHdm6nQhxowfguf6YhquOLLPGUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
يستمر العدو الأمريكي في انتهاكه الصارخ لسيادتنا الجوية، انطلاقا من قواعدهم في الأردن.
فقد حامت ثلاث طائرات مسيرة من طراز MQ9 – وطائرة مسيرة من طراز MQ1    وطائرة التزود بالوقود KC135
فوق سماء مدن بغداد والانبار والبصرة وجنوب غرب العراق. طوال ساعات يوم الثلاثاء 6/10/2026 .</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92882" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92881">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
انفجار هائل في حيفا وغالبا نتيجة تفجير في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92881" target="_blank">📅 20:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92880">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e020a06b.mp4?token=vL2YsMNA5Qya4xf6Glb8iQL9-64ff2YzwPdkLVNm-Uj6gjLeYMz-hkfmtKMxVgCRntgM7BmwTEsUrtk_THJLbYzDPtC_NCm1ec6y-dZenub_FIHtodUKPtjiEmAZ8K8nzciESFIMgndMoohDkB03AklcI1oN-wSlz5XK7BXaeK-w2px88eHiAiC69w56zUH1jubUL8NWkAOLK86tDyIkUdb9ooLDh70w5ixdaF1K9XmT7dnw13gvZPtMOiYHzmT7SJ9m9jCKi4136j0Zxs85_T8-1dvXd1tZf_Y39L7_shRbRhKKJHVEtIcz0wkxe8STPFFuiteZ66e3M2WiQRsvpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e020a06b.mp4?token=vL2YsMNA5Qya4xf6Glb8iQL9-64ff2YzwPdkLVNm-Uj6gjLeYMz-hkfmtKMxVgCRntgM7BmwTEsUrtk_THJLbYzDPtC_NCm1ec6y-dZenub_FIHtodUKPtjiEmAZ8K8nzciESFIMgndMoohDkB03AklcI1oN-wSlz5XK7BXaeK-w2px88eHiAiC69w56zUH1jubUL8NWkAOLK86tDyIkUdb9ooLDh70w5ixdaF1K9XmT7dnw13gvZPtMOiYHzmT7SJ9m9jCKi4136j0Zxs85_T8-1dvXd1tZf_Y39L7_shRbRhKKJHVEtIcz0wkxe8STPFFuiteZ66e3M2WiQRsvpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اهالي محافظة النجف ينتفضون ضد قرار سعر الصرف الجديد.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92880" target="_blank">📅 19:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92879">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
إن إدارة ترامب تتردد في زيادة مشاركتها في الهجوم الذي تشنه السعودية ضد الحوثيين، حيث يرى ترامب أنه لا يوجد مسار واضح لتحقيق النجاح بعد فشل عملية "رايدر" في تحقيق أهدافها.
لا تزال الولايات المتحدة تقدم الدعم الاستخباراتي والتوجيهي وتزويد الوقود، لكنها لم تتورط في ضربات هجومية، وحثت الرياض على تجنب حرب أوسع في اليمن.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92879" target="_blank">📅 19:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92878">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
🇸🇦
البعثة الأمريكية في السعودية تصدر تحذير امني لبعثتها خوفا من الهجمات اليمنية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92878" target="_blank">📅 19:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92877">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">🇮🇶
اشتباكات مسلحة في قضاء داقوق بمحافظة كركوك شمالي العراق اصابة شخصين كحصيلة اولية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92877" target="_blank">📅 19:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92874">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2IngNdplm0ZuIAnHBb5RXKUiQD1IKIkKp18EUH9NV699uTIBne0rTIoZrWuJdu2FyxrgT_IzmSn9-X5O-3q6D4oC64LwbSVR8IR_I_-l2zDMM5EaagyNPOCP6YLH-5SC-S_sDQwyYyHpt3ChhvJUfgwxaF_jCWEBtth1TdC7wjljF12EXFoKSNKfkowiVpgmyPuV2hrSwVo9sbAlXMTr6-aGvVH3YhphIBN28GhLneNKJ5VyN__byiu099oUkZybVNmj6lfuo9_dhNsZJ4rPhb1qAy7s2Lx-oRyJ6stxkYRW4MgewOqZfRHdiJly9Z_jqqJOdOrVklVdH6RuYGv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmUUnMOKFfFA1GVmQL8B6o_0-yj92MhyvyzqdHuuaOX9VRht6hF3iPDWMco1kxInidYPdq-sFVlDcTbpTxAcLknUf0XqfC563ZawAoMdi-Il2x-_FgF1h9PpCTiTwC2c1kJ66Sruqp0x0KHWhRgDIpz-xrFK_j9UZq3D5GDlCQb96ttUroPP9op-Zvie6zwiQ-oeEVXuKwxd6JQrd-PDsNJiNl29SFRReupW6aJXiemY58-nKLqfrAL_qMbXukBr1VvYJg0eXGHVGhV3bzWJ_srPiPerEbwovi6lw-sFBuiwFMF-dn3kOOgouaM90Drz09WaPFNbMwKifw3kLbLuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rY3f1vYPDeM8es1qJvtwZWsHqBty_rdeguov_hkIoIeCZSZucHIypr0bDdEbd_BgZ39GFXSTkg-0gQWf-_ubtF6ZYYuzD1o2k3ib2M8kNptlHa0Ag69cFrWKBwpgFZxefYAqEICt6ZyO2cBnFzsN5iNB7MBBxJG9CLDVKThU3P9Hsc8ODAKpeUroyTfUGGbq1GBsNLpcR-FD5IxQqmRJpiHiHfTDy3A2Y-tfXM4LDzMxwoFVKmIigbqJOzLYDkwK9N3wIPCxcmvDXwoqRA4MhSan0FAcDqzqrLgjoo0_3s6wmf1akzidR6yOBJPD2XhZ8Ei4oLDcQ-EHfGXt-am8mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر:
فنحن نريد بناء وطننا بكل حرية واستقلالية بعيداً عن كل التدخلات الخارجية شرقية كانت أم غربية.. شمالية كانت أم جنوبية وبلا فساد وبلا تبعية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92874" target="_blank">📅 19:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92873">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tsz--oyFHPc5l1mSnwpMmJAJAVgkhZQkJQG1tPNbP3OZtTrSTOtVEohdGM5DkptWVZgWgp66dxfhdSsMlxCu0Z-iCaM83V65FXoX9UzZeBlG8bmRt5NCPKAnJNOVhkwSz6c1UUs6bkL3vsn7zM6arombS-g0ot00ipPPanu9ytx-veYrPgm3onqizTzFtyrbq_7wNUyR7-_IzdizipVBZScra20rGHnBZ8Xs5oW7UurvqtJO45IK5jsfxo36NtYG0eyeEC1MKJAa9Yk6FxepJfht_wchUjwAoEzmB7DOLai_iOzhGjonHI7q0KaUI29D05bDqZYS7_cZHVI-M90csw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورصة العراق للمواد الغذائية تشتعل
طبقة البيض الأحمر بـ9 آلاف دينار، والأبيض بـ8 آلاف دينار.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92873" target="_blank">📅 19:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92872">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
النائب عباس المالكي
: أكثر من 25 بالمئة انخفضت قيمة الراتب نتيجة زيادة سعر صرف الدولار.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92872" target="_blank">📅 18:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92871">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
ائتلاف النصر:
رفع سعر الدولار مقابل الدينار يضعف القوة الشرائية ويرفع أسعار السلع والاحتياجات الأساسية ما يزيد الأعباء على الموظفين والمتقاعدين وأصحاب الدخل المحدود ويهدد بتراجع مستوى المعيشة واتساع معدلات الفقر.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92871" target="_blank">📅 18:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92870">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573cb70c63.mp4?token=C8l2ylnT3i8shSkV6bbxw-c4VVz-hqPm-PqeWsVKQF1lo9DcuoeeONcIp90MpGyRKjFSWxtKVUwuBsZYk90z8FEToQAEqObPAeC4iyIMSelyJ7n5KnefZ08mVGblmxdgXWP_lfScLHqHdhdLfxzXwE9T3qCJ6yFcQu1sYGJBNZCjZBML5mAFTiCjgqCkE1qR923PKUWXkyh31awIz2m6JmETqdftwKJCykctQzNrwsnrcT_Pq-GAYmf4UT5LPhndBE5sdoqTBLn2OLEJD_13GsA_s7k-E1IAvJyK9GeLy4wraTkaVk_GlNaIKRd6VRaJnDcotZBxERMtXJOuq5B8NzLfSifiApqKcKc6YZGtzbAVKI4nwcjeDc3ikIYwMuunQ6vts1sSk0z1SRjQrQhREzMiGgoDG7dHJRJ4U8E1P9rROZo0G-8zi84V6ioql28ZvDDOx3Dt65VCEDCj17Iy_lYXiwvZN2VtdBvIJ_mBxMx6vtFKi1_a7Ma610Q-0haqGx96ADld-dksMXWmJbczlcBoRsxssy6AU87xyy3mcHzMfWIqbAeRguDkWdgVfB4YOfRYErOh5hHpFOjnPx5m14HC9I9TJlIQ28ItLhbD9y10O1QwlX6GzD5HybDL3v7-sj2StKyb2CdjR7fcChRWcBNzReFw0EVGiebQdL25xxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573cb70c63.mp4?token=C8l2ylnT3i8shSkV6bbxw-c4VVz-hqPm-PqeWsVKQF1lo9DcuoeeONcIp90MpGyRKjFSWxtKVUwuBsZYk90z8FEToQAEqObPAeC4iyIMSelyJ7n5KnefZ08mVGblmxdgXWP_lfScLHqHdhdLfxzXwE9T3qCJ6yFcQu1sYGJBNZCjZBML5mAFTiCjgqCkE1qR923PKUWXkyh31awIz2m6JmETqdftwKJCykctQzNrwsnrcT_Pq-GAYmf4UT5LPhndBE5sdoqTBLn2OLEJD_13GsA_s7k-E1IAvJyK9GeLy4wraTkaVk_GlNaIKRd6VRaJnDcotZBxERMtXJOuq5B8NzLfSifiApqKcKc6YZGtzbAVKI4nwcjeDc3ikIYwMuunQ6vts1sSk0z1SRjQrQhREzMiGgoDG7dHJRJ4U8E1P9rROZo0G-8zi84V6ioql28ZvDDOx3Dt65VCEDCj17Iy_lYXiwvZN2VtdBvIJ_mBxMx6vtFKi1_a7Ma610Q-0haqGx96ADld-dksMXWmJbczlcBoRsxssy6AU87xyy3mcHzMfWIqbAeRguDkWdgVfB4YOfRYErOh5hHpFOjnPx5m14HC9I9TJlIQ28ItLhbD9y10O1QwlX6GzD5HybDL3v7-sj2StKyb2CdjR7fcChRWcBNzReFw0EVGiebQdL25xxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
النائبة هيام الياسري:
الشعب خلي يحير بروحه.. اطلعوا تظاهرات سوو اضرابات سوو اي شيء!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92870" target="_blank">📅 18:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92869">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔻
تنظيم داعش يتبنى هجوم قضاء الحويجة في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92869" target="_blank">📅 18:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92868">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
🇾🇪
السيد عبدالملك الحوثي: لم يقف إلى جانب الشعب فلسطين إلا المقاومة الإسلامية في لبنان والجمهورية الإسلامية والفصائل العراقية وجبهة الإسناد اليمنية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92868" target="_blank">📅 18:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92867">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
📈
شركة شوفوليت وكيا و تويوتا تقرر وقف مبيعاتها للسيارات في العراق بعد قرار الحكومة برفع سعر الدولار .</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92867" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92866">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📰
وكالة رويترز تزعم:
حزب الله يتلقى 200 مليون دولار من إيران لصالح النازحين اللبنانيين، وهي أول دعم من هذا النوع خلال الحرب. التمويلات تُرسل عبر وسطاء يتقاضون أربعة أضعاف الرسوم المعتادة بسبب المخاطر المتزايدة</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92866" target="_blank">📅 17:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92865">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
ارتفاع كبير تشهده اسعار الذهب في الاسواق العراقية بسبب تغيير سعر الصرف.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92865" target="_blank">📅 17:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92864">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">المواطنين في محافظة اربيل يقومون ببيع الدينار العراقي للحصول على الدولار خوفا من انهيارات جديدة في سعر الصرف وارتفاع الدولار اكثر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92864" target="_blank">📅 17:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92863">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">النائبة نورا الجحيشي: سنصوت على إقالة وزير المالية ومحافظ البنك المركزي خلال جلسة غد الخميس في حال عدم التراجع عن قرار خفض الدينار مقابل الدولار</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92863" target="_blank">📅 17:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92862">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
رئيس البرلمان العراقي هيبت الحلبوسي يدافع عن قرار تغيير سعر الصرف ويقول انه سيوفر للدولة اموال كبيرة ستدخل لخزينتها!!
ما لم يذكره هو انها ستمتلئ من جيوب الناس</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92862" target="_blank">📅 17:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92861">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Txuy2zuNF8lblYtEgH8uLTQpr-_i5I80lHLM2axsutZhUrTaG83LkwUPsoJhpze6-54aqyN-20X_Fmnb_bxb2pF9FZ6fOEHAV-F7f5O2FzTRfBd-XvMLdJLZ6oeokjkG7t2N0nIUNj57he6hxtM-T3fpbyfVXVM2Ewp7IUiZAcXTGYgJnDy8WVEeC7OX653xjI_FF19G_8_aIf0_SXiEeOWYngKhLL4evBaNQIdbbrtGNZ0I2TNUS5odISvdWBo5yjjmrtCxPZkVV9AjKDpxV48ax7JcOlCCdiMrmSmPaG2sUe-JOCeWKA6Nf2dNfspZygxpFftzQvfYdrlQZR72mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مواطنين يناشدون عبر بوت نايا الفنانة العراقية همسة ماجد بسبب الوضع الاقتصادي مؤكدين استعدادهم للخروج بـ15 الف في حال ان العرض ما زال قائما.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92861" target="_blank">📅 16:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92860">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇾🇪
🇾🇪
السيد عبدالملك الحوثي:
لم يقف إلى جانب الشعب فلسطين إلا المقاومة الإسلامية في لبنان والجمهورية الإسلامية والفصائل العراقية وجبهة الإسناد اليمنية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92860" target="_blank">📅 16:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92857">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DlHXBKzU_OIu7GHFHnBYdQARMlDk_uNtS6ai4tkqacCNcLp8hOCwNtwX_uAU7hF8yLdnregqnv6rzbtqPRRq7Qf_UdVWwBV5swSFibJnNU0TZqY_ZmD9DQQMa9NGsBQKOygegZvjlcXkCPh5E4h4KSPfUohE5Y3s7hy2xobOiYaWziWEXfbQn7vFkMFAZE-rbr_L0HOBJSsc1N5BHONNv7sFrPSDUWAKBTJ_MYqpMM4DpeMcSUyLI1Gtu5eyQc2gX5i_WcXtXT_KmtMmmNM12BVmWCEYrkA0AY929uQ7UM39b8fF6P4wfgjPxjm47p70cfEO_d1E-8CTAq8PPqFSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ECDdNfI8-wmNB9lKkbMU4N7Aa8m8kfEloDJ_mJ4tpMfQMkPV_b7wyfuN2Y_lSmUdjxsESQytx_5Rl1Yi9MbtibrtOurgci7LDQRpZAJPRA-_3DIbZGGMPFVV8PHliL0aCCOAHpalzmDr8QRzSAg3rUB__5gyviXIkSPqAP23R13eLfAF_HQ_jtw4Vq6I8ATJmJMb_qnVYMkTNpAgbxBGj_uy8nEXD02bkFHF6gBnliF6cacSw9o9Ok7lsTmlJTYYpp1NCejByTiYMHBqbaaqwuebWVMUVWa2JTht-hdfazlIzfaOCaXlp1eDhEaHYNPsFwWYjs9AC4rahV7UlvMWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/np0OMAPjgkxo1_jP6AH5Yt3_xhAr-jIHKE2_Yw8rildWauXFn2VhPiCCB9KTUey8BchPQH3PPpliDZY8IYGWC3T68t5Aj443sAjOqAo-oq3nws67sWn68OzVsGr4-C7jszlDwxwKrIOtZsBnpvLyE6U29r-0JhzWt3VpzDcdwefmXEjUNDAaJPjVDCw-Fe3pE6Rfdhg1y6wG-8ITIJQvMRk0hRA7Ah9TzUfa3c_kESkL7d21ANee0u9dg8Ubw5YxRw1pXo8ig_P_9R1cKUoaEKXZAjn2nzNW6IWuLNRnQv4tc4OuhxnLv4nB4jcjp1jHDKMJgVPdOzCj5djCn33Y6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الاسواق والمتاجر والمولات العراقية خالية من المتبضعين بسبب قرار تغيير سعر الصرف</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92857" target="_blank">📅 16:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92856">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kic3WVHpt6S0huBwVQmSgEz33JKlo8JQuBqUTDqBKgj6MdR3upyxkdrlXUIGR0M2qDoB3_h-hHPpWL1GqPUT_ThpmqEYTdtxWNSp7oahUBYuU1scFU4OfEOUxffYA8KwPRhpMxqD6Gk7S86LT8-X_aLARnScixHeDpb-r_GAeSvy_qshYWkkA6rN7FsSP3m4ijZmE-KrPRHCP_xmf8ph9YQE1aoKiUlVEmGDwHFokFsbckJENSPjs6Aob5T6lI74RI8GcU55ehLH_qbPILPnxgnM3DYocXPcAxA3bRhCS7PGt1JLQxZfizcFmfXBBnvf_xhLbeGtF-fs4Kpid8j03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المطاعم العراقية تبدأ بالاغلاق بسبب صعود الدولار وانهيار العملة العراقية وضعف القدرة الشرائية للمواطن العراقي</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92856" target="_blank">📅 16:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92855">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c11b7739.mp4?token=gUYvnEqyyY7GcwqhgfSX8hB2wXDa0y0C9yD96dGOnZoRQ-ageq_5lZuUUKGoni2HbD8xWlh_mkYtcK2HbEaiyHchh-iVm75y_1X8k6abInlrh1RDu-61YhOW0TH_JcioeN44TzVEbiKZrqF9yzDPH4VGasETn3gYnwdlPK916r6etks_nxk-Re1IKeEbvqE3oJ0HK3wuZIxzi6JYKqOrgr81eeEsqa4iQL4xwpHf7yBcrdtJm9H-GF6GSFQ6_MHZDWdMLzKz6bOt_fOcQkDOx7LwnOS0f213ocNnPqUIj3yakKOjUE7rno_NQw__kPvyvlPNv-mnZvu3yINsqZcpFhkUx64zYICqA_BVBewZrC8PZrj5v8CifzjIEBGJ057oQ2NRUwCK51wjTcqhiJyZRJNZZ6QLuXrzVvi9rDa0jgqQJ98vOgKcs8YCt6dDE3_k0zKA_GkCxzPOAO9cSIWOCkZI7o3V6H4Y_b9yktv7IGH2i3fgEwu-Qsoess79OhAZTkSIjOL4IJsHP2DIgTqxhQuYCks-1iyxSk4cgtI0mwqGHb6qcDdgJjlNQhUWdh_ITTgoWHmkxTC2wZoQSbJ8s0xoQOau6s-8LStq4wrNXiIqoxA3MeKuw-P5b6RM6t94wLpCotlpu7edgjyKwIf7CU23QgZkJ3EF58FU0mFY4AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c11b7739.mp4?token=gUYvnEqyyY7GcwqhgfSX8hB2wXDa0y0C9yD96dGOnZoRQ-ageq_5lZuUUKGoni2HbD8xWlh_mkYtcK2HbEaiyHchh-iVm75y_1X8k6abInlrh1RDu-61YhOW0TH_JcioeN44TzVEbiKZrqF9yzDPH4VGasETn3gYnwdlPK916r6etks_nxk-Re1IKeEbvqE3oJ0HK3wuZIxzi6JYKqOrgr81eeEsqa4iQL4xwpHf7yBcrdtJm9H-GF6GSFQ6_MHZDWdMLzKz6bOt_fOcQkDOx7LwnOS0f213ocNnPqUIj3yakKOjUE7rno_NQw__kPvyvlPNv-mnZvu3yINsqZcpFhkUx64zYICqA_BVBewZrC8PZrj5v8CifzjIEBGJ057oQ2NRUwCK51wjTcqhiJyZRJNZZ6QLuXrzVvi9rDa0jgqQJ98vOgKcs8YCt6dDE3_k0zKA_GkCxzPOAO9cSIWOCkZI7o3V6H4Y_b9yktv7IGH2i3fgEwu-Qsoess79OhAZTkSIjOL4IJsHP2DIgTqxhQuYCks-1iyxSk4cgtI0mwqGHb6qcDdgJjlNQhUWdh_ITTgoWHmkxTC2wZoQSbJ8s0xoQOau6s-8LStq4wrNXiIqoxA3MeKuw-P5b6RM6t94wLpCotlpu7edgjyKwIf7CU23QgZkJ3EF58FU0mFY4AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الشركات والاسواق تواصل الاغلاق في عموم العراق بسبب تغيير سعر الصرف وانهيار العملة العراقية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92855" target="_blank">📅 16:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92853">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSys5aiGRk7fnwRmA1W3wW_SnQdI81jarGXztdXege7y0H4vZvImHwwCaqFMFuCi7k2j_kgMrbPl3xrEoOdKBIM0q1gUwM1S9Z0stSVL1tuxDuk2vA1K5CXZC3FyDVIAqN952j3glFIqeH7Qssup1iJoPTpXbsZq_vnAMP_UFhjJ-hysHhhQbfV9hyPopThYKNlzSvMQzJuep55mSEB3IRrwCM7of-j7d2beLntVbrOBDcNsGRRlX05TyU6HKC8v0SJcRFrIX02f6pCD2DItRaNL6f_S1pequOGV9x77A1EMSJ9lr3rXwVhoFzNk2WuMgyOpYMcrV6erQZyqFXGGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQvD1gzZm3DX8B8vcxKUH4MPBtXY14BgEElfA_AiBmvKhBlKFC5a7NOaW4i56nQee-jOr_4GKXDgB0zeFdoAYxAEHOrQDEn_jlQ3No3LFu0AH31xnUzmhBZPLcVe381cyOfrdTM5HzZR-zDgEV8cqCVvFgwPGMSxfHHxKZ70_EyNPxAly9yS3G8RDo8FlDUk4__lGtBUt0SwNuLyu55gEGytUPkjjX-BJF3xjBxoNbbBYpCAerQ3fFwEfYovqcwwsYmY5Zzy75cu5QUNCMDjVH961pvLdcs7m0l5Xqw6qs4__s7-218T5k1JATuoOtisfmVKqD5-gqSItgY7BNABLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شلل تام وحركة شبه معدومة في سوق الحلة الكبير بمحافظة بابل بعد قرار تغيير سعر الصرف</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92853" target="_blank">📅 16:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92852">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فوضى في مجلس النواب رفضا لقرار البنك المركزي بتخفيض سعر صرف الدينار</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92852" target="_blank">📅 16:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92851">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بنك ستاندرد تشارترد:
الاحتياطيات الأجنبية للعراق قد تتراجع إلى نحو 60 مليار دولار بنهاية العام مقارنة بنحو 100 مليار دولار في بدايته، إذا استمر استنزافها بالوتيرة الحالية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92851" target="_blank">📅 16:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92850">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تدخل مركز مديرية المسراخ بمحافظة تعز.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92850" target="_blank">📅 16:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92848">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">كتلة حقوق النيابية تقاطع جلسة مجلس النواب احتجاجا على رفع سعر الصرف</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92848" target="_blank">📅 16:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇱
اعلام العدو: سُمعت دوي انفجارات في منطقتي بئر السبع وتريم بعد تفعيل أجهزة الإنذار في المنطقة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92847" target="_blank">📅 16:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92846">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انباء اولية عن تفعيل الدفاعات في قاعدة حتسريم الصهيونية</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92846" target="_blank">📅 16:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92845">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انباء اولية عن تفعيل الدفاعات في قاعدة حتسريم الصهيونية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92845" target="_blank">📅 16:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92844">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
شركة كي كارد:
اعتماد سعر الصرف الجديد للدولار بواقع 1,520 ديناراً لكل دولار. يبدأ تطبيق السعر اعتباراً من اليوم 7 تشرين الأول 2026.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92844" target="_blank">📅 16:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92843">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة _بعون الله وتأييده_ من طرد التحشيدات السعودية التي حاولت التقدم باتجاه مواقع قواتنا شرقي محافظة الجوف وتم التنكيل بهم واستهداف كل تجمعاتهم بعدد من الصواريخ الباليستية والطائرات المسيّرة ولم يحرز العدو _بفضل الله_ أي تقدم، وسقط منهم العشرات بين قتيل وجريح وتدمير عدد من الآليات التابعة لهم.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92843" target="_blank">📅 16:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92842">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">كتلة حقوق النيابية تقاطع جلسة مجلس النواب احتجاجا على رفع سعر الصرف</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92842" target="_blank">📅 16:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92841">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">كتلة حقوق النيابية تقاطع جلسة مجلس النواب احتجاجا على رفع سعر الصرف</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92841" target="_blank">📅 16:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92840">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اشتباكات بين الجيش اللبناني وعصابات الجولاني على الحدود اللبنانية السورية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92840" target="_blank">📅 15:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92839">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX8RczLNaHAFRarzOCfbL8kVJTFxheCkw53WjeYMQGD-bBdT-3NGMT_Br2JkMaHDIhIWrg4KePxkrMWu0hjI0rpjnli8LwrRnAbmYPKVmNTgFictlDJ8EVMqpXwbF6fVaqoCKEcwHOusjLfaR3LwVmRIFuoK1JWjUGNzT0NZus9AhRvntIPMPIWW7Y81-3L6W9sGwfex9zCV2USIozQnDkLFN5i60f86VdY6yxGJUoIk0WopBEtCWEjxkxmQD4OWVsbumHvYT0vLH-eflfmupFm0dIowPuumC3WpJBrjHir671u-RAn71un_bbf3cCkfDq7yW39rMKWNoYU_ou6C4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
خلال محاولته اللوذ بالفرار..
القوات المسلحة اليمنية تعتقل مدير عام مديرية المعافر أحمد هزاع الصنوي التابع للمرتزقة بعد تحرير المديرية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92839" target="_blank">📅 15:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92838">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989c9d3101.mp4?token=EP-zWh8KkZlwXJyt4gXZGljTo6_P4-KnLYiVLw-Lx7ow_xzRJM39ybk66gA1cRk9oE7idaphFe71A5QnxgMVGiT-xqCeUo0iWkoIttU8isxC3Al0UhV0d5XQ7ppZ03ZHHjfJHig-0OaG1DwLyI6fyBuTe_PQ_VUnjysklPXzgO7UXFHjqMGdezgxgMDIUQIA9k2CfU5_VamuSujtBdt0SUaiTNeWRlpVh9DrYQpHh9mzH44czAeuIqo5E3cGlxoK92f6P6vw-0fPOmYKk_UaPdNgRCnsY5Hy5DTPLFslodoX6QucdBaKlxE8B1vh3wD7u9km723kW7dQHaoI_aeJoqbg59dYPl284hoAtlW5oMDkHli52NsoPpA-kASmuQGmjAtkppFMnCtrHkgUZOC0vtcyUfvAgq8Qk6GpSZ3sfZcNAhQaDPXrM0NSo2xJXuFzCN08PzmgRmfpb2wyuVmdpLtD-UJytbr9XOWE-BD-9hOWMSovZhcnqefz8mpAWqjpk7VYlOUWhFJZok_xFLA9Lm7ZdwYNaLF5ODpJ9H1D5Y_xgQPstZjWjd4iobljtN-4ge4pAKzlITRnHMRSZ34ZqaA_L21Smca42gU2nrKimCdF3rkWZxj7QYbRkSxLCWx2UnHUS6Ebz8B2tW42MZ8wUwG8iFMRmCzMBcUTzOp_gXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989c9d3101.mp4?token=EP-zWh8KkZlwXJyt4gXZGljTo6_P4-KnLYiVLw-Lx7ow_xzRJM39ybk66gA1cRk9oE7idaphFe71A5QnxgMVGiT-xqCeUo0iWkoIttU8isxC3Al0UhV0d5XQ7ppZ03ZHHjfJHig-0OaG1DwLyI6fyBuTe_PQ_VUnjysklPXzgO7UXFHjqMGdezgxgMDIUQIA9k2CfU5_VamuSujtBdt0SUaiTNeWRlpVh9DrYQpHh9mzH44czAeuIqo5E3cGlxoK92f6P6vw-0fPOmYKk_UaPdNgRCnsY5Hy5DTPLFslodoX6QucdBaKlxE8B1vh3wD7u9km723kW7dQHaoI_aeJoqbg59dYPl284hoAtlW5oMDkHli52NsoPpA-kASmuQGmjAtkppFMnCtrHkgUZOC0vtcyUfvAgq8Qk6GpSZ3sfZcNAhQaDPXrM0NSo2xJXuFzCN08PzmgRmfpb2wyuVmdpLtD-UJytbr9XOWE-BD-9hOWMSovZhcnqefz8mpAWqjpk7VYlOUWhFJZok_xFLA9Lm7ZdwYNaLF5ODpJ9H1D5Y_xgQPstZjWjd4iobljtN-4ge4pAKzlITRnHMRSZ34ZqaA_L21Smca42gU2nrKimCdF3rkWZxj7QYbRkSxLCWx2UnHUS6Ebz8B2tW42MZ8wUwG8iFMRmCzMBcUTzOp_gXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية وحقنا للدماء تقرر السماح لقوات المرتزقة بالانسحاب من محور تعز والمرور باتجاه محافظة عدن</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92838" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92837">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
🇺🇸
الرئيس الايراني:
العائق الرئيسي للاتفاق هو التشدد الأمريكي.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92837" target="_blank">📅 15:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92833">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmgRwwRK-hodDKn1Roas1SV0JwAJ5cIT1lcsF__igUBsIpUW9-62fJ8Tq9WK4KddQZoNdjvhhRM7oq4WosgW5GhmFejXwsoU20Zy40hbZMegCSxr6njZOszMp3Q9XKRTA7MZoA-ULFCd90aZbCKPq-Uf3iarK26z85J3leF-yHdjzwA30z4smY5msr5MUkeHNURdlDEDLS7jT-2daoctjwcMlQ2TxK6xtDdH8N4byJigRyRqaKnpb_aI9rAPR3aZOM8yiHTnd3LLvL0QqjwZPR8a70aRMHWQpEHj4FsJHYK5khjplFy7kZMhpQEbWnTLxhqgy5SlGoHbS_NTWGFeew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWEGpX_D3zn5vsWpDuZSw7667MIxBuift4p2KzC4_lcQ0v1WQF8CTbh_8sUNjRNrjUZTYhOCAHqKqzShmIufmDYGd9Qe16HCQKh_OroZwEW1rJ4MUbA0YbsnG4gtu69gDCFdpEi5J51yjMyKbjctV9On2Sm3bcGyIF0ySXvXBJHmvemzKrWcRNsWtcobRKT9pveXLQp5bAPt8I-rN37IeiakK7ddcCFKP96LXbhjYx3PF_QrYviTDVYmkl89PO1sxXVK7eW-yPitBIF2-7IZx-M-pvV0JH7cWBugpFXJvBEXvJzyYlXPBZMPXp3gdbj7uklP85haZSdnwp7k7FO0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKyul2q3RN6GDqzg96sWylH86MAAUrAqqKCpB1yi9z6S_-Obnwa771yIl2GU0WeJDo1wY-CHQhhVD4JvkvCMZBRhFOEM2v64kMkzNw_u8UPBzTcPLngeo4r_BSDU2BICyuNa5BhOYvmV7bUQbOmBwR550jJUFI0yHM7t6avEazqgF1boOagghpDHjBYeIt35J83nvsvH3LRwG9WUAewlm9pN3d4iVRLNWO7xAV7HOfMXWOG38GTfNCYAIW_ZivwwnD19Bax6FmTCjxaCZ6FnSXaY-0kRQOxT_MAL9sPxHuMUlqA2fedSFdMnNOfuBNy5qf2wr53uI7VdQ9KCYS7ovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3oaox_rs1QUbCcBUvP4AbINOzXAU-ebbP328TFXBCtHyjH8iEwRrvnJzVfA2EJUbHp3k-LsCXXi6yD3NdCDaR-MrLqqIIipBdv9TqbhDteXqPcKa7ivm5wdrox-ig8wUU7rsdejt-DnOwTjMIc1OFo6t8bU5Muv0-ZKUeLaY9VS1GX_Oid50IkDsIN6HEPPXq3PaML8BaXKuoqFuUwgQaJ9z3o519PLALs0a_y4CNqNGsxM9in9tDi9K6XBXFqPOeCRlvMZ0HYXTuV4MZ4NMSBdDtaPu8dd3DhOe3nsxsQ1pq8p0CMb_b5kqxzXbazeoim6KCvxm8APMM6-7iVNGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدأ جمع تواقيع نيابية لعقد جلسة برلمانية طارئة لمناقشة انهيار العملة العراقية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92833" target="_blank">📅 15:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92832">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMPPb5qqR55K5LydJ6NY_bNe8JvfmOXn5VBambTCq0mWCDxp5WXlBOqyY-91lXk0dgffEgYhYQ1-f5dugQIl8A5bD7Iwybvqt04tgjGgM03dT-4R6vQ2DVT4rEN7r2LeQRy5vZOw7jtnoKrzSCA1EXiZ3ukycs7DLsNN6JSROkUK3Lxg38Fhho71m-XtugQfEaQi9UpFlA9uxxHhj7_y_MSE2_m4dtA7di5zPTCFEwOaskWh4U7M6TLIZ_iqxnHez6hrKA6YY0pO584v24Zp0hiClnEFJ_1OfYMJJ6FVWaXAYScviSh7hCGUf1Uy3yK9pp6BGIPfa33iY1ukr70SxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السوبرماركتات والاسواق الصغيرة تبدأ بالاغلاق بسبب ارتباك اسعار الصرف وانهيار العملة العراقية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92832" target="_blank">📅 15:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92831">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fba981c1d2.mp4?token=Ph5CpWk8435-s3ASHrpOvbT5iK4BkUeth9ahSpR_cu4laM8yXxWv0yHhZtNEuSn90efdhepLNghHRDoN3BetwCUJRHkUdXSrQ6SpHOxH3Pd3Zndhol_1IE0ALCzlSQvELnJdsKBEaD7HIc1f5X6tgNAFijMy1tLEZ6KDQvVvjXN0eg6vKp-viIvYfx2nAAhMjIH-6VRhMvrqrZ85D02kVe5pe0CJzA9B-9Y4XkcmFmtTabU9d4POWtfOXGDbRGaEgvyfTjX456PQpOANU4qqCBlhpX8papZ1Y1rWB8ujXbhjcI6olKQqkv-zpmgG7vSbkfzhEUT1g9vRLEBCNk0X-pJ7miCURatfPdzMHjVHbCaZgVvp2bRzxepLU8ylxEfpJOZ1K21VrPTHexqU2kKdP9hrKxbXtpwIxT9F0TMt4ggOwfRQg2zpfTQEyPNovqR_V9meAGnpfIsZ2EcbpoB1mIxAtr6KOPgIWu0CQakFgponTjiCM3klo1IvxagXqT-KMgezhIWr6QC9dc_udq5NO9HgHRVsMPIrIftr0BqMLiXpaciZhPGeV5DCr-Vmjgu6Jo7eqd78RrnkqqAw-FEB0JfU6yCw-hhxK380CejSNgO-0lVCnYStS8oAcWVATzarz4hpigNjTmShrpZflQQfuB5uCobsGw2cS4Fs2kEI10M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fba981c1d2.mp4?token=Ph5CpWk8435-s3ASHrpOvbT5iK4BkUeth9ahSpR_cu4laM8yXxWv0yHhZtNEuSn90efdhepLNghHRDoN3BetwCUJRHkUdXSrQ6SpHOxH3Pd3Zndhol_1IE0ALCzlSQvELnJdsKBEaD7HIc1f5X6tgNAFijMy1tLEZ6KDQvVvjXN0eg6vKp-viIvYfx2nAAhMjIH-6VRhMvrqrZ85D02kVe5pe0CJzA9B-9Y4XkcmFmtTabU9d4POWtfOXGDbRGaEgvyfTjX456PQpOANU4qqCBlhpX8papZ1Y1rWB8ujXbhjcI6olKQqkv-zpmgG7vSbkfzhEUT1g9vRLEBCNk0X-pJ7miCURatfPdzMHjVHbCaZgVvp2bRzxepLU8ylxEfpJOZ1K21VrPTHexqU2kKdP9hrKxbXtpwIxT9F0TMt4ggOwfRQg2zpfTQEyPNovqR_V9meAGnpfIsZ2EcbpoB1mIxAtr6KOPgIWu0CQakFgponTjiCM3klo1IvxagXqT-KMgezhIWr6QC9dc_udq5NO9HgHRVsMPIrIftr0BqMLiXpaciZhPGeV5DCr-Vmjgu6Jo7eqd78RrnkqqAw-FEB0JfU6yCw-hhxK380CejSNgO-0lVCnYStS8oAcWVATzarz4hpigNjTmShrpZflQQfuB5uCobsGw2cS4Fs2kEI10M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اغلاق شبه كامل تشهده الشورجة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92831" target="_blank">📅 15:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92830">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
مسؤول ايراني رفيع: يجب على الولايات المتحدة أولاً تلبية شروط طهران قبل مناقشة الملف النووي، اعتراف الولايات المتحدة بحق إيران في التخصيب هو الخط الأحمر لطهران</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92830" target="_blank">📅 15:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
مسؤول ايراني رفيع:
يجب على الولايات المتحدة أولاً تلبية شروط طهران قبل مناقشة الملف النووي، اعتراف الولايات المتحدة بحق إيران في التخصيب هو الخط الأحمر لطهران</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92829" target="_blank">📅 15:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
مصدر امني لنايا:
مخلفات حربية على الطريق الاستراتيجي في محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92828" target="_blank">📅 14:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92827">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">البنك المركزي العراقي: قررنا تعديل سعر صرف الدينار مقابل الدولار لجملة إصلاحات اقتصادية. تعديل سعر صرف الدولار سيحفز القطاع الخاص</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92827" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92826">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مشاهد من الشورجة القلب الاقتصادي للعاصمة العراقية بغداد بعد قرار رفع صرف سعر الدولار</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92826" target="_blank">📅 14:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92825">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
الشورجة.. المركز التجاري الابرز في العاصمة العراقية بغداد "يصوصي" بسبب انهيار العملة العراقية بسبب قرار رفع سعر صرف الدولار.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92825" target="_blank">📅 14:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92824">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28a592b70.mp4?token=Js6Hnd4R2SkLBMr9I9Porrdd4LjW8rVztSlAS92Sal7shyfQaMVez3LPWCbKPb3-ATJAoh1s_Gi-o9VuzTM9nXxqWu-tbrk3JFr5LkK0q1_1ka6YihgArpiJHbt41lmQCYw1WiR8HaGk8CdccdN7bej0gSVJwDGzvgUa57Rc2wUXXUVOf4Oh-95xQRSy0kfoWqPIWfvkl9QOX4ia8_dyLF5NRUgByMj1ZNjuV5aJFnz02A6SJrHfRQtBTrcyL_Cu3pXp8g2a8VLntM603aMXEoJbkbBB21kZkYUKkh-7lpf27nfVklAXVNIdXf2NacNxpAMYFTCpp_6UAgjI094oHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28a592b70.mp4?token=Js6Hnd4R2SkLBMr9I9Porrdd4LjW8rVztSlAS92Sal7shyfQaMVez3LPWCbKPb3-ATJAoh1s_Gi-o9VuzTM9nXxqWu-tbrk3JFr5LkK0q1_1ka6YihgArpiJHbt41lmQCYw1WiR8HaGk8CdccdN7bej0gSVJwDGzvgUa57Rc2wUXXUVOf4Oh-95xQRSy0kfoWqPIWfvkl9QOX4ia8_dyLF5NRUgByMj1ZNjuV5aJFnz02A6SJrHfRQtBTrcyL_Cu3pXp8g2a8VLntM603aMXEoJbkbBB21kZkYUKkh-7lpf27nfVklAXVNIdXf2NacNxpAMYFTCpp_6UAgjI094oHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الشورجة..
المركز التجاري الابرز في العاصمة العراقية بغداد "يصوصي" بسبب انهيار العملة العراقية بسبب قرار رفع سعر صرف الدولار.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92824" target="_blank">📅 14:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92823">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5f0d48a1.mp4?token=RHUqGCumh0AH-lcM6XGhHsC7kwpfqlHg0SV9rOE31f1rZN8xiFhv0L82shOj_SFdcXXBo-W4Dh-Mh9EbG_ptbM1EahRivEV7wYm6BAJawUgjHanveTibUsWSD2aFH60RhvR8Al-j2oz0AIR2Q_uNfqZypz4MZYFLTAkoQfeJ03OfqZZlWMt7j0TT01i7so5P8V7CN9S8vuONx3dHxM2EH4kVvlVNokNTHu2p70J6Yk00u3zljCdrq7OuXSnatBJnsABnbcdoAO9t3cVqllxSsg0VgTwtlmitG70PxZYK41CYp-wJNZSgeZRfDEa_jp0bRaBVBw1HdWLklXU6o7ETSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5f0d48a1.mp4?token=RHUqGCumh0AH-lcM6XGhHsC7kwpfqlHg0SV9rOE31f1rZN8xiFhv0L82shOj_SFdcXXBo-W4Dh-Mh9EbG_ptbM1EahRivEV7wYm6BAJawUgjHanveTibUsWSD2aFH60RhvR8Al-j2oz0AIR2Q_uNfqZypz4MZYFLTAkoQfeJ03OfqZZlWMt7j0TT01i7so5P8V7CN9S8vuONx3dHxM2EH4kVvlVNokNTHu2p70J6Yk00u3zljCdrq7OuXSnatBJnsABnbcdoAO9t3cVqllxSsg0VgTwtlmitG70PxZYK41CYp-wJNZSgeZRfDEa_jp0bRaBVBw1HdWLklXU6o7ETSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسواق محافظة البصرة تخلو من المتبضعين بسبب ارتفاع اسعار الدولار وانهيار الدينار العراقي</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92823" target="_blank">📅 14:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92822">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔻
وزارة البيشمركة: جزءًا من نظام الدفاع الجوي قد وصل إلى إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92822" target="_blank">📅 14:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92820">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qniXjs_GEB3dY8VHXRu-X25Bzmr4YQnjenfjCD8l9i9l6VwpqyqmU5gUZ94924-j2LiJ8s8EwNzZXmJ-1tpoL-uPISx1Ayz6JhjqxCsp_GNLdcxtbIcF7In9hTPGhHnpXPnHs7x5U4dGlvKwwyG3AzxoUAes8JzVV5TmbroVy2-HdUdjjQOcds-INO9LZv2w9rbfXEzz1kp5Fjo9MQy3cAKb3oAZh2feD7Y6PQXChtb89YCh5FQGbg_KfOapDhMNcHzuhMgV4J1rB6o93yW4VVdus-MB2H7jdr6qZmAlImUYGR6U7gVUpb0RJ6LxvJ0eUZvOY7ZFXeTOzwRP_Thrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LA8McYQd_mc7vxeARIKr_OsCZtEgtZNSd84NfM5QjevhVatyYzkF30tM6gMXwmRmwmfPnlCdiKj5djT6-w4A0vAJ24hufKoii7mQLuGywif-DiLde04QT6FuMM9J8WiUQH1710VDk9fFGUXwVRKPzHO7Dl-SAceJJurdc1iP4uOwaEN0eOVnVvr38rauFdZqTYj5MZwq6IIhe05Lh5Q3z4KbP6nZiyMk4Ke2hxQHzqWnomOrC3QtOgMN1NqUAJo8qbVG3lJysEEuI7bal6r_6AOGAr3QzGSqSUrFZEag_WJJbodZNewHIALBddXEVDGTMx-MrKNr7OZExQZY2Y4fXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد من تصاعد اعمدة الدخان من منشأت ارامكو في الرياض وجدة بعد هجمات القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92820" target="_blank">📅 14:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92819">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حزب الدعوة:
نتابع بقلق آثار عدم الاستقرار والتذبذب في سعر صرف الدينار العراقي أمام الدولار الأمريكي، وما ترتب عليه من ارتفاع في أسعار السلع في الأسواق، وانخفاض في القوة الشرائية للمواطنين، الأمر الذي سينعكس سلبا على الأوضاع السياسية والاجتماعية..</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92819" target="_blank">📅 13:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f225d2177.mp4?token=he70fgye-JDalN8k7sFAxOG4sRW8SqQgjslqen-d0VlHba11bdPAK0xDNG8uu0MwX4oEFzeW_jt6xDURpj-OCL6VE7tUfFg3qxXbRN9EA1jrejdbYmupn-7NK99-_tcqmg3jLkGRICV7wf9G5fM2HWLTvHn0SobfZ2qrAHLMPXJuM5ufT_7M7-1w9iyjUTSvQX3Zi00AVHn0Zj4d4JHWCs4zUEuHT79zoRIucyGM_0gVTlphaXj6044Om-dlOBwMFxJGY6hT4MHdskw09_AybXkinEk8fduyqZGaKquYQPbg3UT8PYTg7HPjtrpiKsavBZZC7D5X9pHzLGzvkjefKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f225d2177.mp4?token=he70fgye-JDalN8k7sFAxOG4sRW8SqQgjslqen-d0VlHba11bdPAK0xDNG8uu0MwX4oEFzeW_jt6xDURpj-OCL6VE7tUfFg3qxXbRN9EA1jrejdbYmupn-7NK99-_tcqmg3jLkGRICV7wf9G5fM2HWLTvHn0SobfZ2qrAHLMPXJuM5ufT_7M7-1w9iyjUTSvQX3Zi00AVHn0Zj4d4JHWCs4zUEuHT79zoRIucyGM_0gVTlphaXj6044Om-dlOBwMFxJGY6hT4MHdskw09_AybXkinEk8fduyqZGaKquYQPbg3UT8PYTg7HPjtrpiKsavBZZC7D5X9pHzLGzvkjefKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
إذا لزم الأمر، سنقوم في المستقبل بعمليات استباقية لمنع العدو من أي تجاوز أو اعتداء.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92818" target="_blank">📅 13:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92817">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6994727d3.mp4?token=UPXo7TzafspnAd3-nDmYQtSUTwM24VHvXELB3HqazyvFB8VSaYmotRze4zyv6K-jWEU6TiLiC_bdsGirsZFtRuxjcXvBVxWtktyWLy_M9aepu3LytNyRObE14MB7It0Jl7daWXmxStP4MZNdHzyY6FW0TXmC3aNAJC1GtuMXoS-csXS6nyC9UYRDUbdvPReYYAg_MnjZvzJvQE-oJI25vQGHo3O3RiwPSXcukwnTzboxUAQrW3mzTzVNLRkE5QFDfcAsETjtmt0o3G5dv58fQFwA-3xsxHQGtg8wtkQcq38NucUyVODbVG_yb7Y5G6sCFyqAer5ZIAcuGxWHXZt9gIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6994727d3.mp4?token=UPXo7TzafspnAd3-nDmYQtSUTwM24VHvXELB3HqazyvFB8VSaYmotRze4zyv6K-jWEU6TiLiC_bdsGirsZFtRuxjcXvBVxWtktyWLy_M9aepu3LytNyRObE14MB7It0Jl7daWXmxStP4MZNdHzyY6FW0TXmC3aNAJC1GtuMXoS-csXS6nyC9UYRDUbdvPReYYAg_MnjZvzJvQE-oJI25vQGHo3O3RiwPSXcukwnTzboxUAQrW3mzTzVNLRkE5QFDfcAsETjtmt0o3G5dv58fQFwA-3xsxHQGtg8wtkQcq38NucUyVODbVG_yb7Y5G6sCFyqAer5ZIAcuGxWHXZt9gIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد إعلان السعر الجديد للدولار من قبل الحكومة العراقية.. المواطنين في إقليم كردستان العراق يهرعون لبيع الدينار العراقي بعد إنهياره أمام الدولار الأمريكي.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92817" target="_blank">📅 13:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔻
وزارة البيشمركة:
جزءًا من نظام الدفاع الجوي قد وصل إلى إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92816" target="_blank">📅 13:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على محافظة صعدة اليمنية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92815" target="_blank">📅 12:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92814">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
رئيس مجلس النواب الأمريكي، مايك جونسون:
من المؤكد أن الديمقراطيين سيحاولون عزل الرئيس ترامب، وربما في اليوم الأول أو ثاني يوم. تذكروا، لقد قدموا بالفعل مقترحات لعزله في هذا الكونجرس. أعني، إنهم مستعدون تمامًا لذلك.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92814" target="_blank">📅 12:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92813">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe9d10e22.mp4?token=EsJwVEqSSkvgJ8QDeqGoyDdgLA3nOPkkVgQNjoT3fFSvu4fhyWuH283V1mT2qEgwp7DZvvPN9a76aMBbs62Pq3BVbf8PAjT8Nk8k3xikuITIsy90scjHCAkWUu_tgCHOj9DqkVt2wQu7lffHYcFvyOgCcZZbJ10fb3atVaySb6IzSb9fQXEc7F7YGgtlItiYl9te9JupheSDCqU5HX7ZAVQxSqxaFrhULjbzYhCHWRITwB48QcIX9ojuP8fbtGtw6G8jDHRxuI-JI4l4MQTr87Qgy5Zz6J2GmhSKBY2k6lTuaMOhy1xARdwK-BOjm7n80cdOYZ_ezZef64f4Nya_f1y29r6ZkKiDzQq-5ejAb518R3jq3GFYLWej11MAbnNGsnaQ5fZ4Ask_Q16adYTm8h3K8UwFtWRgb3E-XQaTLpDBs82VspYA1gwwL1WQNoMbrxpyB0NfrWqrNM4R0BYNJNXy1rWKAt8fGd9-_yESlBg_NdWa3OCpzph4873NcaY4ge9gpoHHoANhoyqDn4J4bvjT0NbY8GfrBdiZVSMvLG5vnph6FI8kcgvIo76af-Z8ThNjrUqkrQoT_Sbk3pmpEnDR_OQ0qbccI3xL98geLKaYA7cG--UVccjKzRSbVbShAEC0aZtpyTfOOmxpm9TgC8q-RppTeEMCXFaWh_qnA0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe9d10e22.mp4?token=EsJwVEqSSkvgJ8QDeqGoyDdgLA3nOPkkVgQNjoT3fFSvu4fhyWuH283V1mT2qEgwp7DZvvPN9a76aMBbs62Pq3BVbf8PAjT8Nk8k3xikuITIsy90scjHCAkWUu_tgCHOj9DqkVt2wQu7lffHYcFvyOgCcZZbJ10fb3atVaySb6IzSb9fQXEc7F7YGgtlItiYl9te9JupheSDCqU5HX7ZAVQxSqxaFrhULjbzYhCHWRITwB48QcIX9ojuP8fbtGtw6G8jDHRxuI-JI4l4MQTr87Qgy5Zz6J2GmhSKBY2k6lTuaMOhy1xARdwK-BOjm7n80cdOYZ_ezZef64f4Nya_f1y29r6ZkKiDzQq-5ejAb518R3jq3GFYLWej11MAbnNGsnaQ5fZ4Ask_Q16adYTm8h3K8UwFtWRgb3E-XQaTLpDBs82VspYA1gwwL1WQNoMbrxpyB0NfrWqrNM4R0BYNJNXy1rWKAt8fGd9-_yESlBg_NdWa3OCpzph4873NcaY4ge9gpoHHoANhoyqDn4J4bvjT0NbY8GfrBdiZVSMvLG5vnph6FI8kcgvIo76af-Z8ThNjrUqkrQoT_Sbk3pmpEnDR_OQ0qbccI3xL98geLKaYA7cG--UVccjKzRSbVbShAEC0aZtpyTfOOmxpm9TgC8q-RppTeEMCXFaWh_qnA0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد إعلان السعر الجديد للدولار من قبل الحكومة العراقية..
المواطنين في إقليم كردستان العراق يهرعون لبيع الدينار العراقي بعد إنهياره أمام الدولار الأمريكي.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92813" target="_blank">📅 11:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92809">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tH_Z25cV5g4iMjwNmT46E_76Gf1VMGqS4LvSsrNhiAR7JR7-M8hvQgd-NMK3aI4PYVZOCHnjKE9a8Cff3X5cjzSDzkxkLymMZO7j1gESpyHk2lS2v_8ZC7jGp086L0Yw1kFADcEACWObK_8RGCRrTV6RAm9rd1rVpbUWmU5US3juENEaougM6T4RWQKk0pTLHUOeWtskGC06GwB5Kgw_EYxmkwE-E2SUxideODkQqHRH96ytId9zRlQqxPwEAAuX3Nq4jXRbjGxS_J2khvDvnIxOty2t04mNBAIRsdZFR5g2O1LQv66jKVw5ZhneZqrpx63otPEJQIW3CqpQSbiwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnYfx2tQXE7G7LWBroTNLAZ_Ed8lLftzmUjLck_-qiJIsSWJoUg3QJyEXrG76Z_0MZsTrO7nuWhAL3oQU60SKEibzwj-H14xvPOxNtxuJ-4VP5uARXs8hjRQf7Q4bfZGzS566fKZal41fP7A6CJIC_fr3cxZNS-gkJ_nilOaDD0RJ6ZtLCAOET8Y7QOEI02ZBHgMu3F63C6fBhnTnLlvxcPjzMi5dJtQ0i5kj3ZS8xa8yhDv_mjDtj0Ap_mMVvVEofDPAS7hcjR0fp72b6Vei3EiDvDzKJIexGCz2EDJ0zLn2jhcsQTw6htSru1Y4mJaAGceQF09bXhHY6vGazQcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VlQjqcETlIL-GWvRZ8Rs2D0XuB9QLiMVe9um-zikmbi4TboIzmVkvLtyEN-KD1s-843uDjozDBb9lR0PmniyQ44hJ5qm0YnZPIC-Waxg2GOGras9KfFAGJr8VAuNef53rGPCYmoyRxLalu_eOJgoXHH26pchNDASY7wiTT13zBd-FbAbwzbNymXSrJq48pTOxjyf6R1hca3aNB4rPY3N9X9AlmCJ_hjNW5-R_vOBB78CAgReyZpFtq3MTA5cC6AP6vrRp2Gg1QtB40TfR8B7wu-m8kaCdvg3QmQ18s8Y7KnSGTBPcUNgr4wq2OdMu_gMDVy64SQR16O7TQdZqGvbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UI-QFYQbpeSmpZbyi1P2mjzduD2KanOGo8Y8MwMnqqrbfw1r6AgET9LSrc8JXTqKhFNH-Gt4w0vU2rQfOV6CzjbRCsvuerSJSaNzRuOZii6mD-r8De5WQgSWHzRwc4NNsf4aSRQEG0samRxPeNqZqw3F7PYWgUG_vuVpf0_Z1cQmMx9-8KASK8ofHzajQQ6m-bW3tiR2Zw167BSPeWrFI6bmBk2BmuY2jzrP45Ui39R3kMPIOpsSJ8LNSFSEURoOtDMk-Po0BZYfF0OW_nY0N_TpmTM8rHpA_vj7fDUf9KQsBdYGhuPi5uuXrmNj_fgwJ_-ry06szfYOsCE4BqrL9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
📈
أسواق سعر صرف الدولار تدخل حالة من الاضطراب في محافظة السليمانية شمال العراق</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92809" target="_blank">📅 11:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92808">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الناطق العسكري بإسم كتائب القسام "أبوعبيدة":
لن تنسى فلسطين من سانَدَها؛ ولا سيما من بذل الدم من أجلها، وإن تدنيس الأقصى وجرح غزة النازف ليستصرخ الجميع بلا استثناء، فليست السودان وليبيا أقل جرأةً ولا غيرةً من اليمن ولبنان والعراق وإيران، وقد ثبت أنه لا عُذرَ  لمتقاعسٍ حين شاهد الجميع كيف أقَضّت المُسَيّراتُ البسيطة القادمةُ من مختلف الجبهات مضاجعَ العدو، فما بالُكُم لو  فُتِحت عليهِ جبهةُ الغرب؟!!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92808" target="_blank">📅 11:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92807">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
قائد الشرطة في محافظة خراسان الرضوية:
تم توقيف سيارة كانت تحمل مواد متفجرة قبل دخولها إلى مدينة مشهد، وتم القبض على سائق السيارة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92807" target="_blank">📅 11:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92806">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ee8090f7.mp4?token=ZWRZ3ICkDSiCN9swRtHtNnWyWlve-nopDoUX9ZLCoCLOxDwEAVZeSVCXr6CR2ESRCBKchlIs65wuxByHKZHS0-mk0kfhIH-6erA1QBJC6ZTrgAjEQdPGnqng3oodLIKwcYb2uc4gF6KZKHrI5oAD3Zw7mH3XEZLlGohIAVAY_PqLhn6JjKgZFZRic9ITqi5a8KeTYgwHLI34SniX9od4x1HYnUBiSd7x2bc4Aa3jkIg7X0Sl1NWa0uoyykNDB24i5gP9T_8MxzdD16Zn2WGFJv5gcebMcYgqfR-tPWkcVWx74MM50gAEzFfQwi7TIHvtvTpYesLPzzzgLPPgSBkbKCEG2p5KJ1h9XGk_-_GG4xj_eUF2tKHxtkg8Uaah1p_0-gr_8RdBXvOwvdUCquNKvAs2E6N_A6whRrs_m5YRIvVuc02VQuVgRAj3Yu-oeM15D6ZTLSdLfP4NvWngn1YUxcJRCOs6mYVbdEtYkFMan58f0WLyNnHH6kYadqGuPRCVtoW40kImSAcYZSw5MHcIKy6lhW88O2_VuUwwG1rgoBeJm5vaefj5NHiVwWAki3Tw_udqnETutBztgv348lHxbA8XnJcO-7e-onyAB6JdFkm16lFyAUf8Y5lCipmEoVfmSAP-Xj4VK30yC4phKbSpzG5RuFAL5VwLIs9gyoVHD94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ee8090f7.mp4?token=ZWRZ3ICkDSiCN9swRtHtNnWyWlve-nopDoUX9ZLCoCLOxDwEAVZeSVCXr6CR2ESRCBKchlIs65wuxByHKZHS0-mk0kfhIH-6erA1QBJC6ZTrgAjEQdPGnqng3oodLIKwcYb2uc4gF6KZKHrI5oAD3Zw7mH3XEZLlGohIAVAY_PqLhn6JjKgZFZRic9ITqi5a8KeTYgwHLI34SniX9od4x1HYnUBiSd7x2bc4Aa3jkIg7X0Sl1NWa0uoyykNDB24i5gP9T_8MxzdD16Zn2WGFJv5gcebMcYgqfR-tPWkcVWx74MM50gAEzFfQwi7TIHvtvTpYesLPzzzgLPPgSBkbKCEG2p5KJ1h9XGk_-_GG4xj_eUF2tKHxtkg8Uaah1p_0-gr_8RdBXvOwvdUCquNKvAs2E6N_A6whRrs_m5YRIvVuc02VQuVgRAj3Yu-oeM15D6ZTLSdLfP4NvWngn1YUxcJRCOs6mYVbdEtYkFMan58f0WLyNnHH6kYadqGuPRCVtoW40kImSAcYZSw5MHcIKy6lhW88O2_VuUwwG1rgoBeJm5vaefj5NHiVwWAki3Tw_udqnETutBztgv348lHxbA8XnJcO-7e-onyAB6JdFkm16lFyAUf8Y5lCipmEoVfmSAP-Xj4VK30yC4phKbSpzG5RuFAL5VwLIs9gyoVHD94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
📈
أسواق سعر صرف الدولار تدخل حالة من الاضطراب في محافظة السليمانية شمال العراق</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92806" target="_blank">📅 10:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92805">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
📈
تم تعليق صرف الدولار الأمريكي مقابل العملة العراقية في دهوك حتى الساعة 11:00 مساءً</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92805" target="_blank">📅 10:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92804">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb13ad115.mp4?token=o5ntHSgzanFgJtC-5LVdmYQU9PK4ZHVkXLybLX1WfDNsjK2-piVAUzUR7xmdZUwwPLwZXv3_jQ6U-aReRw_CJQUdbxToooxUgcOvz5FVjsJBT_E1TidrhWNmc1JIzyVIBwYbmsBe88v8P4DKXIZDIoVM4Yxs2p7eP1WQBz4b2SOa6Qp5cXaUFxTgBGStWtXZceSOd__SnoZC3FJZ-Qfcb9Cub_RzrOtl_luxH1rQXWVJBUGQg48nTXVsq0gyMP2sJ1wz4b-5TgWVMSi7vGm-X9i5fcj361mFZ8cgrrCZq3FAGcdlABu0DphRuf_Qa_9qhELm20WS_R8w0qvCx18ypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb13ad115.mp4?token=o5ntHSgzanFgJtC-5LVdmYQU9PK4ZHVkXLybLX1WfDNsjK2-piVAUzUR7xmdZUwwPLwZXv3_jQ6U-aReRw_CJQUdbxToooxUgcOvz5FVjsJBT_E1TidrhWNmc1JIzyVIBwYbmsBe88v8P4DKXIZDIoVM4Yxs2p7eP1WQBz4b2SOa6Qp5cXaUFxTgBGStWtXZceSOd__SnoZC3FJZ-Qfcb9Cub_RzrOtl_luxH1rQXWVJBUGQg48nTXVsq0gyMP2sJ1wz4b-5TgWVMSi7vGm-X9i5fcj361mFZ8cgrrCZq3FAGcdlABu0DphRuf_Qa_9qhELm20WS_R8w0qvCx18ypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
📈
ردود الافعال على ارتفاع سعر صرف الدولار من شارع المتنبي ودخول العراق مرحلة الركود الاقتصادي</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92804" target="_blank">📅 10:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92803">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991f4cd8ff.mp4?token=Ar0BoGpCyeSXiPxIFT4iidgacLekQgglaeLSAH3eKZgALyBc0olSwn6nZXGz2a0jPGxzuiiqeKtqoH59L3ptnPKYS_IXtekodGawCW52ByIqwM9zqUoFRnVs9oRVXCc8sHbSxAh64f9Vdv1wu4SEQPCOlO3BXTY0TmzJu26Ne6a6YuB1FP4KwWDU9hN4_GPVvSCRDEbJ8NcCBpBWCpey1eQvfoJQVi8KZT5bUUwzP_lY4U32eha6k4xVsqinkIy67nRFbxpHovHhgNmIwIrs-3_i2VPVA2HW7p2rTFJPFNThKtl8uzEkr5PPwwhYrDdBCmTO5PBqVfJ4fUEPXcfTSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991f4cd8ff.mp4?token=Ar0BoGpCyeSXiPxIFT4iidgacLekQgglaeLSAH3eKZgALyBc0olSwn6nZXGz2a0jPGxzuiiqeKtqoH59L3ptnPKYS_IXtekodGawCW52ByIqwM9zqUoFRnVs9oRVXCc8sHbSxAh64f9Vdv1wu4SEQPCOlO3BXTY0TmzJu26Ne6a6YuB1FP4KwWDU9hN4_GPVvSCRDEbJ8NcCBpBWCpey1eQvfoJQVi8KZT5bUUwzP_lY4U32eha6k4xVsqinkIy67nRFbxpHovHhgNmIwIrs-3_i2VPVA2HW7p2rTFJPFNThKtl8uzEkr5PPwwhYrDdBCmTO5PBqVfJ4fUEPXcfTSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📈
🇮🇶
يشهد سوق أربيل للأوراق المالية اضطراباً، وتم تعليق عمل بعض متاجر الدولار.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92803" target="_blank">📅 10:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92802">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jud_Z8Z1-bjwzzBdwhyZfwgM9ogA_FDKG0AmkLPbMI7aXfHHYncJ6YoK81A3_YVc8Rp6vZ70cJaMDEsgTdnGBGnjlX7ykq0K-xf1MRtK3NgcU2FKFe6hSq65KDEnCDPmV0cfDh5t3AworKnFNyUUkt9Bt91sGl7z73eW0QEF6CFVAdXoTebTJ0am6AIF3qQmvlNMChxvsLKu-ygTcDKGbRvSVr_EqKroWyZS34P1Oby_692NeFMnaB9Q3fLD-jsG4QlPGd1c-7A1pm678QuXSoV83DT8X95MpzCpRAEOfqh4WZmFp5BlC-vhkITSGhpJGDM_f8Pa-0eFzQG2N01zyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلل يصيب سوق الشورجة و سوق جميلة وسط العاصمة بغداد .</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92802" target="_blank">📅 10:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92801">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
📈
الدولار يقفز إلى ١٧٠ ألف دينار   بورصة بغداد تفجع بقرار الحكومة برفع سعر صرف الدولار إلى ١٥٢٠ ألف لل ١٠٠ دولار</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92801" target="_blank">📅 10:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92800">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
📈
الدولار يقفز إلى ١٧٠ ألف دينار   بورصة بغداد تفجع بقرار الحكومة برفع سعر صرف الدولار إلى ١٥٢٠ ألف لل ١٠٠ دولار</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92800" target="_blank">📅 10:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92799">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
📈
الدولار يقفز إلى ١٧٠ ألف دينار   بورصة بغداد تفجع بقرار الحكومة برفع سعر صرف الدولار إلى ١٥٢٠ ألف لل ١٠٠ دولار</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92799" target="_blank">📅 10:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92798">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📈
الان سعر الصرف في بغداد 178 الف لكل 100 دولار
📈
سعر الصرف في اربيل 180 الف لكل 100 دولار   تحت شعار ر … بالفقير</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92798" target="_blank">📅 09:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92797">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇶
📈
الدولار يقفز إلى 180 ألف دينار  سعر بورصة أربيل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92797" target="_blank">📅 09:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92796">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR_g_qiUr1dzb_xdadsS_kmwim3t77D3r_uTtEIgqbECpT88gkEW0HYW4p18979TJM9c_IbgnAbe32juDCpSzrFI6darjLhE3-1gx_TZk1zh9QOnMKYZzMbQT04yqnPcuAtXd1fvQ6TIxz2zUfTE-Wh7ywbad2klVyT-tEcO4a2TpqXfFJ4YFsHaiwj1an9388YbK-KPR3mPcUEgFrMeLrefbKsjQa6xp1seJpePs9iLoZfbk1yogKy7w6GN_Mzbwb7B3R_h2zEFUiLSaz7dWczqbJJiOdM-k1LidnMMyAL-EyYbBo1A6mxSz-Bkqu37oCF-OWxAn0CloDY-nhwZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
📈
الدولار يقفز إلى ١٧٠ ألف دينار   بورصة بغداد تفجع بقرار الحكومة برفع سعر صرف الدولار إلى ١٥٢٠ ألف لل ١٠٠ دولار</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92796" target="_blank">📅 09:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92795">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇶
📈
الدولار يقفز إلى ١٧٠ ألف دينار   بورصة بغداد تفجع بقرار الحكومة برفع سعر صرف الدولار إلى ١٥٢٠ ألف لل ١٠٠ دولار</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92795" target="_blank">📅 09:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92794">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
📈
الدولار يقفز إلى ١٧٠ ألف دينار
بورصة بغداد تفجع بقرار الحكومة برفع سعر صرف الدولار إلى ١٥٢٠ ألف لل ١٠٠ دولار</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92794" target="_blank">📅 09:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92793">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
هزة أرضية بقوة 3.6 تضرب محافظة كركوك شمال العراق.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92793" target="_blank">📅 09:12 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
