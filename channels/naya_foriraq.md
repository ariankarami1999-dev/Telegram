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
<img src="https://cdn4.telesco.pe/file/dEjn1k701NdgYIDlJz2OyyQvSGPgMWeZR00S63XLAgORKvd-i-CEfKtcQ7yDr1hMn4sKFSd1BkIHnEZlKOOpLzKEGsQgFg5rBEshdzLbqrJYoj_IDls6g-b4Rabac6-vWtw7NIe22OApOl0Au14DwtBG-dU-ok3ov7XCRA0yLPKhrQXkYexgbfZw9Kb1Sm_APxegBF6zJ-_hXRaqQi4h9sTsnrin7Cuw9AHkfzRtB71hd54p5qFKywktF5Vue5Liy4_HLnpdak7RbI7-kQA7mjq0XP9Aqh2xru5nTSHnvEMiEsqUItvN8MkQzzhH8bYYOg-jnXdJ9IS39rCWwmqJ8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 269K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 06:08:05</div>
<hr>

<div class="tg-post" id="msg-88745">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي:
وجهنا بتقليص قطع الانترنت لتكون من 6:30 الى 7:05.</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/naya_foriraq/88745" target="_blank">📅 02:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88744">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d252835d1a.mp4?token=ZXRdydqfV9cYwIRkd1kI7_JUmlBc70At0oTX0nNQDx_tMIgrHWgKm47ObJDDfsfDnsQjxKCfyf53enauDY5XVzLleOK7-4ehZo0HGjeY4mLiVmveMhd-_rY3_JV9opxFO7CCa6WoHFcRgWQgo2SJhh2iZE-MVD6J-oxeKd78R_M0h7fPxdBQStEzz7fRQoiBnuvLxY--eMzD7hYxKEKvmdhgPFMvnJRatRrXbswSTMP2cvD910sQqwDeN8KpLTqUShIJ8raKcVbFw0FCFA04TtdoGOxO2qBcAFZSrWHnH0S85bgTPzG_AlhsYSzzENtOuEIBTKMO82ei8Qwx5zcZNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d252835d1a.mp4?token=ZXRdydqfV9cYwIRkd1kI7_JUmlBc70At0oTX0nNQDx_tMIgrHWgKm47ObJDDfsfDnsQjxKCfyf53enauDY5XVzLleOK7-4ehZo0HGjeY4mLiVmveMhd-_rY3_JV9opxFO7CCa6WoHFcRgWQgo2SJhh2iZE-MVD6J-oxeKd78R_M0h7fPxdBQStEzz7fRQoiBnuvLxY--eMzD7hYxKEKvmdhgPFMvnJRatRrXbswSTMP2cvD910sQqwDeN8KpLTqUShIJ8raKcVbFw0FCFA04TtdoGOxO2qBcAFZSrWHnH0S85bgTPzG_AlhsYSzzENtOuEIBTKMO82ei8Qwx5zcZNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هطول امطار في محافظة النجف الاشرف العراقية على الرغم من وصول درجة الحرارة الى نصف درجة الغليان.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/88744" target="_blank">📅 01:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇶
العامري
-رئيس الوزراء من المستحيل جدا أن يتخذ قرار الصدام مع المقاومة
-الإخوة في الإطار التنسيقي لهم الإدراك الكامل لخطورة الصدام ولهم الخبرة والحنكة والقدرة في إدارة الأزمات</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88743" target="_blank">📅 00:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88742">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇦
صفارات إنذار في كييف و8 مقاطعات أخرى.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88742" target="_blank">📅 00:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
المستشار الأمني لرئيس الوزراء العراقي:
وجود قوات حزب العمال الكردستاني بالأراضي العراقية غير شرعي ونعمل مع الجانب التركي لحل المشكلة، سلاح البيشرمكة ضمن الدستور وسحب السلاح هو لكل ما هو خارج عن الدستور.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88741" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88740">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الخزانة الأمريكية تفرض قيوداً مالية صارمة على فروع بنك مصر (ثاني أكبر بنك حكومي مصري) في الإمارات نتيجة التعامل مع إيران.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88740" target="_blank">📅 21:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8d72455a.mp4?token=TmwPd6SYGbcm4EKCLev1XtDGi0T9AG1HpSTXwMz3_dzA7di0lryqlVkcufale9wC5TlSfCJ4jHcBrHnI7o3DTCjdgIWilz-byKJEd5orrixKftXRPXsODSMReYA3Zrlvl_HH2-GNReFE8iCFA9Rry_9-zsHcCGoHgjClDvQG1YnkeSCPF0Pl21A8-M4MfZ3yNcA21uMCbWC0eeRwYFPyNEjykh4y2mlGsTj9jCGMS9s5uCmp8kZ0TKJWndXOjle4uwr2ePDTuANCIMPmQvY38I2-K4S82TAwZeKZWG_MnFEX_C_dsOSwHJ5XE3dlm7FbOl7QU8z3e3pnPiHYjETGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8d72455a.mp4?token=TmwPd6SYGbcm4EKCLev1XtDGi0T9AG1HpSTXwMz3_dzA7di0lryqlVkcufale9wC5TlSfCJ4jHcBrHnI7o3DTCjdgIWilz-byKJEd5orrixKftXRPXsODSMReYA3Zrlvl_HH2-GNReFE8iCFA9Rry_9-zsHcCGoHgjClDvQG1YnkeSCPF0Pl21A8-M4MfZ3yNcA21uMCbWC0eeRwYFPyNEjykh4y2mlGsTj9jCGMS9s5uCmp8kZ0TKJWndXOjle4uwr2ePDTuANCIMPmQvY38I2-K4S82TAwZeKZWG_MnFEX_C_dsOSwHJ5XE3dlm7FbOl7QU8z3e3pnPiHYjETGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف ينشر.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88739" target="_blank">📅 19:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88738">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف ينشر.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88738" target="_blank">📅 19:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88737">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف ينشر.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88737" target="_blank">📅 19:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88736">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj_LxFFCe_WLc_immr3V2vWqPRESHVqKwih8z_KR8NJAnvt1sk_wb5Xaf-TBzubQy430ByW-hQSiAGA13HtXxFYKrcJO7eK5k6cZTbNTmR684Ow9wr7Evi6L1H0Ie5DpAlaRfGKjYQtcImVyrpcSaPsQue7UCwFUucWuv0v_GX8Mn57gOj2_b-E4PaRSN-jLNdfmrYhms-A6tCI5Gc-Ej3mpUSo-qvrJlrLFCXEUxIe53J8ZERUhhaBz5fWrKb6uL1YUPWvTU7uafITzb8LSpGNd_82qTG_-rgbnW7cbOfvUnIw8LahZQtgJvPeZRgh8-DW_G4h2UOCz96QqAbV3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف ينشر
.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88736" target="_blank">📅 19:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88735">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNE4kDWHj_w92x9OC6nD2uFIvT7n74qjo5IJKLzQ9Z67BmZeEsYdaCmubzy9fOsfRPMZCIxIsQsgHcqHk9kBTZ_QQ9HMl5nckQC2q6nkH51D1FNWEdlpIGwz1NO9J0OoPbAVMMJ4F95d4pJzLu3HT_P4cA9WHWGnIWVX-HomjeP-dX4Fus_UpjYzCl4aKuXypNsI98U-o0IBN97iyjUsGKqsT2WuDhfPkoaWO8rBQ9FepxdP_IzdVGu9lyysfrCP2SWgcXStAH8W8FPAXeoyL-D6VrcwvwirDvUlTpasTSiJ0nzKbuzYDEYRbYmGQsKXGkxAwFs2EzTLPqgGsE22Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
رئيس مجلس الشورى
محمد باقر قاليباف
ردا على وزير الخزانة الامريكي
:
كاذب كاذب، بنطاله يحترق.
للحصول على أرباح حقيقية، اطلب من موظفك أن يطلع على تقرير موديز الذي يُظهر تكاليف حرب تتجاوز 130 مليار دولار، واسأل موظفًا آخر عن حجم الخسائر التي تكبدتها شركة جين ستريت في بيع النفط على المكشوف لصالحك في جولة واحدة فقط من العقود الآجلة، والتي تجاوزت 130 مليون دولار.
كاذب كاذب، عوائده مشتعلة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88735" target="_blank">📅 19:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88734">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15c704d61.mp4?token=qfQM-aVXr3ZmZLC6nmuUshayPQb-KPZTorJ6Nx7ABr40qDUNLSDWDib2HmiZbC4tQP2WDtbd8XJh7qTSlwhwiqeoT4oA1AwNcI5YcBRiE9neGB-wCTtaIyygRclzGBkasM4O1o376kQ1mAsmblhsp0miKpxOlM2X5A9ettmUnS2FaqMVmWrAsSZ-lnkOh-KlybQo_pulms1ivM-b9N76q6sBXOYtaqLixeShHn7PYWRIb5Jpxne5WEzAm9sNzqYMpB2M_WVP4CHiizJy7bLHQ9Gpw-lav2jVvworAMI1sf3Xdp2WrWOrB9M1d905cjZ6t9MRMzcF_hyCPsBvtSI3qXNkkn_gDcy-4X998OgPGTNJD_gEdpDxkP3LgOC9p6nBmG_1NMlccM_CNJtPGvXn0KnB0DGoQmX1ES9C1WQWg4l40nhjvKycUEXTPjEowQQsM12xR4GdAHH_FwIbvDArdAZJnJpvbZUPP7cH4HnN8Z38gzTY7ImA_Hb8I5FqzmQFic5BMyR-uaHPdO-087yQ1vlM5Nx1_AgYOYfHLCHdCkk-xBgE1csqudIyvmtAUYPPv5W2KGxBpcA1ezZG_nioI0aTEY5xXWWd1W_Jvpy5HXcjwZvV_dtph33n3krHC4_tA1E2blKwM04d5Szz-oX96R9DR5peBh6hf-biU_KdlGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15c704d61.mp4?token=qfQM-aVXr3ZmZLC6nmuUshayPQb-KPZTorJ6Nx7ABr40qDUNLSDWDib2HmiZbC4tQP2WDtbd8XJh7qTSlwhwiqeoT4oA1AwNcI5YcBRiE9neGB-wCTtaIyygRclzGBkasM4O1o376kQ1mAsmblhsp0miKpxOlM2X5A9ettmUnS2FaqMVmWrAsSZ-lnkOh-KlybQo_pulms1ivM-b9N76q6sBXOYtaqLixeShHn7PYWRIb5Jpxne5WEzAm9sNzqYMpB2M_WVP4CHiizJy7bLHQ9Gpw-lav2jVvworAMI1sf3Xdp2WrWOrB9M1d905cjZ6t9MRMzcF_hyCPsBvtSI3qXNkkn_gDcy-4X998OgPGTNJD_gEdpDxkP3LgOC9p6nBmG_1NMlccM_CNJtPGvXn0KnB0DGoQmX1ES9C1WQWg4l40nhjvKycUEXTPjEowQQsM12xR4GdAHH_FwIbvDArdAZJnJpvbZUPP7cH4HnN8Z38gzTY7ImA_Hb8I5FqzmQFic5BMyR-uaHPdO-087yQ1vlM5Nx1_AgYOYfHLCHdCkk-xBgE1csqudIyvmtAUYPPv5W2KGxBpcA1ezZG_nioI0aTEY5xXWWd1W_Jvpy5HXcjwZvV_dtph33n3krHC4_tA1E2blKwM04d5Szz-oX96R9DR5peBh6hf-biU_KdlGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد تعرض لأول مرة للقائد الجهادي الكبير الشهيد ابو باقر الساعدي "رضوان الله عليه".</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88734" target="_blank">📅 18:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88733">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">#متداول
🇮🇶
فيديو قديم للقاتل محمد الطائي والعميد الشهيد هشام خلال حديث سابق بينهم لازالة التجاوزات في منطقة الدورة ضمن العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88733" target="_blank">📅 17:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88732">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزارة التربية العراقية تغلق 158 مؤسسة تعليمية غير مجازة بالتعاون مع الأمن الوطني</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88732" target="_blank">📅 17:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88730">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxJGkSFyUMfj9RAiOxx1Va_ztStvwoooBZXxirYFF9r75IgryIYx2bWZaxo8Lih7WlM6JJGc1tmMyVOhKrMaD4X0lz7wxpa7rBwn7gWMMlZH82aBtAueSqsWxuc8yWz3g8Thr4QP1eTQVZXQ-0rEug6dDPW5vk2hzcXA9bodupzzsKrrJgFryxQ8vyvHia88_eaJdySUGpi67elwswh-qHslVzVgXmHH37RNPGhxkX_xkrMO34vx3upkLSHj3sbyTJrFz-I-c15fK7Fmp2FNtoo8Q5IqaDeltbulNIkn2GCw4i9nwHd9VSm40gALg_N569044obcPjhnSovbtNB25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IF7jlcTSnJ9_noWz4zl5x48bJB9OjN-xd3gw04iwsfJtK9u9MyhgdY0MeBYTprwbeGLxZwQ_0urT-9r2lu-udEEHV7OVTnIekY-maznGEEY9zUV_KhqQBA7djVjUkLMz6371OafeqrVUWAOla4FEoDdEbLCaPT7Qhn4lSQwzyJexRhuBHecQePzIT62u6ckPKCrXjAl3WRCL5mPUNaNI4mqrKIkRgLsJArw3oKK2gygLHRg3QDZB86A1u1LSc8TCnxi6W89b3vW2Ag-NRbFI3IfCbTppuNCxa3CZPJ4JDrjzAAXSuxdvhzSrrE6rMN9ltFSvNlYJJXuOTxZugooPrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسم الله الرحمن الرحيم
إِنَّ الَّذِينَ قَالُوا رَبُّنَا اللَّهُ ثُمَّ اسْتَقَامُوا فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
بيان الموقف من ملف سلاح المقاومة الاسلامية كتائب سيد الشهداء
ليكون العراق سيد نفسه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88730" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88729">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4172d25c3e.mp4?token=OcCI5B2gx2QEYavcQK4Nq0CnN_A58uRb9N1AMizc5_ehK51KFI8i2ZVcuKeJxq3OAFDzaXTLhHXA06J_jzGAeni3s7rZwUz0_AK6wNnWQ0fwvLVGTtBsBK1XSVX72GrKt6Xv1N2mbrFNUfMj7uV4HwWiXw2QIquRJ3PIT9xlaQ1UWp0s6bUjnIJjT2Gcpwt_8K09r221KknJJCjGqk2nDRWJRR27wnqFoxvFUiqgA5lJQYzKRcNoBfchGIJlhPqQenZHs9Ffz6Lo1f8wswz3zwsAj5FDEJgxF2BEKNo71C6dNQ2IaEukQpoyhf1FsIeV3_g7NS6LN9h9wVvDYri6VSgfUyfgHBgODF8TpgIjMFNkMjWa413wugEHGzgdHcn_yAUJglx38emeZbAyinswLQaYLEeH5dLVJjdr2zzs1hxqM5S9VsB8ME7mD5RVnjTdfdg-l3kOo_HV-kSCoyfkXD2mHMqSVXqdB1E7tjzIUl47K3NUUbWvTgzpbhStBJ9f5sbrl2dWaeSVEq33g3TpiLCnBEHyOQJ_nQFv6NLoqfHse8crYvRr6yctC5cMkcGvyyNU2Ggmp66hkreYXINW0tq_e7Fxb0zqmN6jwDKKtzZTcHdy_UVUo_LvSXXosOCrIPNdjsNL5qaXf8Fa1GfCu6u-avCM3uL1RQ0WSSLmEHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4172d25c3e.mp4?token=OcCI5B2gx2QEYavcQK4Nq0CnN_A58uRb9N1AMizc5_ehK51KFI8i2ZVcuKeJxq3OAFDzaXTLhHXA06J_jzGAeni3s7rZwUz0_AK6wNnWQ0fwvLVGTtBsBK1XSVX72GrKt6Xv1N2mbrFNUfMj7uV4HwWiXw2QIquRJ3PIT9xlaQ1UWp0s6bUjnIJjT2Gcpwt_8K09r221KknJJCjGqk2nDRWJRR27wnqFoxvFUiqgA5lJQYzKRcNoBfchGIJlhPqQenZHs9Ffz6Lo1f8wswz3zwsAj5FDEJgxF2BEKNo71C6dNQ2IaEukQpoyhf1FsIeV3_g7NS6LN9h9wVvDYri6VSgfUyfgHBgODF8TpgIjMFNkMjWa413wugEHGzgdHcn_yAUJglx38emeZbAyinswLQaYLEeH5dLVJjdr2zzs1hxqM5S9VsB8ME7mD5RVnjTdfdg-l3kOo_HV-kSCoyfkXD2mHMqSVXqdB1E7tjzIUl47K3NUUbWvTgzpbhStBJ9f5sbrl2dWaeSVEq33g3TpiLCnBEHyOQJ_nQFv6NLoqfHse8crYvRr6yctC5cMkcGvyyNU2Ggmp66hkreYXINW0tq_e7Fxb0zqmN6jwDKKtzZTcHdy_UVUo_LvSXXosOCrIPNdjsNL5qaXf8Fa1GfCu6u-avCM3uL1RQ0WSSLmEHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هطول امطار في محافظة النجف الاشرف العراقية على الرغم من وصول درجة الحرارة الى نصف درجة الغليان.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88729" target="_blank">📅 16:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88728">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fc68bb52b.mp4?token=BbO0op_eTqKr4t13sNEXOuDkaJkyWiquADvD7MaZBXacTgs0mY6gFDNTRTla6Aebto8sKLEfuGSAtkvpRDC66nwTcnbskb1E_ASQU-jdmD5NQ29pU5PzDRfp2lkbQJbIsPV5CRz2l3wHmYfaGdVVFicZXYt1ewm-1krEZBp0Xg6YQtROn3U7s8SDheaZnREmISNbBid5y3Es-dcW1A8VvqospSbzS_mgOT2_0Cn5AtlqCq_9UKB3H95Jg69SPYD8KIU8Isy8JeF0NxtHsr9P-TYM7UosyRT6iLpy3xt0Boj0POINcZfNdKVUqWsgqPe3_zH06Qz6yPHSyaLC49yXIoN2RxQQrXCyFuH1_NfHttmS3FELfj9W0KqR764hsqyXWedW2pT0BAf4pgPZlL7WCAotDmTNE8NmpUDtYyqUqEX7afJGNF6C3OEw1ddqu_efqXMosJF97R66cTKKe2dHfBiyRdUyh3htw5Une70cV9TVNiOnvHIq7roZ3GyFcd-xBYjAzBUTqkkM4eEVp8BalgU1Z5LwJMY40jEjQJH5PZLfVMhwV-5nv_LjWqoU_KPxAkerzMQaRZG9gSABWkicx5BdWkrFvMf8ULPuwO1XargIyZPz37XoFMNonA5Yjt8K7lVRoRgD2HtjDMaxwaRQ6RAYKfydTUiLLrqT_f_uaPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fc68bb52b.mp4?token=BbO0op_eTqKr4t13sNEXOuDkaJkyWiquADvD7MaZBXacTgs0mY6gFDNTRTla6Aebto8sKLEfuGSAtkvpRDC66nwTcnbskb1E_ASQU-jdmD5NQ29pU5PzDRfp2lkbQJbIsPV5CRz2l3wHmYfaGdVVFicZXYt1ewm-1krEZBp0Xg6YQtROn3U7s8SDheaZnREmISNbBid5y3Es-dcW1A8VvqospSbzS_mgOT2_0Cn5AtlqCq_9UKB3H95Jg69SPYD8KIU8Isy8JeF0NxtHsr9P-TYM7UosyRT6iLpy3xt0Boj0POINcZfNdKVUqWsgqPe3_zH06Qz6yPHSyaLC49yXIoN2RxQQrXCyFuH1_NfHttmS3FELfj9W0KqR764hsqyXWedW2pT0BAf4pgPZlL7WCAotDmTNE8NmpUDtYyqUqEX7afJGNF6C3OEw1ddqu_efqXMosJF97R66cTKKe2dHfBiyRdUyh3htw5Une70cV9TVNiOnvHIq7roZ3GyFcd-xBYjAzBUTqkkM4eEVp8BalgU1Z5LwJMY40jEjQJH5PZLfVMhwV-5nv_LjWqoU_KPxAkerzMQaRZG9gSABWkicx5BdWkrFvMf8ULPuwO1XargIyZPz37XoFMNonA5Yjt8K7lVRoRgD2HtjDMaxwaRQ6RAYKfydTUiLLrqT_f_uaPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق يلتهم محطة وقود بالكامل في محافظة دهوك ضمن اقليم كردستان العراق</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88728" target="_blank">📅 15:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88727">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFlLzOZFghqu9YrkEZJJJqkot2dKgeNg3VRFRZeI_6bxAsQzCpldUVe5_jBfEOF3V_o8Bajjk0cK7Dx0v8ULC6sktUI_e2IQs2nTuhrGvLJfDhk8Kn-mq-69razPd8X7VSJmKL1fyBWEt1gk25e38NAVp4kKeS4SRBnUOQ9PGmn6kL5fUmHtgqsks6tm1EWBcDHKUrx1zUTyScSB6dhY0oEItieEmciMVYH5PvLj7r2Qk9dOUZSjl4ZuxeTyXR8I_qJd2J4A-iXwMktXYlCLZY16cbkTeqL7B3ScpnGViQcO73Sy0AqIZs7lWFcAqD_7cWTHhTYjU0l5tvbmvqolyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
قاتل العميد بحادث الدورة قبض عليه في دار شخص مطلوب وفق المادة 4 إرهاب في نينوى</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88727" target="_blank">📅 15:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88726">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJTEN7RUKUoDMSK8Wj_WNM-V0vCRn_zsIM_wZZ2CDixyjmiADQSrCpEcXehJm4ippOW4g3cMBRBsQVX6tXURsSZ4JVqlw7UbmSXkszIuLjkwZ4tQQbWqaBWNlHaXTdSMeY3o-BszMgxiq-FF54t6xkx8CTcsyD4wmOTY72ubJM5MtWcnhc6Wk79Cwm_VO9lGrtk2yTihxc3I8zGcfbqkYm05E3uVBCbpr_5qGtkE1DclvclivhxO2sWnETDph2B1M1O3ZyA7u-iJ8Dnik0OJGahP6W05f4KJwgT_Nn-c-0N4Tog_KUq2K-bEvENuxaWENcqd6MUPQwW_28saG5PADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
تُظهر معلوماتنا الاستخباراتية جهودًا كبيرة للتلاعب بأسواق الطاقة. تستخدم عناصر من الحكومة الأمريكية وسائل الإعلام الساذجة للتأثير على الأسعار لتحقيق مكاسب شخصية وإبقاء الرئيس غارقًا في حرب خاسرة.
كما تُروج جهات فاعلة متحالفة مع إسرائيل للحرب بتقييمات وردية.
يشعر المستهلكون الأمريكيون بالنتيجة النهائية الحقيقية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88726" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88725">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇳🇪
جنود متمردون في قاعدة نيامي يطلقون النار على مواقع حساسة في عاصمة النيجر والقوات المسلحة تقول انها استعادت السيطرة على اجزاء من العاصمة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88725" target="_blank">📅 14:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88724">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
الاعلام الاميركي: تعتزم إدارة ترامب إنهاء المساعدات العسكرية الأمريكية المقدمة لقوات البيشمركة الكردية في العراق، وذلك عند انتهاء الاتفاقية الحالية في 30 سبتمبر.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88724" target="_blank">📅 14:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88723">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8369cbea.mp4?token=eeh0RrNqfRSTy86KHsBwdf3n6hpzYN63X2Etb4X2Wwa8CIMJGzkQ_U8Z_v20V6kGgO-PnLZRfy-q8WU5zcUFK12gvg5c5NDqwjb8w2vfGYR2Tjp3wFdIRjNdRxqVYWXOieXQXprtJVB0tWp-Uw3Vu8lOgDaoJ-TbZPFu2eGEnqHS23oU-d6gY4Miyk30hlc-2e5014F_vXr_VP0Ene38I9r2QOrYQFx0QYZ9uFKpNbZSKvltwL_YAWT844r52Bi32-F7eELaYYHqVtGS086Wp28vaBvTDIRIGoN_xpyhtHBaw0wbfio1j1gbQ7_Ny37v5WpluQfJqBr3GrwN1TIcug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8369cbea.mp4?token=eeh0RrNqfRSTy86KHsBwdf3n6hpzYN63X2Etb4X2Wwa8CIMJGzkQ_U8Z_v20V6kGgO-PnLZRfy-q8WU5zcUFK12gvg5c5NDqwjb8w2vfGYR2Tjp3wFdIRjNdRxqVYWXOieXQXprtJVB0tWp-Uw3Vu8lOgDaoJ-TbZPFu2eGEnqHS23oU-d6gY4Miyk30hlc-2e5014F_vXr_VP0Ene38I9r2QOrYQFx0QYZ9uFKpNbZSKvltwL_YAWT844r52Bi32-F7eELaYYHqVtGS086Wp28vaBvTDIRIGoN_xpyhtHBaw0wbfio1j1gbQ7_Ny37v5WpluQfJqBr3GrwN1TIcug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق يلتهم محطة وقود بالكامل في محافظة دهوك ضمن اقليم كردستان العراق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88723" target="_blank">📅 14:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88721">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇱
إعلام العدو:
محاولة دهس قرب قاعدة عسكرية للتدريب في الأغوار بالضفة والجيش يغلق الموقع.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88721" target="_blank">📅 13:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88720">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKO39mQgPg5L0ich2ISV-SAY_rg_9N0NtjqJJE40sKBVB_Ogntx1zCqHvAGwMIcJJXPjGtEfauBJSFWnLIyVE4eqlUeSGYRRGj-2UZDjffxrTtSLZaPUv6QotJ6C6Jzeb6-7tuBcbdZs3buDZNHbKCRTrai_3KCiUvErwBUQZYCBJm1JVqDwrzZt5RxPndvbRW3LMUKrjIEbCTtnwo_oV5OhCrXKKAxgf2eqThCAvXZyOkbQERduoBDftgVZ5U_ksvhSM-0B2hFNtQQuoqjTKISfeoJX9Th0SpKzZKrMzm9HLByPm2sExZ0F8y1ayE-aj12WGn_K7DQvtLyHo0i3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
سفينة تابعة للإمارات حاولت عبور مضيق هرمز من الممر الجنوبي لكنها تخفق في ذلك وتقرر العودة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88720" target="_blank">📅 13:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88719">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
الحرس الثوري الايراني: سيطرة كتائب الإسلام على الممر المائي الاستراتيجي لمضيق هرمز حاسمةٌ لا لبس فيها.   في أعقاب التصريحات الكاذبة والمضللة للمسؤولين الأمريكيين بشأن انفتاح مضيق هرمز، أعلنت البحرية التابعة للحرس الثوري الإسلامي ما يلي:   بسم الله الرحمن…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88719" target="_blank">📅 11:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88718">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
اكتشاف وتوقيف شحنة أسلحة وذخائر حربية على حدود محافظة كردستان الإيرانية عند الحدود العراقية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88718" target="_blank">📅 11:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88717">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔻
هزة أرضية بقوة 4.4 ريختر تضرب قضاء كلار بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88717" target="_blank">📅 10:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88716">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca77794.mp4?token=c_Zm-KzvKiEM43ZePUx2LEDM5S88j5EC9wqQ-o5qpnoFc7UvFcfDZ5mVfXDg5ScR6uWutfsGC9R0DH6InthaV2aU3oFzBNUJdinXqjAo25NsRKwS9iJ9ZmlBOVpgJSwG7cFFpnukCJRJN5h8CsoAkV8olpVe3ERW-3EGzOhhK0GoLgjrOzNGge1bwJGrTo6hzg4Vaw1X_UdorK3AerTQB-oj4_MpFpuTLaXcJfkyrev2GCylA6ekWp5gFH7B9L2qhYJpIIK9MA_eqoItQ4f8utN5Kp0jvvisApQcRtkEqq7OKJ8f42iuNyxgxheSbcaDMe5S3FpgaSjr7FLh1o15kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca77794.mp4?token=c_Zm-KzvKiEM43ZePUx2LEDM5S88j5EC9wqQ-o5qpnoFc7UvFcfDZ5mVfXDg5ScR6uWutfsGC9R0DH6InthaV2aU3oFzBNUJdinXqjAo25NsRKwS9iJ9ZmlBOVpgJSwG7cFFpnukCJRJN5h8CsoAkV8olpVe3ERW-3EGzOhhK0GoLgjrOzNGge1bwJGrTo6hzg4Vaw1X_UdorK3AerTQB-oj4_MpFpuTLaXcJfkyrev2GCylA6ekWp5gFH7B9L2qhYJpIIK9MA_eqoItQ4f8utN5Kp0jvvisApQcRtkEqq7OKJ8f42iuNyxgxheSbcaDMe5S3FpgaSjr7FLh1o15kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يصيب هدفاً في العاصمة الأوكرانية كييف وأعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88716" target="_blank">📅 10:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88715">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
🇺🇸
وزارة العدل الأمريكية:
تم رفع الفيزا عن مواطنة عراقية " طيف سامي " كانت تعمل وزيرة حصلت جائرة من إدارة بايدن لدعم المرأة ومحاربة الفساد ؛ حكومة ترامب عازمة بمراجعة ملفات الجوائز الممنوحة في زمن بايدن ، تم وضع الوزيرة ضمن الشخصيات الداعمة للارهاب .</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88715" target="_blank">📅 05:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88714">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
واشنطن سارعت إلى نقل كميات كبيرة من الذخائر للشرق الأوسط لمواجهة إيران، وترامب قرر تعليق الضربات على إيران في يوليو بالتزامن مع تصاعد المخاوف داخل الإدارة بشأن تراجع مخزونات الدفاع الجوي.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88714" target="_blank">📅 04:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88713">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1_XwnsSyhAUwMv5Xu3IIjIkJ1Pot9-hk4xfBONQL31THAb9xypqp-XC29Tax0wJ4KWBaRv6yGycxt9surjH-od8xXTWo9768UypArTh2PvcLL92LyYx7_ZVvORigB-sRYpAnUGe35SC5Ekv6ot9V3L8qR4wP0VGaVAgRWkNgATSLCi0KOQfvq4-0yyDpMRzIK3svcpY-XgsxLSCrX9Cbbwab_s1jnGiS36-wQ_CeySAKapDgfXLA054uWYR8fdggNn0GKCjiAmQ-CV7IfCIz_6A1uIU5btvW1xs-7KZg7j5Ooiz238tSsSBAEDUntP5XkLA4MgzkwKCk1bcXw5qVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترمب
: أبرمنا للتو صفقة نفطية مع فنزويلا.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/88713" target="_blank">📅 02:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
‏الحرس الثوري يطلق عدة صواريخ باتجاه مضيق هرمز.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/88712" target="_blank">📅 00:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88711">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b125233d1.mp4?token=NeiEk8CISbV2eBP-OpNZ_RTmPX2qop9l5YviCEjIbDjGyUBfTPFPmu-C_5h-DE0NTMLGn_s04del5WmE-vtjhOPy_VJZmBSgEstGwty-KefnKXuwc3dhON9joNak8XLPY4CcL1zU4bgqpjzdHNQYgw9eItukgXPQCZVsZDO6MLUxmVgNqoMOPodp1IUFgTIEF5AJJPaDRIIb36IqemQyePhFN2iH8XmrtvT-HJbMLb6akYg23R2d0XSMb1YUJFrobjK2jL-vArjaf7eyufTgsfqtkNjpyLPCqJCB6YR3R5wC88up93WvxRCCfOCNAsRikWK93MblAWs78u4vlRuyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b125233d1.mp4?token=NeiEk8CISbV2eBP-OpNZ_RTmPX2qop9l5YviCEjIbDjGyUBfTPFPmu-C_5h-DE0NTMLGn_s04del5WmE-vtjhOPy_VJZmBSgEstGwty-KefnKXuwc3dhON9joNak8XLPY4CcL1zU4bgqpjzdHNQYgw9eItukgXPQCZVsZDO6MLUxmVgNqoMOPodp1IUFgTIEF5AJJPaDRIIb36IqemQyePhFN2iH8XmrtvT-HJbMLb6akYg23R2d0XSMb1YUJFrobjK2jL-vArjaf7eyufTgsfqtkNjpyLPCqJCB6YR3R5wC88up93WvxRCCfOCNAsRikWK93MblAWs78u4vlRuyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقجي
: في هذه الحرب، أثبتت صواريخنا كفاءتها بشكل جيد وساهمت في الدفاع عن البلاد بشكل فعال.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/88711" target="_blank">📅 00:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88710">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSUQzbw6RbFjmtPoL87JdcEInMHlug-PLUXLDCqka3nDPJXPSR9m4Pr8g3CSOA1qojl0QM4DNSqvY-oJlH2EFuTTu_SMc4QdmngBbnV9uOhc4ZkSJK3wFSqIt7YzJEv09BQrdTK9oFkWwI5Vp_bcdA1JcphEvzxX7HqDbDclNH_p5QUaSGkoDwaRzDncv46NLsUU37IlRXjIiYreRSwC90z2WV247fL8ZRU4_7nhB9mE6A17FpEDYILURka_RM8wRUkheuAvBXgYiff5FTURH3wEMnFNGy7Dc5qn-7kED4rVPOAj_LqhDrlhPm8sNxK2xfEMOZ2hEKV2RWTztsX9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يهاجم صحفية نيويورك تايمز:
اختلقت ماجوت هاجرمان، المراسلة المزيفة من صحيفة نيويورك تايمز الفاشلة، وهي شخصية بغيضة من الداخل والخارج، ولا تعرف عني إلا أقل مما يعرفه معظم المراسلين في هذا المجال (إنها محتالة!)، قصة مفادها أنني في 11 سبتمبر، لن أذهب إلى مركز التجارة العالمي في مدينة نيويورك، لأنهم لن يسمحوا لي بإلقاء خطاب، وسأذهب إلى البنتاغون في واشنطن العاصمة، لأنني متحدث رئيسي. هذه أخبار فاسدة أخرى، لقد زرت نيويورك مرات عديدة على مر السنين، ولم يتحدث أحد قط، إنها "مراسم رسمية!" لم أفكر أبدًا فيما اختلقته ماجوت، وإلى جانب ذلك، أود ألا أتحدث، لأنني أتحدث طوال الوقت، وهذا يوم لتذكر الضحايا وأفراد أسرهم الأعزاء. ماجوت هاجرمان مزيفة، وصحيفة نيويورك تايمز تعرف ذلك! سيتضح كل شيء في الدعوى القضائية المرفوعة ضدهم، ودعوى أخرى ضد المنظمة المانحة لجائزة بوليتزر التي فقدت مصداقيتها، لأن ماغي حصلت عليها عن "تقاريرها" حول "خدعة روسيا، روسيا، روسيا"، والتي تبين أنها عملية احتيال كاملة! إذا أُجبرت على الكشف عن "مصادرها"، ستكتشفون أنها إما غير موجودة، أو أنها لم تذكر ما نشرته. لقد دأبت على الكتابة عني زوراً لسنوات. إنها متطفلة، ويجب إجبارها على تسليم جميع الأموال التي جنتها من خلال تقاريرها الكاذبة عني.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/88710" target="_blank">📅 00:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88709">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
الاعلام الاميركي:
تعتزم إدارة ترامب إنهاء المساعدات العسكرية الأمريكية المقدمة لقوات البيشمركة الكردية في العراق، وذلك عند انتهاء الاتفاقية الحالية في 30 سبتمبر.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88709" target="_blank">📅 00:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88708">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXGNy2ZWrLpUTvPR8FuCYOn3PReHwcjUw79R9r62cZIvXh4EVp5qCpBPNYve_pf7DAA1_akTtRm3b5_SQG-8dYv44eGyhZOECwmPBXOCYbZNQobYJ6hIONmd3YZlGk2wZdxBds0zA6kRkVwmAcaIX_ADO_jZdcfU9F_riNNu0QTjxr9wmvnaHLIqMp4v9KsxTZhdhS02VazD1nxP0wtz_XtpwXAXYgBcb08f03ieg-fLIW_8WI71EgaZf6hOO2aBfOSgtV8RFzexVIEixtIvJJrSvsjhPuhd9JtRS0vfkKckw5nZwML74gpC3Zzz-T5-TOUCL_dNpBfRBLd_1udT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الحرس الثوري الايراني:
سيطرة كتائب الإسلام على الممر المائي الاستراتيجي لمضيق هرمز حاسمةٌ لا لبس فيها.
في أعقاب التصريحات الكاذبة والمضللة للمسؤولين الأمريكيين بشأن انفتاح مضيق هرمز، أعلنت البحرية التابعة للحرس الثوري الإسلامي ما يلي:
بسم الله الرحمن الرحيم
إن تصريحات المسؤولين الأمريكيين بشأن انفتاح مضيق هرمز كذبٌ صريح، ولا تهدف إلا إلى التلاعب بأسعار النفط والتغطية على إخفاقاتهم.
إن سيطرة كتائب الإسلام على هذا الممر المائي الاستراتيجي حاسمةٌ لا لبس فيها، وبكل قوة وسلطة، يُغلق مضيق هرمز أمام جميع السفن التي تنوي المرور دون تنسيق مع الجمهورية الإسلامية الإيرانية، ونؤكد للشعب الإيراني الحبيب الشجاع أن هذا الإجراء سيستمر حتى نهاية شرور الجيش الإرهابي الأمريكي ضد بلدنا الحبيب، والوفاء بالالتزامات المنصوص عليها.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88708" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88707">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
🇨🇳
وزارة العدل الأميركية
تعلن أنها تعرضت مع هيئات من بينها مجلس الشيوخ و"الاحتياطي الفيدرالي" ووكالة "ناسا" لاستهداف  من قراصنة معلومات صينيين</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88707" target="_blank">📅 23:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88706">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔻
إستهداف هدف معادي بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88706" target="_blank">📅 22:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88705">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxUzbvpGBwXX3zsYQVb2UZq447nVkkyuwvYcUXEAtPUfbFTpAJwXILH9wn5Ynns-IshCjeEfbLorIWxn_ycI7PYveO9AhQmlsa_M4bsndcJdtyRDfFaY0mq2kek5zqrK7caRZ_I8vHfG_U2ZtPmE1CN6ZK6UtCn1P-Czm-E-EnpjGwK6fxHLf-Z-tgz9H_qaFnRkuCancTC4sFDmXATMe4sF63uqgGmEOmNH947Ti57YMPMEoCL953Y0YTWPI6v5xjSudollEO_DE-zi45DrBAbacXswfVpuDTDtNMSulmq_-EzCDV_cWQfQWtbj9ar6FUPzLB2jdm_BEcv-3Lg1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:  أعلن بشكل قاطع؛ ارتكاب أي شيء يضر بالوحدة الاجتماعية أمر ممنوع.  أثمن إجراءات حكومتنا التي نفذت رغم قيود ومؤامرات العدو الأمريكي والصهيوني والعقوبات والحصار.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88705" target="_blank">📅 22:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88704">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
الشيخ نعيم قاسم:
التضحيات كانت كبيرة جداً في فلسطين ولبنان وإيران واليمن والعراق.
التضحيات الكبيرة التي قدمت في فلسطين ولبنان وإيران واليمن والعراق أوقفت المشروع الصهيو أميركي الذي يستهدف المنطقة.
نحن باقون في الميدان ولن نقبل بالمشاريع التي يتحدثون عنها.
أنجزنا أننا كسرنا مشروع "إسرائيل" الكبرى ومنعناهم أن يصلوا إلى العاصمة بيروت.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88704" target="_blank">📅 22:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88703">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
على أمريكا رفع الحصار والعقوبات والإفراج عن أموالنا وإجبار إسرائيل على وقف اعتداءاتها على لبنان.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88703" target="_blank">📅 22:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88702">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88702" target="_blank">📅 22:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88701">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88701" target="_blank">📅 22:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88698">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RA-Wo3hJ4swIfXYfWtK_wQnvmINQi7EDeh0-JGa42BNzDwDqPwm63IrntuPwb2_qNkMnSBgLDvjwu3jp6Z-zxsmnyBKKf4tpxPN-WsT0kPKOWSGqR6YGNebp6-MsLStBzykJgcfOiIrcDZZcAMNr6gxP_jvbc7f0n6QGldQsBZGT8mDtAQ4HwkPtspCTyzI3zUIICvxjcvJZI5PvzBJingA8wPdYqLeltKLqK--5vQuQsb_fm5A8ubHqNfzR-0_CKHmR5Nr5zzs2d6kchv4lAqzbIG45R2K25mCpeDre2_DlXHto7upoDcuaXuphJz6cwtQsN3YBJKHk3RY2XkHVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZtETrNy6IfMLqEpU9qYQXQ4RK8peeZwQ5bwqa9pYp7VNSAjm9Le_5SSxVfn9foQ_pYXMRCNpDy1xePXFcfT75LHL0PI0gPBQMZazqZM8M3dn4AXwOJ0c81GonBp-SwbFLTRP-1Kc21OjXosBcNOBG47O32kh2RcKuk4HvI-T74DHy_GijxUkmrsk2exCEZGj7dqvOFDV8UnE3c2mad2t9q4BX8PDliEP20z21FiWmDsRW-Wvx-Go7q8plWFsPgiizMEsjqaOgfGKwA7yE7Ji5Y6Sm2FDHJpo7OCWE4gWwamRMb7Sh7lU551TWDjVnyw-Jt2A9oR-i6y7OoxB6qmOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtV7fPpf3iIIonl6YREQP2OE1uQAQj3RyZi6q2Y-RrwK_YQWpGYZPbxF2jZ096PA0DadZhky7QeK29093fqHsFwaN5_emPhWTtA8U2X_XM3nus0tAe7N4o7knfQuN0HZtKZYSj927eukkG_CHl95zuC8h_IqZvVGzwuHnBns9ABfkDR2HqsvmX3HvmpFpQw0g1Vx9h_0QUYze8T05qSREHsbuCghJINzXLijFwIVj7yB2NkEmYOq4fEdvIj9qDPX92qFMmKiHV9ucENZNXEAyYFlyUlyM8flAFo9iRQSKjL6tmqDEV-KLgvWMXIearI3OQMYCwbWEFtKHNoZUcpvJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تنفرد نايا بنشر وثائق تؤكد قيام البنك المركزي بحجز أموال 12 مسؤول عراقي بتهم الفساد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88698" target="_blank">📅 21:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88697">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63010842fe.mp4?token=b_EWb61Iq8TLTXc_3Taxa1_mGh16sacaxvsnh1CmLOG7I_DHoQHcUcnpmo1JiAmP68TKYWxRnY9zPD6n_63NaUI1YdfolQhwJ2BUd6ys_VuJmaOQHy2Pksa3aqK2s7KlFlf0XtFjGhaU5heOMVP60-TZxix02JnPuUCf1Vaj5rom3DR1MJ2kCNQSj9N8Ww6PjU-HI0IvPGQIX-Pj5xjxEs1YkeCdsmJRqdLKroXGr8W_0Z9yy9KRZqo661A36vO04R1mpO0wwPn8OT6vfiviRh-x-i11XpLfRM_HY1WmXASjFxBTLDV35ktfPvd19wPRQ_0Ohhx595jWGVHFUH0FyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63010842fe.mp4?token=b_EWb61Iq8TLTXc_3Taxa1_mGh16sacaxvsnh1CmLOG7I_DHoQHcUcnpmo1JiAmP68TKYWxRnY9zPD6n_63NaUI1YdfolQhwJ2BUd6ys_VuJmaOQHy2Pksa3aqK2s7KlFlf0XtFjGhaU5heOMVP60-TZxix02JnPuUCf1Vaj5rom3DR1MJ2kCNQSj9N8Ww6PjU-HI0IvPGQIX-Pj5xjxEs1YkeCdsmJRqdLKroXGr8W_0Z9yy9KRZqo661A36vO04R1mpO0wwPn8OT6vfiviRh-x-i11XpLfRM_HY1WmXASjFxBTLDV35ktfPvd19wPRQ_0Ohhx595jWGVHFUH0FyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
نتيجة هجوم روسي.. إنفجارات كبيرة وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88697" target="_blank">📅 21:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88696">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سماع دوي إنفجار عنيف في الأردن.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88696" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88695">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
عراقجي:
لن نتهاون في مواجهة انتهاك الهدنة، ولن نسمح للعدو بالتصرف بطريقة تجعل انتهاك الاتفاق عادة. لذلك، قمنا بالرد.
فيما يتعلق بأمننا، لا نتهاون مع أحد. مقاتلونا سيردون على أي هجوم بنيران أكبر.
نحن ندافع بقوة عن مصالح البلاد في ساحة الدبلوماسية، تمامًا كما ندافع عنها في الساحة العسكرية. في ساحة الدبلوماسية وفي طاولة المفاوضات، ندافع عن حقوق الشعب الإيراني.
لا نعول على الانتخابات الأمريكية ونقوم بالاستناد إلى قوتنا وشعبنا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88695" target="_blank">📅 21:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88694">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3331e6d8.mp4?token=fs4X1UG0izpIfyId3KPnwdwx28voOLjx5_WgYFqxiWLvSLitZOSOPj0R8AgNngkiGfRbkTT3RSsn8Hnd29SMXJVYZ4B99eCLmo9xobjHfnmnBUE-ITRT3AGwOU_DCEIv-2xWj9NsktiBrbpBhmv3uAvZOcxHOEkLF7E4RXeWCaeTBbl3fZZvFXX5JhISiu2C3YyjzN5fAHYxENMnEgzV7kVj0ESnaz1JXlZsDJuBxzAdQrh8MjH48qutB5hSa6UHGGjjMVUfPiVIHSc0Q9SgD7dUwrwhDbUL0wJxoktb8015LHL5mByOqXs3Bv1Y2RFHg7KehWVp_56PtFK9leK3MYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3331e6d8.mp4?token=fs4X1UG0izpIfyId3KPnwdwx28voOLjx5_WgYFqxiWLvSLitZOSOPj0R8AgNngkiGfRbkTT3RSsn8Hnd29SMXJVYZ4B99eCLmo9xobjHfnmnBUE-ITRT3AGwOU_DCEIv-2xWj9NsktiBrbpBhmv3uAvZOcxHOEkLF7E4RXeWCaeTBbl3fZZvFXX5JhISiu2C3YyjzN5fAHYxENMnEgzV7kVj0ESnaz1JXlZsDJuBxzAdQrh8MjH48qutB5hSa6UHGGjjMVUfPiVIHSc0Q9SgD7dUwrwhDbUL0wJxoktb8015LHL5mByOqXs3Bv1Y2RFHg7KehWVp_56PtFK9leK3MYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
نتيجة هجوم روسي..
إنفجارات كبيرة وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88694" target="_blank">📅 21:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88692">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8280ed98e.mp4?token=Tw7RABnLTB4IjRKvb3g9nBO6TPeOqqFKOxplkOnNCTFYDzO4oZqs8XIvFhXYSQIYKfATP9wy1nXWiFHJv45nZ0dzvjjrFQFtLvruTeDEkKX18ndvTTdOz5K9YHkfoSPYicSYJ0wpTKO2q_nU26dzodphxpmOSULyRecChETcF9y3ukruIjEYD2maH9Z58_QoZC5XCPZpDeIboBSiSzCm_ktiEoUq0Emgx9yDpdRo7mZBTSSE20-0fDsL0U0zoJZy2_qR3gXT9GDrNKwxU3ddrRSQ0bjpAkoYxYxKTnWP7aKA9GYmnGMdhjmxXkZ7kQRfUZNQLRn3eB1HyJajLH9tYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8280ed98e.mp4?token=Tw7RABnLTB4IjRKvb3g9nBO6TPeOqqFKOxplkOnNCTFYDzO4oZqs8XIvFhXYSQIYKfATP9wy1nXWiFHJv45nZ0dzvjjrFQFtLvruTeDEkKX18ndvTTdOz5K9YHkfoSPYicSYJ0wpTKO2q_nU26dzodphxpmOSULyRecChETcF9y3ukruIjEYD2maH9Z58_QoZC5XCPZpDeIboBSiSzCm_ktiEoUq0Emgx9yDpdRo7mZBTSSE20-0fDsL0U0zoJZy2_qR3gXT9GDrNKwxU3ddrRSQ0bjpAkoYxYxKTnWP7aKA9GYmnGMdhjmxXkZ7kQRfUZNQLRn3eB1HyJajLH9tYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
إندلاع معارك مسلحة عنيفة وخروج الوضع الأمني عن السيطرة في بلدة جديدة عرطوز بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88692" target="_blank">📅 21:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88691">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlaTegwTr65oGXhsWZ6kqnKGiTfSJKjzSKcISxeQC9U4x7TIVUsWhAL0NOGNDdXe0yOgSNsc3cx7uMJJf8nyiWzKi1dbmdel7SlcFDH8be819zH7WOjw4paYFumDx3sb7xfGfHea_zetB8tznIz2lK3rgavrPcFmO2BSV8KpkI2fRpdw5hUsZm5_JwnFgkjqHrjKVxGvRIVvPQfZqeAOdWyHAh1827fjt187UZw7uaUwfqAr5hnl7ngzU45fKG2bQpIlMbxBLMlUIIw8Una79y9VHJe7xR62hX5mbMeWqv6FhT-truBh-BRvlDuTiZ3PVdzsOtAEvbgFVRf5HuBypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:  أعلن بشكل قاطع؛ ارتكاب أي شيء يضر بالوحدة الاجتماعية أمر ممنوع.  أثمن إجراءات حكومتنا التي نفذت رغم قيود ومؤامرات العدو الأمريكي والصهيوني والعقوبات والحصار.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88691" target="_blank">📅 20:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88690">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
مسؤول في حلف شمال الأطلسي "الناتو":
لم يتم تحديد أي موعد لإنتهاء عمل قواتنا في العراق، وأن مهامنا مرتبطة بـ "الحاجة"؛ تم نقل فريقنا من العراق إلى إيطاليا "بشكل مؤقت"منذ شهر آذار الماضي بسبب الأوضاع الأمنية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88690" target="_blank">📅 20:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88689">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979455137b.mp4?token=o8Pbemr_8VTLYmPIFRPiGIbPAKWoGgCIgXnP1mTnMYAKxhbG6cq8DzJbyH_ly0xY0gAH92hUDUHNfdwpC6_M8DeShVJMOpcQyD5-G8S87TgCAe6wvAfyd-S9Ql4y-FVFpQ08CyBDdag554BOP9qwbP0DtLjI77ZFmIUgDVFVqx_V3AcZ-LSLFocR8l3Ji9WFd9J4aNPF4VEfIzrWbmwpMvbxlog5EaNBbhalqVxZXrysCu9kS1uqm9h5kTdUiT_zIeg6uMpIlMfF5RZcE9QHKSevHztzomtLjn7YkaPPt9Xne6VNpz43z4DbvTyQoCAXwfog_9e8idGVO4T8Mu5EUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979455137b.mp4?token=o8Pbemr_8VTLYmPIFRPiGIbPAKWoGgCIgXnP1mTnMYAKxhbG6cq8DzJbyH_ly0xY0gAH92hUDUHNfdwpC6_M8DeShVJMOpcQyD5-G8S87TgCAe6wvAfyd-S9Ql4y-FVFpQ08CyBDdag554BOP9qwbP0DtLjI77ZFmIUgDVFVqx_V3AcZ-LSLFocR8l3Ji9WFd9J4aNPF4VEfIzrWbmwpMvbxlog5EaNBbhalqVxZXrysCu9kS1uqm9h5kTdUiT_zIeg6uMpIlMfF5RZcE9QHKSevHztzomtLjn7YkaPPt9Xne6VNpz43z4DbvTyQoCAXwfog_9e8idGVO4T8Mu5EUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
إندلاع معارك مسلحة عنيفة وخروج الوضع الأمني عن السيطرة في بلدة جديدة عرطوز بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88689" target="_blank">📅 20:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88688">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:
أعلن بشكل قاطع؛ ارتكاب أي شيء يضر بالوحدة الاجتماعية أمر ممنوع.
أثمن إجراءات حكومتنا التي نفذت رغم قيود ومؤامرات العدو الأمريكي والصهيوني والعقوبات والحصار.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/88688" target="_blank">📅 20:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88687">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
‏
الإعلام الأجنبي:
قال نتنياهو "سننقل المنشآت العسكرية تحت الأرض". ويبدو أن سياسة نقل المنشآت العسكرية إلى تحت الأرض درسٌ استخلصه النظام الإسرائيلي من الحرب مع إيران. فخلال حرب الأيام الاثني عشر وحرب رمضان، استُهدفت العديد من القواعد والمراكز العسكرية الحساسة للنظام بدقة بصواريخ إيرانية، على الرغم من أن جهاز الرقابة في الجيش الإسرائيلي منع بشدة نشر هذه الحالات في وسائل الإعلام.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88687" target="_blank">📅 20:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88686">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
ترامب:
أنتم ترون كم نحن جيدون في القتال. نحن نقاتل بشكل جيد جدًا. انظروا إلى فنزويلا. 48 دقيقة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88686" target="_blank">📅 20:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88685">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0568799d32.mp4?token=DwlAAiH3JynBqpd3Jo0INRqsj4rXHMngq2R1PTnBb4BOc6LSyT8le8lCSfIVWp4U-LiXPqtxy_TDXZYTRK-1Ez4CmoOnUFF6N8VQYl8Uy4ZBCK4EtHVkEF3vM6Hr8-x8VpWTrPFFjynesBLMjmCgNWJmP9_B5Ebay7NkS3wxLnTQgF7hrYC83Ej_DzVJH0jU2tROm_jg7-0j9USV88YLp6LQ9sAAcdEvG9Igl4HYbS_YxlzryI4e_MiIb1ZXky9vgBNqVlG9nNzO02sfuIDD6sUyFqJJjz6be5cydbhF22XgR4ph-z3COY0UY3ELa1m6VRQjbF4PrhfEUFPdGkc8h6A-BfqoVfpWld3keyyOnXMuvr7sYZEMBIstZ0xjTrr_3L98k6oBpWSuZHIcfdrKUyeFJm8S5wpoi4ZzCWZj_HNSn4y5MzPjF6eekNXUgoupqAf9VxHuKtwbHmW6anihR-mKxf1BaEg6Kb1LSG0JHOJDc7921GQf6MBiPGWusnl0Vn765qHjLZErbqTpMA8gseQhdw4hJJl_VNwxxBFE3uxMFMZa6SWlltxR7gZY0o9_JayKEKFmqycx5CZJ99e_K_78cD_hUaeofSN_hgvE46AytgOYcLm4SET0KoO7x-FVs0Lkt2XaiKrZGUPajgwDvoDNyIteBsnXXXfZYukW1rE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0568799d32.mp4?token=DwlAAiH3JynBqpd3Jo0INRqsj4rXHMngq2R1PTnBb4BOc6LSyT8le8lCSfIVWp4U-LiXPqtxy_TDXZYTRK-1Ez4CmoOnUFF6N8VQYl8Uy4ZBCK4EtHVkEF3vM6Hr8-x8VpWTrPFFjynesBLMjmCgNWJmP9_B5Ebay7NkS3wxLnTQgF7hrYC83Ej_DzVJH0jU2tROm_jg7-0j9USV88YLp6LQ9sAAcdEvG9Igl4HYbS_YxlzryI4e_MiIb1ZXky9vgBNqVlG9nNzO02sfuIDD6sUyFqJJjz6be5cydbhF22XgR4ph-z3COY0UY3ELa1m6VRQjbF4PrhfEUFPdGkc8h6A-BfqoVfpWld3keyyOnXMuvr7sYZEMBIstZ0xjTrr_3L98k6oBpWSuZHIcfdrKUyeFJm8S5wpoi4ZzCWZj_HNSn4y5MzPjF6eekNXUgoupqAf9VxHuKtwbHmW6anihR-mKxf1BaEg6Kb1LSG0JHOJDc7921GQf6MBiPGWusnl0Vn765qHjLZErbqTpMA8gseQhdw4hJJl_VNwxxBFE3uxMFMZa6SWlltxR7gZY0o9_JayKEKFmqycx5CZJ99e_K_78cD_hUaeofSN_hgvE46AytgOYcLm4SET0KoO7x-FVs0Lkt2XaiKrZGUPajgwDvoDNyIteBsnXXXfZYukW1rE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قوات شعبية إيرانية تنطلق نحو مضيق هرمز ردًا على تصريحات ترامب.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88685" target="_blank">📅 20:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88684">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇾🇪
🇸🇦
هجوم يمني بالطائرات المسيرة الإنقضاضية على معاقل مرتزقة السعودية في مدينة المخا اليمنية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88684" target="_blank">📅 20:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88683">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF65Hw8cCfgWth-kk6tFi7oc9Pn5H8p-tVpfjW1dbjTI6GQjCBi-IJ0Z3edrP9mYLS5EPhxCPMyDNmTIUCDpzYsAGj1TKvLFf9eiyWT6UXJEnuCKEAyQ4nnkS2ajIoa24NHTDWQLQJm7kiaAckmz6fCtjNpKlbrxqUNFuOfUkxXAXljlJrM-H89WSolxiIJknGp-jqVQuytkmgWZXUDBxoPNp-gO4crbVvFL0gZwohDlPXeMieu0iwTnnD3uhWzChVJT7LOhGBnntk4SQWQVIc3HSgDMnY2eL6EYOZPM4eUkmm-Z3e3TwOxTQdV-eFMLjDrO2f0EQBH235rtXK7J7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇷🇺
روسيا تشير إلى ايران
وتفتح النار على القصص الملفقة التي صنعتها الصحافة البريطانية ؛ ماريا زخروفا في عام 2010 بشأن سكينة محمدي أشتياني (ولا يزال بدون تراجع) - كان ملفقًا بالكامل. ساهمت القصة الملفقة في تأجيج الضغط على إيران. ليس هذا بالأمر المفاجئ، بالنظر إلى سجل الغرب في التلاعب بالمعلومات.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88683" target="_blank">📅 19:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88682">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
إشتباكات بين القوات الأمنية الإيرانية وعناصر إرهابية في مدينة سراوان جنوب شرق إيران؛ مقتل إرهابي وإعتقال 6 أخرين.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88682" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88681">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
‏
برنامج الغذاء العالمي:
نحذر من نقاط الاختناق في هرمز وباب المندب والبحر الأسود.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88681" target="_blank">📅 19:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88680">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
🔻
الحاج العامري لشيوخ عموم عشائر العراق:
-سنشرع قانون الحشد الشعبي وتحدثنا مع رئيس الوزراء وهو يؤيد ذلك
-فصائل المقاومة أناس عقلاء دافعوا عن العراق وسيادته وقاتلوا الاحتلال وداعش</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88680" target="_blank">📅 18:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88679">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇾🇪
🇾🇪
الحكومة اليمنية في صنعاء:
امتزجت دماء شهداء اليمن مع شهداء فلسطين ولبنان وإيران والعراق بمواجهة العدو المجرم نفسه الذي يستهدف الأمة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88679" target="_blank">📅 18:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88678">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
🇺🇸
أثار حرب أمريكا على المنطقة
ول ستريت جورنال:
‏توقف مشروع نيوم الضخم والمستقبلي في السعودية، حيث اصطدمت التكاليف الباهظة للمدينة المخطط لها بالواقع المالي.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88678" target="_blank">📅 17:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88677">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736924625c.mp4?token=r027ujTP34f0ad0XbMLvc815o1il5AMz1QF4PUJmMTm1OWpMWWFI5ogPjA84CliYSjeq6bKQTUeNtkrWJ6VgVpK3MolXME6KVwJioX0gFj5PQd1QKrvOgF_IptAh6lhjkO8xlLJGvG_T4qk3kD_fX4RKPXEmXK6yoCF5p0TiJ3g7G9e6B_0CoEkLpZFCjoX3E-afODtbW4EZO0gyVttK-7yrAOutYp_q4wJwvtdzpSy9vGtwI3eIyXqLFWWEnn7O6KiApVku-L5O8ZkVVhVl7JcXJPMOoCBJD2uDDMa8v8DJ1gzJJUphHJrMFk1WgLt_ibY-TjPXg6I8IzfTMSgg3JXDbmnt12xzTSQqYDEyPv5UsK03-LLXIS0jJRwqNu5vBkK9c98a9377qWgw-_LYgDMNOizPENg4p2aH9cxyPbky_e2evL_BsQbX0xm484nhIEm24xq3bEaSg8sQY9CMRqaMXJ98xOzzeYl8hIaGKz6mDxSnXc5orAesIzOSfLfz6eQaC7PCJkQYMrUibw6zfNLAhNFrBYNHk54COkG2GZoGIDTlM3KFM2UwMICMP69XDqQxb4y8GdDIhC-8iPdkgXAjY-BkruSMCt_JWLwH5-CcKpuVyLX4DTcul6Vr-wjVUOy2-9-7lnLDOkQjIaYxfTW7ecg9j7kD1jFT8ppdwKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736924625c.mp4?token=r027ujTP34f0ad0XbMLvc815o1il5AMz1QF4PUJmMTm1OWpMWWFI5ogPjA84CliYSjeq6bKQTUeNtkrWJ6VgVpK3MolXME6KVwJioX0gFj5PQd1QKrvOgF_IptAh6lhjkO8xlLJGvG_T4qk3kD_fX4RKPXEmXK6yoCF5p0TiJ3g7G9e6B_0CoEkLpZFCjoX3E-afODtbW4EZO0gyVttK-7yrAOutYp_q4wJwvtdzpSy9vGtwI3eIyXqLFWWEnn7O6KiApVku-L5O8ZkVVhVl7JcXJPMOoCBJD2uDDMa8v8DJ1gzJJUphHJrMFk1WgLt_ibY-TjPXg6I8IzfTMSgg3JXDbmnt12xzTSQqYDEyPv5UsK03-LLXIS0jJRwqNu5vBkK9c98a9377qWgw-_LYgDMNOizPENg4p2aH9cxyPbky_e2evL_BsQbX0xm484nhIEm24xq3bEaSg8sQY9CMRqaMXJ98xOzzeYl8hIaGKz6mDxSnXc5orAesIzOSfLfz6eQaC7PCJkQYMrUibw6zfNLAhNFrBYNHk54COkG2GZoGIDTlM3KFM2UwMICMP69XDqQxb4y8GdDIhC-8iPdkgXAjY-BkruSMCt_JWLwH5-CcKpuVyLX4DTcul6Vr-wjVUOy2-9-7lnLDOkQjIaYxfTW7ecg9j7kD1jFT8ppdwKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
اندلاع حريق في احد مقرات الحشد الشعبي بقاعدة سبايكر شمال غرب محافظة صلاح الدين العراقية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88677" target="_blank">📅 17:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88676">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏الخزانة الأميركية تفرض عقوبات جديدة على صلة بإيران</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88676" target="_blank">📅 17:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88675">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏الخزانة الأميركية تفرض عقوبات جديدة على صلة بإيران</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88675" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88674">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇱
نتن ياهو يزعم إحباط هجوم وشيك من جنين.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88674" target="_blank">📅 17:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88673">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1275ca3466.mp4?token=DuyFqODE4GrIhSiwAHxyZK8aioD7ALerwuXiSnxbT4w0shAoPAXncFcGUiQ7e6ahWnlxydGwTVfUB-ZSVQGd3dmDVVxAiaepVPfl5PT0nIXH6bmWS1fbVEYEngZfHlZoodDkS1mLQae9S5cOIiQ-4iYlsc8-aJ4nrTK8BOp6R6H5wLIvOYwTnjKuz05o5ee4PSG1eYHGTyRPHdAIr1AP2FfPpnHXUpfQac5EdqISxNxo_uUlqLIfBTd3VqcbNHsVjC6zkOWvExnyo1szTw4fv2GP6j4vuTTXjdqR__mWNFjfgZQseJMcBlKu3zYcAfKXcbSCOp8x4lWyGe7rgB8LWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1275ca3466.mp4?token=DuyFqODE4GrIhSiwAHxyZK8aioD7ALerwuXiSnxbT4w0shAoPAXncFcGUiQ7e6ahWnlxydGwTVfUB-ZSVQGd3dmDVVxAiaepVPfl5PT0nIXH6bmWS1fbVEYEngZfHlZoodDkS1mLQae9S5cOIiQ-4iYlsc8-aJ4nrTK8BOp6R6H5wLIvOYwTnjKuz05o5ee4PSG1eYHGTyRPHdAIr1AP2FfPpnHXUpfQac5EdqISxNxo_uUlqLIfBTd3VqcbNHsVjC6zkOWvExnyo1szTw4fv2GP6j4vuTTXjdqR__mWNFjfgZQseJMcBlKu3zYcAfKXcbSCOp8x4lWyGe7rgB8LWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازمة الوقود متواصلة في محافظة اربيل ضمن اقليم كردستان العراق ولا حلول تلوح بالافق</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88673" target="_blank">📅 17:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88671">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">المنظمة البحرية الدولية التابعة للأمم المتحدة": نحو 6000 بحار على متن 400 سفينة لا يزالون غير قادرين على مغادرة مضيق هرمز</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88671" target="_blank">📅 16:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88670">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
🇨🇳
موقع ذا إنفورميشن:
الولايات المتحدة تعمل على وضع قواعد للذكاء الاصطناعي للحد من وصول الصين إلى الرقائق الإلكترونية. الولايات المتحدة تعمل على إيجاد بديل لقاعدة الذكاء الاصطناعي الحالية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88670" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88668">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
🚀
🔵
إعلام غربي :
رصد طائرة مسيرة أخرى في مطار لايبزيغ هاله في المانيا ؛ ويأتي هذا الحادث بعد أسابيع من اكتشاف طائرة مسيرة محملة بالمتفجرات بالقرب من طائرة شحن أوكرانية في المطار نفسه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88668" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88666">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1vpYn8zqUdjND4EbvNn5kUL8nqN0PXI5XUKbF81QGJfkB0-LOoIWc_aY6XZ61YTahAqbsTHQVM3HETxzaEweV-gshJAMlzPmww3L25mlpe-yfy1yY2t8I0pwxLQn65FuJRA7uxwTuKY6uz-kv65IQ-PhUouCZzrlceawGw0en0IxbsL6F0v3AljYpsIh-ym6fbK-2uEKRcd3sj1ZSkoncY9X91FlIpIUZAJGkeIlv0ZFbSes8hChEo80t-U6RQPJI_iJQS8FbOMXykljPb7aGsRzQlIAlyIZ85lRN4pUwPkHy8-EJIm2lzLlzQXWcJfzqmd7g_AnVvbUw4SXvLN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKWoqaJtLRQA9UNZhW7G8akqF0MzjGAL3zJObiSQVaq5NM9rgzUwd8QMiMEXOjzLbHA0FKvNKELrOTmRL79QtHfiRJUBu0ka0471f-Lzmo8DuvU3R7ggWWab6kndvEkgwKY1e65_iyuO7R8LvAG4ub8cKvTL_8QhUtgYsg3mmBSVWg69ncZtNIpfjh0QHOIGCt8VT_ifbfsYp-L5WLwQJkPuD4hEVLYWK_ev4rmGmXUdnS0LdkBY-O3C8OD4bWjyUxkIcJsG1Yb5XlwdGTtkVb3bTc4UC7aoJLToZ7DBUKTuZI3iPmhPwsi6fB02itLWBurDZnQ8NNPEZp6rTaH72Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بيان وزارة الخارجية الايرانية بخصوص العقوبات الاميركية:
بيان صادر عن وزارة الخارجية بشأن الإرهاب الاقتصادي الأمريكي ضد إيران
۱۴۰۵/۰۶/۰۶
في إطار استمرار سياساتها العدائية وغير القانونية ضد إيران، كشفت الحكومة الأمريكية عن موجة جديدة من الإرهاب الاقتصادي يوم الاثنين 2 سبتمبر 1405، تحت عنوان عملية الإقصاء الاقتصادي ضد إيران، وهو ما يرقى إلى مستوى إرهاب الدولة الأمريكية ضد إيران والعالم.
إن إساءة الولايات المتحدة استخدام الدولار كأداة لترهيب الدول الأخرى وإجبارها على اتباع سياساتها التدخلية والمخالفة للقانون الدولي فيما يتعلق بإيران، يُعد انتهاكًا للسيادة الوطنية وحق تقرير المصير لجميع الدول الأعضاء في الأمم المتحدة. وتُمثل العقوبات الأمريكية المفروضة على إيران، بطبيعتها وعواقبها، انتهاكًا صارخًا لميثاق الأمم المتحدة. إذ تنتهك هذه العقوبات مبدأ عدم التدخل في الشؤون الداخلية للدول، ومبدأ عدم عرقلة التعاون بين الدول، وهو مبدأ تم التأكيد عليه، من بين أمور أخرى، في الفقرة (2) من إعلان عدم جواز التدخل في الشؤون الداخلية للدول، القرار 36/103 الصادر في 9 ديسمبر/كانون الأول 1981، و"إعلان" مبادئ القانون الدولي المتعلقة بالعلاقات الودية والتعاون بين الدول، القرار 2625 الصادر عن الجمعية العامة في 24 أكتوبر/تشرين الأول 1970.
إن إعلان الحرب الاقتصادية على إيران هو استمرار للحرب العدوانية التي تشنها الولايات المتحدة والكيان الصهيوني ضد إيران منذ عام ونصف تحت ذرائع كاذبة لا أساس لها، مما يُهدد السلام والأمن الإقليميين والدوليين. جميع هذه الأعمال تُخالف القانون الدولي. وللأسف، فإن لامبالاة وتواطؤ منظومة الأمم المتحدة ودولها الأعضاء تجاه الانتهاكات الجسيمة للقانون الدولي من قِبل الولايات المتحدة والكيان الصهيوني قد أدى إلى تشكيل نمط خطير للغاية من خرق القانون وارتكاب أخطر الجرائم الدولية، مما عرّض الحضارة الإنسانية جمعاء لتهديد غير مسبوق.
تُثبت عملية المقاطعة الاقتصادية بحد ذاتها النية الإجرامية لمصمميها ومنفذيها في إلحاق الألم والمعاناة بالشعب الإيراني وحرمان المواطنين الإيرانيين من حقوقهم الإنسانية الأساسية، ولذا تُعتبر جريمة دولية وجريمة ضد الإنسانية. وتُعد هذه السياسة انتهاكًا صارخًا للقواعد الأساسية لحقوق الإنسان المنصوص عليها في الإعلان العالمي لحقوق الإنسان والعهود والميثاقين الدوليين، وتتعارض مع المادة 1، الفقرة 2، من العهد الدولي الخاص بالحقوق الاقتصادية والاجتماعية والثقافية. كما تُعد العقوبات الأمريكية انتهاكًا مستمرًا لحكم محكمة العدل الدولية الصادر في 3 أكتوبر/تشرين الأول 2018، والذي ألزم الولايات المتحدة بإزالة جميع العقبات والقيود المفروضة على حرية التجارة، بما في ذلك الأغذية والمنتجات الزراعية، والأدوية والمعدات الطبية، ومعدات وخدمات سلامة الطيران المدني الأساسية، والأموال ذات الصلة. وقد خلقت سياسة العقوبات الأمريكية الجديدة وضعًا جديدًا، ومن الضروري أن يتخذ المجتمع الدولي، بما في ذلك أجهزة الأمم المتحدة، التدابير اللازمة لحماية سيادة القانون.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88666" target="_blank">📅 13:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88665">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e23lDHElekfa9qBueOI39VN8JJbsN92k1xaVK_jg7zaTWUqg0eUCEC_k5no8e-8d0AaNMB7j7_-NNnr-JvXgcYD6-Gt7F_1cLvCveF0rCZHRNIfJsBAd9K4zn-wde-SZIktP386flhU79PJDWJ9gjAZCvWAgt4NO3XUYA5hKUwV7MIhEYCu6c0zzX6cI1z-z-W1M7Uzfh9eLvEStkg2WBuykx8xaVRhxIIJfzOehQBw6UmnIoRnHXYyZhYXPe4Aifr_OhCMN0weN5OfVmxE7d42PUD1rgoOfSz_yDMBJ6atgT2h5tKHQCaE3vu7XYU3QcGXpEucERgY9HbbRoGnsWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف يعيد نشر:
معادلة هذه الحرب واضحة: إما الكل أو لا شيء!
في منطقة لا نبيع فيها النفط، لن يبيعه أحد. إذا لم يُضمن أمننا، فلن تكون أي بنية تحتية آمنة، وأمن المضيق مرهون بغياب القوات الأمريكية. لقد أكدنا مرارًا وتكرارًا أن الوضع في المضيق لن يعود إلى ما كان عليه قبل الحرب.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88665" target="_blank">📅 12:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88664">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXFtgDo7V0ni5ON7RSA-d1xIxLV0XjhmUvxko4-4zR0YH5jTYJhkFWAnbHqUt2kdife3sHltc1LwWFBz4eegMKicohB6x904SvMuih7dvA74mlKqfO9kVLoCEWHa9_fGY2nnejADP7uAzOP8ZduWqDrzHgSoNzXKu7wV1x3pPl2A21Up017DTD_Q5wh1-upoedFTqCbRnrEoQwH0HBHyDwBcSRJMr7NGsq4_PHjnqY71Mw4VrVAN5AntQKxA7rEolt6UgJu_aR4E3mnBdlgYY4Keev3MYIcDnypQvxigyJc1M6SCpdWOvBNXFSDd7_s9u-W-fSd-y7MgnO3wV8fziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
نتنياهو يتوسل لبن غفير لكي يعقد اجتماعات مع سموتريتش حتى لا تذهب الانتخابات نحو المنافسيين:
أدعو الوزير إيتامار بن غفير والوزير بتسلال سموتريتش لعقد اجتماعات يوم الأحد. لا يجوز إضاعة أي صوت، يجب أن نتحد لإنقاذ الكتلة اليمينية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88664" target="_blank">📅 12:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88663">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇱
إعلام العدو يدعي :
‏أعلنت الشرطة وجهاز الأمن الإسرائيلي (الشاباك) عن توجيه الاتهام إلى مراهقين عربيين، أحدهما قاصر والآخر بالغ، للاشتباه في ارتباطهما بتنظيم داعش والتخطيط المزعوم لارتكاب هجمات إرهابية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88663" target="_blank">📅 10:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88662">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-PLxS3PkbPH7e3qK0qkVxYpV9m0fxHc48GDmXxr4lgehEIAeJZ4p49WVpw04iRpnxF0MQG0WHKaT4e9cCFr8RzNndJc6VQSPyb5x-qilD4O8TPO4C2ba52n1tByIJfp9a0sIltTQB1k2j0viU5mpA-AlUwGxfR5YaVIrYDme9b1msY75bJJfXf9DbP-VLvHXdEHieMFNRxcHAkVUIVIrq9rpQvqNTtnqSBxFCvAQ2ONzeRxUI-6mfUVsOwxU2uGDPBovQ2TN84s8AxQxBWevPFm-BtshICTqEDGXWXVZkI72TSMvIOwTA_38_vAWY9dA045XjmH_v23C8i34bowAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
أجرينا مناقشات بناءة ومبتكرة مع رئيس الوزراء وزير الخارجية القطري في طهران.
إن إعادة الدبلوماسية إلى مسارها الصحيح ليس مستحيلاً. ويتوقف ذلك على فهم الولايات المتحدة لحقيقة بسيطة واحدة: الضغط لا يجدي نفعاً. يجب على الولايات المتحدة بناء الثقة، والتحدث باحترام، والاعتراف بحقوقنا، والوفاء بالتزاماتنا.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88662" target="_blank">📅 10:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88661">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
🇷🇺
الاعلام الاميركي: سبقت رحلة مدير وكالة المخابرات المركزية جون راتكليف إلى موسكو معلومات استخباراتية أمريكية جديدة تشير إلى أن الكرملين يرى أن الولايات المتحدة قد ضعفت بسبب الحرب الإيرانية، مما يمنح روسيا فرصة لتصعيد العمل ضد المصالح الأمريكية في أوروبا.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88661" target="_blank">📅 02:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88660">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtZNCNOa2fWdy_ZMEq9mcjHoZ6MPHlxx-aUK7nIDc6dQq78lhNSTkd20XiSZwkywtzbi-3puqr--FvI4e49xLeccEsrml7sfE_eSXQBkCCZjG0tKkho419cVwX05bv-bUY05kpxmdPcI80-Ng8CNiPY1be9gzjSbREgmVCOpCIgbaa8U1uWjVwPY12vFUbSYeImd7yh61GDelwmL-bHEq2dft38I1eGtzsw9X428XCINkkfqcNkNZV9G_9VQJs9UiJw_Nl3FoRFzY4BrZvZTW03ApHZaQCTAWD_l6I07_E1xiSGWi1H7yozMo1KCD3OtfXMUP5V-39slzlQOit0p1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: قدم جوناثان هانت من فوكس نيوز تقريرا غير دقيق بشكل خاص عن جمهورية إيران الإسلامية الفاشلة. لا أريد أن ألتقي، إنهم يفعلون ذلك. في الواقع، إنهم يتوسلون لإبرام صفقة. يجب على بريت باير تقويم فاشله، من أجل التغيير!.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88660" target="_blank">📅 02:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88659">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on5Ftt0g8ywmQ-vXY5giYIDQvowjXZmpYKbOnHa1Ps6mVuJyRnHhLBLRELjGU7LMA62v8bRqROcDciCBDcvuDQLprsnQbdwNDiVh2lyGX-wlmTjH1lROlP0spTGrCls9qVp8ygAzR98hdJIDzOXfFWNG7LXs1Ul7RY-IwwbBc_D7hcqQCZ7FTnjXX_rVelcH7eT5dqy54HRlaTMx24FYu_b7X8HKZY5kBXc4iBbxDknr0ezVa6Qbt0O-8A3CtPon-wbMUc-H0rhik1tkd0wmCeaTQ8jyFma85UIdMUDb9X2ht5L2QHNBFMd_Gtn3Vqcaz6moaY9dRmJaOKtqrYAvzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: قدم جوناثان هانت من فوكس نيوز تقريرا غير دقيق بشكل خاص عن جمهورية إيران الإسلامية الفاشلة. لا أريد أن ألتقي، إنهم يفعلون ذلك. في الواقع، إنهم يتوسلون لإبرام صفقة. يجب على بريت باير تقويم فاشله، من أجل التغيير!.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88659" target="_blank">📅 01:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88658">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
اشتباكات عنيفة جراء نزاع عشائري في قضاء الجبايش بمحافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88658" target="_blank">📅 01:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88657">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">المراسل: هل وجه مدير وكالة المخابرات المركزية راتكليف تحذيرًا إلى روسيا بعدم مهاجمة أراضي حلف شمال الأطلسي؟  ترامب: لا أريد التعليق على ذلك، لكنهم لن يهاجموا.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88657" target="_blank">📅 01:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88656">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
ترامب ينشر رسميا تم تغير اسم بحرية أونتاريو الى بحرية اميركا.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88656" target="_blank">📅 01:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88655">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDoODx03yfBaoRfRHtLTrFR7GopM56Qd9uoQTO7ktmONCZ8c7MhlGmw-BS0gt7JJyPEeUYkqZSC1JApBZ-TFy_sTrGvfdiBnnQtzhmRNBuG1JH6lbcDPCUlgAnygqB0JSUgzJAt6C-npXxCoSXqMI83CMQWcXYZpREZTYxv6q9DsciRaE_-oywpbFi5G7mGGrOuxzqdG1rM-dtTIARlXuauk5h3_mJGlNFYnCbvdyAgsH2Be4Lr8_Xv3oKMRBoDKE91H4YfxsiibST65TQn-_942ZTyZS1HLDYfMmWkLY7JPkTKJjLeF4BHCc8I6NQLAxJ6k6BEwERw6cM7CbJ0YXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر رسميا تم تغير اسم بحرية أونتاريو الى بحرية اميركا.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88655" target="_blank">📅 00:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88654">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
رئيس لجنة الأمن القومي في البرلمان الايراني عزیزی:
لا توجد أي سفينة تعبر مضيق هرمز دون إذن القوات المسلحة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88654" target="_blank">📅 00:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88653">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
رويترز
: زلزال بقوة 6.2 درجة شرق خليج عدن.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88653" target="_blank">📅 00:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745cf92c81.mp4?token=ShPVGW-kk4YHXDaPJCrJ7PyDS30CfZVvc0VFPJhyXPMrtwu9XXNYLsXEOCn3sP6uQMzUozj4lgi8kyQRrEvGAt6EufFX6tuP9roJB3MRddfkPw02M-3mloiCoWMiTtp9dzkOgDYIQlBsNFY5yaMzm-hl5_jHBGNwGbEiXsV86FJ6aQ7rYoSgJA9Ci04FdKmJT34ms106Wa03EaWzzubTNwA2zMAM_FHLLfEfGRF4duHCariJ-sXOfb2qW-Tgl2nTzLVP-S5j-LUGwhb2IlonEsEC-s0QazRcsFLOW4aRl-3jQcMPpcgR-cBMB56LksPeilO-cTWz5ocko6sm5Xsc6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745cf92c81.mp4?token=ShPVGW-kk4YHXDaPJCrJ7PyDS30CfZVvc0VFPJhyXPMrtwu9XXNYLsXEOCn3sP6uQMzUozj4lgi8kyQRrEvGAt6EufFX6tuP9roJB3MRddfkPw02M-3mloiCoWMiTtp9dzkOgDYIQlBsNFY5yaMzm-hl5_jHBGNwGbEiXsV86FJ6aQ7rYoSgJA9Ci04FdKmJT34ms106Wa03EaWzzubTNwA2zMAM_FHLLfEfGRF4duHCariJ-sXOfb2qW-Tgl2nTzLVP-S5j-LUGwhb2IlonEsEC-s0QazRcsFLOW4aRl-3jQcMPpcgR-cBMB56LksPeilO-cTWz5ocko6sm5Xsc6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اشتباكات عنيفة جراء نزاع عشائري في قضاء الجبايش بمحافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88652" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجارات عنيفة تهز دمشق</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88651" target="_blank">📅 00:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏
🇬🇧
أفادت التقارير بأن فرقاطة تابعة للبحرية الملكية ستوفر الدفاع الجوي لقمة الاتحاد الأوروبي المقبلة في دبلن بناءً على طلب جمهورية أيرلندا.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88650" target="_blank">📅 00:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88649">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
هيأة الإعلام والاتصالات تتخذ إجراءات بحق قناتي (أي نيوز) و(الرشيد) بسبب مخالفات لقواعد البث الإعلامي شملت توجيه تحذيرات وإلزام قناة الرشيد بإزالة المخالفة وتقديم اعتذار رسمي فيما قررت منع ظهور السيد عماد باجلان إعلامياً لمدة 15 يوماً.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88649" target="_blank">📅 22:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88648">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
إدارة ترمب أبلغت الوسطاء مرارا أنها لا  ترغب في العودة لبنود مذكرة التفاهم مع إيران.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88648" target="_blank">📅 22:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88647">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
مستشار رئيس الوزراء للشؤون المالية
: 40 مليون مواطن مستفيدون من رواتب الدولة، فاتورة الرواتب تصل إلى 7.7 ترليونات دينار عراقي شهرياً وتأمينها مسألة إلزامية، سعر برميل النفط في الموازنة سيكون ما بين 50-60 دولاراً، لا توجد أية علاقات مصرفية بين العراق وإيران ولا توجد أية عمليات دفع بالدولار منذ 2011، حجم الغاز الإيراني المستورد حالياً يصل إلى 18 مليون م3 تدعم الشبكة بـ4500 ميغاواط، لا توجد أية تعاملات بالدفع الإلكتروني مع الجانب الإيراني.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88647" target="_blank">📅 21:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88646">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nziBTuEwGTcU5ROsCWz3PEtQqIu80VUJyc4qM3yvr4jgT6VdZxZx6dQPbPuWItBd0zkFrB0EapmKH2ylE_-XE_wbOt1Q_9Oo0c5bIz041lWZ5FLKuB56ZPneGC9CEgr0nqCQf-HrE7hMN8EBJ27RU8CFUjtRkyilYX6-2u9hU8aP_qm9qoeAf-948vwIqysG0LTir41fQ72hd1nfwY2mDVjfVtDoltoPfvz_hCwJPpOaCJFOmMvho2kePCaLVhnpqQ4o_7aLOU2M8Iv1m1fBKgzEkX7h6CYRhdH0aGsTqfCGVK9pyAk60iLW7h3Se8AvC1VmUCK9Tkqni5OSPKx1jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏ناقلة غاز البترول المسال الأخرى، "سيجيت" الخاضعة للعقوبات الأمريكية، تعبر مضيق هرمز عبر الممر الذي حددته إيران.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88646" target="_blank">📅 21:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88645">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2e6046c.mp4?token=Jh4SgRXmB-g_Ma6W5GNgjW8uAOk1c4jRdvDZInt02sYSKhpQxzdF8H3Rq6lXQokm6uHPYEQkKmZKucMGZgn1RY4Cm926oAlDMLJAhxiIRC3CrMZUBRknrkMiWpH-aUZvaFYXTTrNK0MRbdSqU_T40OhG7WFfBqpBt31fK3FGKfbm6a19OFVOAkx7YPg_xhIahg0nGMyTX_LYFVqS7BHAadxgLCrZAyG_X3Y_WfmtvSqISkHNfAnO53jTnDIaLOoDJjd5EDI6kTXieYf2MAWY-q-VI1_6BnVolCME7eTwjlMZWCtxWxs6_3bJCfQIOZ9tT7TjflGmMywPKIMHTYt2ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2e6046c.mp4?token=Jh4SgRXmB-g_Ma6W5GNgjW8uAOk1c4jRdvDZInt02sYSKhpQxzdF8H3Rq6lXQokm6uHPYEQkKmZKucMGZgn1RY4Cm926oAlDMLJAhxiIRC3CrMZUBRknrkMiWpH-aUZvaFYXTTrNK0MRbdSqU_T40OhG7WFfBqpBt31fK3FGKfbm6a19OFVOAkx7YPg_xhIahg0nGMyTX_LYFVqS7BHAadxgLCrZAyG_X3Y_WfmtvSqISkHNfAnO53jTnDIaLOoDJjd5EDI6kTXieYf2MAWY-q-VI1_6BnVolCME7eTwjlMZWCtxWxs6_3bJCfQIOZ9tT7TjflGmMywPKIMHTYt2ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي : ‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88645" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88644">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/497a3df8c4.mp4?token=eeUzR8sNNauciqzO3JsbIq82Y3CUZ7PVIFrKzpJtXjyE23YI-4DL39Ar5EHj5zq7V6Vhr0oMSdNsZdk-zGPKLR5nD2Fh1GT_wjKdHD4aHxXoEtsTKWGUxOXwroQ8wwBdU2YCX6tSSBoFGwPscJ2-NpCXab_hMFSKCfQusPi0lbtHTmAK05sJF-XVOImk1GVaHjhsOsH7a--oiGmkieh0qC2-QC0ZYbJssxJp1VyKw3b82fHcbTIFjj8m8ApvgmSy9xiTM_IzxetRkHqq1nH4clyL46b8fOdeMqC_JfM_g29SM0cJmjNVFNGu7x2v2-xgsbciVh8CQ2UOqi1ShVETfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/497a3df8c4.mp4?token=eeUzR8sNNauciqzO3JsbIq82Y3CUZ7PVIFrKzpJtXjyE23YI-4DL39Ar5EHj5zq7V6Vhr0oMSdNsZdk-zGPKLR5nD2Fh1GT_wjKdHD4aHxXoEtsTKWGUxOXwroQ8wwBdU2YCX6tSSBoFGwPscJ2-NpCXab_hMFSKCfQusPi0lbtHTmAK05sJF-XVOImk1GVaHjhsOsH7a--oiGmkieh0qC2-QC0ZYbJssxJp1VyKw3b82fHcbTIFjj8m8ApvgmSy9xiTM_IzxetRkHqq1nH4clyL46b8fOdeMqC_JfM_g29SM0cJmjNVFNGu7x2v2-xgsbciVh8CQ2UOqi1ShVETfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: بوتين لن يهاجم أراضي الناتو، لقد تصرفت روسيا بشكل جيد للغاية فيما يتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88644" target="_blank">📅 21:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88643">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ae436795.mp4?token=uWS5IDTeFmHEOGkpMH_8NRAJiRZwj9UxvOLHmlFEtS2tvAqMvhPNwLCCmYqvb1B0vdvcBm0jO3rTW2g5531wultXV37O1UkkBcBvJHi8RkJBZU_Bmu4qgCn9vdlpaDJ1zxVL1RcIkFY445XjiiF547hoUBOVJjqbFci_EAU98Zp2w92JGO-ptD9fDyjnN9s9nfDcUxUq-04XLqvdM0NWpaD3Q8ThMjObxYY_6JdxXEz3cevXrJZKFexIDKa3HvRy6p6GqdHcpjmaLIHkQfDMuYitatD9zP3vKifmian_CLBTxUqPLwN-wiqZm0u-DFir9guatGfKe7FcCbA6L83wMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ae436795.mp4?token=uWS5IDTeFmHEOGkpMH_8NRAJiRZwj9UxvOLHmlFEtS2tvAqMvhPNwLCCmYqvb1B0vdvcBm0jO3rTW2g5531wultXV37O1UkkBcBvJHi8RkJBZU_Bmu4qgCn9vdlpaDJ1zxVL1RcIkFY445XjiiF547hoUBOVJjqbFci_EAU98Zp2w92JGO-ptD9fDyjnN9s9nfDcUxUq-04XLqvdM0NWpaD3Q8ThMjObxYY_6JdxXEz3cevXrJZKFexIDKa3HvRy6p6GqdHcpjmaLIHkQfDMuYitatD9zP3vKifmian_CLBTxUqPLwN-wiqZm0u-DFir9guatGfKe7FcCbA6L83wMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: بوتين لن يهاجم أراضي الناتو، لقد تصرفت روسيا بشكل جيد للغاية فيما يتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88643" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88642">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db380e2cda.mp4?token=hRy37RrV3U6sf1xAxyWSDj8LEjD3sl6OUGSITBFQrtNGez_ej23pCqHq4PcpCPBbaqiCQlZ3weDVDUuScVmmmaBZqSGmddKXVdx9IaYj6J2xxBhoDcnC_d29I3BvAa1gwDiMYmZaXexBk7pmrLl5pabLhNLqy96JZJKeG3ivXN6Xl8I4QjXSH2BCIQ2-oCJfEQfh2uPJdpNF60kcQ4lL0lyNw8A1QK7s7IR6xNesWjJm1tOouZiQj-VPhLPeTm3hiXy2S0V7hJVEYSkVxLP1_5CGBUeY4S5Fv8gFlZ2qA7gvxDbWmL8VFUw7aXUosvRi0MywcZ0gwKNM9axiHITUqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db380e2cda.mp4?token=hRy37RrV3U6sf1xAxyWSDj8LEjD3sl6OUGSITBFQrtNGez_ej23pCqHq4PcpCPBbaqiCQlZ3weDVDUuScVmmmaBZqSGmddKXVdx9IaYj6J2xxBhoDcnC_d29I3BvAa1gwDiMYmZaXexBk7pmrLl5pabLhNLqy96JZJKeG3ivXN6Xl8I4QjXSH2BCIQ2-oCJfEQfh2uPJdpNF60kcQ4lL0lyNw8A1QK7s7IR6xNesWjJm1tOouZiQj-VPhLPeTm3hiXy2S0V7hJVEYSkVxLP1_5CGBUeY4S5Fv8gFlZ2qA7gvxDbWmL8VFUw7aXUosvRi0MywcZ0gwKNM9axiHITUqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي عن ترامب: غير قلق على الإطلاق" بشأن احتمال قيام روسيا بمهاجمة حلف شمال الأطلسي (الناتو).</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88642" target="_blank">📅 21:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88641">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c2bbd3a1.mp4?token=DG6xhQSdgtVKR08qV-INUG22Tuya5bPO2W51bjyF8E3Kdk4kagCruIwHRs7GRcFZZ8m1U5c69vYI1_QXfBDjM12DDRaD8xIvG7WNixkqGsJtefnq4fTlqZeFGyrY9OYvYRNMF3q_qmj2WqM5hhV1mBu5fU6TuAlgtZvAntYnwXvzrhT5L-z7988yLO51XbkQqKVWBHfgHnnh08rIDd4CMABxd--l3_eBbclXMk4E24NG7j3zumkhbDG14KudIg83xIeCx5dAn-twjquDfiMjDrNMiiS8F_MlJdT0MBeXXF0wsadms3QP0XTcl_5T7K_SULQhTEcAlMe0Bc5QT9I0hA-QUj3bwvBgsJE4o52kQtUpiU6b3KaKlr3AtEFuE7iW68rHveGmjAFVvdaDLGN3R5jmOwIS1M3aLY-1g3TzzXU1rWZqqndcMPZ2MoD62dbifISomd6o7m2b2Nncka_9Rx_jTPF9B88ny1h82p1nQvuwI6zb50oSuHKDLPHq7FbfI3Xh4rmOunKRht_X-Rg1zNMfNEHOQvD1lf-DtcytyTzPrANfeFJqlZcYHi8lSBaqgoR-y753OFmNkpKlUHXiYI6czaH2l6jrMRuW-DE3jAbhXxWo3MdWOenvrATLKRFctQGen0EpjjQ7dEfewB3vxt-rh-wnXllSg3cSBzCwu9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c2bbd3a1.mp4?token=DG6xhQSdgtVKR08qV-INUG22Tuya5bPO2W51bjyF8E3Kdk4kagCruIwHRs7GRcFZZ8m1U5c69vYI1_QXfBDjM12DDRaD8xIvG7WNixkqGsJtefnq4fTlqZeFGyrY9OYvYRNMF3q_qmj2WqM5hhV1mBu5fU6TuAlgtZvAntYnwXvzrhT5L-z7988yLO51XbkQqKVWBHfgHnnh08rIDd4CMABxd--l3_eBbclXMk4E24NG7j3zumkhbDG14KudIg83xIeCx5dAn-twjquDfiMjDrNMiiS8F_MlJdT0MBeXXF0wsadms3QP0XTcl_5T7K_SULQhTEcAlMe0Bc5QT9I0hA-QUj3bwvBgsJE4o52kQtUpiU6b3KaKlr3AtEFuE7iW68rHveGmjAFVvdaDLGN3R5jmOwIS1M3aLY-1g3TzzXU1rWZqqndcMPZ2MoD62dbifISomd6o7m2b2Nncka_9Rx_jTPF9B88ny1h82p1nQvuwI6zb50oSuHKDLPHq7FbfI3Xh4rmOunKRht_X-Rg1zNMfNEHOQvD1lf-DtcytyTzPrANfeFJqlZcYHi8lSBaqgoR-y753OFmNkpKlUHXiYI6czaH2l6jrMRuW-DE3jAbhXxWo3MdWOenvrATLKRFctQGen0EpjjQ7dEfewB3vxt-rh-wnXllSg3cSBzCwu9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يعثر على موضوع غير تدمير القوة البحرية والجوية والبرية الايرانية...
وقع  ترامب أمرًا تنفيذيًا "يغير" اسم بحيرة أونتاريو الكندية إلى "بحيرة أمريكا".</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88641" target="_blank">📅 20:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88640">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي عن ترامب:
غير قلق على الإطلاق" بشأن احتمال قيام روسيا بمهاجمة حلف شمال الأطلسي (الناتو).</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88640" target="_blank">📅 20:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88639">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYIC6lO3r7iR0MBGrIx82nyCBWV0GWdYqiW3z4e0JZ7P4wgsDBe82m5sDmX7vYFP39NBwfIjacWK6GS4612E9GWqFaMI-R5HC8xrzxthzSz3OUwi508XhzIdgPxDrGRT6P7Tr0wosaYauwstUbClUzC5miQmJ6V449vOStB0tfQfJ3KtlxC8ltytwhhcRTdjtosv4t5GjN_8WvFUFD_9_WtS3b12lG178tPQnIfPzFx6Q81-0q8WmiwpAfw0hZQgzrlyKKzQ0c_cGFydmRbJuw8Rlt-h7PivpzUIqBMzCNRINqz8FprohYOX6QXGUz76nXUfPs7W_yPtTXy6Zs3uiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
بدلاً من ضخ مليارات الدولارات إلى وكيلها الإرهابي، إسرائيل، و750 قاعدة عسكرية، كان بإمكان هذه الإمبراطورية الفاشلة إنفاق تلك الأموال على شعبها، لكن لا، سيكون ذلك منطقياً للغاية بالنسبة لهذا النظام.
‏يا سكوتي، يا رجل، مصداقيتك على المحك. افعل شيئاً.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88639" target="_blank">📅 20:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88638">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
أمين مجلس الأمن القومي الإيراني رضائي:
إذا بدأت أمريكا أي عمل ضدنا فستحل كارثة على مصالحها العسكرية والاقتصادية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88638" target="_blank">📅 20:24 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
