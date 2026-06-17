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
<img src="https://cdn4.telesco.pe/file/KbteY4qQzX364hZpKecS82tCojVcWe9zjkVDtcoN_rC3Kjf9zpdqtfD7e1hssJiT2A6sCfQP3BlC_97u1PJTDq57O7SwDpqfc_BhNx0NfdkqMe1WPsRV7Bmr2clmJ4yDJQtOL18KArR-Pfxvb4Tl7kGWMBeKzk4JPKYz5dQmfLjK6mwOAU6qQlvsOYtcRGm_tCmu0jm4RdGf2aFz96lr4SUAgVuE3UhoOf5q2zDiJAIIaMdODAIhys2CZS51-2kpQDAI8YM1XqBtGHP2xAgemElLvHpVmpxD-ulylKqc9H-aQ4VRArDkP4j59vK7U2uW_Zjwp7yFu8lv51dGbIfJWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 03:51:59</div>
<hr>

<div class="tg-post" id="msg-79077">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هدف نرويجي رابع</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/naya_foriraq/79077" target="_blank">📅 03:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79076">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f554e92f52.mp4?token=V6n-7dHTU4Xp0YykNyLGrBhYo2ypNgAJtHCgyhu8hd-wK2C4REfuKCWDSLHKbNThuv9Kv8S9CRvkxiFlmN25E97Xc1PfaYVai-fWbAHPeZy48XXJpkRuzsJR3tX8pCwN3dD7f0-AINTHmRNH9lpTUOYUJ3o0Tm3JswkpzmZlwx_Puub4JyUBgqbswpXxENIkIVT5ohLdIarNyk7wMK8jEQnZooab27CH77utzdZI1ZTFDMa2-3DOKXpMkb5FXqhEzjWWB2LxCHs66BPZo582wQSr9wNOL4XuNNHc3BKoF6Xn5c7ePgwm9MwTY5Nu36bE-frUE0aW9MgFSbt8kPtKuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f554e92f52.mp4?token=V6n-7dHTU4Xp0YykNyLGrBhYo2ypNgAJtHCgyhu8hd-wK2C4REfuKCWDSLHKbNThuv9Kv8S9CRvkxiFlmN25E97Xc1PfaYVai-fWbAHPeZy48XXJpkRuzsJR3tX8pCwN3dD7f0-AINTHmRNH9lpTUOYUJ3o0Tm3JswkpzmZlwx_Puub4JyUBgqbswpXxENIkIVT5ohLdIarNyk7wMK8jEQnZooab27CH77utzdZI1ZTFDMa2-3DOKXpMkb5FXqhEzjWWB2LxCHs66BPZo582wQSr9wNOL4XuNNHc3BKoF6Xn5c7ePgwm9MwTY5Nu36bE-frUE0aW9MgFSbt8kPtKuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتخبنا الوطني يخسر أمام النرويج 4 - 1 في أولى مبارياته بكأس العالم</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/naya_foriraq/79076" target="_blank">📅 03:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79075">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هدف نرويجي رابع</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/naya_foriraq/79075" target="_blank">📅 03:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79074">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هدف ثالث للمنتخب النرويجي</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/naya_foriraq/79074" target="_blank">📅 03:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79073">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بلومبرغ تنشر مذكرة التفاهم بين طهران وواشنطن:
- طهران وواشنطن وحلفاؤهما يعلنون إنهاء فورياً ونهائياً للحرب على جميع الجبهات
- طهران وواشنطن وحلفاؤهما يتعهدون بعدم شن أي عمل عدائي والامتناع عن التهديد
- طهران وواشنطن تتعهدان بالتوصل إلى اتفاق خلال فترة أقصاها 60 يوماً قابلة للتمديد
- الولايات المتحدة ترفع فور التوقيع على مذكرة التفاهم الحصار البحري على إيران
- الولايات المتحدة تتعهد بسحب قواتها في غضون 30 يوماً من تاريخ الاتفاق النهائي
- إيران تعمل على استئناف حركة السفن خلال 30 يوماً مع مراعاة حاجتها لإزالة العوائق
- واشنطن تتعهد بالتعاون مع شركائها الإقليميين بإعادة تأهيل إيران وتنميتها اقتصادياً
- واشنطن تلتزم بإنهاء العقوبات على إيران وفق جدول زمني يتفق عليه كجزء من الاتفاق
- طهران وواشنطن اتفقتا على بحث مصير المواد المخصبة والقضايا النووية في اتفاق نهائي
- إيران تحافظ على برنامجها النووي الحالي دون فرض واشنطن عقوبات أو تعزز قواتها</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/naya_foriraq/79073" target="_blank">📅 03:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79072">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انطلاق الشوط الثاني وسط ترقب الجماهير لما ستسفر عنه الدقائق القادمة.</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/naya_foriraq/79072" target="_blank">📅 03:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79071">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e89085b7.mp4?token=l5XTyKiVNUp8m1YtiVfClue95YBPTA3_I-QeORiQfmyfLpo9OPIkc7xG3FvXBHLD8-A4c2IGArMU7C7pY3E2ZbNLGJsxPXDrdvYg4_V4HdVEGXVHuGHwUNnFF-jqFi-8pFbQg_W-ts83M_U7UNqNLAWyclXQCBc4w3q_pk46DJZscRmgVYNPL9VThCtJlzOtikD5YrMpjDLhPkyzWQxENbaEngwgeKswaIJQHpgoUVdR40EuAm7DVhG4u_1dRI8oFvnHmeoERwV_V2zRo-6kSBpc-oTb6LU15MKlGtVbuJ5qnp0uiSqx1ITOh9Oh6gJdjbL1z9DwSHecv1xpuyYEAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e89085b7.mp4?token=l5XTyKiVNUp8m1YtiVfClue95YBPTA3_I-QeORiQfmyfLpo9OPIkc7xG3FvXBHLD8-A4c2IGArMU7C7pY3E2ZbNLGJsxPXDrdvYg4_V4HdVEGXVHuGHwUNnFF-jqFi-8pFbQg_W-ts83M_U7UNqNLAWyclXQCBc4w3q_pk46DJZscRmgVYNPL9VThCtJlzOtikD5YrMpjDLhPkyzWQxENbaEngwgeKswaIJQHpgoUVdR40EuAm7DVhG4u_1dRI8oFvnHmeoERwV_V2zRo-6kSBpc-oTb6LU15MKlGtVbuJ5qnp0uiSqx1ITOh9Oh6gJdjbL1z9DwSHecv1xpuyYEAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عزف وقراءة النشيد الوطني العراقي في أجواء مهيبة داخل الملعب، وسط تفاعل كبير من الجماهير العراقية</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/79071" target="_blank">📅 02:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79070">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انتهاء الشوط الأول بتقدم النرويج 2-1 على منتخبنا الوطني الأفضل في كل شيء</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/naya_foriraq/79070" target="_blank">📅 02:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79069">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هدف ثاني للمنتخب النرويجي بذلك تصبح النتيجة 1-2</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/79069" target="_blank">📅 02:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79068">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هدف أول للمنتخب العراقي بذلك تصبح نتيجة 1-1.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79068" target="_blank">📅 02:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79067">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">على غرار فشل منظومة السيرام بالسفارة الأمريكية،الدفاعات العراقية تفشل بصد الهجوم النرويجي،بذلك تصبح النتيجة 1-0.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79067" target="_blank">📅 02:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79066">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">على غرار فشل منظومة السيرام بالسفارة الأمريكية،الدفاعات العراقية تفشل بصد الهجوم النرويجي،بذلك تصبح النتيجة 1-0.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79066" target="_blank">📅 01:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79065">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRSY78a6qJBJhkE2QM1moKXK2JHFuG4B9r9QCwSsEZnxpURHbPbyNPZ-k0tMFVQRyJGNNPeLp4Y25suH_bYtELRumqfbN_eg0Jgf4rerTc5B1VuHhlp5t2g_SOwKjmp6z2kh2JFT9s99OBFJYnnGrDjjtkl-dcomzpol-jlFbiCIBKsKsKhVL9Pf7pSSdy7eUaUajFRE4QNUJ9Qqjh5wqcGREcRAA1iX-AVC-xX2exO9aCRT7OhA-nQ_i7ZD76QyRQDsAW_8w6TszQAXH6pzcSIYNdVMZ-eH8zu4Oi8Lov596lt8UarRmjRbC6ApMGosHf8mAeBHnK-pIe4UqVREJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
عزف وقراءة النشيد الوطني العراقي في أجواء مهيبة داخل الملعب، وسط تفاعل كبير من الجماهير العراقية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79065" target="_blank">📅 01:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79064">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu3NAOq6ijF8rLACUkewCMwv2vN1YhN0OEz-kw2bZqIW1upnXX6qwR8qifAnKHI7u7LrR2BaRGOWRnXRjReCmM-ew-KWIaASLYaYNxSZa1RRW-4TZItSZEwVJ4aQvta9AYe91ZkKpdayeepI2uEDQDubRkC7fU8G_vI3xJpXV1fXUa_lPFL6uHwlqCyP1WsI8PPaO5oVzGUpwADPQG6erwgUmUIBPE17q-SzvcRu1EaRpPZ-ZTqTbv-bKU49DRWNLxbistcRy3EgYNgB2rJL8yi2bSOpD20D7aMwX4E0ZvVFEvf0_dEQoz9_lb8ayCZ26Dch-Ac7H43RJD6kybMD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اسد رافدين حاضر في مباراة منتخبنا الوطني
هو هذا جني مو اسد للعلم</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79064" target="_blank">📅 01:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79063">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2923a06709.mp4?token=o148dlFLlAfCkieLGO-pbHOBl_4eXDH7oYmaihGTJ85wQATWHyqKipBM5IN6smRFVcdmF6swbw8_DuAFB2kO4QuPfUieg8ew6OhyjOLXFwDoCd3ROZcJ2suHnbLk2hzwB57A0C-5br_EYcDbiIa6WSlwylGcYmiVY0PSyRH39LHhkyZgg1Box9MK8Y6d3mNAfa5oWsFQh9noUJ2xEv-DzTdOeqQb32FCqNI-UD56rt96c5g75JSMYYz2erCEDm4Ts_3x8bXJwwgKTZdOtQgk5i8Oq3ski022gqymmzQD9TXA_GXAkdNYWD-LZNeSMkC6ydXzfrpQBavWgD43Rgp8gis2cfoZTQ38NnmlushxLXVstreIz1yySOvOz-9ovDsem0qT6rNs6w7QZLs4Kx76MI3sIQfSGD5qEB3cffi5CoNiRRWixhmiKLDR-h82NqOCoazaJF5YxLfztoMB2SfEzSSaLvJXxYZBHGACStJ8dQx_5AML2-NCOsnas1o3kEMz96u1ktH-1JgBoDTHZMpQ1lAYLQW0TL28Mp0tGBFOYDhYhd0lY2947_WthTAlDdYkAE6wvcr8OMSRmxt2UvIQIiTV7RD1mmyhkEy0_nA-v7xN3Q343V8P5GC1zpRvZJMnckGNtfnrH_SEbv0Z1XVP4ISMugED8-k4DTCDBFdBcEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2923a06709.mp4?token=o148dlFLlAfCkieLGO-pbHOBl_4eXDH7oYmaihGTJ85wQATWHyqKipBM5IN6smRFVcdmF6swbw8_DuAFB2kO4QuPfUieg8ew6OhyjOLXFwDoCd3ROZcJ2suHnbLk2hzwB57A0C-5br_EYcDbiIa6WSlwylGcYmiVY0PSyRH39LHhkyZgg1Box9MK8Y6d3mNAfa5oWsFQh9noUJ2xEv-DzTdOeqQb32FCqNI-UD56rt96c5g75JSMYYz2erCEDm4Ts_3x8bXJwwgKTZdOtQgk5i8Oq3ski022gqymmzQD9TXA_GXAkdNYWD-LZNeSMkC6ydXzfrpQBavWgD43Rgp8gis2cfoZTQ38NnmlushxLXVstreIz1yySOvOz-9ovDsem0qT6rNs6w7QZLs4Kx76MI3sIQfSGD5qEB3cffi5CoNiRRWixhmiKLDR-h82NqOCoazaJF5YxLfztoMB2SfEzSSaLvJXxYZBHGACStJ8dQx_5AML2-NCOsnas1o3kEMz96u1ktH-1JgBoDTHZMpQ1lAYLQW0TL28Mp0tGBFOYDhYhd0lY2947_WthTAlDdYkAE6wvcr8OMSRmxt2UvIQIiTV7RD1mmyhkEy0_nA-v7xN3Q343V8P5GC1zpRvZJMnckGNtfnrH_SEbv0Z1XVP4ISMugED8-k4DTCDBFdBcEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The fight for football has only just begun...
⚽
🔥
Don't miss the next chapter of the story.
👀
🏆
Watch the full Episode 2 now on our YouTube channel:
📹
Football Against Enemy - E02
🆔
@explosivemedia</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/79063" target="_blank">📅 01:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79061">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b8ac1d54.mp4?token=Obzcai9fvx_ddZaHdbw9qc81o94sy5TMTJos4yGd-muOmDzjbrdMi4a5Mo86oJ3TBqb99IkNKNZRIiEannCz7Dj4Yl7czQGwj723I_iQz4014gNVW6fZ7LocqA2gpHtFCWZLZezqoMnRJebajEkpwJelPCfS0qfEia9yU5VbdxjLixVb3vU1M0-glAn52QJnIdDlWwg-zVy17188wywY-vTyTb0jNgmCmvUY-wpf6edN_MaNY6HM3pKyY2bV3HLRrZ4ym8XWEqz8qXPiK3-sQB3fN__hmENTaacgUM9bxT8coxdzPD7hRc-v5IdovPu8RA_L8RgB0UlLfTeOq9Z34bMqUaB9jx8gWyK_oozcO4oo3tQ8HLDxkEvxZ9Nf7iY5p5OQPLVXtDWPozfHbwKzAF-hWypDoCLxbgzTg8wTJnbP9E_I05t7oe77iP7XhDDPgwqgSG8df_2gWAwZJo3SeKqxtKPm34lWBl40Xuo5X0LPspQ5dkbo7Zz4v3HQV637NFlzD2LeukgzRcJCPyauD7urRKiTaKaf0rCnDn9iiBPdRH7tcji-wWQzNp4TjOm4_TIwR8YaiDQPOp7P1nhsxtmhEyyE-dF17RbGa4Nh3Poje_c6-W4iVnuxcQEONY46kpiSs5sSJiouE2O8qWWYCofekD9ZMagUpiOMQOi6n6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b8ac1d54.mp4?token=Obzcai9fvx_ddZaHdbw9qc81o94sy5TMTJos4yGd-muOmDzjbrdMi4a5Mo86oJ3TBqb99IkNKNZRIiEannCz7Dj4Yl7czQGwj723I_iQz4014gNVW6fZ7LocqA2gpHtFCWZLZezqoMnRJebajEkpwJelPCfS0qfEia9yU5VbdxjLixVb3vU1M0-glAn52QJnIdDlWwg-zVy17188wywY-vTyTb0jNgmCmvUY-wpf6edN_MaNY6HM3pKyY2bV3HLRrZ4ym8XWEqz8qXPiK3-sQB3fN__hmENTaacgUM9bxT8coxdzPD7hRc-v5IdovPu8RA_L8RgB0UlLfTeOq9Z34bMqUaB9jx8gWyK_oozcO4oo3tQ8HLDxkEvxZ9Nf7iY5p5OQPLVXtDWPozfHbwKzAF-hWypDoCLxbgzTg8wTJnbP9E_I05t7oe77iP7XhDDPgwqgSG8df_2gWAwZJo3SeKqxtKPm34lWBl40Xuo5X0LPspQ5dkbo7Zz4v3HQV637NFlzD2LeukgzRcJCPyauD7urRKiTaKaf0rCnDn9iiBPdRH7tcji-wWQzNp4TjOm4_TIwR8YaiDQPOp7P1nhsxtmhEyyE-dF17RbGa4Nh3Poje_c6-W4iVnuxcQEONY46kpiSs5sSJiouE2O8qWWYCofekD9ZMagUpiOMQOi6n6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
توافد الجماهير العراقية إلى ملعب بوسطن الذي يحتضن مواجهة منتخبنا الوطني أمام نظيره النرويجي.</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/79061" target="_blank">📅 01:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79060">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a9bf1be7.mp4?token=sWN8gAD_2UokGonGXFPn2hQxsZ8psrOZoWjUY_2gCbJxoKuVeK3_zyccCPyiTPolb3o1EyfSQTfWAfkFxuct5ZtDvZrlZkVRsEkXNDbFlmT-nNxl9afGCdrUx_GXmRf38rPIFrikiAOIE0ats1uiXlVpvTL97_BybruEpK5gKZXsuhqEe3owZbrrm9rEdyNehlzHOLXwaIYHEWwAoc1brU2HhOOZXqRCWnMh17D9eK4WjMXQiSz-rltVJ0tS7drOc7qvv4N4HtcbxvUZ9Y-QYNA3qjsaeOaSha5rOa_BUoS4Cv-a2h8woF_apHiLGG8Uc0SNP9MkSESibiJ0ydAkxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a9bf1be7.mp4?token=sWN8gAD_2UokGonGXFPn2hQxsZ8psrOZoWjUY_2gCbJxoKuVeK3_zyccCPyiTPolb3o1EyfSQTfWAfkFxuct5ZtDvZrlZkVRsEkXNDbFlmT-nNxl9afGCdrUx_GXmRf38rPIFrikiAOIE0ats1uiXlVpvTL97_BybruEpK5gKZXsuhqEe3owZbrrm9rEdyNehlzHOLXwaIYHEWwAoc1brU2HhOOZXqRCWnMh17D9eK4WjMXQiSz-rltVJ0tS7drOc7qvv4N4HtcbxvUZ9Y-QYNA3qjsaeOaSha5rOa_BUoS4Cv-a2h8woF_apHiLGG8Uc0SNP9MkSESibiJ0ydAkxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما ضم روحة يحسين ابنك</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/naya_foriraq/79060" target="_blank">📅 00:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79059">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b1f4a323.mp4?token=G_2bqCGCHr9iFGTwzJmsNDe7MrJqVhULsu9Kt2bX8iUkWSvYz9CmIMt6QbB18TOHOcvNbMueg5QWL00vEi5S2LV4ouPSn1V9N8K6vshGlVlZ72XowaV9iInebnpiFMnL_3KGlVqSNEfYzHVXp6Zu1kLdFaaFbERm4QUMYefTpvwwapZavMJArkYqaHE-OFbYXDmQre3ntw1tVTRjlWmRFRLxDATkVthG71nSVVCj61YhNwj1m5K_UmlGWwkEr-GZdX4Pds9xQXxwCgIArl1-PLGn4es8kbLpthWvH-W6VbmYMeB1Klo80FGp7WE5OtTJ0t0YJPkZXBiDGKLzI71Vbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b1f4a323.mp4?token=G_2bqCGCHr9iFGTwzJmsNDe7MrJqVhULsu9Kt2bX8iUkWSvYz9CmIMt6QbB18TOHOcvNbMueg5QWL00vEi5S2LV4ouPSn1V9N8K6vshGlVlZ72XowaV9iInebnpiFMnL_3KGlVqSNEfYzHVXp6Zu1kLdFaaFbERm4QUMYefTpvwwapZavMJArkYqaHE-OFbYXDmQre3ntw1tVTRjlWmRFRLxDATkVthG71nSVVCj61YhNwj1m5K_UmlGWwkEr-GZdX4Pds9xQXxwCgIArl1-PLGn4es8kbLpthWvH-W6VbmYMeB1Klo80FGp7WE5OtTJ0t0YJPkZXBiDGKLzI71Vbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
توافد الجماهير العراقية إلى ملعب بوسطن الذي يحتضن مواجهة منتخبنا الوطني أمام نظيره النرويجي.</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/79059" target="_blank">📅 00:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79058">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">" اني سائل عنكم "
آخر ما سمعناه منه عام ٢٠٢٢
ونحن ايضا لن ننساك وستتشرف العراق بك</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/79058" target="_blank">📅 00:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79057">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نايا - NAYA
pinned «
السلام على الخامنئي   الخامنئي منا أهل العراق
🇮🇶
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79057" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79056">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">السلام على الخامنئي
الخامنئي منا أهل العراق
🇮🇶</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79056" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79052">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ctmpiKabO8v_c9-HL2mWPUpwj0FcHyc2gZKVPIHMsGXLlOD9m_is_eoSeMet7mXAN6hmO7KcWpASUP1le0CioCpIaAY0H4tr6X8ZaD6FWy6FLGOdWHOuZlLWEy1MtDP71mnvGT-PqI8Z6MZvKd-TtkaXNyuH_2G75U2FnyD0McpFo9qeeg3kooV9pQoDS65YrOUGYNl0LAIlZqWIDOZJvshm8zrvREDPdzkViQ0jFAu2y_48lS32ofogpNCjucvwZdv1giut4xcwltuzY86-VFq1POlRRAzJw2uMt0PMhn83Ww02t86z7hmBv-RSl0ju11YNNvZH7mOx4CdO0sfNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqdWNQTI43rTUFyRc0kbIeSzMdc9xzo3x81IOr_Yk9gMHKJ2w-R10SypN-dbqX-9KB2v0u6ZRdFqGyAzYnd4QKtQm4g_t-WG-_qLqxvhzsvOOMg3BF4vL7itETtYn515Rew1QUiztQ-VQLpL1qVlrteOFiFj4Y_rPN9XXlcXaUR3KMgbhukOj_oVkW5bbAEBOiKQbs6pQibNYPLJ5NZ8JRZtgetBLvpp-0KsLE-K-nVAye-93pkuQ86RkirWgZtqJljcG__lmFsuv924l60S_AqH3u9RlHQsLtDk5ajNc2-_yFOatdvWHKlHLZlcZ1frn5VYdSWJ3Hjqy2TJyKTCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DR4RXvwtXsla6XcyOn6KBce9vlq31Srt4ba0UO30iXBSzTnPnJB1i1nAanqiBEj_PRLtLkaCoaILFR5pnMLWjL8wIQJunjqy13-tcgL20HSIVMkMv1W4oKJvrlmpes7mZ39qg5NOFL8CpIiaTxpMS6tgxxH6dUI57Q3T5Zu9Gp1ogLcBmNS2rvp4bFKwZdsRtGIAezPAnxAfDuhOz0Ki6Aa6m88tyuJlcGY7xaRwsiuLRz1kW7SOBvKCliIpSwHqAW_sK2zjgHK8uw_ahVZb3IUrA_-XmQEOZvrANb0pDcioCkCnYSRrQpOe-swCh70MvVCcn4EwnoRY-bZHcM7kVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyMlbgentO2LkP9FDcHmBAmq8xLLFxQP_4HaA5O3ym2x3XHr40IA6j5MUrSukP4UPFTGdoISLciad41TiFYklqClMJe20ynnlHWHghPyy8GT-boamgIpELHmt3o9ZPpgcI4BUTl_6_z6kO1f2O8gjaV74vdheY_quAeUqexdklItc2vYMCsM5R6ZJKykTKWLwmaaY4hRzk4mj3gio_UMhFeeuHUdQww96vQ6ImA8GMvObW-tqgApfdcPLFoXcaJmIxIcNVxbczeYl0-T1vUIpcCvVviJE8vfY5qzoKYXgthLTYsXzLsBZEn9KQ8O2KGbxMEOdMmqTuy56Gi-m5qdyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
لاعبين منتخبنا الوطني والنرويجي قبيل انطلاق المباراة المرتقبة على ملعب بوسطن.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79052" target="_blank">📅 00:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79051">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
الجماهير العراقية تتوافد إلى ملعب بوسطن لدعم منتخبنا الوطني.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79051" target="_blank">📅 00:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79050">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
تشكيلة منتخبنا الوطني لمواجهة النرويج في كأس العالم.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79050" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79047">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ff81bb17.mp4?token=PhxUzvJgxwYX55KXpe8ZnGunDUPj9d9pxlz5HOrbsgHxCnzGTEftX9X5XqMz3ejywdUm1M8H7IjnSCG3ZZ-tOvALvuBUZfbjSyuhLwtE_wOXy07FGGLJ2lhrXqM5vtDpbeIQLf2FfdQAV0zVONR_NS2iQHJJF0TO1NltVB5V8vwjeWVJyXZ01qSSGtoVPp_mfqDx9Y42MDc-xvwmKjT7b3KEvblgjSAG9VONnA0gauJwofc2_lyu6RdV5lvGpuq43fI_qiMf1ET6--qBAuV-fvWIsJidzpSCdke7kTo9DMJ07EqxEYMnxNpHiSUwCm4qG3lsIfyy9kObJeaMMItL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ff81bb17.mp4?token=PhxUzvJgxwYX55KXpe8ZnGunDUPj9d9pxlz5HOrbsgHxCnzGTEftX9X5XqMz3ejywdUm1M8H7IjnSCG3ZZ-tOvALvuBUZfbjSyuhLwtE_wOXy07FGGLJ2lhrXqM5vtDpbeIQLf2FfdQAV0zVONR_NS2iQHJJF0TO1NltVB5V8vwjeWVJyXZ01qSSGtoVPp_mfqDx9Y42MDc-xvwmKjT7b3KEvblgjSAG9VONnA0gauJwofc2_lyu6RdV5lvGpuq43fI_qiMf1ET6--qBAuV-fvWIsJidzpSCdke7kTo9DMJ07EqxEYMnxNpHiSUwCm4qG3lsIfyy9kObJeaMMItL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجماهير العراقية تواصل مؤازرة منتخبنا الوطني قبيل انطلاق مواجهته المرتقبة أمام نظيره النرويجي، وسط أجواء حماسية ودعم كبير.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79047" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79046">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293589ed4f.mp4?token=tKhNXa3fLpwW8K6R28r49UV-BwYlH1c5jB5EcHK9n4y3uthvCHD5cXNsrITuUoyyaeKdxwtv_EfthR_Ez-LvbKciAVZh9Kp8WdrZJcHmjw5lFlbnyZQGr71FKT8WC2ZyEHfS8cRh4ZroO27pFs2WAq7bevT4apFG0g0bHMuj1DPV_NAoYUNVuZeYuhmy4ypttb3Fp7BwCiuUiQC13Graj8IFfVtl-VGbZYazIzstWV3usJkcXSL7eTHC1elwzgkhfMIk8wutJKLaG-Qn0ALZJzAVOHsD10wWkKFoUOzaKj7HnpzmJLh92VAKVPkoKSSdsXbu5gysXa_1PEmsrCRolw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293589ed4f.mp4?token=tKhNXa3fLpwW8K6R28r49UV-BwYlH1c5jB5EcHK9n4y3uthvCHD5cXNsrITuUoyyaeKdxwtv_EfthR_Ez-LvbKciAVZh9Kp8WdrZJcHmjw5lFlbnyZQGr71FKT8WC2ZyEHfS8cRh4ZroO27pFs2WAq7bevT4apFG0g0bHMuj1DPV_NAoYUNVuZeYuhmy4ypttb3Fp7BwCiuUiQC13Graj8IFfVtl-VGbZYazIzstWV3usJkcXSL7eTHC1elwzgkhfMIk8wutJKLaG-Qn0ALZJzAVOHsD10wWkKFoUOzaKj7HnpzmJLh92VAKVPkoKSSdsXbu5gysXa_1PEmsrCRolw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عناصر تابعة للجولاني تشن هجومًا على مدينة المزة ذات الغالبية العلوية في محافظة دمشق السورية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79046" target="_blank">📅 23:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79045">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac4c8ff20.mp4?token=en_UpW_ZGf5v5e5CrW9vu1NzQL5lZvD6DX8eKSn7vqx0a6b-R8QMykKk7ZcepYNCYiE3pzQDZuMy4GXOhYxblD96klcMXNuDHEhjNen-X2Bf2RI13Eobwkq8zIdh216mg_6eLpJJALcMmo-F5AsoieUCKyMTuQ0F7mMM_LPkKXe7O2m4-qdUjDiBD675AGbcFMMCIvvJCEAHvduK82gA06YzCyCGmV0a9qgt7YWE28pw_w3K7z3wHoIJ3lPaa7vN5Op2k67hLDdBnxt-zgRdJ4KdCHcmDqQwfj7J139gVYCXqTesSttZXAOJHbykzmISZ-kjhoKUjiCeu6Sx3O_tXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac4c8ff20.mp4?token=en_UpW_ZGf5v5e5CrW9vu1NzQL5lZvD6DX8eKSn7vqx0a6b-R8QMykKk7ZcepYNCYiE3pzQDZuMy4GXOhYxblD96klcMXNuDHEhjNen-X2Bf2RI13Eobwkq8zIdh216mg_6eLpJJALcMmo-F5AsoieUCKyMTuQ0F7mMM_LPkKXe7O2m4-qdUjDiBD675AGbcFMMCIvvJCEAHvduK82gA06YzCyCGmV0a9qgt7YWE28pw_w3K7z3wHoIJ3lPaa7vN5Op2k67hLDdBnxt-zgRdJ4KdCHcmDqQwfj7J139gVYCXqTesSttZXAOJHbykzmISZ-kjhoKUjiCeu6Sx3O_tXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
طائرة مسيرة تستهدف مقر لاحد الاحزاب المعارضة الايرانية الكوردية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79045" target="_blank">📅 23:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79044">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634b152a86.mp4?token=WE1XT66TY4xcCmCk-r1g1LAjgQEeSHs4asxEpaSKG_1ROFsml7Tc5DsZvrXQRDvVC4PqsabiNMpA9U9d2pVzuvXHDlMObOzd6-oeZMvsw6cia9JYC-i4Mlj8ttAOHxszN2FedA_UNMgL0UjVS-ir6BhJhg49nBqzfsjqCSBiTqnnin8-pACIQreRjbagDwNOX4LVTKsq-Ugmw7uYug_kFTJcr5KZwQ91PUuyaK096Tt-Vw1cOehQsC7HuSbXzrQ7baRjkmNZ9N8nCNvHBchOURzFZlF2siRFJHXZrmQZ8E_zjz7o8HsrsXCDX-fy0lWjmWkCiqsvsfFb0g5HXIJvbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634b152a86.mp4?token=WE1XT66TY4xcCmCk-r1g1LAjgQEeSHs4asxEpaSKG_1ROFsml7Tc5DsZvrXQRDvVC4PqsabiNMpA9U9d2pVzuvXHDlMObOzd6-oeZMvsw6cia9JYC-i4Mlj8ttAOHxszN2FedA_UNMgL0UjVS-ir6BhJhg49nBqzfsjqCSBiTqnnin8-pACIQreRjbagDwNOX4LVTKsq-Ugmw7uYug_kFTJcr5KZwQ91PUuyaK096Tt-Vw1cOehQsC7HuSbXzrQ7baRjkmNZ9N8nCNvHBchOURzFZlF2siRFJHXZrmQZ8E_zjz7o8HsrsXCDX-fy0lWjmWkCiqsvsfFb0g5HXIJvbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#عاجـــــــــــــل
⭐️
إندلاع إشتباكات مسلحة في ناحية كردرش بمحافظة أربيل شمالي العراق؛ سقوط عدة اصابات كحصيلة أولية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79044" target="_blank">📅 23:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79043">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c939a9b30.mp4?token=gMuSijVr31IDtvGoguC2ls_WpRfEKnYH21OlLRNnLPomKzkwciTv40_JxYYZ_7o8cB05h2NMdxdv_fWjWoFx-JwqSQ7HzZL8MbqADEbFbPbJUWFXwmb8h0k5cTKzosS2Xyg6Do5NNPBRdi-ygnCdmKwf5cgcYhEFlz8ZvxJVqrmjxy_DdEENMdbc6XRhGz1NM5cBhXw7SjAPmJXmqjSv2SaWHFNGgrXGnHT2WbuEdj3mkFLM69GMhff4LDZg6F6Q9-exDAC7GPhq5FR7v1ox8G4BqZ-Wz5oW5w8EUpSbONZL1asNzP7I59Mmqo1oxmACdFH-WQ2iZv37UgXqa_I5ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c939a9b30.mp4?token=gMuSijVr31IDtvGoguC2ls_WpRfEKnYH21OlLRNnLPomKzkwciTv40_JxYYZ_7o8cB05h2NMdxdv_fWjWoFx-JwqSQ7HzZL8MbqADEbFbPbJUWFXwmb8h0k5cTKzosS2Xyg6Do5NNPBRdi-ygnCdmKwf5cgcYhEFlz8ZvxJVqrmjxy_DdEENMdbc6XRhGz1NM5cBhXw7SjAPmJXmqjSv2SaWHFNGgrXGnHT2WbuEdj3mkFLM69GMhff4LDZg6F6Q9-exDAC7GPhq5FR7v1ox8G4BqZ-Wz5oW5w8EUpSbONZL1asNzP7I59Mmqo1oxmACdFH-WQ2iZv37UgXqa_I5ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
انفجار مجهول في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79043" target="_blank">📅 22:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79042">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
انفجار مجهول في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79042" target="_blank">📅 22:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79041">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258e6fd627.mp4?token=m9GYcxWK3seNllq44dtEzps6m_AEeD22AFiG2q3CnalW_DtQY_J-1pcLxfbhdglRbPq7DQc3Laiz8-eee7huNl_nnPApgXgnjn1ubwdytPZDv-tiiWPIjXIbrVai5d-62wp8qOcdVqeQMR5JcdxLjYSDm0qKZZj1-q2VsfKAIsPI2DZUdySEH_mqXQUbQIq4QzbGS8qT4n5vw-M4h8WIAucxWkUUjdE5UXe4VoLW57FP-chy_5_lqrMl79ryX19PZ9VZKzykzghM0RDnB6IfZTXa2RnEOJjkg2lVzpFYG451Smw9x0dUQlxUbiXfs56MQIJJiHaPYCeaz29YwRS4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258e6fd627.mp4?token=m9GYcxWK3seNllq44dtEzps6m_AEeD22AFiG2q3CnalW_DtQY_J-1pcLxfbhdglRbPq7DQc3Laiz8-eee7huNl_nnPApgXgnjn1ubwdytPZDv-tiiWPIjXIbrVai5d-62wp8qOcdVqeQMR5JcdxLjYSDm0qKZZj1-q2VsfKAIsPI2DZUdySEH_mqXQUbQIq4QzbGS8qT4n5vw-M4h8WIAucxWkUUjdE5UXe4VoLW57FP-chy_5_lqrMl79ryX19PZ9VZKzykzghM0RDnB6IfZTXa2RnEOJjkg2lVzpFYG451Smw9x0dUQlxUbiXfs56MQIJJiHaPYCeaz29YwRS4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنظيم داعش الإرهابي يتبنى استهداف صهريج نفط عراقي في مدينة منبج السورية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79041" target="_blank">📅 22:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79040">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هام.. وزارة النقل العراقية مسارات الحركة الجوية فوق العراق ستعود خلال ٢٤ ساعة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79040" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79039">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌟
رئاسة الوزراء العراقية توجه بتعديل ساعات الدوام الرسمي ليوم غدٍ الأربعاء ليصبح من الساعة العاشرة صباحاً لمتابعة ومؤازرة منتخبنا الوطني.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79039" target="_blank">📅 22:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79038">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
انتهك جيش الكيان الصهيوني الإرهابي وقف إطلاق النار في جنوب لبنان 84 مرة خلال اليومين الماضيين، بعد إعلان الرئيس الأمريكي انتهاء الحرب، ويواصل ارتكاب الجرائم والمجازر بحق الشعب اللبناني المظلوم.
تحذير: إذا لم يكف جيش الكيان الصهيوني القاتل للأطفال عن شروره في جنوب لبنان، فعليه أن يتوقع ردًا قاسيًا من القوات المسلحة الإيرانية الجبارة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79038" target="_blank">📅 21:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79037">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭐️
رويترز:
تتضمن اتفاقية إطارية بين الولايات المتحدة وإيران صندوق استثمار خاصًا مقترحًا بقيمة 300 مليار دولار أمريكي لدفع الاستثمار في إيران، حيث تم بالفعل التعهد بأكثر من نصف التمويل.
الصندوق، الذي تدعمه شركات من الولايات المتحدة ودول الخليج وآسيا وأمريكا الجنوبية وأفريقيا، يهدف إلى تشجيع كلا الجانبين على إنهاء اتفاقية أوسع نطاقًا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79037" target="_blank">📅 21:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79036">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
🌟
هبوط سعر الدولار الأمريكي أمام التومان الإيراني بعد الإعلان عن توقيع مذكرة التفاهم حيث  100$ دولار كان يعادل 18 مليون تومان، واليوم وصل الهبوط إلى 15.5 مليون تومان في مقابل 100$ دولار.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79036" target="_blank">📅 21:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79035">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15822cabb.mp4?token=OzH2ZmMMh8T2R2mD4QRRTBwWfMnE6FPAD6haJPwnn8kcyEjt2kbx7z414w8BwlYexw3xgzjk3KLJVzd1LmZRvPcCdUphyeg1DTp4QH1lYyH_MWGlwy0WAv6kkFFjl_8seE7Sa0ZQehYw_BYYiLC1t_Zki5kRkTyqmXyRUbSoe1x3_TiundOzaoFb2IcST72JdXHSgKyLLVSBddAJ6y6vyJQ8ombCDsgxodBDBfiMlfWL11U_LG8uhgzqpSiDa5xn5r-62ZQOmJrzElcryc-ity9o80m16Aj-eVqd6TF4SOgkvEltG5teqdy7xBKPI5ej2LxukOUh1s1cTTqa7IQrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15822cabb.mp4?token=OzH2ZmMMh8T2R2mD4QRRTBwWfMnE6FPAD6haJPwnn8kcyEjt2kbx7z414w8BwlYexw3xgzjk3KLJVzd1LmZRvPcCdUphyeg1DTp4QH1lYyH_MWGlwy0WAv6kkFFjl_8seE7Sa0ZQehYw_BYYiLC1t_Zki5kRkTyqmXyRUbSoe1x3_TiundOzaoFb2IcST72JdXHSgKyLLVSBddAJ6y6vyJQ8ombCDsgxodBDBfiMlfWL11U_LG8uhgzqpSiDa5xn5r-62ZQOmJrzElcryc-ity9o80m16Aj-eVqd6TF4SOgkvEltG5teqdy7xBKPI5ej2LxukOUh1s1cTTqa7IQrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تاج تاج على الراس سيد علي السيستاني.. بدء مراسم استبدال رايتي قبتي الإمام الحسين وأخيه العباس (عليهما السلام) في محافظة كربلاء المقدسة إيذاناً بحلول شهر محرم الحرام.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79035" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79034">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇱🇧
No need to press ok</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79034" target="_blank">📅 21:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79033">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
السيد عبدالملك بدرالدين الحوثي:
نؤكِّد على جهوزيتنا المستمرة تجاه أي تصعيد أو تطورات في الوضع الراهن من جهة العدو الأمريكي والإسرائيلي يستهدف المنطقة أو يسعى للانفراد بغزة من جديد،أو أيِّ ساحة في محور الجهاد وبلدان المنطقة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79033" target="_blank">📅 21:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79032">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d903bf1f4.mp4?token=C2DXV6soq5cwH0HdEDSjclf3MzzmxxGpbPHbpav84o24PTPE7KdibZBE1--aDzPUO-3ig5ZdvxX5moOr0VAXxOLyuXBRYxtviHcLx0psZ4_ECViRyFBeq-Qea93FseGkZCTNA03KmMJagU21uyzCr53U_h50SuBQWWyEAawgRq0IbmTiVRazCIs79qLZt1Iqx8wO44d57vpBJqRZXoNkLFvzeozpw28QVT8MyRieLEiXIVdgQw-aKr7No5CFhXGHTk9KDgW1va0KMuwsgZl88Q-5ZTVwzlbjVGTrnEG1shl1kejQ7K9r6q7C4JpmGkxlqLDGRacvYy8nSXEgiHYbag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d903bf1f4.mp4?token=C2DXV6soq5cwH0HdEDSjclf3MzzmxxGpbPHbpav84o24PTPE7KdibZBE1--aDzPUO-3ig5ZdvxX5moOr0VAXxOLyuXBRYxtviHcLx0psZ4_ECViRyFBeq-Qea93FseGkZCTNA03KmMJagU21uyzCr53U_h50SuBQWWyEAawgRq0IbmTiVRazCIs79qLZt1Iqx8wO44d57vpBJqRZXoNkLFvzeozpw28QVT8MyRieLEiXIVdgQw-aKr7No5CFhXGHTk9KDgW1va0KMuwsgZl88Q-5ZTVwzlbjVGTrnEG1shl1kejQ7K9r6q7C4JpmGkxlqLDGRacvYy8nSXEgiHYbag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تاج تاج على الراس سيد علي السيستاني..
بدء مراسم استبدال رايتي قبتي الإمام الحسين وأخيه العباس (عليهما السلام) في محافظة كربلاء المقدسة إيذاناً بحلول شهر محرم الحرام.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79032" target="_blank">📅 20:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79031">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ccff338e.mp4?token=f9vqmRQbBXayEYYNt7rK7X2aEKDX6YWVxuk_yykxg6afh8FG1TtXmtXPOwW_CvpwegpbjiiFJK9EklAGbd56ognFdbUsdQ0VqVLBgLlp6AJDnPYoissbhx4Z8tUEz8zFwhSoONDWwENnGsL4oeNy08e0KIcp_PT3tAeIhiIGqEQzgy8-KXFieTAacTfeh4ekow-ASght9VO16s3UziFKtf-5PxRJydR-NEsJtXmy7rN2F3oa52sMhkPqjWLQDPYarKZ_vFdG3cQbBAZMMiSmt1TEdROnUmoiBORnasV3bGDpffuBdGfvPeSAOxycTmaRIhBhnkm7lFu--9i3_159dIU2x_VMRantpfbNlqWYGiiLhXclbNIAOhSXBHPmEnxCTwhLqcHCD_J8kY1IaDx3jdnJ-bFO-mHN6u7CZp4RHZds5Lhm1dy0IkU2HyWrks-HafVkUgl_O43E7WqjAYd1mhvvM_cgr2qAk13HeKwa_oetGAG6HEiW36OSNCXz8OEe5v9PMowUMoaYvmP-J_qSGPooEVaVeWLAaMq3fHR1EdF0dkrqAo1s72JMJF55IyTNfigatRqWmeo_2V_qjHD_UPREQRRqu2kprhgRPp9bN6Hq2TLf5EXQn4Gl23BeB9ZL-OGo8oznfAKkL01WhxY7bMFOUixPIEW3CHqUCOHKjx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ccff338e.mp4?token=f9vqmRQbBXayEYYNt7rK7X2aEKDX6YWVxuk_yykxg6afh8FG1TtXmtXPOwW_CvpwegpbjiiFJK9EklAGbd56ognFdbUsdQ0VqVLBgLlp6AJDnPYoissbhx4Z8tUEz8zFwhSoONDWwENnGsL4oeNy08e0KIcp_PT3tAeIhiIGqEQzgy8-KXFieTAacTfeh4ekow-ASght9VO16s3UziFKtf-5PxRJydR-NEsJtXmy7rN2F3oa52sMhkPqjWLQDPYarKZ_vFdG3cQbBAZMMiSmt1TEdROnUmoiBORnasV3bGDpffuBdGfvPeSAOxycTmaRIhBhnkm7lFu--9i3_159dIU2x_VMRantpfbNlqWYGiiLhXclbNIAOhSXBHPmEnxCTwhLqcHCD_J8kY1IaDx3jdnJ-bFO-mHN6u7CZp4RHZds5Lhm1dy0IkU2HyWrks-HafVkUgl_O43E7WqjAYd1mhvvM_cgr2qAk13HeKwa_oetGAG6HEiW36OSNCXz8OEe5v9PMowUMoaYvmP-J_qSGPooEVaVeWLAaMq3fHR1EdF0dkrqAo1s72JMJF55IyTNfigatRqWmeo_2V_qjHD_UPREQRRqu2kprhgRPp9bN6Hq2TLf5EXQn4Gl23BeB9ZL-OGo8oznfAKkL01WhxY7bMFOUixPIEW3CHqUCOHKjx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
03-06-2026
هامر عسكري تابع لجيش العدو الإسرائيلي في الأطراف الجنوبيّة لبلدة زوطر الشرقيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79031" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79030">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
محافظة ديالى تقرر أن يكون الدوام الرسمي ليوم الأربعاء الموافق 2026/6/17 من الساعة التاسعة صباحاً ولغاية الساعة الثالثة ظهراً وذلك لإتاحة الفرصة للجميع لمتابعة مباراة منتخبنا الوطني أمام المنتخب النرويجي ضمن مباريات التصفيات المؤهلة إلى كأس العالم.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79030" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79029">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭐️
تحطم طائرة عسكرية أوكرانية، من طراز MiG-29، في منطقة خملنيتسكي.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79029" target="_blank">📅 20:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79028">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭐️
سي إن إن:
تشير تقديرات الاستخبارات الأمريكية إلى أن إيران باتت قادرة على إغلاق مضيق هرمز متى شاءت. وقال مصدر استخباراتي: "لقد منحنا إيران فعلياً سيطرةً على المضيق، وهو سلاحٌ يفوق في قوته أي سلاح نووي".
وفقًا للتقييمات، لا تزال إيران تحتفظ بما يكفي من الصواريخ والطائرات بدون طيار والأصول البحرية لتهديد المضيق مرة أخرى في المستقبل.
يعتقد بعض المسؤولين الأمريكيين أيضًا أن إدارة ترامب قللت من شأن استعداد إيران لاتخاذ مثل هذه الخطوة الجذرية خلال النزاع.
تخشى وكالات الاستخبارات الآن أن إيران تشعر بالجرأة بسبب نجاحها وقد تكون أكثر عرضة لاستخدام هذه الاستراتيجية في المواجهات المستقبلية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79028" target="_blank">📅 20:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79027">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYfbZoQElxGIJqRSfrMiHBY9rN38PkWSX0Z6yPETPKKNOMQ4tR1-5nh9RfGEtaElRffBKwTyR-OAsqaXKcxWz8qJtS_BP9GWHDYMXe_xhVFWgGTqtXQkrHSIqBumiWyasthV2xGZ2TeJlcrbe2oRPvOjW7nO6LZ2JeOKFJYz1NTHLZzIEd8KvqVWY2ibVEBTMR3bhnH53A4zmGMz_6xneRpimzOBf8J2Cs6dwqTZtolsAohLkvbtr8heWa21mpiudhJKx8MC8WaHthgFT5r5BKk2IZe_gFl0nuFFK0afQ0MEtK8jKjL8F6B-1u-ZixVRRBKNg_CtFQspHsKzyCbVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
اختلافات غیرموجّه و حتی موجّه را به تنازع و تفرقه تبدیل نکنید
🗓
بخشی از پیام ۷/خرداد/۱۴۰۵ رهبر انقلاب اسلامی
🖨
نسخه کیفیت اصلی
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79027" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79026">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs-C0T8mGTqO3BDsiYmU_r9tBwmn8KF1h9K9A34tqIwcmiTuGesW4hHvHG1JkCo3XmipVzFrU0CUKmCpIPE1k9TK2E-MKfggpTHGvDcTGOEwsKP8hK7ddfD4uPR64wbJDdiOgnBpf8C64WikMksUvNWmIKPV7ST1Wu1KesXlmjuocr7R3BHq3Xtzit-gt0XLdYrcNWGCKtqGJb3vwoAgLiEXrsENu4klhgenqqxhC5fzXqA72FnIUg6z1jpUWzdVj8sLmCUXCAE-d8EsIG_3xuNlszj7xyEXgNRG-9znr1HxWV0cyazJe1fcbG3ArjIt9v-E75dPYAX_smeljuJ1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
وزارة الداخلية البحرينية التابعة لعصابات آل خليفة تصدر قرار منع مشاركة بحق عدد من الرواديد الحسينيين في مراسيم العزاء بشهر محرم الحرام: الرادود عيس الغبص الرادود حسين الأسدي الرادود يوسف القصاب الرادود محمود الشهابي الرادود سيدجلال البلادي الرادود سيد حسين…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79026" target="_blank">📅 19:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79025">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⭐️
غارات صهيونية جديدة تطال بلدة ميفدون بالجنوب اللبناني ؛ إرتقاء 4 شهداء كحصيلة أولية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79025" target="_blank">📅 19:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇫🇷
🌟
فرانس برس:
تتخلى وكالة الاستخبارات الداخلية الفرنسية (DGSI) عن شركة Palantir، حيث يشير رئيس الوزراء سيباستيان لوكورنو إلى مخاوف من الاعتماد الاستراتيجي على الولايات المتحدة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79024" target="_blank">📅 19:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
🇮🇷
مصادر أمريكية:
واشنطن ستسمح لطهران بالبدء فورا ببيع النفط والوقود بموجب اتفاق إنهاء الحرب.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79023" target="_blank">📅 19:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111449badc.mp4?token=Mu_6v9mjnNo9BaiT1MTKCMQJhCRml0t4jiVruWN-bCSiRADTvpbZ2pXg32frUq8enNyMDwF-4cvjTSrbV0m0TPXtmDkP3CvKWpfNKTcGcKIM1DwREY7r2evST4iMw3tDHnSTTP1c8WzBbkGFyrW0acIAX32l3RfX1tPeic8gN0tQ6QsZVrYu4objWlZQOVbN2-qGQbVKiP96d1iOygOj5XgFKUcWSBugyo6ORgYBfVHk-N_ultkyOxr2hFiFOiGTS8Neg-CBt6U-yh2QKc1BcJZljKK8EkEyXH9eSq6kZZYRhM2gsurDVrfem-e-mgqshGS8V71bONOezQcrkzpnWh7R-zaud31Va3UWmunPpzj9K7SOi8u9rtlo08Vs_NZy8AIw0kAh6V71Pcj71Y7__rG7byyEQnQsaqibOS5uq-t3m9JYbk0n7rxkdxX0mzvwwedf_aDKBQ3YCCanthOlWcImxAMzdRHI7T_Mcn9nAtuf3zz6j34Qeb7eZV5Lilv_eygNGB3FpXnn-jROc5rsFBNJHYTZAxgnP7Zrk4-JPOZUDj-kRL5Db-SSkTfq8X7LLfTIowp0efgoTqcV5KNnyk3iQJqBMYbhHqYB8wgW5TgY1mgLMRJ8QDxGW6eoJnOpa9r8cUK_I1MFQPPRRGO8nU-Vp6dziBbTXy5fpCqXlSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111449badc.mp4?token=Mu_6v9mjnNo9BaiT1MTKCMQJhCRml0t4jiVruWN-bCSiRADTvpbZ2pXg32frUq8enNyMDwF-4cvjTSrbV0m0TPXtmDkP3CvKWpfNKTcGcKIM1DwREY7r2evST4iMw3tDHnSTTP1c8WzBbkGFyrW0acIAX32l3RfX1tPeic8gN0tQ6QsZVrYu4objWlZQOVbN2-qGQbVKiP96d1iOygOj5XgFKUcWSBugyo6ORgYBfVHk-N_ultkyOxr2hFiFOiGTS8Neg-CBt6U-yh2QKc1BcJZljKK8EkEyXH9eSq6kZZYRhM2gsurDVrfem-e-mgqshGS8V71bONOezQcrkzpnWh7R-zaud31Va3UWmunPpzj9K7SOi8u9rtlo08Vs_NZy8AIw0kAh6V71Pcj71Y7__rG7byyEQnQsaqibOS5uq-t3m9JYbk0n7rxkdxX0mzvwwedf_aDKBQ3YCCanthOlWcImxAMzdRHI7T_Mcn9nAtuf3zz6j34Qeb7eZV5Lilv_eygNGB3FpXnn-jROc5rsFBNJHYTZAxgnP7Zrk4-JPOZUDj-kRL5Db-SSkTfq8X7LLfTIowp0efgoTqcV5KNnyk3iQJqBMYbhHqYB8wgW5TgY1mgLMRJ8QDxGW6eoJnOpa9r8cUK_I1MFQPPRRGO8nU-Vp6dziBbTXy5fpCqXlSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-06-2026
هامر عسكري تابع لجيش العدو الإسرائيلي في الأطراف الشرقية لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79022" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇷🇺
🇬🇧
ذي تليغراف:
أطلقت الفرقاطة الروسية "الأدميرال غريغوروفيتش" طلقات تحذيرية على يخت بريطاني في القناة الإنجليزية يوم الاثنين، بعد اقتراب السفينتين من بعضهما.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79021" target="_blank">📅 18:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79020">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d03b683c.mp4?token=lNeGOIpKh_sGnG9jicZ0TDr6NInYwk5RSJFYiqrQrraM24igD21VOujbJBW_7pVDaFNrUpBlvs_Du0W7TAxBwDyG-XchXforj90XPGaNMQwGchsFyBVRxx2IQ6H2vmoNp2AqIoZs-KWIjA7MAGGEQO_sl-wgRFGgX8dPF59nJ34UU6ryHzDfxSik4WCr0FBJVTYfbiVYjdgYfw8pTnv8XsEQ_MVV6M1E7dZRYdlgcSapP8iOA8MVAXVY0mc-6_Yw-qBU7kc3k3wNK2cOaEadl9gwZMgBdr6xJqRb0qOqJB_sFZjDVzQtQdpbmXeWMpN_0q7lhgvAICWGKDs_VHk-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d03b683c.mp4?token=lNeGOIpKh_sGnG9jicZ0TDr6NInYwk5RSJFYiqrQrraM24igD21VOujbJBW_7pVDaFNrUpBlvs_Du0W7TAxBwDyG-XchXforj90XPGaNMQwGchsFyBVRxx2IQ6H2vmoNp2AqIoZs-KWIjA7MAGGEQO_sl-wgRFGgX8dPF59nJ34UU6ryHzDfxSik4WCr0FBJVTYfbiVYjdgYfw8pTnv8XsEQ_MVV6M1E7dZRYdlgcSapP8iOA8MVAXVY0mc-6_Yw-qBU7kc3k3wNK2cOaEadl9gwZMgBdr6xJqRb0qOqJB_sFZjDVzQtQdpbmXeWMpN_0q7lhgvAICWGKDs_VHk-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية تستهدف منطقة دار المعلمين في بلدة النبطية الفوقا جنوب لبنان</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79020" target="_blank">📅 17:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79019">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇨🇭
‏
الخارجية السويسرية:
اتفاق أميركا وإيران سيوقع في منتجع بورغنتشتوك الجمعة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79019" target="_blank">📅 17:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79018">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🌟
وزير الاتصالات العراقي مصطفى سند:
بالتنسيق والتعاون المشترك مع جهاز الأمن الوطني، نعلن عن تفكيك شبكة منظمة من الشركات المتورطة في إعادة توجيه وبيع سعات الإنترنت المخصصة للأغراض التجارية وغير المنزلية، وتسويقها للمواطنين كاشتراكات منزلية عبر فواتير غير رسمية، طالت أكثر من 10,000 وحدة سكنية.
ونؤكد استكمال كافة الإجراءات القانونية واستحصال الموافقات القضائية اللازمة لإستكمال العملية.
إن هذه العملية تمثل ضبطاً لمجموعة واحدة فقط من ضمن عشرات الشبكات المرصودة التي يجري تفكيكها تتابعاً، وعمدت بعض الشركات المخالفة إلى قطع الخدمة فجأة عن المواطنين لإخفاء معالم مخالفتها ودون أي أوامر إطفاء رسمية من جهتنا.
تُقدّر القيمة المالية المهدورة لجميع عمليات الفوترة غير الشرعية  والتي تزود أكثر من 1.5 مليون ونصف مستخدم، بنحو (200) مليار دينار عراقي سنوياً.
وتتعهد وزارتنا إنه في حال تم استرداد هذه الأموال (أو جزء منها) بتوظيفها مباشرة في :
تقديم خدمات إنترنت مجانية لبعض المؤسسات الخدمية والأماكن الترفيهية
خفض أسعار الاشتراكات الحالية
زيادة سرعة الإنترنت بنسبة 20% لشبكات ( الكيبل الضوئي واللاسلكي) خلال عام 2027</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79018" target="_blank">📅 17:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79017">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwQbcWT9Ms6mKFcPulJrHfDUVDVJqSfxj9Wvpg45aoC5-GG46b-8UToxuMFCdYqEYwNrc6BAzIfeOYRZZnzP4YjskNV4NXHdObqPp3mVF86ezSdJa44_rPOZ980QPQDQdFwW7ilVsSYfT_vh8OAckTRIcGEec_De-L5rwKlhebPqUniPiNTSzsbbBeXAsiGseOdguCRPeM4lr39JMfYwPp2wLevI4if35af30yF4UgCJryl3yWfyUGg5v9z06cSkstfcOsNydbJjjTmwAlxTMKGYQ-5czK-VxHJGLIP3_SdqHtU4I-UhF0xQmHS3hTJmP_NFDMg8Pgrk4S69-OXdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
المبعوث الامريكي توم باراك يقول أنه حدد مسار التعاون بين بغداد واربيل خلال لقائه مع مسعود البرزاني ومسرور البرزاني
شنو هذا التدخل الايراني ماله رداد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79017" target="_blank">📅 17:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79016">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇹🇷
🌟
تركيا ترفض طلبا عراقيا لتمديد اتفاقية تصدير النفط عبر خط جيهان لمدة عام على الأقل لحين توقيع اتفاق جديد
الجانب التركي يمارس ضغوطاً تفاوضية لرفع معدلات تشغيل خط الأنابيب الذي يمر عبر أراضيها من شمال العراق ليعمل بكامل طاقته الاستيعابية البالغة 1.5 مليون برميل يومياً على ان تكون اتفاقية استراتيجية طويلة الأجل تمتد ما بين 5 إلى 10 سنوات وتتضمن بنوداً إلزامية تفرض على العراق دفع رسوم مالية تعويضية مقابل أي طاقة استيعابية غير مستخدمة أو مهدرة في خط الأنابيب طوال فترة التعاقد
مسؤول تركي يقول انه في حال وصول المفاوضات الحالية إلى طريق مسدود وعجز الطرفين عن صياغة المسودة الجديدة قبل نهاية الشهر المقبل فإن تركيا قد تتجه لمطالبة العراق بوقف تدفقات النفط عبر الأنبوب فوراً</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79016" target="_blank">📅 16:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79015">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f917cdfbc3.mp4?token=OBIZGE2ZTHCXiOBNaNHDrE9Te4-CC8X2G4VNYEAl0MI8vFzCkeuY3_7lP2SrVBt-9ADykmtqBonBiypBkjWnf6BHoKXQ434oYH3VuudcP0YV-RDptAnvlzNx2yoCVzhLxtY3OPJATCMh14TsRIkeu-vGFXwv_DDTD86sWNImkoF5HB1a5_RDLwB7q5QWasJyJGKjO0E-WkuLVe7sD_CEOUP-McwIwP9tTHxk3SgLvUAqaL8KPkwLijc8IzQlFuaiVKhff2fbP23kIugj2igW-mZ3TPVWxXALtvtVDLZKLDnm3q2vrsTIm3Q_3Hfw-ufbUyjSBkjnMBVpmusr2toXZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f917cdfbc3.mp4?token=OBIZGE2ZTHCXiOBNaNHDrE9Te4-CC8X2G4VNYEAl0MI8vFzCkeuY3_7lP2SrVBt-9ADykmtqBonBiypBkjWnf6BHoKXQ434oYH3VuudcP0YV-RDptAnvlzNx2yoCVzhLxtY3OPJATCMh14TsRIkeu-vGFXwv_DDTD86sWNImkoF5HB1a5_RDLwB7q5QWasJyJGKjO0E-WkuLVe7sD_CEOUP-McwIwP9tTHxk3SgLvUAqaL8KPkwLijc8IzQlFuaiVKhff2fbP23kIugj2igW-mZ3TPVWxXALtvtVDLZKLDnm3q2vrsTIm3Q_3Hfw-ufbUyjSBkjnMBVpmusr2toXZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الولايات المتحدة تواصل فشلها في تنظيم كأس العالم:
اشتباكات عنيفة بين جماهير الجزائر والارجنتين في ميدان التايم سكوير بنيويورك.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79015" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79014">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
إسرائيل طلبت الاطلاع على مذكرة التفاهم مع إيران لكن أميركا رفضت.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79014" target="_blank">📅 16:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79013">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaGQXPpp5_GX6JaZYOSlUS2uqNPdUETIMtWAKdjqbV9uwiFV0NOk3n-i7ZgURmWXGhfLm6yfmfneETor1ALetW4oq6nsaxDpR7KWjHyg2CIfqf7tzH-oJxUMjeJb0kSnYGkv_ffi_YbANFY5OOrSHpxqaxgStHEPzP4rUKlczjH4mW2FnBgWAk2pKkSitKUe6DKP5Y-_5GusdoaAeCQVfcb-pnyQ9fROLA09A-jNFpV25QaS-g8evbwaOSBZ4KiaqZAG8ZbaTJ583rC9k3pqvTXZdF7DyTqebw2XFgJcCgfb3kPxkRE37rq7Z9GjvWGVa4m1RfGAIC97GHB9TnQIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اليمنيين ينتفضون في صنعاء تجاه اساءة ترامب لمكة المكرمة وسط صمت من قبل نظام ال سعود</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79013" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79012">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
الكابينت المصغر سيناقش اليوم طلب امريكي بالانسحاب من لبنان لحين توقيع الاتفاق مع ايران.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79012" target="_blank">📅 16:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79011">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c2863c31.mp4?token=iIspL3RulPI8d52ID1SrRcSoCcPUjdxfOeast7biiaLSbcdowGywtEH_de1rpmpf1ZLJgSI9Sa8yHkN0d4X7KC-lE8gZjFo8I9qxLBJQ1CuxAFI5S3IKQ6rrpbksPWl_SpuGIJdK9UAlwCw0AfV-ICt7xdclhGK0ttAdcjWioB2xJ_VjX0eduI0e87UY9z5a9Qqwgoe8o5nQCsmJ50JotHhN3Iv8F-3ffInU9ez8h6MR8D0Qv4f_nQlsHqrVodRkC9nPEB1yQlyEtXGZkKlKy5n7L11HmryUKlkRj_qRpciMH_lSjk5-BboXDy1i_dj4P-pifN-wkmhATISnol8kow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c2863c31.mp4?token=iIspL3RulPI8d52ID1SrRcSoCcPUjdxfOeast7biiaLSbcdowGywtEH_de1rpmpf1ZLJgSI9Sa8yHkN0d4X7KC-lE8gZjFo8I9qxLBJQ1CuxAFI5S3IKQ6rrpbksPWl_SpuGIJdK9UAlwCw0AfV-ICt7xdclhGK0ttAdcjWioB2xJ_VjX0eduI0e87UY9z5a9Qqwgoe8o5nQCsmJ50JotHhN3Iv8F-3ffInU9ez8h6MR8D0Qv4f_nQlsHqrVodRkC9nPEB1yQlyEtXGZkKlKy5n7L11HmryUKlkRj_qRpciMH_lSjk5-BboXDy1i_dj4P-pifN-wkmhATISnol8kow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية تستهدف منطقة دار المعلمين في بلدة النبطية الفوقا جنوب لبنان</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79011" target="_blank">📅 16:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79010">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامب: سأرسل اتفاق إيران إلى الكونغرس لمراجعته.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79010" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79009">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامب: سنناقش اتفاق إيران مع وسائل الإعلام في غضون أيام قليلة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79009" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79008">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسالة حجة الإسلام والمسلمين الأمين العام لحزب الله سماحة الشيخ نعيم قاسم إلى رئيس مجلس الشورى الإسلامي الدكتور محمد رضا قاليباف:
بسم الله الرحمن الرحيم
جناب رئيس مجلس الشورى الإسلامي الدكتور محمد رضا قاليباف أيَّدكم المولى ورعاكم.
السلام عليكم ورحمة الله وبركاته
تعجز الكلمات عن تعبيرنا بالشكر الكبير للمواقف القوية والداعمة للبنان وشعبه ومقاومته لإلزام الكيان الإسرائيلي بالوقف الفوري والدائم للعمليات العسكرية على جميع الجبهات بما فيها لبنان، ربطًا بوقف الحرب على الجمهورية الإسلامية الإيرانية، كبندٍ أول وأساس للاتفاق بين إيران وأميركا. فقد حوَّلتم بارقة الأمل الوحيدة والفاعلة في كف يد العدوان الإسرائيلي الأميركي على لبنان إلى حقيقة أثبت للعالم بأنَّ إيران نصيرة الحق والمقاومة والمستضعفين، ولو احتذى طريقها آخرون لما تجبَّرت أميركا وإسرائيل، ولما بقي الاحتلال الصهيوني جاسمًا على أرض فلسطين والقدس.
قلنا دائمًا بأنَّ إيران أعطت حزب الله والمقاومة ولشعب لبنان كلَّ شيء ولم تأخذ منه شيئًا، هي أُعطتنا لخياراتنا، لقوتنا من أجل تحرير أرضنا، لبلسمة جراحات مجتمعنا ومساعدته. والآن تبذل إيران الدم، فتتصدى بقصف الكيان الصهيوني ردًا على قصفه لضاحية بيروت الجنوبية، وتتحمل تبعاته التي تنذر بالحرب عليها مع عظيم التضحيات. سأقولها صادحة: إيران أيقونة العزة والشرف.
أشكركم بإسم حزب الله ومقاومته الإسلامية، بإسم المحبين من الشعب اللبناني الذين يرغبون أن نوصل شكرهم إليكم، بإسم الشهداء وفي مقدمهم سيد شهداء الأمة السيد حسن نصر الله(رض) والجرحى والأسرى، بصفتكم كبير المفاوضين مع فريق عملكم المباشر ومنهم وزير الخارجية الدكتور عباس عراقجي، راجيًا إيصال الشكر والامتنان إلى القائد آية الله السيد مجتبى الخامنئي(دام ظله) الذي غمرنا باهتمامه، وأحيى فينا بركات ورعاية الشهيد الإمام الخامنئي(قده)، ورئيس الجمهورية الدكتور بازكشيان المحب للمقاومة، وحرس الثورة الإسلامية الإيرانية هذه القوة النورانية التي قلبت المعادلة ببأسها، والجيش والنخب وكل الفعليات الرسمية والشعبية.
وأخص بالذكر الشعب الإيراني العظيم لقد رأيناهم في ساحات المدن الإيرانية وسمعنا مطالبهم في بذل مهجهم لإنقاذ المقاومة وشعبها. شكرًا لكم. شكرًا لإيران الوفية. والسلام عليكم ورحمة الله وبركاته.
الأمين العام لحزب الله نعيم قاسم
01 محرم 1448 هـ
16 حزيران
2026</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79008" target="_blank">📅 16:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79007">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامب: سأعقد مؤتمرًا صحفيًا حول الاتفاق الإيراني.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79007" target="_blank">📅 16:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79006">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامب: سننشر نص الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79006" target="_blank">📅 16:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79005">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇱🇧
الأمين العام لحزب الله سماحة الشيخ نعيم قاسم يلقي كلمة في افتتاح المجلس العاشورائي المركزي يوم غد الاربعاء الساعة 6 مساءً.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79005" target="_blank">📅 16:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79004">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامب: العلاقة الجديدة مع ايران باتت طبيعية وأعتقد أن الأمور ستتقدم بسرعة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79004" target="_blank">📅 16:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79003">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامب: بدأت السفن في العبور عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79003" target="_blank">📅 16:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79002">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامب: مضيق هرمز سيفتح بالكامل بحلول يوم الجمعة</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79002" target="_blank">📅 15:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79001">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامب: مضيق هرمز سيفتح بالكامل بحلول يوم الجمعة</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79001" target="_blank">📅 15:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79000">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مكتب التحقيقات الفيدرالي يزعم احباط هجوم بالمسيرات والقناصة على البيت الأبيض</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79000" target="_blank">📅 15:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78999">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
مستشار حكومي عراقي:
عدم إقرار الموازنة لن يؤدي إلى توقف صرف رواتب الموظفين أو المتقاعدين أو مستفيدي الرعاية الاجتماعية، هذه الرواتب تعد من النفقات الأساسية التي تلتزم الدولة بتأمينها بموجب الأطر القانونية والمالية النافذة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78999" target="_blank">📅 15:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78998">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHxkZ3dH46p7v8yOxmqOudkAAf194gjFyW_0clVmmjrOqXjTMCWErmYkDIj_fheXAnf0gCxKDGj9CepcJN01T4W646mwrxxEQk0cZWSwTrl-iILZc-thcy1IsI1_ft-Ii-jmb3pfOiTfY1Y5_K3GidyaX83BCc4QKQr8n11qjt0sk11dIHy758LJFvH542dZKtYlh7fnAlpQbbDpQ2ZP2ypt4yJYqjmcpTHg9S0DgIZ8PXffaSzEH4w2Lhsacs1PIG_R6WatiUekLwzFUiOOaq-NCcKdPQhKucgFBcCm2FynHAbN15593RrKORommiyw-UQrakrvC6Zop1UBrI1HXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"سنعيد الامن الى الشمال وسنصنع الامن"</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78998" target="_blank">📅 15:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78997">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇹🇷
‏وزير خارجية تركيا: كانت هناك مساع إسرائيلية لإفشال الاتفاق بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78997" target="_blank">📅 15:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78996">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏
زيلينسكي:
ترامب منفتح على دعم أوكرانيا بصواريخ للدفاع الجوي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78996" target="_blank">📅 15:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78995">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامب: لو لم أكن موجوداً لما كانت هناك إسرائيل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78995" target="_blank">📅 14:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78994">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇹🇷
‏
وزير خارجية تركيا:
كانت هناك مساع إسرائيلية لإفشال الاتفاق بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78994" target="_blank">📅 14:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78993">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af5f6a955.mp4?token=XuHALCKhUuKU_88tRnSi_9SgPy95V9xwlocy7HSvnNquchnpS6W-Kp906wjb6S-OrBSBPQsbTpZ5c0j7fQYK3Sszv7hUCLdSscLlCTnm8nCIIL8WJz1xEOu-Dat_XCg3q0L8fXIxgw9_Wuqj5O7X5TuO7CxFSzPjYtZrnC5flWyrUmbKuZ4y2jbIr8iVRpOAj-KokTW9Nk3wISN54am6tArWgtmdIe6UUTGtJhODnu23mO0VUq9ydR9p2uI2oAqUzdIct6dIG7GeB8jwzriS2lVeu3OhkN5Io7C7-AyyAFEQD9RfpktybdT0X5_kL4nvDo5fjmfjbIjGutleQAkzJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af5f6a955.mp4?token=XuHALCKhUuKU_88tRnSi_9SgPy95V9xwlocy7HSvnNquchnpS6W-Kp906wjb6S-OrBSBPQsbTpZ5c0j7fQYK3Sszv7hUCLdSscLlCTnm8nCIIL8WJz1xEOu-Dat_XCg3q0L8fXIxgw9_Wuqj5O7X5TuO7CxFSzPjYtZrnC5flWyrUmbKuZ4y2jbIr8iVRpOAj-KokTW9Nk3wISN54am6tArWgtmdIe6UUTGtJhODnu23mO0VUq9ydR9p2uI2oAqUzdIct6dIG7GeB8jwzriS2lVeu3OhkN5Io7C7-AyyAFEQD9RfpktybdT0X5_kL4nvDo5fjmfjbIjGutleQAkzJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رئيس وزراء النرويج يخاطب لاعبي المنتخب النرويجي: "احلموا بأحلام كبيرة، واذهبوا واسحقوا العراق"!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78993" target="_blank">📅 13:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78992">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامب: إذا لم تستطع إسرائيل إنجاز الأمر في لبنان دون قتل الجميع، فيجب على سوريا أن تقوم بذلك</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78992" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78991">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏ترامب: لم يعجبني هجوم إسرائيل على بيروت قبيل توقيع اتفاق إيران</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78991" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78990">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامب: أنا لست غاضبًا من نتنياهو.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78990" target="_blank">📅 13:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78989">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏ترامب: أقترح على إسرائيل أن تترك سوريا</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78989" target="_blank">📅 13:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78988">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامب: إذا هاجمت إسرائيل لبنان، فقد يبقى الاتفاق قائمًا.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78988" target="_blank">📅 13:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78987">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامب: كنا نريد الذهاب إلى إيران للحصول على اليورانيوم المخصب لكن هذا لم يتم</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78987" target="_blank">📅 13:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78986">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
ترامب: يجب على روسيا أن تبرم اتفاقًا.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78986" target="_blank">📅 13:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78985">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامب: تم الانتقال إلى المرحلة الثانية من صفقة إيران.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/78985" target="_blank">📅 13:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78984">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd979693a6.mp4?token=Fgewr1fzbWksDJzy85acz0OLOi2Vj9Fqz_18zglalzZ3ltcQqPniHZn34gkLRmoCcqX7zmNSF3yc0jgxVpyaLFJoVAoUdSbZRb1T6c1A61WbtZOC9f2xbMWNPtYQ_16fOWzmbGwnxhiFXcEPIcu8VV7PRBjyrIekkwvTDOIe5zwoV5Uh3EyMdhNQNY5_BlgPEnUhpevCzwo_ZylC25N_pZXHweP3xOA1---L8X6vNYQK2m4da7_GGFRUrEB6yslaqJnghgrA3WNxynbyeZBttrve6mx076XZtaRuseg1HNyMPJqRxWyK3f2cCAkABv_sO3q3W6nm_XHwTvR6BAqtcoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd979693a6.mp4?token=Fgewr1fzbWksDJzy85acz0OLOi2Vj9Fqz_18zglalzZ3ltcQqPniHZn34gkLRmoCcqX7zmNSF3yc0jgxVpyaLFJoVAoUdSbZRb1T6c1A61WbtZOC9f2xbMWNPtYQ_16fOWzmbGwnxhiFXcEPIcu8VV7PRBjyrIekkwvTDOIe5zwoV5Uh3EyMdhNQNY5_BlgPEnUhpevCzwo_ZylC25N_pZXHweP3xOA1---L8X6vNYQK2m4da7_GGFRUrEB6yslaqJnghgrA3WNxynbyeZBttrve6mx076XZtaRuseg1HNyMPJqRxWyK3f2cCAkABv_sO3q3W6nm_XHwTvR6BAqtcoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#بالفيديو
⭐️
اندلاع نزاع بين حماية النائب خالد العبيدي وعناصر حماية وكيل وزير الداخلية في مدينة الموصل.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78984" target="_blank">📅 13:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامب: تم الانتقال إلى المرحلة الثانية من صفقة إيران.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/78983" target="_blank">📅 13:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78982">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQJvEZ5LSa3E_ANFaPG2A821Hq54t4Yw-Dqx61sWOp4QGNFUIJIOD-MQBAFdv2EAOutD7nExou0L8kE61m2JHL42W4rmaqlbd1HZL89ua0wKdf992tGyS6a2uui7pWZlxZ6Nfhsbit9uv78aS2GvOplH0KEysZx5irW0KydYVcQzDaQ749qUzVUy3fxycALuWxxmtwXu128pBRG-6FPb06Jp5FS2iPWm2VzgP9vCqkx4dZGbkDjYBaIrk6sF-NymcrKPoGr5CAZlFk78BqTu6ElMXJW0yd6RKNTT78D7O73CpI_6hEkwqdDJWpbF93HAwW8hv5ttNH8lf-MT0XmoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المبعوث الامريكي توم باراك يبلغ قادة اقليم كردستان العراق أنهم سيسحبون قواتهم من أربيل والاقليم في شهر التاسع من العام الحالي.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/78982" target="_blank">📅 12:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ox0HBIDqUpfJYiwYIWLk3VkVzDuJwIr_UnvUBf4i31Gl5i0rkJw3JsfCYVibYxuD8vqW4mUcjAbDz9YruSgAJHZdvFSU0Zzn2kejEvdxsPsiaW5QGSb2TEaBr7pI53JCYaCi_uFXlpknDpwFNubychYw_PcRS-doMc6CO-DzQm2ORVNwhYcJ0g8HZuwRMm5GKrs0HIvqd4PzI-w1t5XCDQ_mrFjlxX6ybmiBHB8E6OSfiFHu65LQNedruQ1xqp6rIXgeat3JNCjWKatMwBuQVItLhMAOHIY8ugJdK8TTGUs6tewNks6LhzuazH8amGbGBnk5cb1_GzktvtAyADFuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78981" target="_blank">📅 12:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78980">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-06-2026 تجمّع لجنود وآليات جيش العدو الإسرائيلي في بلدة القنطرة جنوبيّ لبنان بصاروخين نوعيّين.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/78980" target="_blank">📅 12:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78979">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني: واشنطن تعهدت بالنيابة عن حلفائها بأن الحرب ستنتهي في كل الجبهات، بند بمذكرة التفاهم يؤكد صراحة إنهاء الحرب والعمليات العسكرية بكل الجبهات منها لبنان.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78979" target="_blank">📅 12:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78978">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني:
واشنطن تعهدت بالنيابة عن حلفائها بأن الحرب ستنتهي في كل الجبهات، بند بمذكرة التفاهم يؤكد صراحة إنهاء الحرب والعمليات العسكرية بكل الجبهات منها لبنان.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/78978" target="_blank">📅 12:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78977">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc27dffdc2.mp4?token=OEl8ArAScJv7DcNt0GnqTpjZpv0jUJWr1jIJvziSsdQXaKD9tkoXl1q2WS57D13LH8sKROidGiC8JbOEWV4qzTrgpkMIMYoF0_itCI1gJwGsooElGsoMIhg9yPho76EJbejyRQJ9y2EMygW9BLzsAdCwNXpihkneSkw8BKxcWUEQZfMSs_VEtXkJb9T3yFqa3oJq3BGtV-FVF17n8lniFen3kxiyfczHiny6pcQtqnAny0gowQnc5pK6caPrJGMxOJ4g4Y0W8KomcSiJkiMwEiF0KNU-TqcqWp0mYurmaG7wGdN8vreU0a7-SF_wGWdnowX6izRRDzblU9J3w_M-2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc27dffdc2.mp4?token=OEl8ArAScJv7DcNt0GnqTpjZpv0jUJWr1jIJvziSsdQXaKD9tkoXl1q2WS57D13LH8sKROidGiC8JbOEWV4qzTrgpkMIMYoF0_itCI1gJwGsooElGsoMIhg9yPho76EJbejyRQJ9y2EMygW9BLzsAdCwNXpihkneSkw8BKxcWUEQZfMSs_VEtXkJb9T3yFqa3oJq3BGtV-FVF17n8lniFen3kxiyfczHiny6pcQtqnAny0gowQnc5pK6caPrJGMxOJ4g4Y0W8KomcSiJkiMwEiF0KNU-TqcqWp0mYurmaG7wGdN8vreU0a7-SF_wGWdnowX6izRRDzblU9J3w_M-2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مرور ناقلة النفط الخام الإيرانية الأولى "ديونا" المحملة بالنفط خارج الحصار الأمريكي.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78977" target="_blank">📅 12:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9-vqvcqKcHd-A0imnt_UeblUtRQEBFbNci-SRy6JWiHvDIPOwH1PAERFCg_rRAFAr01HxlbHXrFRzgxGSG2JUvLgCihYCbz5OdJocao73z_7yNl7uNNfdRDTl91JPKsy3NzKzUE9WGmY9OvwudGZZSnzYfpRAldFA0drAdAyjHD60gsBQUOBSuVG24SPChpgsp7v08HTNCcqhVVWpjxcN9FWUW9aZmjvvumkwSFUyRAxK-PLF6A-m3BXByci365I0iOKFB4Ai2wAvR7lLjUM41LMYrnnVFn2MwJtYTbZj-W51VHrzAA2K-wkcVexgCqJzT1MyiT6BBsJcyP_lx_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مرور ناقلة النفط الخام الإيرانية الأولى "ديونا" المحملة بالنفط خارج الحصار الأمريكي.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78976" target="_blank">📅 12:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc22d2744.mp4?token=afEfU3FX4wrHvuxyoj5Vjg4Td8fP0-fe_D3dnh-DZTBQQAdEss6QrKawJVF2eul2je-e8Q7Rx7ZdDYPQwvuImmHkuEdXCAI7baBvmfxZnbvYmRqRSWz9bMsN1r_fCV5f5mDQINoAYhsc1aj7PZcRqr5BvJSz7KruZd3Hd7oHDNTiyzbFUcFgXIf2o0v0kC0fNf3Gp-DFwYL97aakoxvwfNPKVVP5WhxIC1BA2NTqNqI7tajxfvOfrEwkZlijQDYw7y8hCqS-qzj3V-s-kmHKUnEF24F2OeKyhW7gqiyrz86pP9w2KFMk6peuZqACUvAPPoB46nIOoZOZI6H3C29NAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc22d2744.mp4?token=afEfU3FX4wrHvuxyoj5Vjg4Td8fP0-fe_D3dnh-DZTBQQAdEss6QrKawJVF2eul2je-e8Q7Rx7ZdDYPQwvuImmHkuEdXCAI7baBvmfxZnbvYmRqRSWz9bMsN1r_fCV5f5mDQINoAYhsc1aj7PZcRqr5BvJSz7KruZd3Hd7oHDNTiyzbFUcFgXIf2o0v0kC0fNf3Gp-DFwYL97aakoxvwfNPKVVP5WhxIC1BA2NTqNqI7tajxfvOfrEwkZlijQDYw7y8hCqS-qzj3V-s-kmHKUnEF24F2OeKyhW7gqiyrz86pP9w2KFMk6peuZqACUvAPPoB46nIOoZOZI6H3C29NAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد من إطلاق صواريخ اعتراضية من مستوطنة المطلة شمال الكيان المحتل لاعتراض صواريخ حزب الله.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/78975" target="_blank">📅 11:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7652e2bde8.mp4?token=rxQJRzmFWCVSmDNEcRmWZ1iIq8cUyBY-NUASUFbn1rbhcOfhoCi9psz5i5x3cFRojRMs-3gOLawOuhX3zctnG5T9jABWicGtVg5Q2URLVT4ZKMejRGTEP73g3ck58gZRtP79ZpYjmlnfP2cqnWlbIZ2GLoGRQs5WywU2acR6bOpcDKXAJ7OimxXW1gJyP03SmUaVflLfO7XGQVpOCXiWEzermGd9BqxfYKeBql5Hdvz07hgkJlNl2Fxn0b9NSVC3H0kZiQYH8g-NSQQOqHU15pbklJH5SAve8mzijgFTJdwk7e2NxZCGSkfPdnpVTalAOVPE67GMz5mFFNg96JRn96xA5coaYKI6-SuCiUFIBrZhhfEECAUg0iI-UzXcaC4UE55sXty-F1KN-7TUVsffEC495zmtwrSFhekUnhzCUPI62jkZsATmUQlvfxdgzJ7WKwOaeZcS2qvW-smR3C-Fjxn2gIebyNurKBLsZOvWVXl6ff0Cs3qNTW863pKRBQxpJjiPAp6hssPg4ha-XR4CZn-wVhoWj5LMcY8AmALeGheJMyDRi3fQJI7rJm2HPCkip7RqHK3Ajre0SpMiUw9-juTtz4PnICI37iLYaZEiR028t34HldT4IC2ShNiXPxvKCiZWSc1yyp_IQ8jTP4t8RXtfykZOr7y7K8pMmGtDAIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7652e2bde8.mp4?token=rxQJRzmFWCVSmDNEcRmWZ1iIq8cUyBY-NUASUFbn1rbhcOfhoCi9psz5i5x3cFRojRMs-3gOLawOuhX3zctnG5T9jABWicGtVg5Q2URLVT4ZKMejRGTEP73g3ck58gZRtP79ZpYjmlnfP2cqnWlbIZ2GLoGRQs5WywU2acR6bOpcDKXAJ7OimxXW1gJyP03SmUaVflLfO7XGQVpOCXiWEzermGd9BqxfYKeBql5Hdvz07hgkJlNl2Fxn0b9NSVC3H0kZiQYH8g-NSQQOqHU15pbklJH5SAve8mzijgFTJdwk7e2NxZCGSkfPdnpVTalAOVPE67GMz5mFFNg96JRn96xA5coaYKI6-SuCiUFIBrZhhfEECAUg0iI-UzXcaC4UE55sXty-F1KN-7TUVsffEC495zmtwrSFhekUnhzCUPI62jkZsATmUQlvfxdgzJ7WKwOaeZcS2qvW-smR3C-Fjxn2gIebyNurKBLsZOvWVXl6ff0Cs3qNTW863pKRBQxpJjiPAp6hssPg4ha-XR4CZn-wVhoWj5LMcY8AmALeGheJMyDRi3fQJI7rJm2HPCkip7RqHK3Ajre0SpMiUw9-juTtz4PnICI37iLYaZEiR028t34HldT4IC2ShNiXPxvKCiZWSc1yyp_IQ8jTP4t8RXtfykZOr7y7K8pMmGtDAIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: سنطرح الملف النووي وإلغاء الحظر في المرحلة النهائية من المفاوضات  إعلان نهاية الحرب أهم ما حدث في المرحلة الأولى من الاتفاق وتم إعلانه صباح الاثنين  جولة جديدة من المفاوضات بين أميركا وإيران ستبدأ في سويسرا يوم الجمعة  البدء الرسمي…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/78974" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني:
سنطرح الملف النووي وإلغاء الحظر في المرحلة النهائية من المفاوضات
إعلان نهاية الحرب أهم ما حدث في المرحلة الأولى من الاتفاق وتم إعلانه صباح الاثنين
جولة جديدة من المفاوضات بين أميركا وإيران ستبدأ في سويسرا يوم الجمعة
البدء الرسمي لتنفيذ مذكرة التفاهم سيكون يوم الجمعة
نهاية الحرب في لبنان موضوع ملزم لنهاية الحرب مع إيران
سنناقش الملف النووي والعقوبات خلال فترة المفاوضات التي تستمر 60 يوما مع واشنطن</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78973" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59974eb34.mp4?token=mRfP4XeHm3wN8WcW3YBRV75Mmu8Rua28545co5CJrbibCQN6xXGAIkuXupskxS9U7MwcBuCR9rbUintfIHIRd-Bp-NEDkDopbkG9OlviSwF2Pp7dFNBb8pNLQ4HivXW1cpigPVRr3B5uCubvYRhurgIg2P3TLzWFTy_h-UQm70PE5pBtlyI6YxSA6hT197-RJ4nIlD7gVZIdMTNmrbkbRr_DRYOdI0yQcgWxmJEoGpg35P8A6XwRmJ1KHyLIwwIlu845bwZ3hF_mz5Sjamzu5HGF43aX2mBzZFiepXGCEmaXx6i4s4GhlOi9uUjEIrrZZwLpuZko3EArQobhE5YhwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59974eb34.mp4?token=mRfP4XeHm3wN8WcW3YBRV75Mmu8Rua28545co5CJrbibCQN6xXGAIkuXupskxS9U7MwcBuCR9rbUintfIHIRd-Bp-NEDkDopbkG9OlviSwF2Pp7dFNBb8pNLQ4HivXW1cpigPVRr3B5uCubvYRhurgIg2P3TLzWFTy_h-UQm70PE5pBtlyI6YxSA6hT197-RJ4nIlD7gVZIdMTNmrbkbRr_DRYOdI0yQcgWxmJEoGpg35P8A6XwRmJ1KHyLIwwIlu845bwZ3hF_mz5Sjamzu5HGF43aX2mBzZFiepXGCEmaXx6i4s4GhlOi9uUjEIrrZZwLpuZko3EArQobhE5YhwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇮🇱
الجيش الأمريكي يبدأ بإجلاء طائرات التزود بالوقود المتمركزة في مطار بن غوريون حيث تمثل حوالي 20% من الطائرات المتواجدة حالياً في الكيان.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78972" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
