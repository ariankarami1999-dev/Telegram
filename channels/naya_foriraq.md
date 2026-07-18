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
<img src="https://cdn4.telesco.pe/file/QxZbwXXNeCBFvbuyWenAKyN9JyRxVk26L8PFhBRc-8LpVMUA57E9mORtsWLNoEvF9MRMVKH827V63AGFDexNKslURKAKGvLJoWYErF1NOIiq7-dKzPR6nwFbwzIVJMe1otcqwDPQr7gbUpml3R-g6wi2n4hkjvY1cO6lmdexow2hCeZI_de641Fq-hGck-5wByAA_MHenfzi_XqVyOHHIPTuMOxFZELLAIYu5Fn4kdus7MQ5xLKDWsmkfJFcVd3eEiuuvFi4HX8K0uSJVSuY1Us3NDqfjciUUpzsyG3b6KXIWN4yOu7Lley3PW_M2vPuxAujPIk2kANE53N-Jv_Q_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 08:10:41</div>
<hr>

<div class="tg-post" id="msg-83856">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الحرس الثوري الإيراني: في الموجة الأولى من عملية "نصر 2"، برمز مبارك "يا أبا الفضل العباس عليه السلام"، استهدفنا موقع تمركز وتجمع القوات المتجاوزة في مركز دعم القوات البرية التابع لهم في عريفجان، مما أدى إلى هلاك عدد منهم، وفي الوقت نفسه، قامت بإطلاق هجوم بطائرة مسيرة على رادار قاعدة علي السالم الأمريكية في الكويت، مما أدى إلى تدميره.</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/naya_foriraq/83856" target="_blank">📅 07:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83855">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/83855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/naya_foriraq/83855" target="_blank">📅 07:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83854">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات تهز مدينة خرج السعودية</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/naya_foriraq/83854" target="_blank">📅 07:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83853">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d059d386b.mp4?token=IUeNOv0YIwN120zJVtH5Yap6nUIZ0mTvxiaZF3xzLAqrYpm7wFNuXjC2pXVeFGirEzINC4vRwajxz-7X44TNiVbCumht5F77QVctjoMdkqirlv-gJNZAvrz-iGFCqCnYIY3NclEHaXjsyPW3XMZZjvR-y-M2T212VgGTaN1EakYbemKlWPrWis-7ND-5V1o0NXGBoQMhbvC9Ds6wjv0PgbKEfnAcNhiQXoDInU2w3MF29OWGhA3AvEVMTd8TSUCHmDsS5GmWbUbNoxe8ApJtJFXbvbNdfI6Xs3PCBa6j-fLRit99dQ_M7ivSglpA49_VGnR43SlcuvFkkuA5ceECOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d059d386b.mp4?token=IUeNOv0YIwN120zJVtH5Yap6nUIZ0mTvxiaZF3xzLAqrYpm7wFNuXjC2pXVeFGirEzINC4vRwajxz-7X44TNiVbCumht5F77QVctjoMdkqirlv-gJNZAvrz-iGFCqCnYIY3NclEHaXjsyPW3XMZZjvR-y-M2T212VgGTaN1EakYbemKlWPrWis-7ND-5V1o0NXGBoQMhbvC9Ds6wjv0PgbKEfnAcNhiQXoDInU2w3MF29OWGhA3AvEVMTd8TSUCHmDsS5GmWbUbNoxe8ApJtJFXbvbNdfI6Xs3PCBa6j-fLRit99dQ_M7ivSglpA49_VGnR43SlcuvFkkuA5ceECOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفارات الإنذار تدوي باستمرار اثر الهجوم الجوي على الكويت</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/naya_foriraq/83853" target="_blank">📅 07:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83852">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/naya_foriraq/83852" target="_blank">📅 07:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83851">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/naya_foriraq/83851" target="_blank">📅 07:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83850">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صفارات الإنذار تدوي باستمرار اثر الهجوم الجوي على الكويت</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/naya_foriraq/83850" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83849">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/naya_foriraq/83849" target="_blank">📅 07:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83848">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات تهز الأردن من جديد</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/naya_foriraq/83848" target="_blank">📅 07:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83847">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/naya_foriraq/83847" target="_blank">📅 07:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83846">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇹🇷
زلزال بقوة 5 درجات يهز مدينة ملاطية التركية</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/naya_foriraq/83846" target="_blank">📅 07:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83845">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQZHc9R9g3poRW0HNeyWNcE1Uwk-a4y85jzYyPRD38uCsZtc5F115Z7ADBSmuAEV1rhBzkfZgU6yAzzMPt3l47z0k2op26Xjq7ukrYrDbab3EipB79G4VU7v9hwGY0eZEeafu85j-pf8uKI7Oqr__J37r4EkSnT1IvRdf-3X3rZCDbIMOCvfmGQSko2MCdOlXyJsnrqrcsAz8dYolHHSnnSdTQsHsv_oX0b9dfa5-PK6KWCFWyz66A87_LMvYFV3rcN_I6yPRFa-iflsk8e8koxS5tLGe8rth_bgCHnC9VwGXBQql26G7Mu-CWpgHJQuuddy3Y5kG_MTCchEVMdCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
طائرة الإنذار المبكر أمريكية تعود إلى قاعدة الأمير سلطان الجوية قبل قليل بعد مشاركتها في العدوان على إيران منذ 28 فبراير.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/83845" target="_blank">📅 07:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83844">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هجوم صاروخي للمرة الرابعة منذ دقائق يستهدف البحرين</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/naya_foriraq/83844" target="_blank">📅 07:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83843">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/naya_foriraq/83843" target="_blank">📅 07:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83842">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات تهز البحرين من جديد</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/naya_foriraq/83842" target="_blank">📅 07:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83841">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/naya_foriraq/83841" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83840">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/naya_foriraq/83840" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83839">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
هزة أرضية بقوة 3.5 درجة على مقياس ريختر تضرب مدينة بندر خمیر في محافظة هرمزگان.</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/naya_foriraq/83839" target="_blank">📅 07:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83838">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9s_W1TxxiFI9N7uDsVb_mz-fNUH6jQtR40qE3c-WfBIcym33JJK-tPUI9OpHHknsBSIk-MZ7uSbCM_Zkb7P52necGJ5LkdmfzTnzMYVc28oBcMLc5NtGJ-H1NonmjuzLzGXzeMaATYta4revdjdo2jk1uXNEcMYPzSoktP-cpSC2ebsT43jXzvPyOVhM2RtlTPZqKl-px-Kg43TfLe5fA2PCWXMzg1MWMPiLLohzLwlWJqwgRwbtvsxOVIk3YpT-ukS4NX_HRF-2SOtkVIFkfy-RGdV2A_YmIjeaWdhNKGMt1d9mXOXKc_SmWiFtYJsNTcapAJ_BzggZK_RSXEKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار تصاعد أعمدة الدخان في الكويت جراء الضربات الإيرانية الأخيرة</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/naya_foriraq/83838" target="_blank">📅 07:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83837">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca3d60dc1.mp4?token=smUDdXtFgGHpsAAavqS1V1CpKydEvYDuIP3ch5vN-EsVeS660D0a5BcJa4XHVO1Kp0gigfly3f3-aL-_TBeyNn7CivGVwGl3sUz2x7YQNAEIiEHT9jEpIpgDD46SNWS4277tQzEq7X8QV-hDcDC1hGr1s7XJz0UsuJQ7sqAEwnKWYf4pxumPJPH_JWTLZLb79C5nojBzsRyQ-Ewphm0cycUUu0HOMNdSB7b8RRm1VYKp5nlyC_MrfJ6Xvh5P9ECG_xKR0X6bPpFm6mUDTeffeViWi08wVrDSf8N0aIujGWxc1tv8Xtt1LAFqn9QfarRwPuJWjfJ7Q1TJZWo3n15ZDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca3d60dc1.mp4?token=smUDdXtFgGHpsAAavqS1V1CpKydEvYDuIP3ch5vN-EsVeS660D0a5BcJa4XHVO1Kp0gigfly3f3-aL-_TBeyNn7CivGVwGl3sUz2x7YQNAEIiEHT9jEpIpgDD46SNWS4277tQzEq7X8QV-hDcDC1hGr1s7XJz0UsuJQ7sqAEwnKWYf4pxumPJPH_JWTLZLb79C5nojBzsRyQ-Ewphm0cycUUu0HOMNdSB7b8RRm1VYKp5nlyC_MrfJ6Xvh5P9ECG_xKR0X6bPpFm6mUDTeffeViWi08wVrDSf8N0aIujGWxc1tv8Xtt1LAFqn9QfarRwPuJWjfJ7Q1TJZWo3n15ZDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من دويلة الكويت المطبعة باتجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/naya_foriraq/83837" target="_blank">📅 07:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83836">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">إطلاق صواريخ من دويلة الكويت المطبعة باتجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/naya_foriraq/83836" target="_blank">📅 06:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83835">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سقوط مباشر للصواريخ الإيرانية داخل المصالح الأمريكية وانفجارات مستمرة فيها</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/naya_foriraq/83835" target="_blank">📅 06:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83834">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات مستمرة في سماء البحرين</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/naya_foriraq/83834" target="_blank">📅 06:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83833">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/072ab78971.mp4?token=cxjp59hzS16G7rrrcVkaC60-EFofvahNszDZ6RVN57PShvq64BMYL9UK6bBmIC6F7gd00OEmoYWxAl4-s8FysNSsb4GHke5xlyJE-py6QMj3NsjLraYzeqc9bS5XOiiQDieuatU5ToEk6NN61T8migAdlntsOfFgb-bxCYUmh0UDiRqXF0kUvAFoUxa_zGb1blNBqjMFVWpMxPPwo780aXYM0xm7m3tiu5f_K0RCyv3rSVFjEm5m3scGDAQwOPs9oZJv4JKY7cx6B0xO4snS3nh0rXyh2ZpLd4fC8ws3UEgmmr4ZMUnKwTunKuHL8hJCnG26D7GIHlaKHSDms1q7Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/072ab78971.mp4?token=cxjp59hzS16G7rrrcVkaC60-EFofvahNszDZ6RVN57PShvq64BMYL9UK6bBmIC6F7gd00OEmoYWxAl4-s8FysNSsb4GHke5xlyJE-py6QMj3NsjLraYzeqc9bS5XOiiQDieuatU5ToEk6NN61T8migAdlntsOfFgb-bxCYUmh0UDiRqXF0kUvAFoUxa_zGb1blNBqjMFVWpMxPPwo780aXYM0xm7m3tiu5f_K0RCyv3rSVFjEm5m3scGDAQwOPs9oZJv4JKY7cx6B0xO4snS3nh0rXyh2ZpLd4fC8ws3UEgmmr4ZMUnKwTunKuHL8hJCnG26D7GIHlaKHSDms1q7Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق طائرات مروحية من نوع اباتشي في سماء البحرين</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/naya_foriraq/83833" target="_blank">📅 06:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83832">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات عنيفة جدا في سماء البحرين</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/naya_foriraq/83832" target="_blank">📅 06:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83831">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات عنيفة جدا في سماء البحرين</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/83831" target="_blank">📅 06:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83830">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cca7edcf2.mp4?token=BxQifaZ-rkNfy-qOuR-FP1aeN9Ryhd14WtxHwEXsDbucdXLLaPpA4-dd2TzIjsC-i3uq340RlN9fouYXyOkGw-MkrLMMoRhqBjCPCpMLeAcnJzOUXIMMGchB-MPtsaq-5CStBWqxgJ7Bfy5CXZ3KUreXwklmc_MvtIBYKhweMZ0PQGZERxeanOWiK0hr9-f8ARif4brSF8sepSKfgJ-uPk73PlILISPqkPGIvJ1kNbXOTR-t9ieIT-Gl5ZIUHzORmhD58Mi60Cy0VH4qAEw2elON3BmPFqqxcOQe7wktWv_zp-TUF-RbSwXQljjtkmI2bmrfAQjl6GYLCvpNk6mdhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cca7edcf2.mp4?token=BxQifaZ-rkNfy-qOuR-FP1aeN9Ryhd14WtxHwEXsDbucdXLLaPpA4-dd2TzIjsC-i3uq340RlN9fouYXyOkGw-MkrLMMoRhqBjCPCpMLeAcnJzOUXIMMGchB-MPtsaq-5CStBWqxgJ7Bfy5CXZ3KUreXwklmc_MvtIBYKhweMZ0PQGZERxeanOWiK0hr9-f8ARif4brSF8sepSKfgJ-uPk73PlILISPqkPGIvJ1kNbXOTR-t9ieIT-Gl5ZIUHzORmhD58Mi60Cy0VH4qAEw2elON3BmPFqqxcOQe7wktWv_zp-TUF-RbSwXQljjtkmI2bmrfAQjl6GYLCvpNk6mdhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">6 انفجارات سمعت الان في سماء البحرين</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/naya_foriraq/83830" target="_blank">📅 06:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83829">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">6 انفجارات سمعت الان في سماء البحرين</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/83829" target="_blank">📅 06:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83828">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b76b8e936.mp4?token=YM86a9zSAAq8Zk5ReYiOejKJH5VsYAVxReQZtgaQLWwAFqAjLL1ud_q5vYcK9DvSKMiwfk462HkYGkmRV3XIV50V-UK7iZef0vS3nCmffyDlay1zJoa4CYiOxFLmjFQzcmJVd3bG1wzCFAfMwevd9kDZkkxd2Oj2amxxF5ysbZILSI6gPTbrLwnG4wBrk5nYoX8gOc3Y3pbLyaxWcGww7LGKwWVMA-wBZbbciFErHPpy-qo79kC3xfZWiXTvqdOpiUQyo6e4nMhG4xGSZI2g1aPtflqctapWV25sfkNCB99CHq5VqEB9L2HSUVMUIcoPMagaR4-hd1y1BkCY2TgHqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b76b8e936.mp4?token=YM86a9zSAAq8Zk5ReYiOejKJH5VsYAVxReQZtgaQLWwAFqAjLL1ud_q5vYcK9DvSKMiwfk462HkYGkmRV3XIV50V-UK7iZef0vS3nCmffyDlay1zJoa4CYiOxFLmjFQzcmJVd3bG1wzCFAfMwevd9kDZkkxd2Oj2amxxF5ysbZILSI6gPTbrLwnG4wBrk5nYoX8gOc3Y3pbLyaxWcGww7LGKwWVMA-wBZbbciFErHPpy-qo79kC3xfZWiXTvqdOpiUQyo6e4nMhG4xGSZI2g1aPtflqctapWV25sfkNCB99CHq5VqEB9L2HSUVMUIcoPMagaR4-hd1y1BkCY2TgHqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/naya_foriraq/83828" target="_blank">📅 06:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83827">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/naya_foriraq/83827" target="_blank">📅 06:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83826">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/naya_foriraq/83826" target="_blank">📅 06:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83825">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeXRuMYMP5uywg4Ye43HYtamVtUGZ5SSrqcr-qX8XGvNtjAoya0iodIud4l9VzzpZwE8H8wJEKNa_y2Xyr6nQycp8SOuHCP-skJ-0FgRSZ5CRYY3smRH8DiMjaOTuXdQBiSCoZxNew1WkkSqeDyKjkz2mkoWQ3w-ZTrb6pf8bsQrCETbFTc21TpHMkh6NXAST9DDOMIzjL-DBVTTLSLqRg42eUpwShUMVpo7OlTNA_42KAQxrknrYkN0ZM7r9iq3WWAogpiq96yq19PbAp1y6ficCfJbW1G3UxQ6uFNLeqbkiXC-lTpaImZYcFifcvjMthSbFeqWSIy8l2vu2_nKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجة صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/naya_foriraq/83825" target="_blank">📅 06:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83824">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjKdQZw2_d4fv1QRW_cES1aJjouH6qISHjP7ZQ5vYZn-hBXLrq8uw5udii08iLos1yWM0QEGAl9Drkyx-X3SL50cZ8nIZpvIBLZK8_S6YMeFu8bwY54L5cnMifUm1s2AIBtFVxcRHQpLkqaH2ilPGZ3W-9JYqrY1LI2EyiZpTa-OX7ShkzRa8mRBHgWZj8ENix_QYF4FRq1HuzDvKzMEtOnZMCJrNXO-6ymPnAM66SDyxhayVtXFn4NwkILP7BoNNtVjveJcSroE0_EbSMq9gGxF_rWGpt5PVFFu1dD7UfrCyMyOQNhDM20PYO9AMaPI-6mfd8uLIUX0AJjzPYoA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مصدر أردني لنايا: وقوع عدة إصابات في صفوف القوات الأمريكية نتيجة الهجوم الصاروخي الإيراني الذي طال قاعدة موفق السلطي بالأردن.</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/naya_foriraq/83824" target="_blank">📅 06:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83823">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ecf7cdf9d.mp4?token=bpzTUHErAW2hYldVDKWmb3wXQQTVlT39sg8Biand3CCEvnO79N3fiPR0III8643tafs9iXcYPmr1lYjc2rpkLrzOKRIxDd-281wSo67Z_QmgKZwVyxZthrFqRA-mBPkS1jvEVEynBNF_yKlXPwfkzJrmXVpLyljuzk7Ly7CyY7GxbsrIljl0sUztyWmeZliBMDMPp9lFPEAgRnPI1wGFWskzRkwMt-Ib9yypVvIlGL3hUEs5OhxHX6gfFGBJcvM9pF_SZNwxjsRGnAJrJmxpUk3Jf73kOdFEiEQl0I1avip0WtNs0t-GZOmxwxZwNwmZBIDkVRqytYP9F2eUWbdYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ecf7cdf9d.mp4?token=bpzTUHErAW2hYldVDKWmb3wXQQTVlT39sg8Biand3CCEvnO79N3fiPR0III8643tafs9iXcYPmr1lYjc2rpkLrzOKRIxDd-281wSo67Z_QmgKZwVyxZthrFqRA-mBPkS1jvEVEynBNF_yKlXPwfkzJrmXVpLyljuzk7Ly7CyY7GxbsrIljl0sUztyWmeZliBMDMPp9lFPEAgRnPI1wGFWskzRkwMt-Ib9yypVvIlGL3hUEs5OhxHX6gfFGBJcvM9pF_SZNwxjsRGnAJrJmxpUk3Jf73kOdFEiEQl0I1avip0WtNs0t-GZOmxwxZwNwmZBIDkVRqytYP9F2eUWbdYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/naya_foriraq/83823" target="_blank">📅 06:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83822">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عدوان أمريكي على محيط ميناء جاسك في جنوب إيران.</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/naya_foriraq/83822" target="_blank">📅 06:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83821">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">لحظه اصابت موشک ایرانی به پایگاه آمریکایی موفق السلطی در اردن از زاویه‌ای دیگر.</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/naya_foriraq/83821" target="_blank">📅 06:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83820">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله أكبر
موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/83820" target="_blank">📅 05:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83819">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات في البحرين نتيجة هجوم إيراني بالصواريخ البالستية والطيران المسير الإنتحاري</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/83819" target="_blank">📅 05:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83818">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارات تهز الكويت وصافرات الانذار تدوي مجدداً</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/naya_foriraq/83818" target="_blank">📅 05:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83817">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09fc0cbfc9.mp4?token=Bjipqqbwgjlbmf15r-0ouiony96i23uBnGM1B_GiqYl8IZFuB-sOGjhJqpBMNnVs87P_nZJB6ELlIIKnxcEmEC_WsD3g3lW5-QDEIDB4iSKHCgPM6AyoksZtPMpUwtwL7vqqgaSkrWC73LeklV1AeCyaJbQAHht5IX_1wlGKlnO9j6OHyaf5NgqEQ1I-CqfRbN0jo9oT_xY2B2JwFeRvGRHS8JmwV5oDSOj6oXDhom9bh-XVJhF-ymkN5zMkO7QjhPjyVDRWrKFnRgNXWVpYSFblk0ZBFz2m4-JVo3s2SQ1iLOMENeMc1z0Fw3SIvGSPpRY5NVOB3t0RqsN6Sa50ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09fc0cbfc9.mp4?token=Bjipqqbwgjlbmf15r-0ouiony96i23uBnGM1B_GiqYl8IZFuB-sOGjhJqpBMNnVs87P_nZJB6ELlIIKnxcEmEC_WsD3g3lW5-QDEIDB4iSKHCgPM6AyoksZtPMpUwtwL7vqqgaSkrWC73LeklV1AeCyaJbQAHht5IX_1wlGKlnO9j6OHyaf5NgqEQ1I-CqfRbN0jo9oT_xY2B2JwFeRvGRHS8JmwV5oDSOj6oXDhom9bh-XVJhF-ymkN5zMkO7QjhPjyVDRWrKFnRgNXWVpYSFblk0ZBFz2m4-JVo3s2SQ1iLOMENeMc1z0Fw3SIvGSPpRY5NVOB3t0RqsN6Sa50ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
المسيرات الإنتحارية تشق طريقها نحو القواعد والأهداف الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/83817" target="_blank">📅 05:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83816">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات تهز الكويت وصافرات الانذار تدوي مجدداً</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/83816" target="_blank">📅 05:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83815">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
الأقمار الصناعية تظهر إندلاع حريق كبير في قاعدة موفق السلطي الجوية الأمريكية في الأردن عقب إستهدافها بعدد من الصواريخ الإيرانية. يذكر أن القاعدة تستضيف قوات وطائرات أمريكية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/83815" target="_blank">📅 05:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83814">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ff98f4a6d.mp4?token=n9_WO6qnty7utHnmqC7tALSDtWwNUA9mneHGDdM7qZsFWdPANx6V4OuCXNbq97VX8qwJ02gT91_J3UgJkiazAcNBg98uYpqypSZ-Tvwg2tueIX_XotoZsRbg0KdVhR0kLh6vUUKkS9DsJxGkLS3JD3qRPcGI0-NihR4syZRcw9z6V9oQ6tHwvgCbI7qCaES95ToVWoiq_Ps0eU2QlVFwyMENeo3fY3UW8s--W-bLI-di3oY2kCAjmtpx_pe9UpbyDa9YHh_tDZIIuuIWxDRW-fg6grkDE1_yr35Uy4okDM3Q2zicGB7Usf8rNg594sm6UxuL5RwqbRVcRO2Q_-EkO1ma3JFMQFo23J5K55P2K8Z3C1UXhkjzBn5SwI3-LTroXLRncmjFMnVPjW69FWGiOwYf-pN14S1iJEHXUDU7TLuAOm_pLhNtF4SntSVtcETdWngMWEDtX308a-ffCZzaQQegH-gYbeMLHCwP6A0u6ctn8AuwqvzHsEXG3cvYXxZ3T_uXXFLoAqWK9Hexjaq_PEToa19rf8g41bBo5-BnMZVfmQ2t8ec1G4Qkg2F5XrDBkCWb_7NQbeYrFo29cSIFZzITZY9lPIett1NMSZfP_-Mo-osadiADJOIJt-GcI-N5xhdwOsV9vjuRjmR7aOzX643lEph64oR4UiyoIGxXglg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ff98f4a6d.mp4?token=n9_WO6qnty7utHnmqC7tALSDtWwNUA9mneHGDdM7qZsFWdPANx6V4OuCXNbq97VX8qwJ02gT91_J3UgJkiazAcNBg98uYpqypSZ-Tvwg2tueIX_XotoZsRbg0KdVhR0kLh6vUUKkS9DsJxGkLS3JD3qRPcGI0-NihR4syZRcw9z6V9oQ6tHwvgCbI7qCaES95ToVWoiq_Ps0eU2QlVFwyMENeo3fY3UW8s--W-bLI-di3oY2kCAjmtpx_pe9UpbyDa9YHh_tDZIIuuIWxDRW-fg6grkDE1_yr35Uy4okDM3Q2zicGB7Usf8rNg594sm6UxuL5RwqbRVcRO2Q_-EkO1ma3JFMQFo23J5K55P2K8Z3C1UXhkjzBn5SwI3-LTroXLRncmjFMnVPjW69FWGiOwYf-pN14S1iJEHXUDU7TLuAOm_pLhNtF4SntSVtcETdWngMWEDtX308a-ffCZzaQQegH-gYbeMLHCwP6A0u6ctn8AuwqvzHsEXG3cvYXxZ3T_uXXFLoAqWK9Hexjaq_PEToa19rf8g41bBo5-BnMZVfmQ2t8ec1G4Qkg2F5XrDBkCWb_7NQbeYrFo29cSIFZzITZY9lPIett1NMSZfP_-Mo-osadiADJOIJt-GcI-N5xhdwOsV9vjuRjmR7aOzX643lEph64oR4UiyoIGxXglg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة مستمرة في الكويت</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/83814" target="_blank">📅 05:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83813">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الصواريخ الإيرانية تصل إلى الكويت والانفجارات تهز قاعدة علي السالم الجوية.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/83813" target="_blank">📅 05:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83812">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رشقة صاروخية إيرانية تنطلق نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/83812" target="_blank">📅 05:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83811">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/naya_foriraq/83811" target="_blank">📅 05:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83810">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/83810" target="_blank">📅 05:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83809">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oglB3nzbI0QjErkqDgOfsQ71HUixcKzfDtFbemd7jffXq-p1OMZXlBU4F1O9rMBwS6gYaaZzX5M2tRUH-Oiesuc_hD5cXl0VQLzFWxiZgr8Y2SHX03dy2hAsYNpBE3q2XkCpDZ4IwVFA-YalAx-7iLgClWtezw-02gnqtyRRLt10htsQrQvjJDp670Bj1lIq4EuahC57Isn7vNlZgwrVrozY7r8xG9XK1X9cLImrM7KwSEdNUoWzneorsWs-fMK6UEHG8V_9lztCLLOtsuHAa_DFgpoirDNN8WnKLUvL-drO3MpMMvM9VUEpuVg5qEHGgtAlJWIKjQzAvHGKbgkCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه اصابت موشک ایرانی به پایگاه آمریکایی موفق السلطی در اردن از زاویه‌ای دیگر.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/83809" target="_blank">📅 05:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83808">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b56dc8ee8e.mp4?token=fHwZqdt8S3icvRQVWWXhTvLpK4jCp7h6m85WVontGoaGU8cNpMAAwOwwpjYwgxeDat09xEOVSqjyrhtkSmOiFrC4Yby_hYRT8RV3nDoXmWvU4PBBJLsnoCpQG8yjcPsalGCy5nssKwaW3XWERkJ_cObXyIPWNjves6vLWRPy_jZRXEEQOPo3voJTXcFhyb6jtCtFaJZBuo-HUTv-0RbS_sFr8zIoZnMkWPvF3bv2LzNlr3woggOIoCrAMP6IPvcNno33GJt9kihu0q-fNVbNy5gb18LRI3j_4QXVFw7u0kHJRSk3ug3TPsdgDQ2hXO1sKWkV6K0SsM1_CyzIZvSZIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b56dc8ee8e.mp4?token=fHwZqdt8S3icvRQVWWXhTvLpK4jCp7h6m85WVontGoaGU8cNpMAAwOwwpjYwgxeDat09xEOVSqjyrhtkSmOiFrC4Yby_hYRT8RV3nDoXmWvU4PBBJLsnoCpQG8yjcPsalGCy5nssKwaW3XWERkJ_cObXyIPWNjves6vLWRPy_jZRXEEQOPo3voJTXcFhyb6jtCtFaJZBuo-HUTv-0RbS_sFr8zIoZnMkWPvF3bv2LzNlr3woggOIoCrAMP6IPvcNno33GJt9kihu0q-fNVbNy5gb18LRI3j_4QXVFw7u0kHJRSk3ug3TPsdgDQ2hXO1sKWkV6K0SsM1_CyzIZvSZIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجيش الأمريكي:
تامبا، فلوريدا - أنهت القوات الأمريكية الليلة السابعة على التوالي من الغارات الجوية على إيران في 17 يوليو/تموز الساعة 9:30 مساءً بتوقيت شرق الولايات المتحدة.
استهدفت القيادة المركزية الأمريكية (سنتكوم) مواقع مراقبة، وبنية تحتية لوجستية عسكرية، ومخازن أسلحة تحت الأرض، وقدرات بحرية. واستخدمت القوات الأمريكية طائرات مقاتلة، وطائرات مسيرة، وسفن حربية، بالإضافة إلى أصول أخرى.
وتواصل سنتكوم محاسبة إيران بتوجيه من القائد الأعلى للقوات المسلحة، مع فرض حصار بحري كامل على الموانئ الإيرانية.
وينتشر أكثر من 50 ألف جندي أمريكي في جميع أنحاء الشرق الأوسط، وهم على أهبة الاستعداد وجاهزون للقتال.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/83808" target="_blank">📅 05:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83807">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">إطلاق صواريخ من الأراضي الكويتية تجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/83807" target="_blank">📅 05:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83806">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">إنفجارات عنيفة و‏دوي صفارات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/83806" target="_blank">📅 04:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83805">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">إنفجارات عنيفة و‏دوي صفارات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83805" target="_blank">📅 04:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83804">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6d561a6a.mp4?token=RykcnyfxybzqoRRAlESjyi0S3hOA8UVJRlRnHuCvo6yk_S1MnUDypF52HwBVI-PLYTFxWNvzCNHfFUsnDxzm-vUE-I2MtDTWDkW0ABXKX-VUXoPFaYPPcGWBHymbwoXK84ey120EpD_W7xIO9V29iC-Ls8HbafUWMOr4lYTwXGUJR2pFFbT9DhMwJnG4mt4AxlQkzXFcALd4aEhP1XfkS780e2xCU2OZx3DOvqOH1ROgtmO7Pe3isWQzeV3v_x1y1tLvT32WSxtjoTDI3F9byVMizfGtmiZkhk-rkkoANme8f1cZYOyl1gtS_e5CQTMeg35kN1KZTBZvbVM8d45PVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6d561a6a.mp4?token=RykcnyfxybzqoRRAlESjyi0S3hOA8UVJRlRnHuCvo6yk_S1MnUDypF52HwBVI-PLYTFxWNvzCNHfFUsnDxzm-vUE-I2MtDTWDkW0ABXKX-VUXoPFaYPPcGWBHymbwoXK84ey120EpD_W7xIO9V29iC-Ls8HbafUWMOr4lYTwXGUJR2pFFbT9DhMwJnG4mt4AxlQkzXFcALd4aEhP1XfkS780e2xCU2OZx3DOvqOH1ROgtmO7Pe3isWQzeV3v_x1y1tLvT32WSxtjoTDI3F9byVMizfGtmiZkhk-rkkoANme8f1cZYOyl1gtS_e5CQTMeg35kN1KZTBZvbVM8d45PVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من الأراضي الكويتية تجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/83804" target="_blank">📅 04:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83803">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عدوان أمريكي على محيط ميناء جاسك في جنوب إيران.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/83803" target="_blank">📅 04:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83802">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f084436.mp4?token=f6MyuPFqdd_XwpR58YPJYBF9xEcbhcoCuHl7icCGSL1qM2f9wkZbSUJdQ4h9cTw82J4S9mVkVYWbcYghjJM08Z99bCzwtR7iMni92iDU8fByAG0819aKK3Awxf7gMvEhdAIxGZmQNOhzXU_1nG6Y_jAGQnQfyxd2aTn8-QRUSOOd_RVF_kUUiMlm5GywLmnn6bcQNj3Y8t4TMjVFtUzFO1xtCU7VUCg_wDtolp4Qw-dFwJDqc_kxP-0FwgtSmh6_ZHMTiKlnxNnJEGFPdUeyqDCb8du7DcCR8kEV4VNr2lB1DDpobIrwyWDNpaBVIQrWN-pUMiMRXZYHmkP1BBBajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f084436.mp4?token=f6MyuPFqdd_XwpR58YPJYBF9xEcbhcoCuHl7icCGSL1qM2f9wkZbSUJdQ4h9cTw82J4S9mVkVYWbcYghjJM08Z99bCzwtR7iMni92iDU8fByAG0819aKK3Awxf7gMvEhdAIxGZmQNOhzXU_1nG6Y_jAGQnQfyxd2aTn8-QRUSOOd_RVF_kUUiMlm5GywLmnn6bcQNj3Y8t4TMjVFtUzFO1xtCU7VUCg_wDtolp4Qw-dFwJDqc_kxP-0FwgtSmh6_ZHMTiKlnxNnJEGFPdUeyqDCb8du7DcCR8kEV4VNr2lB1DDpobIrwyWDNpaBVIQrWN-pUMiMRXZYHmkP1BBBajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من إيران نحو القواعد والأهداف الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/83802" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83801">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7e23eb44.mp4?token=gJguCDP-Vzn3jhccuEJoob8IA_1YP2XdNYYORMcPw-cFOInUj5yLFcD_REBC8r8GA2S9sXuowjskhZm-NJZ4HCCMdqXc9lRCkPvRgW5FpnWxAjMcI6iZgSCHzob7VrVKy0NcIglJkdtzT9kN6L1U82zXlMPtyumVraRAPiG6GnJBWTAOU4VaUyPYHQ3v5IQK4cWmgXzFCoRjw0qvz3uhJ6GKsGim6M4AgQD5m-LrEdZRSCWi7EWTUMRXD8NvDzkD53h_sSXqCS_sneYOz-CridBo23YbtY1XNIq_DwEdp-vHcpXxcZDQzuy5q14lUi3mdoSpXXsMdmkd6ZtnjufWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7e23eb44.mp4?token=gJguCDP-Vzn3jhccuEJoob8IA_1YP2XdNYYORMcPw-cFOInUj5yLFcD_REBC8r8GA2S9sXuowjskhZm-NJZ4HCCMdqXc9lRCkPvRgW5FpnWxAjMcI6iZgSCHzob7VrVKy0NcIglJkdtzT9kN6L1U82zXlMPtyumVraRAPiG6GnJBWTAOU4VaUyPYHQ3v5IQK4cWmgXzFCoRjw0qvz3uhJ6GKsGim6M4AgQD5m-LrEdZRSCWi7EWTUMRXD8NvDzkD53h_sSXqCS_sneYOz-CridBo23YbtY1XNIq_DwEdp-vHcpXxcZDQzuy5q14lUi3mdoSpXXsMdmkd6ZtnjufWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  من الهجوم الصاروخي العنيف الذي دك القاعدة الأمريكية في الأردن وسط فشل تام لمنظومة الباتريوت.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/83801" target="_blank">📅 04:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83800">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات في بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83800" target="_blank">📅 03:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83799">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxG6J-G0Fvb_JVGHIWfHnyeKsW1CkOO6ZqX8dg6DLWbzSN2_QT49g_zRtoSpR2gLRksU8USsBgJLM4Mr2gnqhEh_SQIIeTUcv0lZiWx3HM_oPkAdIco_vf4S4QWeNnv_oYn2yuVjpYDwwD4V2m6kBC-QLT3MS7JhqEDaR_OVFFQUhASpnq-vWso2ou5mTFH6hB_pnh9ok7gHw2Puj_MmJ1Hy-FMpkvbt8hJ30V0rOrX8TkdCOfNZmYi-DoWb9mmPQYgMJhVf1dizKDmr5WuD8sOQD-HhTjhJl-QICCnbncKsT5uK6-yj7giEfxJjGQcPeCHDN4CxM6xtYErTI_NezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83799" target="_blank">📅 03:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83798">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83798" target="_blank">📅 03:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83797">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/83797" target="_blank">📅 03:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83796">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1009bdb1ce.mp4?token=UCtcxHbiHO9kWdnIais0rU7E021DK7xKMfJu8Vb9VNFKA0A56wgNvpNZfbyLIEq3YwE4M_Lrcst-kHXY7XD881p0bN8kVUD5xnNY6PBAVXKEoyJrnnTcn5yMm5reqZqnMBYtKUO2ZstoUc1m-Qxjf5B5YlKxrauzB88RkMjXQ3kNKBROtfOtWyP_McHXL1YaigotrDndvT2fiwYYzfsKs9BwYxhtjf3YYebvzmalylSGwnMQa7vtKSAo7eb1gMHEcCDJM3HsjxpJyGd4Z1h4UKMK0vU1ZCHy1UVMCG2LDkHHIf1AQ2WWQ_hlu0tHaQuNhwOg0vDGHEDCHHFBTPqjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1009bdb1ce.mp4?token=UCtcxHbiHO9kWdnIais0rU7E021DK7xKMfJu8Vb9VNFKA0A56wgNvpNZfbyLIEq3YwE4M_Lrcst-kHXY7XD881p0bN8kVUD5xnNY6PBAVXKEoyJrnnTcn5yMm5reqZqnMBYtKUO2ZstoUc1m-Qxjf5B5YlKxrauzB88RkMjXQ3kNKBROtfOtWyP_McHXL1YaigotrDndvT2fiwYYzfsKs9BwYxhtjf3YYebvzmalylSGwnMQa7vtKSAo7eb1gMHEcCDJM3HsjxpJyGd4Z1h4UKMK0vU1ZCHy1UVMCG2LDkHHIf1AQ2WWQ_hlu0tHaQuNhwOg0vDGHEDCHHFBTPqjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر أردني لنايا: لم يتم صد أو إعتراض أي صاروخ إيراني خلال الموجة الصاروخية الأخيرة التي أطلقت نحو القواعد الأمريكية وجميعها أصابت الأهداف بشكل مباشر.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83796" target="_blank">📅 03:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83795">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">إستهداف قواعد الأمريكان في الأردن من زاوية أخرى</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83795" target="_blank">📅 03:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83794">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nycoItEXpgrMds4hE9uNvrJDjgVES0vNQCwC1-1FHsTkePsDwaM4-jreFJoOYTT7luvtuNvzjoq45OfxRlbkR8kvIJcHzWszNXoDBM3QMll8DsA_MVjHqQ-5BmrdiiaKX3Sp12xtDE00wtq78wyARl6GgOVrZtNSlz-eYzS6ufPavmnMm1zFLB3nufvk5LfcVbi1LsMHVOK52vQvJJtGs4XiERzWbQfc9HKB9_GgWPOm51WVEOmcXEtsNmpDYkQkKFWFUN0T7kFJkwwUK1zaDqmwyf1rrsqxQZWVjXVnmb5qXp05h6jwXONSe9VjSGfPV_YyQFZMl8isgdfc4e2eDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة تهز البحرين وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/83794" target="_blank">📅 03:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83793">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9785ba849.mp4?token=p3Nv3CESx5EpjglcaujkmIf08YpcVq42Jk4s-XhuKk88ABVPD-1w3KzI7h7aMkmEJRvMg0Mv28gUdhk_qWiK4nWPVct2tSO3-yOYO1h-cfhoZL8Phd3qBTtHPhE9JiPEpiqIio8Qbkth6SL81O1vtw1ma8TgrxmQrUu4equNSXUiSGHBbr9-xwmjLkK7omTd0xSfmhjXuykknonPtMreEYnuBjszJWPIJvBU_5PiKQLrJCYJLcvV7hwgXfEkSqnP8kmEkT7KMZpAPTbxY6rnoosTFNGSIhntSuVCmzkuVSXeLvfmDh9votS6GsG5m_3TTEGh_LRAdVkk9FaMVKIA3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9785ba849.mp4?token=p3Nv3CESx5EpjglcaujkmIf08YpcVq42Jk4s-XhuKk88ABVPD-1w3KzI7h7aMkmEJRvMg0Mv28gUdhk_qWiK4nWPVct2tSO3-yOYO1h-cfhoZL8Phd3qBTtHPhE9JiPEpiqIio8Qbkth6SL81O1vtw1ma8TgrxmQrUu4equNSXUiSGHBbr9-xwmjLkK7omTd0xSfmhjXuykknonPtMreEYnuBjszJWPIJvBU_5PiKQLrJCYJLcvV7hwgXfEkSqnP8kmEkT7KMZpAPTbxY6rnoosTFNGSIhntSuVCmzkuVSXeLvfmDh9votS6GsG5m_3TTEGh_LRAdVkk9FaMVKIA3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تمر بسلام نحو القواعد الأمريكية في الأردن وتصيبها بدقة وبشكل مباشر</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83793" target="_blank">📅 03:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83792">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b58dee1b.mp4?token=SUpqWJ8JgkEs56j-6p9xw4g2GBZ0nU1B8sanHN23BSYtvobSBXNdBBsNcfVLjXYWt28-8IXyUi1nZKAqmFT9QXpGjhAo8m1SProgXsBS7uglhoqpJx0PCF-ZEhp_QWsZBYw_qGqlyFH_-LNChktg0md6UAUIm5PBHD42TQByVdJ1Ejd1gU4rkSB-vkgTajCFnsJlErIwwgioEzEe42crSm_-sLxZxAbyxT0aSCL5KliQcLzVa2btfhRrWLWV9HOw4gUg99fHxQn5rXt3_b9dFxcM5sImPYJca05z89uEO9Bw1IsgkFkqAqjI7vP7XBkWxwhrWQIuloU9sxSv_6dOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b58dee1b.mp4?token=SUpqWJ8JgkEs56j-6p9xw4g2GBZ0nU1B8sanHN23BSYtvobSBXNdBBsNcfVLjXYWt28-8IXyUi1nZKAqmFT9QXpGjhAo8m1SProgXsBS7uglhoqpJx0PCF-ZEhp_QWsZBYw_qGqlyFH_-LNChktg0md6UAUIm5PBHD42TQByVdJ1Ejd1gU4rkSB-vkgTajCFnsJlErIwwgioEzEe42crSm_-sLxZxAbyxT0aSCL5KliQcLzVa2btfhRrWLWV9HOw4gUg99fHxQn5rXt3_b9dFxcM5sImPYJca05z89uEO9Bw1IsgkFkqAqjI7vP7XBkWxwhrWQIuloU9sxSv_6dOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تنقض على قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83792" target="_blank">📅 03:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83791">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a287fd1d97.mp4?token=N8-P-r7PXPqMaqTlmVOG-G4RVqWANNTd1wq0QDiQQpJfcg2hpmcH0l5GyfbuG3W7EC_vWlmms8YAMLge5ZUxtrI9ZSCgj4vMuZv7aUAWH5W0t1X9voORnqhNVUAmwqkKohS7iWthibnm8wsXf23c054QyXaFxy0U2iUvelDWTIaZRFLokTBChYJTa2nI8VjTLclAdZxT8WTkikHZq9WPnKvQIkd2VtkWOaK4cjr9QzE1_P9Ztt25nlBpkH6gfXA8vwxJ2LFKsx2L1Ac0vHKaxsICoAIQpA3Oaj4XPG_DbfFkNBxmMZCigZIZb_bBl5GwiKv9ocNg9DfNEG9sMd8zKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a287fd1d97.mp4?token=N8-P-r7PXPqMaqTlmVOG-G4RVqWANNTd1wq0QDiQQpJfcg2hpmcH0l5GyfbuG3W7EC_vWlmms8YAMLge5ZUxtrI9ZSCgj4vMuZv7aUAWH5W0t1X9voORnqhNVUAmwqkKohS7iWthibnm8wsXf23c054QyXaFxy0U2iUvelDWTIaZRFLokTBChYJTa2nI8VjTLclAdZxT8WTkikHZq9WPnKvQIkd2VtkWOaK4cjr9QzE1_P9Ztt25nlBpkH6gfXA8vwxJ2LFKsx2L1Ac0vHKaxsICoAIQpA3Oaj4XPG_DbfFkNBxmMZCigZIZb_bBl5GwiKv9ocNg9DfNEG9sMd8zKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
قبل ساعات، استهدفت طائرات مسيرة تابعة للجيش، في المرحلة الرابعة عشرة من عملية "صاعقة"، مخزن ذخيرة تابع للجيش الأمريكي المتجاوز في معسكر العدي، والمباني التابعة لقيادة هذا الجيش القاتل، ومخازن الذخيرة في قاعدة علي السالم، وعدد من نقاط الاتصال في الكويت.
🔻
يعتبر معسكر العدي أحد المراكز الهامة لدعم وإعادة تنظيم القوات الأمريكية، كما تعتبر قاعدة علي السالم واحدة من أكبر المراكز لدعم وتنسيق العمليات الجوية الأمريكية في منطقة الخليج العربي.
🔻
وفي إطار هذه الهجمات، استهدفت أيضًا خزانات الوقود التابعة للجيش المتجاوز في قاعدة الأزرق في الأردن بواسطة طائرات مسيرة تابعة للجيش.
🔻
أصبحت قاعدة الأزرق الجوية في الأردن، نظرًا لموقعها وبنيتها التحتية ونشر المعدات العسكرية الحديثة والاستثمارات الضخمة الأمريكية، قاعدة حيوية للولايات المتحدة، تلعب دورًا رئيسيًا في السيطرة على المنطقة والعمليات العسكرية في غرب آسيا.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83791" target="_blank">📅 03:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83790">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات عنيفة تهز البحرين وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83790" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83789">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عدوان أمريكي غاشم على جزيرة لارك جنوبي إيران.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83789" target="_blank">📅 03:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83788">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ace3b7e5.mp4?token=Gy3622LXf2xvCWvVzzkmRSSEhaF1T-p6N7wMm-_QtAUwrltL6f-kKfG_oQwXU-XO4zKwET9LljWU4pmf323Lujd7SUR73yXndctvzut6C3zFqqjogM8-kJHGU2YqkCl64XIup2VlP-C7wFSN6tOTEFrlSUKBKaIDEbAPAvCd-SRgSG-BcKpTWi1_8Pn3ZIsfLTS4H_HfyQLgAvgH1YBqUrYwJU_maBdL14EgYIev7VjC2efiCQC5YPN9Tivob8eOlFqjprxDo4gGl7DI4_UZwvxqEGhq6_NokNH2yBCUXVNJiM0PMHx5_cYXstJChgV-sFxm0s3jar8H3Xt_qvmkWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ace3b7e5.mp4?token=Gy3622LXf2xvCWvVzzkmRSSEhaF1T-p6N7wMm-_QtAUwrltL6f-kKfG_oQwXU-XO4zKwET9LljWU4pmf323Lujd7SUR73yXndctvzut6C3zFqqjogM8-kJHGU2YqkCl64XIup2VlP-C7wFSN6tOTEFrlSUKBKaIDEbAPAvCd-SRgSG-BcKpTWi1_8Pn3ZIsfLTS4H_HfyQLgAvgH1YBqUrYwJU_maBdL14EgYIev7VjC2efiCQC5YPN9Tivob8eOlFqjprxDo4gGl7DI4_UZwvxqEGhq6_NokNH2yBCUXVNJiM0PMHx5_cYXstJChgV-sFxm0s3jar8H3Xt_qvmkWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تستهدف القاعدة الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83788" target="_blank">📅 03:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83787">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d32c27bc.mp4?token=ou9fcjvmgFJ_LSLRY1fTG1O7PUjP2Te9RtUshP0VQ05-FX5uLLgiEQK6o75ImDpQGKBiIjkZtzaJfyTK7GYpQ9oOnmDsaXZO1hJ5ZM3eRBMCvGWUIGxfM58vUxOn9sRVL7JQYv8djEJEaYsm71FweBn2CUZfkG4NLsQueXuEvdQ52MTtp_HP9QTqBgkciKT08KP57nMStifOo0J6abyHn3T7NfVsLx3FBQdIvdXq6PgVR1fzo2_ExeFg8HhE6a_CNlmMa7DKO3zwaBPb59WIBhGvpI_EayjsecZTqQA8cCN2fWQ2prEeEqgSbRvg-7mh5B1kOeAnHehVTPvqUc91RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d32c27bc.mp4?token=ou9fcjvmgFJ_LSLRY1fTG1O7PUjP2Te9RtUshP0VQ05-FX5uLLgiEQK6o75ImDpQGKBiIjkZtzaJfyTK7GYpQ9oOnmDsaXZO1hJ5ZM3eRBMCvGWUIGxfM58vUxOn9sRVL7JQYv8djEJEaYsm71FweBn2CUZfkG4NLsQueXuEvdQ52MTtp_HP9QTqBgkciKT08KP57nMStifOo0J6abyHn3T7NfVsLx3FBQdIvdXq6PgVR1fzo2_ExeFg8HhE6a_CNlmMa7DKO3zwaBPb59WIBhGvpI_EayjsecZTqQA8cCN2fWQ2prEeEqgSbRvg-7mh5B1kOeAnHehVTPvqUc91RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات فاشلة لمنظومة الباتريوت الأمريكية في اعتراض الصواريخ الإيرانية التي تنقض على قاعدة موفق السلطي بالأردن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83787" target="_blank">📅 03:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83786">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454271fe9c.mp4?token=bvQckXNi_qAJLnGNMrgWZAzoASJjFVj-5aOvKaL1NDHGUq2r5OvgIT8p_6aeSlSF5ZRwygS1WkP7LOK8_Iv94oUjzirbeceRsRUw5vOIFiu3V04q_xl9oPLA2jkQehW-mf-5Yf1TwU3Qi4IgFjG2HWJBzbt6eXAUTGjEe9jD_03UZEUeeaPeZj4o8UwIu_XGy_g8bxiLyrL4ir5HIcngTl6CfYNNVe2jSUMIaV9O49ZiWTlYQlWlSSkeMeqZUi_eOcbRCjafy9LQ-ZfXER-wYM5cjMBzAgoq_lx1HeIq1LlH32WW4QGtUT4VWfB4JbmzKQgX31q-aOrmhb6o5ZMSMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454271fe9c.mp4?token=bvQckXNi_qAJLnGNMrgWZAzoASJjFVj-5aOvKaL1NDHGUq2r5OvgIT8p_6aeSlSF5ZRwygS1WkP7LOK8_Iv94oUjzirbeceRsRUw5vOIFiu3V04q_xl9oPLA2jkQehW-mf-5Yf1TwU3Qi4IgFjG2HWJBzbt6eXAUTGjEe9jD_03UZEUeeaPeZj4o8UwIu_XGy_g8bxiLyrL4ir5HIcngTl6CfYNNVe2jSUMIaV9O49ZiWTlYQlWlSSkeMeqZUi_eOcbRCjafy9LQ-ZfXER-wYM5cjMBzAgoq_lx1HeIq1LlH32WW4QGtUT4VWfB4JbmzKQgX31q-aOrmhb6o5ZMSMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عنيف يشعل قاعدة موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/83786" target="_blank">📅 03:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83785">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3b6b0ad7.mp4?token=dTb2dEIn9y3m8TBMDpKjlllVUJrqD4t5ifp_07BteAZ4iU-pctpEUa0LedGqdhVZFhSXl7Ux1y8it8wWY3SBB89IKIs5hOc7ljMliRDyPgxCF0nzy4WGCCk9DymE9A-RiJM362JbbI9Sn6XFWAkyzSdVCt94q-VsLKq7byhxFuGgqYNKNNzmpJ9mLk7xauXaEBdybEs10QS1McCOJl6eoz0R8Zmp23UofqYvgLv4S3m2bQ4eS19zaTloOcW2VB1nYu5u1oIoTV16ehOcZU0YtHoTY-nFjXK9KXVklZW225I_gEbpWhV8azzbKz3S9C_ICYoRLvreT2AfMoX5eVSYZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3b6b0ad7.mp4?token=dTb2dEIn9y3m8TBMDpKjlllVUJrqD4t5ifp_07BteAZ4iU-pctpEUa0LedGqdhVZFhSXl7Ux1y8it8wWY3SBB89IKIs5hOc7ljMliRDyPgxCF0nzy4WGCCk9DymE9A-RiJM362JbbI9Sn6XFWAkyzSdVCt94q-VsLKq7byhxFuGgqYNKNNzmpJ9mLk7xauXaEBdybEs10QS1McCOJl6eoz0R8Zmp23UofqYvgLv4S3m2bQ4eS19zaTloOcW2VB1nYu5u1oIoTV16ehOcZU0YtHoTY-nFjXK9KXVklZW225I_gEbpWhV8azzbKz3S9C_ICYoRLvreT2AfMoX5eVSYZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تتجاوز منظومة الباتريوت وتستهدف قاعدة موفق السلطي في الأردن.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/83785" target="_blank">📅 02:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83784">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3aede10e2.mp4?token=MUbK8Aum05w3GlADZtTBQMDln5Lrrsde5lH5m3uOuiV2pGaJHwx-ojxjlQ2d5gTScWKr-la89__v9tblMJusE8udMmW0HLOWAUav-Qr3hbRr6iN182jb6DYB7qVQnK4bdmGYu_zlEejapXy8Op3FsYysGMBvjiL3l047X9-tjywKoVPSrs2fL3imoR07kfxfLsQmE78ok0tFhydNJzbNlxy-KoBRAPUKAq14LuKSvA0O-CnXmFaGNoPAnUgxdfmWFyvsjC7KpEmyyH--u9Bq-ux-fszWnJeboCN5wlyirJqld7YyIEkIa5Oe4qmYVbJc_XYDanjoN53UfX3dwOX1IIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3aede10e2.mp4?token=MUbK8Aum05w3GlADZtTBQMDln5Lrrsde5lH5m3uOuiV2pGaJHwx-ojxjlQ2d5gTScWKr-la89__v9tblMJusE8udMmW0HLOWAUav-Qr3hbRr6iN182jb6DYB7qVQnK4bdmGYu_zlEejapXy8Op3FsYysGMBvjiL3l047X9-tjywKoVPSrs2fL3imoR07kfxfLsQmE78ok0tFhydNJzbNlxy-KoBRAPUKAq14LuKSvA0O-CnXmFaGNoPAnUgxdfmWFyvsjC7KpEmyyH--u9Bq-ux-fszWnJeboCN5wlyirJqld7YyIEkIa5Oe4qmYVbJc_XYDanjoN53UfX3dwOX1IIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/83784" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83783">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الصواريخ الإيرانية تستهدف قاعدة موفق السلطي الأمريكية في الأردن وسط تفعيل منظومة الباتريوت لإعتراض الهحوم.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/83783" target="_blank">📅 02:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83782">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebaff0c2c.mp4?token=AaPqglCXn4CEmHtVfiw7E5Rzj9uGL2umQLq1f0Qjt8bQjL8tn9snAbilSol1xbO3R5fWOnnwMP8stIsUi5Ya-LGtElCZeENL10wDCA49oQJmFpcMyuabR2c0l5RWbKo1vHuLgB9B572M9siwEvyY3x1uJbIH71noKkf5yWRWEqC0bDHk2ErK_2v3LEWycaBX3tSomUpr85OR_4GLBjHvdJyl-CFgT79Qnz4zJsPfGULrJP52NqhGjn7Spj2abIvfxp2JYST5ayGgZgxdyukZvsMZoAFDb-DcS5mhDSJ76nKXYEQe6neCMDhN2_HrA8mtEAR5PLFxCkTQBJ9JJP70oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebaff0c2c.mp4?token=AaPqglCXn4CEmHtVfiw7E5Rzj9uGL2umQLq1f0Qjt8bQjL8tn9snAbilSol1xbO3R5fWOnnwMP8stIsUi5Ya-LGtElCZeENL10wDCA49oQJmFpcMyuabR2c0l5RWbKo1vHuLgB9B572M9siwEvyY3x1uJbIH71noKkf5yWRWEqC0bDHk2ErK_2v3LEWycaBX3tSomUpr85OR_4GLBjHvdJyl-CFgT79Qnz4zJsPfGULrJP52NqhGjn7Spj2abIvfxp2JYST5ayGgZgxdyukZvsMZoAFDb-DcS5mhDSJ76nKXYEQe6neCMDhN2_HrA8mtEAR5PLFxCkTQBJ9JJP70oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات صاروخية أطلقت من إيران تجاه القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83782" target="_blank">📅 02:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83781">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
🇮🇷
جراء العدوان الأمريكي الغاشم..
إرتقاء 3 شهداء و8 اصابات في محافظة هرمزغان كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/83781" target="_blank">📅 02:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83780">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
🌟
🌟
مسؤول أمريكي: إيران أطلقت صاروخا باليستيا على قاعدة أمريكية في السعودية.  هجوم صاروخي إيراني طال منطقتي الخرج وينبع السعودية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83780" target="_blank">📅 02:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83779">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار في اميدية بمحافظة خوزستان جنوب ايران</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83779" target="_blank">📅 02:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83778">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات تهز السعودية وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83778" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83777">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tnvy9BkhaAD1_UiPeqA5Tt18XtPG6HHezjeatovTrr0y-W5VZXMggTvg0bEk8NmN-QQgOf9Cfj_8AAhNflP5bG9l9xFCv_Y2X_jv-8orGRcY--bgi-E_bKJ1cESY1ZPqp2HEXxn2u5LdUZdM2Dw1GZrZv4n065Z3e60gtsNp6aj5VoyK4kugo3iec9F9aryJKBqatbhAAH1f_myd4OKkKi_HdMTk6juleE5RCs9A4fQCT5XLYT7EBWz60_qYxitShnGZW_r4cccTS2XPQ0wCk-5SylthInsxULSijzXc6uAuyW27ZELZTMBAJ7hwgALhJdAjbBirU1NLvGDj2E-NNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدوان أمريكي غاشم يطال طرق وجسور  بين محافظتي كرمان وهرمزغان جنوبي إيران.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83777" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83776">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f45172ab3b.mp4?token=PZBLQu8WpGnrqg0Axd6N5A92mgZtn-N4cSog8faP_Eu_qpIkD5J_MBmXDx25xyJ2jQz6bOjPVVT_82UblG-6CcU7A7DFy1kAIf_l2rzoRoFl-qtfSDz0LHhWTcIKx1iwWFIhHtS2L0wFmj7t2gZMrlfB5E1ixJal0BIEqQe423tSfHVF8CDjS7OXtmpqBAdaFAncgyczZJGviDgNSeRMP9ACBqpwjMczQ2C6j_RNgdLYCOO6toP2irb7r3EF47tRR8LJjAWil8iBun5PsJ6PP3Ggo_jmy52gCo5ndZKLtd2HI67fV2776QDk73scI1Zrxdl19_1VycFUOLDD8oiEfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f45172ab3b.mp4?token=PZBLQu8WpGnrqg0Axd6N5A92mgZtn-N4cSog8faP_Eu_qpIkD5J_MBmXDx25xyJ2jQz6bOjPVVT_82UblG-6CcU7A7DFy1kAIf_l2rzoRoFl-qtfSDz0LHhWTcIKx1iwWFIhHtS2L0wFmj7t2gZMrlfB5E1ixJal0BIEqQe423tSfHVF8CDjS7OXtmpqBAdaFAncgyczZJGviDgNSeRMP9ACBqpwjMczQ2C6j_RNgdLYCOO6toP2irb7r3EF47tRR8LJjAWil8iBun5PsJ6PP3Ggo_jmy52gCo5ndZKLtd2HI67fV2776QDk73scI1Zrxdl19_1VycFUOLDD8oiEfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات صاروخية واسعة تنطلق من إيران</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/83776" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83775">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f8353d4f.mp4?token=GxaEproDAtPQRPO3atM1MN_WkoK71DwKiVXc5kfPuRonii82asF9vlpEEraGCgh3PNSxS9EqRqBALHH7mnLKmRBQ7lwsC6kTQ5FzjLLgIpLKN-MrtdNeVpScrTnPyYLjPy4ntKRmFGeqNGCT_N2sPRb48lygRiTppiRokdxtvkx7BFObm9eSiNcVeDFe4oLVJPkpCdkb2IcrLuA_tsTGuS6QbMmsb1aredNzwrc3rUJnC13yVEp5brF9kAYFRZb88DuyNWOy3b3xGoerBJ2SGKT0EtbEoE-gMVBY1hwe3unb2B257gyZd4lrpTdfxazddaEDZkSmtYVEsAgSI-xW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f8353d4f.mp4?token=GxaEproDAtPQRPO3atM1MN_WkoK71DwKiVXc5kfPuRonii82asF9vlpEEraGCgh3PNSxS9EqRqBALHH7mnLKmRBQ7lwsC6kTQ5FzjLLgIpLKN-MrtdNeVpScrTnPyYLjPy4ntKRmFGeqNGCT_N2sPRb48lygRiTppiRokdxtvkx7BFObm9eSiNcVeDFe4oLVJPkpCdkb2IcrLuA_tsTGuS6QbMmsb1aredNzwrc3rUJnC13yVEp5brF9kAYFRZb88DuyNWOy3b3xGoerBJ2SGKT0EtbEoE-gMVBY1hwe3unb2B257gyZd4lrpTdfxazddaEDZkSmtYVEsAgSI-xW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة صاروخية اخرى تنطلق</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83775" target="_blank">📅 02:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83774">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae985645c.mp4?token=v8WeiIWtBEYPp2fZ9GWewiVPEZyxWNvqOAEOyiB46ZU-VHeG1TWaiWlgLsXEej25f9wyvoiSdrI5qAkkH3gaBJSswGnOCxuAapObcFvJ5-MP4VGsJwQMQfwbsp6paFwUifT3RYJ78dDvv56V-ysaq8sHxXtNFNMut2a2-9IsYwTYWXO2J8VU1GSSLRDbuel_uEoEKujmo77FQCeHP50AVbxr-xKUprYrxft_gmh-TRVWEl3nmEmVgA2GPYi3Z9DTthGNcxs6mrIvS1kWWV8UFq7qJ2b9_aydNmwCXEyc2gZzY6Uf5WeWOMwawMKeRtKvn38AnwtmRrMnKrPtRN5Zbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae985645c.mp4?token=v8WeiIWtBEYPp2fZ9GWewiVPEZyxWNvqOAEOyiB46ZU-VHeG1TWaiWlgLsXEej25f9wyvoiSdrI5qAkkH3gaBJSswGnOCxuAapObcFvJ5-MP4VGsJwQMQfwbsp6paFwUifT3RYJ78dDvv56V-ysaq8sHxXtNFNMut2a2-9IsYwTYWXO2J8VU1GSSLRDbuel_uEoEKujmo77FQCeHP50AVbxr-xKUprYrxft_gmh-TRVWEl3nmEmVgA2GPYi3Z9DTthGNcxs6mrIvS1kWWV8UFq7qJ2b9_aydNmwCXEyc2gZzY6Uf5WeWOMwawMKeRtKvn38AnwtmRrMnKrPtRN5Zbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر
موجة صاروخية اخرى تنطلق</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83774" target="_blank">📅 02:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83773">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">السعودية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/83773" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83772">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">السعودية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/83772" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83770">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbbb6ed794.mp4?token=tMhGVCZTcy6Os5u-sRbZfL0SHP61jTNpylyQoy1uoRGcCsbt6jPaMVyivs7RcjOMKwsLaRR49stL5DzHjy3B1LNRA0ti6zSpHQQ1erz95xRP5bVm0ggLgK5amLa38sNweHH-MuMtrd4DHrLsepeu2RcAkLmAwscxYoQuopYNysROC8XMCGsezCJTWxy52R4Rt1S4uAoNMuq_-z8sHU-cw5CA4hH0N8QKt9cEfb2p-a24MmnLtX0Ckh_5UUA3UQqYSpE_2-XlxLkoDmjZcVUnJtciaABDaC8t4GC8-c5mv2xROvmR8jt_izlvRPfQr2fXbAhEJKsMAH73H-xMDjKrLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbbb6ed794.mp4?token=tMhGVCZTcy6Os5u-sRbZfL0SHP61jTNpylyQoy1uoRGcCsbt6jPaMVyivs7RcjOMKwsLaRR49stL5DzHjy3B1LNRA0ti6zSpHQQ1erz95xRP5bVm0ggLgK5amLa38sNweHH-MuMtrd4DHrLsepeu2RcAkLmAwscxYoQuopYNysROC8XMCGsezCJTWxy52R4Rt1S4uAoNMuq_-z8sHU-cw5CA4hH0N8QKt9cEfb2p-a24MmnLtX0Ckh_5UUA3UQqYSpE_2-XlxLkoDmjZcVUnJtciaABDaC8t4GC8-c5mv2xROvmR8jt_izlvRPfQr2fXbAhEJKsMAH73H-xMDjKrLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لازالت المسيرات الإنتحارية تحلق في سماء محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83770" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83769">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f0a10461.mp4?token=SD4HNLgQnA0-UKLx5ggaGmLo9ScaClQRLOmBSZH2iu6INxvyhGwhJfyq5yTBk0m0Xte-k6VfcTjEGeenKaP-m8-OT7hZmYzBSwH_Oro-6uUB4AkxEUvMMUG7ZPP4N5pI0nQnOTkX7SNrwhCaOmvsq8FB0eUu6k1szW3FbDXAZyorurqZrw1IOtF0dktmAw2QJFBAG9bJ_U9YEKUYeIbREaMNRT6pZVadJDXURmzLFFMbdiXXM2utB9yi1urcdR9dUaXidmKp3hWiJbLplhqaLxAuEDgIeTw3q-V1RXRaq_LbEDIcBPSMdK7PYiMVtXbm6_Qzagq-wpRwbanZ03khYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f0a10461.mp4?token=SD4HNLgQnA0-UKLx5ggaGmLo9ScaClQRLOmBSZH2iu6INxvyhGwhJfyq5yTBk0m0Xte-k6VfcTjEGeenKaP-m8-OT7hZmYzBSwH_Oro-6uUB4AkxEUvMMUG7ZPP4N5pI0nQnOTkX7SNrwhCaOmvsq8FB0eUu6k1szW3FbDXAZyorurqZrw1IOtF0dktmAw2QJFBAG9bJ_U9YEKUYeIbREaMNRT6pZVadJDXURmzLFFMbdiXXM2utB9yi1urcdR9dUaXidmKp3hWiJbLplhqaLxAuEDgIeTw3q-V1RXRaq_LbEDIcBPSMdK7PYiMVtXbm6_Qzagq-wpRwbanZ03khYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات صاروخية تنطلق من إيران صوب القواعد المعادية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/83769" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83768">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8018ed7cf3.mp4?token=vamDRa9j0nQzNjb8Nkduqa4PYz9DO59_HN6D8kxJ6Eszmeuxrr45zKeI6OiiS8Rrh1vnVPRnVIScqzDgrtMuZAuRqG_CqHoJYLcQqIvvm1mhtkowMywDMoDKEQnIZ9cxsZqE5Md84pyZR8z3hKtIeyHkdn53Wp2xVM2I666MOLXEm-m6XlohFqSY9tQD98nYEwkH3_Bjw7DYZWIvWxVqMWLwm7hrhjAGXFWi1Yz1hFWQfLPpoP8kjNpuJrl1shUOKsvfXVLLNJWmO7eeZM3404tv1O2kSOGemaN34PkdAYUh7WpgJDWz2R6KaFS4VWfZ8d8Ka1N97-OiH80ijThE7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8018ed7cf3.mp4?token=vamDRa9j0nQzNjb8Nkduqa4PYz9DO59_HN6D8kxJ6Eszmeuxrr45zKeI6OiiS8Rrh1vnVPRnVIScqzDgrtMuZAuRqG_CqHoJYLcQqIvvm1mhtkowMywDMoDKEQnIZ9cxsZqE5Md84pyZR8z3hKtIeyHkdn53Wp2xVM2I666MOLXEm-m6XlohFqSY9tQD98nYEwkH3_Bjw7DYZWIvWxVqMWLwm7hrhjAGXFWi1Yz1hFWQfLPpoP8kjNpuJrl1shUOKsvfXVLLNJWmO7eeZM3404tv1O2kSOGemaN34PkdAYUh7WpgJDWz2R6KaFS4VWfZ8d8Ka1N97-OiH80ijThE7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية تنطلق من إيران نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/83768" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83767">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3210d2d30.mp4?token=Nn-NYQJj3l8ga6NxRyUupvtF-KNy4UR3QFxvukwSv9lqLqiLj9L9uiatnVmhqd23X02n6Tgy0pz_br8wgiBmhEZ1K8j8ovzDvBbk8Asqhith_rK9QX7abW__StMoh_5QBT0pdR7EA-iA_PzeaPYPssXyTCVDUYFNqqGZekjjjAlqoWlhJxZNqCc6ZpuIEfUzDDi8OHCYaz_9r1ha4BD2mlSQRH4_DyGUqfiFe8CtDuvXlFMjoPC7ZqDU0MidRc3i0kIUNDDXKUKN1H23po1u2qx4PpEGAFx8YFVWLGjt8ka5N5IwxHUKEqA8AV1kjVh0-mGEbuQmkPE-CA080F4KXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3210d2d30.mp4?token=Nn-NYQJj3l8ga6NxRyUupvtF-KNy4UR3QFxvukwSv9lqLqiLj9L9uiatnVmhqd23X02n6Tgy0pz_br8wgiBmhEZ1K8j8ovzDvBbk8Asqhith_rK9QX7abW__StMoh_5QBT0pdR7EA-iA_PzeaPYPssXyTCVDUYFNqqGZekjjjAlqoWlhJxZNqCc6ZpuIEfUzDDi8OHCYaz_9r1ha4BD2mlSQRH4_DyGUqfiFe8CtDuvXlFMjoPC7ZqDU0MidRc3i0kIUNDDXKUKN1H23po1u2qx4PpEGAFx8YFVWLGjt8ka5N5IwxHUKEqA8AV1kjVh0-mGEbuQmkPE-CA080F4KXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات صاروخية تنطلق من إيران صوب القواعد المعادية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/83767" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83766">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ce5db5c99.mp4?token=YQt8cFvQxXWEItwBXm220d4JpgtUfq__7xqR8DJ0UR0psuuJ57_VDBQYRuUngOtpveeJVFZxMFa_FyJBm3SQvjkaKvSqZDGxWZ6wLRsAiRUW4u1Zeav_k6A59Bd91SxdGq5cZle09l2W-oWI8pHIK5CVGADspmssWgI3t6DSdT5XYngARgpOxYJbPyJ7kK9mqCd8_u42qhBQgXb1Z0CcBKhNUiGKNML1jO3k4VOIFZotZ9LJV3kZmg6Sn_TxiM_liwTAcT3MEm5nFWy93rmEnjGcGsqrlIgEMFHfWHVqo0BwIxSoxH0HXuyqnYRePwwT5i0GlSGvhlIptleaB_X_kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ce5db5c99.mp4?token=YQt8cFvQxXWEItwBXm220d4JpgtUfq__7xqR8DJ0UR0psuuJ57_VDBQYRuUngOtpveeJVFZxMFa_FyJBm3SQvjkaKvSqZDGxWZ6wLRsAiRUW4u1Zeav_k6A59Bd91SxdGq5cZle09l2W-oWI8pHIK5CVGADspmssWgI3t6DSdT5XYngARgpOxYJbPyJ7kK9mqCd8_u42qhBQgXb1Z0CcBKhNUiGKNML1jO3k4VOIFZotZ9LJV3kZmg6Sn_TxiM_liwTAcT3MEm5nFWy93rmEnjGcGsqrlIgEMFHfWHVqo0BwIxSoxH0HXuyqnYRePwwT5i0GlSGvhlIptleaB_X_kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية تنطلق من إيران نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/83766" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83765">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/83765" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83764">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/83764" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83763">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c455d6a4.mp4?token=kdA3ENjTWhF9hwXk7Pe-eLdMAiRy7qjjZLZR03hiDP-wKN0UFT2_jn_8a6Twhcx2MyFZ-H6wI1pikZoZWBsqHEwpmVLcW8afxO2LgeFIFabxv8cIfJPRFvwUHIF58pR3C39EinG_Vbi7LoEbcZ1cqFeu6TnWcZIQWa7G3kDCvZcHgx61uCZa0OVUuLYpL1g9ZrLRhTvyb82neE4E-bwrh8vgoCn-BMTawZ0Vg7K7gKcsEv9-FhU75oviWEycuUlEmqIJQ0eCeVVG9j0NeysbDagxUqZCjw4iqoyQKOrizGGxTN7e5wXCUqfDjUYPHuZ5QA9639NT37FRyhUvbki4Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c455d6a4.mp4?token=kdA3ENjTWhF9hwXk7Pe-eLdMAiRy7qjjZLZR03hiDP-wKN0UFT2_jn_8a6Twhcx2MyFZ-H6wI1pikZoZWBsqHEwpmVLcW8afxO2LgeFIFabxv8cIfJPRFvwUHIF58pR3C39EinG_Vbi7LoEbcZ1cqFeu6TnWcZIQWa7G3kDCvZcHgx61uCZa0OVUuLYpL1g9ZrLRhTvyb82neE4E-bwrh8vgoCn-BMTawZ0Vg7K7gKcsEv9-FhU75oviWEycuUlEmqIJQ0eCeVVG9j0NeysbDagxUqZCjw4iqoyQKOrizGGxTN7e5wXCUqfDjUYPHuZ5QA9639NT37FRyhUvbki4Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي غاشم يطال طرق وجسور  بين محافظتي كرمان وهرمزغان جنوبي إيران.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83763" target="_blank">📅 02:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83762">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇱
إعلام العدو:
حدث أمني في جنوب لبنان ومروحيات الجيش الإسرائيلي تنقل عدد من الجنوب إلى مستشفى رمبام.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/83762" target="_blank">📅 02:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83761">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات في مدينة جغادك جنوبي إيران.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/83761" target="_blank">📅 02:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83760">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ensxm-Mkl0mzuYWILjs19dW8Xwh-gjpjOOUREk9a_s1adHoorDSTiGcOBrZRJ67xBf1uk6Fucx5w1FB4pLBglPs7oD3pcF309Un3VRoM1EQgDu2RIB6cbkft8_p-qI_DXq3Q9XpI-h0cI8qW0sSucHApdDXy_O9xtKIOGTjqyQ2Pk3Bssb0E3oFCy-ruN4q6TTJdlpmLwDfm2DT6mXguNDtMa07nX-ID5rjeTBScZIFIskznD94LnMLm57OcG06SmdDp9WtJhg5Uo-Emhm8_4ZkZ_KGVOHDGWBhdxw8ckVZVmaAW7gDbzqz5Of7mGRX6LSlsqjg5cv2ajJlS453SzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بحرية الحرس الثوري:
خلال الساعات القليلة الماضية، حاولت أربع سفن، مدعومة بالجيش الأمريكي الإرهابي، عبور مضيق هرمز. وخلال عملية مشتركة بالصواريخ والطائرات المسيّرة، تم إيقاف السفن الأربع في مكانها.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83760" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83759">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⭐️
مكافحة الإرهاب في إقليم كردستان العراق:
تم استهداف أربيل بخمسة طائرات مسيرة إنتحارية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83759" target="_blank">📅 02:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83758">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83758" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/83758" target="_blank">📅 02:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83757">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83757" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83756">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83756" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
