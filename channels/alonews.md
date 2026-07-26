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
<img src="https://cdn4.telesco.pe/file/o9dZy5nQlUhSL222gtmk9640dRbnHsLVsUe3zxCjFF4TFWKqQp_lbfEj83AuxWBH7F-bqSoDBg3e_aDofWl_3soe6FsX_GxsDmhNyJ_Q_jggjpBsbNHt4jzZzrWlRAmqAKErtRZNKBGHQHrFr95JhJa9tTKvKOY75kUzqsxsdqdJGgcnH3lmm57gESSR1gmZ0P_LPjh594PNKQoFHInAmXSBTV5fPLgDhlq0kzxPopyHEh39las_X5QQu3vylqKd0-iNwwbiHrA8csi6qnfUqkBDRb-mo7R-TDkGG37_NxRr1alp4pXBtszy-gx6HL5RjPvvPSzu8aJ1RKW4Zi8NaQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 945K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 11:00:43</div>
<hr>

<div class="tg-post" id="msg-137621">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfGwrxIMzDtpF6g5cNdVnaHE6RzQ0IY_5qHGu4savkV2sX4nd3XmxnF1qS7Se8FZdUnezqBB8r3QZzS9ZuWfaRnWKgQW_KHiBAA-CzQ1T9Nijj7I4-Cd9grxuPWZjzQry1p3dM8f1C_38lAsf80izp_2Dzs5hHkb0UgM7ng0VQsYfAN7E3AA38CI6QX2JonEVTg5xo9jK_Xpbi7lzKdZTOT_KF1DPJv4QofsHE1EB_GFMviHlruywGBqJe5DR5e5ebwv22iUJwujv29CLnIxg_Bphzdad5ClIbFf3w9Eob7u0PWraTurBFiWzdoLgAmMI1GhwKfE1icZbtrRcxqtaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏
تصویری از تابوت استاد مرحوم اکبر عبدی
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/alonews/137621" target="_blank">📅 10:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137620">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
پس از نزدیک به دو هفته حملات متوالی، ارتش ایالات متحده برای دومین شب پیاپی حمله‌ای علیه ایران انجام نداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/alonews/137620" target="_blank">📅 10:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137619">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEXt39TK4SDZNBKU2cXOMyfkMGqRNJ5iaMRr6MciUW1wqWLExoW6GCkRl4h9gOMU9mo6hbZZI6ulW4lBYeJp3-I77DNLp04-CjG8wG_3fKfXTxo6bF57A8HHGRIiZdG2bXW2XmpzcW-F46hIW5Jol1rkaas4QOyTH2z-Cg8Nc4aeeP-EDBfoFZ7X_Fbmzam7Y6zTUD78sb3bRtFI5_yLv_6Ke3H7SoZxcHRq1IKt23h4LlQwrt89jxhFRpmD4ISrZw9SIYc5Jo1xlfbW_U5mziXjpzPtU57TXgsZU8EXaaoiFj-vJprBW5RRXTe1YbhKrAzQ3opUBxCHFVtyjrkOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
هرکی میگه با آمریکا جنگ‌ نکنیم بی شرف هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/137619" target="_blank">📅 10:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvMi_UKdN6KqqeyFZ9wDvSwlJNa89Dtk-W9a6TSK4Il-3ao4WpDoR8hLzhtMiSpkpRHkQssi2Ac5gubnUw68dyzgYNECcrkMXmVv1C2K55oc9kRuSsb5blg4nKMqoD-0Te4ucfWerUxYPpZYjYmQwkO3D5UCxpecJt-sY32P20lIcpSzg6o8UFhNAK0ALYM4NpAX4sn77pHvsvaC_8rJoFU2yuOgixr4vkygxELpymyJHvenbH77pio8FR8PLNLATU_83GKtQazk6kzDcy-3EzZGZGfNEI2v3Q0oLVZAtXkwL3pj1GPcTVbLzCDWXptZ2kzi2XeZzKhZSe7850EnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9E8-dCfd8yV3YZyeZIRvfNQyiKGjDJlzMEjs74u_yBGkgqIXp4FobVdyT7mJWIcpUyYL-Vje6DfZEjHdBJGXJuGr9Pgk-Qem1PvuaFgTxBZ_CZuhc9x0guAX5vMVeTY1CfpzdINWfkfFBnXSwLJChbNuL6lKY2lrDI0SJGIvhNBhyBbIwxuO2DOw4RpVQGVbZTGmlo2596a4dkwej3JsxN5Azgc_aZFgb5oQidD8opKlSBGRKC4BXT2qj_2hFDYjEDW-kFyvUnH74RRRl0fv5j2Mg8IJIoXH-HpqmeCsMZa6ufET-ct1Fa9ElwD_jnK02HZU2URUSrVv94bdYMCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVqsdPNFdK2k-0aQ4pu7oLxDWk2lRkB5kyDbsxe34A8M-ddj50MJbtn9qXE8ZZu7j1wpFdaljRYyhfvRKE8u3fjzSGyvJW7SOYVC5uXxWhB8AXH6lddCGnj-k58j1Bod0WvKfY_5s5PX-xM_WkHIERMIe31oYWzsbet724Wv_PdjOKRbz365biiSDufSL5Ktb_30oqfK8PzrRt86a0xmg3uFhQDqkxI8jQClLFuurhr7q9C3Nq4s2rKp8JwNbtjG3I8zZGcPoYYbfsuS6eyKg0Dv6bnovGuFkBi9kx5YiBRgr63BsHylQr-fu7GvZ2yqdSq9Zj2wjtPUP5ydQyIDSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بنادر کویت و عربستان خالی شدند
🔴
تصاویر ماهواره‌ای نشان می‌دهد بنادر کویت و عربستان کاملاً خالی شده‌اند. یمن تأسیسات نفتی عربستان را بمباران کرد و نفتکش‌ها گریختند. مقرهای آمریکا در کویت نیز هدف حملات ایران بوده است. از زمان لغو تفاهم‌نامه، کشتی‌ها به‌تدریج کاهش یافته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/137616" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137615">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6cd690f3.mp4?token=pgpKG7xAGt2G4kfyWOoQ7j_a_klknHpcRaBkaQp_vzMQ6W5Nel6j2kQ0a60zg2g9wZSzNK0AkdgHZ8QqVz0y50oEjnyy1eExxKI8X3qElZLs6QsuqrChIj81RG9KrbhfP2UB-aP4mx-EnpiEJZBpXy1pv9n_Ey6XxsfNpd2SXw1M0p4fR2T7oYOUU57gAsqQ3ywrzAr-69s_e_BHFk21f2VE0_vXaQjn1SRHgEGj4H7YdM7sggI-4f9aD7iRZ-bk-HIBtnfe4Vy3AJTkC0tNc3mT9TMltQN5poyK0xhoRLoMI2CLFRgy2EVLCdMx30Lq1dqNlw4cF0aflIgq_tYyeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6cd690f3.mp4?token=pgpKG7xAGt2G4kfyWOoQ7j_a_klknHpcRaBkaQp_vzMQ6W5Nel6j2kQ0a60zg2g9wZSzNK0AkdgHZ8QqVz0y50oEjnyy1eExxKI8X3qElZLs6QsuqrChIj81RG9KrbhfP2UB-aP4mx-EnpiEJZBpXy1pv9n_Ey6XxsfNpd2SXw1M0p4fR2T7oYOUU57gAsqQ3ywrzAr-69s_e_BHFk21f2VE0_vXaQjn1SRHgEGj4H7YdM7sggI-4f9aD7iRZ-bk-HIBtnfe4Vy3AJTkC0tNc3mT9TMltQN5poyK0xhoRLoMI2CLFRgy2EVLCdMx30Lq1dqNlw4cF0aflIgq_tYyeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چمران: در صورت ادامه وضعیت هزینه‌های ناشی از جنگ، ناچار خواهیم بود پروژه‌هایی نظیر جدول‌سازی، رنگ‌آمیزی و حتی آسفالت‌ریزی‌های غیرضروری را از بودجه حذف کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/137615" target="_blank">📅 10:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خبرگزاری صداوسیما: در ۲۴ ساعت گذشته نیز ۶ کشتی پس از دریافت اخطار قاطع سپاه، مجبور به لنگر انداختن و پذیرش دستورالعمل‌های ایران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/137614" target="_blank">📅 10:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137613">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4114548394.mp4?token=vQ3UXVnd2UFpf-DK9kHb20MGRONInIFZTVif9_DqLZ2kDluhlb2jhrfPr4O_CCGMue__B9hcXwlslPHuFYwxur3Ef_xBIAkCbyY3yRoI3SUHNcIWXj64loLul1U715z3DyhhKKqj8d4GxELjoxeRyPpXfWjfT-liKPggszYSKp8W42lRz8APiycliLPxPTTOd7w00FYxsfal15CjrllrKO_wgcNG_BLrtjbyEi8xPsK-t3Mm5E1n-dIczW2hcx_cXcx7OY5nZ4q2shAt-za6tIjt_6o-9ADAzckKhiJ2s9J4YEXy7sDBa-5pQi-TQSIoC7LeWuqGiUzwXSBo80yOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4114548394.mp4?token=vQ3UXVnd2UFpf-DK9kHb20MGRONInIFZTVif9_DqLZ2kDluhlb2jhrfPr4O_CCGMue__B9hcXwlslPHuFYwxur3Ef_xBIAkCbyY3yRoI3SUHNcIWXj64loLul1U715z3DyhhKKqj8d4GxELjoxeRyPpXfWjfT-liKPggszYSKp8W42lRz8APiycliLPxPTTOd7w00FYxsfal15CjrllrKO_wgcNG_BLrtjbyEi8xPsK-t3Mm5E1n-dIczW2hcx_cXcx7OY5nZ4q2shAt-za6tIjt_6o-9ADAzckKhiJ2s9J4YEXy7sDBa-5pQi-TQSIoC7LeWuqGiUzwXSBo80yOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید:
"من به مردم آمریکا یادآوری می‌کنم که چه کسی باعث بحران توان مالی در این کشور شد.
🔴
این بایدن و دموکرات‌ها بودند. رئیس جمهور ترامپ از همان روز اول برای رفع این مشکل اقدام فوری انجام داد. همه این مسائل تنها در صورتی بهتر خواهد شد که دو سال دیگر با کنگره‌ای جمهوری‌خواه فرصت داشته باشیم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/137613" target="_blank">📅 10:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137612">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
هم اکنون حداقل ۱۳ فروند هواپیمای ترابری نظامی آمریکا از نوع C-17 و C-5M در حال ورود و خروج به خاورمیانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/137612" target="_blank">📅 10:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137611">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
امروز؛ احتمال شنیده شدن صدای انفجار‌های کنترل شده در شهر بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/137611" target="_blank">📅 10:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137610">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwOuwDvOaKDMDGQGV72RVnkXsK0ykhLmZSuWRWZ-YffCBy_ezZZfNMGKUl3gt9KtxSOI4JL8rG22KkaRi4yE_bfttYVCFy4k3EHG8A1JWBWRxczrmf3fW6Yin9jfRC-e_Z7MLkzSpXD42QYLbXZEHgDmEdVVrnPbZ4oTvmHlig03jLKi-jsTIQ0bwNttkHm7gXZK-5gktzXfsIm8ajzafrgx2ZW6JW6e6rLmplQdxtX8VSZHFeo6TydTOLmLeWGbXuoxxFvkiT__zF-13R7FSuvqCvjYv58Dnl9IO2ou-VkA-BhRBOg344FwoyzxBImVb1Lq6LVNkmaHsmXZKNrogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در حال حاضر، ۷ تانکر سوخت‌رسان آمریکایی در آسمان خلیج فارس در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/137610" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137609">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
انهدام مهمات عمل‌نکرده در پاکدشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/137609" target="_blank">📅 09:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137608">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سازمان پخش اسرائیل از منابع خود خبر داد: در پی تنش با ایران، محل برگزاری نشست کابینه به مکانی امن در زیر زمین منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/137608" target="_blank">📅 09:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137607">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
شبکه اسرائیلی کان :  نتانیاهو فردا به واشنگتن سفر خواهد کرد و روز سه‌شنبه با ترامپ درباره موضوع ایران گفتگو خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/137607" target="_blank">📅 09:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137606">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhnjhEGadDfSmFRUlGWf9gkpsYmxjQDx-l4KrVcKHMZAGnt8PWy_6awR9W654zU18kPmDwOiDRS8idjxW0L3gyhxdQ8wlgKaHNxNykbFDnmUblOpaYgkLNIxOhpEqlb2Qmox2mLqZ2zL7lxxfWIm5VugS08estdAIXb4DW-UUNZYR0nXvG-u6caoh_rkAjBj74J8ICI1omcbYpCO9iDgWoWhyFfBIDj9Kgo2y5ZyfL6QJQqh_e2X4ZLbMSJ2cVtRRBwbTcmWyAiHrK4FLWwocKOjUyoK8UkbSv9sQ6Y6AfCmPOzt72vCVwe0KxIqxBiAujG77s5naYFvI5yqr_VmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌بی‌اس : مذاکرات عمان و ایران برای بازگشایی تنگه هرمز پیشرفت داشته، اما به زمان بیشتری نیاز دارد.
🔴
دو منبع منطقه‌ای به سی‌بی‌اس گفتند توقف عملیات نظامی آمریکا با هدف جلوگیری از اختلال در تلاش‌های دیپلماتیک جاری صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/137606" target="_blank">📅 09:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137605">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6gG1Igt13WWlgztPqUOWdMbg2dR7ybH9S-sVF2W_-k-We1mBK2l9XOSZZq34qhyDN1gusiZ9kjgjdkAfZao1bVUbj9rk0cRpRvf4udfEONJOz5wWxHwlRaL6-ovab-ic-dWsWd9eGgqee85dE-atSgJbto09tYTvMVDHZleYyw1bL7F2qmTYSD8duYMd0_zZ1ceqLLOpWicwcj5L-ziFktoCxnm5bZqQuV4Cw6yzv8DOjAliHk3r4vRvI3xoOIqsLgMa16AecfjLzQoAH-JOf6UMF6X2znKuF5AK5eXi3duSVEjgGc-I_5RVFUNlSOPQHe73NFFN90laNE1UKviUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقایی: تغییری در وضعیت تردد تنگه هرمز ایجاد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/137605" target="_blank">📅 09:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137604">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فرمانداری امیدیه: احتمال شنیده شدن صدای انفجار بر اثر انهدام مهمات عمل نکرده، وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137604" target="_blank">📅 09:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137603">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی شرکت آب و فاضلاب کشور : در حال حاضر ۶۳ درصد مخازن سدهای کشور پر است.
🔴
خط قرمز وزارت نیرو جیره‌بندی آب است و به هیچ عنوان نوبت‌بندی برنامه‌ریزی‌شده آب در دستور کار قرار ندارد.
🔴
مشترکانی که مصرف آن‌ها از الگوی تعیین‌شده فراتر باشد، هزینه آب بیشتری پرداخت خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137603" target="_blank">📅 08:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137602">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGE-_9p9Ez_XwBj_NmEz0poik9Mh51bz4-DYQfYSwqzdHOVQ8jFxkDWBoHYKMit56fkQUhZsN6hXyENKjluuMBv6WLu5SjqGa4VZIBQJl5ceNDzvsqJ2evWiN2DiWcMKM3tGLpnbMS2LrX9bJvw6TYuyjSeVZdLGXN9oS3ht76l-PpObY8vZ9TjYSowKZEke402TQGgXNLpUzs1mxT8VyUsdKIQUk1BO1yWxbMM3dEUGqgJDY_PyHJaa9cHCXvZAocVVCm7F1AAjupjN12fanZYf-8_8E-emzZDjinbUHrBlRJAKcsiWivYEiZIuPMf8gMCdJGaYUl21TPRYulfL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ترامپ قصد ندارد تنش‌ با ایران را گسترش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137602" target="_blank">📅 08:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137601">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: نتانیاهو فردا ظهر قبل از سفر به واشنگتن، جلسه کابینه امنیتی برگزار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137601" target="_blank">📅 08:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137600">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در حالی علنا از حمله علیه ایران حرف میزند که مخفیانه از مذاکره کنندگان می خواهد به مذاکرات ادامه دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137600" target="_blank">📅 08:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137599">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-z1ntoeP45mrvlz_7NzQy-iQEtfklBnR4tNEgqgOe3zXc3KWWMdFA__7i5GqKZ2Bx6y7On-x4uA7mQxJmHyyd74IDerPbeno2WpeXDJNSc7WKheTFPrTGuq_iHZGBvXquVxM1y-ZVW1N568NRurFvFs_3TxWi7LI8z14oWUdVnDiyOaMFapPoDFRFDMQMB94mOq25AvkADvIUGFVwVlBwfl-qX29hMu5gbCqfeE4dVRg-BaLljs5y_S3viDhG1s55NB0lQuC4jA6T3ildiIxJaOsKJwY6wj0qYRGFHkBTks-_3CWbuiBSbROobmQKydu-AY0LxtcvjnKUFgXSThnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
سی‌ان‌ان: «جی. دی. ونس» معاون ترامپ و رئیس ستاد مشترک ارتش، در نشست روز جمعه کاخ سفید، درباره ذخایر مهمات آمریکا ابراز نگرانی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137599" target="_blank">📅 08:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137598">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb72TwlarWlVf4DknPP4zWYU8Utwm3KRMBKoD03a2U9CK9LqMYyRi4GuLoR_7DcFebSwtUK4c0gjpRTX1LZC6lc-KcCuVKSF64XaNWGbOnpS0ZwYZ9jbs1J1-F2y9YpteyypManWMHZDslqdOdmpAIjqAAL8sFejI_BYG-mlR8N0hFqlKWQy9Z4hHvPFz12JuucYvkJU9oXwLHlT1eGxdRzISsfjVFYvUj88wpvg1118RdPoWMhjToucf3QelEGoL7JScvPgDK6svoMzHOQkz-gf_nWa6Ib0Ec305xmkEMJFmmXA5-qfcsJMvV3thR53PjGcbTNpBKnFKxpGfFvuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: توقف موقت حملات به معنای عقب‌نشینی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/137598" target="_blank">📅 08:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137597">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmcoRviqEcuSZco-ud-q1alVuQSh82Shv2bdBkqmFEgn2TDo49VevjTF1BWQnI1fQoXiHRpYtTi0k-g5WW43no3RemMOomZnCazyucfCTh4k02wudsDQzTWbq-rwlv-OpNXFlVsGL1iEbNOcKSa61v3U0lNQeDwPwoyccmA_9eNqGaqmMXrwze5Db-bX6z6wEwEC21_sRjHK0RLiko4RjDSEv7ExDJFBBnIFsMZC40ADhRswxatwbQ6McFQXyRMrmJNoeM9yQydEjapEreZ-aZjD9QyyhTRdBD2xTs3JxtfiaSWrYZFCPe_y86eyPg77kqthze-5_Is9dNcF-EHkjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش آمریکا، ژنرال دن کین، در جلسات خصوصی به دولت ترامپ هشدار داده است که:
از سر گرفتن عملیات نظامی گسترده علیه ایران از نظر نظامی امکان‌پذیر است، اما این کار باعث می‌شود بخش بزرگی از موشک‌های رهگیر دفاع هوایی نیروهای آمریکایی در منطقه مصرف شود و توان دفاعی فرماندهی مرکزی آمریکا به‌شدت کاهش پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/137597" target="_blank">📅 02:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137596">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقام‌های دولت ترامپ:
ترامپ، دست‌کم در حال حاضر، از برنامه‌های خود برای تشدید گسترده حملات نظامی آمریکا علیه ایران عقب‌نشینی کرده است. یکی از نگرانی‌های اصلی این است که گسترش جنگ می‌تواند ذخایر رو به کاهش پنتاگون از موشک‌های رهگیر پاتریوت و دیگر مهمات پدافند هوایی در خاورمیانه را بیش از پیش مصرف کند.
تهدید علیه ذخایر موشک‌های رهگیر، یکی از عوامل مهمی است که بازگشت به عملیات نظامی گسترده را به اقدامی پرخطر تبدیل کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/137596" target="_blank">📅 02:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137595">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89df9a7d6b.mp4?token=Cb3eyjfJn12hlhqGCnmhQOqsGRQ1c0n7OsBctGhmuQF3erOBfvFV-8RDQlDb_FsW2b5Zdbf2penKlG87GB_CM-V91yNii0mQ79Dl2YTvgPK6isV7HdSS1f3ywrAUWDN7dmKAg50lDGG1wbPT_D-iqUcjhD6QlMab2vHPAgC_om1VEVq_ESWtT4ndUzkQRDKdAH5eSIm-O_IXMfq1QV9To52WZWLS000uP8e3keCXp4hQW7ozWZvSizoscCdKBVAvwqg0AmSiw9iUpJ43_DwnkTSMS_OiM8AQPSppD2UTFeJyf2yLeoS-eFh1CIyipToh6ShQ_Y6YxGIPg4oi88pHBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89df9a7d6b.mp4?token=Cb3eyjfJn12hlhqGCnmhQOqsGRQ1c0n7OsBctGhmuQF3erOBfvFV-8RDQlDb_FsW2b5Zdbf2penKlG87GB_CM-V91yNii0mQ79Dl2YTvgPK6isV7HdSS1f3ywrAUWDN7dmKAg50lDGG1wbPT_D-iqUcjhD6QlMab2vHPAgC_om1VEVq_ESWtT4ndUzkQRDKdAH5eSIm-O_IXMfq1QV9To52WZWLS000uP8e3keCXp4hQW7ozWZvSizoscCdKBVAvwqg0AmSiw9iUpJ43_DwnkTSMS_OiM8AQPSppD2UTFeJyf2yLeoS-eFh1CIyipToh6ShQ_Y6YxGIPg4oi88pHBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش آمریکا فیلمی از شلیک یک موشک هوا به زمین هلفایر به موتورخانه نفتکش لاوین در خلیج عمان منتشر کرد و مدعی شد که این نفتکش تحریم‌های ایران را نقض کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/137595" target="_blank">📅 01:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137594">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozenIUcvFftmkPFPw7y6KvVsR5bB4W7N5RymTd-Tmg_vRHpX8O3gZukrSGBV3NCMahss_gKnqB1D5776cP9TKLS0lJg62oApd90CzfuwgvLsw4SWTsdaxdBrQairOuV3vuIT04IxMwFA7XZ_TAkSCVBT8Km2r5myEwB67ETF25rBndzvkm6Se3Wm1rOLpGyPYBfXq0C_feeJVOj-pEtGVUNtvJDVIuGIqR2aqflpHTIxbCDNroamCHVNHVOJN3_KiQLgjPFTFWYQzkT9OCbeDBXrUkJCrz6StLjSop1OO3rXxqAJj8pRcrHidSi8vq-Rdf3m_asy_kR50HN-LdbIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس): نباید به بازداشتی‌های اعتراضات عفو داد و باید همشون رو اعدام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/alonews/137594" target="_blank">📅 01:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137593">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سنتکام:
محاصره دریایی آمریکا علیه ایران همچنان به‌طور کامل برقرار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/137593" target="_blank">📅 01:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137592">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0bd1b6b2.mp4?token=B1l8ynEF4QHnjMmi9HU3EjGeGwR18f5U4b5w9CHnK1BAoY4_MOSPmGU6Dbz8G6BIekpUrQEs7Ut_VAq4ULtXcHwzHhcoBVsXk3hIiexWpGAvgubxn7uUFZ81CnqbZhcx2N3ykyhpCF6TlEeggjub4GIwZ55SEm9EbAUI0hr-9xcBtMrr8mGg3M7saTXvJHIUm1FB9MnA6FozQVivoef5rq8JkYS_3GaFeJJmu0Qvl_lvDbWsVLYs9aW4drfo0Et26bO32lBE7-OjlaFNZ-4XP_8S2-v3mIfxM0tUTu_hdEpqF7KEnHR2QK1lZ_Sj2eBIBGvprNMBIV6CnMmy9YMktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0bd1b6b2.mp4?token=B1l8ynEF4QHnjMmi9HU3EjGeGwR18f5U4b5w9CHnK1BAoY4_MOSPmGU6Dbz8G6BIekpUrQEs7Ut_VAq4ULtXcHwzHhcoBVsXk3hIiexWpGAvgubxn7uUFZ81CnqbZhcx2N3ykyhpCF6TlEeggjub4GIwZ55SEm9EbAUI0hr-9xcBtMrr8mGg3M7saTXvJHIUm1FB9MnA6FozQVivoef5rq8JkYS_3GaFeJJmu0Qvl_lvDbWsVLYs9aW4drfo0Et26bO32lBE7-OjlaFNZ-4XP_8S2-v3mIfxM0tUTu_hdEpqF7KEnHR2QK1lZ_Sj2eBIBGvprNMBIV6CnMmy9YMktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تحلیلگران در تجمعات شبانه در حال قانع کردن امت معکوس برای توافق هستن
🔴
یک تحلیلگر پایداری: با این محاصره اگه توافق نکنیم اوضاع بحرانی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/137592" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137591">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/137591" target="_blank">📅 00:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137590">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-y91r-HMTpW8gJcKe8PnsjofNhv3trMCp3TzqR5uFWsXQMrH3yab84ug-RXGoHOfPcRXWjMGpKWMneUIjwKCoNaNtdF5Ehk3tpXyOjVedmcm1t6O-yt368YI_Aphn5grxPuGxjEUB6hs_y6uChji6omOJ7ttlzW9zkR708CcWGjlBn1BxsvXbgpoxJFVME-MOR2TG2IdpaKoSrM1aP8uuWSZXhL1mlP8DioPCfY1XKSBsVbibEBIQdIW7uyfUPzi6ZU9rBrEX6147OZsA_QetPUgUWO2HbYotfXhihxyVQ_E42bPUBeQEX0bbD_18nirniuifDMAPSpZxdVPmFp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی در تجمع امت معکوس که تایید کردند تنگه ننشونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/137590" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137589">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره اپستین!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/137589" target="_blank">📅 00:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137588">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2m_vo8KGJkOPyHwSOWL4j7uzYwoxX9mmfxxtnlHHisBq8SmgpEEiDoC_CUpFfYvYACqTMqWt2ATK5LG1piWtNvTgop8NqE1a5WREs7fN54CNFwHHDEMj0HvFrGv-IeElguvegmVhiMJUfIPswpOapbbObxzJFTAb7DF1pfqLJOmLGn_nNrsx-MJwpQBANKyLT7CmAy2R01AJ72MJgsEc-dcspHsGC-ZVyEmTe390hwOxkjuZfAQ3xYyoKpxuJ1EVxm2s4b2jYwTXFWYx7GboxwSo9N2Yq6WrcvwIky_EXsl1kSYUMrjkgK_i96-zrvDSGfQNlGjTdC2J0OVP4s61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
7 فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/137588" target="_blank">📅 00:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137587">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxXZnAbsUBoeOuY2-G6N0fEYL_SrY9Zbvt5UM8B4nEOKM4zvhPfuRr4uNNKEGJq7NVBYizt7W3UTih2sbV_kq2_5GOobWxIPVIBpcvQrswfjB37FapXGhfnEbyP5JT3iH5mtJGpL7ROdShcqoDa1yLux_gTCKbdo5QqS98YKJnwXgbsQDQsy8Rf3UFgKWn107c8l0XCFNesPhw2LjQ6zAht7SQ8ZyTgp6pEFbe_L7YxqhCuiMaQ0Se_aDUZSVHOSB1LapMcAJPlLZ6_bQBpXJ99mYldrBXorH6SEUfXJbGwI5Lde9LgEYLb4L2xeepKeS9Yh0rMcTO_6qkoMQ6Oqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوون قائمشهری بعد از مصرف عرق با رفیقاش جوگیر شد، این حرکتو زد و جونشو از دست داد.  [@AloTweet]</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/137587" target="_blank">📅 00:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137586">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0ac09831.mp4?token=fpHIThcXPyJ3fUirJQXlV8F86d6o9u6uwg6yeAmkoECtg_Bh6UTOdUqclbMeTEk84FOl5nELG_7EtV2wGQZoKgBdBUxQoSXkSTthvXq4qaQx_d1Yvk9r37Hw51RiwFebRQE4zrH77xdxHdo7JMS14vB08G4UejT1VzYgSjHDpSpqu0dOUZdfjkUhu5NFvfE8DYClzthSR9S8A-xbKnUoCL9OANN4AgqNm8fREVufxBDHWtxOEryn6CkZhHfFmqEv87wtHl5LA8IgYeHKabNnOIUPUvlsO5R5i7nBNfO3slKY_XaQ4UJISkiNtRnyicECy4Pkt5KiYUM4D6V4ZndVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0ac09831.mp4?token=fpHIThcXPyJ3fUirJQXlV8F86d6o9u6uwg6yeAmkoECtg_Bh6UTOdUqclbMeTEk84FOl5nELG_7EtV2wGQZoKgBdBUxQoSXkSTthvXq4qaQx_d1Yvk9r37Hw51RiwFebRQE4zrH77xdxHdo7JMS14vB08G4UejT1VzYgSjHDpSpqu0dOUZdfjkUhu5NFvfE8DYClzthSR9S8A-xbKnUoCL9OANN4AgqNm8fREVufxBDHWtxOEryn6CkZhHfFmqEv87wtHl5LA8IgYeHKabNnOIUPUvlsO5R5i7nBNfO3slKY_XaQ4UJISkiNtRnyicECy4Pkt5KiYUM4D6V4ZndVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جوون قائمشهری بعد از مصرف عرق با رفیقاش جوگیر شد، این حرکتو زد و جونشو از دست داد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/137586" target="_blank">📅 00:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137585">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAZMljDUMg5DRwCf-gW55bi2VSwZ8rc0sBP7NXw-9gAcSZ36l2OliTSt7HJ7K-mstg7uvw-FihwQ4Jp79nT6h-1yLrSRjpVtChc-iVcpO23WyN_c5BxasmW9cK8uQD27Vog591ja0mylsqKPY_6CGoQJD42k0p-UR4cya-wUMbLSJsPokFH2dAbUD-xjAkXQpjjy1u8Wjgxbkq_tRtCaski0pQA83KJ_W7Cz5cEEvTlU_f9o10q0Y9uUdimzCTPR1UsXqO_lK24HdGxdX1vjon3GRWvz4cUFmACJL8wlUWCzH3BFem_MIOPvQ-D4qwCLB3_f6tsVT6ka05OMakM0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری ایمان صفا :
من همونقدری که برای بچه های 18 و 19 دی عزادارم برای بچه های میناب ناو دنا سرباز های کشور و جنوب هم عزادارم
اینا همه بچه های ایرانن
یه سری تلاش دارن اینها رو جدا کنن و به نفع تفکرات ایدئولوژیک خودشون مصادره کنن
یه سری توله رجوی و چپول هم نطفشون بازشده هرروز یه چیزی میگن
من رو صورتم رو هم اصلاح نمیکنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/137585" target="_blank">📅 00:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137584">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
عراقچی خطاب به مسئول سیاست خارجی اتحادیهٔ اروپا: شورای امنیت و اتحادیهٔ اروپا باید رژیم اوکراین را بابت حملهٔ جنایتکارانه به کشتی تجاری ایرانی پاسخگو کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/137584" target="_blank">📅 00:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137583">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/430d4c737a.mp4?token=mcZdbPLGjOex_EGRTaJRc49Bx8JcUdAFTRx1aTRCBoDNAGRPsrP4dkCZ1gb-E7TAh5O84-hIX_Nt_ASnqG0ckDX_Gaj0Q8P-9LQhFPIomnBSmkhIJqlvasYGRfCBAkvd-0MlUCbvmlcmeafWv2OW0vGEU6oZLwwwEBq5kcXGzBRhdEls5ukjY9Sx3DTdLjShmASxSI2HaE6wUZo4nsLHiEzUspp9zOGJiuw7IcgVo83RtR0t8LhMyyU3X4UBSTU3Sm5wdZelhoXG5WxVFgbnYP9fYlNnOuBZoQrcWvxpZHyO4QmWqW7NqRy_wqlFH_mdkjSfAJOCZx7AZXdSK6bjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/430d4c737a.mp4?token=mcZdbPLGjOex_EGRTaJRc49Bx8JcUdAFTRx1aTRCBoDNAGRPsrP4dkCZ1gb-E7TAh5O84-hIX_Nt_ASnqG0ckDX_Gaj0Q8P-9LQhFPIomnBSmkhIJqlvasYGRfCBAkvd-0MlUCbvmlcmeafWv2OW0vGEU6oZLwwwEBq5kcXGzBRhdEls5ukjY9Sx3DTdLjShmASxSI2HaE6wUZo4nsLHiEzUspp9zOGJiuw7IcgVo83RtR0t8LhMyyU3X4UBSTU3Sm5wdZelhoXG5WxVFgbnYP9fYlNnOuBZoQrcWvxpZHyO4QmWqW7NqRy_wqlFH_mdkjSfAJOCZx7AZXdSK6bjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شریفی نیا: اکبر عبدی پرفسور سمیعی سینمای ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/137583" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
العربیه: دولت ترامپ در صورت به بن بست رسیدن مسیر دیپلماتیک در خصوص پرونده هسته ای ایران، گزینه اجرای یک عملیات ویژه و گسترده نظامی برای ورود به تاسیسات به شدت محافظت شده هسته ای و خارج کردن ذخایر اورانیوم غنی شده این کشور را روی میز بررسی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/137582" target="_blank">📅 23:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoPAxyp-Dj5NBczODqa2YDvnH8UckRIy--5OBToFT6Gu_snBynSHEFmW-g6E_KDvTL1EpdlIKqJ-dfpE2Z5D2C8E6VHce0llmlq4uKLTqT1scJxlxVDlci73vYNju4-c7q-R7rl-Af8zw_l0_wwqMJRE1wiS7zjFVK__C37sK7Oolr2IU8PK-uoN5vii8LESk7lycB0FdTEr-4giyL4zIfL3ZD_9QjlDI2c0xLs2e_LY3il5OqvsRktD6mpFXH3snaT6Cctoy0ge_kIw3uOmOXyuCIS4XL7j4gUDpaAzohzX_lhJ9daKCDp_uP8n2cOJEzzjY6Ryya5Yi37S6la1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید عباس تو قرقیزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/137581" target="_blank">📅 23:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d2a9eeb2.mp4?token=YSH9zsq9Ik6WVLuDmAPWQkCKjmtnRzRpXkdyWIEwBKBAsP8WYp4zfMCJoiBq3Pnmwek0vjlcfq0XjQIwt6fxufFrcQrnyj05DW51fSGxLYPh-CXKCX19TPRNeBZGK3V_jMCKRvFws80z4yQGl-FeT0ms5xzqoQxEZyP7jCgQhfNksfhO2dSyZNhCB-NTjuKPq20USY3HawBdLCWspuOpCqdKCXKQVOGcdBxrexmZD01BlYHvgkJFWBg360oHsyvNHmJ2Yro0s_bmsZAD3I3C_BrPqafA3eq3LSDa1xk1F8m8mPFa29mVKDJZxaoJZlYyfLNYi3pWozqTQSid4pa8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d2a9eeb2.mp4?token=YSH9zsq9Ik6WVLuDmAPWQkCKjmtnRzRpXkdyWIEwBKBAsP8WYp4zfMCJoiBq3Pnmwek0vjlcfq0XjQIwt6fxufFrcQrnyj05DW51fSGxLYPh-CXKCX19TPRNeBZGK3V_jMCKRvFws80z4yQGl-FeT0ms5xzqoQxEZyP7jCgQhfNksfhO2dSyZNhCB-NTjuKPq20USY3HawBdLCWspuOpCqdKCXKQVOGcdBxrexmZD01BlYHvgkJFWBg360oHsyvNHmJ2Yro0s_bmsZAD3I3C_BrPqafA3eq3LSDa1xk1F8m8mPFa29mVKDJZxaoJZlYyfLNYi3pWozqTQSid4pa8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش : پدافند کشور بازسازی شده و بخشی از پدافند که آسیب دیده بود را بازسازی کردیم؛ همچنین تجهیزات جدید وارد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/137580" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137579">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMMbK_njMPoxWveqjplt3CIH1QCsBmsZbSZD88HinV_3wW8WN9tdr3Cii248oy8gfeln6yGJXyN-xOHGEOLGcsHSHY2WMQ-gCKsfviMB-R245Hi_h9cByPQGkRuhEn9EfPL-4Ll2OzFfFrU2MArQLYvK5b563WDMOEUaj-yNiQbwl68KFcufMrfz7qvc1vpj1xf5TkAqtEilQ-kMO5lgwLhTHEPAmbRKG8Nk8phYq0F1fJC39zVpUXAIbPmkYGOfO6WeFyCDlUXssdblTVwphHla4IoA2WvXqlob4X-mDut3V532WktKf-aI6oORQ-wE3TOYpwlZdtVDeTIJ9D2-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اخبار جنگ ایران و آمریکا
در سریعترین زمان باخبر شو
🆕
کلیلک کن
⬇️
⬇️
@Breakingpersian
@Breakingpersian</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/137579" target="_blank">📅 23:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137578">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سخنگوی سپاه: انگلیس درصورت همراهی با آمریکا هدف مشروع ما خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/137578" target="_blank">📅 23:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: هیئت عمانی تهران را ترک کرده اما امیدها برای یک راه‌حل مسالمت‌آمیز و دیپلماتیک را افزایش داده و گزینه نظامی کمرنگ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/137577" target="_blank">📅 23:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137576">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxCJKKbwRKQ5ivGWPAbJ0t5D15cBmUGqTtU_LY42yQlrUB0KRlHEG4rNfBoPkszW38ttYvc4oH2MKiD2H5zf3xPEHWvlM4gVAfKUZt_LnELhMfVU4oIuVUBwLNFopYmvGCxEvHd5PyXWIv53BjoVvAo88hW8xsGQ1wps_aItGThustvZh37i1YjwpznRC2zVw3lnGDyxkLOHTbWE9xXUXeYdm-vBbJBvg3tv_jl-oGwKs7eppih2ykSSHr6T5t7ci_fOzhlU6xu-E2aJWC3q9aRtjunIplkarObrKV4DOHnjjohze0v6ZX2mtPvu9R3INqNhfuMfQQ4IAtKJ6I6wdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:  حملات ایران به اهداف آمریکایی در منطقه، تا زمان تسلیم کامل دشمن و به عنوان انتقام خون کودکان بی‌گناه در میناب، لامرد و سایر مناطق، ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/137576" target="_blank">📅 23:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137575">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اینجوری که قیمت تتر هم داره نشون میده، تا یه حدی دوباره به یه تفاهم نصفه و نیمه رسیدن!  ولی صداشون در نمیاد…
✔️
@mahaneconomy</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/137575" target="_blank">📅 23:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137574">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رسانه های عبری: کابینه امنیت ملی اسرائیل، فردا تشکیل جلسه میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/137574" target="_blank">📅 23:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137573">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / شبکه ۱۲ اسرائیل: نتانیاهو قصد دارد در جریان دیداری در کاخ سفید، اطلاعاتی را در خصوص احیای فعالیت‌های هسته‌ای ایران به ترامپ ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/alonews/137573" target="_blank">📅 23:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137572">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4RiTD5hkb7oIT_1E8rzDmz_aWnmAnbir3Tl5U4XbZmTM6uk2PuHNWE--wis9U5s_2nmdQD2Q-zhyYO3fZ0whfjuL07OILLwJOc0zTrx62fCnMcyNFxAibM0LrP3nlzl2YYkXYRCejuAMaAP-WOuoL4mlngaDjISzewmERde3lRHctsnxETtJFUmyUhn30CRHBtcZj2gxa3WqSa-i-aLjzn7rrzEuO7SJOIR4EjIOeBOLj1YTMBK081JNOp6Xuhawjya5GBkKY4UL1rRSrqMkvhGpEmZTiZtg_Xe85Fn1xwQZwVpWKn2szxjcBZW-1vxOy6CZ74qKF_zSSs-UmnbAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی مدعی شد: روسیه به ایران در تصاویر و دیتای ماهواره‌ای کمک می‌کند!
🔴
رئیس جمهور اوکراین: از ابتدای ماه جولای، ما نظارت ماهواره‌ای فعال روسیه بر کشورهای حوزهٔ خلیج فارس و تأسیسات نظامی آمریکا مستقر در آنجا را ثبت کرده‌ایم. این تصاویر متعاقباً در ایران ظاهر می‌شوند. همزمان، همبستگی آشکاری بین تصاویر ماهواره‌ای روسیه از این مکان‌ها و حملات ایران وجود دارد – هم پیش از حملات، در مرحلهٔ آماده‌سازی، و هم پس از آن، برای ارزیابی خسارت واردشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/137572" target="_blank">📅 23:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137571">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-k4W4vydaLoz7E8uUSdVzCaRjgraDkSR3gzTVKiLMHOU1Ma7rKLu48D7pO7tNtPexzp_DZC5KReh2O3n5xYncNPamQK4Bh4xMiW0qHOmLCD6Zus5quSeW8l-jwbNBPhJ_wclt_SYT7K70Xn2TTiOj5jrU39wZJwH2vg-epQpvZEH6B-BcBbfzjvoDyr33rUDRHiz6I-0e34s4hIv4b-KcGBG3VAg1RW1pR0U0pIyWiUz2leUjNB7C65RJF2IxIM_Nuwq0fHqlipEQjKdBhVkAmSKNTvMN15e0M8PATipspPPMXxlo6v1E0fx56xaA5HYA_HUKLAKKOiXYZTdCQo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
یک پهپاد در نزدیکی خانه بن گویر در هبرون سقوط کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/137571" target="_blank">📅 23:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137570">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سخنگوی ارتش: بخشی از پدافند که آسیب دیده بود را بازسازی کردیم؛ همچنین تجهیزات جدید وارد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/137570" target="_blank">📅 23:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137569">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ادامه آزار و اذیت ماهیگیران ایرانی توسط نیروهای دریایی کویت به مدت چند روز متوالی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/137569" target="_blank">📅 23:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137568">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
پیت هگست، وزیر دفاع ایالات متحده، به MTV گفت: ایالات متحده در روزهای آینده حمایت خود را از ارتش لبنان افزایش خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/137568" target="_blank">📅 23:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBIr_lQ_BphHMQxLxlU4S36XmcNNNsima-nE_fkNJw_aQDKgWxPSMyLfLYAn0G9_dKu8Bvmhgqi8IMMrX4lU22Sgv2tXSOr7NH1WTZOo6xaVL_MQ5eZESnpkopUPDp10lBUZWKd-pKjpvnXMh9bRGaJOAyyJHbAjIvJJkSxHCMF4gdsqo1IaWPsak6YJ0peYEPaa7zrTmPrgqRvKvbze5oE9tuVr_GkXgwDNhSz9v_pWOkJaCluuRK6CrYr4lMixrWq-hlMTPPhOmK-7ywnxcoRxfE2yAg7eEd73unedhrNBH7HpHAgsS7ZRZIIzCTEIja8G4TgHSFOxfjzp0FN3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره
اپستین
!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/alonews/137567" target="_blank">📅 23:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8N6WT5bSfN2zuEkJl7uqpCb3TPQgsmQPW5eE4SBLmaRhoxtfKG0bzJz2nM3x-oI8RFxMTriMR5crV0Tq_WLbVSmwCNAq38vnmagRrTp0weFeEqzxENS8tPblrioXVvO9RSs9dWFE4dJIhHY6mBdUp-TKH1MIbARSV1ZPLaQtyyfjuNSDZkfI4B_lc_4f6ap-jV4qWmXPdJYSzmYhuPhJyz0cKY22-_k1dkyURMAoxyhR7CaZC2vBqbvr1xkGpzNiP0X8kFbXg0C1hT7Wvxm5U3pi3JZN0VsE-TfR6h7HGy_nK6SyKfi7ytsMkc63V-ZNhsZABj9fvOBnPqWcx34uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهریاری، گوینده جمله تنگه ارث مامان ثابتی:
اونایی که شب‌ها تو خیابون ول هستن، شعارهای
کصشعر
و متوهمانه میدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/137566" target="_blank">📅 22:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137565">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل:
نتانیاهو قصد دارد در جریان دیداری در کاخ سفید، اطلاعاتی را در خصوص احیای فعالیت‌های هسته‌ای ایران به ترامپ ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/137565" target="_blank">📅 22:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137564">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/alonews/137564" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137563">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/137563" target="_blank">📅 22:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137562">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIU1C4EHsnAOqnbdnKL8F3LyC7-CJyzGEK2A2e8afdCe7trSyCga7E0MQUmvJIhxEZTBUS0QBEGZYRNS65xBd3GFn_VRu_ogPs_BIxrbA0gHV3P7QABgIZWscUfNvcIvmoPILTRHlomVYsl5G4BunuDgmoDHBTjmgzIbUp5wqzHpht7QZrNzdMO4hpwt1Wx42iFX1wK-YLshUNMrjHcG6koSi-8Im9O64_6dmEDnuZ2qSVZyJ5YZXQa5ycnFe4hLYUFkJErAhtPw-ZtptQHH9cCCGBB_Wq-w2-uvq5mOa_XdwP9_4tpuFTrj9XDIfoTytFmf72Z6JEMu-9oDF8R6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
وزارت خارجه:
حمله اوکراین به یک کشتی تجاری ایران در دریای خزر که منجر به شهادت یک ملوان و زخمی شدن یک ملوان دیگر شد را به شدت محکوم می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/137562" target="_blank">📅 22:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137561">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzeUPMyP6kXQYnKtGwFZli7vq42HIuje8H-egxDTRlneRKzT8dokvrnUODi82jKhPH8huxVmOX9cH8nHo77wpOErtlT7Dj1SWBFf_PaoKXmcOz_ruMpIkuL55e0SWAf63T4MYcWo-SZP-WvEAs4lAVwdwCjOmGmAZpd2NY7goWNtXD6ExSkRhDQCgD8z2lAsis4PABw51J0VWsiA94BbglXsuJyO4G8x9SU92JLas73BdjteB094FlUr_40b4klLkYjbehM5Mt-tahhhYHl1DOvnSknZ17Um4ZXXF58Pt2G4eBstaX2n_0sXly5rfffKL20beSRPYREUIg2dMzsXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقت کردید از وقتی سوریه دست جولانی افتاده دیگه کسی نگران حرم نیست و امنیت دمشق رفته بالا و زائر هم اونجا بیشتر شده؟
🔴
پ.ن:قبلا میگفتن دار و دسته جولانی میخواد اونجا رو منفجر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/137561" target="_blank">📅 22:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137560">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی ارتش: تمام پایگاه‌های آمریکا در اربیل عراق نابود شده است
🔴
‏دیگر توان عملیات نظامی از پایگاه‌های اربیل وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/137560" target="_blank">📅 22:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137559">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzezwKAFoS7bm-AWDhhBwUgKXfSV76kMr9e1J4AusYmCDrCOOtbsIhltP47U4VsYIIjWbPzCjp6ykbXU7TNeX0lVsfwPumc9Xp_st7cpJSTSAIr7q_CfEhmf40ecaoRMEkxkSyX117vT0RBr9TSbaEESzArrsp7eBJLATPt4mVRwU0EO4l5mavYZZ-et52uG8cz2EAOLOcN43L-YF35_QcDbLHZHm5vLxbvAOQBDt9dRWoUF7aufI4MArTXshyqs6G7eAWYvVzsgOP2JJpZJHizjeiQkyuK62q8akuSyGYe3SvWRJbUOM93SO8TFnx7t5WFDV8l0LNVjoJ1aMY4V3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش محسوس در ارسال ترابری‌ها به منطقه؛ به نظر می‌رسد هر چیزی که باید به منطقه منتقل می‌شد، شد
🔴
بیش از ۲۴ ساعت از آخرین شلیک آمریکا می‌گذرد و گام بعدی مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/137559" target="_blank">📅 22:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137558">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fbc06d1c.mp4?token=XpKmUtr5Dl0hHS37Bp2Pnd6B9rFpMODFt957k-UWL7HhJNqTCqfv5jsiRlsQhLJqhfWIMYqcwroqJ5zeEW12HwsGkOX9AwGWK7Xcxf4-hpogdZ8V-tgWnkYEq7mJAjE9RokONNs8LktHbU_ymLcrvbM7dZk2RLSjm5jOVZujia-FOcXfg7bKIE7KxOUAqYXOmiLFbwwxLv_vT8E_q_q6XxYRNsgE8p1FDK0-UQGPzEiwd0lI909WVbDd1PPzZ7Mi0hYmDKo0DakKDHwRJHr0RStj9veMjMFofDuZBUELOTp1dxYPQbL5_6AuIJZ-BZKaNXxh32XAUkyXf4PbbkE6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fbc06d1c.mp4?token=XpKmUtr5Dl0hHS37Bp2Pnd6B9rFpMODFt957k-UWL7HhJNqTCqfv5jsiRlsQhLJqhfWIMYqcwroqJ5zeEW12HwsGkOX9AwGWK7Xcxf4-hpogdZ8V-tgWnkYEq7mJAjE9RokONNs8LktHbU_ymLcrvbM7dZk2RLSjm5jOVZujia-FOcXfg7bKIE7KxOUAqYXOmiLFbwwxLv_vT8E_q_q6XxYRNsgE8p1FDK0-UQGPzEiwd0lI909WVbDd1PPzZ7Mi0hYmDKo0DakKDHwRJHr0RStj9veMjMFofDuZBUELOTp1dxYPQbL5_6AuIJZ-BZKaNXxh32XAUkyXf4PbbkE6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏مجری صداوسیما میگه موساد بچه هامون رو در دی‌ماه کشته بعد احمد قدیری کارشناس میگه در دی‌ماه در یک اقدام انقلابی گفتیم کف خیابان بکشید چون دستگیری و دادگاهی و اعدام دنگ و فنگ داره و مجامع بین‌المللی هم گیر میدن! همونجا کف خیابون برای حفظ« پرستیژ» بزنید بکشید و خلاص...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/137558" target="_blank">📅 22:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137557">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/137557" target="_blank">📅 22:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR05YcAzkVQlyHOuC-i-m5vqOi3NpfeaDM9b62jv1_RRabE8612ygQ1tSg2wm5LGDTXvgr1EIvz9C4MTXALKObrq4blTZhpVzDgsertXEyZXqqbx4V27frZlQHhQ4KeXDdFV0rjPLDOBBu11eNodnFyEO1bCouVIGA3qQhQUdvqb3xQMfBN7fyt3CwkkUvZEuLtIYpFLw1KCdSRGia0npTgKccCZTBWqIQOmWK5xJv79b4rt1_8m-jJrYZ03Mys7HjXu4bsB3y2pxJeN9aFfQg05hf_CABReuFd4Lkx8xunoEbZkY_3K9NXIjnQu94ni465N0LrrJmzGakGfzL3oLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ژیلا صادقی: شیر تو آمریکا لیتری ۶۰۰ هزارتومنه ولی تو ایران خیلی ارزون تره
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/137556" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/137555" target="_blank">📅 22:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db14df2e2d.mp4?token=vnGqq12YgQoFBnPpugP29o0akisERkMYHp98rfz1iTwRp9A9fsOspKJYoUWeSMR8Tdj1I0c4Uc8YQGwrXZ-TbcTbyBXcgZw5ApkUFYi1led_9Wb3aI34ZT9nx0oMb_lToA8-unMCs9WyaHwxT1CHoBg1yfYWzcu4YXdSerlHNsuixisLwu51eHZue20kM89Xq79KVBlt19_QX5qQY18kz8EMfAOwmrznYlicLvpQuKGAkSHC-t7qnm2opQeR5_-rxcFVBcpojhwnAMt8IotC-MRmToqghZHisq7wyefZw0iX2w8XdwhpwUnPB4fb-WFu4QTXEQvhryLyHOWjn2XBMZnygXA8nzSLDMNETQ6qPFinIWl2b45yexYcDR33SIq-7LV8w91zi8N1p37GNcX620q58PFw_btjxASFHarLpkCeMxdFP6HOR2FLT7ojHfilTS9elw_wKr-oqSNxypeQBYSvrilitLelI20RadiC865LQLNb_ccn9sSL8Ucfkl_mVmkTwzfz2mCIejWGLtE0riyzhWCkujkgxPla5avH6e0VnSFD_boxGT1yysfm9ar4lgGzdGB7Phi50jE1nN6_xQ7hUhemwl89gGGLQnmDLRh12V7IzYZJ-8P-IXo1DMSlOBd8SRfw4XN6LM8ONfujKmi9WnR0knUepQlgkw9ZjrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db14df2e2d.mp4?token=vnGqq12YgQoFBnPpugP29o0akisERkMYHp98rfz1iTwRp9A9fsOspKJYoUWeSMR8Tdj1I0c4Uc8YQGwrXZ-TbcTbyBXcgZw5ApkUFYi1led_9Wb3aI34ZT9nx0oMb_lToA8-unMCs9WyaHwxT1CHoBg1yfYWzcu4YXdSerlHNsuixisLwu51eHZue20kM89Xq79KVBlt19_QX5qQY18kz8EMfAOwmrznYlicLvpQuKGAkSHC-t7qnm2opQeR5_-rxcFVBcpojhwnAMt8IotC-MRmToqghZHisq7wyefZw0iX2w8XdwhpwUnPB4fb-WFu4QTXEQvhryLyHOWjn2XBMZnygXA8nzSLDMNETQ6qPFinIWl2b45yexYcDR33SIq-7LV8w91zi8N1p37GNcX620q58PFw_btjxASFHarLpkCeMxdFP6HOR2FLT7ojHfilTS9elw_wKr-oqSNxypeQBYSvrilitLelI20RadiC865LQLNb_ccn9sSL8Ucfkl_mVmkTwzfz2mCIejWGLtE0riyzhWCkujkgxPla5avH6e0VnSFD_boxGT1yysfm9ar4lgGzdGB7Phi50jE1nN6_xQ7hUhemwl89gGGLQnmDLRh12V7IzYZJ-8P-IXo1DMSlOBd8SRfw4XN6LM8ONfujKmi9WnR0knUepQlgkw9ZjrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک: در سیاست زیاده‌روی کردم!
🔴
بهتر بود به جای دخالت در امور اجرایی واشنگتن، تمام تمرکز خودم را روی مدیریت شرکت‌هایم می‌گذاشتم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/137554" target="_blank">📅 22:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137553">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وای‌نت: قطر و عمان تهران را تحت فشار گذاشتند تا سازش کند و از یک عملیات تقریبا قطعی و بزرگ آمریکا جلوگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/137553" target="_blank">📅 21:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137552">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI) اظهار داشت که اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/137552" target="_blank">📅 21:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137551">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t38lrtr_Cu6gYMyifu8Jn2b_ZHuvdcRCfUJrgnCX6Lecj7iZSwxeEuqEu1TmchphY_5JM2GSY9djfW9amTDw6SFb7G79afXs_9_vgs-zmINBHGGzb0umVjH6xehn4U3qJneINzDj6h0jHl0yrCwLucqbhEUFFStBNF7o2DqJ3SFENc_rw3egQuDZnBDz3uManIoyVQl_FE-mOu6H1LuO-fqycgLRdr0nHaufS4_7Or7QqJQhvtwb5u4F_5COd7U7ohkAW2iC6IIRqpnU-TKATv2nqd0_sbs8yXIgrUpyvdZvpQkGnWolpECUlkGykX0NarGfR9UyM5rLu8Ldlz7oag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای آواکس E-3G Sentry متعلق به نیروی هوایی ایالات متحده در آسمان منطقه به پرواز درآمد.
🔴
این هواپیما شب گذشته حضور نداشت، اما امشب دوباره در آسمان درحال پرواز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/137551" target="_blank">📅 21:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137550">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVZ5tLCg7UIwHBAS02kupPgO-TW_rW7liN5b064EbzHUpdPctul9k8Yq1MAqdbsLSxaWIfG8x2u0xXUCOG36OfjO0K2X0mFMPLnX-UXEDVHHbJ3UJJT4NbTLtrU4_eG0FuQF9QlCaCTjI9MFO2J8p-IW52M8pe_2AplbNnRVp-zxAUWxluZgC5EayxhYpUqmpHFHf8LMjjudAQfJJcs1JPUAMUD1aof8qmOCvYqMid3lSz87T8mEQhzjSKD5wLYYtPtuzHTpofnfDA_FHpMBU89DA5Xl7rVPXBDAnkVwOipSYkcjrYlc53dMnkrSQyEn5vEaBVk_ZQsgM9DrGT-5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر میرسه عملیات پل هوایی آمریکا به پایان رسیده؛ درحال حاضر فقط 4 فروند C-17A در حال پرواز هستن. هر چیزی که باید به منطقه منتقل میشد، منتقل شده حالا بعد از حدود 18 ساعت بدون حتی یک شلیک، مشخص نیست گام بعدی چه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/137550" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137549">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
منابع وابسته به سپاه : کل خاک اوکراین در دسترس موشک‌های بالستیک ایران قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137549" target="_blank">📅 21:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137548">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7f5eac88.mp4?token=J-cRoDEngD17AjgRPQyErLRlw8Xs8UV4_LddekTBRhdKRX7PVxLANkPdag64BTN3lYUmN4Xq5JXhjw57E4YiZ79vSn_3UZFx8yZh_y_vm2xlcylKH82Zt2yfqKnHXhMorrfxgQK_zgaP_GsuR7Ps0UfrHynOxo4U4BSV9RvjjuwJ_AR70cGHxh4_eCyzw6VtSHzkqlEV6Qu8_yrxwI_4FR9ElSOXqo24pVSyRTDyCesCpkk-lI9yGPVRtQ9_SKPwSKelwh_NIXSAPO1g8yWe6yoB3IPr-MfnjH2hbsvc36a4xvVlxd63RATg4Pp00ZAJpWTL2wglR86sTSB_Z6rwWYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7f5eac88.mp4?token=J-cRoDEngD17AjgRPQyErLRlw8Xs8UV4_LddekTBRhdKRX7PVxLANkPdag64BTN3lYUmN4Xq5JXhjw57E4YiZ79vSn_3UZFx8yZh_y_vm2xlcylKH82Zt2yfqKnHXhMorrfxgQK_zgaP_GsuR7Ps0UfrHynOxo4U4BSV9RvjjuwJ_AR70cGHxh4_eCyzw6VtSHzkqlEV6Qu8_yrxwI_4FR9ElSOXqo24pVSyRTDyCesCpkk-lI9yGPVRtQ9_SKPwSKelwh_NIXSAPO1g8yWe6yoB3IPr-MfnjH2hbsvc36a4xvVlxd63RATg4Pp00ZAJpWTL2wglR86sTSB_Z6rwWYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالیل اسموتریچ، وزیر اقتصاد اسرائیل:
خداوند در دهه‌های گذشته، کارهای شگفت‌انگیز و معجزه‌های فراوانی برای ما انجام داده است.
🔴
پس از 2000 سال تبعید، آزار و رنج و سرگردانی، ما به سرزمین اسرائیل بازگشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/137548" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137547">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae537cb11c.mp4?token=SuRB014dPQ-wWjk9suNdUNt3Au4vKPiCmU6420eM7q7mLZTI9ukS--K3Zb3FnxVPht-bLT7HlRWKByv963VhAmnlbSwnTWt4JJzag5hx4cVOZuFbl_zYbPyziDJ9LFbWVHm4Sip_4jTMsnqOu-IPDGPSWD8ls03083cAM_1ArJdVuicP5TuwomsTonCPDNSyLmVR4-WfZ-RxKeCONHgl9Fa9daTnfd4y3C9GoV2LehfA3kGpBMIGQ4g5MMnVNeFjxkbicGbFJlzxqWnVkytHsMAna-IeUwfidx03-ZfIyude1xXyjab5Iup5K29_Zcam1UAk9rjJHtF7CYi6H0IgbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae537cb11c.mp4?token=SuRB014dPQ-wWjk9suNdUNt3Au4vKPiCmU6420eM7q7mLZTI9ukS--K3Zb3FnxVPht-bLT7HlRWKByv963VhAmnlbSwnTWt4JJzag5hx4cVOZuFbl_zYbPyziDJ9LFbWVHm4Sip_4jTMsnqOu-IPDGPSWD8ls03083cAM_1ArJdVuicP5TuwomsTonCPDNSyLmVR4-WfZ-RxKeCONHgl9Fa9daTnfd4y3C9GoV2LehfA3kGpBMIGQ4g5MMnVNeFjxkbicGbFJlzxqWnVkytHsMAna-IeUwfidx03-ZfIyude1xXyjab5Iup5K29_Zcam1UAk9rjJHtF7CYi6H0IgbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزائل اسموتریچ، وزیر مالیه اسرائیل:
درسته که محور تحت رهبری ایران تضعیف شده، اما احتمالاً یک محور سنی جدید شکل خواهد گرفت و ما باید با آن مقابله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/137547" target="_blank">📅 21:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137546">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3075e4fb.mp4?token=JXbT6H4tTVkChcXNDO3Cm_PD4gEdPxqzjg4YYKxIXzbgOnHSYTYAtvbU8_Cff_zvDhQxT6QxSsC-KpNqT70M8Yim26PxelLkUJnwzrvTHPJkOkKEml1l-zJpBFZ5pxqMynzP7RSirsW6XJTIIzM5ksx8Izhu8nuGpTQKeKc3NKnmuYI7aUC9WLmcjo3X8z8kwioXVKTFPTRjdz73h3D2tGhxUKsyxC8gPx04iE2yUYA8roWkW7qQp3lvG6IyDKNBOsTqDwvmaDy4Ctp-Y43p4l_tpVuxWldwQy1t4A5Ntj3nKU0YIQghtGBTtP8PR0P4EjPG2SK1yzIK5c-pi6w_UJnKPMAGzTZwFaplVKIiJitb2E-L_QVWW2Cj0_qRX28OtuM80TzgibrwfORNDQ8bIQ9qchI2N259uocolrAF0faLmS-2YSYBGOjqFTfr0m5vuBi35VLYgWo1AzySOe4Z2vW-rE0T3VXD0hRsg2EUvhGneN48ndk0yke-PC7wnFY3--XyVw2r-UL_qIBMsbmJ1VMrV5PBqxXWlDsEO6YwWYCPWjY947EXVu6AsT11_JKFKFxiSQLRSMJhkF6rFj5WCjuMDeJ32Az-AfJEoLO12ZHH88UehTjhPFKfAAkufCfHh6f50PKSE1o9azMv5aZEh6GaxuQ8Iu3fF5pYlrAvOFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3075e4fb.mp4?token=JXbT6H4tTVkChcXNDO3Cm_PD4gEdPxqzjg4YYKxIXzbgOnHSYTYAtvbU8_Cff_zvDhQxT6QxSsC-KpNqT70M8Yim26PxelLkUJnwzrvTHPJkOkKEml1l-zJpBFZ5pxqMynzP7RSirsW6XJTIIzM5ksx8Izhu8nuGpTQKeKc3NKnmuYI7aUC9WLmcjo3X8z8kwioXVKTFPTRjdz73h3D2tGhxUKsyxC8gPx04iE2yUYA8roWkW7qQp3lvG6IyDKNBOsTqDwvmaDy4Ctp-Y43p4l_tpVuxWldwQy1t4A5Ntj3nKU0YIQghtGBTtP8PR0P4EjPG2SK1yzIK5c-pi6w_UJnKPMAGzTZwFaplVKIiJitb2E-L_QVWW2Cj0_qRX28OtuM80TzgibrwfORNDQ8bIQ9qchI2N259uocolrAF0faLmS-2YSYBGOjqFTfr0m5vuBi35VLYgWo1AzySOe4Z2vW-rE0T3VXD0hRsg2EUvhGneN48ndk0yke-PC7wnFY3--XyVw2r-UL_qIBMsbmJ1VMrV5PBqxXWlDsEO6YwWYCPWjY947EXVu6AsT11_JKFKFxiSQLRSMJhkF6rFj5WCjuMDeJ32Az-AfJEoLO12ZHH88UehTjhPFKfAAkufCfHh6f50PKSE1o9azMv5aZEh6GaxuQ8Iu3fF5pYlrAvOFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالیل اسموتریچ، وزیر اقتصاد اسرائیل:
رقابت جهانی در زمینه تسلیحات، فرصت بسیار بزرگی برای اقتصاد اسرائیل و صنایع دفاعی این کشور است. ما در این زمینه، پیشروهای جهانی هستیم.
🔴
حتی کشورهایی که از نظر سیاسی یا دیپلماتیک، تمایلی خاص به ما ندارند، باز هم در این حوزه به ما نیاز دارند.
🔴
ما شاهد حجم سفارش‌های بسیار زیادی برای شرکت‌های دفاعی اسرائیل هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137546" target="_blank">📅 21:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137545">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اکسیوس: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد هرمز خواهند رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/137545" target="_blank">📅 21:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137544">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک پرتابه به یک نفتکش در ۷۰ مایلی دریایی منطقه «الشقیق» در سواحل عربستان سعودی اصابت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137544" target="_blank">📅 21:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137543">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m44h_4zm5Ai5b89uFUXtXjAMACjaauPW6Uac3Lg5Qa1ye5JWUUpKo4ScWBGFWATXcio4zLGrzI97EaXxPTcEz_Hu2mrCANjaNALXZB1jJ4xUA5zWa5O8X2KnwBFq7i4vxOhqA62UWkcKxzXQly7wsU3T4nXp2DlpOajIcsB3An_i0z4TTbsPSiCPTz6q3TXXr1PVSWS4_6lKcwEZNGGO-6ns91cgkjvORz2bcn90GD3hNpZnqEKjMfn9oxF9YgYaD_iAxZHDQAOJy5B78TPSXmMZnPXT-4eRQMTGN0v2SdSDTq8D6cTaZZMAZbllA5LQnXXeQgMwZ0J-fbJ9BrgJIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد کتی پری از کاخ سفید بخاطر استفاده از آهنگش در ویدئویی از حمله به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/137543" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137542">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سازمان رادیو و تلویزیون اسرائیل: در حال حاضر بیش از 90 هواپیمای سوخت رسان آمریکایی در اسرائیل مستقر شده اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137542" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137541">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
گزارش زلنسکی از برنامه های روسیه برای ادامه جنگ: پوتین در حال آماده‌سازی مقدمات برای یک بسیج گسترده‌تر است.
🔴
ما همچنین شاهد همکاری روسیه با کره شمالی هستیم. روسیه قصد دارد 30 هزار سرباز دیگر را از کره شمالی دریافت کند و آمادگی‌ها برای پذیرش آن‌ها از ماه ژوئن در منطقه وورونژ آغاز شده است.
🔴
کره شمالی نیز در حال آماده‌سازی برای انتقال سامانه‌های پرتاب جدید برای موشک‌های بالیستیک به روسیه است.
🔴
روسیه به کره شمالی کمک می‌کند تا نحوه جنگیدن را بیاموزد، سلاح‌های آن‌ها را بهبود می‌بخشد و به آن‌ها تجربه استفاده عملی از این سلاح‌ها را در دنیای واقعی می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/137541" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137540">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ad5f15cf.mp4?token=f_YBVCXaT_Flokz9sBfxf3SW8oZMG5_wD6PeyjNVBrxQ-HvvwS7MJexb-xAUx2RWKOA6w7txQRHTZ_NxN3Z_K5k7xiqeXM9CSUaLg03o4vGweG_m0BUPP-nj0nAJVUubNLgjALqW1GG0z9ph4ZddTzGNuNh896x30NplHaDRb_CaTiI6U_6jzav0hsJSeeN7phcOViS2NtQQ8ye8pfVQiCtx__XmqayR5B33l4pJPzvxHv86KVdL_uXC8OGEsqNeMWk-lPauekMnuKbXosDwrTl1IkzmNC8GXdt_T8urPR-kj7ttE6xSBh9g8kNe8ZbNuWKV--W69gA3YbuwXSi9bWP8Cj6AmT3Eme7zZzhDzqvKcbz6n2EgRBCehzzfpaIkr0DB1ei5zKnCWs5U6Unvgj_28EaSK9xm2E2r8HoLETSKAcgnUlNDhzGJyg-_p2o3DEMEzgvlvHKgwVq1g3_1BDz52d-bvChr5EVTTUrI4O8iT0qW1iD8U0QFAJMpubf9eEwhS4WBpgmgdjIflnV5PFhPb900uHMHVsHNNiLZt40Ap2419FfPtRHANini8kCcDYJ7v3J6kiXdAhyEjX7-gNNM-sBXWkxEYapfRBW4PTzJuYrRMb3HJFajfJ7ChDeO0NFHr3YK880LupH5ATkw-aRpbrQPsIVhGqJEb86c1iY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ad5f15cf.mp4?token=f_YBVCXaT_Flokz9sBfxf3SW8oZMG5_wD6PeyjNVBrxQ-HvvwS7MJexb-xAUx2RWKOA6w7txQRHTZ_NxN3Z_K5k7xiqeXM9CSUaLg03o4vGweG_m0BUPP-nj0nAJVUubNLgjALqW1GG0z9ph4ZddTzGNuNh896x30NplHaDRb_CaTiI6U_6jzav0hsJSeeN7phcOViS2NtQQ8ye8pfVQiCtx__XmqayR5B33l4pJPzvxHv86KVdL_uXC8OGEsqNeMWk-lPauekMnuKbXosDwrTl1IkzmNC8GXdt_T8urPR-kj7ttE6xSBh9g8kNe8ZbNuWKV--W69gA3YbuwXSi9bWP8Cj6AmT3Eme7zZzhDzqvKcbz6n2EgRBCehzzfpaIkr0DB1ei5zKnCWs5U6Unvgj_28EaSK9xm2E2r8HoLETSKAcgnUlNDhzGJyg-_p2o3DEMEzgvlvHKgwVq1g3_1BDz52d-bvChr5EVTTUrI4O8iT0qW1iD8U0QFAJMpubf9eEwhS4WBpgmgdjIflnV5PFhPb900uHMHVsHNNiLZt40Ap2419FfPtRHANini8kCcDYJ7v3J6kiXdAhyEjX7-gNNM-sBXWkxEYapfRBW4PTzJuYrRMb3HJFajfJ7ChDeO0NFHr3YK880LupH5ATkw-aRpbrQPsIVhGqJEb86c1iY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار علیه شهریاری در تجمعات شبانه؛ مرگ بر جیره خور آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/137540" target="_blank">📅 21:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137539">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وای‌نت: اسرائیل خود را برای حمله گسترده آمریکا به ایران در فاصله شب جمعه تا بامداد شنبه آماده کرده بود، اما دونالد ترامپ برای دادن فرصت بیشتر به مذاکرات، این اقدام را به تعویق انداخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137539" target="_blank">📅 21:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137538">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
تايمز  اسرائیل: ترامپ از ارتش آمریکا درخواست کرده بود که حمله به ایران را به تعویق بیندازد. او در حال حاضر ترجیح می‌دهد که به مذاکرات ادامه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/137538" target="_blank">📅 20:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137537">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی سپاه: طی ۱۵ روز نبرد (از ۱۷ تیر تا ۳۱ تیر)، ۱۱ هواپیمای جنگنده و بالگرد آمریکایی را روی زمین و در حالی که در پایگاه‌های آمریکایی در منطقه مستقر بودند، منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/137537" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137536">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
آکسیوس به نقل از دو منبع: ارتش آمریکا در حال کار بر روی طرح‌هایی برای عملیات بزرگ احتمالی علیه ایران است، اما ترامپ هنوز دستوری نداده است.
🔴
تصمیم ترامپ برای توقف حملات در روز شنبه، ساعاتی پس از ورود هیئت عمانی به تهران برای مذاکره در مورد تنگه هرمز اتخاذ شد./ ممکن است تا پایان هفته، توافقی بین ایران و عمان در خصوص تنگه هرمز حاصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/137536" target="_blank">📅 20:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137535">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
دو شرکت زیرمجموعه لوفت‌هانزا آلمان پروازهای تل‌آویو را تا سه‌شنبه لغو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/137535" target="_blank">📅 20:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137534">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):  در پی گزارش در مورد یک تیراندازی در منطقه جامعه سوسیا، کمی پیش از این یک درگیری خشونت‌آمیز بین شهروندان اسرائیلی و فلسطینیان در منطقه شکل گرفت، که در آن هر دو طرف سنگ پرتاب کردند. این یک حادثه تیراندازی نبود.
🔴
سپس یک تروریست سلاح یکی از شهروندان را دزدید و به سمت آسمان شلیک کرد. علاوه بر این، یک شهروند اسرائیلی در نتیجه پرتاب سنگ‌ها مجروح شد و برای دریافت درمان پزشکی تخلیه شد.
🔴
سربازان IDF در حال تعقیب تروریست هستند و در منطقه چک‌پوینت‌های جاده‌ای برپا کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/137534" target="_blank">📅 20:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137533">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
معاون نخست‌وزیر و وزیر امور خارجه پاکستان، ایزاک دار، با شاهزاده فیصل بن فرحان آل سعود، وزیر امور خارجه عربستان سعودی، گفتگو کرد تا در مورد آخرین تحولات منطقه‌ای تبادل نظر کنند.
🔴
آن‌ها همچنین در مورد امنیت مسیرهای کشتیرانی در خلیج فارس و دریای سرخ گفتگو کردند.
🔴
هر دو طرف مجدداً بر روابط نزدیک بین پاکستان و عربستان سعودی تأکید کردند و بر اهمیت ادامه دیپلماسی تأکید نمودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/137533" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137532">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
الحدث: وزیر خارجه عربستان تماس تلفنی از همتای پاکستانی خود دریافت کرد و درباره تلاشها برای کاهش تنش در منطقه گفت‌وگو کردند.
🔴
وزیر خارجه عربستان و همتای پاکستانی‌اش درباره تلاش‌ها برای تأمین امنیت و ایمنی آبراه‌ها بحث و تبادل نظر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/137532" target="_blank">📅 20:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137531">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رسانه‌های عبری: احمد وحیدی و مجید موسوی در صدر فهرست اهداف ترور اسرائیل قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/137531" target="_blank">📅 20:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137530">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgGmFehhogEQxvhMjxnAfhkOMIlVm9mRB1_fj42Q_2wHo9Bgt5quZVI0bRtyfpx6rxS474Vc9pSmTMq5zFzTDW9-bGb7MOLoNPLCYEp3FNn81tHpNoenZnEquuywSxM-Ypcgi8n8uv4dSV-8RoPQgO_jTNmO7ZRFtp93xjdRuJC_gB2CXhmg4ej8VhHO_0rtIEDicd43nFqBp4SHbAGpe55lJHKXgy_YdqEtP4uW1hmGy74FrD_nK_FBDcI0kZd8N6nNr0Kk1KPyNLLCDC07av_7YvZFvzt52ihiHK3npeEMyO1bk-ItdD8gagGhJZ2HKD7CPHayHzVQkhrewAY1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صفحه رسمی سفارت آلمان در تهران شایعات تخلیه کارکنان این نمایندگی دیپلماتیک رو تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/137530" target="_blank">📅 20:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137529">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c6d15482.mp4?token=nPmj3hdfEd9DmgYdUccu1XeHDEv6l4JJ1n-bsCDqpkEojTFsJVcnzDJFYUgzBbB6WmIMl2BuxYGWLN3wSIlv_nTpH3PUkPdV9nA1_4keOGhebkLIFIm7NK3GrlVUZ5u1sFyXK33UBoCwx2vPeBk5EnPSgO0Y131eWT8AKjfQQlmmsYssMIm4xZAGhWuGLjTvGg1iB12NPYvLOjJ8u8BmIV1N14egcyrlbhhlZcR3cvBg3N_hyKKU1ZWvV-mwoVTYtRlqjyTq7tGyM9SJWXCiwfgA56vZuQwolmbscg5vtAfxp4qh3SQjLj0zotJn6QmjaOPV6ASZjP59QLsdYilhlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c6d15482.mp4?token=nPmj3hdfEd9DmgYdUccu1XeHDEv6l4JJ1n-bsCDqpkEojTFsJVcnzDJFYUgzBbB6WmIMl2BuxYGWLN3wSIlv_nTpH3PUkPdV9nA1_4keOGhebkLIFIm7NK3GrlVUZ5u1sFyXK33UBoCwx2vPeBk5EnPSgO0Y131eWT8AKjfQQlmmsYssMIm4xZAGhWuGLjTvGg1iB12NPYvLOjJ8u8BmIV1N14egcyrlbhhlZcR3cvBg3N_hyKKU1ZWvV-mwoVTYtRlqjyTq7tGyM9SJWXCiwfgA56vZuQwolmbscg5vtAfxp4qh3SQjLj0zotJn6QmjaOPV6ASZjP59QLsdYilhlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ موقع تعریف‌کردن ماجرای تیراندازی در ضیافت شام خبرنگاران کاخ سفید یاد نیکی میناژ افتاد: «بعد از اینکه صدای تیر اومد، مردم داد زدن: "بخوابید زمین! بخوابید زمین!" همین باعث شد نیکی میناج شروع کنه به رقص و تکون دادن و قر دادن! باورتون میشه؟ خدایی فقط اون بود که فهمید منظور اصلی “Get down” چی بود!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/137529" target="_blank">📅 19:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137528">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
برخی منابع می گویند:  با افزایش احتمال شدت‌گیری قابل توجه تنش‌ها، بار دیگر میانجی‌های مختلف پاکستانی، عمانی، قطری و... هر یک با موضوعات و طرح‌های مختلف در ۴۸ ساعت گذشته فعال شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137528" target="_blank">📅 19:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137527">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پس از اتریش و ایتالیا، دو شرکت دیگر از گروه لوفت‌هانزا پروازهای تل‌آویو را لغو کردند
🔴
پس از شرکت‌های هواپیمایی اتریش و ایتالیا، دو شرکت دیگر زیرمجموعه گروه هواپیمایی لوفت‌هانزای آلمان نیز تمامی پروازهای رفت‌وبرگشت خود به تل‌آویو را تا روز سه‌شنبه لغو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/137527" target="_blank">📅 19:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137526">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
مقاومت عراق: هیچ عملیاتی علیه اربیل و کویت انجام نداده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/137526" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137525">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
حوثی های یمن دقایقی پیش یه کشتی دیگه نزدیک عربستان رو مورد هدف قرار دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/137525" target="_blank">📅 19:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137524">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e37e5e25.mp4?token=JzgVU9el-voNXSjQaKGhtHYzr0iugPtR7LBmvKxxD6L8ez-oshcpQeAvq0xNE6OqiWzrpGHM0CKJxFXyue8Gy_HltqX_oDJjkLWPxpW6I9OCnyZWEkMuj5QD3IUQM9tK3IOR3Lr4sTs12HpCwYtvNppR8KbGLpTyfibZZ9f4ZOZIW997J6v8Mh08jV-6Pgn8lGQJJIQJWi1ipiH21prSC-Rt9krDXLMrFDp0dwTdGpK6Xbf_2LaauET6U2oOeKSsRyypT2-yFg5bkCHHCQIBW8kUl461m3NNsI776UuLNtmWxNvNN7AgY0DfHDINgwsXpVRUWLwEHfseXFy_0-HP1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e37e5e25.mp4?token=JzgVU9el-voNXSjQaKGhtHYzr0iugPtR7LBmvKxxD6L8ez-oshcpQeAvq0xNE6OqiWzrpGHM0CKJxFXyue8Gy_HltqX_oDJjkLWPxpW6I9OCnyZWEkMuj5QD3IUQM9tK3IOR3Lr4sTs12HpCwYtvNppR8KbGLpTyfibZZ9f4ZOZIW997J6v8Mh08jV-6Pgn8lGQJJIQJWi1ipiH21prSC-Rt9krDXLMrFDp0dwTdGpK6Xbf_2LaauET6U2oOeKSsRyypT2-yFg5bkCHHCQIBW8kUl461m3NNsI776UuLNtmWxNvNN7AgY0DfHDINgwsXpVRUWLwEHfseXFy_0-HP1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو عجیب منتشر شده توسط وزارت جنگ اوکراین از سرنگونی یک پهپاد شاهد در آسمان کی‌اف
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/137524" target="_blank">📅 19:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137523">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1gwe0D34HU7MnnO_CgLXAwHr8gS0PpjTkj1uFzw5fLZi_idrA2Br4VIYG4-t6zf_r73rERqTNEQrX_vsv_IgVRJa6JIfmYU_cfB_i6Yr0USeWAcaOE2eT8tWfJ-Le2roYYM1PmKjxFklAexB9FIi17v-Clf45iE6vUGazGx3ckL3gvgr0C1bZ3JxpY0JUDHOfAJ7AtsG-4ox0pmawkTd884mSBrrTvo8_KrbUJTIhqsnai0ZmJyc3QpOQ-rX8vaC6Gz_XwTqB_Ldyp2S9Fu7zq4SNQATblpMDfLaMnDZXzzPEtn7W4gU2wky608y6JJMrobrUKKeguOXO9DoTikXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر منتشرشده از فرودگاه اربیل نشون میده ده‌ها فروند هواپیمای نظامی آمریکا در حال فرود و برخاست هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/137523" target="_blank">📅 19:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137522">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2hEykl9rX5Oh_KwGN0fAS7DlWvoUsAvBrI21PPmWodsln44m_wMk94pxNDLVZbqwq2LnVJ5iPH1B107lnD1m7kYkuISOH1nLIEnP7jI0EL5IDYH8bl5YTjz4tZMGAWfq6IIzNkOi57DAoulgnnPkguy5OTgFovJ0KBtPOOVlJguYQ5DxLKH-3eVSArEnMR7S9rm2OCNqcyRTqgyyrFPNNnF_UQoVrL-oEgyv3ye8sdD0GcL-8UW_4qH5IiI78bfxgxZZ7j4eJvGQoccw03Ct8-rYgTEiwYq_0d2c630_dCJHyCdB7v8a7fQzRuLoXmNDR1diNxDSASK38Hhf3TyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تروث سوشال ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/137522" target="_blank">📅 18:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137521">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
عراقچی: ما در تماس مستمر با کشورهای منطقه هستیم و توضیح می‌دهیم که هیچ دشمنی با آنها نداریم.
🔴
برخی کشورهای منطقه اکنون دریافته‌اند که حضور پایگاه‌های آمریکایی در برخی موارد به عاملی تهدیدکننده برای امنیت آنها تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137521" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137520">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اردستانی، عضو کمیسیون امنیت ملی:
شاید آمریکا با سرگرم کردن ما به «تنگه هرمز» و «کوه کلنگ»، یک رده از مسئولان را بار دیگر ترور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/137520" target="_blank">📅 18:41 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
