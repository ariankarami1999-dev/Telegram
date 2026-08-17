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
<img src="https://cdn4.telesco.pe/file/Y38AWV0lHxkOy8cxoXqtnyRvgYH1WFC7pZoZp10lJdTwUiuZUJaXw52Jh2LgX1SlrF44qUhnj2ue8NizJ7qGr8qRAO-lw8XOYi66Wsc17u8fM2zPlLO-i2AzPfWcfvu3EeV9W3J4CvLN3nGShgbW22le5gr2thgK232NPTQehDuzPLEkQ1ZqUhO3CBoNQmZPP9zJ78bQx4DMS0eXpfANxsABaKrGjUvsOXAPL-wEm0hoiM7qmxqPNL5unqIl2F7lMhPWehdI9txWzFbWvJdsQPKSkfl-h6jzIjBw80BavGl0O4PIg3Hi2S1ZOlmacyut5DyhNDNfkM6dWPebXsXCdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 18:46:47</div>
<hr>

<div class="tg-post" id="msg-87978">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن لاسباب مجهولة</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/naya_foriraq/87978" target="_blank">📅 18:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87977">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن لاسباب مجهولة</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/naya_foriraq/87977" target="_blank">📅 18:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87976">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde4f1ad56.mp4?token=DpvzqDzM7GK1TyVhmraqySXk405dDmSZP8iHwOZQu7GGrxprLwfntjNIwIKDfgebSuRWfLhpFCUSc11fpSW2JKGhKnbo-d_IWPfAS8S7B_DvFRlcpL4PJNWMzg09Tk__GMre2Pug3_GIFY4ywOL6O1a06PJ8OlStie90FHgZUdZ46NLg0a3_r--f3E2NcQiDyFkAIILuneCt5PAgHJ-jyd96AaIm2NtFVKFppfCTfGo7dbSm5bnDVVwva9i-RlpUYbs1yyJguY8HJMpucIe1aVOO5GN7ED8VpB-mPsYdnheRlO8mzf2LgKe50uIouOt8gWItALx_fTZxZY2nB0hnyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde4f1ad56.mp4?token=DpvzqDzM7GK1TyVhmraqySXk405dDmSZP8iHwOZQu7GGrxprLwfntjNIwIKDfgebSuRWfLhpFCUSc11fpSW2JKGhKnbo-d_IWPfAS8S7B_DvFRlcpL4PJNWMzg09Tk__GMre2Pug3_GIFY4ywOL6O1a06PJ8OlStie90FHgZUdZ46NLg0a3_r--f3E2NcQiDyFkAIILuneCt5PAgHJ-jyd96AaIm2NtFVKFppfCTfGo7dbSm5bnDVVwva9i-RlpUYbs1yyJguY8HJMpucIe1aVOO5GN7ED8VpB-mPsYdnheRlO8mzf2LgKe50uIouOt8gWItALx_fTZxZY2nB0hnyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوات الاحتلال الامريكي تعيد رفع بالون التجسس في سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/naya_foriraq/87976" target="_blank">📅 18:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87975">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3805200e49.mp4?token=ZQ-d7yHHsCzIrRHqTDgq960WsguTCp_FGUzAtKpPuJx8K3OBx_F4SCsz34_bvpBuDQpiOOYCukrUfhRdNadfj9nYhkk0cP48ur2PPOurUjf5M2TJcW74Jrni3O81Q7JzCgKJotniQN9Klll_4pr88Y3WSL-xXn-jUw-5MNnwJlaLHK9Zp394MD6vZm3cDhv1hWFvl5vjf1uhMhtOIp0GpVkK4k-RCWdq7xEIboUn-lQfjq9G-yLTG2g-LBzWE83oxgZy7c_yfY0IoQOos8EC81WdjwQK_TAYlt_Rco3hdVztSqo5jgOCqjZW85UyRtsPpZPVnhaoQz8B84GpVw8CQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3805200e49.mp4?token=ZQ-d7yHHsCzIrRHqTDgq960WsguTCp_FGUzAtKpPuJx8K3OBx_F4SCsz34_bvpBuDQpiOOYCukrUfhRdNadfj9nYhkk0cP48ur2PPOurUjf5M2TJcW74Jrni3O81Q7JzCgKJotniQN9Klll_4pr88Y3WSL-xXn-jUw-5MNnwJlaLHK9Zp394MD6vZm3cDhv1hWFvl5vjf1uhMhtOIp0GpVkK4k-RCWdq7xEIboUn-lQfjq9G-yLTG2g-LBzWE83oxgZy7c_yfY0IoQOos8EC81WdjwQK_TAYlt_Rco3hdVztSqo5jgOCqjZW85UyRtsPpZPVnhaoQz8B84GpVw8CQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوات الاحتلال الامريكي تعيد رفع بالون التجسس في سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/naya_foriraq/87975" target="_blank">📅 18:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87974">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L62xoZDeaSqOLu9QgoZL_KUBANiQzZolRj5TIa_jjLpNgwa8vyVxhxsIsohdX0rCoF4kopb5AI-5QFbzjZnGWD3GT3f1HJ-mt8U-Qig1yzeTBTorhD-ShHdVAV8oeLt5PzIVPpAU9Gkc5TvIUePuNKu6bTt72jdtqKRMb0cCDCGwZtFM2oaP14RzTGPnSNkU7Wi9hDOvSTm6oVfOdB4tl7Y0rCIyEA3qYzIoyXyJExWs8P-dqPs5Tj44RHsaDgp0Qz7pgp1dfaDOXM0scOhxiJCuIwRVEBhxRfmst4wrp-k1HFTpawtj2nWrRd-A-8tjnP6sA1xdpMZLHP5yCARCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية تصدر حزمة عقوبات بحق قناة الفلوجة:
- إيقاف بث برنامج حوار التاسعة لمدة (10) أيام تبدأ من تاريخ صدور قرارنا هذا المخالفته لائحة قواعد البث الإعلامي
- منع الظهور الإعلامي بحق مقدم البرنامج السيد (علي فرحان) لمدة (10) أيام
- فرض غرامة مالية قدرها 25 مليون دينار عراقي لمخالفة البرنامج وحصاد الأخبار لائحة مخالفات الجهات الإعلامية العاملة في العراق</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/87974" target="_blank">📅 17:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87973">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📰
🇮🇶
وكالة رويترز عن مصادر:
خطط العراق لتصدير النفط عبر خط أنابيب يمرّ في سوريا قد تتطلّب 4 سنوات بكلفة لا تقل عن 15 مليار دولار.</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/87973" target="_blank">📅 17:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87972">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
دبلوماسي في وزارة الخارجية الايرانية:
كانت دول المنطقة أول من عرقل تفاهم إسلام آباد، وبالطبع دفعت ثمن ذلك.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/87972" target="_blank">📅 16:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87970">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الكويت تقول ‏ان ثلاث مغذيات فرعية من محطة التحويل الرئيسية الرميثية (B) خرجت عن الخدمة .</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/87970" target="_blank">📅 16:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87969">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scaF_6yrPsen_l_epJMJsYvXeV9M5XM6i6cMUlgg23GelICriKcy8lZT5kIV9t2t7tAsIl3z1QxvwP61lZN_HsjOlEhEsxKK9OSCmI8hU99ZEYJrxUaX3VWurjj7NVkl9bfyvfnOC3elSSGBG3g45cO-Hokd5fsF5xo_DLYDZTCDCWrtr9VMxsrbhr-EkxKH-xzKJIkaaRxCnjwUAqyB4NSgGyErEYbaM_J_WYZdmcUIIyH0nK6No5RuW083MTOfDju1Ugfl-thR8yHAtP_Ka1k8tr7HHhZNffQRDaU4dRrpTEI26J4SudFBZimVNk_pRVZZBfOBuzzDit6lhl2KwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اختطاف المشهور ابو الجود المنتسب بالحشد الشعبي
من قبل قوة امنية مجهولة في العاصمة بغداد بمنطقة البلديات .</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/87969" target="_blank">📅 16:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87968">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
الفاضلية بالناصرية جنوب العراق تنتفض
على خلفية اختطاف قيادي بالحشد الشعبي من قبل قوة مجهولة " مسؤول وحدة استخبارات قيادة عمليات حزام بغداد " دعوات جماهيرية للتجمهر والاعتصام المفتوح من عشائر الناصرية امام مركز شرطة ناحية القديم الساعة الخامسة والنصف ..</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/87968" target="_blank">📅 16:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87967">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYDjfETvPEPubBKsddV9_7N9d-pHsvDu2Mh5QmUKZpuEHYIt4acr-w3IcUvIOX8O5B9-qfTMPT5T-Kub3SjZbb4KnVwMT1mMJxM5KntC8Sq3B89vKDsemBVmLkEZ_i7k47WdBgWy6VdS6LtrtEOS5qajCrZJ2hB7PsEGjotFHAlM_qfGk_JCk4XKStqUXHMZVv7KXNZdLCk3QwNpl8r_HHKXb8Z4VocIZxfgIYp_m8-84IO1CtoUzMFlQrdh4Tf1UJkGNwkUbGNA83_UR7Qc8Lp_8QxfcWoQXTAqRl-Np8c5EFExJPlZ1rEXU__zCVv1QfiEyaTc6CNug7i4V_HP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هجوم على سفينة والاستيلاء عليها قبالة سواحل الصومال</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/87967" target="_blank">📅 16:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/87966" target="_blank">📅 16:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">#ترفيهي  ترامب يزعم: لدينا قناة اتصال سرية مع مسؤولين في الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/87965" target="_blank">📅 16:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=PsvibrA2kJ9lKoL0NjlAHJpvsBiJzNCXxFC7U7ou1IPks2q0a05sEYJBHj-JVRn76jkGCWyoXsI7OgSUDyJiXfKq_x1rG4eW4M2I44hzGhvz-H8ULIln84Z1_nM8DB393ou_20cueqpv23VQPCI-G2ptTphhW0RXqir2gShdY6JDxAkFb6wi5o3Q6C3xYaAa-hfShxyNrap5ZOBVbac8SB9YkcRZ1pUUE7D2UgEDzyWmXqSqnQl0orrQ4UnLD3ZFbyGArXCAlt3o18fnNRrNijc7GJvLmPKla1XqbD8s2NDLULkRpmRLRz-NFCtizSouqs1bwWoGYZPLQlOxeD3X_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=PsvibrA2kJ9lKoL0NjlAHJpvsBiJzNCXxFC7U7ou1IPks2q0a05sEYJBHj-JVRn76jkGCWyoXsI7OgSUDyJiXfKq_x1rG4eW4M2I44hzGhvz-H8ULIln84Z1_nM8DB393ou_20cueqpv23VQPCI-G2ptTphhW0RXqir2gShdY6JDxAkFb6wi5o3Q6C3xYaAa-hfShxyNrap5ZOBVbac8SB9YkcRZ1pUUE7D2UgEDzyWmXqSqnQl0orrQ4UnLD3ZFbyGArXCAlt3o18fnNRrNijc7GJvLmPKla1XqbD8s2NDLULkRpmRLRz-NFCtizSouqs1bwWoGYZPLQlOxeD3X_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أُذِنَ لِلَّذِينَ يُقَاتَلُونَ بِأَنَّهُمْ ظُلِمُوا وَإِنَّ اللَّهَ عَلَى نَصْرِهِمْ لَقَدِيرٌ</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/87964" target="_blank">📅 16:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87963">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مسؤول إيراني كبير: سيتم نقل الإطار الزمني الذي حددته إيران إلى الولايات المتحدة والدول الإقليمية عبر وسطاء.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/87963" target="_blank">📅 16:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87962">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مسؤول إيراني كبير: جميع الكيانات الإيرانية ستكون مستعدة لتصعيد التوترات في مضيق هرمز والمنطقة إذا فشلت الدبلوماسية</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/87962" target="_blank">📅 16:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87961">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مسؤول إيراني كبير: حددت إيران مهلة لبضعة أسابيع للتنفيذ الكامل لمذكرة التفاهم من قبل الولايات المتحدة</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/87961" target="_blank">📅 16:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87960">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📰
مسؤول إيراني كبير لوكالة رويترز: قررت إيران تحويل سياستها من دفاعية إلى هجومية بالكامل.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/87960" target="_blank">📅 16:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87959">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📰
مسؤول إيراني كبير لوكالة رويترز:
قررت إيران تحويل سياستها من دفاعية إلى هجومية بالكامل.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/87959" target="_blank">📅 15:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87958">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">القوات اليمنية: تمكنت القوات المسلحة اليمنية بفضل الله من استهداف سفينة إنزال عسكرية تابعة للعدو السعودي مع أربعة زوارق عسكرية مرافقة لها في البحر الأحمر أمام سواحل المخا، وذلك بعدد من الصواريخ الباليستية وكانت الإصابة دقيقة ومباشرة وأدت العملية إلى احتراق…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/87958" target="_blank">📅 15:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87957">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
توجيهات حكومية العراقية بأن يكون عمل الشركات النفطية على مدار 24 ساعة.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/87957" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87956">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف سفينة تابعة لمرتزقة السعودية في  باب المندب بعدة صواريخ والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/87956" target="_blank">📅 15:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87955">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامب: قد أدعم شخصًا ما في الانتخابات الإسرائيلية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/87955" target="_blank">📅 15:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87954">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH4szANWQBbsulxh8ps6zTWv4oI9nOU7FRhal-mUBgZrRrfOocrE1O3021b-qBUjfrQW7Ns3NQnWS79dbVcQqJTKA3om0tGlzD7E1HcMh6Zh-Nmz70qPKb3no7Mw_iUM3kxVhMJWQO_p7HWNjS-Euf250xFjKKK1zLjRbkPDW2cerIDn4NjN-STy9Td0UnUa6sb17B6tkIY0VW6SivCkVZL4zypEqcuoZuuh_6HMnBVc708Ec3eYeQM39nu7zT9yfqgdnoLMiMpEsKC19tF3G1d5_6lq1KX1JzJjYLx45GT2uDh3PNCLjvz8KiD1TGXsqiXJZwEwYhKvSaeGvh1ggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
هجوم صاروخي لأنصار الله على سفن معادية في باب المندب.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/87954" target="_blank">📅 15:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87953">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhNEhpWz9zLUmgPixnVCqPIVJOzgzAr4XA1xq-qSOfkZGp0e3RLDozkXh6lqatEOnH5Z24Dju4ogEbjktsPfwBEgoEr_n9YFyS6KOsLSbMqJHktyHCjprwn8dnmucKpV_d2LfimBa6h6U5ugs5j3bkfaTeNcianYSWhbnMuIMlwND1Wua4ADJT0uk_HD_0auGVoLpCaGQFj6svKUQuJSgCw7VyulVrCmzQExBPNawE219rVElz156uso7XcToL0DXnEZc9YnirmSws8k523DYBudf882YYwYS1_tAD-ya-obYqzRROgfUdv2V_OMdRGh6DH3n71xAeo1q9Y9S2kAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏عبور السفن في مضيق هرمز يعود إلى الصفر</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/87953" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87952">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي يضبط 651 هاتف و341 شريحة هاتف كانت مخبأة في أماكن مختلفة داخل السجون العراقية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/87952" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87951">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
🇺🇸
‏ترامب يهدد بقصف سلطنة عُمان إذا وقفت في طريق الولايات المتحدة</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/87951" target="_blank">📅 14:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87950">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#ترفيهي  ترامب يزعم: لدينا قناة اتصال سرية مع مسؤولين في الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/87950" target="_blank">📅 14:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87949">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#ترفيهي
ترامب يزعم:
لدينا قناة اتصال سرية مع مسؤولين في الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/87949" target="_blank">📅 14:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87947">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObUR2kPpFCDyKPVpoJf7DnyiWqz1vT8MtGRApOeH6cPHTYcn8P5scoAEfUtZZYBZiPqfKA6PhauQ72EzccUZosFwydsFrAhX88ez_huH-yznSPAban7uHXuel4aokVr4yRCmYjNV0IQmRsM3hGpwGj1PS2ahCKCOWAnZnu6HoT_Y6Iy2ewyKJDC6HWWJ9ca7FMoEh_O5V-E1u4QWHq20sn_OZY1ZLMhFoPBaywVDHb0Vm00lpNuIEq75aKeoJPuaSSaz_D020bM232Sxv1NVoiMHb6xmoPewVyMFD2QYh6zGA9C0SHXXQctF26qHlG5ZmGbGEkSPs1l4e_MJdMQpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أُذِنَ لِلَّذِينَ يُقَاتَلُونَ بِأَنَّهُمْ ظُلِمُوا وَإِنَّ اللَّهَ عَلَى نَصْرِهِمْ لَقَدِيرٌ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/87947" target="_blank">📅 14:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87946">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اعلام النظام السعودي:
الموافقة على تمديد فترة الـ60 يوما بين إيران وأميركا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87946" target="_blank">📅 14:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87945">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b2e069ba.mp4?token=NeFNDbUMLHZQDlLoCrWV4Pt-zcowFp9LnH_0N25YAuQLU-aX5_7XXF9Xs24Z4tiTv6Isep9qQU72hw41OsY_iARa8DIrUcP_YkAb2QTu6I0p3_IhqUwz00CgwcAMGwAPX9YC7EWv9C23drHfp6wyogteJHU8qMskNBx8c-CZ4Gs54MFv5iWRN7ApCYybA_lEE357Cu52hUFHLLYx2jJpPuoXw9UIt3b-VvGcrY8esbyR0Z-L5STgfmOeYaMXz3fQHyJBFfiL0CyrHLCcI0-Sp_3ZfZ7kaylZFOzQUvZsf0bk9qPDm3wb9a6F0Rz2kmv1VudMesFe04-ZYIi8Wg_Dxq89Y2OOgyGmebX__e3im_U5RpiwWPZbGMq4rhqlHxUZokq__jV4UMGpz9Ug-i9G7uUCfFHW7bhie9EyQ2QKtua-AFAYFDsAmtOt7OpODSOqZ9031sNczGDDa5YtRMIbTeegShMuuF5hc-K8YSLr9_5ECPE7O1iE3RW_w2aGcQ3HhpI3YUfwQkDBt-eyuBGqW8U5WbWNs6fcXyx6LGuOkSKqGLJujyXUx4NNThUPl9Lr1GyJGAJxSroUOyUefLOZvAGu7rVaKHjvfg5Dey2nwo-xuYYndbxF68Zmzw9UQk3PfzeFVugyLDeR24jTrPzbGOTplVgebY0oqBfOeYQTQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b2e069ba.mp4?token=NeFNDbUMLHZQDlLoCrWV4Pt-zcowFp9LnH_0N25YAuQLU-aX5_7XXF9Xs24Z4tiTv6Isep9qQU72hw41OsY_iARa8DIrUcP_YkAb2QTu6I0p3_IhqUwz00CgwcAMGwAPX9YC7EWv9C23drHfp6wyogteJHU8qMskNBx8c-CZ4Gs54MFv5iWRN7ApCYybA_lEE357Cu52hUFHLLYx2jJpPuoXw9UIt3b-VvGcrY8esbyR0Z-L5STgfmOeYaMXz3fQHyJBFfiL0CyrHLCcI0-Sp_3ZfZ7kaylZFOzQUvZsf0bk9qPDm3wb9a6F0Rz2kmv1VudMesFe04-ZYIi8Wg_Dxq89Y2OOgyGmebX__e3im_U5RpiwWPZbGMq4rhqlHxUZokq__jV4UMGpz9Ug-i9G7uUCfFHW7bhie9EyQ2QKtua-AFAYFDsAmtOt7OpODSOqZ9031sNczGDDa5YtRMIbTeegShMuuF5hc-K8YSLr9_5ECPE7O1iE3RW_w2aGcQ3HhpI3YUfwQkDBt-eyuBGqW8U5WbWNs6fcXyx6LGuOkSKqGLJujyXUx4NNThUPl9Lr1GyJGAJxSroUOyUefLOZvAGu7rVaKHjvfg5Dey2nwo-xuYYndbxF68Zmzw9UQk3PfzeFVugyLDeR24jTrPzbGOTplVgebY0oqBfOeYQTQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تباينت حركة الملاحة البحرية الأسبوع الماضي، إذ تراجعت عمليات العبور عبر مضيق هرمز 19.5% إلى 95 عملية مقابل 118، مع انخفاضها من 19 عملية في 11 أغسطس إلى ثلاث فقط في 16 أغسطس. في المقابل، ارتفعت عمليات العبور عبر باب المندب 6.7% إلى 254 عملية مقابل 238، مع دخول 150 سفينة البحر الأحمر وخروج 104 سفن</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/87945" target="_blank">📅 13:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87944">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز المخا بعد هجوم باليستي ومسير لانصار الله على مرتزقة السعودية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/87944" target="_blank">📅 13:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87943">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجارات تهز المخا بعد هجوم باليستي ومسير لانصار الله على مرتزقة السعودية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87943" target="_blank">📅 13:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87942">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
نائب القائد العام للحرس الثوري:
في الحرب الأخيرة، تم إسقاط أكثر من 200 طائرة عسكرية (بدون طيار ومقاتلة) تابعة للعدو.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/87942" target="_blank">📅 13:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87941">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
إنفجار لغم غربي محافظة البصرة جنوبي العراق، أدى إلى إرتقاء شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87941" target="_blank">📅 13:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87940">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
🇮🇶
نادي إستقلال الإيراني يعلن عن إختياره محافظة البصرة العراقية لإستضافة مباريات دوري أبطال آسيا النخبة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87940" target="_blank">📅 12:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87939">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
هجوم صاروخي لأنصار الله على سفن معادية في باب المندب.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87939" target="_blank">📅 11:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87938">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية تصدر قرار منع ظهور إعلامي بحق أحمد الشريفي ومشعان الجبوري.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87938" target="_blank">📅 11:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87937">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هجمات تطال مقر جهاز البارستن في أربيل</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87937" target="_blank">📅 11:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87936">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هجمات تطال مقر جهاز البارستن في أربيل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87936" target="_blank">📅 11:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87933">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6708faef.mp4?token=YaBNMeQfG_lYCthTb97xu83S3KSAFsd0yZri9aXG4cAOVWrMdMaz7HxNuIU2Klg7cVIYsgyn3vJGEnswgue8PMi887D6KCXhjO-qxarzpld-xRXrc89iwvi883UOKhZHF_p90fHHjtYWYH9qHD3Fj50hO6DzTCnmWIVD9VlBuKbvzEA7ZtaflrtyuxMfK0E1sELXS-FYsimDxzxhoCiZxrBlk2bV2on-sF2qJeKmmaEbo6UL0xQzOArzkkFf7TZxxZYT6y9h0HbxPl6TAiD_rrkoLuy_vJbjgdt96ogHqiL25VWrHl5ItV8hENSy5PXR7NQq5dsj9AbxR4lYhMOwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6708faef.mp4?token=YaBNMeQfG_lYCthTb97xu83S3KSAFsd0yZri9aXG4cAOVWrMdMaz7HxNuIU2Klg7cVIYsgyn3vJGEnswgue8PMi887D6KCXhjO-qxarzpld-xRXrc89iwvi883UOKhZHF_p90fHHjtYWYH9qHD3Fj50hO6DzTCnmWIVD9VlBuKbvzEA7ZtaflrtyuxMfK0E1sELXS-FYsimDxzxhoCiZxrBlk2bV2on-sF2qJeKmmaEbo6UL0xQzOArzkkFf7TZxxZYT6y9h0HbxPl6TAiD_rrkoLuy_vJbjgdt96ogHqiL25VWrHl5ItV8hENSy5PXR7NQq5dsj9AbxR4lYhMOwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إنفجار وإحتراق حافلة تقل ركاب صهاينة بالقرب من القدس المحتلة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87933" target="_blank">📅 11:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87932">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  مضيق هرمز سيُعاد فتحه عندما تلتزم الولايات المتحدة بالتزاماتها في اتفاقية إسلام آباد.   ما يطرح بشأن ممر مائي جديد مع عمان يعود إلى فترة ما بعد انتهاء الحرب بشكل نهائي.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/87932" target="_blank">📅 11:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87931">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b86b7421ae.mp4?token=KjEZycMSEGl2qqjNiOU-SkKcDhm4AthouLgrBIAhJ1u67lkhNqG-AOEiuhkwCOtoTNe7Gl24UkpDI9h1ZNVWzdhGE2-0HoPlDPiOtA2NfLfzikL20eAEoDlttfOjrmlhkU8Im6GVZlfI-wybgitlRxUQsrVN90r1LTHzqLxrrVjiPKG9aBeMqO59yj4IbSLwBv9bXw2_RD6R_D2hAmyTMiGOkVffYKQd1xXblvXURdX7B_MccYV4TsZ0qzjMICa1wyC8UihZ5OYADCWrQcVoUFP-CVtwOCBq2B1TseI1BimPytWaZ273Wb-klFtTcXoLXcEr7HHnOAgu51KyCWGARYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b86b7421ae.mp4?token=KjEZycMSEGl2qqjNiOU-SkKcDhm4AthouLgrBIAhJ1u67lkhNqG-AOEiuhkwCOtoTNe7Gl24UkpDI9h1ZNVWzdhGE2-0HoPlDPiOtA2NfLfzikL20eAEoDlttfOjrmlhkU8Im6GVZlfI-wybgitlRxUQsrVN90r1LTHzqLxrrVjiPKG9aBeMqO59yj4IbSLwBv9bXw2_RD6R_D2hAmyTMiGOkVffYKQd1xXblvXURdX7B_MccYV4TsZ0qzjMICa1wyC8UihZ5OYADCWrQcVoUFP-CVtwOCBq2B1TseI1BimPytWaZ273Wb-klFtTcXoLXcEr7HHnOAgu51KyCWGARYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تظاهرة حاشدة للخريجين القدامى في منطقة العلاوي بالعاصمة العراقية بغداد للمطالبة بالتعيين.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87931" target="_blank">📅 10:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87930">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
هجوم صاروخي لأنصار الله على سفن معادية في باب المندب.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87930" target="_blank">📅 10:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87929">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
مضيق هرمز سيُعاد فتحه عندما تلتزم الولايات المتحدة بالتزاماتها في اتفاقية إسلام آباد.
ما يطرح بشأن ممر مائي جديد مع عمان يعود إلى فترة ما بعد انتهاء الحرب بشكل نهائي.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87929" target="_blank">📅 10:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87928">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
تعطيل الدوام الرسمي في الوزارات والمؤسسات الحكومية كافة يوم الثلاثاء الموافق 25 آب 2026، بمناسبة ذكرى المولد النبوي الشريف (12 ربيع الأول).</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87928" target="_blank">📅 09:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87927">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران:
أشياء جيدة ستحدث قريبًا جدًا. بعضها قد حدث بالفعل.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87927" target="_blank">📅 09:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87926">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-XyTTx8eBivu745KGGhit6Tl6uoI8rAvzL3Fco26UNLDUxsDBOM6L4U8vrv5lp1Ut_4Ft_09XI6Z_znoVXNLxEZ_Ab1Tc4JU2IVh3VmKuejtU2kDEVsdOWWKrJ1n2d0by_HFhkDuYL4_k7lqNK1U_CFfM3MXu8GK1eu7xOWmlYFLUQVvmn5yr1oNivvJX483lXJMPfPlwiqVhf3UO3S2rCpzop2tRnZ9Hsjuuu6DsEA0hGm6REq7rkeb2Y9GagleEuYbn9q5JfWxUi3Vejds3Xhl-LY96L8dpvNoVd6yTFyTjuB0vipnlE4Je2VL4sEuCY6LqSDHhpyaTI2J07GrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
اسعار النفط تشتعل مجددا وسط التوترات بمنطقة الشرق الأوسط وقرب انتهاء الهدنة بين ايران وأمريكا .</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87926" target="_blank">📅 02:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87925">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2bd5f6ffe.mp4?token=EYvU0pZLBIyzjk0nA9smJ2orBGrKQhPmziJMsGWB-AcMxoXoHYKexoThE6INiVqqFj895_ecqZRRWyMlPfxSjXykFwIKtJ6BKUBWpRlc0uB7b7mx3I9LQXbJRc4k1P7T_b86T69Libr9XnSz3FzQXTobf3wVOE3Le3V5YVn-3WbRMXCVdnqU42CpMoQAPXZLA2R6c48fPQARSPgd-UdfXiSLbK4eCcwXVuLmBHmVyxdEYqP6SPowdO1A8_TceCp-UZFBhQyf8z5x60UJM7zJ9oQo7rkyreeh9qf8sU1kloUju3hWVmCToCoQPqLSU7OZOR4LzmiJDImOuaZdNtFLXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2bd5f6ffe.mp4?token=EYvU0pZLBIyzjk0nA9smJ2orBGrKQhPmziJMsGWB-AcMxoXoHYKexoThE6INiVqqFj895_ecqZRRWyMlPfxSjXykFwIKtJ6BKUBWpRlc0uB7b7mx3I9LQXbJRc4k1P7T_b86T69Libr9XnSz3FzQXTobf3wVOE3Le3V5YVn-3WbRMXCVdnqU42CpMoQAPXZLA2R6c48fPQARSPgd-UdfXiSLbK4eCcwXVuLmBHmVyxdEYqP6SPowdO1A8_TceCp-UZFBhQyf8z5x60UJM7zJ9oQo7rkyreeh9qf8sU1kloUju3hWVmCToCoQPqLSU7OZOR4LzmiJDImOuaZdNtFLXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نائب قائد القيادة الشمالية الأمريكية:
الولايات المتحدة "غير مستعدة" للدفاع ضد هجوم باستخدام أسراب الطائرات بدون طيار على الأراضي الأمريكية؛ "ليس لدينا أجهزة الاستشعار [أو] الأدوات اللازمة لمواجهة هذه المشكلة."</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/87925" target="_blank">📅 01:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87924">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1jGRDzNCXb6Eai0A0bQl0niGZDk-DnMxwSxzJ44JGwDNKKPBcdwYOFt__tpMgxbN5FBtbRZLMxYR-ZfICBtcoLBGP6CmsTzy29gV--38nBi0S8xOKE5HbQG1my8IKieBLFlc1JbkOkHEj7Wk7YD6M4T3-s6FLtsREpN6xTTK1MAGkiOEDJCVdC_Oqf2HPW8ezdc6X6IVpW9XhxuVYHuNx6qblWbg0yjfROBraiCwf53cHjP81DPrDC8yMQdbPIecOh2UhMlfCvdg6UPHIrWaVfzpAW5Vm4OmyvGEDACKl6KnQzAoM3H5RWjH8MXolQRrOhYj2EcjNSPbea4Qq_-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
انطلاقًا من علاقتي الممتازة مع كيم جونغ أون، زعيم كوريا الشمالية، لا يسرني أن الولايات المتحدة وافقت منذ زمن طويل على المشاركة في مناورات عسكرية مشتركة مع كوريا الجنوبية. هذه المناورات ليست مكلفة فحسب، حيث تتحمل الولايات المتحدة الأمريكية معظم تكاليفها (كالعادة!)، بل إنها تبعث برسالة غير لائقة وعدائية تجاه دولة لطالما كانت، طوال فترة رئاسة دونالد جيه. ترامب، غير مُهددة ومُحترمة. لذلك، ونظرًا لتأخر إلغاء هذه المناورات، فقد أصدرتُ تعليماتي لوزير الحرب، بيت هيغسيث، بتقليصها بشكل كبير! وفي سياق منفصل نوعًا ما (?) ، سألتُ مؤخرًا رئيس كوريا الجنوبية عما إذا كانوا يرغبون في الانضمام إلينا في نزع السلاح النووي من الجمهورية الإسلامية الإيرانية، فكان ردهم: "لا، شكرًا!". شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87924" target="_blank">📅 00:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87923">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTEb1SGPDHmbKiwC0NLmdEhsNx6Dl6W398TnYVz2XOcG1_nrjCE9KMqjNQWf-EdLwUuPjjBFPoVeRhhJfKSLnxqHf4T6czK3askNNN4EkHEGLS3g1eeXlN-Dd4NM8CHMv_vgK8Y0FvlzJvu8hqMSSUGBN7Dc9SO9crnFj8dyDIFbZ1mxg2_1cq36FIUh-lZyx04h9tHhOSZ66EgwsgoXtxluCxk6l1JYyl5fW7Ej_R02A69QDsvrUghYIPsV0WfjW2y7DGtkxNldy-1s8ls02tmmRy5gfpMuAOcVXBuMgChrQE-fKoGpVaQ61IZxwOjwzLlbRTnww69pqNLCv36gEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
يسعدني جدًا أن أرى أن المملكة العربية السعودية وتركيا وباكستان قد وقعت مؤخرًا، وأخيرًا، على اتفاقية الدفاع المشترك في مكة.
هذا يدل على تكاتف منطقة الشرق الأوسط، وكيف ستتمكن الدول أخيرًا من الدفاع عن نفسها بطريقة أكثر فعالية.
تهانينا للقادة العظماء في الدول الثلاث المذكورة. هذه خطوة أولى كبيرة وجريئة ومهمة - يا له من إنجاز!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87923" target="_blank">📅 00:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87922">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇱
🇱🇧
غارات صهيونية على جنوب لبنان.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87922" target="_blank">📅 00:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87920">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx8bofuAMmv_CNHnL0kfEY0hKDNypvMWxgqOw2UG-IWkO7tKUYKOkMOwmm3ilOo742mB8KxIKbfjG6WgYHojx65h6gber6mwH-Wz1BnXHNCOBHoR3b0OF0PLzr3xWsTNws-ROpxaAdiOTurkPX1BDc69D5PQDbTvMWQWsNihB88qaw4A0msLX3lbGbcvW_uTGpySKs0CxwE3YfDMObN-kY-78iS-DwW5I-h1aAquy5qU7WgSbFBd-z_-EyPTe2oHaUUf6Ou-fmZWgqN8ZNK5zUR_6lqirOrLIRBkqge_DgRP7glKaJOK7lnH8T8xVdxbBg_R2u44KHB02Vn1tV6bdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇮🇶
🇺🇸
فضيحة عنوانها منظمات المجتمع المدني المدعومة من السفارة الأمريكية في بغداد USAID    تداول ناشطون على مواقع التواصل الاجتماعي مقاطع فديو لناشطة معارضة لقانون الزواج الجعفري المقر موخراً بمظاهرة قرب المنطقة الخضراء وسط العاصمة بغداد ادعت انها شيعية وان…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87920" target="_blank">📅 00:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87919">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lirQxLXixPlV8nPDKi-5n5J97d_YYSSyL3BjYCLHPXebUdbuV0-Jjq3VGDvvqQNV2rJsYJjnRsRCAyCUqQSylaTHvSRTh9FPJ-9ADTceYPAYKM8Mh2BhcjQVDcDfdRAr2sTqeUcqcOn-4wft-7sFB2KTym024_3FLrY6Tjw9QTNyMePhWbnmAMg6woyQVCvryBe6Uql-ncdpupkZoDbQ7cXJwOJ07sWyGwa86CXPex6YGgBzRPBvPEAf7wzRQ4YPLIpXEru7ie3Ss9OAErNeB_6vbFwzF5bd64hRVwt4aHNIZQl69feYwmvaOvdgUX4xN_AiN9T7eSHGaiLouRuKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب مقداد الخفاجي لمنى سامي: «أني آخذج لجرف النصر وأنصوّر حلقة هناك».</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87919" target="_blank">📅 00:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87918">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc75c7dd8.mp4?token=vn7hKqL-NBGVX1vlI6U6Ciou5hhFkJEWC8O2W3sj7OAi4ctPxeg3QpeEfk1lgvTu6IZowE429g5BER5hXkH8dhzGCdHZj65aTpYMk2kszYOP_xqk6r6QhUBbNwS9ZKxrd19rqys5Myk-6AXJ69apaWzV9gRasEnGQZJ2Wknc9ZXdAZUZgKKZ5TkwAl8TBt5Vrj6Fi7HoBIbwR3gAiZBats-QNLxaSSiTT8z-dL1tOD_Bw-uXoZm8SQXkWZpefr6r2V9-ycfJdzyu8F4PBze5imf36yyecAuFMbgHoRD0pY_shyFIoVDAS-QlTsMvro-8JMtO1RMctu92qJ8UjeH5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc75c7dd8.mp4?token=vn7hKqL-NBGVX1vlI6U6Ciou5hhFkJEWC8O2W3sj7OAi4ctPxeg3QpeEfk1lgvTu6IZowE429g5BER5hXkH8dhzGCdHZj65aTpYMk2kszYOP_xqk6r6QhUBbNwS9ZKxrd19rqys5Myk-6AXJ69apaWzV9gRasEnGQZJ2Wknc9ZXdAZUZgKKZ5TkwAl8TBt5Vrj6Fi7HoBIbwR3gAiZBats-QNLxaSSiTT8z-dL1tOD_Bw-uXoZm8SQXkWZpefr6r2V9-ycfJdzyu8F4PBze5imf36yyecAuFMbgHoRD0pY_shyFIoVDAS-QlTsMvro-8JMtO1RMctu92qJ8UjeH5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
النائب مقداد الخفاجي لمنى سامي:
«أني آخذج لجرف النصر وأنصوّر حلقة هناك».</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87918" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87917">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279f369819.mp4?token=pxpyJ5z1BtBxRmReqlHA9BAuide6b6KMIHz8b6Ae820ou7Us4E2rsF8rFvLJu24-fZp4BkxY6nFjB7fDyZR5a5slVS9vc1KB38t31NZhAogQeldO4NqYoxjwkWP2kkFndYmOlnTrZKmd8JvLD9xe8-HV1qVsFSRVk6rQwkKUP7srpfFgnoKpDDl7wgXVQuSalXnwSG_FzKbrYt9e2PkE75lw42tjBmU2xectq01ryj5D4fbBWYbM-GLlaGLa3subTxpv4OkcBIsz3RQKqlYBtTEZxUzF_3slKvzDX74q8y5AbKWYqzmMd0B1IHlT7mVhjjdbT-wySzUER9JCLctU44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279f369819.mp4?token=pxpyJ5z1BtBxRmReqlHA9BAuide6b6KMIHz8b6Ae820ou7Us4E2rsF8rFvLJu24-fZp4BkxY6nFjB7fDyZR5a5slVS9vc1KB38t31NZhAogQeldO4NqYoxjwkWP2kkFndYmOlnTrZKmd8JvLD9xe8-HV1qVsFSRVk6rQwkKUP7srpfFgnoKpDDl7wgXVQuSalXnwSG_FzKbrYt9e2PkE75lw42tjBmU2xectq01ryj5D4fbBWYbM-GLlaGLa3subTxpv4OkcBIsz3RQKqlYBtTEZxUzF_3slKvzDX74q8y5AbKWYqzmMd0B1IHlT7mVhjjdbT-wySzUER9JCLctU44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
اردوغان يعلق بخصوص اتفاق مكة:
في حال حدوث أي مشكلة أو هجوم، ستكون هذه الدول الثلاث قادرة على اتخاذ الخطوات اللازمة معًا.
‏قد يكون ذلك ضد تركيا، أو ضد المملكة العربية السعودية، أو ضد باكستان.
‏أياً كانت الدولة المستهدفة، إذا وقع هجوم ضد أي من هذه الدول الثلاث، فبما أن هناك اتفاقية دفاع مشترك، ستكون الدول الثلاث قادرة على الدفاع عن بعضها البعض ضد أي نوع من الهجمات.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87917" target="_blank">📅 23:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87916">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-3v-Akf27rH0hYmJTeb97583DwkQHu1nMuiNzrwcM2MDRiFwWqNG75AUc9aUap1x2Q8BN4yKRHyHob2EZv3Gl-9AtVX6qjZqL9V4Z2wz1uQuEXRyEVtVG5WVtCoNMBN7_XfGxvSfBA4_37KXccruYT7o6YhLuVYWziFGiPC2VT3OJc6n0Jq4wl3TZzkBCtlWFawywuCw0lP9g34jo-t93vuU1dB5SwL3Lw8ak6dwfE90qxiXzZNQsMRqw_URVIBZVxSuGnGyqfytWLn5qpBjvv1f0cSYNvfdLC4yIgfstqColovW1a15q_hZKk3co2rv6pHnzMOUOfDCVSreFPpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يختلف على قناة فوكس نيوز التي تعتبر اكبر واجهة إعلامية مقربة من حزبه الجمهوري …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87916" target="_blank">📅 23:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87915">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_l-mjjjpWJZvbXIVmvk17W5e6j0dBrbLJKaqf9xaTHj4r3zLsIfw4jc3pGgc_JhlZc0PcPlNCQBhIZRY31hJAgXS8IA9LgZgTwZJJYbki1ebe6AIG6rj09z9pJp08CTLfomtsHZLla2GewAwgeLzRttnz7009pNbPzxeOrARhIV_i9KB7eq6JQFhL4M61LLriJ_8SfA3EJAiBcCm81aM9OUrq-ETE_BW4b5iySJMuvapNcYp3q2cotbV3W_YyZfKhQzDhQhjrNcY83wBK9j98AMziWO0rvlCqEPXg_5Vl6g-WqXsr2oHy2JoJC7_4YALYNWhA8U6ZdJ9k0k29guEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
إصابة 3 من عناصر الشرطة المحلية كحصيلة أولية، إثر اشتباكات بالحجارة في محافظة ميسان بعد قيام مجموعة من المتظاهرين بإحراق الإطارات احتجاجًا على واقع الخدمات في المحافظة جنوبي العراق.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87915" target="_blank">📅 23:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87914">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
🔻
نشرت مواقع مقربة من قوات الحشد الشعبي العراقية مقطع فديو دعائي جديد يتضمن ظهور عدد من المقاتلين وهم يحملون بنادق روسية من طراز كلاشينكوف 104 AK والتي يعتقد انها هندسة عكسية من هيئة التصنيع الحربي العراقي مع راس مرتبط بكابح الفوهة او ما يعرف بالإنكليزية Muzzle brake ؛ المقاتلين ظهروا بجانب معدات رؤية ليلية متطورة و عجلة مدرعة تبدو انها الأبهر العراقية الصنع و المقاومة للعتاد الخفيف والمتوسط والإلغام الأرضية التي لا تتجاوز زنة ٤ كغم ..</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87914" target="_blank">📅 23:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87913">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363e3b5820.mp4?token=dMOoD123aZFw9AlFXymmA0XvF6JnoLlGubv9wCYc0327LLVkwWi7hdgwkyEGWdUXtlpiQuY1rWV9plRTSQxa8i9-i_4TsBK94C44Cp9AVk_0WIadoU1A0sOpaAoS0gq6UXwyMhVQDiMRxDfxoEhJ3snQOvqdP-PKpM8gUqpQzDDx5HRDX8VzXPfohdQTz-IylfyuN9rrHBLMErbthAdFKc_AEWvHsYa-af4Fdy75zsCSTt88K3pdVjPZC_FcaN_gVROyxs-N9rGECE6P9YwYUMIXMCmPyg4t63iWukSQlACkFy65mzEYX0IJdufrqNQo0Q9IKEBf6x9hYkh9qrG7OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363e3b5820.mp4?token=dMOoD123aZFw9AlFXymmA0XvF6JnoLlGubv9wCYc0327LLVkwWi7hdgwkyEGWdUXtlpiQuY1rWV9plRTSQxa8i9-i_4TsBK94C44Cp9AVk_0WIadoU1A0sOpaAoS0gq6UXwyMhVQDiMRxDfxoEhJ3snQOvqdP-PKpM8gUqpQzDDx5HRDX8VzXPfohdQTz-IylfyuN9rrHBLMErbthAdFKc_AEWvHsYa-af4Fdy75zsCSTt88K3pdVjPZC_FcaN_gVROyxs-N9rGECE6P9YwYUMIXMCmPyg4t63iWukSQlACkFy65mzEYX0IJdufrqNQo0Q9IKEBf6x9hYkh9qrG7OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إصابة 3 من عناصر الشرطة المحلية كحصيلة أولية،
إثر اشتباكات بالحجارة في محافظة ميسان بعد قيام مجموعة من المتظاهرين بإحراق الإطارات احتجاجًا على واقع الخدمات في المحافظة جنوبي العراق.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87913" target="_blank">📅 23:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87912">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇹🇷
الاعلام التركي:
تستعد إسرائيل لسيناريوهات قد تدفعها إلى اتخاذ إجراء عسكري ضد إيران بشكل منفرد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87912" target="_blank">📅 23:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87911">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec13b8e67.mp4?token=jo85PzERHTY9D2ae3-g0lkEHzvKtYBzudyN-49o0mmKaafBY48DgkgcibCZbNt9HCB6e47-mgsKYgKLvNUd-2GXwVZOgR-p7SHFAmzx8mRueCIRDFq6iN41Jnatmaix39YEdRJ2Qd0SPbPpxxvI0hD0LLvJhFfRQcx5zQ6bsBOHHJYCTsUHk74ubbRhtVnQBfkX__pojzWXfWWbEVNWF03AkfS5FS96g-15bU4slzSZmzdum5PoftmnvOqBBHcdGO3wKvvA_FSbuLqh6xS77r-UwRpVTXKGuy-odeJG3pblbyQ4lK5nDVIp7Y-IKlLs95hbMbv1raXWCsn_Vj5l4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec13b8e67.mp4?token=jo85PzERHTY9D2ae3-g0lkEHzvKtYBzudyN-49o0mmKaafBY48DgkgcibCZbNt9HCB6e47-mgsKYgKLvNUd-2GXwVZOgR-p7SHFAmzx8mRueCIRDFq6iN41Jnatmaix39YEdRJ2Qd0SPbPpxxvI0hD0LLvJhFfRQcx5zQ6bsBOHHJYCTsUHk74ubbRhtVnQBfkX__pojzWXfWWbEVNWF03AkfS5FS96g-15bU4slzSZmzdum5PoftmnvOqBBHcdGO3wKvvA_FSbuLqh6xS77r-UwRpVTXKGuy-odeJG3pblbyQ4lK5nDVIp7Y-IKlLs95hbMbv1raXWCsn_Vj5l4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصادر لنايا || بالفيديو
🇮🇶
بعد استحداث قيادة عمليات البادية،
جرى استقدام قيادة عمليات شرق صلاح الدين إلى محافظة المثنى ويُذكر أن محافظة صلاح الدين كانت إحدى معاقل عصابات داعش الإرهابية ولا تزال هناك جيوب للتنظيم في صحراء العيث ومنطقة الزرقاء!!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87911" target="_blank">📅 21:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87910">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPvqTcBn_5Z65M970kDVkD9WPC2U90Z_EIn8Gve7lRcVFpaeCrqdGi5n9j28d0reF2vD935Yg7eL6JuaH1Wn31yzvMTaUM_xvlzKheNTGKsZBfdHscgCXNBK-1Fw0WhRoGwkAk9EJkjOImU42QHiBOqOu0sE0Lh5g7T4hYyh_FZy4GZP4jQxyOo1bFKQC92atoH3-Rw_JWOh67Qp2UvZJxZpsLcnBH1dZtWfXUACybXXy7NVzgXkqNreatTQxMo-zKR5ZQlnvob14TSAfS6Gd-ickMjmf2V7ccf3SRwX_T06VBeDgUtIe5IkR1GukiqCBeO7SjquUtJNnixPnlO-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
حزب الليكود الحزب الذي يقوده نتنياهو يطلق حملته الاعلانية
(يريدون ان يخسر نتنياهو).</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87910" target="_blank">📅 20:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87909">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87909" target="_blank">📅 20:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87908">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇱
اعلام العدو:
بعد 32 عامًا من إصابة والده في منطقة سُجد جنوبي لبنان، أُصيب الجندي (أ) بجروح خطيرة جراء انفجار مُسيّرة مفخخة تابعة لحزب الله في منطقة علي الطاهر، صباح أمس السبت.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87908" target="_blank">📅 19:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87907">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
وزير المالية العراقي:
نتجه نحو إقرار أول موازنة للبرامج والأداء في تاريخه تربط تخصيص الموارد بالنتائج، إغلاق مضيق هرمز ترك آثاراً مباشرة على الاقتصاد العراقي وماضون في تجاوز الظروف الراهنة من خلال تعزيز الإيرادات غير النفطية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87907" target="_blank">📅 18:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87906">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0bac8e80.mp4?token=HWZeR9IQCB6uyrYpWBF-R3B2vKe1Co8F0P9RCGvgxlJt4MJF4NhCcMO6gUWRN36hYrRRoFPL5ywdtVwYrqeOU45uhy05W4CtD_qgResG_W7FHfp-HENKzIXMZw54IZfVnKJMJfs0_-k11AkaChhG_8Yka5PxA5Eg-HXYrnOVOt-UzzxPP5rVYnLYhNrE4mqHiDR1dXnV7Uh9ELNqix8Uhh0Ev_qG44P6bp9k3uglYNjme2OoUgxYSAIlZdISVKqr1eB-KFgpk7sPnhOF4gflocGO8dNAZuGtliBo0JAp7CaK8mP3-JXZvnEooKXOLcxb0hn3Ca3n8m2KlLdZtAPsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0bac8e80.mp4?token=HWZeR9IQCB6uyrYpWBF-R3B2vKe1Co8F0P9RCGvgxlJt4MJF4NhCcMO6gUWRN36hYrRRoFPL5ywdtVwYrqeOU45uhy05W4CtD_qgResG_W7FHfp-HENKzIXMZw54IZfVnKJMJfs0_-k11AkaChhG_8Yka5PxA5Eg-HXYrnOVOt-UzzxPP5rVYnLYhNrE4mqHiDR1dXnV7Uh9ELNqix8Uhh0Ev_qG44P6bp9k3uglYNjme2OoUgxYSAIlZdISVKqr1eB-KFgpk7sPnhOF4gflocGO8dNAZuGtliBo0JAp7CaK8mP3-JXZvnEooKXOLcxb0hn3Ca3n8m2KlLdZtAPsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر ثلاث طائرات فقط تابعة لسلاح الجو الأمريكي للتزود بالوقود جواً منتشرة في قاعدة العديد الجوية في قطر، موزعة عبر المدرج بدلاً من أن تكون متوقفة معاً</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87906" target="_blank">📅 17:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87905">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
النزاهة العراقية:
الحكم بالسجن لمُدَّة سبع سنواتٍ بحق محافظ صلاح الدين سابقاً عمار جبر عن جريمة تضخم الأموال والكسب غير المشروع.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87905" target="_blank">📅 17:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87904">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4niOLCltWtu6ueFoWRZPGytlRFOMZVueUUc2cR347XnIi5M3lLwn8XwN8tBtXEEDVCwU1uFPbbz-8hjmlE0evRQlEDtfUG8D79PFIehw5FPjIiLRPCexemCgABANxjl8q9kP6Oyd4dyBJRYEnVyr5TY_O75USVDdGx9dQoV9Xu55eRiJJHBDdMHWmHFBmOt46irdvRbjozpNOlolR0AZS8FR_2aGTi8jrhv-h9-Xxg3oF64Y6AlHZkHcwyRO7pghxGPoq-ZRd5tvgS5Y7dyLH0OVZt8z5CJZLL18tCMvO0MnI_vjcytByJEWJrM2QqzuWBht-Us3u1reDDtAzcSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجرات تهز السعودية</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87904" target="_blank">📅 16:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87903">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات تهز ابو عريش بالعمق السعودي في جازان   ال سعود ظلمة</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87903" target="_blank">📅 16:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87902">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87902" target="_blank">📅 16:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87901">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87901" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87900">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجرات تهز السعودية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87900" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87899">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87899" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87898" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
قائد الجيش الايراني:
- مضيق هرمز المقدس هبة إلهية للأمة الإيرانية، ولن يعود هذا المضيق إلى سابق عهده.
- من بين إنجازات الرئيس الأمريكي تفعيل مضيق هرمز.
- كنا نعلم بهذا المضيق، ولكن لولا هذه المعركة لما تم تفعيله؛ أي ثمن نتكبده في سبيل ذلك يستحق العناء، وسنحميه بكل قوتنا، امتثالاً لأوامر القائد الأعلى للقوات المسلحة.
- هذا المضيق أحد الشروط الأساسية لإنهاء الحرب بشكل يزيل شبحها عن إيران.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87897" target="_blank">📅 16:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87896">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
🇺🇸
‏طائرة تابعة لعصابات الجيش الأمريكي من طراز P-8 تحلق بالقرب من جزر المالديف على مقربة من ناقلات النفط الإيرانية قبالة سواحل سريلانكا ومن المحتمل أن تقوم العصابات الأمريكية بعملية اقتحام.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87896" target="_blank">📅 14:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87892">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwrpPjj5JWx-iPofAHStZKzMMrOa3Ed5qBaoYyyeCzDV_6Iydb25GsaSYH_QGwjTT1Tof1h3tiBuLZfmULb2rmt4nm2TPt9Iw29rirRLbJMfqUD17k5675TwYooupgrHAWTANk2_BL7YmQiDO3VlcIYEmEqWFquWrzKPNCHahSqTFbfyK98zQAVVxNnUnc0DuFlN1_RuAnUPz2iKg8kxQHBgCvWohqdce3mgCjZKM2DhcLHZ-0Z50CeY4CWbAnfykZTQnx-vJzRtxngrjU66NAfy_MpNDpQac22rhthqlikprha1rk7pe_00KFvXHt2ytOli9Sb2H8ip4BiOiFCLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikgDPxXbu_axz-EWaFRhd4QAqiUgH8hxxoIQVvVCE1hiU1zdtgU1QeptzgAA-BdapMbu48FHrJwJcfMIryet1hlcd9myRpMLAWa7JJyyKRF_qp4wCgn8uXZIhJ9hd4RUTV2PdbSbp4nX5eYdB9P7dV9hlcH2mnmyUzsds0TkIjNDfW2Lr1JmuCWflUXkn4S0tKatqqal0zSPePG31MSlE9iNinn_N08Q2g72IBQKTCHpAkVTyzR8X7STTgGCXTI9ohSWKww0icMp49YY6QgMQmXoisf6YybQ5L5S4yzTMDWd6d4tflPkWKfPWGZQaGY8sCwfcqa-TvtyvEc8Kg6_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YW14IDKhbAEnJ1PfEjSTxYAergI-b_h0aTjYHISGV1kgUsPtXPQErLo-3L183TiMuaJcrJlXW3K4myxbNZuaO5ow5vWf_qsff2U7H3LwCGjB4_eYy8qXWDg0PSTev8kqW2UtgxTqtJv9crwewS8ulqDUxADKXBNUlS41_awBDUXK-1fhwhFCdX0DEfqZ0wfckeXetdt08InVZE09Nz9pzF1era1csZM2tl5ny0hA_j_uLcanepGLWGpPyQPTC7oceDnP_Qy5an9p85eMUHTm5KRoxn2F9REZE3u5r9iHTT9kRgzGokhrsRmRIKYgMWARiLdz-xtTY5zHf7kn9dcwwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWmiYbUoQHHZrAeF8LiMhptRQU178FJBiG2ioVjRRR2kYvqLCIYpyiALmQ_VKsKu3QouV_b7y2Tu5PtYjDzxtQ3s-RQ10D69UPen5lTmqmSjpph3pAA4fjfRZ-gwUTbkavt2gDQ4-9fDV00xcyDofQCpg4PazZP57C7ozwhsisaR0xWQyyXZY6qIT9JYCLRQuTOUB2GR4P8hLvlIlqAGstKRisXu0Ln8U8uxrFx2WSskatAT-_UTCsjROVt4h3oit-EvZo5DTAIEmbvt8SoHjoBhcTghsYdAVOga6qlKKheQ0mT02erPzFg-MEFGmkahcprD7Y5h7x1wMJdTfNwDxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
حريق كبير يلتهم مخيم شاريا للنازحين الايزيديين في محافظة دهوك شمالي العراق</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87892" target="_blank">📅 14:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d572bf9031.mp4?token=iEBO7Et6fhcKCxgpXyUSswp-Z7xp22PIWKxGkrMKSM2MbK6pEImR2uZCIfA6iewZSDM8ofIDcXwa-takMyDDi1GrkzZvSy-tQK25R2YaM_ULihqnBZgn2wqkmUK6rYWvnz8LED59slY1vtbeoTaDXsoRjEGODz3fj_LnPVzYEYkxhDUgL1GCKnm9Nmnfv2FtuEdmyAgWyPVrqm_JAb86GgUjJihkqDpoC_mOsd6k0m9KNHFfR6aFwRtUQuRITTgCvKQrBObsB7eRMoqlinyUiZWZ_g0jTiHa7DOjr12OBe5w36-ghr8WbvIB5q3u7KoEmCYaLQ2wmaooo3rgPnimSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d572bf9031.mp4?token=iEBO7Et6fhcKCxgpXyUSswp-Z7xp22PIWKxGkrMKSM2MbK6pEImR2uZCIfA6iewZSDM8ofIDcXwa-takMyDDi1GrkzZvSy-tQK25R2YaM_ULihqnBZgn2wqkmUK6rYWvnz8LED59slY1vtbeoTaDXsoRjEGODz3fj_LnPVzYEYkxhDUgL1GCKnm9Nmnfv2FtuEdmyAgWyPVrqm_JAb86GgUjJihkqDpoC_mOsd6k0m9KNHFfR6aFwRtUQuRITTgCvKQrBObsB7eRMoqlinyUiZWZ_g0jTiHa7DOjr12OBe5w36-ghr8WbvIB5q3u7KoEmCYaLQ2wmaooo3rgPnimSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جماهير نادي زاخو تنزل العلم العراقي من ملعب مباراتهم أمام نادي غاز الشمال ضمن منافسات الدوري العراقي ومراقبون يتساءلون: أين الذين أخذتهم الغيرة على العلم العراقي خلال زيارة الأربعين مما يتعرض له العلم العراقي داخل إقليم كردستان؟!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87891" target="_blank">📅 14:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
حاكم مدينة مهران الإيرانية:
صوت الانفجار الذي سمع قبل قليل في مهران ناتج عن عمليات تدمير الذخائر المتبقية من الحرب في الأراضي العراقية، ولا يوجد أي حدث أمني.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87890" target="_blank">📅 12:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
القائد العام للجيش الإيراني:
بمشاركة الشعب، إذا تمكن أي جندي إيراني من القبض على أو قتل جندي أمريكي متجاوز، فسوف يحصل على جائزة قدرها 30 ألف دولار من الشعب الإيراني.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87889" target="_blank">📅 12:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87887">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cL21agmxoHP__AapIRJbAG89Slx9jWW1ZzvkAIUo57dgDMHIZRfr06-U0_jUWIdM3RarY9ZrIAFwCpOxOjqUALvP5LkEeKlypkpUVhOY8bmwJ0f-kEeGtwu9oZbycCCQ-1HNv_eHTJ5Wo0IQnhX-HAxe89s-PukITzBg6F5Rndxao5GX3YtcpQJIO5Oyf8s6qJf01XqEqDW9FzCjg8F2MuzQOqVxX5XfDjwHDonzos_CiBn3Yikt32sGCbJ6jFDTNNS1w_sBLhcI0bnGWUhyKcVlj6cfGUWJXp5bzpoyiH2mWvxGxMFc_lNGh3uer0ey4YAdoax9dt7pl5yqytM5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c305e2b0ee.mp4?token=Jq62jjVMocurginNHeKpX8HoybZE0Afb87d8Vk3oHZLF_5M4KxBIX5d7Jyut3-A08dpPOO-Id0ZbnAUFezqAREIWOUAPh_t048Yf6zCTZTuRxsLIqjqeeAsj-tUf7xRWHH_SUOHqckbhAqzmc69esQ3bjNU8JbrFVTOhtRQvJWl-VL1BvGZtKroCu0pM6Bm3pmME3HoaHlXXasvnfRgSWDI5ecj1M80mCLIDKqR3WDZxIeLSaKK9aY-aQ4xaWCj-q4I-U4wKZcc5w78bRh0OahcXef9Y1x88iBT7eh_tgz8IGOv_e5Xsvg2vu2c98R2US9tigkJ0r4lweGe0mp5j2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c305e2b0ee.mp4?token=Jq62jjVMocurginNHeKpX8HoybZE0Afb87d8Vk3oHZLF_5M4KxBIX5d7Jyut3-A08dpPOO-Id0ZbnAUFezqAREIWOUAPh_t048Yf6zCTZTuRxsLIqjqeeAsj-tUf7xRWHH_SUOHqckbhAqzmc69esQ3bjNU8JbrFVTOhtRQvJWl-VL1BvGZtKroCu0pM6Bm3pmME3HoaHlXXasvnfRgSWDI5ecj1M80mCLIDKqR3WDZxIeLSaKK9aY-aQ4xaWCj-q4I-U4wKZcc5w78bRh0OahcXef9Y1x88iBT7eh_tgz8IGOv_e5Xsvg2vu2c98R2US9tigkJ0r4lweGe0mp5j2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إصابات في صفوف المتظاهرين من خريجي المجموعة الطبية جراء إطلاق قنابل صوتية ومسيلة للدوع من قبل القوات الحكومية.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87887" target="_blank">📅 12:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87886">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇷🇺
🇬🇧
ذا صن دي تايمز:
استُخدمت طائرات بدون طيار بريطانية لأول مرة لشن هجمات داخل روسيا.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87886" target="_blank">📅 12:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87885">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
نتائج الحرب مع إيران.. وزارة الطاقة الأمريكية:
تراجع مخزون الاحتياطي النفطي الاستراتيجي إلى أقل من 300 مليون برميل.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87885" target="_blank">📅 11:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87884">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇦
زيلينسكي:
13 منطقة أوكرانية تعرضت للهجوم هذا الأسبوع وأطلق الروس أكثر من 1550 طائرة مسيّرة هجومية ونحو 1560 قنبلة جوية موجهة و62 صاروخًا على مدننا.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87884" target="_blank">📅 11:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87883">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏴
مَرَّ أربعينَ يومًا…
چهل روز گذشت…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87883" target="_blank">📅 10:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87882">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
هيئة أركان القوات المسلحة الإيرانية:
نؤكد أننا لن نتراجع حتى تحقيق الهزيمة الكاملة للأعداء الأمريكيين والصهاينة في المنطقة، وتحقيق الحقوق للشعب الإيراني البطل، وخضوع العدو. ولن نتنازل عن المطالب المشروعة للشعب وتطلعات قائدنا العزيز، في وجه أمريكا المعتدية.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87882" target="_blank">📅 10:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87881">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
‏
الحرس الثوري:
على قطر السماح بتواجد فريق من خبرائنا بدلاء من إنكار قضية احتجاز الطيارين.
‏خبراؤنا ينتظرون دخول قطر منذ عدة أشهر لإجراء تحقيق ميداني بشأن مصير الطيارين.‏
قطر ترفض إدخال لجنة خبراء وتقصي حقائق إيرانية للتحقيق بمصير طيارين إيرانيين.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87881" target="_blank">📅 10:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87880">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇾🇪
🇸🇦
إنفجارات عنيفة في مدينة المخا اليمنية جراء هجوم لأنصار الله على مواقع مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87880" target="_blank">📅 10:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87879">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0696943056.mp4?token=ZxOBK16avrMqh0TY25LD7E0IB6xyo4Kmy5p4DdDXNtfsZP4G2NWUxAd2ZJWh3FH0XFYjkYxGXHLpGSxriWq9FrcdE5jzNYkTQywuFj4cVraZWNnqU2sZ2EDuRFKS8_j8X1iY9GGPEV6aO6OMD3aMp55ITF0Xc4Datj67IsX05cutsWUqMXeBS_At52RHzpq1aDxpDbH8uElaC5ewpiUHm99pg02NS9o2QqkdR5S0am-RKg7q5YJYzDpEpLDBmMW7jwFDMeXZWeDriqG0zr4qC2HNmNkV7VWAFHgQ_iEJ66LBOLUE9ugsa9MjnO4KIAuR-RSjkHhw5gCu7dygLLkbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0696943056.mp4?token=ZxOBK16avrMqh0TY25LD7E0IB6xyo4Kmy5p4DdDXNtfsZP4G2NWUxAd2ZJWh3FH0XFYjkYxGXHLpGSxriWq9FrcdE5jzNYkTQywuFj4cVraZWNnqU2sZ2EDuRFKS8_j8X1iY9GGPEV6aO6OMD3aMp55ITF0Xc4Datj67IsX05cutsWUqMXeBS_At52RHzpq1aDxpDbH8uElaC5ewpiUHm99pg02NS9o2QqkdR5S0am-RKg7q5YJYzDpEpLDBmMW7jwFDMeXZWeDriqG0zr4qC2HNmNkV7VWAFHgQ_iEJ66LBOLUE9ugsa9MjnO4KIAuR-RSjkHhw5gCu7dygLLkbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني   اصوات الانفجارات ناجمة عن استخدام قنابل صوتية من قوات مكافحة الشغب تجاه المتظاهرين السلميين من خريجي المجموعة الطبية المطالبين بالتعين .</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/87879" target="_blank">📅 09:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87878">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/87878" target="_blank">📅 09:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87877">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87877" target="_blank">📅 09:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87876">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87876" target="_blank">📅 09:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87875">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
🏴‍☠️
🇷🇺
بلدية موسكو:
تعرض المدينة لهجوم بـ 600 طائرة مسيرة ليلا وإصابة ثلاثة أشخاص</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87875" target="_blank">📅 07:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29dd6be136.mp4?token=Q1pP11JD8xyA0txGiJcI-9rxWF6ee3-xvfkjCIJrtwmN_4xHNGnsxvnfqvyQJXE7oBYhx_4AvJXgzosBi9V57ykDsHkqwqsNm7hb5SzBRX7MwoXSnduunmWII8UK_Scc3W301Lwl4KKV6tfs8bwt4tKnfHXvReHHf66z4cBT90vktN5QOV6BbPDrDhScs8iRXbHpd-5ohYTC3UDxWKpMeHsKPhIYgFETVVhVmKWOt6fMeK4sQemgdLVm3kyMzsdqz6UChE3IiIXU5SxM9xGhRNPzglP8ZgmEC3SSe5Virffo0j1EcTA-iTrqHS4_wv7BoV9FhCSc5X8D_suvY4wDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29dd6be136.mp4?token=Q1pP11JD8xyA0txGiJcI-9rxWF6ee3-xvfkjCIJrtwmN_4xHNGnsxvnfqvyQJXE7oBYhx_4AvJXgzosBi9V57ykDsHkqwqsNm7hb5SzBRX7MwoXSnduunmWII8UK_Scc3W301Lwl4KKV6tfs8bwt4tKnfHXvReHHf66z4cBT90vktN5QOV6BbPDrDhScs8iRXbHpd-5ohYTC3UDxWKpMeHsKPhIYgFETVVhVmKWOt6fMeK4sQemgdLVm3kyMzsdqz6UChE3IiIXU5SxM9xGhRNPzglP8ZgmEC3SSe5Virffo0j1EcTA-iTrqHS4_wv7BoV9FhCSc5X8D_suvY4wDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇶
🇺🇸
فضيحة عنوانها منظمات المجتمع المدني المدعومة من السفارة الأمريكية في بغداد USAID
تداول ناشطون على مواقع التواصل الاجتماعي مقاطع فديو لناشطة معارضة لقانون الزواج الجعفري المقر موخراً بمظاهرة قرب المنطقة الخضراء وسط العاصمة بغداد ادعت انها شيعية وان القانون جعل الشيعة مضحكة امام العالم لتكشف صفحتها على الفيس بوك و مقاطع فديو سابقة تتحدث بها على انها مصرية ومن السليمانية فمن نصدق الفديو الأول ام الفديو الثاني ؟ فيما تسأل ناشطون عن الدور الحقيقي لجهاز الامن الوطني وجهاز المخابرات العراقي وتفعيل دورهم المطلوب والرادع عن طبيعة هكذا تجمعات وشخصيات ذات هويات متعددة !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/87873" target="_blank">📅 06:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9h-uFnJ_N5kitMR0DaqK67uNvB3cGFA239Lg2iU7scRnnUMd_3Ss-F_d61tCEUPA8jJ4jt7x99HcjEZAn8Qmpsw70VpsJbuYfG-D-zqZAcgNy_PTcBg1YjczUURh5ChjgJ45jc2FtgfRiJ2CHy7F_AreqL99lhf_ehpzaGrL8FaJVIR8IAB9nPVMZN3u-7bybJqCnFj8CCv8HDXeyiZCBl79mDH11UGY72WbuyK_CwMWmprS3MssQ6D1rIlcoFVspe_-ABJdxDLytnIu1nsyM46ZdU0zRxYBCvOEI2juH4ilo7mwSJJEuvk3mooAA5lxaju2URj7jRflpdKrombuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إنّ من أوضح أوجه السيادة المنقوصة للعراق هو هيمنة امريكا عليه اقتصاديًا واحتلالها وسيطرتها على امواله حرفيًا وتحكمها بثرواته كُليًّا.
فهل يرتضي الأحرار للعراق العزيز أن يتعامل مع ثروته وكأنها منحةٌ تُسلَّم له، لا حقٌّ سياديٌّ أصيلٌ لشعبه؟
وهل نطلب كثيرًا إذا أردنا التحرر من الهيمنة المالية والاقتصادية الأمريكية، وتنويع أسواق التصدير وشبكة العلاقات المصرفية، وبناء اقتصادٍ يملك قراره وثروته ومسارات تجارته؟
فالسيادة لا تكتمل بالسيطرة على الأرض وحدها، بل بامتلاك القرار السياسي والاقتصادي والمالي بعيدًا عن هيمنة ايِّ قوةٍ خارجية.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/87872" target="_blank">📅 01:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87871">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq8j2QnGg05plNSeD-hDptIWF2OA9nqdxH2Xh63YBZZoxT8DtqgOpgJE1oepGTwCU66kJXAwtNVR99oWVnUERC7QYUYaaW9fza7qrEq4_aRWm-q0fXahgeKU5aMH2qnQhtUl68DyS9jrdblbkNoXjiXYTH-XiGemuF2Fp31WIWfyee7nVZgi95NP_ZDUOv-FLt6EJ6_QOwOqAWM4XiALGyeVd2dm5MB3ud-gynMZEUYCLJushdpJhsHZAEdrPbUZKg2doecde_QAV7kPnwSdvhgxqtZFgq2C_sT0fQe4T5M_DOAecJoyUS3ulgwtJmXDJFC_E95bRhogknCGtyVb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
سنتنصر.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/87871" target="_blank">📅 00:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb4c61f98.mp4?token=WZ1DvULYx_3v4FPAq41bFBvY4qcm6kNZTkTgMpsqP0IIscYhs0TFN4-vAzU9Ft_M8uGwsmBUR82pHqAmCjKTkitwVt8W2TFfWJQhqN8CrAWQ1ptlgS5-KJLjxqJ6cUPY2FHEGL22VSDDXuKnuofRfFibpRJ6-w_zjrikMbOH3Mhj1ZhJCGnlgEkTt0KTc1Nme8pzLDcnfT9i8i0ejbbhgcJRBLMw9odfPVBiBOicRewGKhQ3ktMa-86dYRjz3BuoLG6G25avU-gTBK1HuiQQ9uBxDtWFhVO0oLMeokni7R02u_h2hfqDMHHbllFDw4aI-3t4TJ26-2T6H3XtuHT_6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb4c61f98.mp4?token=WZ1DvULYx_3v4FPAq41bFBvY4qcm6kNZTkTgMpsqP0IIscYhs0TFN4-vAzU9Ft_M8uGwsmBUR82pHqAmCjKTkitwVt8W2TFfWJQhqN8CrAWQ1ptlgS5-KJLjxqJ6cUPY2FHEGL22VSDDXuKnuofRfFibpRJ6-w_zjrikMbOH3Mhj1ZhJCGnlgEkTt0KTc1Nme8pzLDcnfT9i8i0ejbbhgcJRBLMw9odfPVBiBOicRewGKhQ3ktMa-86dYRjz3BuoLG6G25avU-gTBK1HuiQQ9uBxDtWFhVO0oLMeokni7R02u_h2hfqDMHHbllFDw4aI-3t4TJ26-2T6H3XtuHT_6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
انفجار في محطة كهرباء الحرشة في الزاوية بليبيا اثر استهدافه بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/87870" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd380ae70b.mp4?token=d-vtBQ5QQC-k_V65X7P3HqiK--GplgAlXBQAbfafPO18ZLDg2GKFCuyU4JDtRWhHll3GjiyURXIygFMPNA_5K4ZAlNxMgcNSOx-rjJzGjR5CFynZu9xqgiYV7h9ad_rEIshqIbAcJ5c6tXk6sXr2dJvj_2_D1SZzvjfa6oR2Zz3Fbgglo9PB7HFIgamQDgZ6xYeavneXuA5ChqUPXmxkmfJfAxA3H65YRqhwmwLAlv6vGSiqBSe8rf7EqiPYIlSB8W_olkPKyBOA2MYnJOuciG6Kd0iTSsjX8mQe73qr-krPyww7ecPEC3h7OlqLrrYV8qi2j_jFFxrvaYs66Zr4Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd380ae70b.mp4?token=d-vtBQ5QQC-k_V65X7P3HqiK--GplgAlXBQAbfafPO18ZLDg2GKFCuyU4JDtRWhHll3GjiyURXIygFMPNA_5K4ZAlNxMgcNSOx-rjJzGjR5CFynZu9xqgiYV7h9ad_rEIshqIbAcJ5c6tXk6sXr2dJvj_2_D1SZzvjfa6oR2Zz3Fbgglo9PB7HFIgamQDgZ6xYeavneXuA5ChqUPXmxkmfJfAxA3H65YRqhwmwLAlv6vGSiqBSe8rf7EqiPYIlSB8W_olkPKyBOA2MYnJOuciG6Kd0iTSsjX8mQe73qr-krPyww7ecPEC3h7OlqLrrYV8qi2j_jFFxrvaYs66Zr4Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
اكثر من اربع انفجارات سمعت في مدينة مأرب</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/87869" target="_blank">📅 22:40 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
