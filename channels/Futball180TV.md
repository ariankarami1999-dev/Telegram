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
<img src="https://cdn5.telesco.pe/file/Cma3ZbAAk513kQ8tQvaGzZrD5R_o1snNfZmEamQr3sXUGZ2vLuDMoE8xUp7II6gDfjdlvOp5k5nJkKImFx_vOR8OcEsxKYL1Pe4x123V3KKawuueCwfwLBJ3yicHXLqQLpn7Yv5mZvxL4coOTxBnzX1SBzNVMmKujf7Wcoud4Iqwbbo_Dh0p7CaJUnrMhBMrAuL1_4aAKUVvTExF_YEgjhcbN_n_GAj73bM751lMxTifE6mf0lITj9BjM2gjzpQ8aURY3SS-WY46UNRACeM8OqK9Fgoeqr1HgpI1XPBFji3mZnn1EzcPM0qIhMw6MjXpqDR3SCndDVbsFHSWhOZ2Aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 443K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 20:15:04</div>
<hr>

<div class="tg-post" id="msg-92366">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGlCaWcnKomknogDZomMMqcWO5aPI10Sh8KgZmGrlPMNZjblYphDGCAUTl5z1xL12II5z72hDRcoN_PKOeJLzdUoK-daskK1QNcuHT6Eb2oDt1QoEG5kzv_JgyYMW9-dg7tJivn4WO_PRpgXgf9f0yexW9S10TePZQ6Vr_Y-t2uR6frBHGMHh0YDdI4VIQ2t1HpuWCxOKdFocCvD0Sm48XTyPJ4hY2n_fcbp9Qp0lscv65YltBYLXjHiR3xSw-dEbxR7aGUGMoZdbtOqTgFhby2jrm_yUtO-3TFTq16In_QyBOfKnnZgHx8XdMYQBnyunyyHTaiHZz-h6pxzrcd95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
خولیان کوئینونس:
برای من گل زدن توی لیگ عربستان سخت از گل زدن توی جام جهانیه.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 924 · <a href="https://t.me/Futball180TV/92366" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92365">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/Futball180TV/92365" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92364">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_lBWoHkjfV7-3TIoEYGbF75Dcl06LEQxlTqFXZhFtBo6gWoHUwiIzXXKjFwTXyZUotAxK6dz5-Gpsgr7pQsOlCVD72xBUquLPJnIs6EDrs-XDmM5nBrsS2E85tRoEck4uzA1AjPSBWOTDUecD_nLhmk6N0rCx0d7Fn8F2iniNoHtrAzdk855rti2y8uCLmnYh4jThzuGMt40tZbmk7PMWPYljPUd1Dg4WOaNR-goKEcneWxbKbRDP2HgqjC3vNo3QOTqsxGPsScg1Z_wLbZP9mL3BjLwXklinVW5wGPsQYPrrYgXZ_HC4QyvSj-3VgkqbDCecn1sWxyrpiFGUAQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 920 · <a href="https://t.me/Futball180TV/92364" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92363">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhCNc7_LAvOKBl3_QqOhY3nZr_GMvfOGOOEpRJmEzGrXE_RX4nPIwVTqHWHkM_L8-flD1pTiWvpz6TMTjYwSRmiQHbcqByt-93jploubmKeo8OVV4bFvqlH7x7PhN8yL2MzA4cAugP39RckdIsDmbPHAEafH5egG3oHlnGLA6MaF1zmDjXKQklQKZ8GljtFDddRlG3AFqrPZBvL7XhYmTQhaKZs35b32Xp-xiyD_ptJm6tWC5Ac5Ti2l-lGJJ-hOYNrd9fSyh_n3Q0bYQahbNkcu2SOv-C6sK26PIA9zfuN9htTGecUYxUs5vGiVgN-ydNgfwLQlr7QC6qhytOtRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سیرو لوپز (خبرنگار نزدیک به باشگاه رئال مادرید
:
🔹
یوونتوس ادواردو کاماوینگا را در اولویت‌های نقل و انتقالات تابستانی خود قرار داده است.
🔹
اسپالتی شدیدا به کاماوینگا علاقه‌مند است و برای پروژه‌اش حساب ویژه ای روی کاماوینگا باز کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/Futball180TV/92363" target="_blank">📅 20:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92362">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPQjrq4yO4P9WcijHPlwTGYCAzHAQHcej4AAU-F6iK7YBedVtgioIewprS75v-NOZ38coZH8YqafUKzttz2WbhSd27JW1TO3RuLLL1Vy30yswJlt1lzChgLyVcgY67UR5KGjNqZOyldFtq5fxUQgKZAfXH0s5-os_q4QHQ5AjgD2bGHOTdGf37WmCy-lINsT6-P4RYC1dRyD3AJ2NH79LdDFaMI49vYpVKA37NcEuH_Ys2n7R2iflJ3JZNE92oDpqHyzvl3jUtE6Mw7UL9Ak1Hb-REVxWBxv60JBJZLSVwzecL5C1R74HSnC05Rc25UsSirGKsGKcL_lkvjhJ-oubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
عکس رسمی تیم‌ملی کرواسی برای جام‌جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/Futball180TV/92362" target="_blank">📅 20:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92361">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇨🇦
هوادارای کانادا کمتر از 3 ساعت مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/Futball180TV/92361" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92360">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-jdPk0ux-azu7-mDKSqRAlr94e-7eT7qCQ_R2yHpe530ra73cedCLcCUvWcYqJGUVpt-1i8gy3EO7MsYSvtiGZyw9HszUZkuWJgmYMy-WSSSVjbX8UlNuGsuGCNa7KMaql-C76s2ch9IulSBxLpNT6GVWw8b67dqyi-mWHpzYC91i67lEqnilkWI1r9S0gf2IxYD8mU-o9ixSbZL9SooLWuOrLCWNz466YwRpPgBlYq30ZXQpNerOBYF70E2zrnv_xJlzORjsnm0ZsrSX3GFplspOEiq9sTes52hjgEpsjbOF7q4-I1fhcfPLBbtMt9gCUJIq9-aQCjRvf33n_MXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
رودری: اگر ازم بخوان توپ‌طلایی که گرفتم رو‌ تقدیم کنم و در ازاش جام‌جهانی قهرمان بشم، قطعا اینکار انجام میدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/92360" target="_blank">📅 20:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92359">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c3684885.mp4?token=VsPTB_15PMDPHymFvz94S_pQpONB328ZbYHo2egSMmGC6sbco5tqGgENSqatKNeo6BKF_ZElcOp5f9kaIhKTOHSO2GAdC5vfRVnINcRWrfkEVJy0ElhhbXcc3gNizxUzPHpU6cj_K1MT_Zd_H_anQKvfVCSTw6UfQWejrasmBaIceygt95c46YS-RHnfAi2HRki3uyi143KSqhkWt43JH78uZUw2PmhWbUGas2XrpzKXy4JlafvpndjVa-xo7Fs83GAfc6_UlBm2lrHw7q-Ozb040Lv7MTIYQrYgy6LoIu1TUY-j5_bkXB-olCqvvU9Wzb8qnGC0mNOOylQdgK4R5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c3684885.mp4?token=VsPTB_15PMDPHymFvz94S_pQpONB328ZbYHo2egSMmGC6sbco5tqGgENSqatKNeo6BKF_ZElcOp5f9kaIhKTOHSO2GAdC5vfRVnINcRWrfkEVJy0ElhhbXcc3gNizxUzPHpU6cj_K1MT_Zd_H_anQKvfVCSTw6UfQWejrasmBaIceygt95c46YS-RHnfAi2HRki3uyi143KSqhkWt43JH78uZUw2PmhWbUGas2XrpzKXy4JlafvpndjVa-xo7Fs83GAfc6_UlBm2lrHw7q-Ozb040Lv7MTIYQrYgy6LoIu1TUY-j5_bkXB-olCqvvU9Wzb8qnGC0mNOOylQdgK4R5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
پلیس در حال بازرسی بدنی هواداران حاضر در جام جهانی:
آخرش فقط
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/Futball180TV/92359" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92358">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ لیست اولیه بازیکنان مدنظر اعضای‌کمیته‌فنی تیم استقلال که به علی تاجرنیا سپرده‌شده‌که بلافاصله بعد از باز شدن پنجره‌آبی‌ها درهفته آینده برای‌جذبشون اقدام کنند.
🔵
پست گلر: محمد خلیفه یا علیرضا بیرانوند.
🔵
پست دفاع وسط: مجید حسینی یا…</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/Futball180TV/92358" target="_blank">📅 19:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92357">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf073331.mp4?token=vcBWUB176BFZ-B0Y5kW9-3x9mhZ5H31KPZ1TlzyT889dKFH8MiVCaQPIlxiBnnx9uPN8KLkYh-RVIjq3lKcC5Pk7hx3xhqJmhEsRGcUUPU7Z5bDdHZ8bbJPnaes4d4NQvvdaezLrwYJs6Gwmq6H0vB0jX7mucwluAiN7uedLy0h3fprrMwPlOxKP9cfnm-2EZLfNJEuqVAyMfbLFkM5MvNeUMeCl1fXqaPUrMfHfXl3sTsujsnvCnc5380DErlNecZ3WYM1lTus8ygECeyw1AgNBL66qqouqcM_x0qKMiHnT949N_EhvwhhKYv_ltaoZo3DVU4GMkSoO-wm6K7g02Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf073331.mp4?token=vcBWUB176BFZ-B0Y5kW9-3x9mhZ5H31KPZ1TlzyT889dKFH8MiVCaQPIlxiBnnx9uPN8KLkYh-RVIjq3lKcC5Pk7hx3xhqJmhEsRGcUUPU7Z5bDdHZ8bbJPnaes4d4NQvvdaezLrwYJs6Gwmq6H0vB0jX7mucwluAiN7uedLy0h3fprrMwPlOxKP9cfnm-2EZLfNJEuqVAyMfbLFkM5MvNeUMeCl1fXqaPUrMfHfXl3sTsujsnvCnc5380DErlNecZ3WYM1lTus8ygECeyw1AgNBL66qqouqcM_x0qKMiHnT949N_EhvwhhKYv_ltaoZo3DVU4GMkSoO-wm6K7g02Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
احساساتی‌شدن عوامل‌برگزاری افتتاحیه جام‌جهانی حین برگزاری مراسم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/92357" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92356">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
😐
رسانه‌های خارجی از تصویر قلعه‌نویی که منتشر شده شاکی هستن. این رسانه‌ها نوشتن که سرمربی تیم‌ملی جمهوری اسلامی برای نشون دادن دارایی‌های گرون قیمت خودش که همون ساعت رولکس رو دستش هست، تصویر رسمی جام‌جهانی رو خراب و زشت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/Futball180TV/92356" target="_blank">📅 19:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92354">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwagenvWi0h-iAHOdQygs5egoalmkc1DoDVrWk5xiXAjYVRFwp2uIZEQ9thgYVRYJjRhsBb5ItwgYnO6zHweRz4Tt1PETsHe5So8FFBz_NziQ59AAGV7OTzyABnz6PWpWAzyhzEgkdJJQZABkzKuT1wLE7v41SlFC5q05ZZcZvDzX8-hcffkr8VihQTfgbFTOP8ldo4rQY6GsGaMzvP43MQI8t5lXGSdjTBZweXk9X-4jIr-dQMZKcDwqy7K_kiUUYZAItxv_lc0Pdcg-BCmsAf4dMeAcjRxHD9xfVPCmj-dsHchxaaVjNBsFAg-cxtd7ovzS2STc4jt47wJq_y8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فووووووری
🔴
🏆
هکرهای مرتبط با جمهوری اسلامی، مسابقات جام جهانی ۲۰۲۶ را تهدید کردند.
🔴
🇺🇸
گروه حنظله ادعا کرد که پهپادهای متعلق به دفتر تحقیقات فدرال آمریکا (FBI) را هک کرده و تهدید به هدف قرار دادن رویدادهای جام جهانی ۲۰۲۶ کرده است.
🔴
❗️
این گروه تصاویری و ویدئوهایی منتشر کرد که ادعا می‌کرد از پهپادهای هک شده است، اما نهادهای تخصصی در صحت این ادعاها تردید کردند.
❌
🇺🇸
در مقابل، مقامات آمریکایی پرواز پهپادها را بر فراز استادیوم‌های جام جهانی و مناطق اطراف آن ممنوع کردند و همچنین جایزه‌ای تا ۱۰ میلیون دلار برای اطلاعاتی که به شناسایی اعضای این گروه کمک کند، تعیین کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/92354" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92353">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری: باشگاه بارسلونا قصد داره به اتهام افترا از فلورنتینو پرز شکایت کنه
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/92353" target="_blank">📅 19:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92351">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxaQN5J-wFNqtB08Tt99mmVEFrIoaffZJSVHQEmAPHXs0NdBj9MntEuwYXGzn68j9gPXLUmWPS5LOx4it85CjLYjKDPg7_rM9MjBRC7OIiGSQ0oGey9MutvTjZemUcGRnk6D8Z_7u5n6j6FltQgi7AHP8-O7IpBhyhfFdFdb96RV6K_LpVF-6002WtHTmlHWP16CHKHjXSFA7BC2lvpmiC00Yof5uLnD-vwLqoZVHngtX4OMjz5ogRDsg9yGWgen7MxA6WqzNMvkr_CvcojVGDrXUkmPt2zhAlZ-cXtEe3k5H1ZVcIULs-nOI0TdsDzAE9RFSzN06BVOsodeYrd1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#
فوووووری
: باشگاه بارسلونا قصد داره به اتهام افترا از فلورنتینو پرز شکایت کنه
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/92351" target="_blank">📅 19:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92350">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY0g4p_E4wIRZolI7UlgLVIGMBxhirAR1Efb_TStUqjBYdB_IPiYJAgSNKZxHvjo_g5Qvz4XXT36EK7EBQy-e5f9Z7qqsUL4F6is_iq67Ya4FEY0uB4sCDExHUohub7P_dpCQ2oAcPNdB0HyiB04GFllemL3LSozEVfKWE1YXnjteeg_xllOFz6SoXmS1RP4sZkBhrvOP5nbEQOOO3qO-MAUNjlADwvvvOeXHL2Md5BHm5avAKR8udSon5tbGY1PKu0Oxu9iQbTEST-kGh8bcX55Dr6gX7DLDTXmLyvTWu2SVxDMZ_4X0bCSup_zW064ptQ0n2E-Fn3--ksDJS0NNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موندو دیپورتیوو |
لامین یامال دوست دارد در دیدار اسپانیا مقابل کیپ‌ورد از ابتدا در ترکیب اصلی باشد و این موضوع را به کادرفنی هم منتقل کرد، اما لوئیس دلا فوئنته با این درخواست مخالفت کرد و از او خواست آرامش خود را حفظ کند و به تصمیمات کادرفنی احترام بگذارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92350" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92348">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veOveq49CaqGYwLmFi2YQSlYlGTSbH5FP0bWFrZHO5VerKbILuHhNSHqxF0iA01y77Ix9MCi4Eq1wQcjfEuEFuRHgLSEpr_B5ghe_uBqkp3Ei4Bu1LZJEuj4-dHW4fPW1hCPg6GmyjsiGbjAZSPLNT0kgXQkhuMhj61FRYjKYbsmeeXeoBeTjkhwEGIrXUV5S-iR16q_buQ4JFAavkgZBaSQetFr8m6lIekQ64F1MNVzOkmSp5I_ufg8YYMf4flkiLRh7GnyfMTt58py_RS02EjNqsPDjKL7cQavXMf78cATaVZPQolCZ5coyhMxda7My-oPfeFGJJGErQZe4N7_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hl5V0yC01JwlQWygZXpU7SbzSenGABu01fpY8-GuCq4SFebH_sIDDRK2Xf-KpmLXgyv9cD50ql0JetiG7xHjC3oI0cGvDSxV3Iy0QtTpCbmQ0JeYjnTqvkooGWWplFFIAzp9I5hXGSDN9wzJ7kUCUybWDKIM2cmZn2iZUF3nvUaR4L3UcTXtqpIsPcNmkC73KDWIBr9EZ3D5qXkBG5YIafWdWQYx2vGNoWcBCZI2vCX5d6p1cOQ8Kr5kkq1syxoUr54ttPnVjuyYSvnbvENkrEyeM3AMBoFi3E3PPUI7MRmyqw5mHbxT8Ad5YtSQ_2LK2u8-5x-MI-iRyR5PtbTN-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏باز خداروشکر Puma کاندوم نمیسازه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/92348" target="_blank">📅 19:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92347">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtQcwyj6loASsWj9JMKqxYjWL3rqM8EYUqvt_L_Kmo9WlKnH9C87YAINWsYQUm02KI9Fg20veugRvG7yTp9epvQCIG2Dw5X6BRQkQK8e5WxAbMN1poCHKQwYXinfU49JhxSv79VXruuzlBoaSgE7xPHlY28EOBh6FyGZaHx7shDVxQ4rI6V1wuX3ZUungSMI-PacP4LowzSwkbGYltEdjs7RhBbX9dgrdADscVacdCQdx_jyIlrN_yqExflm0blgrFe3NtnQ5qRVac1Sb0eoGgxI8McQkDJxSvGtdk0I1WP7UE9nvPMreyxigdWcl-7VbtCG44AAR0ObhbUvPuEvCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فورییییی از عراقچی: توافق اسلام‌آباد تا حالا هیچ‌وقت این‌قدر به نهایی شدن نزدیک نشده بود!
در ادامه ترامپ هم توییت عراقچی رو‌ بازنشر داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/92347" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92345">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZW2Ifq3qFoTUs7uhoOo3vZho4CQtDGZowcNF2UKrjrF61GKOWki3b8beFQDrE0iXHodZNgizzXn4iFMATU09coYG-ge2y0aTrgO4_Rvk9495nyQD4nGKyGrqX0Z6wohLlKeUSDrYy7hF19HYq9B_UK6mAYqExK34rXEd9wA9eHs6kTtybnauC1LtHJOAWLOax3fFlyp5LORzkEQRV0HfiIs-BVpJ7ZYmqkzCo9OpRbat2wFHbCXWOk4ArZRxXeLgwYfdl7T5PWO_uGNqP6lA02EzrOdBLHSTVDIBgSnV9wK6Y6-jY6qA5aZJvLQ7b_toWgCDm7FZbmRnwgF_BgXwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuegYvIYJIf8GV4WDGlif3gkAjGarTsdQrDOsD1Pb50zU0UVw1qAELOAtLTAty45ADe3AIQzI-XtYjiosugt1_VpFddSxgQhLo2XKVKVQ1lEM_6xC5a2svjwS9fRC01J43Jepti-T_6KWE1g2m0ZAOojngO2YtKL1-YPLF-o_4JIWC5LQQ6RCLD-tPcV_XOzCTB56GwmZ9L0Uo0GS6qJz3ALZbl54PgmKDNsL2IvXOozoO7joqVmj9ZyybCNB0VAzoM8OCD-YyQjiGUqjBzyLxFwdzkBYc7qeKZK-VqHvyl54eMukGIso2va51N4ab8vlObHEg9HXK_rzBfV8iEwkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🔥
بازی فردای آمریکا تو ورزشگاه سوفای مقابل پاراگوئه‌ست. بیشترین هزینه برای ساخت یه استادیوم تو جهان برای این ورزشگاه انجام شده، با مبلغ تقریبی 5/5 میلیارد پوند. استادیوم سوفای متعلق به استن کرونکه، مالک آرسنال قهرمان لیگ برتر انگلیسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/92345" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92344">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🙂
🇲🇽
🇿🇦
داور بازی دیشب افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/92344" target="_blank">📅 19:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92343">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0u1KmQrirsZS7Ou_hsFZlBUQT_zaTKWj_Ut8H7MxTaKMZp5Hz7BR4T3aYZtmUuY5JYe9-1PRjzAdq-GXXZ52gAkPf1dQNtpNriTAF1M-VYa4m4X-c_W0zTH1tvck8Y18gTzjAPN4GdXhzi6gvMmNmuloMBjXFYEStHeu5XyLbl2L28rH38fHLEWBJ3GtrOGlPoxHX_v215qAAFefz1DorhtrPa1x7B24I0iwnUepBy-FWJdJwE5jZ_e2qGMQbKFonQ9j5JGrJLTZp9r1yiQ9Nc_zlvfC_JC53GNCXphA_tOUg-gDl5jdt5DfeMIBSMV45C1r9jIiYt0j8FuXq9q4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاکا:
🔴
اگر بدترین قراردادهای رئال مادرید را جستجو کنید، من ابتدا در کنار هازارد ظاهر می‌شوم.
🔴
تجربه من در رئال مادرید کاملاً کامل بود. من از میلان آمدم و در اوج آمادگی بودم، و اگر اکنون به بدترین قراردادهای رئال مادرید نگاه کنیم، من در صدر هستم در کنار هازارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92343" target="_blank">📅 18:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92342">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460611eb6b.mp4?token=FLGJIx5erGcBZ8dpd0Qpoo9p0gBXwD2MtredUrGD-OqAVSyTY1YR9Uk01Ks4CVTpfL3y4uIj7w8zSyhSvszcqCjGfBIo8O2AETHCThRmpnmtkLOykkoxhyfUGA0dxYcrZ0P4xiAt37Jx71axvpITDfkvI5bxZv0jyuBfhpan6im1bTmC1GyYQ5V2J9Felr2L2dwCO0s2oCG_tklIvQr43ojiIEgoMvo52JigLHwyAsxah_VQ70KAUIzYqoa4Fo-QKJ9MwcuNomXdl71DusbQCo7gKXcABjXJ5e6_Qnul6FiIN0-JlJNlESHN493AEY4vKFoVw_IiQbU1HFrQGcX5fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460611eb6b.mp4?token=FLGJIx5erGcBZ8dpd0Qpoo9p0gBXwD2MtredUrGD-OqAVSyTY1YR9Uk01Ks4CVTpfL3y4uIj7w8zSyhSvszcqCjGfBIo8O2AETHCThRmpnmtkLOykkoxhyfUGA0dxYcrZ0P4xiAt37Jx71axvpITDfkvI5bxZv0jyuBfhpan6im1bTmC1GyYQ5V2J9Felr2L2dwCO0s2oCG_tklIvQr43ojiIEgoMvo52JigLHwyAsxah_VQ70KAUIzYqoa4Fo-QKJ9MwcuNomXdl71DusbQCo7gKXcABjXJ5e6_Qnul6FiIN0-JlJNlESHN493AEY4vKFoVw_IiQbU1HFrQGcX5fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
فوری/ "
یک کیلو طلا
"، جایزه باورنکردنی برنامه جدید ابوطالب.
استودیو "
پامپ
"، این بار ترمز بریده و با ابوطالب برنامه جیمی جام رو ساخته.
🚀
🚀
🚀
جالب اینجاست همه میتونن، با روزی چند تا کیلک ساده، بدون قرعه کشی از این یک کیلو طلا سهم ببرن.
🔸
بزن رو لینک که زمان خیلی مهمه تا بقیه سهمو نبردن. ...
👇
👇
👇
👇
-
لینک شرکت در مسابقه ۱ کیلو طلا
-
حتما بدون فیلترشکن وارد شوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/92342" target="_blank">📅 18:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92341">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c13f2711.mp4?token=ir0NPEftxSuN94o9njQMle8XjoIhIpRkLcyrBIFhOU7Iu2Hylxsv0-JPVevpIlk8_BQGAUlWddigsu6vPv3olRn7iqmTHVgTZQ9Hmlgq7vKD74BeKpjHCEF2rtNYoweiqHNoSzgAck0wTd-90yLBu71C5JR7l5oVXMAo1xq1B3EI5JJiD0vbZg-p6TvBB9RRDXhhk8YYcsM8vDb6-V__lwD95N6V99oQupJGSiaHx_1BqNRmNHNdHQZm9qMJP2ktqvUfjNyrtUx7TMDRaK0x6c6ngpPFAgp5rPJ81uTEfjOnMFaIijXLXZxUTjcpE5f4xK-UO2mWL90YNM_5FywgmhtP-OGecTUIVoixWv2rKuThM4eBBBsC4uHGbChkPcDKEAR9izA3T9eS1pY4Mfs8Fjwn6ZjTS6ZyWhSEfP7SLKPeqhuH2aPz-H1B6UwCnvmLrBKtDrFByA5NnazvleEpbzPt72DZmqlp1j1vSZONkTtFzw6YAYzp2NysQtybrpDwnaiDvgeocMW1bdwZUWT-e6ndr4dgT2QRfhhiM3iRjrnqj0AAk9ItcbLh_FqyRMvqXqgLkkGos1w3FsUGB-4IsNRN8DRXg5JwmAJwhbP3ENbsm6rHbhJVdN6Vh_uXdmuR8V7NbPYT_POxZcq7RieNvlGJGqs-S7fxnLmGqGNprA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c13f2711.mp4?token=ir0NPEftxSuN94o9njQMle8XjoIhIpRkLcyrBIFhOU7Iu2Hylxsv0-JPVevpIlk8_BQGAUlWddigsu6vPv3olRn7iqmTHVgTZQ9Hmlgq7vKD74BeKpjHCEF2rtNYoweiqHNoSzgAck0wTd-90yLBu71C5JR7l5oVXMAo1xq1B3EI5JJiD0vbZg-p6TvBB9RRDXhhk8YYcsM8vDb6-V__lwD95N6V99oQupJGSiaHx_1BqNRmNHNdHQZm9qMJP2ktqvUfjNyrtUx7TMDRaK0x6c6ngpPFAgp5rPJ81uTEfjOnMFaIijXLXZxUTjcpE5f4xK-UO2mWL90YNM_5FywgmhtP-OGecTUIVoixWv2rKuThM4eBBBsC4uHGbChkPcDKEAR9izA3T9eS1pY4Mfs8Fjwn6ZjTS6ZyWhSEfP7SLKPeqhuH2aPz-H1B6UwCnvmLrBKtDrFByA5NnazvleEpbzPt72DZmqlp1j1vSZONkTtFzw6YAYzp2NysQtybrpDwnaiDvgeocMW1bdwZUWT-e6ndr4dgT2QRfhhiM3iRjrnqj0AAk9ItcbLh_FqyRMvqXqgLkkGos1w3FsUGB-4IsNRN8DRXg5JwmAJwhbP3ENbsm6rHbhJVdN6Vh_uXdmuR8V7NbPYT_POxZcq7RieNvlGJGqs-S7fxnLmGqGNprA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
برخی از گل‌های لحظه‌پایانی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/92341" target="_blank">📅 18:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92340">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4Xh9mWwK1yRQVi3uic_k3fOOeADYPzboOIlATBSSzm81uf1VtCPwhdKNkfRbHtOrt1AMkgcIwyXuNeefIu6AHQRiVPj9UkwaPgWmGEaJtjOCVEg1ks-s8mR09Z4N6vltHBmmMEM85idC2iqpUEOdKwIBo-K_EsMHQ4KlooISgiXM5aGbz2o8uSE5nb-rUK1FaYgMIk7H0UCofIarssqL22S77VEpWwavDkKThXXCXWb0KOqDG5Ca0OvWe-Um1lylqI2ErUVWYfqvCdtaXGF2mKWdiAPrDe5_2A2Q_V0-q1M5GLU0lNm0U3xviZ5FBku0Ufqz8cTZLbCKMbFChgMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پلیس پروئی دیشب طی یه عملیات غافلگیر کننده با لباس عروسکای جام جهانی یک قاچاقچی مواد مخدر رو حین افتتاحیه جام جهانی دستگیر کردن.
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/92340" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92339">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX6ihPbRMSdYeSPda0w47GCgrLS0IXEvmY0wA_wgivAVO-EkrFr_xYQannc-tIGDFfPjDrCr1Qwl_EaPm0GM0STZ_d3VlxaR2O3LzKVLOMbfxXYAq8iiU8w10JIOyzl1aanxpjcSjrtfrE8NFzvqhlRJeiUa1-Tu7dqb75gGZQIYEP0vHATjk6utKvY9rSbOO0qUIcNeCPcKg5PI4OPoG_is1cN1efF4U4WFfJ-3VDL9crYuLYAzF24Upk09Nxd9e5kQFl5-4yzIUywhE3E8qsDTUkOgwMRmpXgyO6B-P1s7XBS-DJTrIGcFf6j0GrSjtv8oOS4XGB_85oIqPH3a2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
رسانه‌های خارجی از تصویر قلعه‌نویی که منتشر شده شاکی هستن. این رسانه‌ها نوشتن که سرمربی تیم‌ملی جمهوری اسلامی برای نشون دادن دارایی‌های گرون قیمت خودش که همون ساعت رولکس رو دستش هست، تصویر رسمی جام‌جهانی رو خراب و زشت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/92339" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92338">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPK_0oUSeDQJq0o_S9Ily50JURGgqKRTtNFsuqZxe7UAs7_L2LZU6lkZz8gTthVE8_oPka8-omETksMlgwk5HqfacxI3bmMBHcZZFbNdi7FFRPOxxfGW-07auO5NXWmFvaQSuDFHTGlhpD3XI1Bo9ciD2QdZiVdJIyxgyMZTEmwRb1L3BDnxBUauN4F2m4sLIsdoVQSNrNdDIgnGE_U1HQuLUfBDUIYKD7lYSt8gilPzBNVBqG6tx0G-Zosm9nsj3kiaMMLNcVzCo4ErBo71PRQJbl6UPbMsAxZuPAb6C_O0oDh8SvrCy_VWAdY6ZTYQEIrC5Qv-0HXLCJk2eLf4NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🏆
تو کل مسابقات جام‌جهانی گذشته، ۴ کارت قرمز رد و بدل شد اما در بازی افتتاحیه امسال با سه کارت قرمز داده شده ظاهرا قراره مسابقات‌ خشنی رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92338" target="_blank">📅 18:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92337">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGy8rjZSIynDsbLrAzmwrCUJMwJCiD7llifki968qhaKESOOgnxGnPObfRQwSeTJtEg9tK-xpLW_IBBo9Ob-InwIFPm__2Ma0PPv4fafAy9mqW0bREm809jlkqaM0yGtXpiG4VUwlbyP5cYd4oGXpQPthjRxcBGKwOnqMYG5rbd8w-1uNgbWCMKseu4dfQ5r9G2CeeY0rmbRkkO3RKIF18eYQylBE1YEDGDY4D5gYJJKKODcWnA7lHRPlg5WwRS5ZcyGV1PHJfQGNJ50fVi-SpUMn70AGlZJ-fMOS5xjJ7vSE7luBQaXp2FD8ecVQuvvbPMRyFm5tO_sSAjyITYqSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
🏅
🏅
درآمد تیم های ایرانی از جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92337" target="_blank">📅 18:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92336">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8vfuVkNLAOqFPzCpIblFC_fp_WJ5g9NjV-oda5OcpEtZm9Hb04At9QmLhckvgyaenvJX-lgk0tJjOZfzfdnZI0AY4W9-uRUH3pDtOc8n8DA2D3kJXYMRxeWRrZ6i7g3YOihwLmviKiXM2g8ewZJOxhU1K_uZc--mWgFUDWukmYcMcVH5xcb8iBemol62jVIy-LBx5Sfy1Em9W6q2SZQ1nF3BIAhN8Hpn0eQazThJZZwVhEIdb_AiEYF0_NMLStZptMg6kYU1ng91STdE74xcqLXwnbWQoT1hDsv8XAXirjANGJaqEoV6XdSTBXBTW6bglgyZS3op94K-1GZ5kTz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
سوفیان آمرابات:
رویای ما قهرمانی در جام جهانیه، اگه با تمام وجودت بازی کنی و همه چیزت رو در میدان بذاری، همه چیز ممکن میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92336" target="_blank">📅 18:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92335">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0993fc7eca.mp4?token=HHdBvRmtRMb38xsqvFUdC_2ilF-OVrt3WbqyfUSHds7jRLjdMCAKNNMGiIjeC86cT6OqBt7zMM-lYZyE9q6M8eon571pQxhFsIVB-owuFUPUkkwe5yl5F6PARSIiRtsJAawSBwB0vIG6dNaZDLCwpQ-oulJKYGF4akRq5BMaRARrbwdZ0fswVUgmFVonk3AuKmmJkWhQKXU8nKlkPakgRPMtlWN-5Tz2cagGcTtkG7VBc3Ir8793hmYoewm3P6cE2YeWgRTP0pT5cFw567Fi99jClU_Ay5fF0zqsGUN-z2hdaMq8rFQzlm9k60Pk2f_6fnDxQmCiSDILSSWx_QqG_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0993fc7eca.mp4?token=HHdBvRmtRMb38xsqvFUdC_2ilF-OVrt3WbqyfUSHds7jRLjdMCAKNNMGiIjeC86cT6OqBt7zMM-lYZyE9q6M8eon571pQxhFsIVB-owuFUPUkkwe5yl5F6PARSIiRtsJAawSBwB0vIG6dNaZDLCwpQ-oulJKYGF4akRq5BMaRARrbwdZ0fswVUgmFVonk3AuKmmJkWhQKXU8nKlkPakgRPMtlWN-5Tz2cagGcTtkG7VBc3Ir8793hmYoewm3P6cE2YeWgRTP0pT5cFw567Fi99jClU_Ay5fF0zqsGUN-z2hdaMq8rFQzlm9k60Pk2f_6fnDxQmCiSDILSSWx_QqG_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهرا سامی، مجری شبکه عراقی برنامه جام جهانی هستن
🥰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/92335" target="_blank">📅 18:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92334">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051f0d1e00.mp4?token=XVv6nLmB8i4WeV73P4aK6KWZ1f9mlGwMJx9hKlWlhqnvSF9lFkx0fUKtNFYiDjVOk7kd4N7EVmmjfATj27HknPN9KLBVVsBsvXhcXp3ecZOgCJPtyvb9oIK8sncAOKWLi6L6za944w5jfnM_BgKM64w_o1Xlugfkn97jlYiC0HWOas7AYmadOvWsZ9lVt83oIJwCVWfelwwv6N5x-L0L_iUJD-56Mp7GyQhcaW3uKZsWm6CYDabiVBixGqIwLgs59k17eMPia4foV-Vov5A3Q_v5tffXoS_9lmcs17HnTlSvIuH5o7lWD2OithCCWeskzHqcDV4QX7tF5NKjmVevZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051f0d1e00.mp4?token=XVv6nLmB8i4WeV73P4aK6KWZ1f9mlGwMJx9hKlWlhqnvSF9lFkx0fUKtNFYiDjVOk7kd4N7EVmmjfATj27HknPN9KLBVVsBsvXhcXp3ecZOgCJPtyvb9oIK8sncAOKWLi6L6za944w5jfnM_BgKM64w_o1Xlugfkn97jlYiC0HWOas7AYmadOvWsZ9lVt83oIJwCVWfelwwv6N5x-L0L_iUJD-56Mp7GyQhcaW3uKZsWm6CYDabiVBixGqIwLgs59k17eMPia4foV-Vov5A3Q_v5tffXoS_9lmcs17HnTlSvIuH5o7lWD2OithCCWeskzHqcDV4QX7tF5NKjmVevZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکالمه اسپانیایی جواد نکونام با پائولو دیبالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/92334" target="_blank">📅 17:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92333">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718ad0590.mp4?token=OQvC2t2LwM9T5zMHuY46ZWVNse7L_363AJe38QfSRziTjSMKo_py9eLzEKFoZNMlfTpCTy6txncZw4M5JAza6Jk7CNV3PRiDM65wkjmjWp4C05lwqRCZpQoDdHzAiLMca4PEQeyjlXCa_CnEBtUE_N9OOilW5c_DDVI6zqYdqMdwZCigeeSma6sqz6qJFqnjHyXRcVhhnE_JveiwuTtTeRA8gtQqNicceqLIPM4b5L8nGKBIgVVHuXUTG4UDtPW41jKFBv1uKnit6QzQ7iYScsqaMcOVpkiTCQaj_2NJh0u0T4dIWmA3CzoD8hmerM6jrEFYoW04sV-co4pz_OUUxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718ad0590.mp4?token=OQvC2t2LwM9T5zMHuY46ZWVNse7L_363AJe38QfSRziTjSMKo_py9eLzEKFoZNMlfTpCTy6txncZw4M5JAza6Jk7CNV3PRiDM65wkjmjWp4C05lwqRCZpQoDdHzAiLMca4PEQeyjlXCa_CnEBtUE_N9OOilW5c_DDVI6zqYdqMdwZCigeeSma6sqz6qJFqnjHyXRcVhhnE_JveiwuTtTeRA8gtQqNicceqLIPM4b5L8nGKBIgVVHuXUTG4UDtPW41jKFBv1uKnit6QzQ7iYScsqaMcOVpkiTCQaj_2NJh0u0T4dIWmA3CzoD8hmerM6jrEFYoW04sV-co4pz_OUUxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
عیش‌و‌نوش کره‌ای ها و مکزیکی‌ها در‌ روز گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/92333" target="_blank">📅 17:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92332">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f2cc8b70f.mp4?token=tytsjvX1s9rtxddWfsrdKEIebZyKYyo5PUKSRNHSv2QAe_2T5aOLhKRNKYaMyej0JL0XTBbxQl01sj4eA4v2B0XqN6Isc9hixsTGVOuioWF1UMoPn8y4L3_MKWgYOrISUlf3UwtRWfJseFM4SFtyl_L5djWbq_4kY1izkVwI2BxoL-SFWtJ_ptiIIt33I-6djWvMiYJ_-GQxoQAtCBUHlTvI0BHXAupPqf9xPabW5Ijrq4ZtA9N6s3h-FE3LpTo34ZK3NbovH63xPJ4lm3X3kPPTKuHYREl3uyvYZ8oaMtOmwRTsoS9lupD9U6cbFtYNLG9u7B0RhzVNDcMaUdQRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f2cc8b70f.mp4?token=tytsjvX1s9rtxddWfsrdKEIebZyKYyo5PUKSRNHSv2QAe_2T5aOLhKRNKYaMyej0JL0XTBbxQl01sj4eA4v2B0XqN6Isc9hixsTGVOuioWF1UMoPn8y4L3_MKWgYOrISUlf3UwtRWfJseFM4SFtyl_L5djWbq_4kY1izkVwI2BxoL-SFWtJ_ptiIIt33I-6djWvMiYJ_-GQxoQAtCBUHlTvI0BHXAupPqf9xPabW5Ijrq4ZtA9N6s3h-FE3LpTo34ZK3NbovH63xPJ4lm3X3kPPTKuHYREl3uyvYZ8oaMtOmwRTsoS9lupD9U6cbFtYNLG9u7B0RhzVNDcMaUdQRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری نیکو ویلیامز از خروپف یامال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/92332" target="_blank">📅 17:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92331">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=KlTMlJO123ru_1xpzsvoG6gwN39qu9KkfJlyxifWZuHVntKgb1dtOJoj2cFmcZAW60UZTxkhBSN8TFdqoxtzdAa2LTWd1EUyYWQdp2RMmhM1R_6qtghTGWwYEYD3m8x7KdNuhRIXuWcdmEIDFejCJfuazSU1h1tGxv-8IAUSOEnh6kPUBo_g2u6IxDqrRPRKzk0FZPdRuSjEIPWnKYUx2MGaU4nz5WHJUG4v74ceV6Uww9IPX83FI7O_DfZ2n23qe1Qps04XMsFMSCIMz3SBTsGqWDKGcsXiNZPeqGfxvHkjDXuSaZ1i3ny_cHQzg6zA0HjElHSkjmU3HcQQ0lj8uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=KlTMlJO123ru_1xpzsvoG6gwN39qu9KkfJlyxifWZuHVntKgb1dtOJoj2cFmcZAW60UZTxkhBSN8TFdqoxtzdAa2LTWd1EUyYWQdp2RMmhM1R_6qtghTGWwYEYD3m8x7KdNuhRIXuWcdmEIDFejCJfuazSU1h1tGxv-8IAUSOEnh6kPUBo_g2u6IxDqrRPRKzk0FZPdRuSjEIPWnKYUx2MGaU4nz5WHJUG4v74ceV6Uww9IPX83FI7O_DfZ2n23qe1Qps04XMsFMSCIMz3SBTsGqWDKGcsXiNZPeqGfxvHkjDXuSaZ1i3ny_cHQzg6zA0HjElHSkjmU3HcQQ0lj8uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
🟡
اون چیزایی که ج.ا برای رسانه‌های فیک‌نیوز درز داده، هیچ ربطی به مفادی که به‌صورت مکتوب روی اون توافق شده نداره. حرف‌هایی که زدن، از جمله اون بیانیه ضعیف و رقت‌انگیزشون درباره توافق، هیچ ارتباطی با واقعیت نداره.
🟡
واقعاً آدم‌های بی‌شرفی برای مذاکره…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/92331" target="_blank">📅 17:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92330">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
فووووری از رویترز: توافق بین ایران و آمریکا توسط جی‌دی ونس و قالیباف امضا می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/92330" target="_blank">📅 17:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92329">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e50671e6.mp4?token=g3Zdp3gyZNeH-G7dMtCnMjX2F6JnlyIj03XnUTyQv3GqOM5fkxz094yMS-G-ofJQSEPpD7e_oW8SbFI_1vs7atXqFOIToXhQgTIuqeDMB-ouAy2N-15dsaVP7fH9E6MxmU87UKAT3-JJQyTUHtkWO46169lhV4T74E9k-pxD5mYYRaF_iKYnT7VzvRc3sgm5hs8eS3RRPBkLcl1hpiQBxKL6gQ2aMQrBu45DJKGauppKFdV7s60DcVLdBBZhKFZ20pCqcv7b14Fx8hWC-vtVT8I5Mcw6GsnlgvTzBexNAS0IglwxSSyRmqhwPzxMHu_AlSk-3ANGBM-lVqi-wc04Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e50671e6.mp4?token=g3Zdp3gyZNeH-G7dMtCnMjX2F6JnlyIj03XnUTyQv3GqOM5fkxz094yMS-G-ofJQSEPpD7e_oW8SbFI_1vs7atXqFOIToXhQgTIuqeDMB-ouAy2N-15dsaVP7fH9E6MxmU87UKAT3-JJQyTUHtkWO46169lhV4T74E9k-pxD5mYYRaF_iKYnT7VzvRc3sgm5hs8eS3RRPBkLcl1hpiQBxKL6gQ2aMQrBu45DJKGauppKFdV7s60DcVLdBBZhKFZ20pCqcv7b14Fx8hWC-vtVT8I5Mcw6GsnlgvTzBexNAS0IglwxSSyRmqhwPzxMHu_AlSk-3ANGBM-lVqi-wc04Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
ورزش‌در خانه پارت‌ششم؛ برای دوستان گشادتون که‌ورزش نمیکنن حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92329" target="_blank">📅 17:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92328">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e115a319.mp4?token=j03Lq-z9CZmHeKQyRZPw8eA8tEhInlH6GomjP8KrQ-s5Hen80y9ZEQPdWOPL-1qhBT0fPYGF8aQJvs_xCWNjoe47Vlo_Zb4AetM22q69X9EnNnnse1qaMdO8HU34jJuQDtt2th9aY7wT0LRrwCzlJZG3ovQsGL-eHBxYMnkPHibQ8YSC8qvImMvXK5FQ-5hJt0dWmesqB4nUvl7RGy9srTAWZQsRe5CFIMfI-l2IVxiJg4hSbfEDWyGizO_m9IXWmZ9WApIXSRJ_-2CVhdwjl6CVguT8S2Ksh1RfUYuImO-x6dVnt7FyouO-hteR68N2BI745UXSE81BIOV75g5VQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e115a319.mp4?token=j03Lq-z9CZmHeKQyRZPw8eA8tEhInlH6GomjP8KrQ-s5Hen80y9ZEQPdWOPL-1qhBT0fPYGF8aQJvs_xCWNjoe47Vlo_Zb4AetM22q69X9EnNnnse1qaMdO8HU34jJuQDtt2th9aY7wT0LRrwCzlJZG3ovQsGL-eHBxYMnkPHibQ8YSC8qvImMvXK5FQ-5hJt0dWmesqB4nUvl7RGy9srTAWZQsRe5CFIMfI-l2IVxiJg4hSbfEDWyGizO_m9IXWmZ9WApIXSRJ_-2CVhdwjl6CVguT8S2Ksh1RfUYuImO-x6dVnt7FyouO-hteR68N2BI745UXSE81BIOV75g5VQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناموسا اگه اون ۲۰۶ نمی‌دیدم فکر میکردم خارجین
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/92328" target="_blank">📅 17:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92327">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSI9cY8nNyrHDu734xixMrvS0Bw3q3jJr1__8XWMSIvUKqwOrw-xTyvox1lzB_1-n02PKevGwBBawAFFkjOlYSZzg3J6Jjk7b8rIYWHSVsXb-pAu-c1jArjtqbhUw1sCAzBWHbCFLYR2v0ccnYUAihgzPm63ogA2CAqcWfOixrH4R0kW6Ebby9eaaMAGRaQ8hP8iVMC4u0NQrxYrlmTOtEF8kX8JIGm3rFOaWbGV-rSfUbNL8_BzlWa7VUDTS8AAyzruL1L49vi520Q6s-oAlwGaV84bgXjt83Tgd2d7fW7xzfHuq8xexWHM_Im1_8jgWfJVW1mZIgqQcY6R18-GPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏆
با اعلام فیفا ادهم‌المخادمه داور اردنی بازی اسپانیا و کیپ‌ورد را سوت خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/92327" target="_blank">📅 16:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92326">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-IyGWxfd5GDApySd45_WDndGwFMWFFDZ9nnBi1E6KXP9A9cJsj6CTdIfRXOwxhpPT8JE9b-4JHWS6CWvBA1IieDAGAS651dVg4g7QOlu8B-Bb4nhkETpKfOWK7-Xk1sSR89FgfRTqQWP-bRHTMATjkvy7oX4sqSQSXVUfUBbOn5CRmyWjSrOIUSwLeBOyBpD5Fz2vGm9FgjSdDooQThQS7vXrSjnnkZDQk2S0aQn0N9C3PPb6SJY4x-TdAMS6Umye5YAB8xDvDtb4FwDQTogZS27VpEFTp-l2BH3IeqFBPGwZ93AMwEU059oBXTR1h1nHkC5kwTTjTbC7oojBUsgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇧🇷
#فووووری
؛ رسانه‌های برزیلی: وضعیت جسمانی نیمار خوب نیست و احتمالا سه دیدار مرحله گروهی رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92326" target="_blank">📅 16:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92325">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFcK4WI3uoZq-OpWUHwqn9thS67JKz44lbeGPH1HC3jnnZu58LuhycaP4xV1Vy07qymyOrMfsxla4ZamXnSFfEuzPWZHKAnoIORQozn_5YZQUJt8W3-OGO2q5SFKf7hjDUKcYwq6AsRNnq1Xn4dcBJruGwnNRV373hxqr8vJgt1-J7HKnZR9REvv33Kv_ptLeaNyd7BfH-_lp6l9nKYQDZU40xJ7Pw5BJducuv0d3OkN0-G084Ud0STFVMvdOH-0_oBlhSUMRyGiGdQGsqzIkfupuekgZL4L4HeeT_ZEQ7wOUSmaDTvmFqI69VSTRGDaN8iTFgRYYwvM2T9fRKYgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
🇳🇿
سزار راموس مکزیکی داور بازی تیم فوتبال قلعه‌نویی و نیوزیلند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/92325" target="_blank">📅 16:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92324">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOGbO_zbpmvFBqhsZI3fgpio6_L3N-aEjDlXEp7dRbP0u64Kvx2dPiYwRukxGtYxGEeG8R7pn74we9kbZxv5Pt2bYlHBgmUGJz84QoMB1uSqpj0m1LGUcHbNFp-FgUP_cbHDjFsy9d9LEbMtXjoelhenXWA6mqueQvV6evjpy8N5IGJqYoBylcK7ZVk7UJk0uJDpmumIFchDSQiqtX_wVMJAu37HnxReEe1JYUNRJ95cTEWug-FZvjHgcmxpdpLLDphgEbf7m_97WjAWb3SuVk6JVWBCm4JpaokKDUjMGVmyiKrGZ_dCf06mZkY_lKZ8n1BbCiuFUKrxXzTZcwhQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از رویترز: توافق بین ایران و آمریکا توسط جی‌دی ونس و قالیباف امضا می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/92324" target="_blank">📅 16:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92323">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8fe0259.mp4?token=LfZpD1abBuX237kQskDOS3auCmCNSdQxbhNOhsnDyNtC3rCHv7hpG9jFtK_ehxCaoMTHOd6Su724PRcsQ-_Vxe3Nj2tMrovsOjaJuUj1-6Sg6j1yjw_GABOK876H9L_FX3078aB8sWbr98F9AJFwulWP8yFEF1dOb7q-JYEkAK5hklo4dQDiMT6HDn83BP96GTamA0uPojzfi3FmYIzeE2P8wHqo6LG5thQfCRQTZNZxIMgoULDQJqyqbBBrLf02JO7pyOcBAN3YKRxi_SKvLFbBIv5rACRdxa5p4xhY64NRohm0puCBCGo5ryPYli2mJIm-uMX05ZcWUaqaNAqI9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8fe0259.mp4?token=LfZpD1abBuX237kQskDOS3auCmCNSdQxbhNOhsnDyNtC3rCHv7hpG9jFtK_ehxCaoMTHOd6Su724PRcsQ-_Vxe3Nj2tMrovsOjaJuUj1-6Sg6j1yjw_GABOK876H9L_FX3078aB8sWbr98F9AJFwulWP8yFEF1dOb7q-JYEkAK5hklo4dQDiMT6HDn83BP96GTamA0uPojzfi3FmYIzeE2P8wHqo6LG5thQfCRQTZNZxIMgoULDQJqyqbBBrLf02JO7pyOcBAN3YKRxi_SKvLFbBIv5rACRdxa5p4xhY64NRohm0puCBCGo5ryPYli2mJIm-uMX05ZcWUaqaNAqI9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
عشق‌وحال‌ این‌روزهای هالند‌ در آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/92323" target="_blank">📅 16:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92322">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz8FSzZNvQ8wn8HK8oSLzn8e77AyRJ4MTBHmUVllgGZMigSTn-Jo2uQtLVovxTWpGEmX7ZhZCy-lhQsvkR7L-DFKdvMZJePS__NDlQDJmBepKklLBI42d6ry36fz_GaJMSqamagj5-qehG1B_uBjSGlXgLc9KzptA4OqJXRUREKWKe3zWvHJgR3AWiwOenwOKxJdtl1GBZUzUWxvFB5pF6U6z09GreN3UOV5NlENDnyRwXHzhzwDJrYS0OmpaJjcv789sBp7BaiqG-gqpQqxzF5xxsszg-CevKDseCJKcFFNVnnxHHz6gUb-YvEo6d8KLdL9iGVImfLNrmM7MqZi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣️
عثمان دمبله درباره انتقادها از امباپه در اسپانیا:
آنها با او بسیار ناعادلانه رفتار کرده‌اند، مردم نباید اینقدر سخت‌گیر باشند.
ما کمی بیش از حد به انتقاد از او اهمیت می‌دهیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92322" target="_blank">📅 16:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92321">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWrJPSJPuHlEUn_ZVZ-ZEjLewvpeCXO3gUkbXIt8j7zt9i52odOM_J59BOQuLzSd-8taRhQByAyBavCSSlKAO55pNn8He6nB4pW4_e1ldAGSLEEs0caSGK6L4gbF9yRVFvOE3SYyB6TXYBqOjlJpQJOMUuJAgsWzSikrRj8kKuDRQl4302G34bT6eTUcarOfm4EmMSmINblyy0HD2RQisf1SPydzQ5a_wHNhBnPrayNEe9jY-bcveqqhkNC4FXD5edd7DQAhfM2Mkv5wuCe4ICxih6VwnUCnu8LaByYQIO0nGUy7M0RH5I-yR6G6a_DebUInxTpB_bt_UAwHTz5kwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
گاوی:
اگه با اسپانیا قهرمان جام‌ جهانی بشم موهامو صورتی میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92321" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92320">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEmBWvUpiMzpU67WPxVVmElQ9RZf98wCCmQf8RA7NjtdtFuDaWIodSE7KgB4mAYLjg1H1bmF3GtBXIrhYP0dSG7easQ_bAaoSWP7Q9ahs5SResF0E3wf4yy_MEuvHIjirQdP-xo6nN8KBdBpT2ZsP2nHipo1uuRvTx_llu_VWH6Qtq4c_8ZPVIZ-gxHQsILXW-g7pj2u2zMLV8L2EOF9rOHQyPzBBJCNbhvWdg5jMMI1LS4DseFZMBpsq88pV6StvT-ELpGdxO0jKAKhPI88IVR2mPV1XKFaSrI709YjPE6PtZyyf6zG38gAqavgUNIjYWJiU2LdlChjKNWlMMnvZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
این مارکوس پترسن نروژی است - او در پست دفاع راست برای باشگاه سری آ تورینو بازی می‌کند.
🏆
✔️
او در هامرفست نروژ به دنیا آمده است، که به این معنی است که او بازیکنی است که در جام‌جهانی از نظر جغرافیایی در شمالی‌ترین نقطه کره زمین به دنیا آمده است. هامرفست یکی از شمالی‌ترین شهرهای جهان است - این منطقه به خاطر موارد زیر مشهور است:
❤️
خورشید نیمه‌شب: از ماه مه تا ژوئیه، خورشید هرگز غروب نمی‌کند و نور ۲۴ ساعته تابیده می‌شود.
🌏
شب قطبی: از نوامبر تا ژانویه، خورشید طلوع نمی‌کند و دوره‌ای طولانی از تاریکی ایجاد می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92320" target="_blank">📅 16:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92319">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmGV897bWAEPXJLeXOkqayQ69mWfMdYQ50au4u1_WA6VRRKduYmcfA5VrDo7JJkYEJE1p9Gf4XPKL009ZPhWMCZ5SKuClTPOjYP1upCmJKrq5cnT5zFI1yx40JLCqBUjJNHPyI_HLTiT1ul6QZ_c-cGznDIpNSGHKzCBGgoma2GtR_ADblbUXK4kqmdQBtxPZqF9G5RP7T9ZcCxO9G52ZnplejhU_PytYdWEXbiy0Z57YX45M7-YUjq1g6p1N2HgYKIxicxA_gP3B6vshxy6U2m_O8wC9q74l05Ky3SbBQ1OhGVM7LDzkcPxbCy9s0PgHFJzynRI-qKlRl_ul8gJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گویا برنان جانسون هافبک کریستال پالاس، با لیلی فیلیپسِ پورن‌استار که رکورد سکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/92319" target="_blank">📅 15:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92318">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a9fa2e76.mp4?token=i-EX03rwGtVimu1JD0gIyu1N5D_c-3Cz1oP6A-A8kIHhknCvWDgMJbjesHdJsJUJH2nLzkTWbJeq77f1Vdzh0dou7NhOkeuklNFp5S77VUtLj_CvJ21BuckehpC3UlJAsZ08EFWtiNNBGYwRGohq0XZmTZ0xfePjnij5bcoKFqQqHtwLd56X4tLrt9EHG93kzC450jSftBqAbW1g09hg5i9fIhoYtzGnpPsvnTrt8336_uQSrSwWQPPX-2uAD9VfDTHKOKBB9dJqQXhh6hpEejqk90BNrIKXmmt0off0zV8mBOWefKeF-IiaNdF_CRfehhT3eqJ3AtZ8exutfyJSkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a9fa2e76.mp4?token=i-EX03rwGtVimu1JD0gIyu1N5D_c-3Cz1oP6A-A8kIHhknCvWDgMJbjesHdJsJUJH2nLzkTWbJeq77f1Vdzh0dou7NhOkeuklNFp5S77VUtLj_CvJ21BuckehpC3UlJAsZ08EFWtiNNBGYwRGohq0XZmTZ0xfePjnij5bcoKFqQqHtwLd56X4tLrt9EHG93kzC450jSftBqAbW1g09hg5i9fIhoYtzGnpPsvnTrt8336_uQSrSwWQPPX-2uAD9VfDTHKOKBB9dJqQXhh6hpEejqk90BNrIKXmmt0off0zV8mBOWefKeF-IiaNdF_CRfehhT3eqJ3AtZ8exutfyJSkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سی ان ان یک مونتاژی ساخته از صحبت های ترامپ که 39 بار گفته به توافق با ایران نزدیکیم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/92318" target="_blank">📅 15:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92317">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lx66b6n42RCdVxtBdJD-IQW2D2Lc1Nyf79sYgds3Gu1gf7z8BAvuaWSswLzSD8nH3JTnDHIhJ3EeLF0IHkUJg0yeXfsdlClt4SrpKPtKoVRlH3qQbBouzME6uYDcQPS8XoauOJNzCz9yZXLmSdSfYa0XeoUBtyeImnWlbZOaZSkYldGONUGbTatHxIEpe0dC5EKlGstQTWXTvU_4OKyT6Uct3EYkGmgIot6d_ps69GpZIsr8zfaOPnjIyRNnsP1SaoEdUrauOzoBikHoAblN3hSzckjoT8MPKegpVhDtkSCbdxLqvl0WtoQ-4xtUh89RCjH_mvwXa-Bw0eUSNZvjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه حس و حالی داری؟
🗣
کریستیانو رونالدو:
مثل همیشه احساس خوبی دارم، با شادی فراوان. میدونیم که این یک تورنمنت بسیار خاصه و با امید فراوان وارد این مسابقات میشیم. از نظر جسمی من خوبم و هیچ مشکلی ندارم. قهرمانی؟ ما یک نسل بسیار خوب داریم، اما عوامل دیگری وجود داره که کنترلشون دست ما نیست. من معتقدم این نسل شادی‌های زیادی خواهد آورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/92317" target="_blank">📅 15:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92316">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5TENBSzauchq0n8pvE9_3GaclN-Zj5e2CS6GqPdBCE962UdvLjDCMF9D_PNVEj4T6QxCCE6hR883Ghcav1AJsb9wIMkk7YTVqBjeoRD-Pd543TkFfA8gk1EMwFebytbHqMKhxccNJA28b_oAQ4da0e2tfQ3oDGJ8jxB1rfx9q9b5uVHe82fyoVwpvWnB_kZGrSMC2BL6XG4aMu1780T5iJ8beJAqo3tKHfS-3RrczRTWv2-QrB7SG2ARDsLiMYo4dZeDbJ0kHOVB2dHKPgANsefJBfSZY__DjRbQXlCjKhDQWC_KmbDqhAzozuCtxKTtUP2ge87ZXoqJ7kTTXi6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
هواداران جذاب کره‌جنوبی در بازی‌دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/92316" target="_blank">📅 15:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92315">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If6vaI8vB3mveSbuQM7h5VCFS5FScDbdSlht9vWpFLxE9dGZoxF8Zz_OXyEx1HbXnVdtScvUZQzlwp7vqI12PKNHGNXIkXxwwY4gzZUGvrknVPZyGvu1SO9vRRfPcg6dp1oeHpF9t1l1fqGpgg11xWudYo2Q9dCD9CN_p1qctcTPLjb8caxaKKLAwNWJojpQJKPcZ-nW6UXx47ycf5zrlKv1o3DCKKDOTHSrdec3hE98xF-pv_J8AZqFp_qM-GqI1tyC8uVcLBXARjVjtxTJu1kqllOAqBxRVadnLREyYVgjby2GWOmdl6a1xm91A_rDIhyrhZdT65yy9uB-4a7zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
بهترین بازیکن دیدار افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/92315" target="_blank">📅 15:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92314">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plx18OXztv11YdilAR11mXlPXQApIaXGlTJWFt49Vx0kwA1o4cyhLCPS9UkNP6QN0Bn6y3lsO3vBWzl61eqRafYW-FqyyaEgAAIt-lLIWzY1bAc_mdX6PGURIjaEMncsYkrtrAxHwYTIENWHGyCq5MV794q5ZpwM6gB7ZH7RJNAnhw_MdG8CIjZGnGoKQYSeuV0D3Hz9KRt5LGzXfHtEEUpFTsqDBAd77GFdrKAHQLlZIq59dR0BOkt4i0Y5v2x99a0ae0tFUxaf66dQub1L_cfYJ_UjIINegoYAoj3G6DGjk1achbvw4LiHKM7sCJZeGaXrcoy_iMwzBC54G1pz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری - موندو:
عملکرد وینیسیوس در جام جهانی تعیین‌کننده ادامه حضورش در رئال مادرید یا خروجش خواهد بود!
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/92314" target="_blank">📅 15:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92312">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMS2l2_4ZzQ5Fu_Hp4UWS4hf-1rumj-V1wxG9-Hc-4hYxsCxYt0CEpwDMi-8IjuGTRmywofe6RcBaqLWcQ1YWWz7eomN2vkACfWWRMF8xgMNTAQnSIvfYfGh2hr0Suqr2_cdca406PAZHcmJw86WJ7LcctCBKRDxiiAw6x-ofL8l9YqLXz9sVq1GK90PWf7T8qvrgPZoEpazmdJR7yxAB3--3IbuCtGvp6BonLd_n5-z3C1uhgeK5eyqcCMhX_rrPK71e-svcJztq3nXPbKShRs2GFmX9pDHrQANO9Qg-kWFIiN56_cJeZrpL2GGh-bM4vZfNWdNQO8_vrGOzQXUsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhs2z6p3o2kghsG2t-5mPvv_YqaUFuwfy25LeRRD8aRoevWZILd2nHtj04AkfjNWVJkHylbwa21_GpU3teUc7na1xvI2bg6p_dgObteycQBclyjcX3UHrla2iqdGmLnOGa9fBxRCnJtinD7hECtgAJBUjaBvsv9EjKqH6VvgrSEcw9nzn2oSpIJ-aRQGQdRbTlITHqZdEewUyC8JenytI8njZW_PgZTI7Mk5N-E_I7a4xSsi9Le138XZYxzdM9C4vgbQPaC2EfdMkIt7C2OiAeJ5qoZR_C5IcngD_l6ey3daXqZw7MIamnoczOqBkuUDEziOgshghPUCpRIF8KgfNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بروبچ تیم ملی کنگو هم با این استایل خاص‌ وارد آمریکا شدن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/92312" target="_blank">📅 15:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92311">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6VaQTWBMMFGtDi6KkjUj8qaw8cY2oTYIlzZml1DOys5DhShq8-Rv9lvbDeqsA63pc-gI31dvVm59IMBhyW0yi-kcT9GFcnRWYnwM5AJy7VFM5baUlhec4Frb1VwecBJcfG4xTV7oFNd-bh11Q0Qsg0wAeJNh3y86hRtuhFuZIoJSKKSDE9T-C3JNFP3m19D6SCcaMz-6UOz9NvdLz1WzTXsyGQpAdCp8zKWO1kwydysNNzDAjQhdjaaQvAw_X-_ptduoYbdAWGVQcxn7wxu002P-Af4u_-zB55pSaUa4zZzeNbZ7YT5phQYMAjc_1-0IJBb54KF3_jWSS-apVHIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل اجازه داده که پارتنرای بازیکنان انگلیس وارد اردوی آماده‌سازی انگلیس برای جام جهانی در هتل لوکس وست پالم بیچ، فلوریدا بشن.
🔹
دوست‌دختر جود بِلینگام، آشِلین کاسترو اولین کسی بود که از این فرصت استفاده کرد. او چهار ساعت با ماشین از تمپا سفر کرد تا به دیت با بلینگهام برسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/92311" target="_blank">📅 15:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92310">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5515e03704.mp4?token=WqiYPT_E8-Crrw-IHSgxXmekece7S87eUABsMhzEdEoV9HzyNaoccDeSV8vERgRc2Ei3bJf_MbgXKrxRtai2HIEzcUL5rlpOsKH-TUDAFDjPOw8Ba855XtkCi1deoINRv0vgN2MK7WuYwNPusN8i8PeO4HOd24MxodiP5O1zBUnTmwcY05TcTgrkvXU4SfNKrYjUDlihMij0bvqq3U5O5rZlKSjdOIMI4Fof4xXpfcG2gv68fPqvlgG8WE0a0SZKZjUTHyyb-eHnPIsC3zxLViSHIOcJCcbRtGse6gmTUWHqKdBNtyi0GvUNJqdmZ7mhFrG7GrD6bqyp5UjkT02ZxrvQodA9VsHf88sf_4fklehbJk1LENvak-_qMZVovCVqu0yjHy59fM5NKfMNGke_oZMvrl4V5jZql6ZNZfbVYhGs0flcWg9aWuxTU2c4MYjsKpMqam-gatne0TBO3PsTxMxEa-9ZsKeU7MfPqPSK4i1t5HD3Yjpv4kGmgGkdzs30EfuiywvT62McJVh3FTi2Gus_bGPGqrL-HT7CK-Lzod2Ob_ujGq3wL0oan4Plbtm0CXVFhQUzFTULXAwySgQ-dEp4WG_4GRoWB6_nUof6gUHIL_zGNI38Aw_elMsu-UQN4bZegeM6RwQEV3aLIDL61kjL4kKnzq3nu7if4s5lTOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5515e03704.mp4?token=WqiYPT_E8-Crrw-IHSgxXmekece7S87eUABsMhzEdEoV9HzyNaoccDeSV8vERgRc2Ei3bJf_MbgXKrxRtai2HIEzcUL5rlpOsKH-TUDAFDjPOw8Ba855XtkCi1deoINRv0vgN2MK7WuYwNPusN8i8PeO4HOd24MxodiP5O1zBUnTmwcY05TcTgrkvXU4SfNKrYjUDlihMij0bvqq3U5O5rZlKSjdOIMI4Fof4xXpfcG2gv68fPqvlgG8WE0a0SZKZjUTHyyb-eHnPIsC3zxLViSHIOcJCcbRtGse6gmTUWHqKdBNtyi0GvUNJqdmZ7mhFrG7GrD6bqyp5UjkT02ZxrvQodA9VsHf88sf_4fklehbJk1LENvak-_qMZVovCVqu0yjHy59fM5NKfMNGke_oZMvrl4V5jZql6ZNZfbVYhGs0flcWg9aWuxTU2c4MYjsKpMqam-gatne0TBO3PsTxMxEa-9ZsKeU7MfPqPSK4i1t5HD3Yjpv4kGmgGkdzs30EfuiywvT62McJVh3FTi2Gus_bGPGqrL-HT7CK-Lzod2Ob_ujGq3wL0oan4Plbtm0CXVFhQUzFTULXAwySgQ-dEp4WG_4GRoWB6_nUof6gUHIL_zGNI38Aw_elMsu-UQN4bZegeM6RwQEV3aLIDL61kjL4kKnzq3nu7if4s5lTOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇰🇷
🇲🇽
دیشب قبل بازی کره‌جنوبی، یه هوادار مرد این کشور از یه خانوم مکزیکی درخواست لباس میکنه و بدین‌شکل وسط خیابون لباسارو میکنن و عوض میکنن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/92310" target="_blank">📅 15:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kenv9zNPq1XsnJsNWW1q8RzNNOed91Ju6vH6HTTc_xlWtRrKQxczMPP14oxGRsT2JS3LCXxWE6dKCL8cSo8qfmA2SQ0_EfaV1n0840y_D6QSOOzbEsXTSZUCdl9lx2VCP7DwBeYnDF4fCeFMEY2T-Anox0vcTdzsILhEW_Gg1QmOo-RXykjw0yopEcqdEYQn-ES0PmNU9nsbGQysXmKg4q0R6LEwMsEU5LlvO_D4xqArzI0XDdX3j0VYgaaY7HVJZAvu-xZ1XE9-E-OK52LT-3eMqGktFzHDyubBLt4hydW2Y_xaHfkH00xk3QdG-iBuMjsYC9iivblr1owFV9rt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzxcCp7Q4c4nekv-gTo771XIT4Ejji338aeUsVazIY5NsZoAImUsj3UFmgs1oBJ75pi5hpuwvBvFwkuqU0YOuCKx4aaV3PvYRkc_5HMIP0MnLYdPdx4P0HiaDRhv1N_E7mGQdJ9LXrQx1I46cUVSMD7LTyEGzeGCKrqhgsJAWKZCUbvfYtwomIKZQ9AenFMKuV2DRp0JeuWfdNxefffu5nylkvvYa7rUW3YspTjt2ATRah_5f1oeKD9kh68WEzGrsNH5u2Tr67aiMfIh8oP6ZU_4agTaIKoR6o0ZBZXyZvrItEDWfCOdBH377fguFhMLi4lLL8RW0457HK3h9yid5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این جام جهانی هم قراره زیبایی‌های زیادی ببینیم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/92308" target="_blank">📅 14:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d71bdc80.mp4?token=jNtuadcKKFcmJTguazPUnCa1b31sVXQyZMYk0Vanx9SA-b-egJ_Kmj2hp4uY_c4YHLwqXxrVAxj76-U7hQh0tZuryBbEjGmhV54VTToLsuQaY4-arFhXCabMpf3g0mHUt9W_6rhCNPkQ9548L0OlQ2bJuMhD_2K0DPVZuvAS-dGBSLi3HpPP7KNX_XmhDolMaRo8sqsn5abj_B32Bz-6KvmJL2GOWpJ3Kpzr2xT9tHNOGyvz1VJnY7L-Wr08RL_WxC0fuLMFiaYFOIgWHgrGl7VUz9ksb6PUYNOTScY8vm50qzARo9QBBnuWsZ7AIsdIp16YAvSdiIB0n0_wVSy33Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d71bdc80.mp4?token=jNtuadcKKFcmJTguazPUnCa1b31sVXQyZMYk0Vanx9SA-b-egJ_Kmj2hp4uY_c4YHLwqXxrVAxj76-U7hQh0tZuryBbEjGmhV54VTToLsuQaY4-arFhXCabMpf3g0mHUt9W_6rhCNPkQ9548L0OlQ2bJuMhD_2K0DPVZuvAS-dGBSLi3HpPP7KNX_XmhDolMaRo8sqsn5abj_B32Bz-6KvmJL2GOWpJ3Kpzr2xT9tHNOGyvz1VJnY7L-Wr08RL_WxC0fuLMFiaYFOIgWHgrGl7VUz9ksb6PUYNOTScY8vm50qzARo9QBBnuWsZ7AIsdIp16YAvSdiIB0n0_wVSy33Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
صحبت‌های بامزه دیبالا درباره مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/92307" target="_blank">📅 14:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hzwy1B-M8Z4CHTdK5o1TbemA9M7whrDAZBWHM4oSEUH4GJRjidkiB6AjevfORSQhFzNlTimRADYEXxxWRce5LUmPoQ-rWaXGz7HDPJuV02E_Ek07onxMWNfEHIHh1AUskyQ4tcGCpaRNB3E9pYYE1GxLGgSh1lQ-NORNiy284pUJ5LObwvMhOTwD3V78qMQt2rRya7o8vBOc1pLOj9JZbAPNhrK9NeEPS06AYTJNEa5FaDKX0dMO1MNx6dzS2-I8P7c6oYqnY6trKsU1UUGeyxS7MzvDy9RnZzfhbEFVWyNQCGFjAoh9leYLuEnzfeL7hZ03w23WeD8Umhhiqrsjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هوادار معروف کرواسی اعلام کرد به زودی با استایل جدید تو این جام جهانی هم میبینیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/92306" target="_blank">📅 14:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92305">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQWpNopl-ubzRBEsxeb-olO-_C-L5_vd-ZSt7HsSVegVoPa-GMOb-S3fPLtlraqCrrm1RsrOIIm5zuxzlKfu2fi4dSm7lxBt7F1LO2B6kidlcw_qbvfD_uQvWfuKF2C4eTV0fsWaxphHxSX6cupu6H7kHyPuAMfQxX1FB16eoLSqqZcii95xTm9b0YBDijBRPdcyVulAe8BmKPi3OftU75VqwsNlnGERUVhiK2BmCIJ4anzLEVgkwixuYFaeFd2fEXQhmXURa6A_lrw6j0hT3wEo9zWf7bHAQ60Q5PETPFZp8Qfl9LKo1u9SVUK5vTo7RVc6klQeDo_r_T0oQFUTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🇯🇵
🏆
اولیویا، یک طوطی پیشگو در پارک حیوانات ناسو در ژاپن، سه پیروزی برای ژاپن در مرحله گروهی جام جهانی پیش‌بینی کرد.
😁
این رویداد توجه بسیاری از بازدیدکنندگان را جلب کرد که برای دیدن پیش‌بینی‌های این پرنده مشهور به پارک آمدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/92305" target="_blank">📅 14:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92304">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
فوووووری؛ سخنگوی وزارت خارجه: متن توافق‌نامه ایران و آمریکا تقریباً نهایی شده و منتظر تایید نهایی نهادهای تصمیم‌گیر هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/92304" target="_blank">📅 14:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLEO2bMxvV4yKZSrWcgKPciWavEf7f4v-p0xC3zuj99iMHI-JlO_YGSwwkH3HidABH_P-_toad9YQVyLsRoa5fi4ReTeidbFkz56uQM3M1lZNr2Z0TzNDp06jdjlRM4Pwt2NBB3QB5z9ViK1OOEeYbsEqFsJwBie6ddHajAyXmgxZNIkEelTdiRsfEV_EUYTkuF_N4ohYwss_GDvPaFHu28fvN7DcvnF_kAUwbbwU3-ZM4jxKOA-qgDUcP95pG7fR7Kuj6jJckZ5gvKNMQA5Mi7aT-N6-YwWTZhbSnLL11G8tBHJbFD0J3fuwoE1WPSzePIwvktIsbPRtBRjXb8xjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
🇫🇷
عثمان دمبله:
مسی حتی در سن ۳۸ سالگی هم متوقف کردنش سخته و با تمام اطمینان میگم، لیونل مسی میتونه دوباره جام جهانی رو فتح کنه
🔥
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/92303" target="_blank">📅 14:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92302">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
👀
🏆
رسانه‌های جهان مدعی شدند که دیشب تو مراسم افتتاحیه جام‌جهانی اصلا شکیرا نخونده و بدلش بوده که اومده رو استیج.
❌
این ویدیو هم تحلیلی هست و حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/92302" target="_blank">📅 14:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92301">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNh4fxX1oJtoXFRLtfRJLWWSeXKyVAoUqy4CL_BQmHwZfwOpJ99BZ6qfDV3jNJvsDzTMecWjksrRSjSCNuuYlKyho-3rTTJZZhKpV8HFMKFOi1lrmMBI2RLzF8jlYu6ucmOvgs4zt8B3z-71g7blcWNuGAHFaS41FWrdfrhlVZ_9lA6EA1OCgadquyLGd4kWscJRfdo-uPtXaCduR2pgx8PG97PtUR2NdqUwNxwYij8J6KIiDHWl5V5se9UJFZ1LUC4ouT-spjrjNpqruq_LO4bdWsAMnpLgYU9G7if_v9tL2MzVBeFMF_GTmA9beoBtBlOS0a3aEuQzmD5lfzl-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🎙
🇪🇸
اشلوتلبرگ مدافع تیم‌ملی آلمان و تیم فوتبال دورتمند: رئال‌مادرید؟ بله خب یه سری موارد هست اما باید بگم توجه من تماما برای جام‌جهانی هست و سایر موارد به وقتش رخ میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/Futball180TV/92301" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92300">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOJx-JFnGohka4f28XsL5ybhv4IpsU0xoLL7LNuC_XvNMY-0rezWzXzFlBvN478Gyl19_0WbQCUPnV8NUlKvItdzQsRSAl3fcM9-sNGWifmKTDJJfZ_rFM4Vlkv4DcoH7D_gtkC9aaPrm_adzRVXH6Ff5miiZiu0YICxlJE6zIo-r2eOR0pXqw-EpdAI9zZcMpO5ql82E-bBukpV_5jyIsn1a3MOs-qlArn48_sBhzB4iW-tfwqUFlus99j845BsGvwNF09N9Hvui0QcZQmlx6tOXyEVMDhJLx1cOuLrc0lMifCBw34DW95u8JVz40M4rsYtwHSrNdNfjTNxk-kEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: منچستریونایتد درحال مذاکره فشرده با وستهام برای جذب متئوس فرناندز هست. رقم درخواست وستهام ۸۵ میلیون یورو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/92300" target="_blank">📅 13:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92299">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQekX7UMNpnEXSfobuyDhNGk1t1MArx5s6k8NxfqB5wBz2d0lWylnV57yHS1tBmXjdBS-yeTJAS_ZUnebL5RdMW3d-bUqpyaayiPH1x0JESp7egg93Ega9cxphWkregoDmMIbYmQ0TsfGW224segaytzlnzxGWLLGDOoaUsAtnLdpoQ3evgYQVsDS0eU-D9yuEaVUNibHaDU_xhH5OXX0-RJBEJCS_iOZRS0yb6fhng7vz3I55D5RYWMP43nav0otsS_rQauPGoJZdKLS47t25pMUwisa1ZcgVSUSQKFUwv-Bd8EoEN16Y7fcrdsEJKsbsPm2OJnlXfWQyL2aA2Lnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
🇲🇽
🇿🇦
یورگن‌کلوپ راجب افتتاحیه جام‌جهانی: عن‌ترین بازی که میشد دید رو به نمایش گذاشتن‌. هر دو تیم فاجعه بودن و حیف وقتی که برا این بازی گذاشتم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/92299" target="_blank">📅 13:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92298">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULFCfAYBIVMZrbI3EGerCdS3JXC3TPHcvcBu1vQAImSIFYsgECUJiyn6-VSKF9dA-27TAy4VpK6LJxr5ZaddSRUCwDMWmIvGd2GrSHffLaQsNzHiqnkrsct9GHJojADtJGbfI650-OfHgX8bdsfS-eQxgLt44TchNYdLIOnK5OB1dK92K0dmsMztIyEiqZz5HbetyR-ttRwczfRDHP8ff0gAZ_EQm9iv4qOVCYI1QOFhKCjGwOtABYMMiWiA_6Zjq1cn-w2kK5GB1eoSgteaL9qcNmwabSmbNn8Cjycnl9AUIm2aj39OC_2lh4hQgjRSH_KK1_dvJH3EatE6XgBWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
‌دومین جام اروپایی پاریسن ژرمن توی موزه این باشگاه قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/92298" target="_blank">📅 13:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92297">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZQ_cjgJB8eljqWZ_magzAdmKrT1enF7P2nmbWGfcjBUu62Q_Ub93-69BFe5gsOqjJJdZr4Kl_w8Iy30OhYDq98S6SbuRs5OTV8s-UTPP0k57CqThDffrdhc0Lf_hdWZkWtY_WCs8hgMoTHq8MizSaH_zd9M3nbFjO73fxAXccVPftWUkCUSBeh75JKLVcmtt5d7eeGF-oAzVlH_5JTvt4HsZ3gM6D4mEJsKpS3ROI8b167kWyxeC7DpGFGbxOpwuBoeoxAD5xY6FQYI9qawebz3EtKKDZVTEH5c7SwYSghaUpkRE3GsoRvi6Mku5y8CUE9DNkS6k4ySENDTgIRtkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آیا هنوز هم باخت در فینال قطر تو رو آزار میده؟
‏
🗣
دمبله:
نه، اما بدون شک ناامیدی بزرگی بود، با این حال، چهار سال از آن زمان گذشته، ‏خیلی چیزها در تیم ملی فرانسه تغییر کرده و فکر می‌کنم همین موضوع تا حدی درباره تیم ملی آرژانتین هم صدق میکنه. ‏البته آنچه اتفاق افتاد هنوز در ذهن ما حضور دارد، اما به ما انگیزه اضافی می‌دهد تا در این جام جهانی عملکرد بهتری ارائه دهیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/92297" target="_blank">📅 13:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92296">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5acf7f96.mp4?token=GOfJNLNTyuj4k9XwrgEyYb8Nld4WptUaP4MoMiR36aiv1QIMKRxcV3MMN9PEemdm-fR4Ok2VKXwAwERdiIha4x8EFiylmJVoRRPpZ3_019NTL-vj9Igs3gfrIINuaekopwYYW_xTBWtjSKgWJWYqjnDAMRQbYfeyuVAKNfJZZgfN8SOKPkCy00v-p5r9CO75lRtcFUDuBLmnccg6mswuDm9U55UQrNdJ6OfB7rSFV8JHg9M8wU_F3OVTGGSeR1ka0K_rZkNnmeNkunN_VpEqRMZVQWw0eja-eZ4ijffBJfnYEk-5_lvwoW-9F8ot6aiskUKdfetW0juOH_T5P9vBwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5acf7f96.mp4?token=GOfJNLNTyuj4k9XwrgEyYb8Nld4WptUaP4MoMiR36aiv1QIMKRxcV3MMN9PEemdm-fR4Ok2VKXwAwERdiIha4x8EFiylmJVoRRPpZ3_019NTL-vj9Igs3gfrIINuaekopwYYW_xTBWtjSKgWJWYqjnDAMRQbYfeyuVAKNfJZZgfN8SOKPkCy00v-p5r9CO75lRtcFUDuBLmnccg6mswuDm9U55UQrNdJ6OfB7rSFV8JHg9M8wU_F3OVTGGSeR1ka0K_rZkNnmeNkunN_VpEqRMZVQWw0eja-eZ4ijffBJfnYEk-5_lvwoW-9F8ot6aiskUKdfetW0juOH_T5P9vBwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🏆
🇰🇷
کره جنوبی هم‌ اولین بازیش رو برد تا هیونگ‌‌ میونگ-بو یه نفس راحت هم بکشه. این مدافع اسطوره‌ای در جام جهانی ۲۰۱۴ هم سرمربی تیم بود ولی حتی یک بازی رو هم نبرد، رنک فیفای کره رو به ۶۹ رسوند و خیلی زود اخراج شد. حالا با کلی حاشیه برگشته و فعلا تو اولین قدم چک رو ۲-۱ برد تا قدم بزرگی به سمت صعود از گروه برداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/92296" target="_blank">📅 13:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92295">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYdMWrqQDBKK0xdSKIJM_TC1bacpzRpAahdO7GWMpDkfunZBfRLT3PK30IX1KGKaHtlLvt-RDhnr8QTrpqL81UJyiLQ3tcozoJE-WeGaeroEqnpsvSybs2OvK6nYvMEn4_1ODTuOt3yUXA8gjbrQ8NkT6yaZ9hZ9JhacP1EgNWMugCfFfRXJW9VdQOGLTDlNNzLrRAPq0YAuA-_QzfebKuQ7taTb_2KWp90Lkitz2oHx4xJUfmsuj-yi0-wsDRoeOBm2EZszIlYfEsDXDCpvOqsCgNuqwqql_Y67EX-eV3XxhuhBaXhIxZZoSQh3OSziE2ValCTrWlSoWZW55ArfaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توخل اجازه داد همسر و پارتنر های بازیکن های‌ انگلیس تو هتل کنارشون باشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/Futball180TV/92295" target="_blank">📅 13:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92294">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5962002c79.mp4?token=uGTxAV1D4h5SOpJE-tW8VchcxmCLnxArupeD-l8-3p9NXMB_sFeEj-eewespBTLkhtuSOs8eKmKVrbRqYplDeYYrqwiOZ8jxQUZcL0i1Y33POKOkw1LMTACdwo-A2DI21E8cb71GUhb5XeiLbxeeO-ZERBawUZXOKB3bZieCHyUwswVsVJajILbMz8czzQVgeO4AbyV29obCbNbPU5Z6cTi6fXcR5nGOcyv2B4l6npxKzd0sR1hcqxWQY0V_mygD_XfTVKdYdjPC0KvHoKPY65gtcNEkeKkFL5301mZ92TKDoa08oLEvHC6tGckveid9-R60Gm-nDDjyBYLSo5W_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5962002c79.mp4?token=uGTxAV1D4h5SOpJE-tW8VchcxmCLnxArupeD-l8-3p9NXMB_sFeEj-eewespBTLkhtuSOs8eKmKVrbRqYplDeYYrqwiOZ8jxQUZcL0i1Y33POKOkw1LMTACdwo-A2DI21E8cb71GUhb5XeiLbxeeO-ZERBawUZXOKB3bZieCHyUwswVsVJajILbMz8czzQVgeO4AbyV29obCbNbPU5Z6cTi6fXcR5nGOcyv2B4l6npxKzd0sR1hcqxWQY0V_mygD_XfTVKdYdjPC0KvHoKPY65gtcNEkeKkFL5301mZ92TKDoa08oLEvHC6tGckveid9-R60Gm-nDDjyBYLSo5W_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خبرنگار کره‌ای در حین مصاحبه دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/Futball180TV/92294" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92293">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92293" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/Futball180TV/92293" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92292">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=s8YoPYIQ1bo5SO0Xk4jvWMj1RDO0Ms3GKYhsjFc_p57lLqmbZX8fwHWX-fOKzJqafzOlUSkIaEGFZB6m-iU6fbxAmcLhgpdGEw3XCPJA_npq8Iyy3O9H2zi4zp8k7TlL5hdLCp8r-K_HxlvgCAFCWwn0D4NNudcUTKCx8equNT1cqaUKPuhuio-PAzwSARUBXMZpksM21g_jKwcFSQkOHoEZApudF1f07Qbv90LvjLEBmyB0smyDG1AcvfrC95V1G0u3Ppa1KVyxkJtU-NEC-0Pca0phgnRzMvPGnzBbBzaD75wt0AeOdzPcDGdum_kPwzfvQ-BTTcsacRYHFZi8EhWALTxB8BG8MIR_ZPgly_aiGUH1GhS5mIZgHzqwbyDqNGHXZecsRaIXdI0z31pppEUVZ5ZSN_1h4JRgzeqZwqGUZOPUgbzBUD6Gt_Ud5yHdodlX6IAjLclWSmiXD2fwr0Dtq_vb2UxkIuii3v30vn54zqYgZSVInnxNv0yfB9pi8jgjjL_cOK5BAAf5R3AYlO4wkq8kqYlK9neIiSGdUz_bL5o7yex0lqbGfaQcDOyNQI-c4rw1U9Z0EBklOkxELMaog7eWhf_N7WAe1HcgJQKbwQ9xAFXCx4hy-I-dgPTiBSH2GDWn3CAWtpIk7hW328wst5I3amBU8i71JzlfQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=s8YoPYIQ1bo5SO0Xk4jvWMj1RDO0Ms3GKYhsjFc_p57lLqmbZX8fwHWX-fOKzJqafzOlUSkIaEGFZB6m-iU6fbxAmcLhgpdGEw3XCPJA_npq8Iyy3O9H2zi4zp8k7TlL5hdLCp8r-K_HxlvgCAFCWwn0D4NNudcUTKCx8equNT1cqaUKPuhuio-PAzwSARUBXMZpksM21g_jKwcFSQkOHoEZApudF1f07Qbv90LvjLEBmyB0smyDG1AcvfrC95V1G0u3Ppa1KVyxkJtU-NEC-0Pca0phgnRzMvPGnzBbBzaD75wt0AeOdzPcDGdum_kPwzfvQ-BTTcsacRYHFZi8EhWALTxB8BG8MIR_ZPgly_aiGUH1GhS5mIZgHzqwbyDqNGHXZecsRaIXdI0z31pppEUVZ5ZSN_1h4JRgzeqZwqGUZOPUgbzBUD6Gt_Ud5yHdodlX6IAjLclWSmiXD2fwr0Dtq_vb2UxkIuii3v30vn54zqYgZSVInnxNv0yfB9pi8jgjjL_cOK5BAAf5R3AYlO4wkq8kqYlK9neIiSGdUz_bL5o7yex0lqbGfaQcDOyNQI-c4rw1U9Z0EBklOkxELMaog7eWhf_N7WAe1HcgJQKbwQ9xAFXCx4hy-I-dgPTiBSH2GDWn3CAWtpIk7hW328wst5I3amBU8i71JzlfQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/Futball180TV/92292" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92291">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6KsU1MMWHMKKjO7uQA3bQG2fo8pvzM4OZoohoX6ZIlxMRLt-TrRfBXTWYSbm3bgHQ0edTMDbiMF_vhnn-IYPlT19oibdA_cy7TEtRHVCtYb7DO0PssK4-XxjrAOcxSCec5FKoQQrzSYS-7r-PyuAhD8CdDXR-j5IaDQQ3E0tvaxq8TtLmW2mYYY4Q-Ue_66N4ksReB0G-UimjSPnB4MEIBkJLzZodJXe1yV-paIWIqhrJan7ICCawsMTqozce52SSShWiWOvYjQL2jCQSHaUZXwRGBb9LOVptUhoS5eMnJ_fifiYJAsiLAuecXDm7xJEsakv5Yu_VZzbPNu3TTcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کیلیان امباپه در جام‌جهانی
:
14 بازی
12گل زده
3 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/Futball180TV/92291" target="_blank">📅 12:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92290">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c18ef9a2.mp4?token=kPoNQU3W5W1w81Q1_usSyURDUaerwvxjA5qELHqFX6yaFu1kCVL3lItT9Brp2labUqMiQ9K0pI_wcEOamEj8-b_6MWtUt1k3jYzL3AAAkU0rli1qqGaIohtdOf8oheiLFgPH2MEYUQFXC87ie15UrVtZ8nc8cR3oJ9hypvl-LnkDq_vMlQ65qtNyCGPu7IcbdZmBN0p2k_atROw0_c1444vvKPFJrS-7h_7zRQzS42oYcnyQ0e_06aJUrmZgJtjgq5JTHV4yhR8yaQ_6oaMt7LtQcExrrDEoC95qnxf6YWBuQm83nYEuJ_jVkcpOZlCcWytfS3w1OS0t_I0LTpwtPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c18ef9a2.mp4?token=kPoNQU3W5W1w81Q1_usSyURDUaerwvxjA5qELHqFX6yaFu1kCVL3lItT9Brp2labUqMiQ9K0pI_wcEOamEj8-b_6MWtUt1k3jYzL3AAAkU0rli1qqGaIohtdOf8oheiLFgPH2MEYUQFXC87ie15UrVtZ8nc8cR3oJ9hypvl-LnkDq_vMlQ65qtNyCGPu7IcbdZmBN0p2k_atROw0_c1444vvKPFJrS-7h_7zRQzS42oYcnyQ0e_06aJUrmZgJtjgq5JTHV4yhR8yaQ_6oaMt7LtQcExrrDEoC95qnxf6YWBuQm83nYEuJ_jVkcpOZlCcWytfS3w1OS0t_I0LTpwtPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب بعد بازی افتتاحیه جام جهانی، یه ویژه برنامه تو کشور آفریقای جنوبی برگزار شد که کارشناس‌هاشون در واکنش به بازی ضعیف تیم‌ملی کشورشون سکوت کردن و چیزی نگفتن؛ خوراکِ میمه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/92290" target="_blank">📅 12:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92289">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4813f4b6ed.mp4?token=MSeBa6jTrR-0bwHbJV4HICkvT2AX5qbGvYPbeN53b0q78S0h04LSF7CCmMQq7W8SXqfHrTN4pu13n-ksoPI2RGMh9qorp5YVq6Vx4RyM6UrhbNLIGaXR4jut4K2qVxx3p9wJMjkT42NBBG4vEyJGL3OK81r2LNaIePB7uXzf4oCqCwV4XNtx6jpDvMqGIunAaN0HNNo0MGSHBD-j8TTRRhO9_FUk6qtgDEyxOHkKienSX4fAjXYjjw2BeqSeaERI4qF1ubUQFl_txveShADUuGsQGxIMSnt92JZA1XDmHlSjuguSNYIPBgh-Yosxhule3Xnm8ZBMt2mv6SKpZ3IsUm2WzPilt4-NFQvJR0ESfMuDPpVy0nRwM9L2FEgW43VKWJ-grvp3tf4Ly3R3d8a5vDWb-38s9ymvhgQvrdyVlvXXwz1aDN2_ixEJABA_RrQPTdAocktqoJttNUhdDk7slVqcnDIm1wWTcy0zJW6zNIcObKamfmzMhMtULhh1W-giQWm6W_7svo2TwM0PiL-wMowZ4BkWfoGHypxYz_S50RuHPetLjBMc7LRoF9cF0ddhTiHhqS8u9RP6rOM8jKSL-DSchijUbax3-jJ71lpLj3AVojlXllbpTAwVOQiu1uqo-VmLTWoxSqRk2DoVVA6qoaoLdwh2zn02epqIu1ekVwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4813f4b6ed.mp4?token=MSeBa6jTrR-0bwHbJV4HICkvT2AX5qbGvYPbeN53b0q78S0h04LSF7CCmMQq7W8SXqfHrTN4pu13n-ksoPI2RGMh9qorp5YVq6Vx4RyM6UrhbNLIGaXR4jut4K2qVxx3p9wJMjkT42NBBG4vEyJGL3OK81r2LNaIePB7uXzf4oCqCwV4XNtx6jpDvMqGIunAaN0HNNo0MGSHBD-j8TTRRhO9_FUk6qtgDEyxOHkKienSX4fAjXYjjw2BeqSeaERI4qF1ubUQFl_txveShADUuGsQGxIMSnt92JZA1XDmHlSjuguSNYIPBgh-Yosxhule3Xnm8ZBMt2mv6SKpZ3IsUm2WzPilt4-NFQvJR0ESfMuDPpVy0nRwM9L2FEgW43VKWJ-grvp3tf4Ly3R3d8a5vDWb-38s9ymvhgQvrdyVlvXXwz1aDN2_ixEJABA_RrQPTdAocktqoJttNUhdDk7slVqcnDIm1wWTcy0zJW6zNIcObKamfmzMhMtULhh1W-giQWm6W_7svo2TwM0PiL-wMowZ4BkWfoGHypxYz_S50RuHPetLjBMc7LRoF9cF0ddhTiHhqS8u9RP6rOM8jKSL-DSchijUbax3-jJ71lpLj3AVojlXllbpTAwVOQiu1uqo-VmLTWoxSqRk2DoVVA6qoaoLdwh2zn02epqIu1ekVwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای بازداشت شیث رضایی از زبان نیکبخت واحدی بدلیل شوخی خرکی وحشتناک حین پرواز!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/92289" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92288">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8m1uxyfh-NDw58Gx1GCgXfX1F7-aR5J-dtlWTH0TxqLzViJLYF5hYrtAhoXiyC9oBlooYkbZv0m1KT07wcNvZN748H2PZ0ksRSPnibZOnHbXWP8Rqz7mR1rE42furJQDoy2mIUqNA6rWM_VF_2P7bxJ0oKWFwh9JVy_7KHz1QhC_uHoxTneUnmHp1CqYWjkTwdD8O_DC7d7MtEBBrlXm5WAJ6hTVNdmUlvZ9xKP7ng0LS6gDYpr0nTYjmgddpVltr6kyjQm7M3st2m_MWlsWVvQOuIJawP-whkcVVeLQlASHjiQ1I4jRbm7xY5Xp4wbMjsKXRBQkRmVavkMejXaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یواخیم لو:
- من طرفدار این نسخه از جام جهانی نیستم. همیشه گفته‌ام که فکر می‌کنم سیستم ۳۲ تیمی خوب بود.»
- با تمام احترامی که برای کشورهای کوچک که گاهی اوقات می‌خواهند در جام جهانی شرکت کنند قائل هستم، اما به نظر من کمی زیاده‌روی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/92288" target="_blank">📅 12:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92287">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4x-15aguZSe6iegwGrO6Pt6xRCar920R9obF8lk4-LkQh2xkrSzhlAFNLXYAEoKE1KQaBxxamLphYYKbJ7lTFt1XZhRsfj6v8bVLmsywUMgRO1undEU48Bc4aLOGw9JLlC3fFZUDusoJ-TrcQ_-ocML1vYBJFJVDbcRhkujh5XZHUmGbrsmKEvKjXeyc52Bkh7ZUQt9DWh6E9GX3X1-l23dtH2Jwcn2rWf2YWE50QW9nMWxXqrA7wPnaBSzywnhFKKuwRkEC2xRGs_g_hDHzR9XYhwhVpIhN6we_5GP-RaKMtesorDdqVGLOd1jxxNBuRoZ9k7NbjcRFou8mNjNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پیش‌بینی‌های استیون جرارد برای جام جهانی ۲۰۲۶:
⚽️
آقای گل جام جهانی؟ «آلوارز»
🧤
دستکش طلایی؟ «مارتینز»
🎖
بهترین بازیکن مسابقات؟ «مسی»
🏅
بهترین بازیکن جوان؟ «یامال»
⚽️
تیمی که همه را شگفت‌زده خواهد کرد؟ «اروگوئه»
🏆
قهرمان جام جهانی؟ «فرانسه»
🥇
چه کسی توپ طلایی را خواهد برد؟ «هری کین، امیدوارم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/92287" target="_blank">📅 12:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92286">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQizVkZyPOqpIr_kZW7R0A4_AF1RWuoyyc2fQR4GrGcy0UoihE3rYDgjetp7isXJihOQDkMlS9Bz2rexxkVXN6ctMMRK-wxfrnm4jBt3TVoAowdWm3EXVmAkZ4E4zCTCAH_XLyOePA0K2h_L1HZfZBTlOQwmEJVjNBDRR3qiZErpwmBn0Q3KCtBDuzuL6TSCwznIhxq9pmQ3Z3Qc2Mi-WkwkFEr63XQUhCpF3NdILeBUkB0kXY6WhNYmlaJc-YUMvW_6fS4jqi4D9QkkLpXSQ2uXPaK7wItd8c4BfsdH4Epu8HxVm63VVlw0J9DDuLO6RK9OQqhulo15eFhShM2ZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
#فوووووووری
پس از موفقیت مراسم افتتاحیه جام جهانی ۲۰۲۶، فیفا در حال بررسی تکرار همین ایده در تمامی مسابقات آینده جام‌جهانی است!!!
برنامه احتمالی فیفا شامل برگزاری مراسم افتتاحیه‌ای به مدت ۹۰ دقیقه با حضور تعدادی از هنرمندان و نمایش سرگرم‌کننده پیش از شروع بازی‌ها است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/92286" target="_blank">📅 12:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92285">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKPtMn3dfM-OC0PkqqE8DklgeLW4kvNuuYyEVOpFFpYlxIKVdCGITVqQ6N1SPF2aNwz8Y3ygIKypek5iwsb1twai5YRwfvr3gc2bx-njRFC7r8EdKEq_z6tRYv6V8uCsZEk8G4StlBTVYaOqMGz3Ent9sD9NqL8kXDZoLK8mOwdoYzf6BwP6WHOqc9crj_b658fIhkJP4hYJgvYXICw_SPUz3XTdqhF-41lAMgwcc2VN0BGQmop9WXEZul9o6Tk6TiC2IhKrwKES_aqIPtFnaqyNmgKb9lDnjizKzvTZEnp_2XkEMnnlkVSPhQ7LWwXdeN9bUPx_gV4PwsI3XcxS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
عثمان دمبله [
🇫🇷
]:
‏«من از کودکی ارتباط قوی با باشگاه بارسلونا داشتم اما با توجه به آنچه در چند سال گذشته تجربه کرده‌ام، فکر می‌کنم تصمیم درستی برای ترک آن گرفته‌ام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/92285" target="_blank">📅 12:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92284">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40bfdb027a.mp4?token=OEK2mLNrp4S9CqTG-XYONdg-vhau3THFctu7wFrOJt_6lC7ccowiIxDsyfUCWIl7eYtoYYCGHv42ZGyYCgTf56tCCBQDnBJvfN3KEUDhFEL2ialkAgCVEbzw66YhcHrm60Mru38apVnaNKS8GezX7K4M_XOedXhJpFU1O5ZlsGk5kFxwRk2aUINylRDVkf3y2piFXfymniStP8jguWgtH5p5SgQHOzglhvwiH-bz3H1J98lTOs5NFJjgLJBFe46GrG9cgLVc-MLGUa7pJsOKys7w3zSk8USa32nagmbwggnO6cLmyZ8EhLHCRyp9m6MYYGK_0g-XFh1BYCRn3Mju5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40bfdb027a.mp4?token=OEK2mLNrp4S9CqTG-XYONdg-vhau3THFctu7wFrOJt_6lC7ccowiIxDsyfUCWIl7eYtoYYCGHv42ZGyYCgTf56tCCBQDnBJvfN3KEUDhFEL2ialkAgCVEbzw66YhcHrm60Mru38apVnaNKS8GezX7K4M_XOedXhJpFU1O5ZlsGk5kFxwRk2aUINylRDVkf3y2piFXfymniStP8jguWgtH5p5SgQHOzglhvwiH-bz3H1J98lTOs5NFJjgLJBFe46GrG9cgLVc-MLGUa7pJsOKys7w3zSk8USa32nagmbwggnO6cLmyZ8EhLHCRyp9m6MYYGK_0g-XFh1BYCRn3Mju5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇨🇿
🇰🇷
هایلایت بازی جمهوری‌چک و کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/92284" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92283">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae4e3b947.mp4?token=EZAiaFFozhGXvjnYsv36fHv6bNF7I8BVmj665tjs4B-yR-yj1p9w2Rv8FFEsxnD7_ZR9x2lJylDEQBsulP8YmlB_D_b7l7SzoH_dPoHyX5GsPmehq2XK7gzjBnUdvFYdx2jNN3euUcAOXwRC-9ICk53KgYOU4cPH0s_TcV0T5OE4h-v-TvdXfEDRXNdnEC0naCAQ4xozVTeUchSey3kOKzUhUn6YkyOMI7ewPTZAAVEdBY2L14BnzGxReqAwFXy3jQCi3youG1vZfI5xTbmTRF_sv4tZcwojoDczpVGiNZipc0Nivo8CoPh1xZj2ELbrwHluK4AqAJ6qYBwqLLxUxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae4e3b947.mp4?token=EZAiaFFozhGXvjnYsv36fHv6bNF7I8BVmj665tjs4B-yR-yj1p9w2Rv8FFEsxnD7_ZR9x2lJylDEQBsulP8YmlB_D_b7l7SzoH_dPoHyX5GsPmehq2XK7gzjBnUdvFYdx2jNN3euUcAOXwRC-9ICk53KgYOU4cPH0s_TcV0T5OE4h-v-TvdXfEDRXNdnEC0naCAQ4xozVTeUchSey3kOKzUhUn6YkyOMI7ewPTZAAVEdBY2L14BnzGxReqAwFXy3jQCi3youG1vZfI5xTbmTRF_sv4tZcwojoDczpVGiNZipc0Nivo8CoPh1xZj2ELbrwHluK4AqAJ6qYBwqLLxUxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
زمین‌خوردن عجیب فرد حمل‌کننده پرچم آفریقای جنوبی در مراسم‌افتتاحیه دیشب
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/92283" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92281">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhzGASRsYSNCf3hqoyTOvzBjVhYitIUH2zX-6C_LsjPOuEEsTTaqldfK9Par8AK3qDcn1x6kPc0Nl4mk4ka68rAkl8137a_M85gns77AUPWhGJ1ByCLFHEX8N0AHhHz1PuTRoQmD5TPyDlMQam_3iSMXrlDD3gmrHqA3wD5680hkYLUf9gbJ8Q-wkXuzDKiZQEFN1sKJLxHC_qfeLUnds1riVX8rlPFuyJojoMhfAUEi5ypT7uwbka70E5I7kznHquBGJ52bDa71MsGSqY-MgdsizPid4Zyj2oE0k703WuOTTYSbSnbi7OIVeEoLvAcWeHOBGe04XfSV-sE_kRlR7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇴
فدراسیون‌فوتبال نروژ: بدلیل اینکه ممکنه شرایط غذایی آمریکا به بازیکنان ما سازگار نباشه، با خودمون
۳۰۰ کیلو ماهی، ۶۰۰۰ پرتقال، ۱۱۶ کیلو پنیر و همچنین سه تا از بهترین سرآشپزهای کشور
رو‌ برای تامین غذای اعضای تیم به ایالات متحده برده‌ایم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/92281" target="_blank">📅 11:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avEQwvFK850pdOcOkQpevnYGI75brF3R3vGx5kw0qvzmUFsdjzGY6qlS1HIgcsT7QmIs4RF0e8Ka7mKH2g1tPUGtCU4qK0HCks4Z8qIwlWSm9B8K9q1jxiNOzLYY44PZV_8ernEZHWLqtXIoQvl6TYxe-Q7GJl66LSTp3PRIiIqxLYu-PW4BKFCRh6Eetaa9E9EgMcP5ZqVZiLacQcoVwSaPQdm57w-VsMQOhpRhhg8VMBwJCrJdxP3IZpf1hUJyTqy4Pce9afcgqpLN2AhIRcreKmkPLvqoZe39hBq8g-yfS6yEf7hswMyhZ41IoXvm2MBrefLZI-jmOR7Fbqav1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🎙
🇪🇸
کوکوریا مدافع‌تیم‌ملی اسپانیا: اگه قهرمان جام‌جهانی بشیم، عکس دلافوئنته سرمربی تیم رو روی بدنم تتو میکنم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/92280" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92279">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39aa059d6.mp4?token=VI9mnR0NS8sJKTSplsWqhIw1y5sjBkHsFOz_WZBMj7lB_GxSi17qBEE0p0b_uq-fmCTcdGjblQioFhb0yXmFzYJ7-SBPrUr3mkaWhqnNHYi7ftL0-3UyW5cHnAkXvm6cZ1ZLoLNOAM2BdriX3u_GAbqnRcWKUFxyRuMee-E7Ip_6Q2BRpwAwvmObcqAMCTm5HRCEyQ-NnK86k5m5rFilmpsyTIb8tu4rTlKDez1jJ7zUQVrWzXothL1o3aLhUKkupF6pZktsT0yI7XWnDSsS2IdVPN57ABeNEskUplBK51X-ZpKLeCNSyDgCZG6J4hb-qrSwzcqPGWIOs4Z-jhsecV0sg-Q1qt71I03kLoP6maEqtrkfL0suEEoh4CpxOZ6nCN27_2jCrrmKl2VMm7LrojapB9qwtriAzpoP6se-Uv9ELlZUPY7J3x8pf-1_eJ1fSJ_3mWYgtGg4frMGAPlK_QyDNADZXwA-nTbFJblwpfb5rdLdC4Wo07VCftLZdCUQ2y5ArQHZOt2dvv9bcwMNcnTtZNIR-W-8IvXoTR6-GLJt1VKt_4eKQyM4orgtL1OIC6XIht62TZV8lFKAIze-VH50OeMZACzch_FZjlveQ6Y0-BqCIHcl1y_3fGSr490xNu5-6Hc7g5ZKORpyfGYTy_yNl260nw-abfle6OgwIvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39aa059d6.mp4?token=VI9mnR0NS8sJKTSplsWqhIw1y5sjBkHsFOz_WZBMj7lB_GxSi17qBEE0p0b_uq-fmCTcdGjblQioFhb0yXmFzYJ7-SBPrUr3mkaWhqnNHYi7ftL0-3UyW5cHnAkXvm6cZ1ZLoLNOAM2BdriX3u_GAbqnRcWKUFxyRuMee-E7Ip_6Q2BRpwAwvmObcqAMCTm5HRCEyQ-NnK86k5m5rFilmpsyTIb8tu4rTlKDez1jJ7zUQVrWzXothL1o3aLhUKkupF6pZktsT0yI7XWnDSsS2IdVPN57ABeNEskUplBK51X-ZpKLeCNSyDgCZG6J4hb-qrSwzcqPGWIOs4Z-jhsecV0sg-Q1qt71I03kLoP6maEqtrkfL0suEEoh4CpxOZ6nCN27_2jCrrmKl2VMm7LrojapB9qwtriAzpoP6se-Uv9ELlZUPY7J3x8pf-1_eJ1fSJ_3mWYgtGg4frMGAPlK_QyDNADZXwA-nTbFJblwpfb5rdLdC4Wo07VCftLZdCUQ2y5ArQHZOt2dvv9bcwMNcnTtZNIR-W-8IvXoTR6-GLJt1VKt_4eKQyM4orgtL1OIC6XIht62TZV8lFKAIze-VH50OeMZACzch_FZjlveQ6Y0-BqCIHcl1y_3fGSr490xNu5-6Hc7g5ZKORpyfGYTy_yNl260nw-abfle6OgwIvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
💥
نظرات فوق‌العاده هوادار معروف پرسپولیس نسبت به بازیکنان تیم‌ملی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/92279" target="_blank">📅 11:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92278">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki6sEEDwS4I47DkSxtHVytUBJR6h_fAPlFSeo802y6tqeINm4gHX5Ka_oFyNdAChvq35vtg-IXk_AAl0plLJwkC9Tldj-W-tdHtrDghczqtMM506cQnK--339qQ9DuVv274eYlGi4r0f_8eG8khkO_cdRqsKI1xk7LxV-2aKu_WbKAq0STXihAFa7z_FvZf1iaJ-J75ITUOzpfSC0owJgyMHFKeG3ArUvzv5wca2WO8YVm5NcSd0xVipRuP5-9yj73zo2ob958l8MmmPjOaz_STNSDDITaWEhLzy1kIW9PFMyyHH4inLDWKQxMEIyYUYiJE5sNb__mtz79AWjExnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
از هواداران خوب و دوست داشتنی کره ببینیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/92278" target="_blank">📅 11:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbpCIzdYwBJQawhKbE9wYoG81STnGK1QhJePaFxWCckyknPOHohDiWZLuN1MiYnF7xXHMUhm-xUVQAZm6HFljd1VL2wkNzoxFXrSwRbhmCMewao22Z6TfaZAA0iqH1K0dFio5FcaZ9pGv6tkRDuOY1E6MKwAoNztenYM9VM6uv53tw7tZmlJ7ejXjHboV_ujFEoutHn0bT588hT0k-1QLOcj57NubpP6tl-CNq4DCBg1KlK5NXta0JUwzqKfCoO7KYG_CnoEQpAZwRQX5lXfcB09_s664gTV2twmdrpbfKwcbo5-7hnkqhNx733_FQ_Gy6NTxuRlPLXliNroIxArFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئال مادرید موفق شد قرارداد برناردو سیلوا رو فقط در ۳۶ ساعت نهایی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/92277" target="_blank">📅 11:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92276">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvCb4udLqb-nsKGDBWTh_g42dYla7azJygKQ-YjSukXVGkQhHUk2NQdnwLNCXiA0RROsTyR6VeMuwDIvrWYix0RI_rz4wE4Wy_aL-U2a9wn8noyLjExXFNvbIrBdsS1_2XroNiW0ckvwbMAIe6Dwv45H9zEhr-Or8g73hqaKHgdvsyBRtJEvakohNCmiiqexK3UcegNyjfoS2L4s-4bf9Y-oa8NRMwm_DYjTFZreSyrltkjWNBp6tRNQtyfLWb_1C37NrFQE_FO85uu_QE28mmgBLRtvVc4p64vsRFGG3NyiCc-m-vJ3JagBz1SC_vPF_0iZohnLWN2kxkgPDTdJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزبان دوست داشتنی
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/92276" target="_blank">📅 11:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">▶️
یه‌یارو بیکاری بلند شده تمام اسکناس‌های کشورای مختلف دنیا رو جمع کرده و باهاش ویدیو ساخته. هرچند احتمالا پاره شده ولی کارش دیدنیه
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/92275" target="_blank">📅 11:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92274">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
❌
🏆
🇩🇪
هوادار ۸۰ ساله کشور آلمان شب‌گذشته در حین مراسم افتتاحیه جام‌جهانی دچار سکته قلبی شد و درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/92274" target="_blank">📅 10:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-qWJc9D3Gz4F2CcXqvWIdEnFqF_FNYaiYWACwgdLDSJi9XSd_5jkV3a-SiDNL2BiMkUoCeU7EKG2XhylUExgXmlQe086XP99YRwt5qV-WtLCNAZqDbht_la9c5TzVSir5ekq9CiZ-Wr975OJeZfBy27SdiSzZCJF7TzrATvp0ImQW11y4BBlRqIrSGJzDLFYskGUTjmzeU_-X4-zWH6HJ4rOQH7ODvJMnn0xvrGzf0ccQJmdHHts-d-vs2Th5cVEJIqzDPD9odhoZHnZiznIFoc_AKJVnrtYjqSv6YQkZtI4jpZE9r_v4zWOE6SBVGg2c292kBMG0_cRIgM9MD7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
ژست‌نیوکاسل در مراسم‌ فتوشات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/92273" target="_blank">📅 10:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92272">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAT2t_-azDXrPuBEd0qe-UUZVGzMTdicsv6mcQQJMfTpAVlb6k0c15GzlksTxtf54Vi2Zt4dBIIdP0vj1WCt3oRjEFlVzZNEXxOzwLhV0cPRGKB2GfkDc0c4jfwJu-CwaUe6fbZyiR1rYhiUbFb1Btt99_NSO0j_eUd6MXqoRzZfbSaVUfujOZ8hT_415Erc49DeE5ltzGdqwnCpYlJ-sezOuEx5541rkq0HLgRbr-cNKBprEHu3t2DIdADc7S0TfT7yNBtbS23b95HK0kzU2OHemvZG3F-IiN5I-bJcUV87Ge3D4RwEIB-wPGQ-5IsdT9OMhgWJEU_ulLpIkDdQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنت ماکسیمین که یه زمانی وینگر تاپی بود و حتی میتونست تو تیمای بهتر بازی کنه با انتخاب اشتباه و رفتن به عربستان افت شدیدی کرد و حالا با اعلام رومانو به شارلوت آمریکا پیوست
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/92272" target="_blank">📅 10:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92271">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUYmcrXe5_RPE9eud5amu4Om2SW-0oJbiuKJ3MZK2iTgksGu_zj9g06kRBrDE61D10NEWk-KudD0Xs17o0_8fihN6BMnX_yr055yNahDechNqmAVnshoSvSt0wHPyxRkSdzOpo-unZilAc3Cu7LSQ7gheZz3EPvcGWhc12D3Sd8ZdHkKkAWst65ViIgK2awr6EXB8Su9bybnS002oUoEzz198m_WIymegYrOG5_r5gpaBKJdPrdcjMzLkj9_9yUUiARt9U04yl-fpwjtLB3zW6TbUWtKo1USunvOBRUM6F-VBGtNsOve6sOAA6CRpzo4Q0ZQJJxG5e94h9EfP8pf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
دی مارزیو:
🇮🇹
یان اوبلاک گزینه جایگزین یوونتوس در صورت شکست معامله امیلیانو مارتینز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/92271" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663a1bd7f6.mp4?token=tpUifBU-j9EtECTvQNCBCmmG62H9zXZfFyrSBgB0L1OCPLoU3l2cfI1IrJNQzjWfRM7IIhJ7aT4XdKUfmaDqQs5Xh9y5NzYiNNYx9_5ctw3WpKCSuDDzV6r-KvI81wnWz4ex29a2Zghzvq4W1Fy9veRiQujXtude4bG7uU2derHZmVfSDRYbPUZwkXvGIEEjIWFE67LvVJEY7xmj3xFlF3zSvrdu_3yysrIB2Q3AlUqXO0vBh4_9kehgpNcz1TaV5WNHMF7_NA9V2yDj0kSjtzx2_8ei-zJ-ThL9aVmabogi4oAR5gsXjZZrPh_lAWOA7Y3w7LmxUb9-vIh0sr6Duw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663a1bd7f6.mp4?token=tpUifBU-j9EtECTvQNCBCmmG62H9zXZfFyrSBgB0L1OCPLoU3l2cfI1IrJNQzjWfRM7IIhJ7aT4XdKUfmaDqQs5Xh9y5NzYiNNYx9_5ctw3WpKCSuDDzV6r-KvI81wnWz4ex29a2Zghzvq4W1Fy9veRiQujXtude4bG7uU2derHZmVfSDRYbPUZwkXvGIEEjIWFE67LvVJEY7xmj3xFlF3zSvrdu_3yysrIB2Q3AlUqXO0vBh4_9kehgpNcz1TaV5WNHMF7_NA9V2yDj0kSjtzx2_8ei-zJ-ThL9aVmabogi4oAR5gsXjZZrPh_lAWOA7Y3w7LmxUb9-vIh0sr6Duw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنده‌خدا عادل فردوسی‌پور پشماش از خوشگلی دیبالا دیشب ریخته بود
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/92270" target="_blank">📅 10:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba32797a6d.mp4?token=rQpO4OCZtZvOZ6P-a-66bE9ZODrgA2YG7qR0rT-I0PaWfD14ZQXVmTUS5W-llGSj2m_vx2hC0ukilKJxn8nPN7-teUp8qku0KsXDyUb29HD1p6zvjs7QqDxJ97A_4T0jva--YXFQ7gUWfd4pnhi3DTCn-5bwMpk4Nw6nZUjDKFXTNXBFtFuGcN4Yqchh16mze6t1dOXoy4OrsZ6z8qCJo7AfV6yBLCoqZAghle2Bs3gFXsqPNyw5FqJcKErx-Hr0ABpxXrnCWIQfkksFgzcro--TBox3b-dhdZ_uGndEijCIPr7TJRaXck69fikULssmCIL2-eloLFzbdQPpZsK_G6BUFznVxIxwYgrGTtLrhjslWqm7f3oHanfT3IKn_JVkJIk5_s8_N8WZjfgxXd96aj7HT9LvKVabUb99CTpNUU4QQmFxyfj-Myq59c8BVy04APITS1pTE9p4pKw00w30gLHOu48sy8WfsmTLcWnGZSJ8Xfz8iA66GOfoYeiHu1hyuFXqTLk20-LCzka0q0Blfiqn9WrCMBCBPFgOuIlnznGBOK1N58IMeD_1lxXID9Xn6o2bXr_Sg3-1iH7wHdxFu1VCNBQGQybqsrVb6rhHnmEm9fgx7TD89cKIbr62WLD711Kd7LbyObt06GPPWmugIIiByiN0Ce7UhQmr0qsr-yM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba32797a6d.mp4?token=rQpO4OCZtZvOZ6P-a-66bE9ZODrgA2YG7qR0rT-I0PaWfD14ZQXVmTUS5W-llGSj2m_vx2hC0ukilKJxn8nPN7-teUp8qku0KsXDyUb29HD1p6zvjs7QqDxJ97A_4T0jva--YXFQ7gUWfd4pnhi3DTCn-5bwMpk4Nw6nZUjDKFXTNXBFtFuGcN4Yqchh16mze6t1dOXoy4OrsZ6z8qCJo7AfV6yBLCoqZAghle2Bs3gFXsqPNyw5FqJcKErx-Hr0ABpxXrnCWIQfkksFgzcro--TBox3b-dhdZ_uGndEijCIPr7TJRaXck69fikULssmCIL2-eloLFzbdQPpZsK_G6BUFznVxIxwYgrGTtLrhjslWqm7f3oHanfT3IKn_JVkJIk5_s8_N8WZjfgxXd96aj7HT9LvKVabUb99CTpNUU4QQmFxyfj-Myq59c8BVy04APITS1pTE9p4pKw00w30gLHOu48sy8WfsmTLcWnGZSJ8Xfz8iA66GOfoYeiHu1hyuFXqTLk20-LCzka0q0Blfiqn9WrCMBCBPFgOuIlnznGBOK1N58IMeD_1lxXID9Xn6o2bXr_Sg3-1iH7wHdxFu1VCNBQGQybqsrVb6rhHnmEm9fgx7TD89cKIbr62WLD711Kd7LbyObt06GPPWmugIIiByiN0Ce7UhQmr0qsr-yM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
🇧🇷
از هواداران آبادانی تیم‌ملی برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/92269" target="_blank">📅 10:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92268">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947a269dae.mp4?token=rxPsCAjG9QP2nlNuJYbzFr9GvhnZMJMqiN9mx69CHHTm8qrEhQo50lsybbe4PWZBF9t6rtR_EtnXi-On7Vz4Y04-fbUBrxCRzToQg-OEgzeODHwVsqyBcuN4eu5AxZ7YIjBaB7o4__TJcb5Z87KxwhY8X1I03d0WIAAQvw0pnndqAIRqCoIpRQSqSgmIHbSFrDmOiXon0XfgaqNrvsTmP37EkebZDPVOeHMhrCf7u3pw0ZkBamj_CeA5icClWxC6NF-ja-pNdkGM7IRgcYouyyS7hp7uTYhnM8SncDjydVPFmEaahD0HoaHEjRnLT5nNaeWHT06QB10I0AJ1Ulyeqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947a269dae.mp4?token=rxPsCAjG9QP2nlNuJYbzFr9GvhnZMJMqiN9mx69CHHTm8qrEhQo50lsybbe4PWZBF9t6rtR_EtnXi-On7Vz4Y04-fbUBrxCRzToQg-OEgzeODHwVsqyBcuN4eu5AxZ7YIjBaB7o4__TJcb5Z87KxwhY8X1I03d0WIAAQvw0pnndqAIRqCoIpRQSqSgmIHbSFrDmOiXon0XfgaqNrvsTmP37EkebZDPVOeHMhrCf7u3pw0ZkBamj_CeA5icClWxC6NF-ja-pNdkGM7IRgcYouyyS7hp7uTYhnM8SncDjydVPFmEaahD0HoaHEjRnLT5nNaeWHT06QB10I0AJ1Ulyeqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور: مسی یا مارادونا؟
💭
پائولو دیبالا: چون مسی رو دیدم میگم مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/92268" target="_blank">📅 09:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92267">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723b6b4949.mp4?token=p7mnF-mCX-PVB05yhYZy37CbUmq1w8_HS6wWUmCrdaM8I9az4VYKS9qr3ODL_MXoUrWb810Evc1ioxjoE8XYDcc1xpT8k0nyWLQGRuzMGfFJhDWgU-nitBOUYH3B-uu9boG1bn2vtIpIfWu8cB3VgqrCFVL2Pqadh0fiFAijXln3R6Fdi-nqeH67ixwFwOWZbhzt4HNhDdOiSOWBO1JKvaiSeDl1ygQ6yMUVuheuo6Gxgm2B2RKQn95wfiDwxLxougtmA2Asg6tp8Nd-MDbZ8ODuvg8uExL7DZEml1797DLNvGGTjGQ9_nk9ByjGUdCp8niA4wRPT7VKLvoeT9s8fYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723b6b4949.mp4?token=p7mnF-mCX-PVB05yhYZy37CbUmq1w8_HS6wWUmCrdaM8I9az4VYKS9qr3ODL_MXoUrWb810Evc1ioxjoE8XYDcc1xpT8k0nyWLQGRuzMGfFJhDWgU-nitBOUYH3B-uu9boG1bn2vtIpIfWu8cB3VgqrCFVL2Pqadh0fiFAijXln3R6Fdi-nqeH67ixwFwOWZbhzt4HNhDdOiSOWBO1JKvaiSeDl1ygQ6yMUVuheuo6Gxgm2B2RKQn95wfiDwxLxougtmA2Asg6tp8Nd-MDbZ8ODuvg8uExL7DZEml1797DLNvGGTjGQ9_nk9ByjGUdCp8niA4wRPT7VKLvoeT9s8fYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
پیرترین تیم‌ملی تاریخ جمهوری اسلامی در مسابقات جام‌جهانی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/92267" target="_blank">📅 09:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92266">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1977ba4486.mp4?token=X6Z8tv2T7BKPyZ0DDhSPBxj528CFbw83Y3sdoT2CHSlaJ53O-ji2b4IwUp8SbEkPZ3iKKrQ_3wX3u-fWs0g6JsFkpMe5Nyb6IdPiK2m9ikXXjI74GuEoV_Q2CPnfPnPVTZkG4OczSaOuMpzDthVD6wLKNhBku-_zNxKJ8213vQMOYPdazsY-OBaVlWEyt1AFizrPqZECReAQopnS2XIOVC_CqPGjZ307v6pZwKMndUH536kRgc7MnKTKVpdVTtah68_PW1pLfSNebVL5mTXZtOVT9hid_PPc6m5McFMEnPhzvRcQZHe4JjsM9OOCSegOUXzNelS4Yx23JhGJKe9YKJg__p5q9gLy7X_ZxWJGWt2hsFS7i3N6EdHGjbNOqeruHHzUW4p2pRYm1xaMkYR4coUsEOX5d4sse9xJjL_iMqdzoozMzC6CAxfMbsk2SaT_kaJJAadrIFPUtSS3TWHzjCHGAITcjAk1PVlgVaCpEoYQOLDI-3jnWOz4RXbr25Z2WB6Z5WybTG2D2EViza0U7QCVg4FR5XhLH-xZ-ct-cc-_oG5byqzR_9R7vkvzYeIazq1AkW811jwyd7y-_unatKL02ItaVtFejEYTYqg7b0ZtozEM4bAgsr2vUZqG4OyKAo4BGstniIcv0qqCK4LcQiJsjA6Xn2-wpla3lJ6th_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1977ba4486.mp4?token=X6Z8tv2T7BKPyZ0DDhSPBxj528CFbw83Y3sdoT2CHSlaJ53O-ji2b4IwUp8SbEkPZ3iKKrQ_3wX3u-fWs0g6JsFkpMe5Nyb6IdPiK2m9ikXXjI74GuEoV_Q2CPnfPnPVTZkG4OczSaOuMpzDthVD6wLKNhBku-_zNxKJ8213vQMOYPdazsY-OBaVlWEyt1AFizrPqZECReAQopnS2XIOVC_CqPGjZ307v6pZwKMndUH536kRgc7MnKTKVpdVTtah68_PW1pLfSNebVL5mTXZtOVT9hid_PPc6m5McFMEnPhzvRcQZHe4JjsM9OOCSegOUXzNelS4Yx23JhGJKe9YKJg__p5q9gLy7X_ZxWJGWt2hsFS7i3N6EdHGjbNOqeruHHzUW4p2pRYm1xaMkYR4coUsEOX5d4sse9xJjL_iMqdzoozMzC6CAxfMbsk2SaT_kaJJAadrIFPUtSS3TWHzjCHGAITcjAk1PVlgVaCpEoYQOLDI-3jnWOz4RXbr25Z2WB6Z5WybTG2D2EViza0U7QCVg4FR5XhLH-xZ-ct-cc-_oG5byqzR_9R7vkvzYeIazq1AkW811jwyd7y-_unatKL02ItaVtFejEYTYqg7b0ZtozEM4bAgsr2vUZqG4OyKAo4BGstniIcv0qqCK4LcQiJsjA6Xn2-wpla3lJ6th_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیو‌ دیدنی از تمامی‌توپ‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/92266" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92265">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIG4CrTiYltlKzlVsuTM6zuikL25FLDHSSs0CNxj4BDRAib3DCulwNevvRJIHl-OJJczKnE3SAQ3u9lrBH1pjyRW8zoICtME4hwOOHP0rIXB1vIZ5_r8zd-dmeSPh8vdBzIajKWSuPKhbINsF1W8yict71hk7X-79H0ybqP-kfBpavBC-eXNrSlK3pnZ_oWBz-5uAzUp7rYMBGC9dDEBzCq0yzfSl185jnGJMDEjXiAm32bj6ecRNSqu_V655YFIicXRqvt54nLpKIQK9D666COI18z8BoGM2qqjUbE3CF4mfgZCvzQTfhyYjE9AcGU8iE3OQFi6VQECCWK7YpRDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🇨🇿
44985 نفر از نزدیک بازی کره و چک رو تماشا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/92265" target="_blank">📅 07:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92264">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇰🇷
کره جنوبی به 8 امین برد تاریخ خودش تو جام جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/92264" target="_blank">📅 07:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92263">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzWvk8MLsRobVtTtg2dvWDRwDJieFHasD1_a9N1iteQfjOhJDW8g8MAI32vniAWzT6EyYbarAjFDUu3NgHy1zTZt14fO_KppwytsGre6ol1Gu9o1PeSKqZAXHdy_gP4n3sdASAC_HEu_MeQJ_OHsKukSTovnCQMN9pNcVNRT7QShPCPSVwWRtUvSUqjIxonZ8g1p7IfHjzfyTYSLu57hvgeKJYokV8jOVFqvtMjTb89rUU6LqQHBPdQ8JLMEN0Sc7TOcmJmR-0a5TUMbxJ-nEdf_BGhqOaWm9mUCIYTej2idkkhJAxRpqljaUbdeleEkLAdks5l_SWSxYa-sZ1ea-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
عملکرد فوق‌العاده هوانگ ستاره کره در مقابل جمهوری چک:
93 بار لمس توپ
1 گل
1پاس گل
2 دریبل موفق
2نبرد هوایی موفق
کسب نمره 8.9‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/92263" target="_blank">📅 07:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92262">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gDl0yTzPLMYF9_PbhTVof8lafshM4kOVvsdJfQEHcri3R--I47n0AQyR4VO357I3Hnm4-XJo_BIukFVlG3cDCzZDtt_8uK9Q0bLPnMOXUN4YpAABrL6bIDeZyufdcv1v9piMlJRCMWC380PIkpnWNSl8WzSFXhPAVyL39lruBlEEtMrqMk1cG1d9pQGcgL7dvsZvV429LyjWDb9_rTUy3cnPqN1Clt2Vdx01qqUUKSg9pEsYtIOw2Z5qNxn5rpVfkogzLBk9kB7R7DUwlpNQjb4H0l5J49YyW6zT2rCun8stKFsAuYGnj7Z1uH4rWOMUn5kh0llyx8Diui2VG0p9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
کره جنوبی به 8 امین برد تاریخ خودش تو جام جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/92262" target="_blank">📅 07:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92261">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XViNpEDfkX6c-A3wmVpRrsIjWQZFH_ZGUc0Vtqb5pEzh6vKOfkw0uSRXAlvNihWHu6M7gxFvjoPeDqh0OZYaz-j9bOmgEE_UIMNG4J-M1bxZQ3wtfKgNcNkBoJn1GtIZbsFkx6KxV9uRbmDZAe3reG9J4ie18KShtgiX1FY6scMLRWR3EsI48p4ipwaeeXmgpRYYtu3ok6EDcHCNl8FMEN52RqmLnYbZCE1Q8pPbJO_oPW_TTbYAPVhEh4TYNG2zaruIKOwPIZAr-vcD3Llir-qLR28xDS3la7fX2uvEXHIWM6DWQqUuqlTpKZy-65xhnsuPiH8Smd6sikGLm1cAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه A پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/92261" target="_blank">📅 07:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDUElVT61D82-H_dhDuCnEgeKR1Six-sO2fCzH0bbkVR701toChh0YIXwsvDTM3vRrlH142fjxC7IHnP9dN0BHPbqwez1wV11AEbpWZq3V5s33H6waFX-NQYnZDfeUECqz4Nlxqg2F-GbNfooE7fx5nkAy6n-7dnJZOSc4TmZjXfdngpdumGlpFnTkfyQcyTaXkoPLU4YsW3soMzbov9kEXlmnetgbyBb5r7kic4vVHHZYgTwemzG3ghJCEaUEWX-USgp9u1yRa2bAREMwVUSyPDBckWL0s6LwuZz0N51aKz0jp6NN6hVWE3xFLqoaK15vf9lEmBhdXfb8CEk--4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان بازی | اولین کامبک جام رقم خورد
🇰🇷
کره‌جنوبی 2 -
🇨🇿
چک 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/92260" target="_blank">📅 07:27 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
