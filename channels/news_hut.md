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
<img src="https://cdn4.telesco.pe/file/v86Oc6utbMeeY0UQf6ZixNb1XZ5qEeJoSvUnyi_2q889zebKEI5GeWFesJ5Tn0PNL1Zu8wMPsqOsCbj4Q5zHcPRE9JN7igugiS6-GgPzE9-dqnIKbXU-7wUHoGol2WjLWabd0uys01_5AyyhV_4MVNjv4xoBYWLujSJooPlb3z2uvHrJlLeSIoR_IeidmoBTYgNFTeaedtQLnptNy5Qya12DCn6U06EJ8fivA5g9WZC3YArLl0IX7O6bbsIyu9x59X5OyciGB4CmgiVgcvvAbjZ0pVlqxMzBEP4HbU8FfJ3VppybWlrNjAUIQbQ4jYXxCLiqyefi1Ffcsh1Xe5KbRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqAIDyxRaO5-3WQOrttPODZnbH64PPzm_bdeLxb0yzWVE7_Sa5XTVkyVuZrhaTxtuWdyYTvwijQzryxNsIZcLI9hVLtAt2CrYtnC8TZ_WTuoYEKhZAWpMb5tBZm7h5mtXntmt0iFaS7w_iRrEjkc75sir_ZY-wMrtp9V46OEsrzxzfhYRJYPzl3MvFKX2aPx4H8x4vQdFjS364_mZ5iv8jiZ25XA67PkWhne1mqtpNBkd7rtpdAaim8LWqUJNeTAGfxxCyB-MrKneMwMRzZuiwo8eMHgICPkKqCKeLzNgBUOW863Yam0VH7x78DRyy7XcPhuz9cBzcUTDU1Jqm78nIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqAIDyxRaO5-3WQOrttPODZnbH64PPzm_bdeLxb0yzWVE7_Sa5XTVkyVuZrhaTxtuWdyYTvwijQzryxNsIZcLI9hVLtAt2CrYtnC8TZ_WTuoYEKhZAWpMb5tBZm7h5mtXntmt0iFaS7w_iRrEjkc75sir_ZY-wMrtp9V46OEsrzxzfhYRJYPzl3MvFKX2aPx4H8x4vQdFjS364_mZ5iv8jiZ25XA67PkWhne1mqtpNBkd7rtpdAaim8LWqUJNeTAGfxxCyB-MrKneMwMRzZuiwo8eMHgICPkKqCKeLzNgBUOW863Yam0VH7x78DRyy7XcPhuz9cBzcUTDU1Jqm78nIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=F4kW1sC9NbybkpJf3P7f4LSKXBzReg2t5TopkSswMZq7c_RzDljKPgj4dXfWczl_YX4t92m7vqcSLATtEBMFb4idt1NXZsSAlfyXwE5g6Dj8aQ5oR3X-6BEyxrwh2tCCuo6sg3IneZV7V8jkLhVy7xoNbayqSE-OcNoA-FoWxvockqZjFp0IrtaHihNmr-lQg5dtUYzZEtXy8iV0pTRDDA_Zckft1wWcdTykEnG2ahBohWGcyKJV4LuMYuR_8Ptzxj4oFH2KP_9N-05ZAjWD8hVk8r_qZUikU4gv9dSU0IFlav096DBCJhLfL1oL0IKQu7vs-RJPCHQsjAOUBkYdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=F4kW1sC9NbybkpJf3P7f4LSKXBzReg2t5TopkSswMZq7c_RzDljKPgj4dXfWczl_YX4t92m7vqcSLATtEBMFb4idt1NXZsSAlfyXwE5g6Dj8aQ5oR3X-6BEyxrwh2tCCuo6sg3IneZV7V8jkLhVy7xoNbayqSE-OcNoA-FoWxvockqZjFp0IrtaHihNmr-lQg5dtUYzZEtXy8iV0pTRDDA_Zckft1wWcdTykEnG2ahBohWGcyKJV4LuMYuR_8Ptzxj4oFH2KP_9N-05ZAjWD8hVk8r_qZUikU4gv9dSU0IFlav096DBCJhLfL1oL0IKQu7vs-RJPCHQsjAOUBkYdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Djc2buSiJ0pCKkotMSHkZt3L0-kUTvmZ-c7GBLMj3R66acEyp0_GuCni1L1AUdsMG9rnQHlB2tIdYdVM--IN3FOhR8vpMo34rANzVOCE9pzfJtJpYlagqor2zutCOqBHMChSPPdrQQ4S6gcVlEay2a6PVg1CNvHay3O7Mv4XfX3PVH7S8YcX5dLQT7vabGTT3It52Rr_fCrzT9MtKAXP1X2Rg_0QmeUTulXnu8frH8Ynn-uk9DgU_76AdTYvzr-zcNKS_KT11xjjW-HwjlV488U0dAzzxvfn8T9bvQPFOTVuYllFbe4xXvOtr7_-uR8fLfYjWsphkacrPd1AnNxCJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Djc2buSiJ0pCKkotMSHkZt3L0-kUTvmZ-c7GBLMj3R66acEyp0_GuCni1L1AUdsMG9rnQHlB2tIdYdVM--IN3FOhR8vpMo34rANzVOCE9pzfJtJpYlagqor2zutCOqBHMChSPPdrQQ4S6gcVlEay2a6PVg1CNvHay3O7Mv4XfX3PVH7S8YcX5dLQT7vabGTT3It52Rr_fCrzT9MtKAXP1X2Rg_0QmeUTulXnu8frH8Ynn-uk9DgU_76AdTYvzr-zcNKS_KT11xjjW-HwjlV488U0dAzzxvfn8T9bvQPFOTVuYllFbe4xXvOtr7_-uR8fLfYjWsphkacrPd1AnNxCJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCrMBgiod3AAtxGHnbsryD4SYpptlUHSFRa-V4eusO2gWJ5zmVQkXtKk598FWyhcjiKI8xeuJYQXCN74ixaiUqzTG4vapo1m24_HDaLh3wY802KwzJppVwBZvhy3RYZSjRjDqJ4mIFLz2wtb828r5AsantxirbwjN_ZEua6FxsLRr0nXjSdfH_HUNAbvusccorzWJMM7kb4daWcd55XPvOa-GKIIxMEQVE8bXRx1Dg1y_Bf7s_rXWXEGHoI_m_dkxg51qyNqkxsDxT81JjOMX_2yW01Rxpksj4yxxY6jnLaNRsLVif4_VqZKHK1b2MpAUEyD_hGONBO5vBViXNFnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
📰
سی‌ان‌ان:ایران به سرعت در حال ساخت یک تأسیسات هسته‌ای مشکوک است که در اعماق کوه گرانیتی نزدیک نطنز - ملقب به "کوه کلنگ" - دفن شده است و تصاویر ماهواره‌ای افزایش ساخت و ساز در سال 2026 را نشان می‌دهد.
این سایت احتمالاً برای محافظت از سانتریفیوژها یا کارهای غنی‌سازی فراتر از دسترس بمب‌های سنگرشکن فعلی ایالات متحده طراحی شده است.
ترامپ تهدید کرده است که به آن حمله خواهد کرد ("ما ممکن است خیلی زود کلنگ را بزنیم")، اما بزرگترین بمب غیرهسته‌ای پنتاگون ممکن است به اندازه کافی عمیق نفوذ نکند.
نشانه‌ها نشان می‌دهد که ایالات متحده در حال حاضر روی این مشکل کار می‌کند: یک روز قبل از شروع جنگ، یک آژانس سلاح‌های کشتار جمعی پنتاگون قراردادی اضطراری برای تعمیر یک تأسیسات آزمایشی زیرزمینی که در گرانیت در وایت سندز حک شده بود - مرتبط با شبیه‌سازی حملات به عمیق‌ترین پناهگاه‌های ایران - امضا کرد.
یک بمب "نسل بعدی نفوذگر" در حال توسعه نمونه اولیه است.
تحلیلگران CSIS می‌گویند کلنگ هنوز عملیاتی نشده است، اما ساخت و ساز از حفاری به ساخت و ساز داخلی و سخت شدن تغییر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=A0YdovehugeydJExYFcX_1NGfFkb9_kFDCrNGdWS5Ft-yYcQlh_y_w4QbtJbsLSH2D6wgQG-7FWrsgJ600R9JrWGU4ri9NuE7JQUoji8OCDdlsJhOjid-IrFGR2TtNyeBQZSicQd5mh4MlIpz6Klw4_yMfgWNlwu2OIPx-viH0Iz4LA1HiAOolbhPiFEhMgDCkvDl5q3x3Fx1xoYE9qAwBDmJbBP5XMYGStibT0jvZH3Uat9sIv7-PBlKzZm5rEvbAH6YWc3_ubkGhaEcXB0ZV_GWL3NmTY1wewejRivFwE54IbMWTucH68doXXH4huFMzR-CyP0p7UHY8ap5RQDBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=A0YdovehugeydJExYFcX_1NGfFkb9_kFDCrNGdWS5Ft-yYcQlh_y_w4QbtJbsLSH2D6wgQG-7FWrsgJ600R9JrWGU4ri9NuE7JQUoji8OCDdlsJhOjid-IrFGR2TtNyeBQZSicQd5mh4MlIpz6Klw4_yMfgWNlwu2OIPx-viH0Iz4LA1HiAOolbhPiFEhMgDCkvDl5q3x3Fx1xoYE9qAwBDmJbBP5XMYGStibT0jvZH3Uat9sIv7-PBlKzZm5rEvbAH6YWc3_ubkGhaEcXB0ZV_GWL3NmTY1wewejRivFwE54IbMWTucH68doXXH4huFMzR-CyP0p7UHY8ap5RQDBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71365">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/news_hut/71365" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71364">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as6w2wIf2m3RlcQvoIHR7VI0mNPz1-liWmG17TY5haVDDzppgN6MbuOU9Hv5XgIRMJ0O1Lcjv7W5xMcK69mYKPqXjPFLosBFHr-CshWtBhbpI6phNuNfTc9y8ImmnSiP38LSi35z3-87uTdclg5Fae-_4ocuZ6fgWjooMSpmS65vCy7q1VXHcXMNczsuDb3Y0CgBusRiRJ-32t8_RVVGQKVoSRc0-AAkaU8vQ1YurkK0Or9rjsvqZkxZarCQwlq6cqw3Lj3P2savsbQPClY1BfE4iZip5b8l7NYp02Tl7FE2OmIzOxTcjtxcM5s85pE_ATTh-CETE7M1GjSiD-hohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/news_hut/71364" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71363">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hHuoz8uQgK3qBOENQsSa8Cvi20snGdWRlpxRtS0JTeyW2EsYk00IJMXxKtCsrT5sN6Vvyh-po5Rzib-SBDF6FWrytK5sqNb1kwtDaoKh6cBa11zthOypYvelqaOY5ysy6Opswm96E3SAB1OHttTIY1zBeOrj_CEQ9904Vg11747TY3balMTHb_UAcmj9UHWUr5tujKjRY5UlpaRVsXeoE06bOuPMBLkcOtT-xMmcyhVtBfvD3bta1RjrZhYxI8trcmCb5v7ai3Htfd1GwCmOBv4UWsrMbLFh03H8Z1ONoQVkDChMvuwQHyttxfQDJ3ebgaWqvBiwmV6pRqPY4CId3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hHuoz8uQgK3qBOENQsSa8Cvi20snGdWRlpxRtS0JTeyW2EsYk00IJMXxKtCsrT5sN6Vvyh-po5Rzib-SBDF6FWrytK5sqNb1kwtDaoKh6cBa11zthOypYvelqaOY5ysy6Opswm96E3SAB1OHttTIY1zBeOrj_CEQ9904Vg11747TY3balMTHb_UAcmj9UHWUr5tujKjRY5UlpaRVsXeoE06bOuPMBLkcOtT-xMmcyhVtBfvD3bta1RjrZhYxI8trcmCb5v7ai3Htfd1GwCmOBv4UWsrMbLFh03H8Z1ONoQVkDChMvuwQHyttxfQDJ3ebgaWqvBiwmV6pRqPY4CId3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
دیروز تو سمنان عرزشیا برای مجتبی خامنه‌ای جشن تولد گرفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/71363" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71362">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ece16841.mp4?token=GokGvW-bZ7cqZyBcEKSGkGXYvy3BavgL29oqacy6VulXGoFwh5KiymuL12NDHLN2atatr2d8qdyYnjMoswkA-AZ33A2VwgaZaxgaZxH-c3u9LxaM01PGOx6gysKkiOwqiY0gY5ekLHcjQhaVrNmxrAg2EqJNRYVKlE3hbpxEg1hE3OowXC1KtttSuw96KtX4QzSG4RAgk6o7jXHfFLkL_Z9p8k7fS6dqWxayTqVhTCrGzOYlLHtU-m6a4ECZnnx1AHg6AWEyfRAp4zI7BZfZNGaA3lid1y8KnD8VqgRYYQZw6maUUG_vnL4m9iiYntORUbJNmoklvX-wAnvbgmOCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ece16841.mp4?token=GokGvW-bZ7cqZyBcEKSGkGXYvy3BavgL29oqacy6VulXGoFwh5KiymuL12NDHLN2atatr2d8qdyYnjMoswkA-AZ33A2VwgaZaxgaZxH-c3u9LxaM01PGOx6gysKkiOwqiY0gY5ekLHcjQhaVrNmxrAg2EqJNRYVKlE3hbpxEg1hE3OowXC1KtttSuw96KtX4QzSG4RAgk6o7jXHfFLkL_Z9p8k7fS6dqWxayTqVhTCrGzOYlLHtU-m6a4ECZnnx1AHg6AWEyfRAp4zI7BZfZNGaA3lid1y8KnD8VqgRYYQZw6maUUG_vnL4m9iiYntORUbJNmoklvX-wAnvbgmOCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مراد ویسی:
جمهوری‌اسلامی سربه‌سر اسرائیل نمی‌ذاره، چون می‌دونه اونا نمیان "نفت‌کش" بزنن.
اونا میان "نعش‌کش" راه می‌ندازن
.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71362" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71360">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBtC34mpGmiSxrADZdiCRA7mlUCVprzJhM0v5MdCyhQJR077Y67jlCo2TiC1zj9UaFIHKSYm_XAKc6C5mXHytuw3sxtEQDgaAxPyJXsepDi52XveqQQilP6EI0sfC6KW-UC8hbBqftH0COTD5gNdPQNs9rvcABZ-CKW_eC8pouCrUh6EeKctjjPVkCXARaHr3AUSVm-GdcFD7RldCwQimjLvjO9kvclVmLKViZYglQ_aehhEIX7rXP8146mmZkVS5ihnBi97J5dOZWYgo-QRRJD_PngKwCaBpWIf7tHA7kmu_wLnbl9BpD9N5vWfbymnuFoW6MqeaUfVg69_Dfcn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=n0y5XY5huycwFlZz9behA351PAyWqbWGRiMSGVXFnYccN0Et3fTSdveCO3DdhzlwQTnZ3BUYNczRQKsFMxkuNpJfYAamKirJG8fBSS-HdOGMwsikMt4XZfCzqBC_MghBHPNASNmm7_GjyBXCblJGrjqt1YkPPXgZiQpAyD4P85EuuYWpU0ihoRaibXsHmIsXDZ8xAC6rzh7UPAJUqRyW3mhd6j4T-E0LrLSnwcuYdFXuohWNmdBg1fXGiq_oPSleBfSgsJ5txFe4g9D8nSMLl_mvmER4CfCu2OI77_E6zy4CAe0-xXsMrVJf31KbcYjVfrBv-PLXSAUb7th2gSOX2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=n0y5XY5huycwFlZz9behA351PAyWqbWGRiMSGVXFnYccN0Et3fTSdveCO3DdhzlwQTnZ3BUYNczRQKsFMxkuNpJfYAamKirJG8fBSS-HdOGMwsikMt4XZfCzqBC_MghBHPNASNmm7_GjyBXCblJGrjqt1YkPPXgZiQpAyD4P85EuuYWpU0ihoRaibXsHmIsXDZ8xAC6rzh7UPAJUqRyW3mhd6j4T-E0LrLSnwcuYdFXuohWNmdBg1fXGiq_oPSleBfSgsJ5txFe4g9D8nSMLl_mvmER4CfCu2OI77_E6zy4CAe0-xXsMrVJf31KbcYjVfrBv-PLXSAUb7th2gSOX2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⛈
⚡️
ویدیویی که یک هموطن ساکن مازندران از وضعیت چند شب پیش آسمون مازندران منتشر کرده و نوشته؛
تو تاریخ مازندران چنین رعدوبرقی که بی‌وقفه ۳ساعت بزنه نداشتیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/71360" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkMRUfCZ0NjpH3ZHmpJcesmPf4lzqkGaGmB_kUMuzYBXT8NvmmPccQJl91Rj2JzAca89OoCvWhTcRtfLL6TyIVDrhjGZUZtvBDOiS1HdXc3lKPWBDuBJFIX-fEg7uFGhe4x2s8-OJ9Tn94aXyxgI3txEpwtVJ6I0hTCAO0YMmTPWlkKE34CUEuDGyPr7aM2gK4e9lHx-5S9sOaYqkTrTWR434YwSULc2mMBHGfGnH9kX5qoMLHOKGVGbLJnlcLzrPPMt_P3RCAoktrId7amkiTFKBXBxb5L_xCqQG0Kjjk9tEMS5nAckcdYySoZzsAFunOZVf8UlEaOo5uHUmKjbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
🇺🇸
#فوری
؛سخنگوی سپاه پاسداران شروط جدیدی را برای پایان دادن به جنگ مطرح کرد؛
🔴
اگر دشمن خواهان پایان این وضعیت است؛
۱_ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد
۲_ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند
۳_محاصرهٔ یمن پایان یابد
۴_۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۵_از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=sj7q-8T-H8ImwmqpYqZAlD32Q2ALTSFdrKFHOM8WUJZjzHKEQdXFS8Ok53ySHWn8X4OaC7FSGqtjlhshvgB0lpd5oCRQrUFbqUbOuBVnzD4VD2X4uWahxw-Jj_UazU6mlTsdq-G4F-6sqaJrT-q_3V4M6fWsjH8l61Pj5yXvJo-YyvdLZNvR8EktzMG5sW-M5eFQHzQS2Tj7fR_jTbz7OguNm-omXByAbthpAUGGOwdrVfkNRSU5IMAVtEaV97h61a2vIYtFHC-ItMFKIMVcyPFUkZUA0xWt1TxrKoFQxrIuHIn3L4gfx5JL4-fQwuWdTW8KfdANlmeKh44PZJ2YNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=sj7q-8T-H8ImwmqpYqZAlD32Q2ALTSFdrKFHOM8WUJZjzHKEQdXFS8Ok53ySHWn8X4OaC7FSGqtjlhshvgB0lpd5oCRQrUFbqUbOuBVnzD4VD2X4uWahxw-Jj_UazU6mlTsdq-G4F-6sqaJrT-q_3V4M6fWsjH8l61Pj5yXvJo-YyvdLZNvR8EktzMG5sW-M5eFQHzQS2Tj7fR_jTbz7OguNm-omXByAbthpAUGGOwdrVfkNRSU5IMAVtEaV97h61a2vIYtFHC-ItMFKIMVcyPFUkZUA0xWt1TxrKoFQxrIuHIn3L4gfx5JL4-fQwuWdTW8KfdANlmeKh44PZJ2YNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcr65FOwbCxhzQVRrAcmP_0IOd8HTk5KfWwe7ohcHFZDiBib5ehqzNlhSqZCgc25jgex4iFVuIvgZlLonv_nNSqrSElD38AwCESofdqZE0n_pwTmPZJrWS3so3Y0Gv9e01BpQrdHwrSpv_lhCSEsZCvwjHet9KDHWbMwtt828YyJcMlA7hb3G6KUkUEfVcYng9UmY-YPuP4T6G8IY_B2yQk4tS0IimHESO6iRknIFzmIWtZrBu2xO6bhxIvOsDCuUGmP8xv9oBhTLv2lqHgM5u26MLPhjUPBPHy-DP2EZSD4QcSfJg78wdZ0LIMqL4TVtHEvd9j9nExWsUUlAKyUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71356">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSdfg8Qu9dSXOwWqX3AVZfo3crxjIvhn8afjoW_l7uHJuBn4daj1c82xef_d7D8YVjew5v5qnAAfMliK4Rqez9LD--slCQKajxMtruSbffem_sIPIdQv8VsDdJNw-uywpR2vStjuoXPZHugmNLEYv60MtwKsUmzNQooi1PenjrPXiNoVZ6pcvonQ71b2cJDiKFDvJaB3EoPaTqxosshXUtbBp1CnQ1LOKeAs1ddB_HjZbDd8BpH4WgBSgxglmMatDkqZuTChs70BU9Bb_X8LLRFPKuBZTCLrYyTDwJwQ0FbhjXqLJMzhxlOSeOMTr2G8pZ7YSQCqtFCz2WDqjv3oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
🫵
دقایقی پیش دلار و تتر به شکل عجیبی تا 241,000 تومن بالا رفت و دوباره برگشت و الان 234,000 تومن هستش...
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71356" target="_blank">📅 13:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71355">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7Lh59d7Su-5iqq_Feit-_dCQvSkzY7IT02pGP10ww20yzjefM6qb68RP3yHh9B4cISbb7rGNpBJnWU7j2s2c4jkPD_bIMyOeIdbWCtit9xjVOgU8yoTNnMCcbNMYUrQI1fSHXIClPm8WD5MxFW-lT-0ilRfSuy6xW4l_M_DWVkltxeeOwGYiwe5vmmGZelJdGfi-VhDWzp6i9HjFwK1LxWwZCGqYyA1aVEYL_Gywl8Vj3BOi-S2RUcTHRg0uSaF34_xk4b4p2Ae1ylr62izOMtGE-z0AU28_3PYOV9V3gHQoJVMakclsub-S0Bn0nD7UYH4s4nwVE-eqB2xU4s6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که به دو ناوشکن نیروی دریایی ایالات متحده در خاورمیانه حمله کرده‌اند. این ادعا کاملاً نادرست است.
✔️
واقعیت: هیچ‌یک از شناورهای جنگی نیروی دریایی ایالات متحده مورد اصابت قرار نگرفته‌اند؛ تمام تلاش‌های سپاه برای انجام حمله با شکست مواجه شده است.
در همین حال، نیروهای آمریکایی تنها در هفته گذشته موفق به انهدام ۱۰ نفتکش ایرانی شده‌اند. این شناورها بخشی از یک شبکه پنهانِ چند میلیارد دلاری بودند که بودجه سپاه را تأمین می‌کند و ایران قادر به محافظت از آن‌ها نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71355" target="_blank">📅 13:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71354">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=X2SAkz7F-lUPBnmgNFqMc_vXLW-lfoBN-N2JUtmrG-We3zXX77ru80SSZkRK5zyDQt5DsByjxlos0vspRDilgjnvXRn8El_vrzlviQF_zNXm2o83KXElNbvDHsSv54-tMPpmwUsLolpLFBIYmT2ZiGvJ17cidY7b6SDgZURua6wztIbUxqRIdh5R8ZoMEo26FVRAektYcarnyyNaND2Hh4m4EhMkLxVFw1O1hlQw__H36rEBlkVv9VzoFe5N1BdLvRH8XdsLKHcg0mRZvR70CyigeA5zDps1gqijjxhcQO-AL-HnfL894Xl1NBjFxFXw_9D-ioZzLWUGmT4HWND4vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=X2SAkz7F-lUPBnmgNFqMc_vXLW-lfoBN-N2JUtmrG-We3zXX77ru80SSZkRK5zyDQt5DsByjxlos0vspRDilgjnvXRn8El_vrzlviQF_zNXm2o83KXElNbvDHsSv54-tMPpmwUsLolpLFBIYmT2ZiGvJ17cidY7b6SDgZURua6wztIbUxqRIdh5R8ZoMEo26FVRAektYcarnyyNaND2Hh4m4EhMkLxVFw1O1hlQw__H36rEBlkVv9VzoFe5N1BdLvRH8XdsLKHcg0mRZvR70CyigeA5zDps1gqijjxhcQO-AL-HnfL894Xl1NBjFxFXw_9D-ioZzLWUGmT4HWND4vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
پرسنل نظامی جمهوری اسلامی:
رفتم یه شونه تخم‌مرغ رو گرفتم با یک کیلو میوه شده یه میلیون تومن. حالا نمی‌دونم بیست‌وشش و خورده‌ای هم دریافتیمه.
مثلاً بیست هفت هشت تومن سر ماه به ماه میدن به ما. مردم چکار کنن؟ خب دیگه یارو میاد بیرون حق داره اعتراض کنه دیگه. به جز این که اصلاً راهی نیست. بعد هزاری انگ هم می‌چسبونن که آقا یارو تروریسته، فلانه، بسانه.
مرد حسابی مردم گرسنه‌اند. خودتو زدی به اون راه. من با این لباس دیگه قشنگ با این لباس نیروی انتظامی ناراضیم. وای به حال مردم. یعنی قشنگ میری بیرون خشم و نفرتو تو چهره مردم می‌بینی.
می‌خوان جرت بدن منتها نمیتونن. یعنی همین الان میری بیرون اصن یه جوری‌ان نگاه نفرت‌انگیزشون نسبت به این لباس قشنگ معلومه.
حالا یه عده خودشونو به خواب خیال زدن. بابا دیگه خجالت بکشین. بی‌شرفی یه حدی داره. مثلاً انقدر. شما دیگه رسیدین به اون سقف. یه کم خجالت بکشین. یعنی اصلاً من نیروی ناراضی‌ام. وای به حال مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71354" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jciHwHbu0mjZ1DU61jWT25o0fPAdkqbbXtUJyMcaAzNEGvss-fpWpCGOztBfWhDAoqQQ1e4KpDvEhl2Xrg6tkt8LWvYa8UW-lxjteDs25OZxyphMeD2NldqKHFcwqjtejSHchZ8NcBnOtoMpnQgdoHylvHXicEQa_VTZWY3wVDhlGPEQ8-vRtKeDEEmxk8TWLzLvM8FD8VlaUmZCTncq3FypIiUsXgSfqBAo-LicBxI17DHwMu_EttpKx4nv-X75xFvYVwbIW7mrlmwSNANfNcsk72kztiiNiDDoudnhC-_tWu99HlYfU6mM-pYWdGhP1u06o3PcPvqUxwoy9oIXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی از یک طرف ثالث درباره وقوع حادثه‌ای در فاصله ۲۴ مایل دریایی شمال غربی بندر راشد در امارات متحده عربی دریافت کرده است.
فرمانده یک نفتکش گزارش داده است که شناوری را در وضعیت مایل (کج‌شدگی) در حالت لنگر‌اندازی مشاهده کرده است؛ وضعیتی که احتمالاً نشان‌دهنده ورود آب به داخل شناور در پی اصابت پرتابه‌ای ناشناس است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71353" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71352">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/71352" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71351">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QonBR4P7GQXmXbedtdRwnFl11-KTBpv0k0fxaOYta_FdzQFtU0G0G47ljNC-wWps5Ng0EdGPZf4cEMB0HXATG89hCEWphyxhmPtL9SZqv4MVcJ6WDrReRp4I7VqRYpi3J-4G7bvepeR1Jdgp7zs-9I9Ksoi9v5XK3rx3epGCJyGT_6PyPd93Lq_s7IZ231rIW74haUbSUIHFrJm_9fYxltsLbIyx1kowfiZ2LGRfBM4VEnHMAjz0WL1Zi19pNndPYRKIA5GE3Vs4500GYHsSvX6jlGW8iDqrLorG01MEcoOTcrhz4iFxATwr_AieXFpL2C8RGX_eXcJwekQwwGVvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71351" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71350">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5Ady4c7H3JQbgOZ_Kk_WptbtRepiRj2bOnixZSoyPtdcOJZXDpbzEVNAYA-Y9StHrTGfrGpL2z3ScWrB1Rdh0YRMZ1f7clKtfueSgJeSDgifvPNoAe4s39Muc8YyYkiIt6JDPqJGAdrpHJNOpuKkiAXAHkdRdP5tWb6zPmxEhkp6E5YcSrA5LI5zvhoR3mzcMA4uJxEFVIg96w3q8iPahlgbNqv3lt6r4gyHSP1IO2dC0w9kEi-z2HUUxOrvmA-_mhjgrtPo1izASTo_otX-647PVnDGiC74c52Sraz7YIiPeqpep6uFKhN1AJSzgROK8WavIWHl6BU6mL2F09HwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📈
قیمت نفت خام برنت برای نخستین بار از ماه ژوئیه، به بالای ۱۰۰ دلار در هر بشکه جهش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71350" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkjZALUia6ZUowUskeP6uhHjD1bRqg5sPwwMKkVS1UcjXLEU9CWPV_TrKt2dDLyaa2Y-R99-wqC1Vm1qU26rLfpYKfmHLmS0uLfVsJ71bczNrYnxzdBGPUdf1NmygPudj_HVUfz4X8Zn1KDzovtO4m03z38X_BNFdGFVYbY-mDIyzRYp7dzmkFwf9Mx-aw21qQqdfyHZNXfjypBjs8QbqeZwLc1AA2souHtQlSl-DFuLPLN7lz2AZ6D75DbgcGV1JYQeefWryM30QfbIHecCjq6CbhJ5gqkZzKOAYgqfM-LrvYgDYmNBvL7DRG2lyXXgRMWOtXp_NQ5LTR_4zwIsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=BqakshGfk6PwR24r41352a5UeMj_2Fe3udGo_Tc1UlNluer4G8BHWQqY9HgiYOh50WwDZHHPyDy1bK6sGNct5zdOgK5b6KDhh9aJM8Ln942jZaIYAS8JPv_rkpeA6m9XtULfRX59USMzO_ywXol8BxVEDzZx5dWkm_0ol99AS9gvsDZLf_VAIqKLVJn9rOu63rHXe5NtJv3fUyrrrG8YAxPQdcab1BEgMVVGHhiRpW06GdDXwdjLbiyu5loZ8h0vLtYPiszmA9J_vKBjWDsXLLOfYfITSQmE4YnPFSQ08NfWsanEEGGs2PZiChx_wyEwRP5djdb2iFzvhKYvBa2CrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=BqakshGfk6PwR24r41352a5UeMj_2Fe3udGo_Tc1UlNluer4G8BHWQqY9HgiYOh50WwDZHHPyDy1bK6sGNct5zdOgK5b6KDhh9aJM8Ln942jZaIYAS8JPv_rkpeA6m9XtULfRX59USMzO_ywXol8BxVEDzZx5dWkm_0ol99AS9gvsDZLf_VAIqKLVJn9rOu63rHXe5NtJv3fUyrrrG8YAxPQdcab1BEgMVVGHhiRpW06GdDXwdjLbiyu5loZ8h0vLtYPiszmA9J_vKBjWDsXLLOfYfITSQmE4YnPFSQ08NfWsanEEGGs2PZiChx_wyEwRP5djdb2iFzvhKYvBa2CrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دختر یکی از پشم ریزون ترین خودکشی هارو داشته:
دو روز پیش "پایال دِوی" داشت اولین فتوشاتشو برای یک مجله تو حرفه‌ی مدلینگش انجام میداد که یهو وسط عکس برداری تصمیم میگیره بی دلیل خودش رو تو رودخونه پرت کنه.
ویدیوش خیلی عجیبه و بعضیا میگن امکان نداره این خودکشی بوده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71348" target="_blank">📅 12:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71347">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032667483d.mp4?token=p9bbBEkzdQyKC9WMgFoMe5pc1P6003pl4LjmjDtP55E-VhZqvWTm8q7Lu-Z67i5EqQWSx7lvk26nvrQ1TmM1XyOviZ4u4ubslgIq2oeSX9FQMarF-PRdhrtvmB_WLZ9Q7T0BQLR__61OeZznBOZEoDTHL3c1TwEoZrladf8skFX5g1DxYEfR6ymJH0SYoriHE7Y32CYbJacJNI4fOoZplF9iKIunuNI79206oVwT7B1rWE9gUAQrGL_UJ7t4NMYBO9rmQEp_VQHlhdgFe9li24yCx1xjk6Bz4C0khYlAmiZsf-FagrXA7rUvp8mSnHFuOAiQd9xitsb1TdgT-loVGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032667483d.mp4?token=p9bbBEkzdQyKC9WMgFoMe5pc1P6003pl4LjmjDtP55E-VhZqvWTm8q7Lu-Z67i5EqQWSx7lvk26nvrQ1TmM1XyOviZ4u4ubslgIq2oeSX9FQMarF-PRdhrtvmB_WLZ9Q7T0BQLR__61OeZznBOZEoDTHL3c1TwEoZrladf8skFX5g1DxYEfR6ymJH0SYoriHE7Y32CYbJacJNI4fOoZplF9iKIunuNI79206oVwT7B1rWE9gUAQrGL_UJ7t4NMYBO9rmQEp_VQHlhdgFe9li24yCx1xjk6Bz4C0khYlAmiZsf-FagrXA7rUvp8mSnHFuOAiQd9xitsb1TdgT-loVGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا طبق فتوای جدید حضور نداشتن تو اجتماعات شبانه، غضب الهی رو در پی خواهد داشت و تو زندگیتون ذلت و خواری میاره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71347" target="_blank">📅 11:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71346">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhMxEOb8mzaKNll-38wZIi0jlOYJLgKPo1eB8V1tN_I5XIxhagzoV6rD5sOafqewupset-ieVH2di9B2Cl-bq-OgpVXgRMMLOcG7Q7KF5uVnweMLdZb1toMPmkLYo3Au2K46skuZBjuC99I3vNn9QiH4e3u4fyJU0gOByppRbS3CppQlY2cbJa3f_KlEx9m2M4CUHyOoKfcNiNMXyJpgS3rL_4hYKlyM2gJLOZuFloMSauLKodSnTjrW4eDq3IDXOJBNxtdL0ipSmdNOI_ZOXNzeM3Q6sNVSZ_0jj7WProxN_qOOT25EfstPiWfNXYmsu-zFsOdztpS63kPbmnYHvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
دوازده کشور با صدور بیانیه‌ای مشترک، ممنوعیت‌های ملی تجارت کالا از شهرک‌های غیرقانونی اسرائیل را اعلام کردند؛
🇫🇷
فرانسه
🇬🇧
بریتانیا
🇨🇦
کانادا
🇩🇰
دانمارک
🇪🇸
اسپانیا
🇫🇮
فنلاند
🇮🇪
ایرلند
🇮🇸
ایسلند
🇳🇴
نروژ
🇵🇱
لهستان
🇵🇹
پرتغال
🇸🇪
سوئد
مکرون، نخست وزیر بریتانیا برنهام، و نخست وزیر کانادا، کارنی، توافق کردند که وضعیت با خشونت «بی‌سابقه» شهرک‌نشینان و گسترش شهرک‌سازی رو به وخامت است و به طور خاص پروژه E1 را «غیرقابل قبول» خواندند.
آنها از اقداماتی که قبلاً توسط ایرلند، اسپانیا، هلند، نروژ و بلژیک انجام شده است، تقدیر می‌کنند.
این بیانیه از اسرائیل می‌خواهد که فوراً گسترش شهرک‌سازی را متوقف کند، شهرک‌نشینان خشونت‌طلب را پاسخگو قرار دهد و اتهامات علیه نیروهای اسرائیلی را بررسی کند.
آنها «قاطعانه با هرگونه اقدامی که منجر به الحاق سرزمین‌های فلسطینی یا آوارگی اجباری شود، مخالفند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71346" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71345">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf294068.mp4?token=Q5ioMJBhHuLuxjcO9zYqRjhkE4Hc05Anajp7AvLdVvZgKrxu3ulHhFX5GB0A_MuaZrHGaVeIYYcOfEYtyAPsBBKt9rqDA66w2fjUXexOmLoB37NBb1qgSg-A4672Bmxfd36S8Laua83H1MvPTSfMt9pSdzje-wJIqbgiIzGLN1zzOU82OYyCIzJgtUErF3eOcCp54j93fHXkdMJvi1RLjmKrhQaaslo1O8xRw_vkmvThnAXDDAmKg2A9bJ-Jjdm73cIDQUfPry5pEsshgKTzXewwMWyJVCJyZrmaxjhedR8HkNROHddiab45wEiZqjJC7ks_cTS5_r2AlDHv7_Ti9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf294068.mp4?token=Q5ioMJBhHuLuxjcO9zYqRjhkE4Hc05Anajp7AvLdVvZgKrxu3ulHhFX5GB0A_MuaZrHGaVeIYYcOfEYtyAPsBBKt9rqDA66w2fjUXexOmLoB37NBb1qgSg-A4672Bmxfd36S8Laua83H1MvPTSfMt9pSdzje-wJIqbgiIzGLN1zzOU82OYyCIzJgtUErF3eOcCp54j93fHXkdMJvi1RLjmKrhQaaslo1O8xRw_vkmvThnAXDDAmKg2A9bJ-Jjdm73cIDQUfPry5pEsshgKTzXewwMWyJVCJyZrmaxjhedR8HkNROHddiab45wEiZqjJC7ks_cTS5_r2AlDHv7_Ti9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
سنتکام:
کشتی «ریسکو» (M/T Riesco) در تاریخ ۸ سپتامبر در خلیج عمان غرق شد؛ این کشتی پس از تلاش سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی ایالات متحده، توسط نیروهای سنتکام (CENTCOM) منهدم شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71345" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71344">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=iUYcZMjWWGjRY6cN2E3eatFKbNzwEuh5aq7pZotY7DucajXZTr78558iA3uQ_3s7tdK3nPjJIMqkJT7K1nb2_tPCJEeSr2LYql6_K4lEmLVkeuynzWKS6jN4ykdiibbtIpoY7pLFjnX2HA82lAW0vXjYa5Zbm_P9z6Q4jnJVA1bQOQFn1F7xIvsUarPL4yLtiChrHuHBrYMKXM3el8J45E6OmUI8COglGXzUbztkDtJmoCmXOFu2FjxuCe8z2236jqqoLy6Osh19x6p-ApZH5khKZrFUT9zfhkFEE2qOZAtKKWKMUX1g2Qt0F8ns7BAFeOo_zWNczzninFGEYz1a9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=iUYcZMjWWGjRY6cN2E3eatFKbNzwEuh5aq7pZotY7DucajXZTr78558iA3uQ_3s7tdK3nPjJIMqkJT7K1nb2_tPCJEeSr2LYql6_K4lEmLVkeuynzWKS6jN4ykdiibbtIpoY7pLFjnX2HA82lAW0vXjYa5Zbm_P9z6Q4jnJVA1bQOQFn1F7xIvsUarPL4yLtiChrHuHBrYMKXM3el8J45E6OmUI8COglGXzUbztkDtJmoCmXOFu2FjxuCe8z2236jqqoLy6Osh19x6p-ApZH5khKZrFUT9zfhkFEE2qOZAtKKWKMUX1g2Qt0F8ns7BAFeOo_zWNczzninFGEYz1a9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
مهران رجبی:
اونی که نمیاد تجمعات باید بهش بگی فازت چیه که نمیای ؟
این وظیفه ملی و دینی ماست و باید بیایم کف خیابون
ضرر نداره بیایم و شما کاری میکنید که کفار ناراحت میشه پس بیاید
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71344" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71343">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=C5USEFskEDUPKo_bm-WXfNjsy_yFxTstEAuRJnC0qIipSW9Kby8-rzCYPNC1tzx19wTSOK4Bm3SVDaDzOQCUlcp7zym7PnHu4zZkFBwMnbNQjfJHvN6LniLUzH4tDUcPun0XqJ77lWAaQSSEFHSf5rikyfQxJQXoqJ54llrxwziMcmSWieXQQPR8CQOJ_jKJdVmy38TaVd_IoPwXqnNBklNRhe2jSSEa6Qzqi2C-MoEvb4RLb6PJq4LtB2hHGZ9mR6Ea1Yj4iheYIyVNrSGBMu-z6WgHsPI-ubmHHXlbr45k-Ue2hDABufzR4iJ0BEhjre9c5Jwp6-H_AlMq8aSRmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=C5USEFskEDUPKo_bm-WXfNjsy_yFxTstEAuRJnC0qIipSW9Kby8-rzCYPNC1tzx19wTSOK4Bm3SVDaDzOQCUlcp7zym7PnHu4zZkFBwMnbNQjfJHvN6LniLUzH4tDUcPun0XqJ77lWAaQSSEFHSf5rikyfQxJQXoqJ54llrxwziMcmSWieXQQPR8CQOJ_jKJdVmy38TaVd_IoPwXqnNBklNRhe2jSSEa6Qzqi2C-MoEvb4RLb6PJq4LtB2hHGZ9mR6Ea1Yj4iheYIyVNrSGBMu-z6WgHsPI-ubmHHXlbr45k-Ue2hDABufzR4iJ0BEhjre9c5Jwp6-H_AlMq8aSRmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از طویله مجلس
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71343" target="_blank">📅 09:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71338">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gv1YBgJMLhclOyuDsz55CcaK8wf1-eYffpnFeT2zMmaKyNd3hKzTO45qQGe6TgAxJi9H8gNsN2_7NHtSQNxSIZRmMYwAZ0wRqwx8DQql0_9GwSUyUVgwUENAYNyhP0O9KgoX8RASqecnWpIwf_sL1IoIb8rbZftpmmez2TVc_RFaEcXjhsjKy2bsSVe3ZfJLNcAZjsvut--KWBhbyL2tcsn2OBn4pwJ3Np0oLxxF6yBmgdGbfTCzGcLZ4veAdi3dMf1c9eKLRmDbtn1FvCRWM9bZFMoGEK9_ZwgIJn_VsGAe4QGZ2hF4jd9gn-ukLPb-XG4jhtLpv2AGbGZAl_WSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKTf5QWMu-PbG2i6Ja2Yf8wQfTq9SxKR7dt8kstYASx6c-SNTJkChqM7kvCIUppAlKUDBaktTwS9glybdLSuDtfjC-TC43-7-sAjBKfgi4cM2_eWcqy6RYTmy96f3LgCW9hv2Txn3X-bEQfYlEON3cFjb6mJfJrQy_RwJD4letQgKizEhma_yY8DMHkKaRoTRE971u79sfTHbhR-myY6M0J3-a9H6kz-Jhj7__4DLTznLvXEiZXAzxh8GmRV-NLNymKGw_JnurtbWhxNJrfboH__p9Bx7aNEd8E9Ek2TuEIhVyEOOeEDe97hpKa6vHldhXQhj77mmCHo2RKhS6F6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BoJvK-dMyxGQOVVL8pkzFHPaRqMkoqw2-5pOYDTifQBqv-lhHUTxM5DT8-qgoLGN0qYj4CrPTM4Wp1eIbLAHk_veSbfrh3wKD20TjitH0g_FGcvDMwZwj_I-1eYFUQGqOXDD8ydGjwyTV-pZm0iGG5K08AaClXSHxCf-Uo5V1oa226lnaW2KRQv9LK1VBkyMHYBfTe6n1lqSqvBLg3MgLT4WmwEhtK4elyrvCtfRAzyhEEslrd1SIVjQ6yBWO3WCrGqidsOeHfBUlwuX2Ceh2rAVse1fq2rGMv_VfzO9PNV0I0OjCzBaQjjRZmNyxVej2FvdfrOsgW6bIWeDazpoDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDZWP9RgZXtrTdaM42Ow3gq88boM330LbCFZO-THvTXe4japXQDeHZCQ1IragfziNFkbjS1Tdt4eV2MhJcKXVfctDqu1dWRGCin2eqXxgs0ltEIdHE8tN-okLlolfu_D0qJAVV2URrokV2uUGPBHoNr6WDVZUPVsN7Nn4h5D1W0pGks2cfmc7vWcDxO41f-hj1txzYdlYIF-DgcWLrSKYxnodBOskzbYxquiLf8hSxnvufPPzly_ElcWm0Vy6vZqA_bwrUN8WTGCFBs3VXMP8L2GKJx4jQGhemFrH_c0FI5SM2Uugh3WxxnTCCmOs7e8HHQwDVAGs3YjxGGZjw5y-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzvCsm2kq9jBWh3Mh0TGPrnPmrrISRYpszN2I3pl1-yUdgI6Hegjr23zX2Cqvfm6guGQaBuYqdoTlS9G3GUYNNKOxzcLjIdtL6AVj8O1ndDVr8DU5fSgH2kHuqsvRIXzOTexLcTnc8UqjbLrBeTOc7XMQhQDMzy9Mv_zYYWhGFg1B6MW7V0eeYF1vHuvUjVzKmlEP6bofVahXteUX4aZxGr0O2ARvVSqB8gq8gFh4gEAiSYjf-YpBqhpouLMFNx9XE6vOaEzK8ROxOdDY_VngmrxdywwNkHNW1GRtSiVnYmoKY9K23s6FOaVjImx6_KGyyTTkMr3q6I4jPcAYgEelg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه پاسداران تصاویری از زیردریایی‌ بدون سرنشین آمریکایی که به عنوان غنیمت گرفته منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71338" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71337">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71337" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71336">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdyWZSZQh_x4yr30siG58ryRi2vv-GqnbB-JcFf9eeWKh2tRVDB4VsaMH7-y6riFmJf75WfWkrUbEQEQiR2xk9_GVlGHmTD8LxNtUarIw1mqIZoJPRj42h4RpGr1n3T1sFpngC7vHShEWw-cuOwpQlv6pSsWfezFUMNNYui1IzVN47WhwF_TA2Vt1vc9usBUWhdl57rOWoeeOAGvkG-LJEMtGJKaxLg9fr_mEBsOhyWdrW8rYWPTrWsFSuQqIDo2fEZwtyCw1KAsK7pWU0dQM6Otv8S_c6FAA8Rq3X2RItWmvy04g2pAUp43Oflf2DJCEp7sA4W8bLNcWyomYxoTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71336" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71335">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
〰️
#فوری
؛سنتکام:
نیروهای سنتکام در تاریخ ۸ سپتامبر پنج شناور حمل نفت خام ایران را منهدم کردند؛ این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی طی دو روز گذشته، دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد.
کشتی جنگی آمریکا با موفقیت از حملات تلاش‌شدۀ ایران گریخت و به گشت‌زنی در آب‌های منطقه ادامه داد.
هیچ‌یک از پرسنل آمریکایی آسیب ندیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71335" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71332">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
📰
خبرنگار العربیه:
چندین موشک ایرانی در جنوب سوریه رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71332" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71331">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=dIuajY6Nlb96G4EODBlWmKtragLQ6qusfALC2K15V4ScqgLQ_lTPub_bMdLIDJ3plGQx_a4trm1w2xGUwvt1pH6CpOubA-du30_6vt5C6-VFOoY9mqt5cV3f3VDw8OK9h90TVNcuDPHoHvkpgGK-q0Sxm2S1sRzEccUoGlpiN70ZVaYUPn87hUiYv2ltXWP7_1S-craPYjOJ3osBt_MuCMJX0dhlQVcNaHiFAseMnqFhu7snI4j9lM4clrGkdUhQNQEVejboRPTuWGuEQzMKSts49Nw8FbT9XV3bux-d_EJbnEXF9BdoH44znGlXtcNBpf2xvCBQa7A-M81f7xtMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=dIuajY6Nlb96G4EODBlWmKtragLQ6qusfALC2K15V4ScqgLQ_lTPub_bMdLIDJ3plGQx_a4trm1w2xGUwvt1pH6CpOubA-du30_6vt5C6-VFOoY9mqt5cV3f3VDw8OK9h90TVNcuDPHoHvkpgGK-q0Sxm2S1sRzEccUoGlpiN70ZVaYUPn87hUiYv2ltXWP7_1S-craPYjOJ3osBt_MuCMJX0dhlQVcNaHiFAseMnqFhu7snI4j9lM4clrGkdUhQNQEVejboRPTuWGuEQzMKSts49Nw8FbT9XV3bux-d_EJbnEXF9BdoH44znGlXtcNBpf2xvCBQa7A-M81f7xtMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمون اردن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71331" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71330">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=rt2KFLTHWEGNb_aBOgCm6swzoieX_6nEOUsSq_tIx_PiKidMeQmhPUS47C8l6xdkLhhVLaKL9wxKuxBR12z7QZRAr3QAl2qKqZagLRsc7BFCT4ozz_s58FSw6x9Ls1aZTJUDQjMhBAijOE-e3GyngyiEGbOCRZDTOxhJgq-Z9qnxM8t5kTG2htugIsH2gdFMJYyKOUKJJkAd0HApaMKfoyIPj6YLr8_tKWTbOGKsnCrAHLPj0roOC_qNtmuOC1U2672cZNj4S1q_0uQh8d8Ny3_79m78RIS8aQ7WG9ti-dhisCjBrpMPmTPGMgJS-LZuH-brQybc2v-w06Ps9qgcIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=rt2KFLTHWEGNb_aBOgCm6swzoieX_6nEOUsSq_tIx_PiKidMeQmhPUS47C8l6xdkLhhVLaKL9wxKuxBR12z7QZRAr3QAl2qKqZagLRsc7BFCT4ozz_s58FSw6x9Ls1aZTJUDQjMhBAijOE-e3GyngyiEGbOCRZDTOxhJgq-Z9qnxM8t5kTG2htugIsH2gdFMJYyKOUKJJkAd0HApaMKfoyIPj6YLr8_tKWTbOGKsnCrAHLPj0roOC_qNtmuOC1U2672cZNj4S1q_0uQh8d8Ny3_79m78RIS8aQ7WG9ti-dhisCjBrpMPmTPGMgJS-LZuH-brQybc2v-w06Ps9qgcIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
مهمات خوشه ای سپاه در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71330" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71329">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇮🇷
نایا به نقل ازمنبع ایرانی:
سپاه پاسداران انقلاب اسلامی، دقایقی پیش، موشک‌های خیبرشکن را مورد استفاده قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71329" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71328">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=f1k6ya1Ih8TK3dOg2jieO0AWoLYEynZMAR_gS3Q7t6uXvXqasL-OAenqDdvBhOd8ndsmayou8okpslmK5C05EYlvmzuZ_SQkaERJpz2aR_fqM4WUnDOzVuZ0ni4Y1FmHVCAuRZ0gGNW13j6EQr1CdckhaBRLAlvxJNyfWK24itvvhDpuIi_-XhQtJU2aOyAoQDklgB6fJZWFRhGr4gxjd9bgAhn6l9x3-6mFXLjgrT5JaEryUTUenmytlpNPSwiVMj22VSKrIJlwvsNjnJuaEG9yidIf4plSsIbCQdI2fvnvrzHQQvk5HzMm4pdZ41rLicMPfiBcrOCR4G2GbsUFeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=f1k6ya1Ih8TK3dOg2jieO0AWoLYEynZMAR_gS3Q7t6uXvXqasL-OAenqDdvBhOd8ndsmayou8okpslmK5C05EYlvmzuZ_SQkaERJpz2aR_fqM4WUnDOzVuZ0ni4Y1FmHVCAuRZ0gGNW13j6EQr1CdckhaBRLAlvxJNyfWK24itvvhDpuIi_-XhQtJU2aOyAoQDklgB6fJZWFRhGr4gxjd9bgAhn6l9x3-6mFXLjgrT5JaEryUTUenmytlpNPSwiVMj22VSKrIJlwvsNjnJuaEG9yidIf4plSsIbCQdI2fvnvrzHQQvk5HzMm4pdZ41rLicMPfiBcrOCR4G2GbsUFeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گویا سپاه توی حملات امشبش از موشک خوشه ای استفاده کرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71328" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71327">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=M-5-arL2eQuxaGFsfRylXIiAkoJrG3NY1vM7fJHQZ6t9p0eRQFmAgoUQhJJ8ZDncwlSxIP9ZgoNrQC0ge-podBz8UNPmvoU_Vh13wKJj26-cmyYbpf_YOM4ZIjQLnrRcjknsoS7JvwBRVJZgypbB1Oml4xw7KX-n0Dg2lRR_1zyZjQbb8Qdf8Wn4JPRSnfmU-zSMcsskI4orOZcnIsSIhLo5ji4uxqKyKgoxIHLe2iYru_Um845DWZDD1KV6X7RwDOTadtQNa72KUYEAWe8cG8U8qMoHieFgPAxrpZJPZ2CFx4qL7n8UVxbv1NS3eseQWMXAxyT8NUezJ_9tpdr0Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=M-5-arL2eQuxaGFsfRylXIiAkoJrG3NY1vM7fJHQZ6t9p0eRQFmAgoUQhJJ8ZDncwlSxIP9ZgoNrQC0ge-podBz8UNPmvoU_Vh13wKJj26-cmyYbpf_YOM4ZIjQLnrRcjknsoS7JvwBRVJZgypbB1Oml4xw7KX-n0Dg2lRR_1zyZjQbb8Qdf8Wn4JPRSnfmU-zSMcsskI4orOZcnIsSIhLo5ji4uxqKyKgoxIHLe2iYru_Um845DWZDD1KV6X7RwDOTadtQNa72KUYEAWe8cG8U8qMoHieFgPAxrpZJPZ2CFx4qL7n8UVxbv1NS3eseQWMXAxyT8NUezJ_9tpdr0Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت شدید پدافند در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71327" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71326">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
از اکثر نقاط کشور به سمت پایگاه های آمریکا موشک شلیک کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71326" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71325">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=Jx0i6FcZ6URhWzLIxjffk1caJLl1omeA123Sk7ueCAddgfYOIXi-iP2-giR9TdEllmnMq3LmXgojPiFGL6sF7cnoCtvUX0VUFM4G3CmB8wLmIhlKjST2NN-hQd7ABOyhWe2D9wof0wD1SXQPLOMDP9q6GWpOqw_XnH34RpdWMmXzcu_vnucVQDwuZZEGR6N6POhausFAMMBU_Ejqd9KZoyzFp8q1Lx4ffThO1ViLl3V7u0a6-irmFdEvteBQK0SKglD10Awa-D0rftu2qEqZzj0d0kJ-sUXabFXLiYi_nW9EkO6tm8y5rPiyqnuajkp2V5elDHqlC4_q6cayjFbADQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=Jx0i6FcZ6URhWzLIxjffk1caJLl1omeA123Sk7ueCAddgfYOIXi-iP2-giR9TdEllmnMq3LmXgojPiFGL6sF7cnoCtvUX0VUFM4G3CmB8wLmIhlKjST2NN-hQd7ABOyhWe2D9wof0wD1SXQPLOMDP9q6GWpOqw_XnH34RpdWMmXzcu_vnucVQDwuZZEGR6N6POhausFAMMBU_Ejqd9KZoyzFp8q1Lx4ffThO1ViLl3V7u0a6-irmFdEvteBQK0SKglD10Awa-D0rftu2qEqZzj0d0kJ-sUXabFXLiYi_nW9EkO6tm8y5rPiyqnuajkp2V5elDHqlC4_q6cayjFbADQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موشک ها در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71325" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71324">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ارسالی از اصفهان:
از نجف آباد دوتا موشک از اصفهان ۴ تا
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71324" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71323">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=u_Adm060uHnyJFGJ3h4Ve09VmP70V1jH6nK-N05nlvj40F251n3-X2AJwG66J0017hSYx_B6_5LRvIgOr3DHJ4ytNjmbKw5n8McpUG5VNqsEKwbhsYrRI7j6UkfFylTdPshbT-4VwMqdIR2EGPyQjBaSAUJMMupCRwCKk8UKqk7takF0hwyLICg0nZT2-e_cs9yoj164F_iEWQpG3_2Fl6A6u5z-hMD8JcrphEaLEaa7Dmzg8QOKaMdhRdwYEkVpt9B72Zw1XnMv-nzMvTSDeBop-L-dsS9BF51Tflje-qIpbcltC9PnsaKzR3NHx61S9ZDpmD2kMmoooC43B-8CcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=u_Adm060uHnyJFGJ3h4Ve09VmP70V1jH6nK-N05nlvj40F251n3-X2AJwG66J0017hSYx_B6_5LRvIgOr3DHJ4ytNjmbKw5n8McpUG5VNqsEKwbhsYrRI7j6UkfFylTdPshbT-4VwMqdIR2EGPyQjBaSAUJMMupCRwCKk8UKqk7takF0hwyLICg0nZT2-e_cs9yoj164F_iEWQpG3_2Fl6A6u5z-hMD8JcrphEaLEaa7Dmzg8QOKaMdhRdwYEkVpt9B72Zw1XnMv-nzMvTSDeBop-L-dsS9BF51Tflje-qIpbcltC9PnsaKzR3NHx61S9ZDpmD2kMmoooC43B-8CcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71323" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71322">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
گزارش ارسالی:
از زنجانم موشک زدن همین ۱۰ دقیقه پیش
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71322" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71321">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6m8S672LJACrPYlSIeTzktDk0om53GyjjSyxXlg8qYiVf50X7CKcyqK_FAmN6RylLg3KkU9wRPDYj5pP5KYbu-mS6r4Sm1L-ABAAvkvW2JuCSA4_OQbfMTQx4SJ5KjaeMVUHjBedNnunL8gTw-Zm8v2YTzSmQa738sQFIZC2eayNomGDJfXM7O3-ZkTgPzAQSwhfOYBxaKhW534ikA1k6flRQMVTLdcnee5u8zf0L5nhQnoBeWEHLbq2-X6AtEBvTuNmEOdmADyNcZBHxgItMuIxdd7gumSzstDov8Z2AJqMANWsejvD-s1sBFb724L5qN2luyAni8BH4Bpe11K5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارسالی از نجف‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71321" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71320">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc98612785.mp4?token=l2t6oPD3sqEW5pZUlKPG_-IpzOyOJdQ0KeAxpKWO3ETL1sW6htijFsHSqMTy5iDA5vGq1z2KTLO9WmlBNlsPp4u53nV0vft8Jd-mO3r-vtlNB2N3uOYN0eVQeys-hqf8Py8J5xXiY6xRK9JUisqyh2ZDDoBba8BDKR3uSSVMyogjMigCx2BNIHPkXXkONHDZPM4cVTOdsQvDcmyTtyQ1YlpavaA3Sow4fbXdL5D9TIzPTG8bgv6283jZnzkydC1tggclyZtBzmkOMr8A46mqHRza35IIJ_GldiBr_YyRKNHkxMOsudbbYdxtN1jzeRJcisVQHJKP3Aht_4J12IS7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc98612785.mp4?token=l2t6oPD3sqEW5pZUlKPG_-IpzOyOJdQ0KeAxpKWO3ETL1sW6htijFsHSqMTy5iDA5vGq1z2KTLO9WmlBNlsPp4u53nV0vft8Jd-mO3r-vtlNB2N3uOYN0eVQeys-hqf8Py8J5xXiY6xRK9JUisqyh2ZDDoBba8BDKR3uSSVMyogjMigCx2BNIHPkXXkONHDZPM4cVTOdsQvDcmyTtyQ1YlpavaA3Sow4fbXdL5D9TIzPTG8bgv6283jZnzkydC1tggclyZtBzmkOMr8A46mqHRza35IIJ_GldiBr_YyRKNHkxMOsudbbYdxtN1jzeRJcisVQHJKP3Aht_4J12IS7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارسالی از اصفهان:
حداقل چهار/پنج موشک دیده میشه توی آسمون
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71320" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71319">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c50434db49.mp4?token=LFiUlmFza75rmcgvJ9SKIzQjx18b9KzdAjabzJUQWPpYB5llTYZI5QzAVA2Uhjr3sMZ_m4kd2gwW7m8L-m-uw7UTCaQKT7bLSx9OO5F9rqHGW-Af5Ki0QwZ1Xi-ytBKSULQF-bXKJrhUQYCEs6yLJbCsvqpJ2Lmj4y8DqBKQjKITrPxJu2kzDOJa5rHvcwRuq3x3bo4UsZWrDdVwWHYW0Y2ncgcJmFNqILusSvJxvtIfkFzhuJIYhK-JNlRLMwdJc5eHuBuL5eRocDv5jQaSL6hqBBSJK88bm-O_zXVU9vAR8YFTtcRHr3p6y0qpHUWSonYIQGt9cziIfqol0btjnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c50434db49.mp4?token=LFiUlmFza75rmcgvJ9SKIzQjx18b9KzdAjabzJUQWPpYB5llTYZI5QzAVA2Uhjr3sMZ_m4kd2gwW7m8L-m-uw7UTCaQKT7bLSx9OO5F9rqHGW-Af5Ki0QwZ1Xi-ytBKSULQF-bXKJrhUQYCEs6yLJbCsvqpJ2Lmj4y8DqBKQjKITrPxJu2kzDOJa5rHvcwRuq3x3bo4UsZWrDdVwWHYW0Y2ncgcJmFNqILusSvJxvtIfkFzhuJIYhK-JNlRLMwdJc5eHuBuL5eRocDv5jQaSL6hqBBSJK88bm-O_zXVU9vAR8YFTtcRHr3p6y0qpHUWSonYIQGt9cziIfqol0btjnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ارسالی:
همین الان از دماوند موشک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71319" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71318">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
ارسالی از تبریز:
همین الان از تبریز موشک زدن
سایت موشکی امند
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71318" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71317">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
چندین گزارش از خرم‌آباد اومد که صدای انفجار شنیدن./احتمالا پرتاب موشک
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71317" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71316">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ارسالی از بروجرد:
سلام بروجرد هم فرستاد
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71316" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71315">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
گزارش ارسالی از اصفهان:
هفت تیر مبارکه اصفهان موشک بلند شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71315" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71314">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTLl0wzul0hFGrleFCkaW7KpzbXJXw_DbfJ3JcT2Gc350rnnrtb9swOT-dcU17ZtnLmaZVVruGejOF5B-ihaPU-SICi3uHeIKOcJB_-23ykSNamIg9ETplQ1FhifuSzR68Kb0VQd_5A0XJAGvqx942le4Z_NuBPqOCPMmP-nU_V3-8bbx9DvaTOBPLoPxKsl4RFI_xkgn8gKuL8YdTRZ3gYOLrRwyilNvsmyT8rPIIQJITU_fCqhmiSGV-BgqSSWm-jyFZuPietJD3aDH9_krgZ0iBEL-Y14VvmHo_sZOvljgcfKR29o_3jrtQWSx3-jzgOhVVaDaRcNs6tAxYgwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71314" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71313">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
گزارش ارسالی از یزد:
از یزدم موشک زدن همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71313" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71312">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
گزارش از اصفهان:
اصفهان الان زدن موشک نمیدونم شهر رضا بود یا نجف اباد
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71312" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71311">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
گزارش ممبرا:
۱۵ خرداد اصفهان شلیک ۲ تا موشک همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71311" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71310">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛صداوسیما:
دقایقی قبل نیروهای آمریکایی به یک فروند شناور تجاری در آب‌های ساحلی شهرستان جاسک حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71310" target="_blank">📅 00:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71309">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0-17VA1bHWM0Q4j_7Wdpx0ge0bKHdCcBYyJNLL9xHmMpat1lTs6zLS3epOsDA1a2k8Rj3FazftmgyAmKMv8JzH_fNZJmcL0HAEWrWuVPtIS1i-_9jesBDQ36e6lA6WksyProq7875cvlL1XYxeaFjxrF9kyTpgRSVRcPvlsaN6Mrb88BhcyV8_LCFApNJ8McvVZWHgS0mEivw7xvJzfncG7qMNc5v_LxGer67au9Cjr90J-JzvLeSXujW8el_SWl5yMZxpJ1CgilOWUAwQwZtJY_MTMKkNzHcR42s1vLIUEWCSE76aaCYePurTliVDFrqsI0zjkOTz-zigbrkP7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:ایران ظرف سه روز، دومین موج حملات موشکی را علیه کشتی‌های نیروی دریایی آمریکا انجام داد، اما هیچ‌یک از شناورهای آمریکایی هدف قرار نگرفتند.
این حملات موجب نگرانی واشنگتن شده است، زیرا به نظر می‌رسد ایران از موشک‌های پیشرفته‌تری استفاده می‌کند که قادر به هدف قرار دادن کشتی‌های در حال حرکت هستند.
مقامات آمریکایی همچنین در حال بررسی این موضوع هستند که آیا چین یا روسیه ممکن است در شناسایی موقعیت ناوهای جنگی آمریکا به ایران کمک کنند یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71309" target="_blank">📅 00:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF53vdprmR62CBI6trHkYbBLtoJYS2C8gsjR2PYZcK29lxvx3g09Sc-ERMW16afyXHCCgSmrvQLU-eOQcViM6typ4d1_pxOXUB8YHVpm7IVZj4XJoligujlHXNk8EQzo6jbRaqbfL4pCC7-r9QBZW3kub33uhWtZlZ3B31GIikE_NMCFSmnfgzLa8BZcDFQLcyd7xlvyl6y0E7ccZu5GJ2bcctC_iIlx88_81ZBJUjGkbmFNX2bM0qOfmxLCIqBG4Isus5eLbVsokRKxz_tZR5diXrOMoXK1Uld3f8h3mWkkm2ZCczPhFPmILbkIpDHj8wj3tFC7vdQYNZdEWySPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
به تمامی خدمه نفت‌کش‌ها در بنادر و لنگرگاه‌های کویت و بحرین هشدار می‌دهیم که فوراً شناورهای خود را ترک کنند، زیرا این شناورها هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71308" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71307">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwF-az3rIW2VXdNZSiGDIabi2vDy6HjX4DUw5NTuBAQ_RjBboDWfaQf7vPaUrrA3MR6t02TZHsozpUwWVhykkoIQJe-GUj1a7nBqGH0Ei8_BfpxjcheFWCLEhbHKBjDLKKkNrm4WBTPcGqMoWxPFQqen1tZ2DpocK6AYrfTWl6J9zlN9RG7MAN0eeSpDy8OxxmRiJpgV6msyCrhNaJYjzh8f09mfUckYw6SrtYE4P7mFYXjX4JbLgE8s88rvox5rfX3lshHiIuZ7PvZgyiASFFOpFBBDXN2kgYOmOoP-CY96utW1FkXBRFW8JWL3Qe_laUl5iX_7ij6zm-aaTumcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
مصطفی نجف زاده:
آمریکا با هدف قرار دادن نفتکش‌ها در سواحل ایران و مشخصا خارک، علاوه بر اینکه می‌خواهد بازدارندگی معتبر در برابر رویکرد تهاجمی اخیر ایران در حمله به ناوگان دریایی آمریکا ایجاد کند، ممکن است گام تازه‌ای در راهبرد محاصره نیز باشد که براساس آن، قصد دارد حلقه فشار را از مسیرهای انتقال نفت به مبدأ حرکت نفتکش‌ها منتقل کند و صادرات انرژی ایران را از نقطه آغاز با اختلال جدی مواجه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71307" target="_blank">📅 23:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71306">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71306" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=nN75vp8ZSuSesHcKAc6_3SfhCyIyMoqlejP8MAZ2MAPVXOK0zuAIdrpPI_YI64MH60FJxGl1friOC_caWGs8evDuTpgYDccUuBFcECpd-V4AE8elC5T7tqC07E7P9IysIEJZzsHMrK8IhHTv50NXVfYNyzpRfCjl9pgHzkY930PuhcQMPoQ9ZE_4RUFjcRMpSSKDS_yW83k9q6aLBwEHImrnI3dVXiYaCbAVmUkj33mH2F-RYCHo1Wt7SzN1OBoEERVfCwda0kqmZF3LgIJrCM3jVk8dGtNJBgLZZ6rb4PfEn5dGsnC_L_qJuibRYoBc1UaCExi_yaLCShWOwXL4YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=nN75vp8ZSuSesHcKAc6_3SfhCyIyMoqlejP8MAZ2MAPVXOK0zuAIdrpPI_YI64MH60FJxGl1friOC_caWGs8evDuTpgYDccUuBFcECpd-V4AE8elC5T7tqC07E7P9IysIEJZzsHMrK8IhHTv50NXVfYNyzpRfCjl9pgHzkY930PuhcQMPoQ9ZE_4RUFjcRMpSSKDS_yW83k9q6aLBwEHImrnI3dVXiYaCbAVmUkj33mH2F-RYCHo1Wt7SzN1OBoEERVfCwda0kqmZF3LgIJrCM3jVk8dGtNJBgLZZ6rb4PfEn5dGsnC_L_qJuibRYoBc1UaCExi_yaLCShWOwXL4YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این فیلم‌ لحظه‌ای را نشان می‌دهند که هواپیمای باربری آمازون در روز یکشنبه در فرودگاه بین‌المللی میامی از باند فرود خارج شد و متاسفانه ۵ نفر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71305" target="_blank">📅 23:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71304">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=TaJvLXEZ_InGr66EI4fcEH4Gi9gZyNtNmdL77DkVRNF_XrKlwMO2-ood_eCt1ocSr6gU1sg3g2WC9nwTSiuT4fIXwOfn9Og-GAQY7T4ZYJkB_aSB5okvB2JUJEZc8PZQZSKoM1mgs3HZ_MR5Cpi2GVhyJybsPNEW-1f4lra1W0ndJtgycsPD66TBByiN9WyivCScjBbCQ6KKMbkBAhP29tSED4QLIknbA0X2ItSVYU9VgKC6zCGMpfxXDfu8qnUHkCDbzK_obKBP6J9Jd6pi7KeAA1KhldFDujhWScB_LfoDROuSGi3CEG9543ve7ES5637R38O_y47kyQGeoJv_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=TaJvLXEZ_InGr66EI4fcEH4Gi9gZyNtNmdL77DkVRNF_XrKlwMO2-ood_eCt1ocSr6gU1sg3g2WC9nwTSiuT4fIXwOfn9Og-GAQY7T4ZYJkB_aSB5okvB2JUJEZc8PZQZSKoM1mgs3HZ_MR5Cpi2GVhyJybsPNEW-1f4lra1W0ndJtgycsPD66TBByiN9WyivCScjBbCQ6KKMbkBAhP29tSED4QLIknbA0X2ItSVYU9VgKC6zCGMpfxXDfu8qnUHkCDbzK_obKBP6J9Jd6pi7KeAA1KhldFDujhWScB_LfoDROuSGi3CEG9543ve7ES5637R38O_y47kyQGeoJv_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آیت‌الله بی‌بی‌سی از لندن فرمودن بنزین(۱۰ هزار تومنی) در ایران تقریبا مجانیه. این دقیقا عین جمله‌ایه که آیت الله بی‌بی‌سی برای مردم ایران پخش کرد!
تا حالا شده بی‌بی‌سی فارسی حقوق کارگران در ایران رو هم به دلار حساب کنه و نتیجه بگیره مجانی کار می کنن؟!
یا تورم رو حساب کنه و مقایسش  کنه با حقوق کارگر؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71304" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71303">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=jLm0yuWjT8bO-Z8MWI74gIjmh28sb1haFYVvV_Pk0qxcFhsX0K9oWaQ_l2xWTmzGURsc4UgbAwERvuyCXrjVRbLHlF0qKxfxuaYjkWQA7nUKeDG0orur7yI9IiC9gSbIi2YixBRjyTqYJsxyOevSQFt-8tOjrRopxKL9kR7E8dLSvXo8muH9ZB-MhwmVFhblBRP2lyCe08gI5I327yYGxvXuevBpxa3fdx8YT1DgOVMy4uB1tcgu-niqEp3iGmfLx1cEmuNPSTCQPO-S6idELEkENhqzaVMF8A4hGkwVL-6bZU9GaFsmICyMQhrVHV99mO7tRJ_CoK0sRQdjzQEkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=jLm0yuWjT8bO-Z8MWI74gIjmh28sb1haFYVvV_Pk0qxcFhsX0K9oWaQ_l2xWTmzGURsc4UgbAwERvuyCXrjVRbLHlF0qKxfxuaYjkWQA7nUKeDG0orur7yI9IiC9gSbIi2YixBRjyTqYJsxyOevSQFt-8tOjrRopxKL9kR7E8dLSvXo8muH9ZB-MhwmVFhblBRP2lyCe08gI5I327yYGxvXuevBpxa3fdx8YT1DgOVMy4uB1tcgu-niqEp3iGmfLx1cEmuNPSTCQPO-S6idELEkENhqzaVMF8A4hGkwVL-6bZU9GaFsmICyMQhrVHV99mO7tRJ_CoK0sRQdjzQEkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این روزا تور مدیتیشن و استراحت مد شده و طرفدارای زیادی داره
:
اونایی که مشکل روحی روانی دارن میرن درخت بغل میکنن و گریه میکنن
یا با حشرات توی جنگل و حیواناش اینا حرف میزنن حرف میزنن حالشون خوب میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71303" target="_blank">📅 22:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71302">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=YJzpaD3hYdbGtX1qeHLLAKJ1E01TTrkp0MYZOe14FvdzB3YYzGDhzxFNoYDzVPz__B4INmEEEEOK-kuQ0XEhQsUxQ_J2WM-JXXAGivOwUXVYqNF0_4V1t8dZFz1VCFqfI2ewWn7lSd2k6qTiY3fR7_3VViFv8eYveZswSHghjdNiGMTFhJ0-W_G5Pp51Lrz5DvCp-mpXzeOQ1I7epBmkObqd9EyCdS9FGg82FY7oo1ZA9qwDPcf28y7f3CynZ30kPRDjKCnpHWS3HhMboj69MtGAlMz8z65hnPufW68EBY_SlHOcc8LTfWsaAiANsc20JZEW2DLBWYq15dnH7fU4DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=YJzpaD3hYdbGtX1qeHLLAKJ1E01TTrkp0MYZOe14FvdzB3YYzGDhzxFNoYDzVPz__B4INmEEEEOK-kuQ0XEhQsUxQ_J2WM-JXXAGivOwUXVYqNF0_4V1t8dZFz1VCFqfI2ewWn7lSd2k6qTiY3fR7_3VViFv8eYveZswSHghjdNiGMTFhJ0-W_G5Pp51Lrz5DvCp-mpXzeOQ1I7epBmkObqd9EyCdS9FGg82FY7oo1ZA9qwDPcf28y7f3CynZ30kPRDjKCnpHWS3HhMboj69MtGAlMz8z65hnPufW68EBY_SlHOcc8LTfWsaAiANsc20JZEW2DLBWYq15dnH7fU4DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
زمانی که بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود.
گاهی مارهای سمی زیادی در حیاط پیدا می‌شد.
وقتی سر مار را قطع می‌کردید، مار می‌مرد، اما خودش نمی‌دانست که مرده است؛ بنابراین باید مراقب می‌بودید، چون سرِ جداشده هنوز می‌توانست شما را نیش بزند و دُم مار هم ممکن بود تا زمان غروب خورشید تکان بخورد.
اما وقتی خورشید غروب می‌کرد و هوا خنک می‌شد، تکان خوردن دُم هم متوقف می‌شد.
🔴
حالا مار ایرانی — یعنی همان رهبری — هم هنوز نمی‌داند که مرده است، اما در واقع مرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71302" target="_blank">📅 21:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71301">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=HXpfDkan4wk5VXgorymVujmc8i6_wyJtrvESAPv5NTT_yQv36LievU6578l4xTNjrdWmxlaym0eymlu1poauqmqNNYTwsWs9o6RgfIfYQRXBAINKFrCynun17IVfw3MOCdFQetyOlaj7Tkv0R5vsGbsEUOHBhCWLJOj4H7LmJNf7RFtU5e5fSho1-YR3E7LAwrGeXzHrJXwbpKWCuGgGttWSAHROEYy0tmlhKH4QhlUo0knbvCZI1vEoXcqCBKYQupwn9Fy5VAaI1VG0NH4GyCcFbQa7cs6qlEM9olGIB5l5yZKQTcgfPAJz5P5vAL4U1S9fvSlGKPybX70luQTL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=HXpfDkan4wk5VXgorymVujmc8i6_wyJtrvESAPv5NTT_yQv36LievU6578l4xTNjrdWmxlaym0eymlu1poauqmqNNYTwsWs9o6RgfIfYQRXBAINKFrCynun17IVfw3MOCdFQetyOlaj7Tkv0R5vsGbsEUOHBhCWLJOj4H7LmJNf7RFtU5e5fSho1-YR3E7LAwrGeXzHrJXwbpKWCuGgGttWSAHROEYy0tmlhKH4QhlUo0knbvCZI1vEoXcqCBKYQupwn9Fy5VAaI1VG0NH4GyCcFbQa7cs6qlEM9olGIB5l5yZKQTcgfPAJz5P5vAL4U1S9fvSlGKPybX70luQTL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقتدار به روایت تصویر؛
🇮🇷
مقام جمهوری اسلامی:پمپ های قدیمی جا برای بنزین ده هزار تومانی نداشتند؛
یک صفر دستی اضافه کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71301" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71300">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از دیشب تا همین الاناست که مسلمونا افتادن به جون هم، شیعه های یمن، سنی های عربستان رو دارن با موشک و پهپاد می‌زنن، یعنی کشوری که خانه خدا اونجاست
عقل
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71300" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71299">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiDh_9-EgZRlG7wT9vQtyNmoSuDtPc2DMsrKVfHkJwMemykZ1ss80jFzcX1wKP635N-0z6d3xNTjv1bGC4jWUEgbYu2jCDJ6d4X6FWVFOohNnrqEjxMwlnEaUwySvzHR8Y0hJqQBDFoeHouE-xXHeOvrbojP85BKk6ObV0gvLyvgvrXYzYxFFu-1vJPHLhRwvWjPRBKN1InWVsgTeVqMdyrpG3wBRI2pAxGnRuJ7L52-w5F3AdcccPoPhbWzZ0L1QUMgl8ZxHR1wgtnrQITrmeyc-JXAWIz_1rWKZUiMbU_BPdBpEkDloale7kG2qFhXQUjvvGIEYsnWXz4K2w1D8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
وزارت خزانه‌داری ایالات متحده تحریم‌های گسترده‌ای را علیه بخش هوانوردی تجاری باقی‌مانده ایران تحت عنوان «عملیات اقتصادی مطرود» اعمال کرده است که ۳۶ نهاد را به دلیل حمایت از خطوط هوایی ایران، دور زدن تحریم‌ها و شبکه‌های تهیه هواپیما هدف قرار می‌دهد.
دفتر کنترل دارایی‌های خارجی (OFAC) ۲۷ شرکت هواپیمایی فعال ایرانی، از جمله ایران ایر تور، هواپیمایی آسمان ایران، هواپیمایی کیش، هواپیمایی قشم ایر و هواپیمایی زاگرس را تحریم کرد.
وزارت خزانه‌داری همچنین چندین مجوز هوانوردی، از جمله مقرراتی که پروازهای خاصی را مجاز می‌دانست و به شرکت‌های هواپیمایی غیرآمریکایی اجازه پرواز هواپیماهای آمریکایی یا تحت کنترل آمریکا را به ایران می‌داد، به حالت تعلیق درآورد.
این تحریم‌ها همچنین شرکت‌ها و افرادی را در امارات متحده عربی، ترکیه، بریتانیا، مالزی و قزاقستان که متهم به حمایت از ماهان ایر هستند، هدف قرار می‌دهد. وزارت خزانه‌داری اعلام کرد که برخی از آنها انتقال حداقل سه هواپیمای بوئینگ ۷۷۷ به ماهان ایر را از طریق امارات متحده عربی و عمان در تابستان ۲۰۲۶ تسهیل کردند، در حالی که برخی دیگر محموله‌هایی از جمله قطعات پهپاد، تجهیزات صنعتی و قطعات هواپیماهای ساخت آمریکا را جابجا می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71299" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71295">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mRkHmWfVR5l_7N9hMxmRVNkcEOZepROPxayySZ_hyf-prr2KEb68PRqdvTSXYeuap4ECw5-u6oomZwH6PByphojqWsZiKBh0LDqpJt-dVVW05Va7gjuYRcSRfxcklnvaoDYGlOYRZHC_4CKXiIZLsCs5W6KKPCw3OdVoNQDn7Lz2Zqowlgsvnlv_XSn2C15oTpEHnWXevPkY1xJWCmZLDjA3H1REh1sIa57mgI8Uwqc6tz8PBuiRMQum-5K0ucWv3JWuN2iF7WFvqpWhgZWuAIfnIMDMznlMDzvGCFeDyLBuaY1Z4qIDnaEJmTEJcp1nzjdS-x44rEuyB7tmx1653Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d307bda604.mp4?token=JlQxGjoYTRYzqtVtvqfAbqFVFgdYCh9HKHNqx9RYF52w_Cf9hjzhsKqfPmQgH25qw2UgeAQHTGEUGrEYuUb4arL-yaKJqtbBiwcf8hzt_7fL3X7os1mV0VLAS--GH2_bZtg50u58CCxvt5b5gB8kvVO47Ap6vYufsCBcRmAFpWAHlfEUlPtVgSlLXzpnHi5ueJxbmng5walDDQbsPsf-RP9ra952qfk8NZgT0G_jen0fSoSRqwnKfTpDg1QKfHBTkvV-kVW5mGNVWNlRxOfKiVFEtu9-A5RAIP372hX-rTaw1ghf6CK8EI8bvmLFERxn70avHRXepKhSQowxAl40Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d307bda604.mp4?token=JlQxGjoYTRYzqtVtvqfAbqFVFgdYCh9HKHNqx9RYF52w_Cf9hjzhsKqfPmQgH25qw2UgeAQHTGEUGrEYuUb4arL-yaKJqtbBiwcf8hzt_7fL3X7os1mV0VLAS--GH2_bZtg50u58CCxvt5b5gB8kvVO47Ap6vYufsCBcRmAFpWAHlfEUlPtVgSlLXzpnHi5ueJxbmng5walDDQbsPsf-RP9ra952qfk8NZgT0G_jen0fSoSRqwnKfTpDg1QKfHBTkvV-kVW5mGNVWNlRxOfKiVFEtu9-A5RAIP372hX-rTaw1ghf6CK8EI8bvmLFERxn70avHRXepKhSQowxAl40Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌂
امروز صبح رسما شمال کشور رو سیل برد!
به حدی بارون شدید بود، که حتی آب توی خونه‌ها نفوذ کرده و تبدیل به استخر شدن.
ماشینا وسط خیابون تبدیل به قایق شدن و برق اکثر مناطق قطع شده.
باد و طوفان شدید باعث شد کلی درخت و... شکسته بشن و بیفتن روی ماشین، خونه و مغازه مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71295" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71294">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iISKv52eYfeKhheY1WnwYYNck9CNCgajB7Ale8buyWfpyAj2faHnAAhIoVpDoaEJfEJ8myR7qtE7x_OfgJJUh6nWlslfGoZ4_JUwtABezU0QKLA0NyqKD6R72Y7DlTiv5JvJhqDhGSjO70wJsupyaEvPxfpm2DPK-Du9zKpnkHqX0Vxw-ED0BLtzfkgvQkJqjCW7-pqOe_UgmgcToGyx-fD7D1_oJQfbmkzPVXCf8bwM8gVfKhrCIQIw0QZUWJW0mlXB2g3nvhHTdav6eqh2nJtJbkCQRA5hUjI91waURPxCK1sOSc1eO9spWso21OFHJiXEk3lqPkeL7ElaiWEIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران انقلاب اسلامی:
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی‌های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند.
این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخور دار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
گفتنی است این زیر سطحی اکنون به غنیمت گرفته شده و طی ساعات دیگر تصاویری از آن منتشر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71294" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71293">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⏺
🤩
تسنیم:
تا دقایقی دیگر خبری مهم از شکار رزمندگان نیروی دریایی سپاه در تنگه هرمز منتشر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71293" target="_blank">📅 18:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71292">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=YeMvwfoKuddmkhhh3wT1inRMDzKmMEztANQdUYjNrMT8sOkZ2wyUSZohSUvtNt0mIF1jlNhWg6QLzCFPppDV44sL0QIYc_oJq4kJy7aBmGVGTIcAJl4gBgTm09wQZi-mpay06igS5NOctLfJFL6GSg5rdwT3xmGmOfIMfg-Du392tKx-GAFfWhelhqaYH8jA2NnL9EIvZ_JDG7wSFlibyBlFF9_HETx3PDkwK_oUlkTHRVcjymKNNCBdB_Olbn2Iz5To5ohZ12s8EsmTFDXccx6b6Q3Wl82j1RVk3FamA6qSCLN0GlNEz949US_cR1Q4a1ES16gnwi9lubqEpYixfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=YeMvwfoKuddmkhhh3wT1inRMDzKmMEztANQdUYjNrMT8sOkZ2wyUSZohSUvtNt0mIF1jlNhWg6QLzCFPppDV44sL0QIYc_oJq4kJy7aBmGVGTIcAJl4gBgTm09wQZi-mpay06igS5NOctLfJFL6GSg5rdwT3xmGmOfIMfg-Du392tKx-GAFfWhelhqaYH8jA2NnL9EIvZ_JDG7wSFlibyBlFF9_HETx3PDkwK_oUlkTHRVcjymKNNCBdB_Olbn2Iz5To5ohZ12s8EsmTFDXccx6b6Q3Wl82j1RVk3FamA6qSCLN0GlNEz949US_cR1Q4a1ES16gnwi9lubqEpYixfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
⚠️
🇺🇸
افسر نیروی هوایی ایالات متحده که در ماه آوریل پس از سرنگونی هواپیمایش بر فراز ایران، دو روز زنده ماند، برای نخستین بار در برنامه «۶۰ دقیقه» (60 Minutes) — که قرار است روز یکشنبه پخش شود — به بیان ماجرا می‌پردازد.
این افسرِ مسئولِ سامانه‌های تسلیحاتی که نام عملیاتی‌اش «دود ۴۴ براوو» (Dude 44 Bravo) بود، یکی از دو سرنشین جنگنده «اف-۱۵ ای» (F-15E) به شمار می‌رفت.
در حالی که خلبان ظرف چند ساعت نجات یافت، «براوو» به مدت دو روز در مناطق کوهستانی ایران، در حالی که مجروح و تنها بود، از دست نیروهای ایرانی پنهان ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71292" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71291">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71291" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71291" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71290">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdxG9gdOc8xoMv26WkaOZB5k48JSeYSjkVHzypE5NwbqRRVdwNad3a-p0SeIQcT_p47krAK2dUFev7w4D5t75d41RWFU_87WPI3Rgyz_ePi3izZZh1rSzWadlWH_KQi520R4JK527V1cSKZ7HH2gLdNtAAT1TWy9BO9pahucQvvJE4VvmYa4Mv-C_YhNHMrZOHXN2QND1SZKH8u2iGQuyQOAjICD4Q9Cyh96ovmRbwUHxIwPGDSczAt3rzeHankrtTbgS0Y5byZkRE5aSXpVWQJB8xayz58P3XmD5XFuoCm9gkZ_etQ4EPpfpw5WxNyCxFR2965W5YxDBGbwNUTA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
منچسترسیتی
🆚
پورتو
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
منچسترسیتی: ۴ بازی، ۳ برد و ۱ تساوی، ۹ گل زده
⚽️
پورتو: ۴ بازی، ۳ شکست و ۱ تساوی، ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71290" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71289">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
دقایقی قبل صدای سه انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71289" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71288">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=cGPODPjMARYhdnHOspv32CnhqKP9rfQRdk6WH1j59uHnHvcZ3h0dvMXiKHn0tawmP6f7UEI5tWBxKhjxBDOFZVfL4AqL--5GJZs8cDlgjgOj-mDGXnm4ZYRbo7Q_TFLbajqG6E7j-4IydxYxRtyokXykxHqmMgw-CuHfnN1bhRPV5-dePdYos3zj6zadbmNb63zmNSI023J-Or0dc_yAnbhg-7FMiZ_ZcGUvIi4ohgyWA5aEzaADBZV6AIOvoLrmkss7WfaiVF73EQKJxxfUx46gHt_2lofUsSRfq4EN4kE0fwuYVfnFE0JVg0M_vhXaiwhjor7PHhURs7yPUQyNDxt9kqfziNzHESZV0agH6iPdqf2vHYdeKKgp3LF7n2-jgW9i7ndjKaHTKB_AY2kTSvjXdDuZnHfirtR65SsDhY_jJY1RV-NfNuKZLw0X9J1RiaSon434J44J5R-4rGgxt54l2mXcR1uPXdqvBZfoWhoNLfFBUlmEgrfoj_zEcjENl9jKs1TYyGJ9UrJXPQC2Zxy9EP5zG-53FIbYqWAvhOB_7NSKEM6EXO4ei4UV3dO9GpkRhdvIEerCWzai-6oWQ5bEcFM9X1LSk1YIPbGKo_-1KuBc4JT1b1yPheMhY1FwFzMmQA1xc93KSfVWZP3nFgZC0CqXHeMHL8DGx8mhnEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=cGPODPjMARYhdnHOspv32CnhqKP9rfQRdk6WH1j59uHnHvcZ3h0dvMXiKHn0tawmP6f7UEI5tWBxKhjxBDOFZVfL4AqL--5GJZs8cDlgjgOj-mDGXnm4ZYRbo7Q_TFLbajqG6E7j-4IydxYxRtyokXykxHqmMgw-CuHfnN1bhRPV5-dePdYos3zj6zadbmNb63zmNSI023J-Or0dc_yAnbhg-7FMiZ_ZcGUvIi4ohgyWA5aEzaADBZV6AIOvoLrmkss7WfaiVF73EQKJxxfUx46gHt_2lofUsSRfq4EN4kE0fwuYVfnFE0JVg0M_vhXaiwhjor7PHhURs7yPUQyNDxt9kqfziNzHESZV0agH6iPdqf2vHYdeKKgp3LF7n2-jgW9i7ndjKaHTKB_AY2kTSvjXdDuZnHfirtR65SsDhY_jJY1RV-NfNuKZLw0X9J1RiaSon434J44J5R-4rGgxt54l2mXcR1uPXdqvBZfoWhoNLfFBUlmEgrfoj_zEcjENl9jKs1TYyGJ9UrJXPQC2Zxy9EP5zG-53FIbYqWAvhOB_7NSKEM6EXO4ei4UV3dO9GpkRhdvIEerCWzai-6oWQ5bEcFM9X1LSk1YIPbGKo_-1KuBc4JT1b1yPheMhY1FwFzMmQA1xc93KSfVWZP3nFgZC0CqXHeMHL8DGx8mhnEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇬🇧
⭕️
#فوری
؛اد میلیبند، وزیر امور خارجه بریتانیا:
ایران هرگز نباید به سلاح هسته‌ای دست یابد؛
از این رو، ما نیز در این هفته همگام با متحدانمان اقدام به ارجاع پرونده ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات هسته‌ای‌اش می‌کنیم.
همچنین امروز می‌توانم اعلام کنم که ما در هماهنگی با اتحادیه اروپا و ایالات متحده، تحریم‌های اقتصادی عمده‌ای را علیه ایران مجدداً اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71288" target="_blank">📅 17:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71283">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645274372a.mp4?token=svEP4zSHIK6Yzrnkt7x9ELRlP0H1GMAuQ2BruS-LH4oKY145Gwsu4W1jmqSSbDUp2V65KN6p2A0E8RADgsh2w_FJ6zKdAGu9-1lzBJue0Rjri1ZHN9CX0XtolOcckfhQpvJEhcOA5yDU5Wja0RDMdpDd6uTI1L3m7ktm2i2VAy-Q7gNNaftpi5m8hYZY5IQUfhY-H_Uv0S26-CNPwTNZUk3wow7COtsrOELLSOgj_ZMEEzlOTcXY1206vQm74nlR2jui8nJgml9Xss07_d2JyaCH2aIxSLGt7ejtuVOHgetptJRL8vtA4Jkgdu-ELnZRTTG_Y-TYItRwX7S_n26aNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645274372a.mp4?token=svEP4zSHIK6Yzrnkt7x9ELRlP0H1GMAuQ2BruS-LH4oKY145Gwsu4W1jmqSSbDUp2V65KN6p2A0E8RADgsh2w_FJ6zKdAGu9-1lzBJue0Rjri1ZHN9CX0XtolOcckfhQpvJEhcOA5yDU5Wja0RDMdpDd6uTI1L3m7ktm2i2VAy-Q7gNNaftpi5m8hYZY5IQUfhY-H_Uv0S26-CNPwTNZUk3wow7COtsrOELLSOgj_ZMEEzlOTcXY1206vQm74nlR2jui8nJgml9Xss07_d2JyaCH2aIxSLGt7ejtuVOHgetptJRL8vtA4Jkgdu-ELnZRTTG_Y-TYItRwX7S_n26aNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
نیروهای «شورای رهبری ریاست‌جمهوری» (PLC) تحت حمایت عربستان سعودی به همراه جنگجویان قبایلی، شهر «الیتمه» در استان الجوف را از کنترل حوثی‌ها (انصارالله) بازپس گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71283" target="_blank">📅 16:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71282">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⏺
فارس:
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق ارتش جمهوری اسلامی ایران شناسایی شد و هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71282" target="_blank">📅 16:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71281">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de453ade.mp4?token=T6mdu6gQhPFeWR-z8jXZ_UHjWXEUh6i8j6Z2oB_D65IVl4365Xv0uIsBVC-ZNZ86VPIgNM_86pp815krnOKGT9PPqI6BkTTXV9NW-mcnr_wybqO_ERFaAaeykiZW3a0IFj3u000Q6QjYvsZsJnYgqvSILppZXVb_GOq2_sF6DwpOocIa0z6-5w9Jv97Ij1gDWBR21ntk1ksRIJ6cF79jQ4gbazYBzdLoZNf9UplNdGm687Fsvhyf03ap5geHWSzsG6sbCUzCYUSZwnsAFLQlrWX2MQPQM8B63rpIvDveEgIQjrFNYBlb7L_b7Z8HAWI7D3QwVYL3-HeoY82JD9CWsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de453ade.mp4?token=T6mdu6gQhPFeWR-z8jXZ_UHjWXEUh6i8j6Z2oB_D65IVl4365Xv0uIsBVC-ZNZ86VPIgNM_86pp815krnOKGT9PPqI6BkTTXV9NW-mcnr_wybqO_ERFaAaeykiZW3a0IFj3u000Q6QjYvsZsJnYgqvSILppZXVb_GOq2_sF6DwpOocIa0z6-5w9Jv97Ij1gDWBR21ntk1ksRIJ6cF79jQ4gbazYBzdLoZNf9UplNdGm687Fsvhyf03ap5geHWSzsG6sbCUzCYUSZwnsAFLQlrWX2MQPQM8B63rpIvDveEgIQjrFNYBlb7L_b7Z8HAWI7D3QwVYL3-HeoY82JD9CWsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنازه و تابوت ترامپ و نتانیاهو زیر پای طرفداران حکومت برای بار هزارم له شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71281" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71280">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=p5GcgJqzgjOgYZi7izOFiuJ0R8TzEPosFagLT23w1kdh57mImJ0PVekh6TEl1zSY4oWgTqID2A6PzAnZpB0Zs3nT7VX9Axg3E2631nS44H5Oaopu8B1PuTj7CAxpxdJ7ydN5rmeb-vwsjAwdAuj26n90diSvetEtv-ZFGoFyuyBzF0UpkYZqHnS9unQ3zWe63YzV3R4tBKj9x_TnQCk1DwtjSP6_edtyp0ux8_6RrGbne3slPV2cVEqK5HzKYZocUtehy3kyHr0m7oylUCUfEbruakQOHkRciQv9W_tvDOd60sZF9IxXA51rz8HWX853xb1eu5VXH0Pr0A1vZZqoA64OeNTHTFOD6f2gz_rpSMTZ6kP4J9BSh9fDGM9DBxaOUd-o4CDfJC9XZDVU2qe5umsQHnriWSPhYX826SKftQzIQCH3kTeCrJCmN1nCt-dyfjrahR7iY6yWnW4kopFaBtXg3ZhCCKFySBZbb3XTIybctvfzC1Wz0D2wEIrz2CQO-vNZZ25OsMJiZvV7axPgI1WcyQZf7KUV3DbmHvQGSZNUWLv4nA-aerXtxrSJxKxcwZsZaK7ONknVzaMfeXatqnVYsTPoLZQ8JHtlkFwRmea0sox1bqXFbfAvLWMCLKMcIzqxmLgbWV9KI2JYwkdfmc9nQD664JYhvNj4jnbSXl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=p5GcgJqzgjOgYZi7izOFiuJ0R8TzEPosFagLT23w1kdh57mImJ0PVekh6TEl1zSY4oWgTqID2A6PzAnZpB0Zs3nT7VX9Axg3E2631nS44H5Oaopu8B1PuTj7CAxpxdJ7ydN5rmeb-vwsjAwdAuj26n90diSvetEtv-ZFGoFyuyBzF0UpkYZqHnS9unQ3zWe63YzV3R4tBKj9x_TnQCk1DwtjSP6_edtyp0ux8_6RrGbne3slPV2cVEqK5HzKYZocUtehy3kyHr0m7oylUCUfEbruakQOHkRciQv9W_tvDOd60sZF9IxXA51rz8HWX853xb1eu5VXH0Pr0A1vZZqoA64OeNTHTFOD6f2gz_rpSMTZ6kP4J9BSh9fDGM9DBxaOUd-o4CDfJC9XZDVU2qe5umsQHnriWSPhYX826SKftQzIQCH3kTeCrJCmN1nCt-dyfjrahR7iY6yWnW4kopFaBtXg3ZhCCKFySBZbb3XTIybctvfzC1Wz0D2wEIrz2CQO-vNZZ25OsMJiZvV7axPgI1WcyQZf7KUV3DbmHvQGSZNUWLv4nA-aerXtxrSJxKxcwZsZaK7ONknVzaMfeXatqnVYsTPoLZQ8JHtlkFwRmea0sox1bqXFbfAvLWMCLKMcIzqxmLgbWV9KI2JYwkdfmc9nQD664JYhvNj4jnbSXl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چنتا دختر با کیسه زباله خودشونو شبیه لاکپشت های نینجا میکنن میرن تو خیابون...
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71280" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71279">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=uxW7RkO_2GqlCeKIUtCI5vCSYZqqMyi9naCBqHwJ2nzYopHCg8y58TuGUgR_VpIR9fV6dh3N-gegtqVptR_eZz9DQmyB4b80HBIzDKuxPPwwekVl-HIxAU3gYF4OUZpx2gMYXAwvaFskHcknXF3upK83xEKMay-D4EwiAx-ieegY5tUdWQFusoKY2RA2-L8GmS1WoqJtkgmY-LjibU-DCvKnw1byZQfkRH7LA5LMu40ByFrBJK6NTX_2COB9_Xe3y9tp68_kGsFVeGUytXDqPSiTTBTsu1llsnAxMUEFmVZY9b_7lmEMGNJmFlqqCFklz2UvOxrb8-y1QZbTQ__-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=uxW7RkO_2GqlCeKIUtCI5vCSYZqqMyi9naCBqHwJ2nzYopHCg8y58TuGUgR_VpIR9fV6dh3N-gegtqVptR_eZz9DQmyB4b80HBIzDKuxPPwwekVl-HIxAU3gYF4OUZpx2gMYXAwvaFskHcknXF3upK83xEKMay-D4EwiAx-ieegY5tUdWQFusoKY2RA2-L8GmS1WoqJtkgmY-LjibU-DCvKnw1byZQfkRH7LA5LMu40ByFrBJK6NTX_2COB9_Xe3y9tp68_kGsFVeGUytXDqPSiTTBTsu1llsnAxMUEFmVZY9b_7lmEMGNJmFlqqCFklz2UvOxrb8-y1QZbTQ__-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
آتش‌سوزی در تاسیسات آرامکو عربستان سعودی در پی حملات حوثی های یمن
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71279" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71278">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=sSizpJNLLLhoo8xknjqw6szOeSciK-c7H0-rX7eKJ7cX3pmSrU-lATYxekhiFoduch88Vnx62XuTBEJnCe8KWxnU95z9K6ZbopLBxVSIwUKCLJbnqAJj1qc3c9FuGa9eAI4m1M5RiBqxjk4mX-DYVILvLxuP2hU8jZ4hNlaYquYfh8Nw53z4CMaE7xoX8B3cH9SU62gN_DaANyWL1TymIth9NOP_iuoYGAfDgjA2mu0o1UDokfiifFBLB5H8pOPZ-A-epIM2tg2Cuf7KzBX5NnWeUtSJ3jTJvTn3gPmnsjIg6z10Xo1SLnUg35Icndlzkukz3Y9X29Zmttgt2tr8vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=sSizpJNLLLhoo8xknjqw6szOeSciK-c7H0-rX7eKJ7cX3pmSrU-lATYxekhiFoduch88Vnx62XuTBEJnCe8KWxnU95z9K6ZbopLBxVSIwUKCLJbnqAJj1qc3c9FuGa9eAI4m1M5RiBqxjk4mX-DYVILvLxuP2hU8jZ4hNlaYquYfh8Nw53z4CMaE7xoX8B3cH9SU62gN_DaANyWL1TymIth9NOP_iuoYGAfDgjA2mu0o1UDokfiifFBLB5H8pOPZ-A-epIM2tg2Cuf7KzBX5NnWeUtSJ3jTJvTn3gPmnsjIg6z10Xo1SLnUg35Icndlzkukz3Y9X29Zmttgt2tr8vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
در سمنان برای دومین شب پیاپی میان مردم و دانشجویان عراقی وابسته به حشدالشعبی درگیری شد.
این درگیری روبه‌روی خوابگاه عراقی‌ها در باغ‌فردوس اتفاق افتاد.
ماجرا مربوط به متلک‌پرانی و مزاحمت آنها برای زنان و دختران است که بارها اتفاق افتاده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71278" target="_blank">📅 15:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71277">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fuzNkOogHDsz3UDLZHGfr-Mlvv3K8M0RNI8ViUR8xIv24YJGUcNoAMHMeJYt2m3cEWaa0hkNEtS3rXVNNvu-Pnkjj_G1pt6VQRfLHD16Iv2mNhekvOlfVqwUJ2WgZKpqFLjMS8Vs-FRW21qTlSaL59pd1xWpBGzAfrdPxFVwnDgtzidkLGJciPVJ1kflrcExyErp_jSf192elBmE0p4V-ejFr5M8aV_Yry5gL6BLesIWk1cM1PQqoiVO2AQzAWlUs5nNDlcSizijpctsP1KZwymMV1YItmhJb9qY2gpIFVdvhLoGbB-ilSXfOoKL9LFQVmU1VOjob7i7nHETNtRBFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
امروز ۱۷ شهریور، تولد مجتبی خامنه‌ایه و ۵۷ ساله شد.
اگه زنده ای شمع هارو فوت کن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71277" target="_blank">📅 14:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71276">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=TXau-AZaJnyE12GwZUBUotGwJjqr1dfE_4E-qjHhMCy2fma4GbxUmuKI0arimzUNT_dSb_yOOuZw42Uw_axk8jRWAkhKipqOYvwqZojQ_WufQ3c5On9v_Iwv_DZhwjaKysF12hjVDS4krHzyYRtYMjZ2DLcOSCiQnvhpj7pddQ2hP20lLGR0j7Gu-tvwzoSiQ68MdAUpCpgShj1oadZMB18z5SaBgAqI2VKIF_YroPE2YM7ypoFT4wpqRfQQJiio-htTgX_SoKWt5hQSyBTYUHKv1GuVu5P47a-5VI9JsaQ7cWJrJGfEfqVzSak8kNaoFc0QNwx08k6r5IMsSJE2lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=TXau-AZaJnyE12GwZUBUotGwJjqr1dfE_4E-qjHhMCy2fma4GbxUmuKI0arimzUNT_dSb_yOOuZw42Uw_axk8jRWAkhKipqOYvwqZojQ_WufQ3c5On9v_Iwv_DZhwjaKysF12hjVDS4krHzyYRtYMjZ2DLcOSCiQnvhpj7pddQ2hP20lLGR0j7Gu-tvwzoSiQ68MdAUpCpgShj1oadZMB18z5SaBgAqI2VKIF_YroPE2YM7ypoFT4wpqRfQQJiio-htTgX_SoKWt5hQSyBTYUHKv1GuVu5P47a-5VI9JsaQ7cWJrJGfEfqVzSak8kNaoFc0QNwx08k6r5IMsSJE2lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
شب گذشته در سمنان، به افزایش قیمت بنزین اعتراض شد.
این اعتراض در پی تصمیم جمهوری اسلامی برای دو برابر کردن قیمت بنزین خارج از سهمیه یارانه‌ای از روز سه‌شنبه صورت گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71276" target="_blank">📅 13:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71275">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNB7mR5napjXrRAs-d14kF3YAQlOzhs_LqEV-U7I50Qp01f1H8B2PxdV46wWashgBNHKP82iAlfkzgyucPA6GBBu5FMhKdBB1shd5kvp_MvMRNkowXDb3HpHNDPKKrDWCktjx_0TNiPjamUtAxUE3i4_X91Hm5SmzCdNGQfEb_JP1wAZ3W3l5GPUaJ91wUzq3CO_sbK7POQhipywlU6X5dKI_yo1hmJZDAlns8reNUR5M8KuwaxlQn6RW2PZd8y-gyZWJMTUHCYXLZyTaQDIpNAcZl0yygfl4rgWqNZUbHSeMAPTP3gbwsj0_wf0h9pDHMJWP13uXcvg89AAdRhf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
جمهوری اسلامی ایران همواره با جنگ مخالف بوده و حفظ منافع مردم و امنیت منطقه را در پرهیز از آتش افروزی دانسته است.
اما چنانکه تا امروز در برابر تجاوز، دلیرانه به دفاع برخاسته است این مقاومت را تا پشیمانی کامل متجاوزان با قوت ادامه خواهد داد و پاسدار حقوق ملت بزرگ ایران خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71275" target="_blank">📅 13:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71272">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jYn4fHvxlmoW6qcxj83ej5kbJ7oyDEVg4EEFu3wAc_hgfXAn_MSUCOG0bX8_CgPOrGlQOHdOCJtwSNaZ2y1d4AJLZ7-LXpcjalKA3bus3n-aGWLLmSzLR3pIgk2nwBbvhMKq6-22JhQx9pzE1nvRwqi7c1NKEMbnmX7aodxrOQazbQMFjqLQriUij7zMoviXfsXSv70geRA70JLpc1eDR5jrowtnS4TADa90UgT8G-wrDEaiTy6lGhMaOTlyeZZ9GRAsya5tLyYsPiNe_zbZ2Uyz7K-OiU2OXaoKcSQcjthlP3CKNWBmeRd_D2kN3I0aJIHbB8WUjY02dRvy43ddNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8833895957.mp4?token=qqHIDoPRTD8FojBOfi_XLNmtoGFDHptZvFpbeYYs_XMLWUqBluej6uvskjYsZfRnuA96F1Llhjai7SzZlZeIUGXQsvM8O2qKd85J1CKPhAXDeCIT9D6ydz6AaGwCp3kppXddJN868AATAQLJYznD9D8Q_UibTV2hdxQdtdR2j2EUVsQz0o9XWpDqtnmd2WzAK9cnZ0uIlyvH75JznacZk-i6LqtF2_caXIjL0dyc78MS9_qIiwkeH7o8zKzL_OnyRPjo8KgtCoXKh9cN43k4FzQ902vWDo2ZjWpX_pYlMEo8nqxxXIg9zXO8pQQ2kPu8LMOFGagyub1x_WTTaAom-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8833895957.mp4?token=qqHIDoPRTD8FojBOfi_XLNmtoGFDHptZvFpbeYYs_XMLWUqBluej6uvskjYsZfRnuA96F1Llhjai7SzZlZeIUGXQsvM8O2qKd85J1CKPhAXDeCIT9D6ydz6AaGwCp3kppXddJN868AATAQLJYznD9D8Q_UibTV2hdxQdtdR2j2EUVsQz0o9XWpDqtnmd2WzAK9cnZ0uIlyvH75JznacZk-i6LqtF2_caXIjL0dyc78MS9_qIiwkeH7o8zKzL_OnyRPjo8KgtCoXKh9cN43k4FzQ902vWDo2ZjWpX_pYlMEo8nqxxXIg9zXO8pQQ2kPu8LMOFGagyub1x_WTTaAom-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌧
بارش شدید باران دیشب در رشت که منجر به وقوع سیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71272" target="_blank">📅 12:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71270">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stCLgozEAJvpt3_lYlxfvi5O_lGEI_bghqd6dqWO9_b9SKC8xA7l57TsvXORE4-13FDVroqi5V679djSmRQjI1DE_kBwOpRFD76lGHyzBiXy0it90oDDpjbBSLWqDzKZCvFz7iI8PSaPntSuLcthwtOjf_jiyvYKuRqad0K0_TrZLdolaOAX7vR3iVVW1arzD9bN6cGoWi0J8VcXcsGv4ILN5mVZKow0hFjdYyUVq8N2CuvilEGaqmwfYyTB7FxVlS9x_YHOb0QfSpE4ggCWNFLpI8Sr6TFxs33mykSPib1dEBvF_66RCK-LQ_ydyeLho5QlIWfyfxa4gtbfkDmrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=KSfc89dwoZDgkmOcEiEZEf5bpu_VM3j77PnhzGXZzSGsspQy1DaSXXPZaHfkAMv_mC7yBidkG_TkwSnCTyWKSv-eeLAxv54lstMh1OnHF1_Qg26vvdPV8Dt36oWLYWXnMGtJXXZ1kMUth-So4l--s9Cl3ndfs7yceyxI3yzL42CRMnrwRYIiMtM3uZ4_boUI9QbByuiM1Nrljjjh1wkiOXksugNcRqE5AThzvSYLvPKPbF0ItlAkomDlJyiIRs3szN0dP2MYb5LPCeCixpTYGklJ35cLQZIVQJmcW4UXVXC1G6NNAhVH1zlRkbYKyrh7RKxD88faqdrF6LmfQi1k8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=KSfc89dwoZDgkmOcEiEZEf5bpu_VM3j77PnhzGXZzSGsspQy1DaSXXPZaHfkAMv_mC7yBidkG_TkwSnCTyWKSv-eeLAxv54lstMh1OnHF1_Qg26vvdPV8Dt36oWLYWXnMGtJXXZ1kMUth-So4l--s9Cl3ndfs7yceyxI3yzL42CRMnrwRYIiMtM3uZ4_boUI9QbByuiM1Nrljjjh1wkiOXksugNcRqE5AThzvSYLvPKPbF0ItlAkomDlJyiIRs3szN0dP2MYb5LPCeCixpTYGklJ35cLQZIVQJmcW4UXVXC1G6NNAhVH1zlRkbYKyrh7RKxD88faqdrF6LmfQi1k8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپاد اوکراینی به یک ساختمان مسکونی در پرم، روسیه، تقریباً در ۱۶۰۰ کیلومتری قلمرو تحت کنترل اوکراین برخورد کرد و یک نفر را کشت و چهار نفر را زخمی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71270" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71269" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYxqJ4d0_3S2ArluG0R391CHx3B55S9ivZkoNUKmyri2fBz3fwOxny_4EQ6BfDbW8fFWpxFm7ztekEJ1wA_NRFfkv3nL2zCJLaGi66fRvQowiFXlGPzunmEUcBOQKhbVdYBYYJnCI80LCKO2D7E7cwWTyhGq2il-vZc6ckCAlRvvCsntK7m_0UHBRpPyujyGHJRa25TjucP8GujdVcZHdpRzr0tFQ7TUG-SRxRuqtt3YBbXd3bEWousE7TK_08EtuWqwm2jehB2L_gd8tqo7aqZqvPepvKMzzdp5iBN6s0DN5AAU2AmGbCrOGHZs3WahjRwVvqpApXXAbrZYbJLVtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71268" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=mi7aKIJAvoYxnll0Wr6wXSlCf0mmyGhDOShiiz_PxaIwe0VjcFKp6O97mLnApcKY-J_yeLwC0Ik3yd05D4DScLeocVvtLW-C6j5IlWyovaTrSGCsPjF5S0dOVZUkErt7XFnr8ljpHlmpwX5d7T6MEr8igrPvr39v4wtppl6j9C9-0swylq-ibqMIaE7ZFrjUylEZ4SFwvLH6wNHS9QRIhS_TgGrPEhvzHz3cny4YxOTdjDBXTzdOwv_gYRxeHMPuKC6Yw6EkMSa09YHsTOWlOX77v5Pu2Hr3zOvnov4PBKvZkB04kuH5FgQ8k4Zx2qj3EsjbWYQO2mTqCK5Yd6ShwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=mi7aKIJAvoYxnll0Wr6wXSlCf0mmyGhDOShiiz_PxaIwe0VjcFKp6O97mLnApcKY-J_yeLwC0Ik3yd05D4DScLeocVvtLW-C6j5IlWyovaTrSGCsPjF5S0dOVZUkErt7XFnr8ljpHlmpwX5d7T6MEr8igrPvr39v4wtppl6j9C9-0swylq-ibqMIaE7ZFrjUylEZ4SFwvLH6wNHS9QRIhS_TgGrPEhvzHz3cny4YxOTdjDBXTzdOwv_gYRxeHMPuKC6Yw6EkMSa09YHsTOWlOX77v5Pu2Hr3zOvnov4PBKvZkB04kuH5FgQ8k4Zx2qj3EsjbWYQO2mTqCK5Yd6ShwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
حساب کاخ سفید در پلتفرم ایکس:
در روشن‌ترین روز و تاریک‌ترین شب، هیچ شرارتی از نگاه من در امان نخواهد ماند.
آن‌هایی که قدرت شر را می‌پرستند
از توان من برحذر باشند..نور فانوس سبز!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71267" target="_blank">📅 12:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=rcJUY-WTu6DhN2K1Fj3mZYQFUkjlo1s4J8LRADXN1soEG5YmRMad1GyrLJHPAk42YmXuvh2xHD6wXfai8HlF64ZIHG7D50_uanD04ZVUB4l3VOmB3Rt6k8q9U3N9Ro7zkUllDSQ_-TsLBi5Mf87-IZdKuq16wsTvdirEwfJJzakUdTepo6Buu77VM_IKv-vDSGa5hQg7f7TIr-KO6F_KKC3fmoiEAvGRliC-kXfBAax1ov9UPyJKrLtv5H3WizkzkmotEg74zepILH06lBnuS41HBGFKdYbkiaWdaMojpcyrbdXb_BRPFmJe-jm6UumeyGgSdN0g_nl6U39xsa7FqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=rcJUY-WTu6DhN2K1Fj3mZYQFUkjlo1s4J8LRADXN1soEG5YmRMad1GyrLJHPAk42YmXuvh2xHD6wXfai8HlF64ZIHG7D50_uanD04ZVUB4l3VOmB3Rt6k8q9U3N9Ro7zkUllDSQ_-TsLBi5Mf87-IZdKuq16wsTvdirEwfJJzakUdTepo6Buu77VM_IKv-vDSGa5hQg7f7TIr-KO6F_KKC3fmoiEAvGRliC-kXfBAax1ov9UPyJKrLtv5H3WizkzkmotEg74zepILH06lBnuS41HBGFKdYbkiaWdaMojpcyrbdXb_BRPFmJe-jm6UumeyGgSdN0g_nl6U39xsa7FqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یکی‌ از مراسم های تولد در بالاشهر تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71265" target="_blank">📅 11:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=buRtwz9Xb8yYuR6uEm1rxpLnmkRguTTcfm_wUZ2tkuoiC33a3ExDyw0igUwAp9hqcwIm2ezvxe734t-nZVodOHz-bA5abHO3-Dq2ueJJaQ_pdn7pz0QvcfHrvxuh1dX5uFRKNzpaBNKvup5o_1XBYbPWV3YgvEdMG1LCwgs-C7CRGS7-rM_CJMfWbtsHCB2jN7HnlXIKuwT-oJyU0e1BYBxcBpcbrI7Do9_kJ0GMFmX5gmP163FVTJCZftkuPxrmb1zfZ3ysoLDNU16AQN0g3j21fdhQbiJuTGJDxXwzulbBEM49Oh4WEg4NEltG315xBZIIq9r_XWnxc0dcGvZKvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=buRtwz9Xb8yYuR6uEm1rxpLnmkRguTTcfm_wUZ2tkuoiC33a3ExDyw0igUwAp9hqcwIm2ezvxe734t-nZVodOHz-bA5abHO3-Dq2ueJJaQ_pdn7pz0QvcfHrvxuh1dX5uFRKNzpaBNKvup5o_1XBYbPWV3YgvEdMG1LCwgs-C7CRGS7-rM_CJMfWbtsHCB2jN7HnlXIKuwT-oJyU0e1BYBxcBpcbrI7Do9_kJ0GMFmX5gmP163FVTJCZftkuPxrmb1zfZ3ysoLDNU16AQN0g3j21fdhQbiJuTGJDxXwzulbBEM49Oh4WEg4NEltG315xBZIIq9r_XWnxc0dcGvZKvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یک پهپاد اوکراینی در طول شب، بمب‌افکن تاکتیکی سو-۲۴ روسیه را در پایگاه هوایی ساکی در کریمه با موفقیت هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71264" target="_blank">📅 11:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=UBODFFIz1KDsI-Wjbz7w05Bj4FXfU5F2ev1K6qQMs-lkf_NCHAU5fBPwFJ7T4zQ-4gH2WewHK-B0hMrBK3n_3ZbfCzcNbZxhLrpa2yVqeCnYrbYFw_N4c80IopspMiqmZRA0dDsbvM2fuBpmP0XZLGvuV7jGKbmllUvBwFV2InLkWyKDFmmcs7jHnYkSzWUMO4EtK2aHg5Wt8OuG5G39vjJ0KdeKqgexOLrRW1PmqbIw8PMbIe-HyrXfYhiikY-MieviTcveaZ1iiLdSZ-xkfNNFt63-4uvEJqTUUniGlZ4yW-pCs-OO4XD-RRDDS7PdmQsIICICPosPsXu-BEsW_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=UBODFFIz1KDsI-Wjbz7w05Bj4FXfU5F2ev1K6qQMs-lkf_NCHAU5fBPwFJ7T4zQ-4gH2WewHK-B0hMrBK3n_3ZbfCzcNbZxhLrpa2yVqeCnYrbYFw_N4c80IopspMiqmZRA0dDsbvM2fuBpmP0XZLGvuV7jGKbmllUvBwFV2InLkWyKDFmmcs7jHnYkSzWUMO4EtK2aHg5Wt8OuG5G39vjJ0KdeKqgexOLrRW1PmqbIw8PMbIe-HyrXfYhiikY-MieviTcveaZ1iiLdSZ-xkfNNFt63-4uvEJqTUUniGlZ4yW-pCs-OO4XD-RRDDS7PdmQsIICICPosPsXu-BEsW_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تهران، بیت رهبری، ۹اسفند ساعت ۹:۴۰دقیقه صبح
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71263" target="_blank">📅 10:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=b89FjSky4rCzdPbj49os2hq70mmWummPJu9j-1x6xTEXjUlri95LFdM95LPS-TdJc_MEuibVgKv6FiB35lyVv5Ih2uq_45JyBbMH7zZgEvRKc2C2UPOS1iUrMJ2mSEoySII5JC39Sy22gfC9YRTOmPoOzKoGSljSseLwL1pN5GZ-0t-ctOyOtC3zgJKNK00WCVqca4lRdVr0-6HGfjhdbmkPOvJdt1HthiGsbC8Z7o8TVu-YVg1MEJEzl7GGOcC1NUw_4hPWFRMVuleEALdLFR5NdD75bLv8TtqLtvUA1yzHlv_XCrtdSFl_BwWBHoy-r4KrM0ukrbIBkok_s85eZZik7lDx3DL79ftTgIrurzwlWIeMs_eT6xyjMUehmcJzMTS4ycc1tP-ph3vaxU4X44XZ7rodWAJ3COhAbUwK7bHgcBvcYt-O6CB9MtlqDEKSd0R8xGguquEIWa0We8pDNsb9FqDwqOU9NtBYoggb22uu-s6ZnOBIwo-TxCQMjHNydDJF3Ifj_111qlXOeyvj2VHNMiC4DIvEqHT_65_qxQ-HLHaGh68OdHIRCWdMy-SsQys4IoZ8v87NhLUAS7FxBkJeIFtBqciLZKxpDkf3A6pyq8LXzTXR3TpaZq2RFSNhvtLtCizlz9dFa30l9yr_B073VqbAouQpFyDaNGFyQTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=b89FjSky4rCzdPbj49os2hq70mmWummPJu9j-1x6xTEXjUlri95LFdM95LPS-TdJc_MEuibVgKv6FiB35lyVv5Ih2uq_45JyBbMH7zZgEvRKc2C2UPOS1iUrMJ2mSEoySII5JC39Sy22gfC9YRTOmPoOzKoGSljSseLwL1pN5GZ-0t-ctOyOtC3zgJKNK00WCVqca4lRdVr0-6HGfjhdbmkPOvJdt1HthiGsbC8Z7o8TVu-YVg1MEJEzl7GGOcC1NUw_4hPWFRMVuleEALdLFR5NdD75bLv8TtqLtvUA1yzHlv_XCrtdSFl_BwWBHoy-r4KrM0ukrbIBkok_s85eZZik7lDx3DL79ftTgIrurzwlWIeMs_eT6xyjMUehmcJzMTS4ycc1tP-ph3vaxU4X44XZ7rodWAJ3COhAbUwK7bHgcBvcYt-O6CB9MtlqDEKSd0R8xGguquEIWa0We8pDNsb9FqDwqOU9NtBYoggb22uu-s6ZnOBIwo-TxCQMjHNydDJF3Ifj_111qlXOeyvj2VHNMiC4DIvEqHT_65_qxQ-HLHaGh68OdHIRCWdMy-SsQys4IoZ8v87NhLUAS7FxBkJeIFtBqciLZKxpDkf3A6pyq8LXzTXR3TpaZq2RFSNhvtLtCizlz9dFa30l9yr_B073VqbAouQpFyDaNGFyQTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🔞
وایرال شده از رقص و شادی سربازان ناو آبراهام لینکلن توی کلوب شبانه توی پاتایا تایلند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71262" target="_blank">📅 10:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71261">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b860e39243.mp4?token=tcKmxo_NxF9z6EIsrNtFLJMUuBsY-dYXbMYlEINmVnFRQz9r0SjE1GZ7urnxmO7R5z831WeQiFqXIYbAyuK5TE2tRYn7SLhWXD-QfU3ApoAJB6E8JyCuyn5CRrrKh5EjpM-ILKw7MeYFKspqymHfJAV6i6KOUgHAEbHziof5JARdeYbU2YG_0MMoUkq3JIu9Q9c2F0YmrZa-0JlmxvH23W792kQPFTSljsEwiE4Dxk7ifgkbtAUUrpaUISN5l-VE8oYGXA0CRch6nXucX3ze7YjlWOmGdBwmTpStinf06jfW-FmNfYRTmmd5sLRs9s033x8_B_7VmH-FL5Cb8bLCDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b860e39243.mp4?token=tcKmxo_NxF9z6EIsrNtFLJMUuBsY-dYXbMYlEINmVnFRQz9r0SjE1GZ7urnxmO7R5z831WeQiFqXIYbAyuK5TE2tRYn7SLhWXD-QfU3ApoAJB6E8JyCuyn5CRrrKh5EjpM-ILKw7MeYFKspqymHfJAV6i6KOUgHAEbHziof5JARdeYbU2YG_0MMoUkq3JIu9Q9c2F0YmrZa-0JlmxvH23W792kQPFTSljsEwiE4Dxk7ifgkbtAUUrpaUISN5l-VE8oYGXA0CRch6nXucX3ze7YjlWOmGdBwmTpStinf06jfW-FmNfYRTmmd5sLRs9s033x8_B_7VmH-FL5Cb8bLCDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم ترسناک منتشر شده از یه بیمارستان روان‌پزشکی و رفتار یه بیمار ساعت ۳ صبح بخاطر مصرف مواد مخدر شیشه، گل و...
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71261" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71260">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=SUKgYjpjBMQBt89vs8sAK1BMaxwifi5F7Zy_E2MhhykAHeRSMLoKMpaC19ApuL0WrnYdNnIKetbADfTayMJWS-e-6i7YjDsha7pJbFC-52YOLxHLWTvOqfd4X8-ffo6nB-9Uj7kBFScf3UcpD7Pr0jp4jRIg4phhnbdMMD7yjL00FiEy-NFeZuQzLqLSTBKdbbXx2x_2D8JF4yHopk5nPhjXm8jMf3hFCEPVpghvO5CdgRPyxTq0rwGENmPOar9M3dvPENcExt2KQVG5FC8pNMehFbBgYGWqmqgSwC8dBC4Cz9sBHOwiu8GYaXXHdJNM-rTYAqDtsex4bkbYbbengQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=SUKgYjpjBMQBt89vs8sAK1BMaxwifi5F7Zy_E2MhhykAHeRSMLoKMpaC19ApuL0WrnYdNnIKetbADfTayMJWS-e-6i7YjDsha7pJbFC-52YOLxHLWTvOqfd4X8-ffo6nB-9Uj7kBFScf3UcpD7Pr0jp4jRIg4phhnbdMMD7yjL00FiEy-NFeZuQzLqLSTBKdbbXx2x_2D8JF4yHopk5nPhjXm8jMf3hFCEPVpghvO5CdgRPyxTq0rwGENmPOar9M3dvPENcExt2KQVG5FC8pNMehFbBgYGWqmqgSwC8dBC4Cz9sBHOwiu8GYaXXHdJNM-rTYAqDtsex4bkbYbbengQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
⭕️
گزارش‌هایی از تماس‌های ناشناس با ساکنان جنوب ایران؛
درخواست برای خودداری از حمایت از سپاه در درگیری‌های احتمالی آینده
بر اساس گزارش‌های منتشرشده، اخیرا تماس‌هایی از مبدأ نامشخص با شماری از ساکنان بومی جنوب ایران برقرار شده و از آنان خواسته شده در صورت وقوع درگیری‌های آینده از سپاه پاسداران حمایت نکنند.
گفته می‌شود این تماس‌ها با کد کشوری سوریه برقرار شده‌اند، اما هویت و وابستگی تماس‌گیرندگان تاکنون مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71260" target="_blank">📅 09:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71259">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71259" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71258">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw5eUotKrfslKlZFJEzdSeiq_Xqb_uMnZV879knYabswXnAbKU23gBMsuAhCCJimJ55bhWBShfUd_2UKzNLKRXion_XjnuWAmC7ypQyT9k60tlrCy2QG9wHQIi4vHmsfJ99rrNQGFnV9ADhi5r2jbVAPZoc0X8sq7Ek0klkdZR80giLj5xe8aw7pan81KsY_e8dArn1y5-t1rUek6ZmUuuqTQaKRPvmwAR84wX8e57q1_R7blnT08A7H_zcNHT4LG00VZ0RUnxi60y_73oUFTGQQZXSBdmwp74Fu_Cz45_Lf8sk9EiZGtZ7g85tMt7NNUmkuVB5IAtJ9Av3SERIzfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71258" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71257">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕️
⭕️
از دقایقی قبل نرخ سوم بنزین به 10هزار تومان افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71257" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a780504.mp4?token=UlOy1yR7vl6FrraywLjkeBiVsoJGOvvvboZRQs6hldXh3ynTOZutqsvZgfiE1cIgI5F6JZp_wgr0qBc8gDiAfl2ZftAFULQGcaP18m3LhCKpBsRXSeJKbn8ub-fPxKW0IX3S-aoRjbUaOrV9VQby7aJS5J1OQqfTA4RnTGF109BOqQlFVdua05KXXpbOoakLI3_KQKoDTFRoE8QX1pvFv1aSaV1q6rGF5SwjCHvlIvmTSYlb3s3YGSqZB8-ki33suW-SjiruuE7xFYkSR5kGBb4rRpozjNWEMrin5rUYD_k2aKGP0X8pUe6Du3SuO8n1FDRmIfnAPYrKHO07hjWh5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a780504.mp4?token=UlOy1yR7vl6FrraywLjkeBiVsoJGOvvvboZRQs6hldXh3ynTOZutqsvZgfiE1cIgI5F6JZp_wgr0qBc8gDiAfl2ZftAFULQGcaP18m3LhCKpBsRXSeJKbn8ub-fPxKW0IX3S-aoRjbUaOrV9VQby7aJS5J1OQqfTA4RnTGF109BOqQlFVdua05KXXpbOoakLI3_KQKoDTFRoE8QX1pvFv1aSaV1q6rGF5SwjCHvlIvmTSYlb3s3YGSqZB8-ki33suW-SjiruuE7xFYkSR5kGBb4rRpozjNWEMrin5rUYD_k2aKGP0X8pUe6Du3SuO8n1FDRmIfnAPYrKHO07hjWh5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
عادی‌سازی سقوط تپه علی‌الطاهر توسط طرفداران قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/71256" target="_blank">📅 23:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71255">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=pfJsJYzM_AAvIqvKIzgp_MTVQlyRycBh7P860BCDCOt3rHl70XD5oeAbWOnZ5_P3sLgHUXbTbLxFaB1BSbnCto33b_9zx2X9jM8MTlthZi8rCMuNepeW9N2ftNY-4hmIA-4D35RL4_giz3YMt40Y8C71DCTlFu0FVgGns9pRxTNbLARcYH_mzI4ywypirI1J3acgLI7BsWarAGw6A0CZFnUgKJTYnq4Wy0nv3KCfzNX94WlIUTa6_-66llFIYpatRV1OXidF3ixd7pWmzkhUt7Uo8T5YK9quh5lLuUFrarqJhtssk0r68eSeSCr9JBEyuBWrrCf0XHBHOQ9Skk4Xaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=pfJsJYzM_AAvIqvKIzgp_MTVQlyRycBh7P860BCDCOt3rHl70XD5oeAbWOnZ5_P3sLgHUXbTbLxFaB1BSbnCto33b_9zx2X9jM8MTlthZi8rCMuNepeW9N2ftNY-4hmIA-4D35RL4_giz3YMt40Y8C71DCTlFu0FVgGns9pRxTNbLARcYH_mzI4ywypirI1J3acgLI7BsWarAGw6A0CZFnUgKJTYnq4Wy0nv3KCfzNX94WlIUTa6_-66llFIYpatRV1OXidF3ixd7pWmzkhUt7Uo8T5YK9quh5lLuUFrarqJhtssk0r68eSeSCr9JBEyuBWrrCf0XHBHOQ9Skk4Xaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یادی کنیم از اوستاااااد خانعلی‌زاده که در دوره جنگ 12 روزه معتقد بود جنگنده های اسرائیلی هرگز وارد آسمان تهران نمیشن چون باید چندصد کیلومتر داخل ایران بیان و برن و این کار ممکن نیست  و اینا همه شایعات مجازی هست!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/71255" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71254">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71254" target="_blank">📅 22:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71253">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
⭕️
دقایقی پیش صدای چندین انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/71253" target="_blank">📅 21:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71252">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead429175.mp4?token=u7laNZhZsG14Yshgm7Ym-3vAJS5a686WN-8lLVZvXnO7c9DI8TLoH09z6nCs5i4MLVv_fdeRJCPzVvH5KUnpyvm8f-70VwQkd6vKYtqPf4x2OuWaSLyW-q51TgABhQlvWmGEJS5q-x4L_9Dx3QH4RLU07CuYXjCBF7VfFLR9PB8QsMN0cnxrEiouxY8ZFwy0llueiaTg3qgQn6iI0lOdBDU1_8DNKhgsNbHmdRRqVeIwvb8ydB9X_UsqIoLkwXtamxTj3_CT0wxnEVltv2rtElMoe4uFfHtNi1j6KNhbuOYH79R_SvcHaWZC-kSSz2-eAlrTd69x3givb89oghrJLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead429175.mp4?token=u7laNZhZsG14Yshgm7Ym-3vAJS5a686WN-8lLVZvXnO7c9DI8TLoH09z6nCs5i4MLVv_fdeRJCPzVvH5KUnpyvm8f-70VwQkd6vKYtqPf4x2OuWaSLyW-q51TgABhQlvWmGEJS5q-x4L_9Dx3QH4RLU07CuYXjCBF7VfFLR9PB8QsMN0cnxrEiouxY8ZFwy0llueiaTg3qgQn6iI0lOdBDU1_8DNKhgsNbHmdRRqVeIwvb8ydB9X_UsqIoLkwXtamxTj3_CT0wxnEVltv2rtElMoe4uFfHtNi1j6KNhbuOYH79R_SvcHaWZC-kSSz2-eAlrTd69x3givb89oghrJLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
دیشب خبرنگار لبنانی داشت توی نبطیه گزارش تهیه میکرد که همون لحظه به شکل پشم‌ریزونی اسرائیل حمله کرد به اونجا و همچی قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/71252" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
