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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 15:03:20</div>
<hr>

<div class="tg-post" id="msg-76045">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من مراحل استطلاع واستهداف المقاومة الإسلامية للمربض المُستَحدَث التابع لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة وباقي الأسلحة المختلفة.</div>
<div class="tg-footer">👁️ 539 · <a href="https://t.me/naya_foriraq/76045" target="_blank">📅 15:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
🇮🇷
واشنطن بوست:
المرحلة الأولى تشمل إزالة الألغام ورفع الحصار الأمريكي والإفراج عن 12 مليار دولار، مذكرة التفاهم لا تتضمن اتفاقا نوويا بل مجرد تعهد بالتفاوض على الملف النووي لاحقا.</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/naya_foriraq/76044" target="_blank">📅 14:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf43a827a.mp4?token=JcXG1boHfGdFgr20WpJRseJN6Psds4scVtwIbqfv3jb6XSKFH-7kzNutXXV-0eJHrvUdS9qOvQxUBGVGQV_fZbSq1QDxhVaZ_4qom_2XPiTEfC8hYAqtAFOMpln2iylrH_hrQZxDN293xEcJvDzBcdRu0Yu5EGBjx3f-8YiKp8YtRKG0wSgQF80X85AlBKaszcD_ChFeGv296qIj9u4UNXxItuYnu6R5YxtuVDh3-2qSmny1NMAFnWu6kCLGrQOcB5_qUxsOBdzIxh9AgURKFURjzdraJvsl72UQlNUQ2i2AYCPLho5n6fbPSlAdIcVhCSQmnik_o3HelMKwMaD8ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf43a827a.mp4?token=JcXG1boHfGdFgr20WpJRseJN6Psds4scVtwIbqfv3jb6XSKFH-7kzNutXXV-0eJHrvUdS9qOvQxUBGVGQV_fZbSq1QDxhVaZ_4qom_2XPiTEfC8hYAqtAFOMpln2iylrH_hrQZxDN293xEcJvDzBcdRu0Yu5EGBjx3f-8YiKp8YtRKG0wSgQF80X85AlBKaszcD_ChFeGv296qIj9u4UNXxItuYnu6R5YxtuVDh3-2qSmny1NMAFnWu6kCLGrQOcB5_qUxsOBdzIxh9AgURKFURjzdraJvsl72UQlNUQ2i2AYCPLho5n6fbPSlAdIcVhCSQmnik_o3HelMKwMaD8ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
تُظهر صور قبل وبعد لحيّ الشابورة وسط مدينة رفح، كيف مُحيت المنطقة بالكامل ، بفعل القصف العنيف والعمليات العسكرية التي شنّها العدو الصهيوني على المنطقة.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/naya_foriraq/76043" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mky8g2hjkn-OUpizMyZhCHbPc_QuqyPHupHxEpeCTweY5ARJ2vLSlHPdsOFWmHeKObyXJcYdtR2KGWB72zOttlD-CjeZnXXAmfToI-MhDB2Wa7DrczKf63UDuKtFwe1puAOjzMlygsUt5y7uJk41jys7JRVTa1NlTdCbOEYyi4Q5Y61pNSWx8B8f5w7tu2I0hpsih9QOEirLWD_TGSAJmuXtOkXHfiOzXE_otygah2o1NLGQpOolJePI7W4IEr_FYZrOHk0qsWIRZFvRGaELS8Y-uj5lE34TGMfh0cpTfv1Uci1uQBuNBbvZaYW7Y6-niNlwp71kaQRVUQSr1GzvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
أضحك على جميع الديمقراطيين، والجمهوريين المنشقين، والحمقى الذين لا يعرفون شيئًا عن الصفقة المحتملة التي أقوم بها مع إيران.
الصفقة مع إيران ستكون إما عظيمة ومفيدة، أو لن تكون هناك صفقة على الإطلاق.
ستكون عكس كارثة خطة العمل المشتركة التي تفاوضت عليها إدارة أوباما الفاشلة، والتي كانت طريقًا مباشرًا وصريحًا نحو حصول إيران على سلاح نووي.
لا، أنا لا أقوم بصفقات كهذه!</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/naya_foriraq/76042" target="_blank">📅 13:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09156df5ce.mp4?token=BAKPX-0oQZ73zqoPy4MQ_quDQl7iP0scMxkhqIhp5OFhKOUgSq2HKJlKqV5Kax4nHChms5dJS940ATRgUDauSG9Nz1p0b9BgSW2FLSvwSdsewg5qRcpqh9y7oKaGeABN0YQCu49YgNncwM5kGq5kbNGtMPt6kI_lhWxTBt6F93wX2IpWjCbMCmYTXdlNALS_oUg9q4BXMIyPQVfG3_-n9ic3XQU07klZ16Se68SyyxdxO92GsR2eeou8N7mZg7IMPhwj0tkmydW4hgH0lkLy5mVSO6mHIanvFzEN6Wdy-f0oFePjJq29STrSa3qk7tDsLgPGmTNa2f8ofpJxEysUIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09156df5ce.mp4?token=BAKPX-0oQZ73zqoPy4MQ_quDQl7iP0scMxkhqIhp5OFhKOUgSq2HKJlKqV5Kax4nHChms5dJS940ATRgUDauSG9Nz1p0b9BgSW2FLSvwSdsewg5qRcpqh9y7oKaGeABN0YQCu49YgNncwM5kGq5kbNGtMPt6kI_lhWxTBt6F93wX2IpWjCbMCmYTXdlNALS_oUg9q4BXMIyPQVfG3_-n9ic3XQU07klZ16Se68SyyxdxO92GsR2eeou8N7mZg7IMPhwj0tkmydW4hgH0lkLy5mVSO6mHIanvFzEN6Wdy-f0oFePjJq29STrSa3qk7tDsLgPGmTNa2f8ofpJxEysUIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الكيان المحتل جراء إطلاق مسيرات وصواريخ حزب الله</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/naya_foriraq/76041" target="_blank">📅 13:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76040">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6BsZU_oMhP1dY9LbmyAFySbjlT1elh3NmFceE4UUju2Max_LFFvo-5__vyTgOX1Y080tboIkW7WwjyBQj3t9hg2ekUmLznW-893MH42pVAUP4jfLuDs5rsOLwXVlELsYXGf3PFnJ3U7CrS0BwXqvPHBqfDYUOBZ1kAlerdOGUGevcrx1VFvGReF9ASGOji2ZAa2Aluc0AUjm5YeTiC4TKXJToQNr12dD8B5I4wwAiT6RlPueGGM0OSJYwFp40srxSpXMBzI09gMiJxqmXKSR8priPu9A30DK4tU4oOAc8q3AZlt0SnOuXF5yqpmG8Ck0zsa1Ba7dOPEXoE1aD8nqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف طائرتي إنقاذ صهيونيتين جنوب لبنان بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/naya_foriraq/76040" target="_blank">📅 13:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76039">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الصهيونية: رئيس الأركان الإسرائيلي طالب بمهاجمة بيروت ردا على مسيرات حزب الله</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/naya_foriraq/76039" target="_blank">📅 13:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76038">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🏴‍☠️
انفجارات كبيرة تهز إصبع الجليل شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/naya_foriraq/76038" target="_blank">📅 13:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76037">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الصهيونية: رئيس الأركان الإسرائيلي طالب بمهاجمة بيروت ردا على مسيرات حزب الله</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/naya_foriraq/76037" target="_blank">📅 12:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76036">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴‍☠️
مروحيات الإنقاذ تنقل جنود الاحتلال من جنوب لبنان جراء تعرضهم لاحداث أمنية إلى مستشفيات الكيان المحتل.</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/naya_foriraq/76036" target="_blank">📅 12:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76035">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/naya_foriraq/76035" target="_blank">📅 12:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76034">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴‍☠️
إعلام العدو
:تخيّل رئيس أقوى دولة في العالم، الرجل الذي تعهّد بإعادة أمريكا إلى عظمتها، يجلس يقضم أظافره منتظراً جواباً من يتيم علي خامنئي. لا يستطيع حتى تذكّر اسمه الأول: مجتبى؟ مجتبى؟ مجباتا؟ قل لي، هل هو حقيقي؟ هل أنت متأكد أننا لم نقتله؟ ومع ذلك، يجلس وينتظر أخبارًا من طهران. إنه كالرجل الذي وعد بالقفز من سطح السيرك، وعندما وصل إلى القمة لم يتحرك. صرخ من راهن عليه: "اقفز الآن!". فأجاب الرجل: "لا فائدة من القفز، ولكن كيف ننزل من هنا؟".</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/76034" target="_blank">📅 12:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76033">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: مسيرة تابعة لنا هبطت اضطراريا في وسط إسرائيل إثر عطل فني</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/76033" target="_blank">📅 11:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76032">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: واشنطن تغير مواقفها بشكل مستمر وأحيانا في ساعات قليل
لا يمكن القول إن توقيع الاتفاق بات قريبا</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/76032" target="_blank">📅 10:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76031">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
إعادة انتخاب محمد باقر قاليباف رئيسا للبرلمان الإيراني</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76031" target="_blank">📅 10:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76030">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cff109ec.mp4?token=NH9ozKbJMRV6L7B0P9VMlKUXbC4YqwkHQuEQUTPI7RH1V1-8EG5-VflQ9HNHTq0Atte3kGHMCg2jrg2qDI3DrKhfDdwc9ctI6ppErj1T_JKulYu0vW4Bc6Yj8WGWZcoWmrXnPXP3vnTRp3FcmZbUhC0-J8bJy2za-R_GAM_pBTPwsRQoMikRPTnIIxjvZs2EOym9HX68R32kxlJbitAlz98li0eNiQr9GpvisLo8a4z53RPqd_hjsnKiFvd4dxIm0_j3sfXT66-bc32K1IU38sWMMSZaiOnIO5vkK7FlYMyIR8qmFddbPCfOQrcPYd0f9ewPp5L4rVMpljzwgIC51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cff109ec.mp4?token=NH9ozKbJMRV6L7B0P9VMlKUXbC4YqwkHQuEQUTPI7RH1V1-8EG5-VflQ9HNHTq0Atte3kGHMCg2jrg2qDI3DrKhfDdwc9ctI6ppErj1T_JKulYu0vW4Bc6Yj8WGWZcoWmrXnPXP3vnTRp3FcmZbUhC0-J8bJy2za-R_GAM_pBTPwsRQoMikRPTnIIxjvZs2EOym9HX68R32kxlJbitAlz98li0eNiQr9GpvisLo8a4z53RPqd_hjsnKiFvd4dxIm0_j3sfXT66-bc32K1IU38sWMMSZaiOnIO5vkK7FlYMyIR8qmFddbPCfOQrcPYd0f9ewPp5L4rVMpljzwgIC51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تشتعل بصواريخ حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76030" target="_blank">📅 10:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تشتعل بصواريخ حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76029" target="_blank">📅 09:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEeTnEn9f7CWMZ0cnUiLG7e9E8kI7j2DoXgglNcya__QPRBdzZAezw0nZZJh9GdA8iaCZHF7YAHivERIl5hmsE4NRF8epFLxA5_bRm6PmBb6VUT-UMOLeHlJh4ZuiPxbtlz2q1-jSwmQodD9B2HDIxf92MPNeJV9tX2Mr6_fBLGVG7dVEqzsw4kPwgos3G3Fc_OgBMVu-gVfjLm2XmMHJ8r5w7pgx-6oiaycGR3rMe0YWKsUXRmxjlTEq7cHrTStTQmcB-c980l5iRxNpWjgoXb46Dk44oE9IFR8bzySaJN4pfF4qAsROclIFEpKANUGSFkQbzqC9h3yOaDHCsj6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أنباء اولية تتحدث عن شهيد وثلاث جرحى كحصيلة اولية من قوات الحشد الشعبي</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76028" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76027">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76027" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76026">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76026" target="_blank">📅 00:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76025" target="_blank">📅 00:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
لا تشعر إيران بأي ثقة تجاه الولايات المتحدة، ويراعي تبادل الرسائل عبر الوسيط الباكستاني باستمرار حالة التشاؤم تجاه الحكومة الأمريكية.  حتى الآن، لم يتم التوصل إلى تفاهم نهائي، ولا يزال التحدي قائماً في بعض البنود، ولكن حتى في حال التوصل إلى تفاهم مبدئي، فإن ذلك لا يعني أن إيران ستغير موقفها من أمريكا ولن تضمن وفاء هذه الحكومة بالتزاماتها. أن للأمريكيين سجلاً سيئاً للغاية في المفاوضات، مما يعزز حالة التشاؤم ويزيدها رسوخاً؛ ولذلك، حتى في حال التوصل إلى تفاهم، ستراقب إيران تحركات الولايات المتحدة خلال العملية بعد إعلان الاتفاق، وإذا أخلت الولايات المتحدة بتعهداتها في تلك المرحلة، فستحتفظ إيران بموقفها الرافض لها.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76024" target="_blank">📅 00:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpBPJRznJmENhgdscasw-t3siKQkjKPpjQuoYwHOMKBvnymkgMYv5ngx6ZbIu3QN_QHK1LAk9gRB6hn_oM6SUtmuqIZol2h1BdaNND10PfLBDGbrbDfAWSlNEk1RPsdNh3dhxVOLsGA6JxflyxTovd97DCFfHYhWb3An6rC87GF6289jJBRlQ2u7j0uNHVtEDXxChilgixl17P39eltDk3pidHhzwg-3x5bBKWyjdW7GiIB2miInEBZTs0LQ6AvAQAzRS-Qm83sh5fVMpPWaVpQ3bvY76iJ5zy-oyJAbHGeMItd7X1GjD0WNyxtjVlKLEwXsdIV-ikcTJKT0p8UCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر على حسابه الشخصي.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76023" target="_blank">📅 23:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76022">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7EWTGTIOla1FX10HVgS_gIeS7lnvBnoV0MGhBf8fVOa60EI_8lYlBFRWdMYXVEPeq-y3mF_SbdAtAt9_ckAJUVbczv6YgOxQSho99K_EpYokK8fqX2yEKs6-JSAxrSU3vjdKao4mHmwvZQ3Y8px55ej1H7B3lQFZ2UHjCWgCtMmH6Cp0gvYNskJZPZ_M4EedpvC5_27Mng8pwNCstrfdojA5Y2OZuYhfgKodh0ItBYchRib6eBitnYaEAiYDUqfY3fQDyXUOF73_0B_Toab0ZzDmYFtcEOZMMvziS5RvZqxFaEA930mIoFvcCcG00XuSX782x6P_C4t6opFncKOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان.. مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76022" target="_blank">📅 23:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76021">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي: قضايا مثل مخزون إيران الصاروخي وتخصيب اليورانيوم ستناقش بمفاوضات لاحقة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76021" target="_blank">📅 22:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76020">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من استهداف المقاومة الإسلامية عبر سلسلة عمليات لقوات جيش العدو الإسرائيلي في بلدة رشاف جنوبيّ لبنان بسربٍ من محلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76020" target="_blank">📅 22:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
🏴‍☠️
لبيك يانصرالله..
حزب الله يعلن عن إستهداف طائرة حربية إسرائيلية في سماء جنوب لبنان بصاروخ أرض جو.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76019" target="_blank">📅 22:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOnGkp40nxAWSqcTJh7-_giI7Aw0haeMbAjQ8_ldeGFKslRFkpodoIWE8DqNwiI2KkS8iYniUPNvMPfyl1Ddb6EhYGrUyazrKybjh1m8grLniAzFSBYGW5S-hCwR68HRCxwchAUWv1vvWv42Ie7ZQsqy3jEfT5Z_rfdacjij6cO2zOLVKGKvhnQaOJ7Xq87bZJesMgcce88Io65iWPAdDDFqi0VaQ2KGFc4HZWwC6I7ZTJDfZ3Z9-TlIv9uxRQupHhAjvB3IW2Ar5I4SlOjSv2vXtIYS2zx8TcFnZ9avyVGdMsSJAwTKgfnI3n0lRIFlt3s__kInlPF0VF1bh5Iefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إذا أبرمت صفقة مع إيران، فستكون صفقة جيدة ومناسبة، وليست مثل تلك التي أبرمها أوباما، والتي أعطت إيران كميات ضخمة من النقد، ومسارًا واضحًا ومفتوحًا نحو السلاح النووي.
صفقتنا هي عكس ذلك تمامًا، لكن لم يرها أحد، أو يعرف ما هي. لم يتم التفاوض عليها بالكامل حتى الآن. لذا لا تستمع إلى الخاسرين، الذين ينتقدون شيئًا لا يعرفون شيئًا عنه.
على عكس من سبقني الذين كان يجب أن يحلوا هذه المشكلة منذ سنوات عديدة، أنا لا أبرم صفقات سيئة!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76018" target="_blank">📅 21:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a74538399.mp4?token=oZEGnLlLuPd8626eKyJuDAaZNP3g3jsupzWTXw-essjKDwkpGKP-cZZHcFloW6fK1WyplSodDZtaJLdqpD_QxdwHDz5EkQpDOUTwaA6XSEgo_oIZS1Gmg4fyG8ubbom20Oys76RxU7ER7-3HAxMOa0rLrNsoK8YZwLCO_uNaphdePcE9PvZJWpZtlBZIeebDaVChZ_v24PLPoUW05F1oz_RVswW9D3NtWPvv522RK7Gk97BSbYIRmIFaPCKXbhRwXONJjFrFcgcxOTZyigdrkg4FBrwT1QMg-3Jxb_gWCQj10xKF6-U0fT_CONKrQFxyLJ24TStT2Wqoi7jDLJJdBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a74538399.mp4?token=oZEGnLlLuPd8626eKyJuDAaZNP3g3jsupzWTXw-essjKDwkpGKP-cZZHcFloW6fK1WyplSodDZtaJLdqpD_QxdwHDz5EkQpDOUTwaA6XSEgo_oIZS1Gmg4fyG8ubbom20Oys76RxU7ER7-3HAxMOa0rLrNsoK8YZwLCO_uNaphdePcE9PvZJWpZtlBZIeebDaVChZ_v24PLPoUW05F1oz_RVswW9D3NtWPvv522RK7Gk97BSbYIRmIFaPCKXbhRwXONJjFrFcgcxOTZyigdrkg4FBrwT1QMg-3Jxb_gWCQj10xKF6-U0fT_CONKrQFxyLJ24TStT2Wqoi7jDLJJdBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
إندلاع اشتباكات عنيفة بين عصابات الجولاني وأهالي منطقة ترحين بمحافظة حلب السورية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76017" target="_blank">📅 21:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة الطيبة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76016" target="_blank">📅 21:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76015">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة الطيبة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76015" target="_blank">📅 21:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⭐️
لمعرفة تفاصيل أصوات الإنفجارات التي سمعت في جزيرة كيش الإيرانية
👈🏻
إضغط هنا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76014" target="_blank">📅 20:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
إن الولايات المتحدة لا تزال تعرقل بعض بنود التفاهم، بما في ذلك مسألة الإفراج عن الأصول الإيرانية المجمدة، ولم يتم التوصل إلى حل لهذه المسائل حتى الآن. وبناءً على ذلك، لا يزال هناك احتمال لإلغاء التفاهم في الوقت الراهن، وقد أكدت إيران أنها لن تتراجع عن خطوطها الحمراء لتحقيق حقوق الشعب.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76013" target="_blank">📅 19:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
رئيس الأركان الصهيوني:
مستعدون للعودة للقتال المكثف فورا لإضعاف نظام الإرهاب الإيراني.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76012" target="_blank">📅 19:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76011">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/76011" target="_blank">📅 19:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76010">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2993zbJ4i-5ksSpThsAA-x3V5J4OIF_7f7Nc75nJUmlTyk3kZG7gHZVJduEuNVFUEEDszsP-yIcVtQmVy8Xj-sn9av5IVfSCYgZLSzQr21ycUCZdCJAxOJbZfL62ElrYugwquS1YEzQjoSPKfoWr8L-yKPsbZHGbFvLx7gweSVDINUHm5eUWAr19z7mwQmwqY790GvmOkGgvwZ0fdwVtgntJ2w4cevDAWmagDTGG7myn8aUM3M0SRRS36Jv7mky7p4KiXGjLPZZbImzxKY2ROROl0YpExfweP2BGVNTE19CNclKEtCLbfUToZu-8LCQ5ht9AVT8kVhK3enGIvfaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان.. مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76010" target="_blank">📅 19:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76009">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
مسؤول بالإدارة الأمريكية: سنقدم تنازلات بشأن تخفيف العقوبات إن تنازلت طهران بمسألة التخصيب.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76009" target="_blank">📅 19:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76008">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
مسؤول بالإدارة الأمريكية:
سنقدم تنازلات بشأن تخفيف العقوبات إن تنازلت طهران بمسألة التخصيب.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76008" target="_blank">📅 18:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76007">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان..
مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76007" target="_blank">📅 18:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76006">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATrnIPoEBO7PCCSy-DDVOTgTaolQ2XJVnfYFJv3PpSur6NzSqPqCDRXxK8COcJRj6-C-P7RRzbTGWfjzIPFTRYCDiwlSQGMmYIF8Iqmmu1ArN_hAOAn7UyEkLE8Gkou7er_-OxJLOwu7WL4ktG4USHRh_R7MI8TeD2pI-_TLEu7_oR0nm_uJry5G_ymJdRatLy285cBd0w9SdJsTgZ-OLbITWRWiUv5M6E3OMUUHKN-IwnJ-HsqCz3_cbKlJGSRzapmBxyDGfh2oQNSNWhSt45rOXU6fh4gvgruRtV1ZZcJ5rfIgVaRt1jp0MsZgmKrapvOEvPpV35ywvNAkhFHoZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب: كانت إحدى أسوأ الصفقات التي أبرمتها بلادنا على الإطلاق هي الاتفاق النووي الإيراني، الذي طرحه ووقعه باراك حسين أوباما والهواة في إدارة أوباما. لقد كان طريقًا مباشرًا لتطوير إيران سلاحًا نوويًا. ليس الأمر كذلك مع الصفقة التي تتفاوض عليها إدارة ترامب…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76006" target="_blank">📅 18:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76005">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e83ce1a0.mp4?token=UWPsCfdR8xSu0Ut5FqLdyCtR-_tK4s_iPLqLjuAUfm1ovLU7_HV3DYT0ZtggZ3Zshbr9Xhx51OOETTYQL9HalRkx3ak4pnK04NkcxAS6kPZOPuOA1JfPFnLl9RxuIM0Qx1Ag86OOC9pGUisRDLtLxtqh1RuH8BGt8t_lT78sErOqguGpB5AFII-kOtcr20x4eZIXsIAQuVZ52qu71zGH452F3urXkPzWLSbhaTkpQQ9rsgY-9vtu7nzZbnkcR_0C8I2WeDnHYfbI5boV7kVVfSppS1JPiwP_4ATz3fTazElf6DOwbNcfzC2FLXyMD9fr-zSB6CyfmB4Mp8s6O7a6rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e83ce1a0.mp4?token=UWPsCfdR8xSu0Ut5FqLdyCtR-_tK4s_iPLqLjuAUfm1ovLU7_HV3DYT0ZtggZ3Zshbr9Xhx51OOETTYQL9HalRkx3ak4pnK04NkcxAS6kPZOPuOA1JfPFnLl9RxuIM0Qx1Ag86OOC9pGUisRDLtLxtqh1RuH8BGt8t_lT78sErOqguGpB5AFII-kOtcr20x4eZIXsIAQuVZ52qu71zGH452F3urXkPzWLSbhaTkpQQ9rsgY-9vtu7nzZbnkcR_0C8I2WeDnHYfbI5boV7kVVfSppS1JPiwP_4ATz3fTazElf6DOwbNcfzC2FLXyMD9fr-zSB6CyfmB4Mp8s6O7a6rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق وارتفاع اعمدة الدخان في منطقة جبلية حدودية مع إيران بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76005" target="_blank">📅 18:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76004">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63f2c0f5a.mp4?token=mNH5eEvWU3cTJXWdUjGIcRliPjqreF99m08HwC9dFoRw-yaqH2iK3RjXp4TJzxiEc7p-v3gQg7aDCjrudANkRznOdwpBW_QFoNgbKBEJtbPdKfBmdwc2irAYLtxT6Uh_Br6hBwRXqC6AxYTx4jDeTDxLUZy3bDesh0vcNhM3BVR0dgz2nUqUGWbYQITzMt8x3teohcObCk5ZrbEgSzqIzq7BiFklXLAm4ynRB2-kfQgTFuN1CEpj5NBTmSQf_RML9MK5AqyqFt-GP3WDLDu2G_ewsyCcKlNPd7I82fFkiH-TG801PLrgHnBhnKfme7pStviX2wvDSjO9zHKwh7Qemg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63f2c0f5a.mp4?token=mNH5eEvWU3cTJXWdUjGIcRliPjqreF99m08HwC9dFoRw-yaqH2iK3RjXp4TJzxiEc7p-v3gQg7aDCjrudANkRznOdwpBW_QFoNgbKBEJtbPdKfBmdwc2irAYLtxT6Uh_Br6hBwRXqC6AxYTx4jDeTDxLUZy3bDesh0vcNhM3BVR0dgz2nUqUGWbYQITzMt8x3teohcObCk5ZrbEgSzqIzq7BiFklXLAm4ynRB2-kfQgTFuN1CEpj5NBTmSQf_RML9MK5AqyqFt-GP3WDLDu2G_ewsyCcKlNPd7I82fFkiH-TG801PLrgHnBhnKfme7pStviX2wvDSjO9zHKwh7Qemg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 22-05-2026 أحد جنود جيش العدو الإسرائيلي في موقع المنارة عند الحدود اللبنانية الجنوبية بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76004" target="_blank">📅 17:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76003">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-FJBQidRrpecGGgBs-ibiTuJW5ZPEfSFP957utvACPUmO_rg5OdU_-GnF_ZgiEsrJsrM-vLJloks_SUB9KKkiZY3zLGu_VglljShYDZnkuUsRio6yiwL2YNY9pS9Fd6wADF4kWFk_WixDqN_ygHivnzATz0hIDcWkX_wr2moNJYnNJ7ryaewKol2LIQXKN1x335_x3uV7ktkKK_m8RF5u5aZ16gN3VW1GZTdvpeYtvA_xeFiTz4OMyDyIlmDVLeufvSfMIoKQZZP6O6QZCDmq6OapyJK2-Ey_x1f0_TDlf1FPip-2VWSpMAJfv-q7oX3RecBPxzVM1CahQC1HK51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
كانت إحدى أسوأ الصفقات التي أبرمتها بلادنا على الإطلاق هي الاتفاق النووي الإيراني، الذي طرحه ووقعه باراك حسين أوباما والهواة في إدارة أوباما. لقد كان طريقًا مباشرًا لتطوير إيران سلاحًا نوويًا. ليس الأمر كذلك مع الصفقة التي تتفاوض عليها إدارة ترامب حاليًا مع إيران - بل العكس تمامًا! المفاوضات تسير بطريقة منظمة وبناءة، وقد أبلغت ممثليّ بعدم التسرع في إبرام صفقة لأن الوقت في صالحنا. سيظل الحصار ساريًا ونافذًا بالكامل حتى يتم التوصل إلى اتفاق واعتماده وتوقيعه. يجب على كلا الجانبين التريث والتأكد من صحة الاتفاق. لا مجال للأخطاء! علاقتنا مع إيران أصبحت أكثر احترافية وإنتاجية. ومع ذلك، يجب أن يفهموا أنهم لا يستطيعون تطوير أو الحصول على سلاح أو قنبلة نووية أود أن أتقدم بالشكر الجزيل لجميع دول الشرق الأوسط على دعمها وتعاونها، والذي سيتعزز ويتوطد بانضمامها إلى دول اتفاقيات إبراهيم التاريخية، وربما ترغب جمهورية إيران الإسلامية بالانضمام أيضًا! شكرًا لكم على اهتمامكم بهذا الأمر. الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76003" target="_blank">📅 17:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76002">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKCLT3nDkJ_Jct10L28C1A9HKQF_ProXkgBwEOkKxUmdumVK_-gLMfkA-62J6iNuwllDK_uhMUUq17xuXEiDjoBXtrBc3O1RYA068cN-RL0X1bi0Rk1ExYE6AD05w4BWtU5j7bRLQOvL5M6mbZZnKustv5wZd6g_Z-4XlRX07W83ezpOkDVJigtwY8CzztvVvVrqaY9X71di1AoN7bpkURWTJ3icmElYlVGvOAhacVNxfMp6VhOx2RT0HQ23nOzAO0FoII8cBBzj09EdowOnklhTl4Qaq1tMg1gTHRhrFRvHftyOBJhPai9gvrOC0tHfjlE9I3kMreNmJ5Sq931AqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فاينانشال تايمز:
يُزعم أن قوات الحرس الثوري الإيراني استخدمت شركة مقرها في الإمارات العربية المتحدة لشراء معدات اتصالات عبر الأقمار الاصطناعية الصينية مرتبطة ببرامج الطائرات بدون طيار والصواريخ الخاصة بها.
ويُقال إن المعدات انتقلت عبر دبي ورأس الخيمة قبل وصولها إلى إيران عبر سفينة إيرانية بدا أنها قامت بتزييف موقع GPS الخاص بها لإخفاء عملية التسليم.
وكانت الشحنة مرتبطة بشركات مرتبطة بقوة الفضاء التابعة للحرس الثوري الإيراني على الرغم من العقوبات الأمريكية القائمة على الكيانات ذات الصلة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76002" target="_blank">📅 17:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76001">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfS4etVGI9xswT-T0y0hs90gN7E9JKib4s6BK8-yPWhEtlsEX81d0hh1w_Iga_q9ndqx1iJLIdlnLNExRBxTTxBuOdbvlTyn3XOt1lRZCEkMOO_EWxqyBkvFuBDnGh4fnELKYX-72zWALg79XLxVom5-IBftuccgpIi_gOaLoR6Bd4qsS_T8aPMXBndW3OwA75Z57lzat4uN4FlG3SDVQZp0W_KEm2P9oCh0nzwfOCgHstf5gmccf2DQvDaxUMqRgg7KvY7KQpk1MjZHZfZQDk9mbIy_lYQUjMIgwREp1sRaUyNxKvb2MEmbEWGuzjgNrFqvm-f7_gJsk8DpnHE0rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله ينشر:
بعد قليل...
الضاهر تركضلي تركضلي..
😄</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76001" target="_blank">📅 17:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76000">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6uUFwnQpBVaBguyo91cG2BYcmlGG4wpw93hUpo4e-QL7FOtPXc05H9PUoD8-83VZmsOJRS9WCiEPMsufuRmjg91algUnYDYKSPd5RyRPk4C0nmTXjaZNqnBsxLLhtnuO_KyaTIl3pjKzUkfWWg8jMBge5ZJ2h1qc6k4OBaeT13xmkbBXXY_4BIUQ69Su2Rt7hJDSVfyyPThZuPoVFtwSLdrAPxPpwcTTYcNliovUmM-VfJKeNvipBvZ4sQaD1QvZil2Bg4sbJ4nQ65YQt5sWVdIgrZLrb8jPr1it5xCAUOAabBzfgQicPBBEBq1Q7B_gKwhuGt8ljn1L4cpJSwUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
نتنياهو يغرد:
لن تمتلك ايران سلاح نووي.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76000" target="_blank">📅 17:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75999">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
‏الاتحاد الأوروبي
: توسيع نطاق العقوبات على إيران بسبب إغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75999" target="_blank">📅 17:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75998">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bbaeabc5.mp4?token=OEagbdiDJtxb2THrSjtCaH3O1qHXT_h_FO7ydI-_jy9I7p482Q4MdspKxF_NaRg_MJhxWVTbuBgb4-CTX3ECRcZdvcrFK3WgxEW78Frfq_6M9gxHEyRErUBw7N6IIbioko5p2yVFzPHmnnx_TmSK3drYV_0iWsirOwefsx0RlPCuGc3kyf16tbUvEL3qCzlKPuKorygimz4ovogSI3HnXEYixCE02t5V-CRqftdUxWJHTOJb0FZ0CRE92ucfoDhJKiDDRIp-0S-pe-zULUkMUGL-y7mUN_PG6kUFjnCugsFRPIRc5YQFwpAN7la81KucGqDG9SmZatm0dU_7tB2_IhsBCTZELrLggjhZgoF3FUXQnqzmUtanEw8Uji2AjAJiRzIObrOIdOgfFreUMmAJscrcw084HHEyk9Nea2pDwbjWT6mvQUwZF-nGf7hOjLhlGqkYIp_WQHjep1MZAYC0GtG4O6zwa-y1LoFBVncJAkqH8w2TtIaF2vutDg0-TnorEx-PUuWaaqhGkmjp47RfrfEsYZ9HNZmxKNMrJpiSZYXLHfKAmh-4G8hAdYr65s8ote_EdOs8Kql_Kr7yiZu99YjvCc_77jyV_f6yIoRWPF4PG1JKSGY1An4Md5s3ZIp5EEqiC8HktwH0bcY7krdtuqtF-WCwU8BAy5EeMaPuU3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bbaeabc5.mp4?token=OEagbdiDJtxb2THrSjtCaH3O1qHXT_h_FO7ydI-_jy9I7p482Q4MdspKxF_NaRg_MJhxWVTbuBgb4-CTX3ECRcZdvcrFK3WgxEW78Frfq_6M9gxHEyRErUBw7N6IIbioko5p2yVFzPHmnnx_TmSK3drYV_0iWsirOwefsx0RlPCuGc3kyf16tbUvEL3qCzlKPuKorygimz4ovogSI3HnXEYixCE02t5V-CRqftdUxWJHTOJb0FZ0CRE92ucfoDhJKiDDRIp-0S-pe-zULUkMUGL-y7mUN_PG6kUFjnCugsFRPIRc5YQFwpAN7la81KucGqDG9SmZatm0dU_7tB2_IhsBCTZELrLggjhZgoF3FUXQnqzmUtanEw8Uji2AjAJiRzIObrOIdOgfFreUMmAJscrcw084HHEyk9Nea2pDwbjWT6mvQUwZF-nGf7hOjLhlGqkYIp_WQHjep1MZAYC0GtG4O6zwa-y1LoFBVncJAkqH8w2TtIaF2vutDg0-TnorEx-PUuWaaqhGkmjp47RfrfEsYZ9HNZmxKNMrJpiSZYXLHfKAmh-4G8hAdYr65s8ote_EdOs8Kql_Kr7yiZu99YjvCc_77jyV_f6yIoRWPF4PG1JKSGY1An4Md5s3ZIp5EEqiC8HktwH0bcY7krdtuqtF-WCwU8BAy5EeMaPuU3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 18-05-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي عند خلة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75998" target="_blank">📅 17:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75997">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
‏
يديعوت أحرونوت:
إذا تم توقيع الاتفاق بصيغته الحالية فستكون هذه كارثة على إسرائيل.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75997" target="_blank">📅 16:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75996">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117e266d3d.mp4?token=fiF2pFuP8JbkM60j6awue7l_XoTjm8TmggDPtRT3q3CCyMQZPkMh_QSEQxuGKuM1PuJCJuQOm1f9N7CeeU93A2rFR9X6AtMuJpfv8OR8W2Gm9074ZmMuW8twejYaHXaLa5XW0b50Vq2xN6tnEf3YpkSdDoLuoGkKyaQa8C1Du2BkxaDdbTv_WqcA1y3YDbQQUYPV_kESgdd7DLU-fRW6e68Naf_rgFcnDJ63NenEw20CImBC--cT1ajtnOau-5g9aayMOgwnLVYdoSpyI4n5jh4RLfZx2HX2Z8YxOcibtd3WUyb0WvoUOIEysloMYw7AaD6ekSWj_dUsoKTZqv3U0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117e266d3d.mp4?token=fiF2pFuP8JbkM60j6awue7l_XoTjm8TmggDPtRT3q3CCyMQZPkMh_QSEQxuGKuM1PuJCJuQOm1f9N7CeeU93A2rFR9X6AtMuJpfv8OR8W2Gm9074ZmMuW8twejYaHXaLa5XW0b50Vq2xN6tnEf3YpkSdDoLuoGkKyaQa8C1Du2BkxaDdbTv_WqcA1y3YDbQQUYPV_kESgdd7DLU-fRW6e68Naf_rgFcnDJ63NenEw20CImBC--cT1ajtnOau-5g9aayMOgwnLVYdoSpyI4n5jh4RLfZx2HX2Z8YxOcibtd3WUyb0WvoUOIEysloMYw7AaD6ekSWj_dUsoKTZqv3U0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب مستعينا بالذكاء الصناعي   كون الحقيقة مؤلمة جدا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75996" target="_blank">📅 16:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75995">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNoBczEFGayelEUwSSCCcKZWx5kDcyvQj_Tj7wIGyEPO_T3MxmI5OM0263XcWMUAfg3s0vgpMNHKf-Zq6VaJWs89St8XuamYmsQtqt47H6LsIlZjw1MDgKNtJnB4R_JNe9XwIHbSvKumHYPjQgpmaIHF3zHCQ2xmb2mAP8KWh9dvAd0cr4nwGhmKHWy1kH_wfxbiMcb0-SFOoFywI9qO49UFULrsZG6qbAFK6nU1DPenWfIp4BqrUy5Im79q5up9XJp7vUFITJv3y9Hfmf9M5SZhpu64C4XYdtfeecL57sK0w3m86KPshWOd0-Amrq8iPndbuX_q3HkL0VTeHSj5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب ينشر مجموعة من ساسة الحزب الديمقراطي يرتدون زي المساجين!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75995" target="_blank">📅 16:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75994">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea9114205.mp4?token=ZHqZyzMuRKvkPCindcU7YIoiRNRmG5mjIUU-jZ89-U6WNSfnpTeyour9JCdatUNEIyXSqEP9yH22h3WGjyUMrKcK7mUWJPCc99aLGTYbuR1aF_WGwvIlbc_h0QT8rN2AdPZJL3pAyJKRTVfyIQht0nZJr0OMgBsHDzmaF_6wYcHri6KH9a7D4ZjQXYH5is4qW1PHz-4PK69WxfycfJ7tuRzCKNlaMfWUyNmEj7lb7YZFUrQ-wVJLYriQzKvtd4fhf6zZDYfa87wteR4LFL4RotIhZfDL4ger0-wSUpIJHq0zjwsT0Y0OR6ku9u43F8EnqjcSkGvZUKd8C1rrOp8pEAqscEXRhYT4lhaXtELNov1xdMBWRk9QRx9eYN_zmE0BkkknOxk4Tu0K10TPllvzvkBi-VQe_-amzRchZNhc_BevwVgdE8wYeKcF2NwT1rfbzGwSiWljCQNCB2jsrXmG2LFK8p1VUoPUS8bi6_nYTsAX-VnSzN1bvSHcS66edWKHaRgLYTC1ATruJUcFEB8i8VJgfJQGS7RUboDUXh7w0zGz7fwudPQwuOkNS6oUcaR-lhVXLRzjFdeKHn6wXTX4rSsXLI6GacBfPxGECni-PXCQeUQAJrZxTe0f2zWaPyPFGb2hAm7ducGLT8lcM3P0sNXZfIbU3n9jidTv2kUOgnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea9114205.mp4?token=ZHqZyzMuRKvkPCindcU7YIoiRNRmG5mjIUU-jZ89-U6WNSfnpTeyour9JCdatUNEIyXSqEP9yH22h3WGjyUMrKcK7mUWJPCc99aLGTYbuR1aF_WGwvIlbc_h0QT8rN2AdPZJL3pAyJKRTVfyIQht0nZJr0OMgBsHDzmaF_6wYcHri6KH9a7D4ZjQXYH5is4qW1PHz-4PK69WxfycfJ7tuRzCKNlaMfWUyNmEj7lb7YZFUrQ-wVJLYriQzKvtd4fhf6zZDYfa87wteR4LFL4RotIhZfDL4ger0-wSUpIJHq0zjwsT0Y0OR6ku9u43F8EnqjcSkGvZUKd8C1rrOp8pEAqscEXRhYT4lhaXtELNov1xdMBWRk9QRx9eYN_zmE0BkkknOxk4Tu0K10TPllvzvkBi-VQe_-amzRchZNhc_BevwVgdE8wYeKcF2NwT1rfbzGwSiWljCQNCB2jsrXmG2LFK8p1VUoPUS8bi6_nYTsAX-VnSzN1bvSHcS66edWKHaRgLYTC1ATruJUcFEB8i8VJgfJQGS7RUboDUXh7w0zGz7fwudPQwuOkNS6oUcaR-lhVXLRzjFdeKHn6wXTX4rSsXLI6GacBfPxGECni-PXCQeUQAJrZxTe0f2zWaPyPFGb2hAm7ducGLT8lcM3P0sNXZfIbU3n9jidTv2kUOgnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75994" target="_blank">📅 16:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75993">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe46a8c5f9.mp4?token=Q_y8OHyRR0U8LEuGPyAS5HtyuqD4CfnxvWBBV-OPwlXqBTpmFQ3qRZJH1gXRnZ2nd2_m3nQkjUYTWZQhqzcmfNCExPrZbRtZTIZLrQg-OttqakQGD5uaZ4e9jS8FG0ZuSYoxyvoZR8sMP43kVRxN2mf8l5DUBOJ8ZKwwAILW0l2ubg8THR2ZhI_U5ySmmCZUgFiZUgSGkxL4KZpKSr1U1xkLIaboeHN0MISDofG9WgUBV8UQ3XS3UM1DQ--Hjyp6EmhMQNHuvYF0iCu0_1WFAO9Cqt2UZFOhYQdtgTSWamRfPVkieGQzXmet4Z-K0nO4I8YCQjcjF1hT9tlwmH7a7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe46a8c5f9.mp4?token=Q_y8OHyRR0U8LEuGPyAS5HtyuqD4CfnxvWBBV-OPwlXqBTpmFQ3qRZJH1gXRnZ2nd2_m3nQkjUYTWZQhqzcmfNCExPrZbRtZTIZLrQg-OttqakQGD5uaZ4e9jS8FG0ZuSYoxyvoZR8sMP43kVRxN2mf8l5DUBOJ8ZKwwAILW0l2ubg8THR2ZhI_U5ySmmCZUgFiZUgSGkxL4KZpKSr1U1xkLIaboeHN0MISDofG9WgUBV8UQ3XS3UM1DQ--Hjyp6EmhMQNHuvYF0iCu0_1WFAO9Cqt2UZFOhYQdtgTSWamRfPVkieGQzXmet4Z-K0nO4I8YCQjcjF1hT9tlwmH7a7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تنفيذاً لحكم قضائي يقضي بتنحية أوزغور أوزيل من رئاسة حزب الشعب الجمهوري، اندلعت اشتباكات بين قوات الشرطة وأنصار أوزيل أثناء دخول القوات إلى المقر الرئيسي للحزب في أنقرة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75993" target="_blank">📅 15:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75992">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYWNGUXJsIH2jwhByPfRTt2AzSt-AwprAOL1m4FHIskCMWBqBbB-37fGiFnijqhP4vB0ZJCyO6tS-4Zi4J3yfWIqYGYtxEl91KGv5YOoa34lGeiskWxSmG3ILs3XyfPXEIXT0kfWJbSSOckRT1mpr0ipxm7pa1OWnvU15Pj0--2Nmu3hAjuG6HQ4gIDIqtwBPilutg3U5T8GzKjpJhkWmaCmxD_kGztuWZHQTloKgtBC7GUTluYDZATKZh9OCK7Zb5mceKAt8wLklw7JZm6sl7JfbbBzFdA1ZyoGjY8LVEe3Mvv5XgS_614L1hPcjlyeaOY7PMW2arO3glqGuIhdjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب مستعينا بالذكاء الصناعي
كون الحقيقة مؤلمة جدا</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75992" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75991">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff86c83697.mp4?token=lp42LE4oC0cETuO7GAkCCSWbeiwJiZgWxOqHLrxPQjiGBxnSzmRYKuMr5W0EsPqia-o_RcglxbAs7gcP91JvvNJbe99kbJo02VQPZl6T6pSYpRq29csn7g0GsaVD5M03YO7eQiSFpSAURMvTEKAvBTOexZInoVHahw3lZhxbqQAI7goCxhPD8e1rULH5y_FmZDQQyvFdyC5reH32eZAmTEv8aghQN_3ZtjhiyG_Y5p-zLoGWdsjIjd3xDE2BdQpkxnLkUX6fk90ZBbPXe85VnhIr3wTZE9GCw_Jr5J-lZEglfH7VhMzlnqHzyR8SpDb7AaaoVmCfp5Qedk-uCA0A56pH-z8geX3pp_4lrBAdDgwBVTJWt75_m9IETOVw68jfE15fGazQ9sUP8bXCNtaT8rfxUgqFBzCMFzR59NDiiMwpKK91PO7h9IXXLQ2jCIcEBSYP67YUGfYiygSIfCjV4bbESXSWXcyimIoBFlwLVZ2kaxGzMytwzeXD2J13THbE0tiGZoxNTj_e5clV-11sBxscBhWIQYRXeJRmwY8AwU-y-pYAdDsGaSMBOH-_ou1Y0Pbj7xt-Xy-D1Q9so-aYZvvgRaLJCz8lbXRzhKJjW6xpW1p1Vj9g5opkLlXWxzwUWB2oHZj88W_VjBeqlIPvthoNF8-seED1ljq8MGeKJWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff86c83697.mp4?token=lp42LE4oC0cETuO7GAkCCSWbeiwJiZgWxOqHLrxPQjiGBxnSzmRYKuMr5W0EsPqia-o_RcglxbAs7gcP91JvvNJbe99kbJo02VQPZl6T6pSYpRq29csn7g0GsaVD5M03YO7eQiSFpSAURMvTEKAvBTOexZInoVHahw3lZhxbqQAI7goCxhPD8e1rULH5y_FmZDQQyvFdyC5reH32eZAmTEv8aghQN_3ZtjhiyG_Y5p-zLoGWdsjIjd3xDE2BdQpkxnLkUX6fk90ZBbPXe85VnhIr3wTZE9GCw_Jr5J-lZEglfH7VhMzlnqHzyR8SpDb7AaaoVmCfp5Qedk-uCA0A56pH-z8geX3pp_4lrBAdDgwBVTJWt75_m9IETOVw68jfE15fGazQ9sUP8bXCNtaT8rfxUgqFBzCMFzR59NDiiMwpKK91PO7h9IXXLQ2jCIcEBSYP67YUGfYiygSIfCjV4bbESXSWXcyimIoBFlwLVZ2kaxGzMytwzeXD2J13THbE0tiGZoxNTj_e5clV-11sBxscBhWIQYRXeJRmwY8AwU-y-pYAdDsGaSMBOH-_ou1Y0Pbj7xt-Xy-D1Q9so-aYZvvgRaLJCz8lbXRzhKJjW6xpW1p1Vj9g5opkLlXWxzwUWB2oHZj88W_VjBeqlIPvthoNF8-seED1ljq8MGeKJWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 آلية اتصالات تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75991" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75988">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGBolSMxbvl13LeNRTitYWpZW2WHlhCjM7Xwxy952KutaEhcCMY-UKCWumCgheMSiog26VP_0tChGXvtc6jNGxljeRY-B80M5n2jZSiQNnSoRZike7fobfyud6msdu6dKpRxzq8fOE4mnAcPmdHwZ3-VAc9VOXVrTICYjy5QmPYQw_l7TKl3qmjbyYlAixHQCG8X5hYZ9pC99VQugKszUvUKAoKbvuKJi-4gBbuIL6YoysF3cQM3XMqvuUWJj-WK0BhrQIN5omc1JjUMejRCrGM0fTCgPMw23HHz7UGTE9vynJY4BzVVHIuFoSLgQs4AH59gLBM3jcyGe5LJgowf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_5exEGxTBgxeS2We-SWD-YTi2FUoAuhJD7HPogUBfDpm19Vm25p9bMa6mjkE5AeDLzpU5iln1XwObuVfKc7uqgwMIeptoCvpiRJk5RoJhbH1Vsthn09Ej8HEgCAW31gVnxSuug_lvGhzdrOMTsxiWF0jv4UuUeTPZRiBdBewcLnfvtCdO1wmuHiN4cwl7_yYt5PG6LoI0mKyes1WQlWvmTkyvcRwcOekl2yO6JOxuUWW__BPKNkzBEKf4Qp-e92kdMTFr65yE_vDnXmXjYNZt3T4DPyz3U6t934drLybT9lHF-O8Gq4DYiUUDcTg9tGsLqcjeQJ8JQN41K_e-iLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYso8YS6rvZI5UbXlxzr_uVn988XQdw2ic9jYjnp9WGf_JKrJqutWAqBlA-Ca0VKFJsXwBQ3iQBokQCukHXHkJYb4rzUmhrrn2523DoKYClL0JQubrHedESjGkoM18WHjKWmuNZIdeDLXWsAjfyBDJ9Dejiv85TckGX3i4ZZik6kDG3L62HqAHWIuQ81caxlxjIqXRTzlPsAqscc_kAjIcaNa7p-J68Fw5Buasp4iTBY3fBdjC1-NZboDyRkp8lht1mg75m21b_kQjqoH0XnUznCNrrzac4YNVYfBVmFTGs-GGS6jKnZWvi54NILTiWlRgS5PMRevYo5ITMYbcj3AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
ابطال الحشد الشعبي يسعفون اخوتهم في جهاز مكافحة الارهاب بعد ان انفجرت عبوة ناسفة عليهم.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75988" target="_blank">📅 14:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎤
فوكس نيوز:
الاتفاق المتوقع ينص على بقاء القوات الأمريكية بالقرب من إيران لمدة 30 يومًا.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75987" target="_blank">📅 14:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75986">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
حكومة البحرين الجائرة تصدر الحكم المؤبد لتسع افراد مدعية تخابرهم مع الحرس الثوري الايراني.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75986" target="_blank">📅 14:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75985">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8621a769e.mp4?token=b4vMXsdEG6-xEmSIf99syu-U3ZK2GiN50sK6FPBADTmWOwHT71au-Rv0IuRSX6Fv8_xUfGHJFivu2VVJMO-snkZdDtX-LXFAMc4o8ODVmKLf2ZqpWt9oKDx70tgT6TeH9Bd4inO2ETdbjNdygwzUSYX68iLX3Rogk6Ej6arqYfXFOzjwYsFSN7rywMLwd429JmjPTUkkDOJnxi_DbSDBz2TwftiPRgwn3qERprC5kTVpiP4BILQgHNdGFJaQa3C55MF1Pca7I0XwOQoBWPDF-LmG9q8dlVl3nlTct_CmokBC19tYGEDzouaxNLBSOVK3sZvkEbsmpJqwAadAKt5Tpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8621a769e.mp4?token=b4vMXsdEG6-xEmSIf99syu-U3ZK2GiN50sK6FPBADTmWOwHT71au-Rv0IuRSX6Fv8_xUfGHJFivu2VVJMO-snkZdDtX-LXFAMc4o8ODVmKLf2ZqpWt9oKDx70tgT6TeH9Bd4inO2ETdbjNdygwzUSYX68iLX3Rogk6Ej6arqYfXFOzjwYsFSN7rywMLwd429JmjPTUkkDOJnxi_DbSDBz2TwftiPRgwn3qERprC5kTVpiP4BILQgHNdGFJaQa3C55MF1Pca7I0XwOQoBWPDF-LmG9q8dlVl3nlTct_CmokBC19tYGEDzouaxNLBSOVK3sZvkEbsmpJqwAadAKt5Tpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
أحذية شهداء الجيش اللبناني أمام مبنى مجلس النواب في العاصمة اللبنانية بيروت، احتجاجاً على مشروع قانون العفو العام.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75985" target="_blank">📅 14:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🌟
🇮🇶
جهاز مكافحة الارهاب:
يعلن استشهاد 3 مقاتلين وإصابة 4 آخرين بانفجار عبوة من مخلفات داعش في صحراء الحضر جنوب غرب نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75984" target="_blank">📅 13:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 18-05-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي عند خلة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75983" target="_blank">📅 13:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94daa968c2.mp4?token=pjys7Do70LWb-WnaOBB0vKcuIBbkemvqA341RX11TLq0jvEwZj_yEgt-FsWk5p5UVn3tDTbtVRJtqUzklHFIrHyNh5esa6FAjt14FYNdEtM89Q2khtsg85RZpmPbilwgCvQ5L9XBR8Kll75Hs0z21smuvWi2gdUrzSR_I_Sj4bzThUvvhP9MIaL_3McWLEHmkIvfJjrsSchjjQjzs3q2LR7sFc-lpohAtigLdJrl0R0Mfmc2Olf3-DAoQpr4iL3It-1dt4xD2U4mmkwG5sR4ir75vIMA8k_pvDE1nyIU2bOTgf44Oh3ZuxEX5EH3mzOepGnXWJiuTQL1nuvACRtaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94daa968c2.mp4?token=pjys7Do70LWb-WnaOBB0vKcuIBbkemvqA341RX11TLq0jvEwZj_yEgt-FsWk5p5UVn3tDTbtVRJtqUzklHFIrHyNh5esa6FAjt14FYNdEtM89Q2khtsg85RZpmPbilwgCvQ5L9XBR8Kll75Hs0z21smuvWi2gdUrzSR_I_Sj4bzThUvvhP9MIaL_3McWLEHmkIvfJjrsSchjjQjzs3q2LR7sFc-lpohAtigLdJrl0R0Mfmc2Olf3-DAoQpr4iL3It-1dt4xD2U4mmkwG5sR4ir75vIMA8k_pvDE1nyIU2bOTgf44Oh3ZuxEX5EH3mzOepGnXWJiuTQL1nuvACRtaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 20-05-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي في بلدة حداثا جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75982" target="_blank">📅 12:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
إعلام خليجي عن ‏مصادر رفيعة: الاتفاق المبدئي المحتمل بين إيران وأميركا سيحمل اسم إعلان إسلام آباد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75981" target="_blank">📅 11:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75980">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
انفجار لغم أرضي في منطقة الطيب بمحافظة ميسان جنوب العراق ؛ مقتل شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75980" target="_blank">📅 11:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75979">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📰
رويترز عن مصدر إيراني: طهران لم توافق على تسليم مخزونها من اليورانيوم عالي التخصيب</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75979" target="_blank">📅 11:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📰
إعلام إيراني: في حال الاتفاق على المذكرة سيتم إعلان انتهاء الحرب بين الولايات المتحدة وحلفائها ضد إيران وحلفائها على جميع الجبهات</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75978" target="_blank">📅 10:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75977">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
أنباء عن سماع دوي انفجار في محافظة السماوة جنوب العراق دون معرفة التفاصيل.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75977" target="_blank">📅 10:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75976">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
في هذه الأثناء تزور صواريخ كنجال الفرط صوتية الروسية مدينة كييف   الهجوم الروسي يندرج ضمن رد موسكو على الهجوم على بناية سكنية للطلاب في جمهورية لوغانسك التابعة لروسيا.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75976" target="_blank">📅 10:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc1dc9836.mp4?token=osG4K5txiiMbBDbWqhjqSdxMzhkX4rKEynO-BisZCDYRTuG0a1Y_jfbYCUKlNAjGScYRDcVSk0SxgOYN2PRzllINWHGq-mU-2GL50s4tMDH84LZzUY2u574I9OdwKxGQVlEcE6osdGFMuAjnnGhM8hwolzWAtvjqXie1Y4mw78eTm1SvdCd507BHF7vu2ySJBga41UiEBfJQk8d5ZZ-s9Qh4WISIcUkpccKtDWS6EkLitHS9SjFpLlN-sdPIZUFNO1Q0CO8qNmTWurRvxQRZfGyR5H7YfGu2dCyJaCtQePgbXHaFDeNN4v03rtXFgusYFF4Mlg8vzjH2kZCfHD5Hpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc1dc9836.mp4?token=osG4K5txiiMbBDbWqhjqSdxMzhkX4rKEynO-BisZCDYRTuG0a1Y_jfbYCUKlNAjGScYRDcVSk0SxgOYN2PRzllINWHGq-mU-2GL50s4tMDH84LZzUY2u574I9OdwKxGQVlEcE6osdGFMuAjnnGhM8hwolzWAtvjqXie1Y4mw78eTm1SvdCd507BHF7vu2ySJBga41UiEBfJQk8d5ZZ-s9Qh4WISIcUkpccKtDWS6EkLitHS9SjFpLlN-sdPIZUFNO1Q0CO8qNmTWurRvxQRZfGyR5H7YfGu2dCyJaCtQePgbXHaFDeNN4v03rtXFgusYFF4Mlg8vzjH2kZCfHD5Hpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
في هذه الأثناء تزور صواريخ كنجال الفرط صوتية الروسية مدينة كييف   الهجوم الروسي يندرج ضمن رد موسكو على الهجوم على بناية سكنية للطلاب في جمهورية لوغانسك التابعة لروسيا.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75975" target="_blank">📅 09:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75974">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن مصدر إسرائيلي: الاتفاق المحتمل مع إيران سيء</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75974" target="_blank">📅 09:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdaad755f.mp4?token=Wr-_cygfiVqldibRg2A5fQEuA9GG03pm6wvBsVGxzw1OlB2pk1opsUzyONi01NPJdkAh5zkKWlspYAQMWhPu8dXIoIGnDHum8RJMuR3b55a-2sOhGZPtvx58bpSd2sLe7DhoKKpgPUEtwePYGocX6mX0Ewu6RbGOdQAnMkQkY4Uba_oHmawfhCquqogEcgI4pwsZFNO43PQTEK-sPbkVYw98Cxy8jixM56f3z9krdy1A9M9Vuqoy1pY8aolejzzzvnY8FLvay6FikmOATs9o6-94ZxmRvMVbS_cOH25SigJPoO0BjayRasJVrxMx6adUt2sWeeFBFdw7wFE0QQwmFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdaad755f.mp4?token=Wr-_cygfiVqldibRg2A5fQEuA9GG03pm6wvBsVGxzw1OlB2pk1opsUzyONi01NPJdkAh5zkKWlspYAQMWhPu8dXIoIGnDHum8RJMuR3b55a-2sOhGZPtvx58bpSd2sLe7DhoKKpgPUEtwePYGocX6mX0Ewu6RbGOdQAnMkQkY4Uba_oHmawfhCquqogEcgI4pwsZFNO43PQTEK-sPbkVYw98Cxy8jixM56f3z9krdy1A9M9Vuqoy1pY8aolejzzzvnY8FLvay6FikmOATs9o6-94ZxmRvMVbS_cOH25SigJPoO0BjayRasJVrxMx6adUt2sWeeFBFdw7wFE0QQwmFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
مقتل ما لا يقل عن 20 جنديًا باكستانيًا بعد أن استهدف قطارًا يحمل أفرادًا من الجيش الباكستاني وقوات حرس الحدود في كويتا، جمهورية بلوشستان الباكستانية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75973" target="_blank">📅 08:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏴‍☠️
إعلام العدو :
تتضمن مسودة مذكرة التفاهم بين الولايات المتحدة وإيران إنهاء القتال بين "إسرائيل" وحزب الله في لبنان. ووفقًا لمسؤول أمريكي رفيع، أعرب نتنياهو عن قلقه خلال محادثة مع ترامب، لكنه تقبّل موقف الإدارة الأمريكية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75972" target="_blank">📅 08:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu3crL_s8fJ1yqMugSgLJB8c3GHaWxsKrY2Cmse6fRx2OBFQ0eIQsISVVbsZTWzkolpbRjLUWfq17Y-ehE21Lwe6Mv6A_ROcdIWwH-jecYfd-ZmAUbFDnoyuAVh62uPMdZrr3q9ksdk8SpgWHbk382GBySW4q8Cw1MEGb2cy4_fNechtrYlpxxbAKeAUBWpZMu1Bdtoq81KNN0TgpxZEdYDifpbxlAVLfWmZztju8FZlbI3gdzqpBz8Ocs2TJnJrhgdlut671EtFGpNIh6toe2n5c1OwnqyV_EhnMJcw_l-_duSrBysrb-qyvPcIhV0NnHSpbi-cWrPhb62DzJpwKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يشكر الخدمة السرية بعد إطلاق نار واشتباكات قرب البيت الأبيض</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75971" target="_blank">📅 08:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75970">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
🇷🇺
على غرار التحذير من العراق   السفارة الأمريكية في أوكرانيا تنشر معلوماتٍ بشأن هجوم جوي محتمل كبير وتوصي السفارة، كعادتها، المواطنين الأمريكيين بالاستعداد للاحتماء فورًا في حال صدور إنذار جوي.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/75970" target="_blank">📅 01:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUK49HmARHw5qNpRizfgCTYcxCk7XyALHcI5wRklwxTMMEilnvgSrufrfAYwJHvlSa88rArnaZLnK0CpGxh9HU1ck_GUpXcq4smU0Cz4dozMSlcp2PtLrbuOT0mGhNhEmIgpiCq0b5uMd_fOcLdmDE6UdQgoWoWLFUOnqPwlZliCLVbdAVxVIvlVpHSDNQv6qioAdlpz9y22oAVnXRcJ95DHMcj1lwd0RWj-0ZneHUr3Z30mkAA5XgKLMkNwDyHP7MI3DStwRPaRJEYYrx2utb4n16pgWYSJrQAHigE4qhNy6drhxZnwHnLJG6o3aoWqwgFOZMWwxZv8XoOFoNGwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو : ترامب يعلن الاستسلام أمام ايران .</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/75969" target="_blank">📅 00:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75968">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
🇷🇺
على غرار التحذير من العراق
السفارة الأمريكية في أوكرانيا تنشر معلوماتٍ بشأن هجوم جوي محتمل كبير وتوصي السفارة، كعادتها، المواطنين الأمريكيين بالاستعداد للاحتماء فورًا في حال صدور إنذار جوي.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/75968" target="_blank">📅 00:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75967">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b8d79693.mp4?token=d6uW9vQN8E77jjImRI5GgQGWa96WU1zlrJrLxpVl27aSdnEj2dnC1Wjyz7WowE6FsJqN9pnyNwVemFNB_X5DaBiOnFvdSIW8Tg3HHaWYSsDIr80foZPall8Y1HxcIUbVJTDwfjiQdRceUZiBf5wpaPuhwQWM8i4CNnqOOjOEoNK-j7cD6JdBOZTwFP7VwfE7wWxwsZyfk5KdbQWJSLDTRPJwPNptu6L0ewTwzjW9VgOPkF1Q-RrmOVmOiwnfCSUEWwaTtr1_qGrZWyZhT7pmFOvVOS3RKqoF7ivRNPUZat-oBdn6FBqOmSmrAMrP-Xwl5n-v0WIQ0Bf2-D8Tlh_yl5FQ9jSQNZUAtz0sbfVAg5VMfqcOGAWlhIDefG-I-jqNFAEMbJGSe94wwNsr7Puw0IQFI0eCyiSj-pkwRPQACnOcqa5wZcDjizcUNuUIcPppxN4Y7S94y8LLSRzlZEBjxX2ZSoPCKThXQcer1RzB1YJsAyt_L-h2SqeKm_tRiL5CuKwnxaBeFb2uVzfmFj7onvlkHw0mzjqA4ugeNmkmYx3YCgLbmFxUP1R3ZCZe5aoDAnz9AJOFu7bbDuCVbA3h3YkGiAteACeKAiIj-1w8j60xex5DJfUIuPJnWyce568iRxrrQIZJ3lK_YhtfBMPl5JTUtZqyFpEyt4g8rCCwfrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b8d79693.mp4?token=d6uW9vQN8E77jjImRI5GgQGWa96WU1zlrJrLxpVl27aSdnEj2dnC1Wjyz7WowE6FsJqN9pnyNwVemFNB_X5DaBiOnFvdSIW8Tg3HHaWYSsDIr80foZPall8Y1HxcIUbVJTDwfjiQdRceUZiBf5wpaPuhwQWM8i4CNnqOOjOEoNK-j7cD6JdBOZTwFP7VwfE7wWxwsZyfk5KdbQWJSLDTRPJwPNptu6L0ewTwzjW9VgOPkF1Q-RrmOVmOiwnfCSUEWwaTtr1_qGrZWyZhT7pmFOvVOS3RKqoF7ivRNPUZat-oBdn6FBqOmSmrAMrP-Xwl5n-v0WIQ0Bf2-D8Tlh_yl5FQ9jSQNZUAtz0sbfVAg5VMfqcOGAWlhIDefG-I-jqNFAEMbJGSe94wwNsr7Puw0IQFI0eCyiSj-pkwRPQACnOcqa5wZcDjizcUNuUIcPppxN4Y7S94y8LLSRzlZEBjxX2ZSoPCKThXQcer1RzB1YJsAyt_L-h2SqeKm_tRiL5CuKwnxaBeFb2uVzfmFj7onvlkHw0mzjqA4ugeNmkmYx3YCgLbmFxUP1R3ZCZe5aoDAnz9AJOFu7bbDuCVbA3h3YkGiAteACeKAiIj-1w8j60xex5DJfUIuPJnWyce568iRxrrQIZJ3lK_YhtfBMPl5JTUtZqyFpEyt4g8rCCwfrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على الرغم من تنفيذ حكومة البحرين حملة اعتقالات كبيرة للشيعة ومنعهم من مواكب العزاء.. شيعة البحرين يكسرون القرار الجائر في ليلة استشهاد الإمام محمد الباقر (عليه السّلام).</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/75967" target="_blank">📅 00:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75966">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامب:  «أنا في المكتب البيضاوي في البيت الأبيض حيث أجرينا للتو اتصالًا جيدًا جدًا مع الرئيس محمد بن سلمان آل سعود، رئيس المملكة العربية السعودية، ومحمد بن زايد آل نهيان، رئيس دولة الإمارات العربية المتحدة، والأمير تميم بن حمد بن خليفة آل ثاني، ورئيس الوزراء…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/75966" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75965">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RedfnGdMGIX-2ZB83fEbA5lxKFTE1zm4wwBLwE458UgmdYLgHydAFeAguGctNQVclJ6bJOx7dWwGU1BpOfj9p6ff2qYptmz5FOgxxcKFX3KrEHWlyFuF1j8WUyBvuFfLLCPP0iAGAu4iExjycc9pzZFeuLeuXrcT09qTqFU0jOiZZJDewbTYpyHVzWWOgl_u8KrRSnIpCFpCEuZv-hMxPw1TJtNmvm30XfCul9L9d-a09m1PbvguVSRaNC2jCp7g1FbEoSOFqRKCtcV4sqtuyF9b22AHZytpqzcPUsbIBAOncRrgpF6cM0HLreL_6leTHDPPEdamEycuenllcrPfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إسماعيل بقائي: ‏
في
الفكر الروماني، كانت روما مركز العالم بلا منازع. إلا أن الإيرانيين حطموا هذا الوهم؛ فعندما زحف ماركوس يوليوس فيليبوس (فيليب العربي) شرقًا ضد بلاد فارس، لم تسفر الحملة عن انتصار روماني، بل انتهت بسلام قائم على شروط ساسانية: كان على الإمبراطور أن يرضخ!
﻿</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/75965" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75964">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/75964" target="_blank">📅 00:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75963">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttjUkPwPnLW3WlACHcHEL73W8EHLaIui-oSQEmEBp0kPGEd0sDx9ShXqjHwlS_XROM2W_smthQ7-lJmVMl8a8LncpbY9uMdUBh-hRGxwOd8YI10yk06oPzm1u2ndEsxlxZQZGSUATDsnT1RNyrJSauNWbDwpme34w6GV1WOkaaYUEXgCXYr3H1SbXXwFv3AZRQYUBIx6Ze35g8hc0UhGi1JOljUjMGl7hVhfSkmxDQBJTQPaauXTwHSeahYevXRW5-lYMzE5kMNNFXOD36iaCqkzcg2UkQs3UENIJz7PDErf-QtjSDGa-neyt9arxvWrSH0dLvFzP7Xjq8__-_mqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب
:
«أنا في المكتب البيضاوي في البيت الأبيض حيث أجرينا للتو اتصالًا جيدًا جدًا مع الرئيس محمد بن سلمان آل سعود، رئيس المملكة العربية السعودية، ومحمد بن زايد آل نهيان، رئيس دولة الإمارات العربية المتحدة، والأمير تميم بن حمد بن خليفة آل ثاني، ورئيس الوزراء محمد بن عبد الرحمن بن جاسم بن جبر آل ثاني، والوزير علي الثوادي من قطر، والمشير سيد عاصم منير أحمد شاه من باكستان، والرئيس رجب طيب أردوغان من تركيا، والرئيس عبد الفتاح السيسي من مصر، والملك عبد الله الثاني من الأردن، والملك حمد بن عيسى آل خليفة من البحرين، وذلك بشأن الجمهورية الإسلامية الإيرانية وكل ما يتعلق بمذكرة تفاهم تتعلق بالسلام.
تم التفاوض إلى حد كبير على اتفاق، وهو بانتظار الصياغة النهائية بين الولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية والدول المختلفة المذكورة أعلاه.
وبشكل منفصل، أجريت اتصالًا مع رئيس الوزراء بيبي نتنياهو من إسرائيل، والذي سار أيضًا بشكل جيد جدًا.
تجري حاليًا مناقشة الجوانب والتفاصيل النهائية للاتفاق، وسيتم الإعلان عنها قريبًا.
وبالإضافة إلى العديد من العناصر الأخرى في الاتفاق، سيتم فتح مضيق هرمز</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/75963" target="_blank">📅 00:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75962">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiMLbJ_WLSWO_4YrXiOujSr3j615FrwB_XuKm9R_9McXbrsC1enbmmB1T1iL6UWeoOzn-qGvOPyrXM__wA-9R3FFUafT_t40Wq6HsJSfdydsRitBq1-yDHbY4DjQ84Exr-oU7axPrA6SdmKWnkclsrnyx2tiAIu3VwfboE4r1pTwZzg2wD1E_CezXZhtsYodjn7oAvezTRJn4tpeT1czwPQDVrUu4kH9UQrOLGzQVULXKsw5v4fF0PMWRpCjbBATB5GcEd1QpsSlZzXUm4URn6o8wZQ2_Z98JXSyGoQhkK2tDZWMqTcgBPBorp8pJd2sqx03XKM6af-ZyM_UGgU95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة تزود أمريكية تطلب نداء استغاثة في سماء الأردن بعد ان انطلقت من مطار الملك حسين ..</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75962" target="_blank">📅 00:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75961">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75961" target="_blank">📅 00:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75960">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75960" target="_blank">📅 23:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75959">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75959" target="_blank">📅 23:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75958">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
استهداف مقر حزب الحرية المعارض في قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75958" target="_blank">📅 23:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75957">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">على الرغم من تنفيذ حكومة البحرين حملة اعتقالات كبيرة للشيعة ومنعهم من مواكب العزاء.. شيعة البحرين يكسرون القرار الجائر في ليلة استشهاد الإمام محمد الباقر (عليه السّلام).</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75957" target="_blank">📅 23:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75956">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzzlY4bXGhm6amZO3_bfuUfTvi_IdgtTSZ8v3QwBSpOZeqkmmJe5392H3BWTT_XotXAjcRaBargMj5mh92fDcuAWsKqA3wZDw9WztwAyYomAHPcdaQlke5z9nvPipDIqbeS8Bg_hoT9FiT_7aJC-Mm_N2G2pcfaCivIzIpqW402WjncpFGbx-mli6Ghz4ikCtBjJMrCNZaiyTnGaw6yOeTB2HVsZygM_ZHfM1spg9xZI1PFgCdTHmr4Xo6WhlCyPMHS9PFO-5DJR1_Hdt3uNl59SmWlEyXPDMKQs3tNMTJQ35LBlYE5hKj39X0_up_xsVM5Moi81wHD2eAsHei8Yww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: أليكس ميلر (23 عاماً) جندي اسرائيلي يقتل نفسه بعد إصابته بصدمة نفسية حادة، وسط تصاعد الحديث داخل إسرائيل عن التأثيرات النفسية المتزايدة للحرب والخوف من هجمات المسيّرات التابعة لحزب الله.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75956" target="_blank">📅 23:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75955">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4228c26c11.mp4?token=OwQ89XFmrkdPoXGmRu1HZ3VGgO88bl4E9RQT0OWwjbgm8CdM8n4qdwLjAyPYGgz7ZZtbEL4FAO6dZeRnXbCtC3AziQ6cgKRF8qInHDGMUrL4usalxPMDNisuVIRoFX8OLLQHfu88ncDtT7NIYVHvAChKh36Ylqxevm83LvIdswtYpoZ-Anm_CB4KShl7C9YfxN7KVDYpa3X36lpZ0v_A3V2Tr4Ymf6je2xkUmTEMMIFPo_KkSLs_7HCwiLKIuz2spscLNa5sN_zczvBwmvizGASSMm7NLu1FEmnv8kM6D36crn1a3pvzEM3OUqN6KZe5vlyWtj5Eair05SNXzqnoUIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4228c26c11.mp4?token=OwQ89XFmrkdPoXGmRu1HZ3VGgO88bl4E9RQT0OWwjbgm8CdM8n4qdwLjAyPYGgz7ZZtbEL4FAO6dZeRnXbCtC3AziQ6cgKRF8qInHDGMUrL4usalxPMDNisuVIRoFX8OLLQHfu88ncDtT7NIYVHvAChKh36Ylqxevm83LvIdswtYpoZ-Anm_CB4KShl7C9YfxN7KVDYpa3X36lpZ0v_A3V2Tr4Ymf6je2xkUmTEMMIFPo_KkSLs_7HCwiLKIuz2spscLNa5sN_zczvBwmvizGASSMm7NLu1FEmnv8kM6D36crn1a3pvzEM3OUqN6KZe5vlyWtj5Eair05SNXzqnoUIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 16-05-2026 آلية "نميرا" تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75955" target="_blank">📅 23:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75954">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
🏴‍☠️
حدث أمني صعب يتعرض له جنود الاحتلال جنوب لبنان وطيران الإنقاذ يجلون جنود مصابين.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75954" target="_blank">📅 22:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75953">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📰
‏FOX NEWS: محادثة ترمب مع قادة الدول العربية كانت "إيجابية جدا"</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75953" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75952">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70dd906bcd.mp4?token=cd6rT6SUJX7QyoQ0EdtE7g0MfA1L3whzUzzGVuJGKKzb7MxPkFa5zcwPwLfbdYWMKg2KSl9PN_61jhsioqt1dk9AzwJzIJ6beTspVPxhg2DubGYjoe-GslEzaoqy8xbXXfC7k-48grDKi2uoEZAN4H9L2aq8DSvgsKL7raakwOXnW2ekk8_2lLQcR94z9juwcPtu4X_c_-H2xifV0h-CRwkklCXUhX9IelMFlNwmNtI09gnFq6cIeS4rN6IHTVF4c1Args5PUyBx33b9elPlShHQTUHZrVQ93J0Jd1GrtBWaFYnMb25Nr0h0HoN9jkYIpgDUNjLuP2NK6V9QDioPiFqU6L0gbLQ_hiErG2p1UDwmegk-pjSNpFHSJy36GfT5IGL6EoBmWD57i-hlyqyS_mvgrSbbSPMgfAWj6JO3_GqZuUsjOjDXiunjPm_c2rkAKOe2u-AW4DeFN30K3sSGkZ94WilcYddEGH-OxY9xme7qZCSC9fERzmboIXcbrpHOEDboww4BxY19E3blvSYcKZh1NvlGiAvE3nwlY9aKNIO0NGlJakMl5751M2V1gUX9F4B4k7-JK0a-xvfHe-TbMBbZpM4YbCUjc-kl3G0GRBxvEp3SIX2Rw3qWzuIgRkXjiV-r9rp07ViCJyA-X-gc7YYvfdNhv1H7Bca2zNcyL8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70dd906bcd.mp4?token=cd6rT6SUJX7QyoQ0EdtE7g0MfA1L3whzUzzGVuJGKKzb7MxPkFa5zcwPwLfbdYWMKg2KSl9PN_61jhsioqt1dk9AzwJzIJ6beTspVPxhg2DubGYjoe-GslEzaoqy8xbXXfC7k-48grDKi2uoEZAN4H9L2aq8DSvgsKL7raakwOXnW2ekk8_2lLQcR94z9juwcPtu4X_c_-H2xifV0h-CRwkklCXUhX9IelMFlNwmNtI09gnFq6cIeS4rN6IHTVF4c1Args5PUyBx33b9elPlShHQTUHZrVQ93J0Jd1GrtBWaFYnMb25Nr0h0HoN9jkYIpgDUNjLuP2NK6V9QDioPiFqU6L0gbLQ_hiErG2p1UDwmegk-pjSNpFHSJy36GfT5IGL6EoBmWD57i-hlyqyS_mvgrSbbSPMgfAWj6JO3_GqZuUsjOjDXiunjPm_c2rkAKOe2u-AW4DeFN30K3sSGkZ94WilcYddEGH-OxY9xme7qZCSC9fERzmboIXcbrpHOEDboww4BxY19E3blvSYcKZh1NvlGiAvE3nwlY9aKNIO0NGlJakMl5751M2V1gUX9F4B4k7-JK0a-xvfHe-TbMBbZpM4YbCUjc-kl3G0GRBxvEp3SIX2Rw3qWzuIgRkXjiV-r9rp07ViCJyA-X-gc7YYvfdNhv1H7Bca2zNcyL8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 04-05-2026 آلية لوجستية "هيمت" تابعة لجيش العدو الإسرائيلي في موقع المنارة على الحدود اللبنانية الجنوبية بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75952" target="_blank">📅 22:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75951">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d0057e37b.mp4?token=K1Lqj0S-pUIdSmLpo80y7J1q857zsWV_YXkR5m4emtwzRxaIRaIahi9Fc0MTGCc2gY3nVlDj_0IyE3J4K67FZKYCU3SNZaErnuL6-zvhEmS7JXB8yKHvLSgZjVJJemhqelJp2tw1ByOujuUo8Xr9KV3TghL2v9hqzDMATP_zRBQ_vLHFaBDDemFdr_4P-PWPxC1RKhBLvDWc1ddg3Q3YHd0MJa1qy_r7wiyGWSXYwPB6mhUBj2byLhAMqyCLngL2vRemuU3CrRlejdbBEzuciwKe159zkAPUY5qFfc7I1IvXSDorSFyTzUVFqvNbMEZmIIdW4Q0RPGsAPhx0Ql0_Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d0057e37b.mp4?token=K1Lqj0S-pUIdSmLpo80y7J1q857zsWV_YXkR5m4emtwzRxaIRaIahi9Fc0MTGCc2gY3nVlDj_0IyE3J4K67FZKYCU3SNZaErnuL6-zvhEmS7JXB8yKHvLSgZjVJJemhqelJp2tw1ByOujuUo8Xr9KV3TghL2v9hqzDMATP_zRBQ_vLHFaBDDemFdr_4P-PWPxC1RKhBLvDWc1ddg3Q3YHd0MJa1qy_r7wiyGWSXYwPB6mhUBj2byLhAMqyCLngL2vRemuU3CrRlejdbBEzuciwKe159zkAPUY5qFfc7I1IvXSDorSFyTzUVFqvNbMEZmIIdW4Q0RPGsAPhx0Ql0_Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استهداف مقر حزب الحرية المعارض في قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75951" target="_blank">📅 22:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75950">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5151e44404.mp4?token=QW59ZT-G6uA3EBqePU4ywwJ2OupwkeKItQcH6TrZVVB3G7aQTNPJlamfi4IOPf9cXUa7RQM4WmNvb2_7xvlg1W1onFP9OyEUc1pPtEs8InN7I62YuaVphJf0lVlIbFYqEpuapfeH42AkMwC-t6qmH7xgZ6tlbk-ir1l4VGVqaNxfNtpmhjUojdBh9KRLNdnIvDvi47F5HR5UDvHlv2-BDam-s4aLgZDTaKoXxDx0OTHs47WRRXkbxfj48QQQFqXysImN8gFrRuwisKQB3ENCaYj-6SI2tgMZif1qYl5KGugtg98DznXD-cMVDWSu5FqFg8c_JKambclHrwAMuBLE1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5151e44404.mp4?token=QW59ZT-G6uA3EBqePU4ywwJ2OupwkeKItQcH6TrZVVB3G7aQTNPJlamfi4IOPf9cXUa7RQM4WmNvb2_7xvlg1W1onFP9OyEUc1pPtEs8InN7I62YuaVphJf0lVlIbFYqEpuapfeH42AkMwC-t6qmH7xgZ6tlbk-ir1l4VGVqaNxfNtpmhjUojdBh9KRLNdnIvDvi47F5HR5UDvHlv2-BDam-s4aLgZDTaKoXxDx0OTHs47WRRXkbxfj48QQQFqXysImN8gFrRuwisKQB3ENCaYj-6SI2tgMZif1qYl5KGugtg98DznXD-cMVDWSu5FqFg8c_JKambclHrwAMuBLE1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استهداف مقر حزب الحرية المعارض في قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75950" target="_blank">📅 22:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75949">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f4151d37.mp4?token=OkoxkPLRYIQPYwGgl6iyiwsVx75vG5hfttNIpuRC51Wwfil2zGbR-YI6yKb04iypneT0c_l8ppBqLmRhEAM8OxpSR-25yBSwLPn53IOfKPBzcmphX2hwSKsxmk_qsUJ9sg2is5_pD877AMHrvFop_T1y2ZiUjhWj-E9ryVAMJvPTpeaHQ2WYYpEY0xrDG-LCCpo5Q_rd6DyWdHkvEgXEoP-iQoDZIdTAU7MLdSRTH9sRkJ_CyHSPXQaO7YguKwsk7MOg8duwKTtK_PBFArqEBQdP39WivRfcvEXySxvIpe8aFpdziaW5Y_-gB64xYl2QZ-66vvlg7T_e2Sty-MDVYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f4151d37.mp4?token=OkoxkPLRYIQPYwGgl6iyiwsVx75vG5hfttNIpuRC51Wwfil2zGbR-YI6yKb04iypneT0c_l8ppBqLmRhEAM8OxpSR-25yBSwLPn53IOfKPBzcmphX2hwSKsxmk_qsUJ9sg2is5_pD877AMHrvFop_T1y2ZiUjhWj-E9ryVAMJvPTpeaHQ2WYYpEY0xrDG-LCCpo5Q_rd6DyWdHkvEgXEoP-iQoDZIdTAU7MLdSRTH9sRkJ_CyHSPXQaO7YguKwsk7MOg8duwKTtK_PBFArqEBQdP39WivRfcvEXySxvIpe8aFpdziaW5Y_-gB64xYl2QZ-66vvlg7T_e2Sty-MDVYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تحليق طيران حربي أمريكي فوق سماء قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75949" target="_blank">📅 21:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75948">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">واشنطن تايمز": الولايات المتحدة وإيران ستعلنان عن اتفاق سلام خلال 24 ساعة</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75948" target="_blank">📅 21:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75947">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdIBf-nY04BdXNJGcJSuF4xIipCiL_CrzpscPTtLOQJbt4nGjc6xlBLorTI-68FLZmQrIlpvchg-y7S5g7sP2jIGHGkKgO3zvzdahtFIDUTqcQVdKV32zbtoaAt0uadX_Q0DfQusQZC3AZ-gW6Q4vx4yiw4VYWcDu_kZ4emZgDd6iZgPFtUn-vBa6ut14MQFLdrgEOL4D3F13CbDYv4mkmHWoR5nlUTJZQElv5nxzW66SwOnkApPJZ1SzAgvhjHun3blGP8lvywEg1jZ_CS3lpCTgJl3wp7xNIiOdeVyHpux8nFO7vLjy-PMQemyeMyoMOJAzBbPAz-s8NgOsaOIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: نوام هامبورغر، 23 عامًا، من عتليت، مقاتل في تكنولوجيا وصيانة في الكتيبة 9، قُتل جراء انفجار طائرة بدون طيار في قاعدة شمال البلاد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75947" target="_blank">📅 21:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75946">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbbjqkE7bAvAmju2eZSPmW4O2gNSMk43H8od6Hav3ue7KYhP1gytXHU5mmTjYnv2xUxgJvuF3JZXEhV2xCb5OtxveWFwvsO3dTRD2zT8GPPC8llDDbJOLUz70mUov9V4PSAsEDXYeYl-eu1SCI8WSkmPVi4flHMEwKi7EVwWMYs58Yf5HpuAKZvCSU2TysZxQ4a8CXA42TywM4VowRbtiffLyJlVDynObGG0iNZMLLo5A6rHBa8ABwzi_Xkvj_I9tPXmbubAhuPd7A-BVmTq2FQ7BrK2Z-Gv5ZEwg5yOqy39L8Y8uQITs0ALWQ0jwNrzQs3fO7ut_3Crquw8T9y5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
شكرًا لك أيها الرئيس أردوغان!
«الرئيس ترامب هو الزعيم الذي انتظره العالم لقرون - إنه لا يتحدث عن القوة فحسب، بل يجسدها.»</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75946" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75945">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📰
رويترز عن مسؤول أمني باكستاني: يجري وضع اللمسات الأخيرة على مذكرة تفاهم لإنهاء الحرب بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75945" target="_blank">📅 20:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75944">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📰
‏مسؤولون إسرائيليون لـ أكسيوس: نتنياهو حث ترمب على استئناف الهجمات ضد إيران</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75944" target="_blank">📅 20:25 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
