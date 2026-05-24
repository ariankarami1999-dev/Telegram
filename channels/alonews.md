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
<img src="https://cdn4.telesco.pe/file/bdiIB1ufgds_E3tQk2lgIldjwrghyjnbu8VHMsHfO90aRfeGHMD78K1QwVAQdHyE15gIgA06awTCG08tFtHFacIggDVfS_ywEF7P_2gnhLHn2wEauSHUSxG-xGOsiXSQFJaRFliJOQLv4eyETUiPIPP-MbE3KHDsGBo6s8MpRroxOHMPO5RYSr1ZLj_aonFHwdRY6SNR02MGD8tmiSbdvgKrZsNU45rwFXAlL8-P0jEJWibaATh5U1FffdIvzVGbWHHmdYHKfvpQUOQCgiAGBjRxSHjWkEMRyokzky0bBf1sYlGj4pSHw4e-PyZ65qt4eO7QO4J-4dmzspcv5s379A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 03:23:07</div>
<hr>

<div class="tg-post" id="msg-122454">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
هم اکنون هر بشکه نفت برنت 99$
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/122454" target="_blank">📅 01:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122453">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1GkbcPuMcbci7mCbmZlntHoP8Sx_i2kOra49h9bpmOTxQPVTFopdMS0xDyAYJlghFSc4KRtsPmtQKBakMstP6953xbeJudb3Unn6fRszyPbLUJLHxUg-gz5i8D61aFcev27_27pkUCTyqF1zR0yDPRoZ8V6SYvw49LhOBdIolRi8Gk6acbA9DCkd-WWzn09A-_ymSSl8V1iwEvzY8_LaXVZUx1k68Nb-qcE2O1785YjTtvrEukuKHxALpg5FvERHR5HTYKCX0y_Z6k76ByYMVpODEMML7G9l-jWXssu8Mwv_rhX2ORd7hiRvb0inHp2MT6miSONsCzhqfgG900Rsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه: قیمت نفت در آغاز هفته جاری در بحبوحه امیدها به توافق بین آمریکا و ایران، 3 درصد کاهش یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/122453" target="_blank">📅 01:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122452">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ntT1-8vCe8HXCdZnZ26dfnVfrkav7PpoqJ6KCA_IvHB6d2C0mc47Ov38uKjNuMNFAT-108BrxQyk4FWfCw6WPrQLXdW1tKRyC196A3zJCZUigM8B3nMRVWTURmmaNYh8-RWMG_fVilVXXhQf9zmcS74_Y0iMzmqrdg5dfbDPBPDcLDa7mL893q2p987z4OdT38nH8Ur0RMUW-r4tmPx1nyAehGsxoD6JE-6Gh-xBnlMuaVrD0NbBF17qPtagrXpnKpQgr-ewc0uNH0zbs8PKIyEeHpq9he0sFSY2Xja4dhG_EicBcEsZtjDkxGfaF0lp1r6cnnOk_C1OTigGdWUQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکنون یک هواپیمای هواشناسی و کنترل هوایی (AWACS) بوئینگ E-3 سنتری نیروی هوایی ایالات متحده نیز بر فراز خلیج فارس در حال عملیات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/alonews/122452" target="_blank">📅 01:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122451">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">💢
فوری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/122451" target="_blank">📅 01:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122450">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: آمریکا و ایران به توافق اولیه برای بازگشایی تنگه هرمز دست یافته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/122450" target="_blank">📅 01:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122449">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نشریه آمریکایی پانچ بول نیوز:
کاخ سفید از قانونگذاران جمهوری‌خواه خواسته بود که آخر هفته جاری در حمایت از توافق با ایران توییت کنند.
🔴
به گفته دستیار ارشد یک نماینده جمهوری‌خواه، برخی این کار را کردند، اما برخی دیگر «از این هراس دارند» که پس از پایان تعطیلات مجلس، مجبور شوند از این توافق دفاع کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/122449" target="_blank">📅 01:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122448">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122448" target="_blank">📅 00:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122447">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56627faf8a.mp4?token=MwVnjxI-g5nwP3be-4LVG32w041mc9EsG2fjQO8vAHLee6AZ0RyjI3eDJWle7WqkCU9XtS1dsHKOAauYYgbunh5iq_cZa-OBtbX8rOZoV7hfHaj3olsFu3XY0mOqKK7RYvPhDHBaJzRU7KHipZ5asuiGKzbCMBCnW2D-tW7g1T9bbDkAk27OTkRUhx0o1WqwLJ2GCp9_Drr-DlclAXhX9ylv-IIICqb5WfOj53wUL3fa3M4MBQGMOZ33_B-_DJhqYcy1aOtz_DWHUFg91ngW0AK6lsllUH5g914-DsViPe3-yxVWeQ2eVqqfui8P7LX_qBaAMfiIePPBhRHfghem4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56627faf8a.mp4?token=MwVnjxI-g5nwP3be-4LVG32w041mc9EsG2fjQO8vAHLee6AZ0RyjI3eDJWle7WqkCU9XtS1dsHKOAauYYgbunh5iq_cZa-OBtbX8rOZoV7hfHaj3olsFu3XY0mOqKK7RYvPhDHBaJzRU7KHipZ5asuiGKzbCMBCnW2D-tW7g1T9bbDkAk27OTkRUhx0o1WqwLJ2GCp9_Drr-DlclAXhX9ylv-IIICqb5WfOj53wUL3fa3M4MBQGMOZ33_B-_DJhqYcy1aOtz_DWHUFg91ngW0AK6lsllUH5g914-DsViPe3-yxVWeQ2eVqqfui8P7LX_qBaAMfiIePPBhRHfghem4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش‌بینی‌های کاملا دقیق و حرفه‌ای نوستراداموس زمانه؛ استاد خوش‌چشم تحلیلگر صدا و سیما.
🔴
فقط اینطوری کار می‌کنه که هر چی گفت، باید برعکسش کنی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/122447" target="_blank">📅 00:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122446">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyzpw32t_GGuPBZ_r88TjoSwv17wHAFwgKnTLplfvKf_AGJZchizzr-0iVuFvUOsmpk5yZviLujrZhHOM_q5cBUUXaRoLXvTP4O9mRXqp0oNaqRccMEmg98P9VGI6gnK3gL1cu1IVQzSqYinqmzrdnpyse-AZsXP06HsC3kx7Jg_T6l_T_5yVD35Zjb0GrphvYArUXryrCXAJmsybvwveSIZRetSQYBA-fnLAUPLZYWZrmWIOP9MUkbAGKvwrDSM8nzNUboITAg9sF2hUr9uY3dwQEVV2mBvKpzZgVYIFbD3HAxnCC1ItL5n3e1-xWTSt24DEBYhBRZ8ccrvKNt8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی : دست روی ماشه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122446" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122445">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کانال۱۲عبری: نتانیاهو در تلاشه تا توافق رو بهم بزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/122445" target="_blank">📅 00:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122444">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
تسنیم به نقل از یک منبع مطلع: تا این لحظه تفاهم نهایی حاصل نشده است و چالش در بعضی بندها ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/122444" target="_blank">📅 00:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122443">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HqDXq7nErn2CnoysBPYDFYCuaVaAHzJFyeuBa_L0iB46jVFWcxn8V591IEWWPKqSCT67JA8c8-ISuBkuD5esynrk0ge0BjiUbfsjapdoqw6XAtsDRadGTuqEfA_fTdW5tyoyzq19BgAwY2XIhSk_ZBsOEciwYWIHrvqCT8ROvvu0s0e55ro092Hl9nf7v0L5NZLs930pHSAnSgbw9nDRtfqHLeOFDvS423WzWIUH-msoUgp82DkJtGtmUnh-rOATivWv6akLYma3vq-yKvO9JFIUGmvkO2BslvAk9ModIwp5EAwHyY7Kf9DCIamqR_KF7ajvNy8OuORbUXXwYT1Y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییتِ سخنگوی فارسی زبان ارتش اسرائیل
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/122443" target="_blank">📅 00:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122442">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
همزمان با سفر رسمی نخست وزیر پاکستان به چین، دو کشور تفاهم نامه‌های همکاری به ارزش هفت میلیارد دلار امضا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122442" target="_blank">📅 00:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122441">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر در تماسی با وزیر خارجه عربستان، درباره تلاشهای میانجیگرانه پاکستان گفتگو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/122441" target="_blank">📅 23:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122440">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فیلمی که پیامد حملات هوایی اسرائیل را در شهر دویر نشان می‌دهد که منجر به تلفات متعدد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/122440" target="_blank">📅 23:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122439">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ae03c828.mp4?token=YAlzkOoM3jKklFlxc5Kex67dzcKtDtkNkghFimW5y68xd3QrlegmaIqfsSZkhc_lA7dnjw-5zmN64Lz6s61kk0ho48Q_MyvuDT9KELI_KQlHf6yb-46XUC7rZfCrKAzlc8uq8sKepZv6BO44NumA3c4kc6tO9H-J-RHzzUis28u9r2UfWzFLyPhc2GV96H9mNFtdvA_NFotJLfjJtvhN9OTHXFYzscIHQKDBs1HLFaCMhnKGVeYQ2NJAtxGyNP8GyKVP99y2jMyD0ZC4GVWljugBSjZ848UzL4UNNtnlgkOB9_1qzzl_C5pLAP1xwJ_eqYLOMR6cD0BP8aSGrg1b6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ae03c828.mp4?token=YAlzkOoM3jKklFlxc5Kex67dzcKtDtkNkghFimW5y68xd3QrlegmaIqfsSZkhc_lA7dnjw-5zmN64Lz6s61kk0ho48Q_MyvuDT9KELI_KQlHf6yb-46XUC7rZfCrKAzlc8uq8sKepZv6BO44NumA3c4kc6tO9H-J-RHzzUis28u9r2UfWzFLyPhc2GV96H9mNFtdvA_NFotJLfjJtvhN9OTHXFYzscIHQKDBs1HLFaCMhnKGVeYQ2NJAtxGyNP8GyKVP99y2jMyD0ZC4GVWljugBSjZ848UzL4UNNtnlgkOB9_1qzzl_C5pLAP1xwJ_eqYLOMR6cD0BP8aSGrg1b6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی که پیامد حملات هوایی اسرائیل را در شهر دویر نشان می‌دهد که منجر به تلفات متعدد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/122439" target="_blank">📅 23:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122438">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه «فاکس‌نیوز» گفت دونالد ترامپ، رئیس‌جمهوری آمریکا ممکن است به ایران هفت روز مهلت دهد تا به یک توافق «قابل‌قبول» برسند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/122438" target="_blank">📅 23:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122437">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نیویورک‌پست: احتمال رسیدن به توافق بین ایالات متحده و ایران به طور فزاینده‌ای کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/122437" target="_blank">📅 23:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122436">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به طور خصوصی اذعان می‌کند که اسرائیل در حال حاضر توانایی محدودی برای تأثیرگذاری بر رئیس‌جمهور ترامپ دارد و فشار آوردن به رئیس‌جمهور آمریکا دشوار شده است، طبق گزارش کانال ۱۳ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/122436" target="_blank">📅 23:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122435">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سردار نقدی: اسرائیل و آمریکا ۲۱۰۰ پرتابه و ۳۰۰ موشک زمین‌به‌زمین به جزیرهٔ بوموسی شلیک کرد اما رزمندگان ما بدون هیچ ضعفی ایستادگی کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/122435" target="_blank">📅 23:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122434">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
واکنش پسر ترامپ به منتقدان توافق با ایران:
🔴
ما باید افرادی که فقط با حمله زمینی به ایران خوشحال می‌شوند را نادیده بگیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/122434" target="_blank">📅 23:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122433">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92bc8959c.mp4?token=uzyQzNeLQqRf1ptv3a4_xoKJkfnuxBgXv8sWEtpnCTLiOcDAfglo-aJo7WskEByfI86w06Pq9NzCPK_h0tDbRjQ9vKCe35MRJ3DdImmuNuAjQFDs3Jd62rXqyqum8nVQXWLl46qCPH6VFtL829f3ZDU_eFdwQ-K0wJsQjhewXMlPA4XFYl2NVtcqdVE1MOC3YlCKOZP6kUoMdiW39rT91y0so4WfDGLL438sQxlHkbQ7tC4HW5-jrei03L4Zle8k84uYTwMgIZAlVO720lt8OelNSqGS_A_v5LxCGw1u2WgytHSOEli2dMi-4NAbFfZyuqiVnkkslOdWYS2rF6G6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92bc8959c.mp4?token=uzyQzNeLQqRf1ptv3a4_xoKJkfnuxBgXv8sWEtpnCTLiOcDAfglo-aJo7WskEByfI86w06Pq9NzCPK_h0tDbRjQ9vKCe35MRJ3DdImmuNuAjQFDs3Jd62rXqyqum8nVQXWLl46qCPH6VFtL829f3ZDU_eFdwQ-K0wJsQjhewXMlPA4XFYl2NVtcqdVE1MOC3YlCKOZP6kUoMdiW39rT91y0so4WfDGLL438sQxlHkbQ7tC4HW5-jrei03L4Zle8k84uYTwMgIZAlVO720lt8OelNSqGS_A_v5LxCGw1u2WgytHSOEli2dMi-4NAbFfZyuqiVnkkslOdWYS2rF6G6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زنده یاد مانوک خدابخشیان:
خدمت دوستانی که پنیک کردن از مذاکرات
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/122433" target="_blank">📅 23:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122432">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس با تاکید بر اینکه اداره تنگه هرمز به وضعیت قبل از جنگ باز نخواهد گشت، تصریح کرد که  این تنگه تحت مدیریت ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/122432" target="_blank">📅 23:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122431">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوووووری /  پست جدید ترامپ!!!!!!!!!!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/122431" target="_blank">📅 23:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122429">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9UpdoqPgnLIAwJbmm2vThKpvgr6fI9TTW7X3PMO3X2fC4zPMUnBs7shcnzUMv0LRCQW7AnDOVExs9OgB1cHob5OByPGDgbP98nrQtxLPA_auOQpT1Uj7M3iGBGi3t9AKdL5TiNikQYXDihlHSGmSOQLGkGL4NBNKdODU1reSxwIRM2xIjNiKPOl9Pbc9u3XpEtzf_UWlUEiBZAllNi7iUwQtzzk9IqRT6SCmPkQtyslXbkHnEe7cF5WB78hDfA-9MWJKd7dQhXiOTlk2H4vlLs5PRf-unQfJBJgQPxljHEV_89plXxb6zvXf45k1zcJ7P0P_vabgOjtT1ZfQ-HoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووری /  پست جدید ترامپ!!!!!!!!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/122429" target="_blank">📅 23:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122428">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/en_gyFWDg0a2r3u2lfaaJs-sOJfeiVizHc0zY8950C0H_AXuDceJkBO3jI8RVfb19QB1Ur6uau1tEpzeqWGpVvrxWYtLuuL6EqMh9FWIBj6xcvUNxVZwXRf_sApTAX-A9W_5V-d0nNwtegeLDoFj_L5bjAu5kqQQJC8eez3gWdsAvO4qggydDfDlfjtq3xLBKRx06DT3JNL8R8w9mgNSTydqyaqtVXq3aY6m7AED34PAmlSIMiTMUhTaAPn_BK2Ppqgu-DX18KdKsvyNLWvCrd2mXsY96r9I-hMKM9gFvwWX5AxTfJd1PSPp3YEZBCUh_1huJpyKUgSYgw6fbBYCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییتِ سخنگوی فارسی زبان ارتش اسرائیل و طعنه به ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/122428" target="_blank">📅 23:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122427">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=ekzgLgOjkxreIugv3N7EtAMryb9iUqSj5ICkKDe2qi9i4cmfbtAfjfY-UIiwT1T5AOqL6DxA19BcxotsZ2F1hPTIaEmC2BCUakHhF1oG5BUAG71AaSTv2MsoXn-qNzTh8cQ4YVzsO7Sjk9hQ9n9DNjFAKcPIjYUVW2PGFbn9Bnf6wGLzJck6jNnzOuAVLJtF_JqHTXtzExjALss3zu4rj9V4DRvFLoFyCcOAsH7O_kkhsmsTzWm29cZ99mbsfWSQU5_M7bANd8P1Z_swI13DUB-P_Rt2-bicWe_AT8bgaJ8hqs8xo1U1Xpn0EalnFq_erc4BX3ziNbyuidgvKAliFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=ekzgLgOjkxreIugv3N7EtAMryb9iUqSj5ICkKDe2qi9i4cmfbtAfjfY-UIiwT1T5AOqL6DxA19BcxotsZ2F1hPTIaEmC2BCUakHhF1oG5BUAG71AaSTv2MsoXn-qNzTh8cQ4YVzsO7Sjk9hQ9n9DNjFAKcPIjYUVW2PGFbn9Bnf6wGLzJck6jNnzOuAVLJtF_JqHTXtzExjALss3zu4rj9V4DRvFLoFyCcOAsH7O_kkhsmsTzWm29cZ99mbsfWSQU5_M7bANd8P1Z_swI13DUB-P_Rt2-bicWe_AT8bgaJ8hqs8xo1U1Xpn0EalnFq_erc4BX3ziNbyuidgvKAliFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
این ویدیوی کوتاه که توسط حکومت جمهوری اسلامی و برای ایجاد رعب و وحشت تولید و منتشر شده است، بخشی از روایت ۳ دقیقه و ۴۶ ثانیه‌ای بازجو خبرنگار،«محمد نگینی‌پور» است.
🔴
این حجم از کانتینرهایی که گوینده ویدیو هم به زیاد بودن آن اذعان دارد حامل پیکر عزیزان کشته شده در اعتراضات اخیر و سندی واضح برای محاکمه عاملان و آمران این جنایت علیه بشریت است. صدا و سیما هر تولیدی که در رابطه با کشتار مردم دارد سندی روشن از قتل‌ عام شهروندان بی سلاح توسط حکومت است و باید ثبت و نگهداری و مستند شود.
🔴
تاریخ انتشار این ویدیو در صفحه شخصی شبکه اجتماعی این بازجو خبرنگار ۲۴ دی ۱۴۰۴ است ولی ویدیو روز ۲۰ دی ضبط شده است.
🔴
محمد نگینی‌پور، مستندساز است که پیشتر در رسانه‌های وابسته به سپاه پاسداران از جمله خبرگزاری های فارس، تسنیم و مهر و شبکه افق صداو سیمای حکومتی فعالیت داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122427" target="_blank">📅 23:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122426">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1VbO7-cPQRLluTtSIt0CI7344GaIZjqRQpaCGI_4hwhpt-L91NMSMt9hv97Fb-rnjKRsoRRr_EU1JOM-1Ui3UDDNfgFRd4kzSs_eN317nNM-YVg8goc-sNgDZ3c9ViwOij9OPgEF7T9-SDrgsgvHpEO6TP46dOpYuhIzLTpZ4VZS61n0EopGkiV7I7CcgEQGXf3ruyFYjl2RcquTn_DUBvVq77NI_652Mla40eUOQzo-3i8Pq55rpTd7lI-w78IjZgO7eqFBkkAkE7wVkYYpVCxqpBLWlT1Beu_d3XpJyve-XXfxxI-WEXPfN5CB9e0p0H-tuFLjTI6owiqZFAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش دیوید ونس، پادکستر و تحلیلگر مشهور آمریکایی به خبر احتمال توافق ایران و آمریکا:
🔴
ایران ۱ - ۰ آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122426" target="_blank">📅 23:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122425">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی به شبکه فاکس نیوز گفت که هیچ توافقی «امروز یا فردا» امضا نخواهد شد و افزود که رئیس‌جمهور ترامپ تمایل دارد به فرآیند چند روز دیگر برای رسیدن به نتیجه نهایی بدهد.
🔴
این مقام گفت که رویکرد دولت توسط سیاست «بدون گرد و غبار، بدون دلار» هدایت می‌شود، به این معنی که ایران بدون برآوردن کامل تعهدات خود، از تخفیف تحریم‌ها یا منافع مالی بهره‌مند نخواهد شد.
🔴
تفاهماتی در مورد انبار اورانیوم غنی‌شده و بازگشایی تنگه هرمز حاصل شده است، در حالی که نگارش نهایی همچنان در حال مذاکره است.
🔴
آمریکا آماده است تا در صورت شکست مذاکرات یا تولید آنچه آن را «توافق بد» می‌داند، حملات نظامی را از سر گیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/122425" target="_blank">📅 23:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122424">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
آی ۲۴ نیوز: مقامات آمریکایی می‌گویند ایران تا زمانی که انتقال ذخایر اورانیوم غنی‌شده خود را آغاز نکند، هیچ‌گونه تسهیلاتی در زمینه تحریم‌ها یا آزادسازی وجوه مسدود شده دریافت نخواهد کرد.
🔴
در عین حال، ایران بر این باور است که آزادسازی وجوه باید بخشی از هر توافق‌نامه چارچوبی باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/122424" target="_blank">📅 23:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122423">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvY5wNEDYDPsXOrKJ0OBJrjwwMNC9HJDLtI_Xi5E1AAMurVC-NVlRXQUNLOpkvPqjgTL6XXVR75MAbm4q_L015JEgpaeWO9NKyVgr1EnbqUJFFNvRCEc1pkzSXuq929ij8PmTa4LwVVP71AsmsCEFSFcVn7OlOIzRuCDbGqlA-fTzHiwrtBqaFzYdH3Ly96i_TEW-Mi4FiWZ0St7cFoOEGpkm1TCN1AVRWg3Tbc6JoD-qjog4QaCfKffj7r3WSY7g9JavnS2FSPjt--MbbgeBifWdiQ3B3_110LodrCDadOpBCECV2jNl23qsoKeAJ9o56y92ztwUgq543mP6ME-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کشتی HMS Lyme Bay در حال بارگیری مهمات، تدارکات و پهپادهای دریایی شکار مین در جبل‌الطارق مشاهده شد، در حالی که در مسیر حرکت به سمت منطقه تنگه هرمز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/122423" target="_blank">📅 23:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122422">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFZWXtH_SAPp4FMHGzvn4onyMO6i7uSa0trwPPw93zkkncyzXm7N0AeH69_xfO18gbzIm2e7xmbI6ketuL_qfawbkmBqCMcZ0Bi3IG97euO1qlAv7cZyj2pIjQhhD7W0S14DWOVtGDk9YmR3ifNp_GEgCCMzQanqtjnHdT34JGMPF_Acn3c0kEMg_Ve4MhJ4dak92jYNGsFXXJO0OevzHCtaPbA9w1pEd6e1aYLKMyRcnn6G-NYI4tRQLJLfva73MA9NVNXfnfCKwWoHv2wtHRuL0PtxjhasE5BTXI_KYhoh32C1kqfIbixrV5tqNjNRWNyREcmpF8Ul_r83MEBPoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122422" target="_blank">📅 23:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122421">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزیر خارجه عمان: گفت‌و‌گو‌های خوبی با غریب‌آبادی داشتیم
🔴
همچنان به حمایت از تلاش‌ها برای کاهش تنش، پیشبرد همزیستی مسالمت‌آمیز منطقه‌ای، امنیت و آزادی کشتیرانی ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/122421" target="_blank">📅 22:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122420">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB_PMKnKeDNGUnFOqFUoTObfF8bfWRIngzniYxJ8_iwO_8PW49T4amTkp8Bf1968VDvpc25rhjNQHmPfQEOxSNY0JzMxjVv1tyCIyvhrqeveaUSHc8_dv2rhGIi7TMWMEOy7dhEUzLVEBY1yGVJATdHgbEBvZHXFOyNoBvh5M1t5GtpuvI8XcjYz4ecKiZr6L-xFGVnjhaKoxhCjrGSZatI1g0WiCdsLhZcEEIuPX0j5X13D5gkYxzUKsaE7WaCI4Zuumv7pGQacoGbPDt7dxBpPFen9IBXLREl6n7NaekR9y810p-T6wLX8tkhlDObbRuYbNSyKo7dZlZdRV9k2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای بلومبرگ: با ادامه مذاکرات، ابرنفتکش حامل نفت خام عراق از خلیج فارس خارج شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/122420" target="_blank">📅 22:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122419">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPQ-EncS6KVNBLdxEevGFiXBuVye1IGL0LRjhgnGYMZOdfK93BNHfAgRR3Q4SLnwPFafO7SqSHD_rHnkGjx3rAsn_ov6_lc_I-g8q0pCyjPgLPl5jJrrFOudQsAEdXv-HPEeDxkMl60WhZKpxh01mQp-D_Xpq3bPitTztkC4tIOGkSc1qu1ljb650xGss912kVl8PMkPGr_Y1cL1YkLfrIVcT1Kw32DE3QNd3tNhyT1TH1OOVLpaenHSoFjZRtkuD9eUMYeJmKzEJYTU6bqZZSsuvDVkvqZaKzzj5o2wyuOxZ84zwDXr2YfcVL9QvwBjW58btA8AWX4WLqn0dQb6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ جونیور در اکس نوشت:
این یک پیروزی بزرگ برای آمریکاست. ما باید افرادی که فقط با حمله زمینی به ایران خوشحال می‌شوند را نادیده بگیریم.
🔴
پدر من قول داده بود که جلوی دستیابی ایران به سلاح هسته‌ای را بگیرد و این دقیقاً همان چیزی است که او به آن دست می‌یابد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122419" target="_blank">📅 22:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122418">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
اکسیوس: ترامپ از چندین رهبر مسلمان و عرب خواست تا در صورت پایان یافتن جنگ ایران با یک توافق، به توافقنامه‌های ابراهیم با اسرائیل بپیوندند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122418" target="_blank">📅 22:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122417">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
روبیو: ایالات متحده کاملاً از تلاش‌های دولت مشروع لبنان برای بازسازی، بهبود و ثبات حمایت می‌کند.
🔴
اقدامات اخیر حزب‌الله یک کمپین عمدی برای بی‌ثبات کردن لبنان و حفظ نفوذ خود به قیمت جان مردم لبنان است.
🔴
حزب‌الله در تلاش است لبنان را دوباره به هرج و مرج و ویرانی بکشاند.
🔴
ایالات متحده قاطعانه در کنار دولت لبنان می‌ایستد تا اقتدار خود را بازیابد و آینده‌ای بهتر برای مردمش بسازد.
🔴
دوران گروگان‌گیری کشورها توسط گروه‌های تروریستی به پایان خود نزدیک می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/122417" target="_blank">📅 22:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122416">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d3f10d05.mp4?token=p5uT9vtnaW1cvwJrmm2FCkiI9p_CieFXXfgFn0wAMJRusRUmOxbDgwlftJ8QVypdiS3KCL4lFX9gktrvQCCou9cfs-DgC2oFQTdsKnCs89ZRZoyBMFbudRjMh6kmjmElXQE5lP_qqkfVMZq10oiMI6pCjj85xhZlvbDVSGrAjIFDon90idNIMPo354tJZMgePWOYCwFwbllXY-M0r7U72yfjE8dXXZwYFi_T_zrGG-WbcVWcWr9bOr0fImVmHs2Hw2qNRcBonrOd_G3tablMv82zd85LvpZriACsnfYwh49B5J7hyLxUkv8FWih5UujxEGjs1LXro4u80wLDjLhpqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d3f10d05.mp4?token=p5uT9vtnaW1cvwJrmm2FCkiI9p_CieFXXfgFn0wAMJRusRUmOxbDgwlftJ8QVypdiS3KCL4lFX9gktrvQCCou9cfs-DgC2oFQTdsKnCs89ZRZoyBMFbudRjMh6kmjmElXQE5lP_qqkfVMZq10oiMI6pCjj85xhZlvbDVSGrAjIFDon90idNIMPo354tJZMgePWOYCwFwbllXY-M0r7U72yfjE8dXXZwYFi_T_zrGG-WbcVWcWr9bOr0fImVmHs2Hw2qNRcBonrOd_G3tablMv82zd85LvpZriACsnfYwh49B5J7hyLxUkv8FWih5UujxEGjs1LXro4u80wLDjLhpqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سوم خرداد، سالروزِ آزادی خرمشهر
🔴
نقطه ای که میتونست جنگ تموم بشه و جان یک میلیون انسان حفظ بشه ولی با طمع، هزاران نفر کشتند و آواره و شیمیایی کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/122416" target="_blank">📅 22:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122415">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
یک مقام ارشد دولت آمریکا به سی‌ان‌ان ادعا کرد که توافق بین آمریکا و ایران هنوز کامل نشده است، اگرچه گفته می‌شود مذاکرات تقریباً «۹۵ درصد پیشرفت» داشته و دو طرف هنوز بر سر بخش‌هایی از عبارت‌بندی و متن نهایی اختلاف دارند.
🔴
این مقام ارشد دولتی گفت هدف بلندمدت آمریکا همچنان جلوگیری از دستیابی ایران به سلاح هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/122415" target="_blank">📅 22:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122414">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رسانه‌های داخلی: آمریکا مانع آزادسازی پول‌های مسدود شدست، احتمال لغو کلی توافق وجود داره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/122414" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122413">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0235b6f6f6.mp4?token=EpEMgMvIhHX4N775FmaRL_8wsQqsTANEU8JkKPgh7R6I8ZLwa3E0rY0-b8JMF5nxoyW26bO0Dx7196p97tk3oiZbDfujQa3CRe1jRaAFfzZZVN5B2fg_tHOZwoJJyFEgUvq3C7ZAgW2z9Yv50_pJhxR_CcLi8DjCIoGyPZ1-76Cb_F5do8MOFvvLzz-rnPNudwtZ5mrZJascXoaG42QCdXOhnERd04XCjEogHmD1CAVGJzkecczfUm0Ac_sU4wftSZyKCxaPx5TST2wYTiigqZjG1OxZG94pD4rOJQu8h1Zhn1V9ltL0uAzpdncCGgzmXyxE_WElLOaHHYdoJW_0UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0235b6f6f6.mp4?token=EpEMgMvIhHX4N775FmaRL_8wsQqsTANEU8JkKPgh7R6I8ZLwa3E0rY0-b8JMF5nxoyW26bO0Dx7196p97tk3oiZbDfujQa3CRe1jRaAFfzZZVN5B2fg_tHOZwoJJyFEgUvq3C7ZAgW2z9Yv50_pJhxR_CcLi8DjCIoGyPZ1-76Cb_F5do8MOFvvLzz-rnPNudwtZ5mrZJascXoaG42QCdXOhnERd04XCjEogHmD1CAVGJzkecczfUm0Ac_sU4wftSZyKCxaPx5TST2wYTiigqZjG1OxZG94pD4rOJQu8h1Zhn1V9ltL0uAzpdncCGgzmXyxE_WElLOaHHYdoJW_0UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون هماهنگ کننده‌ی فرمانده‌ی ارتش : نمیدونم توافق چی هست، سر چی هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/122413" target="_blank">📅 22:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122412">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
منبع آمریکایی به الحدث درباره لبنان: توافق آمریکا و ایران شامل همان بندهای ۱۵ مه مربوط به آتش‌بس است.
🔴
پیش‌نویس توافق آمریکا و ایران شامل تعهد به پایان دادن به خصومت‌ها در لبنان است.
🔴
اسرائیل به واشنگتن اعلام کرده که هر توافقی با تهران باید آزادی عمل آن را در لبنان تضمین کند.
🔴
پیش‌نویس توافق بین واشنگتن و تهران شامل خلع سلاح «حزب‌الله» در لبنان نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/122412" target="_blank">📅 22:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122411">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ادعای منبع آمریکایی به الحدث: مخالفت‌های درونی در حزب جمهوری‌خواه با برخی بندهای توافق با ایران، اعلام رسمی آمریکا را به تأخیر انداخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/122411" target="_blank">📅 22:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122410">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر امور خارجه ایالات متحده مارکو روبیو گفت که توافق احتمالی با ایران حمایت منطقه‌ای دریافت کرده است، اما هشدار داد که یک توافق هسته‌ای نمی‌تواند «در ۷۲ ساعت روی پشت یک دستمال کاغذی» به دست آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/122410" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122409">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقامات آمریکایی: محاصره دریایی بنادر ایران امروز با سرعت بیشتری ادامه یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/122409" target="_blank">📅 21:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122408">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: اگر با ایران معامله‌ای انجام دهم، معامله‌ای خوب و درست خواهد بود، نه مانند معامله‌ای که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری واضح و باز به سمت سلاح هسته‌ای داد. معامله ما دقیقاً برعکس است، اما هنوز کسی آن را ندیده یا نمی‌داند چیست. حتی هنوز به طور کامل مذاکره هم نشده است.
🔴
پس به بازنده‌هایی که از چیزی که هیچ نمی‌دانند انتقاد می‌کنند، گوش ندهید. برخلاف کسانی که قبل از من بودند و باید این مشکل را سال‌ها پیش حل می‌کردند، من معامله‌های بد انجام نمی‌دهم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/122408" target="_blank">📅 21:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122407">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نیویورک تایمز: یک مقام آمریکایی می‌گوید ایالات متحده و ایران در اصول برای بازگشایی تنگه هرمز توافق کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/122407" target="_blank">📅 21:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122406">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c8f1a7b.mp4?token=av9QjLaizKB5XfojyOsqMvUnCGVFcqRUPbMHxdKlIvCK4sO71NM9tbUCmnpGQ5pfhGWEryaoeYLJC7KJtU21Mr2MegnGr33Or3LP1akO30mx-eYfYXkpUPDFRj4nc1oZP6roCAtE4G2FuTmfvtTN50UKPLqIsmaF8XvJOLa1Lvm9vSCrxUqkS8_xDW-QAcukvpu2ylcuBgI9HEB9OT_YEanxAjsceLsOMDGXosjgruYnKu0Y37zUmEtV44inxWUrpRXX-Wxp8UVnw6xzL6TfI3OZKR0E0Bg6mGPVYeYj9jcPM8s2GI8ilgdChgoQC_kFA9PJV60ua_06QDcDFxotbSWxLSdQ0oGgcWEKcAjMzkaxezX2BMvyWnwmKyM_-McVLqLZ22fNqkqufoDDLZD1WF0QsVqerZYv6A-2kL-HX8GfdVhJ3VXDP6Rm0psNWQ7KZ0vFAEUl_mq1opk8NwkW4fsY0nolQJ52_SD5W8NZam1fuBxZkqrHAHlTi3dLsccEdGLlNCzjxQPkO6YR1stSs8n_zw7e-dVoHNkTgZydgVKsDWtnaoqqaPh367Sd8lzEyk2yeitktOc3CXjqCjLxmMry9FOCEqXRxo7TXUyx2_igSKsM_LCj6ymvdyYVv3_PGOnY2JXZlemtJHfRL7qSTxIVx2z6YLgamDwESRKK1mM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c8f1a7b.mp4?token=av9QjLaizKB5XfojyOsqMvUnCGVFcqRUPbMHxdKlIvCK4sO71NM9tbUCmnpGQ5pfhGWEryaoeYLJC7KJtU21Mr2MegnGr33Or3LP1akO30mx-eYfYXkpUPDFRj4nc1oZP6roCAtE4G2FuTmfvtTN50UKPLqIsmaF8XvJOLa1Lvm9vSCrxUqkS8_xDW-QAcukvpu2ylcuBgI9HEB9OT_YEanxAjsceLsOMDGXosjgruYnKu0Y37zUmEtV44inxWUrpRXX-Wxp8UVnw6xzL6TfI3OZKR0E0Bg6mGPVYeYj9jcPM8s2GI8ilgdChgoQC_kFA9PJV60ua_06QDcDFxotbSWxLSdQ0oGgcWEKcAjMzkaxezX2BMvyWnwmKyM_-McVLqLZ22fNqkqufoDDLZD1WF0QsVqerZYv6A-2kL-HX8GfdVhJ3VXDP6Rm0psNWQ7KZ0vFAEUl_mq1opk8NwkW4fsY0nolQJ52_SD5W8NZam1fuBxZkqrHAHlTi3dLsccEdGLlNCzjxQPkO6YR1stSs8n_zw7e-dVoHNkTgZydgVKsDWtnaoqqaPh367Sd8lzEyk2yeitktOc3CXjqCjLxmMry9FOCEqXRxo7TXUyx2_igSKsM_LCj6ymvdyYVv3_PGOnY2JXZlemtJHfRL7qSTxIVx2z6YLgamDwESRKK1mM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:هند می‌تواند ۱۰۰٪ به من و کشورمان اعتماد کند.
🔴
اگر به کمک نیاز دارند، می‌دانند به کجا تماس بگیرند — همین‌جا تماس می‌گیرند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122406" target="_blank">📅 21:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122405">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
العربی الجديد: تلفات انفجار انتحاری در قطار در ایالت بلوچستان بیش از ۶۰ کشته و بیش از ۱۰۰ زخمی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/122405" target="_blank">📅 21:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122404">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBC2WOg6Wh7qpHrhkpMPtowIHPUNrSCOwIfgmCH3aDzRcSEUB1t82VrRxEe-axyuXtN4bHLms3ZKuKLTj8fD1WD0x3PaLXB7NN8gPgXqMWYuV9ICiW__aSWBocizcVkfTnmFIhCw3e-BlPgU0FulTRgKDmmZ_JaZ3MonQeZSfmBbSrw2i0xHxv2Es99-G7BtNwN3XNRNl0u4dpg2q62LiHabRVTKP6nbUR_XVm2AC5JF51dr1405GHeaJbswDAHt9FveW6rgBOdB1Xt3PPOYgsjMNA0QjSp7h36oTiCjhGCamC7EH-O43L8rkWapAcCFiyBife86bs6DBUUZ7KV81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه وزارت خارجه ایران: در موضوع آزادسازی دارایی‌ها که مورد اختلاف است در حال حاضر راه‌حلی برای آن وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/122404" target="_blank">📅 21:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122403">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ادعای یک مقام ارشد آمریکایی به آکسیوس: «ما در نقطه بسیار خوبی هستیم اما راه‌هایی وجود دارد که توافق می‌تواند تضعیف شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/122403" target="_blank">📅 21:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122402">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
اولیانوف: برچیدن برنامه هسته‌ای ایران خلاف ان‌پی‌تی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/122402" target="_blank">📅 21:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122401">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
یه مقام ارشد دیگه هم به Axios گفته :
شرایط خوبه ولی هنوز راه‌هایی هست ممکنه توافق خراب بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/122401" target="_blank">📅 21:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122400">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
عارف: حتی‌الامکان خاموشی نخواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/122400" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122398">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiRQlFYbdEvdDEdVJKk8CM8VHLKmxPvKVi1DTF3EemyE5nPicaQLPrLTD6Rxkve34IlC7gybrurWWK456uqKbNkkMU3CEBRpNIOfqzx7vxHRlWVczlCzGfS5RckgeKW4qxGkM6DodyIn1hv-iiDFjfUliP7X0WY67jeTf0hDwNaarl7j4HNJL9xWgHufQ9i3Wimyf8aMxuQ4TvVWCMFETjHGAr-hYMkl2TeJX8LK-mKKTqH2rFdRJJwKloHpXbiW1u8ic621PZkkkRf3Dm_GhcaRYgyGqPu57nZAq139JqdxTiQIstKJp0038-N5OEuwdNVVY2ZaI4drhvBD0wCCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray
🗯
گیگی
120,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید :
@v2safeBot</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/122398" target="_blank">📅 21:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122397">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ادعای واشنگتن‌تایمز: آمریکا و ایران پیش‌نویس توافق صلح را ظرف ۲۴ ساعت آینده اعلام می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/122397" target="_blank">📅 20:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122396">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhc63T9wPyTES98iKGtaXLkhvQu1w6GPjHFwSKJ3I5sTLNXpDRfYdC28ppAQjl_zgxeEBo8JfGIFFu6o07KoJPSFfbgPLPw5t9ijEC5wOf6iuKu90SHpeNhLpW-UjZU-R6R9Xh_jQtFUlHbwC3PfjQ43KN5Is3I7aJCwETbWDwI6s3cU-G4uXKT9ZUUH6tqH5seH1Trui-cKa9MJq_Jw6sBvkOdZhOq6GRRMqffEbwD_8Vl1wtuc3VbKIA49Ln6zLlvWAD8HmgAH6cM79JKKf35-eHyzw7iNOMw0eoN0kzhmmezu6mwR8GcJmyiPBwev6iFYLXPWbS_ybHE50ZRJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۳.۵۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/122396" target="_blank">📅 20:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122395">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل هم اختلافات بین ایران و آمریکا رو تایید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/122395" target="_blank">📅 20:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122394">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فاکس نیوز نقاط اختلاف در توافق ایران و آمریکا را اعلام کرد:
🔴
1. اسرائیل خواستار تضمین «آزادی عمل نظامی» علیه تهدیدها در لبنان است و ایران این را رد می‌کند.
🔴
2. تهران خواستار آزادسازی فوری دارایی‌های خود است و واشنگتن امتناع می‌کند و اصرار دارد که این موضوع به فرمول نهایی توافق مرتبط شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/122394" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122393">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
پسر ترامپ: پدرم بهم قول داده نزاره ایران به سلاح هسته‌ای برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/122393" target="_blank">📅 20:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122392">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHAm5M24S9wgKqu4yrczy9ILq5ezrmLZX8-3hyRBD0b4VPzYT_pMxHGWbzh-b9hMYxiWAh9_J74IZAq2r-aAFxpSYsFY8shxU_3C8dbYRVFzsDb-AjKc1A4NmFb-LeSAeag-JyF6V6gWUmNdQ73sC0Clwk3lB6Tgont1AiZJEqa0AM0VDnAEoZt-nTL2ZlpjA9NfFrDnFSt-1yDP_-ae7y4gvXfwHPlF3pgwbC3ys2u_bQZMnAOI5ZUk_JW3SOdAk3v0S2P5x9Q-wyOzTFclh1tt5x0rIBm4RemumkEuZVmN9_8LxKMKiU9rfLLGk-vqdTnMFuNEctHhMZnI8xjwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/122392" target="_blank">📅 20:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122391">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
خبرنگار الجزیره: حملات هوایی اسرائیل شهرهای شرقیه، کوثریات الروز و زوتر الشرقیه در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122391" target="_blank">📅 20:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122390">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
تسنیم: علیرغم برخی گفتگوهای امروز، کارشکنی‌ های آمریکا در برخی بندهای تفاهم از جمله موضوع آزادسازی اموال بلوکه شده ایران همچنان ادامه دارد و تا این لحظه این موضوعات حل نشده است.
🔴
بر این اساس، در حال حاضر همچنان امکان منتفی شدن تفاهم وجود دارد و ایران تاکید کرده است که از خطوط قرمز خود برای احقاق حقوق مردم کوتاه نخواهد آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/122390" target="_blank">📅 20:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122389">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / علی هاشم خبرنگار الجزیره: کمتر از ۲۴ ساعت پس از ظهور خوش‌بینی در مورد امکان توافق‌نامه ایران و آمریکا، حال‌وهوای منفی دوباره سر برآورده است.
🔴
منبعی آگاه ایرانی به من می‌گوید که نشانه‌هایی از عقب‌نشینی آمریکا در دو مسئله مرکزی وجود دارد: مکانیسم برای از یخ‌زدگی خارج کردن دارایی‌های ایرانی و دامنه آتش‌بس در لبنان.
🔴
بر اساس گفته‌های این منبع، توافق‌نامه شامل چارچوبی برای آتش‌بس در لبنان است، اما گزارش شده است که اسرائیل با این چیدمان راحت نیست و واشنگتن را تحت فشار قرار می‌دهد تا بندی را اضافه کند که به آن اجازه دهد تحت توجیه پاسخ به «هرگونه تهدید»، عملیات نظامی در لبنان انجام دهد.
🔴
ایران این فرمول‌بندی را رد کرده و بر یک آتش‌بس پایدار و ماندگار اصرار دارد.
🔴
تهران به تمام میانجی‌گران، از جمله پاکستان، اطلاع داده است که تا زمانی که تمام بندها به طور کامل توافق و تضمین نشوند، توافق‌نامه را امضا نخواهد کرد.
🔴
گزارش شده است که پاکستان پیشنهاد داده است با بخش‌های توافق‌شده پیش بروند و نقاط اختلاف را به تعویق بیندازند، اما ایران این رویکرد را رد کرده و اصرار دارد که بندهای مورد اختلاف بنیادین و غیرقابل مذاکره هستند.
🔴
تصویر کلی نشان می‌دهد که تهران فزاینده‌تر واشنگتن را در حال عقب‌نشینی از تفاهم‌های قبلی که از طریق میانجی‌گران حاصل شده بود، می‌بیند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/122389" target="_blank">📅 20:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122388">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل:
ما آماده‌ایم که فوراً به نبرد با ایران بازگردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/122388" target="_blank">📅 20:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122387">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
طبق گزارش فاکس نیوز، ترامپ می‌خواهد توافق پیشنهادی توسط مذاکره‌کنندگان او، از جمله استیو ویتکوف و جرد کوشنر، اجرا شود؛ اگر این شرایط برآورده نشوند، هیچ توافقی صورت نخواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122387" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122385">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تسنیم: کارشکنی آمریکا در برخی بندهای تفاهم تا این لحظه ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/122385" target="_blank">📅 19:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHjJU87iSQ8jbN5TDQM1C3YX1I0CEB7Z30boDV0d6THlOXn9eSPeEBLy-UaVOSAen8f51St9dSllHx5x0jm9Knoo3_KGwST3M-DCONXZv6GhfFmj1Wy7-xq2LrPra1Ewljw8l5GUdS-0mAZL5DqjJXhWkMvQxOey8vDIz7mtflv1GKEVDk8oVQ0-GFHPRqPn9hOulK3ImQi1-0CXtgoqcxgh_SflavqWkIoffT6MSpPeIirF7mTpGQ5dD-O2rcE2Smf6CF_q01UzHRestGvnYk5brz9MRdev0dmvDT4xTZMMMGFtuth_sGTpq1s2FBF1Vo0dw7ODroB5TfwRnL72Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGpgu79X6brJR8E1zlIBRZimp-sibkO1fBZrvPukNN3XbiqFXqKu4xPO9LjNXM1UTFq03h0HDbty2B6XtDPDRD3h79I-tEK4OEJDwJiaca0aT7WT_3NAIfgixqoAgPFQubq9Mvplf68HNiKV5Fzu8Zf22tG_II1nz6uMJJ4tJNDzAGEje3LqQGIBYOB-EokJ2Cv6e2gfv-Fl_UG9H2syraPuVRjNn3AroOcyqBJX3ZXGg_odjN8Er8PnN-LignxA5KQ_FO7Oi0I0l-IbVtvY6lDKdtuYjzo6M_KCoNdsUb6GS1aYCB9KZb_ine5aUPrl9smeYTWSXxBc_Dq7m6Tp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uy3IRo5ny16N-p3xGurLZysDppMOHUaNHSSs2t82oWVSTJsW2AGllD_jpFHIhR4NNW00UpH3lXlgsYUE-Wulk_acIDDb7eTq02h3JU1tqan08SRry2zZoMYuLEcmMQg5w9e0ZO2XDq_ydMcdod7RhkvydMlE1vjoB8Q1SfOS2vGPVX6VZ9h1Q35NAgHQTqbff8OaJuFvLxbbR-LLe5K0P1lZV9UPRh024qXRll3Gtz2fGkZ-W7qcWTWh8DwSxc6vIrkjmhTslPCv5BMKeHE1k2jOs2pLt9f3JxD378Dt78_OgQCwK8_UP7yMg-xRabDllHCp2SRnPc6LRU8dgFUbBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b49bac95.mp4?token=rZWeTafMnOTV7AL3SfliEZ1bmedy0trarRwoEbEUV2fIE2KhuJeELFan53SyFFNDv3-s40racCfEiPagEakSgLTM1CjQy0XxVx1R1m4viSJY-qyvefKlBlf7DiG-W4EXtQnqSEvkXqvhoNyCnYVo5MXs78a2K1FP2yS85-p3bp-3tmdLCJCyiCWAhumtgWMqcuAG-olHFmvsHRx3Zceeoydnr5PACaZx6gzO-kncCy0bSD_cw41tVGGoFOA2fyJ2_3iSGyrSZ0vc_zQOAsWMoqaEfoJK2gkivEp7rbhTzxwgfzn1qRyUdzdhGyqhYBMemrlseZgzdXAjDpIaVdUmtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b49bac95.mp4?token=rZWeTafMnOTV7AL3SfliEZ1bmedy0trarRwoEbEUV2fIE2KhuJeELFan53SyFFNDv3-s40racCfEiPagEakSgLTM1CjQy0XxVx1R1m4viSJY-qyvefKlBlf7DiG-W4EXtQnqSEvkXqvhoNyCnYVo5MXs78a2K1FP2yS85-p3bp-3tmdLCJCyiCWAhumtgWMqcuAG-olHFmvsHRx3Zceeoydnr5PACaZx6gzO-kncCy0bSD_cw41tVGGoFOA2fyJ2_3iSGyrSZ0vc_zQOAsWMoqaEfoJK2gkivEp7rbhTzxwgfzn1qRyUdzdhGyqhYBMemrlseZgzdXAjDpIaVdUmtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به زراریه، سومور (دره البقاع)، كفرسیر و سر الغربیّه در لبنان حمله کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/122381" target="_blank">📅 19:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: خلع سلاح را نمی پذیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/122380" target="_blank">📅 19:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز: موضوعاتی نظیر ذخایر موشکی ایران و غنی‌سازی اورانیوم در مذاکرات آتی مورد بررسی قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/122379" target="_blank">📅 19:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
یک مقام آمریکایی به اکسیوس گفت: برخی از جزئیات توافق با ایران هنوز نهایی نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/122378" target="_blank">📅 19:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122377">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: مسائلی مانند ذخایر موشکی ایران و غنی سازی اورانیوم در مذاکرات بعدی مورد بحث قرار خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/122377" target="_blank">📅 19:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122376">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
منابع به المیادین: ابتکار چین، تنگه هرمز را از نقطه تنش و اختلاف به نقطه‌ای برای توافق و حل‌وفصل به سود همه طرف‌ها تبدیل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/122376" target="_blank">📅 19:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122375">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
یک منبع اسرائیلی به سی‌بی‌اس گفته که به واشنگتن اعلام کرده‌اند حتی در صورت توافق با ایران، آزادی عملشان در جبهه‌هایی مثل لبنان باید حفظ شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/122375" target="_blank">📅 19:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122373">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXwZ-ztoNig0CQX7iGtlABxvMYP15XsAFmPz9lTkCWH8DE5AW_RwP5JOCkj09TKPcmV9Z5qTnzeQEMzWH92Haa4i3pE9OxwkqW2BEW34tfudILlQIyMBqt96-zBAo09mzBumoiaiuLsQIP-hbNGhKS5l6aICP-Zvd4fyudeN9TFlsO4LkawDyOzSQB2Ab30qcDZYoMTQPWDPS1q-Od_sc96P-hJhRzyTRfdTRra1Wdw9598o8RD3jM-lpYTnKTayJSnL_cIEDmD_pecGfRlPZVjxN5ijP_8yqSQa1CcUOkE7fuYmlOgstIL4US3eVwmkI1cHVpgZFFcukpOSmF0pYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvR8QY0Kja4N5wyM2iuY5xRXurzoT2Oo5GOhWNgW2h3SBP5zEAjkgsNpxf4O2cH2s9IvdJyNRioJRAnVke93tYelrJl1Y8Y8e8U29B2Jsw5fCX8ghcnBEMwg1emc9qI1iyxbR5fLXfI-srFYei0OQEmy0VyzgZ4V-aO_2pE5FPIH084QZ3BMJIKMUV5uBw7ZOBLnYo8A3n56DeyW2xtRjTtOv9JK2B11deXK-adDdWLfnlEKyCxTQIrM7N7B2N-2xpNcl6m9I50Z2ADOeZDNiZYYV6MBqxReaAcSTJWliinEwR5DUYIjhlo_6bcxM6Qz9F4OPGqtqJ_WVBzm-6V4xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اسرائیل دقایقی قبل حملات سنگینی در جنوب لبنان انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/122373" target="_blank">📅 19:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122370">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUELXwrRDgx4KGBMfPEPDWkVoZUN2hjso5k62AwnMzsXMijAVoitTyGd6NMWdx0OI6lovWj5kUT6xMy0H_emKscldkik0r58Zhthsz1WVJGxz79Z990RyUcn6KnlFdQU0dmXbIN-b4ynMeBzQXeqmkSqWxnJvQ0FQyD9_vr6LlnmdUkLEQaw9v5VoBdPeapGctJ5d0zpx8gVq2H37JxXFoF9oOBnhf9cwlbf9DK00nfMdjIA8zHIwZzY1vQVhATJe5TC2ygsDfNzKlqnZtqJue2Yo2ew_FnrpPW7FTJbY6etqEd2hoSOs_PLpQiHpFN_l9MncioSfvjON83SgXRJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSbjfy4kWqfAkLk-R78hYV_eMqShu0Wzez3iph_X8GsvqkHCu64GYm-LquBhJTVlVtoSgKMKwEcOl3fuHTTAk8bZRt3ytTXv9W1lUAE0n-_YwKt-x16hv0OJsC_9KNqMqIGthy8e-pYEJmYJ-GhJw2XTH9RMJUPdxR5_JgaADyLQNb0b0yLF8zGEIQwFjw07tSTEetfkOBliwXfrhY04472_4Pd9WiGa1Ga40W9J1ALpHf63ZU1ZwL9EiXkhPDCx527N9F8dptDvCkB_ZUe4XCKDpLjJOeY91txYUI_WflEGih-gch5LAq21lubWz41V_UnHz23TzYU9WxMzmEZgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUQSTO1TGw04YCeUJvA_sJR9RapeGEME-e9YqhW2XkNegTVCarySQ_DGwUzxJfQiUAYWjzR9Vicyba5OStBc6N3VFgCtGNT4ih41o7vI4CCtvPXONm-CL8uC5OK8-jOWQh_tnVurmWV-wBydfd6at8BwaC70E3KIdb5n89lT0tEVWMaTVRZ9nTLdQBqC2kBznuiDF_ZpszXEDLtcqWhC-CRcQ6aHrc-kyUFgjAu4dD3EdAErFJSdf_pwtHMDLmBoW4cePAUCHtzi2cKyyx8jTLsz3W1GUq0EiygFXZ-9GZjhWwTsHa-NGj_uiATvX63e0h8ewOhJrcZnwV1KXuYnww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
معاون بین‌الملل وزارت خارجه: نشست مبسوطی میان هیئت‌های عمانی و ایرانی برای بررسی مجموعه‌ای از اصول حاکم بر عبور شناورها در تنگه هرمز با رعایت امنیت و حاکمیت ملی دولت‌های ساحلی این‌ تنگه و در پرتو قواعد قابل اعمال حقوق بین‌الملل برگزار شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/122370" target="_blank">📅 19:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122369">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuwWxfpqQ8svxLISH-ra-m_1IJfwV2cuy3DaM03ZhOXiMEsDTyFAQAe36wuetdngwoswczYfeKp6NYShzT3IjAJ-WCXPF3aisRpGnEWlj1Tcrtac74HZVuX10ZqgdskvfBjenR64OqgiBd9k4lmX4Hl6VqzYadXK52BWMJ-VLyomD_Qy2Wu-U1fSrXXEPJ5io8i2nt9laOb-5bgiqkdBCSpiH8QCpxHRVXQI2MAsIZR5RuL1Iiq2_ymUuIiil6EGg85u9vMeVzoIfymR-YccJ6SxCPSc90ROvGNNKX1P5whsqoHWzsttHoPeSS4ED95flmbOpRuUL2WpxbD0BAJJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: توافق ایالات متحده و ایران برای بازگشایی تنگه هرمز امیدوار کننده است، اما کشتیران‌ها همچنان محتاط هستند و بازسازی تأسیسات تولیدی و ذخایر زمان‌بر خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122369" target="_blank">📅 19:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122368">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz_VuoYm9cpuItyp2VuuA61AI4Usas6agg7oY-3m1iDHNNr1krnP-l50iKfqWvl4fFL2yT7kbruk_s5XJxRcUbwPppHAYst__mdDvHbtT9ZhgjSJ3eNHU7epDkaAIxhruu3xg6zJRGUGxDQf0epUhoHDAp90gpM85fKjtfAXEjXXBow8PMwlARcZyRNSnoflXpphA03IW-xEFr7LLT1gxBvuL-ouQWadKiP2u2NfaCkUDhutNn-IaQ17EW3VJPmYztl_x76JMuUb8R5YKwxfiz9F7xBNiTEOjb20Pwa7nhVKkrwd8pBuUMGzINt8-jbGqvQT5vGigs0F4ge6RsmaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: توافق نهایی با ایران به معنای برچیدن تأسیسات غنی‌سازی هسته‌ای و حذف مواد هسته‌ای غنی‌شده است.
🔴
توییت جدید نتانیاهو: من و رئیس جمهور ترامپ توافق کردیم که هرگونه توافق نهایی با ایران باید خطر هسته‌ای را از بین ببرد.
🔴
این به معنای برچیدن سایت‌های غنی‌سازی هسته‌ای ایران و خارج کردن مواد هسته‌ای غنی‌شده از خاک آن است.
🔴
رئیس جمهور ترامپ همچنین بر حق اسرائیل برای دفاع از خود در برابر تهدیدات در هر جبهه‌ای، از جمله لبنان، تأکید کرد.
🔴
مشارکت بین ما و دو کشورمان در میدان نبرد ثابت شده و هرگز قوی‌تر از این نبوده است.
🔴
سیاست من، مانند سیاست رئیس جمهور ترامپ، بدون تغییر باقی می‌ماند: ایران سلاح هسته‌ای نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/122368" target="_blank">📅 19:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122367">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuTdYZM2uqCJWNxCMXy5vVSOL-KJezJVHtLyiYVZ6YA3ufxN2nDoOvBCWFeuuEy11ySk_jn4IYGrmluA2x7o36eqMx5-7mrgqU25tpI5S3VaBklOaVbFLb73cGXI-6XAmGkmuPFDNGC4_zDEloo0RLxy2pedIqWM-sGjHmBt6ohm8x_4oyo_GtdtOy672VlHfUL5zM_weTZSc-n9vuqYvxObNNhBSGhle-8J9chvyPPC5w5QtWHva2lKs0kQkgn2UEpmqUffQyPjnjpRXdHMhpSp0YBPnHgWSpDIgCn80O0yyC5EI5mVLcxxVaj6ViWZX9HDEi62IXxfik7LwtpR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ سخنان پزشکیان علیه سلاح‌های هسته‌ای را بازنشر کرد
🔴
پزشکیان درخصوص سلاح هسته ای گفته بود:  ما آماده‌ایم به جهان اطمینان دهیم که به دنبال سلاح هسته‌ای نیستیم. ما به دنبال بی‌ثباتی در منطقه نیستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122367" target="_blank">📅 18:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122366">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_mnA7MvK1P4vUboiXvVwj_-N7RJ7jAP-6wvHaB19TE68wn9oJOzjEQ5qiZfxl0Kuf2qmRQn7scA8CNaQVHnXsFFdXhAUWy4IwmcIuRHghDUAKeaJ97Slr7Vx9iaE6r-cAnPkwKfkRuoiWI9kwTSAnFcYliyG0YDR14me0HQQIzEAx-HyCIv1lsmAAPQqOqRuE1en7HL5Ax4i69uq0c4vAroA9xIp6eI9RhucG4JNjmjgfQs914xUhd5z23xBmSzBAXqd-cnboB4DczgvluZH8V4REAbNWrs391WX0zeZY_ESTuEVUaNYHR3Z5FquBR_E4eZsh9h2Y2TGvv3ol448w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز: یک مقام ارشد در دولت ترامپ گفته است که توافق با ایران امروز امضا نخواهد شد، اما پیشرفت در مورد یک توافق را نشان داد.
«اگر ایرانیان در مورد مسئله غنی‌سازی تسهیلات قابل توجهی ایجاد کنند، ما نیز تسهیلات قابل توجهی در مورد تسکین تحریم‌ها ایجاد خواهیم کرد،» مقام مذکور گفت.
در مورد مسئله هسته‌ای، برنامه فعلی این است که با کل ذخیره مواد غنی‌سازی شده سر و کار داشته باشیم.
«اگر شما یک توافق نهایی دارید که در آن ایرانیان در حال غنی‌سازی هستند، پس شما یک توافق نهایی ندارید،» مقام مذکور افزود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/122366" target="_blank">📅 18:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122365">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c95c218f7b.mp4?token=frq050Cvxr7lFWHyqNPT5DCoRfcwJtO1sidabS7Pu1PLSbA0sCUSPjZIQB1NyvuF28EhGQRU4AMSqfy8xtxfwgNaCTulBkzN5sxSMuLOfBW_BoOvm6H1lj7ZE_51m1evsXCKCbTey0PB7WHVI88gVe0f6hI36bWSjNST_FHJyFBhZ8VpVHOzCSgzioJMtdarm1WiB9z6QGocQBFI3IFwUvtAq0mDR_9cvbPl4vCnJRj5Ve9xg3FePAFx4bCz_KvhsmesI87dD0RtJt8Kk3oNqtuMi-NElZgpyvzA6qLiyX6Cw_4m3uMb54mGhIQ8F41ExzX2NDLTzn5R5gOdgmzuCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c95c218f7b.mp4?token=frq050Cvxr7lFWHyqNPT5DCoRfcwJtO1sidabS7Pu1PLSbA0sCUSPjZIQB1NyvuF28EhGQRU4AMSqfy8xtxfwgNaCTulBkzN5sxSMuLOfBW_BoOvm6H1lj7ZE_51m1evsXCKCbTey0PB7WHVI88gVe0f6hI36bWSjNST_FHJyFBhZ8VpVHOzCSgzioJMtdarm1WiB9z6QGocQBFI3IFwUvtAq0mDR_9cvbPl4vCnJRj5Ve9xg3FePAFx4bCz_KvhsmesI87dD0RtJt8Kk3oNqtuMi-NElZgpyvzA6qLiyX6Cw_4m3uMb54mGhIQ8F41ExzX2NDLTzn5R5gOdgmzuCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل داره حملات خیلی سنگین تو جنوب لبنان انجام میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/122365" target="_blank">📅 18:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122364">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
یدیعوت آحارونوت به نقل از
یک مقام امنیتی ارشد اسرائیل:
🔴
اگر توافقی که در حال حاضر به شکل فعلی خود با ایران نهایی می‌شود امضا گردد،
برای اسرائیل فاجعه خواهد بود
.
🔴
وقتی آمریکا از ادامه جنگ دست بکشد، آخرین ابزارهای فشار مهمی که در مذاکرات بعدی بر ایران دارد را از دست می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/122364" target="_blank">📅 18:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122363">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH4knzM314f4rvYNOvqAb4Kcc1bdYY6cA2OF1hV2g7wGydCOfN-36O3ewoJQu10vbLaDtVl-hsvfyWRfnJhfuh9FTSXwbbPtgcKehA7_2uya0C5f5jLxOhcyFbLKc0TCORbcL2BYlquxz7nDnEgUT8bm4bM59elReMQ2PXnyjrogfbW9bz8dqS9ypLHc8MYfy3goj2frKTQgyhwQWTL1XC8vfHQukrPZOlhZ7uVBzMOTYfKONxN2n0ft-A5mkg_T4xIhRYYtW_s2-jT5PhxJuatSvcw1Nk6rNB8SnSMs3YAzEgHMdUz1Xuy5ISd9k6w1VY1muiKpiWrtxAhyB1AWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
ترامپ در مورد ایران:
یکی از بدترین توافق‌هایی که کشور ما تاکنون انجام داده، توافق هسته‌ای ایران بود که توسط باراک حسین اوباما و تازه‌کارهای درجه یک دولت اوباما مطرح و امضا شد. این توافق مسیر مستقیمی به سوی توسعه سلاح هسته‌ای توسط ایران بود.
اما معامله‌ای که در حال حاضر توسط دولت ترامپ با ایران در حال مذاکره است، دقیقاً برعکس آن است! مذاکرات به صورت منظم و سازنده پیش می‌رود و من به نمایندگانم اطلاع داده‌ام که در این زمان عجله نکنند چون زمان به نفع ماست.
محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، به طور کامل ادامه خواهد داشت. هر دو طرف باید وقت بگذارند و کار را درست انجام دهند. هیچ اشتباهی مجاز نیست!
روابط ما با ایران در حال تبدیل شدن به رابطه‌ای بسیار حرفه‌ای‌تر و سازنده‌تر است. با این حال، آنها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای توسعه دهند یا تهیه کنند.
تا کنون از همه کشورهای خاورمیانه برای حمایت و همکاری‌شان تشکر می‌کنم، که با پیوستن آنها به کشورهای توافقات تاریخی ابراهیم، این همکاری‌ها بیشتر تقویت خواهد شد و چه بسا جمهوری اسلامی ایران نیز بخواهد به این جمع بپیوندد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122363" target="_blank">📅 18:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122362">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: توافق هسته‌ای با ایران در دوران اوباما (برجام) یکی از بدترین توافق‌ها بود و مسیر مستقیمی به تهران برای دستیابی به سلاح هسته‌ای داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/122362" target="_blank">📅 18:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122361">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgVJSBhurEksmSpTZ1ZWf8uJulRnDbMm4Ul51VVEOUhJs-orLdA7NPxALgmloVn3uU75zmHKjvM5gyDBXoFg49KA_8hCJQD5Ea1pfLAtFujGezdyVmr0rAX0nZHU3TgucHbrecF2-jre7A3Z55ioPddrR58pa0j0SWhW8mP-tK7Agevj1__87E57RBY2dm0AqbN_q10dI7TFFAjF-8sgxLyhcv5duFRu-L6jHFC75V9X5vW9g4TIMWfuU9P5kuh3RtA1v91tGNsD-NW9-CcPhjsq7u8PBjdLtG286OdrX3wjg7eNzN1nos2Sj1ZPvR2zWW26ZT0QdAHj2sgT06dqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای جروزالم‌پست به نقل از پالو آلتو نتورکز: حمله یک گروه سایبری مرتبط با ایران به آمریکا، اسرائیل و امارات
🔴
واحد ۴۲ شرکت امنیت سایبری پالو آلتو نتورکز اعلام کرد یک گروه جاسوسی سایبری مرتبط با ایران، در جریان یک کمپین چند ماهه نهادهایی را در ایالات متحده، اسرائیل و امارات متحده عربی هدف قرار داده است.
🔴
طبق این گزارش، این حملات سایبری همزمان با تشدید تنش‌های منطقه‌ای اخیر صورت گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/122361" target="_blank">📅 17:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122360">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bad4c4066.mp4?token=MYDdYaN8o0ziEE6EmBrHRjIJDCy_V6CzcK1X6OFHU71EMDtGacD4LjXw3eaQZz3no0LWWLCSQooqFCt45p8b_OjA7f14YiKVCDD3FDiX87N5Barv_228mEOOL_q41l8IFGWVLqO6k4N2C602viQ9ED_wU9lWOQd5FLMwJFQCdBubATZ3s8PwKkToqFxXl4_yYsVlUWTtI9HN2FdwBKhhaNkGjthqJGK0JLwQknN6Coor9doHM2oI389Ok-D383KlKOGoPX9fb-TMyIU7aHGNhKXRTw7AQKrYpn3wMkwpKd-1zRltisJo2abDATX_1He4oEM8KZi0EaXzM1jXrJKCEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bad4c4066.mp4?token=MYDdYaN8o0ziEE6EmBrHRjIJDCy_V6CzcK1X6OFHU71EMDtGacD4LjXw3eaQZz3no0LWWLCSQooqFCt45p8b_OjA7f14YiKVCDD3FDiX87N5Barv_228mEOOL_q41l8IFGWVLqO6k4N2C602viQ9ED_wU9lWOQd5FLMwJFQCdBubATZ3s8PwKkToqFxXl4_yYsVlUWTtI9HN2FdwBKhhaNkGjthqJGK0JLwQknN6Coor9doHM2oI389Ok-D383KlKOGoPX9fb-TMyIU7aHGNhKXRTw7AQKrYpn3wMkwpKd-1zRltisJo2abDATX_1He4oEM8KZi0EaXzM1jXrJKCEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت آخرالزمانی کیف پس از حملات سنگین موشکی روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/122360" target="_blank">📅 17:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122359">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdebcc5cf5.mp4?token=Jz4YShWZ8iqrVN8MMP4h-U3uNR4ZKZCjPVpSlI5XSZalpuRYmV3wnHAnYAGdcbz1PJ6c94sWa9uL4g3t7RXHLKhOkIWIxSyZLajnV-XVB3agXic1L6UmMysQaSsDUoRIbWeBQ2wOzEcxS52PxKoNFYyoCz1gwCbgsdrmC47vLEJt-8NKtoCTLkvJs8DAthFNVgicj4If6h3nDH1W4vxfjfKirsuAZOY7OxAD8yfe25CPeFx9Lr-vKd8_AR6zNr03NGLZrbvHJR8x4bqJ-jkusyUXTO78XNVQYPdpd3syXoH3NfXidbVEIWVySjVg9UjqZNF2vBcTVGjjtMK7tDrVng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdebcc5cf5.mp4?token=Jz4YShWZ8iqrVN8MMP4h-U3uNR4ZKZCjPVpSlI5XSZalpuRYmV3wnHAnYAGdcbz1PJ6c94sWa9uL4g3t7RXHLKhOkIWIxSyZLajnV-XVB3agXic1L6UmMysQaSsDUoRIbWeBQ2wOzEcxS52PxKoNFYyoCz1gwCbgsdrmC47vLEJt-8NKtoCTLkvJs8DAthFNVgicj4If6h3nDH1W4vxfjfKirsuAZOY7OxAD8yfe25CPeFx9Lr-vKd8_AR6zNr03NGLZrbvHJR8x4bqJ-jkusyUXTO78XNVQYPdpd3syXoH3NfXidbVEIWVySjVg9UjqZNF2vBcTVGjjtMK7tDrVng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان هوایی KC-135R و KC-46A نیروی هوایی ایالات متحده از پایگاه هوایی الظفره در امارات متحده عربی اوایل هفته گذشته پس از استقرار از اوایل آوریل تخلیه شدند
🔴
ممکن است به اسرائیل یا عربستان سعودی منتقل شده باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122359" target="_blank">📅 17:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122358">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
اتحادیه اروپا: به دلیل بسته شدن تنگه هرمز، تحریم‌های ایران را گسترش می‌دهیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122358" target="_blank">📅 17:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122357">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فاکس‌نیوز به نقل از منابع منطقه‌ای، دو بند مهم از توافق احتمالی آمریکا و ایران را منتشر کرد: نیروهای آمریکایی به مدت ۳۰ روز در مجاورت ایران خواهند ماند.
🔴
به عنوان بخشی از این توافق، ایران معافیت از تحریم‌های نفتی دریافت خواهد کرد. همچنین میلیاردها دلار از دارایی‌ها و پول‌های مسدود شده ایران آزاد خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/122357" target="_blank">📅 17:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122356">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfHcaqDyr0CDGe04Q_UnHSKSuKBhSYfmyWCM7FjvReuCZcoXrXj85EliKaJtNkdhiQpDOlC1zVI9HJocXrQ5bP1sIN8OBb5NsLRxI0INGE4vPJ3ZqF_HnPpDYz1_NGqzYO0d3jq7Jv-DsyN3cfU8IceVMyONRolH9sD3B5svslh8RV39iIbFSwetWVkdRDD2l2nDCilTJHsUD_BlpY_aJ6gkMgDbGLPIKBPz3-KvbukpdqVy79dLmSMtzUGTiaIAH6dm0AHNlX5qGGaGaRAPRrobyKrHXSJY13O7zMYoJ--Rwqf9ElP2V7lUH6a7-dFfvV8zTC4iVKBxM0PRDM4auQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
دموکرات‌ها نمی‌خواهند اجازه ماهیگیری بدهند. با ما در دادگاه می‌جنگند. برای محیط زیست بد است. شگفت‌انگیزه! پرزیدنت دونالد جی ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/122356" target="_blank">📅 17:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122355">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فیلد مارشال رضایی: اگر دشمن به تنگۀ هرمز حمله کند، ما محاصرۀ دریایی را می‌شکنیم و ممکن است از NPT خارج شویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/122355" target="_blank">📅 17:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122354">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یک تحقیق از Financial Times نشان داد که سپاه پاسداران ایران از شبکه تأمین مستقر در امارات متحده عربی برای به دست آوردن تجهیزات پیشرفته ارتباطات ماهواره‌ای چینی مرتبط با برنامه‌های پهپادی ایران استفاده کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/122354" target="_blank">📅 17:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122353">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7dU2fdQH6uXHZo0rcdBzWryD3i3p61b5_I8fmyPShFwIgN6uUD161H8JOP6J3VnrSeCK4sJ3j_2pCHNj7M8cWIAGHSVR-sTqTvnmVa0wc_QjH_fHrBSxpjAFEQ9K1zhaggt-axxbZ3IrLwTjrALINr-ak9lhDoRMs_LDsn__mxD3JRafUUjbu8X0kincknvCJpw8w0K7kQW2j8en3mrmsbQy1FGcdKug91o1DYloKwZseICDD6LRcGXPy4GPu9IOmLvSRKBHxZhyLNmvcxmEMAYtDXr09ZHwEIn_v_VI-x1XoeA2UFkNOC1qQrk62ImrByBSAtR5e9nuIg-XkSZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتحادیه اروپا: به دلیل بسته شدن تنگه هرمز، تحریم‌های ایران را گسترش می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/122353" target="_blank">📅 17:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122352">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX8N0qjV_45wuJRyCBxTvildL3Z7TWlI7WgLWUAFIdlzr3J779YYf_jcgBW2w8ViEuZefHVIUWVQXn50NaleoaZHGKqqxJ9WmKvJ2yohnTz-ZrmashLxwepJlUsJGAVXw85vYuJX902QBtoRPFSbezWYjz5jKpG-n4FJTS7akgNQTTEjN6114-lZpGLMA7QOD-HdKUYHzSqWsqBUAz6VXTm4IX8sT8o6ae0sBKAezmJrbbxiqks88PmKdCHTxqsojcJPp2kXh6VVhIVb7O2_abEx0r1dzmerIFXJHzP8Pw76GBwP5aiWHpnR4K_g6VA4CCWP5hjjt358e-Q7DYiu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید نتانیاهو با عکس ترامپ : ایران هرگز به سلاح هسته‌ای نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/122352" target="_blank">📅 17:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122351">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6hT2INphM-7xM4Wlm7vi-hiQb1A1neOuW5ksa4VC4ZAuPHigxahbvv0Gz4iP0XWkq59Hj9By3Mr6AgZxIxW-PIklfQQilZGectRcIUEblqn5kGpFicDN2jjRwNbQZoh5P1SrZga73h2iQ0udiFYY6kpKFXl6CoNIQCfp9ey2PuuHqA8WiOMWnVrjkVZqCECYpu_kzyrvWovrg_mpD7hukbakuXGtwfkMp9wvKyuD-Q2l9dehg3QfNBJGSdFouqScSzOQ2mab57qqGtcs8B1CcJq81EQV1XemY99BONv9VQNccKneHFR1jB9waUZIbnu0rpvDTvTnJEAMTH4T9Z46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک منبع نظامی اسرائیلی به نقل از یک شبکه تلویزیونی اسرائیل: اگر مجبور شویم برای مقابله با حزب‌الله از خط زرد عبور کنیم، این اتفاق خواهد افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/122351" target="_blank">📅 17:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122350">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGa7oqy_y58bEotJcnY9WZGr3jqmsykPFdMnnC--0v4G77l7EIkXPrJVoIK01qJanM5cy7nezXpewIyUD99o-JKzL7dLr6MwiCgLX-2xrhm3AaAoVAjjXBUVDaUOvbS-MivtzDrJhFx5iuZYW0YhgKBcn1X4EXg8m66tpXCKohqIIlBn_ORZnZfe-MghE0ktD04LyvsEOWMFLPET4oHjzgFdPOizIK5V0PHAFprvZ5E3VV1u2xMsCPQtQVRdg_AVqG5kWvgeh3ygjUG9ne7fKtxN8K6y2P-jdA5vzV7zxVfBFSEVApYPasN0UX1aqh3fM94_TLXFS_xBgCTo6o1kYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام اسرائیلی: ترامپ به نتانیاهو اطمینان داد که هرگونه توافقی با ایران شامل مسئله هسته ای نیز خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122350" target="_blank">📅 17:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122349">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در جاسک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/122349" target="_blank">📅 17:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122348">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ به ABC: کل توافق فقط به من بستگی داره. فقط خبرهای خوب میاد. من هیچ معامله بدی نمیبندم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/122348" target="_blank">📅 17:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122347">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BInnIzxTF9RmFrl1NuaZIekKrB_JJgI2EiiFlImaqGO1TO7lnzVi58bLag9xkrG6flrLj1R2GRuGr3vIHMMxeYYRbyQxu3aVKFDocdjEhKnZiPelFC4FF2Wwo23SbRye-s0SIBHoNB3LvnQ_QeWdJSjqcY63Xld4qo73bk3mR7X0hG5AgWfHvdGz47oyrqjGXpv2gPELPg21k2cpMszY-FnCTnG_mmccctrP1Xch5hZcJCvkySNkCPwx_cYDjVOIvUMK0nTR_bb3XcuZT9qqakiqryP2khEdd0AS4o-GgR8CkzRxcNefvgCiuh3aIdfx9Lt2vwmMgmVxPur3676tkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس دفتر المیادین در اسلام آباد: گزارش‌ها حاکی از آن است که قرار است فردا وزیر امور خارجه و فرمانده ارتش پاکستان اعلامیه‌ای صادر کنند..
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/122347" target="_blank">📅 16:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122346">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس: مقامات آمریکایی به صورت خصوصی به تهران توصیه کردند که به خشم‌های پرزیدنت ترامپ و پست‌های شبکه تروث‌سوشال توجه نکنند، زیرا این موارد عمدتاً برای مخاطب داخلی آمریکایی طراحی شده‌اند و بازتاب‌دهنده موضع واشنگتن در مذاکرات جاری نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122346" target="_blank">📅 16:53 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
