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
<img src="https://cdn4.telesco.pe/file/kCat4hp4X8SibgNgSZm4boPvNKWrcga-qN_PotTX_zRRI0e58PyPf9buS2iBV55ohbTa0Auq8T0ntWmPBD5iQV_I__OVm2BP3h0POV9DlPYHUkdHSpX23tAMZ9Pu4vDbcFGDtkgvkaHF7KelWVtw3ih8tav6kBnK0IaC-8n23f4_MA4qt9FypNW7hND0ShSLP0TjVSxfL7uRJkxvCobUsR2TL3kIB3ppU2j-Vv08ZtzNreWpwTaP0NEesx7uagd9sJoLnJytW0RzGZxwcstbcrAKSF337d70mYiPP1TFpuu5ApNYsdhENUAYB_un1Nk1UohkGSMgEHqV4hzdkCreLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 427K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 13:38:17</div>
<hr>

<div class="tg-post" id="msg-19561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ka4wKt_puKyFJjVlvDZnPJcR69xGDHTi6ai9Ktp6KM01dqruQ6P2ENkIuBmxJqmTkdMggUVbK9mnrgs6wX1ypCqnA1xRa7fNMMB_f6lUcpsDUkK26gUu8w8TQbcIaLsEA1dLJMLTpi1kXQRHAetqhhKfz3kmyOeeuzZCc83JIEftAeKlMoqrNVTtHeMZEiJsqJbycuy0cDYbJ62k5P0DvhjRkwizOBVLniB8-CGuGWW6dUZnf6hNU3Ffnnxu6gy87n3zF2DDwBZUVvU8ogKzG9dAk5a_bPQtP1cq5nA6mgzHWyqBBCYa4mpus5heQTwWBJ8M3ku52PSKGCxyO-E90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو هواپیمای مخوف جنگ الکترونیک EA-37B کامپاس کال دو، مقر انگلستان را ترک کرده و به سمت خاورمیانه در حرکت هستند. اگر بوداپست هستید، آسمان را نگاه کنید و عکس بفرستید.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/withyashar/19561" target="_blank">📅 13:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19560">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وال استریت ژورنال:  ترامپ در مورد ایران بیشتر به گزینه نظامی رو آورده و فعلا پلنی برای مذاکره با سران ایران نداره.
@WarRoom</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/withyashar/19560" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19559">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3197bdc163.mp4?token=RFNIwefaUrD0hT2Yg8jFiFsJzWiGQZDmjL4sjvtIlP9c7Nf_CmgNWKak_r868bU5LbdJw9UP6E6NDiw_iQWDM_oje53WDUzEFadwlALB7vcLtuAmc78D7usXWqIMMrfKeFX_N_zFPDmAhnvlrA_jRr_wIf2ZQdSJsJ1imnAEjm0rn9cLaKCr5NejkfVNPmmCt8kkU6LJrT6Tp0JhqBJHcQEoO5rvsFH_0ZdBRT8BJn5k7KhzooRWj8WskqnuPX_QVS5LvYeYGnQyWZGwu8ImFhWfdihP67zG_dE3ChpoFuwPXzbb5UubLU-3JgbuLnEe0Gsywgepz3VYfMuDpgRwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3197bdc163.mp4?token=RFNIwefaUrD0hT2Yg8jFiFsJzWiGQZDmjL4sjvtIlP9c7Nf_CmgNWKak_r868bU5LbdJw9UP6E6NDiw_iQWDM_oje53WDUzEFadwlALB7vcLtuAmc78D7usXWqIMMrfKeFX_N_zFPDmAhnvlrA_jRr_wIf2ZQdSJsJ1imnAEjm0rn9cLaKCr5NejkfVNPmmCt8kkU6LJrT6Tp0JhqBJHcQEoO5rvsFH_0ZdBRT8BJn5k7KhzooRWj8WskqnuPX_QVS5LvYeYGnQyWZGwu8ImFhWfdihP67zG_dE3ChpoFuwPXzbb5UubLU-3JgbuLnEe0Gsywgepz3VYfMuDpgRwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از خارک و نابودی 4 بالگرد آگوستا وستلند 109 متعلق به شرکت هلیکوپتری خلیج فارس که آنجا پروازهای امدادی و گشتی انجام میدادند.
@WarRoom</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/19559" target="_blank">📅 13:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19558">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvUL6rS_jP7kQZs5-LRdz7WKFxraSGXw3i7Fk2KG9DzjizuQIWlo-xQgr0eIGeD-2y1p5QoRfpBTx3lJvQgFIbNB32MdlVCGAg1B5dm1azz40UsfcYXI4jOy-udN3nLevjOGQ6B-l5S9gCMZ6N4jPmW7tYABbBnTBALGVEb3N-HQl7kJ3hlc9HOCrdW19_6h_7MBcbeUOXgjcurF1-yi6I-mgr01IlcC8YGX4oe_TqaLdykXq2DFsQ6uq5XVvMZC2hvJJG4NTEXskK2wKmw-IEjxYD3c59_5g8cMSWfOlXyNZFI6DGV8RKvWzvcKkqmi7LPQ6Tt4EzEpG6kzpDip4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیروزآباد فارس الان
@WarRoom</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/19558" target="_blank">📅 12:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19557">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏جیک تورکس، خبرنگار ارشد کاخ سفید و نیوزمکس، نوشت که به اطلاعاتی دسترسی دارد که بسیاری از افراد از آن بی‌خبرند و با اطمینان کامل می‌گوید آمریکا برای شکست رژیم جمهوری اسلامی برنامه دارد. او افزود کارشناسان از آنچه رخ خواهد داد شگفت‌زده می‌شوند و سپس وانمود می‌کنند از ابتدا همه‌چیز را می‌دانستند.
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/19557" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19556">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1807f6b87b.mp4?token=ZSWwC9mXVCCZ1eplMAPZxN9RQ1jEPGS9rIOKzV_9DHRYwHAF4mhY2CoXvQsRPGkFO3WLGJDKHm4BZl1mEbZorDctNdAlrlZ7-ojVGc67C6JzOO3C4auQbjXHOZ-0L0RAM_eu5jpqkCapUTOLBQtRmYzHdzd3MyNdeMjWzO21om5NMdJQCjLfoIlijFx64SoEuGUSOSLMbxETHT89Xb2D69TKrjZGt7pNkxZuZi-CtaO-VEXf5acFawpu9PJmPpfp7tNB668Czah-u6oZxSkkv6gj7un5mmVGHtVfBfBtrm-wt0xwItyTahz0JBsf6sYkQGhCWz7dCHgHlUDPIMTsVJh-k9-1EhdWf4PlxAwRl70J8V8yoQPI8tBieieTT1bKJV1u-CmS1kL7zzelDfRLvSG6eQSUnCiXUhHxzdNwVL3mZgzhS9RiGdOBdgpcpgUZ1gUyUVhde0PhIs1ZI4f1yHogqjDBC029U3CblCAvz7UBVZ6C2H5EhhkMJNi_t-hPJmjgQyf4E-910ZeFim07PbTtULxk-I2jsvrlDGjzP2b1Zdai5twkBqAm98zUQMIojVURASd_Ffa3E8mrOlQEdf4NOSRCKY4xq6P3dBFczIDqR-B1JvBuv9wf1a0JnSMbHeYZScgpJnHoMM0MN35jNPj7GIs8RvZRkEpA6LFBGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1807f6b87b.mp4?token=ZSWwC9mXVCCZ1eplMAPZxN9RQ1jEPGS9rIOKzV_9DHRYwHAF4mhY2CoXvQsRPGkFO3WLGJDKHm4BZl1mEbZorDctNdAlrlZ7-ojVGc67C6JzOO3C4auQbjXHOZ-0L0RAM_eu5jpqkCapUTOLBQtRmYzHdzd3MyNdeMjWzO21om5NMdJQCjLfoIlijFx64SoEuGUSOSLMbxETHT89Xb2D69TKrjZGt7pNkxZuZi-CtaO-VEXf5acFawpu9PJmPpfp7tNB668Czah-u6oZxSkkv6gj7un5mmVGHtVfBfBtrm-wt0xwItyTahz0JBsf6sYkQGhCWz7dCHgHlUDPIMTsVJh-k9-1EhdWf4PlxAwRl70J8V8yoQPI8tBieieTT1bKJV1u-CmS1kL7zzelDfRLvSG6eQSUnCiXUhHxzdNwVL3mZgzhS9RiGdOBdgpcpgUZ1gUyUVhde0PhIs1ZI4f1yHogqjDBC029U3CblCAvz7UBVZ6C2H5EhhkMJNi_t-hPJmjgQyf4E-910ZeFim07PbTtULxk-I2jsvrlDGjzP2b1Zdai5twkBqAm98zUQMIojVURASd_Ffa3E8mrOlQEdf4NOSRCKY4xq6P3dBFczIDqR-B1JvBuv9wf1a0JnSMbHeYZScgpJnHoMM0MN35jNPj7GIs8RvZRkEpA6LFBGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهر خودرو خلیج فارس در اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/19556" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19554">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بن غفیر وزیر امنیت ملی اسرائیل: به ازای هر یهودی که دشمن می‌کشد، دشمن باید متحمل از دست دادن زمین‌ها و خانه‌ها شود. من خواستار صدور دستوراتی به ارتش برای تخریب خانه‌های تروریست‌ها و حامیان آن‌ها خواهم بود. @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19554" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19553">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بن غفیر وزیر امنیت ملی اسرائیل: به ازای هر یهودی که دشمن می‌کشد، دشمن باید متحمل از دست دادن زمین‌ها و خانه‌ها شود. من خواستار صدور دستوراتی به ارتش برای تخریب خانه‌های تروریست‌ها و حامیان آن‌ها خواهم بود.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19553" target="_blank">📅 11:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19552">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رسانه های داخلی : ارتش آمریکا امروز با موشک، مقر نیروی دریایی سپاه پاسداران انقلاب اسلامی را در منطقه زیباکنار، در سواحل دریای خزر در شمال کشور، مورد حمله قرار داد. خساراتی در این منطقه وارد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19552" target="_blank">📅 11:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19551">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سپاه تروریستی که جدیدأ با اسم ارتش جمهوری اسلامی فعالیت میکند اعلام کرد که با استفاده از پهپادهای "آرش"، انبارهای تجهیزات ارتش آمریکا را در پایگاه العدری، و همچنین پادگان‌های نیروها در دوحه و تعدادی از مواضع را در پایگاه عریفجان در کویت هم اکنون مورد هدف قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19551" target="_blank">📅 11:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتاق جنگ با یاشار : ده‌ها هواپیمای باری نیروی هوایی ایالات متحده (سی-۱۷ و دیگر هواپیماهای سنگین) امروز از پایگاه‌های اروپایی به خاورمیانه پرواز می‌کنند.  این یک "پل هوایی" تمام عیار است که بعد از جنگ۴۰روزه دوباره فعال شده. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19550" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqejSnp8RvTpJDmh21OdutWFP0sAy_8aY8MkpGjXZ8H26rWZBCfw1wfFp4RmD7wfPv3qHqUaElwud2hg3IjqfZf4ACxISTW6Jq8pA0W4AxNQ8vU2bapLqZ3HxKhsSfHbp1v5tsp8gd_n6BURU6RSuHwW0iECUva2ovKJcHOOJv-BlubksJNULwrPPDsTRbODc1H_PLEYW3VxYYnQCHsgV5yOj85JbJz_5SRSIEESKXNkLJNjmbgIVyu3TLUIkwyXhmjOq7ZfdxuQ4ffJA4uaXB2UR-D9vEuniqBuA52oGmC3NBNcUQUJvIqUM0n2ArcdXT42hYdmKZMDulM9TC_57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته، دو فروند بمب‌افکن
B-1B Lancer
از پایگاه
RAF Fairford
بریتانیا تقریباً همان مسیر پروازی مأموریت
«HEINZ»
را که چند روز پیش انجام شده بود، تکرار کردند.
در این مأموریت، یکی از بمب‌افکن‌ها تا منطقه تحت
(CENTCOM)
پیش رفت، اما هواپیمای دوم حدود
۶ ساعت
پرواز کرد و سپس به پایگاه خود بازگشت.
بمب‌افکن اصلی به بمب‌های
JDAM
(بمب هدایت‌شونده ماهواره‌ای که بمب‌های معمولی را به سلاح‌های دقیق تبدیل می‌کند)
مجهز بوده است.
ترکیب مأموریت بمب‌افکن (Mission LXIV):
B-1B “PURDY30”
با شماره 86-0107 و لقب
Dragon Slayer
(اژدهاکش)
B-1B “PURDY31”
با شماره 86-0138 و لقب
Seek and Destroy
(جستجو و نابودی)
دو فروند هواپیمای سوخت‌رسان
KC-135R
با شناسه‌های
BOBBY14
و
BOBBY16
که از
LROP
(محل استقرار عملیاتی بلندبرد)
مأموریت را پشتیبانی کردند.</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19549" target="_blank">📅 10:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e7b5aa30.mp4?token=WMv7cFXFpVRKs3VzfvB4cZOvXob_mvZ7jU036TISsjZYbU41xl2vkgQkzfWe6hvxTLrFmyj38UrnzKi4YbEhCHV0RmhUc23RKtTxoOXrh5Kd56iI956Em4qleKFGQ3xKR9qPBtenLOjEkcImUtm_ggEfVpxP-7PHHK27cI41hyUjBc1Ce9h38sVFaGYPfnKonU89JTxMtxkKyzPI6bM89EHUtd3f3fXqPlPQhfW3pWabI2buGQDXwC4KEB4CQ3aYhdvt8gEr2AFnCOSse8Mii_TShRxVPVlSJORn6Tyzm5XEDvy8sKqeGmBTBTVGo3VGV8zczzhD6szXxcf4DPy2gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e7b5aa30.mp4?token=WMv7cFXFpVRKs3VzfvB4cZOvXob_mvZ7jU036TISsjZYbU41xl2vkgQkzfWe6hvxTLrFmyj38UrnzKi4YbEhCHV0RmhUc23RKtTxoOXrh5Kd56iI956Em4qleKFGQ3xKR9qPBtenLOjEkcImUtm_ggEfVpxP-7PHHK27cI41hyUjBc1Ce9h38sVFaGYPfnKonU89JTxMtxkKyzPI6bM89EHUtd3f3fXqPlPQhfW3pWabI2buGQDXwC4KEB4CQ3aYhdvt8gEr2AFnCOSse8Mii_TShRxVPVlSJORn6Tyzm5XEDvy8sKqeGmBTBTVGo3VGV8zczzhD6szXxcf4DPy2gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند
ستاد فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد نیروهای این فرماندهی،
سیزدهمین شب پیاپی حملات به ایران
را
در ساعت ۹:۰۰ شب چهارشنبه ۲۳ ژوئیه به وقت شرق آمریکا (ET)
،
(ساعت ۰۴:۳۰ بامداد پنجشنبه ۲۴ ژوئیه به وقت ایران / ۲ مرداد ۱۴۰۵)
با موفقیت به پایان رساندند.
به گفته سنتکام، در این عملیات
مراکز فرماندهی نظامی، انبارهای نگهداری پهپاد، شبکه‌های ارتباطی، سایت‌های پایش و دیده‌بانی ساحلی و توانمندی‌های دریایی ایران
هدف قرار گرفتند تا تهدیدی که ایران علیه دریانوردان غیرنظامی و کشتی‌های تجاری عبوری از
تنگه هرمز
ایجاد می‌کند، بیش از پیش کاهش یابد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19548" target="_blank">📅 04:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فعال‌سازی پدافند شرق تهران
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19547" target="_blank">📅 03:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش انفجار جاسک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19546" target="_blank">📅 03:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مدیرکل مدیریت بحران استانداری هرمزگان:
در پی حمله ارتش آمریکا به محله تپه‌الله‌اکبر بندرعباس، یک تیر برق دچار شکستگی شده و پارگی سیم برق نیز در محل حادثه رخ داده است.
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19545" target="_blank">📅 03:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کامنت برای سنتکام
😩</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19544" target="_blank">📅 03:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کنارک رو زدن
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19543" target="_blank">📅 03:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19542">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUaP2Xu3_bWjN4PjFVBh5-CDCAjwumFlixbATK_Q-4I78Y2eXAf1iNS3HPXlZMANlZ6okPXGRknQQSCnZfQDYjc71kcZ-G4UMhHjVJ25LLQx-F0b9nO8KT1Gl6riZOrFbour5Bs-AQ31F3p0Y_xh6Di8jLgHWmvagwDQOCpzikHBDPn4vEoEK1B9sXJHaFmumj36o5qfHWdDt__Nu2Vebv9li8HYKv9KERdayREs50Mgf3Ozt2i-s0C3ph8fspX3Cw9Fjozl222mo0qx71uutMEN5pcZV-R66g7Wn4Ifi90hjTcqQUMXBXaVxtLg6XqUNWc2ZnsxjQUu5PtMJXWnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش صدای انفجار خرم آباد لرستان @WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19542" target="_blank">📅 03:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش صدای انفجار خرم آباد لرستان
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19541" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19540">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2dd8c2f68.mp4?token=VCct3Yb-ahCVRnFEih7afoT2B1HHGnUb7tE9Nl_dMSy-WUyhYcSu-iJqFTKgkionTzvb8vlL57sUEoykJuwCg4ycjTGYUBrqNz5EqJIcS1NdvORfIbKWIBlT-EI-XTL7G4tPDllkE-UcAR4ycNlHC1B1ZJSU_XxZpc-SK2QFeizGaTyOuc31nBwSvQ4Q4yXt9gmAbWAxLmCdHFFAvbORvtIiKq7ZnLKmFmcGyrNuc38lMjzBd_uGzcobmoKq-6pjNZJRTbr6HTlhvX-PrdWuACTalEPv1udhu3WXw2Yp875PkFQEnRUYtsfZwl5QHoNzbcopx5gSKHxFnhqDbQXPWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2dd8c2f68.mp4?token=VCct3Yb-ahCVRnFEih7afoT2B1HHGnUb7tE9Nl_dMSy-WUyhYcSu-iJqFTKgkionTzvb8vlL57sUEoykJuwCg4ycjTGYUBrqNz5EqJIcS1NdvORfIbKWIBlT-EI-XTL7G4tPDllkE-UcAR4ycNlHC1B1ZJSU_XxZpc-SK2QFeizGaTyOuc31nBwSvQ4Q4yXt9gmAbWAxLmCdHFFAvbORvtIiKq7ZnLKmFmcGyrNuc38lMjzBd_uGzcobmoKq-6pjNZJRTbr6HTlhvX-PrdWuACTalEPv1udhu3WXw2Yp875PkFQEnRUYtsfZwl5QHoNzbcopx5gSKHxFnhqDbQXPWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19540" target="_blank">📅 03:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19539">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19539" target="_blank">📅 03:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19538">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش انفجار چابهار
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19538" target="_blank">📅 03:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19535">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88de0012c3.mp4?token=Hy25yT3MJMe7T4DDK3XsdtNuXrtvl-oxlUWbWQdc-gEgFZRgQMK3laYz8QOcJOQFmt5sNexsrqiM8E6LTj02WoG21AuBkG3IxyDwrqOs5RbHp9g-vZ6snRIwpWdY6ma856_skBWLC85fETPFwZZt5wVwVuOPj3MiJbn4UozM8Uh9UvjoZhrMX9fmQ-ZL2Jtig512N8KfbEa4gz9PXTWMgrjijrw-8jwTQEBQY46ZneJY5ZonB0dN_YXHUxs9kTWgq3H4PrtcOkeuWJc5N1kJgahxxsumehl_rKdfFqY6CeWmDo_2M_DmFbH6qpwrEfH64XlcKHCUsZ5jH63rbARABA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88de0012c3.mp4?token=Hy25yT3MJMe7T4DDK3XsdtNuXrtvl-oxlUWbWQdc-gEgFZRgQMK3laYz8QOcJOQFmt5sNexsrqiM8E6LTj02WoG21AuBkG3IxyDwrqOs5RbHp9g-vZ6snRIwpWdY6ma856_skBWLC85fETPFwZZt5wVwVuOPj3MiJbn4UozM8Uh9UvjoZhrMX9fmQ-ZL2Jtig512N8KfbEa4gz9PXTWMgrjijrw-8jwTQEBQY46ZneJY5ZonB0dN_YXHUxs9kTWgq3H4PrtcOkeuWJc5N1kJgahxxsumehl_rKdfFqY6CeWmDo_2M_DmFbH6qpwrEfH64XlcKHCUsZ5jH63rbARABA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19535" target="_blank">📅 03:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانال ۱۴ : طرح‌های احتیاطی و تخلیه اضطراری وزارت امور خارجه ایالات متحده در سراسر جهان پس از تهدیدهای رئیس جمهور ترامپ مبنی بر حمله شدید به تأسیسات هسته‌ای مستحکم کوه پیکاکس ایران منتشر شد. از آنجا که این مجموعه در اعماق سنگ‌های سخت دفن شده است، تحلیلگران دفاعی می‌گویند واشنگتن در صورت هدف قرار گرفتن این سایت با استفاده از سلاح‌های غیرمتعارف، خود را برای انتقام شدید نظامی ایران یا حملات تروریستی آماده می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19533" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19532">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش انفجار قشمممم
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19532" target="_blank">📅 02:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19531">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734a91582b.mp4?token=c_IbFyfAZKLOjobVh00knDS1FV5sdk-YWjfNsSsStimdW3dJo9P2JKh2gUVzunGvCq4RgKqRHRZLzSZ-Aap1X55MfjzHFTrB3aswkYF0Kz43vv4C1S5sj79ORnqECKjORtXWoCz1a4md6gHIacFwJcgFzIEzcnXXJ7wAJqGqg5Tb7iBvkBv2r1pRQOHPkG0V3wroNYsHDEb1TLlQG85LSmqI1_Js3BaeNh2nkCO_9n1PB9mGhKFwTQL0zi2MOa80eqvZ0qkzg85NZG9C6SfOvqEjfSMjXlcVrc8xneagh1wQa1hjt4c3bYMOpECAs0oBNbli_tUS6yqGvzm_n0QLxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734a91582b.mp4?token=c_IbFyfAZKLOjobVh00knDS1FV5sdk-YWjfNsSsStimdW3dJo9P2JKh2gUVzunGvCq4RgKqRHRZLzSZ-Aap1X55MfjzHFTrB3aswkYF0Kz43vv4C1S5sj79ORnqECKjORtXWoCz1a4md6gHIacFwJcgFzIEzcnXXJ7wAJqGqg5Tb7iBvkBv2r1pRQOHPkG0V3wroNYsHDEb1TLlQG85LSmqI1_Js3BaeNh2nkCO_9n1PB9mGhKFwTQL0zi2MOa80eqvZ0qkzg85NZG9C6SfOvqEjfSMjXlcVrc8xneagh1wQa1hjt4c3bYMOpECAs0oBNbli_tUS6yqGvzm_n0QLxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز کل شهر شد دود
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19531" target="_blank">📅 02:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19525">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1d891257.mp4?token=eHC8Rl6JKLNpel6ATcYQVis2RtfjYa_Y3A2YxX3Cup1TBD-mF0p_GqTDQTlZKGoUp536EGoYC8JDuRGXGN92r9vQkyaI5oSckm9Jo2Uqq3YuHlLbhGktBnCR-c2ntaRBnf1nROdgm5N4xewHXQGbY4sqJHoCkVRLAksOkX5FsO6nQ9cqAF5di5M-29mW3bIgeWIMvEbOPMRAS001EZfa_4excMVriW4Dv6p6U3OKOIrv0JW5ySbGR6-hyAXyleMuRubGVW3MKo81R5AehmZwPDQCRsGc44tI54pDQvjVZoR7BUNVGrA6DcMvw4OBs3TwQc1Wh0nhU5QQ2jHULl40Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1d891257.mp4?token=eHC8Rl6JKLNpel6ATcYQVis2RtfjYa_Y3A2YxX3Cup1TBD-mF0p_GqTDQTlZKGoUp536EGoYC8JDuRGXGN92r9vQkyaI5oSckm9Jo2Uqq3YuHlLbhGktBnCR-c2ntaRBnf1nROdgm5N4xewHXQGbY4sqJHoCkVRLAksOkX5FsO6nQ9cqAF5di5M-29mW3bIgeWIMvEbOPMRAS001EZfa_4excMVriW4Dv6p6U3OKOIrv0JW5ySbGR6-hyAXyleMuRubGVW3MKo81R5AehmZwPDQCRsGc44tI54pDQvjVZoR7BUNVGrA6DcMvw4OBs3TwQc1Wh0nhU5QQ2jHULl40Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم های اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19525" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19524">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سنتکام : شب ۱۳ هم شروع شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19524" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19523">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19523" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19522">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بندر عباس شروع شد
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19522" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19521">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLWv032y2qkYds5s6hNlYuzJh28Iumq9P594K431Yr8D1VFKNGMAGZ54lGmtSCJ8fcRzWXswOVYVpfX27aEwvyR4fGwguGNQaMtO-Y_NWtL7beFEwZAgweYzY-z6RiS6JfYuXvMPwFTJpf_tRc--nKwxPFVZTFGz60vElDEy2yo7hjoK_KD18YNWklZMG-__jCdZr6f89RXvHBB-s0-UR_HYRapxou9r3DlB10ojGz7Db2fDZeBQXhy_u7jgf7MfSYK0UwvTXx1mowvYmkYTOdrY2KwuyXTjJ7FBlT9z_NA0pH3987pLqvM9xk-iRYxmCCkVpkLsGix7X3zuhZ_2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : بمباران اهواز توسط هواپیمای بمب افکن B-1
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19521" target="_blank">📅 02:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19520">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19520" target="_blank">📅 02:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19519">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19519" target="_blank">📅 02:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19518">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اتاق جنگ با یاشار : سرطان  حتما تا اخر ببینید و نظرتون رو کامنت کنید میخونم کارای اداری یادتون نره مخصوصا اد تو استوری و ریشیر  https://www.instagram.com/reel/DbJowDnR54h/?igsh=MW0yMnB5cG5pa2FyNQ==</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19518" target="_blank">📅 02:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19517">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19517" target="_blank">📅 02:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19516">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اهواز‌ ادامه داره همچنان….</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19516" target="_blank">📅 02:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19515">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اهواز انفجار ها زیاد بود حتی‌ بیشتر از ۱۰ عدد گزارش شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19515" target="_blank">📅 02:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">۳ انفجار مهیب اهواز
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19514" target="_blank">📅 02:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19513">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اهوازمممم زدن بدددددم زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19513" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدای انفجار رگبرای قشم
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19512" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19511" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شروع شدددددد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19510" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال ۱۴ : ارتش ایران، ستاد ارتش کویت را هدف قرار داد. این اقدام پس از ادعاهای ایران مبنی بر اینکه نیروهای کویتی مستقر در این پایگاه، پیش از این گذرگاه مرزی شلمچه را هدف قرار داده بودند، صورت می‌گیرد. اخبار تکمیلی متعاقباً اعلام خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19509" target="_blank">📅 02:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d7eae30c1.mp4?token=QfZkhWzm524ZKJ3h7c0FI5UoMr759sxoYNklzFpScUiqgz0UyNAX7rKUlVrawk8BEWp9--nQWzOjUGdSXeDSsbH8ZaC8uJQMdbXSBT4oIe_ptKxgSjE_Gt3gO20r507ek2SBPfm8zoXipDG_2nBNvev8A0tGNt3thTTzyCCTZwb1LpzqAe9g2SFnWb6NbaL3MhqzRuyiC2VHzuQyAffU0ElYMzmt050jzC4GepwE8bYlbWcEgSIo8PXBJsDvY_55M6R6roEiIjF753fWJqgByIL4KSXaDggOJ9a2WzQZIbKcl2t2V9eXddpcNRKpsXMPAijoHk8k1GV_nlxb5NCRyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d7eae30c1.mp4?token=QfZkhWzm524ZKJ3h7c0FI5UoMr759sxoYNklzFpScUiqgz0UyNAX7rKUlVrawk8BEWp9--nQWzOjUGdSXeDSsbH8ZaC8uJQMdbXSBT4oIe_ptKxgSjE_Gt3gO20r507ek2SBPfm8zoXipDG_2nBNvev8A0tGNt3thTTzyCCTZwb1LpzqAe9g2SFnWb6NbaL3MhqzRuyiC2VHzuQyAffU0ElYMzmt050jzC4GepwE8bYlbWcEgSIo8PXBJsDvY_55M6R6roEiIjF753fWJqgByIL4KSXaDggOJ9a2WzQZIbKcl2t2V9eXddpcNRKpsXMPAijoHk8k1GV_nlxb5NCRyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط شیء پرنده ناشناس در قشم
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19508" target="_blank">📅 02:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5CiEKqv3pWjNaCZ8dba4u1Tq4jiZSHAwcKnSFwwa2pK2yMkt_xYpmRQyHkPOfWpJB06OKABMC-kmDDzEsRsNs7ihaUjQ6PFXCUqE_-iPulyk5R5iZXblxIOAwm09cMLK0VTnuZm8fxcBdp000c-Fnk8boJLJDDvDWeQAW0FpUf2RgKZABSqzwv_ooSZU4-O-SInhkp3smLjgiDrywk-yb5t3Xk96F_1Vuqi9B4BHfBITzFWGWZU4xoqdJPE-gDDx1XPGSNy_GrV-niXNz1gDekUDPuBcfmWsxEqocvomq7BWv3D8UhxAtxkVV8eaEmlnGGG3DreMEZ1tzXf4phJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث
:
از این لحظه به بعد، هرگونه خسارتی که به کشتی‌ها، کالاها یا هر چیزی مرتبط با آن‌ها وارد شود، از طریق وجوه متعلق به ایران که در حال حاضر در اختیار ایالات متحده قرار دارد جبران خواهد شد.
ممکن است این خسارت‌ها قابل‌توجه باشند، اما با وجود این، این اقدام عادلانه و درست است و باید انجام شود.
از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19507" target="_blank">📅 01:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19506" target="_blank">📅 01:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برمیگردم
😉
من جنگامو کردم که اومدم اتاق جنگ</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19505" target="_blank">📅 01:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awBvn2izt9i7LImIVjRbNUdM060hqXkPQKuH3g2nFAjQ0ym_4xizOdshs8sNpLTA5B8BSJD7EShvHdhgm8dq8ci-lcfTZEoTUK6LI_UFsVveMzxrExsL-GHk82USYHIydlMQTxPnltOf_f_7x3xmQ1gOGPKmfEG0FO_mbvxsTnv1VJhs-hizRzfRUj4yxSgjPF8hVdl7uPFTB1_Yhr5cJs1UUYOl8IZoXsylttTBri5j6JBq7M2e1cchsN-eXR11GCeKSvKEUsXtRDHUkWTlO3EIpbZhA83Au4G8ZfBDFYmB44sSJ6BsjTw4nYazktZF2kuFLjr0Ftifn7eSWS0dIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : سرطان
حتما تا اخر ببینید و نظرتون رو کامنت کنید میخونم
کارای اداری یادتون نره مخصوصا اد تو استوری و ریشیر
https://www.instagram.com/reel/DbJowDnR54h/?igsh=MW0yMnB5cG5pa2FyNQ==</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19504" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش انفجار های شدید و پیاپی در تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19503" target="_blank">📅 01:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پرتاب موشک‌های کروز ضدکشتی به سمت تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19502" target="_blank">📅 00:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیویورک تایمز:نخست‌وزیر عراق، در جریان سفر خود به تهران، پیشنهادی را ارائه کرده بود مبنی بر برقراری آتش‌بس بین ایران و ایالات متحده
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19501" target="_blank">📅 00:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ایران به پاکستان هشدار داده است:درصورت وقوع هرگونه حمله تروریستی علیه ایران، با تمام توان و قدرت خود دست به اقدام تلافی‌جویانه خواهد زد
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19500" target="_blank">📅 00:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۳ عبری: نهادهای اطلاعاتی غرب بر این باورند که ممکن است ایران آغازگر اقدام علیه اسرائیل باشد
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19499" target="_blank">📅 00:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd98bed83.mp4?token=SKJzKF2cSXaU9Oa0tdTSIuCB2__0kConMySSkPHGDvCtVYYdynuSd3JTjlRw5Mk1o_ISfOQwZHK_0QEl6GjGdGg3OeKkzh0QJHitJ4VaXLXWTYvYKuWXni7gPTSw9xN5X37pxd-qcdS8QJJb5eJ4dCByaAWFSrLu9sAVWblZBEtBFd_0sbBZ53vjkenNsQIPJnxvt92lpNILWFhzA68Q5sIVqzCyciCwM_I7VvShDDZss0u2peCewmt5JozLEOBDU6SrawBpBA9yuyZxk0IhQkeRxWGHeB4A-E7IIvoCJ2w5J_-fDSe12UX54lJ-JmRxEorwX5O_uOnwGXkVsHPHrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd98bed83.mp4?token=SKJzKF2cSXaU9Oa0tdTSIuCB2__0kConMySSkPHGDvCtVYYdynuSd3JTjlRw5Mk1o_ISfOQwZHK_0QEl6GjGdGg3OeKkzh0QJHitJ4VaXLXWTYvYKuWXni7gPTSw9xN5X37pxd-qcdS8QJJb5eJ4dCByaAWFSrLu9sAVWblZBEtBFd_0sbBZ53vjkenNsQIPJnxvt92lpNILWFhzA68Q5sIVqzCyciCwM_I7VvShDDZss0u2peCewmt5JozLEOBDU6SrawBpBA9yuyZxk0IhQkeRxWGHeB4A-E7IIvoCJ2w5J_-fDSe12UX54lJ-JmRxEorwX5O_uOnwGXkVsHPHrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ده‌ها هواپیمای باری نیروی هوایی ایالات متحده (سی-۱۷ و دیگر هواپیماهای سنگین) امروز از پایگاه‌های اروپایی به خاورمیانه پرواز می‌کنند.
این یک "پل هوایی" تمام عیار است که بعد از جنگ۴۰روزه دوباره فعال شده.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19498" target="_blank">📅 00:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسانه های عراقی : در حال حاضر، هواپیماهای جنگنده آمریکایی بر فراز عراق پرواز می‌کنند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19497" target="_blank">📅 00:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارشهای مبنی بر دو موشک آمریکایی در نزدیکی روستای مسن در جزیره قشم اصابت کردند.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19496" target="_blank">📅 00:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19495" target="_blank">📅 00:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19494" target="_blank">📅 00:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نیویورک پست : روز چهارشنبه، یک حمله دیگر از سوی ایران توانست سامانه‌های پدافند هوایی آمریکا را نفوذ کرده و به یک انبار سلاح در نزدیکی همان پایگاهی اصابت کند که سه سرباز آمریکایی در آن در اردن کشته شدند. این حمله منجر به انفجار شد و در نتیجه، یک "ابر قارچ" شکل گرفت.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19493" target="_blank">📅 00:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مقامات ایران آخرین پیشنهاد ارائه شده از سوی میانجی‌ها رو هم قبول نکردن.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19492" target="_blank">📅 23:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Tether = 194,850 Toman
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19491" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آلارم حمله موشکی روی موبایل های کویت اومد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19490" target="_blank">📅 23:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">از اهواز ۳ موشک با صدای مهیب زدن سمت کویت
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19489" target="_blank">📅 23:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19488">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbfb1bbbe.mp4?token=fNRA4X7g8XxYGDhJOeuOufJkPYM2dybRMDtU4xvj5Siplfve0TfI6A_8xIBrwBTH3P8-pzc1i2p4V88XvzneNWe0-zg6wwio8TvrLFHi8sYxSSHPkiisRWXgT1pIWDtIg9lpDFLOz0vdMF31JmPGzrvFnBwWJjfqVzyz3zkxpc37AkJR5xAGaDkNxh1GLTSO3joOb9gVvnjVP5iDrPUP6QgjVsqFJYI7dA5GTJQL-jS-Zu8BS5TquKisEUsFjEyhkFerhGEs23wmxliExeZjEsjg58sltbwUAJVmHCUNBloyqEUIDzOQZAU7XM802QrdvVkSUID3BKztWFPt4GkxwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbfb1bbbe.mp4?token=fNRA4X7g8XxYGDhJOeuOufJkPYM2dybRMDtU4xvj5Siplfve0TfI6A_8xIBrwBTH3P8-pzc1i2p4V88XvzneNWe0-zg6wwio8TvrLFHi8sYxSSHPkiisRWXgT1pIWDtIg9lpDFLOz0vdMF31JmPGzrvFnBwWJjfqVzyz3zkxpc37AkJR5xAGaDkNxh1GLTSO3joOb9gVvnjVP5iDrPUP6QgjVsqFJYI7dA5GTJQL-jS-Zu8BS5TquKisEUsFjEyhkFerhGEs23wmxliExeZjEsjg58sltbwUAJVmHCUNBloyqEUIDzOQZAU7XM802QrdvVkSUID3BKztWFPt4GkxwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون کیش
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19488" target="_blank">📅 23:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19487">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: ایران دیگر ارتش ندارد، فقط افرادی باهوش و آقای ماکرون(رئیس جمهور فرانسه) را دارد، اما همچنان سطح مشخصی از توانایی‌ها را حفظ کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19487" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07325a864.mp4?token=UMQU9veS86pEqb2TL9C1K_qWei8p6ilg1md3TI-81L_ptNGnMzgLH66XkDGK6j3RgAo0G_vgA3orOJ-kqIYHo7MHaB8SEyGTkZ-1w0Nf_SC4CYq3GCMtJVLA-LPabzMMRN__tAiJfZtct1Og8iKpXsX59NorB1raD8GV1I6VNqaNayoeGK0nsDr7A_4K0Trc4FbQoSnJR_nm2xxr7kccK-SQ11ejlcBU-7E3eylPlSuF2NpkpF7LM4i8ohsucODw9Gv2HsUMXWpCv4V3GS8DTGIRLW9M82G_jCFKNq5wLP288dUihXaZHpYTF66jFV4w2XC0DaabLminFNpB-sh4CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07325a864.mp4?token=UMQU9veS86pEqb2TL9C1K_qWei8p6ilg1md3TI-81L_ptNGnMzgLH66XkDGK6j3RgAo0G_vgA3orOJ-kqIYHo7MHaB8SEyGTkZ-1w0Nf_SC4CYq3GCMtJVLA-LPabzMMRN__tAiJfZtct1Og8iKpXsX59NorB1raD8GV1I6VNqaNayoeGK0nsDr7A_4K0Trc4FbQoSnJR_nm2xxr7kccK-SQ11ejlcBU-7E3eylPlSuF2NpkpF7LM4i8ohsucODw9Gv2HsUMXWpCv4V3GS8DTGIRLW9M82G_jCFKNq5wLP288dUihXaZHpYTF66jFV4w2XC0DaabLminFNpB-sh4CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ،: «
ما در برابر جمهوری اسلامی ایران خیلی خوب عمل می‌کنیم، ما فوق‌العاده خوب عمل می‌کنیم
»
«آنها دوست دارند کاری انجام دهند، اما من می‌گویم که هنوز آماده نیستند.»
«آنها به چیزهای بیشتری از این دست نیاز دارند. آنها نیات شومی دارند.»
«جنگ ایران بهتر از آنچه هر کسی انتظار داشت، پیش می‌رود.»
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19486" target="_blank">📅 22:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19485">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1c7f0727d.mp4?token=i-ZqH0YSKp2HCj2iU2Uq2yDXUsHVK3CAZ1Vwf0x8EFvvETuExOX8DDJSgK46Ks2sxUlqVvfONcSgcHLcwlY_AEwcMri5IVP9Cef5pwZKbZP8yHFJRaJCd1dwvCUIYBuweHqPZLhRVhxKlulM1EkWC91gDDJAAzAcNszyzvBmoTd8xAa9AzASKKYPqi3adZrWnorFj4ogXKZU6ZkzNfn3MOfIVV07EzJikn0BC6mg07iEC-gSg8_Qcd4PnfKqizz5AvcYNN7Zwfi1K8jQRz7glSOwRa-5iiGszeEJbqsShX0-DzBj6d1uh_no-wrp8r3iaihS3UiYIvTJnLRSDYDe5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1c7f0727d.mp4?token=i-ZqH0YSKp2HCj2iU2Uq2yDXUsHVK3CAZ1Vwf0x8EFvvETuExOX8DDJSgK46Ks2sxUlqVvfONcSgcHLcwlY_AEwcMri5IVP9Cef5pwZKbZP8yHFJRaJCd1dwvCUIYBuweHqPZLhRVhxKlulM1EkWC91gDDJAAzAcNszyzvBmoTd8xAa9AzASKKYPqi3adZrWnorFj4ogXKZU6ZkzNfn3MOfIVV07EzJikn0BC6mg07iEC-gSg8_Qcd4PnfKqizz5AvcYNN7Zwfi1K8jQRz7glSOwRa-5iiGszeEJbqsShX0-DzBj6d1uh_no-wrp8r3iaihS3UiYIvTJnLRSDYDe5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران هیچ نیروی نظامی ندارد.
آنها هیچ چیز دیگری ندارند جز اینکه شرور و باهوش هستند و هنوز هم توانایی‌هایی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19485" target="_blank">📅 22:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19484">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed657c044.mp4?token=Wysap-iCw4ho71gNFPmIrK8sSAonKa0UMCbV7WMhfaTMaHGqvR6ck3pKUMbxa-yOhyRo-su5f-2D2VTf0lJlKczHo1KGGN6zykQOe0amo-OsHn6HtgFjgsvaxJ7OkEln1yvZIeUlVSchhX3zpStpB-9wKkmwqOREwHOuYjdlRUDz7l9QkQ-FXQN5Aq-_W189TC98JWvEvpNg57xOFnYGyxP_1gIydT_Gq3tVu3bHCOmRUsQLGkRTAqSIeWJ8AZRJObEd6lN5p21Pd3LUxAfR7tCTKMm8ffMpgjPP-cBqwfFMkWRMT-k1InB9pFghBolsa6xxRCOs0yowr9jUitbXvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed657c044.mp4?token=Wysap-iCw4ho71gNFPmIrK8sSAonKa0UMCbV7WMhfaTMaHGqvR6ck3pKUMbxa-yOhyRo-su5f-2D2VTf0lJlKczHo1KGGN6zykQOe0amo-OsHn6HtgFjgsvaxJ7OkEln1yvZIeUlVSchhX3zpStpB-9wKkmwqOREwHOuYjdlRUDz7l9QkQ-FXQN5Aq-_W189TC98JWvEvpNg57xOFnYGyxP_1gIydT_Gq3tVu3bHCOmRUsQLGkRTAqSIeWJ8AZRJObEd6lN5p21Pd3LUxAfR7tCTKMm8ffMpgjPP-cBqwfFMkWRMT-k1InB9pFghBolsa6xxRCOs0yowr9jUitbXvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام  : از زمان از سرگیری محاصره دریایی علیه ایران در نه روز پیش، سنتکام ۱۲ کشتی تجاری را تغییر مسیر داده و ۱ کشتی را از کار انداخته است تا از ورود یا خروج کشتی‌ها به بنادر یا مناطق ساحلی ایران جلوگیری کند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19484" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19483">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شبکه12 اسرائیل : مقامات آمریکایی به همتایان خود در اسرائیل، آماده‌باش ابلاغ کردند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19483" target="_blank">📅 22:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19482">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">منابع عربی: کره شمالی در حال تخلیه سفارت خود در تهران است.
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19482" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19481">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش کامل فاکس نیوز با موضوع حمله به قلب انرژی ایران که امروز بیشترین دایرکت و درخواست رو در مورد این گزارش داده بودید. ویدیو کامل به همراه زیرنویس فارسی.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19481" target="_blank">📅 21:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq1pcWdnzDWr-tNnsoieYxfQMKYkna7lsp4dn9-o7zceXYqLEHOStNOB02aUT5RSjZZUdxbEHKFBooQZUsx6iX8WfsMD8LuKcFVYyKc9Kt05-jXptkVZXz4t3QdAUDXxVm2yr59tdxritpY3Mc5_UUJA0d_Ac0sbNrQsdhASy7T_5e-GiRJxnWuwwtmzZtdRKpr6Ds0EErJIN8Qzf7K4XM6Ve5-SY_2tBgQlsqNntxQ1aqiQxGKZUUR0lovjAcrqAVzXtsPBJODo-u1Z6I5RCbu-E_jQuttNPmsu8Z0XtZDZTaAp36zo5JXdFme6X0Md7eniwQV_ViKTXGqUvlP2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون؛ نفس های آخر رژیم
،
استقرار
موشک ذوالفقار در میدان آزادی
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19480" target="_blank">📅 21:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به گفته منابع غیر رسمی اعضای سفارت آلمان از ایران خارج شدند
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19479" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بریتانیا پس از تهدیدات جمهوری اسلامی : نیروهای ما آماده مقابله با هرگونه حمله هستند،.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19477" target="_blank">📅 20:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تسنیم: تکذیب هرگونه اصابت جدید در جزیره لارک/ صدای انفجارها از سمت تنگه هرمز است ‌@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19476" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تسنیم: تکذیب هرگونه اصابت جدید در جزیره لارک/ صدای انفجارها از سمت تنگه هرمز است
‌
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19475" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال ۱۴ : موشه سعدا، نماینده مجلس از حزب لیکود، در یک برنامه زنده تلویزیونی گفت: «همه ما می‌دانیم که به سمت حمله به ایران، شاید حتی همین آخر هفته، می‌رویم»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19474" target="_blank">📅 20:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سنای آمریکا سد راه محدودیت جنگی ترامپ شد
مجلس سنای آمریکا، طرحی را که قصد داشت اختیارات نظامی دونالد ترامپ برای آغاز جنگ احتمالی علیه ایران را محدود کند، متوقف کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19473" target="_blank">📅 20:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزارت امور خارجه آمریکا: از شهروندان آمریکایی مقیم خاورمیانه درخواست می‌شود برای احتمال لغو پروازها و بسته شدن مسیرهای هوایی در این منطقه آمادگی داشته باشند. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19472" target="_blank">📅 19:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزارت امور خارجه آمریکا: از شهروندان آمریکایی مقیم خاورمیانه درخواست می‌شود برای احتمال لغو پروازها و بسته شدن مسیرهای هوایی در این منطقه آمادگی داشته باشند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19471" target="_blank">📅 19:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی:
ایران آخرین پیشنهاد آمریکا برای صلح را رد کرده است.
ما در حال تلاش هستیم، اما ایرانی‌ها تمایلی به همکاری نشان نمی‌دهند
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19470" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امیدیه ستون دود دیده میشود ولی صدایی به گوش‌ نرسید
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19469" target="_blank">📅 19:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اهواز هم زدن
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19468" target="_blank">📅 19:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝒎𝒐𝒉𝒂𝒎𝒎𝒂𝒅</strong></div>
<div class="tg-text">https://t.me/boost/withyashar
یاشار لینک boost رو دوباره بزار اعضای جدیدی که پرمیوم دارن هم حمایت کنن سطح ۲ رو از دست نده کانال.</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19467" target="_blank">📅 19:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرگزاری‌  رژیم : یک موشک آمریکایی منطقه ای در ساحل شهر سوزا در جزیره قشم، در جنوب کشور را هدف قرار داد. @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19466" target="_blank">📅 19:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجار در کویت
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19465" target="_blank">📅 19:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرگزاری‌  رژیم : یک موشک آمریکایی منطقه ای در ساحل شهر سوزا در جزیره قشم، در جنوب کشور را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19464" target="_blank">📅 19:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارهایی از جزیره بوبيان گزارش میشود
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19463" target="_blank">📅 19:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پدافند قشم فعال شده
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19462" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ به نشریه "اکسیوس" گفت: ایرانی‌ها می‌خواهند مذاکره کنند، اما در حال حاضر آمادگی امضای توافق را ندارند و هنوز به اندازه کافی تحت فشار قرار نگرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19461" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مجری : آیا مجتبی خامنه‌ای زنده است؟  نتانیاهو: فکر می‌کنم او زنده است. @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19460" target="_blank">📅 19:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ به نشریه اکسیوس: اسرائیل در عرض دو دقیقه به حملات علیه ایران خواهد پیوست، اگر از آن بخواهیم، اما ما نیازی به این کار نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19459" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ در گفتگو با شبکه ۱۲ اسرائیل اعلام کرد که در حال بررسی یک «حمله گسترده»، بزرگ‌تر از هر آنچه پیش از این انجام شده، است و گفت که به اتخاذ تصمیم نهایی نزدیک شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19458" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbda7bde91.mp4?token=iGMZu144u53W0VGOsoF3Ua_YHTFBCaMoP3-Gwgf9dPPu2j6gHmLweIqpQAkrkq2GLnChQMrxdksu6s-ycGgkyGavdrfBuBW0Sn6C0vsPtX9wrqY59ctcE6zXifm4s9VwzDMcjbZAm32WBMqPk7MNCqWYCy-n6xB-eO6vh8ME7fI5jeiHOuLG9odfpJ8Zu8jyZ9dAghT4bWXVnk2aJ7C60Z4GiM_txq5X1zTfaqLrGi459nzdt6ZTM81iw-bC9T5h5gYVpYc1FutkJU4ZYBhPA_WWF8ErstABLYwKIi7Kgk9O2sFVYwtXVh2A2S_S6IbWdxfrRmDOGBttSXFOOXWlWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbda7bde91.mp4?token=iGMZu144u53W0VGOsoF3Ua_YHTFBCaMoP3-Gwgf9dPPu2j6gHmLweIqpQAkrkq2GLnChQMrxdksu6s-ycGgkyGavdrfBuBW0Sn6C0vsPtX9wrqY59ctcE6zXifm4s9VwzDMcjbZAm32WBMqPk7MNCqWYCy-n6xB-eO6vh8ME7fI5jeiHOuLG9odfpJ8Zu8jyZ9dAghT4bWXVnk2aJ7C60Z4GiM_txq5X1zTfaqLrGi459nzdt6ZTM81iw-bC9T5h5gYVpYc1FutkJU4ZYBhPA_WWF8ErstABLYwKIi7Kgk9O2sFVYwtXVh2A2S_S6IbWdxfrRmDOGBttSXFOOXWlWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
: آیا مجتبی خامنه‌ای زنده است؟
نتانیاهو: فکر می‌کنم او زنده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19457" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کلیسای جامع ملی واشنگتن اعلام کرد مراسم یادبود سناتور لیندزی گراهام در ۲۸ ژوئیه(۶مرداد) برگزار می‌شود. این مراسم با حضور خانواده، دوستان، همکاران سیاسی و رهبران ملی برای بزرگداشت زندگی و چند دهه خدمت عمومی او برگزار خواهد شد. دونالد ترامپ نیز در این مراسم سخنرانی می‌کند و از نقش گراهام در سیاست خارجی، امور دفاعی و حزب جمهوری‌خواه یاد خواهد کرد. جزئیات بیشتر درباره دیگر شرکت‌کنندگان و برنامه مراسم بعداً اعلام می‌شود.
@WarRoom
یاشار : بی بی هم حتما میره !</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19456" target="_blank">📅 18:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سپاه: دیگر اجازه نمی‌دهیم آمریکا با آتش‌بس‌های فریبنده، ذخایر نفت و مهمات خود را جایگزین و پس‌از آن مجدداً حملات را از سر بگیرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19455" target="_blank">📅 18:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19454">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرنگار زن : آیا روسیه به ایران در هدف قرار دادن نیروهای آمریکایی کمک می‌کند؟
لاوروف، وزیر امور خارجه روسیه: مدل موهات قشنگه!
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19454" target="_blank">📅 18:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19453">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رویترز : ایران این ماه چند تا از فرمانده‌های سپاه و تجهیزات مربوط به موشک رو که با هزینه خودش خریداری کرده ،برای حوثی‌های یمن فرستاده! به ارزش بالغ بر 20 میلیارد دلار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19453" target="_blank">📅 17:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19452">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46d0627615.mp4?token=YXJGb0Ar6rMs67f--VMaP3gqhIoMK6UvH3VUHQ1ZsjiHaczod3AbDv0YToJtJ43na_eb9ZbmZstzkjoUHWEjPrTBriXd1gNs91AgPMZzq_IVJ6EME5CMmFVcVFqmVEgR2L2bL2mPlJUdW7O2KklqUO69IOC-koCPyiKhT0Dfe2_V1Ai8wK5f0zDEV_EXFs3_otqDHrqikF8248Guj1MKeiP5UFLdWrNeCzRMUltdAUqlUEAQwS_gYA0GgvtBzTYG3mGdyK80foWephnRYQA2P5KCFkuDHJhKqfnSUzHZjFFAdmCXdy5G0bHv3AnTQ1x1AsEu-Pj6UKPL8GOkMR0tCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46d0627615.mp4?token=YXJGb0Ar6rMs67f--VMaP3gqhIoMK6UvH3VUHQ1ZsjiHaczod3AbDv0YToJtJ43na_eb9ZbmZstzkjoUHWEjPrTBriXd1gNs91AgPMZzq_IVJ6EME5CMmFVcVFqmVEgR2L2bL2mPlJUdW7O2KklqUO69IOC-koCPyiKhT0Dfe2_V1Ai8wK5f0zDEV_EXFs3_otqDHrqikF8248Guj1MKeiP5UFLdWrNeCzRMUltdAUqlUEAQwS_gYA0GgvtBzTYG3mGdyK80foWephnRYQA2P5KCFkuDHJhKqfnSUzHZjFFAdmCXdy5G0bHv3AnTQ1x1AsEu-Pj6UKPL8GOkMR0tCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی پیش انفجاری عظیم در جنوب لبنان منطقه کفار تبنیت  توسط حمله جدید نیروهای اسرائیلی انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19452" target="_blank">📅 17:51 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
