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
<img src="https://cdn4.telesco.pe/file/rCBAt9iPKJUpol_8ntUMVP2VxNfPQFwJQ9n_6ntSBpDfSoVMSxatq8UMJKcuk3xGYhWZETYNNmnrqJMLNBbWPkm_cSiCXYpueNyEaMrLJUs_7aLRlMHctGR6ejytEGaR_2UPNSol5ONkGnHOi8Cg9t64ll1lR1lBKpolXQYkdAAOLnIMHW7pJrxbu7KzQr0Qp_cwMkzNoSrCunxOXHFK5WbVAFlUUS672MV2awKNHCufEZ4gWhgHvudB-P2R5yUQocsQNrQECwEPSKNf0fmDWeTJd-tFknLBo5IjnBAWsuu2bA4Beku-kEIzSuOmjr6uXCAIsOIxwHNe6xB-z9EXCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 16:19:14</div>
<hr>

<div class="tg-post" id="msg-80060">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">في خبر غير مهم
رئيس البرلمان العراقي هيبت الحلبوسي:
نرفض الاعتداءات الإيرانية التي تنتهك سيادة الدول العربية والإسلامية وتهدِّد أمنها واستقرارها</div>
<div class="tg-footer">👁️ 784 · <a href="https://t.me/naya_foriraq/80060" target="_blank">📅 16:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80059">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وسائل
اعلام:
‏ستعقد جولة المحادثات بين الولايات المتحدة وإيران في شهر يوليو في الدوحة.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/naya_foriraq/80059" target="_blank">📅 15:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80057">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1bzkPYGbLogmvG03v3ARyFYBCThGSbLPN3XY3LJxNsC0LlMMD-JonVhXA8SXedfoQFdps_Er0f26aKHj40Pv5RXLSfUU4nkFyneVW5YGQZ2bVwAnQ4tJCvQfl9mRcV6PAhbeWFLyS7sMcWaoSNf9yXzQz8dNmu5KRwvBmMxEE6XpPcenpb_c4DPhORRVbxkqmrfQCpCuC6oQruSMIA8NyOAouYTeJosx4hozLsR5B8jlT4V4LT0pjO10t4kPe-I5CmOTmfcEgbdDosk_iWsJh3MXKqKJnkl0qNDaWLj1u_qXfrmdjeUs-HlUi_eNxaqnw6KhoznDyBO2O9MYXXiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط طائرة مسيرة مجهولة في النهروان جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/naya_foriraq/80057" target="_blank">📅 15:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80056">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c12540e77.mp4?token=u3kkQDGiTNqWz7Gr_xOYfrowfgEC_6bvTt0hrrzYsl2--KwFnXei3mUeaPVgez5YdEvFL_E9sYGrTu1DkkYO1LqZDGMo46pU_vl966Ihs3aCksMY83CBD5AIkZiKDeyTpfS4JGLPtNamgQhqV3qNpvhZR7QRxzavfchWOytK9dEd0bxnXAXohYcALTgO3gYab7iWclg3biawqKT8oUUIx8gH0kOqspDr66skqCCiNnEaziZK-ihwKEa_eMHxKCVdonFABfeGgD3I5CX2ZtBOcXOWhPRUod69mwSB2APCKRHI9y4ASJGXM3bh4ba9AQ1CkQ92QRQpiZJl-cYwCnC-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c12540e77.mp4?token=u3kkQDGiTNqWz7Gr_xOYfrowfgEC_6bvTt0hrrzYsl2--KwFnXei3mUeaPVgez5YdEvFL_E9sYGrTu1DkkYO1LqZDGMo46pU_vl966Ihs3aCksMY83CBD5AIkZiKDeyTpfS4JGLPtNamgQhqV3qNpvhZR7QRxzavfchWOytK9dEd0bxnXAXohYcALTgO3gYab7iWclg3biawqKT8oUUIx8gH0kOqspDr66skqCCiNnEaziZK-ihwKEa_eMHxKCVdonFABfeGgD3I5CX2ZtBOcXOWhPRUod69mwSB2APCKRHI9y4ASJGXM3bh4ba9AQ1CkQ92QRQpiZJl-cYwCnC-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات صهيونية ترمي بالونات عليها منشورات باللغة العبرية على الحدود العراقية</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/naya_foriraq/80056" target="_blank">📅 15:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80054">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4jaKsRQcSrZ1_0SSzJhwUVWsT6FHOoBuvmQzatHKUls_7bDDmiQHOG2vI8VtXwnpZqyi8ZIVRkpyLGt7s2s_E5pjGD_SP4AVuPM2gbAmQZt-wGcgGOXZ8OnXbBT_mzXU3DdhpcMtFM2vRqfvzWrUkD55LMnJpXTf8Ins55Q5IOnLwAasNn6HqpqJDqjPtyQxf1bPxE4a1iYhMzQcobL4b7w4_kvTycCJNjCoPD1b4mfyjMygRV9YBfueCRlzz6hDJZBXKcjBboQRg9cSd7Y3NPE6KrY5tKQTfdDT2Y102UkoJCQUiH684DV3_M5ra7tXqi9ymioNI7TTuMgS-4YbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2sS_au2UjK92kqLCb830jROqkcB8hqFekdsapiuQATafIAEkBJNb8usyaRzE2qsJurKztHkLBjhDo55jBZHqnKT1tG2tDnDWMHx_7ykNKSRXKue0sdjqq6b1tFNAoxtluWnMn9YhLUff0fYATAojPBmLbHSKToTcAQMNnOtHLR5C-LxDe_BNwzc9E2BOg9SrP09Mr1psAO90o-ZrTjIGG6CV81D-7f6zHEdEW4uS5vqyZ91NR1OXUlpaU9wXSPwyq0R_aANDxEnBvh2ZnZRX-cYd3XR9XmajxX0xurMtyTm5x5iV6WCRP-YZROYrUMOAeJ95ZL-ouVSXSOAFizvcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طائرات صهيونية ترمي بالونات عليها منشورات باللغة العبرية على الحدود العراقية</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/naya_foriraq/80054" target="_blank">📅 15:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80053">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سقوط طائرة مسيرة مجهولة في النهروان جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/naya_foriraq/80053" target="_blank">📅 15:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80050">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSSqV6pHdr9T5DjxcC4BbxgxCMWrhenuS5O8aZqX3MjAjUByQv3oRA9y30t4YSaAkDxPeoFcc0ETRXz5f1r86ChKbMvQM3HJ0W5KbXE5atpulFRIW21rAp11SMJGvMlfOPSboej5yqXGLb3gVoKE3lUDePlJGmnQsaRs1w7Vw6vwiapJ4iRyP1-x2ID5Il58hfjcvJRQ_7G9-vjKUIAXRHeS4td3O5HCjgtBzJdBSgXqo9lPZpGOGe1JeTLao1qXEPXo61c2v2TFVvj7OA1669e1lxxaO2mAzRGfSvlfslkPL1ky1GttKPrahHtvlYpuNtCRt3kSb2EUi_K7q4sgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0UCDn21PctzUgTdwnoQVd-JfmsgXtW6RTFar3e6jobo0YOgk6X_VuNvlq79GAOGI9fXiysv5P5gJdk8KL1ogO2t5BQgjJtfjgxuU5A3O31uQ3QAKAFuIvp8Dho3RfuR0UrBrux9825Qd8oM5A0OC0jmExcWP6lSIanlqLRwtqbk57UQJQEdcV3I4cjVDnV0ILlReXCpkjaTTuek8C6XYT5nXIdlg4ndlUOfPcCrRapBsNsNRUrq-r30s8p2EY6oHoW4iBFgKS6HzDDVegO2X-Nu0mjVoF_LLzcoJQwHjEE-jSQdi2F6XusmN6hXp1b-XIfEmahGgZpPnZJmMMfwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhNjetBx7To6Hn0OBH0Go8hS3oKrP-xHbI_xyeaxTJz6kE783ulmokMSi5cjKwUubmCKrh7l4ECK2iIBEHEop-GLuEOsjxEXht8bwot49P0sRIiAy57yLKMVRKvI4_liBJ1C0khmSLMEH9DjF9mxT0YfEmGyQuc6bE1duLnmjVGKU_sjFkyDFXPOBXA4v3fAknpZX0YpUaQru1gZ8e6v2OVUmSBs5gSPf2AFXwMSNY_IOZqaU46vjqjbrCn4jKPfxWPSzCEoQFEpWfZD3N4JQBeurh4fCA-d_nDtHqyb4hAXTZCdA8WA01iTeOpw-z9L8Sy8btLCur8OLTmQtsGd6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دويلة الامارات تلغي وصف الهجمات الايرانية بـ"الارهابية".
الصواريخ جابت نتيجة
😄</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/naya_foriraq/80050" target="_blank">📅 15:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80049">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📰
بلومبرغ:
رغم تلاشي المخاوف السابقة من تعطل آليات تزويد الطائرات بالوقود خلال موسم السفر الصيفي المزدحم، إلا أن الأزمة تثير تساؤلات حول سلسلة التوريد وموثوقية توفير الوقود لأكثر من 100 ألف رحلة جوية يوميًا على المدى الطويل.</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/naya_foriraq/80049" target="_blank">📅 15:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80048">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">#ترفيهي
هيأة الإعلام والاتصالات العراقية:
نذكر جميع القنوات التلفزيونية والمنصات الإلكترونية والمدوّنين والشخصيات الرياضية العامة بالتزاماتهم المهنية والقانونية عند تناول خروج المنتخب الوطني العراقي من بطولة كأس العالم.</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/naya_foriraq/80048" target="_blank">📅 14:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80047">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اعلام العدو يتحدث عن حدث امني غير عادي</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/naya_foriraq/80047" target="_blank">📅 14:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80046">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اعلام العدو يتحدث عن حدث امني غير عادي</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/naya_foriraq/80046" target="_blank">📅 14:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80045">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الاعلام الامريكي:
المزيد من السفن تسعى للحصول على تصاريح من إيران لعبور مضيق هرمز بعد أن تعرضت سفن غير مصرح لها لإطلاق نار تحذيري.</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/naya_foriraq/80045" target="_blank">📅 14:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80044">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guNtNWLnhd_mXWGAiefvbprt9bJgOdG4iiXqPkPfKqWK_YQQqlV3MAY_lq-hxZ7l9x16Nv7c1ejt384QldUUGdQe4rcdOwPkbuIqgjK--V1Pqq_lE78KTwklk14hXIYehUgji9shG148vP9lbDw4WpCXpWlqnUJ_pd8KFwX9Ao91ht4BMX-wxxBWeYk_g8j5-dPXWFXorkyYwLZ5dMBt-DM1qsHP21ubJQ3qfqZdVy1C1C18OHKYBYfGm0VrcLojIjZgjbw1DmVFfxR6wIMgDv8pR-6I_tlE4QR2G5zS07NODZLqI0UF-bY54RthimszxQ8-bColZY_sMVa0P8frbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مقتل ثلاثة نساء وشاب في مدينة الموصل شمالي العراق على يد شاب من دون معرفة الاسباب</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/80044" target="_blank">📅 14:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80043">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe770_2xTF-tshBqqOO3jse3ZmoRytR4SiNKJN2CRnVOEjrChxiCPUJUV66cnyVAADq4zRcYiCnJO66zN2hIt5aw-H8CeLw4u44ccO2NKYkSxNRr5YzNnV-Sc90ZtPN4YvE3B5aAm-LFDT6x2UgIDHLWqTOoHZeyGXb_ZFVryEAigp8et2pnpdpv9p6Zxz_vdlqD4vGHx2WHA4dNavAtGjVX2OkKEsOzfGUWogEAqbOdju0N5xgKQjX-27pwsrrHplbG26ajnG93VtTxQgvnyREDdqy3GbNsW8v8BHM-mOWbbpWisXqSrc1_CMoDhTM8nj6rbJMSwPhXzlRokWi6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
محاولة اغتيال تطال استاذ جامعي في محافظة ديالى شرقي العراق</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/80043" target="_blank">📅 14:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80042">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
ايران تعلن استئناف تسيير رحلات جوية إلى دبي ابتداءً من 30 حزيران الجاري</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80042" target="_blank">📅 13:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80041">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارات عنيفة في سواحل عمان</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80041" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80040">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">استهداف سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80040" target="_blank">📅 13:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80039">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwYT9IOX4_eMvdNzrZJtg56iJla9NzHeW2nF2gs5zS3q4gFH9O4v5Rzbb8KK4jxWVMi_jneKHnesLrzIW3drm5bEX7V3gC9WYwNBnd3MCPhk8rTBFSleBM1Utgzs_VlwgC6AZWPoWCwaAOv6J7APmcis2JebOZQMZdXGSAIESh1Ic9T-P4NAvyBbItj0pOhGyJ4wn_6PiKVJihNTc1lR8r4rzLAwXchQUOKXyLjNbs5mMR_GcTg7cq5BCl9rNagWTs6o3Or4oPLtErqFeWcL4ywX-XARCqplB-MlHyQqKBEFm1g3AYqm0zo6QoM9XnnIqDBlTRU9-TpwvBeYnxk0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة في سواحل عمان</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80039" target="_blank">📅 13:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80038">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجارات عنيفة في سواحل عمان</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80038" target="_blank">📅 13:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80037">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇧🇭
البحرين تعلن تعرض أراضيها لاستهداف بعدد من المسيّرات الإيرانية فجر اليوم.
بالإضافة ‏لاحتفاظها بحق الرد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80037" target="_blank">📅 12:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80036">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📰
رويترز: مسيّرة استهدفت معسكرا للمعارضة الكردية الإيرانية في محافظة أربيل شمال العراق .</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80036" target="_blank">📅 11:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80035">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: الهجمات الأمريكية التي استهدفت منشآت المراقبة الساحلية انتهاك للبند الأول من مذكرة التفاهم
الكيان الصهيوني هاجم لبنان بالتنسيق مع واشنطن وهو أيضا انتهاك للبند الأول من مذكرة التفاهم</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80035" target="_blank">📅 10:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80034">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">▫️
بيل ماهر: برنامج إيران النووي لم يُدمر.
🔻
جي دي فانس: ما هو الجزء الذي لم يُدمر؟
▫️
ماهر: لم ندخل إلى هناك. كان الأمر كله، يجب أن ندخل إلى هناك ونرى؛ وإلا فلن نفعل هذا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/80034" target="_blank">📅 09:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80033">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
المنتخب الإيراني يتعادل مع مصر بنتيجة 1_1</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/80033" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80032">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429833db62.mp4?token=TMnvdFome3gpPGcNmvCN5Jmx58G5Nr2tAn44XnMHQIxikcuzCAZ6m5wTA6yEp0e2iqgxHMxPcyHW_JBRYFAnSsF-R5exmi_pt2IfEnTTR1Xfb4bGu6voa3gDBV8Qw6X6-GatEYyF-leU0OoDaGyKse2RilWYR-sFbAaHT8LsUOZhD0KqLj64hGpw8qZrpXzhCKxlbjBS6talNa941_GvMjFe0AdmXrzaw6HkxyvGX2qx1EhJFFCnAYYJio4dFEzDC34yC4BSQ4mKJkSk3-XC3kwjb4Uy32xCQF6ajkLOIKqAw4fX6EbcuReZYbIcmDMLYuVSL5TUZh0xLJwliKWEnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429833db62.mp4?token=TMnvdFome3gpPGcNmvCN5Jmx58G5Nr2tAn44XnMHQIxikcuzCAZ6m5wTA6yEp0e2iqgxHMxPcyHW_JBRYFAnSsF-R5exmi_pt2IfEnTTR1Xfb4bGu6voa3gDBV8Qw6X6-GatEYyF-leU0OoDaGyKse2RilWYR-sFbAaHT8LsUOZhD0KqLj64hGpw8qZrpXzhCKxlbjBS6talNa941_GvMjFe0AdmXrzaw6HkxyvGX2qx1EhJFFCnAYYJio4dFEzDC34yC4BSQ4mKJkSk3-XC3kwjb4Uy32xCQF6ajkLOIKqAw4fX6EbcuReZYbIcmDMLYuVSL5TUZh0xLJwliKWEnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي 3 انفجارات في جزيرة سيريك، مقاطعة هرمزغان في إيران</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/80032" target="_blank">📅 05:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80031">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">المنتخب العراقي يتصدر مجموعته من الاسفل ويتوجه إلى قاعة سامراء  للعودة إلى البلاد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/80031" target="_blank">📅 02:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80030">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">التلفزيون الإيراني: بحرية الحرس الثوري تستهدف عدة نقاط للعدو الأمريكي في المنطقة.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/80030" target="_blank">📅 01:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80029">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">التلفزيون الإيراني: العدوان الأمريكي طال جزيرة قشم ايضا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/80029" target="_blank">📅 01:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80028">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تصاعد اعمدة الدخان من سيريك بعد انفجارات مجهولة.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/80028" target="_blank">📅 01:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80027">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فانس: سيؤدي العنف من إيران إلى ردة فعل قوية.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/80027" target="_blank">📅 01:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80026">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فانس: سيؤدي العنف من إيران إلى ردة فعل قوية.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/80026" target="_blank">📅 01:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80025">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
وكالة فارس الإيرانية:
الحرس الثوري لم يصدر بعد أي بيان بشأن هجمات اليوم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/80025" target="_blank">📅 01:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80024">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf3657c0e.mp4?token=bSJTDhoh2UP2_gEHTxs83wcSrFpzjptWJorKS9fB7Q2SD8bjm52ILwPCv7hk5Ao6jewEU1CRlpbfnVB0zsW1zGxdiaiGYOUgR21vr6LHdoZfDjzLZTXijyx4v0kYnxIM8cLR8ntLi6PaWX-UXCSsRYpbCoEFO2Dr5Vcz65CQJjYoY7ptpDxMCZNyWZs4ZgbK5mo8sU6N1XxQ-rfd-1zRQEFuABFlevVe5_y8pQ-G3UZPrSXcqeEQj2buy_YSKjMg-tzWN0uXs1iD4U7i6UjVSD42rFTBAHHYLwzS554iPqlncgeLQVv0gYQztcm1-pgNm03OyW4_hC25BLI7do5rHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf3657c0e.mp4?token=bSJTDhoh2UP2_gEHTxs83wcSrFpzjptWJorKS9fB7Q2SD8bjm52ILwPCv7hk5Ao6jewEU1CRlpbfnVB0zsW1zGxdiaiGYOUgR21vr6LHdoZfDjzLZTXijyx4v0kYnxIM8cLR8ntLi6PaWX-UXCSsRYpbCoEFO2Dr5Vcz65CQJjYoY7ptpDxMCZNyWZs4ZgbK5mo8sU6N1XxQ-rfd-1zRQEFuABFlevVe5_y8pQ-G3UZPrSXcqeEQj2buy_YSKjMg-tzWN0uXs1iD4U7i6UjVSD42rFTBAHHYLwzS554iPqlncgeLQVv0gYQztcm1-pgNm03OyW4_hC25BLI7do5rHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش اللبناني يطلق قنابل مسيلة للدموع لتفريق المحتجين عند طريق المطار</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/80024" target="_blank">📅 01:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80023">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODSOj_pKlRJSd1nQQIA27gKkH6uhX4AVl6dybb-QXQkJqlrRzL0Q1DXFVf_7MKY1EyILDdLvwvJeR8HEVxNRFOD-gNa_eQej-ArBVKXsas3aGXHXsF7EiJ2InjajODJtkKBPlc3hK28_D3WLUTOYz6uZ7o0PbHvJfWjkL3iq31NiICBjhVcUOU18g754fIgcwOcGCVLNfHdg0PKJblNEdXwPjFT75oBrzBRBpO2okcQVEZl9DcPpG_i5i1BlRmwwOEDbZgwuAF0UOuiHab0ZpwY808wflG-58YyNhJysFvY0JrFYJNlHin7G-7bgs2Tdwfrsfi7cDQz6aSRkC7bGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس لجنة الامن القومي
الايرانية
ابراهيم عزيزي:
مرة أخرى، هاجمت الولايات المتحدة إيران في خضم المفاوضات. ‏أثبت الرئيس الأمريكي المهزوم مرة أخرى أنه لا يلتزم بمبادئ التفاوض ووقف إطلاق النار. ‏إن هذا الانتهاك غير الحكيم لوقف إطلاق النار من جانب الولايات المتحدة سيؤدي بالتأكيد، كما هو الحال دائماً، إلى تراجعهم وندمهم على ذلك.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/80023" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80022">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مسؤول أمريكي لفوكس نيوز: الضربات على أهداف إيرانية "مستمرة" الآن.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/80022" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80021">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">إيران | الحرس الثوري الإيراني:
- نؤكد أن هذا العدوان لن يمر دون رد، وسنختار الزمان والمكان المناسبين
- نحذر من أن أي حماقة جديدة ستُقابل برد قاسٍ يُحطم أوهام المهاجمين في المنطقة</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/80021" target="_blank">📅 00:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80020">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d5d0dc8f5.mp4?token=ekvU6z45mbOGRmmtt_w7HVHJYdCZT8uxbHymiJOXQfHVpn8Cc6fYu8Iw6jIFo04YDdYNNITrqgDnrgTXoo-s6dMAl-gd2xYsKfJ9MA-iAAflklJWt09kazZMNZW5ABS4_goYNbhxeZ4d7xrb-XYEjEb5T15eH_j46khyzoNQ_EizoDIVwLfi0dcD9-fSd1c47iP40k5pj4BZr5ROgJac4knY8_8hBj8NFl7hgToNO1bVAAmKAqmUa3pwNxrOSyDiM6iZMM5THM-EDGk2QCLPL_-Jw3Ii9TFzgcAKBKHVn-ZcCIldKvodyIvEFOXGZ2bz0-ETKMqUj8PtsHH_qPSurA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d5d0dc8f5.mp4?token=ekvU6z45mbOGRmmtt_w7HVHJYdCZT8uxbHymiJOXQfHVpn8Cc6fYu8Iw6jIFo04YDdYNNITrqgDnrgTXoo-s6dMAl-gd2xYsKfJ9MA-iAAflklJWt09kazZMNZW5ABS4_goYNbhxeZ4d7xrb-XYEjEb5T15eH_j46khyzoNQ_EizoDIVwLfi0dcD9-fSd1c47iP40k5pj4BZr5ROgJac4knY8_8hBj8NFl7hgToNO1bVAAmKAqmUa3pwNxrOSyDiM6iZMM5THM-EDGk2QCLPL_-Jw3Ii9TFzgcAKBKHVn-ZcCIldKvodyIvEFOXGZ2bz0-ETKMqUj8PtsHH_qPSurA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النظام اللبناني يرسل تحشيدات كبيرة للجيش الى طريق المطار في الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/80020" target="_blank">📅 00:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80019">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzuMAoCBQb2kBwIcrkkKqrSVF3XmB1g1kBF_GFDftkdl28FcJcYQMG-zV7zeVmwcWPZ-P4NTW8rAMrKXQVu1woxd3y19NMDOg6QX9jHzQ-X7GP-QafuoSesCNUJRzQS2KbqJA3yRmAU7sMmeXFkzeTP9Mm-FB_J_XN9coBe_SlErSaLnsO4nv513epvc_9SVJsdcE9zOgOYQHhfLlO7SSb3i_wxbA7D7kbSsSSO0oIwFokhTpYX9wMlBxih0gXqV-kUXij2DmAxdDZVvwolR0qK88d9LIKI0FiLDVuw7J2rtNo57OywaekxNU6Yt0u_Oemmk7zwcZpqJM-ZgvfgbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشاط لطيران أمريكي غير مسبوق فوق البحرين الإمارات وعمان</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/80019" target="_blank">📅 00:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80018">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK4kVQRWPSM1xKQFSXHiB_x0bDt5rz5PSs3Dtw5tdqCyssWQLthbTRUrI6nLYzl8MVgR8S_POcnT0kWDhCuFf5DG7G54jtahJF1y85iLPMvxPTSvSEo77nXURZR4W6RYVyGVN1qXrS61EbzXCCCeZhYcCopCc3a8XEwvQ9K5_t92L4qCFC5utSFbRpdsVjVGjW10k1Li-OW5n-BY_zYlGuwNy3ly5_6w0w3etVRPQuIKQs3UFdzkfQM5vW6nxpplYUhRCb7rhGVpN4zSx36qUAPu0AldYHZWHtpPi4uAkOWHOHtuwBiKCbzLu0xtwmmbF5pyN04BGtejeMZdIB8VUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد الغضب الشعبي في لبنان بعد اتفاقية النظام مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/80018" target="_blank">📅 00:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80017">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxzTa9Tk9elwYra8RY9NIRlpjNZ20NKYqukuZYp6BSlIF2hNB7Zb06rGU50ys6G6IdCOIlS9lbMeTCRPlxglt5ot6BXXN_mMY70F1q3kq50N_gp7RJyAsjDFQP8iqVCA80Wj0xDhEm396RTa7-ruL79F37cbHAgChA3lBmUMwiW921WH3NfMTWm4vjcEy02YFDi1WU2E3MLpKUVtGmAAgSR_4XebaUKLVKdWO-eTdEiEsal1pYdd07VJ2pXBE_ST2f_P9CdogNKX9b5_2zkZifQoxWektbj1vGE-vgFaAbgWu0IBw447t2_chHPKACvVlAIWbX3NcEZvG1Rghg_ipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السنغال تسجل الهدف الخامس في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/80017" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80016">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4eea0f59.mp4?token=NgkeHUAW8OilXRM1vsUCZEcCsNtTTRJLXd2OC-wF6dP8mQdEC4Fo9YHz7NdAwIAk4Ph6u6Qa0el1PXWFItOGcsPOhhHUVlYn6bQlg_pkB8GgEEGDbrsYcnH5_WjoEJRt70yojQJaegUsKRR23OCKiMQTTIl-4KhfvaabEYjrvvDfbA_ARLmJb1aSooatE14t0_cBPrvToM7cIowlFntoBVbl7_eU9iqBnS73Ipswahbiy_NhQPfPNsD7M1py-SDKPNOsRi68N--3njytdjN1KCPahTyV6PHtkiBoxsg1Ld4EgOjHkrjagVItXtuBlnJga7LxhITkFPC-quJcI3wsww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4eea0f59.mp4?token=NgkeHUAW8OilXRM1vsUCZEcCsNtTTRJLXd2OC-wF6dP8mQdEC4Fo9YHz7NdAwIAk4Ph6u6Qa0el1PXWFItOGcsPOhhHUVlYn6bQlg_pkB8GgEEGDbrsYcnH5_WjoEJRt70yojQJaegUsKRR23OCKiMQTTIl-4KhfvaabEYjrvvDfbA_ARLmJb1aSooatE14t0_cBPrvToM7cIowlFntoBVbl7_eU9iqBnS73Ipswahbiy_NhQPfPNsD7M1py-SDKPNOsRi68N--3njytdjN1KCPahTyV6PHtkiBoxsg1Ld4EgOjHkrjagVItXtuBlnJga7LxhITkFPC-quJcI3wsww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
الغضب يعم لبنان بعد توقيع النظام اللبناني اتفاقية مع الكيان الصهيوني</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/80016" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80015">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
اعفاء مدير المخدرات في محافظة النجف من منصبه واعتقال عدد من الضباط والمنتسبين و ارسالهم لبغداد بعد عملية قبض كيدية بحق مواطن نجفي</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80015" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80014">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6017431c96.mp4?token=KA324WwRA5KtZKhn0nbAL8Cpb-UlNaK-DL4xj9iavlPRKF3K4rTGZ9fOYumo_qZzyuZlRvAyzRZVyVEVwBD5HH0xqCKEn_zB-AZOmwcXJaqdITQAv_DtXVl9My45bX6fYPyjKCS4OawA-f9Qwpy3zCUZ-f54tKdVpjGatKtJwwNJnx8MgInd5njDccfOkjYUhjWYHaU3MkrD7AuPQ2w4EH9E-pzPRuFUxH6dNxuakoXSHVbCdNyUbkU4LlevedZTRoY8ZJo6OahZ2OL_LmwuAAF4wtNYp8709hujY0CgTKVmUPtSACT8jnmeCgcVCwF2pV3cL0AyT7VPe4zI2g5STg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6017431c96.mp4?token=KA324WwRA5KtZKhn0nbAL8Cpb-UlNaK-DL4xj9iavlPRKF3K4rTGZ9fOYumo_qZzyuZlRvAyzRZVyVEVwBD5HH0xqCKEn_zB-AZOmwcXJaqdITQAv_DtXVl9My45bX6fYPyjKCS4OawA-f9Qwpy3zCUZ-f54tKdVpjGatKtJwwNJnx8MgInd5njDccfOkjYUhjWYHaU3MkrD7AuPQ2w4EH9E-pzPRuFUxH6dNxuakoXSHVbCdNyUbkU4LlevedZTRoY8ZJo6OahZ2OL_LmwuAAF4wtNYp8709hujY0CgTKVmUPtSACT8jnmeCgcVCwF2pV3cL0AyT7VPe4zI2g5STg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مشاهد للغضب الشعبي اللبناني في محيط السراي الحكومي في بيروت بعد الاتفاقية مع الكيان</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/80014" target="_blank">📅 00:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80013">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e30e9777d.mp4?token=uTKVSOTtCVL5-q0mI-vJTdcSnVCMK0bzWgXt3Ixip0kBl63Ry4Q40_42K0TNmhiVyCETYA8Wkfp94d6MWY889FeUQYAK4YjNxryp6T4Sz6HsmSB6ugr8G05GzEQhkWE5UxGAT2j9Frhn3Sic6IWPAwJhh6cYXNm1ZuP5-0QVTMqSzuYvooGo911MaAlnsin2swEdurt1Q5Yq8kPJyo-Lejr7SSYCgLZXweG8rqftWyzWntEAOD8aQT9Be0b1IfdlEmJ8vyu0IrBW4Lwiv2ceh9HxUHWFcI1Qfx-N9ieAZRqauzSbdrmZ28kDDjUccsluWPck_TY7vMIXHCNDeyImNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e30e9777d.mp4?token=uTKVSOTtCVL5-q0mI-vJTdcSnVCMK0bzWgXt3Ixip0kBl63Ry4Q40_42K0TNmhiVyCETYA8Wkfp94d6MWY889FeUQYAK4YjNxryp6T4Sz6HsmSB6ugr8G05GzEQhkWE5UxGAT2j9Frhn3Sic6IWPAwJhh6cYXNm1ZuP5-0QVTMqSzuYvooGo911MaAlnsin2swEdurt1Q5Yq8kPJyo-Lejr7SSYCgLZXweG8rqftWyzWntEAOD8aQT9Be0b1IfdlEmJ8vyu0IrBW4Lwiv2ceh9HxUHWFcI1Qfx-N9ieAZRqauzSbdrmZ28kDDjUccsluWPck_TY7vMIXHCNDeyImNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاصرة السراي الحكومي في بيروت بعد الاتفاقية بين النظام اللبناني والكيان الصهيوني</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/80013" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80012">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
امريكا تشن غارات على ايران.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/80012" target="_blank">📅 00:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80011">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">السنغال تسجل الهدف الرابع في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/80011" target="_blank">📅 00:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80009">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P11gr6GBpl_g1YmRKvVUSPu-AzSAeUfZKcQmEL-OJKU30KTYVnKfPDA1qvGdDNxQSNtk7YxLWmhbdBVB1Dg-fwzF6gYVFYqhp7k3ZXA_3ilk0hJVWZWjHuuvR_qfss4V6B6pfeBx4YQKMO16jAUs0m_fL2Fwaju63yc1aocWmpfPN-883ZnDmjFsrlQMe3xIsDMPRDXIx7jfnR0Gcwx-09_MQk4pm7MhvR6_Yl2UGzHLLdZAdOmUwn1UuGpVPeNK4k5CP5QwIhzmVH09d0Chss97jWi0iFe2og2RgSF-rctkgqBd3_8yIUKB8FhALC7jfwFXqzeef-8vXhTY5gnzPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzuSqSXIbLxDdKp-xW4hPFW9LElqhpQTHtYv9ARy7qVgnis93y6d-C8W0LKiTihkQxUyOcZm9eR4gkRKhS26UPLHwn_IUhhyhm3VXWWwuVykiaT9AqRbhhxsyULg2YDkeZsocHTAmcYndmPS03SFrg2JYhDMEJ8FYa1CWPrN9d--Sc1pW1VJhxE-OpjrTNhc_WXr1Kp677beHC1O7oCLAZsxqz_lopDuUHAStaluYY8Me4EKxd89KWFWqqmXU7S_64diEdkJmzdToh6Uc4FTzca_gL152c5suAeCc90subrv3MVIZQv2EMBDeN7mNFaMLF_UX8gfQ2qnrYQZApEXDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">النص المبدئي للإتفاق بين لبنان والكيان:  ‎ تؤكد إسرائيل ولبنان حق كل دولة في الوجود بسلام، ورغبتهما المتبادلة في العيش بأمن كدولتين ذاتي سيادة ومتجاورتين. وتعلن إسرائيل ولبنان بموجب هذا الإطار نيتهما إنهاء النزاع بينهما بشكل نهائي، ومعالجة أسبابه الجذرية،…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/80009" target="_blank">📅 00:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80008">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">السنغال تسجل الهدف الرابع في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80008" target="_blank">📅 00:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80007">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">السنغال تسجل الهدف الثالث في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80007" target="_blank">📅 00:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80006">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">القيادة المركزية الامريكية: قمنا بشن ضربات ضد إيران في 26 يونيو كرد فعل قوي على هجوم الأمس على سفينة تجارية كانت تمر عبر مضيق هرمز. أصابت الطائرات الأمريكية مواقع تخزين الصواريخ والطائرات بدون طيار الإيرانية ومواقع الرادار الساحلية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/80006" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80005">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
امريكا تشن غارات على ايران.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/80005" target="_blank">📅 00:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80004">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو يعلن عن توصل لبنان وإسرائيل إلى اتفاقية إطارية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80004" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80003">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو يعلن عن توصل لبنان وإسرائيل إلى اتفاقية إطارية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80003" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80002">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
امريكا تشن غارات على ايران.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/80002" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80001">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تصاعد اعمدة الدخان من سيريك بعد انفجارات مجهولة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/80001" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80000">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">السنغال تسجل الهدف الثاني في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/80000" target="_blank">📅 23:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79999">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">السنغال تسجل الهدف الاول في مرمى منتخبنا الوطني</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/79999" target="_blank">📅 23:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79998">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RptwyaIdaBk0c2HloTd9_Ejm_wCZfRbyrXGfgwN21AcNud8qrCaeDLBiL3I507O5w8y2v0sasyl4gnKSW7-NF1cU7R1638j9oUxkcpirGD_RqPg835MkeS4z4PoShAig46uRVAL-wvftWK5n3MX5yKMPHRNz9CLGXBOxU0oi8EalXShvB189xS65r2L7WWWDo0LZVKSwu3PIMwXWOOK2xKouRNvqvyUoHCqqKw77dvJ4pKarNN6a64w71htdX_c-hN4js9B9VNCfMY0Is7fdNLYF-NHciS00VyOd_9o3ZhIVSSYTWcGJX05gYinTd8MVRFZUQKypAeCTaIt9v5lqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماع دوي 3 انفجارات في جزيرة سيريك، مقاطعة هرمزغان في إيران</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/79998" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79997">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامب: انتهاك ايران لوقف اطلاق النار لم يعجبني</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/79997" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79996">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سماع دوي 3 انفجارات في جزيرة سيريك، مقاطعة هرمزغان في إيران</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79996" target="_blank">📅 23:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79995">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
ترامب يغط في النوم خلال كلمة لنائب حاكم ولاية تكساس.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79995" target="_blank">📅 23:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79994">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1696a6fb43.mp4?token=U5gDFyw8flCiNuKn94JH7nEIYPdDoyTbqiIgVdplR7FwPZPUdl8IGVTYBEtDQTrkBG5x7pGcqMwaAerkyBL8mjN-dkRrAxs70_NHvUJkz94KmjlmivksxdszwJiKj7FVHoPUuqTNOz32pfLKyG3JsPVnR4DzIc7oBT8t-ZgYaLnRxAmZfvRXwDnihTqaJtNxTeFE7dnxMBINlss7Hkc0PDGa4a8Nxapr9oV02ULVfeiFw4oQibsLnnd3HwG89QV23lTZRjhKh7CqDObJ1IcwVggLHYx_o72WqtthTp3s70sGfu_-5CfusPxLQcKvtmhYhDnQ6iCaoWXYYOrdy2g3Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1696a6fb43.mp4?token=U5gDFyw8flCiNuKn94JH7nEIYPdDoyTbqiIgVdplR7FwPZPUdl8IGVTYBEtDQTrkBG5x7pGcqMwaAerkyBL8mjN-dkRrAxs70_NHvUJkz94KmjlmivksxdszwJiKj7FVHoPUuqTNOz32pfLKyG3JsPVnR4DzIc7oBT8t-ZgYaLnRxAmZfvRXwDnihTqaJtNxTeFE7dnxMBINlss7Hkc0PDGa4a8Nxapr9oV02ULVfeiFw4oQibsLnnd3HwG89QV23lTZRjhKh7CqDObJ1IcwVggLHYx_o72WqtthTp3s70sGfu_-5CfusPxLQcKvtmhYhDnQ6iCaoWXYYOrdy2g3Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب يغط في النوم خلال كلمة لنائب حاكم ولاية تكساس.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79994" target="_blank">📅 23:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79993">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">السنغال تسجل الهدف الاول في مرمى منتخبنا الوطني</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79993" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79991">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">السنغال تسجل الهدف الاول في مرمى منتخبنا الوطني</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79991" target="_blank">📅 22:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79990">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2d55dce0.mp4?token=gsmH8uunb-lnIun2XhsdNqnBAtR8ftEN8E_ga5qPBruxs8l0wpf-gP_1UPa1BWhwoeHVblHLe1mlweQD4hbiviu_lMtBU0LxKEqgieWZU_NmZevcJx-dtWDMCnJfqh50VPh-M83xY1D3HA2NPUvs6my1sPXyd4mYAuSEpeom2yJebDqrWcGR4f5YAQLnUR5Uzez9_GBadC_WVZkLFppPoCBoN23L4c58HfD_uFdhAMEACCqcG9Mb74tHNO1CxphRz0dzMalEMasOq7WVAWNDr8PcDjrsCzehlFo8hpAXrpgLpYv4lWseP4akzNOErc2EAZ4k6rN7SP1kmoFtaC2cKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2d55dce0.mp4?token=gsmH8uunb-lnIun2XhsdNqnBAtR8ftEN8E_ga5qPBruxs8l0wpf-gP_1UPa1BWhwoeHVblHLe1mlweQD4hbiviu_lMtBU0LxKEqgieWZU_NmZevcJx-dtWDMCnJfqh50VPh-M83xY1D3HA2NPUvs6my1sPXyd4mYAuSEpeom2yJebDqrWcGR4f5YAQLnUR5Uzez9_GBadC_WVZkLFppPoCBoN23L4c58HfD_uFdhAMEACCqcG9Mb74tHNO1CxphRz0dzMalEMasOq7WVAWNDr8PcDjrsCzehlFo8hpAXrpgLpYv4lWseP4akzNOErc2EAZ4k6rN7SP1kmoFtaC2cKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في ليلة الوحشة.. انطلاق مسيرة الشموع في منطقة الكرادة الشرقية وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79990" target="_blank">📅 22:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79989">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsLThO0ssN8l198sKNM_0cgYdePcFJVhBbI-ey6qNKtxoCnugKO9shorDfPl-j6kVgGWLtMX1BJWxc_Mjt9_1myaWWJyMpxVyk952yhWG45Zm4Y2N7f3MC6KW0uXq9at4qD1VOFmHIstP5yUhlLwM-g2gL6tPGs22mTECidfVkpp8c7WEu0xNkNUbHlGq6nRt3agFTDIQ4WrkLcTfSOibhptHsk0md8phivexI9R9_odw3yxUtjqiAH3T_qkBaDsIxSy5pGerIk47-ShBFVQcB0Wk4oH9Kl84RBNUPvDBAKxQhT1W7F_IsMZH7bTZdZf3K6wxjNOUnIS2imZ2rl0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇮🇶
🇮🇷
النائب عن حركة حقوق حسين الدراجي :
اليوم ببركات الإمام الحسين "عليه السلام" تم ضخ الغاز من الجانب الإيراني بكمية 5 مليون متر مكعب باليوم علماً أن معدل إنتاج الكهرباء في البصرة تجاوز معدل الاستهلاك وإن التشغيل الحالي افضل بكثير من الشهر الماضي، وسنبقى نتابع الموقف كما وعدناكم أولاً بأول، ومن الله التوفيق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79989" target="_blank">📅 22:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79988">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">استخبارات قيادة عمليات نينوى للحشد الشعبي تعتقل شبكة مكونة من ثلاثة متهمين (اثنين من الجنسية العراقية وآخر سوري الجنسية) ​ضبط بحوزتهم مادة (اوكسيد الزئبق) شديدة الخطورة والمحظورة دولياً</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79988" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79987">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامب: لا تزال إيران تمتلك بعض القدرات، ولكن ليس الكثير.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79987" target="_blank">📅 22:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79986">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏ترامب يهاجم وسائل الاعلام الامريكية التي فضحت كذبه: ‏زعمت الأخبار الكاذبة أن إيران أقوى بكثير اليوم مما كانت عليه قبل أربعة أشهر. ‏إنهم يتوقون لإبرام صفقة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79986" target="_blank">📅 22:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79985">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
🏴‍☠️
ترامب: ‏إسرائيل رفضت المشاركة في عملية اغتيال قاسم سليماني.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79985" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79984">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">#ترفيهي
🌟
‏ترامب: سأكون صريحاً -- أعتقد أنني سأكون أعظم شيوعي في التاريخ.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79984" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79983">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🌟
التغطية الإعلامية ليوم عاشوراء
:
شهدت التغطية الاعلامية مشاركة واسعة، تمثلت بوجود (7) عجلات للبث المباشر، و(84) جهاز بث مباشر (LiveU)، و(676) كاميرا صحفية، فيما بلغ عدد الإعلاميين والصحفيين المشاركين (1011)، بينهم (102) إعلامي اجنبي
(12) إذاعات محلية و(82) قناة تلفزيونية شاركت في تغطية مراسم الزيارة، إلى جانب (26) وكالة أنباء عربية وأجنبية، فيما بلغ مجموع ساعات البث المباشر (1006) ساعات خلال عشرة أيام، كما نقلت (87) قناة محلية وأجنبية البث المباشر عبر خدمة (Feed Clean).</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79983" target="_blank">📅 21:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79982">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180ec771cc.mp4?token=SuMuZR9xa7ADmFeN9gyiRk-yLBqcdXxyxtFUqf0oJV-kHRtm8LHGQ5aRxOlcE6cREl4sGAwG6oQB8Thdj-VyTxT-L88m5bp0I6AWwtwMnpQG7MmenU7zMyrZE2R-VwN26YAQtghCuqLZAYjgVezK8aRfgsk-vW2PgeUHzRMXUiGtSP0XTRx_r_pYc7-oIWvnBh_veyiD-nc9r10TovMtZsMrdQOG-VBhQJ1QjHJEJ5vz9wVF9VYC4wMkQ_5SUV6Y2hkauieSvHCY_O-bSpSyIInJQVgo_8gz95ujbS01ipBwIzbWi-dZWlsVeYoJJxxqyCVf74-_k2YlghN13TF3WE33_Kd0TI-iFwrXdAcYHFH1Wqw_y1OlvxrsH65yfMeLnsykpwdsjhcs8ULcADKPzsEqAT8rW_2gUHDnekTKcrnoAHKlgvVQOi3I9I9uVKi02X0bR421ypY3XtLQJ5TK_APuxXk9e3RrUhG9LA5_xESwg03f59dTPm6KEX7ylkLDogBO_wRRDSKs_HNMA__94CMfC1o8cXaPH-7Y4jgmIlEmYM4OlwdKFiI5z_7lQbG8V4xlHDSUUuui_acXgh6O9gJ4H0F4X972uYUKbU5fz13QjLqnH21M_0L7_ja-hQOshOcMllp2w-HSxw1Qc4rjt1vMXSxAxnh6YIW--c54pSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180ec771cc.mp4?token=SuMuZR9xa7ADmFeN9gyiRk-yLBqcdXxyxtFUqf0oJV-kHRtm8LHGQ5aRxOlcE6cREl4sGAwG6oQB8Thdj-VyTxT-L88m5bp0I6AWwtwMnpQG7MmenU7zMyrZE2R-VwN26YAQtghCuqLZAYjgVezK8aRfgsk-vW2PgeUHzRMXUiGtSP0XTRx_r_pYc7-oIWvnBh_veyiD-nc9r10TovMtZsMrdQOG-VBhQJ1QjHJEJ5vz9wVF9VYC4wMkQ_5SUV6Y2hkauieSvHCY_O-bSpSyIInJQVgo_8gz95ujbS01ipBwIzbWi-dZWlsVeYoJJxxqyCVf74-_k2YlghN13TF3WE33_Kd0TI-iFwrXdAcYHFH1Wqw_y1OlvxrsH65yfMeLnsykpwdsjhcs8ULcADKPzsEqAT8rW_2gUHDnekTKcrnoAHKlgvVQOi3I9I9uVKi02X0bR421ypY3XtLQJ5TK_APuxXk9e3RrUhG9LA5_xESwg03f59dTPm6KEX7ylkLDogBO_wRRDSKs_HNMA__94CMfC1o8cXaPH-7Y4jgmIlEmYM4OlwdKFiI5z_7lQbG8V4xlHDSUUuui_acXgh6O9gJ4H0F4X972uYUKbU5fz13QjLqnH21M_0L7_ja-hQOshOcMllp2w-HSxw1Qc4rjt1vMXSxAxnh6YIW--c54pSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🌟
بالتزامن مع ترويجها لسردية فصل الدين عن الدولة في بلداننا.. رئيس الولايات المتحدة ترامب في خطاب ديني: ‏ لكي تكون أمة عظيمة، يجب أن يكون لديك دين وإله. ‏إذا لم يكن لديك ذلك، فلن ينجح الأمر، أليس كذلك؟ الدين عاد بقوة. الدين في ازدهار ملحوظ. لو كان سهماً،…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79982" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79981">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
🌟
بالتزامن مع ترويجها لسردية فصل الدين عن الدولة في بلداننا.. رئيس الولايات المتحدة ترامب في خطاب ديني:
‏
لكي تكون أمة عظيمة، يجب أن يكون لديك دين وإله. ‏إذا لم يكن لديك ذلك، فلن ينجح الأمر، أليس كذلك؟ الدين عاد بقوة. الدين في ازدهار ملحوظ. لو كان سهماً، لكنا أثرياء جداً. عندما بدأتُ العمل في عام ٢٠١٦، كانوا يريدون تجريد عيد الميلاد من روحه. لقد استشهد مؤسسو بلادنا بالخالق أربع مرات في إعلان الاستقلال. أربع مرات. ولم يُذكر اسمي ولو لمرة واحدة. أنا مستاء للغاية. ولا مرة واحدة، ‏في ظل حكم الديمقراطيين، استُهدف الكاثوليك من قبل مكتب التحقيقات الفيدرالي. ‏سُجنت الجدات المؤيدات للحياة بسبب الصلاة. ‏تم طرد أفراد من جيشنا من القوات المسلحة بسبب معتقداتهم الدينية. منذ فجر تأسيس بلادنا، بُنيت عظمة أمريكا على أيدي المؤمنين. أول المستوطنين الذين وطأت أقدامهم أرض هذا العالم الجديد في جيمستاون، نزلوا من سفينتهم، ورفعوا صليبًا، وسجدوا للرب في الصلاة. كان الإيمان هو الذي قوّى رجال الميليشيا الذين صمدوا في ليكسينغتون غرين وجسر كونكورد. ‏في فيلادلفيا، قبل 250 عامًا الأسبوع المقبل، استحضر مؤسسونا الخالق أربع مرات في إعلان الاستقلال... الإيمان دفع الرواد إلى السفر غربًا، والإيمان قاد الأمريكيين إلى إلغاء العبودية، والإيمان بنى هذا البلد ليصبح أكثر الدول تميزًا في تاريخ العالم.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79981" target="_blank">📅 21:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79980">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1cc7c8a5.mp4?token=uVT0g6hwUxAT8Mif-5ii6UmukhauWbJPDRovYg4S1ut1fY1LpEmktqkYbaocPIVi6mp8uXYpf2bigMrIi7XNdLsnDlZTNTLLyxYgNHbL9YJvQJ_C-6dgcngTm02fjtZA1LPo4csdoyP3EDIy_gCH_5Cfzvv-2EQkOFMIIdAR2QGEkK-UgLDT-pPfB4k_ZkOPWMrvMyBXCmF3xbBoSffWCYtCAvt6VTUhKLzbVOC_IyiKBvpgzLH4hpYFk6vQ38DI-do5VvlFjhMCHRjvkZIHA-JSMPsNLaEbtPo9B_Uhp48fgfI5laQM2XrvW-1R82sAsM4Q0xN7HlL0Wj4zpd_hvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1cc7c8a5.mp4?token=uVT0g6hwUxAT8Mif-5ii6UmukhauWbJPDRovYg4S1ut1fY1LpEmktqkYbaocPIVi6mp8uXYpf2bigMrIi7XNdLsnDlZTNTLLyxYgNHbL9YJvQJ_C-6dgcngTm02fjtZA1LPo4csdoyP3EDIy_gCH_5Cfzvv-2EQkOFMIIdAR2QGEkK-UgLDT-pPfB4k_ZkOPWMrvMyBXCmF3xbBoSffWCYtCAvt6VTUhKLzbVOC_IyiKBvpgzLH4hpYFk6vQ38DI-do5VvlFjhMCHRjvkZIHA-JSMPsNLaEbtPo9B_Uhp48fgfI5laQM2XrvW-1R82sAsM4Q0xN7HlL0Wj4zpd_hvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في ليلة الوحشة..
انطلاق مسيرة الشموع في منطقة الكرادة الشرقية وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79980" target="_blank">📅 21:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79979">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏مسؤول إسرائيلي: سنحافظ على الشريط الأمني على طول الحدود داخل الخط الأصفر بلبنان.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79979" target="_blank">📅 21:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79978">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNJKrK8MYnLHKGei3mk1sH34ztcsLL9-scYPUNxfYu2sG_LLcXzbONBTOlUvvZNSdZ6KGt-Xfxouv0-D4TDuGCidanGNMSkkjA5Ob3gskXRv5EFtMaNaWLW_44yL0MJ4Vg8_Dq2m7uZ2yEnK_n3OSe4oA-KYJ6BXWPclzrvhjnfUaWYiWweTeLzHVMyNkP4eXEr73Ruux3XcCbpO6xC17vFHaSjpcQN7qTu60YsdAt0b3nfHyab17Dnp6KyBcJYTU9bLqZmiWLscX-xQnDlrpMEOdny0CAfhsuQ03gAPIdHWZuIFo-y4MMAuHA6PD_QFLnCpyJKIneiB3eEWdSOJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
رئيس الوزراء الباكستاني:
مع اقتراب يوم عاشوراء من نهايته، نُعرب عن أعمق مشاعر الاحترام والتقدير للتضحية الخالدة للإمام الحسين (رضي الله عنه) وشهداء كربلاء. إن ثباتهم الراسخ في سبيل الحق والعدل والكرامة الإنسانية يبقى مصدر إلهام خالد. ‏الحمد لله! لقد أُحيي هذا اليوم المبارك في جميع أنحاء باكستان بتفانٍ وصبر ووئام. نسأل الله أن تبقى روح كربلاء نهتدي بها نحو الوحدة والرحمة والعدل. ‏نسأل الله العلي القدير أن يبارك باكستان والأمة الإسلامية بالسلام والرخاء الدائمين. ‏آمين.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79978" target="_blank">📅 21:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79977">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_-BHztCNi48_-IIc2J4Ut9L4rn4V7xB8lhVB8AnKYB469Gu-5Lj89UNPb1CMJkoOH6D0R3PCy8SxJ-yTcibk1qkN2pV848ss_Ar3ptpePtSbPEsmIzXMSf6GaZt640LyrE6nFMl_PqBqiKa9n5LvWv_Xny9DerfODHBfhyTuUzfDEXonevmmkmxijacrIkTGrZe3vUUijUOTumdZneK94nIFgZnImBat6KHfReHQCFdPUoslHQK0zNIjX9847W6GXMhpUBLgWuVYuiwPG27jRP54GZG201NnjL1CK5nip0y6W4xYFUrJviYoZrZIwmpgngOPC1y-dfWrhkAZ7yU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرطة محافظة كركوك شمالي العراق تغلق الشوارع في محيط جامع صالح بهاء الدين في الحي العسكري بعد انباء عن وجود سيارة مفخخة</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79977" target="_blank">📅 21:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79976">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴‍☠️
🌟
لبنان وإسرائيل يوقعان على ما يسمى بـ "الاتفاق إلاطاري" برعاية أمريكية.</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/79976" target="_blank">📅 21:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79975">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmvzpMIEOcT01-7bOpEAjRuzS3T2OyBPFLArMBzFnd8JVRHHP6HYViumPs4nfsHoc2oPLwfOuJkfipBXqstMtqhftDQtHakIDOAx40XM6eeK8iN5ImXGw7ZqitKsltIWAdiX8SS69G_ldm4MssVOyeqYl_VgI06nFXphQwoS8e1oMeFzAkOXkDJwXfebz8xf5x748Bp1wzreZ8SfbX3LXlv210H9Q7tvokoEg_8UaY8uV_mbvC9MfVya6yhlTJ5Fq3HZwaQuujQskWoIz7ZvgC_xd7ZreHVgfPDW9kvmmBl8T7pkeSA4Q_Cvy2h1RoetBtJtKXqSaKuO6GTxUYG3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو يعلن عن توصل لبنان وإسرائيل إلى اتفاقية إطارية</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79975" target="_blank">📅 21:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79974">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGE3tCBGrfFIHBLvFtIZfpabrX3xsNoZaVPaAsFC3Yl7K_Q5FOhMhRy3sQcNqkCOWO8fMIoBmSX6KRFUTig-GrKDpbWCJAkcsa2kiaas-7tVt2BlJbds3nIBH4eg1QEYBsHzml9m_cFLPHgqpS_ZivD5QPSK2qDwd_u8EHQngXOWJFxS8t-k1V23PHYhJ2s5t31Ft9rw2uuEtebUD4pWfx7rFvvD7W-yNuIX8-_cFoHuP8gZzOrgjC2XkP8WBBCcPlWnDHOK6Vm1lgb2SVC1MX4vIiUH6l6LuFpzz0iO4o6MhFCxNp2rbPhbaOOw1UQpg668CAnB3mWEgRpedjIC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
سأتحدث في الساعة 1:30 مساء إلى تحالف الإيمان والحرية، وأحد البيانات التي سأدلي بها، ربما أهمها جميعا، يتعلق بالانتخابات الأخيرة للشيوعيين في بلدنا. من السهل جدا بيع الشيوعية. سأكون أعظم شيوعي في التاريخ. سأعطي إيجارا مجانيا، ومنازل مجانية، وطعاما مجانيا، كل شيء مجاني. لسوء الحظ، بعد عامين أو ثلاثة أعوام، سيفشل البلد الذي يحدث فيه ذلك. إنه يفعل ذلك دائما، ثم ستبدأ في العيش في البؤس. لن يكون هناك طعام، ولن يكون هناك سكن، ولن يكون هناك جيش، ولن يكون هناك شيء. ستكون العالم الثالث بكل الطرق، وسيعاني الجميع أو يموتون. يؤسفني أن أقول، لكن اغتيالات أولئك الذين يعارضونهم هي عنصر مهم جدا في أيديولوجيتهم.
إنهم حيوانات! في كثير من الحالات، ليسوا أذكياء، ولكن في بعض الحالات، هم كذلك. من السهل عليهم الحصول على متابعين لأنهم يقدمون وعودا يعرفون أنهم لا يستطيعون الوفاء بها، والدوموقراطيون لا يقاومون. من نواح كثيرة، يسمحون لهم بالسير في طريقهم الخاص. إنهم يخشون أن يخسروا انتخاباتهم، إنهم يخشون الصراع. إنهم ليسوا أذكياء بما فيه الكفاية أو أقوياء بما يكفي لمحاربة هذا الطاعون. إذا قاتلوهم بالطريقة التي يقاتلون بها الجمهوريين، أو أنا، فسيكونون منتصرين، ولكن ليس لديهم الشجاعة للقيام بذلك. هؤلاء ليسوا دوموقراطيين اجتماعيين، هؤلاء شيوعيون صلبون بلا إله. هذا هو أخطر تهديد لبلدنا منذ وجوده قبل 250 عاما. أليس من السخرية أننا نحتفل بعيد ميلاد مهم جدا، وبدلا من الحديث عن المسيح والحرية والانتصارات من جميع الأنواع المختلفة، نتحدث عن تهديد آخر لأسس أمريكا.
سيهاجم هؤلاء الشيوعيون الذين لا يرحمون جميع الأديان ولكن، على وجه الخصوص، المسيحية - يفعلون ذلك دائما. جميع الدول الشيوعية تهاجم الأديان بعنف. كما تعلمون، لقد ضربنا نيجيريا مؤخرا، وأنهينا إلى حد كبير ذبح سكانها المسيحيين العظماء. إنهم يعرفون أنه إذا ذهبوا إلى أبعد من ذلك، فسيكون الهجوم أكبر بكثير، وفي ذلك، لا يريدون التورط. أنا أنقذ المسيحيين في جميع أنحاء العالم، على الرغم من أننا لسنا في تلك البلدان المختلفة، من خلال ضرب هؤلاء الإرهابيين بعنف وقوة. سيغلقون كنائسك، وسيقتلون شعبك. هذا ما يدورون حوله. هذا هو أكبر تهديد لبلدنا منذ تأسيسه قبل 250 عاما!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79974" target="_blank">📅 21:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79973">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو يعلن عن توصل لبنان وإسرائيل إلى اتفاقية إطارية</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/79973" target="_blank">📅 21:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79972">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">في ميادين الجهاد وميادين الشعائر حاضرون
انهم رجال المهمات الخاصة
#كتائب_سيد_الشهداء
#لن_نساوم</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79972" target="_blank">📅 21:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79971">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1sOUSXDHEhk8ghneA5zhbFyUwwF4WvP6L4_kEV43U2UrNbFHHnaIKGUTcX7LpJTZGw6L5wqHobEoG3qAQckdYJDrKH-jBkot8RrWaVHjR1yybKj4YTTGsGkMuu4W0d9-t-vKWQ_pfIDERhsUzPElyms9b6bf9IozapnowFC583FNGmQWI2upP-d9ciOEt3L_lC2Qc319fu2g_UepRrXXnrNBPtEAnmAzKjGbFey14pYVU2A_3POCOjvlbU7nn484N33kAZAQ_ztfUOlD85DLP3ynmb0vmETgRae3GPI-8DCFnCIs_Izq1MCAyYn52kPIS8X0ZhcLdN8cfNg4TSLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
تشكيلة المنتخب العراقي في مواجهة السنغال ضمن الجولة الأخيرة لدور المجموعات في كأس العالم 2026</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79971" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79970">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPOJDnFidkQ2_0XNNiqDofGpFiJdHWLPHLFmTyNm3JhvgRguci659ASbmMY1MaQ2_q_cLJhpYqXz-8ICDQzby32aZ2N3shUG_P87YsyfT8XHwWX9HhLuosVNCNd-PArc3bXC8gJe5eccdy_lghGXvIFzO-hRuaiUG9I0UNrGnHiNIxRgMwEmdfrxp03K4RpymwUF7nlcMosNlQTagvVE4K9PJ-fHntw5AaW9jckIcMUTs74kXIlYLNND9yBedByw5_2EwqIOHkNIvtK_3jMS9bfEqUuaN6waYdtLnDJ3CCooaT7Qg9MYZp2xH0mMaw806I94uYxkiTzUGcPuZVM3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي
:
-
في العاصمة بغداد نفذت مفارز الجهاز عمليتين منفصلتين حيث تمكنت في الأولى من تحديد هوية أحد الأشخاص في قضاء أبي غريب بعد رصده ينشر محتوى عبر منصة "تيك توك" يتضمن الترويج للفكر الداعشي المتطرف، وإثارة النعرات الطائفية، والإساءة إلى الرموز الدينية، فضلاً عن تمجيد الجرائم الإرهابية، وقد ضُبطت بحوزته ثلاثة هواتف نقالة وعدد من الكتب التي تدعو إلى الخطاب المتطرف.
- العملية الثانية، أسفرت عن إلقاء القبض على متهم أقدم على تمزيق راية خاصة بالشعائر الحسينية في منطقة حي الجهاد، في محاولة تهدف إلى الإخلال بالسلم المجتمعي.
- في محافظة كربلاء المقدسة، وبالتنسيق مع العتبة الحسينية المقدسة، تمكنت مفارز الجهاز من معالجة حادثة تجاوز وقعت بالقرب من مرقد الإمام الحسين (عليه السلام)، بعدما أقدمت مجموعة مكونة من (١٤) شخصاً من حملة الجنسية الأجنبية على الاعتداء على زائرين آخرين، في حادثة كادت أن تتسبب بإثارة فتنة بين الحشود الكبيرة في منطقة بين الحرمين.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79970" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79969">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
حزب الله:
تنفي المقاومة الإسلاميّة نفيًا قاطعًا ما نشرته جهات رسميّة تتبع لجيش العدو الإسرائيلي حول سيطرته على تلّة علي الطاهر عند الأطراف الشرقيّة لمدينة النبطية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79969" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79968">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
‏الإعلام السعودي: إعلان عن اتفاقٍ إطاري بين لبنان والكيان الصهيوني بعد قليل.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79968" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79967">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOuHc5DAM4UycWnEgLHy5VreO76g0SAxFYyWpxTphbsQcPslr0g1rdIlxp-Y975N5UMvQZhVJhhLyUhLOYG3jLBkqKX8y-AutGeRnNGU_Q-EitivR0Ke904ddMFy80jyDDpCpDSL9TuodTudzpZWqehP5SaBVFKnLbTd3oje_gu-z70M0O8AuxxngLwaNEO91q4UroT7mr0WiJCt9KJrqwpANh0_LTOAb1_dH6368fE4y8ZtBd8_EJ-2ArJ0LmjUAGAMnjHqECxz_-lBiqCBVD6nu_ftxQZC_B67yGNS-6gTyTBuTTDqDTQW424vPmThZFspxRYHat6sHzLLdaB2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب:  أطلقت إيران أربع طائرات بدون طيار من نوع One Way Attack على سفن في مضيق هرمز.   ضربت إحداها بقوة السطح العلوي لسفينة شحن كبيرة ومكلفة. لحقت أضرار، لكن السفينة استمرت في طريقها.   وقد أسقطنا الثلاثة الأخرى.   من الواضح أن هذا انتهاك غبيًا لاتفاق وقف…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79967" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79966">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvBp5kdY1-Yn0aVph24_1UjkZyGvbHXJ-469oLiZrJKtVLnh2eSvYSD4B66bbwM8631vvQ3jL-TijNhEtcSa7ixcP363QnGpvDZSr81NxmAHUcsylmodgOW47RTrhazOhGCSls0R3AyzgvHCEMAIHGR5cSjdAK9H_glzJA3GsDiTzDQ0zFIsQ9EiMv6t19xWJ0ouVhPcqCZljaj9vLejce7Buc8aRrEie_2xP16q7PjKkhyFjdaI49_ypr-o27HDRl0c7SIMXeBuPE8zQzNV3yqFEBlW-pQFpNRaRbhwLSnt8WfVF2vTyd-ZIgQgaDoKBozUKs2dJlMuQU9G2J537g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
أطلقت إيران أربع طائرات بدون طيار من نوع One Way Attack على سفن في مضيق هرمز.
ضربت إحداها بقوة السطح العلوي لسفينة شحن كبيرة ومكلفة. لحقت أضرار، لكن السفينة استمرت في طريقها.
وقد أسقطنا الثلاثة الأخرى.
من الواضح أن هذا انتهاك غبيًا لاتفاق وقف إطلاق النار بيننا.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79966" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79965">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نايا - NAYA
pinned «
🇮🇶
🔻
Dear brothers and sisters, in light of the reports regarding the presence of the martyred leader Immam Sayyid Khamenei in Iraq during the funeral procession, Naya Channel has launched a dedicated channel for designs related to this occasion. Please join…
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79965" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79964">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
🔻
Dear brothers and sisters,
in light of the reports regarding the presence of the martyred leader Immam Sayyid Khamenei in Iraq during the funeral procession, Naya Channel has launched a dedicated channel for designs related to this occasion. Please join via the link below.
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/79964" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79963">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⭐️
مدير عام الوكالة الدولية للطاقة الذرية، حول ما إذا سيُسمح للمفتشين بدخول إيران:
من أجل الإشراف، نحن بحاجة إلى التفتيش. لا توجد طريقة أخرى.
هناك اتفاق، وللامتثال لهذا الاتفاق، سيتعين على الوكالة الدولية للطاقة الذرية أن تتمكن من الوصول والتفتيش.
أنا مستعد لمواصلة العمل الفني وأن أكون هناك في أقرب وقت ممكن.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79963" target="_blank">📅 19:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79962">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxAa6kpJ9rX7To2T2C7BY5Pbo4S-hNQ826DcigsFSgmvuJ6RlEeIPcHtq6cBlis3NsBSmTeDEDsOp0OnwoQP0h3qW5nM9wWq-NCUWLRvgKPnZP0XHAySzFzI3ptbzOkEPTJPQIbCJfzOVg0R26Vb9OMmmaeWSli_L3f_RkP1linaQR1eWElk_a9WEadkVMlhZkR9FeexsKNCIvnR8h3mFmj6Ny53F35LGicq8QZKN5wwnkfVXJRNPk0jR9B-e0ZAqeUXUuP4xCbEFRBsb2hCHW7jibASOR-lJxLSaD3hczdVI_MICuNbUatgAVA-XOvLjzF5PBCR40DdWbQjS3FXnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هناك شخصيات لا تختصرها الكلمات، ولا تكفي السطور لوصف أثرها. ومع اقتراب يوم التشييع، يستعيد الجميع ما تركته من حضور في وجدان الأمة..
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79962" target="_blank">📅 19:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79961">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭐️
مصدر لنايا:
توجيه بخفض إنتاج حقل الرميلة في محافظة البصرة جنوبي العراق، بسبب استمرار الظروف القاهرة وتذبذب وصول الناقلات.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79961" target="_blank">📅 18:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79960">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7f73f33d.mp4?token=s9eU6HNC-qj4Vauw3nXKgN1nYxGKDJySZf8aGVVvyAEcoyQDksxaJRbdZq5YX9n0X726k2eX8FKFHV3GqQzRj2D82uqmNzm56iMaYwdk__Ris3eGGUWYxBsJFfLS4rzp8cDQuE7UAljitnXFQtl-rRsHeYzkrq60Pu4B6CSczT489KUnFix1MV22hUtSG3yQ_eeJWFYBMDIPIPQVvJlUbyjIYrs1OEMWxmBe8sKrZ24mDmInU8zQHxGKTaR4XzN2WsqIAtddqSI5dz7E0NVPPkXdRI3cmtns2jsd-bOlIFJt3hYyv5fXKAszAtem0exYWhD8nghbj0_IRyfPoOWVPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7f73f33d.mp4?token=s9eU6HNC-qj4Vauw3nXKgN1nYxGKDJySZf8aGVVvyAEcoyQDksxaJRbdZq5YX9n0X726k2eX8FKFHV3GqQzRj2D82uqmNzm56iMaYwdk__Ris3eGGUWYxBsJFfLS4rzp8cDQuE7UAljitnXFQtl-rRsHeYzkrq60Pu4B6CSczT489KUnFix1MV22hUtSG3yQ_eeJWFYBMDIPIPQVvJlUbyjIYrs1OEMWxmBe8sKrZ24mDmInU8zQHxGKTaR4XzN2WsqIAtddqSI5dz7E0NVPPkXdRI3cmtns2jsd-bOlIFJt3hYyv5fXKAszAtem0exYWhD8nghbj0_IRyfPoOWVPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
وزارة الدفاع الروسية تنشر مشاهد لإستهداف محطة توليد الطاقة الحرارية في سلافيانسك الأوكرانية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79960" target="_blank">📅 18:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79959">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
بلومبرج:
أخبرت عُمان حلفاءها الأوروبيين أن السفن التي تعبر مضيق هرمز قد تضطر إلى دفع رسوم مقابل خدمات مثل المساعدة في الملاحة ومكافحة التلوث.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79959" target="_blank">📅 18:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79958">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⭐️
المنظمة البحرية الدولية:
14 بحارا قتلوا منذ بداية الأزمة الحالية في مضيق هرمز.
نحقق في استهداف سفينة أمس بعد عبورها مضيق هرمز من المسار الجنوبي.
أغلب السفن تستخدم المسار الشمالي الذي تسيطر عليه إيران بمضيق هرمز.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79958" target="_blank">📅 18:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79957">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">إعلام اماراتي : انتهاء حالة الخطر !</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79957" target="_blank">📅 17:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79956">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭐️
استمرار الزلازل القوية في الكرة الأرضية.. هزة أرضية بقوة 6.5 ريختر تضرب الفلبين وأخرى بقوة 5.2 تهز باكستان و ثالثة بقوة 5.5 ريختر تضرب جمهورية نيكاراغوا، خلال أقل من ساعة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79956" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79955">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79955" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
