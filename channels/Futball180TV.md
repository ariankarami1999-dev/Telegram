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
<img src="https://cdn5.telesco.pe/file/d8FMdeVjuv8LA-TrPQ7By5mi-gnmKO12JacByxiSGIREAuZl3OlK04IMWDx-HoZEd_-0vE5wW5hETgz9GIji41EZDVnR2FVOrPZy70IvNbEFVwTDQPfO7CkY-LkbehH9SwEv7ti9RPtVx-LDdO_0dWWP9bQIbfbUDtCJ-lqmpyiWDkYGMbZ52WPMKlfYtNGn3XMYt-YzZ6d2uXrERmdikaaM_knNDpjcCXfibgqACK9XL9tEgOqZLE0yViOirAroPwjhxQtu2O-cU2KtXn2MPq5ATvL8R4pLTCFW4dLLwUToIgWV-FBKzIqmrkat64yHmpqHnpR8H5U96IleP3o4Sg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 694K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 06:13:10</div>
<hr>

<div class="tg-post" id="msg-96227">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e8ec080.mp4?token=fSRRKZntX21jmnEcV8pTzLauWTOVP0H1wmDi1O2IjYr4DKhjFhnlncZfgugcom3U8xzMuvRCQSzb03TB0pNEbd9YDgmQpyMwp3YwSs0lmXLncNKLGpJR7HYk4Gegj0PHKDO0tD9GMIp4SHNL1wOJ7L8rgFi53BuSHFufp7T2tImB-1yZHuExLG8AiO2_bjvTbG0gNGlcr0tcdae9cff2v_XwVGLcAXUsPTaczmCz2j2rGVEjDWX4bMizeYfHTdG7yyaZFVdRj7n2xLZXZaIoaKo97QOawaBagRJ-2sSknnkBZycSttONnA3uOx36a0ysDqZ5nhgyNZyhjNF7svdwdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e8ec080.mp4?token=fSRRKZntX21jmnEcV8pTzLauWTOVP0H1wmDi1O2IjYr4DKhjFhnlncZfgugcom3U8xzMuvRCQSzb03TB0pNEbd9YDgmQpyMwp3YwSs0lmXLncNKLGpJR7HYk4Gegj0PHKDO0tD9GMIp4SHNL1wOJ7L8rgFi53BuSHFufp7T2tImB-1yZHuExLG8AiO2_bjvTbG0gNGlcr0tcdae9cff2v_XwVGLcAXUsPTaczmCz2j2rGVEjDWX4bMizeYfHTdG7yyaZFVdRj7n2xLZXZaIoaKo97QOawaBagRJ-2sSknnkBZycSttONnA3uOx36a0ysDqZ5nhgyNZyhjNF7svdwdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
#فووووری
؛ حرکات منشوری هواداری با پرچم جمهوری اسلامی خطاب به مخالفان!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/96227" target="_blank">📅 06:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96226">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a25fe227ba.mp4?token=JJjMhrn2q6MqvMXOiowjHat1ni05g8M2_31Bpr-X_IKCxwjDKL0SMncNL_sP7nUZRsqxi4saNRSg0N8Ts0jYl9swl4bsPbNZNs56Sr7h1YRUWOO_fRejgyjXZOHpEJkV_4KNcAySnUWu0H7OndfFx_aZt3pRXBMg2sPtu05kMBSuMfRCVvn9V26BbysaxtdZoojL9sjtG5oBZYJNlJz3kd72aakw23Tz2ngay2tGDkBLFHY0xnpS0m5YwMEa6mdhUj3KtRjYF1a2ZP9D4MVHEO7uOaxReKDaP4DPdhuQPbc8iG5o_8xBd6GnwfKuHKFTxkSvWQCRccKvb0ACYnKC7VSerzbLHvu0KbZHOvyUPRH7xPH7OODS2YjiSszD4t2e82vUJ6-dxOx4b-F3T-U0HUlIg9y_ZYolffYvwhz6l5n7fzSL11P4mWSgvX9zBLjL6w5EEl3BkitoAqrPM73prmakXQhrm398zp35aMAni3umjMx8xWu1tBnqCN9LsUU7JMH1qijrEQjDk5aGu01Fn3xq66f-I7r3ky4IB1hU1LpVpNK7420RIcSrxB2zfhqBGgkkT3AonuuPcqrtJNCovS0CQLqmjECyNAIKeILIQw7GEHUqWhnmRSxzaKMbMZMnCmdp5k7EZnkMOxgbXiykFrefOa3EtQUTGPEA3GlD6uc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a25fe227ba.mp4?token=JJjMhrn2q6MqvMXOiowjHat1ni05g8M2_31Bpr-X_IKCxwjDKL0SMncNL_sP7nUZRsqxi4saNRSg0N8Ts0jYl9swl4bsPbNZNs56Sr7h1YRUWOO_fRejgyjXZOHpEJkV_4KNcAySnUWu0H7OndfFx_aZt3pRXBMg2sPtu05kMBSuMfRCVvn9V26BbysaxtdZoojL9sjtG5oBZYJNlJz3kd72aakw23Tz2ngay2tGDkBLFHY0xnpS0m5YwMEa6mdhUj3KtRjYF1a2ZP9D4MVHEO7uOaxReKDaP4DPdhuQPbc8iG5o_8xBd6GnwfKuHKFTxkSvWQCRccKvb0ACYnKC7VSerzbLHvu0KbZHOvyUPRH7xPH7OODS2YjiSszD4t2e82vUJ6-dxOx4b-F3T-U0HUlIg9y_ZYolffYvwhz6l5n7fzSL11P4mWSgvX9zBLjL6w5EEl3BkitoAqrPM73prmakXQhrm398zp35aMAni3umjMx8xWu1tBnqCN9LsUU7JMH1qijrEQjDk5aGu01Fn3xq66f-I7r3ky4IB1hU1LpVpNK7420RIcSrxB2zfhqBGgkkT3AonuuPcqrtJNCovS0CQLqmjECyNAIKeILIQw7GEHUqWhnmRSxzaKMbMZMnCmdp5k7EZnkMOxgbXiykFrefOa3EtQUTGPEA3GlD6uc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛ شعار ایرانیان ساکن آمریکا خطاب به بازیکنان منتخب ایران: مذاکره حلال شد، رهبرتون بلال شد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/96226" target="_blank">📅 06:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96222">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_U0Z1g8jshSoCOG1h2_mnYLeoEV3W4m1u8U0Dn4-ahwmz0VCJXOUES2oQ1EM01shh9s2UkWQRccUWolTiCmL4msSc8CULwYIniyJlBOUScg_1Os8xzc0ggr0GZxs_BrIwERKENsp1MSlGXXtihF6supIhXGv_dDHmoHWwAIiO_0A7byE5hvIdRm2U95jWZj2L2DBLCL8ApGWlUN9V2frLM8WQ0piUQL9hxR0Yvg5agwm4OiSDkHnlCU3HMKDnTZbzOjB4kc1KFD17_wK-CgYYQvU4hWN7_-oKkJimOYD7NMKe9rcsz6gEzpnxHJaxCLmLFccwmTJ8TmZiP3ZPzCuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4DcMQVsUbgyDe7hfHibwpytHFFPg2JtolfRBqJKQmt4McBfqa0kR2YzruEC-BbA6s70iNPkYgKbsKzdwZDNckeZRLzYL6Uv2Vwbwq2iGMgW-MunFahVyiRpEdN_TiCMPJC_h2ZkGIP1vfIw8mH6cq3G5QCYroUOsvlTHEIqkEv27SL74lWyTukKMX_WQB0Sm5On-iiSKKmvDhu2uuhycuHlE6SQWlJ8izscp7hOGJ1BA4Y_5IE-1Dhj8pUHNVYrFeVcnyFZ7pPMzhPd0_lLnw_m6RGCsvWIUpt-Wg8gVi2vVm9kzhUur63q8VOyZZuih6r1gVZU0FgzlyLKYxvRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSq2KCIkxfuQ4xn9lbljhaiNabKfAClljGF0gplWh6uV8JYvecd0FPHmWH01c58cgCNwFurldDHUyqrUMo1o_nKqYfef5j71KvO8FgrWZHYOVjmvflIvXekaiAGXAVI26qrdU8co1SfZZFzGB5UHV6f_dEcAgcHwUrDD9pRrVwdnUihqf-zzmkCicq0YEKhL0mBNj7m9vlAimTfcfGEsMuEuiCfynJLzcOfYKYRhqwakzwvt50xSV38v_YbQuxMQaIupIu2jGQg4oZnEsvUc7mlcBa6fTP-xDCMh7oFCpmGipPhpU4Uc6x0VDiIUGc2D_EDHWGPwEkLzuBk3TUr6CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSShk2h-5XML585hHauzTGCp3Z5Y9zLMnno6atTqcPCIjkM3ynCsg9_eNDERVRDuZ26_BJJZTP3ApJJHv6qcqEuaMMlG1jp2VIVgGBMiAchXBiC-3GBMsJUJdgB5Q0fDLg_L4UhmKN9l1BOMjf_eNj7kBEmzUoxDddiWZ5by_lbEbgTARGSZtC7KNgqouyCVX2m1Neox0hmoAqXlpDEpGmWw4049CswZZ6UI6eCymA_izSOW3qbsahV99YxYNtELPzSeRjBV54F_Buuqx9nKzFgqUOeEW2ByCN-cgUqzL95t_Oc2MGui9pZp9P3y6Jw9LjbGF08HYvdYGZXxlevBLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇬
🇮🇷
مراسم پیش‌از بازی ایران و مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/96222" target="_blank">📅 06:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96221">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a11d33a2.mp4?token=Pq61mhC7HvWZqTc8kwHJlz6NnhofyMk80xaOX20XmsLnDr1W7Z1UiceD6s7mfmfwjBvO2OYe2befN90DnumCe_r7DF0GhnmW42I-2o0Vbm-axnXkCz3rCGyVyo_YtCmYgMYkNKawjo-QKVJgQlArlKncGkCbzJa6W0zBD1L-CbWKxt9hi8nvAWIx-5Evc5nnfd8xTo50ESScR5Fv3tK37erf0WZmkl4mxlHFegRjz5YFBV1sQKoZHyfWz-7KXyuRo0cPxB8sDPOXFV4J3vg1rVpp-ZEdcQNay1fyhSv8KY6QdLG-Fx5WllflAcRfaC-bSEa1CN2cCsSjS7PiJPXWKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a11d33a2.mp4?token=Pq61mhC7HvWZqTc8kwHJlz6NnhofyMk80xaOX20XmsLnDr1W7Z1UiceD6s7mfmfwjBvO2OYe2befN90DnumCe_r7DF0GhnmW42I-2o0Vbm-axnXkCz3rCGyVyo_YtCmYgMYkNKawjo-QKVJgQlArlKncGkCbzJa6W0zBD1L-CbWKxt9hi8nvAWIx-5Evc5nnfd8xTo50ESScR5Fv3tK37erf0WZmkl4mxlHFegRjz5YFBV1sQKoZHyfWz-7KXyuRo0cPxB8sDPOXFV4J3vg1rVpp-ZEdcQNay1fyhSv8KY6QdLG-Fx5WllflAcRfaC-bSEa1CN2cCsSjS7PiJPXWKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تلاش ماموران فیفا برای جمع‌آوری پرچم‌های شیر و خورشید قبل از بازی با مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/96221" target="_blank">📅 05:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96220">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGmw2k4onYhLoSWEka86J-C2tfncBq_K46NaNBbsxfuDiMCYpt0WcxuVronNT8z2yVq-QkkghBlUBYbCjfh3EnZQLPGbbaaLnDM_qEvem5EfaxII7O2aMtlmRLWptlpcei8nHlrATf6z4hvWnAQGrjNRLF63OmXscYYg--Z8nXNYON4iMH_4Iy4Xqv8kTqzCJsQPj1qiJN9k9051frAEnaT4VKr8C_dCWG71_BSoGV2tKyfGvau3LljTS7TkhzhHveTa4NkuuRB-_vnoGMHv2emG6kFy9jagx7wnCM82gMV4nLFNgY5hx8wi8xYywLu9ZaQ9s8PbeBQJNbe5XBO2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه H در پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/Futball180TV/96220" target="_blank">📅 05:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96219">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5anUuMatWqPEdod9UEkxYCzn8_gSgV6v0BIsK3NLBjivWJrqO3VGpAs5EXeLhuJDW2D5-0ogqxpnB620GXlVTDaSAB0Ss_y4-Rt8_uKDlzs-tJn75ZY-k-pf001arW6zKMMKMWDYgl33YXTtbAYx_1zkSoQaBUyf_bGjo1aYeXbnu8gCOQqwmQTUyL5e2VDG0M7x3trQPS2wdojhwaoOdKbrVDCe1dCL1et6z7fBKoE1hGtNi_Dajo_mc87OrwrJFXOBJjDpUzXoEf5934x2RYW_qzI0g-LAs56xYd1_Jd7EKLl3uQv5ayUM7OczmepwDWvrjxlKyfqtJA21GT1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آپدیت تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/Futball180TV/96219" target="_blank">📅 05:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96218">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4Js6yyyws-5C_1SlvPP1HlcY-QMAl-u5jeJNzAuSBNymI1IhDy4glrUZcFaUTBE2CyrIlSCkksxQbZokOL-zzn5ouY1e6_mKy6yR0ExiRD8qvdzBYQE7w-SUc4O9HY257e0VMLxERpM8ketomxU5qsm4uStkCcsR-V9Wo63RHv-75gwYQQzggMUGyEjYkiSCNS9kEhsqjQ-c7MNHRYfAjVJnZmVG5g7nL4so08FaMnXJZEfgHz9eNhSZ8uzhp5pTW9xf7dfcFoT8ebFzN2eSL9C2qAHDxFLSSZBh0jRmGR4Dh6S0b61vgDR9R49TpQKtEP2gzQ-AQyipPi9bJlZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله یک‌شانزدهم نهایی جام‌جهانی
🇦🇷
آرژانتین
🆚
کیپ‌ورد
🇨🇻
🗓
جمعه 12 تیرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/Futball180TV/96218" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96217">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1cjwYjYh6687Rdnp-3EZyHdmVsgIqtwgfX0iZf8YdL3DiZ1HbmdvMer-JHUJ_Z5U53ADPEBl8dw17XlLgRVUcmmO16FIrfQ3d9aH1rf1GryDJ7kCQLYPZeypZafqeEwjZyPr2u0t3Mf9SGp3ExRUOVIJmPgI2Y7snQj9Mf5EDj73YFehSQGGYUc0CGfoVL45zaeoC1ISfOX0ifRCqsnE-aA9c2cZj8pk2mLAU_6X3aLOtKehNQuanTLYeuSraYh5dbFW0c5eNZspT6TYyHbrWJtt-HWBkz2Jb9QFNRCig9LHBdYgIhCxTIL8oG9qXWqQOjWu33RAKtU7cEZFdC-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | اسپانیا مقتدرانه در صدر
🇪🇸
اسپانیا 1 -
🇺🇾
اروگوئه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/Futball180TV/96217" target="_blank">📅 05:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96216">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUX9pxeWXXfDEzWHFIQ8NOQZ33bNSZO-GaQRDpg0cPfP3xgsOmoz-RWkCbyP0SrtdtQy6O7n3OFn9eUntfI75U9zhprl8CcgughAqu1eOwFBHz2v1MMlcHTgPGaWcv2nomoIiX_1dEH6WTiyjFXvlLkKBfgoXBpDMdCV4T6tRzL7aWqeED-frglFnezH-GPT-xMEiQijGTgnPi2jL9P26uV9GzfjxuIWa5WzfWJY-zCNw1lgKl98cL4Vsvav5DgbL1-x8STUd97yi7xJ2l9yl4QBkgjpLgDnRoanUUv-sz4WVKKHg1LvuhP9P_eG8v7_8Kf81ulra6wxwbATqwL38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | اولین شگفتی جام رقم‌ خورد؛ کیپ‌ورد با ۳ امتیاز صعود کرد
🇨🇻
کیپ‌ورد 0 -
🇸🇦
عربستان 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/Futball180TV/96216" target="_blank">📅 05:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96215">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اروگوئه اخراجی داد.</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/Futball180TV/96215" target="_blank">📅 05:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96214">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e81d27f472.mp4?token=inoKVfSjnb-Q7Fskg5ilDxsrcyKrv8OVevT9lAH_yTVK2bXhppeTWPpzkheKgeFkr_wEt7ZUQYM3RvtVv1eeQIaXjpeYPyMhrE1KCgduHjMIsF0zguxsYJjbzkO5y1aq0wWOmUctoyp_UonbbadkCWwz96iEvN45SVMOTzocEzutoDyBXlD-cyH18-IPIwYl3qe0JdE9AnQIFPIjwgnDUQJWaGW6gq3pZFQWb-Xu57pEdSOIS1LH-2REHBQwSN2zirbvJ4719J1uZhoqiVM_IcktwxRVeWBWRU-etaqf53evxV_RLIIUoG9fCZAWnKKFrOcSJTqFin4SvFeHWLvC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e81d27f472.mp4?token=inoKVfSjnb-Q7Fskg5ilDxsrcyKrv8OVevT9lAH_yTVK2bXhppeTWPpzkheKgeFkr_wEt7ZUQYM3RvtVv1eeQIaXjpeYPyMhrE1KCgduHjMIsF0zguxsYJjbzkO5y1aq0wWOmUctoyp_UonbbadkCWwz96iEvN45SVMOTzocEzutoDyBXlD-cyH18-IPIwYl3qe0JdE9AnQIFPIjwgnDUQJWaGW6gq3pZFQWb-Xu57pEdSOIS1LH-2REHBQwSN2zirbvJ4719J1uZhoqiVM_IcktwxRVeWBWRU-etaqf53evxV_RLIIUoG9fCZAWnKKFrOcSJTqFin4SvFeHWLvC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
پشمامممم پرچما رو فرستادن بالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/Futball180TV/96214" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96213">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnBZnZUofjemzadvNac9cfyJu7y-pokTXc8M-0GvXEn4WbHchfrPIxB2_JmvtWGl76fGRtSnB-2nqY-QdD70CuP8hWh1gU4LLkkEpnVn0JBedBfEwLh267ne-oBZddcDFfNO9vyiEKjwPz51JGgqVj46omaoSCDx2EgFVusexa0q9neXWGbBmiNoekeFpZJXECHhjvjWc1MG3F08Yj05Kxnd-6-ZSoYRCMA3Xf7-7tFXBgBgdORH0qrTjRA65wpa2Ceo9Glj-mml1QoFU-ENuiwij7nwbzm0EtBRAdi7I2J844KWBvFtILqP3QvrYnam6nXc5kF8N-LM2diQK-SO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فران تورس خداستتتتت</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/Futball180TV/96213" target="_blank">📅 05:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96212">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فران تورس خداستتتتت</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/Futball180TV/96212" target="_blank">📅 05:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96210">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c90qOXIeslrfNUoeiMtoqM7h1_86iUmNlt6SEGjExuWHVhuuRHfY7gQfa0EDVQwUCm10rg6tImIxj0qipRX8na3SKb322Qlc98YOdyA8iZP4Go6cl9GIr0sRK9aXqTPjG-sIiuLvLNWt9u8crsUuSkOwroQEJtUU962687dd0s47dqC_8IOUIEseoIFO5XgU7_R_je94Le886YwsKIrml9UC64usu8wwnUliP6oFlyM9U_g5W6UZDZ8FrzYiHYTiAgYKEtXkr1RnqFSK1VqZcjEfXR8GNx5Spjw5HTk3hbvMMYalK4XpgT1tK6nSC8b6jxFfU8hq5Kj7ewd8QbdVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLwgYdM9soWG582MEDmw0zj5RBb8WUuIbfej6TzTJ9-H-s8Sfu0S-KWwek2Y9AqV5bHlCxWKPzoz-bcuPK_ujoj1pJEknxao2d8KwH8-OzVWLhKn_7BT5wy0XvtgDEGXi89UytYY_hzpK5t0v_H9GuHNal6jghdXNI7dEda9e9l7S62y3K4DWhKnJIhNb0A0UVdsUiLsur8VPkjRkVCYaHR3llL6-M1CC5BWyPNL7wfCgdjt5mqg5dPvFr9-HDzWATNR6lUJnz64nG2fKTmnENJu_JZhgOBLykLaebKAaLWxkQuYonncJwXk54UIszXg2R6HIjd_yYBkoaZBlTUftg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇪
🇳🇿
ترکیب رسمی بلژیک و نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/96210" target="_blank">📅 05:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96209">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv8SrS6ETvNuLhHAQAtam8ggHXLvalMgo6bQy2p5X15HflHo26qs-Iz1xQHrs68FgNmWkpU4doA7giaq2crxLauoI05hMQV1ht5HrIdbuT7vkZxivdNQbZTnfu6S94TJ46DM9gYzv9r20uwlNzGd0xYU0HCnnxttXlXXBEyA9hikrHKO43a2EvdjM347FKrGPrDEz47lk3BYCC6GKKvHxKrKwRgDrlnFmST5aeMRGnAFc9JjfSl4gTPc1wlKfPK_rVYxhF-q0YH23y5y7SeCIb8DegpPXjfkPTXOTNgD2aA6KBBsPRczB2-QMwLz2wEk7IdeHSfYyWwXK_Urk9ODqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب‌رسمی قلعه‌نویی برای بازی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/Futball180TV/96209" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96208">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkCcsEwo3mjLArAf4uLydchD9SQzky2G8PRiAL1WpbCmu4_jueNZa76n8ia0dxZKtHwUwkqLkxs9rBtAHFc-S_abKsYmSXZ7r4kldIuSHoMdcr-EQCCQTLAusk1vYNqi3IZoUmPrtGPuRpYjDrNtRKXgxGQmqY87PzJI7CSGKjDlehkj1g6tJDPyUuiKN2XRLHszCkzx8nyoAbsJ5_qy3q08zov3kZ6ev9xRM7gl6oECfEyizzzvgnDTl3ES3Ey5jAsdFB1Xzy-EJXx69RDGXjcgEJCxQpCnhM5qx46_njKApkqaWOKxZZ0_dk0fsXv4xW-ymnkGKxTykOqSW5x8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب‌رسمی قلعه‌نویی برای بازی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/96208" target="_blank">📅 05:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96207">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیمه دوم بازیا شروع شده.</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/96207" target="_blank">📅 04:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96206">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWIirBBLn_yIJoqfM85Ji5cCjZaFyDbGOdCdDbHTz4oJRDk8v18s5UFuJ7KPM9SeVhNQBjnZOOivzEjXhPuPShW4SBmjD7ZDmI_wbRWhONgao8EcG-71b-M8VBunESod8eLclOKMZNRKG5s1vPUmjfyzun7pn5zDK945xpcR3sSMje4-OCpAPo50JdckFSr-Op0R00osqiQLUtOC7p_jQUK2L6-aFDCuQLjEEwlaNtKbzDUEQwxqsNCT3oFvgDJc9IYS6MPxZuGsNqKYCDwwhzs4CWwNx2gT5xpcZpmHYHaoYzejrSbEaYDSRattBKtWS6iE6urd7N-wpu-e7sA1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازون عکسا که دوس دارین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/96206" target="_blank">📅 04:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96205">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnEPXxOpTix91-XB6AyBnK8gnIRYM_GS7jR1IZdMvDk3eNsXppUlYBIhut7Y5EkvQca6qIr6Z6b3umYJyQ3m6V1gwZWQrUtr3gnZyX9JmFqBnESnTUbypeSMjsNlqfDTUBxuKCovfDvMt4K4jGaG1KA2Z3awxEWBD8jf_4B_XWKGO0VGxg9mME1qvoYSxPPe_XHg6k81Q4gQpIDmCOEIEV2Hfs4gBuKmdpRDAUUJZDa9UR4vIyZgsWtVA9WOMBDvrBJklZRALbIOUeLflR2iPdST47pAlwT008pMvlfwiF-CtpWaajUwNQEw9BI_R-ZuU012B6-MAYjWqEIs2p1l4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
| لامین یامال در نیمه اول مقابل اروگوئه:
‏
❌
0 مشارکت در گلزنی
‏
❌
2 دریبل موفق از 8 دریبل
‏
❌
0 سانتر صحیح
‏
❌
0 ایجاد موقعیت گل
‏
❌
0 شوت به سمت دروازه
‏
❌
8 باخت در دوئل‌ها
‏
❌
16 بار از دست دادن توپ
‏
❌
امتیاز 6.1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/96205" target="_blank">📅 04:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96203">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THOmsw061qW_-SqK23d3T6EnEgROI8itjhqO-bwNojp_sk0N7_GLDU0vecLcN727kr2UtVCNNhjs6mcQyJo1iHDiqQs8vbCwvZ18lnkbYoKTpPAQUegmh1UQMcX7IFwJH2Z7KjPQt4vAPsAM0lxC0N4JGca58cEHuPa_wycIwspy4VIHXda37q0EZgs_AyerdEwXYhHj8O0KBmSYxIU7ajQrwY6K4_ZxYONJg9iEqns66Rssa1MS1R6E2aEGXCkoHobNsUaRsKMs7xPteosCi68g541FlRUQNOyvTC1zjJLJ70L257x0Tu4ZC2pC0GA4TkaVCrODEBPHPXFKmDMQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6SlM-wg1_9u82wOSXxmNjxZ4i5ybt4Yf6UXiuIVr9cuDYiyvljOrEctwSDp3vHF7CQ1gCAP2iLtN91mHgb_XVwmR7dC2zw88MFrjUCr0muZI1MkDobkHa1TvDPMVI7uyYZL-JajPF_lkxhH0dTNcQtSkvgwINxOYUEaVuB4CH6xHMbjLx9U2i5sRDAARgjwoJ5p8an9kGJ0IUW9HD5k_GHeluuqZ-pfv8ujDPyNa5UVvk7rku3U-2x5fkWl2wmlXRP8MOcHFxY52DPhSx6GByClyNERqmQrzHlET2sW9yXWo3x8_ARndISBqFJbTb77Oyqd1oIpk_HD57d_VuQx5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عجب بازیای جذابیه بازیای امشب
🔥
4 تا تیم رو هم 2 تا شوت در چارچوب زدن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/96203" target="_blank">📅 04:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96202">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb94d9830c.mp4?token=OUsNcpIT5snGZOXkmBEIjTSBxjTqBm11AKUl3DbdhSX0Hz5w3SaC7GaQHsyfwH_Bz_5RrZCwD4rBGWoa65HnbHOpmyrccLcbzCu8Mz1BIUea1dHjSBbzzw3ah6B-h2sdibc4Zj9_AHvGi0k9CfVFLLoJxRt3WrKfsANh8w2H6nI4pgYRgfFy8_aSXufj-5qL6NdA31r9KoZdF-6fraZ9ohKGbtrkAKe_9BzpHZHukpSB-2JRki2Dw27sn0vXJREVUkJmWZuJY5bmzy-BCmgw5u3WuhlrxMrXWEUSFK3OcyZ-jne6vAL9TXj28ttoj6VyLkiWnQre27mWagDQ6BN_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb94d9830c.mp4?token=OUsNcpIT5snGZOXkmBEIjTSBxjTqBm11AKUl3DbdhSX0Hz5w3SaC7GaQHsyfwH_Bz_5RrZCwD4rBGWoa65HnbHOpmyrccLcbzCu8Mz1BIUea1dHjSBbzzw3ah6B-h2sdibc4Zj9_AHvGi0k9CfVFLLoJxRt3WrKfsANh8w2H6nI4pgYRgfFy8_aSXufj-5qL6NdA31r9KoZdF-6fraZ9ohKGbtrkAKe_9BzpHZHukpSB-2JRki2Dw27sn0vXJREVUkJmWZuJY5bmzy-BCmgw5u3WuhlrxMrXWEUSFK3OcyZ-jne6vAL9TXj28ttoj6VyLkiWnQre27mWagDQ6BN_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللل اول اسپانیا توسط بائنا
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/Futball180TV/96202" target="_blank">📅 04:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96198">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfnjnsug_2BQh0c4DN3I3ahp0e5igRMrpP9oApYCMYzimjEbiVe3_Kpm9Tkgg7JDHuGPTQ2VnH1tA6R_qBJX8KZpjVWOVEcG7jC9TtLsyDW4mOv8NZWKYh1E5oghaGUV_0dJKVH34TC7tPjUU3soG_Xivc-slC2kXZpd1aMQlHaMTQyl_d1OQ4p9bcVhLlVsBZh6FQtkQ1zIuDJnEEmRfi2P6SaZdPvUzV1FpsXdrJ6HBN5-4PHLHQfmdJlBz6SwcEHis7WP_BteFS5aAuQLbAhKhnVoFq97AdvMhWqiRUasmsyDwpJhcqA1Tt7wMYuOd0NICvaqoF51gs0v6M0Aog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxRz8Q-E10wd8WLiZnWqL3rsb1M259ozkSGBwGyOouONIn9ltMyIfA_e4CpNFmEEIjb_hs9EDAzNo1SOZy_3o9RCHcMRZm-XCyVnoVdWfBiDB8da1Eh--ieNH2Izi6Zi_ghRZ9zuGiUPXsTbhGd05ic5yg8ABcWwROH6r9PDl8HT5ppRSKnr5CbqzUJs1BZHyJR9_K1aOXDUwy8b0mHmsJnLtlngW7Fd5fDByrQ4K-FBuk5ApkFwGeVZahlL663UqUHBJyt9oER1Jgk2Pvvvm6osDKn5QAKc_LRVIpj7Hg-33-N14Qmjh1iCX6MAT4ZIcLHnD4LANp47LdmUpJHMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9jFKwLpxR-16GLpGafBjtKJB7gHme92hWAhQsenEFTbEIhcL7anveWxzcsKLDRcadMyMis-N0guT0h-_tEnJF1saZHx-obqBfGYfslDnb0JVEwriX5yyzPCkqviWIk-xKKXH2p_wKmpVeSoxArkUZGe9TVGeOYT0ZeRsD5tpsAr3DVCC7KR7ePEd77U6Sr_Pusm9dQULwxxr45Bejc0nZODSJRDlaMFt1MkcUXiWTygx8YWY8s2o7jcGBXFfrNYHHTLTkB3TlPctxtrY-AB3fUpXsNgGnmLfdYG0sNY1Zx0A4Ltq8xancA0nUMxwmd3XmdaatQX2FgHkhWW2cw3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0zAvROXYTnH1uKE8wSL0INdPUq-aaEsrJfIDk_kWF46rOSCjuBkzCqlKaMZDi8u97gC7v5Lo_8010UOT8GoczKaEMx0R2dtulnMOieF75GrsCZ0hHSnXKGxW_MRv-xSbvQT65scOyfvCiXUqGqkoieJl1XDV6fxyRIbaaYeAKche16vFZ9mcHtu45gUttjKF8SSTkNo55abXwEpt7g_ToRYqCA19VAJ-f8yBGah-tsuSdzIoxKCdNDN6XmoPsQ8lZ_rH3-j8BxQ3Qza5Y1WVQYWT4ltclgXbL5i2-e405LzPQIzPN4l14g8Z3BQBVERxNlS5W9yiHGo92q9jU7pBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
عملکرد مثلثِ دمبله، امباپه، اولیسه در جام‌جهانی:
⚽️
8 گل
👟
3 پاس گل
✔️
3 بار بهترین بازیکن زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/96198" target="_blank">📅 04:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96197">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCjPYU1463Lw37LBZf3LTzTD43TwztGKxbeBNPT6Tfp_g2YIScfhL94TN15NcJDJ9234SKZ2WUKz9SWOx9neG-SG0sW-6wxaG8KfhjKRJzjpHgAsGjouJ9VzpcWht3V2o8oRFVp29J7jotCerdbG4f1NhffhjPN7xCR3ri6d--htoDbIVZuA4JkzAqMrVbn7l-8B-H4JMp6RFj2rIA9zAXQFva41gwMdUp528_6T-yIlav6fHGHfI4TAQp4TCC5rHBd6yD-rOrJXgpMvWsFPq-hAgHBYBWLuJoYmNL1X-SBt_nxFXpv37tdny24Wn7oMrfW6WZbKMOvsJLVEBFo5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمع خوبا امشب حسابی جمعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/96197" target="_blank">📅 03:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96196">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f55e113.mp4?token=mwndXVMYs1UlWGX4gBsLTcXUxoFtWrX7Mh2byyBpqWRTtG25KW37fCRJVdGpcaZk2h58GtGfglWPtdwYcxdUlQAEDZE7_-qAG_RgmFBA6yGyy40QVdfXqxU8Qi5zJKWzcpbfg-vwmWVK06FLQEcGfMu6YPClqzn9hSlX5sA-rTkMVeIeO5M19w2CRCpHV6rBlvam84mCDy3F6jGjITbnpAwVWNHuDH7_WsxIyCFoe2TLG-ZjsmkA9NyKVvnVvbY7tvMqNXQfGJR-zZS1I3hQ1-IL6BoSjdEmIkKHXOnTRXq422UXpgcee7usUb5W6TBX5AnUlW10YZhA5muWns5Uow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f55e113.mp4?token=mwndXVMYs1UlWGX4gBsLTcXUxoFtWrX7Mh2byyBpqWRTtG25KW37fCRJVdGpcaZk2h58GtGfglWPtdwYcxdUlQAEDZE7_-qAG_RgmFBA6yGyy40QVdfXqxU8Qi5zJKWzcpbfg-vwmWVK06FLQEcGfMu6YPClqzn9hSlX5sA-rTkMVeIeO5M19w2CRCpHV6rBlvam84mCDy3F6jGjITbnpAwVWNHuDH7_WsxIyCFoe2TLG-ZjsmkA9NyKVvnVvbY7tvMqNXQfGJR-zZS1I3hQ1-IL6BoSjdEmIkKHXOnTRXq422UXpgcee7usUb5W6TBX5AnUlW10YZhA5muWns5Uow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاله های نارنجی تا ابد
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96196" target="_blank">📅 03:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96195">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بریم برا شروع بازی جذاب اسپانیا - اروگوئه
🔥</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/96195" target="_blank">📅 03:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96194">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/aa83807f31.mp4?token=Y6AGNS6RT4rpD7rLYSQbmGEIyETv8auDFK0WgYva1fcFiWw7ks8MDaQU_OjZ-c3kpzgV6oAEn5RVq3LQU40m0S_qydvU5JevGhsFD4LafSJD2DmTT4IN1pN7imSnDsr_kUHIK_m1PnViZglIUZNDtPaOJD4MqccUouxZgUBiBoR9Vg9ZRwywxcDhtAONm5KOMNhwnmj0Hwq6yYJMVVhF_e5o9yAzyZYruLnTgtBc-bLzmsQlKd4HE1NZMrA5M8wXiPraRC7kzsl76lKwOgSLBlmnlPrJKU5wwldDKvA-aXkW6iz8l7L18cOL7NT0ifKsegP8eNiRTt-D0y4geG9vTg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/aa83807f31.mp4?token=Y6AGNS6RT4rpD7rLYSQbmGEIyETv8auDFK0WgYva1fcFiWw7ks8MDaQU_OjZ-c3kpzgV6oAEn5RVq3LQU40m0S_qydvU5JevGhsFD4LafSJD2DmTT4IN1pN7imSnDsr_kUHIK_m1PnViZglIUZNDtPaOJD4MqccUouxZgUBiBoR9Vg9ZRwywxcDhtAONm5KOMNhwnmj0Hwq6yYJMVVhF_e5o9yAzyZYruLnTgtBc-bLzmsQlKd4HE1NZMrA5M8wXiPraRC7kzsl76lKwOgSLBlmnlPrJKU5wwldDKvA-aXkW6iz8l7L18cOL7NT0ifKsegP8eNiRTt-D0y4geG9vTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی میگه بیا خونمون باهم بازی فرانسه رو ببینیم:
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/96194" target="_blank">📅 03:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96193">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0L4YsGwbQhdMvMmucOI2-Ryo_1Juf0yhCjOckghN-F3Qhwlw8aKelgDgwz-Q6pPIjecT7KU_kB2nLDsLvgBD9uB0iGBSReWYNJbq8JzV78h0gKGNNuGKcH0QzvRhZ62MUYsiTsACkLAmbOXx-kfm2qzrZUJciIM1YuU7auqPcUEpFsXZ0Y82rWwz5ejSm2s3r87augxEjDjSZU5fULiNJ_6t_hF1hFh6GedZO6tHWUz6qQYB2SLQGI_TVteuqy-4X-xP0VSNWF23Hmw8KIwG1m-Db1whzhWazxpQzpdyyVrUYsJi2hC16UpTeulaKvFewlpWKJwLMrFFTE9XvIz2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر هوادار اسپانیا تو ورزشگاه برای پدری: یا منو گردن بگیر یا پیرهنتو بهم بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/96193" target="_blank">📅 03:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96192">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzhB0TX-64GhVDwToTAjdxxrPl1W_gqv9rTRoCFaisJnntWrg0ZMT_zz9PF2lpjqRCc_6EppdY3HwUDhMs9-Dh3HcRXabX6Tel4PYvXQ2fnwWia3DLzF7gP9uB_98AQiC_HLspAYxw4wrIxM9TsEdB657KG4fQe227RgxhJ2qIhtEiBpmvWUfbjF3bAEq1RHk22YTZrx-cohudxPOflOYVqYhhO25f5ULd_d1AWjhdOV0foAqYmU3XeVlFUp24drFH_RqolUaoOFzXjVUsD3S3788lNuqNu_XOaMZ8inw8i_nhAsEhrFtKh9x_z4VIixTGISlb_gf_GyiDpOvh7O4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت امیر قلعه‌نویی تو بازی امروز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/96192" target="_blank">📅 03:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96191">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fn0Hr7XMbhL_aK1qy7YF3KEgRetHa390qfddyB6PlPGR-ZKfKFzHntPrYo0HITq7VXtvLf-851FsXdHumj09fXgMq7lNMHWoYildwVtAQgBiHOmfTXO3SYBomHFwfeMkZoO4XMUFY85iBICiMHl8ykMDtWygegWsIxkOrZFBh5_Ui-YRKEegPw-gmutBAQ0Nrej6sQZndzu4tvKAfJgKYCTztoTSImh97iABklEzOD7issH369elYnDzZ3CHCYRAjjXb-Zzf7KzNjO3B55mE_e2HJB6kaG8QAKpJ6ICpB9NsulRfJcyeJEfazFykP6flt2mCeMXbrT6gEIyd2WzAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
منچستر سیتی رسما مذاکراتش رو با ایوب بوادی استعداد 18 ساله مراکش استارت زد. مذاکرات با لیل قبلا انجام شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/96191" target="_blank">📅 03:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96189">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MM7vLGvirtgEaZsTYXs4H4dzo-5ubAcROFmP1cBv20iNfFOoqF7kR6fLDyEmQVA55ufYmFN9hdzMHXyke-ZyuhBLzh5Jkjwz-X9jyhjA1rrDvNQxXfiI35VmBiCai740DDZ3eGIToFhJGPFwKFRVVwnqwLrWux2SAtmR-HqxnWXiTWqA1NYOw0CdXV5QCyjzYPu3xVzi98Y62xbv7NxI4LMzadhQfFiJezHhdkmaPAF36n6J-Kz7hniutBdzApEhpf9WSViT7MEGNjiF4lJx7rmjTIgUrST-bnkwqg5iY0q5SO5R8nO8JOt-rZ9v4AkXbZ1GPZ7jPmGYKD0TJpkB7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcyNi2lj3ltgHJ1185vQCs0PZEscVcKlDsiFqnQi4Tr4l6AX764pLfQsZHeSMuUeQqJTEBiiUNKJqumdqLc2QNYvfSsGujfTUGmr0JVKw8q0ITh8ZmXsDUW8ZXgKn0lRseka3vaIr2an7WsZj7juXUx5AjB6grxmiWi9ulvgwArEyoakLIUiVNRE7NKjMx9LiKPA-dCMCWZfC6AsaRBzeEjXwqw8Oaxxp1ixfhvZ1nfyWZoaA7c9wMQugiKupv3Leot4bax-AQ49oShUYfvSbej_WpRa0WFMVLD3-fPDKTlT31aeN0PZwtWlrDuLTXhXnjViGuOzOTiHp21cr6KEWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/96189" target="_blank">📅 02:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96188">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsztGXFCYlxFmMKOgbZfAPRfqlZMWWKoYzcp6cv9KulvP-gDHO8P8v9TPVRPpwOHiMwagxZ7GUgnM_m5CE5vNIgJGcqkFtcPfBNjr1PbSqE9asG-UtWfltI-sp9Uf8gePq2sQoqtZj9-00omPeJROaeXc7Agq1VwQU5Zh-NFI-eM_it-X3zyxd_ifTwXLBIRZXzMaPw3E_YhnmIfpD6VZihB_XsZN1RDtE3zotnIr0bdJ9r1-FbDM8E-N3ejuruAuloplmSLjtSMny50ol2hJ7JYs1kW8CdmJb5L6WiBK1o9BJxnqTer3sg291y6z9dooy1hfZbyjvi-Wsr_jh1gyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دمبله سومین بازیکن تاریخ فرانسه شد که تو جام جهانی هتریک میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/96188" target="_blank">📅 02:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96187">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a22b294fa.mp4?token=QiIdAL_tYHduQHPVNeA7Rlidk9OhgLHBcMzE3mjNjNO3PvWeO0QRsL6Rb9jvmPFflFQSQ4LIc9duT2pB7rmiJB3ushMm2MEYb_Q11uF4fjrLJbYpgvXJtkrqqIV9XRCIfR9So9q1jMvBPqL2p8o9q8K3yZfTv4Up0kLc1YV1GfhT1WMAEof2hpLFUonj-uFHd5YrkCSJf9XtHxPzTX0gxVXil2cANgqG5RvYfsHqtMmYGd_X4p2XlMZgfYsWX-r1tEzzPTsts-oD3PePF4EYM9ke8jXic5DB1drcFQ_FH39c1mm51sztK57XxEOW992zH7oQH2j_uuv2aayVbu1DGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a22b294fa.mp4?token=QiIdAL_tYHduQHPVNeA7Rlidk9OhgLHBcMzE3mjNjNO3PvWeO0QRsL6Rb9jvmPFflFQSQ4LIc9duT2pB7rmiJB3ushMm2MEYb_Q11uF4fjrLJbYpgvXJtkrqqIV9XRCIfR9So9q1jMvBPqL2p8o9q8K3yZfTv4Up0kLc1YV1GfhT1WMAEof2hpLFUonj-uFHd5YrkCSJf9XtHxPzTX0gxVXil2cANgqG5RvYfsHqtMmYGd_X4p2XlMZgfYsWX-r1tEzzPTsts-oD3PePF4EYM9ke8jXic5DB1drcFQ_FH39c1mm51sztK57XxEOW992zH7oQH2j_uuv2aayVbu1DGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرکی بودن یه رگ ایرانی داشتن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/96187" target="_blank">📅 02:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96185">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QS4ucX0l7GAGi3vk4gFzBLRXaAH7NkCdcGx8C5RqJnhx7sNPJtWFYslaNS8vztNmxCYrw8eev4wsNUVLOLpZRjJ5kKmlOxaXVR429Re6sHby4YffK3fNvR1CO-C6kD9YcWjHf0HBUD2eLyuG1mLIRYlGjDjmCChj3FCOCn7ePvglFc2BiqP_joiZjStNg9IZwzyhVG_hRR75goSxPXFZxsP-gOeuathxWqQ01iTzlmtPIdPYt0vjIMvr63dVmqW1-mJ80-SmZ-8LU5eTSMzQ4cqst_1qFtHnpEx2pw9mHz6Xfe3xD9ngmfRfJecTEhOL3Jtx-Y3IiIdxGlWGJz-5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSvoIrQp0-C3qC8DEnKauZuTiaaj2lTg_BhyEoRPFumgMNKcbDD1HaErwUHq2R2q65d5iHavjRgovGs-y7dEv_K_0J-cbiVCn6higKLGEjKSEWEzsT4T6LXoA4RW0amEv7Tq9tlYCFbwHGm_1CnVZfOdmPDUK9jcYZa_82w0OLpt_yCX4YcY_zdY7GHdxioWK0O4F1GQCLxQdQ9ahhPFeRAEu0ryG9YqSeu_ycqm6L2jU3fAD7za8eS1EUWgITrOvwmnF0gh9djpGq3eDWM38RX0kV00Z5zaUBdhO4TWsFVUqQdjinJHFnaBZ2bNipQ_grMdvcRIzx2PIYeQwPGLcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇾
کیت خوشگل اروگوئه برای بازی با اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/96185" target="_blank">📅 02:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96184">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/96184" target="_blank">📅 02:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96183">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
با اعلام اسکالونی، مسی در بازی مقابل اردن استراحت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/96183" target="_blank">📅 02:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96182">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0796a912.mp4?token=EcfLREUEkLLmRc5hSTOhmfZoOU89AHCXszkCv2iNh6q8y2tJVtHgcuLzAABbtXL21ehFKj7rjZt3Z_DaicbYNBTsnYg9ImSPk6cPFJYylGGmtw6HJQVJuqJRLbmmA7jy1WvfuUXp3YqvpOXZzBESigN0TY1iK_7-Dh7E61quQ38CHOMzm8Dz9xwbuNC4tT8AZbHWe_FCNZCkQNPzkqrVmEYX2e1iWW79QaxAsqz_gDFt3W6mQ9JB3kUotYaWjRtEN6DjjemZcqTYWHf4Rf4Jkfm7SCM_enC3ZJpdXUAeN-tmQC9ej1tVvCYszMKHjgVC7lFLrK7qb29z4NFZiYQ60Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0796a912.mp4?token=EcfLREUEkLLmRc5hSTOhmfZoOU89AHCXszkCv2iNh6q8y2tJVtHgcuLzAABbtXL21ehFKj7rjZt3Z_DaicbYNBTsnYg9ImSPk6cPFJYylGGmtw6HJQVJuqJRLbmmA7jy1WvfuUXp3YqvpOXZzBESigN0TY1iK_7-Dh7E61quQ38CHOMzm8Dz9xwbuNC4tT8AZbHWe_FCNZCkQNPzkqrVmEYX2e1iWW79QaxAsqz_gDFt3W6mQ9JB3kUotYaWjRtEN6DjjemZcqTYWHf4Rf4Jkfm7SCM_enC3ZJpdXUAeN-tmQC9ej1tVvCYszMKHjgVC7lFLrK7qb29z4NFZiYQ60Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
👀
🇺🇸
هوادار آمریکایی که بازیای ایران رو به استادیوم رفته، قول داده امشب دوباره بره تشویق تیم امیرخان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/96182" target="_blank">📅 02:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96181">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAnMMhkzbSjKkeoWyUgAqDQ_432x6WNEvsAMKR4w4ZVpIqQWRDlRE5tOGS5nII38QEclMMqekKHzXqir8oko1AS_t7h56cqpCHPr0B8qZPD9bnC4yBXk68A7cxHbbVR9UP7XkvwHQ-X5mu8J1rIMHVlDN9UVPJ0iMatm_0OnqrdO-Yn7GariXDzcShH0CrcVjakr034JyUwtqMUUh03g3Hyqh7lTlV66DOqK5uL3j9dRwNBkhQMTnfC1PkB6g3FEywpQo1c-G-6EauTNIqGdTj7NyFWkuybrrhHFz64kLfadNHolgN2gnMnnyW9qSFaK8W4yurgqRpZQpKiM8mshJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب رسمی اسپانیا مقابل اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/96181" target="_blank">📅 02:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96180">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9970f0db9.mp4?token=dWvXomQxBwWCALAQby-6kip1I-2pWuUnYDA-R36kpq18kGxxiN9r61SjWC0JTu35JZoVphXHateqXBDj6N5yqdjj_lDXNwDirZ-YAH21SVzN-rfDpPojK6929a2XFZnqARbd_tU2vOsRnFaFnZ9Gq3xskA-bxXlnCztC8J3d2CmPuZJOM59JOduqNqkJiVe66R1IWF6aTqX2Umv4dxGgTIxWMzmwlT8iLhHUS9fx7f8EppjEVYCY4tjWN8m7yY98o2oRM5HSQ0amSC7dEj3Hi_JnHQ9FyO5S5cqVs981f-qKLsGetgWGTz2oZmJ516kEgR7TjkRNRN3eT1jJLio-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9970f0db9.mp4?token=dWvXomQxBwWCALAQby-6kip1I-2pWuUnYDA-R36kpq18kGxxiN9r61SjWC0JTu35JZoVphXHateqXBDj6N5yqdjj_lDXNwDirZ-YAH21SVzN-rfDpPojK6929a2XFZnqARbd_tU2vOsRnFaFnZ9Gq3xskA-bxXlnCztC8J3d2CmPuZJOM59JOduqNqkJiVe66R1IWF6aTqX2Umv4dxGgTIxWMzmwlT8iLhHUS9fx7f8EppjEVYCY4tjWN8m7yY98o2oRM5HSQ0amSC7dEj3Hi_JnHQ9FyO5S5cqVs981f-qKLsGetgWGTz2oZmJ516kEgR7TjkRNRN3eT1jJLio-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
خوشحالی هوادار مراکش از صعود به مرحله‌بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/96180" target="_blank">📅 02:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96179">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e9b9ed52.mp4?token=C4iA1lWlSqjH2jvPc5QUVFDkPWRkwWeiBvhMdp3wDpf8lPoi40AmXreOZlztGTLrCc4Ks0Tf_rqGj8xykhmhPiq8t8xzkIej8HGjhu64XhiMYNYEMBGU7371nrS2XNPIMrXOcIFMvWXjgEixgoWkfatm-7qMdDzedC1ZnM_Zr_QUxZGYZAOg_hjKaVmqiwMmPsd7VYmEhUZT4MwmVeH-uN0f6qhtVdOmKNmMPJhbQU_S6IAMp0KfhvZV2HttlJSC1xn0H9b26gpj_QkunBGdRLqZOC8VD-L_7vvHPeWzMT54g_5YcP_U0TFf-tV7HA2C1sVTAqRWwkTFTVErxrzniA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e9b9ed52.mp4?token=C4iA1lWlSqjH2jvPc5QUVFDkPWRkwWeiBvhMdp3wDpf8lPoi40AmXreOZlztGTLrCc4Ks0Tf_rqGj8xykhmhPiq8t8xzkIej8HGjhu64XhiMYNYEMBGU7371nrS2XNPIMrXOcIFMvWXjgEixgoWkfatm-7qMdDzedC1ZnM_Zr_QUxZGYZAOg_hjKaVmqiwMmPsd7VYmEhUZT4MwmVeH-uN0f6qhtVdOmKNmMPJhbQU_S6IAMp0KfhvZV2HttlJSC1xn0H9b26gpj_QkunBGdRLqZOC8VD-L_7vvHPeWzMT54g_5YcP_U0TFf-tV7HA2C1sVTAqRWwkTFTVErxrzniA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
بنظر با این پیش‌بینی، صبح کار دراومده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/96179" target="_blank">📅 01:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96178">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8F_spiSHFn3-woX2VRSGR3v6tSu6xwazBYfaZxww5Rw98cPHNmL8S-JEbg-UuZCOowWOzcC-HTuhGfDIte-nSzSP8fSUxF_whAY7LAHuFNUUhG8VzmiYoy9vVw5YoYNXHqkVQqDIVdqYNc8rgrBqbVCAWHy6oq3dl3wMQ-q9OWzWNFfZnJEuX-VwU6mtpz7sqR5Q4Ovq_5pXQaTMZaDHqtWvqxMQal50y-920_5-03RGrjWT7tBaK0LAYiig8oPTubcGoUxOFKep6fjaPxBFvC24dsWtfE_Mj5KzfZptnk9zblt775-T70Cro-3gREimtDvB240GucaRAS2SnNtbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب رسمی اسپانیا مقابل اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/96178" target="_blank">📅 01:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96177">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsPl2sWBUiFO6tHvu_rh4uUQHqI7ddo2vuJZXCUXvwAfIzKEjXR2SYC02olqovE1ocfM4InMVHxZ_qyQp4taBFXtPm3ywFh-pAC38Ai9pypnZpimBgbIUyNGFaY9_SLHLZWZOJ_DyKZybXLNMRujhCm_jrFsiBVRZ9UWyQrPDvWTSuvnf15oixox5vnhN64WKqV2eOOv2vz0j9cbPJE_HeOy8q9CdUzxXoyI_jTiSviEZTXdt60tn0dFu4_OMlqS0M_Xf2IaTc3I8DtpaeTDv3GMe9mWbKSR-LsKtYJTg_gSLxdpjuRJetY4A2t3sHNnxyFolM7jKwrrpu9fJ3m0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند تقریباً اولین حذف شده بین تیم‌های سوم شد. فقط یه معجزه میتونه نجاتشون بده اونم:
👇
🇩🇿
باخت الجزایر با اختلاف بیش از ۲ گل
🇪🇬
🇳🇿
برد مصر و نیوزیلند مقابل رقبا
🇸🇦
🇨🇻
مساوی کیپ ورد و عربستان
🇺🇿
و برد یا مساوی ازبکستان مقابل کنگو
این همه اتفاق باید بی افته که تو جام بمونن که بعیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/96177" target="_blank">📅 01:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96176">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbOk_ptpdfd1PtQ3idFnl0gXauhqH1iTSLJiaNeC3yeovJozb3FUdITYfhIPO9YURe-e8seh5SHryUQge0z4tTXy_-2HeNPadlblHgtISaCtOYRevW2qx02UDtLNDVcH7KkxF1jsCKGXcI7ExFrmDA76Y6gH4U4QQVwvR-t9W8tG4BZzX4OKg7tq0ADa8u6EZYp2XeX9w5lJB4O-MVore4wlEa43wejJC2yKe_5XMrRLYbY2gXvAKBArVPg8EkXr9IyEXgtjHWPvpXybXzgGA4_rKeT5TTzXaWP1QL3M8XPa5hHKlRnbq9dtbykFEHBpzzLfo34XH3iA-9OPFJTr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
ورزشگاه محل بازی اسپانیا و اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96176" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96175">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mj72ZZahWwN-9cLGAQV1WQxJVOw4IvvH6I8cTMK1lgF9FEfqVb09_t9omuUjRwWcT1vCqrqf4xrPDmUN7XptTsiLwTcna4qUHtz0eE2qXonPCgXkaeSZXpS-6Rawv00I__d2ggwdw1V1y7zctllPh2Bq-84Y6NYcgNGza4G87rz9rkOhgg9oqH1vCahHdkiL2x8KoQyi0ufkL4LVf2Dx7-6Ab1nccRKzpr1Ib9XEMMb5sE1XcbMLSptVdZkddMfp8c7sSRdxecv7q7oaTYTHNfgIpAGLCA2K0rFJ5K0dw5cXowEhnq0AVhdlOa9JxNNYDugJkYbQWN2FMWMM7nrLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگال اولین تیم آفریقایی شد که در یک بازی جام جهانی پنج گل به ثمر میرساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96175" target="_blank">📅 01:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96174">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
‼️
دیشب یه زوج ایرانی تو مکزیک رفته بودن بازی رو ببینن که اینجوری گوشیاشون دزدیده شده
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/96174" target="_blank">📅 01:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96173">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea90a3e17c.mp4?token=h06E__9CcIs_xBPSVp_EgI72_hnUdj1nLRJgxnle02idoW2Fy3TclklLMgH5j-L7nsZaiJQMGBiBTvDbv6qRjr03e_dJ9GJC-KcDPEWFIHS_mhfKo1ONcaZBIOrO1jKA6qrTCdDDf900zZw7KjeycHee4xuM4c0O5qNSXYppVDuKnPLin9FWiXwlre45djnPWh3tEi1_cAeZahc662NnYzc3ik0Sol7b7Fane0A-JII8BTm70dhhnL0qjJVrGNYu-J3nfiZzolz_Ii-X-vbClV2u9J55iOPZicpbS8FNDxG9Yf6oJNymagTom-41gAZd05lazU6j46S6qxqsQaMVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea90a3e17c.mp4?token=h06E__9CcIs_xBPSVp_EgI72_hnUdj1nLRJgxnle02idoW2Fy3TclklLMgH5j-L7nsZaiJQMGBiBTvDbv6qRjr03e_dJ9GJC-KcDPEWFIHS_mhfKo1ONcaZBIOrO1jKA6qrTCdDDf900zZw7KjeycHee4xuM4c0O5qNSXYppVDuKnPLin9FWiXwlre45djnPWh3tEi1_cAeZahc662NnYzc3ik0Sol7b7Fane0A-JII8BTm70dhhnL0qjJVrGNYu-J3nfiZzolz_Ii-X-vbClV2u9J55iOPZicpbS8FNDxG9Yf6oJNymagTom-41gAZd05lazU6j46S6qxqsQaMVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
تصور بازیکنان تیم‌منتخب ایران اگه دختر بودن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96173" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96172">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGS8A6fb3-am8g41dRaRI4uExctIpMkw-agOoKtKoFq0KqGj-4armYKXrAEoewjLHy1BZpwmdqWUbK25TYpKwS3FgDP44Tt4m7z3KUfkuGmA4-F5e4Se7P80uQjlwa48fh30UGdZVTocnPCkxQIXKP47Ivn7BIO-gWppYW107ATUObG2OTcWDjnZo7FngKiV8fMwhGyymPq4Vxrxkhk70_RPnoeinq35INrCLLUV_Nwm8IPVpuJK1dWjSgApcxDwuq4ZijnWcrMKDrggDceUGQq5PpNKL8RZN75L_VDBg971W4BrXJ1oVe4XRljDP03RfGgtfuZCZByAMBgKnTNTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ ریس‌جیمز مدافع راست انگلیس بدلیل مصدومیت ۱۰‌روز غایبه و ظاهرا دوتا بازی بعدی تیمشو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96172" target="_blank">📅 00:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96171">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozuTNizh7S4XOIbOmpCgURlPXv9wL2pbH11QOF5pFIX8l2AYiLCAUkI29NYv2yZUb4llt7l-k5ATYn2eayW4yT0te3SWHx5UF53UmCi_aNBQ3d1soltJ1QbGrnastPa0s5G2DIwnW2q6LtFzW0reReexksocoxr5NKg1A8JghFJBObpa_AzrADhv9ySEZEB4MUYGweK7kZUQQG35WESytD2U4qecdk0RdKTpY5RY6FxhJRjC8X2xHKQD87W0zTS9DmM5MbX--sScX6ImQWdUlCqKOWMymY33EWBvNTjk39euM79AvKlmhYpdLScTPk9TTt8pdxhhvf56vX4Okji6OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/96171" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96170">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImEatoFKfqu65Ge4uikliIWM0SkcyC00StKyybjDbzRDrTZeNHqBBbBWz-0CSWkJpEhrTjGYpo5UGGH-h4q9S6xwip0sB2bC6lgDYT9wqAiCyldD7icuUYJIC6uNkzdMheTVsiAZSM__-4_-Bnt4lhlWdxdVuDfEMg1QnPMMdvStXwLr5DleGgnpXU1SYybmCe6q6TwhpFpNKbG2u21z9VTnyG4xJ9hTUlEBOFzZyZn-KR1gu-IJXcJZKKxmQ1bykQKLRalppWiwBLocSEOiVeWLs2CTGbtOZt-ShoRCGtxrSsCVv5qCeBTKTUjfhoRWUQXACbwA1O3-dK94n1h3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله یک‌شانزدهم نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
سوئد
🇸🇪
🗓
چهارشنبه ۱۰ تیرماه ساعت ۰۰:۳۰ بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96170" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96169">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3_JTn35-3K2_UDA07AqNs7A-dUcdrAh1crjGPXYbSYp7jxzmeL59oW4LcW0whpnFzGrpQx0JFmL_BKbYqtsEl3ZLL1mtYtKuuoYtJwqQ_LCOpeTs4k9txGHVoarKAmfFIA0fixjvrdNO9ny_3KVsLmiUpGBUwWUikp4bQNBBylqprGZ5_NHtlQ3PlkCGCZVGjYeM6UVE4yYreayAOoFNekl-EosE_-hmrQxJ8Sn9nkunG_zQJBPySrT9yekXjARODwYfk8bG-aSIwHs9ETXW3rbVp5xa86UDWobQQJIPdda9Ten9cYEJqMktoyen0WooQvAqaaKC5G491ibQEz-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عثمان دمبله جایزه بهترین بازیکن زمین رو دریافت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96169" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96168">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjFE8MLTbnW1OZGVFUfVSqOS-kKXQ80pplhkwE3k8s6qpQD2aQJ6edgPn3A2E-83Bce0FXjQB-dEIy_skxHPSqj_5SKDK7ZOw0jvltRMjD40FBLViGy9BFMeYuWLvyQwopLxRZ9_4wdmCyPE76E9AR_2yDjNoaueDbMBUNA2J6wtbmp9DagKFxG2H7W7b_ymHtV2yWL9JLotQNKKE6eFuJGBHlS_sCDWTKWo2XDEo7bXgL4YEHVRq3KrX2WInB7e41UG1pUO2LBi8SQbjhQjtFXPQ-Xgw7uIbAq7yl0f5bT3ql_W2anJgHu2BuqD1Agw8X3tQfBhkl1hYXcAGWBLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله یک‌شانزدهم نهایی جام‌جهانی
🇳🇴
نروژ
🆚
ساحل‌عاج
🇨🇮
🗓
سه‌شنبه ۹ تیرماه ساعت ۲۰:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96168" target="_blank">📅 00:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96167">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری؛باراک راوید به نقل از منابع آمریکایی:  ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/96167" target="_blank">📅 00:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96166">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇸🇳
گل پنجم سنگال به عراق توسط اندیایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/96166" target="_blank">📅 00:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96165">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdFK7if_rV0GX_wfMxeK6xRlyrZxfUiteIugtVMpTDQywvlRtznEGO5IAxQiFvf0ZeTRichbfcOoCxRc6Uf9MUC2SBhht3QQ-C4WC7bqYp-1u9tp3elchTzjZMII_dGkYITRdQWm4LnNxZ-Lzj7pVgwUsxGL7NpJLVFqMQBFo_xrOQGMpPrbhrygbYZyGloYI0av2BGBm5FpvtZya2HH79eEV-9M5Vaj1xcljH-R6zaUD81e_7SAsYgomqcxDYvJm1tmczhelz7YRlRKr6dV0ShcLKVtxZNjcz8oGGHR5h-q3yWJ6Ee2M8qDM9Tp1SLUsdKFOJu1hAJ4zu_-_poegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|گلباران وایکینگ‌ها با درخشش ستارگان پاری‌سن‌ژرمن در جنگ صدرنشینی
🇫🇷
فرانسه
😀
😃
نروژ
🇳🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96165" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96163">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUSgaTBxKUD6XYApV0GOzlkm-L3jolT0slVu2PdKoqL0Ca_A3k8hOuyKT1PNRu9V6O7SsNduLWKBaceG_uAaiO23_f3vOflMb4BDJmkCoFFnFuULVqa6akDz6UkU5NbY1Lle8CfNcKtGlbz_gzKO6c3MhAYHcWv3cDzfyiaBgl3oee8N1ACOU-gSt_ukSO_e9VejrVoHGdepraiuGwTYQJ_XFzQqhtoS81hfKnhmQQncJh9dR9Rpkm5F9m9_dkwZB-LZfpj4O01VtbFcuHsYR60QLpsY0CLTJidSwsqf3zAxy-Eg029eP8pNycQAzoYxY3nkN2fhSVGj2d-rr5l-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/96163" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96162">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|گلباران وایکینگ‌ها با درخشش ستارگان پاری‌سن‌ژرمن در جنگ صدرنشینی
🇫🇷
فرانسه
😀
😃
نروژ
🇳🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/96162" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96161">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوئههههه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/96161" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96160">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فرانسه چهارمییییب</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/96160" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96159">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلگلگگاگلگل</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96159" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96158">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a0f064511.mp4?token=l6TVqUM8lbm34Md5YhevUXHhnliTRP5Zi_BqhVmsnGc6AVFazOwtcfVzyddIxEHYbKesSnhjXCMN7dAOAQj5hUeJsDZs-74h3eoAzMyFtxC7kVgKsuBpBQ36P7_zJiqpqr0rCbq6n5u7GmYPR2zrLMQdq4L8MYMi2h4SCjBVqFK7n0L6mYhpYJTf-xt7FEZYkzh-hgKwO2h5jTD9__SpysDgb3QFv2OsLSFOTCwMOgvDHpCv_QY7RzWgzf_BDcvI7vNfFU74QQv-mTPcK4-r1MGsmENxZeue1Be4DxuhiV7sGubyRXyr4MN8blDK6Htw4wIr9JxxGh5SvNB1s9vF2kjzCcsPb0O5fr14rtUpgzcEzpgX2umASqmx2Lu6WvgeyHLCi65y-e24rWBieUNaapQ2_OBgcMgtexfVdC3RpfWRV691SRKgrA1f3mTpSrijAp5qaZLG_8iX3kLUhmOJiMmpL4vsRegYqDVmMrlpVpGnAABx4ysMob4phOJ7Zt3ZcAuzXpBfWgDX_fbr80ccXUmNPlbejNMcNi4zk3ARpYoB9s0SJlBSQqc20nv_4Sq8DYaBziAh1at7rcZ_P9awKwGT9ucjk3thGX9ltOpGYUgQVQl0lCO93ALaqXrm3eC1eF8vKVXXFJbPo4KBwpKdWh9WcoGVaxCzpab5Kt9IJ90" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a0f064511.mp4?token=l6TVqUM8lbm34Md5YhevUXHhnliTRP5Zi_BqhVmsnGc6AVFazOwtcfVzyddIxEHYbKesSnhjXCMN7dAOAQj5hUeJsDZs-74h3eoAzMyFtxC7kVgKsuBpBQ36P7_zJiqpqr0rCbq6n5u7GmYPR2zrLMQdq4L8MYMi2h4SCjBVqFK7n0L6mYhpYJTf-xt7FEZYkzh-hgKwO2h5jTD9__SpysDgb3QFv2OsLSFOTCwMOgvDHpCv_QY7RzWgzf_BDcvI7vNfFU74QQv-mTPcK4-r1MGsmENxZeue1Be4DxuhiV7sGubyRXyr4MN8blDK6Htw4wIr9JxxGh5SvNB1s9vF2kjzCcsPb0O5fr14rtUpgzcEzpgX2umASqmx2Lu6WvgeyHLCi65y-e24rWBieUNaapQ2_OBgcMgtexfVdC3RpfWRV691SRKgrA1f3mTpSrijAp5qaZLG_8iX3kLUhmOJiMmpL4vsRegYqDVmMrlpVpGnAABx4ysMob4phOJ7Zt3ZcAuzXpBfWgDX_fbr80ccXUmNPlbejNMcNi4zk3ARpYoB9s0SJlBSQqc20nv_4Sq8DYaBziAh1at7rcZ_P9awKwGT9ucjk3thGX9ltOpGYUgQVQl0lCO93ALaqXrm3eC1eF8vKVXXFJbPo4KBwpKdWh9WcoGVaxCzpab5Kt9IJ90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
گل پنجم سنگال به عراق توسط اندیایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96158" target="_blank">📅 00:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96157">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تجاوز سخت و خشن به عراق</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96157" target="_blank">📅 00:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96156">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گل پنجممممم سنگال</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96156" target="_blank">📅 00:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96155">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7vdl8Tl1Y8AM3ag2ztmmrtBdAFZeXJ6LQFT66zetJ7himNbQcelHHzcGiGKi9iDBTat1k9NUZDKMxLFM-AzYzU06aoQdX6p569ZN1B8ljCukmubiLXH2Cor_STqhsyVSEGt2fG37xIzTMZrYQihoaIRpQuu6L8JwMxJuTYwdj3UqBnJvVcD7CAQiw8tlUFlazvAfXIHnEwELMHOkr_Rm1R7P99RjgSGJKg7r4iRdPFpTDXRLa8Sbw1EzMcK86A1NJ2Vktcp6x-rOGe21k_DVaiE10w1JILMwE5zwR1-3T_Vj87x4kAiElfJdAbbtkIQDg1BLzdqmEmL4BSlBh1iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دو تا لبای همو ماچیدن و حلقه انداختن به هم محرم شدن.
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96155" target="_blank">📅 00:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96154">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f26eabfb4.mp4?token=LNZCwLCHmWu6KKdf31F8Igq60yLL2jsDODsDKifTJYnrQzbKks-F_ei2XrXDet1wFNauJq0kzO5g4Zn0LoGNNVkAhHGF-v1MkCGp1ma-uaermZVPt3lkpz2W75wf-f6vAk5iSpkO5SgS0etlEN1CMHzDHxYE29CUO8F6nnHCEIW9Jo0o-lLRfPgQtPjxcOjtiAqeIEZTY2FMG9qWi8VgotM9Olu7A0jQR1suybAwDrkdgZTTS3eD-3_8VE8knfFDsl9cBLkIMCwAomXLkRCUyKpoD1yFu5upmehx4g_TYnDJHDLCJZVEqpoI7g_HZN-BvBYHe-e9pOg-d8ti_UkmUKPVgThF5GvCvJHRusf6Ob5mjzIImvrZP0wAJ5cjm3FwORC79vap77vp0Qg7MXxpO7TaCS02APzIuWmDuMvv-lYY4GdghgOWsPgiVdnUgNHRqYdIsupDmvZzJt3NeZPRRtlLp6ElxH5GNr0x3UOsyY1rDHMcj7W_ug6ihrV3UbjzNm6kXYq3D3lwoWf4gia2vzu1XjLuqlamH5IJ_0k5KvOX8HFLkDNZ5pxMArvXSSOrOhpOMQ8zE3Kr1juyaSQeTifm340F30ZUtKOhMl5-hYpEZff5FSRx_K7nOMeTV4vHHmvIocG4cw-tIn3mSRaKSz4qJGTUn7nNdx9JHaqUje0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f26eabfb4.mp4?token=LNZCwLCHmWu6KKdf31F8Igq60yLL2jsDODsDKifTJYnrQzbKks-F_ei2XrXDet1wFNauJq0kzO5g4Zn0LoGNNVkAhHGF-v1MkCGp1ma-uaermZVPt3lkpz2W75wf-f6vAk5iSpkO5SgS0etlEN1CMHzDHxYE29CUO8F6nnHCEIW9Jo0o-lLRfPgQtPjxcOjtiAqeIEZTY2FMG9qWi8VgotM9Olu7A0jQR1suybAwDrkdgZTTS3eD-3_8VE8knfFDsl9cBLkIMCwAomXLkRCUyKpoD1yFu5upmehx4g_TYnDJHDLCJZVEqpoI7g_HZN-BvBYHe-e9pOg-d8ti_UkmUKPVgThF5GvCvJHRusf6Ob5mjzIImvrZP0wAJ5cjm3FwORC79vap77vp0Qg7MXxpO7TaCS02APzIuWmDuMvv-lYY4GdghgOWsPgiVdnUgNHRqYdIsupDmvZzJt3NeZPRRtlLp6ElxH5GNr0x3UOsyY1rDHMcj7W_ug6ihrV3UbjzNm6kXYq3D3lwoWf4gia2vzu1XjLuqlamH5IJ_0k5KvOX8HFLkDNZ5pxMArvXSSOrOhpOMQ8zE3Kr1juyaSQeTifm340F30ZUtKOhMl5-hYpEZff5FSRx_K7nOMeTV4vHHmvIocG4cw-tIn3mSRaKSz4qJGTUn7nNdx9JHaqUje0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
گل‌چهارم سنگال به عراق توسط پاپه‌گی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/96154" target="_blank">📅 00:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96153">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سنگال گل چهارممم زد</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/96153" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96152">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a56fb088f1.mp4?token=qiw5sOE0VuoVX6wD7Y7gQP-g-xIDJa9fjk9PScP1yPX2tCLDwTwoI4cweEXdO4sJldbo734x7IVtwDEHngu_Gnf_-HiXVK-CCcrtTb7DRhe_RvqfA-c_oFVldtIUJitsmZs9hfxnQ5sWxSEQpATRUXwu2rQqiI4tDlMnyBGi3-mHYGzxYJ5NnlL1zLTrzkEuG99ExGzu5G9956QGGKfq190LZfweLkRsAvkrN8K4Jr91pYYyfgFSCCcmx2TLDbbG5OwXo7d4tb5Jq-75MjU_U5om9r6r2VD9gikRm9h-pVQk7F7y-MqV6gsK1pVn6IHNHVrIZCxN_u3WuxNWa9Rd-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a56fb088f1.mp4?token=qiw5sOE0VuoVX6wD7Y7gQP-g-xIDJa9fjk9PScP1yPX2tCLDwTwoI4cweEXdO4sJldbo734x7IVtwDEHngu_Gnf_-HiXVK-CCcrtTb7DRhe_RvqfA-c_oFVldtIUJitsmZs9hfxnQ5sWxSEQpATRUXwu2rQqiI4tDlMnyBGi3-mHYGzxYJ5NnlL1zLTrzkEuG99ExGzu5G9956QGGKfq190LZfweLkRsAvkrN8K4Jr91pYYyfgFSCCcmx2TLDbbG5OwXo7d4tb5Jq-75MjU_U5om9r6r2VD9gikRm9h-pVQk7F7y-MqV6gsK1pVn6IHNHVrIZCxN_u3WuxNWa9Rd-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔴
کنایه‌های تند کریم باقری به پیمان حدادی و بازیکنان پرسپولیس: بد بازی کردیم و باختیم
با صحبت حدادی شدیدا مخالفم. در یکی دو سال شرایطی خوبی نداشتیم. مذاکره با اسکوچیچ؟ این رفتار فقط در ایران است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/96152" target="_blank">📅 00:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96151">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09e259859.mp4?token=k9CA43Ycz7IEHEugJlC8qiRINe3HnJPwtzN5RUEY8j4KSnWL81vZxxbdLQs3qUPZpnvmv6MltwDGIopaqLMsqhWOlENFYTpZRyiYN2pNqQTbSrcUmsjdHF8_FbHw6HWQgqZ4LW6OHtYnsOOSrjQrK7MNgCCxJJeXEhQ8D9f55cj8yYv4vim4_MM_tKxwXiv0Jgn-SjRJJxhcTQ0OkIk73sikmSfRM01VWmw6HpgUzcxl5eINrKBDsb_MoBykThsysF2NzqW7qUuo9HPDRBPINZnZxcH8muSLQJgPw16sHAb1C4T5pR4vWKMpAKvorCKXInHJ31ckL5Fx5Uy7l8Ping" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09e259859.mp4?token=k9CA43Ycz7IEHEugJlC8qiRINe3HnJPwtzN5RUEY8j4KSnWL81vZxxbdLQs3qUPZpnvmv6MltwDGIopaqLMsqhWOlENFYTpZRyiYN2pNqQTbSrcUmsjdHF8_FbHw6HWQgqZ4LW6OHtYnsOOSrjQrK7MNgCCxJJeXEhQ8D9f55cj8yYv4vim4_MM_tKxwXiv0Jgn-SjRJJxhcTQ0OkIk73sikmSfRM01VWmw6HpgUzcxl5eINrKBDsb_MoBykThsysF2NzqW7qUuo9HPDRBPINZnZxcH8muSLQJgPw16sHAb1C4T5pR4vWKMpAKvorCKXInHJ31ckL5Fx5Uy7l8Ping" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
واکنش میثاقی به باخت پرسپولیس: مدیران پرسپولیس ابر و باد و ماه و فلک و خورشید را دیدند تا این تورنمنت برگزار شود که شاید سهمیه آسیا بگیرند و بعد به چادرملو باختند که این تیم حتی تمرین هم نکرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/96151" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96150">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ea98176deb.mp4?token=movXN18faMWKeXGlNx8C9BPQnTYSt5WnJCzSfnoqwcrGG0BaLoeb4RBFiQa3Q4M06MxOccQ3HZoxTLLXL4TOMf_mgTHvzAgSyf4ZPWkREs_9b1FRluGGz-0s0P9x8raQb8zB0R7-rlBLJFhK3KU5mTYjDyzU4zHGzl-VHwQ5Wr2fa2YfMoTlXEgILJE08aVkc-tfxtdYpYm4u4WJ1pUI-bFFNdrJHsHmIsY_fqBgaKluNkS_lAvcnfMx98njESpv5HicHc0VCsiX02fDQBIdv95zoLHObCkaxK4WiiuJ46S4-Be8w2DSJYwEH9Jk-vtZwkRZCxh4aY-cOFN7Wj-urx5mdxvivYNXAQxh_pYXaMvqgtwkNmlbeb6LyMGQqtXcyde8cuAexTJ0uG4iEZRNJhF4vQ1_9wNg1SL3iN9LBA3jNPU_Zm0siVc1q6CbwaQ-HwJO63e9EkueN7wsT1sfGAkuk1OfrCFR-4PqAl22jxKnG6ePaue1WizIBPNVrex9tG9fOdsb25TimuEpFnLrgZHe1ethx5p4n373XeG2A5__C7ravlKAjexbgbyNDELWmpFKYLFPvoxiEBppDQQ8sCrCg9FH2XIt_qwibFWarPQ-4YqC4gULdvkMPmhxThlnXFVccbJ_L0d5gXsc-AdEcjbDE_6PN0CZM-0XWnI3WjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ea98176deb.mp4?token=movXN18faMWKeXGlNx8C9BPQnTYSt5WnJCzSfnoqwcrGG0BaLoeb4RBFiQa3Q4M06MxOccQ3HZoxTLLXL4TOMf_mgTHvzAgSyf4ZPWkREs_9b1FRluGGz-0s0P9x8raQb8zB0R7-rlBLJFhK3KU5mTYjDyzU4zHGzl-VHwQ5Wr2fa2YfMoTlXEgILJE08aVkc-tfxtdYpYm4u4WJ1pUI-bFFNdrJHsHmIsY_fqBgaKluNkS_lAvcnfMx98njESpv5HicHc0VCsiX02fDQBIdv95zoLHObCkaxK4WiiuJ46S4-Be8w2DSJYwEH9Jk-vtZwkRZCxh4aY-cOFN7Wj-urx5mdxvivYNXAQxh_pYXaMvqgtwkNmlbeb6LyMGQqtXcyde8cuAexTJ0uG4iEZRNJhF4vQ1_9wNg1SL3iN9LBA3jNPU_Zm0siVc1q6CbwaQ-HwJO63e9EkueN7wsT1sfGAkuk1OfrCFR-4PqAl22jxKnG6ePaue1WizIBPNVrex9tG9fOdsb25TimuEpFnLrgZHe1ethx5p4n373XeG2A5__C7ravlKAjexbgbyNDELWmpFKYLFPvoxiEBppDQQ8sCrCg9FH2XIt_qwibFWarPQ-4YqC4gULdvkMPmhxThlnXFVccbJ_L0d5gXsc-AdEcjbDE_6PN0CZM-0XWnI3WjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
گل‌سوم سنگال به عراق توسط پاپه‌گی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/96150" target="_blank">📅 23:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96149">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1e0f39ac4.mp4?token=O6sNf7Zs0QPn4LaAspq2vAJrm_uC1OjZU3e3G5P0f3D1Azdq_bhZVNL8Bl6lYQ5wO3WdB8oNSJMm6K6Y9zkD2Cc0d8-WRD1QfzGyGLn59iDjvdF77-U_CLZJpuAXM_sfORKzXhPS4J1objR3OFfqXJA4BElBuZXbHJUenLpkhm_KM6oC_hla7QpG3yMMkGCNLnzm8Nr3jjLYXUqINOob_SeQdAiVI76uZsOnB730VpI1D2wM8xwGzbV_pfi5ZBgbsMAYKCRSugVXoOKjvdWqt0BEC0wFPm0nFzzP6tBoQGwpTYpu-MQfE87G8Rhw3zgzqGWaJXlJUVUOrvi6uBqknCfxx0PDUH9PHedLImBds2ztiBCZJ2SO0FXZwBcNjJyT8K04NbNO1Qudr9J1mibC9NW91MsctQ2BBvBi6xkxh1qbifhmBv73YleTxgMzNIxM4DfidlpHuEoinfOzXnlz2kVmgerVNPI0lWy_K7B8W9Gy7A670CLZuDmBO_asY5P0tmdgH-f-LatbTqAvn6vIAKU7vkcVLMQ8EgfQkChVyLVbW1XAF1MOp_pRA4pxurh0O43qEQ9XdETu-sgtXAax1pEHXeN9tSYMN_ulpynNRkX0pYs19R27Z_S-WxUuceBURG-yQT7g5saRu1QEtFolLF_Kmar4f4T4SHpHg9rZOdc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1e0f39ac4.mp4?token=O6sNf7Zs0QPn4LaAspq2vAJrm_uC1OjZU3e3G5P0f3D1Azdq_bhZVNL8Bl6lYQ5wO3WdB8oNSJMm6K6Y9zkD2Cc0d8-WRD1QfzGyGLn59iDjvdF77-U_CLZJpuAXM_sfORKzXhPS4J1objR3OFfqXJA4BElBuZXbHJUenLpkhm_KM6oC_hla7QpG3yMMkGCNLnzm8Nr3jjLYXUqINOob_SeQdAiVI76uZsOnB730VpI1D2wM8xwGzbV_pfi5ZBgbsMAYKCRSugVXoOKjvdWqt0BEC0wFPm0nFzzP6tBoQGwpTYpu-MQfE87G8Rhw3zgzqGWaJXlJUVUOrvi6uBqknCfxx0PDUH9PHedLImBds2ztiBCZJ2SO0FXZwBcNjJyT8K04NbNO1Qudr9J1mibC9NW91MsctQ2BBvBi6xkxh1qbifhmBv73YleTxgMzNIxM4DfidlpHuEoinfOzXnlz2kVmgerVNPI0lWy_K7B8W9Gy7A670CLZuDmBO_asY5P0tmdgH-f-LatbTqAvn6vIAKU7vkcVLMQ8EgfQkChVyLVbW1XAF1MOp_pRA4pxurh0O43qEQ9XdETu-sgtXAax1pEHXeN9tSYMN_ulpynNRkX0pYs19R27Z_S-WxUuceBURG-yQT7g5saRu1QEtFolLF_Kmar4f4T4SHpHg9rZOdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به عراق توسط اسماعیل سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/96149" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96147">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گللللللللللللل سنگال سومییییی</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/Futball180TV/96147" target="_blank">📅 23:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96144">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنگال دومی هم زد</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/Futball180TV/96144" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96143">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ee125817.mp4?token=JvpOuJQfgMsjLQRVRmomcDtBBxTS-S1KWBwajpeSpDbF9O5787kgU2Galo1nJ_vsQykIykRREuOyOVTWOnDK4PwbCOhTjRYG0QIZrE7ZDFAHJnL5wzaF1HEQnWY3Uti5YyqcBhkU_KvJHFB1tH1lsrV7idfHmFZt6kboZx_aYbr0D9kpllPYxChpI9PxEchqtv1Jx7uMd-Ypajsd9mNFShfzGIxYPu6sYaGo1mVHasQywG12gYYnmObTgFDEeJGTeKhz5gJzVitiK08ZyXr52i9_13AnKN_o6TSIAUu8OVrvI3E2hvIxPgpX9iQK0Tbl1-sqrJD4RgcC50ywT2Cf6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ee125817.mp4?token=JvpOuJQfgMsjLQRVRmomcDtBBxTS-S1KWBwajpeSpDbF9O5787kgU2Galo1nJ_vsQykIykRREuOyOVTWOnDK4PwbCOhTjRYG0QIZrE7ZDFAHJnL5wzaF1HEQnWY3Uti5YyqcBhkU_KvJHFB1tH1lsrV7idfHmFZt6kboZx_aYbr0D9kpllPYxChpI9PxEchqtv1Jx7uMd-Ypajsd9mNFShfzGIxYPu6sYaGo1mVHasQywG12gYYnmObTgFDEeJGTeKhz5gJzVitiK08ZyXr52i9_13AnKN_o6TSIAUu8OVrvI3E2hvIxPgpX9iQK0Tbl1-sqrJD4RgcC50ywT2Cf6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
حمله شدید کریم‌باقری به بازیکنان پرسپولیس: خاک بر سرتون. لیاقت آسیا رو ندارید بی‌عرضه‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/Futball180TV/96143" target="_blank">📅 23:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96142">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
⭕️
حمله شدید حدادی به بازیکنان پرسپولیس
مدیرعامل پرسپولیس: این چه نوع بازی کردن است؟ مگر برایتان کم گذاشتیم؟‌بیشترین قرارداد را دارید و فقط دنبال اسم و رسم هستید؟ گاریدو، کارتال، وحید هاشمیان همگی مشکل داشتند؟  ما نتوانستیم چادرملو که سه جلسه تمرین کرده را ببریم. بدون سرمربی هم باید چادرملو را می‌بردیم. با این وضعیت بازیکنان باید بیایند فسخ کنند و بروند. قطعا خانه تکانی اساسی خواهیم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/Futball180TV/96142" target="_blank">📅 23:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96141">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پنالتی برای نروژ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/Futball180TV/96141" target="_blank">📅 23:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96140">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
فوووووووری گزارش چند انفجار در سیریک، استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/Futball180TV/96140" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96139">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پنالتی برای نروژ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/Futball180TV/96139" target="_blank">📅 23:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96138">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیمه دوم بازی ها شروع شده</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/Futball180TV/96138" target="_blank">📅 23:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96137">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
فوووووووری گزارش چند انفجار در سیریک، استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/Futball180TV/96137" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96136">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/Futball180TV/96136" target="_blank">📅 23:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96135">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
❌
🤩
#فوری #اختصاصی_فوتبال‌180
🔻
اگر اتفاق خاصی رخ‌ندهد، اوسمار ویرا سرمربی پرسپولیس طی یک‌هفته تا ده روز آینده از هدایت سرخپوشان جدا خواهد شد. اوسمار بدلیل مشکلات خانوادگی و البته درخواست حقوق بیشتر نسبت به فصل‌قبل، موانع مهمی در مسیر تمدید قراردادش گذاشته…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/Futball180TV/96135" target="_blank">📅 23:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96134">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd73927f8.mp4?token=BJnf2rPfoq5Lz2W2NiTxScPDiSI_Cq7q2IVW_zkUZEwDQTxoK_VuCaVm-G4UT9OVrnRbqe-WdaOK9s6Ap8Nc1MQJtKHSo_Y5IzcjAFRTzOv5Q7gFg1b-YqWzVqGPaC0mhgAVL8w5gq8q92inJ1ysQmx22yNSve4nsndOBV7CBs-QM1Xt50HGc2Vj1laHOutiKhppuOHqckl-oDY75H1oWGiUIIi6-TXgxaNLCfm0K0oX7eU_prnx8WWxmIBWYYoMbWQHuKRD-JSNqI5KXMoqAYeg3st5qWPZq8-zwqoHMZx3wuN8Tbo1_YZnkwlxEJyT-ExLF_FILqc60mE4aeyuaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd73927f8.mp4?token=BJnf2rPfoq5Lz2W2NiTxScPDiSI_Cq7q2IVW_zkUZEwDQTxoK_VuCaVm-G4UT9OVrnRbqe-WdaOK9s6Ap8Nc1MQJtKHSo_Y5IzcjAFRTzOv5Q7gFg1b-YqWzVqGPaC0mhgAVL8w5gq8q92inJ1ysQmx22yNSve4nsndOBV7CBs-QM1Xt50HGc2Vj1laHOutiKhppuOHqckl-oDY75H1oWGiUIIi6-TXgxaNLCfm0K0oX7eU_prnx8WWxmIBWYYoMbWQHuKRD-JSNqI5KXMoqAYeg3st5qWPZq8-zwqoHMZx3wuN8Tbo1_YZnkwlxEJyT-ExLF_FILqc60mE4aeyuaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/96134" target="_blank">📅 23:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH58lxztJ9-Aws7qDXfKEbZz5HL59mF16H89fJNtxhkIpx9WMpJHVeVMEMsaP8apdHS9jtGOPrRnD81qPqkpHX4HSJs6wM-t8JYNswACkcTDaIAFAOQVhKwqItBnNuqSqGwFCI8NIcGFJ3FKIWwSjZmPPklFaxWt2RKqSjCxZRrY_86Rrb0CbjQAniH-ePZ8wp4dXJBQhZq47VbHw-_UDYV410dV0ONAGFzaKW7n7noWBq8J_AUiBnLztZK4aw8vhOxM_flZjiVPogY1k72RFqwHekLi4mP7HjxyCBhwpuQZBjPx_H-_d3-vWYGkhELARyMPWpE-ZACaZWkqS7QKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/96133" target="_blank">📅 23:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96132">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/96132" target="_blank">📅 23:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96131">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/96131" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96130">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇫🇷
گل سوم فرانسه به نروژ هتریک دمبله.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/Futball180TV/96130" target="_blank">📅 23:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96129">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">توپ طلای دمبوزو بدین بره</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/96129" target="_blank">📅 23:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96128">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چیکار میکنه این دمبله
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/96128" target="_blank">📅 23:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96127">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گللللللللللللل سوم فرانسه هتریککککک دمبله</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96127" target="_blank">📅 23:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96126">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0786fc77e5.mp4?token=KHVgyZ4ooyccQTIBjsmsfW-uC4-xna1NT9GdOXf_iV-Ja0af7AQkpaD2e5mWu57TOvE4988-mahn-vfNh_DOFPtPS8l-2SAbt6jZqExnitN41tmcnIEorN8DtpGv8OH5N04x0e938ZoEHhylPsseBWPa_Tj4O794lgiGgebPB7aL92MZLdn1IBxde75EIxvE4UiK5i9dY39x8XTGF92-XY0Hu0GoQilyVdgu9QV-UHCKIV9EMgEkh753_KnYOSGymzLgQAQfoN_bTX5W0qigPONV_0ifqNIOZRTYZ_-rndzMncc15QFkZYq08GjIJ7vZIP0AU-7MNoAlz82hc298-n_b8kudpqfPOFINh86gg2qfEvEe41SO_r49aT8F_bTnMTcymd5YWzbwkxNmkebJOac2s_sfT8LBbVKMw76DZsXg6Wn5M1cbeIlyWjV-3hKCPfkjZr71ySGJ93ybPl1Wq5nrry5YWmVKwajhUegojksgGkQOubqemsFM4cZohvk30hssBTvRSw5j4H_Ik6bdMy6gFvy_KPd1TBcuvjduhzwKpqLD06X0fitmiUpRGqeZBU3kIC7u1iZQzAM-ER8tA_1TMmw6Y0QVGhwpUHQxfn49w_XyYu6Qyb1sAewTysLm-S2TW-7sZ5EUcx3AfMtMF8MVxwnIsZRaYLKYxH6OdLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0786fc77e5.mp4?token=KHVgyZ4ooyccQTIBjsmsfW-uC4-xna1NT9GdOXf_iV-Ja0af7AQkpaD2e5mWu57TOvE4988-mahn-vfNh_DOFPtPS8l-2SAbt6jZqExnitN41tmcnIEorN8DtpGv8OH5N04x0e938ZoEHhylPsseBWPa_Tj4O794lgiGgebPB7aL92MZLdn1IBxde75EIxvE4UiK5i9dY39x8XTGF92-XY0Hu0GoQilyVdgu9QV-UHCKIV9EMgEkh753_KnYOSGymzLgQAQfoN_bTX5W0qigPONV_0ifqNIOZRTYZ_-rndzMncc15QFkZYq08GjIJ7vZIP0AU-7MNoAlz82hc298-n_b8kudpqfPOFINh86gg2qfEvEe41SO_r49aT8F_bTnMTcymd5YWzbwkxNmkebJOac2s_sfT8LBbVKMw76DZsXg6Wn5M1cbeIlyWjV-3hKCPfkjZr71ySGJ93ybPl1Wq5nrry5YWmVKwajhUegojksgGkQOubqemsFM4cZohvk30hssBTvRSw5j4H_Ik6bdMy6gFvy_KPd1TBcuvjduhzwKpqLD06X0fitmiUpRGqeZBU3kIC7u1iZQzAM-ER8tA_1TMmw6Y0QVGhwpUHQxfn49w_XyYu6Qyb1sAewTysLm-S2TW-7sZ5EUcx3AfMtMF8MVxwnIsZRaYLKYxH6OdLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به فرانسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/96126" target="_blank">📅 23:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96125">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bac1b0776.mp4?token=FSvXNOKvmsUyzy99XqfxnowKyILDr3PBa2MQ4YDKny-L-FJYZpStgZZ40Y5zh4pW6lI4RkKTetnt8Unyz8rU3dFs62FmQhG28q5_-Y6b3JtXsHcqBaskVuA62DfsoHHjgQMa7brD4YsN1Rwra7GSuTIN6I5FLYoiI-Y3lAPc4Oo5KK3R1I4VLV3HKujWlY5HAdPYtssv4q8zOitPZdxwkGNaXQUrVUk70SxLsQqejG9P2vh5W4y8uQBEZQ4ccgedDPUDR0H6uCtg5tqlB-p2NLqHk79QZrGiJsSAADtSBNylpg937Lh7-xHjoRfsyh91z-tZSZY-CBnlgIcnF61gdVJyQq-Dn55ZmjWit6SBSugoL-1ToIlKmRctRdghwUBfQKvPicErOV8satou4E2MWupR0o3ZXpXAjlf0zZRNs7m6kiPfmxMu6kA-HD9aGXcar2LGs6bFLtsIu9xziAvzYWiDBFt-jPhBCYBOQJ3nfIRDADNtqMwByxUfuq_PQcvzDewjacqeZwNd3OGnv_5KbOmOfhIJ5P-ln0xyCsvWxVMUVTrl6OBmJWers3CbTEOTeXf0ylExFccU1A2H5CvBnP7P8h8nUzS5RYWeaD_pvsDU8XAc7Km1eyTo7-s3LNbd1PCQ1x7eBNAFt9BV8dK-Br8NPaka5qYAwtYbAfULWUU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bac1b0776.mp4?token=FSvXNOKvmsUyzy99XqfxnowKyILDr3PBa2MQ4YDKny-L-FJYZpStgZZ40Y5zh4pW6lI4RkKTetnt8Unyz8rU3dFs62FmQhG28q5_-Y6b3JtXsHcqBaskVuA62DfsoHHjgQMa7brD4YsN1Rwra7GSuTIN6I5FLYoiI-Y3lAPc4Oo5KK3R1I4VLV3HKujWlY5HAdPYtssv4q8zOitPZdxwkGNaXQUrVUk70SxLsQqejG9P2vh5W4y8uQBEZQ4ccgedDPUDR0H6uCtg5tqlB-p2NLqHk79QZrGiJsSAADtSBNylpg937Lh7-xHjoRfsyh91z-tZSZY-CBnlgIcnF61gdVJyQq-Dn55ZmjWit6SBSugoL-1ToIlKmRctRdghwUBfQKvPicErOV8satou4E2MWupR0o3ZXpXAjlf0zZRNs7m6kiPfmxMu6kA-HD9aGXcar2LGs6bFLtsIu9xziAvzYWiDBFt-jPhBCYBOQJ3nfIRDADNtqMwByxUfuq_PQcvzDewjacqeZwNd3OGnv_5KbOmOfhIJ5P-ln0xyCsvWxVMUVTrl6OBmJWers3CbTEOTeXf0ylExFccU1A2H5CvBnP7P8h8nUzS5RYWeaD_pvsDU8XAc7Km1eyTo7-s3LNbd1PCQ1x7eBNAFt9BV8dK-Br8NPaka5qYAwtYbAfULWUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل دوم فرانسه به نروژ دبل دمبله.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/96125" target="_blank">📅 22:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96124">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گللللللللللللل اول نروژژژژژ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96124" target="_blank">📅 22:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96122">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گللللللللللللل دوم فرانسهههه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/96122" target="_blank">📅 22:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96121">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلگلگلگلگلگلگغگ دبل دمبلهههههه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96121" target="_blank">📅 22:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96120">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عراق اخراجی داااددددد</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/96120" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96119">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گل اول فرانسه به نروژ توسط دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/96119" target="_blank">📅 22:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96118">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dca6328400.mp4?token=G-jlWXh5dNnmFKC7-6BMT1aSVoTHH781KCicbTJ0H4aBmyWK-namPAte5PynhJKA3eFxyjXgMvya1MKASLu3cFZhOtDDhIprih5RRneTP9jklqxEAJBSSee4ucPVdOU3tcivMzVHNL_Tfc9DCC0ZMrOrWG6-XYxBTvIQgMpxF8dyU4UmHhLgiVliJ4SVIEMsfC-QbM08mo_lw7F_NyiSWZQ3zYncngr_tCP9XRy4i_0QAKDgVq4DGFa5J3Bq2ALeCW8S5YwT0zb_dK692lHgkeiHz4SpOSB_JdzYIrJKzGStV6tOXMLogPuI5kUGlpuGy0ZoK3pibLwqwoUO7Exq6GSiubx3_U43NLNdH1pU6toOpjJmB4jzWyWAkj0uvjhPT3q0t-OTOAfgI8Zd--0vO4GZeCCvs-pZzNvYIeTF3gPHdOYnBDCjZn5WKU-oV3nF6QuFvhhMsI7XrkmMla0uo-IyzigC-L75HMfyt_L3yVz4RsAtJtguAPa-swEwZ7NXsbz2XNy4gZT0-G1nPLGrSGLxsdWv7TuqbuVDDGIDtD5agNF1yj3512TPGxlS5GLvTI_0Sks5Y8W80DpHwR4sJPyZPzfoCjJf8i9axDFUfRUXqZe5GsU6Ds4fHqVumXU77ekyd_73NGbKvl12E4moo2eiFClHGPBwasUwpT_0Tkk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dca6328400.mp4?token=G-jlWXh5dNnmFKC7-6BMT1aSVoTHH781KCicbTJ0H4aBmyWK-namPAte5PynhJKA3eFxyjXgMvya1MKASLu3cFZhOtDDhIprih5RRneTP9jklqxEAJBSSee4ucPVdOU3tcivMzVHNL_Tfc9DCC0ZMrOrWG6-XYxBTvIQgMpxF8dyU4UmHhLgiVliJ4SVIEMsfC-QbM08mo_lw7F_NyiSWZQ3zYncngr_tCP9XRy4i_0QAKDgVq4DGFa5J3Bq2ALeCW8S5YwT0zb_dK692lHgkeiHz4SpOSB_JdzYIrJKzGStV6tOXMLogPuI5kUGlpuGy0ZoK3pibLwqwoUO7Exq6GSiubx3_U43NLNdH1pU6toOpjJmB4jzWyWAkj0uvjhPT3q0t-OTOAfgI8Zd--0vO4GZeCCvs-pZzNvYIeTF3gPHdOYnBDCjZn5WKU-oV3nF6QuFvhhMsI7XrkmMla0uo-IyzigC-L75HMfyt_L3yVz4RsAtJtguAPa-swEwZ7NXsbz2XNy4gZT0-G1nPLGrSGLxsdWv7TuqbuVDDGIDtD5agNF1yj3512TPGxlS5GLvTI_0Sks5Y8W80DpHwR4sJPyZPzfoCjJf8i9axDFUfRUXqZe5GsU6Ds4fHqVumXU77ekyd_73NGbKvl12E4moo2eiFClHGPBwasUwpT_0Tkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول سنگال به عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/96118" target="_blank">📅 22:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96117">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فرانسه اولی رو زدددد دمبله</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/96117" target="_blank">📅 22:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96116">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گللللللللللللل اول سنگااال زد به عراق</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/96116" target="_blank">📅 22:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96115">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شروع بازی ها
نروژ و فرانسه
سنگال و عراق</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/96115" target="_blank">📅 22:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96114">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqJASjRc0G_7wy6F1LfRGXBcJxCv019XlvcDk7L-HZMsf1qlGU43u2Awsnr-hAXOND_IRQ3esVj-Rm5CxDoin3D84J_y9McVRSzJkx7RzpmZu-ZwirF-Z5enWGenrNHoBHdjvcW_-8iq9_WzEO9z0oBusYeLKSfiyRe6jhv_B8bOgy34hIdreY5Fs28o0V16Zqp_mD2LSRq9R9xlRyo-t9l6jVFwMAcMjid3B2eYm6zMJlqskKhP-Upfo5iB4hLqo17W2nMcmajXXTI5YpSBziadbVcA2XYBSAGDgQZxUav_QWebKtbIXio27M-ClXiGr3XweIUwNiXlyPgSyHBZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کن 15 دقیقه دیگه از این قاب جذاب سوئیچ‌ کنی رو اون قاب زشت و تکراری جام جهانی.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96114" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96113">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/814f149c24.mp4?token=dn08eCI7db2S7-mapth74SVlOAwAJpxoqqhbVep0izAGg6oNKjewc9IBIN3T2jEFKcb8aJ5RmdFXJrJOU6Fvs5uucCrqWFi52IkuhvCG6JZd0qA2SVlVPYVVqdcVUIwuMmKe5f6rf9oOCnT_sm1JckcoGkWFLbyZ_ocrgCzP_55_iH9uXkU84I57Bg_oqYTgP0LJ0YkFgAKjhBWHFWjRTqs-Jg2itrZvAV5v57CLb-yNZhlb3URtJA2afjZc0v47rs019yeUuHNk3j41RtUXAs-3npP7PU_iLIjqThH2UsRQyfm3eG-B4cWL24sp-WfvGLDMp4tygIiKEHjj53RcLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/814f149c24.mp4?token=dn08eCI7db2S7-mapth74SVlOAwAJpxoqqhbVep0izAGg6oNKjewc9IBIN3T2jEFKcb8aJ5RmdFXJrJOU6Fvs5uucCrqWFi52IkuhvCG6JZd0qA2SVlVPYVVqdcVUIwuMmKe5f6rf9oOCnT_sm1JckcoGkWFLbyZ_ocrgCzP_55_iH9uXkU84I57Bg_oqYTgP0LJ0YkFgAKjhBWHFWjRTqs-Jg2itrZvAV5v57CLb-yNZhlb3URtJA2afjZc0v47rs019yeUuHNk3j41RtUXAs-3npP7PU_iLIjqThH2UsRQyfm3eG-B4cWL24sp-WfvGLDMp4tygIiKEHjj53RcLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
گل اول چادرملو به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96113" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
