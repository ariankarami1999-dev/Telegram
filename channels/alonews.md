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
<img src="https://cdn4.telesco.pe/file/OkNnPhH7KymmABjXjlJA3J4cTf_AikVTNSbnH1m4bDqm2NWJha84kZoIGCy220omjQvpXfiZyP81aMPa7vRsfjA6FFCglZgFwNTD1lEsxrrdfRZCyuPTiHl-w1JugPXxQBdJyt8O3VvwfxlTJ8-HKCcUMbDy0hbCyaKUBngeRLl-kFrq9TYzamj5_moK0N_dYiNJUTp22EzDwIzDnGIZf7YqE1_bnhlOTx7Sc2_7PCewFqGL2yFB7DQRmWj_jmERyePfxGyLKRZfWLo-rXS6wRiQmIV-r3yquTpWK9H5jgKKOhNBUHl_2oHGdCq9wVqJf05BrhR4d1eHTquHnYMBcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 18:13:51</div>
<hr>

<div class="tg-post" id="msg-135401">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فاکس نیوز به نقل از مقامات آمریکایی: دست‌کم ۱۳ نظامی آمریکایی از دوشنبه زخمی شده‌اند.
🔴
بر اساس این گزارش، حداقل سه پرواز تخلیه پزشکی در روزهای اخیر، نیروهای مجروح را از منطقه خارج کرده است.
🔴
به گزارش آسوشیتدپرس، از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران، ۱۴ نظامی آمریکایی کشته و ۴۲۷ نفر زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/alonews/135401" target="_blank">📅 18:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135400">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTuqGLC4qwofgPVJkW_uTADGO8acOuyYaseWvflXnQgIFQqV0YLsCb0fapdxkOfbc1X99zcgQsg6vxI3eSmh4JqtrmMzRQmjt0sGTB7WDE_bLhNzet7KWfWx5lGw5Bqb5jgSV6Q0mOMcOOBjM0OWiVbzdFo7INQ7CguIlaLss0dl05HT0ql3PyCwXTHI7fM_Ry-SLo52bNF5dNCRxvxjqCY_8B9owfYr1nxX2BeUmL0b7v-Vst1lYlnSYaQw9iqGBOSUbelbsUP2MkaDZaf8yjKsARRTL1JMEFb4cgQwhuYLN595fbLdyHIVdIDTxPep5TOQHaB8Zr-AkXSsFhRusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر هوایی نشان می‌دهد، نیروگاه شمال شعیبه کویت که یکی از مهم‌ترین تأسیسات تولید برق و آب شیرین‌کن در این کشور به شمار می‌رفت، بامداد امروز هدف قرار گرفت و به طور کامل منهدم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/135400" target="_blank">📅 18:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135399">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJJ9M1oBNfApS1Q7EPodHstnIdtHaZN7XwybFqZJXkZ6GO2heaMOQ_9LXa6JcPocGG6BvhZzv59RG0k4wD_uXijyucTRSLmQO4eD1LJQG7yD1jg-wZ9C4s4PzUi68xgUTt6HKqMfFl1IyHaPL3gz8fDjsmG3IwB_9sixDOnLNCRAegAYcBLRSi9Y4FBc0hGKlliH7abGpveJBvE1s1JzhCfau1EMWh3Yfw1Pkhg5o0qBeF89zce6W0PEMRUF1KM1a_zZcNiUIq4Ra7TuNLFV0zSwUxMZnHuzGG0ioFg5dHimn5iNWbA1vQn7IE5Gt7BUsoEulqoHwRy66V6odu2vqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله‌ی نیروهای هوایی و فضایی آمریکا:
پنتاگون درحال ارسال جنگنده‌های
F-35
و
F-16
بیشتری به خاورمیانه‌ست، اقدامی که نشون دهنده‌ی آمادگی آمریکا برای گسترش عملیات هواییه.
‎‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/135399" target="_blank">📅 18:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135398">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4ca0c082.mp4?token=vBxTaXH7Gi5IsyL56SUqbBpfe2qMhji81JBJb-CW-ZoLVBCA6n_i_n5rGRJrMJsa5o10ssFerkFLEJwyjo_mFrc-ofwIJtF7QnumQUUmHVo5tfBuvA7tS-MErJ2J3t-Mx7i0H9PpaSl0wJtuLe2TU_Ls-cghVQcL7NQhoLE_JOzx-1Wm2raM_xwPb-ACMenvG9HGdN7Zo98r5MQ92eMU4RKHiSnY_lbGj7vKmPBIKkmqaKs9A7MNDnm44feWizCEyHpHakXp8upFzL7nmzP2E0TtRfmNnuXocXpenwYmewqw8Y2cdj_My6_2ad8v9suVb_nWXgCzMbCQOcXPPYaz6gIIocDgTFa7pwJDzFIOCl3pVxp4jo4_dmLSN4xHDR-A3U_CC727gNm2utJXmir4vpXN9FpkJHLqpDZCxpuNcthV8Ik1fmn9i9fRfxl2PunUxsB3gjzxzmhzlHMw7YEbJH4sf-2eHyvtFQ73u5pEfbGfZLa4D4GsY2CI5NhWS8di1JxvlLQW5E-ZPDSTMUw89eLiUqidyUYrl-o8egrCNB3-HLEDkcV2AfLlKWD_KRzTF6IbyJaDqKgHs5BryFm5Yr9jTublMhBE6ADRBI5I1Pe8Twqj7zhTBTQwYKH7z5pSmhJ6-qbWSSl6tPYviGxN19NR-ETHi_hqI8QFOzNL0KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4ca0c082.mp4?token=vBxTaXH7Gi5IsyL56SUqbBpfe2qMhji81JBJb-CW-ZoLVBCA6n_i_n5rGRJrMJsa5o10ssFerkFLEJwyjo_mFrc-ofwIJtF7QnumQUUmHVo5tfBuvA7tS-MErJ2J3t-Mx7i0H9PpaSl0wJtuLe2TU_Ls-cghVQcL7NQhoLE_JOzx-1Wm2raM_xwPb-ACMenvG9HGdN7Zo98r5MQ92eMU4RKHiSnY_lbGj7vKmPBIKkmqaKs9A7MNDnm44feWizCEyHpHakXp8upFzL7nmzP2E0TtRfmNnuXocXpenwYmewqw8Y2cdj_My6_2ad8v9suVb_nWXgCzMbCQOcXPPYaz6gIIocDgTFa7pwJDzFIOCl3pVxp4jo4_dmLSN4xHDR-A3U_CC727gNm2utJXmir4vpXN9FpkJHLqpDZCxpuNcthV8Ik1fmn9i9fRfxl2PunUxsB3gjzxzmhzlHMw7YEbJH4sf-2eHyvtFQ73u5pEfbGfZLa4D4GsY2CI5NhWS8di1JxvlLQW5E-ZPDSTMUw89eLiUqidyUYrl-o8egrCNB3-HLEDkcV2AfLlKWD_KRzTF6IbyJaDqKgHs5BryFm5Yr9jTublMhBE6ADRBI5I1Pe8Twqj7zhTBTQwYKH7z5pSmhJ6-qbWSSl6tPYviGxN19NR-ETHi_hqI8QFOzNL0KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش بینی های نوید کلهرودی در سال ۱۴۰۳ که دقیقا داره به وقوع میپیونده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/135398" target="_blank">📅 17:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135397">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فارس : اگر آمریکا امشب نیز به ایران حمله کند، فرودگاه های دبی و ابوظبی در امارات را موشک باران خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/135397" target="_blank">📅 17:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135396">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عوستاد رائفی پور :  اگر ناوگان امریکا رو غرق کنیم ابرویشان در جهان میرود
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/135396" target="_blank">📅 17:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135395">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e079109218.mp4?token=bUXYcG2mmpWLOt66yuLlEcIC9PtnSxHQvDuuuVcPvpNXnK4ultX7DRhTj0OqwEnN50QyEtpPqr2S-dEnX0V-Ck9WOp6enqA1TgoU1aNJMAKmDXU_lhLzfQxf0R5IpqqOQcGRBcLurncEAoBp2CIMBJaLDWRT9UoELl0eiiK2m1y84kMLyjHTWu15RPh2fFqqBJtPUY7ugpVNIHrxb2cSfrlLWEPswfvxM8kjCUPpqPZy22LF6M03F_VZTBgIYq3TUOSfLUhgSkln2dicJTN9qONXgj3FlSSe3_jfUeuJB0OqrPrQNjAaDMhsfM5l0dhlLVRuvcAM0LAEownLCdqV7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e079109218.mp4?token=bUXYcG2mmpWLOt66yuLlEcIC9PtnSxHQvDuuuVcPvpNXnK4ultX7DRhTj0OqwEnN50QyEtpPqr2S-dEnX0V-Ck9WOp6enqA1TgoU1aNJMAKmDXU_lhLzfQxf0R5IpqqOQcGRBcLurncEAoBp2CIMBJaLDWRT9UoELl0eiiK2m1y84kMLyjHTWu15RPh2fFqqBJtPUY7ugpVNIHrxb2cSfrlLWEPswfvxM8kjCUPpqPZy22LF6M03F_VZTBgIYq3TUOSfLUhgSkln2dicJTN9qONXgj3FlSSe3_jfUeuJB0OqrPrQNjAaDMhsfM5l0dhlLVRuvcAM0LAEownLCdqV7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراسم تشییع جنازه ۴۵ تن از نیروهای حزب‌الله لبنان که در درگیری های اخیر با ارتش اسرائيل کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/135395" target="_blank">📅 17:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135394">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
بلومبرگ: عراق مسیر زمینی سوریه را جایگزین تنگه هرمز کرد
🔴
تنها در عرض چند ماه، سوریه به سهمی بیش از یک‌چهارم از کل حجم صادراتی خاورمیانه رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/135394" target="_blank">📅 17:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135393">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: به خاورمیانه سفر نکنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/135393" target="_blank">📅 17:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135392">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtC8HvAJiz-RHX4tvElllBZ0-ykiw41pZObmEVoPNDWugjmtAqyuGvAedZ_xeiY84je7vaiZ4WwLcXoFD98gV8_6UeFgPPuyY3EInEU62uOCFMFPh1XHlywjdJCUr6T4sGR_yrfB3lVJgO5Q0LNlTH4zJGSJd7F3aM7__vTF3DKuyFNzJWnMqL32Y3UMdOWUn5eNtU_d7XVyLfvTBJI8LR7I4444wkMnaRZT48W8ACSW9u9i8n0p5KoNFJMuL_JDXHy5Hv7q35ihl5EEsgsnn-wX1J1D7JtAYLTCtVN9JB8aejI-23pCd1Qr0vLHd9K7isB5JTZX3kY2R5SAczi8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده مجلس: تصمیم دولت؛ نرخ سوم بنزین: ۱۰ هزارتومان
🔴
برخلاف نظر قطعی مجلس و در مغایرت کامل با ماده۴۶ قانون برنامه هفتم، متاسفانه "سازمان برنامه و بودجه"، ایده گران‌سازی بنزین را در دولت با قدرت جلو می‌برد و ظاهرا قرار است از ابتدای مردادماه اجرایی شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/135392" target="_blank">📅 17:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135391">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/21a6e4c8cc.mp4?token=k5J4JV90k3czHrlwvBufOAAbpVVP9WEjoDu1Dc7RTAZ61Y9hyhk0XdOUqyvDe2B9RIrn9uVYmeFR36Zdn6iAEwWZAwppfwgnLqgEEVDsadmAADai0OD-m-o7R0DhNWxf_OVGRVEYJ4Z0giXFaIAtkHA_RkULq5UBt92xZXDMW1vVu_yDwY3yRGbDCm8pGMFnWZOmqwJ-9AnmsvDn13FXghcU8BkTAPyMGIOfLf2kPmi1pniE2C_trCFDsP2Wlp0IoskWE4zBQuGDAQE2UHBVm7fc1o0B-zjLG6va5_vmnmi4fUv10urYe7RE-oucoWQMgIRsBtHd58H4rRr-pTXBhSJiVE3kjNXlsyw3SDyfgjOtgR7f8VZAxNDgKG66UF6ykAJ01NLtl16EwxQlAvciJZcVRt1xL6GOEejxGluh6R-In8UkUKFfhl8dKjzs79GO07jPXGFQqajcPk57_uFUrFXyG5Z-NbhMWotOcrR1JqD9yseSpf8ZpY05brPP9L52KBxFwA0m2RhRCBBPvH4-GOJ3EjcxRLA_NeBsOVMUfOgAJ_0qfeBQAJPYY5cxn59GhePYaitoJ1z23wl1BENlpGtcysXJ_oEp1PbBAnNP_SX-ucIiiE-1RWHcw40ret30B4TNElZxyLefsAaCaqqKvbyRsuteBbuiv8JOv9Xt218" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/21a6e4c8cc.mp4?token=k5J4JV90k3czHrlwvBufOAAbpVVP9WEjoDu1Dc7RTAZ61Y9hyhk0XdOUqyvDe2B9RIrn9uVYmeFR36Zdn6iAEwWZAwppfwgnLqgEEVDsadmAADai0OD-m-o7R0DhNWxf_OVGRVEYJ4Z0giXFaIAtkHA_RkULq5UBt92xZXDMW1vVu_yDwY3yRGbDCm8pGMFnWZOmqwJ-9AnmsvDn13FXghcU8BkTAPyMGIOfLf2kPmi1pniE2C_trCFDsP2Wlp0IoskWE4zBQuGDAQE2UHBVm7fc1o0B-zjLG6va5_vmnmi4fUv10urYe7RE-oucoWQMgIRsBtHd58H4rRr-pTXBhSJiVE3kjNXlsyw3SDyfgjOtgR7f8VZAxNDgKG66UF6ykAJ01NLtl16EwxQlAvciJZcVRt1xL6GOEejxGluh6R-In8UkUKFfhl8dKjzs79GO07jPXGFQqajcPk57_uFUrFXyG5Z-NbhMWotOcrR1JqD9yseSpf8ZpY05brPP9L52KBxFwA0m2RhRCBBPvH4-GOJ3EjcxRLA_NeBsOVMUfOgAJ_0qfeBQAJPYY5cxn59GhePYaitoJ1z23wl1BENlpGtcysXJ_oEp1PbBAnNP_SX-ucIiiE-1RWHcw40ret30B4TNElZxyLefsAaCaqqKvbyRsuteBbuiv8JOv9Xt218" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتشار ویدئویی از عبور یک هواپیمای مسافربری بر فراز انبار در حال سوختن «وایلدبریز» در حومه مسکو
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135391" target="_blank">📅 17:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135390">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuVDOaXl_S1kQInErzGDKR8E9uRxtqddHE6Okw72KiQlZ_nV2_m-GI4izfhxfej7TblV2FSnyv1ocIMBI5D9JO4mHtaoBbEDaNavNtbqVdXre0JcXwAd3-d6B5Vi8Evfqi7jEa27xattjCvTz3fHEMZIeJIgqFsp4cEmzU617_D0plE7_E-yI3e89xEPUdB9XVTot8xk2eD4Y7tvp6Fi6jux35UgEP-m4HxCCsJP0SPswAhMpu2N6dFfsZMtFlq3AoXh8f72ymheJvEsxTPkvKyvmY0_W0MWeP5vk5u4JAYlRIyCTF_xkZ_ejYt6ENfmKY5lggFCmRWal8jEDLVy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام امنیتی
ایرانی به فارس :
اگه آمریکا به زیرساخت‌های ایران حمله کنه، فرودگاه‌های دبی و ابوظبی و همچنین بنادر فجیره و جبل‌علی باید فوراً تخلیه بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/135390" target="_blank">📅 17:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135389">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
تسنیم: مراسم بزرگداشت آقا تو مصلی تهران تعویق خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135389" target="_blank">📅 17:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135388">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSYIrctF2_2HoZ9WtMtjV6nPGIX6x0jMVEagtznDA_v-CNThVuHSA126Q8E9aFlIMk9FwvOVmPlHXJri6N94Q5wx3duMlWXpD5jX9ggcSZgQqZqcX-DxZhY7t8HjmQO3e1ya0AYPE_RgjyUgIE9Q-tXWpUY-YZlmuihH6YrJ9qBd8xpl4Qb-SYrRqd0OsNmXMARl7tjnAFYVngG1cgdYVdHIxDYul4ZJbKEzVu1q2vgEITARlgFRympFbGjNihXrn-uUZPhyOkS-xmXsg52hs5IApnXuHgjldqXNymyolUeCik_T2jObGHzaz7lnfYrfSNtdTG_JnoXV0akB76L-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/135388" target="_blank">📅 17:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135387">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXydlG7IPezZpR6aQk_NE4plRxC2_uNx_syPkTXGCYNpogEEG6Rpzb1c4RJ1WY9kSl0KzOVKTwajtw7RuEuQp4aHQ9YC_V8HGPL5EC9SV0GOUTuaCyqJeuWYZCC_bjSeki2iP-zLBVVKUIefdqjhs8MzvN5BWg6NqH2zqBb4CEWk71ozAcOCFMv_QTkasp68n0f6FIK1ZaB0RAofr51CVt3kgePP4WFKxiqf0Qrx6XSy2ztBDK-20zDauMJXQyzzdfb-QYXib7-OXvBoEpfXrt7-jbQqqxFh47SAapqnqpAyebhT6vC9lYEIYAeawrh5ZPGWztmjR1wK5j9QIdK7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ولید گدبان سفیر اسرائیل در سازمان ملل:
"موج آهنین در حال برخاستن است."
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135387" target="_blank">📅 17:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135385">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e8Wjsv1eT0MFfgV_5AvPq_LYt0WuT44Jyh5qh5vwyB9GWK68AkK9OWn9poDgkjwgJ430k1grKR7PwtX4sY6bZlJ9C01T3M3lT74AGUzR5TzANB5_L6gpTOCugVteDoepWyrrCF1qBPLwHy0UJKyLZBDmeS_NoBR9msE5isYSAJm91MHPU6E3ajablo6uSARUZe357BgknPnY8IT5P4kUJ84fs_6nnTmw7YUv1weWJ-tB3ZYLPKNQFext6DMXUPCgN-oTj4n_Zcq_BbVYVLGkTZxNsVKu7t2QW-Knb6kX2Jo5icowtwGfXGZ-uyeHSSCN0ond_60GGim0Ne6bXaTH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o8AxzT2rumxYitLpB2joWm9LERvTrh9ZOuGcPiecMrzvrilQHn02GAMEil8nHrNLh3ECnz4F23glSsIuD0lZsZybkpa7_F5mPXD3QmHjS66YeatBbgmQIVFRUo1DGrg-zIfYv4hm0Sw5Mijaig1_Ox0dsKo2sE72eBNf5yE8eAIrPdsjP7MUmQnEzTLl6faiQZ8ejaTRLO2AsPECV_Ics9O1OyGEtIDVYRT-uoiI8pjGYYb-ivRzu78t-FiomkiXfQGcQ7flegaFDmI8mcUr-iFww4YLorqZXZwnMt2jwRlVvHnEbk39mGWo6w2vcH1LuUXnDeYYRLuAXEyS2QCxoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از پل جاده بندر عباس رودان در زمان حمله و اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135385" target="_blank">📅 16:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135383">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bt4IaRp9fGTq53nIrEq2bwlsimGA2KN5hmAFuzJQq4b9sVTxfL5pKgwflkAF5x_FGWcoBb2c_gpgrBgNK4tghGxfYcM3xYYgqy4-Mxt9FIjvkLMzHVclzuO2Pt5PV7vhuHe0At0jasmnYMVeyQ8q7dDEt3Nh80n2ZlB1bDHvlo7S0Mt_fbuDtqrWmn4kkRR79vf6QT3RuUx7546yV7IjV_kfvXtU2RBSpOPTB3rz5V2bFDE-rVFjkHYQG8GuxJpcf_wRv5U3QmkEGL5heEtBkARFDMq_ea5Cs1B0qkAOuq6zt73KhQ99JhHKnAwpf06SQvKRaNfOaHobTleFZ7rFHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kHGz15tgwzjJmyQLRXEKN8hIytUBjtAUEB-1qtjsHrnqni3yYSm_EXGG4nXvhKQta2Xyakb5zMagYPf7OrYA2cQUZEj3wt1Nu-Cf2-1KOAjw0f0HgkxbIE4PvX2UrDJVYQ0_k0bOphTANZNcLy7sKL7mg4ikOkLeq-uWLPltLf1IPTIuDX4uoOWEPOsI9adS5gSjXCI3HSM_ATsqapBCkkNfYrke_UEDtg0nJUgGWcCdGH4-fkEYYRlsnjR3SDK8QtRX6fm665LZxC41U4PxXcB4LDa2KwSPTT8qOok7VwCnOa5UdPhq__GrCt4DsFE6ReLdY3380vAVF8_Y64BOPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ایران، اسکله شمالی شرکت ملی نفت کویت (KNPC) را که نفت خام را صادر می‌کند، در کویت مورد حمله قرار داد.
🔴
این تأسیسات در حال حاضر در آتش است و دود ناشی از آن از طریق تصاویر ماهواره‌ای قابل مشاهده است.
(منبع: MerruX)
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/135383" target="_blank">📅 16:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135382">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AzotO_u78fE7SPu_CLeXdBfcvdTJ_y3TYI3drLA1p_AZhEa1_rCerSwOlHfq9oTOyI7Z_TzyLkyZXbm0AZF2N7-6jGO6dBAe28wF5uDqla-Ct-c20PTpq_SLvPDl97O7zkDrbQrQ2WDNi9y7EtNZB06mA4zeWOgt51N6m9P67LuViUJA39KWZRH5TYrVDW5MJj-_iHCndXSDffF35jgJ93tDXYKYxunfFnj7hNBXAqWHh__xN7GRK3z10uDzDXhO0EE_Bv_vyUi40xqsIZuZZrzDosRWxaU22nTNPYhDEK4_n5bisH710P8BTHNi_AW-DIyAA2P0mJhD8PNS8vrXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی جالب در تجمع امت معکوس
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135382" target="_blank">📅 16:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135381">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پست دستیار سابق ترامپ
B2
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135381" target="_blank">📅 16:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135380">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
انقدر تو جامعه شکاف و دشمنی بین مردم افتاده که بهترین کار انجام یک رفراندوم اساسی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/135380" target="_blank">📅 16:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135379">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری/ایران تعلیق تمام تعهدات ذیل یادداشت تفاهم با ایالات متحده را اعلام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135379" target="_blank">📅 16:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135378">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
می‌دونید چیه ؟
حماس هم می‌گفت ما منتظریم شما زمینی وارد بشید جهنم درست کنیم براتون....
حزب الله هم می‌گفت زمینی جرات دارید وارد بشید، وارد شد و....
سپاه می‌گفت جرات دارید موشک بزنید، موشک زد
گفت جرات دارید دست به رهبر ما بزنید... دست زد
حالا هم میگن جرات دارید حمله زمینی کنید
🔴
همانطور که قالیباف گفت، واقعیات را باید پذیرفت هیچ جوره از آمریکا بهتر نیستید مگر اینکه در مرحله آخر با زیرساخت‌ها قمار کنید که محکوم به باخت هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135378" target="_blank">📅 16:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135377">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY8YzX-DT_Qpb6-V6JtyjlbKX80eArjkSPgnjY2EEEBpsYcoO8Fg0uTdYxZLYG4vi99XirytR30WdfMhr0TCpQ8ozL7G1a2sRUAMhW52_R17yyGp8kXhjC-KCd_Rv6HemktB-z2V5aUMVCfY5Q3WPWqvkAwzcsvES4epnl3LXEkD3_xPixmL7ffRu9HNKRaSLQUyE0TEELeLhW6wsa0kD6-FeDkNa3iPvx0B37PpzswF8p84tKaAe6yphpmvhyWwtR1UDWM7tMPWqqDBlrvuPTlNVJVTl8W9BV9Lj4aoDf1dZUkXdAE-LwwjKOFcRuI2X1ipkBZLCBjOVxd6Jic_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طی حمله آمریکا به پل‌های بندرخمیر، 8 نفر از هموطن‌هامون شهید شدن
🔴
عبدالرحیم جعفری فرد
🔴
محمد مؤیدی
🔴
همایون چترزرین
🔴
مازیار چترزرین
🔴
مریم پراکنده دل
🔴
سوگند دردمند
🔴
فاطمه زهرا اکبری
🔴
مریم حیدری‌پوری
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135377" target="_blank">📅 16:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135376">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599d7cb052.mp4?token=sBFrfpBNGwbCPOU2MwsV72vw9nrwBb8nCraxmOiZ9kS9CbvMfDfXdBsM3CFQloNNlvXYwYakktVGUpFXNKmFvyL64f_ZA7BfW_KkVKnVsJXsl7A1iqmKP1qZf5Gz8W1MgpRMF8_Qxkp31AhUUQyyftf2NO4474zlmrOmm5BFZ60nYRAUD3vNTJWAwL9Z1cgKu9aCtZLSRefCWOuTl4lZpeaz5_rVYkXuqnFM8APD9WeC51AigL-2wuLbp6tXxWPIxLqBdNgaAEjiVoadQnBcYTcfB5Khd6gFm8OejMmtO8hDPlJy6atIczSclxhVR9KAwRgtudvKDtZsBCJdh7Vw7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599d7cb052.mp4?token=sBFrfpBNGwbCPOU2MwsV72vw9nrwBb8nCraxmOiZ9kS9CbvMfDfXdBsM3CFQloNNlvXYwYakktVGUpFXNKmFvyL64f_ZA7BfW_KkVKnVsJXsl7A1iqmKP1qZf5Gz8W1MgpRMF8_Qxkp31AhUUQyyftf2NO4474zlmrOmm5BFZ60nYRAUD3vNTJWAwL9Z1cgKu9aCtZLSRefCWOuTl4lZpeaz5_rVYkXuqnFM8APD9WeC51AigL-2wuLbp6tXxWPIxLqBdNgaAEjiVoadQnBcYTcfB5Khd6gFm8OejMmtO8hDPlJy6atIczSclxhVR9KAwRgtudvKDtZsBCJdh7Vw7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت کنونی جان فداها
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135376" target="_blank">📅 16:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135375">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a740eae1.mp4?token=nRxGTzmHsO8hQrCqqAKHkENCTd08YgZoCLi9GmChfCSkekw6YMs-M0yU-J9g7obNjeebcLlt72rfUnp4ch4BTaiF1_WdWK1fe0RFdhtg1DbeHr7x2YRmqg3rjhKTaVrbF7PpxwQcTJKxj68gq-MwIPY7nr5oqffzHe9Rmf86V35b-0U16CL9bFN58U-kpdGBe5BLrkelb878P7EkgsWu0P7QXxzFffq3BQpai2I-gx4Sy9p_KyZKBMCv49uEyvlbQq1j7Sws7GPQ-xAAWq5Vmxnoj_D2cCY9KI3FVTh-Pdz7sDteTmYnq1PyZbwIgASixlFDaQAzZ0O31vtcDPD07Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a740eae1.mp4?token=nRxGTzmHsO8hQrCqqAKHkENCTd08YgZoCLi9GmChfCSkekw6YMs-M0yU-J9g7obNjeebcLlt72rfUnp4ch4BTaiF1_WdWK1fe0RFdhtg1DbeHr7x2YRmqg3rjhKTaVrbF7PpxwQcTJKxj68gq-MwIPY7nr5oqffzHe9Rmf86V35b-0U16CL9bFN58U-kpdGBe5BLrkelb878P7EkgsWu0P7QXxzFffq3BQpai2I-gx4Sy9p_KyZKBMCv49uEyvlbQq1j7Sws7GPQ-xAAWq5Vmxnoj_D2cCY9KI3FVTh-Pdz7sDteTmYnq1PyZbwIgASixlFDaQAzZ0O31vtcDPD07Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با کدوم پول میخواهید بجنگید؟
🔴
ما نخواهیم سر غرور مسخره شما یا مثلا انتقام یه نفر زیر ساخت‌ها نابود بشه باید کیو ببینیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135375" target="_blank">📅 16:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135374">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
منابع عربی از حمله به پایگاه هوایی شیخ عیسی در بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135374" target="_blank">📅 16:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135373">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMgWerkPXYGMr-a_d3ie_bhrHE49axEXT9KEDm5J7BUHSD3H54f5Qv8e3gVRPiOok0Kr605tH6Ktiowm95VnePB7xSmDAXDUmB2bb00V2qjO87wH7x6gLRdNMxujuqPegnQ2LnLx8FWbwSk7vTqhKbQ9AD7IXreKNNq-5S-wS-nh9IarJwrwDwwkQoqXA9ZY_n9V-xOr8TfyydXxqbcc0YoR5sc_7aol4VOb7nyQTeZSd6Mv4LpA1Sf1jshjUi26NxxbdHeRp0SaEO-rEPd_LNn9nNuw6o7NmeNvrW-whWrfugd5-xdQL6W6xDC1EY-81Pe95POQmU02yQUcyTvwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز: فیلد مارشال ایرانی به ایالات متحده اخطار داد که در صورت حمله زمینی، راه بازگشتی برای سربازان آمریکایی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/135373" target="_blank">📅 16:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135372">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/5f8e3863cc.mp4?token=rV8cvQdGwsmmtwUE-qAQk_119yVksqtl201E-a7OojdjZZQ9e1mezDBeDQ4oGQU4H5x2MSovDXf0RJQgBOL5zjQqx-0oaM5XbzNNVYvOFsC-I0hQccPFpTnxXPDD2hILFZn5JcuE6PryGB6yUQwhmJoBXt4C89R1Eck0SbZdXtSEnAVIF2-wf9osFoiSFW5pahivh1QRdPej9MWSQ_dTtC8zSFEDCI71B13HVznVV9VNDCzFS5MccYAw1GbzNkcG98veaL3FIDb7HHLnXjmIJhLsSLzT771oA-5JjIcmlxalJbLa5JhdBzgM7hdGI77y4zS4cGpBHKQOn-LYoaPG2A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/5f8e3863cc.mp4?token=rV8cvQdGwsmmtwUE-qAQk_119yVksqtl201E-a7OojdjZZQ9e1mezDBeDQ4oGQU4H5x2MSovDXf0RJQgBOL5zjQqx-0oaM5XbzNNVYvOFsC-I0hQccPFpTnxXPDD2hILFZn5JcuE6PryGB6yUQwhmJoBXt4C89R1Eck0SbZdXtSEnAVIF2-wf9osFoiSFW5pahivh1QRdPej9MWSQ_dTtC8zSFEDCI71B13HVznVV9VNDCzFS5MccYAw1GbzNkcG98veaL3FIDb7HHLnXjmIJhLsSLzT771oA-5JjIcmlxalJbLa5JhdBzgM7hdGI77y4zS4cGpBHKQOn-LYoaPG2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر منتسب به آکادمی سعد در کویت که مربوط به آموزش های امنیتی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135372" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135371">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سازمان ملل: ما همچنان نگران تنش های منطقه‌ای هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135371" target="_blank">📅 15:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135370">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
اداره‌کل ارتباطات هرمزگان: در حملهٔ دیشب آمریکا به‌خطوط انتقال ترافیک و پهنای باند در بندرعباس و حاجی‌آباد، ۱۱۶ دکل مخابراتی از مدار خارج شد.
🔴
درحال‌حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که تلاش برای وصل‌کردن آنها در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135370" target="_blank">📅 15:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135369">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
اسرائیل هیوم: ترامپ تمایلی به دیدار با نتانیاهو ندارد و اختلافات واشنگتن و تل‌آویو بر سر ایران، به تعویق این دیدار و کاهش هماهنگی‌های سیاسی دو طرف انجامیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135369" target="_blank">📅 15:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135368">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / اکسیوس: ترامپ در حال بررسی یک عملیات گسترده علیه ایران است، از جمله بمباران تأسیسات زیرساختی، حملات بیشتر علیه تأسیسات هسته‌ای و بمباران سایت «کوه کلنگ»
🔴
او هنوز تصمیم نهایی خود را نگرفته
🔴
رئیس‌جمهور آمریکا ممکن است که در روز‌های آینده دستور تشدید عملیات را صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135368" target="_blank">📅 15:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135367">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
غریب‌آبادی: تعهداتمان در تفاهمنامه اسلام‌آباد را متوقف کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135367" target="_blank">📅 15:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135366">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
به صدا در آمدن آژیر خطر در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135366" target="_blank">📅 15:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135365">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135365" target="_blank">📅 15:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135364">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
انفجار در منطقه میناء کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135364" target="_blank">📅 15:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135363">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
به صدا در آمدن آژیر خطر در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135363" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135362">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135362" target="_blank">📅 15:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135361">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ممدانی شهردار نیویورک: به دنبال قانونی برای بازداشت نتانیاهو هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135361" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135360">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مقامات آمریکایی به «الحدث» گفتند: ترامپ در حال بررسی گزینه انجام حمله‌ای گسترده به زیرساخت‌های ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135360" target="_blank">📅 15:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135359">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d3f43769.mp4?token=MS5nt1D7eUYWtbvMYeFsDgVIO3TnenRx4Q4snBNUEtVB1h0IJ7t3j8-E7YD8FrKgBDy3wcQNexMPqpkWqg39jH1LXv-J-66M_e1IwpEOvVzj81Jv894G3LAvW87simmAbDiVSHgaNLNOylB5a7SBW0Mi61_RQc2FaLUiEuKEjnoN8a5p_GWithUTjBo59fdDKmgErH481Senli2voNbkeM0biaJa-QlJsRMweB7X5Motf6Gl2VFHIJ9_wYH-QxtbWlK9IhywnyRfTvfRfHDfk_bNbhq7CDSjOJm3mQOaBQ2NQSIZzcejimSWUmiqO2iKNQc08ThUOAIrsGI6mIaIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d3f43769.mp4?token=MS5nt1D7eUYWtbvMYeFsDgVIO3TnenRx4Q4snBNUEtVB1h0IJ7t3j8-E7YD8FrKgBDy3wcQNexMPqpkWqg39jH1LXv-J-66M_e1IwpEOvVzj81Jv894G3LAvW87simmAbDiVSHgaNLNOylB5a7SBW0Mi61_RQc2FaLUiEuKEjnoN8a5p_GWithUTjBo59fdDKmgErH481Senli2voNbkeM0biaJa-QlJsRMweB7X5Motf6Gl2VFHIJ9_wYH-QxtbWlK9IhywnyRfTvfRfHDfk_bNbhq7CDSjOJm3mQOaBQ2NQSIZzcejimSWUmiqO2iKNQc08ThUOAIrsGI6mIaIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دولت سوریه اعلام کرد یک کامیون حامل میوه که به سمت مرز لبنان در حال حرکت بود را توقیف و درون آن چندین  قبضه گلوله و موشک ضد زره کورنت/هویزه کشف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135359" target="_blank">📅 15:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135358">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfM55zotzK7-MtJFnNRNVVveFwQkoNJ4Z9EDGUsqSo-gLqBN25M8rDgu9bjXRAW9fu4YteB4xi0RmIQhhRl68uMlJ61y-zb-GbWSp7a4RpjtXirxkwnvreeUaozSFawyGeV7Lz7b9fW5IQpuz3uc_vEUrPw4_W5ILZ5bvASyuUgryFg0KnuFVq7qxxs7wYYW0Y92i0vIsHziR2k2ysQxGrMwBsL0Cs5ydRj_TXtXNbtwzAAI_bhBgPHFx67rVn4D7d77zPwOP8g8q3TlgA_VwVnWGyvL627Ecv4KgEATSsAVUUlyXyhPketPS0joZAOVqlGfEVTrvS1kFjiBRKtjwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پایگاه های نظامی در اردن هنوز بعد از گذشت چند ساعت در حال سوختن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135358" target="_blank">📅 15:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135357">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZDnimTPedBulHFi2JG34woJVuU39d11yIQGu4J1Pi8LdAtpJ0HDyVJfx7kRaxSWWq-M0ls7V1u-lCFQePLqDT0SA7mfw0_P6S2WNhrZujfvszhV8ofVPvdOKSr18qLMNb7gru8DXvmHJ8uYWK3l5RL-U86pF60npfnfLQko0ejOWtAijupWqhlEp--pc3QaFhZIBwiFNmjEK0hJrBHN9wrnf0BSzZlzaZTK60g1i-6zyIsHWV5byDlQ_WdcmIuXUM3XGWPm44htTwkaY3W-0ccvxjSW_r0pM9ha-2plLvTba0C8rWZKUDsuhJLLASxNhHld1QNPh02sXl3kYelZ-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات پهپادی اوکراین به روسیه، هفت کشته برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135357" target="_blank">📅 15:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135356">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رویترز : حملات پهپادی اوکراین به روسیه، هفت کشته برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/135356" target="_blank">📅 15:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135355">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
شبکه "فاکس نیوز": نیروهای ویژه ارتش آمریکا سال‌هاست که برای ورود زمینی به ایران آموزش می‌بینند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135355" target="_blank">📅 15:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135354">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
پزشکیان: من واسه وطنم هر موقع شبانه روز که جلسه بزارن شرکت میکنم و مشکلاتو حل میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135354" target="_blank">📅 15:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135353">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ایرنا: در جریان عملیات عمرانی نزدیک بیمارستان دی در میدان ونک تهران، بر اثر ترک در انشعاب لوله ی گاز، انفجار رخ داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135353" target="_blank">📅 14:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135352">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رویترز: کویت دیشب یکی از بدترین شب‌های خود را سپری کرد
🔴
خبرگزاری رویترز گزارش داد که کویت یکی از بدترین شب‌های خود را از زمان آغاز درگیری‌ها در خاورمیانه، در جریان حملات تلافی‌جویانه ایران سپری کرده است.
🔴
در این گزارش آمده است، در جریان این حملات، دومین نیروگاه تولید برق در کویت طی دو روز گذشته هدف قرار گرفته و حریم هوایی این کشور نیز بسته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135352" target="_blank">📅 14:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135351">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
۱۱۶ دکل مخابراتی هرمزگان در حملات آمریکا از مدار خارج شد /تلفن ثابت، همراه و اینترنت ‌با قطعی مواجه است‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135351" target="_blank">📅 14:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135350">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO-RSdPD4Vbd1Lib8QMxywU3FYxJMhvrt0LH0kKpFeSn-M1twgAGaK-akhomGSqAO1zX5L31v7AIJWoVUnB0kITdqmHh8uXoJZYRoKxDql3xzXr_KXRw5yH2rISwWiDiU8V6-pSbilsb7YJ70ho_C3xYzgUGVMRWLCChTe0XEYgTL5n9C8ymd2TLY58uvd3MsUZO0xhuUaeChdydMzQv8Zso6Z9WNm1qQltmvklOlsciXRG793bWZZS0C3oV4sq_F-24lDh7ZACVyJa56L7E4ltVTIH8P5wHKmykDRgKKkEulVq8qhrGqqxFgNqmPMf1t-raCq059ypWn9ZOJilhSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمیدرضا مقدم فر، مشاور فرهنگی فرمانده کل سپاه: اگر آمریکا بخواهد از طریق دریایی و اقتصادی ما را تحت فشار قرار دهد، هزینه انرژی و اقتصادی آن را اروپا پرداخت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135350" target="_blank">📅 14:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135349">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس جمهور عراق حملات ایران به اربیل در کردستان عراق را به شدت محکوم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135349" target="_blank">📅 14:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135348">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-h9WaDBK_z7qOEeIYSbjgdcQgQkk55ImC1ngI29HvElksCx5_8rOLQIJIumL1zvEHcSBV9OV_O04LwUBDik2PFwNtRtfpxOyh8qTcVPXQQKLWGOR40-4iAmDGneNFbD58aNQonQCOssGt0H0AWV5lWmL8QIFO8U6npWg7Ukl2ZhUmLcEERDY17kkZzWx6W6S_ZnN70Aq8K7TUXWvXKr4kKVZlTWxZBYeyyhtvd0wif7J6DnyJtHMJpm27QxNl6DWKcG8YR_NQEn0YC8RlLmlyLaWjrCwgheqGeS569rZwugnedTXQN1Qt_frZ6X7CBJ8gFKvCy68zewuyEs5SV_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از رد موشک های ایرانی در آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135348" target="_blank">📅 14:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135347">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
جنگنده های عراقی ، حملات هوایی را علیه پایگاه‌های داعش در منطقه روا در استان الانبار انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135347" target="_blank">📅 14:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135346">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/العربیه، یک مقام آمریکایی:
ترامپ به ایران فرصتی داد تا تصمیمات درستی بگیرد، اما آنها تصمیمات اشتباهی را انتخاب کردند و عواقب سختی به زودی خواهد آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135346" target="_blank">📅 14:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135345">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
خداوندا بزرگیت رو شکر که هرکی مرگ کسی رو خواست، سر خودش آوردی.</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135345" target="_blank">📅 14:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135344">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN7HxrjrFZmg5wtBGA_pI1gxOQTv9SiEYVd4tpGVGoJodL7Qq8aTUThn-zS5AOtuI0Iu_vJep1-thfvwdR3v4G_hx05DeXXInwfc1rPuw6HcLI3d1xqGqTBQdq45nGFpFO2h1bMsqE4xPyf8_P_Zj_UGZZxHMHGjKh__orsMOg6lI7fMijdc72E0JY7_DRLUCjaSb-jaDaSKf6_jCSkBrrUKLfQeL11vZ-2LQiEnw-jbqY1OTjmvhWsagq5hY0cOEzwsQxk5Yu1k_ipwvEzBNMj8fa607IWNBhh5iJ6jifmD8HVCITRwixmR4lL3zGwJsBn4ziYmAsxU1fcsjo0BcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: اژه‌ای و قالیباف با تمام توان برای احقاق حق ملت در کنار دولت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135344" target="_blank">📅 14:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135343">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0375faeb3d.mp4?token=SIkwlvfGhr_KaiZ8Co95A-oRczxxseTLLgMm85oc5FkxudHUA058n1VcBN2CWhNVutARodVA2H8RQU6PypZvUMupv-s0xXFwmYj84rOLKxPCzlwIxEBNePgJFAdlMVjEooYLidqVks5EL4fSFNvzKFsepawKnAhLmTgQFSOmdd02LY_pHXpL21OVZ7_kxyo8H1fT2-1nM6Nv1_3Qivjdao-u937Sw7QUnuoALpRpY3bXSZQM-FO_s6A76_zFFmpRIptsg31cPg_GUwLnprTjqCnjjiDeAr7Vs6xsRaEJoIBzBCUEtnaIO32a9SIdmLgWZi8VDzKQqsYlED4eWl47GxY9wveOc4m15i_SZoQBpmLC5AAaayXdiTjeH4llZsD88Cb2aV0zfVTLDGTwDO7DHTK50g9Slsb2kOjUMikTfe5kQVx4rSRpkXYhJFaWLvzdlTnmNd4KvHFEwUZ_YMf194kjNn42jN51L_IGxZlhU6J9EDK_J1HdfoeFXoSBJDT7esf5YkUocnNPsaFDp6cmhlQg5GcEvkJziOyoWgGeuMABJx3lktLtbtjF7lBqogRIMtOEDwtn-uXKdIa6JsIv7CAHTejUHDEdXKOqPFHEKmR9oyFTXLUMJsYpG74nEHT2F_fCkntSM-fTpv9uY0KmszJyhsyWY2nl3M4v4Y5AEWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0375faeb3d.mp4?token=SIkwlvfGhr_KaiZ8Co95A-oRczxxseTLLgMm85oc5FkxudHUA058n1VcBN2CWhNVutARodVA2H8RQU6PypZvUMupv-s0xXFwmYj84rOLKxPCzlwIxEBNePgJFAdlMVjEooYLidqVks5EL4fSFNvzKFsepawKnAhLmTgQFSOmdd02LY_pHXpL21OVZ7_kxyo8H1fT2-1nM6Nv1_3Qivjdao-u937Sw7QUnuoALpRpY3bXSZQM-FO_s6A76_zFFmpRIptsg31cPg_GUwLnprTjqCnjjiDeAr7Vs6xsRaEJoIBzBCUEtnaIO32a9SIdmLgWZi8VDzKQqsYlED4eWl47GxY9wveOc4m15i_SZoQBpmLC5AAaayXdiTjeH4llZsD88Cb2aV0zfVTLDGTwDO7DHTK50g9Slsb2kOjUMikTfe5kQVx4rSRpkXYhJFaWLvzdlTnmNd4KvHFEwUZ_YMf194kjNn42jN51L_IGxZlhU6J9EDK_J1HdfoeFXoSBJDT7esf5YkUocnNPsaFDp6cmhlQg5GcEvkJziOyoWgGeuMABJx3lktLtbtjF7lBqogRIMtOEDwtn-uXKdIa6JsIv7CAHTejUHDEdXKOqPFHEKmR9oyFTXLUMJsYpG74nEHT2F_fCkntSM-fTpv9uY0KmszJyhsyWY2nl3M4v4Y5AEWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک ایرانی در آسمان اردن
‎‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135343" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135342">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وای نت: 10 هواپیمای سوخت رسان دیگر آمریکایی تا امشب وارد اسرائیل خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135342" target="_blank">📅 14:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135341">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری / معاریو:"اسرائیل" و ایالات متحده، سطح آمادگی خود را برای از سرگیری جنگ علیه ایران افزایش دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135341" target="_blank">📅 14:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135340">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
قیمت دلار به ۱۹۳۰۰۰ تومن رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135340" target="_blank">📅 14:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135339">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز: بر اساس گزارش‌ها، نخستین تماس بین‌المللی مجتبی خامنه‌ای، رهبر جدید ایران، ممکن است گفتگوی تلفنی یا دیدار با ولادیمیر پوتین، رئیس‌جمهور روسیه باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135339" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135338">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ثبت سفارش جدید خودروهای وارداتی متوقف شد
🔴
دبیر انجمن واردکنندگان خودرو ایران:واردات فعلی از محل مجوزهای ثبت سفارش سال گذشته انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135338" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135337">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
شرکت ملی نفت کویت اعلام کرد حملات مکرر ایران به تأسیسات حیاتی بخش نفت این کشور، موجب مجروح شدن افراد و وارد شدن خسارات مادی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135337" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135336">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ارتش اردن: چهار پهپاد که وارد حریم هوایی اردن شده بودند را رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135336" target="_blank">📅 13:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135335">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت نفت کویت:  خسارات مالی سنگین در پی حمله‌ به یک تأسیسات نفتی‌مان رخ داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135335" target="_blank">📅 13:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135334">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
پولتیکو: «آیپک» یا کمیته امور عمومی آمریکا و اسرائیل، کمک‌های مالی به بیش از ۱۲ عضو دموکرات مجلس نمایندگان را که از کاهش کمک‌ها به تل‌آویو حمایت کرده بودند، تعلیق کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135334" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135333">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
دبیرکل سازمان ملل : نسبت به حمله به زیرساخت‌های غیرنظامی ابراز نگرانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135333" target="_blank">📅 13:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135332">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
اژیر خطر در شهر الازرق اردن به صدا درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135332" target="_blank">📅 13:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97983fad64.mp4?token=deKCmM0dJFIHrL_wuzEY3Jjlso-3pMrBPNDH-DZcJvDiKbtzr-wZgYCmNvrh7VjaHTJ1pVYMlywqVt7SfXI9KJs6LtSlGm99JKl4DcYtkZ6dlFNOqpYFOSMDy4h6Qjagr-pjWTknZYV84lKHhQ6rx895Ae2ZXyoL0rSdTYPwETBKABH1ncrfYnZdyzHhHKeXCsJf2MdEe5pnpqFldNCjZFRmX6mdDOOh0VhvDiXLAvnKNkR8fq6TBEyWk0nND9B-Vm7xfjh6tPOS4B0S1LrFAiw8ucTIgWymjd-VCC4jBhPG75F-EZRA-gs5M88O52bhFDfJwwNEmg0Xf8gnQB-2xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97983fad64.mp4?token=deKCmM0dJFIHrL_wuzEY3Jjlso-3pMrBPNDH-DZcJvDiKbtzr-wZgYCmNvrh7VjaHTJ1pVYMlywqVt7SfXI9KJs6LtSlGm99JKl4DcYtkZ6dlFNOqpYFOSMDy4h6Qjagr-pjWTknZYV84lKHhQ6rx895Ae2ZXyoL0rSdTYPwETBKABH1ncrfYnZdyzHhHKeXCsJf2MdEe5pnpqFldNCjZFRmX6mdDOOh0VhvDiXLAvnKNkR8fq6TBEyWk0nND9B-Vm7xfjh6tPOS4B0S1LrFAiw8ucTIgWymjd-VCC4jBhPG75F-EZRA-gs5M88O52bhFDfJwwNEmg0Xf8gnQB-2xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز های متعدد هواپيماهاي آمریکایی در ۲۴ گذشته از اروپا به خاورمیانه
🔴
این جابجایی ها خبر از یک درگیری شدید در روزهای آینده می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/135331" target="_blank">📅 13:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
اژیر خطر در شهر الازرق اردن به صدا درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135330" target="_blank">📅 13:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135328">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mp24Ey8Eg0Atfqb498wh9_VKSx8dY8cfeSF4teGzm0g3FTMTM39Ie0fevQpdsKp8IKGQKpOekyhfFV2bMLB7q69FZScdIED_m8DjXC01QLDdqwUjrqekIf0S1Egi4reKN9P3BhUyiCDJ7S-7rJRFEGqdoTzVtJWz50euyEZGSUhrDaa8-w6fLCc73v7kc_O2VxLT0Qlemk9LR8CwHtN41d0fiea5DxRv-PYhZwQE3RjkHOlvT6PAeTJuun29citkhNkcxuzU6ZbYsfuyD9XHedNqIhRC1EBjdM9xeBwSr7mBhcPTwBbg_x0usS0I7dVp2Dd3NllOw1GODFkrP4iacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ER0-kyUONoq2n3hOLDbmvsBpwkdOSkhhTNYIPPuLCsypDuFBWXYL1Oqzg3uQdwemymwLu9cu6FI8WnPqrsdfQ2kgDinCF_ZP3PZRecHL67L6tGkOw5ImcPvR-e3iW5IB9z_BUsQAj9I-VflTx8h2xe2Xl4ohmFKqRPB-bI_gdmAZso_M3P7hG2VDe8DdR-uEcFP2Tfemzo7FdJV_8mfQzBqoFNUb5tYQwh8HC6SEhZb3yczA19v_UwU3FPBFsfDOj-JaVeVvMnW_b_vFefKhpvscsHS_lx9q6u_VGG-rkwQ8QUQ2cZWOndignLVII0F1Pe3YuNUh_sIIes7qkkGl0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از موج جدید حملات موشکی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135328" target="_blank">📅 13:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135327">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
عراق ۶۰ میلیارد دلار قرارداد انرژی با شرکت‌های آمریکایی امضا کرد
🔴
در نشست تجاری آمریکا-عراق، شرکت‌های انرژی غربی ده‌ها توافقنامه نفت، گاز و خطوط لوله با عراق امضا کردند. بغداد به دنبال تقویت روابط با واشنگتن و توسعه مسیرهای صادراتی جایگزین برای دور زدن تنگه هرمز است.
🔴
شورون قصد دارد در خط لوله‌ای از عراق به سواحل مدیترانه سوریه سرمایه‌گذاری کند. کونوکو فیلیپس نیز ۴۲ درصد سهام «بی‌پی انرژی کرکوک» را خریداری کرده و به بازسازی چهار میدان نفتی شمال عراق می‌پیوندد.
🔴
نخست‌وزیر عراق تأکید کرد بغداد از سیاست درهای باز برای جذب سرمایه‌گذاری استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/135327" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135326">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
موج جدید حملات موشکی از ایران به مواضع آمریکا در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135326" target="_blank">📅 13:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135325">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فؤاد حسین، وزیر امور خارجه عراق، در گفت‌وگو با Rudaw English گفت که علی الزیدی، نخست‌وزیر عراق، پس از سفر به واشنگتن برای گفت‌وگو با مقام‌های ایرانی راهی تهران خواهد شد.
🔴
نخست‌وزیر عراق در مسیر بازگشت از واشنگتن، ابتدا به قطر سفر می‌کند تا در مراسم تشییع جنازه شرکت کند و سپس برای گفت‌وگو با مقام‌های ایرانی عازم تهران خواهد شد.
🔴
روداو همچنین مطلع شده است که علی الزیدی پس از سفر به ایران، در ادامه یک تور دیپلماتیک منطقه‌ای، به ترکیه نیز سفر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135325" target="_blank">📅 13:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135324">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
العربیه به نقل از یک مقام ایرانی: مجتبی خامنه‌ای تا پایان جنگ در انظار عمومی ظاهر نمیشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135324" target="_blank">📅 13:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135323">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
گزارش شلیک موشک از لرستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135323" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135319">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSXNRlRaRScYwK0B-hepB6IhiCfG2kF1gJVBGQXdg1ZGyjpR_sTaQKOzMPxyAtsQmRYvvErj3jcZxgnvmbTn4dFZBUV89GJahbILnyICrkm5JZhgMe6yUsEE4z5ZdfVx-sEQxY2h7vojLd2Xvj588yArVz5NC5Fcf8XmQSnF5tqcePtPSKwlQihf8p-Bs-AWJd80iTy4JcpI9nbdhoIGUL3nk1RxYNfge3205YfXNQs3NhRtBMRRksck3xz1vcF72YejZlR5bFVbMe7lPav7YvYXqD86oWapw7fmPoszztAmMssfSaDiqe97M7Ittv4yOFzXdK5Uuh8v9L8tQO6f7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mkEnuDMqr56E5rS-Vm5WrPvRPvD56XEEE_cJYURmxbj3hi99gYI3m_HU_5_LBWPMcNtOD17f-eFmPCBwZAkhOstnAfiyC9O5Mey6-sq-8aLCROXqAQq5_GmmO_CGRahj55gYY2wS7BNxO9fh5e8ueKgtmSUJensY2PAPsV7VzjlS0Kdjc8UW3nfuI8S56YyQw3mn8KE2DgHtTScU9NTSa40hfW_BCYKA1wKPmgedWG3GH6zIvKrXbms1JX7IX1A-4qqMcoeFDoeRgTQJxz-8mkJzIvXyqB6JNmGvzVNYfQvxHqGQL8OnH7fBOF0Xf9uHbmycXwhveygOSRW4s1qpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_IOUoNjqPXdkfHlGN-bvihy45ij0qaoeUVa4rjOUNSzmRod3wgYFUesBP8zF7qkdbif_8rybif8glQVauUvlD9cFWLWSmqn3dSodGcVjMf6myORvWBdmk-BBbnFVmdAcpV1TP0zw-29x-7wnN0i2al1_auQZVObyrmgnyaR3NZs2Y3Z7dgemBb530HAel3Z4XAOikYct9UYTCGP-rWSwBXvwFAn8G-qGmts369vI44jIf5_RpIWxPLkm6BwBmHcwaZdEqCd9KeKGmN9kCvEwXwQF3kz1XM2plU67AiAJSQxzjY79aRpj-hUFgqT7PuDG2ahjWOjMRWxNncnK-z5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udngaFDz9wsnVEM0uhqX6WfTTbTwhqGK1xhHQG8Vc6aIVVJxkfL8kY2kY3mxwzdd3aPtWu6XDie7jdXa9duTMovbwcImS0bobQOhOE6mwhtXzr2dqrrq-rNaV-Xmbt0s_J1aH5DBEDSc9gkjiNfw1jlI8C1WeaHtoACJhBqA1nWWgKfHisZ3eFSLoGwXtM5RTI1wZra6JZ5YEOkcdT_Ho4SV1W4IrRRw2MndIOyRqVSiunUANVCeN8vg3VsNiQFQ0OVXGWMyjM3vTLzCQdQWSKAr3BAUpSvqqSHa3IJO1juq4Rat9_un52sG1ziNVbW9_Ydb6_QVRMe-1n_TaWF7xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک آتش‌سوزی بزرگ در منطقه کروکستادلوا، در شهر درامن، واقع در جنوب نروژ، بیش از 100 خانه را تخریب کرده و باعث تخلیه بیش از 400 نفر شده است.
🔴
این آتش‌سوزی که از دیروز آغاز شده، از مناطق مسکونی به جنگل‌های اطراف گسترش یافته و همچنان مهار نشده است.
🔴
حدود 100 آتش‌نشان از ایستگاه‌های مختلف، به همراه نیروهای مسلح، سازمان دفاع مدنی و هلیکوپترها، در عملیات اطفاء حریق مشارکت دارند.
🔴
چندین نفر دچار مسمومیت ناشی از دود شده‌اند، اما هنوز هیچ مورد فوتی گزارش نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135319" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135318">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GotrTd0xHM2Xq7ZarLQaMX888POUkkbgEpNenF0hynCKX_TUAxxRfQ_2ECF2qD43SVR7rihW5kwn0QwYxt3G1RidRZtk38BuIchYVaO8LhLFHrQ91TQHHmiJY-oBI8ypnZhN8rbHVkXDjgtAtOJydYp7RPeXWIPD-4rQV7rzlVZKq48LrYGTtbsiPTPNo3SnXN6aHB8fLmj7vuLlblRlQ2cr5VSg8PT1O7n5ZNkCYzzz1NcN9jmULVn4S0EFNkqu2O7bLneLAkiwKuBIod541G9qgjeahNOePb4JvDuPoJ18bFIDrQDCud29L6IexVd71UrLnffsFxrJii8sPpLCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل: آمریکا هواپیماهای سوخت‌رسان بیشتری به این کشور اعزام می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135318" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135317">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بلومبرگ: قیمت بنزین در ایالات متحده با تشدید رویارویی بین ایران و آمریکا، بار دیگر به نزدیکی ۴ دلار در هر گالن رسیده
🔴
قیمت‌ها تنها طی ۱۰ روز، حدود ۲۰ سنت افزایش یافته
🔴
در حالی که بخش قابل توجهی از ظرفیت تولید پالایشگاه‌های روسیه از دست رفته، پالایشگاه‌های آمریکایی بیشتر به تولید سوخت جت و گازوئیل توجه دارند تا بنزین خودرو‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135317" target="_blank">📅 12:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135316">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
دقایقی پیش؛ دو انفجار در نزدیکی فرودگاه بین‌المللی اربیل کردستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135316" target="_blank">📅 12:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135315">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اتحادیه اروپا (EASA) با تشدید دوباره تنش‌های نظامی در منطقه، هشدار امنیتی خود برای شرکت‌های هواپیمایی را به‌روزرسانی و توصیه کرده است ایرلاین‌های اروپایی تا ۲۹ ژوئیه از پرواز در حریم هوایی بحرین، کویت، قطر، امارات و فراز خلیج عمان خودداری کنند. همچنین توصیه قبلی مبنی بر عدم پرواز بر فراز ایران، عراق و لبنان نیز تا پایان ماه اوت تمدید شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135315" target="_blank">📅 12:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135314">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbTuMdYvoqA5oV6ugs00MpUaMD4vDnyji5YcDxczXnSm_6_xxIHGhibo3DlAPwHOC1sR22KnQDoBDc8iMc21L7qjml9MaLjWGA41nwbBzgZc0yt8fH06YZ845bcs_rXwWEizttqq5c3WsDBaB3lRv4Jiky4NNwDNB3_bGdn4rv8BezLPdX-bioI03YCyC9m87xWCI24tIqTg7S0HXx0S4PLigoqOLtvD5lil5IQhgTt8ja2o_mfLa5QbObrML1D6SjCbD383IvGrZB7dj0SoCC5aWUfkzEk1NiH7WNxyF0lLh5DLzuJVlks0Qk7zdQTfowd4MRIVrGvRkXDBNGNjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۲۱ هزار واحدی به ۴ میلیون و ۷۷۳ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/135314" target="_blank">📅 12:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135313">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
معین الدین سعیدی، نماینده سابق چابهار:
نمایندگانی که بر جنگ تأکید دارند و شعار میدهند لطفا زودتر به جنوب بیایند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135313" target="_blank">📅 12:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135312">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqCZSJMlotHrNCk7tyJjH6o7TW-RqYdi-BP5cBd2utktXkmi3PgGNixa50tOt6hBJxAjtSH3KwSYWev8XkcFvLl2FeLoN7z8jDKmN5kDrNG4XUQ-npzEzlnfqMgqKtKrqV9gLubFzSMOzi7BT7y2gIy7ju33__Ggks_WFjNfyoo7I-gJ5V1qkudKyNOa8UH_ciOw3RUGQX4IFoQaE_fQ-U9bvLVDkGCWmzg23X93XFRzY_STSqlFFl337ir0sOd1UFlGWXLbutJ6rLULCZGSIqmEXtTG_jcy91Zt_FUIprFuEhTEoVkBytRGxUabR9HVwhPWs4vjxTazIUJH-eTffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات جدید اسرائیل به خان یونس در جنوب نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135312" target="_blank">📅 12:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135311">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس جمهوری اوکراین: تأسیسات انرژی در خاک روسیه را هدف قرار دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/135311" target="_blank">📅 12:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135310">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزارت خارجه آمریکا هشدار سفر به کشورهای بحرین، لبنان، مصر، عمان، ایران، قطر، عراق، عربستان سعودی، اسرائیل، سوریه، اردن، امارات متحده عربی، کویت و یمن اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135310" target="_blank">📅 12:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135309">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d04de4038.mp4?token=THx5BKdJUr1uD_h7tCRjJ7q17ZfEjxLYZ5FraphoC6W5oTQ_ERj1ty6L6JAwmhWreRbvmVVLN9fCmJib5kGGC3GWqGb5TpkDhfgEdrwrKivUOHBJF6Z8Fq2adv0jnUtMYG8GmZWvsjqzauvGu_zkxn3vuhLeC74drjoxNfknnJ5nh4YeSV5ToKbxDhSByj6wniJDhxVYJ_FdVK3dyp-dqnXBnymfgrHuJTQtqubUP6yufukd9VFKthJJ_DSAETRlR0nLRxFzdhQD6uY5HJ72GLkaI81vAAIBoLA-cZ3YX41PATS91WEKhLO5hzsM1CH2yYuVXQUXfytya2Bqub7u_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d04de4038.mp4?token=THx5BKdJUr1uD_h7tCRjJ7q17ZfEjxLYZ5FraphoC6W5oTQ_ERj1ty6L6JAwmhWreRbvmVVLN9fCmJib5kGGC3GWqGb5TpkDhfgEdrwrKivUOHBJF6Z8Fq2adv0jnUtMYG8GmZWvsjqzauvGu_zkxn3vuhLeC74drjoxNfknnJ5nh4YeSV5ToKbxDhSByj6wniJDhxVYJ_FdVK3dyp-dqnXBnymfgrHuJTQtqubUP6yufukd9VFKthJJ_DSAETRlR0nLRxFzdhQD6uY5HJ72GLkaI81vAAIBoLA-cZ3YX41PATS91WEKhLO5hzsM1CH2yYuVXQUXfytya2Bqub7u_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تردد در جادهٔ بندرعباس به رودان نیز که بامداد امروز مورد حملهٔ آمریکا قرار گرفت، از سر گرفته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135309" target="_blank">📅 12:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135308">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ضرب الاجل فیلد مارشال محسن رضایی برای آمریکا : آمریکایی‌ها فقط 48 ساعت فرصت دارند که به دیپلماسی بازگردند بعد از این زمان، دیگر فرصت دیپلماسی به پایان رسیده و نوبت به جنگ بی‌امان خواهد رسید که تبعات ویرانگرش را نه تنها مردم منطقه، که همه کشورهای جهان خواهند دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135308" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135307">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b779c493.mp4?token=ALtOkdBFangLyqS4syCmV8rHomV6EruODPH1JZ8dDw_CPdQ6zZSk65vdInqU6Jn5B9opLLxt8tYSZxhImZaH_qTXG0wGIT075kdAuVL0Y23txo6jJz9y8JMDszC1Cy1EBwE3jHGGpb3DXdHHsEti_a_E43Tr-OK3P2Dx7EviFXrmhuI-y-OM66-bgT0BPrjzeZrWiBlzahAQv_Jo5bN4CJwnrdvu720dhyOqWIbW5Bn0aC90Ixe5CskTmPO442tTyedLx8K3x7oa1_KcfOFwwI4cfLZHK9w7x_Og8tsbC6UjKTJOA6hjV85iVngbhQ99Ifj7F843pNICoQzEQNmD-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b779c493.mp4?token=ALtOkdBFangLyqS4syCmV8rHomV6EruODPH1JZ8dDw_CPdQ6zZSk65vdInqU6Jn5B9opLLxt8tYSZxhImZaH_qTXG0wGIT075kdAuVL0Y23txo6jJz9y8JMDszC1Cy1EBwE3jHGGpb3DXdHHsEti_a_E43Tr-OK3P2Dx7EviFXrmhuI-y-OM66-bgT0BPrjzeZrWiBlzahAQv_Jo5bN4CJwnrdvu720dhyOqWIbW5Bn0aC90Ixe5CskTmPO442tTyedLx8K3x7oa1_KcfOFwwI4cfLZHK9w7x_Og8tsbC6UjKTJOA6hjV85iVngbhQ99Ifj7F843pNICoQzEQNmD-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی به بزرگ‌ترین مرکز پردازش سفارش‌ها «وایلدبریز» (Wildberries) — بزرگ‌ترین خرده‌فروش تجارت الکترونیک روسیه — در منطقه مسکو حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135307" target="_blank">📅 12:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135306">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIBMjKriJLbzKGtYl0yheDbERznCAQ07spMH9ojpoD1WtB4-49mzpcR2lATy0J_olcViuUtKRtwMCLAvxFA-CxeA0iljnRv0NOjfNpSlal-IuWSIJOCuhVD6DUTyz9FEfEopETHZ1JGpUpwbvQ_O_cMamcwU6_8x2MGU3m8OK1ereu2et4Lb9oQwNmHr5lzX-SNBCJG_gR4YTPWN66Mj5v4ke0UVHaXPDucQfLyt01m2QrvDIat2NGUIIPzC3AM-znobuF_VjpNwuKceglYK8S-l9LYQ69zYRbSNBdeq2GHKaxckBMscXnPOpcI_Xll_elZUiJGUUSZwyv8hJjFvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد قربانیان دو زلزله‌ای که ماه گذشته در ونزوئلا رخ داد، به 5069 نفر افزایش یافته است.
🔴
16740 نفر مجروح شدند، در حالی که بیش از 128000 خانواده کمک‌های لازم را دریافت کردند.
🔴
این زلزله‌ها به 856 ساختمان آسیب رساندند، که از این تعداد، 190 ساختمان کاملاً تخریب شدند و هزاران نفر بی‌خانمان شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135306" target="_blank">📅 12:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135305">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سخنگوی قوه قضاییه: برای ترامپ و نتانیاهو پرونده قضایی تشکیل دادیم و کیفرخواست اونا صادر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135305" target="_blank">📅 11:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135304">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a265df119.mp4?token=mk7H4mrQiMkBIUx9zD5kXia5lyFlAf6TpPJHQp2uzhsuSUMhU49Grx3k6rUtFnBr0kxRXfJ_Kh4lh9AlTaMPeYED8tNyrhcN6v6tRFGhrXFyhyuPne-2Ws6dSJIatown-L6Xt0EcwnJjxYUXnBD_ugzKoGSObcYtJGzl_johmAAfqlQNsQIYg0riGcUMt6KzU3PQ9RIm-gVq1OrIO78uLSbcat0hZTDVDlQiS0_BprMFqD3o-DxV-UsQg0JR1ncXUlOTv1Zd2_l9eZmxk8YmleS3lfqkKtn-UYVRb4SB4hvC2eAmsQATc92nqOiAO-Z8Tda0n9Bk1-ss3ddxltLIFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a265df119.mp4?token=mk7H4mrQiMkBIUx9zD5kXia5lyFlAf6TpPJHQp2uzhsuSUMhU49Grx3k6rUtFnBr0kxRXfJ_Kh4lh9AlTaMPeYED8tNyrhcN6v6tRFGhrXFyhyuPne-2Ws6dSJIatown-L6Xt0EcwnJjxYUXnBD_ugzKoGSObcYtJGzl_johmAAfqlQNsQIYg0riGcUMt6KzU3PQ9RIm-gVq1OrIO78uLSbcat0hZTDVDlQiS0_BprMFqD3o-DxV-UsQg0JR1ncXUlOTv1Zd2_l9eZmxk8YmleS3lfqkKtn-UYVRb4SB4hvC2eAmsQATc92nqOiAO-Z8Tda0n9Bk1-ss3ddxltLIFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوووووووری/ترامپ ترور شد
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135304" target="_blank">📅 11:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135303">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
دست کم ۴ اصابت قطعی در پایگاه شیخ عیس بحرین گزارش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135303" target="_blank">📅 11:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135302">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e976fc0ba.mp4?token=ne8GUHXFTUv9QfanTrKRNmbOdVvTz1IXULpS-fXQbygmnVFIr43WQVfXNNlxXObpaoVpWkwECgT1ZkETGrRoJPEz1E19510mFbCINJrx-IR4-Sy0-Ho1OWlVjP6j8n734Y0Fvqwm6KioHar_dtuPZZhfAw5001Rb__jhEaR4XPH-WXY8mWsoCOIC4O4Sak0BrlRdVK_ddjo4n_o7oHxFm4JQ5JLR-6sCF53nqhjD5idhYgybDzDKRJ1QWP1TiRAC01Qs_tKJ2cJBS--v10Y9qtX2w1mmec5h7czHVe7roYrLrS9-ZIkZf9NSp_KMqzYl7fx1BWFgcQEuFzF7zLH88w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e976fc0ba.mp4?token=ne8GUHXFTUv9QfanTrKRNmbOdVvTz1IXULpS-fXQbygmnVFIr43WQVfXNNlxXObpaoVpWkwECgT1ZkETGrRoJPEz1E19510mFbCINJrx-IR4-Sy0-Ho1OWlVjP6j8n734Y0Fvqwm6KioHar_dtuPZZhfAw5001Rb__jhEaR4XPH-WXY8mWsoCOIC4O4Sak0BrlRdVK_ddjo4n_o7oHxFm4JQ5JLR-6sCF53nqhjD5idhYgybDzDKRJ1QWP1TiRAC01Qs_tKJ2cJBS--v10Y9qtX2w1mmec5h7czHVe7roYrLrS9-ZIkZf9NSp_KMqzYl7fx1BWFgcQEuFzF7zLH88w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاقی عجیب در مصاحبه با یک جانفدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135302" target="_blank">📅 11:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135301">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnsswojiyoDpD5pjF8eSnpLWQlul3IUMY_ZtZppgnOCQvPFtEhz7Q2m3R8xHQkkY308soHfI_n-yWaZDNMhOJL4K6Bgcd6-kkVowPM1ILmW2bKEhNRz5k-Q1Ldwm-9IHkosBx_MMn91o4gxh99a-O1qKkAUrzsnB-8kkCjJTQOQKP8luk8RRTrVlxvrIL_djie3JqY88hgrx_HQiHcue7rEpU-R_caY8ltajiytrYY-tBHAixU-lpntP-e5aSG2BbmrL5NWzFV62HxD6wO0stJqUNJDoaYc_PuwYIDlPaC6yQ72gyEZZMbvCzqLwBtzl8BtIHSU8Vws2bk7QRBhBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه آتش‌سوزی ناسا (NASA firemap) آتش‌سوزی بزرگی را در پایگاه هوایی موفق السلطی در اردن نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135301" target="_blank">📅 11:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135300">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjHNRWU0X0gMuL7SHVeaRr0R6jXnuQ9lqfrBYzgFm8NmWb4NkWYihecHzxPuGzJXZXFM_Bub5ZjEdY2LUwX93uSgDWC12X6gIbctdB1NPUk5yGz5uoHl4IicnSTFM4n8hEt6RfJra1xMFXVCt3A3ZIPsGHsn_dnLyTvyjQvC_jyFfv7yjdteHFGFUAxtTjBboGkHWQCs34NqBHZPsT9qtSaUuTzdDLax6enzasGgugl6Lcs9ZBwehlBUKj_OggeG4e-AIydqOqNU1LNy0WAjzOprHIgW0y3jp8p5pHH4K4hyKq5bl7AXeqlzN8KNFbRW1Gn7U2nPYpeB5yxS71i_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاطمه مهاجرانی، سخنگوی دولت: دولت تا پای جان کنار مردم جنوبه و از صبر و ایستادگیشون تشکر میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135300" target="_blank">📅 11:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135299">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ارتش کویت :  یه نیروگاه و تأسیسات آب شیرین‌کنمون، به‌شدت آسیب دیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135299" target="_blank">📅 11:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135297">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmxyepIi6famyttEoW6tw8NNWYJ_ONzGGRUS-c6cLb_3c3z_R3Kp0gOTsM5UkBwHO1Sa_6RLcvi4kZXZPVXb1IP0gx7dgbYZo_nCWtN76zGwXxTRH3dvRicGrNGHP5XqdWPT1Ykln7etAtDt3faS9mPicCnsM1KDY2yqNmIz47klf0EbjSUY9MZYLjLx9M6QSFKIcqHU0ShBWS3xFjJuJUt6X8L51XVVAiHQ152DnIsBJmHnNpXn7Ugsp30THzk90qsQX_zqFINc8EhXRScvSeKfzhqNLcpXS5ucTBZOghRYI4x0EYmlZSgfdBGXindXWSZzDj8nSzHw_yWleviKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22fbca48f1.mp4?token=DcvqFsLwCgw0zFORfsd7sbzpPJXN-rBQQ64CEJpzI7gOZBqp5pc0JU-c8CC_VNwS7Fh8l6YbazPk0RO5Wrkm8qBgTz90LZkheNYGTZF0XvOAd8-2MQWxy4P345_Ubl3WUgXT69C1vopOI3aU3hDklgZTOY-IsOJ8to5IUDmnLcsJAZatrLZ3CjeBXQvZDHYAYsTxVYD6oCrPEDVHLXD-iOIabl5jA2AJ26mbAPyLcbZTUqiBikeFhnQg9XyjxiXY98x8klFwk057OpFxSVh5O84nadgR_6ajnT9mKmqgU-pQ4BnDQrO4T2IO2zWUusnUqsZtq0jm7YtTqv0cT2WGvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22fbca48f1.mp4?token=DcvqFsLwCgw0zFORfsd7sbzpPJXN-rBQQ64CEJpzI7gOZBqp5pc0JU-c8CC_VNwS7Fh8l6YbazPk0RO5Wrkm8qBgTz90LZkheNYGTZF0XvOAd8-2MQWxy4P345_Ubl3WUgXT69C1vopOI3aU3hDklgZTOY-IsOJ8to5IUDmnLcsJAZatrLZ3CjeBXQvZDHYAYsTxVYD6oCrPEDVHLXD-iOIabl5jA2AJ26mbAPyLcbZTUqiBikeFhnQg9XyjxiXY98x8klFwk057OpFxSVh5O84nadgR_6ajnT9mKmqgU-pQ4BnDQrO4T2IO2zWUusnUqsZtq0jm7YtTqv0cT2WGvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پس از حملات پهپادی امروز اوکراین، بخشی از شهر مسکو در روسیه زیر پوششی از ابرهای غلیظ، تیره و تقریباً بی‌حرکت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135297" target="_blank">📅 11:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135296">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
گزارش انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135296" target="_blank">📅 11:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135295">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
از سرگیری پروازهای شیراز-دبی پس از ۵ ماه وقفه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135295" target="_blank">📅 11:18 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
