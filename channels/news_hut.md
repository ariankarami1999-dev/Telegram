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
<img src="https://cdn4.telesco.pe/file/VHa-eR98vradtqzR8xtJ1_vEV2jaCyfVwjGtR31hyK81_MdXJ7QBOXY08NdNlIzf4wMWJ6Q_aQSwYmGGbogK770ent1mXgT53WKauAOvXr8TDp3FacRySC2I-9fQLRY54Y18DUzcSRRbMNSy-bH7akmGC5T6wqIVoyyzJgj6ouCreAEE0j-qHz5RWM7abKaPv0aZTjBJZdW9fscOsMFuDXopyw_7hCp1GoTQPaA5MLzfKE8tH_ee9fYINbcCU7SpHBNheb2OKn7fWGB_xllKx5KPrVjTvanS-2eeX9oiIZoACGMAqGqcBljNesxcNzVsAJkcmNbwMPAGpZsCuPJ0GA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 22:11:46</div>
<hr>

<div class="tg-post" id="msg-71786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=sJYmlQjVE6zomqaVbc3ZsW1L3atHktXoHYk2vIiXgtiicO9K464j0RKHqBNIieAF0OLx2Zt5Q-7vwvY-F-Qi9G74PtCzLP2zQvra4WFT2NKB2NmdJtqqhB0GwKbcPJy8FJu5uhqI3JSxIpk57wsYpnIzFIAxhSeOS20njc1dX_sUsqWckSmCzBDqnR9H51PS_0TDYNVrM7x2NEp6aKiWGYG346lfT-wz299a-qQaPGphPNupQ4T0Ow2DxHpheZDMwYSdzkG5q5b71WJzHb6bPGAjRHuZ2z1VOwzY3w-VvLh_Gr0WFX_4C5Gnp-8TK0CDATEYWQdQ6yHPhrtDokHdjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=sJYmlQjVE6zomqaVbc3ZsW1L3atHktXoHYk2vIiXgtiicO9K464j0RKHqBNIieAF0OLx2Zt5Q-7vwvY-F-Qi9G74PtCzLP2zQvra4WFT2NKB2NmdJtqqhB0GwKbcPJy8FJu5uhqI3JSxIpk57wsYpnIzFIAxhSeOS20njc1dX_sUsqWckSmCzBDqnR9H51PS_0TDYNVrM7x2NEp6aKiWGYG346lfT-wz299a-qQaPGphPNupQ4T0Ow2DxHpheZDMwYSdzkG5q5b71WJzHb6bPGAjRHuZ2z1VOwzY3w-VvLh_Gr0WFX_4C5Gnp-8TK0CDATEYWQdQ6yHPhrtDokHdjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واجير الونگکورن، پادشاه تایلند به همراه ملکه این کشور در جریان سفر رسمی به هانوی، پایتخت ویتنام شخصاً خلبانی هواپیمای اختصاصی خود را بر عهده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/news_hut/71786" target="_blank">📅 21:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#فووووری؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.  «تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها…</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/news_hut/71785" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR5ticVerR0egxFAZkqgYme_jA5NtTv31qmjTxtHI-wuxUCAZEYA9ngfTt8EqbBv6CAYQRwgTTZvDRHksbj1o4yrvwIUGchbTsFEHKZF9h6yNzrE1bL1hAyMszPFFv1VwYJwPMLznK6XsJYNTQlB0OCpSjRuCw3Vcyt196HnrffdNy8f3Yb_IXilAKwTLBqShXMguAafK_uQMKHWLweOQbj5gI-FyhMKAG73DqvwQFABLHRWz0Y-LGq8d0VYf9LEH15IoO7lLN7juSXJJYvOAaPA5Th7LApDY1rjvxjIbK339gIXpQ4y5IIX90hmMaB9q5j78Gmzt5u4pjW1_852sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فووووری
؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.
«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»
ترامپ اظهار داشت که قصد دارد از فرصت دیدار با رهبران شش کشور حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، برای گفتگو درباره گام‌های بعدی استفاده کند.
«می‌خواهم بدانم موضع آن‌ها چیست و در چه وضعیتی قرار دارند. ما همواره حامی و محافظ آن‌ها بوده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/news_hut/71784" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=tLk_9kqhHxU-9RfumsnyIdSEOITQ1l2InqPI74d9CkLIpTxm94tUyyxXhM1KjYa49Q9UbtHXegaSiaodjqavMvD5pcqFE-FWviK-r976x93wepGpL_5Ek2h3vY5nJe_pL_touij3Qar3AoNC7RHAICqr8pnfZO9Qhxvi5u5eL_WClwwr0zdHC8o71o5Me5Tz5y0v4BidFE_EzLjMdjS4zzC5aZzl6LXFeRd6DSh0NebluN4aAwmzptqKuoZKor_DB-ZcsDn8bYnRUpOROH6CfQ_Tkub_UABU9e6Cs1por4J_Oqx_AK_i9TVgud3ZTXaJBgi5iHvjGNrCrM_wkuN6zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=tLk_9kqhHxU-9RfumsnyIdSEOITQ1l2InqPI74d9CkLIpTxm94tUyyxXhM1KjYa49Q9UbtHXegaSiaodjqavMvD5pcqFE-FWviK-r976x93wepGpL_5Ek2h3vY5nJe_pL_touij3Qar3AoNC7RHAICqr8pnfZO9Qhxvi5u5eL_WClwwr0zdHC8o71o5Me5Tz5y0v4BidFE_EzLjMdjS4zzC5aZzl6LXFeRd6DSh0NebluN4aAwmzptqKuoZKor_DB-ZcsDn8bYnRUpOROH6CfQ_Tkub_UABU9e6Cs1por4J_Oqx_AK_i9TVgud3ZTXaJBgi5iHvjGNrCrM_wkuN6zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در شهر ری جانفداها با جمعیتی میلیونی رزمایش برگزار کردن تا آمادگیشونو به رخ آمریکا و اسرائیل بکشن!
@News_Hut</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/news_hut/71783" target="_blank">📅 20:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71782">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC1lkLU0Mjos9n2EPbzOJblOEHYii6Ppbdx_ECBFy9kO-mPYGfDPotDEvLy8S5jBcAqapdu1OavngpI5g-0jrd9NQ3V5hK2baJwifXzgcfO_LUkkh2aQzCDZ38IKj4M-pUlyatCSAzpxteATYqzk5H_lAThczEI6Me9Zewkiwp0kTv_F68FQy9q7Q25KmGsLNXyBEjs5vu65tYhrUVF5_NvLEaIq_dgRlWy4idirVzT5WhVsGGnmfwGX3PDbb_7KJo2Rn6LcxWksQzEhkZY-x1y4swMGt2EUuMYTFRBL2ZDm8soRJSqCoE0YSgmSvrlMetOS9fzPFd5epl5JpanePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز، چین در پی درخواست عربستان سعودی از پکن — که پس از پیشروی‌های موفقیت‌آمیز حوثی‌ها (انصارالله) در امتداد سواحل دریای سرخ و پیرامون باب‌المندب صورت گرفت — به‌طور خصوصی از ایران خواسته است تا به مهار حوثی‌های یمن کمک کند.
پکن به‌طور علنی خواستار خویشتنداری، گفتگو و ایمنی کشتیرانی شده، اما در گفتگوهای خصوصی با تهران فراتر از این مواضع عمل کرده است. ایران در پاسخ اعلام کرده که ثبات منطقه به پایان جنگ آمریکا و اسرائیل علیه ایران بستگی دارد و همچنان مشخص نیست که آیا تهران به درخواست چین عمل خواهد کرد یا خیر.
چین هیچ‌گونه تهدیدی مبنی بر اعمال فشار اقتصادی مطرح نکرده است؛ با این حال، روابط این کشور با ایران از وزن اقتصادی و راهبردی قابل‌توجهی برخوردار است. در همین راستا، یک دیپلمات غربی اظهار داشته است: «تهران و پکن به یکدیگر نیاز دارند. چین عاملی است که تهران نمی‌تواند آن را نادیده بگیرد و پکن نیز خواهان بازگشایی تنگه هرمز و تأمین امنیت کشتیرانی در دریای سرخ است.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/71782" target="_blank">📅 19:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71781">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=ApPd9LUD0et_a-1oQ4IOMJ9Iu7YEx-szxbTvnz0kzNJEGtFyanT1s4-Jx-8MkwCly-l38ACILCEBDR3_tgT6cBUFIB-6VHO9JaWzzcgGx3sgz23e02ROU33ltwiKe-EGY7QvniiXME3Jy3RWZg_BXoud_-ox8Keb3pkypaovQv6Ts30BuJG5SHFnL0umlbaWuvOjTjGl_vL1NvQw8HF6mEQWniB2Ohqo7RBy6Y6MBI-jfMIinboNI0Am-WGTHFqX_kjpn8etsjTQ9O_G8VaRQRBBSP3JmcmvCO-wBBRowYcN8RK2TYvQwAVa3KeGdkJsjbT6OvU0W7UD89H5_8BJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=ApPd9LUD0et_a-1oQ4IOMJ9Iu7YEx-szxbTvnz0kzNJEGtFyanT1s4-Jx-8MkwCly-l38ACILCEBDR3_tgT6cBUFIB-6VHO9JaWzzcgGx3sgz23e02ROU33ltwiKe-EGY7QvniiXME3Jy3RWZg_BXoud_-ox8Keb3pkypaovQv6Ts30BuJG5SHFnL0umlbaWuvOjTjGl_vL1NvQw8HF6mEQWniB2Ohqo7RBy6Y6MBI-jfMIinboNI0Am-WGTHFqX_kjpn8etsjTQ9O_G8VaRQRBBSP3JmcmvCO-wBBRowYcN8RK2TYvQwAVa3KeGdkJsjbT6OvU0W7UD89H5_8BJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عارف:شرمنده مردم عزیزمون هستیم
واقعا از مردم عذرخواهی می‌کنیم، شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
نمیدانیم چه کنیم، نمیشود تورم ۲۰ درصدی داشت و رشد حقوق ۵ درصدی!
واقعا شرایط زندگی سخت شده و مردم رو درک میکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/71781" target="_blank">📅 19:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71780">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=hG_IAWaPasMVMsRhcVa-umGLQ9Mz5eLFu_apoSxq3rsF8SVlrwB4HTRYLppjYBXLUMTfvYWx-MHkZulmdK3RkaUjU4FpI5WY2Tu0J-d0hrfNzlwuv82khkAVp5NAic2_b8ggz1LswXPJkEa4XAdE1oyVs-gEvgn_qDya95f4EIereZpg0WXa7JzqEoTN0N4jtpZJXfpZa_BFuHyMPeLQDmuWLT6V3U-znSb753KdiJ6iCSJ5ChbuGvUwRZyTaF2kBVCn_hSWCa4mKjJJypfoAOlUrIcHSQ5tcO4GkVmwsbyIfU0HKjD_FPH-A39u1R8hbgtQWldTnPFaAvYip1oG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=hG_IAWaPasMVMsRhcVa-umGLQ9Mz5eLFu_apoSxq3rsF8SVlrwB4HTRYLppjYBXLUMTfvYWx-MHkZulmdK3RkaUjU4FpI5WY2Tu0J-d0hrfNzlwuv82khkAVp5NAic2_b8ggz1LswXPJkEa4XAdE1oyVs-gEvgn_qDya95f4EIereZpg0WXa7JzqEoTN0N4jtpZJXfpZa_BFuHyMPeLQDmuWLT6V3U-znSb753KdiJ6iCSJ5ChbuGvUwRZyTaF2kBVCn_hSWCa4mKjJJypfoAOlUrIcHSQ5tcO4GkVmwsbyIfU0HKjD_FPH-A39u1R8hbgtQWldTnPFaAvYip1oG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلافروشی از اون مشاغله که نکات دارک زیاد داره
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/71780" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71779">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=b7_8JdXKo45Jn4FudUaFnxRH_8zch1aPqDQUsreqD9W543anFrHzDmRo9SyBJoh96pqd7Aahnu-G2yS2Uibglz00DTni-uMgtr6y8n5bDSvKcorqmkGiwgRG9M4qnmP8MVkinqWvvMP0SGuEb4DHlT8KX8hh96IiIBuuQk7AHV13UnwIcGDB0Qjlsg_7UAXK2FUbtpp3u1Fj6QwoiYKbB4dRcbr4pZJv_6zIhug4qqHOzWey8opLLJzltV-r_m5AUm8dR_VON27sOoj6gn8pNnCSus4Ztw41ZGjs5tCoNUeATPE6ErGRQSaa3EGoKL_zg-9-jdPz8UUb6BpCPnX2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=b7_8JdXKo45Jn4FudUaFnxRH_8zch1aPqDQUsreqD9W543anFrHzDmRo9SyBJoh96pqd7Aahnu-G2yS2Uibglz00DTni-uMgtr6y8n5bDSvKcorqmkGiwgRG9M4qnmP8MVkinqWvvMP0SGuEb4DHlT8KX8hh96IiIBuuQk7AHV13UnwIcGDB0Qjlsg_7UAXK2FUbtpp3u1Fj6QwoiYKbB4dRcbr4pZJv_6zIhug4qqHOzWey8opLLJzltV-r_m5AUm8dR_VON27sOoj6gn8pNnCSus4Ztw41ZGjs5tCoNUeATPE6ErGRQSaa3EGoKL_zg-9-jdPz8UUb6BpCPnX2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش اهالی یه روستا تو هند که حدود 2 سال از وضعیت بدِ اینترنت و شبکه 5G کلافه شده بودن؛
زنگ میزنن تکنسینِ شرکت مخابراتی بیاد و وقتی طرف واسه بررسی دکل اومد، گرفتن و به همون دکل بستنش و گفتن تا مشکل حل نشه، آزادش نمی‌کنیم :))
آخرسر پلیس اومد و 6 نفر از اهالی اون روستا رو بازداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71779" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71778">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71778" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71777">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUqSkFnpYiHV5n_S1wpkXzLAbgLlF8WO5qVlBWfBoZ8IV3nRdy5wUIeJEYK8GcMHhcY3lOR-yUpgqu74n4xqG4G8q6d09ulyz9zorLWYSLsDwBE5wLgKGGurjCux7CFN2Ui_A__9yGT_Mogvbv4K0TP-crqmL90skbKbuPhaV9xiYTYHUeopYRaPinDCzmKausThA0CtPhjYlbYRCnWaIz725eWtu9QkJregGyNvtedo8V4VkP4apcfon0klowVBoDhZWDkt_-9AB5sO2h3LJciEobcmLExk7XrCrERIzNA7uhAfemujqXZEiiEXhGrw5-3kWiwVD0Z3560kpvmRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71777" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71775">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=rfqMDEhI7OvznA4XP5FzbA3uvegcZPx3UkuCoa3skDzxUH8MUt5SbpLTqMJy9JrWVnOelLuJY0YHVQSvPFSgso8OoC_GSeFkU2G1q0PWKUouYBaDEGvxHYSxfOktv_bMalOWAPcNBTqhNIeNPZlFBDPCd2buXzYTLjniT1O-NyjZ9tZnJMlGAEiHpaw975q0Yz6uUksJPcejaTMb6WqJBwzGl73hkXZECH6fVSOxTP5W6VBiUlKh1kjx-cZv67YJgySZtfg1nDjHxDbJqEH90higObWaSlJe5JdGVcsmLq1dL5z2obxr1P0ky2JL01x-8JDAlz9thtyZPqq3KiN1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=rfqMDEhI7OvznA4XP5FzbA3uvegcZPx3UkuCoa3skDzxUH8MUt5SbpLTqMJy9JrWVnOelLuJY0YHVQSvPFSgso8OoC_GSeFkU2G1q0PWKUouYBaDEGvxHYSxfOktv_bMalOWAPcNBTqhNIeNPZlFBDPCd2buXzYTLjniT1O-NyjZ9tZnJMlGAEiHpaw975q0Yz6uUksJPcejaTMb6WqJBwzGl73hkXZECH6fVSOxTP5W6VBiUlKh1kjx-cZv67YJgySZtfg1nDjHxDbJqEH90higObWaSlJe5JdGVcsmLq1dL5z2obxr1P0ky2JL01x-8JDAlz9thtyZPqq3KiN1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تگزاس اونم وسط قم
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71775" target="_blank">📅 17:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71774">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=po88ecTCmfFYBTyQkBJ7CPZljYSPjGioknYTf9Q8LOkl58VGfIxlFzhxzBOviszJYM-SXrBl1EVPte2TqZR-XXK5FhWWmNV6sb2judaFfnEX_KPklPD3QUYrYg1oE838eL1PzjsMlKREpBGm5OJPSTrNyoG49ofrvPXR3rwY_17LxdAd37ryTSjfOgKX05KI8m8ok-r6GGEeceszIrl--BYkV0RUQuCBHiXJG585AS_rnKZkTZDx3WN-igVvE5wSu3_sU5GIuo0Jcv4K4HDHV7A0rRrB2WRBeA9wIVFJD0baOkS72We2mSXWpk_Pe-pomcYIpAvU4wYO6ny2NE_gYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=po88ecTCmfFYBTyQkBJ7CPZljYSPjGioknYTf9Q8LOkl58VGfIxlFzhxzBOviszJYM-SXrBl1EVPte2TqZR-XXK5FhWWmNV6sb2judaFfnEX_KPklPD3QUYrYg1oE838eL1PzjsMlKREpBGm5OJPSTrNyoG49ofrvPXR3rwY_17LxdAd37ryTSjfOgKX05KI8m8ok-r6GGEeceszIrl--BYkV0RUQuCBHiXJG585AS_rnKZkTZDx3WN-igVvE5wSu3_sU5GIuo0Jcv4K4HDHV7A0rRrB2WRBeA9wIVFJD0baOkS72We2mSXWpk_Pe-pomcYIpAvU4wYO6ny2NE_gYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
میل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ تنها تضعیف شده است.
تواناییِ عملی کردنِ این هدف، عملاً به‌شدت آسیب دیده است. ما به وظیفه خود عمل کرده‌ایم، اما هنوز کارهای ناتمامی باقی مانده است که آن‌ها را به سرانجام خواهیم رساند.
ما حماس را نابود خواهیم کرد. همچنین، پیش از هر چیز، رژیم ایران را شکست خواهیم داد. ما آن را سرنگون خواهیم کرد؛ این رژیم سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/71774" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71773">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=jM8iszzvkv39uVR1EKXRQt69jsKXtmdimTgUTYxXpc_txlj3efs6hjK_EKxdwM_hofE60uMG7LAERR11xWJZlTIXSlV2M-NTa6wqhmAXQ0Nqam4WpkIUGZb78-V7XYbi0E8bglsMUuLsjdkRMkDQWOFkKYlBET9laMu-t2HNf9YX2ppCAVUfZYa7pYxcJ24wtCQMq39F7RPjSvqyNSiEaMj8hVmXUvTSMr_YfunxRZ2EJ9wS93UPdebFuwfA19-6sQGhwjZz3CgYmut94d8lmUSl2O6jeeP9U-w6XhZ_WWW3eC4vWicYKJyvIpKWpsK7LekEa4egk0ygPIgHIveLXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=jM8iszzvkv39uVR1EKXRQt69jsKXtmdimTgUTYxXpc_txlj3efs6hjK_EKxdwM_hofE60uMG7LAERR11xWJZlTIXSlV2M-NTa6wqhmAXQ0Nqam4WpkIUGZb78-V7XYbi0E8bglsMUuLsjdkRMkDQWOFkKYlBET9laMu-t2HNf9YX2ppCAVUfZYa7pYxcJ24wtCQMq39F7RPjSvqyNSiEaMj8hVmXUvTSMr_YfunxRZ2EJ9wS93UPdebFuwfA19-6sQGhwjZz3CgYmut94d8lmUSl2O6jeeP9U-w6XhZ_WWW3eC4vWicYKJyvIpKWpsK7LekEa4egk0ygPIgHIveLXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو یکی از خیابون های همدان یه مرد به یه دختر تعرض کرده، مردمم متوجه شدن لباس و‌شلوارشو از پاش درآوردن.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71773" target="_blank">📅 16:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=Be30Td9hnIzTAlkGbUUQdQ__Stkv0t2_z4b_SkmZ5Sd2NBFjhISp0XCrRlsyxXKk_k_PmGdsk9gexqlcXSnHATTUhJODfid2-5jJIb1EBSK-dqKzcuKIXB5bXoXe2X0n2qaco_ZeD5z6ZeB3NAWcogouYSx7bkpGeMoBHDFsoY6npzYOqu71V68TAy7PoB4R6_8uEWpQhPH8vlWeQlFrBZQhhxj_agmD35n9dqglJhJ18y-aOc46kHqAB2AAt4R-3aSNTe_RDUDBmWYPmbTKHO-eHvkBi50DhNWirK_e57O2ates-DkNvw3fU6oUEv0TXdVK4vWgrHhsJ_u214PHGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=Be30Td9hnIzTAlkGbUUQdQ__Stkv0t2_z4b_SkmZ5Sd2NBFjhISp0XCrRlsyxXKk_k_PmGdsk9gexqlcXSnHATTUhJODfid2-5jJIb1EBSK-dqKzcuKIXB5bXoXe2X0n2qaco_ZeD5z6ZeB3NAWcogouYSx7bkpGeMoBHDFsoY6npzYOqu71V68TAy7PoB4R6_8uEWpQhPH8vlWeQlFrBZQhhxj_agmD35n9dqglJhJ18y-aOc46kHqAB2AAt4R-3aSNTe_RDUDBmWYPmbTKHO-eHvkBi50DhNWirK_e57O2ates-DkNvw3fU6oUEv0TXdVK4vWgrHhsJ_u214PHGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو سیدنی سویینی برای اولین بار تبلیغ عظیم خود در میدان تایمز را می‌بیند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71772" target="_blank">📅 16:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71771">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d6312725.mp4?token=e-W-HNbGqS9skzTWvdS_-RXTGRJq4jLf4WR0KaGRza2ZgvA37aQZnjiQhEbqTnMvERbIaqitTio8r-J2GVGtscqFy7SAZmvSaxJbC1SoNxyp0XY9Q3ODDGzdjP8cwgh10zt8-yB7AgAkftdIjRL72BEu994EeuS2UTgkGbQHFhAN-t_lBvk9NU_J_4M0bSRavWHmXBzz7oclg0ImMq2G0OztLXI6Gm4bzWoREGC7xQYSSvpfARDQ-CiVm36Zeb57zdnNbD02KVxgInfH3X7NT3oY5AfOjt1QT_OmeY7bIGD0wizrzVLtqKhrs_5R6oxVZTLg_sazo3q7aaX1a9ZSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d6312725.mp4?token=e-W-HNbGqS9skzTWvdS_-RXTGRJq4jLf4WR0KaGRza2ZgvA37aQZnjiQhEbqTnMvERbIaqitTio8r-J2GVGtscqFy7SAZmvSaxJbC1SoNxyp0XY9Q3ODDGzdjP8cwgh10zt8-yB7AgAkftdIjRL72BEu994EeuS2UTgkGbQHFhAN-t_lBvk9NU_J_4M0bSRavWHmXBzz7oclg0ImMq2G0OztLXI6Gm4bzWoREGC7xQYSSvpfARDQ-CiVm36Zeb57zdnNbD02KVxgInfH3X7NT3oY5AfOjt1QT_OmeY7bIGD0wizrzVLtqKhrs_5R6oxVZTLg_sazo3q7aaX1a9ZSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبرائیلی:
ایران ظرفیت گنجایش ۱ میلیارد نفر داره، میتونیم به هر فرد ۴۰۰ متر زمین بدیم تا به ایران احساس تعلق کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71771" target="_blank">📅 15:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71770">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=ez4tJ2gzSWrtvizDgm6Fek0Jc3NU6OtYm8McAvd13oXx6S1j0idHcKFAG_HlbhYj8kqDWlMjjb_5nvrohgBCUw6GT_PRVDm3vHcMM8oL2kuCjxMQnIwVzih2hZnMkhju5gFG4wScjahiR2dvpNU6p7mJ76bkJ2cJnuzINczmKGEvkY7uyXFylYCaNRp8nS8pvgT9PsG2FZPJ-r8DeBvTcdLEbqjCR5IKIrUVisHdtV35Uu4dqKA5e8eVYxkgpNhLchduDf459DeTGUwQhXzE5XwCkeyKErdfIW9YUwxAYa8WHrvXfJ-8bzO18z6A7IAJjucZjjAziI4UjJGFLq13rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=ez4tJ2gzSWrtvizDgm6Fek0Jc3NU6OtYm8McAvd13oXx6S1j0idHcKFAG_HlbhYj8kqDWlMjjb_5nvrohgBCUw6GT_PRVDm3vHcMM8oL2kuCjxMQnIwVzih2hZnMkhju5gFG4wScjahiR2dvpNU6p7mJ76bkJ2cJnuzINczmKGEvkY7uyXFylYCaNRp8nS8pvgT9PsG2FZPJ-r8DeBvTcdLEbqjCR5IKIrUVisHdtV35Uu4dqKA5e8eVYxkgpNhLchduDf459DeTGUwQhXzE5XwCkeyKErdfIW9YUwxAYa8WHrvXfJ-8bzO18z6A7IAJjucZjjAziI4UjJGFLq13rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این گربه به محض اینکه براش موزیک میذارن، شروع میکنه هد زدن :))
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71770" target="_blank">📅 15:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71769">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حال و هوای تهران در ایام تاجگذاری  شاهنشاه محمدرضا پهلوی، سال 1346 خورشیدی.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71769" target="_blank">📅 14:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71768">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMArnhiL3obpzA8WfaS9ANveEb2KQpelbtdcSjqnUDAi9KoUpUTxm4RdYPPpakNk29-AeOeNxvVajGWURn_WvW7AEhjyIW-07W6b1fGdXfz3YjQjp2aqUBeo81rihi_HCEcf8_CfpwaY0atD8GzaGPjDPm-4qzwlm9Smkdhxn1roilIarOR4x_IIxOP1AIIo06QRBOigly8nwy-twCuhmCeR6Nku4NymxcBxmptEX3jFng6mdwgfHnoJEVNKmhbqSv9xUPzBwaVUpzXZFAh7nJ_-TViWIg7a18dEzVFSpUg9mqvI5Zc1LUKIVstXnQKGP7Dqnkly54nxHieVAUeY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ده فروند جنگنده اف-۱۶ ایالات متحده، به همراه چندین هواپیمای سوخت‌رسان، صبح امروز پایگاه هوایی «لاجس» در پرتغال را به مقصد منطقه عملیاتی فرماندهی مرکزی ایالات متحده در خاورمیانه ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71768" target="_blank">📅 13:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71767">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0a15Cb7HfDskf4tHZPXhz0OVTHphwVZBKRHSuE8e-_933pQCmpFFWZnysBfYVrN_YKhRUwl1nJbLAeYb0cWGG8Z7hgvuCVd50DKN-EWQTAzepfIT77KYpyXxkbryofbOA6k6OpLwtCcFRfEbvN7z3ExwtsmFT4R6U6gHo5oKHckcaqmrH4XBcyl05dXkG14kMdttt_HAnWo2fToVGVGgrXDmHpxuzQ2J4l6eETri8NgW04Ol_kZwErDr2bnUP49SKjqyfhCmMtS5Y4mddZWKwcjbkt9vy2OTSn6m8TgpAFQ86c4-tYQRjrNPPQ5N7-PBmHydlMERJTVs5lbJK8X0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک به اونایی که بالای یک میلیارد تو حسابشون پول دارن، کارت سفید میده!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71767" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71763">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKNFXQD22cKhoEG-WYi84hKg0RhVjcghh5VI3QRhEGA3E0OTIyHIAbu2N_AFHpB8bE5pU65qsFxQahcmtZqV5oqvzF5qC3S_A5ytACddmpfMXQ1EYdSq2jpDfftBEdMTJz4fk-EkH226grJvKgmL_zdxosGg0igGkCpuaRs0r8FnjrSrM_JLF9ZYOf_O67Fgaia-Ui971Z5jFhn_Gu0ae6PEaureEI9taCzgldJI8FzFjusxNyBgFdbPFn8jQzQxCJ_0kULykyMc0NImsLyhko5o2jfWA2X0srVaCdvANExky7PjSEXY8kj2ZmC4zzmLGUh4pTNTXScQE3dm3nBMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6wrSEmVWq9ckxF5edkQ-IYDvK7OmqwfXToANRUtuUCL1FwgbkTs7FKQuG92SQrttFhDzQD0OsVIZO990doWXurxKVu_1zkC1NTJIizJTD9bxbfURjQJ8iONDqsbYU7zXshgW56_gNSNV9VDA8zUpTBySWz6mGsc6MNhUKmV5ZfsIKTkSYd8uY5e7qPemHmKcoWp1QlWJAUhjNJLw8547E98wdnxyAmiScRm3bdmvE7xFgD7I7LHtnG9GTGTDHXLBxw-qKt-P_6MNKZiAgzStH7YHAxF0GFbFWBNLZ9hBKGk-lxZ-_9fgPVuzt7esBSYip3VuLPnbmIS79zi4gYnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBvMert7ND8fhHPgspDJhg0tWz9TEBIGOx72qW92iKHmHxB8Q2yX6PJ2SnGU3EG1BECk06CHvBoSsBEDOxvGDA0kKv2AgabGzc3NR8qJSDqfXJPD7V-cmd0q1iAhZWlY-TIwCKK_o6Cl1PZRLaDfYvy3ZlCnxnd4nBFGI1DI9m_YXK4yd-cW3TQONH6E5k764r0Yp5nclcDmkPDAzwfyBFWgYgdKryhpWOi_7E9UQkWeqnqyvwKN0sjeEG1B37vR1XqxKQzB1p4xZhYZLUbzMs4sYgHbsZ_PF-1PpSCXQ-gDZ1ieeLjvn8LfE_HIXo43PSZOlVinUggnaDO8Ac5ZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMrMwK1ROC_79riddj9VfghCbdXLzOCMULMg7p17KidE6QlIczffGGcHrEL7WSp6KyfgodPSEYcSc_x4gSQA8VS05Nkxfrfg6954HdCshJRZE1NTMfxtR0FpHr5x78P3t0IWdL4Mx2aYsSyVSOwSZmo3CILQr7A1EqKHJ_n8xLpQJ1MNFvBYautiooJXf6eY2DNrKAHsTyIy-NOKBCtugcqDwEkcarjsEgNK0zFiR3VaYtuB6H3l5vJxc8h3saheIyhnDF5PlwmS2AM89UJyihVi1NSCXRf8gUBVpB3vEJy1uovv5aCyQO89F6GSqTGPEATMLDP0CXiHvfhMtgi68Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز ۲۶ شهریور،تولد کمبوجیه پسر کوروش بزرگ و روز پسره.
26شهریور؛ زادروز کمبوجیه دوم، پادشاه هخامنشی
کمبوجیه دوم، فرزند کوروش بزرگ و دومین پادشاه شاهنشاهی هخامنشی بود.
کمبوجیه پس از پدرش به پادشاهی رسید و راه گسترش قلمرو هخامنشی را ادامه داد.
مهم‌ترین دستاورد نظامی او، فتح مصر در سال ۵۲۵ پیش از میلاد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71763" target="_blank">📅 11:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71761">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNnP-0AlN55vdKQfinAhKfsGx-WGfNBHQHWeAUGRFNbbvh3H5i_Lrcn7nQXMA1EHlYQ1nE8eg__GeZJmANpQYZeVTbLeznhCncf7wVLT20c_eMIrX4prWGGM0ef5vBtAWY2W3vh0Xy_slP4AvfI146ck_hZlhOixjM3uHSWLBvSehLErDpA7NAFj_AnCIuKkW8tKDDeNaTr4ydwlmiefG8l5ckgKHjGBd7KDp7mIzO0TeK9pNnPv2MLDx3fcZaO_qia-yCaF4PnSTCJXr1G9LyZdyv36DA5JPlnpcQV-IgEHJNNlHY5ntEUxucFt5eqSVevy1QB7zHlg0PhY2Z5bEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=MSU-2qu0HljiIXKguGYCRidGLJis7xyUvwjfP2RhocKFCdDMSoxHqGHqMy4_3ygUsvwC3HUrCjBaokVkTdOd0eZj3UHmCAmGCoEoteSCUCls39fIr4q5ndaiYMYyNCC0vTY3-rWf7Kt7TDoviGxvs1OHBIFSgdrJNyNyDkClrx7PXNIU0ImLMoX1Q5KzoBPZg9TxAwyQCGp4VU1DkhMd_KzY9FKvdRJaypDGok4YgB8W2AE09p5gig4_G2zBbZiS0Dv4BBsSrVjPDXNpYd393CciEG0t4la5vHrv4Dk9BY0Ow5o_EycLkImCsPRPV9A717BIrN2Wojn3GtUAuN3Ptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=MSU-2qu0HljiIXKguGYCRidGLJis7xyUvwjfP2RhocKFCdDMSoxHqGHqMy4_3ygUsvwC3HUrCjBaokVkTdOd0eZj3UHmCAmGCoEoteSCUCls39fIr4q5ndaiYMYyNCC0vTY3-rWf7Kt7TDoviGxvs1OHBIFSgdrJNyNyDkClrx7PXNIU0ImLMoX1Q5KzoBPZg9TxAwyQCGp4VU1DkhMd_KzY9FKvdRJaypDGok4YgB8W2AE09p5gig4_G2zBbZiS0Dv4BBsSrVjPDXNpYd393CciEG0t4la5vHrv4Dk9BY0Ow5o_EycLkImCsPRPV9A717BIrN2Wojn3GtUAuN3Ptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اوکراینی شبانه به یک پایگاه هوایی نظامی در منطقه روستوف حمله کردند که منجر به وقوع انفجار و آتش‌سوزی شد.
حملات پهپادی همچنین پالایشگاه نفت یاروسلاول را هدف قرار داد و باعث آتش‌سوزی در محوطه صنعتی آن شد.
این پالایشگاه یکی از بزرگ‌ترین پالایشگاه‌های روسیه است و ظرفیت فرآوری بیش از ۱۵ میلیون تن نفت خام در سال را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71761" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71760">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71760" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71759">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvwG-Mkqwz4lZ3pMsUfv86oC-tChLm5t3VRZId64GZ9VnAS3YFmucG1tdwXjjUdMNBPXaPXMInrtvK4QZxerRdf5Sg5XkQnijmWW3_crOCI32_j7fRRxl9qBjhsGCAMN5_5XMhw4Sjjfh4Tit8IwaFuwIv4ZYVHVtpRpW9wuZZWAMbi7ItsKVEagckOV3SN19IuZrI19PVkbDChEPg_jZ82cC-4d9NGVT5VJb-vuO60su0zWV6CTwWIaaxzeT85qRwN-pnbW_rggn3uqOYis6A0JXHaFElxj01zQYwSisYolN8dJ_twxJc-5its3_AF_0RZE_F8OmY-6fAzDGRvEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71759" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71758">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=UQjRmU9X08Q30VYX1U1gL3Mx4BFhw8QO1H8SBIqAylPxEAVIXdI4pcyvL6HtlBlQNhtZNkLnduTb4LvuRIJ9ZkH0NJJL7I2siGIAXDxXKdvrgkfCPyLinBDyvRDFucB2U3kiZcFMnMhFeZ09CqUwdelsKWoyl4rUUHy4qGgLXgUNEmbeXJTfCbuEK0oPRO25mUq0QCH1uzX_dR6NqvmCVSMqAKHCytikjx5oKIwXeIe-c4buT4iEwiti_BR_0DfNPPwwlO9w-FcE31-FFydwZ6ZgxnAFT9LvcppFkDQRqXkbKeRKf1wSaXbaAuss7L77n_9PCYy_RYV4Q2UxGQdLzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=UQjRmU9X08Q30VYX1U1gL3Mx4BFhw8QO1H8SBIqAylPxEAVIXdI4pcyvL6HtlBlQNhtZNkLnduTb4LvuRIJ9ZkH0NJJL7I2siGIAXDxXKdvrgkfCPyLinBDyvRDFucB2U3kiZcFMnMhFeZ09CqUwdelsKWoyl4rUUHy4qGgLXgUNEmbeXJTfCbuEK0oPRO25mUq0QCH1uzX_dR6NqvmCVSMqAKHCytikjx5oKIwXeIe-c4buT4iEwiti_BR_0DfNPPwwlO9w-FcE31-FFydwZ6ZgxnAFT9LvcppFkDQRqXkbKeRKf1wSaXbaAuss7L77n_9PCYy_RYV4Q2UxGQdLzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی یک تک‌تیرانداز در رقابت‌های ایرسافت!
خوبه که این یارو تفنگ واقعی دستش نیست!
همه رو هدشات کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71758" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71757">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=gFFx0OM07oZqe2z1oD_9fD3ERz-qLVKTV9uYLARBESFlI0sF0HuW2tw6Bkm6PLWzShhB69deYBOQIBzjDIJeYKn1gLVURekZ6MtIZDBQeHV9MrFmwC6rA4U_7UZNPeAqVCeAhTdPEYo5RaD0xPj67pf1fmDR541Ltp0m4VYWrwUzUm7qro_A1hqb64EjboPP0kXJ5WAZao_UkRlqgIukUeC3QMX4suhEbswbEjpW6cVEW7WcC_02kTZyA1aAKhwBJWrRYZxSggJyS9RJBTjWh8ohoDc8T_ZVf7Hp_Rq8Rp2zp2c2DoGwZZmOVE1MpC_l5lsLaDrvK3wMgwR1l4xJbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=gFFx0OM07oZqe2z1oD_9fD3ERz-qLVKTV9uYLARBESFlI0sF0HuW2tw6Bkm6PLWzShhB69deYBOQIBzjDIJeYKn1gLVURekZ6MtIZDBQeHV9MrFmwC6rA4U_7UZNPeAqVCeAhTdPEYo5RaD0xPj67pf1fmDR541Ltp0m4VYWrwUzUm7qro_A1hqb64EjboPP0kXJ5WAZao_UkRlqgIukUeC3QMX4suhEbswbEjpW6cVEW7WcC_02kTZyA1aAKhwBJWrRYZxSggJyS9RJBTjWh8ohoDc8T_ZVf7Hp_Rq8Rp2zp2c2DoGwZZmOVE1MpC_l5lsLaDrvK3wMgwR1l4xJbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات سالم در تیمارستان یمن
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71757" target="_blank">📅 11:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71756">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=RBT2UU8E9IDoqtgILFbHme62YH2uDf_zNQ_vdCtunUjvtpYJee8fifUrC_pdmE7YLEr1yKFSSlypcaQade4Q4SenJN_n1bGJQStg6vvG6eL8Oz7BbjdeVgqlMMrYw84-7cXIa210Tb9VjCbJKVpffBETOoYh1DPGcUUIhuI7-Mf6oEotOTHeXwN7k8c04x9GaUoK7AI8VHU0X-p-Huqnklyr3NrcStHaeLMFYN8vSgl62y-o4BavfBaJhM5xSHx3BxNajIRhrY-kvETGreVmgeHDhtZuvWcv9HusxIJZooTcQSKcOYGcBpBobNrnR0JRwEUm5gLbBKjdW5ODrtHP_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=RBT2UU8E9IDoqtgILFbHme62YH2uDf_zNQ_vdCtunUjvtpYJee8fifUrC_pdmE7YLEr1yKFSSlypcaQade4Q4SenJN_n1bGJQStg6vvG6eL8Oz7BbjdeVgqlMMrYw84-7cXIa210Tb9VjCbJKVpffBETOoYh1DPGcUUIhuI7-Mf6oEotOTHeXwN7k8c04x9GaUoK7AI8VHU0X-p-Huqnklyr3NrcStHaeLMFYN8vSgl62y-o4BavfBaJhM5xSHx3BxNajIRhrY-kvETGreVmgeHDhtZuvWcv9HusxIJZooTcQSKcOYGcBpBobNrnR0JRwEUm5gLbBKjdW5ODrtHP_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
قیمت بنزین برای شما بالاتر رفته است؛ اما این بهایی بسیار ناچیز در قبال کاری است که ما انجام داده‌ایم. این را به خاطر داشته باشید.
ایران نمی‌تواند به این وضعیت ادامه دهد. کشورشان ویران شده است.
ببینید چه اتفاقی برای ایران خواهد افتاد. نتیجه‌ای واقعاً خوب در کار خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71756" target="_blank">📅 10:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71755">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اکسیوس:
انتظار می‌رود ترامپ هفته آینده در حاشیه مجمع عمومی سازمان ملل در نیویورک با رهبران کشورهای حوزه خلیج فارس دیدار و درباره جنگ با ایران و برنامه‌های مربوط به دوران پس از آن گفتگو کند.
پیش‌بینی می‌شود که در این نشست مقاماتی از عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان حضور داشته باشند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71755" target="_blank">📅 10:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71753">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDZ21w6H7xFUzpp12IedqzAQaF_p3sAPP9-VrpqZL_I1t5X2ib8xACXLOclXl05POGNUedyqhvrslzzx_JlSNZ9ahCtKEvI7AhN1RiBbk2S-pbM63UsFGk0Yeo1rQ-guVI68emE8rX80kfr8hLibQ0lYTgHXH-u1UPjRdxgyHG7OXNrLBEvRu5wRf3Py7DmS3bZVBLdyrvc-mqDPWeZiE1uwzz8WaMMOIbhL8pUZJ9g5Mg6KSISz3pQe9Wqy3I-E6QomXFyiKF3145l89AtZBqZakj0CHiS0X7ydzC1Oc--2iIVb5WgcdGB0nOItVbZVwqwoylLAr81GOVNAGTZBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cba858231.mp4?token=q2lPQQ6JwP9wQGKZqESk-G2fBjnTyAgW0WpwFebXbGM6tCOQF1TOXr_ru01VlqXYm2lbygPZLUak0lrgBaWvZzf_N_RAGx5xSEVoQpgAf46smEEj5Zyi_vhRI0eAThFLJ9YG0MupQxWwGWo41KbMTVBiZxAEC5c4EpytOTFqAk7sExm_zaAc_KjoaOquO5Tn0IQC4TBrLECm85MgA2AU_QjlR49YvKy6L6mFoUV2AdDrwf9r-r5P5K4RNeox4E45tHJYXoWHQfukFMulC97MQepOyrT2IogXHu2XCPerbvf-pfSlYIrbW-gyXJplCpmLgnx3990C8eHVjwGK8PtcgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cba858231.mp4?token=q2lPQQ6JwP9wQGKZqESk-G2fBjnTyAgW0WpwFebXbGM6tCOQF1TOXr_ru01VlqXYm2lbygPZLUak0lrgBaWvZzf_N_RAGx5xSEVoQpgAf46smEEj5Zyi_vhRI0eAThFLJ9YG0MupQxWwGWo41KbMTVBiZxAEC5c4EpytOTFqAk7sExm_zaAc_KjoaOquO5Tn0IQC4TBrLECm85MgA2AU_QjlR49YvKy6L6mFoUV2AdDrwf9r-r5P5K4RNeox4E45tHJYXoWHQfukFMulC97MQepOyrT2IogXHu2XCPerbvf-pfSlYIrbW-gyXJplCpmLgnx3990C8eHVjwGK8PtcgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">« امیر نوری » بازیگر؛ چند روز قبل یه مصاحبه کرد گفت خیلی پولدارم و فقط میخورم و میخوابم و از زندگی لذت میبرم. حالا دو روز قبل چنان تصادفی کرده که با سطح هوشیاری پایین باید سریعا جراحی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71753" target="_blank">📅 10:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71752">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoQQY08Fw_ID2GPb1amnn4RIOLAPpiDkmFGK9I7lJoaQyt4zwGxOxOMPUQU0r33_WYJCx-W36U-nn-Cwk1lj3bJwSZAgCcVu9LbTJZgWx7gce-vE1ASyw3HfI-FwYjLq_Yc8Obu8jG9frLpdeFsWEjC3AXAgKfNzZuDQLFc-BDwgyksOJzfDfPeVCZ8c4n6n8lDKN3cLHmIWxbzmo0-ZLkDq5n7D7hVFcb-vjizWoaaAclSZBGYmVL6soc9ZimoFZ1qSEdm-gvJbEUAmITQOPM8sno15CAbpC_wX_b8PwgwIQAuNjW-DqPYZlhUZxKf8WPwMcBA4H1NCc_BXbvVMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا بعد رزمایش جانفدا ها توی شهرری عقب نشینی رسمی خود رو از خاورمیانه اعلام کرد
اونی که اسلحه اسنایپر رو برعکس گرفته فقط
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71752" target="_blank">📅 09:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71751">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=hep6yodm3bsPI2QkmJmxyFf9zEtPcRbmV86d5_ZIYrTRe2X6JAxuepOJrteRDkuecopuGrnOcbbL1K-wkhE8FYJuCrXNDiA_czEw1lE1W8Nm92tBan37HXZ_ODTj2r4AA-7MERZNy3ZNz3_Psmcjh-PebrXUjFedF2CUm6eCGKySni53nXMbJZaX3ptmp0bOPJlXYZY2EYOyEappJnd8BjuNXcIz382_yG9Mf9WkTjB0JXsy_kStr_rtrmgjXHcP96ztyyicNlF2Z5Bc_6tCbKtQZlXRKuYPdW8s-G2fyBbecu5GxoCWWqOwRotzlgSurovxaN9czRthpM5teqEccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=hep6yodm3bsPI2QkmJmxyFf9zEtPcRbmV86d5_ZIYrTRe2X6JAxuepOJrteRDkuecopuGrnOcbbL1K-wkhE8FYJuCrXNDiA_czEw1lE1W8Nm92tBan37HXZ_ODTj2r4AA-7MERZNy3ZNz3_Psmcjh-PebrXUjFedF2CUm6eCGKySni53nXMbJZaX3ptmp0bOPJlXYZY2EYOyEappJnd8BjuNXcIz382_yG9Mf9WkTjB0JXsy_kStr_rtrmgjXHcP96ztyyicNlF2Z5Bc_6tCbKtQZlXRKuYPdW8s-G2fyBbecu5GxoCWWqOwRotzlgSurovxaN9czRthpM5teqEccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در میان مردم اسرائیل با استقبالی باشکوه
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71751" target="_blank">📅 09:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71750">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=FO24KDqyTRuo4mwvgwkEjKaYKxidnVnHsfuwwTnqVcWf3evMyWZjpSd-soepPXVoDT1mwBDv1DSxlebTOZOrzroLTyC1HdSCGQRsKyvV-IYb1wF0AF43aB8EGAR9yHubETryo8DmCq7YOFiRMzInfvag3sxlOixs9Z_tt_kxpdiOk5mm8m7klShh96Zwuiv17FIJO2hgrySU43owRMNAh031L40LK2E0RKGXhqoaVjfmjT8ng2rHVlV_ezOgPGNpj05Vgkfjhz2UDqsXyLHYZPQCalyhq3nGaxT9QkcnoLxt1OSDCkxNYCJZRLBXDsti3e0mpRbyONVe7QqgXpzbRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=FO24KDqyTRuo4mwvgwkEjKaYKxidnVnHsfuwwTnqVcWf3evMyWZjpSd-soepPXVoDT1mwBDv1DSxlebTOZOrzroLTyC1HdSCGQRsKyvV-IYb1wF0AF43aB8EGAR9yHubETryo8DmCq7YOFiRMzInfvag3sxlOixs9Z_tt_kxpdiOk5mm8m7klShh96Zwuiv17FIJO2hgrySU43owRMNAh031L40LK2E0RKGXhqoaVjfmjT8ng2rHVlV_ezOgPGNpj05Vgkfjhz2UDqsXyLHYZPQCalyhq3nGaxT9QkcnoLxt1OSDCkxNYCJZRLBXDsti3e0mpRbyONVe7QqgXpzbRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا قبول دارید که آن‌ها به خاطر جنگ در ایران، نرخ‌ها را بالا می‌برند تا قیمت‌ها را پایین بیاورند؟
ترامپ: نه، آن‌ها نرخ‌ها را بالا می‌برند تا عملکرد ترامپ تا حد ممکن بد به نظر برسد. مشکل آن‌ها این است که ما بهترین اقتصاد تاریخ را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71750" target="_blank">📅 07:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71749">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=n_8eddYd-Ul80bCZMHZcwrLN3afRPTY5DxqeBIYQsuruq7XUiwnVu-WJiLBqyo7rbCp_zJbrJ1WjL-uajKKVvYS6HlgoZT0k-BSQT5E7wKp2t7z5sHli8q9w2BSWNgw1QwNC7Kd8W-Xt7Kk4lRxN9N7XO787l5zGFwpSEW-U9K-2jbUA4c2UA0z9iBxtB_38E7psmK8ZIZH-tvdX1eWSHIJf5SpDU-RXLHNoDh1JKbBCWnnzRVFRVuNEJAJ6lWWak4eXjk2PaljCx43MDFB2eGHXXAZft6fOfNcRSYwDnkivsJqI7c-CCfLYRXV_WZ7d5Ii_4vPI02m7u_Vht2OM8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=n_8eddYd-Ul80bCZMHZcwrLN3afRPTY5DxqeBIYQsuruq7XUiwnVu-WJiLBqyo7rbCp_zJbrJ1WjL-uajKKVvYS6HlgoZT0k-BSQT5E7wKp2t7z5sHli8q9w2BSWNgw1QwNC7Kd8W-Xt7Kk4lRxN9N7XO787l5zGFwpSEW-U9K-2jbUA4c2UA0z9iBxtB_38E7psmK8ZIZH-tvdX1eWSHIJf5SpDU-RXLHNoDh1JKbBCWnnzRVFRVuNEJAJ6lWWak4eXjk2PaljCx43MDFB2eGHXXAZft6fOfNcRSYwDnkivsJqI7c-CCfLYRXV_WZ7d5Ii_4vPI02m7u_Vht2OM8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدواریم که به پایان ماجرای جنگ با ایران نزدیک شده باشیم. ایران خواهان دستیابی به توافق است.
خبرنگار: آیا مستقیماً از آن‌ها خبری دریافت کرده‌اید؟
ترامپ: بله.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71749" target="_blank">📅 07:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71748">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71748" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71747">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tLDHDxTBjLO8VTs4FrtkKkM-Hp1HVjIk8M6ZSN11bgHpl69fm8VBDybe_zTuMz040l3OELxBEeAMmfxTrswsJb9ZeskgZ_d_Sfq3r0jrDwv79VD1xLltlgWFqHRCOCNdZr8jgoyvM59GOtYCFo2NAUWKDKmqzUznk_SKJ3pjJeyIXmDzn4RhNPsGj5HQ6YFckzmbGmAOqVlRD-Mndppa8qqzGoODHi1_NY-dYntJycvntPWKNapjFgJ23L5QIyhaoy-kxKHn30crz_oKmOKmchZ0ftwqqCPrkRc5sKu7ME3Wl4CewSt2hx-Lo9seAVn9ViORH229gnAMqO0bPzOkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71747" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71746">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=eDf9KlJsFuhNPaWxf-F-UKywvQCHyy_D0g8rseCA091vMHhZOWO45P0krW_fFUGIrNH1LT90tV6eR3k0M5adyclXVVeYDkKPKqaeYOhGYvroLJDXHbYKYB1mvc-fJAK4O_WV26lw2Q_WEHO7rt38y_LBwJsC3UxbWjCqlAC6eok6uVLiwMYbU-scKxvRthNqMu39UEXEs8_EU7xjhxhldxPtZq3geqWcRKJfkZj8B8MB4yJTlBlbrkoyKow_ZCyulas4v8jgvwtbR5Nim-XFHqX785f8xPiYyVhUVlhERRgRiPQOQcnVS2WuOnmwY3ISt-SEs8VS1vgDkYy7YSoXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=eDf9KlJsFuhNPaWxf-F-UKywvQCHyy_D0g8rseCA091vMHhZOWO45P0krW_fFUGIrNH1LT90tV6eR3k0M5adyclXVVeYDkKPKqaeYOhGYvroLJDXHbYKYB1mvc-fJAK4O_WV26lw2Q_WEHO7rt38y_LBwJsC3UxbWjCqlAC6eok6uVLiwMYbU-scKxvRthNqMu39UEXEs8_EU7xjhxhldxPtZq3geqWcRKJfkZj8B8MB4yJTlBlbrkoyKow_ZCyulas4v8jgvwtbR5Nim-XFHqX785f8xPiYyVhUVlhERRgRiPQOQcnVS2WuOnmwY3ISt-SEs8VS1vgDkYy7YSoXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواضع حوثی‌ها و تجهیزات نظامی آنها بار دیگر در مناطق خط مقدم شمالی استان تعز و اطراف المخا هدف حملات قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71746" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71745">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=rigTkHFkbmeEhC_XxdF9NTGAshucOCP7f0C_gRUJC5pv2Bhbe_VHYhCPnKFqhpJ1mhmbaJ844NI6kbQ-EQls8KsSwayFtH83yzEoF7xoc-hUfG_MOqH4VB5b5tLqkF-qyrOkOfgMy6oqLKV0fsAi8R23spX8sUXMBhkuRH1VjN6KBAI80M-KLLxJJy8IMrQ4wODWWuMEhYX1QoDkv3oh6dxnxUYx2cwKZVoFjJilaGqM1duxg8BcU5tSf_hfE-v1eWW3DLLcgbKtHoRPZyKTlp4vGpjm-YDmvbYjK3nLCKTwuXrrPrdK6Bq9YxjNsbMXyPKrM0YEgcr7UV5qiO31uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=rigTkHFkbmeEhC_XxdF9NTGAshucOCP7f0C_gRUJC5pv2Bhbe_VHYhCPnKFqhpJ1mhmbaJ844NI6kbQ-EQls8KsSwayFtH83yzEoF7xoc-hUfG_MOqH4VB5b5tLqkF-qyrOkOfgMy6oqLKV0fsAi8R23spX8sUXMBhkuRH1VjN6KBAI80M-KLLxJJy8IMrQ4wODWWuMEhYX1QoDkv3oh6dxnxUYx2cwKZVoFjJilaGqM1duxg8BcU5tSf_hfE-v1eWW3DLLcgbKtHoRPZyKTlp4vGpjm-YDmvbYjK3nLCKTwuXrrPrdK6Bq9YxjNsbMXyPKrM0YEgcr7UV5qiO31uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر از همه شانسش یک‌جا  استفاده کرد...
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71745" target="_blank">📅 23:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71744">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=qwuwUWAy3XwEcI-cfD3c7Q0EfSy5bajZtmoh3huAUuCng9F3PHWIAvLRCUy2LlSpFfpp1CA46uFh3LDbco-RjEVSom_p4FZE-UfJ4ttq49vPEAgTBHtQIF-Pa7DaE0HbAwChjq3idZ24tc35SRtXAO3ybmOVU3uWKIz_866PuAaZ7PqLtY1KestnE9HF1fWqBLZa4scisdEL07R8aYvrnFt0RCLpjL9akVuqtYPbIKYlpBuJJrKjA82dpuIPtSDGtrvYdqs6jFIbZB8cMlMGFgRsdf4IfBfDQ8Ha7o9Z_MdVf_uWb1Yy5TmPd2uMPhjSt1vpGKzl6fW8RDe6jet9gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=qwuwUWAy3XwEcI-cfD3c7Q0EfSy5bajZtmoh3huAUuCng9F3PHWIAvLRCUy2LlSpFfpp1CA46uFh3LDbco-RjEVSom_p4FZE-UfJ4ttq49vPEAgTBHtQIF-Pa7DaE0HbAwChjq3idZ24tc35SRtXAO3ybmOVU3uWKIz_866PuAaZ7PqLtY1KestnE9HF1fWqBLZa4scisdEL07R8aYvrnFt0RCLpjL9akVuqtYPbIKYlpBuJJrKjA82dpuIPtSDGtrvYdqs6jFIbZB8cMlMGFgRsdf4IfBfDQ8Ha7o9Z_MdVf_uWb1Yy5TmPd2uMPhjSt1vpGKzl6fW8RDe6jet9gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نکته‌ای جالب درباره جنگنده سعودی که در مأرب یمن سرنگون شد:
شماره سریال (5529) روی دم هواپیما قابل مشاهده است که تأیید می‌کند این پرنده، مدل بسیار پیشرفته F-15SA ساخت آمریکا با ارزشی بیش از ۱۱۰ میلیون دلار است.
این هواپیما دو‌سرنشینه است؛ بدین معنا که شمار پرسنل اسیر یا کشته‌شده شامل دو خلبان می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71744" target="_blank">📅 23:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71743">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=jmrkJ7F-3FGiQi0bZ6p3KWOuAO1LzEm95BrCGtoxiXi0DvRFKFvHe0rKDLUUui509fTOs4J_Lq6Hib1X8AwuQO9tIO3pxjQ6UuK48_6l5fi8dxuBl48AFKGYaFhzzgez7PSQ1Ygqi6zRCLxr7TnvauNZ9S3qlDOizhObmGMvgvFUmSv9uke2jvB8bRjChMl_LfNqZguQeznil_tOiLfunMokOsK9nCv7yVa8NGn7-9khYMjTrRsbif7Q0OQrCkF81nnnPuCuQwGwVKNgxEBHLxPIB7c3Tan2mB__hWaVZBIHjHRfJjBVuPnQDqHur0Pogf_W4plGLbLFysJ89yzT6pqe2bAYRoeBviHY8MVMFT2Yy271pOXtaFF2XNvuGT0mjoBJSJmzOBIHu6RIYTozQITeFgYw-Ea7qh2LbDKjjHy5dDJcx4c_gJkUGtYtX2qmbaerLOlNflZRIHiyz4khs1KkrwgzDc_mK7VNpwQVqApV6sUB03kBWl9RQrQ-UgqYcIGIbff69G1I63yc_GJytpnRC4VLBJiHojYWYs_ppb7SP7ENVXQ4xw8NnXmi9Q6LYL7OFjwMbVNmNAhXtNj7wp9wT7v4mD8Z5SQXhcPX0qyRROk3vFAxbb7Il3UaZnA3-b74HBp7VNaXUAZlelbdbePJloOiiRbnB2_fDAGDUG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=jmrkJ7F-3FGiQi0bZ6p3KWOuAO1LzEm95BrCGtoxiXi0DvRFKFvHe0rKDLUUui509fTOs4J_Lq6Hib1X8AwuQO9tIO3pxjQ6UuK48_6l5fi8dxuBl48AFKGYaFhzzgez7PSQ1Ygqi6zRCLxr7TnvauNZ9S3qlDOizhObmGMvgvFUmSv9uke2jvB8bRjChMl_LfNqZguQeznil_tOiLfunMokOsK9nCv7yVa8NGn7-9khYMjTrRsbif7Q0OQrCkF81nnnPuCuQwGwVKNgxEBHLxPIB7c3Tan2mB__hWaVZBIHjHRfJjBVuPnQDqHur0Pogf_W4plGLbLFysJ89yzT6pqe2bAYRoeBviHY8MVMFT2Yy271pOXtaFF2XNvuGT0mjoBJSJmzOBIHu6RIYTozQITeFgYw-Ea7qh2LbDKjjHy5dDJcx4c_gJkUGtYtX2qmbaerLOlNflZRIHiyz4khs1KkrwgzDc_mK7VNpwQVqApV6sUB03kBWl9RQrQ-UgqYcIGIbff69G1I63yc_GJytpnRC4VLBJiHojYWYs_ppb7SP7ENVXQ4xw8NnXmi9Q6LYL7OFjwMbVNmNAhXtNj7wp9wT7v4mD8Z5SQXhcPX0qyRROk3vFAxbb7Il3UaZnA3-b74HBp7VNaXUAZlelbdbePJloOiiRbnB2_fDAGDUG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبرنگار فاکس‌نیوز از روی عرشه ناو هواپیمابر جورج واشنگتن؛
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71743" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71742">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مجری از خلبان آمریکایی میپرسه چی بهت کمک کرد با اون وضعیت از کوه بالابری؟
میگه هیچوقت اجازه نده کمبود انگیزه باعث بشه از تلویزیون جمهوری اسلامی سر دراری:))
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71742" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71741">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=oOztT2NgNtQfw_EBfih_eClIEj-eGq0Fi3gi2HRUDXq7HOWDFDElaj1aRqUie1BUgFM2WTjnZC6wCJfhx19QWpypxmZT1v8jDut9t2O_rwQEhZUMSZSKNK_HBgmEQsbqnt8RLWVjIAanEPHSV13UN-XqE5wW1xGdJwyxtiCj0XunCeO-jE57AAV6k7I8IQYBndg3a5hadMlare0EX_Hkh6KVt0AR4_oqqVYoQ3gjf95qJ86zDv9NH-sjROBZhVrgD08pewPR5F31mIXrHDCTnCGgTzVRBtq_rcTRqv8asTwCpL8xJR9QHO1FkuUTN9haNMN-_6q8bIS2QPXyTJRsvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=oOztT2NgNtQfw_EBfih_eClIEj-eGq0Fi3gi2HRUDXq7HOWDFDElaj1aRqUie1BUgFM2WTjnZC6wCJfhx19QWpypxmZT1v8jDut9t2O_rwQEhZUMSZSKNK_HBgmEQsbqnt8RLWVjIAanEPHSV13UN-XqE5wW1xGdJwyxtiCj0XunCeO-jE57AAV6k7I8IQYBndg3a5hadMlare0EX_Hkh6KVt0AR4_oqqVYoQ3gjf95qJ86zDv9NH-sjROBZhVrgD08pewPR5F31mIXrHDCTnCGgTzVRBtq_rcTRqv8asTwCpL8xJR9QHO1FkuUTN9haNMN-_6q8bIS2QPXyTJRsvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاله مرزبان بعد از دریافت جایزه بهترین بازیگر زن در جشنواره ونیز، جایزه‌ش رو به زنان ایران تقدیم کرد و گفت :
میدونیم که سخت ترین دوران زندگیمونو تجربه میکنیم ولی نباید ناامید بشیم
یه روز امیدوارم رویای مردممون برای آزادی و آینده بهتر به حقیقت برسه
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71741" target="_blank">📅 20:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71740">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQR19H3OrfdCGWkeNjOvIr8ykc019Fs1d58QmgCw7EsXPc5e5cTNbclwNwTUfm2q_KkWETbZ1Gn-3OxyUKnekf_w4RSQGTicnNPmV-e9rUMqoHyik0po1WBQNg5FoGzVfzlgbU-hs2FmkqBRAcniaaYpmMEsX2Iu2CTaceJ0yrezWQgYh-bkH8Fgf0hZhm-swQNYP_N56SaHu6N9Fw_REZ5EYDKNKQ85_Jp8v150xMAw9V7oM_6W4pdvSWbxNR-K5O-sJqBlyKa1lyh6Yshx5fv7gQd0XXfnMMDmvz5jkXNvUsbQC3yMKdUbCd9JLZ-XSILJm4JZ9B5DCVpb1krrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت گسترده ترابری نیروی هوایی آمریکا و جابه‌جایی مهمات میان پایگاه‌های این کشور در اروپا و خاورمیانه امروز!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71740" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71739">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزارت نیرو از پایان قطعی‌های برق خبر داد؛
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو:
خاموشی‌ها از هفته گذشته به پایان رسید، امسال ۱۴ درصد برق بیشتری به صنایع انرژی‌بر کشور اختصاص داده شد!
بیناموسا میگن دیگه خاموشی نداریم اما هرروز داره برق میره
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71739" target="_blank">📅 19:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71738">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4sAN1n-A1L8W0OsTzw8jf4HcNLp9XN9ZrXsYYhvndiyd9fbOFdZ_-ztafe6LTWtjJfDeDwtxGfqUov80h9TBd0LXdr1VWOAT0IUOyChEE-NqhL669ACe7aHnFkDaT0kZP2bjzQNajm9Vw4o8ZmfEoDi6sk-07e-JlEqxkICmrbAnOEQz2CNGne0Qq7cwyoPTJrW7GfFy9K4bOWSSQCx2s1uk3cvA0qEjGgDxujaVgmpktg-jKSpDr2voHuJT_9K2oH0GHC7EDt7rGVv-xCFZBPtH5qV_oRFaNgkWjgi4hg0hEHcVI0GAeZKm8zq8KbnvXJcu-nlIdQDea7fAFGlbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، به «نیویورک پست» گفت که مناقشه میان ایالات متحده و ایران ممکن است ظرف چند ماه آینده وارد «مرحله‌ای بسیار متفاوت» شود؛ او با ترامپ هم‌نظر بود که این جنگ می‌تواند «بلافاصله پس از» انتخابات میان‌دوره‌ای به پایان برسد.
ونس اظهار داشت که تردد در تنگه هرمز به «بیش از ۵۰ درصد» سطح عادی بازگشته است و استدلال کرد که ایالات متحده دیگر دست به عملیات‌های تهاجمی نمی‌زند، در حالی که ایران همچنان به حملات گاه‌به‌گاه علیه کشتی‌های تجاری ادامه می‌دهد.
ونس گفت: «این ماجرا در واقع دو مرحله دارد و مرحله اول به پایان رسیده است.» او هدف اولیه را نابودی برنامه هسته‌ای، توان نظامی متعارف و قدرت اعمال نفوذ (توانِ قدرت‌نمایی) ایران توصیف کرد.
وی افزود که مرحله دوم، جلوگیری از بازسازی آن توانمندی‌ها توسط ایران و در عین حال حفظ ثبات جهانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71738" target="_blank">📅 19:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71735">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cs43-wp_4XXHxN9SV8aRW3o5gL8xooUccM5JwdO66yQ2BhqS2YN53puV1OOIDyQUvnaJzU1UYMxx1JI45IzpJu8NzRSZVqkQGjT_t_fc13KIMT4tOkOnTrqwogwOYHd1eYkc8UzQO0dm4vMLzfF3up6rPjaIQ9pnuJ7s34GWpvRSLNm6OjYmMjgEjv5JzfHw03ttLdsXw4wvB-qjyqNp16DvCfrGxpUEeRiJM6E0RcsuHkE8d-QcuUi8cUX3uR4KfOBYLqCrOPGJF-be21G9DTsukxQC8-2ES_sKwlkBUqNJEWdscwvywBaTwdsXCvOZ2bKmipH9DAUsZsDwEF6Pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gw7QhzgssRIMgEnZQjq9zIVyAMNTjQLAOswV8qjoK3nS-HA81wqvgNGuEliMLH28B8qor_1JBHa-K5AgGRHNHN_jAWyvkxw8BzG_Fo29skpUciOZTUKV23jCjoFn-p8SvPVdsE9P05mo2k0eijC2_tO8S1y2eVIEZ6ii5KyU2VM7MkF8uy-biQawntd25QQkjiba7osQuCaluzJkjqwhCT3Vrkxdcjo3v5ZqGRaJcSa73u3rN2hSpMSHKBqpYy3arWZR4-S3XcPGMSRLV9aOhj67F7RRgt5qUjG-J-STDkXbBvfM6fvG8NzYnQnX_gZ5wrdGkpNIL7J468xLa-_YRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حوثی‌های یمن تصاویری منتشر کردند که مدعی‌اند سرنگونی و لاشه یک جنگنده اف-۱۵ عربستان سعودی در استان مأرب را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71735" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71734">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=KdvZ23RXdbDP6PWAEy6ATzl0XXaE1SBBjsbxQrbogviFljTrOwMZc_5aqZBW86QLBGTcc_f-Ing4Ei4S28Jtra-1HpGUdkC077Yfp3KwEmvV_k8TOXED0SKCZgdFMM1kVG5iAdNlV5w-4t7iut-Wjg_VBqjZQzWOncrUo2KOepq9-gmxCWkyC_cnIiOFkLzQKENrusNcnm1qUaF5IGPCFbXi9AOYoJ7QsjJQQivZh-g-4q6wv9D4yGBiBER9zEZpuZsA3lqRQZUE30IkNjdeGrBoGfXl56MZmeO6v2wzM5be13ngw-M4bJEPlAe5sYv0rJ-YjQdgKn9b25FfDM0VjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=KdvZ23RXdbDP6PWAEy6ATzl0XXaE1SBBjsbxQrbogviFljTrOwMZc_5aqZBW86QLBGTcc_f-Ing4Ei4S28Jtra-1HpGUdkC077Yfp3KwEmvV_k8TOXED0SKCZgdFMM1kVG5iAdNlV5w-4t7iut-Wjg_VBqjZQzWOncrUo2KOepq9-gmxCWkyC_cnIiOFkLzQKENrusNcnm1qUaF5IGPCFbXi9AOYoJ7QsjJQQivZh-g-4q6wv9D4yGBiBER9zEZpuZsA3lqRQZUE30IkNjdeGrBoGfXl56MZmeO6v2wzM5be13ngw-M4bJEPlAe5sYv0rJ-YjQdgKn9b25FfDM0VjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تهران یه کافه مذهبی به اسم ام‌البنین افتتاح شده و مخصوص آدمای مذهبیه و ورود افراد غیرمذهبی به اونجا ممنوعه.
شنبه هر هفته هم سفره‌ ام‌البنین دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71734" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71733">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71733" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71733" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71732">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OReiC0DkBGWY7BcJc-JxBlZB7MBjQLEBbU_M5evPji2MdhAKE2WNShO9XR3pkSTURJ1aiOZPO56j2Kcok0Ha_LCyl_fV-V2ZVxkm45fr3jWwo9sQnOFUoG7IiACr31D894iDjncKBUTRvSKqLpoOevwCvmURNRhNGYxMFqo4MEInpEWRX53uQDfXSjQ6HS-7UlUaix5GWldB8J0-s7ieogoVEQWXGPD2QGcofZQzMHhZGImdjcGzlSJ79ZUCgQ8vVDIEeMHXzhOQX7iPz91osSckLbu4MFXlOb_YScvCpv6Sjo4kvn-atHdUNNIAK-GW3XQfSSjKQSS6fadjYCFWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71732" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71731">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534f93c783.mp4?token=EeUZG0_zVJIMS5tc0ZmeVJiKq6VAX7xkKSCNhzrFXq-xnUJlV6KKWC4SrazOF0Iw2z4LhoW1AD8mmBJ8agNsx73_KyzywHco8SJtii9D22lVHHIVNMDCvvrfZGyqhgBJnRzZ_aqVs6LRxJzjMeXCLLEi71xJW2OML6TuFpmU3pTyq5hSenHugISNdHj5NX-6K137Bs2xM1vk77Y_t_llkNfv14olBmrnS5SrJNfQJxzcrHamXW7d4iEtiulqYiZ90g5YfzCUmQaqQ32qZEtBWZ36jGfDysfd1fee6D3ZHRFVDk_Z9_t06-dcYCdqFwnoHv4EWN3kp7mn_KyD3Ood4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534f93c783.mp4?token=EeUZG0_zVJIMS5tc0ZmeVJiKq6VAX7xkKSCNhzrFXq-xnUJlV6KKWC4SrazOF0Iw2z4LhoW1AD8mmBJ8agNsx73_KyzywHco8SJtii9D22lVHHIVNMDCvvrfZGyqhgBJnRzZ_aqVs6LRxJzjMeXCLLEi71xJW2OML6TuFpmU3pTyq5hSenHugISNdHj5NX-6K137Bs2xM1vk77Y_t_llkNfv14olBmrnS5SrJNfQJxzcrHamXW7d4iEtiulqYiZ90g5YfzCUmQaqQ32qZEtBWZ36jGfDysfd1fee6D3ZHRFVDk_Z9_t06-dcYCdqFwnoHv4EWN3kp7mn_KyD3Ood4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این کلیپ تاریخی که چند نفر میخواستن با برنو، سوخت رسان و جنگنده بزنن
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71731" target="_blank">📅 17:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71730">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فاکس‌نیوز:
یک کشتی طرف قرارداد ایالات متحده در نزدیکی تنگه هرمز هدف حمله‌ای از سوی ایران قرار گرفت که در آن از چهار پهپاد و دست‌کم یک موشک استفاده شده بود.
این حمله منجر به جراحات جزئی، از جمله عوارض ناشی از استنشاق دود، شد.
تعدادی از کارکنان آمریکایی در این کشتی حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71730" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71729">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKxi1krkCaU-xH80QwOGnJL4qsS-6ojmGzwFUJGDPwZta_uvcwo2utqoIqNuYlFynGvYOwxebExRn6WCjFvDJ-T8brojGWwhGTMo8fmo3DiHyXEVvZH4rWKYQkWSjlotcEybZeO8_kuDErPb31jS086oab9acNuMzal3EC7CMUSoSpQtRw-SzVMMDyEygeRp_KwXFPe2RxYFVQji-p0vKMNzCSb71GSiKhaoRZQzjB7nbpg_Ale27M3yuxMEjAmxZSIgHhRW6WeEr5i8YOfLW5c00omY72tkAfkktzkcpygEaCFxhnQy8m8iYwTwd3TQCS2hStQpDs2hx6YIhR5NbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در تجمعات شبانه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71729" target="_blank">📅 17:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71728">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2421361f81.mp4?token=k3bGCgrfKBNUanqCk1C6S9Rouc7gIXXM2XgVPIzh9KeL4CJn68sBiHl48eGRQuDIyq9KhI3Wir8PWOFEfi95AJ6QHbossEoscy-s2SAn6-O-NrqUURzDCFeZ2ShGkRb7f9kqg8UjW99dyjxYrHUPagWLzDtZEA4uY7CbuNn3AAZD0kj0QynqQNkV2CBjHPFrx_mS3aZT-Dz02LzAAL2Zv6GbxcOKUDfdiSF2K2eLmxvcWD6HdQFRuJy5zqP0Gpcv5NJT3dTLlxnVrlzSoHMp_QyuKBS-uE5soX541Zk8GdNXrnkVnFtp5AVDn1bhVeoTUSnCX8OUQoiWJOVGHTmop5jR2V8TUo0sWzqbbPlC2ParWrDvFTffXeUh4wwVlqek-ruQgmqM6FJ8ht0s76dW6LM3174wtggZnrzRKEzybty9HxrA22ksKZrwlyMMDKjxGaBcDXWYwa3xaKR4Fw1BOWHLwwy35S06pPeSoGUX3UXC1scFEsVDjJ7WuDseJVmX3AE0xNiCauPWblQwpNfHTQjjoHGV8BDCXHII2YWS6XEiVyPiByc_95wOXapfNFiyS0tYZe4MAJKKc37FA9jm5WqBV7lWWjvFymhe11-K9LYe87G_UZgbm7zWrV1SdWs6ruW6GsCjhzGVGbNdSrvDboRYD0CfEklipML1s-tZ__E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2421361f81.mp4?token=k3bGCgrfKBNUanqCk1C6S9Rouc7gIXXM2XgVPIzh9KeL4CJn68sBiHl48eGRQuDIyq9KhI3Wir8PWOFEfi95AJ6QHbossEoscy-s2SAn6-O-NrqUURzDCFeZ2ShGkRb7f9kqg8UjW99dyjxYrHUPagWLzDtZEA4uY7CbuNn3AAZD0kj0QynqQNkV2CBjHPFrx_mS3aZT-Dz02LzAAL2Zv6GbxcOKUDfdiSF2K2eLmxvcWD6HdQFRuJy5zqP0Gpcv5NJT3dTLlxnVrlzSoHMp_QyuKBS-uE5soX541Zk8GdNXrnkVnFtp5AVDn1bhVeoTUSnCX8OUQoiWJOVGHTmop5jR2V8TUo0sWzqbbPlC2ParWrDvFTffXeUh4wwVlqek-ruQgmqM6FJ8ht0s76dW6LM3174wtggZnrzRKEzybty9HxrA22ksKZrwlyMMDKjxGaBcDXWYwa3xaKR4Fw1BOWHLwwy35S06pPeSoGUX3UXC1scFEsVDjJ7WuDseJVmX3AE0xNiCauPWblQwpNfHTQjjoHGV8BDCXHII2YWS6XEiVyPiByc_95wOXapfNFiyS0tYZe4MAJKKc37FA9jm5WqBV7lWWjvFymhe11-K9LYe87G_UZgbm7zWrV1SdWs6ruW6GsCjhzGVGbNdSrvDboRYD0CfEklipML1s-tZ__E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیویس کیس سخنگوی سابق نخست‌وزیر اسرائیل:
دیکتاتورهای ایران ظرف چند هفته سقوط خواهند کرد؛
دو هفته، سه روز، شش ساعت و چهارده دقیقه دقیقاً
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71728" target="_blank">📅 16:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71727">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=e1NODVy3H2mbdbCeOR3Z2ASoOFGtYqU7--zjUoagihxlBfyUr1_WxxvCvY_IKQQM0W5iip2n0KJaEE5TlysIsPTqpXpbxothZJRmvRIUJkSw_zSWxf9vUo4dKsXNGxflR6OKHlFp4wUsNIlvrz3TtT_tkJM9jSV6mOFbN5O8EDEvYcAFD8iMgURuIMoQvSZjH5TjiWnBV2Mh8DzOfIu6jnG5lTIwd_bbpEv1sv6xlqCPvzbFXJrza7G6lWen8Zwx-TvKnM4iNUS_5xh8X4apQfjy2kIB0UrDhLzWARdm8TA3_ShC-C8Un46MyHAziQIhzIJ1kaIMR7YlebkWVSsGaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=e1NODVy3H2mbdbCeOR3Z2ASoOFGtYqU7--zjUoagihxlBfyUr1_WxxvCvY_IKQQM0W5iip2n0KJaEE5TlysIsPTqpXpbxothZJRmvRIUJkSw_zSWxf9vUo4dKsXNGxflR6OKHlFp4wUsNIlvrz3TtT_tkJM9jSV6mOFbN5O8EDEvYcAFD8iMgURuIMoQvSZjH5TjiWnBV2Mh8DzOfIu6jnG5lTIwd_bbpEv1sv6xlqCPvzbFXJrza7G6lWen8Zwx-TvKnM4iNUS_5xh8X4apQfjy2kIB0UrDhLzWARdm8TA3_ShC-C8Un46MyHAziQIhzIJ1kaIMR7YlebkWVSsGaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ دعوای این دو تا بچه گربه خیلی وایرال شده، از بس کوچولو ان، دستاشون به همدیگه نمیرسه و رو هوا همدیگرو کتک میزنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71727" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71726">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=Z8aQu-9Eyqbtw7Xe_wmUGPI37WhY3jgXPlP3ssQkaqnJ0zUa7sKa_mH_R4Y2mmClQlGNyOz66vaMeEff6r0mn_B5ggtLgJNcQ0Hx5nyKIvLVbEjj8FTaZBuMP5h-pDWQ7vbiJfxB85muHXpsBCqwyvMBpnApr83XPFNKz1DXujvakt7lMnKkEQ85IHsjeTJS7f_F3QaBqdXofLNWtC7VG_4ne98iOSjr6a990ZrX-XY5Hl7X5UMq9DQCg9zlZXz45XZUH58K7xQhoWF2Ewn5TKIxCRYYanPrnV_NP-hQSNNvs3RhvM8o01c1Gu__j4DRF5rCuA80r4aIDml0WdCMbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=Z8aQu-9Eyqbtw7Xe_wmUGPI37WhY3jgXPlP3ssQkaqnJ0zUa7sKa_mH_R4Y2mmClQlGNyOz66vaMeEff6r0mn_B5ggtLgJNcQ0Hx5nyKIvLVbEjj8FTaZBuMP5h-pDWQ7vbiJfxB85muHXpsBCqwyvMBpnApr83XPFNKz1DXujvakt7lMnKkEQ85IHsjeTJS7f_F3QaBqdXofLNWtC7VG_4ne98iOSjr6a990ZrX-XY5Hl7X5UMq9DQCg9zlZXz45XZUH58K7xQhoWF2Ewn5TKIxCRYYanPrnV_NP-hQSNNvs3RhvM8o01c1Gu__j4DRF5rCuA80r4aIDml0WdCMbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه رستوران تو آمریکا باز شده که تم بیمارستانی داره و تمام‌ کارکنانش کاستوم دکتری و پرستاری پوشیدن و اگه غذاتونو کامل نخورید باید براشون قمبل کنید تا خانوم دکتر بیاد شلاقتون بزنه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71726" target="_blank">📅 15:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71725">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=UsUGxHMA9-XEFyQRrxucIOsMtzlN77SSJoIal6bO0AOfIvf1KuWe_G5arwWoQcwrRAvTWqofvUVlWL9CTUtD238o_Vu7znoY3G0YIqzvmwKkPVXX-yZbAjhWoECQBzEfVe6C-Mty89ORU0Fc5a5cuUIvys3CyV0IAML-WTLSal9-RF18HCUp-q1H5wumF6UHwriZJMRTfE2_RaoRy863amhyUdEMmPXU2Jfft5dMGa2L6cmsJIw0J1MoNBBZIhrPVE_KYCgyq7GJBRMLSg_HrVr-v1NQfOukyo6hZeiCTIIssOybmd-Ui98Di6OOrxnRYk406Ka_qTzVaAOSWLcdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=UsUGxHMA9-XEFyQRrxucIOsMtzlN77SSJoIal6bO0AOfIvf1KuWe_G5arwWoQcwrRAvTWqofvUVlWL9CTUtD238o_Vu7znoY3G0YIqzvmwKkPVXX-yZbAjhWoECQBzEfVe6C-Mty89ORU0Fc5a5cuUIvys3CyV0IAML-WTLSal9-RF18HCUp-q1H5wumF6UHwriZJMRTfE2_RaoRy863amhyUdEMmPXU2Jfft5dMGa2L6cmsJIw0J1MoNBBZIhrPVE_KYCgyq7GJBRMLSg_HrVr-v1NQfOukyo6hZeiCTIIssOybmd-Ui98Di6OOrxnRYk406Ka_qTzVaAOSWLcdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله افراد لباس شخصی و آتش به اختیار به یک رستوران در رشت به نام « سحرخیزان » و تخریب رستوران به بهانه حجاب⁩⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71725" target="_blank">📅 15:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71724">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGlLTyB-oyM91rY4DWrJ6JVyN6hvooNw1HimoWDsL2EN1NL792dV_fjAoGiiIvzHVhYcHxsz_mcmjx5LVhWDaO5spiOU4XpixA1EfCI2hwvow2nXSluz2-mAyHPhfJ0vvKuc_QSc-DXxhN0dNmAVMWnxotUBIKDqgpdo3V17Em-x-HI59OsubRKLN3-RkWI1NOJ1G_hkLCvNiB8w5zMRVbWCHoDCdAQkf3RUKQDzb7PcXuWua9LQ6-ewpw8yilOMe4NNPsjbEER_Tx7hyZ8ITUgHps-21tVYlf2hEpQVb3cWoQL83VlzqiNPiHezYmawjiWSjGXQ2Co76mYec5tV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛  سامانه‌پاتریوت شیطان‌بزرگ مانع شد خانه‌خدا توسط حوثی‌ها نابود شود!  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71724" target="_blank">📅 14:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71723">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=OWvp3ZfO6WjtuquZxoIHubMCCtqjORlXDPPZS20ediFEs4Fk1OG-PW64UKswT-snMJPRwmvATVOwroyW2bQUykAwFdqpmWzezdnlOBCfwsW7QPml1i0fmb2JFwrqpaOCv0HCbcojNp-c56qyBgfwV8RrPFhyZtMC0hT-teNXPZf4hS3JgGja_Vx1u0BU-PvETWbO18kYpMdnlc2OM0wJFHqa8BznhqPLAqelmdrw8sjeVdkDVx5wEYcHIt22iCV3WIyLfxN8ClHPATOGOa6IedwG86CY7RVWIKOCt15ewTJTrUlskywGF47Jq8Q9oa7IEKa1p07Vflmp8_y0RhV05w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=OWvp3ZfO6WjtuquZxoIHubMCCtqjORlXDPPZS20ediFEs4Fk1OG-PW64UKswT-snMJPRwmvATVOwroyW2bQUykAwFdqpmWzezdnlOBCfwsW7QPml1i0fmb2JFwrqpaOCv0HCbcojNp-c56qyBgfwV8RrPFhyZtMC0hT-teNXPZf4hS3JgGja_Vx1u0BU-PvETWbO18kYpMdnlc2OM0wJFHqa8BznhqPLAqelmdrw8sjeVdkDVx5wEYcHIt22iCV3WIyLfxN8ClHPATOGOa6IedwG86CY7RVWIKOCt15ewTJTrUlskywGF47Jq8Q9oa7IEKa1p07Vflmp8_y0RhV05w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛
سامانه‌پاتریوت شیطان‌بزرگ مانع شد
خانه‌خدا توسط حوثی‌ها نابود شود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71723" target="_blank">📅 14:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71719">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IT9vWi4g2xm8mYXiyl-WsCEQUarNE_TjgWQfbcx1lLSMsp3Laj2lAFiNi3QVn5faPOYE74aF-hu9KfNa9xLGEhj3LOudbiUiIuFxkMXVeJLzwaj-zZbeBOZBipGCR535Pu2xnYlM-0UT4e54hEYnLMmI6V0mZtn1C3XUrWMBNsY360L4WxSRGx5AOFlDOB8wyN9bjo7zEwhEkvvQW3B0ET7Rf31YBv0v1waMd48pNPJmG3vaWhDTHlHfwhB4_xDP4XV9THnqjVE7-912zVEdulLG3btwfdCX7DvlgsQDIUv60dmiKmBy6PcZitfCDeBujmXaA0V0kqrPtuKR_skHPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kucINLBcTmqPnMr3Dhpt_yQYjbU8SMoxzIoChBU5kfPF78XLPqZtbOGwT54xOW99fxIR1Bmr5M-di4PxeeWyoYw7j79-vZWAJTICe_-L6MBMHhVmmG75pjH4hIiLlMyaJd_qgDhZ1-vLphynVKCce01TQN2ha--zLv5KQ8JXCX0XcJ18GEYpiPHaVTxNfQc7xPsXKex9SU9Df74LQoRjwplcGj1-CzimnI16STRZlvyNVle6vnFf7SU5mXIbos5A_BCumKIG-qWw8lER0IKeuFXyDRMRvai8kvOm59b8NtOgdpJvP90acdKpLy9aXnZekb7XWk0t_yi-MPvGoDmCRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FGakBCWLncHeFUdd5YTF8O69QgoOQGe7kkYxOS7hPbXlaPtUEGmg6h9PNYxVCHZL5zzuGmUcX-j53XpccekkUxpT03pe3zVQrPwzThd0Taj4Chz74uRwzfayxWpM9gWDWTM-FGlyFHKe-PjXy-RzIxRnOT7hinLvGssiN-hHMjViXMKZrihV-5g_VeQU7_I4B8VIo9PjilZxqBoZ8zz0o-bM2uQYsCZVnQ7PKyulQzcfdf1moS2vbdmkwGeof2OA4hx0LZimYF1-K6-pKuF5UlF5W47zrRaWZZDDsYeBWgTTYAKz3Ql33mARHywi_bJfeTZ5p3DIF7EA14au-wBCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxbVPCG1NId5hchOUDFLReI7KJ0YaBGYyOtTeeRMIwbgS98mKQ8tdfQz9CmLIRY2fj4n_6ke8gBBBBg0FP1618g3-cmQyxdIdFoq9rnEFPSXHmKNHnNpMb8lKeayq30vJXnngM4sZP5y98Mvg6EpNLe_N6yOKImMvQR22BhucF0__gZzxiFvCVlqayyqtd6dr5F6KiwMorYW5XTrUcjrsSTwOIg3VwK4NxUq7FXPlQKcIGSY-mq0ij1Z_6R-sAJMdSB6vFrwgEhzivNUoXpkEPwC-FAHceR4SbQQOkMyT1eyMmD3JQxNprbJkwBwXM_jAF_qnnLKjxy6GmNasXSNYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های اختصاصی که توسط سی‌بی‌اس نیوز به دست آمده، خسارات گسترده‌ای را در چندین موضع نظامی ایالات متحده در خاورمیانه پس از حملات موشکی و پهپادی ایران نشان می‌دهد.
این تصاویر که توسط اعضای فعال ارتش که ناشناس هستند، ارائه شده است، ساختمان‌ها، وسایل نقلیه و تجهیزات تخریب‌شده را در پایگاه‌هایی در عربستان سعودی و کویت نشان می‌دهد.
در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای بوئینگ E-3 Sentry مورد اصابت قرار گرفت و قسمت دم آن جدا شد.
در کمپ بورینگ و کمپ عریفجان در کویت، عکس‌ها نشان دهنده پادگان‌ها، تریلرها و وسایل نقلیه آسیب‌دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71719" target="_blank">📅 14:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71718">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSvOe9BUJvur_B7Wdufl9imQIxerrTtlSlCy0pwOYczr1CJIsa34hWMif0tL-ZSCdvSE7ObbLQF6UjaSiIwS_cf7hWuE7c_liiCabGMzOezBSdXmZw-2BvsVc16X1CeyKO_eKRFGnNq_5QZmYGpVZETvZcnr9fEL9-UtLOxA6yclkzPKR6yZOrR4eaRtg3eTQ6bmr3Qdb2QEcuHiMfa5CUrT2hLzCb4zEeH_792whjQFLvUg3dMz3wnwJEegq-d5-r9q81INXTEsdXxNyCaPxZyep9IJry8YVT53c3Rmxevvcl6AzO10L5MI8ar6NgZDsJrxvbmcRa13r4ujXa0m2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشته است
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71718" target="_blank">📅 13:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71714">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a175287c.mp4?token=CDte3JUZ9fCe9cWKs7r2nrwZstEASZIlyxLdfNgb0JxnjO2O_r6_vqonZKISDPHZm3btmSfdP1uPQ-z3RiogQM8TOGZ2e28Ofk7YjZ2D7DnG9GxxhRf6QFdSed8myjfqULV9HWllwmDvv90EOp_p5EOGch2ET27pf-UHg529XZakvtR3HHDGUZqPea8lG9P2tnfTlrv1v8IRhBgfhSxGOaEp2NOULj9OiV7ypwmEISKC1EOQ5I82vhi0oFMycwjDuKY71JG90AGT8xsDXuHzNnueL-yc4DWzVfmOoxoSUK52YYkIamraD5sgMZ9KhsGTIJXVxQJw2uwq7qjxo9LnTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a175287c.mp4?token=CDte3JUZ9fCe9cWKs7r2nrwZstEASZIlyxLdfNgb0JxnjO2O_r6_vqonZKISDPHZm3btmSfdP1uPQ-z3RiogQM8TOGZ2e28Ofk7YjZ2D7DnG9GxxhRf6QFdSed8myjfqULV9HWllwmDvv90EOp_p5EOGch2ET27pf-UHg529XZakvtR3HHDGUZqPea8lG9P2tnfTlrv1v8IRhBgfhSxGOaEp2NOULj9OiV7ypwmEISKC1EOQ5I82vhi0oFMycwjDuKY71JG90AGT8xsDXuHzNnueL-yc4DWzVfmOoxoSUK52YYkIamraD5sgMZ9KhsGTIJXVxQJw2uwq7qjxo9LnTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
:ویدیو هایی از اعتصاب عمومی در سنندج،سقز،دیواندره و دیگر شهرهای استان کردستان به مناسبت چهارمین سالگرد قتل مهسا(ژینا)امینی به دست حکومت آغاز شده است.
همچنین ویدیو هایی از شهرستان پیرانشهر در استان آذربایجان غربی رسیده که نشان می‌دهد بازاریان دست به اعتصاب زده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71714" target="_blank">📅 12:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71713">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه پسر ۱۴ ساله با یه دختر ۱۳ ساله وارد رابطه شده و ا‌ومده پیش دکتر میگه من پرده اینو زدم و گشاد شده؛
حالا اومد پیش دکتر ازمایش بده ببینه این دختره قبلا رابطه جنسی داشته یا نه.
سن رابطه جنسی تو ایران داره به ۱۲ سال میرسه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71713" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71712">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71712" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71711">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHrEauWIluik_p0HbiIX-gllUskJ6JIyrxHtxrScOxjhtDcAphpqGGobb4uScQT4vRyNLj4QNMJpi2bu-Nmj_zzPjheUOGiRopp8uaHaFmCcnVOTZbj0Rv7nlIS3hqN7t-LWvQcRQTZtoYYKniX33pnsAihEgtEZbPbbRyUERpPJ50L0BkkPfMDHkkeWt757c2Tc8EgEIZNoCi5at9gXuIQPmrxGEsgAn58sh4YP9dMHekx-aqehiJTfItONFE_k8LIbMR11PEYlzeldtlFquUWWXNUld9uK__zBbFHeMcHpE9qkc0KfilE-vZ5WPxgqWWt1pcK3g8SOgW4cMq0pZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71711" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71710">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw4wI509yKyPYm01WfT5DskBjOTaGs7ABKUQL59G7JAkI0-Np9EO15HilW4jDre8vtaZ4-MlZL1dzbfG3prcpTg1lp7abIJd8BJEat1Zi3A4EaIaOKPhNIPt_HUetBzd3I4v80DOyHuqu8W3bvZxF2Y1Qbdv8FgL-dHDBrltZS9Kj9QeL3T-tYFoZ9tgMn1Ir4N2Xdg2gV-DL-1riqtuLM6UHBaqt7GbldmZN1Kr-8Th9VQFZeWwnrkt8UrEbuVyadR7Db9aWLWiZ1cQsJAlRZeMx7n1tRTBnWveVzMtmy5LpDzGN09_0dRb9JLTtIJsn2Nht_wksUidc8GTXOcgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده برای اولین بار تأیید کرد که سلاح‌هایی در مدار دارد.
مینک، وزیر نیروی هوایی:
ایالات متحده اکنون سلاح‌های کنترل فضایی در مدار دارد که قادر به دفاع از نیروی مشترک در برابر اقدامات خصمانه دشمن هستند.
از بیان نوع، تعداد یا زمان پرتاب آنها خودداری کرد.
نیروی فضایی می‌گوید که می‌توان از آنها برای "اختلال، تخریب و حتی تخریب" به صورت تهاجمی یا دفاعی استفاده کرد.
کارشناسان فکر می‌کنند که به احتمال زیاد، پارازیت‌اندازهای فضایی یا جنگ الکترونیکی - سلاح‌های جنبشی - مشکلات مربوط به زباله‌های فضایی را ایجاد می‌کنند.
این به دهه‌ها ابهام رسمی پایان می‌دهد.
اولین نقاشی نیروی فضایی به معنای واقعی کلمه یک هواپیمای فضایی را در حال نابودی یک ماهواره متخاصم نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71710" target="_blank">📅 11:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26353c8137.mp4?token=BfwaHIA2YKwb0Z8pt1jG17cfwtzkz5aE55Pfdasn-Z5W2h6EMe4LFuTIuAaV4ZOuVMYaooOvw1ADVHPX6HR6HPgd5mz98hI3CSAMI_1o7cxW2JcsFaeYALxE-QAwBlmlPgnrPlqsoGWk1BV1myIvIUIu9RglwriU1vDPJVQV66l4DB-Zvy4ZiLj55Zc5Yl8t-2nnSVsOFBwD7fX5VBGXGTrqU1vYkaUP7EDrAgHsNCiJDdkynX2fzDpsoAkjxT_tDoBIlbnUo94m1hBF6opZdscbfs-0pILjdiDYUg3lMd5MNHvNLBMx4atGFtj1SoEni3WmyRwkGK95DB33DaAgZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26353c8137.mp4?token=BfwaHIA2YKwb0Z8pt1jG17cfwtzkz5aE55Pfdasn-Z5W2h6EMe4LFuTIuAaV4ZOuVMYaooOvw1ADVHPX6HR6HPgd5mz98hI3CSAMI_1o7cxW2JcsFaeYALxE-QAwBlmlPgnrPlqsoGWk1BV1myIvIUIu9RglwriU1vDPJVQV66l4DB-Zvy4ZiLj55Zc5Yl8t-2nnSVsOFBwD7fX5VBGXGTrqU1vYkaUP7EDrAgHsNCiJDdkynX2fzDpsoAkjxT_tDoBIlbnUo94m1hBF6opZdscbfs-0pILjdiDYUg3lMd5MNHvNLBMx4atGFtj1SoEni3WmyRwkGK95DB33DaAgZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک دانش‌آموز دختر برزیلی بعد از اینکه نمره‌ی خوبی تو امتحانش نگرفت با چاقو به معلمش حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71709" target="_blank">📅 10:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=UZkURgiinM8xA7bYubc2NbsrDJ-ECtfcAnv036IDtK-63FZ1XNdDAiknjTie-JN1IQNBLeGKtDPaqFGEXNDgrulM2tuu2TViudTWPfc2MdcadnGldFDMSNh6Ozpm9du8aZ328g4jirCuL8lymGDJW0go7AhAw8qreOS6aZ9tf8s36Fy2MrI9-BfvZzj_xcH-vBK2dST-2C8nGBt0CrfNDtg3GujLEsH_oFRdAGDvRsN9E8a9ngtr7P_NXF_DJldTWyGIi974TAcTh0-9RW58YYdGljfw2IVEiLyKuxnAQnUbIt2FZCFutCGdxBZLeq3JCvIluhJkW0_jL11bTAc1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=UZkURgiinM8xA7bYubc2NbsrDJ-ECtfcAnv036IDtK-63FZ1XNdDAiknjTie-JN1IQNBLeGKtDPaqFGEXNDgrulM2tuu2TViudTWPfc2MdcadnGldFDMSNh6Ozpm9du8aZ328g4jirCuL8lymGDJW0go7AhAw8qreOS6aZ9tf8s36Fy2MrI9-BfvZzj_xcH-vBK2dST-2C8nGBt0CrfNDtg3GujLEsH_oFRdAGDvRsN9E8a9ngtr7P_NXF_DJldTWyGIi974TAcTh0-9RW58YYdGljfw2IVEiLyKuxnAQnUbIt2FZCFutCGdxBZLeq3JCvIluhJkW0_jL11bTAc1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته خانم دکتر(روانشناس بالینی)؛
خودارضایی نه تنها ضرری نداره بلکه خودارضایی یه چیز سالم و بی‌ضرره که به عملکرد ذهن و مغز کمک میکنه، باعث کاهش استرس میشه و حتی به رابطه شما کمک میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71708" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71704">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyyRJyyBdqSDD1-QL5rSJQOiweDxwoWuayjdjxKOF08hRUfwX6mn-6UNf4wuCU8WKa-Ldn9vYSIF9epuHiGr_8AA6fBwYA2tCm_V-WlNGh9H2bBpYY-81aN-cQ7Uuls3oi18YNhEXwUaYlOhhJ6X-_gmmH14dUhJvzpJa5UntrCgTp9GMVYMWcFHV8WAOifB-vOMJXJSSQhvbch5rRnyM221uoCoFkR_Hy1_HCQnkh0F4lldncqgXdh9JX9ZD0qsBRJt-m7h4XNvHTP6IGe0Hp54z8HEfLeP79Yf5Hq5k7rltrSoeAgLEyiJOwb739PoXi8rRi8j8W-YQvr6P8ecwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=l3w3qktIeMG4PRsUcIt_wgN6GtL5VhLwYl7CEtsWEISYewtGfWkLPYAyrU1TKK8aSuy2ouFJwUnQDSI27x0YwQdfeDSrvumRJKwyno5S_n23Uj66AabjtdJaHZmG3HVeh73eIs79CkrOYj6gakdj2TonpipY-2Q2lGbd-jFhfwNfpat7D_STfRT8b0Qopt_hJBze5f7UTDLLvyEyYTrifEEh824NZDU-BobudTm9apjinZQkGosCA5nxS3QbqkZ2CzVAOzzNHMYr2RK5NwcClWNzungyQ6zLM0VRCWO-ELt6rePlTYu50vFSpc7a8OXf5TOAOKEe4abSa-dVv_cYQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=l3w3qktIeMG4PRsUcIt_wgN6GtL5VhLwYl7CEtsWEISYewtGfWkLPYAyrU1TKK8aSuy2ouFJwUnQDSI27x0YwQdfeDSrvumRJKwyno5S_n23Uj66AabjtdJaHZmG3HVeh73eIs79CkrOYj6gakdj2TonpipY-2Q2lGbd-jFhfwNfpat7D_STfRT8b0Qopt_hJBze5f7UTDLLvyEyYTrifEEh824NZDU-BobudTm9apjinZQkGosCA5nxS3QbqkZ2CzVAOzzNHMYr2RK5NwcClWNzungyQ6zLM0VRCWO-ELt6rePlTYu50vFSpc7a8OXf5TOAOKEe4abSa-dVv_cYQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر تیک تاکر به اسم فاطمه تاجیک دیشب توسط چندتا دختر که میگفتن عکساشونو گذاشته چنلش خفت شده و خودشو دوست پسرشو کتک زدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71704" target="_blank">📅 09:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71703">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozrHnidlqb8qY_AzkYGVG4ztkEknfOnJ7gH9ijVh-A7DLHFwKfujfOsIR5NLtURM2vr7JS717ufuVe0lUfPgAHv3lbAuvryYxr606G2P9RpGaIQvI9p90oz0vQlWfohgh8neDXUy5nhRmdY6G0Qm6Fwn6BCk7tXjZBNQyc74LvgabUxOjcEaLM5irUumK81hJoCCvpyIE7535CXlp2bMf46Q0WqGyK5VEX2-YwXKjeUn0j5nC-IUTzXwgyWsYAjq_GXIpLDaKjJq96oVVX3tDTdef4_psCQf1lz3iE2mSqfCNKnOQVwT1PUmN5SJUcjo48glgWA-XCqtB3SNSS0_aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس:
فرماندهان ارشد نظامی ایالات متحده، اسرائیل و هشت کشور عربی هفته گذشته در آلمان دیداری محرمانه برای گفتگو درباره جنگ با ایران و امنیت منطقه برگزار کردند.
این نشست که به میزبانی «سنتکام» (فرماندهی مرکزی ایالات متحده) برگزار شد، با حضور فرماندهان نظامی اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر همراه بود.
دریاسالار برد کوپر ضمن تأکید بر تداوم حضور نیروهای آمریکایی در منطقه با وجود حملات ایران، شرکت‌کنندگان را در جریان برنامه‌هایی برای گسترش تردد کشتی‌ها در تنگه هرمز قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71703" target="_blank">📅 09:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71702">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71702" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71701">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcZ0WvrELQmfnhXlztnxMBrAadnhaUjRIHFZvvtKdB9c4lObC-oYTIX-znCitnfqjlCG1mKEu3WPE9Y1PaRXGC8OFzoS1PznfkicigySa7W9FLLEHgfkUKLG68RngfKlhry4bN24IlBLQ_pxORjxiUFTlP6kakd5NQ7XI8ijClPe8PJdw5r7CdtIv_XBGWoXOTi-wpawtUNOohQ4UJticPGaUJNq_gjj1oWpyMk9AYxiC6Awme--I7LjqoWhN-2qg3MUMPNwCGlrILVPLPml9m4CobEwnVfNasaVTL2nOyHZUgrVgty-Yxks_T7DVx8EP8uTQB65QIQc8Iqnum6ZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71701" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71700">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71700" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71699" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euPdsdHEP2czbBVEpNFoY0sJXQa3MVS8kvevu3Z5-ay2rdciPJP8Xh0kymQjns00MANxl-ONOyhc1xhfrpuANJl5A3oTme4arS29mimimuszdqPSVyW8EbUaq7NUSWP-8J7_6wwznn2hjhV03PNpPwdoazY5nenuxWjYtNW4oImDXQgT_DSSNweAqEa-G4ahPRWqHHerxtAlSh5iu7KVQA0KVpmt2tcw976pD8lIHUJONyNcvNU8XSGEONlLLV8RH6vK8kGcgoPWzSrgNsPkZV8vvfPc15nB884wThlalwumL-Qi7QqEMwNX1xAl3diKJuC1nW7gSgGTi6G_f3jqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آلمان (DPA) مدعی است که حوثی‌های یمن اکنون در تنگه باب‌المندب مین‌های دریایی کار گذاشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71698" target="_blank">📅 01:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=WQf_p44mauCtxTtdfFQ4wmNaiOCz61pZZDOkheho6n6eMTYgBW2nc63khLm7a8C0vMBFpQBX6eHP5HdbD7YgNBQQekLopOY77md8wKQFPvyt5Ti4H7_3gk0ZI3X48WhyqKudHKyLNwEB3Zskn3SWuB6tN9s_0-4MX_eHYNPpLl1VeWCX52ta32DIlHS3420ehADvHvU0twWq2tpe8Yp-XSGhBJCxGyx-ND5j8E4pcqmRsQTygn0k6Z7Gf_D-Ay7Us8xN1R0G1AKMu7ozfmWPUrQbtI92zNv44O1KtA7tpwgtlE1QGiPKWApc2hs524gLt5vavxwunP6aHZpwb4lbhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=WQf_p44mauCtxTtdfFQ4wmNaiOCz61pZZDOkheho6n6eMTYgBW2nc63khLm7a8C0vMBFpQBX6eHP5HdbD7YgNBQQekLopOY77md8wKQFPvyt5Ti4H7_3gk0ZI3X48WhyqKudHKyLNwEB3Zskn3SWuB6tN9s_0-4MX_eHYNPpLl1VeWCX52ta32DIlHS3420ehADvHvU0twWq2tpe8Yp-XSGhBJCxGyx-ND5j8E4pcqmRsQTygn0k6Z7Gf_D-Ay7Us8xN1R0G1AKMu7ozfmWPUrQbtI92zNv44O1KtA7tpwgtlE1QGiPKWApc2hs524gLt5vavxwunP6aHZpwb4lbhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا به‌تازگی طرح استیضاح دونالد ترامپ را که توسط «اَل گرین» (نماینده دموکرات از تگزاس) ارائه شده بود، با رأی قاطع و سنگین ۲۳۲ به ۱۴۷ رد کرد.
بخش بزرگی از دموکرات‌های مجلس به این طرحِ پوچ و بی‌معنی رأی منفی دادند، چرا که اَل گرین خودسرانه عمل کرده بود و آن‌ها می‌دانستند که این قطعنامه به جایی نخواهد رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71697" target="_blank">📅 01:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ونس امشب گفت که تو ماه‌های آینده، جنگ وارد مراحل جدیدی می‌شه؛
اما در شرایط فعلی همه‌ی تحلیلگرهای نظامی معتقدند که بخاطر انتخابات میان‌دوره‌ای، جنگی گسترده از آمریکا نمی‌بینم.
اما یه نکته‌ای اینجا وجود داره، انتخابات سنا و مجلس نمایندگان آمریکا  نوامبر ۲۰۲۶ (۱۲ آبان) برگزار می‌شه ولی نمایندگان انتخابی، با ۶۱ روز فاصله به سر کار میان، یعنی از ۱۲ آبان ۱۴۰۵ تا ۱۳ دی ۱۴۰۵، سنا و مجلس نمایندگان با همون اعضای قبلی ادامه می‌دن و می‌تونن قانون تصویب کنند؛ بنابراین از لحاظ تئوری، بهترین زمان برای حملات دوباره‌ی آمریکا همین دو ماهه (در صورتی که دموکرات ها پیروز بشن)
ولی یادمون نره که ترامپ یکی از غیرقابل پیش‌بینی ترین سیاستمدار های دنیاست
#hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71696" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca73G4MvbNOaBbJO6VlqD1VKcIxCtD8bD4k2Vee753RkJiq4foHQZ6fyWq_xJrJVZVPlxbcprI0owHBnClu1v6QycSwD5WonuLG5qDVd5whdtZftKlkSStGFkII5wY-j77f8rOX48YQ_Df-YDJrAOWQ3LYS415veshHLLX6pFNU6ZRKxvewepCE3hbyxSI32W-VNao5WRaUpQUS48klz5YTvyWU3v6x8Ftz0emltzE-9fhX-NJCnXSWs3V0TqgLQB-sYEudKJs22MbLUDRC0ItHJYlgVQZoWTi2eAybk3hcyRddayE36YFPDoyD_Hp_UNp1kFb45ok8UfHlWSUKCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلیا هاشمی:  امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت. مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71695" target="_blank">📅 00:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایلیا هاشمی:
امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت.
مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین لحظه لغو شد؟ یا مسئله‌ای دیگر…
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71694" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71693">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=S4Nmlh-dIVElD3U4fd7nuNqXwC5MB5c6wnTavaWEQbdnblIeunScAUNrN2rk4DB6zPiNM6NPBysWBJb-5JQjp6uKzm1immJepet838LYUgFQDPFwJQIAV-5_5xOzu0rDTqv5WxCYq1YxKeSwLstZcx0yUmYhQhsAKMKz_ZygYMKsGRKtK3HHFtfHPdewJLcwmnRt1Ie3dmhlb_TXK2usXCZZGTjN3LR06St7o5onCsk5PJ5XcluC3FaN8lopCMGEOpbqyW5vOxnePf4ATUuoOBS9P1TK4G0JCRN0tgJe6I-PBmnxe4qsvKlbtt8yjYHhj-di-aSfZBW9gN4aGUR-vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=S4Nmlh-dIVElD3U4fd7nuNqXwC5MB5c6wnTavaWEQbdnblIeunScAUNrN2rk4DB6zPiNM6NPBysWBJb-5JQjp6uKzm1immJepet838LYUgFQDPFwJQIAV-5_5xOzu0rDTqv5WxCYq1YxKeSwLstZcx0yUmYhQhsAKMKz_ZygYMKsGRKtK3HHFtfHPdewJLcwmnRt1Ie3dmhlb_TXK2usXCZZGTjN3LR06St7o5onCsk5PJ5XcluC3FaN8lopCMGEOpbqyW5vOxnePf4ATUuoOBS9P1TK4G0JCRN0tgJe6I-PBmnxe4qsvKlbtt8yjYHhj-di-aSfZBW9gN4aGUR-vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سریع‌القلم:
آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات نظامی علیه ایران می‌آیند چه دموکرات ها پیروز شوند چه جمهوری خواهان!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71693" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71692">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71692" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71691">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71691" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71690">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=k9CP9YQk7_PQtOokR8-JYHciZ-iXFouzrIxKqR-aSF2DLkeJp3XUKlYEcyNL4ABYey81dlxK4XTzJ13QKnO-Q9DKlaZ075legBnLixPol7thnFbsksCfmlIO64xsG4YY33xIesyZd-PodVzdIuRifN1RpXD5r34yTs5geaYfaEAgYZmXWeqvixF9tudL3zhtlTMDFX-YtY3NWPTw3YGT4nyDFnjSsc5oWkidViw8jM30x7eAuMeOtwZpbvN-ffGOjGF_cXVKZzkmP_8CB2_ILa-1E8kaBxAxlQue4fMUTn9LCAk9l2P2qqRYjF7YSUkOclcxTGz_ZUiCp63rorKKDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=k9CP9YQk7_PQtOokR8-JYHciZ-iXFouzrIxKqR-aSF2DLkeJp3XUKlYEcyNL4ABYey81dlxK4XTzJ13QKnO-Q9DKlaZ075legBnLixPol7thnFbsksCfmlIO64xsG4YY33xIesyZd-PodVzdIuRifN1RpXD5r34yTs5geaYfaEAgYZmXWeqvixF9tudL3zhtlTMDFX-YtY3NWPTw3YGT4nyDFnjSsc5oWkidViw8jM30x7eAuMeOtwZpbvN-ffGOjGF_cXVKZzkmP_8CB2_ILa-1E8kaBxAxlQue4fMUTn9LCAk9l2P2qqRYjF7YSUkOclcxTGz_ZUiCp63rorKKDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای جنجالی یه
جنده
: دختری که ادعا می‌کنه باکره‌اس، دقیقا به چی افتخار می‌کنه؟
تو قطعا ایراد داری، مگه میشه یه نفر با کسی رابطه نداشته باشه؟ آقایون حتی توی سوراخ موش هم فرو میکنن، اونوقت تورو نکردن!؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71690" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71689">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=Hez8jWwrvwyGEr1k2fQkugAF1Rlyi9TsIP4nMw6S4DWR7sOaRpORRnu2qAPxUEUMcA-BTS2_-D-93rH7gkmHQzxB9mgGIFKK_9g5tJu_lza-rnZMdXLEpdPGVysFo691wFgpIVrIGYcDArwp5zp9U88LRE_B_12JudhcWSByamBS8zg0dEpJhl37wiT_VGdYLbcNHIj62KEHZPSzkgGMM1zWzE4XcAEiXLPolKULEuwwCyVa5GBsK0TyIEQC-uVgfBydTz3DN4Hs98Iiu7uDnsLwcgYw1MS91On7vaIJwl0a3f26jG6SMekI6wiCNeUzHn45bQiJr63SCNf1R1uWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=Hez8jWwrvwyGEr1k2fQkugAF1Rlyi9TsIP4nMw6S4DWR7sOaRpORRnu2qAPxUEUMcA-BTS2_-D-93rH7gkmHQzxB9mgGIFKK_9g5tJu_lza-rnZMdXLEpdPGVysFo691wFgpIVrIGYcDArwp5zp9U88LRE_B_12JudhcWSByamBS8zg0dEpJhl37wiT_VGdYLbcNHIj62KEHZPSzkgGMM1zWzE4XcAEiXLPolKULEuwwCyVa5GBsK0TyIEQC-uVgfBydTz3DN4Hs98Iiu7uDnsLwcgYw1MS91On7vaIJwl0a3f26jG6SMekI6wiCNeUzHn45bQiJr63SCNf1R1uWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی ایران یه تور راه اندازی شده به اسم «هیلینگ آب دریا» ، این شکلیه که میرین کنار ساحل و تا جایی که میتونین باید گریه کنین.
برای شرکت در این تور هم میلیونی باید پول بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71689" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71688">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان با انتشار بیانیه‌ای مشترک، برای(فردا) روز چهارشنبه ۲۵ شهریور ۱۴۰۵ (۱۶ سپتامبر ۲۰۲۶) فراخوان اعتصاب عمومی صادر کرده است. این فراخوان هم‌زمان با چهارمین سالگرد ژینا (مهسا) امینی و آغاز اعتراضات «زن، زندگی، آزادی» اعلام شده است.
در این بیانیه از بازاریان، اصناف، کارگران و دیگر اقشار جامعه خواسته شده است با تعطیلی مغازه‌ها و بازارها و خودداری از حضور در محل کار، در این اعتصاب مشارکت کنند. صادرکنندگان فراخوان، وضعیت اقتصادی، فقر، گرانی، بیکاری و همچنین آنچه تشدید فشارهای امنیتی و صدور احکام سنگین می‌دانند را از دلایل این اقدام عنوان کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71688" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71687">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265561794f.mp4?token=dzicX3QS3-zuMGKRRQ7e76EyUISAVqkmnPK85i-FPapwdYC4fAaH2mmlLoPQAEv1hxvptM9Yij8puiIdNj62jUG_3Qmvv38_eqhav7boi2h-Cw6oL_vZJ2uhpoUxx0kmKtEjFXlItxfnp6rtCxYQQTIQy3pFaeONe8dqRrJ47wLxWb02AQME3grI7vvDvlugqybF02xaROQtt0M7OaO9A63F7piIs6St9AK7Vf9NJeK9bvWFxE7EGCbUu9WbcsHjZzzUquH_U25MCNCQpqQ2-sf4oCAyKdInhLH3bgqQ0HYra-mzFoBH8Ur1h_JYJJ8SNMe1E1DDT0-xCNmo9E2vQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265561794f.mp4?token=dzicX3QS3-zuMGKRRQ7e76EyUISAVqkmnPK85i-FPapwdYC4fAaH2mmlLoPQAEv1hxvptM9Yij8puiIdNj62jUG_3Qmvv38_eqhav7boi2h-Cw6oL_vZJ2uhpoUxx0kmKtEjFXlItxfnp6rtCxYQQTIQy3pFaeONe8dqRrJ47wLxWb02AQME3grI7vvDvlugqybF02xaROQtt0M7OaO9A63F7piIs6St9AK7Vf9NJeK9bvWFxE7EGCbUu9WbcsHjZzzUquH_U25MCNCQpqQ2-sf4oCAyKdInhLH3bgqQ0HYra-mzFoBH8Ur1h_JYJJ8SNMe1E1DDT0-xCNmo9E2vQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی سخنگوی دولت :
امیدواریم نیازی به تغییر سهمیه‌های اول و دوم بنزین نداشته باشیم؛ ولی اگه بخواهیم گرون یا کمش کنیم حتما شما مردم را در جریان خواهیم گذاشت و بدون اطلاع‌رسانی کاری نمیکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71687" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71686">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شنیده شدن صدای دو انفجار از سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71686" target="_blank">📅 21:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71685">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/61894edf33.mp4?token=Pr7R8RhE4J7M80DaBq5bWVwOtuF8X9_hn9Q05BHNjggtW-tj4PXVDa5-OZ6y9MQrdPQqVLe_Uy5-XjgjyYPblMZwomBsEW41HghBPZt0bXOsWzPqdEcj3hRTlztye9HSqXRDVahPWRHb4M7OQ2cUqRGwDklUsuNFoX9vupFVC42JgfbzTquXCIrgRwciDPLYXACbuxOY0u24q7b5yK5Dw3FH9ArPqFkig7Hb9AWb-ycl2kKnJFoE3Hvc0Ps3zlsKQ7ABIKJ5kkJ2NNrza06PkWS27XTHUlZ_UJ-TnxOYr3xvW_kJYDjRFMPsM66n17M9qHsGBXLJnUgQgTxNx4ejvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/61894edf33.mp4?token=Pr7R8RhE4J7M80DaBq5bWVwOtuF8X9_hn9Q05BHNjggtW-tj4PXVDa5-OZ6y9MQrdPQqVLe_Uy5-XjgjyYPblMZwomBsEW41HghBPZt0bXOsWzPqdEcj3hRTlztye9HSqXRDVahPWRHb4M7OQ2cUqRGwDklUsuNFoX9vupFVC42JgfbzTquXCIrgRwciDPLYXACbuxOY0u24q7b5yK5Dw3FH9ArPqFkig7Hb9AWb-ycl2kKnJFoE3Hvc0Ps3zlsKQ7ABIKJ5kkJ2NNrza06PkWS27XTHUlZ_UJ-TnxOYr3xvW_kJYDjRFMPsM66n17M9qHsGBXLJnUgQgTxNx4ejvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، هواپیمای تهاجمی A-10C Thunderbolt II نیروی هوایی ایالات متحده، مواضع داعش را در نزدیکی «جبل‌العمور» در شرق استان حمص (مرکز سوریه) هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71685" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71684">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1vZr_OPiWthA1Vl-mWpjnLPnR2_Ne5L0-tM9GTwopFl13Lp22aKQmFI5NccTaBCaB-EV5GPPJhXm0ysEtp9dQESB8CoZeMugOgGK-5k1m-JFhrZGcm7pnr4QuwKCKj0cFtFCDNV2IIeUVyddenano0L88lh8iiRP3Qfd8--9bJURVmighJi_eIjqb2q4TZd3JLGoA2nKpzde77TpjWw7SBV9j3WFk6y0ys7s_XQnNXEaQhGQ1GF2bcSXKKBWrhvSDOglcQ_IQro7Yz9moWGEqGPkrSx5bCPadeLBluG3j3jdUokAZYXiu797HzPt9Y5kzmgAQW0PsqzWmKZ45kETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست:
دولت ترامپ در حال تدارک فروش ۴۰ هزار بمب سنگین (از انواع MK-84 و BLU-117 با وزن ۲۰۰۰ پوند) به ارزش ۲.۸ میلیارد دلار به اسرائیل است؛ این بزرگترین معامله تسلیحاتی از این دست در سال‌های اخیر محسوب می‌شود که هزینه آن از محل پول مالیات‌دهندگان آمریکایی تأمین می‌گردد.
این‌ها همان بمب‌هایی هستند که بایدن پیش‌تر به دلیل نگرانی‌ از تلفات غیرنظامیان، ارسال آن‌ها را به‌طور موقت متوقف کرده بود.
این قرارداد برای تصویب به کنگره ارجاع می‌شود و می‌تواند آزمونی برای دموکرات‌ها باشد؛ چرا که در ماه ژوئیه، بیش از ۱۰۰ نماینده دموکرات مجلس نمایندگان به کاهش کمک‌ها به اسرائیل رأی داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71684" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71683">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=gE1vOoMnspHb8cJrD1IiGM8sc7k9BZMlizbhzcHBY1Qi1BTvCKDYr2hzquRNOTpAscrvUNh0aqT-X3EYPlSRwTsGvhB2us-PpzV5GEvCRQkuPOlx-5_JZA6C8qHVecmwUfnS8q165vwmTQEikmi1M0Njms_faXaU_aDYBOSG8Mtgbd6yOywKw2AaTswnvrhymJ8HNZPmzIMS7x5po9d14W9rIthSdORv6Jhd-P0iyrXyZ1JQnSl7J4I3Jk2t3VmFSRfqUMkSEt0589PVdC00sxUAbSyEF-8EvNngXyooUc_Q3TDoVajuozE903R4YQp9z6xhHA93Ov6ECeBC9SkXuYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=gE1vOoMnspHb8cJrD1IiGM8sc7k9BZMlizbhzcHBY1Qi1BTvCKDYr2hzquRNOTpAscrvUNh0aqT-X3EYPlSRwTsGvhB2us-PpzV5GEvCRQkuPOlx-5_JZA6C8qHVecmwUfnS8q165vwmTQEikmi1M0Njms_faXaU_aDYBOSG8Mtgbd6yOywKw2AaTswnvrhymJ8HNZPmzIMS7x5po9d14W9rIthSdORv6Jhd-P0iyrXyZ1JQnSl7J4I3Jk2t3VmFSRfqUMkSEt0589PVdC00sxUAbSyEF-8EvNngXyooUc_Q3TDoVajuozE903R4YQp9z6xhHA93Ov6ECeBC9SkXuYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از نفتکش «ال‌گایا» (EL GAIA) پس از اصابت به آن در بخش جنوبی تنگه هرمز منتشر کرد.
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که ایران ماه گذشته با موشک و در پایان هفته جاری نیز با پهپاد به این نفتکش حمله کرده است؛
در مقابل، ایران مدعی است که این شناور پس از ورود به «منطقه ممنوعه» در بخش جنوبی تنگه، با یک مین دریایی برخورد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71683" target="_blank">📅 20:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71682">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=og-vZtCLLJLdcovhIB6Yjx_9awSHD3677lq8rRhEfN6Z4Fp9pcnk6WZ3T8UyF3DNaFW5lKkf2bCCV_lmVGA4qF-51EyvuLDA3yoYX10gLrKKdsjTM0U8zHgKYmpPlpSD_Z4YYYa5e6HdCfqcZEnOtGqWvuVC_BbnZf_7UQPjlGH7YN3EQtei5gTVcM0PZTo9UbkskQ0GfPWLWw7_CfFyGdi5VgssQwxe-2awkR5lh0AFYnFDNJFFnNK6wuY16hp3P0Be_P15gWyxq6Cw6aJldcJr6Eh2E_c5tvi9jIAB_ROhXSUmSPiLo54dZK5-b3C9C80Ov2a_pCzrFvBus7Rh2yPXY1eDV4qYkPWhELb27iuCK-8Yub4G2WbZc-kZ3op0g-X7hoGL6VJvTWpTVB0Ai2uxt1dBswiDo6AbOxv8_Wr229kpDSmuIXywS1bIjX7nelqPvP3zoQGjE1YvCLPAAUCiTMlh0Pn7UfV9rg8hOX0DHvD2QRm2i6aqjX9GNGOK-B72ntND7oBqVN0nouq-jzaJiAzD8gdoCjjaYU1YT4ua01F-fgm1q7zjE3AYPpHKJlps54pqMOVaCvRAEPsRPFqbwpTj_6LffJMzGNtvG7GbyG89x1ZoP0My13be00adTgFbXH9Ic1kLUv4qH85UZtaQAgNauq9SHVKPPkM5rWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=og-vZtCLLJLdcovhIB6Yjx_9awSHD3677lq8rRhEfN6Z4Fp9pcnk6WZ3T8UyF3DNaFW5lKkf2bCCV_lmVGA4qF-51EyvuLDA3yoYX10gLrKKdsjTM0U8zHgKYmpPlpSD_Z4YYYa5e6HdCfqcZEnOtGqWvuVC_BbnZf_7UQPjlGH7YN3EQtei5gTVcM0PZTo9UbkskQ0GfPWLWw7_CfFyGdi5VgssQwxe-2awkR5lh0AFYnFDNJFFnNK6wuY16hp3P0Be_P15gWyxq6Cw6aJldcJr6Eh2E_c5tvi9jIAB_ROhXSUmSPiLo54dZK5-b3C9C80Ov2a_pCzrFvBus7Rh2yPXY1eDV4qYkPWhELb27iuCK-8Yub4G2WbZc-kZ3op0g-X7hoGL6VJvTWpTVB0Ai2uxt1dBswiDo6AbOxv8_Wr229kpDSmuIXywS1bIjX7nelqPvP3zoQGjE1YvCLPAAUCiTMlh0Pn7UfV9rg8hOX0DHvD2QRm2i6aqjX9GNGOK-B72ntND7oBqVN0nouq-jzaJiAzD8gdoCjjaYU1YT4ua01F-fgm1q7zjE3AYPpHKJlps54pqMOVaCvRAEPsRPFqbwpTj_6LffJMzGNtvG7GbyG89x1ZoP0My13be00adTgFbXH9Ic1kLUv4qH85UZtaQAgNauq9SHVKPPkM5rWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
تنها کافی است به سخنان رئیس‌جمهور، رئیس مجلس و رئیس بانک مرکزی ایران اشاره کنم که اذعان داشته‌اند اقتصاد کشور در وضعیتی بسیار وخیم و بحرانی قرار دارد؛ هشداری که خطاب به هم‌قطاران تندروی آن‌ها در سپاه پاسداران و همچنین مردم ایران بیان شده است.
ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم؛
و در کمال ناباوری، کشوری که سومین ذخایر بزرگ انرژی جهان را در اختیار دارد، اکنون با قطعی برق سه تا چهار ساعته مواجه است.
این وضعیت اسفبار اقتصادی ناشی از تحریم‌هاست؛ ترکیبی از تحریم‌ها و اقداماتی که ما طی ماه‌های گذشته برای شناسایی و مسدودسازی مسیرهای مالی و سیستم‌های پرداخت آن‌ها انجام داده‌ایم و در حال اعمال فشار شدید بر آن‌ها هستیم.
به باور من، واکنش‌های تند و خشونت‌آمیزی که اکنون از سوی آن‌ها شاهد هستیم، درست مانند رفتار حیوانی زخمی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71682" target="_blank">📅 19:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71681">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=UGhYWEfAk4Roc3RvskP5lo83zp176mBjf434qYeEKNDEZA-08VDdtC0yitXlHjJjy6tWAno6wMD2MJ65pRp7LY2OluewQVTswaKVRBhmBgz_lYwyCqkcBLcSB5Oshkb_jeixpSWD1ztb0vNmQnirLW0a7fmV7NN3eDaHotOOuU-ZWbopWzx28jvA4N0Bkgxov60EPSMd6TUqH3QCKK3dTJcPyPQuBc658e3blzIbJSWxHaJf1uSqAyWNWoekmcge4_qqnCsyXNVCFUMMW-_g5dYn0qEsuWSmcg1XGKnuep_1CR7xIJrXxLenoK7mUKmr-2BTutr-OD6huAoUgqknOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=UGhYWEfAk4Roc3RvskP5lo83zp176mBjf434qYeEKNDEZA-08VDdtC0yitXlHjJjy6tWAno6wMD2MJ65pRp7LY2OluewQVTswaKVRBhmBgz_lYwyCqkcBLcSB5Oshkb_jeixpSWD1ztb0vNmQnirLW0a7fmV7NN3eDaHotOOuU-ZWbopWzx28jvA4N0Bkgxov60EPSMd6TUqH3QCKK3dTJcPyPQuBc658e3blzIbJSWxHaJf1uSqAyWNWoekmcge4_qqnCsyXNVCFUMMW-_g5dYn0qEsuWSmcg1XGKnuep_1CR7xIJrXxLenoK7mUKmr-2BTutr-OD6huAoUgqknOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر، آتش‌سوزی‌های گسترده در تأسیسات ذخیره‌سازی «آرامکو» در «ابها» واقع در جنوب غربی عربستان سعودی را پس از حملات پهپادی و موشکی حوثی‌ها نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71681" target="_blank">📅 18:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
لحظاتی قبل یک پهپاد دیگر از نوع MQ-1 متعلق به آمریکا بر فراز تنگه هرمز با استفاده از یک سیستم پدافند هوایی متعلق به نیروی قدس سپاه پاسداران انقلاب اسلامی سرنگون شد.
این سومین پهبادی است که سپاه مدعی سرنگونی آن در روز جاری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71680" target="_blank">📅 18:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71679">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8132b94509.mp4?token=HRNwzUxFg5MIqUfXaH1fjbiq440Lp5Bg7mHkiiolVXHsCl7dCGGXAJ5ybq-Kri4Hz5UNoKcDIdIKyVG5YnofHPPNU_Led2YNCZYLROGW36fOA2QZkFyONIocZ_ZRFNXUPaIIUEIi1BgEr0MN1SpZFJ2-P6Qr40JiYR8M7QvCa9nssyazeGzBh2KpYuvRX0E7lhSZKMgzCwaJ3RdRqPO5P9P1-754ZnveWpF1l2HNJjg-YZC9Sfp7ITn9TIYg1xP1FDgf_83L2l4ca0_9G-yLBiuGj7ZxeC0GdEinpb7fecU5_3Z4vC8QKI6ccLOhA8mYr96j8-3gP8B-vWmquk3nlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8132b94509.mp4?token=HRNwzUxFg5MIqUfXaH1fjbiq440Lp5Bg7mHkiiolVXHsCl7dCGGXAJ5ybq-Kri4Hz5UNoKcDIdIKyVG5YnofHPPNU_Led2YNCZYLROGW36fOA2QZkFyONIocZ_ZRFNXUPaIIUEIi1BgEr0MN1SpZFJ2-P6Qr40JiYR8M7QvCa9nssyazeGzBh2KpYuvRX0E7lhSZKMgzCwaJ3RdRqPO5P9P1-754ZnveWpF1l2HNJjg-YZC9Sfp7ITn9TIYg1xP1FDgf_83L2l4ca0_9G-yLBiuGj7ZxeC0GdEinpb7fecU5_3Z4vC8QKI6ccLOhA8mYr96j8-3gP8B-vWmquk3nlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پروازهای داخلی(کرمانشاه به مشهد)دچار سانحه شده و بخشی از کابین دچار شکستگی و اسیب میشه، خوشبختانه مسافران این پرواز سالم به مقصد رسیدند. جزییات دقیق این پرواز و نقص فنی هنوز مشخص نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71679" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71678" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71678" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMhxyHVYZSK8fOC90BcJLSOhClpEHjkCdIPzQww4wc0UwNzqcwznHmDI588caPCHa2viEtttL0gziaUC_odlU_vKsfPuYkvgroQSaw4ggL3OD8-phHCYAfudH4DwunlD_Bb3T_-xXked7_kd2MVUbm1D_ub2Qxm4ILJfJNVHGaDajBPfFRttPxa4xAYoBYq6rHRNMi-nRnkEd6Sn3MZCGHL5SWFYii-UbAIAyORZFPk7gacpjOOTwLAAG2U0tPy8MQOd_N9l0XmQSdqjdHxHKnyFNqbaglxImh1LaUr26xp4dGRyJlCIra4u8aHjXg6R3W2dgwVWCneBTBbO3ReyuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71677" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71676">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=YSUrfGKwtDIgUVk2dbR93ROzgfR8TW3kvFKOvqyrZR4fNFUmGcqQgm3Hw1t4WungKj21R3h0QaZTCAgAVEZAMjXotyIuyP6mbtKzq-ntpB1GCkvDAWw_uVDarJMupqAtopJuOE2f1-6P7MBEQAMw-YSmirmoxRrikEcU8aw9ssWXhWijYOKl4fzvrJ3TQ_gpJD6_9YPqipuTGvuf1hTo6gxMjTrREYfUyeMOL1IMRhzRQW_DglAAYdZvvSXbi-jihrwhM9MR7Ucagqyp5iggd7Gdh8zd-GPulyPrHFFW6M7ShLw5TB_0x76TjFqe2_1A6gKV5D-tYh62Vv9W-Ge6Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=YSUrfGKwtDIgUVk2dbR93ROzgfR8TW3kvFKOvqyrZR4fNFUmGcqQgm3Hw1t4WungKj21R3h0QaZTCAgAVEZAMjXotyIuyP6mbtKzq-ntpB1GCkvDAWw_uVDarJMupqAtopJuOE2f1-6P7MBEQAMw-YSmirmoxRrikEcU8aw9ssWXhWijYOKl4fzvrJ3TQ_gpJD6_9YPqipuTGvuf1hTo6gxMjTrREYfUyeMOL1IMRhzRQW_DglAAYdZvvSXbi-jihrwhM9MR7Ucagqyp5iggd7Gdh8zd-GPulyPrHFFW6M7ShLw5TB_0x76TjFqe2_1A6gKV5D-tYh62Vv9W-Ge6Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
بسنت درباره ایران:
ترامپ در حال اقدام علیه رژیمی است که خود را وقف شعار «مرگ بر آمریکا» کرده و برای تحقق همین هدف به دنبال دستیابی به سلاح‌های هسته‌ای است؛
اقداماتی که رؤسای جمهور پیشین مدت‌ها از انجام آن طفره می‌رفتند.
تحت رهبری او،آمریکا دیگر تهدید ایران را مدیریت نمی‌کند؛ ما در حال پایان دادن به آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71676" target="_blank">📅 18:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71675">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiF6J_0CPwQrJbWoYQwO106CVPfQc0L3B4iv6HT89iU1AwjhNui9jqfuKGJ5PH4ye7D8gFHFmayUmtjX0EXuN1TRW2n13k-2Qxa-OuSTYDNXMTNMoNexpuNII7djjzpNBH0Hj9RNJ_OIT0LDRVbwg9MtkdPIg0bYuyZzEhhg8ji-KLRjvEvJucZCcZdn-iupb1VFg-qaXm7DMPJS5LSKVDQ_pfx0RVwp3kxhsvUkcIMlX4LbDKygEi8gxmUGKAVdJnunoriX-C4xzQ-zLx9eVwdBQN9-yIXN8lqsEOHp9ZeM9RvTNvHourFJJTTC1PB9hgy1ZhPozrwrZjMlp9nM2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس. تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.   @News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71675" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71674">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=TlHDTLKTX-Oongpogo-HvDjtkZDURmhkuUfQNNiVLm1rPD5ukrPAswpJRcajBNS6Cn40a4EvYV4sjxce4k43qZeYr8VoeALdW1rQaMJCBtLwSQEWyezH4x2XW6VS7cbaMhXdRzfyQrPwLJa7Ma-q8Z_a3cQ27cjPJMV2t9sRTdAjn0gsjjgrUNDv6zGYNh6OAAqLbBO7eCrLo5lwk0KW6N1SFyLpY6KaiW_N7806PhjqYSYhsnOrSbdGbtsOOD0p4ncTZo4vHDnvqGDVFG5NEA1p_bY_fABMhhcHV6vsSeXxZwbkhmoNa1NsMvgfJnA-Xb0ncCRj2G4ZXDHrgDEzYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=TlHDTLKTX-Oongpogo-HvDjtkZDURmhkuUfQNNiVLm1rPD5ukrPAswpJRcajBNS6Cn40a4EvYV4sjxce4k43qZeYr8VoeALdW1rQaMJCBtLwSQEWyezH4x2XW6VS7cbaMhXdRzfyQrPwLJa7Ma-q8Z_a3cQ27cjPJMV2t9sRTdAjn0gsjjgrUNDv6zGYNh6OAAqLbBO7eCrLo5lwk0KW6N1SFyLpY6KaiW_N7806PhjqYSYhsnOrSbdGbtsOOD0p4ncTZo4vHDnvqGDVFG5NEA1p_bY_fABMhhcHV6vsSeXxZwbkhmoNa1NsMvgfJnA-Xb0ncCRj2G4ZXDHrgDEzYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سی‌و‌سه پُل اصفهان، یه پسر نوجوون اومد مثلا یه حرکت نمایشی بزنه و از یه ارتفاع نسبتا بلند بپره پایین که فرود ناموفقی داشت و با سر رفت تو زمین...
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71674" target="_blank">📅 17:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=fPwiM_sniRTWCcq6LWR7_aHXirtAguo4uVxZuWFFX1QZHrh1AKXDUM0FGyk7msYvfPXIMk43PhxNM2tf1TZRLWOqK38ZxJjO7pH3HrR3Hmr_dsAYqjAe_0e0pNOV4NbMV9IbpCwjhwG_T5enYlllVpDudQ7Yq1wKppV9kTxZYCu3sBG1z6kJGVBTTQhdfq7s9oOrCtBg86vh39NuhNEZYpHCuuXDNZ0Ab2TNi7yEifLpMnGSsh2cuRApYFnp1p9M6WoMmPOoZ6KabWqhXsV9vGBtmZzkCWf8LKb3aQUKLXX65WKRtlQ9oyE5PMLhiMHwU0-5eu2NmhnAYRDVgQ2LqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=fPwiM_sniRTWCcq6LWR7_aHXirtAguo4uVxZuWFFX1QZHrh1AKXDUM0FGyk7msYvfPXIMk43PhxNM2tf1TZRLWOqK38ZxJjO7pH3HrR3Hmr_dsAYqjAe_0e0pNOV4NbMV9IbpCwjhwG_T5enYlllVpDudQ7Yq1wKppV9kTxZYCu3sBG1z6kJGVBTTQhdfq7s9oOrCtBg86vh39NuhNEZYpHCuuXDNZ0Ab2TNi7yEifLpMnGSsh2cuRApYFnp1p9M6WoMmPOoZ6KabWqhXsV9vGBtmZzkCWf8LKb3aQUKLXX65WKRtlQ9oyE5PMLhiMHwU0-5eu2NmhnAYRDVgQ2LqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71673" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71672">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نفتالی بنت درباره ایران:
این رژیم فاسد و پوسیده است؛ همچون درختی که از درون دچار پوسیدگی شده و سرانجام فرو خواهد ریخت.
در مورد این درخت پوسیده، می‌توانیم اینجا و آنجا حفاری‌هایی انجام دهیم. منظورم صرفاً اقدامات نظامی (کینتیک) نیست.
صحبت من درباره اقدامات اقتصادی، کارهایی که نمی‌خواهم نامی از آن‌ها ببرم، و همچنین تقویت معترضان داخلی و تقویت دشمنانِ این رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71672" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71671">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=MH2ERvQO5FXkYkzvS79aOIS7yHQS-Ul266DpqftP0h4-6Cqqk1zOX3aSDM0F88IG3An-_fIELHsCXTAtjKvoZ72ktBXoGTVPFRLqpNw5UDtYu1rvg9kKpWfMwG3Jw7X1afTiz4__mXKj5mKrAZp3_VxkjqbcS95eKroohfjOk6Q_ypA27fIWEBBWQNccQ8TU_MqVTF5LrLEYjKDn3NaI7-ChfQhXBonhDPd1jZ0tyHKCkFuYNtNn4L84DgLKYC-R_WYevb8JWPCt-b6WMAVrl1-2SCbbYdtIdVxR18zXjOBc5OuiUKLGPRbIV0uTQQ_NFhWrz8b8FAJH5Rak8KbZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=MH2ERvQO5FXkYkzvS79aOIS7yHQS-Ul266DpqftP0h4-6Cqqk1zOX3aSDM0F88IG3An-_fIELHsCXTAtjKvoZ72ktBXoGTVPFRLqpNw5UDtYu1rvg9kKpWfMwG3Jw7X1afTiz4__mXKj5mKrAZp3_VxkjqbcS95eKroohfjOk6Q_ypA27fIWEBBWQNccQ8TU_MqVTF5LrLEYjKDn3NaI7-ChfQhXBonhDPd1jZ0tyHKCkFuYNtNn4L84DgLKYC-R_WYevb8JWPCt-b6WMAVrl1-2SCbbYdtIdVxR18zXjOBc5OuiUKLGPRbIV0uTQQ_NFhWrz8b8FAJH5Rak8KbZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌ های این خانم به‌شدت وایرال شده و دخترا هم خیلی بهش انتقاد کردن:
اگه یه مرد، دارایی های خودش رو به نام خانومش بزنه، اون زندگی رو با دستای خودش نابود کرده.
آقایون اگه ۵ تا خونه هم به نامشون باشه، هیچوقت تو دعوا خانوم‌ خودشون رو بیرون نمیکنن
ولی اگه خانوما یه چیزی به نامشون باشه به این موضوع فکر میکنن که میتونن بدون اون آقا ادامه بدن.
من خودم خانواده‌هایی دیدم که به دخترشون میگفتن تو که ماشین و خونه به نامت زده دیگه احتیاجی بهش نداری، خودت برو زندگی کن.
خانوما اصلا جنبه‌‌ی اینکه چیزی به نامشون باشه رو ندارن، اون اگه بخواد زندگی کنه با یدونه سکه هم زندگیش رو میکنه، آقایون بفهمید من دارم چی میگم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71671" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=BdkyHeGi-mauYx5ojAkJBWUyVFUhtnxCx91q0HzQZOO1E_-3oDtTXiu12ec6XFdV69J9QW_qfKkH0TkwbDM80XTKm9RWrZ80AaCl9kSlgTzNT2-zwOp47EXml62I6hu8qspru1FSNC_nXVMJj-p6tW6Jgp2AB88mJ0ahfLtzANwajWqny2kzPolyLb52hQERnGsCZ2oPLCVuun7KcVzA4Ydu0FtP0MefQ4geOREmiR82zt2rnUFyQtQARbJio3vjpY4MCoPMWHM0Uszv1OtogMnydIqjSYGa3w4oWwut_p_Rcs95GfiteFuZl030s-MbQHcaEgB8r8jvX-pMNB9sAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=BdkyHeGi-mauYx5ojAkJBWUyVFUhtnxCx91q0HzQZOO1E_-3oDtTXiu12ec6XFdV69J9QW_qfKkH0TkwbDM80XTKm9RWrZ80AaCl9kSlgTzNT2-zwOp47EXml62I6hu8qspru1FSNC_nXVMJj-p6tW6Jgp2AB88mJ0ahfLtzANwajWqny2kzPolyLb52hQERnGsCZ2oPLCVuun7KcVzA4Ydu0FtP0MefQ4geOREmiR82zt2rnUFyQtQARbJio3vjpY4MCoPMWHM0Uszv1OtogMnydIqjSYGa3w4oWwut_p_Rcs95GfiteFuZl030s-MbQHcaEgB8r8jvX-pMNB9sAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی نیروهای انتظامی به سمت بالگردآمریکایی در جریان عملیات نجات خلبان مفقودی آمریکا در روز روشن
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71670" target="_blank">📅 15:03 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
