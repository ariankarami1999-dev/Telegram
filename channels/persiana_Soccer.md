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
<p>@persiana_Soccer • 👥 207K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 20:13:28</div>
<hr>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7dLWrHg3zcsCQRVGlBaIRQlDEUZhlIXTZm22mwbknvXQ5XFLrubQzwIEbYCXf9F-7l5bfcrUqVPJCHuI3BPeDdzDUMnkkDoDlgKsGvkGbe3KO7RU4DSP7D5mNvBdZVlJ1SDFk0cCrFxBWFtI6oMFyx5lsuDoyikFdG--o5JJ7gUc06Vri4CpfqlbTx87llEls3FzfO6RbHDW_1T16GJmTDAgmvz4vbQgffuIMe7Vy91mDRJwjVARb1IHDaY3BRPWETtPKvtejVa4hV9c5b21xS0td7u2seTQBxEPxpLVCbd1_DWhA5JFQP3sVJV4lU1EoMxFuAY20k6JXh4Da4ZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5cRdVuBCUAeEipfdJHH8X5_prW65t1BaeYNsNs4XrERQMY34DD8Z0ehbC5Dn91O5WNqn4edlrF8w0dVmnT6aCmgAR0i7wgKKAa2KuwzghH4JakY7fUVv-i_BQ-D5IsueZ95W9U3nb7vhCn22Fvky8yGT16VrlloSVpPm_-IM4nW6-NN4jhWihaLmiHMKQdY_bYt_lf9ddx3r3DSfWWEbpEA-iXJiH7LZoPaa8ZDTNg5HGZKKNaxRQMe0Agx66DvMfxi2xAbXBMySuoTY8r4OZUiJksLwrymaVGTTpRbj-gtsS7xQyFRrSy8J2s25FdLUE9S_C-F4QRtSvAl7sz2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y900wnun-3-tv5y-Zb2J3PSH5fXG3N-7ItCe0uYTi6fW6wsGJIjrI0dBw411Kortg8qyx9LgDjvOari-FOjrj9kpITafdCWBEGaK9tdFFqMp6YJWfux8Fop_4UNbuhGNN2KBYYFPV83inS6fxqMfrlUOI13Xf41lk3kB5tgfVrsmUkLaG976Murf7Sfu0Gygxv4_UcAM9eJAJgCDgulj3rWO6SCghVt_m8CAHDycYuvgKuqYBGckObd8yIAd2BbEHCQ16dW4fgtdEMtFAHPgmxcGmZsb-c-cZfbfxUHiPPbAtLndg6abJwKT86JoAffba0YiRoqZ2H5eg-jPCivnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/persiana_Soccer/22166" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHOApNytjJ3TU1eVvYc0g1F_sNDmsGMLpQZUbfOxXyuGeVMSes_ROYs77MUSPQV1T9lZGnAAafLz7IPs2wX69UhNPq-vVtKYgPHIp2KOZ4Bnd22RICkGsVKETFPfPX7_G6oyNq3pJC6DKoydaRYQZ_QUSMmIiuaMY9OPlsEVO6S58FbjpeP4m486XeTTxMB9rbjmzgVVlbOhanw4M3Kt_FeRLLe6xiBSCXu1_-JDoqDF584SSO0qBDndoe1ZoYKU4qiq8hSeVC48yX35vO7qbrdZTHLnfcT51LiDCA1iRUKw6ctjzqhfx-FyraiWrBVlp0wzUaPFv4QK658Naht0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdDwpnMygaEC1be6ROoVIDZnF0YwALys9ORTHoO2b97txD-HbMzIFqbbkg7UsyJbKHFwSposuykdOrKx3zFp0TejSQgipAbIl_VOx8lGE9dgU5yrYeMnl72qTME5VQtliLF3-jI7ZR4yvVHmUSUFe-g4Neye8fW-9RliAoTEDl167fIZ_xbl-0m2zECFbSRPY06aUN57OrLr2MwYkYUQ9oTuFcUt_m1LKVdXjT6eCBPGT9pq_ISXHn6bJuIg8pjYXwXTYQfTYxCeDpr4lPGjSuASardex_RYgjPEqX-zAMmrzwHi1fHEo6DZ8nAmQ4DhsWJjqAsxCosKrqOl72CEpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h33ZoQoSg0wVH2_Mz7DEPABRTWVFx6vsNf73h5bmqZbSsGIpCzoE_YC6WiUw7YIdyFwss5d_zCjJbsyOwiwg1FYUFx6WDyKYrEcI6sAsAHjq_AAcPY1r2EZ_2DTCAfSEq3lkzDU-bfKz9AKHxkVYFEUwj4LBXSG81JNxjDTQTSuzr3wttjQXvRNKSFJ6UsMhT9DErpQ2WUfeNkGaXMmsP_afR-JZIrxarHn64PTUlfBs5_bSiXq13JlpiGRmZXAoIRd5Uu5V86JYCJOXVbCjODqxxo_qRIBsa5yIkbDjUy5lZLVAW7r14MexEOXiI73kkdFHK_OqPE0i54bUNzZMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5KCCMqoDYYzt_CFFa9lHMGaRTkG9LrhGV2P-hMuFgou5w6rBRWspi0exXtr0U4PYgQPiB6-zcr0IpjwfM5dTTSsC8wUK8yKU9Lfit5I-3ZFG26FSF6RkvdiHmb-Yy3CO9CxxFLjp9In0gzBRHbCO0KxaZL4I8BpsFY1GaRAi2FoFRDPEf24w1eJVWSstaDfZbRSx-CphltgayfK29eWxcpY8Ih304pnGriLsT75w8OH_EifuZ8y6mE_NqiSVfiVGuLb_2VnWmwTZNznJxSE43y-eIdKee09B0GPoN6Mr9Fc6O2fJjg4fC7q-PpjDC8K3qCapmr5_sSgGxjic52Jew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFK8N4wp8VGERj2ZoZempEFXbLKUrue9ESKN2Gz8ELtT9-Uw6fO3Gg3nE400SJDDfHzwVd6X7mJ-pNNJkoSU5YwPNZXN338WpKCrz26UELUJZdokF26pjEdWCFftmlgeipG88iuYZwvC_JW1cmktZa9nuJW7-kjbSRmnf8cuj2Q5zsSuDN0020AcA8JYus-Nih4225Bbgi_z-jseG9PwHWvJMkT5jFD6StwKCfbHxJogNZ9N1QENNiwoScu9IBXZwDKlzAJj-etw_4u4ll9VCp5sKT1lQAcOjl3XGbrmkw9P_2_14DIJlJOIbrPoLL2rvydQoQB1oiggSqHUIfyoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6zhYLla02CaW9Z1kLzg7R-Wj-a1SQsaRugygVbixauW1oMjJuNDZbN0WedQC3FHb-u6J0dfyDO12WT2fr_Ml06o5k4zxfOLRjUlhsRlwsWz7f7riuFC7tMFJDcyCjVmLEFcaXzHDerCQXdSPkVVFxPmEXwBjrhR7IvRgyzzyuk9gl9UH5-vcAJ3UeDg20ObHsKUa1YevhjEE0_tfVDQXdWwemq2103uPXqRi70zfUW6pUyUCyRLzWNcuk0sPtEUWnYmKDUcMC9vHvkQT-HQ0hRnefoN-Pt51Ppd7FUQCIkY4DK1HoOLsxpybI7MxFDXZ0Kb8WTAxk8ZONMtTqwCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBkHqhLp2T-6MhyjtLZxHZFZbNBkB8X5UYoLZWXWaPUe0H4VjJ_iOAOSFmJXHRl0zXZ0XSyV36YHhhHyHccbNc3mTancajbP8KFivfuJAHuP1V1ppwUZpY_NpQxav1pbvGhTga7GrGcny2nNCDJeV1TLwIXGNljVwyV2jPYdnlfOz0dIRPYY7x1mT8nCN1NQVvUDvm2qHVF4UxEZk9U2v3NmF4v4BJRQTWrs9ikz7diDN_sU81c56LPL55UhG9Ccg0zTifTEWMG-deJPubXVudmrjOfze1orXpCLpPOz88dJimbyO9K43ZKov0yzdAGjNvXdxIuywX9jb33vtdaU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO_dRVmAntAUHYOkP3j8i9oA2dRp8Oa2KAY9f87Fn8h4a0yFLbLQ1s1nDMyLaFPSNc94mVxEzMM37tUfa4Nac_bX68eNLi_LNDk0Cj-W9mzd4DU_ubVq3d91Mw6opPogbTmQxET8dg3xTGqnc778sw_7GUn2PE6cHjuaJy7LBxDgT-vL5QtBzOOglklyR3uJSI7zRLONj4_rzrxtSZVlZi4mjBR981YJPkZfticsjU0QV5bkS5EcuYINOohAahWxmBKkfW-nf4gQbLdl2Di1nFzOxINPoyCZqcUFReDN8zlBfNuMhD_DgrU__GsG6S1OInv0Rb2ewSHS_t0TqwUGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzfuEhJu5XQpgUjvBVLoynzWIBGbrVsQrYooYfSzwJnwG7pQx2gihvlZhzmtVypRblxgmN7uoN1UX3lWaTspXkkz9WX9KYvn4CXt6n0lldX_uswpSRmpUuFK-FOvQKFK5Ur69nIBlQJUkCnDhN6wOnjQi5MMqYUoJGZ1ufLL6j5aD7dZHJH2zzs-vr11VaTm6pjxJ3eCyOu-BvYUVG4VeWSqxxoR686NeZLoS8m8ISU15z9o5-kjVzbLWmsTFbMgeXHjrwtBYPBqzsZZxme5_Hdt78Xc7l-CkPv98adDJv7BgqyQQ5qOwtoU-4u4PMRTBJPN4AHDJa5wb4N8FT6aMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3bbSOpqj-nLMTBokswYax6--qXK0TJ778d-icenqZbUOwhXDaeeP4mM70bkrZ5XudGOn_nXcmd726FJbihOBS_IDuUny8XRjN_bfhbPfC8_C9LYylrSLHW6fQSsB68x80-n1ei43ZytP_Geqdh8-hGOCe7uaiLbELs94hww9wVH1dVpgEb8IN-AgvyRaieNndo3ts9nVfz0oLPsPL8Ul9VUXYiGvOoCkycUomrJ3hw5W-INmrzOl9QGyd3NuXzC7q7_rVX5LqOA7IRzQVNm2I5JiKeNWu_ZEGoA3Aisc9aKHdJ7OE7JQP3HenqO7KYG4XES_b4sN2G7oaU3vsIwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIDrcKPErbyWHiq6g5ZKSQ5nO_xgHAZVwZQ-koocECH_916F3UUteESTOTAiRuxxoQxZ_Fpa2tftkYqcJypPYeMP0atpvENWlHnvxe0maeh98N3xfz6Dgv9MHxpVb1tj42S0BdR4Zwu3SNTRnfm4Ir1pp0gZKAhQMyyfMeHFCJUa5cncaz3cRvSmegkeg6t05FD4j5zuAKOAC0T-udIb9oF8SO20IR2FzjnSEpcSYFnj74HMdtJ9ZxGxWDYKsdFMNjrGMocNVMdgcoryVAObEAbaSqG8dJaNY5D-rv0iqO0MojYvOcuKh4GYRosMANTevpzKtqBTdmRy4IbQLF6JiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0sgxYv_PJ-2R6N0YuqjZpH7OcKw6gHmqH56Lw4oxUHzLik_SXA_Hx694-2IHOyXR2ASSrw-3JmDs-d8n89HyuUD2m73jcai4Jx-J5hCgmpuW07XvN4QbNJ3bvdl1NeRZCtMQUGlAmlxuptA6RFp2EIiXoIsBpKsog2obIODoJBx1IxFwFUFiXXp8D8vwYNy0KaQ7ZGyzfrE37eSiQD6eG38y8EOVnGM_fRTK-MYkUcKq0OW3_YTwN53cH-NmKFa_vltnpv_Aw_38Rg8tczMzwhMiLTfmDUfY3SF8h42BerVwm_NDBq3WSQc-GwcjQDeKqkC7r6JI-WTp4SfChPaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ld9xxsfDx93JYc8hGPSZAjueF2H2AKf95VhhUHZAGoKm0QlzsUd9XABpFW_82upH5VePS_t8AwReduQ0c3QKmHC73Ls868xawYccadbs916QU8087D2N7Pc9lvOVQ_kFgLPhcYqLntuce4uyK7z7BdatCec8b7f6ArmMZ2TCsjJ3e1OEtfLBFBjn_D4cwEvdwHKZHEnmwzWVakoAGnvZBikzvzLo-WMKdXF5tp0IxvX3K-AN3aPuLaU-nqRBMu2vPNET_Zewi8bqj-CNKO_7urEnW5WS_XFETpPzbpAUMJOINVDBUtD5QT7mlDeQqLmMxzvi7vlTTipq4XDqVxtNlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojcH0NukTviMfqsM2gHqSfwYS1z5qak1VuP-u8Q2tqHv9f_VfUxN80F9ShtYrYR6UExiG5IjG2HhBmCoi0KlzAjOg5jGwglMll1m5QTjsao_zzmKg0GPWk_MV0v-ufIclgAwYzvUQr_MxE02ynjZbi340aFYHDW15TMLN8MysvtH1kYMUOz4fTb1ZF6sX9UfHUI_hLDZ5ROYcFcPJVWtp6p8a50oZrVYfKfaXTjCjI0HABtn4WFpAW-8VKaN0YinPupmPML3Eq3EVFb9anpYi2Yg_5VSlCNHUuhk52O-IzCIafO4AIpZ3anqI_49RX3S84cGFR16G7OQ8AsAxgRMpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7eQ7ib27azYWQ_KBqUxUQUnBhO_NEjt2a9SbZB4HOantbA23NHDGqVLsQct6p-WgbFfy5WcDBQaMdPo8e-LZLwLOFRSCrCqShTZP-ixXhCDBKV9HHqzQx1huUArhqPNpXPdV5RiRU6jbaYzOXMExLJ-CVbjYA4v7UUbNKSSmnI7xq6OmtByypO7cmJAsOkxJnzi7o_U0UvjHkUZBZf0BSjOaJniYKQWK-FCwqmAaHI37J3_9BO7X1PF1Fk4sbre4X58wyOTRVOUxaeKDAwv0yXwDbqjkoyhzJj6zDb2qMurkTL2BYPdeClWKmH1SH5_pX3NP7WeNXSB-Ib2wycKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpd4wbofHwDKbUAP2Q1sBohjc1lZDBeGcsnmt3OoCKtg53SsZKXWxJ34MOyhTk5sd3NRj5py8fAb_Y4PxpsxeaatND2kQ_1yHfU6yrRNXr92TLXFozz8zz6o5wF7JUKDw56r3xKaHDmKBVPfqlGWAIIk37a_o8-9pMe6dpRNT5voMOSHeP_SdPCwwjdVSivVzHn224D9jaEwVx0VsT_uHCt3tHnvMiGEAbsrdlMJwO_rfuBV9CJGuhUAwbPArbL9kZn0MNkycvvrHTUabciVMQUAKgaiQuSet0CKdSftRKev-3dvcKH48qoxvZrSL-rEGdzfu4qEry-KdhEYb5om_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZLvOPvsXARcTF-g8zB67Yr3fI0IpX5S_5UAlfnGRikBOQp1h0rIQPRC1gNfBXAdZDZ5p4XxhY0KVbygYdrGbyrnQOd7pq7dObaGCMtY-f6SI1pwbwjntiM1PFW3v0QOVH0X-FqRpc5zqYIJpOQwiJBNtd_HeUgtubvRSam_wczrOFeTxUZLIye8kWzcMo_Tqk5d6b4fD2DUH8gb4P9kRQgIf8lxel2IfFkeLjAol6ExSvwq3B79jPLAPa5UBGKCntHZfaxhvcatV8vmqWuQQtKSOsANm9jaaPOMPgX1MGpx8NaJwfTkVPLp8xRf08gQuQL0V6XobSr7Byb58JQ0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu1TjoLeldOiRw0Yijmj1XhJPkN9Lq6JG3mFdf2t3jynVcaivgruY3TBWzkMSOIvO_DiNSGh9lsqjoIuX1-GNbje6VIyPaMtmsD6NYA14X2gDqo9xzNLNTzpXGz3wHuHZW8_m-kl_FVfWPVPGT-OMvXDkVP9SnsbpFWinVOcx8_QY9P_tLdNr_e-t2678iYK_3Ct30cKQ4E7pBPP6BKnVtq6Bbt7s7EknVwBoEnuYFqLqp2_RBNstHNS2IMRVQS93KUU4_rhm1_eYYg9alUJRY-4BrhF750GmKFv6zwidrVS0rkLt70e3Xu1xK5_edR_FVeCbb4v0Z1fOnh4XbgnCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kigt8Q4kUqpJAtNzFqEAkDOaopJ0CCx_Dp8kEvbGg35Jgk-kmZkptXeHD7i51a7jQ7kV7rPmrgt6vdQ3D0_8E8HXwnFNhrnFzjJ7gysjzYior9nsk0TrQDGxaNxZ497v_lyCiFFMtqDA1Yzz7ND__NQqK-wOOYhE4wmaB3TZpGSTp3fmzNW9WoffKXV8B2J5c1ywtMkXLRtMCE29GaplIaouRqcWDR39y-nUwZqdROzAfhees6I5yH5GITwvaNxf1z3W70Lrw-trvYYt79t2rJaW3Q2IdZGJsnkvNBahFhSwWdwhM-odSOVtUstCf9Bhr8V3nOrMUA7rAT8ll85dPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdGcppP9W-f4YMfZJPt2nNNlP59M6dXfR5RahepHfd9xZSdKqFW5vaCb03ptxI9zKtel8SXcJQ1oHwnGG6WjaiuFWSi1HvQrJ2HiUpsO-kYo7pG1n0dft7g_5ubais1H9YY3xav4p9856pfZ0plOqNZSU6Jx_JqZOYwS-JzHGr2MA1QPMAvf69Eo7_qiTIQa7qMnmgCtboDeb6VvsJlPt35-9CUhfR0j1T9INuIciodGsUrwDxX30gpi7wsYPodRMLIR5_mAuK8IvdSMwBJFWDO5B5tIXTb2zm7s16dqdhmMbCoredn81FAWgIo7WKuCqh30EUB41P79_271mtx_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPReWOzXbaGAQ5IvyoI8nr1difGMLOOauh7QZ8EBEDMnXDzQHRb19uqPbpz_5uWIi4q0QxKVtXggIR3pVrDJeLbLQxaelIrw6erCKc2cZ8UrMJo5pR0ySSqcnnQ7K2ww25eRVFuocqjPkg2TCqPiVPeSnfy5AijJC2qSWGy33jlfFjwq1aWZLdm3Um8k04iGBoOP87dboX-tKxtzQ4KQiUHjVVD7_kQhVfG_xpnSpM-NFnZci3y2rCCM6DZi7wVU5H4m6YldS8f47MqhfPz-xYJH2OWxkb3YxQuCZppI5-2zWaR6mjQhpBFghaJcu2GRUxfR6v_pPpPOZSB5hjkF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjaXNlM2JSxicmL2xN_LtiuclYtO-SsjnXePhRX0Sb1VI6Nyui54JhetfxuYMMai6Z3Kdjl5KLDmfacXvmCAGFM_eEuFUPtVP0zBJLPbOKt-pIpZLNurC43UEt2FhQga4qDFicudE9XiqhJhqjTdncetl-V5A73BCGWBdXO651hEqikFFF0BmzzlQ-6BWFldyh_CodjaKkgwZb6H0DxZl9_Wa0UzeNsrSr-9zH5iwiunlogx_eKEaGSikQQbmapXirSC7z-7c0ZZ4_J3RnMZJ9WPdDfvPrtGkG1j1yIkkbnlIsw_LQQI96yxWHvzsHHqcbWTdEst-9MLWNTa6QsVDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVKcx3NcpULoYKuCWcZWbyv4reNM4JBWs8U3ePirvb6-9VU-v2du_UslnEhhOr-SDkZNBjcOGPvDxu-9vQViIpjand9Yn6B5uD81FGGx7xMhsBwnV0R-0rKbGodbzXiUhI0MWouQeGopEoPD93ypZQmiJdm-ZrcFtiWxwyrc4_tAfnqPU8GDrVTrzJ0wPMTRMirZjP0nUxCXqynifFh3CzzEScoKysS6a2d1ZWxGbnjqAXQhVdwQL4SVMuzeWw5anij1cf4heAALvCBUx8as6Fnr1JKymCJP6QGReJ3rJ9lFd08W_zVkIqD68jxa77Z7kIoiG7fcYtlu0lL-uhPuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvD-BrQMCErWoLfCoGZUzknmYjnxqHpQ15lOi6XP4IjH6WV5ZFnYsj2N00nj0_F5ZJDh8XLpCKHDulnmZAqCvR-HbALqVx-OOiB3qTOp__5I3KV8_epMtOveBvZ9QHNJ4gI5ZhPjNIUoLZ3ZbXw74m95g3ZqYj3Snq8R9KRD9TgECdCJYUWGhkhnN9qPF3KImQ9aBcN7OZjHvTPRo2QrXN4N_Kt-tur3JbQKPmFZkt9m9iCLlpEUcDellIT8GXvcBlwUVwUg_s7PtQxpG1coSp91JmsgzJ31PELAXAyDY06JvdIA8b2eE8ismY1rLS-eBbyIR3G5PdrpgG3EYcpeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBBJIb0usohul7uv3ezFtVlusz3bXSdwFR11rYo9fg5tGla1hTUqsfGLve_NcOVUYcehc1eROoD2nlTj5yAvzF5F4GBP4X_4yEZINlFTXEhT2GHzuwtPVb_sytr-rWNmdREEwHjqjqi1izeuC2LmLEL-R6eJtIjTwDkHJvFT2aVIodp3xmFQs5VNT7MRt2lJ_ipr51tZzFdfLYKgcJyayxQaAxwFy52uIjGS0EZyiVHf_5tfKEV4uJj7OYFfx47bo561joM-k63H-_yd_mahHSenA7KmraIJDUKyyILyRIrZwpN1SOb3DzntUyWEg7Es2K8Nqor00znrtlY4Pq7eqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED2U0DcV1kX_-I5EsSHQNiKsKs2YDlbODBkZywUDT1VGObLbfNQDsv73bMohajRbK99lZvCoga-qMpELQJRVJZ2gx7uG-A6-pnNM2KLi4sTEACYEOOP_pMZpeo37QVnQ7CRJpEqAfX4Jh-74wx86dyo-TZsG6KAo-Qh8jx7fOZyVcXRUPKh2W2sEyaXMCyCDMZBspomh6dsmZop0-6A7MOit79RJTZi2PYqr1KSPlICHXglILmrJmSm3K5begxv1l4_RhmOo_KdlEJ6Ke2iLBF2IqipFiVM7Uh8YTVPbNZ1pgiXwVfMjjUfN24_haWzLwUwByqN8bLu2sFjkcbFFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=rta20puAyE1yP20SOA_IwRhxQb_poG_7KQCWgeUPE6I3JVPouW-fhkWDI5VqKza_sKcwPnfNV6VTklnLT80fSfSOcKPUQPzXffpi_oMHwWT7OSMfblXHykcudsI0iOz9cvv70_QF0VQ_OABDYkuCkMVthDbqLs2JyWM916bl4EwqqCx6DPX8A8umOdJCiRZDaxePpj3xPt14SeVk5q-hd2CbczQtPczyqqJXCt-TijygR3v8LbjUDYOlftQYaczmd6anGjhEfeG4Rj5IJk4d4OKOdw8mL3dw2pEuBDjmD8AUOsmPCQuZ1QcrM0oAWJnpUE9y-5CgN37Jq9SXwZa0PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=rta20puAyE1yP20SOA_IwRhxQb_poG_7KQCWgeUPE6I3JVPouW-fhkWDI5VqKza_sKcwPnfNV6VTklnLT80fSfSOcKPUQPzXffpi_oMHwWT7OSMfblXHykcudsI0iOz9cvv70_QF0VQ_OABDYkuCkMVthDbqLs2JyWM916bl4EwqqCx6DPX8A8umOdJCiRZDaxePpj3xPt14SeVk5q-hd2CbczQtPczyqqJXCt-TijygR3v8LbjUDYOlftQYaczmd6anGjhEfeG4Rj5IJk4d4OKOdw8mL3dw2pEuBDjmD8AUOsmPCQuZ1QcrM0oAWJnpUE9y-5CgN37Jq9SXwZa0PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMhM8QGtR7vgF5ICcvGAtTEjVi-xbM9M-GaJF7q-pk2llsxy0yLUZCwkJt2BMfE-x50LcxX5VDiDzaPo8vSPrJmJXCJ5j-A-5f8c96EhoS0G6bfw4F-00iC9-lI8x0Qk91OWH7PEOHsLbJ7xrwnZ4LFx363NxSZvNLkPcsvGRovoF0xgwA8gN0hkZOCkF-WVHk0NBu2Vr5unQhESGNnYteNK7EnzDF-rrRdxZ4hqGcpX3wc9lsCCGcWD_aX22wX2vRbUpdIO62r4-6ivAaIe9R4yTSslLdX84C-5lkZwHUGXR220mn8dffcV1XQJJEqm_YJ7PIPrwJcKL05MWPU92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbGIgK-sa96Cy0QvWPO5bvcIzCW-Am2CcQxaDmuPwC5-66B4v-lEqS25YvthGujVSb6fTf8BBuxT2qQuEes99_OR3GgoJgOHUM4uhgtqIK-3VhAJQu4enHp-7PrwcvRkfdercv4G3eMyhfcIVRDfHeGeIyRzNtLaTfLtp0oBgX5sUtPTFNVm5mJfqPFCsr9ijnB8rWMpQjNQPmnvwvjUdgPillNSPRWOroRhqdcWB19rjoZDRt3NCQmHrIbE3x6WWV2cadBdmUI4CdIEHqgRPXRKaDwRhiscJR25Gxm6vQ0t7EMKzPy8BMHC9On9e_4lN_8NhT_j0C9QWTDJ0P504g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0bIFlzFNmdO6qDohjI6LCOxJrHlUUYGbP6ZCBaZmjOvbdFkMmekX3SDp8B1Nuo55TZ9AUwv2enZpAkYb_qd96k9n7IYoiGei8sussDIa-bL_OcB2viXaaWguGOt10JgTMmtmbpyqXBrcFR-bm3zNwXZhe4CPb6WtLLd8I3Q_qUQhYTLcpir47w2kEJV-okAsSVMffdAJpi6EQHz3IRQunfNpJTcaDdcuIPtNvVyPYO98v_Qe9bFUIIuC6poqXf9xeyaQuW4ACihRtjjDX3Ojm8iIG6mfKUtR-JXmzdRrH5PyQK9ANdCkFFvNSg8nPBK2MlKuzir836XOT5EGIodVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUgCVz5gdSZKiV9zvbB4Mq9CxBBS09MzhMIpo-AifYcFl_vKfLNfKIo9oJAk0Hi6yXoCGFuHywNpSkKoLGDwB07HsRkE8XbLHj_GL1OFYXbeKJh9b5v9wQ9TrzXSah0XKPdRUpmSwjy6P9v-Bly4whZNGnfGcO0_iu-C9pdTkdBRNKkL_p_fdW84giEMnNJL3zgrTwUlECzMiwVyHSo_rWCjjqR7RFbPJw5NsG86D3p31t__4TsJ5ZIU13I__hAXPuwCIRohCOkPPJqLukZ5eoyKMzp2kw_LZODISpNDOWPm7o75XeiZyBH43dj5k_cVQ7ADn7jH2q-IdHmLd7EYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezlU-sxAxHVmWSCFf1GWzZDLTlB-RXBTEl4XtTRLIaQ1mT-BLZgsyqlwig1rIrP95Y8JG-5a0KvsqbrgriXOGmm9bX-lFCsBvJ8AUR9frzCurDUA3VypXDYVfEYdk2Wxbe1VTaNvdOMNPXCcsLAeTiv6WyD38-OZ3TVMYMZcAhAiRjLMwn1E2DF6dnFfNP5WZzAcLhxhTtG5fbQL6QpCX1hfIY9tjAe8C7Eagzcdm75YVUzYdPaRL4hC65iUsVpnJgEc3BgmIBXP8qbIKmUA0Czj8svDkV2TYgTqS_1Utb5aQs-Z1B-SiAkOptud5uOQfucwSwKhhsUIlCjc70HW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpSwxDhUF0x7kKaMjXus8952-vU_TWgZKCw1Olb2uClm1yb96nOw6BtQk1nYnaK4KsoDAGdGC7Uyico2bTxeLPnMj8L5VOuHlPtH-4YNBpwVsvRHvyU0QsHURoi_9Jh4chbrweGuU0XAQsnP6Q3LP6N23HASnt3uE466wZa053DMItNfC-nEH-Qfs_zfAnxXNxlP9TFdrPBD1lCw4rrafubEp6QrzIY0UgUIm5UMBkSNkvEyb6zIkngOs_mH3v8X4iXZx7ryD0-rTpg8skVlLbamOIgwXt2CYIXm0U1Tni5cBENigHfAc1h3n7b7mhFphrBaTe6_VStrnaZcySm3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQMC4hbIGfpC4v-MDmZBRP66QkaeuuXBkcaDE-0AU8AWEOYEMqLGUm0-cvMRrcbdd9OtzyXSh4IcJWyzeBgx9XGASLZsUM7WWQe_wqr40M_O_KFVG6xyrX-91flSWcvFcBGmz8cNnQj5gHsordtNIuGEi_dNJy1GHnlm5dI8pEYK6jiSQhIOhYS_2IlHgGx3cQmd4YbesPj-aFL4g5ftBrHWO-XNsAdwi6rzGzJUMulOIpF20eQPCYE4HEOLr2frBd8BjK0tKZCHTVV6Pwk_W2HF4cyJGE7cktYqeWvRQUniEJ3XICM3AM7K3XCBaeCDe2IvJBAU4IouQmsJeq_Ssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKKCQC7lXmb_jQnx5QPFjKqklk3hm7YImidb0VwM9WlBdh0LZ0yxjuC2YMhEj8Vi6lysbK_lc_FEJmDeGMioxe2Mmky6lr5hLBnhPO1AWdesKHyAbprdCnFM2qwOgej80BYrZYBfugYCTBtJdjUUnr_PmeGqJxN67knz2x-hkx-liBxe6BFHhidMtpZh0nOAyZ0sP4r1dXT7f0mTfPzq1SmedXO6cPEPk2xRa1YNXI-jyyfdu1hKOdeO54u30EzxX2G_syuN5kWP-GBr4kfnJTFB4ID8NV5bB74VMcL5VfFpGRZhPnGvKrYEuvawHvOdzIW23X5tZy_Yfv3uDdRy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=DWka8c0rnHovgwDmSAwebb0zVAc1Tg8_kjIviAFUcluBiIlrB7gQ0I1k68R7PlM_r3qFdD8id852OACPacPgBcsB4TPO60q-u08GG8eY_zKlWIFnc09MxSdYNpcF--77WBCiDHCeOR2p7gtORQ20trQi3brJ-rsMwzcA3ZrOsEomYGNbbTDVa_nHu8R4XUnGEuY8uoKP6vqiNWs5JLj4A9mTTwIvo9dlzEtviAyHup4thbd2K6rIt8Ch3uaRmYr_A1-ihSukfG5DyvliZ2GLDr-8KZiYeW946sJnYW5kusroIvRKbVscQloGBW7SwZTomVcNCH3tNLxPcRLDfoR3ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=DWka8c0rnHovgwDmSAwebb0zVAc1Tg8_kjIviAFUcluBiIlrB7gQ0I1k68R7PlM_r3qFdD8id852OACPacPgBcsB4TPO60q-u08GG8eY_zKlWIFnc09MxSdYNpcF--77WBCiDHCeOR2p7gtORQ20trQi3brJ-rsMwzcA3ZrOsEomYGNbbTDVa_nHu8R4XUnGEuY8uoKP6vqiNWs5JLj4A9mTTwIvo9dlzEtviAyHup4thbd2K6rIt8Ch3uaRmYr_A1-ihSukfG5DyvliZ2GLDr-8KZiYeW946sJnYW5kusroIvRKbVscQloGBW7SwZTomVcNCH3tNLxPcRLDfoR3ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx7friTVeLGeEIFxTTmlBju_O-3SSjPj9Ww7265SpoqUVKIS5PB3hPm0enkoNKPDG8EZyAf301GweoDf58qOA5fWNJFZsOiANCRIFL1lV6pKvXbK-24yagjA0dmEoZ-ZL_1HL52yl_UlhUioEWGeMo_16zhidWRKsneYoEn3LIsZcWth7pF82CYd8WG0ZTnO4tkmr73TuCtcxWp9F2DU1120YXFLJMNGGBFAV7zFX41didLMv6_T1oIihtVUgAtf3JGSmMFkPN5qIwK381xDN7GAA8iHB2LqhISGhPEW55HF5PHPm2sY-xda7y3aLsCO8xQj5rfUzZIMsTxa8FPVyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwMfNZotQTPn8FzTIGXFhjIvufj_N3M0jijr1ZzKfQr2IsWsSCRbzcIjWR1nZYZfhUH09ATPwloC3mIImrQ9oE0r4-vp4WpFIroLJphhldhrkXTzo-Ds0i7sTfmiCQBYMF6mBlziWiDE2T1wsrpFFKk85q9z9_z66g7y_AeBz-_9H5f2HzDCHD2DiyFJZdjK_iVYh1gIe3PBhFBpl9WbYeDQ39jQdu95BIRx90zejNFG1PEKoUKJ8NhcHzTxm3lZi0BYJt0reUYy7U89M5CCr-BYo6kShVHMtGnZVGQaP6nOoOfRN9dIUxsL_ANCw2-SylLidIJJWIurTGnvuxENvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=rsOskrQxXM6Ch1Uzt3jtKfe8TZ85udbt5CYq71ktBwF2dYItQVV-FXIrVNYdT2n03kXvLgRwaKOmnE7YTeHsIr7eOGq8VJvrpcN7WXzpSXn3qmV2WbGIb4PZb9WBkDyX1wlkkhAv2LLcXt3--XbeyrMW7OoHFXxs14eu9jg6QalJyJ8lQ6Fvv7tVkQ1EcFnsIEiGyiT8EqQ8EjrorebB_ySuUL15uWEYpXsWl2u_HJTV8fpaY8Fgjpoum_9QNHIt-uju1e29jL5cOmqpwUYd889NWR448ZGihrH6JdMZuyBiCV9gMsvKXs3M_0YWfYnlMBJGKG98wVqbpcTakio2MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=rsOskrQxXM6Ch1Uzt3jtKfe8TZ85udbt5CYq71ktBwF2dYItQVV-FXIrVNYdT2n03kXvLgRwaKOmnE7YTeHsIr7eOGq8VJvrpcN7WXzpSXn3qmV2WbGIb4PZb9WBkDyX1wlkkhAv2LLcXt3--XbeyrMW7OoHFXxs14eu9jg6QalJyJ8lQ6Fvv7tVkQ1EcFnsIEiGyiT8EqQ8EjrorebB_ySuUL15uWEYpXsWl2u_HJTV8fpaY8Fgjpoum_9QNHIt-uju1e29jL5cOmqpwUYd889NWR448ZGihrH6JdMZuyBiCV9gMsvKXs3M_0YWfYnlMBJGKG98wVqbpcTakio2MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGR-Q0q4eM_H1-iVp9AMQp8jJBn_tXH__sfaEDQnuM865hQw8rv8HNNB8vZRmbVzX9hfpicP6IcrNFUZNuO6gXdOjpnXBqtgKI7IQJlecgzO6FChopQvaJ7qn1_rAtZcjOn0ANRSHwKwLzOCjbLaUva7T2VYbP_IqneLwKQo8S9XVskuxL0VYUS7J2i3bbPUhVJTwmsrZbcFLfBY81jv9FM3ObkHaxSTgS4VCSo7a7ro-Y6_mStziEK-dqXLbT53Ano1QC3x-AqJjMshZWyiJV4WvVdwx7BT7_rbkgN3VEbF13JISvsq7C2sQ1FQpflRMtieo53e5BSxy-TAM3JKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iQe8Ws7_K9-jFpLx7gjXMJQokq0zQ3siFsFyKGh7yb2D9GtfdfyWgF5vnyVWwDtVIKtjtqb354jZ3RVTR_U5it04Ho9wmgsSQc-8Um3pFA_ncymEzZe_2YpJiyYpm2QOTTlylummivvrNEXPiCwCJ2mFj3hWWqZOtDBkU8NzGnHyFdkFzP6lGOZd2NCl0IShSMvdvRhCTuEmMJgvc0X1lhljFZxmfpES9hFsy5XOCgm1vWzQ0YZe3mH83bt1dUY3Ri5cQS3IE-UWhKAuwAkZEQ5wvRS1oW4T_PJoPFNcXgUk9AY2B3DSgnbbB6YOrwm_l-BVvmeYaYQtB7grLPHjsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM0EcejGOkkRW4tpUWfbrpCV6SC4Yy7z6OaIK36Rv6MA18SVl3TSq0m2RwBTnOj5_NF26q2xqrcM68h6DaHXMlsXwudPtqMAvPcOWnkaw0RAf1drIzX__d-aBWGWxTrfjlIuGt_ty159M3AcgOGPMQ63gPh5GmVboUOe9muUHdffgdAM9YCC9cfoYRQbmoD9QE5SuzubK4oScgSsnVzxZ6WNZTdRS8Ii19J4fdxBjAHrHjeTpxWa2IZuafw9Ru6rgOMceI8qABm0b9EpN5uBrvdtTmRJ570s1nI9-4f56TBDfcOGqcwCkH_gEFi8RCrLfmopVSOGRNkbIAanmPByLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY_b4fCzVfXQ7nJtd1MDn00WgIzenDr5C6vVx6Wb3IEemMn4Su20OuAFoLpW2RQM4mt2seQO1zewil4evT_fkPEuH8NAsqSENzyZaGM4Jd4BxLYxEGPHTT87mybKUY8MamAaUd62KQPqF1G6GaO31DVXjbLYxKXvxt3VGjR3jBiA3xY9W7QLD9Zbd681NRZv3S8OxhrCQn8xXncWbO2OCmLpnZpY9CZ3m8pSQPv_WPpKYe8-hUIvna9pNCpAm2RxpdSAd9FOa0ju7YcAmzf1d03NiVoZhoi6dX7eW5j5_8uwyM99_wo0HW8cATdSQm80z2s9B46efbamDaoyY3l6Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qikN4H51VcZC7z3G5zwwJUghzTBQ2Xg2gwTkGqC9DEXawlBLpP9YfeSE_WFnOeDEDy14-sA47VkfEmM4Ak1DCy9vIe8viePE35JpNsDrVIT8clokhecIwNoeglI05hA6Yff5Nhhc9KuIm8K18aAtEYhSl4Q-fL8zucLmKmGerPnCRbj7Yxr6x76dLhnBmv6KZ58R5nP7rkUJoeiVT3iN-O_19DWvxTLVbKdllVEW_XPHeIpAZ7XkeDyfz25FxIJmIZaSsVLaUlm0NKgdDieHLOVphwHFaDeCFcPUHw5KM2uLIEk_4THQfE-L-W9PAhT3_GplVyTwdF6huoKveGslAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vixKyoJ8JLSrFeOJvsiH-WsadVGSVFEgFhqV4rUFvWvty4XT432XnaDcM_pYwoEbr-HE5DVyMmM2sJ1pqA8yK3BoOKaKDi1Ph6x82F3Xet1LEILHwklrpH0v-S48tWGqxOAWEUCnRrC3IA0tRo3rmgohRjM9MBW1jugowqJm5G3PBlCUXPi8wkiLjEHpRZ9SqafGpTdhRqyOlIr-J8D65j9IQXgeA1sRUeG5kkdN7wi5iYGdp9lykGYhc70n-F2epduQJKJk4EbxGMxawQ8BYWoySFY4VvDQpuS23puVnXMGWx-gqtZgyTNzaR3kn37EB8bbfkSYx669zpPsJALZ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFGYO7OmLkKcFXvxr8MjGTx7U2XBk_ahu9DaJGlam7T2wY60AfD3IurNKFXGSyVrzXWwk5InaOTrRILSWSPYnuSN6c9tPh0ehtMK2ABmLUpZVTi7FyAf7HlTRmvSK-L1aT10cS-FNwnFDahZkQH5EeA8_16c0qDIVcT8unJZShS6y7slbHchdNCzOHx4ScDjYZ9oLq1_1ilj0BrVIumbNzl9CDLYtMQfHVJWG_Ox4GyVDcG16GnrKK34HU_PVq25NFGJj1WQjQ1WjFpNUzyYycWATkSzTFYdrulj_bMdB34BPRAiH8PuvHfNJgZYxGnwdr3MQ8_5Tg4K5XCs1SqG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSJAsneVbEReT1QVfAxGwohBOHbLbvbmqKqnqkm0yb7Iqyrm9lhaScyXuGQkPbPWft3xWLbAWYkWD1wYsup9iNQoy1N11UWKiYbhzV1dkt4B1yXZ9SFg6H1a9ev__WUA_rJlr3vSEIQ8SbHXQFb4LVF7ZgHUrThGds0RZYxbGtynaOy5KEZs6jKWwliA14b3q5H99mxOdspBq2aLA9VBQfiIjTYrs-9_y6cKvnH0aLmctw-e1UOo-YmCO3kR6xPgXkYf8-1uwbxzm9aAdk212_h_76Sw4EIU-J86MoxMxL7VDv_Wlo0e6sefB4ItboOJdwsG2KWstuPxS1TTgrdJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1Qa_GiO5iYHOpuEQFD0MGJxlSKLAHie6Qmsedh89T71BOXZIgKorXpYwxmoRG_HQa_KRSpMuCDESBXz3vRl6RrEPr2W62G5JtekI6baefq1cog0_lVRXQH_VZXxfcrCi16xjkacnZw1Fungb075izy3k_YLJWxZBcchwDdmpG6pOVrHX_kQhICTYUoiIhbAm0hEFFd0LM0KKRDeL-inb13soSziiAMbWT06Ze9tn0bUVXvgReHGQzGfX17y6Z1M_V0eiRogRkukZFJY6M9G9I0suPC1p2LtMw_sZajJ-JMsZkSP_4jTDNJfczGLAOlKu5oe1FPYnA76wdhPqFOpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAtlWnWVl6pBHS5RWSO3Pqqswgotc-ew9QzhEt_ELIPQlFJaOBCEdUfxJ53iuzE-NIt3r4lLr9K0sNMC2NlW5w0nvCwuAWVqwLTI9P9faXQwgh3TyT6Ra0VtEjCCPahf0Yjg4ErCfu_NbIYzaazFGBSMRdCdhSm_ZbmtizQ4FV3D0xdZOlMaddctJ5Pw4wGgFuItwMmKVj67YL0S0kDJw5cULjNgfPJvuLTrKbYdaw-v8_bRhlNCAtRI4IyEu4E-BlW9GdgiQMZtFZKk-5hCbY_7h8GkQMF_rkjttLXfGx43Fvogurii3ITXimsBgNzf3oxo5bkjqn2SG5CLsEGoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDiCbosFpyNra5mYfKtSQoVoinyN5AU42YcMkwtKHUsqUANyCvHzrIgkWRFFkZBaq6Dd2LKvtEOTE0YTuIR73DJwvMQgw7rJQ43F9NgQPzLebCWV0SFzEC6N4SLAXFd4u2WDYZ3-SxDCl87Zl64Exef3BdrbLIEwEeDodo9rrnVDJ1qBJXKvl41epSwlaVI1pQKJ6IRura4qbyoOag5Kix_RFxoUcqN27-zNbnszGQwlDM3ko6h5oEw1wXP51-8jeffNP58PpgybVk0kES6jSksp4fij8qAzy6PE_farexHCubm05eJPhfSOoJ5kbjqeQvOlAEg8XJadbZ_jYiMBOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETWP2FVFnKcsuMcgUnCypzphSJeDvrGV5zVd_kTgq37TcAuyC-jCjSUIrvVOaFQcMsOBJxgHCouOENgi1Hx-swcmMSYxMJLjwgWc-J_e8ngEQ2c-biX_1IfYs9UIWp3DneaKWqWV0qgJrvn9xO2RTMsVhe5MvcSrCftiv9b5ZgPLpSLciFeVl7aia_73mIdaA6-VV9juCCdLay07pCqkSNPzfjfjRoJF-No9gK1h4JW5pnmhbo2iYMj2NERE6wT2Z040GnIBAEI8CeoJ4BCktj_tc6lcrR6nrSZrKaf8961u_ZIju5fULlsP0xcs2qjI9oFE02u1jztdtFiGIp4lVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnlw6TPwVTxolFB5RYBxq9UTo7eRztUxAj8LNLrpbMKj6D028vHDuLWutmyKPYcvKH1TI1NySsVg2Lo39vaHoXfQ-GDCFKlJO86Cl_EDqx_75vqIyw_-sfQ40navIs37zWn70P8Zb8lxZy8K2KM_ivVp9PNsC-FXa4vtceqUCZvrdS3v31O5-TA4o9lOPWkdlSkh_KsyO8crpq5QGPxvJB_OMJh1lM6hzP9XIT7H3-6nmGq3Q_6BzRe9QfhIaZj_6fK4S-7wF2WqKtex9_ln3PgJoDexpYwUX0OoViyTwV3rXKR6O5BC0sb2mHtOvdq6lWf4lycf9uJlhP5TT5v-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3gxcTTLCBp3U-lpGDuB44QHQEvQt_7KiDVFIAGlvEwFE__LrNvx78RBk2mc_YRwaxBLTsuiz1AGkWfgmOL64IM6ZrUzHhYphwZyWxinY2fD7vOiQcsm51x5y7sOFjLk4E83Y8wIJNOjnXRlsoDTmOEuo-T3P42J1A2RfthFiqJ1usPybFEaqndS0RTvrR1SfM1nxS41QliABVlqMCLLk9uQoQfCBxeUBCCCE9ZacTRUwTIA_rIU6cTgRnoUVwVVY6g5vDuRQqADDaOS4s3qbTm242iQZDU6qdrq85tHCdZd7yrDGwsJBAHzwHXdwk0oW0BHItyvIammwh3U5mzMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=mttl5il1fOiK4AfvLQaiD7nRgaS25FfwdGKNdzF1--TBUInfLyyMsZAUhfFZwGWTfFtn0DLu8GRfmhtyd2_4eDGGuRP7F45VWXSMj7i_onVn_c4On4cSnYCNsBCEmcW5blPc0gALrTVNl6pTF7suYy_VCQVGxdjBgmDAEN2aZMK0DIUP7y35gYvOyaCONFz8q9t7WuJDDFncGnLfi4_nw2UzCPjsYLfbobRzoYrFGgtuB-NiJ25nO2I_a_vTqv1Wu8mGA8vHHsrrp8AiNshyMEjQZYE4j0wp5NqqToOWoxTNoSb6fyYA2Coqa1n63Z2njkOjAuQkJaQax1S3AX0P4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=mttl5il1fOiK4AfvLQaiD7nRgaS25FfwdGKNdzF1--TBUInfLyyMsZAUhfFZwGWTfFtn0DLu8GRfmhtyd2_4eDGGuRP7F45VWXSMj7i_onVn_c4On4cSnYCNsBCEmcW5blPc0gALrTVNl6pTF7suYy_VCQVGxdjBgmDAEN2aZMK0DIUP7y35gYvOyaCONFz8q9t7WuJDDFncGnLfi4_nw2UzCPjsYLfbobRzoYrFGgtuB-NiJ25nO2I_a_vTqv1Wu8mGA8vHHsrrp8AiNshyMEjQZYE4j0wp5NqqToOWoxTNoSb6fyYA2Coqa1n63Z2njkOjAuQkJaQax1S3AX0P4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNfpEWn2nyHGUH92YlrVctUOKD35AEk5vlTze5zKIvpAckosIy5K8V3wP5wcYYBqAyqgvCtNDUBnAFkFhSrXkdkX7C-vnWfbpPG0piFtCI2IQJlJnC8O8yBSH-yui2uquOacg4ahmXLrg4Bfu5Dd8wpX30GDesaVQKav0PeROTANd_XiAZqaLFlha0KwifwF1NAhya8-eyDiROY6Z4sKgaf0ccJeIcojqi9aS3QwAi8SW25Yb8YLKsrhm907E0GUGrIfBRyDU9Gb4dL0GxzBz8sXUL4Yn9WNyV6pDsUcyRCWvWnwR4U2-hOXj8virxRLkA3Gn3VfhESZfaiX74rhQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEd_ZEmxxhj9wT2V_BJqp6YmH18l1h_QlR5arD_vqrHN342kpTss5iezZ29k6CM91aP9DcHCkhaxw9ZW0s0s_0b9YIr9dcgzR7EFOKS-y_8ue6-u4k2QyQX1MVYfR7XrkOAtG9nwhKv5sxupHCbg8HH30k2uOreZ5Rr1g4E8vC2TvrzyWeqdNRlNYxNzYZMhRiKaSrDXrvY4tOTCT9FMzP1eo5JICBzbk2wJee7aC53X6w7HxH7W3u72C8Sp9uWWMaY8ZuVS9F3cJJGKahpTczjMZPfjrba4Hm6VJ4Ivsjrizf1bWkzdlopF2AD_gDYMIGNbhSHgM_nrfZggf2Vt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BW1ZVOiuHNgTuzXtTmF7Rd2zaiGGEOUqTr_jaMmrZYku14cMc9D6T8bqb_o4Fx1yYv-td7FkSsn7nXSfzwxheF0rOAnIlvZnXFbPMGpAdIi9fZ1SZG3vwwBmjza128UJHZ-5IZvDnSytovxtNoZISLBQMso6-czC7TJtfH3oGjukwxXVEvrdRawgnCc1yfuOke4V2MexWMnTq3TEmP3_92MxFBZPMvY-ggM3aUfneY4EoaM0K986zK2MsYn-FPzEomI12P8OWvjZoMxSedbNv3xmAL7j4l_NEfG8OCGH1Lzh3RyAjf__eiqR_QgBymkEf-YMwfHpdPmltgZvInFbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvuAuAW0l1fB_J1Ou3V19OFzNt64qcBz-f-F3Mt94smcF6eze4clnjaQK5kKDsO1DJcSU1zJ1db56Xd6N4Qc7xbY-FvOFcFeeomDcrKTx3n7CEaXHQawrbwAQUa6CTiRyDDlKXeoBluOQP-RZ4OfwJKyCmbCVoZ-f1gJbY73U9nYXFEPbxM4PXxVt4u52AVs1wlKNfV6WQ650d7uqBGYR3iO07TPYr9rZjF7RcXf9ahR_hsVUigY6wQf_2XY9gob9K2WClU3p1lNC-fUbF0D9m9T4ulYOJQgJ9h4aNlaPUBg4MEOrePRRSCzz0huQ1k15PFAWubf1ID3xHV8w460Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciOuYNbdxzcAohMMb0lSA-9mR5idcDyCJxAqNkIevAa3ALT715cVTHmTetSCyqq6mGPcwOo4MfQldIPxl-fpPfWmqce_tQFzlbBI5LbRVzYpLINXT8m8cOkck0HkEs4c4YsFvJSMRsR5fr_5P9zaC0Dh8aGpjNmD-NY_7icfCZQhUYTyOzzr5JFv9bhdN6rAjfqRCR2NGhEE8f5RjOOqxyA8wUOGA3APw7OT1fVcvpem1BSfY0Hd6u4c5BzKzaOEKb3RAB7SYgfpLQ10LaCe67Nai-xrFq5i3aFfsf81YfNpsa2fISWSvsP9-1aNyNOU84NCiM0n4bInMMqXpVKHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnZSRFDLChsxXbyf4doslAmeo09J64qIXPy3dV0ImcOHPuve5RfYfkYJe1qo7lJy4TDPu4d29qZfBGW9XFMeGjmXWegmEUDuTwFHXPzu2kPAVXS7gOjz-SRUdLz_kJ-PRKDMWwOJeJsjEio0mawiAYR1F0OYOQWUH2ezmsN7P8tlkbe9yzS8VSGTpULsy0n94GpAIKiykylX_gc9x98boTAsZ4tiXJ2vh1rZXDoJqQs29leux1jadslpYza_8no0H1M0JvYYxkGLk7Z4kqfr7fMedmY_mxnY6EgTznnWF2GyFXdex3JcQcvbITQhM2QMAe1_FA8iJumfdAqyUBH-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFqKOfXvoDCpXD8Urg_yQu-66uWCGqpW32YdC8_MrKTuutIzjegeHYQX8KAuJgPfnhpsYhH9jbVPWc4x6SLer0RcfGWkAciLai_IhlYfjZnN2YY_KMw5V4BqPmVyF8PUFPRHZHxn4zGxz5EdXlYBDRm59W301T_zW8-qOnHpQB7N94RT19zEBsO-CazfRT0SH_Jfb2NxgDu_H0bR7RQfegJQ0XoldmyNPprRzUxixuE3jUu1WTxzc2d4Vv6b01sLnh9g0zulDNb6Ql6ldp57b3zMXfPJFNAZIVGuv-hlRFwbJrpNJyjpCt_8S6wIB49A_emQ6Vp1IUfiITjVpBdUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYN7L_75mPJzd3Hp5MQOTWywxdpUfVJSnw6UXvCqE_uFih9u0hzjj61JPFutAazLMnhdl0Nw39bCXy5L5aHwQS81xPbMQ4KWvcOPwywIDM_zM6cGNVi8t1hFKZ_1gJ3tK_m5sXiABn8Rc_10UATUWn-w07e18m35x9v4qzl11Hf2CVFF779Ys80806TSErL4RT0JtHVInuYcvyV18tCYgeSFVB10iqraFrlGNHAlOeobtXXhqsrkXQARPsLDG_v7obL6ptFnkSqSuTA__2g7_7H4tdm4tRfJQ16x6EgQANNQk0aRC65W7kxKqBIriZmHdEzsWAKKmnFImkpy-yeV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suzJVc0hIHim0ozS40uPRAJbEIeW1iQ37SN6FxbI9mKuiXi-H5F2R2PbtKzCretKvxbPMzfKzoJe_-LbTK7ByYHn93bMO2dhraE_eGQMXMY8JYiqBiMr2csPTdIaU9qqBERMAq2pI-QtpAUCgS6BiTMXnBGME32OcMOkr80lRrO7WPyMR9gLxEtgZ5WAl52wtTk7TzpFJGKQhDl0dGBxHsh_RrLSJmo5W8qgKmSTfHl8DwNuNZbShoCQBBXviog-MuTmmDBzNBTW3Li_NfLdUx2XTByfz-zWvwt6EiFHzMMqu0N9SCQcmX1W4w0iYMDWVMxzMuPDko9_THfZ-txAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt0G66kBJnnxVaWgLwwjpZFbm_HC-Z3F2m7GeRrAFS76Md9oAx4hhQ1yqRLUEV56-8xBBFCj1gn-YEq98d0ISeRcU2iKZljW8s1kpLWy9pgSAg8YlUk6SXWRTJG3FuqqfhvfAKd8_gf-D4ELejOMu6JRuVb_ELwJktsSxsSjvt6oEFcm9fT2wT-86f7xmUgTSDYiSeK32aDGU-UUk-mthPCvYagpVFdyHQ8_Cx-CmTqTWI7NLfkqx_nz4x_Gyg_Lz_vIB54Hjq4bfCkFFDYTXOPFwOtnAbg22TC_5PVo7L7pqICSS64omyl_Q6WHSt6x1tinFA9RULoL88KzJpblLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLTIjZBMv5Lv3SgtDOdIIghbB6M_qU6_lA46Cxk6X9xm3qEwSkSSYw0DnDL5q4J_mqZsYu1l61pIslOqWea-4-xkA4Eqak3b_l66lscYBYzZQrjvxhZPub7E6MrlMZMJDSbG-0qYh29rGf-Z72mwyWtyUxvdaz6xslaCHypzz6gZgG6XsSGJhogc7L4fW7C4zn23iBkdIgeQEyrqJQt6JNmw4TFqE3m3EMKB-gVRkqRB4BI52uSnZgzK5NB31n1K8jx2nK7hYrSZoa2hX4t2mwPhhHVU0apwKbHW-wy6Cfqq3z2p1QuHnT8_87T8ch-eMQd1hzq1-lHUKas3WB2IEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSg4O1g03vGJmqiVFBcIhdrxhFfVJEXwxL5PBgr_2lpM8XAf_jySSA0EH5lu7tfGdI1yg5uHYM4O7Y_7JAZOm7K2GZAVvSF_TFvSXKaaQXCB27GdOVZ1wTSvSpuJOZTqep9doEThon2lpUFpu4fNALR4dogEM2iCRMzT-0EnUZgTMq94_-U6GbURXt3Z9j1gW7je3bdL0aEa2i6q5wcDcMMVlmHCEpP0QQojKLphPUPkUThWi__k-EXLB6vv5uE_2KUEmDczMXv0zNBYq_1pBbDKEx8NfTTXZdI_IpFzyjSuh42fenm7HsAoWhyYw52JqeZdBW7Nmkk6GgBywHIBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWxg3LkVWZ_z4womRxVjWfjFVPBLXfEqj3vy-wxFe6UblMy0B-bTNIFrN_9Jbz9eIR0erjjPyO8Q-yspJ5Nk81V_vP29zYAGQPyY4l4alyT5kDMRuqf-fYSyD4bLFjylAOP4AjClorbx-pbSwZfjpd91gvPbcui6Ey5hfjuGeIMKU23cWTNv6NLL8h5EyJKJUc0Icya0M344nWjEqHvseaXmEvGcZRsEeMY-8oV7M-svDL0z4_Fu-sBLbawxZHadvRQIFqRtetbAYQ3RX7utXSaTuT_nlxX1X5bulk5W-3gL1C6txzfwSTvTsbycY0Qh19s4pGYSqbt5LNG8eIwOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppB5saFmY-QVTbOeuwCn0DiB24yth3alsfOanjGI9K7PF2V5DkHRAQsdexWdxe9fInD9Cbzdd2osFvIFck9W8EXmJz5Vwl0arrxmMHQgzjk3gV5bcP8fmM-HqVEQ70JO2PHwTt9x9CDK8t6BC4yqjXJWpiXWh9x8EC7Olexcar8UBOqTQ7Ii9EdsVA2B6dVjROEvRr1C6xz_uK3PhBb0TafH875VcupOhuGF79bloTLR9PPPyJkE6eV7oUAVSa00AWGClwqz5twRF1PRMxxYD9a3uPD4XcMw-0e8CtgLs5HFtqx9mf5p3W1f5HFRAhqj5UA73ICa_BhhEPrGqdrQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6zfQfeEbVNB78B8D4Am2R-CISTXpRbMVGWeloHOlhVw0fIqbnAZQ326x0TjDwan8lRf47hokZUQEVWfKNO7mBd-yjC6f5VagWODOgwkNu1f5r7hrED97_IZp5h5MPnVgY8X1M3sdloxC1rBKTkCcGBR7wd8MtdaTNdttwGh1wVDu3iZBC5n8Oh3qBIaVZReFkU2DbuoNp2I46tkxOQKNcPCXw7325qlBq6olfiyNkWBEgNckaZbyQD1UqUhsvOg94j8ZAYzVy-YsOjuohLsz2tRaOigpo9WmLwLAjYaphr2kJENeWASu8dY6oWH0YMAg1zZIdZFL2WjlDp_C5Zw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utqL-7TIC4kcz_eH0rggYBGnfkuA5ZQweKY6wK-3zbMVd2Rt43UuPtv6nSUaw_uUU5iYduFtuFIcBhCfVVnkFHU9XkjZXNHui1oHawEeqJ6YDCkRCyoXmaoDBK7L1LcUsuSkQ3DYDaaFuCEFr9xdbs6Zibh53GZY5eUSUaeFfOQlCDOqwOuojpYW0Ku8b-itMDgDb06di2KzMkIKh1rwShrKWt8favW7mB4Pzm95BJ-EGh81L89bZALnbxydSZ6r4dkVGFraiyG8oVeiUNa6OSgCJIWokl8TPYn_RoFKt_cGUW6QwZ002C_QBdVSP7IHYqY5dw_5X24DovoFmDu0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5MbfJbReAkHLm0mJgvl4jnRSKbddta_xMJ13wguoplIJLk8VUWiiaxNDfJKLpSjETFD0E_PWmu1X_bp6f1uX_NQgyBQNuegweqA4aY4DnQk1CV1Ev39xSdvoyxuS37KtjO5PlWXWIll2xtWdpRR3Po5p0ghSxWrS480-LF-0-FEVL8laX4OkFjwQhcTMHvydHkE9-RGtC-h4ixJ3yEPtRi2EXe22SnQg48h2ufM-EilQuk6iDqV9AGdfz5PgPPefP9Wig2jtVdscYxDm4Out5UrmA6O-yMhXD99vebWghYvauXs4TvS1u0bxF6iem2qvYY-eb1xXTjHsn0rI37ugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKsoymqsElNUO5oyROumjz6vATkh5WWF_6m-DAXpUnKmypu-hZWwDRowVdlbjz5VmnwaI7jJ7tcm5mlX0T51ZR4_O4tyQGbsFaHv36Rcwh9b9ljiamAdPpmJOx4ugZtW9zb5VjVny2OirCOHPZlZtO6t7nYMlPhPHgw5liUDe2NdaZNiwIuBEt1eFwa9B5sT8VeH9L0VOg9W-nmuWK948Da3ClzmfFJFDTJsevjDmObfwcXIW6xSiEuRf5T7uE8ph56Dgu1f9AIEMDLSGelnwgzqyI_IjnirVwkgXjW7x9dwz_ffjXMBwM84P1yDD_XmQ_micox4s2Hymha8OGyz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcZlUJVXPYEyXPZwKsm2ijQj3tFmmb5HhfJr7dxW0Hvf_jnuwrEAaiVzvuQw0oQD6W-8p8aoHBzYktrbbqfgpm6DN168JuaYJpc6xA1KXOOaRMCXEdF_XTW4GNYSZuat3ATXFz3CBVo8yjt4tjwRtDeu9jtrOBxytDUTOGZ2X9gLTBwiyZHcOsHadtaQJUod6YSN3Bvlx1i0492Zc6LtWe9HaGbC1CzkqzYGK1R7LxsXzZezT1J2X_SAyLbpVuzX21TplDHGDrb0wHL4U2giW366U13w25-AwVqVE5SRtgY1io8hsHYJJXsKD8Yvl4K7g4o6OPH2l8AMzxzPVO0M9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUIbDMzXX-1Azl9CLvMdY__E3DORwdX4ZKJtWPtp-JUaBwK3WxK2TtjofyNxIyXc72yP7IlPgnF1vVAFGMP5nOpRpXlaQKSigUCLxFqUfXPEfXaw01Vmm3WsTdwE11cQMjZuF7rem33QITlsuajY0EzUDxefQwmcnqW5RHAzPdbG2eySMepwA2OhvT6yEylLXXRLvMVV5CnlfImJAaMhQu-Rfu8I18KzejpDum6Pswyv5q4EPOEmcmay5sNi8VRzaSlBkKCWSyo5ghUNzh3LYd-BYN_XmMQJ6wPKRk7qVV3mHFnH9gwwdMqM8vvwvjxzyahSZcE9DK4hz63FRxAcuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWtseX5sar8iuTinpxoCoYOWFAgIul1ah_vi6nONvVgOAAxAI8xF4N_rVth_WfE2a631ShbRD-sqvZvzWrAXCSPpBCsUPtR0n0K0TOFv6cW2mHnb-kRQfpo_OkKhJ_G0VQT3aoUQJ4ZiExUKKIx89RsPO_PVlKeXfbjSopKApHwQu-F4bggFt0cfni_eWPlMJv4ZFdM0mGbi4Vw2Vppj1wSVfMulj6nEB_s-Kd2KbKWQZ3XVT4TtIMWcDJZWiRvsctJmNIy1P0g26rLMI9IrN6kigOE0flJ-69vjpr78-0qbEKUc8E3df2BkQhseuxXkU-4ALq1izR1aFc2lIOoodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3eljq8_tA_CiGdeQoq-tLkiGbRaGlFsEo4p10_KXP12_GN_cqNIouQ2qJ6vNJPGmYZehGecqAnyDVJ5VZuhUrc6R7Qg3bA1rTlh4rxr1BnAsoiW4zDknVOmX_8MPgYnNLf-FTjin9bpM3RLn_yyP0-GBv1xV_MEBY0MdlOcRT6DsBeueXCukBZi6JLp1EQxIHCULl4bdnJ1uUYuxSbySKc9d9iJN48IdbSGgDJuvQv-84bzYtRI33JS_N6f8bMZFNq6EPJk89nsS81sP_LHCOcqGpFCEz7DMiSVWODGLqT6ZxaLQOFZP41aEIiwueWWjEb8LdTw369GdW79Uztkow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwXU_841qrH2CzVI4tvGDY5mel7DOxTAKmBs9PI-tQLl6DjAa7nsx6q6u8ZaPDnz1skVY6ypyc0AYCjnPA_94CU5cS24Ub3hpm_-X__QH-XcvJl_devSUhhLxIE1MHMqL4VP3hanxq8Vw-SJP8S0mZdkxe224bSddtSUheh5JbcZsQw02LTRLJ8CilWSrDx_HxgK0BnF67Z1Cnc07T3pc8Kb3FzL9iRFso_j2P_vU9l9l61fznxDF-tPOHDP_fYRVAzKzsDl8SHI5N0h2ASxjzUEv3dSABgP0Q4AMazxpDlsr2DETw-4TeZcb7KnjvAceuBLWmWpHTBVulmkCvRcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=c_mOtcLspl5eC2T-Qy_y-Wrlo8aqdjO18ymebmhfM2PRcXYQj4Q8VSWxzNO-ZUGiZ1OLds5qI8Om-lVBuWMgcqBYNhIxUYSifquVEg85lhbTpXnzt8HOT3oB4FkhnNA_rMuMH215c6xYU1gjpajkd1InWWmtuCa_pblEe-mdky7YmpIi6EVWTPZ_rlFRswQWmFdRes_5nMgQW8D8znC_5I3rpcoa1VpjUK_FkawMO9qD0ogHEuqG2_poJ1pfa_gMWfBQIgi8ofCZzKhMkVSX3A9_j8EuOQ7TnWn2--bnhliWNqQ6qbVzE6RpRxNZDV6-UbsY2EratyFc5UsuA3JYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=c_mOtcLspl5eC2T-Qy_y-Wrlo8aqdjO18ymebmhfM2PRcXYQj4Q8VSWxzNO-ZUGiZ1OLds5qI8Om-lVBuWMgcqBYNhIxUYSifquVEg85lhbTpXnzt8HOT3oB4FkhnNA_rMuMH215c6xYU1gjpajkd1InWWmtuCa_pblEe-mdky7YmpIi6EVWTPZ_rlFRswQWmFdRes_5nMgQW8D8znC_5I3rpcoa1VpjUK_FkawMO9qD0ogHEuqG2_poJ1pfa_gMWfBQIgi8ofCZzKhMkVSX3A9_j8EuOQ7TnWn2--bnhliWNqQ6qbVzE6RpRxNZDV6-UbsY2EratyFc5UsuA3JYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUXURMKiml3UmCwxxuUHxa266ij3tox0kWIT1rrRt2qn4aQ8mklJiFyW_Sb0JVTbQ13P2-UDK1dEmyvF0cWFRFhoC1kI_1Sca3KzDpmSuM35YHTAAeJLhOlpJUmDHd6SlABF5Q-wKZXenbfz4152pj1AeOi5ShnmIHZwQhf4_wlQOF0Q4ORVDijTFYwSdtK_NzRaOoM0vty6arHvDQ5jL4VKBjH0oAq4GDbL9-aG9q165xO7VozYECjE9JpFPMJk2dpEtWTT3giroi-br4xhC-n17OKIuE97RI7t0TayAEswZBkFMGlfd4Aj0y65Cgx2qeEOQsbFJe1ac5z8QfSMJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFbuOr_M0Cu4LcX7UGx1lHRGx3dKYkh0UaN39yV0KnV62gkfAWbQm4LfTACpptox1-MTKv5QPLI9xxdvxdgK5no-Jq4hHL-uv9LMCMROxgtiSLX8EhqfV3-mKbMFCYJCxLKGqg7Jc0NOkY02raEEb-ujb_x7cJwTCXudpx4kKYRV8EnPNbVcSKm_bN-lYa6WB38QuGnB5d4bZLYS9UHwsr-8OFSHfW59OiXLau-NrTAychogwzuy98YhFWHXx-esD1Z2dBmdmgntrqjPgu3Mg0sFZpBCQ-PWpwTyuefcLDQsl0hBUYHY-dMfaLbEMA6WuoNh1h_ukvoJUw_T2m_4sa3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFbuOr_M0Cu4LcX7UGx1lHRGx3dKYkh0UaN39yV0KnV62gkfAWbQm4LfTACpptox1-MTKv5QPLI9xxdvxdgK5no-Jq4hHL-uv9LMCMROxgtiSLX8EhqfV3-mKbMFCYJCxLKGqg7Jc0NOkY02raEEb-ujb_x7cJwTCXudpx4kKYRV8EnPNbVcSKm_bN-lYa6WB38QuGnB5d4bZLYS9UHwsr-8OFSHfW59OiXLau-NrTAychogwzuy98YhFWHXx-esD1Z2dBmdmgntrqjPgu3Mg0sFZpBCQ-PWpwTyuefcLDQsl0hBUYHY-dMfaLbEMA6WuoNh1h_ukvoJUw_T2m_4sa3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNkfHaz7LP43Yw7CB3MmsFqb9QTSuQWwY-DzZ-8dpZWHu8QWipZcc9vjQo5rXKVCeowFrD3KejXxoeSBQM728qIxxvZpr6PLoq6VO0jDpvwNjws_q4JYxHcti7maM7LpRngChj5BHsG-sOU87txmOX-9h6MY6HZ7RiK6h5E0URzavpxDU33nJUswwpcblG0wnlwtCgXWHhG5kUHsLgaz4ZR-jSw752crCJXElVgJ-4G9AIau_jY_38eqkPQZDVI06CLgEbdxoPHGZQA9WXFqdyNHJ1LRLEEDyeOum4MA7BghCVwQZ0OgJUF09A2UElxevHVFhFku_gYm-1uiAesdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvIDLaoHfWlMaInAEzJ8QEBCJzs_j6bxoNsSw4PTlQj486JUFNg8Nac3vBGM6Hy75DH11sOmQyWKcDVoY8DCuBzC72yBynWSYEVnABlrL1R-4LrGX0NXioVfia3VS09byIsxLXdUaE-Qawb6oLI7BusUq180c94k5d9hIjFHKwHoonzrO5QIt1bTiFI90ysnsUQlCjNkbkrhGbSjpD2nSSqkCAZmVyVXoqmoKgRmc-JLuL9Ry-2D85Qtefx_cISnUhL-eS6JSoxNgNWZeO-j6aPjJNEcptOGxSG6ix7e1u6rq-ZnlKbHS3RgN3lcb_nbDXNZHHXsG16ZawkzIIn5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjRWkxcsK0lY6jDp7k_MDJVoDZLDZf5_Aq-12K6kLjxg4Edb5cV178zglhqMmuard6-vsSwoBHwAAQaB19LWwD6IJOYf7ZcAiGjCRjYLeQBE3Rd8lRqbXt7L1R4VsnTNGyLF156N0WpmaDPSlnOC3Z8z2z9XFxI95lNoJcwUCOF1jf7ozs-ON8L8dZNmPBKW8crp4t2Pd53TE_dRvoSsycA9GA-h5pO78hC1fwwNYLaN653AUdqYrquHie4WeOJbgH9u9f7ijAugL9hdt0N6_yiG5i20ccuaB5y0Q3-kKRzfG3nbXmcCt09C7lDCisjmr4io4-k8KSZ93iFM9OBAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvPoL0hunsm2vJCNcYlM1Wy0kBrmD-MLjkyuhLvURcvu4nhAo3L-KZAqQnY_xf0owUuQFnOkGCl-Ja8O3KKg3Ad6iN6RkxagKNvOvXE_SCSZr1K7eI0cfGrYQQ8pEBsfklhcc28p1IZSkv4h7JwMrIZwJ31I6vPafSwQvFlz17GAQdRZEbGcgW0bUxamiy08Ncq-IstnD9yIUGbaJ1DO_tITPQzHl-eyYSLlNVb1SSvpP6GXwgvLL1yKZwK8rsnbDHvf7MZ50-xZMUY72h1I3TTHNO8n0ZTeG2sjg9lRar0oCVBVqeV-L4GDG6CVUG9tZrEP17Tns1iL4xWupuD_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQNyj2fWKweXcU25Vk-RwWEZmlOQg7PP7h45pno32lRJn6WbmIXpe6B3l9O0gwCFOmjeRaJ4nU_Y7qmWghitBX6-ogjAFYxhPvnyEBG7dfKVO_yB6DCTAlTn9xPmMGHWLHQ5cyL5cgRSWJwqWrtu592CHd5ILTxThNNlthx5tJc6SE1DJdsmAaWcCE6PT7UbLHHnm89Vzn9E-IoKlEV4_aEJcqZXTmGr4vUBSubo4RfQ9j-O4kz9JbhR22tDQrCHmG5xWyP7YuxKh6kUn1GrdwRhzDg_GO5uJh3EvBjPkqks76H4l_CVOlNqYpULUL9nTwkdIgKLpOLIhbkfZYJcfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr6w0Krq9ek6_K_Hza5WklrMcP5jpBAlzJhg8qrFnfNUVGFiACsKbesW3iLCF1bqZde6rU3-2g4OVOTOPCHJcn4KNyV765bwvcLwpB0-jq87h9rEtps9cv5QJqj1B-PxoluOeknvR9fG4QWoqjrtL9Mp3ycZlM4qPN7sxnBjYC5xHYnrzqTS5BeLZBBzm6GiJbBs2EfH_HpNUP3epwajOyqtsz4C8wasGo5TYx6DPv90BvO7t8W62LZn4VTnK4SYr7E41p2bHSYFQMD1Yui1Eue4o6H1RJwOIFiD2hSaz8MqK57FLVVjVq1oVrCp-BgvcsSpYn-3dOWaBvokrvwG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHZYlmojCqyOXfcqXm3SIDibdRjWy4siVAOivmTbq_6WLHcoE8fUsxgyFU7UZTh2_PYkMmuahJoa3TJqIEUe5V4kY5rIyq388BUntlZwG9xAUo2wDCnLRhZwiOL-8UIbyLNXIlKpxm0vIv6Ltxf7LuZZlHq84crFxLIayuAU_FLc-telMGqCmpS6X3kDd6NS2twbTJ3ptlyrySL4850uQ0-hPDRIORB8JWvvcka_WjiyRHHYlWHNoSGvGnI0hnJITWwj3ulGowOSvZyk6VlXXK02yage7ZaXaLsTz1azfuxVuOWPwazOPCVCpmJIz4VIiPWx_eEYaxm-o3Ki4ku_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orsQiPQ3IIsCcOTYgtAXG0Yqj3d2yg9Fz7GxBh-yEWNRwbnXpRJt7C6v4h3sre824oYXCY0uN2l_XG0QDwIQqcCmhQtBmMBeuEvY9WJDmHSTi2CD6Z7TfFg7XHen8L5seD0QthovTlylbYc1I9zGbQ8l95yBI32bGczw1EWBTneM6yqMLuiHvwVkE25MCIEfYsGtZ8wZqgGFOFdSiXjGnuxM4HjRWlbG0VMiqrgif-h-a_XhwQSWH7Nxzs9NQFRG_ghRVPJCqOaREkJn1PuW0p-9g4T97ZCCVJGHcZ35_17M5YkRxclaoyzehijCoOktC4UVVhm95eIuA4lPpFa9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJI9YN-l89hfsieu1qCtYt1Rw0SBP9Wyl53hLl6RYhLRBPGY46Xow58_-JrFdYaiLQvWwNLvQtaNzTHIADAYl36nWbOjxv8jT-4M2m7D9nXmRPccGCUcU5OIhy_oQv5W9WsPUqP-NdNkxSgncav0ak9FOAoUh7Z0krhK72YpuzUd8v3piXQPYlkF4QF2fFNvFXCappAaLolCP5kxAsQJYKAXHn42ip2uQGEQII5N_w2jBjYX5TCZKwb3wY5cvxCMx2DijWGvZ0adC1TVfd0K51v4uLF-t84fIwPcy6nV0sC3mcr_t5JCRswtWAwzpWIMONNvGELIvknLysoVFjMmsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVcVa3NB4BDG5-lL_zwmkr5VbEUa7NsdQZPeQnhculjaTGUb4tutTjlETMqSP4BYg7AHCNyWcq_e7KugEk-BjSig9oszYcg2dsPIiOi8VfAhZA-EbzQYYzs91qusVX0D3nGiDaFpPGbbHfFN9UTwrIFHM9rU9R5msVS5Q_E74OaEkpw5_nsMRJynf3AQZtG3XxpM-u3PK2ZXMKeXVN17NiLd3ng5ZB18HBrvd6NbS_P6m2N2g0Khwrv2hNJXqHSRfR-7Q0xPk19YVwh3fjyNvpbmdXrGI4Hh6ewTE-m0Afi1rtE25MCoAMSIKc42Qe8C72T2YOMpKE7_wWwskqIt-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fURQp7gN2Z5vy_dIVLLA9CnepdyQCvUAhZzbSoUAgo6YYzKgi7o8zBX921hxUDP9JCyal-cGs4j_G_FTJ6OZfnIlWgnadNa7dMd9rFIMGeTJwR7kR99Rw46diWrUCOJ5_4x1NcBZlgvPY6cuAbSp24eLynXNy_2SzTFz5sm6sq1wmHPf6OUcIandhjNfj9bQfCNB6ZpBORNNSfv9oBMFABSQgTtVie60-x6LiUJkNASD3XP84b7COgj4ghAWpTfwKY9iq-EOVKiD6pED9Vw-ZOaldaP2nbYreRUWn0WzHVBcY3QhZOfaEkd8oZJ1kPT-2B0qR5fmkl6mJ4OMwni8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=ZfMz9U7hQPcpLViaC2G4-rIy7diZYYKjynen-P26J3VVWkXGaLQpCBT3ozuZMIiuIH4ka0UsKofhH4q0MVH-HhgsiL_Y0d2sPJGVM41z3TNZ6EAiJyGMcB6UUIrnb-yrStGJKCAT9edVYdD4TqG1BKyi8BCw-4B1ZZUaVi-zsdbUKZ-5W0yXaaOuhjpmVVE4UGKSVKmxkG23ZNicvJX3hOtUvKqLwezFJnDWxpWTl_Q9eKc8pb3AWLAEW2f0QC3n3nRYwgFWjlsRWjFj_H_uAjr5ubVkc00iPxgBBEOtuPAkLmVyPYtpymFB0lesxcMSlGX7j-6Sbvbdf7zG3H3PfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=ZfMz9U7hQPcpLViaC2G4-rIy7diZYYKjynen-P26J3VVWkXGaLQpCBT3ozuZMIiuIH4ka0UsKofhH4q0MVH-HhgsiL_Y0d2sPJGVM41z3TNZ6EAiJyGMcB6UUIrnb-yrStGJKCAT9edVYdD4TqG1BKyi8BCw-4B1ZZUaVi-zsdbUKZ-5W0yXaaOuhjpmVVE4UGKSVKmxkG23ZNicvJX3hOtUvKqLwezFJnDWxpWTl_Q9eKc8pb3AWLAEW2f0QC3n3nRYwgFWjlsRWjFj_H_uAjr5ubVkc00iPxgBBEOtuPAkLmVyPYtpymFB0lesxcMSlGX7j-6Sbvbdf7zG3H3PfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic9H9QxCmIH4uDVYep_mc9TDWhf7hLagOMl-ZBsivqs4CAxopCwOK_cLeVRCIsCFGbsJE7dOGlbuJCy70rqRU56vPfht5Ue58kALRa6Woq2UMrZjxFI4hJw4Rwf5gLGTY3b3B0iE7aUck39vQQeqsDuXFkpievGA1V5Ij6lvL9YlffSMTJs7_aSjPNruX0UCrmo3_6TL3MSNkJ2yhOtRXS2xabzYqDHQ3ZkwXcJR-E08nAovYmBvdRyYg1-Deu7WCNvdE0FFWnmbv5KARpyqKelbyM1jei9tfvFql0OgyHM6yQXiCOgPsNXdOoI7xnlER92oO8WT_hvQEdyap319Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
