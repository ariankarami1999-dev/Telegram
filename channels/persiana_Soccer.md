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
<img src="https://cdn4.telesco.pe/file/Lsv8vrJmWs7dCo4aRLyxfGyVD5RW8iMEp4i_borQ2Ow2SZBPiVGjf1v7ohb_dH81uHeMt0nH5ED9BoHADVlz68eo6Zdn5-sTrmRgUZ5qwQSn8iN5Qo0rxCaVYWC2Ass1mlWo1wAV_on2AE9gpmdl0KhtnjZQZBQUeKOSSTfAk_cTenZLT-Lu7BwfLxYO_heU9D0s6xt_EGcVSTuZIdWJyxhpSuLZrMFB1_bSpQBf5sMeODEfQCoKW7OphKUkzuy4kyCL58NJAonai93wkfIp1RAayTmb-3re09CV3uprefRQHlI2ZP-yJONn1KZdkmJXSXM0NK6EXKWhuXBFJajCqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 00:18:01</div>
<hr>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYSxX4nUlH4JvAKib2UZ0r3PXf2ajZmmCPG_GUZk_2BOOdnIpvb4835WnJcM5q-y1OzjQVlQ5CSWpkWJtULUwn9Xscmn-2RGOWz_BYRERfVH8F1zNFt6ofhHPZCW669Fwdwuk2TaO5JW1e_Z4ohqu_8sc7ZpWrfGqP5CRvnBcK5eVnpG6E0HQNh3DPaKIb5hr9I5XiDo3y-sYvcOb1dai_hk2dubO0n-XEFMFJQuukvkO6HiXc08JAuEkn-Pvopz-fWRNDfpS5wiXeQgw21LfEwS8t7OkQpf5nTapC3gMqo2RLE_DEb_W9GgWfnGdL6ASfhJ_88F5nT07XtZVCXevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ5DYk-uCAp-xJJsR0ovcPvA3hXBBazUe-kVdIDMjHZNe5R2bxZHBvvZeowQo2qyAntr8w4Be1ztOQj2ifxoJ9EWcQmok714VkAaSrsmcW1VcXDWhzKZ-9KhX2JUCfUEt9RktcCSj20fa6k7MtLhOnEvpNlOwNmBZwBI3_iB0YQ7AE42_wA03pyn_LfE3OEOFoWPbobmv2czQ058MuEvsabPInsIZZtfvQfsMPegOgkNwKpOGZAwST7IOPTwyzEd69sJv8ZFwvCmGidJZMQhfnX-3l4k039mU2kyGYkWPyjx_ZqVn7mI0NVdyA7ckUhJOxzxFmF1xn0HM8uUHvIsqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=nrctwEdoF1iNq670drOZ9L1YMie2qih-ZH6lhHr5TwVZguTwhIV9ajhMAwM8RxFBNUxBcK4Du2hMbjdn_31iHRLCH0oX5UyubZauUW2dS5pVTtpYBgNaiTJkZoWERhhxFdAHoiMtG4Wr1PNLLUJnK8j7kz7jjcAvvb1kNy6MGrBo1t4VDx9bhbJugdEtXGnOlnQdgKDcfCBrmkCS6wCg5gjb7jvRktaAwCs3dGNNVUR-w4sKB14u_d2HvUPRmJxWuWZCA0PZBzyk7__RfjRfoBX-gmSjpkJ5uOofKql8cQnuSojQOuX-oUtAixMpauT2TmQxxLA_ZzDJ9AAYqXCNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=nrctwEdoF1iNq670drOZ9L1YMie2qih-ZH6lhHr5TwVZguTwhIV9ajhMAwM8RxFBNUxBcK4Du2hMbjdn_31iHRLCH0oX5UyubZauUW2dS5pVTtpYBgNaiTJkZoWERhhxFdAHoiMtG4Wr1PNLLUJnK8j7kz7jjcAvvb1kNy6MGrBo1t4VDx9bhbJugdEtXGnOlnQdgKDcfCBrmkCS6wCg5gjb7jvRktaAwCs3dGNNVUR-w4sKB14u_d2HvUPRmJxWuWZCA0PZBzyk7__RfjRfoBX-gmSjpkJ5uOofKql8cQnuSojQOuX-oUtAixMpauT2TmQxxLA_ZzDJ9AAYqXCNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=iZUYuSwWDO4PIBInTdjRW1zjtNdxgsmKqzl6y7yUgomMnG3fpnQLbdWiLjya5wdXkZe4pFHGpfEi_V12TObapxs2Km-iJ1UOQ9Rlhiaoc-I1EYWvOkN4h9uai756WkpynBqz7mtadXHgaNDBXUeIfGCImxlkoMg7_pzIasD56VRHmKTXiJj_0c_Bz1SXGGZg3l0VPezeBsFtrP8aVtmRjxFFwrNYfcMgwgNX96_p4QrLTSyN2EsICDVIP63x4vkjkTa3fQfc6ntcHFFcVF-9SbnN_kNDpPRNjDvefR3I9eWI0dXNVPemMS3b6F5XK5t4OrFH-8AvD7fONjHvu4HHgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=iZUYuSwWDO4PIBInTdjRW1zjtNdxgsmKqzl6y7yUgomMnG3fpnQLbdWiLjya5wdXkZe4pFHGpfEi_V12TObapxs2Km-iJ1UOQ9Rlhiaoc-I1EYWvOkN4h9uai756WkpynBqz7mtadXHgaNDBXUeIfGCImxlkoMg7_pzIasD56VRHmKTXiJj_0c_Bz1SXGGZg3l0VPezeBsFtrP8aVtmRjxFFwrNYfcMgwgNX96_p4QrLTSyN2EsICDVIP63x4vkjkTa3fQfc6ntcHFFcVF-9SbnN_kNDpPRNjDvefR3I9eWI0dXNVPemMS3b6F5XK5t4OrFH-8AvD7fONjHvu4HHgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtRGVTCm9ikfXxsX-nEz24lpe77p3xU8pXKPLMKaR_JJTSq51anmVc5en0wnFxh3dVEm4HGG2fACh2m_iGKFTd_DB2oU92TRzhl_7ZwU0r6GU71JTcgO3cO825yiIb8BMugMsnaW4gFHKI1cxPkNv24nL56Ac1nC8zbL2BdezZI62C5Q01wZrlKsXMw5aG8ExcIOvBZaUCUbmx7FkjnbN5gnE7OKF5dLmYMLjDAACTxjMbxe24ALgBcEzt2bck2wl_ySnwWx1JzuXQWm_YSvxRGV7ZCzaimn3nzsFsidhbmxha1nyYRcQuSaqS6j_5jNuefAeh6xfNvEK0dqW_5ceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=ufkxQoD4N6DweIQby-Ajo0Zv4SjLytIN9yP5isw1_v2ZwCIOm6dJ2Pu-qZFQJqSE5ml2G9WHTFutgZGpOrZJNOmcDk7L9YFn2MJSm-JpSiA8QSUaF-r5LGbr40xQmBZYob_6lLKZ46HoibUFFGY8gH8wbVhtfPmmabLvHc1hRmfeN8cshm9EBtxdf_8pBQsZdiJDBX77nddIeC6auZPmwcBvpz4WfOmKXxoyttN-jLOjxdcIoJcPI2eFOo_gKOBpQOMe1yPQMD252OzzNv9m5phMO3Ko1ZdcUrgVnwcdpEtUe6wSdzxcCdXdDbvdRUSQjUJR9m6NiLRk7pYxmHnpfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=ufkxQoD4N6DweIQby-Ajo0Zv4SjLytIN9yP5isw1_v2ZwCIOm6dJ2Pu-qZFQJqSE5ml2G9WHTFutgZGpOrZJNOmcDk7L9YFn2MJSm-JpSiA8QSUaF-r5LGbr40xQmBZYob_6lLKZ46HoibUFFGY8gH8wbVhtfPmmabLvHc1hRmfeN8cshm9EBtxdf_8pBQsZdiJDBX77nddIeC6auZPmwcBvpz4WfOmKXxoyttN-jLOjxdcIoJcPI2eFOo_gKOBpQOMe1yPQMD252OzzNv9m5phMO3Ko1ZdcUrgVnwcdpEtUe6wSdzxcCdXdDbvdRUSQjUJR9m6NiLRk7pYxmHnpfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=YiPx2i_EsV2LYhIGb2SMc5c9GM9l-nEm2rfVCujbJewgwlNwhBbgcaMM0dlIBxEdjv4JHs-76u3j9FU9xJx6HNwgbMS9tx77Yg4OWDUy1nAxU0Tpt1rhH0GuwyOV5DXdxioZ49gXpc5eFszWOAd6XKitDGYt2IUGxvS3WC_w5ysNkNuIJJoVqv9lLWcM8N-lz0-RZ8w-9iN_xzrKmS4lnZS9bSRooKcQ5_9dRhwCKNJmNC2LxSWPLUPQEuFTfhJzxcmvtSD4BxaWP52C-8SdnhSJCzUiWhOonsrym2POEcunFyotgtR-2ooR7hJCxR8KOCEymNEeJ7H9PzFQfW-OwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=YiPx2i_EsV2LYhIGb2SMc5c9GM9l-nEm2rfVCujbJewgwlNwhBbgcaMM0dlIBxEdjv4JHs-76u3j9FU9xJx6HNwgbMS9tx77Yg4OWDUy1nAxU0Tpt1rhH0GuwyOV5DXdxioZ49gXpc5eFszWOAd6XKitDGYt2IUGxvS3WC_w5ysNkNuIJJoVqv9lLWcM8N-lz0-RZ8w-9iN_xzrKmS4lnZS9bSRooKcQ5_9dRhwCKNJmNC2LxSWPLUPQEuFTfhJzxcmvtSD4BxaWP52C-8SdnhSJCzUiWhOonsrym2POEcunFyotgtR-2ooR7hJCxR8KOCEymNEeJ7H9PzFQfW-OwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=vsEZ5JJxbjesoFIKxjzJm-j4oX9WGSUCLuwYuld89og4dpq3uX_G_Wjy3Th6ZzMgcOv0gwyJSmEsQanlSkCJVVKd64uhPoEbzJ7H3ECMWnWksnlUwhfiTtXmPbdcn3qpPn68JZQLwmfUJMLrEddL7LkpsQVGxUgGhFsPgMH1vF9ovIrv6d780UXfjk6L2JV9_Cyry6AELyVoN3uf8oABZ_5ou0-IWRVBtoUHrin6e78VnUGKoVNsjS_eyaynNNF1_3LvSeLWPA2FU5uhwffsf4J9JQ-6fYBxu2tZhWE02xFNCmHoGGthS85SzWuS3Y80S0FbEGTCdHarG5Dg-ABH516onWNlqaRPDlWwbLktUxfvZgkvYEXHDHPom6AYMvhd4DMIUfIGsvBx3MG1Rswv30xMOj8rtdPF0kWpcWpxFwq2-0FrkxVZDZoO_XM7t5Ik8ms4JK9APfwhpGSp3tkgd8nBM3m4oqDsPqRq7C9VFfn81lVPyloUwKbpm3b9SHARWVMpQ_LDH_Pu5rJIfhTXvKDnSliAFlJCbdlhW2OL2oF-5NZtkFe54ynfoo1-_2XLzPYLPKcyCwYdthSdDNSDMwelw259U94CQM4nnvzVehtiN9j0x8DTLZ94jIufkm1VPaU3MSInj1EfCVQFdYjMU1atMy4xxLA0qf-1ebsy04I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=vsEZ5JJxbjesoFIKxjzJm-j4oX9WGSUCLuwYuld89og4dpq3uX_G_Wjy3Th6ZzMgcOv0gwyJSmEsQanlSkCJVVKd64uhPoEbzJ7H3ECMWnWksnlUwhfiTtXmPbdcn3qpPn68JZQLwmfUJMLrEddL7LkpsQVGxUgGhFsPgMH1vF9ovIrv6d780UXfjk6L2JV9_Cyry6AELyVoN3uf8oABZ_5ou0-IWRVBtoUHrin6e78VnUGKoVNsjS_eyaynNNF1_3LvSeLWPA2FU5uhwffsf4J9JQ-6fYBxu2tZhWE02xFNCmHoGGthS85SzWuS3Y80S0FbEGTCdHarG5Dg-ABH516onWNlqaRPDlWwbLktUxfvZgkvYEXHDHPom6AYMvhd4DMIUfIGsvBx3MG1Rswv30xMOj8rtdPF0kWpcWpxFwq2-0FrkxVZDZoO_XM7t5Ik8ms4JK9APfwhpGSp3tkgd8nBM3m4oqDsPqRq7C9VFfn81lVPyloUwKbpm3b9SHARWVMpQ_LDH_Pu5rJIfhTXvKDnSliAFlJCbdlhW2OL2oF-5NZtkFe54ynfoo1-_2XLzPYLPKcyCwYdthSdDNSDMwelw259U94CQM4nnvzVehtiN9j0x8DTLZ94jIufkm1VPaU3MSInj1EfCVQFdYjMU1atMy4xxLA0qf-1ebsy04I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgNy45Dj87-erwcvj6Y-T5cWk31eheNP_b2YqseHYm9ujbT2vCDw33I5d1PvGT4uCiVNbdOQ9j3O6jKgdTSyj9Hmyrw36muEbhiFOdSDZzJSXBMsT_CRJlKIFNEpQ6ufAoSMQS91Amle5X3viZTXuPD3GgGFgaF9akk8Clr0-nVb9UkkacvkuqjfOjZ3o7UIKLi6xs_m-KmK-jHXVr9pouSGq4KTZeakWY77I0EbbotTiLdRgDQgQNw1g-giFfdZ5YOE6ugV3oE40sd2A8d73l8qbcg67CSKYh1fanSbnvRb8DwP3X-IHKYad1qIJHBOy5S_amA8EN3X5NsdU2rt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W67U8lsoLHPmnGnEqAIWpBGKaOHs-NhndjnPDyrnw3e8yhhYMdcyAWrrpW62aGFVnP8MGEFrHIA4JK_EtRP0VTV788eH_NCciCjf2XHSlQfJaj0FgB83DHgQAi9j9SbHnr3_60fgUPv1bAYlrbigaSYiV_OtMdM_1912iwm4_kR1A-NxZqW0uCWu_l71QjjrqEg4qilwVOpDBMg8by8B-_h0MOYeR4VyYWtB8sz43H_Eu9jBITaQdJNG9RzCmO-WqtB-MkwNPeJBhJLLE4ZHTiI0ZtadYB-YnVD8nAwlr9MrW--fCGOEYK2gEV3zDc7gi3sTzFC35_X7YRtT010gQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=HqsSD4RTQO2D2XkzRtmc2FIDXqot6JVq9qW2bb_u9l6cF4mhQRqspI991hRinKV77Gxji2UrF4XABa9spcfh8zXQnUVpsq7p95027GwHuKnvay6ziSabPE8eKBegKDI5tLabMwPwG2njpxsyW82zywH0MpCMwRup32T9TsuG_BUgPoDpfkj8lAwpQvY-q_BoBHP79BKBSGk86TIWbu9SVX2SPTaxxL9PebMVy_NoCcIWC2zrv_MCLk2pjt693WB_NdSCpkEULgfG-9WAQ8VoOaUiyYUvbp0Bql31xgW3jNN7AP646dTmj4LHWLGERXBFqMA0rOIH4Ti2Y8M3oCZqBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=HqsSD4RTQO2D2XkzRtmc2FIDXqot6JVq9qW2bb_u9l6cF4mhQRqspI991hRinKV77Gxji2UrF4XABa9spcfh8zXQnUVpsq7p95027GwHuKnvay6ziSabPE8eKBegKDI5tLabMwPwG2njpxsyW82zywH0MpCMwRup32T9TsuG_BUgPoDpfkj8lAwpQvY-q_BoBHP79BKBSGk86TIWbu9SVX2SPTaxxL9PebMVy_NoCcIWC2zrv_MCLk2pjt693WB_NdSCpkEULgfG-9WAQ8VoOaUiyYUvbp0Bql31xgW3jNN7AP646dTmj4LHWLGERXBFqMA0rOIH4Ti2Y8M3oCZqBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9U_06HzaKfbF-jPj1fOEKxIuXGivRBEYRVVMg4ugNSmp-0ba9hVOw0Ze9l0yYmL_io5h9xSYmsD8hjQWZ61LKkX_yjNA28WSCZuab9y3nxT6AKFbqOiTpxRLh_DZhCIemIExqGmh5q1o8s0Wokiak9ETxH8eamuugEw-LXCwpBndY-bQuc57KgcWwoC2o8WQXjg1Zui_06cmN9R9yva7xYrTQTsJl1fPAtHXECoLQrpqNnxeaBi-XWyofUzBXo8Ocj37pO6Nf86jTH4UoEo5vw3TVIInpqT1rfd0btdEL0ZLxksO7HkHQvJdOuZIriNPducqvYDFA-yGWKX6-1zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BatfYXnhMi-JPzR743Hxk4PHT92oglrP_CCHJHIU0R0LNfE2XxuEwAVGdel6I3BhMreZKH9V-4StnbXkZdI2NwwZ4hatadMmbHHCt_qBTRbRq6yLU08PKxqzcMpQx7QxRcFO1drNugMGPRd1x6bPh-Ntm9tzsKVQKIKhWVT9xC7NNFwol-ZFj5GUiRx3vv3OpxcRHghQT2b0ajWJ9cPWPmg_ndTWrJt3lo74Ew-Zmo33vM79udINJXOXW4SKsXyb5S_nPsaph92T0WGuZIYmDcR7dpQ80KCca4Z9Zb6mpl75o4w_gLEN__AYvVLdlZb8xRcqRkQdyhNIsjhvUiOgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1CxXafY90W-N-U6R5jwd5-Q0irGmLPceZHsQ9QAVMlPyO9xFRaLc6hizP9qzyn4h47StXYqi2k88EcVQvLlr2jowYuu0XeWcXwjGrwu0MzXZD6Ynvz1DG_HsDEG0prjvxD71OPwht5HQ8vTipTfIPrLdLkQd4-a1co6aguJ4W6a5Cpq_TEm-SyYYPZqSXBMr1WZdYhMlBK4eRDllMunCTfsV4mzXDEmrX0846dgkF_7U3Z793yuNnIFhLFuYltRqY3DTZ1B3POoVXuZnm2jgIBA-SLHwn9tAef_mitosLejyoPA7Nkpd5jZqafpJtAigxJRgjqWRkbPCC9eYCLiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=VeDfgVLQwMNzSbSSa2lUPwsEW_eHGhpERZDCfr7Kh1HD5C2IplZ6Acd941eMlu1v52ZA2LY6NpHUW_q1IJ1We3hv8b4f5xzPJAAYmHCjzlvtY7wAfWt3bCy_e6ISeCmb3w1A0I-EmHetimONr_98u6jZECm1xoyL1IirvpHuXXQZdsjo5UQ2hWFoDj52NECTyFDEV7MaES7IGZgpuzjWPj3_jFs9vYcWH7JESwjPkVDtV5Qv-8ohogJWusELGGKuEXRwOQaLDZkz2E3q6deEd3Lz9_IcmXzoITr3X2iJAJK_fsdEZZcx_SEBeHcz8tUFQP3QOq4f-UhVpvGAFwUP1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=VeDfgVLQwMNzSbSSa2lUPwsEW_eHGhpERZDCfr7Kh1HD5C2IplZ6Acd941eMlu1v52ZA2LY6NpHUW_q1IJ1We3hv8b4f5xzPJAAYmHCjzlvtY7wAfWt3bCy_e6ISeCmb3w1A0I-EmHetimONr_98u6jZECm1xoyL1IirvpHuXXQZdsjo5UQ2hWFoDj52NECTyFDEV7MaES7IGZgpuzjWPj3_jFs9vYcWH7JESwjPkVDtV5Qv-8ohogJWusELGGKuEXRwOQaLDZkz2E3q6deEd3Lz9_IcmXzoITr3X2iJAJK_fsdEZZcx_SEBeHcz8tUFQP3QOq4f-UhVpvGAFwUP1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_3AKvuSEttRpiW6ILxrhbz_tRQTdoAxFgqq9YUQh2_a3g_Uw8jHR2eKzbdpLgMFqp4cMJ4gg7kaNDWip3KEu31CN3Szgx_FOdBDauF4R4Man1FHlSWZbd5Jf4CqivvimKc-Cs71xqg1G1PxwCEEgMXn47BltbV-KOj1gmSVfikSdgIJGJQOX7zTTNqzIbek29XZ4RDT_LcT2DY4yAMuduxukM-0zU9T4vFfa9G5ezK2J5KBfEEGzDIc3ByXlG0FKcfjJTRSnno6FSj0DRQzl0vR_YDSjdeV8CqNkpGooEZiH1jSmylv21H1D5OWAXncyjjb5CU_JNHrz0rbiFY0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22834">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYQR5m36ZCyUzi1CZ-jr3PnJvIxuj2IBbkZkFeL7tEGekPECUxNmXAJLvV1QlX0ZVPgSNKjibqx3Lx2PjUN7xWxsxDZEAfCRsDpK3IsBKR2Uk4xjy1ymckdlU8rEbPcrcubRsQ6oldmYsf4i2Hv6XKPf17V0nIQESDXn4830WWpqVssyWnHqBN_2LMcYxJXtTVgNmoR02HZpmLs5cru6aTJu6hDHSNbgXQo_RcogoIluVmyROhG3Op0t58BuQ2p2tacArh8Fp0KiD4q7cGe4cZqpq54l7YEl84hSl2YciIhAQl08qmvBdRYhLuqW1DKe9R6oOptT0qYzDUxvYdP7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
15
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22834" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijoAa2n8dEFS2RLO7ClDU_n-ozNwtNhM6f4L1BYpey50RqkbztEmdiPGbt00sk4FELiJsD9WL5IJ8Mn2ijxXVTFZ6-ysdjIU8ckDY5f59dsy-l3ZmQ5NdMC6ppV96delNrZIiqCmkIW4l9xBcQm8X2JHyCzzhS6jMcytuLrWS3f7OacpcAxhuvCrmhViynqjZOzw2Oxg_SdpUsmSQ69N4ZEqQCRmcHdENzw-fO_JWYuPqwq1IvPxOy2_REvVz9lsstoJMr15z7ff2f_GxdaKjUEhswE_APDPMCpbd-WIZXjcfcDrqK-V-1DiyyO_F4jINXdAVodXTPzNj1XXAmDjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE3hFsPmyGp-nfrFVHJ8n1rHIqo6g5bq6nC_fGqJPWcdhpFIlN_ZBrO9aDB9ufAAAIlzS2U52y8DgIcftcxYn4UWB-qFg_231dj1wKNo7D-L4Rtd03nysVukYq9Thg2oVVJmiqzvyY_l0RPXI6uqP-YrkwkzZ1gTuqiBPoGjlm547Nju3Cc7gBzvH5xJBetNWN7qS5ufSM_kcl9cL6-yr8eDwbGpFiSKCZo19BFx-L3SNFIpJyrd4g5NuyZIhcyUsPlpy-HwQTqemTPiKc2ZPhclnztLyCNuZXQFGsygy5XlbZ0GtcsUsrgSG7i8RqSCV8OnKCx6YgePPpWfjm0xGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG9Wd7ulGCBm7wIvWZkHPQabOhkIizA7TfoSZatjXW2IV8C9x-941WKFTUldX-lDBwrP9XTXrTus3XdGIPnkEgx3YYtUXpnq3BIbHdwa-BKUOUTOtEzuBcr6pZGmLJAsJ7u1vz1xbbCzlnpOKvw5ZfT5zYVR_3Wl1XXlFennYza-dfbXQdmutKT_Jai5XRhA7LzZYM0tOzbl-kX3UH_xjJJuiB1ijZiIZrRMCWoIpexvWGEcnClAhw2eGUqsPZ96nvQ3UXxgeTdzQKsdTGlV1FGJK-YjvIkP2n2wkoT4LsMcYoWIPSLKgwEPXdLLyM_1dTRgy3ZFVNOcbizFSRfliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNxtcBYlq-ELsdT731GzdXyPSIZe8Sc1CToVICoc9RDusXKIR-LDgV6OAm_ZBTnJQuGgKynmh9zg7gd8vie9ZdzzMN--wuIpMvNwA9LHTWoQCFsD0Rxw_pRa3WJV8cvuQvRqGE1Vl46IhQunyAh8Va-YExS80aVUwY_Fkk67LiKQwHOJE_0QVlrGwan7aWji572uIUMthCg4mvD6_RhPvyNY50nmv1jbF-tQYnxarLXyI9Xq9OGyEQaObeljgkZ4qDtC7Zzn8IertpuxCwsEp8F6lWkbg8zHHP4-HRIQ1AGcwM3DdnT4ZLJJBqPfGXxELo-1IMqXI6TQl88wXyNfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=UnB11S1O74pUpV2B_0zqC3MS2DqBt24wWSy9KgbVBMJxz11eNIpMrjGldFGUn3QQ3q8HtWe3ozaOnC-6f_9peQ2ptSdE5HWW6HXi06dTrvBRwr1yBMoHbWFTWrql4_GXhcm-d94jHBs8jCl6XSjqMpxuYvi9UKDSpGAu22G7xxlvlKjuf1AvuIW3xQM9ly0gzyi7TbMAGNHl87WjQC1x89L82ywzZbsnt4ef8s957Ml_tBFYfCgOy-ifxZ-7GW1Onwr9JE6M8rpRODLTW1vJOSSl6eGVPHzN4wNmto5vuRQY9ccipiDuTlThZP8TwmyJeSVAyZVcuGAVuhrJQ_drNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=UnB11S1O74pUpV2B_0zqC3MS2DqBt24wWSy9KgbVBMJxz11eNIpMrjGldFGUn3QQ3q8HtWe3ozaOnC-6f_9peQ2ptSdE5HWW6HXi06dTrvBRwr1yBMoHbWFTWrql4_GXhcm-d94jHBs8jCl6XSjqMpxuYvi9UKDSpGAu22G7xxlvlKjuf1AvuIW3xQM9ly0gzyi7TbMAGNHl87WjQC1x89L82ywzZbsnt4ef8s957Ml_tBFYfCgOy-ifxZ-7GW1Onwr9JE6M8rpRODLTW1vJOSSl6eGVPHzN4wNmto5vuRQY9ccipiDuTlThZP8TwmyJeSVAyZVcuGAVuhrJQ_drNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6qkZaSKlI38vCC_C0TKps5yb5OqgxMFAuoSKzRXm2BUVE5r9GBuxMV9zv28wyHIqFQqLc85dgwjQa-7jtlJLHExiAg9KuDeCbY8J0GXWoooNIpcR3yNYT6fqB0I7DiSa-0g1e4-cznephyYGYwwOSbPqpdn9o2EDHYw_sRN-eqDi0DfKMDIpADcO9rUa75DTveIMnz1JEEbBppsRPyOPqLYdEiWPAUdfCA_SwB_vLpxo01f2hG2Y__sSYDivhkrBb3lvHEqVfSb3NR40wSoJ7cshi5aVUc_kp_qoNUdU9jkPjQY320yQPSkY2qo6EQMBF-kOveOmgyF4Q1B9JPd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBQoog96Hjsl6IhJqKM6bQ2Mw_zS_R9KeNpr4bMokawatBgHNaCBQ4Wnnloo5-9tgmBGQ_w32Ihw6RawqCCrqGPOy3l9D9mxyG5DWugo804FsiyaHcqa01Wa-dDjV-y1rEoUmM5bZHpz0avaPZWeYLmQdgC4hX0IrWj-vddptnUNg8DO3EJD3Ij8aX-MkKhxa4WpA--03I4080irtaSEdae_VlC7udZflu0vspqvx3Se6lIPzqRya2I0IfiLxVNGVINKlGBdRhdc55d7BSylyswEyA9qm7Mzbq79JD5q87T3BdQKTwDm3nEUve3wtIi2IhnEo2rLR-ru_FfvAcugzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=htUPydZgqIWRGPjZ6nxdobKDqvrb-lQjjGuzPn326kwkxLgRAPsYLYOF-RCV949L9KMGgVmDq49h89cxgID2lP7ladb2ePqpSL514bdGJk1l2wzH5joGZS4xCoGPmbrT6IL7Bfmict1QO7xwVJRsHs0um8dvJ8wh8xmbYYPmUcAcND-JWuCDpXHE8SC07qm9z6hkhze9CWY-ggBUujWH4xGGs2iqzRrNnd1JMBuKtfJx7P7mvvZAcJ8rxGEXwaPjBl9owsaCtBIzTKdPol3_CmH4XIhWtxVR9fV0xjKti13-msp0QhUUcolD4lxi8LuivcVK-dz17Z_FuD71ot9zQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=htUPydZgqIWRGPjZ6nxdobKDqvrb-lQjjGuzPn326kwkxLgRAPsYLYOF-RCV949L9KMGgVmDq49h89cxgID2lP7ladb2ePqpSL514bdGJk1l2wzH5joGZS4xCoGPmbrT6IL7Bfmict1QO7xwVJRsHs0um8dvJ8wh8xmbYYPmUcAcND-JWuCDpXHE8SC07qm9z6hkhze9CWY-ggBUujWH4xGGs2iqzRrNnd1JMBuKtfJx7P7mvvZAcJ8rxGEXwaPjBl9owsaCtBIzTKdPol3_CmH4XIhWtxVR9fV0xjKti13-msp0QhUUcolD4lxi8LuivcVK-dz17Z_FuD71ot9zQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLkW_Ku4GGJRCN8ObjzFcJagdBOycFc8s-RPilrEotu-sInHI4CBH98gIQ42lEDO3mFJ1fvqx8s3dUE11yxzfWXfEIQjJj3vpQZKl2-aKLujT7mBf6k074-gVpsPPbUVg84XY__8X0I3UlJhTx8vV1TzjtCdCQCv8cXUBubB-Hz6Coa8NbOtjXOwDg3recsVkiFNoUT9-zZfki72Ssnl2wMuAHEQ-VbYvzH6euc6zNwTwiCLluTMCNhlfuMgW2ox-oQN4NmMzWZGfRaW1aWKGG4YUvzhO2sxw1PGkpP_FXzZK4J46GceGWAXbNyvaXpQc6dZauNJkf3MjJDZw9wlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJRtOujKaTdblfk5MxHvDq6LDCf6ef3JRn1cpbqbcFqvqMldpF_4h7qOrmLEM3vQsILTPkHWFMfgrJewYdUtOI2qWCodD9V13ic_jRfRyVNdcQKUcWM1YwnBOQYnF9hUxk3JDqKGSv_9mUUHmghPUSdv_5LSpyy3YlxzGMc8gYUKDThY6nA0xWo4GKRDZnxDyMKy3DV-tEuzpwpuIKMxZWBR-jjz3CKxE1RvvQG8O_IL1BcQz-BO8T1XzhrXpZo6jxDVKiqnjqsoKauILoMfftv1Rhht27Xoyj1rMAYhpQdf7qdtag8iW5pa2lkCwB6LORWuOa3RDnQtpyh9Vd4lWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLLoiDPFhmBndP-w5RcEz9OYCi8MGmTCSDQfOhDqs0dbvcsDN3HBTCCNbmwiXoPmnKDERp7Ql2kejJYKEzJxPTqaQ6aA3ORJHbzT3t4Z_f3-LZjNHzTI0u2lvmGn7TB8KnzJIeRCthG3mo44gp5t-FH-cbVXplFLbtTMMiaDHTeNZT77kJnsUmLqBvNSuWXXJIenpT2FQjYiaKITT0MP5tktqYj_he9TJXq348anOpKwimRAJ35SwAMEa9hfNFJI_2NdxhvNpuKILYXRk2y97LiQf0RizE3N6xYmv3qQZsYsn7kbpliPnG1nIQUTmQaBbvukGO_ro-q9a1D6O2QYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhfnuCRRQ77RPy6tfSIUYfJpl-2YTR6GobRHB_PCBM-c1SuKmQNsYcFahpGl7QiLdKqwBqPpMOPtXFC0IAvLnj38asTMt0DL2QydfnhPPJx4x2Tjb6okVJSPVNPIxKfe8Qnh3WdR6InKqNgrURRuk4NErIHv4iTO9NXLFiQR8euOwWT5LaIBzyOFR5ovA6dd_rfsJYoIXSgyTrE4iOJR6CUjfLn6UTMwI6qu-VbZxfrHkqb5dpB0saEPUvH1ULN1dsKg_D12WNBLuHM3esIaHnpsU0wD9K49jEfPMFUZeP3Esj_ygc2SsjE96Ud0mKh-UY7eBdbgr5cAYw7YDW5Lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVEbC9jkkgS_hYodVHAcuAGivZ9OyZCdVUKT2cHxtMhFmCg5JBWqWDA8FAS5qehZ3PILawddQoxqJBd8yBgx24jYCySU7XUtod-2UgUKe30aLnE3xbMrtnIs1LUj02vCdGY-vMHqduKGsmgN32njvHHzzZ9f-bPQ-wpqN8g6TnrvYvHhayDCH73GdcnPHPrjdO3E5Pa1_sT8XfbbEWGklaFnTkM5oYDjFuHjOl1jo47rhPr5bRa5h8yz580zMFl_69Oajzpl4utYYmE3VLOjLv23BErfZgQQQ18nBT85JqUdOiSmo4CX1uU3RJA6vmfKHln2jlJK-83TaN-uHfZ4TNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVEbC9jkkgS_hYodVHAcuAGivZ9OyZCdVUKT2cHxtMhFmCg5JBWqWDA8FAS5qehZ3PILawddQoxqJBd8yBgx24jYCySU7XUtod-2UgUKe30aLnE3xbMrtnIs1LUj02vCdGY-vMHqduKGsmgN32njvHHzzZ9f-bPQ-wpqN8g6TnrvYvHhayDCH73GdcnPHPrjdO3E5Pa1_sT8XfbbEWGklaFnTkM5oYDjFuHjOl1jo47rhPr5bRa5h8yz580zMFl_69Oajzpl4utYYmE3VLOjLv23BErfZgQQQ18nBT85JqUdOiSmo4CX1uU3RJA6vmfKHln2jlJK-83TaN-uHfZ4TNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhDAGDKVEjrix4hfHRRsCvr8aJ95xmFxg3VBTg7LQokGZwIdYYjWn7UmDjo12FkOPQ_pvd6jeWd1FI5eOidQJQd-vtQzW9dXDQ0i6Biba0qy3g7RQpBcjkG6-DnF1ETyHqmUrM7-8OZ92AceBEC-RelrvS9ucHC4vgSlRys2_nYaIVzoKRODQJjZ97AnW9Ra-UrbK6AtddtkDi9Ik04dPs6SdioPbzBvqQAaucppnCMOQ0MqfmKfNDn4XxZAB0zvTC7XQkMeAaAc93-kHhIIWctoapEm88ufYcs3rBmPIov6kGVdVXM2i9VtFRcpzTy1KjR1Ihrj9wvlscTXJj7tw7AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhDAGDKVEjrix4hfHRRsCvr8aJ95xmFxg3VBTg7LQokGZwIdYYjWn7UmDjo12FkOPQ_pvd6jeWd1FI5eOidQJQd-vtQzW9dXDQ0i6Biba0qy3g7RQpBcjkG6-DnF1ETyHqmUrM7-8OZ92AceBEC-RelrvS9ucHC4vgSlRys2_nYaIVzoKRODQJjZ97AnW9Ra-UrbK6AtddtkDi9Ik04dPs6SdioPbzBvqQAaucppnCMOQ0MqfmKfNDn4XxZAB0zvTC7XQkMeAaAc93-kHhIIWctoapEm88ufYcs3rBmPIov6kGVdVXM2i9VtFRcpzTy1KjR1Ihrj9wvlscTXJj7tw7AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsBFztrnWTqx-K2RMkRRagXavrxO24bJ6tQ4ThzMqK5233KoLM1_i6BJ1R7aKXPhgSsSVlCWXghSK3DzkCm-Ii5V51Kyrzxaw6dSNwzgiqyif1SjniD_grUI0lD0I1NMw98ExbPFqSBZjivjdt0Y1k_Jzp9twedlC4eto-ntzYc8-ZoRlZlpAHRET2L4SLs2NWxkhKzEXplo2xVFry0E5fSvH05tiHGa8wn79j5XPYL0udoaR_oe2J0MMPFOIl680Aiy8NLAWqFbZXWIBTHAafVPP7merOH66Zs1aznBxzG1R6RRG2MMviw9aI2VOcC82jTnSBvEsSO-Mhovt8eAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqb5wfaecfYE3D1CtcKzl3wDtJIN0xGgQ_Qq5_1Wm1xYtnGEIGbprgvFA6IUMiGaETQyDn_M7IJQb9OcS-gP9qjzp8vWmRjClIbU38KHdbCU7NNCwZUtZxwbvhYFq8VmZd2u0PnbQHSjA6GQQNQER0nUSIS_4Z-p8MWk09eQ9SLkVW1ktRxHG2Bnm6yjmTbi3r51oef4Q0iZCYmQvEIjBJZtWqS1XgbOgPZSSZO8UQBmYvXNF1uUkHPgMwY7UYvbZmFSZrv8a2KrMUGL74HVFjVfgli8_lcIiE1xBDZfuZ47-yUmgjOnet20dmdh3liu6lsTZLvU7lkMmEZ02isFGLAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqb5wfaecfYE3D1CtcKzl3wDtJIN0xGgQ_Qq5_1Wm1xYtnGEIGbprgvFA6IUMiGaETQyDn_M7IJQb9OcS-gP9qjzp8vWmRjClIbU38KHdbCU7NNCwZUtZxwbvhYFq8VmZd2u0PnbQHSjA6GQQNQER0nUSIS_4Z-p8MWk09eQ9SLkVW1ktRxHG2Bnm6yjmTbi3r51oef4Q0iZCYmQvEIjBJZtWqS1XgbOgPZSSZO8UQBmYvXNF1uUkHPgMwY7UYvbZmFSZrv8a2KrMUGL74HVFjVfgli8_lcIiE1xBDZfuZ47-yUmgjOnet20dmdh3liu6lsTZLvU7lkMmEZ02isFGLAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCGe_QCSSxu-CwQs1gCXTp55jkJmdwxaGWBgpTuJ0_1KdrdYUu1lhsU4pKmVWtk1_4F7_Eeb5SqtvnDo4zrl6qdjf_X9SagJo3Y0odiC9FTuKvqQHj-z14EJAVL2jnrvD5-ZWplAViHuUiq2lDEysP2ic0ZWoeDmftsoRm3_WDkNIqamEuIty6Grb8aNlmZiDCZUpAnf2jWY68iGPXgrcmqrDcwNW7Fy3ax-f7QJpfMuIWpT_uFVk-9QoRYV97Dfy68HMxSStUaNMQIQAtjenasVRUAELujf_nEVEcVzyMkn67UOZ3FYDSrMj0mfkZ94VFxJuVVRNpaNfXwPuZieTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=gEZgOzLC4cq6rl-N6ZSIoXPs0DfvhviDyayKNkn-tv9pRj-57Cwln5ytkxRziGpOPQe_KcRcZlmubKF-aTDcV95I6Me4paJorXmYGWK3dguHyszHIDZrmkKRLmWzyycpRMFQHGQGW9A4pBpf0B_m0ptf0JjWr3N_uh4EClHsDeHzD9MK0kVr8ZMh_wycFakHBJgmbdtGvRGasOsnVadgwOYgfM1Kf7WvUuBGTCYK8AJZ1Y_U1S4ofaG_yRReLdn-J6DNUfMMS3_9rR-ihsinwXUG8aWvXcO7Am4tUwjQWo7nwZG5olfB_FAsGx9IwFTX6uWgtmZRDeoG-re5Etx-JyUieXUN2oJmwoRCenQKME3v3ef69hmwK01w0l8wxZC6oSXNfGYzO19lsedgDuzE8rpI7oSIIFUhwW_ve_NHMdgqqXeD-seLLotXEHLU6epweQ8wokJt3NSs4wNZdyws_NSMHokMmI_mqqgTE_LI3WEhgJmFccDwJN4zRMeVBzPMrYFcOS0MZKU7buWGOImYO1ijFiXFxkyref577VkOi48AMEtGBm0o56r6NDihQhNn64EoMugM2JI1DJtzFjaH9KpmGUvSmZXlYiVCnqNokNwzrcJLX9UMH08Q9FcIDQBwz1eP_ZdxMPsO0EiUzwtVtoAxjBBydFDwKjtxqM_hryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=gEZgOzLC4cq6rl-N6ZSIoXPs0DfvhviDyayKNkn-tv9pRj-57Cwln5ytkxRziGpOPQe_KcRcZlmubKF-aTDcV95I6Me4paJorXmYGWK3dguHyszHIDZrmkKRLmWzyycpRMFQHGQGW9A4pBpf0B_m0ptf0JjWr3N_uh4EClHsDeHzD9MK0kVr8ZMh_wycFakHBJgmbdtGvRGasOsnVadgwOYgfM1Kf7WvUuBGTCYK8AJZ1Y_U1S4ofaG_yRReLdn-J6DNUfMMS3_9rR-ihsinwXUG8aWvXcO7Am4tUwjQWo7nwZG5olfB_FAsGx9IwFTX6uWgtmZRDeoG-re5Etx-JyUieXUN2oJmwoRCenQKME3v3ef69hmwK01w0l8wxZC6oSXNfGYzO19lsedgDuzE8rpI7oSIIFUhwW_ve_NHMdgqqXeD-seLLotXEHLU6epweQ8wokJt3NSs4wNZdyws_NSMHokMmI_mqqgTE_LI3WEhgJmFccDwJN4zRMeVBzPMrYFcOS0MZKU7buWGOImYO1ijFiXFxkyref577VkOi48AMEtGBm0o56r6NDihQhNn64EoMugM2JI1DJtzFjaH9KpmGUvSmZXlYiVCnqNokNwzrcJLX9UMH08Q9FcIDQBwz1eP_ZdxMPsO0EiUzwtVtoAxjBBydFDwKjtxqM_hryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXo6i3bu1UbKHd-1ymz4jGf5CfXcRv00A7nAKJWwAiwtj3x2cB8TJSvxlyNGLDv0_Pi7yHZAXqRXUrr1-mvIpY48TKyLEbNSJsxBfY6z5QXNC_gvHRmXdNv7tgMQAxperfviWoDQhGMdHEyevykp0qk2RT7edapDqVJq4eRF8v_fED_18TS4VDhcGKyG39ZA9-i8S29jj9upLaqHDRi2OzFfPrg_IZ8o-xJcR0gdnfdJ3pC4tH_M3Uo0dZVvuw6vdNkIwkouDo91RRFT671uJsUnFupX7mhfyhFiEHY09nEp2xPjpT9Ie3Pj9JfORRejJ-as7DWtyJLSVeCsD26j8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_Em_VTQ1i76FTDwwRPPRzspVwnec_i7eX7hKN4VFFk4HTlGEdAxwRY3bacRu2SqdliYDJGaGpjwPFWOzPckrXQARmMnBXNZGmz_Zde2KazPNaff0uuJqcoo6QPeDZxUfoyDUB1mD00qWeFXutZlCF7_IUleGn3G5Vo7EUSBiWLiGomzAafdgpivo9Pv7GKiVZtZsUqoHPNgmEDsLTpf8DGVmKqImTR4b4-6E46DnL0jpmYe-riU2aiFRZFZCyrS1yRkOwKUXBrpoXalFmZvXHnL4hMS-tlgaXtgai-r4OOBp92BYOSEszpdzevGl7HsUYnLCi75XSvaaGj56q611Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKTkb695nWPIGfFZyFOp_mxhnCo2I2Cg-tUQ6q5VB13SrJ3gaChUzKgtr-lgKfMkizun2GTydNXFvlGrS3dU7Ek0kiJKVBdPbDkD_fIwm4erVChtMIyERBm_nES9je0eRVC-zZcDGy4qHi3cZeJhLtGvWROvmkl0VfvlGXx4DjICNyV8BvD8redxyWfgXi_N0y29zTUyzbj4c3HaYEPt5eztLEa-frYTv8Tys6ojT0WMB7d5hMmfIGmVZKBbuDtBnxeBEiqtbw2XSjzS-lmaQ8_2fp4xM5rMV1YEq8K8TAjFTvgcnoxDmOLd-YzNnPo7ncnBper3Ist_LVny5BW7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22811">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚠️
خیلیانمیدونن‌که‌اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس‌خوش‌آمدگویی‌تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22811" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5D7zJFBdBnd1FV2SPURYHinnJlr8Vpi22VIZqKE5vtHemvA5n1wTb6jFpUEntEOmUjnVpgzr26qMw7n2IpVyPp29Bf5nVnd_VfizojzkvW4bRN_QTTyusovGJVOSss855Ce9reOS5xWXmzAcdK85tLerDvFcOMh0XGCroa2WNGb5DuMEXdMgnPadI3tAHQCuaza_V17ibacaImdDvgfPr3nWsnrXqUdSQorP5cVvrDJG45a79GsIzSXhMV5icRJRXJWH4LRCHFJdaYa0Izm66RYOY5LNlA-2pZJTPBsXzFv9iUg34q96O92YiUFR0R-mScGgfaxR0xEdDZXZUeVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiSd-mheKOgsxrDLBNwIrz3lXgp0CHL7Em09ZB4qjWuOfXfpkkV64RJdN7Qra75XcuChrL593PXhlMfNd2BTgWCOGt_zWdjPGWY0l-VBHeLhVELIBFIGvWXVrWvd3Biio0kX5hgoQrvnYQyMiF58wquCXis45fYII9ISn7BbYPPnzzP1lpq7MSSA0c61SM8Ja2rBN1LP9uR7CdNcYSDRfKSl3u9hyFzv1XrcZ2xw1lcz_PkIxF30FYusPZWWBlk4XaiNF86NbE-IfT6PxevPDLn8dQOBvSd_RAAFAh3KqlJPKTi8iCkZ4BCfMJfzj33CAQlsEakOraML_gLgDd3BaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgFwInCDyrsbaxy8Rh-RIP12VDmlFZhBlYyKsqSU0HM-kPKuFj9f7M-h9ZK_hJiH4vu5FHF35CcBv3-L14ZL9xxiqKz2K1kn_1qGDcfVWzWp54JxtF2HhcWRK28XWXpl_2VwrUqNBbBcyPn_uPE9sx_7uqSeEBY9mLh-N9p37Nbpy_Tfl_2xCj45C0Wu4UVS_1WmBCjQbLcXIeJmbtg3jzkVDlGRIQ7oltYXM8KYVBtbPZDqIu5vJtT8alwBi1FAM3uKWGX3_owvZzfXupfx4jFq27hQrHZ-UGP7FssdljwjfIvT9aKklHSV981IRcAVjnOMBlqhqexA1qN8taA1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atjQkO9ehJAPYwhyN5kfbwZyX5lWMcBPYkEW_mYXuNSZUY63DMxXBS3lbKL6fOKcfIT_3aOCVLHGG-aOIkgGaBYDU8onfxVt38aMimWh2bLtnsdYVChEMtsGhpe6bVLJRXO1IkGcNvz3hyujyrn6EE6hjLvQzG7AVqcuGdQx6TqtTOjYOe8Nig_iWgFyjkIEPHs6Pe34VNjWHjjjsIkVczVeLQc7HpHjqBhkJY9XlM1EuvZl7DQksE_NCmXykOAZFzzXwypLLDf3WQiTD3aDKq-Cesf2OZkhme96V8JZ12ZmGHaBM8iMK49srbkrsCmhQquylDBHtmBqGL-1M0NfzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3fy0_9lwqXoAfgUK9BAYjjo_2paZtqTEhn1g-4KO5yyucB0k2s-9dr9KK112MQl4Xz_YiACPrs5ForvD3CrhHhTd1iBaAe3Tv3mnxQcIClLQYkW3afvmlIJQzrBAiaZ2UVsGOTAIch0PGLvWZ-mmAIJ6aLbEZ2ZpST0QeaXwPCMnEUTV3KUrQeNM8JUIfmk-Mgp2RJKlPWVvrNl-4dlmYu_TC1U_Zq1rivX8o2BiaC9h34Nt_hNbIoKhywL4I_oIOoaJHLbYiS9FmOaCFUHnjeYGYGwaNwlo_kBfEuUqPDbWPkE-Oh7q2hqCYCoOQo4BunYBhLjOPSygfQ-8JTB6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbHb1S92MOIuXukW20vZkGU8OXFh6rlLj1ryPVpGMv5uV0DXm9Aqbndxwm4sFf7p7lTOPp6Ml_6jP_kNczjf0-GDbH-6Q4k9vEauu0QzJrdZjpQj6LVUkpraZGqtfQ23zdcJoFDIz_ZjDGNxDSlHUrVJm9lQUGvHLP0ZoWicbbQdCOtQAiLRUHG_QGcRypCKyL7fWxPVEbEUzXGyo4DSXzkObLUFTbO2yY5bvp1li9Yl99s-Rp45l2QsdvgUVqY-JWnOb-TyqlEnChfQdOj5LjxW2OTdPd61XPldFf2j2A_tbgvj4iuJL3Ztd52mMTgP-6VW_sdua7CC__IEie4y2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi_8jwHg2c4DycbYXuIear3ffTxAoNJqex7aJHtujmZdJg5sGIEouw1oU_HMTUwZYN-IzInDbX2Qj9I_qwuc5Ir6vWc5SOZwrmOblFsmJ_QvsP0yyz24S4Jm1XHcwfT-w2VaxKut4Ti20f40ALLc0TvtB61BYD4l_Wtkw7hXzeEEQwHLYK21v8VigQm3UKs7FAqIp6kN9k2aLO0_EhcIC8oKAUs5dmYVcueGVu2jHOobG2nuWt77EWsT__JGBkkYSFpLv4LyqrzMBIIe4efgtcxOjS0EM3VObj_0uiyIM6_-rhnTQwRjhy42IUomhaasN91N3AcoEoMqz1phCREOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDACSDa25jmr_HknotT6jm7u8GrUmxCJjtJ9UmbgSQ5MNH60jsJmv1YsrpDSLKIblETwVlJS9wK1G4ILS3ZtSTFuKOi5zO--PBrbErbrM_Dr6EaP2Eqwc-X8iu2MaXZlbOPu8iUGbcgDIPh8KVzmpUhAXfLqvNxguhzGg9iAOP59kBMMDOhxFDAwt08jWP79pUoShPlAxiZ_KY5xQhXAqXKsneEH_PZPb18HS-d0qvz6fQM6nXTago2m4NG35y25r5OiCGSJbEYENrlDZbXinFuDVmb5dyJ6ASqcAuXAaJwmrxYb101q1PaEPMOP3nxDECQyNXGLYoi01vbtD_ma5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXcqWYESh5C62txQ9vXLKNfIC1kYOY1IrML5KcmnJYoun5IjE-C11O9TDWwUbv1W-OtZjbbjt4pb_IvnYtrClf_nvBnjVZFzSDrnsHYv_ZzU4zRqjHb2HD5KN6nZJ4pZep9dqxHy-8OTQf9L029sStznfT_haqkGwVvdw0Nk0NaMQmSoiYLIkXh6YZn2t_9aozDDLtYgy-jaYQEfYGopBc2Yamq9aw5bY_UGNeqx_Xf-0zndTJqlchOZ48gfox5ljOWlEudAi8_puFKvlvDMtQaQ2X69Pzhc4ed0iaZxeeAdIwEE7FvNfZM0-XdzKm2qfuBprId6Gq9WvUxNcizxaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=SN8BF8zUx_52_6RzQWfVyEpD0SgfDNaNYqydncXymHCYT4vVib9wmObQG_t9xDE7QG07RBX3SjMTqYOJbbC6RcHVpaQt5Fy2gUx3W_upedwTWjKJ-b3v7Mg_x2gwd7uI36LXNiK3kcdr-1U0l0-1HKAAjjpH7zbQQKe1U04Qie_OEzqcUojt3aAdSesI_vKziDR2-0Fx8-lTYjk3ONRhP3f7nPYWOotDVzgSljykmVm5FQ3fVeFpvXUTctFq9x8xxZ2so5xf5W35jut5Tl_MhbBgw7qs6g8VOYjsCsVfdzeiNKQR7rnzhOPJMb6-2ybbpGsDLVo32onMLK0qGp2FUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=SN8BF8zUx_52_6RzQWfVyEpD0SgfDNaNYqydncXymHCYT4vVib9wmObQG_t9xDE7QG07RBX3SjMTqYOJbbC6RcHVpaQt5Fy2gUx3W_upedwTWjKJ-b3v7Mg_x2gwd7uI36LXNiK3kcdr-1U0l0-1HKAAjjpH7zbQQKe1U04Qie_OEzqcUojt3aAdSesI_vKziDR2-0Fx8-lTYjk3ONRhP3f7nPYWOotDVzgSljykmVm5FQ3fVeFpvXUTctFq9x8xxZ2so5xf5W35jut5Tl_MhbBgw7qs6g8VOYjsCsVfdzeiNKQR7rnzhOPJMb6-2ybbpGsDLVo32onMLK0qGp2FUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGFIuP_nknMtQ-GETSpWR58Pb9ymbvS9ubjj1hJq5vSIjcqwWnW2aBF5eVfdcqO0bjluheLTJJ33B581rIk4q7yP1Bh-xkMtJzs4ZSj6Zd3iru2rh77M0Vdq0lxfg6UAxeRtrkR-qhwHiMwd3fEwv0Jb1kUx7d5uzueYh_oN5NfUbW_scEGJPkpX-JEjN7SwMcwCEXK4rsmSHjuoWBskmAMFeDUyvZa_jOPfqqsVwLCmPhx0pr4f0cn3Bbq0oJ_QZimOPKrDnWa-mto65-2phHyx82zzLfX2Gv2PMnmPqtP_Q-FDE6ayktqhSutSWx89CrCUtJ-QZoUjCXiunvLxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=gvAzquGRnwsZfeblRPn1Ub74fhiVjFlaP1Mape7IVsWh33ApcEOKnybSheoc_5y8RJF1Q_4suvjEt3iGSqr82JyYNdiSks_v5pAnE1UabRx_3ST3Xuw1U4xCi6-1T1rfxTHl09EXvgmMxYVGO5jf4kTbo9x9wLyZ2fKX3VJrY6-wAd-Y_LmjPTucT8pv5G-tpO8qPJDntxIOS2ZYWiOW8TXp1HQ1_i1jLv0d1bwZK8qiaJ8KheRX6evuWuzrfKkj6O0u9PQzr5OmIEFxsHur9xYya8wCQyKaIJjOosjrHCkzJeDA4h1vjJ6LsZ1ehU3wSyFvZYT9tBuXWvdlm7YliA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=gvAzquGRnwsZfeblRPn1Ub74fhiVjFlaP1Mape7IVsWh33ApcEOKnybSheoc_5y8RJF1Q_4suvjEt3iGSqr82JyYNdiSks_v5pAnE1UabRx_3ST3Xuw1U4xCi6-1T1rfxTHl09EXvgmMxYVGO5jf4kTbo9x9wLyZ2fKX3VJrY6-wAd-Y_LmjPTucT8pv5G-tpO8qPJDntxIOS2ZYWiOW8TXp1HQ1_i1jLv0d1bwZK8qiaJ8KheRX6evuWuzrfKkj6O0u9PQzr5OmIEFxsHur9xYya8wCQyKaIJjOosjrHCkzJeDA4h1vjJ6LsZ1ehU3wSyFvZYT9tBuXWvdlm7YliA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDH5OInDypqD3MKKMiHHHwlnlJgSQgxpkiWcob1EFbMnS8BbqS5xHZdCOKAh7splnaUmJPJ4jR5TxZoBZpAiklEmm1y0rz6sxPVn6Xei0cB7s62SVlknDQ6gsx4rTTmrw3py8Dy5X9vU0E6kJOKhUdsaahv8H_TURH0eOPy-fYv2iyHnUMw7G2xuzh6hEseVhDjT6HVriIdPEEiUJV-EpCHvyAz3YlLvI4cGasgGIFVN53Gd1S1sDovOxQ7_ZxUq8OuKwz5u3ZRbLkoWOj5TH4IoSJRUKve6udgYQh7Bu0e6OycvdRv7x_6E0Y1hwVBvI3B58tD6CE98dnmSv_KRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmLNaDmoyY_rSC_2S37I8nyVjknRJ6fF1AHO7ezhXVe_cWCDs_OzPkCgOesl2W1Jas1BD-USwb1zvSEPvDi9QjajkjalCne7Kra-LyncsOO1yXCHs4UHwwPoNdDf9R1Jcy6AM19UGaomFKiZ27IXnzBckBwA7ZEd-GA5quyzd2VQHLxk4PxJ-RRbZgPeveLHJzoKVscUsGs5p_fq2euGGg4tG06Nx_C4eA_5jDRy0KdTKmeDvWv_TnlWYnr1hqbqyqMtlqrs54q9p0_d-2NBJ-No7-kf66wxZb-fAUBQvT3cU3yfl6m15h27ZPoBIffxcIOt2-npF3PEUaXq73yJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAZAuNNEfQhWFGzW-caI1f_Ad4pzQ60oYBtk8Y7NDR3Bik8u8r3qdhIoGDRAg-RiVmPb0UVNXRJ8IYH8ES8wMXgMq_JNkfZ7GkwPUpqzEOXiOcUzu4Yy79oGv0yOClNL3EX18bmRprODHAjEKI1cIj79kLmLNBHg7Gu3WLkRmsc8_-eNiaixD9Bh2eRe3iQX3qd99Cf1B5hG5RUGpn0zw7YSYPX5sTjkdo1OzVvWKy_Qo5gtFCs19cuoxC9-CUUJmgSYCBsAsRdh_Pr2W0oNm5xq-bNh4UzcwlRnrsug25ZIu-MfHx43X2d-wxziF9dcRbkecqQy1Iyefm68GATsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nryXjzmH9_PXAox5KrXoAVM2poablgRoAR6zPp7LjxrESl0SFVwGS1np6dHzF_zWDjT4pxtfvKUahwJeKa4yjsni0_-ay-MwzWMthZPOL9QGIJIQcDjDzt4u78PiJyJjuzhqXgU3HBH8Tiq0FpN8bwOifFXsy9lXZHAkFWCuTN1AFkysirdS67rwEcwBhzmmuepkI320J9DPEZLpH7Bhio6-qmV9OvxWVSD6opEPKjA_sOF_kk81QhS_i3gw_0FnMrcOSstBAr_eTEbtmtjmCdP0sQ8sb9L8hgmYmt376YxSErCSQSDCsZTskIknaabUrVNtV6-hbvk6vAk6WgU63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCjLK75Mh7VYBISuVMeu9rpw1o6VBNzqcTuhVouG-QLIL6vl-EvVR6Xx2MvFyItUo0ySD1d3BIolaUEyaBAhX9nofzo4FqKwDqCnwXGCxN8R7GE3dSWRuWe3_VwtLA68cHIv1HYAat0IUZXgf1KRvYXXn0rV8o_3bErODeo6xPiQb5bLFirOlesDHIE-nJTTd5MfMR2yZPWbABsrGqFZEySqU4156WvRfvYDrtJ7slwOm-Ky5kPEUmPJBIibqQUghwo8K9VfF8yoYLgzJy0V8pAYiIBjXRzNRJ9kVURyjjyTA2UwRMFpzxXNcRs2RYiWPeMHvLYN_WCUy1Y9l5aqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sy8uFKS9mfwmGsKsh1uXJYEk3XIVNGpkd_wQyOAdz4MU3ZFpZrQIbKhIMjEbeq4cbbkxHxXkWpI_9AtuRMWItA3IF20s5CSCnH4EKJ-Wju5SVc32wVRZSS1jn8Nv4mzwGf7SzBkSOlGm_gLcBq745QfNRVcESMenBguqX34-L9dNzIJ1BZ9BeCccZ40PrJX1g0RMJvciLx54FpA0dOgNtW1VQqCw6ApmaqqxEpkG7HCh7yS3wIfT25UP496SRnmt3-xUSBNfGQQt-dKPLn3X76Iw9Ud8YOLBrVFzmezCjjXnR7qRHZJ-n1ZSTuuvAh3a3_1MOrcIF74CkIsdGkWQnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IWJcRJEAE8hDhQvZIeGWnisVYimM0Ydf8SrSWAjPeiwgWGCPN7Trcn1yF6xQwNzk5_Rbs5VVPCCVxng_RBy8PRrn6lAVAd8hFArMRWgFZm9dxxaQIQx20CdSgA8Ut85n2salLJ5dMyZciMGf2SHrdFMoodjXBjf0sLr-9jX0oWxnz7tGQ47Ufh9EvY24vYKQBtmeU1i21OS0Nzi1G_q1xraZMwAGDQy4KB1Q7dHmeXEOC39IdgqJWR0GhDh4ZSb0-_Oz_RwfO-fRORAuIXlGNS1wQ3dCuPpeDNUsX5e6qjBmiPaR5RMMzH3HglE9oY7GhSBthnktw-rp-YGMzzOwTII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IWJcRJEAE8hDhQvZIeGWnisVYimM0Ydf8SrSWAjPeiwgWGCPN7Trcn1yF6xQwNzk5_Rbs5VVPCCVxng_RBy8PRrn6lAVAd8hFArMRWgFZm9dxxaQIQx20CdSgA8Ut85n2salLJ5dMyZciMGf2SHrdFMoodjXBjf0sLr-9jX0oWxnz7tGQ47Ufh9EvY24vYKQBtmeU1i21OS0Nzi1G_q1xraZMwAGDQy4KB1Q7dHmeXEOC39IdgqJWR0GhDh4ZSb0-_Oz_RwfO-fRORAuIXlGNS1wQ3dCuPpeDNUsX5e6qjBmiPaR5RMMzH3HglE9oY7GhSBthnktw-rp-YGMzzOwTII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=XWGhU9NZMc838vC7NiSQt0j8QMPTcC4kJ3uq7aCcnIowgkMYrGtzJ41iW6x9YttTZyPDlZlA3Ir4b0LKynYHwlt2Z11tw5RFHWAC2BOUCCowGxvqs_6hUDvBwy7xxHAT8F628Bsfnl1B4SWp5VHO6Kn7aNGsblgaxgnS8yMGVMFzMbaau7Ki9eKJtvSX56lklcytxO_xho0ixzcsXyd9sc1e5EwKMrSHATHTqde78veViy7naa7JzsjdNGdWrrxr4Kw3ZGuRQ2Rw89up5kPzqNKhFAc_l2N-WBigU6teRfkeb91O27vELVc00weo_TEqbUFIR-lIsbC9kTwFhR9Wjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=XWGhU9NZMc838vC7NiSQt0j8QMPTcC4kJ3uq7aCcnIowgkMYrGtzJ41iW6x9YttTZyPDlZlA3Ir4b0LKynYHwlt2Z11tw5RFHWAC2BOUCCowGxvqs_6hUDvBwy7xxHAT8F628Bsfnl1B4SWp5VHO6Kn7aNGsblgaxgnS8yMGVMFzMbaau7Ki9eKJtvSX56lklcytxO_xho0ixzcsXyd9sc1e5EwKMrSHATHTqde78veViy7naa7JzsjdNGdWrrxr4Kw3ZGuRQ2Rw89up5kPzqNKhFAc_l2N-WBigU6teRfkeb91O27vELVc00weo_TEqbUFIR-lIsbC9kTwFhR9Wjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz_Qt138qYkB5k9RdwzYDH5E3Uhy-KAnmd2y7hXKax0D5QpO-4-YM8ncjIpxchmJiI-7OfNahUfMNZAbGtEZIFSJ0ZMdzMlA4gVogrTnAfVgPlioJCEFhEB7-jcXRU-JpE-17hrqVfkEdVEG2Kc--7TtlP-rYGZLrxlRVc3OjujLozK0mFn0Q5CjZcwzFM-wYTnJXx1GtQovG5d6CyPKhTU-3oY1gV9KXqw1TfilaD9Q33_DaNXwOf6zJmgy2y-Nu7ngAz5_OvDdFIo5jndN245hY0sy66rYfKG_ms1jKKLXQ8zbF8ymtc3AqnOs5kzZ-tGetMPxeiILts0mIY4vQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHG8rXXG7o25-xuoHr1LjrzHM-_1FyWN2fwV9MEOfkpqjbbkZaUe7cB1dnqy2yOqT2OlQxjXiba2pBrftCEzjTYvJfCkK-rAYD-JOc9jMBPKGLDnmm-m2MIgjOkmWUJOQP8PWGdJaQwfppRZc-vx5SJyls8V0qvTq74ov2PVip27e3v-LzFd5ACaItvR9L4INzFMSUuW3TjLa-GUuNGR1OvmQWKx9YpGt0Ezlr3oV9EamW6ZtW7Q0SzEh0CyvTrF5lwc5TzAZndzH1JEzvRdhA1aEdq8KJrj1D03KdGIX8kTvowffhhWR9XGaEJeZPb2AVtGfWhx6gEnDoPi4pHGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqvnVtvwu3fDM-PAJvsehaNqgyfsEfTgMFzP1q1Dtzb10mXwhG-UeH2USmiYJUeOyMDZU6cZXJq7qmnXutKIBbA3QfeezfPl2_1pfrPCwoqo06coMM_jQpdyqHtXPjZyw5P6x1QOjSMbhVWR1wyiCyGvLCb_VYQqki_dtDgxdu-NBPPBupgrciJePbWp7tzKnsgfLWRd0cvZ-JbfWBd8lZLHCrq396Z9iB_QCfheZm1Gij7Ok6VfX-Zq_KvZsfYLaVInpvCbrDE9Qu1kLN7Lc6WWA2ZZCrpzSl2WIwiB51MxLVBPu6A5C01bnRvmx5s6A4IQMfkvwWisbzUmGMW81A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBS2inp1PEDL9jK9JgJtWKMHfnD8KWV2SFK-UlAyqe2J8HRrSO_aoXvVKJstxK7OzASQiDVyirqUG4m43W2ToBWqdB9UyBVvswiVAnAGVuuQcKQiglI_HP2nPItjKwQMEzUNuFOgCdWVM0-HchW-Smkf5cZYvDJsnMdUDSLwdWgcwsQeKcxOgpBhR-N6pWHni8g23ZsZwWZl6vsWbfDgKGZd06MVM0ueY5ajP3NBKOekla7_cFnRsUirp64tZY-fg42hWdGU4eNaiF-dxuU0iQIegTQvvkxcAD_j-7MqacpGAuKmFPosGS8fwrwDPfJPoUJceIZkwzW3ORK3i49xtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfaBumk1If7YsBryZq9CzJ7GoJXsNAT_cs1RQGg1M_FdJZtdTLM3AghrpbdfsBfCsVRfRCOMC4P1Frq0iY1WAeNCR0aFCMQNmhpOZY0JYJJEk427Jv44wTTWnK-dWuNdEs75xzSXqUnG4PKmFW68yfL6TQ6ph3Dzu6dOAxxza8kxFSuXIEt8aiVPXc7x-NgdTXzsCg__CT69KKPpjNz7_BMrORMB46nXbfC2Ct3WSCPYhIwGH6Uo5EEtNOv_eRvc2Z88BSiMsmvUEl_8QL20M5y-dGfAERLT4Vih_uPYcriX2ww4mU91usq_NT2LT3Wnr152XnhNYYhM6CANL8JMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnU3ZxrH8xsFzDD3r7pI0ZuUptrvnCWZ8BWXf3XcvfUz-sLft5zt6A35WLfJFPZ0IkvGaTvBhY-P7FBJ4bg63uo3ZJP2kg9u39HpQ3PbGFZwMmhZLYgt2GNP2dWFJh_xNheBTQw8tl7M8rxLByamimAdn4gKJOSb_Jr51DFWqz0Icv0SVtsGQPma91sZc14IpFq7NaVqEbcAiD8tb9oqSCicOmlB7ZDefQf5DyY2h4CG0Jx9rDVDfK2wAGis3WEsOIyr_qJV_LAWc2y4UazWveMT8n5wtNIXcX7ngbGqzAhqO0b7mvDxMbrR1a0znrQZJ-X0d8t_0Dy6Cfh1e7Z_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZcRUx-CQjRzCqDRcjc2AUiqcEZT5-dDEIADNpx83REyOORTqq6cX4feUH-66kLKmSwAbSYQ5K_Oh3OlH58ocTQV4dZX-sVUzINySx83Cs9eg3i--fHs490XbPC9KY-uw-2brp_QloPGb5HMb2luP96ImB9scn64DkeDp7PA4-4QCRs_BHJXT1JG4_iRTvOzpWlSERN0tkJMcfmypfBy2pnd21JisK4ixxfNOLTWYnFUiKalAoetM-ByXyoEXQoKIVFPbQw4vS3efvxd4XKO22xZgVih7Aki5KjbKKdLFaBPF1NH8PItWBl7o2y52D1GqX69wNBZbox9vR1X1oJbKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjkJWmDXvMcLfr7CisU40m-wpliiWnCyR7VvazjQtAevgo3JRkB8ut52lsBdXAqZv0igpedhtgPBgcJtFiJUIaS9DPghzMRTP6qCYpx_6ioZuChziJuaW08P4xCraJOBUQGioyGi5xe7p9GWaBoIiCMKan-c119TCTo50t-fYmb-Ah8wDqJ1cJFMaX2Y8kFFDesyghWnehjcgqmKhnEQpz7pT3QfVDV_hwRCsrd1vyqOzBg_zaobRUzsE2ulnmXt_dqjfa5sD5wNEuf3B1Ysop8FGpRFil9n8oWYCnAtj_AG9zWAAHLt5x2F06ajPysph_MZtik1DaL58emNF3oTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYhgSWP67-ooPb-5EX-ryYxheTgvLLbUfmtWFQ8S2t0uMABwvH3H3brWwvJOum9QiXjzGcgTTz-VZsfkj139Jm5n0DpZLmrjuH_foiOCPOk8eD6cM16L9A7u3TSUl1qzlzoP-1ph-oZGPaZIPO-XEsxtk90YeXv3D-YMA8ZfS96DgpIK-OP9hoqDyn3pD0jqSV20fryqTcKSAQzynYzlb9MA8m5PQBR0_YM5ScdzDbRv4o3PNL-d1tcONc3E0JWd2ajwrqN8pO2vTe8Rk_z3Vz0YaZVbh2b1zAh3gpoUDhiPJ2wtgBmGmxuwWNoyF8TDuis0gC5cixqj69BRaZS6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuTC6JtpAYfJMOVqgUW9awUJuJmRrn7Ajgw3-JKCiABdDyIrj6oF7EyjSaJ8kLGkbDvOvOfaiwLCy30DT40s8FApJFcDHt-7AkmhdUQ2wbLKK-iKn6OJrsEJybfnaIwKtOCHVBMqOkRckiCewG6Ot0j8L7elyghUr6hRzl2ZoFxQxkE5RWyaIQuJg7R2UuWEa-duKIriN0eCVOygZH0QmOWqEvp0zP4ktueVAcZBFBVsCxoMwAD9v3Bb0XJ_JtcOgbkWA3iBj_4FGzg6qUASpQSH8XY-fbEBV8Jzm01Xal2fFzPdtoO85A_IEF2pN1GKa8zWVSGkGkurBDJFhcebUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=pXiEqsWV_l8Pv2jp9r8lfR_myWP2FR0nJ-bI9zUkJl8S0zPRG_REy8rohNtEUU4Dx5cr5QM2gmN0AnlwtX4HVcflrbAOHA1u4_92ft3wG6WUf8yrhyzfd91DAGFeOPVxpapuLu6ef67cOl-PCp6FAJkI6gRqN__epLN16Ngd0tBB8LZ0yOhGStztQZqeSmGYotzC7NIMjlo4TN7fUdMKvN1gP2h18JwQXpv3Sd1dat9H1a-TYVeCqvXQeeokVWOLO57_ammjSfb-fFF2wPkGGCbOMlqo8H3jN3sLYKUdtjekOG2eMVuxzDygqiDBLdy_0dEmpojgbPFEowaB_uQyCK26gdbb-A0Smo5JtQPX9BA5p4_efizTthEDe4o-DzsDZx-FE7W883t7QejnHcOdCV0Q2qmCT6udYZsMsPO64zqpMUf1365lRTFctuvqlyaPTetXhn2TKOf2Z_KebBc-uXQxbvUqi1PcE4wbqqhe2Nx1SoHl7hgVLcwfiFPhj4s8bzdvGJWUtrcsZPMcxEud0yACBiYosAkLN5QWS_vw0McPINYEPEmk60r9Y7MATwSFO6Gu0EMQxHFJVkb3BBqtq5VVH7One-Uay0mm-qQyDS7L76IuU9ga6bBmE60AFOJrE6i8gm7t0dkuoRwrB8dAcQYIA5hTid3pVOyWsBfiDiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=pXiEqsWV_l8Pv2jp9r8lfR_myWP2FR0nJ-bI9zUkJl8S0zPRG_REy8rohNtEUU4Dx5cr5QM2gmN0AnlwtX4HVcflrbAOHA1u4_92ft3wG6WUf8yrhyzfd91DAGFeOPVxpapuLu6ef67cOl-PCp6FAJkI6gRqN__epLN16Ngd0tBB8LZ0yOhGStztQZqeSmGYotzC7NIMjlo4TN7fUdMKvN1gP2h18JwQXpv3Sd1dat9H1a-TYVeCqvXQeeokVWOLO57_ammjSfb-fFF2wPkGGCbOMlqo8H3jN3sLYKUdtjekOG2eMVuxzDygqiDBLdy_0dEmpojgbPFEowaB_uQyCK26gdbb-A0Smo5JtQPX9BA5p4_efizTthEDe4o-DzsDZx-FE7W883t7QejnHcOdCV0Q2qmCT6udYZsMsPO64zqpMUf1365lRTFctuvqlyaPTetXhn2TKOf2Z_KebBc-uXQxbvUqi1PcE4wbqqhe2Nx1SoHl7hgVLcwfiFPhj4s8bzdvGJWUtrcsZPMcxEud0yACBiYosAkLN5QWS_vw0McPINYEPEmk60r9Y7MATwSFO6Gu0EMQxHFJVkb3BBqtq5VVH7One-Uay0mm-qQyDS7L76IuU9ga6bBmE60AFOJrE6i8gm7t0dkuoRwrB8dAcQYIA5hTid3pVOyWsBfiDiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZsvCvqngZXqoEQzahNh7Y2dxDBMjeKDcM0fot-sTXPSMd5cFEtl6xJhHysq3NEz32XmjXcezHjXnqqG4Jfi46GMhMlm5z1OsPwlz7SaHP9gc45Q_6Qnju5tplTZRxG69yhOqAgAl4qwFimD-RKzlNoPZ9ondtj4GLqzMoAL6KbOXxzAY8FrdhLMXt_alYk-lP6irxzGBGQZCAjlaaxtd-I0u1-_woXLM_U7tAMpV7890ZPBjtcVbSMv_gZfGbh4yPc6W7HvigGa2RKBP6Xi6rOz_vreDEK1nvAB89-D7ufsT2z1WnbX97ibbMJRoMIdjx8edNsbrd_5d33DcAQklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=GZYqHGgfyjT5KUuW-RrDN0DlNvxZXFRoxwMA73gHdDRJ_fgCi8LdV86QM3ymUVrqT3tfV-kj4nEE1Jw0IWEdKACKBnVJ8XwCooW8Wo-S14pe6M73J4Zz0nQrRpyi4HG8sGkh_8kSVm8JTwb9u3lkctwPV5a12KbqVjLRnktiSANwW8rRTMlQ9cQkgBFE5tGOsB0U7vNhnwVBq1M47lvbh7V6gW95D-XlYVTrdBye1AJFymrxh5d60W4n3pXJunGLXPBK5NDj_DjA8LHJBdQpErZ-5mPNEuIMOltYi2zjge5qEkunW8w_N8iVgnB00G_2wbTDFkkMGF3V1fMR-b_cyaUh4OFYUG6M0LeIHgfCMXhk4yVmmCcwc3baUbfSj_JyyV8zjHg9WEEjaimSiifVSZg3f6yF1LJzZp7l2oKfcBDWnVRBBIhbZWySTdarSjyQg1Wy3j9CZ10EDt9bC64nZRiB19WRXvoO1sniFzNrKBd42_36pdxlYXdf_dvnc-UgbfGI0n3_8q7zSi6egb29Xo6GFp44us2MrqTILI5DZ7tiUWRb39WDWxVJEZHJNpcCw0_BO0rz54II7bmM0eu9dBksKyFNyRbzuJE2cBENjhVE28na4pDeTgGTqnd5dX59VO7acEJ4WL7YWDG8MVB3ZzPahxn1hZyqjCGgwjMbgxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=GZYqHGgfyjT5KUuW-RrDN0DlNvxZXFRoxwMA73gHdDRJ_fgCi8LdV86QM3ymUVrqT3tfV-kj4nEE1Jw0IWEdKACKBnVJ8XwCooW8Wo-S14pe6M73J4Zz0nQrRpyi4HG8sGkh_8kSVm8JTwb9u3lkctwPV5a12KbqVjLRnktiSANwW8rRTMlQ9cQkgBFE5tGOsB0U7vNhnwVBq1M47lvbh7V6gW95D-XlYVTrdBye1AJFymrxh5d60W4n3pXJunGLXPBK5NDj_DjA8LHJBdQpErZ-5mPNEuIMOltYi2zjge5qEkunW8w_N8iVgnB00G_2wbTDFkkMGF3V1fMR-b_cyaUh4OFYUG6M0LeIHgfCMXhk4yVmmCcwc3baUbfSj_JyyV8zjHg9WEEjaimSiifVSZg3f6yF1LJzZp7l2oKfcBDWnVRBBIhbZWySTdarSjyQg1Wy3j9CZ10EDt9bC64nZRiB19WRXvoO1sniFzNrKBd42_36pdxlYXdf_dvnc-UgbfGI0n3_8q7zSi6egb29Xo6GFp44us2MrqTILI5DZ7tiUWRb39WDWxVJEZHJNpcCw0_BO0rz54II7bmM0eu9dBksKyFNyRbzuJE2cBENjhVE28na4pDeTgGTqnd5dX59VO7acEJ4WL7YWDG8MVB3ZzPahxn1hZyqjCGgwjMbgxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJEsTgQkwLvia7iI9f3XXUvUvtvHkwfsPNgT38DUUGA9cTlDvGqFV59g0PMAgb90dvr2x1qgxLpwOQfmkr_P-de1-iTwrq8idbNqrGdaAaiBO77KSwH8iNuZuYeB3LvToCfOp2aE4iDCJHDY0EFeqrrtQcmVVL0V_xE34-mx3lw8Jkfg2wOFlm3LD0kQzDZCfYxaZ7-UJC2EV94zgyEfSJfxGSq1GtnW1hSOs08SSKJHLN3nsLqG5hJ_tImdwzmb76-UXNBD_O8FU0a_hgeyuKg_8dQ9z1gtU8pwEumlV60C_8BiV0zFMohbTDGLnxRdGTK7lwRwdpGLuZrmEh7kow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ0f14JH-c8FrTl-4Ox8-ytn1KCKeM7AV9kNxS0DMghG9gMPEAR1BVojZcBG5EjbEeRr7Wg3JlgiyQ76hTiFGWWSx7PTEwuIAWPXbHN16Wnp9ZFnBG0pX3Gq2JuxjnFBe-lXrPFxcQP5fXwPi3gq9FFAFyzxXngctRW7uRSC-39KVryOX_GkjwGFJ1k-Q-S6OfirizLOsdVvOhhntjHD1MWDtHKR6KDTaX3I355ISzZEZwZGFNth_h4MPfaYnsHUTZR0sTlZBNjZgbT7WytWhPb9QvkzO5Peb2_LHf_DlWIEzy8ND02OzPZqK1dshX0dTxHIvhmhOP-Spgj8piHP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rgw-73JX6HdA41EfFSWKP1W1bEbvWsrhg-eCoSb8rlNYezzNxZvCvV9qEHGXQYMvZS4i7oXtJEKA27aGPimrTmSoJ_SIh-FQVr8x62nL6spxMCrhcGhfcy3ocWkk09cQeeY6gDaob2I_TsZCusc78i_mWCc0TCjfb6KX61c7WfBjMtH2AMkfzi03Ys4YG1i_ZyH70oPtdJGzuNXWCV3FyU8xbZUlTYE4vh1iCx0RPLDZmVNVbPQnMGPTIpfnt5164uT8BDlktUaljGsz1AMPfSWuxQSkC6tjxGxzJQdIq8V-iXItwM4_0efCA0gtEAoPlDAZVuBpgEmCMA8LEB4MSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiiR8as0AqgKmd_x9Ka2QXGdJIFnwd2puIfIkbhelSRDJ0khGlqLJYxVsgJaLYxihFu_q0NiVjTg0mFFaGCv2-J2cBeo4d5ezaEt3PTMfB1PffPBoiHF-jMCPXpGtTXl6Z7tfNwkkqyX6KmYFdO_zEGa7mpq9xXG48eggWq-feXQcJBRw2VCJ44g_mx0ktaB0Y6-16dNmhFM_A44wOaVIsKV_KnxoMI3f08LJD9Bf4op0xlRKOld_9qX7l1M38ogk7uMugCjey1HPwZGEzhgKDxkbJGK9eFOqwQN6jBWBUhGHvO4-tkwPXpwFudKu92t1jdMbSBbFAhzuQ6bgBzmYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r38BLb7cBopViLCo2PvD1G4FHRkiYuIS11t4q1sSEbaD3a_scVseRrmcN2E6c6ywRGm8CDiauMGjexbz3XeplQFLjRWcOlcJo7nCM9PJgRJrs4zE6uHSHYDDoAAnDMKvsV3fNQSEhE1GQiJPyLopkqrraSp6JPXzMIciEtL65tu_6nvwJgjiKQzzDhP5UGZKcJ-10zp8aYzxx8S_za-wpng7tDeyPAyEBDgeKGLK7LjAi1gRjVfAqvMGHWLr-ADuPgxaRjuPZWkRj0vdttDRWWAPktUT1xYLq5JlihZ-1sfnxTt6XgWGV2OfwlMcIh3Vwi7KF754n4oxJBZMeQkCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1TTwBC8KB7P-LRt94BGINBI9vNYPSbsN73prQJRMFuRHcJRFmfZybYChwS-TQOoizkAeUibS4HFPxoEyNRSDpjsZI0Wi-_ywtfkQjtL-p0jVydpmVAXg1QihjMxQjYu92MtG-mOicj6d89ZIdVKt-m2sh9EDg0OKObfHSJxmuL5pajmgVpOjLXCMiSUH122ttllrpptXkRQ_GJ1BhRuojaeIficHBnZdGZD_9uVVbda5HYe-N6PJvKdgxLFdC6Pj8E5clsd6g-T_ZkKgcKCwqOBDuHMO4VpGQAsemo6eVn32PXMojbkcoFrRI6jtyP6sIAkm4gP0j2ZcdSFOhkAng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvETQ27S7sYj0SzTn-5GNsih6zuLJxLV6qiyn7JkTXCt67-n6EsbP-onim3TcgIhSCwsILRDsjJfC_amSH3SFr8Haj8NJHwraJMca0fPR8yxfRDNtx66ZevaOBNWs-GggLRZ3wFBGJgGLCPYGMahofsb4KBo_91v_41MAJWdFoWBvjqgqRGBQ9QZKg3_nTSEBmiys2LHvm4FYuNdCSkSmo5gcIoSY6yH4a7gFDMC1XvUTeVlVQj6TT6QwK0cG9qavoj0c9wW06VQHypm5FWdSJT0-6kf7eHOZdO30IKbljGhWWEnuyQVsfi-oGrn4bszjofAqqGtlYSBoXaW094TAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGgiCTXldu0cBIq8L-CdxDtazL9dvNOKmLeyLyu67hWx7oJwBaniz0kEUlHdtzQ3dfpFYsAr8I1qzoehoHQyDk6r8BSa1rU1YU-QiIzdD2Ji7HwhCQwJj9LpyN1b81nLIMbkn9prQb1gE-V2RYSnaRH75spWCx3b3acXoMN-ZwCVVZIxeNIcxEiZkcRpce8WeRccyhdGMKoixVHoNEmGjQUL7Vw3lbx4-sgyTJmnu3UCI3KMVpJoQDZs1J0bGEFq27ABeaRKcYo8O6SnQihkWZAWssHTgW-MYDsEBrK7aRJDxHCMthgxdle-NlqKb12O_AuvQyWGcNjgX9d-P_PnGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU2OLBNN68wEL3XnmM6awJqQ8lswei9wq6IhEE9BPwfc94zUD3F7mgbyUv_zxgVgySDc3_0vZwrqdQaepRoP8WBpgqi-D_hk_4ymoKqxkTfxoXl8-fzXCdps4ImYUBRHmAs-XaK32LHA0yl4HoHssPX2nMytwJQxOYa1ITgwrJ3gZWS7auyIIlxpHqIYp_ogGOEZ-jvDvIe8MKthUcVlsNilO9kOCqj3dlUU-ta2CwXd8vy3kDZMqNE6dA7WI_Q8vdGT9dMyu9pNt6W3DXTZ_3L2ocsqWkjHAIbS3Ha5Ewm_EEtjQOMEDLnszVut517Ait1SPEW7KlvucMPY3okPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9FsZ4c8l80A2iRN1ew4Kkvr0bayb_Pd2HyjHCC0HIyXhJGlaxfob5e01h3E39UK7n5cTEd1sPll-AmhX00r_ixuNibl9WR1j1Y1v_jaNz15ucn9ILoYxrAGMOpvJlJ8bFY1G-QRZietijI39AojBAC9V3oHGPTrcmtCrfv1hid8cHGqVaRw7FO0TwMOdgYakpH19O0vzi4-XiruM5vRZy5huzCp2_MG1iadV6TnjHXmWFes3C_5V1tjrk9tDm2ue93CnfNJo81AlQZopyMU8ICEOoF6tKIladDPBZnpXjcnXkfWHBQnC8hG7PfYGZXknJd_j06Dly2FeS18XS3hUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=qlmKv9XNKK44jzezw2IKiG9DUNQEqWnXbHdzRa0SWgTeo0j09QQCNADL-k_3J8xx1mFBUFAXQL83xxUIo73J7TWzZuPmIIDttXqwWnl7yjBjmTbsMzpknqLW2YPG51fK_fe4CvTmFuvRsnBCHXQ4WjjY3pZgPQ9n66aw0rwyd7X4X1HW-Bx7x3SA2Vtn7mdLckBv5-q4wJaWeaWrLDcxwFRh1ZPBgvGcUSXW26RWminkRe507t9KK1fN5UNQTnnTRCCHCFzZbg7GNGgGFUeejcfV_q6n4kitmP1KmFfQlfkhJeAy3yrHVsTBTUc3zWqp4d63SS44wiizEeQbYyNTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=qlmKv9XNKK44jzezw2IKiG9DUNQEqWnXbHdzRa0SWgTeo0j09QQCNADL-k_3J8xx1mFBUFAXQL83xxUIo73J7TWzZuPmIIDttXqwWnl7yjBjmTbsMzpknqLW2YPG51fK_fe4CvTmFuvRsnBCHXQ4WjjY3pZgPQ9n66aw0rwyd7X4X1HW-Bx7x3SA2Vtn7mdLckBv5-q4wJaWeaWrLDcxwFRh1ZPBgvGcUSXW26RWminkRe507t9KK1fN5UNQTnnTRCCHCFzZbg7GNGgGFUeejcfV_q6n4kitmP1KmFfQlfkhJeAy3yrHVsTBTUc3zWqp4d63SS44wiizEeQbYyNTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsgiT8zoAST13nq4dUT5y_zTYni4b1gDL_BGSiT1iDRMlwYeoe3DKKvhNYDifB82FV6tDVmy1iceG2kcVK8-aVoafXI_126I48Z4ydZq7WwNL9-pmd0yFAqaxXwlw_3K-PuC4oztwizwFzdd8tlPWkS4Z8jnzlqGeeZA54jlrcVvk9C1BYQr-rpq9p0mmuGhcEK0bTC_yVGTxpt5yhEY9bkM6yY-RlGfu5X_sYflB1yhsGwu5PQrMro3DBAlgoNv-IwFRbmKscu349kyjLSivIU7drlyWkqiEIcT0CvM0cAuWe2zHyIVFPV5AXxW_YY9Kg-9lcXkymI9tS9yeXymvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byXnD-xFYohv6nN6BGs6zTfBlFQfP80_gEZZmBRhn0j5R8faQG1PO5BRera9R0zrD8zwFspS7DzGe0Ffgjzu1cGt2AlOA6NH3NC4ihFj_wqd_iXfeS4lg1T25378YLl319_aVUfE1aSDt-aRUPVCa2EingNIZnuJ-RNcppmOdZd62hDSwKHPPc9kFHAPXnFpalM_lHBRfCBvc5wEGBo6_lhnl2sgSyjN4IBDnbnXUlin5s16RF9pE6wrA3YZ8rghEI35MFz35tZUbRM5gssc88Y2qCjKzMzj_blZCHNnHiuxgQVhS1Pc8oX-sO6Q5bQ9hIp8d1VDRvQ7rGJCD1Ar7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsXctxDphBIlCmm2KFfm6xs8zZVRqMc74lpHjRcDIkBSh5NH5va972Vl-1To4qAMIW1gMMVKJ21BfAKYE4e-mmRczCaDGEwJSoRqT3bK1jOpvvVjVD2K3MpO34fA0b73BJP9rb4pFtcCiac-5QUcsG_UqSTJrqBAfvR9O5yb7P_k5OoKziKu1Not442UKkjbNlkJwerDFE_9ggO4ecXNgY7vN-jXtuE4Dgf3QwoGXLoJQG8w8XobjTItYIgjja9KaAhsJXWakN_T-ROrQQqTodZDgFOnEoPhzsx_m4qhrxb_k6r3keugfFiIVwYIQcVh4L-N5FZ1UKop94LRNmAAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=pofvVgnkMWlbpg1HiDq-HsbvczOSmgl4Va4RTwLNXD5f-Td1WSjgQguuZ9NSGnjkR4UnK5XiPi290UGNV3FHVQAl06c8QXnMwLOWSESVHKsf7HmkOeIpqGu8wJzHnCXIDDbefz-KIspnSdsICydWu92Lnp8nsOVwXuWdl-0h2nNTPzXbkgIoDrTyv4qtqZcC_ayNah9AI-_gXuXZf5cMUJdmagET9_x4LPBDQWucdTho2CtrcCMlXCp8pQDN6BuRA3POA1QM_NfAmTYFK1JECLDaSLVQV37v74mugWqAGueJQiQqxCCp_hEgR9ucpbc73CD6p8x0bPPy3jeK_vUMZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=pofvVgnkMWlbpg1HiDq-HsbvczOSmgl4Va4RTwLNXD5f-Td1WSjgQguuZ9NSGnjkR4UnK5XiPi290UGNV3FHVQAl06c8QXnMwLOWSESVHKsf7HmkOeIpqGu8wJzHnCXIDDbefz-KIspnSdsICydWu92Lnp8nsOVwXuWdl-0h2nNTPzXbkgIoDrTyv4qtqZcC_ayNah9AI-_gXuXZf5cMUJdmagET9_x4LPBDQWucdTho2CtrcCMlXCp8pQDN6BuRA3POA1QM_NfAmTYFK1JECLDaSLVQV37v74mugWqAGueJQiQqxCCp_hEgR9ucpbc73CD6p8x0bPPy3jeK_vUMZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aH8OnK7VKbEsv5fLVoOPbIUXggs65jMyNOgQI-FihgX1HnIuW9JxWxxMFEyGABoFAE2-ywKrHZz12qV9NETiy4BHGH-Vr5eu8Lt_aoRLqo4eVPyDznlA4LghyrLkmljmcfMnKMI7k6frC_jkb0pV5nBbG_gXUI4l4bdtEZYd1f5iRTb463hK_D_db5HBwMGJ0rzDUL9F2Uvg3xrLJm75prt9_vr2xY1wxHj6axwAKXboyGffTDUfbNvvJRQWc_GapNixIKgMF8a8AjCTch4UA_6XwBYgjphPX4mTbTYOZsfXqa8cakG3g8y2ZZhOHW87kkd_p0phUQ0RTd9zXZvoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKUid8G3xZwbuy2FNiRZB_XH55Pr9w3hICXQHt6qEtoyHdvwgfQlLnyvtG_-ZIO2EDY9u_4hjZ5ONR2KWnMFprBOi6PtoZ8rQM8QnhrFMHDsKP0LynJLobZuZ4R1t4aVFRIu0qk2ABsu8wCliD9uoJUzTfIxDL1UB6tCeV1D7Ci3Z_6m6iSvX4I5vWI-X9qyyZKmdps42a7-3Mvf2Ymrygcqf4fAc8kBb3tone6STjt18MI9c_QLav2tOqPilLZOADHvt1KdaDVl8yo5_8GI-pZsTqaL4wazckknErjgDIIV1YZBTOH8-S74VXpoUAq44tUlk8ayYgZ_WZ7IiIoFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7VrLv7l1hFjkYJZlS4MJRyUyxOernve9KWHZrLp6tH-k5-YNgm0GR17RVH4dk-zTM-RxQ37zl_axC7SnSXxmRqEsKzate5zKETAUTOKV8YYqAByXYch3XiSJTEkVGReHGWoPns7YS03OsIUzoUm3j5EvJz_VSH7PzbPhFkScomHBwc_QiGhRzI7_NhPBPHXvrn0bdem2HFVww9PgtP4qTsxAxVgrqB6lMw16FiCFQT1xFBcTpTqeBNPv8fxorKdaC4OSxhzvFZLYbTMqLDCaDLnazEqaHaNEhwDi44qDVGTLnhRZL0iYev9lx6pyZ9mhow3mD_Edn0VIe0FqN1ypA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8LVkzcgLgpG0vEdBTH3vIQ1bZasWBvHjeVjKIA8r1guJ3ETk_Mg6jqFJMVADp50Nz_6-M_flkDrdyjcdAjgLvisB3ZOLr5NRADjNOk3LJzhN43POZnuCtUXqmvfKdvSavuJ317uq7gJte38rxVW7AmV9znqlY9h14iHxeNuyUuDLvVd5g1SFCEgchV5hO1gQEALN9GD_o9Io54zbXrfPjUVzVDr8Ezoy94KYuvVSkQvkBiSEeINqfl3Tyi8QyYCdZZ6dfaYNg2Gurx_UkKmnCDg0w4F9VBsDb8EBujLYoSw645hrCtLKMibtfBHZDV_apH56pnO9V8_Dewx5jtUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEHY-lHFjHwpzD-BAuJCu4f-oSG8cGCDK_pS9saRBDeVQtZRg-ATN6S9-N_K8I3sX6KvM9NN1yZMZ3Egrm3ZbwDLmLT2-zpayNNaFAFnLcIHnvfpVeS2lsxqg-Iv81_Ylykm47pJ3kZqFy_ydLCaAkh7fCAGEkjwZRJFqAwxSva28Xspy8RqUmjiJZweV3Fn0k5baJJZiMUDWhZKqHFDPVm96Wbi4BgL4WEaoK9d6s-vwYVD7sFKDBcn7LAfXAKO_oIKmpj90QG0IHheb3ewpzxrBcKFn5agTsvrCFUz8-q1QS2FYiqJ79kzeYEDrRgg6tMI1uMQPe7Ck32YdtTNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAzUoUHfSB13jo7TE2vwlnk9XWs-F6CWUw0KEBhun8WClOvs9o05vCUXJ7B2bAmTBS-DrPpof-_poxBz6UBGOfpWkez9kJ5L3O7Zwg0fPd7weeTdmkTOnmHQkf8aAmlnHDFWAl2W1w7NRyEjlua9I3fgtxOxl31AVbGEJ6Wc9D8vzxub-x42mHnyAcrq8KC0ypAuN1qOtLBzQ-fdSqysuabLgi7qLNWQF2NcW-33-8bgo8UTy7IT8Oo6sGn4tkLxaT6Zp4safLNzWM08oqC8q-5sETfxwJMMGjlHqyNt_NCHicOueTaZqmq9rYIMX-PfGEqIxh0owQSDRr9tVHahGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myu6dae-POk1D6xg-fhjnpK3wu0Lpx8S4QhA2S5wrOAeZZWjcx5AhAppQB59f9XEVC8Mat3XcJOALgz39qURKiz_Z0wHQeIyEcNR38TZuDq8OfoSb566DmLFQ4WJdZTVM9gTuYFxrIBFquw2vogUp8eLbmAxFks-Nr16WGOi1w9eUwnjnRXNo90ITwpC66F0qVmg-lPACaotZgBfOs9TxwPb4bVWFzq9FHhYV1fx6AzVkYNy9rsve9wS2XbK6JyN-8u2wqybx34HkTE6CL-xfaMduk6QoilOWmxs3AeEsEQiBAOB86aJcBq4J6Mqc7s0UtY1Lvqkkm0umGhMZbA7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=QYDCxf8hkVLcJOGTguSE0EJA3feF2u-hRJXnjUbj2DhiBD4fNHo6c2XvYCC5BRoUmQMNYSk1sw9DCzutUf_tyfoulJBytWf8B0TwqXRdwvQWCp85rvW9deMuUYxJIKv17jilOprerRAjYg4UK98u2uA1PqEemja07Pbp_ZyuznEGoLw34cevpANjTwFi_evU5tMVEx56JOYvxa-Ar3YzLxdvu0sN3K1TKbwUOZd_ykRNex-4DQFc1nOvUum29hhI9Ogouygfczny4zXxOpekugiypmgo0RUyeJf15ZE-x3feCbnGKZktKwchtVRR6d0jPXuOJKC1pKiDdtZvTlw3mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=QYDCxf8hkVLcJOGTguSE0EJA3feF2u-hRJXnjUbj2DhiBD4fNHo6c2XvYCC5BRoUmQMNYSk1sw9DCzutUf_tyfoulJBytWf8B0TwqXRdwvQWCp85rvW9deMuUYxJIKv17jilOprerRAjYg4UK98u2uA1PqEemja07Pbp_ZyuznEGoLw34cevpANjTwFi_evU5tMVEx56JOYvxa-Ar3YzLxdvu0sN3K1TKbwUOZd_ykRNex-4DQFc1nOvUum29hhI9Ogouygfczny4zXxOpekugiypmgo0RUyeJf15ZE-x3feCbnGKZktKwchtVRR6d0jPXuOJKC1pKiDdtZvTlw3mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dlwg8pf-lBsUl1d4gD0cBlj-dqzOdn-ECY_qRaToJQ66quvTJlw9ig7mhgIXuAvyUi8LukUiP3JyXG8qdSATDDUA3Ja1ve_snqR6FKG8k1Un5dQB20eftfLtHwF0t5mj3uzPAzfozpM9CRGP29cR23nLkFr6r0R5j6VHI9iKe5cdR7RtpKcxD6Vfa91ubVv1_GJZGQf9vr3iobTlnZxfJ0tCM0sh21Uv9cux_AKEr16yeyn4eQoeb7peupCHUC2bFwJZp8-LSUri69W7jRdWBZ-AJ11bl1W-8FkQ17qD-5DwlLL8zWmfI20EfCRZGKOvOdqDjCW1x1_I1xjZmjmjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2J6kuPjiL6Q_pKfo9s04bPjG6fgQ5KGgCDS_Qf-58ayTvfxQtCaVj6nDsTZEQABuGkCEuB_U5_UQvyfqV-YE0GPePgwu4gUtDBP-mhm3pJqCSHw8s7jJpd3uEZRgNoPUQCV74i9F24ThwtgdIXvqt21mxqzqGMdph0LxyFdyaNOeDRJG8ldoDMlEIPyXVKpEkHDQempMp_38JxuYbSWKUR86yEDZXy0xIuJwhAZH2rTXbkGhZ37li7hZg-oFYwUPVtdIOUXpKrYAc0LEgdV1qTe9BsidMhERjoM58sOLMhbfKwRluMJX775aKeo6GGHdEOZofBTO_soFaEW39AXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaMUG4ISpntTkHaWfHfSWafL1sYf3JD2OFOA6ybjhbUmRwNakv6gpLL9iltgu5EHfWUZdr2Uu_pbeUQmUG7uz6xaEekop2dn52nC1ANykfXt0HaXLLhW9UqqNWpp5JR_CrI8_hqQbKr9R8mgHdzXWVWXQ4ZrE3nx0wSsvM9_U4MF29SlmC8thfQZ06tN_ALBBEgGqQi0vnoniXEXidaX5Ltci-nsnF8km3iV2MydiUqGTUuc6WsOb0n4k3w05z3np-p1xxSHHcLwPFbKdtLxgflMaEFUBlL6CAvB2nciUERnvSyK3c20039b-3I-v8th411N-ugMVnPmCJ-lmRo-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUdRMRaYVv9MDvhu6ZaXSJ6AULZDR6ek1yLN_7uwMzfrORDR4KzZe2TWVAooER24QQWTIDMDN-BXZWDX12XtREbJ-2vq-UviUlDmvPh7p6nxJ9MXUWGC5ScD-rto5jUJAMGDI9RgkL589HDZ20MZEvWaWyFr_BbuLoAuGtToDdItVa6nDqTOvtavcNF-U4TjSi5YGVkHZLobP-hMfMxBiKneeiJOrTkCYVvXs5xzVL2Qu54XsWQqgMGpVCQgxCz4ScNl9jlV3w6e6clNtaLOT3wlJh2xqMC22v6jwA5RXk9n7iWwHPHex6B1QPr5CZawtGMxdIK7DzbDGCzPLNAixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIWOA5QPyuJ4cPA3jpew9hAx9RkfKfGPzekugkyUcU6PQnqiO3D-09fnwtnZ1LsEzck7nMvi-5c8_aUVxvDSnXTQjEIZGr0PQ-fHATTyr37vC3VBNjquWRk1QrsTa5ZT2T6s9tIeqA0DxRI-sRyoBTojOAkYx0Sq7q0gRXUrTIUJDCoB31ncBb0hIf_KLLAOWDqyTN-DOyXHsUNKHkJE7bQbHsNu_08tu4AbtWW5zr-S_1L-Otmx8p8gPQn97yA3f-bLYsgDoOGBYQKrH0Tgo0CY0Bdi6QrlSocDlExf_Y3-Sb3KP7Q_zsOXxCc7eElZ7i8ne4oCAMceZm4D3uiN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
