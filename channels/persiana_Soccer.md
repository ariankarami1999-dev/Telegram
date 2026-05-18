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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 09:11:25</div>
<hr>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5cRdVuBCUAeEipfdJHH8X5_prW65t1BaeYNsNs4XrERQMY34DD8Z0ehbC5Dn91O5WNqn4edlrF8w0dVmnT6aCmgAR0i7wgKKAa2KuwzghH4JakY7fUVv-i_BQ-D5IsueZ95W9U3nb7vhCn22Fvky8yGT16VrlloSVpPm_-IM4nW6-NN4jhWihaLmiHMKQdY_bYt_lf9ddx3r3DSfWWEbpEA-iXJiH7LZoPaa8ZDTNg5HGZKKNaxRQMe0Agx66DvMfxi2xAbXBMySuoTY8r4OZUiJksLwrymaVGTTpRbj-gtsS7xQyFRrSy8J2s25FdLUE9S_C-F4QRtSvAl7sz2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y900wnun-3-tv5y-Zb2J3PSH5fXG3N-7ItCe0uYTi6fW6wsGJIjrI0dBw411Kortg8qyx9LgDjvOari-FOjrj9kpITafdCWBEGaK9tdFFqMp6YJWfux8Fop_4UNbuhGNN2KBYYFPV83inS6fxqMfrlUOI13Xf41lk3kB5tgfVrsmUkLaG976Murf7Sfu0Gygxv4_UcAM9eJAJgCDgulj3rWO6SCghVt_m8CAHDycYuvgKuqYBGckObd8yIAd2BbEHCQ16dW4fgtdEMtFAHPgmxcGmZsb-c-cZfbfxUHiPPbAtLndg6abJwKT86JoAffba0YiRoqZ2H5eg-jPCivnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22166">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/persiana_Soccer/22166" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIfP9rLJD2YNNE2EG7FPmCNLz_5PCrsSGpodtjB5XXiWLX9S_YeFeWeYrvAucG0oUqYLqD1PHN_2RfEd6_NoV3g_x_WNo7taWRIUi5pEDBv4SCZoBxsHLbar7vmC2EyHkmuAGlq9Y8kScToy9MIQaUjX6UpfQQ5FK_gucdDfKlREi_xvCKMORaBKBQvkZp_K5TAzHuAhQSwckuRTNhjPulcS_0Mjc8LhbFU4ofP_jSijIwANozkTOdptVY2Q-VGCbhLde8Y5q1qf--k49LshvaewE-xjramqqeEAWAFBSFd-yAS6dQXQe55BWtfcVk_181LxmOZb7Do1pJrqVAl-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGLC6fEF3a0pEh31JEifn8mHJighW88fTRVX4nhGiJBuRMGkv3JJMqfaro6wfGvI-8m4xzK0JnZy6_b9CqqQB6jlCYhaNwONTXt5Z4uPIat55ItMWlPn1F2o1nnRLFlMmSKiwsV5j-qdUjJHMkxt77P7rejDNQvAW4mYalE1knBkX9-yIM8UUuZWoai0nNaOUnEIOyiJ2syY7Qaq3Lsb3KBpSyULt8Jh8SqEhtl93q_INulWSqVPy5LK3pjUhmEnrL2u3K-8-KdHu7lWB9FwikoJBHK2tT505WwyzOYUjNQuYA8vFeZF1Lb1Za80ZdP7FziV7BVMt1uJEGzyyPwuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIJKVMoVGDwXhrk8Wy-OWnvfOkqBYkspHjQDLdwTEZxwtZA2SieqQBPTZ7r9zLYwefzhbltVxarUUSxb332fkpLHLK_-oP--PQClnKexJcp1GlmqkfNxhrLt1WW_cLM_yrh7tYBPeEbgWShmXeZj2vQK5lshfNNkACTgedojiBczkDZ5TBmf0iYwKmr71ygIs2IYKcVsRl5_KrUFip4m6KbxpCd99CwSGibpChW7Fk5O9D5A5m3NCT4mQV3MXgF85codV27uIX5UEzoC4UZNB3KRCI7P188NItmDE02ljGRdY20_HsPGu67X5FZw1jfz_wnL4E_OixJigv5d2la0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCfbJCDahA9sjTq5M4frCjkqHVr0xPnt_6XyaAvcOooYLjRFVJb2sr5NAOGPZWieDr7W85amSHBms7nTyhkhmOGGIqADd09aNmYVSCqXlgUtlEHNtOX7xP3mH3_p6VKEpYrLsBuUsyxhX2QKh5UCH2Sc1zhAMCukjEDMWG7V5sR_NxENM5PnFmliNu-qhTxuXlNP2-bhigeUhcL9kQ9rtJsbNV2MDrV3A7Bhc7iy80i3NpgAvfXZCU-EO9Z2jtGkh818IahXF6YALTG7IHtztwNyRXZaTzxCnTUbkEWQux54ZfPO6f33thJfKAPTIib93ddmoIpGR4O_bybGIAU1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22161">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/persiana_Soccer/22161" target="_blank">📅 18:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiBGEho4N-vmmjREn7f9EFlp_DPEaFx2BcQ7Pcc6lBO1miK0V4JQBYS6B8OOu4efsGwaMnI1njboyNkeKNVobr5v_YhHMq1uds2ZRSZWaOZJfRvze_7hGaHOs6NsRHvnXCF95iS3DyaMp6-gNhmtFcOq-bSPdc0dSz8wd4PuH7C1_V67fM74rBzpyEYzq8XVLYGNNFe7nPf0iSDeMZ_0xiNVtMYzA7SPmykJonXEYlzmZNd9OVnte-h44_OEag0d1gxRgmMZGHHczSoajuRa9C6OV-KYZFgrQ5Y1-oov23CSiOcEIZbK7mGCIFTPWJPsiKtInXStGAEqvXLNNcLV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYDC0JSpB8uD2-M-jqckF6T7RIdMZFqLGHr1KU_IrUGXfWy_b0dLMAsCvl0B9GTwFXYVBI3Ot1BQlepkmmQHkTZ66mdGtgXnvuxXb4aQTS7lG2yGg-bfQaJFr_Vq42Yr2QTEfQr0tFdOY0be2TItomSlfiCNEHLIdHD31pr1LgDMaemtlUdB0ZlG6saY6cR7ROnoeFe8wV3Fbf-AWb9ut8lQosrVIcqodO2h37jnrreqs_mvs_H9wzsPHTTrKNzQr5-vdkHI7_iGALpC34yIkXa9-smFdqeoZNQvtkLbRfnX0vSKXFlIr6miVnweHSOL7iwoKIJ56V0ZZNoUTqtoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBkHqhLp2T-6MhyjtLZxHZFZbNBkB8X5UYoLZWXWaPUe0H4VjJ_iOAOSFmJXHRl0zXZ0XSyV36YHhhHyHccbNc3mTancajbP8KFivfuJAHuP1V1ppwUZpY_NpQxav1pbvGhTga7GrGcny2nNCDJeV1TLwIXGNljVwyV2jPYdnlfOz0dIRPYY7x1mT8nCN1NQVvUDvm2qHVF4UxEZk9U2v3NmF4v4BJRQTWrs9ikz7diDN_sU81c56LPL55UhG9Ccg0zTifTEWMG-deJPubXVudmrjOfze1orXpCLpPOz88dJimbyO9K43ZKov0yzdAGjNvXdxIuywX9jb33vtdaU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO_dRVmAntAUHYOkP3j8i9oA2dRp8Oa2KAY9f87Fn8h4a0yFLbLQ1s1nDMyLaFPSNc94mVxEzMM37tUfa4Nac_bX68eNLi_LNDk0Cj-W9mzd4DU_ubVq3d91Mw6opPogbTmQxET8dg3xTGqnc778sw_7GUn2PE6cHjuaJy7LBxDgT-vL5QtBzOOglklyR3uJSI7zRLONj4_rzrxtSZVlZi4mjBR981YJPkZfticsjU0QV5bkS5EcuYINOohAahWxmBKkfW-nf4gQbLdl2Di1nFzOxINPoyCZqcUFReDN8zlBfNuMhD_DgrU__GsG6S1OInv0Rb2ewSHS_t0TqwUGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzfuEhJu5XQpgUjvBVLoynzWIBGbrVsQrYooYfSzwJnwG7pQx2gihvlZhzmtVypRblxgmN7uoN1UX3lWaTspXkkz9WX9KYvn4CXt6n0lldX_uswpSRmpUuFK-FOvQKFK5Ur69nIBlQJUkCnDhN6wOnjQi5MMqYUoJGZ1ufLL6j5aD7dZHJH2zzs-vr11VaTm6pjxJ3eCyOu-BvYUVG4VeWSqxxoR686NeZLoS8m8ISU15z9o5-kjVzbLWmsTFbMgeXHjrwtBYPBqzsZZxme5_Hdt78Xc7l-CkPv98adDJv7BgqyQQ5qOwtoU-4u4PMRTBJPN4AHDJa5wb4N8FT6aMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCYc6ECHk3SLagFyf3Vf1z628GNBxtGXP0FAeV-ZE98auwMPUWfE0Ft6dHqe2KJnELUK8Zqpz9WPPZvZEWuP_KbfW1NG4vsitxX9WmsvBbYyOm6-w1cRquQeVyqCdb2ZPowKkj6hAhY91e7jUcz4zFvtBB_dtHCBe17N9KwSqBFK29uRMAN8WyL3SdFU_cIxTZ3fyOvhHGTMhPFR85wq-Vv7CLQ8Ji34Wf5axLr0QIaT7nIVON-lByCsBbbyC7CcnHys88JFBvaikZclskXgFmMlgWOLatdo_wlCqZQNVQm_eWw_i9R2q3diLEJ8UZczAhJqtnF9hCE4uGXjaIlhGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRab_-Ge5Hc3eFJoIujQp9cHcxwMq-w5fXGx601nwIaTcyGndKX5Q2Idq4cu31zdy4zXCsaIYex6esm51zMvDtQDI8p5yg_eJScadFLiEYnunTQVzk4JpnxMdghGj1NrAQxmo8JKtrjE_l3O7Y0xgUhS6-qTu-CjqWA2KgB3hsImqGTknX9D3R9G44A2UwyTEZWBepamuJ3emSSr7bad4SEM7yfv3eLmwxhbkc4zW8KSw_Ld9_qJS4GyVlXN3LZW0TukPOUWT22bC3WXmdyYA3MeAODezC4jd5KDROuA8UxYOHxPMyHnWlkmXwUsovZgKMfnnGCXpwN71gx0XVDF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSSGw6gLDyonOF4X6gC803SbhgMoOil8AWG4gYlShM1yxBtXt_YHp_KgMFcvG1iGFWmhm8JHbb1hzlnmBkfG6m75xyTs1SFzbQHOaJIVTWjR1jGhMHKdEJoBfm4YTD3Qjs_9RBsytASJEYxY_EbUM9e3FIBK2ng8yR7b9_hhHaBrwANjxrDHP_d6M7t30HPLQNYEqJujawTlQflhP8G1svK-8eJ0W1DFw6GkK4ZazjQGueQXpJDgYAlU8DCrZNmdi9lQX-RBbb_q7snKoxOMstdoq-3NrAC5R8kgS_X55buPtf3Uuqnv8imS184aLf_KjwhQeJf9UqtBsZKn0I_XQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCHtrwvtbSbGKYvxa3tUPpTG1q-3hK2ZePRt_OHECwsnTgq3vS3S7FJ-CCWnQ91DEWEqyH3ptwgS24T4K0ieTbogOQdmuZGomwvZGQAiRoX2DSg4PmueQpuRjJmH3Ifwi2j8wOmgxVpWwIAV5n0ngfnTGOf3a_nMqNFwlgOLK-dKK_5x-zAIUbouzQhoWIF69MTzVjzfFgPj07oAzDtb9PNV2d7qUSgFo1HZhE02yKmzLzRAF5PCFoI1-xyeoTPW7j2teDfuE4GyOSmAVsN4Nk0baalmVfiABrnYdiosQQ7V9sJFAQIOkBYJeVaNG8xhlunaPd7eED1vzvcVFLISkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22150">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/persiana_Soccer/22150" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pattams6lDxb4XpAjRsaLuh_oOdIS6HVlnpxdGImlbyK1opyPx6l6MaSr8h2SLS3iV2SXUdsuJ555GaTjfOdgNm0EkvoqD1CgLFcx0n5F6L_04tfaZn178ZDXngqGA11XNX5sew2HARPR0fOBCrwmLn5NFuOfNSQVVISwCt4eC3p-NVTbwiwEaR1quH1FsPKM0AekZ5IQMkcv5iC9-qXeVBnB6qLiHCz9OlvHtfbsojXScSTdLbNBV8FhXxJMkOkfc28ZuU48gBcKc-qFy1b3EoaTcNqjEIFyPtAaht2rB5O-GuhOR7N6doak8ewo_xLTA33roOO7G8jKYxWA_uXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIO8VfwE6nLGUeJb5vE433a6Rg41CYwYuvDHpIX01VEv8RKG43enPlyPbFLwnR2siGsdDvF8SRjcWCBPFCwA1UaG8ttc4xiVwXo3-Pv0NV9MfOzK_lIVbUK2YRvxXh5dQ42QhYc0x-eyuyt00L4zMBocqQN2yMUdlHyylloCp40Wo62WXvquXAVJJiOQO6xEk8O4y5SeUo6etkMr9eVDGy9WtpW8MSg891nAAKG7nZFnBNj7i7v9RrRsbYqrKVN3BG2vev2KIce42VPrI0A5LN-Nt-wCyxh-pnq5r19MDpDs5TZ-m-I9qZJ9So6nPDxAm0XSf9xIN79XbKheUSkd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_OX2msRDN2SlDMHlox5eq47CkLxQSZyUqW8uOXjzQccZ6-Ux2seZGrOJYp26c1StjvZoPJHi7XoQDbpZRW67qpsaOb0GohJpJjI5SunfEEbOEctgNkRZNiJw_x4FGTNCwIjk4gprRvd_v5mlEnvh2uPV8QArMVpS2vB11Fvq_0D3CO-PJvQYbIfvjc_6tr88kM1uoEgdMq44qTKNTWibzpl-tliwuKKxXZ5wLTrpzJEgvktOKbmMw7scRByIHXwW827xIV15TenkV8OUUSO5w_nYijtveKSZnB05v1ifKVYIx45QbmykDsfOTsKEnnY3AMzpss-3G65daX3aeHmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6DfTLasxgWniEWbE5J3At4iqXwFL6Mx5hLpRTNosZlQLmeO3baUnimx2NQvE_mhPqyEhoNqVzEHW2eJTPctL91SuPtPibEFDcLBnoT8nKOFOuqRzj3zwjVp_gb3KkIqsXrhxjpkL1YnW5EI8jwjOCb9yeIfMeAduueooGKgBHHo-Z1VJh3WctZnW1jYRwaWR7e48k1DJMhBgrN5cYYMwaqjNNBzGXEUB8k-28JhMkJyF4_UXJjRZ8P7xn-0m6In20g57Xui1KUzsp6s00jtr2EVeSONBoACiI48Ps4oVgxsMN65pwTTNHJAGLTREFEsWZY41LXCYHPIRAq9q3uphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OI1i_UYyZ9oVRH1SKNQvwkwzs8LnNZaLKqG6m2aeOLLLFoeMR9GzOO9j1RNj7HHGJI4x6AdxZ4hBOSSdGjqfC9B-ANcj7qCgWHSDImrfqimb4_ok99Wnn9jwgtLzVEf7VCX1FlWlqs-w2ZbHxGYwQky1zhzTTNomseTjivhSx3Z0O35DH4q-X5w4rpvnPmcKSg5MlgkrklAdR9ic9b-V3oOZJ28cvsfowGfXE-GyuHCRs1PzhhhtOx5DHLH7n7Z44XKI-bJiYxXav1j3gTiYjDFScK9A_qXxa9mbl-vQJNxszQlIhUi-7rCzwgVoLyIMQDnDCvXTHNHggA1864BEHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilbN_gme-dzR0MjvUrKPjJBCCepp9T5Hp9OktCYpPBEPwWIhesk6XZjKZIU6vnmX5E5Xh3_HlTKJUJBRwIZjNjW12HcmXy-1WcGzJY8gfoicMkt44w4q2a9IF7rRDFJs0jXLRrJxY-7klMVc2rDn3EeOeJqAklCNEscUDFG62OVAVyh3MM6DvQ22LFzrWjl132BzM1kLCI4mc8zaX3sic1fgnjKXQu760XvthH8_RnX1Cte0H_X5RpKpPgB0DqshWX7_d-DDmeDh_S6VlNXsteaI_USKg-2Y9XDEH4j5oE5nxey9XsXmJ5l3Xyi9z1ph6Mik_wQpZUpukiq1OCARGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx0aspYnmYLiUx71vW5Lv3RSYaerO5s2d_UbQrti_usZCoz_UE_uUmr6gnEYRub6O6JQK57baMlzQV0Q-l_FT9Lz9IPAl-4gyErhTPpGOxs4GhG5T3isxoyFLw7dWO9Ia2iUeyQjOkrteIwxcHp7yVaF2ngqKMYJ4Q1qXlcQtV3Tir664GsN4x_jRoI0VeTh2DFJL5HVDBGgTou4T4B9ARTTm-4qPge6BqkYkkIOwls8ETm_NGX6UCR8JdNiDJEvDgihQRru1eT28Q0whL8hGSc-bFl5qwgl28UJVTk_TSOJ6bDotGSM3tZgN30gqnSV1FSe71vg_MzEO43WBpEFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2RTqAGg2yRUd2oGomY6QrwXUJwhF3abHN01xhue9cKtRPBvTM0cHD7Ip4p_bgleyj7fcXqpfN3xfJohC9m14NLaUat1njfOvTz4RnqvBMENqxA1TORjWMJa1i6FndJKUH7eOSZlt63PYO9U_Ap8LJycjxh83iQE6JMwASxpQ0BJ_ZMmUN0GEeyus6mOc7xDt2CVWsFrKevhRRNlSeHy4kBZEsEZftzu5OIL_iYpqmh9aiI0ZZhZquabFy0tH7ZAGYowFTf-6SIcjTedCqH4dP3Co9Bfm7ZAw7I2P9FbVICg0HhxZxNxN8SECjsTBayCZuGWzd2cgICqeM7Dtm2xYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMjae2PLiQefxJjdI0zIdDTeIJL_ontHgu86WmNZD0yUzFBAUXkJV8PyNjBltgAbctkY3typl35qhGdYYVtu5INc2AYUNMN0DTbcNAmKbX8Csf0ILpkEHJOpEg1A99iJEl2kYME5dMIl0MlOOnLB3vLsj2631698sOzz4w4iqwEgPJsuDuf0PO-Nm48Gd1_v2H7mz-d3WUPBMhiirx0p0wJWJFdYffaZ3U-6Ze15LJfyG9Gzf7ok0ri6yxCr2ID821Npxjk_yWh-KKLX4riJAVdD_s1DY6ur1SuG4rGqLJZkNyspr89aROfdnGkUQaucO6rHjXNmJS334Yetr2wJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNoP2KSIfU-wUgijflXMzmNkwVviMPvyp9fyWZrxrIRcVGaSKJrMmP8QdpFLvLNvP0mOrJPwZU5cGvQw8fc3PIaeQPQ8JRISKeePxjzpYpGBtCHbxoZowEpcxUejTkYh8F_zXS2Xwh2gwVhYeZUO9NPBZUuRdHjaNbZ6fq0aQwLwv5eielEJTsUJKFi8og6gm_ycRL66FKD6gKJpK8DBd9DlIX_BszrBAyr_zexvOSNFVpWoa-j3yV-7RzKpcdbBLypjUBKAkLqvekunG-_hey9IbkUpqQQd5DVQPOIb2tE5dYoFhxu1LsRj2e0QAkMZ0NuPcyb7J6zlp9hlkTQBMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbR2308_GXCJdOuPf66pofn6mipDpckRgs0B2rFzAaGvgHj3blwgAjzDJ6vYcAp4HT2PQdgvMQVXEPxbUijtcY_BtRN_OmrVG7fizX8AsQ07MuvFiem5OHIF0jOcIU2gTrUvfA-MGA5l-13trYEGYtUU4ckfYMaUoZlKkEgOrKiULQh1o0kePKGkmrPRe6NwZpr5sug4t9w7cWtfCz4WRfHpRL9fTG5TEu6oFv7v7eeLhb-MEw0cOfn86kZ3jCdHT7CZ5bJxKd41D1uXeTb06q0k02cDrUKS2Ix8viFdt6ERA7mN0kWizjfOZIupcTGxZ_wPOu2PurtgODe9f3u5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg7SHJbV3N1phfKjyug-aorccuLojHuM7zchHymFAkygbkcanBXPx_Hr2YCOncVc1YZpU4gJZM54EfFaemdZq6YItN1pr7KsINNSD_sPXpWTvoq2t2dYOMip_hX94S0u0f-2d1a-kpPCinlmSjwSIg6a6zwDqOSG1yrwGuflRwsnLTu5aNW7mpA3blxrHoV1LCiwz7j46FlKDmEnhsK47wrk3nlnro8udQeUflyLew1ZI_tm46c7MPf0sATayASJXaTili-m2vjm1rmcTiWoTeILvWSG2YCoZgPq_gXUI7Gv_LKp8m2IxxmfWkDML6frv66uR9hQjty5hKGAS5rYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWFls_dcFJUlQkFJFfJFMn_jUjCcMginKbgDot1zC-A8P36E5FuV3YlmHqpd_Stgi4YjOUsEOJ3w_h82rZOvYZTWy9cWXXbnRKuPLhf0lx9O-ZovglXAacKxzp8GZGg2trDILBgAfEADJUkQw73IP-IBJFnxWniXfCc__vTljxjnOB-8nGmG11PwPymmoIxHPvWsjJ50JzkH8tvKUIrKPdC8A2HdifRnPJ6JqMMzr5-8ChTGQu_Gwgz9G8YepR-JtlKoEL4ztkPBS7NibD4fWr788oUfV2ZfOh2GFE0qve4vCcmkVjdVVOD0CA7eMHFQMrko6WNxrCEcnkSqBccyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ztax8GyVtV3GWZTcBBqxgE9d0UiTH08y15OVecvsmyJF8LpD4pHstKXlB-dJsDSgs9fXY9GSqY7NHpDbz32i8ZfyToUWr8udK_p3h0JtSl0GUmebN4vs9hcGEwV9sdh5CY39cqHTbZB5cDFLaw1gcwS_xyCkRLV93oGGK6Dz3k13J46Lf-NCO18MO_3apPpdpgQ1Q0-BJajCkw7kgIH9pmQOJ-_azyUwZFdC3gUQ13LFhgSPYpg4DqUsf5pMkPakMswyqlUPwrJi_upOZpSEt7Iy0bZZ6cQlmjtzdx-DYBw4dVW4_T7XP9c39g-7UPHfbCJrzBfJW_NjjZER7ylurA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdVQIqDdQpRtjFC-3RPYB4pr468VNMKp3ICHl1Ih44Oli5ovwI0USqalFZ3-r2zSDmO_LpSIgD0P6UV1Am7xJ4QZ9D7GkvOc0S06GaAqJuEDAFGoAO2iYTcuj_MIQqk3EG40HUGySKtK7FE8BPSckuzE6p48TlWpzv8phR5wRWD0jOBV1IfNmrLI9UnYo2i4_KE-hgIYorMtXn4OVnqYhsdfX0UoCPcpaLIje72x3_9kCQNfNUWv7NvD5mxqjWymaFaDGnGYpcrksIRRA_XcM2O27OxRMh4nuHu3dAj-VxCDcj2saK2IVqrRuYjO9QI_ayoPulSj8jy7RXknQMJhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dub_PTcy_7GNrrE2Qwe9kSr6liDxfF7M3jqMR9DhkQlsQMNEO65o38r3VrBhRUfSBYUEMBl6INVh08ON9jQMqypjOsO3YE_BkXCHCHw-PbrusHM3FcRovPzMX146oWM8twgI9QUd41iXxcaDtTzye8g7cCGU8TQvQo3j9UpjiuPz7d3794OD_KFxWMwhv_LmW6qWkunFVnC7M3sSY8_Gp1VMYqZ1RTVbnWUb2YCbDBPJP1wLJgZ5QG03CbK-RDWuqsY2yhUNyXl5Krgw6lyTaskKF-7JaD6Rr67hI2matzSWVTpL2UijBQ0lyMdEELEKlUtOu3h0SyxmZjtIGTNsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUp0YbJ-nheyAzvhbZepLWjRh1lEpc-mrNOTpc7BrUhoHrM825ZcQK_BJeCBku1o7kyzB1qrd683OEgLe18JKt8ijZUjX0Sv6mretLCKWMNHxCXhykycNHnNlhaUcUjbGH2qC9dAsJ3lN0byatsW74RFNCnnvMG0Xaa2cmVT_VSoTCerYYHgsAvA6ouEEvogb7wf1CUHbYfBCf2BItbaoFHKzSKLaiv6RpiXSCFtQpmad6_YoW-faH5gC5gOUEj0Mh9Rp7E7NYfi_V_M5CbFJHWli1nq5oKAN4KXk9j2bRTUooo1inhaiUloYPY0EfTHNm4Db8CnpPdo5W2vYiaV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhg0wJRfyAtvzMwRGMhVIAo1XOXuMEf8mTjSGi0ZOAD68dnXZySGBTzU-HP54o6zAGmSala2qaMkxk1onXAyklznO-wAfuiRjsPmLzRdSbo1LOkSAHKKoxFn62TikzAIw4mOU2EFGOYxmyOAUYP_FlbUi3l5pD_IHwoaXVdGBWRDN2EoeDvsUL0It2eUIzR9YRSFJwMVsDBBxRFHq_tqQCHpT4JstTbHhMQUesCFM3d_slMZI1K6K-t99iiWNJxliY-zlTrIS95gNB7OF-McPghExH6RTEA3jYfh6ToA-rzFQw3qUN1tDKSZNc1Hm1xzAv3Xiej0b6iUythlEXA9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgCqWetFaO26PjuakUHWM88oPR8IWVkfJ8NBeVuif2seT2zRex1SD4q39Tb3VHafFtnvimSF-_spCKkUrKySCHmNfmwrIY-yRYWQY5IIlKpC2eL7uD7kGo6TlEJqBjLaXOtMg_Hj0DJpRGBo2WrTQ9Ujtbv55xjzpZRxCZ6_FxWe0-1ojd_YO8JQ7Ax__uH6gLKdyVHg8yzxRq8J7bk9xQRKHpUdhpHgBt-TAJxuYfM8i25r28q44aBGMNpN84q5XiaQ2GsJagkw0kcRQQ0z98K8zcJMWKa1_kFzcPbt-WzuO5HpWITQHhmSiFASiupl4Wst2fYJzJiT4GTw4G_uxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyZCDkk5QRVj0KlEmPXGNeMPxr64kKQeN221pDvf1pZSvzKpLaYtt_kbqEYc87jH8fA5T9bw5sf24fUbk4GCk2Ow-9hK5agXQRuPtxo9NyAkK07Oxe9MSHYOUiahB5iQxcqz0rjw15HUoS66OUmbUMTaAEHmADAD4lz-INUH5XMSlA4MxwYYiF-mUUmOaNZ6TRoIVmjyLMWzP_eI-hBxm1jn0h6fCVGnw6JRISWVD-0ZPdbCPjM2yfb-K-cds-c9B3fPIEh_yAOYLIaJYwEShlZ7lulDISE1OCZGqzIlpQeDEajIOyO8xWE5Pib3aqs9qxQbeGQvfw09Ex72NBPJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er-fDk9gKM0RhdUiyliUrU35pjHl_sW1l6c-gyOf3sqFSj2HK36-Mzs_uEhVXnK0RKPQIhNSC8ZsSy9GSL4BVxI7zK-yv8Ha43KbLJVNeODVXKwzq7CuM9yX2puG0t-u0mmPUCAnmcx-2pV0MYhvWcgQ19HTD7LniJseKYro75flKRfp6eRH8Szw_utM04PJDLUGUTnq3uQt7B3Hc8S1jYeCVJo9vZhwFIbDW_FeA0JtPYHQpieaNVlSw69xKq13oa5zWdO6xPX6zIgWIIH4MmV5FwFggJWNnZB7rYquBHBV_5KiGfRlO0QBtN0kbHA8UdMHAeiQqxL52yL4Pd8xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Dld0bal-HMJgG946uzXaKETXf5UxldO0AlDCR2QfoMJ9ZC7FPxvKlCZMhvCQqJ0GRZ3UceU5kr_cZSnlr2Xu4wOOgCZgKvPEoRs2k2NTpcK9wovQj9MQu9XThSzLPqTQUEePB7cT43R6trIXmzWZcCj2pUjQefLTwscCEx1fqEI7fp8GNOPDdrE30jNkQ2kKBQhjHhQUecOK-y5cK1ToopgD-XhNV7mTaGcx9qRh60sTci7chWpfMvM6reKGuxMKfqL7UvoKhYKwvj9qCE8rovxeZ-7YEslBjWNEDuPgTDIrGaqAdgK4GrK18eNTJA5Caxw2GClQuZtMuHczMUH8jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Dld0bal-HMJgG946uzXaKETXf5UxldO0AlDCR2QfoMJ9ZC7FPxvKlCZMhvCQqJ0GRZ3UceU5kr_cZSnlr2Xu4wOOgCZgKvPEoRs2k2NTpcK9wovQj9MQu9XThSzLPqTQUEePB7cT43R6trIXmzWZcCj2pUjQefLTwscCEx1fqEI7fp8GNOPDdrE30jNkQ2kKBQhjHhQUecOK-y5cK1ToopgD-XhNV7mTaGcx9qRh60sTci7chWpfMvM6reKGuxMKfqL7UvoKhYKwvj9qCE8rovxeZ-7YEslBjWNEDuPgTDIrGaqAdgK4GrK18eNTJA5Caxw2GClQuZtMuHczMUH8jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHJxsCB357iyHOYKnAO5TrlwAHEex6saU3KGddQf7X2qO7FxvzzNKzOidAVc_CSHwH_v1aR11uCOZRz_XwEIk6oSZ_sf0Uj6PfPaFBTibUBFdxC9ShRPR9l7AON4ojy_Zs0JJ8gdNVk9FYCWbX1EQ8-3xhCuXCWtQU_KRWldZf6cYvQ-ehvaTkKNvHwb5rSAyvL3EdF1eiCRUUoNIg6QlEYTPfB-2c47jFLRhszrKGzZ6Hh7oOsaA-8ikJRN6ve4soOKwu5AO8po5rcyknJwAcuTfwP3taCDt16h5cLkiHaQxTu7gQ1H8dRJGt7Bxm_EjX1n51HYjod2me22cKfOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hyTr-8FabC1Xh6MTvuHAFohkQUVKmEyi7ONOvu3H6Ria8fpPBuTobJARuSZIf8Xl9fZ1PDtbw0IsHoqtyCO9GfnYsl7Nt5uWN3xShoeHcIvFPJtFC9d48GR3uRWwExLQo4scNbzhHXxb0GFf1VVL5tQiIuu_BcOMwjP96kkUZUQFAOv0AveZUF6WlYMXcDF1cPpDM6NJDTPB7JuOx-zorqYeOzCNXKV_YZl5cKhDltnMo2udGNgVQMnAscKebY85EIgWMRq4X8mo_Txd-0wDjY496LpkiGEiMRLpkDEUy1grSnYcPpPg0IJZ5JlvEkTJSsDasXE_paefoophy-m-FQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfKXhN31YgQSIelAIqjEOKh9wcFvtf7qrGxYIxm7B6sBL3wz5s_lZfdBbWs7d3pibhoH4YOzNnlZaiLgzkRQxYOqQIM6Ce0Nq1w5cDX-Dd-v4btiN8mah9SgSsXU0fK9E5w70AqoJzR3--q3wB5AcigOp5Qu1rknwiIBRvkkG5Ch-VkKIv4L9i71Auu42W4rpQ9UdcnpKWA4amXaknXmin4zYPZKtve2wrswJba5NsdenLZLLKC9-SYSupUOFxV3OPvVLiqUP7lyenQjav9gHplaKd-HIcMAByFB_Rwhtz0ZYvIAPyWxTogTAckQDCExL9XxIpuNxKLQnYztca0fNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSC4joQ4_KbJaF5RXeYzspQ00TgisszuLVWlFUaC4wSnO30F5tATrbd7GpelbSpL_sAS0V_8fAMOZokNxwh-t7yx1TcZ_rHESGKP2vdnVeu3mu1MdtRa6KC9ktaibwt_q96UK4hZhOQcepiKM38gt1CzexxbAdvSyMKk5xSo7XaFZ5wQWynQQ74ncM00pcaUsqT7Ym6TlIJCTRovsstD64thHkdSo89N19qIHPd4jRfYfLJKgbqEQPpkomGYRQUe9XQcbdpEMFShyQAvSOEp52I5wMPa9BztHluOZLfcu4SBJs1tcNWxKRxiE5DuOoP75dikgVOQxCbadkVrX4sf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvZI9Rrzdxav39alGzP5Pq9nd0syhJQQ7jjeHnNTMNZbb7_WlMSbItyuqb6BQMtlBB_-sAdwwCdImZhT2xcIPin9fSOWbuhzurpiAQ-9G37WbmHwfuvFUrA8soTKlkNz3eZWUnwjyX0zXfwOFsqwgPBnXwIrdqcUCJ1OevwSoxr5NCt5pelUpq24GNIldebst3vQMQTStcBrcSDamo0KebtAgfsV0VY4WpQKsBEHgSI9knpXGGb9dy4aRY6kCquBsh8FIBiWFZ7t86BTCFmM6c1gGuX2Sc-fGgCzJjyRZOAjuQacqGBpaAdYo7vaMNBf9uHf-nui6Z2Rbm4YesyDsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABKkIR1lQ1gJNoOKWuA4cjKuzr-bbr3A-FuOKQK3mbKqXcvJ4c6HEf1CGLCuSoDqvWQ3duo02KXuiahn1tqJCbhSm7nb7fdVXhkurw1fAwn_oxdV8rEDzDMnH0mzJKNcqnq3rdT4UbycXCLfigH4VHCkNV-aX8baYtHgnK7REkY0mV6bu5RNGOViD-YuM5PBPOG4JUSzy-kk925rAVcK3xWofbzlSUf3PjAKhLXTaaL3wG85ag1J_qThOz9Qd47elE4VVX8q67UnhGxgW13pu2hhYqFVK2TrStLlvoIVsVJ7WDbfTPFF68K8ilQkbVE7RYQgHmBT1XSydSZ026nuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5BLWgVyZjKoR-C4uTWvU3CqOsIZs2z_r30_4LqUNTBP803_wv0tuN_Rmt4XT61gpoZ_4K0WHzdH7i-f_L9VqgdHDQj0rz2y2y5GPf6QfGu7wN7-qYQ6-Wd9LGf9hOrGv-eBdX4xwuV3qh1HCUOSGcc7KIVlafRqChnHH0ktVjemxvry_Nf-De705Y4Gg0_axJcscQVNImeSRnWyGTV-rW1ty5gQkDB1P32FJG50fPnr9BDjOZWgi2RSmNXcCV3RP5QdCfg5FJw37QKPImB_xdvoQkyBy3ohgWT0x0kD9IiSIsVF0OesIES1LSDIMP8uAPUO3fUEJGg8zHTnVj56Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3XMin6fQ8l7urnnE3Gx17w3gktzxnX_LOcrJV-RVK6UqraXeGBeUj9duDirjIf2-YhIcZM_z2BNPR-0tL2T22y5oV9E7NI5dYra3Gt0dtaWyoGrX34W7QuB-N8DhDyFdq3LL5fCbst6iookxxW4_ffonEFfA41mz0Afziu_B1qhxvinDgHhg4mKn07NwDcYo0bqL1pEbEUVOcNPBiFYgdXLGldDyEshtazmAlK1EqCIMGyAroPL6XNU4KkdnO9vwyIamr5x6_VwvThQvUATshbRT7oU2SZGvzY7b7KglmHFZi7KqlQB2hwnGEkkoIIfWU4AukT0jRB8AFS6q54IBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZkmiUYmRKVn4FH-Y_jOk15QYyloGrLrgXlM2IMmgRTx8bd7szHlr8oZ7ncMMgzWLkrMUEGHY6psjXr5B2m_pI9lps5OoV4UxpDj5spICRq9Rqr6VHAcJekfhYrwB8LJSsH0WtvnoHSKL9pUHx5c4poeISnuZJDk5H2VVKrAASTPAddIa09iMLUynLBBglXUTLWk2k5fC_BXxD3H6TWKFYqjGGuK5P268EFNgT2J8dcyVXNaQgfUY2-4dx9IUKU_PjiL2VK1xppXevxR3DDawm0bRhWmLDId8KQlgOouAw3Nm93DAK29PsZv6HfkktlbijzzHbQBFiMlmMS9yTd_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DleROq3yTnBRKMLluEbYIkYA7AIeKkUmA9Bbgx0fclNIvmMXZAwYvDGkQcBUCSSERiY0v_u6S9IfIGdOIZA-y6XtWHzcmEEdwDeagGEXHyWLiVmAZgE44qxYrAnJPXgIoytKU16XVc_l3q2n8cwVkiF9VJF7gXGJ7LzSp-kWWwxlBp3pSuBIbuBfq4IaZDCXRvgOvZQ4FZrre86d0umQjctW0b-o2qdB-PDFW0hKfxSLUQi9ZblDCJOQqhfkAgDiSRvc8LR_AzlXU5sm6UusgjcKwRDR58sqtleVwnLm4PeDBtqfHmZx4TM0IU7d8XAx9T1XvaiZ0GtB0ht3esa7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE42BwOuPq1GTo5AVqKH5xEfiM12WhjQ1Q24CcEcsYJK4XMtSOfIWmpViowPwZe6kvXebv2mSc0BdCZtLBq8-4m-B33drHhTCVPw6yHGZJKauY-4MQKMvvyI1t3O3qYsnhCsPwsCokGIxyCPllRuB-NRK3kSC7mjcwCcwMwhbC15A-Ig_BiuXr2-Pbx6Ata0_LlzzPXgUDgyUpkubWQj-kuHpui1KeS9mxjjZGPt47qn0a4VMLUNpiFB30Eu3tkiPzXZX4Ia-AR2YgJxEFtlG_f-LNRF4SE1TNXmm56-WYSA537YA8kqT-oOr7O_BymXFqVscwcbEQOVDAAJtNQaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ezrw5lO07XHCYCF8V9BXbwaVKe5r9otWQ-g1LMH8v8KXsAsoAhKbsaVFXCjidMkJmZcLfoTMwSxu6PnEgylKJn5prHbnyiYWSIETPvY_BbGPtfR_YjTHzMrAfxe6djIHV8saM8boU5aNo_4A4-lss4c9G2OWCIKs1S4mw-eH_N5VZ7RAqz-7e6lkf_1LHZFJXCTXNDmkrtuPyDPSBiXlg60MNGJLJM3XoUcpjH9NhQ0iGmqDkhEE3z8bPsT1odXdOC_0BKSm9z3N2Ozby_2UspOX_wS8EOifbur-Cu8SBiNqGEkHiy-_GpXt_fDDXA5jIJP8McbMxGqEg8-rvEMV-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5n2jNHVcgWAw5Ojljz2j0ZZenCxaOqmors-TW6SXW3E5rA3g-oLVQgOatfA0LOKFsKuCAJX09xO-YVhqMjuMworihlQNQOYqp6x9PmTXkxLJe_U2r0XErAsLYIMzXM337oN-LF_JgZmSifWWDIo3SaiMQ72xlGteuyH1apOMoTNUFg21hKFM-BZAIZTFxT2DibuwUGrRTG-RNnbEwfyGlxLKiHobsdZJCYzvmagkfmGwm-wVKKcJkuZeReHTVEojI4ntItaw8jIYpmm01ykLORUj7M5oqBaTKLVA1mpmTdo_gl0uAC3O0Uz6k-yq5-Wn0j64Ch_CUVK574Cbc1wWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgDBlChby31fEgo8p2V6Ail2X2WTmWq3qoviFU38twcoRX36LZ3UV8DVqs4VIMm-cKeDivJWtv6PLhy1rpMHPC-SgeSXsoX_RRf6sKmNK40uBx2evZrWKPp0PUcrhNRa-2f9SZamgbQIHF0OY4wJknXMo2-EaLZZyNHq60x1_3M_6kVU5816-cEpbFnk8dlVeDmHZXeh_CrJAxnnnYeMzS38YIEzgWNwRjLk6kiT-5tnDg3Fpi4n_xFLslSuU7NoihLfgB3E-e2IbXX6rARqRnDrIIgr4yUxWGJnOhbf2SCRD8gRzZjf1ZZ2u8YQ7HgQFIGtXAg3GvVUQyzwG_dNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=GmZQpDMObAPXVkgqLKnJaJXyrA1xjVJHfnNa5KeL7mI8mAZJoP2VfmcCisY3j8jNTK8s1X_mq4ZqsWGsmk3hs3zF6XjKtgsTmc_7NxaHY0EsTqh-GP_j0bDjI1_i-uVzFMPeW74H6AcNHIDYewpGORSx8kVFGykZRT1UFw08PeAaO1w8dtNKG4sumNy5xt5vHgdt-TeSibLv2WcEypQnWRfgagwSpUKfz_aHH0l-k_KkDIgIVrh2OLv4c_bYz4cUgRGOVBvD5jBPeaLjpjyItNcUl17CN29Ohbp932A6t33wCTYvep2ugbeh2bbZoNIEWuZlcCvS6LEpb4mXvG0gAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=GmZQpDMObAPXVkgqLKnJaJXyrA1xjVJHfnNa5KeL7mI8mAZJoP2VfmcCisY3j8jNTK8s1X_mq4ZqsWGsmk3hs3zF6XjKtgsTmc_7NxaHY0EsTqh-GP_j0bDjI1_i-uVzFMPeW74H6AcNHIDYewpGORSx8kVFGykZRT1UFw08PeAaO1w8dtNKG4sumNy5xt5vHgdt-TeSibLv2WcEypQnWRfgagwSpUKfz_aHH0l-k_KkDIgIVrh2OLv4c_bYz4cUgRGOVBvD5jBPeaLjpjyItNcUl17CN29Ohbp932A6t33wCTYvep2ugbeh2bbZoNIEWuZlcCvS6LEpb4mXvG0gAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XadJC-dYKTk5TglwrR8uBv18ercuDEiGpHugppkZrOY0HPERs-0_v1JA-Ua_-PcL2caajXjiY3CQ3qp0_QQi8VQnRVryiG4PpoNZQ-cVlURfRFisBIJ9JMNhwqLTCMuJsSrNxkHHWx_5AtU6RIQUqObX_Nb5ZN1-qG7AxchEnos0oPG5qnDIi8t48FyHFJEbb_OUhWQEakhR_5mnVj3SIVqhLOGQWlGLM3qL25_zf2-DZ1HvOhhBnkPJl_pLlMPm5wAcT9O0PPItJo5rwEmeEwNKuLB4eEZUTBYC9_-V13D733nWZqHzwvdZZ-GTDhpeInxCrqaQutfMqEUIYOH4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ5BtRPegmPKZ61JI4CpyvRJX0Kdn3IDvKt-QV9mlBe5Ce23tn6pXdzaDa_5VCvah1QPmwcpVwkoBSk7XgRDLQcmDxgSkzhQLezsmIg2bK3IgkTMnQ2nCncpAAkGN-pfNtKgFYokwr84Oer1Wvx1_GhoZw9-E7H1hnvZft0i_HjSKEtsOLoDdxYr4mZYWYmzeFf6CSFiVXIWMDAKnbpEvBxl4-Ae8zkVE-M6q42FZqqQ00iNFjffbEmgzwQx-yqivtsl5h0SQaoAgh4U2YU86FuhAqR9DPAmrl3ChdHC_sopxQ5pqjt1xieBYtNPA3kLA_b_TBA1vb5hefKhw5tJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-K78NtORVZCVQCZ1nSTmxkv-CE5dZqK3XcRvJwv6aTKXmMxJOMFJ4SvCej7hb5f-5jLqQM1UKBmUmPPraodAQqZDdzgbhenvA0wYFGSpzGieM-IHuj_sCfNxlwi6q1Udc26OeDF9Ze5udkgioxJpbjes8TC9ej9fzm8kR2ahOLNaQNCf2UN9B-VpaG8R_-ynNAZATr7DaQMMFsUeTAiZ_j-zDJXz7-kBp395W1nfnqB8AkwPEPJ1Io9au3gP0J3zx3pvLdm5ckHYFCV04g9SSEuZBYnxMmCUR7gmw2MV0WKvXFpIYiJn3dsmNF-F-oa5jz1kM6eTQb7KdkPGPO2Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnOYKm49FBzlDb73Bm-4jW-c8e3x_p429MSMy_XP8IcRUQ3AtKRTrtkmlehLthvww7XlxRNULA2vZxC4K3k7e9WdrzLREM0BkuMOF2AUWrI9Q0TNX7owfGQdRvUnvDXJomvFL5Qns2rTfpJDznXT0inWTw0jnY5AkR9RfYkui_hrjFGPQm6ASCtyCiAs6gPNup1FSAD0WrLeZUl70BVYeN2t5Xvn_Z9ztCrXrP3l5XruNi2rLdakpaoK35klZX8COXNa8aQJuZbm7IaDHgVQna1OHTgY6Fk5aZ7HiCCTZfQnRcWdpcK7vpPocH4kMIp19AhCVanGuzUUfDpcwNq7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq49AxLliGXwZ5FDANIIDo88SpiO_7hI57PW_LGJR3-JiqdpP2pIACnhYZ4kSoNKdv6A7mFv_TkoShAtMDQl-R_Noa8otHzJaBC900uHOrqBsV8fUI4so0nfyl5MZzya_iu5pLswK_dp8dLDyUWDQbwdWmXjWdVwur__yMvhh0wZ5PODtQhw4iGP3iYwxYw2XH7FSYI_BAPIeZCSTFPDxw-MTcEJ8J-Wg63h0qQLfU16RkhRusl_skKcDzS8FvSlBcmNpd_Mg-2AKV9mc3toq5oW89JMMbKyvrmL__E-Q6Ck6qeYVdg1bjzQP-stHEJS2hsGUQeWskqLwEiQ9NCokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzprsBU_-NoahFxNE-ndZH6L6hU6KI90Rpqwg7gUCDF4MPgoVG42trfC3fwPnaBPpSWVGwVzoO7_xH8HcWAmu-dF-PyJy_AfzoFJV_PN2y3oZN7-F_Q6LNRM9LfeusgdlGbHbL8i7EzREjtg5DBrVT0qR9AtHO9Kcol1DwzXlR43T_9s2-TO5XEmnonhtY3WhOEagym2mCK5wda_xiFeTtxYRwqfnS1gTKG-JlOCSPv47yN_RZZQyIR8h8foovjn4NErxtImiHH_vhSy9k6yj6DNKX5LBwnibK_fxeXH3plrJrrRnjpMLp4Unm1-8KDjaW0nInhJmX8N0hOGsrftEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-6C_9CRlduUu-j7ns3HJ_dsRUFQ-9l2i_O90l-L9yaFzo48c8G1Zz8zrghT9eunm4aCExtdKqpCmM8jm_vKEaM5FNMqrNI0Cw1Y-NpP4O1ySvjivlBcJhf5QbmMPdrGuBh_2QWqCF1p9r3obT2mXjlgrXKESZbYGQwaxBL7XYdd85mZYrQE6mwFnHafzCmk8CkuTC1bbzwh-pOLetxzgKIGRZBUyPBoQbT7j5hBCrjl7A9Ii-X6ljdp2xdeeEjqlkCAwxD81lDfbJTco9ODFuyvqWpu-V8Jjs5vX9glB9ouiyG1pL7gWxUEwru4rebdJKrBU-sNmJg86LJYiAPReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruTL3_r_3lo_y3aIykpvBgTAg8z1tITXyq7mQmPYiEsoeoov5G-7s9H_nr4-4qUaxZ_7GJlnBzbaSjGoz8Lfzh0bjvTqTg_EpOb45k2nnMZP1KbP5LS5mi5DcdMNEeKJs7cU4Ry5cYIAPp94BAqADH0zvXlst4oVeuipY1XJLeie06ilwhhegxZfNx6knvIJnRCU8qkruy27vTSloeDm6Ct_Clgt5HwSQAYGsZASwC6B4O45rA6w4WF9IoO-Oy1yJUZv0SgwfFw4VA8MhcTJGjkXajBJYmFSR43LSzL9ulSBi2peT-1URZTlFO-aHOcdvyqOheMjz1jO2d8UK6t2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpe0I06-aSP05OFmSlhYvRkWKoep-w7S6zNSIez0rJiRMoaPkoap8IPG8MeXm-UvWd88OjLWcEL1Khm2v8KB57hQ55NbA9eT1WAPBxWdmNMj4C7CNT5hpyXkgNQdP_uci_6TE2H1ZYTWeoZ672xy44flYxgu6WYijGNu7pq0PJZORzFrUbS0V_fTE04ChJ_2NEQpE1SXRsI7QhnwxM6FHwKRG92g16udE0EPpMLSLLcXucxbDHO4as8j-rK1EphImG5njSX2l1UHOx0qSOtwIDCSNEd-aAr9BDeI3rVVazo_4eucHWaeIb-hlavcRrD97okQ6fiBs69_4Y3upAYfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSZ9ig8mVFos8mgxIqISgD0Y0TrCWwpmseHz4CWuKePFUSmPhDqftqSy7_q_Rb389pKnUxzTDXuE9RpXkbocHzhsXllwgrSzB4I9ENSdrYmpEv9A3U73vp8dZTiApQf_bRb3xu9Wbd9qVU-65fjExoEGPSvfBIgiXgBRv764YIqvwc-4EAuVpYVtXWV564bER3tMN8psujpB2UiEYmlJaf83EtzcXbJQMUNdqV6eiPcn4B3FLixvKZmE35-HXL3S0eaZQ4DlxBgUP3NuHD1TdisZ_ZmM2lmYHFxkzxAg0MaXfIlt0Q-IQLt-UboETWe5Y3Cab9ktLXBwJydjVz-Mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL2WN3xM9ZRXBNHzeAgjTmeFuV32fgt4ENpJO58Z1HtVM3V9sc1Sll8JVt6hVpFnhDfxlH1yjE6XMUS_W11WVT_tTBDQOvBe0CptlngpiOZlqTK_sretE3ulqOG0lPyc9I2TI-yJ0eCz8J2wfL9BEbMRwzI59srXfuvEb7yWzNMeHyfwBrJkxOTI3X1DBN_JCgbJ1mWj6JPx2NuESpWADEcAECZJ7sZv4WuRrlQl4uIbdJlfyeZ011zEC8l1kbyh8pi1w3LuNMqVlxBEGtWIvenfjwOwBS437Y-VGt6RrOJ4zniPF4ls9Iwv2vVlFvqC81Y5nSN-oe38QbcwAFSh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2gC2O4eTRkpTblyI6iQYKCmd5rhjLkR7J52cqFyMv2zmG3_uUz6aau_JW9IiEf3Kf90Gb5nTm5KgrSa_akQGREOrqMxYd785ievOkaw1BKfFjHpllfqDPvTsAUUfxsz8OGKLm2MMhQinXeT5XXJdHzPJrX5__ZNn4jt2QeWQvo7dLzounQf4jxFYjxGHkOZg8Zi-9Rhb1EoDuluyAO1bbC1Z-U_C1dG24LbCf7OI31dBkdnAUqREo1VBvktOd6XvqeB-j7JfR3c-Mlj0CnLkzxyZwrb6RfBkY7Ir-gn3bkAwaOUkOMFxjf0wFm819c3jOKflEXh6klKhOrXqfiUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzdFf7u5sGQ8qTpD_FM7WhccLYc-lMXuOTiWUt94QlGwo_SbApjnOtIVHW8Jw7v3E4e1qB0qT2P-GjppaRmw_uVOfkVzZMVTqDfGL5vCbNU20WbsPewgVvYByttMiK777fYAsqaYhQ5pTP2XVYippCoegURK4cn167XSVNeC2DUXxscwrHYCSYtVi4EMcEgC7Y283pq8KO8FXcZ6mUz-lP3czXs8YcQGSKcnoSMRy9wgomwJmCJ_1apgFcBtJPwoCibzz7_-V3V7lpq6hwbJuwSCOSwWCPRRs99nk1aIDpUm06qLz6f1D6UkUpZd57OLa5918yCJeoHHPsooWZOSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuz5JOBKxF-Jblk3hmBtOE0R78KdQBu0K5EAIs8GoNptWy1cHpM2NmgvChYGnc8AlxgjoygpqxVKAi5Pv7PE2_vvw00eVrVuS-w4OVIzDpmOJNMvhrxoOKxcjXDVtW1seEAt_8-ZCOnWdFayhW59WcqnmDrlRI29ovfsoGLVJ2FWreqBDrEj8bGYqRKLZnRNZLfFqEH4FY-VZx-ZkbyYeCcFvMs3dN5SDqL_y1rcuko84wDci-y4-TDduATYu5VT4epZnQ0U11JfNvAA6qo66YWycd_g3Si8HeJbJ17RbEERrLpToFzeio_HAFNL9C4ms8TLwIHDwP0eX7MMh-QB7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSFGFRVjA73lmz2a65tXNoVrGna1mfT6vyo65kTqao3_g9lgjtu5QiMY0VUaalyDtpnMR2jOobdRoA6HLbN3KNM0I56hX22F0_wAamvETylMgTq4vpFdqz6nTPs2NfV6xz1l1JrQ-wzLp3elddUZQvmYv6g9bTa09ET0dfONgP041zzVp45Dpmn8vxgQgdCm8QlZsInXbABEgg2pIJHtBAdgIPhC0YtKIokvk8-65UObOC21Cl-glCMWW96ALBPLx8xfM21z7i8mBH6dqgNOobULqb8FZR6BwVTLsMfWDBn9gT_XHR9qczZ9UUkvdSms7B18LC1K3S09qV-Ja8kJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY7_lgDLJYB1yOETLBRspkuf3rudzXIRkWHPAxkuXZAFcEzk9EAhuHpi2EQ-BvB0M1r8qi--cN-5zc3vNXMIdhZwj4p46o0EcvJM_lc4eya6YEeSqThxIHS0APwIbb894Qa5DR9nNt95pr9nJt0ZF-fZzfeOmrkas4J2w8XlmeVRwpIZjn4-zYPr8zYUzDmhklhb80618MxelDWPHrqnWVPJZmwOf9KqH8n3caQIru4tWtepFfhGi8q0SD712Ml0eBflT7dqVMiHJ31j63I6nww4vz1A-IG1Va1ML-boLRNM7sPFS_4hw-LBXjLGmSNWd90tFrYQ62oetjIjqghqyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXnO-qOduM8DbjzPKUB6gIa9r0MfAu-z9pgy2M0UVVHc_qWnzTonZjOpj3AcfNBonXwSbaimclB4eE_omqdKkX44QUrwLIHW15lRKPrv5ZHwWsckK9xjxLAdAYIx9dOz6z98yCiIwFEkXyNtGc2ZRywAVSU761qq2uu9bd0BKkLDeCy8-Q9Cb9wkxe8qGOfUXF5mZ8horQo1P0N-4G47Oht4XAE97YW1kILOxpGpSlrouyrwjDw6QIy8znRTZ5b0LaXBss9N6tfFr6oo5du5g2Dl1gsxeeRUVAXmFLPTKwaTs2zlNg8W0jWRPeajCAi1KEsnY23lEiBA-LyfUO4RyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6egij9GC7HBW3uGjNMxYwLGcVV6DgT0y_2St-5kpx5-P2o-mPzMa8EhUbiY4m8_l68kV5dFSLRDzSsjC_AEyd9-eygthskc0SyitF2J2U3FdSMiBsUp9VMmzG5mPGLHv3MJ9GSYk1o15LnP7GOz30tf57mpmH2x6zsGPLEqvNyAENHubWhUZIhRziKVXOKXmN29sEYhEYJJ2ULjhpPY1VVBgqocyEF6WJQydzNMQBkPjQIxOE8BshTsFw0iy1-o7c_JUzpeQ1G9iv1YxNZ_Hoq8-ARGlnUXU4FwpjMziCSA00haz89Z13FcO1ZFT7xPQhoqASF6ewWEGF5oLn4CCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOKRsrB7RHB6fbStQIPHDbOh23wU844vp4lsm86OTOT7oF76AsOVG-1aDP8XWpMWI_UTt-iBjHylc7F5q8BopDv1Xg-kxSoCe-p7VRj4mAovwy-djeeHLOY8Pebi-rMluPkMhmraU64n4LyJfr3X5xke6Zruwhtn1T9B7VsK91FI04tB4QCxjpug9i4xFz6k7sM8sDqVNLJ9cNUhLUzSxIO7gtAj5mHdv46_-3kjTs6XWwROzfcSkdsTWh6lEhbzDn8B5lj0cBImswd9ESMqE0dbXrozlSMqgVQsoXsp_Ly6HELbmT1rMGh-OaawAkJlxFCfbBdT3s8tgwPvdTbpZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2Eb2HcN36OK4ErMaPAX6Gy2LjSoaZ4doYxz0d46sobDpzDH4phKQhGcXewuYWJVZi85weg5NBaaydRCaO-YBN81EgEH0_jsvzdEgG_wpdFYIZNhLuYsGbMRu_MZUDyfXVfpXn_6xyHzcICUjMEpMN6lKCnASK53uC8UZ6B1qAEUs2vAyPFVU2drEcA16TnlHR_MC-lF_t2SEUXIrQRa2AqjvWyWwhMyvUTNWvYlQj0o2ixbLWIBpz1P0fVXK4J-rawwdpdKoOWCYRaXMl7Gwdl8Qzzkc54VCa-FOCSO15r75iKxffmJvSnZjRYe_5Rz5lbS-YCjCTrRsA-0pnnyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItXvJ7yk0ZB-leWfM1sS0vopRcorxLbmD3jGwus7UGHB8YtLxu9NlW8_Q3bTuD2PAKRCAuyWfp1WpJ7ydtF55UMQC2l1epD1aylXErN7LzkVxIBPPSGoOgQselvdf7H06uzl1VnbhmDIwJ4_pHNwaXiOEEXDIGwK3oHFEaIAh-HJIrwKQq9S1s5xnVLf__3AE_Ye4vO8dFUh7_LEI1X9Th_b3mTGt7f3HfEC90c3Hz4niXSSl8kPM3-nq8BoxYk1OmG5Np2b9UAlG0uzs_iIT0kC6BFqV5mRJ2jZOI57DFb36PzNRTem3ZmTYI9HlAtwjXdV43BoEBc4uuw-U9Tsbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNAvjLSZ3C9Zs1UupIu--jzAJu1gjCGGkcSPyY_4kmBWBhr4hQA8Ut64yiiE4fAC2dlz5W8_PfynbPwld-7PCb9nRbQqzrntOwFRYNWc6_2uTofDR3ILn-w3B-vePfJ9jPMDtPNDJUOaQMktLi1SveGtO3icj2C5nO8npHD-JezZlOr09WOnaUpyraooPoz7pjGczWZy_UKecMpuZJGbglZQbDU1zTNIwj8MovfKFVe3-maDkh2Hx_CeTavMMkNsG_BCSLQJiE_0tDwjLvZeiLXqvW-EKldBhVLbYUnlHRv_QmNlGtAAz6-IUMDhvHCLm5IoCKV6qrDt84y11n9atQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_u7VDWt4Vn0K2Eu2IR0_F7zX6DXXYhX7C5fsAt-mH1IEaz8o4auF1WEuIVY3MTd8x0i6oY4ngwMcpReTbQMMGexdv1PpmPLv7GyG1-0cVV9cQrjrzp6obGJJcyYANqtX8D3JlAWfn84Q2OklMXjE6r4tlsNCeT1jD7Gr9fc0uODDaMJmBS9HdY-2ZqULF5V8qYZMrcJcSfXTkdwC7uvIysHVp0lwzTI6VvxDjUFXZBc28MJLzLbYoJq3VTciTtuReqFLbYgFIlbvGt9HE_ffThHZC7RgPM2YMFHQJFHZtKVqkqvgpUH-SDWdPZwT3QyJg-lcbpsBSdCBrl3RHyatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=s8DFlLF4RRcGXequruKBpQAmHf5X2nyln7MaBbroPrOQzzvm63v8K8ip-39yWweBZz0iPQv2AhSu1ET7tPwLqPk2HyabiaM_Y5eMUFtoBLcnZRfRKwR3mHbBO3BebcqkPLHQYNqM3k7oE9HFMtriyW1IsHxVBmkX6Tu3lVNyeBYx7-e-c8CtP0klDc2maRAHTdePY9d40qAcqVWAIHLlCUDoNM0gUqj-CE44yybgCr9EinOh2SIvSbU8JjDd25WxqD_L1mqITfpsfxWo7azB8J_fC52XhqQPPMwwDFt0WNabnDcihIG64UcQwwOD52YS_Hd71g0T41BRe-OcYcIsYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=s8DFlLF4RRcGXequruKBpQAmHf5X2nyln7MaBbroPrOQzzvm63v8K8ip-39yWweBZz0iPQv2AhSu1ET7tPwLqPk2HyabiaM_Y5eMUFtoBLcnZRfRKwR3mHbBO3BebcqkPLHQYNqM3k7oE9HFMtriyW1IsHxVBmkX6Tu3lVNyeBYx7-e-c8CtP0klDc2maRAHTdePY9d40qAcqVWAIHLlCUDoNM0gUqj-CE44yybgCr9EinOh2SIvSbU8JjDd25WxqD_L1mqITfpsfxWo7azB8J_fC52XhqQPPMwwDFt0WNabnDcihIG64UcQwwOD52YS_Hd71g0T41BRe-OcYcIsYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L13xjw91uXcoMCVuKaKb21-loXC6u6-v0AA1TvmD_8GfwhbI5gRuEZk0TW7ixp1ix8ps2ibqD1r8KvSsPt4rGH9C35edXtebWLWZYiA8IbO_EjzlUSEX5SO-zk_Cj1sRu10vykc_4UyZeXWr9NPiNxPk7alhpdl3nWuS_iqcNku7s2RPY-KWUz1DAXW2e4qKcmXI4IJ_EtbKkk-yM0OvoPzaX6c0Xy4CpiSCxXC_S44mW-h1aPPWhj49MWQ9kuGTkMEctOKKKsne3DeUID7Qgz9wDHx3FguQhoThIWwQEl8sNRJ7jdWhn2DgG37eQNpGuEZzFmKr5jVw7QPTzPq0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFVsdP9ydjeCjTyNh0Nx522gv098_WLKFhJRa92KE_7AD6m04cwz7nuMO_juUpdH83XStK_MY1EPUWve8bRUSdLALEGu990XNmVC3vKsa3HLCDpw2wjKHJAx0HuTezySu6FQTFVoH12ifklBwXxKwwTbSRGtxaCJNfspglwsqA2FfbpX0OxVcNc77xqfjtaJ4R3E6KRVneViVDoFh6HU7E5cZxkWB1BZuQQcFImdpkZvxSBhkvar7zqvVGJt3BxcRWLEjN3o4a4A2uhaMP6pmilICHB3seXRwcECttJIivKkq3GETNmETI4gBphNHu8Mggdt7Db1o6Y3GeaG6pZ7Mojg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFVsdP9ydjeCjTyNh0Nx522gv098_WLKFhJRa92KE_7AD6m04cwz7nuMO_juUpdH83XStK_MY1EPUWve8bRUSdLALEGu990XNmVC3vKsa3HLCDpw2wjKHJAx0HuTezySu6FQTFVoH12ifklBwXxKwwTbSRGtxaCJNfspglwsqA2FfbpX0OxVcNc77xqfjtaJ4R3E6KRVneViVDoFh6HU7E5cZxkWB1BZuQQcFImdpkZvxSBhkvar7zqvVGJt3BxcRWLEjN3o4a4A2uhaMP6pmilICHB3seXRwcECttJIivKkq3GETNmETI4gBphNHu8Mggdt7Db1o6Y3GeaG6pZ7Mojg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOoXIKHVG_qepq9dxAq8fWGDdysmq6Tss08JlwlAb6ZDMOGywxBo9uMNpx0_1E4DGz6WRXjpjibbT8r7Wi0bLL1SlVQOPalnh4CxfqCwaTkoSX6NwN1VgR42Pka0y8JS7UJ5tsCMaeo0jjouZPQCxNeOgKHGvf3aWo3Z73-0YgOAqYcADeb-qEaeF3r-mdz7aMkUUzBQEi5wOma_-q2gKjiN0pZN4ZT81p52afCkSToQ0M_PuK7tALbeLCfyo2mTfiqjLkJojWbrw-CT0yJzkDRXUzG3XxJhpruwtkqvxy-zbGmrkoq3-cz-9DZc9aZXSE488CWJb6I-zGY_93ieqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGJiAhZ6e8yO71oi5xWB9wY-5dlFvGr8eLbGY1SCf3xcwJFSkRX-2qToLPpJJrhk-601SnQtp6a3QU8JaG2zvyi6OnbJe2OyRZGytDtBnn8furYMecm5TWrZqg8_l32V7ZW9XR79uvjFDPnmdyD-7azlo04LN-WxH3tmQaikJtTCLQ5Hcy6Dd_j9Fzr8qICbli4Zm2fFZ-EtI4JcmxA5iGzB94K3aXxXFqNuc2DzvQqxKazGVZidx45tmhVh0bWWackLZQtQ1bzvGjx_Cjs0S0Qj2It6xcFlN7ht93vu8GG2y4j8D0JKXNj34x_acVqgEQgOSZ_T4BlrMaHqLG-VNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ9Dh5kQizHATY6qtwSMZbPX0M4Hnc_WLpp99iviqFUZ_BsxInsKU61kYBK52m48pmE0atmk0ptsNJAfAaQbZiRV-QX0GgbXG5KZMjn0GsPZujkS6GovdeZRiBAFCXS9cmMTmpVVvRAcgSX3wBHddLraFrKcg7L8mBUcrO_bebrFOg4CVxeuVPxueGGrACji0dPsVF33m38ugKh366M-0rpgbMyO1ZuZM7ekujCR_hiFrkyqxYrlAUyXiNYckTYMsiVLVuxqhrlFvofZp61QsF5X2Zl6M2RaYpNFhSCfj3u612j62FPwoED_PWmi3eSCylLfKAqmyW-qbrZTtsuRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPjf6TG7gW0B0vyLhs3rlAnhwOnH5S-ELCTMGrmD-UtvHAWtmi-PJHiWsdsSk-vMSyWFB3x1VIAxCLcSFTNUhh-n45DqJMKGGX_ClqD1fHljQPnMb402Oonqo43HGajkXKu6Aq8eap8sT8_Bc6CJNFyWfJLzRYIGcvqFEBs2bWPEO1wxPGO1qBLGcBo3RPbCUC7vtXBlY4r9O37Zj6qOtue_WtknxtEQUgXDMO7OspZR2RNESv_C8_QBMtjzdBQPabLOpkVgPVrJxGTXQNiuEt4ejPqODdss3NrQ3Q1Dl9clG-dCCZNTn-EmL9zkEy3h5EwWnTeNYq7_k7r2_3_nvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOM8xBouQ3CFxF95tAIdeKz-UqZM-QbvZYn-sUAHPTaEvslcQ6JVLc_RvAmgkvsvLgU5RS2ToPT_vZlyipWIj1unYbrTUDZLdq_M22xhXW67dVzMBZ_k8-oQhwmAPRXawEXvllM2hdpnPUoF-Wlngt8nIcLvyl9eXTUf_F0FtRMhM3nI5xZ3XvSXmkXbl90FPpExnTUFmYDY1Ku45AWWYxVnMJX5vk690-aFpw20RJBFAvSeJfnUOn_Ws_u5lNd4oz9XAABVU-GI_GbhU1zLSyp7UHdAIaEMj2bcymHvdXin_sPGiOiEytJekOSwVglLOpG6KWGq1CgZMU1KzXqhpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhPq1BZWuSu90ahfSsNX7xJuJTwd2WqxrU2SXznGKli1Hez34b-00CalDqfRmthp7PZBmnNV1ePP5Z1YcZsV8U5OF9yeyBwCFHzA4ykDqvzJ2YcfYxscyoX-pxNzTcce7AKfye8zZVahkQoMrnn9bdPKhMh6vNDzEFDS8MjkK0leepwRw1-baEJJi6vekLbxCoc0Zmg84CRUw_Xd5oeySsBljLuURMtk90Rw-EbvhmmQmibHmZ8xnVSl4N1beBTHPb1APajtejSQGMwTWarwg67Vui6hd6mnazUqz9CSbM_-lz17hOQxGTz5G8Bj_BGeJrLds2WxQIbhsr8WrWL3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpnyK9GrOXsXMMeyz9WXwpiWldHjdzIv259jjoWgxm1nYb8SEXJO1_n0VrhdhAcM4KNVMHNlB3OBG2hGcxfvazf14bW6zwlQ3B0a70FsurmgVk-XPUnxoy-rDhUbZkfGsni5gHKpM7DZihjDmvnFdMT8qhTrCQ0RIik5vyofIOyOsLiYC0ZY2OUNlODHMjuO6AC-5swrtLWu6SgcsyZyegDwke6SwAmGaimC1cH8WhH7WXJkWvlqAUi4TXyHrJPSwjZA33YGuD21HHBR_vmfzmZjM2Spbsjv3CRt1OfPoun-opnjKWdC2xrJwWwHpd_XousuPYZBSkOtdg6QTkzcqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cKhOdQ4fuk53vDrZwATGQjul4xawLceyBWnfII6WU5TdYkt8nhcRuvrdg9P4X-SSj8uAjdP4od7abYvP60NsynT_jFgfidvFrtwBBH8pGVJw6cXWnkz0HfhjDKuNz94fHRjABE9cOxDkweOFP8bzpjYHWD95h5fT-EddYgqZLD-3sp2_1GyOg_qf4SNNYxI1rwqYGjaZVmNjqgtO4J9meI2y1pG3QkoRCHhrQEOmRvi88eHupVuCPNkI4NWGKzKxzb3NvzbfPQmtgrHK37QYCD3U3U81fd_UPQaeMzaGoYOlIsu0xdv4VAJskl5zN6qggX7KjrYgUrEydbv81J3HNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qc-7T8DMNVzflDsXRtbTitBPCW34S6mLor4Ns8GAv4m48Ozf-gurUR6lpOGZeX7Tgw3KUTu5_9b0yY_Ys454TFCnODlywP1ws8_wkIg0n8mAw9R-36oZHZplVHqkFpLjtzSowxaA2SEoC2wWeGKlgs8hCMLdtpzJ1FY8hO8WduiW8ivPX_AdLlFp4_M_X0Ex0bk3bkkruNsCSHAFC8nU29hqJ9ES73du73-ajw4JcHyKuWhC1rWAXTnzAx6zIJvsDN-qUavLbYvwxnFnkZa6qxxHzVOjQnp0TPNMz1hoS4yXX4isjQS5ik7GLY_tL6la4ZGs9xDrfP_LasNj649R2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXgSBkV35LHNuWo6WNJIZ5QM-quPIzR2elUDPIx8NM-bcp06rQUucuoUAt97ynt0-gh70jGqdP0MIS8gd5EztQGAxDThjos9eD-Dp9xcZh-EgUrJiDjB_y3MjRSQRhT8ShB4XoaWYvsVfYjNNwzd9CnZeu1dbV9TQUdTbsVGIPy1oTP38PTe38ky-WusZDf7dqIuKwW9rGwV-qShAp9AMLHcfi6rxLI8kaPk2fv1j4KbMj8Te5gbTZ3HoMi_BtzUSDf6Cp051BKbQhNKd3_uhdKy9pPzVWvoTQA5DecAAzG4uJaUraX3owAHIveBC6Fs5Ck__u__dJ0Bo9hvG8nesQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=XqJnupwB9Ki0ZB17VjpnI0pe3xjY_UQJrORUW8BCXF16tVoGQmZOHFAnzfa-2IWTE0DqEBM4aOR3rvZMt-WkqZmsnxFYATXHYBN_VOOT-N--JqA1t8PigvCB0RNDIsh7AgGJgMo9hJSjT_IQSvUkfVKKYXqouxMgYwEOp-93cCxi9BNzEWg2poRSCLuRS3kgIIXupNsuuwt-oqDnCkUmk85YuaiUFymZo87vjuljTIiUGsyRN-jgVwsKzbilopbNJNycELJukx2j5hhzNjGTk3F9CJqxhaYU5W9aAewJl_nHugxO5b_qWVReMffJOcA5QZ4EDViGlUflgB0837c91A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=XqJnupwB9Ki0ZB17VjpnI0pe3xjY_UQJrORUW8BCXF16tVoGQmZOHFAnzfa-2IWTE0DqEBM4aOR3rvZMt-WkqZmsnxFYATXHYBN_VOOT-N--JqA1t8PigvCB0RNDIsh7AgGJgMo9hJSjT_IQSvUkfVKKYXqouxMgYwEOp-93cCxi9BNzEWg2poRSCLuRS3kgIIXupNsuuwt-oqDnCkUmk85YuaiUFymZo87vjuljTIiUGsyRN-jgVwsKzbilopbNJNycELJukx2j5hhzNjGTk3F9CJqxhaYU5W9aAewJl_nHugxO5b_qWVReMffJOcA5QZ4EDViGlUflgB0837c91A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoQICzmK3ZDodbvKxzlteaMmAXnnH2ggvapn0ENQGO3hYCw3jNgB1Qcl98haw78UYbNUNbhAsyEvjjAHPzK3tMRWfsqfsta9y1doW6D0GL7z6VxtG-oBpZ_ROWjOQIWvg3nBJk2BVt9YXJDyPLH0fKh2Zz1QN9WkVq_3OP2Hn82yEdD3aSGZMjsIJ4MqlZ8rxiuK0btj959itsSSNyArbvlhRnt4ikbLlkY06YgBPppPM1_f8Wdy_VaMiWl6wa8HSdeZXuwu2x12kqj-2DH3O7_k9jbEorho-afsxU44OdUFJ4ANJWR7k3NnmL34WmAsm48iWji1bSt2zj4rMo1keA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
