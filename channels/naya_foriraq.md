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
<img src="https://cdn4.telesco.pe/file/VxHNi4-1PIcABC_8ukxBkWGsTcfBxwnIH5RS3Lr6F0I_t5O-B5AvQudH4EFE0DrhRo2BdtEZyfG6yNH4XYjRQwOY6txM7hQfbBR4wnZ2TOvfDgZYIOwOVUF2r3VhodrgRSYp3yIXxdud8ViYNnxQvWwK0C9hC4wkOe4058P2kjjdHz_W4PbwC7ZaJwkfsLV5P1NMD-vy0tD231AE5JsyBEf0aMbFr-rapv2PST1DOul9GsPfKdR-bB-lp42YRqinedcGs-C8EX8H3epw1VvoS0Yyrf85acL8jWFB2YBObiME9COEc2XXfwiLzc8M6-0gQDQ5Rr6D9NPKioouS3MQXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 06:57:32</div>
<hr>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
قائد مقر خاتم الأنبياء التابع للحرس الثوري الإيراني:
نُعلن لأمريكا وحلفائها عدم تكرار الأخطاء الاستراتيجية وسوء التقدير.  عليهم أن يعلموا أن إيران الإسلامية وقواتها المسلحة أكثر استعدادًا وقوة من ذي قبل، وأنها على أهبة الاستعداد، وسترد بسرعة وحسم وقوة وشمولية على أي عدوان متجدد من أعداء الوطن والأمة الشجاعة. لقد اختبر الأعداء الصهاينة الأمريكيون مرارًا وتكرارًا شجاعة الشعب الإيراني وقواته المسلحة الجبارة.لقد أثبتنا بعظمتنا وإرادة الله أننا سنُظهر سلطتنا وقدرتنا للأعداء في ساحة المعركة، وإذا ارتكب أعداؤنا خطأً آخر، فسنتعامل معه بقوة وقدرة تفوق بكثير حرب رمضان المفروضة، وسندافع عن حقوق الشعب الإيراني بكل ما أوتينا من قوة، وسنقطع يد أي معتدٍ.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75651" target="_blank">📅 00:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75650">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9pG3CsNcRZsJ9ap1CM0vJrC6mKtwwJQJfSusCxja4wHzZGMvmZ6fdxVvHY8t02AHOCeLjb75doppdj1BRrFWtbVg-PM0UI3011cc-3gHpyOS4y1LY_FbzEOWeNBiYSHVxJKB3-d77H8_4KFwTOGeXbg494ra_wOl7pL0FfoEGE4RwVIZZVV9NqEQhbGnQ7MJGhyqKF53TUfs5c2pQqRxmDD4mAMS9K8TEkXtbYxC4g4kjee-nohPtdMJKDx9lDhDYWVAiBlG1s4-O4zsjOHQuHSsKAZKEorpwv9oDSiR_UumkUQLA7kvaPv5nalVFSDdhhlyE0Llf26KdF8bOSqdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
عصابات الجولاني الإرهابية تختطف مواطن لبناني من الطائفة الشيعية من قرية كوكران الحدودية بين لبنان وسوريا وتطالب بفدية قدرها 500 ألف دولار.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75650" target="_blank">📅 00:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75649">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oV2wfzl-VCLvWEAT92KCYB0fOT078aG36MT9t-ELuM0r1qunm-pYv1fb7_PO5oi_zcr3FCp7ir_QRbX4XnNXU_VQfOPOgAMfLDLbuY8XG4q0B4UscHEfI9JydLjyHuEh7MEdXw525WBpUSbklmgjxbsH138XdmiUeEp92gg8Q2ScvIH210qIgcUSr1hEJmYiugkw24TMfrEKBV9VsROf7mRPKGhvR6DHykNqFowtTYEGs1sqdCMCfBj8FO-_pcrsO6aKxcSoPLkb3XRv7XfTV5rz2sLMsIUES0XbHHYexaGk7ccALEEhCuq6THS4wc-2FfBxkCNSrK40bxu-CHRdpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية إسماعيل بقائي:
السيد فريدريش ميرز، ‏النفاق صارخ. فالهجمات العلنية التي تشنها الولايات المتحدة والنظام الإسرائيلي على المنشآت النووية الإيرانية المحصنة لا تُقابل بالإدانة، بل بالأعذار والتبريرات. ومع ذلك، عندما تقع عملية يُزعم أنها عملية مُفبركة - والتي رفضت حتى الإمارات العربية المتحدة نسبها رسمياً إلى إيران - تلجأ هذه الأصوات نفسها فجأة إلى لغة "القانون الدولي" و"الأمن الإقليمي" الرنانة.
‏إذا كانت الهجمات على المنشآت النووية تهدد شعوب المنطقة، فيجب أن ينطبق هذا المبدأ بالتساوي على جميع الدول - وليس فقط عندما يخدم المصلحة السياسية للغرب.
‏هذا الإحساس الانتقائي بالعدالة يذكرنا بالقاضي آدم في قصة هاينريش فون كلايست "الإبريق المكسور": رجل يستدعي سوء سلوكه الذي لا يغتفر عملياً إصدار حكم، ولكنه، في غطرسة وتبرير ذاتي، يتجرأ على أخذ مكانه على منصة القضاء.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75649" target="_blank">📅 00:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75648">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭐️
تفعيل الدفاعات الجوية الإيرانية في مدينة أصفهان.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75648" target="_blank">📅 23:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75647">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3da62d1b00.mp4?token=ACvnBOtVXP6DErBPY_UJa_r5qy9Y0qvEQg-FJWD3MG_G2dl5tOZp44ljyGTXaqAYjoQpI91NfYPPj2L0O2DFUu3Q3hqGCmXp06JHJPVtIgT2DRQjDSiGLa2TQG2zhNOXBtzQrSfnD0L2ZGqwRSUrid6GP8SLxPmhYXsfTlPYFlP1pBKYa7deqxBpWHEGfOXSoWpKDkFGm7W_T2I8DrGzRsunpq1Rbk22DBWzlxSMf6ppWzRR_z0nR860zznehMdYSCIOWbQa-9zNYpmwH7UOmBts1N-Xfttjb3DEPQORoaNaGlhRIMvKgd5hyF5l9kBZnOzWZTAfa1rxJrhi4afUrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3da62d1b00.mp4?token=ACvnBOtVXP6DErBPY_UJa_r5qy9Y0qvEQg-FJWD3MG_G2dl5tOZp44ljyGTXaqAYjoQpI91NfYPPj2L0O2DFUu3Q3hqGCmXp06JHJPVtIgT2DRQjDSiGLa2TQG2zhNOXBtzQrSfnD0L2ZGqwRSUrid6GP8SLxPmhYXsfTlPYFlP1pBKYa7deqxBpWHEGfOXSoWpKDkFGm7W_T2I8DrGzRsunpq1Rbk22DBWzlxSMf6ppWzRR_z0nR860zznehMdYSCIOWbQa-9zNYpmwH7UOmBts1N-Xfttjb3DEPQORoaNaGlhRIMvKgd5hyF5l9kBZnOzWZTAfa1rxJrhi4afUrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
اندلاع اشتباكات بين قوات جيش الإحتلال الصهيوني ومسلحين في منطقة حوض اليرموك بريف محافظة درعا السورية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75647" target="_blank">📅 23:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75646">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62de0d755e.mp4?token=k37fkz20YwvgCQr7jZiwLNjeVpCsNgIvofVnm4eNmWxaJikhK0QXprEqGmCZXKbK5m-KgL3iyJs0XFfRGTzM75RNxf57v4Uy4xA84E48xfsqu72VrL2GB4kCNlJJZLo0wkX8m3T953O6nBHks8TOgNT7lOJR1BqYOQpFSuSJB32W51PzlcJXbuYOe5Jb0YgotfWFXs-VYbRX0A73UjvsAGDJbO2HzMSlHE0y3CbubWh-c3yuoqrrhtgTx7QMl_kNUD_dv7x4nK4tBdg1Q7-MkfrLY0qBJcWfCU91wC3qgQj9JLHOhy2fhpi991_s8dlpX00afy5TQtJLCgI2SdSR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62de0d755e.mp4?token=k37fkz20YwvgCQr7jZiwLNjeVpCsNgIvofVnm4eNmWxaJikhK0QXprEqGmCZXKbK5m-KgL3iyJs0XFfRGTzM75RNxf57v4Uy4xA84E48xfsqu72VrL2GB4kCNlJJZLo0wkX8m3T953O6nBHks8TOgNT7lOJR1BqYOQpFSuSJB32W51PzlcJXbuYOe5Jb0YgotfWFXs-VYbRX0A73UjvsAGDJbO2HzMSlHE0y3CbubWh-c3yuoqrrhtgTx7QMl_kNUD_dv7x4nK4tBdg1Q7-MkfrLY0qBJcWfCU91wC3qgQj9JLHOhy2fhpi991_s8dlpX00afy5TQtJLCgI2SdSR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تفعيل الدفاعات الجوية في جزيرة قشم الإيرانية بعد رصد أجسام معادية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75646" target="_blank">📅 23:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75645">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwaW8M0K_V5sBp0U6jtfV2KvxEw2TdiWupYZlglfgDjWhQ1v79Bt8NJyGdx2cU1cgaVMr06MhrIdlYJEejPaJnbaN7BTViXXSachdTXqiGJnC6CubXUmF9-4criS9j8NcftY_irAKGeIUkTeTh2u-q66disK87Yw39glumAEWHA4Gfh3KzIYCZhk9evFCpExhxRUegsqw_0f8mpVi4ncy_mY_eAWwcdBKmA1_kHDejNlEYSlVsKNCK4DT5v0CVUhEAwa39K0E9j1EsSqT9sXZdeIkfArxgxkpQRz94JJ6rxk8mxi1jLbl7nwgutUgktIgFdgMrZZEgug4PEkFDfdhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
في ولاية ماريلاند، أرسلوا 500,000 بطاقة اقتراع بريدية غير قانونية، وتم القبض عليهم! والآن، سيرسلون 500,000 بطاقة اقتراع بريدية أخرى، لكن لا أحد يعرف ما يحدث مع أول 500,000 بطاقة أرسلوها. بالإضافة إلى ذلك، ذهبت العديد من هذه البطاقات إلى الديمقراطيين، لذلك لا توجد فرصة لأي جمهوري يترشح في ماريلاند! تم ذلك من قبل حاكم الولاية الفاسد، ويس مور. لقد سمح بحدوث ذلك للتأكد من فوز الديمقراطيين. لم يكن من المنطقي بالنسبة لي أبدًا أن تُعتبر ماريلاند ولاية ديمقراطية تلقائيًا، لكنني الآن أفهم السبب. أنا متأكد من أن هذا استمر لسنوات. سأطلب من المدعي العام للولايات المتحدة ووزارة العدل إجراء تحقيق فوري في هذا الوضع.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75645" target="_blank">📅 23:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75644">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b5c3d572.mp4?token=koK-AxWhICqj-OEM9JVul_EBuETTfN3iZGDL2OzWBTsKJWL-AuTA85thDLlMesKG5_pWjOJVxe90aozhtO70hU7q3Acj5M6T0xly_7_LVA4PKFCt2YVG9D7lE9Xz8ROo14PXKwe3Hdz-xUQT_G8UlsuT5qzG7DjVy-wksuYfejiSJ9h1kglDKeJQAxJhvDQE1AQaNXRG_LFnQpWFC1Hn9fRYxocqzfaAH-9mUfhXX-hYCXbg4vYU8uJiVjn-nd5WpoHtv7TBHD0EGOLLcPWMQq_-ptL-KriFcfoxT7KIBlclfhQHhunLX5GU2ElkAPHJ5C_26jhL5U2yIvLmNN1rTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b5c3d572.mp4?token=koK-AxWhICqj-OEM9JVul_EBuETTfN3iZGDL2OzWBTsKJWL-AuTA85thDLlMesKG5_pWjOJVxe90aozhtO70hU7q3Acj5M6T0xly_7_LVA4PKFCt2YVG9D7lE9Xz8ROo14PXKwe3Hdz-xUQT_G8UlsuT5qzG7DjVy-wksuYfejiSJ9h1kglDKeJQAxJhvDQE1AQaNXRG_LFnQpWFC1Hn9fRYxocqzfaAH-9mUfhXX-hYCXbg4vYU8uJiVjn-nd5WpoHtv7TBHD0EGOLLcPWMQq_-ptL-KriFcfoxT7KIBlclfhQHhunLX5GU2ElkAPHJ5C_26jhL5U2yIvLmNN1rTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75644" target="_blank">📅 23:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75643">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭐️
إنفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75643" target="_blank">📅 23:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75642">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd6f7973f.mp4?token=Eh0l-VrrIr-v_pvxGTzlqMXWi_OYKe7tD3OE7YmRgTNbs0FP5XdFRwc6jb8EoRvAjMlYn8T9I3p4PC3YeVVNl6O6ooRvHAV-vgI3OXEKpWlpwnMaINh4pPMnmmN39sSSUqENSxz24wCJgaMcUcTVl7xO0xYa3OwYHB7nx_PHLmodXZu4-8KOjmtyWxI5Fkid5Qe6z00vcfL7SVYXeOQpy6xReLr_aUgQcATwD6wnCt1VMFGUvr9XCMyrqD8ozP3ikoBN1aAViilEhFY_iIhlQGTwneUJwHEy3_D7VOQpP69bAfzBR-uN80B-q0aG3jbNvh1QtyBtAH7yxAWaxn7ODg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd6f7973f.mp4?token=Eh0l-VrrIr-v_pvxGTzlqMXWi_OYKe7tD3OE7YmRgTNbs0FP5XdFRwc6jb8EoRvAjMlYn8T9I3p4PC3YeVVNl6O6ooRvHAV-vgI3OXEKpWlpwnMaINh4pPMnmmN39sSSUqENSxz24wCJgaMcUcTVl7xO0xYa3OwYHB7nx_PHLmodXZu4-8KOjmtyWxI5Fkid5Qe6z00vcfL7SVYXeOQpy6xReLr_aUgQcATwD6wnCt1VMFGUvr9XCMyrqD8ozP3ikoBN1aAViilEhFY_iIhlQGTwneUJwHEy3_D7VOQpP69bAfzBR-uN80B-q0aG3jbNvh1QtyBtAH7yxAWaxn7ODg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مقتل شخصين على الأقل وإصابة آخرين في إطلاق نار على مسجد في مدينة سان دييغو بولاية كاليفرنيا الأمريكية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75642" target="_blank">📅 23:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75641">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGOPbJJ-DNkM77yV2CL2BOu-4ykit79qBYk1YObedMRWXFmo0FCECpk9Ht15JNQxv1Ak9X_BU66GvTWQxYsmua2kRL6VhbvX7yiDf0oxpATTJIAfqhQxSmzTg6szjKLYclDbQqsvje3NNyCdIk-ElxVte4rWheJH0wNSEMz3Kprny8KqgJ5l-47pcpZv-Ient1ssp-tuvHONLHVgle8QJJpwM2F7TIBEEo95szdN0-zxeeKtU01sUQfWR7EqPYrH2YRFXPSvLwB2B81gaUW-aNEkttuXkRkFKb72N44nyI729B0h4n_KOvMcVcfXFmkWRzlwqOB3g_imrLLHWaqvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب يجبن أمام إيران الإسلامية:
لقد طُلب مني من قبل أمير قطر، تميم بن حمد آل ثاني، وولي عهد المملكة العربية السعودية، محمد بن سلمان آل سعود، ورئيس دولة الإمارات العربية المتحدة، محمد بن زايد آل نهيان، أن نؤجل هجومنا العسكري المخطط له ضد جمهورية إيران الإسلامية، والذي كان من المقرر أن يحدث غدًا، حيث أن مفاوضات جادة تجري الآن، وفي رأيهم، كقادة كبار وحلفاء، سيتم التوصل إلى اتفاق سيكون مقبولًا للغاية للولايات المتحدة الأمريكية، وكذلك جميع الدول في الشرق الأوسط، وخارجها. سيشمل هذا الاتفاق، على نحو مهم، عدم وجود أسلحة نووية لإيران! بناءً على احترامي للقادة المذكورين أعلاه، أوعزت إلى وزير الحرب، بيت هيغسيث، ورئيس هيئة الأركان المشتركة، الجنرال دانيال كين، والجيش الأمريكي، أننا لن نشن هجومًا مجدولًا على إيران غدًا، لكنني أوعزهم أيضًا أن يكونوا مستعدين للشروع في هجوم واسع النطاق على إيران، في أي لحظة، في حالة عدم التوصل إلى اتفاق مقبول. شكرًا لكم على اهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75641" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75640">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
تفعيل الدفاعات الجوية في جزيرة قشم الإيرانية بعد رصد أجسام معادية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75640" target="_blank">📅 22:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75639">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OntxJ7k-J-gg6Xui-ZJLbRMog94f4oOsKp0zvsVugAlSkLXqQEF9I3ZOsewKpmCxj89GVeIzQ2Ozd07Wxfg3GVvVMOfpNQHIRD9Q1gjSSFDluPHrWiKXrj-qCPGVeoETRAq2Qpet2DkM-MtRpItugbhYQx9ZWtcGavy2rkyPZRmYGRIjWri-KI1gkKBC2uomLvyC_HCjo0ySmDP2SPjHRfkZYKrfTpy0MpnjNOOjgX1vJWpg7eOLDppwszM5lRakFbhlkbphj5kSCW3jn5TvzsPAIr0lAiQBjTTZRJ6EsfZ1aLi6ZxLVbp-fkePw3-309YpuWpJclfTK2QxtCfLLlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط ترتفع لتتجاوز 112 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75639" target="_blank">📅 22:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75638">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK-C7Vwcvndt5kF1ZHAu4PyOPDje_dhGTQleAX7aTP22xcc-225YdJd2FFHLbyKV6s94zLEunMKtPzezmPMUYHQsYeuCuwTKxrIQmtDFuOlY_Fvl5KEKAZE42UXDcJKR1N20hxtoOtWSmHGiECACDNTvtIKjUFIqGOi3Ek1a1BvaAGXs9b_TKmnVwXfW3b2d2Us2xYI5_H4Zl3QZYl54oLuB8Y-HonySXSP6m1IvG_sf8FGsMOh2H16Y7IUTY7pkcujsLtyw-53EeDYc7BzH9IkzYSmmxw0FXhMLji65GteUPLYXX4IeciF2GN7PMiZo-bS-NZZGltA3t9xIyO-bSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بزشكيان:‏
الحوار لا يعني الاستسلام. تدخل الجمهورية الإسلامية الإيرانية في حوارٍ بكرامةٍ وسلطةٍ وحمايةٍ لحقوق الأمة، ولن تتراجع بأي حالٍ من الأحوال عن الحقوق القانونية للشعب والبلاد. سنخدم الشعب ونحمي مصالح إيران وكرامتها بالمنطق وبكل قوتنا حتى آخر رمق.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75638" target="_blank">📅 21:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75637">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea61dffae.mp4?token=Fm0FUDMNZnDFKixnY7AnedCCA4F8xbDH2lsWD7O8JnKtWuu6aBzL6pfft4u80iBtfBa95XTICsxhnOfEe9UjrI-PRRy4w5Drz3gN7EnT0MxaU4DbElFhHB-U-F9R1dQACEq5lXHu0OT57oBFjw7-PINva7BlNu63DkvfV-qv0hl0BURY4WGKLsaRD9prLiWs5dO0iUtBOpr6V-jliew5g-fd9GrEJflrKqyFzZMWHYL3Uls_m93RlOwEQdmpJ39jnYsntcEuO0YXFx30toJtz6dAIxb7dpjuYjnw7S7cO3F1UqkVmuWbUSWPuTE_-DhLAEpSDj0EpkZsVtV1SAGcQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea61dffae.mp4?token=Fm0FUDMNZnDFKixnY7AnedCCA4F8xbDH2lsWD7O8JnKtWuu6aBzL6pfft4u80iBtfBa95XTICsxhnOfEe9UjrI-PRRy4w5Drz3gN7EnT0MxaU4DbElFhHB-U-F9R1dQACEq5lXHu0OT57oBFjw7-PINva7BlNu63DkvfV-qv0hl0BURY4WGKLsaRD9prLiWs5dO0iUtBOpr6V-jliew5g-fd9GrEJflrKqyFzZMWHYL3Uls_m93RlOwEQdmpJ39jnYsntcEuO0YXFx30toJtz6dAIxb7dpjuYjnw7S7cO3F1UqkVmuWbUSWPuTE_-DhLAEpSDj0EpkZsVtV1SAGcQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بيت هيغسيث يقوم بتقليد ترامب.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75637" target="_blank">📅 21:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75636">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlU6V0kp6jAyLTb3uyzEQ3uKXS7XWz30-0dfBrMqMU7RQfA6SxMjXLvDn3ViSycBpBqVHO4DvuJ_Wet3DVmC3yFqlT9RwT9pSedPyNB-fYVPdhYgh2DJrn5k47qqyX4INSjhDRhmEAqMcNM86Jy2tHrBb7_KTgDzPHrQLFHX_1kGNNsWD5EGWZBTkina_2UfK7S06c2TAEPOS7Y8kYZvOciwb1ioT3hJH3a2OySlKkMzt_luN1cvDJGgOktH302WKicjCVWFnoD5p8utpdc8Qbo8Zh3LG5hvZAIUxMckAt8QXVQwr_JAAF7vpy30oVOOO-THYB_dLizEULRRHGoo7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
يجب طرد عضو الكونغرس من الدرجة الثالثة توماس ماسي، وهو جمهوري ضعيف ومثير للشفقة من ولاية كنتاكي العظيمة، وهي مكان أحبه، وقد فاز ست مرات، بما في ذلك جميع الانتخابات التمهيدية، من منصبه في أسرع وقت ممكن! إنه أسوأ عضو كونغرس "جمهوري" في التاريخ، حيث صوت ضد تخفيضات الضرائب، والجدار، وإنفاذ القانون، ولصالح تشويه المتحولين جنسيًا لأطفالنا، ولعب الرجال في الرياضات النسائية، والعديد من الأشياء الفظيعة الأخرى.
لقد منحنا الشعب الرائع للدائرة الرابعة في ولاية كنتاكي تفويضًا لجعل أمريكا عظيمة مرة أخرى، والشخص الذي سيساعدنا في القيام بذلك هو ضابط البحرية الخاص، وضابط رينجرز الجيش، ومزارع من الجيل الخامس في كنتاكي، الكابتن إد جالرين، وهو وطني حقيقي يضع أمريكا أولاً
بصفته جنديًا مخضرمًا شجاعًا، يعرف إد الحكمة والشجاعة اللازمتين للدفاع عن بلدنا، ودعم جيشنا/قدامى المحاربين، وضمان السلام من خلال القوة. بالإضافة إلى ذلك، وبصفته رجل أعمال ناجحًا للغاية، يعرف إد كيفية خلق وظائف رائعة، وخفض الضرائب واللوائح، والترويج للمنتجات المصنوعة في الولايات المتحدة الأمريكية، ودعم مزارعينا المذهلين والزراعة الأمريكية، وإطلاق العنان للهيمنة الأمريكية في مجال الطاقة، والدفاع عن العصر الذهبي لأمتنا. في الكونغرس، سيناضل بلا كلل للحفاظ على أمن حدودنا، ووقف جرائم المهاجرين، والدفاع عن التعديل الثاني لدستورنا الذي يتعرض دائمًا للهجوم
شعب كنتاكي العظيم يدرك حقيقة ماسي. إنه يصوت فقط ضد الحزب الجمهوري، مما يسهل الأمور على اليسار الراديكالي. على عكس ماسي "الخفيف"، الخاسر غير الفعال الذي خذلنا بشدة، فإن الكابتن إد غالرين فائز ولن يخذلكم. يوم الانتخابات هو الثلاثاء 19 مايو. صوتوا لإد غالرين - إنه يحظى بتأييدي الكامل والتام. لنجعل أمريكا عظيمة مرة أخرى!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75636" target="_blank">📅 21:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75635">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
🏴‍☠️
توثيق آثار بعض استهدافات المقاومة الإسلامية لآليات وتموضعات جيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75635" target="_blank">📅 21:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75634">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
السيد عبدالملك الحوثي:
على المستوى العسكري نحن جاهزون إن شاء الله لكل التطورات.
ثابتون على مواقفنا المبدئية الواضحة التي أكدنا عليها مرارا وبشكل عملي، وجاهزون لأي تطورات قادمة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75634" target="_blank">📅 21:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75633">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7fed53b3.mp4?token=qATmxCUwSTqqHLH6PAnIJCxWBc3pad7xh7Blg7HFYnlczq3UtY97jp4mahv2C5bJsh9bigpDGPxHcOjecK8BIK917UcYyIdIPLuNgxlvWzGuE_hm_kau212kc5aAg08Z5cVJhAvp1-cygv_Z3qi4b9tD2XhX3UIue8aKrrvc_KtvEwQ-gG5k_9m8RH-BhMwkr0W6fB_eI8elFUGZHgd250GTgK7F-wxKQZ1SR4ODwPrLPSjjqTZWuOL6xq3bWa0lzd-t8i9ne12Y-mtHktxdX1rsCU54KFZRf0Y1UTztuRx_ZFINfimhNO5-knemzeTx1Qzg4NzF32NXxsYIR8R0Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7fed53b3.mp4?token=qATmxCUwSTqqHLH6PAnIJCxWBc3pad7xh7Blg7HFYnlczq3UtY97jp4mahv2C5bJsh9bigpDGPxHcOjecK8BIK917UcYyIdIPLuNgxlvWzGuE_hm_kau212kc5aAg08Z5cVJhAvp1-cygv_Z3qi4b9tD2XhX3UIue8aKrrvc_KtvEwQ-gG5k_9m8RH-BhMwkr0W6fB_eI8elFUGZHgd250GTgK7F-wxKQZ1SR4ODwPrLPSjjqTZWuOL6xq3bWa0lzd-t8i9ne12Y-mtHktxdX1rsCU54KFZRf0Y1UTztuRx_ZFINfimhNO5-knemzeTx1Qzg4NzF32NXxsYIR8R0Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
حادث سير في تل أبيب المحتلة ؛ مقتل وإصابة 10 مستوطنين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75633" target="_blank">📅 21:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75632">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف طائرة حربية بصاروخ ارض جو في البقاع الغربي اللبناني.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75632" target="_blank">📅 20:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75631">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
🇮🇷
رويترز: أميركا ترفض المقترح الإيراني الجديد.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75631" target="_blank">📅 20:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75630">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن استهداف آليّة قائد الّلواء 300 التّابع لجيش العدوّ الإسرائيليّ في مستوطنة شوميرا بمحلّقة انقضاضية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75630" target="_blank">📅 19:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75629">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭐️
أكسيوس:  أن البيت الأبيض لا يرى في اقتراح إيران الجديد تحسينًا مجديًا أو كافيًا للتوصل إلى اتفاق.   وقال مسؤول إن الاقتراح يحتوي على تغييرات طفيفة فقط مقارنة بالإصدارات السابقة. وفي حين أنه يوسع النص حول عدم سعي إيران للحصول على سلاح نووي، إلا أنه لا يزال…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75629" target="_blank">📅 18:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75628">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭐️
أكسيوس:
أن البيت الأبيض لا يرى في اقتراح إيران الجديد تحسينًا مجديًا أو كافيًا للتوصل إلى اتفاق.
وقال مسؤول إن الاقتراح يحتوي على تغييرات طفيفة فقط مقارنة بالإصدارات السابقة. وفي حين أنه يوسع النص حول عدم سعي إيران للحصول على سلاح نووي، إلا أنه لا يزال يفتقر إلى التزامات مفصلة بشأن تعليق تخصيب اليورانيوم أو التخلي عن المخزونات الحالية من اليورانيوم عالي التخصيب.
ورفض المسؤول أيضًا التقارير التي تفيد بأن واشنطن وافقت على تخفيف العقوبات، قائلاً: "لن يحدث أي تخفيف للعقوبات مجانًا" دون اتخاذ خطوات متبادلة من جانب طهران.
وقال المسؤول: "نحن حقًا لا نحرز الكثير من التقدم. نحن في موقف خطير للغاية اليوم". وأضاف: "إذا لم يحدث ذلك، فسيكون لدينا محادثة من خلال القنابل، وسيكون ذلك أمرًا مؤسفًا".</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75628" target="_blank">📅 18:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75627">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9P_iMX1MEOthkPLtI9YTRRQ9Hdg3Zf_9MDl4NSA3lre5cg6ab5KCzFte8Ogt3wricefiQ7FnwU5_k0ppoSD_sVgtWnN4CSA3guPJV4jsbJvjXbi_Iyc2MH7RnNTrBWVdfGsyAGoQPo8y4uOSus-lA-AdxVDuyWMrO3Ae0Z5I32TsVaJ7MUbIKGAmVIyZfQTLCMNamO_IrezaxHvFuiaPmVbl3_IebCNrez1OnP1LId4tvN0r3b_XPg_BdTiXV3-iq7cdkiXUx3nPsC_dGtl8fAcAt06zTpzyi8WaLxUpoEMnemN8pFHRNj-kMM-6HC7ue7Hdy58AsM1vbaps4147g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐦
بيان للمسؤول الأمني لكتائب حزب الله أبو مجاهد العساف</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75627" target="_blank">📅 18:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75626">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk3YzpKI1jGcGK8qS-729Of2gHtEFv69E1nt_rJgm8sRZy8oddXReT1NKPyNx7oiLyJzGk40m71tNcOhy9MdWupxWw-TQ8BhPSQe5CCpvrccQ7DWmtTzl1V0yN30fVxjjubhhI8UNTY_E87VL9DpCVXrzOWw1EiOwmoj45jvZHNFBl1-4JVgGalOME7DGH0FVj95hRT757xA5LaPA6ftTqa-kcqdJdsGb79UBCNvqGtLhcvdwKqmzPO7Ul89bXX9wXxwHP1bt6g355CRdxqzxfpLmhFcdPN_W-8W1_v0BydE7c_xU8ctiloVtryYfcytV3U3e7u0mHkGYjN_Sm7NAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
دونالد ترامب:
إذا استسلمت إيران، واعترفت بأن أسطولها البحري قد غرق في قاع البحر، وأن قواتها الجوية لم تعد موجودة، وإذا خرج جيشها بأكمله من طهران، وقد ألقوا أسلحتهم ورفعوا أيديهم عالياً، وهم يهتفون "أستسلم، أستسلم" بينما يلوحون بالراية البيضاء، وإذا وقّع جميع قادتها المتبقين على "وثائق الاستسلام" اللازمة، واعترفوا بهزيمتهم أمام القوة العظمى للولايات المتحدة الأمريكية، فإن صحيفة نيويورك تايمز الفاشلة، وصحيفة تشاينا ستريت جورنال (وول ستريت جورنال!)، وقناة سي إن إن الفاسدة والتي فقدت مصداقيتها، وجميع وسائل الإعلام الأخرى التي تنشر الأخبار الكاذبة، ستنشر عناوين رئيسية مفادها أن إيران حققت نصراً باهراً على الولايات المتحدة الأمريكية، وأن الأمر لم يكن متقارباً على الإطلاق. لقد ضلّ الديمقراطيون ووسائل الإعلام طريقهم تماماً. لقد جنّوا تماماً!!! الرئيس ترامب"</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75626" target="_blank">📅 18:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75625">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6JlXavf0DeoXnnsvMwPOa8b4tYXfpM31jkRPeA5Sb7lYKhnnlaJ0R8_Y6d3F71IUU5tknob-t2T8i-E1GhRtRdA97UStAv1oHIvhPvp58ZBTXS221yoSGoG9mQzgHq97U7Oz8ydHvZWeg9D6m26xIIo90aPRUQhPYy9seeqrE8Ei86IGCkPk5IuXVfOAh-4lXQLktp0wDR1m8AqOahP1HYAcFoDfj8_Hx7Iac9n4Z9GKtbDpkfooxtryWaG6GefL1UeJvTjEMpyx9KgXesY0jxwKWDROb6lzThcUBrd8Ga7YmjB0kWXvszCx5mtvXJboPLZYxFVI7e0mbMobeYqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐦
بيان للمسؤول الأمني لكتائب حزب الله أبو مجاهد العساف</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75625" target="_blank">📅 18:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75624">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سوالف الگهوة
رئيس الوزراء الباكستاني يزور العراق يوم الخميس القادم</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75624" target="_blank">📅 17:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75623">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
‏مصدر إيراني لرويترز: أميركا أبدت مرونة فيما يخص القيود المفروضة على البرنامج النووي، سنناقش القضية النووية في مراحل لاحقة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75623" target="_blank">📅 17:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75622">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
‏
مصدر إيراني لرويترز:
أميركا أبدت مرونة فيما يخص القيود المفروضة على البرنامج النووي، سنناقش القضية النووية في مراحل لاحقة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75622" target="_blank">📅 17:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75621">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
وزارة الخارجية العراقية:
لم يتم تأشير أي معلومة من خلال وسائل الدفاع الجوي والمعدات البصرية العراقية لاستهداف السعودية من الاراضي العراقية وفي هذا الإطار، تدعو الوزارة الجهات المعنية في المملكة العربية السعودية الشقيقة إلى التعاون وتبادل المعلومات ذات الصلة، بما يسهم في التوصل إلى معلومات دقيقة تعزز الأمن والاستقرار لدى البلدين الشقيقين.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75621" target="_blank">📅 16:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75620">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇱🇧
🇮🇶
إعلام لبناني: قدّم العراق للبنان نفطاً بقيمة ملياري دولار لمنع العتمة الشاملة ولم تقدّم الحكومة اللبنانية إدانة للإنزال الإسرائيلي في صحراء النجف</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75620" target="_blank">📅 16:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75619">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3O0DD9fFgng-vMSUTSaOxbchFM9K9zWArW0_t_ySORm23VG20R-J2gO0y6ewpmozRpMS3MEmdLE9NSgnj8EbKB8qORUZN75Fg8XC_-_MRrIEHChTH2dONbt395YPrU2Q6iEBZuEuVGqpFmYebQDCTLcTTDkoNzw1QrSv7UFlfWo1jTJ6W6meySnLMO7Fd5N0P1IUWoybAVMRM1jls1ONWCdwMA1S-90HKp7Lk03vMPN_9pd4h-jK-p5I_ly5rsfGQ-kPuT6vRx1CQId4XVy36N1-ztwxIGyvlBwzEdKJ0xQDV-brWup_KVv94bJndrMucW0b3iEhllivWI1H-HsrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئاسة جامعة الإسراء توضح حقيقة الملابسات عن ما حدث في جامعة الإسراء الأهلية في العاصمة بغداد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75619" target="_blank">📅 16:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75618">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📰
‏
نيويورك تايمز:
أميركا وإسرائيل تستعدان بشكل مكثف لاحتمال استئناف حرب إيران هذا الأسبوع، الاستعدادات هي الأكبر منذ وقف النار</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75618" target="_blank">📅 15:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75617">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صافرات الانذار تدوي في كريات شمونة ومحيطها بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75617" target="_blank">📅 15:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75616">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
وكالة تسنيم عن مصدر مقرب من فريق التفاوض:
الأمريكيين خلافاً لما ورد في نصوصهم السابقة، وافقوا في النص الجديد على رفع العقوبات عن النفط الإيراني خلال فترة المفاوضات. رفع العقوبات يعني رفعها مؤقتاً. تُصرّ إيران على أن رفع جميع العقوبات المفروضة عليها يجب أن يكون جزءاً من التزامات الولايات المتحدة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75616" target="_blank">📅 15:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75615">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بعد منع ناقلة تحمل نفط عراقي من المرور.. المتحدث باسم القيادة المركزية الامريكية: قواتنا منعت ناقلة النفط آجيوس فانوريوس من عبور هرمز لانتهاكها الحصار. ناقلة النفط كانت ترفع علم مالطا ولم تكن محملة بنفط إيراني</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75615" target="_blank">📅 15:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75614">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تصرفات معيبة وممارسات غير أخلاقية من بعض المحسوبين على العتبة العباسية بحق رجل دين كرس جهده للعمل الإنساني وخدمة المظلومين بعد مشاركته في حملات دعم إنسانية للشعب الإيراني المظلوم خلال حرب رمضان، هذه المواقف النبيلة قوبلت بالتضييق والاستهداف داخل العتبة وانعكست بشكل مباشر على وظيفته حتى وصل الأمر إلى ظلمه وإجباره على التقاعد بطريقة تفتقر للإنصاف والوفاء لتاريخه ومواقفه الإنسانية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75614" target="_blank">📅 14:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75613">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الانسحابات متواصلة.. انسحاب النائب عمار يوسف من ائتلاف السوداني.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75613" target="_blank">📅 14:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75612">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارات تهز رامون من دون تفعيل صافرات الانذار بعد هجوم بطائرات مسيرة</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75612" target="_blank">📅 14:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75611">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴‍☠️
مستوطني شمال الكيان يطلقون تظاهرة يوم غد في مجمّع أرينا نهاريا تحت عنوان: «نناضل من أجل الشمال – ننزل إلى الشوارع» على خلفية تهديد الطائرات المسيّرة التي يطلقها حزب الله
ثورة ياعلي ثورة
😄</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75611" target="_blank">📅 14:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75610">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
وكالة تسنيم عن مصدر مقرب من فريق التفاوض:
طهران سلمت عبر الوسيط الباكستاني نصا جديدا من 14 بندا، يركز النص الايراني الجديد على مسألة مفاوضات انهاء الحرب وتدابير بناء الثقة من جانب الجانب الامريكي</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75610" target="_blank">📅 13:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75609">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بلومبرغ عن صور أقمار صناعية: رصد نحو 23 ناقلة نفط قرب جزيرة خارك وهو أكبر تجمع منذ بدء الحصار الأمريكي</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75609" target="_blank">📅 13:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75608">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇱🇧
🇮🇶
إعلام لبناني: قدّم العراق للبنان نفطاً بقيمة ملياري دولار لمنع العتمة الشاملة ولم تقدّم الحكومة اللبنانية إدانة للإنزال الإسرائيلي في صحراء النجف</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75608" target="_blank">📅 13:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75607">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الحرس الثوري الإيراني:
إحباط عملية للمجموعات الإرهابية المتمركزة بشمال العراق حاولت خلالها إدخال شحنة ضخمة من الأسلحة والذخائر الأميركية
المجموعات الإرهابية حاولت تهريب الشحنة إلى داخل إيران عبر حدود محافظة كردستان
تم ضبط ومصادرة كميات كبيرة الذخائر والأسلحة المهربة في الشحنة
أي تحرك يمس بالأمن سيواجه بحسم وشدة والقوات المسلحة مستعدة لرد يبعث على الندم</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75607" target="_blank">📅 12:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75606">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: عمليات اعتراض البحرية لسفن أسطول الصمود تمت قبالة سواحل قبرص على بعد مئات الكيلومترات
احتجاز النشطاء ونقلهم إلى سفينة أطلق عليها اسم "سجن عائم"، ثم إلى ميناء أسدود.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75606" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75604">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600e666909.mp4?token=q_KB1dwmbky9i7ckhk-NVZQRxFDQOi_oM4V8kHO4hghOlG6NMBFHD_dSxkoFriOsRzDt0f5irdQkbX5no1l1suLCIpV3oe8Yg_7RsrYB53JvPc6I2Py70JZlurm4aXDon5KrAFSYVb3Wu31G0MO-D5y35-ydqDtRB-dg9KFREp8Fhwf7BTykm96tpAHXpe02Y4lmCOj1QfyydUXgBvtu7S65wBa34Olqnuqazlm9d8SAmnR3M4Tc_fCnnqYwUkZhvzJMFYUwxWZ7UWwy-D5F6DjclV4PeLNmwlFxfW5XWuLKTvJJE7wgPSCZ7CjdgL801HjXHKq_u6EPAEd4HPFIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600e666909.mp4?token=q_KB1dwmbky9i7ckhk-NVZQRxFDQOi_oM4V8kHO4hghOlG6NMBFHD_dSxkoFriOsRzDt0f5irdQkbX5no1l1suLCIpV3oe8Yg_7RsrYB53JvPc6I2Py70JZlurm4aXDon5KrAFSYVb3Wu31G0MO-D5y35-ydqDtRB-dg9KFREp8Fhwf7BTykm96tpAHXpe02Y4lmCOj1QfyydUXgBvtu7S65wBa34Olqnuqazlm9d8SAmnR3M4Tc_fCnnqYwUkZhvzJMFYUwxWZ7UWwy-D5F6DjclV4PeLNmwlFxfW5XWuLKTvJJE7wgPSCZ7CjdgL801HjXHKq_u6EPAEd4HPFIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الكيان المحتل يتدخل بشكل غير قانوني في المياه الدولية ضد أسطول الصمود الذي يحاول الوصول إلى غزة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75604" target="_blank">📅 11:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75603">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏أوكرانيا تدعي : مسيّرة روسية أصابت سفينة شحن صينية في البحر الأسود</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75603" target="_blank">📅 11:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75602">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية إسماعيل بقائي:
التقت الفرق الفنية لدينا ولدى سلطنة عمان للتنسيق في ملف مضيق هرمز
ليس لدينا عداوة مع أي من دول المنطقة، من بينها الإمارات، ونحن جيران، وطهران تسعى للسلام
الوجود الأميركي يضع المنطقة في خطر دائم
لدينا عتب على الدول التي تضع أراضيها ومقدراتها وسماءها في تصرف المعتدين
حقنا في تخصيب اليورانيوم لن نثيره في المفاوضات
نحن نراعي مبادئ إيران بكل جدية في مسار المفاوضات
مشاريع القرار في مجلس الأمن بشأن إيران ومضيق هرمز فاضحة ولم تشر للمعتدين وهي غير مقبولة
الولايات المتحدة تتصرف مثل قراصنة البحر
نقوم بتوثيق الجرائم التي ارتكبتها دول العدوان من أجل المسار القانوني للمحاسبة
كل انتهاك للقانون الدولي الإنساني مثل حادثة مدرسة ميناب قمنا بتسجيله في المحاكم الدولية بعد توثيقه
الترتيبات الجديدة في مضيق هرمز هدفها ضمان العبور الآمن وحفظ السيادة والحقوق الطبيعية لإيران
لا نخاف من تهديدات العدو ونؤمن بما لدينا ونضع الخطط للمواجهة</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75602" target="_blank">📅 10:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75601">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏴‍☠️
🇺🇸
إعلام العدو: مسؤولون كبار أوضحوا أن الإعلان الأميركي عن تمديد وقف إطلاق النار هو موافقة رسمية على 45 يوماً إضافياً من العمليات</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75601" target="_blank">📅 10:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75600">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📈
الرابطة الأمريكية للسيارات: ارتفاع أسعار البنزين في الولايات المتحدة ليصل معدل سعر الغالون إلى 4.5 دولار</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75600" target="_blank">📅 09:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75599">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ae5d7ef9.mp4?token=Xc6H6-huAaaN2rl98qu6mr4Z8a9JlqrIuCBJ4wh4P7hNdknQJFDgKCtY9BhT07ZcEJBYnTqS0qig1636ijczdx5qZ48PC-iqYBDYzhLwRQV0v05MBf9qrb1Vx9GHtWjklki313kmiIU5gkjFof17pYvQCdpfx-esGSvq21GPDTVf3dv4XA5E8-vm9C-Qdi6qvLUh6BPPD_1YV3ihW_WnJBysgKHmI-w0RAlLKUkMZFhFc2AIkwDAMTcyT426Ws_AnyWED70Du7pp-JOiX6uwbpvBsxcfzS9zKLnZ5LZpmgkQDc_ENnhinXrUBzfHeUbMXP7Q6fbZFPmuMp1ozAg4hkTvFi1LsbBGSZv4bK1xcLV8DSH6nSCs227--wDrBknUWo7DwszNBLiuBDp_kQc2-fAYdvxTr7YiaFWG3pyPxTpmhKSqVKo0kq0Al0YMcFz3BNwQ4ftGR0AtTFC8qj752c2Gbmg_P5SEwjletkAZJo7rbuAPYJyMXQW1K6XkueMeaaQrXGbcN3r3G4idmEdhrav9JVBbLml-5EaPPaslu_qHo-R62pOl5GW6c8PuSaWX8IUSTLUV4Mq1DKqKWXsLDTlo0QPcSaV0luSPYKePKQLIT2N9H11IIRUd9Ek4HgiatTV_RCMrPzl9Jnsxg3r1TPuOxr0j-TAmydeogj-bd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ae5d7ef9.mp4?token=Xc6H6-huAaaN2rl98qu6mr4Z8a9JlqrIuCBJ4wh4P7hNdknQJFDgKCtY9BhT07ZcEJBYnTqS0qig1636ijczdx5qZ48PC-iqYBDYzhLwRQV0v05MBf9qrb1Vx9GHtWjklki313kmiIU5gkjFof17pYvQCdpfx-esGSvq21GPDTVf3dv4XA5E8-vm9C-Qdi6qvLUh6BPPD_1YV3ihW_WnJBysgKHmI-w0RAlLKUkMZFhFc2AIkwDAMTcyT426Ws_AnyWED70Du7pp-JOiX6uwbpvBsxcfzS9zKLnZ5LZpmgkQDc_ENnhinXrUBzfHeUbMXP7Q6fbZFPmuMp1ozAg4hkTvFi1LsbBGSZv4bK1xcLV8DSH6nSCs227--wDrBknUWo7DwszNBLiuBDp_kQc2-fAYdvxTr7YiaFWG3pyPxTpmhKSqVKo0kq0Al0YMcFz3BNwQ4ftGR0AtTFC8qj752c2Gbmg_P5SEwjletkAZJo7rbuAPYJyMXQW1K6XkueMeaaQrXGbcN3r3G4idmEdhrav9JVBbLml-5EaPPaslu_qHo-R62pOl5GW6c8PuSaWX8IUSTLUV4Mq1DKqKWXsLDTlo0QPcSaV0luSPYKePKQLIT2N9H11IIRUd9Ek4HgiatTV_RCMrPzl9Jnsxg3r1TPuOxr0j-TAmydeogj-bd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق مسيرات مجهولة العائدية في سماء محافظة ذي قار جنوب العراق.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75599" target="_blank">📅 09:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75598">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#ترفيهي
دويلة ‏الكويت تدين وتستنكر العدوان الذي تعرضت له السعودية عبر مسيّرات قادمة من الأجواء العراقية
🤦‍♂️</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/75598" target="_blank">📅 08:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75597">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrzKamBl8xVKL10Opvg_Ensm5_rhqQ-gHmFTP7XIDNfdXvVZPcKbEZVUixZ4qALWIhnUvDBnkcq9a1ZZuiJEKpbpdTKiUwfHMoQhyL6c7SiN5vhcxtEUpGXYJb-4pQed1R5P5MvBQVPy7500noP-f7Mlgr5VqXA8qAVM_QRFQzqpA0LWdpRqSG5I7Z5nE8qjWNeCbgnGnpRMzf8KfvMuKs__m8XP0bjiLc3tqJaEFQXQR2PfRnfVvNytNvR87IPckNnIdT5zAe_X_BpgIK3pubPhFGCrUkkuDuGKZxUej9a_5q-ajCKsEmNC9mAQ8CZovtIoLawq4Hvv1Z-8i2ctfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط العالمية تستمر في الصعود لتصل الى 110 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/75597" target="_blank">📅 02:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75596">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4GuP7KH7QdVwb3JlX_SW6ziymhe6sYjAfocvNLZ_B_GbV1J9rfbJFjn9GS5U4xL8WDpll1S0AEpQ5CDaFJnWadCkTcUe9C4bi09NE85X2Ua-sUF3rAkCsMo896LtP9JYdXQTxR6781aqt_Gw01UUlsubQ-jdkignEkjuXol2n-rAqmMvAo2DnAM9DLgVEIZC7ucVp-TT7AR8u2pFRNBqDEYn3h0mEnODIxgYNwo6wdFw2aFSqyiQvg0m1OmxpiMMxLx88W1jFFgV7q7W6FXsVgnan2cTOLIdij93M0PsuZ_33YQ86Z31ptKDS7z8oc-KoPUnECcO2GO05ju47aS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب ينشر محاوطة ايران بالولايات الاميركية!!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/75596" target="_blank">📅 01:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75595">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هيئة الحشد الشعبي تنوه:
تداولت بعض وسائل التواصل الاجتماعي مقطع فيديو للشهيد القائد أبو مهدي المهندس، وهو يتحدث هاتفيًا مع شخص يُدعى قاسم بخصوص عمل خلية الإعلام الحربي، وقد أشارت بعض الصفحات إلى أن المقصود هو الفريق قاسم عطا.
ونود أن نوضح بأن المقصود في الحديث لم يكن الفريق قاسم عطا، وإنما شخص آخر يحمل الاسم ذاته، إذ إن الفريق قاسم عطا كان يشغل سابقًا منصب قائد عمليات جهاز المخابرات، ولم تكن له أي علاقة بخلية الإعلام الحربي في ذلك الوقت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/75595" target="_blank">📅 00:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75594">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات في السعودية</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/75594" target="_blank">📅 00:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75593">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqgzFuR2EJGUtDkhN5K9lSw_Quns2yxnj4PQQB9vO3tgeJJYAqGajhHiPDUWyYwyKQIWrJ2vSd-sMnnUe7cgmNCV_3YHLMHwVfONmZZHX_IcWiFTRIsGe3PMDey1ODGG-LVKdd9YGAeJYeh8w32MXie3BUfB6LDcliotx3G6A0ZDCYulEsqEGNU6C3UR1J1cs7rC2bOymfwOrL8WnXprQFvbEnuZj7-yMacNYZBoQWrdWXUPniDITjY-qeWz9Hj0rapItONaiB2pZCHDFG_whBlQnTFulu1tto-im_kLDEkcXaPF-KK3jcsCqVmEyPP8fhXw2cAQZ4W8sc5_IMgnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👔
ترامب ينشر صورة لنفسه إلى جانب "فضائي" على حسابه الشخصي.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/75593" target="_blank">📅 00:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75592">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
عملية إطلاق نار في مدينة اوستن الأمريكية ؛ إصابة عدة أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75592" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75591">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/75591" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75590">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQJdI2fEbvRZu1MVklEsH1GUotEWjQWGCf82uE0UPnuqgkaR21v0cnJjFJdc93Vz-g_t5ocKcRfyR3EMbB9VoVVRqlCt9cfJgiJgZyysug0cTG6fWr5JPjc2vh0JgK1xQ_uf_mz2CWElKj0mG0cbDFSSL0uWhVg0CI2ivsF_pNp5I15BEfOmY5spHYOjFMrrqQpGnPlUn2XmoCQSHJNxwvT3ad3h9G5BjovmqQNnM-0TtxshTjR8J2qUFQol4V2gtbQMhjIGi8daKl02XeJP4eHM7B8cpwXPWSLPsWdV4GOp6DxkWsD9MAXWoFLSaxOodnu7RDTDqpdDaTqSeCe4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🏴‍☠️
🇺🇸
بمشهد اصبح مألوف
قادمة من تل ابيب ؛ طيران إرضاع جوي في سماء بادية السماوة جنوبي العراق " مقتربات أراضي بني حجيم " النشاط الجوي يأتي بالتزامن مع ادعاءات اصدرتها وزارة الدفاع السعودية قالت ان مسيرات انطلقت من العراق باتجاه السعودية التي تستضيف عدد كبير من القواعد العسكرية الأمريكية …</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/75590" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75589">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c98316ec0.mp4?token=rn4tsSkpk_JBMXtc684imkDP0C1byhJwGFM5dL86XPbWrK2O5l8upADH0HRxvy3Gxn4aQv1g1aBK8H2RoyKk9bAI0aAdXqSNbCaAyo9o24KmlwX0vCmUReguYu3O5LQ3Kc8F6ouwXywbyQmcyNs2i-ln8GBiammWhspiUWf02O8EPIxhhVomnMUp0sSqqKt8-W7kC955OQWTiOpGX2n9jKq4pi2eSh8WjKquyrjyRmBZf0oEpH7UuCIK5zOqaU-uu3ihuPrzIzVLvYdXeB5tJJ88y59pM749-w9sjmDDYzXMUFuyFdANskoPpYP1TcIyO6yNTLIuiTtGu1lNE-s0IS1IwIELuBrQyQom0GQfzjGZ_KYHFJS2Dl9nkDPA7KeniZ8U0Y_VZH_XLozCaMuO75xzAEcvxTnpFcPBgxC20x8It-Yz3jzTpcFM3Rbz3gCGNmkSlFBtSy-CaJ4M9YwBEyP1898NPW2Q2z1kvzj4xP-R8J_Fb02h92Ms_YsYae6uFmgSD4b21vijMlWKaYC2SoXXXgiXbJ6ETPLQDzZ22Uv2dqJoy9hLjfQXLWjrnTM5UzM5zmJo8Iw31XvuarnTPh7VHFu3fKb-URPqXvg0Re3Y4ZSkvq-gYZv9qVxrIz3wFPJP2VA-Zo5mkK0ZNJ-xf6ibBumgQPq7sWGkQou0hqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c98316ec0.mp4?token=rn4tsSkpk_JBMXtc684imkDP0C1byhJwGFM5dL86XPbWrK2O5l8upADH0HRxvy3Gxn4aQv1g1aBK8H2RoyKk9bAI0aAdXqSNbCaAyo9o24KmlwX0vCmUReguYu3O5LQ3Kc8F6ouwXywbyQmcyNs2i-ln8GBiammWhspiUWf02O8EPIxhhVomnMUp0sSqqKt8-W7kC955OQWTiOpGX2n9jKq4pi2eSh8WjKquyrjyRmBZf0oEpH7UuCIK5zOqaU-uu3ihuPrzIzVLvYdXeB5tJJ88y59pM749-w9sjmDDYzXMUFuyFdANskoPpYP1TcIyO6yNTLIuiTtGu1lNE-s0IS1IwIELuBrQyQom0GQfzjGZ_KYHFJS2Dl9nkDPA7KeniZ8U0Y_VZH_XLozCaMuO75xzAEcvxTnpFcPBgxC20x8It-Yz3jzTpcFM3Rbz3gCGNmkSlFBtSy-CaJ4M9YwBEyP1898NPW2Q2z1kvzj4xP-R8J_Fb02h92Ms_YsYae6uFmgSD4b21vijMlWKaYC2SoXXXgiXbJ6ETPLQDzZ22Uv2dqJoy9hLjfQXLWjrnTM5UzM5zmJo8Iw31XvuarnTPh7VHFu3fKb-URPqXvg0Re3Y4ZSkvq-gYZv9qVxrIz3wFPJP2VA-Zo5mkK0ZNJ-xf6ibBumgQPq7sWGkQou0hqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رؤية مختلفة .. أبطال حقيقيون.
علمو اولادكم انهم قدوة لنا ..
انتاج نايا على التلغرام ..</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75589" target="_blank">📅 23:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75588">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtIU9tshLcqHHlXWqHnywLcBcnr4pX7ggGtt2NS1xxTI1yUGCE0g2Ymw9ry6_FJOUBztxy2mUYoRRTylEZJHbC-EJ1Ijb3uLhLFFghqpHvFmL3rihU-nfGG8LfFst3DNJq3RY49Ulh_wEm3fQf26452l5rWNl_dnFWCvyHkz53iXKvA8LXWjj8G3MLGvhpguwmLNix4EFg69wIZphcfAHXHNZeJLTNcq_6sQqvbmqKGgB5Jzid81smawFCziRWNpJ5MqjAes7IfXyXKtcCs4ptvfQQHzpcoCps2sXVKZAS6gEXMG22XxuonexeWZCJzyv_bBqfiLE3ChfOXMUizO1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
يجب طرد عضو الكونغرس من الدرجة الثالثة، توماس ماسي، وهو جمهوري ضعيف ومثير للشفقة من ولاية كنتاكي العظيمة، وهي مكان أحبه، وفزت فيه بشكل كبير ست مرات، بما في ذلك جميع الانتخابات التمهيدية، من منصبه في أسرع وقت ممكن! إنه أسوأ عضو "جمهوري" في الكونغرس في التاريخ، حيث صوت ضد التخفيضات الضريبية، والجدار، وإنفاذ القانون، ولصالح تشويه الأطفال عبر الجنس، والرجال الذين يلعبون في الرياضات النسائية، والعديد من الأشياء الفظيعة الأخرى. أعطانا الناس الرائعون في المنطقة الرابعة للكونغرس في كنتاكي ولاية تفويضًا لـ "جعل أمريكا عظيمة مرة أخرى"، والشخص الذي سيساعدنا في ذلك هو كابتن إد غالرين، عضو البحرية الأمريكية وحارس الجيش، ومزارع كنتاكي من الجيل الخامس، وهو وطني أمريكي حقيقي.
كمحارب شجاع سابق، يعرف إد الحكمة والشجاعة المطلوبتين للدفاع عن بلدنا، ودعم جيشنا/قدامى المحاربين، وضمان السلام من خلال القوة. بالإضافة إلى ذلك، بصفته رجل أعمال ناجحًا للغاية، يعرف إد كيف يخلق وظائف رائعة، ويخفض الضرائب واللوائح، ويعزز "صنع في الولايات المتحدة الأمريكية"، ويدعم مزارعينا الرائعين والزراعة الأمريكية، ويطلق العنان لهيمنة الطاقة الأمريكية، ويدافع عن تعديلنا الثاني المحاصر دائمًا.
شعب كنتاكي العظيم حكيم بشأن ماسي - إنه يصوت فقط ضد الحزب الجمهوري، مما يجعل الحياة سهلة للغاية على اليسار المتطرف. على عكس "المخفف" ماسي، وهو خاسر غير فعال تمامًا خذلنا بشدة، فإن الكابتن إد غالرين هو فائز لن يخيب ظنكم. يوم الانتخابات هو الثلاثاء، 19 مايو. صوّت لإد غالرين - إنه يحظى بدعمي الكامل والتام. اجعلوا أمريكا عظيمة مرة أخرى!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75588" target="_blank">📅 23:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75587">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزارة الدفاع السعودية تزعم اعتراض 3 مسيرات</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75587" target="_blank">📅 23:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75586">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجارات في السعودية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75586" target="_blank">📅 23:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75585">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات في السعودية</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75585" target="_blank">📅 23:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75581">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wg9fp6c4Jej-kCNpQAuXwnOhGK3f72DOMLgW-95Ptxl-ebML_6XaeTmqrznKRcXQVOhGdINcuSMAKOGAwjK49V3dwqK4RGXeDcYCVNphumkwHBzoP7RxbPSJ4iLrlcozS75hw_KaeJpakBKCp9iyJQE2VKeV8TftaOK1By2dSdqDrQqacXhBGptZSl0EUEC3ho_2yYzZJZW88Gs6cWTlZ5ddsydsGzWD-a_9l5wsc3vlhchECfd4AjGBt1v1XAMNpSS4nJS5oGRQbxAcQpm9w3jJrHNKdkf4lzsOY7-GuiPBw71x4LON6_9RVrP72D021QvGnBADuXPbAYUP9YMWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOy6AZpxqzDN9PgO-LIKp71W_dUDNuQa-VEXC_4GCJ9HvsWSTZKDRxLXKUa5KrJYVd87ZjqMntWKmQg81PezdziKk2hNwJ29vQvzI9UVrGEmzeS47UfyEumFUHrwUAyxIKRFKwrsXj3n4E5RkXHrP-mcmnPjEGcKF56b-v1mpWQf2rJqic4ny1-U2LOdAThGz7wrW_wWK6yF4l23QP2BTnh7ucXx8lU_WtUwROWFecXojU3uHzwHq3x8wkK4GysLFVL5ShRxuJLJHOumwXqjDlfNcetg92lC2WUNM77_Wn3JavDhkuo5wjNLcy0rzUFg2QhnRGLYmvFffiS6lVM2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MfAZe-2X6f5CU3bzR-q6NNsvdHbEkWsOEkrxFUCdYiEM_eBZrMoTkAF2tJLSLdbH3sDX63ApLODjD-ldxhFsnKDM4KwSGbDKiIqg-qEt8F9LdIsBmZZIZX_KE4zIWEvpaw0bPZQGLcLrs6i6ni6okcrqZQSeKGD56nM21HpvpD0Zwrv0m_wOvZEnjs9oVnkR4GjvVRSUBCwJKI-0EoVzHQYeQEoIXsJDjUTVuQegdeR5PL4Zt8RYXL060GRbO6cxKuYqu7QHxYgDQAy9JD0kCz2m8jPSeoRMLKgDxnyDVr5u-HkGUxrGmyRRM9hpT_gERSVlggobHJAOhxJquMDVGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197be02628.mp4?token=FCp5XVOxHxbfj9H4hxxHpLu_i9ratxKHHymdUAWi0CzL9fcrC4797Ay7uSoji_ygvXRFhxLNO6LeMGkDOzn2XlF4ZYsAjWZ5xsYyFSwY8KdEyhww8JbMXArEWJU_RNg5MpNOl-gQB6YjMLYxfo71P-n7IQLoTqvnNEN79k215Q3mezok-9ZZBNpnEy1ybNqMiahuaccKtCpyN7IiutO30qGyxM8m-p7-KGdxlmHO78y-9DRvnKMf8Ojtam2Or8qR-pHqOYDc28ROl7Tx3JCXX-xTLCSIbnEvEuw4Yz6fnJhzi2IqIlsnOlM_zHUt8oDc3Q2m3ZT5r1DPU8JNd6xKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197be02628.mp4?token=FCp5XVOxHxbfj9H4hxxHpLu_i9ratxKHHymdUAWi0CzL9fcrC4797Ay7uSoji_ygvXRFhxLNO6LeMGkDOzn2XlF4ZYsAjWZ5xsYyFSwY8KdEyhww8JbMXArEWJU_RNg5MpNOl-gQB6YjMLYxfo71P-n7IQLoTqvnNEN79k215Q3mezok-9ZZBNpnEy1ybNqMiahuaccKtCpyN7IiutO30qGyxM8m-p7-KGdxlmHO78y-9DRvnKMf8Ojtam2Or8qR-pHqOYDc28ROl7Tx3JCXX-xTLCSIbnEvEuw4Yz6fnJhzi2IqIlsnOlM_zHUt8oDc3Q2m3ZT5r1DPU8JNd6xKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇺🇸
القوات المسلحة اليمنية تسقط طائرة أمريكية من طراز MQ9 في محافظة مأرب.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/75581" target="_blank">📅 23:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75580">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
🇺🇸
القوات المسلحة اليمنية تسقط طائرة أمريكية من طراز MQ9 في محافظة مأرب.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75580" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75579">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭐️
مصدر لنايا:
عبور ناقلة نفط عبر مضيق هرمز باتجاه موانئ البصرة، حيث ستصل خلال اليومين المقبلين لتحميل مليوني برميل من النفط الخام العراقي.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75579" target="_blank">📅 22:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75578">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
🇺🇸
موقع تانكر تراكرز:
ثلاث ناقلات نفط إيرانية تكسر خط الحصار الأمريكي بثلاث حيل مختلفة. أوقفت إحداها جهاز تحديد المواقع الآلي، ورفعت أخرى العلم الروسي، واستخدمت الثالثة الساحل العماني.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75578" target="_blank">📅 22:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75577">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba050c1c9.mp4?token=GWbMGMMwh0iRoGA_tYNElIWbsWF1Y64B09RZprwVThqK6JVvkZ3G0KZ7gzev-gMnTkBfKDL8wEFBlCs49vA7mzxs72Km6dOc_vxmFXuyycC-pcumhPNNwia2KAD1vB1-lmnJWJ_u1SJcxAv_FXHLeEHlYx2ng6xVA6Qp6YnUlzJKgqVs3wxAVH7s0R8eqoh8k9m9fXnM3cyFJQ_MRKfgCKWmT-vYKpdTTpWOyDKGsDita_o8D6S5hI7ecfsKFqoOSvqNCSn05Lymc9BcscwEO1UanSBCkEg13--9EFJ2NoA9wMr1o8FsHi3HLjU2-jgStDrgm9vZfkqpsL2Ga3YhIbBAEgCTRv12U0WlWSSdgzSkczd1WQf_91dr7QgM9Sy391c13CwfWOPsQRwVcbiUGKV6E35m8tmEIGwAxMAtcQzIzHXhbE6tQLbYJ-z5-FGj3HkA5hKA27cDxNcchi2JMOSWhsvCUNnbYFcQgjcKTv5WYGYIeOGk3CbQ1trjM-LXHqjPduhySd8QFfgiViDZFFNDah-A7OGDtIiDLu9X4JmDI38UGcXIPmKJcVJWhD9M3qUUT-fOOgVrrUiuwd14M1y1pGzJl5-I1CpS22L-EBC9hRlQJ5EO4jVKjixusfezD3kKQf6ol1na-YFJd3ETygHqKx_S2QDhQnPHP06lyaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba050c1c9.mp4?token=GWbMGMMwh0iRoGA_tYNElIWbsWF1Y64B09RZprwVThqK6JVvkZ3G0KZ7gzev-gMnTkBfKDL8wEFBlCs49vA7mzxs72Km6dOc_vxmFXuyycC-pcumhPNNwia2KAD1vB1-lmnJWJ_u1SJcxAv_FXHLeEHlYx2ng6xVA6Qp6YnUlzJKgqVs3wxAVH7s0R8eqoh8k9m9fXnM3cyFJQ_MRKfgCKWmT-vYKpdTTpWOyDKGsDita_o8D6S5hI7ecfsKFqoOSvqNCSn05Lymc9BcscwEO1UanSBCkEg13--9EFJ2NoA9wMr1o8FsHi3HLjU2-jgStDrgm9vZfkqpsL2Ga3YhIbBAEgCTRv12U0WlWSSdgzSkczd1WQf_91dr7QgM9Sy391c13CwfWOPsQRwVcbiUGKV6E35m8tmEIGwAxMAtcQzIzHXhbE6tQLbYJ-z5-FGj3HkA5hKA27cDxNcchi2JMOSWhsvCUNnbYFcQgjcKTv5WYGYIeOGk3CbQ1trjM-LXHqjPduhySd8QFfgiViDZFFNDah-A7OGDtIiDLu9X4JmDI38UGcXIPmKJcVJWhD9M3qUUT-fOOgVrrUiuwd14M1y1pGzJl5-I1CpS22L-EBC9hRlQJ5EO4jVKjixusfezD3kKQf6ol1na-YFJd3ETygHqKx_S2QDhQnPHP06lyaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اصطدم وتحطم طائرتان من طراز EA-18G التابعتان للبحرية الأمريكية خلال عرض جوي في أيداهو.
مشاهد إضافية
إضغط هنا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75577" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75576">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭐️
مكتبُ سماحة السيد السيستاني (دام ظلّه) في النجف الأشرف: يوم غدٍ الإثنين (18-5-2026) هو الأول من شهر ذي الحجة لعام 1447 للهجرة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75576" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75575">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 15-05-2026 ناقلة جند تابعة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75575" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75574">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تشير حسابات إماراتية على مواقع التواصل الاجتماعي إلى احتمال اتخاذ الإمارات خطوات نحو الاعتراف الرسمي بصوماليلاند، في خطوةٍ تُعدّ بالغة الأهمية. وتحتفل صوماليلاند غداً بيومها الوطني، وسيقدم أول سفير لها لدى الكيان الصهيوني أوراق اعتماده إلى الرئيس هرتسوغ في القدس المحتلة ؛ وتؤكد مصادر في هرجيسا متانة العلاقات مع الإمارات، إلا أن توقيت هذا الاعتراف يعود إلى أبوظبي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75574" target="_blank">📅 21:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75573">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a281c93fa5.mp4?token=eVHzsBKkxdqf4jIGb5EYLdaZk9Gq-dXIwsnGOuMigZlGAB81hOCTUtfpnn5xDy2gjGLFhvQJZ0837SZqlETiENnSTK9mZ5tFalRiQKH9_GZlFNv0re2Qa38wJNwvbOwTbvi4NWJVjoF21eQYClUnrxxmlFIW3V10P47aiH0rJRLGzREtKstmsWU8C4eN-Om2i-Xcv-vK0RsAEX_JrDj0be2Jhv4XCpu5jeIxiHfKaSpXog5JToODmRkACDx0SICPeZvIxUd7vYlRp_NQ1VpjTplgG9LqPpSarcb2ykmX1zFK-BVnYsP3Gm_rCv2Xpg3X28_HRhKqIz3se7sXNyaPUILIUKxk_cwBZL1rroYKALG3LWuUreD-Ou8xw72i1e_zIvXBCRqgBwFyeDCOW8-Lx8zJXvaebyiebYiEJ2Rwk1XISVcxwVoEo00lWEag4HENr4A08OB755QtrrzjrjNZeneezPvSY49BqpR_sVp6ro2uznc1_6AM3SF5y-mdCBaHD4zU5asxjl0NXhiTRFOq3KMavH4_pSw8mYNaSbW2f7hKSbsK4xG93cn3Id4iTadf-VHNxFI6vm9ObjMbvLbIBOora_xltZesedleH8gsMpjT-tuvuLPMmbfU9dySrmqrcWTBsiItbt35J090il_80VktlK3--6AxV3tspS0v1-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a281c93fa5.mp4?token=eVHzsBKkxdqf4jIGb5EYLdaZk9Gq-dXIwsnGOuMigZlGAB81hOCTUtfpnn5xDy2gjGLFhvQJZ0837SZqlETiENnSTK9mZ5tFalRiQKH9_GZlFNv0re2Qa38wJNwvbOwTbvi4NWJVjoF21eQYClUnrxxmlFIW3V10P47aiH0rJRLGzREtKstmsWU8C4eN-Om2i-Xcv-vK0RsAEX_JrDj0be2Jhv4XCpu5jeIxiHfKaSpXog5JToODmRkACDx0SICPeZvIxUd7vYlRp_NQ1VpjTplgG9LqPpSarcb2ykmX1zFK-BVnYsP3Gm_rCv2Xpg3X28_HRhKqIz3se7sXNyaPUILIUKxk_cwBZL1rroYKALG3LWuUreD-Ou8xw72i1e_zIvXBCRqgBwFyeDCOW8-Lx8zJXvaebyiebYiEJ2Rwk1XISVcxwVoEo00lWEag4HENr4A08OB755QtrrzjrjNZeneezPvSY49BqpR_sVp6ro2uznc1_6AM3SF5y-mdCBaHD4zU5asxjl0NXhiTRFOq3KMavH4_pSw8mYNaSbW2f7hKSbsK4xG93cn3Id4iTadf-VHNxFI6vm9ObjMbvLbIBOora_xltZesedleH8gsMpjT-tuvuLPMmbfU9dySrmqrcWTBsiItbt35J090il_80VktlK3--6AxV3tspS0v1-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماذا حدث في منطقة شنان قرب الاديان لمن هي الـ عجلات العسكرية المدرعة ماذا يفعل الأمريكان بالأحداثية  ‏37R  KV 750018  3478349 ما قصة هبوط هليكوبتر عدد ٦ ونصب خيم أمريكية في صحراء الانبار جنوب ناحية النخيب منطقة شنانه الاحداثيات ‏38R  KV  69654  98230  لماذا…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75573" target="_blank">📅 21:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75572">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
🏴‍☠️
هيئة البث الإسرائيلية عن مسؤول: الولايات المتحدة وإسرائيل ترفعان حالة التأهب لإمكانية استئناف القتال بإيران.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75572" target="_blank">📅 20:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75571">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
‏ترامب: إذا لم ترسل إيران مقترحا جيدا سنضربها كما لم نفعل من قبل.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75571" target="_blank">📅 20:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75570">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
‏ترامب: على إيران أن تخاف وأن تحذر مني.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75570" target="_blank">📅 20:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75569">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
‏ترامب: بالنسبة لإيران، الوقت ينفد، وعليهم التحرك بسرعة، وإلا فلن يبقى منهم شيء. الوقت جوهري!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75569" target="_blank">📅 20:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75568">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzCz8ZSz0Yi633mdKFSSQ7TL2DdpByxD5WQZz4J3vucWWisYSTPSL9e_55qrlJRmqYWMgC1mHbOCux2670krfB3X9yGqVx3po6AnsVVFGT0XqcR4LwX4SP_j2jAwqvc4pEV-ApltUYm_-HWuA7opCBF2UcWuaZSqP7XPoN1--HJbvJAZdXlsjWSn0lRsjlZbNBlnLKkBlDhLyBsB0kwyKJhp2RKmkO4p5VtJygRKMU6hDv7HOvwqHgbqiHOrKcvBY9T89zCM0m1TPGJQ44CvYQ3zF4J0IWE_zTgCtxlcXgGSwhzBo_Ooj5E_iSjSe-JVwLzVmku-2OE43PAMM3T4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
بالنسبة لإيران، الوقت ينفد، وعليهم التحرك بسرعة، وإلا فلن يبقى منهم شيء. الوقت جوهري!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/75568" target="_blank">📅 20:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75567">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭐️
مكتبُ سماحة السيد السيستاني (دام ظلّه) في النجف الأشرف:
يوم غدٍ الإثنين (18-5-2026) هو الأول من شهر ذي الحجة لعام 1447 للهجرة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75567" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75566">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭐️
روسيا:
القوات الأوكرانية قصفت ورشة النقل التابعة لمحطة توليد الطاقة النووية في زابوروجي وشنت هجومًا بطائرة مسيرة على محطة "رادوجا".</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/75566" target="_blank">📅 19:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75565">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-05-2026 تجمّع لجنود جيش العدو الإسرائيلي في موقع رأس الناقورة العسكري جنوب لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/75565" target="_blank">📅 17:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75564">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزارة دفاع دويلة الامارات: تعرضنا لهجمات بـ3 طائرات مسيّرة دخلت من جهة الحدود الغربية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/75564" target="_blank">📅 17:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75563">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75563" target="_blank">📅 17:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75562">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/75562" target="_blank">📅 17:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75561">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رئيس مجلس النواب الأمريكي: عملية الغضب الملحمي انتهت</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75561" target="_blank">📅 16:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75560">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3348e2fc.mp4?token=ONLqML9iGhVbYf-Y6fYbTKqRElsDWmzCPqHFsJWkXA63wbXKLlVOIW6EFJIqUwEG1SJqdyMZQw9oGZ-BmcT4KHR8LaJGsqNsDMRRIECQ56hyNHnPzSz8GTGAOUCVbSvLrlG08InLRUaQKoEHPbYgStc5oqitVcXGFjnmZvtsKdGPiSzgYoSUkNfMAsRqEofMXMVSqUh5ElcIJ34mUmA8UCHd4Yiybiu0GykTo8OoEsk4GTCTuo4cP6gA52FWYNcLlJRmu0rLZUmTSDDLUjBk725XhnSifkle8Zbdc6tJlJ9pc_cnZf4vgNsjEkjB6n3mTG7mtFRhEJG9SB5EIXhOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3348e2fc.mp4?token=ONLqML9iGhVbYf-Y6fYbTKqRElsDWmzCPqHFsJWkXA63wbXKLlVOIW6EFJIqUwEG1SJqdyMZQw9oGZ-BmcT4KHR8LaJGsqNsDMRRIECQ56hyNHnPzSz8GTGAOUCVbSvLrlG08InLRUaQKoEHPbYgStc5oqitVcXGFjnmZvtsKdGPiSzgYoSUkNfMAsRqEofMXMVSqUh5ElcIJ34mUmA8UCHd4Yiybiu0GykTo8OoEsk4GTCTuo4cP6gA52FWYNcLlJRmu0rLZUmTSDDLUjBk725XhnSifkle8Zbdc6tJlJ9pc_cnZf4vgNsjEkjB6n3mTG7mtFRhEJG9SB5EIXhOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الطيران الصهيوني يرتكب مجزرة في بلدة طيرفلسيه جنوبي لبنان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/75560" target="_blank">📅 16:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75559">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📰
‏
أكسيوس عن مسؤول امريكي:
كوبا بدأت مناقشة خطط لمهاجمة سفن حربية أميركية وقاعدة غوانتانامو وتسعى للحصول على المسيرات والمعدات العسكرية من روسيا وهي تحاول معرفة شكل المواجهة بين قواتنا وإيران</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75559" target="_blank">📅 16:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75558">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الصدر يبارك للزيدي
المكتب الخاص / النجف الأشرف: أجرى سماحة القائد السيد مقتدى الصدر (أعزه الله) اليوم الأحد السابع عشر من شهر آيار ٢٠٢٦ اتصالاً هاتفياً برئيس مجلس الوزراء السيد علي فالح الزيدي وبارك له تشكيل الحكومة وحثه على الحفاظ على سيادة البلد وتحسين الواقع الخدمي بعد أن رأى منه الهمّة والعزم والإصرار لتحسين الواقع العراقي، كما حثه على الوقوف بحزم لمحاربة الفساد، والحفاظ على مقدرات البلد وتأمين العيش الكريم للشعب العراقي كتقديم الخدمات وتلبية احتياجاته وحفظ حقوقه.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/75558" target="_blank">📅 14:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75557">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نيويورك تايمز: دور الولايات المتحدة في الأمن العراقي كان جزءاً من حسابات إسرائيل في قرارها بأنها تستطيع العمل سراً بأمان في العراق.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75557" target="_blank">📅 14:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75556">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نيويورك تايمز: تشير المعلومات إلى أن قاعدة واحدة على الأقل من القواعد التي عثر عليها عواد الشمري كانت معروفة لواشنطن وهذا يعني على الأرجح أن حليف بغداد، الولايات المتحدة، كان على علم بأن هناك قواعد اسرائيلية على الاراضي العراقية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75556" target="_blank">📅 14:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75555">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نيويورك تايمز عن الجيش العراقي: في جلسات خاصة اتصل رئيس أركان القوات المسلحة العراقية الفريق أول عبد الأمير يارالله بنظرائه في الجيش الأمريكي وأكدوا أن القوة ليست قوة أمريكية. لذلك فهمنا أنها إسرائيلية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75555" target="_blank">📅 14:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75554">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نيويورك تايمز عن المتحدث باسم قيادة عمليات كربلاء: الشهيد عواد الشمري اتصل بالسلطات المحلية بعد رصد قوات اجنبية وبعد ذلك بوقت قصير، فقدنا الاتصال به. بعد يومين من البحث عنه تم العثور عليه مقتولا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75554" target="_blank">📅 14:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75553">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏نيويورك تايمز عن مسؤولين عراقيين: في كل من الحرب القصيرة العام الماضي والصراع الحالي، أجبرت واشنطن العراق على إغلاق راداراته لحماية الطائرات الأمريكية، مما جعل بغداد أكثر اعتمادًا على القوات الأمريكية لاكتشاف النشاط العدائي.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75553" target="_blank">📅 14:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75552">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
نيويورك تايمز عن مسؤولين عراقيين:
في كل من الحرب القصيرة العام الماضي والصراع الحالي، أجبرت واشنطن العراق على إغلاق راداراته لحماية الطائرات الأمريكية، مما جعل بغداد أكثر اعتمادًا على القوات الأمريكية لاكتشاف النشاط العدائي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75552" target="_blank">📅 14:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75551">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-05-2026 منظومة اتصالات لاسلكيّة تابعة لجيش العدو الإسرائيلي في موقع بلاط المُستَحدَث مقابل بلدة رامية جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75551" target="_blank">📅 14:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75550">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الاعلام الكردي:
الاتحاد الوطني الكردستاني يوجه رسمياً طلب الى حكومة إقليم كردستان لتطبيق نموذج الإدارتين داخل الاقليم</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75550" target="_blank">📅 14:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75549">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75549" target="_blank">📅 13:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75548">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">استهداف محطة براكة للطاقة النووية</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75548" target="_blank">📅 13:40 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
