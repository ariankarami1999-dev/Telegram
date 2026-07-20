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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 16:52:31</div>
<hr>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcdmousp0lVeyaVGAmZ5EDquZe0KQ9zsmf3709S9R8ZeqxtePuTSnNDAXcUPwqbAAHKBQKXZoHHu6oJIzGuV5VAaxi6cA8wfLbAkC90h-w-mFZ0wmt0C1zNKC9k96TcPCgbpciThDLa1s3KfYo5z7IEPaWiO-1RTu3ArcS4W1HrK-zznAeqajy7Q6N_0RRiLmoTvJOSRDxyf4LVOc46SHTMfwNXtXFyVocMmTS8i8HJtNIexcnsZAnW38YOKd0WH_uonoTL1Ni_rhglNN_gL0JzM6KI-YEtIWActCDCfmGzrOVtwMoeUrxGjQBw3tbZkS35k7lSzsqbSnnbqfdYzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okuTdKje8YFPAFaFtT8iK04tvGrvGBhCNweAigICTl9Ss3tUNEnsWFHD3T8lwxrziHEaL7O7HnifRaA5bKCU7hyJUfEPc9iO6bvbB1i9qyudjd762YYstJ-EEWxNljb0gQnRllat5LadLyshVFo7sPM7NMe3zPLXFpfSXZAsodvNPMUf1xwvDbM37nYdMMJxWqkLYVArVb0icyZcVGKPskPw-fT6JP17nxMInNiwrkuKv0thzA7i_SuzJn1ATvKYmWRnFk2A1elhgbvJXmYlTQ7VlmXkZsGZZGdFrvsrLBoV1rgq-UQuOLIJACpGEZexpFm7kscXgtjXwtPOLpbedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6HOGWW58Ca8r-IfC0ijyKWBEbOMY0OfGjz7IobZkHa-aFb8m-FOHAs580oxjfI-FLULgtoG-ornyIyE6DwdizY-8jXfwlEU96jGIkjEhRK4-uB62C8Uu5FxtP6EM3yTYj805it_LJZM-BBU2IGV_xlASohq3YLaMouLrpXlq4FtHiw97YPKktgC_kN5p2NOltNH62ffMmoGfdHTK4ISX_vAd0Kfe6QcXpqMmstJ5pXI4LRBg_Jxu9qhLbRR6MenRjkUEj8p4K7e3tUIDy73L7ZcW6eOrH_r_hmBpUgANFCbiO-dcOY_CuyWzvk9QIU9TO2DfIrggBBt5vWDe1aHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDHceAws_DgHKJfPyxY_hbQFOKydTvRD8S_cgOocirT6Wx-ywl0KRXHQf6OhMNN3zocsp_m-f-qXQ5LsVUrIyAVJFqfaNc5rw6pss_ec7QVWAkSntWb2KwTWP8YwjbBOOMihz8GGAkNdJ8ch25z8QrdZado7tnLzBnW5Qe5efpv584P6L5_V7miT_QLG-SBABYenMKGWGB1YzjZ8woeN7pf2VImgkxl39Tm3qZ9YAEcN39WQJMSSSDCbPBI85r5LMCrbsCFz60xSY9D4pxmoZcKLUvjGJq3yRKS9pgyas2mT1tB2gou46k1MEs9KDv2QarRE2KF4-LjKR8PvP9KJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQTm-GORMQsHyoQA2Jfe9odBDfnVbM5wg4V5gYjcyBNcP5-N-mcPzn6CoE9Wb0cNKNhboYrr5VmCWpbBjgOua9Da7F7pXnc9pWvx_vqb95Pfy8J98qtAB8y40-DEhbThH_fxPQLv2PYX4I9L13zNe27kGLwMlHl-GrBtyRKIA5R91UYA6PSdBGFbhCoCpBOhNRMWNP6cblMKBmYyAMdgwixCp0ghnR92N84suRuHUGRzNK65D8nvMayKqteTQavqfCoYy5TsGTJYAM7_EJxKtZl9BRA_QIDnyWNICKImpt4obdRBKdmm2EDSgv7fODc27_CpxORuOeWjHQR4hFgyyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIOQVfZhz0XXHmouuOFUMaUiXc2QtDnpHgcvJ_6lMyLvPvs8vAbQMS96y4x7Fu4lDImcltyaeO8qcsieUdVVrjqKvLhVz07RWiYvEFnCkc5oEGMA-lLoYN5cDatcaY-zGj6oPI7Qm46NNOvRDBhCi4U1Jlq8OEUBy_4XnOo1zaqrfKEbt0K5KwyvFFMkdEg4g67rxaIVirQN9_0UIn_o8wFWi8hihh2gx97z3j5bs0XutuWDNU7b4xStT6ya4yX8-Ag8dIL_Q6WPFsMnI9tyJXPXa5_fgJOgJpUDHnJ7_LSTh7ubMeAxPL1wUlAXvn9ggmQQZSi1SaUNzFZR-02frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKb2WoAYB2BfZWkNY37IBbkbjJc4SIQ1g5XruVQSrsNKs3qgofww7iRVf2qoHSMHt6t6iMSSSuI5_6vfGuhUR14Gj-tuEAUG7WOMbKyyWwtPM770N2Kf7em2Ts-reWnN13h58cs7C2vy2zGJaFZBJg9S4K7sWOw2xdY7vpCzU8FrGrZBPb4ZBv2JGSw1BdmJmBzcJ5JxWICl5QqD8l_FZ-hXN96hAPs-knwNk1QmApMnpJMp45YZSZiJZLYuw5X3NAHMPzlMKAR0HCu4nBM-LypbT-i9VR58PTd4ID9ZsTDQmszlfFOJ-ihl0o_I2WCB1dabJaw2OWhHUsecid3pIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9kAc70o0QSrgOyZb3qL22pEDPiZMjZBkBuqJntjSQ47t7p_PP0-Noc4xaaXo5NBCUsq4-5Yu9fkjhdSWODDBi9d-IGRpXzI_T5aP6vNyG12r3UgICQj4ZIqEwwZxwjzbPtAgGzgoH-555Xqcgzgb2Kn1ADQUgf5b07qdvEy954mJweZIjxHF69DEeF2xMtsXHZyiBQ6hh_J9q5hRgkBRVz7-tESoEC7bROUf8JgYqMuz_tNk0JMX0Dv43zEEmnYKlupSlIw1xjczVun7Jlz4gkYqniOiZwTSlWnKs4ioTkPoinSzwgZEKRv7EWCCzrqrN0T2JyCSrQ2PwwvqSXadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=TZXgI32AS_SB8unOKg_otUI2CMdBIYOW7KMPEJy1Y5-zryNaPo4BPYcU87x7EpDuQ01wENxNp0ghkfUvLbceTLw-a2wQ5l6SHaFfGPSw_NuXZro-PqBq5X_Nn2P_KOvQk0mozokrtJXXXJzhkrerqt5rMTRzu7AKFeD7UN1X2nxFwlnqOH0PYT__F-Tqqj7RCbYnRw-5om5WLJRTRVUAwbDWCZ-jyTCFvN6BAiFYgY-KHylzb-3rSeNjpaRbH__tFOkxD9ZxGXv50rxGsDBZoGeKPPsCPiEGQHG0tJJHtdujOnzHYLKkI1GNRGXmyvihRZJ33k96Aq9VLwwfunvBrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=TZXgI32AS_SB8unOKg_otUI2CMdBIYOW7KMPEJy1Y5-zryNaPo4BPYcU87x7EpDuQ01wENxNp0ghkfUvLbceTLw-a2wQ5l6SHaFfGPSw_NuXZro-PqBq5X_Nn2P_KOvQk0mozokrtJXXXJzhkrerqt5rMTRzu7AKFeD7UN1X2nxFwlnqOH0PYT__F-Tqqj7RCbYnRw-5om5WLJRTRVUAwbDWCZ-jyTCFvN6BAiFYgY-KHylzb-3rSeNjpaRbH__tFOkxD9ZxGXv50rxGsDBZoGeKPPsCPiEGQHG0tJJHtdujOnzHYLKkI1GNRGXmyvihRZJ33k96Aq9VLwwfunvBrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v80nr9Qt8uaUUoKJ1EbyqLr1M8cFY1JszbNw0m6HSs1Jy-6NoGRS95JhDWMdQTl_boSId3vt4rzpOOjwetKH_TTpormmUD19vlzgGCzD-V8nGRP8WhMCNV6uY8NxZtn-lE355MKyqWbVmb1PP3CM7iOP7zPbbieM-HHFO0HABNn3AID2qqqcyXGBrqxXSZfhlmh4EDrb9b8FXuBVyb5cnndOkbxhMFNCU3cy_Z1zxuXrJbm958p0spMSGp6fZR-fiku0XT4XuX_uccOtCFi2EorupPfTkwDCBbIje_08fN98QoN6JMBeHtRRVHdpplSjIQCl4FlzCSil0CORr7qTOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGAGc68KyttOLrzoPrVw4VK8IiJ9SImkp4t96B0BPeMX4zaiVtDX6PjBy2HZHxWW-VW-4DUEjzStKo2J_YJhXLs2kKaWi4qhZrZjeCczJn5Gd3fx9fNPDORqAQ3scqPidZwGAtyjIOmXqnZXiCY7Es_Y4oxLzlsLUzAf2QAMPslNde8TFWe3ByqNWrd_qW-z49lJBNZ4ZyR9BIzaZIsVzMotqox5Q58rcCUGLDLVmEyMIGj3T3iFxPUFmIvFN3n1tsPcb3mYf52OnlBvyRlyl8ghtOYLfVJyF2ril9tEH5jYtFo_VoWx1299mHT6SA3_bnQ_ch9ngYBXsTiSJiFJ-FX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGAGc68KyttOLrzoPrVw4VK8IiJ9SImkp4t96B0BPeMX4zaiVtDX6PjBy2HZHxWW-VW-4DUEjzStKo2J_YJhXLs2kKaWi4qhZrZjeCczJn5Gd3fx9fNPDORqAQ3scqPidZwGAtyjIOmXqnZXiCY7Es_Y4oxLzlsLUzAf2QAMPslNde8TFWe3ByqNWrd_qW-z49lJBNZ4ZyR9BIzaZIsVzMotqox5Q58rcCUGLDLVmEyMIGj3T3iFxPUFmIvFN3n1tsPcb3mYf52OnlBvyRlyl8ghtOYLfVJyF2ril9tEH5jYtFo_VoWx1299mHT6SA3_bnQ_ch9ngYBXsTiSJiFJ-FX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=F6ZOuHni2W3dDdKbOR37ADMDs9gO146R1lBC5e45UWUUhYc_Jn2eRHxQUsXl0yCzs7RnBkQTptwjUd7GmVHiMOyLru2eeLoOW1U3jP786BwuxQQZ7r3OQZsLtDwP7yaQp4omLlWZJTe_8rpRtQdVoeZs72FIY5mxWXWmny3O1fzR8DzKjGr8o_QNh2SkvAuR6f_S6YkPC7JDrlBoZ25heQZNFc_Bq4K6jDnTCmPl4T-P9vOPzsH6W7tclXimeMZjHunplyUkCVkA03huwzYbpuMg8F6oe5ocoYInxMrDe6WUed797v2yxXze3AIlJkAYe-5kByif32kEQ9iuZbFHSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=F6ZOuHni2W3dDdKbOR37ADMDs9gO146R1lBC5e45UWUUhYc_Jn2eRHxQUsXl0yCzs7RnBkQTptwjUd7GmVHiMOyLru2eeLoOW1U3jP786BwuxQQZ7r3OQZsLtDwP7yaQp4omLlWZJTe_8rpRtQdVoeZs72FIY5mxWXWmny3O1fzR8DzKjGr8o_QNh2SkvAuR6f_S6YkPC7JDrlBoZ25heQZNFc_Bq4K6jDnTCmPl4T-P9vOPzsH6W7tclXimeMZjHunplyUkCVkA03huwzYbpuMg8F6oe5ocoYInxMrDe6WUed797v2yxXze3AIlJkAYe-5kByif32kEQ9iuZbFHSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BUaB5wUvZh3vyog7itS4clOMlIsOjqZgC-wJTOanM4YmVcoPsfvqrAqC-dO6pwW-eybLIcxDoc3mLpPlfgyV3Qe19NmmeRqzFHRyyP66vXWblvpEi8uRbSLgxVWgDMDXeP9v5w6PITeSKHnU9LSyy3kentRO2OJaM9TZpvL_HTBVOiULzoo7B80c9AwRrt2p3nanpsE4sRW7JdL6TdQB9rWlNK9NyQtYRD6rXQbGuUWsKR33f3rwuy88OOVHHseHA7ycWvoauGYKRLSuTImVZd5m3-g1FcrTg4aeEXvi90FhJu7sdXBDeS39GWSjaPy3eo_HwIVkOkUq7yrzvy21KLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BUaB5wUvZh3vyog7itS4clOMlIsOjqZgC-wJTOanM4YmVcoPsfvqrAqC-dO6pwW-eybLIcxDoc3mLpPlfgyV3Qe19NmmeRqzFHRyyP66vXWblvpEi8uRbSLgxVWgDMDXeP9v5w6PITeSKHnU9LSyy3kentRO2OJaM9TZpvL_HTBVOiULzoo7B80c9AwRrt2p3nanpsE4sRW7JdL6TdQB9rWlNK9NyQtYRD6rXQbGuUWsKR33f3rwuy88OOVHHseHA7ycWvoauGYKRLSuTImVZd5m3-g1FcrTg4aeEXvi90FhJu7sdXBDeS39GWSjaPy3eo_HwIVkOkUq7yrzvy21KLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2NBIoG3SO_NjeGuV5H_hieog9405KzO4Wu7ohk09A3kLToP08A2U6VEGdCYYEFoN8TpwPMWbTAmbQTvBUvHBs64N2TAHHdukcs_K-ZCMBgDzPyjV6ViNitHB94RfdCu6O0q6ws63YX4sLAR88PMHYaQY8JfkALTWB6PLgVUCwKgjV8u6-9c9ixTqGmqb6ycUn7XTNKhDM-c_hnfByAR0Bspf-Shv-dS00bB3VGiA6NQwwnbEPRjV_RG7FK_F8QWkiJgP78W7CcegXaxy6-V8ncVtxm_12KYYydgodPhiNmLKMMVDj7ko6yGgxT214S83QutGGW7Uj-7LwJSIZcl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW8TuA_rrZ9OhowJegx4NUlvbcTMemGxgV4-lFJXHew_gsW8nfQ0LNF_SUf5NaIe1Bs202dlbrkDP3iiruk2-A2vF2zfGj5whIPQmypY4Zxzobonex4XcYS35cECN2um84pUXTz8g4mCwNe5fXOzS6d4q-tMGjpUkQmM4-PZF0VuNLMgCwcomQ80G2x4joO1nAF0GNT_8bnn1nl6v-_L0r49RLZOokKXG3cOOr7QNhGVEaJfx_cpIVoEY3ZhWL9pXuYdJcMjXq5a6_GezZtultXSXeOPbMVEItsDyJRv8Q7ibsUsWCEpMyWo2c6VUMqBjeeZYY-ZVcpBz53cD6cBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pypk2TH8-k7tLtvjS_bTB5yYZv5piZIm-ICIgCJDq4bm4N6hvj7Yt-efNeN1DZzSaeYuI2OH291YdOgcYu0y0h_bdRuztvoWWr_g3Rb4sA_K0aIYM79dA61uj8-LD1KmXIuhkHwKa_YVRXT0ebuBI9y6jNmkKBTDiYevrG7R4fHi43Mx21-f44Kl7UxJZYSau3whN6y_Rmq04061wGH6G3YwCZR4Vl5oG0dSNK1rHJudw08yiO53j2o6eyvUcm94UKdr86VvVAcx1v3ojJ1lcPltdAhBG2HHlPf2YlPgiXqY6AqZ85COY_FOsjgrKlv9ZZvOSwqLWcjmsQpt8FBtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUH1iTXYzDE8LmXE--dBgCrmW2aSBPHHAhCpZ2OjkQ_RkXEEe5nVBxfXzhn_Vn5XS0bjRaTGP_5e2R0fEOkgy00u5xzNUDUoqqQSanw46IIUF8NFxK6C96fpP_DeDOqFq_AqQqIJ6i-y0knFq2l6xJIibSz0CczhnrwIi5ts_UtRDcabHLS3CdFkmjE76Z0TwGiId-zsH92AZYlBoGRfm3fGT4uBGUAORm55Mo1gpYtIC7hNOWRqyS6RIZg1e-I7MLx6DREM1WOgPdB3MUSWK8s8OEJrdQozvVn1AG_AvcGbZNbQ2h4U02HuZLDpvhVjIKnC73ZwcHdgS-Q48LZN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKsNvN3tOTRkbwVmv0T-mQOTm4tf9mLQm3WLK9Fucx6jrXxwE_e74NWVfdxWnZppbf-ExcZ-CNaqPwZT8fu90LzSEqqLXKhne9ZBDvcZsSN3Inn3aPlfNWBRBiYkpLa8DUQkxp_Ir5cCFKOrZRhZf6460QLxZyGWf-1cBatyqvr25DYyyP-kJsrIhjtEyLR9Kvx8FyNYc8exNm_7Lax0Ijxchgd-xdJ4NCgbYtxOw9B0UkrmtFchM4zQP4qNNHxrQvk1lTvfdX4-8NRTTktWeKutreLa-O_qj66JoIMLlOPuLqHv9WmD9H08yym_nztl3VJr8lmXQayPUJv-aPQzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB-PuvPvg4wGggzPcPaeqis6SlG50vZz4V8o8bc1Zu982GNtjjiwpI-fq1Vvs7RXYzcUoHEJ7ZpV_pK6r6eEr8znFAK_ngX46Er3zHdKIyuZXh_L8pHPZ8m3OtunkyyzsNGI6a1XMzZ_7GTJwtZ34zL1MnMpRGZI3NC-lPOn8xsdxuyEbvAOBfgRkdweCYn68LW2XWG-pZuhe0CX0rirQsVMIhrkmE-ShiXSpoOfv_opIP7So3Imc3siSHbcbKCOCoZ8vBsNg0q8nL5pxLk849HgzWjV7IIpvfaDwXs3eq4nSYQlAi8wRRp4WhmJL-RH72xEwYnPwtjWFAdSHnVQSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ2ipTCJ2n-yAwFvFzz9mZYplUo1LgdRBoBx3CduIr1-1CauutuV2kzwCAHphuetIp2PQuEh5ODdi_ydJPuIyteoDG6PeAPdHM5dyTF9hwYRM7Rercxrr6exyKSbQSP5AygOye3uV2OXdTgGHx-5U1SQYqE02rlpJ9RsvoOsixwzMExa8ly0AoNK3F5dCSPcjkMKw5QXIQULH9j9xyTfQOINAd9R-nqWlFx4lqhZ67mIYgK5nk8xSN_TBOLkxeIi6b_svAXsNebFLUkT7HD2JYUofKYVzEFdS8Rr-NiIRl5CAKfBGmizKguF9hcLBPayBB2S5z7QYmKE4sfeAAxQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0e4cxN5wtrwJOng1FqeVQP2Nw2bxte19ICDLMprXjPqt5O0GXfy7apP_z_amtF2avbGCrt6dNC84snR82Qq2f1lURF2yzPC4ZNIH8HfifVWP19oJ3n39WBYjFeYV1gr4i23G1tGxUB4HW9PyLkmZwmtk6DHYrA4rCLtc7GT-sw7boP6-n0gAW3L0MMFx6iY9l99KJIDSWyXG0uhLUKIdcKH8jCPfFLqUzdjLHzdHCJFDAzpsXfgR_p6l8xmXrThjmFGJsH0Th1URONwh_ypF3hV7qN1QGUzaeFj0RjZNN2RAD-0GI9dk5r5xTC4DDRtsKyRz54Fv_ucoYExybjdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC5xdZx6ubQH25wW-CLY65B2GBmNw3pFkgk9EiJ8YaofvDr-jEDUVvm6WfQrXIrxKoekUEooY_r2VP8YjEgw1V4F_4nEvZCyu4mlSCCpY5_FWUo_gsuy5TfVpqqZ9hczLzrfW4cQv04b8Av5hAQHDv6-HWJOOq1xsM0yypvBp41Gr70fV1RnWU54ebSe9xv8BGRjf24i6xigteyxVBfo9gvalG6KxUW9tSpOy4YgWhjIHd5KHh32Rn5Twm7CibskN6VqGkxbdZnDPGNRnB5LEKHWsU6J4BL32s0iV19AWRjNctXFAPChh5pr_RW1sk1CxdDAIogRDUXg2n_6we3Haw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ux7wAEo07w7r04sHo08C2XNh1bBaN84flb9PdL54dKNs6_oPo5OReJQNRBSl5-sQHWuK9EjZpGlFPmmbgLpDOyosRZZlt7vl9TpXmwwFD2qbaVaacJyAdBcjkANestIBD_ex_3ngZT6YFFvdawff3xMxi6BBkBA2M_FPcVyLdwWTQ07IZo6aW4ll6z1VW-zJMEBOANsZhl2d8bJ5AHNkvxPlLmH6-Q2vLrXUaPHDBXIK9F_dB97I7e3Btnh1DXQMNoFmQtVInPefNgfZ8aho7BW4hPu0A5UGMHjV5Ahtj9VcFVneG_c9-myHUKQ03g_JoqR-uVm4nV5ckyYGOFJz-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMLVWjxHAb1wsPC-FxRcDjp27DMAWhtZzzWv3MZitoKOYAgsLxz8eacaN8k4L7vsrBgYzATyxnwMeQaDEaCsXy-nhcSsT7asCiqNuaonbBf9l2WVvZ-7jrgWP-UFwEfz_tYW0aJSPQnEt7gGj2Iyi7avBM5H_Kzp0GCsq7YYK_z36pD64dlKbK0smLEJeUO6g78zHwL6Hhn0JOwfVkijTO-v3Yg4JWV6pcAIPv68r9J0IPo59aI866rMJ8aNZvHuQ2whQf9L2mLVVVjve9CdBgLtac36bJJllT_9TEGizzvzEO_sXVqEDRpalBn9PVj5IQZVxk9nUrROlsjC2HKreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKeCKQEMSZe-qebEjGYQkT2zHYi4POWtF18r1NmZOX2AiojKJjr67jtsJvTz6DePWvjkUh8jylmuGOMtAhqYQS6tnjWvhgaBa4JTmJKL5JGZoQv-Br2oL3YGXLlXWS4M4H8Vsv8-liQTl9lu4o7NdVYuGkpub65WLWKO7Pbvb1StKWUVpff9fZV-gnulhqUH9mFtMLWqO5yPwFGzDRDAJfu-Pj3EP5gl4Vg4PPaOf9fFg-8e69GoqjJWGC9V2d5oVCZoTwvHQY6XlffgNuM4iXWXgDvIM-C0F9gfIRyG4g2JGOmyExORF1Eg-jTSe4Ia5yiEj9I9Woc7HOxpAHMrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMBgvdUUFwXqCk6Jxhro4PDY6iZOts64qlDVhYOHPYhAKpA6Gh4gjEkR0seJ31vJz0_6HwnBlMyUUHdhLCJ7HB77USqAyKEBu4pnMSopw_MXAX1DSxxb8rsqPH-7oMt6dRlwsv2qt1A89JR4J5quQeJu3Dw_VPeXWKli0rSmJJ0hW8cRJnK7InNiYL9p4iNR6zHOt4rgLgA6EJuZgcgPwZq7S281ouqvJ-XS_PKnLtIOHdJKPVR7S-Fjiz8t0gmdKcuXdeI2b80eM2vZJRjz_kaE_IOZajNIZsej__TQjWMTd5vmaC6ry8hZhWSfvNbua49F3NKYuvR1NuvNF2Kxlw3o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMBgvdUUFwXqCk6Jxhro4PDY6iZOts64qlDVhYOHPYhAKpA6Gh4gjEkR0seJ31vJz0_6HwnBlMyUUHdhLCJ7HB77USqAyKEBu4pnMSopw_MXAX1DSxxb8rsqPH-7oMt6dRlwsv2qt1A89JR4J5quQeJu3Dw_VPeXWKli0rSmJJ0hW8cRJnK7InNiYL9p4iNR6zHOt4rgLgA6EJuZgcgPwZq7S281ouqvJ-XS_PKnLtIOHdJKPVR7S-Fjiz8t0gmdKcuXdeI2b80eM2vZJRjz_kaE_IOZajNIZsej__TQjWMTd5vmaC6ry8hZhWSfvNbua49F3NKYuvR1NuvNF2Kxlw3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=s38oQ6s-N3KNpXGNL01v0guF1XoZr7D7L62WtmBZwEkCsZlEDb3Gs0X4OkZNXp4YmAcSV_Z0tnUzd908LzkqbxZKAFv2hk1x38CmeERhIw0FMTYE6FVcC8YA-4JD4uuBEPrlCyvuDA8cl7bqeH67NX5ygn3kF9lU3SoO0z31NlKCn1wCfxOpsZWwbNphIuFiESjRR754UAIaRDhRgTqzAlB6oi39jusDiW5O2rlbosrxf9iXDWddhKE6mu1feXH1Te7bwk_bSI5RHXs1AniGfirDU8Wzt5O_cNXXNzO60SIoBFWo1Ef4Suyoa0h-44dSvQ3wY7kPp5ho_bFXOwFmOmqAX_rjoNLer3hLFtvz78h5jE5JWIvhshMDSZwYo98cmGoUriPAw_HCtdpN33PBVXrcPxEcLzSyob6ZIW98THHHNaNLxteXqIgr9s8hnu9cwzJR0jc5oiDUeVPfZ1_c-k6Ndw6okVbzAEfxV5nru6lvQXfqIEFWtqRIqu1mWTz32hKDPdBscLv9iPw59iWJfm72cHg3kKHO0z07HjWWyBVnhWd_-UaapaXKoMK4IxXp9IQcD2t44qw6wuzRYKbOTpnnwlyaHcNlhMidtFyuahdzIpADw2Vw3D3hLZ-N1WdLywGAlaFc3AGraeyDEtbLK_tI3hlNhGDCbwR1oqbCPjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=s38oQ6s-N3KNpXGNL01v0guF1XoZr7D7L62WtmBZwEkCsZlEDb3Gs0X4OkZNXp4YmAcSV_Z0tnUzd908LzkqbxZKAFv2hk1x38CmeERhIw0FMTYE6FVcC8YA-4JD4uuBEPrlCyvuDA8cl7bqeH67NX5ygn3kF9lU3SoO0z31NlKCn1wCfxOpsZWwbNphIuFiESjRR754UAIaRDhRgTqzAlB6oi39jusDiW5O2rlbosrxf9iXDWddhKE6mu1feXH1Te7bwk_bSI5RHXs1AniGfirDU8Wzt5O_cNXXNzO60SIoBFWo1Ef4Suyoa0h-44dSvQ3wY7kPp5ho_bFXOwFmOmqAX_rjoNLer3hLFtvz78h5jE5JWIvhshMDSZwYo98cmGoUriPAw_HCtdpN33PBVXrcPxEcLzSyob6ZIW98THHHNaNLxteXqIgr9s8hnu9cwzJR0jc5oiDUeVPfZ1_c-k6Ndw6okVbzAEfxV5nru6lvQXfqIEFWtqRIqu1mWTz32hKDPdBscLv9iPw59iWJfm72cHg3kKHO0z07HjWWyBVnhWd_-UaapaXKoMK4IxXp9IQcD2t44qw6wuzRYKbOTpnnwlyaHcNlhMidtFyuahdzIpADw2Vw3D3hLZ-N1WdLywGAlaFc3AGraeyDEtbLK_tI3hlNhGDCbwR1oqbCPjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPA0oK2dvg_bi4Anku5mIA7RzJs68st2oqexV_cr6B6jkeBEmeFkvizPZhrarTPRCnPNqwq71Er3UY3nlftfV90AEIKLldB62S2ROQAzgM6bbC8ZY7oUS-vocP1sgM8fvex2ent930PAx9ywRoUZtSsNucmIGwERGzmvWe95rH6n8uhFJKg2lvF0R5r3nS1UVUUuVQrgwLLZnRPDoLBgxGZehl6kJFqFU63fncwx5DRZaTCTNV43lZl8gD_hzEyCq5S2tqvxB7lSMlin8slfdCIjnlY8zlRd2dYwtVTa_M04TQa8xCsbQV2EIXegdGRq-TeL0tQkjFmsJdyAouUbKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=awLdebqGWp5lXGfFL9zhj5gYzVPcK9rVqhOzqgr3SQXYGFKKX-_Y5AuMAWxWQcBQswP3rqsSRW8rIeynVkuObOQJ9Tmpag5JpQIg0lZU1IbFOlB6T0lXlQgAzowCcYUZE1d2qk8XQLDPCMW0W4ruC5ANcBzdcAk_tx_IMAv_RML_S-mJWqj7_UzT3HVecvVjLhkROV5WO2Kq-R4FA7X3iSUqveEDRQQb3oYkUtj6YEgYbPA4LFs8AaepsmV4H8fft8Zf77Hk1DoapM4_EiLg-QRr9VL5KF6PbWwa1y-zd-qePLnx0xEsAhDwBvgzKIeRK895LXDPrsPVP2z3HqJVTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=awLdebqGWp5lXGfFL9zhj5gYzVPcK9rVqhOzqgr3SQXYGFKKX-_Y5AuMAWxWQcBQswP3rqsSRW8rIeynVkuObOQJ9Tmpag5JpQIg0lZU1IbFOlB6T0lXlQgAzowCcYUZE1d2qk8XQLDPCMW0W4ruC5ANcBzdcAk_tx_IMAv_RML_S-mJWqj7_UzT3HVecvVjLhkROV5WO2Kq-R4FA7X3iSUqveEDRQQb3oYkUtj6YEgYbPA4LFs8AaepsmV4H8fft8Zf77Hk1DoapM4_EiLg-QRr9VL5KF6PbWwa1y-zd-qePLnx0xEsAhDwBvgzKIeRK895LXDPrsPVP2z3HqJVTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=M8CWTkoDkfJuLESI5JdJCxZB9Wrgc0ALagDdqyQcOVG_9DLgNVOupLJ-Gy7d8z9ccqfLtm9BdPJmALWUJcekYL9d8mKbdJf5KkRLzggx0i2tl2mgMtRMWtVxURiBFlnlWM3BKyNMwrHIZ0b_3kcZbU41ooYu89rQzjJTC5xh4PJACgVnsVhJH-tjIzGHUD8OpdYj1iXpTJfvMxz4QqHHLf_23qXZu0yNpJXVnJ1y7qi2vxztGqFSOLeKvolJL_oQf0VL81-FGXn9gNoUoqp9aECAqvfZqyXUNXnEw0K9IO1lu5oN9bWZ9p8zlkIJ1_uyuwMU51rgigR_ihjr-AwgqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=M8CWTkoDkfJuLESI5JdJCxZB9Wrgc0ALagDdqyQcOVG_9DLgNVOupLJ-Gy7d8z9ccqfLtm9BdPJmALWUJcekYL9d8mKbdJf5KkRLzggx0i2tl2mgMtRMWtVxURiBFlnlWM3BKyNMwrHIZ0b_3kcZbU41ooYu89rQzjJTC5xh4PJACgVnsVhJH-tjIzGHUD8OpdYj1iXpTJfvMxz4QqHHLf_23qXZu0yNpJXVnJ1y7qi2vxztGqFSOLeKvolJL_oQf0VL81-FGXn9gNoUoqp9aECAqvfZqyXUNXnEw0K9IO1lu5oN9bWZ9p8zlkIJ1_uyuwMU51rgigR_ihjr-AwgqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU5Bjz3opX9bF0lutxJ8ajZOha_DXyr509FtEk4PlTb9HRwFDE2e903YTKtTX1MjEQiTYPVZcrhSJ6LakqfJEc85EkhLnkq07PbWO-G36QIo5jBnnAQyfj-YeGAV94jU6016F-YpL0QFEle5WE1E75iDXkne-Gchvg0ZwIz0gwUxSiu1xcoxdn6ykADhS7eyxViJWPiUIwh_kyqF0cejvj-pE6oQpdb-DG8EYxIbAa49K6x-P00nU3T-M1XSuEHPqLrHqgzxMTAJ3gR-LQamRPTB0IgUUzfFaJqrWxY1kgDj5-XID9U6K29qHlLdNMWpxknyXg09NrvdFxFF5skFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STCbY4ZoQ5bI9Pnwr9nm57-f0VAywoBw5ADbmnXKNWWBmAXX3-mDddOVTTEgkFZUsSkl1-FZzoDvrCaOTw2TdBpa2RM3dBrIRWvBApKFc36AB3GoxXpG2kKDDER4YqrmyguPbIA4mVZIZ-55sxQ2FfFB1yH0yd542Q3c0MlApKM04DIS64PuruNh0i2yHJplmmNBspeSjnJtHgdp8YNbDclmAZ2vTYQwaJ8v3JMYUTE7o42Ji_WheA8teWzvY40_TtlD1btRWCLVSKD9D4FVc_5o6yql3cFb2s-5psTg_oYgT3pdYmNBUkJCsIY6nsaubP7J1ux_onKLFjjfJv5nwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=mj_MkxpERuXiKqLdlyhLYDsWfke1jymi7kgHSyhwjPQS7_4rTZczhOydpE_9WB7TS-rvCnH12p1QE92qajM8yedQa6ey4dS34Ez57vrTeaSbPycAsxWkNZ_DeoU2o99fPOUnN-evBiM6-56fhVKGUqcOlkqHiE3ksSYs6mdb33KWQfZIeSf1w6c3VjOm5dS98eKreaBnw13ExbcT8c3YlxxD69fD60XXNzQtYVhGm0JmBcKvudOX6SxEhLUxpgcjaFIzmSbuyC3kZXamiq0Db6Lz91FL-afVk4l5yCmiSJeygMSUEz8wKTmtQgEOvtuc06zKoLCtZg79sdrGxN5trwZ32WEnMRQOpAYxrhM8bgN_0Ar87LkQnmIykcBpDO2K-3fpoQGzH8LUw8jsKJZ3CYacVxvznvvaHhC0f5RkzG0LzdbjXzysn8zNt5ArEodCosAF-zdSWX7JMdQ8hduZHbrw6eIR5fu2wQOE3z0AxYbA17fzYK2HKuQrrquOww3bsYxYXJ4HZrI8GHr2o1cl1IBuEhJ2DUtuxfJkAg2hX99lXGMlgDUCniX8WHUc4v5Qh0Mvf_ACw_x-sFb6H5qNFS4yNxHcWC_iUIibwGmLZDzJD3MJMwHLVdB233-_kZ4euiECfj4X3lFdr3viH-ZoVCb3EcXWG597t5wNRsk-VR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=mj_MkxpERuXiKqLdlyhLYDsWfke1jymi7kgHSyhwjPQS7_4rTZczhOydpE_9WB7TS-rvCnH12p1QE92qajM8yedQa6ey4dS34Ez57vrTeaSbPycAsxWkNZ_DeoU2o99fPOUnN-evBiM6-56fhVKGUqcOlkqHiE3ksSYs6mdb33KWQfZIeSf1w6c3VjOm5dS98eKreaBnw13ExbcT8c3YlxxD69fD60XXNzQtYVhGm0JmBcKvudOX6SxEhLUxpgcjaFIzmSbuyC3kZXamiq0Db6Lz91FL-afVk4l5yCmiSJeygMSUEz8wKTmtQgEOvtuc06zKoLCtZg79sdrGxN5trwZ32WEnMRQOpAYxrhM8bgN_0Ar87LkQnmIykcBpDO2K-3fpoQGzH8LUw8jsKJZ3CYacVxvznvvaHhC0f5RkzG0LzdbjXzysn8zNt5ArEodCosAF-zdSWX7JMdQ8hduZHbrw6eIR5fu2wQOE3z0AxYbA17fzYK2HKuQrrquOww3bsYxYXJ4HZrI8GHr2o1cl1IBuEhJ2DUtuxfJkAg2hX99lXGMlgDUCniX8WHUc4v5Qh0Mvf_ACw_x-sFb6H5qNFS4yNxHcWC_iUIibwGmLZDzJD3MJMwHLVdB233-_kZ4euiECfj4X3lFdr3viH-ZoVCb3EcXWG597t5wNRsk-VR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=OQTWFV79Va2uV6w1q9_xUqqKtc-D7pmcq7ovkdtNEzw4q5ewKlDD3BXvFFYs13ilRVJtQtt1G5_g3rulJ9S19nIEOOlqXn-1YhULF4MK8l-jD2ofjB22kAJixGkLhgHGYT1awUkOwxPyDBxtVpwJSc54LfdGrH7na9bsx7XMLSJzY0lgHiapXaVqHnx_t0Ue-2v7Y_DvV_dLLqFadVBUqUt5iBoxnScP1eBRuKlrTrX_a_q67A04kDc45RGFLEyDLVWWUhV-y18C7oesxnwtaJPfx4i3gi5OE5IhZrqs5ybp-hMktJeC7ADQVMinFTJR5ioCv4FLWxC29-BEZUkGuV28gKxuEjf5A7P0Gn1K79DeJD6f-twX6SUaddEBeJ2FjLgGB-gY3LG6yYO3htLYtcNSBreJ0f-CxoW3d7_mcPIyjhj8QgOx7FOexKkIrjdSpTKLsT6yUeaWPD96ElK2WI4jnKSK60TxYr9hIcu0xDRF3oUbYZ_eRp1HbYSl2uH4a1Pb-65wTYyjEGI39giLR02TFqfcslGBa5QF9eEn0lPxPrkTmatALhuH4xntspdcrSAHKHS6O8Qir5q7BcM0UEj3lNXHhGIvZC5qBR7F33grXb-dw8mLkLgDMExnkLzu_jStU22LVniUUvGb6lkpOvZbLhR0YaJ6rqrIZWpGQYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=OQTWFV79Va2uV6w1q9_xUqqKtc-D7pmcq7ovkdtNEzw4q5ewKlDD3BXvFFYs13ilRVJtQtt1G5_g3rulJ9S19nIEOOlqXn-1YhULF4MK8l-jD2ofjB22kAJixGkLhgHGYT1awUkOwxPyDBxtVpwJSc54LfdGrH7na9bsx7XMLSJzY0lgHiapXaVqHnx_t0Ue-2v7Y_DvV_dLLqFadVBUqUt5iBoxnScP1eBRuKlrTrX_a_q67A04kDc45RGFLEyDLVWWUhV-y18C7oesxnwtaJPfx4i3gi5OE5IhZrqs5ybp-hMktJeC7ADQVMinFTJR5ioCv4FLWxC29-BEZUkGuV28gKxuEjf5A7P0Gn1K79DeJD6f-twX6SUaddEBeJ2FjLgGB-gY3LG6yYO3htLYtcNSBreJ0f-CxoW3d7_mcPIyjhj8QgOx7FOexKkIrjdSpTKLsT6yUeaWPD96ElK2WI4jnKSK60TxYr9hIcu0xDRF3oUbYZ_eRp1HbYSl2uH4a1Pb-65wTYyjEGI39giLR02TFqfcslGBa5QF9eEn0lPxPrkTmatALhuH4xntspdcrSAHKHS6O8Qir5q7BcM0UEj3lNXHhGIvZC5qBR7F33grXb-dw8mLkLgDMExnkLzu_jStU22LVniUUvGb6lkpOvZbLhR0YaJ6rqrIZWpGQYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=Hyb-O6f5jfFmm4fsbAFyziGa2gXn1YCzVl_uFQZwHpQ_gWfyxs6howX5ZGrKKK0iqM8c3FmjNZq9MsZ5P-gYX7FYjAW0-rz0Bgh9tSN6TbsqZk0KnmqKWnqC28frQz8JHUGgW7dj3k5PvWJGfSq0EVQwLEIcHjkjdWXN_3CGNKj4xE5cP7hi1IT6j3Aou1ThLGAJE7pboDejT-mWPEliHjA0e3Ky3CVBs0CEcGnqB2ovlWZe-szu6xRMdYVV-Vbr-cwbk1sto3rQS2fdH_FS0GJI9C20qvx8Ok9ee1k4p5xbOgv6KuRTrIK-iNo0ppqZPCm3h7SrQcGK9p9qvzRIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=Hyb-O6f5jfFmm4fsbAFyziGa2gXn1YCzVl_uFQZwHpQ_gWfyxs6howX5ZGrKKK0iqM8c3FmjNZq9MsZ5P-gYX7FYjAW0-rz0Bgh9tSN6TbsqZk0KnmqKWnqC28frQz8JHUGgW7dj3k5PvWJGfSq0EVQwLEIcHjkjdWXN_3CGNKj4xE5cP7hi1IT6j3Aou1ThLGAJE7pboDejT-mWPEliHjA0e3Ky3CVBs0CEcGnqB2ovlWZe-szu6xRMdYVV-Vbr-cwbk1sto3rQS2fdH_FS0GJI9C20qvx8Ok9ee1k4p5xbOgv6KuRTrIK-iNo0ppqZPCm3h7SrQcGK9p9qvzRIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UylDp1Zh6G2uxKVwvLZTKlxFu_lB_7NKlsaat4e_XcqKwFTVmOV0BIKgBbKbJ0aBAeRCun8DWY4-IAYvvisXMLNObJEVBnW_Y-cJO81kdH0aFq_gnrMQGpmEUGCA_ntWMz0TRtpFxD2UBdSb3LVEli7yJA_xHoTE8dGC4_So37mpLEnU5KPiSGtm4jH-4ezH52t9ITw2d94aWiZU7c56J2Hq14gLOIHzzCAdDbu_SXWf1a3LjlaVgeNUMajQVDsteymrsUAW8G93NtZhgYHaW0AXZFMjK1OFAQ4BHSgWyS1pR-5cdI2FKI8BToOxBV0c2O-VDQg2SXMR1P8wcFkIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=W1hmZNLkCLDBy33rP6FS4yBfybagBEb0-64KuRNeIb9WJhXC_mD7cudyihcm3-w05oo7zyFJu61nagvD1hOdKGB84qnVnOIN-5XiIwE8Zg0Ki2r_aOb_q5k4FBSVcHhXZt4dsTeGPYszSMVUY9ogVdcApbDUqi4NeSHBt0i5WRLj5QTXKlGdo2nJgxVOtDRMGDdN9nrczds67VjlFNs0skYx0Mh43WT_vdYnTNYZT5pRrvYkGi7WCY77zQ5U9j6RxXSt3lonRMzlv_LCvOwcZ7HKdWwNCjO5jeAMI4hntlOuJrVJg1AO7GWpsXYPrWgH4gz1qXHphaQZ3QUfQlEAdRyIvnCPMHi3R2pM72pI1B7vSSgZmm2HfaD3iu82pJJ4DU9p0AJHT0nzFBLlfmSfzauBxJQL8z-DENO2U-rHkvsGB2oGshbfDnAVlEwx-aii3TGbPytaSYwOn73umkoXhCssty1knFbQz5p_XCAvtejsNFfEj2N-AGFI_ZQadmPabiAAV6HMJIKilrHwTYvqMmU8TAGO9XnPh9I31yiES2SQSkVt7w2oQXZ8FpOMq2a9f8V9QL9Gj8vVCpLuuYMVxyTeCJw0z8MbOC5C2Wmru0HdJLonY111HGhLshXYl3oHlfTlbUk2wLtA2UVsUKUqcJOS3n-Ehq4Y-bEMC96FQw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=W1hmZNLkCLDBy33rP6FS4yBfybagBEb0-64KuRNeIb9WJhXC_mD7cudyihcm3-w05oo7zyFJu61nagvD1hOdKGB84qnVnOIN-5XiIwE8Zg0Ki2r_aOb_q5k4FBSVcHhXZt4dsTeGPYszSMVUY9ogVdcApbDUqi4NeSHBt0i5WRLj5QTXKlGdo2nJgxVOtDRMGDdN9nrczds67VjlFNs0skYx0Mh43WT_vdYnTNYZT5pRrvYkGi7WCY77zQ5U9j6RxXSt3lonRMzlv_LCvOwcZ7HKdWwNCjO5jeAMI4hntlOuJrVJg1AO7GWpsXYPrWgH4gz1qXHphaQZ3QUfQlEAdRyIvnCPMHi3R2pM72pI1B7vSSgZmm2HfaD3iu82pJJ4DU9p0AJHT0nzFBLlfmSfzauBxJQL8z-DENO2U-rHkvsGB2oGshbfDnAVlEwx-aii3TGbPytaSYwOn73umkoXhCssty1knFbQz5p_XCAvtejsNFfEj2N-AGFI_ZQadmPabiAAV6HMJIKilrHwTYvqMmU8TAGO9XnPh9I31yiES2SQSkVt7w2oQXZ8FpOMq2a9f8V9QL9Gj8vVCpLuuYMVxyTeCJw0z8MbOC5C2Wmru0HdJLonY111HGhLshXYl3oHlfTlbUk2wLtA2UVsUKUqcJOS3n-Ehq4Y-bEMC96FQw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=bn1uDdD0JPI_w2QNoUo9IbYGOYifDeijLL-D_RGQrH0P-y6UO1CUhfPC2IsCdTvPjK1OjCLA8ojeVGowLkE9IrI3z9-jlP00CSGEzHjo7zuQIb0JMvgk_29khSSczueWZZu-DUBp2aoUCAcgJcDzTgxktuWMR3t2JP8ptgejXJ45pKVe_5zzqHZ2XzhVORe1tSS7Myw4sk5LDsqrIzFVe6xWFdzTVRkwlDhmlxQr4U7uBpf3zTfazXbOD7_H6MhmrQjbolNTmk61Oz7USoClUtfhKwX_067px01XPqEj5c8o2sm_QBgu6cNChOwok27t9XDkQEHHhCr42cwlLYN4iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=bn1uDdD0JPI_w2QNoUo9IbYGOYifDeijLL-D_RGQrH0P-y6UO1CUhfPC2IsCdTvPjK1OjCLA8ojeVGowLkE9IrI3z9-jlP00CSGEzHjo7zuQIb0JMvgk_29khSSczueWZZu-DUBp2aoUCAcgJcDzTgxktuWMR3t2JP8ptgejXJ45pKVe_5zzqHZ2XzhVORe1tSS7Myw4sk5LDsqrIzFVe6xWFdzTVRkwlDhmlxQr4U7uBpf3zTfazXbOD7_H6MhmrQjbolNTmk61Oz7USoClUtfhKwX_067px01XPqEj5c8o2sm_QBgu6cNChOwok27t9XDkQEHHhCr42cwlLYN4iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF88s92VT8_ELATz_jQMWKgLAnyV30x8T2F2E2q5IhaPs4BxEljwf5Ll8mLQluu0NooYgtdnAfep9I2x8h3SOkRv9PZ50_9PvyqgwGq3XR3sup6wrgr8RDjOy8q_zH9rNTwsTeK6DDCoWon66PTPGzPnl9i-otpRmUvCVrG8o7IazTuQE96kisutv3iYyu-IyBAp7rJIotf0RvW0AQMP6RvjmF9kzxlUvg0M55R9kBjv0pWwIb8D86uy56b_cW8er6v58P1yR-K2ZqzdzCS5kNolxqAm2AHNVBH81vPHZiu-xMPK31-PW_zFb2kD_68B52346_1DamlxaNy9_MuGLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7nCJSIbBDj9A8QFzQ4r_5nrKx3RPqLxSIGb5nEYARQ52b9DaPzrUd9K6r-bF4cZTZELIEIlegu9ZyxSk1bt2TeBe7C3q4BH6kaXvbVwyYtvPdR7OOL5QglFtPB3qMRjjkK_7dYH5XfmDAeVMOiW4rZZlV-36inTy9u5ICVH2TTNAp-8CL8mTT6xgPa2t5LL91WvtHH6dk6H_MyLDj_Zw_MQ1Oy_5vk32_wM8TAFqezsEB3YalfQRmCeEDTaSVrXs7RN05h4dHh3gwZnaXdBssY47zRC-0vUhAM_-F3u0Ztl7JpSf_IjzmNNadF4ciL5SI70OF_vgW4r-ByXwbWVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8bv9JWmDtwtVWREUo9tzC7lgjZARW8mtKR5CC3yFIsnJU43LRVsjd2Z7-FLbxW-TRgOqIjEfDZMNPXiUPyk4JLPiL7Y45xvZBxo7WRBEYzKVg_SSaA9COgO707NyIRcBaCd89Xitz7HlBjYEOmcDxuEP5k655vCSldjwPMbOlqeLGdhPSMNEfcjJWZ2Yu68xqBJQy7mQQ4DWEtjbqYTNqeeKKa9sCGdBSITf7_vhbdHRbZKy8TEYNfG04MJtYTOmUsgK2LfH42weP4ZQgJJOph_J1nuxN3PAnvAVG4gffu6dNlrHfCHLVNUODqd8c3IlPvVIfXZF4SkAmBI6ksxXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JrY-42W2U_edgI_hRLNslfVU7gggyBE7xas1GYEBRw-zS-h37zc5UqXLU-L9aEP0weoHt2AGwiUpy63tpqvQlV5V1yTUWzHhY2Dsi-4kDQz9_XDl-083ryXcgLQunD4gRmCGZ7MCVgdwOLzp8sWUq2T0nf1oH6wP1vJX6bD2Xqtr2lvW6RX8-eF3XJyzMt7OPH4icUIsofMuiQMMnyNEDFljRDk2UorcPYlxLK4l38vTMvt-IdWqgV9HscynTSoMGyWSUc6e6R4UEFeGokg_4mFzjV98Z05kFeK9ZeLKoIzCTUFyxsL2c_v_Af91-ukrDkSf95RJy1rSqbjgzNCwKZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JrY-42W2U_edgI_hRLNslfVU7gggyBE7xas1GYEBRw-zS-h37zc5UqXLU-L9aEP0weoHt2AGwiUpy63tpqvQlV5V1yTUWzHhY2Dsi-4kDQz9_XDl-083ryXcgLQunD4gRmCGZ7MCVgdwOLzp8sWUq2T0nf1oH6wP1vJX6bD2Xqtr2lvW6RX8-eF3XJyzMt7OPH4icUIsofMuiQMMnyNEDFljRDk2UorcPYlxLK4l38vTMvt-IdWqgV9HscynTSoMGyWSUc6e6R4UEFeGokg_4mFzjV98Z05kFeK9ZeLKoIzCTUFyxsL2c_v_Af91-ukrDkSf95RJy1rSqbjgzNCwKZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa9V-YK9MAtXxqKqQFJB8Tb2zcCLTYos3FNym_Ckp3VvSdBXesj187gq4ASv0P-baLGZiyvXYCG4Rs9bdJzSjwtDzy4jhLIFB2F3wXJMGkzVDL0-EP83z1CRL6_E0PYluE4uOrIkg6RwUpnEZv03kcXx1mQL7dz6MmygfgkmhSFapagoXCvlp6iIEX6EwzM14PYdLYIRtJvkPgvLI496scqAmz0zk94eew-k_Tdg6n-Z4-b8bWJ_Dad-H4RPX91a_OReZjQFiRUY2BPgA2r2EFI6bueLjqAAD2DXlc9wli5VWBobl8gdQpn3QoMp4_WUEfm3OUv2wXbmVRLwsk6WuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=KeTHa_BWN_ojmHvVVfd_B3hZgbE-2cjPOrawChfseAVwFX7XstuLyEiY3hT1JgnO25XMzutnArm5ZITe5_al-zlDK03eo58zeYSB82XcorTmrt3gLwOHs4zVNtlCajoLbzbykO3UgBS-L-CvdEfP6xWBIVgXpo06gk7Sq9EhfEgT5I9l_4A14bdh7IWy_ZtzPxT_9UTVGeXuuSnLFLc7jpGVDsJq8LvosnEEHReBaD7HBBPyw0KdMJaGBm05PSEHI0g2oH06-YIY0YJ6x6VmaW_xTg2XuqSxLu7sJPuQO8-Yy4ozvDBpUUwFAnFJcHc3vO-u9Zgq3qlNNTOW5wv0hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=KeTHa_BWN_ojmHvVVfd_B3hZgbE-2cjPOrawChfseAVwFX7XstuLyEiY3hT1JgnO25XMzutnArm5ZITe5_al-zlDK03eo58zeYSB82XcorTmrt3gLwOHs4zVNtlCajoLbzbykO3UgBS-L-CvdEfP6xWBIVgXpo06gk7Sq9EhfEgT5I9l_4A14bdh7IWy_ZtzPxT_9UTVGeXuuSnLFLc7jpGVDsJq8LvosnEEHReBaD7HBBPyw0KdMJaGBm05PSEHI0g2oH06-YIY0YJ6x6VmaW_xTg2XuqSxLu7sJPuQO8-Yy4ozvDBpUUwFAnFJcHc3vO-u9Zgq3qlNNTOW5wv0hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=KZVSX4GqBGZIWQcXcnhGBwlRAPTimXO-1q48CwIhOgm04IqrZQpHxQvuH0k1EF8y-V_Mr35J1TVjUz9_m8-TPIK-oddLUKUYSD1Wvz-aDQHtPap7az4A8Ft6aJhAyCcVjGXvzphAjyIIz9ShKG89Ebh4B7lI72ddbg88Rvz_O0CXsuMOy1wwEVkA2Cb29sW9C_G7o_5WQo0E_Pcf0XZKEouSfO6i4Rgi7hLJ52yLXRj45D0YYyzc-YcqwTTWdWtSjA8mM8m-KlWkiJjrqYdeXy2lhE2CRXEZztPoj8dTtGLh0H-iBoB_vOfrdp1s0liH6nHOp61C_9ZPtkXd6cHAqxbb_vSrK2GaIloCmh86mIHM9c_3tNcZYnIx6o3qVyuQNedqfU0_f4pm1PPDkOz4UMIkQTwSMbGvzsfAvmEUjfHa0QNLv5zDbD7GyTbry8aULApFoyw38XiIhLmtzUzHn7pIO6lr26rY2fbAFC--OyohuhIzs1OM80PL9ggYhE9DFa30FRfSwAV9Jw8uUiOg0KuxXVco3qzVdjrPjCv1AG9G9pUtG10WSsuIabgKlIdFY25WP7NBbJExTkGIChq33Xp0A8j2XmraNSNbPWp9SDv4Pefn9Ol34WOIpR6ezolk7LGdosCxAa_BtIKGFLaSZImnVt3LrkxDs_RpSJtyglM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=KZVSX4GqBGZIWQcXcnhGBwlRAPTimXO-1q48CwIhOgm04IqrZQpHxQvuH0k1EF8y-V_Mr35J1TVjUz9_m8-TPIK-oddLUKUYSD1Wvz-aDQHtPap7az4A8Ft6aJhAyCcVjGXvzphAjyIIz9ShKG89Ebh4B7lI72ddbg88Rvz_O0CXsuMOy1wwEVkA2Cb29sW9C_G7o_5WQo0E_Pcf0XZKEouSfO6i4Rgi7hLJ52yLXRj45D0YYyzc-YcqwTTWdWtSjA8mM8m-KlWkiJjrqYdeXy2lhE2CRXEZztPoj8dTtGLh0H-iBoB_vOfrdp1s0liH6nHOp61C_9ZPtkXd6cHAqxbb_vSrK2GaIloCmh86mIHM9c_3tNcZYnIx6o3qVyuQNedqfU0_f4pm1PPDkOz4UMIkQTwSMbGvzsfAvmEUjfHa0QNLv5zDbD7GyTbry8aULApFoyw38XiIhLmtzUzHn7pIO6lr26rY2fbAFC--OyohuhIzs1OM80PL9ggYhE9DFa30FRfSwAV9Jw8uUiOg0KuxXVco3qzVdjrPjCv1AG9G9pUtG10WSsuIabgKlIdFY25WP7NBbJExTkGIChq33Xp0A8j2XmraNSNbPWp9SDv4Pefn9Ol34WOIpR6ezolk7LGdosCxAa_BtIKGFLaSZImnVt3LrkxDs_RpSJtyglM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=m5EEDEdw6FUpRm250TFctaQlJyxNAWD3eETxrfbTvGoWvefDOgIB3ySyewftXKNCxhr1KimuuQvF2HLpHtgN9W7-s_WCsz7k7dcbaCYMWNM5_OBv_C9tL-D67JdpkkvqWbSA8tTy-jwcksVBFiyh05X7IhYE1pHBjvK8-sNjwllt60qRBy_Kn5CWTkffZTkFF0GT8wzdCaUjNA4cFWFL3bfu3halVPdQE8sQOi0LjlJbFqNY4FrE2s2xh3MJAZ6D5rganTx8aoTVbrEgB_DRjPjN0U-8w8XrZUL6Nr0EWKzaShRRZG18biQg2IRC0SYLr0uTyqTlEmCoudXXE1YzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=m5EEDEdw6FUpRm250TFctaQlJyxNAWD3eETxrfbTvGoWvefDOgIB3ySyewftXKNCxhr1KimuuQvF2HLpHtgN9W7-s_WCsz7k7dcbaCYMWNM5_OBv_C9tL-D67JdpkkvqWbSA8tTy-jwcksVBFiyh05X7IhYE1pHBjvK8-sNjwllt60qRBy_Kn5CWTkffZTkFF0GT8wzdCaUjNA4cFWFL3bfu3halVPdQE8sQOi0LjlJbFqNY4FrE2s2xh3MJAZ6D5rganTx8aoTVbrEgB_DRjPjN0U-8w8XrZUL6Nr0EWKzaShRRZG18biQg2IRC0SYLr0uTyqTlEmCoudXXE1YzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRpPKjc4uYUN_HD3v8_szZ7CkeBs5ELe_qCfFjxlMXpWXTLgSYIyJ-V2wNdYnu5X1jzdO1j1yCKA-uJtrH56fuoKwviJFzTNTTsnvRP_SD1TQnSKuCHa0hEuk6M7CzxpEQtqwrI4WASL-AfOwka0i92oBrqqSt9K2fW9u_1z60xzpq_4bG97quElnArKX19yL8rrb5W1pHGR5EWXIi0m9gVWFrl-gjlti8wm1TJDZyR_7oORWoBmnjCZtEZf0JnmctMHdw916wmS1mBoSDtUIGCb9SWaZtMeqdTogQ_18miy-assl75BA0OvX3yZDgTzqyWsrCcmC8FA5Dlm_eMP0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=v63n7mUB7JB29NiHgg1wL2AVU50zF7WwlR8GhkwxmroV1yJuRDSB3DA4DC7aWGYh_kJ4pAL53ZTIkfzHDp4nKbzHdiSksKoctgabQdPmxtRxdUvQQn4mKvNVQoYu_vq0z8o_8ezhujFcHpeXGR9km_ChuyRm4UOKhAkNAvyfoA9w9enP98Qg_skT3rfPeEijzboijCccaRCIO9wf1A10c1SM-O9xSxgsqjXhnuHMX7hJQ-Hmqh1YLveIkChkWhk5kHrzJHYzqM2xP3M8UtzoztmRpRQbTcKy8QCNx_eID9EKvFDq2UHWk0-OE0bjHvFJ0WuVvqatLe6_A_z2e0FqpThISSPA6dff6Nssp3Mx_KyuNLMSAUDaxA8ueUuG1kGn10UmhgNGR_WAWDIEGZ_BIskqsJk-Jb8jrjhFwWaSFATWhC0u8y0oQ8j8Kab4Zpqdw2gMeLL40ZYoamq0OsyjRU2UMme_w4jKtsKRmoo4fW6PU0zMRDIPVEu5Hyt1VcyX2VIfhyhRcDCB__v3p28pLRrYU7-2o1Q0AdCDup_1odqJeHVvKGVjXe4OAwbhooBdOTx_5qVj_B1woGQZljc1bcChgsJHae2gR3pVcdP2DI_u9H5RNGzjCc_w6znpAe83IlicV0bPIZYL0h374C0i9MHiRx_otIY_rBjiQAhi5ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=v63n7mUB7JB29NiHgg1wL2AVU50zF7WwlR8GhkwxmroV1yJuRDSB3DA4DC7aWGYh_kJ4pAL53ZTIkfzHDp4nKbzHdiSksKoctgabQdPmxtRxdUvQQn4mKvNVQoYu_vq0z8o_8ezhujFcHpeXGR9km_ChuyRm4UOKhAkNAvyfoA9w9enP98Qg_skT3rfPeEijzboijCccaRCIO9wf1A10c1SM-O9xSxgsqjXhnuHMX7hJQ-Hmqh1YLveIkChkWhk5kHrzJHYzqM2xP3M8UtzoztmRpRQbTcKy8QCNx_eID9EKvFDq2UHWk0-OE0bjHvFJ0WuVvqatLe6_A_z2e0FqpThISSPA6dff6Nssp3Mx_KyuNLMSAUDaxA8ueUuG1kGn10UmhgNGR_WAWDIEGZ_BIskqsJk-Jb8jrjhFwWaSFATWhC0u8y0oQ8j8Kab4Zpqdw2gMeLL40ZYoamq0OsyjRU2UMme_w4jKtsKRmoo4fW6PU0zMRDIPVEu5Hyt1VcyX2VIfhyhRcDCB__v3p28pLRrYU7-2o1Q0AdCDup_1odqJeHVvKGVjXe4OAwbhooBdOTx_5qVj_B1woGQZljc1bcChgsJHae2gR3pVcdP2DI_u9H5RNGzjCc_w6znpAe83IlicV0bPIZYL0h374C0i9MHiRx_otIY_rBjiQAhi5ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=t-birFqv_boxOrdkl-k93jQGJzW7ZHEqxpoptrlDbidXjJvFa7jpamX_NDXL-xpy9ro92GzbGZspPIxCQ70L8bNOGN_r7AZ1glbbnqC21gHTfsUEav7B104XLrTbqfjP3EYbSjyFvNh35GAgQA7cIuDa2jru3lg0jyUji5owFaw-6rk5QYA_Af5WdebLeHHc5Sx2b5pJaE2TYvq1FYO5uMLg5ACROdHWSDv-mRNLggwKQ-P2io-_oIQLQ_7KN8hiBMKTBDAyCjJjZr3Qbs6iJRNiSAxlCXG3uO5eI7ZhUEcDmtJrbwefVDM0IyDLFD71yJomQoMv4gSXpdYXKwF64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=t-birFqv_boxOrdkl-k93jQGJzW7ZHEqxpoptrlDbidXjJvFa7jpamX_NDXL-xpy9ro92GzbGZspPIxCQ70L8bNOGN_r7AZ1glbbnqC21gHTfsUEav7B104XLrTbqfjP3EYbSjyFvNh35GAgQA7cIuDa2jru3lg0jyUji5owFaw-6rk5QYA_Af5WdebLeHHc5Sx2b5pJaE2TYvq1FYO5uMLg5ACROdHWSDv-mRNLggwKQ-P2io-_oIQLQ_7KN8hiBMKTBDAyCjJjZr3Qbs6iJRNiSAxlCXG3uO5eI7ZhUEcDmtJrbwefVDM0IyDLFD71yJomQoMv4gSXpdYXKwF64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=wBuimLnOGXJqUnzC8NboPO2a2dbLq5C10LPDMFzdrjRCxK1v4uO6dye_4ZfhF6menbFtuD-gmJD9aVa-V08pPJdyuiVzcqBNmreWDaB91QnM1EVWk9Ddd8D2baUEJEB8t8QS0FKBvaGxKbuyobkp3loIDivi40tfcSwljweLxrvo0rFv1Fj_2E3ETj91fv1QX0Ly7VkBrADRMmaOcrplB7XAmwubakkK9HZcYTNgNed87KulSg8ix_55s5q-66-xS2UYY7E4tdaYFR9eZlvnN22MEqVrS5CgzpIbGy90aXSQPNnOjkrxnKhwPoGJxolXkdVZNMilOJVTj13kPx5o2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=wBuimLnOGXJqUnzC8NboPO2a2dbLq5C10LPDMFzdrjRCxK1v4uO6dye_4ZfhF6menbFtuD-gmJD9aVa-V08pPJdyuiVzcqBNmreWDaB91QnM1EVWk9Ddd8D2baUEJEB8t8QS0FKBvaGxKbuyobkp3loIDivi40tfcSwljweLxrvo0rFv1Fj_2E3ETj91fv1QX0Ly7VkBrADRMmaOcrplB7XAmwubakkK9HZcYTNgNed87KulSg8ix_55s5q-66-xS2UYY7E4tdaYFR9eZlvnN22MEqVrS5CgzpIbGy90aXSQPNnOjkrxnKhwPoGJxolXkdVZNMilOJVTj13kPx5o2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvIPR-jGrbRifY3kgTFCwQcRZBQFWcCjqu2yPMK24VEwtHW7RztdHqsCAv3UE32_2SraPiWZrQrtfgz0SfdkcmtdtsjK9FaEtBYikDJ7WCeFrLeamCfe-nL54DT-khPiWjo4V8Wv3-mTnfqxdpFJIn08N5bqqCSgbYN8iRRxh_bHDlok9zdzkad50a-NVoAyLjM8UMCmTu2TQlFVA4oG3TclMFC8ZwEjy4REJhcHlw4a5UjfKJx2pt0NS1HGHMmAhhlrf4nzsV9iC9zB59fY6yBY8SuFO6RdVXs-zwrKUZQ7js9W8tqu8ZeW6qE_R6FgMoEAWIyDUYClZLzJz4vLxQ.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
