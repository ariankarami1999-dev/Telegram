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
<img src="https://cdn4.telesco.pe/file/iTlvKHoaHmCU_0YdDnUHUscsOCcq1E1HBRv7UKT9sQvuk1qwy8EkI4gp70CZgvm6q4U9wE2F57MLDYSOAQ4ewhct-C2FbFUdZeNO1l9cmZNh2rMiH83L3AiP-w3U8stC7K6rV5lgeNeLPmB5QHUS83r0ghJRN1MnnBhe-HjCJ9alMA8AsE0dC0iG-0LPVUT0rJo6qGmhx43UkQo_Y8PhdL8i7-QYYREni1esZy510zG9ppNuOZpMhHdEW4A8Jm1F2SFwOHxgUMa1hEyqr9o3OYuxRbBODJ1J-o04Ze58J7xI0XsGyd6_29W4essNzn2-8lt8njDTAYaUOWx-D6-bEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 589K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 04:01:21</div>
<hr>

<div class="tg-post" id="msg-29221">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac1rlSb2LbTgLIMwQqJFUYp1_u11puGbA285tqegTFjCNJjFDH19_TpViZd_Fu-OvjtvVOlEsJr31l_wX2RSDNmU8brVv-pqGjNaqKgvacyczDwD8wElVle0EyDme5iBbRFamNkmA-JIJ9Yq2a5XI8KpJbkQVz2uGvdZ8NZrEeoqLXNDvwoe4U3GxEPNFn3SfvQdkFjViyVqY2AjI_gsGwmNNpxjdrOIRZVof60ZDsvBTaWgM2XQUnNEVu6wxgbrLlLf9spV5b93WzcCLlE5wuiCB6tUd2NjVVLzrIqLvbZi57tPTmGk8_DCNdWftmXcSCKvGtyza8s65xPTrhR8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/29221" target="_blank">📅 00:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29220">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEbvW5Tg3RL08lI3JILcxY8fHMIlYEmGe8_WN_XG0_scekRyZiWcX2yru5r2ruuv5i2fUBzr85varHstG-pW5-qkd7ARhCWMdsm5_Ok8VM0Qwn0PvlIW74WT2uBMNFwAffs1BG7Uums21QNPYreN_Q_BVvdd0EO1ThZ63JnGwbLkR_VlsOnyyvhZs_8QSigVaeohLpZZqtlZ_RyH9Fd7B-yEXKZZNGHB3ui9_xoglxx1MZcWYE1jrZurVEGKE5l2Jn4pZhjpv5OeaFW1b4tdGH9xTBWZPDIByzYQFkivANOVhpEgZTyZBlP1XNks3HG_y7NkUIGH0wZarqtiZgieag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛مصاف‌شاگردان‌مهدی تارتار با گاندوها برای باقی‌ماندن در کورس صدرنشینی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/29220" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29219">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpIumgk_lEkRYF4n1ggV8sF_CwwXfD5F8sVBk-lHQivaUxNn0KjWFMzRlaRU68kpR-aJ_kmCQP82Qp6lSmGqakPdBUag_1aNeT9SGM6oBZRczmOs476F9wLD5LKsYCesazrYDVH8B10O1qIyuRGERCQRkRA7AeNFlFIM3o7VYbQqJTXIbfFNW8MDDYtncsHBarKFjmA9W1ayiQB10sANoh0NeJdlV3rSZA094JyqH08kIk0nKTZidZnMgGNTXZ7xel-QtYwuA0bXcORyB6sOopOGGEVhYEEzXvWdRYs-kNFDwWTK1MSMjOoDYY_mUIhu23nELnvJ99DVGQ3RIINcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
توقف‌آبی‌ها درشب درخشان خلیفه و شکست‌ناپذیری‌ادامه‌دار آرسنال دردربی‌لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/29219" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29218">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6Sc4Rij1Uqus6FFxOV9wqNdJ9MGvrxPqLrnjsLoK_xYWQyenQY-hXPbcTSvotYAli8dlyGCF6B1pr2hMG2qfid-9ZjgjeYhlAr4yGr_Bm_zDoJys51rjFrteZG0CBKLsYKSCPllW0ygnKhg5J9Y1uGWt16gU_CYNPw2rherDALdkuNCh1xVnPfZ-m-ZFRxeb8R_jnK6D1GYjZNwxyvP9yrep1dhF7p0-YKAt6mK3C8BJFi5JGKCI_AsC3twwJEvdSN8-m_WX-R6WD4wiy5PDeNum5Z82IWUZgv_tamWgwZjWKi8TD3pp6x_zoiBId0hypdwO9LCd2Oe6jNFBOonyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
بعداز نمایش نچندان دلچسب در بازی اول؛ محمد صلاح ستاره‌مصری‌ترابزون‌اسپور شب گذشته دوگل‌خوشکل‌برای‌این تیم زد و سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/29218" target="_blank">📅 00:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29217">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMsnzL6C5nTyQZECobDyQaGbVo1KgamWeu0T3DMj46DpgzHNimpXiqFpAmOtTrKU4_MW7T2ZuuhsoYU1s8SbrpivHZj6R1n5xmKru9IK1fD8-8Tep2tTi79Tx_blA-QFpr0xcE_NhXez3CHIUzf85qPskBznwWdqcob3GT8ei9YoxbcWnMvtFx7et-1mQBBi8hlfyPipEvObfMLPnwwuA-o8KJCHBldHpIIbPoJa37G5ODWXIwRdPbFbymI1DfPtHaoz1DDar0wsG5Vo1Tbd2UbuEY5TsAGlmiOuwnnNu_Qv5H4uCmMX8md8tIno9441Tec-TRzI2vO0TFUvLM33hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌‌سوم سری‌آ
؛ شاگردان آموریم در واپسین دقایق بازی گل‌مساوی رو از بیانکونری خوردند و سه امتیاز شیرین بازی رو با یک امتیاز عوض کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/29217" target="_blank">📅 00:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29216">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGlBVEpb-ll8KApmJ6B9oUqURvTXxCB60U1zDW3NouoLkW8E6rRglyUvpGX2cc9V9TI6fYuauwzXhKcDHb3a7PYWjQVz--2No2P1do0X9DIEBloCRpQKwMa7HqAKlkQ66s8dbSfDnS_UAYBGfRPk_INABoBULYcJL-ylqwZMwGV7Bcarci-nIjXOmiZqHQrUOTgpm2dxlsOKjQkHb_OFrOLpHL2DEzIcF1CLnsJ4PXfJ0cRFtcKVPzKaQjajTcIFKr6DwlLsTxg3qTL_i3_6U0kIfiXuftvkLgo2M8quUjowgyGz28Cl6JX4biXoKqOwhi81LUdAC8Po0u3TY0dhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات لالیگا برای بارسلونا به یه جلسه تمرینی شده! ۱۷ گلزده در ۴ بازی‌واقعیه پلی استیشن نیست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/29216" target="_blank">📅 23:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29215">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=jWsvmu-rxZGgsKOJ1gDxjA8OunaF04pGjuTuimM30WCDpwx5lSOp0PYOleQk2p3lFtfvMdmI7M2f4adMEhS-D3MlLRq8j6ra8SSfHCMj5CIjW5N2nZ77aO2plLKj5DjJNns8u5tXeJ_i8PujhsxkfdrGh7zHslQOda3sCw_2evRiIoQHHCOSZYxCCbofnjTUWVACcVMviRjWpQJQ4At6etmRFJeMy2pQHh9DmS_6C1PnEolf-m1e2bU6TfQoTAYuc6XIrtHjzcNn1Xjmlb6Buiwax9qsCsBHPBYFDk5reolTEG6mH3UztY7oNAsC-vkvKjaFmpDLJ4JEKIQrZQhq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=jWsvmu-rxZGgsKOJ1gDxjA8OunaF04pGjuTuimM30WCDpwx5lSOp0PYOleQk2p3lFtfvMdmI7M2f4adMEhS-D3MlLRq8j6ra8SSfHCMj5CIjW5N2nZ77aO2plLKj5DjJNns8u5tXeJ_i8PujhsxkfdrGh7zHslQOda3sCw_2evRiIoQHHCOSZYxCCbofnjTUWVACcVMviRjWpQJQ4At6etmRFJeMy2pQHh9DmS_6C1PnEolf-m1e2bU6TfQoTAYuc6XIrtHjzcNn1Xjmlb6Buiwax9qsCsBHPBYFDk5reolTEG6mH3UztY7oNAsC-vkvKjaFmpDLJ4JEKIQrZQhq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی آقا دایی هم عصبی کردین؛ واکنش اسطوره فوتبال ایران درباره درگیری خداداد و امید عالیشاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/29215" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdJHn7v0jodbQeBCSkOPCydd_zoWLVMvcjv1nehojkjATdSnrdtQgyDSDXsQZGB7D7YX-O90ZsNb3BWiN1vjkONI3GXrgVkcFlqliZVCbdEGSR3g34gd9LRs8mToJOsr22tQ6zRERZcXuGzawO5V-971s4scoqVGsKkkj8mEe34G1tGzMSQ6pP7-InrfQdCBxRO6feWAhuaVlmE2F3IZMT998uHZ9JZINkxiY8jUMSw9zsh8uD7suj0AwPHk0YXV3AIlPbiHa4tjK_Tkxy6bzZOlScWQUpp5P7_izf-PttYobCEsZHfrObnrhjmKa-vI1Cpd5NHg8-pLCfH0-A8oJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیروزقربانی‌سرمربی‌آلومینیوم: کاری به توافقات بین دو باشگاه ندارم و اجازه نمیدم خلیفه و گودرزی دوتا از بهترین‌های لیگ نیم‌فصل از تیم ما جدا بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/29214" target="_blank">📅 23:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4nZeoNcjIsnfTx3STBsD95e0FVoZSxznc9HNkTIjrCjHju0Sff2yrQ6jToHwcSvXrobxNdrcwEIRMiA0cLI_bFBj7LtaTE31YEmlfiJ6zxBypj9iRY-Z0oXQ72TEa11sWhWQrc5G3MHP8GBgpr6pEZROrRbVigGG9IbMhQmKrPX24sNroDBcNRkq1ufM8L8cMw3xpsGYl8c06-0G7G4Ec8izSMje5Xgvf7WbMKnNpS6s1y11Qq4M2Bp42B4d7mx4WLsGWRPy0cMJS8nDWQP0t5-Gb3rjmy_8LJN-7__LaqstWJU6doU34CK6YGiV9e2P-V1UgxjB4YIKo7f0UKvSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/29213" target="_blank">📅 23:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=MUq5q0XeHF-hWXm_v5RzeFpg9M9PymIa7C53f3mHQPAuKxOFlwkzvUdCQMyq39kmL5kaXhpCczm2QK1jOsuWHEGG5HqoAN9FYiUdIT1LqEicpVu8kgiG7Ci_TpweL3CbA5yC0OXZySSy74WuKW6mNMXKDmajKCaLsZuI4JpQdd3SisMWt8QJlPP76pFDWWfQgXJ58q271Fo_R_nOgbAQI-xojFAVuWMDV9VPDsc2MH43JxhEcYJ_D0pAGKBy8XSkKXj3_ScLP3H0wkIbY9TLP5t1J5J8SdNpkeOxlq2A3FAK7uDd51OdQ78eZ3GQzlh3RMoGMw7kgNRNGLwGmH3D2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=MUq5q0XeHF-hWXm_v5RzeFpg9M9PymIa7C53f3mHQPAuKxOFlwkzvUdCQMyq39kmL5kaXhpCczm2QK1jOsuWHEGG5HqoAN9FYiUdIT1LqEicpVu8kgiG7Ci_TpweL3CbA5yC0OXZySSy74WuKW6mNMXKDmajKCaLsZuI4JpQdd3SisMWt8QJlPP76pFDWWfQgXJ58q271Fo_R_nOgbAQI-xojFAVuWMDV9VPDsc2MH43JxhEcYJ_D0pAGKBy8XSkKXj3_ScLP3H0wkIbY9TLP5t1J5J8SdNpkeOxlq2A3FAK7uDd51OdQ78eZ3GQzlh3RMoGMw7kgNRNGLwGmH3D2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی‌لیگ‌برتر درپایان دیدارهای امروز؛ سپاهان با همون تک گل لیموچی سه امتیاز خانگی تقابل با آبی‌های خوزستانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/29212" target="_blank">📅 22:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6Le4QOBeAoi6qXy4ZYg30NpkoebFuJ8Lt1Ocx3olaFQjegyjY7sTF5sSa_JEEyCpvlLXISxqYHvG1wi-pCmjvCHP3GFPpby-QboT_fhweQvvEQSdaMV1mCe-1LVmE0CCyzKJr12SPy3-cfoyAT-o1f6UbW2QHD-Ew6xlKiNt8fWIoIXqTkfEY5b-Ye_Fn3pdi_yWOBZsbiPR8YvooH6Xk1ug1pM_1X3tq_--4LN4mqXL6x0KjQ4nnr-nC0BfgECsGN8i28qihZ6_jK1Mw3fW_IZZCWYRgAcKq7HjwTTM_EYZ_hPzBAl8Dp85Dyc1TM1JszrlTDmbj0wxwA2BjXOBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/29211" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29209">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uv94aotyjbQ6hsDuasZx8r4Yb2vH0kA04ioO__cjngrZ1tpTdEg4BlRC3hSGZmLLm5h0ixDvAlIlmFPEKu-ieE4AABORk-YYj30XzHtd7EzaCRd2x3LDguzTJAegwJhq2LL46DyixAZEJYYTqq-AGhE4nT2GrrCbaXY-tNz58TpfgJcqXWGvVBs7m3fyWRreWi8ih9K4Tc5bRTcqgUsPhM3RmeIZg3n7tm2xwqHH-eVpovqVBlSqtjHVOa99E9g38vcTwwrmpR3N_vIVC4bedrL9DSvjyQ0CNqcGZmeRlY9wrNdCTwUJmwhBgmY3-xn3PNgDy_qrco_oerQAgM11xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29209" target="_blank">📅 21:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29208">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=qM6frFOb-iQDEDJ8LTOgwAXHzvEQcSBGf8SD3GUy6mOAu3JwBXZp5ZAL5UHqBTu4DoLHoO6HJ4L0tlPGxNesWfALRTp5I_fsVo0IjwA7B9KqIqVda2gYPAZRDJHxa_hRtxJBZCSYodUnuWo1q1R1raEPWlRkCAaVx-7zx9cdHy7dBUO2m5IBuqmXa-NNTzN2RvhJR68A7gHXaNsH2JPfDDDNOSmXGtUbIFUaX85Ik1vOPyUXVnzgYkJ65kINz_NeBEkx0IA60hZ69nJmbsEgABkFuV0paPeRg4Te0469lpwRJkO8qH73X1qEa0tXXJD-4Wrasc4PvjvnqQjFwLM4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=qM6frFOb-iQDEDJ8LTOgwAXHzvEQcSBGf8SD3GUy6mOAu3JwBXZp5ZAL5UHqBTu4DoLHoO6HJ4L0tlPGxNesWfALRTp5I_fsVo0IjwA7B9KqIqVda2gYPAZRDJHxa_hRtxJBZCSYodUnuWo1q1R1raEPWlRkCAaVx-7zx9cdHy7dBUO2m5IBuqmXa-NNTzN2RvhJR68A7gHXaNsH2JPfDDDNOSmXGtUbIFUaX85Ik1vOPyUXVnzgYkJ65kINz_NeBEkx0IA60hZ69nJmbsEgABkFuV0paPeRg4Te0469lpwRJkO8qH73X1qEa0tXXJD-4Wrasc4PvjvnqQjFwLM4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29208" target="_blank">📅 21:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29207">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg8W9CAwiag-JY6xpaDztF8fKgXJp-i6CQkrUDL46X_EY3MR4Y28OIPhlWRr4QCFujEtuyQeb-SDYNDSU3ekdYeFNrbT77pWcWFOWr9o4-ulzaUv-Y0oslc0UX8qnXETkBYn5loQrvq5nXowWyuZvec1w4LhbtpquPePO6yRbUoC0PZlFNa6ADlzuuyG7vD9IGdiXrqTnrSGMRxrODSmM8twarDH2cN_K_bIlXz6CmmBMzR0M-5jKCYogFRQ0xjH6qRgTjry9kgrcujBgI8deyyxAaPodM1GKK7iAo8fjrbFJF1hBtzEfY11Y9kjEGSa5xBu2juh7LBwNuQshkDWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29207" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29206">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd5ZPDIL0J0LD1J1G1fCAqpCsLy2PHlWZphWn_Gb0Kj9_EQI0WzZsv6GhBvD8VvfujZNHDs-n-Q-uzkxO3VXdYY6NE6oS_sk0vqF57OVe53jolPwrhELUxp0oTgS-iQ2zAYvWEgl8jxizyQCf04wMRSbMuSmpPJyrwYqKtRjJwCCTSSMpE7WXD1FDgUS926JCRNZQgEURGSz3GJZQQmRec50-gr-J8R3uT5i3E1187I2oyNUgsHk84FZH3r83lrOh3rQPiagCG3WUnBgydK4-E1KNbl6xIWEY965Gpcluvfzex2LhY-hvQt8T-wuSLPu6RU5vr8l3XfP43xJXVLV7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید یاسر آسانی که نشون میده عزیز گانیف ستاره تیم‌ملی‌ازبکستان هم‌اکنون در تهران به سر میبره و به احتمال فراوان تا پایان این هفته تیم جدیدش رو انتخاب خواهد کرد. اگه استقلال پیش پرداختی رو بهش بده 2.5 ساله آبی‌پوش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29206" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29205">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrJlRoJ86dCP54nps2XQs2252A2UIAP6E9UEZfHN2wt6yxR5K_8OO7WvluSphqfxRkXSVlZUUv3jIYg-BCoZhmkwZXHG2n2vujLdM9o1q4RGamO9oBWs3N0P93q8i4QSnKskwQ9srcqXaYYS3Bez4HoCcURh2D_GMphYKETzomZ6m5N27p8PbO5ywspYaexvQ7u4SvjkNwHXSAfm7nSxkmuStn0Iey_yQq9SBCfdtLlWKSRzZLpXjqDx_5VfiQ8GiSOCvNxSRzP-qXhBQ9uTsgx4QnsT3P8wPKanKyWkzHahFdBCFAL1ViPW3UwSTB1DwaGBy3ZU_Tu5TA_OgmxKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ توقف شاگردان سهراب بختیاری‌زاده دراراک مقابل یاران پیروز قربانی در روز درخشان محمد خلیفه دروازه‌بان جوان ایرالکویی‌ها.
🟢
آلومینیوم اراک
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29205" target="_blank">📅 21:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29204">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEtYXs28TL8KX8XBbozD2CizNpWrRzdHU-3hzKkGgmz-of1g1Vnpxe2ytr4sE0K8LpsM0b6r5DOhMEj3ghp0NK79NgtJ3125TR_t5HD5tLqRriIAFAYJ8TfvFaS1q1SwcU5V4gJ1kBqMEe-qSNWDrDF5x5DBWaik5FFIN8z4Q9TVmBQX0GAXpZ0u8AWTf5Ly-w82mYaA4VG0zrOSU3GIGe4GQWhVzHQImWv2kIcfYbATUN9HBNbV3Ek8L0Sj-WSA36g5O04F1KDnr4v1CLmwkP-6kjHR91GzJvU4ajQ1J1NJNbQ2BbCU5YoyueSTyif16QYAXpVFfwvjRQqafLv7tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛ شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29204" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29203">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/banVahDOnWQElsi9p4pViX_nh7efNeHLtnjbUuCpmrBRu6jOtQlyECxtG7Pbo-blHn2tMaVzpzkY47d0KASF4Ki1zUYmb2EEKSyB3n01dTaUZ2C3omcufhGF4rbVf6XkwTxm4q6n6YjcdgwB7Lx98FGXkQ5agUOSs-793AdMosMBClHdh7oukx4CYATXoYNsRUTnfOJLCyzrhc5VC3zN5yX48U55hG-TwCltI2-N9bra5zb9eWweow6qJJRVHlTo6srxCpQHTE374D9cirFDDHFybkH9V9RZk18Qih4380G8Zq_JY2ppS-RVj5UgabTzCP0N0Vz-SCf8rF6IACmgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دبل‌سیودیدنی محمدخلیفه دروازه‌بان استقلال که قرضی در الومینیوم بازی میکنه مقابل حملات آبی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29203" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29202">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvhW3OmnSxWMZk-Ew6h_Lr6SYTc2gRbEYGugX_0At6UgXIF0Gt9z4eMj8EiGYKYgaCN58nl82gQXy3yUC5EoqM7xhGsPfcVna21ENoQlg1Nn5cUqyjUt9fY_UmZCnrnZxLMKm9zTcI5gaAI9RirX2xGQh048GgaZcPG9vYnPmG5TWOo_PHlq5x5SldaggFikbgBAuBQ74HVclYHJA1lMJR496J89cFXBV3m-9F0tRGQGJDAGVtJBUUV9K22TUXZAXN7SJ9HvJ4dPhjMYX13jxYksZbVPS2Nfl19hEpZHd6j2nrb0SZTRa1bKuTWxubxCxmvamUNqlIWZ9NqXAEOl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/29202" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29201">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pluBGrDzRZLrKORHFVWeuaHgzqsC9A-cOFp14Rcz_kG-qygDftuBhL5PQOcSPy0HeGrvpLTBpn79QzUFJR9gfT4t2QS2m9UUirC0_9qJeMbKBL_bLfERvhJTUg0PyHK_KlX7km5mARrwxFk6cjA7TvyntDAZuYphTUnu0Yoxc8rqG8isBC2EuJ4hNRWy2xKDvBtyZyJ8sgbFD2AbQWxOccCke5gDWlVqn0u08BKwO7qh1EBga3VQM3m9XpOBsnFqrtISJSBHGgJ-76noTcJ1pYkQP6h56QoxlHTlY7SJ-u1prkCpsI7tJfXcn-I2aZuS-Y1bqyBBKY4zgXR3SIUrWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته سوم سری آ ایتالیا
🇮🇹
یوونتوس
🆚
میلان
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/29201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29200">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=ugtJMeX94BOvZML36Qble1J0W7WL6Lz2bvPuC3_C72xL1QJydOB3ALVB24DrfiglGkUGs3lE_TGBlGJo-QEmy2obIPCT-c-kJRCjI3NNJ4MOLd_VS3eVO2MlCBsbwirCuOIyH0vI3JWoJNby-w7mrqZ_0urnoWvtgyVQfbUoxAwHVcaMZ2P4OTVY7hkOXot5rLUXscBnoGMYtzqMkLlYq97N7q5LMpxAEhJidW21SV1lo-jSt4dxFwMvaz2ix1XHaeNX3NX0EmezGPMvoU9csWpjbSdpPD5_yYcjDTixEDGraTQX2ND5xpw87rdmvBGp9i7I79TnJrFbYA_-xLMs-rg4afBL8jwGZmNBVAMOHYchyaqcHAKwUlEEFsO4_c2PK9nG8LhkwV5pawFTJikCxhLibQXsjV8MAOXda1q0ReQA3sYIDig2ehG053hLlUMEnp3isDW-7j0ZXhHu8cD4yUlHpqRUZd3wCb2kJS-7LwVHYEc2i09a7DzdTGiKyhsbCPcxCRoEEL-0ne-m3cWRXeTfLXLQNQrkv_Abdd7iStaUv3IpCVtuVZWNnB0nF3Kx0WBngXHfQnyIKh743GZzednOStJREHjA7o8K_5x-WUsevR999FqaJR5UtBLahbUmCE8W459gYXGdKm2KNwDRX6HR5JlFMhusEh_iFaQr7-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=ugtJMeX94BOvZML36Qble1J0W7WL6Lz2bvPuC3_C72xL1QJydOB3ALVB24DrfiglGkUGs3lE_TGBlGJo-QEmy2obIPCT-c-kJRCjI3NNJ4MOLd_VS3eVO2MlCBsbwirCuOIyH0vI3JWoJNby-w7mrqZ_0urnoWvtgyVQfbUoxAwHVcaMZ2P4OTVY7hkOXot5rLUXscBnoGMYtzqMkLlYq97N7q5LMpxAEhJidW21SV1lo-jSt4dxFwMvaz2ix1XHaeNX3NX0EmezGPMvoU9csWpjbSdpPD5_yYcjDTixEDGraTQX2ND5xpw87rdmvBGp9i7I79TnJrFbYA_-xLMs-rg4afBL8jwGZmNBVAMOHYchyaqcHAKwUlEEFsO4_c2PK9nG8LhkwV5pawFTJikCxhLibQXsjV8MAOXda1q0ReQA3sYIDig2ehG053hLlUMEnp3isDW-7j0ZXhHu8cD4yUlHpqRUZd3wCb2kJS-7LwVHYEc2i09a7DzdTGiKyhsbCPcxCRoEEL-0ne-m3cWRXeTfLXLQNQrkv_Abdd7iStaUv3IpCVtuVZWNnB0nF3Kx0WBngXHfQnyIKh743GZzednOStJREHjA7o8K_5x-WUsevR999FqaJR5UtBLahbUmCE8W459gYXGdKm2KNwDRX6HR5JlFMhusEh_iFaQr7-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
درهفته چهارم لالیگا؛ شاگردان هانسی فلیک در در دیداری خارج‌از خانه آتش بازی به پا کردند و با نتیجه پرگل پنج بر صفر والنسیا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29200" target="_blank">📅 20:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29199">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e23364253.mp4?token=CYFRr0VGoG27ZqcqwdyzP5jWl6Bw6MvggLWOATrqxOjDQ0VahgPcWU9IlNX2h95-fLugpDFQDt-9WMQMt11TPtCL_onTxr73awEpVif7CK3TGcsJO4q3jzSLtxYSsnTm8E1YqRqKF4VyHVwPfbRTMdDR954XnNkCDW_byQDC9nzmi7l39VntqvAtm71Qe80So4oEi50R77anSEp51QDwKNGgUiGUQeLLGGjzvORpr_V8vOifksk9S5fExyQRKsweVkF2rENGZ7rzWa9YlEmSTrgUw56-1Gb4k-FGZFfjP1m0_Vrg15pQ0rIb5A4b580hq9ejg55ShC7avOYk3wT2Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e23364253.mp4?token=CYFRr0VGoG27ZqcqwdyzP5jWl6Bw6MvggLWOATrqxOjDQ0VahgPcWU9IlNX2h95-fLugpDFQDt-9WMQMt11TPtCL_onTxr73awEpVif7CK3TGcsJO4q3jzSLtxYSsnTm8E1YqRqKF4VyHVwPfbRTMdDR954XnNkCDW_byQDC9nzmi7l39VntqvAtm71Qe80So4oEi50R77anSEp51QDwKNGgUiGUQeLLGGjzvORpr_V8vOifksk9S5fExyQRKsweVkF2rENGZ7rzWa9YlEmSTrgUw56-1Gb4k-FGZFfjP1m0_Vrg15pQ0rIb5A4b580hq9ejg55ShC7avOYk3wT2Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ کسری فیکس شد؛ ترکیب سپاهان برای دیدار مقابل استقلال خوزستان؛ ساعت 19 از شبکه استانی اصفهان پخش زنده خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29199" target="_blank">📅 20:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29198">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIgC4xoKKvWTkaKD-YLrh6H3gp1Z9nFHPTyoRXv1ZIVDBUFa_Nwm4ZB8XEdIgUdNJbFz7UWoSbE1HcNiyxkLdT7eFZLYSmXM_TiCyi9p7xuSSeW1hHnQ9Purg7IqSNUa2wgGKkb2WXZRkVpuHEWGyTTj_qj24XwimsXvadZJKNN7bUdthaVvOursWJqawJarB7gWtravEstChCsqAjb4bWviSlZpacmQVUTrQ1E4ZoG9Dh3OvRIHfXcmGvilcJ6Q08MsJiuyYB6SCpzH6wWstviFKS2YOTD3bSMC-N5lNUTwttT0IXpWiW4BPXWKtJp9RNED_iut1CxGP3pAeo0ARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی پرشیانا از سیرجان؛
مدیریت باشگاه گل‌گهر به سید مهدی رحمتی اولتیماتوم نهایی خودراداده‌اند و درصورت شکست دربازی هفته آینده با شمس‌آذر از هدایت سیرجانی‌ها برکنار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29198" target="_blank">📅 20:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29197">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKPIkCqtH_u03FdnqzqcXqZUA7EcBtc_ORZMUVzYI736r159lZlINOphbTvMYQs2DAMd-vVFYmM9_wBQ9sntqduDPB7ZCRJwTvaJhSknfhK9Jzzc861gjXIHKTvqncCW2s2xq1wgKEYpr3LkU-AZ7b4g7gASw-YZ58sPaXTROK55jbQAjm4EQom8rPQJ0lVNPw2GFN_IR4tXVyNyspUj7Nnh66nwr1odDWjqCDiVj68QL4k7QPAMMbJrAS2PLriwz123QAeRVVhTrIHe2T9qIOhPqiofbSX_IUW3rr2FwBhKNCfdyu14coxnLBsqs8LMG5I61Xrt3U_xznsEi0HFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امروزمقابل والنسیا؛ ساعت 17:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29197" target="_blank">📅 19:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29196">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=OWZNnmuRdQ_qffINMrF6ICfYI3uUjL6-HXQocc7ap7bx5uvy-Vc3MJ8t0Anr6Rrz5EiWNnTahhSRysCDlmboYSjL58zh4tMMVWlF38vAS-qcfsJTuYYF4EhylvYHY-j-mCnXHeXfbtroFIYvfFvG9SCNpCP9iHHWQTPc4XqzUNA51o9szSlY-aDwpP0bt3GaycpLbejzEVd6bp8JkOwt_UIRkSesJwhRRF4J9Bl3fqP8qW9GdtUw1lcxdajFun7sYhhLaSPUut-BlpZSxZMu9kv8-26J3oX4qKqQ3TsoltYo951_8Gx2bnda9Uqz6A3U_HS8yOi784u0_cjVeXF1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=OWZNnmuRdQ_qffINMrF6ICfYI3uUjL6-HXQocc7ap7bx5uvy-Vc3MJ8t0Anr6Rrz5EiWNnTahhSRysCDlmboYSjL58zh4tMMVWlF38vAS-qcfsJTuYYF4EhylvYHY-j-mCnXHeXfbtroFIYvfFvG9SCNpCP9iHHWQTPc4XqzUNA51o9szSlY-aDwpP0bt3GaycpLbejzEVd6bp8JkOwt_UIRkSesJwhRRF4J9Bl3fqP8qW9GdtUw1lcxdajFun7sYhhLaSPUut-BlpZSxZMu9kv8-26J3oX4qKqQ3TsoltYo951_8Gx2bnda9Uqz6A3U_HS8yOi784u0_cjVeXF1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت تیم آلومینیوم به پیروز قربانی سرمربی آلومینیوم اراک اعلام کرده دربازی فردا با استقلال از محمد خلیفه و بهرام‌گودرزی استفاده نکند که قربانی اعلام‌ کرده که محمد خلیفه و گودرزی از بهترین‌های این فصل تیمش بوده و نمیتونه اونارو کنار بزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29196" target="_blank">📅 19:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29195">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAQAawG_FO231zm8vDhsdY7ujlvPOr6s-_13roaQGWlBNXOIOXhymfMJGjoONvQlAzPffO4NHFP63iTjmR8c4Of8kS4LNJ3MTI28K4rmGlqiXlrU_cPoXRKUe9leOSYnJwRJ8bw8FtLWi0VTYw2r70HTZ9PaGdmP6bmobu5H9k_avEjSrArtjLxe4NLCyt_n0KGDrM2F23QEmlDZcxpCLIlKFD6Nk65xGKytY9r9P6qoTZN2OLDnHTdLlIzsOwIm4jvyw4p1ShHf-baI-tS-pcwVNY1RmOq6CTNkL2QF-lhAjq4RbfaE8XaQka-2DDOrsBW6EIfGVLHWJZd4JwSWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29195" target="_blank">📅 19:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29194">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKD5NVIppBIN59y8490ZD-1tug5TIeIDIaSaaDvx9ZFBo72ncVjo_aY1QYEpORI6TsbBlbtb4arjoE4ct8A1FME857TpjVzypnziR6Wd8fJAEp6e5_66A3NcQ8V0YU-bx_fBO9hfM1btd7I9Lslm46EpOt9kYq2Jhi-lhUJ-9_RO6FOpfwEzxOWM-T6t3jE-jj8Y0god61RGbqBMce40qO5LaQZ6OlqYvRE8HcAqSEKE7DvLjFjL8KzepcZMBHpdjf0oopJH1NNdIyODzjZdh4Addg2RihRZooEjOg3JRi4GjSA9miIDmeH-YikuNlUbkqa12ke2GqLM91uEl4sg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛ ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29194" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29193">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🟣
درهفته‌سوم لیگ‌جزیره؛
شیاطین سرخ در حالی تا دقیقه 96 دو بر یک از اورتون جلو بودند روی یک غفلت گل مساوی رو خوردند بازی دو بر دو به پایان رسید. گل‌های دیدنی این مسابقه جذاب رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29193" target="_blank">📅 18:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29192">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiurhtT1vU6UK0Dh7c4cmjIB1mwpBD0OzirPuJ8SnjTBkTFuzzHucAleAGdVxvzO0SJg2trh-JvwZJgXursfZEDD9QQozSLonbpqhpXc6H0mBZ5yQI9AxjSGOPl-9NZ0myJDpr6Hb9nceM27tuTYAGN6ETKGEpLh1SwGw5KXV6LSwJodGeQR2wM08WsXrq35e-qj-UQIX0bv8Rql4oTXcX1cpz4hkQXrgEzkhDP-HG5wEAvrcqA3oDRBXKUcMVQrCcebqVWkiPPKTCxpWJaA4x_73NnzHiqHtHfEa-sgmSyUTxdbSiv6b77QsUMZ96CJBNk7eocoz913doQEf538vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29192" target="_blank">📅 18:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29190">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKw5VrUF9Cpg3bN8pSMQa01KfYicE80A96LK0IxbFJizTrIU77EuWhu3fVdgeYQfWnPobsl06reezzs3r7bDr9GPokmlecOkvHAqTW62b15U2dUPMUM5jhPNIJkvOZvSjTXPAaAeqRsLLIyNmtqs8a-1Rp-5V6_5qsI4NeaZSvfcVEe81-sXaTzXngl3jIqlhm7XM6MSQ5auZD4ipvThfvbsUI7JS1rt2vpQGv6fA1MQJXE0TrCCDcszx7BaPhvcs8a4Op00QArJ4Kr4zXEHTUaIB_m4_J-Wb6YLYRJZ-skyMHUyKILmayUB8bKMmqzPYe0VG0LYsn1qv8-E6obGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9R4lXO4q1W1qqy7R85EOSflJrf8VjnC6h2EpsvaG4Cpdg4mqsKAlyD3PXAGlSL158cbGY4SB5TbYtNrjNpAER-obLhTAv8ubuaQovXjLJeCuWS3YxLLM8bGJ5d3UnACoAUkd_joPL4-mC4sdr9D6U1e7Qb0F2DJMUlQ15ZkVNfAN2uKvgoOIMSXKWdAnGsfEb2lhq1r01XP5LiukfNkhCI9wkWYt1_pBVTZKz24siWywB6tIlHMBd2GtDVvbwK6n1h1isvux9r5baHxFPRXiGRC-Zx3V_Qed0dj4U5SFkPTdlBLUu1FIEl6D4muXr2d4_RzbiSePjxzOwuJJ2prUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛
شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29190" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29189">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcClqR28BVaX6WQyU4NF1Mn34TAKGohl96wwYmEs6Hr5UkNDP01a7idTGI1Y1xgdHuGrEvkBN7Fv7G93v3EtqKAsk4UxQxiFEMZUffXeSSppeJvRLA0gm7fAnJgFoQCI31u-P53ejizwBj8N3E9Nt6qMhap6Wubx061qlOtoZMQ43XTKF5cSx09gw2POmY2r4Yt-M8TOgUsl1IunBRFsOj6IBDVXN3ulxpT-99RH4UAE9FYmBUKV0EAiAhMV4e0DTNvbegvtTyBKEapKAQbxTftruDURtnzskkh33UeUQTAnztzX9QiIhO7xv3bLPQX6DR1lA3E1-wVvEZKZ3fz0LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇦🇷
رئیس‌باشگاه‌اتحادعربستان:
سال2023 قبل از پیوستن لیونل‌مسی‌به اینترمیامی ما پیشنهادی دو ساله به‌ارزش 1.4 بیلیون دلار به‌اوپیشنهاد دادیم که اعلام‌کردبخاطر آرامش خانواده‌اش قصد داره ادامه فوتبالش رو در آمریکا پیش ببره و پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29189" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29188">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgWPE3gmQhOqvEPOS_EteFPp79Ro-LB_ongMvrxCKvsPNWvyZXOtMJTjsJpb6SbygD95EUtY9hf2Ri6LEvTcQP4_oR3AKV2ECYr_izm1Yy4s8t_J4UCGXouDV_SHZirwZLQ0Spwk4hD6ZoarQarabC9qBbzimtqZRgPc0nf7CtESxlw4yKlMnbopdOp1OCJiQ8puB528urGBRYLIoSeqxBg4Z_jHWiPVQYAWE591YeyTYizEgmz-E6PnyFtwDBo93JQO7gmzbRVadDGYTd9WHa0yX4QWLea9nXYHIHHQKkq1EUK9NurGf4X-S2VojRxb75yI3Jr1sLoBnkHdJqvXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه‌های اجتماعی هم ۴قسطه شدن!
بااسنپ‌پی می‌تونی از بین بیشتر از ۴هزار فروشگاه در شبکه‌های اجتماعی‌مثل‌اینستاگرام، بله‌وتلگرام در ۴قسط و بدون‌کارمزدخریدکنی تا دیگه با درگاه امن پرداخت اسنپ‌پی، خیالت از خریدت راحت باشه.
لیست فروشگاه‌ طرف قرارداد رو از لینک زیر ببین:
https://l.snpy.ir/gskco
https://l.snpy.ir/gskco
https://l.snpy.ir/gskco</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/29188" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29187">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6gg6avdNPmBynAEAJLSO4aNsyWBqW2dA7ZNpjVeQdiCo5hRW_P3i_aOtjwn43tIUYhBE9NEjD0XG54rnAVdnxZk-lAzbgDDZLV56-EbiVmhlJgMkkuUeuyh6POlGI-ddzcr80j0fuGmXZR7DrlaTU3gfndKxCkeZvj7g4r-OrYwc1Ipmj59lkkSx-cmjdmbPMM_f5aHJLZDM5fjZBd_Z_pnMiRSm6w9xqEPcHOio_scs4UFe9YO1UmMlvvuXhU0Jf5V8KtLwR56j-RCrwEFcLxQBUnQdKIrbL16-T_xX9lieXnK2A6SYsW5ECsszC6BiGXVNqAtNb0FvQAlRHE_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29187" target="_blank">📅 17:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29185">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/POkvJlEz-S8r8wBt8ZJ5QPXbRaFe1hc0zGOhnabUR3wbjfDJXb3aepKTR_iBdVL21Q82YXhyCaUOU6NwQ0nmq3-BdraqDSCtJro2cfxk2y9ds8hXMhAcitPeRIYByrhFfXytc7Mjd6DRPQfvDaF77MxHVWhp7oLBxmCYolJd2f193epsgSmO0Qei6zNXNGf9nqI7HccNo-g9rl1uL-qsshDxCicjm_odlV2eb5AjSgT7B6c2jGY4UEGq-6HLA6bX_6vbjPsndihYC7UrBdd1vpFaunDJFB-4WvTCL59EqPO8nRwMAO-ovbCIMDh1RvQrf_cMWE8VIEoN15DblaSdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cO4LQ4XdFrqqlmNbgKqNf_6zWCcw-Jb7sUVeQRYklCmDWzuRfVOmH7pXMGIbBUAk5ewBQQ7xDTMGESCIzGpCAaCrb7gBSwA0s_GtvhhEMhlvVltsLhqKRV21ibEe2OcycqdInC-pSrU2ERaahMVCVelnCymUSXgiOImc8KdChHP2yrd16xBCn0QyNQAQ8H9sJiBAPSOYh-WqnqMPAWWGbekhUBR7-xXd3BIxIIcGf0n3erzACg3J8KeVccVGT41jzQxhWaAnYaXWkkzFc1LrWJZqMl964Gavl-MTFjmVSHwv6csuufkqd9YXVLkadhFuiRfjbpgYHjNAQLxmL82OfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛
ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/29185" target="_blank">📅 17:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29184">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_dJ0JWEYfQd07Q_7a6VPCM0q45KcODHrbqmQ-M7bvC7y1fK6loztGeN5E1akACUPsK8YHMZuEcGy0NYUvFEuBYwpSl3LmzijzFEW3hHN_4RUOPjsQyhA4PEH6H3zj52_gmxmw5XgnhVg9CbLD9153eIkmZdM3lJbL6CMMNDGZbZMA14N41WHPI9z8h2BSZihTTjkJ4h0osYuN-V4fyEJ3BreQ1iJx89rkMTziYvFnAhIviahjk2rioPSLwEt9tnyee2JBp9vTH35y5LtunVCfh2g7Jv7BK9k-kiNZQuSDRk7Vsl9bNpgeFu8g_N_SyL09Nfoao2Ek0ooiX7h40vGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته‌ولی توسال ۲۰۰۲ تیم پیکان یه اردوی ۱۰ روزه توی انگلیس برگزار می‌کنه و اونجا یه بازی با من‌ سیتی انجام میده. بازیم یک یک مساوی می‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29184" target="_blank">📅 17:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29183">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=EoA_DXBIbMk-zekc4JtOWWl2kb6_pPogaiDsymXUJ2jfRVhEZUp97kdBh5XgklH4AiN_xsdnfCaerJIefR790oM--kisKU91G90mC-rIv0snm8QUWA3fpmRd_n0OAASn6gB6SlKfr-x8Ya1ZWjEvrJFY9Fni1S3Hl0eNufdAamynLmdQxgWMMHOWNQFvGbxgHWbieodomf9fo7qYcH05kxDLvHbXIZtonIP-SGZQp5qCajNqDh16YcgHqsNvJ11q4HYNh1r0VeLHGtZ4kb74oPI9VjFTpPuxMVkmef2kJy19_cmzbpOUM417FpW6ii1HUi6da0FZGZeCpwKf7VtSkw-nIpGVfSAIcxa7EnszIM_E2Ml-JJDTimx_l6y-fPLLcXuByyOGzCCYd7XYZXySP7xhGn9qopxTaSlzDmX0PeFuocCEtMYDxZrzMr4d0mpy9C0cCi47AcqxM2kzzP60u2BOuodcSWJZN3fE-1ZZCIfEv1wVvPHt4zooSexWtvd3CsEt9ZQQPX5ZXWzOy-RqA1-N5EA5EGmuU-lCvoj5dI0TfzjmmG2fAc6Fk0mT-MVCuXANGRDUFZKly_83eWJSS_oh4kd2JiK_J9LIBjBmaKY3vsEc4vROtAc2pPB3P-fKKuuWhrbRIxhz2SmXMTSccGgbNNS1iT34cCar00YkT2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=EoA_DXBIbMk-zekc4JtOWWl2kb6_pPogaiDsymXUJ2jfRVhEZUp97kdBh5XgklH4AiN_xsdnfCaerJIefR790oM--kisKU91G90mC-rIv0snm8QUWA3fpmRd_n0OAASn6gB6SlKfr-x8Ya1ZWjEvrJFY9Fni1S3Hl0eNufdAamynLmdQxgWMMHOWNQFvGbxgHWbieodomf9fo7qYcH05kxDLvHbXIZtonIP-SGZQp5qCajNqDh16YcgHqsNvJ11q4HYNh1r0VeLHGtZ4kb74oPI9VjFTpPuxMVkmef2kJy19_cmzbpOUM417FpW6ii1HUi6da0FZGZeCpwKf7VtSkw-nIpGVfSAIcxa7EnszIM_E2Ml-JJDTimx_l6y-fPLLcXuByyOGzCCYd7XYZXySP7xhGn9qopxTaSlzDmX0PeFuocCEtMYDxZrzMr4d0mpy9C0cCi47AcqxM2kzzP60u2BOuodcSWJZN3fE-1ZZCIfEv1wVvPHt4zooSexWtvd3CsEt9ZQQPX5ZXWzOy-RqA1-N5EA5EGmuU-lCvoj5dI0TfzjmmG2fAc6Fk0mT-MVCuXANGRDUFZKly_83eWJSS_oh4kd2JiK_J9LIBjBmaKY3vsEc4vROtAc2pPB3P-fKKuuWhrbRIxhz2SmXMTSccGgbNNS1iT34cCar00YkT2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛
به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29183" target="_blank">📅 17:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29182">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=oIDCQqEgQSg85MDGifyRgoMXlhUa0IIWu7QqIkw6sqBoJfD138Lds_zpCPHrwDP3oDSyy2_mJefJLPUO6zQ6llVXhkj28m9u6sx1qaKJsLJw_C-s4T9wjuAYQyaUTKa17YkWHtFLxFM87T6vfkGYFcsSTvpZWToaDYRx9sH6y06yv8jSgb5FWEP7pARisZ_4bOOBM2o3AqISzIxD9Z6YB-FxMBtgZbBa4qH64nfvkRCxZHXXSklJ1f-fLfjrYvllfMl93fcRc0-TUqusXlI8Bj0V8XtMLiyniwf3bOrayU5_GVaK5QEPEGpbMk-Mst96I2UJwltTkALwtVE_dNkTPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=oIDCQqEgQSg85MDGifyRgoMXlhUa0IIWu7QqIkw6sqBoJfD138Lds_zpCPHrwDP3oDSyy2_mJefJLPUO6zQ6llVXhkj28m9u6sx1qaKJsLJw_C-s4T9wjuAYQyaUTKa17YkWHtFLxFM87T6vfkGYFcsSTvpZWToaDYRx9sH6y06yv8jSgb5FWEP7pARisZ_4bOOBM2o3AqISzIxD9Z6YB-FxMBtgZbBa4qH64nfvkRCxZHXXSklJ1f-fLfjrYvllfMl93fcRc0-TUqusXlI8Bj0V8XtMLiyniwf3bOrayU5_GVaK5QEPEGpbMk-Mst96I2UJwltTkALwtVE_dNkTPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عمرمفیدقطعات‌مهم خودرو؛ این پست رو ذخیره کنید و برای دوستانتون هم بفرستید بکارشون میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29182" target="_blank">📅 16:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29181">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVzFrxqSOu3jsIUSl82rLM-YYW2vRqpQTfgrpW9vDtOMz7wFGx10VW5yLyeZ-IzZcdCOtPa7DtKAdNffcEvu0EvMAHmpiPA1H_KW-aNCvRffpH4W-p3dPX8RkxLk5_b1wfV0JB96zBayS6Vu0MX8R_XzwO83LLSl-nHlp15FS2YpvvBfnVu_9mxmM_Jt2uFIB9s0iT7ZdtQhDTQYSbYmvERgMLmugPsV_SCHRwNzKYEf6Yq0m0nGgD3X0z9BsuO_K_u4_JZrDkIBWI-WZehtoA5sA5NOL7oXE7vbwnlWn-nwE34rZWCf6jIcJkDEF1GFLEHcjb4jU4JanUw1IcxQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29181" target="_blank">📅 16:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29180">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnYw9couK6ZUmAFnvWPPXs2bXjbG0SwtxqTxjQNMeGLZl5UnGVCX6Cz4XdDY47CvYqheMS3ZdbdDZBcKJsG-MsXTekMFCRj7ndyHAj5AiQMSmKC8Iy7zQKoJpkw5Wijql04VpOsfKNW6jzGg76V2N1QqApCl0XzLrKMOl1ONDRdeqosckK2DiQ81sCb9Fy6zUIpsKuyrSdhJ18RbvCfDza5slhZN4qe9nFWQKpLBW_lwl1vsTh8VEYh9WLyNtE8SyxNYeuyS_U6wquj7HSCBnN_JQyr1bEKbtOAaAtF4uLLNPp3d41Pnu28c05So4YcJ0Ghp5pRlskJMQwYlDBKF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29180" target="_blank">📅 16:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29179">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_RkhHfjpil19cNR-SNMBKoIxVHXcTuWGI2hALDFG8mL-dAFtmLfAnyi0-CYbu3m_YvEXzCs9if7SGSKDHYSNHhOAQSpmBLJL78Dq_vgsdQVhI7wzm5u6uFBmCmIyBthD9VSWcLXvsXFFMssgU2K2zAZ9cFs24ko5SxsIQKOYCkZW5QmYlXhrkg_uunnkUcY9GL2W5bdy06jyJ40vIT8Ej2d05ff3FdNyK0omZf9rGgZmk9pjw0pWmLcnKFByLoPzjSM4q-M3Gdh2Z2B-d6tRB_LxQ8wylymEAvh4-nYJIY7iUtEZnVg3mb9NtMiF0UPhc3zaOVRRB6nPMqi5IV4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29179" target="_blank">📅 16:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29178">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=i4nmhwN1QxSGK5O7DYyrXKMOda2__mVU_4ctFvr9BR2Xk5uX1qrpgrwaIxypXXHfYCOzOjuGRagsjb2iXQhlvEHWBgyhJO31VwrgwjjzSC5ROrt9iPSBiFEzcQ7z9pNYkQQp_vNWDmrMU4FZXIVhGcJH-K4Wx67jVgaC__kOB-tTnMEbpaizYpO36aOF5ft9--nN0ekjJn_8ETqOnWCP5ikpqVPhPDk48E63kJASjIjfWTn9ue15xPLJWEt63uC9I7gu-Frup-ffjuBycHRz5qDQDSdNqO4RdyRBeM0h3YmmvmsmpE5KXpk_EqDrJGAzNIZcwreLf-oWgKgCwo_aeTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=i4nmhwN1QxSGK5O7DYyrXKMOda2__mVU_4ctFvr9BR2Xk5uX1qrpgrwaIxypXXHfYCOzOjuGRagsjb2iXQhlvEHWBgyhJO31VwrgwjjzSC5ROrt9iPSBiFEzcQ7z9pNYkQQp_vNWDmrMU4FZXIVhGcJH-K4Wx67jVgaC__kOB-tTnMEbpaizYpO36aOF5ft9--nN0ekjJn_8ETqOnWCP5ikpqVPhPDk48E63kJASjIjfWTn9ue15xPLJWEt63uC9I7gu-Frup-ffjuBycHRz5qDQDSdNqO4RdyRBeM0h3YmmvmsmpE5KXpk_EqDrJGAzNIZcwreLf-oWgKgCwo_aeTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29178" target="_blank">📅 15:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29177">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=e3WikVR7shfxKYSX3uJcFRC-lEV2KFl9RUyMFkaRxsU5A9p9wmupxmp0phWkC2qxH9zQghCkwdxdt5VQ2T0b7AXIjZkdkvViW2GBApOgp8YJ-ExdDQHM8Q1ajUoTY1aWmVX-5Ia9w1x7U0v_Z6IML3kYUI8wm5ghY8Ho6dyeGU17LJukjdcYgBcXtl_PfUi6yOYTRjK5TZ9hRJPx28ZtS_CTUCZeqi2w55b3iHh3jRUF-rP2NTWBJW163LQNuI8DYoXAU2QTIlkLD_qCJ7JYDdih4C_c9ttdVUOk2PscmlAKFbUUsj00j4lqt3jSVwQer-tQoart435eHh6m4Kxy_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=e3WikVR7shfxKYSX3uJcFRC-lEV2KFl9RUyMFkaRxsU5A9p9wmupxmp0phWkC2qxH9zQghCkwdxdt5VQ2T0b7AXIjZkdkvViW2GBApOgp8YJ-ExdDQHM8Q1ajUoTY1aWmVX-5Ia9w1x7U0v_Z6IML3kYUI8wm5ghY8Ho6dyeGU17LJukjdcYgBcXtl_PfUi6yOYTRjK5TZ9hRJPx28ZtS_CTUCZeqi2w55b3iHh3jRUF-rP2NTWBJW163LQNuI8DYoXAU2QTIlkLD_qCJ7JYDdih4C_c9ttdVUOk2PscmlAKFbUUsj00j4lqt3jSVwQer-tQoart435eHh6m4Kxy_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزی‌روزگاری‌ادن‌هازارد فوق‌ستاره‌تیم‌ملی بلژیک و باشگاه چلسی درمستطیل‌سبز؛ کاش هیچوقت اون انتقال انجام نمیشد. هم رئالی‌ها پولشون رو به چوخ دادند هم ادن هازارد اون بازیکن سابق دیگه نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29177" target="_blank">📅 15:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29176">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfWhakMKuCqDtwecvfm3CgVyBdxP61pRLui4ZohQv3IBD7OJflzutil8_HycSGQiG8Ia3YCbMnKVyoJlijx2cRdBpB7L2basIGek_uZVtivZne_6FwZp0iBal9K54OqeAWCa7XhCjcaCwsw4xL-FiJd8CYFKE9KPOiMeUsBx1-OXVA5txvb-PKGK8Ul4MTjoSKf0fxiKbiIxRuAtitJaa4lxF5OCb1hq5_mKWvKmOcsJhTfvBLr8XZyHU955o5CHKj2qaH35GFlElnl_IhBPufX3LJ81OtqVUuatoxD5-Rzjjz-sIHqXYJ1LDOhsutPEMMQ1hb-RGw9OID9ly3Rw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛
ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29176" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29175">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=CVvCUikEIxHl_YE6SVPy91z1qr7zPfqcGA5pDcpDx3VK-_ovKZ2ZJd_25-OKWVTKaTDdNetT-LrdeQRIuhyQui8nbpB1CoKqim7OzaiCubtoj4A0bVqCTY2hAe9f-lFpCb47pS9Pf4Smpy1v1y_zKgNSSAU0GjQa4lArsxHYq3C9sbBBmBe6-sKu9HEhtdqWi581apQXT8ZVaB4i72RFbRncljgrEYDp7b_Q2DDc2t_hTS19jiD32fqb6IZPJc28BD2Chf31a2yLYu7wkdEzkiQY37dIVWZSLiVfvg4gX7aJKKbZCqi_NLE4GKDIYsp0Tpl-3YAz2QSiBvYm0WNMZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=CVvCUikEIxHl_YE6SVPy91z1qr7zPfqcGA5pDcpDx3VK-_ovKZ2ZJd_25-OKWVTKaTDdNetT-LrdeQRIuhyQui8nbpB1CoKqim7OzaiCubtoj4A0bVqCTY2hAe9f-lFpCb47pS9Pf4Smpy1v1y_zKgNSSAU0GjQa4lArsxHYq3C9sbBBmBe6-sKu9HEhtdqWi581apQXT8ZVaB4i72RFbRncljgrEYDp7b_Q2DDc2t_hTS19jiD32fqb6IZPJc28BD2Chf31a2yLYu7wkdEzkiQY37dIVWZSLiVfvg4gX7aJKKbZCqi_NLE4GKDIYsp0Tpl-3YAz2QSiBvYm0WNMZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇳🇴
صحبت‌های‌جالب ارلینگ هالند درپایان دیدار روزگذشته‌مقابل‌کاونتری درباره کوتاه کردن موهاش‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29175" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29174">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDsphwxQgjIyrVnvS_r77PjBmZfRZxKcg3BRwEc9jQL6b0qz6d0yfgpFwN6hUr5cjs6haP6NZVqwm6G30idWAIM2-QF7Loj1Q5qxlX1zSxP_jAPNUwZlLaVCDMC2IZtBY03d13htuUCC5Q83nJV0wh8bHelUwvRLC1KcrEmZO79WyO_jhGDhFCqnXWxaB9uYAJT5qSVDrJ5Ue83PZAAWGta-PLJIafjq9SRr3Tpnc9cdZgmnduqWc0JIN4Bc1vdp1XRJQLzXkbuSLOZ4ujhyFazNOmwl4_PEd-PuNQio2vRLPr_FP2P_vLQrscv6fP38Q449cwMKRq0Kw5E8yXaUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🟢
آلومینیوم
🆚
استقلال
🔵
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/29174" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29172">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=hIekGYOWzBtMTUy1lq0EJNEHAyx1gcYTQ37kUj1iiyXceLtOHGu_kYwjzBgXXYnOa2O_eeTgzduCG8KYH7RSbbu2q1wWxYWMH8iQYyHeiVgmQcA8vLjpneTwSomAlbLPFRpR_c0ZbyHzyxLFhn5gzTnfwbkow9_GF2znCzJ-jr7P38KLurmsLrSqeKWH8DgJ2AHkt8JYw5Hy93KIO6hnrqTERuZm4NyqeYIqf2NZTMMgWWf1NolldL8ja-uIqhYzMRYgpOPux6e22xLu7oqZUZIG_1pZAEZ5HugMpectC5nzR4ptqtJQoVpjD-3yo8z7QzfHnQQolkCUIyiRy_Z8mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=hIekGYOWzBtMTUy1lq0EJNEHAyx1gcYTQ37kUj1iiyXceLtOHGu_kYwjzBgXXYnOa2O_eeTgzduCG8KYH7RSbbu2q1wWxYWMH8iQYyHeiVgmQcA8vLjpneTwSomAlbLPFRpR_c0ZbyHzyxLFhn5gzTnfwbkow9_GF2znCzJ-jr7P38KLurmsLrSqeKWH8DgJ2AHkt8JYw5Hy93KIO6hnrqTERuZm4NyqeYIqf2NZTMMgWWf1NolldL8ja-uIqhYzMRYgpOPux6e22xLu7oqZUZIG_1pZAEZ5HugMpectC5nzR4ptqtJQoVpjD-3yo8z7QzfHnQQolkCUIyiRy_Z8mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
گل‌های‌دیدار جذاب و دیدنی امشب دو تیم اینتر میلان
🆚
ناپولی درهفته‌سوم سری‌آ؛ برد جنون آمیز افعی‌ها در جوزپه‌مه آتزا در دقیقه نود مسابقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29172" target="_blank">📅 14:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29171">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpLOoUmW4qzeMEm37E5RH_unTzqT_sUY1Fb0bCEDhaU776U0QXa2L_NyoSf9Jnhyjk5L129rzo1ojtJ4b2K1EcieMPOr5zp0KpZdJ-Ap9TyhRHcCuNwjBidAh67gKetoWk6FpQin1-5Wzx1TnaHgbGmEEAQpgW7nVsiglOFg1XZ8Wp9hmi9_M0VW5PEU2893LCsULWJ1I6wMyuvCDygdJj1iCEuVw-BVFhGVxlgkMlEg_Ju7wz8KhPyP17qcwbsJ1p76BeBXkRJAXwsOo34hS2uA-FDTHFiuQG_t6IWXao-uJzekVZ_eNoxlF5tgN3EiAXBs4IwcSuJKPMFD938E9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29171" target="_blank">📅 14:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29170">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvfZ-IFQLOsmCm6kyikzga0_SpnnYru8uk4yPi8YNlsLLWyCOXkKnf-qKVmnU-elxtbWJs7WYUBrr0QBYWhlN6PyDsVXfFnz8qRcGOA25fTOaFjUgbAGJmgDNgl7qVszuCfPgdGqzz1JghDWZES2wOQDYAYRLHRLYlJ2CfIIvbO-fLhJgBP5DNrUCdQ-sTzEnfU3-Wq5Pt0W5lI7u_HB-7hOZKS55eSz6Ly3lYKIQ3BbeCVzFY1JQRs6jDf1tjl9th1avn5lvjXIstlgOhVSwcEEhEnKLOVZ2olr-zEJ6QBvcZtSZ3bvgGp08T-kVKHVP_MXNISc6GCtsAPa9eIXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29170" target="_blank">📅 13:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29169">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8b-TVaZAPA30rvFi1VYWTfpBSs3lPWiwZSQtDeUlqNgPe0GmfhEstjpQ3XW2KAcqiv7F0tcZcfH_s4v0Hey0aAcmwt5wl8NdvwpeIG-Vv4XQC5gLAP80z-CQ5CzswZO9M7tQ3KVjKgj0C_2WwxeFv_B_BbeCwxjGAzsVpL5Xdrs1ksItnCUXX6YEzpk-r_bhF4llsx7D2KOW_Dv0tK3t0dxrU5ZGID-OogTmg4SzAesykESTVvGyEhR1whLvd0BtGKUqlb8KR-jlqhL3BLMyE6OzSxo8AebEGn9jESvjokchTXUk9F3SnYGfzfbEPFAJ07rjhh49KkkW9OjT19GDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29169" target="_blank">📅 13:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29168">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtybPRFd_R_HXHTlLWquIKUwrl2Q5qKziZmuaN1ifkDNVzXsjv12yJ2jLm2h0k65icMWvMlLgF9cyMM_GuzzZJxXqfzxap56aggK6reQX5IhQMWITAL_yC-N1NgB-EGaoFCKpU9OXDfSipy6w1SloOtylGvvnMI85rP6Ap0hbl_huRmAvh5ryMLbOqk1kF3ScHmsB4uNBxtwQp-RYYlAml3d1XAGbgyai_Ptw0HjVQRnOa37hQzyp8D-R-ad7IAucXNwRnD4DtxwN9dghEd15HWcUI34IcdvZyyYYS4VvCRLx7Bj84qmV9HVHf7jfJZyvOCWxvVG154_a3fXVcXW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29168" target="_blank">📅 13:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29166">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIraeS5opqMj4AiOoDQ_Nnit9vkGghQ6vkSMA5NNGbDR86YNludJSM5fdUEbBV_zWg_f1sKLBD8jcp6q3iyzUARDt8E9hEC7AZAH4zJ17rPRgCayda36ZbHj0Ld2pQwEA8j9zMCvxEUqk9wUvTj3jp0XcD7aU94fK5u1nJmfOxrHGWcSMDo0GD5M9lQY-4eaXgknbMDi0IvO2v4mndCF_c3lsTg5oXwXt0j04MG7dDwtMzDSfykKc1C9cfc2INXt_0LAnFUUIusaaB-Jcj2gOFM8ziCQ-h303Equ1LaAnKqfVymQoyVUc3TTnYoAvh5uExqIcVIwBuprLfdL8NOqKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29166" target="_blank">📅 12:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29165">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQGSh6JyEpXqnB05IDpW6jaIAkg-19IvHwMJ51XUNgqxcnpWKRX3Y4G2yqSDBaHSC7ce9NpAK3Y01s76hqwQQBBXP35UQG1Uy84fftZ6SNLz_NrLokDOGyC06ctSVMyxRpzuMJKdBazTDUPEfqER6VFvEsMp6--UIiTLVHbDv8tFobofAG_kLaoVDtJFdPevwMVNFvz18S0XYfIdaj9hUMhiLOVSVdJ_Rjwlxy1FpGfP--yAqQ7X6a5J9uOvAXbr7A4xIXQbVYon69R9lv-QWyNfggRPvIA5B2sf4P5I7zvAQqRPhACBOJYkEZhbnANNKHq0JKQ6lYkNKvWJ1jCNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29165" target="_blank">📅 12:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29163">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYTS-trzNgmpJGZduooqZI0l0JNZa0_Q3MkYdqZRUZBi9cflu7RfCguzwF6B4a4b8U4DB3fKfcpfheb-Jk5TC_3GweVMsTwrEe6CSdoXtu6pbMaDiYi5VPbI-8kjGTLJbVEFhVSWxx2x8R2bs_nLsTfJSy8aquxoii8fcVJZBq4ivSaaoqtFUboJHzxB0WPh6YX2JuLpKAhLmlfEDBc_G3Z2PgKHb87OgkKdY8gxfWnnpdvTBLxBvBN4Ae4XDZcIl4D05AFshqfTvYw2fA2fKIccPf7wQE493fDpvKGSquyUcRzGqUO2DRxh7IhRjRVc_ZwDu_Y6TkjHgijcqZ5Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CunfDdBpkpHZJukrLs9gHfk1F504GrzYoMEKXfiqCrm2Awf8uGy9dNRPHsAYy0ROGbOxfdYg2BNhKKG8IGSW9ZQvVqSPyayOSveGXD1B5LB0bArDRRRbKJH6n62LMFN3cNKQgxW9Z_94irrlR-7GVNoymGFONYuOki0IIl5RMkjDIHU5wNjHbRgUvtHYydleA7lf0yInMza2o-9AOXyP9rs8iFd_LRQ32ymo77yl0ePNqSCEr-salIsx7ZfjDc9z0R1_Lau7uSFFLLexbq28ghtyorf0KcgHhG9v7AuyidwsDLz4cOWox4S_z0seQGKs4rNmvgS7w1Nk7gE9glNkfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
همسرگابریل‌مارتینلی‌سوژه‌عکاسای عربستانی در جریان بازی این هفته الهلال در لیگ برتر که از گابریل مارتینلی ستاره جدید خود رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29163" target="_blank">📅 11:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29162">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chBLtNctKhUyaE-NiIfNq0pkCc_Xo5YUHzzQ3h9lUhQ-2Y0VvR9XhGWMGaLHh1orBhSKYLZmFexFeUPRjgG1Dh93oHpwQLt3JCau-WBndi3oqxndl_GMG_CnzlrrG_xdf2xLxLCM2bUrwPx4kOvlTSlwo__cDYPEDmcOr67aG5KWdbsPYbNJL2cOPel2_VKqDkSk1b-o4HnfcdDfOMVoabmsOoSAkPbLZAY3A8GMsIQfUtQFwyMtlTbpz0S68grzkvdnilIFdimvQyT6ek277IhJxxARxT-JFxiS95Ccv_IeRZk5-CRE2D3aez3d0fOB6anNYNmHZHcG7-RB7RkYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت‌دردناک و تلخ ایوب الکعبی مهاجم 33 ساله المپیاکوس پس‌از برخورد با دروازه‌بان حریف در بازی شب گذشته تیمش در سوپرلیگ یونان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29162" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29161">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇪🇬
10 گل‌تماشایی و فوق‌العاده محمد صلاح ستاره مصری سابق لیورپول در دوران حضور در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29161" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29159">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29159" target="_blank">📅 10:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29158">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=REW8z8KJXO18H-eB9jRfyQ9jrPMj0IFCVQZjxMApK0R0YJ6GdKC3TT_75dl4-jojiA8K6Vizqge1GtDs2N8IjJ-lfujBtYrvBzwf1Ox0l6d48OOUdWZZiVvYRvmMrKAPXIsVhTHgyvPoXsp0QhJoDP_uFd6j9g07EVmL5w-XWpL5LtoM7mrJ5_CjX27KLsVo10usw4f3Uu246SMute0U2sRaKWR4lwdHsqADPAG9FfH9CZP_ELgGjni3am5Bavy3c3yDy0sp0Kgc8YY9ec2go-7I24vdwUjnLGYYAeTheRtQHsjDiMcA-umfWpKjSHi_HStDulWf1tU4zniAhv86bZqeuqGLC7bTiOJcr8lUVc64bm5eIh0qnMXd9GQNKoC0njbDOiRUUVCj1o3dEFrg9PaYfba_bffkDIDgJNIp2BWgFPtbD142AbkzOKgmjAiYjfJReOtQ9_fI1Kf5AfSWMJKNQF7hi5x5oyOx7_SZ4Z5XazG0pJUE1qVyKSuHxxf-MmOlmxUFP3GxMeIGD2pp4eq_A9J0MhO7zlBhYDr63157ppka6zRDHJR81MfMs63ekArjMzmO5Jhjjv881BoUJl4IqkoAVC8Qdw0v_00BcaXnISUJG7x5L1umuQ1iduYmQh6RD4-SGRlssPs6Ej3GfmE9tefPFQu0RCJkVXW3gwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=REW8z8KJXO18H-eB9jRfyQ9jrPMj0IFCVQZjxMApK0R0YJ6GdKC3TT_75dl4-jojiA8K6Vizqge1GtDs2N8IjJ-lfujBtYrvBzwf1Ox0l6d48OOUdWZZiVvYRvmMrKAPXIsVhTHgyvPoXsp0QhJoDP_uFd6j9g07EVmL5w-XWpL5LtoM7mrJ5_CjX27KLsVo10usw4f3Uu246SMute0U2sRaKWR4lwdHsqADPAG9FfH9CZP_ELgGjni3am5Bavy3c3yDy0sp0Kgc8YY9ec2go-7I24vdwUjnLGYYAeTheRtQHsjDiMcA-umfWpKjSHi_HStDulWf1tU4zniAhv86bZqeuqGLC7bTiOJcr8lUVc64bm5eIh0qnMXd9GQNKoC0njbDOiRUUVCj1o3dEFrg9PaYfba_bffkDIDgJNIp2BWgFPtbD142AbkzOKgmjAiYjfJReOtQ9_fI1Kf5AfSWMJKNQF7hi5x5oyOx7_SZ4Z5XazG0pJUE1qVyKSuHxxf-MmOlmxUFP3GxMeIGD2pp4eq_A9J0MhO7zlBhYDr63157ppka6zRDHJR81MfMs63ekArjMzmO5Jhjjv881BoUJl4IqkoAVC8Qdw0v_00BcaXnISUJG7x5L1umuQ1iduYmQh6RD4-SGRlssPs6Ej3GfmE9tefPFQu0RCJkVXW3gwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29158" target="_blank">📅 10:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29157">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT9EtBBpwhO4O02nxCAl1Z5Vjj3aOBhNwJRjbFO_FVJa3AVTzvuxUpMkdglaGNFeCQ18_-WqI83KUJb9C0bMsdagG-LTi4dHl_123mMG9qxnMpAi-XRG9Xobd9JAchhdoMgrWfv4lD_gAMzrmVfEO6t5e7DQr0CcN_DcdN01avGoCIs5ZmPRVF8LJ2_0DCP-WXj9g6U8Ugvpn3nfv6y0wy84foEYS3moWvQBJee3vfHBu33aFqwSUfZYRf1lbnHOF5-EskZXuffh0ttDi-CXWgTm963DOl6PzsIbg_5WOgsSudFCe0_D3bF7V3m7rwX3QBrWHGnxBNZYM_4vSHzCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29157" target="_blank">📅 10:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29156">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CklOXVd7Shh2jLNFk0chQ_q2ZdwigNjQb3E-DizUrgJ4KWIqvqs7FLOFJ-WscAtOmAV-QsUcacdy2XRxoHkjUCxt_YzUkm6c1jAgXqyLjyH56nyFptQ94fqR5dl1hjs60_BGT9IoNQlAdceEKVgRrCN2_7U3-3l7N0ajaAj62CMYfCxixx7Qd_rZF6OO1H2WzDoxbukOEhxki022Cd7TQprmHpPcJCKzibc--w4A54cnjumtVYDJXM-hHLjsv7ID7Ge76-IDF8I1smtZZZapVzXWV6MPkfv3_TPrWTjlL5FMhOMcomNvYt6FDHHJNYs-izzmHOdAK8i1e3K83EdbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29156" target="_blank">📅 10:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29155">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29155" target="_blank">📅 09:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29154">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY-XX7815RNGJ_mB4kGLM1sF5jVaQ3Q-mSIMoH_fz6kHRaQaIAYjlEj3Gqj3gH-JlLjgOeVhkw9HmWCnIBx8OlW46UHzq6MjY8gLF85kt0zIAJjb7i-v2XyPPt--We5K9jqfCBMv29QMzckB8qs8qidmJMrnwu-NYPPv-gHbdadhM9lkgEN0hYV1AWVpbqkY9BAyL5db2WRIxAj2ymoIHYm3pKv4zjDGI-IOQtxIWtMjJyI89U0bdASm4fC6xyrWJdc36YkfjhqawXVHRljGg6Bn06XaletGEQ6cS-0PJIERC0cpRFLbu2SIRZpl_p1nBGgnAQ7pQ9QYJu5tmSyHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29154" target="_blank">📅 09:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29153">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/29153" target="_blank">📅 02:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29152">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=jPFaiBYrhe_5lvSQ2ATGDbPDXOD-6m6oEJODNbPbiOz_4Em6V5Fv7QsGhB1yeJyVtsE3cFkqLO6PR-oClGAvtn1-jhcv1nQ2kHLmWbf8Ss-3vlwgoxwTlMGuBvxSJD8HGSUINunenpb-0Wm8fmP9u9UDwZNMrFWn55iuTHt34RE0M0CuZ58wNj21fY22P659g_s-TIiD6VjjV3HsPimKI-ggOEaEzkZn864Ugbam5T6FUkBAqj5Ys8J32EErZzCAZ76dQmZZxpLWXvB5NSKlXEwuRpHq8uRY2-N8W88Gt6KLYIPPCXORZlg6JCtXc5Rk1mAcGZfUbcG6QPUjfiPwFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=jPFaiBYrhe_5lvSQ2ATGDbPDXOD-6m6oEJODNbPbiOz_4Em6V5Fv7QsGhB1yeJyVtsE3cFkqLO6PR-oClGAvtn1-jhcv1nQ2kHLmWbf8Ss-3vlwgoxwTlMGuBvxSJD8HGSUINunenpb-0Wm8fmP9u9UDwZNMrFWn55iuTHt34RE0M0CuZ58wNj21fY22P659g_s-TIiD6VjjV3HsPimKI-ggOEaEzkZn864Ugbam5T6FUkBAqj5Ys8J32EErZzCAZ76dQmZZxpLWXvB5NSKlXEwuRpHq8uRY2-N8W88Gt6KLYIPPCXORZlg6JCtXc5Rk1mAcGZfUbcG6QPUjfiPwFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
رونالدو دربازی‌امشب تو اینصحنه داره تلاش میکنه ببینه رو برگه دست بازیکن الاتحاد چی نوشته شده اونم بالا میاره برگه رو میگه هیچی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29152" target="_blank">📅 01:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29151">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuH4ZC5XoRH7FPLhP7ufZ3--rteiXmo5V4q7Eu6tySmmRDeZj3ps-9XzQSp3HAlUwWfLYL-9ZMTO4XRKlXDOTGJeB8j8Pwh6ADpAvwouyWY1Jq23OMdzAeGJ-naGJVD9_CLRsgCYQLR_X7txBsGdZ_UDpnULXtVefS_H4vM5r4Bo9q7DFuei985pcFbk25Y2seIPzd5LBhDr4zzezlp8dLg28K-eFeOziMTsbLq9XA9bf9jAbHkEyJ47KQSZfBzUeO7poRI1Fj7kDNvu0oc9eOP1WGocfMsdxs39OAwvjTLtIAL0HCBGINe4mm8rUp_y9j3eOd8muOXyolRawGL9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29151" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29149">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApqE0xPHR0mXf-HCo-AMuD1B337w2Bu_AN8RmZX5HeHnnsZpxQ8W-myhNnwoE7qopnuxYr4r0opOzB8V6nfVd5Lp6K4YmeDssN8rwjwmbGBCdypMZDfMuWeMDSo9Sjg_GuokyaqXurQddrqdBxkaohonReiPJt-NRnWLl2Y-B3Ory2rn9lk_FcquensmYfODxBsj044lV_dPbU60jaT5bCU2NH1tMHdraU513U1ZQrsMGXGff7B0MucpIgaZ-bgMya5fXH1e3Vf__CGNBlZF-X8_GJq0308W6ioIhz65H8Vc_MRiKpXzulXIdlPrMBVNHo3qtgHCRU1ytpmggBwOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از جدال استقلال با ایرالکو تا دوئل شاگردان آرتتا و آلونسو در استادیوم امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29149" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29148">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWaafTdYR8OnhM8YUJnWCZBS-614L_bo4mwV2f5XqwSypuLawXzXcP4E-XUttVfvlGYUU8KIdZ1rIOsFgxR4j4Ad5d6CGOD9IjjzawkHmx68IomWFsSieD4if4REdHm0oVVpEy-UGrulAhCxglft1E_j_ma8v-NkJHe4-HCyAkUEPtfU59G4Lu5c_Ft9DVrBdyoQGuF3dmy57VIsYJL9CHV3wAnNKrNXLVXS_9ZwFr81aJVFslT8e0ul5MBcs3yKEd0y_pGuWmrz08Hamk4edj1Ysw932APVtdeD1ntzoOySjHs99pgzjAxm2zqKaDkee_DyB8wvGtheqPL56n97ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از شکست یاران ال‌چولو تا کامبک‌های تماشایی دورتموند و آ.اس. رم مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29148" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pB4irU_jGL0rLUYvx-L9psF2U-3cRYrSCj-Bgssc7SH2_olPQnefy9A_R7by9FtS7SQVffS8iWWzaxiOMvHsr_OO5d1PqFmvHj_FBi-k4uG_61KUd9q05WaN3zRa0fdMGr6FXHFOrbryD7Lo_W2D8Z92XaZSGu8JfyWwQaTJXHqP8d99eGBQxz3o6DFNvWaYgpN-AH0LIUQBZFDlpL7JZ2SFv1MF597H5unNDBn7cSMBTt-8WE42JDIoFWxCspeFYK5iiN_6XgdPATW3LxuTj5k45jf2DzVl0c9F5s0i-D8umopVeH9q6-mDdXQXoT4ddnePTXRWfejYlbJPFRcAyr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pB4irU_jGL0rLUYvx-L9psF2U-3cRYrSCj-Bgssc7SH2_olPQnefy9A_R7by9FtS7SQVffS8iWWzaxiOMvHsr_OO5d1PqFmvHj_FBi-k4uG_61KUd9q05WaN3zRa0fdMGr6FXHFOrbryD7Lo_W2D8Z92XaZSGu8JfyWwQaTJXHqP8d99eGBQxz3o6DFNvWaYgpN-AH0LIUQBZFDlpL7JZ2SFv1MF597H5unNDBn7cSMBTt-8WE42JDIoFWxCspeFYK5iiN_6XgdPATW3LxuTj5k45jf2DzVl0c9F5s0i-D8umopVeH9q6-mDdXQXoT4ddnePTXRWfejYlbJPFRcAyr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29146" target="_blank">📅 01:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29145">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/persiana_Soccer/29145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‼️
باشگاه گل‌گهر: خداداد عزیزی امروز الفاظ رکیکی رو برای امید عالیشاه بکاربرده و صداشم هست که او به این بازیکن ما فحش خار مادر و مثبت 18 داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/29145" target="_blank">📅 00:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29144">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsKfE9Cm9G_mCYAL0W8rVAY8ZFGzM0F1lgMP7vEq1tfJ2oZcbEx_2eGD0u4GOzEuVHIF10GI1vt8_FXnFfL4D687VVJsZMDRI3QCX9g8tT4RxqgkEHxqujr2Auf6FTd-yCLH4f4Z7XvMZUjGpp1hJduJ088XMI9QPGvKXvp0_rq5X8xz5whbiMPK9h5hcAXysnPfzSonZnoA1yx2gG0cqvCt680WZr51pYuAilJqa-JbP_vXSbk77vLAckfAUeFGGqfwNlTpnkJqamvlgEMjA_7-VqdfaBlPHre9RTF_gd7-m-sdFlERbC4GXnR2Tbrh2Hw6fwQS-9SwjhhzqUohFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیای‌عجیبی‌ شده؛
یه مرد تایلندی که از فن‌های باشگاه بوریرام نیزبوده دراقدامی عجیب بیضه‌‌هاش رو به 2.7 میلیون دلار فروخته تاماشینش ارتقا بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/29144" target="_blank">📅 00:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29143">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtsLbJtJUs_4M5KBy2rkSk35zP4_rFvk__C0Fll8UbetoYNP28tSY4Uxjskzw5J8DSoJquPJ-5PngADYUlwENbGcjc43Wn0kPijed8o68yOHq4X-b_IywKXickgMi_53y1Ttwrp_LFDhFZp5fINS-3M6gOwyhCSBh1GuJ6QiVo_hu9pLZGMDywp1ACYyFbTO2vudhGDmw3HAVXWcDgTl6Sjizp9iwOCye_Hs_-Mgl_UeT2_He0V548fhsOJiwp6ppMspBssOYZZw1YH4ADY63OLTNgpIwXS3kszm1Tyy7wBUZNp2HMTsvuGH3QYjL_qO-YHAhQZ8OhK2j8syeW4bew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29143" target="_blank">📅 00:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=KK-n0M0LdD6YaZRwBoBUNwh8jLzLegFWAe0r4R2oKzx-MxXfheqMUbcfWaFi4hAxNWSgOHgIeDv192XU6lTEe9aBA1VgW-e3hY33QC9RNmh2DJ0l68uYah_rPH4RsQmfWTf1PUmYetEDQsa-tn5LkvmHSV8c3_NqYdCn3ZZwYukCGr_y5tDJBq6eV0JVYaB5IO-GK1PE9_12rnOOb84LH4yVTIudzWnzZa3miadHAi3TQrTjB27FCsBHo-_NSwST9YpJTrkFOprMr4NTCejOStIepqMdRtDgJiral6j-rcvy5eYNiA6JvKw6LaiOOfciqv9PYPoFRBcnjsjx208E4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=KK-n0M0LdD6YaZRwBoBUNwh8jLzLegFWAe0r4R2oKzx-MxXfheqMUbcfWaFi4hAxNWSgOHgIeDv192XU6lTEe9aBA1VgW-e3hY33QC9RNmh2DJ0l68uYah_rPH4RsQmfWTf1PUmYetEDQsa-tn5LkvmHSV8c3_NqYdCn3ZZwYukCGr_y5tDJBq6eV0JVYaB5IO-GK1PE9_12rnOOb84LH4yVTIudzWnzZa3miadHAi3TQrTjB27FCsBHo-_NSwST9YpJTrkFOprMr4NTCejOStIepqMdRtDgJiral6j-rcvy5eYNiA6JvKw6LaiOOfciqv9PYPoFRBcnjsjx208E4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29142" target="_blank">📅 00:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29141">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwDXwjs5Hyoj0BoEHj6SbaQ4MLqmQovaOKvXC0r_rlESaQplpfp5nTJXC_5SLl9lXh5ETOJuIy0p7hg25JcxCfe5MIU6aA7o659sLuTKZ6NoMHcnXn0YekGJKawS6tIP_n4aOxfzYsHXRgSGzEPBMOVMHF5MsFumGzF2dN7PAux2J7xzwtPIEfwYR4nZTv1hv1bkAaAb9lnujWvjKLOZRVMph-5j2NWOko010WXZnonnuw5Q4kgoqbH2y0jDxn-s-6QeYfmMqoM1uSuRMFPM0BxiRTs2XT2YIbHIf0SlYAENSzpzNrK2wOcKpC1vNuaofQLfItm0WYxmTcs5XvG9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امیدعالیشاه درجواب‌صحبت‌های خداداد عزیزی: اگر سابقه‌ملی این‌گونه است خدا را شکر که من بازی ملی ندارم؛ نان بازوی‌خودم را میخورم نه چیز دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29141" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lipg3q7wz3S-X1AX6zJYJ_eSPBW16E87iUPo-UW8mA0MzM2lnYElJW_lSPSD4G-7mF-aO7-qEYrRa66RTC0xl3dQtIuaYNZEkH3zpNgWozdnJbolDfCR6BmTbm3eKnE7D3j3AsyjaTzIg2dBuEYMUmzrva1Gzzxc-3pDIBSQNHyVUYPX4N4itAELDribnqKAZ2Smr5si-mELvx5D7s-kAMDs1lICqVOzUfFomLTbJTzWU2BW3rSm7dAfNiNLWPTLjEYbMK9FMrYhFcvbKQlrOMV5ByyYWbmszAp3goGvePiTzypaGfLw8-jZDmvJcYJvH2EGzfpoq4hmutlexu0d-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29140" target="_blank">📅 23:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29139">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMjZb-ziaT_s0nvBqKAmR-9_TANAqvhX4V1KWk9Fo-riGj4poXWM6Nc0ug89thz_YVSt1pWV2CTCDceU5sOf1UjgLFoQbcNdPd0v_FP5lmUX_xUASw2DgQ_6ZFY1lrh0cT3LT9zoOi_iweEeRAUWF4gT_mRVzofxDVm7zVIqPVG6BbimPwY1xQlce6VQMsVC_4936TYOhhC5HkQLrgQhBZimsgBIg6CSIdtrOn8Z0Wr7fanCl5CY1oKbgbHIgDDlts4cboSaOracDEcDvXBZtx-BwuMk075vhoXBIvzozRGHLPRjWXetJSleQ9MTQlwB6MLxGnE8bxhG3bCgdADKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29139" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtqueINA2OZg0so3zmY1bcURykChiGaaR7PvarSPvhvMZafAaMT30H7Ivmi8zPIOoqZyYwksdzQlAgbnIbZxhF_nLyxEWiuRXZQMCzHK0qJpuBa9N382OSIlfsnkhJvyVNi-Ii-iYbo9OjxgdKAJc9yA8ze5nKMqmseDz_Vb8Vhd5w0YMhiJy2TEjcNRzwnLizE1HIoRdmZyGqGzyZJqSjlUmroEwoDzICJY4uEXlavabnEAF9KOHFaYTWGN9vXM_lhV-JSZpimt0EJObrlLvTJft-n3iP6GTVDq4OnS9BWwUhERbXCbLOGs4_iXXwU0fZBXyOxhnb2omSFmGQh12GZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtqueINA2OZg0so3zmY1bcURykChiGaaR7PvarSPvhvMZafAaMT30H7Ivmi8zPIOoqZyYwksdzQlAgbnIbZxhF_nLyxEWiuRXZQMCzHK0qJpuBa9N382OSIlfsnkhJvyVNi-Ii-iYbo9OjxgdKAJc9yA8ze5nKMqmseDz_Vb8Vhd5w0YMhiJy2TEjcNRzwnLizE1HIoRdmZyGqGzyZJqSjlUmroEwoDzICJY4uEXlavabnEAF9KOHFaYTWGN9vXM_lhV-JSZpimt0EJObrlLvTJft-n3iP6GTVDq4OnS9BWwUhERbXCbLOGs4_iXXwU0fZBXyOxhnb2omSFmGQh12GZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29138" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkpF6f19EjyUU2_AkzOhcTXCqRBJTgeHGfGa2srXyqmKwDRvXiNWxVEE-7bkCFuJ2QN946IucXWmxyuWiWhV5z-Zmd5xTNIbn58BY4lYk0UiMgzzpTNPmfcR1P_UE9UfCVUK7nLmtk2WX-pE64ix854en9qDckAKUro2bnkqYQ96rKaS_7NbHVNvsNKVratgl1JV7RsQl48TMpJuPJoegDug_ATgO1rrgH3Dm1JkSa920svRXQ_Db83hwUGMLKzczyGqbfsDHrd291AS_NXnaZH-3HHgVo7tK91RK2vEuErcWEbGdW0mcOn0bq7rMgz3YR5MPORC-Q7mH0jta3GnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی تیم آلومینیوم اراک: آلومینیوم تا حالا استقلال روشکست نداده؟ خب نده، اگه‌ اینجوری‌بخوایم نگاه‌ کنیم باشگاه ما تا حالا بایرن مونیخ و پاری سن ژرمن رو هم شکست نداده‌ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29137" target="_blank">📅 23:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29135">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFg7vcYkIGGL12r6-nrCNzNBG_N4BTkQ2CIlCcecnCX6hugvI9c5GZhDMwzo8fy69jQD_EL4qqR1EMjFLWF9iRAio5NNA-blQODSIVXHHIZIRVT1Z0anYUkj85W2Ui-acNNdkwJhHXhMOZ7GtnidV5Phkrq8fvC5n1NbsJE0S_WVZGpXDJPdF6CEl747o7m5Kdoh95EHx8moqJqqvwePr1FpGxfatT7vvxREmHajq-w-hmKGqlfesWQgakQ_wFrNA5VYkQa2ENNm55i8FLn_buJxpKEYfGPwalxzjIXKs7Y76sNoMZvIGV-8Z60vLr9SvGfmi6ZHxTdF5K7ykgxrIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7T4l4vVXhKHtM76guNl5uR1wiayvUZLUsPlmxMNEoep1Z5EksMT3HHCm6L0f2CQUl3wEyimBVYnV_gRp0oRt7aLL7F6osgo4pijjAcMwaiABdbrQHuGw3_m70sK7tekGAQY0T6Mv8rQq-vh_h1XPS5oM_JqBxr5PoDvr7nAlDmdM6Gk8ocOJzDE8kqE33R1ujzY_Cwis_AHcDPaPGJPnCQoKequJ1-nGK1Z1ZSno8-DW2m1HlyE0if5zr_VQ6-tyb2oWUtCddd9UCGpOoLKJaUOozn4g8nvRjSe8qgvVmMC-20y6UZVmB747lMj2uvHgakYi423hkqXwJwuUdgMEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در لیگ نخبگان آسیا دیروز عین آب خوردن دو هیچ کلبا رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29135" target="_blank">📅 22:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29133">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mQJaXsu52Eui0rWdkpLIlVbQp6WdC20w_JvttS6BGQwfIB5ae_255G_Qu7mmd0yrbLT4SZeQ7S6NskaPiSdlCTFCtsCGB3sqH0YpmWMp3zVUZc2cGk0-QS9_Jrl1l_gA3_dOieEjKt8cmmMAT05wKosWMfU7ZjfN7pzh74bspNwtbiP0p9pemF6vA9chN_ma6X27R12ZNbFUCH_rodL2fXPWyulZY8sFNkWzjEq_JC91cC83ziru1TymqPfuBxieVgw0f7Qfnnn9wbpRph8Ryn06Wr06JzuyG3zuE9TO5bL_NPZjBWRotsTZm0axHXe2tqTPyKY3C8XnK2A-2OWg9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaCfVgOfGvJMlwPhyxUfgIp2sdq0w-gpTlhzDoPvXKrn_uemmbJqSgQOjCydA7f-z87chASTuBCV82il8-91zWbwQlNV0ZN0ceJI0HJt7igUWLtIOrUXsV0Szu1hj-lTFLyvu-6xLNrTCWjtCSnmR7XY0cxGDkpzAD_Qe0_C6tyq8QKB5WVYJHi81D5VEevrVwxmahcFPtNXGEU9JaGZuK5GYLthRpyQb9bcGtCpq4Cv4zqMYntPCdXhlA02YbyDH_t77YzytV8LiEWLZCVc750enBQx9AQNYgJ8s8_uuWTZ_NxOwHl3DQDZwphrF02K9CiGOg5kyoW-PwLUarcsmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29133" target="_blank">📅 22:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29132">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29132" target="_blank">📅 22:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29131">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=LHVLHozXdoMr_uoUxgSqtujp1GPNb_3LKmvdEM83RG7x_XPEhclPh71HE35lEGuK5MiVPrd0HUaVUq01BE0bQhh3HsK0rSpMGq1KhpnDGI2D14T8Jnz12ekT3YHo8AMTHgfEXsNHjh-7pE3NZSWvt-x2x3YjhxkpmTNaxJrQH2EFU1_ScA86qXQ9ySQOECv40ka8tKeLvn-zzhb655-_QCtZq_Nihbv-7gznrBUVhX_XwiBj_AHl7PwrcLVX0MF8ZgqttgfxdYTkcSGj-leCMODT1PeZ7ioA3uQY7uwCHWuRat4TcT98xQ_aVYh5hMmueL6jqo06Xu1OObkb4KRiCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=LHVLHozXdoMr_uoUxgSqtujp1GPNb_3LKmvdEM83RG7x_XPEhclPh71HE35lEGuK5MiVPrd0HUaVUq01BE0bQhh3HsK0rSpMGq1KhpnDGI2D14T8Jnz12ekT3YHo8AMTHgfEXsNHjh-7pE3NZSWvt-x2x3YjhxkpmTNaxJrQH2EFU1_ScA86qXQ9ySQOECv40ka8tKeLvn-zzhb655-_QCtZq_Nihbv-7gznrBUVhX_XwiBj_AHl7PwrcLVX0MF8ZgqttgfxdYTkcSGj-leCMODT1PeZ7ioA3uQY7uwCHWuRat4TcT98xQ_aVYh5hMmueL6jqo06Xu1OObkb4KRiCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سهراب بختیاری زاده سرمربی استقلال: صالح حردانی بارها ازش بی انضباطی سر زد و بهش تذکر میدادم اما توجهی نمیکرد. برخورد من فقط بخاطر رفتار حردانی در مسابقه دربی نبود. تا زمانیکه من دراستقلالم او دیگر در این تیم جایگاهی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29131" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29130">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCVUwMH1kKbTdqKJhpIjkmxTfLnX470iMWPNKdzPxNoJLvQ5jrnWAoI7N55_1Wf0r5Wpt9EMbIbYhJPF9MXGdBoxi8OqgUICtSF99BEHQt7TMaKk-VTBAf8vCChQi3rRKcOcj3m0uDoyiCLUXpbd4cOK9OT77x1GUYQK1gBnkncj-wVyMG9h7DVLtC8DW1RxNz0lRrRJwLmPyJOBj01-8Dk40sOvVIn1u4IPOMwzKPshxVUzxdljIYrqFVgXLXBANaO9PFZoYIXzCHKdUzXArgGrUQDvQpPqc1O6aTkwcsVA5GFz03SWkvktG-8K0q6o0XPbl0PNT-Q8P7j20vLwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29130" target="_blank">📅 21:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29129">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIgMivq2ygMA7BlGaS6pG9L5Q3A-_vOtmBNmwuAu4NOXCQEnlQP3voJbS7kSHr3h-yqDJIQ-5jzXRXU7k4PfhFNmVM59HFpGHV6ll0jKgYszgfYd-S_HeO4kD4MqiU7g86tinPgTiQHmepQf6djNnl1KXmWa7LhrFWDxgGK2LrYwlDAMR93Hbi4BjAjUy6V2NIiulttgI23dQh1sE1QGlyLvu-hVpkVQbD2VfMA73TqkPQAVsL1GNtXr6AKg6rBNYkTYzCUYSFEWCUXbTjCsBhKYrH6HVcCaRqOR19TjeZcBqFR1gXLWJD-yxcOhEOo-qKg-Ut7wpYkbrRaITa6bwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛
اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29129" target="_blank">📅 21:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29128">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29128" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29127">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=vMbDkUB7CI3EviBX5_lHW9h4HCn_dd2-Xm-eVCxeeYEwP-xjbDVVgXR4KewvaWwDGZn2-cuE33h3-A9X7_sq4b-ngvYvJDIRhUjz3_R0ykkY1iQsKYBLbQAglKrfbmaXvjBWIx3--z4qe6krOmN3OPaspVpyWwyiVmmHlcO07k8PbP37KbLoV70Ur0pOlLylfBU_a93XxVAjg2hZigoQo3NsEkaORUNKMwMX3CHaAFR3GYXE6rRcW5UGOrKmILj2d0FgMCmPbPsk_Fg0ucRIk3rd6Wp01T-YXOmBTZqedMWY3z7umNfZHBNBvYAQFfx-saLe4IRUfXkUPIGnEn6Okg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=vMbDkUB7CI3EviBX5_lHW9h4HCn_dd2-Xm-eVCxeeYEwP-xjbDVVgXR4KewvaWwDGZn2-cuE33h3-A9X7_sq4b-ngvYvJDIRhUjz3_R0ykkY1iQsKYBLbQAglKrfbmaXvjBWIx3--z4qe6krOmN3OPaspVpyWwyiVmmHlcO07k8PbP37KbLoV70Ur0pOlLylfBU_a93XxVAjg2hZigoQo3NsEkaORUNKMwMX3CHaAFR3GYXE6rRcW5UGOrKmILj2d0FgMCmPbPsk_Fg0ucRIk3rd6Wp01T-YXOmBTZqedMWY3z7umNfZHBNBvYAQFfx-saLe4IRUfXkUPIGnEn6Okg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29127" target="_blank">📅 21:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29126">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkIfdT4EepeSXR-kT8dwxgSfpjxl8TuKm4kxWAvCALEp45v7InE4iAl1xW1Pb01EMTxyiPbyisC7yDHAZDERRZtFcQ4yVnryeb3h7QVQUzW32li0VLjC7AX_KHijPNrERdeDp0VqTOQmGPxsIId26vo4UX4ktsGPwb8EQaM837epvnj_4T4CdEIZZi55cP_OalMGkx8fWJ54-aVe_qKYEWoJ5YmHe3oq7gCmUDkS6vE1wUX86vLPCRvPqSttfZuCz3kjFu-uhxRyOEkfjjdmnWIHOz6N61BwBFfp_zyWJ_AgKox9uCTXiyqB38TRVsWVNeeDJbBix1zwiqq7Sz6KKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29126" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29125">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEQik0bqj7eGPHkxpqwtrJrE1iwMjc2egcK7ikCgo8p1VDZYErtbvk45uTZ8L7H-LUh9nRBd4gkdhxYNk4xXtgytVuaqIouIFhzkDC7AvDuWIKHJyUyJqNJ1HNgmT58Dl4wZLTA78tW4igiQYgKXMYghflFDRzLuoJGDXOb9IcMzjxAa3dR2mzeWa9OS8aY1oetPrUAHmKmsQeeY5x3DPJnFf04oJ5_vTYFkzI0gUeBmJR9tHW091kWfdx2DMhWJWnZgBY4fPLkZmbIErGuA5jzBBC8KGQN8m0w6DTpXqtqAQ5UjE86JI8h8znM7_vz0nC7f6Q25U7ksErnowYqqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیغام‌سهراب‌بختیاری‌زاده به بازیکنان استقلال با خط‌زدن صالح حردانی در بازی با آلومینیوم: کاپیتان تیم هم باشید اما نظم و انضباط تیمی نداشته باشید جایی در تیم استقلال نخواهید داشت. از هیچ نامی نمیترسم و به راحتی کنارتون خواهم گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29125" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29124">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_D7Ky8ng9WGOct0-R0c6JOMfR1TFGGFgvscDM7sYiRki2-mOkaLa6eprggt11tyzxcanPdQaN_j4b1smQczdsk-P6CYRk-Qc1xDbGjiy3ZiP6p4vGGYNoFl_jMqB-ZFPrtOvMw8caTMLfFyoxroV26biXAMMUiZVcKZIGU_iTKDuJlDtbeYoT4PpNVwreURbp09t9049Z_PAANNWyvWtrsvpD_Fn4BzILp2RHPAmEed43wbl8lIfNnI6fVoTZHWnHr3Y0xWZh5wRQJBDALihXGDacXiKyc6TI6usY8eQSFxD0TR-croMgxqfO3sIJJSfs2mF6mlg-5-d-ysALookg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ اعتراض شدید بازیکنان گل گهر به تصمیم جنجالی داوربازی‌امروز با تراکتور؛ در حالیکه بازیکنان گل‌ گهر برای ضربه کرنر در محوطه جریمه تیم‌تراکتور بودند داورکرنر را به ضربه دروازه تغییر داد و بیرانوند سریعا حسین‌زاده را تک به تک کرد. بیرانوند در حالی مسابقه…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29124" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29123">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=gTyn2312H5lwjNV2Nouh5xh4Dc6I4xdW9-kAeAM16zWRfvc7kioKZnewX6Ttx5TEdp-I81v51J5-3Hpb0hjV8FvUlNrf09SCeywFal-1sUfVs5dfF4fjEKSFgUwO9yxO2FxAKQBhWhq1uCV0YbM9UamyST6niBwdTSgTRJRaam5Ipf0x3k_YXDCcC4tTAjVkL_rMZIZYQZItSCBT34scmoCGjgXiCHdeFh26Wsh07y0Vl5ynyM32Gao8O8F76EM5to1WEduK1kCf90vhW9NjB2DTF6_kFoHZcZQUFsGPfokR2aH4roYyhshY0RTnLkSPFkTmkgHE16melID7665NQ2umxJeXUztafPltPopTnLCZmHTrJQs5cElpeSZDRZIQK9XtJTK1C-3ErK_A2nEnDZ8Ct7mBKUm0_Ksm3Idu0LGiD-aNMYf9eIWagt3rx4my2V6owA882wfWbDrjGosFmDZuJYuoNZvoDpzXvaMAcD2xjsgXbsAW5eIT1fWcEt89YlAjBi7XgR1YCl9oC3BsOu3XVHPblWXGPCLEkBARcwKnem8MYZrnswd1K7hRI5D4AEWHYmTaHrjlj5dCnunmuFcsIKNRuDnfrVSNHjt2x00COHmhNLqXGH6Un_9LVpM_MvcXWrNVcs7jEVzg0HDIdiA_-F3xjTfPHYt2Ypk2XEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=gTyn2312H5lwjNV2Nouh5xh4Dc6I4xdW9-kAeAM16zWRfvc7kioKZnewX6Ttx5TEdp-I81v51J5-3Hpb0hjV8FvUlNrf09SCeywFal-1sUfVs5dfF4fjEKSFgUwO9yxO2FxAKQBhWhq1uCV0YbM9UamyST6niBwdTSgTRJRaam5Ipf0x3k_YXDCcC4tTAjVkL_rMZIZYQZItSCBT34scmoCGjgXiCHdeFh26Wsh07y0Vl5ynyM32Gao8O8F76EM5to1WEduK1kCf90vhW9NjB2DTF6_kFoHZcZQUFsGPfokR2aH4roYyhshY0RTnLkSPFkTmkgHE16melID7665NQ2umxJeXUztafPltPopTnLCZmHTrJQs5cElpeSZDRZIQK9XtJTK1C-3ErK_A2nEnDZ8Ct7mBKUm0_Ksm3Idu0LGiD-aNMYf9eIWagt3rx4my2V6owA882wfWbDrjGosFmDZuJYuoNZvoDpzXvaMAcD2xjsgXbsAW5eIT1fWcEt89YlAjBi7XgR1YCl9oC3BsOu3XVHPblWXGPCLEkBARcwKnem8MYZrnswd1K7hRI5D4AEWHYmTaHrjlj5dCnunmuFcsIKNRuDnfrVSNHjt2x00COHmhNLqXGH6Un_9LVpM_MvcXWrNVcs7jEVzg0HDIdiA_-F3xjTfPHYt2Ypk2XEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
چهارمین گل حسین‌زاده؛ گل اول تراکتور به گل‌گهر توسط امیرحسین حسین زاده در دقیقه 43
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29123" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29122">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfTcN6QclG7Muk634cNOjnyLzM0gzK2HetGEhuMXHJs4ihnUykv8BAq644FH31SrqrOh-zsLztzD3uNp9Ze8Mywx8CSW-YPrGjYplmYJyytSktPqL7ZHbGIx6B2_DAITc1ii1dYPvmskh_Oqaodi4LLCP__0kfinB1nFrdR9_s0hCQ-gLEDx1yDbYd_yYu7JG9iFowbWyZQX79xpAqpHUN6hbZn_mYT_5rolrum1bZfBcgbmRzQuRrWM4yRyejf5sZ0QVKiawSwY22xAF2thhtgz8Sp9i9l7u48r7AVDH5Se2XC6MMwKrlYEDM6lf--bzI-RAhyYMc3eGoViQ-IgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29122" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29121">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ezs7kEb0mdlT2ibmYX05ZAMyEDAWquumboS0qp4NkePVjqHHIF2SBYvzQZAraVkiSB0ZlSpZVh3FqCacS8Aa7HrqL90w3hRlc5njWbM6gKW4KU5P51pjx8YP7_1IYUqZKYMLqNFzChD__SfivnLaqt0-SACHpyqkzz1u5QXpbpa0FMhWQC-HsRA3cBEolbeAwbbtJWXRmUVE_6nvW3WhWypkNf19KUL4GARd0IEC6UWx2xaggD12-9qqaYLIFrdNNMbtjrUctQdKCA-_UYZASgND0T4SykED7x9p5vW6ajAp8A4ox8GqEGFvSPWeir3RVWcG53hkWuwNitLjhUGlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
هفته پنجم لیگ عربستان
🇸🇦
الاتحاد
🆚
النصر
🇸🇦
⏰
ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29121" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29119">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxauxw94KqI8A7wovfkPPFqsW1xivIN8RWBaxmyOT-SrDCP8UxJjxVK4Y2_zIvmwFBpohU9ynm18n9Xuhs_7iCcz896VnHehJDX9apOLK43ZI2V3g-HnV0ADCCm3O6s7dUizNwR5QhYzNJuSZopQ6DNWRDhj9IeWSK6XXK3IkVXfiyfE17gcjsSvHBNUdfFpoUZ5v064ZEdk_RnQkXcK1TZemZho0y78U5kPb9G8doh12XDQkbuXK_9dfz-Qtt1p1WvSNmwiBe2-hXWMhkcaGSbJRE3C3XJyKAI2vcnjkuVqY3YkGhRZ7Z0kk0aVsw75HrM20nl5waloAKZJpPmJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXsNfImd4SzYTswU8GRiraTiVvgzvRHUHFk807wrWiymWmvviDIZwISVDCR4Glsa8Bpbk_4mOe_tn1Uddjyl6nqHoFTrP3cWm9b5k1a_KjFjyBcEYGKfRfxydClBni5t3JEJg4sCK8xg6tghIXKDR2aHOZCbWhch11HMmZfn7CcRiGwK8gX0xSNjksoDaGEFqYhjeYQtmiZQii57xVq86tCBN2Lfb4WNYEk51BArkXxPZCRjUgckKDkl96ApAbIgC4tTrF59kQSKfS4ZBqyySpCFXf0aU3vxXB3Junzl2Vsf2BJCDgmOou7eCPp3sB4aGI1jJQxK6eOUSbMkpYxDUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
خبرنگار باشگاه گالاتاسرای ترکیه هستن که میگن امسال گالا قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29119" target="_blank">📅 19:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29118">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf_h7nH6oUpgo6p-Sl-ZWI10xBPBa0wsfK2TaSR31PIIOX0KLkhsRIJVDVG0Qlauuuu7K2_dLGReGLrbtG5zoNf7ZQigJGKlkLU00FFw-BSzb8YASzv2FUcPF4nOQZAe8l0xwcGVyvM16GpKBYLYqZcMnDbTQ76is2NZiHwarveq-mpdARJ6ClAbd_jPsyaFIoGaAGR3FgoGazl20NWHCaUvSF6KVdrLh2xs7Y_8WwqQzCV5recYDVNnxasfqI1Bhf-ut9CmhdPJpH-MvCZIZC6U_gzMITQC3tdpUnRMp76QAySxEvmzdK8SY-UaG3HYY5VYLp0g0wbz60MH6m6g9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب کهکشانی و پرستاره بورسیا دورتموند اگه در سال های اخیر‌ ستاره هاش رو نمیفروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29118" target="_blank">📅 19:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29117">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=TbVAfko0hGqa5mwvG2Fa1jpBO_dwPkqBTWWWkIeI-uLUBGB1MZ44UWF1nwHxTICFXobRkoXfUNd5duH9GmYcgmpbnmZG-WaPgdx09V4ZB5kGN3GufZNkvjAusP3grXy5o2mCDGPjePbKom4oczVWnfhqW2tqHIIDXcp-QMQ9a7VQzceQksK4vNLzbuFIVXEp0606eoRXTMAci4tIwJILgtsKRqIxrIEN_p9z6dMP-ckUgUJewjC1EjbwHrepOIzj9ej9VZ8mYQNNykjM7Xr6ptOdZizEQQoQ51DS9WrpDI-qGU-MHpQHGwDfoxKJJAVjzlMCpfrV8Wug2oeEe1LU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=TbVAfko0hGqa5mwvG2Fa1jpBO_dwPkqBTWWWkIeI-uLUBGB1MZ44UWF1nwHxTICFXobRkoXfUNd5duH9GmYcgmpbnmZG-WaPgdx09V4ZB5kGN3GufZNkvjAusP3grXy5o2mCDGPjePbKom4oczVWnfhqW2tqHIIDXcp-QMQ9a7VQzceQksK4vNLzbuFIVXEp0606eoRXTMAci4tIwJILgtsKRqIxrIEN_p9z6dMP-ckUgUJewjC1EjbwHrepOIzj9ej9VZ8mYQNNykjM7Xr6ptOdZizEQQoQ51DS9WrpDI-qGU-MHpQHGwDfoxKJJAVjzlMCpfrV8Wug2oeEe1LU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
برترین‌های لیگ برتر پیش از شروع هفته ششم رقابت های لیگ برتر؛ حسین زاده، بابایی و بیرانوند بهترین گلزن پاسور و گلر در این فصل لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29117" target="_blank">📅 19:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29116">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eojDYSayh1WsvWWEtLjmkPnX27gQFQiipVxY6pr9t-wdyBttbe-PThcQiKQoALU6KQZ4g5t8z34jRghu8z00g3n__oPyJksJDvK66K2OjlpuVXR8UHrREDuWDANtlNp2TQMwn95fq_Q5O3GvFYIw4EvzUiWXVCM-vLpt60JpuYa9pc4IM7olZ2FOCljORk5mBv1q0s36HQflnpfDfsw87UgHV9AOVYgVgZFBMxt1i32EP6qaZLVshuAhZptgNOcB385EPOxNvK7vwktWHm07mZAzoA-1deCpqDzQJYDx5LG1PnWSi7_pI8UWeQ2KNcDn9GDD0NF60dR5Xpq1faDCEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29116" target="_blank">📅 18:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29115">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCRr5sq0c-yyU_yy9H9dVST2fO_MHHdj7nRfPajogkK47wJdyDeGIAYoT9VcxcoPOV1YvVcFOb43QVlpPTfVmRXkcpLpStESwWb0lDvJ17U_tdG-QmV3gkhW-lXJxgraF_TQhErFlUM5A-e92w7V-Jl-JfmKRGE8ZwbjXdsomdgWHFx2e3Lhj8-PG4FnRXvTQB9WY3jSipArTCysd-CcVK2zHbgs8MWQH6O-gkkMonpI0WB-ERv2NqtYvvEJUl7w0Uj4qXoMp9YCDlFjl21Yc4RyvrbTuHqPSL5TwDu26y8GVjFcFJhJpEjxJHo714TO_EbiOLDSTrQFlv4EdYzwEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا: هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29115" target="_blank">📅 18:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29114">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=NWIVadQFjmFFI6EZLy2kWdSsVCINGYB8XSHf2Lxln-P1h62DbQyh2aTTnZWJK277K7GpI9vYsXZ737JliRlO2Ch5butzPir0mbvnWeov5i1ZGLHL-uVFVhGDEhzSj3diPpm9gFlJwSog2eO_fj5v4K3gWCIW0vU3emlcmhwUVMy25UDIgDP5e2XUpNaloEXOOZjVr0bCNQudFSKMRBW2SoKun8OkvDWfmCHpK1qG5btXPpmKBUgd4ZhXmqCobcquZEPRKIE8E0yiUGlinqchzlDAM-0Bmw4qNpOmXzHJjb3zUMnk8LL0O35GyL2gVxNdzcNmMSVTM998gh3R4W8HWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=NWIVadQFjmFFI6EZLy2kWdSsVCINGYB8XSHf2Lxln-P1h62DbQyh2aTTnZWJK277K7GpI9vYsXZ737JliRlO2Ch5butzPir0mbvnWeov5i1ZGLHL-uVFVhGDEhzSj3diPpm9gFlJwSog2eO_fj5v4K3gWCIW0vU3emlcmhwUVMy25UDIgDP5e2XUpNaloEXOOZjVr0bCNQudFSKMRBW2SoKun8OkvDWfmCHpK1qG5btXPpmKBUgd4ZhXmqCobcquZEPRKIE8E0yiUGlinqchzlDAM-0Bmw4qNpOmXzHJjb3zUMnk8LL0O35GyL2gVxNdzcNmMSVTM998gh3R4W8HWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزی‌های‌عجیب و غریب وینیسیوس و امباپه در بازی شب گذشته مقابل بتیس که منجر به اولین باخت کهکشانی‌ها درفصل‌جدید شد باعث شد دل هواداران رئال برای یه بازیکن بشدت تنگ شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29114" target="_blank">📅 17:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29113">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2dbRxuUpb3MbWh0VNGbMYF_4gK_HgKC3igxYsX-oq2b1jRF_7sF4eHhXODLEQEH1eWOz8nIR_FETLhNRI0MsoyioVIQ-OtOt8XiQqANVPk3cQMm9khB1MHFFhRpDtvdXcfR9SqKAkZ9R1F9PZa3l8mpGzW1ifSk1RBydPhhZXQ7lGl-SB0WPI8a2RKZyAp57tjJdofVqYE3XnmUDUA36GalaLqHuovJDs1cAeUKcESGUPccetFsrdjUJHRe7uDYyvJPQVPurjneIYfHnVeT6uNwPGUytqOrAnv1sFReGebpBw-nEuvNjp7dch79WpXkcl-47OAxwLYQV4Nd1MNjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه‌آلومینیوم‌قرارداد مهدی مهدوی مدافع راست 20 ساله این‌تیم روچهارساله تمدید کرد. هدف باشگاه اراکی درامد زایی از این بازیکن در نیم فصله. رقم فروش این بازیکن 450 هزار دلار تعیین شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29113" target="_blank">📅 17:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29111">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=Y4lsec7E_yD0K1X4dclM5pnvcO0cqxJZDoP85zkBGTBGVPmF4bRgIurt3KCeyS5RGA9oZoef6qV3PwuC2qqWZ6nTeU4M7jZpriOWUPCZkD6EyvtCPs6ho_ENx81ZZD3-l4IGi_YrOqT4iKsiLl2WFZc4KUcb6KMyG5w1mdc_b5DYGMkvLzN25DaMPDNjQlaHUlyjEDX3p868D9hD6VR6qC2Vy20V7ylJqmU-rlBWDd5FljmtG3ll4hwsZHUUfAp6XkppNv06xatIIGfd5fBO3C-zw1erfvMiSA8hsywNfHxpuM4efrNhWPJjevvQ5DRCHSkEwcXPk2QQkwjCajsfZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=Y4lsec7E_yD0K1X4dclM5pnvcO0cqxJZDoP85zkBGTBGVPmF4bRgIurt3KCeyS5RGA9oZoef6qV3PwuC2qqWZ6nTeU4M7jZpriOWUPCZkD6EyvtCPs6ho_ENx81ZZD3-l4IGi_YrOqT4iKsiLl2WFZc4KUcb6KMyG5w1mdc_b5DYGMkvLzN25DaMPDNjQlaHUlyjEDX3p868D9hD6VR6qC2Vy20V7ylJqmU-rlBWDd5FljmtG3ll4hwsZHUUfAp6XkppNv06xatIIGfd5fBO3C-zw1erfvMiSA8hsywNfHxpuM4efrNhWPJjevvQ5DRCHSkEwcXPk2QQkwjCajsfZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خنده‌های‌تلخ‌ومعنادار ایسکو کاپیتان تیم رئال بتیس پیش از دیدار شب گذشته با تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29111" target="_blank">📅 17:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29110">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ttc2K_wqIr6OShkorGnnpIn8jwrIAcZVNhfNafp6zlaYQzOYC41eOumtPc3Ac6eekleWfatbTHTFjj_IsUSCVEF5aWmJmZ47AS2kiN_Far2gqcdFWOoVNLAByq10mXsFw5TEGrgDK2oER6FBWiQJBG_2lSRmdNeOm-sZXUK_4SzKd34fsx-R-azSKVplCyyoi6CQiQ6PivC8IxOReMLKXsv0D2TJIN-RlkIi5oWvvcdK2B_fwZTSEIZSoEpfucIpHbVo0s07utb-Use2HtSYYg_oP4zYEUsRNk-j5WyiOxLDuX9O-1lq8C-bmMrM-ZNEPaJiQXP04qObpZeZ5FuWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت؛ درپایان‌دیدارهای هفته‌ پنجم تنها تیم تراکتورِ جوادنکونامه که‌موفق به‌ثبت پنج کلین شیت متوالی شده و هیچ‌تیمی‌دروازه این تیم روباز نکرده.
‼️
همچنین تیم‌ های استقلال، تراکتور، آلومینیوم و فجر تیم‌هایی هستند که شکستی متحمل نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29110" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29109">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9FFpwrHCWRiD4XG0plPxTgx_dSHG4Fqu3bPXEhT3dBqJOnt-MTAtAjtDUooQw5DxWduHK0Hlpsx3JNUr9h54EvhgcIcPQQJxBIgb5Ooo5Mg-Xu38edzGZGKirgRa7qsJwj0wXFQirNQvd4QbU5wsMOUnPbSwFteOsneXR_i22JRtAR201eLZuvOXAqccWde0btQvI3LhQhNJxReQrBVSkPt1sq0Q84tS5QsTJk-jy3fTpc_c3VqdWIGdTuCwBCvApzVoWglrFezCOzP058L3NGDVkin0c78dbVyK4rArox1xuOvlgE6HmIRaL07UzAdVYNNADqHzazLvobegcPUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد خلیفه گلر قرضی آلومینیوم اراک علی رغم تلاشی که کرد دروازه‌اش مقابل شمس‌آذر باز شد و در واقع گل بخودی بنام محمد خلیفه ثبت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29109" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
