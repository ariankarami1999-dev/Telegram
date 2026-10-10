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
<img src="https://cdn4.telesco.pe/file/GxKcpdktsIiDvt-fsU81J4jZq-TNfLdMFPeUMGbwaArZ_tPGUruJFFoij4nuMIeQOJ26nULM2vda0lN7VpZ9Mebm77hGmVdwI1JWJ6Ltll-Ubm2qNT8O-fP07p2rYEG7UfkTogE4HFivSk_97IGEmad1gZuOC71TtUThnSKtRiPwrTCuSr_VFIwjTIXd92xQsrHAPZk3ICHjuzN8jXGG23-pEs2AyiKdGrzqqSlqgaJCDH7sVZ-iabJKnvyuXW48qMsgaaWKOzcjbH4pfl8GUMLdwPYunL22u9EqO2akNFWME5fRv1wo1UGltxmKnkiDMkZnSOgMxLktJP_Cp04xTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-93132">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🐖
ترامب:
رغم كل ما قدمته، لم أحصل أنا أو الولايات المتحدة على جائزة نوبل للسلام.
غدروك يا شبل الاسد
😄</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/naya_foriraq/93132" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93131">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عدوان سعودي على مطار صنعاء الدولي</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/naya_foriraq/93131" target="_blank">📅 15:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93130">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انقطاع الكهرباء في كييف بعد ضربات روسية</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/naya_foriraq/93130" target="_blank">📅 14:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تسجيل اضطرابات في حركة الطيران في أربع مطارات سعودية: جدة، والرياض، والأحساء، والدمام.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/93129" target="_blank">📅 14:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHGesNeq0gN280tcFmSPW5GLx8N8uV_7hcRvdzGesh4zpKB5D9fvmPHMxvRqq5EAnBj1cLDdnWJZ53jVvJGB46lll1dswNhb6Lev2w7qu13_9z13Z-ysYdUYFwtyaRTXoZwQMRDBQ5YeDDPjRWDQbGZDD-1qDB-Pw0OYqpvV9dnoEpMDZZSKc9qQuEDimF6Tu5XbatEsog5W09CizuiSyl9SEibJi8yYlfPAzJws9yUD0RjiQaNgWuSqIQyAiFlqNXBUUZ_WQWsTDJ1ozdz7s77ONEa8swyMj-7e16_T3zGFxutN7slZHG3GsRTrP-goDMrNwpPgZ3C6kPpfkuYI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسبب فقدان الامن في الرياض..
النائب العراقي السابق ظافر العاني: ولدي وزوجته والأحفاد كانوا هناك أثناء القصف وقد صعدوا الطائرة مستعدين للسفر إلى القاهرة فتأجلت الرحلة لوقت غير معلوم، وبقوا في أماكنهم. إحدى الضربتين كانت بالقرب من مدرج الطيران
نايا تنصحكم بالسفر عبر البر ، المطار مغلق بامر من صنعاء لحين فك الحصار عن الشعب اليمني</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/93128" target="_blank">📅 14:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93127">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef27bfce7e.mp4?token=fR9Ebkb1OFEfH_14-5RqC9FPJM3TBtw-kKEZ4O_cnarNPrRCjRUXICVQAt9ISkrG6UpoFoJKFpDCBuOszdXcxZL5aDXP0WGADIraNcy7KofmA_lzdk0yjYSQ4Mmtoxg_bBXXTZh7r3id_KgJFAsS56Xq-xrD4FX8R76wqERTaJKbA0FJ-cxzmML7G9VrOVO7DFr6vtcSso0gGdgcF23QXESPX40dPulUmPyTluePbfVZLiQiVT-wq5C_u9j8EnjUQZhj769NjEdx6Lb2zvsla7gAWBNXdwYr3DVxNDTbzeAUGrnmHKwHLq0XrCH_Ku8m0I8DFqqFQg_1ww9YNXyn5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef27bfce7e.mp4?token=fR9Ebkb1OFEfH_14-5RqC9FPJM3TBtw-kKEZ4O_cnarNPrRCjRUXICVQAt9ISkrG6UpoFoJKFpDCBuOszdXcxZL5aDXP0WGADIraNcy7KofmA_lzdk0yjYSQ4Mmtoxg_bBXXTZh7r3id_KgJFAsS56Xq-xrD4FX8R76wqERTaJKbA0FJ-cxzmML7G9VrOVO7DFr6vtcSso0gGdgcF23QXESPX40dPulUmPyTluePbfVZLiQiVT-wq5C_u9j8EnjUQZhj769NjEdx6Lb2zvsla7gAWBNXdwYr3DVxNDTbzeAUGrnmHKwHLq0XrCH_Ku8m0I8DFqqFQg_1ww9YNXyn5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مروحي عراقي كثيف في سماء محافظة كربلاء المقدسة بعد وصول رئيس الوزراء العراقي للمحافظة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/93127" target="_blank">📅 13:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
‏
مسؤول أميركي:
الخروج من العراق يحمي قواتنا من الميليشيات إذا تصاعد التوتر مع إيران.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93126" target="_blank">📅 13:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdJef_ZyvFEd6U3fnyEmxBOOUpRHIksAG2cjmchiIhzUiftQn-XIz5wICfHJjkfJP3MdV3kUrOGTkzTb_kbKS11Aaw1eAZVftHk3GbNNaVYrD7M80sl_xJFHa5HedciTvePwq64QnKhajz8_pZvuEHgZczmJJaI1qwVAjo5uulSwbkMBGMXFV8b34PyKcf2IsV7ZnsvLN9-wwgS-MPhCvVLvOuHSE6t0hQNDPlg3EebxM1ciZXIt5G9OlyPUQcygRBhUfaMng3e-kBEFRT9Vj0oEHKpLR_GPyr15_ixcP4ElKjy41T7yPf8oTLeyiyf9CeBPOJmoDlzt71H2Lnedyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد الإرتفاع الحاد..
سعر الدولار يتراجع أمام الدينار العراقي في أسواق مدن إقليم كردستان العراق.
100 دولار = 163,000 دينار عراقي</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93125" target="_blank">📅 13:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93124">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇷🇺
🇮🇷
🇺🇸
الكرملين:
بوتين نقل إلى ترامب بالتنسيق مع إيران وجهة نظر طهران بشأن إمكانية التوصل إلى تسوية للصراع.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93124" target="_blank">📅 12:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93123">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇾🇪
🇸🇦
عدوان سعودي على محافظة صعدة اليمنية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93123" target="_blank">📅 12:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93122" target="_blank">📅 10:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93121">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnh2COScOPEsUVRxWS_YVIRPi0FOzPmEb892MaZKYQvVYY62vJb-G7FXHAPKrCdHmuEc22atnyszM4JRmyJDq7M_Bjch6RxsVlJUtJ4-wgRlqR16oy84EO_XteUg677Pjlp0eqptUc4ijge83RQ1bZWCJPhTbfkCcqs6ZGr_-uOoXwZDprzWrf60067646xrO9c8e3jHY2Pt6PUqWpluyKKbLdLK7daWY5Achg53nGRnjBQUoDeW29TILf4f-vXhhxEcVkOi0rVjuQ7JuhS9v8c58ufZOM1wclMakC89GOisaUaZiM0YvQhD-84RXK1tsPUyEcTHYk6IJoPq2KNMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
إنفجارات عنيفة تهز الرياض.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93121" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93120">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇸🇦
إنفجارات عنيفة تهز الرياض.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93120" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93119">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75fedd1dc2.mp4?token=AAgMh7YymN_i0-IbHjb_xGBqT8FK2W_LILwppW9yHp5Ysvlo6W5ahNiRtKlbt6DH2FYbPS9uIb2YVm5SMVph4kriyIydyfU9FH_4jS3GgCn7-TJ8NfcdJtUzLwYBWBokm1YDltjxF913Rul8HOa7blYVh_jGHXauvUtj3EwZHMePXQHUORKLMzmM4Bq0kDWJi8uOT2TCeJ75mfjqxfc_wcH8LEvZ2DRQ8PBLgeQBRLo_5WbqV1KmjZ7y_Puhcssjx3JKf-7ekpnUpSg9lFk82LkeyYdMR4MfcPl8ULzDoEaNIIAFROjgLM_78qR9l3jv0Hrum9whjFUw2q65oGLrTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75fedd1dc2.mp4?token=AAgMh7YymN_i0-IbHjb_xGBqT8FK2W_LILwppW9yHp5Ysvlo6W5ahNiRtKlbt6DH2FYbPS9uIb2YVm5SMVph4kriyIydyfU9FH_4jS3GgCn7-TJ8NfcdJtUzLwYBWBokm1YDltjxF913Rul8HOa7blYVh_jGHXauvUtj3EwZHMePXQHUORKLMzmM4Bq0kDWJi8uOT2TCeJ75mfjqxfc_wcH8LEvZ2DRQ8PBLgeQBRLo_5WbqV1KmjZ7y_Puhcssjx3JKf-7ekpnUpSg9lFk82LkeyYdMR4MfcPl8ULzDoEaNIIAFROjgLM_78qR9l3jv0Hrum9whjFUw2q65oGLrTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض ارهابي في قاطع الدناديش  في الحويجة بمحافظة كركوك ،اشتباك قوات الحشد الشعبي والشرطه الاتحاديه مع عناصر داعش الإرهابي وانباء عن سقوط قتلى في صفوف عناصر داعش</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/93119" target="_blank">📅 03:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93118">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1a1c88504.mp4?token=B0juG2kGzllwI7BkMNca3j7Qgz5HDkBm_sKGtoxnPy5MfTnX17zR9Cr1m2ygm5Fvk48IY7_x2MvxhvmLDFdiRJQUlLtUGcYue_Bc91fhy5-ocjeKlIuwXQ7pAuJX9dVicCC9pWA0iOrSv06A0-yJH_tvzr_6kDcL8uvszjO-PRbGfdW1pVFEz1aQJm_M7JS63On_VqHoVcGYGna7YaIokzjM6HbdM_zkp6SYr6uxT3uOMxrOb6BCVoQNDVvXvdquk2pGcObhsxhpUrgJu9X8HHMFK4a1omadsuZZtgmKpM1yQl9ZOVSbG-f7GFv24o-UbxgJrXm5dNm3wu9cPlwcQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1a1c88504.mp4?token=B0juG2kGzllwI7BkMNca3j7Qgz5HDkBm_sKGtoxnPy5MfTnX17zR9Cr1m2ygm5Fvk48IY7_x2MvxhvmLDFdiRJQUlLtUGcYue_Bc91fhy5-ocjeKlIuwXQ7pAuJX9dVicCC9pWA0iOrSv06A0-yJH_tvzr_6kDcL8uvszjO-PRbGfdW1pVFEz1aQJm_M7JS63On_VqHoVcGYGna7YaIokzjM6HbdM_zkp6SYr6uxT3uOMxrOb6BCVoQNDVvXvdquk2pGcObhsxhpUrgJu9X8HHMFK4a1omadsuZZtgmKpM1yQl9ZOVSbG-f7GFv24o-UbxgJrXm5dNm3wu9cPlwcQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض ارهابي في قاطع الدناديش  في الحويجة بمحافظة كركوك ،اشتباك قوات الحشد الشعبي والشرطه الاتحاديه مع عناصر داعش الإرهابي وانباء عن سقوط قتلى في صفوف عناصر داعش</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/93118" target="_blank">📅 02:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93117">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3287583d27.mp4?token=WjDRwaJ49zlP1jmaip0wkp4IbWYR3kHBHazfaECPnP96vK3At1pGpasX8ZhqOPNRRnWjETv-1Jr8dtj92LIAEfWLv20YX94sw3I6uJ7ex42x-Je6eXoTSDpRmX4Cr0nkDmHWu1aNEJSUItenAHwRk3uI7rNSuA5ewahAFvpCRWnASulCoeKpePKqzoaHnGME5c_Y9bJmBxWgdWfn4-dPwKDfXmADKzS60FB0E0b_Nm7KbWijm2j0TCn7tU951xxGMuTmTQ2oi7HkInpzn141mQaID8xASOiryWlsr1BEcHnECPkiKaeEO2YWDoiExdcBZwrH_VaETX54OzHNOzRJxHL_Ovuhv_oE2jERCO_9iaZybAw8tpva9mGyMhtuTfLt_cKCrUjBK5tLldvCJusrg1fFLEUE_RwuJ-yvwVva7IP5XiunDGDQPXy5VNH6J4ynI4Jdg2WoUiJu7l9z4UL4BDWGeY-zfuacqG3FBQmepnrwMKuxTseXWxN5CcJV4bvVgJ7ccTYEiB2JD2RqNgk0txc5V5wtV7rdqFoQxCs2y44EB5x7ZQ_warF6py6XZ7TrmBw5XBzEyiMtbkdJ8prjlgrIIN6XcBPJ9OvNHsB-RcZu1a9tTx9klRKVqn_O-fCUzcrLked9cV4XI5U_070NwqsnTLNQAS20PtkG3dd2wX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3287583d27.mp4?token=WjDRwaJ49zlP1jmaip0wkp4IbWYR3kHBHazfaECPnP96vK3At1pGpasX8ZhqOPNRRnWjETv-1Jr8dtj92LIAEfWLv20YX94sw3I6uJ7ex42x-Je6eXoTSDpRmX4Cr0nkDmHWu1aNEJSUItenAHwRk3uI7rNSuA5ewahAFvpCRWnASulCoeKpePKqzoaHnGME5c_Y9bJmBxWgdWfn4-dPwKDfXmADKzS60FB0E0b_Nm7KbWijm2j0TCn7tU951xxGMuTmTQ2oi7HkInpzn141mQaID8xASOiryWlsr1BEcHnECPkiKaeEO2YWDoiExdcBZwrH_VaETX54OzHNOzRJxHL_Ovuhv_oE2jERCO_9iaZybAw8tpva9mGyMhtuTfLt_cKCrUjBK5tLldvCJusrg1fFLEUE_RwuJ-yvwVva7IP5XiunDGDQPXy5VNH6J4ynI4Jdg2WoUiJu7l9z4UL4BDWGeY-zfuacqG3FBQmepnrwMKuxTseXWxN5CcJV4bvVgJ7ccTYEiB2JD2RqNgk0txc5V5wtV7rdqFoQxCs2y44EB5x7ZQ_warF6py6XZ7TrmBw5XBzEyiMtbkdJ8prjlgrIIN6XcBPJ9OvNHsB-RcZu1a9tTx9klRKVqn_O-fCUzcrLked9cV4XI5U_070NwqsnTLNQAS20PtkG3dd2wX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحفي: ما هو موقفكم من الهجوم على المطار في المملكة العربية السعودية؟
‏ترامب: ليس جيداً. إنه ليس أمراً جيداً. أنا لست سعيداً بذلك.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/93117" target="_blank">📅 00:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93116">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44502f8fae.mp4?token=ST7KxdmcHuyKs9yvOQ7fyAAH3dDPqWVX3lz7-_7KO_y9znU3sAsP7CcO-P5jKoFuyUXtyb-IYOfVuPlFNWSldodz0QhT5nvezQCzA_2oXmwORCoK-_kffN6ZClDb52t6f_SykrApuJkh3Y-CrA9ExONCgYZWp39EBK_83cZRC0QPsHboxOKnViUtC3TlrWOSCQEPZKbnKTXYdZc0apCEPZg9yLq0OVfiG30gO1ZVfJw1mOH0g_6uhf7J0enqk5lrULrUolU0l8AuG9Dd2peCESIP7gpieO1FIiEkHQCq-KCJpDOP_B7AqI_E8dLdQf4IUsugi7NNhC07F_d75uwqig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44502f8fae.mp4?token=ST7KxdmcHuyKs9yvOQ7fyAAH3dDPqWVX3lz7-_7KO_y9znU3sAsP7CcO-P5jKoFuyUXtyb-IYOfVuPlFNWSldodz0QhT5nvezQCzA_2oXmwORCoK-_kffN6ZClDb52t6f_SykrApuJkh3Y-CrA9ExONCgYZWp39EBK_83cZRC0QPsHboxOKnViUtC3TlrWOSCQEPZKbnKTXYdZc0apCEPZg9yLq0OVfiG30gO1ZVfJw1mOH0g_6uhf7J0enqk5lrULrUolU0l8AuG9Dd2peCESIP7gpieO1FIiEkHQCq-KCJpDOP_B7AqI_E8dLdQf4IUsugi7NNhC07F_d75uwqig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد جديدة من النيران التي لحقت مطار الملك خالد في الرياض اثر الضربات اليمنية الاخيرة.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/93116" target="_blank">📅 23:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93115">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEAY30RFKRiIax7GQzOu5Jown8vPD4R0XvVwC0dnExn_em-CgCn5u5gy0EPg3tWcB4i4sXfi0YTIpjktH4JrOMrmTun3jXSKI8Ogh_-VkJMqpDAH6Xp7TyF3zMqL_fbHmYU_AmshlT1wLEyJLZN8hhWGgkLLMpWLrepsxUpvcLQU2SCrDdazCiJ5qtzFrI0FWewfLgFQfHQtM05PTvcrLUatQnObSegNEwkJFQf3_5hkkFdSn2iwQId0C1FlAEa-cvKYS0p1pn1LZGpE_t3M0Es9x48rwm1ka-4tbWWTdwEMD7XtAYKR_ZuUUbywidATFep6J02N_lLPK3s1ZcoO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
يستمر العدو في انتهاكه الصارخ لسيادتنا الجوية، انطلاقا من قواعدهم في الأردن وتركيا والاراضي المحتلة والكويت والسعودية.
طوال ساعات يوم الخميس 8-10-2026 .</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/93115" target="_blank">📅 23:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93114">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaKu7JbQm6pj_hEHTzzUOdyUtDhzCqn7iC-AcTSxvoj_IQKPcY1tzpkkYEzXjuCvlHLnS_lbdanFBEY4CvraFrpqZcD10MiYtK1cHdoz1mEPQKlkgIpV9p7WxqqMH59sLhf9zIXxrffePKbxKbwkdBuEfv7R3jUoUAhJAdPiGf0kPlky64qmyWtMKjEJt266cNoOjbGAVjwNGRcBBgqAXD0lmuwludwMW9XFgExlCUfZGXnXWA1_eEJK2muwRiFIaJnxx7AlWjEaIx-avTiNq4cjCKi47gtpj56wfu20BMNvZpD3O0_D20P_TpfQqYiTasD_XicD0XDEHprtkEBBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب:
لقد اختتمت للتو محادثات ناجحة للغاية مع الرئيس فلاديمير بوتين، من روسيا، حيث تم الاتفاق على أن روسيا ستقوم فورًا بتوريد أكثر من 300 ألف طن من وقود الديزل إلى السوق الأمريكية والعالمية، و500 ألف طن أخرى خلال شهر نوفمبر، ومليون طن بعد ذلك مباشرة.
بالإضافة إلى ذلك، وبناءً على حالة مصافي تكرير الديزل في روسيا، ستقوم روسيا بعد ذلك، في فترة زمنية قصيرة، بتوريد 3 ملايين طن من وقود الديزل. وبفضل سيطرتنا الكاملة على مضيق هرمز، وإعلان هذا الإنجاز الكبير في مجال الطاقة الروسية، ستنخفض أسعار الديزل للمواطنين الأمريكيين، وبالفعل للعالم بأسره، بأرقام قياسية وبسرعة كبيرة!
إن خفض الأسعار للمواطنين الأمريكيين، وخاصة مزارعينا وعمال المزارع وسائقي الشاحنات الأعزاء، هو أولويتي القصوى. هذا إعلان كبير ومهم للغاية. بالإضافة إلى ذلك، يجب أن نفهم أن إيران لن تمتلك سلاحًا نوويًا. شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/93114" target="_blank">📅 22:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93113">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مطار الرياض يحترق بعد الهجوم اليماني</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/93113" target="_blank">📅 22:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93112">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇱
الاعلام العبري: محاولة استهداف سيارة في بلدة حوش السيد علي قضاء الهرمل على الحدود اللبنانية السورية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/93112" target="_blank">📅 21:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93111">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAKKUYLsW7EWmiNUfZ9mgfuMrB9yL43Lswc4EQn9cnsYZk8oQ3rB9RuJtZ6zGea8Vnm9H4uXrbBPSJ5kvtdWEgkCN7_O_-sPvN6gwhO2ryZNTEFWdEPHXdFJFRypTxkJ9IfuCl4rbrXUGlx4rDmNviGLg2z_XY3CO6BbEKd_Ix5Tt2ndp2ctNMPMShYVut-VjYusTONf_XqiHth3Vdl92qc31TeiZKAfJoTa_vDdt2DsuXYcdTuLE5FsW8lwc8UP3e_NKEInqqdhKyfFnDv76wn1wzc6qTbHAwPPvbbzC26GYVn7HiWW6wQWTSwG2Gp4mPytUhsyxCcopKjWoSbKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/aboalaa_alwalae/status/2108613399643123736?s=46</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/93111" target="_blank">📅 21:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93110">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 77 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية في العاصمة صنعاء ومحافظات مأرب وصعدة والجوف وحجة وتعز وعمران وذلك من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدنا 1934 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/93110" target="_blank">📅 20:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93109">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWqV7je3UoC5x8hQUwRngkKMB3AMW0AZS0761mGlZFhU3FXOZze7GJl14derjPGMdB30yTScMl1eTeMP-RiNMPrCe_y2SH3WnOP70RyfucJFKEsemqcq7d3zPC7ERr_eRktuBo64tSV4iuroqTCh18PZMlhYIRumTt-egW7i3zK9C2TI-gNo3P7yo9G5Fis1rsW3FE8PX0MfZar200WUP2AV9Y9EZMDcB5vGJuI_Hcq1ADOE43Q2y9VYwbOBA31eQDgwAmZmbJ-cfQiZ3cK0-SRNj8lKjYrMfcsAPpRv7o31zqIC3eXYcryz_bNZ40P7FxQKlKISG0WrusRy0xhO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترفيهي
النظام السعودي ينشر باللغة الهندية يحذر الهنود بالاجراءات القانونية في حال تصوير الطائرات المسيرة والصواريخ واماكن سقوطها</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/93109" target="_blank">📅 20:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93108">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
🔻
الحرس الثوري:
صور غير منشورة للطائرتين شاهد 136 و238 وهما تطلقان النار على مواقع العدو الأمريكي في عمليتي نصر 1 و2 وعملية معاقبة المعتدي.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/93108" target="_blank">📅 20:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93107">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
اعتقال اربعة اشخاص من الجنسية الافغانية متهمين بقتل مواطن عراقي في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/93107" target="_blank">📅 20:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93106">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjX94G5dqzb0oaNZLrVoVgcIOI5lus8aDCKiztSRbnwrCRj6EEtyl2mnWHTabn207ljQROG-HRDpPJClxIVUS5GKgfHDxm-g91JzJsj2dGfC5gzetX2ndSQ0JQBSmZnUJRcNd4658mgPOzqkpfIX7pQrz4RtSgabv4ZBv-j3l_vPYgu7kYtd5sM8Bqf3YTIdU1mUCymfDdbuhzhUBLpXJyB701I2Es8Ya02jZGcO7pL1GXLvyVwaT7I4xAOBsEQLo4FKuiphp0lBgUoe3X615iaZv2q5SrTnWfdCTptqew4Yh3OpNR5ivDVKEDjs1YaLMBs5J-w6jAEBLccVYioDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
المعاون العسكري لحركة النجباء الحاج عبد القادر الكربلائي:
كان الأجدر بالعراق أن يحذو حذو هذه الدول، وألا يمتثل القرارات الظلم والجور الأمريكية ليجنب نفسه مشکلات هرمز، كما فعلت دول كثيرة ويبقى نفطه يعبر بانسيابية، كما هو حال الكثير من الدول التي رفضت الامتثال الأمريكا المجرمة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/93106" target="_blank">📅 20:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93105">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
ترامب حول إيران
: إنه ثمن صغير جدًا يجب دفعه، إيران كانت ستستهدف على الأرجح مدينتي سان دييغو ولوس أنجلس بسبب سهولة مسار الصواريخ إليهما.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/93105" target="_blank">📅 19:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93103">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
صاعقة رعدية في قرية ابو طيبان ضمن محافظة الانبار غربي العراق تسفر كحصيلة اولية عن 2 وفيات و7 مصابين.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/93103" target="_blank">📅 19:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93102">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامب: إعلان هام قادم بخصوص الديزل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/93102" target="_blank">📅 19:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93101">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامب: إعلان هام قادم بخصوص الديزل</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/93101" target="_blank">📅 19:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93100">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فلاي دبي تلغي رحلاتها إلى الرياض وينبع وابها في السعودية بسبب فقدان الامن</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/93100" target="_blank">📅 19:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93099">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
الولايات المتحدة تفرض عقوبات على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/93099" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93098">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcd2029e25.mp4?token=dYzW1pAH_N95eOpy7r6twzcMESS3LQtgUlMEuEyeU45KOkmIyswd_Gh7-fxjN1fr2UQYjjrX4mht7aegChsSyKhXKzilzJOyaUUcvrwAFdg8tTunciDLLHzQpka4Xf3XjkbSRT194eMnEIMgK2BweJGfYBeNLPskPDlogMEpJDg-xQ2uBX8a6f1vIuEdIvQU2CrpyLgKH2aV76AF9aLSQNKmHkkJy_FXt7I2CnhRPI88usWquq0ZG5-o7wnxd5WkhmvxpGDcCfpfZp9RTXIKVimtbKrmlinVQ5pwW7r7UBnkVOjWTwWx89B2k-lZgm6a25vo-FfFSsLzyRuFTHf0H155k3rosWCPDgU9pVfhDRbiaffMaQ-AUgcSD-axWQr2q86LAxW_AOU9dSJy4pYLcYbEITcuDkrQVc0PtSm1SDPvcfjXc88px0ADPEnvsczDuhlkpZo1emUKd4rNfVUlnr1YN1bdEXL7qhAo2jdy7t9kMQCAnqendvxPpJ7AfeR30_Wl-j90NI-ZaDH8qj0hqM0_XiKOZ5ZGFHEuhDrxhZYmSuzOjSS8h4AFnnB4To9gjIM7jG-nQstpIHogMMutvZb2Vs95Z76h6yZtL4QIsrJH00VZzw2qC2mdLXI1flyHDgk8R7zO8poGiGqtOUvmBUzpYxHL8wEfGSwnxvuoOIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcd2029e25.mp4?token=dYzW1pAH_N95eOpy7r6twzcMESS3LQtgUlMEuEyeU45KOkmIyswd_Gh7-fxjN1fr2UQYjjrX4mht7aegChsSyKhXKzilzJOyaUUcvrwAFdg8tTunciDLLHzQpka4Xf3XjkbSRT194eMnEIMgK2BweJGfYBeNLPskPDlogMEpJDg-xQ2uBX8a6f1vIuEdIvQU2CrpyLgKH2aV76AF9aLSQNKmHkkJy_FXt7I2CnhRPI88usWquq0ZG5-o7wnxd5WkhmvxpGDcCfpfZp9RTXIKVimtbKrmlinVQ5pwW7r7UBnkVOjWTwWx89B2k-lZgm6a25vo-FfFSsLzyRuFTHf0H155k3rosWCPDgU9pVfhDRbiaffMaQ-AUgcSD-axWQr2q86LAxW_AOU9dSJy4pYLcYbEITcuDkrQVc0PtSm1SDPvcfjXc88px0ADPEnvsczDuhlkpZo1emUKd4rNfVUlnr1YN1bdEXL7qhAo2jdy7t9kMQCAnqendvxPpJ7AfeR30_Wl-j90NI-ZaDH8qj0hqM0_XiKOZ5ZGFHEuhDrxhZYmSuzOjSS8h4AFnnB4To9gjIM7jG-nQstpIHogMMutvZb2Vs95Z76h6yZtL4QIsrJH00VZzw2qC2mdLXI1flyHDgk8R7zO8poGiGqtOUvmBUzpYxHL8wEfGSwnxvuoOIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في مضيق باب المندب بعد الف اعلان سعودي حول السيطرة على المضيق</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/93098" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93097">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52c72fd4d.mp4?token=J-P8MpwnCK9hA_w1c1RzCOyx74EqpsuWcs87nn3BVtqfdslHWyMn8MqqrIehmR1NwyHimTY0ZKfi64yc2_XUIDWpB1S8iawcHktRpr8eq5fJxa59I9Oo_T3cb6wS1Cbe7RYpslLRG8oWPnS1BKskK2l6bWNevQpHwXKCrG5UC8OoamrdUvim-N6mbZLO65eAfA9e3FWi7sqxFnap-iJOaaBzlphWllQbS3YeCfJD-lU14eqoxCTfbDnaCFWvtmpqSNkybP-UnRBY5qPJI5ifkvrP9qXjoAcbkmk41g_2WiM2MTVxZyWU695g-su_QW5eolY2oCbAA9fwCsCQrf73FjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52c72fd4d.mp4?token=J-P8MpwnCK9hA_w1c1RzCOyx74EqpsuWcs87nn3BVtqfdslHWyMn8MqqrIehmR1NwyHimTY0ZKfi64yc2_XUIDWpB1S8iawcHktRpr8eq5fJxa59I9Oo_T3cb6wS1Cbe7RYpslLRG8oWPnS1BKskK2l6bWNevQpHwXKCrG5UC8OoamrdUvim-N6mbZLO65eAfA9e3FWi7sqxFnap-iJOaaBzlphWllQbS3YeCfJD-lU14eqoxCTfbDnaCFWvtmpqSNkybP-UnRBY5qPJI5ifkvrP9qXjoAcbkmk41g_2WiM2MTVxZyWU695g-su_QW5eolY2oCbAA9fwCsCQrf73FjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع اشتباكات عنيفة في شوارع الحسكة بين عصابات الجولاني وميليشيات قسد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/93097" target="_blank">📅 18:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93096">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bbc462dbd.mp4?token=q_rqUA3o0-IgcXZYPQApFadv3fLWQVj9mPM--JQkp3q2tBrTQX0AqhdeXCk5J7P36HP6F9D4s7tO83SVzVCB9oRBihNk3tylOe3gkSoyNwRAlvFg_WOiB0a9beY8mT7FLdqUTR5Avws8LCmgElXldd3yimwWEIshn9IT5wSY_o7mtG6oJmyp9DlBz3L_RRALMYnaurjlBDrbVps6IHkX31iMpYRJ6rA7yU0xmW5WhjR0Ubc_yL2dTxdkuoVG5WOXaXKVHRMYun0XpD_gIrjB82b5i_eRGDkQ6rQjH5Rys5aeD8GKHrZpJd6wCpOyR5ri7_h1jXgcvzDZUJoSIYyYO5GuaU2gr03T6bTEQgkyG1lHcuhzrjNtutE9uwsgJegD3vP8E23LPhjnqVoZeQRiusYFMZrdHbsv01HF9XkLxRs1K2ybl7lHIpQJrxz7dAzi1UDjkJYrg1SvQB-pnCLDYjq7R4_FAxvm7gr8dCu-yUD48wzFJYGgzcWHj2TbMy-LGhmGVp-P-lgc3G_ZTW4Dl9C53vL9yvL886GPF5-ptE57dEPcdfeVYGRfPofD-8zMlHIvMqdyDggsix76z6OJvmClmwqAQe7ItKUM4-uq9D3RaoryrpnydCGyixIfecYAeq28ly7aKqxUJNgeufM98rVLv4XHm4MrsNuL8QzgHec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bbc462dbd.mp4?token=q_rqUA3o0-IgcXZYPQApFadv3fLWQVj9mPM--JQkp3q2tBrTQX0AqhdeXCk5J7P36HP6F9D4s7tO83SVzVCB9oRBihNk3tylOe3gkSoyNwRAlvFg_WOiB0a9beY8mT7FLdqUTR5Avws8LCmgElXldd3yimwWEIshn9IT5wSY_o7mtG6oJmyp9DlBz3L_RRALMYnaurjlBDrbVps6IHkX31iMpYRJ6rA7yU0xmW5WhjR0Ubc_yL2dTxdkuoVG5WOXaXKVHRMYun0XpD_gIrjB82b5i_eRGDkQ6rQjH5Rys5aeD8GKHrZpJd6wCpOyR5ri7_h1jXgcvzDZUJoSIYyYO5GuaU2gr03T6bTEQgkyG1lHcuhzrjNtutE9uwsgJegD3vP8E23LPhjnqVoZeQRiusYFMZrdHbsv01HF9XkLxRs1K2ybl7lHIpQJrxz7dAzi1UDjkJYrg1SvQB-pnCLDYjq7R4_FAxvm7gr8dCu-yUD48wzFJYGgzcWHj2TbMy-LGhmGVp-P-lgc3G_ZTW4Dl9C53vL9yvL886GPF5-ptE57dEPcdfeVYGRfPofD-8zMlHIvMqdyDggsix76z6OJvmClmwqAQe7ItKUM4-uq9D3RaoryrpnydCGyixIfecYAeq28ly7aKqxUJNgeufM98rVLv4XHm4MrsNuL8QzgHec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات بين عصابات الجولاني وميليشيات قسد في محافظة الحسكة السورية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/93096" target="_blank">📅 18:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93095">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
الولايات المتحدة تفرض عقوبات على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93095" target="_blank">📅 18:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93094">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة بفضل الله وعونه وتأييده _وللمرة الثانية خلال ساعات_ من التصدي وطرد التحشيدات التابعة للعدو السعودي التى حاولت التقدم من جهة لحج باتجاه باب المندب ولم تحرز أي تقدم بفضل الله، وتم استهدافها بعدد كبير من الصواريخ الباليستية و الإسناد المدفعي وبالأسلحة الثقيلة وتدمير أكثر من 22 مدرعة ومصرع وإصابة العشرات بينهم عدد من القادة
ووصول أكثر من 30 سيارة إسعاف إلى عدن تنقل القتلى والجرحى من تحشيدات العدو السعودي.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93094" target="_blank">📅 18:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93093">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">استهداف تجمعات الجيش السعودي في مطار عدن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93093" target="_blank">📅 17:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93092">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7828e24c.mp4?token=cbSB7heTuIpbV6qd_TdIuQ33jbVq_Z4YyNNeos33vHWqoMfMlTD6sm3q9uWzeCorF40DhW2NQVKwU9nsIP5JH_4b9A06lNsIj8xPWQ8ENKUcPv_u43yykGGMOdb9hcBVARNP9qfSD3CHDcOEgZ1srt5YpfGzEYoWiY-w1qVpukeaIA8Sdl9qcT_cg3tsyfpdKSJJGQAN4dRoZKH1MJPmOzwz62vC90A2ReCymnsGj3fAVtl8enWd5aVYMc1bT7mZ4MsTV7RQSFbk7OWgjD5eBwXFr8UxU-S-_DKg02EwjkHlK7Y9mwElgDtQH1XmWRm5qUecZWz3lIh2fPsvr4UxXn5-9GaX7EsFdSykQucAdObp2SAtbfBfDYEZGCAFFyhb8BcNq96TI2Z17iKweibr_9XLjJkp8oFCo0RJu8FYew5k6EPiXGl7wC4z6rqx66DoiJva_wfMDY-mnwkQt86Aa0rsXOHmE5drpHW7QBqJRw4HLpRt0n9XjGqDzITVBRTq51DVFrievklsyKQjuaeCAqzC9MBJfWSK3XCI7aBzfsVqG4Ak9IdvPo7BakZ2QG_yE2R0d5vPiVTY9qjXg-iIr8zjIPPC42s01OTvviJTxw9b1mwZw95vB7YK_bVB-moCYEi1ZOc7-TsxFv6bHvlzpowSWJaGjEYdKojsiK3Llm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7828e24c.mp4?token=cbSB7heTuIpbV6qd_TdIuQ33jbVq_Z4YyNNeos33vHWqoMfMlTD6sm3q9uWzeCorF40DhW2NQVKwU9nsIP5JH_4b9A06lNsIj8xPWQ8ENKUcPv_u43yykGGMOdb9hcBVARNP9qfSD3CHDcOEgZ1srt5YpfGzEYoWiY-w1qVpukeaIA8Sdl9qcT_cg3tsyfpdKSJJGQAN4dRoZKH1MJPmOzwz62vC90A2ReCymnsGj3fAVtl8enWd5aVYMc1bT7mZ4MsTV7RQSFbk7OWgjD5eBwXFr8UxU-S-_DKg02EwjkHlK7Y9mwElgDtQH1XmWRm5qUecZWz3lIh2fPsvr4UxXn5-9GaX7EsFdSykQucAdObp2SAtbfBfDYEZGCAFFyhb8BcNq96TI2Z17iKweibr_9XLjJkp8oFCo0RJu8FYew5k6EPiXGl7wC4z6rqx66DoiJva_wfMDY-mnwkQt86Aa0rsXOHmE5drpHW7QBqJRw4HLpRt0n9XjGqDzITVBRTq51DVFrievklsyKQjuaeCAqzC9MBJfWSK3XCI7aBzfsVqG4Ak9IdvPo7BakZ2QG_yE2R0d5vPiVTY9qjXg-iIr8zjIPPC42s01OTvviJTxw9b1mwZw95vB7YK_bVB-moCYEi1ZOc7-TsxFv6bHvlzpowSWJaGjEYdKojsiK3Llm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
شعار الصرخة يهز جبهة الاقروض مع تصاعد حدة الاشتباكات بين القوات المسلحة اليمنية ومرتزقة السعودية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93092" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93091">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">القوات المسلحة اليمنية تدك مطار عدن</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/93091" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93090">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">القوات المسلحة اليمنية تدك مطار عدن</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93090" target="_blank">📅 17:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93089">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c3880c04.mp4?token=BHPhS-cnG38rkIpfsauv1CcJik1F3ee2-Yw2iSYf25i4fbxO9uPdG07w-38GbKLZVh5SjXn8ozIrxa1s6I5wcbk7pVlo30xueeXGciy1SAHMT4_k8C_Uw2zkK4ynPfJReGta5qv_jxjVpC1P9eF7M7uYgxH4t3R4VlxLWmzEhNiuoCOBQy-O1olJy6pVLXDFO9IuDcU4BYzZ6eNGpBVSqJfsf3DGkV3g3MjvscAOgqRMRwWeEdjALM56kJSFcHXJaYMxTRDak4RnjBMtqUUfzPblkmZsI_HcyOZTNLinWv5o-SyAnKn2cGH42aX4gJ4108XK8_qc6x-yW3GC059sGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c3880c04.mp4?token=BHPhS-cnG38rkIpfsauv1CcJik1F3ee2-Yw2iSYf25i4fbxO9uPdG07w-38GbKLZVh5SjXn8ozIrxa1s6I5wcbk7pVlo30xueeXGciy1SAHMT4_k8C_Uw2zkK4ynPfJReGta5qv_jxjVpC1P9eF7M7uYgxH4t3R4VlxLWmzEhNiuoCOBQy-O1olJy6pVLXDFO9IuDcU4BYzZ6eNGpBVSqJfsf3DGkV3g3MjvscAOgqRMRwWeEdjALM56kJSFcHXJaYMxTRDak4RnjBMtqUUfzPblkmZsI_HcyOZTNLinWv5o-SyAnKn2cGH42aX4gJ4108XK8_qc6x-yW3GC059sGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
شعار الصرخة يهز جبهة الاقروض مع تصاعد حدة الاشتباكات بين القوات المسلحة اليمنية ومرتزقة السعودية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93089" target="_blank">📅 17:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93088">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3629a87b.mp4?token=h4M7Cg3tCQEb-3nxu4-ePdgB6v0prw3ZZve26cSwofC3ACI5dodd4GYEj2hK07nBtg13w9m_OnoXDLlymMfZzyV8BtNoCSy3M-aoHQH-yz-2IukYuW2iiGqEL99gFM0-3O7qY5-2BgBaPnKvrKJ-KQMt5tlaAyYCV3o7-GN02gyOcTHIngwyNb-50Bljq6yrJo0RZpWMZysf3ST68cO0biREsGc0Ouvd2qs2OazQOT12mPKFAdXY16jovW0zV62uRms2u9OcUbJnX_lAuXHpDvqMAXeXvvMvsP9Eq9lOhK65hE8r0NpIi9G6Odf9L9BWCngs2i972SxnIhrqENw7Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3629a87b.mp4?token=h4M7Cg3tCQEb-3nxu4-ePdgB6v0prw3ZZve26cSwofC3ACI5dodd4GYEj2hK07nBtg13w9m_OnoXDLlymMfZzyV8BtNoCSy3M-aoHQH-yz-2IukYuW2iiGqEL99gFM0-3O7qY5-2BgBaPnKvrKJ-KQMt5tlaAyYCV3o7-GN02gyOcTHIngwyNb-50Bljq6yrJo0RZpWMZysf3ST68cO0biREsGc0Ouvd2qs2OazQOT12mPKFAdXY16jovW0zV62uRms2u9OcUbJnX_lAuXHpDvqMAXeXvvMvsP9Eq9lOhK65hE8r0NpIi9G6Odf9L9BWCngs2i972SxnIhrqENw7Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من محافظة السليمانية في شمال العراق لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93088" target="_blank">📅 17:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93087">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4386405697.mp4?token=SmIyA7jkXGz6rJMrEFh51kvABjt1wJ5GQFyYB1dESEOPJWgQL_pXTMg6YvLC0gtaiphtlXKF9zpIPoKQcvO6qdVpqJySmEkv3QEnxjOyjEVkOLQDY7LBTHJbUAJkOd0KmLph4Xo1U45n9Ua48K40dMx8ehQs6Gmt3n2IE7_6-RB75onVLCTEo9Sa_bjXaAbfcZvTFexJBQJKQ4pvYi8cY0JpHh04t7kKFREC1zQGxzD7xICdXFbRGBfC6Yei6zPooBViCOWrSJbyumGr2eobZ_vCgram5klRdaU2iIO9rTvRK_XIZqMJEspeYRYwtYrbld8vP4Z-MzrlVb8p9-ScHCJS9EwsNcUlJ_vkapetXKLlI6xUyYI9kMyHCmGMCF2YeCQAb_q9ZGhuCgeNhqyg4NFNbBLyPHNL8pGxj3u20YUBiBCpJt2jchhBwEC76_qnDe1wr3Hp3iqeZ4CqbxEv9iTCjHexDHEDY5BIW9OdUqvORoV4A-FG38txOt_hOWLfdjLI6YeQ_0kCF0SDRMmhaDa8k_JOHnv5hHcX414DVZ9s2krRRWun2xlswiWVrDWgd4lbJUMryE-GWOZ3f6haGkTwy4-VxbL2KPrmeFzKDHTeFIpms80ZlHvggbRlzjv-hqhtU8liYDyOcFESI3RCrR5CC8U9g8vyY5BNODx8Cck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4386405697.mp4?token=SmIyA7jkXGz6rJMrEFh51kvABjt1wJ5GQFyYB1dESEOPJWgQL_pXTMg6YvLC0gtaiphtlXKF9zpIPoKQcvO6qdVpqJySmEkv3QEnxjOyjEVkOLQDY7LBTHJbUAJkOd0KmLph4Xo1U45n9Ua48K40dMx8ehQs6Gmt3n2IE7_6-RB75onVLCTEo9Sa_bjXaAbfcZvTFexJBQJKQ4pvYi8cY0JpHh04t7kKFREC1zQGxzD7xICdXFbRGBfC6Yei6zPooBViCOWrSJbyumGr2eobZ_vCgram5klRdaU2iIO9rTvRK_XIZqMJEspeYRYwtYrbld8vP4Z-MzrlVb8p9-ScHCJS9EwsNcUlJ_vkapetXKLlI6xUyYI9kMyHCmGMCF2YeCQAb_q9ZGhuCgeNhqyg4NFNbBLyPHNL8pGxj3u20YUBiBCpJt2jchhBwEC76_qnDe1wr3Hp3iqeZ4CqbxEv9iTCjHexDHEDY5BIW9OdUqvORoV4A-FG38txOt_hOWLfdjLI6YeQ_0kCF0SDRMmhaDa8k_JOHnv5hHcX414DVZ9s2krRRWun2xlswiWVrDWgd4lbJUMryE-GWOZ3f6haGkTwy4-VxbL2KPrmeFzKDHTeFIpms80ZlHvggbRlzjv-hqhtU8liYDyOcFESI3RCrR5CC8U9g8vyY5BNODx8Cck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي على صنعاء</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93087" target="_blank">📅 17:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93086">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ad45a45d.mp4?token=uLoo-YieStt9aUha3MxX7DCvWfpjXGNToyDwsJYKRFjiuiJ77N1WzJq3Tx8gPTzS6w-pJ6RU2nXe5cTvzDNeAkcbrIylngf-TXjchJCXDr_-WGXwLolg3AmHhP8ZCbPoSaX7QF09sIwLSbfwNAnM9qcBLQhXTsCAuL6pjwphPl6mAsgprENz71fmwar9PeTNRoX7YVSFyHju1rTm3YVYqEXp4RxRIB3isv95HsEoDyjsOdkTsguDuFBbFRYJUMAP2RWvFI96aOefI3GpjKMQJrM16kU91zgmgzu0Tis83NcXnqwlOZqVaMPzPPx1_W_vKwNjKU5Md1wWr13y7sWDBDqKrgnY9E_IQtOFc8WPuarZf2GsWPWjWV3EnVzkrly4zwIjx39jp-lE33gj9mLXdIvx39NXeZSo534P42yCtmTBIqwg2ssPXU9_k7rIgTzrLcgFjlGCeAvCY20Da1xpuJ_G4DQesGFWQSkvhhXI-bEP72vnxUBHeWyNopUO3a2u-lK7bVNTmvP9XRJ5PJCHRIruZ_Rc3RvNO8LCXDtOs-1yjDWyRoubvPOGckrr6E2qCm6L6ewF87DPLfI31Y1w2nS4cEN1wxyF6cBINitDrK7ahfhmH0NGh1B2r7zsFJl1322VVz5-ikPaDcL4Abj_Bgb495_P8V8IQlmP1pd34Fs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ad45a45d.mp4?token=uLoo-YieStt9aUha3MxX7DCvWfpjXGNToyDwsJYKRFjiuiJ77N1WzJq3Tx8gPTzS6w-pJ6RU2nXe5cTvzDNeAkcbrIylngf-TXjchJCXDr_-WGXwLolg3AmHhP8ZCbPoSaX7QF09sIwLSbfwNAnM9qcBLQhXTsCAuL6pjwphPl6mAsgprENz71fmwar9PeTNRoX7YVSFyHju1rTm3YVYqEXp4RxRIB3isv95HsEoDyjsOdkTsguDuFBbFRYJUMAP2RWvFI96aOefI3GpjKMQJrM16kU91zgmgzu0Tis83NcXnqwlOZqVaMPzPPx1_W_vKwNjKU5Md1wWr13y7sWDBDqKrgnY9E_IQtOFc8WPuarZf2GsWPWjWV3EnVzkrly4zwIjx39jp-lE33gj9mLXdIvx39NXeZSo534P42yCtmTBIqwg2ssPXU9_k7rIgTzrLcgFjlGCeAvCY20Da1xpuJ_G4DQesGFWQSkvhhXI-bEP72vnxUBHeWyNopUO3a2u-lK7bVNTmvP9XRJ5PJCHRIruZ_Rc3RvNO8LCXDtOs-1yjDWyRoubvPOGckrr6E2qCm6L6ewF87DPLfI31Y1w2nS4cEN1wxyF6cBINitDrK7ahfhmH0NGh1B2r7zsFJl1322VVz5-ikPaDcL4Abj_Bgb495_P8V8IQlmP1pd34Fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي على صنعاء</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93086" target="_blank">📅 17:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93085">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR-a-7uuE74Pq_iXAHcg0rjhOvUEr99W5j7eGyBHDqRkVkUf9YQOUHXopNq989c3BECRCJO_LfyVUJ2N3_6eNnq_O6gJOpSlmC-4y-cPW-vkDjVDiSQSU5FtokCR-QuuAExm9BkK1imGe2B5-cwDMmR9BMl_hLvNw4yk0ab72rIiu3aDqD_zmenoIWcwW8SYCAKdousBOzT27Td-M4seEVbpGc_kgjHQxOp8qnxWvYW0_b6fk3hsn5-mTmPlS4ErwFoDkly4vVpzeXvSr5iiMwflSbTWiGf-csW4LD_CWNA_6sItu7Jyqr81J8Fsf_t9feACZGluaS-X2sFkE8YiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القيادة البحرية للحرس الثوري: من الآن فصاعدًا، لن يقتصر التعامل مع السفن المخالفة على مضيق هرمز، وسيتم ملاحقة أي سفينة تمر عبر ممر غير مصرح به في جميع أنحاء المنطقة، وستكون عقوبتها نهائية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93085" target="_blank">📅 17:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93083">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBECvXht8NxTWOhKngMqYQGK-v-T0qPmO7Mw4GjR9pN-iDsnQ-qv746hQA4JZMJ1062nWvEhduqIyIns__26OwJXSx3tVjLWZpJjF89ghNIQ6C4slKy8-CUNKrJtXV2F0UOSIghLVwbEQtvg9v56xJTJj65iAQ-W7QLlSFUdsh2vQGIQtglMGtUiQDxv6zG101L8W3ZcbVr__oC3O_c2Uts4ZuUrzZ4TNaGaHjUSrScgjlxBTeHsQlDcj2085tllgC77q9i0M0My4dm9uhgrjlLgaoVOhoR05RifJXnSOurDcm9LTH4xcamXk8qvT47jh3UTux2ShQ5v1favkpm5jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndGZ1zLNUeqAbei47qdeMNxVwsLfr6TxCsLvZS9IfD2BZWJ4HuJCjNI_swOv0M5dWrfBx3keDMhwExgFaC8A_hSvrP6LLfBkdjdUHy4DSYMYKrV9EImSdJ3gPVxZhXfvVTTNUg87oG0lm51QOmYQTh4dg616yWh8xn46h2kGHUScZ-_E7MdwPje_ctpkTsPu-F6S9mDjQyADhQn0OA0uGUu30AlrItMkRm1nCAoxx4kRycEinX-cmASqpDS0jUzNRFHasp480Hg5HtnFDIUBDCr_0b3Ie82YkC_-u-e3uH_FY6vK0cQJ5X70CD6GrBL7Bji2we8PD2k-B8fGo0sizg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من العدوان السعودي على صنعاء</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93083" target="_blank">📅 17:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93082">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de14d93788.mp4?token=TJoRR2DhNfSWWJNPMxkFnWcCcXlechbLfNKm3cLM2aV-0Y_DH1IodIBqz9YqA5k-q9tx3zWgLD7CRM0Zx5GPaIULX8snw2Wi5hEyXD7x1JZnu_QdhxFNFuLz2fujY5zuGN4g7aSV6fi3GbbJMcdzlzvWoXzxljH3nASj2p2S6-FxQJmc43rQLoyIUIWKR0cCCqz4PQ3GyJXAEsHWzHzOU37FVWx6MU3QKLqE4mIsdVxgsotBmO0rs2byNspKD3ipQWS8r9UQjbJFP4uVscmLBLHOuCasuisv9rscWMrDXd2VP6Yqj3fgqMWdSB5JEDNq9SlxWB04rhccbE1E-1aeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de14d93788.mp4?token=TJoRR2DhNfSWWJNPMxkFnWcCcXlechbLfNKm3cLM2aV-0Y_DH1IodIBqz9YqA5k-q9tx3zWgLD7CRM0Zx5GPaIULX8snw2Wi5hEyXD7x1JZnu_QdhxFNFuLz2fujY5zuGN4g7aSV6fi3GbbJMcdzlzvWoXzxljH3nASj2p2S6-FxQJmc43rQLoyIUIWKR0cCCqz4PQ3GyJXAEsHWzHzOU37FVWx6MU3QKLqE4mIsdVxgsotBmO0rs2byNspKD3ipQWS8r9UQjbJFP4uVscmLBLHOuCasuisv9rscWMrDXd2VP6Yqj3fgqMWdSB5JEDNq9SlxWB04rhccbE1E-1aeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجار في صنعاء وسط انباء عن عدوان سعودي اجرامي</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93082" target="_blank">📅 17:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93081">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سماع دوي انفجار في صنعاء وسط انباء عن عدوان سعودي اجرامي</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93081" target="_blank">📅 17:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93080">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇱
بلدية كريات شمونة:
سيشنّ الجيش الإسرائيلي خلال الساعات المقبلة سلسلة غارات على الأراضي اللبنانية، وستُسمع أصوات انفجارات في المنطقة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93080" target="_blank">📅 17:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93079">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
عناصر من التيار المدخلي تقوم بكسر أقفال "جامع أبي بكر" في منطقة النساف ضمن محافظة الأنبار غربي العراق بعد إغلاقه من قبل الأهالي احتجاجاً على ما صدر منه من خطاب تكفيري.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93079" target="_blank">📅 17:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93077">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c2f4e39e.mp4?token=iGgWiSLXjC-r7EBuDPWo9FgQ-ze540ZYNA5QdH_X8Be8Vt2qvgVwA4Os4D7m2pNyY9eqHSo2Ba4R4_ttWZCHe2B0shyWwsZCRCutNCnaBne05EhxELd6mzz4NcbtA68Ggigm2kdxPt15jWsOgUhbR27Qu9T2fNdMaK8uP9u222_Ga1da5hte2uwIf1yH-o0vrDaHnLZQW2orZlde5oClZkBSIsfxfex_zUIeXRoskH2B5AelDUO4CV-zNfslvnVL9zCwKu0SYH1eZ5rXPh22VzJgdyVmpvg9AIHlqtbTFHAonsVM0utwBFwpQpqD6qS-f6JbSIgJeSK1pgU8V0sVTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c2f4e39e.mp4?token=iGgWiSLXjC-r7EBuDPWo9FgQ-ze540ZYNA5QdH_X8Be8Vt2qvgVwA4Os4D7m2pNyY9eqHSo2Ba4R4_ttWZCHe2B0shyWwsZCRCutNCnaBne05EhxELd6mzz4NcbtA68Ggigm2kdxPt15jWsOgUhbR27Qu9T2fNdMaK8uP9u222_Ga1da5hte2uwIf1yH-o0vrDaHnLZQW2orZlde5oClZkBSIsfxfex_zUIeXRoskH2B5AelDUO4CV-zNfslvnVL9zCwKu0SYH1eZ5rXPh22VzJgdyVmpvg9AIHlqtbTFHAonsVM0utwBFwpQpqD6qS-f6JbSIgJeSK1pgU8V0sVTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
محاولة استهداف سيارة في بلدة حوش السيد علي قضاء الهرمل على الحدود اللبنانية السورية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93077" target="_blank">📅 16:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93076">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
انفجرت عبوة ناسفة على جانب الطريق في طريق سيارة تابعة للشرطة في منطقة "تشمه زيارت" في زاهدان بالجمهورية الاسلامية اصابة عدد من الشرطة كحصيلة اولية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93076" target="_blank">📅 16:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93075">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoVsjvhaEN9xV6lv-6bEYKe4u_H3lhpbIWNm9WrIKFemPd2YvEOlod2TSscw5ynC0pQF1Fogw0QFztwesC9-ywz_nNlvVot8VhpZyE0ssO5d6F865pEZSB5_IoBA1nL8sW8aAFwyyDfKoVuQJjxlmuJcYtnaxBVM0Nhr365oeaz-s9vTAbhOlRWyhTvUKxlOCpH2R7KU_CviRnTDkfAEhlVcpWPZBsqtAyvIq2XpmHQD6GtchyOBPMQVCyT6xSr64pH2D69Z-q4g-mv4LChqDD3R4H_0Lw0vM32BHxJ8yv3Pxz0MkRfr8-feVzUy5V8mo2lNojnyG5MpRcxHFawFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
مشاركة حشود غفيرة إمتثالاً لتوجيهات السيد عبدالملك الحوثي ودعماً للقضية الفلسطينية والقوات المسلحة اليمنية في مواجهة العدو السعودي بمحافظة صعدة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93075" target="_blank">📅 16:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93074">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooVfLJ91kFaLrtNyIBAs7ZjwMK-3I4g-32DQRxxBii3AMBy0cJiCDHW7FU2IcIGDA3HyU-CrSMrguyPbcmCW_Z_WIxUaWG_shOJo_HFTDixPLtYM-wPXl2xa5HQ7zrJthzmbopSgM-VBhQ5D82STanbP3mFNbOL0W6oe3Q6K2ZUO2PyjgwFMAWfpl5glgcjLdMXuU8VYEnxcNyn51IJMO7fx7OHQ7FWeroxW5s9RvjnVbTybka7YOuALdSPuHGQ6ZfJsd754adHcgmw6ElMkD257IpHIXJDpKAffjWlFKENibQ4gR2Mwwp8cvjMinjw14oDbpgOfCGJNTS8lVSUM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربة تطال سفينة قرب سواحل الإمارات</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93074" target="_blank">📅 16:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93073">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
سيتم السماح للرحلات الإنسانية من وإلى مطار الرياض لجميع الرحلات الحاصلة على تصريح من مركز تنسيق العمليات الإنسانية في العاصمة صنعاء.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93073" target="_blank">📅 16:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93072">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏قوات المرتزقة تعلن مقتل قائد قوات الطوارئ في أمن الضالع قائد اللواء 16 عمالقة خلال المواجهات مع انصار الله</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93072" target="_blank">📅 16:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93071">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0a1a81fbc.mp4?token=mralBpzP7dNr3z0sltYbzDceRTKEmDYn7uObY5XiMWBCAc1UqZJ3lll8JloOrqBVJlwdoW2FZKKO0Qn2ZAC47tnjxXtJlfqizB2RVFKAfoWccHIBwE-Ng3m_esGqjNhPJ40llZlOsRMx1iGGFpWWNwXurmMSnsxYOFWEaKU5l37JYSTGnlatPMiwyTqrYKAqNACFWTsKKL_t-MFHT64vLVOb1PvYolsQrED3O5j-bzsFbVQUOkbliV-ag0FXkTLyFEInqK37MGbHyuxUfiWRj3m9d1OczWL-B8l6jk0AQiTn-Z6b05nbCmWx3MUaD6xR5rhd30nMZazjGFotS9cRGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0a1a81fbc.mp4?token=mralBpzP7dNr3z0sltYbzDceRTKEmDYn7uObY5XiMWBCAc1UqZJ3lll8JloOrqBVJlwdoW2FZKKO0Qn2ZAC47tnjxXtJlfqizB2RVFKAfoWccHIBwE-Ng3m_esGqjNhPJ40llZlOsRMx1iGGFpWWNwXurmMSnsxYOFWEaKU5l37JYSTGnlatPMiwyTqrYKAqNACFWTsKKL_t-MFHT64vLVOb1PvYolsQrED3O5j-bzsFbVQUOkbliV-ag0FXkTLyFEInqK37MGbHyuxUfiWRj3m9d1OczWL-B8l6jk0AQiTn-Z6b05nbCmWx3MUaD6xR5rhd30nMZazjGFotS9cRGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93071" target="_blank">📅 16:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93070">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93070" target="_blank">📅 16:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93069">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
🇾🇪
وزارة الخارجية اليمنية في صنعاء:
بسط السيادة الوطنية على الأراضي اليمنية كافة حق مشروع كفلته الأعراف والقوانين والمواثيق</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/93069" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93068">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ليست مشاهد من فيلم الرسالة او حرب البسوس في الجاهلية.. مشاهد مباشرة الان من محافظة الحسكة السورية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93068" target="_blank">📅 15:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93067">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c462e20.mp4?token=r5NW4wxklxbrPMiEItBNmHcPQ3LTeJXunMvdu0cW2X_P4qls-eRqJhF-SrhmupUFdTvZOT6rdJgEgZNTwTD2YgfwGis9kpUU3G-m5r2z8UH1pRBk7cAqmWHYD6PUSaivU7pH18aRh_LW6lE1hoCszjhD3NNoUOLcXAITyXId3cHbp6yGf4ue9FRQvcIqP4pGpPoGckTqtx-Y25WqsOfWcBHzEaNEHXTdBZkw6xVsBfgxqfcTSY7tV8r6NwiJc0R20MwS8te_wUAeJ1HBCHKDoJDSjMihJq1uGzmFaL7jBwQ18j0h4G6AD-NX3UB4PWq2oKDvmwmWko9DfFutUkx2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c462e20.mp4?token=r5NW4wxklxbrPMiEItBNmHcPQ3LTeJXunMvdu0cW2X_P4qls-eRqJhF-SrhmupUFdTvZOT6rdJgEgZNTwTD2YgfwGis9kpUU3G-m5r2z8UH1pRBk7cAqmWHYD6PUSaivU7pH18aRh_LW6lE1hoCszjhD3NNoUOLcXAITyXId3cHbp6yGf4ue9FRQvcIqP4pGpPoGckTqtx-Y25WqsOfWcBHzEaNEHXTdBZkw6xVsBfgxqfcTSY7tV8r6NwiJc0R20MwS8te_wUAeJ1HBCHKDoJDSjMihJq1uGzmFaL7jBwQ18j0h4G6AD-NX3UB4PWq2oKDvmwmWko9DfFutUkx2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ليست مشاهد من فيلم الرسالة او حرب البسوس في الجاهلية.. مشاهد مباشرة الان من محافظة الحسكة السورية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93067" target="_blank">📅 15:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93066">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وكالة سلامة الطيران الأوروبية:
نوصي بعدم الطيران بأجزاء من المجال الجوي السعودي المحددة ضمن منطقة معلومات الطيران الخاصة بجدة إضافة الى منطقة أخرى في شمال غرب السعودية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/93066" target="_blank">📅 14:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93065">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزير الطاقة الإيطالي:
لن أحضر اجتماع وزراء الطاقة المزمع عقده في الرياض الأسبوع المقبل، وسأشارك عبر الفيديوكونفراس.
الحصار بالحصار</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/93065" target="_blank">📅 14:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93064">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">"يا عاصب الراس وينك"..
مرتزقة السعودية يقومون بتشغيل قصائد داعشية ارهابية خلال اشتباكاتهم مع بواسل القوات المسلحة اليمنية!!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/93064" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93063">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اضطراب في المجال الجوي فوق الرياض</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/93063" target="_blank">📅 13:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93062">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اضطراب في المجال الجوي فوق الرياض</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/93062" target="_blank">📅 13:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93061">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عدوان سعودي على العاصمة صنعاء</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/93061" target="_blank">📅 13:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93060">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇾🇪
🇸🇦
🇵🇰
اليمن يفرض قاعدة الحصار بالحصار..
باكستان تعلق رحلاتها الجوية من وإلى السعودية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/93060" target="_blank">📅 13:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93059">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXCmfHhU4lfpnyGThRCcYj9VK8i8gMqIhti1RO_n_v2zq8v-G5RhBfwplKPlmYy2Fjq-bmUe4EGvXUj-ABaNPL7yI0TgBFp6KBdmTBcc2Zf4Gs0okU_vDb1mfBBN7As7uVpAiMJKWGNQItUKLr4YU6GOim-5ST-7zEqXXn3tZt97QY0EqrpiOYEQFPmthNjt5pslMGld55yiBzAVF2m3upLFHquT09aY5IAqehDCxV9nMKTSMl5s_sBBHRkDaFhV410gF5DR0qMizJAK9AjPOKi27jDbEvQwY10QhS9YBOIh7DnAO3u19YqIxeS3bT7EVO6oWmKt3bPaJeHdKtCOvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
إنفجارات تهز العاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/93059" target="_blank">📅 13:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93058">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇸🇦
إنفجارات تهز العاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/93058" target="_blank">📅 13:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93057">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
السفارة الأمريكية في الأردن:  الأمريكيون الحاليون في الشرق الأوسط يجب أن يكونوا على استعداد للهجرة بسبب البيئة الأمنية المعقدة. يجب أن يكونوا على دراية بإنقاذات الطيران، وإغلاقات الأراضي الجوية، وتعطلات السفر.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/93057" target="_blank">📅 12:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93056">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
السفارة الأمريكية في الأردن:
الأمريكيون الحاليون في الشرق الأوسط يجب أن يكونوا على استعداد للهجرة بسبب البيئة الأمنية المعقدة. يجب أن يكونوا على دراية بإنقاذات الطيران، وإغلاقات الأراضي الجوية، وتعطلات السفر.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/93056" target="_blank">📅 12:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93055">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر عسكري يمني:
انكسار هجوم لتحشيدات العدو السعودي جنوبي باب المندب قادمة من لحج وسقوط عشرات القتلى والجرحى وإحراق وتعطيل عدد من الآليات.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/93055" target="_blank">📅 12:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93054">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36234c6463.mp4?token=RwOTNyEJkfifpRgk3VvoWhMhUzIvpbJH3gHA5_K3g9bDwIskKaYbtiMArJIjqhLa6fTJT3jwUFbXXVJ5z2WzFKcDcdn5uDWWgIfA2T3qukKyq3IpOvX4rh05EWG2uBtozWQEinHt02RBUN1k-AsksYQGces5iq61KO3kcrWTt1J9phrGKAYrmbMgWB9CTAgGRxtexvAA1Hg2jgZt6y2JvrRdmBTjKTq_u1nB1qFxF-5NtDKBcSfD7NUPJqdeGsguqfAWXRySwG_UhvFu8G8RRjjX1gmirqkGi8OeRyHwwZwAZ0Oyll8EPv_aNJe7_-oQ32CuBZnPYaBwhdtHrxmLvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36234c6463.mp4?token=RwOTNyEJkfifpRgk3VvoWhMhUzIvpbJH3gHA5_K3g9bDwIskKaYbtiMArJIjqhLa6fTJT3jwUFbXXVJ5z2WzFKcDcdn5uDWWgIfA2T3qukKyq3IpOvX4rh05EWG2uBtozWQEinHt02RBUN1k-AsksYQGces5iq61KO3kcrWTt1J9phrGKAYrmbMgWB9CTAgGRxtexvAA1Hg2jgZt6y2JvrRdmBTjKTq_u1nB1qFxF-5NtDKBcSfD7NUPJqdeGsguqfAWXRySwG_UhvFu8G8RRjjX1gmirqkGi8OeRyHwwZwAZ0Oyll8EPv_aNJe7_-oQ32CuBZnPYaBwhdtHrxmLvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
منح جائزة نوبل للسلام لعام 2026 إلى "نافي بيلاي" مفوضة الأمم المتحدة لحقوق الإنسان.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/93054" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93053">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a4d2a50f.mp4?token=WFVWwseTsxjwoQt2dEktvrG0_I3sbgv2bs5a7a_i5pzwMl0js6BvuBSzZNgAMkHGPui2Ko2fJt7X_psSNPcZ4JTRnS12iRw4r4OodWyLDRUxNnTatred7LptZ6tn2P-vB2ehvq1yioRyaDTfFddHDk9z0AA0RKTyTDJfsFIDCD99mpsHYW9BMHjTl6o-DLBSzTAVn7Uy9_nx2mU017VFH68QSxnNLb5hbsrvUl4wWc5OMKwSSWgigib178HuU-lhwpKzphmnQ-xZPIHLT79iXj_qHw6VMYFImPqRl5PR4qJlzrSNlrfJt2OFmf9XTztSeg_2vdTm8VnlrJvZsfQb3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a4d2a50f.mp4?token=WFVWwseTsxjwoQt2dEktvrG0_I3sbgv2bs5a7a_i5pzwMl0js6BvuBSzZNgAMkHGPui2Ko2fJt7X_psSNPcZ4JTRnS12iRw4r4OodWyLDRUxNnTatred7LptZ6tn2P-vB2ehvq1yioRyaDTfFddHDk9z0AA0RKTyTDJfsFIDCD99mpsHYW9BMHjTl6o-DLBSzTAVn7Uy9_nx2mU017VFH68QSxnNLb5hbsrvUl4wWc5OMKwSSWgigib178HuU-lhwpKzphmnQ-xZPIHLT79iXj_qHw6VMYFImPqRl5PR4qJlzrSNlrfJt2OFmf9XTztSeg_2vdTm8VnlrJvZsfQb3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
منح جائزة نوبل للسلام لعام 2026 إلى "نافي بيلاي" مفوضة الأمم المتحدة لحقوق الإنسان.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/93053" target="_blank">📅 12:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93052">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
‏
مسؤول عسكري أميركي:
القوات الأميركية تلقّت أوامر بالاستنفار يوم الأحد الماضي.
‏تقديم اقتراحات لترمب لضرب قدرات إيران العسكرية على طول الساحل بعمق 50 إلى 80 كلم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/93052" target="_blank">📅 12:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93050">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇾🇪
مشاركة حشود غفيرة إمتثالاً لتوجيهات السيد عبدالملك الحوثي ودعماً للقضية الفلسطينية والقوات المسلحة اليمنية في مواجهة العدو السعودي بمحافظة صعدة.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/93050" target="_blank">📅 11:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93049">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇸🇦
هيئة الطيران السعودي:
تعرض مطار الملك خالد الدولي لهجومين في يوم الخميس، أدى إلى مقتل 3 سعوديين وإصابة عدد من المواطنين والمقيمين من جنسيات مختلفة تراوحت إصاباتهم من الطفيفة إلى البليغة. الهجوم الأول طال مرافق المطار، فيما استهدف الهجوم الثاني طائرة تابعة للخطوط السعودية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/93049" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93048">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
رويترز:
ساعدت الحرب، التي بدأت في فبراير عندما شنت الولايات المتحدة وإسرائيل ضربات على إيران، في خفض معدلات الموافقة المحلية لترامب إلى الانخفاض وتثقل كاهل زملائه الجمهوريين وهم يسعون إلى الحفاظ على أغلبيتهم التشريعية الضيقة في انتخابات نوفمبر.
حوالي 60٪ من الأمريكيين - بما في ذلك واحد من كل أربعة جمهوريين - لا يوافقون على كيفية تعامل ترامب مع الوضع في إيران. دفع الصراع أسعار البنزين إلى الارتفاع بشكل حاد في وقت يقول فيه الناخبون إن قلقهم الرئيسي هو تكلفة المعيشة.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/93048" target="_blank">📅 10:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93047">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
البنتاغون : سيتم بث إعدام مطلق النار في فورت هود رمياً بالرصاص في الولايات المتحدة على الهواء مباشرة</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/93047" target="_blank">📅 00:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93046">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a053f827f4.mp4?token=sMubiSkvHnOO4V5CPH39Hnv0VoHRDei05skqcadMEkXvO0NEf3tEIbM9XTZdfAJUECFmplAQMBPunNYRUXiLvN4xkTNeCb-aG2hD8blPfDap226eeAwLo2xug0bJftc6uyY_DUx1eCyoFjBtdFlVobmJq89XSECrmV-mSElgQZhswlZS2X7B3vqz4QAUoEeUohUI8pKaBNqh4evO3Ivkk4weaAFglOZv2lWsjkPBCpNddr3x5XUfTQj3jLE9iZPO8PtgY5LkaxWQXIzBUHBCmniaYhY0AbBe1a2ZtZnpGYn-mETeTj5zxHSRv9S28s7MYfdjWAoicoic4BH4Ld9i6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a053f827f4.mp4?token=sMubiSkvHnOO4V5CPH39Hnv0VoHRDei05skqcadMEkXvO0NEf3tEIbM9XTZdfAJUECFmplAQMBPunNYRUXiLvN4xkTNeCb-aG2hD8blPfDap226eeAwLo2xug0bJftc6uyY_DUx1eCyoFjBtdFlVobmJq89XSECrmV-mSElgQZhswlZS2X7B3vqz4QAUoEeUohUI8pKaBNqh4evO3Ivkk4weaAFglOZv2lWsjkPBCpNddr3x5XUfTQj3jLE9iZPO8PtgY5LkaxWQXIzBUHBCmniaYhY0AbBe1a2ZtZnpGYn-mETeTj5zxHSRv9S28s7MYfdjWAoicoic4BH4Ld9i6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا... لانطلاق الدفاعات الجوية السعودية من وسط مطار الملك خالد الدولي بعد استهدافه بصواريخ اليمنية.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/93046" target="_blank">📅 00:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93045">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b786078ca8.mp4?token=AW3WjuFPRN-cuh60WqleXzPzEMowavBeBQr8PHsn2RMO3GsP6AYEqb69d6gcaDBar2fjGbC4b1fg9kTyp3-6P6EfzKNy4BiA_rKkCdJrE8o4DPV3QtKqvDQqGnic00p6ymKnajBatfDPLYw_nZWQ4QTwZRY4b_Bp01nehlO__ceBsVnclLvZlnJpjFxDxDXbyV_F_Iv24l8hYGPnyWdd8mXulEwKLnvKjfAyp4GsZxwV9OKfORbT5SHQWnV43idvWgNBmRmOWKhqdB6tcDWez65er2OdBCG1jfr6Fe2Tnv5cz0EKWsqQedyas5lWQqGTORAfKfY6naalmww3OpsA5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b786078ca8.mp4?token=AW3WjuFPRN-cuh60WqleXzPzEMowavBeBQr8PHsn2RMO3GsP6AYEqb69d6gcaDBar2fjGbC4b1fg9kTyp3-6P6EfzKNy4BiA_rKkCdJrE8o4DPV3QtKqvDQqGnic00p6ymKnajBatfDPLYw_nZWQ4QTwZRY4b_Bp01nehlO__ceBsVnclLvZlnJpjFxDxDXbyV_F_Iv24l8hYGPnyWdd8mXulEwKLnvKjfAyp4GsZxwV9OKfORbT5SHQWnV43idvWgNBmRmOWKhqdB6tcDWez65er2OdBCG1jfr6Fe2Tnv5cz0EKWsqQedyas5lWQqGTORAfKfY6naalmww3OpsA5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة الهجوم اليمني على مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/93045" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93044">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي
: وزارة الدفاع الأمريكية تضع خططًا جديدة لضربة محتملة ضد إيران في الوقت الذي يتردد فيه ترامب.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/93044" target="_blank">📅 00:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93043">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇫🇷
🇸🇦
رئيس الأركان الفرنسي:
لا نزال ندرس مع السعودية خيارات تتضمن وسائل عسكرية للمساعدة بحماية ميناء ينبع النفطي.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/93043" target="_blank">📅 00:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93042">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/93042" target="_blank">📅 00:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93041">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVTbqyLHMCvW3VEZTjdfHylfcOiIWD2BAucxhDa01h8dhhOKLCmm5jjMsBC1U65Kj1ciKh8097NMPc0a8Sx9lyHqP0T8Ch9e51Mn9wKGuYF9b-K5wvUA8uvWCj1f_gxAR2_kE1hVvNg7RfIgGNRI2ZskbmNy2k-KEtu--et5FLP4GaSKSKiGT7t35WQuOTN4GzmEpZeT8AIO9tZCnLCVLkF-k-bm8AOmiwadqE-oigvUan2UE92ngMgkwuKmC0gtIa123_xskWQtLiHG0TZ9cK7a102pQB14uod7QW6Mdu-ZmonS5ga8yrkndGNT6v0HE-kdj0oXf6vm_-SCaQamhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇺🇸
🇮🇱
🇸🇦
🔻
أصدرت السفارة الأمريكية في القدس تنبيهاً أمنياً تحث فيه الأمريكيين في جميع أنحاء الشرق الأوسط على توخي الحذر الشديد، محذرةً من احتمال حدوث اضطرابات في الرحلات الجوية وتصاعد سريع في الأعمال العدائية بين السعودية " والحوثيين " ..</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/93041" target="_blank">📅 23:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93040">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovDkiviSyN9X2t65dzCZrO06YM-phmV5NKtH2FN1X9gSgfeQA5TdNAsYBRznC0pbquluux17RPhIo49ClySyrdvnKUKrl_ZcdCSO08T0Y1dBjpZpSAfjopcvMZ2lIrSw9cdjt0FngJ4cKkbpe4FxK-eEtbfm76qXDfpvM705EvHXdwurONuV2mhiha94RLmxCkQNAjbzJfm63m3MM7Tev04E_KGLnVNfISI2d0YX16L1-PTZR3GNVuT_EuqX1CuUswYQLxWNKcgNAYWH7tEsvBT7U_0sj7jc6FQHYtgjvFiwprAaxHbQPMd0n-MHQOz1zKQ0A6GnUQlHOxndPRVhDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
متداول
وثيقة تتضمن شمول رئيس هيئة الاستثمار العراقي بقيد جنائي ! الأمر الذي يطرح تسأل عن كيفية الموافقة عليه بمنصبه الحالي !</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/93040" target="_blank">📅 23:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93039">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw_H6bWFEI59arn-kZQ2akG7VqIHdxO4Zb03wKCy2Aq9ymc02zB9iQb7R4NyKVa_4NPbJT9Fj5QypX6wVJQuACQ0XKg2h0SfW7pGh7G_tddHz3IF8yVFMgcoX78gvUvLxNVKr-8uNIpO2SqVCHGtwnnWd_JCNUq8o8Jxl4svl0K9ZCg8hnPavKnxb-0BbfS_CeDjq-3XZNg3qR_6qRHFV0aqj3d6va3g6yTS8WCVSOrzSmz8Q6cSU6GYYiDW3mUMLc5u4crYrJnVmag-GguHFpGGIZpUeqyjLa-xvauMVJe-ZtlaSRNXVL-EUaO7H2P-ElflAQA5ArbfiuaRlBDQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصوات انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/93039" target="_blank">📅 23:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93038">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اصوات انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/93038" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93037">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfBHmjXX6cPwOLTss7_Tk0XzhS1Dc0s2QX44LKIvYXTqsqnZU3ywISBMqlB6RlHyt2wf4uCVTAnhgyY65AurLaD5NkVUyTQPMXm8TAnb_23oSqEnuc2GqRxm8i4AXXM5OIW1feFnWoCNUkwvQSlITvWBlj2VBavoASxmn4fEJuRFaUfs5jGT10b391TbUK0ERB3bGtwZTP8ZeQgTXZFTMrAm9Hoj3AU6jN70LwJWipyG7nA8lDKyIX_ESmEE5jW63968kELRMum5zrzrbIgyczsKZgj1t96gT852-J59dbQFiIuWkbXgCP5vikKSGz4QeWEjG53V_npSf2zt1J-ZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
تحذير أمني جديد من السفارة الأمريكية في بغداد للمواطنين الأمريكيين في العراق</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/93037" target="_blank">📅 23:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93036">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlE1e7Og56c2En6ETw6V0hxqncffyR8gd_yEVI_sngM7wYYesJMkaAEZFV3amC63qiajOXxBdZmeLErjzg_AMoXwul1UWrXgxNytBtsH4FzqtHjJEqyfnrX1KMotUuTl3OpBLo9bhiVG8tqL0i4da-cDuVXNo9awQiM2y0U0DWhshJveuJJnGrS8BgIPPKb40CWJA9zuRL_D9I9aRKxlZGy40WMHKd9KoKCLNEv3WGKMZOYKBoTZ1Pghv4Rnmh7XyyREsBiempnd2JdzMlErrL-ScpxYcZljanaLsSueSDkSFpDVnh7rLoJI0rd6wW7MNl0hFNQabUcJCXrd5p_ylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اندلاع نزاع عشائري في محافظة ميسان جنوبي العراق مقتل طفل واحد كحصيلة اولية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/93036" target="_blank">📅 23:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93035">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
🇮🇱
السفارة الأمريكية في القدس تحذر المواطنين الأمريكيين الموجودين في إسرائيل:
يجب على المواطنين الأمريكيين الاستعداد لاحتمالية إلغاء الرحلات الجوية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/93035" target="_blank">📅 23:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93034">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa770901e6.mp4?token=RkicVebszA-EO3vpXfzNsi6n9M2piDPfwYjQIKN6kS00dPtVJBRpTdIiema4GqBayibR7iDSCu7BzJKBE9Wt-4dzYpsVvqLD2NuhVG3SvBO5oDwsLEH2muDluSFjSYdmr4pxMdZ1hOSBEuhpiNDrmkW5oI6lyX7CYgvNUsieSwEiESjD7uc0mnGuU_L0yKY74ewUtvUnFcBEVfuedpZtTgZbz7GLWyP5fKyuuPPcc6AgTpDsNwcxan5Uiqm0rHaAM2_FPGYentFPANUEHpPxnMboh6z3_E3kSmzwwlavUsGjLI4LvYt-qo6sWN8j-7RgERmV7pNLbf0FrPchkpCTEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa770901e6.mp4?token=RkicVebszA-EO3vpXfzNsi6n9M2piDPfwYjQIKN6kS00dPtVJBRpTdIiema4GqBayibR7iDSCu7BzJKBE9Wt-4dzYpsVvqLD2NuhVG3SvBO5oDwsLEH2muDluSFjSYdmr4pxMdZ1hOSBEuhpiNDrmkW5oI6lyX7CYgvNUsieSwEiESjD7uc0mnGuU_L0yKY74ewUtvUnFcBEVfuedpZtTgZbz7GLWyP5fKyuuPPcc6AgTpDsNwcxan5Uiqm0rHaAM2_FPGYentFPANUEHpPxnMboh6z3_E3kSmzwwlavUsGjLI4LvYt-qo6sWN8j-7RgERmV7pNLbf0FrPchkpCTEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توثيق قريب ومباشر للحظة استهداف احد مقرات الاحزاب المعارضة الايرانية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/93034" target="_blank">📅 23:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93032">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c0ef9968e.mp4?token=jpP3hYT_ojLe7Ue1CWdebpBA92eE4W3O60bZJqHTMBL1f6IpPaCHfpxvyItdkCK24ELOhhyOK8GAKBEsOb-FCCTdjvuWUpMb0D02QWM5XrHAJTYgfmqZ8ekWGinv60NihK1MtmJpIIe8rL6zUsRjTJv3VE97IIXGTp8tGhc8KsfOyOqigk9smGMTrbDZ2jZ1ME-yFaiMvbzkU1e4flgkp6juJ1TLDVvjQiBRpoJaJqRNwcnHR1mYbZBNPiA9eBwCkV1ttTtZ4zLGG4-gBzKOfV-sTFOYJjCGcBXjMMr-Si2WbbIN_LI04feXB5lxsRkj5OuNZOL9gDn-WE4L3Xv9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c0ef9968e.mp4?token=jpP3hYT_ojLe7Ue1CWdebpBA92eE4W3O60bZJqHTMBL1f6IpPaCHfpxvyItdkCK24ELOhhyOK8GAKBEsOb-FCCTdjvuWUpMb0D02QWM5XrHAJTYgfmqZ8ekWGinv60NihK1MtmJpIIe8rL6zUsRjTJv3VE97IIXGTp8tGhc8KsfOyOqigk9smGMTrbDZ2jZ1ME-yFaiMvbzkU1e4flgkp6juJ1TLDVvjQiBRpoJaJqRNwcnHR1mYbZBNPiA9eBwCkV1ttTtZ4zLGG4-gBzKOfV-sTFOYJjCGcBXjMMr-Si2WbbIN_LI04feXB5lxsRkj5OuNZOL9gDn-WE4L3Xv9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من مقرات الاحزاب المعارضة في اربيل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93032" target="_blank">📅 23:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93031">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039ff7ebef.mp4?token=p-it8kAXdkD9bHgM55l4EJ7XqpItncvC3QzMCWHJN8wPmtBDqfmYHKkhoVHmEDcuGolmk4crdDfYk695tc5wj4ExvzfUPPe7tPsMQYLr_5JaoaimzqwrjiH2WDevsvyqhO-DMC3Bcb8AeVhLzBH_JVpRUj1aEwFoQtRXAHGWei69pWWbRAwxtvtGFEr3p-K50ZHhiWEajsqWRGIoywbAl7Wptn6coWWvQEbMkxvlmIC584cVsFS9Szi09-4vwXXEWlJ0mvIsHLiCB99lxCxNMki9T90ZU_nKfkRCamloQu5j_Dz6EWY2LfBqHwJ9Xy1_xp1on9L09D93svFggHq-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039ff7ebef.mp4?token=p-it8kAXdkD9bHgM55l4EJ7XqpItncvC3QzMCWHJN8wPmtBDqfmYHKkhoVHmEDcuGolmk4crdDfYk695tc5wj4ExvzfUPPe7tPsMQYLr_5JaoaimzqwrjiH2WDevsvyqhO-DMC3Bcb8AeVhLzBH_JVpRUj1aEwFoQtRXAHGWei69pWWbRAwxtvtGFEr3p-K50ZHhiWEajsqWRGIoywbAl7Wptn6coWWvQEbMkxvlmIC584cVsFS9Szi09-4vwXXEWlJ0mvIsHLiCB99lxCxNMki9T90ZU_nKfkRCamloQu5j_Dz6EWY2LfBqHwJ9Xy1_xp1on9L09D93svFggHq-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد قريبة للحظات الاولى لسقوط المباشر على احد مقرات الاحزاب الايرانية المعارضة في اربيل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/93031" target="_blank">📅 23:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93030">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace48d1baf.mp4?token=aaKVMw8s_IMKZpGH-PQ7Xc7IkzieCmiQECZLqhKJWS3BovfsIoB0D3rWCTjK3LVSQsElzHcqqN56jHQ-diA_V8ph_8OP6R3zR_s1HLPzyBIrArfzQJGn7H_ESMrpkaQUDgKS42bg4GBp5aI961jtI2VT5qbLwXTbxuhCF7IBefOcA8_6KftnjAoCPrLXG3_01M4dr6uy9SDL56cXFdvOL7JGA675eCJcPmSDKCI4tIXCANE5XQLgJEUo3Bd3zunPJdloF9-khXFsoLLIjmITYEIHcIdyXDVE2AD7-E3Nr4VF6gxzY0Uq9SlG4HuI4_RIcgXloJd-fuE2OWiParNc-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace48d1baf.mp4?token=aaKVMw8s_IMKZpGH-PQ7Xc7IkzieCmiQECZLqhKJWS3BovfsIoB0D3rWCTjK3LVSQsElzHcqqN56jHQ-diA_V8ph_8OP6R3zR_s1HLPzyBIrArfzQJGn7H_ESMrpkaQUDgKS42bg4GBp5aI961jtI2VT5qbLwXTbxuhCF7IBefOcA8_6KftnjAoCPrLXG3_01M4dr6uy9SDL56cXFdvOL7JGA675eCJcPmSDKCI4tIXCANE5XQLgJEUo3Bd3zunPJdloF9-khXFsoLLIjmITYEIHcIdyXDVE2AD7-E3Nr4VF6gxzY0Uq9SlG4HuI4_RIcgXloJd-fuE2OWiParNc-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من محاولات اسقاط الطارئات المسيرة المتجهة الى مقرات الاحزاب الايرانية في محافظة اربيل قبل ان تسقط على اهدافها بشكل مباشر.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93030" target="_blank">📅 23:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93029">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bf39202dd.mp4?token=bqmgUgz73aj-t272y-DkhFTGi7br99D9W2caI-CZcAUz2i8XuxFleb2XsGjt0oXy8KOInxB-rwX1bT1huHqNp5dC0G9VXmQkorz-Eq1DoPhyNJQmmW8RqzaSMl-s3Vdeen-esBN0cb9G8oey60w4A7gcCaY56P6YmYLljCrgAnu6-LlJGqZFLIVkGct-5TiE14lt77zzQb2VtWXQDeyPiLWW04_rAlWnMM08Gl1m_jPSilZbzgPDydjTfmUQNW2IIhySpRiR00wtazXTT04JEe0NOGDnb5PPwv3wMsykB5SabZ1GGmhQFYTYkEwv_Rw_5CH9BPi_FqZkd0mwrCm9AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bf39202dd.mp4?token=bqmgUgz73aj-t272y-DkhFTGi7br99D9W2caI-CZcAUz2i8XuxFleb2XsGjt0oXy8KOInxB-rwX1bT1huHqNp5dC0G9VXmQkorz-Eq1DoPhyNJQmmW8RqzaSMl-s3Vdeen-esBN0cb9G8oey60w4A7gcCaY56P6YmYLljCrgAnu6-LlJGqZFLIVkGct-5TiE14lt77zzQb2VtWXQDeyPiLWW04_rAlWnMM08Gl1m_jPSilZbzgPDydjTfmUQNW2IIhySpRiR00wtazXTT04JEe0NOGDnb5PPwv3wMsykB5SabZ1GGmhQFYTYkEwv_Rw_5CH9BPi_FqZkd0mwrCm9AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة تطال مقرات المعارضة في اربيل.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93029" target="_blank">📅 23:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93028">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db89739427.mp4?token=gQSzWFcI7joPe56Lq6GvwldkR827ekA6fi6_7dnetXEhEonH2YbZkAIVDaUdaON4qvACTH6celsccFLf_ijyocRgri2i2QDkF2aCzqdh0Wv33Il8rtdWYs8yV00OK1BRXqU9vpMwT904YAp4xxsELOkfmPutYyDuQF2cmLXEN7wtdb670FO8UuUzEc2MjtwZrHZwTJkrJtsG0ZyTNc-xqpWSd8W8lv5fXGXH70Pa_isXTE5BpHTdWe7O31wLK6djvgJuoolZef-k968Ak2irNusI6S1LMEI2FvTIhucpusWD8wmmVOsNq-7Esvewe_dssZ43iwMcIzjIcUhRY1CwCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db89739427.mp4?token=gQSzWFcI7joPe56Lq6GvwldkR827ekA6fi6_7dnetXEhEonH2YbZkAIVDaUdaON4qvACTH6celsccFLf_ijyocRgri2i2QDkF2aCzqdh0Wv33Il8rtdWYs8yV00OK1BRXqU9vpMwT904YAp4xxsELOkfmPutYyDuQF2cmLXEN7wtdb670FO8UuUzEc2MjtwZrHZwTJkrJtsG0ZyTNc-xqpWSd8W8lv5fXGXH70Pa_isXTE5BpHTdWe7O31wLK6djvgJuoolZef-k968Ak2irNusI6S1LMEI2FvTIhucpusWD8wmmVOsNq-7Esvewe_dssZ43iwMcIzjIcUhRY1CwCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد اخرى للحظات الاستهداف الت طالت مقرات الاحزاب الايراني المعارضة في اربيل.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93028" target="_blank">📅 23:00 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
