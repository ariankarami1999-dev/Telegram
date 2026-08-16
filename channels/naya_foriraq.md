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
<img src="https://cdn4.telesco.pe/file/OHCKsSt6yC4Y-hRuM4em7Us2bCvHpQgNjo1PzWZXt71eMBMXLbyuYdauQs-XgFTuOptif2oUfOly7waytxTeTxZKE0Nm-Cxbd5KKJqLHJYUozgDE4ZCpX3PlRzSFQZQ5WBgAwzAH6DOvHFI2thDKduKSie5LNAIXLw2J5qyYqmoU9cElCaqSmR-2PKO1hRX6sxgG1p4EMs-2E7Bm0pEcGg2nccIj7ImaG1YHyYhvJYCVe4XidzHsYOgwhjdVTvLHjomB8tqxY_1Lf5QxupLvMvb-qpp-dgiLxu2XLf9CWkxdB2B-Qh_r0p8NmpPak1MTnYcqQjpDz1bY4zNJn3Y5CQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 21:11:39</div>
<hr>

<div class="tg-post" id="msg-87910">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPvqTcBn_5Z65M970kDVkD9WPC2U90Z_EIn8Gve7lRcVFpaeCrqdGi5n9j28d0reF2vD935Yg7eL6JuaH1Wn31yzvMTaUM_xvlzKheNTGKsZBfdHscgCXNBK-1Fw0WhRoGwkAk9EJkjOImU42QHiBOqOu0sE0Lh5g7T4hYyh_FZy4GZP4jQxyOo1bFKQC92atoH3-Rw_JWOh67Qp2UvZJxZpsLcnBH1dZtWfXUACybXXy7NVzgXkqNreatTQxMo-zKR5ZQlnvob14TSAfS6Gd-ickMjmf2V7ccf3SRwX_T06VBeDgUtIe5IkR1GukiqCBeO7SjquUtJNnixPnlO-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
حزب الليكود الحزب الذي يقوده نتنياهو يطلق حملته الاعلانية
(يريدون ان يخسر نتنياهو).</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/naya_foriraq/87910" target="_blank">📅 20:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87909">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu03PY8UkgKI0TnQLa0yKevAgDmVUHI2fm9kfQEw5k2-Mftcj3GlHgMSW8lsCH_SQMpzYTaXfSe8qmkDpZRIwuJSALkkrr-BMyCe4PkvUDHxkRBQz4OsKdy8cYfWQKjdhwMHMVAwULMnX9utO7U5s_tj4YfL22C16YBWPVPs-4ahXxRqjWGegGnaezp8sotWRQEnp_-s-B7i3-Gl7jypX8XIiMq2Ktmp-d4PPni2YCAUbrx0wP_kThLKIzGqVpuK0UwdMUxjDyAmZi47lQE_kWVHyEsOBXDjO1JOsERL5XAkKDMuy2ayCDAx5ZXRF5kVRtxB035sbQnPzOor7bVfBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الايرانية:
‏
تُطلق واشنطن على كندا لقب ولايتها الحادية والخمسين؛
‏تفرض واشنطن تعريفات جمركية على البضائع الكندية؛
‏واشنطن تهين كندا وتهدد بمعاقبتها بسبب دخان حرائق الغابات؛
‏........
‏رد أوتاوا: مفهوم يا سيدي!
‏وفي الوقت نفسه، تشارك أوتاوا في الحرب غير الشرعية التي تقودها الولايات المتحدة ضد إيران، وذلك لاسترضاء واشنطن!
‏ما هي المكافأة؟
‏هذه ليست ليلة الهوكي في كندا؛
‏إنه فريق واشنطن الرديف.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/naya_foriraq/87909" target="_blank">📅 20:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87908">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇱
اعلام العدو:
بعد 32 عامًا من إصابة والده في منطقة سُجد جنوبي لبنان، أُصيب الجندي (أ) بجروح خطيرة جراء انفجار مُسيّرة مفخخة تابعة لحزب الله في منطقة علي الطاهر، صباح أمس السبت.</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/naya_foriraq/87908" target="_blank">📅 19:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87907">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
وزير المالية العراقي:
نتجه نحو إقرار أول موازنة للبرامج والأداء في تاريخه تربط تخصيص الموارد بالنتائج، إغلاق مضيق هرمز ترك آثاراً مباشرة على الاقتصاد العراقي وماضون في تجاوز الظروف الراهنة من خلال تعزيز الإيرادات غير النفطية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/87907" target="_blank">📅 18:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87906">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0bac8e80.mp4?token=gncQAUTV7fR13jfBSBhjlezXbl5NuCw1ac6Vujlmpm7tLF4Z6cA0bAKLwQB0NmfN2qnire5T6JiuGt8JMPDezaGG_DnxqRZLE86mJxck9HjFvathqxWfg5DOiVvLxcFbzPSl3i070NVkMfCeTp3fxyQkoQu1XwX7UXvOjIkUNLGA0YG0rI3RLIkDGMTLhZeAfxI8iRhlGo8Neaiuvh1DrmP6p62u4tunS9eikluu7zb1OD7_1fDm2nlQchTzz7OMegtM3_OZulgATUjMdm7rYAzdlA0shluczhuj22D3z82RFniP-8k0fyMIer3uBpoAY06nWQpMJq986-cP5YGb4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0bac8e80.mp4?token=gncQAUTV7fR13jfBSBhjlezXbl5NuCw1ac6Vujlmpm7tLF4Z6cA0bAKLwQB0NmfN2qnire5T6JiuGt8JMPDezaGG_DnxqRZLE86mJxck9HjFvathqxWfg5DOiVvLxcFbzPSl3i070NVkMfCeTp3fxyQkoQu1XwX7UXvOjIkUNLGA0YG0rI3RLIkDGMTLhZeAfxI8iRhlGo8Neaiuvh1DrmP6p62u4tunS9eikluu7zb1OD7_1fDm2nlQchTzz7OMegtM3_OZulgATUjMdm7rYAzdlA0shluczhuj22D3z82RFniP-8k0fyMIer3uBpoAY06nWQpMJq986-cP5YGb4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر ثلاث طائرات فقط تابعة لسلاح الجو الأمريكي للتزود بالوقود جواً منتشرة في قاعدة العديد الجوية في قطر، موزعة عبر المدرج بدلاً من أن تكون متوقفة معاً</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/87906" target="_blank">📅 17:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87905">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇶
النزاهة العراقية:
الحكم بالسجن لمُدَّة سبع سنواتٍ بحق محافظ صلاح الدين سابقاً عمار جبر عن جريمة تضخم الأموال والكسب غير المشروع.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/87905" target="_blank">📅 17:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87904">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASXoJWG6dDdBMWaNHS4FmTCWEMsVCdfKAFIqmVGzcmvertXcLPyunFWs9gbBs_6PDzLky8oC-_hoamFoc7mrn2MQP6hDHeKgT3h9JMSYR2EjKcTj77WkQzq4nTRirikiAzt98GBTz9qW452VVduNdaeHg_hWewovogerHwvgCHdG93Epyi_qBBhptc41_EYlohZzDeE9DGC2tcwlTIbJknBC-AWCUMyuzlzrRN60lbSwlaMzNqTQBznhFgGI03RYHqYCaZ1mlYWo7nfFTUzoJZ8dGtMVwe4tlu8wPsrI9zMfZxqSs3--Xf2tXGOE67WlvbRgpvu98TUcRd-KUHYM6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجرات تهز السعودية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/87904" target="_blank">📅 16:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87903">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات تهز ابو عريش بالعمق السعودي في جازان   ال سعود ظلمة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87903" target="_blank">📅 16:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87902">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87902" target="_blank">📅 16:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87901">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/87901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87901" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87900">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجرات تهز السعودية</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87900" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87899">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87899" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87898">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/87898" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87897">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
قائد الجيش الايراني:
- مضيق هرمز المقدس هبة إلهية للأمة الإيرانية، ولن يعود هذا المضيق إلى سابق عهده.
- من بين إنجازات الرئيس الأمريكي تفعيل مضيق هرمز.
- كنا نعلم بهذا المضيق، ولكن لولا هذه المعركة لما تم تفعيله؛ أي ثمن نتكبده في سبيل ذلك يستحق العناء، وسنحميه بكل قوتنا، امتثالاً لأوامر القائد الأعلى للقوات المسلحة.
- هذا المضيق أحد الشروط الأساسية لإنهاء الحرب بشكل يزيل شبحها عن إيران.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/87897" target="_blank">📅 16:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87896">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🇺🇸
‏طائرة تابعة لعصابات الجيش الأمريكي من طراز P-8 تحلق بالقرب من جزر المالديف على مقربة من ناقلات النفط الإيرانية قبالة سواحل سريلانكا ومن المحتمل أن تقوم العصابات الأمريكية بعملية اقتحام.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/87896" target="_blank">📅 14:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87892">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGaP-m6NoZCA9irhTiEfp_TGz9Ps2NVKtlL7oH7UJTFGG3GXSpY4qS-XodUYeC7_3EshY_UDnzuOm_OdHJymRsbNf8lO5ZFzBJgirpYh4hJTAisHrhFd4gOIoGe3J2LheAtvRwTQMaOB4tJ-Y7WxxDL_cZBLPR2NrTHSLpZ9Du_X-pJh5UtS409O73CgSOGJGa_5uljxzori2WJ553BQAd-KDu21FxUcLbMnNcAjNcJGkmg5CyVnVEX9D8YdSDsnn8A-arXMmBw2dGt5ytv53IITxeln7lBeh-s29j5kflf3ej5YRYYjT5TEY10CrfBLgJLQJlzcM88U9WESCsoflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMLsLer2SWhJsjD_lMXeVXwyQh4nCB2qaXfnjwzYNev7bLQFNz98KhtzxWpXMpXpp-9zPfchvVShW_pdtD4iZSxdiyQF-TzM3elruxjG0sQRVWIOY7CCOT4RWpmiD_xd4_KeOc1Hu6HWYbT6KSro2q1PZeQoLPPYOtfqBnquZCyu8SA9gHzDqiVDYnHd7gFFKKTcDI4d7ti4eJz9DyKqG0z0px2ILCFqiDmeE12kfzNGlCERElw-eMC8yUlbI-0JBnfG8HYK9JTgILMm5cwzij3Gl09oMWQjdswjSOYvY3sFDlX79cW7E2Fm2wF7BO8beuT_HnQH2FxiHGIH6UxNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNQCFf5kH0mJHYh1vMZsU6PVEPk_DiqP6IV6jCFeG3cGSTZ4O27B3Gq1gKQH5efac3fs4lajnkNmwrpTjTapaZbVDuUM_43CfU2wx-KCEALQADLcFfGTCKtUA6N1u8iDZybH4yCgV-gm7uVJwFbij0N8qH4ku_YDO-SLfes0mBolO6VsfedZUG_k36MQ0thPSpBhVmsqRWGX5zY05bwWOep7JJ7QIQL1ISmTrrHYh2cU6qb38pRy7ZRI61CIPQvMnv4LOrm1rXdAhaiG5MpXJ-vQzr6yodhEdy92Eyo_FdXVbJWL0PHagJTf0rGclWut3eVi_rnZGMXdk_x1fAIHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q42xbcgp2_5z2g2BNhEsDwc2JXc0pVFFyb44I8b49N7bQErPyfKI1jTx5lMsi6BEz7j0RQWOtCuEGtcXtLUOm0JX1GBegXdZwExe7L5Cpkf5P3ffP2NRwPcqTmLGb521rn9vhUer2NN44lC1v-R9Hg6AZ838Iy5fkdw7tyq_JBY53qSwJvAXuXk3owWyEbvGboQNOaufRyk4PlCGqyNvh5I5PtRRK1n8_BTFIMUWv4jbNtFWzJEPIiwZE5pI9vUbfdUuCU2EnX7ib-nDiRqSoj8F__FSmt6b8UfH2aUhOBIeVSJuX5TMOWe-dnZD4nird96Fa3tUDszAOD3SA8n7mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
حريق كبير يلتهم مخيم شاريا للنازحين الايزيديين في محافظة دهوك شمالي العراق</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/87892" target="_blank">📅 14:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87891">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d572bf9031.mp4?token=SQgq7aFjiHW23NJL0XEKEIunO0k44LV9NTCRdaHvhOiKBoi4asCXK6jdIDlnlnRbtOeSAoaq_iaqWKv1a-_UK3Cv9jvVeKlUH00xwsQ33DIWGxjZv-8h1A4Du1ofqCpe5WI-pRd9Q2q8FyS0TK52AVgUtQmO9wHBid-l55ikIJGJRt-jjPY-s8A-HQxjnMyRZ4dvKY-kfr2XvQ5CHz7lx_gSn_bkDmcmOAfE7vSlRbUwGRQOMbBIm5cmgA-1j-p17_JBkAIKiFus-8bdAnbtIzcKKxrfWieRYPiZQ0-zsJZzE__S4yXWF6e25ui0VhOV2VWlfxde9RL0bEpbnlc1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d572bf9031.mp4?token=SQgq7aFjiHW23NJL0XEKEIunO0k44LV9NTCRdaHvhOiKBoi4asCXK6jdIDlnlnRbtOeSAoaq_iaqWKv1a-_UK3Cv9jvVeKlUH00xwsQ33DIWGxjZv-8h1A4Du1ofqCpe5WI-pRd9Q2q8FyS0TK52AVgUtQmO9wHBid-l55ikIJGJRt-jjPY-s8A-HQxjnMyRZ4dvKY-kfr2XvQ5CHz7lx_gSn_bkDmcmOAfE7vSlRbUwGRQOMbBIm5cmgA-1j-p17_JBkAIKiFus-8bdAnbtIzcKKxrfWieRYPiZQ0-zsJZzE__S4yXWF6e25ui0VhOV2VWlfxde9RL0bEpbnlc1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جماهير نادي زاخو تنزل العلم العراقي من ملعب مباراتهم أمام نادي غاز الشمال ضمن منافسات الدوري العراقي ومراقبون يتساءلون: أين الذين أخذتهم الغيرة على العلم العراقي خلال زيارة الأربعين مما يتعرض له العلم العراقي داخل إقليم كردستان؟!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87891" target="_blank">📅 14:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
حاكم مدينة مهران الإيرانية:
صوت الانفجار الذي سمع قبل قليل في مهران ناتج عن عمليات تدمير الذخائر المتبقية من الحرب في الأراضي العراقية، ولا يوجد أي حدث أمني.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87890" target="_blank">📅 12:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87889">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
القائد العام للجيش الإيراني:
بمشاركة الشعب، إذا تمكن أي جندي إيراني من القبض على أو قتل جندي أمريكي متجاوز، فسوف يحصل على جائزة قدرها 30 ألف دولار من الشعب الإيراني.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87889" target="_blank">📅 12:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87887">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NReLswzqkJl8Nk2iKH8q0b7jpATWROTaXyAqs5A_plAi3S9d2kUeljw9gvzfo585NMJyPyfYd9V2ZOSrRTCftsdMHTh9U3KHgBDbJbdNCznzQCp-M-j7J-axM4M_dB5c4C591gkm04m6jpBeskrjqUK0s4HimhhJtYA6MMPNWftQ_vWIT29AMqCIbuDIit_oitK54kWKwzLB__2ZU1pbvpCqTM8cp1O3j9JxSJKmIMVwKTbPmBtFQ-YfVKJIRtOnxfEdQ3Il4yqvZa4M2tlvYAp3knmnBIxVUOCreLbc-xw1aXXDXh7WDxUVZETnGeFxafs4tVu60R2WXQZ8gJRv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c305e2b0ee.mp4?token=IicCBFZ0vJIpW7sSAVEWYs5x5NHSN6ymz5RPs2FtD-AG3xchR9NwLsBTmzDhq2B2tmufNbwOrQOUPivJOIl4l_H3B4--pH5Yum_vUAsp-rwLi2nv2Onmeez6P56SLm33kXl8M8Y4AjRtdkMKk9u3OmuL2Stl49FcXnUa55ItjU9bHeeIbvDoCAJkHFqU_km1GDoDLnktnrBp3llfQOOVSqkY54aRrRIu-Le5djKj_DSc2WrjnPlEgK-mjGtb-gXRDr61qIJgAjbml_ixd8Hf6Std-Ibfj9CDOxA83v_GTfa4yok-VdecctItI-dsrg5IhwWH9nKvj9Tj7fEQtj4IQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c305e2b0ee.mp4?token=IicCBFZ0vJIpW7sSAVEWYs5x5NHSN6ymz5RPs2FtD-AG3xchR9NwLsBTmzDhq2B2tmufNbwOrQOUPivJOIl4l_H3B4--pH5Yum_vUAsp-rwLi2nv2Onmeez6P56SLm33kXl8M8Y4AjRtdkMKk9u3OmuL2Stl49FcXnUa55ItjU9bHeeIbvDoCAJkHFqU_km1GDoDLnktnrBp3llfQOOVSqkY54aRrRIu-Le5djKj_DSc2WrjnPlEgK-mjGtb-gXRDr61qIJgAjbml_ixd8Hf6Std-Ibfj9CDOxA83v_GTfa4yok-VdecctItI-dsrg5IhwWH9nKvj9Tj7fEQtj4IQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إصابات في صفوف المتظاهرين من خريجي المجموعة الطبية جراء إطلاق قنابل صوتية ومسيلة للدوع من قبل القوات الحكومية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87887" target="_blank">📅 12:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇷🇺
🇬🇧
ذا صن دي تايمز:
استُخدمت طائرات بدون طيار بريطانية لأول مرة لشن هجمات داخل روسيا.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/87886" target="_blank">📅 12:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
نتائج الحرب مع إيران.. وزارة الطاقة الأمريكية:
تراجع مخزون الاحتياطي النفطي الاستراتيجي إلى أقل من 300 مليون برميل.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87885" target="_blank">📅 11:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇦
زيلينسكي:
13 منطقة أوكرانية تعرضت للهجوم هذا الأسبوع وأطلق الروس أكثر من 1550 طائرة مسيّرة هجومية ونحو 1560 قنبلة جوية موجهة و62 صاروخًا على مدننا.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87884" target="_blank">📅 11:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴
مَرَّ أربعينَ يومًا…
چهل روز گذشت…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87883" target="_blank">📅 10:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
هيئة أركان القوات المسلحة الإيرانية:
نؤكد أننا لن نتراجع حتى تحقيق الهزيمة الكاملة للأعداء الأمريكيين والصهاينة في المنطقة، وتحقيق الحقوق للشعب الإيراني البطل، وخضوع العدو. ولن نتنازل عن المطالب المشروعة للشعب وتطلعات قائدنا العزيز، في وجه أمريكا المعتدية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87882" target="_blank">📅 10:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
‏
الحرس الثوري:
على قطر السماح بتواجد فريق من خبرائنا بدلاء من إنكار قضية احتجاز الطيارين.
‏خبراؤنا ينتظرون دخول قطر منذ عدة أشهر لإجراء تحقيق ميداني بشأن مصير الطيارين.‏
قطر ترفض إدخال لجنة خبراء وتقصي حقائق إيرانية للتحقيق بمصير طيارين إيرانيين.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87881" target="_blank">📅 10:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇾🇪
🇸🇦
إنفجارات عنيفة في مدينة المخا اليمنية جراء هجوم لأنصار الله على مواقع مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87880" target="_blank">📅 10:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0696943056.mp4?token=JCT-mfRO86mJCpHxe1a53MPN5lro10QtMJ_9O4RH51szH8OdlyJkl-FEMpsoO3eN4G5ENMLN6HDmdzd-v_8mz8zGKl74FB7-5yrqYzG3NiX5ftJVA8-cs3uT6L9pdkoJsNfhrHy9d7IXiCTJN8y0xsgzj3xJPIolv6dkgm9lexLd8AdsJkEBOAWUIQ8Ub5P9BHU2pfXvk4lPK2AkpGT53ABOxKaXkWvn-YA7mHDnN0HWRFmypqU2lmAnfAN1JhTdpT_8f6AzEYDIhM126pWTWo_ZV5GfQjy82x_-hw9Wy-VJeEVt24U_zrA-fxm-boxP_RbjCbpjcXGbsdrjlakG7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0696943056.mp4?token=JCT-mfRO86mJCpHxe1a53MPN5lro10QtMJ_9O4RH51szH8OdlyJkl-FEMpsoO3eN4G5ENMLN6HDmdzd-v_8mz8zGKl74FB7-5yrqYzG3NiX5ftJVA8-cs3uT6L9pdkoJsNfhrHy9d7IXiCTJN8y0xsgzj3xJPIolv6dkgm9lexLd8AdsJkEBOAWUIQ8Ub5P9BHU2pfXvk4lPK2AkpGT53ABOxKaXkWvn-YA7mHDnN0HWRFmypqU2lmAnfAN1JhTdpT_8f6AzEYDIhM126pWTWo_ZV5GfQjy82x_-hw9Wy-VJeEVt24U_zrA-fxm-boxP_RbjCbpjcXGbsdrjlakG7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني   اصوات الانفجارات ناجمة عن استخدام قنابل صوتية من قوات مكافحة الشغب تجاه المتظاهرين السلميين من خريجي المجموعة الطبية المطالبين بالتعين .</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87879" target="_blank">📅 09:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87878" target="_blank">📅 09:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87877" target="_blank">📅 09:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87876" target="_blank">📅 09:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏
🏴‍☠️
🇷🇺
بلدية موسكو:
تعرض المدينة لهجوم بـ 600 طائرة مسيرة ليلا وإصابة ثلاثة أشخاص</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87875" target="_blank">📅 07:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87873">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29dd6be136.mp4?token=P73iUCTNzZes_aJRm2HMn8vgY2IFuf_kTcGyIdzNsBVHXMDs1kbN7ZxuKS1oK5QbytWETPRa9NsfW5sAVrnC53v1bkmi1f19H0cc9pOW3SpT3MinV_l64-5arMsjAxs3_dHvPz8fHs9KV46r6yK5NWzIGgVKVlPcICyCI4gssH4lt_iT7uL9E0ipSTxRXP7H3JuLtUoFWLH5KJWRjim4MbEgcYE9h4BgVHoqTTla7jvmZ2gM3QYhpLp4j1pQoRh1mDsUcJ38ef5PHMkHBnBAmwDbfxpwbsSz0RXwcF3YOQZQb9Drao1apBN96kaB1nJ_MWaOqS0bG9V83HpHzrghNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29dd6be136.mp4?token=P73iUCTNzZes_aJRm2HMn8vgY2IFuf_kTcGyIdzNsBVHXMDs1kbN7ZxuKS1oK5QbytWETPRa9NsfW5sAVrnC53v1bkmi1f19H0cc9pOW3SpT3MinV_l64-5arMsjAxs3_dHvPz8fHs9KV46r6yK5NWzIGgVKVlPcICyCI4gssH4lt_iT7uL9E0ipSTxRXP7H3JuLtUoFWLH5KJWRjim4MbEgcYE9h4BgVHoqTTla7jvmZ2gM3QYhpLp4j1pQoRh1mDsUcJ38ef5PHMkHBnBAmwDbfxpwbsSz0RXwcF3YOQZQb9Drao1apBN96kaB1nJ_MWaOqS0bG9V83HpHzrghNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇶
🇺🇸
فضيحة عنوانها منظمات المجتمع المدني المدعومة من السفارة الأمريكية في بغداد USAID
تداول ناشطون على مواقع التواصل الاجتماعي مقاطع فديو لناشطة معارضة لقانون الزواج الجعفري المقر موخراً بمظاهرة قرب المنطقة الخضراء وسط العاصمة بغداد ادعت انها شيعية وان القانون جعل الشيعة مضحكة امام العالم لتكشف صفحتها على الفيس بوك و مقاطع فديو سابقة تتحدث بها على انها مصرية ومن السليمانية فمن نصدق الفديو الأول ام الفديو الثاني ؟ فيما تسأل ناشطون عن الدور الحقيقي لجهاز الامن الوطني وجهاز المخابرات العراقي وتفعيل دورهم المطلوب والرادع عن طبيعة هكذا تجمعات وشخصيات ذات هويات متعددة !</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87873" target="_blank">📅 06:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87872">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrhYXpqKrrvRn3R2Omae2FClA-sjgDfm_FQ1HrHfWwmIzb65yl_jnmKLWXkpvVlI71S_x8wFbgxdaFuTwhplPca8Yn-4K5IzvA5oPJhXccV6ru05c5MZ63ef2yiCRLCcBe4YZPUpeGCNbol2eNUHw7QFnFW6IlzRj-4uzfJ6zFUvQ8JmrIT4iO7XpweThWYjlX0FUKjGzdpy-WenwwpHpZN5Y0fdBOzE9PzWLSMHbThAkTFKs8fNDzzjtEZQksIAMJuGn6gGmtx79-8rnfAjrzjhsrRFqRVaabUtrprjxvX4IMOM9EqjWAIB9NP8v3C7q4evpjtrBbW3Ah4t5FMOpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إنّ من أوضح أوجه السيادة المنقوصة للعراق هو هيمنة امريكا عليه اقتصاديًا واحتلالها وسيطرتها على امواله حرفيًا وتحكمها بثرواته كُليًّا.
فهل يرتضي الأحرار للعراق العزيز أن يتعامل مع ثروته وكأنها منحةٌ تُسلَّم له، لا حقٌّ سياديٌّ أصيلٌ لشعبه؟
وهل نطلب كثيرًا إذا أردنا التحرر من الهيمنة المالية والاقتصادية الأمريكية، وتنويع أسواق التصدير وشبكة العلاقات المصرفية، وبناء اقتصادٍ يملك قراره وثروته ومسارات تجارته؟
فالسيادة لا تكتمل بالسيطرة على الأرض وحدها، بل بامتلاك القرار السياسي والاقتصادي والمالي بعيدًا عن هيمنة ايِّ قوةٍ خارجية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87872" target="_blank">📅 01:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87871">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRyPbEhjljPDj9SOp-xxE9dBOq7FsXsHpWjEmMhawkxzCC7UAeemhJdroXZXToQbH2ayw6AO__IOctbMeYZcOXOA9b6zy1q-bB1KvkE1oyLS3Fj8mTCxVVvNCratPifQDW-R-JDTQMFnpz4M5JPnLD8eXqfCBv7aRwLWAgutQftg3F161UHtKc6POdqhNIX2TCIW1gR2XEvYnYJAFIP_BUO24Pc5vp4UVkv7x1BGoaXpGHJXI_7CcTrkkycX0SH2mqwdGmJosOq5h9_beNl6wn94nel7G0-lQuU_KfeJECtKYETUlA4Yt8DtOaKKs1SlAAfxiSDCVBvFIf_iniefMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
سنتنصر.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87871" target="_blank">📅 00:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87870">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb4c61f98.mp4?token=Uj09Li-_Jpm2q3lDrefmqo-EOtXxZhKbLZ6HLV2TvE7Ru57GoRMGIsjhTNc3dX-sWksFjUzi56anviTJ8YAKXbIxaBoEcSVG7mfeZNKOQjWNfuFRE_Gxw1hSSvsT8HZ67hoXihZnJDY5dVSSyke49B637P4Qy4hQxXWDs3igfyGit2kRBa2CUsmXvQVvXggU4P-6x7LjRyYlPWhMBR0VeWh1pDp4RwdBkZjzHP0Obs448GrdKhILBqi2uvo4t1OrWeJUowJofUgyKbL_pg0x4xxCtgF58qfEQMcnlvJDqXHM5wPAfCBJsKGMCChtrL53M0-lRXu6Tcw-jc2il2rCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb4c61f98.mp4?token=Uj09Li-_Jpm2q3lDrefmqo-EOtXxZhKbLZ6HLV2TvE7Ru57GoRMGIsjhTNc3dX-sWksFjUzi56anviTJ8YAKXbIxaBoEcSVG7mfeZNKOQjWNfuFRE_Gxw1hSSvsT8HZ67hoXihZnJDY5dVSSyke49B637P4Qy4hQxXWDs3igfyGit2kRBa2CUsmXvQVvXggU4P-6x7LjRyYlPWhMBR0VeWh1pDp4RwdBkZjzHP0Obs448GrdKhILBqi2uvo4t1OrWeJUowJofUgyKbL_pg0x4xxCtgF58qfEQMcnlvJDqXHM5wPAfCBJsKGMCChtrL53M0-lRXu6Tcw-jc2il2rCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
انفجار في محطة كهرباء الحرشة في الزاوية بليبيا اثر استهدافه بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/87870" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87869">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd380ae70b.mp4?token=Re_ByfCtgJGlIN1DUWWdMW83edNFzn7LJolTegGa9BUsNEjonly-oNRhd5zTuT3130nt2VuD1rWPcjtqWlKolhR1Hn7oebEBA8_WL0wxnFmRkqL5IAflkXzXnWoln0QlB75iJBtbzHUuh08n21p4G3e9AR-dlmoWDJkyp_ZIKaJWqHWyLdgsfxzIcijrFtfozvVZurcXFAxgakwAIBGT1W2WveGGhvZ3x6LbRY6vZGWOa-5foMom6JS-js-07CzfTHvMCTAtfUTolv8PUfuBc796FRhj8b1Kws2Hr034yVSSqOw2qRnf1DKs0IzADYdg0hCHsMWWD3kY-3C0nXx6qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd380ae70b.mp4?token=Re_ByfCtgJGlIN1DUWWdMW83edNFzn7LJolTegGa9BUsNEjonly-oNRhd5zTuT3130nt2VuD1rWPcjtqWlKolhR1Hn7oebEBA8_WL0wxnFmRkqL5IAflkXzXnWoln0QlB75iJBtbzHUuh08n21p4G3e9AR-dlmoWDJkyp_ZIKaJWqHWyLdgsfxzIcijrFtfozvVZurcXFAxgakwAIBGT1W2WveGGhvZ3x6LbRY6vZGWOa-5foMom6JS-js-07CzfTHvMCTAtfUTolv8PUfuBc796FRhj8b1Kws2Hr034yVSSqOw2qRnf1DKs0IzADYdg0hCHsMWWD3kY-3C0nXx6qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
اكثر من اربع انفجارات سمعت في مدينة مأرب</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87869" target="_blank">📅 22:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87868">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇶🇦
‏
الخارجية القطرية:
ننفي ادعاءات احتجاز طيارين إيرانيين، فرق البحث بحثت عن رفات الطيارين الإيرانيين وتواصلنا مع إيران للتنسيق.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87868" target="_blank">📅 22:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87867">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
رئيس خلية الإعلام الأمني العراقية :
موعد 30-9 ليس بعبع وهناك مفاوضات تجري عبر هيئة الحشد الشعبي كونها المؤسسة الدستورية والقانونية لهذا الملف .</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87867" target="_blank">📅 21:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87866">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
انفجارات متتالية تسمع في صنعاء ناتجة عن اطلاقات صاروخية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87866" target="_blank">📅 21:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87865">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇾🇪
انفجارات متتالية تسمع في صنعاء ناتجة عن اطلاقات صاروخية.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87865" target="_blank">📅 21:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87864">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3kxGNeQxXIKiOQr8WNWxyE0isNZwIP88m1uvzAYoJhttsqtg28K_255s7H66MiHR9YCObRZGZxGnAGbrzSKt85AhltwgU0Uyyl4efXvZBMurQHa7muGyeN4JuV6do4vOun7ybsW3a8VgeSbIRk5rHDI_ei75YR67DHf71inbXU4qXwND172FanUbSYRVTFgD303zdkCod_HU-K7Qu8K7LmOA-pJ_nL3JcLMuXzncnPv0KI0ndYLP-pvm_nECYR7tsP0zzp2_o7d2zVUeXorpjGv4MiJWx8gVCwHdy2AqlutGtonD_rBwkbplwRap5t4jTHSbfu1AnrcxZu0myI5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
ثلاثة انفجارات قوية تهز مدينة مأرب.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87864" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87863">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله اكبر اصابات مباشرة تطال المليشيات الموالية للسعودية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87863" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87862">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇾🇪
مشاهد متداولة لمدينة مأرب يعتقد انها ناتجة عن قصف لانصار الله.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87862" target="_blank">📅 20:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87861">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb5TiSeu59ja6sqPuz7b_LCUd6bAhUWYKNKYRrVFBaPFGcTrvFwpFEGQ57CiaOnr3rEuMwJ7OchD2QdjIJKLMaC-ZTfg26jMpMkWNrMLJO24ZPZxQoW1kMl3U9BFouicy_XCN13vfkdy3xGp8ntYoXrgGyowbE7D7xPLt9WFHhIoSFYz79Zmm_aYrqQzqtKG94_yd5LR3fcMF_nP9csZ5GZmp6FPnG94KBL_wqW3Cqp641ZiwwpBNGlQfH6t3seSCwlpg2qbUXpT-LuvnZTO_oe1ItH2Ot8P_il9cBuCG2NTaxPXQlxsOIA9O9oBfEzFxGAonqsMD1Et6OgpD6s0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
مشاهد متداولة لمدينة مأرب يعتقد انها ناتجة عن قصف لانصار الله.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87861" target="_blank">📅 20:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87860">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA60C0fAMRKQ9ojvK_k8jW6D0RjcBPs_hUpkY-bKCljN8RSb6Y-ADq29Uyd_kfvJToA6yuzYRhZt2oBQzi4Gy5Fcipv29wEbEhTU95A7U5fRFjtvnOF7vSB_9YmpJNdQnVVTwA20NZ8Xf4C5B_byBfXam0pg6fzjOorxxhQFIzwSxb4N1TKQhvURAO-YRGCb291JeWKOChtLPHqSPCGxkkswlYS6FXa65_qinKmDsTGRRZ2NUO5ipb9unK7vMakwNDcgqbtDaSIKpAPUBB24OQYmXKjgRAJq05-1zQfDAFSFJaRhPd3Y4PP4ZE7uuWE7tSK96VVkw8B39efcblUyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هل العالم بوضعه الحالي قادر على فقدان أربع مليون برميل من العراق في حال اندلاع الفوضى ؟!  هل يعلم الإطار التنسيقي ان حجم ضربة لوبيات الطاقة العالمية للعراق الأخيرة الهجوم الأكبر" ضربة السعودية للعراق " كان بسبب فقدانهم نصف مليون برميل فقط من بقيق !   هل لا…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87860" target="_blank">📅 20:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇱
إعلام العدو:
تعرض دبابة لهجوم في قطاع غزة نتيجة لغم تابع لحماس.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87859" target="_blank">📅 20:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هل العالم بوضعه الحالي قادر على فقدان أربع مليون برميل من العراق في حال اندلاع الفوضى ؟!
هل يعلم الإطار التنسيقي ان حجم ضربة لوبيات الطاقة العالمية للعراق الأخيرة الهجوم الأكبر" ضربة السعودية للعراق " كان بسبب فقدانهم نصف مليون برميل فقط من بقيق !
هل لا يرى ساسة العراق افول امريكا بهرمز و وضع قواعدها بدويلات خليج فارس ؟! وبروز نظام الدفع المسبق للسفن المارة بخليج فارس  ؟!
هل ستقطع علينا امريكا الدولار الذي هو منقطع أصلا على العراق منذ ثلاثة اشهر ؟! وتمنع علينا بيع السندات ؟!
ام ستقطع الكهرباء التي هي أصلا مقطوعة منذ ٢٠٠٣ ؟! ويومية هزي تمر يا نخلة اجه جنرال الكترك راحت سيمنز ؟!
متى يعرف قادة الإطار التنسيقي ان مصلحتهم لا ترتبط بامريكا ولا البرتقالي وان مصالحهم الاقتصادية مع احزابهم وخوفهم من المجهول لا يجب ان يكون على حساب سيادة وتاريخ شعب العراق …
كل مشاكل العراق وبروز نظام بشكله الحالي القريب من امريكا وتحت سيطرة الحاكم في العراق والشام " توم باراك " بصورة مذلة يتحملها قادة الإطار التنسيقي ال 11 …. وعليهم اما ان يتولى مسؤوليتهم التاريخية او ينكفوا عن إدارة البلد …</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87858" target="_blank">📅 20:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obh5fJDY78Qd0HwAns8ZiEyL21Apq4rZgMmKhlhYTyWuZqMLnp9KTCXPQ2nLRjyV-NSazYqI2myqxtQ3QBs81zhgB3Cz_H3RSJ7tOUC0mXRUQ6ZvPR8WCV7mORCoM5id8n1JGOcLoxggPA4JbOF61Pl1DSfNcm2SYpPBCpN8WZekbQ7otKFHYG2tLe1yrJJAq9i5n6aKEW-XtgC8eQTe-tHRg3v3Sw7CAzksThyEDNryL6uz5nBhXaxmPQUsAn6Ppi4IRj54e5TUGYj4WTq_8w6DgtG185pvfmqLsldNK91O1x4a_sIpISjDGgaWKrocsgDbG5A7T9zObIavUtckdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اول تعليق للبرلمان العراقي
زحمة قناة رسمية تثير الفتنة</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87857" target="_blank">📅 19:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FACLFewM06dP0kF44vBQ0i9RsBs7BUgB9YgG_lBEjGyycRdP96K6mfO-6fWJQSPzfn4cJWqiieE9HC3VQzZmZeBy0-MhVEj1m8HzsPsfUulxuVUaafPuxe34iZ8w-as0dwH1RaaZOTTltLafFKQ4m9xR-ap-YNldo08uK_p0j8w4JnbL_qXjN2XRoFy956byZ0vvL0TiOaoGXt6pYF1I04bkQ8Tnt16yTu5WDWzQxs7Q7pWQhBnCe2fQ-czOW2M0IAXBQJcfGqqTB-EQW1tCpPbq_SiI8W_nklH9HAYKSvxXFn9gkOS9U64PK6skkJDT96PAJd0N5WYT9tnfJHOzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: على الرغم من المظهر غير الودود في هذه الصورة بالتحديد، إلا أن هناك العديد من الصور التي نبتسم فيها، وأنا و Kim Jong Un نتفق تمامًا.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87856" target="_blank">📅 19:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87855">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
أعلن المتحدث باسم كتائب سيد الشهداء،
أن الفصائل المسلحة لم تكن وراء الهجوم بالطائرات المسيرة الذي استهدف مدينة أربيل فجر الجمعة.  كما يوجد "شبه اتفاق" لوقف العمليات وتأجيل الرد على الهجمات السعودية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87855" target="_blank">📅 18:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87853">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇾🇪
مدير ميناء المخا اليمني يوقف العمليات بعد هجمات الحوثيين.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87853" target="_blank">📅 18:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87852">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
رئيس مجلس امناء شبكة الاعلام العراقي: تقرر ان تخضع جميع الفواصل الاعلانية اياً كان مصدرها للفحص والمراجعة من قبل الادارة العليا للشبكة ولجان الفحص المختصة فيها.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87852" target="_blank">📅 18:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87851">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇱
مكتب نتن ياهو:
هجوم لحزب الله في "منطقة الأمن" اللبنانية يؤدي إلى إصابة ثلاثة جنود والجيش رد بقصف مقر أصدر أوامر الهجوم ولم نعلم الا لاحقا ان بداخله مدنيين.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87851" target="_blank">📅 18:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87850">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7OzoOmLmAmiYKf_OBkUXXr3Sx8qqMEtAW_EtKjS0YwauBf5WtbAjlZcOVL_72ZyXmIsAIswiY4B-PsQFdn3eqfdxUpi4uHKhE0v0VsNw6NZR_Goznc2cp6NdTksH_PPk_NC9WtMSVun86LoHQwWTzcC7bUraFT-1dq1Ud3H2knto0XIZq0KfF2Q4VEtN-TzHaZIKSgK1J1-q7c92NJu35S2u_1w4Maa0fIqsRIJZyU2VL_Oref944dQ3KpHpAXhpEpQNKYEm7wz8-bzwhjZhFQOffinuvSLeD_omUnbeAxyViouQhhjn2MwB9DHkMkIG4dt-wSWmIcs2chiFa6KGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
رئيس مجلس امناء شبكة الاعلام العراقي:
تقرر ان تخضع جميع الفواصل الاعلانية اياً كان مصدرها للفحص والمراجعة من قبل الادارة العليا للشبكة ولجان الفحص المختصة فيها.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87850" target="_blank">📅 18:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87849">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عشرات الآلاف يقررون التظاهر ليوم غد ايضا احتجاجاً على الدعوات الطائفية في محافظة بابل وسط العراق   المواطنون يطالبون بمحاكمة عدنان الجنابي و شيوخ الفتنة والتحريض .</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87849" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87848">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
مصادر خاصة بنايا   حراك برلماني لاستجواب رئيس شبكة الإعلام العراقي تمهيدا لاقالته وذلك لدفعه وترويجه الاقتتالات والحروب الداخلية في العراق .</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87848" target="_blank">📅 17:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87847">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b7ffa1c5.mp4?token=X2C0r4xzzyxBARYfKkzgZqGyaCukGTSp92UOqehMcOmnbV48z1LfpyYd5sx2u7TM6lZQBMyLy1YwGlh1UXKqWRnFCCAc6OA-ZF1DlLjcQKFu2zq_grWn3gnAIt6w2zfmo_TOJ4J5KsCbnpXXCRFAhs6iGDYXOmUjbDqiMVAs4TM6Xe76xUZKO7ii1rNoQnXGpPgwUFkW3Rhi5O8Gb2m9K-v-OHEXoZLZl3H1hKuwlWVFbTQFAlccOKPEVoRX8kYyc-BajCjMxbipFCBJTPCoJ59354RlwegEdU6Bz3Jt_wV7iTzTGJjlKEWVz6J8VmT1x3X84YI_oggtIoUEa_NGAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b7ffa1c5.mp4?token=X2C0r4xzzyxBARYfKkzgZqGyaCukGTSp92UOqehMcOmnbV48z1LfpyYd5sx2u7TM6lZQBMyLy1YwGlh1UXKqWRnFCCAc6OA-ZF1DlLjcQKFu2zq_grWn3gnAIt6w2zfmo_TOJ4J5KsCbnpXXCRFAhs6iGDYXOmUjbDqiMVAs4TM6Xe76xUZKO7ii1rNoQnXGpPgwUFkW3Rhi5O8Gb2m9K-v-OHEXoZLZl3H1hKuwlWVFbTQFAlccOKPEVoRX8kYyc-BajCjMxbipFCBJTPCoJ59354RlwegEdU6Bz3Jt_wV7iTzTGJjlKEWVz6J8VmT1x3X84YI_oggtIoUEa_NGAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🔻
الموضوع هو اكبر من المقاومة وسلاحها ، الهدف هو الشيعة وعقيدتهم التي تقف اما المخطط الصهيوني الابستيني ومشاهد ملايين الزوار من الشيعة حول العالم في الأربعينية هي مشاهد مرعبة لأمريكا وإسرائيل ودول الخليج والهدف القضاء على هذه المظاهر لأنها شعلة الحق الوحيدة المتبقية في العالم ..</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87847" target="_blank">📅 17:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87846">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الرئيس التركي: استمرار الهجمات الإسرائيلية على لبنان يشكل مصدر قلق كبير لنا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87846" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87845">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سلاح ما نسلم   مثل ابو حميد ما نصير</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87845" target="_blank">📅 17:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87844">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c189e3c62.mp4?token=C8C_mB0hhUKIxOAq9IEL-ly3ygo0tsC8qqyfjAhkL86GKNuNrad-23H7AsuGydqIIFFvaBiH4MGqJq2okPP7V4o_c4JTAbY7F6YQxsoR4iIGinfIVjtzkqsvxV6KdSqRv1uLKr3UDpe196Ig8BdCIkWJH1cPJLk4bL1RBHHluWz5f9zyvb-s3IcA9YBDvWDLN5eDB9p7dmmTM0lGOOyKxohA0SdKjFpnbSakg4wD-2M6GVEk6wqge_vmUr34PM3GxeEJMliSK4ERl6jGEVl5QifZTcaMjsvsY9KzXpVia3Y25jUw70jiA9i0hc_DEKJoQnbW2zgr9f2iAjRGm8gKxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c189e3c62.mp4?token=C8C_mB0hhUKIxOAq9IEL-ly3ygo0tsC8qqyfjAhkL86GKNuNrad-23H7AsuGydqIIFFvaBiH4MGqJq2okPP7V4o_c4JTAbY7F6YQxsoR4iIGinfIVjtzkqsvxV6KdSqRv1uLKr3UDpe196Ig8BdCIkWJH1cPJLk4bL1RBHHluWz5f9zyvb-s3IcA9YBDvWDLN5eDB9p7dmmTM0lGOOyKxohA0SdKjFpnbSakg4wD-2M6GVEk6wqge_vmUr34PM3GxeEJMliSK4ERl6jGEVl5QifZTcaMjsvsY9KzXpVia3Y25jUw70jiA9i0hc_DEKJoQnbW2zgr9f2iAjRGm8gKxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشرات الآلاف يقررون التظاهر ليوم غد ايضا احتجاجاً على الدعوات الطائفية في محافظة بابل وسط العراق
المواطنون يطالبون بمحاكمة عدنان الجنابي و شيوخ الفتنة والتحريض .</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87844" target="_blank">📅 17:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87843">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIWNDkQVySm9uRf8SHQOCJIQOPFVTaZ_KAgmbRELN-bKC9O8wlnfbOFqxyHXsbXzyeI4D640LXi8fq_Yb81bcMI_uvg3RIbMAgil7cvGehbM3v92oLdQwxB0YE7QEoqBYCThg1IzD1K7jcUL5D2iVQOb8rKfrh1QdKkmQ0_DVEvYDjmG9PdIYE92pGoQHxipejXNAuK0MlGOF-HKMYhDzlAyriRZeyoORoVyai4eRdB95nq20kc8aNng06kbpFA9f8l4ogjlaHu0RbY5Shu_GOa1McSPIGuOvOdYz0T202hcNSTwmB6C2MiBEy2ffGcA3kTKy1xwnuR7HyghLNlVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
منصات التتبع:
تواصل أكثر من خمس ناقلات نفط عملاقة عمليات نقل النفط من سفينة إلى أخرى قبالة سواحل الفجيرة، مما يشير إلى أن صادرات النفط الخام من العراق والإمارات والكويت لا تزال تعبر مضيق هرمز. وتدفع بعض السفن رسوم العبور الإيرانية، بينما لا تدفعها الأغلبية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/87843" target="_blank">📅 17:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87842">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb7dc434c.mp4?token=ERJY0hQ_7Dbl196DTzbmbASR7paOTYFY4kCNXtL9l9i9dw_zNI0Ax-6Hx9tEsGF1Y--rgjPGAR5nox9W5eeuuuhU-wEUF5jRsgjTr2xWn0bzXNxTanG6quUX-cNMItIXjxvocCIToGI0xD4Sa7os9Qn9WqhNPmbKxIrXr7zvW4xICHgR3j2-rJepEtMJYR2P3xXydWwPpRZMfgI9cn93Z70jVWwJcHYMMviEZQuBQUQUh3RQzQ8qCxvq8tT5ga8KzNfcKbHR-X3cUIMyJIsjd3FYcRUUifCYR4d3yPaChqDlHM6xAjzKl_JOy8k7eTgrFMw3MJgIzz--3wjAkLTq4FRphzT6ueRgqFhtCb1VAFS4WvgUL__RW1iXCxtHrMb8aJwFq0va9VvHrBkUD7wMjAjasg9GePB6KzxxVUFj9zjMq_yyyyZecPTkdD5LRvVc5-dXXzpUbiNagRP39ZV8WWNk0VQA8XMLdZTlIEZpY-oBv9KJRtPFmQOh27NMIvfcOiZMZXR-9MovMsTrEpfjggOJhNcyQX4dG9B9Rc53IMv4ijjS3Df1JW9TPxHJsTe43vXBzkBOMZ4FiYr2uATLZFQ4_QasxjMN9gdXCJCZnErMJ12VSPz8CDeiXf0Q4AChmwNoS56Ti7916V7jv8x-QYQWlZqjPBi606s21QtOteU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb7dc434c.mp4?token=ERJY0hQ_7Dbl196DTzbmbASR7paOTYFY4kCNXtL9l9i9dw_zNI0Ax-6Hx9tEsGF1Y--rgjPGAR5nox9W5eeuuuhU-wEUF5jRsgjTr2xWn0bzXNxTanG6quUX-cNMItIXjxvocCIToGI0xD4Sa7os9Qn9WqhNPmbKxIrXr7zvW4xICHgR3j2-rJepEtMJYR2P3xXydWwPpRZMfgI9cn93Z70jVWwJcHYMMviEZQuBQUQUh3RQzQ8qCxvq8tT5ga8KzNfcKbHR-X3cUIMyJIsjd3FYcRUUifCYR4d3yPaChqDlHM6xAjzKl_JOy8k7eTgrFMw3MJgIzz--3wjAkLTq4FRphzT6ueRgqFhtCb1VAFS4WvgUL__RW1iXCxtHrMb8aJwFq0va9VvHrBkUD7wMjAjasg9GePB6KzxxVUFj9zjMq_yyyyZecPTkdD5LRvVc5-dXXzpUbiNagRP39ZV8WWNk0VQA8XMLdZTlIEZpY-oBv9KJRtPFmQOh27NMIvfcOiZMZXR-9MovMsTrEpfjggOJhNcyQX4dG9B9Rc53IMv4ijjS3Df1JW9TPxHJsTe43vXBzkBOMZ4FiYr2uATLZFQ4_QasxjMN9gdXCJCZnErMJ12VSPz8CDeiXf0Q4AChmwNoS56Ti7916V7jv8x-QYQWlZqjPBi606s21QtOteU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توافد حاشد لموقع التظاهرة في محافظة بابل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/87842" target="_blank">📅 17:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87841">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">المتحدث باسم الخارجية الايرانية بقائي: لقد تم التوصل إلى اتفاق بشأن خريطة حركة الملاحة بين ايران وسلطنة عمان</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87841" target="_blank">📅 16:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87840">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da068288c4.mp4?token=ZsjtDnJ-NkjODtgQaQl2SBK8TIsfSW_e65YKQhy-KUsFi9PIqGsOxI2iGq7hSxYJ0pI16AW8cZzjtJ45TxVsakP2VXVp4kWDDxJ_6xSu6r25bOjW_tw711EWVh6iM3ZVKcJw4Mou3TZ9Iupq1eSpGLayDJkF6M2wCFxZMA4TUIk_z4toiGhUZYrc-APge_To-wsPNqjR4FAZaLofqfgUzokMGAacCoMQSHJ4p08fer-5f-6VLTomipkwcoFhDCz7ags-b9WThamTW4adfmo26l-EI2gdY3JjzYweIRu1pAaLnTPyC_GfwgTL-Hq88xtcuofB3epzu0GsUOYc3q-Xxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da068288c4.mp4?token=ZsjtDnJ-NkjODtgQaQl2SBK8TIsfSW_e65YKQhy-KUsFi9PIqGsOxI2iGq7hSxYJ0pI16AW8cZzjtJ45TxVsakP2VXVp4kWDDxJ_6xSu6r25bOjW_tw711EWVh6iM3ZVKcJw4Mou3TZ9Iupq1eSpGLayDJkF6M2wCFxZMA4TUIk_z4toiGhUZYrc-APge_To-wsPNqjR4FAZaLofqfgUzokMGAacCoMQSHJ4p08fer-5f-6VLTomipkwcoFhDCz7ags-b9WThamTW4adfmo26l-EI2gdY3JjzYweIRu1pAaLnTPyC_GfwgTL-Hq88xtcuofB3epzu0GsUOYc3q-Xxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلاح ما نسلم
مثل ابو حميد ما نصير</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87840" target="_blank">📅 16:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87839">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d027dce5.mp4?token=rkdYJ6SSyBRa0Tnjxl0S6XyR5gtT-NHqx3uzrLLPBlenlSQ_E-XaHjOqqyse51UsXq30ZBTnFZu5V34O6IJ0H4_e5mXeXI47ZIxlvkP06yd4AvYpIHEordf7pP3HK-7Mo2gdrrW26ztpOnYJZq0AnM3tnynV5mJCwhzZ5a6ggR4OGeWyiExFTY1kkPBOPIOwoMbhRUzWLNV2PsPUxBYqW4kWG1WEwZfAzQT2T00jBRnts8DptW7JKXjMuZZ-2rpn7_OW1bFwETvNbg37sx6dIv6Vjk42Np60hdfQtutr2kHcIhkN6hfG51dj0TUUItFFCZAhibhDCO_xEEY3pqx6OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d027dce5.mp4?token=rkdYJ6SSyBRa0Tnjxl0S6XyR5gtT-NHqx3uzrLLPBlenlSQ_E-XaHjOqqyse51UsXq30ZBTnFZu5V34O6IJ0H4_e5mXeXI47ZIxlvkP06yd4AvYpIHEordf7pP3HK-7Mo2gdrrW26ztpOnYJZq0AnM3tnynV5mJCwhzZ5a6ggR4OGeWyiExFTY1kkPBOPIOwoMbhRUzWLNV2PsPUxBYqW4kWG1WEwZfAzQT2T00jBRnts8DptW7JKXjMuZZ-2rpn7_OW1bFwETvNbg37sx6dIv6Vjk42Np60hdfQtutr2kHcIhkN6hfG51dj0TUUItFFCZAhibhDCO_xEEY3pqx6OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطنين يتوافدون الى موقع الوقفة الجماهيرية في محافظة بابل لادانة عودة الارهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87839" target="_blank">📅 16:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87838">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏وزارة الخارجية الروسية: شحنات الأسلحة الأمريكية التركية المحتملة إلى كييف ستضر بعلاقات موسكو مع واشنطن وأنقرة، طلبنا من واشنطن وأنقرة توضيحات بشأن مزاعم وجود خطط لتزويد كييف بالأسلحة</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87838" target="_blank">📅 16:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87837">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بدأ وقفة جماهيرية في محافظة بابل للتأكيد على رفض عودة الإرهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87837" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87836">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
اللواء 52 بالحشد الشعبي يتسلم قاطع بسطاملي في آمرلي من الجيش ضمن تنظيم توزيع القطاعات والمسؤوليات الأمنية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/87836" target="_blank">📅 16:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87835">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa80e2a4e.mp4?token=ElQXU1jFdjuJ3SoRhSvDmnp043qZ1iworqwtKPQo9GV1jVgrHZ9Is4ZXfO9T8IDCHuf4tPbJp77CQ6MjJenRd4XLhCJOovKmWngd2AYvYMLFk7zu3tEmaJsyB23JOdUzq0OjOqZKcvtNHImfIqfiXAfHNkT9rQx7LaS5MtmzwXNJY0db4CTZfRKLdb0nqstyFtfnYw2gX9vY9_cn8iYgxoF5tVjm9cGdNQdJ6iisMFoJ_R0Mih_msheHLlBfDqzBmM0bAY0r0gM9UGkO2wf1QBygKSpRTpF8PxYbISItVGS6vQbgq5Ahb52LDUiKe7DW3UEbf45CP4NnmDKGb2K3zgMwS1VODm3JZeqdx1N50lxEvBU3RuGznV8ei6e8Y6XYhinA4caahL_vtHfC5cAhuTbOv9xqITATaSwcRWDWI6RjMCoI2yUjTs5jK-bQbAv6qp5IE6L0eKlXeXY4D7YxqcHTBDg934ZuFa36GOcvFgwFiVsERMXqOC0Iuop2eZkvPqdbsokdFGBU--XXF3FanB9GtHNikZousKkMFx9nwoS102x8y38EuVoqF8f8bAvgJJ1OoH4Rf8RmW7zPF8fef8DtMl22aA1PxJzhqw6aeM1_5rX8W9zsbPOY_IjljByVZ7-P_t7NGX6orGePnXD5ki-g5sqAYG4JLD6mQSq1VvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa80e2a4e.mp4?token=ElQXU1jFdjuJ3SoRhSvDmnp043qZ1iworqwtKPQo9GV1jVgrHZ9Is4ZXfO9T8IDCHuf4tPbJp77CQ6MjJenRd4XLhCJOovKmWngd2AYvYMLFk7zu3tEmaJsyB23JOdUzq0OjOqZKcvtNHImfIqfiXAfHNkT9rQx7LaS5MtmzwXNJY0db4CTZfRKLdb0nqstyFtfnYw2gX9vY9_cn8iYgxoF5tVjm9cGdNQdJ6iisMFoJ_R0Mih_msheHLlBfDqzBmM0bAY0r0gM9UGkO2wf1QBygKSpRTpF8PxYbISItVGS6vQbgq5Ahb52LDUiKe7DW3UEbf45CP4NnmDKGb2K3zgMwS1VODm3JZeqdx1N50lxEvBU3RuGznV8ei6e8Y6XYhinA4caahL_vtHfC5cAhuTbOv9xqITATaSwcRWDWI6RjMCoI2yUjTs5jK-bQbAv6qp5IE6L0eKlXeXY4D7YxqcHTBDg934ZuFa36GOcvFgwFiVsERMXqOC0Iuop2eZkvPqdbsokdFGBU--XXF3FanB9GtHNikZousKkMFx9nwoS102x8y38EuVoqF8f8bAvgJJ1OoH4Rf8RmW7zPF8fef8DtMl22aA1PxJzhqw6aeM1_5rX8W9zsbPOY_IjljByVZ7-P_t7NGX6orGePnXD5ki-g5sqAYG4JLD6mQSq1VvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام امريكي: المنفذ ليس واحد بل عدة مسلحين</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/87835" target="_blank">📅 16:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87834">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUUnC0dVKcHTbb0ygW6V-waaQCuAS2X9HN-2A_bzO-RhmLh2a4fpZSbPxaIDqMPpimLHhrS-HnBG0_zLPoMqnaj4UZkyKcLfy6B8M8Haw0hNBX-4M0MB3j61L6OMrd8JEM_eY07unp_r8Y9s57pBVDuiZtNXZ-9QcqRnr8XX3l3BbY2MUdJ6d7Xmb-zW-0f7HNNn20pQlVOga3Pqsly5rbxHdzKk73OSMJfFmqZORsGZIS2n8DRsiz_BteALwqu9YbavyS5hIHJuViQAsHYASHxuCdazuIzCZIMSp48fXjZbuK2G0vrJd1hfzUZijeJZm4aYWEzA44x7Oyy7WtWZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مصادر لنايا
شبكة الإعلام العراقي بصدد انتاج الجزء الثاني عن تسليم السلاح لكن شخصية حميد ستصبح كاكا حمه في اشارة لسلاح مليشيات البيشمرگة ..</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87834" target="_blank">📅 16:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87833">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اغلاق جامعة ولاية فرجينيا بعد الهجوم المسلح</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/87833" target="_blank">📅 16:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87832">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اطلاق نار داخل جامعة فرجينيا ومقتل واصابة عدة اشخاص كحصيلة اولية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87832" target="_blank">📅 16:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87831">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حدث امني في ولاية فرجينيا الأميركية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87831" target="_blank">📅 16:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87830">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حدث امني في ولاية فرجينيا الأميركية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87830" target="_blank">📅 16:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87829">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
بيان صادر عن حزب الله:
استيقظ اللبنانيون فجر اليوم على وقع تصعيد عدواني ومجزرة وحشية ارتكبها العدو الصهيوني المجرم بحق المدنيين الآمنين في الجنوب، من خلال استهداف منزل في أطراف بلدة أنصار الجنوبية ومبنى في دير الزهراني، ما أدى إلى ارتقاء إحدى عشر شهيدًا من بينهم أطفال ونساء وسقوط اثني عشر جريحًا، في جريمة موصوفة تضاف إلى سجل العدو الحافل بالمجازر والجرائم وسفك دماء اللبنانيين وتفجير منازلهم وجرف حقولهم ومحو معالم قراهم.
إن هذا التصعيد الإسرائيلي، باستهداف المدنيين وتوسيع دائرة المناطق المستهدفة، يعبر عن رغبة وإرادة رئيس وزراء العدو المجرم نتنياهو  بتصعيد الحرب تعزيزاً لواقعه السياسي الداخلي، وخدمة لأهدافه الانتخابية وإرضاءً لليمين المتطرف. وإن هذا التمادي في العدوان وانتهاك سيادة لبنان تتحمل مسؤوليته حكومة العدو  والولايات المتحدة التي تؤمن الدعم والغطاء لها، فيما يجب على  السلطة اللبنانية أن تبحث عن السبل المتاحة لوقف هذا العدوان وأن لا تصر على الاستمرار في مسار المفاوضات المباشرة المذلة وتقديم الهدايا المجانية للعدو، رغم كل ما يرتكبه من جرائم واعتداءات، وما يعلنه من نوايا عدوانية وتوسعية تجاه لبنان.
لقد آن للسلطة أن تراجع حساباتها مراجعة شاملة بما يحفظ سيادة لبنان وحقوقه، بدل الاستمرار في سياسات تأكّد عجزها عن حماية لبنان وشعبه، وأن تقف موقفًا وطنيًا وشجاعًا ومسؤولًا، وأن تتوقف عن اللهاث خلف المفاوضات التي يجرّها إليها الأميركي، وأن تدرك أن الرهان على الضمانة والوساطة الأميركية هو رهان خائب، فالأميركي شريك للعدو الإسرائيلي في جرائمه ومجازره بحق لبنان. وما التصريح الأخير والوقح والابتزازي للسفير الأميركي في لبنان الذي دعا فيه إلى تسليم سلاح المقاومة، فيما المطلوب منه أن يضغط على العدو الإسرائيلي للانسحاب من المناطق التي يحتلها، إلا تأكيد على أن ما يبحث عنه الأميركي هو مصلحة العدو الإسرائيلي وأمنه على حساب سيادة لبنان وشعبه.
إن على اللبنانيين جميعًا، بكل مكوناتهم، أن يدركوا خطورة النهج الذي تنتهجه هذه السلطة على لبنان ووحدته وأمنه واستقلاله. وإن على العدو الإسرائيلي أن يفهم جيدًا أن اعتداءاته وتجاوزاته ومحاولاته فرض أمر واقع لا يمكن أن تستمر، وستقابل بما يناسبها، دفاعًا عن لبنان وشعبه وسيادته وكرامته الوطنية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87829" target="_blank">📅 16:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87828">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXS_rxtaZAn1akPNQ-Khcbi9jNi-KBUIbBp-_g9Rc7Z0guqRz9327ZZBHho3lqXNaNFZ6yPcZr6GzBlXolP_A_IZdCGcoyepgQEQsXr2Gj_IFLkg5zKLWrUB5t2q9wT38hakLDpgpXxwYEylsUBHi994FrMIQuaYvRE8ncfuw4rjxAgs6XUCD2wDGEQ1M_-v9ip7sYn6P69MX8CMxeYmZ_gT7_GTEH8GuZF4YqAxFa7PtT9E5l7ET32R44qgtyXXBH09jAhCK-9i0BPLNc9j1JD2VQoxlAfNNEKLhkW8Aqv9Kmyuz7Oz9zzhKPrz-jq7J-2_L0ckW-E8q7iOqbRL9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشوراء الفرقة الخاصة
نار على أعداء العراق</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87828" target="_blank">📅 15:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87827">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بدأ وقفة جماهيرية في محافظة بابل للتأكيد على رفض عودة الإرهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87827" target="_blank">📅 15:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87826">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNgPu9DC-GeeEh3JeXpo2vQMdWzEZThopiKtqqXKA-5VVdVQnSssdDOP0ftzx0wJfHDTlq7U1uqQ6TKkJXrNt1hd_4mXbZu8okxsn58QiFNNNx8e6nuHQg-Pli-d7_Yjrs3rE9T41GGe-0TKhs1MVV3SfMaxKghM-AZnKdTkenvt38sjMTMcj1FmrOIENGWPG-XLJ2TBe8Y1ZzDK0Iw2suks0IJw64-hh8604C_-uXqnkcLT2MxoGe3nFbuCB7k9jKxPKrT_SInIzOMfBY4rcr7ZMKOypwWAI_9rUMoSlT2rwZwa0E0gPiJJqCR0cGUlYveYCBGXf6fxEt6YOfeT2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لولا دماء بلال الوحيلي و شيخ ياسر عاتي الكعبي
لكانت الجرف الان ولاية ارهابية داعشية سلفية ..
شكرا حميد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87826" target="_blank">📅 15:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87825">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏قصف مدفعي متبادل بين مرتزقة السعودية وانصار الله على جبهة كرش شمالي لحج</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87825" target="_blank">📅 15:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87824">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">زلزال بقوة 6.9 درجة يضرب إندونيسيا، وهو الثاني في يوم واحد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87824" target="_blank">📅 14:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87823">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
الامريكيين ينتجون فيديوهات دعائية بعد ساعات من تداول اخبار عن تعطل مراحيض حاملة الطائرات الأمريكية "لينكولن" واضطرار البحارة للسير في مياه الصرف الصحي على متنها وكيف كانوا يحصلون على طعام رديء. كل هذا دفع البعض إلى القفز من السفينة.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87823" target="_blank">📅 14:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87822">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">السفير التركي في سوريا: اردوغان مغرم بدمشق وسيزور سوريا نهاية العام ومتشوق للصلاة في الجامع الأموي</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87822" target="_blank">📅 14:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87821">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
الحشد الشعبي جزء من القوات المسلحة وحصر السلاح يشمل الجهات غير المرتبطة بالمؤسسات الأمنية</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87821" target="_blank">📅 14:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87820">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: تمكنت القوات المسلحة _بفضل الله_ من استهداف تحشيدات وأسلحة تابعة  للعدو السعودي وزوارق حربية تابعة لأدواته ومرتزقته في منطقة المخا، وذلك بعدد كبير من الصواريخ  البالستية وكانت الإصابة دقيقة بفضل الله وقد أدت العملية إلى تدمير الزوارق…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87820" target="_blank">📅 13:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIm-sb_Ft6MMWEilZTqfqym-ALB1Fq1A0WKRcHUcQZ9xSqJO-OSacHK0gHXKJnzu-KMY83IUCjqiw4AX9my8TdOxowW-3WLVGVinA9Izv48SmLvw3n1MN5iR1GLrTzHQBAxjQwzFk7WbmM_rB3qyvB9_PFvv1Ucxrnh8ECioZNnel7aIEl6L0HybV3DJvVRyqrkmmgjyHKCZ-HsBnI7x0y95EvRoscRw3YICbaMO8xSSKNcrGcgnycJvtnyB6UzK6UQ8dhFOGpJuqjOsmTnBnqQBlvImeRSdBOPfKAHjCOMHh198qI1lv9IQ1DrT5KmeYtbMyEohRMudnGLd8ueT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مراقبون لنايا
تحويل الإعلام الرسمي إلى منصة تهديد ليس هيبة دولة بل عبث بالسلم الأهلي .. إذا كان المطلوب تطبيق القانون، فليُطبّق بالقانون لا بالوعيد من شاشة الدولة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87819" target="_blank">📅 12:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87818">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-ixGvD_6WmNBeiYTO9KfIcG_Del_74QFnTDo5HYUUjntA8339p4VihXdd_5_TSRmPUB_P7uF2SsH2jWhex5Hrft6KMkuIIxUNTjxQfn55-EA3yrwIPKPJTeKXL06uWVKZb1IIH_AI9RrlKO-Bn0mcN2ATCDQEMROEgNDMwpdxE_WmAhk0TcOXIraaMaKwFlW_TxeNcIgtVP_Uxlv_YdAVBBWPqvnQkQONCBKBw6cgn4BBGwuqAjeO1xQngzQjSFEGgKDa6Xm14SuUuE9efLosUAktB4DwEU2g4GDpH_k_pW3IYw_EUz4sPK_kvmld-yaw0EJzjAORYqGVnCCwVWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
🇮🇱
إلى أنظار جوزف عون و نواف سلام..
عائلة كاملة إرتقت فجر اليوم جراء عدوان صهيوني غاشم على بلدة أنصار جنوبي لبنان.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87818" target="_blank">📅 12:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87817">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4aa482a54.mp4?token=QeQotM5usC_GCP9CQ_mEC3XJ9UjU9PnG_aO_i53eB0BRwZ9m-NO1GhOYYDNm9s9ChqXnZ8ucZEmOdzSJ5oem6N7_WJpyVDuRiLz2A6eqV5ZhenizjTMFj92i5pTspNoI__s7BjovRtPqBdFfwyVCwhnYxLWTBucl_mttE8XHkhfeV1Evvq9qTaAgOexNRQsnlrCEpFQ-q-r1mBoOkzGjj53QFOukb5aZftNwtZw3SaCEtRf7UgI2Y6RghHQlwM7OaJahmBhb0IU0W4JTpLT4GGwLMg9uoxHjU6ajKyo3Y9EfWVhDdfm85jA4BuCNoG3OEdzq_ZkkRWLvuxomJPtjlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4aa482a54.mp4?token=QeQotM5usC_GCP9CQ_mEC3XJ9UjU9PnG_aO_i53eB0BRwZ9m-NO1GhOYYDNm9s9ChqXnZ8ucZEmOdzSJ5oem6N7_WJpyVDuRiLz2A6eqV5ZhenizjTMFj92i5pTspNoI__s7BjovRtPqBdFfwyVCwhnYxLWTBucl_mttE8XHkhfeV1Evvq9qTaAgOexNRQsnlrCEpFQ-q-r1mBoOkzGjj53QFOukb5aZftNwtZw3SaCEtRf7UgI2Y6RghHQlwM7OaJahmBhb0IU0W4JTpLT4GGwLMg9uoxHjU6ajKyo3Y9EfWVhDdfm85jA4BuCNoG3OEdzq_ZkkRWLvuxomJPtjlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇮🇱
إرتقاء شهداء وعدة إصابات جراء غارة وحشية من الطيران الصهيوني على منطقة مأهولة بالسكان في بلدة دير الزهراني جنوبي لبنان.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87817" target="_blank">📅 12:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
رئيس السلطة القضائية الإيرانية:
لقد أثبتنا لترامب وتابعيه في الساحة العسكرية أن مضيق هرمز جزء لا يتجزأ من المياه الإقليمية والحدود الإيرانية، وأن أي مغامرة فيه ستقضي على أي قوة متجاوزة ومغامرة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87815" target="_blank">📅 11:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عدوان سعودي على محافظة صعدة اليمنية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87814" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7000ddea94.mp4?token=WRxd_X4Qket1lmea07APlO9oB_0DbspvEa1GDvul5qtlwxyt083Ixl4d15n-dfzZNu-o6O292ec2P6vfRLBjBsC6LWQd_es9rKN4qYXzwHlXN4LDm46-fpFjG1QonOOKdR1lTrBsg7ahPai5Q2z0DDyiF2UAO6Xji2YZrWhK4HJP7zsbXvNS6E1026PaWOCYWjEKgOYaz5gM9maVudfG6oiBsPk96nKBCp3qZ8G-KzsceSm9DrPB4TPBykly51iFYbHM-hmJBgEbleCCW4Nb_W2DziMgeL7l8AYvXnncJI6eNIMP5au5zZSrrVf9Tm50COhTBEXNFfQuJrmO0Qw_oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7000ddea94.mp4?token=WRxd_X4Qket1lmea07APlO9oB_0DbspvEa1GDvul5qtlwxyt083Ixl4d15n-dfzZNu-o6O292ec2P6vfRLBjBsC6LWQd_es9rKN4qYXzwHlXN4LDm46-fpFjG1QonOOKdR1lTrBsg7ahPai5Q2z0DDyiF2UAO6Xji2YZrWhK4HJP7zsbXvNS6E1026PaWOCYWjEKgOYaz5gM9maVudfG6oiBsPk96nKBCp3qZ8G-KzsceSm9DrPB4TPBykly51iFYbHM-hmJBgEbleCCW4Nb_W2DziMgeL7l8AYvXnncJI6eNIMP5au5zZSrrVf9Tm50COhTBEXNFfQuJrmO0Qw_oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مروحي يحلق بإستمرار في سماء محافظتي أربيل والسليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87813" target="_blank">📅 10:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نيويورك تايمز:
هاجمت إيران في بداية الحرب القاعدة البحرية الأمريكية في البحرين، مما أدى إلى تعطيل مركز لوجستي رئيسي، وأجبر البحرية الأمريكية على الحصول على الإمدادات من جزيرة دييغو غارسيا، التي تبعد حوالي 3500 كيلومتر عن حاملات الطائرات العاملة بالقرب من إيران.
ساهمت مسار الإمداد الأطول في حدوث نقص وضغوط على متن السفينة الحربية الأمريكية "أبراهام لينكولن"، حيث قضى طاقمها المكون من 5000 بحار ما يقرب من تسعة أشهر في البحر دون توقف في أي ميناء.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87812" target="_blank">📅 10:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
🇺🇸
القناة الحكومية العراقية تهدد فصائل المقاومة العراقية   نشرت قناة العراقية الممولة من الحكومة العراقية فديو دعائي لاول مرة منذ عام ٢٠٠٣ تضمن لغة تهديد للفصائل المسلحة بالتزامن مع نهاية المهلة التي اطلقها توم بارك بخروج المزعوم للقوات الأميركية في العراق…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87811" target="_blank">📅 10:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX1uticxx9ni670T5fqK1uaDe5CoOhKg1BLqqTuQoT4roW_FVA6-gL6aGod-siBZfz62aARqs1IzIcnLJBQCHlXrlwF-eQMRT5iVJX54HpjbTD0kk37X4MvO0fNDsOHDzGs7h3z-K7-Z221J3ZmYtjCx1b32vu9JPfXVpZi1aUEWBGHNCTVq-Sj0tJmMwqXu8O3QFCidlGkqY33CX85ljafDxPEkgQ9yh6YvWX1GWwceBP_nn_0n5AplbsyKjMvDWAYFN92MT6BatqXhMlnSeoNvvp7ANNxSMOd0kQukeBRwMRtVQlPcX41x9uf_xJ-rxkv8SkAMF-iUfdyRtgyH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇺🇸
القناة الحكومية العراقية تهدد فصائل المقاومة العراقية
نشرت قناة العراقية الممولة من الحكومة العراقية فديو دعائي لاول مرة منذ عام ٢٠٠٣ تضمن لغة تهديد للفصائل المسلحة بالتزامن مع نهاية المهلة التي اطلقها توم بارك بخروج المزعوم للقوات الأميركية في العراق ومهلة الحكومة العراقية ايضا للفصائل بنزع السلاح ؛ المضحك ان القناة الحكومية استخدمت في الفديو طائرة MG 29 الروسية والتي تخضع للعقوبات وتفرض امريكا على العراق قرار بعدم اعادة تأهليها مع ٣٥٠ طائرة اخرى روسية الصنع تحولت لكتلة حديد بمطار التاجي بسبب الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87810" target="_blank">📅 10:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87809">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMUswe8zVGQUuQu5vl6hPfnI8Eokb4cxxEy8pzZfAHOsiBT__0IrHGBDgqGjQEJzokIh5WOAGw75C-o9xwa5CZiXhbfgoDbYtZJzBRglSS5chRPslrt2wfF3QLY76QlYdiS3Qa4FYcf0mEziFqgAnmV1aKv5zftMwNZ6xG4SIb2wPhIbOE8-1IQYkMUDNQImzYBITu3xOGr-fl4UhoKDhSUA5P9NgwhzP7y3x49fyOwd9KA7QVtx0l2UGq8bxmTn8oT4Ae2Z3yYTXRLj6lKv-2z0c_1oOYPvvsRupU8Ylik-JJWPVuCeAGRYiBjVdCtXzwr2K4IH5dhhqmlpYTqaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/87809" target="_blank">📅 09:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87808">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87808" target="_blank">📅 09:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87807">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
القائم بأعمال وزير البحرية الأمريكي:
عالجنا عددا من حالات الصحة النفسية على الحاملة لينكولن.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/87807" target="_blank">📅 01:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87806">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579ffff276.mp4?token=XWuCypXzzh724fBLQ-X0kfbfCxJ65S3nhuRh6HoFZ7scyElPAtPNSGCvCbOabPh7o6IaTsKTdSh6iwMFLwa3Wf8e8UGjBTGLuqHd7Ins5MdwOQjvbjGiTynqrQLGQJtHH4Qoc0G8jIKgeYhk_CKU3ud_22ITxUAfcCdWJno22CTYZrVO71JIfn3VSLW94eDrvrsdugmqTL5wzrxX_IJrmWet0eCz1CyYE2n_bZH_Np4iRvPPizEolRhEkydI0sPKeRdouraStWsQ4wTl92b3nP4q8JvIzLbvCGWySRnGtxnzqmP2fwrwTNn0VKZn0YUpEdqKv7zoIWZkDKgdVNXf-VKi6lLAmhZ6f7O5a3XW-A_Xkdz1d8Fx_c8nh6IT2xRowFAdnVV1nWG8UMdQpoLPBImnQrv1kFKbScrIF0fvK6RoKKW6sgC1G0dYdR9jffISBi-5gcDFetc-4iz0-wITTHSeq82r5F53eeiIUoq1XECC1A_S2rH-wBAyYt8Y7o-MR9TObp3Jd4z_WxazesVSWDX7ILYwX6CfnZhT3r85LjSFXGfM09nMzqnip4bXGxy2NfW6Y7-HqkzMYQMw6iuYcOEy_hjZGHkiLOa8PcGaz6d9bixCQzI99-h2CxBUXRI9G8X0EfqoBmxJwPHnZErKxup7UU_5IWTKFQXzCsmNDm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579ffff276.mp4?token=XWuCypXzzh724fBLQ-X0kfbfCxJ65S3nhuRh6HoFZ7scyElPAtPNSGCvCbOabPh7o6IaTsKTdSh6iwMFLwa3Wf8e8UGjBTGLuqHd7Ins5MdwOQjvbjGiTynqrQLGQJtHH4Qoc0G8jIKgeYhk_CKU3ud_22ITxUAfcCdWJno22CTYZrVO71JIfn3VSLW94eDrvrsdugmqTL5wzrxX_IJrmWet0eCz1CyYE2n_bZH_Np4iRvPPizEolRhEkydI0sPKeRdouraStWsQ4wTl92b3nP4q8JvIzLbvCGWySRnGtxnzqmP2fwrwTNn0VKZn0YUpEdqKv7zoIWZkDKgdVNXf-VKi6lLAmhZ6f7O5a3XW-A_Xkdz1d8Fx_c8nh6IT2xRowFAdnVV1nWG8UMdQpoLPBImnQrv1kFKbScrIF0fvK6RoKKW6sgC1G0dYdR9jffISBi-5gcDFetc-4iz0-wITTHSeq82r5F53eeiIUoq1XECC1A_S2rH-wBAyYt8Y7o-MR9TObp3Jd4z_WxazesVSWDX7ILYwX6CfnZhT3r85LjSFXGfM09nMzqnip4bXGxy2NfW6Y7-HqkzMYQMw6iuYcOEy_hjZGHkiLOa8PcGaz6d9bixCQzI99-h2CxBUXRI9G8X0EfqoBmxJwPHnZErKxup7UU_5IWTKFQXzCsmNDm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب عن إيران: كان لديهم 212 طائرة جميلة جدًا، بعضها تم شراؤها من الولايات المتحدة، وبشكل ذكي، في عهد أوباما. جميع طائراتهم اختفت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/87806" target="_blank">📅 23:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87805">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6da41714.mp4?token=p7_154eaAXQOa9z-gNEAd54LcYpBW22w4g-2exjcG8uPlAI1QUyxuEkfAqSv7qRlXVNHeg6pVTc8CQTmH9Nx6I0mrWop9av-PXvkc8m61PIo2mWZr89KJwoaMhjLnfj1gqD9QpgKC2regmDidpQKrhP6b1bF9E2pqKYla3N4b6pBfPhsNRhIZIgd2PZsp8KVtqp55fdoD8EtTO9Z-ep1OmRT7-R9dzODSMvj6mItPODhIiEuoj1Yrbu9kwtYWzJnBezTUbR-1pZ6DMHJTdJrDUlwdyR3X_fF3q9IRmWM2Cl6eVsTDt3OK5UacMcJ1VYsMBVteEQ1YzjfpKr7MHhnkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6da41714.mp4?token=p7_154eaAXQOa9z-gNEAd54LcYpBW22w4g-2exjcG8uPlAI1QUyxuEkfAqSv7qRlXVNHeg6pVTc8CQTmH9Nx6I0mrWop9av-PXvkc8m61PIo2mWZr89KJwoaMhjLnfj1gqD9QpgKC2regmDidpQKrhP6b1bF9E2pqKYla3N4b6pBfPhsNRhIZIgd2PZsp8KVtqp55fdoD8EtTO9Z-ep1OmRT7-R9dzODSMvj6mItPODhIiEuoj1Yrbu9kwtYWzJnBezTUbR-1pZ6DMHJTdJrDUlwdyR3X_fF3q9IRmWM2Cl6eVsTDt3OK5UacMcJ1VYsMBVteEQ1YzjfpKr7MHhnkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/87805" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87804">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
الوضع بين الولايات المتحدة وإيران مستقر.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87804" target="_blank">📅 23:48 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
