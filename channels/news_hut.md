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
<img src="https://cdn4.telesco.pe/file/QR1ePsiGx-a3pmKpiBAZi5GXhn55iS2k6AzlIscQ0VJDiQb2HnzNbIy58kmgMKbhI1yLumAOisYkIUNJGGylo6lB-4lOC1V-YJ_8k3rDr5crH4q1ZSfaYJEtEtzILLeNGBHD9794uPZBZKE3_1YBaiVeU6PecCpmEuS4gYEbv0_XWbewkNx4WpjL1S9QQn8SgjI2V2xsjfRMWqqH6HbDMKrJvt-Ld17QT5VkrI0K3V1ep7OkTLrFC4w_GWu_Z74-k62-BsJZI_f8qTXhNcYfvvCF71cWG4mMN1IHVciTjhWYmKIqb8wV_1nYgsAZS2Wqsiyi_rO6_CsD3xrTHsfsKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 192K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 22:46:24</div>
<hr>

<div class="tg-post" id="msg-67553">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=SCqoHwPcV8yItPRHiF7Rp3e992YBog6QhI43H34r7aF5GTH_3J542HpBR-EF-pViflZIGM1-KTSrhC-zeJ15WBpTh5COllteUTnFk-pigjm0ztFB8uiZ6mxEl6sMrZxGoNAnCPAzDzTH44mBZZJNHHifLnbKtCiphRQxpKlpVgWLtnjeMjmigy8l7Xo2oPvCTzXV7pmNVF9o1HZjEJAcMrUGr6PjDJVM23UzNTJc2g3nLq1VRllwOC2BzB3GXoMN114Dc3o4D7kvnkaB8W69W4X6qRWW6NBHqw_Jx2xQx4EzzsynUytNcTSPcnt95PSaTdvVglFYNr1xlACd5cHBBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=SCqoHwPcV8yItPRHiF7Rp3e992YBog6QhI43H34r7aF5GTH_3J542HpBR-EF-pViflZIGM1-KTSrhC-zeJ15WBpTh5COllteUTnFk-pigjm0ztFB8uiZ6mxEl6sMrZxGoNAnCPAzDzTH44mBZZJNHHifLnbKtCiphRQxpKlpVgWLtnjeMjmigy8l7Xo2oPvCTzXV7pmNVF9o1HZjEJAcMrUGr6PjDJVM23UzNTJc2g3nLq1VRllwOC2BzB3GXoMN114Dc3o4D7kvnkaB8W69W4X6qRWW6NBHqw_Jx2xQx4EzzsynUytNcTSPcnt95PSaTdvVglFYNr1xlACd5cHBBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرنگونی پهپاد MQ-9 آمریکا توسط جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/news_hut/67553" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67552">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697775e593.mp4?token=FId8yRiQQPUrPG4uIuAFaFDqvShmnYrdiODv8HSvjC-vy2oudK3fT7sd_ph1KKfGPjVSlCx9LRAOp9wk0EQag1UPLLgAe2YQ0tqcgzMvhQZpdxX_wMw6DroiozFhTfdCbcIIpacxC_jBbyFA9DwPaz8qduN_Oo4GACxCpWJGqzpFK4j6r2-oNZm_YPzBOM3EPKtSBip-Ef4BfUOHlEgf_hhzfTP_J0dtfB_0q8aafHi5ibzO8_nh9k3g0dgaFPBuhAC_N-Gi5y0zGYukeoIvLEA8N89p2f8g0rAoHzxeDCK84f3LXqqgOTPOyBgfw4BB6XbAMGGSxJuSj4okqAgZiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697775e593.mp4?token=FId8yRiQQPUrPG4uIuAFaFDqvShmnYrdiODv8HSvjC-vy2oudK3fT7sd_ph1KKfGPjVSlCx9LRAOp9wk0EQag1UPLLgAe2YQ0tqcgzMvhQZpdxX_wMw6DroiozFhTfdCbcIIpacxC_jBbyFA9DwPaz8qduN_Oo4GACxCpWJGqzpFK4j6r2-oNZm_YPzBOM3EPKtSBip-Ef4BfUOHlEgf_hhzfTP_J0dtfB_0q8aafHi5ibzO8_nh9k3g0dgaFPBuhAC_N-Gi5y0zGYukeoIvLEA8N89p2f8g0rAoHzxeDCK84f3LXqqgOTPOyBgfw4BB6XbAMGGSxJuSj4okqAgZiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پس از پایان اجلاس ناتو، ترکیه را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/news_hut/67552" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67551">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd068</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/news_hut/67551" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67550">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FN5yFpzoZJKm-kptOyTpcxSgxgeQF5M-4s_17G-NQgRVkQVEgVway1RFMvG_Sj6R8S85oCprAywv88bMYblnLMal6vhwcHx3GQKmRl6bxYq5fv5FQMK9K7eTsxwQ10ZW_V9nVE_VoXPqMCCScS_ubeIDP8JNU70aPwaWJzgHH4dElr2DYpzu8H7_TXYdBKTHYNXcP2M8VseH-l6B8PqbCGMW1GJYGCnOOMOp7zXogOTj4UYn9s8mht4bzldX0PZuQHdJw3fZUke6toWIzYCrpIzs-xsgiNXZ2wg9qzVK-1USVgyF_po6m5ISUo2hQOx_6Ox91ifS5I8_nRUlMsysZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
عراقچی:
صحبت کردن با لحنی تحقیرآمیز با ملت بزرگ و شجاع ایران، از عظمت آن نمی‌کاهد.
ایرانیان به خاطر متانت، فرهنگ و ارزش‌های اخلاقی قوی خود شناخته شده‌اند. ما به بی ادبی با بی ادبی پاسخ نمی‌دهیم، بلکه با عمل: با شجاعت و با از خودگذشتگی فراوان.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67550" target="_blank">📅 21:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67549">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
گزارشگر: ماه گذشته، شما گفتید که رهبران ایران بسیار عاقل هستند. حالا شما می‌گویید که آن‌ها افراد بیمار هستند. چه تغییری رخ داده است؟ ترامپ: من آن‌ها را بهتر شناختم. آن‌ها بسیار عاقل‌تر از سطح اول و دوم هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67549" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67548">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/412c846bfe.mp4?token=tGFL9ixvGV6MXX60CWsR3WoytAlssudAj7S2wSEEw2R83iHDj6EAkvWo-kUVU41nr6yyqT_-57KbQ6DcAb0AGsXGz4ohUIrV9CC7cDEEBmzKw-TyniWJSfQ7Eqgu9aAoyZBlW0BuGS2mqrZvftGnZ3UeM317Fqnyy4spOtA9zIrcCgEZ8mPxBGxGXGzKSrU82rUqfQwqUf63QQppO8O-bNjP5OTydnBTIiBf4mmsLMzXijG0QqgaHupQYEhHDYD35z2a4pRZgqe6SqENSxtrqEblDWy1JnrBV4Lpwh9999ulScg-Xt1bEGYZ2oQurnUyag7LHRsj5SDCyIb4c5uT-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/412c846bfe.mp4?token=tGFL9ixvGV6MXX60CWsR3WoytAlssudAj7S2wSEEw2R83iHDj6EAkvWo-kUVU41nr6yyqT_-57KbQ6DcAb0AGsXGz4ohUIrV9CC7cDEEBmzKw-TyniWJSfQ7Eqgu9aAoyZBlW0BuGS2mqrZvftGnZ3UeM317Fqnyy4spOtA9zIrcCgEZ8mPxBGxGXGzKSrU82rUqfQwqUf63QQppO8O-bNjP5OTydnBTIiBf4mmsLMzXijG0QqgaHupQYEhHDYD35z2a4pRZgqe6SqENSxtrqEblDWy1JnrBV4Lpwh9999ulScg-Xt1bEGYZ2oQurnUyag7LHRsj5SDCyIb4c5uT-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ خطاب به ممدباقر درباره اورانیوم:
ما دوربین‌هایی داریم، که بخشی از نیروی فضایی ما هستند، که می‌توانند نشان شناسایی فردی که به یک سایت خاص می‌رود را بخوانند. محمد، چیزی آنجا وجود دارد که با بیل و کلنگ در حال کار هستند.
بیل و کلنگ به شما کمک نمی‌کنند. بزرگترین ماشین‌آلات دنیا هم به شما کمک نمی‌کنند. این موضوع بسیار، بسیار عمیق‌تر است.
اما ما این موضوع را زیر نظر داریم و اگر کسی به آنجا برود، منفجر خواهد شد. بنابراین، هیچ‌کس به آنجا نزدیک نخواهد شد. در نهایت، ما آن را تصاحب خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67548" target="_blank">📅 20:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67547">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8dc7e8bc.mp4?token=XVwssvTXM4Rd2JeeHGhz4u1lDt3joDuoPqmMtvI7-GtC--L-zG0R6aohkfHenGczB_wedJLQZO6N8Vb17PFqXLox0ZiFx3NxPbxvlEO_Qn6NVwzNhMk2nQdPPhg8IOqyJWpZJV4nrS0suDuZ3T2S1blfiQROtpCNpmI5Vyfhx_8dkMHWTEaMdji7ZOrBDwyckOIqZTQXdvn2pc56MUiGSD1BjjiiV89N3XtY3NqlxhbzC8Ba3AGtvToTqtzT93z5ZxNqEUN3ys9rEYvYDvgFjNpuokj4ydMyM-quE2s3_5IkX0JDyUvxXH3M7JwX6-1gsWiq2te-JdSaOUJrvIWaWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8dc7e8bc.mp4?token=XVwssvTXM4Rd2JeeHGhz4u1lDt3joDuoPqmMtvI7-GtC--L-zG0R6aohkfHenGczB_wedJLQZO6N8Vb17PFqXLox0ZiFx3NxPbxvlEO_Qn6NVwzNhMk2nQdPPhg8IOqyJWpZJV4nrS0suDuZ3T2S1blfiQROtpCNpmI5Vyfhx_8dkMHWTEaMdji7ZOrBDwyckOIqZTQXdvn2pc56MUiGSD1BjjiiV89N3XtY3NqlxhbzC8Ba3AGtvToTqtzT93z5ZxNqEUN3ys9rEYvYDvgFjNpuokj4ydMyM-quE2s3_5IkX0JDyUvxXH3M7JwX6-1gsWiq2te-JdSaOUJrvIWaWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
مطمئن نیستم که بخواهم با آنها به توافقی برسم.
ما می‌توانیم بازی‌ها را انجام دهیم، اما مطمئن نیستم که بخواهم به توافقی برسم.
فقط بیایید این کار را به پایان برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67547" target="_blank">📅 20:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67546">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d009a331.mp4?token=vxjcvb6W2PABM4EqQpqTQDBKxSXELA0prniydxl9fUEYdVlzeoghLJpqQ0JE6828AgEUbi6kbC-TC32lZcbA5khSmZlRGfugscD6NhHyEbpwZrp4sAuH6UVASant0sLZm6r5c2l4cgmGkajQFSdnXH3024sW1e00uja2vNoG8jN1bb6LlYws4dEwo7J2n5oJoPxn-XAvoB7OMYxP0Q-xrEKY77Z9JXcQakuCqN57rTX4L9wQCl2Bso4ckkDX1pEQtqk01Fe-QmWyAsXuv0tJ6Im7qxReSkjtkt6tJWEChmaUiCe5BDFfLa4MvoaGfUbk4fcwyM3y4ZHWnEixM7dszw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d009a331.mp4?token=vxjcvb6W2PABM4EqQpqTQDBKxSXELA0prniydxl9fUEYdVlzeoghLJpqQ0JE6828AgEUbi6kbC-TC32lZcbA5khSmZlRGfugscD6NhHyEbpwZrp4sAuH6UVASant0sLZm6r5c2l4cgmGkajQFSdnXH3024sW1e00uja2vNoG8jN1bb6LlYws4dEwo7J2n5oJoPxn-XAvoB7OMYxP0Q-xrEKY77Z9JXcQakuCqN57rTX4L9wQCl2Bso4ckkDX1pEQtqk01Fe-QmWyAsXuv0tJ6Im7qxReSkjtkt6tJWEChmaUiCe5BDFfLa4MvoaGfUbk4fcwyM3y4ZHWnEixM7dszw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
املاکی درباره ایران:
به نظر من، جنگ با ایران دوباره آغاز نخواهد شد. وقتی آنها حمله می‌کنند، ما ۱۰ برابر قوی‌تر پاسخ می‌دهیم.
شاید امشب به آنها حمله کنیم.
هر اتفاقی که قرار است بیفتد، خیلی سریع رخ خواهد داد.
ما به دنبال یک راه حل بلندمدت نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67546" target="_blank">📅 20:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67545">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
من می‌خواهم این موضوع را در مورد ایران به پایان برسانم و با رهبران فعلی بازی نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67545" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67544">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966c88b1c6.mp4?token=ZkOOci7GFdWKbbbIdTEc99KQVOOuHuVDF4dieWL2mgyfiKZoDV4SdEP_VwU74lg1a3b3HZJybf-pegLI-mC_0jwpfgKTufpJRfj73Si7gJu4Z4EI7088DSxSprXdAoNed5OJBnYYJUulqLXKzRPAf1WCCj8swA3OAFGoF7N1yFfL6DpPYMCMquIoEIdNfMqOtNTdl3g-ogd5YeZbsxQQo6KeeQ7ukC0e7ea1CFwe1HuvskIqnHJNNHqmf1H13-P_f4TjjO-mQaDulOKCCsLvhufpgnhJxgPePye6vs3VjZ6zRsY8EGyUgZuZORxXzw13bNuXAps04P7fefnA8TOCgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966c88b1c6.mp4?token=ZkOOci7GFdWKbbbIdTEc99KQVOOuHuVDF4dieWL2mgyfiKZoDV4SdEP_VwU74lg1a3b3HZJybf-pegLI-mC_0jwpfgKTufpJRfj73Si7gJu4Z4EI7088DSxSprXdAoNed5OJBnYYJUulqLXKzRPAf1WCCj8swA3OAFGoF7N1yFfL6DpPYMCMquIoEIdNfMqOtNTdl3g-ogd5YeZbsxQQo6KeeQ7ukC0e7ea1CFwe1HuvskIqnHJNNHqmf1H13-P_f4TjjO-mQaDulOKCCsLvhufpgnhJxgPePye6vs3VjZ6zRsY8EGyUgZuZORxXzw13bNuXAps04P7fefnA8TOCgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
هر اتفاقی که قرار است بیفتد، به سرعت رخ خواهد داد.
ما به دنبال راهکارهای بلندمدت نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67544" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67543">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce02ad2ec.mp4?token=sqkdtPTufZacBFAriQNqLC420DBg9Nl17pcxZFSmKD9V8VEXLYHybbQVA8gYNGFHt-X5d5_vYhHZpIzv92sf44DX9WnbO2LlY5IC2eS3G5GhGDZETpsIdCYD1ysgOv3gJYlB1aAO-ZIxUlg2ZrsPdjB8_FxnLsVWZhCD5xSCfnSlGA8PU3hGZvlf2uHl65KEHv4lra_iaEqPnI62Of2-HfOfM0pn8IlIBtWJV-euNJhtb6OaH7ourrq6wYyylpljbwoi7uJOrYoe5OCFenpHBR4VZgrDbZ8QNFjJhqJOnIDpuRyEGVdsKUEmN-PVtTIEqAbZzwHqkW8tEM-U9Gfk-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce02ad2ec.mp4?token=sqkdtPTufZacBFAriQNqLC420DBg9Nl17pcxZFSmKD9V8VEXLYHybbQVA8gYNGFHt-X5d5_vYhHZpIzv92sf44DX9WnbO2LlY5IC2eS3G5GhGDZETpsIdCYD1ysgOv3gJYlB1aAO-ZIxUlg2ZrsPdjB8_FxnLsVWZhCD5xSCfnSlGA8PU3hGZvlf2uHl65KEHv4lra_iaEqPnI62Of2-HfOfM0pn8IlIBtWJV-euNJhtb6OaH7ourrq6wYyylpljbwoi7uJOrYoe5OCFenpHBR4VZgrDbZ8QNFjJhqJOnIDpuRyEGVdsKUEmN-PVtTIEqAbZzwHqkW8tEM-U9Gfk-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
گزارشگر: ماه گذشته، شما گفتید که رهبران ایران بسیار عاقل هستند. حالا شما می‌گویید که آن‌ها افراد بیمار هستند. چه تغییری رخ داده است؟
ترامپ: من آن‌ها را بهتر شناختم. آن‌ها بسیار عاقل‌تر از سطح اول و دوم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67543" target="_blank">📅 20:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6daa8309.mp4?token=SVVfLlLznv2Y8z9vcW80VrwF3p0nBgQlmZ7YVXj9NlhnkJw5f22MWFNG2ne9sYCfIjKTSGmxUPJSPuAIkpjy7gRFHIH3R5vsz2rzmZ8m9Kp-199e34EtxqyCShq4D6S-3fWNvcFOGxPH4C9A9Cdx6ynK8whV-aKOH3aKmvAx6eJ22V2r1SqFcFEzp6ydPZlAPIhy1Kdm8MplnFg7ZqytkyZpxyHzTjkDGXe5lnnnHABMKtGgF7DpVJgbV0czVTcqBgqycHAN6vCVnxWkLmGwyqawHf8WEBEIsLP26hbXxZdB-xiOALfhsJ4IW8xAeKSDSLgXSlhp44LeDM2de4V5-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6daa8309.mp4?token=SVVfLlLznv2Y8z9vcW80VrwF3p0nBgQlmZ7YVXj9NlhnkJw5f22MWFNG2ne9sYCfIjKTSGmxUPJSPuAIkpjy7gRFHIH3R5vsz2rzmZ8m9Kp-199e34EtxqyCShq4D6S-3fWNvcFOGxPH4C9A9Cdx6ynK8whV-aKOH3aKmvAx6eJ22V2r1SqFcFEzp6ydPZlAPIhy1Kdm8MplnFg7ZqytkyZpxyHzTjkDGXe5lnnnHABMKtGgF7DpVJgbV0czVTcqBgqycHAN6vCVnxWkLmGwyqawHf8WEBEIsLP26hbXxZdB-xiOALfhsJ4IW8xAeKSDSLgXSlhp44LeDM2de4V5-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
می‌دانید؟ ممکن است من هم دیگر نباشم.
من هدف شماره یک آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67542" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67541">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0540439bf4.mp4?token=nTnQirPWx_uc_Ybewi7sbMXNuBLf4LJa4m_Mv9b6o9FeiejkTpndq_lpDvVVlNBdRmt7B--xznPc-Q68Jv1VR8odmykXvUAZUjb9eHl4bJXDSALDsmCV4IpC1QQMVINCRQL3Huyej1HBsyeWRE4Ez67OcJKNQQBqcIJzhSzhh348XpnkGzR5pulLRQA5EDXIsy2aF7RHueHbAqBdikIULhXbQyV6aYk9Y2aAjANbujB0D2p_vOBUha5eQpR61zHsEh239QNvnK7rYrAxy6X4D7BrtvTVeGrZV18iNc_CpAlmhpWbhqu5XftWPBrrw_rom8MWsXnlO9O7FFW45-C8iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0540439bf4.mp4?token=nTnQirPWx_uc_Ybewi7sbMXNuBLf4LJa4m_Mv9b6o9FeiejkTpndq_lpDvVVlNBdRmt7B--xznPc-Q68Jv1VR8odmykXvUAZUjb9eHl4bJXDSALDsmCV4IpC1QQMVINCRQL3Huyej1HBsyeWRE4Ez67OcJKNQQBqcIJzhSzhh348XpnkGzR5pulLRQA5EDXIsy2aF7RHueHbAqBdikIULhXbQyV6aYk9Y2aAjANbujB0D2p_vOBUha5eQpR61zHsEh239QNvnK7rYrAxy6X4D7BrtvTVeGrZV18iNc_CpAlmhpWbhqu5XftWPBrrw_rom8MWsXnlO9O7FFW45-C8iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ایران می‌خواهد به توافقی برسد، اما نمی‌داند چگونه باید به توافق برسد.
و سپس، شب‌ها به کشتی‌ها حمله می‌کنند. من این کار را دوست ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67541" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67540">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff03b3210e.mp4?token=hoLI3alymaUVZjVxfOZkk16UO0t8PkHtrHrUFqUStESrDCfunB5oDgaabABu82-6vTgbeNfKtVQ9B0igmJs1HEteamoLAZOuR1nvgD-bksqo7OxOnHD30xTMQ6_fhHAP5FEggkDM4VdGTzFf7TSU2cA4E4ZupwihFhv5MhqGUeFMQ8twVS5oAilYEthoID0q_t4C0veBuIyHzqNi-lpKYHKYO9Q-zAd2_o8CKrGol35FKGZMsbavF0pRxi-m0E89HKAGCOQgzeh2trEE2HqF2ehguMaZeU-8vAY03sxGcwk092k0ALaYwjRG2kpDtUHs-3LrAWmVfvOQtFGlQpO7TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff03b3210e.mp4?token=hoLI3alymaUVZjVxfOZkk16UO0t8PkHtrHrUFqUStESrDCfunB5oDgaabABu82-6vTgbeNfKtVQ9B0igmJs1HEteamoLAZOuR1nvgD-bksqo7OxOnHD30xTMQ6_fhHAP5FEggkDM4VdGTzFf7TSU2cA4E4ZupwihFhv5MhqGUeFMQ8twVS5oAilYEthoID0q_t4C0veBuIyHzqNi-lpKYHKYO9Q-zAd2_o8CKrGol35FKGZMsbavF0pRxi-m0E89HKAGCOQgzeh2trEE2HqF2ehguMaZeU-8vAY03sxGcwk092k0ALaYwjRG2kpDtUHs-3LrAWmVfvOQtFGlQpO7TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز، بیش از 20 فروند از ناوهای جنگی نیروی دریایی ایالات متحده در حال گشت‌زنی در آب‌های سراسر خاورمیانه هستند، در حالی که نیروهای سنتکام به ترویج امنیت و ثبات منطقه‌ای ادامه می‌دهند. ماه گذشته، ناوها و هواپیماهای نیروی دریایی آمریکا به صورت منظم در دریای عرب حرکت کردند و قدرت نظامی و توان آتش بی‌نظیر آمریکا را به نمایش گذاشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67540" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67538">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
ویدیو ای که سپاه از حملات دیشبش به پایگاه های آمریکا در منطقه منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67538" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67537">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735f956d53.mp4?token=g-FeuWGZC5HEIyVkVx_9GAcQ6Iv8vrwtl2Pi5tz5yMVCMrMrZSIGcJ4mCVdegg-1MdedIWtELi37FTs4qyEVhweW5evIc-vg5A420NfH-NHd7X_qKoT8yIbKoBeFMSmvoMaPp587EhJY1hddAjjqivK65laS3YeuG8XTlL6jyCDFWTciZIClyOhFFkmaCLr8k8GDDvhF8pYFqRoa6vD8N2lrVkgGiJzKd9Bo-V2FQvQFM_mIxYprH7o7KyKd62MwWWrIkeoijQak2LWliifs03a48t55gGqbOS6faCjPYHXHnT_sB-lmBisYxPYOJyA0v7XtgJMuqdXVa-kxdYWYfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735f956d53.mp4?token=g-FeuWGZC5HEIyVkVx_9GAcQ6Iv8vrwtl2Pi5tz5yMVCMrMrZSIGcJ4mCVdegg-1MdedIWtELi37FTs4qyEVhweW5evIc-vg5A420NfH-NHd7X_qKoT8yIbKoBeFMSmvoMaPp587EhJY1hddAjjqivK65laS3YeuG8XTlL6jyCDFWTciZIClyOhFFkmaCLr8k8GDDvhF8pYFqRoa6vD8N2lrVkgGiJzKd9Bo-V2FQvQFM_mIxYprH7o7KyKd62MwWWrIkeoijQak2LWliifs03a48t55gGqbOS6faCjPYHXHnT_sB-lmBisYxPYOJyA0v7XtgJMuqdXVa-kxdYWYfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
صدا و سیما و رسانه خامنه ای برای اولین بار فیلمی از حسینیه امام خمینی در بیت رهبری جایی که رهبر جمهوری اسلامی مورد هدف قرار گرفت را منتشر کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67537" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67536">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
یدیوت احرونوت:
نخست‌وزیر اسرائیل، نتانیاهو، و وزیر دفاع، کاتز، حضور خود را در یک رویداد لغو کرده‌اند و در حال بحث و بررسی مسائل امنیتی مرتبط با تحولات مربوط به ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67536" target="_blank">📅 18:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67535">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a14b7982.mp4?token=RGl8Rmu7u2hp6gkmd68Zf3ChfIzVgOcLtx2TYO_1b0zkskze7tG-Pl6-leQ9B-yIYCmt2g08q4X1MIFMgm5Kad0r-iJ8Zn4UhHGyptyfqvT5mP1G8sE_T4vHA6s9IZnW_4eLo0jzeYVnsmYB_MSC5seLQaZH6tVw6ZN60H47kc0KQniICIXkq28Xjc9frMJwcR7EOLiKboVC_is7_AZzKyCFFxG2EsFB9Ca0bNzReliQzz4ieXeaI6JzxmL7HivS5IEkZNWNbOju7ORBUWkj8qyr3k3GTGsmGd11Br4RppQExKZJiyzrAy0ByKQC5a5cR41a-k6jDYb_k_ElpNegYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a14b7982.mp4?token=RGl8Rmu7u2hp6gkmd68Zf3ChfIzVgOcLtx2TYO_1b0zkskze7tG-Pl6-leQ9B-yIYCmt2g08q4X1MIFMgm5Kad0r-iJ8Zn4UhHGyptyfqvT5mP1G8sE_T4vHA6s9IZnW_4eLo0jzeYVnsmYB_MSC5seLQaZH6tVw6ZN60H47kc0KQniICIXkq28Xjc9frMJwcR7EOLiKboVC_is7_AZzKyCFFxG2EsFB9Ca0bNzReliQzz4ieXeaI6JzxmL7HivS5IEkZNWNbOju7ORBUWkj8qyr3k3GTGsmGd11Br4RppQExKZJiyzrAy0ByKQC5a5cR41a-k6jDYb_k_ElpNegYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا برنامه‌ای برای اعزام نیروی زمینی به ایران ندارید؟
ترامپ: چرا باید الان وارد عمل شوم؟ من زمانی وارد عمل خواهم شد که آن‌ها کاملاً از بین بروند یا به یک توافق برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67535" target="_blank">📅 18:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67534">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2479db8c8d.mp4?token=b5NUGUFcwknfXWKcs04FgsSuep_LpSezJIU4y2xapqf4OuIfE5y9FI09cyLA0PkKIWuLmczxUS8nuQp_fsvEMM0fdbDpM6pU6RNFj2wdmRcQK-JZsxtMnDdSdNQv-U-Bmgrm8nm23zojB0BAHkfCh9FFyOvW1WvAaB4kXPr_q742RGJZKRk9K64r4jd-dNSWDkzVxMoKrNJwwWY-PZ4qr-2nHaXFtq-Y3TfSSy_Bqz6xWjoKKClZ2Z_SjIAHEGpx1ggHUDTd1nYFB4_8d6JWaMIhQ9OTHWc-lmyvIGp8Xf66632CzJRD4KKIpK6G6yL2_EfcjXYSDHa9zM10AdeTWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2479db8c8d.mp4?token=b5NUGUFcwknfXWKcs04FgsSuep_LpSezJIU4y2xapqf4OuIfE5y9FI09cyLA0PkKIWuLmczxUS8nuQp_fsvEMM0fdbDpM6pU6RNFj2wdmRcQK-JZsxtMnDdSdNQv-U-Bmgrm8nm23zojB0BAHkfCh9FFyOvW1WvAaB4kXPr_q742RGJZKRk9K64r4jd-dNSWDkzVxMoKrNJwwWY-PZ4qr-2nHaXFtq-Y3TfSSy_Bqz6xWjoKKClZ2Z_SjIAHEGpx1ggHUDTd1nYFB4_8d6JWaMIhQ9OTHWc-lmyvIGp8Xf66632CzJRD4KKIpK6G6yL2_EfcjXYSDHa9zM10AdeTWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
هر زمان که ما به ایران حمله کنیم، قیمت نفت کمی افزایش می‌یابد.مشکلی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67534" target="_blank">📅 18:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67533">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=Hp-e8uze6Hk2BHakwRlAgXVWCtFqRoxF9PdIMo1-qBEd6JFjb7yXrSFVDZF5jce1BcJnKYS1itU8OknuihjCvts_aC1OgpVtpw4v1IR8fvvUJwLpZb5gttuMQ_6-ZbOWr2gvteQxLfGMcalVQjADHWO6kqpUNMoYRiIfgU346aAAOboh9r1MdxDVNBMQgIO4oMM1uCrmBzWAic1DwOjruQ8Or88aGZSK79tl3eRmQ8d4zwprDIlbLixuUTyRCeVOoHnMsi39f4iKYIjNwlJrkLOn8cGgigIDK3inqj22F9ZeHtLNkz-VZkK8medf2raybGjoEpHFg-jMGnQrO9nK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=Hp-e8uze6Hk2BHakwRlAgXVWCtFqRoxF9PdIMo1-qBEd6JFjb7yXrSFVDZF5jce1BcJnKYS1itU8OknuihjCvts_aC1OgpVtpw4v1IR8fvvUJwLpZb5gttuMQ_6-ZbOWr2gvteQxLfGMcalVQjADHWO6kqpUNMoYRiIfgU346aAAOboh9r1MdxDVNBMQgIO4oMM1uCrmBzWAic1DwOjruQ8Or88aGZSK79tl3eRmQ8d4zwprDIlbLixuUTyRCeVOoHnMsi39f4iKYIjNwlJrkLOn8cGgigIDK3inqj22F9ZeHtLNkz-VZkK8medf2raybGjoEpHFg-jMGnQrO9nK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره اورانیوم های غنی شده:
این مواد تا این حد در زیر زمین قرار دارند که هیچ‌کس به جز ما نمی‌تواند به آن‌ها دسترسی پیدا کند، زیرا ما تجهیزات لازم را داریم.
این مواد در اعماق زیر یک کوه قرار دارند و اکنون مشخص شده است که برای دسترسی به آن‌ها، به ماشین‌آلات بسیار بزرگ نیاز است که ما در اختیار داریم و هیچ کشور دیگری این تجهیزات را ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67533" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67532">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=KdSBRMk7bTP-uXoR6dxGAC-fnNpVZ3mVgnLJRNuT1rF1R6SZT9d95wH7-WKJPUrfFCsH8tuxZq-qF1iPxNN_l-cpNM5qY7p7pG0pxD9OWbGWCkADjxAh12E8O6d0wMUHKOUL0YBNbUwV-AzwYwyt2si3dwRfaFukqcz_0qacl4XJaI17PTQXWTU3pA8xLRQA4IUYNj2MJJGsSJ9mSCg32Ve7TkpNn60IPcYXJ_2jAJpvpFwOLqws2gLEGdxx2VqRG7oCsK564xpf08lM-IK8OACPNbtPUi6um8RTZISU4FrfW4S5OahT3--anCvsjKq7bwr8BEgd7e2p7LlwvAnc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=KdSBRMk7bTP-uXoR6dxGAC-fnNpVZ3mVgnLJRNuT1rF1R6SZT9d95wH7-WKJPUrfFCsH8tuxZq-qF1iPxNN_l-cpNM5qY7p7pG0pxD9OWbGWCkADjxAh12E8O6d0wMUHKOUL0YBNbUwV-AzwYwyt2si3dwRfaFukqcz_0qacl4XJaI17PTQXWTU3pA8xLRQA4IUYNj2MJJGsSJ9mSCg32Ve7TkpNn60IPcYXJ_2jAJpvpFwOLqws2gLEGdxx2VqRG7oCsK564xpf08lM-IK8OACPNbtPUi6um8RTZISU4FrfW4S5OahT3--anCvsjKq7bwr8BEgd7e2p7LlwvAnc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:   «امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67532" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67531">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=TNjgr6dqDlyKYTB_om83D-IbuKTfaqY_iq0Havns7nxoXFa8Wr1tnmvNJbD0A4LzMGpVpHYVrVrw65Z8DSYDpq4p9Ek4CqsKEXbnUG1XhApp4buwzAH-7o6vI30u8ZGw870wpFjJqor3pcodabQ8OhhQ_7Bg1vwZLUbsAKGdT81u9blxp9uPNCQ3e3qVVbbuKzjBaEpA4m06rePNPB0oIbzOtmuAISKHTtWhghjPEO54YAwAH6B3tY7zXA4944DvYjDqTiLyj2FWNfMD3GTsJDlnp_Hzzb_OQTtL61CoD6HeXXCsqih8hERoAsEAQUyoeHGhMIOKlzABt6ZhN3v0fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=TNjgr6dqDlyKYTB_om83D-IbuKTfaqY_iq0Havns7nxoXFa8Wr1tnmvNJbD0A4LzMGpVpHYVrVrw65Z8DSYDpq4p9Ek4CqsKEXbnUG1XhApp4buwzAH-7o6vI30u8ZGw870wpFjJqor3pcodabQ8OhhQ_7Bg1vwZLUbsAKGdT81u9blxp9uPNCQ3e3qVVbbuKzjBaEpA4m06rePNPB0oIbzOtmuAISKHTtWhghjPEO54YAwAH6B3tY7zXA4944DvYjDqTiLyj2FWNfMD3GTsJDlnp_Hzzb_OQTtL61CoD6HeXXCsqih8hERoAsEAQUyoeHGhMIOKlzABt6ZhN3v0fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:
«امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67531" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67530">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ ترامپ:
به ایران هشدار میدم، دیشب ضربات سختی رو بهشون زدیم، اما امشب قراره براشون سخت‌تر باشه و حسابی بهشون حمله میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67530" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67529">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=lKW5l4jx1AeuKijz-6cj-VCMqmUHuAYscW6r6lqfwBtwef-os5NuY7sxX1H0V2R85mxVGAWyh5wvoK6lreu2pdkQiNPX8cTfvbsNJvIkVWcmZqW8QSAfI7pmdfZzVJxLhoMfwdxR3lXDekA6nhw-zcTnqqKeLZhzyrBr7cDCdw9y2gb2wBz1bmL2TsQEwmq1jb1ABY1b99m4vTlOpMIgURyOAPMkTFv9hW_LE6w5YmMI5wxxcdIkYHPo8NWuKSHFNAwSfHBYui0pRR9-xXHXdCu_USqby7lqaGXtaueoF3zW4chk5Pu8VR6QrewLrF6zHmjlmY6NbrKZM5Wn-g0lkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=lKW5l4jx1AeuKijz-6cj-VCMqmUHuAYscW6r6lqfwBtwef-os5NuY7sxX1H0V2R85mxVGAWyh5wvoK6lreu2pdkQiNPX8cTfvbsNJvIkVWcmZqW8QSAfI7pmdfZzVJxLhoMfwdxR3lXDekA6nhw-zcTnqqKeLZhzyrBr7cDCdw9y2gb2wBz1bmL2TsQEwmq1jb1ABY1b99m4vTlOpMIgURyOAPMkTFv9hW_LE6w5YmMI5wxxcdIkYHPo8NWuKSHFNAwSfHBYui0pRR9-xXHXdCu_USqby7lqaGXtaueoF3zW4chk5Pu8VR6QrewLrF6zHmjlmY6NbrKZM5Wn-g0lkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
آنها توافق کردند که هرگز سلاح هسته‌ای نخواهند داشت.
و سپس، آنها به بیرون می‌روند و می‌گویند که ما هرگز درباره این موضوع بحث نکردیم.
چه کسی باور خواهد کرد؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67529" target="_blank">📅 17:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67528">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=TcM2Ns-vPHDWzf59zyZQkg-k3RkKEOhqQgBJRw7rg6HC8O1bc4mpuzRxXfGySAQTPQCMWKppCJd59bRi0BxN3-RVlmw7pc9XAdyiycMH99_SRb2jgqcWjAgxLjREnbHoRrDnGC6EAdolizF4tHsnjUfWtkl1OtHF505MAuBX9hxulTn0H70vv_y39fuh-rnCKWeqUb_UDNSx0tgcfMv3SeVY8Lg17WIP9qJ3avR1Jb8SyGe3M3oigGaq7LlsI2IJiPY9yxdJbjfktLcmcED1ihDWfkKb0Ls9WZanTg88c26wxQsQJbiidOwITWFi_3CnVF-RQZg27VABjojVAjhbDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=TcM2Ns-vPHDWzf59zyZQkg-k3RkKEOhqQgBJRw7rg6HC8O1bc4mpuzRxXfGySAQTPQCMWKppCJd59bRi0BxN3-RVlmw7pc9XAdyiycMH99_SRb2jgqcWjAgxLjREnbHoRrDnGC6EAdolizF4tHsnjUfWtkl1OtHF505MAuBX9hxulTn0H70vv_y39fuh-rnCKWeqUb_UDNSx0tgcfMv3SeVY8Lg17WIP9qJ3avR1Jb8SyGe3M3oigGaq7LlsI2IJiPY9yxdJbjfktLcmcED1ihDWfkKb0Ls9WZanTg88c26wxQsQJbiidOwITWFi_3CnVF-RQZg27VABjojVAjhbDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
جمهوری اسلامی ژاپن دیشب به ناو هواپیمابر ما حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67528" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67527">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=vg6b1nmnzSJkWQuT70zHauahyjY5Ga0x8JXxaYcVevRA_obf885JwC2e1BWILtIgTLcCTowkOg81Rqjbkzuful0NsCNqwRYJSMYnFaU4U-vh1BXPOybZcBDLU6RFUQ-N9e0liO0mtB79n5gFYymiQaPOqM5_NbGzRn_pKJigoW6TZCFFMAXUjmIX5ORzX8rR9yDxArixTAyk8-Q6O7LabPTcv8T6SNb2OolGXb7e_DgcqhdJKPGXF7YtCesP37kMoRFGItzs5OjIBASzP2NzxctNZxs6obswkU7-X6Snm5D7QNBk6q7gQ3kGdYpZwhHv2vpixucbw-1--3EZsJvzrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=vg6b1nmnzSJkWQuT70zHauahyjY5Ga0x8JXxaYcVevRA_obf885JwC2e1BWILtIgTLcCTowkOg81Rqjbkzuful0NsCNqwRYJSMYnFaU4U-vh1BXPOybZcBDLU6RFUQ-N9e0liO0mtB79n5gFYymiQaPOqM5_NbGzRn_pKJigoW6TZCFFMAXUjmIX5ORzX8rR9yDxArixTAyk8-Q6O7LabPTcv8T6SNb2OolGXb7e_DgcqhdJKPGXF7YtCesP37kMoRFGItzs5OjIBASzP2NzxctNZxs6obswkU7-X6Snm5D7QNBk6q7gQ3kGdYpZwhHv2vpixucbw-1--3EZsJvzrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ممکن است محاصره را دوباره اعمال کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67527" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67526">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e08b208584.mp4?token=UoUHmt2veR1nvA-31qKxo60y8HhAm9eq_Q5Q5crIa4XrqXKDuKrbqfv4HW3yvQQSWNrc_2stiOXwPuresdCij_oaVaI3cal3gwnkhTi4yXLjG9ioXsNFvX2CG1XAYMkcUlf2oL_vvUDvxZQcVDi-m6YnE091Sg8STRVwNUhJ-YhPLCrLQieXq6oxF-YkRgYQxjjDsAO6jU7doWeLXv-pgD-dbLohrYdHSgwZsAK6RpIIefqmRZyN27HThsgMdM5LtQYjuFpFyBqvACOOwkqQ0jVX3XzbWEDRgfEHx3zdFx1c5Sn4Rkk9k1nrey7ptE7t44C53kx39CKVqa2u2A1xYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e08b208584.mp4?token=UoUHmt2veR1nvA-31qKxo60y8HhAm9eq_Q5Q5crIa4XrqXKDuKrbqfv4HW3yvQQSWNrc_2stiOXwPuresdCij_oaVaI3cal3gwnkhTi4yXLjG9ioXsNFvX2CG1XAYMkcUlf2oL_vvUDvxZQcVDi-m6YnE091Sg8STRVwNUhJ-YhPLCrLQieXq6oxF-YkRgYQxjjDsAO6jU7doWeLXv-pgD-dbLohrYdHSgwZsAK6RpIIefqmRZyN27HThsgMdM5LtQYjuFpFyBqvACOOwkqQ0jVX3XzbWEDRgfEHx3zdFx1c5Sn4Rkk9k1nrey7ptE7t44C53kx39CKVqa2u2A1xYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
آنها به ما گفتند: لطفا در مراسم خاکسپاری ما را نکشید. من گفتم که این کار را نخواهم کرد، و ما هیچ اقدامی انجام ندادیم.
و سپس آنها به سه کشتی حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67526" target="_blank">📅 17:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67525">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=KpRQO5xcPESx6rLUCPG8BcZ-SVNeIh8lM-pAowFqd4BUJX9Hm7EOuRhYuHmCn1hc3yo3KPRZaEOvJNz5nrgRjeYvlXGYqnOYOsVNmQvQWeo1PP1qC9t-WstRMMqMtIfH-z0T-TJxGvDklt97K_-o0dWTfHrLdJhNsmf0ej0ItsUUqgeJbYFI7jpU2gPRAWpGkzwg7M0_zinCnXy7FxAhSvt9eIgM4U-s_TNEPL-ML2X0QzeihW2AzM-57WG0_nlRl1P1uOC63Wh75OtS5EiZpNim63_N0ZuFT6B4gkoFEA7wTopWPCD8jcQg6g7DinI7TXnP5phO_84VF1vXDoxkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=KpRQO5xcPESx6rLUCPG8BcZ-SVNeIh8lM-pAowFqd4BUJX9Hm7EOuRhYuHmCn1hc3yo3KPRZaEOvJNz5nrgRjeYvlXGYqnOYOsVNmQvQWeo1PP1qC9t-WstRMMqMtIfH-z0T-TJxGvDklt97K_-o0dWTfHrLdJhNsmf0ej0ItsUUqgeJbYFI7jpU2gPRAWpGkzwg7M0_zinCnXy7FxAhSvt9eIgM4U-s_TNEPL-ML2X0QzeihW2AzM-57WG0_nlRl1P1uOC63Wh75OtS5EiZpNim63_N0ZuFT6B4gkoFEA7wTopWPCD8jcQg6g7DinI7TXnP5phO_84VF1vXDoxkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما شب گذشته به جزیره خارک حمله کردیم.
ممکن است کنترل جزیره خارک را به دست بگیریم. هیچ کاری در این مورد نمی‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67525" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67524">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=NJ8kUfJolKLI4brkmkFW7pFE_XcDBI5IWQxl3GXfUh_isnudGLRwu9fdohOhXEdeD2rTmpaG7x-7wzmtDk9mpcq8Kab5RTvDeXqI2vfIlIQwmb7gojA6RFBjxgOWzs7GY6Ufz22FqBpkG8G8EXzicd42m222gI29ZTdPXQAVK1dzdRdYJqvHQvXu_3admmSwlLqVapsHAz-vq3a583ES8lPjKUnS71V8nrI591TeWnXc4GzJIJHrK9rwSaeJmrasWNCpxF_jJuIMtKWNGH5rHoknrcNAVK6Hi-PjH7oHDj7T6EDcHCufvZAwQeyDAl5RmO4prj7V50MzihATDS1i5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=NJ8kUfJolKLI4brkmkFW7pFE_XcDBI5IWQxl3GXfUh_isnudGLRwu9fdohOhXEdeD2rTmpaG7x-7wzmtDk9mpcq8Kab5RTvDeXqI2vfIlIQwmb7gojA6RFBjxgOWzs7GY6Ufz22FqBpkG8G8EXzicd42m222gI29ZTdPXQAVK1dzdRdYJqvHQvXu_3admmSwlLqVapsHAz-vq3a583ES8lPjKUnS71V8nrI591TeWnXc4GzJIJHrK9rwSaeJmrasWNCpxF_jJuIMtKWNGH5rHoknrcNAVK6Hi-PjH7oHDj7T6EDcHCufvZAwQeyDAl5RmO4prj7V50MzihATDS1i5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گزارشگر: آیا امشب قصد دارید قایق‌های بیشتری از ایران را هدف قرار بدید؟
🔴
ترامپ: معمولاً این موضوع را با شما در میان نمی‌گذارم، اما می‌دانید؟ آن‌ها هیچ کاری نمی‌توانند در این مورد انجام دهند، بنابراین احتمالاً بله.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67524" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67523">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=sOwzN96gZRif3TKjVD3OqrLsAhxDH1LkzuOEyxZTGz4THomNCCeKrcsolGDLh6SvgvxJBggoY0IPeFEZxAuI1X1du2zYbmdYQ9VLqcO0OwbKtPsAPAfaPjfc6cc31uz8qsNTjLp0nSHf0uhppmJV0v8ATsKKGt7-Jg5hQahWc481cHD8q_BYZdj9_6ndXIogFYJZPe8xc1rp9MUtZ8YFaqgtCZyfjVCrK1RnsAfe__JqrPGcTYHSujSI08iFUwezMqMP9An6ix-tZvOAGxjuaCSylBmSEEdQls4EFPCsyV1HdrQJOclTDNeHOzSdCkR5_i4fuzE9aS6Ifwyw8bP76g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=sOwzN96gZRif3TKjVD3OqrLsAhxDH1LkzuOEyxZTGz4THomNCCeKrcsolGDLh6SvgvxJBggoY0IPeFEZxAuI1X1du2zYbmdYQ9VLqcO0OwbKtPsAPAfaPjfc6cc31uz8qsNTjLp0nSHf0uhppmJV0v8ATsKKGt7-Jg5hQahWc481cHD8q_BYZdj9_6ndXIogFYJZPe8xc1rp9MUtZ8YFaqgtCZyfjVCrK1RnsAfe__JqrPGcTYHSujSI08iFUwezMqMP9An6ix-tZvOAGxjuaCSylBmSEEdQls4EFPCsyV1HdrQJOclTDNeHOzSdCkR5_i4fuzE9aS6Ifwyw8bP76g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انگار یه نسخه پرمیوم از ایران هم وجود داره که فقط مخصوص پولداراست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67523" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67519">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfz15MgjzGb5ymlJSZl0cwqnxPCXdhzTRshfaJUvZiMplG_u0BS-ip-c_VXtSxKPk2hpZy0HDZnIUBfKuVHZtFKeHmR9EyjWpLoFRxK3XXD7jmmWS-3Hiep9sO2HhTUze6gxWBRzP2oppC1rszaCFrnT0axtBydHdmHio6_z_3Lo3xkTu3Lk7iUBu838Ohz3xUH9FwuyDlIgpL09SBsdtNB2gZ_b3Yi4ipocatgRi3AvuyOIxsCBsfslgyddGZ8ONT4ah1hnCMVWQfxfif3_LLXifWk_YyNs6cdUD6Q5oFhTKams89kIDU85dD1Y1lwst_hQCQMxMeyBLV7MtGiYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41735c920b.mp4?token=dArQ-Q9ojJWOHDZtoDXGe__Z_Fd7XYEJwxpWp2II_v3CJTlXxNUdBWQiXvWs90kZxVIDyIfGeV8Zej3E5rap_SA2jX5d4fGYg8jHndCc6UHzWnkvvcgy8eOfaeJkL49fMwWB9OgAtm-8QSiCUmSQ0yQRKn7muNt3lEQ9Zif1yUYmddn6w1L0r4wUog1NRX5e6GcSCkPUjY85FrF1x0Ij7APtd_Ov-t7FkOtSl9K6AkPhearIBGmKwye6BRbUMS6HBMij4ERTF7Jh9cFyHEGJ44o_eDn4CkgFQ00ARPLH4eGphsoQKNxoe1tXXLiWcCmKezKyai_Klqc25B8_IDaAjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41735c920b.mp4?token=dArQ-Q9ojJWOHDZtoDXGe__Z_Fd7XYEJwxpWp2II_v3CJTlXxNUdBWQiXvWs90kZxVIDyIfGeV8Zej3E5rap_SA2jX5d4fGYg8jHndCc6UHzWnkvvcgy8eOfaeJkL49fMwWB9OgAtm-8QSiCUmSQ0yQRKn7muNt3lEQ9Zif1yUYmddn6w1L0r4wUog1NRX5e6GcSCkPUjY85FrF1x0Ij7APtd_Ov-t7FkOtSl9K6AkPhearIBGmKwye6BRbUMS6HBMij4ERTF7Jh9cFyHEGJ44o_eDn4CkgFQ00ARPLH4eGphsoQKNxoe1tXXLiWcCmKezKyai_Klqc25B8_IDaAjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات موشکی شبانه روسیه به اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67519" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67518">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_fzl4NCcDIc0QpK0BxVSz93YUpE9ggkzMLVpDUM9ReIbXidx08jr_Dk0spD6sSkANRq7hG8wn1rVkA36nXddde47XWlIdJ1Ob68cUDRkhzRXKwC36b2Sh_cCyTAbhU4-jr0n1O3G0G1QmckNnsL0C_H1iY9PIIOqpu9RbfB_cG_U9gl9YKNG_H2-l2qMto0Is_M4vfUam5ZVHJeHR8cc8GR_hO4fZEta7qW9z7WN5mXU6rQm-hiErQhmw6ot-FFqTxfvHb_WFNr17GlSL050cGJt2uegew8uOK-CmMnjawJPVOMhL7W4y-fldAWZIxhnmon0HIEb2Z2N0j2hFKhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری هادی چوپان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67518" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67515">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwdlH35WnJimMAaHpydFO_EmIklIZj6zp0DQfPCGltpyQNzNzWmayKUrvUJ7c1bu23QJ_4XwtZ8g0b8woaX4rgusBkFgIVfiay9AdjH_3vKOV5I6EuEK0dU7LXO_2NEQLcXZmerbW3poe2l88lkcxgwroSiqVU05w7-12v5-3lJMlzt0DShtyIGYddLrq0BPGtvOrxixADMVy_jDU1ISX4SqLh04Wc_F3XBr0plbQMQnfgyggvGbSy465WCBxbAMzasOa0Xw2H9BUd8ZbyxEMdtY6sKjtinDOC5vCsJP7KJ3y2yDPb66cj53GIyslgdVriI4BTdffhOH6s4AgOzLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKuuigbqGpjOp9CF2zvdn19qBAun6gXMhQmpPjgoBQjisSiNNt8FIhkklIpqEoN1EAaKL5_XK4V8_jFNWvzPVcWnOurFnlqgnZ1ZnZ5U-jHrxLGBzi6TCtOkWGDnZsYZdXjsvQH33mmGjM9Yc9PXI1XQX-G8LcqAVAnPkO9gdydf-A608LGc1XW1823Xj-ccIfnhPxzoLHTBfdgK2jpTmdOap0OtBzQr_-26oazU7_kdNsEn__14yF6be0deoLwVKiwb7oUMM8o9WF8lIBQ7HlQC_pbG67QlCVroNAL8B1ukjb19F-4vYdrpha5A3mEyguhd9bLni7V9XJRR6uVaNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=eaIftD7Q6gu-AoJj34a-TcZgRyxDIp34qw76JPdI9EhyFRssvcemixc7QdqMntsGRPL1RqdHq5hj42jJ7oWE1Im1W9DGyVthYyUpoCim8-Let5OvJcuH8oix0h7n4JpkSSOtoYjZzCCCRV6A5PbjzjHv0u30ZIY_LA-FshciZKkZCD5fnfuHO-pRaC1LEYq3AalvtVWpH9hmyXfrQbhRDucLvmxBkuJSUublU3Wx_-0PmwSXWY6Oa1vo0pJiG-rJLQnqz-XGDcatoxzePyiSaoE2hOGAulpFRZVtM1uYtn-Jrbjd2CmEoZisbAxM1bfwxAAzFGfb-RBsUZl1uOHPv4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=eaIftD7Q6gu-AoJj34a-TcZgRyxDIp34qw76JPdI9EhyFRssvcemixc7QdqMntsGRPL1RqdHq5hj42jJ7oWE1Im1W9DGyVthYyUpoCim8-Let5OvJcuH8oix0h7n4JpkSSOtoYjZzCCCRV6A5PbjzjHv0u30ZIY_LA-FshciZKkZCD5fnfuHO-pRaC1LEYq3AalvtVWpH9hmyXfrQbhRDucLvmxBkuJSUublU3Wx_-0PmwSXWY6Oa1vo0pJiG-rJLQnqz-XGDcatoxzePyiSaoE2hOGAulpFRZVtM1uYtn-Jrbjd2CmEoZisbAxM1bfwxAAzFGfb-RBsUZl1uOHPv4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه تو ایران با سنگ و چماق میفتن دنبال عباس و میگن مرگ بر سازشگر ولی تو عراق اینجور نیست!
مردم عراق انقدر عراقچی رو دوست دارن که اون رو تَبرک میدونن و خودشون رو بهش می‌مالن تا حاجت بگیرن!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67515" target="_blank">📅 15:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67512">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEoRnu0z-mjWbdv1M-2auWqRkyWqqBKSnl9OFjIOWKSiclWgKd0o-haaUtKnLcSWjdyS9FUq_XqfrqvIsXvR0xCpm_sNIK7cpSBOQMQmY3LwJloQgdsuVO3ggao5TPEESPOI0qb6v91CPGBv1j_xwz7h9LDV9pHLEdXBdRMP7o91Ndo39aPVJg5j4-ErYRxr7B5d5xagE5YDdYSiYTM76SJC-zSbLpPCgKbkV8UOEfh4tLOU7wPqWrQPpVZr1iBL7y-Jb3pPtASycFNqoTcENQwrgLSWwJhYAFFhTclsBJgHaDCha9S6lHTao_hjN2-kkmO7Mx3XkPLL9UOIPotkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuE8kcucSsobQbnZ4sdJsINlu5pp1J78ZjIgvbGpvrjc2QlMfbpnVbp5EvPTH2kHHYZvp8QR1Y23RlLjTWCOHTWfv8mWD2zeKZpjg8SFMuf2yaSZBvZgFfZrBQiRqQQQwqUV19DNN6WaJ1V9GJkWtZ_hwTzzA32XhTGeDnsDlmd3Bp9vYahrY-gNU1LVDxliOBCm7ncRaUrw9pytoQMWbOR61HHV5rxvO0Qt-wHfS82xBNbylL6-n-rbjrqteyVwXKX0CODAOCPdg-_m3D8i95is4XvsLmTBxiDE8cuHVRBaWGvOZRRRrwAkhjEqLkOGl2LbOzBLow0Zy7YsW3jBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hi8Xeb7BGty50k5lNjrLM8je8E0rYaevmopVcUNilOsnwDbTvUPVnDSsBQ6mm7Y0ay6dJI17eFY2Bi-qBxJrSWhnyYOWGa3y32aShvGGym30PjbO58y9qFWxnECCTjvkeU2-QXnkoKfDmUXltmxjDY9Q6HMYIgJ9qY_7K9RLpUqEmU2mgWgT-UOZe-zeXMtxs6vGhSpyEfEb6PDSft8t05NzL0B9w1W0B_0LFfKpHRrmiXCRpMRPtFW2Q0-yUy0SriythFoXY_6bfwbNw3o4tYkvduw_jVGHEuF5_S-t5ktBDPeSkcHGhuc93xIqOrRnuGHQ3j_5OwaeltO_TW_IXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
خبرگزاری تسنیم اعلام کرد یک پهپاد تهاجمی MQ-9 آمریکا در آسمان بوشهر سرنگون شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67512" target="_blank">📅 14:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67511">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=JN2RxP2POpSpo2bPzqGoczbiotzy8SvwEWXI6CsXYHmx2Uf83ldO9ADPCqwsawsT2s9pp88Zwj9ljTnLfxnd5A_aoUcjBbadOtWYGywOQ5O34IRRSklP7liB3QOcesev0it08B41cJAlcP90vZnUMCSCA5d12IcMME9e6-Blg02RKmSar9rMP8bpp10lOzHe_D_d_7f_WtADkweS8cWIaz0XG1qx4CfweH2_sccYnzCIQ2Q1yT2p1K-V_kmw6Tvu30avctAXrYRjkGp4gLFjVpz-hVKsqe-lqjTsjQw94ebEA2zhrCb7SrUjbmxiorZLFyldjLL9zW2kbpIPIgQLsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=JN2RxP2POpSpo2bPzqGoczbiotzy8SvwEWXI6CsXYHmx2Uf83ldO9ADPCqwsawsT2s9pp88Zwj9ljTnLfxnd5A_aoUcjBbadOtWYGywOQ5O34IRRSklP7liB3QOcesev0it08B41cJAlcP90vZnUMCSCA5d12IcMME9e6-Blg02RKmSar9rMP8bpp10lOzHe_D_d_7f_WtADkweS8cWIaz0XG1qx4CfweH2_sccYnzCIQ2Q1yT2p1K-V_kmw6Tvu30avctAXrYRjkGp4gLFjVpz-hVKsqe-lqjTsjQw94ebEA2zhrCb7SrUjbmxiorZLFyldjLL9zW2kbpIPIgQLsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احمدی نژاد : بابا داره بهتون فحش میده،یه مرد بین شما پیدا نمیشه پاشه حداقل بگه خودتی؟!
+ترامپ امروز به مسئولین جمهوری اسلامی گفت آشغال،پست فطرت،کثیف،تومور سرطانی، شرور،بی‌ کفایت،بی ارزش،بیمار،روانی و حقه باز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67511" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67510">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
رسانه های عبری:
ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67510" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67509">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbjxAb4K3NmzOwRAU_Ewp3e91G7Ku0GoUGcRDEe4ZZYn2im51xGmuAQ1J9OJFssNioTiF8HravSUawirf5K5mU_JdkcQ3NJEY4AY1skevQJvJY4CD_9q-xNoS4Zivp3kmdM9um0wohRuJok0mgyFmZUXf_iGZSOlWoQqtFFV3e8RBT2IjSltQ5UUxN5TXo1sNLzlv1h92yQe0gLmY1al1eVa9mdTXWeI3OHaylqPwjlyevS2mDjAMqE1axEMQGXGWz_a9TqmPht03dj1NhiefIc3J7s2TRA7tSweRbYrbBkDCqbbQpdjk0SmBIEn-GZUJRh4g66U-UqQ7hjQI_sHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
پزشکیان:
رفتار دولت ایالات متحده به عنوان میزبان جام جهانی، همان سیاست خارجی همیشگی آن را نشان می‌دهد: زیر پا گذاشتن قوانین، زورگویی در برابر رقبا، ایجاد موانع و تقلب. این همان روشی است که آن‌ها دنبال می‌کنند. ایران چنین بازی‌هایی را رد می‌کند. ما به طور قاطع از حقوق خود دفاع می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67509" target="_blank">📅 12:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67508">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-sHzm-3uJ92ikJ_AuWLvpAbnGSmkdqP9aX7v0tLRdcgcr-P16HseEHARQyEQuDEt3JLqWCZwoS7kG5tXyMcyPOeRLt2xZvgH-eB-nhtukFPc-xNPVaAKVzl20dC4URBbw9EH5N9F-fEFXWUm7volwtHNGFm2Y5Z-3HB2XKDFVZIXwXAE8Z4bGpSMR3MsqfuUHI9wz17oC6UFyExmYmoFGKwg17gakrG8vDNND9hadD7x69sENkAXx2M00fAIN5mY00I451cGNiSp1Se31ZPYXnAXUajp7e3IBFNnCPEC3Jd0fzUoQMOQWjhBdhj4fXpPWyMjHZSikQ3iOHWwsGR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمیت سگال:
پیت هگست، سفر برنامه ریزی شده خود به اسرائیل را لغو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67508" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67507">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
«ما دیشب به آن افراد بسیار خطرناکِ وابسته به ایران، با قدرتی بسیار زیاد حمله کردیم... یک مشکلی در آن‌ها هست. ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. بنابراین دیشب خیلی سخت به آن‌ها ضربه زدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67507" target="_blank">📅 12:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67506">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=J1Gb0Fpjv7U08n6ggwDZxMXkocf8wZKg-e70Y2p1QTGZhshFXj3TsvWSFEahWYEzzCJ6RbajPqRrX5dCIzZynZzFcXbzFVell_kWhn24ezTKqPFDibGJfSMtnA0RA9CQUa6qg82EWjeD1v6pckMLILv4rUudsCeRiWTFrXHiMJss9LLpMGhRL_DlLxfrgcXsJrvOteWKqHYttO9kc9U9aw1y_EAWvrHUG2Ie4xw4mO5PvyiRxqWDCOVYprZVPjbwZ27Mu9bytoDBKqliSpbvY5pEbUGLGu_ke5uAGWrWlTLJN9ZpxtWps00qVka80s0edUXD3WGOKXsKI5sw1YIvZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=J1Gb0Fpjv7U08n6ggwDZxMXkocf8wZKg-e70Y2p1QTGZhshFXj3TsvWSFEahWYEzzCJ6RbajPqRrX5dCIzZynZzFcXbzFVell_kWhn24ezTKqPFDibGJfSMtnA0RA9CQUa6qg82EWjeD1v6pckMLILv4rUudsCeRiWTFrXHiMJss9LLpMGhRL_DlLxfrgcXsJrvOteWKqHYttO9kc9U9aw1y_EAWvrHUG2Ie4xw4mO5PvyiRxqWDCOVYprZVPjbwZ27Mu9bytoDBKqliSpbvY5pEbUGLGu_ke5uAGWrWlTLJN9ZpxtWps00qVka80s0edUXD3WGOKXsKI5sw1YIvZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره مقامات جمهوری اسلامی:
آنها دروغگو هستند. ما یک توافق می‌ کنیم. همه موافق هستند. هیچ سلاح هسته‌ای. ما یک توافق می‌ کنیم.
آنها به بیرون می‌ روند، با رسانه‌ها صحبت می‌ کنند و می‌ گویند که ما حتی درباره این موضوع صحبت نکرده‌ایم.
مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67506" target="_blank">📅 12:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=pFZ-FJQv3eZdMU4IHqT17G34cTO4U_uMyglYTuCbwtn0aaUpIF4_1PWxbXzL9ZzCNzk8Ffq3i_IUQBcr9dKdtyzr2q0b6eIgzwIjd7ATrUwPQpgF3Ev6DgZxeALPUq9KNixlizyTcVbpRBewW2ioCw93Z07PUYNAcfjeXa5ynj4rtx18vVyhQ0zyjOEA6cWLrkQxcjbOBN3z7-ojc55ngs1YOTWY_tTlTgpKNbKA2qXsi7i942E_hVrOoXloSqN2PnzVKxOs1-sp4Th5coFSh1NyQemFcaYvpoSjcdLwn48WVkuJjRbhxO3yxPqio4nTFFB4TWUdjHkX7AViO4RJ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=pFZ-FJQv3eZdMU4IHqT17G34cTO4U_uMyglYTuCbwtn0aaUpIF4_1PWxbXzL9ZzCNzk8Ffq3i_IUQBcr9dKdtyzr2q0b6eIgzwIjd7ATrUwPQpgF3Ev6DgZxeALPUq9KNixlizyTcVbpRBewW2ioCw93Z07PUYNAcfjeXa5ynj4rtx18vVyhQ0zyjOEA6cWLrkQxcjbOBN3z7-ojc55ngs1YOTWY_tTlTgpKNbKA2qXsi7i942E_hVrOoXloSqN2PnzVKxOs1-sp4Th5coFSh1NyQemFcaYvpoSjcdLwn48WVkuJjRbhxO3yxPqio4nTFFB4TWUdjHkX7AViO4RJ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
به نظر من، ایرانی‌ها ناکارآمد هستند.
اگر کارآمد بودند، ۴۷ سال پیش یک توافق انجام می‌دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67505" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=o74X0KCT_7ZkIUPPNamdyEGccPKy472ySoGCEFvnL_ZaDWtW2xeNuomg7y5kmUrzZkxgRnFVSKK6IZeHgEJjmSxRpvqqKwKEf8lVvb6l0Mq_uw2m8V0pdFPZ2i1qItpas-4Ka_Wlwqj8u8Z_QS1c5lrdJaNVoKYSEiKWrWFvFx_lwppzk0mrKXGPbbciJTWIn_yR1psDfD4V-y8iLMucf3O0WhuP9VdOucl7iGyO6J8TQU_9c4rGworLXs_KDqZwHDyaNFZHn4oyhm6azMv3-5uuyt-SVt54nDAwW2N7On75mAFxgaDohfmFhUMyiT-JgJ37hW8Dr3UeVVv2ZcIsug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=o74X0KCT_7ZkIUPPNamdyEGccPKy472ySoGCEFvnL_ZaDWtW2xeNuomg7y5kmUrzZkxgRnFVSKK6IZeHgEJjmSxRpvqqKwKEf8lVvb6l0Mq_uw2m8V0pdFPZ2i1qItpas-4Ka_Wlwqj8u8Z_QS1c5lrdJaNVoKYSEiKWrWFvFx_lwppzk0mrKXGPbbciJTWIn_yR1psDfD4V-y8iLMucf3O0WhuP9VdOucl7iGyO6J8TQU_9c4rGworLXs_KDqZwHDyaNFZHn4oyhm6azMv3-5uuyt-SVt54nDAwW2N7On75mAFxgaDohfmFhUMyiT-JgJ37hW8Dr3UeVVv2ZcIsug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
من در تمام لیست‌های آن‌ها قرار دارم. و تا به حال، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی برای مدت زیادی ادامه نیابد.
چون این‌گونه است که مسائل پیش می‌روند، اما ما افراد بسیار خوبی داریم.
اما این‌ها افراد شرور و بیمار هستند، و ما باید از شر این "سرطان" خلاص شویم. این "سرطان". و شما می‌دانید چه باید کرد؟ باید "سرطان" را در مراحل اولیه از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67504" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:  فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67503" target="_blank">📅 12:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67502">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=Ki4ScAC-M58U-jYMZc6dUg0Mm3lTxNF0pfzEsAPy_DbGZdr5PNtFgzW0n22aL9bDODFNi3LerZCbRt7jI4EZC81pjS3BbSi6jmMggXlTiLp4MeTB8dhsPW01P5lovhr2dBvD3ioQXehmb35tBRSX9s9cOkLQ-3YHDhAAGQcj2p-9Vg9FtXWfd1LT4wLZMFftei7rGPLivI0hIVrWMnsaUl9rP7fQVZ_LoJkfh2rYH771WmFfDwta_ai40ORF-4X8nuINL0zHhrbvjSHbMR4OCnkBuE1rBqgBD3OoOybhdOkBQVxl2RX8BrA7mqerJ6LB6A83qr-YPyFerR9FZih7Coi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=Ki4ScAC-M58U-jYMZc6dUg0Mm3lTxNF0pfzEsAPy_DbGZdr5PNtFgzW0n22aL9bDODFNi3LerZCbRt7jI4EZC81pjS3BbSi6jmMggXlTiLp4MeTB8dhsPW01P5lovhr2dBvD3ioQXehmb35tBRSX9s9cOkLQ-3YHDhAAGQcj2p-9Vg9FtXWfd1LT4wLZMFftei7rGPLivI0hIVrWMnsaUl9rP7fQVZ_LoJkfh2rYH771WmFfDwta_ai40ORF-4X8nuINL0zHhrbvjSHbMR4OCnkBuE1rBqgBD3OoOybhdOkBQVxl2RX8BrA7mqerJ6LB6A83qr-YPyFerR9FZih7Coi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:
فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته باشند از آن استفاده خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67502" target="_blank">📅 12:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67501">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_SlYyeGVaXaltKOd4tDLDzlm0bEM-wIhuCYkyg5By2zdy-mgofelvkkeXuaLrcj9pc2xdpebLpM5BiE26fOHkaQ-4wjmcayoxQoRyOUJGOOcCfqYMMwY4FC802gjaZ763UNyQdahnO4DqNlM9UrTsDcmMZ5fiKnS8QjTqekPDf5vRlA74dSRrscUlGaoyVdbJz2rxWLfe4Yf_BZ8vtVHvO9v5bLCQaXiFX1n3YK44xCDef_U2CnO6898bqc9-ev6ZYfPA2qWQBHwIHYqQleNbJ2HfO5iWpJY6tZ07dD3am6m_2nrskw3pAuJU29dZKnyBMjwdMqAYJJOM_64oTAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از حرف‌های ترامپ، قیمت نفت ۵ درصد افزایش پیدا کرد و به بشکه‌ای ۷۷.۴۰ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67501" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67500">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=EGnbtVQLQyxf3dKGIsPd4fcfxIXQnqdB39IOUFSmHLjliRwei9OxZfXMbQ2E3OrBw1Z99qmAKDAT8h5AH2s5Sc3aeX1cNWK9P4p1PuS7TLAffNcIehxur2pGG8gha1LRLGP8GJfWQaTSFr7ZrZZVr0m7v3ZGLHCzhxiAavh7SAuVnOlXymegHvNWXA190qrf9i8PHwfOgGug0zBK1kCFEpNPcJNEWwx11piD5WF45DnH3NXZTbDysAhHkyubNVABsSGXSXtk3mNbrbtGpcJiORFYXNoBeYKB0-_tm491qgdMgovx6Brp4JFnnf4cmsVDRWPO-b7g6ibqWnwJcpPSTgbmL72_ad8Q7HbJWHNzkzJlKBDXA3LiZi2jjtxi_0gzX38HANiwtW54cCs22su3F7RMvxPjCPOsIXXLgEZ2AsaUTewHaBaPzCvMSP_5D9524JzJKguyy0RZL8-3-mKUpV26QdXeeFoi1hI6ASSUu_m7i-hNsZsYKtALmidsHrCfDg5h13jzLokzHwnHQEch85cynB5U-dFwmwG6u5kiVCnB61_atVk66_IijfDQFL73j-ojhlWijfDYmjPOGqt_SYhZEQFRaZiV1NHp5fnUyz-fAwR0n6UUXzNkPS3Fxh0meN26gMRDXW2SxkKCGo3ZkunsvMCZlMxhM-T4BISEfPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=EGnbtVQLQyxf3dKGIsPd4fcfxIXQnqdB39IOUFSmHLjliRwei9OxZfXMbQ2E3OrBw1Z99qmAKDAT8h5AH2s5Sc3aeX1cNWK9P4p1PuS7TLAffNcIehxur2pGG8gha1LRLGP8GJfWQaTSFr7ZrZZVr0m7v3ZGLHCzhxiAavh7SAuVnOlXymegHvNWXA190qrf9i8PHwfOgGug0zBK1kCFEpNPcJNEWwx11piD5WF45DnH3NXZTbDysAhHkyubNVABsSGXSXtk3mNbrbtGpcJiORFYXNoBeYKB0-_tm491qgdMgovx6Brp4JFnnf4cmsVDRWPO-b7g6ibqWnwJcpPSTgbmL72_ad8Q7HbJWHNzkzJlKBDXA3LiZi2jjtxi_0gzX38HANiwtW54cCs22su3F7RMvxPjCPOsIXXLgEZ2AsaUTewHaBaPzCvMSP_5D9524JzJKguyy0RZL8-3-mKUpV26QdXeeFoi1hI6ASSUu_m7i-hNsZsYKtALmidsHrCfDg5h13jzLokzHwnHQEch85cynB5U-dFwmwG6u5kiVCnB61_atVk66_IijfDQFL73j-ojhlWijfDYmjPOGqt_SYhZEQFRaZiV1NHp5fnUyz-fAwR0n6UUXzNkPS3Fxh0meN26gMRDXW2SxkKCGo3ZkunsvMCZlMxhM-T4BISEfPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره رهبران ایران :
«آن‌ها دروغ‌گو، متقلب و بیمار هستند. به مردم خودشان آسیب زده‌اند. تا امروز ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید بعضی‌ها می‌پرسند چرا مردم حکومت را سرنگون نمی‌کنند؟ چون دیگر زنده نیستند؛ آن‌ها را کشته‌اند.
مردم سلاحی ندارند، اما طرف مقابل مسلسل دارد و آن‌ها را به گلوله می‌بندد. رسانه‌ها هم این را پوشش نمی‌دهند.
اگر مذاکره‌کنندگان فوق‌العاده ما بخواهند، بگذارید به گفت‌وگو ادامه دهند؛ اما من امیدی به نتیجه نمی‌بینم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67500" target="_blank">📅 12:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67499">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ :
سران ایران یه مشت آدم کثیفن. اصلاً ازشون خوشم نمیاد. کلی وقتمون رو باهاشون هدر دادیم. بی‌عرضه و ناتوانن. بهتره فقط کار خودمون رو انجام بدیم.
اونا می‌خوان رهبر آمریکا، یعنی من رو ترور کنن. سال‌هاست که من نفر اول لیستشونم.
باید سرطان رو از همون اول ریشه‌کن کرد. من این‌طوری به قضیه نگاه می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67499" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67498">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
من دیگر نمی‌خواهم با ایران سروکار داشته باشم. افرادی بیمار بر آن حکومت می‌کنند و از نظر من، این پرونده دیگر تمام شده است.
«از نظر من، تفاهم‌نامه تمام شده است. دیگر نمی‌خواهم با آنها معامله کنم. و اگر سلاح هسته‌ای دارند... دروغگو هستند... به نظر من، ادامه مذاکره با آنها اتلاف وقت است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67498" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67497" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67496">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ:
این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند.
آن‌ها مثل سرطان هستند و باید این تومور را هرچه از بین برد. این احساسی است که امروز دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67496" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
قرارگاه خاتم الانبیا:
هر نهادی یا مکانی که برای حمایت از ارتش آمریکا علیه جمهوری اسلامی ایران مورد استفاده قرار گیرد، هدف مشروع نیروهای مسلح تلقی خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67495" target="_blank">📅 11:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea62c3daa.mp4?token=D0k1ZaRKPz9kA3h-PyCps0sMEibNH8oXRjdFXbcC1yllxG8PVVokx2NxCmkzMCZmbjaxm8bWXGT8ZhrCAmZ8bi4ZhEkG_-s-HbVpx3zrJp4IFGtxTEKbIG0PoaJLZ8V7bfOJAN15GgniyRDgKeE9mNTwLd8pNLi_FYvIKzIcoHOF70q3ShEFFrBk0Q2-wvxomt83hbnjliv81gVRbK1WrtGQwjnmvd2oPl9UM0gLbuPt7jhhXRlNyFqELciTIL6xpceT1zH0VpBYxsCYfCer0uNtlrd2kWH5OUeGp3j_A_9hJq5AmrXV7GrQGouRZ2pCtHbL2o4jlGzxR2fUqb_kxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea62c3daa.mp4?token=D0k1ZaRKPz9kA3h-PyCps0sMEibNH8oXRjdFXbcC1yllxG8PVVokx2NxCmkzMCZmbjaxm8bWXGT8ZhrCAmZ8bi4ZhEkG_-s-HbVpx3zrJp4IFGtxTEKbIG0PoaJLZ8V7bfOJAN15GgniyRDgKeE9mNTwLd8pNLi_FYvIKzIcoHOF70q3ShEFFrBk0Q2-wvxomt83hbnjliv81gVRbK1WrtGQwjnmvd2oPl9UM0gLbuPt7jhhXRlNyFqELciTIL6xpceT1zH0VpBYxsCYfCer0uNtlrd2kWH5OUeGp3j_A_9hJq5AmrXV7GrQGouRZ2pCtHbL2o4jlGzxR2fUqb_kxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن رضایی:
مخالفان مذاکره صبر کنند، خود آمریکایی ها آن را از بین می‌برند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67494" target="_blank">📅 11:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67493" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=gaA-yIjKWkCw48MbHb9AcghKLc28DhqWVioikC_GOxsN-WnVtmdbJBKviJsAXD6HjNaCFqwdfPIoSq4DpEzRLEjTUjT12iRaDORkEY7r-E7VeSlarfY-OOJQg9It-kMQvpLRhjKCSZ5j539u0ByLNRmOeFp2az9TIYgcH3rzPU3ORxjBiAnGOFrJdxnFO8xWBz5UXbEu5fD0t0B5ESxenTdX_csTcrjLYOL1JENSxdBJUT5h95biCYXWkA9EsKoPt74set59pvQ07caV6FVtdyW4V3h93GEYGe441HtvjixBAduhj-MUn4zQBIV8WVJs0tCN-1GSl5P2zt57hF8Jzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=gaA-yIjKWkCw48MbHb9AcghKLc28DhqWVioikC_GOxsN-WnVtmdbJBKviJsAXD6HjNaCFqwdfPIoSq4DpEzRLEjTUjT12iRaDORkEY7r-E7VeSlarfY-OOJQg9It-kMQvpLRhjKCSZ5j539u0ByLNRmOeFp2az9TIYgcH3rzPU3ORxjBiAnGOFrJdxnFO8xWBz5UXbEu5fD0t0B5ESxenTdX_csTcrjLYOL1JENSxdBJUT5h95biCYXWkA9EsKoPt74set59pvQ07caV6FVtdyW4V3h93GEYGe441HtvjixBAduhj-MUn4zQBIV8WVJs0tCN-1GSl5P2zt57hF8Jzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مستند حملات امریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67492" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجار به سمت پایگاه هوایی عیسی در منطقه صغیر در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67491" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAPNdRB2ybEaE6Ce5L1poEQg9QHnj7vRbCJtzC5W9X2dHS0DKwdnwxJE9XivJYF5lshoS5ceyKZxHzF2rHUr_uzvkyQIdiS2uIJ4Ufrw4T_Ocl4FdjGITC6NKkPHN1poiHDQiqR1_zSaqc4W5iua5kpL8ufaA6O63C_Uq74E4w7NmDusvlQgKWUX9a3ydf6EpyKnvaOtRwko1JKdEV21uhf6PcguSMc__KielT4ornZYbmCl8LYF2uJBu6yLUIATwOJIzplWs9JSNbM5TZKrXs3ORY4JNz-RYIJBHik-Spk2cfE-6GZ3TeJ4uDCn_MV7tyqUPF-8MfZiWUteXDolbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف؛نقض‌های عمده تفاهم‌نامه توسط آمریکا:
نقض ترتیبات ایران در تنگه
تهدیدهای مداوم به حملات بیشتر
بازگرداندن تحریم‌های نفتی
حملات به جنوب ایران تداوم
تجاوزات صهیونیستی علیه لبنان
دوران زورگویی و باج‌خواهی به سر آمده است. این مسیر به جایی نمی‌رسد. ما تسلیم نمی‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67490" target="_blank">📅 10:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHA9Xdul5BEq3aKxmNCbYmIXwKQxoaaPK89meZMwhERNc8C3PnNyD0aNqZ_8_wwTy0JyF21uiisvgAakUKGvPGeB8ojU12G4c7sdUCKCEbQQeMrZmZyJsr0iHk1dCAjs6DWpEtWdwWK6xPpH-j1Tw7TQLQh8tio3YUD4oWQ2jfU2TbDhhNP7gP87P7WneXZyXQhq-IWzLxyzk-MB8P6PcRywS7IkWIjtIo8kBuCUXvR9OImCHw4GRzUZR2d__UuyumcW9pQRux319DoW2bpR0VDUc5e49rW9e3pWax1hMlQFZoiF1iLE3lwDXI--zaTmKIK-g5pFjXNx3wGA8oiq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یک هواپیمای آمریکایی مدل P-8A Poseidon که در حملات علیه ایران شرکت داشت، امروز صبح نتوانست در پایگاه هوایی خود (پایگاه عیسی در بحرین) فرود بیاید، زیرا این پایگاه مورد هدف قرار گرفته بود. در عوض، این هواپیما در پایگاه آمریکایی واقع در عربستان سعودی فرود آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67489" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در بندر عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67488" target="_blank">📅 09:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67487">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67487" target="_blank">📅 09:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67486">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9920364084.mp4?token=HaFAcfGkBZhc2YM82Uvr2Q5kD-L9l4R1n97e159Wx9vJxnmlfFcQeQ7QJXXLVx1DV9pj6nrPdMlaEd7De_gEdejE1ocybcVQalnCavqMl_1c8hO6qu0tD7cJZaqFt37tpmuUEK78ntVgz4etjuo2SyRxnSSCesgU2wNGJSq4pLo6QcNFZ1ZVFlmL-36Pvg59WI9fIekWoITSXoqXryRoAMsN-sIqhceAGyRGvA93i7NQwgtgnhQ23esb2QVEcYQjcVkpwvD1LmWPpZNSTrtBNikdYeTseig-L_ANZAmZr5xQ-AqN_nsFplsU5tWn0gfKReZ9j3FB0Hdi5AE87ohC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9920364084.mp4?token=HaFAcfGkBZhc2YM82Uvr2Q5kD-L9l4R1n97e159Wx9vJxnmlfFcQeQ7QJXXLVx1DV9pj6nrPdMlaEd7De_gEdejE1ocybcVQalnCavqMl_1c8hO6qu0tD7cJZaqFt37tpmuUEK78ntVgz4etjuo2SyRxnSSCesgU2wNGJSq4pLo6QcNFZ1ZVFlmL-36Pvg59WI9fIekWoITSXoqXryRoAMsN-sIqhceAGyRGvA93i7NQwgtgnhQ23esb2QVEcYQjcVkpwvD1LmWPpZNSTrtBNikdYeTseig-L_ANZAmZr5xQ-AqN_nsFplsU5tWn0gfKReZ9j3FB0Hdi5AE87ohC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی‌ها خطاب به سعید جلیلی:
نزاری به مجتبی خامنه‌ای جام زهر بدنا؛ ما امیدمون به شماست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67486" target="_blank">📅 09:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67485">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs1BgPLb5moWGfIACQ77QJFeIg8wkr91pHW0LjpHQAKaDo3QTaZcQCdimLp1vhhH7oOtrDAzh2nMKgj_Rdi2uTPYDiuY22aRNza3v95Z0cdJ56mciWDCHxkKLyJKonRAzHDZVlMdxoKHoSrye6wXT1gApssnx64NDrn_Z1cS9cT6_ecA-n_nCBMMjJ6IjWxJ4s0pb-9LifkjRFlcPHHL8s_e8a9spdG2jJqjTeFW3Ij8zUfIQDcOsZsDQlBl_mqsB9OOYOYxeJQ2xXvSFuPXGAGa6sfU9GrwcFOUp0bHfcRfCc81Sv7dcJKe1ziDB1n43a0sOrle0Qx5ZbHE--JPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه وزارت امور خارجه ایران در مورد نقض آشکار ماده ۱۰ از یادداشت تفاهم اسلام‌آباد توسط ایالات متحده:
کمتر از بیست روز پس از امضای یادداشت تفاهم اسلام‌آباد، اعلام لغو مجوز عمومی صادر شده در ۲۱ ژوئن، نشانه‌ای دیگر از سوءنیت، بی‌ثباتی و عدم اعتمادپذیری ایالات متحده است. این در حالی است که ایالات متحده، در طول بیست روز گذشته، بارها و به طرق مختلف، چه به صورت مستقیم و چه از طریق اقدامات رژیم صهیونیستی علیه لبنان، به مفاد مختلف یادداشت تفاهم، نقض کرده است.
از زمان امضای یادداشت تفاهم در ۱۸ ژوئن، جمهوری اسلامی ایران با حسن نیت و تمام توان خود، برای ایفای تعهدات خود بر اساس این یادداشت تلاش کرده است. با این حال، دولت آمریکا، همانند روال معمول، همزمان با نقض تعهدات خود، سعی در توجیه این اقدامات با بهانه‌های واهی داشته است.
وزارت امور خارجه جمهوری اسلامی ایران، ضمن هشدار در مورد عواقب نقض توافق توسط آمریکا، اعلام کرد که هر اقدامی را که لازم بداند برای حفظ منافع و امنیت ملی خود، انجام خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67485" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67484" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uf62mnm14c-ftA6-NjreAD5mJ_jC7mY3gvf95uRPoUz0g-wUSy3-ZooUB1RGcxoRCQkQXtPUaiG33JmfTZmWmrcO3aq8bZRfNRGSbDdg6voRtcl0Vw5vX6Tnfx98gv0zk7RJzc27yrrbnk6rmrnFR37ALklGt26tlSrYPUvOHG5SjwKmExkkg3vpWi1_EhHTZi7vxuzyzaVssqmtoapO8l5MO_EZo7EebbTpELd317x0LUI7nPVbC5thIWVtahwI6hxJo8ftCJLw1pPr1odtunG5zr-onG6NB0LJ2LC1UsaNvPez0vg985HfMnzLaP_Z4ree82KrTD6K1nYzTFrzCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67483" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phBDuJBZCu6A7h4Fgc6vAnv08yJ1Ewd3bpKUs5IrwAZv_ZQHQj9cEyo1Jwq09vWc-iNOCfiLKca6LXIe8KnjAqjPW9LX1qujG2yzFFavrBsyAXDywFw_1bS_Zcf8-EYO0LzAIoD8nPuczW_7CGza4c6PJp1ZNfGaArDU8DOZagWX9EQYFMCwR8Dn-CsfhRpV1NfOOvM-qx_9O8qjIjNg_77k4E3-AZeTtU1r0pgR1Bt-jCxTPwv6u9JdBZ-nwtrnoa8c2v2Q4VYyQv3G8ItCBl5uQF1IguNlBHgcxxZyeD9T94f3NHT8QP6kYMIMWLak3mOes3-bGjBr41POF4_I9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پسرا فحش میدی واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67482" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahut6sFnj1P5wOcwJRbUCCwXuos0X7IgU3qStLchnb0OwapPAbuXnwZ9JGQpLtiUM3BnLfauFKmDmd62NGVxsYa-6t1OgOrzIbM6gfmtoQxabrEt9Foos8lXJ5HbOK6pvCkjsPdboL6AnOabH7vIonHYVLH8GjW5EaPDhDf9vRBz3lIkXh5WNAU3VFY4a4LUvHabKPmSV6Ie3t960vA_5Jr4EEBWu5cBsofJ4bNvTV1gN3z9-FMpwVjEvQDdK4hYCyCMRyPxFScjNCekobrGmyrn6o16GYLJ6AsAAe6jFxfR0PmD6nMjy_BqB1dbsLmx4y4q3R5nW5XSkMliHQAmNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداوسیما: وضعیت بندرعباس کاملا نرماله  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67481" target="_blank">📅 02:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67480">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بنظر من زود تموم می‌شه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67480" target="_blank">📅 02:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSor60</strong></div>
<div class="tg-text">به پسرا فحش میدی
واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67479" target="_blank">📅 02:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDasK4KlENp-KZL6-Nsn3WYbviYkzEoYHaFqoL5ZK51OqwU1-6EGNRPzhWDB1XEs9Q8OlrG8ORHO8xvDpeHiGtVdRrfHNz-m1LaPoZ_4qB8WXjFB23xL3lvtJ4aMWdMxpyYHtFfVEliLrwaJivNBh-XjAtUeaJDLOxdJfBlebRRjOeuqaq56_9N7mIEaDkHFl9rwN1MgF0MnFp4IiZ-wN6ID6eyT-eOP_HbGBCgiRSH3GDnydvgfUqLsfAaBq_Di2-YX35qVFBrJgSdYFaglLCX6jVc2UwWXs6DW4t8Oh064Wt0YTp7sxbJHRPcaX16gcpCZE2-pGm6G9AI1sGY6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اومدم بعد مدت‌ها، و تازه متوجه شدم این ادمینا تو دایرکت فقط جواب دخترارو می‌دادن متاسفانه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67478" target="_blank">📅 02:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67477" target="_blank">📅 02:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67476" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67475" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67474" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67472">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=cdKsHAvlLod6RG_kjRMdzt5h1fNSDLHlhgDMNXtZgtrg0yg668QxfNKCkTeGumm7atlJVVpwNulcb4YEkQv05EElOyYs7Ti6_7GCnd8JqoV12z1B3qmm2Y1khuUInA0_QrpXvUzFDE9tzzjxB8vAyD3lfGQSkq2ghGF8pRzi0PLHosgWIx30i6zOpFH4NOdq7Dusoj0Nl2S8MCdzlF79_GL239s2ZF-1S_XGbN2QuREgVPmLvo6QjlLmsRm_rw4C9tYWZQOgb6vrJEdiDRoaARJiLuQbgj8JkqL3mEaGDLrc07Ol5LAg5K7X4TTSz79PDdEbOfRqw3t4gsreDnzFig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=cdKsHAvlLod6RG_kjRMdzt5h1fNSDLHlhgDMNXtZgtrg0yg668QxfNKCkTeGumm7atlJVVpwNulcb4YEkQv05EElOyYs7Ti6_7GCnd8JqoV12z1B3qmm2Y1khuUInA0_QrpXvUzFDE9tzzjxB8vAyD3lfGQSkq2ghGF8pRzi0PLHosgWIx30i6zOpFH4NOdq7Dusoj0Nl2S8MCdzlF79_GL239s2ZF-1S_XGbN2QuREgVPmLvo6QjlLmsRm_rw4C9tYWZQOgb6vrJEdiDRoaARJiLuQbgj8JkqL3mEaGDLrc07Ol5LAg5K7X4TTSz79PDdEbOfRqw3t4gsreDnzFig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67472" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
پرواز جنگنده های آمریکایی در نزدیکی بندرعباس در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67471" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
انفجار مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67470" target="_blank">📅 02:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwqMh22xWFCWpVVg4oJ7v9fJ3ce46WsxTbYytFzCC0YKpnSoyE3W94CmCn1WwEhbDU9Qp-ar-I7-eQLh-3PFHWFSh7Y520kVk2VuZomtPRsi2ZVWYCr2MniFZVVyHH4lbYmJ5KELA4u_Sv2CNakuWDnDkuUyCYGD3tpbK-oGyDvC0aj-vWoeTK8J8o45aURJI5ssjt6e6QtQV9tx6moOrPvnFMAKKtcYAREEI9JOVm-e7ncY9oYt35rnZHxS8NZX-c5fK_BbCI0qLB4lMqkriVGCKhISbXiqG3bsqMC-OViY9DwlOGOh6a0Q0gqtFe3NjnjL0XV0RnW-B0GrWd7zug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
مقام ارشد آمریکایی به من گفت که حملات ارتش آمریکا امشب در ایران چهار یا پنج برابر گسترده‌تر و قدرتمندتر از حملات اخیری بود که حدود ده روز پیش انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67469" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGINQXEwK8XJsVkgkd6KkyCEPDHzOiMHIoc7InyAdgEEpoKt8fb910A4cIwzW8CvGCPa9gZDf3C27RMEGbSPZRWGKk1yXXWfalTJrHffF8zkEZM8wNTVDTmD2wJbqEVIPNskB9QbqVYj72kmcuhXLlnMSa6UTSAIO5BxkrmwMX40OP50HQEvCUV4ovcAdmUJItCzt_DBFkEHHPhJAebWfVbBXk9eO_vk2QCyoS9tHdWDKIlpw4wGPzC2dztnZBdyAX8FIKKuxfh3uALANNNDzka-RRWT8a8zbRsRv0JGG6xfz4oKbjCYTrDEtKYg-dOwv7lsch6zm02skgULlCfNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67468" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
قطعی برق در کویت و مناطقی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67467" target="_blank">📅 02:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67466">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
انفجار مجدد در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67466" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67465">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=QbnzSYlyA67b6gXwMfQYYaBeLKJ6gZ6vxcjtm1OryN4vOm8mDHWv6oPPY9_XB_Wczc9Qpn4OezaYYcnsxIwggXzYwolBGnsAtTRPnj2C7sEJfW4Dlox9O4WDQy-KYI2oqxBQHcmkYdBMFQDf0T-Ae2Nkw2zFCyLE6NNsvIS3G2HdnFCxI9KGPNlVEeyYk26RcpfguURPehSQ9Zi8pW_-edxQ22ziAI_mspo4-AYYrIWFsJ_NXogZKUWZTl0zhrp_Tmo6am0aSU4_v1aN-e_S7Va7pirGqQIuIQIOnCFLG1eQnDs3pmPfW0fzYC_nhKdigIMsZsqJHZijvOS056pgBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=QbnzSYlyA67b6gXwMfQYYaBeLKJ6gZ6vxcjtm1OryN4vOm8mDHWv6oPPY9_XB_Wczc9Qpn4OezaYYcnsxIwggXzYwolBGnsAtTRPnj2C7sEJfW4Dlox9O4WDQy-KYI2oqxBQHcmkYdBMFQDf0T-Ae2Nkw2zFCyLE6NNsvIS3G2HdnFCxI9KGPNlVEeyYk26RcpfguURPehSQ9Zi8pW_-edxQ22ziAI_mspo4-AYYrIWFsJ_NXogZKUWZTl0zhrp_Tmo6am0aSU4_v1aN-e_S7Va7pirGqQIuIQIOnCFLG1eQnDs3pmPfW0fzYC_nhKdigIMsZsqJHZijvOS056pgBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67465" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiVOfU9xXr1tqOjS7VjB7214FkXhp4DTqRy-SBQL7Rcqo6MjtrHZh-Bi7z5HnsNpGgCiUGeKCCjVkDOiln4etPjx7RTBg09-SzO-vXq3zqQO9pFUN-14taF00rdTos8M6hlw4hD1tjZ4y6yjD-6GJPeiNgSpJdh4NKvihnXBXBXvnfKjaQJfAzDIRvBLvMYm1CHNqcq156BxTYwPsdi0pku-cmPe6-_7VK_inowvA9K5UB4j2gxBBk8R7AV-gvh0IznKdUxnMHBkIKiSPJ4xs5C73J3pf4-tVopIK4PUybQ_t5-2wEJyBKSCTcqOQlr5xdKtw7NePCl7gsY3ygFl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابوالفضل ناصری، عضو فراکسیون مجلس:
آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67464" target="_blank">📅 01:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
کان نیوز :
در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67463" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=tEvcP2Dai-nAYZQ_RKm8yLFr-GwFPDUSW42TrzpmR8G6oMsqjeUGo6h9tjrIVc1WRiK9BfKfLPC8vtuK6nHW5S3cvUW2S-Nm4XzJd7-WdaTCSt5sqlxUwVwD2ey5TgLaXdsggpga5sSrSls20BfARgNcALQNosrRCFrMP910tWzMIDN8ELEjcjmGabDBBVRoYFWvTO90gCbmfoIMB1q-JYsGsKIzAelmGzoD5ipidjjEuqCVP58Lqssqr_-MoDiEWPenuFTNGbLSwMOQ8xgj5FYYihdR01mmA5B7EPOBVG2eolcjdpVRPR7aW1YciSGEDrhdCatYmD5FiWwkoeaNTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=tEvcP2Dai-nAYZQ_RKm8yLFr-GwFPDUSW42TrzpmR8G6oMsqjeUGo6h9tjrIVc1WRiK9BfKfLPC8vtuK6nHW5S3cvUW2S-Nm4XzJd7-WdaTCSt5sqlxUwVwD2ey5TgLaXdsggpga5sSrSls20BfARgNcALQNosrRCFrMP910tWzMIDN8ELEjcjmGabDBBVRoYFWvTO90gCbmfoIMB1q-JYsGsKIzAelmGzoD5ipidjjEuqCVP58Lqssqr_-MoDiEWPenuFTNGbLSwMOQ8xgj5FYYihdR01mmA5B7EPOBVG2eolcjdpVRPR7aW1YciSGEDrhdCatYmD5FiWwkoeaNTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید و آخرالزمانی ارتش آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67462" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=DZx2OVnnkPsuoqKsRxDl3qPs_exKd_sD9r16znPOHvlTvyvgzHzIH3aU7w26k8P9liqONfPqDIC0o1KA3kYQhXeROFMs7otS2aZCy36060RRSi0HX00LoiEUmpwnVX-Go104Hu0yl12p--UsjeeDx-h6AjT-malWHblHkydvibgDAWO9QFABCV1_OKB04ITCtEaBc8O1VttDkK1Ov-kwDRiGSQmvkeuLFb8rdbxCAqVOqnncSOww4_gXXLK1s--B5tcSuVwSn8JYVbVt0xwhjRZNhn1w_lPo5-guIn9P3EWjAIirTPgUCtB6tnjh-CesixzToisOc9xxK71i4LT3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=DZx2OVnnkPsuoqKsRxDl3qPs_exKd_sD9r16znPOHvlTvyvgzHzIH3aU7w26k8P9liqONfPqDIC0o1KA3kYQhXeROFMs7otS2aZCy36060RRSi0HX00LoiEUmpwnVX-Go104Hu0yl12p--UsjeeDx-h6AjT-malWHblHkydvibgDAWO9QFABCV1_OKB04ITCtEaBc8O1VttDkK1Ov-kwDRiGSQmvkeuLFb8rdbxCAqVOqnncSOww4_gXXLK1s--B5tcSuVwSn8JYVbVt0xwhjRZNhn1w_lPo5-guIn9P3EWjAIirTPgUCtB6tnjh-CesixzToisOc9xxK71i4LT3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67461" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس سیریک و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67460" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjaEgtI9iWuNb6QDIZxHo1vXjq1oqvXLx_21QoMpYuuDCpKkQ1TdggN6p7raC-vOWilvumnT0fLvNDhvxOrVf1JHXFRawq3JHJdky__0-wRnoQCFns3o6hcCTUO0gr-MqWxwnqeq8CmBk5j3yawZLUkervi8CSSg_v4p1dZtv96wLWffh6h4bB8u6ufSVNGhkAOExBN1PpOFRTSg-ZIQTDxv_VLCa8T-i38KxvoyuID2LkZ9SMMi55SXXkfETHzGdXmpcR3BVZWWS4FzQMJ9eQSzdb7d5cvPZSyXmX-Bz8Ap3t3PuHtg66VY76M-zH7EHzHqcAGE685p0yPHZXAzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تحرکات فشرده هواپیماهای ترابری نظامی آمریکا در منطقه رصد شد که شامل برخاستن دو فروند هواپیمای C-17A از پایگاه موفق سلتی در اردن، یک هواپیمای C-17A دیگر از پایگاه ملک فیصل در اردن، علاوه بر یک هواپیمای C-17A از پایگاه شیخ عیسی در بحرین و یک هواپیمای C-5M در پایگاه Alhairates در پایگاه الحائراتس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67459" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761109e119.mp4?token=lteigOMCXhB5GqnhnbTgMIh9FRMV9ywTkV5I25Vq_H6xcUJJcrcQJV5Q2WXGKqxUWVuORMNKPI5p_zKCN6KHqQ-EGwPN95u3LFDLA7tqjigsc6nW0f6wrqr32lWRmNQzit8T22I-NUOmUyizd5os5gBv1Hq155mYSelSsg9-fMbTRGwmmzZ1x2r22_pnO2vtwcTG74Tzzp6Uw7wzlAZQJD4KYLtXVXN7E-ygFIuTeYDWVX5SJ63w_Pn5CK56VcdzKBu-aRHiOpjO4Mb7O2Nb2h6ME-5uYES81gqzYdfwSaQsRNPlbR_pjOg2lW8jeRbCOCn5MJ8Ym1NnYuCWZkf9tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761109e119.mp4?token=lteigOMCXhB5GqnhnbTgMIh9FRMV9ywTkV5I25Vq_H6xcUJJcrcQJV5Q2WXGKqxUWVuORMNKPI5p_zKCN6KHqQ-EGwPN95u3LFDLA7tqjigsc6nW0f6wrqr32lWRmNQzit8T22I-NUOmUyizd5os5gBv1Hq155mYSelSsg9-fMbTRGwmmzZ1x2r22_pnO2vtwcTG74Tzzp6Uw7wzlAZQJD4KYLtXVXN7E-ygFIuTeYDWVX5SJ63w_Pn5CK56VcdzKBu-aRHiOpjO4Mb7O2Nb2h6ME-5uYES81gqzYdfwSaQsRNPlbR_pjOg2lW8jeRbCOCn5MJ8Ym1NnYuCWZkf9tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بامداد چهارشنبه؛ بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67458" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=rC1AMe4mmfjPVx6PyzZ5UyxGLlrH04G_ushHUObxDsnPCoREdvXjrCghxWUoZMAtBzokTfE2lgUykZ41SRP60o5bUBfHhPUVtvWTAtR6NBfQDKuU_4e182DgybBtfM1PU-35b-9at9h_7mQ5E_TwtVPradyXx8UYUkFTaZE8IlDYrXYikuHpjmqSR29eZm49SoVPLZCXr-Saqgion0QkFv_VqvjjrmxlevkWRyR_NbvMbavMoiB4LkFUI5kAWONMpkVRqgwyRheR69YU39g9VtRhxpNsOrh6BZlVk2USlKm-qeFZ-FhLekH1HoZdqMjCMOgaSDxO42YTZqwW6nRyyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=rC1AMe4mmfjPVx6PyzZ5UyxGLlrH04G_ushHUObxDsnPCoREdvXjrCghxWUoZMAtBzokTfE2lgUykZ41SRP60o5bUBfHhPUVtvWTAtR6NBfQDKuU_4e182DgybBtfM1PU-35b-9at9h_7mQ5E_TwtVPradyXx8UYUkFTaZE8IlDYrXYikuHpjmqSR29eZm49SoVPLZCXr-Saqgion0QkFv_VqvjjrmxlevkWRyR_NbvMbavMoiB4LkFUI5kAWONMpkVRqgwyRheR69YU39g9VtRhxpNsOrh6BZlVk2USlKm-qeFZ-FhLekH1HoZdqMjCMOgaSDxO42YTZqwW6nRyyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما که نقض نمیکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67457" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=XY-KGONvwN4FIVLI-SXzE2efhGtfof_aVP1Qd2D49Xfx6HLA59lA-De4Q3j9ePfZ8AOu3vsUiidb2uE2THIbXKb-KzUOSkGyA2pC8rp-PNNHfMYVYze7Y8CfP1eNfBiP5L7xES_eI5QQvi_u4Q57yu6WEAdxpwXc6YO-xZJIRXm9od70oreWZxR7uwEehmOkvWcx4k125GRg2pl_BqxBGXWiZHdHnw9wXXT1lnkJUO813VE-nFUcEN4xgae88tDilZfJPlG-dIyJLTaqUraGZR6_AdAjRgEr_8H7nwaSWtkrkRaFI_7clwDU0AGEQPaR1fwu7m3LKlqJjjRMJWvubA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=XY-KGONvwN4FIVLI-SXzE2efhGtfof_aVP1Qd2D49Xfx6HLA59lA-De4Q3j9ePfZ8AOu3vsUiidb2uE2THIbXKb-KzUOSkGyA2pC8rp-PNNHfMYVYze7Y8CfP1eNfBiP5L7xES_eI5QQvi_u4Q57yu6WEAdxpwXc6YO-xZJIRXm9od70oreWZxR7uwEehmOkvWcx4k125GRg2pl_BqxBGXWiZHdHnw9wXXT1lnkJUO813VE-nFUcEN4xgae88tDilZfJPlG-dIyJLTaqUraGZR6_AdAjRgEr_8H7nwaSWtkrkRaFI_7clwDU0AGEQPaR1fwu7m3LKlqJjjRMJWvubA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بندر عباس دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67456" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=byJjXX-bftTP-YyrZ6vmEOUvScYionwRNZWk3LV7zdnc4--ltEJ_P6L5W4pMA1lfFfnsO4D8Mrnw4N0IF0XT-sub7eMirwgRgmv1yni6gxdtkxV0MKJ0s1F_-TVZdM66n6WnskbxjMnpMm5sIiktVwBOXckbQxlHoSkAweGVca4cFqhDDG4D3rlQBVdfbNNXj9n7cCMoLeAvuYoCJYo1gXFK6h4MHE93BJpXUGUt0DzgRdvbbT3avz1mgtzGE1bqKqZ4DoT0LhPVRPYJeZgRMorrjXFowazWeyeDfqa2Xbl951zbD-8saDSBPwUQWdoWj63Nonhvpqv5ryjs_5c_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=byJjXX-bftTP-YyrZ6vmEOUvScYionwRNZWk3LV7zdnc4--ltEJ_P6L5W4pMA1lfFfnsO4D8Mrnw4N0IF0XT-sub7eMirwgRgmv1yni6gxdtkxV0MKJ0s1F_-TVZdM66n6WnskbxjMnpMm5sIiktVwBOXckbQxlHoSkAweGVca4cFqhDDG4D3rlQBVdfbNNXj9n7cCMoLeAvuYoCJYo1gXFK6h4MHE93BJpXUGUt0DzgRdvbbT3avz1mgtzGE1bqKqZ4DoT0LhPVRPYJeZgRMorrjXFowazWeyeDfqa2Xbl951zbD-8saDSBPwUQWdoWj63Nonhvpqv5ryjs_5c_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندرعباس دریابانی
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67455" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال:
کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67454" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=ezftIgypbICtBNcpqTqav1qs9iKcBAZahBoq9ykKKQCxTBQI6yx05hd6l66cHFnpxsSVflVp5n_DgtzbLPVFGDkkU46pAO44F2P118gblt6RkrYG_D0VwHyf3i5Iec5aNRkED0leOPtbquTPuj7SIoABenUs4ZmgDrn_M-aKTibRPo8gLBIFST4J0sumGmGMwAj4_zP3TkyRRkF3woPLN1YR1grsVxIMnem5yF89HKCYhLQu3gBuiRr0v9FHttaa1l8EiV9-JElaQBEDuk0VeKkLXAoUDjputBSzPyYjv82IdzAMBioGErpXEZPqRord3QZSWF5bwDUtFfW7qfxQHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=ezftIgypbICtBNcpqTqav1qs9iKcBAZahBoq9ykKKQCxTBQI6yx05hd6l66cHFnpxsSVflVp5n_DgtzbLPVFGDkkU46pAO44F2P118gblt6RkrYG_D0VwHyf3i5Iec5aNRkED0leOPtbquTPuj7SIoABenUs4ZmgDrn_M-aKTibRPo8gLBIFST4J0sumGmGMwAj4_zP3TkyRRkF3woPLN1YR1grsVxIMnem5yF89HKCYhLQu3gBuiRr0v9FHttaa1l8EiV9-JElaQBEDuk0VeKkLXAoUDjputBSzPyYjv82IdzAMBioGErpXEZPqRord3QZSWF5bwDUtFfW7qfxQHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو ای منتسب به پایگاه نیروی دریایی سپاه در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67453" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vRsD8VPoelfijlPZRuiba2Bp8fVl7JLLpxAJjWSs4hLrCTLfW3IeTLnY6bXHC1aIfKnwQYnUm-NkbLVnE641keP434VpKynx50xJnV6zJEu-O16fcuyxwkfqa__Qb97ztCVU9bNTLIWk1mvNnbSkrWN9NvnZE8XHAEKrAaaVHpAUMN953z6tEDubbr8UD_d7ucDT-MjAJrnNAqgreKle3D8DjBsGaUYSU6z-N9NqRQIlIr9n5LTgi1Akzo2w8n4Oy0MV1843L-qVdrafS2p_C632EdKN91UQsNIkT4pXfeYzf8Ojgg1rsXirL3OX-Fq41V-iIWcM0oppWlnPwSKZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بامداد چهارشنبه؛ مشاهده ستون دود از سمت پایگاه هوایی بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67452" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5trVLUTeHuyEFwQfR6bNrulnCU2yInULTOHaNJvGs11UbdB_FBll41wgenDGRlT1EITJ8OTRHaPlnkwN-B1bXRFC6i20Pbq0MSeloH1_W_LimMC8bfWNELe_5KpuChFs34c_mPq5An_8s7NXWrkOUyD3PzfHoH7cGiDHcj0Il9fHDy3p_WSbWAOS5ru0NaSzEOMCKCxsUndoHictolY8ZXrdBMgMcG8b4ap7rNh9WmgT6c2CXaitYCCLOG0rEtY19Ln3DsGaG3m9VWrePjVu53s42-MgXnnFfNeIdzQincHSzM5S8HWAQDdVw2goBtz8IXoqqFcHwSzJ3Ix548GEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67451" target="_blank">📅 01:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naNlzEfVPaX4ebgZkCZSs3Y_QMkeDI2CwxC7-5UB-zCw8D9M5hiTT-OI8jShB_RSmUmlz1XkvImWpsEQlANxIGeG5nfKtq5j3_RWtORdeLtd9Ii_tLtXHvOslwFMkNl0wGLkiT4ntyQfDo8q-ikw8e8wDJwmVNmIxFVayAk8vTh2Fj1JPNUhuN2Is6VhFMzsAlns8ZzTKAhONe87g0MBqsCSELxIYrrQbNJ5epD4S4dMcTKScVqnGVeN1sLBLI3Wy5HL-wGfwuTGOVDTOZDPbx-eyLt_gEaNH2pvgIPWg5guCv-1B9Qw-GYslrJ0oVfUX0_RLgXqP7I_tXQdx4LM1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه حمله آمریکا به یک اسکله‌.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67450" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4rQW4nfzq7kx9Q9HVI8aaFet7cSECRZ9bj3PHZsruNTxE9A389CikvS80VsMJLEq7raUpM03iX8OibcAk4-BkFqhW4rXnmyIEERuDSG7O4iTwA4CNFsGpGA6C4skp92kg02FKo6JbnwlDI7AUuqgsYkgzjY6UEI603nsKjj0kmB6r9M9LLXE8pfWGhsFefHsoYQQJNwSDsf_rxfhxKFuhZx3oBJ8ej_cfPH4yEAwkllNv_pmxH2tSdHW857KShT2Vk2D8pH8R36ga-yvOaiEY-4xxM_OBza9sMgaiLuqAa5HhLQvYreobjmeI55cI8qmAf1ohv7Bit9EJk6URFJrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری منتسب از سیریک هم اکنون
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67449" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g3EWYV3RQ4MgQvePZI92ezKuU549i4djaS_0g9rGOTUiVZczD5tnrW7Qm7VUkeuJxdtBU7_tUcrcmq85YUhdWoKZqzfuodTPE8c46DT4LygJ5PfHV2VdUv4Ca7SUbFCC0reecoShixr438e35vLk0ypjenoaov6w5ZropWxK-_9cxaMmW6mB-lXAwo_H00Wlz-xZQJv4x-MB4COimvtXJGcgDzRTvTP_DPTeIT1QFFMDlmYOnzqANISFRQW5T-TSB6jWpMCh0ApMrYt-Z786g2DoipL1PBCyJYz941NKyZQLwDgWzgXZkjVAP_bmbY5SsutwlhaEV5snzOLMc7xbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسکله‌ی سیریک، شناورهای سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67448" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKB4C_SKwRR3EsE3m8n-vWGSgwagXGtyktGu9YeVkMEc-ckd9MgGOPNDaXy-w8s4lUw--kLIWh1SaYOfUCkV8JNw9eo_4JaWeKaea2gehOTBIIzw_HLGlsUpexSPqOIzCkc7LjEGn5hZQtKIPrt_6hFMJt49hM-N-_-EvN73KwM6h9n6UUoyZ0yaL3w2ecpSH7kPA_NEo3Mog04KJO1k3xgNOHKYMhz_9OF41_2mEVu3HCD5NJuaC1k3d0FfgConG6x6o1A5d-iFfpwuJi79QjefPJFj0ZkE_tXLoWjlT7BwYuPnHgmJyNaHD69FiCc4zgCJH8RPnFFXjUfh03mFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید آمریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67447" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از هدف قرارگرفتن فرودگاه بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67446" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=LI7qB_opzPCOy6T04HppjHrY-h6El6b5m4RZodVvxAXrdsdNi73LfG3yUGmB8vcYpBrw9nn-8Xve9h89JwWolPMCHiBKNomLAVkD7k5Joi3iw7AgYP3s4hOyhYE98qVbIxxEV2kiFYHYl8_vtkLYEu6d9feCOFldw9CQtancr0gn9uSfAXa4-DM-eMUIf5BqTsY2QoylS98pR2jwt9RQhruyOxljcRjD8fXiVmQQuMMr1dJrTxr3-Rh7RlsHKmTqzMjTZbqO3WmKLLHSdcIkNYCa696nlFpd3V_SOhtoRWvJqkcw4J-6mU5u969WzfMJvjJNqZ9ZZ1OhWYU7toeeXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=LI7qB_opzPCOy6T04HppjHrY-h6El6b5m4RZodVvxAXrdsdNi73LfG3yUGmB8vcYpBrw9nn-8Xve9h89JwWolPMCHiBKNomLAVkD7k5Joi3iw7AgYP3s4hOyhYE98qVbIxxEV2kiFYHYl8_vtkLYEu6d9feCOFldw9CQtancr0gn9uSfAXa4-DM-eMUIf5BqTsY2QoylS98pR2jwt9RQhruyOxljcRjD8fXiVmQQuMMr1dJrTxr3-Rh7RlsHKmTqzMjTZbqO3WmKLLHSdcIkNYCa696nlFpd3V_SOhtoRWvJqkcw4J-6mU5u969WzfMJvjJNqZ9ZZ1OhWYU7toeeXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
جنگنده‌های اسرائیل حملاتی را در مناطق باراچیت و بیت یاحون، در جنوب لبنان، انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67445" target="_blank">📅 00:54 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
