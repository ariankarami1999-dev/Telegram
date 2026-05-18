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
<img src="https://cdn4.telesco.pe/file/iS-R2wp-n33KVG72K8R5OcLJ85vQEWTgxoeYi7yLG5WAlNr5_P13xW5Dn6U-LaNhIAGBwSVziBuCdKE4soeQrzOgdDsyNF5PyciallEqPEbLAgaojVp5N2QbH2jqefQYswCJINVyudHx_z9GDfIbd7bID1l6qnhQvGdv5FlTNcG7zP53seKC61EOyEByZovQtTCcJ55drY5zaeTqR0qIYOcxUqCQS0YHIBh5MFgvGuZF37jVD8vUCfTPjR4Ve319JyMAMIbwTA72k9HalFEC9OSBYk0hQWEpoiOVbo3ygtPl17RSHQBZ4Q5htbtFVYhKOvrjeRtmQwQ7yVuHQrJZ6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 208K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 17:08:29</div>
<hr>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7dLWrHg3zcsCQRVGlBaIRQlDEUZhlIXTZm22mwbknvXQ5XFLrubQzwIEbYCXf9F-7l5bfcrUqVPJCHuI3BPeDdzDUMnkkDoDlgKsGvkGbe3KO7RU4DSP7D5mNvBdZVlJ1SDFk0cCrFxBWFtI6oMFyx5lsuDoyikFdG--o5JJ7gUc06Vri4CpfqlbTx87llEls3FzfO6RbHDW_1T16GJmTDAgmvz4vbQgffuIMe7Vy91mDRJwjVARb1IHDaY3BRPWETtPKvtejVa4hV9c5b21xS0td7u2seTQBxEPxpLVCbd1_DWhA5JFQP3sVJV4lU1EoMxFuAY20k6JXh4Da4ZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=LaRG8Ru0GTbhcaYbZuOiDrWBAeTjOBf9Km41L3ZG-oZyBUqeou8sU9I-phrgOzBep4tR4oNPRarwLJgSQZYWxb9uQg22zN3Jn8G_pNkYu_y0QStkP3BL_v-QWVI48TybmMlePoJuUbnXVjVOPSwZ2O1YdHyPSOs4w3axqoX--4XM7b9E1exN-cslcsbqKxp9ZSXNJBuKzKYvfFabawor8I8oeZ_MlLtzrJsXxzlAY6SPkduQyve-hZzzM1K4Ik9b4A1_qyfxXy8O56LDmjrLHHw-DoSz4-k-LpvLD7effeY5Q0ozHVYBzeGe0KBaxBZrjlu_cSzYujMagnUlUeWWsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=LaRG8Ru0GTbhcaYbZuOiDrWBAeTjOBf9Km41L3ZG-oZyBUqeou8sU9I-phrgOzBep4tR4oNPRarwLJgSQZYWxb9uQg22zN3Jn8G_pNkYu_y0QStkP3BL_v-QWVI48TybmMlePoJuUbnXVjVOPSwZ2O1YdHyPSOs4w3axqoX--4XM7b9E1exN-cslcsbqKxp9ZSXNJBuKzKYvfFabawor8I8oeZ_MlLtzrJsXxzlAY6SPkduQyve-hZzzM1K4Ik9b4A1_qyfxXy8O56LDmjrLHHw-DoSz4-k-LpvLD7effeY5Q0ozHVYBzeGe0KBaxBZrjlu_cSzYujMagnUlUeWWsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=ka6yU7aDI0SgnwDkEMAz2_AU_ovHKAnXkEeVvpWwEX_nMivdrB0CUNRiVTMz2-sl9-yZGQNP1ieBzzwa2rJ51npVtwqzQQFfDabF9HZlzqvUDUkKnzFZupGNOlxUIA4bLfPO0kLf7vT00212Jqr4omfVpmKla7GNmrtRwmamt4F2UbGcsiHqIHAKEsYgSqzu9mRh0O4ejQhOBcSKS2vhDnjpSGeTKeFvrgT-WYQDfhl3csZIgmM3dKnWgWQnuL3ID5CvGjNewIKDkwb_kojGnH45OykTVNSaW5-z6t23I60ggY3gotOuzxaWwI1OYzkjIvsgKb6dBtkxHBxIchvkEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=ka6yU7aDI0SgnwDkEMAz2_AU_ovHKAnXkEeVvpWwEX_nMivdrB0CUNRiVTMz2-sl9-yZGQNP1ieBzzwa2rJ51npVtwqzQQFfDabF9HZlzqvUDUkKnzFZupGNOlxUIA4bLfPO0kLf7vT00212Jqr4omfVpmKla7GNmrtRwmamt4F2UbGcsiHqIHAKEsYgSqzu9mRh0O4ejQhOBcSKS2vhDnjpSGeTKeFvrgT-WYQDfhl3csZIgmM3dKnWgWQnuL3ID5CvGjNewIKDkwb_kojGnH45OykTVNSaW5-z6t23I60ggY3gotOuzxaWwI1OYzkjIvsgKb6dBtkxHBxIchvkEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5cRdVuBCUAeEipfdJHH8X5_prW65t1BaeYNsNs4XrERQMY34DD8Z0ehbC5Dn91O5WNqn4edlrF8w0dVmnT6aCmgAR0i7wgKKAa2KuwzghH4JakY7fUVv-i_BQ-D5IsueZ95W9U3nb7vhCn22Fvky8yGT16VrlloSVpPm_-IM4nW6-NN4jhWihaLmiHMKQdY_bYt_lf9ddx3r3DSfWWEbpEA-iXJiH7LZoPaa8ZDTNg5HGZKKNaxRQMe0Agx66DvMfxi2xAbXBMySuoTY8r4OZUiJksLwrymaVGTTpRbj-gtsS7xQyFRrSy8J2s25FdLUE9S_C-F4QRtSvAl7sz2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y900wnun-3-tv5y-Zb2J3PSH5fXG3N-7ItCe0uYTi6fW6wsGJIjrI0dBw411Kortg8qyx9LgDjvOari-FOjrj9kpITafdCWBEGaK9tdFFqMp6YJWfux8Fop_4UNbuhGNN2KBYYFPV83inS6fxqMfrlUOI13Xf41lk3kB5tgfVrsmUkLaG976Murf7Sfu0Gygxv4_UcAM9eJAJgCDgulj3rWO6SCghVt_m8CAHDycYuvgKuqYBGckObd8yIAd2BbEHCQ16dW4fgtdEMtFAHPgmxcGmZsb-c-cZfbfxUHiPPbAtLndg6abJwKT86JoAffba0YiRoqZ2H5eg-jPCivnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxV8dymgd6U-aTBwUBvHk25QSuKAy8NaW5W0h6X33xeUudFOGqpYFA1beBHqto4sa9--wuPbu-7lkt9tbIeC3h0d39MdthpXW-oERjpmQt15eubkGinYtdD5jZmvBTM57-aFhJ9H2WxzmaTXBcIeihbLbpJr3NYgrZCXgFf-4lPabcSwozFGR9cLQmyAH5r0JOT_3AbnRJ1KveCm-SEGEPi_WGOBdZkZrjFDN3LBxAGyFtJLq6enQfsm5TE6GxAemB99NzTjNuqdPf3TiujoDOsUSWjJnS-aksIefpBC88iVLCXnnLYqg2eYni0yeMkQZejEOdAE88YN6A7frKBjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورودی کانال VIP بتمونو رایگان کردم
؛
خواستم یحالی بهتون بدم هر کی جوین شه تا ابد میمونه
💯
https://t.me/+--L2Hz5HpiY1YWZk
💎
#تبلیغ‌نیست
💎
👀
کانال وی ای پی رایگان برای همه
👀</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/persiana_Soccer/22166" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIfP9rLJD2YNNE2EG7FPmCNLz_5PCrsSGpodtjB5XXiWLX9S_YeFeWeYrvAucG0oUqYLqD1PHN_2RfEd6_NoV3g_x_WNo7taWRIUi5pEDBv4SCZoBxsHLbar7vmC2EyHkmuAGlq9Y8kScToy9MIQaUjX6UpfQQ5FK_gucdDfKlREi_xvCKMORaBKBQvkZp_K5TAzHuAhQSwckuRTNhjPulcS_0Mjc8LhbFU4ofP_jSijIwANozkTOdptVY2Q-VGCbhLde8Y5q1qf--k49LshvaewE-xjramqqeEAWAFBSFd-yAS6dQXQe55BWtfcVk_181LxmOZb7Do1pJrqVAl-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGLC6fEF3a0pEh31JEifn8mHJighW88fTRVX4nhGiJBuRMGkv3JJMqfaro6wfGvI-8m4xzK0JnZy6_b9CqqQB6jlCYhaNwONTXt5Z4uPIat55ItMWlPn1F2o1nnRLFlMmSKiwsV5j-qdUjJHMkxt77P7rejDNQvAW4mYalE1knBkX9-yIM8UUuZWoai0nNaOUnEIOyiJ2syY7Qaq3Lsb3KBpSyULt8Jh8SqEhtl93q_INulWSqVPy5LK3pjUhmEnrL2u3K-8-KdHu7lWB9FwikoJBHK2tT505WwyzOYUjNQuYA8vFeZF1Lb1Za80ZdP7FziV7BVMt1uJEGzyyPwuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIJKVMoVGDwXhrk8Wy-OWnvfOkqBYkspHjQDLdwTEZxwtZA2SieqQBPTZ7r9zLYwefzhbltVxarUUSxb332fkpLHLK_-oP--PQClnKexJcp1GlmqkfNxhrLt1WW_cLM_yrh7tYBPeEbgWShmXeZj2vQK5lshfNNkACTgedojiBczkDZ5TBmf0iYwKmr71ygIs2IYKcVsRl5_KrUFip4m6KbxpCd99CwSGibpChW7Fk5O9D5A5m3NCT4mQV3MXgF85codV27uIX5UEzoC4UZNB3KRCI7P188NItmDE02ljGRdY20_HsPGu67X5FZw1jfz_wnL4E_OixJigv5d2la0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCfbJCDahA9sjTq5M4frCjkqHVr0xPnt_6XyaAvcOooYLjRFVJb2sr5NAOGPZWieDr7W85amSHBms7nTyhkhmOGGIqADd09aNmYVSCqXlgUtlEHNtOX7xP3mH3_p6VKEpYrLsBuUsyxhX2QKh5UCH2Sc1zhAMCukjEDMWG7V5sR_NxENM5PnFmliNu-qhTxuXlNP2-bhigeUhcL9kQ9rtJsbNV2MDrV3A7Bhc7iy80i3NpgAvfXZCU-EO9Z2jtGkh818IahXF6YALTG7IHtztwNyRXZaTzxCnTUbkEWQux54ZfPO6f33thJfKAPTIib93ddmoIpGR4O_bybGIAU1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
⭕️
⭕️
بچهای پرشیانا
باعلیرضا صحبت کردم هر گیگ کافینگ‌رو ۲۱۰# میده‌سرعتش واقعا محشره اینستاگرام توییتر تلگرام به راحتی بالا میاره
✅
تضمینی
✅
بدون قطعی
✅
بدون ضریب
✅
به همراه لینک ساب
✅
سرعت عالی
اینم ایدیش برید هر چند گیگ لازم دارید ازش بخرید پایین ترین قیمت تلگرام میده
👇
@Alireza_mosve</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/persiana_Soccer/22161" target="_blank">📅 18:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFK8N4wp8VGERj2ZoZempEFXbLKUrue9ESKN2Gz8ELtT9-Uw6fO3Gg3nE400SJDDfHzwVd6X7mJ-pNNJkoSU5YwPNZXN338WpKCrz26UELUJZdokF26pjEdWCFftmlgeipG88iuYZwvC_JW1cmktZa9nuJW7-kjbSRmnf8cuj2Q5zsSuDN0020AcA8JYus-Nih4225Bbgi_z-jseG9PwHWvJMkT5jFD6StwKCfbHxJogNZ9N1QENNiwoScu9IBXZwDKlzAJj-etw_4u4ll9VCp5sKT1lQAcOjl3XGbrmkw9P_2_14DIJlJOIbrPoLL2rvydQoQB1oiggSqHUIfyoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6zhYLla02CaW9Z1kLzg7R-Wj-a1SQsaRugygVbixauW1oMjJuNDZbN0WedQC3FHb-u6J0dfyDO12WT2fr_Ml06o5k4zxfOLRjUlhsRlwsWz7f7riuFC7tMFJDcyCjVmLEFcaXzHDerCQXdSPkVVFxPmEXwBjrhR7IvRgyzzyuk9gl9UH5-vcAJ3UeDg20ObHsKUa1YevhjEE0_tfVDQXdWwemq2103uPXqRi70zfUW6pUyUCyRLzWNcuk0sPtEUWnYmKDUcMC9vHvkQT-HQ0hRnefoN-Pt51Ppd7FUQCIkY4DK1HoOLsxpybI7MxFDXZ0Kb8WTAxk8ZONMtTqwCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBkHqhLp2T-6MhyjtLZxHZFZbNBkB8X5UYoLZWXWaPUe0H4VjJ_iOAOSFmJXHRl0zXZ0XSyV36YHhhHyHccbNc3mTancajbP8KFivfuJAHuP1V1ppwUZpY_NpQxav1pbvGhTga7GrGcny2nNCDJeV1TLwIXGNljVwyV2jPYdnlfOz0dIRPYY7x1mT8nCN1NQVvUDvm2qHVF4UxEZk9U2v3NmF4v4BJRQTWrs9ikz7diDN_sU81c56LPL55UhG9Ccg0zTifTEWMG-deJPubXVudmrjOfze1orXpCLpPOz88dJimbyO9K43ZKov0yzdAGjNvXdxIuywX9jb33vtdaU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO_dRVmAntAUHYOkP3j8i9oA2dRp8Oa2KAY9f87Fn8h4a0yFLbLQ1s1nDMyLaFPSNc94mVxEzMM37tUfa4Nac_bX68eNLi_LNDk0Cj-W9mzd4DU_ubVq3d91Mw6opPogbTmQxET8dg3xTGqnc778sw_7GUn2PE6cHjuaJy7LBxDgT-vL5QtBzOOglklyR3uJSI7zRLONj4_rzrxtSZVlZi4mjBR981YJPkZfticsjU0QV5bkS5EcuYINOohAahWxmBKkfW-nf4gQbLdl2Di1nFzOxINPoyCZqcUFReDN8zlBfNuMhD_DgrU__GsG6S1OInv0Rb2ewSHS_t0TqwUGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzfuEhJu5XQpgUjvBVLoynzWIBGbrVsQrYooYfSzwJnwG7pQx2gihvlZhzmtVypRblxgmN7uoN1UX3lWaTspXkkz9WX9KYvn4CXt6n0lldX_uswpSRmpUuFK-FOvQKFK5Ur69nIBlQJUkCnDhN6wOnjQi5MMqYUoJGZ1ufLL6j5aD7dZHJH2zzs-vr11VaTm6pjxJ3eCyOu-BvYUVG4VeWSqxxoR686NeZLoS8m8ISU15z9o5-kjVzbLWmsTFbMgeXHjrwtBYPBqzsZZxme5_Hdt78Xc7l-CkPv98adDJv7BgqyQQ5qOwtoU-4u4PMRTBJPN4AHDJa5wb4N8FT6aMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCYc6ECHk3SLagFyf3Vf1z628GNBxtGXP0FAeV-ZE98auwMPUWfE0Ft6dHqe2KJnELUK8Zqpz9WPPZvZEWuP_KbfW1NG4vsitxX9WmsvBbYyOm6-w1cRquQeVyqCdb2ZPowKkj6hAhY91e7jUcz4zFvtBB_dtHCBe17N9KwSqBFK29uRMAN8WyL3SdFU_cIxTZ3fyOvhHGTMhPFR85wq-Vv7CLQ8Ji34Wf5axLr0QIaT7nIVON-lByCsBbbyC7CcnHys88JFBvaikZclskXgFmMlgWOLatdo_wlCqZQNVQm_eWw_i9R2q3diLEJ8UZczAhJqtnF9hCE4uGXjaIlhGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRab_-Ge5Hc3eFJoIujQp9cHcxwMq-w5fXGx601nwIaTcyGndKX5Q2Idq4cu31zdy4zXCsaIYex6esm51zMvDtQDI8p5yg_eJScadFLiEYnunTQVzk4JpnxMdghGj1NrAQxmo8JKtrjE_l3O7Y0xgUhS6-qTu-CjqWA2KgB3hsImqGTknX9D3R9G44A2UwyTEZWBepamuJ3emSSr7bad4SEM7yfv3eLmwxhbkc4zW8KSw_Ld9_qJS4GyVlXN3LZW0TukPOUWT22bC3WXmdyYA3MeAODezC4jd5KDROuA8UxYOHxPMyHnWlkmXwUsovZgKMfnnGCXpwN71gx0XVDF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0sgxYv_PJ-2R6N0YuqjZpH7OcKw6gHmqH56Lw4oxUHzLik_SXA_Hx694-2IHOyXR2ASSrw-3JmDs-d8n89HyuUD2m73jcai4Jx-J5hCgmpuW07XvN4QbNJ3bvdl1NeRZCtMQUGlAmlxuptA6RFp2EIiXoIsBpKsog2obIODoJBx1IxFwFUFiXXp8D8vwYNy0KaQ7ZGyzfrE37eSiQD6eG38y8EOVnGM_fRTK-MYkUcKq0OW3_YTwN53cH-NmKFa_vltnpv_Aw_38Rg8tczMzwhMiLTfmDUfY3SF8h42BerVwm_NDBq3WSQc-GwcjQDeKqkC7r6JI-WTp4SfChPaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ld9xxsfDx93JYc8hGPSZAjueF2H2AKf95VhhUHZAGoKm0QlzsUd9XABpFW_82upH5VePS_t8AwReduQ0c3QKmHC73Ls868xawYccadbs916QU8087D2N7Pc9lvOVQ_kFgLPhcYqLntuce4uyK7z7BdatCec8b7f6ArmMZ2TCsjJ3e1OEtfLBFBjn_D4cwEvdwHKZHEnmwzWVakoAGnvZBikzvzLo-WMKdXF5tp0IxvX3K-AN3aPuLaU-nqRBMu2vPNET_Zewi8bqj-CNKO_7urEnW5WS_XFETpPzbpAUMJOINVDBUtD5QT7mlDeQqLmMxzvi7vlTTipq4XDqVxtNlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22150">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
⭕️
⭕️
بچهای پرشیانا
باعلیرضا صحبت کردم هر گیگ کافینگ‌رو ۲۱۰# میده‌سرعتش واقعا محشره اینستاگرام توییتر تلگرام به راحتی بالا میاره
✅
تضمینی
✅
بدون قطعی
✅
بدون ضریب
✅
به همراه لینک ساب
✅
سرعت عالی
اینم ایدیش برید هر چند گیگ لازم دارید ازش بخرید پایین ترین قیمت تلگرام میده
👇
@Alireza_mosve</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/persiana_Soccer/22150" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzmwbqPKBrDzVeo-hb5yDIZlaktCuOIxbKcbWL8Xmdrm2oTqABTb6lPDEzxc7gLvP4bAWGdorjYp6IsJyPuLT6TMdYX89Y18tRxnI3pDn_wj8A2j8UZuHD6ay9SraBgC2vzN4J6wWhXG6huTNzvVoZCIl9Sw6LPnpVv2YUnIYApsJ1ihuTkNTTWLIB5DGIP8L8ANLX_mNHVlKOiZNT_Nlu77Vouqb-374-DmbmMFvSpkyw4KSW7YVbTVBL8_hZZnSyeJuDGBtvxEm-SVK0h1Bo_Z9vCsbTtQJlQGWyhsDFaEk3QWNjs_00TBNfKe4GxEQh9n2nNC3pv7N9PTcJ5p4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qY4YhXgJPUyDaZF9JCjOXkdlsX_HYBOdmfuL2MJ2o2YlExu6OHe5Qhb1F391mpiUAGtnI_Btv-gGi7aJBFi0RACT2XJw9ssCn1cDqZpq_WmxADoe6rb5haQRc-dHoA18l1gnHkd-P10Y7tMu9_aALU5k38m2anO6msFlEhJtyqBOwQY3jOMAM86D1nf4azr1mhplfK424_ot9bLVZB1esPqIXlR6m--Dk34fLU1qlli5tTH8eqBDZ__LXeYWJRBgCftYyJUCF4ZGpi35pWVSKLqP0irwABzKqYeBgNQtZPG8iSh7-kIxdj_kkBUph82eL-n6xNeE7Zrg7FpL5xtyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIiXv-wCUB1JbDmedOigfnUea0_NMYNSxb7oT4LxzG4EYM0_3DsoVQnXaOv0LpP7WYXvHU_18uAEafbhddKoJDxhWFLe373gBqNzZyRhdKoBvlvidynO8OLAVKjoxxJ5ESN0X1MbXvipXOLzCaI9aR4ZrQ_-y104kelvyrQfpUAf3fqAa9hUPsKathVRl1CmY_v6ESBU6ZlWAbQ8cR-deqcmAxcCjtDFCSki9eEW3n8XWnnggIPB2FvVBn0FOti-66eSmB8Zvh6YWqOovURRfz_kqrklRtMn3BQWbxQASfcF-jBiA49JlISFu2mKBfX0E3jWYc3S-hknHReT6uEHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqEN_IiLc4dv0mjj4CGSPW4dtw9L-hj94coRXJFAv_0No7Kp0kPtJRcNT1VLO_TaL--eVmHGZ0xZB0JZEhzi41BIAQnlfTZTANb01T_bxOCjxhq_qgu5bV-07S-59Bpsq0TQunIzeq4wf9C4CasKMhNRcKqoU5m5wlf9K-n5S5I8kqHBqS13khmb-9IuciiU89CiTyP_B3jgsa0ZU1XT70dMmCz0_SsbIqnfnq23oKxrKi1ljxWqjtqLin6-aNM0BH_G4aiE8OYq1c24LBEBxIJJJ38SDDrv3KB419zL8I0jLNFz6q0mkaHChM-775P3WORU5FzgEZFjhsfG_cu9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_kg5hK9j-wvmTe8CDkOk_DcK6fT--evejCIJXeOyyxzqIHcQjI7SrqQTpqLu9IoQ0KxZPxDU7Vhn_1Lbtd_VhBNxqD0wNWH_el_n7vi8U6weleLDITzzWY8HRQ6B3DB-l_Hou9aGLhPsF9jApvZti4iyfVQ30kmkD1YfKZf4W9gkuUxjnJn_NqyFyiWA4EmTzc_6UbgqCwFrH6YBDcO9mFogl6005UAOJ7U23-AMrYjpJht9e23rWcqUE_tclRb9oLI4WTnmbFwBzUG9BgEp0KAvuOHLLsveMuKuKA4VUW6eWK0U-9LDVp9vKUkBL_YxrZzBBORP6DeioCs-AGDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWWtjWWzntpeyH1l0hgRP0MUrd0EJ9K7Dc3X_AGl5MoN9vNKiorNc5gbM2x7E5r6V20z1Vs18ovTtueWFvY5rm89IbEJNRMbJwtJSEXQvTVdqO87cCtXrpucOvG6JQ5IzH5QQFjXTEmvp1k2-XVaNg0VuhuVZREdawnsPPZgpuyypGXzXafjDy_M1g10omzbtq6-nOwtqVMsn9bRx49FfUqvQDceckIi3WzYSnuGs5qoNmuV1qQZ-9Jow0f5bS8oeX_3LjMsPW4_hQ-nFyG_-VdmHLmuMEpu6p-djIOTy6_vSAd2VpkJlBWvcCjU4U-djVcIRtAKb8UUSDyJPD3t7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJwqMfz6FLXsoYzdjBLlztxGq3SYGalpzLxNURuaVm8sctj9ck7XkYPosFhyGWqiJGQSoIm0CVm04sN60Vw4fJcXmsi6mp5853QE553C65nBWYdSKCqLmYnA87RnIvxmPEPRGDSy-z6ab7UH8rIql7Qt0hRZvIzLwSfv7kLUrxNrOHLnvIA819LYG0ct50dYGhlj4vnhDsLfqCyNj6AgFftvlQcMC_SpnIZvHtHTPfMxrW9sUFZhlmphZagEfZnGjDeb3G0L_XMNDwRWrU8lOnLWs4KbvlCyZguQWM6duXONrBmJXybvuWEZv82_eDVJK0sD1Rjp9FMMjMfByG3z5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agkUNmBcuDsRvbgdcQ9BC9TgB3GUW-sLwCt3WVL0sx80mNzd5fa4Ecx6q8eqpCUjNwRDU9cS9ybCt07cM8UzTnCPboSwRjr1t-leQMlFc2ocQb5TJ9nrXurjQ1h97kc5f-R-71XKKfYp2-_DaG2kOFp6rBx86zjOBAF2HJ-RgvLx8CRNQAEOdQnpdTLQXsidJvqWpendtltRcdGxTknaBaG1faQTZJQOq3OTtLMNGIZigcY2iGuKiHrdYaqUbixazKCThAwr5_e_FQLdcgROW6NkRVMTk6D1dGqwZ86Z0QsmPdECLh0iWgMnW1WWtFg9m4mgXHU66nit5hoDXjt_UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeziei-xmzm08LWlDmBWRza2YWsA3lhUjjjj_LLGLLwAEOCAwR1VCj9QQxlDuSBnK5QfwgZ3YAyneFZBNR0zD2iTFj2K0icqZN2uahq6WTeLlSQauFB9e0AJ2sqmeGFezKtADTGJiEZO9kzV7ECCAJpIkSOquiczTwpKB52qD6jXcr5CdAer_W3zfDNbIpJW3JlJIB4sgso7B35VB09Ui39IplyGeuOHr48_ime3sNfB4A_E2dts0shsIxFaE8VD9dzS6JFtXElpGx0k9gJE20o9p1bvXyDRIck-LdMAZEEFNqLrNulfl6xOrFGaIasl4E9c5Ldhih3FpaduYXMgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQYfG2saVtaJ-jh8BIAd01BiMvrjrZcPU-SsYrGweFWAsAQribXJJJiafkol11P6MSIvUUWIusQMx7YJweZh9wZU9gb8IJ8VZpazzmu9QGg09nr1yNTZ0LIZf2F5bTBegrIErk0ybboeDIBun9bdEEHLlEvuczb9vqCfd5vWW6aLAytjDoywoo5oKCfM4lLNyVpxrHDk-uScdrBUkQeEXQZ20CYRY_EMwLDkbqB3Y3t3k_owQ5cGbCBlkx7B7WPDCqIHfeHKp6pGqyU9mjC4k3bXxrIe7i6_Eu1_d2ISgR7laZWyaMZton3CU0dxbp3u25RL_8nORJtwxllJLzPq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNoP2KSIfU-wUgijflXMzmNkwVviMPvyp9fyWZrxrIRcVGaSKJrMmP8QdpFLvLNvP0mOrJPwZU5cGvQw8fc3PIaeQPQ8JRISKeePxjzpYpGBtCHbxoZowEpcxUejTkYh8F_zXS2Xwh2gwVhYeZUO9NPBZUuRdHjaNbZ6fq0aQwLwv5eielEJTsUJKFi8og6gm_ycRL66FKD6gKJpK8DBd9DlIX_BszrBAyr_zexvOSNFVpWoa-j3yV-7RzKpcdbBLypjUBKAkLqvekunG-_hey9IbkUpqQQd5DVQPOIb2tE5dYoFhxu1LsRj2e0QAkMZ0NuPcyb7J6zlp9hlkTQBMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIzzl4ksDnjSeF59mB5CWs1TIMNmAEjLA_dTdJ6Gk71Y8tSMM7MS9_00mTeyf9fyoyjAwWgIaFCCpbB68YosOVMYan8VqYkjiL_YXFFCqk79Aqj12iSJUZWBZxjgbBOJVxOARx53A3XED9gqySH6f1EAJvMrOvOAOiL1qPg86kYRa74DUKekDwS73klW9Xvg3xLEYKil19BfYw1DBe11rDHzehVDEdY4PYJOTV9lWe29VVCSg4BlO5eUEClHR_TvDv1vR1Y6onh4DBTtZM21lUqJyfRKnIVfSBJF47j_SMHMhQXmMpZ8Snq-hegV98C2cQEmrE08YL75Bxd-V6FD1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfUpmQAg1ZMiJSly7HbPMrArR6RmaT_Bv7jEB70bn6iFKIQYZM4t_mwcq34fnyNbfM9HLnosECY2SxYVzev_9YXOfQa4ty_Ll1vVmRqE4Nf0gGrGo9YlYvrFvL7pRwZLkk_1zCbkFfskro0nHv6hoTbHz0_bXaGbeZEZANt_9X5QtmwIjkEJU_hv1ShbPxX5nlTBaUzHmVB-3ZrTTkvn9Cs5UzIQuyEclRLN_ptGS7HOIPOHi0x6R_wdnjmCQrynJHJfyuSbbyrzZ2olUxDQTItiULOpJB0rRzQpq01qsLZJbdXX-sM47Q9hOvvK70AknId845eNHkF4mITb_z2cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=tJEnMVWJZ0JnjZ5bEo_8fZbphBK6pGRx6NF2WGuf06dFipE-ugaUlRfhRihzI-eYEXZWpV4HOXkxF_W3H2gIJxWMSTb6CXVAfe8vpeSIeK0b2lQ1Ah6niQWxUgC35S1fEpKJoAPCkyyRsAb7LdtN92mqbzAkB-vxNZZYAqX54Odwy_JzvphMmzr-nAYPNVE_UYT2nKbhbKp7gGHmMm1G-FMJtL5HcQcjBVKTFWBbf2vuCcz3W9znJSWadCQMMVgm6YOkMNsVQ8oD7TO2vOicFmRsvA4rSdRSDYmlswXATdA8HOpIhHCrd3-LXXgBKvyanAfrZKrCVbVBXm6Qw5BqxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=tJEnMVWJZ0JnjZ5bEo_8fZbphBK6pGRx6NF2WGuf06dFipE-ugaUlRfhRihzI-eYEXZWpV4HOXkxF_W3H2gIJxWMSTb6CXVAfe8vpeSIeK0b2lQ1Ah6niQWxUgC35S1fEpKJoAPCkyyRsAb7LdtN92mqbzAkB-vxNZZYAqX54Odwy_JzvphMmzr-nAYPNVE_UYT2nKbhbKp7gGHmMm1G-FMJtL5HcQcjBVKTFWBbf2vuCcz3W9znJSWadCQMMVgm6YOkMNsVQ8oD7TO2vOicFmRsvA4rSdRSDYmlswXATdA8HOpIhHCrd3-LXXgBKvyanAfrZKrCVbVBXm6Qw5BqxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHEIob0LKKXMoYm4cFXXQFbGkmTw9Y2D4_LRJRFnl5SodlsNoU7kca7YhN8Sr61_Ng7vRpSyCi81ZoyDPnkQi-YfGwJX4xYQFJqEcVkx_Kwyd_6lDqLBxa-u4EfgSAZNST6l2VPinaYaqKuG3nWJ96lPgM1hZKWksEKNQDvmrPf8RsIyGSmVyeaDKFjfloc2nEqU5FrKHfYtHSpCAAVtL2NAQuo4QLIWnKnTOVpW4p5eC8iNNfSyjeEDa2aYzoebw_CyVQ7jsR3jBE2iQxr_IcHeU6LczTHVdyNaILTfWYgnz2XYbMzpYR5R9CpRys1KciidsOzkJ8QxKk5a-mVlBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hdxf4Vr2C-lZcpNiNX49UAFrg71MoqI59r75ezifJtC5kP4XXAgc4miHNXDKai8BuUwGLmfsm0vDHEFRlmSCodqUFxvqNgxSGAzq_6Id4kNf0_26hdJ3to1gLHHm5iW8L5_skb9_CrElBPdx4UzQRzHtsb9STvVGGR0bPfmEyzVLirjor_8gOpF3hpZeHQal4Ln16MXYim68_g6YsGLphad1WWvtuVZnJGPCx5uDKAt9XVUrARPfq5QF0xqbEU08MB6bmIOyjMZxdRx-GTet0BCble66VOCkM3kNN0x1gclLn3-tnpfbRltca5wwrbY2u72V4mjSqCeXn8M7xh7oJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLez37EuEAtuav5NTlxAr5pXOvxIF21WXS2YucNW4Z9qNV2EDUCMwVDYG9qT6e0aEp9TsPxUE5ZaqNiuUGAEDqdGae-uvRXCtE22hWQ7kRRACuSEgA1MLsQuBMb05R2FD6ihMz7dEH5PklVtc8G71KoBtxdXnOeTs0gCDvh5CuRSI18tU9wG8B-trb3vXw2pyLSFWMsAcawevRu9ljEEyKkPZC8NWcfChOvIS_POOwuK23aOpMdgc_BgDufgLwq0ak65IXgjExKR9MPq2u_lanCXRgCtvzUcWX_eCNqQ4UzRNaBlQhrDL5wW8bdXzSKNbBKENL-zfI38XvNVsO82sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dub_PTcy_7GNrrE2Qwe9kSr6liDxfF7M3jqMR9DhkQlsQMNEO65o38r3VrBhRUfSBYUEMBl6INVh08ON9jQMqypjOsO3YE_BkXCHCHw-PbrusHM3FcRovPzMX146oWM8twgI9QUd41iXxcaDtTzye8g7cCGU8TQvQo3j9UpjiuPz7d3794OD_KFxWMwhv_LmW6qWkunFVnC7M3sSY8_Gp1VMYqZ1RTVbnWUb2YCbDBPJP1wLJgZ5QG03CbK-RDWuqsY2yhUNyXl5Krgw6lyTaskKF-7JaD6Rr67hI2matzSWVTpL2UijBQ0lyMdEELEKlUtOu3h0SyxmZjtIGTNsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_Z9gdE4EjDsvBupENjZ-wygnjLki6SBtO0uB_HEh6ghCXrqmTwGiMGZY3pRwautEMeoKs2FCm7Sc2X8CEbOmUhJCBgR3BO9tltyMgT7NP0ofpIko9UgIuuSX7LO6ncdwNSNzWgNyMvbHDALP1cBPxn-DmL7a4dGwb8OgFosRVWYkkWKEVRpmOmwP2I4ltLqx2ke_Y5v-nljzhf0iQqOKR3M3UkI2bZTViYq_dvV0gcANAR1m6joKGRfbzTuAGPM0iLofnAp6Al9Z1DovNncgYBssBvNJiVOCNimCFE8DvMiZDd7EF8XXbSdvFNk9EL9ScVb_wrI172qo-Rjg2HWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW3m3wx13Z2N16fKZhmXLAKSW6tlJFFZNZNebkxHvhfD86K2LTSiQs1tITSDZmYNGOtq6eh_tE9agC0FCOETacfYnKA13HGMRf8P4sXAoRRCqZpq63KHko60VpmZrNYkTr_4E808z8iiPxXIAqjm0pJNVP46tHaIP__02gZrrs9EQXVqy9w6wQce0LrJy5KKPblBK9S1qvjppShbkJHD3TSgAx55fxrjMDYUQfh3nowPupOmhsrGNVKIcHDwZJLBosd5zfdk7hxwWrTCWkc565TDJzkWnEESOKNh5vJRjmrx40SUjeHArP5VsxhFtfeqxVMUpcUnWBXES55wykPvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkMVRvUIBiAulr7q1T8vCHtaWnoOI6H-AV9D890q53n_CD34vBpuaT0urTYqCOs48H7hBxf2d3JUefvB-mPad7ByNd41ykgYzLvFxTwI41mpN5H2jTzud_8LHWluZzlTyhbIBi_vpFxKtL5FG7zkyuMx-bDvGm7km578igWGhFU1fRci7DZDEDodcZYO7JyzqdlHhd3aMCJbjcKiUDlOY0IHdVh5tEKi1dNcaqAQCpRWZ5PjQ4oFULYdE0I8ZZdwfzMljzhtrPpkj95Uf8ICROAZm2rr7Zbgtp70QaTc9kZBL0g25eGR2tmpm5Yh6nNfacAiG6xUjCOp6b6JGgRYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAnV1GYqqvF8OuhQ3Rcl0q9_yZnnWI8h25KeDVdkpbnhrxYdtRA2EExnXFEmR76V2NTdDFMRQv58FgaVCEFgANUFhs7upIu_yVXuqwLIK4pacCNiVWgATBA7KRtPM-OteEuradkbc1pAjd1CYwgSt3dUK94Ie71EweSVqF7pd_MgsZw6tCuTjAegl75q7mED__kS7ehopVq_1ZNJphBflwxFQRL96sPI--fCtKsXh2euLWzpX0vhLcXo-rG9dKf671YjcDfPTtKVMxySEf7eFz-0A3Q_CKtNodJaH1Tn4G4dt0TGb8BQ67qZfm679IPiU-qSlTHC-9Hcjf7M7yk9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=BS-CPeFckG1oHYOnedsZ-RnjZnYkFepBc2srAxmDnCnApLbexlPYheSQD9rzwSpgs5WMw5rpUDGtnDhHJzRiHhDmCqQAqRTnxUl21_21D0y06Mj9812o1-Niw-aUUmZzlMsNxnHqT80rnhyTYMFxMEwCH-DAUyhqI9hfbQ69TLIah9oLqziu2ZbCmEfGzzPVDdOFvawVnWbAHa0MOTtrQsTkMXZwU4lPm3_7z0Yh2cfS0NX98btu_s38rwrxhBRoRQ48WrEZ8Ou5aDr3b8L3cr8wxGxTAOM9PAXRn7s_m6fdLGi88Ntz2-57QzuOFPX7cqcbRT_GXs5UrwEJ04-9gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=BS-CPeFckG1oHYOnedsZ-RnjZnYkFepBc2srAxmDnCnApLbexlPYheSQD9rzwSpgs5WMw5rpUDGtnDhHJzRiHhDmCqQAqRTnxUl21_21D0y06Mj9812o1-Niw-aUUmZzlMsNxnHqT80rnhyTYMFxMEwCH-DAUyhqI9hfbQ69TLIah9oLqziu2ZbCmEfGzzPVDdOFvawVnWbAHa0MOTtrQsTkMXZwU4lPm3_7z0Yh2cfS0NX98btu_s38rwrxhBRoRQ48WrEZ8Ou5aDr3b8L3cr8wxGxTAOM9PAXRn7s_m6fdLGi88Ntz2-57QzuOFPX7cqcbRT_GXs5UrwEJ04-9gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjykfUVMPYlMaRV_zGZ6yndaFwd9Qk5pnsEO8U1kaC7GeSCeRnX0yteA93pVN2PjWn89GP5gHHfoVexPL0coVGetBeNE7EQcAkMBPSnpm0cKSe72HjUW9EqoNyLOu1gUc9jclFT_wuyOKX0vkAe-9qI6WJfVLM9Kc67kTrcOgg6x7x_8F_uL80x-4igFCr1bIhlTTPYSRD0PjlOR5i5CCJ-oI-YoDJOEV-S7JCVbV98vg5sipGBu2yIJV05uw7lAEc9votK-klC88rQgTTCx7ykSVtmb6f9GuZ5oDsRCm1u44ZREYcsmE68veBHmRNOxrbRIijZ-iipRZiEsJ4yq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XT-kXVS6ziF7SkaSLToZGny7uYdhQhksBZTPvjJMtd7cw0gcry9pe2Y67B_iFOt1BffXnvMDAqfINkIEupLtf8ZtH1sdCplITG6klcMuo-nHNza0NU8XKKz84dbbg_lSSnfgDciJ9PiZpOfYJg9x9v_SOChdKQCzkZaIaynFJPhN86hgsr_nKQmyB02OFOXpVv-xNCtAAT8yTH01EKcM0cUpqdpBm1y40VdTBp_1rw12w7x9DS33Jw8x0OUNIzAnEoEb5lix69gb7d7N5-jDZ1TOGJA3-WwzifQ5kj9q-rvRcx9pl1LKMV3SUJVgvmjyq7uudZjSgoQHGB-ep39gGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=VHAf8fOhg7fMG_9UJGzY8492_p_ZDoR3gY1k8BhJ47U6YjNSby-w2Nd3INyjQ1y7b7bZMUh8jKz3KnYS8ytfqX7pcAjjMafDy3lcSEjDlvWZheVowBsD9RHHchX9qo8Hz02LiE47Z8fBkergt4YtH1ru6ME-_1tGatVVH4wVLxfR216kZqL507XM3B9QOy-5FfmXyj7pv8qQyWKyULUt5HfZc4C0Hr9ozbD119WKfFWzBIct1GhnZwMwK-VoeuYQzy_sw23FukYKlFzZGjmeiNkXYhGm2dce1I4imVZYATDze7YfTVru5x_oqY_ye1uUFVNIwsNpEmt155h2kwzsqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=VHAf8fOhg7fMG_9UJGzY8492_p_ZDoR3gY1k8BhJ47U6YjNSby-w2Nd3INyjQ1y7b7bZMUh8jKz3KnYS8ytfqX7pcAjjMafDy3lcSEjDlvWZheVowBsD9RHHchX9qo8Hz02LiE47Z8fBkergt4YtH1ru6ME-_1tGatVVH4wVLxfR216kZqL507XM3B9QOy-5FfmXyj7pv8qQyWKyULUt5HfZc4C0Hr9ozbD119WKfFWzBIct1GhnZwMwK-VoeuYQzy_sw23FukYKlFzZGjmeiNkXYhGm2dce1I4imVZYATDze7YfTVru5x_oqY_ye1uUFVNIwsNpEmt155h2kwzsqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh3ebEC0zQLgou6nXOolct-ikY6iDRTsLpJrRMY7VCj0MqIV1QaXd38n8FuUjmts34c1kNq8_-Mcu4CpkxQS-M3T1u6WHidqIgDRaif-xwEeSkt761Qh6ik34D38IsMzj6W_wdgWrM6QeLWFEgtRLqVGGj3bn0v6tIBiuPktV-MJCiWChdPkBdYUnVQZhelmVivmgWshvfneaK1ZKZ28uHjr-21HL7W6-XNjGa86AM6-idbH8bSzsd1sjv1E67ISIoYM9rrLbhuGsUMuJ1urtUKqgD03U7H366H9aT1hBypqz0S7C3484LAdGGOMChWofqYkToon3yUY8i2MRCuPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YnhvwYlaOQfO6VQjP8ptezGU96PyBEZGt2uT2bZp7t4NR6dG-evDTZgvZ9dU8TU8MF8ecVKItF1ZMnJ-OthKfZJS06k2zAUVVxQg-J7ZvYFSLGR5dGL4n67bUjcgibfdb1L56S-UTbfnI5tT_ADdQpHDI6bzuf9dwZVyWz05vvBsLSFBZJJL_gZ7ISEftAwPAkLwgj-5Db-xX6w8nB7GWzYI9Bvpj-mDmWiBkY1qcabpyBbJnAmnS13tZsWeZ44I_R17NnNFQ0Ppn0-AcnEzyZB9u4GceZfNQ4iwKel6ZmI3vxK_BbJ0LoknWRHbEE6Y94JgrVEkAQ14l9KJrDF6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOpMTNw2DOWDXNCXLhS6BCSVXc1InmE4WYvs9uAbaEMxUbYFWDyBF4Jh582lsJa7fZ7NhOB3-DUyO3-bFwJQwo5lB3ZkdkV88OM9v5UdkSaaJA15KKWwNpqGTD8oyRsDDuQlEWCWa2gVHvYfedgYdyGyXtiUXLpYyaL49p0s1iP7kLfYttMos5xCTEDuhiFxzRqY8zNfY0jafUy7Z-Nsv64bX2Wy0GNXDwZ-povHTGYu0H9zDDGz4ppHfaWpYfYs9Km2koDmkH7vU29d6zvzCTS6d8Wx3B9YqJ8g4ZnTPIOTUr_nUxkAV53r63Xh9lbJsmEpKeunFYk-YrH3Zv5A0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlwkqjUTU0EMrLE28HCGCEBefv7lkPpEswIUQhUCLe-xv0FhIFukPZ7GIvHO_6HGqk909IuILpL16xe5h7Ab6Xvd8B1XZyK9aY8KAlJpsUsUOR7KSrz53RyVGKvIQzVR8TJVmw47dWR4XAVG5hCFNfW0lj5IrYkv_zVNcMHPagg2bxFQk-TGFuJZrix9bYpEwB-cXIj0S-7hcsRF6IC-PQl4LvOGVcM-Atr2I0X3TmA8lTqFxzTm1U0b5IotyKWcK6Bjy7UG2c6Mi9raNN6wcWc9ddoFnqvO_38Hc5_vZ1B1qetEzxMHUqJMVeyFlLDJb5wTDa30BH07rTTYiPSlgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHGU03Mk8up8Sep2bUigOBMATEg4HQz_mq3QZoUTY0AQJagpyVWq_LLtX5bFnNDvdp9XaBaT01rmEqqmNblWpKbOU42C7L2RdyP8TvHqy00cmu0FHBIpZhcT6O5_sgOTodb4Onkj0n9aINwPb_yVsYvOCSsHY0hJaImmeHbC51GmoAihg0ieIjgrmWNHu2puXMOozgqBZwOTaPgt3p4oUooKDc1JRzbpxbw86uSGAuAoqjlXWAmV_Th10thddUmipF_ZmMKSk-e3qn3SQFNdgRghcPgxZFPSlud5BAryBfYv_FN_p_dasUkXudpOxUzm-Q9726ydV2SMD4lcQsf2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQPLT_X5epHKGTN36y5VFUhhw5qyaydaeBrhq_trlCSu0XERxu_SyeBZ8u8knrxv42L4cnZ8eDj72vDiqm9o6tMxrvEMrTWGDzCOJ2sULb0PVT64oUtzIs0aEfr5KoLMz3LAxEjBdwdQkbT4KIQmO1bxJWjKMwBuTnqiPqrtP_1tbBuQ9ipvqrZlD_4WipvQICmSxufShI_yGV8YzRpjMKyXVKEQSVRZK2BU8LBaY0aen5soUIp8OLr5fHm98T3SjuVAGviyXW2h6rIeXRWSgkw1EMB2xx1gTfd166TLj0y7lmE2CVP1r3B0Ls6kln4JzDZgl5hYANFrKAP5mGUc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKkbmJPqB2QKSu-iKLUHacvfKdUsGsjMm92n69MuottoKt_3JbCyvM263cKEfXSC24nHGFsIogaZpzulT3tySbRGPkJ9RzoCooLdPcPSH-2jSRKxZILXGB3t3G78Y-VDheVJ_ST7foPxwkfXDaJLz8NPraKhoU6j3ZXr0H8KTVOeXmfKxPD_scx5jd1Tgr-CzYbcs5bPCGZ-jKMbooBiCaZHIk1ifd3-x3DAGjENIrEXzXKaoqFyXCfHBz9HiM7FnFkwID1G7aWkIuKl2hVO2BCRMd_Qs5AYVUXhi-QPCo77LbR0bH4fTR526kIoD_A_BMVGCDiXX1IqLd-2S-vqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3aCUPEEOokQ29lSvQa0XVYgc23nKbOfbXocplzorPwJ_WdziLnDz5EdpZxRoRwVaJfKbtrveTKnVF0aDnKuah-MOW4U_27OAPamdFy2oszXSRI16pRjlKHE3LE3ob8RjPPscjKbFKC1fcOrj4WNIHitNy-GU-RkU9qzn1U6IGkCYmAkLV3mOJxgcTgKWqNJ7jc2Z5JvIpnNmMNpg6uhOMHel-_25JNAL_Wk2VZiCcAsqzBljKbh11DfrpP-KvKsETOC5tPdmBIfdI7X5laIfvJCMcbFD12Jm9UHTkz4FIQPjg1JNJWOcnuAp9MUedSfpp3UKfjKiOPnZ_LJhKPp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZOusYEaTQ8VM7K1bBY_ScEOFwokF2UJeTeRTvYZYMld118z0iulgLKbDcbBW4oa86svWZHfI8ghP-U6v0Z7yU42bHUFVaJpMyWZYeZKMR0xofxElJVNGG7gvC6RHyFidI3tKbHgDBvlTQ5jmxPlgdVIp-P9mdvHqSe6Iq1E5GnKTLpILjKon7FHecPhktaUVlc35dOnd7RmDz_uftahBFBfk6epzL47yxZcuLiU7nGTSlNHLUe28hjUrHvqq1SLWeLQcdeCLlEX80-hsv6Oo7LNtNgPJS3Sq701__fDhk8SSlxKy7Gg8qdFitynztZ-VV43QT7x4_U0iEvAbNuURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNV0u00gpLEeh67yaqAonsg0JmXFQLh_SmD5qmnlqCiL85ZLz20sZygIJpui8SCNGsV6EhvgLkETjxJLJvKI06jpR-HbU-qJKR0P_Tx4j9PUZlcDLmCWPMuOuWPOom92pG6MRCi7NI8KJg00bcUlyMTWA6RXti1NyEdIDktPEtahTYNeoyOvkoXjfpb_PwTUIQvXusgymqBtmbx-rF4GpV8P6GLGJtlDAxfOCIutfyyzkHOrG3WR9if96W3QkZZC-gTDiT8cz58SAwEyM65ekbHQgp9nZzDDyv2mMCR3loX1gVWevjgEpkZzk8RME-QaAefYcnkWBZEfDBRrC6HhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-3pVNZFrg-9EuWj3AJnEdQ4lqeUdOlY5dRmZl_oiAZwt8AWu7EmeV31nrDpz4XAY5Iek1V7IgRQHTvCQmu1ibPdIJdh5OEYrMNxiSKtCvH_qpntW3R8hfljJgCdU-piM2TA9QnAQG7kdQXQfETNNqyQKawZzV2xPK-UL0rypGxWv1Kts27xTlAGf8c1qwHNTfp3xFfCAOdOPKYh9-3nmdFYZdkt4ddWYrfEbYcn4xLnpEhC5onSGai-_YYWv3-FEFRNBLEaNf6M_CUDW1XS2F_wx4uyLnz8br4kTjaF4xm5y1ij9EMMGTW9ZYoFNYgvsNbB45P-tFUQCsD8_RiStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcNVSh0Kr0zPpJ3MjFJJCelDfkX8UkcVLf3JMJHqPquFjaeUthzgigo6D5ZqPbUoKRd4Tu_I3FySkB83iPr1GlGbwlhmQfweG4_evRiEF3nnCuF_Ma-h3sbBkpYzF3pO5ThOZ072uJg-0VQ4Dw-6FUv0Pt2VbuhzwM3bEje-3hncFXBpkxmzXaWxEDEjNVR4fmSDidBoRHHgbmiS0mZ6vURH4S3al9K8yZbfPzV-3QKkFxuYgl3ZkThu3w7NCtCnzI0UyVQXmdkFfrUMqj_BOxLjxAAH9sbiXeeiW82y9nyJ-SGVxUGdczK650z9pab21Lx6C_Xn-XoAWCJeiv7H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlS1A6OzFTFJMTyiDqdu_yz3wuoI-UtciZRBVWiBCA0NIKvbVsopbBUXONuiX9ByPhPoAesCCBbOYw_OAijDv5oBsaq21wTJ6sbNHfyScV4yC-GXiY2XvB9myhfBWinngIZXnVaiidFVmtZM1qLukrbgoLPeNzbEiAJ5ykcWz6HpKsBYnLBPHsQrtJk7kT50r7cSTKqwMSkclHowgh127-Hkr10RCnvlE44fcXr58uoWLIKk_THIIkYlJCnfgPgZGHWgH1Ifk-dAP23KVss2Qn-AM-54TyV-OUqEhUwm7inptcfZj0XHsa7FO_u47lcq00khJE_LxYTL02SSGR7Y0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaA8XVTy85lKJsQtqvdR-4pkVohCUofk0VvUoq7TNfhNZvOMCp930pk-APeT50ungpGrfydlOPOSLHZ4H8-1VzinL6IEbPLt7PhUlzvGAhKcOFZyXU7SSnTH0gylIxJPfsN1miOK826dWt0IrtMy-AiRPWGn34nIECW0smsJqt-nNH7-xJ1yDCKzAhcPPkPjyMfN2EaMNx14N2QWNEb-6vzlySWrQPqx0oKeympVvrczcew4YtAyzyfEAP7XxRafEhadFARe19sLcz4C-X7YzpfkpMzFMhccoyDdjW1uI5USJoR1LczYR5rYsxBg-nmO7gyLykCg2wXs0JM31NNYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=LhUoojy96m0qGKf83fwf39Ojk2ut4UKzOo6MK-xOhaV7_GQadViW11Xz62wJwRiWUqWq-shlCLn_OL4dQPhFcsVren4QN9AmvPQAXfXcNCxXcHFpdtlKsICXZVwXhl31e7-krTYnWPkwHlKHKMlWKsPb8vL_wZt7g9bgHN57JSaSAI3Dg7sgy7qYuMCBFSRoul6mlYS1k0woNlF5sQixOJcwQEg8ABbummzOFI9NZWXme2N8PZUfpSgJhpXrt7c-vTEFPlgNngMVzaHRzRVNU6rhPUqTjFTjJNrGYpSVoAOSK_RfY0AL9nqER4rQI8E8AyzePI0Bjf8T82gc-oPFVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=LhUoojy96m0qGKf83fwf39Ojk2ut4UKzOo6MK-xOhaV7_GQadViW11Xz62wJwRiWUqWq-shlCLn_OL4dQPhFcsVren4QN9AmvPQAXfXcNCxXcHFpdtlKsICXZVwXhl31e7-krTYnWPkwHlKHKMlWKsPb8vL_wZt7g9bgHN57JSaSAI3Dg7sgy7qYuMCBFSRoul6mlYS1k0woNlF5sQixOJcwQEg8ABbummzOFI9NZWXme2N8PZUfpSgJhpXrt7c-vTEFPlgNngMVzaHRzRVNU6rhPUqTjFTjJNrGYpSVoAOSK_RfY0AL9nqER4rQI8E8AyzePI0Bjf8T82gc-oPFVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvBlUU35zWsj9grik4XfeuzbXHODkUyZOTtk2Kd5MXnfTG7tf7GssLgvSeWP8iKMIn6YsGlJ1D9MFKHJPAoIPs4BWPUhW4TPovXRnLGXRCaplsjIt5b0Me7rvrJ6Z61Dc27vEqXf3K41H4fMN65L5lSTug1fAl0ogWHB9mEeLtG7d2NTlUuTpyDrIpKltAafHYExpRMTvz6q4EeqkJp76CFW8sxj7rCQJFg-k3JM7YSdUqJ_d5EuZmjxK0B88KeUWrvwWegc_hf0tvXsVDb3mLHNKt6Qqco6rQyz0UR9cmPQQFN_vJo_ac65tUPdqHZZE8nVWcyzjay4rIGqiQ5Cag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxpmUeXgk7iEhztRE2gMk-UaWjtPRc4v54LElcClyfmQ1288OsMNDO57TA6dSU3vs2qYC_BTpLvrxcYTxkQIjTAKozpRNMNQ72cw7cQ6wZkUwBdHatD7t554PSfhpOtmdqnpOHxxAraOtsTuDuJEPkCwChYxMGSLqbdvZCcUdANUjJ3r1oh0AZmieQmw7Eg6oiMHq87v-c3cbAZz7GuUDvdP0jvXeMjeiOkwCcNb3YrfY1SoNuj9EAVpdOyWnGAc4GXKQ35wLXh7GPoiObaBsodAug3Fictf66X0WkeEtLw-x2LfKU-nw0WsUBjU3pG6oRFhrtmD3ssPoX6GebfIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvnreblzBMPcENkL5olfISXt1nyl50RbMv1bfXGmk7bpo47gZZUeF3krPPyAHciCsn2CQszITBpn7NJQ3Q_I9Y3vodVZM-r8cCQ83N2x5dWRUir7OHSRxgoBQ9Ni-UVYOk45JS0XjT3qs1Pz7HZgaBn0bHworSw9QSIu5FgXp9P3MGUeAPCERcNuW1XCxx-oFDkxUWHk-ceEnxwnokzmextuZUOllNZOyYHS34PkhWgb65LMxffCsE_rHJUn9thQKSqkskhg3N7hxszQq7iLXgRD9UVXBOEzjvkhY8HI6E5qc9q71O_VzvZ53Jm0Q4MJuPI63pvGEaVpgDmlg4u1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djrJ6BvJ1QrmK4R8XAukVXvguW1FyVaddNvy_1smtd59sJoOj3UnM53D_QiffxGU6unwxDsmYiY8zS6jQnMbFjYDXTpe7UQdHi7GAe2XJ3_pidEwNONl9EXzdaw-7bS7lAE1IVcfz_FWwf4azzoHcAuQkAm6WglmLuC5ahSMNU9JEeh5U7moPJUrMGOUZYeEghJSCG6F-4neiXtOoSncvdkim6KQXqTyUjUnX9-K30rsldQviNgQsz_fXqEP-npc_5v1BBbalUpsXUwD8jkDPwIgNuOqRMxgoFv-wKy1beQsSZFbAPaXNay6H1G8sTyOgYmJAnMns64M_A21ou1HBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr8iVDKsAFtOXYKTtMkcJBx6sPtho1kLW3tolpeIAORyEYA6pbz6-1xNPxdlER4kbk8EWyyE8lYpLN3Mt-0YjL4Ntvvu-xkn0OXe9aaUaeYgjb1iPZ-z_fSb2p1B6qoy-eCEX0AGl3QRIS33Kc65KoHm1ZHesxjqqNF_OIsl7vg9FSElUQTbfAYdY4cVvOtJBTX37WkmJqIYLeQSwZp10mAVXD_d3PKhNSJpCueARLler5dIf2EDlrGQC0f0xwX0qcasd_HPhVsI-Key8JGHz1ro0ENOqSz8xdvcJTMeSnbGksLXG0ODAxWWSwRM9d3T0-T-Vx_UMhQIcXRGR_qeNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIr0oProlf8t9QcLvEmrTwY_351IGNO443uetAEsmbJRG2R4AAt_poxus2ypj4bsurHW_T1ZiR6J7eR9gDv2Hbp3ZFTl83fCGqjabca86zRZIdAMBt170e5M6thBanjfIqdjV92hFxTRnMbd8DmRTwc_Yv545PEz_p7rA4t0su862MNK0BSldd_GGVV6AaQ5kOJAe7KWXMvlnX-_HSOaT90GJ_BRBfVE_3JIdHyUcOPaoruiMhCijve4uyK8Me-cne0I6ORnKxnv_TbPn6DSHo1GvWZcsAWRJJt_jqw8M0Q9DkopjXhPza-V-mwj1t8JYh72oi7RxfsoTYn8xptKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp3FeCWFL-rs_Nhz3pwWCWkfOWNGBy6FUiZT-_uqnmve9E6ot4J2rAojddfJEyzQtx8ITsDcAbcOI7YoKKH9GsaojhGJUUlzsMZ-STsFCpBol6euM6MvI_6XpZIBzs5pUKgGKiAcaQNlvcMJ3Z50BLASWfbszzfUpzl_qFbHrJcR1fKVOM2LL71WymF3C3nDZ4qzZ11xXpCNGiwgzPzZZlbBvNIPTS3_uzbPFtucM4iivsAFSekofl3Lry8ULJweQVJDEIaQ3HAWedYwVmxrOHntNXSmMZ8oE_AHrJhuXxOUUeevPBSHdbTvDa1kr-GnuU8qaPo5stlSbvJY5ZA0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaBmsdRvWUrgQvc57w_v0duZOtlsE0gtsSOFP7oEoDphiyKjT7IKuYvITnG5nWSl785MTSeQWEEdTp41Qki-s35C0hLGatUAv0-2vf3p1Dekx0XRXNHvsIBvRWUQjWAhEp1G_ir_ywKrqQl3sEIL6YnfyyGTdctff59jwwpJK-t5kDUtoA8BajS7C24tSFc7v_GRXNIzZdaDVWvAPqlXo0lgSNd7y6DP0WddFLJYEaiiPbElVLNWOfHQZCuGvMgfg-n5iFRac2bsq9sEaxAu_DIsVujkgRH03guj5Almi06842WFpBlqLksGhwpP4X_uxO27aMKeb8H6NTMwzKdwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP4Sal_r2ZrO4p8l-9evf8gLn0pIcSV4QxYou1f15ANf8Pye2utj6gmxln4MR2LK-8-QJaTASmnutpI-SijDzomBAaC6GYKLrdyV8JApajE7ZhlLyb0_nC4e2hM7x2y60RFLwiZe4kNF52v_4Wrobs_hkZW4q8HEO5y8msUBRLPUtm54DTzhtH8EGTHII6PEVuy0UCSCVJjsIRTapAz-tzsjYABQ3N1cLJW0QDVuZTt-G-o0x97bdvS7tF3M2RC2NqDYmFOluhH5rBhbtIKGEMihBSHXyQCKZcFDZSpelntgd1uRCbFJDXZzM3k_xZvowNfHuibBOpqY4T1YoKlx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxNhLQPaC7PQOqcrB6uutSjn-D6AFYrdMKXOIX-goqIons-SmUAilcQOCpmDtBCo3pqKrL2r-33l9rDCt78aXeoKAHFQLUoe-rVtM-1tRPIzPWHfu6afVmOspZIf79lJZf7nEbyi4F-Xn-yfAmTkLKh8rZpQGJZuAQgTkIPoKwwJsJaEc9WpfElIKw_emEQD1punRZuDMjrDuY5tsecRuiXwJK2ulQ4vJ8RbPbk-5kns9Gdv5Ee5OMTdZtkqkBJKpqsuUf5Jh1j2d6S1ROPpr3Kc5Yi0GzwtURwdZuf8Sj8IZOHNBmzEfL-lCv01Cc6w6nArgEIUAwrl4eL06jnLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uljxk7wGUAu6qhewo-VSqYEnbLAY4G02D0YnL8XUyNgklCtG8UhgdELqtsinKeMayQhKyEy4Wc_DIis3aY0xeRU-4b7KyisPhoFYpLiIQzlpXr93YipCjn_NLZEbfnjLTcYfUZnPxVVD0JzE6z5mYQWVeejxrpuLpxuzqFPJXwXYU22eEPGBlGsgivKWeasXoTrM_aH5K8IiEkZwVTaGNitTP8aEOb4ibQOQaLcBvNfw2LzkopsdwWiY7oMExxcfrf-bYMiv_fQ2EZ5oEAG-SWPZVTf7aeavdNT9lIz4gjnZDd0c9MxIa7wfMhvMADTmMCJw-saJb4CAJy46hhb2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzbDEhXZ-qVu0HRomtZlpNRcSN3IpJF4auQIEjrstWkCAjg9NpBQSEBI1gg8LA2SofCGUf8PAG-RBE9yG0YU1bexChP4RXPPTuweeUHQkd6KBP3dVCIoTfKL8ZAMeU_OP1hpELE556Lt-2DvuiTO4Jw4FWFEDEDwuHruTyOt-5cLUn6h4HGUdO2qYbNiDQKYOiruckUwy3-0BypBoUVGM8texx-7ER_cLjGruMdVvqMDtps8cwzeSv6l29EAq1Qrz3zeIS_UGk58W2XweQtVNm5lkpNoGLTiQkVZcba7PrUcyDJ_Uv1QtWi04-ZAu9KRkEN4LjN_AEhF9dx2_QpgWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNoeDwS5J7QEWMOEOb9mNSewH1IhLxwKH0g4K3E9rBkSVis2abV05S5tY7ly7NcTq8R7vOwBZ008Kui0J-Qu7OBammDaxn53AhbWRSYQrvsSFIqvhiLKlkjwFfxvTbOtLKiwJp_ww8KdI9LEOkOFiApVRtDPS2JuYRF-BOE7GHiVtjXqxRnv6hWk3MMVHJIrRBsNUchz2afUYiMQv4m4dR_Abh27aj46txXZxvk-oJVTv8cBUI0cGwEbCEAIEvT7vAt3-br4gXytAEujRipipUTjETQZlYspKzk0u6-Q898D3FI0bWZEC8AGGxGtsdHkkNy9uRbjXkU7443qU7EYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaOyFlfrCwsRoUTEc3puMNU90zNK4V-JqRhSARbWTNsPs4QUYVy31JIj0YYjFW-rCkK737c1edlp2OvEJPT6729qD4kVOO4RFDk5bvt71f65VYFuRrksMcs4wBuuV_qmf86nYfNOEPBlHQXQq9bSI10lbBSQqRujIWmmuoUObBJXxmUeDpe2ExGZBGhdfr4fVWxEZd_SA9V-Vwb4sREMY7FHJsAopauuIgyI-_PP7JnjOmRLGmb0hTMozvhYvMkO1u3YhhhddZf9oP_TLGXaqFF2vEQP-UVcOZxcYJ5VAgzOqzLgweYNdWkV1vQNeEInc7BhJxedocX7wRyvH7642g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUJNlZLdRrytN8vifmwAqDrglFuGlR_q23_W4j8YSBuJvvpO9h39hYqCoe6BIxmEg6ufJEo3QHRC1ilNVuks4lTjG1Xy-eZ5VApN_iLQ6h6lJCbopT3RoNVUUBOl5APFq3ezZ4bWShO2ffsYrdPaCMoXwgiaOBstRZt6UnBC1IS4v3wINwu9_mf1u6oIUmg10R7gx78n-rwLd-MazZa6rmWIEChup9ZRuAzknbxtFG-d5xt2Ty141BkChIStVoNX82EN4WJJE8Z8dUOumjdoKgPDoZyf2cDVYiYWKMmEF-s_5HRvLct0RZ7GJepqDi06VDvf3oNkSBLqg3Aq5hCfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ-dSLqXaLGLT38VLg5tclIH2imJmYGSObNsRLp16xD2IDd6j0BLaz12prLn2Rlesw6lcE72pfrFe0D_7mWuwpHZYbbHk4XHayduao_MWILSi6LNleoFtiUtZR5S-De0-PrQhakeiQnFHrmFPlQ5Y8I1s52GvAtUmTLSu7H23tySAdAtJ4UkpM4xLpuGcVxO5fS9Or8XAZAwz9fIhgVc7xu0KbeldPl_lTx-4iZ3TNMPSn1CLW2PIOmhz05oia57rt3qqrb3hzydSwNrYqUPB5jHxUeW6D1ZlKfSpyV72AIWhD-egCy9hjH2MaI5gkSNHEh8sCFPH62oWxDPc4L2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbwQuXmVvd_KOrPk7LHC7FAn4b2ZAtY9S7ytCSZPTflr6Q0T-sj_-z8rzodoirO_xnR6PgsUUusi34dgzG_eSJ-WZzUQnHOlnS1H4BIwLxCQCeKdB8XGHlF7tCZ5oxe1nOpTkdZNDC0yBM7GVtgrCkV8FgHqK9hN9_oWqw62Hs0O1zWP9sVBzdWZvWDxkODqGOqyzsABwuVRnRd6mtMQxfo6b2_NixSH2GooYaVE7USVORRr-PnzSsbQ-ZGmSmz718g5oJ4qkRfDdlqXgqA7HyNCICWnLf80MUl24y_r25alyV68iHB2Me-kUrWU59k0Rk0hU1_BUhX4WRBm8BR9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atrDl-wdSJ_IQqhWCx6wzpMJe3ZxQdtcj2_ZxLPN9Ss5oXNrtmvH780rquHHc-5m0RNRPJIzKuy6BHKidwLDQWRcDW0oC9TEJjGCCTGVcQz7PSmRsgDvDI5k7BBGupfg6aTw1pB8bGPXw9uZCwFN84NYEcK2KgNlvPoJYngsNrpOkHMti-g81eEohRBV4pJ0Px2MdiW46x9nfHPWfklkwSuQgxmvp86Yaj9-Z3hFs8YdPd-LPdv8_Q44fYzscdPNNytpjIR7jjR_0cqpSlz3pioYdQaTi0tRZSrEfsLC2f1htzfdfqsaThO59Sw9K20gqeeB1ymRsC31JGsbBJ3cCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvqIGMqzp8KwGsOMgolnKgHNofOoko2JEpsAbcAb-22SSa38pT2CfRky3Qnb4LwsAS_P9WgJWlreshrnzGQFmdeo_6VH9jZqNLhAtooj_ybWNXRg6cGwBGzOOba7aVPUDjiCUQist4QWxSFMDVnRewUM64iYTQQSxQ49jaUkxkoPXTwL_eLCcKmLh8GdHOeWEJftsG-7uhG3vVyYYaXkkUu-vCDCK9_Mnoieun4DlZWEjxuAnD2nNBp80SgQZPkyxCAfGgzRe8675K98KfVWU2xcFBaWPnDCAGMOICIjjzV39Zgl2hGLxPzJrZGYWABjACl47iCOe60imK0zkr4M1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzidBDuooTwJiGsVDTpB884OBmsrP5yayC_j7QQqeniTeV6N6KlKla1eU3cIcKaxPUx26dl_VcwH0npF9iJdLctU8z8m6WNpClsIW3m79GSJ6ZvDJo8xKueG7unlzPmW5lyY96TeGtjkvl7HeV78mK0KSTgsVII4tgoU0Xe70roBO6JlYTf9HyIGkYJX2yMmat6bET1MqpA5pKc7Vcpcg_ksKu2Tx8unOZ57KzJ0uyWkfFIlBpiyBB9LY0ubtOIVtUDI1l1q2yIDxm41SiPKoxFw1ssttnpDdSizTwZRq7zgc2pgjmR0G4BQGqQOVlcybhduffeGzRM9RxMClIoiew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/My5VO4K0yjV-uMZDJyZ5LNGqkZPXoHiqaWk82LTukSrkS4vHWV8Y9krmS-hngLZm2tzYSjVJb-HDpykRRnK0GSUYH2IcB7NOSunn65ouMkxZ6JqjP4kdNdUt37HC0LQudYl7geuydSpkwKsdHSmG0qboU1sb-XM5y1jFC-RswMpDIfA4L36f-COV4aaewB0XrPYmZ609xstyL0ITfWyLZ_9PQmoWJHnwdf_8ydbhZ99skN4RMwZuaFyJtdS3OjuM3O2361uSU3gAdcrdfQ0W21eFoE9rLwlIweTdxWua4vkQGfiKD0eig6roa9QV2M2pqIqrWFM7cyx_PZk32_x8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF4NR4Kt0gZaWGOvYDskFC8pP97b0Amkncx415ZeYCa_XYAcnxZsje9LD0An84mkBw66-i8OlTfqnk0DfN5_FjiogK7tRIZ4W1XeVCluWopbm1oabsg56DjPqaFJ2neHFAF_i9AkZkTyL6a-Gg-HSQibuRGu_-akkWI8guW0x0EeCtOpqKLZ4H5ubmiw50SV09YEReBkn1ud4kOUGMpp6iOxUhPaXBBA57CStqmcCXM4t2-xBlgzz3wjOcx5Xx036iDFVDYx6TVIoZ9aQxZPV3N8rrLp-mun4yE-ARyrUvjDTppZd9PBGcmaAqG1zToLYMkCTVCw-B0p1Pa3ma8pqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW_sIylaCjGVi6_ciRM4C61z1Mmu0vGQ_aoDoaQMLWe0dEyPVYe8yC7bVgLtqqk_VJNq60CalmKP5q_sAZCj95yskKwLxBIxXuwwevFu9wzwza9oPnu6sbuVZ6rTGpi5_HLTZmRLiw2sjTm8zXgiHZZp-lQliXOq6P4KTPagHISnOusGa4-rh34e3zpCy7ltotV_TUVofRgv0cgSrHX_u3Bh7zitYwJEI3DxCNoQmPfENEchTxEpYwXL2MNIx8VpZSWIyahFW4EbVkjrRYdnNCHfytnzazpXW7MO2FOpxD8KbiXPxfm_TUiWbPBGZ6Uh5m_N4O12RoPf99B5VIoQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=BH2jaj6VyzVuen1XLHlXA55QZXKKPzafFj04mupAfx35i0LBhU-dJ9Rf0J5i7Zz6MCUO1DH2bRpmboqZaFlPKItwS3shXPsyvYPOnpBaPkULQ5AZR0jioVNFHht4U_29hFUJFKaC-7slau_qDIb3YrtsI59pBqrasw414yLA3OrbvZjoIXSVz6H6Y8ebFvFQ3sbi9mFhBZ20c9234pKTOlIK1OqYWuFKhNE5g54Bi8mdAV4KwajCSMW7vk4lUKiXjLhv22-4wIQJ-g1RetA-HaU9upoI_LAZMIExkJ_IVyUG_VbUCKp2IH0O8XMwh0qFepzMdAsrhHx5y9YpVo-nAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=BH2jaj6VyzVuen1XLHlXA55QZXKKPzafFj04mupAfx35i0LBhU-dJ9Rf0J5i7Zz6MCUO1DH2bRpmboqZaFlPKItwS3shXPsyvYPOnpBaPkULQ5AZR0jioVNFHht4U_29hFUJFKaC-7slau_qDIb3YrtsI59pBqrasw414yLA3OrbvZjoIXSVz6H6Y8ebFvFQ3sbi9mFhBZ20c9234pKTOlIK1OqYWuFKhNE5g54Bi8mdAV4KwajCSMW7vk4lUKiXjLhv22-4wIQJ-g1RetA-HaU9upoI_LAZMIExkJ_IVyUG_VbUCKp2IH0O8XMwh0qFepzMdAsrhHx5y9YpVo-nAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7yQW2JXWayfOW_CDdTepsIjlxmOACf5kM8MGD4lGOYeSQzRzVE71WJ1NpZg12jiPPy3f7xs6RWSHeQii3UGchriYIVLuX2kBJ-ikSiyRj_QBtViuvP1cO3GYzCkQ3TgPFjOfIeYNYF8AbT-6qQgZl43CaGMX6uhOYU4B_fCfVV0FEZMN2WL9Yx-UbkuuiuIk7fIBiEGlqbIIgBw_djxDFtucBBMR2D4AS8mJ9k0ulwUTkPke8cIjCqnJpFg90dlq6KiaNMiq5mM-RvlL814z1byeHT97mmwRQJjQRSn7UJfn6sSmXuDNc5LoHDoXN1cZOkd9H2IK6vq0kdHJvaycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor4FjfEuudhKAqXUoFr8e5QblOyM0q753vmLHPHjWxZVTupAi9G8tvnL0oJf6xGfG-FhSyvgSIClEEww10EnDanNmNgXVrXPh5oQ86p7jX7bxDIJdA6HiLewxhEmh88tNkMlcwSg2gctEpwT0GyptWS5h6uoM2-udKbgzT4zhug5shQ7QMMSCvVLRqXhdiv2Re-nQup5F4QoByES-_-oi0iFaJiB7XAl8V_-r6w_iIrGG91g2Jvkc9TJCqhoKzcNPLQRyq5O6ImAYJt126Vm-kz9q35GLHfxWY7g2ZzpSZLhLmsiyS7SmpgU_3DSEVvoYCoMnxBa5WCZRqMGHakF-apg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor4FjfEuudhKAqXUoFr8e5QblOyM0q753vmLHPHjWxZVTupAi9G8tvnL0oJf6xGfG-FhSyvgSIClEEww10EnDanNmNgXVrXPh5oQ86p7jX7bxDIJdA6HiLewxhEmh88tNkMlcwSg2gctEpwT0GyptWS5h6uoM2-udKbgzT4zhug5shQ7QMMSCvVLRqXhdiv2Re-nQup5F4QoByES-_-oi0iFaJiB7XAl8V_-r6w_iIrGG91g2Jvkc9TJCqhoKzcNPLQRyq5O6ImAYJt126Vm-kz9q35GLHfxWY7g2ZzpSZLhLmsiyS7SmpgU_3DSEVvoYCoMnxBa5WCZRqMGHakF-apg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PchjnBJezdBAcQ-_Fp61EiCwwKnOFVh_QL9pl28si3s6Go0tWTg0rcCBRz0V8URLDVKpUIVvXeaESofhpja1H9DGwtWC55i3qMkraabT1oxXDZpmsyaa-0Muk6B4_XflhJk3rpn1Py5Feq2oCOzumG2ykI8Ddzu4heFQoHWhXKQvd42Lca_EsD0Wg9p6dmtIrpuRMqY8mQRJ8M85saU5HeRA37l4gkCkRcEL2izNns-pXw7Lfctwa2myX-ewSI7GEd3w7xe8OKCWxR3G31l1-Jdsh6noJ2ACc_cLk3vjAyQ6OetHHyJX3LL8s-uDRPI3VI5JDxH50JlnJNbCcMsOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo_v6lQ-RP5sbLFF-cFARNNKOVNHfQ0N04RaLu9cU7Uvxnz5Sp0cm8EwA5HPI9h_BmLnmLF4W3LVVdI-5wqFJihIq36NZSb4-4nqlL4q41HcTm2_e-cPbRcViMlXUV-aytUxpU19I3AcojCkLvyYCP8iTCc_sg6PVsiKDj2j_o4Dbf4GePhMWhh5dSjDwkM3AdPC-Dz9DIbqjeIcxJNQEvC_fgK3hmCf47ABAb3BHzQ6R2cpMMJ6ADVfu71rVe6bC9q7XvLxSqqq6DGXUZ7kdyozZgDzogvo3Mndmpmpu8QLDh83YR0rK1bvvehm-gbsGUdeAZzaC6qtQauntXqb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-Jp0_V8OX6ugKlNhAWs2wbSbuMa0Y7X4p6nC5p3qESHBykHtQQWY6gT8pJvTvEaMxZ3K9O66AZUYKJ_-T0nEPiuMNRKPF9BQmfkxygPG1ptf5EHMD4t01NFWu3gEWXacjXnrXdgjx7mn6odTm8FJWCTRWPVu7cxSKTen1rwuSJ2u3weVBczCtg7-C-tQaOUpCsGn9Pb2tVszYVoMg1s29Jt-bIOusdVxo0_VQRpodyFP4ZoevzScT5z2sOwPSpV_WAg9TQHeymkDE39CkT49ueYXqisxkDshS5m-5DdjzZWS6kE53CmQlWtqUpQFxY0hB_Jq5OR_i3qGXac0DP6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSJ9QUWyI5HovrvsRUYzOkaeAc2WFo5BHFO9UtBbxuQY_sxVeyVKtYKsjhbPpysfoej_bVaVcJlDNlnCfDtltke4OBSZJz15uLN47QWL_i6iKjqrctvW5Xg3QkwMjqRru9zKlEvl1HXXktxIixrDAspKNFcuh8ytxtL6s5TrvL8IAAmc7Db0CzaU_dxEhJERmRkpgJBfJO9LZTodog62ye8TZTtyln8sd-XANpdzopnXknQDvDj4T28_WcUkRSW0nndjzVfXRDuL6xwZi0gTjoPhcwsW47fNCJf3CJowSfSrLHrMYxyfXm6dpF1A2cyLWaURuNUFlOxTk4245GtC6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFRLL5r1VdM2RVKw0p4pVvhaA_8xBwuuOSTA3soQcwlgWHF2qTIcnLzXQNufHcyiQ7s2gFYAhKD5glranQUJZcUbqJrZRwS9T9zMnFXwuFmZR2cqeqRRBs4zLMG40YpRlOXEDeE_0kRyJN4IV61rLXwG0xqdO9AE1NoEiwN9ChUJ3SkV9ss-cRwRAgMrWoI6f21lTdJ-IwezzWrP5GnSw-OsKMYOw0QS9OYeBD7qpZGyVKvru0Utww14ivY8hop9byLFhM0kk36EMdQGC6wULTBu3SCDERPh_kq8Jm3kYrx2oHPKv2osv8yICw8jSlNZ5ZNKM9yEh28mWQ7Zb5KXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtYGVK1_ccmnjkAko38gMunQTbGd2UGa97ZVbPkwrys7lAf1BR2Hq74iNmRZfNWwBQ7BV0IVae0e6AjvbwS4zjLc6heyMOG4p__NpcjcWRcY_TQyO9rUENrWshWZ0Nr64wE_utfRFUW8QJ40tfmVcKQOO7mVc71u8ekpMyyA5i8faV8LB8RIQt1_HXZkD5fENPRSVR-B8bJim-6-4QcGh1zFPnCyFDkAjEXqCJH3RJUiTv_WDrzhJXDhbdHxehbwNpmzZS-SMQsNI0sSkqQctz7HiYOMgf8c08e_f6fZiF3jzzIKfneQqMECTv1UjaRiItqCVZCgQZDks9Zcrg0xCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRO-FMyMBv-SN_OYDShvTkgkcWlUCVYV_ezV0KnsdvFNoNTzIDpEtzlGegUi60mkGQe3xZbY05VHlWqn35zmgSxNvQGADqSQEwgubm87phRe99jARAWb6uH0iHdvZBdfZZ3EGdp3Ix2lWGQ94cyR6DiSR-5G85YmKVc5y98DOV_eLUYahXUg-ZUyfi29V2dDTyqZiJRkyTl5ELta6BQYklYGCA5EYu0-4yFW_VAGWQjWay0ApFdOmrW1dayxm81h-JxRw0aB3-GEtawpRVbaP-_0xKKevCl6BcvwYyDWPVbu3SiY2HwiLiq36Iagu4yYpUNbvzk6k-DW9Pdfj6OhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwPsw4IiJdlKhyqHXPGtNvBneksCi8z-_TLacC-7cxjSCRWPLJQqCH6EkI6-krKXuxjL78HJ0lQq0lNgOxDvjQBiswkPbjsaAdjD06s0soMJBkQYPKyfsiyW3PTu1kez4KnZ6WT83x-TZ7syAqmwQbhwwC3mbxstm3HGownlv8bRWy7deeof-LulPYWzgrzQovWZzUQPSPOJ8GqkcIj0DOzhzLKX-Y9-oEKLkd6Hgmh-2wXlhqfuQb_p8IDHIaiKHc2my5Okwm7_Qfyd9_nFPwlVLDYt0B5TgfnsOb6LKlnmUrYd3y092wb4mdym7EriQH4tgYy6d5kEWwqLqg0Nyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAgTS_eaG8-CiR60d1XXrIBov2DzBv2FwcF2jb_W4TFWp7-LX5gYtPWfQcKzsHO2dUA1HVIV7vXaCgN7TivjRsuxd9GGdxS3yKDLSKov7aYFWcO0BN31oE6Rfz96SrQc4xiy0_4cFG3hDAzTaT_9uVp6mIP8pGSfFtdekZ5ZtEuIxAJvb8sO9Wd2nALTGkyxp96gAgDLYVzybGiOi2AYMvaKuYBd7o_T7NOQBu9YEy_-AYn1X9-zU-M1tAmbDLoldsV8zHlH7nCsIuvIYZAb5vEwoo0n-0uOW7n1ICX6vdifJGFxgJY6ORCc7y9BgRqFrZII3TI5MreKRbDnN79INg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRDBRCS_jFvT0UZT7PcYGVm3oqM15qxYODK90x8QoFawsWSQUiNSNR5LvjGc250U4Dgjd5_SFetYjBbb1grtn0XxwRypfYWfuSnL_8po1iUzAcDkibQdjZdT9I6aCZgQ8o0yAyqJvGdX6Kk_hzG8L1iwFFnnRVxVE5DdRvnEWcewGta7Bj0ZN3qmgXxYcKM3r_hkHETawXBvo8HAfq4eWEnhN3Cb8jdbDFANvrV28_o5opGeN8hDCjjHlNiUeDrfA-l4cLvTmsarxPY4f7F8GCP45Yh6GKLH5QStU79fEaNWf7UEdH044ImV1x9wsW6dwTopXS2o3v1lelr_7f8T-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0IDeIY2fPG8xZdRvfQ1Qjh43EHJdP_03ic0OnhRvSXZMjm4jR_h3-5ggvjFYTRnWJiKepIu4ypnUc5dlQsVyMYMObdNmAOfJisccyKNGnaRw9IlXuH72Jg8zlG-vTpPz2-ObJWd0UiGZEsSgZuKiPG9-v497RcAybgdaDLeXzXFOrgioD1teUM-mee41ZAubfUtdFP5i59irCG4sW1m3SjcclUwJ1fITXWXXdpg0ZfrLPSCwOXbboBfqCY7pwxRxi9EoVH4j5bmMqn6IxGYq50-jvzujKxZUxPjtOIZ6-GrvYSneW1_HUe-qD1OP4vTU8zBfuyzQSdYZc6FrVIm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
