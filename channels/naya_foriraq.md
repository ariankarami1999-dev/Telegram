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
<img src="https://cdn4.telesco.pe/file/MMkYbnMLq7bT3oAyC2ulmqpnP0UQ-w3lSepGhuGfhaYbiguWcpz6nso0jyQ32wMxS9HR4es87sDHn4OHV0_l4pPuEY2kPbHg9AP-yAFnCkaKVdrPd_AlPdN9v4Qi2DABJPISugjMw3-_ePqFvDOs5UNfsdOSYbw-4YdKIjyiBow7EEY04V0vACTgH1GemSzFg52OB5QS8bhmaqv3iDPlHPJtxj6_tGCrzCbHgH5i1HcYZpOcN99GG3SbJCWQF6_bJpiqU9XxEBbxJMpJR4Wd4hFXafSsIkw7FDp-82Hf1HyUCzvCg_TpD1XY4X-cynzdTDNn0sN2CQ_Tx2H6U_LAJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 260K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📰
مسؤول امريكي لرويترز: نعتقد أننا توصلنا إلى اتفاق قوي مع إيران.</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/naya_foriraq/78627" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏴‍☠️
مسؤول رفيع المستوى في الإدارة الأمريكية: سيجتمع ترامب مع قادة دولة الإمارات العربية المتحدة وقطر ودول أخرى في الشرق الأوسط في مجموعة السبعة G7</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/naya_foriraq/78626" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🏴‍☠️
مسؤول رفيع المستوى في الإدارة الأمريكية:
سيجتمع ترامب مع قادة دولة الإمارات العربية المتحدة وقطر ودول أخرى في الشرق الأوسط في مجموعة السبعة G7</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/naya_foriraq/78625" target="_blank">📅 17:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78624">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌟
وزير الخارجية الباكستاني في حديث مع نظيره السعودي:
تم تحديد التوقيع الإلكتروني على الاتفاق بين الولايات المتحدة وإيران ليوم غد.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/naya_foriraq/78624" target="_blank">📅 17:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ 05-06-2026 آلية هامفي تنقل جنود جيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/naya_foriraq/78623" target="_blank">📅 17:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
🌟
وسائل اعلام:
وفد إيراني يضم وزير الخارجية يصل باكستان غدا.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/naya_foriraq/78622" target="_blank">📅 17:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
🌟
وكالة مهر:
قدّمت قطر خطةً تُتيح بموجبها تقديم 12 مليار دولار لإيران تشمل الإفراج عن 6 مليارات دولار من أصولها المجمدة في قطر و6 مليارات دولار أخرى على شكل قرض أو خط ائتمان.
ادفع يا طويل العمر</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/naya_foriraq/78621" target="_blank">📅 17:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d92db5d7.mp4?token=rLpq6kGs_NYVw_BoMc9-YQ9iUQGPVZ7SDgrtpogghDBw2erYCjuTgny-Zv0SLaSwUa0V2L5NsZV4YiIn7CW_LtDnmPrYNYzKvXungYep3Kk5VW9V4YAY7Nb-tLJro0b62hxwlxpioyO--b3uFacCCXreSvXFmke1HqrRYGktzwlHOryU1Lhlg6D4MCDS2-c3tubcdNFU9BMFm2DNhjBsOh5RYZThUJAMXla6rAdYJePDeXRb4dx5RM-IOx0GYyBHAeryib4lqXajmFntYJ4w86X5Kw5IdndavDtntfszypqyg7BVMXwp9_1lrdPIAlBiUcZd9u0mdD-5vPiaEQt8CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d92db5d7.mp4?token=rLpq6kGs_NYVw_BoMc9-YQ9iUQGPVZ7SDgrtpogghDBw2erYCjuTgny-Zv0SLaSwUa0V2L5NsZV4YiIn7CW_LtDnmPrYNYzKvXungYep3Kk5VW9V4YAY7Nb-tLJro0b62hxwlxpioyO--b3uFacCCXreSvXFmke1HqrRYGktzwlHOryU1Lhlg6D4MCDS2-c3tubcdNFU9BMFm2DNhjBsOh5RYZThUJAMXla6rAdYJePDeXRb4dx5RM-IOx0GYyBHAeryib4lqXajmFntYJ4w86X5Kw5IdndavDtntfszypqyg7BVMXwp9_1lrdPIAlBiUcZd9u0mdD-5vPiaEQt8CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
How did China , Russia, North Korea see the war in Iran ?!</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/naya_foriraq/78620" target="_blank">📅 16:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: حادث غير عادي في أجواء المجر: طائرة إسرائيلية تفقد الاتصال مع مراقبة الحركة الجوية.</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/naya_foriraq/78619" target="_blank">📅 16:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حادث غير عادي في أجواء المجر: طائرة إسرائيلية تفقد الاتصال مع مراقبة الحركة الجوية.</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/naya_foriraq/78618" target="_blank">📅 16:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: مذكرة تفاهم إسلام آباد تركز على إنهاء الحرب في هذه المرحلة دون مناقشة الملف النووي.</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/78617" target="_blank">📅 16:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية:
مذكرة تفاهم إسلام آباد تركز على إنهاء الحرب في هذه المرحلة دون مناقشة الملف النووي.</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/78616" target="_blank">📅 16:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc8c581a7f.mp4?token=VPxF1zUO8V48BWP0fKU4KhqQbmDMkM9L_ye7pKmND3_qtVVxDk_56BrJW3usr-wt4b3XJOoTP13nXj9YIaaSX4gGOUrEHXcLpXM8LEkjZKcGZWXtEP0HdQFF0wLGi2GK76tvewbt1rSEDuB_dFg7K3kDLfIMJqAAO-urRlD9nO1aqAJr59H4SsMEsHhj03bBgAo-FTTb_SItjFKTqLyRwLJsg9XpnEM10czJYzXiSW1UxTBDM_KFriXJjKGn_XRJVS64GDNjwXMONWPOnGatyDZ88dEE7sloHRnZIoN48pSpk6OyfzPORdQbXDhJg7Mnes85dveG2dScnQQuF3FZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc8c581a7f.mp4?token=VPxF1zUO8V48BWP0fKU4KhqQbmDMkM9L_ye7pKmND3_qtVVxDk_56BrJW3usr-wt4b3XJOoTP13nXj9YIaaSX4gGOUrEHXcLpXM8LEkjZKcGZWXtEP0HdQFF0wLGi2GK76tvewbt1rSEDuB_dFg7K3kDLfIMJqAAO-urRlD9nO1aqAJr59H4SsMEsHhj03bBgAo-FTTb_SItjFKTqLyRwLJsg9XpnEM10czJYzXiSW1UxTBDM_KFriXJjKGn_XRJVS64GDNjwXMONWPOnGatyDZ88dEE7sloHRnZIoN48pSpk6OyfzPORdQbXDhJg7Mnes85dveG2dScnQQuF3FZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان صهيوني يطال بلدة كفر رمّان جنوبي لبنان.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/78615" target="_blank">📅 16:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231e7d73b7.mp4?token=KTn3OCRZLNTL_so9HJRzm4f8e5pzpDd5-0qG3KhXLk12OAHq31mYPomd_nVx0jVjOxvkXxMyfTTb4_xiT2tJioKZ6P-aZKIbdYTgCoSUi9xAqPaOk2Kwb61LPMZtF6ETZ-OCO4L9nmAf9c8qtS8QhDZdq0idZ5Gl03f045RrpyesnmJ8qfgN6WH7SXirLUuKq4rjx8dlYnDhmtvaN9yYM7Q7AomlOJeNrK_srSWMwZu5JBwjE7x3PCWrfuVnb2oqtvjGtK1clPMtO8_nt0ouAiuz7VJ3DvHHPdC-rD8HtogNmBC0ALwzzaWQZcbtJvOFh_fFyYJSQ2dNnLghqtx4Nl0oMXs4ogbzZ3ViLzeppZ2hSKEJjFKOQE2xh-zQOACLAMu-HUhxpzRikQ_k3GYohtWZdLxYfI3QMjDUhIxnZj5QqXpJOyJgZGULz0z21S0sRKLlYDIGMEfgNC-gypbBKPBVD34pZKKuOd0zDMG6C696aWXZgpfXxcLUF7RboOLk99cSi7Xq4HkKB-NZvipL9JJngEUsCHv-gOF3zhqwmTGTKnHZMZM5H830EWfLNt2AoYXb-npyS3DWWs3YA19poJV3wQi7hSkeZdMdVy22m24LPUUzU4J8h_KmFI1Wg3soZjG-rEOKy65Ho_-njN2Nh76_1vg5yGEJVIfqgKizko8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231e7d73b7.mp4?token=KTn3OCRZLNTL_so9HJRzm4f8e5pzpDd5-0qG3KhXLk12OAHq31mYPomd_nVx0jVjOxvkXxMyfTTb4_xiT2tJioKZ6P-aZKIbdYTgCoSUi9xAqPaOk2Kwb61LPMZtF6ETZ-OCO4L9nmAf9c8qtS8QhDZdq0idZ5Gl03f045RrpyesnmJ8qfgN6WH7SXirLUuKq4rjx8dlYnDhmtvaN9yYM7Q7AomlOJeNrK_srSWMwZu5JBwjE7x3PCWrfuVnb2oqtvjGtK1clPMtO8_nt0ouAiuz7VJ3DvHHPdC-rD8HtogNmBC0ALwzzaWQZcbtJvOFh_fFyYJSQ2dNnLghqtx4Nl0oMXs4ogbzZ3ViLzeppZ2hSKEJjFKOQE2xh-zQOACLAMu-HUhxpzRikQ_k3GYohtWZdLxYfI3QMjDUhIxnZj5QqXpJOyJgZGULz0z21S0sRKLlYDIGMEfgNC-gypbBKPBVD34pZKKuOd0zDMG6C696aWXZgpfXxcLUF7RboOLk99cSi7Xq4HkKB-NZvipL9JJngEUsCHv-gOF3zhqwmTGTKnHZMZM5H830EWfLNt2AoYXb-npyS3DWWs3YA19poJV3wQi7hSkeZdMdVy22m24LPUUzU4J8h_KmFI1Wg3soZjG-rEOKy65Ho_-njN2Nh76_1vg5yGEJVIfqgKizko8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاوةُ جزءٍ من وصية الإمام الخميني على لسان القائد الشهيد للثورة الإسلامية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/78614" target="_blank">📅 15:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 05-06-2026 تجمّع لجنود جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/78613" target="_blank">📅 15:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اعلام العدو: طائرة بدون طيار مفخخة سقطت في موقع عسكري مستحدث في جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/78612" target="_blank">📅 15:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اعلام العدو:
طائرة بدون طيار مفخخة سقطت في موقع عسكري مستحدث في جنوب لبنان.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/78611" target="_blank">📅 15:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdDu10DU6h0BTAT8ICOlIBgd8LBNZjaHR4pSCy-bmZYqZ2ybGlRydJea5QpoQ-puJn3-JeiBjoFYvof-bD8ldsqIRmgscfSpXCypkkiEFN5gjbItoR6ZWju68Lb0B-GmFUbfPFlAykN-khiXoIvpqvw6pz7HbnRLDIb0hb8CH7yeHrXOpnTXqQ-G1sq9wTNwTXZFoPx1kvwHyWlvrVDoMTaXM13fGYcXd7CtMf6AKVX_DpxwUWJWWX8JYi_2K3sW-yf55vUiJvZk4dsX8I_Xz1sHqHInJmKfj2Gntf3g9Oh9Fa3T476bJeL2H6AqJntD8Z_sqJRfzP2ja0ZtpaCCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">١٣/٦/٢٠١٤
🇮🇶
اعظم يوم بتاريخ العراق المعاصر ؛ ذكرى تاسيس المؤسسة الأكثر عطاء في العالم انهم قوات الحشد الشعبي اليد الضاربة للشعب العراقي .</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/78610" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">استهداف سفينة في بحر عمان</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/78609" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئيس الوزراء الباكستاني: توقيع الاتفاق بين ايران والولايات المتحدة سيكون الكتروني.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/78608" target="_blank">📅 14:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">استهداف سفينة في بحر عمان</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/78607" target="_blank">📅 14:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رئيس الوزراء الباكستاني:
توقيع الاتفاق بين ايران والولايات المتحدة سيكون الكتروني.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78606" target="_blank">📅 14:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce9584a4b.mp4?token=Sx5nhlRbWIGBgblfOb3SZEoS6-fXeVWopwOSiyt89aB_bbPbJdJ51fOLlNx8XwQLhiV3fgKLupJBHttNpYESQL9qmAi6K5EJtH5Bf_TD-DwR6W3sECitwsNL9WY734rd9610nmVvOHOdI9xiXCn15Zf9mZZJZh19HzycUSsZy1m8yXKtCtagwolvzxMOvUbR1vGZy3tunU8u_xRyGRjftMXoHiNiLn4xzZDa9eoCQlWOxKi3pyWyYaidPM1i8alaYFkW0ghHqobGVdtXTwnNJbTsedlhXYdux-_YXV5Sq8Fn8HNLaGFIQjWn4J6j7o84GX8P-hF-t6SpYR3dWas9Mx_TPS2jy9Son-5HJXIy7IFdhSNNb1XIzrSKpXDFr_-bH9ALbrOz4Xna6anfoZBEpO-9jCtSL6mo5fEHVOxkqSrvrepFn3gSk3R9SfWiPCBr8ZQCXEyxmd4ZQ-d4tObSYLa9alDdYD1Udz2siknmO48z0-i-wMTCGTaIF9j7pdwMhcY7YTenl1eA2JPJA8U1aMfBnFuCS5llhHkiYsN6TAOEhTFY_HLiDDT-JgC8OE7Luz7m45a5Bopvz6olSdZdAJbl-wjwvAxRdQjoBpQiJ39vc_X-Rw_2bQWq2LSLl5UN_7rsWCOcRrbtqKsSPToM5-wvBaRvpVBaJzEJvy51BZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce9584a4b.mp4?token=Sx5nhlRbWIGBgblfOb3SZEoS6-fXeVWopwOSiyt89aB_bbPbJdJ51fOLlNx8XwQLhiV3fgKLupJBHttNpYESQL9qmAi6K5EJtH5Bf_TD-DwR6W3sECitwsNL9WY734rd9610nmVvOHOdI9xiXCn15Zf9mZZJZh19HzycUSsZy1m8yXKtCtagwolvzxMOvUbR1vGZy3tunU8u_xRyGRjftMXoHiNiLn4xzZDa9eoCQlWOxKi3pyWyYaidPM1i8alaYFkW0ghHqobGVdtXTwnNJbTsedlhXYdux-_YXV5Sq8Fn8HNLaGFIQjWn4J6j7o84GX8P-hF-t6SpYR3dWas9Mx_TPS2jy9Son-5HJXIy7IFdhSNNb1XIzrSKpXDFr_-bH9ALbrOz4Xna6anfoZBEpO-9jCtSL6mo5fEHVOxkqSrvrepFn3gSk3R9SfWiPCBr8ZQCXEyxmd4ZQ-d4tObSYLa9alDdYD1Udz2siknmO48z0-i-wMTCGTaIF9j7pdwMhcY7YTenl1eA2JPJA8U1aMfBnFuCS5llhHkiYsN6TAOEhTFY_HLiDDT-JgC8OE7Luz7m45a5Bopvz6olSdZdAJbl-wjwvAxRdQjoBpQiJ39vc_X-Rw_2bQWq2LSLl5UN_7rsWCOcRrbtqKsSPToM5-wvBaRvpVBaJzEJvy51BZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على ذمة اي نيوز
سجلت محافظة المثنى ضمن اكثر المحافظات فقراً ؛ ٣٦ مليار من واردات بلدية المثنى وتم تسجيلها من ديوان الرقابة المالية تسرق من رئيس هيئة الاستثمار بالمحافظة بعد بقائه منذ ٩ أعوام  .</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/78605" target="_blank">📅 14:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-06-2026 تجمّع آليات وجنود جيش العدو الإسرائيلي في بلدة القنطرة جنوبيّ لبنان بصاروخٍ نوعي.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/78604" target="_blank">📅 14:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f58e3487.mp4?token=guXDMyozIVkYpAvgCsTSp4UkP60abEVZQGOvw88Vx2hjkVY1MqG87BdKnffS8CIz47nAn8coANUJwJFM6GnbkgsF3j_8au8snmj9CchPFQkw9jgNFoBNkuUy3xpwFbSIIG3Fg7PNhOVxEEFsFKp1Vag5oSQYiH6yg1U9ycFm-aPkA_iqXP5zYw_90V0vPM6L94oXTclvoGJGYNLahJtqUjJICJnt5mR_QFH-OPPHsuS__ij7FaA4oKqb66R_bydLabj8hnzJQ6y-s9JI_c7daaUTQciCXeQ5eOPYYVvDDYHjo9N0ZZKzMU9jlTDYYta1COcQ7tW2jn_m7OIcell2nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f58e3487.mp4?token=guXDMyozIVkYpAvgCsTSp4UkP60abEVZQGOvw88Vx2hjkVY1MqG87BdKnffS8CIz47nAn8coANUJwJFM6GnbkgsF3j_8au8snmj9CchPFQkw9jgNFoBNkuUy3xpwFbSIIG3Fg7PNhOVxEEFsFKp1Vag5oSQYiH6yg1U9ycFm-aPkA_iqXP5zYw_90V0vPM6L94oXTclvoGJGYNLahJtqUjJICJnt5mR_QFH-OPPHsuS__ij7FaA4oKqb66R_bydLabj8hnzJQ6y-s9JI_c7daaUTQciCXeQ5eOPYYVvDDYHjo9N0ZZKzMU9jlTDYYta1COcQ7tW2jn_m7OIcell2nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">١٣/٦/٢٠١٤
🇮🇶
اعظم يوم بتاريخ العراق المعاصر ؛ ذكرى تاسيس المؤسسة الأكثر عطاء في العالم انهم قوات الحشد الشعبي اليد الضاربة للشعب العراقي .</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/78603" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78601">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
🇮🇷
خلال دقائق، سيُعلن مكتب حفظ ونشر آثار قائد الثورة الإسلامية الشهيد تفاصيل مراسم الوداع والتشييع والدفن للإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، وذلك عبر بيان رسمي يصدر عن المكتب</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/78601" target="_blank">📅 13:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">To Zendei (Echoes Of An Eternal Life)</div>
  <div class="tg-doc-extra">Ehsan Yasin - Ehsan Saeedi</div>
</div>
<a href="https://t.me/naya_foriraq/78600" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">أنشودةٌ موسيقيةٌ بلا كلام «أنت حيّ»
هديةٌ قُدِّمت بمناسبة أربعينية الشهادة إلى الإمام الشهيد خامنئي الكبير، ذلك الروح الطاهر السماوي
نغمةٌ تكسر اختناق الدموع المكبوتة طوال هذه الأربعين يومًا…
#شاركها</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/78600" target="_blank">📅 13:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نايا - NAYA
pinned «
🇮🇷
🇮🇷
خلال دقائق، سيُعلن مكتب حفظ ونشر آثار قائد الثورة الإسلامية الشهيد تفاصيل مراسم الوداع والتشييع والدفن للإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، وذلك عبر بيان رسمي يصدر عن المكتب
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/78599" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
🇮🇷
خلال دقائق، سيُعلن مكتب حفظ ونشر آثار قائد الثورة الإسلامية الشهيد تفاصيل مراسم الوداع والتشييع والدفن للإمام المجاهد الشهيد سماحة آية الله العظمى السيد علي الخامنئي (قدّس الله نفسه الزكية)، وذلك عبر بيان رسمي يصدر عن المكتب</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/78598" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🙃
🇮🇷
فضيحة من العيار الثقيل
زلينسكي الذي لم يحمي سماء كييف ولا خاركيف يريد ان يضحك على بعض دول الخليج التي فشلت منظوماتها الأمريكية بالدفاع عن سمائها في المواجهة الأخيرة مع ايران ؛ من خلال التسويق لمنظومات أوكرانية مستخدما تطبيقات الذكاء الصناعي وفديوهات معدلة ف " جيران  " النسخة العكسية عن شاهد ١٣٦ أصبحت الزائر اليومي للقطعات العسكرية الاوكرانية المدعومة من حلف الناتو دون وجود اي حلول ممكنة للتصدي لها كيف سيؤمن سماء البحرين والسعودية ؟!
😆
الحل الأفضل هو اتباع الطريقة الاماراتية دفع أموال لايران و ضمان عدم استخدام أراضيهم كمنطلق للعدوان .</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/naya_foriraq/78597" target="_blank">📅 13:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-VAcIzQ3P-PvAfSGo6A6DXFeySWw1ds6BPDVy7EfEepaZGJ7O9E3G-NpJJ2amOEin7-HT0jWEcpbOZo9NX6NNDd2IueHDpnm5Un_X-z7QdhguFUSp-gzeqYakvUCDKrNG5UnSTxNJGxF6pdWK4J0rhxfBl-2JeW4qWIll7H9Ghnw9lZMB5L4zHwIBaVsLSs59OjgV2OgcY0GgJ2SYVSp9wU15LW6vamwx4Ft-a-EcIwuF6ktZXcrF63YXae35bYMUX7xE5oiEnKhREe8VZygbcb9ZqP7edQRB4z5PtH_xAPC9iGzMSNo0EuQXlcSY9a2-makTq97iJmpxdEFdysMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙃
🌟
صدور مذكرة القاء قبض وتفتيش بحق مهند الزبيدي مدير مدرسة النعمة العراقية في العاصمة الاوكرانية كييف اضافة الى موظف وموظفة في وزارة التربية العراقية على خلفية تورطهم بعمليات تهريب الدفاتر الامتحانية المدرسية الى الخارج.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78596" target="_blank">📅 12:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏نواف سلام: مشكلتنا مع حزب الله هي سلاحه وعليه أن يكون قوة سياسية فقط
من المفترض أن يكون الجنوب اللبناني خاليا من السلاح</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78595" target="_blank">📅 12:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a0766e31.mp4?token=EFmVUXgHppUu03n6ePZttDBS716cKh1mJ3W11gJytvAm36ubAlZld6BS-L6LCHEbtSeJKz1lCw7n1K1BNdB9Pzmk5ez1Q93lcp1B3oEQtrQZ7ob0R6c7xsRcdTfcJnUsIWD4n8uPeuxU3xVjppXm3HF-cL0wJY_nneZzE3fQ-7JIpo_uJ4mc8OZlWFSYrHDbG0u8yDpTyTV8cZYrJ9-aG1B-AL1cnSBRcAikOsjT-Xr5e9V1lHTASSsxItxE3a34eAiwUC2kvxYDf9CJuT0gcPTZP94OW744bGnu1jHnTL1IcRHFIuTKGu68C11byohYCAFMyy7-R6V_g8C5bQ5TGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a0766e31.mp4?token=EFmVUXgHppUu03n6ePZttDBS716cKh1mJ3W11gJytvAm36ubAlZld6BS-L6LCHEbtSeJKz1lCw7n1K1BNdB9Pzmk5ez1Q93lcp1B3oEQtrQZ7ob0R6c7xsRcdTfcJnUsIWD4n8uPeuxU3xVjppXm3HF-cL0wJY_nneZzE3fQ-7JIpo_uJ4mc8OZlWFSYrHDbG0u8yDpTyTV8cZYrJ9-aG1B-AL1cnSBRcAikOsjT-Xr5e9V1lHTASSsxItxE3a34eAiwUC2kvxYDf9CJuT0gcPTZP94OW744bGnu1jHnTL1IcRHFIuTKGu68C11byohYCAFMyy7-R6V_g8C5bQ5TGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: السكان والزوار الموجودون على الشواطئ الجنوبية لايلات يبلغون عن سماع إطلاق نار من جهة البحر</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78594" target="_blank">📅 12:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📰
تقرير شبكة CNN:  في الأسابيع الأخيرة، زادت إيران بشكل كبير من جهودها لسد الوصول إلى مخازن اليورانيوم المخصب  وفقًا لخمسة مصادر مطلعة على الاستخبارات الأمريكية، تسببت إيران عمدًا في انهيار أنفاق وزرعت ألغامًا عند مداخلها باستخدام متفجرات  وفقًا للمصادر، أصبح…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78593" target="_blank">📅 11:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📰
‏بلومبيرغ: إيران أضافت على الأرجح أسلحة روسية حديثة لمخزوناتها خلال وقف النار</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78592" target="_blank">📅 11:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📰
تقرير شبكة CNN:
في الأسابيع الأخيرة، زادت إيران بشكل كبير من جهودها لسد الوصول إلى مخازن اليورانيوم المخصب
وفقًا لخمسة مصادر مطلعة على الاستخبارات الأمريكية، تسببت إيران عمدًا في انهيار أنفاق وزرعت ألغامًا عند مداخلها باستخدام متفجرات
وفقًا للمصادر، أصبح الوصول إلى مخازن اليورانيوم المخصب الآن أكثر صعوبة وخطورة ويتطلب وقتًا أطول مما كان عليه قبل شهر فقط</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78591" target="_blank">📅 11:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: توجد فجوة شاسعة بين نظرتنا إلى أنفسنا والصورة التي تُرسم لنا في الخارج ؛ يُنظر إلى "إسرائيل" في الخارج على أنها بلطجي الحي وتُعتبر تهديدًا للاستقرار والسلام العالميين.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78590" target="_blank">📅 10:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🏴‍☠️
تسلل مسيرات من حزب الله نحو المطلة شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/78589" target="_blank">📅 09:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad3b3f7e1.mp4?token=oKexbVTnwOzCsX76uJLVrOyoI4tD2InQAlv8pf7lPGUdkve0HOZwU9oSM0nBuY3wwwOF_38DTMWbE6IK9maGRf6cDkutrEOdB05uoxkCcvuDzyRsCNwdelcR-1p0N3tl9LKRRQWqcpgUs7CHalbnIjbIJDa93njIxblQ8j5kUWVihYwUbxRgQ38yNzes3hRe1k5Qn9SW68MP25ea3U7gtlWnE9atNB6q00zXDoXm4t-xgGvNnztbJU1ClEJ3Vl_1cABmipqDBCIJ1F_GIAYR0OihwEAP8NDddtnDPoYBeDjj-6VwQFDmMj8UWiX0s3LW9XrwvcW6Svq_LMOVaHVSGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad3b3f7e1.mp4?token=oKexbVTnwOzCsX76uJLVrOyoI4tD2InQAlv8pf7lPGUdkve0HOZwU9oSM0nBuY3wwwOF_38DTMWbE6IK9maGRf6cDkutrEOdB05uoxkCcvuDzyRsCNwdelcR-1p0N3tl9LKRRQWqcpgUs7CHalbnIjbIJDa93njIxblQ8j5kUWVihYwUbxRgQ38yNzes3hRe1k5Qn9SW68MP25ea3U7gtlWnE9atNB6q00zXDoXm4t-xgGvNnztbJU1ClEJ3Vl_1cABmipqDBCIJ1F_GIAYR0OihwEAP8NDddtnDPoYBeDjj-6VwQFDmMj8UWiX0s3LW9XrwvcW6Svq_LMOVaHVSGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
عدوان صهيوني على حي الراهبات جنوب لبنان</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/78588" target="_blank">📅 08:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDfckSiuRps_EqH_5eTK30OfaTCg3snWJuY4MbmC-dvoTXvTQg3D52-Zue1cRTDfrISBWr_UykogrjT-u1rBeb3KJHAKeiArBdydcWWZU8qunrawaSNHyInR_rGbBtE8L1VfBsg8ORNmirzV8GbUBZ5bk3SI-GTiSdjFXUCk0pN6Hv-RaT6S7MHUXhPWmcCrzKtjBrDol_sRYTZdbzlMJX8SN5ZLAcqmqrE-plp5D42mqIIsdOj4bIJsA8VR5BGGbHxG71gM0VJ0wRSN5qPbbnC_T9ziGdO9n-3t1vCeD2eyiFwVHRyPgyN_YxBr3LPPze-DNNA2hFse7umBIdObKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: هبوط مروحيات إجلاء في مستشفى الوادي العفولة شمال الكيان بعد نقل جنود مصابين من جنوب لبنان جراء تعرضهم لحدث أمني صعب.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78587" target="_blank">📅 07:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📰
وول ستريت جورنال
: محادثات فنية إضافية بشأن قضايا شائكة قد تجري بعد ذلك في إسلام آباد، جي دي فانس سيتوجه إلى جنيف لتوقيع مذكرة التفاهم مع إيران، عودة وفد قطري من طهران الأسبوع الماضي حاملا صيغة اتفاق جديدة شكلت نقطة تحول حاسمة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/78586" target="_blank">📅 04:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186c1827aa.mp4?token=pOZ8q1iEfXUiBlrkG39qgYNQCdJxX2VktznkU317wM7I4kE2YAk4A4Cx-mSrO9OwyGr1zKmtCdNpPy1R17rckNQaDr8RSY7MG47xnGDz-mQTzH4ad4h7wCe_fGj5u3wHnE3UKm_BbQBeidk84Hwa2-xSb1LokiGZ1IiWDWYsuHoxqRqtRaDJVQPR8pM9M5QPTqH9MM0kLL72oZRJFg1yhYggucPAzye29F4xXjR8PMoU87YNuhggDvOzJCy0Rarh0ezxM9_lzNp3ACf7_x5gqK3tc3RRjT82OqpQOjFXXiJE3BzOR6K6ofO-EPZAoK5u8lzCpG13aviBr9oTrsJvaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186c1827aa.mp4?token=pOZ8q1iEfXUiBlrkG39qgYNQCdJxX2VktznkU317wM7I4kE2YAk4A4Cx-mSrO9OwyGr1zKmtCdNpPy1R17rckNQaDr8RSY7MG47xnGDz-mQTzH4ad4h7wCe_fGj5u3wHnE3UKm_BbQBeidk84Hwa2-xSb1LokiGZ1IiWDWYsuHoxqRqtRaDJVQPR8pM9M5QPTqH9MM0kLL72oZRJFg1yhYggucPAzye29F4xXjR8PMoU87YNuhggDvOzJCy0Rarh0ezxM9_lzNp3ACf7_x5gqK3tc3RRjT82OqpQOjFXXiJE3BzOR6K6ofO-EPZAoK5u8lzCpG13aviBr9oTrsJvaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب
:
"بتوجيهاتي، نفّذت القيادة الجنوبية للولايات المتحدة ضربةً سريعةً وقاتلةً أسفرت عن إعدام نينيو غيريرو، الزعيم سيئ السمعة لجماعة ترين دي أراغوا، إحدى أكثر المنظمات الإرهابية دمويةً على وجه الأرض. قبل عودتي إلى منصبي، فتح جو بايدن حدودنا الجنوبية أمام ملايين المجرمين غير الشرعيين، وسمح لهذا الجيش الأجنبي باغتصاب وتشويه وقتل مواطنين أمريكيين دون أي عقاب. خلال حملتي الانتخابية، تعهدتُ بطرد هؤلاء الوحوش من بلادنا، وتحقيق العدالة لعائلات ضحاياهم، بمن فيهم الطفلة البريئة جوسلين نونغاراي ذات الاثني عشر عامًا، ولاكين رايلي ذات الاثنين والعشرين عامًا، وعدد لا يُحصى من الأرواح البريئة الأخرى. بهذا العمل، حقق الجيش الأمريكي الانتقام لهم ولعائلاتهم وأحبائهم." في بداية ولايتي، وفيتُ بوعدي بتصنيف حركة ترين دي أراغوا منظمةً إرهابيةً أجنبية، وترحيل آلاف المجرمين الأشرار، وشن حربٍ على عصابات المخدرات التي لطالما شنت حربًا على مواطنينا، بينما ترك القادة الضعفاء أمريكا عاجزةً في موقف دفاعي. وقد تم تنسيق هذا الإجراء بشكل وثيق مع أصدقائنا في فنزويلا، الذين نتعاون معهم تعاونًا مثمرًا. ونتيجةً لذلك، لم يعد لإرهابيي ترين دي أراغوا ملاذٌ آمن في فنزويلا أو أي مكان آخر، وسنجد هؤلاء القتلة المتوحشين وتجار المخدرات في أي وقت وأي مكان، وسنرسلهم إلى قعر الجحيم حيث ينتمون. حفظ الله أمريكا! الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/78585" target="_blank">📅 04:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
رويترز
: أطلقت الولايات المتحدة صواريخ على العديد من طائرات بدون طيار الإيرانية أحادية الاتجاه أثناء توجهها إلى مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/78584" target="_blank">📅 04:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌟
اعلام العدو:
ترمب أصدر تعليمات بتخفيف العقوبات عن إيران إذا التزمت بالاتفاق.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/78583" target="_blank">📅 03:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rth0qX4XPCFcMA1VHGlO2eKJBtC7Yl8WPde_DphJXUANNKNktLa9Rpnor6DZku8Nn8dbTkz3ece7oPF8-QP_qTp1ytU7RK3pddgRLP2n4B_5v9NIdmqYCM0zRENwuuL9GPB0PN7irW5EQNVkwFX2Y0B3qtr4158rHhKAD5rcxtfigcdbu-xskr-qN7yKfLwQqDFLw6Xvecxvo5DyqkF2B1Syy9CuPVYvqG3Ka-A1O630HMDpJKKPWrhOoKmeiyir8lXgB81-X21A1FGEw3RlI-Y0oStVCdaw9KMM4apo04O2Xk61gmhDPsASNoRx1RyqNnZsg35JXb32L1FFWyIeiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8VfQE7yx_myPIe_PmTV9orteAYjoxlT6v2YLx6QS-CYSTedURRuJL_-8NKlkTQNOWEsTGtCOPRCJ-PL_aQHp-Z6OOgPXqj4851eEFLGZeUGWLGstw55pBX4njFL-b_2snfhjYwhYtlISyAA7OLHZZp0fHzqqBvrL5xsjdmvo3_pkGziWkUS-uxBTTCwHb9JAfJeUf0urvMi8tB0Lois5OFruqaLwhLoiK1hKEc8lagFXeV-ps1I7FpTp8U60VHMC8Aw_9eFMAV8tz988YFraPuryzj9-_z2sBxuzzoqAm45Wr4i4-ahzqOlS26XTOABLnjYSE45fx2t6HTwplRdpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
عُثر على جثة في صندوق سيارة متوقفة عند ملعب كالينتي بالمكسيك، وهو ملعب تدريب المنتخب الإيراني.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/78581" target="_blank">📅 03:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78580">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇬🇧
🌟
المحكمة البريطانية تحكم بالسجن 29 عامًا على شابين كرديين من شمال العراق بعد إدانتهما باستدراج فتيات قاصرات والاعتداء عليهن جنسيًا في دونكاستر، فيما تواصل الشرطة البحث عن متهم ثالث ما زال فارًا.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/78580" target="_blank">📅 02:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78579">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
أكسيوس: نتنياهو وجد نفسه خارج كواليس التفاوض ولجأ إلى الاتصال بحلفاء في واشنطن لجمع المعلومات.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78579" target="_blank">📅 01:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
أكسيوس: منشور ترمب يوم الخميس الذي أعلن فيه التوصل إلى اتفاق مع إيران فاجأ نتنياهو.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78578" target="_blank">📅 01:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
أكسيوس: نتنياهو بدا أنه أدرك خلال الاتصال مع ترمب أنه لا يستطيع منعه من إبرام اتفاق مع إيران.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78577" target="_blank">📅 01:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
أكسيوس: ترمب قال في اتصال مع نتنياهو الخميس إن الصفقة مع إيران رائعة وحان الوقت لإنهاء الحرب.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/78576" target="_blank">📅 01:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌟
أكسيوس
: ترمب قال في اتصال مع نتنياهو الخميس إن الصفقة مع إيران رائعة وحان الوقت لإنهاء الحرب.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78575" target="_blank">📅 01:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏الإمارات تنفي بشكل قاطع بشأن نقل أموال إلى الجمهورية الاسلامية الإيرانية كتعويض، مشددة على أنه لم يتم الإفراج عن الاموال أو تحويل أو نقل أي أموال إيرانية مجمدة عبر الإمارات.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/78574" target="_blank">📅 01:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: أصوت الانفجارات قرب ميناء سيريك ناجم عن إطلاقات تحذيرية أطلقت نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78573" target="_blank">📅 00:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKN-0rrPNC_QKoQeYPD13wx3-t3ivmF3aW71bmOIA3wKzwX33PO-X9-eGlvO1R9gZGHc5jCyMGPKAU7GXRkXY6nFFsO3va6xms2O6ZOV8OVsnH9VTk6zk6bk1gaS9tAUL7xJLWoZs8rtrAmu7klIi0cWNREX5NJblUXGqznzBKkdFDnB3-0VDeWNxz0fiQYUmRYVnARQzLYJPo9wss4_7BOkjTOujY2n0pDhjRHB6J1Jl_SaXlJBaqVqx4LGKeb0ZELpbW6pjBpXewL7RNkJDkbQfY2-AMB1k0O7oFRnHcEFLsFyD79KSLPa4eOCFHWG2UbqvEU-brvujwDYRQN1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: أصوت الانفجارات قرب ميناء سيريك ناجم عن إطلاقات تحذيرية أطلقت نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/78572" target="_blank">📅 00:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">أنباء أولية: سفن حاولت العبور من مضيق هرمز وتم استهدافها من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78571" target="_blank">📅 00:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سماع دوي انفجارات في قشم وسيريك وأنباء عن اشتباكات بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/78570" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78569">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سماع دوي انفجارات في قشم وسيريك وأنباء عن اشتباكات بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/78569" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_GX2ccG-in-hXyPw4P0ickoiw9vn9DWuv6ranr2jGciDfTFoSqB1YSIek_TUSMhHqOnS-c87cbqAMoC1jZUORIg7TXDpGPVkV7QakACj-qjZQ5s8WfhHfBN7-MfjVgvFc0QI-ElBHdsTydDNSc74bzIWG9bPU57j_Xn5OkcFUCT2yGdfd4oRFeR5RdiQgn5r3usuOcEpigsbfJjpW7gW24TvGM66LiO780ri8ybCwvwLleWhWNI8hC_nKIKH3bgbME0xZOAwypjagXZCs-iWp3NGUu7MsWkdhqFfF0IvLIMntXI9VRX7SNhQ_UR-75NUVpKchPvZ-Wtx6EdWYojCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
رئيس حركة حقوق
النائب حسين مؤنس:
قرابة 600 مسجد شيدت مؤخراً في أبو غريب وحزام بغداد ناهيك عن المحافظات الغربية ، تستغل لنشر الحركة المدخلية ضمن مشروع منظم يُراد له التشويش على المذاهب الإسلامية المعتبرة، وإنتاج توجهات وشخصيات فكرية منحرفة.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/78568" target="_blank">📅 00:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
وزارة الدفاع الإيرانية:
نحن على أهبة الاستعداد للدفاع عن الشعب الإيراني بكل قوة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/78567" target="_blank">📅 23:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78566">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d230a970a.mp4?token=MxCohbd8Nth8nwQH5f53rcGxkKJZkQPPMIngpEuw5sReoraosMHr0yOAcHQm95DV85QYEEHpTJ7W44MN2mgFIX4vqKolVMX4UpbOMxQA0zcYsqw_YLNcmD7QIdW9CWr0T-TRoKcnuxsbyd1jRlTMkC7Fs_PCFIAj-hF0mPAj3pj6Tq0PEO3Q7oI5t7VqYdVcdd_NxKX0OCbj2Y5u_EC7Uu2Cz_SIto8_ljTLMyclbzly8wwDGEcDYTV2s41djrcjzHSWM6_s8-ZwuMzF3vO6hZQE8umUOjkEV_J5_3MN5463Tmj684nvoQjuHrrsGK78fUnYG7BF1PVvz9O5Pm6F9HYd8Vd8_C1I7QTSj1GodUpJ-s5zmRmgTSeQXS07QFncOvo6VZpJRvUtWNdZImiOGrVDO3DBPEH_ATgxkhRUGeHrJShAncY-h_9Yi6dQaEUu3IeSa0ZdYC3RV6U3CMkYby7dcl03eb3KzkgmZlG6BINX6YioUfYknj0DCVK_63FDROqL9HDhkjrmPHOghrSvAsRAzhybUqC8ZuWg2jBEqrrU7G512jEUFcSkB07ZptBiAI7QXaY-rBjdCK2-hfHZgK99DgOEwgqD1imiKhOj8e1opTIjGVFC3GpTjmq3UhpFXcQm8o56GjchRstd5TvV9nqDjhZu9EPaAELezmYWzRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d230a970a.mp4?token=MxCohbd8Nth8nwQH5f53rcGxkKJZkQPPMIngpEuw5sReoraosMHr0yOAcHQm95DV85QYEEHpTJ7W44MN2mgFIX4vqKolVMX4UpbOMxQA0zcYsqw_YLNcmD7QIdW9CWr0T-TRoKcnuxsbyd1jRlTMkC7Fs_PCFIAj-hF0mPAj3pj6Tq0PEO3Q7oI5t7VqYdVcdd_NxKX0OCbj2Y5u_EC7Uu2Cz_SIto8_ljTLMyclbzly8wwDGEcDYTV2s41djrcjzHSWM6_s8-ZwuMzF3vO6hZQE8umUOjkEV_J5_3MN5463Tmj684nvoQjuHrrsGK78fUnYG7BF1PVvz9O5Pm6F9HYd8Vd8_C1I7QTSj1GodUpJ-s5zmRmgTSeQXS07QFncOvo6VZpJRvUtWNdZImiOGrVDO3DBPEH_ATgxkhRUGeHrJShAncY-h_9Yi6dQaEUu3IeSa0ZdYC3RV6U3CMkYby7dcl03eb3KzkgmZlG6BINX6YioUfYknj0DCVK_63FDROqL9HDhkjrmPHOghrSvAsRAzhybUqC8ZuWg2jBEqrrU7G512jEUFcSkB07ZptBiAI7QXaY-rBjdCK2-hfHZgK99DgOEwgqD1imiKhOj8e1opTIjGVFC3GpTjmq3UhpFXcQm8o56GjchRstd5TvV9nqDjhZu9EPaAELezmYWzRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
وزير الداخلية الأمريكي:
كانت كاليفورنيا تعتمد على النفط القادم من مضيق هرمز. سيكون لديهم أسعارًا مرتفعة للبنزين.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/78566" target="_blank">📅 23:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">طيران مسير من لبنان يهاجم الشمال محتل</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/78565" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba9b3581f.mp4?token=inq-ffxm_zJdKGifTnj0DNpRoF1sadRO-V6fETrkz4UcCd5CQyQX7lGe2uaKhuzpB7-bjlaH8i5J_D-iMlmr49tZkCsciI73fHyWajeXjMzTWO0JktAL6RAIjBhrj2v5yhYO1vYOq-GAlYo5uo4VbzbcLDbEUd0MEXzODue28xwYFFvJcdBpwhnWG0oJGGeYO_5_vRyG4fkRy3DgunSdT9Drgg7A_3bAcoSGR-taK50SqqjLlMmFcpVlfWhct3rUab05ZwaXgJDMKeZy5C6hMEbXC5dZOs4M-Tc-h1n52KEA_UUNyYQsbLgHChLsNwTshac4cde2zfgqgwt6l0-jVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba9b3581f.mp4?token=inq-ffxm_zJdKGifTnj0DNpRoF1sadRO-V6fETrkz4UcCd5CQyQX7lGe2uaKhuzpB7-bjlaH8i5J_D-iMlmr49tZkCsciI73fHyWajeXjMzTWO0JktAL6RAIjBhrj2v5yhYO1vYOq-GAlYo5uo4VbzbcLDbEUd0MEXzODue28xwYFFvJcdBpwhnWG0oJGGeYO_5_vRyG4fkRy3DgunSdT9Drgg7A_3bAcoSGR-taK50SqqjLlMmFcpVlfWhct3rUab05ZwaXgJDMKeZy5C6hMEbXC5dZOs4M-Tc-h1n52KEA_UUNyYQsbLgHChLsNwTshac4cde2zfgqgwt6l0-jVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقجي: أول ما ورد في الاتفاقية هو رفع الحصار البحري الأمريكي.  سيتم الإفراج عن أصولنا المجمدة.   أُدرجت مسألة التعويضات والأضرار في خطة إعادة الإعمار.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/78564" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78563">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عراقجي:  مضيق هرمز بلا شك تحت سيادة إيران وسلطنة عمان ولا يوجد ممر مائي دولي في مضيق هرمز.  مستقبل إدارة مضيق هرمز لن يكون كالسابق. لا يمكن لأحد أن ينتقص من سيادة إيران وسلطنة عمان على مضيق هرمز.  لن تكون إدارة مضيق هرمز كما كانت في السابق (قبل الحرب).   ستصدر…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/78563" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عراقجي:
مضيق هرمز بلا شك تحت سيادة إيران وسلطنة عمان ولا يوجد ممر مائي دولي في مضيق هرمز.
مستقبل إدارة مضيق هرمز لن يكون كالسابق. لا يمكن لأحد أن ينتقص من سيادة إيران وسلطنة عمان على مضيق هرمز.
لن تكون إدارة مضيق هرمز كما كانت في السابق (قبل الحرب).
ستصدر إيران وسلطنة عمان قريباً بياناً مشتركاً بشأن إدارة مضيق هرمز.
سيبقى سيفنا حاضرًا دائمًا فوق مضيق هرمز، وستدخل القوات المسلحة الإيرانية عند الضرورة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/78562" target="_blank">📅 23:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78561">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01cf391ca6.mp4?token=DmcLRsr0izkAh8vkuc0_ZidnfgxOIse5ZenhcrhP3dHfSFlYD6vsYwwmdYu5TCsgz3XLoK2obqbKMNjNWjpHT0sAhEXL1AdPam68kyD6WlFFrxIzDkYH7cdwh31Aee75PoFGtX9ONo6ZlZ5gZXrepZZNYNWvdUSm_XwGD-5PSKOeBJhXpAaBhSEEbboLti7cLhmgEuKn37TVwJyjdTjIjmqroFB-XQR0fs00pCSc9UbS0S972Rgr2Edn64kQIKC4_tRh7t7Fxm5iGWqCgz1YhxTHHQZatXY9IQn3mGpKLFYbd1PVzjbSyCpaEFzwqtXvLxpTNqrcK98QmIn66IdY9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01cf391ca6.mp4?token=DmcLRsr0izkAh8vkuc0_ZidnfgxOIse5ZenhcrhP3dHfSFlYD6vsYwwmdYu5TCsgz3XLoK2obqbKMNjNWjpHT0sAhEXL1AdPam68kyD6WlFFrxIzDkYH7cdwh31Aee75PoFGtX9ONo6ZlZ5gZXrepZZNYNWvdUSm_XwGD-5PSKOeBJhXpAaBhSEEbboLti7cLhmgEuKn37TVwJyjdTjIjmqroFB-XQR0fs00pCSc9UbS0S972Rgr2Edn64kQIKC4_tRh7t7Fxm5iGWqCgz1YhxTHHQZatXY9IQn3mGpKLFYbd1PVzjbSyCpaEFzwqtXvLxpTNqrcK98QmIn66IdY9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
إيران لاتترك حلفائها.. عراقجي: انسحاب جيش الاحتلال من جنوب لبنان ضمن الإتفاق</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78561" target="_blank">📅 22:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عراقجي: تُعرض نصوصٌ مختلفة في وسائل الإعلام، وتُثار ادعاءاتٌ متباينة. وقد أكدنا، نحن والأمريكيون، أن هذه النصوص غير صالحة في الوقت الراهن، ولا نوافق عليها.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78560" target="_blank">📅 22:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عراقجي: إن مسألة مضيق هرمز ورفع الحصار البحري واردة في مذكرة التفاهم. وقد طُرحت مسألة إعادة الإعمار في صورة خطة لإعادة الإعمار والتنمية الاقتصادية، وسيتم الاتفاق على آلياتها في مفاوضات لاحقة. كما يجري النظر في آلية لأموال إيران المجمدة. وعند الانتهاء منها،…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78559" target="_blank">📅 22:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78558">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عراقجي:  سيتم اعلان نهاية الحرب بكافة الجبهات بالتحديد لبنان.  ‌ سيتعهد العدو بعدم إشعال حرب أخرى، وعدم استخدام التهديدات أو القوة، وأن يحترم الطرفان سيادة بعضهما البعض، وأن لا يتدخلا في شؤون بعضهما الداخلية.   لن نترك حزب الله في لبنان وحيداً.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78558" target="_blank">📅 22:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de96c18531.mp4?token=LA22DyNDULfOv0gkz2fEXAT8n-STTZqTgUEBuwJB1cgTxy9BWraSgSNgFHTLr7mCoLAASHEW6WA46Kj2a2nK2YVZThgt-RdrOpMKPPd00Eti4p4qdEWzyyx5GynNxnR3yJH8pPE8csu_v9zcP1WLah1NX4JYqU81W6iKpzqq--R5yebS9Ys1bfrPY53G66dvnwP8smc4pKEqw7QgxOLFVNhN2K3Esq-CJANd1TPWlNtGF5UXcoAiEl4GFU9NwkwsDKVApLg1gYPv4TmF3PLvNXfQHz4LafTT7EqOA5warTEnoiod5caY31FG74qffKpfWX00hhQFGlLO-YLDUGN_IVRwSliPqVj1rAwhi9E9OUPED3soFx9Y_ZP-rbeU9U6XiphT1zres_7KiW1QJ914gQyyn88KD_-uShiujSbKskk1ZSpAtWVLs35eEsVxXNdIckfZWNqPHSTZ5QoVS3-XyKwK4SHYm5bUFCPCnQsmncjL1k0rCfhcljcYwdCtZG0s6zyeb3HFunH8u3s7_zVcqXur7kz9769vOoLB9Og-c3Pq8DdxVHqtmAebTFA6owxNCcTWzgLAp4P1p1UEkF2SIA3Sr_8CZa20-XsDOGjaC_gOmnqZPpbGDDrJ21aU95I6RBAzcEsFLH1xfbzM0nUObHEnxTYEkCrrh9ks3MSvSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de96c18531.mp4?token=LA22DyNDULfOv0gkz2fEXAT8n-STTZqTgUEBuwJB1cgTxy9BWraSgSNgFHTLr7mCoLAASHEW6WA46Kj2a2nK2YVZThgt-RdrOpMKPPd00Eti4p4qdEWzyyx5GynNxnR3yJH8pPE8csu_v9zcP1WLah1NX4JYqU81W6iKpzqq--R5yebS9Ys1bfrPY53G66dvnwP8smc4pKEqw7QgxOLFVNhN2K3Esq-CJANd1TPWlNtGF5UXcoAiEl4GFU9NwkwsDKVApLg1gYPv4TmF3PLvNXfQHz4LafTT7EqOA5warTEnoiod5caY31FG74qffKpfWX00hhQFGlLO-YLDUGN_IVRwSliPqVj1rAwhi9E9OUPED3soFx9Y_ZP-rbeU9U6XiphT1zres_7KiW1QJ914gQyyn88KD_-uShiujSbKskk1ZSpAtWVLs35eEsVxXNdIckfZWNqPHSTZ5QoVS3-XyKwK4SHYm5bUFCPCnQsmncjL1k0rCfhcljcYwdCtZG0s6zyeb3HFunH8u3s7_zVcqXur7kz9769vOoLB9Og-c3Pq8DdxVHqtmAebTFA6owxNCcTWzgLAp4P1p1UEkF2SIA3Sr_8CZa20-XsDOGjaC_gOmnqZPpbGDDrJ21aU95I6RBAzcEsFLH1xfbzM0nUObHEnxTYEkCrrh9ks3MSvSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقجي: المفاوضات مع أميركا ستتم على مرحلتين.  المفاوضات حول الموضوع النووي سيكون في المرحلة الثانية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78557" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عراقجي: حتى الأن لم يتم توقيع أي إتفاق.  سيتم نقل تفاصيل الإتفاق حين يتم بصورة نهائية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78556" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عراقجي: إيران خرجت منتصرة واقوى من هذه الحرب.  إيران كسبت انتصاراً استراتيجي في هذه الحرب.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78555" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">طيران مسير من لبنان يهاجم الشمال محتل</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78554" target="_blank">📅 22:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عراقجي: الدبلوماسية كانت بجانب القوات المسلحة في مواجهة العدو.  المفاوضات الدبلوماسية تعتمد على قوة القوات المسلحة وساحة المعركة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/78553" target="_blank">📅 22:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLU5gFx3u8oO25vq41gMKa0M4grZcyvWASgFA7kwnjlPLoMEQFXEkX5YwJJGduFwUNg_tn3MC5vDhePQfsyALBcZLPPrihpjGoBdmW0K_NKqs-kL0kOGtO3WP4PIFl1OzcQka2MR3hBxPy9chiueV0fLLhBDerZ7aXC1BuNuFZnQtsoXESsw9D8qWYxOXsQMvTX7RUTk-m-6RBbdh6bZONT-dFcoL74vP3C8HByvLeWq7Zqey_x-81w4VFlevSUOSt0kUnZqADIoiDImME_1-O21g4idAauijfqeqqaNA0vBjGUPgdXefvSK1ORvIZ3F1nw-Sd2D_LKo7vX2GbqaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف: ‏الالتزامات يجب الوفاء بها. لا مجال للتردد أو الأعذار. لإتمام الصفقة المرتقبة، لا سبيل آخر.
‏تحصد ما تزرع.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78552" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عراقجي: خلال سنة مررنا بحربين صعبين.  العدو ظن أنه يستطيع خلال حرب رمضان أن ينهي أمر النظام الإسلامي في إيران.  نحن جميعًا مدينون لكلّ القوات المسلحة ونحن مدينون أيضًا للشعب الذي لم يتركنا وشأننا، والذي يتواجد في الشوارع كل ليلة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78551" target="_blank">📅 22:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">عراقجي:
خلال سنة مررنا بحربين صعبين.
العدو ظن أنه يستطيع خلال حرب رمضان أن ينهي أمر النظام الإسلامي في إيران.
نحن جميعًا مدينون لكلّ القوات المسلحة ونحن مدينون أيضًا للشعب الذي لم يتركنا وشأننا، والذي يتواجد في الشوارع كل ليلة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78550" target="_blank">📅 22:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا لجيش الإحتلال الإسرائيلي في محيط بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78549" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
حسين الحاج حسن النائب في كتلة حزب الله البرلمانية:
ما تبلغناه بشكل واضح من إيران أن لبنان مشمول بوقف إطلاق النار.
تم إبلاغنا من مسؤولين إيرانيين أن إسرائيل ستنسحب من الأراضي اللبنانية وفق الاتفاق.
لن نقبل بالعودة إلى ما قبل 2 آذار 2026 على الإطلاق وليس لإسرائيل حق في البقاء بأراضينا.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78548" target="_blank">📅 22:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78547">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭐️
هنتر بايدن إبن الرئيس الأمريكي السابق جو بايدن:
لدى دونالد ترامب الجرأة ليقول إنه طوله 6'3 ووزنه 224 رطل، بينما نعلم كلانا أنه طوله 5'11 ووزنه 300 رطل. لدى دونالد ترامب الجرأة ليقول إن هناك أشخاصًا رائعين جدًا على كلا الجانبين.
لدى دونالد ترامب الجرأة ليقول إنه سيُنهي الحرب في العراق في يوم واحد. لدى دونالد ترامب الجرأة أن يكذب في وجهك ويضربك بالبول ويخبرك أن الأمطار تهطل. هذا ليس أصالةً.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78547" target="_blank">📅 21:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭐️
رويترز:
الإمارات ستفرج عن مليارات الدولارات لإيران.
سيتم إطلاق ما لا يقل عن 10 مليارات دولار أمريكي، مع تسليم أول 3 مليارات دولار أمريكي بالفعل، وقد يصل المجموع إلى 20 مليار دولار أمريكي مقابل وقف الهجمات وتجديد التعاون الاقتصادي والاستخباراتي.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78546" target="_blank">📅 21:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09/08-06-2026
تجمّعات آليات وجنود جيش العدو الإسرائيلي في بلدات البيّاضة، رشاف، وفي محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78545" target="_blank">📅 21:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭐️
مصدر إيراني مطلع:
وزير الخارجية الباكستاني سيتوجه إلى جنيف.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78544" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78543">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الإيرانية:
ليس من الجديد أن يُقال لنا إننا قريبون جدًا من التوصل إلى تفاهم.
المشكلة التي واجهناها خلال هذه الفترة هي التصريحات المتناقضة من الطرف الآخر.
بخصوص نص التفاهم، نحن بصدد وضع الصيغة النهائية له داخلياً.
يُعقد حالياً اجتماع للمؤسسات المعنية.
لا أستطيع تأكيد أيٍّ من التكهنات حول نص التفاهمات.
إن عدم قدرتنا على الحديث عن تفاصيل العملية الدبلوماسية لا يعني أن الناس ليسوا محل ثقة.
نأخذ تجاربنا السابقة مع الولايات المتحدة بعين الاعتبار دوما.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78543" target="_blank">📅 20:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بناء على مناشدة عبر نايا
استجابة الحاج حسين قانونية للمناشدة وصرف راتب عدد من الاخوة  بالحشد الشعبي الذين لم يستلموا منذ اشهر بسبب تبديل البطاقات الائتمانية
#شكرا_قانونية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78542" target="_blank">📅 20:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي يزعم: واشنطن ستحصل على مواد مخصبة بموجب الاتفاق مع إيران.  مسودة الاتفاق ترفع الحصار الأمريكي وتؤدي إلى تفكيك البرنامج النووي الإيراني.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78541" target="_blank">📅 20:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي يزعم: واشنطن ستحصل على مواد مخصبة بموجب الاتفاق مع إيران.  مسودة الاتفاق ترفع الحصار الأمريكي وتؤدي إلى تفكيك البرنامج النووي الإيراني.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/78540" target="_blank">📅 20:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭐️
‏أكسيوس: ترامب أبلغ نتنياهو أن الوقت حان لإنهاء الحرب مع إيران.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78539" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
ترامب: ما زلت أعتقد أن الاتفاق قد يوقع خلال نهاية الأسبوع أو يوم الاثنين.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78538" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78537">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95d839e0a.mp4?token=eptM_qD0wjYCLvrRWac_5gb04I_UUXmA6F60TdcBAaPwSJPwLrc9_sVNE7Q8wCi8M804Bqjwh2IK0zigc813c7Gj08pTXEMRI60Bsx1DmmIav3zmyduSdVyrb9Fl8aQiLyEMqEvvr_SqfR0zMKylOX7ugJ05_May75N4PsgzwXNXOZNu1X3vsask5e20YBqKF5A7iu62E5VE0Qjr5A9BSrmR7eA8cLXdAc-pWyd2ghMTWIZsXvAm4bKAJ3_g5vU3OFWaLgHLiFOlZqsshX4uGeXQl790r_sfTEIyrbYjbznHt3PEXmBy7H5-wwLNVRVrLrh9MKq6nVBnhbhPZ1Dq3pzji17wRE7AuGfi6ZDdFwaAa0KwKI6Fi4xXwizaXDUkUfjXHeykmYl8QBzECa-5eRyOh68GbkDQDYDPQPg87-whH3qhHKl65z-mfwwC3jPTFAOcUkZUF8iD8VUfH_1xAvmxkrl_H3UoVODaUcwDpalals5yvaibnGc_r6GwjrWi1oIlyVxjElEAAqT3qzO-0wIu25HTfd40dfTEuAOk8uq1T4MEnqYSF5VkAF2DnK23IQE__V_404IJ_-J9h5X7jyS94iBWu7yrQ-xCljJFwdBDps7pf4sbilUSGaN8aDD2FYIJ2B5HoYTuCl96AfCdLqc7rUNTRA4dgVl8JNJo2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95d839e0a.mp4?token=eptM_qD0wjYCLvrRWac_5gb04I_UUXmA6F60TdcBAaPwSJPwLrc9_sVNE7Q8wCi8M804Bqjwh2IK0zigc813c7Gj08pTXEMRI60Bsx1DmmIav3zmyduSdVyrb9Fl8aQiLyEMqEvvr_SqfR0zMKylOX7ugJ05_May75N4PsgzwXNXOZNu1X3vsask5e20YBqKF5A7iu62E5VE0Qjr5A9BSrmR7eA8cLXdAc-pWyd2ghMTWIZsXvAm4bKAJ3_g5vU3OFWaLgHLiFOlZqsshX4uGeXQl790r_sfTEIyrbYjbznHt3PEXmBy7H5-wwLNVRVrLrh9MKq6nVBnhbhPZ1Dq3pzji17wRE7AuGfi6ZDdFwaAa0KwKI6Fi4xXwizaXDUkUfjXHeykmYl8QBzECa-5eRyOh68GbkDQDYDPQPg87-whH3qhHKl65z-mfwwC3jPTFAOcUkZUF8iD8VUfH_1xAvmxkrl_H3UoVODaUcwDpalals5yvaibnGc_r6GwjrWi1oIlyVxjElEAAqT3qzO-0wIu25HTfd40dfTEuAOk8uq1T4MEnqYSF5VkAF2DnK23IQE__V_404IJ_-J9h5X7jyS94iBWu7yrQ-xCljJFwdBDps7pf4sbilUSGaN8aDD2FYIJ2B5HoYTuCl96AfCdLqc7rUNTRA4dgVl8JNJo2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 07-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78537" target="_blank">📅 20:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
ترامب: اعتبرت منشور وزير الخارجية الإيراني عراقجي بشأن الاتفاق إيجابيا جدا.  إيران اعتذرت سرا عن تقديم معلومات كاذبة بشأن الاتفاق.  طالبت بتوضيح علني بشأن تقارير إعلامية رسمية إيرانية عن تلقي طهران مليارات من الأصول المجمدة فور توقيع الاتفاق.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78536" target="_blank">📅 20:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌟
رئيس وزراء باكستان:  وسط جهود الوساطة المكثفة المستمرة من جانب باكستان، نحن على دراية تامة بحملة التضليل المستمرة التي يشنها أولئك الذين يرغبون في تخريب اتفاق السلام.  بغض النظر عن الضجة، يمكننا أن نؤكد أنه تم التوصل إلى نص نهائي متفق عليه لاتفاق السلام،…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78535" target="_blank">📅 20:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🐦
سي إن إن:
كادت الولايات المتحدة أن تفكر في عملية برية كبيرة لاستيلاء على اليورانيوم عالي التخصيب في إيران، حيث قام رئيس هيئة الأركان المشتركة دان كين بزيارة سرية عاجلة إلى مقر القيادة المركزية للقوات الأمريكية في فلوريدا في شهر مايو لمراجعة الخطط قبل إطلاع الرئيس ترامب عليها.
تم تعليق العملية في نهاية الأمر بسبب مخاوف من أنها قد تؤدي إلى رد فعل إيراني شديد، وإطالة أمد الحرب، وإلحاق أضرار بالاقتصاد العالمي، وتؤدي إلى خسائر كبيرة في الأرواح الأمريكية.
قام المخططون العسكريون بتقييم المهمة على أنها تنطوي على مخاطر "عالية إلى شديدة"، وقد تتطلب إرسال مئات من قوات العمليات الخاصة لدخول المواقع النووية الجوفية المحصنة بشدة.
في حين تعتقد المخابرات الأمريكية أنها تعرف مواقع المواد (فوردو، ونطنز، وأصفهان)، إلا أن خبراء النووي يشككون فيما إذا كان يمكن تحديد موقعها وإزالتها بأمان خلال عملية قتالية.
كما قيّم المسؤولون الأمريكيون أيضًا أن إيران قد ترد بالوسائل الاقتصادية من خلال تشجيع الحوثيين على تعطيل مضيق باب المندب، مما يهدد شحنات النفط والطاقة العالمية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78534" target="_blank">📅 20:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78533">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭐️
المدير العام للوكالة الدولية للطاقة الذرية:
سنجعل التحقق من النطاق الكامل لقدرات إيران النووية أولويتنا القصوى.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78533" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIlq6toG11sVyJj4e2UPTv5Tx1nRdI4Kv7yiQPAjAe_B3hmm2VhJjJazm_fQVUVuKz3L3i4lMcFT-jtVGQ0K-uqweStlECA2iIh4yE9ZPigRue6NBTG4TgMSvz7OukYxLDiz3Hl7QDjDgV0wZDgdBVIPV7mb5Fbw2-JvhgeDCY-sGz1KTgCXWHLNojFMjF9_wIj39Q-sbt-xWelDxY3Ltn8NUlh9lQ3KRbKwOPdFM5yTceb4TCxaaWcV5kFPAFL5bHdsYSv_4fl_hMSokvyst6MBruM64FjwNRUUGpLYVbVA6fu3uUBpsWEyjTmPkRMA-3lxJtr3RMs8OvSHoY1Lng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
رئيس وزراء باكستان:
وسط جهود الوساطة المكثفة المستمرة من جانب باكستان، نحن على دراية تامة بحملة التضليل المستمرة التي يشنها أولئك الذين يرغبون في تخريب اتفاق السلام.
بغض النظر عن الضجة، يمكننا أن نؤكد أنه تم التوصل إلى نص نهائي متفق عليه لاتفاق السلام، وتعمل باكستان الآن بشكل وثيق مع كلا الجانبين لوضع اللمسات الأخيرة على الخطوات التالية.
لم يكن السلام أبدًا قريبًا كما هو الحال الآن.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/78532" target="_blank">📅 19:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d31c79e4.mp4?token=vWb67YqM1gXK9HCRODQ80jCxcS_13uHLv9vkp3cbARhhXAFdjEe3dJ8h7ouOOv6RKgeEGnaf0n8aAKxorRhpslY0m1j6B_3QOwwwgyBPt08cVGqlMr5xokw293KS5lOvDMTkw28vWguFS9cEiApsfsS9vFjsKmXVsGKaeT7fYieBzAbOevkrzN1wY6b_GV4lpqMEZpE2pDICrJ5qnUPPvp8FmcOnPNDQT2ySXDu6DdqUU9GRpb4wEZAl8vCbwarCLFpoundlIJ-qw4OJQFRWm9xDruAgaRiWpoXrt1pGlXu8DB1OpPv8H707CuUZupyG964W4gDi8oCifChX0HIFkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d31c79e4.mp4?token=vWb67YqM1gXK9HCRODQ80jCxcS_13uHLv9vkp3cbARhhXAFdjEe3dJ8h7ouOOv6RKgeEGnaf0n8aAKxorRhpslY0m1j6B_3QOwwwgyBPt08cVGqlMr5xokw293KS5lOvDMTkw28vWguFS9cEiApsfsS9vFjsKmXVsGKaeT7fYieBzAbOevkrzN1wY6b_GV4lpqMEZpE2pDICrJ5qnUPPvp8FmcOnPNDQT2ySXDu6DdqUU9GRpb4wEZAl8vCbwarCLFpoundlIJ-qw4OJQFRWm9xDruAgaRiWpoXrt1pGlXu8DB1OpPv8H707CuUZupyG964W4gDi8oCifChX0HIFkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
لحظة تنفيذ غارة صهيونية على بلدة تفاحتا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78531" target="_blank">📅 19:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78530" target="_blank">📅 19:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFH2UqV1DWIYUQWSXjVaz-CwN540Ukip6uceI7sy85eOJ3EY1NwXh5a0VF3b3jyizL5gr-qSBUSTWgch9W9Y3dKOfjSOsOMuoRipKFKMlvidSORC59HbbL8VKv5HHa3Ylk65joz-qy43DcqlXF2RHziyMaN8lODybfdJkOO5nPjlwjXzQEUCNmgbbIdsEmm57sRsu1VJgsv1ZqY5HdKAbjLn_gM8rfQK8Fb7p8qJSXQA2zoGrY9B6MNGWREGAT4Xdfb1G_7S094YizkBBp0R8AbvMFVG6ADYC-8TGOu_wNeYOQ_k5q3yhnYPtjbfnSyibk1bsSooBBD6R-9yBsUzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي: لم تكن مذكرة التفاهم في إسلام آباد أقرب من أي وقت مضى. في انتظار إتمامها، يجب على وسائل الإعلام الامتناع عن التكهن بمحتواها. تماشياً مع نهجنا المسؤول والشفاف، سيتم مشاركة جميع التفاصيل مع الجمهور في الوقت المناسب</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/78529" target="_blank">📅 19:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQb2w_gYu836TwwZEMcFMKZglZv0zBy2ZENNwmJfv5n07Fg0kMXWDhqiqdt-tsx-Uuyu200ssABFhQycxP--0sJsDjKrVeCllGOT6Yf49b1l8GMbEzeH04FXLs7t5vnXoWEY2GxvlteT_MMAENFLPZ31WtvsSGM__z7K7KPJI6WA5ydzYuPwtZNsFoDM9nK4H8sgvGLAGpug_9wY11HeWSzltR-_ZHmkj01gH_q9SJmJ8C3FE2SurTEaG_KBnxymzNzkOomvoKYHIyapD56znItOYDgCR1WtK42Uz5ABL2IVpeAK48hfnpyAmhsIKMJxWAy5c-mMGL90ouwaKcDjnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
نائب الرئيس الأمريكي "جي دي فانس":
أولاً، لا يحصل الإيرانيون على أي أموال نقدية، ولا يتم إطلاق أي أموال مقابل مجرد توقيع اتفاق أو حضور اجتماع.
الاتفاق مُصمم لضمان إعطاء الأولوية لمخاوف الولايات المتحدة وحلفائها، وإذا امتثلت جمهورية إيران الإسلامية لالتزاماتها، فستتدفق المنافع الاقتصادية عليها وعلى المنطقة بأكملها. هذا الاتفاق لديه القدرة على إعادة صياغة المنطقة وإدخال سلام دائم.
لقد لاحظت بضعة أشياء غريبة في التقارير خلال الساعات الأخيرة. أولاً، الأشخاص الذين (بشكل صحيح) قالوا إن دونالد ترامب كان رئيسًا تاريخيًا قبل شهر، يقومون الآن بانتقاد اتفاق بناءً على تقارير إعلامية غير مؤكدة. ثانياً، الأشخاص الذين يقولون إنه لا يمكنك الوثوق بأي كلمة يقولها الحرس الثوري الإيراني والذين يبدو أنهم يؤمنون بمشاركات وسائل التواصل الاجتماعي من مصادر مجهولة.
الرئيس سيحصل لنا على نتيجة جيدة، بطريقة أو بأخرى.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78528" target="_blank">📅 18:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
وزير الطاقة الأمريكي:
يمكن أن يكون هناك رفع جزئي للعقوبات عن إيران ضمن التنازلات التي نقدمها.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78527" target="_blank">📅 18:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KD9USmkf5rMRow_HiktOotBC9cVUSlk8Trhwaw7HQW8MSWLkQgqI4ivmppsJK1JVpu1mnxewE41zSl7XMbGvsrhoY7OhyyDJSSzWN7QGGYlfw_TTtOeHjKs8icMHDF2kpGBA3NEn5xq9Sn9H0G7a4-QeovJAf6NCrAlMi03USDPzmz4eekKfi33Lyt4ekAHpwQQ1HWHCl6KaMLO-Bt1fvwvF8B4dFY8aySPvdJrrxMGlF31qlDy7AudA7tZzdSFbc5Ou0mz4nb46bcSnUO-QnmCUqcFANO2tYi_gUKvj2E79Q8npaYLRvhi-JBqSqFd7xEwGnN8E2v8DgFlIRTfhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
لم تكن مذكرة التفاهم في إسلام آباد أقرب من أي وقت مضى. في انتظار إتمامها، يجب على وسائل الإعلام الامتناع عن التكهن بمحتواها. تماشياً مع نهجنا المسؤول والشفاف، سيتم مشاركة جميع التفاصيل مع الجمهور في الوقت المناسب</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78526" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
