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
<img src="https://cdn4.telesco.pe/file/cWt925GrnxF4zF43HIMG6F-JqYuH6Z0sAzTmmTaqoXb4CrSNVDqz5amntQOmdLjz8xuCtyorfO32Zl5AeadZ-YmkYx1u3hvpTzKepk0xB33qSgIOc3irTnE9qRIkWZu-obe-qOG0HFTxtncJaoL7xbbg0UxPZg8GXqOYjmtGIVjLr-XUMi-Z5LKqhR319AyEnDJogkFJJfV-BEmEoaF7thlVpR2AYrmGaJVf8hU9MJ7SSBjXQlxEkNs_6Gm0FbiERGkdnQAyapB7PdtdH3kqfV773y9Hh2snooNJVSDAuJ1Atjjak2Rz61WYxxmz_diX-EKUNPCbd5cghMbUib9iLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 962K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 19:58:23</div>
<hr>

<div class="tg-post" id="msg-129181">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: تماس بین نتانیاهو و روبیو، وزیر خارجه، به زودی، درباره لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/129181" target="_blank">📅 19:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129180">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667c0e662b.mp4?token=e9XJmvLNqip2uitPNmQwpP6OHxEKelj5TL-1KOnYo2efqVxBqpQ4bSKD8s8VSZj2KqLockU0RK2s8elv2q5REX283CUIFvgq0gc-Tfd0c5bYoLZ6e3whd5u2wchFuxFdl0cfn0_TZopxZq-Lws_nKgnja9u_ILSjQEZW1vCVHpEDCDuIDBtq5m8Kgh2FWH6dEa2kqPRsPpwgacIc-ADHbh6Rf_ADezJSvEUEwb9DO-WUQLJDQYVRrQpmPfI4KbAX-aONW9Pe9nEl_wvizpPvihQLHCLFGpDpaZar0YAYC2NwNr6D8IY0dUSpRgjrfUIcXV0j7nOVHaR5pJOhD24gsEw4rNCczSELlPrTS_cH9FqFoZNxbrtWlOJuhqHLMyRh1hhw8KVWEMm2hVUv04Vh4SxDlNhj070gBbnP29jMgguSlKez2Z3U_7ZztlG3VRxUWOGc49LqzxxBnksd1PMrqvbJQECkDoToqV4kjHCMynhB88Q6aubzVl__TjKPzUWt6MevXbhFbNZYSgCxwBDi2vCEHohbX4b5GXUp5Be4NFDcOTrjmk-LCu4-zCEZnPl5z2lP-sfpEl90RkbzPmB76tGe28Vsp7Kt_4gUfYBKZvDSwHu8fhCPzH2DFQsEjAozmSxq1DVYkz5yLs1s8lkrZDhhCJTP35iAG3GF7wqzuzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667c0e662b.mp4?token=e9XJmvLNqip2uitPNmQwpP6OHxEKelj5TL-1KOnYo2efqVxBqpQ4bSKD8s8VSZj2KqLockU0RK2s8elv2q5REX283CUIFvgq0gc-Tfd0c5bYoLZ6e3whd5u2wchFuxFdl0cfn0_TZopxZq-Lws_nKgnja9u_ILSjQEZW1vCVHpEDCDuIDBtq5m8Kgh2FWH6dEa2kqPRsPpwgacIc-ADHbh6Rf_ADezJSvEUEwb9DO-WUQLJDQYVRrQpmPfI4KbAX-aONW9Pe9nEl_wvizpPvihQLHCLFGpDpaZar0YAYC2NwNr6D8IY0dUSpRgjrfUIcXV0j7nOVHaR5pJOhD24gsEw4rNCczSELlPrTS_cH9FqFoZNxbrtWlOJuhqHLMyRh1hhw8KVWEMm2hVUv04Vh4SxDlNhj070gBbnP29jMgguSlKez2Z3U_7ZztlG3VRxUWOGc49LqzxxBnksd1PMrqvbJQECkDoToqV4kjHCMynhB88Q6aubzVl__TjKPzUWt6MevXbhFbNZYSgCxwBDi2vCEHohbX4b5GXUp5Be4NFDcOTrjmk-LCu4-zCEZnPl5z2lP-sfpEl90RkbzPmB76tGe28Vsp7Kt_4gUfYBKZvDSwHu8fhCPzH2DFQsEjAozmSxq1DVYkz5yLs1s8lkrZDhhCJTP35iAG3GF7wqzuzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: آنچه در هر جامعه‌ای جشن می‌گیریم، بازتابی از ارزش‌های ماست و ما زمان زیادی را صرف کلیک‌بیت و خشم‌بیت در مورد فرهنگ سلبریتی‌ها و شایعات می‌کنیم و زمان کافی را به محتوای واقعی اختصاص نمی‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/129180" target="_blank">📅 19:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129179">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نعیم قاسم، دبیرکل حزب‌الله : تلاش برای حذف حزب‌الله شکست خورده و اسرائیل بالاخره مجبور میشه از هر وجب خاکمون عقب‌نشینی کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/129179" target="_blank">📅 19:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129178">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18a311e35a.mp4?token=CyhuTtm6QAPOQ7gZDYfPq-Fov12IaD4QIPbk8OOTPzH3uKBoQhDLogOhOGkiO4w5g5hWcZPw5PqsPuhg9RJYv8wLNafbSTMTwT2_mLoO7W86oHIAEtsbUAixtsxJHAUhChi5l4y6WD3DuNzcgvSTBc3wr6Z9wj6xtbkuFdFyR1lyl_LyHCFluYoRsUdPfV_9b-ixHkvzwEH39I7uPNGe1ETtKdCmct1sBK-nE1u9EmsvwRbDN22zU8i20iwTpb9avsA3WAq6pt-shfgKr301VoXCHELgk2afxH0JQK474CfJphf5Mwdvi1qlUL0C848qzlYpSNj_ZmWbVpdQqTuUTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18a311e35a.mp4?token=CyhuTtm6QAPOQ7gZDYfPq-Fov12IaD4QIPbk8OOTPzH3uKBoQhDLogOhOGkiO4w5g5hWcZPw5PqsPuhg9RJYv8wLNafbSTMTwT2_mLoO7W86oHIAEtsbUAixtsxJHAUhChi5l4y6WD3DuNzcgvSTBc3wr6Z9wj6xtbkuFdFyR1lyl_LyHCFluYoRsUdPfV_9b-ixHkvzwEH39I7uPNGe1ETtKdCmct1sBK-nE1u9EmsvwRbDN22zU8i20iwTpb9avsA3WAq6pt-shfgKr301VoXCHELgk2afxH0JQK474CfJphf5Mwdvi1qlUL0C848qzlYpSNj_ZmWbVpdQqTuUTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: از نگاه بین الملل در ۴۰ سال گذشته یک روز نبوده که ایران بدنبال ساخت بمب اتم نبوده باشد
🔴
اگر ایران به سمت بمب اتم حرکت کند همین چین روبروی ایران خواهد ایستاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/129178" target="_blank">📅 19:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129177">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy76vKiZ7rCdzArQwftsCVYZyKKq7BnXTGVQxZsO-uXw9lKQs7_Pzz8TouTb-QieSiKSihyz5z4PtoS1t3XDMK88SSf0loNbZwH5MFMhYr20Lsd2B9Ri4i_jRJufaQ0sqooyJVtV9kIL8fyjK5JV5ORWRsxfinyn8Bvf_dnZP3kDTYqQlsyoTRdvRcrHyFjglCZFKk1gxhUD0_zTec22Xs-T7r--cF3ZGpOd0fgYTcT00Na0_aGS8U14RoCLby-TvGfmWFWTIBS8AvY7pvxtLLO7SoDzWd6y5dsRbJXa8IiiIb48VR7-DzvueOnJEK6fyFVblFzkFNFAgvAMuhcBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور هیات قطری در سوییس بدون حضور ایران و آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/129177" target="_blank">📅 19:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129176">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
واشنگتن پست: سازمان اطلاعات آمریکا اعلام کرده که اسرائیل به طور فعال در تلاش است تا یادداشت تفاهم ایران و آمریکا را بر هم بزند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/129176" target="_blank">📅 19:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129175">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری / هلند: برای تضمین آزادی کشتیرانی ناو جنگی به تنگه هرمز اعزام خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/129175" target="_blank">📅 19:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129174">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
امانوئل مکرون: برای مشارکت در اجرای توافق بین آمریکا و ایران آمادگی داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/129174" target="_blank">📅 19:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129173">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نتانیاهو: حزب الله بهای سنگینی پرداخت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/129173" target="_blank">📅 19:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129172">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سنتکام: بیش از ۲۰ کشتی روز گذشته با امنیت از مسیر تعیین‌شده در تنگه هرمز عبور کردند
🔴
از کشتی‌ها می‌خواهیم دستورالعمل‌های مرکز اطلاعات دریایی مشترک را رعایت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/129172" target="_blank">📅 19:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129171">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سی‌بی‌اس: ۴ کشورمیانجی تفاهم ایران و آمریکا یکشنبه آینده در مصر نشست برگزار می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/129171" target="_blank">📅 19:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129170">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
گفتگوی قطر و سوئیس درباره حمایت از مذاکرات واشنگتن و تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129170" target="_blank">📅 19:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129169">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزارت امور خارجه ایران: عراقچی به همتای پاکستانی خود در مورد پیامدهای هرگونه نقض تعهدات یادداشت تفاهم هشدار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129169" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129168">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
بلومبرگ گزارش داد که ۱۱ نفتکش حامل مجموعاً ۲۰ میلیون بشکه نفت ایران این هفته بندر چابهار را ترک کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129168" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129167">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فدراسیون فوتبال ایران بابت رد درخواست ورود به آمریکا ۲ روز قبل از بازی با بلژیک به فیفا شکایت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/129167" target="_blank">📅 18:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129166">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
مالک شریعتی نماینده تهران: ظاهرا همراه با پیشنهاد جمع‌بندی شده‌ی شعام درباره متن ۱۴ بندی تفاهم‌نامه،
یک متن تفسیری ۶ بندی نیز درباره اقداماتِ طراحی شده‌ی ایران، متناسب و متناظر با بدعهدی‌های احتمالی آمریکا، از سوی رییس‌جمهور محترم برای رهبر حکیم انقلاب ارسال و اجرای آنها تعهد شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/129166" target="_blank">📅 18:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129165">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی آمریکا:
جنگنده‌های اف-۱۶ به گشت‌زنی‌های خود در خاورمیانه ادامه می‌دهند و آماده مداخله هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129165" target="_blank">📅 18:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129162">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PEe4SfTK3Y0uI72835emKnoHXE3blDw1aMLtosm08shMnkwP-WVciD-Q-Tbuie3-s_ufPpE05y_CJfrH_bAZi0wcf_jZShewzGuIEErdp-fnUVcGhmtnO2PIHDLPjetac0NEKaGbwElnyz8fB0ikvAzz3Kcww4aur7OuFYX3bopHS5Naa7QqXuUVx4-_-FqqpW-33Yx_S8PmesTOA-8oEcLU52eat9E2at1Y84foNzGCflyEnOVtqpn8LH9RLdTI07b41iodlzdI6zFS6O8T6ohdvw4paqVpa4qZb32DAmhaGZ277lb6AkLRFmd1Di_GX7pUn2etoZ69EB1V1Q0fEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CoTauB6JAG_YIPr1zKi7lpiqq8ZSR9-vF53aKQ0PCmvFt-DmlErnMqJ7cd_p-9o2c-_2bfHx_1E-YmMGnLkheD4euJoYc4PGj55EvGgVtiaaV5NVLwq_dL4Ter92ilRNZn9_qJPxDvkmQvBWeeOkDSN9HNJlQpAqQAKAeZ4Fhu_A880qjlx-7_MzO6Bwo5bxAqwOLFkEG-LQljQF5InRLmkUQANkCZCiYHcsVRpWdrEqcrrE5SzCpaOrCZ31PWgh6_xyCuGfxs5iYBJAEjvADdpekSXuKBQY90uOiZGqXZ_y9TTO4EEtgcuojLHrDRXndxsYya2qtfiCtYcmpzE_zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5245763015.mp4?token=low_ufZIBVx_v2p0PHfoQU30XLPuTL3nLLJabywtSo6186XwAXm_n10KDhG49j9_hlFi0pa5-zsYUYz8_Gmhh-JHX7QLURlxEWQlk0HXjm8SLAf-jpYbdKFI7yjeNHV59ZH9v54b4sJRCUytRrOJcuuClFcYsMlwticaP4eU9JfpLaBJkOp7BGVa8fvaENRVSl2RbO78LKEQntZaSB5kXudEL63piouZzNnQZDfb6LN6yPlqhDkzqYmw_pv0XIC55kd4M-oBGSEThKWlWLuc13JqaIC2AAwr6omtoLOMGetizbK55fidskoe-o0fksO_iCDHXsVCA1dnxQelwfqYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5245763015.mp4?token=low_ufZIBVx_v2p0PHfoQU30XLPuTL3nLLJabywtSo6186XwAXm_n10KDhG49j9_hlFi0pa5-zsYUYz8_Gmhh-JHX7QLURlxEWQlk0HXjm8SLAf-jpYbdKFI7yjeNHV59ZH9v54b4sJRCUytRrOJcuuClFcYsMlwticaP4eU9JfpLaBJkOp7BGVa8fvaENRVSl2RbO78LKEQntZaSB5kXudEL63piouZzNnQZDfb6LN6yPlqhDkzqYmw_pv0XIC55kd4M-oBGSEThKWlWLuc13JqaIC2AAwr6omtoLOMGetizbK55fidskoe-o0fksO_iCDHXsVCA1dnxQelwfqYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/129162" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129161">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8lefqoJgr0XnHSX57uaCb4oYe8q0wZdvgcUKkTpOFRihJUeZ4XWAWEuMG0Is27GIy1bcSiFwWyIqzP2LJFAtZtUQqk21rnai06DjqeksAQ6p3AMNgeG6k3sKcU4R4D45WcuR5J4U4Yquw4R0D0P7x-FmiLgJ1psUCJmEF_CWqVN6omk8quyA4-Qcadvp5gAxi_zfontji8EAioXfxPkb1M1zgu7KCvp0MSZSBCbH1GeEE9ganChlNuPTUWyCQfgcrEAMbMMO8-_slHzhxJuf2PavmM5BF91WWhSG06zV5lkToS537NU66cPnkOKpAGG6p65s24GIxVmLK_EKg7tcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدمنان رییسی، نماینده مجلس:
خوش‌انصاف‌ها(منظورش قالیباف) مجلس رو باز کنید، رهبرم تنها مونده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/129161" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129160">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNpGx2qMqgAvIchwc_vALMlqj8Ij0CY39Yt8LOHFYPz60LPftuINCJ7jp2bthJBonyNeuceGYwePAp9_McKoWM8mp9lm66jLdTom6u47yf6O_olgEsOoDoOILsuq62rLW5DiXxPCZSKKUDped7qsjKGvu_NSfupsrmNMEkMpJWF8H6x6zglBedd4HD81KIBPzDPjOHPjt1PCPvljYnNAl9JYZLa-EN0_ZlB7dp1zbnWXcsUFo8CmX8i-HZ6xAGsgwBafvMq1bwH4ngZXSbjBBQR6bRVFADliOA3XowasSD-DyCwTJeoXvA_UNF3CHFXVzZf974VsUEHFPsm_3XZ1aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
دولت باید همین حالا و از لبنان شروع کند و نباید اجازه دهیم مردم مقاوم جنوب لبنان مورد قتل عام قرار گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129160" target="_blank">📅 17:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129159">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نتانیاهو: به دستور من ، ارتش به 150 هدف حزب الله در لبنان حمله کرد و ده ها خرابکار را کشت‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129159" target="_blank">📅 17:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129158">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmDRrkloM42VtplQ6GrgoeSgdb9jATy2TqgOQMXh5utD7qNt3bny_9J1PwSTLYzVGDpvyOyFlnjL4EC1_ILfZMTWi3RpAdVuW2wBlwJWAVRaBVF6Ount9agrElmdad4S_ceQBeLeDjvJ04_OZ0iwtFVmoDBQ7G_u_Y_w6KsPGx93Lnmer0yevBxzlW0uBvgVboqnFipg-YbM7qxe3MJ_m5BOWphpwZNE0v8C7iWFvuGD8a7ZI-ou8C2dXkTYZfRZ4bYXAaI16mxyLJ8zmjzWMMV_XdUsSsD9XbNv1X7vUwvWpe2M4H2wufBXFGKjVGJ63ePzfi0DeFVCIqQUPJkQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : تنگه رو ببندید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129158" target="_blank">📅 17:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129157">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: رایزنی‌های لازم از طریق میانجی‌گرها درحال انجام است و در صورت فراهم‌شدن شرایط لازم برای شروع مذاکرات، اطلاع‌رسانی خواهد شد.
🔴
طبق متن یادداشت تفاهم، آغاز مذاکرات توافق نهایی منوط به شروع اجرای مفاد بندهای ۱، ۴، ۵، ۱۰ و ۱۱ یادداشت تفاهم…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129157" target="_blank">📅 17:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129156">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: رایزنی‌های لازم از طریق میانجی‌گرها درحال انجام است و در صورت فراهم‌شدن شرایط لازم برای شروع مذاکرات، اطلاع‌رسانی خواهد شد.
🔴
طبق متن یادداشت تفاهم، آغاز مذاکرات توافق نهایی منوط به شروع اجرای مفاد بندهای ۱، ۴، ۵، ۱۰ و ۱۱ یادداشت تفاهم و تداوم اجرای آن‌هاست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129156" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129155">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی جبل الرفیع، شوکین، الریحان و ادچیت در جنوب لبنان را بمباران کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129155" target="_blank">📅 17:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129154">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
خبرنگار الجزیره:
چهارمین حمله هوایی اسرائیل در اطراف شهرک کفر تبنیت در جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129154" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129153">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7667710266.mp4?token=WSpaSUNXL3tvvzUYjnUC-mpegE0cKqXOdmTXfrdj_R7JdMQZIE_yYx2tArLZUr-pMu7EATW3mx9LpOPX9Q3IkwCYwQkp4EUVEGHWRcJee1pYSy22YykAPoqcU1-81kl1wtGwAm3HERDnM__HdE3fujhgvbcPuVGw7r2891Jnmw2OiT5eYW1vST6Hgyikj6lr8vwvgQ0KZPIwle-wZLC7V-T_TLI3Ib7kS_oExhj5xXtYz3jX-R77oCrnM1BCAFMkqJe3IUSKrBBQHiCSICBm1GLpCqQHi_F8p_gL4StHgWdUR0zfVVrmzjAZmH_TWR9o_7fvP6jSwM3zfa_o7UZV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7667710266.mp4?token=WSpaSUNXL3tvvzUYjnUC-mpegE0cKqXOdmTXfrdj_R7JdMQZIE_yYx2tArLZUr-pMu7EATW3mx9LpOPX9Q3IkwCYwQkp4EUVEGHWRcJee1pYSy22YykAPoqcU1-81kl1wtGwAm3HERDnM__HdE3fujhgvbcPuVGw7r2891Jnmw2OiT5eYW1vST6Hgyikj6lr8vwvgQ0KZPIwle-wZLC7V-T_TLI3Ib7kS_oExhj5xXtYz3jX-R77oCrnM1BCAFMkqJe3IUSKrBBQHiCSICBm1GLpCqQHi_F8p_gL4StHgWdUR0zfVVrmzjAZmH_TWR9o_7fvP6jSwM3zfa_o7UZV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با وجود اعلام اتش بس دوباره، اسرائیل همچنان درحال حملات سنگین به جنوب لبنانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129153" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129152">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unSaUbGEOhdvG9GMzMH7gkVup5gUukwpsD1F_ULPVd4bSb8aNkkOaAYccCDFlcPqm7yKIWjtXaVM8-tfz9cl4nUMT1P-6V7JF4WS5tg52Ns0c_5_HLFBKa8o1pclg9_BklIkeG8C47PPCdXMDktPh223qaOtSEEJbUJmrweLHRXX2KiJUx_RAAL0QvxR2bevdQRrN_GwAanzsQx7zPtdSgXzIWrAajGux6dRHAFa2jpPUt2r9LNG-t-sqWpFZOrTSnGl6NQxG-A1gvRgeh1XGHy_Wgyvrdw3VLWb8WL_pxL0eHNGUTdbnuME7e89b85QXyug30EHtgW82HqmSVEWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس به نقل از مقام ارشد کاخ سفید : بی‌بی (نتانیاهو) صددرصد با آتش‌بس دوباره تو لُبنان اوکیه ولی خود نتانیاهو و تیمش فعلاً نه تأییدش کردن نه تکذیب؛ کلاً سکوت گرفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129152" target="_blank">📅 17:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129151">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7aa6588e.mp4?token=nMY0LhSef7t32UtdYcpxMWSRyjDXskbnNibb0IdbYC9xnOJk_InIhGk3O1QmmAlryKI-LXc0zIBRDXGO5990hPxgu9yaYzafoVbG_CUHoi3h9rBWUWkVZ7XbWQUQ8PXeuccD6IMvVl9_Qn_-0KSgtq8Ii3zlmg-0esjz_O-PNEsoF42HEG1DtjCUBvW0RcOdvb0aNrJdZREAKUOllOY8a9lQbJJGmkdshBEm1IoCsaSWTJq4gS1wIjr2KeeO25NlOBrWY1Yty_nXO9TB9fuefK6g-tEi36-6fx3mxc1zGLeVPRDi1nIwkyYE1L78AxcNMewFOmhRGqAZrxpaff9ltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7aa6588e.mp4?token=nMY0LhSef7t32UtdYcpxMWSRyjDXskbnNibb0IdbYC9xnOJk_InIhGk3O1QmmAlryKI-LXc0zIBRDXGO5990hPxgu9yaYzafoVbG_CUHoi3h9rBWUWkVZ7XbWQUQ8PXeuccD6IMvVl9_Qn_-0KSgtq8Ii3zlmg-0esjz_O-PNEsoF42HEG1DtjCUBvW0RcOdvb0aNrJdZREAKUOllOY8a9lQbJJGmkdshBEm1IoCsaSWTJq4gS1wIjr2KeeO25NlOBrWY1Yty_nXO9TB9fuefK6g-tEi36-6fx3mxc1zGLeVPRDi1nIwkyYE1L78AxcNMewFOmhRGqAZrxpaff9ltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: از نیمه‌شب گذشته بیش از ۱۵۰ حملهِ هوایی به لُبنان دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129151" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129150">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f118f174c3.mp4?token=aFUGcyoT0nXRu0L8J5aTrTLqA3GRx4kOrNoh0p-37es8n366vgq2LlqCjgn1QrLDXuHaSTm5nCWdqQyiWzoYRNjxWC6aRFIbryxAaQLdS2CTkm3G1M8LFJtaaR_kXVLxvFHsHahz2YhjzN2sW5zxOLmRnZPgyyKFcBBZsYR2W1FBqrHisc1rmZyT9-gY7rfnPBipfPDi7hylq1cfg-8s0cf0q1HhN8qLwguZF04NGHSQu1nD_owQrPN-8N2J6osJq6wYT54dnnVkNfvh5cs9RFVJmqFLtETcm4x_J7ED8t8qIJcrzoZNYRvYX-Mvg1DfOmgolQLq1J5rExpbsb4qsFArOgJkM-lL6_Bv6Wf_lR1o4f0d2eaLVncvSSDQ9zAePTg3RgPqXctTpOIg9Gfzq0znkRiBJmunVzr7R4ieMPL3Vt3dxjbOVWfFs08znpd-3BJ6w0DrWeUdneIqJkP7CAdhQF2ypyAo4zJTgCNTEvof-UE8awW07uUHJAfUTGnLOZ-lTOmwum2O5SX5m0U8fJhwQBS_8zbrI0rbzZU9PVrDgWe13rzYodYmENOcKT_4oMH2c5pD4D0_aD5bHC1GYgRf5hGxKfdgq6ujVAloR-B2Kgg6MELVQLkTi6QaqjHKY8cy2N_i-gda6UI-gITsUBifs311glvZXGiwnGvVb0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f118f174c3.mp4?token=aFUGcyoT0nXRu0L8J5aTrTLqA3GRx4kOrNoh0p-37es8n366vgq2LlqCjgn1QrLDXuHaSTm5nCWdqQyiWzoYRNjxWC6aRFIbryxAaQLdS2CTkm3G1M8LFJtaaR_kXVLxvFHsHahz2YhjzN2sW5zxOLmRnZPgyyKFcBBZsYR2W1FBqrHisc1rmZyT9-gY7rfnPBipfPDi7hylq1cfg-8s0cf0q1HhN8qLwguZF04NGHSQu1nD_owQrPN-8N2J6osJq6wYT54dnnVkNfvh5cs9RFVJmqFLtETcm4x_J7ED8t8qIJcrzoZNYRvYX-Mvg1DfOmgolQLq1J5rExpbsb4qsFArOgJkM-lL6_Bv6Wf_lR1o4f0d2eaLVncvSSDQ9zAePTg3RgPqXctTpOIg9Gfzq0znkRiBJmunVzr7R4ieMPL3Vt3dxjbOVWfFs08znpd-3BJ6w0DrWeUdneIqJkP7CAdhQF2ypyAo4zJTgCNTEvof-UE8awW07uUHJAfUTGnLOZ-lTOmwum2O5SX5m0U8fJhwQBS_8zbrI0rbzZU9PVrDgWe13rzYodYmENOcKT_4oMH2c5pD4D0_aD5bHC1GYgRf5hGxKfdgq6ujVAloR-B2Kgg6MELVQLkTi6QaqjHKY8cy2N_i-gda6UI-gITsUBifs311glvZXGiwnGvVb0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: ارتش اسرائیل آماده و مهیای بازگشت فوری به عملیات‌های شدید رزمی در هر میدان نبرد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129150" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129149">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">محرم عجیبیه
حکومت هیئت‌ها رو کرده میتینگ سیاسی، خیابون‌ها رو کرده فستیوال
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129149" target="_blank">📅 16:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129148">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213cbd739f.mp4?token=v5MRrTRD8H_R9UsqTrU5sLtZNikCGzN4j1zP-q7tKItXcMicLC_d_7QFIHjHl_-h7fwS028jROgTq0G2NZ-8Vfc-JQltl2xh-28q94ooCl9ZIsBF-2z7qv_Mfmi3gOb8SkjYeVTu5OeuEYvq_4dtWTWBaDsocY2ZmJa0Y0yU8lMntGe4qBdasS4xmbXSZk-TbP1OYSGxqxZHPWIqGprF_wV5gieip8yOmq8MSAlMAjwLbLZohnKR0nwwdXHGiBj3CK2f7lxc4FrzPe5jDIrS9ag-nK1kddqyd1Yo0mxFfhP5hX90uT7Fv2bRz2T1CEUQDY39inZeaAMNXXYjIn4QxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213cbd739f.mp4?token=v5MRrTRD8H_R9UsqTrU5sLtZNikCGzN4j1zP-q7tKItXcMicLC_d_7QFIHjHl_-h7fwS028jROgTq0G2NZ-8Vfc-JQltl2xh-28q94ooCl9ZIsBF-2z7qv_Mfmi3gOb8SkjYeVTu5OeuEYvq_4dtWTWBaDsocY2ZmJa0Y0yU8lMntGe4qBdasS4xmbXSZk-TbP1OYSGxqxZHPWIqGprF_wV5gieip8yOmq8MSAlMAjwLbLZohnKR0nwwdXHGiBj3CK2f7lxc4FrzPe5jDIrS9ag-nK1kddqyd1Yo0mxFfhP5hX90uT7Fv2bRz2T1CEUQDY39inZeaAMNXXYjIn4QxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به نبطیه، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129148" target="_blank">📅 16:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129147">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی گزارش داد: اسرائیل و حزب‌الله پس از مذاکرات با اسرائیل و ایران، با میانجیگری آمریکا و قطر بر سر آتش‌بس به توافق رسیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129147" target="_blank">📅 16:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
حزب‌الله: هنوز هیچ اطلاعیه‌ای درباره زمان آتش‌بس دریافت نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129146" target="_blank">📅 16:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129145">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNiGPsqOI9HlSrbUSmrGlrPcRERq_tLkBs8FaHVJGmXCtGi7Af7tuEAKKPWbrHNXLDJLEIdXZjkaHbya1Xi0N13PhVZEWbC7wQ2T0mKDi_cdjy3xu5vsm3oFQrk1jDYe4w2u3zegXmbZSKTwiyflWTueA0zVoHNGSf95aim5QoJ5oeKJMpi5aQ7GbF4X3PLDrG-6obn6f_4IzXUhAy2qQmITg_sI_DQxgdCpqCp-NjmppFZSKIKmE4JSZnK3JTUnSvV5CcFZ4O1gIhlE1bp1l201C6iZ38q1E8TdJOenT5UyR28pMUwSW_yPHOA0mAtphEPri6K1CDPU-xs5Ql_lHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش تتر به اعلام آتش‌بس بین اسراییل و حزب الله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129145" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129144">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کانال ۱۳ به نقل از یک مقام اسرائیلی:
ما در حال حاضر در آتش‌بس هستیم و اگر حزب‌الله به ما حمله نکند، زمان جنگ از جانب ما نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/129144" target="_blank">📅 16:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129143">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: آتش‌بس شروع شده اما ما توی منطقه میمونیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129143" target="_blank">📅 16:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129142">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / خبرنگار المیادین در جنوب لبنان: همزمان با اجرایی شدن آتش‌بس ، حملهٔ هوایی اسرائیل به النبطیه صورت گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129142" target="_blank">📅 16:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129141">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / رویترز به نقل از مقام آمریکایی :   اسرائیل و حزب‌الله توافق کردن که از ساعت ۴ عصر جمعه به وقت محلی، آتش‌بس برقرار بشه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129141" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129140">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / رویترز به نقل از مقام آمریکایی :
اسرائیل و حزب‌الله توافق کردن که از ساعت ۴ عصر جمعه به وقت محلی، آتش‌بس برقرار بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129140" target="_blank">📅 16:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129139">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4030a7e818.mp4?token=ibQT4DVp9xHDlUMHciA0Ge6moc2_aSJT8jyPuSIThq8_mGXa8qHy3DOtzpaOqYyOMZVupvUJdQCRKW2xhFhKdilrccRIzPAbXZNEimq60gzkBPG7XE9m3X1bfDiyL4otQFrIN2Aoe9CHkttj4c2gJ4D01DvBL6aQDer0StHEZWpKmDFeSwHNBkkfbv6njNrn5wHHxz2dY1aM_Br4jxrsT8omYDGkXlMJOEWda7zv4OLj523EhtnBPlo5bS7-SEzKoV-a1O62sktqPK04Z_Ua_4_LL4DDXdFGGZIHodFpZMS30gZFHcrcr2yXn6df2_1dqt25F7JZWhNt7jthjvGRYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4030a7e818.mp4?token=ibQT4DVp9xHDlUMHciA0Ge6moc2_aSJT8jyPuSIThq8_mGXa8qHy3DOtzpaOqYyOMZVupvUJdQCRKW2xhFhKdilrccRIzPAbXZNEimq60gzkBPG7XE9m3X1bfDiyL4otQFrIN2Aoe9CHkttj4c2gJ4D01DvBL6aQDer0StHEZWpKmDFeSwHNBkkfbv6njNrn5wHHxz2dY1aM_Br4jxrsT8omYDGkXlMJOEWda7zv4OLj523EhtnBPlo5bS7-SEzKoV-a1O62sktqPK04Z_Ua_4_LL4DDXdFGGZIHodFpZMS30gZFHcrcr2yXn6df2_1dqt25F7JZWhNt7jthjvGRYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ در طریق Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129139" target="_blank">📅 16:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129138">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6PYMwsL6kCM9n4acSr0IyEDAlm2Dlz2CsKovTrDpZqEk5br0eUvecLJpIg_Mcjkw4FZU5Wv-BgDqTVqLQ-XKm6CPmVWV55hsty526XjbtNuWe_LqY8XPggQv91FxF7ebmXFwP7nVR_1nNGSCcDcHVbqGDQVd5K7slUPFcEtWn_kyfx2ZNcl9vaGpKi_PrEkmz5JhIfY8GVYhUFqRIUEJD9p6_uFi2D6Ud94OZ_42KglyGTXmS0D95rz22_DSxIlt-sv8gSPO0zd22a_DqBfXtcU9FiIsw7OLOGY-mGk0OmSbcOg6eJjOQ6IKGhNK-dSybVzxPJt6CNiH9raZYjrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : ما از روی استیصال نرفتیم سراغ مذاکره
🔴
این ایران بود که بهش نیاز داشت، کارشون تمومه!
🔴
همون ۶۰ روزی که گفته بودیم رو جلو می‌بریم، هیچ پولی هم گیرشون نمیاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129138" target="_blank">📅 16:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129137">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgNEXk5tsZ2k2bn4qipDrVYNaXk1UgmFSmcPEOw30n3mAA5g1vWYlkR0PqC7JjfEaj1fGmyom_Qo8aYngi8OAsMTpWaAr1geIE0BCH60M7uKeN-15hgb5cTGAqcqhLtO4rYYpot-LUQNwMyEGTzueyODPisgM4G2qLPZNuwpzZzTu916nUxkg760PRO7aoij5cNduR-N95mqI1fAXPd9lGgGYqSvR6lv8hrFsL9sZYAqKpFa55eUmndTv5uu4zTfM78kmGsIEnErw6YBSMoF8x65OJVtaocEWWTnWCeYsxESr3RZlSY5ZqzKnZQOk2bvmMxaflbNfhLJ2iELBZLvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : این جنگ ایران را به‌شدت ضعیف کرده!
🔴
دیگه نه نیروی هوایی درست‌وحسابی داره، نه نیروی دریایی، نه تجهیزات پدافندی، نه رادار، و تقریباً هیچ‌چیز دیگه‌ای
🔴
با این حال، دموکرات‌ها میگن ایران الآن از چهار ماه پیش وضعیت بهتری داره
🔴
باور می‌کنید همچین حرفی بزنن و ازش هم جون سالم به در ببرن؟ بعضی‌ها چقدر می‌تونن احمق باشن؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129137" target="_blank">📅 16:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129136">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_Mgfi3FHR6jj8PJdBQX_k2PmEbkEM7uitevIsBClHvOWHI50hPX4lYOhdi8_b5kWoGhqtlosLpr5tib_eq9XTDgicbZ3vbFtskhmr2N3wYfi6Udhu2ZX_1S-UIxNaBTfBhXUV_jqToCfv8PxLDse3L79B7DMvY1aSmXxurrz38IZ-kr7YdbKZImPeJt6e7UE98yY8H-J3UrJfj49xDKhGvCYQ8bKjY7B7VKu6ETWxv4F6dschy5EKZ_S_iedeOZkWpPXFCfieCuZFegLyI-V7-Toh0HqPYket8STINzk2OQOrLgiFx5te_qVF4V3L9fN37Gnpz83v91vmCxmRs4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش عراقچی به اظهارات وزیر امنیت داخلی اسرائیل:این‌ها رجزخوانی یا اظهارنظر یک دیوانه و نسل‌کشِ بی نام و نشان نیست؛ بلکه گفته‌های علنی وزیر امنیت داخلی رژیم اسرائیل است.
🔴
فرقه مرگِ نسل‌کش که مقر آن در تل‌آویو قرار دارد، تهدیدی برای تمام بشریت است. این جریان همه انسان‌ها را تهدید می‌کند و تنها هدفی که دارد، جنگ دائمی و بی‌پایان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129136" target="_blank">📅 16:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129134">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lb1pxXe8Ex5cFRLfPgq7SzImLeF6NfKDerBXuHjUlH3-rJq9phiIee-t0CyKpxft2HiQ-jUS-TmHhxtXhpGb2HWhBIRnUMU4FpVNXqRw71uSlv5MGUDY3dNadldymN8GSvt98v3cl_Dxh2Rv4_p04cm3Km9D2wQX9lFJ1eQvDB68m4m-jqZcfnXYt4TAUeywSCCJRiGlJJj8E1yWxnvinjXnX9XvtgN09xj_o8ZsIZI4bjMBaVbdB_4nc2DG0wRPk8FbFpSETsmE-ggQn5vnx0JHC1PwMpY6unUKNtHz7ZE7FYXcnlvShD7bqTC-3ipY1kcayIjNdfUdTH3wz2bkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PAZ-Lq-8w4lvZh-nsWoP-XYwdZvmPDAPaDvQ2TuVzBdoFNBbNXPdqUrbgahqzGSAlUr3nypnIAjOmSMaugSlJn-Kh868fUsdpv3PxTHW8uKCevDp6AXhLWcohgGWSt4lccyKxihHEsv3Q46Xjq245GQ4Hcxijb0OegBMjmZhiS-jgYer4TEF_oyDRuhXGMeTV8CPFxWPd2afsN_44vpNA5Cr4BlQJ_897Hsyr-WGW4w4tzvPAdfNDaW3HVdNKI-jbrAQWLGkUfT4NXNbMCJ2H0yUSXmyzwSajOok7a1chvQXoDazPlMxa1pnHvSOZyCdviqulIWuIQw0TSItNU9UEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصادف شدید کامیون با پراید و فیدلیتی در مشهد
🔴
۵ نفر دردم جان باختند!
🔴
از پراید چیزی باقی نمانده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129134" target="_blank">📅 15:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129133">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
گزارش سی ان ان، ایالات متحده به ایران «به اطلاع» رسانده است که اسرائیل حملات خود را در لبنان بیشتر نخواهد کرد.
🔴
یک منبع گفت: "حزب‌الله آتش‌بس را نقض کرد. اسرائیل موافقت کرده است که این آتش‌بس را به ایرانی‌ها رسانده است و این وظیفه حزب‌الله است که متوقف شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129133" target="_blank">📅 15:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129132">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
خبرنگار الجزیره از حملات هوایی مجدد اسرائیل به شهر النبطیه و اطراف آن در جنوب لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129132" target="_blank">📅 15:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129131">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mb5ICu34TgFV0QC2GUhdgLM3LiY2dnUE9AHPuRkHAGwSPFmFbGI1aYaAmvBRZYG2yA36B3F_ly-EmHMFx63hRfNn6lZjXuyOyvFHKDBpbm52g2_HzZlE_IDh7d5AjV7aCCbV4SNjgK4br5kXqfE3pFvyIHwpJpb2ePULXYjFmPc90Osj8oCKVkXp2iWNqhi-Ba8wlxWG1lI443Y7uSxLP50nsPzvsRX8zcnVxMzhIPSLXxqO6mL1bnjisWhEjT-0Q7b142SNUzvojcCKxr9TVGOGkxI2-z4qOsXeCuNQ_uo49XkjoNXA9gfHiNNVuY1M1BMagc6zUKKVk0qkIbA-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفیر آمریکا در اسرائیل از حملات این کشور به لبنان حمایت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129131" target="_blank">📅 15:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129130">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ در پاسخ به منتقدان توافق با ایران: برخی تندروها دیگر محترم نیستند
🔴
من یک آرزوی اصلی به‌عنوان رئیس‌جمهور دارم؛ هرگز نمی‌خواهم به هربرت هوورِ مرحوم و فقید تبدیل شوم
🔴
بعضی از افرادی که قبلاً به آن‌ها احترام می‌گذاشتم، دیگر برایم محترم نیستند؛ آن‌ها تندرو هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129130" target="_blank">📅 15:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129129">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرگزاری تسنیم :  تنگه هرمز رو تا عقب‌نشینی کامل اسرائیل از لُبنان مسدود کنید - تموم مذاکرات رو لغو کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129129" target="_blank">📅 15:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129128">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
معاون وزیر نیرو: متخصصان اتمی روس به زودی به کشور بازمی‌گردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129128" target="_blank">📅 15:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129127">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_sOUqjVFjUUepv5dqgXaxnk4Go1abYPxIPtBqGZl9xoOB3Wj6O1pFtaB4X6xgGjhRyJxqCOdCvURLVK3sW1LWcy4oaITOO4tb7eu_PQqJFgrkhAx4LVsKFRydQmbSXdHglB1zYa8WKip86LWCv_ubwVdRqtv5NklCcjqTRFGL4ISNaUS8ZYP9cLKHTMXRlB50de8yega6MxdRmR6cU8yuHAcWSBMOngB8hB9q0dwLMyIWtskmHoO1safqBWx1W_d4-pdvqlx5AsM703v7Q3TNTfKFs_q_rDredfcOpRZtpHXMdFQbDbkBlqsGyzbUXQ8RaWA3rjElqxJTj8VofKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی شورای امنیت ملی: دولت باید همین حالا و از لبنان شروع کند و نباید اجازه دهیم مردم مقاوم جنوب لبنان مورد قتل عام قرار گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129127" target="_blank">📅 15:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129126">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری/نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/129126" target="_blank">📅 15:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129125">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
خبرنگار العربیه در سوئیس: مذاکرات بین آمریکا و ایران ظرف چند روز آینده آغاز می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129125" target="_blank">📅 14:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129124">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc08f96bc.mp4?token=p-1pbZwSsN0Dz_81KFYR3Om9LFnIUG0P8_ZSJJwz6DP_vGACFyEaf5A0090JecyOZaoQzLRQGQxijVPtW2t_-w9vMcChP0KIelZibqIh6ScWopdeijSvslE53OVW0GeG0zMWOhtUDhvCtskXa5TcYjGiTsvUMV6liBOwx5a8KBoPsVmL4WgINu371VayzfOVf4spQOZzpCE85xGELMrUGn6dhVLlfr0Z7dNP3kpw6GNBiHyK3FBtUkxHiNXw2LA3TqazQtf_5AKdMtQZVqaSNbaXQrgPo7LwWZ4PZiRR-dZdIPobzpVD1OmDb3AHkYtQ2gNN8jC97QFNdFyi5x2CKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc08f96bc.mp4?token=p-1pbZwSsN0Dz_81KFYR3Om9LFnIUG0P8_ZSJJwz6DP_vGACFyEaf5A0090JecyOZaoQzLRQGQxijVPtW2t_-w9vMcChP0KIelZibqIh6ScWopdeijSvslE53OVW0GeG0zMWOhtUDhvCtskXa5TcYjGiTsvUMV6liBOwx5a8KBoPsVmL4WgINu371VayzfOVf4spQOZzpCE85xGELMrUGn6dhVLlfr0Z7dNP3kpw6GNBiHyK3FBtUkxHiNXw2LA3TqazQtf_5AKdMtQZVqaSNbaXQrgPo7LwWZ4PZiRR-dZdIPobzpVD1OmDb3AHkYtQ2gNN8jC97QFNdFyi5x2CKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش صداوسیما از آخرین وضعیت تنگه هرمز
🔴
تردد کشتی های تجاری در بنادر ایران از سر گرفته شده
🔴
در روزهای آینده نفت‌کش های ایران به سمت بازارهای جهانی حرکت خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129124" target="_blank">📅 14:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129123">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d85acc4b.mp4?token=QjAMwi4JI4JkL-nUWG-iJPBtnbDLJourhvLf574aY1RAKdC__clAEwX0B19iFTgSGDeE8rTgZFU_Zz3NPKFipxekAWtPc1J8mIDm5M_9lL84XXUxl_6fd3Gxjr0JDNbwu6MIzQXqRAmGVdgiBf4d_4DSw64ClJLKI1R3bIgI6WADm60ouMAMcF6xz-uQxUwA8-G_ipvUgCau1v7eq6FxV6gNCvXhhdv3jN4SkIWmYaSlopZTyBf3NLhdXm3LJocGORh9pRgWEkwj41xd2tr0kenQG-riM-OcVx_zbdW7LCvezgCBBlfbWyaBJ5Tq1fqiMVX5Oz4eqzzsFgqQv5Ju4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d85acc4b.mp4?token=QjAMwi4JI4JkL-nUWG-iJPBtnbDLJourhvLf574aY1RAKdC__clAEwX0B19iFTgSGDeE8rTgZFU_Zz3NPKFipxekAWtPc1J8mIDm5M_9lL84XXUxl_6fd3Gxjr0JDNbwu6MIzQXqRAmGVdgiBf4d_4DSw64ClJLKI1R3bIgI6WADm60ouMAMcF6xz-uQxUwA8-G_ipvUgCau1v7eq6FxV6gNCvXhhdv3jN4SkIWmYaSlopZTyBf3NLhdXm3LJocGORh9pRgWEkwj41xd2tr0kenQG-riM-OcVx_zbdW7LCvezgCBBlfbWyaBJ5Tq1fqiMVX5Oz4eqzzsFgqQv5Ju4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهر نبطیه در جنوب لبنان در حال تخلیه شدن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129123" target="_blank">📅 14:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129122">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
حزب‌الله: دشمن اسرائیلی به نقض آتش بس ادامه داده و با ارتکاب کشتار و تخریب زیرساخت‌های غیرنظامی، آن را تشدید کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129122" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129121">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / نخست‌وزیر پاکستان امروز در توضیح درباره تماس تلفنی‌اش با همتای ایرانی گفت «رئیس‌جمهور ایران دعوت من برای سفر به پاکستان را پذیرفت».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129121" target="_blank">📅 14:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129120">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOYIM5GDERvrCLDNrtb6wzK87kFG0uzAG4iTFRCW51MzzUWgmVcvOEjV8ajpfidaQNrVVQdKseipk4TxLj3bWY1KgST_VCh9GJ7ruZBA45e-V0QGkbVPtFNwjK1i3AteI6d61J5l5WkJ_uYu_qBXJOJQRQH0eTTfsnjNq-XOonv_Beu_Lqx-7RuFhPu4X6UjLGhPjIWElLpfoLkWZPu9jb82vJQqmRbyLx1zhj6px-NxCm6eLsNxJ3ZchA5ywMPJ2brq0MEcg8Sk1MpppJe7WnbYkVzV9JMS_JW6xufi_8l7Zb1pwP02OAy26DfHYSojDj7LOCUJb6SqN0ZAW2h6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو تیم مذاکره‌کننده: ترامپ به تعهداتش عمل نمی‌کند
🔴
اسرائیل به شدت مجازات خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129120" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129119">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orMRMUsk6HSoUJEcfsQVRlFqUXmJvHcMmDhk9YQMFXCX98SE18dhOeCeqTOWoIh7EWeVbV9Jb3Fj97KzDeUFp1WEquaDKeQDSO_tfmVrJMLHOEOCU4t77jh6oBXZdK6jFQyYsWv3E9Em5KH83SnLeuX5K5uqS2mmxKsMApZLNgUYF6jr_NIPZXM6VgYDdMxDC1_RF-xlV5PU8-gBTcfXdT3kSsnBE3mERVpLipruRU5j3r7l87Rs5jX9VqstwjJFD9XpMbTVnf19vkKUjN-b67X45yxa2yhpCaEc85Mog2rAwQJRLptssWhFbowRuL3UNcMJMVhmXRHXWZn7me6Lgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج فارس: با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129119" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129118">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / گزارش‌های اولیه حاکی از بسته شدن تنگه هرمز و شلیک گلوله‌های هشدار به سمت کشتی‌ها پس از حملات اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129118" target="_blank">📅 14:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129117">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30950fe2bc.mp4?token=YZSsSIaqm1rv-BJ10XjXSQ3VgTKwF2zOSg5kwtqG81lfhlB4mvrk6EaH-zyACeSkMXXMpSjUh3uscNmJxqUTZecgQxHGO28aO0EYWKjYAxdMWRye7fMRvKH5epJSwR21KfLUd1wcKn4t_AQYZsIirRQMUUVCP_PhfptkMsz8tlirnb3VqWHWCUw9jnKCGZo8Fd7hIxSIH0n4qWLEdmtcXq7e2Vw_7aVTQwytM9nKVKI6eJ8F43v1Br37bZS-hhgBSKspyy2q6yhzswzTPg1Cjnrgg5arYggoRVL8eIUK63jDFtKngvH6w1SClkVel_XURQMHzTDQeqjWGYJXs0yX3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30950fe2bc.mp4?token=YZSsSIaqm1rv-BJ10XjXSQ3VgTKwF2zOSg5kwtqG81lfhlB4mvrk6EaH-zyACeSkMXXMpSjUh3uscNmJxqUTZecgQxHGO28aO0EYWKjYAxdMWRye7fMRvKH5epJSwR21KfLUd1wcKn4t_AQYZsIirRQMUUVCP_PhfptkMsz8tlirnb3VqWHWCUw9jnKCGZo8Fd7hIxSIH0n4qWLEdmtcXq7e2Vw_7aVTQwytM9nKVKI6eJ8F43v1Br37bZS-hhgBSKspyy2q6yhzswzTPg1Cjnrgg5arYggoRVL8eIUK63jDFtKngvH6w1SClkVel_XURQMHzTDQeqjWGYJXs0yX3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اکسیوس: آیا می‌توانید اسرائیل را از حمله به لبنان کنترل کنید؟
🔴
ترامپ: بله. آنها احترام زیادی برای من قائل هستند و همان کاری را انجام می‌دهند که من می‌گویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129117" target="_blank">📅 14:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129116">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نتانیاهو : اسرائیل تا وقتی لازم باشه؛
برای حفاظت از شهرهای شمالی‌اش، تو نوار امنیتی جنوب لُبنان باقی می‌مونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129116" target="_blank">📅 14:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129115">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نتانیاهو: ما حمله به سربازانمان را تحمل نخواهیم کرد و کاری خواهیم کرد که حزب‌الله بهای بسیار سنگینی بپردازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129115" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129114">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaJ9bPCHq7Z5fot8jG6hJ0NUrFslbdD_EiXTxclQi3wn0NVHVFhG13jJAXrIrsfj7ECLzNz_1jEIUbn282I2Plz9I11NcLJV6CtpXE3-eGXnt1nCBwxbxVIRgPnfCIAZlgZkwqkWi4yMcfhAFsI_ut-jSvMQ4JouWpRhooWBOUqmZ8zw7A-Bhi3ezF2aR4XE4P-AICts9ZyHh_aVl1Z5EQ1kV3lel4IfCrCrika6N7QgBwjWMIP2HWY0OafpiT2kTtAZCCPGK06MPrICwy7xbwzTR0oErJqvxdcnJorshysKwneyeYPdOXQyb9zF_BiCvstrvqhCrLnFVLbls3zRSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل هیوم خطاب به ترامپ: می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی.
🔴
آقای رئیس‌جمهور، شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد.
🔴
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129114" target="_blank">📅 14:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129113">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سایت ردیابی کشتی ها، کپلر: ترافیک کشتیرانی در تنگه هرمز رو به بهبود است و دیروز ۲۵ کشتی از این تنگه عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129113" target="_blank">📅 14:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129112">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWgTFWAATHBYbnejMj_nZpqUEpR6KAEyeNet2AEZDMQjPcjY_nxH00PVgHVyO7uPsJDYNAgiT36rjChrDtiP9yRaj6WtTEcg42iIsNOvU3pNXZZD3c02tj-6r9jnF7mA3n059XswupLN5ZBl_fMYE1m0OOxPOl53I8nffWe0vBA6p2omt7zV2N6NOiNG287LBEj4TmoCan9rNsLCrT8uNx97Ytd0yf4ePKm-dtpSIhAYSO1qGR9jFD_apkZM_PLSws3V_4Xn3bNuVpCsqy_DzkOdXaoJUEMb58yreK9swsScF1XFEYwMQVVOhPFMoFgSwQSvtC4debGbtnN1jW5cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش ثابتی به حملات اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129112" target="_blank">📅 13:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129111">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ به اکسیوس:  اگر مداخله من نبود، اسرائیل له شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129111" target="_blank">📅 13:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129110">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3KGcB0yc6kJLR5jiHM0ZovIPPWj8JZOpAqALRT_W-u9tCfGf_Xhgd5_tapBpTMmLPzAkhZ54n-gMjmokYDNhuSdswmOEiBawchgipZZbMoskUWx5Oa9f7gKQNB6JKvjgfYQeEH15KjfWG0v9QUKUqVdH58-SgvIMtYL_v7yJt93hH7NA7gpk8ddw7Ss8HrxEF4cuEtoflK3o3dLkqcOF5RYJgWSANz0GwbiEOxHe5urzNHBZ4aclAEjg6PfiEEVjoLLxMlO-ZMhjfrOVEOl-IW3iyOOym-MN5KSZFHu2NCJwhigyUMuhAGgWuuB6s08NQmd--6OVfmlgcnauScrMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز نوشت: در طول پنج روز گذشته، جمهوری اسلامی ایران حدود ۱۸ میلیون بشکه نفت خام صادر کرده است که ارزش کل آن بالغ بر ۱٫۴۴ میلیارد دلار برآورد می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129110" target="_blank">📅 13:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129109">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ به اکسیوس: رابطه من با نتانیاهو خوب است، اما باید او را کمی منطقی‌تر نگه داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129109" target="_blank">📅 13:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129108">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر امورخارجه پاکستان: هیچ مانعی برای آغاز مذاکرات سوئیس وجود ندارد و مذاکرات باید ظرف مدت ۶۰ روز به پایان برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129108" target="_blank">📅 13:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129107">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قالیباف، رئیس تیم مذاکره‌کننده جمهوری اسلامی: مذاکرات با ایالات متحده همچنان در چارچوب «خطوط قرمز» تهران باقی خواهد ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129107" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129106">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: هیچ مانعی برای شروع مذاکرات سوئیس وجود ندارد/دلیل تأخیر در مذاکرات سوئیس مربوط به مشغول بودن مقامات ایرانی با آیین‌های ماه محرم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129106" target="_blank">📅 13:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129105">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: دقایقی پیش زیرساخت‌هایی متعلق به حزب‌الله را در منطقه بقاع را هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129105" target="_blank">📅 13:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129104">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ارتش اسرائیل: بیش از ۸۰ نقطه تو لُبنان هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129104" target="_blank">📅 13:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129103">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شبکه سی‌ان‌ان به نقل از منابع آگاه اعلام کرد که پیش شرط ایران برای شروع مذاکرات در سوئیس توقف درگیری‌ها در لبنان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129103" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129102">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bd4028ca.mp4?token=pLyuXW8ty0H2y_ISVrOvo-Npnq5Js4q-8RSAoXD0ogWMn4RrriEVAzsAsLMTO1-mMUdoxPiJxnM-fPgaCY2R7tiQw-M2er5dvNNleZji6_bZqTHFQgNiaAITb_kvcgsU8y0GRZsHUI4dgC0iCIOm-ucWqCQfZJAvc5g-8MrX1RREJtIhd1_uFFvMa7hiSe4_5ATnQSjccJZqrIy4nrGyZ-1fzVDdY5Yj5VZVT189To1CN9h8bgC-7-HvuSvDngh3Y8jWUyly1KJBmyrGphBEHxc0pUTal4k1fSD7URJ-SnFT7v3aWz0RcsF6Xn38d80e43_jHalyF4FkvKRV4d2ELA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bd4028ca.mp4?token=pLyuXW8ty0H2y_ISVrOvo-Npnq5Js4q-8RSAoXD0ogWMn4RrriEVAzsAsLMTO1-mMUdoxPiJxnM-fPgaCY2R7tiQw-M2er5dvNNleZji6_bZqTHFQgNiaAITb_kvcgsU8y0GRZsHUI4dgC0iCIOm-ucWqCQfZJAvc5g-8MrX1RREJtIhd1_uFFvMa7hiSe4_5ATnQSjccJZqrIy4nrGyZ-1fzVDdY5Yj5VZVT189To1CN9h8bgC-7-HvuSvDngh3Y8jWUyly1KJBmyrGphBEHxc0pUTal4k1fSD7URJ-SnFT7v3aWz0RcsF6Xn38d80e43_jHalyF4FkvKRV4d2ELA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
چرا ما در سوریه در طرف مقابل هستیم؟
🔴
چون باید آنجا باشیم تا از خودمان در برابر آنچه در سوریه می‌بینیم محافظت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129102" target="_blank">📅 13:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129101">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c80f50a64.mp4?token=JoXQP90qShE7SWlTaJjt9m3TtJtFnrzDxPy9hHfN4dbdu7UrjjW_Rn1eDujmeYKyYRd4K8Q8fCP404pOKg14okotkViuF3sDjUjXoqHkd3OTP3Qa7NhbMVwJIERcGOAXruHQ2zFcbMeaRyILinRfjOeLKBDiQtH8o7o3SW61YGVAcqYLRJmoYQMsL30ipNgK-AkRnYGLYInmUs1UeFKKuJUWqDRYo8wj7Xq_TqgB8yDFyei73ReHMk5UaeTIZdhhoXhsSRZNamP4GGCMKFAgSz8hTU0jBZjYIuv3P2dYIiVyOQzSfAriXWXFJMHzWhpQrdJ-ig0GkqXVVI5ltAxq0DkFdNPsXCytM-huPzORuOlMETXtN8Sd5Hk0PbMbL2U3YALjD1En6L6WpkEWMtRbK5AOTRifiU2o8_egLV_YgU692xQRG9v7z4rwL_dlVdCm35iMOHpkuG3eYVbTmnc5mgcUquTESkKLnCsBJSs4e_VUQyxQokzom6OUsO9qi6XQLy99DHbJwjrzRXhfmgOMs5HuhvTN4qBDWBURpCRG5wsmmM51z1ylgr_7OT-tQu3oTd6YH8DuSkTkNK6SLVtFN2o8azyncTjoS6SW9HHElkiq8-52U-MKaHTAhKioOdYgIHDe4FE-NeXsmHo6XT38za6iO8UmWFgVZ9vRb7BSChc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c80f50a64.mp4?token=JoXQP90qShE7SWlTaJjt9m3TtJtFnrzDxPy9hHfN4dbdu7UrjjW_Rn1eDujmeYKyYRd4K8Q8fCP404pOKg14okotkViuF3sDjUjXoqHkd3OTP3Qa7NhbMVwJIERcGOAXruHQ2zFcbMeaRyILinRfjOeLKBDiQtH8o7o3SW61YGVAcqYLRJmoYQMsL30ipNgK-AkRnYGLYInmUs1UeFKKuJUWqDRYo8wj7Xq_TqgB8yDFyei73ReHMk5UaeTIZdhhoXhsSRZNamP4GGCMKFAgSz8hTU0jBZjYIuv3P2dYIiVyOQzSfAriXWXFJMHzWhpQrdJ-ig0GkqXVVI5ltAxq0DkFdNPsXCytM-huPzORuOlMETXtN8Sd5Hk0PbMbL2U3YALjD1En6L6WpkEWMtRbK5AOTRifiU2o8_egLV_YgU692xQRG9v7z4rwL_dlVdCm35iMOHpkuG3eYVbTmnc5mgcUquTESkKLnCsBJSs4e_VUQyxQokzom6OUsO9qi6XQLy99DHbJwjrzRXhfmgOMs5HuhvTN4qBDWBURpCRG5wsmmM51z1ylgr_7OT-tQu3oTd6YH8DuSkTkNK6SLVtFN2o8azyncTjoS6SW9HHElkiq8-52U-MKaHTAhKioOdYgIHDe4FE-NeXsmHo6XT38za6iO8UmWFgVZ9vRb7BSChc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
یادتان می‌آید حملات را؟ آنها وارد می‌شدند و بیرون می‌آمدند.
🔴
ما وارد می‌شویم، نابود می‌کنیم و ترک نمی‌کنیم. این کاری است که اکنون در لبنان انجام می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/129101" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129097">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lklWqItaPGpAL6mNQUc2gWSNKDAqEUM6GFFcFSEwl8qiMjQJElZqkudf91hP3uS5TPJIADcNVNe416J63Ml9Hz4E20-3fE7t92tnFpI1F3_oWPa97eEKmywme-RgqT_SWMJtPEf6Kc3JoQscDt-NXpR_s6Ka4PUfWEWRJ7KM8Kn6jJ5QNY-fkj742j3GG9kcli_jImqrJPxjP3w62Cz3o9XcaPM18Eq9riDO75M2ZLWewrxT26J7eJwdZljvSMHIKu0592mJqxa4j1a7iQXzeTDo0O47qZjMUPzJEXkPOEvcGRDTlifFpLWAaAdhJZklRW7NZAiWEKtpIHs9BIN57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2I56qfH7k_7VzTAuXv6dEC4OMyRN36BBEIR9yeCOxA0Klvjk11gnHmkxS3Gk4lShhb-NGYSvdVJh1WXjoyNbNTeTrF93C5eFZ30Ac3Gz7iSnevUQPyDUX4QwD28xUbic2FvFuGh0ynH_0Jw95OXkSfcpDY_p9-f6eRDEKyxq9ZcIKl5JYtQq1SSbua9toea1cy39pCRnmTEC9N-CYUCgQG2EnAmw1d75JtOgniDKY7b8CNI3T6tquCN5hhSxwbeS79xfZXwNeXSgLc3JTD1JwoGgmgvTXc-AC4XDFHJTrl_EmXcDOfWsKmQ2F4WRBLoPcDBdP_cRVgXoVEsOpGnag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5lnsA7NHK9D5edMvzHIF17KKpGP89HZ7yvkwNzY-riWKpWgdXbkLtiWPbtJRlTvCVfBLbg9kxdBEneILJ0zXqaXwG7Xd0UGBJmJuw09801-0u2zfWJ1kyv5CNi7v96__mU8mlSwYEJ17l1Hq4zEIY0T3dkO8bWCT7fHcXD9-W8cWjuOWw3UoK3-hTLFB4D5JLG-1fEwTAjf7mVsloZ06ls2qk-NRI4jX8fSHleNnJdRXV9mRISRRzKN3t1wYdrqbPXwlPagocwDXnAQNoL5lSRXg0X3xbnR0Hg2eAZXNsh-j9JAAzPQbem4pw2RcgD7b0bsYKqhfsb1ZepZADUk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJh1E-RKef3Q3GWmrDLp9u_HmcwEyhCYj7oc2_w3YAvgm2af-hg30UhAox0oE_6BaNg5hhJSx6SvvgYmj9Fj7KNV5U3khsmb7-MKR2XOlFqqWeuIFFvjd2UBOOou2bjThEsab32ZDqiz8ODhVF3NnNcTt8FibodEm4Tg2nMtv75UNFVwz236S8WFu8NPLHz7JkhiIcHPztH_dl_NDSL5AvyMxinH3hrLIkd_HeK_MQBGgIHfWJonD7lyB8_JzMcJwUshy452y86a2mVe0W950LYk6IgdCFiCj2YdmbMiJEUnGJPhZ-LcXLjN2wjBuhlqRMkKTeiuGbcKerT7xE8nlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات شدید به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129097" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129096">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بعد از پیام دیشب مجتبی خامنه ای دلار ۱۰هزار تومان و طلا ۱میلیون تومان گران‌تر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129096" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129095">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnOXNDF62HBJxZvSWMR_4ideFcdrns9wcfhEJcr7GOQoMJOxQgMfVQHKQUVop2cdf_uyiJy0E7lKf66rVo8Tc5ZqCiotXagM-YUGKQQlJVB8G4XvmRdYgE6iR6Lx5wo0QLCjWXQarBIR0qiPhL_OO29lgKjIIfHkkugCldB_DCm37ZPx3mQQYTPQkcU_NB2xxnHpOeZGuMoY-FKAIYQDk_DMvt7RmJUe-n_5iznYi22X-cZ0jEBSYKAYol1bWtDjijkxlr2ky0Y9c5V1F7OsFpi2np5_9yfdwQXlUv3ApP8qFwUegyq-QNWAFFPknXFZ8CHEi7aKTyldWRnuKA5AdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسموتریچ، وزیر دارایی اسرائیل: «وقت آن است که با آتش سخن بگوییم. دروازه‌های جهنم را بگشاییم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129095" target="_blank">📅 13:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129094">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
در لبنان، ۲۰۰٬۰۰۰ نفری که در «منطقه امنیتی» زندگی می‌کردند، بازنمی‌گردند.
🔴
هیچ‌کدام از آن‌ها بازنمی‌گردند.
🔴
نیروهای دفاعی اسرائیل آنجا هستند، زیرساخت‌ها را نابود می‌کنند و روستاها را ویران می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/129094" target="_blank">📅 12:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129092">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19bde11aa.mp4?token=El21yvjrrVm75EwO6zoJrDvBR_R86VaCuolCJbmbcTm7qLZgppEP4iQ9-BGRq9USDnYjV1eMWyWdSbJr2iGXNtf9DkaQVTm7KW9wnQ9Lje4qynM6wmYPoQMyPm9NaJSq2S58YL2GznnAFG6ETBO2h2vhfpV3m1y9lXWpn82mEe_CQZbIgsUX9VKuhT5NjPaKBNtVWI80dlth3nIh6c1l2fHASedP-qrl__ELY2Is78knPd545KrFK6aX3pb6PYe0p6eRK0a1n7o9FnJPvFa8DqzQhNASNXKb-GHJYthlTj2V5Kb9Vzifm5_IE8AJJ9akt72mRwb-OoTtxgwvffATUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19bde11aa.mp4?token=El21yvjrrVm75EwO6zoJrDvBR_R86VaCuolCJbmbcTm7qLZgppEP4iQ9-BGRq9USDnYjV1eMWyWdSbJr2iGXNtf9DkaQVTm7KW9wnQ9Lje4qynM6wmYPoQMyPm9NaJSq2S58YL2GznnAFG6ETBO2h2vhfpV3m1y9lXWpn82mEe_CQZbIgsUX9VKuhT5NjPaKBNtVWI80dlth3nIh6c1l2fHASedP-qrl__ELY2Is78knPd545KrFK6aX3pb6PYe0p6eRK0a1n7o9FnJPvFa8DqzQhNASNXKb-GHJYthlTj2V5Kb9Vzifm5_IE8AJJ9akt72mRwb-OoTtxgwvffATUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل علیرغم اظهارات دیروز ترامپ و ونس، همچنان به بمباران لبنان ادامه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/129092" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129090">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278b037b53.mp4?token=ridfseyNmcguDCaD_GEVLiAcFf2O9Nvt1iLTsKpyudqLZCdMDPOzvJ-JAHuk8DPD5zcGAH_dQhDlHSW5gTscI0FbdaJ2aso-KY8ZPbg8ZUWpGKFZTDGUVfsQodYJDyGJGRIIjChQzz-E1oggZ5d4o5VRyMQh-0zag37d20RV2YIqk9gfao_i00DkOj8NyxMQdUTD7GjfA5NxTaqIePDC5sp9mqjIoW2t7bGkVFn0y3jMtVJ5XuMhEadx2Wha9TnINGvWv1Jdg2lmFeEpyQHRSGyVIObiAN3rPrn2EnZ1AI1IRS_y43GInmZX7QyqrJIBqDLCtHysH8MqX-M5b7MwWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278b037b53.mp4?token=ridfseyNmcguDCaD_GEVLiAcFf2O9Nvt1iLTsKpyudqLZCdMDPOzvJ-JAHuk8DPD5zcGAH_dQhDlHSW5gTscI0FbdaJ2aso-KY8ZPbg8ZUWpGKFZTDGUVfsQodYJDyGJGRIIjChQzz-E1oggZ5d4o5VRyMQh-0zag37d20RV2YIqk9gfao_i00DkOj8NyxMQdUTD7GjfA5NxTaqIePDC5sp9mqjIoW2t7bGkVFn0y3jMtVJ5XuMhEadx2Wha9TnINGvWv1Jdg2lmFeEpyQHRSGyVIObiAN3rPrn2EnZ1AI1IRS_y43GInmZX7QyqrJIBqDLCtHysH8MqX-M5b7MwWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهر نبطیه در جنوب لبنان به ویرانه‌ای تبدیل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/129090" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129089">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd73e104fd.mp4?token=sae8ItR_ruK8JPIqnGWh_HtLZ-0rBGqW-BucKOZRGwcE7J-IebvQQmsMMyfM0Obp2wKcUfS6hkV3LZaj2tEUN1qDNvwGbbkCBaH0EcXkCvzqg3v3EnOSy4JCgwTK5hxZHxhngpNkfhd4N2HkQpehOInyorROae1Y_cmE6gdx_86RnZxcigPNe71iQMLlYaeRpOx3S2EOIIfithTOxTAOwi3lVwFjY4kvFs_VnrTESZoLmr3_9mpg9roMZbuDk9MCLLJFCD18Q4507CQDCsYUelbGURjDFWF7t_IXDxx2sDbiux8repq9ttBab1EgmGeslN7DRhh9a0-pfp_qsl0dpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd73e104fd.mp4?token=sae8ItR_ruK8JPIqnGWh_HtLZ-0rBGqW-BucKOZRGwcE7J-IebvQQmsMMyfM0Obp2wKcUfS6hkV3LZaj2tEUN1qDNvwGbbkCBaH0EcXkCvzqg3v3EnOSy4JCgwTK5hxZHxhngpNkfhd4N2HkQpehOInyorROae1Y_cmE6gdx_86RnZxcigPNe71iQMLlYaeRpOx3S2EOIIfithTOxTAOwi3lVwFjY4kvFs_VnrTESZoLmr3_9mpg9roMZbuDk9MCLLJFCD18Q4507CQDCsYUelbGURjDFWF7t_IXDxx2sDbiux8repq9ttBab1EgmGeslN7DRhh9a0-pfp_qsl0dpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.ما از «مناطق امنیتی» - نه در سوریه، نه در غزه و نه در لبنان - خارج نخواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129089" target="_blank">📅 12:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129088">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
فارس به نقل از یک دیپلمات آگاه: ایران پیش از بازگشت به مذاکرات با آمریکا در سوئیس، خواستار دریافت تضمین‌هایی درباره پایان یافتن درگیری‌ها در لبنان شده است.
🔴
تهران تأکید کرده است که توقف خصومت‌ها در لبنان باید مطابق مفاد توافق امضاشده اجرایی شود.
🔴
میانجی‌ها در حال حاضر برای حل این موضوع و رفع اختلافات موجود تلاش می‌کنند.
🔴
مذاکراتی که قرار بود میان ایران و آمریکا برگزار شود، در پی حملات اخیر اسرائیل به لبنان «به طور موقت به تعویق افتاده است»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129088" target="_blank">📅 12:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129087">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">چجوری یه مشکل رو از سر خودمون باز کنیم؟
اون کار رو استارت کنیم و اگه دیدیم داره خراب میشه بگیم علی الاصول نظر دیگری داشتم
اینجوری همه چی رو میتونیم بریزیم رو یکی دیگه و عزیز بمونیم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/129087" target="_blank">📅 12:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129086">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfddaba168.mp4?token=HgOKOfpvfn_du0XtF4IJb6plH7eAFwc--C7RXnsrVDojHpDC3tZMmLX5lw1ns2Ky4HvIgqvWbi-0eYmIFElK001peitW5vOW4-cfNNU30Ug_GkjV4cmUnqLJtwkKYi_41IzZvGrPqpujj32l_Pxskg8ATvAhL_E_56PqdbKpZSHgn7kfa3ei-1owHZUWXYml27g2HUYMD-H8IZL6npX9-UWTIxhpjvgrDoa-ic50ANc2whwy9KjAtxmaITHFWTDPAjkoMM1KS94L_dy3-SjCK_u4GMpXduQAlXeQUcJKNxkRJl170nWpVjVEK9TtUHV9O81K-evoL5ZfRSv4piUTVIcbj84HXM6zYmoHqq56nKzRUfoH8IVUJ49q9U2YnUBCScluhPy2HBq8AKwMgPTBp8ozkpVgDvMXXqMn-74Z7Mb_yv5o1TYYXqFyaW7wFvUvbtI2Z0iUX9znMeVqLAtvNmXcumNiLxBMC0ZvxjiG_Lx6G6TvWzZ3O0QhHmSDmfmBcpxzMz5il2BlzO07_WuWWfjdUb2MsqLxCOyeepbWcGPJB67ujg72jpwc5epI5jd9879gtB8GDtSE-KK0itvcC8mFGTKLrfY03xUzAtyuZpD3xHSNjjQ-ygHg8cJOLsGGB6FWddUt9adYfoCO2zB_WYGnRtC8Dw-b2ABNO40_q_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfddaba168.mp4?token=HgOKOfpvfn_du0XtF4IJb6plH7eAFwc--C7RXnsrVDojHpDC3tZMmLX5lw1ns2Ky4HvIgqvWbi-0eYmIFElK001peitW5vOW4-cfNNU30Ug_GkjV4cmUnqLJtwkKYi_41IzZvGrPqpujj32l_Pxskg8ATvAhL_E_56PqdbKpZSHgn7kfa3ei-1owHZUWXYml27g2HUYMD-H8IZL6npX9-UWTIxhpjvgrDoa-ic50ANc2whwy9KjAtxmaITHFWTDPAjkoMM1KS94L_dy3-SjCK_u4GMpXduQAlXeQUcJKNxkRJl170nWpVjVEK9TtUHV9O81K-evoL5ZfRSv4piUTVIcbj84HXM6zYmoHqq56nKzRUfoH8IVUJ49q9U2YnUBCScluhPy2HBq8AKwMgPTBp8ozkpVgDvMXXqMn-74Z7Mb_yv5o1TYYXqFyaW7wFvUvbtI2Z0iUX9znMeVqLAtvNmXcumNiLxBMC0ZvxjiG_Lx6G6TvWzZ3O0QhHmSDmfmBcpxzMz5il2BlzO07_WuWWfjdUb2MsqLxCOyeepbWcGPJB67ujg72jpwc5epI5jd9879gtB8GDtSE-KK0itvcC8mFGTKLrfY03xUzAtyuZpD3xHSNjjQ-ygHg8cJOLsGGB6FWddUt9adYfoCO2zB_WYGnRtC8Dw-b2ABNO40_q_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز، درباره لبنان:تمام خط اول روستاهای لبنان ویران شده است.ما در حال ویران کردن تمام خانه‌ها هستیم. ساکنان دیگر هرگز آنها را در مقابل چشمان خود نخواهند دید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129086" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129083">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoehqPkEC7gOlRBdXjI0Q5JZ-U3EF_3Vy4Yz6eBipO3UwKtxTfeCy4L9ICb-0RCItePSaflKh0jOwf-OCD_Miw5ago-rDv2M_4tZW2ydHoOU-D0bzaf3szYITZ-nB6oMciD2OsUebrkSWps1Zww29IuBVdG_mPSPjV1pTbjqHdY3-Ga7wsh_tcp-DPiX77j58GvzJJu11ozxampz7s8W-ExgiLT5aOpUA2TEBOPszRKnmL49sV4OT33ckpExqkBdHq2njojfJmoPM6OQkRQodzTauw7NQaErCdzlMysVLgH0bchTM8iYlr36O2VQFBHi7bPk2jLWan9fZVC7-ALVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رهبر اپوزیسیون اسرائیل یائیر لاپید:
اگر سریعاً این دولت را تغییر ندهیم، روابط خارجی اسرائیل نابود خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129083" target="_blank">📅 12:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129082">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=jsN12O1mtSQWCWlc0dm31EQMmak4KGytUCma-QZ-VEAPrflpgP7eusiX7TWi75uhRJWSEOi98fRz_Zw7rdFysdvItdsFcgEFOHzEFz_dSEOKMtiSA2C6rcP1OazcGrDmMEZyt4WLp4gdfmO1sfgOq6jVjMK8mTv-8B_dAhBQYgEbwBPMSLrcN8M7bo2fdm-j1Pnoj4Qs4f6UfCUUijiWReqY_UGkRzCD8gLWeX68n0dgOpjgvCyFOlKYPkQJcShlzHnpj0LeKUEcBnoXTdwJm_KZfnyKs4U_-jKleA_MQJkKzR_HMVA1FN2kc38CDmWo-Sb2salRgHjLH0lno72KXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=jsN12O1mtSQWCWlc0dm31EQMmak4KGytUCma-QZ-VEAPrflpgP7eusiX7TWi75uhRJWSEOi98fRz_Zw7rdFysdvItdsFcgEFOHzEFz_dSEOKMtiSA2C6rcP1OazcGrDmMEZyt4WLp4gdfmO1sfgOq6jVjMK8mTv-8B_dAhBQYgEbwBPMSLrcN8M7bo2fdm-j1Pnoj4Qs4f6UfCUUijiWReqY_UGkRzCD8gLWeX68n0dgOpjgvCyFOlKYPkQJcShlzHnpj0LeKUEcBnoXTdwJm_KZfnyKs4U_-jKleA_MQJkKzR_HMVA1FN2kc38CDmWo-Sb2salRgHjLH0lno72KXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران شدید نبطیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129082" target="_blank">📅 12:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129081">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bz59P2qVJWT077fQbQTEjtNVrjEip3okSy24vf4K49PK9XNvJfXLIHl7oR-V2aCoE4ucuXadUByBbpeG4_K2vCjmdF869i5IWYChGl2pG20Qti0pkCDMberrf__kdPBYK8cJryZczafIiCpYxJbrcnZ3iDLIJV1SR9j5wjRStaAKz0w2ZMRk2FQeczkWxKi6ke5ajnkoSTb1yuFIFmu_LVBsyqtvLb_HqYj89z9wugVG026RKfKKiIwDNOZn7PYGqMHvI96FHwWynvnVpcuYxN0Gykf1anJmdaIlMTqbdk9Ib0iGTmbPCPZiLvYrIfrarecXElHJT--IRd25aD7nyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لاوروف: خطر رویارویی مستقیم ناتو و روسیه به‌سرعت می‌تواند هسته‌ای شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/129081" target="_blank">📅 12:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129080">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل اعلام کرد که فرمانده یک گردان زرهی و سه سرباز دیگر در جنوب لبنان در اثر اصابت پهپاد حزب‌الله یا موشک ضدتانک به تانکشان در روستای کفر تبنیت کشته شدند.
🔴
انفجاری که منجر به کشته شدن هر چهار عضو خدمه شد، کمی پس از نیمه‌شب رخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129080" target="_blank">📅 12:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129079">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کاتس درباره درگیری‌ها تو سوریه و حزب‌الله : ما اونجا داریم می‌جنگیم
🔴
ما به جولانی نیازی نداریم
🔴
جولانی، همون تروریست کت‌وشلواری، لازم نیست بیاد و به ما کمک کنه
🔴
ما سوریه رو خوب می‌شناسیم اون قرار نیست تو لبنان به ما کمک کنه
🔴
بهتره تو سوریه بمونه، تو…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129079" target="_blank">📅 12:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129078">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / هم اکنون منابع لبنانی می‌گویند:
ستون‌های زرهی اسرائیلی در حال پیشروی به سمت نبطیه، پایتخت حزب‌الله در جنوب لبنان هستند و درگیری‌ها سنگینی گزارش می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129078" target="_blank">📅 12:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129077">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
شهباز شریف: از طرف ملت پاکستان در مراسم تشییع رهبر سابق ایران شرکت خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129077" target="_blank">📅 12:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129076">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129076" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129075">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
حرکت گسترده مهاجرت از شهرستان‌های صور و بنت جبیل به سمت صیدا و بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129075" target="_blank">📅 12:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129074">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=KssGyTcUYx7EWj7C5S9wHMLYN_s3nM6wdXc-Rn3nk33ID8E9KFNUkIFzvB_hXFKaShKQw07oRKs1Ws6_NHYDBGBIhr6FPWsY8VT0ZkKlvg5XjSrfePqhqmYalMiyU-hF2l3KJIgXQxQ-YgvpELe669hwh7AFbOSz7P0-XVLqQMnhVJGwuOMCrZZudvRTG3vfAkOfpP1CkVn2oZFUmmdoER_utFG9N-x54lqnFH4novp6zhYYwRen6Nz8Hg0hsfT5GEMxiTIK06bLo5CeEN_FtVmxdWkn-yLXYr6ZxcME1-_ic5IMr3_Wm3s46DUp63DhELV83j5vGEGogd_dQOnhmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=KssGyTcUYx7EWj7C5S9wHMLYN_s3nM6wdXc-Rn3nk33ID8E9KFNUkIFzvB_hXFKaShKQw07oRKs1Ws6_NHYDBGBIhr6FPWsY8VT0ZkKlvg5XjSrfePqhqmYalMiyU-hF2l3KJIgXQxQ-YgvpELe669hwh7AFbOSz7P0-XVLqQMnhVJGwuOMCrZZudvRTG3vfAkOfpP1CkVn2oZFUmmdoER_utFG9N-x54lqnFH4novp6zhYYwRen6Nz8Hg0hsfT5GEMxiTIK06bLo5CeEN_FtVmxdWkn-yLXYr6ZxcME1-_ic5IMr3_Wm3s46DUp63DhELV83j5vGEGogd_dQOnhmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129074" target="_blank">📅 11:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129073">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری / معاریو: مقامات اسرائیلی نگرانند که اختلاف ترامپ و نتانیاهو از سطح حرف فراتر رفته و به اقدامات ملموسی مانند تأخیر در ارسال سلاح، محدودیت در کمک‌های نظامی و حتی گام‌هایی شبیه به تحریم تسلیحاتی تبدیل شود.
🔴
اسرائیل معتقد است که فشار ایالات متحده برای خروج از جنوب لبنان و حرمون سوریه تشدید خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129073" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129072">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌گو با اکسیوس دربارهٔ ایران:
🔴
«تنها راهی که می‌توانم سخت‌گیرانه‌تر عمل کنم این است که دو یا سه هفتهٔ دیگر آنجا بمانم و همچنان به شدت هرچه تمام‌تر آنها را بمباران کنم، درست است؟
🔴
اما آن کار چه نتیجه‌ای برای ما دارد؟ تنگهٔ هرمز باز نخواهد بود. ماه‌ها نفت نخواهیم داشت. تا وقتی که بمب می‌ریزی، آن تنگه به طور خودکار بسته می‌شود.
🔴
این از آن دست مسائلی است که می‌تواند باعث یک رکود جهانی شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129072" target="_blank">📅 11:49 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
