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
<img src="https://cdn4.telesco.pe/file/nJFPETt4V-tlikbppDGwPyo3_wUZnKOsTg6Qwd5QFod1QcAuGI2EIAghdrDNxHwazAY7Cwv2tYFELhjJckSKBN-L-jf0Fto81wMkB7hj_mwhqPapZmclXaP5vGNIyR14AkL03qNFEAVMkV2pMppapd3KJBollLRakJSATCmo7xu-v1VAd8fKdoUXhiLGMYOPAvKElnKX1PPIBYTeqJi5q6sffcF8cRM4ASoasZZWd9ICcfF4ZPlzxNPR4d2vCBLu_eR55Myp5T7Ce8W6mYn5iJ1amIYSh-fRXgy3cp44H13e1I9Q61pL5CcbFpbHtGlXyccCarLS1WBKhZItgVIGCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 11:07:02</div>
<hr>

<div class="tg-post" id="msg-76109">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">إعلام العدو : بدأت إسرائيل تعبئة احتياطية طارئة، بما في ذلك قوات المدفعية التي تم تسريحها مؤخراً من الخدمة، مع تزايد الاستعدادات لعمليات دفاعية موسعة في لبنان وسط استمرار هجمات حزب الله وانتهاكات وقف إطلاق النار</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/naya_foriraq/76109" target="_blank">📅 10:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76108">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_رهبر_انقلاب_اسلامی_به_مناسبت_برگزاری_حج.pdf</div>
  <div class="tg-doc-extra">415.4 KB</div>
</div>
<a href="https://t.me/naya_foriraq/76108" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">النص الكامل لرسالة قائد الثورة الإسلامية بمناسبة موسم الحج | 5 خرداد 1405</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/naya_foriraq/76108" target="_blank">📅 10:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الجيش الإسرائيلي: لم نشارك في الضربات ضد إيران إلى جانب الولايات المتحدة.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/naya_foriraq/76107" target="_blank">📅 10:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭐️
هجوم بالطيران المسير الانتحاري وعدة صواريخ يستهدف مقر تابع للمعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/naya_foriraq/76106" target="_blank">📅 10:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📰
‏القناة 12 الصهيونية عن مصادر:  مجتبى خامنئي لم يصادق بعد على التفاهمات المتبلورة</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/naya_foriraq/76105" target="_blank">📅 10:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76104">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO5k7mXLMtKNjp4q_61SAnyhILI-RZaitHfKjrb89nv2eXkO2MkMmy_AXHe6_BOu4Rsu8A2Xbxc4DzmI7NC25VEdK6DGvVHz12dshL18r1AIBfGDOVVxbSijAE5d6BImx7DulkWdXuzBD_2CRsDOww6hQlMKAnpyWr9FIpP0Oqxz4IpxuoeBKWqS8b2FDvebvSVncP6FIJWPdfUTN4xFDoPJMgFyfdO-4uR1-_Eoky6nKtHlzsXtd93ItNPBHOP82KUHkeRvtcvp3LD0PN0sdb3W0YdnGU9N8ySMkK2oY9RaVqutYwKK5XBBQOg5YdNzefaSYaWQBwftT4vML2yacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني في الشارع الرئيسي بمدينة العفولة نتيجة انفجار سيارة ووجود جريح في موقع الحادث.</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/naya_foriraq/76104" target="_blank">📅 09:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴‍☠️
انفجارات داخل مستوطنة بيرنيت شمال الكيان نتيجة هجوم بمسيرات حزب الله.</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/naya_foriraq/76103" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76102">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي: إيران حاولت مهاجمة القوات الأمريكية على مدى الساعات الـ٢٤ الماضية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76102" target="_blank">📅 02:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76101">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
إيران حاولت مهاجمة القوات الأمريكية على مدى الساعات الـ٢٤ الماضية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76101" target="_blank">📅 02:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76100">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: ‏القوات الأمريكية تصيب أهدافاً تشمل إطلاق صواريخ و‏مواقع وسفن إيرانية تحاول زرع ألغام.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76100" target="_blank">📅 02:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76099">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: نفذت القوات الأمريكية ضربات دفاعية في جنوب إيران يوم الاثنين.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76099" target="_blank">📅 02:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76098">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76098" target="_blank">📅 02:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76097">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مصدر إيراني:
ماتم تدوله حول تفعيل الدفاعات الجوية في مدينة قم المقدسة لا صحة له.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/76097" target="_blank">📅 01:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76096">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نقل النتن ياهو لمستشفى في القدس</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/76096" target="_blank">📅 01:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76095">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تفعيل الدفاعات الجوية في بندرعباس.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/76095" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76094">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03326bd1d2.mp4?token=Jki8pj0MBzgGhFgGvAqkbGfBn23ABRazQlHgrCIzbKbALaJgjYcuwdTyKhA5R9-6D-bYrv4e3RmtKsvrf5HLkqvt5rGEYT9g826Ey0woTi7d5IHW5gQ_DiSENUptpzHBCBTHof24F8xMUZSdnXhVrdDcf11FoZIy6l6TsYqiK9iXGSAwvawZJgTIAUIWLAJ7WHBtiv5ZejlHTpfKlzZO5qU3aLVcNjXzZMk-obuwpx22mJwf-EqMPmjYqGjQFV_7rVVSsiMQOPQzOMKYbbYuezihJRoIvYIa1Nk-eb-OJDdBKf0AmqUG4VAmKuay02FF4gaCJjQQ4LYi2mbsQAMKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03326bd1d2.mp4?token=Jki8pj0MBzgGhFgGvAqkbGfBn23ABRazQlHgrCIzbKbALaJgjYcuwdTyKhA5R9-6D-bYrv4e3RmtKsvrf5HLkqvt5rGEYT9g826Ey0woTi7d5IHW5gQ_DiSENUptpzHBCBTHof24F8xMUZSdnXhVrdDcf11FoZIy6l6TsYqiK9iXGSAwvawZJgTIAUIWLAJ7WHBtiv5ZejlHTpfKlzZO5qU3aLVcNjXzZMk-obuwpx22mJwf-EqMPmjYqGjQFV_7rVVSsiMQOPQzOMKYbbYuezihJRoIvYIa1Nk-eb-OJDdBKf0AmqUG4VAmKuay02FF4gaCJjQQ4LYi2mbsQAMKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇬🇧
السفير البريطاني في بغداد : الأمريكان لم يعلموا أن السيد الخامنئي مرجع شيعي وأفهم تعاطف الشيعة</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/76094" target="_blank">📅 01:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76093">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نقل النتن ياهو لمستشفى في القدس</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/76093" target="_blank">📅 01:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76092">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGmFeJPzPDyPP0FzEEsn5DX2eMQsxMVEQJDr3tzbdSbnv1hk7YaE1ju_AaZ-1BR6dcB96pegz5N-nuNkIHgoTXS5h35k7TekaKulMvKwzA0hjGcENdVJ4GY99SSP3dHNsyQdEY0R4l6MllKkI04JRbSVp3qWZn6oWsIOJzWxVaQoycJaYss-FWX3zxgYLORA2Ps3_XQL6FVoKl59uC6he4iDReT4w9H0CPcASf53TlFFI1ukcpnxfWtl4rhI_tAxy0FmDNGgJbHyptTs5UbxiXXTdX6gsL5xdkKeYJYEL-7g_701z-00LSsZVxHWLLy83fF0pnfJoRfOlyGZG_qeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
سيتم تسليم اليورانيوم المُثري (الغبار النووي!) فورًا إلى الولايات المتحدة لإعادته إلى الوطن وتدميره، أو، من الأفضل، بالتعاون والتنسيق مع جمهورية إيران الإسلامية، تدميره في المكان أو في موقع مقبول آخر، مع لجنة الطاقة الذرية، أو ما يعادلها، كشاهد على هذه العملية والحدث. شكرًا لكم على اهتمامكم بهذه المسألة!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76092" target="_blank">📅 01:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76091">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76091" target="_blank">📅 01:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76090">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هجوم صهيوأمريكي طال عدد من القوارب في جزيرة لارك جنوبي إيران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/76090" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هجوم صهيوأمريكي طال عدد من القوارب في جزيرة لارك جنوبي إيران</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/76089" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76088">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76088" target="_blank">📅 01:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76087">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76087" target="_blank">📅 00:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76086">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6e89360b.mp4?token=QybNEY3dIR-DMSZPq_a0PzRhg0z5EGYqKlmcgdHzga5IYTbJn-12H9Ut5wGPUtuCvstsFRgHmLfr58tkntLvOFBEnk3JmqOsH4swkv8hWqrne0jj6KsOmPoJmg9GWycmk_sJYzULpeG0A-jfOUiP0hQ2WUdMC3TYI1il8dcuZQEBt7CA7pQeKUCTCuGXoLtAGdCGOplM9MgT-aZzvd7PiCjiQsJBH9EFLY3UtKQJsnOoi4QW4armE93kknhf-JEA3_lfmnFdSjO4g-9tsSngW6d8LBOabfVrC5s5HfyfoVyJ4OhJL4pAKng1ftZ-cABDVPmk2UoX13TkJlhLmZzaFQkMQ2AepefeWLUzvMF-HWxEATpWO9LnXXfE5fTXtYIwAKB4053I11gN4R9W7OtJ8kxb9MaojVZ5yd2XVxqicEakWUXzD42UPB55F5OiZm_ARDKxbk7EL15OpHUKwYnQzX4UY8S04f4yKRFoiu9wpjGCRmFPrzKzMwfhoRxijW_jA5oRQE_FuwuKkTCRl1nI1F3yYNvR7JQGsZ5e6gkQXg6SawHI7UObdWLX_b363kmo_-xxM9-hmr0jbRRx-VQQLmkgmsWn0LOhkj42AEDXYULXFs6StsRpEDjArFidGVAPmgDtHzPNStydkcYM8msgasnl1BfgTJhrsCEu-VssOFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6e89360b.mp4?token=QybNEY3dIR-DMSZPq_a0PzRhg0z5EGYqKlmcgdHzga5IYTbJn-12H9Ut5wGPUtuCvstsFRgHmLfr58tkntLvOFBEnk3JmqOsH4swkv8hWqrne0jj6KsOmPoJmg9GWycmk_sJYzULpeG0A-jfOUiP0hQ2WUdMC3TYI1il8dcuZQEBt7CA7pQeKUCTCuGXoLtAGdCGOplM9MgT-aZzvd7PiCjiQsJBH9EFLY3UtKQJsnOoi4QW4armE93kknhf-JEA3_lfmnFdSjO4g-9tsSngW6d8LBOabfVrC5s5HfyfoVyJ4OhJL4pAKng1ftZ-cABDVPmk2UoX13TkJlhLmZzaFQkMQ2AepefeWLUzvMF-HWxEATpWO9LnXXfE5fTXtYIwAKB4053I11gN4R9W7OtJ8kxb9MaojVZ5yd2XVxqicEakWUXzD42UPB55F5OiZm_ARDKxbk7EL15OpHUKwYnQzX4UY8S04f4yKRFoiu9wpjGCRmFPrzKzMwfhoRxijW_jA5oRQE_FuwuKkTCRl1nI1F3yYNvR7JQGsZ5e6gkQXg6SawHI7UObdWLX_b363kmo_-xxM9-hmr0jbRRx-VQQLmkgmsWn0LOhkj42AEDXYULXFs6StsRpEDjArFidGVAPmgDtHzPNStydkcYM8msgasnl1BfgTJhrsCEu-VssOFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇬🇧
السفير البريطاني في بغداد : الأمريكان لم يعلموا أن السيد الخامنئي مرجع شيعي وأفهم تعاطف الشيعة</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/76086" target="_blank">📅 00:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏴‍☠️
إعلام العدو : انتحار جنديين اثنين هذا اليوم ، أحدهما في معسكر للتدريب.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76085" target="_blank">📅 00:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اصوات انفجارات سمعت في الخليج الفارسي قبالة سيريك وجاسك</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/76084" target="_blank">📅 00:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76083">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76083" target="_blank">📅 00:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⭐️
الإعلام الإيراني:
دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/76082" target="_blank">📅 23:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76081">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
مصدر عسكري إيراني:
التحقيقات الفنية تؤكد هجومًا إسرائيليًا بطائرة مسيرة على الإمارات.
تُظهر التحقيقات الفنية التي أجرتها القوات المسلحة أن إسرائيل نفّذت عدة هجمات بطائرات مسيرة خلال الأسابيع القليلة الماضية في عملية "علم زائف" ضد الإمارات. أن هذا العمل الإسرائيلي جاء "لاستفزاز" الإماراتيين. لقد أظهر الكيان الصهيوني أنه لا يُفكّر إلا في مصالحه الخاصة، حيث يتواصل مع بعض دول الخليج، فيجرّها إلى هاوية خطيرة، وفي الوقت نفسه يشنّ عمليات ضدها.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76081" target="_blank">📅 23:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
إبطال مفعول عبوة ناسفة في منطقة حزام بغداد بالعاصمة العراقية " جسر الرفرش " ؛ المنطقة نشطت بها خلايا عصابات داعش أعوام ٢٠١٣ - ٢٠١٦ .</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76080" target="_blank">📅 23:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق صواريخ دفاع جوي من جنوب لبنان نحو طائرات حربية إسرائيلية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76079" target="_blank">📅 23:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
رئيس لجنة الأمن القومي في البرلمان الإيراني:
ما لم تتخذ الولايات المتحدة خمسة إجراءات لبناء الثقة، فلا جدوى من التفاهم والتفاوض معها. وتشمل هذه الإجراءات ما يلي:
▪️
إنهاء الحرب على جميع الجبهات، وخاصة لبنان
▪️
رفع الحصار الأمريكي ومكافحة القرصنة
▪️
السماح بمرور السفن المدنية عبر مضيق هرمز بتنسيق إيراني
▪️
تعليق العقوبات النفطية لمدة 30 أو 60 يومًا
▪️
الإفراج عن الأموال الإيرانية المجمدة</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/76078" target="_blank">📅 23:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc8092e1.mp4?token=bhmRyXVZMWwclJAKRHOCC5yifU3hzeXh6PE0jk_nSOpFW_nIVlaCoT9yjEi1u5JSx5Cg-sSKQHxJhBlzlLtC2LNixHDwY3p2ikO7TVTuCGARSp31LRuBhrHfN8_i_-6kbDxqZp3A9CauxUuBhoa_lr1VF7II4s0_5orRMQg6YlmxcxuVLFHMq66_PfSXpXVe24XOm4B75AgTzeq5StvKtg1X3p6qE9MdwSVs1Ris6WnWujAUri82iTVjb65j9XrX-duZopgZ0OjubW8vnvhJmzcEZ6CQeJ4wUzbkvQl5fMkqvT5SyIRtFpIyabIAg2FgJpJ9LlF2HUVCbACsMabLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc8092e1.mp4?token=bhmRyXVZMWwclJAKRHOCC5yifU3hzeXh6PE0jk_nSOpFW_nIVlaCoT9yjEi1u5JSx5Cg-sSKQHxJhBlzlLtC2LNixHDwY3p2ikO7TVTuCGARSp31LRuBhrHfN8_i_-6kbDxqZp3A9CauxUuBhoa_lr1VF7II4s0_5orRMQg6YlmxcxuVLFHMq66_PfSXpXVe24XOm4B75AgTzeq5StvKtg1X3p6qE9MdwSVs1Ris6WnWujAUri82iTVjb65j9XrX-duZopgZ0OjubW8vnvhJmzcEZ6CQeJ4wUzbkvQl5fMkqvT5SyIRtFpIyabIAg2FgJpJ9LlF2HUVCbACsMabLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
هجوم بالطيران المسير الانتحاري وعدة صواريخ يستهدف مقر تابع للمعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/76077" target="_blank">📅 22:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تخشى "إسرائيل" من إطلاق حزب الله النار على الشمال، في أعقاب الهجمات الكبيرة التي يخطط لها الجيش الإسرائيلي في لبنان.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76076" target="_blank">📅 22:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac03e8b15.mp4?token=qItn6sf8Nq1qz-YW28xl99BFgrzTzdGNvcetHaIkzsCirGlhPbI-A3WirHuIhar0BqewEfwazxVLghzBErQIOUDML901ZihSsOjMvRIcOCYL4s-YPGV03g1azkI8Vdn9AI-W2jccJKzR-7E-nQuyEdaHdbofKBS0uA_CjN8sao7EtYSUBDtlyM_vqTKLnWeGEEuG7NPeJ4YEY2GUsa15c3B3FMTVbOq7w6X0Edf_vMX3pdrCs27sz-6jjrNKbTp5c0wA3IZw7ViF5d96Z-ST2kuqYWv68PFnPpLwN36MQvnx2L4SzSxrCqhORwtuce1jlCdGq4YSg7_OSu1MoIxUWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac03e8b15.mp4?token=qItn6sf8Nq1qz-YW28xl99BFgrzTzdGNvcetHaIkzsCirGlhPbI-A3WirHuIhar0BqewEfwazxVLghzBErQIOUDML901ZihSsOjMvRIcOCYL4s-YPGV03g1azkI8Vdn9AI-W2jccJKzR-7E-nQuyEdaHdbofKBS0uA_CjN8sao7EtYSUBDtlyM_vqTKLnWeGEEuG7NPeJ4YEY2GUsa15c3B3FMTVbOq7w6X0Edf_vMX3pdrCs27sz-6jjrNKbTp5c0wA3IZw7ViF5d96Z-ST2kuqYWv68PFnPpLwN36MQvnx2L4SzSxrCqhORwtuce1jlCdGq4YSg7_OSu1MoIxUWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
وكما قال الشهيد الأقدس:
بتوسّع منوسّع...بتعلّي منعلّي</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76075" target="_blank">📅 22:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76074">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🤙
🔥
الخارجية الروسية : على الجاليات الأجنبية مغادرة كييف فورا</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76074" target="_blank">📅 22:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76073">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0cJsR07UNFKOHdKSfbyMzLphT8lh7osjIJF11vfoGkilGliVPTyu9fB2obNDTtRt3UfoQY1c4z9uIuOpySAYcAMGfkMOONO7GH__oLdWHycuCuwaUsdr1JKKn9qqG5HRMXXpCeeNrQejv-p4j_T12qmfY7esh_C7oukO4PbX3PvT4CcqaqzcgbCNzMKHyNgtnGLnOGxCD4GsdZg06V4-4OxT5CqJIgmTmkCzxPImJoLDDDCaZRfWmF4ywk5erP-vaSZ2XOzOBJ4UE7WMt4h9Rxc26hmq82mNR5h04FXFY_VLgZ_dZjJhisImWlj8r6MmUqvcXdy1wl8knUb7X-FCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو يطلق حملة تبرعات للجنود والعوائل المهجرة في شمال فلسطين المحتلة بسبب ضربات حزب الله.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76073" target="_blank">📅 22:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126245a760.mp4?token=UDvNdZp6Bh7l7iioQeygIu-3rjjZGYbQ7N5cgNaeUZVKNw6QDTVbWj8dw6lfAysJa9O4-itXOLG16Bg-1vFhbJ-ckwNj26qCKaDhDSBBJUtXzke6qEjkR9pqNquczY2C61UUHxfIyrje9tXCSkNyHLJAB40gRji8P1jjq56joACjI9RjYDNfd2yBeQ5AZXt1NbZ5fKy0TiAokL3s-F4ghgT5DlYXmg3IDCV3NF5SA5g1afrOBbTnOa0hkHDCs65wc7EEC78jc3t0riJeVNuKfBZLKSIjD51_kUghpRtjBeAmKmDv-GeozeYAOAR_S_N4tIuxTJSm2c26bVOmuoP6u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126245a760.mp4?token=UDvNdZp6Bh7l7iioQeygIu-3rjjZGYbQ7N5cgNaeUZVKNw6QDTVbWj8dw6lfAysJa9O4-itXOLG16Bg-1vFhbJ-ckwNj26qCKaDhDSBBJUtXzke6qEjkR9pqNquczY2C61UUHxfIyrje9tXCSkNyHLJAB40gRji8P1jjq56joACjI9RjYDNfd2yBeQ5AZXt1NbZ5fKy0TiAokL3s-F4ghgT5DlYXmg3IDCV3NF5SA5g1afrOBbTnOa0hkHDCs65wc7EEC78jc3t0riJeVNuKfBZLKSIjD51_kUghpRtjBeAmKmDv-GeozeYAOAR_S_N4tIuxTJSm2c26bVOmuoP6u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أعدّ الجيش الإسرائيلي خطة واسعة النطاق وهامة تنتظر موافقة القيادة السياسية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76072" target="_blank">📅 21:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أعدّ الجيش الإسرائيلي خطة واسعة النطاق وهامة تنتظر موافقة القيادة السياسية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76071" target="_blank">📅 21:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76070">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
استطلاع رأي أجرته القناة 13 العبرية:
يعتقد 58% أن الاتفاق المُبرم مع إيران، وفقًا لما نُشر، يضر "بإسرائيل". ويعارض 51% هذا الاتفاق. ويرى 39% أن الوضع الأمني ​​"لإسرائيل" لم يتغير بسبب الحرب، بينما يرى 34% أنه ازداد سوءًا. ويؤيد 49% استمرار الحرب في الشمال.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76070" target="_blank">📅 21:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76069">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
أعدّ الجيش الإسرائيلي خطة واسعة النطاق وهامة تنتظر موافقة القيادة السياسية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76069" target="_blank">📅 20:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76068">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f73557bac.mp4?token=lYrM7xV0n0CyGzFkhXiqtwFabKDi7NNZtJv8dkBGaJ__1_a5tgdBOyAwA0EmHcLcjXT3Qa6WCvN5f29tmnlsVG6dG8E7wVKegSvbcW87GB1zM8SvBOAaSd9YAbiWE8uSaphfiOk0WdQlr-OzSU_T8fEILoFDLuuyvwO2HISniyd8v11HTkfvYCy-kxE2uileB-Bn_GpoHwi1DNVtV6BdhN_jqytBJ3yHiDNH113ddceiFSuSHAeYNjm5OJ6PffaYH0FBzopbifgGTZj5rZg9g5GirItYAPTwOAOBdZon-0rsTs1-YzgPsCIV0Lv9nintaHJ8ZRsEg_ZFLB4QdgnY0mg4bi42NAzcWwrOEUfSmAcAX3HuVr16gDxhPXlZLwAgva9KXGi4R82K8hWmXGd2wD_Iv627Z6yq0zsyeNQ6l83kpdy0QspWHGwzBZIDB-jWMBm6-iWyG-AwDmKLIqxpTzH5tD5xo7y-WAVsMKziBDcztQ_7D72nvY5yy46ucmD7wXNE4LnFRlY4PLurjZr8Pqmh1nzOhX0uve7bFc6H4FVO-mxdb7bPvqSHNKwyqmWIKhXRjQvFnGfDTNaDk-w_Sd5Oaf-gXH2-SZH6y64Io_rQlrCLGUcBzwkALwt7IB9vwZqeIQ3tjh2OVKoDyVfeMTkIm5H-QAXS4YBWpPrzTIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f73557bac.mp4?token=lYrM7xV0n0CyGzFkhXiqtwFabKDi7NNZtJv8dkBGaJ__1_a5tgdBOyAwA0EmHcLcjXT3Qa6WCvN5f29tmnlsVG6dG8E7wVKegSvbcW87GB1zM8SvBOAaSd9YAbiWE8uSaphfiOk0WdQlr-OzSU_T8fEILoFDLuuyvwO2HISniyd8v11HTkfvYCy-kxE2uileB-Bn_GpoHwi1DNVtV6BdhN_jqytBJ3yHiDNH113ddceiFSuSHAeYNjm5OJ6PffaYH0FBzopbifgGTZj5rZg9g5GirItYAPTwOAOBdZon-0rsTs1-YzgPsCIV0Lv9nintaHJ8ZRsEg_ZFLB4QdgnY0mg4bi42NAzcWwrOEUfSmAcAX3HuVr16gDxhPXlZLwAgva9KXGi4R82K8hWmXGd2wD_Iv627Z6yq0zsyeNQ6l83kpdy0QspWHGwzBZIDB-jWMBm6-iWyG-AwDmKLIqxpTzH5tD5xo7y-WAVsMKziBDcztQ_7D72nvY5yy46ucmD7wXNE4LnFRlY4PLurjZr8Pqmh1nzOhX0uve7bFc6H4FVO-mxdb7bPvqSHNKwyqmWIKhXRjQvFnGfDTNaDk-w_Sd5Oaf-gXH2-SZH6y64Io_rQlrCLGUcBzwkALwt7IB9vwZqeIQ3tjh2OVKoDyVfeMTkIm5H-QAXS4YBWpPrzTIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
فقدنا في عملية الغضب الملحمي 13 جنديا لضمان ألا تحصل الدولة الأولى الراعية للإرهاب على سلاح نووي.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76068" target="_blank">📅 20:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76067">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭐️
رويترز:
تمديد وقف إطلاق النار المتفق عليه بين الولايات المتحدة وإيران في أوائل أبريل 60 يومًا.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76067" target="_blank">📅 20:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76066">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
رئيس مجلس تنسيق الدعاية الإسلامية في طهران:
لم يتم بعد تحديد وقت محدد لتشييع سيد شهداء الثورة الإسلامية سماحة آية الله السيد علي الخامنئي ويجب على الناس عدم الانتباه للشائعات.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76066" target="_blank">📅 20:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76065">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
خبر الإعلام السعودي حول تفاصيل تفاهم وإتفاق محتمل كاذب وغير صحيح. أن هذا الخبر في الإعلامي السعودي، مثل العديد من أخبارها حول تفاصيل المفاوضات، كاذب ويأتي في إطار العمليات النفسية الأمريكية.
في نص التفاهم الموجود حتى اليوم، لا توجد أي جملة تفيد الاستعداد لنقل المواد النووية، وبشكل أساسي لم تقدم إيران أي التزام بشأن الإجراءات النووية في هذا التفاهم.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76065" target="_blank">📅 20:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9c91c53a.mp4?token=Qy8LlDs_n4m1H-3UECucy_PTiS7yrTlxZ4RdRONEOH5y93BtEmqVLOa_J1EbZ8dJtxBgz1guuqwqtn8pWUPHeWozDKMd_cO7nknLbtnHPlGBThY-hmgVKZR82dtWRG2SVcplvP8vaOwGOUO9nYOl8HqX5m0R3QyZ0pdEM0cGht2o6kVlrtU6ctNl56TCILGJtqk3qr0z8JN4UUDBjrJr2WUKcom-4iYWDx7fgsDia9jLfvc_X0hQf2gQnYCWkJ3jhpqMBsN_cVXCC967ZdWX9mGMj1y6ZRZdIru4RLO-R820A4vodn5tk_E-vPc5YjRb9WpJA-PvAAZk90x_GGG5LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9c91c53a.mp4?token=Qy8LlDs_n4m1H-3UECucy_PTiS7yrTlxZ4RdRONEOH5y93BtEmqVLOa_J1EbZ8dJtxBgz1guuqwqtn8pWUPHeWozDKMd_cO7nknLbtnHPlGBThY-hmgVKZR82dtWRG2SVcplvP8vaOwGOUO9nYOl8HqX5m0R3QyZ0pdEM0cGht2o6kVlrtU6ctNl56TCILGJtqk3qr0z8JN4UUDBjrJr2WUKcom-4iYWDx7fgsDia9jLfvc_X0hQf2gQnYCWkJ3jhpqMBsN_cVXCC967ZdWX9mGMj1y6ZRZdIru4RLO-R820A4vodn5tk_E-vPc5YjRb9WpJA-PvAAZk90x_GGG5LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مسير يحلق في سماء قضاء سوران بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76064" target="_blank">📅 19:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cff5fa941.mp4?token=JBTQUybF1GdMjSzAuV-bsDqPjL40ERzif3dF_-9RdasntRyKtOvsoPe3j7kOZqdRNopkasV9w7HCEh3D7TqZN3SHobl-BeaWimMWnEPl-3Qaw5nzgdAa9mz5sgrxn8ybGa9eFSkDDP9AlrKAMcX4aWAUjLcrOOcZ1nRQ5DU2Qp2pCy6Fpm4TEYhneP1SQL0WQatv75fHNu8zyHsN8EyirvZzDlobQO7GXdf69Xfh3Hi5GEIj-MK3QpeWgxNud2xy6FByJBW3p7ZQUHrX9F6LTa-xjo4PU_KQRzn4c2hczu1VM_H77TtYSlmXu0fe9mR2zJWj20nQg-W7vnbtUg2AY0PO0RxpnQLrWJzXHu0nzB8W-JhAP9LelqVDsj-0LW7RFeTVerwaa_zry7VqvxUfXA_Plc5UIrTaCTE7bR_gJHFRjRheZJgu0Tupws95eg-w_0hszNZK6PQXyDI1DDaHUKHcrnqzlAmvG-_9Q1wFmDOnWGPukdsEw6hmQFUXvITuS0FLe7dA3bA7SQDV0bC0E1bMWu9vcpaSlrYdMSraMw9f5b47JLUoqOTD_HXYD01iOkwh0oeThtpAgSglCo1JjDcQhDj1IbaIUL7er4JJPfEOuFrjqaB970KzcQVChE2L-QkzC8ad7QA-eGC37lYUUM-usznpgHYUPutizVBvM6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cff5fa941.mp4?token=JBTQUybF1GdMjSzAuV-bsDqPjL40ERzif3dF_-9RdasntRyKtOvsoPe3j7kOZqdRNopkasV9w7HCEh3D7TqZN3SHobl-BeaWimMWnEPl-3Qaw5nzgdAa9mz5sgrxn8ybGa9eFSkDDP9AlrKAMcX4aWAUjLcrOOcZ1nRQ5DU2Qp2pCy6Fpm4TEYhneP1SQL0WQatv75fHNu8zyHsN8EyirvZzDlobQO7GXdf69Xfh3Hi5GEIj-MK3QpeWgxNud2xy6FByJBW3p7ZQUHrX9F6LTa-xjo4PU_KQRzn4c2hczu1VM_H77TtYSlmXu0fe9mR2zJWj20nQg-W7vnbtUg2AY0PO0RxpnQLrWJzXHu0nzB8W-JhAP9LelqVDsj-0LW7RFeTVerwaa_zry7VqvxUfXA_Plc5UIrTaCTE7bR_gJHFRjRheZJgu0Tupws95eg-w_0hszNZK6PQXyDI1DDaHUKHcrnqzlAmvG-_9Q1wFmDOnWGPukdsEw6hmQFUXvITuS0FLe7dA3bA7SQDV0bC0E1bMWu9vcpaSlrYdMSraMw9f5b47JLUoqOTD_HXYD01iOkwh0oeThtpAgSglCo1JjDcQhDj1IbaIUL7er4JJPfEOuFrjqaB970KzcQVChE2L-QkzC8ad7QA-eGC37lYUUM-usznpgHYUPutizVBvM6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
19-05-2026
آلية عسكرية تابعة لجيش العدو الإسرائيلي في مستوطنة مسغاف عام شمال فلسطين المحتلة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76063" target="_blank">📅 19:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19805be467.mp4?token=EsGfk4UGSxUpleMGpe45n2l05VjmqZ5bzp0aGv8o1zmzEcXFyNSkU4fP1MeHRPI4j7qtplXV5y8u7bCqv6XD0aFsLSwjcmDkq2venSNMMDM5xTwXFYbOJUhhMMDDOMjyn4DN5SHR8M1h_elt7GqajuVzfmnB22Y_Gaaj2l3ObAo3oPg0nxpvM7z9svrZ6kXOiNU3cQNXZ-sSFy4U9Zn-CorF-Fg1BMAg7mI42o_oXJeW5sm5TOOvayRD8IduSOHLqR7OmPszUoJTiWBZ8STBh8qzjZ_NJefh5qwEZ8F1GOKtUVAkavXDVn2EsqJL1qwFArB-3Zqle4yWSAxC3DjaGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19805be467.mp4?token=EsGfk4UGSxUpleMGpe45n2l05VjmqZ5bzp0aGv8o1zmzEcXFyNSkU4fP1MeHRPI4j7qtplXV5y8u7bCqv6XD0aFsLSwjcmDkq2venSNMMDM5xTwXFYbOJUhhMMDDOMjyn4DN5SHR8M1h_elt7GqajuVzfmnB22Y_Gaaj2l3ObAo3oPg0nxpvM7z9svrZ6kXOiNU3cQNXZ-sSFy4U9Zn-CorF-Fg1BMAg7mI42o_oXJeW5sm5TOOvayRD8IduSOHLqR7OmPszUoJTiWBZ8STBh8qzjZ_NJefh5qwEZ8F1GOKtUVAkavXDVn2EsqJL1qwFArB-3Zqle4yWSAxC3DjaGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إنفجارات عنيفة وتصاعد اعمدة الدخان في رأس الناقورة بالشمال الفلسطيني المحتل عقب هجوم مزدوج لحزب الله بالصواريخ والمسيرات الأنقضاضية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76062" target="_blank">📅 19:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfe153a8f.mp4?token=aknc4laC9rFdXbR1GaZCk9Ct81pfcbGAxkMFwoHu1rct5dryw8JtpzOCPkt0au07guxb5RfQN0DZ-EWt4bnSsPs2Hfzou5MKLHqBZBRivSkWin3jAa9TkQiX7apAVSJMUpPRZJaxCGGTUW07veRQBWM2KNVSgVwO9HaBhcyTT28yRu0uB6JihoHDiEYTISX25d_IY4lfgFhN9b8uURBcToecIlZQ_Z9SV0NtEwq-TrSwKhACMFaLGNxCSRgBpEv35p6o7aBuT50A9d7IN01gpxFWy8HdCRZlNYhnEpAHTjz6efySA0Y3Egh3PX_6UZ2qVlc234QGBlmnCQoca5sW_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfe153a8f.mp4?token=aknc4laC9rFdXbR1GaZCk9Ct81pfcbGAxkMFwoHu1rct5dryw8JtpzOCPkt0au07guxb5RfQN0DZ-EWt4bnSsPs2Hfzou5MKLHqBZBRivSkWin3jAa9TkQiX7apAVSJMUpPRZJaxCGGTUW07veRQBWM2KNVSgVwO9HaBhcyTT28yRu0uB6JihoHDiEYTISX25d_IY4lfgFhN9b8uURBcToecIlZQ_Z9SV0NtEwq-TrSwKhACMFaLGNxCSRgBpEv35p6o7aBuT50A9d7IN01gpxFWy8HdCRZlNYhnEpAHTjz6efySA0Y3Egh3PX_6UZ2qVlc234QGBlmnCQoca5sW_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
عقب فيضان نهر الفرات..
حكومة الجولاني تدعو لإخلاء فوري للمنازل والمحال القريبة من نهر الفرات في محافظتي دير الزور والرقة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76061" target="_blank">📅 19:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3c4d237e.mp4?token=pFCR53UBSLbr3dsJHhBtWHjGYQBDHAvLgLWly2qdlj_n9r5Nvyo8cEzs-OEdVsed-O5fy2Dw6NkPrJKXfrQyNIkN1mmfGBgBlEV7iAVoxgxr3JRdd_YQwzSy-1ZV7HYtNnVRS6mZD6dXUzWydhUc3HRON-64C8riyw3U7941W9rT31SCtnM6irCrDbENmwfcFps0EmDdTF1eqNVlgxI9tLDobvuUf2IfGBJDCUcN0QlKiBTVt2-7BZB2sOcWL8tFglmTlwpiXD5_FMmc7ybv4jc2Wix8DeF4bpklLHSlB6BRppHMgbaRl6zONZtr7lnHCXsLs8gZT6gEHXTaSxIw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3c4d237e.mp4?token=pFCR53UBSLbr3dsJHhBtWHjGYQBDHAvLgLWly2qdlj_n9r5Nvyo8cEzs-OEdVsed-O5fy2Dw6NkPrJKXfrQyNIkN1mmfGBgBlEV7iAVoxgxr3JRdd_YQwzSy-1ZV7HYtNnVRS6mZD6dXUzWydhUc3HRON-64C8riyw3U7941W9rT31SCtnM6irCrDbENmwfcFps0EmDdTF1eqNVlgxI9tLDobvuUf2IfGBJDCUcN0QlKiBTVt2-7BZB2sOcWL8tFglmTlwpiXD5_FMmc7ybv4jc2Wix8DeF4bpklLHSlB6BRppHMgbaRl6zONZtr7lnHCXsLs8gZT6gEHXTaSxIw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إنفجارات عنيفة وتصاعد اعمدة الدخان في رأس الناقورة بالشمال الفلسطيني المحتل عقب هجوم مزدوج لحزب الله بالصواريخ والمسيرات الأنقضاضية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76060" target="_blank">📅 19:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb0OZBg9JF6srU8dPo3MJx2bEnruj9Rp3vWUKo56T-mBNvbeKQjRbbJZB9-TzG4VgQYgAfD9gJO9lFdtfI9Ousj5R65YaUoE6lakn253wVW251X8-alaHxRSMj4dmqwd36AuDqOOppkWidNkbaBeYv9_-7Mv691YG5FelouXV4apmqxsO4vyCn9m9lyFhMwN45KOZeHFp07HQwr2vZ6zkDtLVrFeH94EfERAmv_bkeOq-E5Tj0_voeSOlPict8NbjZuYHymf565rTaQ7N2oEdIJ2e9eSU0xET_u8w6j-aBNvDhZqPeOcYF9yMcwxkd-juVGKSDATfPN30SkciJzFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
أمين المجلس الأعلى للأمن القومي الأيراني:
"لن يكون هناك استسلام أو تراجع"
لقد أظهر الميدان العسكري، والميدان الدبلوماسي، والشعب في الشوارع هذا الأمر بمقاومتهم الشديدة، وأجبروا العدو على التراجع. الآن أكثر من أي وقت مضى، يحتاج الوطن إلى الوحدة والتضامن، حتى يخيب أمل الأمريكيين والصهاينة في هذا الشأن. ميدان الوحدة والتضامن ميدانٌ آخر في النضال. إن تضافر الجهود لمنع أي أقوال أو أفعال تُزعزع الوحدة سيقود إيران العزيزة إلى النصر النهائي، بإذن الله.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76059" target="_blank">📅 19:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76058">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ السبت 23-05-2026 تجمّع لجنود جيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76058" target="_blank">📅 18:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76057">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c703c1c6bd.mp4?token=q801P8fct-Q4O0okFakikBf9XeBCVf4RNNQs_rENCfUaGmxnWfR_7vhTboQ9TUcAoKVgO9X16iSWC9-H1cVORSsbm-bIvk6-CaXMZAM7Fy4VEBQPYeIBcoB4hS6CidqSDSFFN7jz6JWKsp1lIJrDaLBam-D08gUnA3dSgd8QTSrFvnWojC6hywnAzjHrbaIg4mpV5hmzxtCixvprakPRefAayTYVHD_bVt5XNjAbasrBr1aQijuqi4fLlFDZmp_Yg4Bsid1C_syudspbNd-gNMFrUO07ReZp4F3qZrvkblnqqdC4e8B7yImjKSW7nrxF3VBPjZok-J0xlgBIh2mFSQQCBOjkMfFejv3jHACwgl3xBxxVg-56cgGaubjof7Es0XmNIedcR6zev7GuTaAjX39coHXeOXS8uQJODgIxFfSHxTpo5XjVmDeFe4a7jf-XM2y2hO8g6Sl2pG2gzduhfpxHpaa0-_Ht4F0uUEgHpjUu2J7QfkshdticPOFqB5EATsVJ3v2oM33uAqdHMm4v_uNYVr7mZuMOQOlbxXA2iNwev4bjaH2yIdPrcttd9fsEqpz2TUN2XYRsBXK7bDTzyJqxxw3me_V76SJG8uSES8weMT2nnY6EuKJSO1dPZOqgENoemJYFAa6XcUQxpEYjijaDATJmIOuNAJi1XnoQaKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c703c1c6bd.mp4?token=q801P8fct-Q4O0okFakikBf9XeBCVf4RNNQs_rENCfUaGmxnWfR_7vhTboQ9TUcAoKVgO9X16iSWC9-H1cVORSsbm-bIvk6-CaXMZAM7Fy4VEBQPYeIBcoB4hS6CidqSDSFFN7jz6JWKsp1lIJrDaLBam-D08gUnA3dSgd8QTSrFvnWojC6hywnAzjHrbaIg4mpV5hmzxtCixvprakPRefAayTYVHD_bVt5XNjAbasrBr1aQijuqi4fLlFDZmp_Yg4Bsid1C_syudspbNd-gNMFrUO07ReZp4F3qZrvkblnqqdC4e8B7yImjKSW7nrxF3VBPjZok-J0xlgBIh2mFSQQCBOjkMfFejv3jHACwgl3xBxxVg-56cgGaubjof7Es0XmNIedcR6zev7GuTaAjX39coHXeOXS8uQJODgIxFfSHxTpo5XjVmDeFe4a7jf-XM2y2hO8g6Sl2pG2gzduhfpxHpaa0-_Ht4F0uUEgHpjUu2J7QfkshdticPOFqB5EATsVJ3v2oM33uAqdHMm4v_uNYVr7mZuMOQOlbxXA2iNwev4bjaH2yIdPrcttd9fsEqpz2TUN2XYRsBXK7bDTzyJqxxw3me_V76SJG8uSES8weMT2nnY6EuKJSO1dPZOqgENoemJYFAa6XcUQxpEYjijaDATJmIOuNAJi1XnoQaKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ السبت 23-05-2026 تجمّع لجنود جيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76057" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
‏
🌟
أعلنت الرئيسة المكسيكية شينباوم موافقة حكومتها على بقاء المنتخب الإيراني في المكسيك خلال كأس العالم، بعد رفض أمريكي لاستضافته.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76056" target="_blank">📅 18:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7x-2jwY1yvmkHb2x22aBoytGRcGXRJJoUipCCN4IzS-I21DtIGR0Xfd2WAf7lpyo-LbZ8dbNK8JYMrBceoEPE8xEO9suBDEmcB5SfjD04WbSrvReJmu4XlC93_M4QbqsAkMgDlU_gdrgNgNEtgzUvDbc4jmk7ajhsT1BY0kNLeIZ3Wobs3m_aq1YTegLei5VOEbnQk7keLoNCKM2GqCwdpVQB9hGCGlxVSZGXSuTKWTkcdDcCqEE3wDo3j1_LHK94vtYYwBFzwC0skhBdPMJqcmPn-SNORqawDnKutto75pobX79mpbpT9xYl9sUP1BlIgvsqSNpVhJqPaSissz5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله:
بعد قليل...
تركضلي تركضلي
😄</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76055" target="_blank">📅 18:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🐦
سي ان ان:
تقول المملكة العربية السعودية إنها لن تطبع العلاقات مع إسرائيل إلا إذا كان هناك مسار لا رجعة فيه نحو إقامة دولة فلسطينية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76054" target="_blank">📅 18:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
حزب الله ينشر:
وَكُلّ عيد مُقَاومَة وَأَنتُم في نَصر.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76053" target="_blank">📅 17:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76052">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇹🇷
🌟
السفير التركي في العراق:
166 مواطناً تركياً من المنتسبين لتنظيم داعش كانوا محتجزين داخل العراق، سيتم نقلهم قريباً إلى تركيا، في إطار ترتيبات تتعلق بإعادة الرعايا الأتراك من السجون العراقية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76052" target="_blank">📅 17:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76051">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🤙
🔥
الخارجية الروسية : على الجاليات الأجنبية مغادرة كييف فورا</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76051" target="_blank">📅 17:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76050">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🤙
🔥
الخارجية الروسية :
على الجاليات الأجنبية مغادرة كييف فورا</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76050" target="_blank">📅 17:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76049">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5TGvHDFv1b7pgKm_Ma6n_kLtldDYt3KM7Y1vreiYPOCKuNNePcczz_yWMSw3GlJ0LoD6jOaZxwwUNO0uvl8BtO_7rLSS5XfTyr9o494uU4vbhcDLuW76vVc_7BVQ2RQha8bdCAVSjdeNBl6VqLXeeC_PbF2cgq1wf3Xt_KJMq3-zvvYmCk5LUqvAELTqi7zjLD9cN_LixMlw7PKKHCn8HjYSlNW91NpU1U-9_IY7ZHz3kMi-Vc5tolAdxk8x0To0gy0APgXw9AnSU185WpFU0nFD6OkfNgExIUuMNmcN_7AoAqdgfq_q933Ekcf4iU4tHuCZTXE9E0t7BwfjXfksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الاعلام الاجنبي
:
بدأت إيران في إعادة بناء إنتاج صواريخها الباليستية خلال وقف إطلاق النار، بوتيرة أسرع مما توقعته المخابرات الإسرائيلية والأمريكية.
بينما شهد قائد القيادة المركزية للقوات الأمريكية، الأدميرال براد كوبر، أمام الكونغرس أن 90% من القاعدة الصناعية الدفاعية لإيران قد دُمّرت وستستغرق سنوات لإعادة بنائها، إلا أن المعلومات الاستخباراتية المحدثة تُظهر صورة أكثر تعقيدًا.
نجا حوالي ثلثي منصات إطلاق الصواريخ الإيرانية من الحرب سليمة، وتم نقلها خارج الأنفاق المغلقة.
تقوم إيران الآن بإنتاج صواريخ باليستية جديدة ومنصات إطلاق وأنظمة دفاع جوي في منشآت تحت أرضية مرتجلة باستخدام المكونات الباقية والمساعدة الروسية والأجزاء المهربة من الصين.
يقدر مسؤولو الدفاع الإسرائيليون أن إيران يمكنها إعادة بناء أسطول طائراتها بدون طيار في غضون أشهر وزيادة إنتاج الصواريخ في غضون عام، أو ربما أقل من ذلك.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76049" target="_blank">📅 16:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76048">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIT29PUHB5D4hmNTGc40E6is0yGhMxyuVrKWY7dfI3qo2mBnck8a0KvRv5P-e81cKxyo8hrqBXxIopX4m_1EQPd9DXaHz7TcwiItwAxm8bGzxnN-U-SfP7xuubOcJaZ5K2iwOhMuyFnvQPNouOC4STQrBrwwlAHQfKzzoB68W-kOEG6LZLNnSIdHVyCNmDgcJ8uTDTNfd8baPgxseO8xW5sVKWMaSHgIt0EmbpQdeuKU6sxp7E65NpIyotBFOsU1g2qvbqxsP7J9Hy1kNNatCvq8MkpksUzNeVdY_0Bh7HRy8sI3m6BKu6znmIC6PQivge6rYmx95LJplQtTVCofXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
:
المفاوضات مع الجمهورية الإسلامية الإيرانية تسير على نحو جيد! لن يكون هناك اتفاق شامل للجميع، أو لا اتفاق على الإطلاق - عودة إلى جبهة القتال وإطلاق النار، ولكن هذه المرة أكبر وأقوى من أي وقت مضى - ولا أحد يريد ذلك! خلال محادثاتي يوم السبت مع الرئيس محمد بن سلمان آل سعود، رئيس المملكة العربية السعودية، ومحمد بن زايد آل نهيان، رئيس دولة الإمارات العربية المتحدة، والأمير تميم بن حمد بن خليفة آل ثاني، ورئيس الوزراء محمد بن عبد الرحمن بن جاسم بن جبر آل ثاني، والوزير علي الذوادي، من قطر، والمشير سيد عاصم منير أحمد شاه، من باكستان، والرئيس رجب طيب أردوغان، من تركيا، والرئيس عبد الفتاح السيسي، من مصر، والملك عبد الله الثاني، ملك الأردن، والملك حمد بن عيسى آل خليفة، ملك البحرين، صرحتُ بأنه بعد كل الجهود التي بذلتها الولايات المتحدة لمحاولة حل هذه المعضلة المعقدة، يجب أن يكون من الإلزامي أن توقع جميع هذه الدول، كحد أدنى، في وقت واحد، على اتفاقيات أبراهام.  الدول التي نوقشت هي السعودية، والإمارات العربية المتحدة (عضو حالي!)، وقطر، وباكستان، وتركيا، ومصر، والأردن، والبحرين (عضو حالي!). قد يكون لدى دولة أو اثنتين سببٌ لعدم الانضمام، وهذا مقبول، لكن ينبغي أن تكون معظم الدول مستعدة وراغبة وقادرة على جعل هذا الاتفاق مع إيران حدثًا تاريخيًا بارزًا. لقد أثبتت اتفاقيات أبراهام، بالنسبة للدول المعنية (الإمارات العربية المتحدة، والبحرين، والمغرب، والسودان، وكازاخستان)، أنها بمثابة طفرة مالية واقتصادية واجتماعية، حتى في ظل هذه الظروف من الصراع والحرب، حيث لم تُبدِ الدول الأعضاء الحالية أي نية للانسحاب، أو حتى التوقف مؤقتًا. والسبب في ذلك هو أن اتفاقيات أبراهام كانت عظيمة بالنسبة لها، وستكون أفضل للجميع، وستجلب القوة والسلام الحقيقيين إلى الشرق الأوسط لأول مرة منذ 5000 عام. ستكون وثيقة تحظى باحترام لا مثيل له في العالم.  سيكون مستوى أهميتها ومكانتها لا مثيل له! يجب أن يبدأ ذلك بالتوقيع الفوري من قبل المملكة العربية السعودية وقطر، وعلى جميع الدول الأخرى أن تحذو حذوهما. إن لم يفعلوا، فلا ينبغي لهم أن يكونوا جزءًا من هذه الاتفاقية، لأن ذلك يُظهر سوء نية. لقد تحدثتُ إلى العديد من القادة العظام المذكورين أعلاه، وأكدوا لي أنهم سيتشرفون، بمجرد توقيع وثيقتنا، بانضمام الجمهورية الإسلامية الإيرانية إلى اتفاقيات إبراهيم. يا له من أمر مميز! ستكون هذه أهم اتفاقية توقعها أي من هذه الدول العظيمة، التي لطالما كانت في صراعات. لن يتجاوزها شيء في الماضي أو في المستقبل. لذلك، أطلب بشكل إلزامي من جميع الدول التوقيع فورًا على اتفاقيات إبراهيم، وإذا وقّعت إيران اتفاقيتها معي، بصفتي رئيسًا للولايات المتحدة الأمريكية، فسيكون شرفًا لي أن تكون جزءًا من هذا التحالف العالمي الفريد. سيصبح الشرق الأوسط موحدًا وقويًا ومزدهرًا اقتصاديًا، ربما لا مثيل له في أي منطقة أخرى في العالم!  بموجب هذه الرسالة، أطلب من ممثليّ البدء في عملية توقيع هذه الدول على اتفاقيات أبراهام التاريخية، وإتمامها بنجاح. شكرًا لاهتمامكم بهذا الأمر!
دونالد ج. ترامب
رئيس الولايات المتحدة الأمريكية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76048" target="_blank">📅 15:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76047">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
‏ رويترز: عراقجي وقاليباف في قطر.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76047" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
‏
رويترز
: عراقجي وقاليباف في قطر.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76046" target="_blank">📅 15:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76045">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من مراحل استطلاع واستهداف المقاومة الإسلامية للمربض المُستَحدَث التابع لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة وباقي الأسلحة المختلفة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76045" target="_blank">📅 15:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🌟
🇮🇷
واشنطن بوست:
المرحلة الأولى تشمل إزالة الألغام ورفع الحصار الأمريكي والإفراج عن 12 مليار دولار، مذكرة التفاهم لا تتضمن اتفاقا نوويا بل مجرد تعهد بالتفاوض على الملف النووي لاحقا.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76044" target="_blank">📅 14:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf43a827a.mp4?token=JcXG1boHfGdFgr20WpJRseJN6Psds4scVtwIbqfv3jb6XSKFH-7kzNutXXV-0eJHrvUdS9qOvQxUBGVGQV_fZbSq1QDxhVaZ_4qom_2XPiTEfC8hYAqtAFOMpln2iylrH_hrQZxDN293xEcJvDzBcdRu0Yu5EGBjx3f-8YiKp8YtRKG0wSgQF80X85AlBKaszcD_ChFeGv296qIj9u4UNXxItuYnu6R5YxtuVDh3-2qSmny1NMAFnWu6kCLGrQOcB5_qUxsOBdzIxh9AgURKFURjzdraJvsl72UQlNUQ2i2AYCPLho5n6fbPSlAdIcVhCSQmnik_o3HelMKwMaD8ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf43a827a.mp4?token=JcXG1boHfGdFgr20WpJRseJN6Psds4scVtwIbqfv3jb6XSKFH-7kzNutXXV-0eJHrvUdS9qOvQxUBGVGQV_fZbSq1QDxhVaZ_4qom_2XPiTEfC8hYAqtAFOMpln2iylrH_hrQZxDN293xEcJvDzBcdRu0Yu5EGBjx3f-8YiKp8YtRKG0wSgQF80X85AlBKaszcD_ChFeGv296qIj9u4UNXxItuYnu6R5YxtuVDh3-2qSmny1NMAFnWu6kCLGrQOcB5_qUxsOBdzIxh9AgURKFURjzdraJvsl72UQlNUQ2i2AYCPLho5n6fbPSlAdIcVhCSQmnik_o3HelMKwMaD8ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
تُظهر صور قبل وبعد لحيّ الشابورة وسط مدينة رفح، كيف مُحيت المنطقة بالكامل ، بفعل القصف العنيف والعمليات العسكرية التي شنّها العدو الصهيوني على المنطقة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76043" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mky8g2hjkn-OUpizMyZhCHbPc_QuqyPHupHxEpeCTweY5ARJ2vLSlHPdsOFWmHeKObyXJcYdtR2KGWB72zOttlD-CjeZnXXAmfToI-MhDB2Wa7DrczKf63UDuKtFwe1puAOjzMlygsUt5y7uJk41jys7JRVTa1NlTdCbOEYyi4Q5Y61pNSWx8B8f5w7tu2I0hpsih9QOEirLWD_TGSAJmuXtOkXHfiOzXE_otygah2o1NLGQpOolJePI7W4IEr_FYZrOHk0qsWIRZFvRGaELS8Y-uj5lE34TGMfh0cpTfv1Uci1uQBuNBbvZaYW7Y6-niNlwp71kaQRVUQSr1GzvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
أضحك على جميع الديمقراطيين، والجمهوريين المنشقين، والحمقى الذين لا يعرفون شيئًا عن الصفقة المحتملة التي أقوم بها مع إيران.
الصفقة مع إيران ستكون إما عظيمة ومفيدة، أو لن تكون هناك صفقة على الإطلاق.
ستكون عكس كارثة خطة العمل المشتركة التي تفاوضت عليها إدارة أوباما الفاشلة، والتي كانت طريقًا مباشرًا وصريحًا نحو حصول إيران على سلاح نووي.
لا، أنا لا أقوم بصفقات كهذه!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76042" target="_blank">📅 13:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09156df5ce.mp4?token=BAKPX-0oQZ73zqoPy4MQ_quDQl7iP0scMxkhqIhp5OFhKOUgSq2HKJlKqV5Kax4nHChms5dJS940ATRgUDauSG9Nz1p0b9BgSW2FLSvwSdsewg5qRcpqh9y7oKaGeABN0YQCu49YgNncwM5kGq5kbNGtMPt6kI_lhWxTBt6F93wX2IpWjCbMCmYTXdlNALS_oUg9q4BXMIyPQVfG3_-n9ic3XQU07klZ16Se68SyyxdxO92GsR2eeou8N7mZg7IMPhwj0tkmydW4hgH0lkLy5mVSO6mHIanvFzEN6Wdy-f0oFePjJq29STrSa3qk7tDsLgPGmTNa2f8ofpJxEysUIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09156df5ce.mp4?token=BAKPX-0oQZ73zqoPy4MQ_quDQl7iP0scMxkhqIhp5OFhKOUgSq2HKJlKqV5Kax4nHChms5dJS940ATRgUDauSG9Nz1p0b9BgSW2FLSvwSdsewg5qRcpqh9y7oKaGeABN0YQCu49YgNncwM5kGq5kbNGtMPt6kI_lhWxTBt6F93wX2IpWjCbMCmYTXdlNALS_oUg9q4BXMIyPQVfG3_-n9ic3XQU07klZ16Se68SyyxdxO92GsR2eeou8N7mZg7IMPhwj0tkmydW4hgH0lkLy5mVSO6mHIanvFzEN6Wdy-f0oFePjJq29STrSa3qk7tDsLgPGmTNa2f8ofpJxEysUIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الكيان المحتل جراء إطلاق مسيرات وصواريخ حزب الله</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76041" target="_blank">📅 13:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76040">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6BsZU_oMhP1dY9LbmyAFySbjlT1elh3NmFceE4UUju2Max_LFFvo-5__vyTgOX1Y080tboIkW7WwjyBQj3t9hg2ekUmLznW-893MH42pVAUP4jfLuDs5rsOLwXVlELsYXGf3PFnJ3U7CrS0BwXqvPHBqfDYUOBZ1kAlerdOGUGevcrx1VFvGReF9ASGOji2ZAa2Aluc0AUjm5YeTiC4TKXJToQNr12dD8B5I4wwAiT6RlPueGGM0OSJYwFp40srxSpXMBzI09gMiJxqmXKSR8priPu9A30DK4tU4oOAc8q3AZlt0SnOuXF5yqpmG8Ck0zsa1Ba7dOPEXoE1aD8nqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف طائرتي إنقاذ صهيونيتين جنوب لبنان بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76040" target="_blank">📅 13:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76039">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الصهيونية: رئيس الأركان الإسرائيلي طالب بمهاجمة بيروت ردا على مسيرات حزب الله</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76039" target="_blank">📅 13:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76038">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏴‍☠️
انفجارات كبيرة تهز إصبع الجليل شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76038" target="_blank">📅 13:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الصهيونية: رئيس الأركان الإسرائيلي طالب بمهاجمة بيروت ردا على مسيرات حزب الله</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76037" target="_blank">📅 12:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76036">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏴‍☠️
مروحيات الإنقاذ تنقل جنود الاحتلال من جنوب لبنان جراء تعرضهم لاحداث أمنية إلى مستشفيات الكيان المحتل.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76036" target="_blank">📅 12:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76035">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad59608b1f.mp4?token=Sz5p45jU1pYwpoiqKCYGfVvvj8ftUu1wWVKxEtHaEvAsUuXRAoiImwC_qDFhWJ5YsWWWZRj24w2CLk23csGJlN4XosK6zb9IrzEP9dnNX8EQsDZ6BJydKKT8etuyzbILQklWI37-lXRVrwRp2ZFG482ShlsRIHfN55kui7VUuDnH7aHO0gX_eXbL7Tf3Fmb80uWz0hVekoiMjLcpbuBgnkip9ka49cNN274cDDIwkaQbXlPKg4-MaHhK5rL29r-wP4GPLY0rKGveQDjCSl8fljgyJwbpNsoT9GKq_UlJjr54_VwonpUGGodrYcDuPTjJArGg0UG6EHiJyW8XV6XmLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad59608b1f.mp4?token=Sz5p45jU1pYwpoiqKCYGfVvvj8ftUu1wWVKxEtHaEvAsUuXRAoiImwC_qDFhWJ5YsWWWZRj24w2CLk23csGJlN4XosK6zb9IrzEP9dnNX8EQsDZ6BJydKKT8etuyzbILQklWI37-lXRVrwRp2ZFG482ShlsRIHfN55kui7VUuDnH7aHO0gX_eXbL7Tf3Fmb80uWz0hVekoiMjLcpbuBgnkip9ka49cNN274cDDIwkaQbXlPKg4-MaHhK5rL29r-wP4GPLY0rKGveQDjCSl8fljgyJwbpNsoT9GKq_UlJjr54_VwonpUGGodrYcDuPTjJArGg0UG6EHiJyW8XV6XmLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
منفذ زرباطية الحدودي يستقبل الآلاف من الزائرين الإيرانيين لزيارة المراقد المقدسة في يوم عرفة وعيد الأضحى المبارك.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76035" target="_blank">📅 12:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🏴‍☠️
إعلام العدو
:تخيّل رئيس أقوى دولة في العالم، الرجل الذي تعهّد بإعادة أمريكا إلى عظمتها، يجلس يقضم أظافره منتظراً جواباً من يتيم علي خامنئي. لا يستطيع حتى تذكّر اسمه الأول: مجتبى؟ مجتبى؟ مجباتا؟ قل لي، هل هو حقيقي؟ هل أنت متأكد أننا لم نقتله؟ ومع ذلك، يجلس وينتظر أخبارًا من طهران. إنه كالرجل الذي وعد بالقفز من سطح السيرك، وعندما وصل إلى القمة لم يتحرك. صرخ من راهن عليه: "اقفز الآن!". فأجاب الرجل: "لا فائدة من القفز، ولكن كيف ننزل من هنا؟".</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76034" target="_blank">📅 12:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: مسيرة تابعة لنا هبطت اضطراريا في وسط إسرائيل إثر عطل فني</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76033" target="_blank">📅 11:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76032">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: واشنطن تغير مواقفها بشكل مستمر وأحيانا في ساعات قليل
لا يمكن القول إن توقيع الاتفاق بات قريبا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76032" target="_blank">📅 10:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76031">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
إعادة انتخاب محمد باقر قاليباف رئيسا للبرلمان الإيراني</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76031" target="_blank">📅 10:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76030">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cff109ec.mp4?token=q7Nys1laDeMK6m-PAPGXxm6-Mb5Ym4eISKiPYzLFM_kLwSH8CUPWR01z_DRkZ2daPB2P0XXxvalGjNrX32u2vB0x90JLISpmID3K3jLXHcBxX_Uz5Hba6I2JPcoVRrqXkCfWFNLSaDAlZF7pHV2TEAQe81NfmzDK4OOCqADUehzSzTQ_T6m47ZAqInJTot2UW9uxw6EDGExr5CI9k_NWP1rgd6Kqu9ghlZqM0OMNiW1nuTFzDVSaxA784rs2gOj1uJ6PDrL052fppVHbVh69qk0g6Kv5h1TlfKUFF73dceJsOaoT8N-UbYUD2Qscr0ZhO1fGmdYnsYrpN5Zd1qrhlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cff109ec.mp4?token=q7Nys1laDeMK6m-PAPGXxm6-Mb5Ym4eISKiPYzLFM_kLwSH8CUPWR01z_DRkZ2daPB2P0XXxvalGjNrX32u2vB0x90JLISpmID3K3jLXHcBxX_Uz5Hba6I2JPcoVRrqXkCfWFNLSaDAlZF7pHV2TEAQe81NfmzDK4OOCqADUehzSzTQ_T6m47ZAqInJTot2UW9uxw6EDGExr5CI9k_NWP1rgd6Kqu9ghlZqM0OMNiW1nuTFzDVSaxA784rs2gOj1uJ6PDrL052fppVHbVh69qk0g6Kv5h1TlfKUFF73dceJsOaoT8N-UbYUD2Qscr0ZhO1fGmdYnsYrpN5Zd1qrhlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تشتعل بصواريخ حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76030" target="_blank">📅 10:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تشتعل بصواريخ حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76029" target="_blank">📅 09:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBxYes0_ljL-4Hc6Pymy7VK8zzh60D3K20rJZfZIsxNu-DX0wvbis_nVXG6Do_uhxD-c4mImaYfngQ022YqwkrEbGaC8QqdzDlKPWE7SECQDlin66Q6_7HfjcPG7o5Ra4cY6qE4QW55kOuPsph9s-sEmSRO9lo_3rpWFa5Rw6rRKUbu4zByUX14Bk05zE7IcwZYvHFFbkUKKvcby3gbXbhpbNb_aU7bEDfglYKjMh4v7HzpziZboMOFZoj7d5glINWK0oRka53464lTSqNOrTnNeZuCB_Dgy0G_m4p_9vc_dM0olKJQEgR-lBKVyVnn4nLWx2jwAkwWSbOPxCjO4jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أنباء اولية تتحدث عن شهيد وثلاث جرحى كحصيلة اولية من قوات الحشد الشعبي</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/76028" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76027">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76027" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76026">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/76026" target="_blank">📅 00:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/76025" target="_blank">📅 00:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
لا تشعر إيران بأي ثقة تجاه الولايات المتحدة، ويراعي تبادل الرسائل عبر الوسيط الباكستاني باستمرار حالة التشاؤم تجاه الحكومة الأمريكية.  حتى الآن، لم يتم التوصل إلى تفاهم نهائي، ولا يزال التحدي قائماً في بعض البنود، ولكن حتى في حال التوصل إلى تفاهم مبدئي، فإن ذلك لا يعني أن إيران ستغير موقفها من أمريكا ولن تضمن وفاء هذه الحكومة بالتزاماتها. أن للأمريكيين سجلاً سيئاً للغاية في المفاوضات، مما يعزز حالة التشاؤم ويزيدها رسوخاً؛ ولذلك، حتى في حال التوصل إلى تفاهم، ستراقب إيران تحركات الولايات المتحدة خلال العملية بعد إعلان الاتفاق، وإذا أخلت الولايات المتحدة بتعهداتها في تلك المرحلة، فستحتفظ إيران بموقفها الرافض لها.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/76024" target="_blank">📅 00:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIfntvacUsHOO2e79s-Jq81OJ5W7IV1QtkfQ4I2bb4mBfhN_cJADF9iG8TntOJYOBrqBKWSVnItpkLLrT19ZgcQ4h805v3BHoYw2bB7-1IEOYUD9roJ1-H_T7qQbGbzDQLi8Fc92rMODmbj9EC4GU69FAvECZc3AqRKn7h30027EFI9-1tm23rRYZiHWZJPsC26-CtwbZFybWyfngdZBgejmXcIkNi-HVpc8T-msh6YSaeNwSiIYRF0ehhjFJJVH1jPk7ofsnejeVFotmJOqZR7LRTh4qVefkqM0Zr2fUyb0ZCgg3wVEexi_vFHcthqiV1S6CjhVK5LI4LSUXVlhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر على حسابه الشخصي.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/76023" target="_blank">📅 23:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76022">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgN126htUFVgQB31eQJ1Tvf-NAZNwA9HDhkaYHBwJT36bbJlhlzM8CtHKImoF9-iNgIW-7L_1eCMF99V9_lrqdCxP9EtMnGX5VtXDBkfaPF1175jUFyD2sVs41rNXbqcy16ee1Wa2XuwNSdZsCmKnaeCJQdLj62wv1vC-7yTZquXS0OMgprhKsmfvNQcVtwel7iCRf4m9aa4BDCY28h_iRdTYvUkNslNVPpVYetsZoY8If58aCuoS17zuahlWlX0QDH4AAa92NioGyJ6d7ZjtA03179yLyjANAfWlVsjprtVdZ_ysvC0WaLDDIzKZJjKmV_t65PMbkfD048mllMtcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان.. مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/76022" target="_blank">📅 23:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76021">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي: قضايا مثل مخزون إيران الصاروخي وتخصيب اليورانيوم ستناقش بمفاوضات لاحقة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76021" target="_blank">📅 22:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76020">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من استهداف المقاومة الإسلامية عبر سلسلة عمليات لقوات جيش العدو الإسرائيلي في بلدة رشاف جنوبيّ لبنان بسربٍ من محلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76020" target="_blank">📅 22:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌟
🏴‍☠️
لبيك يانصرالله..
حزب الله يعلن عن إستهداف طائرة حربية إسرائيلية في سماء جنوب لبنان بصاروخ أرض جو.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76019" target="_blank">📅 22:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0_c1QTkIlr1dXPpPrphmlinyRLbSut3AfgSYVzgBNFTBkLe_i1rQ5ovn8ZfRLs0Vv_T4y8_5NGNmVYECsqrq01ieFsItV-v1ypcYiLJ70yo10-3TUhO-eFcok8fDem-RSjz4MOjyD7sAD_icypS6eKFgl6PzOycXXni9pTnlXKVMIzh3A1MMfO5Lp2ZQ0Mr1SLpC-dz_l5lSgpC40SEq-t-yA4cP_aT0Rrxu6lcaeTdcDh4zebLp97kgqKmfdbh8HwOVUNuTo1Dd78GxOzGrmdLIXXVimCs5cgKYspK0k_6AC1vgA2dGZ85AkMXDaiZnR5KEWLQQ6Sb7Dszvoq-gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إذا أبرمت صفقة مع إيران، فستكون صفقة جيدة ومناسبة، وليست مثل تلك التي أبرمها أوباما، والتي أعطت إيران كميات ضخمة من النقد، ومسارًا واضحًا ومفتوحًا نحو السلاح النووي.
صفقتنا هي عكس ذلك تمامًا، لكن لم يرها أحد، أو يعرف ما هي. لم يتم التفاوض عليها بالكامل حتى الآن. لذا لا تستمع إلى الخاسرين، الذين ينتقدون شيئًا لا يعرفون شيئًا عنه.
على عكس من سبقني الذين كان يجب أن يحلوا هذه المشكلة منذ سنوات عديدة، أنا لا أبرم صفقات سيئة!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76018" target="_blank">📅 21:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a74538399.mp4?token=lYYxZglhv535wFYcWOMBbKUTpw-vSN3cSCf9OaE1fX37ZV-q3fp__WS4pSbDAdpclyFXBA2cc6EcP4cMcldCQB6hkb2p-En-U9svSrRm9wBd6Mq1X-xGNLNkIYFMHQAQ7FBXmwpEhzkIHsf5zc3jaYwPyFAE_HR1BUu5uEKR2JalPg9CoDPEOv167LjFyfPtAbxRVCrU0Vb4e9GlSkC2Z1Z2_aP7QcZZeZ_xIWOgzQj7ok7V_RzejzfGc3N_xY7f82AjIA5v36lK-TDbFqMLMz_ri0j8-zo292zzi5Gi-wkpd39eLRm7N_SFZnhNRhE2LYUrMNdeUGPPAv_q2-rTEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a74538399.mp4?token=lYYxZglhv535wFYcWOMBbKUTpw-vSN3cSCf9OaE1fX37ZV-q3fp__WS4pSbDAdpclyFXBA2cc6EcP4cMcldCQB6hkb2p-En-U9svSrRm9wBd6Mq1X-xGNLNkIYFMHQAQ7FBXmwpEhzkIHsf5zc3jaYwPyFAE_HR1BUu5uEKR2JalPg9CoDPEOv167LjFyfPtAbxRVCrU0Vb4e9GlSkC2Z1Z2_aP7QcZZeZ_xIWOgzQj7ok7V_RzejzfGc3N_xY7f82AjIA5v36lK-TDbFqMLMz_ri0j8-zo292zzi5Gi-wkpd39eLRm7N_SFZnhNRhE2LYUrMNdeUGPPAv_q2-rTEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
إندلاع اشتباكات عنيفة بين عصابات الجولاني وأهالي منطقة ترحين بمحافظة حلب السورية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76017" target="_blank">📅 21:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة الطيبة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76016" target="_blank">📅 21:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76015">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة الطيبة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76015" target="_blank">📅 21:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭐️
لمعرفة تفاصيل أصوات الإنفجارات التي سمعت في جزيرة كيش الإيرانية
👈🏻
إضغط هنا</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76014" target="_blank">📅 20:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
إن الولايات المتحدة لا تزال تعرقل بعض بنود التفاهم، بما في ذلك مسألة الإفراج عن الأصول الإيرانية المجمدة، ولم يتم التوصل إلى حل لهذه المسائل حتى الآن. وبناءً على ذلك، لا يزال هناك احتمال لإلغاء التفاهم في الوقت الراهن، وقد أكدت إيران أنها لن تتراجع عن خطوطها الحمراء لتحقيق حقوق الشعب.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76013" target="_blank">📅 19:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
رئيس الأركان الصهيوني:
مستعدون للعودة للقتال المكثف فورا لإضعاف نظام الإرهاب الإيراني.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76012" target="_blank">📅 19:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76011">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:
سنبقى حملة راية الحق حتى تسليمها للإمام المهدي (عجل الله تعالى فرجه الشريف).
ستدافع المقاومة عن الأرض والشعب والشرف وكل من يواجهنا مع "اسرائيل" نواجهه والسلاح سيبقى.
خسائر إسرائيل كبيرة جدا وما يحدث في الجنوب اللبناني سيكون سببا في زوالها.
حصرية السلاح في هذه المرحلة استهداف للمقاومة وخدمة لإسرائيل.
المفاوضات المباشرة مرفوضة بالكامل.
سنعلن التحرير الثالث قريبا بإذن الله تعالى.
من حق الشعب أن ينزل إلى الشارع ويسقط الحكومة في مواجهة المشروع الأميركي الإسرائيلي الذي يستهدف مؤسساتنا.
لدينا أعظم مقاومة أذلت العدو الإسرائيلي فاستفيدوا منها.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76011" target="_blank">📅 19:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76010">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkiCaexSrTx_H0sFpIYUuBj9kDnRiyJm28VP9OpFd6c6YVXEXe4FIvn948h_VnJfkvijPWEzBnHw3BCovfVxeDoY3xMRollskx8k8LhF4FtEriG3BDprfbiNxPrW1V4xC8cpwrLLFT5gWt7CvqW_RpbBq2Zl2vRdwocZ1J2wc1x8S6US0aJKVrulVt8rLVszq-PnT19XtH3mSUPHzMabw_v8YkDKPVQD_dHLsdewh_o_OvWfA9XX0YaMRJlg9OXfq3t-HQCubzhDG4qE8Q09T1d33gYACnNL0eZZMy1-HdIU3CtAFTvrLcarnw18CQgtuaPRccYGGZq6RTbKXsUXFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان.. مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76010" target="_blank">📅 19:25 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
