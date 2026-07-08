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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 21:26:16</div>
<hr>

<div class="tg-post" id="msg-67550">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FN5yFpzoZJKm-kptOyTpcxSgxgeQF5M-4s_17G-NQgRVkQVEgVway1RFMvG_Sj6R8S85oCprAywv88bMYblnLMal6vhwcHx3GQKmRl6bxYq5fv5FQMK9K7eTsxwQ10ZW_V9nVE_VoXPqMCCScS_ubeIDP8JNU70aPwaWJzgHH4dElr2DYpzu8H7_TXYdBKTHYNXcP2M8VseH-l6B8PqbCGMW1GJYGCnOOMOp7zXogOTj4UYn9s8mht4bzldX0PZuQHdJw3fZUke6toWIzYCrpIzs-xsgiNXZ2wg9qzVK-1USVgyF_po6m5ISUo2hQOx_6Ox91ifS5I8_nRUlMsysZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
عراقچی:
صحبت کردن با لحنی تحقیرآمیز با ملت بزرگ و شجاع ایران، از عظمت آن نمی‌کاهد.
ایرانیان به خاطر متانت، فرهنگ و ارزش‌های اخلاقی قوی خود شناخته شده‌اند. ما به بی ادبی با بی ادبی پاسخ نمی‌دهیم، بلکه با عمل: با شجاعت و با از خودگذشتگی فراوان.
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/67550" target="_blank">📅 21:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67549">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
گزارشگر: ماه گذشته، شما گفتید که رهبران ایران بسیار عاقل هستند. حالا شما می‌گویید که آن‌ها افراد بیمار هستند. چه تغییری رخ داده است؟ ترامپ: من آن‌ها را بهتر شناختم. آن‌ها بسیار عاقل‌تر از سطح اول و دوم هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/news_hut/67549" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67548">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/news_hut/67548" target="_blank">📅 20:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67547">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/news_hut/67547" target="_blank">📅 20:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67546">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/news_hut/67546" target="_blank">📅 20:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67545">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
من می‌خواهم این موضوع را در مورد ایران به پایان برسانم و با رهبران فعلی بازی نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/67545" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67544">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67544" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67543">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/67543" target="_blank">📅 20:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67542">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67542" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67541">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67541" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67540">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67540" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67538">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
ویدیو ای که سپاه از حملات دیشبش به پایگاه های آمریکا در منطقه منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67538" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67537">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67537" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67536">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
یدیوت احرونوت:
نخست‌وزیر اسرائیل، نتانیاهو، و وزیر دفاع، کاتز، حضور خود را در یک رویداد لغو کرده‌اند و در حال بحث و بررسی مسائل امنیتی مرتبط با تحولات مربوط به ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67536" target="_blank">📅 18:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67535">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67535" target="_blank">📅 18:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67534">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67534" target="_blank">📅 18:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67533">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67533" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67532">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67532" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67531">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67531" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67530">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ ترامپ:
به ایران هشدار میدم، دیشب ضربات سختی رو بهشون زدیم، اما امشب قراره براشون سخت‌تر باشه و حسابی بهشون حمله میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67530" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67529">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67529" target="_blank">📅 17:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67528">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67528" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67527">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67527" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67526">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67526" target="_blank">📅 17:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67525">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67525" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67524">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67524" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67523">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67523" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67519">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67519" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67518">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_fzl4NCcDIc0QpK0BxVSz93YUpE9ggkzMLVpDUM9ReIbXidx08jr_Dk0spD6sSkANRq7hG8wn1rVkA36nXddde47XWlIdJ1Ob68cUDRkhzRXKwC36b2Sh_cCyTAbhU4-jr0n1O3G0G1QmckNnsL0C_H1iY9PIIOqpu9RbfB_cG_U9gl9YKNG_H2-l2qMto0Is_M4vfUam5ZVHJeHR8cc8GR_hO4fZEta7qW9z7WN5mXU6rQm-hiErQhmw6ot-FFqTxfvHb_WFNr17GlSL050cGJt2uegew8uOK-CmMnjawJPVOMhL7W4y-fldAWZIxhnmon0HIEb2Z2N0j2hFKhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری هادی چوپان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67518" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67515">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67515" target="_blank">📅 15:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67512">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEoRnu0z-mjWbdv1M-2auWqRkyWqqBKSnl9OFjIOWKSiclWgKd0o-haaUtKnLcSWjdyS9FUq_XqfrqvIsXvR0xCpm_sNIK7cpSBOQMQmY3LwJloQgdsuVO3ggao5TPEESPOI0qb6v91CPGBv1j_xwz7h9LDV9pHLEdXBdRMP7o91Ndo39aPVJg5j4-ErYRxr7B5d5xagE5YDdYSiYTM76SJC-zSbLpPCgKbkV8UOEfh4tLOU7wPqWrQPpVZr1iBL7y-Jb3pPtASycFNqoTcENQwrgLSWwJhYAFFhTclsBJgHaDCha9S6lHTao_hjN2-kkmO7Mx3XkPLL9UOIPotkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuE8kcucSsobQbnZ4sdJsINlu5pp1J78ZjIgvbGpvrjc2QlMfbpnVbp5EvPTH2kHHYZvp8QR1Y23RlLjTWCOHTWfv8mWD2zeKZpjg8SFMuf2yaSZBvZgFfZrBQiRqQQQwqUV19DNN6WaJ1V9GJkWtZ_hwTzzA32XhTGeDnsDlmd3Bp9vYahrY-gNU1LVDxliOBCm7ncRaUrw9pytoQMWbOR61HHV5rxvO0Qt-wHfS82xBNbylL6-n-rbjrqteyVwXKX0CODAOCPdg-_m3D8i95is4XvsLmTBxiDE8cuHVRBaWGvOZRRRrwAkhjEqLkOGl2LbOzBLow0Zy7YsW3jBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hi8Xeb7BGty50k5lNjrLM8je8E0rYaevmopVcUNilOsnwDbTvUPVnDSsBQ6mm7Y0ay6dJI17eFY2Bi-qBxJrSWhnyYOWGa3y32aShvGGym30PjbO58y9qFWxnECCTjvkeU2-QXnkoKfDmUXltmxjDY9Q6HMYIgJ9qY_7K9RLpUqEmU2mgWgT-UOZe-zeXMtxs6vGhSpyEfEb6PDSft8t05NzL0B9w1W0B_0LFfKpHRrmiXCRpMRPtFW2Q0-yUy0SriythFoXY_6bfwbNw3o4tYkvduw_jVGHEuF5_S-t5ktBDPeSkcHGhuc93xIqOrRnuGHQ3j_5OwaeltO_TW_IXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
خبرگزاری تسنیم اعلام کرد یک پهپاد تهاجمی MQ-9 آمریکا در آسمان بوشهر سرنگون شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67512" target="_blank">📅 14:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67511">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67511" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67510">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
رسانه های عبری:
ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67510" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67509">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syMDemz1wKYaxwWqRMP5scx4j1LEt7VO5PeHG6YHMLPXPeeYiM43yJ9eXY4vjKMxV9MuQfz5Ny5lTf2DMt_r1NIdB2SQMQKPJzdWY_gB9YlNXg2Q-IFa05I2La6YJ6rchP0z0tlyHwhR2s4ZLs0wo76as5sQDHN3js3JHjPPpmpPwBNtC2HLt4n3_q7ijwMlw3bcseOOta5ij2UqNAvvHR_5e80kl5A_lpQQPf85pagYmAGNKbszDjLVKzmvve5VnykvK-OTv_6WJ7-w1n8RbLcY8KZPRfY6waO8FUmGUWMxwigf7vXlftDhOwMp9gi7jTlpuUn1rUG-V9Dp1iJqMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
پزشکیان:
رفتار دولت ایالات متحده به عنوان میزبان جام جهانی، همان سیاست خارجی همیشگی آن را نشان می‌دهد: زیر پا گذاشتن قوانین، زورگویی در برابر رقبا، ایجاد موانع و تقلب. این همان روشی است که آن‌ها دنبال می‌کنند. ایران چنین بازی‌هایی را رد می‌کند. ما به طور قاطع از حقوق خود دفاع می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67509" target="_blank">📅 12:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELU9RiQnl4Lruz2nDhjUXxfFXAhf3QsQ4dlrPEeBoPZuU7UpkjbpWfGGdGh0Jd6Zmx3FeSQYcURicDTXC0UEOiTZa9-M9Qwl78hbJxyJLXTo8Oa0NNo1ddvxqnKnysQk1D9bZcHca2T3v1zXoAKoogllMXH-_w7S9wYN_-czUQG0uwh-WHjqhSPbbu9PK8r0MlzdtyFx8Yt1pq9HyGOjPBZpW9_FrSAHE0Ci5R1AATPf10La08tKphq0uU_KjB5Afg1ROt7O-7ZE8T4rFMDblxjbimyWOGxcA9gv5lhr15zSiTo4A6l7VuzxxODTwBLuS4am1q8wAZ0bqLEyfdNHMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمیت سگال:
پیت هگست، سفر برنامه ریزی شده خود به اسرائیل را لغو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67508" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67507">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
«ما دیشب به آن افراد بسیار خطرناکِ وابسته به ایران، با قدرتی بسیار زیاد حمله کردیم... یک مشکلی در آن‌ها هست. ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. بنابراین دیشب خیلی سخت به آن‌ها ضربه زدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67507" target="_blank">📅 12:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67506">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=PeS4e2BMQf-GhfTWEqo70KhdQTlB_plSwiUT0o9DSVy9O35WvpTDX_CAnU9xMHMOsmp9Miht3jDI7b7mZvpQ2f6WQFo0BZomsliZQx_jh7gVkwzjqs6cZNo_I29Kh2xhnU70iEai_1sTpI0K9r1b9g76Ccw7Yjh5rp1KBE5Etjm9aY9IhjU7W_GmVY32DQxiG6V8R_b-61KzhjEZWTuoU5PBFrtaqBkW9Av9VPVnDY35i1GwiPYON65-AuvHEZsGpPLfnN7o7JLHAXg_Ntj2B-4EIXBWyVLBe-B0iEQd1VbhROeLFZrlyZUtoLx2M87PEm94iF5i9gbjj9VxDQri0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=PeS4e2BMQf-GhfTWEqo70KhdQTlB_plSwiUT0o9DSVy9O35WvpTDX_CAnU9xMHMOsmp9Miht3jDI7b7mZvpQ2f6WQFo0BZomsliZQx_jh7gVkwzjqs6cZNo_I29Kh2xhnU70iEai_1sTpI0K9r1b9g76Ccw7Yjh5rp1KBE5Etjm9aY9IhjU7W_GmVY32DQxiG6V8R_b-61KzhjEZWTuoU5PBFrtaqBkW9Av9VPVnDY35i1GwiPYON65-AuvHEZsGpPLfnN7o7JLHAXg_Ntj2B-4EIXBWyVLBe-B0iEQd1VbhROeLFZrlyZUtoLx2M87PEm94iF5i9gbjj9VxDQri0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره مقامات جمهوری اسلامی:
آنها دروغگو هستند. ما یک توافق می‌ کنیم. همه موافق هستند. هیچ سلاح هسته‌ای. ما یک توافق می‌ کنیم.
آنها به بیرون می‌ روند، با رسانه‌ها صحبت می‌ کنند و می‌ گویند که ما حتی درباره این موضوع صحبت نکرده‌ایم.
مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67506" target="_blank">📅 12:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67505">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=BmMldQABfH4CpETOxdis7hbhOe_gs2FONF22eICDBMOo2iNfa1GXsxaXYEdghnfKFt2fGhA_4Je92HBeyBcXeWbFBxmyKp_VCXXVty3XfwIBInQFHXe4Pvb8kK3FToE0WanByTsFsJO3qJLQkmNAYqq3uaT4ckV-mQBFmizkYt0koqDIg7_QFjapYcx3OA7XnIazLhmji1daFWSf3ipUPj-65eaURyOy14YwwGTKleibyBuisPRp9PajdqpypwuSeVxNDWXOnwJdION4bBlTxHGOX02niSZ8-t5-XZwBDU-jChSYI1VOYbVLBClEo-1W7saLTb2MTehdpjtPgimKGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=BmMldQABfH4CpETOxdis7hbhOe_gs2FONF22eICDBMOo2iNfa1GXsxaXYEdghnfKFt2fGhA_4Je92HBeyBcXeWbFBxmyKp_VCXXVty3XfwIBInQFHXe4Pvb8kK3FToE0WanByTsFsJO3qJLQkmNAYqq3uaT4ckV-mQBFmizkYt0koqDIg7_QFjapYcx3OA7XnIazLhmji1daFWSf3ipUPj-65eaURyOy14YwwGTKleibyBuisPRp9PajdqpypwuSeVxNDWXOnwJdION4bBlTxHGOX02niSZ8-t5-XZwBDU-jChSYI1VOYbVLBClEo-1W7saLTb2MTehdpjtPgimKGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
به نظر من، ایرانی‌ها ناکارآمد هستند.
اگر کارآمد بودند، ۴۷ سال پیش یک توافق انجام می‌دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67505" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67504">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=vQ9f9BKVAKj3OSs1PQKoijKEEiyfWDml7NWLw5y4AqSuKqUFhoZeGU6O6ZIaRZm6-VoG4rnn9AbCyg4Jm6pCnPJa656v1bOht32mKCGE7SUI1_95PIZZd8b3AKgBdY6d0FXb7PPWlxAHt96ui_6xbzryMnlx5UMouiuedtNtjsYjnFhK0xlwMvTiMdz3YOTzzTiiXZfOtSbrjO0_AgynM3VTGjifqqI0COk890a2lmf_7VUSbiT8z_BCM9P2_v-oKAmKBvt3qo7fbRjGPMqKRL4b5uNTFzezkx4AGYbySWPLj7wnLNq56gXWDFCceDBJX83bXCicz5BIJCilxuhgog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=vQ9f9BKVAKj3OSs1PQKoijKEEiyfWDml7NWLw5y4AqSuKqUFhoZeGU6O6ZIaRZm6-VoG4rnn9AbCyg4Jm6pCnPJa656v1bOht32mKCGE7SUI1_95PIZZd8b3AKgBdY6d0FXb7PPWlxAHt96ui_6xbzryMnlx5UMouiuedtNtjsYjnFhK0xlwMvTiMdz3YOTzzTiiXZfOtSbrjO0_AgynM3VTGjifqqI0COk890a2lmf_7VUSbiT8z_BCM9P2_v-oKAmKBvt3qo7fbRjGPMqKRL4b5uNTFzezkx4AGYbySWPLj7wnLNq56gXWDFCceDBJX83bXCicz5BIJCilxuhgog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67504" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:  فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67503" target="_blank">📅 12:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67502">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=DnVeq9o-gXXIIuk8kfnnuo_G0AmqgXL8XQtgRLY7jB9pNaG-av8pvCV-s4L3QQxORMcb5Hx5jWcAg_u8Dxso29g4Uy2QP7fsXEHqDgIBB_Zu9nmWWJZqftfgAmWboselYYBoudq8ZpMWjGrZUk92qmI8JmDjVEf2oxo0E5ojdRBGXCybZ4FtHH_CxpsMrtQwyvoOVYnS2RS4szWgG8mOKImQ2BRpO9kbU5r8cRGJ3o4KGfakjeb48aYDgOo_iI9tzqtVIvDrThN7adJpdJoplxlGshDJOmLOxj90JLOJgQCacG8A8qJve2Y0HBJ9bk5rxDw5IU5hs8-tKH1cTs0lZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=DnVeq9o-gXXIIuk8kfnnuo_G0AmqgXL8XQtgRLY7jB9pNaG-av8pvCV-s4L3QQxORMcb5Hx5jWcAg_u8Dxso29g4Uy2QP7fsXEHqDgIBB_Zu9nmWWJZqftfgAmWboselYYBoudq8ZpMWjGrZUk92qmI8JmDjVEf2oxo0E5ojdRBGXCybZ4FtHH_CxpsMrtQwyvoOVYnS2RS4szWgG8mOKImQ2BRpO9kbU5r8cRGJ3o4KGfakjeb48aYDgOo_iI9tzqtVIvDrThN7adJpdJoplxlGshDJOmLOxj90JLOJgQCacG8A8qJve2Y0HBJ9bk5rxDw5IU5hs8-tKH1cTs0lZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:
فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته باشند از آن استفاده خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67502" target="_blank">📅 12:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67501">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnDjLhggBE9vWao9ReZmjSkvYDKU5eBq799rsKJ1KpZSNELUjKmSL612GgWjjWbLBKYD4xfemBQf1Q-UfKx5r1QxUvdBvkzq3GBaFSFZ4gyv1PI_yHCLxV0cUYjvEzYa7jM_Fp_Fw6FbyUt3zyMRNDpxuEdRcU9LoOSzkn7HimWzpDDqt67WGCcqrX_gp34cqmO5WDhwmIg0xPLsdE0VKEtQEJBgqUUAJQGis-UtYrup_C7Wd57D1hpAXXSc-rErkdPQTQvnDGp15UuyGT59VvWy--x5F_BgxpVUA3oAOIZyL6B_IgBJJiuUar-V1MCd2-1qdKl-gken7_T65yoTyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از حرف‌های ترامپ، قیمت نفت ۵ درصد افزایش پیدا کرد و به بشکه‌ای ۷۷.۴۰ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67501" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67500">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=fHMiV7dU_UoWPwlVC0ILjHnN50CAKiEDiQ5EQM16yutKM1_I3CEsF3lCGuS5vm-cTrMitwkctrkPIr4eauSbrQzjPAT5oeffBirORrUxcexqK4hriJcG7Tk_ba8qD5o_ge8pUZgZ78c5J7y5e8qJzcCWOERh6GKRRzHELiIHrSi4l-3uEYKspxjC0F844-Iyy7JafukM3ucdWtyLCWboMyvNvW-cVbtUR44Ys1C6hkUT8FsEnXgVPPrDx-i_mDafI0XlKi9Ny8RT5RZsCejX4V-FAcSKOqscCmeByjo0PzVyD9GALEGCNK6K1q_GASWJPLKk5AeTOptFhoT_jUMVvgmyjFKFMEFTA_lNOISfy2WL3pYeYbdGNjiWCaSFJG0WQBO-GkElrhVEg-MFzRm9VuazrAXJvNHC6x-7vIUr1necummdAwYWM7uiDyigM1kJjHegyPDVdNV4s84A6eWGZ8SI7faiu1PoSOmqi6q_01pc4F9zSgKtv8eWGx55olfFYjSFVWWizHn0MyiQv_FaGkWv9qp9zWGHSI9wezm7kxwOtzXmJ4x7DqZy_1i-R6jSF4KfXP94tBQcKBQ9V7LrwDA3u6k0d3V4E_66FCsYJFx_GiwiOWqYL644QSFRlvsmLMoVKjvuDIIN7c4ry0AXhIp_ucyHVWyuypUF6X10L5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=fHMiV7dU_UoWPwlVC0ILjHnN50CAKiEDiQ5EQM16yutKM1_I3CEsF3lCGuS5vm-cTrMitwkctrkPIr4eauSbrQzjPAT5oeffBirORrUxcexqK4hriJcG7Tk_ba8qD5o_ge8pUZgZ78c5J7y5e8qJzcCWOERh6GKRRzHELiIHrSi4l-3uEYKspxjC0F844-Iyy7JafukM3ucdWtyLCWboMyvNvW-cVbtUR44Ys1C6hkUT8FsEnXgVPPrDx-i_mDafI0XlKi9Ny8RT5RZsCejX4V-FAcSKOqscCmeByjo0PzVyD9GALEGCNK6K1q_GASWJPLKk5AeTOptFhoT_jUMVvgmyjFKFMEFTA_lNOISfy2WL3pYeYbdGNjiWCaSFJG0WQBO-GkElrhVEg-MFzRm9VuazrAXJvNHC6x-7vIUr1necummdAwYWM7uiDyigM1kJjHegyPDVdNV4s84A6eWGZ8SI7faiu1PoSOmqi6q_01pc4F9zSgKtv8eWGx55olfFYjSFVWWizHn0MyiQv_FaGkWv9qp9zWGHSI9wezm7kxwOtzXmJ4x7DqZy_1i-R6jSF4KfXP94tBQcKBQ9V7LrwDA3u6k0d3V4E_66FCsYJFx_GiwiOWqYL644QSFRlvsmLMoVKjvuDIIN7c4ry0AXhIp_ucyHVWyuypUF6X10L5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67500" target="_blank">📅 12:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ :
سران ایران یه مشت آدم کثیفن. اصلاً ازشون خوشم نمیاد. کلی وقتمون رو باهاشون هدر دادیم. بی‌عرضه و ناتوانن. بهتره فقط کار خودمون رو انجام بدیم.
اونا می‌خوان رهبر آمریکا، یعنی من رو ترور کنن. سال‌هاست که من نفر اول لیستشونم.
باید سرطان رو از همون اول ریشه‌کن کرد. من این‌طوری به قضیه نگاه می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67499" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
من دیگر نمی‌خواهم با ایران سروکار داشته باشم. افرادی بیمار بر آن حکومت می‌کنند و از نظر من، این پرونده دیگر تمام شده است.
«از نظر من، تفاهم‌نامه تمام شده است. دیگر نمی‌خواهم با آنها معامله کنم. و اگر سلاح هسته‌ای دارند... دروغگو هستند... به نظر من، ادامه مذاکره با آنها اتلاف وقت است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67498" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67497" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67496">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ:
این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند.
آن‌ها مثل سرطان هستند و باید این تومور را هرچه از بین برد. این احساسی است که امروز دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67496" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67495">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
قرارگاه خاتم الانبیا:
هر نهادی یا مکانی که برای حمایت از ارتش آمریکا علیه جمهوری اسلامی ایران مورد استفاده قرار گیرد، هدف مشروع نیروهای مسلح تلقی خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67495" target="_blank">📅 11:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67494">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea62c3daa.mp4?token=K26GRLrM4aiQczdMtgsNC8ZO149RhOIkgN03a-WCakppJC3--Qo6sYtKJUbcpazulQVS-1rPvuH2sSmenHNFr7pvSm1WPdkuXSv8StOjSlbG3j2qhGYTj3sSKK9hAafnIa6Ys-8YN7Wkj3PoR17Ay448XySP_OZ1p6W8YUAghO-nvQ6Zs6YlzBeH5JoccSt96fJfwRWJL3KNpMs_Sc8ayP4YFIeXptYMybnVFNfPdNwOspF0VgVULqEfR7WjFF6VR-tYPMgWs6rPRjY1UL7N5t4BKk_BaH9ELJOgVofUZHvlBsgGPmqYqGHPCRrZVZ88Fk1gDwEYkQw1ppzTKajssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea62c3daa.mp4?token=K26GRLrM4aiQczdMtgsNC8ZO149RhOIkgN03a-WCakppJC3--Qo6sYtKJUbcpazulQVS-1rPvuH2sSmenHNFr7pvSm1WPdkuXSv8StOjSlbG3j2qhGYTj3sSKK9hAafnIa6Ys-8YN7Wkj3PoR17Ay448XySP_OZ1p6W8YUAghO-nvQ6Zs6YlzBeH5JoccSt96fJfwRWJL3KNpMs_Sc8ayP4YFIeXptYMybnVFNfPdNwOspF0VgVULqEfR7WjFF6VR-tYPMgWs6rPRjY1UL7N5t4BKk_BaH9ELJOgVofUZHvlBsgGPmqYqGHPCRrZVZ88Fk1gDwEYkQw1ppzTKajssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن رضایی:
مخالفان مذاکره صبر کنند، خود آمریکایی ها آن را از بین می‌برند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67494" target="_blank">📅 11:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67493">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67493" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67492">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=XUnnpPplkzDR_Q3WAY_643veSqGvdclXViUW3skV9f5he9bhxMg85xPP1nge2KFQu6YoF5ebbqOIIywt6ufiAYvUl-r3jj4JQbQsC5iVj5_rJMtLtbtA9zpm09SibK9lE4nuvKiiHzZG1EEKG-ulf4-yzMsPnWhwTGNgjK7P1lDyy6gXYSEeEQ9NHtN8uC2JWEc5pCT80oL2eGP_T77Iiasp9Mk5xu9TpKd4PR0wVmrOvrUn2GqpDyALTDZom921zL2beLAPynsfZS--5xgcaJFd9UnuSdAVaW8dTu9Ugs9Bx30ejaxaZoofYPKWr6hBaU-CsN2B226szGpcCHMQUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=XUnnpPplkzDR_Q3WAY_643veSqGvdclXViUW3skV9f5he9bhxMg85xPP1nge2KFQu6YoF5ebbqOIIywt6ufiAYvUl-r3jj4JQbQsC5iVj5_rJMtLtbtA9zpm09SibK9lE4nuvKiiHzZG1EEKG-ulf4-yzMsPnWhwTGNgjK7P1lDyy6gXYSEeEQ9NHtN8uC2JWEc5pCT80oL2eGP_T77Iiasp9Mk5xu9TpKd4PR0wVmrOvrUn2GqpDyALTDZom921zL2beLAPynsfZS--5xgcaJFd9UnuSdAVaW8dTu9Ugs9Bx30ejaxaZoofYPKWr6hBaU-CsN2B226szGpcCHMQUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مستند حملات امریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67492" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67491">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجار به سمت پایگاه هوایی عیسی در منطقه صغیر در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67491" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67490">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVQDEidMfx_Vtv6EPa6WQDiOmdxvw65aHLQ5R3eYa-ogBnEHg28NXKbaeEE5NwHgMRHVTRtX9zm6HkG8WS6X8BrdKAMuIyD7WyplO4JEcMsafKNt7OhDCErWC2icRttUfKW51PY9F-HmGkK_60Rp1Ed65iGe7nfWTm2q8VE-nORxrJoglukbnejvphMeFsB4k75M9B1LQ_OKSthelPfRCqdkssDyFtee6SqWSZZ4mHXkmm3nFBI_mQv5JMBJ2heA1d1LFlNkvHrq7PaUtF9PvazqVZ3NvktaWEzGdwGJCDzy7aPY_lTpAxysaPZKTP0bo-svT-7m20S4XO_J3PwJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف؛نقض‌های عمده تفاهم‌نامه توسط آمریکا:
نقض ترتیبات ایران در تنگه
تهدیدهای مداوم به حملات بیشتر
بازگرداندن تحریم‌های نفتی
حملات به جنوب ایران تداوم
تجاوزات صهیونیستی علیه لبنان
دوران زورگویی و باج‌خواهی به سر آمده است. این مسیر به جایی نمی‌رسد. ما تسلیم نمی‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67490" target="_blank">📅 10:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEpLpINU2Hf8MAOy21_PsejR2QzYFgb37brklFpUzflXeOfDw6SXdILYHs8IWYsNzylxEZQ4-E6SQVDxrdmBZuxfMjV3DOsZqoAU2e7H_g_fRwJpZ2DsMYvhz8QNy-fyvEOlBaXjaHUNP3TF4Mqq5sSwEX__16vR_eCGQCtBIdzIo_6acEU_pKsBMbnVytSAuj2wdKRAAxYQSG0uOi4YE-94KtQWEFu2uGZ0iqwXl6f5yzVQb5cagNvl2Dpe6xu-eaTGFP_L608765ZMQmAhI6dlYoxh-jt3W7jA4s2y_mmYg07q4Ee1Uqo5gtJe0Zj3yYDHyu7JOmVLd0YGxPqv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یک هواپیمای آمریکایی مدل P-8A Poseidon که در حملات علیه ایران شرکت داشت، امروز صبح نتوانست در پایگاه هوایی خود (پایگاه عیسی در بحرین) فرود بیاید، زیرا این پایگاه مورد هدف قرار گرفته بود. در عوض، این هواپیما در پایگاه آمریکایی واقع در عربستان سعودی فرود آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67489" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67488">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در بندر عباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67488" target="_blank">📅 09:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67487">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67487" target="_blank">📅 09:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67486">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9920364084.mp4?token=geWQAm1vbOvGXVeL98nkwdDbA4-OapItCxQQL-OBxN7p30fCgbzGni6Rd6gOLMACcQ0gQBT_AnxkejrnWuPT50Pdx72m0lmeL2kRnDwBuoG6wDXbqTgBuq9fegw4YcyiFqoxZkUJ9X5qxMHltRftOnf4p_w2n5ehzJ4MHRVJRJlBHlagiHrWkbIuqvg8VnDivUHN53nzZuVKsUgu-AyFnlC7bt3q0jfJdQm8wQuPADKkWNfsDXM54dFYBlaY9oKi3yUVOh0tI7rCIjT3iz4UGpEimYxEWIQqOEx0uagVxG4ZJTYIHWW5-JDe4ylr8srQuZW58rPv9wCfQVZ5LCVG4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9920364084.mp4?token=geWQAm1vbOvGXVeL98nkwdDbA4-OapItCxQQL-OBxN7p30fCgbzGni6Rd6gOLMACcQ0gQBT_AnxkejrnWuPT50Pdx72m0lmeL2kRnDwBuoG6wDXbqTgBuq9fegw4YcyiFqoxZkUJ9X5qxMHltRftOnf4p_w2n5ehzJ4MHRVJRJlBHlagiHrWkbIuqvg8VnDivUHN53nzZuVKsUgu-AyFnlC7bt3q0jfJdQm8wQuPADKkWNfsDXM54dFYBlaY9oKi3yUVOh0tI7rCIjT3iz4UGpEimYxEWIQqOEx0uagVxG4ZJTYIHWW5-JDe4ylr8srQuZW58rPv9wCfQVZ5LCVG4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی‌ها خطاب به سعید جلیلی:
نزاری به مجتبی خامنه‌ای جام زهر بدنا؛ ما امیدمون به شماست.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67486" target="_blank">📅 09:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67485">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbJMJ2Q43kxexItwQDqVlD2l1msC7sEezM7nDRBTwKvWCDkEbRqXPdUlqO9Ch627p4W7cAurIUsfPrMfMdeu2foiHIrAGZaSV1deriw0gKmzQNm2i8so2grs_Sm3vB-S1E3nokFJoFtRSORUz3lwXeb1KSOsUSOGq9U_0i5JuoJNnhmoe_VQ41H1E3CadFcy8wgFd6rFuE23TTnSVBofRUwEh0oLb0yFtkSfU6qz3dWIgaEdqgPeV-USAo1zPqKwpCnDnv1NjjevboccanTlWFbY4nhi_cIhtOONH0RKiHy02u_SxoyZ7rgWhPxvLv9go3Rc75zuqBpwFm3Nk-72AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه وزارت امور خارجه ایران در مورد نقض آشکار ماده ۱۰ از یادداشت تفاهم اسلام‌آباد توسط ایالات متحده:
کمتر از بیست روز پس از امضای یادداشت تفاهم اسلام‌آباد، اعلام لغو مجوز عمومی صادر شده در ۲۱ ژوئن، نشانه‌ای دیگر از سوءنیت، بی‌ثباتی و عدم اعتمادپذیری ایالات متحده است. این در حالی است که ایالات متحده، در طول بیست روز گذشته، بارها و به طرق مختلف، چه به صورت مستقیم و چه از طریق اقدامات رژیم صهیونیستی علیه لبنان، به مفاد مختلف یادداشت تفاهم، نقض کرده است.
از زمان امضای یادداشت تفاهم در ۱۸ ژوئن، جمهوری اسلامی ایران با حسن نیت و تمام توان خود، برای ایفای تعهدات خود بر اساس این یادداشت تلاش کرده است. با این حال، دولت آمریکا، همانند روال معمول، همزمان با نقض تعهدات خود، سعی در توجیه این اقدامات با بهانه‌های واهی داشته است.
وزارت امور خارجه جمهوری اسلامی ایران، ضمن هشدار در مورد عواقب نقض توافق توسط آمریکا، اعلام کرد که هر اقدامی را که لازم بداند برای حفظ منافع و امنیت ملی خود، انجام خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67485" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67484">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67484" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67483">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RdC2RKoJpoMzUGuunUjTbd_OgveE5h9LPxdGi2buRhk9VrOtpMwM7mmE1rGqfyohuX7eCsbGHfKcoR2nTH3jqbGskkjGRIr0x_vQn-Cvl3k1bcEQ13dt_XpzayARIJ1aqy9AK-LBBp9rGO396uQa995_Xga5ybjSIOMyMR_8kF5H8e0Di1p-H-LziKxDVOpN60C3R5VtCyfwRQ3aKEqhqhhoCJS35z5dT0TXvIl1GtiDuxZ6vQVRok-P9icKoEon-2rjaEuazzV2os4iAfZSoR_3S5Oh2nNSSSjjWNxWPTX6m8XmDg0ggxxf-zj1C51YRMih5TcvIRknxJt3p46bHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67483" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67482">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw4M-OYAcnOGDEBcvvLy7J1wEV_yeDQr4iQYzzFUvRBwGrZDPMEcND2bLddtsXEGrV9IgU0q1nvOETLy9zYBX2xdRgcAhm3TgNsewdWGlKvpW3FsRJwq6Gl7W_O4bE7mHKycD4AxmigEwC6Zw8RFJbBiHJATh0La5h_hw2agssR-oIFtMdUl4GHv_Q6gJg8kVtvv98dYFLPZhE46pEisRd6Ul-uvXeC0zQ5db-UY3L9pjxu6UKQLzssOZ3LejvRhBCN-Uxa8VZId0l0q02MCHrCHaplZr0R45G3rZjfqf3O3st4RzsE6h7wfnBSz2r-mjEbxq1RGKHxP18PgT0Q7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پسرا فحش میدی واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67482" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67481">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPR_l40eUcUIqZR4YQMaxqXl_qhs4Py2JJiQexiQG3ZzfHSadZ4mMZyR_qwuJjvmU_0P5GLrolU5UXt2yhuH8OMgdPLbF7ECmuiepZixaLGGyrM789jBiPaktYCCicsAnF9ydizobKU_ZWk_hp6seMTzNLu7suy0-wXNr7oYQqYxe5AcllIj6mDEslILhiKG8nsJ97fBYmtDVQI89gq42mJlO8Ektus-mLexBy85TRtVuMC-K8hbKQI9CXdBMxMD-br4cvmJQj7016JtsoenfkM884KHH7UEztiHAPCxbDQS7kkdNzeFp0P_0yYuWaQnwcZk68G5GQC7woU0CkmRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداوسیما: وضعیت بندرعباس کاملا نرماله  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67481" target="_blank">📅 02:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67480">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بنظر من زود تموم می‌شه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67480" target="_blank">📅 02:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSor60</strong></div>
<div class="tg-text">به پسرا فحش میدی
واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67479" target="_blank">📅 02:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBSJMCLWo31wMUuLDlkB5lLXYQcvKTHAwQROAJynnv0ikvPkV4edVndlBdIAF--SQKsxVgo3NIbkmTDWBQdzxGh-EFBvAoai3bxkTr_MmVKBkO06shlq7FXMMf-NXsQ88ZRERI0RGrAeEQLMt4DszTwDJInm1uGDrJ2gHWynb0Wha4RpPnvZZVEBhUUzIknR6TEmAUkTvXPsVVmcvpmjmuITrQFcZVm8TtwmQSj_uizh0Yg2JstULv-lyQ94TZtL15HH4IO3AlvSMd9udOqCqfwjXBq0ezPjSdTdK3daLyknFL7W0zWcwvOlSSr_gbD-rDs0mquuxOEPyfZyJ3dluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اومدم بعد مدت‌ها، و تازه متوجه شدم این ادمینا تو دایرکت فقط جواب دخترارو می‌دادن متاسفانه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67478" target="_blank">📅 02:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67477" target="_blank">📅 02:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67476" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67475" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67474" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67472">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=RFKWvpprsNs9F5MagqjRTRT0rYobCaD4V9-0GqiR2DnO44SFh2tZbkFtsKBMJFlHcS_ZNJCaa-uKoxbipR8XUKR4dekXDmSNJkhaqmJ9ibTAI8DpQrgWuE5qZQbVxKNyP1SapDpQbzPHDuL4YfhYe9d1T9Em5UyDQNa84fwuwNcEZNTW64Jmr5U3mwbiFs02qoqOMwQwv4SWIESJs2oGoDmsGi828aORSgzXlwedTWq1sT8EC7UPBKOsgr01jCqJMBq-v2ff9xJDzWYUbRyOyOJDVroFRxoSsYAo_aA-FPL2TpIJ3SY1Fd7w21hNz3796acaNVt4XXNkQDj8Ni-j4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=RFKWvpprsNs9F5MagqjRTRT0rYobCaD4V9-0GqiR2DnO44SFh2tZbkFtsKBMJFlHcS_ZNJCaa-uKoxbipR8XUKR4dekXDmSNJkhaqmJ9ibTAI8DpQrgWuE5qZQbVxKNyP1SapDpQbzPHDuL4YfhYe9d1T9Em5UyDQNa84fwuwNcEZNTW64Jmr5U3mwbiFs02qoqOMwQwv4SWIESJs2oGoDmsGi828aORSgzXlwedTWq1sT8EC7UPBKOsgr01jCqJMBq-v2ff9xJDzWYUbRyOyOJDVroFRxoSsYAo_aA-FPL2TpIJ3SY1Fd7w21hNz3796acaNVt4XXNkQDj8Ni-j4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67472" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67471">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
پرواز جنگنده های آمریکایی در نزدیکی بندرعباس در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67471" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67470">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
انفجار مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67470" target="_blank">📅 02:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67469">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFuvISZmA2KK08d7E3DiaIngAMyD3TNkGu6RjL29AAO3TQBqZN8IFGuhX3zKv6mb2j0rWPkoDLRIa9yr-_G8P3tgKPvKoI7vR4JfpBROy6h8RjDinCD2ol3jVM9n3w3aofzEng42ttU-jlTppHlV8hGiQXIukvyz4-VJBbrcDOtmHTV_Lb7OgR-allYTqidh-wpRGVcX99lUN5syxUMVq8ezitt0z5O7UJyzVWLiDMAyDW09D-1ul1v-Fa3ZPgcSnQBLDvxYOasku-AtumFlM74XmFHbP940WmA6og1FLL0gJYhhIRlDDyslHrdzXId3yAw5ka2RFy3dUbCXfgGRUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
مقام ارشد آمریکایی به من گفت که حملات ارتش آمریکا امشب در ایران چهار یا پنج برابر گسترده‌تر و قدرتمندتر از حملات اخیری بود که حدود ده روز پیش انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67469" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67468">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXt-v8MIu8-G-WmBcEJDzOCK-Q1XS7MS30ufE5kL5Qv05hkgfl9oYKkK3CxnkY_gQ3wbbI98zifYyIJXoG9htrpkQcKcwbJ_A7GVNRYbE2CYA_mw15g9e58_w4JVeNnB2pRWREtnZmqNGSAhQ_YstMvRr1g0OJICtQzytLzH137-Vjgt3F0Mwm2p5Q6h_OiHwJVZq04ykXwoH8RIxOMR1gbhZ1ANdvC_VOxue4JXoQI1Cfkzm-n7xNIXTiuibKIXk2gJdlKWqMlpOJhIZyTzm80wd1FLJh213rMtLlk_NfRog8ur-2w1tnGEu0m3ZkRoavU-vWzptPWA1_8MbResLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67468" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67467">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
قطعی برق در کویت و مناطقی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67467" target="_blank">📅 02:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67466">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
انفجار مجدد در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67466" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67465">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=qvIsHSzpE5GCwti0mUT2rmuA8IA3OpsPW6Y87YnAdAdVHsJ4QsHayiKuoYSQLSN-ULdZyFCNhMnbrpCFbyK_P_nQrTmLg3UDNi0qiQnkj_TA_ocGkbZE12PbwECuvqeFQfMSXCUN1wszFxuAm1W10J8GYZIDZYc92dbH0h1rt1S1RL7sdbR5kCv7US4VBQ9GgJZXsajMmY0eqp7M48kx1ZDRH0CdIvXp3jDjNALaYIReiTgWfzy8UwJpbhGf7_HegCX7-HM_fLW-2lgsCy2oCFnHGY5N6XueWjUsxxEsTd5M16E58csJidiAeArUxXPMPM9tAhmbv-moL3WjTaca6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=qvIsHSzpE5GCwti0mUT2rmuA8IA3OpsPW6Y87YnAdAdVHsJ4QsHayiKuoYSQLSN-ULdZyFCNhMnbrpCFbyK_P_nQrTmLg3UDNi0qiQnkj_TA_ocGkbZE12PbwECuvqeFQfMSXCUN1wszFxuAm1W10J8GYZIDZYc92dbH0h1rt1S1RL7sdbR5kCv7US4VBQ9GgJZXsajMmY0eqp7M48kx1ZDRH0CdIvXp3jDjNALaYIReiTgWfzy8UwJpbhGf7_HegCX7-HM_fLW-2lgsCy2oCFnHGY5N6XueWjUsxxEsTd5M16E58csJidiAeArUxXPMPM9tAhmbv-moL3WjTaca6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67465" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67464">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDiC-aKV5eEfxJ6UelxfpkUl2sTZvFBX04XE1N4wIYNwtmd3-aVF9QhDiQyv5ZP-kxJGyZOPXZ2m01BjoOgs1tJ_M_sk0i2htNZcpD1_FHEbeZLulVirnIM7qhLTWjJ-IQrM2hG811l4YDLRrKNTKddqUZ3Jc2wUuey9cnJP_bFAzcIWf4zXHdVeKYj8uTyKS_J04nd5A7vrJGkJ8xB3WZcTdPiADsONoT4AW1y5A74PHfDjAFEvt5OzZG2KNUilC4-IBhRnwrUllbDIJIbvfC71q1Pskj6Us9C6iwogrdGaSpfr1zAMTJgtyaBjrEYDmEPSE-Gj0vcm3sqXU8Kl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابوالفضل ناصری، عضو فراکسیون مجلس:
آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67464" target="_blank">📅 01:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67463">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
کان نیوز :
در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67463" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67462">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=Qrbo1yOJ8MxtvAa34V-BVsO_p5Yg-aBfvWzrVbMKupOSxnY3xvqQxnSoOMR5TH7g2KlGut3-rLFZWWkXqj__BPkn9WDwFsBp_mlnvahrcDIVDXiy1ehfuZWbn3HwKujfsYOBYlOfYNiArDJaOzKpwVePY9evqgC_RDGXJz1i5DfGhh3JNou2SpdVVu4Cv95F2nWrs0JlAFGheNtm8MyUnGqHhYMuynRfGtqD3de4DysU5vMFO4Nk5Zs0sCdED1ebGl_VqoxwqXSrgGIB9EXn-7yQmgBUHq2XNEjp2TFeL9tcBy1IGcdgeKlny8-QZct6Rt3X-u5_2EMk7hZUjqWuwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=Qrbo1yOJ8MxtvAa34V-BVsO_p5Yg-aBfvWzrVbMKupOSxnY3xvqQxnSoOMR5TH7g2KlGut3-rLFZWWkXqj__BPkn9WDwFsBp_mlnvahrcDIVDXiy1ehfuZWbn3HwKujfsYOBYlOfYNiArDJaOzKpwVePY9evqgC_RDGXJz1i5DfGhh3JNou2SpdVVu4Cv95F2nWrs0JlAFGheNtm8MyUnGqHhYMuynRfGtqD3de4DysU5vMFO4Nk5Zs0sCdED1ebGl_VqoxwqXSrgGIB9EXn-7yQmgBUHq2XNEjp2TFeL9tcBy1IGcdgeKlny8-QZct6Rt3X-u5_2EMk7hZUjqWuwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید و آخرالزمانی ارتش آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67462" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67461">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=dRxh6vtouzWN9gRTL7Se1G64Au8Vr7iTAcCZG2iQ7sF3LEvNT-v6nKd6vxEVPkLe3vIq4ouW_C3LpmqVgY9VWQqkt9ss1pTPQu7LUISvKj6eYZOVAMD3qJrz4oO_c_Rwf1vvjpVIWh6aYUBqzoCsanrv7NVNp4md9PCz6Y5xKI3cHdiVHo13SDwyIbcPTckJc4EMirNMpXQe31TgSWnkeCj8vnB-R9C3E-NwwQtp5HE9BrYaf0oy4bXKAu5yhQ3v8Rxr0Rt59xlfBJs8PggVHvLsREiTTwl0GO2s6i96Sb3jERJMSdTEUDGOVu6eO0Pec06xMhm4A3r7J78Uy2E1RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=dRxh6vtouzWN9gRTL7Se1G64Au8Vr7iTAcCZG2iQ7sF3LEvNT-v6nKd6vxEVPkLe3vIq4ouW_C3LpmqVgY9VWQqkt9ss1pTPQu7LUISvKj6eYZOVAMD3qJrz4oO_c_Rwf1vvjpVIWh6aYUBqzoCsanrv7NVNp4md9PCz6Y5xKI3cHdiVHo13SDwyIbcPTckJc4EMirNMpXQe31TgSWnkeCj8vnB-R9C3E-NwwQtp5HE9BrYaf0oy4bXKAu5yhQ3v8Rxr0Rt59xlfBJs8PggVHvLsREiTTwl0GO2s6i96Sb3jERJMSdTEUDGOVu6eO0Pec06xMhm4A3r7J78Uy2E1RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67461" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67460">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس سیریک و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67460" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67459">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh_hoehG1S7FVkVyJV4BF5iwCCitC5WbH3Zwfr2YYYn1Crba2vxNrhAeX4LC9Yffz3ByX85dRAVctazpgfOmG1ty_V6_ZaW9XWKxB_mJSvBDY4Nh_eVSPt5ku61SMJ-Exj9hp2ovl5K5JmntHul4wysoH_0TFsBDXdatdUxTcfRrkyi_ipzJfvUx58MJs04zr1sQ0ABjEj-Kt3LTIp1GMkwsbS5-bv8ONnzuebzbIfhFguqTzpK7NsGEaIiANcwAVQmxJXsGERSH9D-2ilEtMCqqDPBfIUSDYTGXLt2PvKi0ohQGWMXtZRMIsNBPF8y9uLkZNC7N1ZmMFdS_lstEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تحرکات فشرده هواپیماهای ترابری نظامی آمریکا در منطقه رصد شد که شامل برخاستن دو فروند هواپیمای C-17A از پایگاه موفق سلتی در اردن، یک هواپیمای C-17A دیگر از پایگاه ملک فیصل در اردن، علاوه بر یک هواپیمای C-17A از پایگاه شیخ عیسی در بحرین و یک هواپیمای C-5M در پایگاه Alhairates در پایگاه الحائراتس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67459" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67458">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761109e119.mp4?token=qk7iX9uEaXMArQk2AXP5V6L1yeJInH2XvXLsAz7tOpzC9uu7npb7TXT14m8D7-aAB0ZL5k4JAhb3hhhpBAUQKArMbQrg43MDS91nae598MmBPHNouwXHzZ82mqm5HSYRK3N4Ysr1wf5-PczqOkgAIG7rY8NG0LNeLRvB3LAg_CtPj11SNIfGpxuw0Y32ZgCS4M9uwNdyU-KAkojrStT9dM4VcLBoosZ8CrVmHpGt_I_6qDzys0P3X6Zcii6iAWVBjXJlXUgRFj33KE2QbUQoHn4dROv0j-z_f8HCRx7y8oPBkOXyG53neucQvMnSyEHIf_nKbazeFo1tSOOx2JtQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761109e119.mp4?token=qk7iX9uEaXMArQk2AXP5V6L1yeJInH2XvXLsAz7tOpzC9uu7npb7TXT14m8D7-aAB0ZL5k4JAhb3hhhpBAUQKArMbQrg43MDS91nae598MmBPHNouwXHzZ82mqm5HSYRK3N4Ysr1wf5-PczqOkgAIG7rY8NG0LNeLRvB3LAg_CtPj11SNIfGpxuw0Y32ZgCS4M9uwNdyU-KAkojrStT9dM4VcLBoosZ8CrVmHpGt_I_6qDzys0P3X6Zcii6iAWVBjXJlXUgRFj33KE2QbUQoHn4dROv0j-z_f8HCRx7y8oPBkOXyG53neucQvMnSyEHIf_nKbazeFo1tSOOx2JtQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بامداد چهارشنبه؛ بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67458" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67457">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=NCgtlyEAoHuykGcUmPeMBNW02GibN8UqpjbBFn6eKbRFPL6bedOeA6rL__CF3WPcp3jH-CEIDQNUyWUZXGcwv6ff5-aTKd7suusjOSzI3N89r2Ut84tVnsbywhadq9PPR7kZ3gF9YRI7bPbYEplk7_pUMpVnB17_RPkeRM46Xh32rQS710vGiCKrRFBZYAKYbgMMz9Xs2uZCeNWVnvqw8uaaaWBkpf6zEwT8-LRb2kWLgJ6sXRKRsSvNoVYnyX7Ee3VoDjgCYwyXkpCgHH8GbDywL3Rqa_mE9EW7QOM5ezoTvBBWAwT5zaXH5duigyfTjEgV5KkCzQ8vCJ-iSOV0GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=NCgtlyEAoHuykGcUmPeMBNW02GibN8UqpjbBFn6eKbRFPL6bedOeA6rL__CF3WPcp3jH-CEIDQNUyWUZXGcwv6ff5-aTKd7suusjOSzI3N89r2Ut84tVnsbywhadq9PPR7kZ3gF9YRI7bPbYEplk7_pUMpVnB17_RPkeRM46Xh32rQS710vGiCKrRFBZYAKYbgMMz9Xs2uZCeNWVnvqw8uaaaWBkpf6zEwT8-LRb2kWLgJ6sXRKRsSvNoVYnyX7Ee3VoDjgCYwyXkpCgHH8GbDywL3Rqa_mE9EW7QOM5ezoTvBBWAwT5zaXH5duigyfTjEgV5KkCzQ8vCJ-iSOV0GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما که نقض نمیکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67457" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67456">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=aedGuhGijUFffq5W0CzmAfLjqtMRLgcVsh6it_A0uh3Y9yme-wBSAZdB9XCmwJ-9N4xM9hJXjf2hA7xcZY4OWlcuNsDq6oSXl_7eZFKowkN5aOqAYBqtbCxE_NTrHjb6Ktg6BdgASlOKzqyFpY5_jixCl2Zx-_ed-V_JT83sDasesNCjhgzMeG5UserutdzA8Xe0wk3pPqXEMzFzCvH8wEdwO4sCCsUFMrk0hWdIEw4AxvQ2DVMf-DZPdfEjgFdip4rjBjg-ebrxtCUXQFsYn_2nAteMzIJwRU-XNEMYeZW4iwhnOnyvpMQQ0LicAGsYwGWyyOOv4jbYWFObg6UaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=aedGuhGijUFffq5W0CzmAfLjqtMRLgcVsh6it_A0uh3Y9yme-wBSAZdB9XCmwJ-9N4xM9hJXjf2hA7xcZY4OWlcuNsDq6oSXl_7eZFKowkN5aOqAYBqtbCxE_NTrHjb6Ktg6BdgASlOKzqyFpY5_jixCl2Zx-_ed-V_JT83sDasesNCjhgzMeG5UserutdzA8Xe0wk3pPqXEMzFzCvH8wEdwO4sCCsUFMrk0hWdIEw4AxvQ2DVMf-DZPdfEjgFdip4rjBjg-ebrxtCUXQFsYn_2nAteMzIJwRU-XNEMYeZW4iwhnOnyvpMQQ0LicAGsYwGWyyOOv4jbYWFObg6UaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بندر عباس دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67456" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67455">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=GpfVZlPC1nK8lbY9fkNdbfBrEHIN9Ic8n4QbbV8ucu3wjKAvbhl8_9A1UUEOVky-IbKFHY90CR3sTrFNlN63JNtfC1UKvNeUiRQUyFdlTx969BVcvTYE0pxeYCg-JkCpwUdWhZwvVxO_qA7hvyYg6Uq6RvOaZYkZ1F0hLvdocO3iZGpOAgPQqgb4jVpqhdh7Kpw7Pj_9RSdgy50tSoEVtTL_25aJkcOMjusZTl3vUaO2gKZ3-CSOs1uyySrU-Zyfy5TI-ZkVTZfg3PcrGfQrRyr4RdudCjzp93Ibpi1OmXxLsXoiz_fTuf1DtrTyxP0cRRD8j2KPNUxy6FSCVRDVOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=GpfVZlPC1nK8lbY9fkNdbfBrEHIN9Ic8n4QbbV8ucu3wjKAvbhl8_9A1UUEOVky-IbKFHY90CR3sTrFNlN63JNtfC1UKvNeUiRQUyFdlTx969BVcvTYE0pxeYCg-JkCpwUdWhZwvVxO_qA7hvyYg6Uq6RvOaZYkZ1F0hLvdocO3iZGpOAgPQqgb4jVpqhdh7Kpw7Pj_9RSdgy50tSoEVtTL_25aJkcOMjusZTl3vUaO2gKZ3-CSOs1uyySrU-Zyfy5TI-ZkVTZfg3PcrGfQrRyr4RdudCjzp93Ibpi1OmXxLsXoiz_fTuf1DtrTyxP0cRRD8j2KPNUxy6FSCVRDVOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندرعباس دریابانی
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67455" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67454">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال:
کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67454" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67453">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=unVTQbw6OcQiYDgyMNeNxtdGj9eB7g6qXNs_fbvh7OyyYBmAXrXgTe4RnOKE7QnX0lWd9BbDhMZw3jmSniFmC6cwvtYc83CEOF5y2VQGWX6BWPltZ6eDyj-heP93JRsis88fJZWLnz-n2F1021vN9mVp36sJUUKBDazUPsR_1z7hpFPmB5g-HjUwr3OUs7yk9NwxqBZ2rrIfbME0Neh0CA4oKPnluuiJ38cev_nkmx7BCtm6CXbTdqueyxv6rfQTegAm2bmC7dUmfB_lyzi9x0DufknDvKGCi65fhl17woCreL5lwm1yELjhSksWEE-Mp81fH33Nq2iZhKjxFe-blg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=unVTQbw6OcQiYDgyMNeNxtdGj9eB7g6qXNs_fbvh7OyyYBmAXrXgTe4RnOKE7QnX0lWd9BbDhMZw3jmSniFmC6cwvtYc83CEOF5y2VQGWX6BWPltZ6eDyj-heP93JRsis88fJZWLnz-n2F1021vN9mVp36sJUUKBDazUPsR_1z7hpFPmB5g-HjUwr3OUs7yk9NwxqBZ2rrIfbME0Neh0CA4oKPnluuiJ38cev_nkmx7BCtm6CXbTdqueyxv6rfQTegAm2bmC7dUmfB_lyzi9x0DufknDvKGCi65fhl17woCreL5lwm1yELjhSksWEE-Mp81fH33Nq2iZhKjxFe-blg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو ای منتسب به پایگاه نیروی دریایی سپاه در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67453" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67452">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hTcZyLvwPe9bo82-x9c4-sbEl3DDrcBs_LhLPIB1YmOyv6DtuVNlXEfNuWoIwyuIKeHvwuFBCLnjEYHl7zu6-G9ANxKVZPyV29sHef7sOqjL4R_Dm_XjHeRx-3IXINdASb-9_GFCB7Vr0HgWMsIxhZDCQlF3yUF1yMnGQD7mcWf7iTnC7SaWoH7-VcXiZ7tA0mU5dnGPu7F1Sn8zEQh_lIIg3PjTci60nzCaozyqGPCooOFawlYEBXdeUPOKY41oTFW-_g-O2hOBPjlg2X5IlnEKajcBh6KXRQ92H5T7HPmultORS335FO4F9f_GaTLeKWU1aQgpR5uP0IZJy2fItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بامداد چهارشنبه؛ مشاهده ستون دود از سمت پایگاه هوایی بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67452" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67451">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6btLrkdRT-TEneelCLFmd9rJlsypolXgI3RxRr4CU88a5ef3b_JnWU8RXDCH0CBCOrOoI6sqg0GAb4bJfoPBavWrPqmYodPWxvsUJLUo_nr6gu1vl5bTplxHnE_PjX-Kq_yKUm12tDet6q-04XYQjP16HBw-_p2rTmCdOH6YzEYkPZ4s_7iZ1nKG8eRRWEfh-45V2-7fWma5Vht9K6JXB3IQ30GSDsbgVoiMDkTZGbUjoLrp8yqlKmBjAg2aYEzYTx8A2EHAjiH8dkFvzbDYYH_ajxS-KpmFY-Mnio1R0k1x6_HIvYWBWxZibw48hvBCkt9Rc-dZ72xd4H0KeqE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67451" target="_blank">📅 01:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67450">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOwVaBgmMPV6a7pgYv49AaY8DyAAErch90zcJdAiKl2HSlhgqitYYUZR0GXaxGOETH0UYNFzGP6yrjKSZa6tw44HncYF1tOW_QuOyld5IG-MLpTLva2pkwGo43qq1iVKxk6qUIehus1Fq6HJDot0oj9_H-Exfp-kB2XThw0J-2gZgKZ9EhLcTrr7CxHrq0kTogelJ0nhNMfRwVpNN4Fr_t4l3mJFIJoTstO26VDRQQpBUx6mwyvbdAd7FC6f2luaVNuEPaBHKsB77KLZhiPJjaImHiW9VEby2E0xL0Rc5w3tvvqfMpv9jMJNdCGczxR7oXmpviCLiJkFkfyi6jiRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه حمله آمریکا به یک اسکله‌.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67450" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67449">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmJvs1UfJP-ihA62HP5f6zqPLlk4SdzPh_T4ckNPejXVLDsIqAyqzZZnxRajLrvOWsO98LxzHiJ2sXLuustCBwUOOwHU-JpJ7Fw61cui7umkIWDSlno0I_sI15s8Vpkcgrs0KQwXCOHSQ9u7NkUXXEbE-LUZ13c2CC08-7msdokN49FGivvgLVzppE8dFXLfNxpJ4_giekxHhVtz7aGRJWvK3VtoxGx6oCHThi7kidmzdpVZ2P3ausdS5qnmfIClvWEEDSeaPWGkwOGtV5v9MKUs4YqBFVUCJPjcxHAtoF6eesPCe0WA9LCLJUbUUBuCtGkaFEQoo48a_Sd3Bz3qbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری منتسب از سیریک هم اکنون
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67449" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67448">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KIPa7lr1WkhMW9ZAA6YMnVdEU5MhWIGum-SPa6hEDcs5n4BsnOtOl_tdxeK96uiKgDMG80jsQEwo-lDGCUhXY0G45TaggyZrL1nQle8U93SBKxkjZYZGgn8VhpMcepHMO6kdC2xfhdUExWhIzviTPtFqfVfstDl-FJgFJm-aV4EMU5ncjwwIPTvuKL7BQxQGyoyrsCrGtPmQexBM33JDZjPisOiCcEoPehSKD0R0XF0EDIRcdMLgyNM9S_Qx_vBtWWOJUOgm3uvy2gBqFJ_pqa_FmcitJwVeU_ddPFLrLz19gEjC2WVoBPzTN9VXhOwA0ZuV8BrD4deif1TBWKL2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسکله‌ی سیریک، شناورهای سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67448" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67447">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWWCKNKnxJ435BcGpZ6iDveWiiaU1pIq7sKwqBHwjqFmgFTmH5SJQ6UpL2nBsNu07VEYp4Pco_1bPRORzuubhGzGuaJlg9qPQ7z6EuWZ7e0NC1fSniUDzBYv3-h9OE_k6r8KEz6lNlHi_slh36i8rIx3sjzouBphpubc-vHVvuiAHZw6y3WO2n2P1I-DZSjirdPd86x7y0PZg7fYwYvMenKmVBZDwmbvNOwZrP2K1RG8cOzdhdqjO8IVraKyeTNjAUSwxW0cWVUYzkBUQgyiY7QIyDC6ud-pgnKYAtBQJVPPUwtjuCuqswBeVgjFQZKRtU7gTSveXBp4l3jhn9f5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید آمریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67447" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67446">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از هدف قرارگرفتن فرودگاه بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67446" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67445">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=RqVOvDBTDRvjGq-MmIgd7vTgCJ_c0Ea2yqcq-_5EQEwDmFKIYvOK14qJnb87QxkuVINnMFIPBTBdAnUC7mDqVf50kqqctRiprUrSI6SulhJLbMHHEfk8TKlvA_k6r9U7HfXMN93OpJEx2JSSqFI5jB4fmkhxUcD4Ukh1ca6n4ZaBAbyGiTNb9idwIlhAW3EvhxJNW8yF_pp0a7pF1T87H_ZTJKgnL_rDgq5885C-s72tsE-r637vmThRWd9b56xdzVlwbRVokrzs9IgvLBW5CnvU9YbquY1pqicQVGY89xmbJOdpitHIYpmMh8_mETSciMPFF2uJube79uYVcU7bJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=RqVOvDBTDRvjGq-MmIgd7vTgCJ_c0Ea2yqcq-_5EQEwDmFKIYvOK14qJnb87QxkuVINnMFIPBTBdAnUC7mDqVf50kqqctRiprUrSI6SulhJLbMHHEfk8TKlvA_k6r9U7HfXMN93OpJEx2JSSqFI5jB4fmkhxUcD4Ukh1ca6n4ZaBAbyGiTNb9idwIlhAW3EvhxJNW8yF_pp0a7pF1T87H_ZTJKgnL_rDgq5885C-s72tsE-r637vmThRWd9b56xdzVlwbRVokrzs9IgvLBW5CnvU9YbquY1pqicQVGY89xmbJOdpitHIYpmMh8_mETSciMPFF2uJube79uYVcU7bJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
جنگنده‌های اسرائیل حملاتی را در مناطق باراچیت و بیت یاحون، در جنوب لبنان، انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67445" target="_blank">📅 00:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67444">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ از ترکیه و بیخ گوش ایران، دستور حملات به ایران را صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67444" target="_blank">📅 00:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67443">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
حملات مجدد آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67443" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67442">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZScPzJ2k10yet1TZZEccmUcMhUmg5Fo2_Essu49aweK_4iSo0TX3I1QE59q6kCHQIiU4tPdcUttyhA3MH8JEKi3xR8tUCaqr9xD9j6FrRELud8LcpYtDDj88fE26CcYiIOQp4nWyFAlxdY6x0659zGwN1XEntqVLbAbkgWjz2gS86QvHE20JViaKuxK5REwxeqErwdUM4Z5AR20z94bPT0jLjYEGkCudiUVYrh6NWaSnlQvnYZvUx-5X6Hu9I_Ee5Ogt7TWGULpK-sJGRd_rxqkltSyJ8eEFBgTIhxUOUeQXXKH7vUxnETq4I11yvdfkBd5Wwk1mw3Kjqnv5GyrfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنند.
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67442" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
