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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 13:12:49</div>
<hr>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7dLWrHg3zcsCQRVGlBaIRQlDEUZhlIXTZm22mwbknvXQ5XFLrubQzwIEbYCXf9F-7l5bfcrUqVPJCHuI3BPeDdzDUMnkkDoDlgKsGvkGbe3KO7RU4DSP7D5mNvBdZVlJ1SDFk0cCrFxBWFtI6oMFyx5lsuDoyikFdG--o5JJ7gUc06Vri4CpfqlbTx87llEls3FzfO6RbHDW_1T16GJmTDAgmvz4vbQgffuIMe7Vy91mDRJwjVARb1IHDaY3BRPWETtPKvtejVa4hV9c5b21xS0td7u2seTQBxEPxpLVCbd1_DWhA5JFQP3sVJV4lU1EoMxFuAY20k6JXh4Da4ZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5cRdVuBCUAeEipfdJHH8X5_prW65t1BaeYNsNs4XrERQMY34DD8Z0ehbC5Dn91O5WNqn4edlrF8w0dVmnT6aCmgAR0i7wgKKAa2KuwzghH4JakY7fUVv-i_BQ-D5IsueZ95W9U3nb7vhCn22Fvky8yGT16VrlloSVpPm_-IM4nW6-NN4jhWihaLmiHMKQdY_bYt_lf9ddx3r3DSfWWEbpEA-iXJiH7LZoPaa8ZDTNg5HGZKKNaxRQMe0Agx66DvMfxi2xAbXBMySuoTY8r4OZUiJksLwrymaVGTTpRbj-gtsS7xQyFRrSy8J2s25FdLUE9S_C-F4QRtSvAl7sz2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y900wnun-3-tv5y-Zb2J3PSH5fXG3N-7ItCe0uYTi6fW6wsGJIjrI0dBw411Kortg8qyx9LgDjvOari-FOjrj9kpITafdCWBEGaK9tdFFqMp6YJWfux8Fop_4UNbuhGNN2KBYYFPV83inS6fxqMfrlUOI13Xf41lk3kB5tgfVrsmUkLaG976Murf7Sfu0Gygxv4_UcAM9eJAJgCDgulj3rWO6SCghVt_m8CAHDycYuvgKuqYBGckObd8yIAd2BbEHCQ16dW4fgtdEMtFAHPgmxcGmZsb-c-cZfbfxUHiPPbAtLndg6abJwKT86JoAffba0YiRoqZ2H5eg-jPCivnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/persiana_Soccer/22166" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGLC6fEF3a0pEh31JEifn8mHJighW88fTRVX4nhGiJBuRMGkv3JJMqfaro6wfGvI-8m4xzK0JnZy6_b9CqqQB6jlCYhaNwONTXt5Z4uPIat55ItMWlPn1F2o1nnRLFlMmSKiwsV5j-qdUjJHMkxt77P7rejDNQvAW4mYalE1knBkX9-yIM8UUuZWoai0nNaOUnEIOyiJ2syY7Qaq3Lsb3KBpSyULt8Jh8SqEhtl93q_INulWSqVPy5LK3pjUhmEnrL2u3K-8-KdHu7lWB9FwikoJBHK2tT505WwyzOYUjNQuYA8vFeZF1Lb1Za80ZdP7FziV7BVMt1uJEGzyyPwuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIJKVMoVGDwXhrk8Wy-OWnvfOkqBYkspHjQDLdwTEZxwtZA2SieqQBPTZ7r9zLYwefzhbltVxarUUSxb332fkpLHLK_-oP--PQClnKexJcp1GlmqkfNxhrLt1WW_cLM_yrh7tYBPeEbgWShmXeZj2vQK5lshfNNkACTgedojiBczkDZ5TBmf0iYwKmr71ygIs2IYKcVsRl5_KrUFip4m6KbxpCd99CwSGibpChW7Fk5O9D5A5m3NCT4mQV3MXgF85codV27uIX5UEzoC4UZNB3KRCI7P188NItmDE02ljGRdY20_HsPGu67X5FZw1jfz_wnL4E_OixJigv5d2la0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCfbJCDahA9sjTq5M4frCjkqHVr0xPnt_6XyaAvcOooYLjRFVJb2sr5NAOGPZWieDr7W85amSHBms7nTyhkhmOGGIqADd09aNmYVSCqXlgUtlEHNtOX7xP3mH3_p6VKEpYrLsBuUsyxhX2QKh5UCH2Sc1zhAMCukjEDMWG7V5sR_NxENM5PnFmliNu-qhTxuXlNP2-bhigeUhcL9kQ9rtJsbNV2MDrV3A7Bhc7iy80i3NpgAvfXZCU-EO9Z2jtGkh818IahXF6YALTG7IHtztwNyRXZaTzxCnTUbkEWQux54ZfPO6f33thJfKAPTIib93ddmoIpGR4O_bybGIAU1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/persiana_Soccer/22161" target="_blank">📅 18:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiBGEho4N-vmmjREn7f9EFlp_DPEaFx2BcQ7Pcc6lBO1miK0V4JQBYS6B8OOu4efsGwaMnI1njboyNkeKNVobr5v_YhHMq1uds2ZRSZWaOZJfRvze_7hGaHOs6NsRHvnXCF95iS3DyaMp6-gNhmtFcOq-bSPdc0dSz8wd4PuH7C1_V67fM74rBzpyEYzq8XVLYGNNFe7nPf0iSDeMZ_0xiNVtMYzA7SPmykJonXEYlzmZNd9OVnte-h44_OEag0d1gxRgmMZGHHczSoajuRa9C6OV-KYZFgrQ5Y1-oov23CSiOcEIZbK7mGCIFTPWJPsiKtInXStGAEqvXLNNcLV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6zhYLla02CaW9Z1kLzg7R-Wj-a1SQsaRugygVbixauW1oMjJuNDZbN0WedQC3FHb-u6J0dfyDO12WT2fr_Ml06o5k4zxfOLRjUlhsRlwsWz7f7riuFC7tMFJDcyCjVmLEFcaXzHDerCQXdSPkVVFxPmEXwBjrhR7IvRgyzzyuk9gl9UH5-vcAJ3UeDg20ObHsKUa1YevhjEE0_tfVDQXdWwemq2103uPXqRi70zfUW6pUyUCyRLzWNcuk0sPtEUWnYmKDUcMC9vHvkQT-HQ0hRnefoN-Pt51Ppd7FUQCIkY4DK1HoOLsxpybI7MxFDXZ0Kb8WTAxk8ZONMtTqwCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBkHqhLp2T-6MhyjtLZxHZFZbNBkB8X5UYoLZWXWaPUe0H4VjJ_iOAOSFmJXHRl0zXZ0XSyV36YHhhHyHccbNc3mTancajbP8KFivfuJAHuP1V1ppwUZpY_NpQxav1pbvGhTga7GrGcny2nNCDJeV1TLwIXGNljVwyV2jPYdnlfOz0dIRPYY7x1mT8nCN1NQVvUDvm2qHVF4UxEZk9U2v3NmF4v4BJRQTWrs9ikz7diDN_sU81c56LPL55UhG9Ccg0zTifTEWMG-deJPubXVudmrjOfze1orXpCLpPOz88dJimbyO9K43ZKov0yzdAGjNvXdxIuywX9jb33vtdaU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO_dRVmAntAUHYOkP3j8i9oA2dRp8Oa2KAY9f87Fn8h4a0yFLbLQ1s1nDMyLaFPSNc94mVxEzMM37tUfa4Nac_bX68eNLi_LNDk0Cj-W9mzd4DU_ubVq3d91Mw6opPogbTmQxET8dg3xTGqnc778sw_7GUn2PE6cHjuaJy7LBxDgT-vL5QtBzOOglklyR3uJSI7zRLONj4_rzrxtSZVlZi4mjBR981YJPkZfticsjU0QV5bkS5EcuYINOohAahWxmBKkfW-nf4gQbLdl2Di1nFzOxINPoyCZqcUFReDN8zlBfNuMhD_DgrU__GsG6S1OInv0Rb2ewSHS_t0TqwUGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzfuEhJu5XQpgUjvBVLoynzWIBGbrVsQrYooYfSzwJnwG7pQx2gihvlZhzmtVypRblxgmN7uoN1UX3lWaTspXkkz9WX9KYvn4CXt6n0lldX_uswpSRmpUuFK-FOvQKFK5Ur69nIBlQJUkCnDhN6wOnjQi5MMqYUoJGZ1ufLL6j5aD7dZHJH2zzs-vr11VaTm6pjxJ3eCyOu-BvYUVG4VeWSqxxoR686NeZLoS8m8ISU15z9o5-kjVzbLWmsTFbMgeXHjrwtBYPBqzsZZxme5_Hdt78Xc7l-CkPv98adDJv7BgqyQQ5qOwtoU-4u4PMRTBJPN4AHDJa5wb4N8FT6aMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCYc6ECHk3SLagFyf3Vf1z628GNBxtGXP0FAeV-ZE98auwMPUWfE0Ft6dHqe2KJnELUK8Zqpz9WPPZvZEWuP_KbfW1NG4vsitxX9WmsvBbYyOm6-w1cRquQeVyqCdb2ZPowKkj6hAhY91e7jUcz4zFvtBB_dtHCBe17N9KwSqBFK29uRMAN8WyL3SdFU_cIxTZ3fyOvhHGTMhPFR85wq-Vv7CLQ8Ji34Wf5axLr0QIaT7nIVON-lByCsBbbyC7CcnHys88JFBvaikZclskXgFmMlgWOLatdo_wlCqZQNVQm_eWw_i9R2q3diLEJ8UZczAhJqtnF9hCE4uGXjaIlhGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRab_-Ge5Hc3eFJoIujQp9cHcxwMq-w5fXGx601nwIaTcyGndKX5Q2Idq4cu31zdy4zXCsaIYex6esm51zMvDtQDI8p5yg_eJScadFLiEYnunTQVzk4JpnxMdghGj1NrAQxmo8JKtrjE_l3O7Y0xgUhS6-qTu-CjqWA2KgB3hsImqGTknX9D3R9G44A2UwyTEZWBepamuJ3emSSr7bad4SEM7yfv3eLmwxhbkc4zW8KSw_Ld9_qJS4GyVlXN3LZW0TukPOUWT22bC3WXmdyYA3MeAODezC4jd5KDROuA8UxYOHxPMyHnWlkmXwUsovZgKMfnnGCXpwN71gx0XVDF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSSGw6gLDyonOF4X6gC803SbhgMoOil8AWG4gYlShM1yxBtXt_YHp_KgMFcvG1iGFWmhm8JHbb1hzlnmBkfG6m75xyTs1SFzbQHOaJIVTWjR1jGhMHKdEJoBfm4YTD3Qjs_9RBsytASJEYxY_EbUM9e3FIBK2ng8yR7b9_hhHaBrwANjxrDHP_d6M7t30HPLQNYEqJujawTlQflhP8G1svK-8eJ0W1DFw6GkK4ZazjQGueQXpJDgYAlU8DCrZNmdi9lQX-RBbb_q7snKoxOMstdoq-3NrAC5R8kgS_X55buPtf3Uuqnv8imS184aLf_KjwhQeJf9UqtBsZKn0I_XQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCHtrwvtbSbGKYvxa3tUPpTG1q-3hK2ZePRt_OHECwsnTgq3vS3S7FJ-CCWnQ91DEWEqyH3ptwgS24T4K0ieTbogOQdmuZGomwvZGQAiRoX2DSg4PmueQpuRjJmH3Ifwi2j8wOmgxVpWwIAV5n0ngfnTGOf3a_nMqNFwlgOLK-dKK_5x-zAIUbouzQhoWIF69MTzVjzfFgPj07oAzDtb9PNV2d7qUSgFo1HZhE02yKmzLzRAF5PCFoI1-xyeoTPW7j2teDfuE4GyOSmAVsN4Nk0baalmVfiABrnYdiosQQ7V9sJFAQIOkBYJeVaNG8xhlunaPd7eED1vzvcVFLISkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/persiana_Soccer/22150" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pattams6lDxb4XpAjRsaLuh_oOdIS6HVlnpxdGImlbyK1opyPx6l6MaSr8h2SLS3iV2SXUdsuJ555GaTjfOdgNm0EkvoqD1CgLFcx0n5F6L_04tfaZn178ZDXngqGA11XNX5sew2HARPR0fOBCrwmLn5NFuOfNSQVVISwCt4eC3p-NVTbwiwEaR1quH1FsPKM0AekZ5IQMkcv5iC9-qXeVBnB6qLiHCz9OlvHtfbsojXScSTdLbNBV8FhXxJMkOkfc28ZuU48gBcKc-qFy1b3EoaTcNqjEIFyPtAaht2rB5O-GuhOR7N6doak8ewo_xLTA33roOO7G8jKYxWA_uXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIO8VfwE6nLGUeJb5vE433a6Rg41CYwYuvDHpIX01VEv8RKG43enPlyPbFLwnR2siGsdDvF8SRjcWCBPFCwA1UaG8ttc4xiVwXo3-Pv0NV9MfOzK_lIVbUK2YRvxXh5dQ42QhYc0x-eyuyt00L4zMBocqQN2yMUdlHyylloCp40Wo62WXvquXAVJJiOQO6xEk8O4y5SeUo6etkMr9eVDGy9WtpW8MSg891nAAKG7nZFnBNj7i7v9RrRsbYqrKVN3BG2vev2KIce42VPrI0A5LN-Nt-wCyxh-pnq5r19MDpDs5TZ-m-I9qZJ9So6nPDxAm0XSf9xIN79XbKheUSkd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de7WpEFTa0HNKcT1TKfHPh-E2tsLMSySdmZPVPjQHxqfK4bZYbvTocMhqix6uFmj-CMqnroYTc6CtV4isBJVfQUZb_3W6ZLAOZWKE-j8oKYYmdrGshg13QtdhVg3G2rh62pUSbkBiSZhr_PkEE0GPeKYhqFc6CpnDEFeqcYOz5amlR1G3ZQxQXH9kP1jRa9a_zcKfXpf3r6WzEPpGT-Qon3Hr9A7duuIJq9H4qwvU8LEnrvmaWA3AN15WPQApumGebMX-eACJPh20r-cNqd7LkykELYICD2VHzypcxgAEDJOs2whzzUc5NZjeCHkehrTKyxLEbAc6J6brVfXWRHpeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6DfTLasxgWniEWbE5J3At4iqXwFL6Mx5hLpRTNosZlQLmeO3baUnimx2NQvE_mhPqyEhoNqVzEHW2eJTPctL91SuPtPibEFDcLBnoT8nKOFOuqRzj3zwjVp_gb3KkIqsXrhxjpkL1YnW5EI8jwjOCb9yeIfMeAduueooGKgBHHo-Z1VJh3WctZnW1jYRwaWR7e48k1DJMhBgrN5cYYMwaqjNNBzGXEUB8k-28JhMkJyF4_UXJjRZ8P7xn-0m6In20g57Xui1KUzsp6s00jtr2EVeSONBoACiI48Ps4oVgxsMN65pwTTNHJAGLTREFEsWZY41LXCYHPIRAq9q3uphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OI1i_UYyZ9oVRH1SKNQvwkwzs8LnNZaLKqG6m2aeOLLLFoeMR9GzOO9j1RNj7HHGJI4x6AdxZ4hBOSSdGjqfC9B-ANcj7qCgWHSDImrfqimb4_ok99Wnn9jwgtLzVEf7VCX1FlWlqs-w2ZbHxGYwQky1zhzTTNomseTjivhSx3Z0O35DH4q-X5w4rpvnPmcKSg5MlgkrklAdR9ic9b-V3oOZJ28cvsfowGfXE-GyuHCRs1PzhhhtOx5DHLH7n7Z44XKI-bJiYxXav1j3gTiYjDFScK9A_qXxa9mbl-vQJNxszQlIhUi-7rCzwgVoLyIMQDnDCvXTHNHggA1864BEHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnksSfa-AvPXjxSEqG314blyQ0xPetpQ0x0kvDH9jfFgqwt-AS6Mn3OhZr2u9-EUDZt4qNX_yb7sp627MpP5emOBzTDT29sRqqENcRFWNx9OjbMXW-jA2tcK2ry0yosegyKp4uOwG4XxXdJ9cvhP_wlw-lJ4Z1c9bCszZB646A6fJwQobSiQOOf-NuPHTf-d-T2pVUG7tUcJOozSgSvGwlZ9kApfTzq1rSI1a6kbXE3_OySh2CLKtUcjbBbmAU_dyKEQptew4Wd3_j5yL4Pp8uRJ2r18hh9ypkDJO7EeBMORtX7ZCpqpjGiQzMwibzgc28T14yKRNE8bdBWaKVQ8SA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilbN_gme-dzR0MjvUrKPjJBCCepp9T5Hp9OktCYpPBEPwWIhesk6XZjKZIU6vnmX5E5Xh3_HlTKJUJBRwIZjNjW12HcmXy-1WcGzJY8gfoicMkt44w4q2a9IF7rRDFJs0jXLRrJxY-7klMVc2rDn3EeOeJqAklCNEscUDFG62OVAVyh3MM6DvQ22LFzrWjl132BzM1kLCI4mc8zaX3sic1fgnjKXQu760XvthH8_RnX1Cte0H_X5RpKpPgB0DqshWX7_d-DDmeDh_S6VlNXsteaI_USKg-2Y9XDEH4j5oE5nxey9XsXmJ5l3Xyi9z1ph6Mik_wQpZUpukiq1OCARGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx0aspYnmYLiUx71vW5Lv3RSYaerO5s2d_UbQrti_usZCoz_UE_uUmr6gnEYRub6O6JQK57baMlzQV0Q-l_FT9Lz9IPAl-4gyErhTPpGOxs4GhG5T3isxoyFLw7dWO9Ia2iUeyQjOkrteIwxcHp7yVaF2ngqKMYJ4Q1qXlcQtV3Tir664GsN4x_jRoI0VeTh2DFJL5HVDBGgTou4T4B9ARTTm-4qPge6BqkYkkIOwls8ETm_NGX6UCR8JdNiDJEvDgihQRru1eT28Q0whL8hGSc-bFl5qwgl28UJVTk_TSOJ6bDotGSM3tZgN30gqnSV1FSe71vg_MzEO43WBpEFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_15u4gHrAoQQkWeK7LPcwYiqs5G09LSOYzGUXanyVxO72oHQOR4gzP_pr4vMSqOnUR4PG4RuLUv0s5fq4cmbar364HE4fjqUbZ_Tc1u0u_bY9dqHOU_YSA3xELxnuzq1rZ0WavqMeDyECt5MuDCYFUmqd7y63-178QWPupttWQ7QK3Qw9YAFiJGfoUmUqrIWk9n8KlobeXvzAu2C973jcv5NJEC2ez-kB2mS_kR-uTwouW8YxBlNsIMncxRURqDVR9NH_KLksek06R5vSFcUKmBWYJiPka9q9KSRiA_rzO8LQ2JNVGNiiFDfS1MkUQjKTB92htABFXMfWL-l-zyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMjae2PLiQefxJjdI0zIdDTeIJL_ontHgu86WmNZD0yUzFBAUXkJV8PyNjBltgAbctkY3typl35qhGdYYVtu5INc2AYUNMN0DTbcNAmKbX8Csf0ILpkEHJOpEg1A99iJEl2kYME5dMIl0MlOOnLB3vLsj2631698sOzz4w4iqwEgPJsuDuf0PO-Nm48Gd1_v2H7mz-d3WUPBMhiirx0p0wJWJFdYffaZ3U-6Ze15LJfyG9Gzf7ok0ri6yxCr2ID821Npxjk_yWh-KKLX4riJAVdD_s1DY6ur1SuG4rGqLJZkNyspr89aROfdnGkUQaucO6rHjXNmJS334Yetr2wJ-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbR2308_GXCJdOuPf66pofn6mipDpckRgs0B2rFzAaGvgHj3blwgAjzDJ6vYcAp4HT2PQdgvMQVXEPxbUijtcY_BtRN_OmrVG7fizX8AsQ07MuvFiem5OHIF0jOcIU2gTrUvfA-MGA5l-13trYEGYtUU4ckfYMaUoZlKkEgOrKiULQh1o0kePKGkmrPRe6NwZpr5sug4t9w7cWtfCz4WRfHpRL9fTG5TEu6oFv7v7eeLhb-MEw0cOfn86kZ3jCdHT7CZ5bJxKd41D1uXeTb06q0k02cDrUKS2Ix8viFdt6ERA7mN0kWizjfOZIupcTGxZ_wPOu2PurtgODe9f3u5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg7SHJbV3N1phfKjyug-aorccuLojHuM7zchHymFAkygbkcanBXPx_Hr2YCOncVc1YZpU4gJZM54EfFaemdZq6YItN1pr7KsINNSD_sPXpWTvoq2t2dYOMip_hX94S0u0f-2d1a-kpPCinlmSjwSIg6a6zwDqOSG1yrwGuflRwsnLTu5aNW7mpA3blxrHoV1LCiwz7j46FlKDmEnhsK47wrk3nlnro8udQeUflyLew1ZI_tm46c7MPf0sATayASJXaTili-m2vjm1rmcTiWoTeILvWSG2YCoZgPq_gXUI7Gv_LKp8m2IxxmfWkDML6frv66uR9hQjty5hKGAS5rYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=g2_IyqF2Dcw9WSWzxjlf0mDJtM0rS9v5njiQ3AUl3FwUrB_vZj5iM3GSZLGpvDPf4LLzIaWwUhqVAxfEZqdkgZYFkETwtRPhKalbp4D4lbmNNuArF7c3wYttIYa-ah3pAPd6plGgCgJq43RtqViM8RMYs1zttVr5r5GdhXFL3Acvge4EXVq6dHbmHDsiG47uKS8ZeRlko2v2zjLcCDH25OV-d4Y0eFRW8DFoYs2y7H_qD1YQt14B9uyxNj1WNFvjK0bCxYUaEKlJ2zITWuvZ0Y8i2aMIpz-C39rKhv3xtJh6-LaA9MWfehRzze4OXXKzfoZ5R04u_fnf2Unc0-bDzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=g2_IyqF2Dcw9WSWzxjlf0mDJtM0rS9v5njiQ3AUl3FwUrB_vZj5iM3GSZLGpvDPf4LLzIaWwUhqVAxfEZqdkgZYFkETwtRPhKalbp4D4lbmNNuArF7c3wYttIYa-ah3pAPd6plGgCgJq43RtqViM8RMYs1zttVr5r5GdhXFL3Acvge4EXVq6dHbmHDsiG47uKS8ZeRlko2v2zjLcCDH25OV-d4Y0eFRW8DFoYs2y7H_qD1YQt14B9uyxNj1WNFvjK0bCxYUaEKlJ2zITWuvZ0Y8i2aMIpz-C39rKhv3xtJh6-LaA9MWfehRzze4OXXKzfoZ5R04u_fnf2Unc0-bDzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuFC0MCNzSdv2XhDMkYHl0X9HN6NuYvaLUjFZeJWg8pZLw-KU75oIPyvPpEOgSXRmrcIz2UtqZ6EUVTgNw_mpERlk6k-8FXqcuwbLM84fWwMIJhzen_Oh2yqALDTGL7RO6yHYD5HFI0jxPAsZhvUW94h1neYRG2Y8HfBKB06AzbCYohWG2IQijMidbhJSD8CtrPVHoI6hetjrwK5yNBo1_NPW8-N4dqH3Ka2aLakEHSDa4wEwT8tlz29tPDD5q3dDWS8lx5CRKk-lWycpNAHq5-Zkcg5xdfGvYIPGDM_tRf3O6tf_5zYR-JqgszAA9mYk09dD7cAsTh096j5rc_9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjGkQRaasdwM6pWE5H6Wysq4gPw70KvBHzc4Fl4KLUtodLkB9bpTrCR4HjXoD88aZtzsXp9wEGTRqSar-j2qtHTBXHgqIgiXxejCTFjTEyhtCPgDelIUiVlKEGuCMwSEHM-UAfLl3TcY17tuCbIrX9PnFdAcaksa-e2_fjt_bLsvvshOVgQyAIpxlzAwq5Ws3XoSaHhbJQ0XOIMvSNvf0gpr_OZvRWUiF72xpmeI_ofQI6RcdQwtkBDRzR6grEqjiQ6bvNbKLjJ_nPmL8x5J_ecxp7mbXxgn1AA9cp3qK6pYFi61TV533MUc_PI6MCJasqtSH-IlkG0o5VxvDlKLLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dub_PTcy_7GNrrE2Qwe9kSr6liDxfF7M3jqMR9DhkQlsQMNEO65o38r3VrBhRUfSBYUEMBl6INVh08ON9jQMqypjOsO3YE_BkXCHCHw-PbrusHM3FcRovPzMX146oWM8twgI9QUd41iXxcaDtTzye8g7cCGU8TQvQo3j9UpjiuPz7d3794OD_KFxWMwhv_LmW6qWkunFVnC7M3sSY8_Gp1VMYqZ1RTVbnWUb2YCbDBPJP1wLJgZ5QG03CbK-RDWuqsY2yhUNyXl5Krgw6lyTaskKF-7JaD6Rr67hI2matzSWVTpL2UijBQ0lyMdEELEKlUtOu3h0SyxmZjtIGTNsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3-9Ok7wB4DVdBZzl1NL20IHw_QcM23Gx22-axWg7ZJltf0Am0LgCr7_rMXobJfrio118tR95P0B6UW1jQu7mqnUpmjeDRrPUJ74QtQDE6z8gogaSWzzRVLZ5pPGXSXAScG1ggstzCOQZAQ24SjqaavJddi3pFzTdS6rbvzKoLwg9G_oOuBs5zuz49t38FMlGzVqYvRiZC0XoVUsTNKxKBk9oV_cwhFvpHQ7hDqx8iGiOuVbWbTdglp7ByLEZeYKeG_M2cnzu7bdYCbTNnVQRxNfkZ2Y6nXBJwkkNXvaKwpYGN5ZXyp81evaeGZu1SoWDTvB-mi6MUJN7HQ6GK-alQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM62qsni8Y5eXUeevtcD0CwANLhDJz4miWE2TL_7TCPDIMLgYJCDIYuoiW3mXtMSKH8pdYLd1URVU49b88w5kqS5S0LusjdOkE1Z4VSGVYz_iHwwIhpyXKWD9KRpL845i8sjFrFStd2hGZIoezx04lLMC67d_ZsxK61iNsKiqYQuyPecjHtrRIUgqFLK4jnF387SlgZrzGtw0WiZCev4yQYifTumQtNZClxgjLvtekAOmgxO0fpC2SD3ng_k8wmmqMBweBXF8scJjbDi6RWFOxnrS-ueqQJwxFjseVJSX0O-XA1VdXnHMfygBcdzlGODyJ0uHI_Vtx8fuTxpOB8Qww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzeeIXFPeeNxhH7AVOLJZsuPVfEbqM9O2rTyL9pcjTYSzDEEcc4B1kDcgqTmvLi1Z7dlp9zLh8qeDhAZ1C5dULowr2jpfQFJsukvgejwz6v0fAgIxbaKd5N79jFqe7WpmJ7bumAkGj_O9fQWtReNcTQ6Ev-lYu11HZhuF2NYMUwe9jS10UB6nB-SNVup-ytujl6ta7vvU3oeJGBhF2xLoAhezSZvpgCoT2zgn_4hHAAbffNFl0EUMFPJmMZ_RIJ-VisS4-8r0P0UiMwp1uarh4vbHHq4Xn5E4C0QbmPc1atWHPxiOGADUpedXVPpoCNyDzX3gO7GPDlB1NP8w8XZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyZCDkk5QRVj0KlEmPXGNeMPxr64kKQeN221pDvf1pZSvzKpLaYtt_kbqEYc87jH8fA5T9bw5sf24fUbk4GCk2Ow-9hK5agXQRuPtxo9NyAkK07Oxe9MSHYOUiahB5iQxcqz0rjw15HUoS66OUmbUMTaAEHmADAD4lz-INUH5XMSlA4MxwYYiF-mUUmOaNZ6TRoIVmjyLMWzP_eI-hBxm1jn0h6fCVGnw6JRISWVD-0ZPdbCPjM2yfb-K-cds-c9B3fPIEh_yAOYLIaJYwEShlZ7lulDISE1OCZGqzIlpQeDEajIOyO8xWE5Pib3aqs9qxQbeGQvfw09Ex72NBPJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=r4Kw9V4Ixk0AJ4fHfrgSkQssYngmpgo5vJySfqsdJqtRjEP2-UebtPa-TZTuNyM309oc11EbD28URFdLVjqXrKebm0CFQR4hqqPIWmcVsdLlTpOiDm8T73hdgyKeBQNVCDcg4haLgsoblvkI1nwzIbblinJUhbMe710dxNBRIPqpt29bWgHyROy8Q2vfKGtQ7GKej4t1x7eLZjzXxB3MomJt6Nf_wAZbWxFm9xjGbZsAcvmalNQRJ0V5xWTgY5BYsd799ewkOGy5-rLeb1R5TGwr6dppheI6u294H9TfB9cZ5gva09Z8azvPEkk8qWjDieDmPkISXxh374g-rxJkXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=r4Kw9V4Ixk0AJ4fHfrgSkQssYngmpgo5vJySfqsdJqtRjEP2-UebtPa-TZTuNyM309oc11EbD28URFdLVjqXrKebm0CFQR4hqqPIWmcVsdLlTpOiDm8T73hdgyKeBQNVCDcg4haLgsoblvkI1nwzIbblinJUhbMe710dxNBRIPqpt29bWgHyROy8Q2vfKGtQ7GKej4t1x7eLZjzXxB3MomJt6Nf_wAZbWxFm9xjGbZsAcvmalNQRJ0V5xWTgY5BYsd799ewkOGy5-rLeb1R5TGwr6dppheI6u294H9TfB9cZ5gva09Z8azvPEkk8qWjDieDmPkISXxh374g-rxJkXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEfwO2FS7H1iKiv_EK7dOGdwqoNl7tMVX-uO6AC5Ji-HHBabFsPpp5nA4qJPNVxodhS0t3EjkHfcnqaH8S78PNmFo9npRiX6mCKA0NsHJELnReYbDRcUX8O5PMcJ_XsCMf9DOGYJ5cHZNJkLYPNHAJ-9vLvUgWOaPw5bGMf0dJT7I_RmpweP7yagHstnrNGf7RXVk8zFrP1Sa4mmp8q-d2cL-jNFrqD2HqxUSYfKNa4tukS-wh6gN6t3Brk2cBc8e0P44zxFDYlVI-DZpC7Lm5EkzMaRtz6VXxOHpws3yCcQTTvSahxiznFUiSQPqaSh6b3n90UTRLDagFWa39qL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er-fDk9gKM0RhdUiyliUrU35pjHl_sW1l6c-gyOf3sqFSj2HK36-Mzs_uEhVXnK0RKPQIhNSC8ZsSy9GSL4BVxI7zK-yv8Ha43KbLJVNeODVXKwzq7CuM9yX2puG0t-u0mmPUCAnmcx-2pV0MYhvWcgQ19HTD7LniJseKYro75flKRfp6eRH8Szw_utM04PJDLUGUTnq3uQt7B3Hc8S1jYeCVJo9vZhwFIbDW_FeA0JtPYHQpieaNVlSw69xKq13oa5zWdO6xPX6zIgWIIH4MmV5FwFggJWNnZB7rYquBHBV_5KiGfRlO0QBtN0kbHA8UdMHAeiQqxL52yL4Pd8xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=PCRw1nKFHMA19yxQBssAQrJpf17nPFkzuKTIks4HNNye73dXvnIPA98sy9BlXPEk0xlqyaEC73MT6u4YYhlDPj_tq9jknvq286XSXFQ1cwva1WVXQGYuVMmVqQqa9rLuy_FcAbA8PM_pW6_Vt22ZQwGrUfq6DIpLEJYDKTQDhOS0TjoeFKXarYw3I6HJht_emqUZKMXwzGnVCMTuxrcy6sLm7-9V2BVPHjvIoY0LxymYhMTxBTeGhjWkrTZAbQLmFtiHRAJ6FDxhN-T3fSvWavXTB7hXhOIZXQx5U8O22zqTjxC37btm8IuwlVZ9BgJohaonS5Gl87Xstct6K9XzQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=PCRw1nKFHMA19yxQBssAQrJpf17nPFkzuKTIks4HNNye73dXvnIPA98sy9BlXPEk0xlqyaEC73MT6u4YYhlDPj_tq9jknvq286XSXFQ1cwva1WVXQGYuVMmVqQqa9rLuy_FcAbA8PM_pW6_Vt22ZQwGrUfq6DIpLEJYDKTQDhOS0TjoeFKXarYw3I6HJht_emqUZKMXwzGnVCMTuxrcy6sLm7-9V2BVPHjvIoY0LxymYhMTxBTeGhjWkrTZAbQLmFtiHRAJ6FDxhN-T3fSvWavXTB7hXhOIZXQx5U8O22zqTjxC37btm8IuwlVZ9BgJohaonS5Gl87Xstct6K9XzQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHJxsCB357iyHOYKnAO5TrlwAHEex6saU3KGddQf7X2qO7FxvzzNKzOidAVc_CSHwH_v1aR11uCOZRz_XwEIk6oSZ_sf0Uj6PfPaFBTibUBFdxC9ShRPR9l7AON4ojy_Zs0JJ8gdNVk9FYCWbX1EQ8-3xhCuXCWtQU_KRWldZf6cYvQ-ehvaTkKNvHwb5rSAyvL3EdF1eiCRUUoNIg6QlEYTPfB-2c47jFLRhszrKGzZ6Hh7oOsaA-8ikJRN6ve4soOKwu5AO8po5rcyknJwAcuTfwP3taCDt16h5cLkiHaQxTu7gQ1H8dRJGt7Bxm_EjX1n51HYjod2me22cKfOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VcG9uoND2RY9Pcu5TTlHI2VPyCNlbWRJr09jCXAOyYjXlXK_YNQXCpZXuBmKSiI_JYFujJrIak79AN9gu9GwO8PNMjEP64xZaS3kVS3u2KrOjVygZ57DGfmEeBQQJT91SvJ9vQ_ODfWcMEkWbF-LZ_o334XwVNZBHY6JhtnyrDuRRz3t0PeTgRjE293kivTNIfSmHa7M3KG-sZwA42pqYEM1NzMx1hJY7YdrbwYdu9ZRot2lmVyyXDr3rZjg2xa4v5_GDGT6ELMxEJ5qh73vr2y4IwQQ77O5bq3xdeWy7oU5CPzwgO7xYdOt7yaQT7IbmYeO0ffZm-buVyyYejw8jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfKXhN31YgQSIelAIqjEOKh9wcFvtf7qrGxYIxm7B6sBL3wz5s_lZfdBbWs7d3pibhoH4YOzNnlZaiLgzkRQxYOqQIM6Ce0Nq1w5cDX-Dd-v4btiN8mah9SgSsXU0fK9E5w70AqoJzR3--q3wB5AcigOp5Qu1rknwiIBRvkkG5Ch-VkKIv4L9i71Auu42W4rpQ9UdcnpKWA4amXaknXmin4zYPZKtve2wrswJba5NsdenLZLLKC9-SYSupUOFxV3OPvVLiqUP7lyenQjav9gHplaKd-HIcMAByFB_Rwhtz0ZYvIAPyWxTogTAckQDCExL9XxIpuNxKLQnYztca0fNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSC4joQ4_KbJaF5RXeYzspQ00TgisszuLVWlFUaC4wSnO30F5tATrbd7GpelbSpL_sAS0V_8fAMOZokNxwh-t7yx1TcZ_rHESGKP2vdnVeu3mu1MdtRa6KC9ktaibwt_q96UK4hZhOQcepiKM38gt1CzexxbAdvSyMKk5xSo7XaFZ5wQWynQQ74ncM00pcaUsqT7Ym6TlIJCTRovsstD64thHkdSo89N19qIHPd4jRfYfLJKgbqEQPpkomGYRQUe9XQcbdpEMFShyQAvSOEp52I5wMPa9BztHluOZLfcu4SBJs1tcNWxKRxiE5DuOoP75dikgVOQxCbadkVrX4sf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvZI9Rrzdxav39alGzP5Pq9nd0syhJQQ7jjeHnNTMNZbb7_WlMSbItyuqb6BQMtlBB_-sAdwwCdImZhT2xcIPin9fSOWbuhzurpiAQ-9G37WbmHwfuvFUrA8soTKlkNz3eZWUnwjyX0zXfwOFsqwgPBnXwIrdqcUCJ1OevwSoxr5NCt5pelUpq24GNIldebst3vQMQTStcBrcSDamo0KebtAgfsV0VY4WpQKsBEHgSI9knpXGGb9dy4aRY6kCquBsh8FIBiWFZ7t86BTCFmM6c1gGuX2Sc-fGgCzJjyRZOAjuQacqGBpaAdYo7vaMNBf9uHf-nui6Z2Rbm4YesyDsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABKkIR1lQ1gJNoOKWuA4cjKuzr-bbr3A-FuOKQK3mbKqXcvJ4c6HEf1CGLCuSoDqvWQ3duo02KXuiahn1tqJCbhSm7nb7fdVXhkurw1fAwn_oxdV8rEDzDMnH0mzJKNcqnq3rdT4UbycXCLfigH4VHCkNV-aX8baYtHgnK7REkY0mV6bu5RNGOViD-YuM5PBPOG4JUSzy-kk925rAVcK3xWofbzlSUf3PjAKhLXTaaL3wG85ag1J_qThOz9Qd47elE4VVX8q67UnhGxgW13pu2hhYqFVK2TrStLlvoIVsVJ7WDbfTPFF68K8ilQkbVE7RYQgHmBT1XSydSZ026nuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5BLWgVyZjKoR-C4uTWvU3CqOsIZs2z_r30_4LqUNTBP803_wv0tuN_Rmt4XT61gpoZ_4K0WHzdH7i-f_L9VqgdHDQj0rz2y2y5GPf6QfGu7wN7-qYQ6-Wd9LGf9hOrGv-eBdX4xwuV3qh1HCUOSGcc7KIVlafRqChnHH0ktVjemxvry_Nf-De705Y4Gg0_axJcscQVNImeSRnWyGTV-rW1ty5gQkDB1P32FJG50fPnr9BDjOZWgi2RSmNXcCV3RP5QdCfg5FJw37QKPImB_xdvoQkyBy3ohgWT0x0kD9IiSIsVF0OesIES1LSDIMP8uAPUO3fUEJGg8zHTnVj56Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3XMin6fQ8l7urnnE3Gx17w3gktzxnX_LOcrJV-RVK6UqraXeGBeUj9duDirjIf2-YhIcZM_z2BNPR-0tL2T22y5oV9E7NI5dYra3Gt0dtaWyoGrX34W7QuB-N8DhDyFdq3LL5fCbst6iookxxW4_ffonEFfA41mz0Afziu_B1qhxvinDgHhg4mKn07NwDcYo0bqL1pEbEUVOcNPBiFYgdXLGldDyEshtazmAlK1EqCIMGyAroPL6XNU4KkdnO9vwyIamr5x6_VwvThQvUATshbRT7oU2SZGvzY7b7KglmHFZi7KqlQB2hwnGEkkoIIfWU4AukT0jRB8AFS6q54IBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZkmiUYmRKVn4FH-Y_jOk15QYyloGrLrgXlM2IMmgRTx8bd7szHlr8oZ7ncMMgzWLkrMUEGHY6psjXr5B2m_pI9lps5OoV4UxpDj5spICRq9Rqr6VHAcJekfhYrwB8LJSsH0WtvnoHSKL9pUHx5c4poeISnuZJDk5H2VVKrAASTPAddIa09iMLUynLBBglXUTLWk2k5fC_BXxD3H6TWKFYqjGGuK5P268EFNgT2J8dcyVXNaQgfUY2-4dx9IUKU_PjiL2VK1xppXevxR3DDawm0bRhWmLDId8KQlgOouAw3Nm93DAK29PsZv6HfkktlbijzzHbQBFiMlmMS9yTd_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DleROq3yTnBRKMLluEbYIkYA7AIeKkUmA9Bbgx0fclNIvmMXZAwYvDGkQcBUCSSERiY0v_u6S9IfIGdOIZA-y6XtWHzcmEEdwDeagGEXHyWLiVmAZgE44qxYrAnJPXgIoytKU16XVc_l3q2n8cwVkiF9VJF7gXGJ7LzSp-kWWwxlBp3pSuBIbuBfq4IaZDCXRvgOvZQ4FZrre86d0umQjctW0b-o2qdB-PDFW0hKfxSLUQi9ZblDCJOQqhfkAgDiSRvc8LR_AzlXU5sm6UusgjcKwRDR58sqtleVwnLm4PeDBtqfHmZx4TM0IU7d8XAx9T1XvaiZ0GtB0ht3esa7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE42BwOuPq1GTo5AVqKH5xEfiM12WhjQ1Q24CcEcsYJK4XMtSOfIWmpViowPwZe6kvXebv2mSc0BdCZtLBq8-4m-B33drHhTCVPw6yHGZJKauY-4MQKMvvyI1t3O3qYsnhCsPwsCokGIxyCPllRuB-NRK3kSC7mjcwCcwMwhbC15A-Ig_BiuXr2-Pbx6Ata0_LlzzPXgUDgyUpkubWQj-kuHpui1KeS9mxjjZGPt47qn0a4VMLUNpiFB30Eu3tkiPzXZX4Ia-AR2YgJxEFtlG_f-LNRF4SE1TNXmm56-WYSA537YA8kqT-oOr7O_BymXFqVscwcbEQOVDAAJtNQaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9w34_oZe_OiHQUcqWsAf9N-ePHuDoz5Of88PPG69UQI5l3U_CZDmpvq2d2hDKb9eerBY5Z_AwvyIJy-qhvLO0DUuXCs6p-nl_I_pdy834qVL44V9PcHBlx0ZTYqkKbSkcSMysKYR_z74VFoj-A3pzUkpmpWpyGndAD22L40E6QhZcxQf9lUzRHe_usZFoOJQVCw3pJqmflDaQsUIfZvwfrdKqNBFV6V_L5mKH_5fbOMNZoRc_qJlh9PWdDK3CO24O7HaNY7hyCNn55CjZ23XjYxO4lQfecMuI5yqJI58ZwBVA-PRl3oEFkF24mMI43edEK4lAWJlFqGEGsyiYxaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXVKNbFUw9mxK2nQV7dESYRntii5jbWgyJIWwyyMDZmEd2ejlknzWUnFGeVYUnTCBpzHK_C01M60VerKH4qjoygp0Uwr5F_0zVlbXd19_rHYmI_2T2NuJyQo7rtN77eK69GOqMku6vO7G_nZtrvM1DJ3-AMsw9SbUP2YPk1-uNREM-Y10-ZPXw4K4fMTuK5oOr4qUbfHoH_uShRyikiszYIwuZ2ZDJm86cNOtHchLuZcBYCz8c9blt7eCzAYXJ_4UJ1aLVhd7CS7qJIhLwbAm92CslgPBEELA1o1QvimHHnfwQChwBqiuzaVi7l4c8NYNhbK2WThVJZrJeSaDXpRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFaCoJKytA2UTMvXmJWtDCpT6IoLcyFWSLBwBAQxogu_Kmf2x6zJlAU_8yKF5ZnuNVX9jyWtSwqB6TcEEs8xowt8ntaTsqUhEKkXd9zzAa5Idors5Bnux7rRudiISAsSsOU48hCgVoYd93iFowDoIgxYPdm1jEzz15UviWqE-cDJ-DvWR9mEut3DCJ8qOJ_aexnYhWc4e4YHt63NQwCLw5Eo_Kr6-svfO3-Z6zwYqvszV1olRIU1tzR6l0XEFvwaTOSG-aF8Onp5-_PxK3QuHKPMc_kU9eLZGAQGFc-S9gkx2F4OJNx1UWV4l1myZqVvAkekO4kd1VMKN63H0_s2jw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=sAAC-EnJ6FJDTqeWpT3KP-WpUdNL2tBBeq3XdD8SXUN0lQs1Z3tB9umoUC3Y46zPnusGv5cRBAHFnTNNsfcE-1V8rN4pu4q0giO4BOAOsV-oE-FgYl9iEoSgqE5OcXhGUBgDU1yOnzA0FQVoBo0sqHeyVC1aOh9bKqlpWS7l_hvEJGyZad3k3P_yz4wlWW0km3qcjqq3rfLVeNYqIf3ZUf93S-jZIXyUs1_-j4a8fR0tABRFPcig_sm7HCjJLq2ZRLdwLm6u3st0z-5fKq9kHOZhX4fcEtCrTpfVoioNhoBZfR_Bd7NClfhu4Xljgc5dJBRa-3I-gsXdO0kSB_aPbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=sAAC-EnJ6FJDTqeWpT3KP-WpUdNL2tBBeq3XdD8SXUN0lQs1Z3tB9umoUC3Y46zPnusGv5cRBAHFnTNNsfcE-1V8rN4pu4q0giO4BOAOsV-oE-FgYl9iEoSgqE5OcXhGUBgDU1yOnzA0FQVoBo0sqHeyVC1aOh9bKqlpWS7l_hvEJGyZad3k3P_yz4wlWW0km3qcjqq3rfLVeNYqIf3ZUf93S-jZIXyUs1_-j4a8fR0tABRFPcig_sm7HCjJLq2ZRLdwLm6u3st0z-5fKq9kHOZhX4fcEtCrTpfVoioNhoBZfR_Bd7NClfhu4Xljgc5dJBRa-3I-gsXdO0kSB_aPbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJbiB5cD8Sg0m4_CBcmDpiwqhQ9amwjcZxCjOu-s-3Q5r2_fzVeGqFglzjJ7zwVPsF497MyccxhWoHTei8k0c_TkUATiHHU4K5Nv5cPT82UPu8zFGJpMiWepM0dC69s6oQ8Yj4ksnF4hy11fCybNJQzi4LDoDPWHYnoII8qDhSRp09e6LpPZ0TZpGs_QEXsYm1zoKAtB59LUEqqVtxMkz0L4lRBCCzfGdcU-QfPcC2e-0iqkvLtkPsewyalYiL9ARHLm2tHmFl6utuPnd4cuJfUNrdq9vWjTiLJpjyfcJsZKfPgkqLpYubKVcjaC0SdtNbzkw3EoE_hL_AH_iGh-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asMgJ8KC49vfDZ4_JgAaIQEdOFRCj_FTCC4UezqcPyZuukbgyPeKhbC2gLkRLEwUTCHaQdE2ytp95KLfCZWThsGjOF5P_HxnFaob8pFSWLKLTBXg19WtdqkjmPX-zlaKQynRvWzC_nTnIEbjseeqXGyOfyqnEr8AQAjVWFSPiiUAQbbqVomZai8NJYeQD68nJwN6KwdDkCPqjtcm6nMLDZMsclS7OaMtX4mK2TSDGwdwnUwS3UhbILIgK8p9n96dUfddAGwOijEEO9NfUesizoM2Y1hodHDybWX_l8aAtf3huGyCPKaftXrL6ezbjSp2rpEqa_EBGS6EQ7SetKRPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhO7suxdhCm0A0MJ_sSSf9P2FgZpN3o72h85_tsvv7aF48xxodLvnypNxiN6gVV1DRcStomqSTe7XzcBYnd1hhB-4nsS-sdQSND9GSyEk3UNqvB6LVlfcbRn31ZL71e4vWzPdzOeYLj9SqpvJQxcyGvxS5RuKb6sq6emUqPTunyxGHqnbvCDVvV9REHipUJCb9ARcbuV7wb28QFJu--pKDNB16BZMDcdNR1lSGFg3xl93kXYlUV1tt8fHHy8ST6c1YzVyu5dpM0jZjxiYqau16jDXyQPzSyDPZ6lX6JjYRq39-LHtbWjBtaiYcL8fTzpNoqKEqRYSfF0OETgLRzY0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAPRK3xIoc7wPrv9rdQz2vuuqz6TaFlyRKLVlfH5YocE77Pfc182D98duJ5mNv1jeC3C1zTtA-rY7vtQbgBp0QkOZ3cjdzEX319_zfScRlVIGrVI3IZC5Cglx-QT4qeabtNjn-8SaoerjzjPeJR0wz8ZHQKknb1FBYnu65oa98Dj_yEiTNzlj5sJtETjmHLig6Og29cFRETrKnP906MWY5jC6291bsdcH4S1piAYr47ncf1exYu3iuBKZXIegHs4lj4PC97smNvWPwSYaN24Oe75Mhm-2YkvrSvfTwJ6oZMxV94l-zzmsIQ0KtXEWOvMvSqTAx4dl7y1uZmWeJzekQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4iUnKPMqPr2C9kw0B04wQtFYQYUxa7zrfNJxDhRCIheJl_r8r53sjVK6WbWBfm7CUD2dpzkXsqWSrED9hmXdHKx4O10ayu-MicfRGBHpHDqqk8lFmKWb-GAZEnl7sNo6ZilOu2Kr_n9gGJcelZYY8K9p9ilNb4W9vn6LHwsOi8LAZIJojwf7L7KagWkQOZgQgmmpGS2-U84_kjO_W0AmNQHpXuF-mYSltF8hUuxjRS56UiZrka8JEmhR1bKw7v49nQMSSQwBMnYC03bmjs3zmv1PuzcKimzKI_M5_sTRiwBT2CVCZ42PZmXB0QtbzHCQjhSJHOIFH5fN5YzfBNmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dja06RzKurroRlnOrjdCm0m-UZRL1FrCbh9krwGleKH2E1xFjE40vqrUOVlchUCVp9RN4q6P8y6Fzn_Kdj3QV6ISCmkctUxUmJGXU9gBo7neUQ917vYkjZgnIbDcp_YI29aBdks9mUIswhYGRXtUSXSqPK-5o94yOXd-HDI7morNwbXiZUAmLXQATcwuW_88yDSqadvzJB2PpRKiLenGuCyIUYeI24qDeWvgM736RaDZZ8ZteVdv3VJtzSlfAxxayQLDPyV9_rBPyaSytAoPIMbBGX-fPmuqswgnVVdSDMIDdWdVhc3KtuV15LHFF4_XWftFBPNaK9AvOtuW8RmoIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt7VJpvSVF4mBXpAkQiA-lgViB3YxoeGa_Z-aVxR495bATQIaNOZVC4FMIp4k0DfZACOlb5KRmjSKtL3Fk0AkyJVfRWJc93QiKysFfpqnNiFdp6LRqhSSCQbd8AS0ocvg5ykKr6j4JfNLjmQW3XXvoR5Ym-UDQsy4aBgTBwp6Oyze4PkmMxWuU5Zb4dK0phlyVLW078fFWre6pWahvV1kslJPcsMgN5Pr2E5mSbkO0-X9LW5nCbnxlhXfjLknhV3ErWrk8bh84L7y3ve8T4OBhqCVIajK9jtZ_7JlNufRmD_MuRdrPmeurJW5Dz3wrTgbXLqIuMMZaTUHA1CVmbVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4AQGMJle5fBbWW17yp0FSWwdmbjZVjAbubEmG59Yu9-2iqKi1HdfihHjvNKx6ZAYPJiMvnx7_MiP8Sqdf7yU60kgXEBil3ZxlaUXCycDe7XGi7yb92NBxcctJuJfYSPBT0GzwRcSOoO_9XXlzJi3eGTietllJYA3Us7nlpCOgjQlP4aBy_PO76QkL1mjjGFj85xq_LYNouUos5_Da1WCWO3bQ3YnCAzcsEcGORbzkithlTtb2MQMjmhGUJ-MJoVbzZl0pUt1hZn8Ji8LFORM2-sNtj-wWvWUOptZL6IXy_7ZNnEx9MHq9vWN8KpYqCgZDG2lWn-4sG7sblzhoT_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOanzYzz1TqPsp8hfvHVRJ11AqfnT7Eh8tJM83bHAUS5px7drnxLnrieQJYPFj2TgZ6suWvqB9O3LQykauUfln8AVpj3ckMcHrZVHfUzSlsVjo9fFEyw15GdAqG6-YNK_sleKQCamSntBf40Cwv5oELlcDOfPH2XZcitq8AgtCV2rNSQ_C_hxYj38EVATUPOKyNFqBZ_5DuSVvlqU6heNJLJ6x5emVKtt_aziMDfCn_u6xsMGCDIIC9ArxVG-gS0TK7VXwX6jgFkBUQlYcoDIjMR9Di2Iaj15arEwCckNshvW65Q-5nZSkYke2hVKMJqRCRvWV8zg5_JJ-6x3daMRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSZ9ig8mVFos8mgxIqISgD0Y0TrCWwpmseHz4CWuKePFUSmPhDqftqSy7_q_Rb389pKnUxzTDXuE9RpXkbocHzhsXllwgrSzB4I9ENSdrYmpEv9A3U73vp8dZTiApQf_bRb3xu9Wbd9qVU-65fjExoEGPSvfBIgiXgBRv764YIqvwc-4EAuVpYVtXWV564bER3tMN8psujpB2UiEYmlJaf83EtzcXbJQMUNdqV6eiPcn4B3FLixvKZmE35-HXL3S0eaZQ4DlxBgUP3NuHD1TdisZ_ZmM2lmYHFxkzxAg0MaXfIlt0Q-IQLt-UboETWe5Y3Cab9ktLXBwJydjVz-Mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmUXjLNavAEUw2kYhOuKcnLNtwUZnQBWJS4YVohRdfP5jpRV3p9ZCrztKsR3wpOtmNfj_7Ig6lQ-ZjpUqc7umfYpuBV-ndSlMaQ7BQwJY6kDphOqui9RShOtao1iMlHi08k-RyW7N_YAHTaj4US2maXveXT1UKt4mYS1Yc7o2huXWwuWgNiy2HPf5Hhp6WuWQemiTB1w9X2NWf16ym8vrCodK_6dgWJQ996Z0tFkA-c-xJaaX-6Of3RJreLrr5_kWYOnfc_3EWZPmCnMxLb6lqAkZZa7GXAb0_GCgKFrF-R_RGx4bqS3UEUW1oxJiLIEhCbdiRE6jfh2BTU_t4pZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dme_wRnVLC3eMJLCfRPTtBWkmBEDSjPI8RKQG6mWzCcnGR2ZitIr-XSnK1FCDWx4D7IXUtg_K2EgTzTnuzwOPgWIS-VgxmcQaFnUa-s8tnu9RCMtlS4UB_-o0isTA-sRPu5fSyn1yBl78O4qVuMtiNpDHsZGBOdgzX_tIHA-SoN66oTX_x5J42BigD98J2-54eJnJ4lCmDUul2kQaZyHRe9eSRUDd-h4HFov6AoqElzT63got416O18R11VmrbmYr3Cnz4DqQHB26nVQT__w2gAlmMTWbCmlrtUsTVU7Guay6Zh82ae32NhOSZuc7yxgpP1bkAGypdNikq6c6VXHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiT2OfRssA3VDgP2OkFEgKitvU_m1D27IHBAEox17iG7OO3wbkOFpUCLq0kpWRHiOIdNxp2eq9plbaiMGt-CMM6uaBDGH30sw3RJyLoRhRlxJkZZ5Pt4YzuEt62jP2JWObxsAPvP5voxju4TrftOowFfK6j3dCOfcxoNiXtIGFcC5KTvpC5CqbDMnRUCdwK4UGS-R3Izo1gAoQCCWrrEV4-c8xJPilsuRejJS3t7-8XPd8kjDUBoUUXbTSTiLzBwxF2hLIyNWmrpIIcMAH4fw7iyYceZ_FBb3-voEVq4kiYj7gne94c5NiczfxcNPz59HG_-N9SiP68vYU0cRE-AgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6iivOpzHibVxY3ALRTfE_n32V9jJ7L-4QtIVMlwIjApaEhtpq74J-Ff6c6xDIz3-uzNUmi5fKFZPHDc80n-2Hzasi9AKbEGIXZ53taqzxduX9VBORX1hVvBeOlfdLmvmVkBhCqVT-hYc5EXxnr_eTHl4r9X253P8u-VM_8DaLV9-adm9DzA94xFi4hIukdOveSQFt3ErVUtAfTvZ0uyWcDX5uU1mmUKuFL2zkDaFKv_2LNdmOoaZKTEB8-tOuG0hg_EZJBmcJD_fVhjkvVmEoO3XQCzyDjQnN7DQ26Nnxxh_urUe5zMMrVkHeMfl6nvLDY0MMo9iXGbVTGpagD3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9SrdLe21e1OonA_tSPpkFxTMp7TFH1NdT-oYjCsAuwhzeb348aYJYbWw1qywGqWovZcjfCHF9V5y4gAWPht8AA80Pet4oHJT9ltAD_tZ8JU5ATu7lRsycXATGFvBxppfDAdAH8d--XHLQzKLGVet9U09P_Fhi0nTcFwSpyAOy4uNa8rbbsE4EADykELSEdiAm4l7swWhy3tIVrGNI6666mz0fbD9Prz-T1Pbrk6rvDc6i39TTKiTH7HHcK3lSr8FcM11Cqu63woS80Aoi5X3Tnshg55daUyCGSAU8ebgG-owlXUtdzbENmUtnZhx2vJMoLgZ5XdlRa_RPRN2N0Awg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjABP5tm-8kb5tjWioafzDnDpzRTsJQiTW2uElvCVUjYuG3zdD7rO-6QcRxWDtWWYotpglgm9OZBxTDtYFohn-lmSSFRn1KC2ZtrqyaFd97APN_bxTNVNZr3lcXMBPVdKK1auu0SoK0K10YDMWg5BdFQz8xo2MsQMN0o_F_XvcWUB9hhzLCbzKMp__0plE0UNUCH14yktBbh-6fQAK8rz3DKB-TKaY-aoSkolDTB_ni-4dVBrn4ID1jzQbtu8S4g4VlZtD8APU1r8A03MaUSy0ar0RRpBqSfX3cYWCYiv26-xU5vj8BUdFUVrnT9zPUWCVJWaB4i9CKmdQR-0eTfTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv00XvyZ7TwZ-V6EAu949l5O50TKpbIoTKF6c2iQzT0wd6WBycW-mmj2-SXWBUqD_p9Jb7Uil0y35NBfsPqEIVmOq0R-BmKplagyDDUARvgrFi_Fx2QkrMTPATqozPGHfb5Q7yeAIN5FaDKxHzvBQlpRhQn4NZXm1nLpowkHMCJooItcvvsfJTfITbMZlh4W3m2IH-ANFwhqyihVpYjGyEK_72WkgFmfXTeFMJcByRhPX6qjKLplUbGGkEx9DpYE-fXQ9156tlXz59yEixVWDfOCD85da9a7RzPTM7fri8QaNtqaA9YMPp8oEkSWG_sdSA4sgg6R1fNVXMhES98Y3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2H-H-2G7U7B4na5ZeK9Gstb6exaeRrxdbYkx0YEpGgIQHX8b6glrvBxx8FowO3JPqa-ezBeru22LzwKWJaXM_5ttjJ-L4Zl9cQN-YWliVgIeZ5LrebSx9eeLFXBtM1Wn4WbSJ95XTWcirD9qJvv0E0-GyEaWOU1kprrV90Zn8bEqaBXFUhDfGqcYmlruViY2yn_pYiE7ChScJnE7YtClwRiuf7MuUjPMNEkB9n6lC6cv0BGtP6UGAHKZ1vVEtASVNFF6Q-x3OsiI4mIxHbDNoFCzSqjuxLWxDmqGWDmeQ9bHUUzUiKj3MSVsY_OkkVluFY2o12tzeupMbpK0-R3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvYScy6U-akuZ3eBtNG4ACKpjmheMLo9leKqU8Rj73qEZ1D5kXcMVj0kgirtm_7QHMbzVb0AvAiwbYxzlcK83IQ3eP26tRyi4c9Z1Fkh8u-TWLbSj8S1EsLBLFIQnsmOEClWqZ8gvwMRyIAFcz-DZTpbLLpsemg_Sal-8EBMLrrr46bR3Hl_pM8fRiwFhBu1bhcwrEK_K6IOPm7nX1pkyWyFH6mxRnuX2cw36NVugJy4o6Ep2tBpYIBsehpvlsGk49bkOJDdF27KpgF2XCe6ooRaHki3WsDz7-eRoHrT4cZNtQ19M1qxK1K5FW9qNVMv3zrQAp0yzXrWREJYWlvK7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyoKfx2RZ0XYBGulnLpggQMwUsqBtGJaCD5DTZcKP9HGvzIbi1GhQOOvN4lje_qO3J0aiX35jl5cvlHRCng-nA-jXpJo-1jM1jVhOvehWIwfaMUp2MU4I9OEH-fMmahDmWCyaxaw246Rl3UxE8ogNN18LLejQIs0tRINu1mR8k5cpMkj1nVacYXtTiBGgHx-5aBzxEJuqjMt5GrF4_c0Yih3969lw4QJsM0g-AoR4xl3J2ekhHUO4Qh7jPKlQwbcVFZ8BuJHW5cOCoLRb_T6JhW8pvBWfOMHROCk3MZ6B4b_D3WA1FSA5pbE8LYQvfiwJUbpapu1wkO40ul-1l40Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekAG9InmbjIOatQVUDT5P4krBMkN8RTCGo-Nont-lK-vwnIrpF9TH1fiQ_3CT3g2b5-nfAVd4Y5sWvFBY5zm0G4H6TP3mOh2bPTFTtw74nXy0Lrnoy8PlIa9dodcb3FrSmoOKgTlP8Kg_cQkbzZxlvxyZmJBUFIvRVV7Jx3AWIUVqdUJ1KSeASLV6haAa4mZgmt3ykWg0zSdgDIWk18rvhH6tX1VdVB2LPtNmXK48LtQojOimGjKfCR-DBzGH7kHC6iGmT4RUkf5FAP-XBFjAi-F44gl08Ukf8kjP80JRGQLw_Bscqn3xl_T5RqG0dj049VDnrXqRX_wnMBSm7tnAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWnyiYMFNW0nL1WE_-jNmZqeHD8I1OhlHexdKcjQwhq6C67bRnfkGAH9Df_l4eCcpiuwfFTrPkyhLdaiVVQrbUrDzDPS0Myj4aoYB68Kjpt4af2kw_nMDEDOe4j-PIELytCbRtAhd5OLAWIwCpUYssZ1426dDjT-cbTt6JXmPZzHwEsUORqFwcMQw1FIgciCM-A5tlfuFfOt-ZDSsKQVN-c1d9a_3XI7j5Zj9a6Ny6cQGV0EIbkrypFW29RyL3J4tVEyuuS1GxTFKMk8_-fG7obuk10kCyhPloPVxC7ja4vJgMx_nSk85tjcYRW4lRO6RdvhZpE5y0nLzESh1Q3eTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3qI-I5b15-6jjNPxez79FdU8nTSndoN2EEIw1XjCVK8K5TWTnuPb9jSvnH9yF1qGx2Bgj1hqG6W7TKXdDPFOIrg_oqhqIWosluqVhdkDoo5O-ruWbeLAImWfTlBEb1RcMJnk8HFBtY83Hu4dmNkJRC93K1Uq6uqMdV1oBIOMWbsDM309Sy6t12FRc4VS2HI2DnIpGm-SKkLRCQ-8kM7n6fUi3ZV3-KpL15GlSTWkZ-z7ulBeH7aVcXgeF4Op_1HWZEx2CfLQrXfcopSDipRE_EY-O1Sy1KGljVwyjYsu9RrtlClt4jOD2B2sDxPw-ET6qWovrFEiLiK09qjoC_XBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=OFsOarOXGJ-ARb3C3ALdO81f8-YR1PVtIysNGdfuN7hvDg3ftmdOFTYtws4otQUM_Q-RD-RVZDG4KbMlZ9XRPAdIPgFdzSePt2QLlTzJ1JsH0Jn1f6Zrfvfi1c8gHA_h7fXFwR4GgAermCJnMv5vGVpu9-4e1h3Dw9LoEsNNt7F_mUxQqv_ZWTT8IyvWVQpU1nBja5yIagwJK00YSYVIaWHBYlOX4KgCPa-OZ6anPla-MqeNeR4EER6VhEK1cLvm1ED1Sv_TNX0z9mtcKlhgVhIFPKdY8aHDZjkpDNw2hii1HY6dFqxuSYz8xiXx8rmLgop7t5lZElGT0U-KOHn-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=OFsOarOXGJ-ARb3C3ALdO81f8-YR1PVtIysNGdfuN7hvDg3ftmdOFTYtws4otQUM_Q-RD-RVZDG4KbMlZ9XRPAdIPgFdzSePt2QLlTzJ1JsH0Jn1f6Zrfvfi1c8gHA_h7fXFwR4GgAermCJnMv5vGVpu9-4e1h3Dw9LoEsNNt7F_mUxQqv_ZWTT8IyvWVQpU1nBja5yIagwJK00YSYVIaWHBYlOX4KgCPa-OZ6anPla-MqeNeR4EER6VhEK1cLvm1ED1Sv_TNX0z9mtcKlhgVhIFPKdY8aHDZjkpDNw2hii1HY6dFqxuSYz8xiXx8rmLgop7t5lZElGT0U-KOHn-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdjJWnGz5vmnRzz43nyHM6pp4kAPTnbTiDUr1l8UYloxKD0o-4E7BPwOiHSDrD2vkcbmpP0Vp1TquUU_hc1uWXTBTBlSmjUKJ98iHWjUDkbCbLPoxkvWBxKtZqCqGsJWnhm6HaOXVzJtw83TlNVo5i8nxIkieDZb85yrQJlTLVpdRCkTWKm-FIvK96gnGjtt-V3dPbLzVOOu7kaJJrSkR0AOGo3e_G2tU4xkJlluZN0GI5Hjv0ARAQN-dWjpQe5BRrDIPXAwtwnxUYyJ06TALiv6kG2DWTEaFrt06Ci_QBX5_56sJzjxGTT75S5VVFJvCynUu--HF3e91KpayclSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyorx9qpIG4UVsBpU0233EOgSIBtzA2vYp9q-rShja-dAvQNwNCbDJxtpqhcLMzeJ6_P6lIzdhNilundz396CbgmBtgN06qMlUSZ0XtzOejm5vyYEheevh6rOhzsNuSBVORlJyd_Hl61fU4ZA6BthQ0Ze5uFjbtLkJV5mQq_wtsQ3YwCgE9oHO2Gy73fZPF_ScYJhPJXuHAkcHKOwowXYC7YRIUCw4p9IvjoUZOjdwWsPbY1kc9M4_TsdFEiOKKu-hLuiyT-O63wRAvC17S7sZTTlL26bEgYXWa_ACoknv-hUqX5Sy6mvI27ttJPAZOQyK5PoCRKiyYAxn9vMaHQDRgNyY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyorx9qpIG4UVsBpU0233EOgSIBtzA2vYp9q-rShja-dAvQNwNCbDJxtpqhcLMzeJ6_P6lIzdhNilundz396CbgmBtgN06qMlUSZ0XtzOejm5vyYEheevh6rOhzsNuSBVORlJyd_Hl61fU4ZA6BthQ0Ze5uFjbtLkJV5mQq_wtsQ3YwCgE9oHO2Gy73fZPF_ScYJhPJXuHAkcHKOwowXYC7YRIUCw4p9IvjoUZOjdwWsPbY1kc9M4_TsdFEiOKKu-hLuiyT-O63wRAvC17S7sZTTlL26bEgYXWa_ACoknv-hUqX5Sy6mvI27ttJPAZOQyK5PoCRKiyYAxn9vMaHQDRgNyY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkJGbFvD_S8FJJKyBmFy9N4zATYNEv5ijtgbbUDadx3ne0HUvRM1jrLMLuwRyuX4wztiM8FKmCyg4IhWQotYG_Enjo4VrNCc54SGKnANgK-Ct3zSxJ-rkfp_NBdgXX_7jpKq5-LXN9G7dybHF340hegK2iLSMAfffekd4w8qAoJB8tfd4UcagKP8T_zgiLmekjoaWs99ASzg9eQ7TKMbVVT_2leXugxzeSuUxPn-d4nLDrKE7M3ZWKX4xEp1Pz218nyc86-kPDne8Fk3cze5AQtTUNjOvAam3O5RecqQ_BuhSaUjrozGbPf_3Uu3xXkPkNYStGMtBHbdWDHyQ7L2gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d18gu6WIR3R1RNeqvYyi_pTDRinyzApsnSVV_IHqOZyfA7caDMmays2Uho7MiH1Dp618sB87Bzr3SbNZMPOv5PUQVgy2KsY9vQhRsIIdWKMYBaWBLaspcXf8x_NzWtWMJT8dkX3eKbLup5muDiZ8QgjwilCHhNRCEsNkENUrWIUcovUWysoUefY5gpv3GjC8B7M4WUQB662w4QYlsJyNs2HJreKc5yAdtFns325BG0jQ50xksQv79V6WKSzHEyBmkPnyIlOgDlfNsRx49RIyp2NdpBTzSB9i3S36LSgwkEr4uYT-t-0oXLxIKxzIvtpIj5yd-vTk3x8t1yZH9EW2BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNWPtgQIIzc1IKwT5BXlHIdc0BP0ed8VXOQ7PDtp8-eG8N6r9UOBHrr8NkMfWFMr7eiyorW2atUwvJb_jFHM7RmnT_eB6M8OZlxO_p90gfrXuQKo26kds8z36fz57Epg5XJTAsAMd-VQLzqB6zBPKQ3P1lQOHq1OFb43jsgxIrPKiqlPSKiyILw0dl80chp60Qcr0T3NKOVe7GlHc86V63U3ixkDGabZYTm6xetgAcKlOEm-Cqsj5NhfcO4_YLaolnbb2yMp9lHGviXZwQmHhVb6offz0R_DmClnR3aCf6DDNyurSaFaRHtdJ2YdYoYKg3OOIjZSMgBBTCXXp2YwJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXsdRqfzjol6ZuylpWjxor1Ayi_z1TpPDY7nYUNs-U8denh67T5MhQwe5X75ZJV_o2MAHG-cLykpKsETQ4VUX9ZEs2QRyL8mwQ1Uqm_icFMU4LR8jQRE5OEh7HMGKH873tlIBoYkjbEA2LpvYTV2qrXw0hqsSHdmhUM_hFHcw-Mfy0QRGsQTpyqH5zuyWHQM6Swh1FT21fIp-yfOBhGPIi2QqZF_4MiH6_FH7ObtngWAdgfEkWn-39uMWiFpzy5MxoMFxZXt0A7kgOxaf5csHGUetWvrwooc9yIbofxOb9ePWq3SEDwEdASizwOSSjXPywxkDwIWK5dnWuX8jKk6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw_1mOrVKhSJou07lG6D97405FJPkESRjiwE6bBJgQHKjhYjjWzNd-zxnRlkVE0scQJku41k4EOEg0dMwOJfUlW871d3b_7ufIbnpvy1uVuVYvVFPR0kx3CkJVMj2flw1e9U92k_dRW53ejPKl0m-V44Sc-Cj3HLmFHhujvGf8LLxq9HX8f0NmNXfOG7PMk6yBaekjQJTD3EFnbvRvnF7dbXtrSXBU2MrZ056kUURAKKpzW1kdaR00Qxmwp4OQLjtlevJw7bsQ8H_LH2k117aH7AoptZv4Q9_qcfjSBfMZOMgEaTZI8SKRhXQD9kwp0zz9_XyJiEIJSx1ShxIUE8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHONh38ZjD8yaVfeksfiR8kcXsyfmmcIJ2pI-EYVwfFWGFnI11_SgRmnuyM5JS0pUfbpTEVRoPxBQSi6Nzrt3epSXVgKJip2ytpkQNeH_JRN9IuRAvmx2omv_HeEOCEVtyvsXE1Wp3AYF1tyQtyAE0Y_gXSNylKveYI0SiP1Eb5n0YT6kEPgI2pLFaVRTEyLL4NpJoTf6MdubCJRQ4R08xo1uzfaGOBBNEKLbCHDUfcxh1U3W1hwg-BIBLRKXyeRXy-Sef4LkZW9xLOu4Aq_rrzp631D-v3oQu8feYIKNg1IllOYqkt-A5DCBQL8qzEKD7FshRajhm6xmqLYPN7-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBswSh3KqpMFwsiq4EkZTosL-MJaMiu-BNAJ7hDTIzWXU3RzDg5FefCHU7cUh23ifr00chxVddSpAopzLzE-cJcy__L7nP6UL8yMRAzp40eATJO8816KTZM3jDpUUbO2ZJm5rYVbQ_YDJpBtKAM05IznQRog6Svizm0tEJ0nxZ6zpdLvtyJofoyBd7uVELJ8gkhp_liMb8ocBSqbZestolHYBMpxG1NtovwWILTRJIK2CuRHXPtgRiIzK7r7thxAmiOa_fkJp73B8G80dOP8-QH3Jmx3kzUF0mUSpBfxdwdet6ChYeZ7lVxhJtA5d9zxXAcls_xhOexyHyheBOXRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYwoBmiBorVM2ksLgygM6kW03C8q6N0My3s3w2tCGifWDc-RMgIYgYboSn05dd-ZDvM86YdBAco1XHUSqJZwg5nDYt1mI8gK7fqEMBYG02jDxFjtt9F5h9YOOAIPvpsxACOmYfw7_hANbCHN7rzni7cMtJbZJcMGCddUqDj6JSaHJ0d-hzdC9apZhyFnE7Qant_Za-DJBT-r8LM9-90BztIlPm8pLM1018YhPVPoam58WWw9WCWzoSxpU7ahvv3cuKPssKtXlgDh4yvYHvfPRsK7wFnCR83otW27w9tEoM2EoBn3TrHZbxSj7_6jE6TZPDU0QFTWCD1lb6N41FLn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GooENJhdXYFD9bX-9YmM1U7DjRvzujNPpTmdfiMtlgH9_ZGL2NGu4kzQwYkW7I3oB88S98YT2mnPFybn9K-4ry_Er3RkTaHWqZu_HWWZ-yuQGcxv2Wvzz9GRnucIR8h2p8MnDRTYw_qqiEOgngqhyUatL4KuFPNUGTtnyUmOqeCGETnS-sgoDJyc5PhjxUrd4KMcxkxIksh88rGJa7YwTZ3mq6IrfVoevrVufTi7u00CmJ30B3400HXOIK0HSawfuTSVXPCjJV-92xgga9pNCYeRBy-8mvY76KXytowGQ6QOVZr0j3Ntj4OaX5KmgfTrQLPCtjWSECnEzUUuakV_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jk1gNhz_kdUG8rJKqM7dPZnTGAl2ns0apy1lMIsH2pAS3698wWvvDKd7zeu1rVDCLTAIoJavvhsbYhru5rVGJqlz-sKshIhQz2UKS8UBTb_EbhEGHmp7R_bw1kK45Bw14iVdAwjwowzBs1GniHH3jc6hNSpK0I9Q3kTQCBwhujrO65tkqIh_goKleDcVphJ8zJZ4NptJNj7dSowybZwCPG3XWDSoZXvW51jMv8zauJsuL3K9YgnGTct-sPmqAXKMuaI05RjZa2N5DtAk0yvPFrnPQTTSciMVGPgjwXD9iZHqr_WEH-hP1ffjyXiZGGIWWBu5W4j8_odO1xxkSbw3RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZ_LQ6z0NwYzbSdavPRAvQDPSGGF7rQG_fDcomBpEP2pchn3xVIABnpfD3DkfcrYFQUYE9j2uqOhDDifTUq35LmxkiywqFkcFbpsSXDwpc3XPBbTslMtpyql36l-gN1VbXmMpiFaMUo6UX9MypHrkOfncqhgW_ojl_avFeQGZEo_kTd6UMUYhOpoPUUVc6dQRPBxLU5-TQNmHSHGebRNDWZ7wo1wq5IviLXbLEZPp3w-SZP6e46XoPaqQ2OYWLDTkhw1gNzTfKGgpxZ84isGcQ0UbrcDef0Kb2rYWDRM6yCP28cXCY1GkZ0QDvia5r7vMfKN8RYBTCPceP2wcX2VlQ.jpg" alt="photo" loading="lazy"/></div>
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
