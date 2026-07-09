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
<img src="https://cdn4.telesco.pe/file/fKMnCr9Q6qCGF6vrgSyQ65ICG454TEJGbfmQT9z9-LFkyDsyxQ3YoHiaEUomy1vOduTewkxiR3eoPwgUv6JuWffdDRPw5BjoyOY1zk76UN9wAHHxkQo4O8p9iAKINl9tnAKMWCT4rZcJxInxY2f-t1epCRYtvk5rZo_LiXeNXkEQRQKIEG2oMWBVEORrh8ORYywZeiah5BcZ9Asu7ORfoyhHzJ2ZQ9ATTZk_A7s_cZzUEbyCzpDbymzAqgYLngMSoLuwApwzFfFkRgYejeeypBGRywRIdeF-SU-l2FU32N9BQuAhyZ7tRmhZ3nUgRyPWPjCl-ZfEIBCdcBbziccfsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 15:21:46</div>
<hr>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAUM7kt-oHcC3bzVi3dRFiD5gZ2_eg2Duf0hjd_NMpaFJ-K59CzvAbj7iNlg8T7SIbGKkKwEMqcQJkNsuv6UjLUopdGBxGEcEjCr5L80lKzWlWp9jCSRQ7gDx5MZXFPC5R92fpN16Uk6xPS8bo0TURKvKwT6rJequeqd2i7mZPAb7NFDzZxQSjKkzehvFM2vSWoHf9qQd30oJmdVjF_lv46pmo2OJ_D8JFrcThXXLGhYf38WKMlXsYohrl90i5PRWeRjxeb6rBEsivDO-IjTA8EoRe9Yt7wxSLhO2GcubiEIos2Vuj-q5uhvpWf3aQysXMAadxfvbl6FoZ3l6NFkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcLA0WXYacawZWx3_u4HVWty577zpM2nH0JI1PYVmyGQqUvEp1q01uG58hk1ZbELZeOu9k65wQWfMzumJCziZA4ySjt6IcbKkOX2HkrF3jBPNSwBL7d2RkREWAe-miI8qBFzB_EpkvmR_IuqmCJP899WGGEqcH6kwVr047R3CHt2wMn0FrMKT5jUcPsJVs4eAPTLyt4Y86CBr0NZoVfxbJ85lZUh6lJQvUkthwDoCJO9pRBoAtPiBX3XYOe8dqUff3iEZd5LiHoX4Xr8yjw86U89kJw5-nQ47cmEahzQ5wEt4QywttGBhnYPQY1RjG3eKmo-TjVgUQ5xzt_o6CDZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JosCXh85VHRAbDbcDk3trNKCJqfhPLRdbzFIu3hQ_vtvTgWHJicx5F-AX9JLs09T7lMfL_1f2BNRTU57A74IZ2ObgHel7f8HBT2UdoKQPLT-ZG8PBWiKpPr9r4dfjzF2fhu9787rRd05pYkNHuNjMytulfndcHY1NdJ27vgzp-xxNol3Yf3Ms5Zr88oj5cBTg1ksb15L7Wig6QBD2QDznE5DcTc3R1tzEYH4_90VucOiG0VidRLBCMr_YoLL9k9p4xYdilNi1GOmymufb9Jra2ugB4tBSKNraF1BVTQw15yU4sqJbUVl_wHvLFqXs7LFge_U7QhiYerpbL6Y3PY8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGSojSNHXigIM8WCCyt2nR8U6TOX3bq22Zp5Y9JYwD2Q-TQfIGGckVJ4UlpeGsvsmrNPhJJgoR7rU76MhXFViQiC1KP0geYwgdjlXMd-EWMBD7SdVcRxnkosqFu3J4aVM1EbF_UBoYVBJhmwlJjvoq5jnGCFbuqw108mwdWbKYWzO--qDjTCXob0gfJJ_KRMg9lFWahiHPrBK2wiF3CxC-whueRyRKfadatsjzYhpTY2bIXwQKAzzLWWP_zxvhTKpX3r5GlM_EmBCg6alfOLTAHVGQa9Osc3D9qM3-7_3yC5YmXNXCLUCbc2xR3c8l8I7wnLOogmoPtc3ZoA2eWxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiVHk1CQHJj_RvcFYPNcsdxPxBNfSYgU3vcVHzmmkubLFWE9FqHn7fDin073xDta0SYYqhlno__ycjO1qyBcBsKS65dnpK0VIrv0w2Eb9gg0FJ7LH2BqzX3UTLC0yTScCsDtFM2iiZooKn1X-FOHE_lIDVuj_JCbyhpEpEU2G0AEPHhmTaEtym9Vv1CZozrYETbWkRErU7Ozq3PEiFlGh7IpGt1do8PI8JkG4SXfYJ2dx2WFq6znXmexmV4N3K80h2m-biFiUrm7sclO0H7CEYyF7fV0HdpevaIzA_RZemAt_YUd3kjIyrq8WBIpkI9MFd8GIkvczLM4BOlew8Rtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxmiN-KAgTdU7i7HJPqCG_TvE8molKMeNWPB33edVWpBhiLxEtF9n8N6MzjC79yx-opxlJld7xPFf31dRIG8PRXAkBJ8HR_A8oEiqkFQXCn8Uw9oXzjHauYAL3k9HQ1WJe6w2iJa2SpZyaXMx5E68mrbxCK5jMnEFpoKNLEXK0mofQSzASwwxPLl_Gey21bHECa1j_TlcQGtckEHsHFICg5wp-FZdyWX8ypcsBo-NgddMl9IKXlDIHoCa5eK8QUsM4E7HGt9-7sLfgAwtsiabwK0nXuCRYT2hefSt-leHijokIDMZpLrxiGFVh-g0RbCtLFlJHlbETK37LrM60Fh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5hBpvVZkufDvgzdetBMa4t7-t3ekHa7Z_gTvuaIw0WVk2JiKgl4t350O6oHY-TmU5MwzBP5PieLKiikhJq9wrKVwiggY7dh3nd5bNagMVMR2NEMPDkxB5PO9txeim1KCfpUWn5-UrT67YhWe7--uxkIAR-wDE8uh48rmy6gUrdOxvvUwcHLQ67Qbu_zXhT_kDoOuzc3BuXXL96DdLhZC2E7s1gm13MC7tNgBQo4F7GuXiLa0Cv_g89MQ6FyV_TshDuLL3MSgMW7Pn-SR1Q6jpfHMGvOb0aUS65r-v6y3lzN2l278FnXv5V4TckeMhEEBO_Wa7V7E1uDCuXqnyyWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIpDT9IRQeZX2vzd0hujlyuNTqAYwkHwiPDgS9XmMX67an0nvFYutJWvNy23bg5aGNl08CwR33wXoc-X0CPnbtQ6QOoTAY2lGCBlE72HUGVmqoErxbML1tgLANpl10frNXnQfoZztdiFineLHACsoAmRMl0sLPPksXqMj8hZLvA0NmWH2jDpgHaJszmrysYIbndTbsHG8-Fcex6q9fVnNaI75ds3yotlDl6yJt0vnjC-gyhf6vAH9mnBsrpsvJ-x1WiKvsrie6YtYYRkKGctLH2wV77yTqGhzst6iTkVApoB0OtlJxZGkgFW1-IzqNdzz7qRQa4dxLZrmycfkNr7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szF6WelATEBsSN7TeyDrwXiWO_3Y4INYxCK_7Za9l6tGIjLbCSaDQH9ZRNfVbiWLiG_Meah8fTSxcJZ02Bc9xTvSSrAr1CW6GbTfXad8ZuNajUF1UeX3TRw4MR-kNCbynmYJUUAzTYTHKst5grV1XcP_rSMne_tN3Ixv1dEQVjqyUnbrakX4jsM9I1bsL51Kq9xPTka8hcNzXhSDTymJuNNLjJ0ThS1PHqJvdU0pQevLeQ7jVssk1oXa3qLCotD9DhjMY4671OcHIIEh0VDLZuwoHg5wy2hMtmjXPnu_vAvJgJhRud77Z5OTeMevkkuUHPw3JPBY9fq5smtUPRbuUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=Funaps8mxy1k28sM011a7dimpvu_2ra5xWwpw8JJtBH1unqDVUxWWjRHm2AKCNGhHp9aDZyYAC0DdTdntNXvhzVY3S_bSYZFcTMiiTWXDb_qM5s8SjClgYv0DLsIjzs7mBUdiemvu-ROzpDcdCyPVRP0R4BduYcTjOLNRxxRhw0K6RYM7rudHepydDDReT50oTUviUU9vOmXdVB3AvjzA-9sUe8vy6LXXTN4LMTePdi7eCOJZ29iz1E3-QY4WPdXlPJa2Zd2ZVbMKDXBPh1m9FTaEiJJ-kAuiVpEjg-zvLzQT7at6SfETMrsjbx3RuTWQ1zKXqwiXN9-IbBRUok5Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=Funaps8mxy1k28sM011a7dimpvu_2ra5xWwpw8JJtBH1unqDVUxWWjRHm2AKCNGhHp9aDZyYAC0DdTdntNXvhzVY3S_bSYZFcTMiiTWXDb_qM5s8SjClgYv0DLsIjzs7mBUdiemvu-ROzpDcdCyPVRP0R4BduYcTjOLNRxxRhw0K6RYM7rudHepydDDReT50oTUviUU9vOmXdVB3AvjzA-9sUe8vy6LXXTN4LMTePdi7eCOJZ29iz1E3-QY4WPdXlPJa2Zd2ZVbMKDXBPh1m9FTaEiJJ-kAuiVpEjg-zvLzQT7at6SfETMrsjbx3RuTWQ1zKXqwiXN9-IbBRUok5Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_3OF2rY6rzh__c-2cLGbKmxssqphmgXoqskvv9UF9FlxhZXnkofxUZfK6PcArPfPkLpyhd414-JwZbtnf2pPeT2bKqywQ6LeGEvgh-HrVE--LUhRhSUkYKzq8PTTUHjpX2IE6L3am-2E3l92wp36kJai5mjyA8NGjgynw5vkHH9HMqw5ASjupUwiHokgnrYFRLmlYxmQc5Uq6vT8QVCNbUZH5X20zGNXQjkitxryO8I0E-o3LhpsalPsQ1nP2JVVnWF1wGIFVfhpRNF9H4Uqb_Ysql0bnU6cLKAizx805NfdU8hm3dt8ThwiDnCqqKWfQCqCbVHK_CLFoxMkU-KUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv0-GFpZeBGLxwmTqv6h-H-EluiJ61YO5sgBxGa16_yt2WmniQQg0kXV-lsdFLANJn8YU9_rHksGWTqVDy1Ud43C2yvCX7-lLJxuOsytrQ4jIw9tK7Yw3K3Ts47dFxZqJkKLyhpNlicjFMk7TaEK13DR9J4TmtN1nX96KO26a4TtTIdTn1BoEbliz3FXVw_CQ2HbXYSOQDSWnUHXl8iBVVw7TSgJm80SwEJ-9CJJPeIzuyciE6M6UgfBMK8CeW_tZVQgJO4TBS57l1P6iO65WbkGEoU9o1w5-rIytW1gK5bMunm52e4atyWDxSaQldsjGCxAoHIQkRRv2GrMAGzc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsyPIUG-A4Gfebxl8JBGHygw2fzdrR1fWzhy5_cqcMBUNgspczQSLE6g6BpvOHxjxVXa-B_VBlLwKBdvQUw0CRdYps0JFIj4N3Hktrr-gUZsYnY_Zek7zb3QpFBXzJz1_Y2M0aWXKy0JRucAcx3QNQU1tE5aQ4RkclgNiv2DuPlXsLq0F7P8LqFm5qAIBcGbmy2y1qeqgiPM-Q10QJ4IVlUUzCRgy6OrBUJkuoeNA2tWZirLLHu8fUlJg2xOwdE1zW8zSR_I4KflZhcmfZmMyxQjeyEJdtAlwF7AzJdeJapyqSBajP3YfIapswwzWB88I6xVAA3iOf5H__XSYfIscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=aD6qsJGZuR1tuVTyYLwa8nPgdO9h3KA7z9ynkb6o-tlRr2iy-XyxOcPbRlZbpmNnsPCVoYK_RkwmrDIImT27MB4Ql5DuuizPura0SKXvedtas12xicP-ifyW2yhcNfflLqsdNJwLkZnytvId093NIuGlZSO2P7LEOZoIhKyfytAXE9AojYoWQKZy0J_YXMXqr8OrpUaitmDBbzv3XMZQn_Rn8ZLcMQxyDlUr2SYOg4EXM16pvkVVzSs8_dSh_5e-qQadTsw9UFHhB2y7S4V2IU9OV2e_yTu5idMvMgVkkpO4OdwrO1uc2tMJi5ZiiXQiqRd4fk1p9rIH2-IdKJK3mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=aD6qsJGZuR1tuVTyYLwa8nPgdO9h3KA7z9ynkb6o-tlRr2iy-XyxOcPbRlZbpmNnsPCVoYK_RkwmrDIImT27MB4Ql5DuuizPura0SKXvedtas12xicP-ifyW2yhcNfflLqsdNJwLkZnytvId093NIuGlZSO2P7LEOZoIhKyfytAXE9AojYoWQKZy0J_YXMXqr8OrpUaitmDBbzv3XMZQn_Rn8ZLcMQxyDlUr2SYOg4EXM16pvkVVzSs8_dSh_5e-qQadTsw9UFHhB2y7S4V2IU9OV2e_yTu5idMvMgVkkpO4OdwrO1uc2tMJi5ZiiXQiqRd4fk1p9rIH2-IdKJK3mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFce7TkPocBu01EY1K82vDsPGPP1NOb2W1tAEXqD-EFq9IXe-eeXUZ45_TbA5b6xvNDeXMZ57yeqP2Bi-lN8u7x49fU_27ucGmoXTOtt_v31EcLl5A7mgDHB7ZNMfk0_G3F_Ywc9oZ9_VpaNNLFaqqSptWrGCEEff_GttHjKL7bZJW4g6foyQqGsar4g4Hg_EUQv_xWcsBdtEg2z0aWMmt7dbQXUOeYDzoxLMbXIJ0UfBqGTycbpzPlfM4SJCvjSK9xDFe81cj24xmgYBFMt_n-7rgxgFeUWN7HnwFUqVNL1M_Ln7BJ3hAy9KTiG6CJLTwn_0yfy-KXkIbbka3Tidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFa3lGLjnInVlbhpXa406gZYU0stxPOdOW4QLlh_xzRf9mXW3MKz5HRNzpIYs6hrjUnORdEFSzrcHKzt-smGiW5tBP2lv3MxSBg8tQxbHnZizmrz0sX7bG9hc1Be7hyNJsSny-ZaKNAVL6H2Vz4aV7M4wceYeoQzzYphRNQfm1coSQnoaxsYCotglcKJPT1sBFdNsoHfi0Ui6iPhuKKf0apu7ISiM2hZjUzc1k5qSOleUiGRzgREdAp_9ViPoVPsGx6bFU7mi7qZrOA3PzlDc7VQRqTOODq99tbxfD8Xt6zmwM2LBrN-DcSwk_SN2uBkJ-9PYC_R9NnSbuAnkPqhhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prfMKpWXmoEGLmXsUU-ZoRba7zPYMH7sthai8jxgw4DLBpMy2s7ob65Cd6FYXaRDfVdBcRqsPZRFDpI5BqYIxkEEVbaCNJbYz-bU7_iG1AcUfTsY_0mwvVaorytgx_IiinW6JyFsnIj-M5qyD5LvsBobbz_9nlFbjsztKuQuFyeHStw1oXdBRm-qxJC4cawZ5EVvXyGftuzEwkFhoUhwuwLsm6Z6QBGzKnRIUp6rwa1KgN6zkXppKVa00Hp8hIfYtROsmJfYy2vFQa6fs4_hLlOibeo-z0rIzOXL9NK1ATkRCjHUetDKDtgMzZnJyF67U_iLdQ_5rQF3cqJeQL5rPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXpoSf3xU6JaEvyz5V0ZGZzws-g_xaOZE0lOGzOaOU-ZfAJr2G97ALRZGnrofz22OQHfQcKI68EkPRpTK84_h_IMLi5lXSHeY6L-OA6hsKZh3ZOkg86lajzDFhHJPU2KpgyvcH0FAmd2fCbTvgCijw57Cs4oz8xLvnfWvXtMrI_0RH2Fri5cD0Q0_sKdSQWWIVFqK8PHozxg8PVmdyWFJBbDw8HLUx59i9Lp9ZCfJbl0Ur46o9yTr5lpsOy3OF-LfGai1_Rztc39Atv44gGO8P3QNUCfTCaIYe1lIfzyB_hnxALC3---0RdkR1PrZ7VnVev0Wu4gnUYW6UnkBJ4Kpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9IzGpAivKCiSiMAO5OfHrxD_DWow-SaUesgCFHvzxzyZUdN5YwL1nOuOv7m19MTccw-5VTWamJ3eBoKiXqujnd9UMxHv7-V-4GfX2zM2Hwj6cAztW8lIcapPJhbhVK3GPTM7FPcJj_tFi5y8JwABV51XljHx3A9Mr8KV75IQA_OjwDcZiHzSRThF_FsqEbSBy06P2seFBU5Sao_ztjIESBMIrVGBvKrzIiFEawcuRyBgdKP2hgcYB2gaUU7B2J8dwQkBRcpcCA9m5LOwGEUkJvn-i3ywUe1e-CcC5ukjm849JhQpXOr-5n1snS_JTqA3tkkgXFIX7UAi_mPV0ZLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJtXPCK2WOJwrewEGZONlLaEa9ht0F9cQPOei0orvIZzeupbRUGIGL1MG_hnuFrGBZTjaG3G-zVe3cpJrL-SgW-XRRCash5AOoQ00eAoWQItHsawnJgma3GcitrcO9WkEa8Nsckzg42kQduQSK9wPPQoC7TtwZKsEF_OPs1k5ZvYRQgka7WpHuOCkdRkiTOYMKSZdlSKgjYZYWhwEhM_IOz4JciOGCJ_4XNth9dqMLvwoVE70DwylR132xMCjUmePB_6swn900nt1uHne49plQ1oEOi8655DvDuHRzf_JVUeoR7BFkbv9ExX5mHCWxEdjWYdbGO6AT-n0zQATwruRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwM7XRzKzA_8gjcixTpo9Mjz5GDj33fYFCaCiuCpJTiIe7ZVF7MSwldD0Ijlj9aEef2rtF0UsgqNwfcCvUZOTTT00jME7kj2keQMXrvx5KtM4RYE5cJQC1TIfCP_qRcPqcfAz4cMkyWwzituScECoF_XL8YmzF0azzL6QanxI_x8C6lILxPkSFbFy1hE2bVfeuG3AJFN5_khtKwuCq_OVZUl2ISOikI4WProH_xexQt7b6j0XUQHZFM4tUpR9nPTaje4pE6GMgcbWQ6eGoyEncWTj3lC6YHOJ2e-qzfWdunBZ_6sfgFeCObhcVvBG-4B9PzYD-j3gbV3RZZIrE4IKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=sKaXffP6uUWfeo909RQdNy1H2QMxnXPuH61xDbQSiZ3f3TGHFNZNktaFtpM7MWfc4JsM0IP8Ps2cpe48QoIIc_QefTJbXDYJx5g4TFqwwZZKGAjWnDloQ4xSAPJK5yT-B8IU2acTZJPX68V-nBEsme573FyzDl0BcNiOklDQBxNyMZ0dj26GyXyrA3nxZl3F84Pp8FsoinzJNgbZMYg_MtSombVEHgOtqYBVfPC6QYbbI8m_3KV62rc2gfDLdjt5HKl-AvIMiEqMfP903h09pgCfeTyBma14ZE_3jzSzbgZ8UGpW81IOYZQmPNx2ln7OysETvGrg3Z7oHxgdTY44A5FO10GOZ6C6xyChNtRJKxv2si5ypG8d46WiVqRTbNNOcjRsCt0E0gl0UfhtcOrhSkg4U-oOtSYrYDnEyxew4or6eC8qtYLMURYzsWCLV5kGpd08X0QzvL2NJfXkcvGdHSjZdbZsdTL354Anqz0S2-lQkvOlamD53DmKLu5bWZIPJowRV85Te3GeZEtDYQnU7trJcKuzQup0eLYL-D02yTNkdSR3Px7lWKjMpMjMO9j67RxhcwMmlRDneMB2CUUeF_MQMrGB0_wnLD-Bc98y0spQ0FaISZLAEUn_NmDRVXdqDD74-lKVn-FOVqKrq2VX02SHu33bd6-KDk8maIt9Zu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=sKaXffP6uUWfeo909RQdNy1H2QMxnXPuH61xDbQSiZ3f3TGHFNZNktaFtpM7MWfc4JsM0IP8Ps2cpe48QoIIc_QefTJbXDYJx5g4TFqwwZZKGAjWnDloQ4xSAPJK5yT-B8IU2acTZJPX68V-nBEsme573FyzDl0BcNiOklDQBxNyMZ0dj26GyXyrA3nxZl3F84Pp8FsoinzJNgbZMYg_MtSombVEHgOtqYBVfPC6QYbbI8m_3KV62rc2gfDLdjt5HKl-AvIMiEqMfP903h09pgCfeTyBma14ZE_3jzSzbgZ8UGpW81IOYZQmPNx2ln7OysETvGrg3Z7oHxgdTY44A5FO10GOZ6C6xyChNtRJKxv2si5ypG8d46WiVqRTbNNOcjRsCt0E0gl0UfhtcOrhSkg4U-oOtSYrYDnEyxew4or6eC8qtYLMURYzsWCLV5kGpd08X0QzvL2NJfXkcvGdHSjZdbZsdTL354Anqz0S2-lQkvOlamD53DmKLu5bWZIPJowRV85Te3GeZEtDYQnU7trJcKuzQup0eLYL-D02yTNkdSR3Px7lWKjMpMjMO9j67RxhcwMmlRDneMB2CUUeF_MQMrGB0_wnLD-Bc98y0spQ0FaISZLAEUn_NmDRVXdqDD74-lKVn-FOVqKrq2VX02SHu33bd6-KDk8maIt9Zu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeC19FpaPaFa9N8mvwKIt7G2Ud5hZ0vZftlamnMYRpAjlq8s-apwBJkEJA1ygLqx5yG-906baqBXex6xGapY4q7opEBQlcAsbrbohq4DSOfE1OMrSXnixSyBsgF2lPu89gWZOVwRWlQfX9_AWn06_UNmkNysIzYuQU_KmwtXJkXfc6u2LK_uGkdZihvBHuf6JtCBJs188kG8W9DXKylIqtgV1EXpEYlWNpz8qN4vJtizlVlYZnPGOY7XjaCigl9zWgJM7Diza29fY3rjEtvw_5VEYwvsZOAvIQSswXhwrjgmmrWBricKYmmnda0OPf1hvvFT08jENKMgekeBDpQYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUBGr2vkSKiocpXwrfJi4VFbTVFnJP3JxTcbh3KtySEc_OFigjSdd2uLIZVygSVMPzo9BV9mytoEkfiU7g_KEpQE4VBuHHxSIEO0ROhN73h0kUR-MRdFCCyCbDe1becNEQv0E70vMnkUVSbFECL-XfHUAawqQpweghKApeKu-IJ73eyvFoIC3uwi7r9ZEUVZ8A0FtZasbRq5kZrMPPYJMkCrclQ5HznPqHmUkoiLGxfQFRc2MLFBC7ICHbeB5uHWw7EogtDhhIx2EBdUgFN2Y8wMOweGDmdLTdFIeya-DplvZKWmsVIY2M1ijJS7cLHOKjleiox4RHEvFaXySCPKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVHSLdEEVmLOqwq7pOiBqT4Ot4wRUOhaU1DdcsIDneA9GYS5vRfpHyfM6BthddeE2aNtCk2DyP_DRHNuu9-pN0fNZQg83f1Z_5cnnzXcB2aQPcpDIJJwo0H59foMhhKZDfxYWnxS2tYe5uO1EWGYq8GerW_DOZaK8ZD6gmhs_YVRFYH7cfiZlvwUpZ-LQl4mPkG12sE6JCdjT0GR_Lm1p50mfFvnMo2KJ_UhFEhhV8CKUz2jagVZ55_HJ0tSRpiglEO6jED1DNyqvc0DwfivDHChOpCdUlFQLBA-Y9oCdQzh_tuT3oi_GopXzmCSEix_hPiwV1hmzopLgzgp3OwlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=qDKfkkrSP5ZadoGiDoYYXWndhq8p-rrBO9n789plne07FGtrWcr44ywEdTEXo73E9Wb8s5IMG8d-24_SXs70ZoKtE5Yfhi9l9hhh0KoWOh41y0yU79dffPinplJqqXp0aAwY6gUlMfHKfi1Qa80SFs5Z_f1jdOmJ2pX9-NZ3Q65p0D1Wk-KrdaWLut_TCLQiQWF4FCqcxFMHoZs3y-v1NJ7QEA2S1RWwX9fUKSAEnQCMvyEcXhDHXJcE7f8NxxsOthX44SfqJq3c1H7acB2zOy9LDAiGI8V6zN_Yb9OcuuCSeLwgVBDPwxCX5PFSTQnWqZMobO6YfcaYDwPlM0T_Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=qDKfkkrSP5ZadoGiDoYYXWndhq8p-rrBO9n789plne07FGtrWcr44ywEdTEXo73E9Wb8s5IMG8d-24_SXs70ZoKtE5Yfhi9l9hhh0KoWOh41y0yU79dffPinplJqqXp0aAwY6gUlMfHKfi1Qa80SFs5Z_f1jdOmJ2pX9-NZ3Q65p0D1Wk-KrdaWLut_TCLQiQWF4FCqcxFMHoZs3y-v1NJ7QEA2S1RWwX9fUKSAEnQCMvyEcXhDHXJcE7f8NxxsOthX44SfqJq3c1H7acB2zOy9LDAiGI8V6zN_Yb9OcuuCSeLwgVBDPwxCX5PFSTQnWqZMobO6YfcaYDwPlM0T_Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDuQh7zeeEIKaTBRLH_yNRfBS5h0kPn3gcImTyf72OEHqgqsi01qhaOmc4fInRU7x94vmsUw4bcqCnMkdWWkEMxMcPWKodTkoCDH9Rt7TfgNVz66DHn-rpyDSU2Y7YG3SEIiEv54Q-n1wWM_bvRAlZvfaiNR37IlwKSL9mTUC_1XS_2VuU9RdHRZaeiQwjel7hMT-7-yJxa_gutRzMSx6aswZ2Js5DjCQP0PBBdin_nfcaOGh59qasEEKiLS2s7flnv5QnSUrBGiHvuj_4HFGgTPm2E7_U3uyHKmKMDLUvVKpxk8eCFCKBjBsuRMNhaoh_yp9MCWMQmMePCIiFl_iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aryq-eFvYca65T336GEj8A7sh5trzJVr3NxB7PLdGG94nn8BrF6K06xQ5fjTglVcRz6c1aYK0NdjBqBM9nMiYZmB_rKtl_bX7hwNmBFOrZ5jh0vrfaVPITtzRBzLi74Xj7UJ2gP85gRt7BpBxDGQ6ON1PB6cTzKjWUzmjEpo8_4sSmeOBSBOr9S2tFnhsobpRSXgTZEPgoXYw7Ol_fa7wKrLER1RfQmcH2Af6lp5xzUA7hOmXeNQYWxM_FmJr-9I1vuyoGf_xyDle1SmbnaH-M8a3TdycuEWRyCYtLV3G_Ou7oKDlOOe2hMR1bTFwgxECqk9v018oPI9EnogJ2bprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0fBOOSEWciKGmcB_typ-OUdbTfvKiYrWXBZKPCXtN0qqpkq3T8d_dv7I0qy6zH1gCF_tho---nuef5wfnpJN26St8k9ofvrBYYYY2XcqEOBLZvqfedmSgCCvBbjaCOf6C2HuQm4NAOb6y6oZnDm9lkVmsj-UMsauSbk0y54S9N-Rr1DHLRdR0hjWi76H2Q_hOdakOudG-LWSty1r_Sj663ubQxxOYp9HPkF5Vtr6coU7NVOdeZ0Gj1eLGnWKxiwleeuebAPN2D6gRiUyPkmCYimyXOHuaFHc8RY7GrrFZDMghYVzAIdD_9cgo_t_9dzvEB4Hk_2rrOVOMkaXHJJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSACBhjpJY8srntsNgvqIUvsoXaEsDofgAT6j-UY_MCUpOwwh2XGmhG3ZHIFd5JT6LrZfmDK3Abt71pQ6HG6GAYTy85nolgo4AyXSJMGu3ob8JPxPK-Gz9duEUSV8M8kX1NKDBfGkhwJ3Xq_SDmG2IiovOsJuyBJDAcGYTjIUFHWo-GXTLu_sExDuDK2dVZoBurkDyoJv5zVIroxfVB8MhiwOODyEfD27LgqEI98nY-o8HCdyuMt2ROvDmMjpbo-alomREGJFqoDsDAF9mdm5IXbe2orB0fXpUH0EVz6OUGiF3l8bC53qN_oZxN4F8HjwBAC_ynOjVPgNcsV428ajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKqYXS6kpQ6NMqnbbR6IWF0IDt6DSJLkMd2js92TcRyR32J9Q_4L8HwfDMiPF6AQd8QmqKot7KSRvAWvsE3v9xNF2PPwag9eiNR_qCk1wxx0ZavKUYJPe9uqHMuXmJedBtvqObtJVGRWL89AfE393AW5wKwOhy-nA2-343qMyeDaSxEAoTfrAM1pohmudPpqg-oBEugGLVJAbYKR6tbA_4TO-j40_f-ea0nyWh9QqI3ReekPF6es0Wsj33fUWXMHYnNFaEECQfqGW2jjaaf8-RdXSsLxFg8gqeiIGdxUSItlfhKVCS0QC9j37kKEJclevySzD4SI3WJijHBd0V1f0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6vLeOzymi1NPh9Z4zF-uZKtY1qpTDJmBdo_0h8nOZKZXfxXZxGg-WEs2SGwQfauiqJcwNf_AY4WKYZMpBqqz00wiP-TPQavQ-8tLKApJAPTkxIOZInaoES-hfqF5ht68Yxr28hf1YbQmRWOeDapTIePaDc1A0DJ-mRo5tGFMmDNkm7cXekMS_gq2U_hSKQ3ZcdkKvfZSFeEJRulPBNQYtpIBOrGd_Uoq6hprZ6GEsm5Qr8aTXX2i4oGEMJBe6WVTfJARBbPjV8_Q29uajYo3noPqYe998CIrAaCBMiqNQ_M5IJMnIpR13ytZsxa4IhDt0zUo0wqxQpvDHo3iiO6CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTCR1IUouDpraMylj4o29ZTCUtO51LtiGpGlPeuWJZEWm5Qxtvj21OLDYXmFD54cRwjm1lUiQvWVcUyGV2KDeE4YGBlmMaABCeRk_avpQnYU3giOH2MNPnj4wzb2WWE9GH-qTfnrrdcn17UK2O356MvdabooQUhCioN6GYqjodxdtXI7BvaRA5IeQge4qw7VNVWX-q6p1VgQpKoVjdF0ckkmN7aYxNM1yNG5ON-b4VgxOZZSmMQHseEQE4u1YBW8W0q7f2qXJLItvVLumdgwm38GC3EjZrEgYyMYCyuCit2fTeWs0KjUJOHi0lyrCxTmoNS-c09auaGMYL1hQE6JVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SCENi1smIJQtvp54X9pfOikxnRqK2fp-PXEs9uLha24f08klbmfjSmum5XbfU9eLMhwl5cvsK05Txjra4C_e15bwR7RBNLyeqinqr-2F8lp-PqNE7WWwkoxSKTH3A5_3ULj45yHk_cN85p7SlSOafy5RpgN3bREyfyt2aUUFhJUEcUjChIII8k9ibgRhWYNjWS7jx8NTq9K98_8oAdByJOLLjH-kDgD4OGS5aJVtfpyYelF6oDoMVcaO58vZcMY2ehvwDVrMrTdDzI-A8Id20dRa7B0ys93obat6YCB8tZeF4YAEFjo1E10OJjLxACCCc5RDXs9r3OVbJk_yF6xQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLGhTnG8L6nsMjydodK3gbmeuJePR-EgAifHmMnhOzze0hdf4VuIUMYcjCige5aWh66PaZG0J-rjAHQZ_3GAz8OPtGlnplBRV3Gsv1Trcmet9efyjK12dPF211DJFuoS9KBUiU0xLE0Qt8v3r4e5EVkdAVkFBJ0dBbJahUwUIV2XBnlN_2O6_QnMF3MEp1G4pV8WlqAdBhToTow8jXfoSfNxXNLKkRIU-SS-K9Bb5juA6xxciH3tWREFXiLvL8ozK4wYPDJd0GqEgM26dsnr1ySvxBsg_cdQMxqv0HIl-bRCI3z5GazgYjmFvjGqQp2nSoBliTYpAOSi8JYUO7J9xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=HEDz_9RiP9EXSTnNk0luGnxtXB7xTJMHKBQNRJfcdOVrzvMcAGlZ0cQGuspvmRvLInxXXtlhU6g9-SgMDNvso7aLz3ncXdFiiZRZj9ESpSIqPuWuM8cPDNPshR-n6wa9shA_yJqFc219EWYqWZPlxP8o67xLX3scB5d8x0XHsTCzD-TP9MDtK4bKT-s3SF9_AmOADvfmUiyi0bFO7aft8PhF4AQ-sVZQYCQSZ8l1tZgdZAjXYoe9CeOfPKbPgqkqnrYZnPYTtmQs8b_rpStV8s8MLVDjA6pjNPIIkSei62xX5JvqWLQ25BxneB1jO4c6enoHqyy4p8XZHDPxSkeDHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=HEDz_9RiP9EXSTnNk0luGnxtXB7xTJMHKBQNRJfcdOVrzvMcAGlZ0cQGuspvmRvLInxXXtlhU6g9-SgMDNvso7aLz3ncXdFiiZRZj9ESpSIqPuWuM8cPDNPshR-n6wa9shA_yJqFc219EWYqWZPlxP8o67xLX3scB5d8x0XHsTCzD-TP9MDtK4bKT-s3SF9_AmOADvfmUiyi0bFO7aft8PhF4AQ-sVZQYCQSZ8l1tZgdZAjXYoe9CeOfPKbPgqkqnrYZnPYTtmQs8b_rpStV8s8MLVDjA6pjNPIIkSei62xX5JvqWLQ25BxneB1jO4c6enoHqyy4p8XZHDPxSkeDHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQBbpM81Cuj-nPLmGMtHuviByUGiCgEMRd3in4MO9CFGANzI3pl5xVAM6NJaN3z4K5Qa4OJn0LrNpZFYuTIp2bV4rHsR_YOafL6TZTmpYTvl6d0jPKmfZyqD1AaiqhJv0UijDNnA0mWrr0yCqnvSIilHXTdxW1JrO4z8HVkBTXqrl7xNvADTlHadCkFkhrxy5_SLThvL6xNSnCJSoiMYRuUXXUNCd8kwNXrxV1GCc00qZOf2o8zoLWVGKt7vPlNHUDkEbYubmG-ae1Q_X-rWb7Gexd5yin9nZ8LlkzKxHdpxTzuf_TckN_oQKJ9k7hsSlCNmoP275B8iJ3moB4J4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25238">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=T4FYKUArSYYDXdh4Se_-QtdrWJG6dCj2OetK6lAmkxtIzMW6ynSnjjh2nllTGjEH_WA1qupHpS1i1N0De-KcwLBgrQ-f8tEOIRYmSGBtWOKwiP1C4YcSV5_Z5hgVAWpHbbvHKMimLwt7YE7XQHvsbyWWcfqY4-w3scmhinvUXWhEC3s_I_QlRcZ80T2k35Hlgp6DtDo-qvOW9YPOVihE4Q_KZDIp2bOg4pWZ6_3NQYW6D_vhzmEVAOUbSkioTky64PceGrW1C8V57-7EYDVDDRFWuvTgEroSYD69sMQL4fhcj9ACczDuR0BrE8vku1-iH4JADoPMhx9Oj_D6-rbmd2UDP7TX5KOkrcmG2YZ1Iztb8DvzDZmr_pF-a7-vb-68UHzuJ0iz3Kd0yrMKVLAJYRkMQjQA6uHyGXNz_2l7ooxphS_jDmrIGoPPacjIVdHqwGSTw17_-otjgj2vzK04N6vkJSUOby7U-A3AfgDF_l1EN_BG8lXaNRI9RFp1AyxQQmwqMbaE6rwoSUC9YL-KDOb2JLT4-zS5zGDv9L7UnMNbGTnlcG6RsUtjk3rSGmkVcyp6CSwpar5lNK3xHV7ppDWelJ8i06COy6nn3-E5MSm1J9cvOHjwV7pH9B-siJvrgjk8XllHjeHPuGTs7N8SvYkgJ9epq8nrI6XuaqiWDPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=T4FYKUArSYYDXdh4Se_-QtdrWJG6dCj2OetK6lAmkxtIzMW6ynSnjjh2nllTGjEH_WA1qupHpS1i1N0De-KcwLBgrQ-f8tEOIRYmSGBtWOKwiP1C4YcSV5_Z5hgVAWpHbbvHKMimLwt7YE7XQHvsbyWWcfqY4-w3scmhinvUXWhEC3s_I_QlRcZ80T2k35Hlgp6DtDo-qvOW9YPOVihE4Q_KZDIp2bOg4pWZ6_3NQYW6D_vhzmEVAOUbSkioTky64PceGrW1C8V57-7EYDVDDRFWuvTgEroSYD69sMQL4fhcj9ACczDuR0BrE8vku1-iH4JADoPMhx9Oj_D6-rbmd2UDP7TX5KOkrcmG2YZ1Iztb8DvzDZmr_pF-a7-vb-68UHzuJ0iz3Kd0yrMKVLAJYRkMQjQA6uHyGXNz_2l7ooxphS_jDmrIGoPPacjIVdHqwGSTw17_-otjgj2vzK04N6vkJSUOby7U-A3AfgDF_l1EN_BG8lXaNRI9RFp1AyxQQmwqMbaE6rwoSUC9YL-KDOb2JLT4-zS5zGDv9L7UnMNbGTnlcG6RsUtjk3rSGmkVcyp6CSwpar5lNK3xHV7ppDWelJ8i06COy6nn3-E5MSm1J9cvOHjwV7pH9B-siJvrgjk8XllHjeHPuGTs7N8SvYkgJ9epq8nrI6XuaqiWDPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۲۰۰ میلیون تومان درآمد در ماه از معرفی دوستان خود امکان پذیره ؟
بله.
شما ميتونيد براساس مراحل آموزش داده شده در ویدیو از معرفی دوستان خود کسب درآمد کنید.
عجله كنيد، ممكنه دوستت زودتر از تو دوست مشتركتون رو دعوت كنه
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25238" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORgdkeUOBUX8yIpdydHgpOgxapGPZwZYXp-wGSQKUrI1y2vOo9qa59CbTelyaI4B5qR5MOcNueATmARQdJRYD7Az-fx7E5ZYB0ZhzRrxxMXvPOnORzENnVZeUJXgBc4kQ0ld-Xlt1dUUMwe0_2hlk6B077SREj3Ih3Da2Imeew0Auv5jW-o2QoHplI5xF07RgRk5OwZJX9BIe3CLeYlS3qrxup1bOWqKSZq9ldAP7tw9TugS7VD4fyHYwHnnI2RT6qUVKhGueWLxGSEAiRzs19PZYdId5Zwx2DQI1hSp6Kro42qWPRfBOx2-_nKRZ-oKdGHmHec7vCCsBFEfGInRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djEzoGTd-asV6BrQRhvjG3XC9K_0yY-evNdAqI6PbT9nT4ZskuJSEJPDO-vQRloDC5mC8xfn1JO4x59qmpPR25wemmrA2fislo2o0Vzl3Qry39C50WI0aG9jVvPWqo9wydS7zWVZydeNNhe3o-WvovoaxzXQ3WSg2h85OGPMZUJO6aPP-c2ul0mtKHUKkcD4CGB6Nhksqut-MJGn-C2MKk69oLPpCvKZhwREGo9lMweWUYtvvec-N2Ss6YzMGIudyMvfTscejntLfXR6F_YM6KSsBcwTYMqHzPj6E9fJZFVB2mBD2rT5IAhlPIzD7EF-65VuYuHO3IGOHJq5sIGMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mezu5gGqKg0rBLqJYKtfgV3aWynpiKxTEKt25HHt-vTynye5aPr-HtDI_sq2OS_QGHbM-YAMUvRByKbgTnXj2hfGQYCmSPz8F1NeIWccqYnHLI9Obl4O3ACxlQRM8jQO6IU_h1XJLidqj3l4nB4L3DlE_--Ad7y4Yaoe1n-Idba_kP3k__HcthO4Pp8u3ayYh2abusEJnmHHoxwNblXvcy7w3_SWAx_cE9H_UEBvqTbKb5IrlDN0CsABJo6Hhhv-gb6AYT-6Ss79X0yG9OKgVzGM4V60VS6YI6ZzCiYG64fiQsidbB6VviWAneDFeSvgZMop9IsfWvVcVegFEgbK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlT2OBex37_laawS-lc0g8RIat1CCkTqErSjwyXruMHqTlY9Lo9fWRRuoXZhAk8vzItfh0wTjjqRVmsXLSJcBzXICTxQMxapSG_61Z0Rr4dy5oR6azcQ0dzHQXK23G517eQFUogG5PUCah1Co13JUQAZ-2FeiK_2U8YKCDOftaY8HiQ9VCu8c9uORqpOWXgEpUAyVDN0BgvRwEsqSb09eIKdiDixRDSa87-p94HKq4wvHVX72KxTLLC_5UrD9KifxqrOgg1ZtOJxaJ7-oyLS-dnYsOUlE-LwZ8yIbLD8YGcB1EaimIqk0A-4-zuMG-IfocY1Wd6N4miiE9CVQD264g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRFZG3hi6bq2jLN1ui9eeAUFR2rXNkeEmrHUWdit8uKftsSCLw9wza7pCByLN11JzvmtEh4b49-7dst64xHjEH_2Knam0Pr7ciUYWUxaEbo7SxSTbr-YVYJSt_6d058dl-jbEotWWSuQeP6Qt74Kb0Tf8sMYkgA_8qpUwB-mQg_-g7-9TyYHkPEtoPSknayq8eAUI3ptGFOilMcXMyNgR7MaMafLVTSZZqK-afJTTDZQOhnFQPHjqfCtXZKo3Y8oQpMDsbloac4qw4DM-WpfcQqTGR9gh_V8Sp50MSnypuPtSHTTjP1-KJf3YgKImq6dZXn_1ajeUYFJHlQrgoopXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev2hstLi3EdP_hjixdfoEasqEgLqnjQrWMG05iI2qnQCPING-vY7xJUBI6GmRV9lBRxNSZ9LS8vjj_ITlz-l145NYbbtsqQ6VP9sbshbBw4BybIRVh5xysBlkv0rMcZmbxMFKmXE9hsJ_BIdV4onRmrXVmdyNpQ3FX_sTP9FFveSb5apeIYLhiVEzo5ga6AYiVXJ1i-y3mr6kH5_dOdqELSxCXoIdoDrY_JejrvRIyChZCLRNrPZfZmzqhgoEydtECNFvHrN0sSuKtzEEVQKzVY-vHXMgwJfTC02abKwd21DLulRnHdh0lDkFgWmNhGDdj_2R40a2L1cYXeyca5RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVI9a4mb1HYWij1kFqCJC5lMmu0z6rQPSvSk9EeDo4z_4GxQlGJpFYgEm0Zgx5FMzhfF24tU-dZ4fASwxEK6Q56YufvM7TOvlnec-JX9RmJKVxoOd_YBdn-KtYOx8ctxqMq4lSxuv2-7dXk0vlEmsMckTVhqq_6fL4RX2jbjWYrhLMloIuATchQkIvxMs7opPbiM9_boCf81Bo6gazvVkhFvw231pVsgaAdOkDRfIFLqlS9u2bJFtNuMnvy4cgkQZolSeZhzkbfFegVZvu97xv_heOp5AT2spUD34Sm09wVvGzoCAvu_wJ0AtjxwEV5GEhUu-CYcSdh00TFP6yYrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYRQfxvhk7pKiqnCGvRAeBainqLHMarpw7YnAcanYDGdQ1-15CyZfvOXQUl7On9gybdIDfAGPAwsGQlIteUHte4gG4Kce5P8rxI4S29IdIZ2Q6233PtoXEHGl6LKnulMEwHK1g8U37ajQlfod-VepX5PtXeoCfmectuqHZdeWHLpqVSGP5FGmuhAKAn_R8bjtWFhL8gcp8bY333a_XhqnyA_HcYztS_b8PJTd5OPGfy6L2LM9cqvyy1NqiGSJNQ7iRdVIKnXtpRoHzEww-4uT871OjTiPxgqRZulncAhTra87EG1usLoiw8DAWHXvUH1sTd7swkeClZ6qWNqs7u0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay3_YcK4za1PqZVFGz2ia0NyW4tUVarjeOZTNLp0ulVwpf24i6jCrWj-1SpVrw20J9i1gU_Ez11GDaeisQKC7v8AUsegj2PntEcEf6f1IBCcnxaithJv1Ap8RaP0ZegnGELjcJ5uJlj52oLlIY25Xj4m8_6DC4WtpWRcPTWwpMtNbcho9rBZMGF-JNm2JrAFPU0HoundIobNKynGirmFfERtkAu3__prVJgocewD8gDO1-05M6naO5T84XWa5yOVeRpcug7uEvwlStKjkuGDlJYNW03D0cXky5zLPAuSA8MOZZpBHINQtUuw67Zq4dt5fQimm3eiZM_BikukFZvlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=Vm7vCYUOBRdCc5W2qjMGbJP4BjCklL07jf98Zj8JMU-EbaD4LWmbhY1UBAzZaAwus1tTUw0lWwUaF6lvQvMyqv_2kSkumOlwwEZM1KFb5whH2xRjXjQduX2QxPKjl95qSy5wrqpZnfVLY0x9FL0FMq5msqRVBtVwGrFfJq0noMVApnhBEVrqm3e6Chryh2BLZNTaZoYo6z9RTP7llUIqnNB7N0JyV6Eu3MhGsBsqQ6tduJe4KgxtzbyDp92h1KQGD2HSeA15G_F_EsM8XqGsMn-goD1I9_i-9dVeQPrt4qbVIMQpl_D4Rxt0m4MeWhdC9wfbI5P4jLms5jzaF8PYYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=Vm7vCYUOBRdCc5W2qjMGbJP4BjCklL07jf98Zj8JMU-EbaD4LWmbhY1UBAzZaAwus1tTUw0lWwUaF6lvQvMyqv_2kSkumOlwwEZM1KFb5whH2xRjXjQduX2QxPKjl95qSy5wrqpZnfVLY0x9FL0FMq5msqRVBtVwGrFfJq0noMVApnhBEVrqm3e6Chryh2BLZNTaZoYo6z9RTP7llUIqnNB7N0JyV6Eu3MhGsBsqQ6tduJe4KgxtzbyDp92h1KQGD2HSeA15G_F_EsM8XqGsMn-goD1I9_i-9dVeQPrt4qbVIMQpl_D4Rxt0m4MeWhdC9wfbI5P4jLms5jzaF8PYYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF6ZFcu4Ko4LZUF0tDRoEefJAO9N2XwR4Miu4ueykc7m1MnzICrk6rOcCliWB_13-7hh9tHpYwOvKai27cc8Z_IAISf4vjYlqQ16g33tOhGXwwtT2hbB68eO_3A3pyUKwEC8Cpsb0Bz5z-FM8N-Esoyfqj4V1nhv-edpoNKm4GtVPxyWrt1WChfJR85_J7aYWR0l9Ymy2UCYeuvWT-aDqe-eTWnRqPgtvPxvuPGzGVFmnce1CmHzzVTDGgiNyKLoYPT1625A1kuK7Ry3NelqN8UmRN9v_yISEXnbsqhUAy3egnT8jKbG9gR-3bCR8kekD5LwqtGL0cjRv5DDqKH0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9j88sFk_seq1mTky5YQ8ExbQVjEYBLMoBgb_bafG5dh94kVoT7Aub6yaFCtNvXTkxvic7KuD4kfkVHNKDCIphqYZz9TY6tMrE2xTFA8SRXLPjIvBNNvWoX47dYRcot4SnyrWZ3zjpXFO7VWGOkSKhaqg92ay09RvevCAbL_TlHbZaMf7cUu5J-TBTeuDtu1x33BF1_2rl8l9_fzTF-DQycRVZNr10AT2z2t24F4Ds3vieD_AV6dEwuq4hFhzKPrM3Pz6F74xbZzc1SaXVcx54KHObLuO7ko4Dhu6WudSvQRZxrtke9VLrrGHbu3qD1_26RLx0PxGEfPa7XoyweKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adOgAASCz2hWamraCVYhgO-_HaUgpS-wWtsgRjv3gzf3P_EUOAWAtTViuPfcv4WD3rPvISSoeQmpIfYUULZFv-RO34snTh-Cx5nailJghRxHAgDkrD0XkXABE6DTMO4O4Eqt9FR8tPDdCljx_jwiCMg7oazcxUilanx_6csZ1P9NY2UJVNgv8jg6GWt2opdqLTCbDTewMhAnPV9EBoIROrMemUeoeU_DDXx5HyPW2PUp-ujHuAWXreljZJm6oXZ7eRb6gY9y3OPbfzMMTeZGTVujLK8OnMmuSUTAk8SSvZTdG4niB18zQs1JoFeX-jjroLWTr9nIHkAE5tYuFg5AoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyY9wfndZoIgIjJta_zl5m_0PCNGDNDLfDnFtVnovmnGI0QnDHtG6AWYLWKlrhn3CtCeajkK-h8-91Nd0mRsOph9m7aDF-wg-7t5CiOynfusx85QQg0f8MQHci4PiBSnT1sVQ3jYfUeZ5kxoHi64sNVS9E2ic-D4aNwhjhCpPG1b5FMNRucuylY91de10ZGfqKSjn7z3IyzRs-4BujDsYRZSXeYExplIRBV_1ne-qwIw6757wz31CPORFJj9TjyEMtSrNwsJi0Cf5Jl_Ey6Y16n1eYSz_Ffk-TbRaUPeNhV-LTT4PNMhoGw6Aqqqmt4iQGyGJphWt2MIXDG_4lUKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNDB_o8LpwLEAPm5Ol4dHnugV7DY0cGn1A-VTAsdjwDbYpw4GKGganeOZ_DmFoUVM2l2ZLOrUB7hEL9KlOCYjip7fNHYpGFFzSqmZZamyqsArRbnQ1iuTRvPYy6IJPhmDkXb10Vu4hn4FGppizxMM2YM1RKclu-X7FnBrBmNexucg1ILMOmna0oDaVCD_rYpWgX_fpYHrnpEKJKmARaWx6fIfY8UAm3XYsLNOi7fPAdilRevuFTl3arMoJiWpNfqV7e3guqE45ms0r6hb7qXG99wF22bEKN9F680gn_wXYQZXv_IJg0IoLnOwBTGbH1uiR0ARhoWBKHVrRR-W0Zjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amuJc2jS2vpaDplursd2ix8MyXfL_F0wiDswCR29ada_VPEL1b6KY9C73hSn4H8BlkDHBy8vozUUrPLnn2kp_Z2Vw3EUMedbwnzC6ms0aSs9bKli09WUTbetlsSiRypPLO7Augj73djm13pcgIKMcjkg_Q7IKeOP_jFpQ8zeF-QytKezhNAcQ-jXDf76WZc0fFxJObhjIHsMAbw3U4LNHvm1z4qLaEte_8dEMfydfKHIsVxgPsXd0T90dvMOsOPuOGnVKI3tR_2oui0sSk_X-E8AYqMsDdBRuq2A-XzjF-qfTCo55bs4Bp_uDO4DRwyslEhXt0dl4g1nxuh1a5kmTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWCz2366JmUPtqu0agu9E6lKaLOjYeWKx3uwyN4Nmw-I9NCTOcE6MUE0gbwnrr66j-oVzolFWWXP1hSKEc4UAusH3E69iksmzmc2rIeJAi411nfOseeGRwfRXPF4bXIIydK7A4OiCAw4TWHjG3qf2ZE5y3yaTT-xJ5GYbltSLpFebkowaxoYUuc9MKzsC6R2Sfx1CphNzYF168vRdJ2HfdLDJzRl3EVl6WtWwpwIcFElxDkQ55FC91CLuk--2rceLU-iWfYnv0gSB5DGVSJMNyJhYaEdj8amzuAqgmxDozUoPPmoCJO_OxzSdZiVyWcFhRlf5dXAgCuD5Siv2jGD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMHOgxndxiP9024r2tKnkgRQ4RtVx33bZB_PZQR8H3ZOu9llK7_rTMRnMEDwVChWnJ2m7139Crt16DCoQ-hwWY0melprHAKPPepNPgEZmUrxJS4qF5ILW19fCAvvHzZOfdrA0nzuZZ9-Jp9aXfAskdIEjYk3wfXME7CYTvsGbuginZ61vbIbCRkWy4b1NUB7MA7wFAubD5uFO0sDc-SOufbkmt1B0ymnCyuNsCiIpg0LAMdNPX3Y050kYHNV55Nync4f061ua6Z4o0NSh4By5aGqvyr8Q0pS-llQu5AHVZtgWnf43DTiJXb2O0swHWFpWrKU9XITFBTjEZpexJlxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=R6-z0VpCJJRdr-IGfWConVUck0xxQZ4dQ1kZOP7rIe2C0vBqxTtEA012yRGjtiicmJZ4o3-Kr-7tum6D-gZ2NJ7Oim6Rp9nOGrvF9T5LXULjVulA56mAumgYV70xvX4uJAP_1x9ic8PIkeqzPFXdqZjhf66mN2Rs2sG-fdYcUI6kxoHa20ER-39MhNTozqtokUaF8vq7DZguoDYeC3kfCKwonwcW7WpdmP7NPRHpSp6IhrI6T_cXt6UaKPKS9gdUboucr25cFWiXtZkXoznvQ76tsKc8JQ-yGaKJYxogdTTmvmy0NjP9OUTOnTIag7xaDP4hASrh3vW4m-6_Y1Dh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=R6-z0VpCJJRdr-IGfWConVUck0xxQZ4dQ1kZOP7rIe2C0vBqxTtEA012yRGjtiicmJZ4o3-Kr-7tum6D-gZ2NJ7Oim6Rp9nOGrvF9T5LXULjVulA56mAumgYV70xvX4uJAP_1x9ic8PIkeqzPFXdqZjhf66mN2Rs2sG-fdYcUI6kxoHa20ER-39MhNTozqtokUaF8vq7DZguoDYeC3kfCKwonwcW7WpdmP7NPRHpSp6IhrI6T_cXt6UaKPKS9gdUboucr25cFWiXtZkXoznvQ76tsKc8JQ-yGaKJYxogdTTmvmy0NjP9OUTOnTIag7xaDP4hASrh3vW4m-6_Y1Dh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDNL60i8tDOeFClGpcu8z-BCeEj03I-_lLfK1_enTJ_7iYBWLLFB7Ifn_DaYRRZG6YXRsAtXXayDixAuLV5OpVNitupAInAL6l_iWnlyrBj_GBARl_l-KaOrliMcLFU0eH6g-HvnlzFagUs-_C9NzEVF_W5TFa5a0SSwC8lYcOBW7wffCEn435WOs0rQxNc8fGwAntLS0Iy0FYpt441LDqLpAZN1cjYoiOzh6QchZ3rYygnpXrxhbFbFqo6Akr0jr4Ddl7bkVoonQBcUFCm90S_T9TpWsi8ivo1E-KahdxvPIOgyHrETuVaGcWQ4tNSz9fDkd-eeNAjpG36PKId4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eicmgl56bqDE7pu0pZ6RF3uryCeKPK6GUCU9gWO0Y7pPgLuHg2tx-58NA_hZKpoFlkC-Qyxl9baR_qs43HRBZWvti94dPoxwK3djRE61-bEXSCwzp_PbXp5ZwJV35B0od7MxWa91zQv_1RSqge6lBNoNdXZY8W53DtZr-AAbthxUHuSmUPlmwX7STKq0XmAySAvyd8iPl4g8FgFeSDoHjF3Gn_v6X61SbIaicZoJ4f2J1L8y4XKtdnie554zB-ij7wjGXt8uYrcvaRKg6tpP9lzvlLug6kl57npb4VP-8Mi3PjYM-6Cx866os4-C6H62mNwvU8KFHZLnUHo23NkjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go5lr9sTq22FuyejDBT3XS2qB_4PYHWtJLzVGBka9_O7HP0hmDzcN7CM-c3k4oX18J18YHYCOC1DnOeD3Xu3X5m_jh5mMcWnSEJh8EuLSasenJ4Dn9pWKBhU-76PbdYDXIHbmDdF-sGeSUJTFWuJSst0EGNEH_zSuWtzU6sCVO9YNYNMHAdqovxLvJwJmkgsYu-k1AqqVo0BFsiQnViETDEiPb1iZSEfH1E7SfQeoKltpbtCIVqgOhD3RE5SBTC7B0ruysoS9BAjhP17WUaq7zrsKlgH_GSp2i2wj0Up5jDA3XW204flIjI3Y47bo89eb1qYeIlIjwhsRV3N6d1jYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY4IE5sskfCDD5evkuPBHoOy-4Y3wcwf5ur8ABaxPkGpq0nAf5XlOydw9B3ivkOIkr5CNAWbCEEIhPBsZOBl4RENzgNpKtPdzavXcmRA8NxpXjTbm9lmCVS5dC884-gJjFO6gGDyzKd90KZQpReE_WeNzrZuSjSdKxVDqXPffNicgU4D13Sg_U54weXL9XBuvrjUgbJm7A7EUXxyRH3sOqOX5D45ZsTQNZk4L8WArbZnTrirDZHnPKGrPy4OEt195HcSITUeyGdDp4tHzOhLN7L2e1l7qi6VvX_gQsT8Qs_xoIWF96htRuA9JQRDyV-Z_AamY2IIbL10mQ8fPktXIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=XM5829tn0hNJ31kGN7Teko7KS3ADNoSnsQyvzIfe2Z8CkXcN9lVxxUDczmv-GE9aOrMU-rJh76e9VTyNk85AD5dW7YoUeGHUdZNZCbBkz8amqF5Iy2yUrULsLnYq8jRTAd8fDy2KkV_Mn39xY2eFcBv23UJKHDaDyxyZjfANwSyXgz9ymtn_dIG1VB4YhID9TpUWIQgTtFmfrJQOD9Did36vHueMZ5JMqUs8HsvjWtotg0Bg-UAhoNkQblSOxyzMPMuoxTZ6de5UDf4IFRPqsDKggMXCDZQR32gg_gXl3XXjp3iC0B2k5kK9G6K0VH70PNZUoTZl0J7ZzZC5uQZ8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=XM5829tn0hNJ31kGN7Teko7KS3ADNoSnsQyvzIfe2Z8CkXcN9lVxxUDczmv-GE9aOrMU-rJh76e9VTyNk85AD5dW7YoUeGHUdZNZCbBkz8amqF5Iy2yUrULsLnYq8jRTAd8fDy2KkV_Mn39xY2eFcBv23UJKHDaDyxyZjfANwSyXgz9ymtn_dIG1VB4YhID9TpUWIQgTtFmfrJQOD9Did36vHueMZ5JMqUs8HsvjWtotg0Bg-UAhoNkQblSOxyzMPMuoxTZ6de5UDf4IFRPqsDKggMXCDZQR32gg_gXl3XXjp3iC0B2k5kK9G6K0VH70PNZUoTZl0J7ZzZC5uQZ8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4SGHA4E5T2sxPt4TT17Jf8ngmy9VE6izPmUTi-hsnDCxIEqpmP_1_SU-2LV1fO_nA7M60l2CCyWVvJi3fSBnmX-uFN1UISSnek6Ag8QPqep9N_qTdqHme0Fph-j82c9N7CBs297XdM4USgSNRU7WRGxwpqGei1PXPGA8u_K7r9paRyWdBJy58u-f8l5yZl_Qtq09fPmWy8ykOYNP0eBuX3xpAXwd4shXKfMDod9Vg1lu2sYrBrkE1DE6nM1npUZKsEuLfxC2fyM-JijwLsmEhCvxFazyoQIZuVl4Vdy_ZD4S3dlBciawUVVbv8epVR2X29V6lqN7b3fxcPh0h_MYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI94dwQRrgR4rXsIa5cno9Nox-PJ92zYJDoLsAMkbFZ7LBxAatPMyWqwukX1kDqGbx-vRWwJ8pPnlM6Ao6qKYVElKqSCkX0ie_2krRcPtqxg3gaXXDg61goPSTsgUo05axT5m-T5SJXFphkxZsNcIQvOuz9GH98rv4vQlJDfNw56Q7tkSAeNGJs0GPrKU7ouTstvkHAl9eY0ONO0DF_EVFqKfa046_zF9ccYaaX1xitk5oP6d5FD1ZwmPQjhuJsqnLecXqrfeuRHBHueo1XwCPiNtFM7BZ2u3Vf-PNFESG-rThOB_iCDm6C-bbAEUA62hyTV3dW8bbQDPdMn792L5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NurGAatkTFsYYkCv1P-S1Q13q0Vt-PDxa89ut5NVKqDuPfkwcf_aO0sfoN0wue0FuWEN_kbiAyAykbsyOUwBKjHj8EiCFqiuO7X8mDo-relw5UifJV0OdeVOjKVG_tzMrPRCdrbwAlquxW6fUrfv7s5f21b9MpJr50mpTtwaA-xCvtUsseEKXiZVXvQNeNfnfh4qhj59NGOFSBr2X3xstUe1m74Px8kqLX9MMiiIy4o5-FbSeIBYApQxKMG_l7jAMKU1jOriwPs2yChiOwoRl3-U4ftj831yxSfSAGVbwP5Ll31XvTSmmSMd9kOTb6bb9rOuLO8u6W3WPSt_jyGBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBo4meqm5RAGBQajGdt9pudrSo7Rpmo-fra7fw7IU9XBC0aHsAZNdrn1awKfFopS0ABDpKkQgY1S8xt01wC-iAS2mAzgnOg8DTXiMWDHSOWOsmbH7TOlOelygYVDMsSb3bA3hjYYSPpuQzR1sHAhUXyOh5HB2L75tX1o8U6CjtwAlB74Ib0zc2v86U6C9vR_OXY9VsgjSuezByjjk6n9Tt2QKwPQ8gXf3pO_bh78ruCR1za4EiBLPIiF5egQbuQr8OaSUaaJ7wrex-dKhGHn0rOZQf22I69_GdjbJ5g8RqYz--GE323KOV7CUzdBp-w08fE_O-anx-DbVKDV1L-5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=F0fBUvCaJrT9BpLX_q-ypmfhcyId89OKbjwCZEDAW6ZMxjBX23HyBXWpRNg7h-HDl5o5LezVqbRnvOp53DfkRVI5t8ulm4RpGEG4MZOXwE-JwkmI0fj4NnWNcNd4Jmv3TzJ0xZJHfktb8pHV8z9toaGrffPQvNmWUYUzO6RuI19JHgJtzZXmbGyiSR06vgWhgQjD8a8NhtD5srIa0VqM6WydMrsmZYcuMZ1xbg6ywO8tnnJo3uzjRsn4jK-Aufkzs-Eyyv_nx7kAUMS6I8H3j_HcTqTCypacpxIAWhZi0mVvOPjPJqw-YQ_MYtXYaol0mvXVyIGB_jCKeGVI70iS4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=F0fBUvCaJrT9BpLX_q-ypmfhcyId89OKbjwCZEDAW6ZMxjBX23HyBXWpRNg7h-HDl5o5LezVqbRnvOp53DfkRVI5t8ulm4RpGEG4MZOXwE-JwkmI0fj4NnWNcNd4Jmv3TzJ0xZJHfktb8pHV8z9toaGrffPQvNmWUYUzO6RuI19JHgJtzZXmbGyiSR06vgWhgQjD8a8NhtD5srIa0VqM6WydMrsmZYcuMZ1xbg6ywO8tnnJo3uzjRsn4jK-Aufkzs-Eyyv_nx7kAUMS6I8H3j_HcTqTCypacpxIAWhZi0mVvOPjPJqw-YQ_MYtXYaol0mvXVyIGB_jCKeGVI70iS4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=S8EfTejHYROsDYU_o_CzrrRsAAOpD_IrYAZJjzdbYLV4ZaEuCkO_BQGyhS8cKvMMcK88gU8hsNOa8x1EFieOHYludjSsvn3CuSENmxf7_XFAWWjiO-_zaO-McDC962CGEPm97g6Qzxe7eNojJdDwCaDFqBPEmLL3QNI-h3-fNAp7w1tiMSqzisJa4nOmSqklcgRV9ZGM6mGqMKsgKYhwegd1vZ4zXnOaCZXKU1AOsTNZBLiWFwd9y76CkCBrLtoIa18qe9qQX-l5XoC2ZSTqJ2T3MeWg5CpZk9T_N-Iaqvt0EKrTKrBFmGXZfgFFzMwif5EsX-cZV7j2wSzjsMBDnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=S8EfTejHYROsDYU_o_CzrrRsAAOpD_IrYAZJjzdbYLV4ZaEuCkO_BQGyhS8cKvMMcK88gU8hsNOa8x1EFieOHYludjSsvn3CuSENmxf7_XFAWWjiO-_zaO-McDC962CGEPm97g6Qzxe7eNojJdDwCaDFqBPEmLL3QNI-h3-fNAp7w1tiMSqzisJa4nOmSqklcgRV9ZGM6mGqMKsgKYhwegd1vZ4zXnOaCZXKU1AOsTNZBLiWFwd9y76CkCBrLtoIa18qe9qQX-l5XoC2ZSTqJ2T3MeWg5CpZk9T_N-Iaqvt0EKrTKrBFmGXZfgFFzMwif5EsX-cZV7j2wSzjsMBDnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقدقرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqDXQS3F1E-RfqPwFpThDtHyFxnaTssjykKlMO629rMTRKWd6gpwP4TOeTwyW_QbP0SyTa4IdLQNu-bteAlzhHbCxtZFH27ttKO8plNadQD77aXx7vwNrF1oFkONk7dQ0ny3mxfqz72psDF5gVG9oZGh31JvdAu0rt5clrrrZw2GLEisTOZLP7_bz_G3pmIpIKvT6JBvjkyeqW0GHutr-AYT5mACXjgr8ADmz3MyDfIlwCdkaif5_DMt-aGPGC0sPv8H0TmPj-CMEJv3hGixRK_J3o85tmdeoN7vesVG0YlZr4ROjvKhCzEh2m0k910W837ZpjG7YWvS6gFaNGIEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVvawnArqcYIkuSdrdSvPjE64CReCDb-5IbkT9aCEb8qLRFywQvZTRfYlE9PJgFsTWiFMgT7vhbkJpNopoFL0LzdENdpyi3D6d36FQiqbx2M5-ff-hNKIIP8DRNmcjPAqv8iZyxMcqtIspO2P0wvAmoYlDVDKC-Dekmkyy8QWrYZ3LGJ0UvVRYHgX_Jgk7WYoJ5YuAGqo4HE1yK7-CZPVjccM_MHlBb4Ay3f4OJd82bV41OW-xQmQctkwJs3T9tUPmnopTeDh8C5YGhmj1BHw80MuKbV83jWlHfV6UFOb-pxfYlG5kCTSmTawYirL8sXX3TtWSDDmUdL-Z0tJKjx8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=YXDug3D_Fgbls4GmypyU2iRn_OBh_mAm5xkW-_xxtRrT4jwTWNm7aIutZhCDntr5I6FyoWOpT4hrF1QIyIBZayOs3SNQxJo0HX3Z2jm804oX__rX6OMPKq_XJTSep3sHkFzUJMcFUzhNNPDFCbjchuOObxo_B7WtbPDm0y9ycy8h4dQsq_lo5XPTEuMuDyxpxmn7Ad0p_d0MqEwQLZNznDLER7uMaLNRvRQf6kEyberUc196Mgj5AqtZroKxdfuB3rpMGlS5yLeLJLAeLq8b0lQOJbmU95XmoTaPsVoky-8VV1Rciu_ltzf2UvOsv4xNoD_EejjySE2eq1673ihzXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=YXDug3D_Fgbls4GmypyU2iRn_OBh_mAm5xkW-_xxtRrT4jwTWNm7aIutZhCDntr5I6FyoWOpT4hrF1QIyIBZayOs3SNQxJo0HX3Z2jm804oX__rX6OMPKq_XJTSep3sHkFzUJMcFUzhNNPDFCbjchuOObxo_B7WtbPDm0y9ycy8h4dQsq_lo5XPTEuMuDyxpxmn7Ad0p_d0MqEwQLZNznDLER7uMaLNRvRQf6kEyberUc196Mgj5AqtZroKxdfuB3rpMGlS5yLeLJLAeLq8b0lQOJbmU95XmoTaPsVoky-8VV1Rciu_ltzf2UvOsv4xNoD_EejjySE2eq1673ihzXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=sr5D9fCjKHFVxuQmm1yQWlaJqQ-HdEpQxDQDVlNgCY66dQiQILc8MqWxSKm2hP89J6118g8Eq5jMv-jYV4cGunyOhh-gZ9oqcLohcIlg9_su34nQHcHmayQSIVw3DMFZtvUVavGLEhAllhQGkutfRntZYiR12j5wTV6np6jV2zSCIzeHTLi9wVmTrrpsPSZUslS8oCgUKUaT_D6RRB8ZNgOhX3usYGoai8gnjFWbbVyZCOasFy-tdAosRUHVdbmXI7fJbMchb2yvF6ON7QverbLoIMeRkaC-Sv1dy4ceWLThuAisDOQDEFS54tiNfQJXkXAKzBuMd_mo4f-7BvY7eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=sr5D9fCjKHFVxuQmm1yQWlaJqQ-HdEpQxDQDVlNgCY66dQiQILc8MqWxSKm2hP89J6118g8Eq5jMv-jYV4cGunyOhh-gZ9oqcLohcIlg9_su34nQHcHmayQSIVw3DMFZtvUVavGLEhAllhQGkutfRntZYiR12j5wTV6np6jV2zSCIzeHTLi9wVmTrrpsPSZUslS8oCgUKUaT_D6RRB8ZNgOhX3usYGoai8gnjFWbbVyZCOasFy-tdAosRUHVdbmXI7fJbMchb2yvF6ON7QverbLoIMeRkaC-Sv1dy4ceWLThuAisDOQDEFS54tiNfQJXkXAKzBuMd_mo4f-7BvY7eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxPqToeoX3b8qi3ADO0dBXtOGNRYkba2vib4gEyQIx4IHYetMMZMuNtuWN7laffCNygXXmKIFWuDFCgBgiEVJEqJSuYzthm8P-lRo3aQrvJlErnvae9RV3J8Exqt_6svXJBeLCn8zINDZl_n8m_OEGDZYZDBVnSDNg5wyJ4G9vNopaWak6Gm_2zUz2NG7ihl1sir5Qnwb7YWgm4wO16a-YlWlxlbbwgkEe1_il2PDMnixC0gaP7JotU3jMHqb80dff9kYB7N1edbxRvh0cq-0J8hsHVHmRifmI2hhzQ6izorYGJ3lSnvWh3wM2GU4TdEKfsPZyMcg__nae58HkfRhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksuZ2ZDRea29z7C7RmzpbyQpJZniHJDuyhV4boYOy-PKn6LYqLP4xFiu2jcOH5yxIP662oiLrH_j_i6hHxXk0Y0uC9XdstiPLeFCb4ViJw8zF1AsU-EhrshpyxqD1LMdr9G1M-IniON6UnPgLwBxo1ae9Fgf_hyRkjNrvZRNdQEaiT133HTgy_Pdun0EVHGJqRO3X9yr9yWfHfOHsUX6d8vWu6x0ein4jysNxpJjFNQsZ2NTrorMLwKN6FvBwkgA1n8NHO5aGqTCEQ5kK1xfFdwPlMh7H98qNn0oIB3YUmIFsEC-WWEsTG48EzgfC6fwfxZX6VFuvU7aXHnKlwLkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1tnHr88pWqejZE07abNjbigv5bAQ8Am_zoC9BMGY4Nu6ta_LEoPu32o7_UhZFz0XrIpl0t9_bSKmmqWu-svyXHJ_EWP2Azdt2EIo8KPGcdJVzf3gaPG7770B9qEFeL-7sUZJOeQnRcv6jnlFDmhPxHfQyR2iZ2qRNvFAzgZSsTwPGyrZZDmMiz1nHz9ulwr1mBocZpQ4ci3mgFEBdp8cwxTUW-JoR4exJf3u-myAFiDLc-pW4FKAH6ddHAGv9vFFQO6Eptk2VSOxDP-DWjdvjcoP70dEpcGtZuGM4SC8ndKEjkCq_xAGMfRob50zOp39IT3Df5DSZ4UVyg5J6efzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=cmvDcFwaFDZfrkDwcUD8Bj2U3w0yRYodkvd_7jMae3_FcNKvGCnzcx_02hYprkXwPIZFe7g36Nn3a9YLZIFTWdfh-Q85Q-TXAwRweNtFz2Wj0a_83gBug-QHvXw8Rf8UDDXV0omDEGwVhHXKjF7e-822D1UMN09VQabZ0e65q2bDzl3mzPvkO2koQbdMmmrr0Ody5XoK-aOYFZz74tABNjans1CFWc9jIhy20WdMP9qWrpZRNiwuBeoa8lAPkIjV9htoH_7lS4MScq20QRk_b9d3agxI-a07vY_m0_qkAhJMWphEzkWFRRdZTD-jGslItgBAadbGi2kALQAy3H0aPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=cmvDcFwaFDZfrkDwcUD8Bj2U3w0yRYodkvd_7jMae3_FcNKvGCnzcx_02hYprkXwPIZFe7g36Nn3a9YLZIFTWdfh-Q85Q-TXAwRweNtFz2Wj0a_83gBug-QHvXw8Rf8UDDXV0omDEGwVhHXKjF7e-822D1UMN09VQabZ0e65q2bDzl3mzPvkO2koQbdMmmrr0Ody5XoK-aOYFZz74tABNjans1CFWc9jIhy20WdMP9qWrpZRNiwuBeoa8lAPkIjV9htoH_7lS4MScq20QRk_b9d3agxI-a07vY_m0_qkAhJMWphEzkWFRRdZTD-jGslItgBAadbGi2kALQAy3H0aPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=akLXkGWmMiAF5sDiGZJF5eawtJuLhg_UlS6e82GAaqClciMQ23fp4j7hgyCRc9YjDHULfxuDEiSD4lZ4bvVjuiiaA5qbok8CsF4YhOaiw1Uow1jNQI5PbEHVct9wEJkI_LaUP7lHvmJ8v1q0fFwAf2o1UE1kVgPyQY2TYpnyWpTo663tgZHwqZ4PIBbiOKp2vPp5h1WZHB602PtpqaqOFYJgjE2m_7OGwU6MQV9gYPOfiufcu7QxlLamk8RVzZYjCI2FBuO_6U78SJVsa_YTbPuFHpNtxD2ArvkX_KtZFuYfwiIaSGfmX67SfENPXZ6hZyFQ2ORJMEYbiMCFx6AYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=akLXkGWmMiAF5sDiGZJF5eawtJuLhg_UlS6e82GAaqClciMQ23fp4j7hgyCRc9YjDHULfxuDEiSD4lZ4bvVjuiiaA5qbok8CsF4YhOaiw1Uow1jNQI5PbEHVct9wEJkI_LaUP7lHvmJ8v1q0fFwAf2o1UE1kVgPyQY2TYpnyWpTo663tgZHwqZ4PIBbiOKp2vPp5h1WZHB602PtpqaqOFYJgjE2m_7OGwU6MQV9gYPOfiufcu7QxlLamk8RVzZYjCI2FBuO_6U78SJVsa_YTbPuFHpNtxD2ArvkX_KtZFuYfwiIaSGfmX67SfENPXZ6hZyFQ2ORJMEYbiMCFx6AYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMlbMjUGkEf1K65BxJDWQvDp6g2SapEpU1Yqh7nBPC4clgE-sBCIbDbhDrAx-A7EjUlKE1-WgXNGLhqhRSHTaHKAQxrVJL45WSQk9Wo7MvRh0jmO2SCb-6a6PI8jYAqO9_qRKJj9A1I4cu53Yi2XUaSqle4faGhmBjSBjw5i_htpPYbNlJJkQRNo6FfApCJWg4EmG9XZkaQ4f2n8-RT8ccY5bq_IZunXp07KYcjRRvut8-WhPe8tOpTVYoZ0Zao0ri5pZ8VkRjSgxzgIUS_8u6kFc19wts9YftXyqG_gZ0ZJ3s9czuhGW6AWe2KwU2T1Arj0SiH2t09sGHOkocvPXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du0uv-5lHcIpb7-cV-728BHrwZvWRNTbbTvIwTOlA3p_eHGppkSdOsduO_fZMB-lfrnjw716CO38ceMgtE3NXUWuKKay_YGeNfoMoWc1KuIVnVn1lBahrm8sd_Xf0JOy7izUxZHF737Y9H-3Il3GZrpY6UC9vtV1JEmlZ7anv9iQwuhZg3nx3LkgcUOjHDct4pQv0UFIi_CgPf_c8dy_QESXJkv3ldyfYSCvy42rJUeq8VTXGNP7Qfq9Gp9okrum-OwEtvffV_tWZ8HCSd9rGqRidVwg6hj1nLpCnBM3Ni1h5NqoKRwAf5YOwnmOHVcpT_tOYWAwThqV4nEL3RXAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SifddilDJGzHjUx36kr4P7IhYd80RbhIoFkkywk1lUgLbRa40TsixFBPjib7xjTCvng3EnO5Wy-ZOLl7bmOZWAzGJKOQ-d2PjFv5neaVgUzNfR4Eq7sGOmOgCA447oq6hrfGJLQvWSh44u4AjOVdUNiL4RzhCnoXtezXbGQEoftH5Ode1dPzGjFWmvkaE9E9mLDR1GWaj-UZxXTiMGL6zAR4wJiAACnvyeljdpjVTWcRPP4Y-RlGmzQoTc6ijKiV4YPbk335jO3JtZLPNrLirbT7KWp51tfM5mr-eIVKXkf1DXo9KTQSuXtRJl5qEIVc6Ibwy9cwlvF9BEz9MSmNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXpzbH82oWsuJBuki-wZ5YIQmUQ-tlP367zN-bu5W_Xz6KVzpnXKlSkCIWfl_N9ke2WTks-J7MGfQUuUn2pLR2IkGOBMH80iJehZ-2HJS-w6WblwA9IdWfAk5RQZHbxlNAFtRFPMZuQhXBD4VYxJdW4Xzl6lfOfotcWsHe6_838RJNTPk20tjnhVx3mu1GZWA95I2XnOJYohgMK5zd93BDoCzKzgujcaNNeH2E4H9YdtDEq34-rwOTkK9zwFmAwJouLljLKGS1Ut97GEenkJ5vU1q2CbwlF4-T41liGEIRTokQZrzw5egQ7BdR8r-8rdF_-Alhbmal-nq94h5Ko5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIl8QozEINxhm24c1I_0AWPV3ISf5QGNy_9NFM_1zLG7tToQi1nwjNTGgwiEbrjnq8vzMnfGvpw8iPVUvgAEmrfeKC7NdkGQZk0BYgpe6BXgzgaBIE57Nawkn32qiy8bnoS6PoHoFM29td6q6qBFe4uWpbnOha5QxLwTFRQvjbKrEsU-xwIL3ewisU_-6Ydm_IH_1bPr2TjI3M8DbrzVNfSeSdQcA0ADQ1BpFuSMGA3hypo9ryW08k_ITk025yzVCsF06pKjkQWRPrVO0L0yWo_WYUARvcno32MoTG11EURhAy7bkZ1kBDjoJ5g3_Kebqg5rFnilN5vOvsnNQ9lQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoItJv4BNVwZ8mGFUQDzeniM-G2EQZDSgki_-RFHW79HalRzxziEh_5Cr3SsdVmtDiBq78dJfbV-r0scTU0AkR0DthDE05FygncyalJdc_K28lvkuAKXItJwoy7wECoSlas809OfyaVR-dEBKZINlntGRd09t-4cJ_H91VDpUjBXJP6xrthZ8hEDoXPzqlNP77g-GLzgVTpgfY3t1GsIIU9KD2MCVkR9FATIoGYZqJto--aoqS0cXRn1jeBBTZRn3agAvpqBBVwhhZEs5JShUfEjndXxRGxgOOHqFxCJ5ARNQ_18vPop7daAxh7MIjVMqelCw-jBgiC7FTpZ95rjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaMn6_3T2DcWXd3vlGv_5JccyePfbVYeZlVqmx0SoX8-VFaeSYcCuEkI_tpj2MXc5JCbRs4z70wA76zvbnT9Eoti5r8Ht6cXXNLyl_4ffJVqhUdQRY0KksOPaox4rxzW1_6WbVaSd1nCxcjvHPB6sp2T-isKNkkyAds4oapAcdXf8ER0rJeW9fQ8lIB4dVF-zmoNLslaOKEHQFdZws_qZ7zdJxzULfCI0Rj3vtMecWk8d-n1dv1iHO3tM_9lURAktnywu_qECPuk1DCRsrXY2RCzr6NrPYNS6ZAYXyInGSL7sm9LM3pJmTjMA3uTVLTCUBoHHtiXLSVVh-8UKkFb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfBUgYZ9mgWn09XTd9pfn49Kh6KwsjQWEXnoQfKVGQqr3QxRNYPh08Ocr8z_j6ChxhznyOyHlZxujjVlvofoVhypTL07tsmxRfr8KMCBTvRCB_vS_Fu2x3Jh1DVJaSe2JtPY3_Tsbpl-GQEJV5DoueR2nKAtFiLBGGMfEDYT3NuOl25Gyu-m9cSG83fema3Oc9JgW8LQeJwDfiKIEqI4L8enz5lZhJ9uJT6VOQT64v5mEhXJDOO49d2t7ie4a1Tt1_wFWP35hzDM-kyZUlERVGvrkPHXt77893DWbTaWg_tF2sCVo-e59IDPdRWPk7a9jDcPoQrDlcnYXIIbO-89uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=qdJDDrEMu0V22yd7-lB6ESo9gxbLzayqNvbA9a_l-5mebU3stFxXr9yD4tO8EfXPbwimpMm66atkAigu46gF7nHZ0Rg1xbJ2SSM_vEN_F5XU5WusrpGLG6AivWNMclif0jLDaH4gPwjA1qLFi2bPDyV8XSNb5vFgaCvgTgjYXZm2kQdvuxpP6xezSh2-m8zF54enfeZuKm07PrKEWk-FSgLrkwCLLsBCopYtPlyhNbQZwgMaoSsb9BX3ZV1aDTjEZz0-U7IEaw5suCTq4kUL4VkEFH89tU4q2dCt_LXbH7SWwLcnpfBqeIBC9sVH1VkT1_lpdDP29lTSDI-S16Xt6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=qdJDDrEMu0V22yd7-lB6ESo9gxbLzayqNvbA9a_l-5mebU3stFxXr9yD4tO8EfXPbwimpMm66atkAigu46gF7nHZ0Rg1xbJ2SSM_vEN_F5XU5WusrpGLG6AivWNMclif0jLDaH4gPwjA1qLFi2bPDyV8XSNb5vFgaCvgTgjYXZm2kQdvuxpP6xezSh2-m8zF54enfeZuKm07PrKEWk-FSgLrkwCLLsBCopYtPlyhNbQZwgMaoSsb9BX3ZV1aDTjEZz0-U7IEaw5suCTq4kUL4VkEFH89tU4q2dCt_LXbH7SWwLcnpfBqeIBC9sVH1VkT1_lpdDP29lTSDI-S16Xt6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=lXoc24o9ytTgMgG8PkLSWD0gHThzciOA6Cs82rBj51JVM5Ka2ivFcer_lUEn6BSGKgS5Mj3tiUEAJDugg5X6srWJLsl5MFNENT-N0IELNdYK7hR2YtKq8fHrrZLuzflZs5It0lsCrBYH8a3WiqpKTyGp3Dgf8aRk9chmdGJxWcEbTc1lQnZiNtUVn1D_Xdy9Wtc1U9BDMWbQI5InbNhaPsXW8Q5MjV0Sgjg8nv9GLHQGPt2PIUzuZ_qzoTSYpzyU57IpUM0u0rT3ysAvQ8aCwZPHtZes5iRYQw-A108CFGEWTjVvjDa2HutnilX9aHhGMqfP3KhYLDYEF4fcBC7_1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=lXoc24o9ytTgMgG8PkLSWD0gHThzciOA6Cs82rBj51JVM5Ka2ivFcer_lUEn6BSGKgS5Mj3tiUEAJDugg5X6srWJLsl5MFNENT-N0IELNdYK7hR2YtKq8fHrrZLuzflZs5It0lsCrBYH8a3WiqpKTyGp3Dgf8aRk9chmdGJxWcEbTc1lQnZiNtUVn1D_Xdy9Wtc1U9BDMWbQI5InbNhaPsXW8Q5MjV0Sgjg8nv9GLHQGPt2PIUzuZ_qzoTSYpzyU57IpUM0u0rT3ysAvQ8aCwZPHtZes5iRYQw-A108CFGEWTjVvjDa2HutnilX9aHhGMqfP3KhYLDYEF4fcBC7_1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLYYiYy5d7F0lW4d9VM2K6isXybBL6VCnHMue2PgxGqmt0iTwWdllaT9ewJ0wYxWlO4ExTeXDDb_cXubwDwEdbDeVZoO47ygIuhVAdd2EzF5p4Bm53Z5TSIVDoWo3ZEA9wahEPOMuVR93cZpMhpKbmbuwXYKPakaT9RIbZTPn0SY2SS-8J88oBHcQ2kYyrZoPEJhnt-VQWMG4RKCxHNEppBWJmBH3ObKskCfxQh5iVY0AHPGFhXgOk4LBFrjiI5COjqLt-yZ4lfzapjODQg6o7805luSP0SSSWEnyvxr0ZGA-KdNJYnhaiBbUOTsiKRIRWSwxj0O7M_Cm57HetVihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuHLkJCQBlsuasCMDPfkKZZIqtQo0Wh2N_gcwLx0SE9ISY0BoN716NzgiZwwkV5C7CSj2KSDJqZyEuHRMPewBbC-MgUptc2WzVclUZY1TD1btv-B1lBAby9hRNlMRpBv9GMd0HngL8aJMmGManXLR5t2Crw7cfhtA6uM8-AzGn0rajgYgc1SsyjluAnCGyQpd_eg1l1YnnixzBPUzc9q5puXscpw3J5RuDw8fy6TshFvfmPnbRZaza3W1vYW7hDBSlzsuI4v3lu3ozLaufGkIDzdmSWFc76PG_CxsAkR4h0Vt7BpDX9MXjnziPl55Kl1iJ8gSTksmBy33ftEYkA9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=GpmgeXWkS-61xYbIVz1uSqLzgL9oOKgc5M8WzCO_sr19IdFnOnsXN2AfgnNvgXrXRxPtCOPPlp2ml7gMq1eyRzNKhCrcuaIZWo2Dd9w2Wl0GwsWAA5Ys4TwsDj8zLk-b9zt2MyBNzLMzEMdC48jhak3wWj9nrwcnvfAZEwoTrV0xKJ78fRqkkJCVJslY0UPvvcRixzCguTTLd9IxTyX_6swvChRL1BkI03g6LHI2GDg-CjdLVFV3ECPuTOSr2AP6UpKU-mre0wBOPgqEO25EbsWm5nulY8NjLF8EvbB65pKICkhxh1zrmJlONJRZD9erVFnzTedaBjhJ0jPJW_AX6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=GpmgeXWkS-61xYbIVz1uSqLzgL9oOKgc5M8WzCO_sr19IdFnOnsXN2AfgnNvgXrXRxPtCOPPlp2ml7gMq1eyRzNKhCrcuaIZWo2Dd9w2Wl0GwsWAA5Ys4TwsDj8zLk-b9zt2MyBNzLMzEMdC48jhak3wWj9nrwcnvfAZEwoTrV0xKJ78fRqkkJCVJslY0UPvvcRixzCguTTLd9IxTyX_6swvChRL1BkI03g6LHI2GDg-CjdLVFV3ECPuTOSr2AP6UpKU-mre0wBOPgqEO25EbsWm5nulY8NjLF8EvbB65pKICkhxh1zrmJlONJRZD9erVFnzTedaBjhJ0jPJW_AX6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuwOVlDNFykicOm0m7CZ0ETVD6xb08opA54ogYMw2E73GT6Gz68Ka7F-WFlCYwNhf2Gg4JjRNbFrNt5dymQ3tKofg93ie1eejDmtYy7945a9GvgsRm_SpIyHFNd6jUyuGWPC8fd7TDDT5zMYzRVdAJM2uGADfgQEOjD6GlaBOqUELybA41GIzG5CVCRgSpVNjNT5W3UmV5gmhUzSnxZqGsHjFVgte3cgVKEdpq1TRUlL87WIVfC05_Fc-4Mr2-ooD-VdMkVJ12Rv9CVnUrk8lZXVmRhWYnSqkoUOoPkcjcDq_Rs7zdZAazmxodLeg3k8DY0IWp0o0TwZeCcdmg_4zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EL3_YMIjPt65e5OB9e5cW5sYw6gQtXekiCn67hKU-tZQo7tE1m9n9Ooqpb7kidF99cK0sokGQ3HWnJS11Ons9s6sBOiYmrPe2PQ8SaM_ugE2CO0CK85CPvdsR9qL7PF-Oj-xceGGn2m7ZrVZ6ltNmFtrkJGB2DCNeL7Kvi9_X2mv0Ku4ikflBvIn9dtm5GAHYgx7hVBiaPmSd-L-ayZ2D6ankqLHsSv1N9b-Q2LRtBE8WmnIwH9IXB6ZyCu043bdkQ_AkD4Y2RDzjHBKrmYsVmR7LOr8sq-To83t0eh3uqUKuPyHzBhA0NxDPzGzQrKPWDKLV77Vs9tu-CwClHzu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emUy-zVTyR97XsHFsRIkiS4ut1E_HHPJm3rAgF-EPdrSLoaB2GIPXc2vWMjQpX1HZUkxgXObCN_hh5vpTuYvrOb-HkARB521yAMll6j5Wk1b7lkpg4KxxyU55IB7LGNIgPWAm15kgVN4LV3rXKFxrvZ3CLCPX94H0a_2SVSi0ZFSD2pxdXfI5_1NKLtulQWP169JqZ9VA4mmIVa6gHd2Qf4uLBh8q0PPh6c5FgqPoW_GUjhoG_yfK4nRE89mkPHBLuUIAFQMbG6_4q00n7cWYoTbPEinlG4rYvQZjoaEP3yTKn4ySDAXc-XymEcxCI3F1V4T3G7ZmvGOVmWLE9xmEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lo9hR1dAbGGy1sYvJnTOe7h8LjaqKlbZqBymTleCIpCGYKRH4zDu4YAFkMkOFIzLQ8Qey-ZySyv9L9Xe5r94okCXKaXQ-g9Fd_giK6KWWaFeeN2V-nbZ3uwmBm3EnmSChbupv6D9x3xQWwlJDX395X2pn96gqqRMXBi1B8IFUmxAXYTW7aWc7a-vKdOBIMLfE8w9le7tCIeld37DtWCRbkAICKSiCclfQELdvl4R8_Hr1UHmnvJcOCzT1T5LR8RMpyADnCB4kuE80E_s4D2e8t19zpSiHXhlabSZiXaj4RiIEhsct9a47I_EZs6e1SH8CXln0g_5s3aEnonJDzwoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOfwyaAe5TxOms4HYvceRoWabOIG_Davk2iVmE0NSh-jkeIB9ThLe-oFV2leL38aR4-5D5iPtApZoe4-HYihrtbwimytF6f-FQbvKYyij5qExEGMTltNjwjAWQpE__HZf6XZpTtJotoxDwL7UvWR3xwV0JVhAaeYFDe9Kg4DtcJXOQPmhX6MzIl2bI8J9KZl_92KHSJBuApBRzUTlrYlH7IghCEup_fJare79_XNyNkftFJj8UhhEqvlG-8bYf5kYw2-nHjXJDkIfspAEhjXf3MI4DjW3jZsKO1cCDxqWnPM5kX9cwXep4k4iz1Rtwk649ExhqyWakgxMcenjpFSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWQX6Bw1g7JklUkrTlTecnYm8VS0pcKB-Keq6vJAIADMj1t125GIcvYV1-phsCZ5vvbWM5IH3wFYnrjICHQnC_6h34WPpxOTGJ956wJZBIgKwKJ59pJaKngrl50jrxDaF2Khu_kHYZ5yp8Ug0dEjaw5G-QGs_cjkE5pgVTOzAOKgArLxkeRPXnRvfe88UyJb9QQzlUC8Dab1pzmIluoOzcxzUfOALme-QqwEP0r7tu8OqTxzeDTNTsIU7ikIeasJjzSWWINw48jMxrh2qH66rSDVrqJWFQum38_685HM2uJPPPxWZ21rbcFAPYOh1q_Cm5zZjT8oXeKQpBD8oq9yiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkKXdZ2m6_64LvrwQnMn3i79pJBPjpA88DZ4xGJdX3M7YiJQEK9SbLfUp0MGO3hoGzR1C4L3K1yIO4sM8C8t0dZgYWEm1N4UmkDZkB5BGnDgt_Lz_mzkyXmARJ5HW5tjmW3F3M1OJmFW3tQSrWlqNVh4FkaDGXQn8af0dSYp3gQBo58Vtf7GJeszqkxdY-ks2DdZGi9R45RTPZxHRoBjxYF9DIGJoa5TM5kuRO-mDnHzrLZIBIzG8wZC9AYiMxNCp7XeXrO3IsX7DnwwfnLocJgMxJFHqECXVsAlxAWzxSORi2kCEi4kdGq-PlVKdMR0TyHMn9zxXhvgGIrKK7W_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7VUYUrleGIPkLyzIXgIEKHl9EsIynPADWzAQTcTmvvCQkC1XWrno3jC6XkiVogoaHaQGRrYG1K5HcTAii6eJyNSIvmjln00VKlNLoC0QoX15lcAy0xyrOs5T58qvXYJVwKnQyx-nah1Z0Xvxgg27qUixNspF_OKSSIkrorwvjdiB_YjoX9r6q2sQyLS-561XtdzVG_SUu6_W83LxrLiY--YM8Z1o4yZtkmhXqCM8cq6G7Nl2-4XG5kfVx4w5haN7v6ElgwLPReEcWXY4le1bx3b02zWsot09Krw7IW4GUWy0Ki8e6FrnC0VHXKlRblgmCkDoCL78kTvfcKi58QIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKKMSJ_gvWqWtTEL099lTDSME0eLhyBRBQW6YwNZsJlbvhVdFRrrhlsHHtMEcS2UXpUaYwSCR0PZCMhcEYFuJVvUI3NnBy__DArFIbpTIqVLrKb5jK2NIHDkKVZp6bWVe0Bu14BGbtbU7nPx5qTn0QBt-MGYQ6CUW_1OWZeZc3LuVjWanaGyET2Wd8a0JUnUYGqYxOkQcIGDAFPv0YCffDoteQxPFUv4M7X-G5gOKh-nybZAnBXDEyRIT-VRE_O0j7kT8jFycgn76A-mSMS4L7_6K3TibRPeGepbUObijVG2ra7JtIBPQRlAE6GVrQVfcacDVyxhPWPpfjajEE2zmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNZm1Aw_BZu-t2CBTqUwGKBGYJtB7QcuMy5BnkLyrN3qe-CTpLUjyRPXbk_KSsBm2UQAlerCr0W-_rTy6XZLOQEprvykQbbDRWXdVxpk-Wjc01KmxxoRMBon3yg5M7Q_aWO1u6BO6U7AQFI90IGps-1rBtqEVAqwlJeA_3Uya8VwOz8vuGtPvG4nsV1G0a9r8nf5zp1EF6Cg0GVzpyfHztcrRJRZBSVp2l-GTAwm4XFDGVhSmC1qZGxeONQVIhKgoPrLsuYT7LDkRdM_AiWy-grF6znlwQFHOnHU_TsDacjmH4cyJYC8dMP7vk3KYghw04qa8FLGtVpah7O7EBMJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIQYd4bPj3dDCszBI8ITMyLvkUb8ur8cNFhdM7p4WUVWOfkPA89X25GenF85Joog_vrLZPEtrGsdqY2PPq_Qf3DGhIDvI6tzdqLn9HgbTlc_sKLO2ptHMR4UrNvBUA-rsex6wxj9_WIAwVaiwcqi6dVDXvr6w_Hw6QOyhARpDyUjtXpzbsgssmi1c1s8ab5AxoSKZFOdnEBDtcr4DcO0C1Wtxe_cE25dnw3RBEwGC0781d0pQM_DMrPatz7_4sA2xc9IVlBbm5BsHMuM8jDCN4gL3_L988QhH8jnZImhSz6EGJyehoETsiROmiXw1x98slQTm_KXi13TRC1uECjAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
