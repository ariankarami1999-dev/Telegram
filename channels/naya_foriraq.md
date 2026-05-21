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
<img src="https://cdn4.telesco.pe/file/gKmQdUj6gXJnq02NxBNx0GUGkkOVC6Mtof2ecxXSjv7XZ9fLRQoKKMbziou0g5499tXBhLY1jos78Vyal1dZyStECim_5GzGdtqpGDHM8lazeV3vXIA-L0i3oHIQQMFWEkQvbYqyPHaNY1abb7oaz6DRQlWfkX5zHS2tAweiLxTbi_mSPtTZf2iYJnlbiwB6si9E-LMt0Pbr4Nb5TbCUVRKiwxg9jPkRqmaf2cQFObAJqw6BmaLw4D8i0C5qluh7I4NnCLIxvuw3iKvImJwG-XPNdfbTPtit2P8CeznP2aHHEnyZsfnKCBr44N1LVsbhsoMngqACNczChFnXDT3B7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 10:14:44</div>
<hr>

<div class="tg-post" id="msg-75794">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇪🇸
وزير الخارجية الإسباني: ترحيل 44 من نشطاء أسطول الصمود من إسرائيل إلى إسبانيا عبر تركيا مساء اليوم</div>
<div class="tg-footer">👁️ 912 · <a href="https://t.me/naya_foriraq/75794" target="_blank">📅 10:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75793">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن ضباط كبار:
لا جدوى من البقاء في لبنان والجيش لا يحقق إنجازات في هذه الحرب بشكلها الحالي
مهمتنا غير مفهومة ولا نعرف إن كان الجيش يريد وقفا لإطلاق النار  في لبنان
لا يوجد وقف إطلاق نار في جنوب لبنان لكن لا يمكننا تفعيل كامل قوتنا
هناك تحديات كثيرة في الجبهة اللبنانية فإما أن تسمح لنا القيادة بالعمل أو ننسحب</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/naya_foriraq/75793" target="_blank">📅 09:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75792">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-vNn50y9E6xbmqU-HBFOmfTTR3VppMgINDNNLRWopFj74gbvRf6twX5oNfgQGzGpz_m6Qkgsb7j5VBGzc5SDEIuJC6wFZUNMkJG0tahvfBP15Q7JELi0ruKVle_6ybnwzTYwmxQJNfj8QbxEi6goPZ7RIIp_Unn6xHTGMYQYvvcqDNd_HhCoHGQheqAqYNnE83pDoOOQVV7KgbKiy-u5lv54kVLAbN2O6C-E3JcnuMbtfpWX6wATjlqTbYdqIn56m_V-CvGqdJqITp0BveAaG2vYE7qviJybirwkNGX5j5xpGxedfB7uhL8B0MGgrOS7tpaZ95Y3aBNpJ11egN_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو
في تلك الأيام، في مثل هذا الوقت: عشية عيد الأسابيع (شفوعوت) عام ١٩٨١، دمر سلاح الجو الإسرائيلي
المفاعل النووي العراقي
. زجّ الهجوم "إسرائيل" في جدل سياسي، إذ كانت آنذاك في خضم حملة انتخابية محمومة للكنيست العاشر. اتهمت المعارضة بيغن بالتضحية بالأمن والمصالح السياسية في سبيل الدعاية الانتخابية.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/naya_foriraq/75792" target="_blank">📅 08:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
مساعد قائد البحرية في الحرس الثوري الإيراني:
أيدينا على الزناد وإذا كان ترامب يظن أنه يستطيع فتح مضيق هرمز بالقوة والسفن، فعليه أن يعلم أن البحرية نفسها التي زعمتم أنها دُمرت ستُغرقكم في قاع البحر.
على أعدائنا أن يعلموا أنهم مخطئون تمامًا إن ظنوا أن هذه الأمة ستتراجع بتدمير بنيتها التحتية، فقد أثبتت هذه الأمة على مدى 47 عامًا أنها قابلة للتدمير لكنها لا تستسلم.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75791" target="_blank">📅 23:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية يطال عجلة تابعة للقوات الأمنية في مدينة سراوان بمحافظة بلوشستان جنوب شرق إيران ؛ إستشهاد أحد أفراد الأمن الإيراني كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75790" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGR58ax5-XUxnIJhQzQQkLruW_b-9FK6fuNCdrQPi4QP-Z7LU6ABdGgVeGalNfpiLP9GS-OcoV85Sd3MYTI8g8UfsWistRIV0QmaVkiyF9AdrQIT5qA7uXFH3pb_o6SUcOE4v0BJX5sN809USgKu6157-XR8_hVE5z1fOR0An2W1yme-onG5rp4mq9yL3ZwZfLNLd7NRO7kWzMZ2cERObR1e-1yIRtq05U_AoY9cakQSym6cW0p9KOWOqMl_NL0J968MsXn2H-p7CI7l-dvSrSyfGs0VcbjVUK-JELMEW8MOd1MmUBaybuMccRnSdkv0KnATeddFPpiLbuwYbJmppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق الخليج الفارسي:
حددت الجمهورية الإسلامية الإيرانية حدود منطقة الإشراف على إدارة مضيق هرمز على النحو التالي: "الخط الذي يربط جبل كوه مبارك في إيران وجنوب الفجيرة في الإمارات العربية المتحدة شرق المضيق بالخط الذي يربط نهاية جزيرة قشم في إيران وأم القيوين في الإمارات العربية المتحدة غرب المضيق.
يتطلب المرور في هذه المنطقة عبر مضيق هرمز التنسيق مع إدارة الممرات المائية في الخليج الفارسي والحصول على إذن من هذه المؤسسة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75789" target="_blank">📅 23:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ddf11200.mp4?token=N3mhVe8IDJbXgn6q_FuaHu4VV4A80fQNbGBABxW9tlDvD5xVxbV8hSxI40qAp_wJ-NNDbgV9NhE4ZW725RlvibclVtYbUWfBKnPaxSmo5r1dCrYIudyzH8P0Ro_7CwgGDG2VNJETAiIHBL7D4MlQ67v5mHMeumWiDu8Fyl1AwyJqSraZL1nqloAskGFOumnyc8OlTvcAtscZguwgoHF5emPkddGt0yTVy6EpGk-hUIQTm0-FFme8VOyDi2rYVwKQe_NpjGCknznNVfxUce7ayJIrJQW6cnWIds7RX1DBsawZgWnC8DIPXPMO7lpwgaABoNjBt_VM2s9HghtgH7-DSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ddf11200.mp4?token=N3mhVe8IDJbXgn6q_FuaHu4VV4A80fQNbGBABxW9tlDvD5xVxbV8hSxI40qAp_wJ-NNDbgV9NhE4ZW725RlvibclVtYbUWfBKnPaxSmo5r1dCrYIudyzH8P0Ro_7CwgGDG2VNJETAiIHBL7D4MlQ67v5mHMeumWiDu8Fyl1AwyJqSraZL1nqloAskGFOumnyc8OlTvcAtscZguwgoHF5emPkddGt0yTVy6EpGk-hUIQTm0-FFme8VOyDi2rYVwKQe_NpjGCknznNVfxUce7ayJIrJQW6cnWIds7RX1DBsawZgWnC8DIPXPMO7lpwgaABoNjBt_VM2s9HghtgH7-DSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوالف الگهوة   من منزل العامري ، طرح مبادرة اليوم تتضمن صلح وبناء الجدار المتصدع داخل الإطار التنسيقي في العراق..</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75788" target="_blank">📅 23:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bhg7lLgh65EeQX68hls6GPuKSaII-xuZeywJEtZ9ovoXlRFSxP0WY0aUAJJT5USNqeDWltnX9COTj54B6dlpG6VqQMle6VHctp_taMbIKm0Vm2qYqGYSVTKIb0LHXzJA48jCBlxGbOXr92oMkGsbocKKpkJ8OuXrtUSvLJsgK-zKzmgdBhPJyxbq-yUs9JljOWKcqJxUbiJZ37S6pxW2ZcLAf8zVcA_AzWbQdyOY7lDc5UaUOuI07-YO-RFssRNBRw1HeJ2pTTgy3-cxtkDX0JhFXqxReJNt6pEDScJEY1-HTWdNFJf4rrKZJnFCxNYiPBDcZNW7oCd-Bnujoilgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة   من منزل العامري ، طرح مبادرة اليوم تتضمن صلح وبناء الجدار المتصدع داخل الإطار التنسيقي في العراق..</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75787" target="_blank">📅 23:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭐️
هجوم صاروخي جديد يدك مقرات المعارضة الكرادية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/75786" target="_blank">📅 23:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭐️
توثيق يظهر تصاعد أعمدة الدخان من مقر تابع لحزب الكوملة الكردي الإرهابي في محافظة السليمانية بعد دكه بمسيرات إنتحارية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75785" target="_blank">📅 23:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092cf934a6.mp4?token=WkflnzkcGTUSwAm3vEOlYOkXl0QH2OemOfTD8C1tGhInVkKpleHGAO31KcbzvMt3fgJwNzu_oaeOO-ce_Tjh4s5n3qX0Lo9tPSDtSIZ1yVkPGN7PWIcYDclxJ7vgb6pQ10cWjz0I3U-S2-KTQl3_xecLFqo5clFj3TrOrXHPOQuNYZFmWGhrI4lxucuPbK2Sd9-vlQRPehQqQneZfX1jvY9JwVc4qJfGoB9_oSKjZl2aNPmhTiNuJKl90IXIIXtimC50wqjtz4Udqng0lvz64QdQWW2EPVyQI1JSoBYNVrl1xQuQrD7zZ6YVE-ZTiB61_DaDtPZNJG8ibjipe56XgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092cf934a6.mp4?token=WkflnzkcGTUSwAm3vEOlYOkXl0QH2OemOfTD8C1tGhInVkKpleHGAO31KcbzvMt3fgJwNzu_oaeOO-ce_Tjh4s5n3qX0Lo9tPSDtSIZ1yVkPGN7PWIcYDclxJ7vgb6pQ10cWjz0I3U-S2-KTQl3_xecLFqo5clFj3TrOrXHPOQuNYZFmWGhrI4lxucuPbK2Sd9-vlQRPehQqQneZfX1jvY9JwVc4qJfGoB9_oSKjZl2aNPmhTiNuJKl90IXIIXtimC50wqjtz4Udqng0lvz64QdQWW2EPVyQI1JSoBYNVrl1xQuQrD7zZ6YVE-ZTiB61_DaDtPZNJG8ibjipe56XgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجار جراء هجوم بطائرة مسيرة انتحارية استهدفت مقر تابع للمعارضة الكردية (الكوملة) في محافظة السليمانية ضمن اقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75784" target="_blank">📅 23:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f0661e65.mp4?token=GzP_IfvTaeHGhPXHMIUPteBnT-3YO143jTQrpyc8l9jv1Z1y6cduoWZy10dBI0jbtvlRnndg6cyNg9S3UdEVxTOjZmuBlFyPcR158wNdsbjQTmx-4SgTwqo7O6O3leipiJAZQljFMLkQSFxdk1GiJztUJ-fYkTHxIe8s41sqaF0OgDppnuNAkFbXSarZZ5Vfqlh42lmslROZIuUNfXTc7rS_0eaVZmEOUz8gdqsKk0WjbH9T00_ObxOzEEQInAaBHBVR5NBAcMLEUiGQgwCHgPB5UxNwkTzcxokyg8kePfN0-WUzcIxXLZr6rFM2HX854SodXfnTtG5sEiaEQdR9Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f0661e65.mp4?token=GzP_IfvTaeHGhPXHMIUPteBnT-3YO143jTQrpyc8l9jv1Z1y6cduoWZy10dBI0jbtvlRnndg6cyNg9S3UdEVxTOjZmuBlFyPcR158wNdsbjQTmx-4SgTwqo7O6O3leipiJAZQljFMLkQSFxdk1GiJztUJ-fYkTHxIe8s41sqaF0OgDppnuNAkFbXSarZZ5Vfqlh42lmslROZIuUNfXTc7rS_0eaVZmEOUz8gdqsKk0WjbH9T00_ObxOzEEQInAaBHBVR5NBAcMLEUiGQgwCHgPB5UxNwkTzcxokyg8kePfN0-WUzcIxXLZr6rFM2HX854SodXfnTtG5sEiaEQdR9Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مواطنة جرينلاندية تهتف ضد مبعوث ترامب إلى جرينلاند "جيف لاندري" وتدعوه إلى ترك بلدها والعودة إلى منزله.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/75783" target="_blank">📅 22:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الصهيوني:
إصابة 7 من ضباط وجنود الجيش (بعضها حرجة) نتيجة سقوط طائرة بدون طيار مفخخة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/75782" target="_blank">📅 22:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228ceb0fe.mp4?token=EDMOcQLf9k-7QAL8i5S8M2BPOm2BwHl-BlSti1BwpftF7bw7xVZpS87jTNoF2JcsdndlBnodcobTqnVntumrcri5GC9TepS2rdH_jI8M8BfZvoSvOGak54kZE7Lm-v6M-FXkA2NGRRTTW_6qucn58Xj8yYnj9QdA8u1xoYysOhp6hT0oBBZ0LuZpQXVLvvc_2q2KIbnJNPez3am6pDRKNgRRrLLiNB7QCYkgja9TaWetoObLyeee8rhzsyH55I9QAhYKmZImmeheXByXv7gz6HQHVrGbs4YQrPoROuBruKufePNjD3atGaY28wazl79jvJXIxjD5VyTMzzXnJLfHVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228ceb0fe.mp4?token=EDMOcQLf9k-7QAL8i5S8M2BPOm2BwHl-BlSti1BwpftF7bw7xVZpS87jTNoF2JcsdndlBnodcobTqnVntumrcri5GC9TepS2rdH_jI8M8BfZvoSvOGak54kZE7Lm-v6M-FXkA2NGRRTTW_6qucn58Xj8yYnj9QdA8u1xoYysOhp6hT0oBBZ0LuZpQXVLvvc_2q2KIbnJNPez3am6pDRKNgRRrLLiNB7QCYkgja9TaWetoObLyeee8rhzsyH55I9QAhYKmZImmeheXByXv7gz6HQHVrGbs4YQrPoROuBruKufePNjD3atGaY28wazl79jvJXIxjD5VyTMzzXnJLfHVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران حربي منخفض في أجواء محافظة الموصل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/75781" target="_blank">📅 22:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
الله أكبر.. استهداف قوة مشاة ودبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة حداثا من قبل أبناء نصرالله.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/75780" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f088d5ca1a.mp4?token=li82aT1b4S4b1Bn-MhBKI2qtxVXc05u0JsIeGFzUNuJcmw2NqF7EJTEiwdjuh1-uLYozkw1QY1Nb2brQxYSUAdFB5aPJlDaXWt7Ji4P0DuVV8-vV4AoA2JQ_xHCWre-ifRmAId1dsuRRn81vLjdY_C2-sVLuTdlm-Qh196sQSBHjuMeYHfthhuhONfFowIJvvOHhdvQ9YmqB4aHTm85YgA-eMv3prTr2g59UzBTSe8xcErbzzWzKDPXD2ze-ru-0ctuW3-uEY5dAtdi4HEK6OlLFwMtnTHB4u8J-RMOXBVTWR3a6icRG2Fvxmu3ukM0mc8ZRPYjEAcsr1L_Sn6NhG2oXsgw7HU5elYby8n4U_B13IV5FMgFIMecAJvnd6WzKNdOzpuC3JVP72Gmvcw9aa2ib_AzrBAGoKzuMSWAS-WbtPVOBg0WHBAYhlRnDp4tAGxoBdK-MZa3dFJQOZyDKH9PV4wxap7FnQdGlSV6PiGjvuzpV7Q1Hn1nwsJuZdZPcjP2qYoTByIIEkIEaJet-z_MGgJGvaFAM7HgBW4bYMR4xMc6nez4Dki6LNFNLjjO_tiPzubE53G5zvV5rRrW3dGqctFe35HRx3SUotkpy8mXC8HuqivUh_Lk0HLZAWSjgwETiQDSudCd5pukx2DGsyxjjsflwZRR7i8AMzvMftcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f088d5ca1a.mp4?token=li82aT1b4S4b1Bn-MhBKI2qtxVXc05u0JsIeGFzUNuJcmw2NqF7EJTEiwdjuh1-uLYozkw1QY1Nb2brQxYSUAdFB5aPJlDaXWt7Ji4P0DuVV8-vV4AoA2JQ_xHCWre-ifRmAId1dsuRRn81vLjdY_C2-sVLuTdlm-Qh196sQSBHjuMeYHfthhuhONfFowIJvvOHhdvQ9YmqB4aHTm85YgA-eMv3prTr2g59UzBTSe8xcErbzzWzKDPXD2ze-ru-0ctuW3-uEY5dAtdi4HEK6OlLFwMtnTHB4u8J-RMOXBVTWR3a6icRG2Fvxmu3ukM0mc8ZRPYjEAcsr1L_Sn6NhG2oXsgw7HU5elYby8n4U_B13IV5FMgFIMecAJvnd6WzKNdOzpuC3JVP72Gmvcw9aa2ib_AzrBAGoKzuMSWAS-WbtPVOBg0WHBAYhlRnDp4tAGxoBdK-MZa3dFJQOZyDKH9PV4wxap7FnQdGlSV6PiGjvuzpV7Q1Hn1nwsJuZdZPcjP2qYoTByIIEkIEaJet-z_MGgJGvaFAM7HgBW4bYMR4xMc6nez4Dki6LNFNLjjO_tiPzubE53G5zvV5rRrW3dGqctFe35HRx3SUotkpy8mXC8HuqivUh_Lk0HLZAWSjgwETiQDSudCd5pukx2DGsyxjjsflwZRR7i8AMzvMftcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: نقوم بتحرير كوبا وعلينا مساعدة الكوبيين فليس لديهم طعام ولا طاقة لكنهم شعب عظيم.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75779" target="_blank">📅 22:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامب: نقوم بتحرير كوبا وعلينا مساعدة الكوبيين فليس لديهم طعام ولا طاقة لكنهم شعب عظيم.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/75778" target="_blank">📅 22:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d5c56470.mp4?token=TbDEG2PNi8RJFZZniLgj-FvfvuXnSoMHGyyzbV-PIks6qvVsz9KmV0vbDuajYKW9bZQPqWX0Enf1Ds3VCAQC1pyeFT8fECupkqo3PN91yDjRzkycsPoOHZDwOjI9MHUNiaR3giUGzqeCJCmz27sHF-ibS9WfQtR6a4mNafw6pVpUioqNv2tVgwnP5iRY87WBzkgSsZNANb5euCAvYfxyHOK_Cb08SwC1_R-wDf5cUg5KU8oUid6yHvWiuUpFJ5W9u8w0ZI1Blqd8tCJL9GeYsLnyaQIeb-i2HzCw5U2Kseq0YLlpMDLOtjKAwX1jQ5ymqisNbpaUol6s1JS6GL9IMapTutjinAT34YsJwHLAgEOnoBLLQYKr1Ki-kwypm7A9yJIQx2cgO4P8DVGhxK4BNUWgzOuIP1KrE92QztBf4mLm87pRWqGhKgfYx9pS_nmG3qk0TuKUThm_pXH-kwY7ZpYl9kAe-LJ7UWWbw664Ek8P-skgb16LHEae77GiPbrRf4TGae9g6xG0204f_Tras4sKZnF43gcJb9dt-8uFHIwvgKt7CIhsjbJ6YsN41O97jmo2sRenr33becWidxs8MRZ4jA6BtVwp--6vbjble--HEoSWzqJVax0IQ-daZCdkW-Px9ZojsvbF8-cdnI5FNKS1U9bk161ARMDYjVtOsHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d5c56470.mp4?token=TbDEG2PNi8RJFZZniLgj-FvfvuXnSoMHGyyzbV-PIks6qvVsz9KmV0vbDuajYKW9bZQPqWX0Enf1Ds3VCAQC1pyeFT8fECupkqo3PN91yDjRzkycsPoOHZDwOjI9MHUNiaR3giUGzqeCJCmz27sHF-ibS9WfQtR6a4mNafw6pVpUioqNv2tVgwnP5iRY87WBzkgSsZNANb5euCAvYfxyHOK_Cb08SwC1_R-wDf5cUg5KU8oUid6yHvWiuUpFJ5W9u8w0ZI1Blqd8tCJL9GeYsLnyaQIeb-i2HzCw5U2Kseq0YLlpMDLOtjKAwX1jQ5ymqisNbpaUol6s1JS6GL9IMapTutjinAT34YsJwHLAgEOnoBLLQYKr1Ki-kwypm7A9yJIQx2cgO4P8DVGhxK4BNUWgzOuIP1KrE92QztBf4mLm87pRWqGhKgfYx9pS_nmG3qk0TuKUThm_pXH-kwY7ZpYl9kAe-LJ7UWWbw664Ek8P-skgb16LHEae77GiPbrRf4TGae9g6xG0204f_Tras4sKZnF43gcJb9dt-8uFHIwvgKt7CIhsjbJ6YsN41O97jmo2sRenr33becWidxs8MRZ4jA6BtVwp--6vbjble--HEoSWzqJVax0IQ-daZCdkW-Px9ZojsvbF8-cdnI5FNKS1U9bk161ARMDYjVtOsHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
16-05-2026
آلية هامر تابعة لجيش العدو الإسرائيلي في اسكندرونة ببلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/75777" target="_blank">📅 22:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن إستهداف وإسقاط مسيرة صهيونية من طراز "هرمز 450" بصاروخ أرض جو في القطاع الأوسط اللبناني.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/75776" target="_blank">📅 22:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭐️
إنفجار جراء هجوم بطائرة مسيرة انتحارية استهدفت مقر تابع للمعارضة الكردية (الكوملة) في محافظة السليمانية ضمن اقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/75775" target="_blank">📅 21:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-OfHfNx8-ahEIIRjN3zkLhEBoi7MhVdwH2lXx2OcHLpxQewKLKJVPJj9ZNrC340SiBYuWWqomS8JgjEIzMhB-PfUCjyLYaUNJdMvNfF-2s5t7Z5mcrOrrhV8yf-RmhPaP0B-tCqV7EM6cXAAk3LuxQCPKf2I5DDiHqxxHKNIdvuxRd_q8162CjzeeHD9CDJ22TYy4T_AtwYrnw0_6wllgq_oxGW29ZdXKPCkLS3A0G1_jGsSVZD1qvYSItJ6Sr3ssXfk1cjNeDxRDbFlT0HBZSz2lTQrUXPDOMkM1MmAcToOQ3vXaU_GgcqHNBUfXpAbujzl6dSgLJ58uEaBkbpqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إن الأمريكيين، بعد إرسالهم رسالة إيرانية من 14 بندًا قبل ثلاثة أيام، أرسلوا رسالة أخرى إلى إيران عبر وسيط باكستاني. تدرس إيران الرسالة ولم تردّ عليها بعد. يسعى الوسيط الباكستاني في طهران إلى تقريب وجهات النظر بين الرسالتين. لم يتم التوصل…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75774" target="_blank">📅 21:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75773">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الإسرائيلية: نتنياهو يحاول إقناع ترمب بمنح الضوء الأخضر لاستئناف الحرب على إيران.  ‏نتنياهو لم يكن على توافق مع رأي ترامب بشأن التفاوض مع إيران.   ترامب يميل لدعم توجيه ضربة عسكرية لكنه لا يزال يترك نافذة ضيقة للمفاوضات مع إيران.   إسرائيل تتخذ…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/75773" target="_blank">📅 21:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75772">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
🏴‍☠️
محرقة جديدة للميركافا.. حزب الله يعلن عن إستهداف 3 دبابات ميركافا وجرافتين D9 تابعة لجيش الإحتلال الصهيوني في بلدة حداثا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/75772" target="_blank">📅 21:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: استهداف دبابة ميركافا وإعطابها بواسطة صاروخ موجه في جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75771" target="_blank">📅 21:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75770">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8a416d9e.mp4?token=ieMSFbn9siTihmouoZbE0UPGqhHsUm4e5TiyokTH4TqRuKS_7AHWclro0rIak4kkKZpSCt722FJrZWgI1pX_m-Gm0DyUDkv-8paNc8So50p4x3ok9uUEb7gfEQVmXjVbWz_TIKHufxtCGmeitYee1H4HOU8j0oWmuzxW9j-dw6KQkETrR-3JiNm3MVxvk1epaUcigdTLjYZsVmpuYNx-JuY4y4lXXTg1QNdLmETKgB4E3BnBVdudmeyUuqNEnXjzaIYES-KJfkQQyneo-9MtKIgEJmBPxPowD0OYSSlzv9Gfu6yIj5JAAYHUV6BG_j0JAAqxQkFd2ypavQ0bZ8A1mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8a416d9e.mp4?token=ieMSFbn9siTihmouoZbE0UPGqhHsUm4e5TiyokTH4TqRuKS_7AHWclro0rIak4kkKZpSCt722FJrZWgI1pX_m-Gm0DyUDkv-8paNc8So50p4x3ok9uUEb7gfEQVmXjVbWz_TIKHufxtCGmeitYee1H4HOU8j0oWmuzxW9j-dw6KQkETrR-3JiNm3MVxvk1epaUcigdTLjYZsVmpuYNx-JuY4y4lXXTg1QNdLmETKgB4E3BnBVdudmeyUuqNEnXjzaIYES-KJfkQQyneo-9MtKIgEJmBPxPowD0OYSSlzv9Gfu6yIj5JAAYHUV6BG_j0JAAqxQkFd2ypavQ0bZ8A1mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
نيابة عن شرفاء العالم..
ناشطة تبصق على جندي إسرائيلي أثناء اختطاف نشطاء "أسطول الصمود" السلميين والتنكيل بهم.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75770" target="_blank">📅 21:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الإسرائيلية: نتنياهو يحاول إقناع ترمب بمنح الضوء الأخضر لاستئناف الحرب على إيران.  ‏نتنياهو لم يكن على توافق مع رأي ترامب بشأن التفاوض مع إيران.   ترامب يميل لدعم توجيه ضربة عسكرية لكنه لا يزال يترك نافذة ضيقة للمفاوضات مع إيران.   إسرائيل تتخذ…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75769" target="_blank">📅 20:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏ترامب: رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه  متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75768" target="_blank">📅 20:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75767">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff7f595ec.mp4?token=CBLGrAYuw89kmkvQXu-daj7rRXgwVes_JHMhAnlXjEjl4oEopEVfbk0tB1d9P_WGzwSXu-V5FhWOM2_SFkSsGurhRczkMQY7lqE7hPxZTv8Tj-hE5c0fn3WfM00oat8iaSH-QJMhMyZf7F93oHOqEvrJMu1xmnLU1peOjz9289g3likzSXn5ynmUiu1o3YPKHWNIB5jcE42_De72U4-ifEj4gfxr47xf1UbCG8dSUFc4-rV55yajLICI3eg3soKNGpeu7kMFYAT3hVlbYKwVW8UkhBdoVm1p2QcpdCN317OQXuQHmAZ--3CfP-0ZFKOTyjjlHN90xhvP0vSczKP3_1jy_m0Xlwr4iqlzDRZSYoKoSew-lOacv62hyAL8IiFlOTU-NL1l9OqYsjcl-K9Wm_1k3kpWuCk4B5-oC6URhITgyFXudtsA3hD71YHnwZv_cp1XTa-3U436dknjQ2mL_ySvw6Z6XIHUqW5nPQvDp9r07wI8CyRoH5kvpTXTb6Lm_9teJtuaBnEUNxBnt6_dtHFVOGJahzTAhkNoZW5NAfRpj5qflpUvmJbWFmFBAqfBn3t0hCeVBs5JEQyBqLrBQLl97aSfvbUZyenXIEpaaN9IWd8LzFaqYbDXug2sWkHAVsUu4TRY2QEMIm1hNzSJ13RU4Q5d23uMIYLcWFsAPlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff7f595ec.mp4?token=CBLGrAYuw89kmkvQXu-daj7rRXgwVes_JHMhAnlXjEjl4oEopEVfbk0tB1d9P_WGzwSXu-V5FhWOM2_SFkSsGurhRczkMQY7lqE7hPxZTv8Tj-hE5c0fn3WfM00oat8iaSH-QJMhMyZf7F93oHOqEvrJMu1xmnLU1peOjz9289g3likzSXn5ynmUiu1o3YPKHWNIB5jcE42_De72U4-ifEj4gfxr47xf1UbCG8dSUFc4-rV55yajLICI3eg3soKNGpeu7kMFYAT3hVlbYKwVW8UkhBdoVm1p2QcpdCN317OQXuQHmAZ--3CfP-0ZFKOTyjjlHN90xhvP0vSczKP3_1jy_m0Xlwr4iqlzDRZSYoKoSew-lOacv62hyAL8IiFlOTU-NL1l9OqYsjcl-K9Wm_1k3kpWuCk4B5-oC6URhITgyFXudtsA3hD71YHnwZv_cp1XTa-3U436dknjQ2mL_ySvw6Z6XIHUqW5nPQvDp9r07wI8CyRoH5kvpTXTb6Lm_9teJtuaBnEUNxBnt6_dtHFVOGJahzTAhkNoZW5NAfRpj5qflpUvmJbWFmFBAqfBn3t0hCeVBs5JEQyBqLrBQLl97aSfvbUZyenXIEpaaN9IWd8LzFaqYbDXug2sWkHAVsUu4TRY2QEMIm1hNzSJ13RU4Q5d23uMIYLcWFsAPlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
17-05-2026
تموضع لوجستي تابع لجيش العدو الإسرائيلي في اسكندرونة ببلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75767" target="_blank">📅 20:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75766">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73f31002da.mp4?token=f9GtIQDJrrZWSuTAQz4QJqBUnqVYI2Mh45tLojbcSZEs2H6C_723QOp6_YDsr5pChjUTFvgec1RKoSTeOYb_pm4hPTNDaNEgjuE_GGEFSIluYn0qMDaMfE9zztCRIoTPTsCvgUvKAfvKKsLxZuiOsg2ioYn9SAiyJfJB61--YH1ESNhtKIfgllMYt3qzvFEmx_5Nr0GHE5FvvOjmqBY3-sh3MK58jkaes7fmjDxSFUIRGhNiIiWVbSiKD2P4Llu04olN8nv4AkQPm9bdBFGkXIDqe_Xvpm1sGVoIdV-4MERFwkEKZrtlyozkBMeIA2KEzhzmCdmU966VNA9sLatwAzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73f31002da.mp4?token=f9GtIQDJrrZWSuTAQz4QJqBUnqVYI2Mh45tLojbcSZEs2H6C_723QOp6_YDsr5pChjUTFvgec1RKoSTeOYb_pm4hPTNDaNEgjuE_GGEFSIluYn0qMDaMfE9zztCRIoTPTsCvgUvKAfvKKsLxZuiOsg2ioYn9SAiyJfJB61--YH1ESNhtKIfgllMYt3qzvFEmx_5Nr0GHE5FvvOjmqBY3-sh3MK58jkaes7fmjDxSFUIRGhNiIiWVbSiKD2P4Llu04olN8nv4AkQPm9bdBFGkXIDqe_Xvpm1sGVoIdV-4MERFwkEKZrtlyozkBMeIA2KEzhzmCdmU966VNA9sLatwAzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية تزعم:
في وقت سابق اليوم في خليج عمان، استولى مشاة البحرية الأمريكية من الوحدة البحرية الاستكشافية الـ 31 على سفينة النفط التجارية M/T Celestial Sea، التي ترفع العلم الإيراني، والتي يشتبه في أنها حاولت انتهاك الحصار الأمريكي من خلال العبور نحو ميناء إيراني.
أطلقت القوات الأمريكية سراح السفينة بعد تفتيشها وإصدار الأوامر لطاقم السفينة بتغيير مسارها.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75766" target="_blank">📅 20:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75765">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
نركز حاليا على إنهاء الحرب في جميع الجبهات لا سيما لبنان.
إذا أصر الطرف المقابل على مطالبه المفرطة فإنه يمكن القول إن الدبلوماسية لم تحقق نتائجها.
الحديث عن الإنذارات والمواعيد النهائية بشأن إيران أمرٌ سخيف.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75765" target="_blank">📅 20:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75764">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⭐️
رويترز:
بعض السفن تدفع لإيران ما يزيد عن 150 ألف دولار لضمان مرور مضيق هرمز.
‏رسوم عبور السفن لمضيق هرمز لا تفرض على كافة الدول.
‏الآلية الإيرانية الجديدة في مضيق هرمز تعطي الأفضلية للسفن المرتبطة بروسيا والصين.
‏"وثيقة الانتماء" التي تقدم للسفن مقابل عبور هرمز تؤكد عدم ارتباطها بأميركا أو تل أبيب.
‏الدول التي ترغب في عبور سفنها مضيق هرمز يجب أن تتصل بوزير الخارجية الإيراني.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75764" target="_blank">📅 20:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75763">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⭐️
إستمرار موجة الإنسحابات..
النائب "حسن قاسم الخفاجي" يعلن إنسحابه عن تحالف الإعمار والتنمية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/75763" target="_blank">📅 20:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75762">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2e4689c.mp4?token=X8YDH7K9w0Jcz0C-3viUmFioKJtwNRdDTV2-2b60HrzSQ-Hbxb3QuWakbfrxCpx77b1gT66IaPCSxJPyzdy9Dtv2NvDaXV70PgSNFRaeOh53WifRKLHGzYG94IIFMTkrcTfBr_ZsnMcp3JuEJn2G8ccXMQ2UtIEKl7swN4gKh1i8W1rs2V1ExgSx01fxUVVQ8lwYXliSXwal_heTGsd0AXIM0hq1hpiOHIoA5BWdihma-TkUxeo9v32Ff1LJza7fLj2xvzXK0wtl-rU6MPRgfc58rdkbkm-F3JIid-B79C7jnIExIlzrijbpNrPh97qrfRNH3gE-EEfG7i9zbHSDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2e4689c.mp4?token=X8YDH7K9w0Jcz0C-3viUmFioKJtwNRdDTV2-2b60HrzSQ-Hbxb3QuWakbfrxCpx77b1gT66IaPCSxJPyzdy9Dtv2NvDaXV70PgSNFRaeOh53WifRKLHGzYG94IIFMTkrcTfBr_ZsnMcp3JuEJn2G8ccXMQ2UtIEKl7swN4gKh1i8W1rs2V1ExgSx01fxUVVQ8lwYXliSXwal_heTGsd0AXIM0hq1hpiOHIoA5BWdihma-TkUxeo9v32Ff1LJza7fLj2xvzXK0wtl-rU6MPRgfc58rdkbkm-F3JIid-B79C7jnIExIlzrijbpNrPh97qrfRNH3gE-EEfG7i9zbHSDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب: سنمنح ايران فرصة واحدة، أنا لست في عجلة من أمري.  إما أن نتوصل إلى اتفاق مع إيران أو سنقوم بأمور قاسية ونأمل ألا يحدث ذلك.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75762" target="_blank">📅 19:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75761">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية يطال عجلة تابعة للقوات الأمنية في مدينة سراوان بمحافظة بلوشستان جنوب شرق إيران ؛ إستشهاد أحد أفراد الأمن الإيراني كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75761" target="_blank">📅 19:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75760">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
استهداف دبابة ميركافا وإعطابها بواسطة صاروخ موجه في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75760" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75759">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93dd2e141.mp4?token=s8x8AYc_ektokuN8ahN-pPE8vyQw3lHfgIeV0iNL21GY0Wkwdl7J9WfPJeUoKTTTC12vi8hx3fR0vN07NralTFcRE985Tf7Er13hfFM688B8Yy43PK4CGGuDHqC7At-XgVXuzzDjMcU8YDGVkd4BOycstXXKAsTKTLM3xRWQ2kO64XaP0Xuzi3G6qRKkW8eDwree04tfp5Xv0UJi-5VaBZJdLtC4Ix69_HTc9d-SeGY-DF2EOUoCVuF6j_u1JhwpmAwtkypECkHZDojq2yxCua8BkypYv4BYpsQ-prXKnNdJlSAVIFl45qEpixXVfgQvIY7w6Qi9vtiLfoqdMqW7cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93dd2e141.mp4?token=s8x8AYc_ektokuN8ahN-pPE8vyQw3lHfgIeV0iNL21GY0Wkwdl7J9WfPJeUoKTTTC12vi8hx3fR0vN07NralTFcRE985Tf7Er13hfFM688B8Yy43PK4CGGuDHqC7At-XgVXuzzDjMcU8YDGVkd4BOycstXXKAsTKTLM3xRWQ2kO64XaP0Xuzi3G6qRKkW8eDwree04tfp5Xv0UJi-5VaBZJdLtC4Ix69_HTc9d-SeGY-DF2EOUoCVuF6j_u1JhwpmAwtkypECkHZDojq2yxCua8BkypYv4BYpsQ-prXKnNdJlSAVIFl45qEpixXVfgQvIY7w6Qi9vtiLfoqdMqW7cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🏴‍☠️
ضمن الإستعدادات العسكرية للعدو الصهيوأمريكي..
مشاهد تظهر العديد من طائرات التزود بالوقود الأمريكية في مطار بن غوريون الصهيوني.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75759" target="_blank">📅 18:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA9Pe9ESzTXJL989fzb5YPX12t5np8oybqZS6VOnsKi6o9gXlb5SLpb-C2dSzYS4ScbRIdagFzHJ5qOe7Oe8EvEyRc7XAV37S7vl4nP52t6IBvlgxV_OKmwZ6I9rJWYCVK23EdHCwxxDegbL4a5021WOhNekKyW0YgttKo7b97TIDi1nfFXf_oQ7zIJEZ34sQXda0RdnyVFliBpebUVgExM8zUh_YCb2QqbFyarmlSsAodNax1Bhm_bNYR7wvqC3zS-_x59w_ByPNg9rGsGS1MzabnqzEBV2QWfXyhn-KqYIUFsMA_w15NCH-7BKOFmzPLXJCDtptX6sZ-ePJR4ubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
من المثير للصدمة أن الجمهوريين احتفظوا بالموقف المهم جدا "البرلماني" في أيدي امرأة، إليزابيث ماكدونو، التي عينها، منذ فترة طويلة، من قبل باراك حسين أوباما والمجنون الشرير المعروف باسم السيناتور هاري ريد، الذي أدار مجلس الشيوخ للدوموقراطيين ب "قبضة حديدية". على مر السنين، كانت وحشية للجمهوريين، ولكن ليس كذلك بالنسبة للدومقراطيين - فلماذا لم يتم استبدالها؟ هناك العديد من الأشخاص العادلين الذين سيكونون مؤهلين لتلك الوظيفة الحيوية.
يلعب الجمهوريون لعبة ناعمة للغاية مقارنة بالدوموقراطيين. إنه أكبر عيب في السياسة. يغش الدوموقراطيون ويكذبون ويسرقون، خاصة عندما يتعلق الأمر بالأصوات في الانتخابات، ولكنهم يلتزمون ببعضهم البعض، في حين يسمح الجمهوريون لإليزابيث ماكدونوز في العالم بالبقاء في السلطة، ووحشيتنا. نحن بحاجة إلى تمرير قانون إنقاذ أمريكا، والآن - وبالمثل، قتل المماطلة، التي من شأنها أن تعطينا كل شيء! إذا لم نمرر واحدا على الأقل من هذين الحكمين بسرعة، فلن ترى رئيسا جمهوريا آخر مرة أخرى. سينتهي الأمر بالدوموقراطيين بولايتين إضافيتين، العاصمة وبورتوريكو، وكل ما يترتب على ذلك، بما في ذلك
4 أعضاء في مجلس الشيوخ، والعديد من أعضاء الكونغرس، والعديد من الأصوات الانتخابية الإضافية، وسيحصلون أيضا على حلمهم في محكمة عليا للولايات المتحدة معبأة برقمهم المفضل - 21 قاضيا.
سيقضي الدوموقراطيون على المماطلة في اليوم الأول الذي يحصلون فيه على فرصة للقيام بذلك.
الجمهوريون لا يفعلون ذلك لأنهم يقولون إن الدوموقراطيين لن يفعلوا ذلك أبدا، لكن الجمهوريين مخطئون. كن جمهوريين أذكياء وصعبين، وإلا ستبحثون جميعا عن وظيفة في وقت أقرب بكثير مما كنتم تعتقدون أنه ممكن!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75758" target="_blank">📅 18:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d89ae9e5.mp4?token=CdwpqpDDeG6FwEEeTTZwHcPlP2LZ7kWZP53Hc38R6P5KeB-GIc9iMZRYMNH9h5h1lVqXO80OA0iv2L8ZkQPG1ar6h2w1xfnoURURraRgQPFBEC8HYd0p9OaeahYH1f8UNFWhkJzCugYkpOSnSrxw4HBznJaRdxoKKTXrXVD6uHXQ3UNpvabDjgbSdpzbe9-v9-ILywEpacXCSFDAQwVquTym_Ay-jVKr0Kew27duXfRo_STs2TB-dNiOfbJT2TeWpexvsnprmg06giJKM9ICqjidPMTaVO6mRh7LkXTNQS3u1QgS8w2jdxjpmcsIiQwr4oAnktDbx4NE_CZFKgwlU5_IQlPtBAfRSBKaMTrzMfl0gRBOQjpEeJGXlufP5zEAGisduCLxqRr_bh-iG3Jfi_h9eB_4MuWq-OcNFRe4FEKemWLw5TVuYCulBtCUKB7MB_dDDrdjRLHCs98Sl0kRkcwAmYlXrF8WMColFWGepl_hBT1IL_tbUXxlCRLWB4Aw7YYK842hts6arH2P4ZcFwDMjmbRkkBbPTvaah15J2u7TugX1eKL_ZSXNPDVFO5aLdQEjDrE6S9n6uRXmtsGPyVtwOWoCoF_kMJIPYplvwcWCXwrMEYUFZ6yPiefUGX4WTI9plk_J0FAHppCSQjTUqJwwfYAHKT3-SpAz7Df2Kow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d89ae9e5.mp4?token=CdwpqpDDeG6FwEEeTTZwHcPlP2LZ7kWZP53Hc38R6P5KeB-GIc9iMZRYMNH9h5h1lVqXO80OA0iv2L8ZkQPG1ar6h2w1xfnoURURraRgQPFBEC8HYd0p9OaeahYH1f8UNFWhkJzCugYkpOSnSrxw4HBznJaRdxoKKTXrXVD6uHXQ3UNpvabDjgbSdpzbe9-v9-ILywEpacXCSFDAQwVquTym_Ay-jVKr0Kew27duXfRo_STs2TB-dNiOfbJT2TeWpexvsnprmg06giJKM9ICqjidPMTaVO6mRh7LkXTNQS3u1QgS8w2jdxjpmcsIiQwr4oAnktDbx4NE_CZFKgwlU5_IQlPtBAfRSBKaMTrzMfl0gRBOQjpEeJGXlufP5zEAGisduCLxqRr_bh-iG3Jfi_h9eB_4MuWq-OcNFRe4FEKemWLw5TVuYCulBtCUKB7MB_dDDrdjRLHCs98Sl0kRkcwAmYlXrF8WMColFWGepl_hBT1IL_tbUXxlCRLWB4Aw7YYK842hts6arH2P4ZcFwDMjmbRkkBbPTvaah15J2u7TugX1eKL_ZSXNPDVFO5aLdQEjDrE6S9n6uRXmtsGPyVtwOWoCoF_kMJIPYplvwcWCXwrMEYUFZ6yPiefUGX4WTI9plk_J0FAHppCSQjTUqJwwfYAHKT3-SpAz7Df2Kow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اعلام العدو تحت بند سمح بالنشر: اصيب قائد اللواء 401، بجروح خطيرة إثر انفجار طائرة مسيّرة مفخخة اخترقت المنزل الذي كان متواجدًا فيه في جنوب لبنان. كما أُصيب معه أيضًا ضابط برتبة مقدم.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75757" target="_blank">📅 18:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الايرانية:
المفاوضات مستمرة عبر وسطاء باكستانيين. ما نريده في الأساس ليس مطالب، بل حقوقنا. قدمت الولايات المتحدة مطالب عديدة، لكن السؤال هو: لماذا ينبغي لإيران نقل يورانيومها المخصب إلى دولة أخرى؟ لم يكن أحد قلقًا بشأن برنامجنا النووي، والجميع يعلم أن برنامجنا النووي سلمي تمامًا.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75756" target="_blank">📅 18:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
‏
ترامب بشأن كوبا:
لن تتسامح أمريكا مع دولة مارقة تمارس عمليات عسكرية واستخباراتية وإرهابية أجنبية معادية على بعد تسعين ميلاً فقط منا.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75755" target="_blank">📅 18:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75754">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌟
نت بلوكس:
تُظهر المقاييس انقطاع خدمة الإنترنت في معظم أنحاء ‌العراق باستثناء الشمال لمدة ساعتين تقريبًا هذا الصباح. تُقدَّم هذه السياسة، المطبقة منذ سنوات، كوسيلة لوقف التسريب والغش في الامتحانات المدرسية، لكنها تؤثر بشكل غير متناسب على المستخدمين والشركات.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75754" target="_blank">📅 18:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jeh9_ABjZohB7Zh7zY01h2ySNkw7h64tQNHfNLWQ0x0yaQHaShGmDk-6IgL_BHHPEXyFRNbjkfgNi9o6ht-Vmln-A9OQSFmdY-Gwvzu5K1XGdZDHkrk3g0te14FcTev68rVn4V-jc2E8kI26LOYcDklXbPDPPiG7Tak_7L4anD29sY_6p-mPgPkR6lyqb5rGYnJZCDRSDkINngzmpAuzqUHj1MekcbN51-LoDnL7aac98Jzq1pBeiyaj7-3Um5qMp9LK1aNiQqUomPVUibGuNSA0aKGVuXMDFZDFfOmMh_sF5dXdSJB9BTAp0jcj5o_iBOYThFaa5acyKQwf7YZKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسالة من مجاهدي المقاومة الإسلامية إلى سماحة الأمين العام لحزب الله الشيخ نعيم قاسم (حفظه الله):
بسم الله الرحمن الرحيم
سماحة الأمين العام حجة الإسلام والمسلمين المجاهد الشيخ نعيم قاسم حفظكم المولى
السلام عليكم ورحمة الله وبركاته
تلقّينا رسالتكم العزيزة وفيها أثر الوالد على أبنائه والقائد على جنوده والشيخ على مريديه.
نشكر لكم يا شيخنا الحبيب مشاعركم الصادقة ومودتكم الخالصة وعاطفتكم الصافية.
ونرد لكم التحية، بتحيّةٍ ملؤها إيمان وسنامها جهاد ومآلها نصر وشهادة.
كما نتوجّه بإجلالٍ وتعظيمٍ إلى أرواح الشهداء من إخوتنا المجاهدين وأهلنا الأوفياء، الذين أدهشوا العالم بصبرهم وثباتهم وصمودهم، وكانوا وما زالوا الحصن المنيع على الفتن والسند المتين في ذورة المحن، ظهر المقاومة في ميدان الدّفاع عن الوطن ضدّ الاحتلال الصّهيونيّ الغادر والهمجي.
أيها الأمين المفدى، إن أبناءك المجاهدين في المقاومة الإسلامية قد راهنوا على الله تعالى قبل حمل البنادق، وامتثلوا لأمره وتوكّلوا عليه ونزلوا سوح الوغى مسدّدين بالصّبر ومؤيّدين بالمدد من عنده، وهم في كل يوم يسطرون ملاحم التصدي الكربلائي ويلاحقون العدو بكافة أنواع أسلحتهم، يدمّرون دبّاباته ويحرّقون آلياته ويرعبون جنوده ويلقّنون جيشه دروساً ستُحفر في ذاكرته المصطنعة، ويبقون الوطن عصياً على القهر والإحتلال.
يا شيخنا، لقد فتحت قيادتكم الشّجاعة الطّريق أمام سلسلة من العمليات التي جعلت العدوّ منهكاً، يتهيّب الاستقرار فوق التّراب الجنوبيّ، قد أدمن النظر إلى السّماء، مترقّبا صلياتنا ومسيراتنا، واعتاد تنكيس رأسه في الأرض، مذعورًا من عبواتنا وكمائننا. عهدنا ما عهدتم إلينا به: سنبقيه على هذه الحال ولدينا مزيد؛ لن نهدأ ولن نستكين ولن تقر لنا عين حتى يرحل الاحتلال عن أرضنا مهزوماً خائباً، وبيننا وبينه أيامٌ لن يصبر على مدتها وسنصبر، لأننا أهل الأرض، وليالٍ مظلمة في عين المحتل أضأناها بذكر الله، وميدانٌ سيحصد منه أشلاء القتلى والجرحى، بعد أن زرعناه بالبارود والنار.
باسم حبات التّراب، باسم كل شهيد، وكل مجاهد في تشكيلات المقاومة المتأهبة على امتداد جبهة المواجهة، نجدد لكم الولاية والقسم والبيعة، بالاستمرار على هذا النّهج حفاظًا على العزّة والحرية والكرامة والإستقلال؛ فحياة الأوطان لا تُكتسب إلا بالتضحيات الحمراء، وشرف الجنوب يأبى أن يتحرّر إلاّ على أيدي المقاومين، ولن يخيب عليهم رهان إن شاء الله تعالى.
والسّلام عليكم ونصر الله وبركاته
أبناؤك مجاهدو المقاومة الاسلامية
الأربعاء 20-05-2026 م
03 ذو الحجّة 1447 هـ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/75753" target="_blank">📅 18:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75752">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الاعلام السعودي يزعم: العمل جار بجدية على وضع اللمسات النهائية على نص اتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/75752" target="_blank">📅 17:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75751">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الاعلام السعودي يزعم:
العمل جار بجدية على وضع اللمسات النهائية على نص اتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75751" target="_blank">📅 17:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75750">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏴‍☠️
اعلام العدو تحت بند
سمح بالنشر:
اصيب قائد اللواء 401، بجروح خطيرة إثر انفجار طائرة مسيّرة مفخخة اخترقت المنزل الذي كان متواجدًا فيه في جنوب لبنان. كما أُصيب معه أيضًا ضابط برتبة مقدم.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75750" target="_blank">📅 17:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤺
🏴‍☠️
اعلام العدو:
حدث أمني في جنوب لبنان.. التفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75749" target="_blank">📅 17:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ed3da2b.mp4?token=sGpYxHMErIDWhGIajMHBDqruRiyL_dCejwEsC-SNR3qEg3xZTdgwVJ13eMAtiSJXBXX0gTN4vbKGmKOOtgefjNU3VNBYl49HR0wm7-ugYVOI2LvWYZHozr1cqadV0TTFKsdCj_ezApFsOJHXVh7wgSMVpDmfwVdCx5DJ7fMA5ed2DPGFKNVVDmwb4t59eY2xjljIYbx1ecDJkKqnE33IZ3krIB6axNB8rJLtK91iob817PvvgsMc9uHghAHMVl76c-JgT5vgoZkgRLLYqxUUbZaz2yAbj4Fob2IZH_PmcGd807msGG2-CKFHRGZ_R4Wm4mSxO0gNh8PdY3C_CRympw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ed3da2b.mp4?token=sGpYxHMErIDWhGIajMHBDqruRiyL_dCejwEsC-SNR3qEg3xZTdgwVJ13eMAtiSJXBXX0gTN4vbKGmKOOtgefjNU3VNBYl49HR0wm7-ugYVOI2LvWYZHozr1cqadV0TTFKsdCj_ezApFsOJHXVh7wgSMVpDmfwVdCx5DJ7fMA5ed2DPGFKNVVDmwb4t59eY2xjljIYbx1ecDJkKqnE33IZ3krIB6axNB8rJLtK91iob817PvvgsMc9uHghAHMVl76c-JgT5vgoZkgRLLYqxUUbZaz2yAbj4Fob2IZH_PmcGd807msGG2-CKFHRGZ_R4Wm4mSxO0gNh8PdY3C_CRympw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أوباما انسحب من أفغانستان.  علما ان بايدن من انسحب</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75748" target="_blank">📅 17:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f240d29220.mp4?token=f7apRT7z71Ghwx-naj7qz9a2iXjqZJZKKLMw6Sau30BlzQJu5y-iOVZdPbZOrO89Hlm3x3EalRGKhTWVxe1XALk8WyEzJm27qM2WMCYqQ23wIzrP_jKDtkdNwG4i-soVFu8_dPFT8DpEPpgd4FsNFNx0zs95TaYjzirCI6CypiuZxyWjNETEKM4npn39Bj659GmyaLTlg_ofeBn1wmanDCLFA8UMIgSOtp6Tq4jXaL1ARZdD4yLbJwJPBw3yPzOTv86ZinPMHvSNDghVR4O-ivwPi0hpa4e20hAJY2egtAbfzyA1QMez-3np_XrKxfYzPYzCQeMT5jKR4VS7dQqmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f240d29220.mp4?token=f7apRT7z71Ghwx-naj7qz9a2iXjqZJZKKLMw6Sau30BlzQJu5y-iOVZdPbZOrO89Hlm3x3EalRGKhTWVxe1XALk8WyEzJm27qM2WMCYqQ23wIzrP_jKDtkdNwG4i-soVFu8_dPFT8DpEPpgd4FsNFNx0zs95TaYjzirCI6CypiuZxyWjNETEKM4npn39Bj659GmyaLTlg_ofeBn1wmanDCLFA8UMIgSOtp6Tq4jXaL1ARZdD4yLbJwJPBw3yPzOTv86ZinPMHvSNDghVR4O-ivwPi0hpa4e20hAJY2egtAbfzyA1QMez-3np_XrKxfYzPYzCQeMT5jKR4VS7dQqmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: لو أن يسوع المسيح نزل وأحصى الأصوات، لكنت فزت في كاليفورنيا. لكنها انتخابات مزورة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/75747" target="_blank">📅 17:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lqxc8EmeKy8rHxW1hc-ijySJrxu-9vmtSoIoDBRRm2FsbXNqP2dAYOJUqvkeNoC3VF8DOLLVlV1rj-FjBZvTpcPYeuubpLjNgE621Zx2NzZo26cY5CPgYlgdhJHSLbRVgNf_b1iSVixuPa1-R4OmeCBprPP7RjpV3AbkvWpTtSOyQVLJVVeOGe2X-SAkw8bUs89wVgk13hcwS0jp0J_ZLVXUDAf1LpkTW-4CobfJyx5Ozewd0S-kBoSKkiCTxzNalcZYqcY_HF9qxCZwtN3IQsdDifQSNfHL8kEePX9gDqVfqGls9qqk9BilwD28dSpKEjdmwGKu8XzbgFhaqa3eug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
وزير الخارجية السعودي:
نقدّر تجاوب ترامب بمنح المفاوضات فرصة للتوصل لاتفاق ونتطلع لأن تغتنم إيران الفرصة لتجنب التداعيات الخطيرة للتصعيد.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/75746" target="_blank">📅 17:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامب: لسنا على عجلة من امرنا لفتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/75745" target="_blank">📅 17:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب: سنمنح ايران فرصة واحدة، أنا لست في عجلة من أمري.  إما أن نتوصل إلى اتفاق مع إيران أو سنقوم بأمور قاسية ونأمل ألا يحدث ذلك.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/75744" target="_blank">📅 17:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75743">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏ترامب: رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه  متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/75743" target="_blank">📅 17:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5677620f9.mp4?token=bW8npgvoEjPDLwGwWPdZYcbZ6bxLx-YIFwlSt-IXkZznKD4BWBKAeK1hxAuMS0U0X8bijW569dScHLCaNTV5NdeOG6BeYH0TnsZ2YnEdyASFnNJz0TEjTYTZ3wB-jIkgupvkGZiJZz0DWjNfFDXeA7Th_FBwYrr1u8-rgMe1Zl0yoKuu6RgClKvNetMW7FuYOjUpdnn7ZP6lNmK3bxAgQdCHEwAGAJVhRJDdXebR5Zcs6HGln7LaVo8ZXjA8rWOpfThueIS6iuCMoN_io_PtbUdj5TmBlAaHQd11-vgrBtzB3FPLASnXFnGfAx4pD8Esg_uFhLltYtpWG5Yu0613jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5677620f9.mp4?token=bW8npgvoEjPDLwGwWPdZYcbZ6bxLx-YIFwlSt-IXkZznKD4BWBKAeK1hxAuMS0U0X8bijW569dScHLCaNTV5NdeOG6BeYH0TnsZ2YnEdyASFnNJz0TEjTYTZ3wB-jIkgupvkGZiJZz0DWjNfFDXeA7Th_FBwYrr1u8-rgMe1Zl0yoKuu6RgClKvNetMW7FuYOjUpdnn7ZP6lNmK3bxAgQdCHEwAGAJVhRJDdXebR5Zcs6HGln7LaVo8ZXjA8rWOpfThueIS6iuCMoN_io_PtbUdj5TmBlAaHQd11-vgrBtzB3FPLASnXFnGfAx4pD8Esg_uFhLltYtpWG5Yu0613jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب:
رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه
متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/75742" target="_blank">📅 17:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75741">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رئيس المعارضة في الكيان يائير لابيد: الهجوم الذي حدث اليوم قام به بن غفير لكن المسؤول عن هذا الهجوم الخطير هو رئيس الوزراء نتن ياهو الذي أدخل مجرماً مداناً إلى الحكومة، وكل من وافق على أن يكون شريكاً لشخص غير مسؤول بهذا الشكل</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/75741" target="_blank">📅 17:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">محمد باقر قاليباف: لا يزال العدو يأمل في استسلام الشعب الإيراني، ويعتقد خطأً أنه يستطيع إقناع إيران بالاستجابة بشكل إيجابي لجشع أمريكا من خلال مواصلة الحصار واستئناف الحرب. إن الضغوط الاقتصادية المتزايدة والحصار لن يجبرا إيران على الاستسلام</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/75740" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75739">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
‏رئيس البرلمان الإيراني محمد باقر قاليباف: التحركات الواضحة والخفية لـ"العدو" تُظهر أنهم يسعون إلى جولة جديدة من الحرب</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/75739" target="_blank">📅 17:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
‏
رئيس البرلمان الإيراني محمد باقر قاليباف:
التحركات الواضحة والخفية لـ"العدو" تُظهر أنهم يسعون إلى جولة جديدة من الحرب</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75738" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75737">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFkgOnDCTAQlTnClq4POSBFXg5CBkoFqo0WdIbxsVusStAa32z6c9qFMDnde_AKuNAP6_ONOsy4hYidP0f468G6tnzwTla4pk05kz5tKQ-c2S6-AlLPghu2r-pJEZRXBrk-q1HFUzfP3vSGwULfbV99FNF7xnVm-_DzYJmjnXr3A5p6VIhCVMHYvuPvLdlSFSBgqnDHkBM2R-DruYzWPkCDLPO9oiJAr4UqIwO0Th2vdL0TE1RHe0CkxJTuuLeu-75nGY_fgszyEPzsunm0_2-99bS9vB9vs-0lISf6G0pjY6qtUJLCl2MTgZftRyi8fPsFpZQe1JgU5PUJeoSHXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن غفير يهاجم وزير الخارجية الصهيوني: هناك من في الحكومة لم يستوعبوا بعد كيفية التعامل مع مؤيدي الإرهاب. من المتوقع أن يدرك وزير الخارجية الإسرائيلي أن إسرائيل لم تعد دولةً تُعتمد عليها. أي شخص يأتي إلى أراضينا لدعم الإرهاب والتضامن مع حماس سيُختطف، ولن نتسامح…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75737" target="_blank">📅 16:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9PNHKUegQv9IkEWX4UyT5tZkgi6Uoy77T-D8Pyvo9oxE-q64PZ08YS0pmpFBreBK3mzJ0RwkIE3vF3VWBUrryhNU5elsJMi4vtkDj1F50go0aKyDIKm9Rwfnn7Wma34t3oMu6OQWVcwjVjIZJwKy7fInWvXVD2nqRPY7EvsVETrkR234anvslW9X6LZGUS2oVBW9-76Fm2W0A1yqWpKMzzY064UZ2lz5A74CotDyw0AMRJ_QPsVRwLAeXq9EV2KBtMINN1dbbX62Qmdm1snvDjFnbJO95aNuhqNllJOgVaW8anPQDot0-AbIwjzn5CbvkoFYa8dfIqjGTsiJjpKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الاعلان عن تشكيل تحالف سياسي في العراق تحت عنوان (تحالف البيان الوطني) يضم تحالف العقد وحركة سومريون ونواب اخرين.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75736" target="_blank">📅 16:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75735">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQOSfA6HDHZqlLmwukJsNjQWHz-Qe-nox2GsxDJdK_Z3oqMglYCIjbGvKHMp4trlfCyd1BHRiOQdRoQaIUYbFwv8clblBBeYEleB9RnzYhOXEk3d9fUOVmLtjpKWFrQ07eyZWAXh7KgZLoJcsMu5V71mFUdMA_LxMqBBoTqrpieevr2wB9ogCoqVDHs0K7d682evtfrW96khtgND6dqOVYNso4E_wq6dVFRCBMGMhhkltRjzb6_ktqMkg9g0V8CCvlgFqb4YJ9u8p8v7737_2p1f7Lqru1pvp2ouzCItSE2EVE79cT9csj-86tqF_xyFH5VwHYHHqyErxLa2Gv_P-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
وزير الخارجية الصهيوني يهاجم بن غفير بعد ان كشف الوجه الحقيقي للكيان: لقد تسببتم عن علم في إلحاق الأذى بدولتنا في هذا العرض المشين - وليس للمرة الأولى. لقد أزلتم جهودا هائلة ومهنية وناجحة بذلها الكثير من الناس من جنود الجيش الإسرائيلي إلى موظفي وزارة الخارجية…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75735" target="_blank">📅 16:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75734">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJiRU6BtXoXzl9coe9s_jRT63ojy4wrITMAJ0MSt3GWy0wUglqAXF8_QIlmjZ2wi7B8fwNR8ECcyJI-URC4xSRRinrVFWmhKzLahrL5MfJbkKWxm-bTWijSy4ZyKm5XZQANXTPd-McsoZfAQhn2bTyBYw2FzlQXEQStg__eFF0r_zw-z15qZ6qpTCa88lfIasQdWNaZ0xZ0T5CFe5hGd6ZhKEDgIJxpS7-8jqcssRCfJwZPdgT5fvmrH-jq7cXsDOpKiH8Z9PQKvL5XozqCSQYwqYil4Gfm-W_L76WM8sD7GpXfGGC4X-43LrJn_ehZxna923vZq5-lJ0Q--uxRqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن غفير يقوم بجولة في ميناء أسدود ويشرف على اعتقال نشطاء أسطول الصمود ويقول: "أدعو نتنياهو أن يعطيني إياهم لفترة داخل السجون".</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75734" target="_blank">📅 16:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75733">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رئيسة وزراء إيطاليا ووزير خارجيتها: معاملة إسرائيل لنشطاء قافلة كسر الحصار غير مقبولة. نتوقع اعتذارا من إسرائيل بشأن معاملة نشطاء الأسطول</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75733" target="_blank">📅 15:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رئيسة وزراء إيطاليا ووزير خارجيتها: معاملة إسرائيل لنشطاء قافلة كسر الحصار غير مقبولة. نتوقع اعتذارا من إسرائيل بشأن معاملة نشطاء الأسطول</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75732" target="_blank">📅 15:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🤺
حزب الله:
شاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في موقع جل العلام على الحدود اللبنانيّة الجنوبيّة بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75731" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75730">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سوالف الگهوة
من منزل العامري ، طرح مبادرة اليوم تتضمن صلح وبناء الجدار المتصدع داخل الإطار التنسيقي في العراق..</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75730" target="_blank">📅 15:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c36a9108.mp4?token=EIw77dctHTr2syk4wmQDudVa-cfnr5OLV5jq4EcNGZ4QKQllIO6m_HPXFSr3IpfqApb0rmFEa_bWKDWQQ9ZRO66kJuyY5VkqXoW2zvzQ8ngW5fUzC5enQyieIm6NToGNqz-FlH3gIiovT7Wt-lv9JLJ7n8zfRmlVLvvk2s8hXWqof7c0i1gdcJ1nq9fukEJQBMS3n1DHlt7UcA1TZWTRi-g3f63vOP8-ZTmDH6q4rEodWgBqD_NxTDH4jpTvxMUp76jqUm8ivM9CfMJmfUk_7zhxMipK_jt9Mw9O4N_QUVhk7Ti7Ago9RYxPnvtwzCO2XLKWyX1EYXsYVW_2oDldjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c36a9108.mp4?token=EIw77dctHTr2syk4wmQDudVa-cfnr5OLV5jq4EcNGZ4QKQllIO6m_HPXFSr3IpfqApb0rmFEa_bWKDWQQ9ZRO66kJuyY5VkqXoW2zvzQ8ngW5fUzC5enQyieIm6NToGNqz-FlH3gIiovT7Wt-lv9JLJ7n8zfRmlVLvvk2s8hXWqof7c0i1gdcJ1nq9fukEJQBMS3n1DHlt7UcA1TZWTRi-g3f63vOP8-ZTmDH6q4rEodWgBqD_NxTDH4jpTvxMUp76jqUm8ivM9CfMJmfUk_7zhxMipK_jt9Mw9O4N_QUVhk7Ti7Ago9RYxPnvtwzCO2XLKWyX1EYXsYVW_2oDldjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الكيان:
رصدت قواتنا أجهزة مراقبة تابعة لحزب الله في جنوب لبنان داخل مبنى كان حزب الله يستخدمها لمراقبة قواتنا وتوجيه العمليات.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75729" target="_blank">📅 15:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75727">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزارة خارجية دويلة الامارات:
نشدد على ضرورة التزام حكومة جمهورية العراق بمنع كافة الأعمال العدائية الصادرة من أراضيها بشكل عاجل دون قيد أو شرط وضرورة التعامل مع تلك التهديدات بشكل عاجل وفوري ومسؤول بما ينسجم مع القوانين والمواثيق الدولية والإقليمية ذات الصلة. كما نؤكد على أهمية اضطلاع العراق بدوره في ترسيخ الأمن والاستقرار في المنطقة، بما يحفظ سيادته ويعزز مكانته كشريك فاعل ومسؤول في محيطة الإقليمي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75727" target="_blank">📅 14:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75726">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6bfe77ce.mp4?token=lpKNUYFZksAyi85CYvJl-K8pIsqLNzkQnDilaAGnv4CXFLZrVkiL2uOPIdUL3sPJ_AQhZRRuYCxVjTTgKxnun4vSH7grHs4AkNkvBkEtHyyPH5ie8TnAoJJhRpoio5hQ42XoBQbjpxJFQRzApMNMGe5S06_RxYu0qd5ZfAN0aSR7pv0PRmEn7-Iwc5_Zd6A0ZNJvHptfQGIFRYqU-NWavSQZcbCvptIIDmaZiXOFCcvNBZAZymsjmctX9BADaW6a523wph6eknIbG768hCuAXCOD6ngFSZpuecyzm6Q3Y9XnNa58FFPJOr-daWmFKMDyFRw1_r1TRnDom3tx6yCkSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6bfe77ce.mp4?token=lpKNUYFZksAyi85CYvJl-K8pIsqLNzkQnDilaAGnv4CXFLZrVkiL2uOPIdUL3sPJ_AQhZRRuYCxVjTTgKxnun4vSH7grHs4AkNkvBkEtHyyPH5ie8TnAoJJhRpoio5hQ42XoBQbjpxJFQRzApMNMGe5S06_RxYu0qd5ZfAN0aSR7pv0PRmEn7-Iwc5_Zd6A0ZNJvHptfQGIFRYqU-NWavSQZcbCvptIIDmaZiXOFCcvNBZAZymsjmctX9BADaW6a523wph6eknIbG768hCuAXCOD6ngFSZpuecyzm6Q3Y9XnNa58FFPJOr-daWmFKMDyFRw1_r1TRnDom3tx6yCkSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بن غفير يقوم بجولة في ميناء أسدود ويشرف على اعتقال نشطاء أسطول الصمود ويقول: "أدعو نتنياهو أن يعطيني إياهم لفترة داخل السجون".</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75726" target="_blank">📅 14:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75725">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
رسالة قائد الثورة الإسلامية السيد مجتبى الخامنئي بمناسبة الذكرى الثانية لاستشهاد الشهيد رئیسي وتكريم شهداء الخدمة
بسم الله الرحمن الرحيم،
إنّ إحياء ذكرى شهداء «رحلة أيّار» (حادثة تحطّم المروحيّة) وفي مقدّمتهم رئيس الجمهورية الشهيد حجّة الإسلام والمسلمين رئيسي، يُعيد إلى الذاكرة استشهاد قوافل خدّام الشعب في جمهورية إيران الإسلامية، من مطهري وبهشتي ورجائي وباهنر، إلى رئيسي وآل هاشم وأمير عبداللهيان ولاريجاني؛ مئات الشخصيات البارزة من الذين تربّوا في مدرسة الخميني الكبير والخامنئي العزيز (أعلى الله مقامهما الشريف)،  وزيّنوا سجلّ الخدمة المخلصة والجهادية لمسؤولي الجمهورية الإسلامية بتوقيعهم المضمخ بالدماء.
ويمكن للمرء أن يعدّ  من الميزات البارزة للشهيد رئيسي: تحمّل المسؤولية، وإفساح المجال للشباب، والاهتمام بالعدالة، والدبلوماسية الفاعلة والنافعة، ولا سيما الطابع الشعبي الذي اتّسم به؛ وقد كانت هذه الخصائص تبعث الطمأنينة في نفوس أصدقاء إيران، ومنهم مجاهدو جبهة المقاومة القوية وكثير من الحريصين على النظام. وكلّ ذلك كان ممتزجًا، بالطبع، بنفحة روحانية متجذّرة في أعماق نفسه.
وأما بشأن العلاقة بين المسؤولين والشعب، فإنّ الخصائص الإيجابية المؤثّرة كانت تؤدي إلى تقدير متبادل. وهكذا جرت مراسم تشييعه إلى جوار مولاه ومخدومه الإمام أبي الحسن الرضا صلوات الله وسلامه عليه، بمشهد مهيب قلّ نظيره. وقد شكّلت الفترة غير المكتملة من رئاسته للجمهورية معيارًا لقياس حجم الجهد والحرص على الشعب والبلاد، مع الحفاظ على استقلالها.
واليوم نقف أمام الملاحم التي سطّرها الشعب الإيراني في مقاومته التاريخية الفريدة بوجه جيشين إرهابيين عالميين. وهذا الأمر يزيد من أعباء التكليف الملقى على عاتق مسؤولي الجمهورية الإسلامية - من القيادة ورؤساء السلطات إلى جميع مستويات الإدارية ـ أكثر من أيّ وقت مضى. واليوم، فإنّ شكر نعمة الانسجام بين الشعب والحكومة وسائر أجهزة الجمهورية الإسلامية، يكمن في تعزيز دوافع المسؤولين ومضاعفة خدمتهم وجهادهم، والعمل على حلّ مشكلات البلاد ، ولا سيّما في المجالين الاقتصادي والمعيشي، والحضور الميداني والمباشر، وتعريف دور جادّ للشعب الناهض بمسار تقدّم البلاد والتحرك بأمل نحو المستقبل المشرق.
رحمة الله ورضوانه على شهداء طريق الخدمة، ولتكن النصرة الإلهية ودعاء سيّدنا عجل الله تعالى فرجه الشريف سندًا لخدّام الشعب الإيراني المسلم.
السيد مجتبى الحسيني الخامنئي
20 أيار/مايو 2026</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75725" target="_blank">📅 14:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75724">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوي انفجارات في محافظة السويداء جنوب سوريا</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75724" target="_blank">📅 13:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">إعلام إيراني عن مصدر بإسلام آباد: وزير الداخلية الباكستاني توجه إلى طهران للقاء مسؤولين هناك</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75723" target="_blank">📅 12:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75722">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏الجيش الأردني يدعي إسقاط مسيرة في جرش دخلت الأجواء الأردنية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75722" target="_blank">📅 12:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">إعلام خليجي عن ‏مصدر دبلوماسي: تضارب المواقف بين إيران وباكستان حول قنوات التفاوض ومكان المحادثات</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75721" target="_blank">📅 12:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇹
إيطاليا الدولة الـ19 التي تشغل طائرة التزود بالوقود A330.
وقعت إيطاليا صفقة بقيمة 1.4 مليار يورو مع شركة "إيرباص" لشراء ست طائرات تزود بالوقود من طراز A330 MRTT - مما يؤدي إلى إلغاء طلبية شركة "بوينج" لطائرة KC-46 Pegasus، التي اختارتها روما في الأصل في عام 2022 قبل إلغائها فجأة في عام 2024.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75720" target="_blank">📅 12:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">🇮🇶
إلغاء القرار المتعلق بفرض مبالغ تحت مسمى "أجور خدمة" على شركات الهاتف النقال</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75719" target="_blank">📅 11:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇱🇹
أ ف ب: إغلاق مطار فيلنيوس في ليتوانيا بعد الاشتباه بطائرة مسيرة</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75718" target="_blank">📅 11:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75717">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db7a1d74fb.mp4?token=ZN4voaIJqF7WBaSu7mqoQUqvhJOqhI1HyLGujEW7rqHsMS4M2x7LO29N3AoZuNow0eys7jr2sz_t3I9Mdyp_uxhGekHrhYwqpusZN6QI419q-B7Qdru_djvaf1GljXwxsY_9fB2H7BglP9CQH0p_pM-FuiR2cXvn-ZzJ8ZCCZTp9abS-atRRsx7CMMx1P2AaC-WyZq9iHZ4TFAIDf726xHkvzyOmxi1w2VVF7dy13py-3HsBMCGCfCx4ElzPLHUQjXN5NcM6_Mw1pYjwUsjhADLr93SUkg2BIdF6ei8jjmUsre5D8Q7FyAXYhfSkO0slFKCjSiqmBbA83oNgckp8Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db7a1d74fb.mp4?token=ZN4voaIJqF7WBaSu7mqoQUqvhJOqhI1HyLGujEW7rqHsMS4M2x7LO29N3AoZuNow0eys7jr2sz_t3I9Mdyp_uxhGekHrhYwqpusZN6QI419q-B7Qdru_djvaf1GljXwxsY_9fB2H7BglP9CQH0p_pM-FuiR2cXvn-ZzJ8ZCCZTp9abS-atRRsx7CMMx1P2AaC-WyZq9iHZ4TFAIDf726xHkvzyOmxi1w2VVF7dy13py-3HsBMCGCfCx4ElzPLHUQjXN5NcM6_Mw1pYjwUsjhADLr93SUkg2BIdF6ei8jjmUsre5D8Q7FyAXYhfSkO0slFKCjSiqmBbA83oNgckp8Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
هبوط مروحية عسكرية في مستشفى رمبام على متنها عدد من الإصابات في صفوف جيش الاحتلال جراء إصابتهم جنوب لبنان</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/75717" target="_blank">📅 10:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75716">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3GuIhUBTh_gNkRDob5o3rBRsPMzcFL9qZ20Yb1ONTs725nqjxYF-SYXBdgT2Bh4OUlZRtUhmV57Pl-U9x1fXeTT8uANu8EWErGxyaP6iKHWFqkqyWBu1TMbv2xhpsQHDlzJQXV1D4QL3vqkdw_07dF3Ss9mP-UwiGPwIbdjkuBvnvk2Hsus0tlElK0mx_ol8D65wBv2jzf28IWWrL6RanYJsBICbgLi9n6GUP4uw1hYEaDpd3_pZvoVMeTYzylQc3zSAP9-Zh6Kmy5aAvIQQx5ap9tgHeAhD1Wy6T5POYSwJyahC7lUS9QemDZx712ei8uqwGIfnUYNSnYvwrmrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇸🇾
الدفاعات الإسرائيلية تعترض مسيرات في سماء محافظة درعا جنوب سوريا.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/75716" target="_blank">📅 09:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75715">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زلزال بقوة 5.6 يضرب شمال سوريا وتركيا.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75715" target="_blank">📅 09:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrUrl7QXGJRjt_C3d-1BP5e0DEXZxBuKBFCUQUPkwo-FZrygLFR8s_CjgkzwJ1v_kOfbEJx7YyEvnMjwJYf5JhUqIjMwt5bV7a-iadGtWScBJgbTgkc7st9L7roH4Nszq1APN8zsCHtCvEoQ7t6AgU1p0m4Nax2zqB-HOJ3fx5Brzlux6pZoGLBITHIqRUquTAHztUscR58iKUJpskIaBp2zWGKdkCW2puIIy84Bmz_lHn6eVdTpad-jrVw1x1NUoqV0kkAIo9G7ORMExXG9lbUzdtx9D1-d2ibxQRvCDDTeH7uB8fTIUqHlp25KNh5665GgLG2y7jwQf1UMbbNtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نيوورك تايمز: يخطط الاتحاد الدولي لكرة القدم (FIFA) لحظر المشجعين مرة أخرى من إحضار علم "الأسد والشمس" قبل الثورة الإيرانية والملابس ذات الصلة إلى ملاعب كأس العالم خلال بطولة 2026.  تم أيضًا تقييد العلم في كأس العالم قطر 2022.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/75714" target="_blank">📅 01:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utsM-G_tTvoymCKzUOAhg53S_Pz1pKYq1Adr_TZtmwZJvHhCrCqQJLhb6WVDs_E6pA2ush0bJySVHdFAn-Ohxp6pfR7s-vcxsmj1VfWIZMqw70No51wo6BdRBlAgIxjQhaOktPMFlcyLn5JjviFJmiFgVgLYvcW4vImniEhqbxwI6W0i-YgijPzY_dR9ORjeezSqOaTyJMWOvFJwqLxSZXQ2ED0Ezc-klt-msHTtlBOgC7XKiOhczkRvWitO9ypQu-oPwWqNvCfYNdHhqAnnwzKMQm1wsoA_lYwnwD33F62xOXGeWitKnTfxUCHb_OpxeWfIJhWohq7aNVlFi1Schg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجولاني يشكر دونالد ترامب على “كرمه الزايد حيل” بعد إهدائه شيشتين عطر، ويعتبرهن “الأساس المتين” للعلاقات السورية الأميركية، وسط ترقب شعبي لمعرفة إذا المرحلة الجاية تشمل بخاخ جسم لو مزيل عرق دبلوماسي.
القدس تنتظرنا يا اخوة
😄</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/75713" target="_blank">📅 00:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75712">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5RaTLva7_4WthTliHFYXRBqtNku-ghkvTZ8TbHvS1bzLf9_r88AceoXJ5gosZaqyIZI1OBCRFemqVSVcgeUwt_3HhaRxtHg-0XOfFk7FybN4-qzzrEQiNS_8f8P9yGk_DNWDTxWH4GakVGJU2KFFhtT3aeg37cNp56Mm6DhUPc0Mou9fvKPSwpWTOLCpNvFfkOiezFGGE8j60BcSr-RYLkVExmBN6XiIjkgrH8gpAkSIPikZ9_2duYTKGM2W-h2W6bWsECpHrgPU3eIqj_YigwGw9NMjqS8VCVL8aYr00rKmaREYttsL9P8OAacC4RxVMSmGsZQMqQzpROXAfTEJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
بعد أشهر من بدء الحرب على إيران، يعترف الكونغرس الأمريكي بفقدان عشرات الطائرات التي تبلغ قيمتها مليارات الدولارات.
تم تأكيد قواتنا المسلحة القوية كأول من يضرب طائرة F-35 التي توصف.
مع الدروس المستفادة والمعرفة التي اكتسبناها، ستضم العودة إلى الحرب العديد من المفاجآت.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/75712" target="_blank">📅 00:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75711">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
🏴‍☠️
قوات حزب الله البطلة تشتبك مع عناصر جيش العدو في بلدة حداثا بجنوب لبنان وتتمكن من إستهداف وإحراق دبابة ميركافا وإصابة عدد من الصهاينة والمعارك مستمرة حتى اللحظة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75711" target="_blank">📅 00:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
🏴‍☠️
قوات حزب الله البطلة تشتبك مع عناصر جيش العدو في بلدة حداثا بجنوب لبنان وتتمكن من إستهداف وإحراق دبابة ميركافا وإصابة عدد من الصهاينة والمعارك مستمرة حتى اللحظة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/75710" target="_blank">📅 00:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbad0422a.mp4?token=FN8CLgsKuAMRwDllRhCm-MfogZ2IvjxATLEGwB8g52epIV_ndx881EhAZ2_7CweT7vHukzaLzrJcKSs7e8Usf9Eu6mE5UrahOHQZKfBHsZGO5XT86y3Z_a_Zh_U7osmg_adIFcCHLcTO-1SkJNqkIMpgeB-P_qbOCXnh41BLQcPdV8rLeiA0caToR2UZAF4QP-ylRKNT6gJb--FPJNdNs6z9TjsFW8iwyquy-um3nrTUwOuWFrNHB3yCGYWWhd_TDN6qt9SLuaeiFFoazgu51aR5-P8CQGM42EJaTsygfO8cGaoe--8L4xTXd1TABE6c-zZlgaZca2gAXCqjDXO-nGdypsdzwlxe_Yux8EwUqnrSEItItGaa9tA6RbFpb4U6jK7gU16RWjrRxrHzEYobeiXdCWMTKOsImmnZ0tUMFeGqnLeEDqBnPXJs0Zm4gzfy-k7LnbqnCtjziB5yrYS0lIRhfHR2BeJm07wfBMghKfpUdQu1VCEgQIAgHCmdCvwkemF6FA4zQ-e756fzA2DmJ0R4PG4SJRrSlgFJYHfUd5I0J0fAMpm28unsxKWHc-1WO5rlwnGuiqmMfBGkdUxPRHOtURmM4ux_Pba4-OvdkMX_AzSTtWwkghdt0xUE4TRtNanQcrJGrmLe_d2C0SSHQ29iATsHokc0gQV1CMJOKp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbad0422a.mp4?token=FN8CLgsKuAMRwDllRhCm-MfogZ2IvjxATLEGwB8g52epIV_ndx881EhAZ2_7CweT7vHukzaLzrJcKSs7e8Usf9Eu6mE5UrahOHQZKfBHsZGO5XT86y3Z_a_Zh_U7osmg_adIFcCHLcTO-1SkJNqkIMpgeB-P_qbOCXnh41BLQcPdV8rLeiA0caToR2UZAF4QP-ylRKNT6gJb--FPJNdNs6z9TjsFW8iwyquy-um3nrTUwOuWFrNHB3yCGYWWhd_TDN6qt9SLuaeiFFoazgu51aR5-P8CQGM42EJaTsygfO8cGaoe--8L4xTXd1TABE6c-zZlgaZca2gAXCqjDXO-nGdypsdzwlxe_Yux8EwUqnrSEItItGaa9tA6RbFpb4U6jK7gU16RWjrRxrHzEYobeiXdCWMTKOsImmnZ0tUMFeGqnLeEDqBnPXJs0Zm4gzfy-k7LnbqnCtjziB5yrYS0lIRhfHR2BeJm07wfBMghKfpUdQu1VCEgQIAgHCmdCvwkemF6FA4zQ-e756fzA2DmJ0R4PG4SJRrSlgFJYHfUd5I0J0fAMpm28unsxKWHc-1WO5rlwnGuiqmMfBGkdUxPRHOtURmM4ux_Pba4-OvdkMX_AzSTtWwkghdt0xUE4TRtNanQcrJGrmLe_d2C0SSHQ29iATsHokc0gQV1CMJOKp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انيميشن بأسلوب الليغو يوثّق المسار الذي خاضه رئيسٌ شعبيّ للجمهورية الإسلامية الإيرانية
نُشر بمناسبة ذكرى استشهاد الشهيد رئيسي ورفاقه الشهداء</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75709" target="_blank">📅 23:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75708">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
حاكم كاليفورنيا:
إنهم يحاولون تزوير الانتخابات. دونالد ترامب يعلم أنه سيُهزم بشدة في شهر تشرين الثاني.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/75708" target="_blank">📅 22:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
انتحار جندي من الجيش الإسرائيلي داخل دورة مياه في "الكرياه" بتل أبيب.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75707" target="_blank">📅 22:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75706">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
🏴‍☠️
مراسم تنكيس علم العدو الإسرائيلي الغاصب في مقر اللواء 226 التابع لجيش العدو في بلدة البياضة جنوبيّ لبنان بتاريخ 17-05-2026</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75706" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75705">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
‏احتجزت الولايات المتحدة ناقلة نفط مرتبطة بإيران في المحيط الهندي ليلاً، في الوقت الذي يهدد فيه ترامب باستئناف الضربات العسكرية على إيران.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75705" target="_blank">📅 21:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75704">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
‏
جي دي فانس:
خياران أمام إيران إما الاتفاق أو استئناف الحرب.
نعتقد أن الإيرانيين يريدون إبرام اتفاق لكن نؤكد أنه لدينا دائما خطة بديلة.
‏لا أحد يريد عودة الحرب والفرصة متاحة أمام إيران.
إيران بلد معقد للغاية ونرى مواقف متشددة من جانب فريقها المفاوض.
أوضحنا للإيرانيين خطوطنا الحمراء.
لا أعتقد أن الإيرانيين سيكونون متحمسين لنقل ما لديهم من يورانيوم مخصب لأمريكا أو روسيا.
مخططنا ليس نقل اليورانيوم الإيراني المخصب إلى روسيا ولم يكن ذلك أبدا ما نخطط له.
لا نريد فقط التزاما من الإيرانيين بعدم امتلاك سلاح نووي بل بألا يعيدوا بناء قدراتهم النووية مستقبلا.
هذه ليست حربًا أبدية. سنتولى الأمور ونعود إلى ديارنا. هذا ما تعهد به ترامب، وهذا ما سيحققه.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75704" target="_blank">📅 21:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🏴‍☠️
‏
هيئة البث الإسرائيلية:
الاستعدادات الأميركية – الإسرائيلية لاستئناف الحرب ضد إيران اكتملت.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/75703" target="_blank">📅 20:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75702">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxupKaMIzjUwkIl9yh1wMmT5MJ7_1bwpleL1Uc4mRk1hqZg-kW1WUnVDj1iUeAuDmbMiO2lWhTUXYcYbfAKbkid9B0JMQBovTLBySIZ5_lkFFMVAyIeobrY9E0NyrMZV4JsqHApbjQQ_q6EHM8ftr9oUAogP_rEJP2ng19GFYs4tp_CNDt4M-34XxcodWQUDwFllrnM9v8seBBcv0YlxIzJpuU8phHwweMvimtfxU9BmZsqzI0gIzjMnlo4vjXdfodbKNS7DB1U4qWJi097mInVMzebq6ue4JwX81va_rQgRP14Ygrc8UTDFinco66Ku4MX-_0cITNHPXZIfR6p9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
وزير السيد مقتدى الصدر ينشر عبر حسابه الشخصي.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75702" target="_blank">📅 20:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏ اعتقال موظفة في السفارة الأمريكية في بغداد تدعى قند محمد فرج ذياب الجنابي بتهمة الرشوة والفساد !!!!
‏</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75701" target="_blank">📅 20:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حدث امني خطير في بغداد</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75700" target="_blank">📅 20:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeQZydF8395p5OhQDOIWw9XLPrU9-zsKbToK4HZgSXEEj-MmlILrdxTzrmA3BBpsrv22V3qnRjO5nrTp4excIElZqojt7nZZhbzAH2PmyMXlcoIoSeNJgWS8vzdfgW7AA9Sd-G1YxvpuMeyPwAACHWWqTMYYySzoImnkn2PWTCUTycTAYDAODoNk8fiQLHobeEl9Z_p11rOhNYv_bAbVPh6eZ_Cd1E4UGg83z2D8zi6-tz0hcze_HUtqOXGoYBLEyQIiQkDF0rob1tmzqawE5bPiUwG-3BnQomSt7QLcF5uVguICZAaZedIuxHkJqkMi1WRg_44itaGTN65P9mqxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
مقتل جندي إسرائيلي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75699" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
حزب الله ينشر:
ترقبوا... مراسم تنكيس علم العدو الإسرائيلي الغاصب في مقر اللواء 226 في البياضة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75698" target="_blank">📅 19:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⭐️
ذا أتلانتيك:
اصطدمت طائرتان لإعادة التزود بالوقود من طراز KC-135 Stratotanker فوق غرب العراق في 12 آذار خلال الحرب الأمريكية-الإسرائيلية ضد إيران، مما أدى إلى مقتل ستة من أفراد الخدمة الأمريكية بعد تحطم إحدى الطائرتين بينما تمكنت الأخرى من الهبوط مع أضرار شديدة في الذيل.
صرحت قيادة مركز القيادة المشتركة (CENTCOM) علنًا أن التصادم وقع في "مجال جوي صديق" ولم يكن بسبب نيران معادية. ومع ذلك، تظهر تقارير المخابرات الأولية أن نشاطًا مضادًا للطائرات تم اكتشافه من ميليشيات مدعومة من إيران في المنطقة في وقت تحطم الطائرة، مما يثير احتمال أن يكون الطيارون قد اتخذوا إجراءات تفادية قبل التصادم.
رفضت قيادة مركز القيادة المشتركة (CENTCOM) لاحقًا هذه التقارير، مستنتجة أن الإطلاقات المكتشفة كانت على الأرجح صواريخ موجهة إلى أهداف أرضية وليس طائرات.
من المتوقع أن يحدد تحقيق مستمر لسلاح الجو الأمريكي ما إذا كان الحادث كان خطأً يمكن تجنبه من قبل الطيارين بسبب ازدحام المجال الجوي بدلاً من عمل العدو.
شمل الأفراد الستة الذين قُتلوا ثلاثة طيارين في الخدمة الفعلية من السرب السادس لإعادة التزود بالوقود في فلوريدا وثلاثة من أفراد الحرس الوطني للطيران في أوهايو من السرب 121 لإعادة التزود بالوقود.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75697" target="_blank">📅 19:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6863208b.mp4?token=pONWCkF4j6-ZqBxdz4O1rLUsqr-m8BjBE9pUhxAEFwjMXYaq831OsZlvUPooJNlJP4E0sXzoWDunXZ3cmqCbaXbX_2sWxcsRLCamDjJ2vX22CzXqZMtTWZOjgHwy_ufTi_dw6QNZwVV9_2loBlqcn7M2Yts1O666IXOx_ZjUNABR-J1aqujt3OfkAIb98kXUM_pUnem03WR5KM3FEgTCysPvfPBiH1R8X_df3RdDrlIjISyZpmwb6ps8dguhMaoiUJahdVhqfQxaT5EttvDamVsnlmfuQdPnmeCFh3yapQMUQgPuikPxQ6BnXLHylprYLkOjzYAEG9Y2pEuFMX6fi6nAv-T_SgOwLNXMxidaFirY7-W8RJ4mwv6Hq3csdPDvHxKRBky-tYpfEvjIARUe2S_0fXTeDrHw8Ocy4l2p4tEGSjRM4vGdA-GvaiNeV4f1zgg-lWI2GVLtUhdNYcmc4-dKfqaDyJvfhR39yI0r8Hr54x4VXO1ZC4RGB_1FbZN1WLOqU1QBtxgxZRqWASvaX8EzSEVpY9VULq2iCZCDnFLqt8dMpsx6Ny5bmQvgkYOebMD6hvMBAVM0EJXLdDpXkYI8gCzK9UQBb3cACG5HyPl4AI3becBTHlrLYM84DVHc7C0B6O8exlKPrHpzP0ri-feWnibr2PpewIPcb8FUbX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6863208b.mp4?token=pONWCkF4j6-ZqBxdz4O1rLUsqr-m8BjBE9pUhxAEFwjMXYaq831OsZlvUPooJNlJP4E0sXzoWDunXZ3cmqCbaXbX_2sWxcsRLCamDjJ2vX22CzXqZMtTWZOjgHwy_ufTi_dw6QNZwVV9_2loBlqcn7M2Yts1O666IXOx_ZjUNABR-J1aqujt3OfkAIb98kXUM_pUnem03WR5KM3FEgTCysPvfPBiH1R8X_df3RdDrlIjISyZpmwb6ps8dguhMaoiUJahdVhqfQxaT5EttvDamVsnlmfuQdPnmeCFh3yapQMUQgPuikPxQ6BnXLHylprYLkOjzYAEG9Y2pEuFMX6fi6nAv-T_SgOwLNXMxidaFirY7-W8RJ4mwv6Hq3csdPDvHxKRBky-tYpfEvjIARUe2S_0fXTeDrHw8Ocy4l2p4tEGSjRM4vGdA-GvaiNeV4f1zgg-lWI2GVLtUhdNYcmc4-dKfqaDyJvfhR39yI0r8Hr54x4VXO1ZC4RGB_1FbZN1WLOqU1QBtxgxZRqWASvaX8EzSEVpY9VULq2iCZCDnFLqt8dMpsx6Ny5bmQvgkYOebMD6hvMBAVM0EJXLdDpXkYI8gCzK9UQBb3cACG5HyPl4AI3becBTHlrLYM84DVHc7C0B6O8exlKPrHpzP0ri-feWnibr2PpewIPcb8FUbX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇨🇳
لحظة وصول الرئيس الروسي فلاديمير بوتين إلى بكين، واستقباله من قبل وزير الخارجية الصيني وانغ يي.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75696" target="_blank">📅 19:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75695">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbuGmJu7c6Ugo4-1BxCIuaL7INOZXq8Fc2oA-J05F4xHV737gODy6-5fqGBytX9OW2n9TP_C5uUZutGGcGhLFGsJva6gbqNNjEZMjehs0XYmjqTp090cD2GHwCUZ7Se35fCuBtlxiWJbTgNmFA1x6lu5un6cBR_aa6mzmgfWREUUowmyYArBsOSHdYBM1zpu4I6u8gQlGku8NLq5I9tpY8SqYxz6ZBHERFi71dHfqCJ2r1TXdDA5Np-TrD7-ulvIB_lpVvyO44zkUjEzs1PT7jHIhoycwuexMh-j6VLIMBWGP5Ual3ATqNwhLoYoZMOGNEAZdaV3h5C2eNd2I9DtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رد قائد الثورة الإسلامية على رسالة جمعٍ من الناشطين الشعبيين في مجال السكّان:
أشار قائد الثورة الإسلامية، آية الله السيد مجتبى الخامنئي،  في معرض رده على رسالة الإعراب عن المحبة والتعزية المرفوعة من قِبل جمعٍ من الناشطين الشعبيين في مجال السكان بمناسبة استشهاد قائد الثورة (قدّس الله نفسه الزكية)، إلى مسألة زيادة السكان وارتباطها بقوة إيران الإسلامية وحضارتها، مؤكدًا على تكثيف الجهود المتزايدة للناشطين الشعبيين في هذا الحقل وضرورة ترويج ثقافة الإنجاب.
🔻
وجاء نص رد قائد الثورة الإسلاميّة، الذي نُشِر بمناسبة اليوم الوطني للسكان، على النحو الآتي:
📖
بسم الله الرحمن الرحيم
بعد توجيه التحيّة والشّكر على إعرابكم عن المحبة والشعور بالمسؤولية، أيها الناشطون المُخلصون في مجال السكان؛ فإنّ من بين الإنجازات القيّمة للدفاع المقدس الثالث، والنعمة العظيمة لبعثة الشعب الفريدة التي تجلّت للجميع، صعود إيران إلى مستوى قوة كُبرى ومؤثرة. ولا شكّ في أن استمرار هذا الوضع وبلوغ مستوى أفضل منه، يرتبط ارتباطًا مباشرًا بقضيّة السكان.
▪️
إنّ قضية وجوب زيادة عدد السكان يُنظر إليها من منظار تعويض النقص الناجم عن بعض سياسات الماضي؛ ولكن إضافة إلى ذلك، فإنه من خلال المتابعة الجادة للسياسة الصحيحة والحتمية لزيادة عدد السكان، سيكون الشعب الإيراني العظيم قادرًا في المستقبل على خوض غمار أدوار كبرى وطفرات استراتيجية، وقطع خطوات واسعة في اتجاه إرساء الحضارة الحديثة في إيران الإسلامية. ومن هذا المنطلق، فإن الجهود المتزايدة للناشطين الشعبيين في مجال السكان وترويج ثقافة الإنجاب، يمكن أن يكون لها أثر بالغ الأهمية في سبيل تأمين هذا المستقبل المشرق.
⏺️
ومن جهة أخرى، فقد كان هذا الأمر أحد أهم هواجس قائدنا العظيم الشهيد (أعلى الله مقامه الشريف)، الذي طالما أكد عليه في الكثير من اللقاءات، والمداولات، والاجتماعات العامة والخاصة، ولا يزال يُعدّ من أهم القضايا الاستراتيجية للنظام. يُؤمل أن تؤدي جهودكم المخلصة، أيها الأعزاء، في ظل الدعاء المستجاب لسيدنا (عجل الله تعالى فرجه الشريف) إلى نتائج مثمرة، إن شاء الله.
✍
السيد مجتبى الحسيني الخامنئي
🗓
19 أيار/ مايو 2026</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75695" target="_blank">📅 19:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e2efce8f.mp4?token=GkO0_SbNASSPXekE5mttozREBjdOmtkh9UvBxhjbhFjkNQD6aYQWZxLPvs48mrwrp8Kw47QMq1f5o0ZMPAEMxh1vmzzdOO1t8HgSCPX_vY8P6pBH7gUnGAkPoxQntSmYLv_inhVU9sglgjp3wHq9xaknKQc0iNwQSwy5TYG9mYij_QsfBIrNTjke_qhDbA2A1ssPHNQHMusOiWPHtq5Wc_Hv3HjmC-iMcqRVbZmG-fVpzBBrqqoBS1GBOmC-mWNMQJu-LMnC1W82Tn5kCJmrEM23ET7LqpoiIBbnS1_EneoB08CcLqNnTsnbXldDhicQIU35yIENGs6p45stLrG6PllYU8wk0KTtnJlwO2IU07oi6xue4VuZuv620c0kE_lVsSTlWENBxPRXKnWuaEHFa_6BJ0vRGdgSStu17yNO5quowzdrGUSsTBewvGJhYWhc4acngMSxqlUjNSEx_ZjrGQWhKjVuKKLK0r1QilrHULZUXHmL1Za6DuoeSLCz8t0U2IpAn4RiMXeegBxJgOEaKa0AW_UmKu2PNWdE0zlc07eF2XS1NbhZuf8giwsz-6gytFQqpAoXW3BJJVjecXx1rbqVaLAJiw7qvtvAR_HI5g4Nv4WxWfSMg5_BqcP55FSQmBkzTUEBsiMLDNJfh5FEm5JBBMs43Qji-9MWDyO8syA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e2efce8f.mp4?token=GkO0_SbNASSPXekE5mttozREBjdOmtkh9UvBxhjbhFjkNQD6aYQWZxLPvs48mrwrp8Kw47QMq1f5o0ZMPAEMxh1vmzzdOO1t8HgSCPX_vY8P6pBH7gUnGAkPoxQntSmYLv_inhVU9sglgjp3wHq9xaknKQc0iNwQSwy5TYG9mYij_QsfBIrNTjke_qhDbA2A1ssPHNQHMusOiWPHtq5Wc_Hv3HjmC-iMcqRVbZmG-fVpzBBrqqoBS1GBOmC-mWNMQJu-LMnC1W82Tn5kCJmrEM23ET7LqpoiIBbnS1_EneoB08CcLqNnTsnbXldDhicQIU35yIENGs6p45stLrG6PllYU8wk0KTtnJlwO2IU07oi6xue4VuZuv620c0kE_lVsSTlWENBxPRXKnWuaEHFa_6BJ0vRGdgSStu17yNO5quowzdrGUSsTBewvGJhYWhc4acngMSxqlUjNSEx_ZjrGQWhKjVuKKLK0r1QilrHULZUXHmL1Za6DuoeSLCz8t0U2IpAn4RiMXeegBxJgOEaKa0AW_UmKu2PNWdE0zlc07eF2XS1NbhZuf8giwsz-6gytFQqpAoXW3BJJVjecXx1rbqVaLAJiw7qvtvAR_HI5g4Nv4WxWfSMg5_BqcP55FSQmBkzTUEBsiMLDNJfh5FEm5JBBMs43Qji-9MWDyO8syA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بصاروخٍ موجّه.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75694" target="_blank">📅 19:00 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
