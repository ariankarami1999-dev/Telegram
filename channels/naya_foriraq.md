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
<img src="https://cdn4.telesco.pe/file/AstfgjoVRdBNcp2eyoDxFkiqslyTkqayzZzjQON3y6UzTxV4krkmMDfSC90DwHi2QnuymwPQUB0gwfLU8ze04ZGGy1VMs7MVo7f9NaGLVufi4A4KLnvTuRfPV_RtRD3rD5MOE4orp-i1tp16mXI4W-UkudZeGvgZ_xqzZtR_qde2KTljTXZJKdAkRxSLsmvvfvGlZXSUOZ4LwDvNnlFKEbUnjnWDPL432GTUMytuDHEvNgicb30ZVn_CkgGpqCO_o6VZykna1TEFJvfrpwAi3WiFf-0USUq_RV9uyWgovvm9AmA0i35kvrt3ZtOkt2RAdZNCYI0eP4Qv57BTAU0PjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-89529">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇷🇺
‏
الكرملين:
من المبكر جدا الحديث عن استئناف الحوار مع أوكرانيا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/naya_foriraq/89529" target="_blank">📅 13:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89528">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني كاتس: أصدرت ونتنياهو توجيهات للجيش الإسرائيلي بالاستعداد لحرب شاملة في الضفة ردًا على عملية الطعن.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/naya_foriraq/89528" target="_blank">📅 13:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89527">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جيش العدو يعلن استشهاد المنفذ  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/naya_foriraq/89527" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89526">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇱
اعلام العدو يزعم اعتقال المنفذ بعد العثور على سيارته بالقرب منها حيث جرى إطلاق النار عليه بعد محاولته طعن قائد القوة.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/89526" target="_blank">📅 12:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89525">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني
كاتس:
أصدرت ونتنياهو توجيهات للجيش الإسرائيلي بالاستعداد لحرب شاملة في الضفة ردًا على عملية الطعن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/89525" target="_blank">📅 12:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89524">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇱
حدث امني داخل الكيان الصهيوني   أولي: قبل قليل، وصل فلسطيني بسيارة نقل إلى مزرعة "معوز" في الضفة الغربية وطعن مستوطن ؛ المستوطن بحالة خطرة   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/89524" target="_blank">📅 12:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89522">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇸🇦
🇾🇪
تمكنت القوات المسلحة اليمنية بفضل الله من إسقاط طائرة استطلاع مسلح نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية صباح اليوم في أجواء محافظة البيضاء، وقد تم استهدافها بسلاح مناسب.
وتعد هذه الطائرة هي الثالثة التي تم إسقاطها خلال ال24 ساعة الماضية بفضل الله وتأييده.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/89522" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89521">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aef4dfe9d.mp4?token=VrSBtC4I4Boc2YOCMD9Vb28-GZjRtnRZsqQGrBwkffp4cGsaqNTiYRQcFoGlOS6mzjiATVMlwijdZnEbcx2lM2EA3N6T9Nyd3uNi1VQfkOGpMZvfcUB29RzHZTLzxv9r6BLlS09oGg0FASXrvM-Iw7AzxFAyh6Q1Jg68cz_DuTItsXV8Q1UrwbDmw3yzkN2Kxvb5Yjn8teFyPNIUYagxw-6-ua6L3sHLZVzfu_q1Nyp92xIe_a6PWYpzOMHUMfBPzOFi6gbxXbkK0D5KpFrN6GHMNpRPvhkHDB9YKBrIyc7burbZ7R4ma0hqGwJk7L8AtywD0aTxWNlO8ShkTpm8eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aef4dfe9d.mp4?token=VrSBtC4I4Boc2YOCMD9Vb28-GZjRtnRZsqQGrBwkffp4cGsaqNTiYRQcFoGlOS6mzjiATVMlwijdZnEbcx2lM2EA3N6T9Nyd3uNi1VQfkOGpMZvfcUB29RzHZTLzxv9r6BLlS09oGg0FASXrvM-Iw7AzxFAyh6Q1Jg68cz_DuTItsXV8Q1UrwbDmw3yzkN2Kxvb5Yjn8teFyPNIUYagxw-6-ua6L3sHLZVzfu_q1Nyp92xIe_a6PWYpzOMHUMfBPzOFi6gbxXbkK0D5KpFrN6GHMNpRPvhkHDB9YKBrIyc7burbZ7R4ma0hqGwJk7L8AtywD0aTxWNlO8ShkTpm8eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار كبير للقوات الأمنية خلال إنطلاق تظاهرة إحتجاجية لخريجي معاهد النفط أمام مبنى وزارة النفط في العاصمة العراقية بغداد.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/89521" target="_blank">📅 11:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89520">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a0805be6.mp4?token=BViMWzFk7T8VBnjQsCgwh0P1Bu51KcxvRYT68yh8H0qriU_6Fo_SobhXgOCidBs9pUG1P4-rNOCy1g41bTdIHnRL-aPUlBeCOsYcEeR7yEWKoO8TilKJHqCWamoKAynX1wDoQSBxDyICXUKKPwybAjHXfA36OwTaBOIkpy9kk89Eas6P-oP7Hx08Sez7AZvZo_V7gALHzlUNJY-5IYrx7IA2BfLkl9WbqcnIYv1wpFqwQdHIvljL9JSlPa_3uVkuo1c9ly6fplq05MeN-th8qBU8e4Uh_0lkmbo0r_lLCD-xmE7lqLqQS9EAO3WQaNa-UweDqn507MC7RgedmBrTrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a0805be6.mp4?token=BViMWzFk7T8VBnjQsCgwh0P1Bu51KcxvRYT68yh8H0qriU_6Fo_SobhXgOCidBs9pUG1P4-rNOCy1g41bTdIHnRL-aPUlBeCOsYcEeR7yEWKoO8TilKJHqCWamoKAynX1wDoQSBxDyICXUKKPwybAjHXfA36OwTaBOIkpy9kk89Eas6P-oP7Hx08Sez7AZvZo_V7gALHzlUNJY-5IYrx7IA2BfLkl9WbqcnIYv1wpFqwQdHIvljL9JSlPa_3uVkuo1c9ly6fplq05MeN-th8qBU8e4Uh_0lkmbo0r_lLCD-xmE7lqLqQS9EAO3WQaNa-UweDqn507MC7RgedmBrTrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حدث امني داخل الكيان الصهيوني
أولي: قبل قليل، وصل فلسطيني بسيارة نقل إلى مزرعة "معوز" في الضفة الغربية وطعن مستوطن ؛ المستوطن بحالة خطرة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/naya_foriraq/89520" target="_blank">📅 11:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89519">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur9T2dcgmrKlFZM7DNskt5DiNpNf7uazUVXz6mNlHnDNKMCeeCgt_05jcHeckbF6mtVggQxSdqNPu2xQF8wMj0JesJtVBerwwGem9-5DgcelsiuYOmQ2eKFHV67ahZOeMmZifR59i5DhFfcjfk6ttIOL2JygT19csbpXoRqPDclSDWXmfxzkcFgn-DUarYqMqaQRR7p3wdx02rOZmdalELI2MdVM_baGq4meQdu1i6v8tVB_f4-XMqDdC3cXQEaYoCEDxwvfG1ct_P8Tqky-nJDznVMn47uzX1OM7wNKZn164EZOMGnknKXKACOEEDKUaW2jGCkkiZzONy_XqnDi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوربا تنهار ببطىء   ‏يتصدر حزب البديل من أجل ألمانيا اليميني النتائج الأولية في انتخابات ولاية ساكسونيا-أنهالت ؛ الحزب يعتبر نازي وعنصري متطرف ويرفض الحرب ضد روسيا وحرب امريكا في ايران</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/naya_foriraq/89519" target="_blank">📅 11:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89518">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏
🇮🇷
🔻
المستشار الرئاسي الإماراتي قرقاش : التعامل مع إيران لا يزال قضية محورية بالنسبة للإمارات العربية المتحدة ودول الخليج الأخرى.
- من غير المقبول أن تتعرض ناقلات النفط والسفن للتهديد المستمر في مضيق هرمز
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/89518" target="_blank">📅 10:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89517">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لاول مرة   النفط يلامس ٩٨ دولار للبرميل الواحد  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/naya_foriraq/89517" target="_blank">📅 10:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89516">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇱
إعلام العدو
: بعد أسبوع من إعادة فتح الشواطئ في حيفا: وزارة الصحة تحذر الجمهور من السباحة في شاطئ كريات حاييم حتى إشعار آخر، وذلك بعد تلقي نتائج ميكروبيولوجية غير طبيعية في فحوصات جودة مياه البحر، والظروف التي أدت إلى ذلك غير معروفة في الوقت الحالي.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/naya_foriraq/89516" target="_blank">📅 10:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89515">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
طيران مسير إنتحاري يستهدف محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/89515" target="_blank">📅 10:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89514">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992b2e12ce.mp4?token=dq9KVtGJ5P4PcUtH1J6BeJgnAxqkGZwg0qzjQH-EsE5PknSmKmOWS2-uLGVBZdp-WinpQ1p6ulln8vLBk0YYfruSzgcQOkf5n0uRNbkxis36E6YYUWu7ksl3ENqy9kHeocOx-XC4bgDMl1H-KzPnO7ZKZ7HRgGBpX_TjiO32fjTQsmbH0JxSgUwFe3hwv_mkd6-YQB8Iz2e9nwkSwbYjMDDh7P53I02YEOKuBLonhfqJvnXYnvbXOo32dTRVtyJ11xdMtMOXylL-pDyUJ-FugZE2CdNZb94VlwT7r3_JgMP7K_nBt5CgisBSnLPDxrW4XoQ0s3CtAI8d51qIabunEwFKiUkCLItyg0wqu9hKDh_5YJa4IXD0VahNDq2ADq5dTYw1c8P5uO9YTONjB4cIC2lx1Q4Ieydj6-pbzyNVtDmZUMfgMrGBN-Mab6cGa_pp2KQp3lwXKfVxLwOUX8ofQiw-g0BmaBCW150R8oB66fsz8keW4p3kqpuUQyuMKi7HNx3RWsV3s6H-2sbbU_u0Sxk268RiDRrHrMOS3VSdjifDXAUQ6_qguUtsyis5ia-fxlIz5_k9Q7pIQpUgd7g0PokRKcrLLiwF2WN-GnObMqnlGsrggQUcwm7uWaNOPZId_JDOHO7aWWnL5WfeQ228YOGx_fEQ1GinAjuOxlP6Fjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992b2e12ce.mp4?token=dq9KVtGJ5P4PcUtH1J6BeJgnAxqkGZwg0qzjQH-EsE5PknSmKmOWS2-uLGVBZdp-WinpQ1p6ulln8vLBk0YYfruSzgcQOkf5n0uRNbkxis36E6YYUWu7ksl3ENqy9kHeocOx-XC4bgDMl1H-KzPnO7ZKZ7HRgGBpX_TjiO32fjTQsmbH0JxSgUwFe3hwv_mkd6-YQB8Iz2e9nwkSwbYjMDDh7P53I02YEOKuBLonhfqJvnXYnvbXOo32dTRVtyJ11xdMtMOXylL-pDyUJ-FugZE2CdNZb94VlwT7r3_JgMP7K_nBt5CgisBSnLPDxrW4XoQ0s3CtAI8d51qIabunEwFKiUkCLItyg0wqu9hKDh_5YJa4IXD0VahNDq2ADq5dTYw1c8P5uO9YTONjB4cIC2lx1Q4Ieydj6-pbzyNVtDmZUMfgMrGBN-Mab6cGa_pp2KQp3lwXKfVxLwOUX8ofQiw-g0BmaBCW150R8oB66fsz8keW4p3kqpuUQyuMKi7HNx3RWsV3s6H-2sbbU_u0Sxk268RiDRrHrMOS3VSdjifDXAUQ6_qguUtsyis5ia-fxlIz5_k9Q7pIQpUgd7g0PokRKcrLLiwF2WN-GnObMqnlGsrggQUcwm7uWaNOPZId_JDOHO7aWWnL5WfeQ228YOGx_fEQ1GinAjuOxlP6Fjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تصاعد أعمدة الدخان من مقرات الإنفصاليين في محافظة السليمانية شمالي العراق، نتيجة هجوم بطائرات مسيرة انتحارية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/89514" target="_blank">📅 09:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89513">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏وقع انفجار للألعاب النارية بالقرب من كنيسة مكسيكية خلال احتفال ديني، مما أسفر عن مقتل ما لا يقل عن 10 أشخاص وإصابة 64 آخرين
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/89513" target="_blank">📅 09:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89512">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لاول مرة   النفط يلامس ٩٨ دولار للبرميل الواحد  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/89512" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89511">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruZE49Zv0u3jAyktXWIl_iXgM3uTXGhMe8q4gv5_coXtDBx8gXvgsroC3SPpsf8o63uJmDTXQowBjrMxYY_4xoiQZ6dACz4xXAZ28WGcOoyZdv78LvWg1F1KLWO2314mzWLkefFs0M3Bc26Tsq5ha1SQExm0xUKyxfpfLrxilzjMKhwCfDhwAfNutq4aLSV6jEro6oMr3l_CfHMxSaCzMy3ol28yfe2d6jNPIrCOXW2xKWjFvsR8MxBU2fEW3vfDJNdpfWQ8zCaSlrfqEDsAZcykXXjmjLpn491hoVGZ4URRb1BHNkpZwS03QjsRwbBSDeWC9twM_H2sJzoIRmYbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاول مرة
النفط يلامس ٩٨ دولار للبرميل الواحد
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/89511" target="_blank">📅 08:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89510">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc56be204.mp4?token=I6-v3tg4kybhbYqCXg5YDPB8GJDdP-K7ztsUIqByAzUqjUfJ_V0efxokMSKXrMId9I--o4M4HleqhOJTLNpdY30gCRwNiEE5vdt7QANETXRQTVSThuPHGdgLZZgXxVZ-1LC-l0eMxtvsxkHtQQe1ACwT7yWns_gLRWFWnLwBdCJXMwKucomO_A2Hn_Hclf5r2ZxEcU9j9y0oTHhes8k5WCVtmLWBAfMTRryP0mtwXCPH9Rb9HfgwIVdBHosL1fkvyi23wuT0KmyIMmhPansQFXt11r-FsauClnn4OYTfW7F8rzAIqA8lFIUAWabnqkv43rwaRSL6XJ6evYNVJ44KGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc56be204.mp4?token=I6-v3tg4kybhbYqCXg5YDPB8GJDdP-K7ztsUIqByAzUqjUfJ_V0efxokMSKXrMId9I--o4M4HleqhOJTLNpdY30gCRwNiEE5vdt7QANETXRQTVSThuPHGdgLZZgXxVZ-1LC-l0eMxtvsxkHtQQe1ACwT7yWns_gLRWFWnLwBdCJXMwKucomO_A2Hn_Hclf5r2ZxEcU9j9y0oTHhes8k5WCVtmLWBAfMTRryP0mtwXCPH9Rb9HfgwIVdBHosL1fkvyi23wuT0KmyIMmhPansQFXt11r-FsauClnn4OYTfW7F8rzAIqA8lFIUAWabnqkv43rwaRSL6XJ6evYNVJ44KGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار كبير للقوات الأمنية خلال إنطلاق تظاهرة إحتجاجية لخريجي معاهد النفط أمام مبنى وزارة النفط في العاصمة العراقية بغداد.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/89510" target="_blank">📅 08:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89509">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa43e52504.mp4?token=shNAwmR9aZ0ZSpVjedA8NRpxmd1xBf2PubCodpYsGqgeHKFKNGNbztp683I69OQ1qJ2uUslcVgH0msbm6wPkslKL2jMqyowUzbemvOBemXxPg1l8Pdow4bkKvPj96yVPtkRDz1vDJ0CvY_MhpJ7Bh_-qv8Cikt0DGztFcmxwBKAjtBgoY7hSHk1Q2sBJhvf2RtHQofEDwf2w8RxWi13pEflTHg1gsRVemWORbgLZ_vLDYzzCEE3yDmgUxKB_fRnAn5wwKxRKeZAqG9Le5Hc43n4GnzsUN3xfKAFQsZLwDWpZH80G5Y5wDjmyhE_cjbSzG7R4-K1q06XSRi5N28RNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa43e52504.mp4?token=shNAwmR9aZ0ZSpVjedA8NRpxmd1xBf2PubCodpYsGqgeHKFKNGNbztp683I69OQ1qJ2uUslcVgH0msbm6wPkslKL2jMqyowUzbemvOBemXxPg1l8Pdow4bkKvPj96yVPtkRDz1vDJ0CvY_MhpJ7Bh_-qv8Cikt0DGztFcmxwBKAjtBgoY7hSHk1Q2sBJhvf2RtHQofEDwf2w8RxWi13pEflTHg1gsRVemWORbgLZ_vLDYzzCEE3yDmgUxKB_fRnAn5wwKxRKeZAqG9Le5Hc43n4GnzsUN3xfKAFQsZLwDWpZH80G5Y5wDjmyhE_cjbSzG7R4-K1q06XSRi5N28RNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مسير إنتحاري يستهدف محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/89509" target="_blank">📅 08:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89508">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
طيران مسير إنتحاري يستهدف محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89508" target="_blank">📅 07:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89507">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇾🇪
القوات اليمنية:
تمكنت القوات المسلحة اليمنية بفضل الله من إسقاط طائرة استطلاع مسلح تابعة للعدو السعودي من طراز CH4 أثناء قيامِها بأعمال عدائية في أجواء مديرية خب والشعف بمحافظة الجوف، وذلك بسلاح مناسب بفضل الله.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89507" target="_blank">📅 06:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89506">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf13f32be7.mp4?token=BpN-S04C_zi3O4qxCsRc6fgiSvqZxiv856B5CA5SblFJ9gRnG8XBRacE2E8mwttw4luVoKfjaufA7oFMASqwkYvTuXqA78cf9HyRnZdoUs03uLwapEcyWyfkQqnVwvH8noILxO6rrXygLL0hqmN41ARaFN4OolocvAlvK6Yzcd2j4pW3nXcnVM8z0YjyJSqhT9pPBegsRXZG1p03AKzGSGYQL2LFuI8dRM1iBVcnkC-RhXL_-wuNEfcfrhOVi3i9_3YpJPwhJ5dvy8gTi_wwfI_t39YenwsMm-fHqfvWJJWlNmwjOAttED_XoQUKEx69IPxv3w9Jg1fOZX5NezcQvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf13f32be7.mp4?token=BpN-S04C_zi3O4qxCsRc6fgiSvqZxiv856B5CA5SblFJ9gRnG8XBRacE2E8mwttw4luVoKfjaufA7oFMASqwkYvTuXqA78cf9HyRnZdoUs03uLwapEcyWyfkQqnVwvH8noILxO6rrXygLL0hqmN41ARaFN4OolocvAlvK6Yzcd2j4pW3nXcnVM8z0YjyJSqhT9pPBegsRXZG1p03AKzGSGYQL2LFuI8dRM1iBVcnkC-RhXL_-wuNEfcfrhOVi3i9_3YpJPwhJ5dvy8gTi_wwfI_t39YenwsMm-fHqfvWJJWlNmwjOAttED_XoQUKEx69IPxv3w9Jg1fOZX5NezcQvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇮🇱
إستشهاد طفل بعمر الشهرين في بلدة كفررمان بجنوب لبنان جراء العدوان الصهيوني الغاشم.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89506" target="_blank">📅 04:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89505">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1633213891.mp4?token=DW4ymDJuN11_gXQu1JnToKz_8h55rPPxNEIfBA3PnQfE0b7bxSxQ_WPefHxr6iGcY-OA-CZAAoB0e18Gk2kOm8oJPsesagTq4OWZBoYw0zMD6VuN4u1YuhJuCO4lxJXPYcOfWjNElONYEYTAj3FkWEjAokpfn-aSfZpXv71iC8Ir8bdyLNyEazhsT3Zd-QZbboAMKMWH5UHSZ7gkp2JBb18ycATt9Pdk_gkfHlVmd8GyOh7ftQRaGEVLPI72t-101uylQ9qcw75f9LvJ1pa7fiqUUWX1fodYRfaBJkjqpq8SKrnySN1LpMTw7h25fJzqWKSnCH6f9frbQFUVVozpYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1633213891.mp4?token=DW4ymDJuN11_gXQu1JnToKz_8h55rPPxNEIfBA3PnQfE0b7bxSxQ_WPefHxr6iGcY-OA-CZAAoB0e18Gk2kOm8oJPsesagTq4OWZBoYw0zMD6VuN4u1YuhJuCO4lxJXPYcOfWjNElONYEYTAj3FkWEjAokpfn-aSfZpXv71iC8Ir8bdyLNyEazhsT3Zd-QZbboAMKMWH5UHSZ7gkp2JBb18ycATt9Pdk_gkfHlVmd8GyOh7ftQRaGEVLPI72t-101uylQ9qcw75f9LvJ1pa7fiqUUWX1fodYRfaBJkjqpq8SKrnySN1LpMTw7h25fJzqWKSnCH6f9frbQFUVVozpYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇱🇧
جيش الإحتلال الصهيوني يصدر إنذار إخلاء في دير الزهراني بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89505" target="_blank">📅 03:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89504">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG7-I-9Fe1KTD-QTuWtpYus6QPuMZQNrSFTB0Xa01D8FF7x--gyeRMYXUHWNO1B1y1z3HnixFzB7qpF4efLHUlxga5NA4sNucuviCbyOuWR-fVnUHOvw4Uw0O9JrY0A99KSsTWE79kkyAc2OFnXqPOwiaISoN5jGOGUBI6diDp11daruildBXx9VyjuSlVf9Gi5yg-d8C3c7WjjVJIAXD7Ce2-PRYBDc7Oupim1yJtqYs1gqkosQ7PBNlscrVYIcyMfdsmOJghg2F2RIu5OIA7B1yxI92Cut0HthGbxRtEs4foSomLY2FDOY_RezMFwDRbrQq7aCtekJT1jEd28aDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
جيش الإحتلال الصهيوني يصدر إنذار إخلاء في دير الزهراني بجنوب لبنان.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89504" target="_blank">📅 02:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89503">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVz7QPyhbzoxn-FncCeBdIwfkSV2jaQikdYN-s5cov9sCLH1SMD1w5EAgxuJs10pCu7w26TJ35NDb_JWXan9DpD3qIEPwKyWJukouYq0_Q7pCKQXDmwK9fAt6iqjBiz-f4yJdsjFEIumNdA4mzQSDN7rAe9Xs_BExWi_I1OH8XjmcsQo7xRJToMfC-Ny0WfVbRxkrK9KVTxl9IsMxxDxhcGcN4xN-VQGW7pmlr1Ta5kvsBUcfapOYSMpDUeXo2Hvs9fVf7NXgMAm9XMmyOfuLIa-eiWe6cExuL1awQ6DkvX73cS_e4OMdI7UAPOvuqISgkRsLeC_GoYF55Sk7q_eVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تبدأ بالإرتفاع وتلامس 97 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/89503" target="_blank">📅 02:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89502">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
🇺🇸
المتحدث باسم وزارة الخارجية الأمريكية:
"
لقد انطلق العراق في مسار جديد تحت قيادة رئيس الوزراء الزيدي، وذلك في شراكة كاملة مع الولايات المتحدة. وكما أوضح الرئيس ترامب خلال استضافته الزيارة التاريخية لرئيس الوزراء الزيدي في 14 يوليو، فإن الولايات المتحدة تدعم بقوة رؤيته لضمان مستقبل أفضل لجميع العراقيين خالين من الإرهاب، ومنع الهجمات داخل الأراضي العراقية ومنها، وتحقيق شراكة أمريكية عراقية قوية ومثمرة للطرفين".</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89502" target="_blank">📅 01:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89501">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217b61cb81.mp4?token=i1EtJqeKpTa5s5X25m_ad3b16m0-Q1XfnogU3jGg8p0QbS71b6SZ_XMa9ujiBVGY5f09sIK5_ySm6jLr2wmqpLQQVdXMMVU1MVLsHKxPfBnOPxBTPcQhpEZnxTnxzRTvgAngTesbVLI1Rk4G62HTaYbNE9jjOLNlIYgRLJwRTWhrUwiPon_Ru7Tm_QAFf-bit1dRWOpjBlmHuOqjlOqv809lcopUrO0CTWdI3yyszccV70-aOwlwVi-v1H7_U4aSrV40OSK5w9VnlVPmB857pLYfxSCYBRAR4k8yf6LAC-GUJ2HrP7jtZECGOrau5RX355O2cPQu4fwX8BpoLZ5Iig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217b61cb81.mp4?token=i1EtJqeKpTa5s5X25m_ad3b16m0-Q1XfnogU3jGg8p0QbS71b6SZ_XMa9ujiBVGY5f09sIK5_ySm6jLr2wmqpLQQVdXMMVU1MVLsHKxPfBnOPxBTPcQhpEZnxTnxzRTvgAngTesbVLI1Rk4G62HTaYbNE9jjOLNlIYgRLJwRTWhrUwiPon_Ru7Tm_QAFf-bit1dRWOpjBlmHuOqjlOqv809lcopUrO0CTWdI3yyszccV70-aOwlwVi-v1H7_U4aSrV40OSK5w9VnlVPmB857pLYfxSCYBRAR4k8yf6LAC-GUJ2HrP7jtZECGOrau5RX355O2cPQu4fwX8BpoLZ5Iig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
الجيش اليمني: "
ابتعدوا .. المعركة أكبر منكم"
فلاش 1448هـ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89501" target="_blank">📅 01:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89500">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
انفجارات في محافظة تعز</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89500" target="_blank">📅 00:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
بقائي
:
كان مضيق ‌ هرمز  مفتوحًا على مصراعيه حتى 28 فبراير، عندما هاجم ‌ اسرائيل إيران. شنت واشنطن حربًا غير شرعية ووحشية على المنطقة، وعطلت حركة الملاحة التجارية الطبيعية؛ فتوقفت ناقلات النفط، وتعطلت التجارة، وارتفعت أسعار الطاقة.
‏تحاول الولايات المتحدة الآن تحميل العالم تكلفة اضطرابٍ من صنعها، ولصق التهمة بإيران. ففي رواية واشنطن، يجب إعادة صياغة حربٍ أشعلتها الولايات المتحدة بطريقةٍ ما على أنها "ثمن سلوك إيران على العالم".
‏بدأت أمريكا الحرب لكنها تتوقع من العالم بأسره أن يدفع الثمن، بينما تصور إيران على أنها المتسببة في هذه الفوضى.
‏هذا أمر سخيف للغاية!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/89499" target="_blank">📅 00:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
إشتباكات بين القوات الأمنية الإيرانية وعناصر إرهابية في مدينة زاهدان جنوب شرق إيران؛ إستشهاد 2 كحصيلة أولية.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/89498" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89497">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBacNFtAflWLYQIjUrzQiBK_VLWLL5einUndvn78OQdWaIex6R5j3Yllaqxx2QkbCGx99KXDsuxpXxExvKGa68rJMo78F1VKlBu4Zad3WJmE19Szue-KkqJvdxRYSjiLxQwwpnAQ6pRYrxJVLUn1DP9i_3n3Hen5GxDNqSw-BFpiSbiCrjP-wF4yQY2bHU6zgnpMBh_XQyQXCUxuj2xO_YA_irQa4_IsHJvTRRMDcfcRSjw7mKzgFYB5oAelq-LwNVSOubFGwrMNbPoBySfP-WPtqee8nmBLlcEj3bVArU9nZdFBK3FYp_2Flwpw70g_aMMno0phQlCVl7_f9fJl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أنا التاريخ الأصلي روحوا گولوله
انه بالبعث لاعب ميت الف جوله
٩ بدر بالميدان
🔻</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/89497" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89496">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoDWBzNHr3IveTrbnnSU-vNmlvk-oPsKKYLjjpQOdWii9W-Ot7si93SYpzLt9cO_WttmEmSsymV_1uXzHwrDHPebj8MVo5qeHaOOdfOqJ2YcsD41ZvBt1PF2yBoNfAxm8EXwzzj9Uo3ckC4hoOe2BnpxNWxVZ3iw94upGwUJoVLiN-BRwdSDVzrJempK9yHpG1XIufVIVCKWnJJLqvqJZbGABc-Bh5i92NsFd977AiYLjDvWO-exSEfoGc125DXCtEtFg3_873A3I4ISRalEfb30BAmO5IHq0DFjV-C_UoXxSllc0JhfLJfiPONgQyYZ_-6NN16b-ihdo4grFRQq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
بدأت فعالية ترامب الاسبوعية بنشر صور مولدة بالذكاء الصطناعي لا تمت بصلة في الواقع.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/89496" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
‏
ترمب
: كميات النفط التي تعبر مضيق هرمز عادت لمستوياتها السابقة.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/89495" target="_blank">📅 22:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54cb8764d1.mp4?token=rLc5Rypu6BpTAegLBVZpALKQwz1cg96QPgqoKEPv7b_Qy4mQsv5lK2EtAl8NURo_yyluxzDZu3WpKennsi_KuIr5LEp4suMmpeLOLb1yJ3_Lu9UXb2bv1JirPHxgZ_JqJzP2cYpxKl6Umnkwf6eIjyM2lTXIfua7F7JKA320yPz-UHxM5u1SmbEHnRUB6GN41hTSGd0A9z1DjPnip2vhRoVutQ8lA60QLOLZSJbPglkfiQXFL_51K4XWR6n_zs7oPo9170f1hkGwp5IQtrbE1QhyPdhSIjrG0gknOczsLhceTGiLKvv8zSVBT01Hv0aJggOV8DZkrfxlDK2wSN5zZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54cb8764d1.mp4?token=rLc5Rypu6BpTAegLBVZpALKQwz1cg96QPgqoKEPv7b_Qy4mQsv5lK2EtAl8NURo_yyluxzDZu3WpKennsi_KuIr5LEp4suMmpeLOLb1yJ3_Lu9UXb2bv1JirPHxgZ_JqJzP2cYpxKl6Umnkwf6eIjyM2lTXIfua7F7JKA320yPz-UHxM5u1SmbEHnRUB6GN41hTSGd0A9z1DjPnip2vhRoVutQ8lA60QLOLZSJbPglkfiQXFL_51K4XWR6n_zs7oPo9170f1hkGwp5IQtrbE1QhyPdhSIjrG0gknOczsLhceTGiLKvv8zSVBT01Hv0aJggOV8DZkrfxlDK2wSN5zZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رضائي
:
قبل 48 ساعة، ولأول مرة، اختبرنا صاروخاً إيرانياً مضاداً للسفن فوق سفينة حربية أمريكية.
‏لقد خلق هذا الصاروخ الخاص "جحيماً" للأمريكيين، ففروا هاربين.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/89494" target="_blank">📅 22:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
امرأة تخالف طابور الوقود وتتسبب باعتقال مدير محطة في كركوك
🇮🇶
امرأة تخالف طابور الانتظار وتحاول الحصول على حصتها من الوقود بالحيلة فيما امتنع مدير محطة البنزين في محافظة كركوك شمالي العراق عن تزويدها بالوقود إلا بعد التزامها بالطابور لتجري بعدها مكالمة هاتفية  قبل وصول قوة مجهولة قامت باعتقال مدير المحطة ويقال انه قد انشمر ورة الشمس</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/89493" target="_blank">📅 22:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qImOWKHHo3CoucN21tOYkVyWQh8Ux5fSDClcchFmClDyJ-N6MLv3QZjKoiM0v-XVGcdZngfUzY0aiG-as6iKqwoPtQDlLuQG44b7DRJIX8Sor8C6H2UIEpyT7hlEAah-WyfkOHeohGpKS4Xbn8gWfa5KWrhporiJjlQZ7tSaD_gxnLwAtQcZRy-7aGe6bO7X5ex-mqG9wuQlFSYqqgBRyZ4FA5wIdgE7kKtsjTd9H_a1Zo6Xhg39KzWooHMuFPyxkGUgofIbTwre-y8DQhe407tgX2IUCInPEvWnv-S7cvs8YnejUHc_JgwsOZHjTP2oK8lhnFRLKFV9sNwbnmJCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تحطم طائرة في مدينة ميامي بولاية فلوريدا الاميركية.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/89492" target="_blank">📅 21:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCLt7SQnod7n8fxJ7nhpS_pYaHwmekurOXAw9xVdB4Hi88wxN8ApKR8yZyStMQTvuL6HNSgRAxXEbRcKQ7paQBO8_iPc4JbgrrnEsSlGGZacYZ5cP089KSeTXd46T9Iq5Tpp3Du9SLOw6GpOcyZCPCgGPE6382gl_jUvKuuXBWs-7lKQSy0sPGlFbonf3g-hVkQC1DTWzycDTCFqmADSsPDp8hdVBO5ovT5T_YfPZW7FsRLlGy66vHScLhCIVM_XxQV6NgltjBHcejBi_VTDnjobDvQjoruboA1tlNEAmJ6hFpNYy1EMBaBIHmPM7S6XjWn-6fhc8JJZdJJ8y69yXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🌟
ترامب: الرئيس واشنطن يزور الرئيس ترامب.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89491" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89490">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlhDmpMMWY7-H4UWTQ2z_f9yGekZF1lh-Ybfh59ywb2wwR5bAKBefWb5NvejOo-WjOyhcC34BhuuQFicIObLbVVzCRyIGtHIrgL4dcDyHgfzV-Cam_qsKvhl3efWQWaB2OFTSQdV7fnVeo-WnkwXD82pXw1HYD6IwkCwBryiNB7PhvbRVWCyW8Ra9-5aRnyJPYyagL7PsIRlw_wiHN18iu1fWNjHtTFFWuYwvCHKPoUckyzZYG0KlqxJz8F_HPdPrL679fxPr17KZbYDANC_STjxFcEkGoH809hj4qkpZh2ol7ZqDqOMXBI6L4P5Unez1CewK5dOVrhzo4aQv_3QoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🌟
ترامب:
الرئيس واشنطن يزور الرئيس ترامب.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/89490" target="_blank">📅 21:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89489">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQc1b42enEHyc0jIqDyAADtjeV3mj0JWzu7evRX4TXOViNOiiV6AFcl2nXcMLuOWDFMS6Hs-CXXDOnDvBrhDY0jE8RYiqf4kSZ543a-HZS5je7kF87Hxt2YVD_y6XQ9KY1mS07QpumIFVtizUP-3pDeeR5VSNdgKZm_n9Ma-OIu5Qj2eQMj6m92epI-RXSgzc63wevnW2mnM5KHLExt8EQawsN_g1d-Dp08hEG1Mevu8A4PLvVf2bzQXbb6rYtq3FhPXyk_cEBNka0Zy6eKYEpy9qm8IIJN5FoiQKSM04uixuq1IyRr1uEveyo1USJbR3sTgt6aqOQFelrx8TrxQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء عن إصابة الصحفي علي شبيب والمصور في قناة المنار بغارات إسرائيلية وسط مدينة النبطية جنوبي لبنان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89489" target="_blank">📅 20:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9affbbc7.mp4?token=deLp2CoA5S1pC7GlCEUzoY5k__PcxQ_w-ent1vNWWLjw0nf9uOyq7EDQQBbK2GBKTEJP2TErdvhXVQ-9JYEqOKM5rHTGL5BnMMaVulaVE1cmxZqQNko-_WkCfDDHAfuimn3RkzSlVlkYCRam4mHPia66DL-TAeWldlEEB2gUksAQPbhejECVtopp2WeiUML5NT5LLbU92zvArU1HBX7xOaQTY6subHv0EeSftGK_RMSbewMnLRMv6r_zumO5oQPK0uP66ESa1m7Q6UnRPuzfIPbrtGPdnvYyuujaSc_2XSsAhYWZdNn7--iDhiug2l5y1VGX8ML70qaSjudvtCdOzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9affbbc7.mp4?token=deLp2CoA5S1pC7GlCEUzoY5k__PcxQ_w-ent1vNWWLjw0nf9uOyq7EDQQBbK2GBKTEJP2TErdvhXVQ-9JYEqOKM5rHTGL5BnMMaVulaVE1cmxZqQNko-_WkCfDDHAfuimn3RkzSlVlkYCRam4mHPia66DL-TAeWldlEEB2gUksAQPbhejECVtopp2WeiUML5NT5LLbU92zvArU1HBX7xOaQTY6subHv0EeSftGK_RMSbewMnLRMv6r_zumO5oQPK0uP66ESa1m7Q6UnRPuzfIPbrtGPdnvYyuujaSc_2XSsAhYWZdNn7--iDhiug2l5y1VGX8ML70qaSjudvtCdOzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية Sentinel-2L تظهر منطقة محروقة جديدة حول خزان لتخزين النفط الخام داخل مصفاة ينبع التابعة لشركة أرامكو السعودية، وهي مركز تصدير رئيسي للنفط على البحر الأحمر.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89488" target="_blank">📅 20:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2yvHQe2ucXP5vW6SVKnK0kleGa-dnU5aCYYv4iK3i1Vv5txy0LqKLopUZdByfDhExj1Ta_G3bhiyl1dK9fFs0-_DkC22cVj6cYuswVaZWHguPgEhYe9-JqafVHqbMeciDJHLkV56kXDsVDpfHeld9L374wcxYKj9pjX5Dll7QDs34oirQJ2HibeGjfjyoMGIWCI51rGiw6QJBLJXgNkanf5L1Hb42UEvcKeIF15b5JG52y7zGioSg8WKB-8LP4jtxIYEYlVK1NRB0NPVOO4oAn6zK_v4VwIzcxc7t8_Bq6lNLT-o-1IkNTSzFN7aT5KzhdQlUwGS7lzFTRD32ZsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مصدر لنايا:
العثور على مقبرة جماعية في مدينة الرمادي مركز محافظة الانبار غربي العراق عن طريق الصدفة خلال اعمال بناء تضم رفات عشرات الشهداء من منتسبي الحشد الشعبي والجيش العراقي.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89487" target="_blank">📅 19:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قراصنة تابعين لمرتزقة السعودية يسيطرون على ناقلة النفط "نيريدا" (NEREIDA) التي ترفع علم ‌جزر القمر⁩ بعد مغادرتها ميناء رأس عيسى</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/89486" target="_blank">📅 19:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اوربا تنهار ببطىء
‏يتصدر حزب البديل من أجل ألمانيا اليميني النتائج الأولية في انتخابات ولاية ساكسونيا-أنهالت ؛ الحزب يعتبر نازي وعنصري متطرف ويرفض الحرب ضد روسيا وحرب امريكا في ايران</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89485" target="_blank">📅 19:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇷🇺
🇺🇦
نيويورك تايمز:
نظام المشتريات العسكرية الأوكراني عانى من عمليات احتيال وهدر وسوء إدارة جسيمة خلال الحرب. وتُظهر عمليات تدقيق سرية أن حوالي 1.2 مليار دولار قد ضاعت في عام 2024 وحده نتيجةً للمدفوعات الزائدة، وفشل العقود، وضعف الرقابة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89484" target="_blank">📅 19:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">القوات المسلحة اليمنية تعلن إسقاط طائرة استطلاع مسلح نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية صباح اليوم في أجواء شمالي غرب مقبنة بمحافظة تعز</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89483" target="_blank">📅 18:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXbDTfESoapN9ELVZJmN_Sob5OvJUPobP_MMMCuryvzyLEVJY_dkIy34W5K7waiwKYxZsCg9pQOZlkPwQg9BYl-OEj7upV78vDGYX_scOU9yW67Fb9HQ4zG9DOs9zpz4YiiYHnAFX2dqHB6bak5jzx3-HzJ7KHidH_OGV5B-sGoMAKubyhpdjbPWxzmf-f2JQ1ymfzuI1IFrZDWthNxX8FH4rtkSZWO4bx1TGt0u5clphtq_eCryG30LRUsDWtcRInZNPLnRboXHqU7VuMA481wDfk6Sx1BxRl5r7IOEx3wvicpCcKXla4S_-bU-HOmDjfGKqTFem7UaXfpdo_xr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف ساخرا:
استعدوا للإقلاع. الاستعدادات قبل الانطلاق:
ارتفاع أسعار الديزل إلى أعلى مستوى لها: بيعها على المكشوف
أكبر دائنيك يتخلى عنك: حظاً موفقاً مع تدخل ين++
النرويج تخفض 80 مليار دولار: فلنغير اسم النرويج إلى أمريكاواي
انخفاض التوظيف: نسبة الدين إلى الخدمة مع الحرب الإسرائيلية، حسب توجيهات من يحركونك
أوه. مخطط النقاط الخاص بالاحتياطي الفيدرالي يومض باللون الأحمر
😁</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89482" target="_blank">📅 18:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📰
رويترز:
تعتزم الولايات المتحدة سحب أنظمة الدفاع الجوي من كردستان العراق بحلول نهاية سبتمبر، وقد تنقلها إلى الأردن والمملكة المتحدة وقبرص.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89481" target="_blank">📅 18:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
البنتاغون يرفض صرف تعويضات للجنود الذين لقوا حتفهم في الصراع مع ايران ويزعم انها عملية وليس حرب لأن الكونغرس لم يعلن الحرب رسميًا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89480" target="_blank">📅 18:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNbraj5zcCQpCAzkaDY9zdCzDsEDJwLZe51vAn6EiwN-eBPEP2VhUAQ_lo7lPEoavkFdDYACEJ7ICv6sahyCkK92j3ue0CS9uTBxAcO2LQbzkn3K4pTqniQfdWzy3jjV0ZAvI0yB54aASNKoG3odTEbeichmzyKtX3bNEKjlVpfQeqLgByFfiSUrhKcoZlgnTjMTRasq1FNkujoQKdEA9EXGF5TMykXLOdS5Vf_KGR-9N0ZAWqh7GSQvaBUPCflDOVDzqWwVUt-L-C17tinNU4FrIZOmc1Id-xx93fY00xjf47oasgPAY18u9IoOywbeHU19N6FY2m15LSG21o2byQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
حريق مجهول يندلع في محطة رأس لفان القطرية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89479" target="_blank">📅 17:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">#متداول
🇮🇶
بعد فضيحة تسريب أسئلة الرياضيات من وزارة التربية العراقية التي تعاقب على إدارتها وزراء من حزب تقدم.. تصاعد موجة الغضب الشعبي بين الطلبة وذويهم وسط مطالبات باتخاذ إجراءات حازمة وسريعة وفتح تحقيق شامل لكشف المتورطين ومحاسبتهم بما يضمن العدالة ويحفظ نزاهة الامتحانات وحقوق الطلبة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89478" target="_blank">📅 17:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89476">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AILktC5DJ9DYyUifPgjNfydJoeW09NyDyUQ_eIPK4LRNjuGIRFJc2motz_lMUrgZmyjhIZtbfWDUzsqEYCdebhQziSk2fuDEkS2qppN0VNPvHSxDRRya2sFPvero7sHb0Py6UGINQXQYfw_8PvNKPIo9Kok2M4QqKOS2ivj_cgmwEwFIETrWsq8qJqD_mesxbQO2tHOIXlEEycagDXLySL9CqiVeoAFfRz_5-gO1nBlUjQEB0eB8H-ctFwxV4y2jlp6FJAU04QnNSIJeCPDP7zWZ1xeomoZ_tk4MKz91EaHwrSMGAtKlHzb9emeDOi6AjEiQwiqQlMbwbkA1T_g5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nR_5eR9VkfsxwVBe9QS-uEzP6MNscDzZXlxcJ9CPHqhEpIUaIPakpnPgfPwxy5c2xLkxPspibIr3fyyG90qPIQqoaVC2LBXo08p2SdWnDg2bouT2SMkYj82ZHRqkPIP91XdTkvZTwwjLGNF1fGfJf0x0Bzlw109B0Yb529Lz3ae3BNrMsc8jIJufEnbnjrXCL9rGpVLjBLSVltryPWTuatAW5P-jXGWrzhhbPMd1L-fBymzHaDtk2ri0ggiqRxzmV6alXQSaR4jNSS3-7vnrXGeMZB-54-CTTwoLECXKkdAwEapFnlEvDPq9tHtB9fy_-JWO9hzX7_2QnWiqsOArUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
محافظة بابل وعدد من المحافظات العراقية تبدأ مراسم تشييع عدد من شهداء الفتوى المباركة بعد مرور 12 عاماً على استشهادهم إثر العثور على رفاتهم قبل أيام في محافظة الأنبار.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89476" target="_blank">📅 17:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89475">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">العدو السعودي يستهدف بقذائف المدفعية مديرية شدا الحدودية في اليمن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89475" target="_blank">📅 17:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89474">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ضربة صاروخية دقيقة استهدفت اجتماع عدد من قيادات التحشيدات السعودية بصاروخ باليستي محلي الصنع.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89474" target="_blank">📅 16:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89469">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">محافظ البنك المركزي العراقي:
لا عقوبات من جهات دولية على القطاع المصرفي بعد اليوم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/89469" target="_blank">📅 15:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89468">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGBqzIxaQGZ-vF6OHYDZEMnVOLPIM6VcFk6XnSHB3NpcY3RH_Ghh8pwNedazYAA6KS_EY_TI-nTw3r05rI3WYAnhy7xcFMQTImyxF2NcckLKvxiuwnqRsjVEcOqgIFNcAgjO0Df8nvR970r1DhzPRpzxwM4feqFiWFkCNBkh9qC2dwT6WXfdJOWBOAR7c1l3qC40bLKJMmgyYGyNgoII1nnjaRWvxV8QnFeqps3mXATIytq_ci-FSgrNo9vYvSy-7sXi2K_nfQKj0wjWxQk0LhYM6gwowGyJL4yyKTPRauDM0KtqOaVRQNTSedNF65leQfqXx2-PrEfHtiT-EPCjjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج ابو الاء الولائي مغردا حول تنظيم السلاح: ‏تنظيم السلاح مقابل السيادة الكاملة والشاملة</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89468" target="_blank">📅 15:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89467">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اندلاع حريق في منزل وزير التربية العراقي بمنطقة السيدية غرب بغداد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89467" target="_blank">📅 15:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89466">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cdpms-DbPlVnCqYE_-gOHfLA-dnOiRIEUG3-ssudHp7aKQ7zIqQNNErJgYnoB95mJcigwn9z8Kyz5k40bvGbtXrGQtvMOo5ykzSXdcPTtB_m3Zl7bcnZnoSg1tACGTTvUjU7HdSaFkN03vrhji66ZGL1LxVSlqQDWcyGDoKGqqOjk-UWNbr9B32Ulz-Q1gNtgy-Pnm_0XRk-kdrg2yVS0jJpK82qku2Hd9PhiJ5-jbxypt_e4MO129yIDMEHlWMWksjGiY1AEknOLJOdg76DCMQHH3_DOS5B0S6vtLFq9wytV5G12QeLiyLtXcDq0R753ppFW538l0Hu-RuSi5eNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
🇮🇶
هل اصبح معرض بغداد الدولي اداة لترويج كتب تنظيم القاعدة الارهابي ؟
جانب من كتب هادي العبد الله عضو مؤسسة سحاب الإعلامية التابعة للقاعدة وكتب الجولاني وكتب ثورة سوريا التي تضم الإيغور والشيشان وتنظيم النصرة تباع في قلب معرض بغداد الدولي للكتاب !!!
المطرب سيف نبيل تم منعه من دخول سوريا بسبب مقطع مادح الحشد !</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89466" target="_blank">📅 15:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89465">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f73977c8d.mp4?token=mppvYMCmYNzqXLQoG7fnGUroP3_wUEQB2WpqjbvVdOoTRwG9Y8vM-lNLCMZJsEfZ5keI9imjK2q6P8s_CS8ibg3GhcXrTqWfS0M86oa2oypcikS6Qcsh_FJlOOcC4MAsMvoWAJ6dQl6K-zOrkhXx-REQqWWU49FvqXmYHN4R2-GPga8KbNvnkchSjN9A9-fgpZVe2X0IZ0JlrSqAZrSf5yExESfJIXXf7VYdDHzXCHG8D70Aw-EiauUxKDScyfH0JYQmmWZER5M4tRbdzmch0J5lrhhrJ5hB3BodF3RS2y8CDxlIZAmIfebz2vytBP9du6K9WqWoSEIJnsIwRFL1fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f73977c8d.mp4?token=mppvYMCmYNzqXLQoG7fnGUroP3_wUEQB2WpqjbvVdOoTRwG9Y8vM-lNLCMZJsEfZ5keI9imjK2q6P8s_CS8ibg3GhcXrTqWfS0M86oa2oypcikS6Qcsh_FJlOOcC4MAsMvoWAJ6dQl6K-zOrkhXx-REQqWWU49FvqXmYHN4R2-GPga8KbNvnkchSjN9A9-fgpZVe2X0IZ0JlrSqAZrSf5yExESfJIXXf7VYdDHzXCHG8D70Aw-EiauUxKDScyfH0JYQmmWZER5M4tRbdzmch0J5lrhhrJ5hB3BodF3RS2y8CDxlIZAmIfebz2vytBP9du6K9WqWoSEIJnsIwRFL1fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
وصل كل من المبعوثين الأمريكيين جاريد كوشنر وستيف ويتكوف إلى كييف.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89465" target="_blank">📅 14:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89464">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
ترقبوا مشهدا لعملية نوعية استهدفت اجتماعا لعدد من قيادات التحشيدات السعودية عند الرابعة عصرا اليوم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89464" target="_blank">📅 14:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89463">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698ebc0493.mp4?token=COyo4mQtLCIQlhzfm7ja_2yAXzxjcDi0G3zWVxnKlHQxdcfSYng7jBivYPEdh2ER36Q6oB0LVfhmJoorhtDaEOU4ssTIeWPB28JNqg0eKb0Ep6cndhp18kjEI_R3L4nmVhXh8lv9Aiu-aGoH6HSm0NgBOrhY9SjaBAxyQz2CVeuMtxRreWi66WgL94DXs8hNWZR8y-4fpmFQRScxTC3iAnCDu-J4CJf5-cEI695LSNpQ6PuF0k9PbXD6Hzq4MJyrcRgp8NfZc387eLAEap5degYYAgCZOp2p1DplzbaNSyVQo47ot8q710v53uKYl6Zq1S8hG5Xa033Fp6Vmm4rQZpkFl8pXu_U7F9yTDTQ2O6hixILfNTjcCXRWnjAmqhYZtbsbt744KIwWiop7osABByfuUhIvtRxGhlAt4VGymPK5xjVWjYztrB-BXWdCAXCJH-6cRljZmWErs8FcaXUGx6D-blphEoihbL9DfdwJS9bUzIm91t87Whar4_VUQVIjg0v8tD6ldvFw1xyYpI6hUutX2HfZxCPQQnC-KupdHFHrJ2eqhXFVFgkb2J_n7w_sp7MznNkp-Ykja3cnTQnBw-t1qnLLsCVELu61ihzyri2Zbkrs-_BLWyT7ZX2iTTN1jDiSfrTqCm-XzH1v8vJx1aul93Cfn1vg1WR3GwjSYJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698ebc0493.mp4?token=COyo4mQtLCIQlhzfm7ja_2yAXzxjcDi0G3zWVxnKlHQxdcfSYng7jBivYPEdh2ER36Q6oB0LVfhmJoorhtDaEOU4ssTIeWPB28JNqg0eKb0Ep6cndhp18kjEI_R3L4nmVhXh8lv9Aiu-aGoH6HSm0NgBOrhY9SjaBAxyQz2CVeuMtxRreWi66WgL94DXs8hNWZR8y-4fpmFQRScxTC3iAnCDu-J4CJf5-cEI695LSNpQ6PuF0k9PbXD6Hzq4MJyrcRgp8NfZc387eLAEap5degYYAgCZOp2p1DplzbaNSyVQo47ot8q710v53uKYl6Zq1S8hG5Xa033Fp6Vmm4rQZpkFl8pXu_U7F9yTDTQ2O6hixILfNTjcCXRWnjAmqhYZtbsbt744KIwWiop7osABByfuUhIvtRxGhlAt4VGymPK5xjVWjYztrB-BXWdCAXCJH-6cRljZmWErs8FcaXUGx6D-blphEoihbL9DfdwJS9bUzIm91t87Whar4_VUQVIjg0v8tD6ldvFw1xyYpI6hUutX2HfZxCPQQnC-KupdHFHrJ2eqhXFVFgkb2J_n7w_sp7MznNkp-Ykja3cnTQnBw-t1qnLLsCVELu61ihzyri2Zbkrs-_BLWyT7ZX2iTTN1jDiSfrTqCm-XzH1v8vJx1aul93Cfn1vg1WR3GwjSYJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
مشاهد مرئية لتوغل قوات الاحتلال الإسرائيلي في محافظة درعا السورية ونصب نقطة عسكرية في اماكن تواجدهم.
عوي ولاك</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89463" target="_blank">📅 13:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89462">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo704SGwayqh53QVYvUxbn1YE5v_tCLdZRu_TaQZi5MDeGVAsaZNi2BXb96_v07NEukVdxi_MNpnvTLRQ9Ku18LTLf4t3ff9wSlSBHSUMwV1VCcaYZund7VKJl-KV0CRCYfUA_KyHuEQWl2Diky_XWVM4juo3ME9u0lwkSyIEI3wnu2SyGevHqC4C4OOkurm73HZ87KAo3vKOZBU5gkXRyMHC42NxnrbmymuvGcaFBfs6Q6mb0Y-Pur1ZRTYudYCwCtLteMDLpjvru83n8-MNRJW7ulVS90Tl12eUkc0kr0L1FSpY_f33bhZPi-WxoUC-MfoZK3Qhu61AndWFncUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇷🇺
وصول مبعوثي ترمب كوشنر وويتكوف إلى موسكو.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89462" target="_blank">📅 13:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89461">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
نييورك تايمز:
‏بلغ متوسط ​​تدفقات النفط عبر مضيق هرمز 6.7 مليون برميل يومياً في الأيام السبعة المنتهية يوم الخميس، أي أقل بنسبة 60% تقريباً من مستويات ما قبل الحرب</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/89461" target="_blank">📅 13:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDrA9i80a2S1Yks7jKodEh93e3VRI6VzmGiYRuw2j-ooDm-ogK3T9OY3VlXW3bmlSGSOuR0yHntt_fv7fLvXTRpicM_pU8JdKhpfVclkzauqS31y1XZjBw1YThRWQ_jUpVo3MJntsS1HmabQ_XVC02e_tdDnjWg3FqZkD0kLtu9cYhgzNhNaOMXvrjdl5er1Gh8WjlwKKA7HWUhp73t2aLZBK289WllymFr6nUZRxPDiNBN4OrxsijaRLVGJBsKsHyXguobJLD9mwq1Ms1WP8nF6hgEsDe4Eo5JQX6axWS6oreT2Eu5-wHeMoWk2gC44sRdaqAddryuNNqVu7mU6QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-8_YQIYEWuewF-xU6gMerO6f-TgfbF67uZBnvYGfoIirGbU27WYtVwGD7RQnx5HGh52eBrFpvFB64DMajn04KJC7l14uZinhxzPCkQnBXWEaHCxnJaWO9TaVGUwBkn7_-6h_WpECSo2ZNSUWu6_H84MNwL-daK3EHfSq6m8T_ArbqLsFnPS_M1RVvdJBPmrVMVabzsnfczVi17J2OaznAI1P1z-qI4JoMSUp8TPgrH2-_Z6-Yq81pxeh3SeLu3l6fxHtbOlwUwuVFCqHABG9YUP03Pmitopc0MsFpW5QA4XbmTBnMHW8DONBC843AWl1F6mwCp4QWvb-sby1MQWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ViWKAiP-SQvCYxez8CGKMhPjtXDQSwJfL-3UYzQdcmMuXiWqvH8qNy0CXWybW1eRvjEkVi2Z2PS0bC8UIUd31huGfqNxJirCD1eYZfOTb2waG9PYau4PrAyIozcLkgS-Wp1P7J5EGS5CD4GZigljwaVnKL8lCaVicriMrgOa-WUqTiC8IMR_oHch-g9j73ciGX2QkiKmPkXMuYzOIQfb4rkEjcLlGQsdaRZStnSZQaMplFsAe_ihHYdl31hkWYd-E_1ANFqD60zsYLuCsf-w5d4odFwRynIRjKhTctrb1IwJivWb28L2HHsYXhdre9tqxuGV9aq6vHuU-K9pPJxkxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
في تصرف شديد العنصرية ويهدد السلم المجتمعي
🇮🇶
بدأت بلدية محافظة أربيل بإزالة لوحات المحال التجارية المكتوبة بالعربية وإلزام أصحابها بإضافة اللغة الكوردية إلى اللوحات بدلا من اللغة العربية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89458" target="_blank">📅 13:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
شاب من الجنسية الكينية يحتج برفقة مجموعة من المهاجرين الأجانب أمام أحد المصارف الأهلية في العاصمة العراقية بغداد احتجاجاً على عدم السماح له بسحب أمواله المودعة لدى المصرف وإرسالها إلى والدته المريضة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89457" target="_blank">📅 12:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c96b93cf3.mp4?token=KOhuxUegCV66Zhk9gMAHHHA-VAy92-K4ELTfkPjPP_aCtNhuFAAcf3zTwA25xhPcpch0oGenDGG1su4gEOs2EVG95Sbw9Jmelw4aT9lnqhobGotFptrl03ddbdmlfsn-mPGn0DInREvDUhHsYIgXQLcFtD6_flJ8knRUmP1vgJE1km8LZ49ntW8FHbzzkhom8lalMDM6WUFX3_oR2jNMM_ijXuktP2TWOnPp48HAmSQtjZR88KBX8LyyiTAyMxcsX6UBdlpzD2-BdSexb9OGYqZ2fbaNj6V84RP8t2jM9zYJG5xyIctZeIvcYAUQa37IHJyiWQiVJxKBscKwSmVbbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c96b93cf3.mp4?token=KOhuxUegCV66Zhk9gMAHHHA-VAy92-K4ELTfkPjPP_aCtNhuFAAcf3zTwA25xhPcpch0oGenDGG1su4gEOs2EVG95Sbw9Jmelw4aT9lnqhobGotFptrl03ddbdmlfsn-mPGn0DInREvDUhHsYIgXQLcFtD6_flJ8knRUmP1vgJE1km8LZ49ntW8FHbzzkhom8lalMDM6WUFX3_oR2jNMM_ijXuktP2TWOnPp48HAmSQtjZR88KBX8LyyiTAyMxcsX6UBdlpzD2-BdSexb9OGYqZ2fbaNj6V84RP8t2jM9zYJG5xyIctZeIvcYAUQa37IHJyiWQiVJxKBscKwSmVbbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف
: الضربات القوية التي وجهتها القوات العسكرية الإيرانية إلى القواعد الأمريكية وضعت قادة هذا البلد في وضع يائس.
رئيس البرلمان في كلمته قبل بداية جلسة علنية للبرلمان:
لقد انتهى عصر الردود المتناسبة.
كما أننا هزمنا الولايات المتحدة في المجال العسكري والدبلوماسي، وبجهود شاملة من جميع أركان الدولة وصمود لا مثيل له من قبل الشعب، سنهزم الولايات المتحدة أيضًا في الحرب الاقتصادية.
توصية القائد الأعلى للثورة بالتحلي بحذر شديد وتجنب إظهار الضعف عن أنفسنا وعن النظام هي تعليمات استراتيجية.
الأمريكيون بالتأكيد أدركوا أن عصر "الردود المتكافئة" قد انتهى.
أي انتهاك للمصالح والأمن الإيراني سيقابل برد "أسرع وأثقل وأكثر إيلامًا".
﻿</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/89456" target="_blank">📅 12:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89455">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
اندلاع حريق داخل مستشفى ابن الهيثم وسط العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89455" target="_blank">📅 09:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89454">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoOhmM4e_YIsAzPCs-3EkPrQHJlWDznfy2B8AlaSLyMu1ZgTvn_jqsfQobB5gwdnuZqK_SKjILTKKvpKzgxbgejYlyNcpRxvuhOEokFjqCx0Nv81LoMxbpk4ez8WmCNY3hpMHNbcd7Hy8L5-KFW54uZpdmcgQY3IssqG8y28rGaT8B1HBMRpP2m49H9GYWBl9r3wWdt0JKO6lIL5H_FmU3MMRgIxwZosotf2s52cZzmS-8gqJlxvFfDAiQyezG2_dhjx_rjXAo4SSeKYDKhNfrCfplB8QbaKb_Otdgm160uzNZilSlgzEY1wQ_CfjQZUjYp81pLp8Bzsob1pEqV7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد اعتقال عدنان الجميلي وحسين طالب، وكيل وزير النفط ومدير التجهيزات النفطية في وزارة النفط العراقية،
لا تزال أزمة تجهيز الوقود تلقي بظلالها على المواطن العراقي، وسط أزمات متكررة ومتفاوتة في توفير المشتقات النفطية.
ولليوم الخامس على التوالي، تشهد أغلب محطات التزود بالوقود ازدحامات طويلة، دفعت المواطنين إلى الانتظار بمعدلات تتراوح بين 20 و50 دقيقة للحصول على الوقود.
وفي الوقت الذي يثمّن فيه المواطن الحملات الرامية إلى مكافحة الفساد،
ما الفائدة التي يلمسها المواطن على مستوى الخدمات؟
المواطن لا يريد فقط محاسبة الفاسدين، بل يريد أن يرى أثر الإصلاح في حياته اليومية؛ وقودًا متوفرًا، ومحطات بلا طوابير، وخدمات توازي ثروة بلدٍ نفطي بحجم العراق.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/89454" target="_blank">📅 09:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89453">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFJgJmbDbPRq_q8cLezErxzV5LGbI7h0pWMA22rkMxaQJbLRRZt3JDeUlANiWN3EKrsNp9ZRCZaJSJEWCfk_-UZNUTZkGQpPa8xJN17Z4uK3JxjBOj89wYS4hp7-8QAEGCThcF9vmwakzwgwpkKYHM-L046LQbR5BF9rbEQaZFd1uZK_a3xwfy0wgHw2sKxbRIllAaZPP1pnftxisYutaBZ_m3e5ag_hr9Yxi4bsAS75yREX3mqL4FZI3apb3ti1E_CgBAvyO-tuy0tf2S0HmLEpv_CQ4Gi1gDv6FFgjR_LdSZeohxaG6yBZK4LRB2JG48Gw__bewTCEMTv6_SFx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89453" target="_blank">📅 08:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89452">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
لأسباب مجهولة..
خروج عدد من محطات التحويل الرئيسية للكهرباء في الكويت عن الخدمة، وقد أدى ذلك إلى انقطاع التيار الكهربائي عن عدد من المناطق في محافظتي حولي ومبارك الكبير.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89452" target="_blank">📅 07:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89451">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الصهيوني:
مسلحون من حزب الله أطلقوا طائرتين مسيرتين مفخختين باتجاه قواتنا في المنطقة الحدودية؛ الجيش الإسرائيلي يرد الآن.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89451" target="_blank">📅 06:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89450">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8OvKQvLQGckf-F5IuuWzuMYGbK2ABtPr-mzXV6yoMJmIqcm3unD8HHu5rX0-J7aWr-IVit7fJ4iz7_umC0WKT4q5CVpQ7BB2M4VLCa40JlUEx8sT7R11knmwHr0ckDKsxtigk5MzJNx6x5_BtDJ5Ik2SmZ5eD28g-rjTblCS2eZilY9OsfAjdZ5Z3DhWrgstyeiGyWQ8drdCUqvFz2kv98opKKJFnam8o8abhpF1VVcEgktlsTRLw0uo_7BIf_fynYuHpw6C_YOKdTg2RgWwZG7UW1y2xJWJ_BFWMJcf7NO1o1QBdUbQCFNPk2DSgtgBBqxXjNA8DIEejp4Zp03Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
جيش الإحتلال الصهيوني يصدر إنذار عاجل بالإخلاء لسكان بلدة عربصاليم في جنوب لبنان.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89450" target="_blank">📅 06:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89449">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGtOBlLRlit4QbFEzaXQOsx6jkiwcMcXDdliCDUxcZNL-46AP8isP57WDQlKPZVan0NlcJthh0PkI7mE7R8t9WDbYUl1hMtBTSxGNI6Rge6hCMnr6od4bf0OsFuptTfujCdJE829ghXD5loD4aLjZWAJoI8YlPmsQNo4J0VL0uS8SYvMwfUGNJzXKCQW_u-vBVacx2Y5rGqx_k77--rAyYgyYu12UzXqwKNiBMgsczAOK6765HjvZDjsStE6T6PrtaJ045U6Cx6a3nNsuS1oM00WSyvfDZFdFmx9f2Rm0e5BSWsMYHxpu8u07PkAeNR9TlpXPzdu-tUTlFMFhiqOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
غارات صهيونية تستهدف محيط النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/89449" target="_blank">📅 06:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89448">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
الحرس الثوري:
قامت القوة البحرية البطلة لحرس الثورة الإسلامية باستهداف زورق (مركبة مُدارة عن بعد) تابع للجيش الإرهابي الأمريكي، كان يهدف إلى دخول المنطقة المحمية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89448" target="_blank">📅 05:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89447">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇾🇪
🇸🇦
قصف صاروخي عنيف للقوات اليمنية تطال مواقع مرتزقة السعودية في محافظة تعز.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89447" target="_blank">📅 04:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89446">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb10a23f4.mp4?token=mH5hpGW9uiZUBJOK_MhKcjT6yX70XmPYoNFDSzzZkmikErh8DgxVpeG9CJJ5Zd2BKD6D2u9UEzYs9qMRKsMGZVSxoX0yWn29lg3K-hk6Zb82QcL0xEhm0uGeeI4rOh92FYNy-8iPYk7d-qN9y7pYW7puVVgSf2E3WdaveQzd46JWCr2jTu34DodJaIsNtzE0bieFZcw-qwzTnspfKNLJ_FqmvCtspWr8PnEjZorQOpPzPnRjmshrXX7iRyQNDUJmo6AqO_PcM-WPBF345rxBXZc4geZDr_TjTyPEz1YsQOj_bwfm21vt4bk3Uc9H-wy53Y8Rzemi9fbXbr9e29xi3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb10a23f4.mp4?token=mH5hpGW9uiZUBJOK_MhKcjT6yX70XmPYoNFDSzzZkmikErh8DgxVpeG9CJJ5Zd2BKD6D2u9UEzYs9qMRKsMGZVSxoX0yWn29lg3K-hk6Zb82QcL0xEhm0uGeeI4rOh92FYNy-8iPYk7d-qN9y7pYW7puVVgSf2E3WdaveQzd46JWCr2jTu34DodJaIsNtzE0bieFZcw-qwzTnspfKNLJ_FqmvCtspWr8PnEjZorQOpPzPnRjmshrXX7iRyQNDUJmo6AqO_PcM-WPBF345rxBXZc4geZDr_TjTyPEz1YsQOj_bwfm21vt4bk3Uc9H-wy53Y8Rzemi9fbXbr9e29xi3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي ينشر مشاهد يزعم أنها لإستهداف وإغراق ناقلة نفط إيرانية في خليج عمان.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/89446" target="_blank">📅 04:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89445">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
الحرس الثوري:
شنّت القوات الجوية التابعة للحرس الثوري الإسلامي هجومًا بصواريخ باليستية متعددة على حاملة طائرات ومدمرة تابعتين للجيش الأمريكي المعتدي، الذي كان يضايق السفن الإيرانية ويشارك في الحصار البحري.
اضطرت هاتان السفينتان الحربيتان إلى مغادرة منطقة النزاع بعد تعرضهما لأضرار وخشية هجوم جديد.
اضطر العدو المعتدي، الذي دأب على إطلاق ادعاءات كاذبة في مرتفعات الجولان لسنوات، إلى الاعتراف رسميًا اليوم بتعرض سفينتين حربيتين تابعتين للبحرية الأمريكية لهجوم.
إن اعتراف القيادة المركزية الأمريكية (CENTCOM) بهذه العملية دليلٌ قاطع على الهزيمة الاستراتيجية للعدو، وبرهانٌ على القوة الهجومية للحرس الثوري الإسلامي.
يدافع الحرس الثوري الإسلامي، إلى جانب القوات المسلحة الأخرى للجمهورية الإسلامية الإيرانية، بحزمٍ وحزمٍ عن الأمة الإسلامية الإيرانية.
إن الحضور المجيد للأمة الإسلامية على الساحة، والقتال الدؤوب للمقاتلين الإسلاميين الأشداء، يحولان دون تحقيق العدو لأهدافه الشريرة.
إذا استمرت الأعمال العدائية والعدوانية، فعلى النظام الأمريكي أن يتوقع ردودًا قوية من القوات المسلحة للجمهورية الإسلامية الإيرانية. نحن أقوى من أي وقت مضى. النصر حليف الأمة الصامدة للجمهورية الإسلامية الإيرانية، والهزيمة والندم مصيرٌ محتوم للمعتدين.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/89445" target="_blank">📅 01:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89444">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
مصدر أمني لنايا:
دخول رتل عسكري أمريكي إلى بغداد قادماً من محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/89444" target="_blank">📅 01:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89443">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
مشاهد مرئية لاستهدافات المباشرة للحرس الثوري للسفن المخالفة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/89443" target="_blank">📅 00:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89442">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f593e4ec53.mp4?token=tw2-GhclionIWqHZLGuId0hkTtNxMpzgd676yvRpaguPnVks5oU-c-XBlRcdPb2BgiciIjPtJWnykQXNR3VwyjupXsivDTwDKffCJh-LAg4t1U7HHL1v6MS3Cb4MSrHUyLPsvHnKve3M5v8FI-uaxuMdrMGi5X33E_ZfViEOa4F6B-niyI_AU7kiQ-jq6MoVcUWtfMI0BvSlQUkGiQy8jC2VSNW9F0eLCFTzpY9oKgMJY0uIUfwEar0XycQnIIyYb7PFYOzEYH1HZKqamIc_eD1x5s_1_44s_3AGJJuNeHKwMT8hhgG15h2lwzCxEsNpRtrfMmcdUVI-kOFUrsz1Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f593e4ec53.mp4?token=tw2-GhclionIWqHZLGuId0hkTtNxMpzgd676yvRpaguPnVks5oU-c-XBlRcdPb2BgiciIjPtJWnykQXNR3VwyjupXsivDTwDKffCJh-LAg4t1U7HHL1v6MS3Cb4MSrHUyLPsvHnKve3M5v8FI-uaxuMdrMGi5X33E_ZfViEOa4F6B-niyI_AU7kiQ-jq6MoVcUWtfMI0BvSlQUkGiQy8jC2VSNW9F0eLCFTzpY9oKgMJY0uIUfwEar0XycQnIIyYb7PFYOzEYH1HZKqamIc_eD1x5s_1_44s_3AGJJuNeHKwMT8hhgG15h2lwzCxEsNpRtrfMmcdUVI-kOFUrsz1Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
‏هل حدث شيء ما في محطة رأس لفان للغاز الطبيعي المسال في قطر؟ تُظهر صور الأقمار الصناعية اليوم ظاهرة غير طبيعية لا تبدو كغيوم. رُصدت طاقة حرارية قدرها 80 ميغاواط صباح اليوم على جهاز VIIRS، كما رصد القمر الصناعي Terra طاقة حرارية قدرها 120 ميغاواط قبل أربع ساعات.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/89442" target="_blank">📅 23:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89441">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLVw5M7fZ8y6bL1kXrPQu6l-exqqIHaFP0ZyanFLVvba7cEhIudoORipjQwvQLiuKwkf-mbtDgnjCn7Ri4iSKFkskr_TBgqpPbPHC2v_IYMryjIKP3mz9gowGKtAtzFtP3NDBcUjrXG-XEZBuWjYTONZ3957CNJpexUJUv39AhgFvdevWdXrJWPYFvXtSH6JQTCn2ks0HSZIDZNWHJoJvsde0YUJ0KW-3Ei1gVgM01pAgBKZR_2qPE7b-uVD_VoSUc-jVsJRn7eapsUGYbfnscmgAf0bt11uDA_l1jQHPMT4DoBHKITIgkxr3Ww05wlFNH4cPgN8oGlIejL5FKBJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🔻
انتحار جندي احتياط إسرائيلي يبلغ من العمر 46 عامًا وله أطفال، أنهى حياته نتيجة لصدمة نفسية من الحرب مع حزب الله .</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/89441" target="_blank">📅 23:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89440">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/89440" target="_blank">📅 23:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89439">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ee9026ad.mp4?token=IO7WtV_N4ivQkWuxS4nhT-5elhODrXhXex9lOGYy4ynNODGm2Gd_EA9lCgqOwtmh9uxCRhNIau5vuJhBmnpAPJTWoc0Kdbjrn_BtALJ3UF3LLSX4h3m86W1n4ZRwqV1xFo-9TERWrkxa5VNbgD3_nCBDsPepySUoxkwn3kQD5ekWGvr_YhlEzyx2sYoE_r_HyPfNScI3jzMsl4ikb9tL5q7_4Ozu8LF-5yxeSB5vlUWun8S8q2EOQU2XqFp_xhVF0SSboDjFYObSH_ut6s6WetK8EktAFxgQogWtxDdPtBIX36N1uKjaDGH48IPAN2eg39mxHIlORZS5OaRzQdcS6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ee9026ad.mp4?token=IO7WtV_N4ivQkWuxS4nhT-5elhODrXhXex9lOGYy4ynNODGm2Gd_EA9lCgqOwtmh9uxCRhNIau5vuJhBmnpAPJTWoc0Kdbjrn_BtALJ3UF3LLSX4h3m86W1n4ZRwqV1xFo-9TERWrkxa5VNbgD3_nCBDsPepySUoxkwn3kQD5ekWGvr_YhlEzyx2sYoE_r_HyPfNScI3jzMsl4ikb9tL5q7_4Ozu8LF-5yxeSB5vlUWun8S8q2EOQU2XqFp_xhVF0SSboDjFYObSH_ut6s6WetK8EktAFxgQogWtxDdPtBIX36N1uKjaDGH48IPAN2eg39mxHIlORZS5OaRzQdcS6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔻
القوات البحرية للحرس الثوري الإسلامي:
تحذير شديد اللهجة من قائد القوات البحرية للحرس الثوري الإيراني: لا تنخدعوا بأمريكا؛ أي تحرك مشبوه سيتم استهدافه.
ردًا على عدوان الجيش الأمريكي الإرهابي الذي هاجم ثلاث ناقلات نفط تابعة للجمهورية الإسلامية الإيرانية
القوات البحرية للحرس الثوري الإسلامي:
أيها الشعب الإيراني البطل المستقيم؛
هذا الصباح، قام الجيش الأمريكي الإرهابي العدواني، في عمل وحشي ويائس لإغلاق مضيق هرمز، بمهاجمة ثلاث ناقلات نفط تابعة للجمهورية الإسلامية الإيرانية، مما أدى إلى إلحاق أضرار بها.
استهدفت البحرية التابعة للحرس الثوري الإيراني، بعون الله وتوفيقه، وبدعمكم ومساندة الشعب البواسل، وامتثالاً لآية القرآن الكريم: "فمن اعتدی علیکم فاعتدوا علیه بمثل ما اعتدی علیکم»"، ثلاث ناقلات نفط في ممر مضيق هرمز غير المصرح به، وثلاث سفن تابعة للولايات المتحدة الأمريكية في مناطق أخرى.
وعقب هذا العمل، تُوجه البحرية التابعة للحرس الثوري الإيراني تحذيراً شديد اللهجة لجميع السفن الموجودة في الخليج الفارسي وبالقرب من مضيق هرمز: لا تنخدعوا بالجيش الأمريكي الإرهابي، وتجنبوا أي تحركات مشبوهة لعبور الممرات المائية غير المصرح بها، وإلا ستكونون هدفاً.
والنصر من عند الله العلي القدير الحكيم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/89439" target="_blank">📅 23:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89438">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9d45912a.mp4?token=BuO6dRtL2Y3vGZG3d3nIIXYYwYg3GFVinuPc4o0yWDbkJdYmRlNJ4SnfIrGkZZHGcl9IrobLjlxhzTDieaBMchpXiZZXZSAl3DK577RAFmekjBK3uLkCyY63ZeR-ieNCnWW5JN0VOj6StfOlewFKI9O2f3YHxM9AaW9Dg0pvc_YQ9tgK3bAz5mQb718VwG9mzPcaJ6zt4tQSoIQSLaOlmn6ENPwaxtlzX9Z7aMnH5csSryHCz6XMTCjoQaevMZ1QHciwTTdSh67JhiWKIle3RsAs32tWU212o8QvFNjTZkzCPNauQEzVtYIUoe0DakvbeaoD35BEM-1pXslvE353IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9d45912a.mp4?token=BuO6dRtL2Y3vGZG3d3nIIXYYwYg3GFVinuPc4o0yWDbkJdYmRlNJ4SnfIrGkZZHGcl9IrobLjlxhzTDieaBMchpXiZZXZSAl3DK577RAFmekjBK3uLkCyY63ZeR-ieNCnWW5JN0VOj6StfOlewFKI9O2f3YHxM9AaW9Dg0pvc_YQ9tgK3bAz5mQb718VwG9mzPcaJ6zt4tQSoIQSLaOlmn6ENPwaxtlzX9Z7aMnH5csSryHCz6XMTCjoQaevMZ1QHciwTTdSh67JhiWKIle3RsAs32tWU212o8QvFNjTZkzCPNauQEzVtYIUoe0DakvbeaoD35BEM-1pXslvE353IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇮🇷
نتنياهو حول إيران:
إذا لم نتخذ إجراءات ضد إيران، لكانت إيران اليوم تمتلك قنابل نووية تهدف إلى تدميرنا.
الآن، سيحاولون مرة أخرى. إنهم يحاولون مرة أخرى، وسيحاولون مرة أخرى إعادة بناء التحالف الذي حطمنا.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/89438" target="_blank">📅 23:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89437">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇱
🇸🇾
جيش العدو الإسرائيلي يطلق قذائف صاروخية باتجاه حدود الجولان المحتل عقب رصد مجموعة من الشبان يُشتبه بمحاولتهم زرع عبوة ناسفة في المنطقة.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/89437" target="_blank">📅 22:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89436">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/89436" target="_blank">📅 21:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89435">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اصابة عدة سفن مخالفة في مضيق هرمز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/89435" target="_blank">📅 20:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89434">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
الانفجارات في جزيرة قشم ناتجة عن اطلاقات صاروخية نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/89434" target="_blank">📅 20:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89433">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
جيش العدو الإسرائيلي يستعد لتقليص قواته في جنوب لبنان.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89433" target="_blank">📅 20:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89432">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
دوي انفجار في جزيرة قشم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89432" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89431">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
دوي انفجار في جزيرة قشم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/89431" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89430">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b07a20cb6.mp4?token=J0R1tPoDFTWC7faoZbWfq5-5Z7YAfns7ym8oX8gz1Q-ZQVC8YSdSBd6atzBlbv0Hk7Rlcuz4OUsZ09HrqJCgY5UbhRqvZHDnv3llGoNIlqp4RfNRfmfgDIUsxsc1aEWL_ghx25G1oVg4A6BQLJHNNbPFAusmXPFSUZef_a-E5dz8UBXQ0UaSzi0JHaRlCgoFp-wZAPvzz3-e2U3UYGOxg0rRyB1N2zGvLIbgxzX4ZorGQx0d8qcJ1hIkft3Wy-TC93tziXhooSZyFudsvf-PovZIaqhOBDWY8Kbu6LsFnqwI4LudwPwpMc84DkzL4sboHJipP9kaLRyNpSYnPgPnSlYhORjZtPUM2Ruca7ZbZ0xbkpQ3UQzCR6ARKiF_HdFQhXbut8r3h2vU0MJv7an-RhEGg6dixLw3ZStYgZVgKlFRwrHZ_iS5JtHbOfOW7okGGQqy2EqPWqEc4P4lkjmvoKAph2Euk9GvqZJ6IUs_-nBcG4YjLQx9ONajKZAfJEoidrm-ZmNn2ax-knwn8Kxn6g1K2VG6Cddmw0a1MVuQ8Gvwuibo89VyXSKeLqiM1CI2oSSN41IeNQYQqAFYw-Tq6zSUYlSs9K0zKh_PNs9D2wLkXPXEsMO-UgYekDjsUGtKTUecyPrdMxptJZkA0oFghpLEW6-p1QHlM2OeseNoIAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b07a20cb6.mp4?token=J0R1tPoDFTWC7faoZbWfq5-5Z7YAfns7ym8oX8gz1Q-ZQVC8YSdSBd6atzBlbv0Hk7Rlcuz4OUsZ09HrqJCgY5UbhRqvZHDnv3llGoNIlqp4RfNRfmfgDIUsxsc1aEWL_ghx25G1oVg4A6BQLJHNNbPFAusmXPFSUZef_a-E5dz8UBXQ0UaSzi0JHaRlCgoFp-wZAPvzz3-e2U3UYGOxg0rRyB1N2zGvLIbgxzX4ZorGQx0d8qcJ1hIkft3Wy-TC93tziXhooSZyFudsvf-PovZIaqhOBDWY8Kbu6LsFnqwI4LudwPwpMc84DkzL4sboHJipP9kaLRyNpSYnPgPnSlYhORjZtPUM2Ruca7ZbZ0xbkpQ3UQzCR6ARKiF_HdFQhXbut8r3h2vU0MJv7an-RhEGg6dixLw3ZStYgZVgKlFRwrHZ_iS5JtHbOfOW7okGGQqy2EqPWqEc4P4lkjmvoKAph2Euk9GvqZJ6IUs_-nBcG4YjLQx9ONajKZAfJEoidrm-ZmNn2ax-knwn8Kxn6g1K2VG6Cddmw0a1MVuQ8Gvwuibo89VyXSKeLqiM1CI2oSSN41IeNQYQqAFYw-Tq6zSUYlSs9K0zKh_PNs9D2wLkXPXEsMO-UgYekDjsUGtKTUecyPrdMxptJZkA0oFghpLEW6-p1QHlM2OeseNoIAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين
: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89430" target="_blank">📅 20:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89429">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
اغلاق قناة NRT المملوكة لعائلة عبد الواحد المعارضة للبرزاني في محافظة دهوك شمالي العراق من قبل مجاميع مسلحة بسبب نشر تقرير عن الوضع المعاشي السيء في دهوك.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89429" target="_blank">📅 20:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89428">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8076d542b.mp4?token=cg1QfNINQNouIZgJo4ceiD3dseeAxX3-hP0AmjKAb_5QHC3bd3ECJa1OHASLOv9tG0WA12JgbGe1CRz3bg2OGvlXhT6OtMiBwSf43KN9oHBJDKu4Xo-KBdZ31UgXrl4kCoCZknNXZuLURcC0IqY8eteuD6Xm-o8M1o1DNyayOBsZDBKz7Qa-a45YOIeIF9ned9hmSif6M95R2QhU6BPzQxWwtXrrj5IwSvQuviU_CDJqF5ZeXX1m27v3dLmEw1su7x35lZFS0Qpscxo4CUdB2p9oEb-jVuJstlnQuOiAZnFfXtQZ6Z3eZeAuxIcJO5mBL9xN-z2aciBB1U-M5Cmg9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8076d542b.mp4?token=cg1QfNINQNouIZgJo4ceiD3dseeAxX3-hP0AmjKAb_5QHC3bd3ECJa1OHASLOv9tG0WA12JgbGe1CRz3bg2OGvlXhT6OtMiBwSf43KN9oHBJDKu4Xo-KBdZ31UgXrl4kCoCZknNXZuLURcC0IqY8eteuD6Xm-o8M1o1DNyayOBsZDBKz7Qa-a45YOIeIF9ned9hmSif6M95R2QhU6BPzQxWwtXrrj5IwSvQuviU_CDJqF5ZeXX1m27v3dLmEw1su7x35lZFS0Qpscxo4CUdB2p9oEb-jVuJstlnQuOiAZnFfXtQZ6Z3eZeAuxIcJO5mBL9xN-z2aciBB1U-M5Cmg9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد آنية من مضيق هرمز تُظهر تكدّس ناقلات النفط بانتظار أوامر الحرس الثوري للسماح لها بالعبور.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/89428" target="_blank">📅 20:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89426">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c1784708.mp4?token=DOeqC3slhjKATFMWtr50RBtDtc4npA2ojItqAB6p1b0Br-mvOwn_QzoFC6pVGsSb3I9v24F-F9Gkl1AnJWSPUjs5jgyugdxS0A856P9MKdaxpdPjZ6isCcWSEHYOj4LOG9G150ztOjI0XpojSteo6XTHhvhh4eI8ZOz87jsVf_NU2KlnDyJ1WBOwXdftKYGtEtdXZxBKe283psSfYrYpxA6Um_rjO08f_WA21Cv7M6C0QrhUyAl9EutPjZ9sadc1qSjCIacy-E5jUyms20E3bexp9GQ3U2Pyl6CfVLF1m1fCYyDSyDlGaE2IrpPmxcM_8fRfAMRAiyoy3O3yf9K_sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c1784708.mp4?token=DOeqC3slhjKATFMWtr50RBtDtc4npA2ojItqAB6p1b0Br-mvOwn_QzoFC6pVGsSb3I9v24F-F9Gkl1AnJWSPUjs5jgyugdxS0A856P9MKdaxpdPjZ6isCcWSEHYOj4LOG9G150ztOjI0XpojSteo6XTHhvhh4eI8ZOz87jsVf_NU2KlnDyJ1WBOwXdftKYGtEtdXZxBKe283psSfYrYpxA6Um_rjO08f_WA21Cv7M6C0QrhUyAl9EutPjZ9sadc1qSjCIacy-E5jUyms20E3bexp9GQ3U2Pyl6CfVLF1m1fCYyDSyDlGaE2IrpPmxcM_8fRfAMRAiyoy3O3yf9K_sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
الاعلام العبري: تقارير أولية عن عملية إطلاق نار في مستوطنة نتانيا.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89426" target="_blank">📅 19:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89425">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
تقارير أولية عن عملية إطلاق نار في مستوطنة نتانيا.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89425" target="_blank">📅 19:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89424">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb25991r1I6xDICnET2Fq7a_vnBwdb7qQsKYnP6_m3jc58vLIFeyhkJVTUKOPSL2_VH4BHAyagz2-D2rJ7wXyc4e6Jh4-sW0EIe9e6zCp-I8mamiC-BINMcVyltRUCrh6rpwAbV48uKWJUOf6zGTzAg4MOwJZcxko31DGS2igg8wakvIvjYMIcWVp38fc9pryUB5I23q4mOFGpL5VopTAEb91OMrrTv-PWgHh73Z7LAfLMO4mmINHevN7h6pfSf45WY5UpPuri1AUC1TQxSi_8I28HvvTaY6VB7xFwEWcxH0ypWFB6P1JJiKhakVkLF8xAWmhRHCiskTRM-7TmekLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات اخرى قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/89424" target="_blank">📅 19:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89423">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارات تستهدف ناقلة شمال الخليج الفارسي قرب السواحل العراقية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89423" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89422">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عدة احداث بحرية في الخليج</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/89422" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89421">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حدث بحري</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/89421" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
