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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 21:37:21</div>
<hr>

<div class="tg-post" id="msg-85901">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teyvVMaiQumvjwp0AJcG4g52eHtc8xKc-BEG8GeAk9AI4yvdLyNTZ0iYB9pyY6LwORwuIk0TLIe1-BVICetCZJna3kwI6UeItjPNpRTpwcilfKDspUia_flyXitNd2YSRWhRhdDNrhpXjYHGyi6LithixgQbF-UeBJOzqxTQO9fImeVCnO2z2JKt3BFKQugtdv_1tyav2koWPsB4Ic01c11QaKmw7X8jQyD6s38VybrrEMBxAnkKykeiOa31FrsBjkC6JI8-Li7_NfoX14lsCJ_sJpvdyiP0krjt6yRc5LlerQ9MNjS98o_F_hIzt4ZtHz72ddKlqrbBKLKfQPDEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏السفينة التي استهدفها انصار الله في اليمن تم إيقاف تشغيل نظام التعرف الآلي (AIS) الخاص بالناقلة منذ 5 أيام، عندما كانت راسية آخر مرة في ينبع.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/naya_foriraq/85901" target="_blank">📅 21:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85900">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇱🇧
🇮🇱
اعلام العدو:
اطلاق صاروخ اعتراضي من كريات شمونة حول هدف جوي مشبوه انطلق من جنوب لبنان.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/naya_foriraq/85900" target="_blank">📅 21:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85899">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epmliGkCMICWwlknxpiXvV7ydvv9ymE38rsphd4AYQqJxvC-7gZOz6mh19YDlI13HqiOjSZcFmnjdX1OvNTe-P8MiNC7PeXjbRHguyXiRMXkpYuhw4GOtmyHugTdN1Vnt7UKKxOPv6A0iU_yRMZlHCdjyZKTfJheyLKv-a2C00yP6VNrcx5xDEqs33QUX6ps5yrvttojkjS66Qv22NgDcR7YJCJdGHhcCFL41yK0JEFiZTNcPes_ZXipBQnUTDLJY_Glhh-i7GBQCrzfor5BLEEhxcsCfI46FBeAUpEG4ZpNSGO1SaFBZxKlOur8TkcD3F_PfVjCZPJWI_nLNVyFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏السفينة التي استهدفها انصار الله في اليمن تم إيقاف تشغيل نظام التعرف الآلي (AIS) الخاص بالناقلة منذ 5 أيام، عندما كانت راسية آخر مرة في ينبع.</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/naya_foriraq/85899" target="_blank">📅 20:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85898">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cepD3fXpV8zir-1DGgsw3F9RcmcYGGGZLJXLV5U0Wxd8QFcVfsgyb7Vszt7jxYuCAiCfbVskaxxML04cG9F9t7bam7S0OhGlBP-RpO5Fb9B-Z7vrNODwNa8QDeC41A-bp1i31Zq2N-SAgnHRhx85RbbzjSv0zp1-AtlbC5QaqO2jVaFCVRovEmTPTxFQ9AWypVWYulLUPQeXC2ayYm3YVEp336d9sCwHeWUvcquCcRHCKedI5ly-WKICQZs87VMn8aUzMIbe1E2nF6M2tDUOFBN963m93at70MxeP5d3JY4FtYwF21KxpfyByOepnNuZ5x8gVs43_mhYucbcalQAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏السفينة التي استهدفها انصار الله في اليمن تم إيقاف تشغيل نظام التعرف الآلي (AIS) الخاص بالناقلة منذ 5 أيام، عندما كانت راسية آخر مرة في ينبع.</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/naya_foriraq/85898" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85897">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زيلينسكي المهرج يزعم: استهدفنا سفنا في بحر قزوين تنقل شحنات عسكرية لها صلة بإيران.</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/naya_foriraq/85897" target="_blank">📅 20:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85896">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
عراقجي:  أن العمل الانتهازي الذي انطلق من أوكرانيا لن يمر دون رد.  هاجم زيلينسكي سفينة تجارية إيرانية وقتل بحارًا. هذا العمل يُعد انتهاكًا صريحًا لميثاق الأمم المتحدة، ونُفذ بتحريض من إسرائيل لجرّ أوروبا إلى حرب معها.  خلال اتصالات هاتفية مع كايا كالاس،…</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/85896" target="_blank">📅 20:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85895">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5AS893n-WHiQ3s98OWsYBuVNn4rR3qUi-YaJKmR5pkwWYE5Vb3ZbOJTvX3qyShIo8CMXOEr4Taf-HFWHpD-MZQcF3YZyR_RfRzyNWR7YdH6Nwtq8teIB7E1Uf4OXBWaJO0rNYT0g7rpL_Ck0SHKZqGwib0tl3AkPRJZ-O-zYiCAkhAthWaYrzIzNBbjsQKAu97lcUgwh2aXc7Nqvjq6sI_CTRGja_nDUOGTLPmzb1r1YdHJIHuoMS049vBe19Uio4eH8xfxHBn0T7aL789AFSjFXbKlML44MbU7n-kXQ46fByZAz9PduCs298JX8NEsoc3wUWv-P1ouelkNa-uLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
(أمريكا، لا تثقي به)
شعارات على شاشات عرض متجولة نصبت امام البيت الابيض اثناء لقاء نتنياهو وترامب.</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/naya_foriraq/85895" target="_blank">📅 20:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85894">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇸🇦
مجلس الوزراء السعودي:
ندين اعتداء الميليشيات التابعة لإيران باليمن والعراق على منشآت نفطية وسفن بالبحر الأحمر.</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/naya_foriraq/85894" target="_blank">📅 20:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85893">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
وكالة أمن حكومة إقليم كردستان العراق:
خلال الأربع والعشرين ساعة الماضية، تعرضت خمس طائرات مسيرة لهجمات في كويا ومحيطها، وطائرة مسيرة أخرى لهجوم في شربازهر.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85893" target="_blank">📅 18:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85892">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGBcYMB7kdY-SV302MgAV36TaRfmHqm6lekEB70U8z1YcpoCOGdKs5WhwM8dqoaOi5D19fsmjQPo9PZ_wRTq2v_dThQEVN85Lytf-7xTr8l5ZmzVKGrOpnYza4ITzqvBJy2zoAJVANNzxO99mZyBm8CUzo6pq18moXUNx483gecGr6z92KoGEZfNICCV6ToCY74bS6DRXoczXI-ioYUl2Ayca6HL-jTAo7zM3PkMQjaw8etuXGm0yNQlvn00guiWNqHqE1Re94Sz_hu9pU-7EAallUA-FKPgSS7Cnduo7Xokh8OM_696csFbKx_rm-1f_r-zk2QwSGDvXh2YuW-XBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس اسماعيل قاأني:
من المتوقع أن تتعلم الحكومة السعودية من سلوك أمريكا غير الحكيم والمكلف وأن تنهي الحصار المفروض على دولة مسلمة يبلغ عدد سكانها أكثر من 38 مليون نسمة.
إن توقعات المسلمين في جميع أنحاء العالم من المملكة العربية السعودية، التي تعتبر نفسها حامية الحرمين الشريفين، هي أنه بدلاً من مواصلة الحرب والضغط على أمة مسلمة مضطهدة، ينبغي عليها استخدام قوتها ومواردها لدعم الشعب الفلسطيني ومواجهة جرائم الكيان الصهيوني.
إن محاولة إنقاذ غزة المضطهدة مسألة شرف، وليس استمرار الحصار على الشعب اليمني المضطهد.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/85892" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85891">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇱
🇺🇸
اذاعة جيش العدو: ترامب يقول قبل ساعات من لقائه بنتنياهو: "لا أحتاج إلى أن يقدم لي نتنياهو معلومات استخباراتية عن إيران، إنه سيقدمها لأنه يريد أن يبقى مشاركا في الحرب."</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/85891" target="_blank">📅 18:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85890">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c4d8863e.mp4?token=GNfj_AHyK7ic7SG48d-LhgpA0ICVr17-D48qkHUpH_ftQPmQ6Wo1pX1HIb30ZdHpNXomjAtSuOjoDrDgHz5538cvjbCBKUEg89T--oefIQ6Y0OuFH71et9B6PnZG1tYO-GC3bzyxepPXgMD1bJJqWqRzYaxiOKqt3OAxSPh_NJsRaLtdLw4rIUNjEMi7clakIPIuyXcQrwXKbMyg-fiBj6azC5QLKcMkzxzTEED36pP3_zQRcuym1DXFPp5C1anbAd31mWJo4E3Tts_n7RNPX74EG86fbid4OTyYh4FOPifKYuqrQXrefRVb91LpiMIloMKKNOSeSeMD2YLVM-tjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c4d8863e.mp4?token=GNfj_AHyK7ic7SG48d-LhgpA0ICVr17-D48qkHUpH_ftQPmQ6Wo1pX1HIb30ZdHpNXomjAtSuOjoDrDgHz5538cvjbCBKUEg89T--oefIQ6Y0OuFH71et9B6PnZG1tYO-GC3bzyxepPXgMD1bJJqWqRzYaxiOKqt3OAxSPh_NJsRaLtdLw4rIUNjEMi7clakIPIuyXcQrwXKbMyg-fiBj6azC5QLKcMkzxzTEED36pP3_zQRcuym1DXFPp5C1anbAd31mWJo4E3Tts_n7RNPX74EG86fbid4OTyYh4FOPifKYuqrQXrefRVb91LpiMIloMKKNOSeSeMD2YLVM-tjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية تظهر اثار هجمات انصار الله على البنية التحتية النفطية في ينبع السعودية على طول البحر الأحمر. ‏تظهر آثار حروق واضحة حول خزان تخزين كروي تابع لشركة أرامكو السعودية في محطة ينبع مما يشير إلى احتمال حدوث أضرار في الموقع.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/85890" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85889">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf5eced14.mp4?token=IWPsWhIF9riL2hvjnFUL7vbFRtFiAO1x_Ovn5PXDToTqjr_GTY-Ijlui_8KXLDPZ3PANNqev3wjEPZYZd06NJ3cyLAj-m2bseCJZe29OyQpIi5QFxs0HV-BEC8P1QwoFCqDdxXUQIwt9rQgbQjdIY-YSsHCuzEgn_pwDUo63YgiAjAWPIJDrIamYxK2uDr1pFVWIWeKZDYN2LInXX1M4VCg481CIZ7j5AJCTRVbKvzl4u2v_WunfvnG-2fUc31Mzj3Cg_kc7Kwn54Fy84UhlSOWJkFR6-CQcjTlreEVCxuQHL84gJOBWHI_OEthsADdZ_mw11EghtELbnc3VuyE68w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf5eced14.mp4?token=IWPsWhIF9riL2hvjnFUL7vbFRtFiAO1x_Ovn5PXDToTqjr_GTY-Ijlui_8KXLDPZ3PANNqev3wjEPZYZd06NJ3cyLAj-m2bseCJZe29OyQpIi5QFxs0HV-BEC8P1QwoFCqDdxXUQIwt9rQgbQjdIY-YSsHCuzEgn_pwDUo63YgiAjAWPIJDrIamYxK2uDr1pFVWIWeKZDYN2LInXX1M4VCg481CIZ7j5AJCTRVbKvzl4u2v_WunfvnG-2fUc31Mzj3Cg_kc7Kwn54Fy84UhlSOWJkFR6-CQcjTlreEVCxuQHL84gJOBWHI_OEthsADdZ_mw11EghtELbnc3VuyE68w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية تظهر اثار هجمات انصار الله على البنية التحتية النفطية في ينبع السعودية على طول البحر الأحمر. ‏تظهر آثار حروق واضحة حول خزان تخزين كروي تابع لشركة أرامكو السعودية في محطة ينبع مما يشير إلى احتمال حدوث أضرار في الموقع.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85889" target="_blank">📅 17:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85888">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937ee85070.mp4?token=DJ5QVYZ4-3SWd3FR7c1rR6UysTmSOffRrP1kGFddy0DBEpYCvLOnQXhw6AafiXrWq295uJ9jIymIymmGF51r4mjDWK5r0_fyFt6P1UDP5xXCPRLVPC15L9RdW8IGtnxTi1tJdfThsfAZJ9tTNtOUEEpfrBcdiYtrUw9sc0qYg-3YeZ8b55135INeuRP7Qw3yXCTRxgE5Nh6TZxeXmLowFV3EiDRUxWBDz25NQmdNwWXGrQJWblmKGFdewcH7EHbDVedSCirnBgZxSuGGd1nWX0cg08H2BJFvbd45o_pnAc83jXyEpQ6BigE9wAg9zAPmLX-TiStjDh347AZb96EQ5mgv1NP8TtSYjqM0OBmvWoFkxxpjRDkeHV93jqPOZbFVN1besEoDADcvrPZbApTp-8uG1NPGN1ZRqppQ4Mu2LzH2D1LOfyAxDkJcC_EjShk4AIwvPcE4u7VyFjddIQF-8YQxzc1clGsVm92o2H9isaTposoVe580SErLSTTedVJ6bcEVzsjFWj6JQCVDUt4-M9xgJc0p1wYd-TEFTnNuiIkRpAUMFjeyFS2OhQEEyOMeGRnxAxv5G989SROqUHrH1zlQUHpqmVrLRuKMpZWFgebSau14NzLJPlUUH4R6FU6rb-b1HjkkiSGKjiWUvd_Rj2PQlCFISO5dEQPVtnIFFng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937ee85070.mp4?token=DJ5QVYZ4-3SWd3FR7c1rR6UysTmSOffRrP1kGFddy0DBEpYCvLOnQXhw6AafiXrWq295uJ9jIymIymmGF51r4mjDWK5r0_fyFt6P1UDP5xXCPRLVPC15L9RdW8IGtnxTi1tJdfThsfAZJ9tTNtOUEEpfrBcdiYtrUw9sc0qYg-3YeZ8b55135INeuRP7Qw3yXCTRxgE5Nh6TZxeXmLowFV3EiDRUxWBDz25NQmdNwWXGrQJWblmKGFdewcH7EHbDVedSCirnBgZxSuGGd1nWX0cg08H2BJFvbd45o_pnAc83jXyEpQ6BigE9wAg9zAPmLX-TiStjDh347AZb96EQ5mgv1NP8TtSYjqM0OBmvWoFkxxpjRDkeHV93jqPOZbFVN1besEoDADcvrPZbApTp-8uG1NPGN1ZRqppQ4Mu2LzH2D1LOfyAxDkJcC_EjShk4AIwvPcE4u7VyFjddIQF-8YQxzc1clGsVm92o2H9isaTposoVe580SErLSTTedVJ6bcEVzsjFWj6JQCVDUt4-M9xgJc0p1wYd-TEFTnNuiIkRpAUMFjeyFS2OhQEEyOMeGRnxAxv5G989SROqUHrH1zlQUHpqmVrLRuKMpZWFgebSau14NzLJPlUUH4R6FU6rb-b1HjkkiSGKjiWUvd_Rj2PQlCFISO5dEQPVtnIFFng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أزمة الوقود متواصلة في محافظة أربيل باقليم كردستان شمالي العراق وسط استمرار طوابير المركبات أمام محطات التعبئة في ظل شكاوى المواطنين من صعوبة الحصول على الوقود وامتداد فترات الانتظار دون بوادر واضحة لانفراج الأزمة حتى الآن.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85888" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85887">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8db80c386.mp4?token=DsF-RRh72B6QxZHcRDQPBnKlWbGETli5VVe1Ys4-JT5I4GratYz-COyoDm4uKPhYrMOkA68T2o4pPYLCGu_Jw3Jcnnx_of42zgGpT6JrnHEZEHXx9L3bc3wL14kKkWijLvmfLw8nB9nRndETnp0kAmxH53ULH7mp6sOfMs6RMaCCLTtBe2Cl-GVrAR8r0pOpqQm7G5yorX7vtZI720Zpvb9E7Ukb0C_cFP7KlWRJDlHhO3jaZT5Gqi_cn96aqVU2dNxF_IbUYAOugnEvY_fAPwY4gyZ53PichSLM4MfIU5vJr_4ZOmOlQtsgxXQze0D920TOPoD242JIZI1i5a6y_gm5lzBCsV9xEpuiTXjvtrFdRjXlUntqG_J1DAZ1m0y8-j07l1rholZLO45kCrysdGTcqiIPccx8EKPWQ-2rz6UgGmKYBSAYNCDNnCyrUy8ZYUcRDyky0b3rnWOO8vQ7E732DLP7XO39ejb665AwFO9CoHxJP7zkuSNW6i3Mm3co43Rkv6aBlRV3wXaIrcJN4BZUunU6yCccCN73VVZ7N4QJ7G18GZHm_Y9lZLOm6RoRCbUXqKx0YkfdZwJrTWYo8nH695lPuH-UBV-yYcaJ7dwPAgWIGuXXlW7KOtHvBWSBZY4Nhg7Ot2xwyYbXafH0TGFhiWWriYFtVLkHSab0VZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8db80c386.mp4?token=DsF-RRh72B6QxZHcRDQPBnKlWbGETli5VVe1Ys4-JT5I4GratYz-COyoDm4uKPhYrMOkA68T2o4pPYLCGu_Jw3Jcnnx_of42zgGpT6JrnHEZEHXx9L3bc3wL14kKkWijLvmfLw8nB9nRndETnp0kAmxH53ULH7mp6sOfMs6RMaCCLTtBe2Cl-GVrAR8r0pOpqQm7G5yorX7vtZI720Zpvb9E7Ukb0C_cFP7KlWRJDlHhO3jaZT5Gqi_cn96aqVU2dNxF_IbUYAOugnEvY_fAPwY4gyZ53PichSLM4MfIU5vJr_4ZOmOlQtsgxXQze0D920TOPoD242JIZI1i5a6y_gm5lzBCsV9xEpuiTXjvtrFdRjXlUntqG_J1DAZ1m0y8-j07l1rholZLO45kCrysdGTcqiIPccx8EKPWQ-2rz6UgGmKYBSAYNCDNnCyrUy8ZYUcRDyky0b3rnWOO8vQ7E732DLP7XO39ejb665AwFO9CoHxJP7zkuSNW6i3Mm3co43Rkv6aBlRV3wXaIrcJN4BZUunU6yCccCN73VVZ7N4QJ7G18GZHm_Y9lZLOm6RoRCbUXqKx0YkfdZwJrTWYo8nH695lPuH-UBV-yYcaJ7dwPAgWIGuXXlW7KOtHvBWSBZY4Nhg7Ot2xwyYbXafH0TGFhiWWriYFtVLkHSab0VZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن الاعمال النووية الجارية في جبل بيك آكس الايراني: أنا لا أحتاج إلى أن يخبرني نتنياهو أشياء عن هذا الموضوع. نتنياهو يخبرني ذلك لأنه يريد أن يبقى متورطًا في الأمر. قلت له: "لماذا تحتاج إلى أن تخبرني بهذا؟" إذا لم تكن هناك صفقة، فسنقوم بتدمير هذا الموقع…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85887" target="_blank">📅 16:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85886">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aab2d7d62.mp4?token=L8VTUfCjYxaSdoDV4eCJMSiWFTF6EOwUlFkIveyb8LE-yBgLDRthdrdDKjf1ZrDWQ3GPZwimmY_2REY-WUZAU0Hm00mWm6uAUQl9Z3XnmXsx_1raI7NwknExgLpzKWp7svvM0wzVpUPb12ck_TKQAxK7EudXDh7dX9kGm4boEJZEMdVjuRCW7s6LnNTeZ9bM1yMIu0X_wtnCi3CARChFiWIVTbwXZNQfz4pzDPD9E_vxFKmAfniphIS6oO24-PEbU6S9B4VfklMZ4mawhmQ6MUer6avKuQ2mPDuPfvpLE9D1O5zEirogNY-evYXHWANHeJoFL8c6MWlfo6QVTWQolp-aBlTNMXXLMqrDMnMLEQJ0PbW3W09m7OwwqijvxAcE_pAhosc5M7tInW3TqY4UNjkZeEbKa6prDPtnMqy6RnzI-7E3WWQq524pdYayGfOubU_ysTLZVjBg5wccn_KEpMN0BKThNpOR132Ysa2z_P5MjE6QPoENpXlPOEuAl6RF15gz3Bg2vtpzgdqtnkChdemqep1oetQY1GLA5BSHyUKNLh4VfZ2p9-c8kc-TTiDB2Vb1M1fbEJ0_2p7HZneos1qv5jjUM7tRqO0qBeWOkKS9HNXxKZ4K5sMCISbwhpWsTmHog7Pm41ptWyhJaSg35h5gZ72ycIsGrQ8DI3R9Urc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aab2d7d62.mp4?token=L8VTUfCjYxaSdoDV4eCJMSiWFTF6EOwUlFkIveyb8LE-yBgLDRthdrdDKjf1ZrDWQ3GPZwimmY_2REY-WUZAU0Hm00mWm6uAUQl9Z3XnmXsx_1raI7NwknExgLpzKWp7svvM0wzVpUPb12ck_TKQAxK7EudXDh7dX9kGm4boEJZEMdVjuRCW7s6LnNTeZ9bM1yMIu0X_wtnCi3CARChFiWIVTbwXZNQfz4pzDPD9E_vxFKmAfniphIS6oO24-PEbU6S9B4VfklMZ4mawhmQ6MUer6avKuQ2mPDuPfvpLE9D1O5zEirogNY-evYXHWANHeJoFL8c6MWlfo6QVTWQolp-aBlTNMXXLMqrDMnMLEQJ0PbW3W09m7OwwqijvxAcE_pAhosc5M7tInW3TqY4UNjkZeEbKa6prDPtnMqy6RnzI-7E3WWQq524pdYayGfOubU_ysTLZVjBg5wccn_KEpMN0BKThNpOR132Ysa2z_P5MjE6QPoENpXlPOEuAl6RF15gz3Bg2vtpzgdqtnkChdemqep1oetQY1GLA5BSHyUKNLh4VfZ2p9-c8kc-TTiDB2Vb1M1fbEJ0_2p7HZneos1qv5jjUM7tRqO0qBeWOkKS9HNXxKZ4K5sMCISbwhpWsTmHog7Pm41ptWyhJaSg35h5gZ72ycIsGrQ8DI3R9Urc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مقر خاتم الانبياء المركزي:
بسم الله الرحمن الرحيم
أعلن رئيس الولايات المتحدة، في أعقاب أعمال عدوانية وجهود متواصلة لزعزعة استقرار المنطقة، ما يلي:
‏سيتم دفع التعويضات من الأصول الإيرانية التي تم تجميدها عن الأضرار التي لحقت بالسفن التي تضررت خلال الحرب المفروضة على إيران، بسبب انعدام الأمن الذي خلقه الجيش الأمريكي، وانتهاكات الطرق غير القانونية وغير الآمنة في الجزء الجنوبي من مضيق هرمز.
‏وبينما نحذر الرئيس الأمريكي المجرم من عواقب هذا العمل غير القانوني، فإننا نعلن لجميع الشركات والدول التي ترحب باقتراح ترامب وتستخدم الأصول الإيرانية المجمدة تحت هذا الذريعة أنه من الآن فصاعدًا، لن تسمح القوات المسلحة للجمهورية الإسلامية الإيرانية لأي من سفنها بالمرور عبر مضيق هرمز.
‏ولا نصر إلا من الله العزيز الحكيم.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85886" target="_blank">📅 16:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85885">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/85885" target="_blank">📅 16:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85884">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga-j2AEXXP00_v8SyAXQOQoaKs0y8fNzSk9GrnJ8lA-DxqtYViwb-wV7H6VVnO4INmAqcDO_OKKGjozTcREnM6X4Ht0u6ZdML_IaRyyM9hZQlAHBAhmNN_f99A9iZLjH-Lf1OjW8h2wHK8s1g8JQp0f4ayjenESBfPbre8kcNpkzE5LPiQdRwMQbNzEN0UNQJBi_YutMtadz3KOl6cbCqKl---KMJUTdX70ePDZQWCoSuRu_8s75qm66u2sseNspA_zfhokD98JLgXok_SkpekmLl0AidmddTcrY8MkeNJWfWUapB2a2ItLGQYUKGeljievv0lABuXUNtg-JkyLASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
کانال خبری ما در روبیکا و بله راه اندازی شد.
🔹
لینک کانال روبیکا:
rubika.ir/Naya_Fa
🔹
لینک کانال بله:
ble.ir/Naya_Fa
کانال سروش و ایتا به زودی ..</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85884" target="_blank">📅 16:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85883">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrgkSBaapXRfG85lYa3i7YWWOJdE_EA6SDlmmyM91lrBmbHbrM8b1l9Fa6Iu4QFkGc2HgXiVM0LUfcMd4gleNyS9IEhcr5qm1t9cVpYSWZNEwCBJs-qsCqW3DtAFU6Zw2h-WHA4vCdC3-YRylzogyMGUg0J58BVmh_LqvNeq_esZkU23jTxjhAFxap8mB92SxYqbwrh6KnKvb-dtUBJuS7w8DhOquKjiMzRNlxp8VUdNGqC1Luze3bTMzig-Jn0fotUMxaMuNUxhOqTjgFaMNBvHL0qBvaLOCu9Rmqh1OFiYj2aqZ0AG5T2e72QSN_oDIaeuLBnKkoLmUYn4ZZ2yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب عن الاعمال النووية الجارية في جبل بيك آكس الايراني: أنا لا أحتاج إلى أن يخبرني نتنياهو أشياء عن هذا الموضوع. نتنياهو يخبرني ذلك لأنه يريد أن يبقى متورطًا في الأمر. قلت له: "لماذا تحتاج إلى أن تخبرني بهذا؟" إذا لم تكن هناك صفقة، فسنقوم بتدمير هذا الموقع…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85883" target="_blank">📅 16:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85882">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الأردن تعرضنا لهجوم بسبعين صاروخ و ٢٥ مسيرة خلال ١٦ يوم</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85882" target="_blank">📅 16:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85881">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏الاعلامي: سمعنا أنكم تتحدثون مع قادة من إيران. لكن إيران صرحت علنًا قائلةً: "نحن لا نتحدث مع الولايات المتحدة".  ‏ترامب: حسناً، لقد خرجوا للتو وقالوا إننا نتحدث  ‏الاعلامي: هل يمكنك إذن أن تخبرني مع من تتحدث؟  ‏ترامب: لقد أجرينا بعض المحادثات الجيدة جداً</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85881" target="_blank">📅 16:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85880">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏الاعلامي: سمعنا أنكم تتحدثون مع قادة من إيران. لكن إيران صرحت علنًا قائلةً: "نحن لا نتحدث مع الولايات المتحدة".
‏ترامب: حسناً، لقد خرجوا للتو وقالوا إننا نتحدث
‏الاعلامي: هل يمكنك إذن أن تخبرني مع من تتحدث؟
‏ترامب: لقد أجرينا بعض المحادثات الجيدة جداً</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85880" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85879">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇰🇼
بسبب انقطاع التيار الكهربائي..
إغلاق بعض أجزاء مصفاة "الأزور" النفطية في الكويت والتي تبلغ طاقتها الإنتاجية 615,000 برميل يوميًا
الكويت تعورت</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85879" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85878">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇯🇵
انفجار يهز المركز التجاري في اليابان وتسجيل عدة وفيات وفقدان اخرين على خلفية الزلزال الذي ضرب البلاد وانهيار المباني.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85878" target="_blank">📅 15:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85877">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية: إن إسقاط طائرات مسيرة تابعة للنظام السعودي في المجال الجوي اليمني يثبت انتهاك النظام السعودي للمجال الجوي، ويمنح اليمن الحق في الرد بالمثل. ولمن يستنكرون رفض اليمن انتهاك أجوائه: افتحوا أجواءكم للطيران السعودي يسرح فيها ويمرح كما…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85877" target="_blank">📅 15:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85876">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
إن إسقاط طائرات مسيرة تابعة للنظام السعودي في المجال الجوي اليمني يثبت انتهاك النظام السعودي للمجال الجوي، ويمنح اليمن الحق في الرد بالمثل.
ولمن يستنكرون رفض اليمن انتهاك أجوائه: افتحوا أجواءكم للطيران السعودي يسرح فيها ويمرح كما يشاء ويستهدف من أراد.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85876" target="_blank">📅 15:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85873">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBvmc-Cz1bXKAQlwki-MOBdIGMpJNcorcgrddorFaTbuVUepgZM7CYplfpB_8zMSdtxAzbP18fvB4MFYc4vbaRomO9pBy3-_e1V4G3tqmr7KFzgiABbC31rWGotBSqG2QxjyGKzw1Z0-WFs0cNRVWwWbap6QBnRqFt_WE0_aLaAqD6oQZYCKD7tkbDNawnElycxQ0S4uCg9Z_cnZth5bsRR2dSI3wpuSnqk_CIY4Usq9VJX5l9jvvNHQJEwP8QiXNXJBUF5hTDpUX_fmDJlry_MrZr8XHlcSKztWhtDYFhLkPmG1j_DwPYkTcLMyLr0PMaj0o51fbqeZ-xWfwTcRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAtXbjTbTRSv9xtCtA9YUftP7NwqAlHYoWEU33zCUaoEhHbVJ01CjmXJEKN5FcxIOwuiuoeoD4eEL70LlQiVXg-Yukwl4nSrnWbZEu20LtWdm4OOhJUyHB0-qriQw0tOg0CaihYmCxOuddsOFS3EuQg9PQ3d_BpRO2cphXozGp0FBD8jLNys9oAqrShoA_b6LYn8nhF4MwFoGStrMJ4QLTUk75gTXGatM2tCG-tLAusN88LeK_oPU9178oTcfvQWyxR5caq3g6MJGCpieyHq1udjtNTag6WVsFZ9uq6IRQPsngiFqMD0XB-RRfiip-2w56Zkm7hvSJVMng-1u0Y0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5GSyDwjYnQ2gSlvCD4Piz1oylUHlWtLfTFh87ZoIAxOPHqLjXLGoMdZyP7RdCDShce1B6ZTopL4nLgxln7-wf-RjB1ARQmtm9A89ij4UdFip-okeOuQ3jJ17iO1oGSLa-8mS8O76Nt-ehDtBsmN8h_TQpno-T38Abi-TLKpUcPK6IAqYIQiXiraDgsYvvGMb6lj5MJN3hajOh9DdiTRBsZqJoCslfkFHBaVTDF9NVCSNQDmp5ODnJbHf4gCkLVydkKQXbKX_48AI0sLkYZqEMuFBeIRzQ_FRQtVLUhY3EIvkxO-Z0w5bYc6rbGzL2ldWBBy8vr7PceRW_mtubDdPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇸🇾
هيئة المنافذ الحدودية العراقية تحبط محاولة إدخال أسلحة داخل شاحنة قادمة من سوريا.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/85873" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85872">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd6LQiIxrxwaDXbx0RErreSHA6a235IrbZKTdMh2TJfcG0qFxP8WWdzwXF1_rL1Lke7HBYEfwlHmNEAeYpW7z6KkDDLJZFqA4bAh-7mWUtB4EhvET45BmrH84F6ARs3GxUyeFX-Dt0ZbC5WUEY7sIHe5dnqWDtELIJoiZizjJQ4MfcV4OaSkHL0Ex-zU7MBcc3JC-TFPEYzrkHaJ3nHcUXU0J5igI9L2O4_9roeiJ4M302gLd_MNh3eWS3W-FrPlosRMLgGi8_VKUUBep8AfGMSFN341UsAmmV8_dHxsCDHt9xzg45N8UGuSYdPH7ShsDhiAaHfUPCwDV8xf0lw8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇸🇾
هيئة المنافذ الحدودية العراقية تحبط محاولة إدخال أسلحة داخل شاحنة قادمة من سوريا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85872" target="_blank">📅 14:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85871">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شركة أرامكو السعودية تغلق مصفاة جازان للنفط التي تبلغ طاقتها الإنتاجية 400 ألف برميل يومياً عقب هجوم انصار الله قبل ايام.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85871" target="_blank">📅 14:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85870">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇱
وزير الشتات الإسرائيلي:
مشكلة إسرائيل الأساسية الآن هي سوريا خصوصا مع التمويل التركي.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85870" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85869">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇩🇿
🇦🇪
الرئيس الجزائري يهاجم الامارات:
هناك دويلة كل ما تضع قدمها تسيل الدم ولدينا أدلة ولا نريد زيادة الطين بلة في العالم العربي لما يشهده من انشقاقات ولو غير ذلك لقطعنا العلاقات معها منذ زمن بعيد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85869" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85868">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزير الحرب الصهيوني المجرم كاتس متفاخرا: اليوم، لم يعد هناك حي "الشجاعية" في غزة، ولم يعد هناك مخيم "جباليا". كل تلك الأماكن لم تعد موجودة. لقد قال رئيس القيادة الجنوبية لي: "لا أرى أي منازل، بل أرى شاطئ البحر." لقد دمرنا غزة. في غزة، نحن ندمر ليس فقط ما هو…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85868" target="_blank">📅 13:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85867">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزير الحرب الصهيوني كاتس: تم تكليف "الشاباك" لحماية نتنياهو والقيادة السياسية والعسكرية الإسرائيلية من التهديد الايراني الخطير.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/85867" target="_blank">📅 13:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85866">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني يهاجم اردوغان: نحن لسنا الإمبراطورية المسيحية المتهاوية. القدس ليست القسطنطينية، التي غزوتموها عندما أسسستم الإمبراطورية العثمانية. لا تحاولوا استفزازنا. نصيحتي لأردوغان هي ألا يحاول استفزازنا، وألا يضع نفسه في الموقف الذي وضعته فيه إيران.…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85866" target="_blank">📅 13:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85865">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هل سترد اسرائيل على الطائرة المسيرة التي أُطلقت في وقت سابق من اليوم من العراق؟!
🇮🇱
وزير الحرب الصهيوني كاتس: نحن نعرف كيف ندير الأمور - نحن مستعدون.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/85865" target="_blank">📅 13:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85864">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
صرف رواتب مجاهدي هيئة الحشد الشعبي.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85864" target="_blank">📅 13:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇱
🇮🇶
إعلام العدو عن مسؤول أمني: الطائرات المسيرة التي أسقطها الجيش يوم الأمس واليوم على الحدود مع الأردن، أطلقت من العراق.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85863" target="_blank">📅 13:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85862">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85862" target="_blank">📅 12:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85860">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51c4750bb.mp4?token=i5Mw7LOn67ZWW9giA_E3s_mPDHHW2GNBjZUl6rj6Ywu_zU5TgQb-N4bRQX914ZvtQw7YPeIMuoFEiEvkWL5YY-m5TAzNrdo15FnxVgiagtw3IrwNcim994fw_By7Sb68j2P4HZgxWP0E5icSnvIx1IJbZ-KZc615aU1HmMDTxOGqdpS0GEavRvPq2Wq4r49tQiXHgfZ7QgKhwhhTmkg4TT1ReMhK79yxYcSgoY_aq3HNPHLLXDclbISNC9Naq5Lwt2VZD7J9OGmHwL-EO1B-mtktuK_Cza_eQDe3xL6QqpidGWb0HI_w9S_7ZrNIC90P2QuK6Fh7SW_eVExNOyVMHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51c4750bb.mp4?token=i5Mw7LOn67ZWW9giA_E3s_mPDHHW2GNBjZUl6rj6Ywu_zU5TgQb-N4bRQX914ZvtQw7YPeIMuoFEiEvkWL5YY-m5TAzNrdo15FnxVgiagtw3IrwNcim994fw_By7Sb68j2P4HZgxWP0E5icSnvIx1IJbZ-KZc615aU1HmMDTxOGqdpS0GEavRvPq2Wq4r49tQiXHgfZ7QgKhwhhTmkg4TT1ReMhK79yxYcSgoY_aq3HNPHLLXDclbISNC9Naq5Lwt2VZD7J9OGmHwL-EO1B-mtktuK_Cza_eQDe3xL6QqpidGWb0HI_w9S_7ZrNIC90P2QuK6Fh7SW_eVExNOyVMHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مسير مجهول الهوية يحلق في اجواء مدينة الناصرية جنوبي العراق</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85860" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85859">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇱
🇮🇶
إعلام العدو عن مسؤول أمني: الطائرات المسيرة التي أسقطها الجيش يوم الأمس واليوم على الحدود مع الأردن، أطلقت من العراق.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85859" target="_blank">📅 11:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85858">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇱
🇮🇶
إعلام العدو عن مسؤول أمني:
الطائرات المسيرة التي أسقطها الجيش يوم الأمس واليوم على الحدود مع الأردن، أطلقت من العراق.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/85858" target="_blank">📅 10:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85857">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
قيادي في حزب المعارضة الإيراني
: تعرضت مقراتنا في وادي آلانة لهجوم ب 5 طائرات مسيرة على الأقل فجر اليوم.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/85857" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85856">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏
🇮🇷
🇮🇱
🇦🇪
فايننشال تايمز:
مع انهيار وقف إطلاق النار الهش بين الولايات المتحدة وإيران، قامت الإمارات العربية المتحدة بمقامرة جريئة: إعادة تنشيط القنوات الدبلوماسية والاقتصادية مع إيران وإعادة الخطوط الجوية الإيرانية و ٢٠ الف مقيم بشكل مؤقت مع مضاعفة العلاقات العسكرية مع إسرائيل والولايات المتحدة.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/85856" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85855">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">إعلام أمريكي: سلطنة عُمان قدمت لإيران مقترحاً لآلية إقليمية مشتركة لإدارة مضيق هرمز تعتمد على رسوم طوعية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/85855" target="_blank">📅 09:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85854">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇱
إذاعة جيش الاحتلال: الجيش الإسرائيلي قلّص عدد الجنود في كتيبة احتياط على الحدود اللبنانية بنسبة تقارب 30٪ مقارنة بالعدد الأصلي ؛ وأوضح قائد الكتيبة أنهم يواجهون أزمة حادة في عدد الأفراد تؤثر على قدرتهم على أداء المهام.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/85854" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85853">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/85853" target="_blank">📅 08:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85852">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/85852" target="_blank">📅 08:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85851">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات عنيفة تهز المنطقة الشرقية من السعودية</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/85851" target="_blank">📅 08:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85850">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات عنيفة تهز المنطقة الشرقية من السعودية</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/85850" target="_blank">📅 08:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85849">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b37b70352.mp4?token=NNzNeAJZ7bHeU1ac4uL9bUfwWaFBEJUcwLDsO-Kk1_5NIbHgY2TcKZaSIu8ejQdinhOsBEZHMYVqO9iluDHD9e1kofjsn8V9tFSS9HzSlDCqcHOBTjO55a7jpWfcPjVFO7AmCYpJaNQiiScwors84s-T_zv2RJwTyR0IfXXkgYYuchLMOvjqTRPiEM9fmWEpPTqhGjL99Ka6A2RYRw_5WKE0SdX0XWCHA-aHA1UYAtvUyiGVyVcXkJ67iPu6f0Otcv5pYzqekQENrTpDuwFuGqbe-sR5Z156pv1ppZhuoVtZLBg29rW-0RTniH5AJ1ioaZrYfuJVf3oVAPg4nYNvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b37b70352.mp4?token=NNzNeAJZ7bHeU1ac4uL9bUfwWaFBEJUcwLDsO-Kk1_5NIbHgY2TcKZaSIu8ejQdinhOsBEZHMYVqO9iluDHD9e1kofjsn8V9tFSS9HzSlDCqcHOBTjO55a7jpWfcPjVFO7AmCYpJaNQiiScwors84s-T_zv2RJwTyR0IfXXkgYYuchLMOvjqTRPiEM9fmWEpPTqhGjL99Ka6A2RYRw_5WKE0SdX0XWCHA-aHA1UYAtvUyiGVyVcXkJ67iPu6f0Otcv5pYzqekQENrTpDuwFuGqbe-sR5Z156pv1ppZhuoVtZLBg29rW-0RTniH5AJ1ioaZrYfuJVf3oVAPg4nYNvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد أخرى لحظة حدوث الانفجارات في أحد مخازن الأسلحة التابعة لحزب المعارضة الإرهابي في محافظة السليمانية شمال العراق.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/85849" target="_blank">📅 07:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85848">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇱
🇺🇸
هارتس العبرية: ‏يزور نتنياهو ترامب اليوم وهو يملك عدداً أقل من الحلفاء وخيارات غير جيدة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85848" target="_blank">📅 07:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85847">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇨🇳
زلزال بقوة 6 درجات يضرب مقاطعة تشينغهاي في الصين.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85847" target="_blank">📅 07:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85846">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a50630e63.mp4?token=eBqHznnBNUkhTkFypf8vyi_kVEQbPeEMQGyF7hdhvhpwb9PI8GlPICZGR-LZ1or6UPE-zNfAayaWIIhhRJ3PfVesf41X6OR47e8PBZIx-O_fAKUbWak6DXvx5Cg54-pKVk2NCZ3r0ZNeM0cIQfbt-Vgk20XxEh1TRDVml85803hxrIJCGK0lVmUpr38zG-Yit4PsonNPSkyHFnR4Y1KVG1BGS__CFyhhY3GKijBXUhtPGf7SjFWgTCuS7V9ubH88DMYAuCd4SSTZZYANNVAPcx780az7Hym5zS5EbQXqKTAa3mujQQTBjFuEzDswlxmyeYDDzaQ0BQH7oAK5MJwE3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a50630e63.mp4?token=eBqHznnBNUkhTkFypf8vyi_kVEQbPeEMQGyF7hdhvhpwb9PI8GlPICZGR-LZ1or6UPE-zNfAayaWIIhhRJ3PfVesf41X6OR47e8PBZIx-O_fAKUbWak6DXvx5Cg54-pKVk2NCZ3r0ZNeM0cIQfbt-Vgk20XxEh1TRDVml85803hxrIJCGK0lVmUpr38zG-Yit4PsonNPSkyHFnR4Y1KVG1BGS__CFyhhY3GKijBXUhtPGf7SjFWgTCuS7V9ubH88DMYAuCd4SSTZZYANNVAPcx780az7Hym5zS5EbQXqKTAa3mujQQTBjFuEzDswlxmyeYDDzaQ0BQH7oAK5MJwE3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات ثانوية عنيفة في مخازن السلاح التابعة لإرهابيي المعارضة الكردية الإيرانية في محافظة السليمانية شمال العراق.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85846" target="_blank">📅 06:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85845">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇶
تصاعد أعمدة الدخان من داخل مقر تابع للإنفصاليين الأكراد في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85845" target="_blank">📅 06:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85844">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الصهيوني:
إعتراض طائرة مسيرة عند الحدود الأردنية؛ التحقيقات تجري لمعرفة مصدر إطلاقها.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85844" target="_blank">📅 06:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85843">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI5ZXFB1fcASmCjAAh6rUsdqoiFlfk6lDtZnK4onzDzVZ3l9GpBCM9GIgygsYIIo4H133udfjPIbZ1bDcTsZHHGMZdsvPIcAkOGAZaivREXLlawKS2kwwa686y7WGyYIrQMQg45S1FSqDHCQV7PFpqzOrFSSHU-UKX5EZbAmC-9F9z_eh8333cl83RJL8vWXm7CPXmVReIl-jVryOy5jMUcG8K8zS1dF8XPpBtmY9RRnL_SNm-rMc4UIi6iPBiuVnqcf9PWzpbsZQ74co8RWYvG8P3xitTXBHSilmQ8wbJko-rQFEetBbpiO-BeYzh3-Ff3WMsj7m8JmnE3M6I6vzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مع أول ساعات الصباح.. إستهداف أحد مقرات المعارضة الكردية الإرهابية في محافظة السليمانية شمالي العراق بسرب من الطائرات الإنتحارية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85843" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85842">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
مع أول ساعات الصباح..
إستهداف أحد مقرات المعارضة الكردية الإرهابية في محافظة السليمانية شمالي العراق بسرب من الطائرات الإنتحارية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85842" target="_blank">📅 05:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85841">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صافرات الانذار في غلاف غزة</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85841" target="_blank">📅 05:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85840">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
مسؤول أميركي:
العقوبات والحصار البحري الأميركي سيستغرقان وقتا أطول لإجبار طهران على الجلوس إلى طاولة المفاوضات.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/85840" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85839">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/85839" target="_blank">📅 01:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85837">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293704c82e.mp4?token=Auy1zGv50CyW0woO7CJSZa_l_6jQyBSH1o9W814LPWRqs1G0novfhZc7UHVI061xSZcLmE0GlvvjxmIfaxw2L3OXSU4RB_cvsBCOlwP5UmaQPMm65xKOw5Q_wlM2ZEZzbjIPcY8xihnqLNpWNbuE0IQWUqgOEDCzHP5SZel2gwFvlM4a7jTXGq13aI-3IzhRgfgC2hN7SieZChMQ0gRWSBzNy0Ycqzde8Ly7NiMWWcO8ySuj4H02-FxwS1XxPMFqvkviyNF4R8eEJNg_XsEzu3jmRq0fvLIKk0kEk8QZOijK8WY__aMA_k9ZTEGDuJSYWzkd2yNS_4GjLdi91Whlfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293704c82e.mp4?token=Auy1zGv50CyW0woO7CJSZa_l_6jQyBSH1o9W814LPWRqs1G0novfhZc7UHVI061xSZcLmE0GlvvjxmIfaxw2L3OXSU4RB_cvsBCOlwP5UmaQPMm65xKOw5Q_wlM2ZEZzbjIPcY8xihnqLNpWNbuE0IQWUqgOEDCzHP5SZel2gwFvlM4a7jTXGq13aI-3IzhRgfgC2hN7SieZChMQ0gRWSBzNy0Ycqzde8Ly7NiMWWcO8ySuj4H02-FxwS1XxPMFqvkviyNF4R8eEJNg_XsEzu3jmRq0fvLIKk0kEk8QZOijK8WY__aMA_k9ZTEGDuJSYWzkd2yNS_4GjLdi91Whlfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق يظهر لحظة وصول المسيرة الانتحارية إلى هدفها والانفجار الكبير داخل مقر الانفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85837" target="_blank">📅 01:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85836">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a1c105dc2.mp4?token=f2lTVQcoNWalBbZk_MHF0iYl58qPogC3M6kfJzVCO7ZObv-2ivyp9_KFB3mn85Q7zu8_DddH_J-GHRfWtGhl1bUgTr9u2EVwtlUS88ZcajHt25QmWynTzWFig-tq2PTcp1RTfh0Hopa1M0l507v4nCE-7sed8_jmxb_6TSESNbzAvxHRXhY7_UdwBlhPvS0smrBSYHQoB062jlT9X5uFXDzZj3CqvHQsz0U5Z97LoF0xaVE9V1CcQkHFSHm4rVz45ZeKCFrmy3BTrmx0H44PNYRIWCAa2BX285cESAaecFbrjLnw2pMgD0iiyWikuORICmaakm1suJ8CNihhFwI0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a1c105dc2.mp4?token=f2lTVQcoNWalBbZk_MHF0iYl58qPogC3M6kfJzVCO7ZObv-2ivyp9_KFB3mn85Q7zu8_DddH_J-GHRfWtGhl1bUgTr9u2EVwtlUS88ZcajHt25QmWynTzWFig-tq2PTcp1RTfh0Hopa1M0l507v4nCE-7sed8_jmxb_6TSESNbzAvxHRXhY7_UdwBlhPvS0smrBSYHQoB062jlT9X5uFXDzZj3CqvHQsz0U5Z97LoF0xaVE9V1CcQkHFSHm4rVz45ZeKCFrmy3BTrmx0H44PNYRIWCAa2BX285cESAaecFbrjLnw2pMgD0iiyWikuORICmaakm1suJ8CNihhFwI0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في القنصلية الامريكية بمحافظة أربيل</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85836" target="_blank">📅 01:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85835">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c75dde8d.mp4?token=QISmL5LtPsrB8dM8NtzTcpf55eXfE1UQGCtUdSUL1dB_7WnH2pEWipeTnyjc2j4GlYwgxNKfladHWDbEZYNpNoEvUMFSbKWieqEZVTv9a1Avif0O6HN33NBlpDiVdPB3FcshjYRlR3v9wHuwHkylpj5oeXq1DchlRibn7j-yjcw5BZHPQcn9abTKxZNb5SloDA2WkGcD5XleSJjylxZavyxlH5-HAJPnDnesCcbaS1DywQomr38Gc7UzoMHZmyn1_9pFsqMe4REEfRs84zb89PujWwhvD4DqKkJ4uM2slQi1eFwOvoEfu5_zsCWhylpFa-GwWccZ0ijD0j4S4IO5Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c75dde8d.mp4?token=QISmL5LtPsrB8dM8NtzTcpf55eXfE1UQGCtUdSUL1dB_7WnH2pEWipeTnyjc2j4GlYwgxNKfladHWDbEZYNpNoEvUMFSbKWieqEZVTv9a1Avif0O6HN33NBlpDiVdPB3FcshjYRlR3v9wHuwHkylpj5oeXq1DchlRibn7j-yjcw5BZHPQcn9abTKxZNb5SloDA2WkGcD5XleSJjylxZavyxlH5-HAJPnDnesCcbaS1DywQomr38Gc7UzoMHZmyn1_9pFsqMe4REEfRs84zb89PujWwhvD4DqKkJ4uM2slQi1eFwOvoEfu5_zsCWhylpFa-GwWccZ0ijD0j4S4IO5Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في القنصلية الامريكية بمحافظة أربيل</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85835" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85834">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇱🇧
🇮🇱
غارة صهيونية تستهدف تلة علي طاهر جنوبي لبنان.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85834" target="_blank">📅 01:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85833">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbfd07761.mp4?token=YvzyomKIN3WIen7Fn3kpgHelHC3XBpbTdrCRPdJsDS9q4_j2UxuumKRgUDU9LzDuUhij8vnVKHky5WYfK6jjn_uPUot-vl33Lg7tbID582_h4NYzkYPcpiy7gQxh3CFm7epin6iXl0crIXkp9F_Kt9mdjp2CmRyKsZmor8-A2Y5qTZwQjsbi3wh4EgPji6Dzpr958J30zTZnoOncNlxSIhPy3PHYFsrS_F2074SLelobfP5dsaukWx-BZBURr3jFLbzkyuF0akli5w-f0Ys4techi-FT4X2Ig6RWiYXopZUh5Cj5SMYgOVDqZL99sdzjSZpS-VicRyaTH6Fs6rpHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbfd07761.mp4?token=YvzyomKIN3WIen7Fn3kpgHelHC3XBpbTdrCRPdJsDS9q4_j2UxuumKRgUDU9LzDuUhij8vnVKHky5WYfK6jjn_uPUot-vl33Lg7tbID582_h4NYzkYPcpiy7gQxh3CFm7epin6iXl0crIXkp9F_Kt9mdjp2CmRyKsZmor8-A2Y5qTZwQjsbi3wh4EgPji6Dzpr958J30zTZnoOncNlxSIhPy3PHYFsrS_F2074SLelobfP5dsaukWx-BZBURr3jFLbzkyuF0akli5w-f0Ys4techi-FT4X2Ig6RWiYXopZUh5Cj5SMYgOVDqZL99sdzjSZpS-VicRyaTH6Fs6rpHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق واسع جراء الهجوم المسير الانتحاري الذي طال مقرات المعارضة الكردية في محافظة دهوك شمالي العراق.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85833" target="_blank">📅 01:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85831">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef242c138.mp4?token=tP39MY80Rg_eT8r4MViYrv8ShAHLqvGRI_XoqsO19FCsULzXEbePLKFNBsDk1LjinVtijDT0CV11To_HoEXDkJg8IbSzzb5-mgeRACRQeOC_9b8dtyhhbawGAKycgfHI7766Hbu4F7DrQMY6PUt9TWsWQJdbd6aROjsCxjZlLafKSnGcMOf1D1PGLa_7kE6IPlMzKuuXc4_MhUSsAEBm7lHL5wxlhPg46syDayFpaYZ0BiRpvSpSmtBuN1zSvfzW4cgFJfXZmXlpyuizzIHkGbr3A2RQExLhVGtkoCvT9V4X3RD2Vw4fMxebZzSwdZT2kvhDj6kJ6IjRlUmrPHUQtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef242c138.mp4?token=tP39MY80Rg_eT8r4MViYrv8ShAHLqvGRI_XoqsO19FCsULzXEbePLKFNBsDk1LjinVtijDT0CV11To_HoEXDkJg8IbSzzb5-mgeRACRQeOC_9b8dtyhhbawGAKycgfHI7766Hbu4F7DrQMY6PUt9TWsWQJdbd6aROjsCxjZlLafKSnGcMOf1D1PGLa_7kE6IPlMzKuuXc4_MhUSsAEBm7lHL5wxlhPg46syDayFpaYZ0BiRpvSpSmtBuN1zSvfzW4cgFJfXZmXlpyuizzIHkGbr3A2RQExLhVGtkoCvT9V4X3RD2Vw4fMxebZzSwdZT2kvhDj6kJ6IjRlUmrPHUQtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مباشر وانفجار عنيف أخر يطال مقر تابع للانفصاليين الأكراد في محافظة أربيل</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85831" target="_blank">📅 01:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85830">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6577c5fe83.mp4?token=Bf9xrBwF6Jtq_f7yP_pvdmyFo2yVGXgLsrEtpB2bas5LkY40a3INk9ySuXXQCyhBq9HKYTbJFGCr17q7xyrsvuiIi9ckh_Au-nkEz7S4xwy7b4Jy2T_tyj1F0BGD6m8lShIr1XkroPCUlw0iigYhw1qQ9ibgyFa12_ctASvxIMj2kVlFJ16OwCBaTSozx602wF8XSd4i1RSg15fOw4q7WEbmiMlWQw-YwkQih6p8qM9Bg45AcrM0uQrpXu4anMgWRu3qnJeh80h9_lH-pZFVCYWwUamjxbSMFgX0PED5CQtJKetZxsQShgDHfJeC6ezyXBkeQEYS9RHUd2zOrMJuDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6577c5fe83.mp4?token=Bf9xrBwF6Jtq_f7yP_pvdmyFo2yVGXgLsrEtpB2bas5LkY40a3INk9ySuXXQCyhBq9HKYTbJFGCr17q7xyrsvuiIi9ckh_Au-nkEz7S4xwy7b4Jy2T_tyj1F0BGD6m8lShIr1XkroPCUlw0iigYhw1qQ9ibgyFa12_ctASvxIMj2kVlFJ16OwCBaTSozx602wF8XSd4i1RSg15fOw4q7WEbmiMlWQw-YwkQih6p8qM9Bg45AcrM0uQrpXu4anMgWRu3qnJeh80h9_lH-pZFVCYWwUamjxbSMFgX0PED5CQtJKetZxsQShgDHfJeC6ezyXBkeQEYS9RHUd2zOrMJuDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار الانفجارات العنيفة داخل مقرات المعارضة الكردية الإرهابية في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85830" target="_blank">📅 01:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bba43befb.mp4?token=Gm-QpYkbeZ9W-wAQuVHAGPwDma6D8F_Uvr-kWkr_MGFfsloUkNFgLREN9Hal5OkkJ32LdZaY7hjja_YlQE0C4PeqBto3LyJ6hQsDGea9l5kQcvN58Bp6yEL9gI0s9MSMvbLYXmUrWChqFqiMhLY7QrAhR0zBREHvXyjezcC4N1fzriKZ0qtxyTjkxpDyslBbx5V7KNBb-3Bms01meNF7JfnBDlIwRck0d2DRS0aXbE5aSukw5LWVoWkRDlSBWy8pm7H48QMofkibeJEBXOrfIeVJVgb9bG_juOsMtkVlzzVi2PUxVqHWL0n0zdUcakwpdC9lyuHNFIdBvZthEn1e5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bba43befb.mp4?token=Gm-QpYkbeZ9W-wAQuVHAGPwDma6D8F_Uvr-kWkr_MGFfsloUkNFgLREN9Hal5OkkJ32LdZaY7hjja_YlQE0C4PeqBto3LyJ6hQsDGea9l5kQcvN58Bp6yEL9gI0s9MSMvbLYXmUrWChqFqiMhLY7QrAhR0zBREHvXyjezcC4N1fzriKZ0qtxyTjkxpDyslBbx5V7KNBb-3Bms01meNF7JfnBDlIwRck0d2DRS0aXbE5aSukw5LWVoWkRDlSBWy8pm7H48QMofkibeJEBXOrfIeVJVgb9bG_juOsMtkVlzzVi2PUxVqHWL0n0zdUcakwpdC9lyuHNFIdBvZthEn1e5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشوب حرائق واسعة داخل مقرات المعارضة الكردية الإيرانية في محافظة أربيل العراق عقب استهدافها بالطيران المسير الانتحاري.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85829" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f8527a49.mp4?token=bSU3VvVu32uSuvKTsC9HUcg5d0u79fSv1hbgqVXTohZZiLfu0z0a2mt0dCrNdHztgGdBBsHungx84bKX4zM6o0q6XtSoA2MJtlnQkyvcX5aAI1gYsx2AOXJcKh1xokl4nl9gyf6Zq4C6QpqMzjnMcxsvd7xDxlwbrmTsxSWqYZEAOJUknkwgFCtQnyhXn_nvWuUvxDf7s6W0DDMQz21j4-m61Sdo0wFaTWzGKLVhHUAOMqLyWcZZ74VBIXFbRFm-xSJ8iGXKLMzzSyEYLUb_ij1SkndxAV8KwlCTbNsj-Ip1t9d4_eNpepSExWxDQCxq3ph691G_e77zvKINpbvGag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f8527a49.mp4?token=bSU3VvVu32uSuvKTsC9HUcg5d0u79fSv1hbgqVXTohZZiLfu0z0a2mt0dCrNdHztgGdBBsHungx84bKX4zM6o0q6XtSoA2MJtlnQkyvcX5aAI1gYsx2AOXJcKh1xokl4nl9gyf6Zq4C6QpqMzjnMcxsvd7xDxlwbrmTsxSWqYZEAOJUknkwgFCtQnyhXn_nvWuUvxDf7s6W0DDMQz21j4-m61Sdo0wFaTWzGKLVhHUAOMqLyWcZZ74VBIXFbRFm-xSJ8iGXKLMzzSyEYLUb_ij1SkndxAV8KwlCTbNsj-Ip1t9d4_eNpepSExWxDQCxq3ph691G_e77zvKINpbvGag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی در مقرهای تجزیه طلبان تروریست در اربیل عراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85828" target="_blank">📅 01:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85827">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a82d562b.mp4?token=T1QCXLvI4xwdr9R_9A9fRr9v52f2LQB5oywS7VMGSjBRGa9uyUK6dlCh67KWpl646tVSGedERedi3SX0-XkOeu-Lzg-X3zXwQ7c_VGLMp4b3ogNOaThenrL-lfOwk5Px6IESQq2aU7jzrABe8qCuKm0L4mfllzV1NMdkwd6Kmsj156l6Ayo-OcsXE4RF7iZpdrySEGwboTR40dzqgAFpx_2s9TQuAgIlLyJllcKw29n4uvMjubGC-TDizQ-1Z3th30YGAQhWWQ56cDW_jWNIYcIOn1iz-pcOGMpYQIUbVcfD62Je-UgD6JupzNNz1ee5vdwHgx68fGEXtoEV_TQLEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a82d562b.mp4?token=T1QCXLvI4xwdr9R_9A9fRr9v52f2LQB5oywS7VMGSjBRGa9uyUK6dlCh67KWpl646tVSGedERedi3SX0-XkOeu-Lzg-X3zXwQ7c_VGLMp4b3ogNOaThenrL-lfOwk5Px6IESQq2aU7jzrABe8qCuKm0L4mfllzV1NMdkwd6Kmsj156l6Ayo-OcsXE4RF7iZpdrySEGwboTR40dzqgAFpx_2s9TQuAgIlLyJllcKw29n4uvMjubGC-TDizQ-1Z3th30YGAQhWWQ56cDW_jWNIYcIOn1iz-pcOGMpYQIUbVcfD62Je-UgD6JupzNNz1ee5vdwHgx68fGEXtoEV_TQLEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملیات لت و پار کردن تروریست‌های تجزیه طلب در شمال عراق ادامه دارد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85827" target="_blank">📅 01:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85826">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3b235c206.mp4?token=VcL7fyJ0_R6To0dAB7vkHav-oEzszKC-JhaR5bl01sxOnqKwBP4uPvmdi8s3H3hQdWCrQACjfn_5O2lKytAQ-Hz94aU2OEAMUSWA92X_frebc_5ZhxTSef6qUklhemTgM8F9BPFjcH6TO4VQff6EWbWq0lR-Ts1-iBvJmaWw4HouDuCHOmLBMnf-Om_Zsr6JyV5_T6K1SUAN7O8uJHzuhpC9Ixxw0Xcl4JmE7ZICV38mCkxpu9im5KFFfOxq0LYz5sKCLkeR250fnQG58--CUS0PdaDFoRtS8VGUv_9YGZ0qf2ohx3ImHhZXNcEBfl3aiUNGplrUqm13ysok3iDG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3b235c206.mp4?token=VcL7fyJ0_R6To0dAB7vkHav-oEzszKC-JhaR5bl01sxOnqKwBP4uPvmdi8s3H3hQdWCrQACjfn_5O2lKytAQ-Hz94aU2OEAMUSWA92X_frebc_5ZhxTSef6qUklhemTgM8F9BPFjcH6TO4VQff6EWbWq0lR-Ts1-iBvJmaWw4HouDuCHOmLBMnf-Om_Zsr6JyV5_T6K1SUAN7O8uJHzuhpC9Ixxw0Xcl4JmE7ZICV38mCkxpu9im5KFFfOxq0LYz5sKCLkeR250fnQG58--CUS0PdaDFoRtS8VGUv_9YGZ0qf2ohx3ImHhZXNcEBfl3aiUNGplrUqm13ysok3iDG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق للحظة إستهداف مقر تابع للإنفصاليين في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85826" target="_blank">📅 00:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85825">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/decaacf8b1.mp4?token=PhixCQ-HlO5kNvSy8xVCa9z1mInNXemD9_MEn78ShO8zZZpysPqWcBaxaRZYrVM8UEG6DPpepouCkZvO1iGItdwrMTGTTpyj0MYPLhP1zubyCuCLW_oFjsFcV1BbYhDy2LuGU5kMiR-Ywr9NN9knmcR1bNvJJwkHPKm01efeG6HIXn9in2Hm5doEhFcnRFviOaoFt1hHxxE7-kPtsdg2jkGfhTgv9vmR8cJx5ykkJGuk2gHceQQ-gjWpZJUKcAqppysBakKghvJwCkWo_606pJBDeom1Vosdo4LRqRVqNxZCzmlg0UhcSeAg-o_AUeLd9iAxAbV29wgv_FIEaJVkpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/decaacf8b1.mp4?token=PhixCQ-HlO5kNvSy8xVCa9z1mInNXemD9_MEn78ShO8zZZpysPqWcBaxaRZYrVM8UEG6DPpepouCkZvO1iGItdwrMTGTTpyj0MYPLhP1zubyCuCLW_oFjsFcV1BbYhDy2LuGU5kMiR-Ywr9NN9knmcR1bNvJJwkHPKm01efeG6HIXn9in2Hm5doEhFcnRFviOaoFt1hHxxE7-kPtsdg2jkGfhTgv9vmR8cJx5ykkJGuk2gHceQQ-gjWpZJUKcAqppysBakKghvJwCkWo_606pJBDeom1Vosdo4LRqRVqNxZCzmlg0UhcSeAg-o_AUeLd9iAxAbV29wgv_FIEaJVkpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/85825" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85824">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85824" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85823">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a653f7d251.mp4?token=QlBrbwggx8p-ZOEU7iXrW2A9JJ7XJKXsGlMi2T-oNq5n0GSztYm-6aeVr4bWd9OjAvBBDE6KJ96KlrKks5cywAa_sO-Ti3NwcTOq6B3g0byWwUf1dnVhFhJZuKh3QVnYV8_7_6ujCFSykS6g8fxAFk6XdBLbibvWX3HM1CnMYjVkz4ycGU58gW5wa10VegQHdnkyn8cmqdfPWHVqHFZlPknJ_DWzfcnmHRVJ2wievbt7jcIxIvSUaWhymuBao6QBtIpnh9ZposdhWyy_Q7VOHtn6qEjexrqhTXgKsAL6IaBS4CTxhDTh04pssQ6ttNpwNqXaw8_EGW9i9HjGsXO-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a653f7d251.mp4?token=QlBrbwggx8p-ZOEU7iXrW2A9JJ7XJKXsGlMi2T-oNq5n0GSztYm-6aeVr4bWd9OjAvBBDE6KJ96KlrKks5cywAa_sO-Ti3NwcTOq6B3g0byWwUf1dnVhFhJZuKh3QVnYV8_7_6ujCFSykS6g8fxAFk6XdBLbibvWX3HM1CnMYjVkz4ycGU58gW5wa10VegQHdnkyn8cmqdfPWHVqHFZlPknJ_DWzfcnmHRVJ2wievbt7jcIxIvSUaWhymuBao6QBtIpnh9ZposdhWyy_Q7VOHtn6qEjexrqhTXgKsAL6IaBS4CTxhDTh04pssQ6ttNpwNqXaw8_EGW9i9HjGsXO-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرة اخرى استهداف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85823" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85822">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مشاهد اخرى لاستهداف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85822" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85821">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79187ad90d.mp4?token=oU01AFasdMcpJYFeFUwiWJ1dsa6CGpqjDHLb_TOUOlSpyCderRZOcIYuoyGrL0OOTVzCkg4i4XxSBjQxW0fL1E1VE4iTMDqPJjk8DGPNdaHaef0IMsqLGI6vSi-bVcRhhg8Lg6nID3xJQbmGnZIgOK7OnNMw__POJQDtA2bKZyo4tfbfl94r1njSlqZ-fP9xePb-5y79A_fnBDxqrIx_A9MUHsdv8PcsTGsDZ8L3_L_-ZY9vv3gkGVhRfF16nflbV7kPhJbQKz1s6CdXbOy7mU3E0Us9DHcYwRe8fdSn9g6dVcNPwyC4NbS0eXnZEwBJEjKA2KJwV4VebMwGfDLXdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79187ad90d.mp4?token=oU01AFasdMcpJYFeFUwiWJ1dsa6CGpqjDHLb_TOUOlSpyCderRZOcIYuoyGrL0OOTVzCkg4i4XxSBjQxW0fL1E1VE4iTMDqPJjk8DGPNdaHaef0IMsqLGI6vSi-bVcRhhg8Lg6nID3xJQbmGnZIgOK7OnNMw__POJQDtA2bKZyo4tfbfl94r1njSlqZ-fP9xePb-5y79A_fnBDxqrIx_A9MUHsdv8PcsTGsDZ8L3_L_-ZY9vv3gkGVhRfF16nflbV7kPhJbQKz1s6CdXbOy7mU3E0Us9DHcYwRe8fdSn9g6dVcNPwyC4NbS0eXnZEwBJEjKA2KJwV4VebMwGfDLXdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف يستهدف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85821" target="_blank">📅 00:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85820">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af9e5cd42.mp4?token=aw2F5QIRXMJHbaTUU54DIncsiyxZR2MQgS6BTkxx8c315zl3AkW4gEu5ZF8bUjBZeTnnCwOx_tV-DJ_OtjDREGzR7fIBA0owZ4LOOh6SA_VqJKi2rshOJ_XMAbC87zF77aJI1HcfYtyPZZWm5A6LyzdtbbbtGXYwZWxwg3fV5IKAot3kvCbEZviQLr6E4YEeaCxiWrUAFXWG1J_DjRqaUhIMD3L56FCZis7qnbvT_Qf34D0uwLmmt4ptPKfHIbtfOdJuG6KWrRni-pR77yeLnp3kTpVZzQpMhF9ylnkXL1cPOg56O60rFbcvgO1nAhENogJz9ijA8yGV7ms92oJOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af9e5cd42.mp4?token=aw2F5QIRXMJHbaTUU54DIncsiyxZR2MQgS6BTkxx8c315zl3AkW4gEu5ZF8bUjBZeTnnCwOx_tV-DJ_OtjDREGzR7fIBA0owZ4LOOh6SA_VqJKi2rshOJ_XMAbC87zF77aJI1HcfYtyPZZWm5A6LyzdtbbbtGXYwZWxwg3fV5IKAot3kvCbEZviQLr6E4YEeaCxiWrUAFXWG1J_DjRqaUhIMD3L56FCZis7qnbvT_Qf34D0uwLmmt4ptPKfHIbtfOdJuG6KWrRni-pR77yeLnp3kTpVZzQpMhF9ylnkXL1cPOg56O60rFbcvgO1nAhENogJz9ijA8yGV7ms92oJOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار طيران المسير في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85820" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85816">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207797b8fe.mp4?token=iVImswSfPVua3wpM_BpGVhVev7We1o5KllgobKfXqhTUHJ2WUqmBvarkd4n7c5r9tGW3uM2NOrAHOXTadkVcclqjMGBXT7H5uB6tCcMmNssky7wv0uLjpV2JABnp1aAnnm1gJZRXqA_rUJ69WHnlWdh4j7hKKOSn5viYPzYdxb2SqphGhHv0C_h-PhfD2qq-ZKxk51pcSa_wFKjX0Xa-twwUHZudBgmmLn82LtVzcKHoILcq6yt3teojRqosyO7IK4uZ1PO-ZNRqXkjOjab9-NvYJQJSZ37IVu24ypmfTgmZYc24bIC1-krBCqcmG63FCGDtRANRIBBh5BqhHNIw7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207797b8fe.mp4?token=iVImswSfPVua3wpM_BpGVhVev7We1o5KllgobKfXqhTUHJ2WUqmBvarkd4n7c5r9tGW3uM2NOrAHOXTadkVcclqjMGBXT7H5uB6tCcMmNssky7wv0uLjpV2JABnp1aAnnm1gJZRXqA_rUJ69WHnlWdh4j7hKKOSn5viYPzYdxb2SqphGhHv0C_h-PhfD2qq-ZKxk51pcSa_wFKjX0Xa-twwUHZudBgmmLn82LtVzcKHoILcq6yt3teojRqosyO7IK4uZ1PO-ZNRqXkjOjab9-NvYJQJSZ37IVu24ypmfTgmZYc24bIC1-krBCqcmG63FCGDtRANRIBBh5BqhHNIw7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار محاولات الاعتراض والتصدي لمسيرات في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/85816" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85814">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4a468f9f.mp4?token=pO30iffqAneag2xNybX1d5cjdAu30ScN9qLrYfQ5Cp0nEmhyiB4ZDF9XTQ_iXM2Ua1Kwi3ktN6jX27W0ReEOpUKouZhPSp5OIoEbeJ2U9_INszwTtDtmIfBc5Fbw0hA_T9MQm3RuaEgHL_7tqsl-8Hd1dw9nqLfSlJAzXzZ_L8XtXePjPgoqFDAbDD-6fMmIIn8sWlCQ347PITmVth1ZHZH3Gn8erJeTRD7f7POVPiTki2GtgUl3xSx0s313XmBh2N-EmXIjqyQjwnqU0DOWB1ugPh2DmrrhOamGuWroCighNgO842GnortI14HcZsWLzu7Ez3lNYTxsvTcO22HFGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4a468f9f.mp4?token=pO30iffqAneag2xNybX1d5cjdAu30ScN9qLrYfQ5Cp0nEmhyiB4ZDF9XTQ_iXM2Ua1Kwi3ktN6jX27W0ReEOpUKouZhPSp5OIoEbeJ2U9_INszwTtDtmIfBc5Fbw0hA_T9MQm3RuaEgHL_7tqsl-8Hd1dw9nqLfSlJAzXzZ_L8XtXePjPgoqFDAbDD-6fMmIIn8sWlCQ347PITmVth1ZHZH3Gn8erJeTRD7f7POVPiTki2GtgUl3xSx0s313XmBh2N-EmXIjqyQjwnqU0DOWB1ugPh2DmrrhOamGuWroCighNgO842GnortI14HcZsWLzu7Ez3lNYTxsvTcO22HFGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء محافظة اربيل تشتعل اثر الهجوم على مقرات الاحزاب المعارضة الايرانية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85814" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85813">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d950af84df.mp4?token=oHxCGLITYAIwuNOOG7NAo_PBB6jsUWpYOyMdTR0MMBeM2smmELtWxXOwZtMTevbR1XgLwd_wCiL_B6pI8QWvZsU7aqZPraRWMryShFR_Hk0kqDDQw-R8dPsPSiOC2sAFrdpbItZON64z7x7LEfemVS8ExgsQ_UXu3vQ2R_lMv_TnoW09OtEhXTlWaR-fx6cP0E-oQJsNkKk1Im3AQPMumIy5TfLYqephJd9-fNaovTYoXD6vvk8U6Eehd8KXESPCIgBKPk0PINX8ZWvxOQSocLKR5b1Pk_sGBhZuPsPnfpqVKwJN5WNxhbxs7Wvhk9vwJ_r4uulsBBZbW6nZplXEMkdlp5kYvBZEj1b15bCbSEVM4h_Eh47HwskoKNFOHfm7x3KuMdlW1h0pG_y_AWQ8VC-k9hgu3IHDJ1x05LENrErlX6fb8omKJXscS7JWhPooUgCwGN9wTV5QpMp_I1mg1fND6ZV24ddpM33LUzu3bcP9RrgMaw2RDdUMgCxnO_Rk6T_HCkG6e6oNo2YkS49ojhk_M6D3EGQNP_qEJ6ZcwGAYZjjUMiYBkQ1HHcewxSa-pEO0RohMr1DuA3GCpypZID_FR68_cy5elpKPpa4QtbSdcxklMuAGaCnLozmngBk6Cu81mFdBp48pKi9XW3ojI6mtCfoH_zyNKpITSvJpQcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d950af84df.mp4?token=oHxCGLITYAIwuNOOG7NAo_PBB6jsUWpYOyMdTR0MMBeM2smmELtWxXOwZtMTevbR1XgLwd_wCiL_B6pI8QWvZsU7aqZPraRWMryShFR_Hk0kqDDQw-R8dPsPSiOC2sAFrdpbItZON64z7x7LEfemVS8ExgsQ_UXu3vQ2R_lMv_TnoW09OtEhXTlWaR-fx6cP0E-oQJsNkKk1Im3AQPMumIy5TfLYqephJd9-fNaovTYoXD6vvk8U6Eehd8KXESPCIgBKPk0PINX8ZWvxOQSocLKR5b1Pk_sGBhZuPsPnfpqVKwJN5WNxhbxs7Wvhk9vwJ_r4uulsBBZbW6nZplXEMkdlp5kYvBZEj1b15bCbSEVM4h_Eh47HwskoKNFOHfm7x3KuMdlW1h0pG_y_AWQ8VC-k9hgu3IHDJ1x05LENrErlX6fb8omKJXscS7JWhPooUgCwGN9wTV5QpMp_I1mg1fND6ZV24ddpM33LUzu3bcP9RrgMaw2RDdUMgCxnO_Rk6T_HCkG6e6oNo2YkS49ojhk_M6D3EGQNP_qEJ6ZcwGAYZjjUMiYBkQ1HHcewxSa-pEO0RohMr1DuA3GCpypZID_FR68_cy5elpKPpa4QtbSdcxklMuAGaCnLozmngBk6Cu81mFdBp48pKi9XW3ojI6mtCfoH_zyNKpITSvJpQcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاقات دفاعية في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85813" target="_blank">📅 00:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85812">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec823fea58.mp4?token=hfFSfRDbyEzmHn01ZzwaoC4rLSyFiznGfPg8AzpOguQk3eq5n6Nc7eK8ZJehHf-JChfawQh2mgD1-B5gywKBGxnpu4sTtqMO5mEXrvVRF9xsfRYzlWGHinhXIQd7KZduv21zNNNWKaeZWnCshsejNKU3kZQKCqHB5CWezL3p6qlZaE3VuPZKNRjvmdXjodFwSH67Aq_d1ivKWgyJagxNB2cwgcqI0azmQXmhKtW-S6jxAGUol1gagwf8uJRJ_MhHXG9BeMeu4f8FTOVuW31jHVQ63Guk28sqR_EgU2IoPxHCFmvJqHJnfA-zgBX_dRqaX5FEkX1fZZhcxz0jFBphsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec823fea58.mp4?token=hfFSfRDbyEzmHn01ZzwaoC4rLSyFiznGfPg8AzpOguQk3eq5n6Nc7eK8ZJehHf-JChfawQh2mgD1-B5gywKBGxnpu4sTtqMO5mEXrvVRF9xsfRYzlWGHinhXIQd7KZduv21zNNNWKaeZWnCshsejNKU3kZQKCqHB5CWezL3p6qlZaE3VuPZKNRjvmdXjodFwSH67Aq_d1ivKWgyJagxNB2cwgcqI0azmQXmhKtW-S6jxAGUol1gagwf8uJRJ_MhHXG9BeMeu4f8FTOVuW31jHVQ63Guk28sqR_EgU2IoPxHCFmvJqHJnfA-zgBX_dRqaX5FEkX1fZZhcxz0jFBphsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء أربيل تعج بأصوات الطيران الحربي والمسير الإنتحاري في هذه الأثناء</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85812" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85811">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d05b791a.mp4?token=WPSp9jgJp5XPPP6ZNqbB6gOtHFX9n6uSapMQ5Ihr1nq7nsZOKXYRa5BQWm8GGcoXrOweY6s0EnIi6q-zXOwXkmgCybNFZGxEpnHgyKhZBi1R4BgVDHNNaVpPaO96qv_FMhD6HprPPfgKYQ2EjDYh8lrN4ZWB5PbWa118PnMfQg8Tbt9cRXYhEvf53WjQv8A_0bc1s1sBGXG8Mt20PceMABZDDU6uq4ONAGkn6fHbwcAUGq2Mjf6OigX0EfTqwuThzOuH3JxGLl8x4vTaTwVuNSK0TaONvW1g9zzifyuhiUEOlK2y-QEMCY0Lx944OUp2CBc9ldYc_R0-oAD3PAsioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d05b791a.mp4?token=WPSp9jgJp5XPPP6ZNqbB6gOtHFX9n6uSapMQ5Ihr1nq7nsZOKXYRa5BQWm8GGcoXrOweY6s0EnIi6q-zXOwXkmgCybNFZGxEpnHgyKhZBi1R4BgVDHNNaVpPaO96qv_FMhD6HprPPfgKYQ2EjDYh8lrN4ZWB5PbWa118PnMfQg8Tbt9cRXYhEvf53WjQv8A_0bc1s1sBGXG8Mt20PceMABZDDU6uq4ONAGkn6fHbwcAUGq2Mjf6OigX0EfTqwuThzOuH3JxGLl8x4vTaTwVuNSK0TaONvW1g9zzifyuhiUEOlK2y-QEMCY0Lx944OUp2CBc9ldYc_R0-oAD3PAsioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاقات دفاعية في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/85811" target="_blank">📅 00:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85810">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c719c4ee4c.mp4?token=tNnL8O_N3ZiODH07pNTB7fzJmEwkjlOqRUD4-2NHdS7GqOLhGPhheDMIE3iZMCvUwyVpRIyta1w87cCiOIs_yQgneNMRlJ9P9SoKkVUHJzs8ki_oddEtjiHpRYMJqmcw7g4YhpFfm2StCzktkRtF7BmPM--zmOIk5mE0FRGKpByWgFCxtRxzp11jPRIgDu8kXED7WgPBXQjtRI0hsay5MpJIaZejwqO8uH0rRGCkxyhKgES7qOzbSguJfu4KI0jNuZF8K7DFigG5Lw-E1WZMaNmkXonYbVtGGVE_PUGF_Jv05M7PJvAC_lAP6UVYleS4aQFHcxMB85tO_v0WuNMA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c719c4ee4c.mp4?token=tNnL8O_N3ZiODH07pNTB7fzJmEwkjlOqRUD4-2NHdS7GqOLhGPhheDMIE3iZMCvUwyVpRIyta1w87cCiOIs_yQgneNMRlJ9P9SoKkVUHJzs8ki_oddEtjiHpRYMJqmcw7g4YhpFfm2StCzktkRtF7BmPM--zmOIk5mE0FRGKpByWgFCxtRxzp11jPRIgDu8kXED7WgPBXQjtRI0hsay5MpJIaZejwqO8uH0rRGCkxyhKgES7qOzbSguJfu4KI0jNuZF8K7DFigG5Lw-E1WZMaNmkXonYbVtGGVE_PUGF_Jv05M7PJvAC_lAP6UVYleS4aQFHcxMB85tO_v0WuNMA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء أربيل تعج بأصوات الطيران الحربي والمسير الإنتحاري في هذه الأثناء</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85810" target="_blank">📅 00:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85809">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/065589ca73.mp4?token=JJ1kjfQUoH1x2uc1emWvgQSIPJ26XN78DTcYkLJ17btDQvnJzRJjXYAoO6lurkwrHbRDd3fjnr2hpsrNuTRFYGkRc7kAX6xe6cSkXL5nHlN0UozeOwk8JVL3mVcdXZki5LaNtiyd86LQuQfZMsGbNwuvOrHGHSpcoClYXN6pXGBDwQ9BiU6Qmd4wvm0GReFH9uxKQ1IS3yHJ1RVkCcpftKBYsEvO2voNZIf1kQBOwcT7FCePTRkHxZNcejlffDOZajZGIN2tWj9Kh3mf-KEE5P0KTGcnGiUzzmRQWx7R3hofbA7LFRTeUVDQDU3zfRAcd5qcL5Z3REWaxH_W9s-wyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/065589ca73.mp4?token=JJ1kjfQUoH1x2uc1emWvgQSIPJ26XN78DTcYkLJ17btDQvnJzRJjXYAoO6lurkwrHbRDd3fjnr2hpsrNuTRFYGkRc7kAX6xe6cSkXL5nHlN0UozeOwk8JVL3mVcdXZki5LaNtiyd86LQuQfZMsGbNwuvOrHGHSpcoClYXN6pXGBDwQ9BiU6Qmd4wvm0GReFH9uxKQ1IS3yHJ1RVkCcpftKBYsEvO2voNZIf1kQBOwcT7FCePTRkHxZNcejlffDOZajZGIN2tWj9Kh3mf-KEE5P0KTGcnGiUzzmRQWx7R3hofbA7LFRTeUVDQDU3zfRAcd5qcL5Z3REWaxH_W9s-wyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اربيل لحظة الاستهداف مقرات احزاب المعارضة</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/85809" target="_blank">📅 00:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85808">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8944cda6.mp4?token=rHzIpn7OIlI--SBAJeeMPgE45QFsOLSqo6b0w3iboFw3fpKfxoQJ9ny1vuJhjfpSHFcE27ffCa5EXI2Gq1fQHsylLDvO1nVEw7XUW5SIki_s9rh_YfecU-v0ysn_ib--TLQXSDpPwzumQEmL9LEg4ZMuBzi9Ok7JtLqx5_wAIUJtCnPGlVIXTcwqCzBbHnum4KrfYffZrkBFRZFhpIKFqcSDykvkbMtvP0YRVLppDzPEqPY0wZ-DvIKrzLliqWDkbWsZaJ4W4qplN7q_nnW8MOqzD6CDWFiFT5lZJfWkoIS_nYU5aVjrHHlGpaYqjbHdlI2qoSNnpC4Zva3Un98pBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8944cda6.mp4?token=rHzIpn7OIlI--SBAJeeMPgE45QFsOLSqo6b0w3iboFw3fpKfxoQJ9ny1vuJhjfpSHFcE27ffCa5EXI2Gq1fQHsylLDvO1nVEw7XUW5SIki_s9rh_YfecU-v0ysn_ib--TLQXSDpPwzumQEmL9LEg4ZMuBzi9Ok7JtLqx5_wAIUJtCnPGlVIXTcwqCzBbHnum4KrfYffZrkBFRZFhpIKFqcSDykvkbMtvP0YRVLppDzPEqPY0wZ-DvIKrzLliqWDkbWsZaJ4W4qplN7q_nnW8MOqzD6CDWFiFT5lZJfWkoIS_nYU5aVjrHHlGpaYqjbHdlI2qoSNnpC4Zva3Un98pBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اربيل لحظة الاستهداف مقرات احزاب المعارضة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85808" target="_blank">📅 00:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85807">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الإطار التنسيقي:
عبرّ الاطار التنسيقي عن موقفه الثابت لدعم الجهات المختصة في محاربة الفساد وتعضيد جهود الحكومة في ملف حصر السلاح بيد الدولة.
وشدد الاطار التنسيقي  على رفضه المستمر لاستخدام اراضي الدول في الاعتداء على الدول الآخرى، واغراق الجميع في صراع لا يخدم اي من الاطراف.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85807" target="_blank">📅 00:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85806">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
انباء متداولة عن استهداف حقل كورومو في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85806" target="_blank">📅 00:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85805">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
🇺🇸
نشرت صحيفة أميركية تقريرًا يستعرض آثار العدوان الأميركي على إيران والتداعيات الاقتصادية التي انعكست على دول العالم بدءًا من ارتفاع أسعار الوقود والطاقة وصولًا إلى زيادة أسعار المواد الغذائية وسلاسل الإمداد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85805" target="_blank">📅 00:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85804">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef69381f74.mp4?token=c88_R_uFYXnXfe6prcr5huxO4zk-FSEbQ-slNNcjCFOnYX9bO1EYzOqtserwxyrN84za9q3R8AV5poIn5K480__OCPdCTj_zFWlkxlJHkwhGs6dB4menp9IPtkLxTdOUfnV9OwVozXqiDSJWCA5HRQJ5OwXJZJTlOF1oaQc18bpgNQCLqh0iBUBpfc2Wcg7nimHno4Bjh-O-FOk3-V4qihiQ3hlwOTnO2p8pDWbJmWKxB6FQji-dWFqoell2jhiraSiqlOz-Q34AY8RYxYaTXuLxxym16MRHCHMnhDMBbgm_6TallZ1syQSIQIeDQQMyFyzEfJ6jmfHYfdY2TJ7EHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef69381f74.mp4?token=c88_R_uFYXnXfe6prcr5huxO4zk-FSEbQ-slNNcjCFOnYX9bO1EYzOqtserwxyrN84za9q3R8AV5poIn5K480__OCPdCTj_zFWlkxlJHkwhGs6dB4menp9IPtkLxTdOUfnV9OwVozXqiDSJWCA5HRQJ5OwXJZJTlOF1oaQc18bpgNQCLqh0iBUBpfc2Wcg7nimHno4Bjh-O-FOk3-V4qihiQ3hlwOTnO2p8pDWbJmWKxB6FQji-dWFqoell2jhiraSiqlOz-Q34AY8RYxYaTXuLxxym16MRHCHMnhDMBbgm_6TallZ1syQSIQIeDQQMyFyzEfJ6jmfHYfdY2TJ7EHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
What if they come back ?</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85804" target="_blank">📅 23:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85803">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالمقاومة الاسلامية في العراق</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIKfCqZvUDnNyBfJVOx3rMz5nNnGtQHi3oWN1UI2TAtcoSQGX2RX6kykgV1iP9DFwhRvYq3xfUiDLI8zdmIRqch4aeIogi-hDYyLXdJC3eXDpcZSKJrWj7FoAo9b-f1swzzlD-Te1OThRE-xLYCbzkrWlKlowbHKBTOOrQhw-fpU-x5Qixr74rPRsNNN9yJS36vg8T44zT0aQV9MW9kwCOGZBPG2BIIpBLfiJ-z-JGT2GkWOy55gucjaV7jkiR5urJXtR73jVoIjY2_nd2xKHKjuDQqvPjLJi5Gn5mf_8F75ahv8DF_KlbOBDWsvHFgRUDaPW5hvTF9gzQecFWY3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
(إِنَّمَا يَفْتَرِي الْكَذِبَ الَّذِينَ لَا يُؤْمِنُونَ بِآيَاتِ اللَّهِ ۖ وَأُولَٰئِكَ هُمُ الْكَاذِبُونَ)
بينما يواصل الكيان السعودي رمي الاتهامات نحو العراق، زاعماً أنه المصدر لقصف منشآته البترولية في الشرقية والرياض، فإن هذا الادعاء لا يزيدنا إلا يقيناً بأن العداء للعراق وشعبه سمة لاصقة بهذا النظام.
إن هذه التخرصات ما هي إلا محاولة لتبرير العجز عن الرد على الضربات اليمنية الموجعة التي طالت عمق بُناهم التحتية، خوفاً من طبيعة الرد اليمني القادم.
إننا في المقاومة الإسلامية نُوجه للنظام السعودي تحذيراً واضحاً، نُعلن فيه أن أي فعل سعودي أحمق سيُجابه بردٍّ قاسٍ، يجعلهم يعضون على أصابع الندم.
ونقول لهم، وبكل وضوح: إن كان فيكم رجل رشيد، فأنتم أحوج ما تكونون اليوم إلى رفع الحصار الظالم عن الشعب اليمني، بدلاً من توجيه الاتهامات يميناً وشمالاً، لتبرروا بها فشلكم، وتغطوا بها على جرائمكم.
المقاومة الإسلامية في العراق
27 تموز 2026</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85803" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85802">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/naya_foriraq/85802" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85801">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1Gl7Cnmmju1nz52tPNIftPKvVUBAXHA0DbiXDIhBNWM85_csLgywvLuU_4WPwL8RZLqUprSw-AykLx6vlPyp2S1mPYkrV7Opbyl5Qi8bE2PQ4HREF4DWbQVKq6PvckWNnMknhrckPbkZ2IU5_s46RYJK9-RvkRak47lSubW7t1BHOeKqLR-s8qg-4ki1m1JWVhDKWMvkvOBx-tWwuaD887gs7V8PO0ux6Q-1oA-x8WM_PUYiJ5nhi6--YNfFscX2b6jnr8HdtwI8TWEt5QPJdMiKjKMV_YzKqhXr8-n_3glDybam3uUjOh96blBBigL2I7jYhE_DRiSomGpU4Ithw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط طائرة مسيرة أمريكية قرب سد حديثة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85801" target="_blank">📅 23:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85800">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سقوط طائرة مسيرة أمريكية قرب سد حديثة</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85800" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85799">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85799" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85798">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed1a8163b.mp4?token=RgDHbIm-g-wjp5tSlqR1qfNZqmrF4XZYh4I-H928ozsC3wxOrzLX2BkXP-De_ycErfBSBVDzvgG4pkG-daT7vcq_u5VPAZ2FBy5yl0B7FkqpHUJ8q-nWxIjhOR4Ozu4pHpZujCiqPRoRaPUV4qRRR4FADkx8vtPTicueI-SGAIMnoEpzchWRY4OJoamlzreC50CGPst2LMsrGvX-llWrXl--FXlUeDqBCLVy6j72X6Oljfus4Edh1BaEHti6R1Q4WaLDYadfUyyWRzDpIcNGZIXTV4w6vwuwfP7c38cihPCjz01QdWj2RDrXRGrXJFwEvv82Wwr3hWBVctyXDOX9nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed1a8163b.mp4?token=RgDHbIm-g-wjp5tSlqR1qfNZqmrF4XZYh4I-H928ozsC3wxOrzLX2BkXP-De_ycErfBSBVDzvgG4pkG-daT7vcq_u5VPAZ2FBy5yl0B7FkqpHUJ8q-nWxIjhOR4Ozu4pHpZujCiqPRoRaPUV4qRRR4FADkx8vtPTicueI-SGAIMnoEpzchWRY4OJoamlzreC50CGPst2LMsrGvX-llWrXl--FXlUeDqBCLVy6j72X6Oljfus4Edh1BaEHti6R1Q4WaLDYadfUyyWRzDpIcNGZIXTV4w6vwuwfP7c38cihPCjz01QdWj2RDrXRGrXJFwEvv82Wwr3hWBVctyXDOX9nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: لا يمكنك رشوهم. يجب علي هزيمتهم،ونحن نهزمهم بشدة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/85798" target="_blank">📅 23:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85797">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98851fe969.mp4?token=VYD5sEbb3F_-sCFjFARMdJQ-Sh13KNms-YNTkExphNMbOQb2d5FzuAXbY5mn7iSBfxLWGx--amhcfT4e5Y89H2EHeXjliXJbI2uczrzyVmuV4goiVIVFTJFbsMISwLiHLriWN2q-OdIncNklY8kfnuNuoip4xJksBXHS57TQP_iXbWmZq-9Ec619JMtOslxCZfazLlEqKHfMXUGRSbHJGPwxYhyI2-8rqBHtJQi2az1DoRar6wBK19qBjZHxa5WwHcpS7Wcz__YIFnzwbwGKrPTTUuazwETjYKwskAELsOuBX4yMvde-AbtngPnA2thSadTXFT3F44hnghzTOPSiPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98851fe969.mp4?token=VYD5sEbb3F_-sCFjFARMdJQ-Sh13KNms-YNTkExphNMbOQb2d5FzuAXbY5mn7iSBfxLWGx--amhcfT4e5Y89H2EHeXjliXJbI2uczrzyVmuV4goiVIVFTJFbsMISwLiHLriWN2q-OdIncNklY8kfnuNuoip4xJksBXHS57TQP_iXbWmZq-9Ec619JMtOslxCZfazLlEqKHfMXUGRSbHJGPwxYhyI2-8rqBHtJQi2az1DoRar6wBK19qBjZHxa5WwHcpS7Wcz__YIFnzwbwGKrPTTUuazwETjYKwskAELsOuBX4yMvde-AbtngPnA2thSadTXFT3F44hnghzTOPSiPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏أحدهم يصرخ في وجه ترامب قائلاً: "حامي المتحرشين بالأطفال!"</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85797" target="_blank">📅 23:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85796">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07efc12575.mp4?token=RRKJUheXAhdTqL4bvROvs6cfb3ONGeUdtBXYIBVQOjNa9pLhi6ANclSeAegBaCBth7FRiEDIACsQRYc3ux_ioHDSUWagZwCKE1fx-0JoBbiOU5Aqy_laOUYbWXC38IgBePDJUR3yCsiDfnFxCJKF25BToIrUoYw3V2Accid3BJ9PRWRKI7zJolU4LFFDs4lfQYeCV7UvzLaWUsciqAHL0MWyWyIPxmevbGrt17oIiU3Rv4Xax2_z_jI4xUK6pFYrKIPCdZnHI44uRhdepIqeY3Ajvwj7M5iuDGMztwThkOXh8Ap4zmpX8E69JVrmWtNgkEmq-xiGjJeWLLeeL2Z9YWMXZkzafJSXrNVkT8MQN8hpGQa163QwBhIA1-AGPl-SttFdcg6IOW3XDQaMlYEjGqtiJKlp-bdvP7ghqrZb6UNghLUSbIDQSJLONBAp6dGafvI8LtK4D39HcrkdnRODiLtCFY2mgtlIO-7H3hnyyYcMI0-SwSAynSYL_GnrLYN1Z3z6RmcPMj-M5xQASjiXFdeOptmoq7rXvD3IzI1L0gVu83uEsfmzzkRzkU-7eIuHlrN90bf8ac2F4c7i-R5p0CfkUs2vwaGTIz8-NIDLNVnDg-Adr9kE13VcI4V2kfctHgfinC1qjORpOQLpBG4cdtgZFj9e9LH7hU5fafoPWQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07efc12575.mp4?token=RRKJUheXAhdTqL4bvROvs6cfb3ONGeUdtBXYIBVQOjNa9pLhi6ANclSeAegBaCBth7FRiEDIACsQRYc3ux_ioHDSUWagZwCKE1fx-0JoBbiOU5Aqy_laOUYbWXC38IgBePDJUR3yCsiDfnFxCJKF25BToIrUoYw3V2Accid3BJ9PRWRKI7zJolU4LFFDs4lfQYeCV7UvzLaWUsciqAHL0MWyWyIPxmevbGrt17oIiU3Rv4Xax2_z_jI4xUK6pFYrKIPCdZnHI44uRhdepIqeY3Ajvwj7M5iuDGMztwThkOXh8Ap4zmpX8E69JVrmWtNgkEmq-xiGjJeWLLeeL2Z9YWMXZkzafJSXrNVkT8MQN8hpGQa163QwBhIA1-AGPl-SttFdcg6IOW3XDQaMlYEjGqtiJKlp-bdvP7ghqrZb6UNghLUSbIDQSJLONBAp6dGafvI8LtK4D39HcrkdnRODiLtCFY2mgtlIO-7H3hnyyYcMI0-SwSAynSYL_GnrLYN1Z3z6RmcPMj-M5xQASjiXFdeOptmoq7rXvD3IzI1L0gVu83uEsfmzzkRzkU-7eIuHlrN90bf8ac2F4c7i-R5p0CfkUs2vwaGTIz8-NIDLNVnDg-Adr9kE13VcI4V2kfctHgfinC1qjORpOQLpBG4cdtgZFj9e9LH7hU5fafoPWQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏أحدهم يصرخ في وجه ترامب قائلاً: "حامي المتحرشين بالأطفال!"</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85796" target="_blank">📅 22:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85795">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-YmxlsV433GaiboXD11Ef-7Z3RkccI3LZ35xKP_xjTFBsW4plEftr1QePgNgh8JPDbOklM5nBJkEgUtvusLz5Ekm3Hw4fMLf5qX8pgmohagumNWvU5Ag4mTdEHtMoI0AbVh1sq7CPuKuCfNcD0TyXZc--AqiZWOI-m4HQFikjEo9QNoNIaWF8H98b_MXw5KzRAetCE9O2JmTxMspS8iAJCq2K7Ehu0FUwgXzIB2AE8eW3tZZPADJ4JoRepIOG57RVoIeXT10DltdfFgSI1pb6p4pfhpMS-p_jNlEFnpj__vKICiVfxCwSx7fBkbSQfr1EiLbDf6wyR0gr-itYHp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ارتفعت صور شهداء ميناب في شوارع مدينة النجف الأشرف، قرب مرقد الإمام علي (ع).</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/85795" target="_blank">📅 22:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85794">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85794" target="_blank">📅 22:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85793">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
مقر خاتم الانبياء المركزي:
إن الولايات المتحدة، في استمرارها للشر وانعدام الأمن في المنطقة، وعقب فرضها الحصار البحري غير القانوني على إيران، هددت السفن الإيرانية، والسفن التجارية، وناقلات النفط في المياه الساحلية والإقليمية لبلادنا على مدى الأيام الثلاثة الماضية.
نحذر من أن هذا العمل الأمريكي يُعد امتدادًا للحرب في المنطقة، وكما أثبتت القوات المسلحة للجمهورية الإسلامية الإيرانية على أرض الواقع، فإنها لن تتهاون مع أي تهديد أو شر من جيشها الإرهابي، وستتعامل معه بكل حزم.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/85793" target="_blank">📅 22:28 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
