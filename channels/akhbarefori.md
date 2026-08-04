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
<img src="https://cdn4.telesco.pe/file/PSwJLHpxesUkD5ih6mphrrBGB6aQkIzBiSYi8-xxfG0aSiwRDubvV7WnnLyzM6HpOudFGNYwIvNgsCTQ1vU4qBYBqz4DU6picqbjMRVFy15dYXR0hI1sfMCagDmQj1LiTlgVBvpfLbaJtc4TnR6JoyDoAmhtpI2FsmRBQhQ3yi-RjQzb4bH3JgUrUKvLQRV2Bky9E_0ZfrL2V259TukEu6wvRTBiqEYtTWLHD-M5-dc0Z9Hvjr5X4LGKT0pStvxPJ1OIMV_skH56flQiFJi5YSLg3giMgGCzyRVNCFWkG6io7U07YvV1USGb8GF3wao3X6kpg63b-oAb163aqCUoog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.04M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 21:39:20</div>
<hr>

<div class="tg-post" id="msg-678485">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/138531676e.mp4?token=kmGoMkHd1QerZg6vo8RE3RAjjBTTThEQOJkXObAjQmR6FJ2RbUAXJcuMbSHz4MjelBICPfFPH766shtovCa5poFj1VEPQhaYe-2IDZC4UAPPCr9pgYX1oOThtzEhMNYBQPdT6LhFIk6sEyRWIwYUw-L55AuMkoQr4hxKTHJvhAsBE52F3XWDrJ9brF3oMeC8_dkuVsgKvJc9uERG-_GycfdToGp3Xnaejw18PhAxrJKjHo-NQuwGUhlMIAX8lH6xv0oMW5bbTBJ1id8DRDLlXJOA4ibull9XK1ULD9d4CHXo5EGuEJ5H9n68HAJVxAFKS-EUqf9gNmE7KmuxkmHc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/138531676e.mp4?token=kmGoMkHd1QerZg6vo8RE3RAjjBTTThEQOJkXObAjQmR6FJ2RbUAXJcuMbSHz4MjelBICPfFPH766shtovCa5poFj1VEPQhaYe-2IDZC4UAPPCr9pgYX1oOThtzEhMNYBQPdT6LhFIk6sEyRWIwYUw-L55AuMkoQr4hxKTHJvhAsBE52F3XWDrJ9brF3oMeC8_dkuVsgKvJc9uERG-_GycfdToGp3Xnaejw18PhAxrJKjHo-NQuwGUhlMIAX8lH6xv0oMW5bbTBJ1id8DRDLlXJOA4ibull9XK1ULD9d4CHXo5EGuEJ5H9n68HAJVxAFKS-EUqf9gNmE7KmuxkmHc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو پیشنهاد آمریکا برای غزه را رد کرد
🔹
نخست‌وزیر اسرائیل تأکید کرد که این کشور از غزه خارج نخواهد شد تا زمانی که حماس به‌طور کامل خلع سلاح نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16 · <a href="https://t.me/akhbarefori/678485" target="_blank">📅 21:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678484">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: شروط ایران برای بازگشایی تنگه هرمز اعلام شد
🔹
ایران اعلام کرده است که مایل به بازگشایی تنگه هرمز است، اما خواستار حق دریافت هزینه‌های ترانزیت، تضمین‌های امنیتی در برابر حملات آینده، پایان محاصره دریایی ایالات متحده و لغو تحریم‌های نفتی ایالات متحده است.
🔹
ایالات متحده و کشورهای خلیج فارس درخواست هزینه را رد کرده‌اند و اصرار دارند که ایران ابتدا تنگه را بازگشایی کند و ایمنی کشتیرانی و امنیت منطقه‌ای را قبل از هرگونه لغو تحریم یا سایر امتیازات در نظر بگیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/678484" target="_blank">📅 21:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/678483" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
افشای هدف اصلی مذاکرات خفت‌بار بیروت و تل‌آویو از سوی آمریکا
🔹
وزارت خارجه دولت تروریست آمریکا مهمترین هدف مذاکرات خفت بار میان دولت غربگرای حاکم بر لبنان و رژیم صهیونیستی را مقدمه سازی برای توافق فراگیر سازش و عادی سازی روابط میان بیروت و تل آویو عنوان کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/678482" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678481">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ec22fe91.mp4?token=vED25Am2c3E10RYKpqZasPn7KLRiG2atnj5te523UXH7LHxMtOfiZsu8w3UInpY3XLhNUaH8y3AB4bHmjFIOu29crehJquQ0hj6e3b6g6Suiy17gnIplxNWoHhymHCNWB_03-AT8OhCSWyIfE08iJs9VT-_1Gkccp3bEhsQHrL7hvOCujdRHD_X1zexqKEkg4gRQKsvqvXk5-CA_WnyCI0yoyM8tywL7AHa5IgPAoj6Mn4mAcEgtn1vUTXqyCLAhhS9hdsikTS34RO9jbjtdGBSbZ5zTZpSFUORz_Qnql7RIf5H7hyp6tNWVoBMTbwM7FYW1kQtYmpF4OcZ9PjmChg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ec22fe91.mp4?token=vED25Am2c3E10RYKpqZasPn7KLRiG2atnj5te523UXH7LHxMtOfiZsu8w3UInpY3XLhNUaH8y3AB4bHmjFIOu29crehJquQ0hj6e3b6g6Suiy17gnIplxNWoHhymHCNWB_03-AT8OhCSWyIfE08iJs9VT-_1Gkccp3bEhsQHrL7hvOCujdRHD_X1zexqKEkg4gRQKsvqvXk5-CA_WnyCI0yoyM8tywL7AHa5IgPAoj6Mn4mAcEgtn1vUTXqyCLAhhS9hdsikTS34RO9jbjtdGBSbZ5zTZpSFUORz_Qnql7RIf5H7hyp6tNWVoBMTbwM7FYW1kQtYmpF4OcZ9PjmChg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سؤال امیلی گرت‌ویت، عکاس و مستندساز انگلیسی، از مردم دنیا درباره سانسور اربعین!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/678481" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678480">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDLk2WH79zWF9sFFkFPod58CpA9NRI9ON4jx4gZ1N9p4-XYD9MMq6lcjHt424vBUqAECU9WsLFDVmM1o2b0RiKecatZUBHex78kixs3FaMligBqSPktvY0Ua_pxlDJGe_osELnoBM6atKuNjVbd36-wViRt2w9J084O5WryeMvYjC1eiuYEvOYuyyVq7QSPRMN9fcQ-RGCC4gXcFtrs47YfW3ZG7hFJ_feuOyGtOpdmPsoSmMz5HJHbIiDfpAmTul5Vuko1eO_da2O0_O8Cs9SHx3ioZ9qkcKfQLoAMsVKvrFFd3Oh3XdXQxw8Axa_GLsCvKK22RlNvGbtMwUHN5DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عربستان به‌دلیل خسارت‌های اقتصادی، یک تریلیون دلار به یمن بدهکار است
فعال رسانه‌ای حوزه جنگ اوکراین:
🔹
آمریکا در طول ۴۵ سال و نیم گذشته، به‌دلیل خسارت‌های اقتصادی، پنج تریلیون دلار به ایران بدهکار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/678480" target="_blank">📅 21:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678479">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سپاه هرمزگان: از فردا احتمال شنیده‌شدن صدای انفجار کنترل‌شده در اطراف بندرعباس وجود دارد
سپاه هرمزگان:
🔹
از فردا به‌مدت ۳ روز در ساعات ۸ صبح تا ۱۲ عملیات انهدام مهمات عمل‌نکرده در محدودهٔ ایسین و سرخون انجام خواهد شد؛ شهروندان نگران نباشند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/678479" target="_blank">📅 21:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678476">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54678ab5de.mp4?token=H4wCoK51T5DPDTBIvvAIXvgPH16HwgiUSnYj-nVBdIIND118yK_kcM84bF-th4fzAlDMbdxscTIWNoPL4bT1qRyyC0KppunvILrmWVr0JMwTnVcQBanb1D4PGvf_AkMD3sPUm86Tq_mRpKp1Kefj1eHtYGk2j9MQDFw62SGcPUl-I6-9ZdOKzXLgeIw68HSAOeFLF3EPlGGTigD1McrbtX6TDjCZ2rm4_TWFujkZ4vyRvjxWf9beI8vNgdkr6IoRej1-m4C5uWdzbpThs2bwQCZhFoiMTgpScS25ahs_V3YhyRb-qlOQzMnOc0vaOrqSg_8JDOsbZTUllisf3hnjfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54678ab5de.mp4?token=H4wCoK51T5DPDTBIvvAIXvgPH16HwgiUSnYj-nVBdIIND118yK_kcM84bF-th4fzAlDMbdxscTIWNoPL4bT1qRyyC0KppunvILrmWVr0JMwTnVcQBanb1D4PGvf_AkMD3sPUm86Tq_mRpKp1Kefj1eHtYGk2j9MQDFw62SGcPUl-I6-9ZdOKzXLgeIw68HSAOeFLF3EPlGGTigD1McrbtX6TDjCZ2rm4_TWFujkZ4vyRvjxWf9beI8vNgdkr6IoRej1-m4C5uWdzbpThs2bwQCZhFoiMTgpScS25ahs_V3YhyRb-qlOQzMnOc0vaOrqSg_8JDOsbZTUllisf3hnjfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمد انصاری، بازیکن اسبق پرسپولیس: اربعین امسال را به نیابت از رهبر شهید و شهدای جنگ ۱۲ روزه قدم برمی‌داریم/ یاد عزیزانی که سال گذشته در کنارمان بودند، در این مسیر زنده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/678476" target="_blank">📅 21:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
الجزیره: ساعات سرنوشت‌ساز برای تعیین وضعیت تنگه هرمز در پیش است
نورالدین الدغیر:
🔹
طی ساعات آینده احتمال مشخص شدن وضعیت تنگه هرمز و
توافق احتمالی وجود دارد.
این روند به بازنگری واشنگتن در محاصره دریایی و تحریم‌های نفتی وابسته است و می‌تواند زمینه‌ساز ازسرگیری مذاکرات و تمدید تفاهم‌نامه‌ای شود که ۱۷ اوت منقضی خواهد شد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/678474" target="_blank">📅 20:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678473">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79aab0b359.mp4?token=SRwv1PmeI2UZ7wXVLBs0sLhuBfXnGEX8LPpbVbzr7waXsysBJCOI3Kk6nJcODL6CFLT0ykYYTd_s9a7RLCYJrBJhSACONuSqMYEY8ugY7eAY5WzJN4VFL_DguBv0Jh849RH1zhpY3DK58A0XJ8YOxGxRZuEPN1sff0LazMDZFvvdhjyPA7cq89XPr-NM-BrT96XKbGELJnt_2wU4Ai_33dTQKG0sq47IuZWqI7GQ387DrfiH3q-r97iZKOkRM_3tQ0Gb2z0amAYVVi2Lu-xZUXnXrlKoIJUZWd-Glu0H9K0pl9IjHAcekrbi4t3MXnz1STY4eYynbO5951J0KDuWJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79aab0b359.mp4?token=SRwv1PmeI2UZ7wXVLBs0sLhuBfXnGEX8LPpbVbzr7waXsysBJCOI3Kk6nJcODL6CFLT0ykYYTd_s9a7RLCYJrBJhSACONuSqMYEY8ugY7eAY5WzJN4VFL_DguBv0Jh849RH1zhpY3DK58A0XJ8YOxGxRZuEPN1sff0LazMDZFvvdhjyPA7cq89XPr-NM-BrT96XKbGELJnt_2wU4Ai_33dTQKG0sq47IuZWqI7GQ387DrfiH3q-r97iZKOkRM_3tQ0Gb2z0amAYVVi2Lu-xZUXnXrlKoIJUZWd-Glu0H9K0pl9IjHAcekrbi4t3MXnz1STY4eYynbO5951J0KDuWJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید غلامعلی رشید: اختلاف حقوق، سم نیروی انقلابی است
🔹
خدا میداند بین یک نیروی جزء و فرمانده در سپاه چقدر اختلاف حقوقی وجود دارد و آیا فرمانده کل سپاه نیروی خودش را درک میکند یا خیر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/678473" target="_blank">📅 20:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678472">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309a7e5446.mp4?token=pm6SuPrapSPBeLw_CCj9ZXz_H7htWaVcjKinQrspCsO2h25X9e4bBrXD0_i1OlNyuKntLsIpOteBW7l4PERxkDbn6oJGttUqnjAV6VtdXvEhFGXtrT6mh0G11FmKn2bkLbJ0uaBuS7_Fvj-AQyDTx_SoROQRhyLDxk_LGGnxftzHzGDS2CXWI6BQPtZwJ2ibBSeyGMa18yfTucMAg5FGIX6ANUk1hgPymLhgkA0qejW_99brUiLmyoPRvbn9zCBbtAazWLw-YnKSyzU6caF--q441qhRjNUaRRMk7Usx7HQof2onZgDPpBiGAUE9f1-kCjrO6gUR5h73AeSO0XPI-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309a7e5446.mp4?token=pm6SuPrapSPBeLw_CCj9ZXz_H7htWaVcjKinQrspCsO2h25X9e4bBrXD0_i1OlNyuKntLsIpOteBW7l4PERxkDbn6oJGttUqnjAV6VtdXvEhFGXtrT6mh0G11FmKn2bkLbJ0uaBuS7_Fvj-AQyDTx_SoROQRhyLDxk_LGGnxftzHzGDS2CXWI6BQPtZwJ2ibBSeyGMa18yfTucMAg5FGIX6ANUk1hgPymLhgkA0qejW_99brUiLmyoPRvbn9zCBbtAazWLw-YnKSyzU6caF--q441qhRjNUaRRMk7Usx7HQof2onZgDPpBiGAUE9f1-kCjrO6gUR5h73AeSO0XPI-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز شربت زعفرانی که تا یک سال شکرک نمی‌زند
!
مواد لازم:
🔹
۶ لیوان شکر
🔹
۳ لیوان آب
🔹
یک سوم لیوان گلاب
🔹
نصف ق چ جوهر لیمو
🔹
نوک ق چ وانیل
🔹
زعفران غلیظ به دلخواه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/678472" target="_blank">📅 20:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3Rvu8eTWDeiJP8o914nDdt_rG5d1OMdjHYnDsdjtEf5BfUJmeSjV1Mqy761RlhpCdGlTp2wu5C2eS9-5X32lMqBcGlukpIKR7hUpapKTUFqn-Rdh_i5nplPMdZjR0bmjHSy3eMHSAKO85NHXSUGoE0ein7kxLMmq03-tMrmHTjMvwWpwVruXuySpU0lv5SP2cfaWbe9EQ_uHexXuh05FOIElmSpfZjGIlPpLS7WZxJuOW8zA4lKw5Ed-bjykmXl6ZzHshluWvWiOlITVOfnIMBVUv7-YTHU6PjZbuBVUDVQyT9NcqIoJfGLTqgUp8hTIrLrUdQkI2qtYOevhbcERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یزید؛ عموی جدید علی کریمی
🔹
علی کریمی این‌بار در پستی از «یزید» به‌عنوان عموی خود یاد کرد؛ اقدامی که با واکنش رسانه‌ها روبه‌رو شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/678470" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56502a6d.mp4?token=MSnV-psUTEfU2FqiFcQvHVna6G_zBey0W2LyfbB5fVg4Y7kFwGpiP_J_gT7v6Fk-OK0MiNgoBM0r1psurSd88wvk8hwPbfeD0TqgzDF4uHCX9vJPnFviGQV5JX58lEgO5LE-q8F9PhhCzVldZMzQdmiwq08cGm1C01_8-ZvpFbvBqZjLkbnMb7FyqQVfjBFCh7CJWajjKDbde-SpbgLfOh7SY_0oJVYh0gKGGMkrHXgd2eosOlEtZuGizq4EBwRrjymLwnMGDb6VOWmJpHHnx2oyI2rzvGYI6fySZU5BtxL4_48rFS2L260XWfs8uAO3IHB5P1pfcuoxmMdwthn-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56502a6d.mp4?token=MSnV-psUTEfU2FqiFcQvHVna6G_zBey0W2LyfbB5fVg4Y7kFwGpiP_J_gT7v6Fk-OK0MiNgoBM0r1psurSd88wvk8hwPbfeD0TqgzDF4uHCX9vJPnFviGQV5JX58lEgO5LE-q8F9PhhCzVldZMzQdmiwq08cGm1C01_8-ZvpFbvBqZjLkbnMb7FyqQVfjBFCh7CJWajjKDbde-SpbgLfOh7SY_0oJVYh0gKGGMkrHXgd2eosOlEtZuGizq4EBwRrjymLwnMGDb6VOWmJpHHnx2oyI2rzvGYI6fySZU5BtxL4_48rFS2L260XWfs8uAO3IHB5P1pfcuoxmMdwthn-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت هشت دانشجوی کره جنوبی حین سر دادن شعارهای ضد آمریکایی در منطقه نظامی
🔹
هشت دانشجوی کره جنوبی پس از متهم شدن به ورود به یک پایگاه هوایی و سر دادن شعارهای ضدآمریکایی، از جمله «بیایید نیروی هوایی هفتم آمریکا را درهم بکوبیم»، بازداشت شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/678469" target="_blank">📅 20:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678468">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ادعای وزارت امور خارجه آمریکا: مذاکرات بین اسرائیل و لبنان در رم تا ۶ آگوست ادامه خواهد یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/678468" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678467">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
رسانه‌های عربی: یک کشتی هندی در فاصله ۱۳ مایلی سواحل الحدیده، پس از هدف قرار گرفتن با یک قایق انتحاری بدون سرنشین، غرق شد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/678467" target="_blank">📅 20:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899728c115.mp4?token=iO-LKEbj84SLVZi96ICv6jH8a39iIhtCbqSNYZJavYW33ate_e3dInrPqB6dKEY07zaJ1LT0N0RZVfdcISEhi8dmC_3IstCiIhuukL6a6dlrhqnDO3OTPQgUv2FzQAFeqkYVfT2j8kkAM5fE-XoHpi0f2CWlOew1XFzaDmKO4BgPPALz6OzRSOCzlQ1FzzzFAuA4iEWcaeIA_gP7X4a0jvOjfX5ByyFWzJUaIYoxsjP8Lxt-HF77LcQLdwEbiVTN9mPC8vxvP49yCVhF8Iv7-FzfbvBhmzcSYXDDuwZARMDACOWjFyMNCNRCUHl2W17WbL3s7qpn3s0OiCm9iV4rNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899728c115.mp4?token=iO-LKEbj84SLVZi96ICv6jH8a39iIhtCbqSNYZJavYW33ate_e3dInrPqB6dKEY07zaJ1LT0N0RZVfdcISEhi8dmC_3IstCiIhuukL6a6dlrhqnDO3OTPQgUv2FzQAFeqkYVfT2j8kkAM5fE-XoHpi0f2CWlOew1XFzaDmKO4BgPPALz6OzRSOCzlQ1FzzzFAuA4iEWcaeIA_gP7X4a0jvOjfX5ByyFWzJUaIYoxsjP8Lxt-HF77LcQLdwEbiVTN9mPC8vxvP49yCVhF8Iv7-FzfbvBhmzcSYXDDuwZARMDACOWjFyMNCNRCUHl2W17WbL3s7qpn3s0OiCm9iV4rNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلوه‌ای از همدلی؛ پرچم ایران، عراق و لبنان بر سفره موکب‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/678466" target="_blank">📅 20:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a241da0c1e.mp4?token=OqXel2s2KY822Vo9lF5kedisXD90lfoYiEDtQcqD6RPaWBTDwknAdOlvqW-MArCE_MvDCWG1uBTcK9P7O1FmwRSyAgnbLeg9bomQUUR3zpSGK3vKZemn3oBRZSZRG5jYmyLoNFn9hywDkTOWPkWWR5QkbX-kyYRxMgTOPEF3c5WPUBeHISNuURsEJHytxYxho0hJ6vXeEtu6-X0LDije8p2jqCF2IAbFkoesiQ3-lCFmyEn0Pkc3Dhaz-ljQM65TwWMegXQFC8Jh1BOmd8isMmnZmuVv2nItmLfs7pTBpzTGrIku7Pun8E3wFHsld10d3YRGvd8Q_H_g8dPoNgAFpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a241da0c1e.mp4?token=OqXel2s2KY822Vo9lF5kedisXD90lfoYiEDtQcqD6RPaWBTDwknAdOlvqW-MArCE_MvDCWG1uBTcK9P7O1FmwRSyAgnbLeg9bomQUUR3zpSGK3vKZemn3oBRZSZRG5jYmyLoNFn9hywDkTOWPkWWR5QkbX-kyYRxMgTOPEF3c5WPUBeHISNuURsEJHytxYxho0hJ6vXeEtu6-X0LDije8p2jqCF2IAbFkoesiQ3-lCFmyEn0Pkc3Dhaz-ljQM65TwWMegXQFC8Jh1BOmd8isMmnZmuVv2nItmLfs7pTBpzTGrIku7Pun8E3wFHsld10d3YRGvd8Q_H_g8dPoNgAFpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خطرناک‌ترین پدیده برای جامعه ایران چیست؟
فولادیان، استاد جامعه شناسی:
🔹
جامعه ایران خیلی صفر و یک شده، یا بر حق هستی یا حق، هیچ راه میانه و وسطی برای تو باقی نمی‌گذارند.
🔹
عملا هیچ وسطی را به رسمیت نمی‌شناسیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/678465" target="_blank">📅 20:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
از گودال‌های آتش تا بازگشت به زندگی؛ روایت تکان‌دهنده یک تجربه نزدیک به مرگ
🔹
00:08:00 کشش شدید به سمت یک چاه تاریک از پشت سر
🔹
00:12:00 نجات یافتن از میان دهکده آتش با صدا زدن نام اهل بیت
🔹
00:28:00 اقامه نماز جماعت با پیشوایی حضرت علی(ع)
🔹
00:40:30 حسابرسی توسط ۳ خانم و پاکی نامه اعمال به خاطر زایمان
🔹
00:51:30 درخواست بازگشت و فرصت دوباره در سجده بر خوشبوترین خاک
🔹
01:01:00 رؤیت وضعیت برزخی خواستگاری که از خودکشی‌اش بی‌خبر بودم
🔹
01:08:50 روی برگرداندن امام حسین(ع) از من بخاطر نیت و تلاشم برای سقط فرزند
🔹
قسمت بیست‌ویکم (لوح سفید)، فصل پنجم
🔹
#تجربه‌گر
: معصومه فیضیان
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/678464" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc72e04a0.mp4?token=qjByGsjHoolRutiaG3tLCB8Ot23qwII196HDzlqQIUxpsIX-G0BG9mqv6FDQ9_qd1G319O0GK2yrjuFZiQxY-4G7huiDxrwXQgpPsCTTowsUCNjX_1_LvAwZ8124yc4_JfSX-aF2-WIDu35sTY_YSrT7ITVf7dJczs5FFxn_yfBg7JBV8KVBu3v0cfGy4Bjyrw04oN7fZgiXI1Y0RLwj7vS3y-_0kUHJCDMWvwsuklv_biavei5-XFQgMrZTZesspSIKA22KtkDSbB1dEeIrn9psiZRGJLVDRsVEDLhqB9II1uOy7sM6AItiDro0vQF6v6Ok0Hlk-tGgWJHfa-O3mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc72e04a0.mp4?token=qjByGsjHoolRutiaG3tLCB8Ot23qwII196HDzlqQIUxpsIX-G0BG9mqv6FDQ9_qd1G319O0GK2yrjuFZiQxY-4G7huiDxrwXQgpPsCTTowsUCNjX_1_LvAwZ8124yc4_JfSX-aF2-WIDu35sTY_YSrT7ITVf7dJczs5FFxn_yfBg7JBV8KVBu3v0cfGy4Bjyrw04oN7fZgiXI1Y0RLwj7vS3y-_0kUHJCDMWvwsuklv_biavei5-XFQgMrZTZesspSIKA22KtkDSbB1dEeIrn9psiZRGJLVDRsVEDLhqB9II1uOy7sM6AItiDro0vQF6v6Ok0Hlk-tGgWJHfa-O3mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش احساسی رضا قیطاسی، قهرمان مردان آهنین به حضور در پیاده‌روی اربعین/ روایتی از حال‌وهوای متفاوت این سفر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/678463" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a510468f.mp4?token=LiGELOjBWpxyjY0QCBe4DEuYU-vq-m8PrXnU5gfSW6_IwSM3dc6YGjFeO5Ae8_gS4dBzelGURvVfcBR9lcq9N6K_d35BctrEQHAtPYeAMIXTTioDj980eocDua7esGgVqGQRP_DBHNV0TY9HCnH0CAYkwopTYm1HhtFkAQupF5B5opPJpLWznDbhk6fEPHMkZf09q35j52hacM7iitYTTw5J7AgZaotQOvjK2Gk6cMGlSzVlpx1xvnvFin-IEEjHhPCJlkZAPwAJ26lw776IouwTFmLwRrXP-nRp0ka-OLW8_RD0NGgG7kGVj2bvXc5J0jb4tKxlxSeOiBNuUZwdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a510468f.mp4?token=LiGELOjBWpxyjY0QCBe4DEuYU-vq-m8PrXnU5gfSW6_IwSM3dc6YGjFeO5Ae8_gS4dBzelGURvVfcBR9lcq9N6K_d35BctrEQHAtPYeAMIXTTioDj980eocDua7esGgVqGQRP_DBHNV0TY9HCnH0CAYkwopTYm1HhtFkAQupF5B5opPJpLWznDbhk6fEPHMkZf09q35j52hacM7iitYTTw5J7AgZaotQOvjK2Gk6cMGlSzVlpx1xvnvFin-IEEjHhPCJlkZAPwAJ26lw776IouwTFmLwRrXP-nRp0ka-OLW8_RD0NGgG7kGVj2bvXc5J0jb4tKxlxSeOiBNuUZwdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنگاپور ورود دو عضو اصلی گروه موسیقی انگلیسی Massive Attack را به دلیل نمایش پرچم فلسطین در جریان اجرای کنسرت هفته گذشته خود ممنوع کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/678462" target="_blank">📅 20:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dabb9ebf96.mp4?token=L4lK679fVtEg1daXBaT9VRpJhuj6y__kdU-FiYPGeEhJm1tNQi5F0ptlPWb2wy1iZGJzSsDVwW3O5b00J6zMo_o84fR75feFLI1zFlgx_NyfDGpB9U2n1C99oDpvSIl9gJmpe15ubvkU5s0RfBWhnPEdIAde9k6Asp7PxbOgGCuZ9wOT3VGUhKbqi1j9AqbH6MY4BtWB8afxX10pq5p_vfM3d_RYFPhdk0k_UUc5xel9txvu79b3JZMeiyUmjFEOzllqhO_fu4KT6JfWih0vpkM8JlHmOqcHcq-obAkQ0OnLSpZZ175obw4DO1vVvApMKNOZ_7KmHQ469fxCnl_Cxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dabb9ebf96.mp4?token=L4lK679fVtEg1daXBaT9VRpJhuj6y__kdU-FiYPGeEhJm1tNQi5F0ptlPWb2wy1iZGJzSsDVwW3O5b00J6zMo_o84fR75feFLI1zFlgx_NyfDGpB9U2n1C99oDpvSIl9gJmpe15ubvkU5s0RfBWhnPEdIAde9k6Asp7PxbOgGCuZ9wOT3VGUhKbqi1j9AqbH6MY4BtWB8afxX10pq5p_vfM3d_RYFPhdk0k_UUc5xel9txvu79b3JZMeiyUmjFEOzllqhO_fu4KT6JfWih0vpkM8JlHmOqcHcq-obAkQ0OnLSpZZ175obw4DO1vVvApMKNOZ_7KmHQ469fxCnl_Cxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معروف‌ترین سلبریتی‌های دنیا طرفدار چه تیم‌های فوتبال هستند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/678461" target="_blank">📅 20:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادارات و بانک‌های کدام استان‌ها چهارشنبه؛ ۱۴ مردادماه تعطیل شدند
؟
🔹
کردستان
🔹
قم
🔹
هرمزگان
🔹
ایلام
🔹
کرمانشاه
🔹
سیستان‌‌و بلوچستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/678460" target="_blank">📅 20:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAIYwb5aftteM5btwuIkxwb32NSJOSfiktwyaH5J4LbcHSDqSfsmfW1JAdfEgz0iZFxWEb3PqEZbeMMqwQ3iJX4hHSmnhpqz2HeO4W63w72IWz8rrkKV1cg2aU5gnIpF0XZUUfyM6b5iVXn00UNoaxZZ2668K1NPKpzmOB2APah7QCZC6f5yrpumb7GT_mMDkIKCWLEdllEb45DhnzNtlhv1hnPZIS0g5gybMyKkdOgL1jTkN5QI8NoaGFBBuhxFTKC0FjXO-Nh1kOygrxZ6OfIE8bo3q10Xq_QaR8itI_nYjVfaMBM9zkkbn7WmqVa4H2tbTxWPJ7YVtaF_exsDIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/678459" target="_blank">📅 20:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
یک منبع امنیتی به نیویورک تایمز: سامانه‌های پدافند هوایی عراق در امتداد مرز عراق و ایران، از استان دیالی تا استان واسط، مستقر شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/678458" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9ULhqX-pfROCM4JNjbbA_DbeqbKN6SV9jd50jj7E4lUvMjnGy-tZLBcLp7bfiHRaNmhxZqwvLjs_7tBgmUa9nX0b-7yUczaqyt-fD3inQ_4ZRtY9SXpQxs2OaT1by8Y1SWg4St5vwcAbpkyyKSx3r9zCndp0LvGKooZfeXDwlnDUzrs8z6dtvR5h9da5nV0F19e0WA23WFttrVA4t7x-VKAK4OPpNGPUj5dIjk34hfknfn0k5LL1paG1qhhtCBDUhUnFn31CDDoDYLxI4yhXpbz_UAQaw4x-vERgLSx2vOj52Ltt_3SQU1r2rRdkSTN0Iwn8dpBwMHLUPK7xzagQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقایق شگفت‌انگیز درباره بدن انسان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/678457" target="_blank">📅 19:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEA05I-GzxUl0T4M8pcxMTp8IxSJ1nnuf-8EWTIGxncPCVUM1JDEwgY4qzI0eaQ3-ZdTxBNL-_ENRzxqaot1RpQy5c6xgWlmhAgUBfafNXOBrBrvgua7f2GaU8Ku9E-pVrZLsnrz3zMs6_A7HZKAH2D_9TYB2zt10vBXWdzdAhFX8iG2L1I35YiYfRvkHDTUpGJwv994DWyQOt9Z-ZsZaXaXLuulI5oBQtdT_fa_1KrOeDFb2H4KW7wjl2oHQcd9VlmXS2ymCusSZ_-sSNcg_cb68gOWUtzg4cMILFAuchDXlOHC6YYynXlTcJh3UsFiwrrabrGGRP7I-1kdZOhPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش قیمت تتر به ۱۸۸ هزارتومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/678456" target="_blank">📅 19:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678454">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادامه مذاکرات ایران و عمان برای سامان‌دهی تردد ایمن در تنگه هرمز
سخنگوی وزارت امور خارجه:
🔹
مذاکرات به عنوان گفت‌وگو میان دو کشور ساحلی تنگه هرمز، با تمرکز بر تعیین مسیرهای رفت و برگشت ایمن برای کشتی‌ها در حال پیگیری است.
🔹
گفتگوها تاکنون در هر دو سطح فنی و سیاسی مثبت ارزیابی می‌شود، نتایج نهایی این مذاکرات پس از جمع‌بندی، اطلاع‌رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/678454" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678453">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e805de888f.mp4?token=FSJIOn3EfO2Wexj0Phhi5dZLPypPeC43I1Tle4MJHBiPDoMRPuniSMAZOhfl2Xod-6hzcrw5XRG0qUnew8QbTfBbC3QFZQZPF2ggNzM4zQuFsLa4-tmGMVdiofOsk4442MNAMO-U5b5eD3na9hpzveQtdnUMp5wrfaw6FJ-9dIQzXvDoUzmaiMmENety0YFt_e6G1aG7rHBmfalA8ypr643eRA_iCp8uMEDRNgda7NtRJAlYXUMirBw6Aao1tZoeMiEkfgY4yYJlna5e3dQpWyKleyuC_VSsCxK_zyO8oP21sBqhZz6L7OIsvxostiwEynnIIP9YNHg1sYQN5mPPEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e805de888f.mp4?token=FSJIOn3EfO2Wexj0Phhi5dZLPypPeC43I1Tle4MJHBiPDoMRPuniSMAZOhfl2Xod-6hzcrw5XRG0qUnew8QbTfBbC3QFZQZPF2ggNzM4zQuFsLa4-tmGMVdiofOsk4442MNAMO-U5b5eD3na9hpzveQtdnUMp5wrfaw6FJ-9dIQzXvDoUzmaiMmENety0YFt_e6G1aG7rHBmfalA8ypr643eRA_iCp8uMEDRNgda7NtRJAlYXUMirBw6Aao1tZoeMiEkfgY4yYJlna5e3dQpWyKleyuC_VSsCxK_zyO8oP21sBqhZz6L7OIsvxostiwEynnIIP9YNHg1sYQN5mPPEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به ساحل تفریحی و  شلوغ روسیه
🔹
در این حمله چندین نفر کشته شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/678453" target="_blank">📅 19:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678452">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای روبیو: درباره تنگه هرمز پیشرفت داشتیم اما هنوز به توافق نهایی نرسیدیم
وزیر امور خارجه آمریکا:
🔹
گفت‌وگوهای جاری میان ایران، عمان و آمریکا درباره افزایش تردد کشتی‌ها از تنگه هرمز پیشرفت‌هایی داشته است، اما تاکنون توافق نهایی در این زمینه حاصل نشده است.
🔹
فوری‌ترین توافق در شرایط کنونی، مربوط به تنگه هرمز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/678452" target="_blank">📅 19:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678451">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
العربیه: ارتش سوریه بدون اعلام دلایلی، وضعیت آماده‌باش نظامی اعلام کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/678451" target="_blank">📅 19:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678450">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fed2c750b.mp4?token=jmAL4sc3F8vklBE7Lx0J9hjwQmcNu6U4pUeGyrQ_2Dpi2FVWMsex9LoXNSHAffUr4LQNRFHcpgH81LnV_fQTd8mfm9lEgy5a4bgIqWbZCA96IQagGznAuDcQvT3OHQzABmQFrGZ43DwH3JnUgMaBF_gf8w0O3YEBDop5MHGSYOpAQw4UHRwCygW6zQ_PgGAIRdYEGmFeqSfaBuBuNgIfYYqXU2QohUo0eS1Ox5jDoBg5hX6SSTsgfAAbee4ff-AcjUqxBh7qCf_LIEKxPhOTNPeKAx49xvjt-_gUISi5_LMnR5lBk-y_Hw5HtKkrVemcIODaO9A6AJ_A4KmjOx6kkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fed2c750b.mp4?token=jmAL4sc3F8vklBE7Lx0J9hjwQmcNu6U4pUeGyrQ_2Dpi2FVWMsex9LoXNSHAffUr4LQNRFHcpgH81LnV_fQTd8mfm9lEgy5a4bgIqWbZCA96IQagGznAuDcQvT3OHQzABmQFrGZ43DwH3JnUgMaBF_gf8w0O3YEBDop5MHGSYOpAQw4UHRwCygW6zQ_PgGAIRdYEGmFeqSfaBuBuNgIfYYqXU2QohUo0eS1Ox5jDoBg5hX6SSTsgfAAbee4ff-AcjUqxBh7qCf_LIEKxPhOTNPeKAx49xvjt-_gUISi5_LMnR5lBk-y_Hw5HtKkrVemcIODaO9A6AJ_A4KmjOx6kkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: تلفن همراه دارید؟ بخشی از اسراییل را با خود حمل می‌کنید!
🔹
گزارش تحقیقی شبکه الجزیره انگلیسی از نفوذ اسراییل در تولید گوشی‌های تلفن همراه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/678450" target="_blank">📅 19:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678449">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/babacb9d91.mp4?token=uos2uhMC_cIZIoLQl5GAn7QQTbSLBD4INFfQ8FhY1SrwsolZVKZMn1Ft29EWozeyx-uBLnRirJ0BHnSBdE0w_wYMoRRhtJiyfpyDBBs-jzkn7sm3f6KeqT8z_CLv6Pws7QWynlFJ2ibPsnNnvLRMfqfA0qlR2OQEwYch-bvTsuq5KDLqF4W4zA6z1FPu1qyPIglHblHxVCzKbU5VdZsTsAvXn7oGjEBNE7ZrPR9M_VQYmbl7nXc9AbCQtXG5gGJ77ofRfrVgXNV9CVh0L8BAFCcKq30d0f1om4CinTcy_PwTHbkRPHBA92GiHWlgG9TemBwzn4Sbzks7KqQcGymoGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/babacb9d91.mp4?token=uos2uhMC_cIZIoLQl5GAn7QQTbSLBD4INFfQ8FhY1SrwsolZVKZMn1Ft29EWozeyx-uBLnRirJ0BHnSBdE0w_wYMoRRhtJiyfpyDBBs-jzkn7sm3f6KeqT8z_CLv6Pws7QWynlFJ2ibPsnNnvLRMfqfA0qlR2OQEwYch-bvTsuq5KDLqF4W4zA6z1FPu1qyPIglHblHxVCzKbU5VdZsTsAvXn7oGjEBNE7ZrPR9M_VQYmbl7nXc9AbCQtXG5gGJ77ofRfrVgXNV9CVh0L8BAFCcKq30d0f1om4CinTcy_PwTHbkRPHBA92GiHWlgG9TemBwzn4Sbzks7KqQcGymoGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای حرم حضرت زینب(س) در روز اربعین حسینی
🖤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/678449" target="_blank">📅 19:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678448">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np8qrfmLT007qdRm_WNao9sm12UbTekUuFIoD2icGm5lkoDjZQ93GGW8A5q_wSIo-tFiqfuqOoOIKx8-aXLXxPmgxQA4Ri8YlFbl_zSfP_Eyvuo2WsL-kdWGTo25yr5yxtGIe02LRDGew0y5b2EHCP8zVdfwOSJAIqy3Rl8hKh8QigJ_NP6PzJKVxNQIG4IXRnEJ1CaTAtJO6AKzQuYzhsSzvbqD2QhIoIku07MYTQVd4N012BVkgluYvXMeJgfUnZ4vYS6laCzuVlHtlwy1uk1Uvww_o7uIAYIL_tFK3wjpXY9XdvMYkConIGY4zRxYyoiy0oAd-GYjSZNKSuiXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش جورجینا به انتقادها از بدنش
🔹
جورجینا پس از انتقادها از بدنش، درباره تغییرات طبیعی بدن زنان پس از زایمان پست منتشر کرد. آنتونلا، همسر مسی، نیز زیر این پست کامنت گذاشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/678448" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678447">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5b9fc7a6.mp4?token=YLN5ha7EjfiDBHEZhrsNAjDQtgdQ7kD-mi6rj7WoSMW4A3XL_LJYT6vUJdGswXS6lraFOgQCS1Lvz2hnrGWLy2Vxj-xJar3qTAoJycwYORh_PU0GAqaDDeGnRrKKP2FGdfTgT4QmiyW5trd--wfBxxHSF-2tVdiFo6Fg9c1NEY6uFbRJw-iW8YY_fBtCNk1eN5k5Lbo3mIrU4wJqp-rD_5yMpAtc79Q12DBfY6Mpnirt-wc6R3KN0kd5DzYuC8qRrbSYFRbdPC7_QS-TCWjfrEwnX6E520Ddb6G0LxeNhWsn3sLATFJbvrFtLGuIteqkA8l-I0pDB-LKk4KhOoK6PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5b9fc7a6.mp4?token=YLN5ha7EjfiDBHEZhrsNAjDQtgdQ7kD-mi6rj7WoSMW4A3XL_LJYT6vUJdGswXS6lraFOgQCS1Lvz2hnrGWLy2Vxj-xJar3qTAoJycwYORh_PU0GAqaDDeGnRrKKP2FGdfTgT4QmiyW5trd--wfBxxHSF-2tVdiFo6Fg9c1NEY6uFbRJw-iW8YY_fBtCNk1eN5k5Lbo3mIrU4wJqp-rD_5yMpAtc79Q12DBfY6Mpnirt-wc6R3KN0kd5DzYuC8qRrbSYFRbdPC7_QS-TCWjfrEwnX6E520Ddb6G0LxeNhWsn3sLATFJbvrFtLGuIteqkA8l-I0pDB-LKk4KhOoK6PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین پهپادهای بیونیک شبیه پرندگان و حشرات ساخت
🔹
مهندسان چینی پهپادهایی با الهام از شاهین، کبوتر، پروانه و سوسک ساخته‌اند که با بال‌زدن پرواز می‌کنند. مدل شاهین با قابلیت شناسایی و ردیابی اهداف، در آزمایشی ۲۵۶ دقیقه بدون فرود در هوا ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/678447" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678446">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
انتشار گفت‌وگوی پزشکیان با مردم عقب افتاد
🔹
با توجه به شلوغی کنداکتور صداوسیما در شب اربعین، پخش قسمت اول مصاحبه رئیس جمهور پزشکیان به فردا شب موکول شد./ دفتر رئیس جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/678446" target="_blank">📅 18:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678445">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مذاکرات عربستان با یمن برای کاهش تنش
ادعای بلومبرگ:
🔹
عربستان با میانجی‌گری عمان برای کاهش تنش با صنعا مذاکره می‌کند و هم‌زمان گزینه‌های نظامی را نیز بررسی دارد.
🔹
آمریکا نیز از ریاض خواسته از عملیات گسترده نظامی خودداری کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/678445" target="_blank">📅 18:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678444">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
مذاکرات ایران و عمان درباره کریدور تنگه هرمز وارد مرحله جدید شد
یک منبع آگاه به پرس‌تی‌وی:
🔹
مذاکرات ایران و عمان برای ایجاد کریدور جدید در تنگه هرمز وارد مرحله تازه‌ای شده و در صورت توقف کارشکنی آمریکا، تفاهم دو کشور در دسترس است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/678444" target="_blank">📅 18:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678443">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeJ179GiawtyP-SqyCoS7_qGDC1Wzv9TsoJrmT7APRiXbPZJQQQ3qqF-MRASV5sfJmnjpwxZIokPG9eXx5kt54NvwoktpeAlkEETL9vmHkrJJW3t1tuIDycvIXS4StwW2WWqB1WsGid3avh4NQX2CS6vd66hO403wl_lD3GbMlKDbiBEYXxmTybLbgbZdp1Fl4r3cbRQL2SLPYwFQwauriGKHl_wD3pedV8LbZ0HInU-qkMbE8t2vooZ1OJQJc-7pH1guu2gBPzWf4WsdJiV1fDwo3lj6vBd2hWNo5lMpIU7FQLE4dl9ubxIkmAtXmCBpt-rWPWQoUIhl6j_q8V-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت ضرغامی درباره آیت الله جنتی: خودت استعفا بده و به نظام خدمت کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/678443" target="_blank">📅 18:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad9f5dbc5.mp4?token=f2KNr_XsMhn7S39v4yEdE7JpIE3GyOUFYJPd2Z87QD-48Qh0lTLGHnKEvyN1tUaB05mG-islp0WYoyZDyvnxanq4zH6_DR29GE2s6q3tRk4gAnQhlwOtPZKK4gA0fhwBCTcba8b6C53mvedg2y2fJN9qnfXYx_qH7cE7dbVRm9nKXIjhDpRx-QvNpD6rYE0wZxGGVOumuF_lcjZmmCvSryR7nGIjuq8b77TAfAeoLHhFrUkIj366nd8gSZSB84jW7lwjUlTmVvDZkIVvApNYQK60oY6aCVRlUpNcd_qoSYVebpkhT3o4ecqwBEVNlhydug1reIlZ5Db1s8LxdLXC6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad9f5dbc5.mp4?token=f2KNr_XsMhn7S39v4yEdE7JpIE3GyOUFYJPd2Z87QD-48Qh0lTLGHnKEvyN1tUaB05mG-islp0WYoyZDyvnxanq4zH6_DR29GE2s6q3tRk4gAnQhlwOtPZKK4gA0fhwBCTcba8b6C53mvedg2y2fJN9qnfXYx_qH7cE7dbVRm9nKXIjhDpRx-QvNpD6rYE0wZxGGVOumuF_lcjZmmCvSryR7nGIjuq8b77TAfAeoLHhFrUkIj366nd8gSZSB84jW7lwjUlTmVvDZkIVvApNYQK60oY6aCVRlUpNcd_qoSYVebpkhT3o4ecqwBEVNlhydug1reIlZ5Db1s8LxdLXC6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید میوه‌ها رو از زبون خودشون بشنوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/678442" target="_blank">📅 18:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcEJDwN1hgNJ-OyCWugAZiKSujGMVbQhgrhUguu3vtp7gQODqqUJoPABannUhR4F0gtNPjMSsEoRWCByqfJLUwoXTtMUURpyMsuXyyqIvAEopyWz_vYJVVlm7WB1u61wvzgskesgIkUg-hwCqD2MaiaK1o08mEnFyNrw2PJjKk5UkUhzm11Wqk24X21l0AENySIw30_l0ehbZu9AjF36Ljah6HxVmz1zqcMTTH7v3o97Qx-caDd-kYLaEyETf6DPEh-_N5vnZ5bEvEYQH5Sypoa1vQplP4YBNEniT7M2fIge-yU6boATxXwe2s8nGQncsVyEesDTENuuNYPfmD4ZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پستی در تروث منتشر کرده پیرامون توافق با ایران بر سر تنگه هرمز و برنامه هسته‌ای
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/678441" target="_blank">📅 18:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
استاندار کربلا: ۲۲ میلیون زائر برای گرامیداشت اربعین امام حسین(ع) در این مراسم حضور یافتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/678440" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678438">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
روابط‌عمومی دفتر رهبر انقلاب: مطالب خارج از مراجع رسمی فاقد اعتبار است
روابط‌عمومی دفتر رهبر انقلاب:
🔹
اخبار و پیام‌های مرتبط با ایشان تنها از پایگاه اطلاع‌رسانی دفتر رهبر انقلاب و پایگاه حفظ و نشر آثار ایشان معتبر است.
🔹
همچنین ادعای مطرح‌شده درباره واکنش رهبر انقلاب به نامه رئیس‌جمهور را «کذب و خلاف واقع» دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/678438" target="_blank">📅 17:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678432">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T02O7Js5HP69lbOqE-2MLgPEUlkXSTZdTHzvuC0R8shFu73OYZVt3LuSo42EWw1wl-l4TcbnL-3_cmOXvQdPuFzyRce1I-rN6GErvUIwSErL9RcKZTTc2uAgDUFBPHobB9OPEbGB1JMaoD2a2Usec1DD98RzFge_JTeDYzCr8DZsN1tSJNCZ1MIAm4cVBjEz22LjRvO9cqHs3RC_cTKV4bjgF4Ck4bgTHmkmNQebbld2bmQv6WrCVHL-NPS6ZWhAbIIVgGbvGHaykfcZOdHgEcA7rweyH2UCm1uwAy8JZtzpfNuj2etXMThJeTUJ2K_qZYgDxCcHd1AwFW_C6PCQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOYKs1iqjVVzsx9_Vs1NU7Tmi5Dw86sVvRN1T58OUpcxHZgwvQPhqoWLEWwqxNHkZPc_SGbZzIFJ6h0y9edlbSZOPkDPKQWSANO9wPIj6z3nAqY0QSRZ4id4qGZPchGN7m2P_nbh_N5sGmGbTUFC1N_QycTG9akD9FQnAhs820gbO1JQI2Ezraip4CFUH7dnUd-I1ZUaay7SGN9WmLLMpreuAFf2jzexi2jwuiufVezoBIR-Sj89HYohkroNvKABOYxuwYEDSksAsJwa77ut6wVbsM68mlB9Zw3SR7PRNrff6Q7KpLZh63_iXFQ_hl5M3HWJ15HQpwH_HKApTUgcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSx0PKjLURYbQfkTNzBE63RQRTVBF9gSgn2tUvS-yOgAo-mufffyUzdtb53MY7YKbtSoBN9IcEYbiUtrk4v1xuT86mYJuhzAydy9jn50tON2oHw1e8H7A7IhIfauD_shPOxvyubOMLD01pg2BGA8azUq2vX67SmPTGeEeEStXGaJOq91C3EN1VjFGSy5OhGV-el5shmDuo_dQEr_GTWN8z_176Jf7KefKGbA7Py5FhrZIJDde804gzp3PwebsRixilguQIKMa94ktI5_4Td_Ti_9_wmImcDr7N4RGHGQvQNOmJLgOv97oLHZnqYn83uuEU-7imalaLU6vke8OVZ0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQC48IWNWXNUUg42EprH2UemYdhcXB7MArHZ4cTcSeNVpIexofoXQwY51yZh8qoKHsVHl29Z03lweVadMzNTn2VYfY0uY5R9pQaKjKfmOCiJZr9vuw9XCWhO_gVY6W-mVpbNIBICweZ6OCtqbKXCWiSVEQWS2ninD4nJ_F8N23N-9Va96b5pDr53IjzrxulwFdEOBUguHuA3vV2ok8EUFNnZecx1rSRrMC7j6rg0xlszoY4m3cDV8PRcPcV7cg67Ph4hanye4gBt_Y7AbcbX7hWZWOAq3AdS93h7CUZqqgQP3AgsEIt4wy3xL-iZO_h0dC2oaAWEClH5bITi1YKcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSjJGmzvu9XgbrqVfQx9_pU9hmM4dqCjOzppRt0mSPgO91-cEGGSfCCNG8h1pePfCOa5kS-4h35wTiSU2Kejpziuq8rKjtOnaA8Kgl0H87frjPOzjLbht7eMqgQqvjtceETjv2YALTVCzv6q5BdS9InMBC7x0ZDG7qSauuXxLW0QxjeUKYe76i3guVa7RQOIgPXLQyPuxCDnSC7WmOSmubBb11XQoCTEGm_p8ho4HvYgEmbO2R7axUIIMErKedM-RuPKz_DOo4iKnK0Ogt436vbI48s6cVnX77pQje9AVqowEpUU7Ffb1CkorjFKfOev5KwPsfU1GN27uIWI0nEEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6tlf7gTgmJcymlLWDqI8Kduwm9yaPsEnb-aw0OLwu4Bc0MtLyuxCY3ziCrkrOfCDxYhGDLmMZ6EjeF-H2f8eTGhlmHSErvc96qX2J63zpE8XZe8gcy4gYR1aTQFXPDzu-0LgP4IzNtW1CQKvZNZX6De82rHX7ae_iWG08XcYaYmMsKlhsmA69gIyHsJo4RRZoHn4_rAOeDOQTFT8zaG1FOBq6y2FwXmtWEID_uaPsY-_GBG5dOUqEGhQOBwcPfhMjzyKBSeS46jL3qADKNY1ZqjDs1Bbw77H7KxUkOuiiltljhJQMrxuUroNYTVhsytuatEWdbsGCiGhyBSkGreig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
«زیــــارت اربــــعــــیــــن»
▪️
حضرت امام حسن عسكرى عليه‌السلام می‌فرمایند: علامات مؤمن پنج چيز است؛
▪️
اول، در هر شبانه‌روز پنجاه و يک ركعت نماز گزاشتن (هفده ركعت فريضه و سى و چهار ركعت نافله)؛
دوم، زيارت اربعين كردن؛
سوم؛ انگشتر در دست راست كردن؛
چهره، جبين را در سجده بر خاک گذاشتن
و پنجم، «بِسۡمِ ٱللَّهِ ٱلرَّحۡمَـٰنِ ٱلرَّحِیمِ» را بلند گفتن!
@Heyate_gharar</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/678432" target="_blank">📅 17:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678431">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
رسانه‌های عربی: یک کشتی هندی در فاصله ۱۳ مایلی سواحل الحدیده، پس از هدف قرار گرفتن با یک قایق انتحاری بدون سرنشین، غرق شد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/678431" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678430">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای وزیرخارجه امریکا: امیدواری وجود دارد که در آینده‌ای نزدیک توافقی درباره تنگه هرمز حاصل شود
🔹
پیشرفت‌هایی در مذاکرات با ایران برای بازگشایی تنگه هرمز حاصل شد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/678430" target="_blank">📅 17:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای قطر: متن توافق احتمالی ایران و آمریکا تدوین شده است
سخنگوی وزارت خارجه قطر:
🔹
متن توافق احتمالی میان ایران و آمریکا تدوین و میان طرف‌ها در حال تبادل است؛ میانجی‌ها به دنبال راه‌حلی کوتاه‌مدت برای بازگشت تهران و واشنگتن به میز مذاکره هستند، اما فعلاً برنامه‌ای برای مذاکرات مستقیم وجود ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/678429" target="_blank">📅 17:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f565286a.mp4?token=HsA19i1g60BiC1R436Mnil3G19VhQ0j6cviX4o6lVqHyjkX3Dt8Z9j5UHPBmYdCT_SjyBnZcndY0dkypob0dK6Q1WT8GZglO3JVTtRBRAPqMe7f36EC6yo0Ja7rRkej0MWVzn3WfHbKBHeDmfn2WKxlAla3v-qQzoBb24KImBsvk9pRkgcgGLcCtXXzBnR_jcuDP4zQaC9xHBupEIrjXMQ3aNoxYiD314iL4yoNjdOoxWzVm1Wi7e0HL88N4vTrD3xcv2PHfF_6_v6zlKxAuz15OH8IcUwCwwGg7rMflfHSl7S3dmI08_qGufzndIaiokBeEbl8tx3npXqbbUnapjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f565286a.mp4?token=HsA19i1g60BiC1R436Mnil3G19VhQ0j6cviX4o6lVqHyjkX3Dt8Z9j5UHPBmYdCT_SjyBnZcndY0dkypob0dK6Q1WT8GZglO3JVTtRBRAPqMe7f36EC6yo0Ja7rRkej0MWVzn3WfHbKBHeDmfn2WKxlAla3v-qQzoBb24KImBsvk9pRkgcgGLcCtXXzBnR_jcuDP4zQaC9xHBupEIrjXMQ3aNoxYiD314iL4yoNjdOoxWzVm1Wi7e0HL88N4vTrD3xcv2PHfF_6_v6zlKxAuz15OH8IcUwCwwGg7rMflfHSl7S3dmI08_qGufzndIaiokBeEbl8tx3npXqbbUnapjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر بستنی اینجوری درست کنین، قطعأ با بستنی دبل چاکلت بیرون خداحافظی می‌کنید
👌
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/678428" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678427">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ24GIzRSfI5mzsg0W84SRviygZ8ya-5RLNbwvnRtY9IOUiQKKeRscXPnCK3EA2-5H4fvnGYnBAZ3o9l1moNmgiRxm48bRYNLupN8md40OJs7qr8Yp5ZbwL1zSGdnUcqB92xOp2SXIdCO378qGZlTER6dZUKyZwRiXkU_oV4cksxrDKbXu365bHbx5qAsLB2jndJOq52OJZPlNQVwt5xRtaDHsKTawNj4w3co0SK_ZKkZtlAvX7cbuojuqfSsT9IGfM0fI_9V8Wnj8NopYrcsDD6fkKV1hN86zEC4rjy3TawIfmrs1XaaYdc2u7ts0Mb0FWr5eoEE0RiGvTzp9L3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش شدید قیمت نفت برنت پس از ادعای وزیر خزانه‌داری آمریکا درباره ایران
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/678427" target="_blank">📅 17:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما بزرگ‌ترین مانع جوانان برای ورود به بازار کار چیست؟</h4>
<ul>
<li>✓ کمبود فرصت شغلی</li>
<li>✓ متناسب نبودن شغل با توانایی افراد</li>
<li>✓ عدم تناسب آموزش با بازار</li>
<li>✓ شرط داشتن سابقه کار</li>
<li>✓ سایر دلایل</li>
</ul>
</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/678426" target="_blank">📅 17:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678425">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای الحدث: به گفته یک منبع، اعلام ترتیبات بازگشایی کامل تنگه هرمز ممکن است ظرف چند ساعت آینده یا فردا انجام شود/ انتخاب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/678425" target="_blank">📅 17:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79f74b13f.mp4?token=ATgSUIAsc1mDITfJFIEAUtSOSFGSFQn4PsOvXrnSdiGrqb_vMJCVCBFpuht9hgUgIxDQHSrbSksRrdxoYiZWbZGlk6Gn1pWGnflvNhzIw0_ep67yd9-D1N91eVmFdTNFKuYdd3JsIWXRzd6NR7Nj9EQny8ohODY1oyltLX0JitAr3QHyuJLzMRuXVRgud81FV_xRNN5h1Mo22KAQ4Sjp28qU5jBNS4o1f5X5jah1nSm0AMmN2UUAC_jf6-tEl0nMZua4WtmyV8lAaaEvHsldzZNs1mxhshK9Nh0uP_cYRiuk9EJQM69VFDxpQ04T7mqx3dhwWwYFJfBXL0H6KqVCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79f74b13f.mp4?token=ATgSUIAsc1mDITfJFIEAUtSOSFGSFQn4PsOvXrnSdiGrqb_vMJCVCBFpuht9hgUgIxDQHSrbSksRrdxoYiZWbZGlk6Gn1pWGnflvNhzIw0_ep67yd9-D1N91eVmFdTNFKuYdd3JsIWXRzd6NR7Nj9EQny8ohODY1oyltLX0JitAr3QHyuJLzMRuXVRgud81FV_xRNN5h1Mo22KAQ4Sjp28qU5jBNS4o1f5X5jah1nSm0AMmN2UUAC_jf6-tEl0nMZua4WtmyV8lAaaEvHsldzZNs1mxhshK9Nh0uP_cYRiuk9EJQM69VFDxpQ04T7mqx3dhwWwYFJfBXL0H6KqVCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی در میامی کسی مزاحم مسی نمی‌شود
🔹
لیونل مسی در میامی می‌تواند همراه فرزندانش بدون مزاحمت به خرید برود؛ موضوعی که باعث شده برخی این شهر را به‌دلیل برخورد عادی مردم با او، انتخاب مناسبی برای زندگی بدانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/678424" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUzyWY5BPBeBWsN2CCsSInUNpf8WrSmm6CJReosb1y8n4_aOA0Kw2aTEl3zkVz22vR80GFxCeI1TtSZBR0igNzS9ux4xV-72IwA6FsG9q9vk74uhQHykZW6OM30f-XP1zILiVsj7EVJ_G_RVKL9C-yovhysarYrClJwzBmB4Ei8-mT_paO-d51CuDztjqoHTTiLSnwHqqw9sOMFjL6R6-tNyIswjBVKBrW9zbEFUmgB9b9NMw6oQ4dxkpyekr06H2OpaIrlRVcceMJ2bPT9fHq3rYtlqAftlfl7fdFSho0JJcx1C1Qb8Mwko1ciHcnCUeZ9xjyUwYwS0PwxwBfhs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر وایرال شده از قرآنِ منسوب به دست‌خطِ مبارکِ امام حسین (ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/678423" target="_blank">📅 17:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678422">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای الحدث: به گفته یک منبع، اعلام ترتیبات بازگشایی کامل تنگه هرمز ممکن است ظرف چند ساعت آینده یا فردا انجام شود/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/678422" target="_blank">📅 16:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFqXXItJtgD7BRsM6hzzF1FBaI3hUJvbwfiIanXJa_3ynQlYn8YdjLSZ-CpMNskO_2Csf2P2_v5abwD0pWB91UHG09LvrdfOF7XbwVmZ1JCLgPMz8uDabZb5Io-BZLNA8cC5vS6PPrrA91HWSq1kEyfjMWZ9vE8ROnutmb7VJhco43Fn_c9haAPCMwo6u4otW_lvgDSDy93X-JRFWHWT3KY-yO1MXQadZ5OYO1Wx4nQlGf1-OXOMcyWmHOxCT34p3ftPL4hQktuLwEELu3d1xIy7X972W7JpnuSXeJJ_d-lWEPIvlmAmqKzFz_2ZzlnGLMvccd1gEF160aKOW97m2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: مسیر بازگشایی تنگه هرمز با ابتکار ایران در حال پیشروی است
ادعای پاتریک وینتور، دبیر دیپلماسی گاردین:
🔹
عمان تحت فشار آمریکا، اروپا و عربستان در حال پذیرش طرحی برای بازگشایی تنگه هرمز است که بر اساس آن، ایران همچنان کنترل غالب بر مسیر عبور کشتی‌ها خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/678421" target="_blank">📅 16:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678420">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfedd1510f.mp4?token=IF_yo8GI_rg3egVm4Yb-Etwd8DtMVPIA73u_dH33a8Lg2aGNG5FKSB2yvY8C4BQmE3ao3wcwmJa9Xb8D1KT6FgdOew15fpMN-w_-1Py4b8r9-439jzsk6N0j1kav7TMXatqLH1YADzu-NqEf-cRAi-sKqnQ-jESMKXV66DrZlyrJiAah4OgLeg8k5JrMdZe2uD7nQ5kXeNshrISZI1eaHpICiLMo0Obbv_SvcZUS9YHhMI0cayzka568Vd1LRAdNm5J13n65mzIBrCwnsFayy-qfygwozEavIk_R3gm2b0DFUnmzqz_rlwV7EQtg7DelZp08MwtiOtyFkm896-4Mgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfedd1510f.mp4?token=IF_yo8GI_rg3egVm4Yb-Etwd8DtMVPIA73u_dH33a8Lg2aGNG5FKSB2yvY8C4BQmE3ao3wcwmJa9Xb8D1KT6FgdOew15fpMN-w_-1Py4b8r9-439jzsk6N0j1kav7TMXatqLH1YADzu-NqEf-cRAi-sKqnQ-jESMKXV66DrZlyrJiAah4OgLeg8k5JrMdZe2uD7nQ5kXeNshrISZI1eaHpICiLMo0Obbv_SvcZUS9YHhMI0cayzka568Vd1LRAdNm5J13n65mzIBrCwnsFayy-qfygwozEavIk_R3gm2b0DFUnmzqz_rlwV7EQtg7DelZp08MwtiOtyFkm896-4Mgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر اسکای‌نیوز: ایران در مسیر تبدیل شدن به قدرت برتر منطقه است
شان بل، تحلیلگر نظامی اسکای‌نیوز:
🔹
ایران با تداوم مسیر کنونی می‌تواند به قدرت برتر منطقه تبدیل شود و از نگاه راهبردی، کافی است بیش از آمریکا دوام بیاورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/678420" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678419">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ویکم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم معصومه فیضیان که با درد ناگهانی در قلب، روح از جسم جدا شده و خود را در میان گودال‌هایی از آتش و انسان‌هایی در عذاب دیده، اما با صدا زدن نام اهل بیت از این قسمت عبور کرده و با شنیدن صدای اذان در نماز جماعت با پیشوایی حضرت علی (ع) حضور یافته و در نهایت در صف حسابرسی قرار می‌گیرد و اجازه بازگشت به او داده نمی‌شود، اما ایشان با التماس و سجده به درگاه خداوند بخاطر داشتن فرزند شیرخواره، اذن برگشت خود را می گیرد؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: معصومه فیضیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/678419" target="_blank">📅 16:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678418">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
نفتکش‌های غول‌پیکر عربستان مسیر آفریقا را در پیش گرفتند
🔹
شش نفتکش غول‌پیکر سعودی، خالی از محموله، مسیر باب‌المندب را تغییر داده و از جنوب اقیانوس هند به سمت آفریقا حرکت می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/678418" target="_blank">📅 16:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678417">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE_J01-445Sbz1njMCvjg4Jw48J8tPpJZuN_RLmZ6uJWCMLcNkKVGRkee0jzgtND9n_RZXLSewNJ9oDc1BPXqNPRFzNR3A_7GkQvLugSd5uG4dx94TVR85BpSgTDDOI0MDWanKacXifV0NqW9_D78JFuosLJUGisxDd2xghDdDVR9WqYVxVqNC4-tbLc3Mln19TRxIV7-C6lenfBGt6pVvYqktZtE8FM5AoUpvc-ZTET1p1FsnAH-ao7aCwdcFsFcKIMCSxL9a5XimQNQjnTJ87Iy8Y_TtfVbs20iIbrfTYNjablnv3DePWCel8-hwuuzfRbHJu1XDFQY6H6pjKyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: صدام حسین ۲ قطعنامه سازمان ملل را زیر پا گذاشت و آمریکا او را اعدام کرد
🔹
نتانیاهو ۷۷ قطعنامه سازمان ملل را زیر پا گذاشت و هنوز زنده است. عجیب نیست؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/678417" target="_blank">📅 16:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678416">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcVFabQc4roTInqxzqYLNOx_goIaIzykwi3QjM95OP-2vz-rx8Yqb2anvVaWLWsk4S4szTZ9_7SOCrttLMpDUlbtP3XulQXiFy72GD1qdvKoNxMiJ6TPxOwz_rRQUa24LdCcTnPhzfC4yKUj2MlWPfbBES0qDdKAnO-E-6otvlMOehIL0eKaM43PfYJWWjB28-2e1Ias62MpH_rVKJ1aqC_swtZe6uznxcft3dEzPltRsSEtPWPnBJ_DVzKKuj6jtxfeQlxwYOEA3G9RG-MYC9nMu_gpvVpBx7BNcec3dft9Roe8cp6PLubs5lMa-RqHQiqogo1kOko3N_jVHvATKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین پیاده‌روی زیارتی جهان مربوط به کدام ادیان است؟
🔹
بزرگ‌ترین پیاده‌روی زیارتی جهان مربوط به آیین هندو است که هر ۳ سال یک‌بار با بیش از ۱۲۰ میلیون نفر در مراسم کومب میلا تا رودخانه گنگ انجام می‌شود.
🔹
زیارت اربعین، بزرگ‌ترین پیاده‌روی سالانه جهان است که بین ۲۰ تا ۳۰ میلیون مسلمان تا حرم امام حسین(ع) پیاده‌روی می‌کنند.
🔹
پیاده‌روی زیارتی تنها مختص اسلام نیست و در ادیان مختلف مانند مسیحیت، اسلام، هندو و بودا وجود دارد.
برای آگاهی از جزئیات بیشتر بزرگترین پیاده‌روی‌های زیارتی جهان، یادداشت زیر را از دست ندهید:
🔺
[
لینک یادداشت
](
https://B2n.ir/dz7708
)
🔻
@amarfact</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/678416" target="_blank">📅 16:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678415">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
رویترز: آمریکا بخش زیادی از موشک‌های خود را در جنگ با ایران مصرف کرد
🔹
آمریکا تقریباً تمام موشک‌های دقیق دوربرد و نیمی از ذخایر جهانی تام‌هاوک خود را مصرف کرده و درباره ادامه حملات علیه ایران بحث‌هایی در دولت ترامپ شکل گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/678415" target="_blank">📅 16:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678414">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55efd5d312.mp4?token=mnTpmM9d9PRdOoehOQPt24fMx6MSjK3SgIud-kO233uSn5DcG9ixHialdfHKpMcqkvYAAw8ozNmzZyRnlDVdlGbiSKVMUSt2fBZ09LS3QhAU1MtUepLpIIjJ7DDRPlSmPYhkN-eRdL5ZS6iBIhKjJC-3V7HFwCjwfleoVoDv465G7nzCaWebWFhocvbk4E2Ot8r0-kS3jO5kXacVidhIFtRoloQMBnsDvN6ezkIT1O24rusKbGkMMRVm4AEL6XpLC38j-X98FMfvvxx9etIcnDlLVRPkL1MnF57cKN7k6b9rXlaZW1fzlk5UyvupGF9-fBv5cDQzq-DQmP3zZr7cGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55efd5d312.mp4?token=mnTpmM9d9PRdOoehOQPt24fMx6MSjK3SgIud-kO233uSn5DcG9ixHialdfHKpMcqkvYAAw8ozNmzZyRnlDVdlGbiSKVMUSt2fBZ09LS3QhAU1MtUepLpIIjJ7DDRPlSmPYhkN-eRdL5ZS6iBIhKjJC-3V7HFwCjwfleoVoDv465G7nzCaWebWFhocvbk4E2Ot8r0-kS3jO5kXacVidhIFtRoloQMBnsDvN6ezkIT1O24rusKbGkMMRVm4AEL6XpLC38j-X98FMfvvxx9etIcnDlLVRPkL1MnF57cKN7k6b9rXlaZW1fzlk5UyvupGF9-fBv5cDQzq-DQmP3zZr7cGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون: جنگ ایران پایان دوره اثرگذاری آمریکا بود
🔹
جنگ ایران قابل پیروزی نبود و به پایان دوره اثرگذاری آمریکا بر تحولات جهان منجر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/678414" target="_blank">📅 16:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678413">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ستاد اربعین: ۳ میلیون و ۳۴۰ هزار نفر ایرانی به زیارت اربعین متشرف شدند.
🔹
عراقچی با استانداران کربلا و بصره دیدار کرد.
🔹
سوریه با درخواست دولت ترامپ برای کاهش واردات نفت از روسیه موافقت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/678413" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678412">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
قیمت بلیط هواپیما تهران به اصفهان ۲۱ میلیون تومان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/678412" target="_blank">📅 16:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678411">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@shervamusiqiirani-12</div>
  <div class="tg-doc-extra">آرامگه یار 2</div>
</div>
<a href="https://t.me/akhbarefori/678411" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
سرم خاک کف پای حسین است
دلم مجنون صحرای حسین است
بهشت ارزانی خوبان عالم
بهشت من تماشای حسین است
استاد  کریمخانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/678411" target="_blank">📅 16:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678409">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuEst9An-4lQIf6wtZGB9HkEq2eX1XTY6o3fO5_lhSph5f1BG2TKk4odVJk8J3zbvs-S9BoS-JP3bh8zlbYTk6CxhYy9PhgshbuHiEvXyC8ReqeQHnyOGY1SENRjnyEEuKPzrnBZmLYvQJRHCIwZnqZ3zRE7jNEt2J_JDQB8rsQlR_F5idmVPDd5-ntol-6uyf7ck6G-xECX9Zpb0SPB-gSs9KNxXtTMKJi3kxob5O2U5Iu0vF2Gb8B3PhVyft9yczk2ZOm6bOuLkKNG8BGf-j-9zpTc9PXBYYHmQYefENQ5ri71BrJ0DCpKSk0lztVdS01Sr7v3p49QXZILzOKstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمپین تبلیغاتی ارتش آمریکا برای اعزام به جنگ با ایران
🔹
کاخ سفید و پنتاگون برای ترغیب سربازان آمریکایی به اعزام به جنگ با ایران، کمپین تبلیغاتی و محتوای ایدئولوژیک راه‌اندازی کرده‌اند و در این محتوا به آیه‌ای از تورات نیز استناد شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/678409" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678408">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz0f5i0Xi2Ko-DzilVX-vhyfu_aW52c-IQTazqwgTQIrSMuQojNj0_wGWYabgWENPJBihbpAIPSrCT8je_ygM89qSActL9eQqLBqP355OCeZ3p7XBveOaMjjY591am-Xc5N8NAuyfAKC0s94gF3xlbv-zBUKQJm02zqppZpy-7idoWbSBsTwWTFMTsW4rudtQby3zAw6xyif6rQ536DluHr1vYAXMUlLjsR6fxuQjgWDLEj-MoLxnGCoc25ls2WSzBsMr9HS40am5qyQ8JO9Zl8xclZB_5pJ8S9WGd6d2kTRv_et0De2nrPfceds49214LDGU0-P2IVO4XDXjiusOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/678408" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4V1OKANM0mSVVbo7gC8lhKI9CRyXiZ_BDwtJ2AyHoya4Xx9axbmv1b8wUOmrCr5EAlqypY00ZdKKXg2eqOViJpXBWFMPswRai26Cf0R-a5MLd_d-OBHOg5Lve0iljAcVi4UZCCLJlQ1RngkCKBehL1zPYiGlDgAH3NbdI6OOH5vA3VMYoc_Ca_NlbUfFVK4Z_cc4HbNw8EDctU0infP9ZT05Efu-9TgOORIc3OWfKx5RP4HvwiBd26gimkBuiggHe6oORE2kEjtGJpUrDLlVL9oLhRd4Yj2G5uNzG3Tcw24klja9lPITIpBIgAzU7nH2Tt8q36wkH6aX2sJDnQYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HuE9xi0fVDL5QLBRJjW4vdJPtfroIH64IZi0KfCkujU8hRKUxW-_KlGefYD-x09mgQb2P_IQ26xgZcdktMeGDGnatj8h_zVlYwrkqHszElWGz8XUAB7XPVD31Ugk7NO-yofDCcpV-qSPg3zDRtZ3OckQ7Ov7KYIaeH4QJkOLnm5FH12NHAmxLAlW256iVJornOcEIKdpq-amDa-WQKUsHzIUTLYAV7PGXqe_QeLUAkVniAjRFG_Yiko11cA5kfrwJgwXag6LMOaUMjFwqjiaShV2Shdcb5sU5sNdtbFt1_9N8lYLjy-8-Noj5hxVEY_HtS-DerjACQnTJJ5fV_hTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نگاه پر از عشق توله‌پوما به مادرش وایرال شد
🔹
تصویری از نگاه سرشار از عشق یک توله‌پوما به مادرش در فضای مجازی مورد توجه کاربران قرار گرفته و به‌سرعت وایرال شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/678406" target="_blank">📅 15:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20000f14f4.mp4?token=f2ukwnVGKtdo96746fHQRAbqpJujcTk15p81JFJ1N8BYGmP9lyencGQwwCtVX8SC-guEzd7wk_1K-2wqTt243Ui3XbKo8aQ_AaH-3zu3gXR38cRks_RXLzTVhW0XnbZcDVdrbREbjxM0QHnUbZmGNBIVbXg89joe8MRxIXh6UkfPzkLgsauIrY5lD6hdwOX1ckkZQQqqxnhTt3dZpkVmuTiE3XD_HVmKHxNBWPNqUIhbkr_vohb4h9zHiM0jfPoIYyvqyclPIfrp6bVzQbooPV_cy4je2ycViEuZANu2JionVFazz8BOtGZHiDCLnO5uCHYe8d2SL9tmNfJ_sPKavA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20000f14f4.mp4?token=f2ukwnVGKtdo96746fHQRAbqpJujcTk15p81JFJ1N8BYGmP9lyencGQwwCtVX8SC-guEzd7wk_1K-2wqTt243Ui3XbKo8aQ_AaH-3zu3gXR38cRks_RXLzTVhW0XnbZcDVdrbREbjxM0QHnUbZmGNBIVbXg89joe8MRxIXh6UkfPzkLgsauIrY5lD6hdwOX1ckkZQQqqxnhTt3dZpkVmuTiE3XD_HVmKHxNBWPNqUIhbkr_vohb4h9zHiM0jfPoIYyvqyclPIfrp6bVzQbooPV_cy4je2ycViEuZANu2JionVFazz8BOtGZHiDCLnO5uCHYe8d2SL9tmNfJ_sPKavA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
چطور عضو اتاق تهران شویم؟
🔺
اعضای اتاق بازرگانی تهران می‌توانند از خدماتی مثل مشاوره مالی، مشاوره حقوقی و مرکز داوری به صورت رایگان استفاده کنند و برای گرفتن کارت بازرگانی نیز به کارت عضویت اتاق بازرگانی نیاز دارند.
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
service.tccim.ir/membership</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/678405" target="_blank">📅 15:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">یکی از قشنگ‌ترین ویژگی‌های لهجه و فرهنگ گفتاری عراقی‌ها اینه که اسم آدم‌ها رو با محبت و صمیمیت کوتاه می‌کنن.
مثلاً:
حسن ➜ حسونی
علی ➜ علوش
عباس ➜ عبوسی
محمد ➜ حمودی
کاظم ➜ کظومی
این فقط کوتاه کردن اسم نیست؛ یه جور ابراز محبت و نزدیکی بین آدم‌هاست. وقتی یکی بهت میگه «حسونی» یا «حمودی»، انگار داره میگه: «تو از خود مایی.»
شاید برای همینه که مکالمه‌های عراقی‌ها این‌قدر گرم، خودمونی و دلنشینه؛ حتی اسم صدا کردن هم بوی رفاقت می‌ده.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/678404" target="_blank">📅 15:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678399">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12c5524b92.mp4?token=j7LWSBs1_dPp_YlBpkTcvZDDwmsRbOz5Ncby_p_yJXv4-ZIoY0eWYyXo9-Ew4Som3rZpeXGTzWs21jmiOtEeMSwafFVKi0ywtw1_7_rrS2kPYb_5dQ9oEFpvkdFMn1Trgae8zbN2tyy0BMdRGiwxzr5TFgGG2YoanKNuz4e2nPvzrzP_fXytlTtRRKrQbIsBYmNEShhG5XRZjXJZu9Vf1JD8DWCo-YpGgjxrUm_Dr4RE_Jos1X_dJ2IPCWW-MmKqg_v5HzrLZ9ouG_g_rXCWDpLnFjxwsJ9KspXSIyAnk6Yi4Udb-6Bug33FcN5w1LcHy4SLJmm_9St3nvJ8LgabMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12c5524b92.mp4?token=j7LWSBs1_dPp_YlBpkTcvZDDwmsRbOz5Ncby_p_yJXv4-ZIoY0eWYyXo9-Ew4Som3rZpeXGTzWs21jmiOtEeMSwafFVKi0ywtw1_7_rrS2kPYb_5dQ9oEFpvkdFMn1Trgae8zbN2tyy0BMdRGiwxzr5TFgGG2YoanKNuz4e2nPvzrzP_fXytlTtRRKrQbIsBYmNEShhG5XRZjXJZu9Vf1JD8DWCo-YpGgjxrUm_Dr4RE_Jos1X_dJ2IPCWW-MmKqg_v5HzrLZ9ouG_g_rXCWDpLnFjxwsJ9KspXSIyAnk6Yi4Udb-6Bug33FcN5w1LcHy4SLJmm_9St3nvJ8LgabMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴
تصویر قشنگی است
که در صحنه‌ی محشر
ما دورِ حسینیم و بهشت است
که مات است
پک
#استوری
ویژه
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/678399" target="_blank">📅 15:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-R4Pfyr2NJWQ6UtgMVZ1F_-DzbMLkUhEcqh8PnwNDAFSxeNjs5ab3PSlL9ryFrln_FKjfxOZylBIgTiH0W14hvF0Hha6ClacylkZVIDQwygf1teYbhch5dodwlXyLWsj8pZ-htK3UAS2oNfn8T9l2eYA1iB869mJfeG9wQXe4mK4gQhxQC1lrEKco8yVdIDoWn7rGanOzYEqXsjmO7rdcPQkEfW30witAHqtIs0EIMSDcbDl60UQKcqwfXecQQop_R0Iq9YdFM63X9u0hvRr7g15JTfy6nRIlQuze84YXdnJX-DaCOITMF1p4QcBgFUrK3xdR3IH65DQlAisfi_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgWamGdSq07QYumiWU3LwTrOYfPktiN5kveYUz9Ca-Rsetjp_fFPrEZGpg2Hs0s691RY6HR-ghHlbr0V8Xm4t4XTboRRfx9vRe7rj9fkIoM6nlwZv0aMSZOeXhAdOzYsBh70aqejSz8VaUw4rkMkHjUHtRFDxCKb7SxLs5yWPbwvH-XVE3whhbz_moYNc90U8ZgfCaOjk3cbcBfhuegLmo-_p2GHS6XC6bycT5n_gUgA_s3rrGsUjV0izL7WjEE4eNk82hxeqHEyioM-8eKikdGwd5g95IBdcA8jp8kgtMAsvDxrgcgS2omeBVxpiCQV9NitscOiFX2cevuXDwRT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCbNPVz4YRw2dtgwcI17W1Q5zwNpldspqL4obCQxEeEKJNXRYTLUYVQYnZqEzRFgTOzCb9F0fdw1G51xCZr9cpZ6fFMHFVPArf4IVKiXIDOd4SP0vBDHzWZOCgY9NKT4kGnlIZ7QPm5L6Qly9lkxGhqIP-KD-6lDpdu6NfKUnyPOHEINDKBCpX5F9mA4OQOkNB2zzzNDxmNb8S7ZRQT_OjKD28SvXJ64QvtzEE5iwxnydEgcZ95ueb85fkj7Ih157OGpwfWxf_JlyGMDpyRVyQHC-gm6izIIy20QSV4oqIto7UTtZswCHt_KZYPh2kEKfkpgd2nG7_EMdn7Xe4dUmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سخنگوی اورژانس تهران: انفجار در شهرک صنعتی شمس‌آباد تاکنون ۱۸ مصدوم برجا گذاشته که ۴ نفر به مراکز درمانی منتقل شده‌اند
🔹
یک پایگاه اورژانس نیز در نزدیکی محل تخریب شد، اما نیروهای اورژانس آسیب ندیدند.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/678395" target="_blank">📅 15:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1364c3e1e4.mp4?token=kUgc8ZqMp08AQTdKQoTATnCz_0OxfYEmf7pplnDJHy80eNXxnI6f-XQC9A9uwJjTLfuYZgvPxW4xP7P2UfGeP9UbDqukKa3lMgATEFErqAeCDTyDuYMDH7LW9i_I6BWqUdcWzdN-LCo09ydZ0DZSh0GZKMB6RzJaU_p8xsFo9H5fokV-QwMtBIRieD11DDCfcr_sswWOoE0W17J6iGoc6scp8kMDQnAxoHEI17swdlNZC6SHXnmOI6xPFe9etGoMr1cZm00txlzdfukR73f5JNDmLdqTdjBUYlfx8KQuRelPraJldXjhLw4LPzmDyrRjPDLeFWZtfbDyksjqnYzG6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1364c3e1e4.mp4?token=kUgc8ZqMp08AQTdKQoTATnCz_0OxfYEmf7pplnDJHy80eNXxnI6f-XQC9A9uwJjTLfuYZgvPxW4xP7P2UfGeP9UbDqukKa3lMgATEFErqAeCDTyDuYMDH7LW9i_I6BWqUdcWzdN-LCo09ydZ0DZSh0GZKMB6RzJaU_p8xsFo9H5fokV-QwMtBIRieD11DDCfcr_sswWOoE0W17J6iGoc6scp8kMDQnAxoHEI17swdlNZC6SHXnmOI6xPFe9etGoMr1cZm00txlzdfukR73f5JNDmLdqTdjBUYlfx8KQuRelPraJldXjhLw4LPzmDyrRjPDLeFWZtfbDyksjqnYzG6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/678394" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678393">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd19e4330.mp4?token=u2d7CBsfj93JZ_hO-M0Wnqv1QUXi4Lu7qP9DlsMKtb6-UZS4l1TUzFLVhl17cWZ7b9KpWtDWcaVpXkyxlk5Xypfx2XroZ4tWqrSFT78YlQK7UzJNoypTMIxXnxv1X6KgRL0HU1lMlpVc1xy0iH8A5HS0oSo0V5RCDWDOd3yF0_DrLNo9RXuWoPsuXnZ85Pu5jjiMFmkp2VOYaSHRtUVxczXTPRYuyvMN4Y_E_Vnt20NrBGqu5zPFuY_nTNhz8u1XNVjL7wTup9JuVKd35aR2G_h13K5hFxCVXAlI8uOGLr5GcyLg2FihXqAca6PJ5lJ62ddlHr2HRa1_JGDRp8Xoew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd19e4330.mp4?token=u2d7CBsfj93JZ_hO-M0Wnqv1QUXi4Lu7qP9DlsMKtb6-UZS4l1TUzFLVhl17cWZ7b9KpWtDWcaVpXkyxlk5Xypfx2XroZ4tWqrSFT78YlQK7UzJNoypTMIxXnxv1X6KgRL0HU1lMlpVc1xy0iH8A5HS0oSo0V5RCDWDOd3yF0_DrLNo9RXuWoPsuXnZ85Pu5jjiMFmkp2VOYaSHRtUVxczXTPRYuyvMN4Y_E_Vnt20NrBGqu5zPFuY_nTNhz8u1XNVjL7wTup9JuVKd35aR2G_h13K5hFxCVXAlI8uOGLr5GcyLg2FihXqAca6PJ5lJ62ddlHr2HRa1_JGDRp8Xoew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم خونخواهی یالثارات الحسین در دست عزاداران اربعین حسینی در کربلا
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/678393" target="_blank">📅 15:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به یک کشتی در نزدیکی تنگه هرمز   خبرگزاری رویترز به نقل از منابع امنیتی دریایی:
🔹
یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت یک پرتابه قرار گرفته و عملیات تخلیه آن توسط خدمه آغاز شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/678392" target="_blank">📅 15:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای فارس: آتش‌سوزی مخزن گاز در شهرک صنعتی شمس‌آباد
🔹
یک مخزن گاز مایع در یکی از کارخانه‌های شهرک صنعتی شمس‌آباد دچار آتش‌سوزی شد و نیروهای امدادی در حال اطفای حریق هستند.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/678390" target="_blank">📅 15:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LojrIjkyW9UlUKsftb_YeYHQ46GE-RHFRf6GOH5O5PxZWjnDI3ueWSM8Pv8ubpEcaGGKC5bXCg-IoTQ50YPhohY9R2ujFlbFNS7rdHVZMAHMIYtDpt_o5BYEJlKxK-1ncjP6Dj8MPvjqZKbNbfE1H65R0ecrJAXloZbfc7lnbzV5sl5H-QuwwUlQKrqD4EAHUDZl_NQkOu4yY-SdpF6IlMVAC1q3dwfczzahW-qK8zxFF4gfz2SA1whxERKD_c7vJ6dULqQv1_9gmLvBh0gCJPtarrLExf5Z0A-Op__PNZjvyXWX0jwcOIKy24dMgsaaVcRNGPygLk-Ot0qNI0GbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش فیفا به ادعای تماس اینفانتینو با ترامپ
🔹
فیفا اعلام کرد اینفانتینو در روزهای اخیر هیچ تماسی با ترامپ یا اعضای دولت آمریکا نداشته و ادعای مطرح‌شده در این‌باره «کاملاً بی‌اساس» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/678389" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJDQ1f7hRzcDAdMtLZwfDKcycxz_Q2f9YPSTbabaxfuiedwVLaAyGkW2WJ0jGyyAEPPs0eOKB_Cv1PAmiHWTbam6NOzz7RviWh8qjpbrihNsK8A3dBsU_9Ke_tdTx9MNFWnj5U7Zp25GELzU99u7HWHCrxTWCND02i1yLFCMX1BPREOq0YYlC0IwZWII7o04BSXrp36IjJohuTQ9Pk_GOJsNBEukB0-wvnTgp8xlVABEXA3UdfeqiET7IsebqcDbumVR_bO1MAMrFLxjfsxLAnNrXEFAT1DyE2sqVLkYycPJbInCraoGSawvrWlTDhGo7fdaj52cFkwrEO2ymxgvdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژلی نوآورانه برای بازسازی مینای دندان ساخته شد
🔹
پژوهشگران دانشگاه ناتینگهام ژلی بدون فلوراید ساخته‌اند که با تقلید از پروتئین‌های طبیعی، روی دندان آسیب‌دیده داربست ایجاد کرده و با جذب کلسیم و فسفات بزاق، به بازسازی مینای دندان کمک می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/678388" target="_blank">📅 15:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678380">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ یه حرم فقط</div>
  <div class="tg-doc-extra">روح الله رحیمیان</div>
</div>
<a href="https://t.me/akhbarefori/678380" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
این چه سری ست که هر گاه مسافر داری
باز هم اسم من گمشده جا می افتد؟
▪️
پک مداحی ویژه جاماندگان اربعین
🏴
برای دل‌هایی که از کاروان اربعین جا ماندند، اما عشق حسین(ع) در جانشان جاری است…
#اربعین
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/678380" target="_blank">📅 14:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678379">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2ff459e7.mp4?token=gXEqgHAfudP7tts3LlMjOayE5X-LnvbL_ZRIiGmydiqEMYEKVRwmjawOArLHd5LgqSXk33oNhC7UjDtmKWvzmNPz-fg41GlwvFt6I57Y7JsSeIMs6Q4U9x5naK2UxdqFD4_SR_CsnyI_pnGLDBiJpxpk8DQC1zruV3MruQYheTB53njOYvX44kHzOJPuiyVMH7vnc105YDVuNn5_Af0xtQdhpDjEDRD3_CNAeliwxybCINPyyeZmTZSTywnTa7gEFPs0ysaEDVGxISQgVK1jP_cPl2PcblAqWLQUiHEdSJkoCu92kaAXjF4umUHsjkrX-1bMC_gu03nR424j5QGUPg1oVswvnkGkXQIIITkKsobLW_9HQvq1odat6g9ZuWIQY2k-AnV-dukg9cYBi_4QOhALNSIFQ5ZxC1I5Q7eRajdBiKmgJJWUGbi-jn7EsSpnuciIROrjUMv9aqzVzBXs1KhQU-oiziYE_JGaxH-MmjvCEzkRCBYABybEX2VJ8xXsVooplq9yl1I1xqwdNUYPpyI_xoOolnleofZsCghz3fzo7sjpvE9VvbFx2Zjhvw-VCTkesiHxFsu0jwY7aOxig5NmsyIacF-lSs3SGp5jnDCPFbqXz9S8yiw1vUcBGdO28JNbeHDwX4eYqbiEkmp7OF_eKv9_22XYA9r4yXyBrBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2ff459e7.mp4?token=gXEqgHAfudP7tts3LlMjOayE5X-LnvbL_ZRIiGmydiqEMYEKVRwmjawOArLHd5LgqSXk33oNhC7UjDtmKWvzmNPz-fg41GlwvFt6I57Y7JsSeIMs6Q4U9x5naK2UxdqFD4_SR_CsnyI_pnGLDBiJpxpk8DQC1zruV3MruQYheTB53njOYvX44kHzOJPuiyVMH7vnc105YDVuNn5_Af0xtQdhpDjEDRD3_CNAeliwxybCINPyyeZmTZSTywnTa7gEFPs0ysaEDVGxISQgVK1jP_cPl2PcblAqWLQUiHEdSJkoCu92kaAXjF4umUHsjkrX-1bMC_gu03nR424j5QGUPg1oVswvnkGkXQIIITkKsobLW_9HQvq1odat6g9ZuWIQY2k-AnV-dukg9cYBi_4QOhALNSIFQ5ZxC1I5Q7eRajdBiKmgJJWUGbi-jn7EsSpnuciIROrjUMv9aqzVzBXs1KhQU-oiziYE_JGaxH-MmjvCEzkRCBYABybEX2VJ8xXsVooplq9yl1I1xqwdNUYPpyI_xoOolnleofZsCghz3fzo7sjpvE9VvbFx2Zjhvw-VCTkesiHxFsu0jwY7aOxig5NmsyIacF-lSs3SGp5jnDCPFbqXz9S8yiw1vUcBGdO28JNbeHDwX4eYqbiEkmp7OF_eKv9_22XYA9r4yXyBrBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه ساکنان در پی فوران آتشفشان گواتمالا
🔹
فوران آتشفشان فوئگو باعث تخلیه فوری مناطق اطراف شد و ابر خاکستر آن تا شعاع ۴۰ کیلومتری گسترش یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/678379" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678378">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3b9e300f.mp4?token=G1Tb8ohfLvSXx9recP_nG-PRfUIUg3DwTR14Tuxtp6USjRSSU3VqMQPgXAaTWgPJxlFZs0p_yooSfh-dDKBg2neJ-rLalJTUQw5tgsgrlkhYs8rS-BzYb26YrwH5SDWLmSTNc1_CsuCl-kQYs4lML2TwzA_eRhiJEFF76Y5FwAmECChSFDvx0uC3165QEZKDAGCkrCo0-Gu1paQxsfeRBWuxxj_U6Q7f2Rp5dXp7-3qOPK79tAx4EjExHQpydwZPGjBOPvFPgTUAX383TMziWWTmzmR9xm9X3-YzxuVIuiOQsCL9_YcEqTa8dUOk-CegFmkqRFbino6G0BcfvcZjPoteASszNZWkGrqTvQyMb_L0_hTZU-Ja-sv_juhxqpVXrrWvSOCJCCelyiUdpFTew0J15qsTUpxaM_ZKLQj23ADeOIvOmK_tumD_cQDxXhSJP5tt3EOb44l8sBTdKG_N52IFYGSuonCJlt7i7uGtH3dtN5hszOEgFByvpOvTI40bxU91TkzBS1-DwhRU3w_XsYMDf54HJL6CDcrmImb1o50Yt3pZqFvX1Yn45hQwznYDgGGPEikzf3EaBkw8Uba5nwFLb1N_qGZ2cffVRYvCGc_bOzz1cUARdb4sWq3P2TKfjWw3j8DtWnYQut8o_oc4LDbIPToEr4sIc8Ib5LxdNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3b9e300f.mp4?token=G1Tb8ohfLvSXx9recP_nG-PRfUIUg3DwTR14Tuxtp6USjRSSU3VqMQPgXAaTWgPJxlFZs0p_yooSfh-dDKBg2neJ-rLalJTUQw5tgsgrlkhYs8rS-BzYb26YrwH5SDWLmSTNc1_CsuCl-kQYs4lML2TwzA_eRhiJEFF76Y5FwAmECChSFDvx0uC3165QEZKDAGCkrCo0-Gu1paQxsfeRBWuxxj_U6Q7f2Rp5dXp7-3qOPK79tAx4EjExHQpydwZPGjBOPvFPgTUAX383TMziWWTmzmR9xm9X3-YzxuVIuiOQsCL9_YcEqTa8dUOk-CegFmkqRFbino6G0BcfvcZjPoteASszNZWkGrqTvQyMb_L0_hTZU-Ja-sv_juhxqpVXrrWvSOCJCCelyiUdpFTew0J15qsTUpxaM_ZKLQj23ADeOIvOmK_tumD_cQDxXhSJP5tt3EOb44l8sBTdKG_N52IFYGSuonCJlt7i7uGtH3dtN5hszOEgFByvpOvTI40bxU91TkzBS1-DwhRU3w_XsYMDf54HJL6CDcrmImb1o50Yt3pZqFvX1Yn45hQwznYDgGGPEikzf3EaBkw8Uba5nwFLb1N_qGZ2cffVRYvCGc_bOzz1cUARdb4sWq3P2TKfjWw3j8DtWnYQut8o_oc4LDbIPToEr4sIc8Ib5LxdNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جابه‌جایی زائران اربعین با بیش از ۱۶۰۰ دستگاه اتوبوس در ۲۴ ساعت گذشته در پایانه برکت مهران
🔹
توضیحات علی‌اکبر پورجمشیدیان، رییس ستاد مرکزی اربعین پس از بازدید از پایانه برکت
✅
تازه‌ترین اخبار و ویدئوهای اربعین را
اینجا
دنبال کنید
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/678378" target="_blank">📅 14:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678377">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBfDxK7F0m1E8UP6wEUohRi-f1_RJxSYpwojZvI7xK88kKxWEM3oW1h1SftSijsQLg0ZVWn-90X9gJf3jfWAezw21DTIL4pyMsynR-0wA52BMu0B_E21CCfJDMQ1qcorigIy7r1crJrhUr-87L_oHQfJI2WmlLkcPsrhyDNosLkWNdzKLTzfYLdDIGFSdv0CSVTKTVVvOPoIYIzpvsk1YQ47JI9sOMdq2MuHXktcrJbXw1chow1kkUNnhO7uZdj-nOaDsWY9hzxpdpnPZpeOZoTmjoSBARec-QYz2pvc3oo8jQ_25HCE4VheNpHHf-zVSe_pCjXbIGgSwZE9Uy77dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ربات‌ها از انسان‌ها در اینترنت پیشی گرفتند
🔹
ترافیک ربات‌های خودکار و ابزارهای هوش مصنوعی برای نخستین‌بار از فعالیت انسانی در اینترنت بیشتر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/678377" target="_blank">📅 14:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678374">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63521f75be.mp4?token=epNd6xteIZAr1CWDHTfv2TSObroUSjvf6QUvdjPUi0nXUjyjhsMkQA-eR7ALCsfaQ53smhFSg8SigGEF1c9TVXXrHP4Oy57W06UM-nTnowNF1tRUmgRKeFYnaKuoy_MBqBNKvui282E6VqKcHifuwVBWTC0oMJHulPJZWkvQQ4jjvWIACNAhOYWN08DkjjTJLlMOdysYPvyE1o2u-5X-bXLWPPOk3ObUTgqq0XsIvuNCDlaC30THv0nwNcZrEwSdPbrO4aEaq2a50gaOVqZnL1DokgvoigSoGUMXubDNZX-0728-X0NYEcz_spkMMW5BxTxHukp8rsXhUOAvKu4SyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63521f75be.mp4?token=epNd6xteIZAr1CWDHTfv2TSObroUSjvf6QUvdjPUi0nXUjyjhsMkQA-eR7ALCsfaQ53smhFSg8SigGEF1c9TVXXrHP4Oy57W06UM-nTnowNF1tRUmgRKeFYnaKuoy_MBqBNKvui282E6VqKcHifuwVBWTC0oMJHulPJZWkvQQ4jjvWIACNAhOYWN08DkjjTJLlMOdysYPvyE1o2u-5X-bXLWPPOk3ObUTgqq0XsIvuNCDlaC30THv0nwNcZrEwSdPbrO4aEaq2a50gaOVqZnL1DokgvoigSoGUMXubDNZX-0728-X0NYEcz_spkMMW5BxTxHukp8rsXhUOAvKu4SyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر جامانده اربعین: آمده‌ایم نشان دهیم مردم ایران تحت هیچ شرایطی کم نمی‌آورند/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/678374" target="_blank">📅 14:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678373">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3ROiWjO8lP5ERHmS9VQ7fHKl6kP2eHIK7Syqi50dnPH48Kczmswto2FyOv15HyY-OvYh-j4YYBMK8XLQXIAvF4zEDzLYUTI9d2WtjxAqB45PIL25RXdi123BQz67gmb5esB03JgvHk9BLs1rVLDbX4gZpu7QhN4zrh6EXdL4GSsltkkKfP0AmB_wAiH4mX9QpoBM9MSgnVS5kXDK5UOZmst2JV9xryGJrf4TcHkH77W3bXfJsMA95y2YmSdx7l3GUImHP3-BYb45Esm9NEO3VN4WDQlkhJN-vkHfaBQ7Ls0uf50xVwO4kFAh6NY5B18JXZJBMnnrxsoy9TrRg5eNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از حضور سردار شهید علیرضا تنگسیری در پیاده‌روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/678373" target="_blank">📅 14:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678367">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdf615adb0.mp4?token=dqo-nOqobOFu4itemK9Q5AkTvjeLlsrawtEyQgRKCZFl4HFBwTIO-p7KI6l4zEPqTI853hHE5UV4ZLQMDBd4KBFH1CF_ZgcXGkhLkZDK_O-tDtY80wZvPTX4AblGFZw67AOKNbR30DyygS35VA0biyPnIBThQ8bufLrpagZgI2WcCU_MAeQcEA_6UzKzVc9MAenAdKEU7uGzUIrsP1aeDPmmJYS_dAPJ6UtfHUZBizKXSbSDUspHJzvShhdnSFEqlCX6ON3hWJ6ai-_qRYSZ5r1jD5hXRu72_agEp1OXUVKqDAtoYj3LY9K2jDmRt9Uh37oRqyotdewAowIbyvF7c4Q8iIJQK_EWSPSSfyr9SBA_DtnAMePZW_RBkEN0nUrt4U1PcJbNy3vh-x8O91o0MTs_O-Y-lUdNTblJBBfrDhUxZtcdYEX8BhQ8I2fzmo3FolYoVZunR7vC-LJNRpkhGhz7f-X0XsCtF-2jx9ci-1Uz2aOTQBMh9KQnXpUNX3BvgZvXKIiH-7GJMGbqqbtSa1E_B-xVHeHhLEYeihTvHUXDtqsUUV78Ezw15te9xMq4c5Kpuy2w8tMBH5cCX3y0McsvxsfS4mA7DUYmhUKkZiITjm_TK9b30Z_uSLLbsXA37l-WUg50eig_e8GppcIzAD8iF2yPeuko1vhsRbAAOfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdf615adb0.mp4?token=dqo-nOqobOFu4itemK9Q5AkTvjeLlsrawtEyQgRKCZFl4HFBwTIO-p7KI6l4zEPqTI853hHE5UV4ZLQMDBd4KBFH1CF_ZgcXGkhLkZDK_O-tDtY80wZvPTX4AblGFZw67AOKNbR30DyygS35VA0biyPnIBThQ8bufLrpagZgI2WcCU_MAeQcEA_6UzKzVc9MAenAdKEU7uGzUIrsP1aeDPmmJYS_dAPJ6UtfHUZBizKXSbSDUspHJzvShhdnSFEqlCX6ON3hWJ6ai-_qRYSZ5r1jD5hXRu72_agEp1OXUVKqDAtoYj3LY9K2jDmRt9Uh37oRqyotdewAowIbyvF7c4Q8iIJQK_EWSPSSfyr9SBA_DtnAMePZW_RBkEN0nUrt4U1PcJbNy3vh-x8O91o0MTs_O-Y-lUdNTblJBBfrDhUxZtcdYEX8BhQ8I2fzmo3FolYoVZunR7vC-LJNRpkhGhz7f-X0XsCtF-2jx9ci-1Uz2aOTQBMh9KQnXpUNX3BvgZvXKIiH-7GJMGbqqbtSa1E_B-xVHeHhLEYeihTvHUXDtqsUUV78Ezw15te9xMq4c5Kpuy2w8tMBH5cCX3y0McsvxsfS4mA7DUYmhUKkZiITjm_TK9b30Z_uSLLbsXA37l-WUg50eig_e8GppcIzAD8iF2yPeuko1vhsRbAAOfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
‌دیدم شکوه گنبد و گفتم خدا کند؛
چشمش مرا بگیرد و قربانی‌‌ام کند
پک
#استوری
ویژه
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/678367" target="_blank">📅 14:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678366">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52aedd4564.mp4?token=Npd_Z-GN4jjMLg38YiT6ZDw4gh-u_FLo2wLkLwQLayOsp5tpIVlKTd0WxI6_mgVX5eAEvFfgdn_6UvGw6SrNH3fKiEI1LvYldsX34f5eyVa9CTMdgCoQS1QtFEa4m03JIIFH-qDCzjceP6GIhymzyUiqgBuRuyxS4d7aDAnvMIlqgRZNN-oPcjaSd7bRF8_Nco-wKwHMJlW-ecWZFNLMjc2Z87qc6tx4BwwQ-DnyYJ4ZuoPhIcSNj6yzX7By4HkkaTxnkuAMCLM6wauH3sfk0NwMSof6hbkEI2b2GEAaMD6Gd6-qsziATt0FyDOLGSfo_T3PZTTZZU550KVylyS5Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52aedd4564.mp4?token=Npd_Z-GN4jjMLg38YiT6ZDw4gh-u_FLo2wLkLwQLayOsp5tpIVlKTd0WxI6_mgVX5eAEvFfgdn_6UvGw6SrNH3fKiEI1LvYldsX34f5eyVa9CTMdgCoQS1QtFEa4m03JIIFH-qDCzjceP6GIhymzyUiqgBuRuyxS4d7aDAnvMIlqgRZNN-oPcjaSd7bRF8_Nco-wKwHMJlW-ecWZFNLMjc2Z87qc6tx4BwwQ-DnyYJ4ZuoPhIcSNj6yzX7By4HkkaTxnkuAMCLM6wauH3sfk0NwMSof6hbkEI2b2GEAaMD6Gd6-qsziATt0FyDOLGSfo_T3PZTTZZU550KVylyS5Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف عجیب در مسابقه موتورسواری آمریکا
🔹
در جریان یک مسابقه موتورسواری در آمریکا، راننده در پیچ زمین خورد، اما موتور بدون سرنشین به حرکت خود ادامه داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/678366" target="_blank">📅 14:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678365">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
صدا و سیما: شنیدن شدن صدای انفجار در شهرک صنعتی شمس آباد شهرستان ری
🔹
به گفته مقامات محلی شایعه پرتابه صحت ندارد و علت این حادثه در دست بررسی است.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/678365" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678364">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
رویترز: ایران خواستار امکان مداخله در تردد کشتی‌ها است
رویترز به نقل از یک منبع ارشد ایرانی:
🔹
تهران در مذاکرات با عمان برای بازگشایی تنگه هرمز، خواستار کنترل تردد کشتی‌های ورودی و نظارت بر کشتی‌های خروجی و امکان مداخله در عبورومرور در صورت لزوم شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/678364" target="_blank">📅 14:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678363">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشستا رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab631c7c2.mp4?token=Xxw7YyISnV1VLiC1oePg4WSH12PmtDrz9O9FaLra1-D1fhjzV6m74OKFBh3nhzfRwdlpg21FnB1hs0gvFG-zI825pnz03CWVJmT3K-7wS1FhYJ2tCYIjw9Lx4VM8yj-5J8Mxz3BcQXcoGlAznFp_Vh7st_hc-4b2pdRfWpkw9y_uXeFLwL7Yc1M8hX2c2vCKYoiPj-mKvqYEqkJrhMnnDpUH5HZ9AFkMdlMAz0-ENQcJEu-EBdmyjZHMG1nqLBkMTvySHZ0XseREAoONLee_81fUwq6gCu_xqpn0eZlDdyAbkkXqBmvWKzUZRjuPat3pWDY9uFW-iSrbpmDKYs6GnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab631c7c2.mp4?token=Xxw7YyISnV1VLiC1oePg4WSH12PmtDrz9O9FaLra1-D1fhjzV6m74OKFBh3nhzfRwdlpg21FnB1hs0gvFG-zI825pnz03CWVJmT3K-7wS1FhYJ2tCYIjw9Lx4VM8yj-5J8Mxz3BcQXcoGlAznFp_Vh7st_hc-4b2pdRfWpkw9y_uXeFLwL7Yc1M8hX2c2vCKYoiPj-mKvqYEqkJrhMnnDpUH5HZ9AFkMdlMAz0-ENQcJEu-EBdmyjZHMG1nqLBkMTvySHZ0XseREAoONLee_81fUwq6gCu_xqpn0eZlDdyAbkkXqBmvWKzUZRjuPat3pWDY9uFW-iSrbpmDKYs6GnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدمات‌رسانی به زائران در شلمچه
اربعین حسینی(ع)
#شستا_کنار_مردم</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/678363" target="_blank">📅 14:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678362">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242129ae3c.mp4?token=VaX0N6X2q8Cor1p8eM_FwBcms-GrFkfAkTzgFLAUaXdGl0TNOdBUezn84rxSm0y4V__2dIYcg0yeerpC8l01WLnraqGZpbHHb98oa0htrYe5cXA9VcawFF2rzBx1zgh3ca0dB284gNzy09zKGyElGrt-K96pgNBRs22KMQomeub2BocJxOXi9gsbxSg6y0uFbZA48accyVIzutTLub-_tCXhlHiknOdRtgazTPAriVL0zxVGKDIubAz5_a1E-k1msNYQGxXrEPGBZng5Z0PLAptKsZadNWRsK7BZ3ku1h_Zi6DE_PJqsJdBe4vSM_ZTnooxFoZQeV3mm3g6Oxq4DeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242129ae3c.mp4?token=VaX0N6X2q8Cor1p8eM_FwBcms-GrFkfAkTzgFLAUaXdGl0TNOdBUezn84rxSm0y4V__2dIYcg0yeerpC8l01WLnraqGZpbHHb98oa0htrYe5cXA9VcawFF2rzBx1zgh3ca0dB284gNzy09zKGyElGrt-K96pgNBRs22KMQomeub2BocJxOXi9gsbxSg6y0uFbZA48accyVIzutTLub-_tCXhlHiknOdRtgazTPAriVL0zxVGKDIubAz5_a1E-k1msNYQGxXrEPGBZng5Z0PLAptKsZadNWRsK7BZ3ku1h_Zi6DE_PJqsJdBe4vSM_ZTnooxFoZQeV3mm3g6Oxq4DeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مخزن یک کارخانه در جنوب تهران  عضو هیات‌مدیره شهرک صنعتی شمس‌آباد:
🔹
صدای انفجار در فشافویه مربوط به مخزن داخلی یک کارخانه در شهرک آلومینیوم‌کاران بوده است./ ایرنا  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/678362" target="_blank">📅 13:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678361">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
قطر: رایزنی‌های فشرده برای کاهش تنش در منطقه ادامه دارد
سخنگوی وزارت خارجه قطر:
🔹
رایزنی‌ها برای کاهش تنش ادامه دارد و هنوز توافق نهایی حاصل نشده است؛ تمرکز اصلی دوحه بر بازگشایی تنگه هرمز و بازگرداندن طرفین به مسیر گفت‌وگو و تنش‌زدایی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/678361" target="_blank">📅 13:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678358">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df08a618f.mp4?token=QMmqiLIkfjgcEHPoy3riaDT9UeXGbJzZCYsCmI6fO-GpwQA12AFSxi1CJe45xyvxOJ-tRfPjKwdQoMy7YtGsTPPQv2zHXXP6bCcXnUshnF3uqc4HRDogKRwnj1AbUZgt3STmkqXybSTB_IYeqkcQeINnW5dKZbL58DekBsPfENtaSbDXoUJwdVZFqUuiX7FcoeYIVtw-ft1eIyHivenxnn1syro0X1SBZ2tuTGTuIlBlfXIUu33QQdD0zM1nwJbDQyDedzLCDHVHSgWIucvyJiMN0D7_xnTNQHjjbda_espCRryMkNfJDBMdp0fZVPRm09GfbbZN5eQC1jGcO_LKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df08a618f.mp4?token=QMmqiLIkfjgcEHPoy3riaDT9UeXGbJzZCYsCmI6fO-GpwQA12AFSxi1CJe45xyvxOJ-tRfPjKwdQoMy7YtGsTPPQv2zHXXP6bCcXnUshnF3uqc4HRDogKRwnj1AbUZgt3STmkqXybSTB_IYeqkcQeINnW5dKZbL58DekBsPfENtaSbDXoUJwdVZFqUuiX7FcoeYIVtw-ft1eIyHivenxnn1syro0X1SBZ2tuTGTuIlBlfXIUu33QQdD0zM1nwJbDQyDedzLCDHVHSgWIucvyJiMN0D7_xnTNQHjjbda_espCRryMkNfJDBMdp0fZVPRm09GfbbZN5eQC1jGcO_LKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه خبرنگار خبرفوری با زائران جامانده از پیاده‌روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/678358" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678357">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ3jHkeRq4CE8vQhyStR6HtiZFHd1RWew_M7OHKhgPqVmEiPNWczoq_LVeHARkLtH5Ha9leTDz7jZ3_xFH2ujhCHqpbFCNMGou7yoJ9S28KmGA5PooojFEH8jNr4G-eI8GPRyGkYLIqZr_sdOQc_aOzBC7x-JmJPiz9JFC5KGS3g0ZvgInhMC0OlJvLW-PH-vxXgVckDP9vzbo7qutxbQypfe2QkSb6Xphvfg4gpZCM5N9PyWMVr_IpCFIz5yunABQ5sKBgSPD4MXPm9-6UvApwTJeIpr6AHvD2BMcAQD5QuOh5mLFCurgvlnCf24DHhQDyKbY5TaQnRVnB3TUbPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
فضیلت زیارت اربعین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/678357" target="_blank">📅 13:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678355">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
انفجار مخزن یک کارخانه در جنوب تهران
عضو هیات‌مدیره شهرک صنعتی شمس‌آباد:
🔹
صدای انفجار در فشافویه مربوط به مخزن داخلی یک کارخانه در شهرک آلومینیوم‌کاران بوده است./ ایرنا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/678355" target="_blank">📅 13:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678354">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2QmYnlyZqivTvYqCmMDjFupJDp2Ro9_mtQcDBld-d-LdLRn2BPsvvB5oHfKtJquJe-Bf7qphy2pQwc6tyQwRN3aGelgkwTD5KCb1TU_tk4AxsxC9JXeQK8E_N7j6ENspLHOzLYW3Me5h1lvs6mKbbCHmlxp-rhFby-EnZAI1RMXlyLAMGr5jSYlRbRHpNp-2s7oiR_-ngXzhBWOhJf7u0EdXi9KEcd4CkxPMxzduQZdlqZHdZ_yAzZuMzkF7HYfHiQ5IulJT-PM637VBkwEatzPINGtGsB5Uqefj0Ro6TndsfniMg77QmY_Vv-gnMP754u-D6OJxJZJtrZhclPIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده تهران در مجلس: کارنامه شهرداری تهران در حمایت از شعائر حسینی درخشان است
کامران غضنفری، نماینده مردم تهران در مجلس:
🔹
در مجموع، شهرداری تهران در ماه‌های گذشته و به‌ویژه در ایام اربعین، در حمایت از شعائر حسینی و تسهیل حضور مردم عملکرد بسیار خوبی داشته و اقدامات این مجموعه شایسته تقدیر است
🔹
یکی از نقاط قوت این مجموعه، تلفیق موفق خدمات عمرانی با فعالیت‌های فرهنگی است. شهرداری تنها به مدیریت امور شهری اکتفا نکرده، بلکه با ایجاد زیرساخت‌های مناسب برای برگزاری مراسم و اجرای برنامه‌های فرهنگی گسترده، نقش مؤثری در تقویت فضای معنوی و تسهیل حضور مردم ایفا کرده است.
🔹
کمپین‌هایی مانند «یالثارات الحسین» و اقدامات مرتبط با نصب پرچم‌های سرخ، از جمله برنامه‌های ارزشمندی است که در ترویج و بازتاب هرچه بیشتر شعائر حسینی نقش مؤثری داشته‌اند. در مجموع، اقدامات شهرداری تهران در این مسیر، مفید، مؤثر و نشان‌دهنده تعهد این نهاد به حمایت از اجتماعات مذهبی و خدمت‌رسانی به زائران و مردم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/678354" target="_blank">📅 13:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678353">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
حمله پهپادی یمن به فرودگاه نجران عربستان
نیروهای مسلح یمن:
🔹
در واکنش به نقض حریم هوایی صعده و حجه، هدفی حساس در فرودگاه نجران را با پهپاد هدف قرار داده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/678353" target="_blank">📅 13:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678352">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekunauCYr7HieU75OTqVU7_Pw2swBCfPQM5sbKVOpUuneP0X9fOkOay552BZ8hz45hmP_YE_yF3pGuyK0G8QmGKnP9M5fgs1_-Ipxdb2tR_gJbrK_04__NMvJmusIlf7pfMAGJfUxEKgXfqj3bg0zvQXJuZgnN7XRNfnM0FqF_YhQu__mk3o2GGb6BRSK1-Vzc-4lTY9LW2Gpuy5ozzBQTZ0hNslRsSx2y-l8EmRU6yOYbp43K_OVxxMECzqFb9BWyKQHxU3lpX6fdE9EPfNQdoMeMu39g2bLG7m-Z9_F_gie5UsJOf_v_W7ytJH3BpsXGG7pfJfqF10aEeNYwX0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر کمتردیده‌شده‌ای از لحظات قرائت زیارت اربعین توسط رهبر شهید انقلاب اسلامی در حسینیه امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/678352" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678351">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3040b11d1f.mp4?token=noxvv7di8Mt1_LbRCDP8TMkyjZ1OYma5jLsO7cTfsPpGQ_zInXezqXkyqe_Rc5e0a_iDE6K2yW4NRwD-OIdmLebZUzAqMPesyfPJl_o92IeC7GpYmiHdgpbmCT6fN7hk3mcdkod1teL_CYeDMLPEqRvRqjJyihZwtpojT7IXc-KYJvFYYZLnHU7Q6k_LMoNZ7IIMQQ2wR1O2CqxmT9Y-BVpQyymHGZD7LIVhxlGN__5tTIBUnYysWCBQbQ2USjc-eQX6m-EQhfIUPvoApMf6HOUaHRvGJ_FgwKyKJp9JKLwhSZUhRRmXVNip-tLKbjNXLMLxaxHrjxg9XY5Nbps2TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3040b11d1f.mp4?token=noxvv7di8Mt1_LbRCDP8TMkyjZ1OYma5jLsO7cTfsPpGQ_zInXezqXkyqe_Rc5e0a_iDE6K2yW4NRwD-OIdmLebZUzAqMPesyfPJl_o92IeC7GpYmiHdgpbmCT6fN7hk3mcdkod1teL_CYeDMLPEqRvRqjJyihZwtpojT7IXc-KYJvFYYZLnHU7Q6k_LMoNZ7IIMQQ2wR1O2CqxmT9Y-BVpQyymHGZD7LIVhxlGN__5tTIBUnYysWCBQbQ2USjc-eQX6m-EQhfIUPvoApMf6HOUaHRvGJ_FgwKyKJp9JKLwhSZUhRRmXVNip-tLKbjNXLMLxaxHrjxg9XY5Nbps2TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبلیغ قدیمی خودروی برقی؛ اگر همه چی با موتور درونسوز کار می‌کرد دنیا چه شکلی می‌شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/678351" target="_blank">📅 13:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678350">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457e9bdb4f.mp4?token=S6h2zVXLtEgH-nFvtrygj2ebhmzUdEYFow4dcpN1uHshHbMclCV9tHx29vYPhMPMTBStq1ZjT_I7e7mOdcHfwUjkhrYiVIWd8Y1I2gBg77yb5uGgxmpVkWcmIIsW65qxqQ3nCCVW7rGHBPWA0mFYnTICccPs3rbasKwkIamUTy19mbqblMmHSLky5paVvUyqOXKoRmGWAaUDi3JEY32zxLHcukVoB0No5ICHBXmC5MiRgYQW9T5NFYOLEVtTZpx8XJdg2vG076viF62ZRu_XB9KDBsup3W8rKn82DTGGDAMnyJcN34PMekHL0HK-OssYHnMmY5PA-qo3Drz3KSwo0b_7S_eIV6yGXMYPmkeIqzoaY6FkHWjyyJzdoTsyWYHnPCImXnIzWmuYsKpLTo0rhdfGfgbmi0Bg0xVQ8krmwmphxLzr-rUhHck52GPgNIPlG0IB8Mgr7mivHFdLrwyH4rrqCmihrutVniwPxZq5yObrhkZ85fV_hv9rpHaPsOkNQIZCoM-yxB6opyHkmUZvyGTphlKBx_slfLng-2Nbta5k6NtJTBtEotwn_mtS9iwnfaN-2WCkKb6sQpTmlsY89nyG1sqNoKPtKUG5fFXR2gB3bvzUEU-piROITFPMu2oPu04FNXztnGXvZyf6TYDHpWvNMe29IENhISJXBSGW9Z8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457e9bdb4f.mp4?token=S6h2zVXLtEgH-nFvtrygj2ebhmzUdEYFow4dcpN1uHshHbMclCV9tHx29vYPhMPMTBStq1ZjT_I7e7mOdcHfwUjkhrYiVIWd8Y1I2gBg77yb5uGgxmpVkWcmIIsW65qxqQ3nCCVW7rGHBPWA0mFYnTICccPs3rbasKwkIamUTy19mbqblMmHSLky5paVvUyqOXKoRmGWAaUDi3JEY32zxLHcukVoB0No5ICHBXmC5MiRgYQW9T5NFYOLEVtTZpx8XJdg2vG076viF62ZRu_XB9KDBsup3W8rKn82DTGGDAMnyJcN34PMekHL0HK-OssYHnMmY5PA-qo3Drz3KSwo0b_7S_eIV6yGXMYPmkeIqzoaY6FkHWjyyJzdoTsyWYHnPCImXnIzWmuYsKpLTo0rhdfGfgbmi0Bg0xVQ8krmwmphxLzr-rUhHck52GPgNIPlG0IB8Mgr7mivHFdLrwyH4rrqCmihrutVniwPxZq5yObrhkZ85fV_hv9rpHaPsOkNQIZCoM-yxB6opyHkmUZvyGTphlKBx_slfLng-2Nbta5k6NtJTBtEotwn_mtS9iwnfaN-2WCkKb6sQpTmlsY89nyG1sqNoKPtKUG5fFXR2gB3bvzUEU-piROITFPMu2oPu04FNXztnGXvZyf6TYDHpWvNMe29IENhISJXBSGW9Z8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
این روزها با قطعی‌های برق، داشتن یک چراغ‌قوه معمولی کافی نیست!
🔦
چراغ قوه دستی ۸ کاره LED Torch
هم چراغ‌قوه است، هم پاوربانک، هم ابزار نجات!
✅
نور LED پرقدرت
🔋
قابلیت شارژ با USB + استفاده به‌عنوان پاوربانک
🧲
مگنت قوی برای اتصال به سطوح فلزی
🔨
چکش شیشه‌شکن اضطراری
🔪
تیغ برش کمربند ایمنی
🚨
چراغ هشدار برای مواقع اضطراری
🏕
مناسب قطعی برق، خودرو، سفر، کمپینگ و نگهداری در منزل
❌
قیمت قبل: ۱,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
قبل از قطعی بعدی برق، این ابزار کاربردی را تهیه کنید.
https://memarket24.ir/product/brief/30291/180124/</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/678350" target="_blank">📅 13:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678348">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbLSq63bB_ddYs7T4sHd2BZLXxEgFyAWPbVZobQLu1KWUdK51rWMZQ8pwBv79HgJOZUU5TiFr079pEZ4npvZ_98EEQlKTUrPhWX4zKUeYCUFarAzBcVFw8PF-IxUOq1bM89G7hAcB2LWzcpaNxHjni8LpgBexWySx5OxvkXVpAf-WKtB98vw_LZ1BpxgPQgaVORKG3KFhbZ6DyQ5zzE5HPko6rYKnopBZ-p0SSBPGR2L9RytLudgF24hXAZHgg1kfwlDzbaHOjvp9QED2FsMw9AyMJJwTBDKnaD6X9HBpO_4oVet-Ix-dqjBcVxRpMheN7zKdKi0xkhUxp9cdeHjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-VuTx89Gqa9cSA8ve_qwIkpiLlq-Yu4Pta-ZBy2ZFSgPXL1fDTFgFgCgjDlyXzcG42XKlwcVDZlbb_477VOFYcwt3MFxaozJsTTxmcovsiBLvsGFwRfCQxa8uGTvsvHmw1qtLPYXT071KLMj2zZ-G5AK1R-BGBoJkgke0MveTrbJxKNbQefuiR1qcZn_lEJ-AFWLSxm0xz7Ok59tc1yB_7IflyEwcHJNgU8QO2vbo3QF1yoEk17GdYBYJabyS_IuItnqF38_c7hTSDHurhIRIDQ1FOsiQS2eRs7T5xuPi98eYGsHC5f2qqJUPAEReORxUKjmOJvPo1YqGZNN9ICcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور سید عباس عراقچی در حرم مطهر امام حسین (ع)
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/678348" target="_blank">📅 13:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678347">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843e1723da.mp4?token=mxXrrS7gXdGOuN9hjwuLuzLYe0QHl2kCJemXtg1dRD-I4z4nkLSsgy8VtFxsPp5MrEok8LDxtpm1EsiiOJuY1awLyl-KgcesfCu9Ub2XzGYH7xui98RZxj3gxVKm76iRNe0-RSNWovPNkgabI7GHd0dGV_pq2riXN9vctBYkfffp46A118hJTrkDK8KGU-K7GV3pY9sB1xklN8blU49dvxiyutyWitkZ0j_4OmtPNw8BwBWrvl1dncwuldjkd5DRxIZWb_srp0IgRJyA3mkWX7WCbBM3PBcBZQE8bdOL012TCc4GI97FyqzPGptqXdQnEy-7GzgfwijrjbDrSQe6mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843e1723da.mp4?token=mxXrrS7gXdGOuN9hjwuLuzLYe0QHl2kCJemXtg1dRD-I4z4nkLSsgy8VtFxsPp5MrEok8LDxtpm1EsiiOJuY1awLyl-KgcesfCu9Ub2XzGYH7xui98RZxj3gxVKm76iRNe0-RSNWovPNkgabI7GHd0dGV_pq2riXN9vctBYkfffp46A118hJTrkDK8KGU-K7GV3pY9sB1xklN8blU49dvxiyutyWitkZ0j_4OmtPNw8BwBWrvl1dncwuldjkd5DRxIZWb_srp0IgRJyA3mkWX7WCbBM3PBcBZQE8bdOL012TCc4GI97FyqzPGptqXdQnEy-7GzgfwijrjbDrSQe6mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری | به نیابت از رهبر شهید در مسیر اربعین
🔹
روایت قدم‌هایی که در مسیر اربعین به یاد «رهبر شهید» برداشته شد.
🔸
الوفوری را دنبال کنید
👇
#زیارت_به_نیابت
@Alo_fori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/678347" target="_blank">📅 13:25 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
