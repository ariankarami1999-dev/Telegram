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
<img src="https://cdn4.telesco.pe/file/F8C--9F5toJF6s-p_nAMtdGK3sZs1GV8kAWQuObXBPbRh7XrXbR485BENluvC3Uydk7OrdCboIiQJSuWIaS-WSbqqsri8U7N9k6dENxRb6q2CP-2UOJ7pzfAfU_30ksG3pmy6D0Bfs7XuNLlIaA-ygmcsHyUKvSawDVi154t_BDk3yK2LNz3BiSNeePaVhCx-alM-abJ4BR1DKXxLhoIrRLUduKw4VLVNKcifXqm1zbNzRrYZG_-eINwTxpDJb032YfFE5yHtj4JcSrN5wcEjJWRsSABopSc1IXOnGrGBHL69c7rUlYbkd8IsT2NyzQAk7P-K-Fg1p3bxULcSjYoUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-85868">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزير الحرب الصهيوني المجرم كاتس متفاخرا: اليوم، لم يعد هناك حي "الشجاعية" في غزة، ولم يعد هناك مخيم "جباليا". كل تلك الأماكن لم تعد موجودة. لقد قال رئيس القيادة الجنوبية لي: "لا أرى أي منازل، بل أرى شاطئ البحر." لقد دمرنا غزة. في غزة، نحن ندمر ليس فقط ما هو…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/naya_foriraq/85868" target="_blank">📅 13:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85867">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزير الحرب الصهيوني كاتس: تم تكليف "الشاباك" لحماية نتنياهو والقيادة السياسية والعسكرية الإسرائيلية من التهديد الايراني الخطير.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/naya_foriraq/85867" target="_blank">📅 13:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85866">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني يهاجم اردوغان: نحن لسنا الإمبراطورية المسيحية المتهاوية. القدس ليست القسطنطينية، التي غزوتموها عندما أسسستم الإمبراطورية العثمانية. لا تحاولوا استفزازنا. نصيحتي لأردوغان هي ألا يحاول استفزازنا، وألا يضع نفسه في الموقف الذي وضعته فيه إيران.…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/naya_foriraq/85866" target="_blank">📅 13:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85865">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هل سترد اسرائيل على الطائرة المسيرة التي أُطلقت في وقت سابق من اليوم من العراق؟!
🇮🇱
وزير الحرب الصهيوني كاتس: نحن نعرف كيف ندير الأمور - نحن مستعدون.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/naya_foriraq/85865" target="_blank">📅 13:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85864">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
صرف رواتب مجاهدي هيئة الحشد الشعبي.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/naya_foriraq/85864" target="_blank">📅 13:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85863">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇱
🇮🇶
إعلام العدو عن مسؤول أمني: الطائرات المسيرة التي أسقطها الجيش يوم الأمس واليوم على الحدود مع الأردن، أطلقت من العراق.</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/naya_foriraq/85863" target="_blank">📅 13:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85862">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7bffd9c2.mp4?token=nA-p1K0-yeGT24rj2k9LHHhFUtrnIG0TCtiwD-8rihLdJOYERv9kU9XKPFZdAO1e3sQw9xrcZCY3xLtOVESuSdaP1Rip_xSgePbjbuzogpjvbxxSSq6NYdrwqeRNr9HUQqcbGdqELHqaEGYaHsI2I-Ab2UM7FPKvbZLkoInhE8BoUIWV8RJtPsWJvD_d4-YCVrjmxMw21uof_87Z-oBjnYUWG5sPF4pPbVYeW5OMzguUQ8YnS5uJPsWz_8ByABws5AYhVRLQ6YjO3dIVl9Kd6U6x2l0WeZ2jB5DkCpSDawE1HW64er0__qazG7SZrvq4Vs7tT77Ds9lYuC1TgyrAXULCIbG6gVtx9kuEuKzDMdX4fn1hoDWdLQwIamQ7OryofTq6RiFWJEmWB3g7giEAMycG37-M4nQEoDzojZQQGQBL137FYT8Sv1oohmi6W0EchIdALCZYxXd-UfcxJko6cMw6jqcaaoN0wBoU712iehgFrxBLLXZ-DblAudEbs9LaLlfyLRSX6h_Qk1gbVXoJW8phw-Pi3nI5gesjmi9xN91D2nTIFYAc9-9Sl9s8RggST4s2us2W3tRcl1tBH3deE7sUhtsgIHZ5lhi_6NVBD4K5IiLA5tRqC6z5cjgYnbzR8b0zm5VPP4042oqeUXbBeB_4RZUvRFgkIfEHfEsmLEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7bffd9c2.mp4?token=nA-p1K0-yeGT24rj2k9LHHhFUtrnIG0TCtiwD-8rihLdJOYERv9kU9XKPFZdAO1e3sQw9xrcZCY3xLtOVESuSdaP1Rip_xSgePbjbuzogpjvbxxSSq6NYdrwqeRNr9HUQqcbGdqELHqaEGYaHsI2I-Ab2UM7FPKvbZLkoInhE8BoUIWV8RJtPsWJvD_d4-YCVrjmxMw21uof_87Z-oBjnYUWG5sPF4pPbVYeW5OMzguUQ8YnS5uJPsWz_8ByABws5AYhVRLQ6YjO3dIVl9Kd6U6x2l0WeZ2jB5DkCpSDawE1HW64er0__qazG7SZrvq4Vs7tT77Ds9lYuC1TgyrAXULCIbG6gVtx9kuEuKzDMdX4fn1hoDWdLQwIamQ7OryofTq6RiFWJEmWB3g7giEAMycG37-M4nQEoDzojZQQGQBL137FYT8Sv1oohmi6W0EchIdALCZYxXd-UfcxJko6cMw6jqcaaoN0wBoU712iehgFrxBLLXZ-DblAudEbs9LaLlfyLRSX6h_Qk1gbVXoJW8phw-Pi3nI5gesjmi9xN91D2nTIFYAc9-9Sl9s8RggST4s2us2W3tRcl1tBH3deE7sUhtsgIHZ5lhi_6NVBD4K5IiLA5tRqC6z5cjgYnbzR8b0zm5VPP4042oqeUXbBeB_4RZUvRFgkIfEHfEsmLEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇺🇸
وزير الحرب الصهيوني كاتس:
نريد جدا معاودة شن الحرب على إيران لكن الولايات المتحدة تمنعنا، طائرات أميركية تشن غارات في إيران انطلاقا من مطارات إسرائيلية.</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/naya_foriraq/85862" target="_blank">📅 12:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85860">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51c4750bb.mp4?token=i5Mw7LOn67ZWW9giA_E3s_mPDHHW2GNBjZUl6rj6Ywu_zU5TgQb-N4bRQX914ZvtQw7YPeIMuoFEiEvkWL5YY-m5TAzNrdo15FnxVgiagtw3IrwNcim994fw_By7Sb68j2P4HZgxWP0E5icSnvIx1IJbZ-KZc615aU1HmMDTxOGqdpS0GEavRvPq2Wq4r49tQiXHgfZ7QgKhwhhTmkg4TT1ReMhK79yxYcSgoY_aq3HNPHLLXDclbISNC9Naq5Lwt2VZD7J9OGmHwL-EO1B-mtktuK_Cza_eQDe3xL6QqpidGWb0HI_w9S_7ZrNIC90P2QuK6Fh7SW_eVExNOyVMHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51c4750bb.mp4?token=i5Mw7LOn67ZWW9giA_E3s_mPDHHW2GNBjZUl6rj6Ywu_zU5TgQb-N4bRQX914ZvtQw7YPeIMuoFEiEvkWL5YY-m5TAzNrdo15FnxVgiagtw3IrwNcim994fw_By7Sb68j2P4HZgxWP0E5icSnvIx1IJbZ-KZc615aU1HmMDTxOGqdpS0GEavRvPq2Wq4r49tQiXHgfZ7QgKhwhhTmkg4TT1ReMhK79yxYcSgoY_aq3HNPHLLXDclbISNC9Naq5Lwt2VZD7J9OGmHwL-EO1B-mtktuK_Cza_eQDe3xL6QqpidGWb0HI_w9S_7ZrNIC90P2QuK6Fh7SW_eVExNOyVMHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مسير مجهول الهوية يحلق في اجواء مدينة الناصرية جنوبي العراق</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/85860" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85859">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇱
🇮🇶
إعلام العدو عن مسؤول أمني: الطائرات المسيرة التي أسقطها الجيش يوم الأمس واليوم على الحدود مع الأردن، أطلقت من العراق.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/85859" target="_blank">📅 11:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85858">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇱
🇮🇶
إعلام العدو عن مسؤول أمن
ي: الطائرات المسيرة التي أسقطها الجيش يوم الأمس واليوم على الحدود مع الأردن، أطلقت من العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85858" target="_blank">📅 10:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85857">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
قيادي في حزب المعارضة الإيراني
: تعرضت مقراتنا في وادي آلانة لهجوم ب 5 طائرات مسيرة على الأقل فجر اليوم.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85857" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85856">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
🇮🇷
🇮🇱
🇦🇪
فايننشال تايمز:
مع انهيار وقف إطلاق النار الهش بين الولايات المتحدة وإيران، قامت الإمارات العربية المتحدة بمقامرة جريئة: إعادة تنشيط القنوات الدبلوماسية والاقتصادية مع إيران وإعادة الخطوط الجوية الإيرانية و ٢٠ الف مقيم بشكل مؤقت مع مضاعفة العلاقات العسكرية مع إسرائيل والولايات المتحدة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85856" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85855">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">إعلام أمريكي: سلطنة عُمان قدمت لإيران مقترحاً لآلية إقليمية مشتركة لإدارة مضيق هرمز تعتمد على رسوم طوعية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85855" target="_blank">📅 09:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85854">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇱
إذاعة جيش الاحتلال: الجيش الإسرائيلي قلّص عدد الجنود في كتيبة احتياط على الحدود اللبنانية بنسبة تقارب 30٪ مقارنة بالعدد الأصلي ؛ وأوضح قائد الكتيبة أنهم يواجهون أزمة حادة في عدد الأفراد تؤثر على قدرتهم على أداء المهام.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85854" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85853">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85853" target="_blank">📅 08:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/85852" target="_blank">📅 08:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85851">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات عنيفة تهز المنطقة الشرقية من السعودية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85851" target="_blank">📅 08:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85850">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات عنيفة تهز المنطقة الشرقية من السعودية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85850" target="_blank">📅 08:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85849">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b37b70352.mp4?token=NNzNeAJZ7bHeU1ac4uL9bUfwWaFBEJUcwLDsO-Kk1_5NIbHgY2TcKZaSIu8ejQdinhOsBEZHMYVqO9iluDHD9e1kofjsn8V9tFSS9HzSlDCqcHOBTjO55a7jpWfcPjVFO7AmCYpJaNQiiScwors84s-T_zv2RJwTyR0IfXXkgYYuchLMOvjqTRPiEM9fmWEpPTqhGjL99Ka6A2RYRw_5WKE0SdX0XWCHA-aHA1UYAtvUyiGVyVcXkJ67iPu6f0Otcv5pYzqekQENrTpDuwFuGqbe-sR5Z156pv1ppZhuoVtZLBg29rW-0RTniH5AJ1ioaZrYfuJVf3oVAPg4nYNvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b37b70352.mp4?token=NNzNeAJZ7bHeU1ac4uL9bUfwWaFBEJUcwLDsO-Kk1_5NIbHgY2TcKZaSIu8ejQdinhOsBEZHMYVqO9iluDHD9e1kofjsn8V9tFSS9HzSlDCqcHOBTjO55a7jpWfcPjVFO7AmCYpJaNQiiScwors84s-T_zv2RJwTyR0IfXXkgYYuchLMOvjqTRPiEM9fmWEpPTqhGjL99Ka6A2RYRw_5WKE0SdX0XWCHA-aHA1UYAtvUyiGVyVcXkJ67iPu6f0Otcv5pYzqekQENrTpDuwFuGqbe-sR5Z156pv1ppZhuoVtZLBg29rW-0RTniH5AJ1ioaZrYfuJVf3oVAPg4nYNvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد أخرى لحظة حدوث الانفجارات في أحد مخازن الأسلحة التابعة لحزب المعارضة الإرهابي في محافظة السليمانية شمال العراق.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85849" target="_blank">📅 07:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85848">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇱
🇺🇸
هارتس العبرية: ‏يزور نتنياهو ترامب اليوم وهو يملك عدداً أقل من الحلفاء وخيارات غير جيدة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85848" target="_blank">📅 07:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85847">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇨🇳
زلزال بقوة 6 درجات يضرب مقاطعة تشينغهاي في الصين.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/85847" target="_blank">📅 07:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85846">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a50630e63.mp4?token=eBqHznnBNUkhTkFypf8vyi_kVEQbPeEMQGyF7hdhvhpwb9PI8GlPICZGR-LZ1or6UPE-zNfAayaWIIhhRJ3PfVesf41X6OR47e8PBZIx-O_fAKUbWak6DXvx5Cg54-pKVk2NCZ3r0ZNeM0cIQfbt-Vgk20XxEh1TRDVml85803hxrIJCGK0lVmUpr38zG-Yit4PsonNPSkyHFnR4Y1KVG1BGS__CFyhhY3GKijBXUhtPGf7SjFWgTCuS7V9ubH88DMYAuCd4SSTZZYANNVAPcx780az7Hym5zS5EbQXqKTAa3mujQQTBjFuEzDswlxmyeYDDzaQ0BQH7oAK5MJwE3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a50630e63.mp4?token=eBqHznnBNUkhTkFypf8vyi_kVEQbPeEMQGyF7hdhvhpwb9PI8GlPICZGR-LZ1or6UPE-zNfAayaWIIhhRJ3PfVesf41X6OR47e8PBZIx-O_fAKUbWak6DXvx5Cg54-pKVk2NCZ3r0ZNeM0cIQfbt-Vgk20XxEh1TRDVml85803hxrIJCGK0lVmUpr38zG-Yit4PsonNPSkyHFnR4Y1KVG1BGS__CFyhhY3GKijBXUhtPGf7SjFWgTCuS7V9ubH88DMYAuCd4SSTZZYANNVAPcx780az7Hym5zS5EbQXqKTAa3mujQQTBjFuEzDswlxmyeYDDzaQ0BQH7oAK5MJwE3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات ثانوية عنيفة في مخازن السلاح التابعة لإرهابيي المعارضة الكردية الإيرانية في محافظة السليمانية شمال العراق.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85846" target="_blank">📅 06:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85845">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
تصاعد أعمدة الدخان من داخل مقر تابع للإنفصاليين الأكراد في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85845" target="_blank">📅 06:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85844">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الصهيوني:
إعتراض طائرة مسيرة عند الحدود الأردنية؛ التحقيقات تجري لمعرفة مصدر إطلاقها.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/85844" target="_blank">📅 06:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85843">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI5ZXFB1fcASmCjAAh6rUsdqoiFlfk6lDtZnK4onzDzVZ3l9GpBCM9GIgygsYIIo4H133udfjPIbZ1bDcTsZHHGMZdsvPIcAkOGAZaivREXLlawKS2kwwa686y7WGyYIrQMQg45S1FSqDHCQV7PFpqzOrFSSHU-UKX5EZbAmC-9F9z_eh8333cl83RJL8vWXm7CPXmVReIl-jVryOy5jMUcG8K8zS1dF8XPpBtmY9RRnL_SNm-rMc4UIi6iPBiuVnqcf9PWzpbsZQ74co8RWYvG8P3xitTXBHSilmQ8wbJko-rQFEetBbpiO-BeYzh3-Ff3WMsj7m8JmnE3M6I6vzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مع أول ساعات الصباح.. إستهداف أحد مقرات المعارضة الكردية الإرهابية في محافظة السليمانية شمالي العراق بسرب من الطائرات الإنتحارية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85843" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85842">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
مع أول ساعات الصباح..
إستهداف أحد مقرات المعارضة الكردية الإرهابية في محافظة السليمانية شمالي العراق بسرب من الطائرات الإنتحارية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85842" target="_blank">📅 05:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85841">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صافرات الانذار في غلاف غزة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/85841" target="_blank">📅 05:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85840">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
مسؤول أميركي:
العقوبات والحصار البحري الأميركي سيستغرقان وقتا أطول لإجبار طهران على الجلوس إلى طاولة المفاوضات.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85840" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85839">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2655270d3.mp4?token=B0v1zV4jxtZuKxJsScaLgykrlSsGz4H1wmn1q_upj9lComepIAnnmImP_s9c0UZJgR68qaMs0glWdPLEMF50IYGCpki_-MX_0jfS_gQWcxT2QFy-NFYs1t5PeheNPk7Zpb6JCnbWOkVk2YVaCCV8wDeCpkWRPPcRNEJqTlKSkoc0ojYc466hsKknUbA-g5jruiVtarmKiSU5RhLNccF0Ms9HWP8YJRJ4sNLVm9Nl-DUgKzVpbyevvQbZrT-oHepjMyHcpORGYALeJQtGycWZaRV_CzIT7n__xDDFnr_06GygMowmeTmnqHGNJPhI9u_1CX2-Wj-M4mf9n9LEffmk7xXkqlr37dDFi9xREq8qy0LpjM2jvb6U3JkT4-F2KFDpfOKY_8O6M8gUOMktaeURsU2Wy_Z9fC4nbGkk3bR7OttWfy-3NDsh_8IvTI3jh--VKCNQOhZ_IO4rWuGWV00UM_LZo6FaJnvTgKeEDAwEqwKPRabP_vMCBULMwV8rR-pvCK1AOzk0j9mQN0tjQ2sc64NnPW2i2aTov0ow45F06erdnLohyffuK2-RRYNmAOXAeIZjbJWj94sFeyhuwVZe2twmch1SH46yITz26cuDA3g5eZBQpFFhwDM3cO0i9kCd1MbdFGjl19AM9p4gn_6-zHmT7OjzpaTKXyEXymxHmU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2655270d3.mp4?token=B0v1zV4jxtZuKxJsScaLgykrlSsGz4H1wmn1q_upj9lComepIAnnmImP_s9c0UZJgR68qaMs0glWdPLEMF50IYGCpki_-MX_0jfS_gQWcxT2QFy-NFYs1t5PeheNPk7Zpb6JCnbWOkVk2YVaCCV8wDeCpkWRPPcRNEJqTlKSkoc0ojYc466hsKknUbA-g5jruiVtarmKiSU5RhLNccF0Ms9HWP8YJRJ4sNLVm9Nl-DUgKzVpbyevvQbZrT-oHepjMyHcpORGYALeJQtGycWZaRV_CzIT7n__xDDFnr_06GygMowmeTmnqHGNJPhI9u_1CX2-Wj-M4mf9n9LEffmk7xXkqlr37dDFi9xREq8qy0LpjM2jvb6U3JkT4-F2KFDpfOKY_8O6M8gUOMktaeURsU2Wy_Z9fC4nbGkk3bR7OttWfy-3NDsh_8IvTI3jh--VKCNQOhZ_IO4rWuGWV00UM_LZo6FaJnvTgKeEDAwEqwKPRabP_vMCBULMwV8rR-pvCK1AOzk0j9mQN0tjQ2sc64NnPW2i2aTov0ow45F06erdnLohyffuK2-RRYNmAOXAeIZjbJWj94sFeyhuwVZe2twmch1SH46yITz26cuDA3g5eZBQpFFhwDM3cO0i9kCd1MbdFGjl19AM9p4gn_6-zHmT7OjzpaTKXyEXymxHmU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من تصدي دفاعات الإنفصاليين لهجوم أسراب المسيرات الانتحارية على مقراتهم في أربيل
😆</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85839" target="_blank">📅 01:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85837">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293704c82e.mp4?token=Auy1zGv50CyW0woO7CJSZa_l_6jQyBSH1o9W814LPWRqs1G0novfhZc7UHVI061xSZcLmE0GlvvjxmIfaxw2L3OXSU4RB_cvsBCOlwP5UmaQPMm65xKOw5Q_wlM2ZEZzbjIPcY8xihnqLNpWNbuE0IQWUqgOEDCzHP5SZel2gwFvlM4a7jTXGq13aI-3IzhRgfgC2hN7SieZChMQ0gRWSBzNy0Ycqzde8Ly7NiMWWcO8ySuj4H02-FxwS1XxPMFqvkviyNF4R8eEJNg_XsEzu3jmRq0fvLIKk0kEk8QZOijK8WY__aMA_k9ZTEGDuJSYWzkd2yNS_4GjLdi91Whlfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293704c82e.mp4?token=Auy1zGv50CyW0woO7CJSZa_l_6jQyBSH1o9W814LPWRqs1G0novfhZc7UHVI061xSZcLmE0GlvvjxmIfaxw2L3OXSU4RB_cvsBCOlwP5UmaQPMm65xKOw5Q_wlM2ZEZzbjIPcY8xihnqLNpWNbuE0IQWUqgOEDCzHP5SZel2gwFvlM4a7jTXGq13aI-3IzhRgfgC2hN7SieZChMQ0gRWSBzNy0Ycqzde8Ly7NiMWWcO8ySuj4H02-FxwS1XxPMFqvkviyNF4R8eEJNg_XsEzu3jmRq0fvLIKk0kEk8QZOijK8WY__aMA_k9ZTEGDuJSYWzkd2yNS_4GjLdi91Whlfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق يظهر لحظة وصول المسيرة الانتحارية إلى هدفها والانفجار الكبير داخل مقر الانفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/85837" target="_blank">📅 01:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85836">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a1c105dc2.mp4?token=f2lTVQcoNWalBbZk_MHF0iYl58qPogC3M6kfJzVCO7ZObv-2ivyp9_KFB3mn85Q7zu8_DddH_J-GHRfWtGhl1bUgTr9u2EVwtlUS88ZcajHt25QmWynTzWFig-tq2PTcp1RTfh0Hopa1M0l507v4nCE-7sed8_jmxb_6TSESNbzAvxHRXhY7_UdwBlhPvS0smrBSYHQoB062jlT9X5uFXDzZj3CqvHQsz0U5Z97LoF0xaVE9V1CcQkHFSHm4rVz45ZeKCFrmy3BTrmx0H44PNYRIWCAa2BX285cESAaecFbrjLnw2pMgD0iiyWikuORICmaakm1suJ8CNihhFwI0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a1c105dc2.mp4?token=f2lTVQcoNWalBbZk_MHF0iYl58qPogC3M6kfJzVCO7ZObv-2ivyp9_KFB3mn85Q7zu8_DddH_J-GHRfWtGhl1bUgTr9u2EVwtlUS88ZcajHt25QmWynTzWFig-tq2PTcp1RTfh0Hopa1M0l507v4nCE-7sed8_jmxb_6TSESNbzAvxHRXhY7_UdwBlhPvS0smrBSYHQoB062jlT9X5uFXDzZj3CqvHQsz0U5Z97LoF0xaVE9V1CcQkHFSHm4rVz45ZeKCFrmy3BTrmx0H44PNYRIWCAa2BX285cESAaecFbrjLnw2pMgD0iiyWikuORICmaakm1suJ8CNihhFwI0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في القنصلية الامريكية بمحافظة أربيل</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85836" target="_blank">📅 01:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85835">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c75dde8d.mp4?token=QISmL5LtPsrB8dM8NtzTcpf55eXfE1UQGCtUdSUL1dB_7WnH2pEWipeTnyjc2j4GlYwgxNKfladHWDbEZYNpNoEvUMFSbKWieqEZVTv9a1Avif0O6HN33NBlpDiVdPB3FcshjYRlR3v9wHuwHkylpj5oeXq1DchlRibn7j-yjcw5BZHPQcn9abTKxZNb5SloDA2WkGcD5XleSJjylxZavyxlH5-HAJPnDnesCcbaS1DywQomr38Gc7UzoMHZmyn1_9pFsqMe4REEfRs84zb89PujWwhvD4DqKkJ4uM2slQi1eFwOvoEfu5_zsCWhylpFa-GwWccZ0ijD0j4S4IO5Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c75dde8d.mp4?token=QISmL5LtPsrB8dM8NtzTcpf55eXfE1UQGCtUdSUL1dB_7WnH2pEWipeTnyjc2j4GlYwgxNKfladHWDbEZYNpNoEvUMFSbKWieqEZVTv9a1Avif0O6HN33NBlpDiVdPB3FcshjYRlR3v9wHuwHkylpj5oeXq1DchlRibn7j-yjcw5BZHPQcn9abTKxZNb5SloDA2WkGcD5XleSJjylxZavyxlH5-HAJPnDnesCcbaS1DywQomr38Gc7UzoMHZmyn1_9pFsqMe4REEfRs84zb89PujWwhvD4DqKkJ4uM2slQi1eFwOvoEfu5_zsCWhylpFa-GwWccZ0ijD0j4S4IO5Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في القنصلية الامريكية بمحافظة أربيل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85835" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85834">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇱🇧
🇮🇱
غارة صهيونية تستهدف تلة علي طاهر جنوبي لبنان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85834" target="_blank">📅 01:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85833">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbfd07761.mp4?token=YvzyomKIN3WIen7Fn3kpgHelHC3XBpbTdrCRPdJsDS9q4_j2UxuumKRgUDU9LzDuUhij8vnVKHky5WYfK6jjn_uPUot-vl33Lg7tbID582_h4NYzkYPcpiy7gQxh3CFm7epin6iXl0crIXkp9F_Kt9mdjp2CmRyKsZmor8-A2Y5qTZwQjsbi3wh4EgPji6Dzpr958J30zTZnoOncNlxSIhPy3PHYFsrS_F2074SLelobfP5dsaukWx-BZBURr3jFLbzkyuF0akli5w-f0Ys4techi-FT4X2Ig6RWiYXopZUh5Cj5SMYgOVDqZL99sdzjSZpS-VicRyaTH6Fs6rpHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbfd07761.mp4?token=YvzyomKIN3WIen7Fn3kpgHelHC3XBpbTdrCRPdJsDS9q4_j2UxuumKRgUDU9LzDuUhij8vnVKHky5WYfK6jjn_uPUot-vl33Lg7tbID582_h4NYzkYPcpiy7gQxh3CFm7epin6iXl0crIXkp9F_Kt9mdjp2CmRyKsZmor8-A2Y5qTZwQjsbi3wh4EgPji6Dzpr958J30zTZnoOncNlxSIhPy3PHYFsrS_F2074SLelobfP5dsaukWx-BZBURr3jFLbzkyuF0akli5w-f0Ys4techi-FT4X2Ig6RWiYXopZUh5Cj5SMYgOVDqZL99sdzjSZpS-VicRyaTH6Fs6rpHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق واسع جراء الهجوم المسير الانتحاري الذي طال مقرات المعارضة الكردية في محافظة دهوك شمالي العراق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85833" target="_blank">📅 01:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85831">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef242c138.mp4?token=tP39MY80Rg_eT8r4MViYrv8ShAHLqvGRI_XoqsO19FCsULzXEbePLKFNBsDk1LjinVtijDT0CV11To_HoEXDkJg8IbSzzb5-mgeRACRQeOC_9b8dtyhhbawGAKycgfHI7766Hbu4F7DrQMY6PUt9TWsWQJdbd6aROjsCxjZlLafKSnGcMOf1D1PGLa_7kE6IPlMzKuuXc4_MhUSsAEBm7lHL5wxlhPg46syDayFpaYZ0BiRpvSpSmtBuN1zSvfzW4cgFJfXZmXlpyuizzIHkGbr3A2RQExLhVGtkoCvT9V4X3RD2Vw4fMxebZzSwdZT2kvhDj6kJ6IjRlUmrPHUQtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef242c138.mp4?token=tP39MY80Rg_eT8r4MViYrv8ShAHLqvGRI_XoqsO19FCsULzXEbePLKFNBsDk1LjinVtijDT0CV11To_HoEXDkJg8IbSzzb5-mgeRACRQeOC_9b8dtyhhbawGAKycgfHI7766Hbu4F7DrQMY6PUt9TWsWQJdbd6aROjsCxjZlLafKSnGcMOf1D1PGLa_7kE6IPlMzKuuXc4_MhUSsAEBm7lHL5wxlhPg46syDayFpaYZ0BiRpvSpSmtBuN1zSvfzW4cgFJfXZmXlpyuizzIHkGbr3A2RQExLhVGtkoCvT9V4X3RD2Vw4fMxebZzSwdZT2kvhDj6kJ6IjRlUmrPHUQtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مباشر وانفجار عنيف أخر يطال مقر تابع للانفصاليين الأكراد في محافظة أربيل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85831" target="_blank">📅 01:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85830">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6577c5fe83.mp4?token=Bf9xrBwF6Jtq_f7yP_pvdmyFo2yVGXgLsrEtpB2bas5LkY40a3INk9ySuXXQCyhBq9HKYTbJFGCr17q7xyrsvuiIi9ckh_Au-nkEz7S4xwy7b4Jy2T_tyj1F0BGD6m8lShIr1XkroPCUlw0iigYhw1qQ9ibgyFa12_ctASvxIMj2kVlFJ16OwCBaTSozx602wF8XSd4i1RSg15fOw4q7WEbmiMlWQw-YwkQih6p8qM9Bg45AcrM0uQrpXu4anMgWRu3qnJeh80h9_lH-pZFVCYWwUamjxbSMFgX0PED5CQtJKetZxsQShgDHfJeC6ezyXBkeQEYS9RHUd2zOrMJuDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6577c5fe83.mp4?token=Bf9xrBwF6Jtq_f7yP_pvdmyFo2yVGXgLsrEtpB2bas5LkY40a3INk9ySuXXQCyhBq9HKYTbJFGCr17q7xyrsvuiIi9ckh_Au-nkEz7S4xwy7b4Jy2T_tyj1F0BGD6m8lShIr1XkroPCUlw0iigYhw1qQ9ibgyFa12_ctASvxIMj2kVlFJ16OwCBaTSozx602wF8XSd4i1RSg15fOw4q7WEbmiMlWQw-YwkQih6p8qM9Bg45AcrM0uQrpXu4anMgWRu3qnJeh80h9_lH-pZFVCYWwUamjxbSMFgX0PED5CQtJKetZxsQShgDHfJeC6ezyXBkeQEYS9RHUd2zOrMJuDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار الانفجارات العنيفة داخل مقرات المعارضة الكردية الإرهابية في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/85830" target="_blank">📅 01:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85829">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bba43befb.mp4?token=Gm-QpYkbeZ9W-wAQuVHAGPwDma6D8F_Uvr-kWkr_MGFfsloUkNFgLREN9Hal5OkkJ32LdZaY7hjja_YlQE0C4PeqBto3LyJ6hQsDGea9l5kQcvN58Bp6yEL9gI0s9MSMvbLYXmUrWChqFqiMhLY7QrAhR0zBREHvXyjezcC4N1fzriKZ0qtxyTjkxpDyslBbx5V7KNBb-3Bms01meNF7JfnBDlIwRck0d2DRS0aXbE5aSukw5LWVoWkRDlSBWy8pm7H48QMofkibeJEBXOrfIeVJVgb9bG_juOsMtkVlzzVi2PUxVqHWL0n0zdUcakwpdC9lyuHNFIdBvZthEn1e5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bba43befb.mp4?token=Gm-QpYkbeZ9W-wAQuVHAGPwDma6D8F_Uvr-kWkr_MGFfsloUkNFgLREN9Hal5OkkJ32LdZaY7hjja_YlQE0C4PeqBto3LyJ6hQsDGea9l5kQcvN58Bp6yEL9gI0s9MSMvbLYXmUrWChqFqiMhLY7QrAhR0zBREHvXyjezcC4N1fzriKZ0qtxyTjkxpDyslBbx5V7KNBb-3Bms01meNF7JfnBDlIwRck0d2DRS0aXbE5aSukw5LWVoWkRDlSBWy8pm7H48QMofkibeJEBXOrfIeVJVgb9bG_juOsMtkVlzzVi2PUxVqHWL0n0zdUcakwpdC9lyuHNFIdBvZthEn1e5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشوب حرائق واسعة داخل مقرات المعارضة الكردية الإيرانية في محافظة أربيل العراق عقب استهدافها بالطيران المسير الانتحاري.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/85829" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85828">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f8527a49.mp4?token=bSU3VvVu32uSuvKTsC9HUcg5d0u79fSv1hbgqVXTohZZiLfu0z0a2mt0dCrNdHztgGdBBsHungx84bKX4zM6o0q6XtSoA2MJtlnQkyvcX5aAI1gYsx2AOXJcKh1xokl4nl9gyf6Zq4C6QpqMzjnMcxsvd7xDxlwbrmTsxSWqYZEAOJUknkwgFCtQnyhXn_nvWuUvxDf7s6W0DDMQz21j4-m61Sdo0wFaTWzGKLVhHUAOMqLyWcZZ74VBIXFbRFm-xSJ8iGXKLMzzSyEYLUb_ij1SkndxAV8KwlCTbNsj-Ip1t9d4_eNpepSExWxDQCxq3ph691G_e77zvKINpbvGag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f8527a49.mp4?token=bSU3VvVu32uSuvKTsC9HUcg5d0u79fSv1hbgqVXTohZZiLfu0z0a2mt0dCrNdHztgGdBBsHungx84bKX4zM6o0q6XtSoA2MJtlnQkyvcX5aAI1gYsx2AOXJcKh1xokl4nl9gyf6Zq4C6QpqMzjnMcxsvd7xDxlwbrmTsxSWqYZEAOJUknkwgFCtQnyhXn_nvWuUvxDf7s6W0DDMQz21j4-m61Sdo0wFaTWzGKLVhHUAOMqLyWcZZ74VBIXFbRFm-xSJ8iGXKLMzzSyEYLUb_ij1SkndxAV8KwlCTbNsj-Ip1t9d4_eNpepSExWxDQCxq3ph691G_e77zvKINpbvGag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی در مقرهای تجزیه طلبان تروریست در اربیل عراق.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/85828" target="_blank">📅 01:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85827">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a82d562b.mp4?token=T1QCXLvI4xwdr9R_9A9fRr9v52f2LQB5oywS7VMGSjBRGa9uyUK6dlCh67KWpl646tVSGedERedi3SX0-XkOeu-Lzg-X3zXwQ7c_VGLMp4b3ogNOaThenrL-lfOwk5Px6IESQq2aU7jzrABe8qCuKm0L4mfllzV1NMdkwd6Kmsj156l6Ayo-OcsXE4RF7iZpdrySEGwboTR40dzqgAFpx_2s9TQuAgIlLyJllcKw29n4uvMjubGC-TDizQ-1Z3th30YGAQhWWQ56cDW_jWNIYcIOn1iz-pcOGMpYQIUbVcfD62Je-UgD6JupzNNz1ee5vdwHgx68fGEXtoEV_TQLEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a82d562b.mp4?token=T1QCXLvI4xwdr9R_9A9fRr9v52f2LQB5oywS7VMGSjBRGa9uyUK6dlCh67KWpl646tVSGedERedi3SX0-XkOeu-Lzg-X3zXwQ7c_VGLMp4b3ogNOaThenrL-lfOwk5Px6IESQq2aU7jzrABe8qCuKm0L4mfllzV1NMdkwd6Kmsj156l6Ayo-OcsXE4RF7iZpdrySEGwboTR40dzqgAFpx_2s9TQuAgIlLyJllcKw29n4uvMjubGC-TDizQ-1Z3th30YGAQhWWQ56cDW_jWNIYcIOn1iz-pcOGMpYQIUbVcfD62Je-UgD6JupzNNz1ee5vdwHgx68fGEXtoEV_TQLEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملیات لت و پار کردن تروریست‌های تجزیه طلب در شمال عراق ادامه دارد.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85827" target="_blank">📅 01:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85826">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3b235c206.mp4?token=VcL7fyJ0_R6To0dAB7vkHav-oEzszKC-JhaR5bl01sxOnqKwBP4uPvmdi8s3H3hQdWCrQACjfn_5O2lKytAQ-Hz94aU2OEAMUSWA92X_frebc_5ZhxTSef6qUklhemTgM8F9BPFjcH6TO4VQff6EWbWq0lR-Ts1-iBvJmaWw4HouDuCHOmLBMnf-Om_Zsr6JyV5_T6K1SUAN7O8uJHzuhpC9Ixxw0Xcl4JmE7ZICV38mCkxpu9im5KFFfOxq0LYz5sKCLkeR250fnQG58--CUS0PdaDFoRtS8VGUv_9YGZ0qf2ohx3ImHhZXNcEBfl3aiUNGplrUqm13ysok3iDG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3b235c206.mp4?token=VcL7fyJ0_R6To0dAB7vkHav-oEzszKC-JhaR5bl01sxOnqKwBP4uPvmdi8s3H3hQdWCrQACjfn_5O2lKytAQ-Hz94aU2OEAMUSWA92X_frebc_5ZhxTSef6qUklhemTgM8F9BPFjcH6TO4VQff6EWbWq0lR-Ts1-iBvJmaWw4HouDuCHOmLBMnf-Om_Zsr6JyV5_T6K1SUAN7O8uJHzuhpC9Ixxw0Xcl4JmE7ZICV38mCkxpu9im5KFFfOxq0LYz5sKCLkeR250fnQG58--CUS0PdaDFoRtS8VGUv_9YGZ0qf2ohx3ImHhZXNcEBfl3aiUNGplrUqm13ysok3iDG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق للحظة إستهداف مقر تابع للإنفصاليين في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85826" target="_blank">📅 00:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85825">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/decaacf8b1.mp4?token=PhixCQ-HlO5kNvSy8xVCa9z1mInNXemD9_MEn78ShO8zZZpysPqWcBaxaRZYrVM8UEG6DPpepouCkZvO1iGItdwrMTGTTpyj0MYPLhP1zubyCuCLW_oFjsFcV1BbYhDy2LuGU5kMiR-Ywr9NN9knmcR1bNvJJwkHPKm01efeG6HIXn9in2Hm5doEhFcnRFviOaoFt1hHxxE7-kPtsdg2jkGfhTgv9vmR8cJx5ykkJGuk2gHceQQ-gjWpZJUKcAqppysBakKghvJwCkWo_606pJBDeom1Vosdo4LRqRVqNxZCzmlg0UhcSeAg-o_AUeLd9iAxAbV29wgv_FIEaJVkpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/decaacf8b1.mp4?token=PhixCQ-HlO5kNvSy8xVCa9z1mInNXemD9_MEn78ShO8zZZpysPqWcBaxaRZYrVM8UEG6DPpepouCkZvO1iGItdwrMTGTTpyj0MYPLhP1zubyCuCLW_oFjsFcV1BbYhDy2LuGU5kMiR-Ywr9NN9knmcR1bNvJJwkHPKm01efeG6HIXn9in2Hm5doEhFcnRFviOaoFt1hHxxE7-kPtsdg2jkGfhTgv9vmR8cJx5ykkJGuk2gHceQQ-gjWpZJUKcAqppysBakKghvJwCkWo_606pJBDeom1Vosdo4LRqRVqNxZCzmlg0UhcSeAg-o_AUeLd9iAxAbV29wgv_FIEaJVkpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85825" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85824">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/85824" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85823">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a653f7d251.mp4?token=QlBrbwggx8p-ZOEU7iXrW2A9JJ7XJKXsGlMi2T-oNq5n0GSztYm-6aeVr4bWd9OjAvBBDE6KJ96KlrKks5cywAa_sO-Ti3NwcTOq6B3g0byWwUf1dnVhFhJZuKh3QVnYV8_7_6ujCFSykS6g8fxAFk6XdBLbibvWX3HM1CnMYjVkz4ycGU58gW5wa10VegQHdnkyn8cmqdfPWHVqHFZlPknJ_DWzfcnmHRVJ2wievbt7jcIxIvSUaWhymuBao6QBtIpnh9ZposdhWyy_Q7VOHtn6qEjexrqhTXgKsAL6IaBS4CTxhDTh04pssQ6ttNpwNqXaw8_EGW9i9HjGsXO-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a653f7d251.mp4?token=QlBrbwggx8p-ZOEU7iXrW2A9JJ7XJKXsGlMi2T-oNq5n0GSztYm-6aeVr4bWd9OjAvBBDE6KJ96KlrKks5cywAa_sO-Ti3NwcTOq6B3g0byWwUf1dnVhFhJZuKh3QVnYV8_7_6ujCFSykS6g8fxAFk6XdBLbibvWX3HM1CnMYjVkz4ycGU58gW5wa10VegQHdnkyn8cmqdfPWHVqHFZlPknJ_DWzfcnmHRVJ2wievbt7jcIxIvSUaWhymuBao6QBtIpnh9ZposdhWyy_Q7VOHtn6qEjexrqhTXgKsAL6IaBS4CTxhDTh04pssQ6ttNpwNqXaw8_EGW9i9HjGsXO-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرة اخرى استهداف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85823" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85822">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مشاهد اخرى لاستهداف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85822" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85821">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79187ad90d.mp4?token=oU01AFasdMcpJYFeFUwiWJ1dsa6CGpqjDHLb_TOUOlSpyCderRZOcIYuoyGrL0OOTVzCkg4i4XxSBjQxW0fL1E1VE4iTMDqPJjk8DGPNdaHaef0IMsqLGI6vSi-bVcRhhg8Lg6nID3xJQbmGnZIgOK7OnNMw__POJQDtA2bKZyo4tfbfl94r1njSlqZ-fP9xePb-5y79A_fnBDxqrIx_A9MUHsdv8PcsTGsDZ8L3_L_-ZY9vv3gkGVhRfF16nflbV7kPhJbQKz1s6CdXbOy7mU3E0Us9DHcYwRe8fdSn9g6dVcNPwyC4NbS0eXnZEwBJEjKA2KJwV4VebMwGfDLXdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79187ad90d.mp4?token=oU01AFasdMcpJYFeFUwiWJ1dsa6CGpqjDHLb_TOUOlSpyCderRZOcIYuoyGrL0OOTVzCkg4i4XxSBjQxW0fL1E1VE4iTMDqPJjk8DGPNdaHaef0IMsqLGI6vSi-bVcRhhg8Lg6nID3xJQbmGnZIgOK7OnNMw__POJQDtA2bKZyo4tfbfl94r1njSlqZ-fP9xePb-5y79A_fnBDxqrIx_A9MUHsdv8PcsTGsDZ8L3_L_-ZY9vv3gkGVhRfF16nflbV7kPhJbQKz1s6CdXbOy7mU3E0Us9DHcYwRe8fdSn9g6dVcNPwyC4NbS0eXnZEwBJEjKA2KJwV4VebMwGfDLXdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف يستهدف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85821" target="_blank">📅 00:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85820">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af9e5cd42.mp4?token=aw2F5QIRXMJHbaTUU54DIncsiyxZR2MQgS6BTkxx8c315zl3AkW4gEu5ZF8bUjBZeTnnCwOx_tV-DJ_OtjDREGzR7fIBA0owZ4LOOh6SA_VqJKi2rshOJ_XMAbC87zF77aJI1HcfYtyPZZWm5A6LyzdtbbbtGXYwZWxwg3fV5IKAot3kvCbEZviQLr6E4YEeaCxiWrUAFXWG1J_DjRqaUhIMD3L56FCZis7qnbvT_Qf34D0uwLmmt4ptPKfHIbtfOdJuG6KWrRni-pR77yeLnp3kTpVZzQpMhF9ylnkXL1cPOg56O60rFbcvgO1nAhENogJz9ijA8yGV7ms92oJOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af9e5cd42.mp4?token=aw2F5QIRXMJHbaTUU54DIncsiyxZR2MQgS6BTkxx8c315zl3AkW4gEu5ZF8bUjBZeTnnCwOx_tV-DJ_OtjDREGzR7fIBA0owZ4LOOh6SA_VqJKi2rshOJ_XMAbC87zF77aJI1HcfYtyPZZWm5A6LyzdtbbbtGXYwZWxwg3fV5IKAot3kvCbEZviQLr6E4YEeaCxiWrUAFXWG1J_DjRqaUhIMD3L56FCZis7qnbvT_Qf34D0uwLmmt4ptPKfHIbtfOdJuG6KWrRni-pR77yeLnp3kTpVZzQpMhF9ylnkXL1cPOg56O60rFbcvgO1nAhENogJz9ijA8yGV7ms92oJOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار طيران المسير في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85820" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85816">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207797b8fe.mp4?token=iVImswSfPVua3wpM_BpGVhVev7We1o5KllgobKfXqhTUHJ2WUqmBvarkd4n7c5r9tGW3uM2NOrAHOXTadkVcclqjMGBXT7H5uB6tCcMmNssky7wv0uLjpV2JABnp1aAnnm1gJZRXqA_rUJ69WHnlWdh4j7hKKOSn5viYPzYdxb2SqphGhHv0C_h-PhfD2qq-ZKxk51pcSa_wFKjX0Xa-twwUHZudBgmmLn82LtVzcKHoILcq6yt3teojRqosyO7IK4uZ1PO-ZNRqXkjOjab9-NvYJQJSZ37IVu24ypmfTgmZYc24bIC1-krBCqcmG63FCGDtRANRIBBh5BqhHNIw7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207797b8fe.mp4?token=iVImswSfPVua3wpM_BpGVhVev7We1o5KllgobKfXqhTUHJ2WUqmBvarkd4n7c5r9tGW3uM2NOrAHOXTadkVcclqjMGBXT7H5uB6tCcMmNssky7wv0uLjpV2JABnp1aAnnm1gJZRXqA_rUJ69WHnlWdh4j7hKKOSn5viYPzYdxb2SqphGhHv0C_h-PhfD2qq-ZKxk51pcSa_wFKjX0Xa-twwUHZudBgmmLn82LtVzcKHoILcq6yt3teojRqosyO7IK4uZ1PO-ZNRqXkjOjab9-NvYJQJSZ37IVu24ypmfTgmZYc24bIC1-krBCqcmG63FCGDtRANRIBBh5BqhHNIw7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار محاولات الاعتراض والتصدي لمسيرات في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/85816" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85814">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4a468f9f.mp4?token=qSoxH-ttpPGfTjhkyj7FbBrzHK8arsN1gaKLBGTiLPJ0lrq-kV6T7on2UihY4LtT5r289iecsOoldohImyQhbu0puzwCIvSITHGwHC0WV4ZWM8J4e--G7pS8sZFElB-hNZx2HkIeCDysBWKeH9MNDtH2RDWDyche-ak5Dj-v_JPxm8K-LQUYIpNJjp_poJfvxj3gDZOat2mvJclMJniQavJJQrBEya6mHWiiyP-DewL5Q9lLlw-HYUqpwatQoRYggdBHQByz2e59xqzEHSU0dcv_6drnVowlAbwkbzQT_DRZ4cYVwScMZaYcsl60fgyCiSEBqocfuw2WEYVU80ZJyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4a468f9f.mp4?token=qSoxH-ttpPGfTjhkyj7FbBrzHK8arsN1gaKLBGTiLPJ0lrq-kV6T7on2UihY4LtT5r289iecsOoldohImyQhbu0puzwCIvSITHGwHC0WV4ZWM8J4e--G7pS8sZFElB-hNZx2HkIeCDysBWKeH9MNDtH2RDWDyche-ak5Dj-v_JPxm8K-LQUYIpNJjp_poJfvxj3gDZOat2mvJclMJniQavJJQrBEya6mHWiiyP-DewL5Q9lLlw-HYUqpwatQoRYggdBHQByz2e59xqzEHSU0dcv_6drnVowlAbwkbzQT_DRZ4cYVwScMZaYcsl60fgyCiSEBqocfuw2WEYVU80ZJyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء محافظة اربيل تشتعل اثر الهجوم على مقرات الاحزاب المعارضة الايرانية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85814" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85813">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d950af84df.mp4?token=oHxCGLITYAIwuNOOG7NAo_PBB6jsUWpYOyMdTR0MMBeM2smmELtWxXOwZtMTevbR1XgLwd_wCiL_B6pI8QWvZsU7aqZPraRWMryShFR_Hk0kqDDQw-R8dPsPSiOC2sAFrdpbItZON64z7x7LEfemVS8ExgsQ_UXu3vQ2R_lMv_TnoW09OtEhXTlWaR-fx6cP0E-oQJsNkKk1Im3AQPMumIy5TfLYqephJd9-fNaovTYoXD6vvk8U6Eehd8KXESPCIgBKPk0PINX8ZWvxOQSocLKR5b1Pk_sGBhZuPsPnfpqVKwJN5WNxhbxs7Wvhk9vwJ_r4uulsBBZbW6nZplXEMkdlp5kYvBZEj1b15bCbSEVM4h_Eh47HwskoKNFOHfm7x3KuMdlW1h0pG_y_AWQ8VC-k9hgu3IHDJ1x05LENrErlX6fb8omKJXscS7JWhPooUgCwGN9wTV5QpMp_I1mg1fND6ZV24ddpM33LUzu3bcP9RrgMaw2RDdUMgCxnO_Rk6T_HCkG6e6oNo2YkS49ojhk_M6D3EGQNP_qEJ6ZcwGAYZjjUMiYBkQ1HHcewxSa-pEO0RohMr1DuA3GCpypZID_FR68_cy5elpKPpa4QtbSdcxklMuAGaCnLozmngBk6Cu81mFdBp48pKi9XW3ojI6mtCfoH_zyNKpITSvJpQcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d950af84df.mp4?token=oHxCGLITYAIwuNOOG7NAo_PBB6jsUWpYOyMdTR0MMBeM2smmELtWxXOwZtMTevbR1XgLwd_wCiL_B6pI8QWvZsU7aqZPraRWMryShFR_Hk0kqDDQw-R8dPsPSiOC2sAFrdpbItZON64z7x7LEfemVS8ExgsQ_UXu3vQ2R_lMv_TnoW09OtEhXTlWaR-fx6cP0E-oQJsNkKk1Im3AQPMumIy5TfLYqephJd9-fNaovTYoXD6vvk8U6Eehd8KXESPCIgBKPk0PINX8ZWvxOQSocLKR5b1Pk_sGBhZuPsPnfpqVKwJN5WNxhbxs7Wvhk9vwJ_r4uulsBBZbW6nZplXEMkdlp5kYvBZEj1b15bCbSEVM4h_Eh47HwskoKNFOHfm7x3KuMdlW1h0pG_y_AWQ8VC-k9hgu3IHDJ1x05LENrErlX6fb8omKJXscS7JWhPooUgCwGN9wTV5QpMp_I1mg1fND6ZV24ddpM33LUzu3bcP9RrgMaw2RDdUMgCxnO_Rk6T_HCkG6e6oNo2YkS49ojhk_M6D3EGQNP_qEJ6ZcwGAYZjjUMiYBkQ1HHcewxSa-pEO0RohMr1DuA3GCpypZID_FR68_cy5elpKPpa4QtbSdcxklMuAGaCnLozmngBk6Cu81mFdBp48pKi9XW3ojI6mtCfoH_zyNKpITSvJpQcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاقات دفاعية في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85813" target="_blank">📅 00:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85812">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec823fea58.mp4?token=hfFSfRDbyEzmHn01ZzwaoC4rLSyFiznGfPg8AzpOguQk3eq5n6Nc7eK8ZJehHf-JChfawQh2mgD1-B5gywKBGxnpu4sTtqMO5mEXrvVRF9xsfRYzlWGHinhXIQd7KZduv21zNNNWKaeZWnCshsejNKU3kZQKCqHB5CWezL3p6qlZaE3VuPZKNRjvmdXjodFwSH67Aq_d1ivKWgyJagxNB2cwgcqI0azmQXmhKtW-S6jxAGUol1gagwf8uJRJ_MhHXG9BeMeu4f8FTOVuW31jHVQ63Guk28sqR_EgU2IoPxHCFmvJqHJnfA-zgBX_dRqaX5FEkX1fZZhcxz0jFBphsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec823fea58.mp4?token=hfFSfRDbyEzmHn01ZzwaoC4rLSyFiznGfPg8AzpOguQk3eq5n6Nc7eK8ZJehHf-JChfawQh2mgD1-B5gywKBGxnpu4sTtqMO5mEXrvVRF9xsfRYzlWGHinhXIQd7KZduv21zNNNWKaeZWnCshsejNKU3kZQKCqHB5CWezL3p6qlZaE3VuPZKNRjvmdXjodFwSH67Aq_d1ivKWgyJagxNB2cwgcqI0azmQXmhKtW-S6jxAGUol1gagwf8uJRJ_MhHXG9BeMeu4f8FTOVuW31jHVQ63Guk28sqR_EgU2IoPxHCFmvJqHJnfA-zgBX_dRqaX5FEkX1fZZhcxz0jFBphsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء أربيل تعج بأصوات الطيران الحربي والمسير الإنتحاري في هذه الأثناء</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85812" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85811">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d05b791a.mp4?token=WPSp9jgJp5XPPP6ZNqbB6gOtHFX9n6uSapMQ5Ihr1nq7nsZOKXYRa5BQWm8GGcoXrOweY6s0EnIi6q-zXOwXkmgCybNFZGxEpnHgyKhZBi1R4BgVDHNNaVpPaO96qv_FMhD6HprPPfgKYQ2EjDYh8lrN4ZWB5PbWa118PnMfQg8Tbt9cRXYhEvf53WjQv8A_0bc1s1sBGXG8Mt20PceMABZDDU6uq4ONAGkn6fHbwcAUGq2Mjf6OigX0EfTqwuThzOuH3JxGLl8x4vTaTwVuNSK0TaONvW1g9zzifyuhiUEOlK2y-QEMCY0Lx944OUp2CBc9ldYc_R0-oAD3PAsioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d05b791a.mp4?token=WPSp9jgJp5XPPP6ZNqbB6gOtHFX9n6uSapMQ5Ihr1nq7nsZOKXYRa5BQWm8GGcoXrOweY6s0EnIi6q-zXOwXkmgCybNFZGxEpnHgyKhZBi1R4BgVDHNNaVpPaO96qv_FMhD6HprPPfgKYQ2EjDYh8lrN4ZWB5PbWa118PnMfQg8Tbt9cRXYhEvf53WjQv8A_0bc1s1sBGXG8Mt20PceMABZDDU6uq4ONAGkn6fHbwcAUGq2Mjf6OigX0EfTqwuThzOuH3JxGLl8x4vTaTwVuNSK0TaONvW1g9zzifyuhiUEOlK2y-QEMCY0Lx944OUp2CBc9ldYc_R0-oAD3PAsioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاقات دفاعية في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/85811" target="_blank">📅 00:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85810">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c719c4ee4c.mp4?token=tNnL8O_N3ZiODH07pNTB7fzJmEwkjlOqRUD4-2NHdS7GqOLhGPhheDMIE3iZMCvUwyVpRIyta1w87cCiOIs_yQgneNMRlJ9P9SoKkVUHJzs8ki_oddEtjiHpRYMJqmcw7g4YhpFfm2StCzktkRtF7BmPM--zmOIk5mE0FRGKpByWgFCxtRxzp11jPRIgDu8kXED7WgPBXQjtRI0hsay5MpJIaZejwqO8uH0rRGCkxyhKgES7qOzbSguJfu4KI0jNuZF8K7DFigG5Lw-E1WZMaNmkXonYbVtGGVE_PUGF_Jv05M7PJvAC_lAP6UVYleS4aQFHcxMB85tO_v0WuNMA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c719c4ee4c.mp4?token=tNnL8O_N3ZiODH07pNTB7fzJmEwkjlOqRUD4-2NHdS7GqOLhGPhheDMIE3iZMCvUwyVpRIyta1w87cCiOIs_yQgneNMRlJ9P9SoKkVUHJzs8ki_oddEtjiHpRYMJqmcw7g4YhpFfm2StCzktkRtF7BmPM--zmOIk5mE0FRGKpByWgFCxtRxzp11jPRIgDu8kXED7WgPBXQjtRI0hsay5MpJIaZejwqO8uH0rRGCkxyhKgES7qOzbSguJfu4KI0jNuZF8K7DFigG5Lw-E1WZMaNmkXonYbVtGGVE_PUGF_Jv05M7PJvAC_lAP6UVYleS4aQFHcxMB85tO_v0WuNMA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء أربيل تعج بأصوات الطيران الحربي والمسير الإنتحاري في هذه الأثناء</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85810" target="_blank">📅 00:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85809">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/065589ca73.mp4?token=JJ1kjfQUoH1x2uc1emWvgQSIPJ26XN78DTcYkLJ17btDQvnJzRJjXYAoO6lurkwrHbRDd3fjnr2hpsrNuTRFYGkRc7kAX6xe6cSkXL5nHlN0UozeOwk8JVL3mVcdXZki5LaNtiyd86LQuQfZMsGbNwuvOrHGHSpcoClYXN6pXGBDwQ9BiU6Qmd4wvm0GReFH9uxKQ1IS3yHJ1RVkCcpftKBYsEvO2voNZIf1kQBOwcT7FCePTRkHxZNcejlffDOZajZGIN2tWj9Kh3mf-KEE5P0KTGcnGiUzzmRQWx7R3hofbA7LFRTeUVDQDU3zfRAcd5qcL5Z3REWaxH_W9s-wyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/065589ca73.mp4?token=JJ1kjfQUoH1x2uc1emWvgQSIPJ26XN78DTcYkLJ17btDQvnJzRJjXYAoO6lurkwrHbRDd3fjnr2hpsrNuTRFYGkRc7kAX6xe6cSkXL5nHlN0UozeOwk8JVL3mVcdXZki5LaNtiyd86LQuQfZMsGbNwuvOrHGHSpcoClYXN6pXGBDwQ9BiU6Qmd4wvm0GReFH9uxKQ1IS3yHJ1RVkCcpftKBYsEvO2voNZIf1kQBOwcT7FCePTRkHxZNcejlffDOZajZGIN2tWj9Kh3mf-KEE5P0KTGcnGiUzzmRQWx7R3hofbA7LFRTeUVDQDU3zfRAcd5qcL5Z3REWaxH_W9s-wyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اربيل لحظة الاستهداف مقرات احزاب المعارضة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/85809" target="_blank">📅 00:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85808">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8944cda6.mp4?token=rHzIpn7OIlI--SBAJeeMPgE45QFsOLSqo6b0w3iboFw3fpKfxoQJ9ny1vuJhjfpSHFcE27ffCa5EXI2Gq1fQHsylLDvO1nVEw7XUW5SIki_s9rh_YfecU-v0ysn_ib--TLQXSDpPwzumQEmL9LEg4ZMuBzi9Ok7JtLqx5_wAIUJtCnPGlVIXTcwqCzBbHnum4KrfYffZrkBFRZFhpIKFqcSDykvkbMtvP0YRVLppDzPEqPY0wZ-DvIKrzLliqWDkbWsZaJ4W4qplN7q_nnW8MOqzD6CDWFiFT5lZJfWkoIS_nYU5aVjrHHlGpaYqjbHdlI2qoSNnpC4Zva3Un98pBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8944cda6.mp4?token=rHzIpn7OIlI--SBAJeeMPgE45QFsOLSqo6b0w3iboFw3fpKfxoQJ9ny1vuJhjfpSHFcE27ffCa5EXI2Gq1fQHsylLDvO1nVEw7XUW5SIki_s9rh_YfecU-v0ysn_ib--TLQXSDpPwzumQEmL9LEg4ZMuBzi9Ok7JtLqx5_wAIUJtCnPGlVIXTcwqCzBbHnum4KrfYffZrkBFRZFhpIKFqcSDykvkbMtvP0YRVLppDzPEqPY0wZ-DvIKrzLliqWDkbWsZaJ4W4qplN7q_nnW8MOqzD6CDWFiFT5lZJfWkoIS_nYU5aVjrHHlGpaYqjbHdlI2qoSNnpC4Zva3Un98pBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اربيل لحظة الاستهداف مقرات احزاب المعارضة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/85808" target="_blank">📅 00:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85807">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الإطار التنسيقي:
عبرّ الاطار التنسيقي عن موقفه الثابت لدعم الجهات المختصة في محاربة الفساد وتعضيد جهود الحكومة في ملف حصر السلاح بيد الدولة.
وشدد الاطار التنسيقي  على رفضه المستمر لاستخدام اراضي الدول في الاعتداء على الدول الآخرى، واغراق الجميع في صراع لا يخدم اي من الاطراف.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85807" target="_blank">📅 00:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85806">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
انباء متداولة عن استهداف حقل كورومو في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85806" target="_blank">📅 00:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85805">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
🇺🇸
نشرت صحيفة أميركية تقريرًا يستعرض آثار العدوان الأميركي على إيران والتداعيات الاقتصادية التي انعكست على دول العالم بدءًا من ارتفاع أسعار الوقود والطاقة وصولًا إلى زيادة أسعار المواد الغذائية وسلاسل الإمداد.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85805" target="_blank">📅 00:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85804">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef69381f74.mp4?token=Ok_HM_wzAqgNUbZ8uhLNpwKCo3r38NRiX4Sqi0COBFO33T0RrD3zVmCJHDDRB8JcE6SZqd766jEWbAtJTU6QNLEeaBS99D3z7SwbONYdeEuZO8mv5xLJD27-494OnGQrTVL1jZg-FCPAAkNXJebhEJ26Z5FijWQ_EXS-kZDdveQSVJQCMKGbt5_6ukVRUerG_u45A5hS_GnELOw-hHhKRnJLXI7yxbH_4wItET12ux1rKobDab2_oawT1GXioOzCsOMVLZk7GmOF5pLWtujFag8FwXv90v2UJkOA3OgleJGYG7hhtmyhL0eL0bpUUza8obi8JU98AQCegbnAL1MeHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef69381f74.mp4?token=Ok_HM_wzAqgNUbZ8uhLNpwKCo3r38NRiX4Sqi0COBFO33T0RrD3zVmCJHDDRB8JcE6SZqd766jEWbAtJTU6QNLEeaBS99D3z7SwbONYdeEuZO8mv5xLJD27-494OnGQrTVL1jZg-FCPAAkNXJebhEJ26Z5FijWQ_EXS-kZDdveQSVJQCMKGbt5_6ukVRUerG_u45A5hS_GnELOw-hHhKRnJLXI7yxbH_4wItET12ux1rKobDab2_oawT1GXioOzCsOMVLZk7GmOF5pLWtujFag8FwXv90v2UJkOA3OgleJGYG7hhtmyhL0eL0bpUUza8obi8JU98AQCegbnAL1MeHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
What if they come back ?</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85804" target="_blank">📅 23:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85803">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالمقاومة الاسلامية في العراق</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-JdND6PhuZO37S77yfyor8RFpSqOdUnA6lE7pY--65GqIQjNyLGwZGWULqV3oDrUvQuZJvGOAB7cOkeCgCdBxDuO1cEu-LdfN7415_bOOCSsQCqEDnhk7OQ4D5rVVoss1bg_PBID-QG0lD1IG6DusuzMDefFeT0F6WN_nwqqU8JMMP_mAtUomePQ_5NH0aOUgoTtAqfqnMiHgO-rtvhNwgtX-YSXV6BDrl3Y3AxY0hAgpm6ZShW6PFl0wR7ilmvmyDaUOqgYal0kKgg4BVBw94yCnCR41BZCS_Y-LPDZWLYm59L_RQxjvheY2DHsG-Ck-v6vkR6-f6tLZ5U-w8TWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
(إِنَّمَا يَفْتَرِي الْكَذِبَ الَّذِينَ لَا يُؤْمِنُونَ بِآيَاتِ اللَّهِ ۖ وَأُولَٰئِكَ هُمُ الْكَاذِبُونَ)
بينما يواصل الكيان السعودي رمي الاتهامات نحو العراق، زاعماً أنه المصدر لقصف منشآته البترولية في الشرقية والرياض، فإن هذا الادعاء لا يزيدنا إلا يقيناً بأن العداء للعراق وشعبه سمة لاصقة بهذا النظام.
إن هذه التخرصات ما هي إلا محاولة لتبرير العجز عن الرد على الضربات اليمنية الموجعة التي طالت عمق بُناهم التحتية، خوفاً من طبيعة الرد اليمني القادم.
إننا في المقاومة الإسلامية نُوجه للنظام السعودي تحذيراً واضحاً، نُعلن فيه أن أي فعل سعودي أحمق سيُجابه بردٍّ قاسٍ، يجعلهم يعضون على أصابع الندم.
ونقول لهم، وبكل وضوح: إن كان فيكم رجل رشيد، فأنتم أحوج ما تكونون اليوم إلى رفع الحصار الظالم عن الشعب اليمني، بدلاً من توجيه الاتهامات يميناً وشمالاً، لتبرروا بها فشلكم، وتغطوا بها على جرائمكم.
المقاومة الإسلامية في العراق
27 تموز 2026</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85803" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85802">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/85802" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
عاشت المقاومة العراقية البطلة وسلاحها الموجه نحو الاحتلال</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/naya_foriraq/85802" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85801">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1Gl7Cnmmju1nz52tPNIftPKvVUBAXHA0DbiXDIhBNWM85_csLgywvLuU_4WPwL8RZLqUprSw-AykLx6vlPyp2S1mPYkrV7Opbyl5Qi8bE2PQ4HREF4DWbQVKq6PvckWNnMknhrckPbkZ2IU5_s46RYJK9-RvkRak47lSubW7t1BHOeKqLR-s8qg-4ki1m1JWVhDKWMvkvOBx-tWwuaD887gs7V8PO0ux6Q-1oA-x8WM_PUYiJ5nhi6--YNfFscX2b6jnr8HdtwI8TWEt5QPJdMiKjKMV_YzKqhXr8-n_3glDybam3uUjOh96blBBigL2I7jYhE_DRiSomGpU4Ithw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط طائرة مسيرة أمريكية قرب سد حديثة</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85801" target="_blank">📅 23:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85800">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سقوط طائرة مسيرة أمريكية قرب سد حديثة</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85800" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85799">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85799" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85798">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed1a8163b.mp4?token=n0I_Ii4jCI0MR1qZAowEOgfVIphkVTeZ6xTsAQGIxs2YYSsFt7cYGElyWDOdfuSqqLbOMysNTiWF7H4k51-4WsfnnJSc7xw8pRHUdZlVzEJ1G4cr22FI6Bk6Fdae27-BcXds7Z1ta3UWZMZZXoOmIEvurjlGYNH2v9xQmhf4n_yVAFcDRx2AFX3zB_U0_Z9_ud8-rWUk5rkgBY42oFiBht8d5mNbRh8-5L8g8ebpA25ID0pL88cdAX7y4qOORssqGbJyonaYQBYZRZL7_4NOBjT_LAX-LDzaFzTvqv2Qn0Z3Dg-WB37SkI5VlUPFsDjdcKbia9JCzsUl6HAA1W1xbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed1a8163b.mp4?token=n0I_Ii4jCI0MR1qZAowEOgfVIphkVTeZ6xTsAQGIxs2YYSsFt7cYGElyWDOdfuSqqLbOMysNTiWF7H4k51-4WsfnnJSc7xw8pRHUdZlVzEJ1G4cr22FI6Bk6Fdae27-BcXds7Z1ta3UWZMZZXoOmIEvurjlGYNH2v9xQmhf4n_yVAFcDRx2AFX3zB_U0_Z9_ud8-rWUk5rkgBY42oFiBht8d5mNbRh8-5L8g8ebpA25ID0pL88cdAX7y4qOORssqGbJyonaYQBYZRZL7_4NOBjT_LAX-LDzaFzTvqv2Qn0Z3Dg-WB37SkI5VlUPFsDjdcKbia9JCzsUl6HAA1W1xbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: لا يمكنك رشوهم. يجب علي هزيمتهم،ونحن نهزمهم بشدة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85798" target="_blank">📅 23:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85797">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98851fe969.mp4?token=C8qoFBYmo7_PJhcmtiqJ8-F1lXxXDhTv3BSDF6ArZEvCQNFjPCprd4WeNpvOZ-9wUhujeGx-yCCLQEcs75je06FCeg4dujNSeWQiIleyYIlYy5m9srThfPWUnJUDdK_-ErmopsvJ4LjCUyww9z6T_IyA8IfWe3j1eqbg2427_ordlEAaxGwzWTWAZ4v8pNHcki434JLfrh9og9BTKE5rj-U6WjMGDEUGI6U4LkB2qoEprrmDoKc3tDSDAtLZzzt3KqszFyPcQ26SFKW68YJpRI_cE9h6ERBHEFWfYtQuac9rtfOM1lS1SrL3FlessLNkhdJUiOLuNxOjhqMxfbN8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98851fe969.mp4?token=C8qoFBYmo7_PJhcmtiqJ8-F1lXxXDhTv3BSDF6ArZEvCQNFjPCprd4WeNpvOZ-9wUhujeGx-yCCLQEcs75je06FCeg4dujNSeWQiIleyYIlYy5m9srThfPWUnJUDdK_-ErmopsvJ4LjCUyww9z6T_IyA8IfWe3j1eqbg2427_ordlEAaxGwzWTWAZ4v8pNHcki434JLfrh9og9BTKE5rj-U6WjMGDEUGI6U4LkB2qoEprrmDoKc3tDSDAtLZzzt3KqszFyPcQ26SFKW68YJpRI_cE9h6ERBHEFWfYtQuac9rtfOM1lS1SrL3FlessLNkhdJUiOLuNxOjhqMxfbN8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏أحدهم يصرخ في وجه ترامب قائلاً: "حامي المتحرشين بالأطفال!"</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85797" target="_blank">📅 23:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85796">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07efc12575.mp4?token=gpJU_teaQGgrVB4_4doPjpiIYQCrDMVYMkDMBAKX-Fir56Z0WSuIZ1aecpfHhGyqKIR8J-hKP4Yf9f3aIgL4X1oBRERL6MAHQag6TozOgJD04_LXajaHzmLZePmsPLEnX6k6ppyWR9wqU6N0Qp-oZv48DOjsXnm5ArDu4iOEAqKd1wHbLFQ0UNF3HA927jIkFN7d1egWnGNITujp9_qPiGKSFkX-evd_WA1yc6iBrVihYLDxb8EcAgVG0ydsEDVtepdDI1TaO_ZbhZznANycThM-wxCQkYyWQkiDDjiNH97cvxNYOh3ajnTAavw2muaDKHprWoQHKj7yVasgHtrLwRA3Cf9CRf-GnXEKbrrbFKboaaFLksxIyV2rUbcJEnusHKCjTf_Dl-tIcht36Xw_Jap1zA3g07NaROz4uRIGfXd986aF2kaLzFUK6teFg6yd49BJYr9-ZUNu8oA2VgqyvZrmU1lHSbJ-WQoUX9h4YaeDF7e46WJ4E_3viijXbvMQ7oOsrHz63cgBi93pi8cerq6wPPPXJmsl2VxYLu1Vm9GihdKwLYPVPsG8VKMk97eZyFplA4OBTtXh227_7_HRE2WoxSuIxKEigTtq01Ly2Rz9f0FR0fNQ-LUtjPkik7oKn2mppf6fxckl077nGEUE05orq-9ulTpU2eTlUvZ5YxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07efc12575.mp4?token=gpJU_teaQGgrVB4_4doPjpiIYQCrDMVYMkDMBAKX-Fir56Z0WSuIZ1aecpfHhGyqKIR8J-hKP4Yf9f3aIgL4X1oBRERL6MAHQag6TozOgJD04_LXajaHzmLZePmsPLEnX6k6ppyWR9wqU6N0Qp-oZv48DOjsXnm5ArDu4iOEAqKd1wHbLFQ0UNF3HA927jIkFN7d1egWnGNITujp9_qPiGKSFkX-evd_WA1yc6iBrVihYLDxb8EcAgVG0ydsEDVtepdDI1TaO_ZbhZznANycThM-wxCQkYyWQkiDDjiNH97cvxNYOh3ajnTAavw2muaDKHprWoQHKj7yVasgHtrLwRA3Cf9CRf-GnXEKbrrbFKboaaFLksxIyV2rUbcJEnusHKCjTf_Dl-tIcht36Xw_Jap1zA3g07NaROz4uRIGfXd986aF2kaLzFUK6teFg6yd49BJYr9-ZUNu8oA2VgqyvZrmU1lHSbJ-WQoUX9h4YaeDF7e46WJ4E_3viijXbvMQ7oOsrHz63cgBi93pi8cerq6wPPPXJmsl2VxYLu1Vm9GihdKwLYPVPsG8VKMk97eZyFplA4OBTtXh227_7_HRE2WoxSuIxKEigTtq01Ly2Rz9f0FR0fNQ-LUtjPkik7oKn2mppf6fxckl077nGEUE05orq-9ulTpU2eTlUvZ5YxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏أحدهم يصرخ في وجه ترامب قائلاً: "حامي المتحرشين بالأطفال!"</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85796" target="_blank">📅 22:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85795">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDPsfFNZ42c9-ehC8zanI_JRou3994hKVcjd6RPWWrMR1dWVFieTxrr3lKO-mQ4BpN4FuCco56CSssqegJioV-f6HfxCgV_8EnSSai5UbggkCmLx0V-x5nR3vhH3_ualEJMI2JzoMT6BV6F9XgHAsAk57qyG-rhDIiE1sjsXcrk0yQEtwjqCkRiurGJZJ4ioin6FZNep2VQiY9pkEH34A7aRKVQFnlkayfCXkKT6IZfePbolUTY0FspAs3LJtQCzhVoHOQDd1rCCAdF61zcHo3t-jZna3JeGuBga2K7gUneRMuPwRfP_5ZeJP_jAYi8Z9FxEHciYoDhHQLbaoxS5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ارتفعت صور شهداء ميناب في شوارع مدينة النجف الأشرف، قرب مرقد الإمام علي (ع).</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85795" target="_blank">📅 22:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85794">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b09d4680.mp4?token=A_RIYJtyY3NikOtQ6nNpLaDk_CSorennA7N8kWARLkidmUanhFQNS-P5Zqyc2KM2Q4jXeWiSDpDfFRET_mpg8gpMHthJXp9okW8AiVy3cvEDSZc17-_udWt4D0iA3OtTN-mxXfCD_snxpDA63vADW9NhsxfGlu9Z0bZnjhAVH08uHQ_ZIDdUYz4nsxtiNR_5xOzL1ukWEdhje8TLu-UwT5pvInu4pdU_6Fx5VQEUR81HkjUszHGVnhO1FWBYuVOcDiK2qbUsAR44yuCa4od4EVKwcwBWrBSPBoceivm-PX54THoCkra3DJOLiYvV6kPOS2pugPyX7bacNRAvVZRfDIiGLHhBFgfJmYMzACTTjOZ-DjcKV-Z5g0GeoglS2UPpXNB5BqYhdDihSMQQlVp8T8gFzChXlnIwOs7KySqi3xtOf8pA5278xXxWpVtGhxVK_H0Sg0gcfDSWvQXQHcNdt6zI0M-f6E29KVsNDVwauqw6J7yA4jvkmlkFt4BHIeWGHNgH-lvDyI6mEJuTgGsSRSZAG7osbdvMrMDvEKVWdToko7hojqa6sropBZwXqXe6d-Uyk4UeQCHU_007XTmQIqhts_fbhMOaHGymDM3MkRyUFcaNan50Elw-mXLZl_GuKHlSkEpt31aAK9hB-HAC78zKojGQMtNliythb10TmTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b09d4680.mp4?token=A_RIYJtyY3NikOtQ6nNpLaDk_CSorennA7N8kWARLkidmUanhFQNS-P5Zqyc2KM2Q4jXeWiSDpDfFRET_mpg8gpMHthJXp9okW8AiVy3cvEDSZc17-_udWt4D0iA3OtTN-mxXfCD_snxpDA63vADW9NhsxfGlu9Z0bZnjhAVH08uHQ_ZIDdUYz4nsxtiNR_5xOzL1ukWEdhje8TLu-UwT5pvInu4pdU_6Fx5VQEUR81HkjUszHGVnhO1FWBYuVOcDiK2qbUsAR44yuCa4od4EVKwcwBWrBSPBoceivm-PX54THoCkra3DJOLiYvV6kPOS2pugPyX7bacNRAvVZRfDIiGLHhBFgfJmYMzACTTjOZ-DjcKV-Z5g0GeoglS2UPpXNB5BqYhdDihSMQQlVp8T8gFzChXlnIwOs7KySqi3xtOf8pA5278xXxWpVtGhxVK_H0Sg0gcfDSWvQXQHcNdt6zI0M-f6E29KVsNDVwauqw6J7yA4jvkmlkFt4BHIeWGHNgH-lvDyI6mEJuTgGsSRSZAG7osbdvMrMDvEKVWdToko7hojqa6sropBZwXqXe6d-Uyk4UeQCHU_007XTmQIqhts_fbhMOaHGymDM3MkRyUFcaNan50Elw-mXLZl_GuKHlSkEpt31aAK9hB-HAC78zKojGQMtNliythb10TmTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🏴‍☠️
🇮🇶
خلايا اوكرانية تنفذ هجمات في العراق وتُنسب للفصائل.. مستشار الأمني القومي يكشف سراً "لم يسمعه العراقيون" من قبل</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85794" target="_blank">📅 22:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
مقر خاتم الانبياء المركزي:
إن الولايات المتحدة، في استمرارها للشر وانعدام الأمن في المنطقة، وعقب فرضها الحصار البحري غير القانوني على إيران، هددت السفن الإيرانية، والسفن التجارية، وناقلات النفط في المياه الساحلية والإقليمية لبلادنا على مدى الأيام الثلاثة الماضية.
نحذر من أن هذا العمل الأمريكي يُعد امتدادًا للحرب في المنطقة، وكما أثبتت القوات المسلحة للجمهورية الإسلامية الإيرانية على أرض الواقع، فإنها لن تتهاون مع أي تهديد أو شر من جيشها الإرهابي، وستتعامل معه بكل حزم.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/85793" target="_blank">📅 22:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85792">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
🇮🇱
سفارة الاحتلال الاميركي في الضفة الغربية تصدر انذار بعدم السفر الى الضفة الغربية نتيجة التصعيد الاخير.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/85792" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85791">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f416d3226.mp4?token=DbixzG-olkWWzTvMaLeCJ7-LdDH3TmP8HuArlZPXpO0tnQfemsVyorIPngLqwwsh3MWnv0S_H22-jc6-057luksia_8Du7sRZmGmcvL87dz8zSx_upt-C8Xi1H_F2MaGtWXU_pCClPSZlJFM8NfhmwDelVwzmTkpRkV9sicsQassVce3bwlhDctLaPcv7ExAuV54a51o77KHINLnjHjmAeDQ9p2-bR8ldfTyS_0Qmfp7i3cKVS_7XB5943xnVjLNsGaUS-gv1rxUXDaRmkTntWMqMyB4dY6AmCh0dtIuqjBF_AkQqrVc2PYwguO2MgT3vU7qiO2AtemgylU4o0Y3X4wQkZFa6_BxzrwROOybWcTI7Wh0NGNyr9yzvEvEqi9aO3H03IlajtHQCY8obWc9cROcNx1n2o8Koi7wOJGVQXY8EMMreq_a_ZlBXncUT4jAYMqyVE48qy3pva-PEuLGLEjJDpT0IBNany38MuCfDl3SEf3PzWTh43JoFyKQwWtNDA5L48RuyU5DIu32aKHu8D5Yk7Kw4fJfsgiGPSJx81S9sZecIvI0b92NnV4xxUTxrSkfRwgZL6Ft7OHhOkgt6fCcDKIsYhhvKhy74hLednNvHvpj4Lk64SV3cVf4MZ8BHKFVuVeu5E8TYikBTV7t_Lly2M3yjcC1D6B-qPPACcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f416d3226.mp4?token=DbixzG-olkWWzTvMaLeCJ7-LdDH3TmP8HuArlZPXpO0tnQfemsVyorIPngLqwwsh3MWnv0S_H22-jc6-057luksia_8Du7sRZmGmcvL87dz8zSx_upt-C8Xi1H_F2MaGtWXU_pCClPSZlJFM8NfhmwDelVwzmTkpRkV9sicsQassVce3bwlhDctLaPcv7ExAuV54a51o77KHINLnjHjmAeDQ9p2-bR8ldfTyS_0Qmfp7i3cKVS_7XB5943xnVjLNsGaUS-gv1rxUXDaRmkTntWMqMyB4dY6AmCh0dtIuqjBF_AkQqrVc2PYwguO2MgT3vU7qiO2AtemgylU4o0Y3X4wQkZFa6_BxzrwROOybWcTI7Wh0NGNyr9yzvEvEqi9aO3H03IlajtHQCY8obWc9cROcNx1n2o8Koi7wOJGVQXY8EMMreq_a_ZlBXncUT4jAYMqyVE48qy3pva-PEuLGLEjJDpT0IBNany38MuCfDl3SEf3PzWTh43JoFyKQwWtNDA5L48RuyU5DIu32aKHu8D5Yk7Kw4fJfsgiGPSJx81S9sZecIvI0b92NnV4xxUTxrSkfRwgZL6Ft7OHhOkgt6fCcDKIsYhhvKhy74hLednNvHvpj4Lk64SV3cVf4MZ8BHKFVuVeu5E8TYikBTV7t_Lly2M3yjcC1D6B-qPPACcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
انصار الله:
بيرقدار أكنجي.. سقط الرهان وبقي الحطام.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/85791" target="_blank">📅 21:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85790">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
🇸🇦
رئيس الوزراء العراقي يوجّه الجهات الأمنية المختصة بفتح تحقيق بشأن الادعاءات المتعلقة بانطلاق طائرات مسيّرة من الأراضي العراقية لاستهداف السعودية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/85790" target="_blank">📅 21:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85789">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇸🇦
بيانات ويندوارد البحرية:
تقدر الخسائر السعودية من هرمز وإغلاق باب المندب بنحو 504 مليون دولار، وهو ما يمثل 90٪ من عائدات النفط.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/85789" target="_blank">📅 20:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85787">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b04273ad0.mp4?token=UdGctU8FbC3_5OCGqBo5l4u8TGS4x38lyzhSQkox0pzDT-ZR5nm_mQymBvp-kHxuuj28XT9XXKuFqLQWJk-BVT-hpReQiTipIx3Y_kwS5pyLERGFxG3G7TNLctcub1eHpuxcZG8Rtq96ywVamqki6k1Qkhtzvw1J-OxQXBsTAPkEnUGMZsITDzDgD-YcwLM6LMRdjtx7k9MjkiRuIsemcjBTJzxRwuYoNbj-TOZ-vZkCdUf-WqX5Nv1CEtIGYE9KAkJF1rRcxoKw4DY4n0UeWh64dMwLDizhSA1wJa2rE9ev7JeI-tQvVF3ETKm75CBVAwrIt-o93ZKikKNYFlWzKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b04273ad0.mp4?token=UdGctU8FbC3_5OCGqBo5l4u8TGS4x38lyzhSQkox0pzDT-ZR5nm_mQymBvp-kHxuuj28XT9XXKuFqLQWJk-BVT-hpReQiTipIx3Y_kwS5pyLERGFxG3G7TNLctcub1eHpuxcZG8Rtq96ywVamqki6k1Qkhtzvw1J-OxQXBsTAPkEnUGMZsITDzDgD-YcwLM6LMRdjtx7k9MjkiRuIsemcjBTJzxRwuYoNbj-TOZ-vZkCdUf-WqX5Nv1CEtIGYE9KAkJF1rRcxoKw4DY4n0UeWh64dMwLDizhSA1wJa2rE9ev7JeI-tQvVF3ETKm75CBVAwrIt-o93ZKikKNYFlWzKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الهجوم الجديد الذي استهدف مقرات المعارضة الايرانية الكردية في قضاء كوية ضمن محافظة اربيل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/85787" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85786">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27556c8a9a.mp4?token=lA9fk0eFUOwjxr-SsfBFzB5EM-W7X3Wc4e9p7TpwBm5Ehl2Oz5-Wz45ZfLCRT5YuCPdAgx1b1Mcjej5dSmlVkjyOd_iB99Uq4L5nCzO8HUQEAeSe0HQ8VP095fhHOKv0Ar8bgGvOyq42veiwI0JY91P-0D2gAIRHksfTmOI1PZlJC1iFwhd3SBkfJVaX67y1xCrs6czdpUehQvz_oVF8Pcl05wo12bOwDlDfAbjIhmdc6zzDlQ7zKpQvrUlO_8I5ItUUMxQnAxCmhcepcA64QlHVv7YlIm8yZtAmTH20AjGDKn8kIehJwgDH9-k1fqYizqJXzRdf7jnx1n2LeTH8Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27556c8a9a.mp4?token=lA9fk0eFUOwjxr-SsfBFzB5EM-W7X3Wc4e9p7TpwBm5Ehl2Oz5-Wz45ZfLCRT5YuCPdAgx1b1Mcjej5dSmlVkjyOd_iB99Uq4L5nCzO8HUQEAeSe0HQ8VP095fhHOKv0Ar8bgGvOyq42veiwI0JY91P-0D2gAIRHksfTmOI1PZlJC1iFwhd3SBkfJVaX67y1xCrs6czdpUehQvz_oVF8Pcl05wo12bOwDlDfAbjIhmdc6zzDlQ7zKpQvrUlO_8I5ItUUMxQnAxCmhcepcA64QlHVv7YlIm8yZtAmTH20AjGDKn8kIehJwgDH9-k1fqYizqJXzRdf7jnx1n2LeTH8Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مواطن عربي يوثق لحظات من التوتر والارتباك داخل الطائرة أثناء عبورها الأجواء الإيرانية وتحديدًا فوق مضيق هرمز.
عبالك راكب MQ9 مو طائرة مدنية
😏</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85786" target="_blank">📅 20:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85785">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇸🇾
سوريا تدين محاولة استهداف منشآت نفطية في السعودية عبر طائرات مسيّرة اطلقت من العراق.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85785" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85784">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssfW_7HmvK05-rW5td4CngYhfUJ29vm1yNP_tWiNRF1EY6i_o_o43m-MK_8F5IgAQF-pigzamA9fUj4pjuNg4YvcPvj4-Svu6OQgvPpABUpaoqfDld5JRqlFVw-2bHSuaAapTSJFiAOTnOOr1OzRtNhxX0Pf28RucEaw8tpyfhpQC7FXLbzNUMLrQ-wnQUZ_30X52Zbm_X9la7jWkMWZ0qvXUGahfbBnxkzqbt6NyU6uqJ8oxwxuBwuccZ1PhVVlathwntX4o2dTlrdMpQrUmOdPzuvgy2tFB59F_o2ihaiWl2wKtu8PbJSn8KdrPv9jaV_N9mJ7FSXuOBwRawtiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇺🇸
ترامب إن هناك "فرصة جيدة لحدوث شيء جيد" مع إيران، ولكن إذا لم يطرأ أي تقدم "فيمكننا العودة إلى فعل ما كنا نفعله قبل يومين".</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85784" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85783">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d98c88fdce.mp4?token=HYGWQN0j3G9EHbf_V57YDwVqpu13rmwLBFvIg0o_7qsznlvbqNurjFOC5jOXEjuJsIFbhc9XUYT1Ch11O969PswgHbu-uvoeiZN5yUxOQM-hOBr0RY4L0h-_3QMnTrLz1lRMXeBvGefLeQAODa6AiK-XriDPqIidVGg0xUi-HESfvjlZaH71P67j1FQkuivtzDjdjRIEdc8eSxm4uXNNc-uYomjPrpLG6bsscraGi-0Lpb8LcH2MlveXd4kejDrB4wkU3qkUAIXpGnF7CaawGNPluiobkKWnK5cRzmP5OxnZgAbdleiz9lz_vy8bpaGAxLGuBnWDlq6hZ3Yrdb54dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d98c88fdce.mp4?token=HYGWQN0j3G9EHbf_V57YDwVqpu13rmwLBFvIg0o_7qsznlvbqNurjFOC5jOXEjuJsIFbhc9XUYT1Ch11O969PswgHbu-uvoeiZN5yUxOQM-hOBr0RY4L0h-_3QMnTrLz1lRMXeBvGefLeQAODa6AiK-XriDPqIidVGg0xUi-HESfvjlZaH71P67j1FQkuivtzDjdjRIEdc8eSxm4uXNNc-uYomjPrpLG6bsscraGi-0Lpb8LcH2MlveXd4kejDrB4wkU3qkUAIXpGnF7CaawGNPluiobkKWnK5cRzmP5OxnZgAbdleiz9lz_vy8bpaGAxLGuBnWDlq6hZ3Yrdb54dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: يقول زيلينسكي إن روسيا تزود إيران بصور الأقمار الصناعية للقواعد الأمريكية في الخليج لمساعدتها في تحديد الأهداف. ما الذي يمكنك فعله حيال ذلك؟
🇺🇸
‏ترامب: سنكتشف ما إذا كان ذلك صحيحاً. سأسأل بوتين عن الأمر. لم يكن له تأثير كبير.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85783" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85782">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78581c857c.mp4?token=r9Gyaf4EudRNB1m-YxMB26L5XxmAyK-6jMHcu0VzPri76rkpI2UMjQSWegbc72OSsxsf5tXp4KiE6zpFXCRtNPK3Kboh1jVWFL7mOB78V043K_VRy1Q85aLP9LFaMblgdblw2ot1pvOp_7q9TnW_1APut0yFLANzQScSUSIs60vQwMeVQ9riKWusi_e4pSIu4hNtSf7V194k7SsKMhq57OjHEf1xIaqeh9pVAR6VkYBbJl1zMmT_p47wG3u5lpuKy807qbeWxe0ODZqDBeYl-dnF7hdMUGIjyNIEaGifr3HlqgPSNBgF0anPRATLsyA3Pesb-9FbSGHlYxSnE7fvog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78581c857c.mp4?token=r9Gyaf4EudRNB1m-YxMB26L5XxmAyK-6jMHcu0VzPri76rkpI2UMjQSWegbc72OSsxsf5tXp4KiE6zpFXCRtNPK3Kboh1jVWFL7mOB78V043K_VRy1Q85aLP9LFaMblgdblw2ot1pvOp_7q9TnW_1APut0yFLANzQScSUSIs60vQwMeVQ9riKWusi_e4pSIu4hNtSf7V194k7SsKMhq57OjHEf1xIaqeh9pVAR6VkYBbJl1zMmT_p47wG3u5lpuKy807qbeWxe0ODZqDBeYl-dnF7hdMUGIjyNIEaGifr3HlqgPSNBgF0anPRATLsyA3Pesb-9FbSGHlYxSnE7fvog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: هل تتفق أنت ونتنياهو على موقف واحد بشأن إيران؟
🇺🇸
‏ترامب: لدينا اختلاف بسيط، لكننا متقاربون جداً</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/85782" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85781">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75da70ebb2.mp4?token=W35W68UUpjgcCnxZmsOM7ubPs3kqCk-rDYebZiwyR10LQCasntPsICqB5JeT8SKIZA_sa_Pi_lEgKOORqS-Uy3-gTIzlwWpVqOiFwVs0dG9LA-aB0L9_46yjBVW4LhCbSExr0pPX_DNzZ9CDJlw1FLayRJUrl90w_10f98rEl0EO-RrVKxYVoE_F3HZeffrBTefaIM6yNt7gKUefsgjF9ibDZ18w-RH5h9TIcaCCvAhPfTljl9XL9Zh0Ox_GixT8MOYh6mXJ5Dja0uu94t7DT1iICDeBYuh1XhG07DtOKif2KZAoKbN8mTiNyLf2yO0RtCIKCYlDpnxhpfIdlrBXJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75da70ebb2.mp4?token=W35W68UUpjgcCnxZmsOM7ubPs3kqCk-rDYebZiwyR10LQCasntPsICqB5JeT8SKIZA_sa_Pi_lEgKOORqS-Uy3-gTIzlwWpVqOiFwVs0dG9LA-aB0L9_46yjBVW4LhCbSExr0pPX_DNzZ9CDJlw1FLayRJUrl90w_10f98rEl0EO-RrVKxYVoE_F3HZeffrBTefaIM6yNt7gKUefsgjF9ibDZ18w-RH5h9TIcaCCvAhPfTljl9XL9Zh0Ox_GixT8MOYh6mXJ5Dja0uu94t7DT1iICDeBYuh1XhG07DtOKif2KZAoKbN8mTiNyLf2yO0RtCIKCYlDpnxhpfIdlrBXJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏المراسل: هل أنت قلق بشأن مخزونات الأسلحة؟
🇺🇸
‏ترامب: بالنسبة لبعض الأمور الأكثر تعقيداً، نود بالتأكيد الحصول على المزيد. لقد كشف بايدن الكثير منها.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85781" target="_blank">📅 20:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85780">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fffac8ab.mp4?token=WgKSNNuGAKco1kuyJaMOGpsYdm90lbPR5hbmCfJLDGzMt2KpeFztaP3dZFE_QdKdXCuSw0Jol596esr7oI6gyLvD5beZaSvSUP4bZQHBUyeebtVL3KVm93yCEyLd0iDFgb9kRmPwkposF5w6Lfg1G_hxVMxF5_mGpBA5E1V1MGPNqJnZcvbphwNkkNJzYibkr8sbozypapX0JSQS_RIC0QkiA0UDTmEvP9TLzDpiDVJjH7N_JtDCKzfvWScY3CBAuB9rzQnvZqf0KKFHp4-oYu5TOsN0GntITvPaB11h2kA0hO0ajx2c0YAziFuNiMFAQNi3SIriygkxn027pOEN7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fffac8ab.mp4?token=WgKSNNuGAKco1kuyJaMOGpsYdm90lbPR5hbmCfJLDGzMt2KpeFztaP3dZFE_QdKdXCuSw0Jol596esr7oI6gyLvD5beZaSvSUP4bZQHBUyeebtVL3KVm93yCEyLd0iDFgb9kRmPwkposF5w6Lfg1G_hxVMxF5_mGpBA5E1V1MGPNqJnZcvbphwNkkNJzYibkr8sbozypapX0JSQS_RIC0QkiA0UDTmEvP9TLzDpiDVJjH7N_JtDCKzfvWScY3CBAuB9rzQnvZqf0KKFHp4-oYu5TOsN0GntITvPaB11h2kA0hO0ajx2c0YAziFuNiMFAQNi3SIriygkxn027pOEN7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:   نتحدث حاليا مع إيران والمحادثات جيدة، لدينا الكثير من الذخيرة وأود الحصول على المزيد، وأنا ونتنياهو لدينا بعض الاختلافات بشأن إيران، ايضا سأسأل بوتين عما إذا كان يرسل صورًا التقطتها الأقمار الصناعية إلى إيران. سأسأل بوتين عن التكهنات بشأن مساعدة…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/85780" target="_blank">📅 20:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85779">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
‏
ترامب
:
نتحدث حاليا مع إيران والمحادثات جيدة، لدينا الكثير من الذخيرة وأود الحصول على المزيد، وأنا ونتنياهو لدينا بعض الاختلافات بشأن إيران، ايضا سأسأل بوتين عما إذا كان يرسل صورًا التقطتها الأقمار الصناعية إلى إيران. سأسأل بوتين عن التكهنات بشأن مساعدة روسيا لإيران، وسنستخدم أموال إيران لدفع التعويضات عن الأضرار التي تسببوا بها، نحن لسنا متورطين مع الحوثيين في الوقت الحالي، ولكن إذا كانوا يمثلون مشكلة، فقد نضطر إلى التدخل.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85779" target="_blank">📅 19:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85778">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16632ab2c2.mp4?token=mMvouEfT0VR2y7evzQ8VfSBZJZMUcO6HvpupBJ0Rk5DWR8h-yxEaBcLZDTeq-9z4dA-NySdObMrbHqYrWIRO0YdiGVes0NDz1PODVncaMlOM9x5cDVE8Eypihp1sUCpu9853KlW6L8WT5KkUR-DZN4S67odSsFqBGFWlAjn4-7FoX0UI5gPen2U6L1eC-ycwAethJaP2RpKsjZv9ZjDWzyuaa8T4HMOC2UnqIcHeWQ54VWkE0sKaTndM7k0QFlVpAzHqeOhB5_JE796DxaB9WAzxVd1ElyWfNHZk_4owoEmscVC1_9m5qf9bsQwpAiXKyI7-4XaeqPLWOeCoDy34yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16632ab2c2.mp4?token=mMvouEfT0VR2y7evzQ8VfSBZJZMUcO6HvpupBJ0Rk5DWR8h-yxEaBcLZDTeq-9z4dA-NySdObMrbHqYrWIRO0YdiGVes0NDz1PODVncaMlOM9x5cDVE8Eypihp1sUCpu9853KlW6L8WT5KkUR-DZN4S67odSsFqBGFWlAjn4-7FoX0UI5gPen2U6L1eC-ycwAethJaP2RpKsjZv9ZjDWzyuaa8T4HMOC2UnqIcHeWQ54VWkE0sKaTndM7k0QFlVpAzHqeOhB5_JE796DxaB9WAzxVd1ElyWfNHZk_4owoEmscVC1_9m5qf9bsQwpAiXKyI7-4XaeqPLWOeCoDy34yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرض طوق امني حول القنصلية الامريكية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85778" target="_blank">📅 19:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85777">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هجوم يستهدف القنصلية الأمريكية في تورنتو</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85777" target="_blank">📅 19:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85776">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هجوم يستهدف القنصلية الأمريكية في تورنتو</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85776" target="_blank">📅 19:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85775">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
وزير الخارجية الإيراني:
لقد أثبتت الجمهورية الإسلامية أنها لن تخضع للتنمر الأمريكي.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85775" target="_blank">📅 19:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85774">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/85774" target="_blank">📅 19:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUOTH_aZSjaWkHzbGytjvEfR3hRGeFZL17fhBpTCW6nBCMpJyqquoMtZtGX3av_3Z5Y_KtmoNAF9eNuA_SZ2Ojm1vWWd8mSvW9LOY8sJc5GVvMPa0T7RjqoxTNXfG-E89SmHQvyDjxPh7lqf6G_llJFYXIG1HoKnhHQjpjFJfkxtWJNjryqt161qpNmLr8lRSqo4JX7vrUnl8zk1pvpEWnVV49KHZJBGrH8lPVnEvbZtOZKs-mP0lwFc2VlL-jIC841W9rlirDEtSEE-yqk3AIMpHlzmr5LWPoP3PeW1KHIXch4WIhi8Cg56VF_LUATceSzucwq06K4SMdVpq7CbVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3DFwAyfRrbWGMPGBK5IZpA8AoY4Z4-Eiow44Abrgxp5Zyy_BQ8Js9JDRIooIDV7hw-fbrgGZjhIrijlvh17kZfyHdV-zx4nQ_nUKVQeg--xVRyWFQWeDOVsV_9hUPsGsdPdSRzV5Ij8nkyFLu-YU2hBXmB_E30yQflaLebPDKZrTIKuD0kr3BkAX2aNweS0Hb76UQiJyBTOLPGmkBHiyrNQG_LzJVF9PGHHKIQ6O_SRe2cHkKFqO-9ahEQoJK68xTgeNydqB2E2r5dltZbjbnUPMZ7gXE2jj7E5KjmxqcfrLzlcZGCAYVEkI7I4KFKHRggkFUAfNUNBZMZwI_CjxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد توثق لحظة سقوط الطائرة المسيّرة في محافظة بابل العراقية وما أعقب ذلك من انفجارٍ عنيف في موقع سقوطها</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85772" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85769">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdX8kW8rsK7ptRA5Z9dkwt1LxzA5ja4tdxCbUVhz9NzH6udgcpBjTYwdSD-gwYfY9Kw_MGHMAeWi8ldnLar4soVNMjqA-6RP_xWcUVbEjyEH82nexVkjLhyUDhseagLbtAhlY2qDkYE-VllHDuEIvODqLAzr2yxPVrbquP-KYFU6UzhEn7v0HvYHVj-bDyzxlx4Ka1Y8r35a0eS5x3U7YY4pTaAi9HRYx4XnXoYnnrwNvXy-3Z7_UViXWhfjkl6KuE06Q45i_YvECqAqU03iDuuKM-jijuikJ_e9mppNIuXPgkg_2ngwyzAHtAwCDckB1xR69P0pUY7PdzL7Qd4vCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHTSEYfFyLeswwE6zaoxF8iOLXKVoQQxd16SjNnZO38P3sMqoahHsjk0Gv7H-FMzBjnoRhiboQokLUWOBfjD5J8vAjmTOxo3B601OyTGOcP18NAssVClf9Wq1nR5WBJpJcbXbXCYvRg49W-0Caf00b2CN_Y_3yzYntUEGNoUJ-RU6ShN8aReNUXy9noRlUPHEZ1rxtpUSuQ7BnqLVJy8rbm69e-Nu3FIfXvtO7Y7YVdLKdFTB5uG_NsTrQRRwQVuphzQ-gf5d3GxePJxILTVnrbYuM5GBGqq8juYQthffTFWGSZLNAdjuM3G47_mJ9YYRUPzuGM84Ce8WP0acu4s2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTAW6vbcKBQFZ3oT9g2JJLy0su12C62VWWudjY5-mG_FzGwj6wWqQM0eWBsQ2ejR2dC-ZPhSoEKbwHcsw6KAz5tLYfED6U5fTz67yd2v5Ngh_nQVehoS3Wdgv-Xw1mUR1O2oRnpnaW4nSoRFp3rfOa6yLOfD092BumvUzeDP3nIGXmThvvQpjR9-uuFpVSTBeXCLSy_kU58kcN8kihwzPnbskullotDOnBSfuRsKOwwmLeRTc5n5YVUMujG7SorxSoE9rs7aRjsGO8CHTzEQHvI5ApwPKahOEv2Ci3VSSIdKZ8-rNqXba5de3eePW3pbOVgv-BsebO7fZc1yBpmDKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
من السماء إلى تراب
بيرقدار اكانجي تحت اقدام اليمانيون …
انتاج نايا على التلغرام</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/85769" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85768">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
🇮🇶
لحظة سقوط الطائرة المسيرة الامريكية في محافظة بابل العراقية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85768" target="_blank">📅 18:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85767">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
‏ترامب: لن أمنحهم وقتاً طويلاً للمفاوضات؛ إذا لم تنجح المحادثات، فسوف نعود إلى عملية عسكرية قوية للغاية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85767" target="_blank">📅 18:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85766">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
‏
ترامب:
لن أمنحهم وقتاً طويلاً للمفاوضات؛ إذا لم تنجح المحادثات، فسوف نعود إلى عملية عسكرية قوية للغاية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85766" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85763">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJrlSeI10ax10dyO53ijY4QevkySDJcF9Lf3fUpfNfiLZ9LIocMOnaeou-HiYWYJzLWw3z6_gNvg0lLsLVXoOa84pYJwITmY_atEh1P_AOQ5xy7Qjm_gEhXYAvqepqZ6kVu0tm64vP0wNwFuF9DvanIsfgRLMqg1drYq-D-9C7P5oCOl3_ekxwskMLFeR8QJacchBzmtjiNv8XdwUSrxE-amvS7UUlqhOyu3mzupwXBiNt2HQPKSo-DXJ68CU-sa4OQipXUv5-MBzy43UPxkDFJM2VMdI-78ExxFmTuoZWF_xi-3TcZrpcqoe9llB2WlSwufvxn_F3RNwZZTVLy58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0y4jAu0xUhRzQWQDv2jKihOCcHNXeFGl4UPUqpHoiC7qliicL3fXZXNkx5CG56VOXFoMI-8zMDjnpqqOZ9sWpWGzpJsYqbaQmb-ungt_fHnPGfOFwR6AD9LQakQLQxY6XI-x0dLRFrOffQo8q2_HwKk-tp5dF1LdEUKo07ZKBN2RERFTVPhAeB_L4VMzZ429Qm_7vM--Q2ycM4Q0lUmkBMArSvqfOjgHu2JWRvR9uhosN009_qb_ejNxJdv9CmrEkAWKTwk2S_L2BacBBpvWWrshQnFUX8eeHhiu_3tBv8afx38LROcBN1vX5oKtP7w0AX5NkkqyA9raMPnsV9ecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kug_BzfJ8mI1CcDVPLF0-IJX01QsjsMByVjpRI4zAw0h2xbmOpM1WqlesQOYoaEUMnMWey8jjVr4KSr5fMghaon_3SndtjH622IGnZFRtRU9qLw6OzyAQNSP1dMtbFtr_mDuF8jL0mW2yyFdoIASQ5CXgZBRCHsagnBCkLQRG37sVjk6v3vIxY6gmWOo--G0HBE-21X40N2wTwTVKIy4Jg7av5M4_9qkfIm18a3rzarlX0qiPteSqjVXC9rnA9aXsJh-ML3QOzu8ElII-duwHTsp9uW1z5wS8WVUcjYR6rSzHiCDAJvZkuyOQotJ0972PwvQVcTk4eqPmExJrKZ7Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏الاقمار الصناعية تظهر احتراقاً كثيفاً للغاز على طول خط أنابيب المكثفات/الغاز ومواقع الإنتاج في المنبع المؤدية إلى بقيق السعودية. كما نلاحظ أضراراً واضحة في خزانات الضغط في المصفاة. ‏من المرجح أن تتأثر كل من خط أنابيب الشرق والغرب وإمدادات الغاز إلى رأس تنورة بهذه الإضرابات.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85763" target="_blank">📅 18:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85762">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
سقوط طائرة مسيرة امريكية في شمال محافظة بابل العراقية بدون اضرار.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85762" target="_blank">📅 18:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85761">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd27e2cef9.mp4?token=iIrW02xoyaCSh9Ob9iwpKUJTfZnTGvjT55dFnALYvBmVN88Fi0TesWLzIqEQJs8hXivXDnj79tIx_uo3g2fEv5F7IkNsuQqyyIjOTjxN0JtsT5an6ssT0YFFGCebyWEm_qzhxQbnrYiTe_7I9HG-Qd69mzxQnmDk9La9L_Bw4SnUBj6EUAlo-wGDU8Yko5I8hMvu_ZYD1JtimRAb3K4cD6xdERigf5_eRC_YSiS8wwf6LpV_Ct8HJi0d05dmUHQ6rwpu0AwfIhscDtpo570hDL5sj-PcvT3J-9wlcIGxUn5bYyhu2UJBGV_MhAA_x1pBAX0ofa83F41BwOke8uVW8rcSF5X2_GW_8vAGoaM6kk1kLoMGMmldP85psevbPQSGVYPSDttl2BmGk163-LnoIZvtz3dmI5yU3Ft0hd4ezzVx36vdLyzOceC5FhD5CqAa7hlZpjRY1ZWdaqsU9JRf-nevQQj1ftemodaSXscKx3n2jd0uAsGzSuODeZkMUlImWe_zHm4I9yOzH2eRZi91YfX0azeD_ozaWJKnoms-B70aiBT48bQV6EEYDhISePtUFK2Ucrc7IIjXFIx2l3gPcFZ2YRXFs09bJ7F9D-L4TuazVtPs3thuO4HdSEmQxW4p4yrQxJNQ9YwfqrFMgvtkFMz5QeDMtmjXbu11_5WKNjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd27e2cef9.mp4?token=iIrW02xoyaCSh9Ob9iwpKUJTfZnTGvjT55dFnALYvBmVN88Fi0TesWLzIqEQJs8hXivXDnj79tIx_uo3g2fEv5F7IkNsuQqyyIjOTjxN0JtsT5an6ssT0YFFGCebyWEm_qzhxQbnrYiTe_7I9HG-Qd69mzxQnmDk9La9L_Bw4SnUBj6EUAlo-wGDU8Yko5I8hMvu_ZYD1JtimRAb3K4cD6xdERigf5_eRC_YSiS8wwf6LpV_Ct8HJi0d05dmUHQ6rwpu0AwfIhscDtpo570hDL5sj-PcvT3J-9wlcIGxUn5bYyhu2UJBGV_MhAA_x1pBAX0ofa83F41BwOke8uVW8rcSF5X2_GW_8vAGoaM6kk1kLoMGMmldP85psevbPQSGVYPSDttl2BmGk163-LnoIZvtz3dmI5yU3Ft0hd4ezzVx36vdLyzOceC5FhD5CqAa7hlZpjRY1ZWdaqsU9JRf-nevQQj1ftemodaSXscKx3n2jd0uAsGzSuODeZkMUlImWe_zHm4I9yOzH2eRZi91YfX0azeD_ozaWJKnoms-B70aiBT48bQV6EEYDhISePtUFK2Ucrc7IIjXFIx2l3gPcFZ2YRXFs09bJ7F9D-L4TuazVtPs3thuO4HdSEmQxW4p4yrQxJNQ9YwfqrFMgvtkFMz5QeDMtmjXbu11_5WKNjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مشاهد للطائرة المسيرة الامريكية التي سقطت في منطقة المويلحه ضمن محافظة بابل العراقية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85761" target="_blank">📅 18:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85760">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004bc022b2.mp4?token=OyrLV84JV2Nn9HLhiItHXowaxPva7TOrskT9wj5RJ1AKa3rTlffy2yAr6af_e-DD575j7duwqnJuCvsQh509Fp0n0IurnWBt-4UqDLxRKMtIwBd9piiF2aMZUAZyaDp8a9lbkAr-tlCrN565mWrSRwUh12BZk8Hpt6OIx9u8_gEJqnmIptCfOQdZhiTc79LqhyWu_DdwSm5xnjkyQDYGwzvBK8cut8d3KE2s44OR51i_JErFZAO8r8oHHesQlN6P_ZSFCeSnTqD0D63bqWzhhr5SC2vVPaa0qBX8vMmCjy5L-e-Dr9qfOFyLfauwDGA8lHwkUVwa3ldDknx2_L1s6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004bc022b2.mp4?token=OyrLV84JV2Nn9HLhiItHXowaxPva7TOrskT9wj5RJ1AKa3rTlffy2yAr6af_e-DD575j7duwqnJuCvsQh509Fp0n0IurnWBt-4UqDLxRKMtIwBd9piiF2aMZUAZyaDp8a9lbkAr-tlCrN565mWrSRwUh12BZk8Hpt6OIx9u8_gEJqnmIptCfOQdZhiTc79LqhyWu_DdwSm5xnjkyQDYGwzvBK8cut8d3KE2s44OR51i_JErFZAO8r8oHHesQlN6P_ZSFCeSnTqD0D63bqWzhhr5SC2vVPaa0qBX8vMmCjy5L-e-Dr9qfOFyLfauwDGA8lHwkUVwa3ldDknx2_L1s6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سقوط طائرة مسيرة امريكية في شمال محافظة بابل العراقية بدون اضرار.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85760" target="_blank">📅 17:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85759">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada0a48777.mp4?token=iqHRSvv9yBcdYviLVRsquzuZnPXEWB_A8gHvPFMgUlPICOEXVd0kkXRJ5WUyO6l_MKJigEyuvRaUmd8iVs1d_OCO3RI0p2TLX9DJpcIFvS-CfWI5-EnbH3oNfDE5WZpkzoYlwH4rzP7rlLbBJXiBk2dCded-yz2xmbWJZAmHLCwN0IJsmn3sw7BM09DOpMKkWrapAkHoHk4-vb-UV_kHjn0utdl5a_XoaEp_0kCjMioIKDv9haoRWU0MVHL5N6sUbIOaDSkqSRQLtKEMswYg8z1EMWxVXaBOrJ8gpI6JOaujuoFBE0u_Y0m3pOfnT3_jaU64CQDjvN_twH5Pgptc1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada0a48777.mp4?token=iqHRSvv9yBcdYviLVRsquzuZnPXEWB_A8gHvPFMgUlPICOEXVd0kkXRJ5WUyO6l_MKJigEyuvRaUmd8iVs1d_OCO3RI0p2TLX9DJpcIFvS-CfWI5-EnbH3oNfDE5WZpkzoYlwH4rzP7rlLbBJXiBk2dCded-yz2xmbWJZAmHLCwN0IJsmn3sw7BM09DOpMKkWrapAkHoHk4-vb-UV_kHjn0utdl5a_XoaEp_0kCjMioIKDv9haoRWU0MVHL5N6sUbIOaDSkqSRQLtKEMswYg8z1EMWxVXaBOrJ8gpI6JOaujuoFBE0u_Y0m3pOfnT3_jaU64CQDjvN_twH5Pgptc1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سقوط طائرة مسيرة امريكية في شمال محافظة بابل العراقية بدون اضرار.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85759" target="_blank">📅 17:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85758">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇶🇦
وزارة الخارجية القطرية:
ندين بشدة محاولة استهداف منشآت نفطية سعودية بطائرات مسيرة انطلقت من الأراضي العراقية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85758" target="_blank">📅 17:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85757">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">على عكس اتهامات السعودية للعراق   اليمن تتبنى هجوم على بقيق والرياض</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/85757" target="_blank">📅 16:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85756">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjxZjMeyBwAaIdwcZiyAenPicIFroKpGtb4s41XNGUn17QVocBzMKt4xkPra45BLR6Ly4JK8NZQLKIH0Wqn7IHux4KZqgWePFfiyNvdfSjofMQ2ike0cAQQInPq-EBNIHZP3cjaY0JJij5BhzXvVJ9boYza9tBCk5IF944lfdDh59jiGX8AkHHqRflB-yUEKvbkLLrIRDI9Atmwsqet5KqOf0U44NurPTtVxq0ByxZsaNzLrf5ZEeiJB_FrT8mroI28nL_f44XKbYqY7u1-FQMYRecTwX_iTlPmQADKcN1EDN2r5fUk0e1QydEb0NWiAjG-kYg2ndBvBMkZR07j-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة مسيرة من طراز Mq-4c تطلق نداء 7600 (طوارئ عالمي) فوق تل ابيب بعدما كانت تعمل قرب حدود ايران</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/85756" target="_blank">📅 16:46 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
