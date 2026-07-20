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
<img src="https://cdn4.telesco.pe/file/DhagzxL07yQhsjYeVb6Gs0aKX4GzOiQdpKhqv-EjXOUxuHVS55sxq4mM5JXB9cvkAAorSaJU1cVQ4ls4AYxarIGINnruzNKjr2rjVoDK43vWQ_dG6GB_M_NBlzEygyi92G2-TzbamMu6BJVLiKekOB6i0-DH0kVir0RziioBAAOKDXrFwAS30QYKRYmaP4e16SfwGy4lBmwUkfk0kt94upjrDDcamoX_rN70jGsTJ-Y_13HF5EJ56gb04UKFPDAb8Wfn9_3TURZVRd3p7R9dT5wZuvHX2YcnkDnjCfT9r-S8MgRxPtRWQu3xGdkNZwzkuMulOBSYX4jB1ZleeQAfRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 14:49:00</div>
<hr>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=V-GfGla_5EIojnHgbsZVg18Dn7lbQv6aozxX24bwMZhC-slIv8wewcWxnS1VrrrkrJOeJ2lXub61RMh7ezzNIBc1ZXsHBfuwcbSJied-hK2oVS5-baLfEqn0OQxcITrwTzsTiL-e_rsya2oGdLRYOqlhu06u8Yv5Z_q4M0QGxxTAvzaPSrJKfrZjsho0EEsw8CbbewhkbvuPJfGR2ToRAnYc5gWomlkwS7Yi4zRpIaqz0iyaJLQPx4Ma1QB5e-JU6rpZs45nfdxinN2EqJOvWq4y2Vg1sc29otF9ICWCOgFniEP5zwXBM5YuzUj_5fkxygDEUlfzPxDq-JOqBYCtSZVTZlMrFgpbRgAcpSQZHkUlDFq8lxhZ-sxa0UGKSUdsqaCWDT8ZWbD_dLkVYXkwVL9F3O2S0mOTvxhAOXww7apzsfJHRR67enkf0DPSD_0Nq8G7LPRObthHmQr6AeSCdlvn4vx1EEKrM8-lDRMLPUPug7rub1e5dX5pc7JPnDRJOsOnF1h3fq8maigf6yTnsb7Hg5e4L3FcrfDM-OQKrqcQf6GKHpk-1-cii_t0eFlC-saaM7yyD4Xr8iEqNL889xHzhXHcs1JYgelUviVZeEdWsB0hGZcfl-vkxowuh13Y8IAcGr5sYsovfpu33nuuhFY0nQSkw2uyzGaHPT6K9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=V-GfGla_5EIojnHgbsZVg18Dn7lbQv6aozxX24bwMZhC-slIv8wewcWxnS1VrrrkrJOeJ2lXub61RMh7ezzNIBc1ZXsHBfuwcbSJied-hK2oVS5-baLfEqn0OQxcITrwTzsTiL-e_rsya2oGdLRYOqlhu06u8Yv5Z_q4M0QGxxTAvzaPSrJKfrZjsho0EEsw8CbbewhkbvuPJfGR2ToRAnYc5gWomlkwS7Yi4zRpIaqz0iyaJLQPx4Ma1QB5e-JU6rpZs45nfdxinN2EqJOvWq4y2Vg1sc29otF9ICWCOgFniEP5zwXBM5YuzUj_5fkxygDEUlfzPxDq-JOqBYCtSZVTZlMrFgpbRgAcpSQZHkUlDFq8lxhZ-sxa0UGKSUdsqaCWDT8ZWbD_dLkVYXkwVL9F3O2S0mOTvxhAOXww7apzsfJHRR67enkf0DPSD_0Nq8G7LPRObthHmQr6AeSCdlvn4vx1EEKrM8-lDRMLPUPug7rub1e5dX5pc7JPnDRJOsOnF1h3fq8maigf6yTnsb7Hg5e4L3FcrfDM-OQKrqcQf6GKHpk-1-cii_t0eFlC-saaM7yyD4Xr8iEqNL889xHzhXHcs1JYgelUviVZeEdWsB0hGZcfl-vkxowuh13Y8IAcGr5sYsovfpu33nuuhFY0nQSkw2uyzGaHPT6K9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=AM5aqFRw48bWB3Aug0gRhMlTLAP7WdvAd8VUYcgBJMIUlH2HWvhoobesVRdDp8q5L74GzzV8gMUKUMXySSfhNHWGWmDogwnWFncWrbKMMXPKtBM_FgcEwoaAFb0rxk9MKzUH5WUvEDP4VvqSApvqCS3rda9MIDMuhCUYhrA9kSCr4gqCYB_wtuYAaf_bGd45aRCQ98iU9L8DIthkTNpTsEevNN5nqQh98O1lzowGUP_mJc0EXW3XGAYB9rju0yEvG9bTvCWqmuCqjo3fixjWKJVAm_xtw0evH2e_8nur7Cq89Ir0cLAi1ryG6TugqzHluikFbVnw2aJYUKfkesrNcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=AM5aqFRw48bWB3Aug0gRhMlTLAP7WdvAd8VUYcgBJMIUlH2HWvhoobesVRdDp8q5L74GzzV8gMUKUMXySSfhNHWGWmDogwnWFncWrbKMMXPKtBM_FgcEwoaAFb0rxk9MKzUH5WUvEDP4VvqSApvqCS3rda9MIDMuhCUYhrA9kSCr4gqCYB_wtuYAaf_bGd45aRCQ98iU9L8DIthkTNpTsEevNN5nqQh98O1lzowGUP_mJc0EXW3XGAYB9rju0yEvG9bTvCWqmuCqjo3fixjWKJVAm_xtw0evH2e_8nur7Cq89Ir0cLAi1ryG6TugqzHluikFbVnw2aJYUKfkesrNcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okuTdKje8YFPAFaFtT8iK04tvGrvGBhCNweAigICTl9Ss3tUNEnsWFHD3T8lwxrziHEaL7O7HnifRaA5bKCU7hyJUfEPc9iO6bvbB1i9qyudjd762YYstJ-EEWxNljb0gQnRllat5LadLyshVFo7sPM7NMe3zPLXFpfSXZAsodvNPMUf1xwvDbM37nYdMMJxWqkLYVArVb0icyZcVGKPskPw-fT6JP17nxMInNiwrkuKv0thzA7i_SuzJn1ATvKYmWRnFk2A1elhgbvJXmYlTQ7VlmXkZsGZZGdFrvsrLBoV1rgq-UQuOLIJACpGEZexpFm7kscXgtjXwtPOLpbedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6HOGWW58Ca8r-IfC0ijyKWBEbOMY0OfGjz7IobZkHa-aFb8m-FOHAs580oxjfI-FLULgtoG-ornyIyE6DwdizY-8jXfwlEU96jGIkjEhRK4-uB62C8Uu5FxtP6EM3yTYj805it_LJZM-BBU2IGV_xlASohq3YLaMouLrpXlq4FtHiw97YPKktgC_kN5p2NOltNH62ffMmoGfdHTK4ISX_vAd0Kfe6QcXpqMmstJ5pXI4LRBg_Jxu9qhLbRR6MenRjkUEj8p4K7e3tUIDy73L7ZcW6eOrH_r_hmBpUgANFCbiO-dcOY_CuyWzvk9QIU9TO2DfIrggBBt5vWDe1aHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDHceAws_DgHKJfPyxY_hbQFOKydTvRD8S_cgOocirT6Wx-ywl0KRXHQf6OhMNN3zocsp_m-f-qXQ5LsVUrIyAVJFqfaNc5rw6pss_ec7QVWAkSntWb2KwTWP8YwjbBOOMihz8GGAkNdJ8ch25z8QrdZado7tnLzBnW5Qe5efpv584P6L5_V7miT_QLG-SBABYenMKGWGB1YzjZ8woeN7pf2VImgkxl39Tm3qZ9YAEcN39WQJMSSSDCbPBI85r5LMCrbsCFz60xSY9D4pxmoZcKLUvjGJq3yRKS9pgyas2mT1tB2gou46k1MEs9KDv2QarRE2KF4-LjKR8PvP9KJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQTm-GORMQsHyoQA2Jfe9odBDfnVbM5wg4V5gYjcyBNcP5-N-mcPzn6CoE9Wb0cNKNhboYrr5VmCWpbBjgOua9Da7F7pXnc9pWvx_vqb95Pfy8J98qtAB8y40-DEhbThH_fxPQLv2PYX4I9L13zNe27kGLwMlHl-GrBtyRKIA5R91UYA6PSdBGFbhCoCpBOhNRMWNP6cblMKBmYyAMdgwixCp0ghnR92N84suRuHUGRzNK65D8nvMayKqteTQavqfCoYy5TsGTJYAM7_EJxKtZl9BRA_QIDnyWNICKImpt4obdRBKdmm2EDSgv7fODc27_CpxORuOeWjHQR4hFgyyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIOQVfZhz0XXHmouuOFUMaUiXc2QtDnpHgcvJ_6lMyLvPvs8vAbQMS96y4x7Fu4lDImcltyaeO8qcsieUdVVrjqKvLhVz07RWiYvEFnCkc5oEGMA-lLoYN5cDatcaY-zGj6oPI7Qm46NNOvRDBhCi4U1Jlq8OEUBy_4XnOo1zaqrfKEbt0K5KwyvFFMkdEg4g67rxaIVirQN9_0UIn_o8wFWi8hihh2gx97z3j5bs0XutuWDNU7b4xStT6ya4yX8-Ag8dIL_Q6WPFsMnI9tyJXPXa5_fgJOgJpUDHnJ7_LSTh7ubMeAxPL1wUlAXvn9ggmQQZSi1SaUNzFZR-02frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyuCq6tEiv8NQL36SMUIf6ZA9QmVBh8SCbwnL5bDZah_QiIqzuYa2DZqZUYv6w2wlal-eKGaYKY_bgFyXVslqJCEQlIxO2p0mgaDotC9QI6xJ6TgWcRy7yfZ_Eao7vev0eRndXnW3uzS3FgHwfbe24eB0Oham2-4aRyTdUaqFg_u2xvjHlvzEywVAs-V7t2-T5B9Od0diDdmUHH6fgZkL994Hn6-t58TdqGgq0md9BETc67g3OVakxf466Vp6v23kWISRTizM719UWroRY-PA8av6oi2Jh262UPS6QRsr8lCNK-tDOR7H1x6OiKC9Zp5tDWw2PIzBWQd_Ep3RirYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKb2WoAYB2BfZWkNY37IBbkbjJc4SIQ1g5XruVQSrsNKs3qgofww7iRVf2qoHSMHt6t6iMSSSuI5_6vfGuhUR14Gj-tuEAUG7WOMbKyyWwtPM770N2Kf7em2Ts-reWnN13h58cs7C2vy2zGJaFZBJg9S4K7sWOw2xdY7vpCzU8FrGrZBPb4ZBv2JGSw1BdmJmBzcJ5JxWICl5QqD8l_FZ-hXN96hAPs-knwNk1QmApMnpJMp45YZSZiJZLYuw5X3NAHMPzlMKAR0HCu4nBM-LypbT-i9VR58PTd4ID9ZsTDQmszlfFOJ-ihl0o_I2WCB1dabJaw2OWhHUsecid3pIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=iGQ7uWuF4IVbYvQBAeK_vgUaE4-VNFQ-gV4mPYw-ZFL1BaoWz9I2FloV4rf_Nb-or4n6ZX_ASuO4PB_sbhewHP8KNgWxRZolYOvUNmd9Htb3L8I0ip88MHjoNBWAp2NrHrVaIJTUx4Ercy8-le1pv5vPWBeuAzXtfRMjtQ0Tp1BWQwW_6O7iTm2aTlcqp4IiWUxYpgENc_Q7iAHgYrtNgW8U4d9XRbCo-Hp8HovZiLInUONHY6yLY4vQtwVBcwX2ov4-WUGR1Ow6-de4wxvWnWr0bUsQm3glRxV042sOZlWAaYpgMCx3qzd5UofghkrX5Ahne90_XWKjZUrhfYeQcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=iGQ7uWuF4IVbYvQBAeK_vgUaE4-VNFQ-gV4mPYw-ZFL1BaoWz9I2FloV4rf_Nb-or4n6ZX_ASuO4PB_sbhewHP8KNgWxRZolYOvUNmd9Htb3L8I0ip88MHjoNBWAp2NrHrVaIJTUx4Ercy8-le1pv5vPWBeuAzXtfRMjtQ0Tp1BWQwW_6O7iTm2aTlcqp4IiWUxYpgENc_Q7iAHgYrtNgW8U4d9XRbCo-Hp8HovZiLInUONHY6yLY4vQtwVBcwX2ov4-WUGR1Ow6-de4wxvWnWr0bUsQm3glRxV042sOZlWAaYpgMCx3qzd5UofghkrX5Ahne90_XWKjZUrhfYeQcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2sNc5mxwePwKfGIFj0BQvMIApb2cCh6AU1o36HycD4LQQHFcO78m5-waxsz_pkGtHLJvlaDIjUvdtsVp7R5PtXGyazqIELl-QRteq__KqsQgh4az-GF5jE8ElfTc1MyEa-8xAqiKD2xT4_5wVyhpPWifZbTyiNgXtY4aGe1cRcxqnz1t56DyO1-0NtzvX2P90SZEUG0E4l1Hg8oqyTGyA4-iKw-yUM3IhF7gWNEbOoDzkZi4v8ob5Nwjt0-TrRR48P3KF-fWjBvDnHxRkWxNhUYDBYulWmgaMLr0yDsDjQ--Sm5ogtMD_gIVY97WzwBP5IBoTJO9ubn2kqSQT5K3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=l3g-ianZAdcVjPYrLP5vlT4Qj_MAdABPgltN-c5_6tucrRtLxbM4lgQ4AEk3iSJgM-qq7-xZ6DHn6qU9-Kxq2jJvYvEjjrDfP3WIzeo7braBwnMADGkmBwKlGX2_B74RVz1un26q5vqaR5GkHYEm6e8H3zLnyu6LUfjV7LNBZuGdyflt_NGmhIMkzzL-lr0UKVuHSTi1xd3-9QTdmxVgQMIQXdsRJWkinEkSqyJxcayNsGqpGDZ36QXEwVfKd2edV5F5wTVSFsG5DQH_l1NqFEbAbHhrv0pZNTh_lUusWHMol0ZSDYlWO5NbJPXi2xXFUJiHkA3sFJnR8NlHH31fWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=l3g-ianZAdcVjPYrLP5vlT4Qj_MAdABPgltN-c5_6tucrRtLxbM4lgQ4AEk3iSJgM-qq7-xZ6DHn6qU9-Kxq2jJvYvEjjrDfP3WIzeo7braBwnMADGkmBwKlGX2_B74RVz1un26q5vqaR5GkHYEm6e8H3zLnyu6LUfjV7LNBZuGdyflt_NGmhIMkzzL-lr0UKVuHSTi1xd3-9QTdmxVgQMIQXdsRJWkinEkSqyJxcayNsGqpGDZ36QXEwVfKd2edV5F5wTVSFsG5DQH_l1NqFEbAbHhrv0pZNTh_lUusWHMol0ZSDYlWO5NbJPXi2xXFUJiHkA3sFJnR8NlHH31fWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PD8N-Yq9uJ9JtXUb43NPwFMvJUiTtoIIyLbD4PHKsoMrFXI7OJHdEgCKDZkGSxk1Yt7ONDo4PEKtnYo2bkMRLiAPBzqO2Yg3TTYi3_KscP27WNz1qjzfT0u0AGQ7qMrTrrpYAvbzJibrqt_fgivV8--2YjoAOLybO3oKQLydMnaRteCMSrJKWtuMRp1OGgLUeTzqLxSYIZsxAw0Rx_pjoEcwXc-wMFI028ieucsDORFSjzYseIE-jn5OLfOo3fsN_wXA5EXDdOAs1wKdVhdFgBSg-_-vRVyqHU6A9tjMoiMx0W1OYjwu1qCrDq_uK-rhjXTgswK26eWnFjmLihnrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=neHkeRSJKVLcSbyh3D4cyKJdeHHTdrYaomTAtr0nMd2ObIxNbLOOk3GdnL2XkdcDQqMsBxDCpLYdpDa-G_IDXpuSSUdLoYQ7tEgv2keHfPWlOEXF_lPKckyCoEnrkKENTZm8q2cWGrmJnsgsFqJYwo2_yjp8_0xbU8Vlav8kC86_cwJlrTdNThGqzxIlYic-tFLARZN6x7pKRVV_eqhGv-4oUC-6341twWvUCQk4yakLbf5T-2_nEXzEZ8CBs8QU4eVTkVJecRhX4pmO9N2fh9M95KasxDsljDu7W1hZTHjOKgjuzplu90k8O27VR8ZsR9LfliaLCLJdH8Fb7PZZZlNL6BzxU3P4WmBod-t_OHsKSLE43Ejv5mCBWHMoW7ntFoNCKG79oR85cLxU_c4AzK_pmX7-7wjZWEfeU8UuQN0UL8-tGz80RyBy0pM4OpBIsi6N5c9OmaFQooBVOdJIPl9UTln0GlNznhnRTwMzniZb4E_T-GPpmXp78ePMis1IGvuckxFNVmZIihu1Gsfczb93k45FWUF3kGQRKGDVncX6g79SOZ6i8CLcB_oU3IJ-YoJROs0dhRzGnWNl4niOKU66YDx1UW7TOF7O_lcyDjhpoX9XaVy6o-W98LHKVPlUXvAMx8gGkQ_RAyrHksYTIybQn0xndZPxmju6XKiK3To" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=neHkeRSJKVLcSbyh3D4cyKJdeHHTdrYaomTAtr0nMd2ObIxNbLOOk3GdnL2XkdcDQqMsBxDCpLYdpDa-G_IDXpuSSUdLoYQ7tEgv2keHfPWlOEXF_lPKckyCoEnrkKENTZm8q2cWGrmJnsgsFqJYwo2_yjp8_0xbU8Vlav8kC86_cwJlrTdNThGqzxIlYic-tFLARZN6x7pKRVV_eqhGv-4oUC-6341twWvUCQk4yakLbf5T-2_nEXzEZ8CBs8QU4eVTkVJecRhX4pmO9N2fh9M95KasxDsljDu7W1hZTHjOKgjuzplu90k8O27VR8ZsR9LfliaLCLJdH8Fb7PZZZlNL6BzxU3P4WmBod-t_OHsKSLE43Ejv5mCBWHMoW7ntFoNCKG79oR85cLxU_c4AzK_pmX7-7wjZWEfeU8UuQN0UL8-tGz80RyBy0pM4OpBIsi6N5c9OmaFQooBVOdJIPl9UTln0GlNznhnRTwMzniZb4E_T-GPpmXp78ePMis1IGvuckxFNVmZIihu1Gsfczb93k45FWUF3kGQRKGDVncX6g79SOZ6i8CLcB_oU3IJ-YoJROs0dhRzGnWNl4niOKU66YDx1UW7TOF7O_lcyDjhpoX9XaVy6o-W98LHKVPlUXvAMx8gGkQ_RAyrHksYTIybQn0xndZPxmju6XKiK3To" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=YxAOoHuPohQ5vLwsF0kN07n2M8y--c8s_MyqLcDc7yOMNtq3-z_m4YoyPhblWFiGrfQP2afnQHbN_0fdFDGeg7duJV14AxBOyH7G7rKY5dKaYsCCDXgz_J8Mx4UzHg4cqvpLOtJOw0rAipqV2pXsZUwECvNcFFpqDcFf-XeP1tYLEehIeOzx2EboZwPioUqZXmqN4MJKYD4xiDSRPSXYp_7TgbF6tVc3FELXdO1yCBKaCIdrN7Gcg57tkJnkmQ1hxHbGzykOZZ1ipTOpKAEkrJa2-Ps5tGYgFaCqCmJ2W-_KMyLbC0lVK1jQnY-rWmvrMAv2lW9Z3-D-r_4OQu5ReA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=YxAOoHuPohQ5vLwsF0kN07n2M8y--c8s_MyqLcDc7yOMNtq3-z_m4YoyPhblWFiGrfQP2afnQHbN_0fdFDGeg7duJV14AxBOyH7G7rKY5dKaYsCCDXgz_J8Mx4UzHg4cqvpLOtJOw0rAipqV2pXsZUwECvNcFFpqDcFf-XeP1tYLEehIeOzx2EboZwPioUqZXmqN4MJKYD4xiDSRPSXYp_7TgbF6tVc3FELXdO1yCBKaCIdrN7Gcg57tkJnkmQ1hxHbGzykOZZ1ipTOpKAEkrJa2-Ps5tGYgFaCqCmJ2W-_KMyLbC0lVK1jQnY-rWmvrMAv2lW9Z3-D-r_4OQu5ReA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BVrSyXhm1yyWy_lYjwMnS7IzSQeTYA0XBCZFzvLU9i45MGvwOnI7Hp3yLGtsqktKFbZ_FtZOOp3jVfWFk-qmSd0KB_rmJEzipD8-RDC8tGagYAVYdTfMjKSN6DP49ACR4nWw8UJ5d-yOkSinEj0WnIfFBN70ZsW4PyOEQ2ZZvuU9q1j0486JWaP636uqk2DdqHl425RZvD13okh4pkmbhBQJnarTOL_XKGS3pM5xo8DOcLNCksOr_ct1_iP9acW6q0HSjnJClKoT0YU9bPxsM9e5l2IlJQ2G8qEprtc-MEuHWBYpugW5Scid8FsIYvScCo8Wix8SRr2_xUBPeECSThc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BVrSyXhm1yyWy_lYjwMnS7IzSQeTYA0XBCZFzvLU9i45MGvwOnI7Hp3yLGtsqktKFbZ_FtZOOp3jVfWFk-qmSd0KB_rmJEzipD8-RDC8tGagYAVYdTfMjKSN6DP49ACR4nWw8UJ5d-yOkSinEj0WnIfFBN70ZsW4PyOEQ2ZZvuU9q1j0486JWaP636uqk2DdqHl425RZvD13okh4pkmbhBQJnarTOL_XKGS3pM5xo8DOcLNCksOr_ct1_iP9acW6q0HSjnJClKoT0YU9bPxsM9e5l2IlJQ2G8qEprtc-MEuHWBYpugW5Scid8FsIYvScCo8Wix8SRr2_xUBPeECSThc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okmus4hnnnhQVDKkS4FYZHrWwvQ8YVaIQ9j2__EiHITy7U6tlGDsaIaZHdytucJfoAhs9lOdugFsU3UrOywiK_1vkXlYptUoHekdQdmz25YD2x6czxSv251NWAe3ILUyV8Sn3qCAnAywr5915gYOD1B0UZPZk88m4gHgHPe8NVDlUyB-ZemnSUZYOlWxlDJIhIbXg5vE9EDpC5AZsJ6dbU8hmfwni_M5EUyLJ4JrvWq7ENseCP-QQyQBHgTb3ef_-zewYwo3gSFJl5DDMygLN9akLB4YL5f3_YBythdFULvG0mhT5NP6nCBgvE0QfBJFUckEsanyxRv6eIJdLdZrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHBRPZQKi6WnBBw1tcLlA1Ok-zQoYXURyA9kHCunLnX1VwVA6XU1ZVVSRNINn4eFadjepIKvJjfeVUeiuGLZQxnN3uhxbPa-RJ-fNqzYI6ndKdAMafDiDEP_K3rzT4vNafxPu_uGTKiDhZ4qdjnuyYuq5GMwIEegFma8GSNVC1Rc5jrMyzvQ713YO8CigIgokng2fW7_Q_C8sF2Cu5PW_kal_JgWw_AEbCPX1U7SWrBOeLhGHty1ZZ3FjJIaMdyRYiq7vZFab42Cr9bPY2Ayj28ISaMGXv6nQop82cw48cQFNi9N9ji__SnKQss5fiIY8c2VBMrJv8uTCZ9QcH5qqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pypk2TH8-k7tLtvjS_bTB5yYZv5piZIm-ICIgCJDq4bm4N6hvj7Yt-efNeN1DZzSaeYuI2OH291YdOgcYu0y0h_bdRuztvoWWr_g3Rb4sA_K0aIYM79dA61uj8-LD1KmXIuhkHwKa_YVRXT0ebuBI9y6jNmkKBTDiYevrG7R4fHi43Mx21-f44Kl7UxJZYSau3whN6y_Rmq04061wGH6G3YwCZR4Vl5oG0dSNK1rHJudw08yiO53j2o6eyvUcm94UKdr86VvVAcx1v3ojJ1lcPltdAhBG2HHlPf2YlPgiXqY6AqZ85COY_FOsjgrKlv9ZZvOSwqLWcjmsQpt8FBtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NodERfnKqDwA4oWr6DjqCxWDWGefxMPfatoVOq2x2qI9OueVSq8fdil0PGMGU9YxTdgchNFBakxzwhOpHt4wvxDrIJ9WvpJusz4BjWcBdhHyPRBVuxJpvRe4rK9ECnYPOD9-wPzfBh1VgMy37Ggl5P7__warRdNwkrrEPeo3lE81ZYMOyLs774EMpUvx_9E0TZOhKZcFx6frIMBBvCZFrlCvY2G-BupMw_HhQJ-eWFpyoDzgXS89n6QElJwE8IzXYkF8F5N0X3kDwo5GSVaqt1Cr8v_KDgpS68jdnIUInrw2Me-XttBI1ijyVoi_lDkbVSLUZGvYvY8iH-i5tjbJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8oX-gIAqLf-DFMtiuxfdBDphNMFHO8eQnEFtVWP3zmgT0pLu6PmAM42YV99mpAvRlO9WchApIcd1DUu84eDESMKbV3iZCb4T5rrz8KSS80-29rvoM3LT9m3zPoRYqgbRu8JIH7Yq1rSE1UUyHL6kkK7jtPkpZPji6zlYYFEjUw2F0NwVjMFRbNzTjGJVyBFiJsLmizylC25cA0oRQ6ogeEZF0q67tzXVIvjrHQ3Xj6kMyBMlwMtIXRKVjlbMkKHeyUXNK1BnvxowzQl3J38BlSGUwE-d4KiRNT8qvosOL3HhMR3Pbq4H-62u5-B2AsK5l-Xie2za6tzNnoEiYZuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3MJEkCESgtTbQ4ZZ_TnCaYLDQxloKLRHhPzL34DjiFT3C6kD-mR-zrYsVJxWbz5WtYeCUpL10Oibw7yc4cVjgD6uZ7Vwr-_BfIbtLfWpp3cVKNns1_Ynh-xOTqEBvYWmiX43AbFFo66QpukSzU0cprYKqTnXPsgtvA5F7J2gqM32-yTcwSlUeWp9w-exP9TgwDxYAzRiQ93AV_AdOjr_MVdS9cA5IzatQjF9A10jGKgeehd8pTs_wkV-jF5b5T6pUvJG29Cp5ZdKUhkjmHB1yb_626OvFlS8TajHm__0EZihlkH8YzdjDBmDks5nuw-up3x8Kuvqe-Ak7PY4DEWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsaH63HHW8kyoqvjMEmeu6WbZRfQ6T2Oj7aNqUkI6qBZ4PhnLEq2Iz9Gm-qZpkG0E21FtD9_W2rt4lLLIG4a47O53OZU6J_MOxMvw7-5Fwq0xyg7Vrx05Ox3HdQ6zLOUZsUOi241A2CRQ2M9YxrgFdSGQpmsORDiEJxHlEA4Lf5WL2Jnza6hMq-5yZuqSvqjkkCiolutChf5vtb6XHRvEcn-Qp87czaFBsRpPmT7MjwP07WPV-AXETTDnTm_W5EaFvLr9mcS53E1WYamxF6cBHL_KdWOMO1HbZ7yF3mVuDkvxwV21CFgf9ncKbCMS0nMxq2fq-W9LH3GT45mubarDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwyMPyK6Abo3RvsLwrlklnSPAAVPi5FX3yNDgYow-bVfGmqY_MjVU8gf0bcqnOCyz5_D74saSWomZNUJg809kjjJeTxM_xGgCSKjAXlhoTXxBE9ANEVBZvJV5cKqIcimkPhHRSFW-UQfAaZN1XCNNKONN0Y2gNN0lndPI4_If4YpP5lb1m-_iE5rymPUg2msldrFw2fUwtaxekfC6_lNnSajy3CEFfjFJA-dvD3hS2laE3AvuDSvM_U_YzFkaFzo6SUiGi_mmSudM6DKnrRSxW79QCYNUF6g84gUUZkEI7pWjRqs_o4QxkK-9DJeH3ZQ8IkeDs14U3NKPAAYyXBOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJuBOjDaYCvmWqMh0GfmIT5-3ev1tHicaQd_mfdhHqYCoKCVeEUYyzRuY3cIjs8A-c6t87nDFTXH8tDB0V6IFzWJ-YfqxJI6yNFg0dfeoWOaNLZz2ewM9xs-HmaXHJuG6FaenKhoOG1hUNCWCLKa6874LXu90165Ox5V4vfXZUecadrtfD-yhmmpkavbFUyYEMKjywBCCxxc238a1MdMWzQMXSLH1ardORwY9FTLOizpSpZF_LALO7HaJxeglN384_YvH84Xpl86-VyapHqKIInQwp2LBv-ZKuM7Mddp9e6DG1IH3kNAsDhOgFZOzvWipGH1JeQDSQuOWRCLQYijjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjNdlog0zm6LxB2W-IWt6Z--o_U4DrpkPVt6PN8UC8fXMDOSVjc8DIVz3GGLuWnOPbBF8kHHSAdO6o1zmJl0myI3wElCnhQlwejMRuWPrM5VxHlbIFdEEwlGoX-CqZdgayhavZkj2QZHI5svj7tPZWYHlp-HQfaM9cQCgLBRjOQoW-7LxWKHEpxbBHHfttXWHBQYVAp4yxoVoaaX1mkYsq7Gm1_JlgxmjkKeURSlUOir7sd51FkJu2Fo0I_2gT9auN7pHXpOUpPcPQlTr69kVciqel6XlpyFncoiJTAxJEUZt0Cvd0g4h_q2io37qQVlxchOCVx-coqb04PixW1MNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qt8xUVJqh3WHxiCwYqq1RskD8amGxR8FBlSgWNSK9b6ISmmwBToLAS2aacxtCJlIUxCwP-gdlKo1mRbLTSC6ZMmimEpYS7ijhgIlV_fXfhRGRKQcfmdWA17ThaurbiZ6VXWnOH6kRzIUwRN6FoDwyiJBVvEJ9U0r8Y60Z42J_lzhu2d92yMMXrZh0YyD7K4jpuy8UUKLIEochXvlXjBflO6iLMHLQNlcoYI0ew9IQEvgxOu6EYk1qxIkI8XbxPZW3wRlL1Fpytyk_B5NWsHf7opminbKZzt2blMtcZlffiq4laySwpNPvsSyzH25vJAtsiriS0AT6rnVW-smfsFgSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofkTY9mMpovJsKEvZGRWmHyuKY4KZUG_YFin0OLO1p8BzhTsul0ugD3NPsWH4-EZ4XOqpClVduDOQRQQQLtnr7mHogAgmyL_BJbyA36rTircrzhdVUzkTOPtVKrVYb6vQEcDuQdvwljSblDJ30u2Jd3IU9a4eO-J5pMtg23F5zDyvb-pewKQUKH88-1vc1s6PC1T6zEf4DyYELU4C7ADiRX0WW77oHJfdobOLxAhZ8YQAaCVOTV6hc2B7MFbgYiZXWOpxjjJdUwn5wUbjQf2vxQ_Y6zIRcFqMycJjYpaxXSF5tjLF_1fKnqK7QDAcLojnYsZAxwlZYh1ciKZlZ5myw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=OtmY0SVqgmc32Zl5cu7V9RbqF4uOtVoO70lu5DIPJp6tnJuGK34TC3TQkL55oGpy9Yp-fY0Ihph9ZiTNwNuYfJSrt1YofYFE7PLHsY_BNm5LJRl7bZRmb42HvBIX5g4cDZD3kiAIb9oR5Nkva-DZK_bApm9dsSe-jpnbvlkBosvZbZYAf7Tw7R2lE_leOcS_QMgZpchYQb3p5LKItf-oelVe8bDmF0qJ67e5dUiX_8xE7z0dYHbfoIX3TeSJSaMCjqtxGnnh11DhpaFkfY2wL4ymoICoAbA-MZtewB9j7iLKhwh4DXVCkEU6j06JQb1CItSwjMKHC86EcXlOyWQ_p0hcsYHYc4qk8DASPqlmWalcrgbDZDUkuTZD3qL2pk6qOSBsUzwyeqvDbizfHeb9GGW03TqVX1WgiXBu3A7vztoHhXPhsdnkc-tnNt2UFIvaeZqV71e9PDvsQ-EQkKlHG1R7rsgUBx77dtJz_2xo_A27cFU6s-qUZLsVrQatI2vttArXJgBtJytv-59MX8K_vGxA8nw4-ZwgR6hkRTTB15s_Zyv3QvQxjL8dV4QRHkOkmgg7cQGutwMMmKGHd9nZpk9TBbxKo2aj8Z2LAkNIM2EkXPoF7vkUr6Ic6yVmvZ-9kvTTBf2cSTIYbUiWEgAbLbjN4u42dU9QGxV2DCeh9wM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=OtmY0SVqgmc32Zl5cu7V9RbqF4uOtVoO70lu5DIPJp6tnJuGK34TC3TQkL55oGpy9Yp-fY0Ihph9ZiTNwNuYfJSrt1YofYFE7PLHsY_BNm5LJRl7bZRmb42HvBIX5g4cDZD3kiAIb9oR5Nkva-DZK_bApm9dsSe-jpnbvlkBosvZbZYAf7Tw7R2lE_leOcS_QMgZpchYQb3p5LKItf-oelVe8bDmF0qJ67e5dUiX_8xE7z0dYHbfoIX3TeSJSaMCjqtxGnnh11DhpaFkfY2wL4ymoICoAbA-MZtewB9j7iLKhwh4DXVCkEU6j06JQb1CItSwjMKHC86EcXlOyWQ_p0hcsYHYc4qk8DASPqlmWalcrgbDZDUkuTZD3qL2pk6qOSBsUzwyeqvDbizfHeb9GGW03TqVX1WgiXBu3A7vztoHhXPhsdnkc-tnNt2UFIvaeZqV71e9PDvsQ-EQkKlHG1R7rsgUBx77dtJz_2xo_A27cFU6s-qUZLsVrQatI2vttArXJgBtJytv-59MX8K_vGxA8nw4-ZwgR6hkRTTB15s_Zyv3QvQxjL8dV4QRHkOkmgg7cQGutwMMmKGHd9nZpk9TBbxKo2aj8Z2LAkNIM2EkXPoF7vkUr6Ic6yVmvZ-9kvTTBf2cSTIYbUiWEgAbLbjN4u42dU9QGxV2DCeh9wM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=clklE1HUN--c2jbNsPiKsGvnxBzf3knkBFPlEbrZX3CGv6zWOap6UUux6k07FrhQUR3NWOYw2vmBpQUCpkBST74ysQ2_CFCcgsQd_SecY1k6LOJyuVw93H8dZtiJ7iIduRVRucwj8K3zVEE3_z18VyoQDIGphB0ix-IG2NeQMkQvjSevFT2qCJFYC46t7K8JUneSkUAspO1t1uAEid7hMj79XKE6J9kHu8E6a9NgKoxYwwncwWFF-M6xavNPEkKH-W4AXXx-DK7nBgYSxpdq-7lWnE82BttEpsiIiOpIJXbSvxYUXfBCFL5lQ2nkRktZITbB1NK_mKE0n_5M_1vw-ZNnqllw46KZYXu0gI5MnuQajgAjKOEfQ5gXCT4nwN56x1dU6QUMAs9oDSfpI2A5QZdt81LXUF4v3F7R5WAXlFq90d3U08eRSls9RcaiuKgjwS6kmefUhm6XQGS3TQZgejlUDXzzZX2FxQvaoDR4YB0iVTz4fF2y4sURS7IfHkXwJkDbRjoEoRTOueV5oKTgHT6AWJnvrhAHgbY-ZMvOVQDjrjONhj2-vSywYcrzvRcnQiAhdTDxyz2skmEQVLsg6Qb04raximRwYgPIGmNnI8MhvJqvoK37ceLJo1XPk1nUcifzHbZuphn-loYBA670SzIotXRZA8r10hsMlqVW3Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=clklE1HUN--c2jbNsPiKsGvnxBzf3knkBFPlEbrZX3CGv6zWOap6UUux6k07FrhQUR3NWOYw2vmBpQUCpkBST74ysQ2_CFCcgsQd_SecY1k6LOJyuVw93H8dZtiJ7iIduRVRucwj8K3zVEE3_z18VyoQDIGphB0ix-IG2NeQMkQvjSevFT2qCJFYC46t7K8JUneSkUAspO1t1uAEid7hMj79XKE6J9kHu8E6a9NgKoxYwwncwWFF-M6xavNPEkKH-W4AXXx-DK7nBgYSxpdq-7lWnE82BttEpsiIiOpIJXbSvxYUXfBCFL5lQ2nkRktZITbB1NK_mKE0n_5M_1vw-ZNnqllw46KZYXu0gI5MnuQajgAjKOEfQ5gXCT4nwN56x1dU6QUMAs9oDSfpI2A5QZdt81LXUF4v3F7R5WAXlFq90d3U08eRSls9RcaiuKgjwS6kmefUhm6XQGS3TQZgejlUDXzzZX2FxQvaoDR4YB0iVTz4fF2y4sURS7IfHkXwJkDbRjoEoRTOueV5oKTgHT6AWJnvrhAHgbY-ZMvOVQDjrjONhj2-vSywYcrzvRcnQiAhdTDxyz2skmEQVLsg6Qb04raximRwYgPIGmNnI8MhvJqvoK37ceLJo1XPk1nUcifzHbZuphn-loYBA670SzIotXRZA8r10hsMlqVW3Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzLaVvzu8ZlFB5kzHRdJh3vfpZlF70PtrOtwd1qrF80wNa1K9bXGOrTteXLj8OT5LhWt70p59wGlxtITD9J3Yi7vJMS8z95-w2t7YAc8hK0OaoFQGM_4B3FDEi2fmOvExxArfo46srdtVbSPjb93BiP3xTXJePH9INrSBZ1Qn0GKjrDc5UAzFd9POxi75e53ZkI_WnVO0FdH17sj-onkafYRUtozDmMp2rEuKnPbgdEUQ9GgwIrYuC3EIRF4H8un6nqBc2mLFpqYI25KDqHiXasrUusRoMF50v-TDKDxdZk4OYdy68STW94-IMOF20N7r-ljjS6bJ16IUPVgfUq_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=YfTBoMXH6-cDiVrDIiNSQn07pPgOwSUnnJ30r15F7vXA2BoBaO0JAucAcX6ev7sqa25Jr3eb-IBt7_QKtQT7ZCTbzk5UYydKIustEKXlJr5EL5yfJRCZO33J49I6ySwtAkxvr_t1qZQMIdib2i8IKREGW6cvOa8iPPPvBgDf8-3Kz1l8g78hCEzy274-xVX1a9lR43dclZhnszj7sar2JJl4l4MBEXRWEkE83jB2L2rLicEtFVBrRIRdbUTBrTLi5_3P5_hk3XIyR3u0kqJu1XO-yZ1J5XAC_LoqI2dhRD344KFhUI7NtPtxgw7S2bQ7qbQSVMlqTwGL1pEsZfe43g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=YfTBoMXH6-cDiVrDIiNSQn07pPgOwSUnnJ30r15F7vXA2BoBaO0JAucAcX6ev7sqa25Jr3eb-IBt7_QKtQT7ZCTbzk5UYydKIustEKXlJr5EL5yfJRCZO33J49I6ySwtAkxvr_t1qZQMIdib2i8IKREGW6cvOa8iPPPvBgDf8-3Kz1l8g78hCEzy274-xVX1a9lR43dclZhnszj7sar2JJl4l4MBEXRWEkE83jB2L2rLicEtFVBrRIRdbUTBrTLi5_3P5_hk3XIyR3u0kqJu1XO-yZ1J5XAC_LoqI2dhRD344KFhUI7NtPtxgw7S2bQ7qbQSVMlqTwGL1pEsZfe43g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=XVr6LuaoQEH-yRWYYrnC1_ncVoTNMvgUJvrn9e4FBtmipNlTbPtSO_KnD_2hhLnJrBEwplY2VJ8aN-mHAWR4FDsuS2lyb62lmKTkiIUnWmula4XvbzmyA1nBbnCiOfpTX8WDOw_gECwVsyEuqnFWx7uYxYUYZ55TPPRk2gGDfeCzePv_4M1LvrjWuhFd9eNLExF18FT62s27iBaOJMCsEOcmzHe4fsuoqrRBuPAPf019Lg9OtJ_El5_FPRedGjnzUa5UIQ-mtWEaZsQlPDgqlr6_LLF9kdoLTPYPCyHaZgAskqoPVLdDSWzOVOht-wBuOXpy7q0kGNkDcAXStOy3hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=XVr6LuaoQEH-yRWYYrnC1_ncVoTNMvgUJvrn9e4FBtmipNlTbPtSO_KnD_2hhLnJrBEwplY2VJ8aN-mHAWR4FDsuS2lyb62lmKTkiIUnWmula4XvbzmyA1nBbnCiOfpTX8WDOw_gECwVsyEuqnFWx7uYxYUYZ55TPPRk2gGDfeCzePv_4M1LvrjWuhFd9eNLExF18FT62s27iBaOJMCsEOcmzHe4fsuoqrRBuPAPf019Lg9OtJ_El5_FPRedGjnzUa5UIQ-mtWEaZsQlPDgqlr6_LLF9kdoLTPYPCyHaZgAskqoPVLdDSWzOVOht-wBuOXpy7q0kGNkDcAXStOy3hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gve3Qh0hTVqzb1_9dLBDuxlU5N9QKhdXFeNHEfmJFIendX4LsvyCnsHf4YleJfTj5u6JBhi9QPRHFyFTOsQu4nJi6qa_nPAUJO7Q9vDzvxnMZ0uUvZfxgD7IkgIP_CqVu30Nz3PftTl2yTuambj1tIF-P-LpN4ToSFv-HXK5tN5MlJg_j5BrDociuzlPtAOHsvHpLKdTYJECNlyxC9ipi6eZQSuoNSmEENuK1J98CicgRVh-TENTXLfbhHqZqaAmpmKje4s86sq3Jlw0wcjsTnrlXr9gy59QIZzSJf236iN4wHvMgtT1k2VFx3yFt5-LHsfpCUfbDXFQt4DeufHOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhVDGUCmkEWDVO57AsgWf_TG-8dCk9Cj3LQ31-LkyhCAlQH50HlgqQ3iSqEzPqqpgdymctQS3PqYT6LdsRmxsFJgS3r4Myr-EuuwjnKYjRp9xXjgcRhIhVUk3kUNj20G6WR-dRwtIEk0Ft1h0lwxWzv7pI86qz3w1vFEm45oDbDPuMm0OdtpvF2k0LvDqYmndIzst-dnTvyoBhymWfW6gExunJsFywLhLbLkRVXH867e5_nJfsQwe7B7UYKGJ4GHx06JOLHRnx3W9ueUGHNkM_7BDL4gdPou7-tTYGgz3MqQkByNyxJGKTnMItKFf7a7jQSpny4FKM3colmwkCelTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=EYNEPJ1cQUPwANOzNdtToLHw13q0Z_82YBSvbd-v92_ucOhncW6XFYE1qRLnGF5fFG9rmFUaDmANZUqj0Ds9kJENcNPRrQ0O0vE6d2rPEv15rNaKoYPwjup_Ylr9ZWZJN9jaRR-vUvBGgaUiqLSMcmeE4sIACyQD_62jB7AU6M5Del5JA-r3J3ecEQwE3L3acR8UrIPt_JL_aZScaKiqmY_NPnUFqbAxQQnArDd__S5uh0zky2ASgXJmgcelFCf7rRQVt8CMqsNekWU5coOq7n6ax_RyYOWyxAJ0vjCR8l8hyYx4rAvJV5ZRvniMYTYSmvJN5LqGLBdY8HmAedJOi6IKx0J3kSAMlyZlLEebFvpDlnb9OGDCbWLQwWShqGLmWs2T_swJ9wZhkf3i9Cezks1HCuIJc3RYYGBqXBzYkGPExBynoft_liBbbnbcRq_3ivVueNzmCfNGESlunGaAtRJQknVfU9LXHf4pDa-oBLM3V-gPG1MuzYpkUcOO3ltX2fxS3Jhvt2Pn7bEOroPLf1Qx31lr_6yqVkC3Nd9OGr4zLwIhmwmvmHAY30aNPz0CPy0LCJHcmpSI7h_oMotLCT8DKJFzW9K8fm-urFr_V54uzib0JPfiJ9aw0KnMppc826n_Z0BCi9VFSPmMXLydwXH78qJenWgcFpKnQtCEYBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=EYNEPJ1cQUPwANOzNdtToLHw13q0Z_82YBSvbd-v92_ucOhncW6XFYE1qRLnGF5fFG9rmFUaDmANZUqj0Ds9kJENcNPRrQ0O0vE6d2rPEv15rNaKoYPwjup_Ylr9ZWZJN9jaRR-vUvBGgaUiqLSMcmeE4sIACyQD_62jB7AU6M5Del5JA-r3J3ecEQwE3L3acR8UrIPt_JL_aZScaKiqmY_NPnUFqbAxQQnArDd__S5uh0zky2ASgXJmgcelFCf7rRQVt8CMqsNekWU5coOq7n6ax_RyYOWyxAJ0vjCR8l8hyYx4rAvJV5ZRvniMYTYSmvJN5LqGLBdY8HmAedJOi6IKx0J3kSAMlyZlLEebFvpDlnb9OGDCbWLQwWShqGLmWs2T_swJ9wZhkf3i9Cezks1HCuIJc3RYYGBqXBzYkGPExBynoft_liBbbnbcRq_3ivVueNzmCfNGESlunGaAtRJQknVfU9LXHf4pDa-oBLM3V-gPG1MuzYpkUcOO3ltX2fxS3Jhvt2Pn7bEOroPLf1Qx31lr_6yqVkC3Nd9OGr4zLwIhmwmvmHAY30aNPz0CPy0LCJHcmpSI7h_oMotLCT8DKJFzW9K8fm-urFr_V54uzib0JPfiJ9aw0KnMppc826n_Z0BCi9VFSPmMXLydwXH78qJenWgcFpKnQtCEYBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=WoMFkCSm-0QG-fEa1E7NwQAQv5hU_yMSKTVHU9NkThaHHQqSlwSSMI0bS84QxScWQyaU2uP63PItZ-o8aMn4N-NfsS2kwN592cXGHj2EOm8PXUhhJGYs2dh_rUVsOrNdie-T3jhwrZNYnC1K9HG1OO2romKA0P3xkSAquOmyZOFODNh1Vz05Tl9A86FtQMLTqiA-_YN_eyx52HlxrESWv7pu1y25XSXBCEG5hRBUCq8itaCO8OQeIZXMJbawHzOoSX0FvH56aYW3TA4XW6tr6T3ZV4RSS98uB33JmIzNP2FdaWM8gt1ewtHTAB0uaI51J44F8k2z-mJIH9o8qqvd5WyPG16YWbhQai_OkogEEF73_1q1GCKUOKfGUYoOPv9xVqaRf9Jdi8ddBAjOdpYaKlhsK1oCQTzcne1W2kvug2zSBJBU1qubg1VpRHIZLug45zzNsppI1z0OMtCkhs_MVeWZvPqLQHu3NOtvIbtnt6NNb5vsm212nIJMM4T5-FmzVHJDNZWnMVhVyv9YIqx7nizWYu7H-lxEhAhloF1SmuyvUmVefzetS89wFHgvfUsVChe-fr7Y5ZCNh3_VJSuQo7bdRj0pwpbZW3-K_5eeE2P2YrhUgEc4XR4eFwdcfVpNW5rpQ5p9jc5l8AksvHxQGXx4LzuiOEjUBUyaohMNey4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=WoMFkCSm-0QG-fEa1E7NwQAQv5hU_yMSKTVHU9NkThaHHQqSlwSSMI0bS84QxScWQyaU2uP63PItZ-o8aMn4N-NfsS2kwN592cXGHj2EOm8PXUhhJGYs2dh_rUVsOrNdie-T3jhwrZNYnC1K9HG1OO2romKA0P3xkSAquOmyZOFODNh1Vz05Tl9A86FtQMLTqiA-_YN_eyx52HlxrESWv7pu1y25XSXBCEG5hRBUCq8itaCO8OQeIZXMJbawHzOoSX0FvH56aYW3TA4XW6tr6T3ZV4RSS98uB33JmIzNP2FdaWM8gt1ewtHTAB0uaI51J44F8k2z-mJIH9o8qqvd5WyPG16YWbhQai_OkogEEF73_1q1GCKUOKfGUYoOPv9xVqaRf9Jdi8ddBAjOdpYaKlhsK1oCQTzcne1W2kvug2zSBJBU1qubg1VpRHIZLug45zzNsppI1z0OMtCkhs_MVeWZvPqLQHu3NOtvIbtnt6NNb5vsm212nIJMM4T5-FmzVHJDNZWnMVhVyv9YIqx7nizWYu7H-lxEhAhloF1SmuyvUmVefzetS89wFHgvfUsVChe-fr7Y5ZCNh3_VJSuQo7bdRj0pwpbZW3-K_5eeE2P2YrhUgEc4XR4eFwdcfVpNW5rpQ5p9jc5l8AksvHxQGXx4LzuiOEjUBUyaohMNey4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=uS7YuUX1qi3pHfZIPAU96u6Zp3zWoJxQVicyoMPZZEMP07OxKEwTqd0ErGN6PocAlN4Sh94LA07obAgAc1fdQC39DmUzd-0GOMK_-Kp5gy2cOk279K3hb598QEcn6U7UIcyICAbPhctWMscng-izJdXcK1U0-wT479Nej2rNRaLc43LCh5qkXLceppQQKxQ0soljhBYFPmQ7Sl-YEjHyTefxo3ccXtLfLzGlWGMQjwmQqd-eJBQI7YOXjGgQLDvKPIVCceDY4AeA1WFAg9thwosLyd6QoECb89Kic4KdgBalR-Z6o2Kt0x-7_0xPb7lVn2pGSdGwCDZkt2pVlG_3wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=uS7YuUX1qi3pHfZIPAU96u6Zp3zWoJxQVicyoMPZZEMP07OxKEwTqd0ErGN6PocAlN4Sh94LA07obAgAc1fdQC39DmUzd-0GOMK_-Kp5gy2cOk279K3hb598QEcn6U7UIcyICAbPhctWMscng-izJdXcK1U0-wT479Nej2rNRaLc43LCh5qkXLceppQQKxQ0soljhBYFPmQ7Sl-YEjHyTefxo3ccXtLfLzGlWGMQjwmQqd-eJBQI7YOXjGgQLDvKPIVCceDY4AeA1WFAg9thwosLyd6QoECb89Kic4KdgBalR-Z6o2Kt0x-7_0xPb7lVn2pGSdGwCDZkt2pVlG_3wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJBUfZFoC3rG_IJ_MbyfhjLcM-5mpS59c1qUDigZ_9iSPC3JK-rdrwybA_Vb9K52xOMxJo-nHmVqZIVzLnqbeD_ruzPmA3hzhx0I4Gxdxme_-Zri4vR5wv_oM6oR6V7IfOqgC2W28-LC_6WUmhmSt3AT4IcnFpEaOo1dZ8ZloNeCmfWj1sMnkO2dF1FIij9cZ279Cgvb4ivPbR5jBetD1mBmHAMWoYkPaksZ2L0EZZWuBxiU86eKCvy28eHkFeOrj4SRXGgzdcs3EEGMh8bASub_usOAKWJJ4OM55K-yJ5SuYUNZ_WRPNETthacgBy0WI8KbwIxbhgDFQKcv_yftGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=pH1Hd2CgkKy5ilh5IVGUD3BO_c2yAdu3IJnpkEcSSGaPlWsOsEdzEC5v2V90wHJt7ptNjknwH3gYyq4BXAB6s8qyvCp0VQs1T9_025C2J07mK6chIj3PySelBWf0ZKdIsVHdSns28-C9aOtFxCbnZXq8ST4AzdGaBCvZbkDgNcVs2Qte-Boilehoke_msHKPs7m9UktRcjlgU14uTxwk8x6IArqM14TsnVmi14JkVmLpo4WO3umibExDJC4eKdpg_qpQ1fE-eJn67SOo8LjKEqhs__x6gfT2N0sntuZJQq0W-cyMrZay4RY077_LtrAhJxd8_kdlQbRMdHiliE6lrSA4XkfxlM9CRWXiKUjnojgzIScgiA6X2cwfVlb3j-WyMTSiqQdLDuHaujfyqTGbATAQfCRbSTTcQwlh2aLWho734IyIIOyz49jIfTMukQKAWm2XjC3ggn2M8x1QHHiLRO1zQzKALSiJXSYdhWe5z1Wg-6Uzydv3jTdLaZQI45vNxArxEjXMymyMcbVuHkCIy7URxMD_ATEwm6Cu3JCjvxrh8z3zPTPM7ly_cvs375GQnpYE0-huklimbUF7ZNM4ZnMKnYzxKXJJT3i6Lua4C-_X99SkyO3OUC4jxB883Iys8mmCB4pKrGKN-nUrY8E23ki9QFciVQmRnyMQmp5mZ3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=pH1Hd2CgkKy5ilh5IVGUD3BO_c2yAdu3IJnpkEcSSGaPlWsOsEdzEC5v2V90wHJt7ptNjknwH3gYyq4BXAB6s8qyvCp0VQs1T9_025C2J07mK6chIj3PySelBWf0ZKdIsVHdSns28-C9aOtFxCbnZXq8ST4AzdGaBCvZbkDgNcVs2Qte-Boilehoke_msHKPs7m9UktRcjlgU14uTxwk8x6IArqM14TsnVmi14JkVmLpo4WO3umibExDJC4eKdpg_qpQ1fE-eJn67SOo8LjKEqhs__x6gfT2N0sntuZJQq0W-cyMrZay4RY077_LtrAhJxd8_kdlQbRMdHiliE6lrSA4XkfxlM9CRWXiKUjnojgzIScgiA6X2cwfVlb3j-WyMTSiqQdLDuHaujfyqTGbATAQfCRbSTTcQwlh2aLWho734IyIIOyz49jIfTMukQKAWm2XjC3ggn2M8x1QHHiLRO1zQzKALSiJXSYdhWe5z1Wg-6Uzydv3jTdLaZQI45vNxArxEjXMymyMcbVuHkCIy7URxMD_ATEwm6Cu3JCjvxrh8z3zPTPM7ly_cvs375GQnpYE0-huklimbUF7ZNM4ZnMKnYzxKXJJT3i6Lua4C-_X99SkyO3OUC4jxB883Iys8mmCB4pKrGKN-nUrY8E23ki9QFciVQmRnyMQmp5mZ3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=aoPrpk6HZyTz0609Qmzk3mWzryX8JysJ0GaLCs0WtvO8aj28jA5b-flpNqEovWz560FawJbyg3qpgKPtMjCJY1WoDUSl7LMJsKe5lJ_qUMFhJmCIBxH0gYVcAncOGujhCHvCiBN7PRGcocWQ7Zij8sHzZ77g5RzSXZAyelGiQ97H9jhLBFAUh_dZQ8TS9WLTd54CKaBGP2OunJmhzDyGmoy2RlRRnhIqhd_rj8c7wQP62h_7rufWrksJEC8YGYRLaBea5ZyBH4YihwjvgStWwFMe3QVbmsQBmo0vgahFA2F9XafTx9PfJa_7d2wRlL48W-2hIRLcs1pV9l-ID0bJRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=aoPrpk6HZyTz0609Qmzk3mWzryX8JysJ0GaLCs0WtvO8aj28jA5b-flpNqEovWz560FawJbyg3qpgKPtMjCJY1WoDUSl7LMJsKe5lJ_qUMFhJmCIBxH0gYVcAncOGujhCHvCiBN7PRGcocWQ7Zij8sHzZ77g5RzSXZAyelGiQ97H9jhLBFAUh_dZQ8TS9WLTd54CKaBGP2OunJmhzDyGmoy2RlRRnhIqhd_rj8c7wQP62h_7rufWrksJEC8YGYRLaBea5ZyBH4YihwjvgStWwFMe3QVbmsQBmo0vgahFA2F9XafTx9PfJa_7d2wRlL48W-2hIRLcs1pV9l-ID0bJRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtY5Yx5KqT0tARXgaqh2tvpZ1h8W-rCBp5qJKAPWRAk7htDBqqw4TWY1Gg2ZapUySD9hlK8g5ysfm30TQMRSO4L84php1Rqhvs82ptXbp2WH4AlXMkgt_XJC2uXFlUJo-_bg1LMIUiQHSNCA-loSOdbr2wj3-sjZoeJgvGZVbKOaAh6esTcvJ6Cij-3z5NGFVJUqzg2gov8K2nW5ws6FdomVfLaZQsX0Y-FNXKJoHONMShO40jOsHX11a1PaL1YXIGu4NvXF56VlY5xYSI_MyPmpmXQCerlH7jHVHoQ0t11SvNJhoLWlYv2aDt3pHw8kOfrw6Hr5-fRst-srTVraXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuQWXQuCKLXbK7mxOVd-aaiPNuV6boMBq0J2CCugQNut6iF47GrK_HKnux5Njt9dfZ4zdFM7bDbEdvjnHZddDhdOKhyuaXuX4YbYZJwYQ7iZiMBrviCGTD6lZQnYOt0T828J4koq__iqVQbvdRAApPXteb5Qu_4yUXfGIdrA6ZgyM2GIc_hymIuN_I8oJNDtujycutkPDmURHDUUCgLzxMtcOG2rGbh5ySZCSy7TVkQ7mK_wlB-S9_sgvdEPTHJsrwAaeW8t5xwJUCYAOMy2rnbiHA2ysLcx_gRtWDBBI4YbgK_5vgGVrHb4VJyEn40cwRQgg0m8X6qrB2JMaHEjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubA_G4RR2YIy6ED3p-BxLC9WGmkiEklW5XbgiDAAaQqFVFfQpvNzuH_EwvRLcPSeVh6fklgojnrBhrjy5vIBB1mie8UoxNE9toIMMpSQ_pMOzhZ-n3w8CmmR7JDQ6cSQ5lK3aRdL_svicrh9Et6GMhRq-dEqJG7OdpVgHqLSy77Tkef8uF1Cv5oe3NTWhv66Q17Y4cA6cEeSHZq2FCeKFSQD-is9ZpCMxB8HONDGq56GGkPlOqrZJ8HZUpUt-5fxCHH41nNbnlAfViwhaP907yNjnWieIwG7X922dUch1qgky2xTO81fgtlJkFTGeH0DBW6jF3Ej-NwawXoLkClJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7Jj8ZlmWeMDi-7fdZglVaU7d4PuxLFToCuhyGefTMQSCT2ZlalrPJ3PytF-3Iyo7dnN3ovGoTESpjUGHyrCss212mu2m7CvdAowoCDFxfkkqCnkv5zTULdG4LFR-icy8KE40qbhmv-0xDcTEkwX4q4B7Bi7AzpLaByOM529OFvCKd94csVywUsFLoj7_6sXKOxMBwS1WOXdKCVfypzY8haN0Ae9q7syg1gqLhbnek1RC14mqXQfOsklhlPau81I-DODP0YpoBsO4iLlM0C8Ro6eLfZ8anHSHnNmhrAIHnb1yzzvXOayNdqu8QTD_oWy828MTAgtzRVXa7B3JQtkPk2w8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7Jj8ZlmWeMDi-7fdZglVaU7d4PuxLFToCuhyGefTMQSCT2ZlalrPJ3PytF-3Iyo7dnN3ovGoTESpjUGHyrCss212mu2m7CvdAowoCDFxfkkqCnkv5zTULdG4LFR-icy8KE40qbhmv-0xDcTEkwX4q4B7Bi7AzpLaByOM529OFvCKd94csVywUsFLoj7_6sXKOxMBwS1WOXdKCVfypzY8haN0Ae9q7syg1gqLhbnek1RC14mqXQfOsklhlPau81I-DODP0YpoBsO4iLlM0C8Ro6eLfZ8anHSHnNmhrAIHnb1yzzvXOayNdqu8QTD_oWy828MTAgtzRVXa7B3JQtkPk2w8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byWb-QMMyPOAj4geJY205weQyF6AhxvhSi-xdP03H8od9fa8lls5YZHyY5vIN6RpjpeeY014Ly4By9cXt_RQwbglW5J3QXL_BbiOmuBhcYNZSw56LYKmED15vt0b8UqclHrTfkwq9gtF05MoGfBAHAF4YfjN36AWX0Z0MS8XWi2tEfETt_XpUFLZHB7rr2AL0i60JTslckJgW0x9p0auttaG2p9N8BL28l5Zm_0qE0I9yb0xMDTv7qr6VavHrp3-08fypRPK5ZUZO3hbzdSRCMTaats8SE-m-W-ies6-k3ZsBB8DnYZ_cF3zl-qwGvTr_BplhDhTsUsVzS2_4lVcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=D8fGKm8Ehs3n9skKCdbanzGmFfNili70ocTxljiJm_QzMw0ZHmXZFCbICa5W3eh8XP0DUTw8QHoJTtg9V9Vlv-AAyY2BhJ4AytSEeFA7qkqP5BTHvIEhu7zkBOwNuw1LeZgJQaHM6ogyIbvOONuB-ddmmjYLaMsEHjXrAu76vrcFqKysNZBaUMAmNcr89aBdJcfnOM_S0UIp86hFZQTCHudSkmRKuTmO732xvZ-tISJK9Ad8RhQAL7_2GfLYxHbh8NL1nqL0_5qit_eyft6IX79JgJIJnNygK7e8_1g2g7Y4zgmlKEQigxHUyb8EbqXeF9UkggdPeQuDcLax-Z_wBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=D8fGKm8Ehs3n9skKCdbanzGmFfNili70ocTxljiJm_QzMw0ZHmXZFCbICa5W3eh8XP0DUTw8QHoJTtg9V9Vlv-AAyY2BhJ4AytSEeFA7qkqP5BTHvIEhu7zkBOwNuw1LeZgJQaHM6ogyIbvOONuB-ddmmjYLaMsEHjXrAu76vrcFqKysNZBaUMAmNcr89aBdJcfnOM_S0UIp86hFZQTCHudSkmRKuTmO732xvZ-tISJK9Ad8RhQAL7_2GfLYxHbh8NL1nqL0_5qit_eyft6IX79JgJIJnNygK7e8_1g2g7Y4zgmlKEQigxHUyb8EbqXeF9UkggdPeQuDcLax-Z_wBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=HTU-YT_75sV-3UJCSOMH1cEupM1k7SX0KZKP3E58_db6YhNnylA0VpFsN1xQRuaztYdzBHDBF8QabY1-3eIPgRtXlkzhLECMMKj42V1P0hGHZ0v_NgeuYVGYes1SoXtjlMBvRqLO0wxDGIFmgOaOXWIKKKistSNO4qnBw1dOm15mKerqKg71kQKrgz7Eg8_CEXmXEdAYVnKUbZtZnqYUaMywwV-TBRBfc14LglXXktL3m-YW3-l0XPkPAXIaW1367DfaKKmz7cuLXrrHPtBIAqNQhuJy1r7C5IRC7MjcEezB03PQhhoyceNAxvSFjI0-K0stDI-_hXbgn0pSRPszll3daClZy7bg1PP-EQxyBJn-910MPcvSD8BYwbe6_3FBA3_zppxSDrlOOEeBUC_9gZUG-o0QKuGd7MA-lvdksfXh3IrrD3iCSZuI9O8hy5bJMrvnnTJnJFIEjjydYDJUIPJYBMJLk4y8MMz2Wdl_kiQGSSGwhu_o1nIwHrxcYQR0cV7G12RVZBdfWqRi1hXdHhBqU6fmBVFOxMXWpmitjJhv04C_I7ARMLISPQWxSPCK-TGl9WFru8sicjZziz72iPNoid-pNq8oA5gluB-us2uvmGUpATztxDBKsqftqN2b9tiZZrtpdLZSaobBSOXgHZw7MXjzZDtkq-4nNjnPzdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=HTU-YT_75sV-3UJCSOMH1cEupM1k7SX0KZKP3E58_db6YhNnylA0VpFsN1xQRuaztYdzBHDBF8QabY1-3eIPgRtXlkzhLECMMKj42V1P0hGHZ0v_NgeuYVGYes1SoXtjlMBvRqLO0wxDGIFmgOaOXWIKKKistSNO4qnBw1dOm15mKerqKg71kQKrgz7Eg8_CEXmXEdAYVnKUbZtZnqYUaMywwV-TBRBfc14LglXXktL3m-YW3-l0XPkPAXIaW1367DfaKKmz7cuLXrrHPtBIAqNQhuJy1r7C5IRC7MjcEezB03PQhhoyceNAxvSFjI0-K0stDI-_hXbgn0pSRPszll3daClZy7bg1PP-EQxyBJn-910MPcvSD8BYwbe6_3FBA3_zppxSDrlOOEeBUC_9gZUG-o0QKuGd7MA-lvdksfXh3IrrD3iCSZuI9O8hy5bJMrvnnTJnJFIEjjydYDJUIPJYBMJLk4y8MMz2Wdl_kiQGSSGwhu_o1nIwHrxcYQR0cV7G12RVZBdfWqRi1hXdHhBqU6fmBVFOxMXWpmitjJhv04C_I7ARMLISPQWxSPCK-TGl9WFru8sicjZziz72iPNoid-pNq8oA5gluB-us2uvmGUpATztxDBKsqftqN2b9tiZZrtpdLZSaobBSOXgHZw7MXjzZDtkq-4nNjnPzdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=LEfjHuZWeql_GJxP9Fkf8RMGSsU-13YG0V0Vj98lfh8e6t_Lkn9q4UDW2A4_DLc0i05KngejB-gWqsqV9Nj7bZQzZs1bFSrpUB0jqehWB9GYwiXy6ZOWgel0pLtO_BzkVBWi4k2zfbZXEwORjJzSl_y9GipAkpK-uKIy8SA3Yx2hRZtJFSir2p3oW1TzMf7k6oo5u3kcgmL5m29UEOFt7oA1_2_7al2pyxpUE3X-OkR_JiXZpnhdJ7zACL_9Lay4DGSEuwy1pGbifYK6EvsO_kriVsv6uGkWg__ubwCWl_HGXe5hzPRoDAFkEBAvcGmAo_jpvTBng0NCQgzMvzx_3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=LEfjHuZWeql_GJxP9Fkf8RMGSsU-13YG0V0Vj98lfh8e6t_Lkn9q4UDW2A4_DLc0i05KngejB-gWqsqV9Nj7bZQzZs1bFSrpUB0jqehWB9GYwiXy6ZOWgel0pLtO_BzkVBWi4k2zfbZXEwORjJzSl_y9GipAkpK-uKIy8SA3Yx2hRZtJFSir2p3oW1TzMf7k6oo5u3kcgmL5m29UEOFt7oA1_2_7al2pyxpUE3X-OkR_JiXZpnhdJ7zACL_9Lay4DGSEuwy1pGbifYK6EvsO_kriVsv6uGkWg__ubwCWl_HGXe5hzPRoDAFkEBAvcGmAo_jpvTBng0NCQgzMvzx_3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChPpG6Rp20Nc2HT7MGRJgE-MSXy5fzWrHNOQrJi1QDRZjHD6JDQ_b8rUYP6I4DWoMCAchcZK7q_HFG0JjoI_6r1i5l2tedtfJA7CwQ9U5iDm2cH2PbYKfDQt-FcSKr0z4AMGF0qSx3ENkzl7Y9wYd8VL9ZfQAzwKIp28KtarcUP_V6QQCmUi8wHbpAir-TrRbeeWlR7OMMcIISczCOAiEGiSbFAMsw3HjPRptROtahy4phIB-ToUxzK0bLI6-XxL-AbXP2tEBIx_EfnodSAxuuqR0ShYSOV-sfP5bO_JmLtUH23oVvli0VkIuTSWP-AT6FdQcZs2gkdsIRtvfWwyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=Oxtsp_1oGwYYY2fed-ohzC-ADEp8Ei3sbBqgwjlqFdQuYchA42Rf9wn0qT77snvwc1h6felR92HQm2YAVq1h5YNFJVF6KhaXs7foFV9Gu5omcL6ij7EHtUU3T8LR4om9R_KvqTZtJ74mQjVeiyySqQKAwJa-HIc009wnf-_2pM_qN75Mk1D0PXRIT2Kxq0oBNlM8DO1xHWlb15LoYx8aUtPqlDSqFYuqzlYo4SyHLICFF4htYUeqxB9NTKL366y93BviW-USGcGOxdEF_dX2KqDW7_8HZadX9gh1Y4aHtD8WBMm82iS-eTemA-_tU_bqmSiZO2BwwHwlo_Zkeji78C0qE3TyMpqDDD7FPoOoKbpBKxBzbNKO3rJq87dVgGo_lu-ftfpYsuAVTDX_wREndxEwqOnVmLEZYuf8ZtD6WYQPlAQe7EXOFZ_uSkPFinI-ExNa0q1zyMjulo2j8CftCX75mGelIm6yTN54V0QXkQ_QP8wsYX5Nth5aKRBAtJ2oOFIMviRwP0_x6bVCG7C9AhxhQ4nPmdAJbaVebVVBjcTQ_3bvJXGQs9RZEpaWb3iGTHakkwEOOaYOOILQ0_GDGMj52N1MvmPJ-z11wTMdIHDrl4myo8A46TtVRD-HR-4YR19LxbWh-cmAD585HtntgQub0i_cV3DlWTJ9YkMG-Zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=Oxtsp_1oGwYYY2fed-ohzC-ADEp8Ei3sbBqgwjlqFdQuYchA42Rf9wn0qT77snvwc1h6felR92HQm2YAVq1h5YNFJVF6KhaXs7foFV9Gu5omcL6ij7EHtUU3T8LR4om9R_KvqTZtJ74mQjVeiyySqQKAwJa-HIc009wnf-_2pM_qN75Mk1D0PXRIT2Kxq0oBNlM8DO1xHWlb15LoYx8aUtPqlDSqFYuqzlYo4SyHLICFF4htYUeqxB9NTKL366y93BviW-USGcGOxdEF_dX2KqDW7_8HZadX9gh1Y4aHtD8WBMm82iS-eTemA-_tU_bqmSiZO2BwwHwlo_Zkeji78C0qE3TyMpqDDD7FPoOoKbpBKxBzbNKO3rJq87dVgGo_lu-ftfpYsuAVTDX_wREndxEwqOnVmLEZYuf8ZtD6WYQPlAQe7EXOFZ_uSkPFinI-ExNa0q1zyMjulo2j8CftCX75mGelIm6yTN54V0QXkQ_QP8wsYX5Nth5aKRBAtJ2oOFIMviRwP0_x6bVCG7C9AhxhQ4nPmdAJbaVebVVBjcTQ_3bvJXGQs9RZEpaWb3iGTHakkwEOOaYOOILQ0_GDGMj52N1MvmPJ-z11wTMdIHDrl4myo8A46TtVRD-HR-4YR19LxbWh-cmAD585HtntgQub0i_cV3DlWTJ9YkMG-Zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=SRTOpeBpDW4UkwRfSHpkH9s754yqHCb8eY3WWZIBYSwWDMq3h7Y6Sdml3-Ux-mPFN5eJ1d7RUJD4UpIDyBWnRt2MLTQqyj4Plw3Eyxj1SRuFyerLZuBqBU5Unr5Lr6Lpl5OzmfAKqUW7tFYSPteQ0B1BNe3VQplToK2nZ7VvMj_XC78WNHyOA7yM0he06q2Ffy6NN2yOymABMo6HHmeIZj-J8pBBrG6SHzukC1asTBdvL2lXp1niY5c_auR7zS3v75_SWA0ix8x4L3J0d9GkIan0C4vdHnEn3mFfBhfWdQnpqAvB-1N3FD37o-dXLLu6-o5sfsY0soTcUoe_RjmJmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=SRTOpeBpDW4UkwRfSHpkH9s754yqHCb8eY3WWZIBYSwWDMq3h7Y6Sdml3-Ux-mPFN5eJ1d7RUJD4UpIDyBWnRt2MLTQqyj4Plw3Eyxj1SRuFyerLZuBqBU5Unr5Lr6Lpl5OzmfAKqUW7tFYSPteQ0B1BNe3VQplToK2nZ7VvMj_XC78WNHyOA7yM0he06q2Ffy6NN2yOymABMo6HHmeIZj-J8pBBrG6SHzukC1asTBdvL2lXp1niY5c_auR7zS3v75_SWA0ix8x4L3J0d9GkIan0C4vdHnEn3mFfBhfWdQnpqAvB-1N3FD37o-dXLLu6-o5sfsY0soTcUoe_RjmJmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=uW1Z25jyV28nXFD7hMj6oIMkGcDKEK_8H8VPdTM78GCnNfSDsO41rMTkbDkesL-V4AqTif0nwJr_SnEvU6jpcxz4874qrN8UAk77LTBFa3lpDRivfdqW6fefvBybFegp3VYCcWhGAhO7gfRfO77JKG7CQAlYESj4UKVds0ge50KMyi9aXAiPfMUmrrpYTx3fRQ6TL-UYcBLd5cmZw9zGQWpDZRxauiftUFJ2OUuFxD80vKql2oBfrRZHqfoFXUR6ZDsqIb2x5J5jImVkC4DV-XsKyzFeDF4bc_2YpxrmQ3ahDQZOxtzjXKWBumm2HWfUsgtBO0p7gMoufg8L7tyFew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=uW1Z25jyV28nXFD7hMj6oIMkGcDKEK_8H8VPdTM78GCnNfSDsO41rMTkbDkesL-V4AqTif0nwJr_SnEvU6jpcxz4874qrN8UAk77LTBFa3lpDRivfdqW6fefvBybFegp3VYCcWhGAhO7gfRfO77JKG7CQAlYESj4UKVds0ge50KMyi9aXAiPfMUmrrpYTx3fRQ6TL-UYcBLd5cmZw9zGQWpDZRxauiftUFJ2OUuFxD80vKql2oBfrRZHqfoFXUR6ZDsqIb2x5J5jImVkC4DV-XsKyzFeDF4bc_2YpxrmQ3ahDQZOxtzjXKWBumm2HWfUsgtBO0p7gMoufg8L7tyFew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWJ40t0keD_e7ajHUDL-lYKzV3LsRqKOwECav9T0wYghbTedXQDUdYsKf9CctX1VkR6kdodzrMJjwLfjL0gh_JQHL7rVPCvde8Q0gfrWuGsLdCveH9tICiENzQFCGlTO0T2tFNAVAIZBprfviDUfrZu2maYMdt7rJvp-iwclyi-fnNFy4cIQAR_QM5zaEa6tghoxFbGBanlpMW1lIPBZUZpC0vijr3lkylTU4sVSLnmmIuoPy0XYK_CKzStXyUI2I9DzZmIO75d56MH-Z1b7_oQ6HFU4V7fAy0Iz9w6Pzfakq9QeBxGFhikwTkQp4ilFLxxdsOcSrRWgP-NlhIhyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
