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
<img src="https://cdn4.telesco.pe/file/tGzl99DTxpMYOc03avwktwhPr1Ug2QqI8isfIt_NvNRFPWdSn-5pI4b80idjKbnsm7U2HOBnF-ipKQ-UNWctSL5lbCN2qB3KTcge1uw-SGV3uvXT5uIeYRI0lDVO8Q37AnUwPSJDuccTqXS1mr6SdYkjeQungtc2LOL5V1PK9eGbRGX-g8gyId3SU_gggTzhu_M8Zzc1rk1GH0UYhORFRxJk-juR-G8omp2B8i4c_zgAkMH5Wr1RZlSFhijyUBohqCXk4Uqq2aSErseUpXh7aQoPpF2q9IVsUNaGb8JWJot_keM2MMyzXogK26DabfbRnQAaI_-bsOVik3AaxZ-P0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 984K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 15:12:32</div>
<hr>

<div class="tg-post" id="msg-143350">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 18 · <a href="https://t.me/alonews/143350" target="_blank">📅 15:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143349">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
پوتین: ما در حال حل کردن مشکل سوخت در روسیه هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/143349" target="_blank">📅 15:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143348">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee3b1ebd9.mp4?token=fCXGmROLE7SJ-WYmaRXPVz_Fisg2hsO8yR4kcjJLBK3kYxM24R93V4uIDIj5IP-JtjKOH4KIa1ZPZ2PdfxBlRyfDQVwL931--2aT0J5iWZNF9ReQNb5wvo4qYd8xUFshfJpxsTLqkd6lF8xjefm7llp8Ni7xckw8qtsyvYJJvcUGCnte8LNLGQ2Hjoa2xpM4V6YfkVO-XQWQMN-bNVPNdPqx5n1XKFFBr7ftfEZOLg4FDZM0Pn3k4-EImt05kA3U4Ct-ytQNge1CJ657YArFdkqFsHGVDrgs-XBVGNQ7OMcA3aX80SbZZS0iqsWtPrNkaThmP6dLPO6iJW4BIgk7T0NXppDbZ115arLC5g9upjyR3xpV4qyXuxch-w6MD3IERrss11h0pkJ4MPzl8Nxf442qZ-VZqlQ6bDVvdXV1QBX28Mi8KvJ7lSYGzQTClfXBo8ndYQvWZKnkRr-bMkU2U8QsJ_6DFUDTb3AmOIj-g7YypR9vyTv8GP539R2Wu-juGiS-o6NOLxnXX5rWK3jUS9DNiu__FKzX3G2S816Tf6oQz8wQyKD8FGdeCZQFKj7x7GnLnIjcNpcZ7sPKvGyQ8nOYGu0aXl2dG6q-7PRn0ILBH6N4ou9HvpvJ2gB_M63DTD4Rue65bhqu2sXzfEyyQvdjMCzuGyj9h23ILXhUYR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee3b1ebd9.mp4?token=fCXGmROLE7SJ-WYmaRXPVz_Fisg2hsO8yR4kcjJLBK3kYxM24R93V4uIDIj5IP-JtjKOH4KIa1ZPZ2PdfxBlRyfDQVwL931--2aT0J5iWZNF9ReQNb5wvo4qYd8xUFshfJpxsTLqkd6lF8xjefm7llp8Ni7xckw8qtsyvYJJvcUGCnte8LNLGQ2Hjoa2xpM4V6YfkVO-XQWQMN-bNVPNdPqx5n1XKFFBr7ftfEZOLg4FDZM0Pn3k4-EImt05kA3U4Ct-ytQNge1CJ657YArFdkqFsHGVDrgs-XBVGNQ7OMcA3aX80SbZZS0iqsWtPrNkaThmP6dLPO6iJW4BIgk7T0NXppDbZ115arLC5g9upjyR3xpV4qyXuxch-w6MD3IERrss11h0pkJ4MPzl8Nxf442qZ-VZqlQ6bDVvdXV1QBX28Mi8KvJ7lSYGzQTClfXBo8ndYQvWZKnkRr-bMkU2U8QsJ_6DFUDTb3AmOIj-g7YypR9vyTv8GP539R2Wu-juGiS-o6NOLxnXX5rWK3jUS9DNiu__FKzX3G2S816Tf6oQz8wQyKD8FGdeCZQFKj7x7GnLnIjcNpcZ7sPKvGyQ8nOYGu0aXl2dG6q-7PRn0ILBH6N4ou9HvpvJ2gB_M63DTD4Rue65bhqu2sXzfEyyQvdjMCzuGyj9h23ILXhUYR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک کارنی، نخست‌وزیر کانادا:
ما آماده بودیم و به توافقی جامع نزدیک شده بودیم که برای هر دو کشور منصفانه باشد.
🔴
اما آن‌ها تغییراتی ایجاد کردند، از جمله تهدیدهایی علیه زبان فرانسوی، فرهنگ کبک و فرهنگ کانادا.
🔴
این قابل قبول نیست. این هرگز قابل قبول نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/143348" target="_blank">📅 14:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143347">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
عارف در مورد قیمت بنزین: اگر مردم مخالف باشند اقدامی نخواهیم کرد/ ما ملاحظه زمان جنگ را می‌کنیم/ بعضی اقدامات خوب باید با تاخیر انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/143347" target="_blank">📅 14:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143345">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35f6e38e93.mp4?token=rnE9eKmnoWr8y7yUq78X0GDU34_xw143BrWsHy4yplAoqeDqInRaRyRFijTuvHAaPn5_CkUz_KYDd1Rpv3t-a2vetBRb_9AKdEKG3aFpDdMJ9KRS57ieQI1E2SN4GersakCHwWySvWhMXPIUVi20FGtxD4Gzd3xatVeyOp2uJGY4DpEqzos1PDQwHiHkW0l1aAspli0oMCUUO5f1S8Jbmq-DKVViYfH1YZ0AMj_Dh-qL7zp8Xt2Ca5bssP8YFzA_kbPiMz9B4LRlyO7P9bhXI7RBcx4UQ13TqvWUOMgojCsktvdnoAJJzJb8J-TmjfLmb882oUuL3pGar40geaAa0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35f6e38e93.mp4?token=rnE9eKmnoWr8y7yUq78X0GDU34_xw143BrWsHy4yplAoqeDqInRaRyRFijTuvHAaPn5_CkUz_KYDd1Rpv3t-a2vetBRb_9AKdEKG3aFpDdMJ9KRS57ieQI1E2SN4GersakCHwWySvWhMXPIUVi20FGtxD4Gzd3xatVeyOp2uJGY4DpEqzos1PDQwHiHkW0l1aAspli0oMCUUO5f1S8Jbmq-DKVViYfH1YZ0AMj_Dh-qL7zp8Xt2Ca5bssP8YFzA_kbPiMz9B4LRlyO7P9bhXI7RBcx4UQ13TqvWUOMgojCsktvdnoAJJzJb8J-TmjfLmb882oUuL3pGar40geaAa0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نفت: برای قیمت بنزین تصمیمی گرفته نشده است­
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/143345" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143343">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XkX4iVr5D5Fd8UQpkYJHKRzKYhlMJVYlMVYCqa9JB6V9-lonJCndK6TAPmI_f35sB604jEZl-w-jpyaXqNhGd3w6UzK395VQagCRPoEc0W3EJs7mY8aZX-B9kaUInfb8KtwqPzZxpdgoEiPVZR1ZTBp8WDTngZqwdsp-uVLHc-WwpkWziEiNEH7YDHAFkqLT3lwjl61UtAi9sgVniZGhMnpWSxOOGQMWuRpCj1QxrdQbh8X_Uw8HRh2KKZOAXFODoEqEH7pfohqWfEtjSYLqBYrcGpHxe0701g0C3xmu5M52UKHFUyuc83TqoQaGm2vut28gu8WkrLY8Cp1Nqh92DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFz50aYxDjQ884uCrO7_mGnXJ1scw8lXWxrUvjmrMSGMeUO3b35Ev56xp4g_DSKYJdSoKTT5Pa8Smfh1D_Jvl8bOo_F5v6S8_dBzuBFHVtk5uo2VSe20Udvot8PXnWX1GMRSmpaFQoywwvVmmH-Aohdfd2IWg0ew5ZYFYJRvyeVwq_gY3-dgoAfaCSNU6y-hTFsmeUr052ZuFnDc_AwtWV6bo5Z7hNj9FrMwANNByOpRHRBy-FUsY42ms5VyJenynCTecFZB4omChFNt6x6ixPFPdgizMSZbPgWj4cDlmfMf-FD0JIbtXBMLngoC4ygx_pklACej4yAgO_ebK13a2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که همان سه کشتی متوقف شده در تنگه هرمز حضور دارند، و نشت نفت از کشتی Minoan Dignity همچنان ادامه دارد. به نظر می‌رسد ترافیک کشتی‌ها در تنگه هرمز نسبت به دیروز کاهش یافته است. همچنین، تعداد کشتی‌های موجود در نزدیکی فجیره حدود 10 کشتی کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/143343" target="_blank">📅 14:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143342">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoWOmVvKE08ZrWOrH3ek__3v5QC5FShxpqM0ZshTkLWAoaHGootxSPWciK-Hw3HT5556lxRaIZYWgfu9u3Q4B_g2rqlrA9-pRcIIPP_OLv9vyCMIrO16whUhXyG0TOkjH5Nx1RWXcC1nsBEGdsvuzcvB8KbTQOA3BUwwN5KTq67D8eoc2dXMwU8kATB-FpRjQMOAqYA20XaXB0xkR88mxqRqU6Ti9MhQlH2VWqHybeWLn5dSMvo_vKbymC8oPiQrj8jWurf9hqJ-iQZXuFBDTCcrbfx722PpmEXtpEXEUaq1afZViFbTOfxCCJubAtQoeQUmI_gsP-035XwwHgmmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آبفای تهران: ذخایر سدهای تهران ۲۶ درصد است
‏
🔴
ذخایر سدهای پنجگانه تهران حدود ۲۲۰ میلیون مترمکعب کمتر از شرایط ایده‌آل است و میزان ذخیره سدها که در ابتدای تابستان حدود ۳۰ درصد بود، اکنون به حدود ۲۶ درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/143342" target="_blank">📅 14:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143341">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عباس عراقچی، وزیر امور خارجه: آمریکا راهی جز صحبت با احترام و مذاکره عدالت محور با ایران ندارد.
🔴
اینکه بعد حمله نظامی دوباره رسیدند به همان راه قدیمی یعنی تحریم های اقتصادی، نشان از استیصال آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/143341" target="_blank">📅 14:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143340">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
روزنامه شرق الوسط: قالیباف در سفرش به عراق از دولت عراق خواسته تا بدهی ۱۲ میلیارد دلاری بابت گاز و برقی که ایران بهش داده بود رو پرداخت کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/143340" target="_blank">📅 14:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143339">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
هر یک دلار رسما 200,000 تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/143339" target="_blank">📅 14:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143338">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: رسما گفتیم دو دیپلمات متخلف فرانسوی باید ایران را ترک کنند
🔴
سخنگوی وزارت امور خارجه امروز با بیان اینکه رسماً اعلام کردیم که دو دیپلمات فرانسوی که مرتکب اعمال خلاف شدند، هم باید ایران را ترک کنند و هم امکان بازگشت به ایران را نخواهند داشت، گفت:‌ اقدام فرانسوی‌ها قابل توجیه نیست و برای تداوم روابط ایران و فرانسه مخرب خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/143338" target="_blank">📅 14:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143337">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaG4nanxh3tXv7xSwaO4KSNQi_vOWpSm8TJAnvv2j8ZbYiA9L51yqV2nzlcZS3emvGnH0JIPdVC7kCm8kEPsK9ATAX5e1NiXbHJ9PrCUxg6y--cRZDhcaMdeSXlEAbtNiGdJ0vN4sn8Bb8GQBW4XyBp-DLP0Q4AfkQaZzMSgi4q8YtpgWW6eUL5MyFR6xqM-evXQ5G7ZXeUvLDXfYxPXYTQRmUF1jykJQh5zxIVdQYacVAfbzThisBqUjX5buvTUNo0sfgtikPe-Vgcwiqu05YqlESYqFP4h8V82d1Wmt5UkBPHpdNWuda1eKf_p7y534I4_TfFdoUy5IX3z-hpEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق پیش‌بینی این دانشمند در سال ۱۹۶۰، دنیا ۱۳ نوامبر ۲۰۲۶ (۸۲ روز دیگه) به پایان می‌رسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/143337" target="_blank">📅 14:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1rGx7MQxpB4sCg6ruCAyGb0XmAV1iWS3mi77VB3IcAnPFynmmBoOQqwQWnuKj8egGPy2QWu7z7JnApbdUag00tLN7l5GSbe4fBLYpdt0brXJYQvhIal0B5X7TKouTphLozmivJ5Xf_RoC6mRvGXYG7PJ43SMBP2oJUhBlOVzuSXJQsaVbQMAPv0sONF3yoFBTmpCZp94v4omLdk7uKXyiht560753sgimCj_VigwN2YaA4SJqwREfHQE3yFMARLH0lW3zPCha7RDgYGJXHGSe9NxcQXgJYhukwXCLlAtewqLjUdq0KzbVeoJML__zTvS0tmMKStS-CFXZlOjgVzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rp0vFXBlWJ_0CAZGVwh7EmeyT3KQDjN337PvWQnYlaK3XgvIG9c_5cKhohtRrsk8fraPIa2NrTPyXJ3ZytJ9lYtGy_sJppTpt00uevVJ6oW6pNLdhQvVsOmbRzcKuraQAXP-SU1q10h-vDEiM1CgwdygMTP0wAbqBJmxBhBmn8MmgCDSrbYcD2JZSLS1DDFdtfoSyJCKdo0ks123_F2PDub-WgJoP0zWChruvYqVF-umAbj9TK11VmLfTg2MGfPfjAigARPQzl6Zj3S4IGX9tBWav23P3K0wQTSHwZRJ3TDhGsLYqjA0HZRxFYKdDPX1nQNXiNcRTHByE80TeAghkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oK4Vj_7G3-6DT9ZcrlnoH754Xx_3yzS0TmC_0rUJSOZeg2roGUf-OZUxbew60w6_WqBgu5RoVOkqK-KaZ-k9oS6Tmh9fGqz6sfr-hzdzkwQIE0htfD4DCWYWOL5zF3ttUine23XS-s8yJXSFFnGHIBnwhacMWYczv_SFE9UbP2XkCgxwkgwfKNEaU4yNy13fRKivDT-Bljpc3TDRV281qTbO3-U5DarRDxrJ5G7fpbYbHnk3y7mcMgIW46d8Ccwx7_72s1TyryTx8TwLxi43_PgmklLH0VMT8KI1DLbMPtyE7R_kvQt1Sr3x2q23MsRes3OpE1jxDeQfzMdX_sM4fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDmqLEmg4m7G4VoylKnnMxwF_Q14nbzTkT2HY4-Bmx4_CbBrEzYxLyNPbE5yDjXL4vhjalT6UQpH4Vo1H3nB_b1a-9eEfzl0F-mkjJhOvt9hGVU_97CaMzHcc0ybgO_btN8fgdm2hg0cI5qOBlgE7HCA2qDAVkY8fJyXYgjto5YODsFzOQ2nkbaYEx_ZdWyehHOjOcKnJoAm_nIl4ARzBbNvxeGaqWMgIjWUUBJrzzq-3ExcIewldANghLK12-aEMw4AhryDLbvTZLRtd0lTBYccpnXpVlXRYSgH49d1kwN7F7GnJGWyu5czKL_1NtXreuT1yr1Z27A4bEjH78h24A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569812a8b5.mp4?token=YWhtecANFouJOro7sohJ0HFFAr6tdXfR3D-0XtNLFpO5S6PMktj20gpLlYvmPZR6RauNccoLYoZjWVrupLdNaW_ow1Bczhy2DX9ZAhSJMepPeFwmQ82DMRIDp6IYlMU6dy1c__nUZbkUigWmzFUQIElgphti0vSOVkIVR_y2sjevb-DO0KMTgfYDbvTD5J65MY1L3Kq6y2QW_6dHrbSX5CrZycKqaLSAHXiRFlFjzppKOSaujKq9FTlUMVZEYjMzjLCXMTHCnnhWrd1X5BmDR1qg8TeeI_3Q5-48Sds6u3AOYcrXPJVFZEP2XVM8QSLU3SvygxlPNVeRsVOwq-Y1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569812a8b5.mp4?token=YWhtecANFouJOro7sohJ0HFFAr6tdXfR3D-0XtNLFpO5S6PMktj20gpLlYvmPZR6RauNccoLYoZjWVrupLdNaW_ow1Bczhy2DX9ZAhSJMepPeFwmQ82DMRIDp6IYlMU6dy1c__nUZbkUigWmzFUQIElgphti0vSOVkIVR_y2sjevb-DO0KMTgfYDbvTD5J65MY1L3Kq6y2QW_6dHrbSX5CrZycKqaLSAHXiRFlFjzppKOSaujKq9FTlUMVZEYjMzjLCXMTHCnnhWrd1X5BmDR1qg8TeeI_3Q5-48Sds6u3AOYcrXPJVFZEP2XVM8QSLU3SvygxlPNVeRsVOwq-Y1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به مرکز نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/143332" target="_blank">📅 14:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHtaKQnDqxpeKV6wFAFoDOkK05YBHzsQ9yxIFdeKsOznVuJgXYqJEjDkZc5vO-5CpITF3iNg3ADw4TjwCujXPiLlf1DEibgGfaWrzqOZwlWbSMvsNu_KX5SuFwprAZnH5xYFC_m5NtE3k6f_brdvWtzSlGmyzo2U0FRZ4iiQ8ANPO0i3xP8x8n6jrVeZqwkbFxEQ1doCj3NnRf75slevmCyHaLG9XbuA0lHqNuRHVG3Vg7uRIsvcxvbrdPecyl6VS3jXAWldSf8xzRQtkzH1W6n26eTmQ86XLYD5cD-Bi9CSpYJd6pTUaJhLqogBEsUjKpInsAo8ucfpsX1TdblWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر بار که صفحه رو آپدیت میکنی، دلار میره بالاتر...
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/143331" target="_blank">📅 13:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143330">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
زلنسکی: پوتین نمی‌خواهد جنگ را پایان دهد؛ او منتظر زمستان است
🔴
ولودیمیر زلنسکی رئیس جمهور اوکراین گفت: وزارت دفاع اوکراین از کسری بودجه ۲۷ میلیارد دلاری رنج می‌برد.
🔴
وی گفت: پوتین نمی‌خواهد جنگ را پایان دهد، بلکه دامنه حملات خود را گسترش می‌دهد و منتظر فرا رسیدن زمستان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/143330" target="_blank">📅 13:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سازمان هواپیمایی کشوری اعلام کرده به درخواست عمان و شرکت فلای‌دبی، ایجاد یک مسیر هوایی جدید در جنوب کشور در حال بررسی است.
🔴
هدف از این مسیر، بهبود مدیریت ترافیک هوایی، افزایش بهره‌وری شبکه پروازی و پاسخ به نیازهای عملیاتی پروازهای منطقه‌ای عنوان شده است.
🔴
این طرح در صورت اجرا می‌تواند مسیرهای عبور هوایی در جنوب ایران را گسترده‌تر و روان‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143329" target="_blank">📅 13:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23dfb6270.mp4?token=U1ohkb8P__FIw0c-41iL4I0MxefffXciJlGRvd2Ak3ijXgzejRsibUV5K60O5vYfECemFypkLmvQJPTQNboSDk9ZF2v2yhDuT9qj_3smvqBq5L0J4Wm_E53OAjRZfbcNveWokHSZLBnp6p4ntGDebyBKhmm40w_LOpdPj3IWgyZH0UJTVClxDoDaif0GrjbOvbPQ21ZlssTpNJWc4lzv3dlAMrFkgQqTtg_9K03ul-WaIpuSVuJmpothMeH1fb3NhvBTE2uwBilI0k0RSZuyEa1PkVNqE-YtFsmmitEzCqgVWLL9kkf-jYo7LZMU47x-ZsZRxGs1d1MlgkhKX0IkP57YoJc6Z484wQgJFgGYumfRpHTzjneRHua9d6uj82H4SBNbLnyQf6KUSLVoP-iT2ulyr8q5zrusenTDpEa72RLYQ2agr_-Tc8XJxF5uaL73825qptuStPRuZTOHyoPkbnF_pqtXNq1VOBsIbaXeV874rUplXS7ct0kS2NWCLEmHOiqXDH9CZ0QxoA5JW6nNn9NVj35AKfBxHbL2djT7FU7VzPhRlrWJB8UFRG6v17CwhKS3MIQh5oLSca8X_-5kPSREcWOPGmFpCAVYZ_R6VfFNqgi9YXZLiK7celXcUdn__qDOW_i1nYAze4GhTONRTImwnPZNI9hZnof_JCyCMCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23dfb6270.mp4?token=U1ohkb8P__FIw0c-41iL4I0MxefffXciJlGRvd2Ak3ijXgzejRsibUV5K60O5vYfECemFypkLmvQJPTQNboSDk9ZF2v2yhDuT9qj_3smvqBq5L0J4Wm_E53OAjRZfbcNveWokHSZLBnp6p4ntGDebyBKhmm40w_LOpdPj3IWgyZH0UJTVClxDoDaif0GrjbOvbPQ21ZlssTpNJWc4lzv3dlAMrFkgQqTtg_9K03ul-WaIpuSVuJmpothMeH1fb3NhvBTE2uwBilI0k0RSZuyEa1PkVNqE-YtFsmmitEzCqgVWLL9kkf-jYo7LZMU47x-ZsZRxGs1d1MlgkhKX0IkP57YoJc6Z484wQgJFgGYumfRpHTzjneRHua9d6uj82H4SBNbLnyQf6KUSLVoP-iT2ulyr8q5zrusenTDpEa72RLYQ2agr_-Tc8XJxF5uaL73825qptuStPRuZTOHyoPkbnF_pqtXNq1VOBsIbaXeV874rUplXS7ct0kS2NWCLEmHOiqXDH9CZ0QxoA5JW6nNn9NVj35AKfBxHbL2djT7FU7VzPhRlrWJB8UFRG6v17CwhKS3MIQh5oLSca8X_-5kPSREcWOPGmFpCAVYZ_R6VfFNqgi9YXZLiK7celXcUdn__qDOW_i1nYAze4GhTONRTImwnPZNI9hZnof_JCyCMCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید آجورلو: چین با کاهش تقاضای نفت، مانع افزایش قیمت جهانی شد
🔴
چین بر کاهش قیمت جهانی نفت موثر بود؛ چین در نظام جهانی نمی‌خواهد ساختارشکنی کند و اصلاح‌طلب است
🔴
چین می‌گوید جنگ آمریکا و ایران برایش بد نبود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/143328" target="_blank">📅 13:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نایب رئیس مجلس: هر کسی به اقتصاد ایران حمله کند، اقتصادش در منطقه هدف قرار می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/143327" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
حبس مهریه بالای ۱۴ سکه حذف شد
🔴
نماینده نجف‌آباد در مجلس اعلام کرده طرح اصلاح نحوه اجرای محکومیت‌های مالی در صحن علنی تصویب شده و بر اساس آن، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف می‌شود.
🔴
برای مهریه‌های زیر ۱۴ سکه نیز امکان اجرای حکم با استفاده از پابند الکترونیک پیش‌بینی شده است.
🔴
این مصوبه برای بررسی و تأیید نهایی به شورای نگهبان ارسال شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143326" target="_blank">📅 13:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143325">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
خبرگزاری فارس: احتمال اینکه ترامپ پوشک میپوشه وجود داره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143325" target="_blank">📅 13:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143324">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlhfs89j9or1C7zFMIBs9lfH_-3179LlYshlfnmBxIu5tYlgsMpaKXYMus1FUpkVL13zubrj96ATuS6Xg1iF-YlRTTMcp6wBjZVGC9wUIzIhZwis2YeheFc0QSvazUFJWRJf5C9RjtU_l5Wb_hmbJGqzC-5PKU0SAA_b163OS5H_EmBv-q-VQdkAQFc3Trv0vcSHqSvgRm6HPYLJknPXxesHGHTSyn4NEMJuAmEZEv5cX4qS6nw2Jl5_ErMLQLEvyeGIk8pL06eTg2jvN26CY1DAgKI_aJ1JGaRdzbtbc3RN1dSBIcu1JHVafIEaDbSawd9YH2MDXs5TvGnsUQvC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با رشد ۸ هزار واحدی به ۶ میلیون و ۷۰ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/143324" target="_blank">📅 13:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143323">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مصرف خانگی گوشت بوفالو مجاز اعلام شد!
🔴
‏مدیرکل دامپزشکی استان تهران: گوشت بوفالو از کشور هند وارد می‌شود و فرایند کشتار آن در مبدأ، تحت نظارت‌های شرعی و بهداشتی انجام می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/143323" target="_blank">📅 13:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143322">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فایننشال تایمز:شرکت‌های انرژی بریتانیا در حالت آماده‌باش قرار دارند، زیرا هکرهایی که با ایران مرتبط هستند، یک نیروگاه برق را از کار انداخته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/143322" target="_blank">📅 12:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143321">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
گزارشات از اعتصاب برخی کسبه بازار
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/143321" target="_blank">📅 12:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143320">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سعید آجورلو: آمریکا از مسیر جنوب تنگه هرمز تا روزی ۹ میلیون بشکه نفت عبور می‌دهد
🔴
مسیر جنوب تنگه هرمز همین الان دارد کار می‌کند
🔴
عمان محافظه کار است و با انگلیس، عراق و آمریکا طرف است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/143320" target="_blank">📅 12:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143319">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeTD4PTkYv_rAZhj_54QMmarqbGTA0w3wqMb_ez0tgNcDGnA358WM9_mGwpUhAJXiNfoW6dgejpeIUVZi9-GplXP6rOcp4Xct4il_HutZqUM2WMpRaOSbmhnKLLGjmeZnHNNAnuMO41sR338wV3MsoqGxXODvPWFz0qHfXPjPdVrz_ivo9gXz4c6bE74ZmihznHmpLuyolRcPrA_V6gsbHbsQNbh_k-82jNyB88nGz75izZVtXOMJDJM52GnrVvmikketqpJdjaUJlFFCNKDuiCEaE7Pekb9fzAojKxccjUQxC71xdV6-E7EWZWa1pEfvPcNOwAL_bTwhKgv3aPauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسسه HFI: بررسی ۲۱ روز اخیر نشان می‌دهد نفتکش‌ها همچنان از مسیر عمانی برای عبور از تنگه هرمز استفاده می‌کنند و ۵ میلیون بشکه نفت در روز از این مسیر عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/143319" target="_blank">📅 12:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143318">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaEw_puR_y-1qsjeKf0YZe3j0mCM-TKKU65U9BZ4Pei6SL6MVfqOZp7QVF0Oa6Z8JeWAzZnIQ8ewLPUOWoBVJzlercUzN8qT9-bpW5QaPXOtbv-EZ3ou6GC_w1a9WL8i0jMHLE5d5fBeC8SxILcwHapQEkuzFFzc9MWKuOhNJdUDdxd6ikxUhrFQMJ3V1qRbBS6kaidUVEBH8sqbSyD53f94W16NZxpSTOndqP89mMhjvgOqv3Tvlv0Dw_CEvoB6g2JCkOLXWebDAvZXy-STKBzsgwnJklOzIPtAVmlx2eWVLFs-vXutSwDAfNX3cOsUAdXJ7MJHI6hcCR7P78QydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران و روسیه در آستانه امضای توافق‌نامه‌ای برای اجرای پروژه ساخت خط راه‌آهن رشت-آستارا توسط جمهوری آذربایجان هستند. این پروژه، یکی از پروژه‌های کلیدی کریدور حمل‌ونقل شمال-جنوب بین‌المللی است. طبق گزارش خبرگزاری ایرنا، انتظار می‌رود که نمایندگان تهران و مسکو به زودی این سند را امضا کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143318" target="_blank">📅 12:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143317">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_Aee3PzPhgaeeZ4WXpb0VuDEHaY5RGB7kedBzi9f__y36sjE6OanxmCGPDleiE31zNE1IjtMFM1Jmz0qycsz_EjLPTDRi0C1pwFPRiUKFxq3tB1Gj-jwyttDPkMX3LcP-ywTTvylbFgiiUJLn1zu8YvK-_YW2As6AMtKA8-bgBe3UxETGQejlAHRIbOSGXGfME_3y-zj6HX-YXFEW_xvnTAg9dtrrZoUrvrB5oTzJEXYr_aoCPttolH-CCMgT8tSTAy0a28iVT9LxslTf9vWvudIU3zewjyJK_aGS1Pu7L_wyhxYH7o6pHE2UZ-_ulJTei3EQ5nEHwfJmDzeLP5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات ارتش اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143317" target="_blank">📅 12:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143316">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
عوستاد خوش چشم: اگه بخوایم توانایی ساخت گروه نیابتی تو آمریکا رو داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143316" target="_blank">📅 12:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143315">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558651d0c3.mp4?token=N8SfQzlTH7O4QSBH6CaK26dEDCvzGGJxmNCBx5fOngdySfTlTLpMofHOfBXQsgiegtrNtLQPcnA_cGUmlmaDF_G-R4sDojmD4v_U8trn-LVYPhsm-2NjSw3w9_ZQsMYZlFiVbSXCthHFAcPU6_gzf1g_Ce2T8DsAXhvSlpMv25CsAmVtzVnmgxKhydC6z3mc-THQOFytqVCBkMqIrpJGn7BAxqjrIBPw8EJ2uiQ3HHCh1YuDSOJvttqDruW7pa9Dr9zCSHsuV3OHhTd6SBR3olkuwe95n1LuTmmenf-F8OmHgTUUIX2doElvZJMaFUsIbc3APIBeH-3TdZ4_mra5WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558651d0c3.mp4?token=N8SfQzlTH7O4QSBH6CaK26dEDCvzGGJxmNCBx5fOngdySfTlTLpMofHOfBXQsgiegtrNtLQPcnA_cGUmlmaDF_G-R4sDojmD4v_U8trn-LVYPhsm-2NjSw3w9_ZQsMYZlFiVbSXCthHFAcPU6_gzf1g_Ce2T8DsAXhvSlpMv25CsAmVtzVnmgxKhydC6z3mc-THQOFytqVCBkMqIrpJGn7BAxqjrIBPw8EJ2uiQ3HHCh1YuDSOJvttqDruW7pa9Dr9zCSHsuV3OHhTd6SBR3olkuwe95n1LuTmmenf-F8OmHgTUUIX2doElvZJMaFUsIbc3APIBeH-3TdZ4_mra5WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی جنجالی صداوسیما؛ نقشه ترور بارون ترامپ!
🔴
صداوسیما در اقدامی بی‌سابقه، اطلاعات محرمانه و مکان‌های دقیق تردد پسر ترامپ و نقاطی که در تیررس است را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/143315" target="_blank">📅 12:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143314">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7qcgbVLKserbo1YEBqEiN3zmKZ3wm6qllTfvpW1BdCGUGxQImXGN2g65qJZtFMqyThIsJy6WH41Zss3c2zbu_ViuXIEUgBB9T2H1-VbSmXJgcwwmZVhbYLgCjAEGhWJN4sz019_-IN5xF5Pmphti1v-4IUstTdOPIu_OUGvIhUcLxBwMSo4D_6YVwueljc57Kidab_1UuM0Tod-guJeaaNOE68dMfTU-A8r1rxAVpgFu87vwThhdEScWnWykfNpg-7bXfxhaFXDF4lzgXhiyiv6Ruu1689MZLSKCTSlW9YbBuUBwp9RLifoFXrGSNzplxcw2iC9i8MKqBX3UKBMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک‌تایمز: نخست‌وزیر کانادا مقابل ترامپ ایستاد/ تداوم روند کاهش وابستگی به آمریکا
🔴
نیویورک‌تایمز در گزارشی نوشت: نخست‌وزیر کانادا در حالی از ادامه مذاکرات صرف‌نظر کرد که کمتر از یک ساعت تا ضرب‌الاجل اعمال تعرفه‌های جدید آمریکا باقی مانده بود.
🔴
پس از اعمال تعرفه ۵۰ درصدی آمریکا بر ۲۰ میلیارد دلار از کالاهای کانادایی، او نیز از اعمال تعرفه‌های تلافی‌جویانه «دلار مقابل دلار» خبر داد.
🔴
کارنی با این تصمیم مسیری متفاوت از دیگر متحدان اصلی آمریکا در پیش گرفته و حاضر نشده توافقی را بپذیرد که تعرفه‌ها را به‌طور دائمی وارد روابط تجاری دو کشور می‌کند.
🔴
او همچنین تأکید کرده کانادا در حال کاهش وابستگی خود به آمریکا است و این روند را ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/143314" target="_blank">📅 12:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143313">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=nAva8siPwPrdvMgljeH0bO_IC3Yi_BBov_OXfJTfRUQ1XsEO363L3mUnZJdRVCGmxFYf4yKHTLqvRWy-wLsrVv-J1M8lR6e0d08nDhaRQuxNMskf0rwicP2-ygiQs283-zaKvcaI8YmXOnIvoe7qxAgHWMtTMKHC5IocvX4Z1mgAJWZTO-Acc2wjFIlXQK_muX6DHXfZcmEfYzBDNCxqDsg8QApJ1HnvWwR5ivxgnaoI1yKsQfYNzUahRf_oH4pemdskzMjXnoldJdZvCuG3_UM439PEuAGAUHbp3-NeVZ8Z2Sn6cIDSE4a5U6FLi1vbvQ8sQSNW4zz0gPGD87CkTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=nAva8siPwPrdvMgljeH0bO_IC3Yi_BBov_OXfJTfRUQ1XsEO363L3mUnZJdRVCGmxFYf4yKHTLqvRWy-wLsrVv-J1M8lR6e0d08nDhaRQuxNMskf0rwicP2-ygiQs283-zaKvcaI8YmXOnIvoe7qxAgHWMtTMKHC5IocvX4Z1mgAJWZTO-Acc2wjFIlXQK_muX6DHXfZcmEfYzBDNCxqDsg8QApJ1HnvWwR5ivxgnaoI1yKsQfYNzUahRf_oH4pemdskzMjXnoldJdZvCuG3_UM439PEuAGAUHbp3-NeVZ8Z2Sn6cIDSE4a5U6FLi1vbvQ8sQSNW4zz0gPGD87CkTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر گرم طلا در آستانه 22میلیون تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/143313" target="_blank">📅 12:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143312">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=EI7GGwFH5v15MJtMXmGGEVsnuH5zn8TbaDWIv9ehIk2pVfUiRC18VARzNdWiUyL9IxhKbICzwtakhAz3ujIID2ckUHCbBQZ30-0Es-GiozFGSqUMcCOxu1ybMBLmlg_lWqah2XhPk99N9xBUPbII6xQLzTd6H424iZ1LJpySz8LxZyRWbVtE7uKZ-Yft_uWg8mEsI2rTJ2lzIFRfX4cPkz54UAOxqELNLmE4KFh5t8lRRUoODC0e4jU9ybwbW0TTfIj1SspDVPI-azRG9N1XHZtAYIlr-DgFRJz17ywon2Az1NhQ2fM-Cmf_8CtIe5MdKkcPriRA1eFrjhmfM4og_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=EI7GGwFH5v15MJtMXmGGEVsnuH5zn8TbaDWIv9ehIk2pVfUiRC18VARzNdWiUyL9IxhKbICzwtakhAz3ujIID2ckUHCbBQZ30-0Es-GiozFGSqUMcCOxu1ybMBLmlg_lWqah2XhPk99N9xBUPbII6xQLzTd6H424iZ1LJpySz8LxZyRWbVtE7uKZ-Yft_uWg8mEsI2rTJ2lzIFRfX4cPkz54UAOxqELNLmE4KFh5t8lRRUoODC0e4jU9ybwbW0TTfIj1SspDVPI-azRG9N1XHZtAYIlr-DgFRJz17ywon2Az1NhQ2fM-Cmf_8CtIe5MdKkcPriRA1eFrjhmfM4og_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 198هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/143312" target="_blank">📅 12:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8loA-qecLRRMGWIw_ANGVlb-KbqNuv266XuDS7Ls--0wtKnsyfEsA3cIfaHazn5fHjUjN49WT_E9yzDyg2Z5BauEq7E--VFCFIKfVnLalZ7UNzazvy7BnrV7Q_-0sVc8HyAPJo4lC58moFXn95sD7MutPMcXKTs8AjANrM3v4B74-HBUP8XEew-_JLBhVWs6K0zswQKGa5XWUwTeMZ5q-hN2paQOlv9hGfLpiAp0eMrv2Kxk0VBoVC1eiyth7Wvyg9Nh0hsRhF5f4JA3icRZN2QN89l72p0b7iH0_u-wdy2hDMdtOWrgog9TV73F6ACvtP94WdM9t8a5-YASJHUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMtelmVaOmO4GjjgbrUUoebSgQSw8-WG_1S2Ho9jFcd7-jP3Hp_5VYqGrDm1UlPo9q59n8uDy2-64XixPExPq8uBk6SNs8HzMLcPJrxhVwIUNBxq2N2STL3o3LGUh3gauMESxirVEaJ8A7Mrl02h9NXE5qrSNNANECtc2p-SNoZ7WT1OiW40yVXW5GpqwOlI9hrV-IIsGGUQ7rdq5aqu459ylj03Fb_R6YcfFipeMqmVMuuGvAzxLnpbbVZal44j45ZKQZpbZoIXFTXWOh901OutLnKQ0VaK6y1YFB9fhnyXqWcE0BlU-UgmdtIHg44AX61k9vxwfz_9EBptCJW_aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در طول شب، نیروهای اوکراینی به یک مرکز لجستیکی در کلپینو، سن پترزبورگ حمله کردند.
🔴
بر اساس گزارش وزارت بحران‌های فوری روسیه، آتشی در ۸۲,۰۰۰ متر مربع از انبار ۶۸۰ در ۱۲۰ متری رخ داد. همچنین سیستم FIRMS ناسا نیز نقاط داغ بزرگ آتش در این مجموعه را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/143310" target="_blank">📅 12:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
زلنسکی هشدار داد که برگزاری انتخابات در دوران جنگ کشور را از هم می‌پاشد و آن را یک «تسونامی» بالقوه برای دولت می‌نامد.
🔴
هیچ شریک غربی تضمین‌های امنیتی مشخصی برای برگزاری انتخابات امن در سراسر کشور ارائه نکرده است.
🔴
این بیانیه زمانی مطرح شد که فدرور، وزیر دفاع سابق، به‌طور عمومی خواستار برگزاری انتخابات شد و استدلال کرد که دموکراسی «نمی‌تواند گروگان روسیه باشد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/143308" target="_blank">📅 12:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">تو ایران حتی نمیشه مُرد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/143307" target="_blank">📅 11:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/143306" target="_blank">📅 11:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143305">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
قیمت هر سکه طلا با افزایش ۸ میلیون تومانی نسبت به روز گذشته به بیش از ۲۱۷ میلیون تومان رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/143305" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143304">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a338f70a64.mp4?token=dxEp_rInFA8xOPnhnYJa-Y6dlrKWl8bopsKVNokCLrsDXa87urrG7gpXqunvbtSjJf6ThP1ZilvMEmmR9YTtoQMKcFcVYQhQTcbEbACzVnH3N4y4tNhmcRvwqrJ3hUC69YMco-CxmyAEoxes5fE40V4EMAQdDweUSjPk2AataSNc1cZtX5QJQxIfAWBAwF9vAVjrXT63pZ_AXWFlFj2E3xa-eBldf33_--HibgukGGO4aMeEt-FDzucgO11T3HHyN2Ae_5HjeUuJqzBRwSYZwhREbHKaLxxsngh-9rnA7kEQf7pIhA16QsuJjju92D-j0dNjJO9pYVxrPiQ_QtchsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a338f70a64.mp4?token=dxEp_rInFA8xOPnhnYJa-Y6dlrKWl8bopsKVNokCLrsDXa87urrG7gpXqunvbtSjJf6ThP1ZilvMEmmR9YTtoQMKcFcVYQhQTcbEbACzVnH3N4y4tNhmcRvwqrJ3hUC69YMco-CxmyAEoxes5fE40V4EMAQdDweUSjPk2AataSNc1cZtX5QJQxIfAWBAwF9vAVjrXT63pZ_AXWFlFj2E3xa-eBldf33_--HibgukGGO4aMeEt-FDzucgO11T3HHyN2Ae_5HjeUuJqzBRwSYZwhREbHKaLxxsngh-9rnA7kEQf7pIhA16QsuJjju92D-j0dNjJO9pYVxrPiQ_QtchsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده‌ای موسوم به «هاوک» که در کوهپایه‌های شمال شهر «رینو» در ایالت نوادای آمریکا شعله‌ور شده، تا ساعاتی پیش بیش از چهار هزار هکتار را سوزانده و همچنان در حال گسترش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143304" target="_blank">📅 11:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr_TecFvid0xfxkDi-OyGN3ZVepbPWLiP5LPeapU8jsCjU7LOeBn9PUZkfaEYfdg351vO5QzXLt5JpI2VIaixomYyf_UiAB-y6eCp4IwdqbaCEJlCOcXtdzN5WoJh_lvtupAEYkEh5zvPsQ8F9bgr2iGU4Q6qGoahuNZ_tZKhf96ObrDyKBFP_a3QxSZzjNbHaK7HbX2JzB1rUGRur8aRa3fJ0JnujBdATZEAleoM3D-mZk_PrCTZGCDIk7C1SbxvvC3yXyaYX7jTJ6iut93YD3sKLuThUu-BKZamKVm0Zz60EHPEa6WLtLS9jLDHLa0MA7f-yqrK75C9Jxqi1W6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
مشاهده دایناسور در مناطق بیابانی خراسان رضوی تکذیب شد
‏
🔴
دبیر شورای اطلاع رسانی اداره کل حفاظت محیط زیست خراسان رضوی:طی روزهای اخیر تصویری در شبکه‌های اجتماعی دست ‌به‌ دست می‌شود که موجودی شبیه دایناسور را در محیطی بیابانی در شهرستان بینالود نشان می‌دهد.
‏
🔴
تصویر مذکور کاملاً مصنوعی، تولید شده توسط هوش مصنوعی و فاقد هرگونه واقعیت میدانی است.
‏
🔴
هیچ گزارش رسمی، مستند یا مشاهده میدانی از سوی محیط‌بانان، کارشناسان و نیروهای حفاظتی این اداره کل مبنی بر وجود چنین موجودی در طبیعت استان وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/143303" target="_blank">📅 11:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خبرگزاری فرانسه: ۳۳ هزار مورد مرگ اضافی یا مرگ‌هایی که مستقیما با گرما ارتباط داشته‌اند، تنها در هشت کشور آلمان، اتریش، بلژیک، بریتانیا، فرانسه، هلند، پرتغال و اسپانیا ثبت شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/143302" target="_blank">📅 11:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d7bcbd95.mp4?token=KdYsdVEjUlaAUzlUiKbu4QGp4_qB-krLQUcaIZXMa8xqdlXpCl-cPbzr-MLNN3Y-SGENZUdMMbrthamE9qR6F1cQj9EtWPgDY8-zts71DToUSAXxiWQM3igVkEW9mZhjh35uHoWJSfYvuNkglJfKvboOjTaP0qPMd9FFvunKTOwu1JxOP9BPnS1IxS5GyDFl77IcFZ8qracIyO2qQj3TE5VgdQPr2NMuz2lhTF7fu-o3Ut_1I4k9U1qTTwypPbyxae1qPrjUFCwxyLylPWgC1Uw3x8Jcw2fhHtnj42xjv72QVp8FUrBwDE5TEKKiQodEPvtDxTQ_eocZ6n5dqaQuHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d7bcbd95.mp4?token=KdYsdVEjUlaAUzlUiKbu4QGp4_qB-krLQUcaIZXMa8xqdlXpCl-cPbzr-MLNN3Y-SGENZUdMMbrthamE9qR6F1cQj9EtWPgDY8-zts71DToUSAXxiWQM3igVkEW9mZhjh35uHoWJSfYvuNkglJfKvboOjTaP0qPMd9FFvunKTOwu1JxOP9BPnS1IxS5GyDFl77IcFZ8qracIyO2qQj3TE5VgdQPr2NMuz2lhTF7fu-o3Ut_1I4k9U1qTTwypPbyxae1qPrjUFCwxyLylPWgC1Uw3x8Jcw2fhHtnj42xjv72QVp8FUrBwDE5TEKKiQodEPvtDxTQ_eocZ6n5dqaQuHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آناتولی: طوفان از روز جمعه در این نواحی شدت گرفت و سرعت تندبادها در «فورلی» به حدود ۱۲۰ کیلومتر در ساعت رسید.
🔴
تصاویر ویدئویی نشان می‌دهد که هواپیماها در اثر تندبادهای شدید از محوطه فرودگاه رانده و سپس واژگون می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143301" target="_blank">📅 11:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: فیلد مارشال عاصم منیر روز دوشنبه در راس یک هیات رسمی به تهران سفر خواهد کرد
🔴
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و نیز ادامه مساعی جمیله پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد.
🔴
عاصم منیر در…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/143300" target="_blank">📅 11:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر امور خارجه سوریه:پیش‌بینی می‌کنم که به زودی مذاکرات با اسرائیل در مورد یک توافق امنیتی از سر گرفته شود. ما دست دوستی دراز می‌کنیم و از اسرائیل می‌خواهیم که از این فرصت تاریخی استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143299" target="_blank">📅 11:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رئیس کمیسیون فناوری اطلاعات و ارتباطات اتاق بازرگانی ایران: ارزیابی معماری زیرساختی شبکه پس از تجربه قطعی اینترنت بین‌الملل ضروری است.
🔴
دولت انگیزه رفع فیلترینگ را دارد، اما این موضوع باید با بررسی همه جوانب و رعایت شرایط موجود دنبال شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143298" target="_blank">📅 11:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
دلار هم اکنون 198,450 تومان ...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143297" target="_blank">📅 10:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: فیلد مارشال عاصم منیر روز دوشنبه در راس یک هیات رسمی به تهران سفر خواهد کرد
🔴
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و نیز ادامه مساعی جمیله پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد.
🔴
عاصم منیر در این سفر با مقام‌های ارشد ایران دیدار و گفتگو خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/143296" target="_blank">📅 10:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0a5G_AxQutR9p8Q00cABtWrHVEgGiAeJtpgAX5KK3muChxlBcafUsZaqBibiSxM-QeO1rD48DvFSLuIjNNtmfpfDaPatcMdMfH_STb-tocEyS81gLzAKobhfvy0CRUGtn-WO2U1fR2kepd3jeVugkqu52c6w0tFkBsqlYTPY1mN1mlNjgDSUk55LCQ-OqXFHUD8keZZ53_EAcssyXCYRNOObCSkVVwa3H6l_Z1b72xQr_gJX6hU_-Jrugaiy5-mzOEw20B-5gL55XDVJwxEhWuuU6ISE9ZANqthslUTqT2SUtXHTHBBnb1UBOtbsVw2JlSbP5PbLHncslA4s8lRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده مجلس: اگر وزیر پیشنهادی اطلاعات، برنامه ای برای انتقام ارائه ندهد، به او رای اعتماد نمی دهیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143295" target="_blank">📅 10:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
واکنش مردم به خودروهای برخی گردشگران عراقی، بار دیگر فاصله بازار خودروی ایران با بازارهای جهانی را برجسته کرده است.
🔴
محدودیت واردات، هزینه بالای ورود خودرو و پایین‌تر بودن قدرت خرید مردم باعث شده خودروهایی که در بسیاری از کشورها معمولی هستند، در ایران لوکس و دور از دسترس به نظر برسند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143294" target="_blank">📅 10:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHlghNUJMUUZVuXowOzWla9uP8bA6OBUsfPywYo2NcPYhrCO7gm4oHjRcTFKTTACMFZpF2Kque495kjzEr1HO4tIsqrFSi6nJxi57dNzj47z5Nx_C6RoO0nUkQ-nbshA8YJNDUvQoQe7mlRJOEVOFZ2_tSg32WLBpmRqs9kiC9LK2v6kNRCeZCBdNqa-iaI_pUQ-9W8i1wEVZlsVBgRsgtH2lG9Yr-Ry7zufL6Y7Umt7tOUBXyyfm8O_RQ5qPCdQ0xvu0JE2ToPNjkTlmNy3pt0BuKwO5-mKbPWp9Mk87RBiEYj_djCnqx6i58hNsmX7w5xHEBN1HjqGJhThU3rcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بامداد امروز یک شهریور، کارخانه‌ نوشابه‌سازی ایرانشهر طی حادثه‌ای در آتش سوخت.
🔴
هنوز از میزان خسارت‌های مالی اطلاعات دقیقی منتشر نشده است.
🔴
مسئولین این واحد تولیدی در حال پیگیری این ماجرا هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143293" target="_blank">📅 10:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBzdC7J62YSfKJUZqP4nfOAYwEK90MEinSBio9ThoxjChQGUoJJ99pbxGvwrTtjyK2bDpPHkjG9OEAj9T4_16sHCH-jkgEsA6dQ67RygC250gTyFit4Ipmzhse6O6JMAFcevWg3cEqMOFM5sY87UvHt_QYWzrhiCCc9o8Z08PUgSb8fCfvyjMH6PYO400ghd-pDevXi5_a1jEMS2zajNSw36uW_B2eWEdhdIfXlHjavKUjwG6uWTUx_i_it-N6ZBNC0GOOSbNWU8JJ57ujUrF2mQ98ufnaTl2_zIlFzgOSsvYsQHbqBZpO2fIPpPm3wbFPhBSnwGZ1NknD5NuWTMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rHx8eHdPNS-aVYPgKBmDRgtQVVXe5CQnLWoEY3UNcYM9uwwunJhhTWU5gbgJRws1e7n7ZHqZFl8NuR32NkQkYsd4JgZhdpNwlhtV_qlHFtimneAdiKBNtN_F-hIwTQ7sWOqFKfBdFwizF-Wd1bzRlpvs-xhDAOhDuhVulGIElF6luy0agRjxXqSNRRDW3Zsr4cUwk5077pnzWaAGAaL9gB_uzz645hvAGPJCxc7bLB8xbfVtAdh1rBekEIrl8M5aP3IzwSRmJPH0LglS8RGGjlaDOsGi2piFApsBcv00JA2uF4laSOr2H6S8Y-gaiBs6DBti3OPXdBckwxq2dNoQNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
۲۵۶ میلیون دلار خط تولید BYD یکی از بهترین خودروسازان دنیا راه‌اندازی میشه ولی اینجا ۶ میلیارد دلار به ... میدن بره زباله‌های MVM رو بیاره چند برابر قیمت به مردم بیچاره بفروشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143290" target="_blank">📅 10:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نماینده مجلس: امارات باید سرزمینش را بابت خسارت در اختیار ایران قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143289" target="_blank">📅 10:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoThCTQ9arsmX7s5FXA14Mq791GoDOMOQ0-tSuy0aIiCepUxHgvZqNLvpglvjSC4C_ISHii10siKvOrA1tzzDH16PPBzJEdFJPEpEdlyJ8icZAwokWEgJsM_AJyzyUq4_xmz178xO_afhRn4F1N6tpLzSn1M9Eadl2gOFtjKIBezt-YpDtPd5Us5rzJ6nfDtNmPZLuatJWlhKUkamENj1qRPBSlAN2GuSe8ckFz-wuOD_bOOQGkMJt1B3hhHu97gCxhjy8qbzXtmSBUhqELGh0jHfy42tB0k57b5jCTzB2B2XtOHVt8S47_6V-ef810dikkv65-RQUN349yHX7Ww-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه تلگراف بریتانیا: هکرهای ایرانی یک حمله سایبری بی‌سابقه به یک نیروگاه در بریتانیا انجام دادند که منجر به از کار افتادن آن به مدت ۴ روز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143288" target="_blank">📅 10:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhoRpqfBpBlw1QQFh2I22Jsqr-suFeSP9AIRGxHvDe4ZQZaXAKYi1EKslZRZb37lgAARO0h6FD26K55ieNhGTSfxSMV0OSo3O-GO1AS2A8o5gEZ-Mc_kU-dqJrrtF3QI2jNwfldowgRxDPQQFj816ssNK1HVs9TTTzltGU1oyH5acgvuz4FAEYZkbgU7oJNJdyQyiqtq6Ge_KWvgifOVEFlulehibm4b6nQ-k5oJHdigVdlFSDnlZmRyR7sh4acTuV3LHJ5WxZRn2CI7YvAogTzOE8isHSz9sP7DPEEblFOA1PGaGkKSiDXQ82XTAJqJZ09LYpDvFsxQ6WKNZqRnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
علی قلهکی: تصمیمِ فعلی دولت بر «عدم تغییر قیمت بنزین تا آخر سال» در ازای « تغییر در میزان سهمیه بنزین هر ایرانی» متمرکز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143287" target="_blank">📅 10:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaiaI9ZNNIUfTfPmHpu8cDlibpa7Tq6NFW6tAnOAGa_Xasx6hxkAnv0v3GUxPWsaOz8rPaN-ku_i7nPnkY34KFzE3YmDlmOWIUKxbLhJyrKpCRP-o6KS0ZoSNMAwDC_SJxikSjcujjC-hWv1TJ26T26a665kFISLApaBMglP5zF05qaaEeBmUzm4Fc82GnvWBi2H5tF5pdyBpE863uQcBBBDxgxrAi1ctiINRkP_HtGz7DgufcD2ZOc94uYLbDZqV58_Hws6qrU-u32G5XqPe5F-F78F5cC73PJi7swJ2-hR43kprufqKhlCsi4zzhEAblRMvYf0O62pc_vOy_5Izg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی که به نام چین ثبت شده بود، از امارات متحده عربی به سمت ایران در حرکت بود و از تنگه هرمز با استفاده از مسیر تعیین‌شده توسط ایران عبور کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143286" target="_blank">📅 10:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سپاه اصفهان : احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و مناطق اطراف تا ساعت ۱۳ امروز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/143285" target="_blank">📅 10:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
به اعتقاد کانال ۱۲ تلویزیون اسرائیل، ترامپ سبب شده است تا فرصت چندانی برای عربستانی‌ها باقی نماند.
🔴
چه ترامپ این موضوع را درک کند و چه نکند، استراتژی او مبنی بر فرسایش، کار را برای متحدانش در منطقه دشوار می‌کند.
🔴
عربستان سعودی ممکن است تحت فشارهای رو به افزایش اقتصادی و امنیتی، به دنبال دستیابی به توافقی با تهران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143284" target="_blank">📅 09:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e169546d5.mp4?token=HlGpkBdPYvSHrYhbL-b-tnolnVDISy9zefKVLlf8_Lmmq9d1yJxKufZKtP_1yM-y1PVOadc0qvoVTYdaLhevioy9MgRSlLaoK8Kgm2zGr2NrZ-bhpmeMZKN7BSZabrm8UwtlOL6qSbbHxSiPT8X0HC5yXgBxFg2hCZrf8bUaATtxx6AGDtr1YbaU7vhJnzJvZLs1Ae51BsLLJd7RIbxVHkfq0yi8TXQS8qW9-TRgT9VtXAOMJyEJYZl3dtqD8FrtbrezWMt-xvZZVQDXAvM44x-IHJMUGIMxUHHjip5Z7nMsvROLvt_1z5r7OIy9_BhdfTijAMZyZpLMjYYQ4AcQTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e169546d5.mp4?token=HlGpkBdPYvSHrYhbL-b-tnolnVDISy9zefKVLlf8_Lmmq9d1yJxKufZKtP_1yM-y1PVOadc0qvoVTYdaLhevioy9MgRSlLaoK8Kgm2zGr2NrZ-bhpmeMZKN7BSZabrm8UwtlOL6qSbbHxSiPT8X0HC5yXgBxFg2hCZrf8bUaATtxx6AGDtr1YbaU7vhJnzJvZLs1Ae51BsLLJd7RIbxVHkfq0yi8TXQS8qW9-TRgT9VtXAOMJyEJYZl3dtqD8FrtbrezWMt-xvZZVQDXAvM44x-IHJMUGIMxUHHjip5Z7nMsvROLvt_1z5r7OIy9_BhdfTijAMZyZpLMjYYQ4AcQTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: کنار گود ایستادن و حرف زدن خیلی راحت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143283" target="_blank">📅 09:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN4FLG5MuU-wEVaXxwEyNWRVHFpbPkOEtrH_HN-Y5QRb2aYzMPazkYHKZ_AXHWfB-pUs66IvgNo2-cwYxa5er5jqNKuuuZ6pABPDBBuag9ME5adezcJyEpAFdMGKk0btVs54wecR8mpQ0ghjRjPpCbUGR0zcMfKRqrJoKBCBR_M-Q4f6AKkX8WwnJbvzjnX7_HS_0Ch-i1cPVnls6wf9MLGTM8_xAXvIqTPjjyPeu4zEXUxFrFlOATu5sC1SnLxRpQfvkGoDncdiLprNN8saFNSMCiUCpBIic3maMu4yiUzrDjW3idML2OXQbalmEygWvblVKo9tlQkKP4VRyYfjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست: در هفته گذشته حدود ۲۰۰ کشتی از تنگه هرمز عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143282" target="_blank">📅 09:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2_Id-ZLSRVyACFDRGt7JDAPTie5QQPzrkaatBItLOWXwMRroQ-OIhr2oN-A19QcoUcZRkD4hZ7CrQSi1pFAH29uVSEIXaid-UDaZx969WQWy4uxO7ym3VClBpas9DFhe3V8TugVOfaBPuhyw5E8TZ-wwnMWuVLc-gOoHRI8zVLgNzS9iBy8ebqDNozjgY4QpBZeyTz2DdNCF-CDsNbFQLa8Mg8J39z6XSB6nfXfKwd3SOFaUzsCUT3GcJ_egVFT08dAHlewCcv47AxFatPrNToD_yxKrr-bOPtqNPZUt_ByHoF8SsF-hkp6qUsc4BakuYeGXBkYkI-vMdcii4OTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، یک مطلب را دوباره منتشر کرد: ما بیش از ۱۰۰۰ کشتی را از تنگه هرمز عبور داده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143281" target="_blank">📅 09:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFjrNd-Wh2qXnLg95qahsFLeioMDB-gQztXTVWBU5ci8kR7ngaRKF-S7YApWNg6KoAxSoe0_BmPMgrtThkSa_ioHw_pv5E2MdZhilv0WiSzRLtqYReVNZkh3BZnrofaa3DyMOiG749YRAtt8LjFMI6Q9FTdzt3wSpIRtYQ0PsGzSZj91LYo9VBVqBlOVHgMEnlcj9laI47Csaa3ivTClkeyvbGvvyLwDE03g3f_R6j32vYYTlHdtk1v1GioGDw9FQ5L9AkKa9HqeBiJa6gkfb0squt9kiZp2PtBzf20fxuKx3GoFdTXCOMJlGMcEax_5G2y_hNsDGcpLtKj067zEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش الجزیره، انتظار می‌رود اسیم منیر، رئیس ستاد ارتش پاکستان و فیلدمارشال، در چند روز آینده به تهران بازگردد.
🔴
هدف از این سفر، احیای تلاش‌های میانجی‌گری پاکستان میان ایالات متحده و ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143280" target="_blank">📅 09:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سی‌ان‌ان: عبور چراغ‌خاموش برخی نفتکش‌‌های اعراب از تنگه با اسکورت آمریکا
🔴
سی‌ان‌ان‌ مدعی شد: با کمک نیروی دریایی آمریکا، شرکت‌های نفتی عربستان سعودی، کویت، قطر و امارات، نفتکش‌هایی را اجاره کرده‌اند که فرستنده‌های خود را خاموش می‌کنند و نفت را از خلیج فارس، از طریق تنگه هرمز، به دریای عمان منتقل می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/143279" target="_blank">📅 09:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نماینده آمریکا در امور سوریه: حمله اسرائیل به پایگاه هوایی «ابوالظهور» در سوریه، ممکن است اقدامی برای «تحریک ترکیه» باشد؛ این بخش جدی و نگران‌ کننده ماجرا است
🔴
نماینده ویژه آمریکا در امور سوریه گفت اسرائیل پیش از حمله اخیر به یک پایگاه هوایی در شمال سوریه، واشنگتن را از این حمله مطلع نکرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/143278" target="_blank">📅 09:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ff2cc3a8.mp4?token=CECq4xKpCcwhxOvKJluzRWtDwg81VIhT-S1meliXnNDZOfwj5hBy6de2x3U-9vJBL86Er31ug9h1RB-wG0hU_sIAKiuwie_0k-2HzyRo8L9CllOBczDX32hFHam3ZjmFjGU2K406V0mq_74r1tUiEkRke95-ULIx42VhtS64Q6yNF8XBE1b0P1w1Lyn8k3-ZjN_FjBSMUE6uuDCZlikNtzZ1fQhULed9p4-Z9Y8XfVbjOOCwpVTh6cGiHuZ9b5u1JkKxVRwy54hAICwHyBvtavwCfOv55BoNGMI3ZYwqoZjvM1DzLyhVSZfS_Ehg838bFYxTgibyxIdkvdA5egkZrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ff2cc3a8.mp4?token=CECq4xKpCcwhxOvKJluzRWtDwg81VIhT-S1meliXnNDZOfwj5hBy6de2x3U-9vJBL86Er31ug9h1RB-wG0hU_sIAKiuwie_0k-2HzyRo8L9CllOBczDX32hFHam3ZjmFjGU2K406V0mq_74r1tUiEkRke95-ULIx42VhtS64Q6yNF8XBE1b0P1w1Lyn8k3-ZjN_FjBSMUE6uuDCZlikNtzZ1fQhULed9p4-Z9Y8XfVbjOOCwpVTh6cGiHuZ9b5u1JkKxVRwy54hAICwHyBvtavwCfOv55BoNGMI3ZYwqoZjvM1DzLyhVSZfS_Ehg838bFYxTgibyxIdkvdA5egkZrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: وقتی تصمیم گرفتیم و تفاهم کردیم، همه باید پشت سر آن بایستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/143277" target="_blank">📅 08:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV1M-p6UQCtTTc_nyv9fDRdxPn96pIdSeJnqAjoi9NIyUSydWo9kl1MW2u1XKljO2_5Y-AmpVGVVUei7eo_azxWQW6othmvPnYNio516C-enSuXLAiMu8LusoOX8cjDtmH1iobZ3dfgI_I0JWW5gmQb8cZbkEDe7eDIZ9-WTJSMx4YtYqZxGKUz6AA4lwkn5bMsi5sqnC5cLaTLTTHZOamehnMu_1bWqWZI0fpjCp3tPAlZach9iZRqLgcAkwJofn_QaHY5xL5ZF3BpW6ow64You55eqwqM3lRVMXVRMUEMdQGWfBF8EXIispB_OWmcXzXR6wpK4Dm5f4gBwaWehsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:  «کانادا می‌خواهد از مزایای یک ایالت بودن بهره‌مند شود، بدون اینکه یکی از آن‌ها باشد!!! آن‌ها همچنین برای سالیان متمادی، مقادیر زیادی تعرفه از کشاورزان بزرگ ما دریافت کرده‌اند.
دیگر بس است!!!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/143276" target="_blank">📅 08:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e8b6d915.mp4?token=n3veBSrZW53lg9yrYsRNsNLyRjWlheVVXXmxMnkTa7AQo32EDa0cvCPt2fzUNWOBBrfCLPLomU86XLIaASVP45pGDmXlkx3Z45d3aBp59D5xbmzUZyire5aTbJGm4q5F0Lzzn_hszBFGUrNbvglF2RKunjkxZVQeY5F3bknBvdRiDGdEhQ81RPpl2qWVVXVapGrlS-Azv2HaZkaGd-JtfKcN_bg5g2BsoSCws8skH1RAEN1rvolYh9oGe4WDhnQwcicu2XGT371KHHigFmn_TjDNBAO0AgmNDmtXrIQSkq1NSfCUVwQnaxre99nVgOq7kEhH6eEWRSHc8UKosa2osCtRMuGCRwgyuI1f59gaVvBVQ8fNzTdtPclhV60dNUYl1ge-eAtY75ojzoa_QSvFOhDA3_qfXH8LYBruSHeS4tVsJTg_iT2HsR-OYtOOtLv4GiH_6nJ-INMKMOtNe6_7iMZOCZIChSBfiY-HfH9DrRLSjuZQ-HdEs_6_mWbGW43OYNIm-IrClphVVF0TV5napW6NpdqyUbT8aLtRU5PDLkOLtRGFez6KbvPp35pAXua797x1XYinsT9hQGRjKaf83nuGDUj45Se-Zd9gTOgoZ-EWb7RHNB4AmNVx9C368S7kADxoCNvutu-cN1l4XmHkWwhQzX_Hv0IyuQRmL8bGTFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e8b6d915.mp4?token=n3veBSrZW53lg9yrYsRNsNLyRjWlheVVXXmxMnkTa7AQo32EDa0cvCPt2fzUNWOBBrfCLPLomU86XLIaASVP45pGDmXlkx3Z45d3aBp59D5xbmzUZyire5aTbJGm4q5F0Lzzn_hszBFGUrNbvglF2RKunjkxZVQeY5F3bknBvdRiDGdEhQ81RPpl2qWVVXVapGrlS-Azv2HaZkaGd-JtfKcN_bg5g2BsoSCws8skH1RAEN1rvolYh9oGe4WDhnQwcicu2XGT371KHHigFmn_TjDNBAO0AgmNDmtXrIQSkq1NSfCUVwQnaxre99nVgOq7kEhH6eEWRSHc8UKosa2osCtRMuGCRwgyuI1f59gaVvBVQ8fNzTdtPclhV60dNUYl1ge-eAtY75ojzoa_QSvFOhDA3_qfXH8LYBruSHeS4tVsJTg_iT2HsR-OYtOOtLv4GiH_6nJ-INMKMOtNe6_7iMZOCZIChSBfiY-HfH9DrRLSjuZQ-HdEs_6_mWbGW43OYNIm-IrClphVVF0TV5napW6NpdqyUbT8aLtRU5PDLkOLtRGFez6KbvPp35pAXua797x1XYinsT9hQGRjKaf83nuGDUj45Se-Zd9gTOgoZ-EWb7RHNB4AmNVx9C368S7kADxoCNvutu-cN1l4XmHkWwhQzX_Hv0IyuQRmL8bGTFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: نه تنها ایران ونزوئلا نشد بلکه دنیا در برابر قدرت ایران حیرت کرد
🔴
شرمنده‌ایم که مشکلاتی وجود دارد. ما در جنگ تمام‌عیار اقتصادی، نظامی و امنیتی قرار گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/143275" target="_blank">📅 08:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پزشکیان:با تمام وجود به دنبال این هستیم که تورم و معیشت مردم را حل کنیم/ می‌فهمم مشکلات زیادی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/143274" target="_blank">📅 08:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcefa0d663.mp4?token=JXWZiuv9SbKzs6-ymF9wgpRz7ciRXdQg3zyiNUgmol-7p8AwuopVEeHxBCKj3nHAMlpKOToG4airN3M_cwD13Rbp-w2p_VEs9Z5hnEswd5QZGCcnnqWqoHq_IcSfIVr2wn2InsbXA4dcVbN6f86Y9suuczFtPkeqc1W_UmazobbGLbMI1pnUg9Stdn3DFb2zPDNXbcbxh5XMOwpZ0S6Rm6nD9p2ewf8MiU1lRlfu1_G75a0qL7moz7XXF5V6X14EMh3Vy4jX9aZC_IO_W4s1cBXDHr3OfQ7RbHnnHR9K7MlTiRnVB-eyYcXO2r09z8gTEQQO-SjZ94JfUWU46pDktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcefa0d663.mp4?token=JXWZiuv9SbKzs6-ymF9wgpRz7ciRXdQg3zyiNUgmol-7p8AwuopVEeHxBCKj3nHAMlpKOToG4airN3M_cwD13Rbp-w2p_VEs9Z5hnEswd5QZGCcnnqWqoHq_IcSfIVr2wn2InsbXA4dcVbN6f86Y9suuczFtPkeqc1W_UmazobbGLbMI1pnUg9Stdn3DFb2zPDNXbcbxh5XMOwpZ0S6Rm6nD9p2ewf8MiU1lRlfu1_G75a0qL7moz7XXF5V6X14EMh3Vy4jX9aZC_IO_W4s1cBXDHr3OfQ7RbHnnHR9K7MlTiRnVB-eyYcXO2r09z8gTEQQO-SjZ94JfUWU46pDktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور پزشکیان: تفاهم‌نامه نتیجه بحث‌ها و گفتگوهای طولانی همه کسانی بود که دستی در آتش داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/143273" target="_blank">📅 08:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af847fdbd.mp4?token=e-CTqxlGvm7uew3BYT6pQyKqqIj2zKBEy92mRclJlAtBX-Sh9QlwJMSPwskV7VknWyDr3NJ5P5NmzbQCeAu5su9iMSrw2joCVKK3btVWcVxJBNTTwE0KawO9E-QM6IYRqNFNs9X0eYu8ANGiH-DQ-qvhGX6EUh0FJTJDTHKC74YFD0LI9RtEAkVfZz6jCfx7mEqDT387qseMI7MzIJNxSyYTJhj8iKWm2Suix5NqY4z-iuTiCqX0d1LJYAZLLdRnyo-gXeit724BhZZinnztk4S6hWE-AqFYbJRjn_hrRzjBrWyhfU1X57DKutIZOr67YlTwPaeZToFYz-P99A9q4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af847fdbd.mp4?token=e-CTqxlGvm7uew3BYT6pQyKqqIj2zKBEy92mRclJlAtBX-Sh9QlwJMSPwskV7VknWyDr3NJ5P5NmzbQCeAu5su9iMSrw2joCVKK3btVWcVxJBNTTwE0KawO9E-QM6IYRqNFNs9X0eYu8ANGiH-DQ-qvhGX6EUh0FJTJDTHKC74YFD0LI9RtEAkVfZz6jCfx7mEqDT387qseMI7MzIJNxSyYTJhj8iKWm2Suix5NqY4z-iuTiCqX0d1LJYAZLLdRnyo-gXeit724BhZZinnztk4S6hWE-AqFYbJRjn_hrRzjBrWyhfU1X57DKutIZOr67YlTwPaeZToFYz-P99A9q4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: تا جان در بدن داریم خدمتگزار مردم خواهیم بود/ امیدوارم بتوانیم با قدرت از بحران‌ها عبور کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/143272" target="_blank">📅 08:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رویترز گزارش داده است که عبور محموله‌ های نفتی از تنگه هرمز به‌شدت کاهش یافته و در روزهای اخیر به سطح بسیار پایینی رسیده است.
🔴
‌بر اساس داده‌های ردیابی کشتی‌ها، در روز پنجشنبه تنها هفت کشتی حامل کالا از این تنگه عبور کردند و هیچ نفتکش بزرگ حامل نفت خام یا کشتی حمل LNG در میان آنها نبود.
🔴
تنگه هرمز پیش از آغاز درگیری‌ها مسیر انتقال حدود ۲۰ درصد نفت خام و گاز طبیعی مایع جهان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/143271" target="_blank">📅 08:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143270">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7gVWkOPpOdZRsNgOQs0SRD9j30WJdutw-nVNQezHAMNpw70kQv1ZJd38pQtm5HvgouijbiGkj4Go7CS-a14R0wIUN6xuHklhZDlcJPOBq3p37lAi4MbMuPSNjUZsq9RoxXg7W40hf8HdGlbEUJj3yqb0Zb6oVdMy_ZI6klYzIiv6vUq9ShrvdC4sK9zhtXFT84Rtwvn2lzc61zdvBJhuuw-WTBaMEnlkb13JamoyUuTRjvJyRVcc0WZDYvJEeO-3G3vOkmS_ztXGBw9Bx5CxOt_hluZij8M2akpTwunx53hE0h_OMVmoypqdXlnbXnbVhUpNsFudt9H_l9zj4vp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیهان: پزشکیان و قالیباف به دشمن پالس ضعف و انفعال مخابره می کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/143270" target="_blank">📅 08:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143269">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
خبرگزاري کان
: اظهارات شما درباره "کشته شدن ۴۰ تا ۵۰ نفر در غزه هر روز" باعث ایجاد موج بزرگی از اعتراض در سراسر جهان شد.
🔴
بن-گویر، از اسرائیل
: عالی. عالی. من ترجیح می‌دهم که آنها گریه کنند و یک مادر یهودی به خاطر پسر سربازش گریه نکند.
🔴
خبرگزاري کان
: آقای بن-گویر... شما نمی‌توانید این‌گونه تبلیغات کنید. شما باید با مسئولیت صحبت کنید. ما هم با جهان در ارتباط هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/143269" target="_blank">📅 07:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143268">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/je2riFlDHci8xKbN15MbSnsbLgE2XhwI55UWyKYwodgm56qEYJ10Q4YvZtTwcJb3HYBouzgOMzN8Z6g70qwe-HQkrTtBmYLBTPzxYz7w_BHXA0WPKSpjEen5Y7wQw6_v7ilG-3h9F5pbl0RkhiU_aDfDFsSkEKSOSyuQcmo-TIgkQ2y1qva9GaEu8ptpZOcz7-SNk3zytDWkpHi3f2EbD1ZE-S9YH5Opn3zkV61M9n4trsM7J6kuVfd0F3AddHLGwgt0Ans2WtDtLblJ7N9DgsF25R92f11tsf8v-BWaX70KRLKOhkWka1RhiwyBDF9gIPAoHUMpIZ42geitV9fCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: بیش از 1000 کشتی را برای عبور از تنگه هرمز همراهی کردیم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/143268" target="_blank">📅 06:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143267">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ-veF01CIyqpY3XB8bSSZfxvEVdw5N1cXr7ezj7cobVOqPdp6YEHT5PL8o8AvjyqSd8m1W39WxCvAHEvsGSlXn4Xl4S36jp5gQKvUeY2PTBgNkP_8nyIuZVtlo_ZIOTkfEwpBTFDoWLPBtPF8hmQWeSdM_ov3zf5lXSAYqHkAVP465h7BmqiSrGe5gZ0XR1ydCGwHzRH66B96hJYVHhpcV6aewZeYJjLQ4AAqLzBzXhaK-vvLKqZWyktHBgp92JXEYLMjzUNhsgr219aKfVX1Guat7zz7TdgGN8uQoyVwptkzsfauXkZO3BcyL5LSN39LvInx5dGCCxDE4jFICa2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/143267" target="_blank">📅 01:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143265">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghZz78qrhhSJ12tCpN-dRwVUO682ggNkQ83Pymn6q5RUzcvdEFuArhFP37Ctw4WpxGTVx8nJTaBtARBW36GVxFEu6gEQbVMqMN1e_1ey1qoN84LF4wZg3LQofjb_xqNMV3mSbsTUZzt3hO941Go5bAqvIWIyuXr0p8jqdiRGaaeupSornUtikRgkJ-opePz3S-KXddxY8dytlEY6iYWDezL3Pc4gE2pFCd-qHIYz6UVj60fGB-0yx0hxo7HgIImHlkUN_ipVV2mDhTeXGg1gM76SiZda504hizu3Vka5XMzwLBijihVVgr_BfTyx9nGhYuVRBP44Wp4DOh_OKWQTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
میتونیم تو آمریکا هم گروه نیابتی درست کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/143265" target="_blank">📅 01:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143264">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd43a5dfd.mp4?token=GiV4JKj8iMhUWqJBcZfBbudqxy2-U9x4oOQZQZ2lf8ZzhkxXz0pxh8bKUlwXY21nHXNNQHvPdc-eWMlu8HHgkyqpgSMIU0AnncAbl872NoSKif7bz_rdmfLOq1tBHM05sV-u53BTV701428Fqmnku5xNyrJ6htxe8AgbZXAMZ4rotccaysjd1s2gubWe4ZjBsB0EIgZJE59wGI5yRPH5GZSOTjuQjuWSQO_oscbJ-ZPMY6Zr85KOCHfIbZhEJ0nKoOqXXzmVxWTY2p3y2zS2w9kp40CwWyrWYXJAnQonOvSKJN3sZqpposBf1xQI49h4g-FG1Qg1noQpblYc5d79Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd43a5dfd.mp4?token=GiV4JKj8iMhUWqJBcZfBbudqxy2-U9x4oOQZQZ2lf8ZzhkxXz0pxh8bKUlwXY21nHXNNQHvPdc-eWMlu8HHgkyqpgSMIU0AnncAbl872NoSKif7bz_rdmfLOq1tBHM05sV-u53BTV701428Fqmnku5xNyrJ6htxe8AgbZXAMZ4rotccaysjd1s2gubWe4ZjBsB0EIgZJE59wGI5yRPH5GZSOTjuQjuWSQO_oscbJ-ZPMY6Zr85KOCHfIbZhEJ0nKoOqXXzmVxWTY2p3y2zS2w9kp40CwWyrWYXJAnQonOvSKJN3sZqpposBf1xQI49h4g-FG1Qg1noQpblYc5d79Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گمرک شهید رجایی، پشه هم پر نمیزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/143264" target="_blank">📅 01:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143263">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5mlVDs8WQisxzkI8ZOMI-zCWsf53wpSkdQpbv7uCvd0fdWV7zaIV2aU_M33Dq96mRbhGKGBY6TLsIvsQNRXZkXxn09f1749SO8FR5G_54Sg7xgHyPOQhIPo8WojlBB0pmbwBRFk98tPB_iJ5Cl1S2vjbzE2nMdWEgnDXG1Y6Pk-XBCso59_7zqLjqhVK_dgO-vr3Be0I4V-MqbhRWwRiZz2Yi5D66JyzYGgp5wK8RzWUaf0bste_pF4SI4mLx7lT2FU35viPk76pRNSlNUB25QH73JadnI8QXBj4yGtZ__CGAa6nv3LVsyk5TQJUx8968Oww3RcDar4GY24MevohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازم این عکس رو پست کرد و نوشت تنگه هرمز قلمرو آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/143263" target="_blank">📅 01:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143262">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
علی هاشم خبرنگار الجزیره:
فرمانده ارتش پاکستان به ایران می‌آید
🔴
منابع بسیار مطلع به من گفته‌اند که انتظار می‌رود فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، طی یکی دو روز آینده بار دیگر به تهران سفر کند.
🔴
به گفته منابع من، هدف از این سفر
فعال‌سازی مجدد میانجیگری میان آمریکا و ایران
است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/143262" target="_blank">📅 00:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143261">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
دادستان مشهد دستور برخورد با بی حجابی داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/143261" target="_blank">📅 00:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143260">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phsR71Ku2MRjDtYNpUw5kvC9YjBq0j58GKWTJ5GtcaPR9LXEwf1MZUmjoRqxkwEqVqob24u3eZ36I17KuGcOwj0nm27nkTWrs1Hdj_R1cyJiQbhO2iEP_Ji5swPMSc0VPWNUv_tqeBz-chNHUN6kwUmxlR_QLvFt9S3IgkMwgzbbk9l9bXK_Y-F0p9mTUA28w8tp0h8JGJxUlP1Nq-c43zHjtTuNb3x6zY276BjfDDvyC0eN2UxpOZ7IDi4Rxe6yR0TyGxN5WwA6pBHy9_ZHOGiIbyfEuFZEs0ogT4rL8m0rvsfrIdnHzHccfRpZFKPpsYcEFxa_XEIjQv0WA1nOdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخن بزرگان
🔴
مردم خودشون نیازشون رو تولید کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/143260" target="_blank">📅 00:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143259">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ایلان ماسک: اینترنت ماهواره‌ای به صورت گسترده مستقیم روی گوشی میاد!
🔴
ایلان ماسک گفته داره روی یه شبکه بزرگ کار می‌کنه که باهاش اینترنت مستقیماً از ماهواره به گوشی وصل میشه؛ یعنی دیگه برای استفاده ازش نیازی به مودم یا تجهیزات جداگانه استارلینک نیست.
🔴
این طرح فعلاً در مرحله آزمایش قرار داره و طبق گفته ماسک، قراره در ماه‌های آینده گسترده‌تر در دسترس مردم قرار بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/143259" target="_blank">📅 00:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143258">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
👈
المیادین: ایران دعوتنامه پیوستن به «توافق مکه» را دریافت کرده است
‏
🔴
شبکه المیادین مدعی شد ایران دعوتنامه‌ای برای پیوستن به «توافق مکه» دریافت کرده و این موضوع در تهران در حال بررسی است.
‏
🔴
«توافق مکه» میان عربستان، ترکیه و پاکستان با هدف تقویت همکاری و بازدارندگی دفاعی سه کشور شکل گرفته است. وزیر خارجه ترکیه نیز پیش‌تر گفته بود این توافق علیه ایران نیست.
‏
🔴
تاکنون جزئیات رسمی درباره دعوت از ایران یا تصمیم تهران برای پیوستن به این توافق منتشر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/143258" target="_blank">📅 23:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143257">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ادارات و بانک‌های زابل، زهک، هامون، نیمروز و هیرمند به‌دلیل شدت طوفان و افزایش غلظت ریزگردها، فردا تعطیل هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/143257" target="_blank">📅 23:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd998e89b.mp4?token=SrOI9t-UTKHdcNYyMM6L4F9EvKCv0-X93h1zgBQ2E_8YUCRwziRFO2YHqR-ELJ2bdN0pjNwkaAMKrjex1uaMkAjIDZrbzeLLv75yEkz6e3OzJYEjw3q4571MBs9_SkWDoWiYm0xTXa4aH911bZ4Wg_wW-vFtDIikhgq9RV3V7tClV0JwroClLShxy7OdOC4lwAesDc-TY6ts20ZYfEkAyAcEVyoPr9pFw18ENy_gHb724nEBfhkyUB7-ZmFmvbZ-M77HJ4Blw_FYs0e00RYK_y8hqIsgttU_Q61hEiOI92YInfmk2UBadCt-_lhypwK6fxBgJH8NKKZus_vtiZr80w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd998e89b.mp4?token=SrOI9t-UTKHdcNYyMM6L4F9EvKCv0-X93h1zgBQ2E_8YUCRwziRFO2YHqR-ELJ2bdN0pjNwkaAMKrjex1uaMkAjIDZrbzeLLv75yEkz6e3OzJYEjw3q4571MBs9_SkWDoWiYm0xTXa4aH911bZ4Wg_wW-vFtDIikhgq9RV3V7tClV0JwroClLShxy7OdOC4lwAesDc-TY6ts20ZYfEkAyAcEVyoPr9pFw18ENy_gHb724nEBfhkyUB7-ZmFmvbZ-M77HJ4Blw_FYs0e00RYK_y8hqIsgttU_Q61hEiOI92YInfmk2UBadCt-_lhypwK6fxBgJH8NKKZus_vtiZr80w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فووووووووووووری / نتانیاهو و ترامپ در میدان انقلاب تهران اعدام شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/143256" target="_blank">📅 23:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۱ ریشتر نورآباد ممسنی را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/143255" target="_blank">📅 23:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143254">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e79a6b6eb.mp4?token=PpxUS-8Xu_9UU1dklVlTxplVSpEGbmkuk7MFhqqF_aH5mVhtifIf0vq1-m2oJmFxI9gi6TKnHm_ZoxKjC7SxBT5yYxR8YlvEGMu2aRgVVNHe1R6DlP_jSIZww79sEmj5ltm8CR5TaTTk9aKHynnf6YPK_MBMR8XsEnYDsEuClBKQ6_hRZMRN7Pu0cFRD9mYxtp2_2jOUJ8TfB2kwvuz6z_PJweaahUYK6yJcDr5Ypf9jbAEj5pJC1RCgblnAWO-MWKtTXSk1zAyR8a2beAXJpxmJgjmK3yPHoFzeFww2K7NAZxYGykHN6kMta4o1gV8EmKnNcr7MUZUJFLUXzmeTIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e79a6b6eb.mp4?token=PpxUS-8Xu_9UU1dklVlTxplVSpEGbmkuk7MFhqqF_aH5mVhtifIf0vq1-m2oJmFxI9gi6TKnHm_ZoxKjC7SxBT5yYxR8YlvEGMu2aRgVVNHe1R6DlP_jSIZww79sEmj5ltm8CR5TaTTk9aKHynnf6YPK_MBMR8XsEnYDsEuClBKQ6_hRZMRN7Pu0cFRD9mYxtp2_2jOUJ8TfB2kwvuz6z_PJweaahUYK6yJcDr5Ypf9jbAEj5pJC1RCgblnAWO-MWKtTXSk1zAyR8a2beAXJpxmJgjmK3yPHoFzeFww2K7NAZxYGykHN6kMta4o1gV8EmKnNcr7MUZUJFLUXzmeTIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال رضایی: ما تاکنون به هیچکدام از منافع اقتصادی آمریکا حمله نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/143254" target="_blank">📅 23:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143253">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5154e38b47.mp4?token=QIWvlifrAdxQ9tgN7j6N4Yowqywo2JMhKOke90omdK69GWeG3z_mX-bGNsnitV_qllsTOavuIlxpqlfHcMWLyTZ56yoehhmPVaCQCM7kAybgK71dAU1mCaKuah0LAiXM0ygYHpD_OjahyUqyExlYKKqdIoXUQKtKGKbLUqI6X5kJR2Rz2Rhr_k4i5usjOvW3lnI0LqH3zBPY3Yq3F3v6F0CyiotdB_qv6WlH6FkNWjoc-4utyd51AWvD1u5mzBuGxT771K4b030dUOPmXe7hNn7Fa72at4V4EcqqcPPp9lUBUAdmtL_VDxH2lKDwsy4Mj-7z0Eu6Q6v3gWEeZUwIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5154e38b47.mp4?token=QIWvlifrAdxQ9tgN7j6N4Yowqywo2JMhKOke90omdK69GWeG3z_mX-bGNsnitV_qllsTOavuIlxpqlfHcMWLyTZ56yoehhmPVaCQCM7kAybgK71dAU1mCaKuah0LAiXM0ygYHpD_OjahyUqyExlYKKqdIoXUQKtKGKbLUqI6X5kJR2Rz2Rhr_k4i5usjOvW3lnI0LqH3zBPY3Yq3F3v6F0CyiotdB_qv6WlH6FkNWjoc-4utyd51AWvD1u5mzBuGxT771K4b030dUOPmXe7hNn7Fa72at4V4EcqqcPPp9lUBUAdmtL_VDxH2lKDwsy4Mj-7z0Eu6Q6v3gWEeZUwIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال رضایی : بازشدن تنگۀ هرمز هیچ ربطی به توافق ایران و عمان در مورد مسیر میانی تنگه ندارد
‏
🔴
در زمان بازشدن تنگه ما آن را مدیریت می‌کنیم و این مدیریت با دریافت هزینه همراه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/143253" target="_blank">📅 23:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143252">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5818c5a880.mp4?token=nhfuf9cXW5ReY5wWWU8XOIeOK6_f8zl3O2uOlBopPYZDSdHMTqRhWYLaItESP1B7pVPKApfCyWT2eHmSICftP42nEA2HVKmqrvtDlyWigFhXTrZL3Tzn8d0ZE4ctySqg6jPuHlnPu8yngH7PJWosKkdgNhNXk6b48Lm_yPoXnykDo6umi0eLqmru_cmj5Vs-Lxg-UrzQhSGOANhJ-92xXUOIAPh7bG2DIbAH7V09FRszXANDsBc0tVTfEXd00W33l1tcRRoWBGIEEsmN2ds_eyiF-fhHJ_k0_x1m2gcTydW1AcAM1ozdccCUg6YelDah4NcVggbZYMYKu-YWTuhWBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5818c5a880.mp4?token=nhfuf9cXW5ReY5wWWU8XOIeOK6_f8zl3O2uOlBopPYZDSdHMTqRhWYLaItESP1B7pVPKApfCyWT2eHmSICftP42nEA2HVKmqrvtDlyWigFhXTrZL3Tzn8d0ZE4ctySqg6jPuHlnPu8yngH7PJWosKkdgNhNXk6b48Lm_yPoXnykDo6umi0eLqmru_cmj5Vs-Lxg-UrzQhSGOANhJ-92xXUOIAPh7bG2DIbAH7V09FRszXANDsBc0tVTfEXd00W33l1tcRRoWBGIEEsmN2ds_eyiF-fhHJ_k0_x1m2gcTydW1AcAM1ozdccCUg6YelDah4NcVggbZYMYKu-YWTuhWBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی : ما با عمان روی مسیر تنگۀ هرمز توافق کردیم که یک مسیر میانی است اما این موضوع روی کاغذ است و تنگۀ هرمز زمانی باز می‌شود که آمریکایی‌ها به تعهداتشان عمل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/143252" target="_blank">📅 22:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143251">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b20524ca.mp4?token=sVla7e637joQiuRBOQa-lmVsIG2c-Wogria6AmPXijEv1WdI0guQc3kjklSTopIh7o2Y44YALmVO-EN4nJlZTjIIlPuHDH7njadyvRUMzYRwbagiWJ1TTrobotoXyJdxLH7YeLAP8pyUCRsTUWE8muofWNQlzi4pdEj0ab0EtQ9nE6q4giMqsFRO4Bx3PYKFMjoVBnJ6zxz6v1lMCKmEpDABRGhlQKlhHydZgHyfTSckX6qcN8LUWbB-8MDZmP4kN6Qz5xS7K9QhRpxb7-YSyJiFG1YNNoxUDdQFgZbxU__QYUWjYFfl_6PKQX9zANVp86_GKwbZuV3pKzg2XK2zKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b20524ca.mp4?token=sVla7e637joQiuRBOQa-lmVsIG2c-Wogria6AmPXijEv1WdI0guQc3kjklSTopIh7o2Y44YALmVO-EN4nJlZTjIIlPuHDH7njadyvRUMzYRwbagiWJ1TTrobotoXyJdxLH7YeLAP8pyUCRsTUWE8muofWNQlzi4pdEj0ab0EtQ9nE6q4giMqsFRO4Bx3PYKFMjoVBnJ6zxz6v1lMCKmEpDABRGhlQKlhHydZgHyfTSckX6qcN8LUWbB-8MDZmP4kN6Qz5xS7K9QhRpxb7-YSyJiFG1YNNoxUDdQFgZbxU__QYUWjYFfl_6PKQX9zANVp86_GKwbZuV3pKzg2XK2zKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محسن رضایی: مردم در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/143251" target="_blank">📅 22:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
محسن رضایی: اگر ترامپ بخواهد کارهایی بکند زلزله‌وار مقابله به مثل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/143250" target="_blank">📅 22:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143249">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17724980d1.mp4?token=m5nmEfXHXUoN3tTB6aytQ65xWIDturJcHXfliIBrlP3Lrslx8E4zTZC_PBqIDMU9tpgO8AiP3KXd6yJqoFzq2d8RrAkLGm4TugO1AgtiEs-pAzUexPsq0imZzgn6umiKBquZUES-K2gjk84eVPJ0PJ2MJE-sGkR3b24HTsPOuwaDYiul1FRTrZ4GniwhbI3FFTB7pnxcEzxZiTVP6zfLjWwoIIvU4rRAThAlxGpSXJSi5kyUhzidSCHLmKoaJXFpysLYTmVB9GE4bjGVyRHPed3oOixj4zpY1iKBsB-p_twW9jZ0gVx9ARAlbsj5TFBHSacpIWIgLWvU1yGlXbIIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17724980d1.mp4?token=m5nmEfXHXUoN3tTB6aytQ65xWIDturJcHXfliIBrlP3Lrslx8E4zTZC_PBqIDMU9tpgO8AiP3KXd6yJqoFzq2d8RrAkLGm4TugO1AgtiEs-pAzUexPsq0imZzgn6umiKBquZUES-K2gjk84eVPJ0PJ2MJE-sGkR3b24HTsPOuwaDYiul1FRTrZ4GniwhbI3FFTB7pnxcEzxZiTVP6zfLjWwoIIvU4rRAThAlxGpSXJSi5kyUhzidSCHLmKoaJXFpysLYTmVB9GE4bjGVyRHPed3oOixj4zpY1iKBsB-p_twW9jZ0gVx9ARAlbsj5TFBHSacpIWIgLWvU1yGlXbIIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال، رضایی: ترامپ به اسم عملیات آزادی ۳ ناوچه به‌سوی تنگۀ هرمز روانه کرد و وقتی هر ۳ ناوچه را زدیم، او ۴۸ ساعت بعد گفت عملیات را متوقف کرده‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/143249" target="_blank">📅 22:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
دبیر شورای عالی امنیت ملی: باید در رفتار دیپلماتیک ایران اصلاحاتی انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/143248" target="_blank">📅 22:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143247">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1939831dcf.mp4?token=iRGX5z0BgLXkKz4e1cMlFGcZ82WNkC8F1UFPymVKu6nmI54yPGobjwYkMeorUWINCIAOIJAmEDrROw1ztCBQdU_mz3KBnq9rdVqI6V4P-CPES8BooTdVTGefvTt1-g7P16LMDq-2_qLssruwRFWLGkTikOfGa_xNdhORZUlBPK6n5z4ZYrvjsgOhdp3LWDfI3Qst6MneuNx33CTAO6IoMKpP32ujqQQptxd5aohnLBklD8MMx_SCFh1-Nt3L87xegy-EhtaQy36R7pPLoG5u1Xfn4-tjTf2pcCZYIPsp3bqyH3_HvHHzcS7f1eiO9XF5PYOt90Ujzf6aVl_PUoQnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1939831dcf.mp4?token=iRGX5z0BgLXkKz4e1cMlFGcZ82WNkC8F1UFPymVKu6nmI54yPGobjwYkMeorUWINCIAOIJAmEDrROw1ztCBQdU_mz3KBnq9rdVqI6V4P-CPES8BooTdVTGefvTt1-g7P16LMDq-2_qLssruwRFWLGkTikOfGa_xNdhORZUlBPK6n5z4ZYrvjsgOhdp3LWDfI3Qst6MneuNx33CTAO6IoMKpP32ujqQQptxd5aohnLBklD8MMx_SCFh1-Nt3L87xegy-EhtaQy36R7pPLoG5u1Xfn4-tjTf2pcCZYIPsp3bqyH3_HvHHzcS7f1eiO9XF5PYOt90Ujzf6aVl_PUoQnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال، رضایی : ما فعلا فقط جریان نفت در تنگه هرمز را محدود کرده‌ایم اما درصورت جنگ اقتصادی اجازه نمی‌دهیم نفتی از خلیج‌فارس حتی به روش‌های دیگر خارج شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/143247" target="_blank">📅 22:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143246">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فیلد مارشال،رضایی: در آمریکا مردم با جنگ با ایران مخالف هستند و دولت و ارتششان را حمایت نمی کنند، اما در ایران مردم و حاکمیت هماهنگ هستند و هر دو پشت نیروهای مسلح کشورند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/143246" target="_blank">📅 22:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143245">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
فیلد مارشال ، رضایی: در صورت ادامه محاصره اقتصادی شرکت های اقتصادی آمریکا را در منطقه خواهیم زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/143245" target="_blank">📅 22:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b333c88c2.mp4?token=CLYvtTKgSBpygZAwqtH2BQQ-A33BuN_AZVsQxA67S1dW42Z3CrDDbY3FyB6l0DS0_lHO6-a-I41fAMST-l2MfjxYvaWNzT3VZZ9UAFlC-Y-d68JqjRjnP74SRmZBUCnDcjVh6wCKs98JdTr5cvyqb2U71DmWsfZ4VBi3QkXiYL35aRqDY8WBx3415KklVuUj5LWMGTatVeEaTCp8JMJXbCYUYNrXkHyAeQW8piNdXGPRtgay0gbzKIPXH9B5CfQSDcU1UBOdA4PybXTCWpwyJ__R3u2Y0di_6hSNlpt-55jCXC5BiS9cnI9AXZENl-4qP_jDCx-DiGTDUPUtf4euog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b333c88c2.mp4?token=CLYvtTKgSBpygZAwqtH2BQQ-A33BuN_AZVsQxA67S1dW42Z3CrDDbY3FyB6l0DS0_lHO6-a-I41fAMST-l2MfjxYvaWNzT3VZZ9UAFlC-Y-d68JqjRjnP74SRmZBUCnDcjVh6wCKs98JdTr5cvyqb2U71DmWsfZ4VBi3QkXiYL35aRqDY8WBx3415KklVuUj5LWMGTatVeEaTCp8JMJXbCYUYNrXkHyAeQW8piNdXGPRtgay0gbzKIPXH9B5CfQSDcU1UBOdA4PybXTCWpwyJ__R3u2Y0di_6hSNlpt-55jCXC5BiS9cnI9AXZENl-4qP_jDCx-DiGTDUPUtf4euog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال ، رضایی: در صورت ادامه محاصره اقتصادی شرکت های اقتصادی آمریکا را در منطقه خواهیم زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/143244" target="_blank">📅 22:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پولیتیکو: طبق اسناد وزارت دفاع آلمان، این کشور قصد دارد تقریباً 12 میلیارد یورو برای ایجاد یک زرادخانه جدید از موشک‌های دوربرد هزینه کند تا از روسیه بازدارندگی ایجاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/143243" target="_blank">📅 22:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5b2734a6.mp4?token=HmR7x9gcr9-a96e86q9A3SlfdhpWdJ-GUewJ6b__kz3Ot_Lqisr6RDODtCEn48Il2JKNi9eV3ZKEgZBL2EFa-54_WHgxue9SRqGSvxg0_eBfO7gfGZbx77wXY5Q87TUb_2Os8l_7MUPC9DkPvd-qFQZzZgihhBHgJyikHKZ1wAzsh3XYHptxNJRSa4dGM8jKVi4UbjhbG5ziIoNbP6VwMceUFeP--LXL0PYe5yMJqxC0idWkAV1iZ159dp5V_dEASbDmlOKT70HW1fmGwZ-r_xR0ICbKG-z3weVE7Oe3GcKOdgEwqvfF3O84sKs-xzuH6XsnGKsb1UjgsK6qt3EvJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5b2734a6.mp4?token=HmR7x9gcr9-a96e86q9A3SlfdhpWdJ-GUewJ6b__kz3Ot_Lqisr6RDODtCEn48Il2JKNi9eV3ZKEgZBL2EFa-54_WHgxue9SRqGSvxg0_eBfO7gfGZbx77wXY5Q87TUb_2Os8l_7MUPC9DkPvd-qFQZzZgihhBHgJyikHKZ1wAzsh3XYHptxNJRSa4dGM8jKVi4UbjhbG5ziIoNbP6VwMceUFeP--LXL0PYe5yMJqxC0idWkAV1iZ159dp5V_dEASbDmlOKT70HW1fmGwZ-r_xR0ICbKG-z3weVE7Oe3GcKOdgEwqvfF3O84sKs-xzuH6XsnGKsb1UjgsK6qt3EvJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: باید از وضعیت «نه جنگ و نه صلح» خارج شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/143242" target="_blank">📅 22:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV8pQ4vTgeZe5ADY7238tlmx-GhL50XCbHxLrTTYP_jkxw6LUi9LdZ6bnXHxTj07ACqXOn875YV2ZmC1_JxSzsj27miZUGupS6zeUk1xBu1n0ZwzbxG_VZ5JIoTP8BBZMEQJ-ZJWK7bMVhCWSLMc6uTplyTN30jj5HDx-Za0eEO3Hs5NFVKup-S9Rw56T8sJsJ7TZmVZg8XNKHBNZPp8MeI7CfBsxrgsjbf1tVjUIZYgWwCFpucNZ2WNYlfTyjmguLkwolazEC_F2Kd8VoMLft6GpmPtyxSyltBzuGnBa0ohArb4mwuuo7cYKiP8wN7YqzaetzTic3SqUrMhhPPBOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: حمله ترامپ اشتیاق کشور ها برای تولید سلاح هسته‌ای را بالا برده، به خصوص اینکه سازمان انرژی اتمی برای جلوگیری از حمله کاری نکرد.
🔴
حمله ترامپ بجای اینکه باعث امنیت هسته‌ای شود، باعث ناامنی هسته‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/143241" target="_blank">📅 22:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر اقتصاد: احتمال انحلال چندین بانک در ایران وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/143240" target="_blank">📅 22:22 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
