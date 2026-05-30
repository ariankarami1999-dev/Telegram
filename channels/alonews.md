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
<img src="https://cdn4.telesco.pe/file/AvrEjUeEN7UKx-Z8EXsbu19WRRQNzjKnDdbOFgqU2wW8lZr0xK40GN5WpoNyivhGzCf2mOEKD3wS-6aryX9L1x12rvLUT27xTsv2U_xxeaUSpzD5u0ZFEMxcAvpeRgcdP4uo76HwVd8NaO4LmlIeIbq9QP6rS_O_oUE2pQyWwTOpVcgwtm2qn_WFdLNBJbq0GzDk9iNK-MwORn2NxYuT0QvgQZ9k2eg5UQxaB8cD_7nxdkoGiPMRNKdGyzy9GMIQG0xUNlX1sxDjmW6MoOqMy6IXuyJyT0NrYzpE2ITHok2a9apZAzUePf6tOIuFvV43IbAbpzIbg1ZYa4TcWIZk1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 909K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 01:00:47</div>
<hr>

<div class="tg-post" id="msg-123833">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=Tf76oSPYuon8Lrje9JDmnDRtI6rIXb25HXWKOr2OdJe-SKwkl7_5ZNf5eaHbnuN5yotv8apj31ZmxaQ2U_xi2fgQ3-EKhJEAwTMAEOkw_DYYlU73xPAwDI1K-aSm649Hf9WmJcogJIorrnXiwVGZIDPZPF_JdBHzM3LFZOBFrgjHPKPi-sfHW1j9LltE4mTx0675cUpEtOdtW0kxLen8KQp27sltB5hVy4-wdkIoTsnEZKjr14EPY6Lwvqr_jbOIiCQ-s-KOEOcTgWxPtGNvfrHoYdX0RXOxvV0sALliwkzEf2y8YIJSyXYBdUAEkVlx_jdAkdUyklw0_1AHzLD8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=Tf76oSPYuon8Lrje9JDmnDRtI6rIXb25HXWKOr2OdJe-SKwkl7_5ZNf5eaHbnuN5yotv8apj31ZmxaQ2U_xi2fgQ3-EKhJEAwTMAEOkw_DYYlU73xPAwDI1K-aSm649Hf9WmJcogJIorrnXiwVGZIDPZPF_JdBHzM3LFZOBFrgjHPKPi-sfHW1j9LltE4mTx0675cUpEtOdtW0kxLen8KQp27sltB5hVy4-wdkIoTsnEZKjr14EPY6Lwvqr_jbOIiCQ-s-KOEOcTgWxPtGNvfrHoYdX0RXOxvV0sALliwkzEf2y8YIJSyXYBdUAEkVlx_jdAkdUyklw0_1AHzLD8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت های امشب عادل فردوسی‌پور در آپارات اسپورت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/123833" target="_blank">📅 00:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123832">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نیروی هوایی ایالات متحده آمریکا برنامه دارد در قالب بودجه سال مالی ۲۰۲۷، تعداد ۱۵ فروند هواپیمای سوخت‌رسان KC-۴۶A Pegasus را به ارزش ۳.۵۲ میلیارد دلار خریداری کند
🔴
با تحویل این ۱۵ فروند تعداد کل سوخت رسان‌های پگاسوس تحویلی به نیروی هوایی آمریکا به ۱۲۰ فروند می‌رسد و برنامه نهایی تحویل +۱۷۹ فروند است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/123832" target="_blank">📅 00:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123831">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqwnvD8A9T1qnNKWqH4wEdIMK6CuWDsk23NUKvrTg9tSV0_0RH1DDz5mB-yDR8po0iB-uQc-l3Pu5bIiF6DRjL05ZpuLQO8-ada70tQwPVfs-jG9jE55MCYC-g-GO5zsjivcQ5vOiTmRHjO4nfgiKOHxpL39s4vaZD-ZwYqiWNrxZiUrKJJwMM4LKDOYMO88UeGo5hwnpDh9Gb4U_sQukRimmhI_9jgMWFzeUj_esu2dPOzzZCppTef1G6q9r45zaHaz_b0MrWi7q0kUIP-CwlTMG3Y_H6NQKAkDqJ9vy28siUYrnDVxP3YM4i8yJvkvy0jYW4VDmh0uwJw_4ZpTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :
- یکی باید به پاپ بگه شهردار شیکاگو به درد نمی‌خوره، و ایران هم نباید بمب هسته‌ای داشته باشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/123831" target="_blank">📅 00:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123830">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f8f1e279.mp4?token=RYezsZKYeY5isiGz30V3oY-N-sCGjcBWesHeKFeW7KRZe1FF2raTIHEnmjkcJuiCHN3IKILBDwrcNwAj1Y7FW8D-pPN8JvUULxvet2ny7ousVWIvertgOtqzCJ48N6Rjy48T4FtK3mi1IrERkpSyQTkQ3i8xSv_nLwxWZzpJHRv6f2eo6DzWM06ltqXD7nNmV7qAH6jk4uG4HcWNtuHNVZALHNcbY4kzqd876mGUIPdpG4dNHmJ8REmWGbKXg3gdQrspazMos7r_mi38DvV3fFxcAFgkiQKYLrjyNYLwykyb5zZDR1x9pMnPrXOnxHpXEc5uEm0aowUvi3vGSrECZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f8f1e279.mp4?token=RYezsZKYeY5isiGz30V3oY-N-sCGjcBWesHeKFeW7KRZe1FF2raTIHEnmjkcJuiCHN3IKILBDwrcNwAj1Y7FW8D-pPN8JvUULxvet2ny7ousVWIvertgOtqzCJ48N6Rjy48T4FtK3mi1IrERkpSyQTkQ3i8xSv_nLwxWZzpJHRv6f2eo6DzWM06ltqXD7nNmV7qAH6jk4uG4HcWNtuHNVZALHNcbY4kzqd876mGUIPdpG4dNHmJ8REmWGbKXg3gdQrspazMos7r_mi38DvV3fFxcAFgkiQKYLrjyNYLwykyb5zZDR1x9pMnPrXOnxHpXEc5uEm0aowUvi3vGSrECZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کنایه مجری تلویزیون به تاخیر ۹ روزه در انتشار آمار تورم توسط مرکز آمار: اعداد را اعلام کنید یا نکنید مردم تورم را لمس می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/123830" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123828">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgWw7HvlskBioyIOEY1wuEMujs-hopR9moUmWBcPM0VVlfrUjNCwdw0ko59Td-KCHFYRFUhyEmAYrlTguvj4uBBYKYTz5jqchz1Ntk5096bQ9lvt05AAT0H87Op8UFhpvpC5zNAkU2qVmxVAPzhj1jJbeej1wPQ7J5qY-Eyk7cOG8Dkeo4813vaBOh3dQomN2MJLzt8Z_PQ07C-ULERQ8hm_HQKUE2MLFZdvJq6Tsia6IWv27P6050FTukEXaktSVQ9A3rNueKwqJG0-Wye7yd114E-3-Zh2uCIjpAsJ5KeQeBTblMx6IF-s9OGUq8OWJKjDo1TYLCLqQuByKQ1-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwuEjm2Mo3_wXAQZAJ6iQ7q6lWjwkUdRXst2EBLawxT3NeyGxvLPHI2fEBehHvfBP-khhBYne26upbeZyz8ioAwmp17mE3PDEvcSPAjy8Z9d-LcRuqVpdV5OZMIPThRNqb1PlXt9uOCqGwHwP80GsN-xoGG-sIIGk8hfU0fA4VTXr-9zvym10o2mUE41Q8KgKMSwh3iiLesNb-5xNWl1NKW63E2KGH0lgIAIiIvZh6exbHwNAcE42odEE7kj2p1r5RleBiDsyHZc6gqh7KNcf3FEJnFsmUg3JsuPTMEUzCZ_eOEqh5LNytWIKlFv9-qLIuTxXYBG4Yy9LH1MJXv8vQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل بر کفرجوز و شوکین در جنوب لبنان انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/123828" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123827">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
مدارس شمال اسرائیل فردا تعطیل اند و بنظر می‌رسد اسرائیل خودش را برای موج جدید و مرگبارتری از درگیری با حزب‌الله آماده می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/123827" target="_blank">📅 00:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123826">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
به حداقل ۵ جهت به سمت فضای هوایی اوکراین، پهپادهای روسی Geran-2 پرتاب شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/123826" target="_blank">📅 23:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123825">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAc6wWM_i6X8GdsCl-5FNTlBT2DPKTFzD5R9tg0O2aoUGHUT61C5kEdoeFZQUfzs2pRkCgAhG59rb_yAXCHqwG-VrIdtlXpjbJeONvj34U1LkJpdWUvexQX_kRf6rV0coAtek9qX_21TvkNfVVLDc1nHRvf1PrP5VUhSPkq04LYLJZGzIjND7bK_rEsny3RBK9lwtrn27HAjDkgBFC0sBpNs2ZUKdBO896tn9rKWn8SM_yhIzrlItIUneYx8hxu7CTqgNqwDyL09adJjQO7JVOjsxD0k1xnMxf7cxAKaAOvHqUbyVejqUhSY2DTGkj5fL5M6Y8LAy3LpNpgVixZhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری جدید و پربازدید از دونالد ترامپ درحال عزیمت به زمین گلف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123825" target="_blank">📅 23:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123824">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کابینه جنگ اسرائیل در ساعت ۲۲:۳۰ (به وقت محلی) تشکیل جلسه خواهد داد. در حال حاضر ارزیابی وضعیت در دفتر نخست‌وزیر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/123824" target="_blank">📅 23:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123823">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
معاون سیاسی سپاه: ایران بر تنگه هرمز مسلط شده و پس از ۵۰۰ سال، به موقعیتی دست یافته که حق مسلم مردم ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/123823" target="_blank">📅 23:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123822">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: میدان و دیپلماسی دوشادوش هم آماده برای هر وضعیتی
🔴
سخنگوی ارتش: امروز دیپلماسی و میدان نزدیک‌تر و هماهنگ‌تر از هر زمانی در مسیر تحقق منافع و عزت ملی کشور می‌کوشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/123822" target="_blank">📅 23:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123820">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI6QdrB8QuDB0MtApR_BEHLkQDq8z2B3QzTGiNAm4ETMol54CG0tR_jzZB4IxFImJSqK-E_LvZJl3g3Mm9AA0wV601cdP7mZJF8vxwHamdDBal6NFViEV4Hxcp8jH7GhTn_3W1vP0hcnQlb4OOrTAU16-oGxPRUQe4gHM79qxleLPSOjkmjDPeQaTsyV5PDMASTQKNmrkVfh1eKNjq6YHZ2-YNFGUtWZMwvpnN0qOkIVm7DR7gN-CeR-_amymTE57Z8prIXxdHGK2Ci2W3mK9mxSADhoQRvufxkZQh2v_z53lcBKw7AKCzq2bQpxivODm4JSIrLxlHY2tKIXf_eQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7752c409d.mp4?token=vZ-oCzoySIgfmB7eqw1SldTBidF5Nsa5u8zBZD2Hm3U3QG6Ux3sBnvuypM_FEEzz5fiRM5XqbL1647XUsJOJmJm5HG1llYQ-8UhVT6IcGxUT8n8jM3DzaIkUzP_Q3zNYxcn-MH83xHEM6zdQZDprqWExDNm9E1GfJsK3r-SUDeK7iwRgUAX_NfH7M1_YKzxhaorME-26ALm8Keg1jfy5sVupvjG8MoMIfR2hhpAgXGlSLszTy_QEvDkkdCSOqQIELtiINOexdEe20L0O38km9iMOU5wUaaZlcZjzNCh2-KHVXXOwhOsMsvNXh1_5t2xCGjLqTqR7SvWZm-TWA5R0Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7752c409d.mp4?token=vZ-oCzoySIgfmB7eqw1SldTBidF5Nsa5u8zBZD2Hm3U3QG6Ux3sBnvuypM_FEEzz5fiRM5XqbL1647XUsJOJmJm5HG1llYQ-8UhVT6IcGxUT8n8jM3DzaIkUzP_Q3zNYxcn-MH83xHEM6zdQZDprqWExDNm9E1GfJsK3r-SUDeK7iwRgUAX_NfH7M1_YKzxhaorME-26ALm8Keg1jfy5sVupvjG8MoMIfR2hhpAgXGlSLszTy_QEvDkkdCSOqQIELtiINOexdEe20L0O38km9iMOU5wUaaZlcZjzNCh2-KHVXXOwhOsMsvNXh1_5t2xCGjLqTqR7SvWZm-TWA5R0Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز یه مین دریایی ایرانی نزدیک سواحل عمان تو تنگه هرمز پیدا شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/123820" target="_blank">📅 23:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123819">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی:
پیشرفت‌هایی در مذاکرات وجود دارد و ما این را انکار نمی‌کنیم، اما باید مراقب باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/123819" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123818">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktvMgtqnKhagdb8ZP6YfNzugM92aJIJs9vUfUAbFQiNodkqnefZHZ2DlgqbjA2EvKdNVscQyZcdPqkqqMpv4MS4VwVXhsva0EUF-4nLa0bAx-Lrk9OAD9oi9-ObPAkx0Dc4ap1Bmo4VLVA9hmSm-n_Prddu8veZLUMh_F41PqC4qS4rRKn6ncKR16PT0gKD7q2Yni37EsyT1qac1CzHH8e3XYpwXdxI-aqIFnNv4rbDR1sq1FR3dU9KgGXN4LIHVCQvjYaLCiD7PDeZFyogH3hSZmoZxANniWbeVebTWtvpMnWxnSoDmQvo9QlCDDFxlf-5QKkQ0Ieir3ZkxoFqB_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
موزه ریاست جمهوری اوباما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/123818" target="_blank">📅 23:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123817">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a49146ae6.mp4?token=h_6RUURP4nuh1xgGqAo3aKCmWe_TzT73mlVCUvf21aPO6z-W3849kxykGhU3zK6WgT3V77djuVRW1SxODlwnan3Pbz9iInqidyjbruF9ch512m0t7d9t6ptL5Yk_q-_iYJGsoTb7VT8jxL-jIBgxOuVS4f8DiLZc8kUI5CibJnqL59epW8BrOOvklqGai_6CCTJbV3mMEhwntrMoBCwpQmIZYIZQ9F4n0GdiQny06GspkLr7e4bcobT7Hi5XhzxuGM5dFJslsAeX-K8tRpKzNmmiSa_4-Fw8-ih3j7TnZAg8vfFdaL8SEumC9xg46uLbUJZUEudV8NxbGpmoc3qJoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a49146ae6.mp4?token=h_6RUURP4nuh1xgGqAo3aKCmWe_TzT73mlVCUvf21aPO6z-W3849kxykGhU3zK6WgT3V77djuVRW1SxODlwnan3Pbz9iInqidyjbruF9ch512m0t7d9t6ptL5Yk_q-_iYJGsoTb7VT8jxL-jIBgxOuVS4f8DiLZc8kUI5CibJnqL59epW8BrOOvklqGai_6CCTJbV3mMEhwntrMoBCwpQmIZYIZQ9F4n0GdiQny06GspkLr7e4bcobT7Hi5XhzxuGM5dFJslsAeX-K8tRpKzNmmiSa_4-Fw8-ih3j7TnZAg8vfFdaL8SEumC9xg46uLbUJZUEudV8NxbGpmoc3qJoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام حديثه اكبرزاده ، 18 دی در فرديس كرج با شليک مستقیم گلوله به سينه‌اش آسمانی شد.
🤔
عرزشی حرام زاده این دختر ایرانی تروریست بود؟ ظلم پایدار نیست به وقتش سر عزیزان شما هم میاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/123817" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123816">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1e62f376.mp4?token=DXa-yJFUK4_7ztbed-1mIrdpfH_6Dpl3hs1_PuU0fcFvKqdpBxH8HRSRr9bsj2eBlsoHbltvI84A-DOWt13hRZ0-XXlIJfE5nuO2DJMGktraDFLxhAWlbBT37XPvJOjIywKcrvwxkbHh5NneosqUrfu1J_OtPfn7mqn8DoOARTGDB63qrHBfBvxe3FlNZG8LtP9GOwJ-ECazhQy3RFZ647o-nE6B6TwdQxjqJ0kK6-jbWpMMVS4NfEOj_31FUxfGebSH4iVv4yMs3Qq3E4otzxYLQr2iNid-cO5dXbR8R78yXgXEhnc3U7sdqnaZRW_-9Cjqy1YVOcDX9RjKsBfWKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1e62f376.mp4?token=DXa-yJFUK4_7ztbed-1mIrdpfH_6Dpl3hs1_PuU0fcFvKqdpBxH8HRSRr9bsj2eBlsoHbltvI84A-DOWt13hRZ0-XXlIJfE5nuO2DJMGktraDFLxhAWlbBT37XPvJOjIywKcrvwxkbHh5NneosqUrfu1J_OtPfn7mqn8DoOARTGDB63qrHBfBvxe3FlNZG8LtP9GOwJ-ECazhQy3RFZ647o-nE6B6TwdQxjqJ0kK6-jbWpMMVS4NfEOj_31FUxfGebSH4iVv4yMs3Qq3E4otzxYLQr2iNid-cO5dXbR8R78yXgXEhnc3U7sdqnaZRW_-9Cjqy1YVOcDX9RjKsBfWKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت ملی اسرائیل:
«باید بیروت را صاف کنیم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/123816" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123815">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: محاصره دریایی یا با زور یا با مذاکره پایان خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/123815" target="_blank">📅 23:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123814">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی: محاصره دریایی یا با زور یا با مذاکره پایان خواهد یافت</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123814" target="_blank">📅 23:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123813">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ارتش: هرگونه تعرض به خاک کشور پاسخ محکم‌تر از گذشته را دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123813" target="_blank">📅 23:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123812">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
خبرنگار الحدث: درگیری‌های شدید بین حزب‌الله و نیروهای اسرائیلی در داخل شهرک دبین در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/123812" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123811">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c0b1479d.mp4?token=jAFbdFQkz1rK-dtoMcxHgIjYiPKOWbV5hcqfoB5lchbIv2H-ahnkw6To2_DqBBRoGtEnHFrfrnSEy1FmhUvgHOfZl5B6HIHn4BuLW_AOl5-QWIvgx5VL1kKXvllA9BrKArw4lKXHs3PQSRYZXLKIPtNB11PXL-aoq9oOmnacAqFqP-Uq5d6RFghvG9bSDt4eOTcT3zgUX3c9cKp46CSDiWQlz_mfla9WlxgMy9KXxT88jIaewa_HhG08Wvt8IOhXfX05ZuFpPr1ikGKWwtUiuprPUyyfb26c8CQ41aFcKtlHgzZkF8nHO36EMd4uwnlVP0fBM3ra7oM7dfZaiMELNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c0b1479d.mp4?token=jAFbdFQkz1rK-dtoMcxHgIjYiPKOWbV5hcqfoB5lchbIv2H-ahnkw6To2_DqBBRoGtEnHFrfrnSEy1FmhUvgHOfZl5B6HIHn4BuLW_AOl5-QWIvgx5VL1kKXvllA9BrKArw4lKXHs3PQSRYZXLKIPtNB11PXL-aoq9oOmnacAqFqP-Uq5d6RFghvG9bSDt4eOTcT3zgUX3c9cKp46CSDiWQlz_mfla9WlxgMy9KXxT88jIaewa_HhG08Wvt8IOhXfX05ZuFpPr1ikGKWwtUiuprPUyyfb26c8CQ41aFcKtlHgzZkF8nHO36EMd4uwnlVP0fBM3ra7oM7dfZaiMELNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت سد کرج طی سه ماه اخیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123811" target="_blank">📅 23:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123810">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
اظهارات عجیب مشاور قالیباف درباره مذاکرات ایران و آمریک
🔴
توافق صرفاً یک تاکتیک برای خرید زمان و منابع است نه استراتژی صلح‌طلبانه
🔴
توافقی وجود ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123810" target="_blank">📅 23:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123809">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0eeee36654.mp4?token=IPY7BuKPY6_RQVsXe6T4jWa4D32kqf0VnLbvGPN6-OY19Hq1JOwtE_fhhCTa_HU4dvBE7bB9Uq5nKlReXaUEdR42UW5By4GtaMJJE30q8j7fBAa3gnSpqxKEJAz_6Dn-coATa0ven1tP9D5V7oGvUD2YY9TJuWDQL3PmCgMJc-J0ar-4yAWmeQdGHeZx-4B1J65G69sFVuQ-b89ZxGaQKNPur1qeYKGQuHOWxrd7CXsWHhGhpoSmoq8kUVOtwbDiHrCl5zqTty8KuKo5mql9bD0TcMgXxUagFJaSovXAPAnpyd3ZUwKkD-U2gYUCSuFUNEjzL3zC3Tvxnf7Qd2YuwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0eeee36654.mp4?token=IPY7BuKPY6_RQVsXe6T4jWa4D32kqf0VnLbvGPN6-OY19Hq1JOwtE_fhhCTa_HU4dvBE7bB9Uq5nKlReXaUEdR42UW5By4GtaMJJE30q8j7fBAa3gnSpqxKEJAz_6Dn-coATa0ven1tP9D5V7oGvUD2YY9TJuWDQL3PmCgMJc-J0ar-4yAWmeQdGHeZx-4B1J65G69sFVuQ-b89ZxGaQKNPur1qeYKGQuHOWxrd7CXsWHhGhpoSmoq8kUVOtwbDiHrCl5zqTty8KuKo5mql9bD0TcMgXxUagFJaSovXAPAnpyd3ZUwKkD-U2gYUCSuFUNEjzL3zC3Tvxnf7Qd2YuwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ویرال شده از حرکت ورزشی یه پسر جوون توی ایران که شاهکار خلق کرده
🔥
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123809" target="_blank">📅 23:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123808">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
کانیه وست برای شلوغ‌ترین کنسرت دوران حرفه‌ای‌اش در استانبول روی صحنه است.
🔴
هزاران توریست برای تماشای این کنسرت راهی استانبول شدند و میلیون‌ها دلار درآمد وارد اقتصاد ترکیه شد.
🔴
حالا تصور کن اگر یک خواننده محبوب خارجی بخواهد در ایران کنسرت برگزار کند؛ عرزشی حرام زاده با فریاد و جنجال، کاری می‌کنند که ایران و ایرانی را در چشم دنیا عقب‌مانده و وحشی نشان دهند.
🤔
ایران می‌توانست مرکز گردشگری، موسیقی، هنر و درآمد باشد؛ اما جمهوری اسلامی فقط فقر، سانسور و انزوا ساخته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/123808" target="_blank">📅 22:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123807">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
گزارش ها از درگیری شدید نیروی زمینی ارتش اسرائیل و حزب الله در نزدیک شهر نبطیه، پایتخت جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123807" target="_blank">📅 22:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123806">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پاریس تو ضربات پنالتی آرسنال رو برد و قهرمان اروپا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123806" target="_blank">📅 22:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123805">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
این هفته مراقب تابش فرابنفش باشید
🔴
این هفته شاخص فرابنش بالا است، تا حد ممکن در ساعات میانی روز(ساعات۹-۱۵، با توجه به داده‌ها) کمتر در برابر تابش مستقیم خورشید قرار بگیرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123805" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123804">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExpXHc30W2oHWw_Ezx4tO6F1ndvM7VuTBxkM9kZQhocHJELRDaQ1HSZ2gYofpmupI-Wi5X2VE7jpMHouJrJgMoNaP8Ly47eAus9lXxfPYpY2HBg0fal6amawtmLIGXw1WRZqczj1mfWvcbGcbUYKLGj5Z2WwW_Q4k86IvbIQMUN0n-hfoU4Ruy_5x_6_ryl3giRImo1nOWOJe_oAsNuPVV5J6fp0jAM_ASXANotvHOaaNvswX6fMTetIShKG1i_ITSsO012m5IcPfi--X7TsR89idafeWhHBE5hhMN1AoUh1B7IOeVNFlDNZRo0FgV5_j8ycjASnjuV3tS_DDQBRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
فروش باز شد.
✔️
✔️
✔️
گیگی
5⃣
1⃣
هزار
✔️
✔️
✔️
کابوس هرچی گرون فروشه
✔️
حداقل خرید 10گیگ.
✔️
با لینک ساب
✔️
بدونه محدودیت کاربر
✔️
چندین لوکیشن مختلف
✔️
بدونه کوچیکترین ضریب مصرفی
🔽
🔽
🔽
🔽
🔽
🔽
🔽
🔽
🔽
🔽
🔽
فقط فقط گیگی
5⃣
1⃣
هزار
✔️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
فقط فقط گیگی
5⃣
1⃣
هزار
✔️
https://t.me/V2ray_confing1
@aMi41garavand12
😎
چطوری اعتماد کنی؟ چنل اعتماد
https://t.me/v2rayaMirconfing</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123804" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123803">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8MHmv16FWOsgyl9Wpd2YhWn3gLwc93EXm7UuQxbpqVsCYYVlOBuSTYUE5wwNzrds_p1yIOeAz-CpsDBqrpcKYwMAnWxVug6sv_EQqMYPFqVW3h_9nzNtOvQgyhyfhW-XQbJyZxgWf1FD_1ji4WWqtEgUoXY6o8HdCiGOzGr2dFNyJrobzkY1iDMtBdA6xCC3Mfjzf2Es2ScwRenP1CxAzQGFzv7ibLZjZbcKCU-LxdK_JaSRr7HdZA-nK5kswjtR5UANEBAtBmHnzZRRulHqLQqEYGAZ2dR34e80eU-1L_k3XoIBDGkplcAdviwvjeQwP9OOTWRJ3U-kpZ5ueYFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا مدعی است که در جریان این جنگ، دست‌کم ۱۶۰ شناور دریایی ایران را غرق کرده است. هر یک از این شناورها می‌تواند منبعی بالقوه برای آلودگی باشد. وقوع یک نشت جدی در تنگه، مهار آن را بسیار دشوارتر از حالت معمول خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123803" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123802">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
به گزارش منابع خبری ، صدای انفجار در سراسر بوستون بزرگترین شهر در ایالت ماساچوست واقع در آمریکا شنیده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123802" target="_blank">📅 22:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123801">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsQjMoiEa1Hxs7G3MbzVE9AUowDvQkzENNjwtn4BwUKFcTKU8qbUjxWSVKyaERTUKh0_bdZPn-obUo6cF499kGtDMzR-fg-BEMxAbO3O8wVuDT9E2YkQ_HG8zkA0LwslwzHNtYGc9azAEEHwxnm41nydRRo4TIU10h8PXxegLx0WK6NOIwUYP0OKnU4fsl1DU5ioKWJ_SPunmHlmt7VIzjF_Z_AEYA8tk6XVoW-8TtuAwzafvzpRkhpDKkDTYpu-jNtXBL0MirFsCy1sfUPALNmwXJFPZ3VGDI8h8mpXksVUhPm80BL3LcKef9sxFlFkNpoRTJwe-YSTx8ZbduecAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: چرا نمی‌ذارید صداسیما سخنان رهبر درگذشته در مخالفت در مذاکره را پخش کند؟
🔴
نماینده مجلس: جای تاسف است که رئیس جمهور در دیدار اخیرش با مسئولان صداوسیما به آنها فشار آورده که چرا صحبت‌های رهبر فقید در مخالفت با مذاکره با امریکا را پخش میکنید؛ عده‌ای…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123801" target="_blank">📅 22:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123800">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
شبکه 12 اسرائیل: ارتش یک طرح تهاجمی در عمق لبنان آماده کرده است که منتظر تایید سطح سیاسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123800" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123799">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uk3uTHG15QOCQYqoOmNYmRY6Pe65FK3YeATKaZq7dRD6AmbRaTupzJKAsjYkfwZbj2DZlxL17lC6Q8jX7WvCTBTvKA1l53PHjJ0MAZ9HdGwqj7aEy5AGwxJyWgzKN1OUQydWtRyEhoTt84G-c-otp5JjK1UilLthO6UzUggcvKo4WPGIjNRIE6Bx77aRZs3H12GCBSFZzbXfhddyYtMhlNhIyia1IZn6qIQtksRUSn3hZitUhP6xfvrexxcDgPSGZgtu5slJbdLoEQloniuCogJX3zbkRpUip8Xui0_XZN3kZOas7VCfScMJvdu39XWKd003eEIHyNCraAnOMH9gLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موجودی انبارهای آلومینیوم به سرعت در حال کاهش است
🔴
ذخایر موجود در انبارهای بورس‌های کالایی، نیاز جهانی آلومینیوم را برای کمتر از ۵ روز پوشش می‌دهد.
🔴
نمودار فلزات و میزان پوشش ذخایر:
🔴
نیکل: حدود 31 روز
🔴
سرب: حدود 29 روز
🔴
قلع: حدود 21 روز
🔴
مس: حدود 13 روز
🔴
روی: حدود 6 روز
🔴
آلومینیوم: حدود 3 تا 4 روز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123799" target="_blank">📅 22:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123798">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7AU3spuar8r7ql4Vb9jMkpoqraB9ampMr5nMCB0oYjpTN7WgGmwzqW-aWcUaUc2_VOqlXOdzfoa35_rezoZgykVvDzfKyHYMoRjwIG64TZ8QYex97-Zx6i3BwB8rmwR8UPOT_5Y3tMQz7zDxHoatTrw-jfZlKxzw4Sj5emylsAqjFQm-w1kDZV0ypqUyqveGG9wVlxcgdDm-unizMmnTwG9GrTbsj2jiBOFt-moFsocU91R2N1IoGJUYeRYcbAzqn1zBDWIrw9FyXB_bOPWCuuAbBaGdec1CIQXK_wk6nqfFqLEAo_pHsjEhwM-wVOE6QVWrM17nc2bcknjceyX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: چرا نمی‌ذارید صداسیما سخنان رهبر درگذشته در مخالفت در مذاکره را پخش کند؟
🔴
نماینده مجلس: جای تاسف است که رئیس جمهور در دیدار اخیرش با مسئولان صداوسیما به آنها فشار آورده که چرا صحبت‌های رهبر فقید در مخالفت با مذاکره با امریکا را پخش میکنید؛ عده‌ای هم به ما میگویند سکوت کنید تا وحدت بهم نخورد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/123798" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123796">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3bcc37acf.mp4?token=Orc08PIWQMB9FTtxc3kcmBq7Y2rrZbxR3sJ3_w-0R9MyTLohbmVZWC2aJehykRdvvSGdIugdvciXdtelz6n0N2nfaRVfhSZh_XfYJIvVFy5DVN5Yv7XegHNpCn_U-J_PpIMIYYsRD0Aw5jcQqdPL5JbF1UtXGj5H2Iv_SlZD8Ujav88Ku9_3CDABpdxss5wAD1lp6x20k80lPif-iLUdZGtcsGfMMCWB3Jz58q89wfXzIKYJ2fFrhD2irPTcw-mlSB13y10pADGwIaI6Lpk9N89Mq7C6SK_OdSvnDWju2IOIaEbOJUNvA9GdeXZo5GdG6wxdgvSpGDUcVNY95Rzkzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3bcc37acf.mp4?token=Orc08PIWQMB9FTtxc3kcmBq7Y2rrZbxR3sJ3_w-0R9MyTLohbmVZWC2aJehykRdvvSGdIugdvciXdtelz6n0N2nfaRVfhSZh_XfYJIvVFy5DVN5Yv7XegHNpCn_U-J_PpIMIYYsRD0Aw5jcQqdPL5JbF1UtXGj5H2Iv_SlZD8Ujav88Ku9_3CDABpdxss5wAD1lp6x20k80lPif-iLUdZGtcsGfMMCWB3Jz58q89wfXzIKYJ2fFrhD2irPTcw-mlSB13y10pADGwIaI6Lpk9N89Mq7C6SK_OdSvnDWju2IOIaEbOJUNvA9GdeXZo5GdG6wxdgvSpGDUcVNY95Rzkzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز امشبِ جنگنده‌های ارتش ایران شهر"
کرج
"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123796" target="_blank">📅 22:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزارت بهداشت لبنان گزارش می‌دهد که از زمان آغاز تهاجم در ۲ مارس، ۳۳۷۱ نفر کشته و ۱۰۱۲۹ نفر در حملات اسرائیل زخمی شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123795" target="_blank">📅 22:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123794">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
این هفته شاخص فرابنفش بالا است، تا جای ممکن در ساعات میانی روز(ساعات۹-۱۵، با توجه به داده‌ها) کمتر در برابر تابش مستقیم خورشید قرار بگیرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/123794" target="_blank">📅 22:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123793">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">💔
همه اعضای این خانواده جاوید نام شدن.
🔴
جاویدنام بیژن مصطفوی، ۵۸ ساله، بازنشسته آموزش و پرورش، رزمنده جنگ ایران و عراق
🔴
جاویدنام زهرابنی‌عامریان، ۴۸ ساله، بازنشسته تامین اجتماعی
🔴
جاویدنام دانیال مصطفوی، ۲۰ ساله، دانشجوی کامپیوتر
🔴
اصالتا از شهرستان سنقر،…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123793" target="_blank">📅 22:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123792">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کارول ناوروتسکی، رئیس‌جمهور لهستان:
متأسفانه، رئیس‌جمهور زلنسکی نشان داده است که اوکراین به دلیل حمایت از راهزنان و قاتلانِ ارتش شورشی اوکراین (UPA)، آمادگیِ عضویت در خانواده اروپایی را ندارد.
🔴
در خانواده اروپایی برای راهزنان و قاتلانی که زنان و کودکان را کشتند و لهستانی‌ها را به قتل رساندند، جایی وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/123792" target="_blank">📅 22:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123791">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAdGZMoT9TH4Qg68KIQIC0zbYclSE3cGTsySTE54hqsSC3xW32oTM-A6ZsY8s9aT5xcIhIopQ-i_OBTEI0_WVmRuoPe9zYZ-cQ7n092dUjgcKFOc79i0N38tBfAxeoJU8T7GVs04BXZlvUMJr8sENFUgz6n_Vf0RDSDX2zDPPHL-ymT0q3YY1OHB1s4lgtpq2kxk1eLBXG5liE-6a0figSRc638f4morEGquenMmskIkup4-Wi3PYItYiL5GPAUNg-CvM3tddZNecer616w2nezXwxFBn-BkKD_YE2qotFyLHAY7B85FY4GcVusydd0nxfdnsTfr89xvjSR7XACOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام اعلام کرد کشتی تجاری Lian Star که از یک بندر ایران خارج شده بود پس از 20 هشدار توقف و عدم توجه آن توسط یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت و در دریای عمان توقیف شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123791" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123789">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سازمان رادیو و تلویزیون اسرائیل مدعی شد: ارزیابی‌های آمریکا و اسرائیل بر این است که حزب‌الله با هدف کارشکنی در مذاکرات اقدام به حملات موشکی می‌کند.
🔴
انتظار می‌رود مذاکرات بین نمایندگان نظامی اسرائیل و لبنان در هفته آینده نیز ادامه یابد. نتانیاهو طرح را به کابینه امنیتی ارائه داد که به موجب آن دامنه کنترل بر غزه گسترش می‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/123789" target="_blank">📅 21:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123788">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
صداوسیما جزئیات غیررسمی از یادداشت تفاهم [ایران و آمریکا] را منتشر کرد:
🔴
موضوع آزادسازی منابع بلوکه شده ایران از مهمترین بندهای رونوشت غیررسمی چارچوب تفاهم اسلام آباد است.
🔴
بر این اساس آمریکا متعهد شده طی ۶۰ روز امکان دسترسی کامل ایران به ۱۲ میلیارد دلار از دارایی‌هایش را فراهم کند.
🔴
به گونه‌ای که این منابع قابلیت انتقال و هزینه کرد در بانک‌های مقصد موردنظر ایران را بدون محدودیت داشته باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123788" target="_blank">📅 21:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123787">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سنتکام :  تا الان مسیر ۱۱۶ کشتی تجاری عوض کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123787" target="_blank">📅 21:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123786">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، وزیر دفاع کاتز، رئیس ستاد کل ارتش اسرائیل و مقامات ارشد امنیتی امشب جلسه‌ای برای ارزیابی امنیتی برگزار خواهند کرد، گزارش کانال ۱۲.
🔴
بحث‌ها بر تشدید تنش‌ها در شمال اسرائیل و سخت‌گیری در دستورالعمل‌های فرماندهی جبهه داخلی متمرکز خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123786" target="_blank">📅 21:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123785">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مهدی خانعلی‌زاده، عضو رسانه‌ای هیات مذاکره‌کننده جمهوری اسلامی، نوشت: جمهوری اسلامی هیچ پولی در قطر ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123785" target="_blank">📅 21:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123784">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کانال 12 اسرائیل: حزب الله در 48 ساعت اخیر 100 موشک و پهپاد به سمت شمال اسرائیل پرتاب کرده است،
ارتش اسرائیلی در حال تدارک برای حمله گسترده در بیروت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123784" target="_blank">📅 21:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123783">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e34f3b02.mp4?token=cn5mC4NawJZf4hRMcn4OB3X9p5XOQ1rBwlwo80SRWRzHIi13dJ_-wTaDdqnxpQML4myjhThlUI53CY6Svvp3hWoOeVXCduUp0v9cXTHmKFZsU7R2vtFq2sed-TlO3qr5OcVhd2eek9jMIQMjxcAvZAlTkdory543W8XE8E0WpeltfTqdHI484hs0gO0s2QYzEjD54pENmn26SPdJi-2fQ6WQkQUNMpZ2Eo7MuCM45zVrEIRY-Ucxf8XrFRNRy9dZJWYNYQzknsi7AiTYVcNdhamLLejlHLxakMc4q3Wab2zs1A00bnmQbPWwOfKAsnUMTx8k3utDdV6qTqB9kDcyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e34f3b02.mp4?token=cn5mC4NawJZf4hRMcn4OB3X9p5XOQ1rBwlwo80SRWRzHIi13dJ_-wTaDdqnxpQML4myjhThlUI53CY6Svvp3hWoOeVXCduUp0v9cXTHmKFZsU7R2vtFq2sed-TlO3qr5OcVhd2eek9jMIQMjxcAvZAlTkdory543W8XE8E0WpeltfTqdHI484hs0gO0s2QYzEjD54pENmn26SPdJi-2fQ6WQkQUNMpZ2Eo7MuCM45zVrEIRY-Ucxf8XrFRNRy9dZJWYNYQzknsi7AiTYVcNdhamLLejlHLxakMc4q3Wab2zs1A00bnmQbPWwOfKAsnUMTx8k3utDdV6qTqB9kDcyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جزئیاتی جدید و غیررسمی از یادداشت تفاهم احتمالی ایران و آمریکا
🔴
گزارش صدا و سیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123783" target="_blank">📅 21:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123782">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
الجزیره: ترامپ برای جلوگیری از جنگ با ایران پیش از جام جهانی بسیار مصمم است
🔴
او همچنان برای دستیابی به یک توافق موقت با تهران تحت فشار است، اما پیشرفت فوری بعید به نظر می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123782" target="_blank">📅 21:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123781">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1713e4ae.mp4?token=uxAJoE8429FERMfFSrYu2GaMXcgVPtUVJXVABhIKLyvrbZTLWujefWNDZP4ECvd7SZvTU8AyAmUkqnK3X1rwFQGMxysl5Fl4YYbXhm_wL1E14bQ2HEIMyeqBpDemreSsOkMn3SNqUFoe0doCRlrJcvxinJzryaFhosqos8JYPjpT1ATUAa1j73Nmao-WS_E2yWF1p_m7mLEWqiW7qAnGDeUp37W1dH5_kk_s3kMmDGbAEz71bXtQL5PZPMTzKBpOxAokvoiWYzlpiF8FRGKMjpDYqen_gdPGNnC53swGgo8Qmf2_EcL5GDa018AIF4A1YZyLLFwe-ct5TV8DcL1k-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1713e4ae.mp4?token=uxAJoE8429FERMfFSrYu2GaMXcgVPtUVJXVABhIKLyvrbZTLWujefWNDZP4ECvd7SZvTU8AyAmUkqnK3X1rwFQGMxysl5Fl4YYbXhm_wL1E14bQ2HEIMyeqBpDemreSsOkMn3SNqUFoe0doCRlrJcvxinJzryaFhosqos8JYPjpT1ATUAa1j73Nmao-WS_E2yWF1p_m7mLEWqiW7qAnGDeUp37W1dH5_kk_s3kMmDGbAEz71bXtQL5PZPMTzKBpOxAokvoiWYzlpiF8FRGKMjpDYqen_gdPGNnC53swGgo8Qmf2_EcL5GDa018AIF4A1YZyLLFwe-ct5TV8DcL1k-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلللللل مساااوی پاری‌سن‌ژرمن به ارسنااال توووسط دمبلههه دقیقه 65
@AloSport</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123781" target="_blank">📅 21:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123780">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/123780" target="_blank">📅 21:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123779">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C5gloSiXES-9Lz6fQcfzzno7qdMyvunMfzSQVS9dThHml6T3jM5IthVB1-93oL6gLlH987SxKSe-Qx8_EvCeNsnL-oSAjLSMB-ftDA-iJQiTjJwK4v7G03FDFsz3EZal6IfKUQwYdEwCrBe5oTSp1cfLRF9T5iDCpeSM3K8S_UAlm2kb3Yrjs7bmk5E81YSm1KV6beA0WrOVXVEZpZJLD_Cnj900UuWFbrQk3eFlL_4ZNt_9YLNH4R4newcRUMzI7zn3x2QGPfPzNQjGkIJPgwEoBY_aNK6IejX1Y7pV7QJwiSHnoJSe9xLRQyXg7S5dNuanJ4KUICmKMyc4dMHHNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/123779" target="_blank">📅 21:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123778">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
معاون هوانوردی سازمان هواپیمایی: بیش از ۹۰ درصد از بلیت‌های پروازهای لغوشده تعیین‌تکلیف و وجه آنها برگشت داده شده است؛ ۱۰ درصد باقی‌مانده نیز افرادی هستند که هنوز برای استرداد بلیت خود اقدام نکرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123778" target="_blank">📅 20:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123777">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2BQTfZbRGjmvBxGKceefiL9gdvcVVlAHTRm7C0Xdnuk5ruhNEFFxymCzSTh6MUhb4pchQrFtaktvgnw9tiFvBASTyy3mb4pzaK45WsU_FoLWv_VJ2Zb_h5llNfP1huRvHG0eBhA4sz3lP9TqSa4Pi9bzKzrHxPKa-EU1sNusAKEjt5T0CISCTTw3YxGROkMy3EY4eqIjXrVV8BlyuX6iD-pLs-Gthb-ScrXLf23iKaNeS9_yNzyiIa5tTncK5KHTl4CPOX14F6I2DNPLxvdpO92U4GjaOJfcjM0sTaIw20cyRdr7492_zwW2LLNj_uFjCKsvL5iFYP_mv3N7fzXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیمام خیلی جالبه فوتبال دزدی پخش میکنه بعد کنار زمین تبلیغ بیمه قسطی میکنه وسط زمینم تبلیغ تشک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123777" target="_blank">📅 20:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123776">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل : نتانیاهو، قراره به‌زودی یه جلسه امنیتی برگزار کنه تا درباره نحوه پاسخ به شدت گرفتن حملات حزب‌الله تصمیم بگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123776" target="_blank">📅 20:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123775">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پزشک رئیس‌جمهور آمریکا: ترامپ با «تورم ساق پا» و نیز «کبودی خوش‌خیم» دست دست‌وپنجه نرم می‌کند، اما همچنان از وضعیت سلامت «عالی» برخوردار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123775" target="_blank">📅 20:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358ce379f1.mp4?token=vPBxRWOXVKMi3-uAUZJ_-6emD9MUshZGaPw_lSZAVpFyJ7LahC7KtrFO1m4HFup8SRsSLMKlQpQEmK-uuUX--aozQWcn3uIGMr4Fnue4d-ogK9SXksaCaTAz0DT2i9lLB7MOgGuZLoQj815DzPshZWhoA-qCXF-_tJ0H1RTQ5xihhOmLeCs1DnLvlbxjyPbViGQSfM8RkfvCho9RsAsm1-8btXTELwW5UlVYcCaSa8yD0m3QL1_2lSlDu6a1FTqM-Z8VyE-h2NTpVoOyS-yPFsnNxHprTxCjjqgc95M1u0dHFY0zgcpBLOL1Wk3zFGlGD46ABgrm08MkEn_-s707tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358ce379f1.mp4?token=vPBxRWOXVKMi3-uAUZJ_-6emD9MUshZGaPw_lSZAVpFyJ7LahC7KtrFO1m4HFup8SRsSLMKlQpQEmK-uuUX--aozQWcn3uIGMr4Fnue4d-ogK9SXksaCaTAz0DT2i9lLB7MOgGuZLoQj815DzPshZWhoA-qCXF-_tJ0H1RTQ5xihhOmLeCs1DnLvlbxjyPbViGQSfM8RkfvCho9RsAsm1-8btXTELwW5UlVYcCaSa8yD0m3QL1_2lSlDu6a1FTqM-Z8VyE-h2NTpVoOyS-yPFsnNxHprTxCjjqgc95M1u0dHFY0zgcpBLOL1Wk3zFGlGD46ABgrm08MkEn_-s707tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاطمه مهاجرانی، سخنگوی دولت:
دولت پول بازسازی خانه هایی که در جنگ تخریب شده را نمی دهد، چنانچه تصمیم بگیرند خودشان بازسازی کنند، دولت مجوز ساخت دو طبقه بیشتر می‌دهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123774" target="_blank">📅 20:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123773">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBDYzhJ8kul2g2EJ4KXI1mCavS1t-ns3kkoLnt46QSOqhIIvRHaiVXPpW0cdh9QLwr_Y2yFGXlDgGTPM5R_2Na9mVbbSUZ_2nEZK3ZgpBWPH_jSnSgxdah9RsAqqZF94sPGQCOZeeniPaB3T9LEgYn13FsTjmi-lSz4nbugv9KvY4S4lMsGN0ayWE3SOjLtHiMvl3Yd-FziR2y_T5B0YBp3nd6oKrERkIznf4eE_235IB54_BizzYps2IozbtG2E0iic0IdmHccI6lcjYLpNjGwq60LG_tCtyrBKHCiCAG1QTmps3v7bk7NIdZgDRe38ZouioGf2RfDLwMDPzAPe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ در طریق Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123773" target="_blank">📅 20:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123772">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xi38hlcCmu6tl5oqq2fzGn2jwbC0mXlVxONa9lt761bb5jPLO0lyUFzwXirV94TS5VXhnaY85wqRGZIoMe3QtJCP5KCP9mUy8JdCMp0p-0B7OcMJbLZvasUPsP7BfgXSiZnRlHXIPBankhliDFMi88G5VKDKSaDDQjfVABJmYcaVA3Y4e_kxyabbqZQoOK0ks261tf3SbN8hAyKZbihUvSw6TW3HWjDqX2DBVxSml0TA95bdIYeLjXI6aPJuralv8UI3ZBze7KuoWdhN5208FC8fvnOYkXvaU4nc8vpvYjOp8Q4GmjWez-sp3IT8li2qs9saZU9jJIDTcS6OGJxA_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در شبکه اجتماعی «تروث سوشال» درباره «سندرم جنون ترامپ» پستی منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123772" target="_blank">📅 20:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123771">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lryYXdUvQ-SWg684VpcALSSfK9gwj42ZkdDTSE1YjULD4Zmk_m3m7eOenf13NAlJgPr2gcBDadu7cc5fw8UNd0u_ZH4HMyZs9SJb6h_oiF5buo-M7KxQkePp31uTwXocxfYJN8_JUTKLs84Ywtgt6iaGQww7_RSntuDLTGfdLdrn1ioupsGAashehZqeg_pOtKQWlkD-TRkGXGYdUqxlZ53-r23b-8qC4O3HaZe8r_Z0zmH0iYRmrkHNHjpTbBh6h4KPtWCvTxGxdUAXZMXx7YHYB8kcqx3xI8NrHSL5a67gvyzzU7rehFAAS3Ib93x8rqpZxUGoLse2FGghfrVFbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
می‌دانم که هنرمندان دچار «ییپس» شده‌اند و نگران اجرای خود در روز چهارشنبه هستند، بنابراین دارم به آوردن جذاب‌ترین شماره یک در هر جای دنیا فکر می‌کنم، مردی که مخاطبان بسیار بزرگ‌تری نسبت به الویس در اوجش دارد و این کار را بدون گیتار انجام می‌دهد، مردی که کشور ما را بیشتر از هر کس دیگری دوست دارد و مردی که برخی می‌گویند بزرگ‌ترین رئیس‌جمهور تاریخ است (THE GOAT!)، دونالد ج. ترامپ، برای جایگزینی این «هنرمندان» درجه سوم و بسیار پردرآمد، و ایراد یک سخنرانی مهم که کشور را به جلو سوق دهد، همانطور که از زمان ریاست‌جمهوری‌ام انجام داده‌ام!
🔴
دو سال پیش، ایالات متحده مرده بود. اکنون ما «داغ‌ترین» کشور در هر جای دنیا هستیم. من هنرمندان به اصطلاحی که پول زیادی می‌گیرند و راضی نیستند را نمی‌خواهم. من فقط می‌خواهم در کنار مردم خوشحال، باهوش، موفق و کسانی باشم که می‌دانند چگونه پیروز شوند.
🔴
پس، با کپی این حقیقت، به نمایندگانم دستور می‌دهم امکان‌سنجی برگزاری تجمع «آمریکا بازگشته است» را در روز چهارشنبه، واشنگتن دی.سی، همان زمان و مکان بررسی کنند. فقط میهن‌پرستان بزرگ دعوت خواهند شد — این جشن وحشیانه و زیبایی از آمریکا خواهد بود!
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123771" target="_blank">📅 20:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123770">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
دلار در بازار آزاد تهران: ۱۶۹ هزار و ۷۰۰ تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123770" target="_blank">📅 20:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123769">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou2nQ9W2EvniGE5iFvv-gsXpf27EByw5H-7ijoNuAw_Dfij3NBjvnc-kWDfUKHvbwsdysGMEEcjX0AxsMunIaDxyqTwVelDfFas_TsQf8VhYDkr2zAVbjqNXeh_1_YvY3-gVRkKT76rp_-DDcldsvSGZmRvAsQOb7d-W42eEkw9xUa_dbPwi3BdF-3ry99C1TPcHFWFv7PsbfJBnN-ShExzDjYzbmANr3X4otIOWEBO4iT8sgeim_PwIaMWVGf_kNv0YKLbjElQ5E0f7YIav5-0IbGruEHjNhPEvRPhK-fnls1NaVYTfOQ6vsPQXwjAz9UeCj5ckNbUyHe82Yon2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتلانتیک
:
تلاش‌های دونالد ترامپ برای پایان دادن به جنگ ایران نشان می‌دهد که او همیشه در مورد مهارتی که برند خود را بر اساس آن بنا کرده، اغراق کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123769" target="_blank">📅 20:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123767">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
حزب‌الله ویدیوی جدیدی از حملات پهپاد FPV خود به مواضع ارتش اسرائیل منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123767" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123766">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی اعلام کرد ذخایر هسته‌ای یک نقطه اختلاف بین ایران و آمریکا است و برای کمک به حل آن آماده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123766" target="_blank">📅 20:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123764">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50be41a822.mp4?token=tBKN2ypnVFJyT80qkMLZTvtxKUgMRkRBTOyQlyqHDdNYGfOKbZUCIkCxtyqDJ1PSp5DSQE52-5ljLwj8bXmjqjGqAH6n3hvG9an32fa1PD-34KV6OY7org0ABnq4AXPpZwQKHqPnyN5TtLg9EQ26kQuz0gsPklQBBMfgs8Xovimd3_rG_Y4Fzyg8FYPg4dVFJCEw4eHmYJ-GpDeMVE30dn2dMcJdi4U6_AESxq94VHwqOY2rorevMTQgyuYPUzgipP25xHNImyRN_PTqHvbPz7b87PVzCEg0NEy5i37Nw2dELS6P5B6lrZ-RwlBsiYJNwAB6w-cWGL7-JcNyJ1eiKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50be41a822.mp4?token=tBKN2ypnVFJyT80qkMLZTvtxKUgMRkRBTOyQlyqHDdNYGfOKbZUCIkCxtyqDJ1PSp5DSQE52-5ljLwj8bXmjqjGqAH6n3hvG9an32fa1PD-34KV6OY7org0ABnq4AXPpZwQKHqPnyN5TtLg9EQ26kQuz0gsPklQBBMfgs8Xovimd3_rG_Y4Fzyg8FYPg4dVFJCEw4eHmYJ-GpDeMVE30dn2dMcJdi4U6_AESxq94VHwqOY2rorevMTQgyuYPUzgipP25xHNImyRN_PTqHvbPz7b87PVzCEg0NEy5i37Nw2dELS6P5B6lrZ-RwlBsiYJNwAB6w-cWGL7-JcNyJ1eiKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های شدیدِ ارتش اسرائیل ساعتی پیش، به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123764" target="_blank">📅 19:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123763">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: دوستی واقعی بین واشنگتن و اسلام‌آباد در حال شکل‌گیری است؛ این مدیون رهبری پاکستان است که به تلاش‌ها برای مذاکره با ایران کمک کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123763" target="_blank">📅 19:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123762">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6f96dc5.mp4?token=GlgnoohIKp2L7A1h7khaSTmsrNdmUMvxsgwXvCHMvEuxAFqszfvi9PUiBLjkYEjsK7hxoZ5Ne8A5xnfAWIuG-SUyke_o5vUDrvWJNuho4YvsErDxycywHnyKNDvaA1IxOS3BAwz1slQhl27K1Mm0igMiMDL4ra-Su2ZE_qgMxCqrs68y7HHsViYd5PUiGS4QLjIj5d01xnpurwUO_wHL1K6_PNcqYFTo-Z8Gwtui6gSwmQ27ECYPTETMS0w3mtX0GeBB0eyNvMRsNNlToDH78qijesgKQ11aN2_5D7n4UUj-iGM_4UBSmF4YLh6koSYh1X97roBXsRpWAsSccjBucg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6f96dc5.mp4?token=GlgnoohIKp2L7A1h7khaSTmsrNdmUMvxsgwXvCHMvEuxAFqszfvi9PUiBLjkYEjsK7hxoZ5Ne8A5xnfAWIuG-SUyke_o5vUDrvWJNuho4YvsErDxycywHnyKNDvaA1IxOS3BAwz1slQhl27K1Mm0igMiMDL4ra-Su2ZE_qgMxCqrs68y7HHsViYd5PUiGS4QLjIj5d01xnpurwUO_wHL1K6_PNcqYFTo-Z8Gwtui6gSwmQ27ECYPTETMS0w3mtX0GeBB0eyNvMRsNNlToDH78qijesgKQ11aN2_5D7n4UUj-iGM_4UBSmF4YLh6koSYh1X97roBXsRpWAsSccjBucg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6
@AloSport</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123762" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123761">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
هم اکنون نیروی دریایی ارتش آمریکا از شلیک و متوقف کردن یک کشتی تجاری ایرانی که قصد داشت به بنادر ایران وارد شود خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123761" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123760">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رضا پهلوی: مردم ایران از هدف قرار گرفتن زیرساخت‌ها خوشحال شدن  ‌
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123760" target="_blank">📅 19:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123759">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_zt6NovIToKVfjGsA7wTcWV1VaOvWFBIwVI_9J5TEuk2l9WEjeeqeTYENCNkLfuJdyNsSoEGXe3bTuItEcJ64zVjk4cqn2TXUBWVkNsb618sP4CkB-gj-WMSuqRabQ5kO56m7AshcLThjXU_7sqaUfPLIAap6OaTLGr4OpBm1m4vz4fTltGvt8O4q91R6Xm_5wnNX_WfWtYGfFQpuzG9ayqLk6Yl2DDOkVC8WkXoscYCFe5nseZm4h7wAdwKWIMomhjFJYtLGMUxW7LP9cPaCy2b9Hyx_Betnpo3ZfFjBkOgBpZ4O9QjYrdVPPlMUKg4nfi_6CqrUSXG0f_S_FjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی: مردم ایران از هدف قرار گرفتن زیرساخت‌ها خوشحال شدن
‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123759" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123758">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
مدیرعامل آروان کلاد: زمانبر بودن بهبود وضعیت اینترنت از نظر فنی فقط بهانه ست، نت رو گذاشتن رو حالتی که اگر خواستند سریع قطع یا وصل کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123758" target="_blank">📅 19:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123757">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مقام آمریکایی به AP :  یه کشتی تجاری که قصد داشت به سمت یکی از بنادر ایران بره، متوقف شده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123757" target="_blank">📅 19:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123756">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75424ce9f6.mp4?token=drqVWohNDzeOAXk_2ppttfpDS1pcAmW8DVdjAmvF6OcNtIZN_ZfLtnFIxgDNsYJ0gl7fyWPrusZIFRRSq38mOpzeezgcKqPGFgacAqW4KQKOUvDT9ekTjeDAgQ7B1vJnZhuUFDWHqbKWuLLP1JDqaQ09QrVgvyQpWCREAGp4-Qk4LCKaU0yVvdWUEC62rKdlpPMt9nT9p78N6mCvndhfl-Rut2cVCZf6Il-amE1G5Y1n7DzwcVsVTj5-2UAGo1rqpyD_iVS1GlMfyhQ3hfdXTIZoAQa_tmYM3Nz4H9ZQzCfobfodJkISEbRxUtKXKV88EqedpXp3ajIGLsdi06biOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75424ce9f6.mp4?token=drqVWohNDzeOAXk_2ppttfpDS1pcAmW8DVdjAmvF6OcNtIZN_ZfLtnFIxgDNsYJ0gl7fyWPrusZIFRRSq38mOpzeezgcKqPGFgacAqW4KQKOUvDT9ekTjeDAgQ7B1vJnZhuUFDWHqbKWuLLP1JDqaQ09QrVgvyQpWCREAGp4-Qk4LCKaU0yVvdWUEC62rKdlpPMt9nT9p78N6mCvndhfl-Rut2cVCZf6Il-amE1G5Y1n7DzwcVsVTj5-2UAGo1rqpyD_iVS1GlMfyhQ3hfdXTIZoAQa_tmYM3Nz4H9ZQzCfobfodJkISEbRxUtKXKV88EqedpXp3ajIGLsdi06biOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ بارها جی‌دی ونس را دست انداخته است
🔴
نیویورک تایمز گزارش داد دونالد ترامپ بارها در جلسات و محافل مختلف جی‌دی ونس را درباره مسائل سیاسی و شخصی مورد شوخی و انتقاد قرار داده است.
طبق این گزارش، ترامپ به مخالفت اولیه ونس با حمله به ایران، نتیجه سفر دیپلماتیک او به پاکستان، تعداد مرخصی‌هایش و حتی قطع کردن صحبت دیگران اشاره کرده است.
نیویورک تایمز همچنین نوشت ترامپ بارها ماجرای افتادن جام قهرمانی دانشگاه ایالتی اوهایو از دست ونس در یکی از مراسم‌های کاخ سفید را یادآوری کرده است.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123756" target="_blank">📅 19:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123755">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نماینده سیستان و بلوچستان در مجلس: برخی از مناطق زاهدان ۲۴ تا ۴۸ ساعت آب ندارند
🔴
ادامه بحران آب، استان را با چالش‌های امنیتی و اجتماعی روبه‌رو می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123755" target="_blank">📅 19:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123754">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مقام آمریکایی به AP :  یه کشتی تجاری که قصد داشت به سمت یکی از بنادر ایران بره، متوقف شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123754" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123752">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aadDHheP_iPGSIMX8t-tggOzYGxtx0nGPPLpPAdFPBATI8vVuS7GCszFRLnSb6-xbRGJWXR1H5pcEGR3lgC1ZYFSU4QwwpZhAbWCKRcrE0B-HJ6iTD-JMYGvsYGGJb3rhZFGNeGoH_a9f_aVlP6FiDg9UZTrBcV5kwe284FfZ9f9NMyeaAnOSyEN00Abl3s7_vra-fhssueIreKCxCiAmj8p_fR0MQvi5ouIGFrtHHklo81x1JLzSW6EvRKNnJ98GAq2Ix_YpJDdyQ01RyTYpg8vFaPocKrx1WudIxOwXTNGLy51HFGUaec1YYzz-YH-MnBmDiu-TgQ7oGkqjzxIzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4ojP6jrvB_vFR8uaWH_VLYjdkmLwbNYuA-cWUVRJwvq17qvpXvCiYnMyqdcITVAroKb86U3JfnTmx2eY5wKSfQubdPWiZPT3LIgazv3D30pAuCs1Kv2qfSSvI9GrdS0vPJ_8vyvclfqANgUtM_Hdj0fzuf6jy7ZnxreiXWrvl4u0zf_ZO-bvuW172osckbt3I8CuL-PhqRfozShaEws7VS2JS8rxlg6NPXS-L-hW6F_3G9e609sY_jyT8tDCdMpq5b1xJz_aG-lQ6d8E7SBojofADM6sotyovRJOWI417wKBA9Ld3pM3Iz_owZAM1madr-RHlBjXIKX1TVyQcz0tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سلفی حسین طاهری مداح و یک جان فدا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123752" target="_blank">📅 19:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123751">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BAbgjsLWmb60T3gLfRNOWZ70fIVjj4MZp8bBUcgHMOarondZhUSIxsY9mZ44jRKtJIYdrS1-XGVUovjaQy1gZbE9lV1UhUQC19seQTZcwq_q8Ung9DoOBfMoI6IEaSOEdZSNto6DP9W1rz-tZS7ghZbZQH1gdQrQsSaqkQA323dzvwyvbQCoxz0NFpAeoyDVGp96Z_l5gvFqpfVEvw_LRFE-x54YLpfux02WakDJ_puBXnL0bbRfJlAzKXZ85t9_SyePFd8HaYrodzLA69Cs5B6Nbh2xaVqFD5pjTn94ph7wFUev8K4Tz2BmZXOYck6zwvOSiihMGTBBnIMciFr7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌الانبیا در بیانیه‌ای اعلام کرد که هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی قرار خواهد گرفت.
🔴
در این بیانیه آمده: «هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.»
🔴
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفا ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123751" target="_blank">📅 19:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123748">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E1gF9Eulnp7KlNLmyXWOne5cNfl9onF3XCW7UH3uXN4Tbn8omYpjyoCnBHyMLZMjzc0flmW4X_5RzA4JADfP1YlXdEvp9s0gloSEUM89-gEeH7PkSZhZCrN-IMXIgugKQQ7uWA9-Or9shdG2ozPce-8zqyjjS0P-gf6hTf1zoAbk1Cx_BWQnNJ4OwwymwRjHZ2IEmUXfjtdx9pxO_3rgI2el_mT1oixjtYg3z9wyHynaasVDjZis378qT0Lk6nJ26RAF0nghB5V63juolLps_QcbiHapmjdGgzRBbgJO7o9sMWovmo7qDmJdEEce1PeuluEgIMvZIy41qLK1AWGL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hXSxWqSMoc93G0XWM0Udk3V2YwntTz550O3lcDPSi6uFNk2RXq_P0Hm0pZNxD32sKKeLcr78bDhCPqqPdCaVtNMZsHxmipxu8Glxv_6ocxi3DIRshbBpzwLX9vtv7EqWTnzWRNW0iOr0oT4ou_TlOkSLcvRtNZMsu25NTIr5sQKSHn5JtyBy2kJv-8ImaZkBmmIMMTENG4Cr-3-GJb0At2tX1szJx-dTmVkxTtOrQjDJw_xcbgD2an9Dy0o992imQe_Qd4ywhdRz9Jh-jP6RqKKRlRHTaupAN6FyG3U08b50Os7utnwch3xd0bTZfGOywkaSCg3tshPArS2Tg8pTsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a561eadb68.mp4?token=SlyliyK2s5opHpP2nsYPjgVmJZtk8eRcRgCYPc8lln7U5qgiPCnhPdk6HV7oqZhIssLSAitNMZZV0eO9d0G3_XBPW3OVgWLzuxB9AcWM8qc9axFE-DKsdnbWnooPPwno981E1XvR-b1q5Nof0fHLQp6alzeffx1gf3BIE6PlXcimggiSamczAmfAyvLZBd0w4QqM6jwU4MJvVZAlfFtCrjCVwXFYXYrNKmp3HhmXldJUSb2CKielLbkV0rifpUh80lZDoR6R_I-yNqgfCxXfW_22elPS7yxlaCM9OElr-qhQL5u5gacs7HycTg0Hi7MUk59GVQg2h0G5dZs57M99wg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a561eadb68.mp4?token=SlyliyK2s5opHpP2nsYPjgVmJZtk8eRcRgCYPc8lln7U5qgiPCnhPdk6HV7oqZhIssLSAitNMZZV0eO9d0G3_XBPW3OVgWLzuxB9AcWM8qc9axFE-DKsdnbWnooPPwno981E1XvR-b1q5Nof0fHLQp6alzeffx1gf3BIE6PlXcimggiSamczAmfAyvLZBd0w4QqM6jwU4MJvVZAlfFtCrjCVwXFYXYrNKmp3HhmXldJUSb2CKielLbkV0rifpUh80lZDoR6R_I-yNqgfCxXfW_22elPS7yxlaCM9OElr-qhQL5u5gacs7HycTg0Hi7MUk59GVQg2h0G5dZs57M99wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">8 اردیبهشت ماه یه زوج عروسی گرفتن و 20 میلیارد تومن خرج عروسی‌شون شده!! فقط یه میلیارد پول فیلمبردار دادن! اینم فیلم عروسی‌شونه.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123748" target="_blank">📅 19:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123747">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCWAHSCPVe3BYnYlbGRLHemgYW0dzHdFvJsSns9D4xOdbqjD0BRY2QNTpUCuMxwklIUclgE1m5TkJjQdblraX1jpQriO1x1lOPpy05jC878pLCepfxSDthNwsY_3fHBWaobD_Ic7Ab4Q8PelwUEVb95u8WLXqQGeagDZlsi2CqSEosBT_HjYTLjGeqpaa8Moh_dCrd9LnW6vRQ6vAGN3Jh_w7pyKhoDqjihZxjJEw2bnkTZZziVH8Gf1ITSUWtuxUwXtSm8-J9klRWLXfbdz2lnb7lNGc7eJ9o-AJ-stBW2KD9iV8AwF_pMhRKSco6oTkfmKBaaCdvAakeWg1bav7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
همه اعضای این خانواده جاوید نام شدن.
🔴
جاویدنام بیژن مصطفوی، ۵۸ ساله، بازنشسته آموزش و پرورش، رزمنده جنگ ایران و عراق
🔴
جاویدنام زهرابنی‌عامریان، ۴۸ ساله، بازنشسته تامین اجتماعی
🔴
جاویدنام دانیال مصطفوی، ۲۰ ساله، دانشجوی کامپیوتر
🔴
اصالتا از شهرستان سنقر، استان کرمانشاه
کشته شده ۱۹ دی ماه خونین ۴۰۴ در گوهردشت کرج
🤔
عرزشی حرام زاده بدونه که روز تسویه حساب باهاتون نزدیکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123747" target="_blank">📅 19:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123746">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سازمان ملل : سال ۲۰۲۷ گرم‌ترین سال ثبت خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/123746" target="_blank">📅 19:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123745">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
آزمون‌ساز برنامه شاد هم پولی شد!
‌
🔴
بسته‌های آزمون‌ساز شاد از ۷۴۹ هزار تومان تا ۳ میلیون تومان قیمت‌گذاری شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123745" target="_blank">📅 19:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123744">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123744" target="_blank">📅 19:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123743">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Is_lO2U3UaxQYiBWQfHr6AGmyg1i15SN1rY7aI1xEpvXp8Fq8btRZoWUOYbgOO-mnBwcMRJ5Lw4-NnQkyLCC24INAPwq9VZ56UrOO5mZOdVZjl9c23ZDuwryvs4iUHC4Rvhy5yHCpIYctxkTclUE_gKXlz0bOvnUdF8pjv9t6B0zw7jtcBiOGZmyFeuyPAQdJwrlX4te6FeJHWYP4DHcNIpyFttkdrWA1jEU3lzcYbF0qjy4vNxd79L5v0WsfBS9aYmMmKrTOVW_ohW4ccXfBYLyRNGmSnzkGpjvkCaRCHNJNeovMmQYECaNhBHZS0yegvZty2O6kqvQGjVAq50rPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/123743" target="_blank">📅 19:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123742">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وال استریت ژورنال | کاهش چشمگیر هزینه سرنگونی پهپادها: ارتش آمریکا راهکار جدیدی پیدا کرده است تا بدون صرف هزینه‌های کلانِ ۱ میلیون دلاری، پهپادها را در آسمان منهدم کند
🔴
روزنامه «وال‌استریت ژورنال» در گزارش جدید خود اعلام کرد ارتش آمریکا راهکار تازه‌ای برای انهدام پهپادها بدون نیاز به صرف هزینه‌های ۱ میلیون دلاری پیدا کرده است.
🔴
این روش جدید با به‌کارگیری خودروهای تاکتیکی ویژه مجهز به توپ‌ها و مهمات تخصصی، هزینه ساقط کردن پرنده‌های بدون سرنشین را به شدت کاهش می‌دهد.
🔴
در جریان یک آزمایش میدانی مشترک در فیلیپین، تفنگداران دریایی آمریکا با استفاده از این سیستم جدید تاکتیکی موفق شدند یک پهپاد مهاجم بال‌ثابت را با هزینه‌ای بسیار پایین‌تر از موشک‌های پدافندی متعارف، بر فراز دریای جنوبی چین سرنگون کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123742" target="_blank">📅 19:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123741">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JTT_n9zP1jWYgD3Q6TnY1_dJtwsRVcimCuqXIHP8xyEUigCwMQhogk3xXiSeDVWtrJshXOCpLKmLlykZvQPSthSzKFz1w9f7g-ZK2KXzGr4nNo4LaRI4MtDUDWLBIpblLNtQtc7GFjLAbWi5VJ_vIcpgTIfwV0GmYmQnLo4DYgFyIhVYn01wrvM9yZKXQd-IlCxrtRGuDIRanwFlxifjXw5-M_PjlXXrnOHY2p7Ki6D8zD1eNYakPjeGVbqVroaYx3vvbKMNrcWs5_1bnNUuIW6Tejz9cHU_MoohHVF11mG-dJp03AcYlgLxraQlYmMG9NnlcltBLokGoNKLbwDXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس دفتر کاخ سفید: جی‌دی ونس اغلب در جلسات با تلفن خود ور می‌رود و ترامپ به او گفته است این در شآن معاون اول رییس‌جمهور نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123741" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123740">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWHFWWaR07uXZ2Kx2ICp76nIk079A8eObqwNvdujNv9EVbJA9bpYXkK9vbxvYM5uG5JhyAuBefhE4gAWVV7-Ze0LW2gtRaaOqd2PyLtpq0rOZsCVOp9WQVoZhLTmygAck-lo5I4f9TLogAMi96JIHU9fRk2K-BSJYZnTC6SazT8JjdQWWz1LF6M8dkTwv9YC4YTb-zO3rsYPXCZeRMkAb3mBY198CNC6KN2YBrsqPunjgyyCoyfvNZRgLPjqwFHVaJttqKABSWZMeqkiSOyU5erAXtTvDrIs1JQb5rSiZ_mIIaGSwdhRVfrY99kEo0qbkw-VCgIaye_FcmUnefl5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123740" target="_blank">📅 18:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123739">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f215eac88.mp4?token=TrsZ4JQKj-qCiwCEPip-76QhwZGBcCmQOt7ckAmiygb53HeUS3Saq8oK16C5WVuzdhN-vagJNXke6e3IAtZ4AVB2rC_byvLqgvpkUAGWELnarN_7ilOV2Sh6khjylCPfM9SnypMqX_VShtFnqwjK0ZPI5_zBhhOXXxuyZk24_JSCFm1HZsD-J5ySkfphmxttaptxVCypn8GwHlbRc2kCGk8aMa5cvfvTTApvQ0urlQZn_g18RfOSd1BSADy_adY2K227IluPIFdobaFFKCmZ_ZW4GavFhc5hgV3kfAseWlIo4Tct-DFGpAcSLZhWVuKx-x8DPhxkwMwZoPlqMosSYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f215eac88.mp4?token=TrsZ4JQKj-qCiwCEPip-76QhwZGBcCmQOt7ckAmiygb53HeUS3Saq8oK16C5WVuzdhN-vagJNXke6e3IAtZ4AVB2rC_byvLqgvpkUAGWELnarN_7ilOV2Sh6khjylCPfM9SnypMqX_VShtFnqwjK0ZPI5_zBhhOXXxuyZk24_JSCFm1HZsD-J5ySkfphmxttaptxVCypn8GwHlbRc2kCGk8aMa5cvfvTTApvQ0urlQZn_g18RfOSd1BSADy_adY2K227IluPIFdobaFFKCmZ_ZW4GavFhc5hgV3kfAseWlIo4Tct-DFGpAcSLZhWVuKx-x8DPhxkwMwZoPlqMosSYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مک‌ینی از فاکس:
بلومبرگ گزارش می‌دهد که حملات موشکی ایران باعث مجروحیت چند آمریکایی در پایگاه هوایی کویت شده است. فکر می‌کنید وضعیت کجاست؟
🔴
میک جانسون، رئیس مجلس:
من دیشب با رئیس‌جمهور ترامپ صحبت کردم. او کاملاً روی این موضوع تمرکز کرده است. فکر می‌کنم رهبری جدید ایران می‌خواهد به این درگیری پایان دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123739" target="_blank">📅 18:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123738">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a2bd44da.mp4?token=ljgExvr5BFyIFqnVCPJXbJW0k5rIDdzbHyxhmVvTkMvyNibj-xGJOlLTow5g39xEv3IJhQl6phxA5e1ShRYXpH7GJciij7oHNrhrOhsot6htfaA45y6snilfswavjsJdQGxLwD1aCE_BGuRtm8XUbPa7gwV-tmb9VYoedpuOcfapuyOk9OLf96MJehiibzCYWy-pQxtgHAiO0-Jk23CPxe53K--htQkUE9bsSMcQa6iI4dB3tW0RUZhJMvCeNo2Nn19y4HKB_WyCo_dVryzb0KhJ9FuV-_1N4XmmP25D7k1bNusSy1aTcKLgsdgbTJBqqX3FuCrxDIuvPG2VaHPZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a2bd44da.mp4?token=ljgExvr5BFyIFqnVCPJXbJW0k5rIDdzbHyxhmVvTkMvyNibj-xGJOlLTow5g39xEv3IJhQl6phxA5e1ShRYXpH7GJciij7oHNrhrOhsot6htfaA45y6snilfswavjsJdQGxLwD1aCE_BGuRtm8XUbPa7gwV-tmb9VYoedpuOcfapuyOk9OLf96MJehiibzCYWy-pQxtgHAiO0-Jk23CPxe53K--htQkUE9bsSMcQa6iI4dB3tW0RUZhJMvCeNo2Nn19y4HKB_WyCo_dVryzb0KhJ9FuV-_1N4XmmP25D7k1bNusSy1aTcKLgsdgbTJBqqX3FuCrxDIuvPG2VaHPZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کا
رشناس صداوسیما : ما آریایی‌ نیستیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123738" target="_blank">📅 18:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123737">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-f2z-XaSmNgu77ZBgyhzJ70qzibFfMrymFeSquXAXsZwiaAGGlXbxdJqRXHMCeOwzC6k9RoFPElXK1K7mndT4IGLmVmVZKp9oevMH4W-JaiwANR-kPyqLSGVZ3ZAFaKah4qrrhj9wPBuz5STevQtL7q3FW1bnYI3OlRojDi4reC-rJfarDRhdBh0TJOqcmMKACeSkE41dy29aLWhMM2sl6fE4UawOEk0O91kcyLTy1tqAa9QK4_EiygLckVIk_aL4-TRHlyknyaPzJ1cDIrcG3JUWkBg2LWv1hzYl-KCM7GkyvvDk8Z0NdiKb4cJM2V6PDPX1coZPgDJ4BE7VxZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:
شاید عده‌ای به حرفم بخندن اما آمریکا تمام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123737" target="_blank">📅 18:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123736">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279e9c5133.mp4?token=hG__1niPZhtIxlcwOop74mmJqHW4FOQkqpBH3P56TB3eBzld68MpsDh9E-2q6vJEZUiyhvMlw_tOSj-ROsdgVgIFnkDN0UCjNR6d4qhSxevKAOjPdrditH_x5HhDskJ2UDZDIRBPrq-epdarF2sK0qEswI3h_nQstpCOHECro2-DKYHfGfM8E1coBwkK2J0YzfS6oA_6SMAKlYMD1WjxFopPzc3nDlIPo-AFmYbIiPhvC5JA1gPDAzIAsRKRQVIodLEIpWXigq1Tw7m7Ha5KpsUdiBAGyG9x5VPEPPLPH1HFqZtNZ18TuLb5YV-XWKNzuAXG2kMr_8UW3CWuMYTyYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279e9c5133.mp4?token=hG__1niPZhtIxlcwOop74mmJqHW4FOQkqpBH3P56TB3eBzld68MpsDh9E-2q6vJEZUiyhvMlw_tOSj-ROsdgVgIFnkDN0UCjNR6d4qhSxevKAOjPdrditH_x5HhDskJ2UDZDIRBPrq-epdarF2sK0qEswI3h_nQstpCOHECro2-DKYHfGfM8E1coBwkK2J0YzfS6oA_6SMAKlYMD1WjxFopPzc3nDlIPo-AFmYbIiPhvC5JA1gPDAzIAsRKRQVIodLEIpWXigq1Tw7m7Ha5KpsUdiBAGyG9x5VPEPPLPH1HFqZtNZ18TuLb5YV-XWKNzuAXG2kMr_8UW3CWuMYTyYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره ای از انهدام کامل ذاغه مهمات، و سایت پدافندی پایگاه هوایی اصفهان توسط آمریکا / اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123736" target="_blank">📅 18:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123735">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🔴
پرسپولیس رسما از آسیا جا ماند
🔻
دبیر سازمان لیگ: به دلیل اینکه باشگاه پرسپولیس در رتبه ششم جدول لیگ قرار دارد نمی‌تواند به رقابت‌های آسیایی معرفی شود.   کنفدراسیون فوتبال آسیا مهلت لازم را نداد که پس از برگزاری مسابقات لیگ برتر نمایندگان کشور جهت حضور در…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123735" target="_blank">📅 18:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123734">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
تلگراف: دو ژنرال قدرتمند، احمد وحیدی و محمد جعفری، با هم متحد شدن تا قالیباف رو از قدرت برکنار کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123734" target="_blank">📅 18:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123733">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
از صبح امروز هر ۲۲ دقیقه یکبار آژیر خطر در شمال اسرائیل به صدا در می‌آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123733" target="_blank">📅 18:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123732">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8c6e85a5.mp4?token=oprHMOZ7ku9vSd7-ovGU8JHX9xutuiFf7ytQn31zLKp5saPcij5WU4Dd6sfKSO5WkIHdBvE50NvCB6yD916Ckiz9wPNkGwkJm-P3fOESlq_R75PYpu4NVq5RJzWOfe8TGG-qF6xXV3e7oCzINHxgPYTyyFR47Cogv7G-KqMu3nN1eQoPPjYub2_sdPabwEsPi4ca7h0EMbDEDXn2ph7G46L3wKNOo8VVlX44y_cgA4UYYOFc2pxJoH-icgqV75I3aO1aPXLGZh-McTRDKfBgekoWNb_MAmk6UEe7HV-AEDrp1tldq65ee8WuY8uOO6LwsotczzSKvp4OXZhk1my1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8c6e85a5.mp4?token=oprHMOZ7ku9vSd7-ovGU8JHX9xutuiFf7ytQn31zLKp5saPcij5WU4Dd6sfKSO5WkIHdBvE50NvCB6yD916Ckiz9wPNkGwkJm-P3fOESlq_R75PYpu4NVq5RJzWOfe8TGG-qF6xXV3e7oCzINHxgPYTyyFR47Cogv7G-KqMu3nN1eQoPPjYub2_sdPabwEsPi4ca7h0EMbDEDXn2ph7G46L3wKNOo8VVlX44y_cgA4UYYOFc2pxJoH-icgqV75I3aO1aPXLGZh-McTRDKfBgekoWNb_MAmk6UEe7HV-AEDrp1tldq65ee8WuY8uOO6LwsotczzSKvp4OXZhk1my1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی که تازه از حمله‌های اسرائیل و آمریکا به خرم‌آباد تو جنگ ۴۰ روزه بیرون اومده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123732" target="_blank">📅 18:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123731">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c7efd305.mp4?token=iXpc7DlaSPN6biJVPUTM1LkBs7P93s-cd6J5CX2u-UZgDGsYuf-XFvjZ7VofieV4tZ5dmP4Y1j43NkIO14rj-3oTtaoIpj__HX-FpQZfRMXzOpkR1vTwITRG5K1Emq8KAhE0LNejxXis5npv0N5Eiz4xIUxx5YW51VfWk9Sg5Ec0XrJWa0HjFs1O5ADmK1ahKTaWkanBiPF6PzkVPjXTL9yeh-c8uKfhgSyz-LWgrYMEFNBDPHk0xuI_eG9f62K3bP8HH-VbJLhNNg9woEyQxfb911G68oTAmTffhAZJgL7hkR05Xv3ug7hOfyO4YajGZG0WQFAzfhU-f2LLKiLO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c7efd305.mp4?token=iXpc7DlaSPN6biJVPUTM1LkBs7P93s-cd6J5CX2u-UZgDGsYuf-XFvjZ7VofieV4tZ5dmP4Y1j43NkIO14rj-3oTtaoIpj__HX-FpQZfRMXzOpkR1vTwITRG5K1Emq8KAhE0LNejxXis5npv0N5Eiz4xIUxx5YW51VfWk9Sg5Ec0XrJWa0HjFs1O5ADmK1ahKTaWkanBiPF6PzkVPjXTL9yeh-c8uKfhgSyz-LWgrYMEFNBDPHk0xuI_eG9f62K3bP8HH-VbJLhNNg9woEyQxfb911G68oTAmTffhAZJgL7hkR05Xv3ug7hOfyO4YajGZG0WQFAzfhU-f2LLKiLO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاطمه مهاجرانی، سخنگوی دولت:
دولت پول بازسازی خانه هایی که در جنگ تخریب شده را نمی دهد، چنانچه تصمیم بگیرند خودشان باز سازی کنند، دولت مجوز ساخت دو طبقه بیشتر می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/123731" target="_blank">📅 17:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123729">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BP8DNs8VxGY967ILc6fjvws58A4JPrsutwLrW0aQspY4p4XyU8wybEcGpI-49yVoPmpxhZXROwqPS7jBczYEzzX7-B0fk18k6D3o5kzvminZ0gu-2fU4-d2I92XlQRo2GqMrMWUrCqQJUOlV2QCSOmp2NF4Vd4bDwUuIRLgYhq0U6a-X9IIws1eNY32X5S6lGc887_sqh8TGqT_lKzAGOv58HZ0HjuqGnOzx5TUdYATLbjWluS1vu5lKIozVEHoeJ3ozAEmXVFC10ktvP-slwew2d3Lpd5XfPL_X3GMAlQQAfiuCcMnbXy9dZ2SrcVohWSQtsxaTBO6MduONSA-QPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewKBERwkUHWTvSdXNaFuu1jNdQQvXpppSjZa4nKgZ4wLMiOEm4QPLTs4ND6uVpcCQIcXXcQbdkifg4GfSCuX3H6mbnRK3oOSdNzPHUpuZk37rpfcq3Wi29asGU5L5HZqoh7mqaCgFMyXkoExzR6KKL1JqCjXBpljM51wrpHoor4ZUSIYzxaNxKuGzo9QanMw7AdlIr0Lc9PBKDyOf5a0AcXplMh1FpYQWUm_YtcrXIgJw7ji6GQuezMdMcKDPq_MB0NdUA-GVx1yNQvYvSqDQRKhH4FOg8e_onQTdRiGAY-MJnKoHyDrU7-R7yMojpMmo1vdAWOId8yVIimOl49pcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون حملات به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123729" target="_blank">📅 17:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123728">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeEmzXykiJLMq4hq0mBZskEuvb-HUklHOPaw8QbZ30DwOMPUWch-VTIna3YKBTERh7nNMrdfX23dYZd8PStjXNbQWxE7uG-i6slIYAwKxoyRruuEcpytbCpWWOk1CXcmKfi-7lYqCSmN1NJCdIuqbEtN5PsWYN3N_VlnLCrDUDxBFOcMde7K9-V6TWmGBgES2s-u7pyXpTlPIhvrkBErscyvLgO9VA_XPsRkl0l1PyuMwWCweUaxGWoq5NWoNtHalQBJg2O6QHjOVdnHoBfoAkttJ9jyxjCkwC8e_Vz7JJcTjdHcO1tAok29BCA0a_NQVALEwoqWVnrRpzwE_IBF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ بین ۱۵٬۰۰۰ تا ۵۰٬۰۰۰ دلار سهام شرکت TKO Group Holdings را درست قبل از تبلیغ گسترده رویداد UFC در کاخ سفید خریداری کرد، گزارش نیویورک تایمز.
🔴
افشای مالی ثبت شده در ۸ مه نشان می‌دهد ترامپ این سهام را در ۲۵ مارس خریداری کرده است، کمی بیش از دو هفته پس از اعلام عمومی رویداد «Freedom Fights 250».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123728" target="_blank">📅 17:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123727">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f22528c0bd.mp4?token=Ljt1RHnj0pk_lzZotMGdFdyq-X_sic5keEcxE6QPA_E6HVxwOYypVfjBx2210LFkl-suHpH20rL_hoFtsqRxKaBcEFZbSy7YrLsO3u9guFgX5-USNyqCLcw1e48lV4h9VH25nW9iNBcknd8_q1F6lZR0HSM8b44JVKRF_71doxDdplTPYF2pjUhIiUbyFkbbmfCxfdCBEfn2o00WD1E0Hrbwp_t7QoLZ_r1fT3jY-s5ceKvRZiKIXZNg0vFedUD72A9voKfOFU8i8vvylhTC0KJ30XQR64DK95eoz4mWhTW-6jzfZ2mEgsxhB1Lhe-FNG4kWfrbz-vRdkrTVfS-OEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f22528c0bd.mp4?token=Ljt1RHnj0pk_lzZotMGdFdyq-X_sic5keEcxE6QPA_E6HVxwOYypVfjBx2210LFkl-suHpH20rL_hoFtsqRxKaBcEFZbSy7YrLsO3u9guFgX5-USNyqCLcw1e48lV4h9VH25nW9iNBcknd8_q1F6lZR0HSM8b44JVKRF_71doxDdplTPYF2pjUhIiUbyFkbbmfCxfdCBEfn2o00WD1E0Hrbwp_t7QoLZ_r1fT3jY-s5ceKvRZiKIXZNg0vFedUD72A9voKfOFU8i8vvylhTC0KJ30XQR64DK95eoz4mWhTW-6jzfZ2mEgsxhB1Lhe-FNG4kWfrbz-vRdkrTVfS-OEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس هواشناسی
:
ورود سامانه بارشی جدید به کشور از روز سه‌شنبه
🔴
وزش باد شدید با احتمال گرد و خاک در تهران پیش بینی می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123727" target="_blank">📅 17:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123726">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/123726" target="_blank">📅 17:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123725">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SLAON6rWnbcMUp_iXXkU-ePVCDWIkTNVvIlNqr1ft0IBzTPYr9LHqpfLF2Vcyn_rlSh3M_DxUWWZNEMVn1RWRZFFJ7pMtvx3TetDaWTUIE4LuFrD9KJwBzEB2Wc3kPFrgic_zXdnZsvWCYpf-WlXS2gKMnauhYLUEHMlaQoh9UtyvFQRocvGzR7EVU-gg13cYX-vQuoVhYcV9-wVEBqExY6HS_UzloKwkHpumoyLbsJRRYmBEErzOsiGVpce8vzabMYDOwwk9G7RIBwRI4oTTTmXGDFQFdxcvzSjOm9HfL6CNgr2TDnMxf_yAb5GrjiTLADltO3Avt7Z2tkZW-juPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باکسر به خاورمیانه نمی آید
🔴
به نظر می‌رسد که ناو آبی_خاکی یو‌اس‌اس باکسر (LHD-4) قرار نیست در حوزه مسئولیت سنت‌کام  مستقر شود. ناو آبی‌خاکی کلاس واسپ نیز امروز از بندر سِمبانوان در سنگاپور حرکت کرد؛ اگرچه اکنون به سمت شرق در حرکت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123725" target="_blank">📅 17:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123724">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ho3a6AJOxitY2Es2uJNTCSmhaLBnadADsWInE7PpO0U4PA7hv1TjjrNTWgXNKsaknbWjFvo5QSebjnJzGjuUvMejOAx3tD5JSYSWJnBJU4Hwx9ITdQ2WsOeebRsYLzqmr2yx4F6luug6GNnYSxG4sq8P-NtVZz7m3xofcyJVrVZMNnr90TctlNJz7N5yHvdKXWfIqoLB2WG-hbyXk-a3Pc6s8Y0VRTLbbBlFbYbrBTNs0oCf8hu65ujKbPclvMXOP-yNU8BNy3oADIP3vTIInKHhJMgZl2pheU99IOb8nyEA0goNw_Hkw0x7hcMgiUwRwRuDfCm-azqU4JQJppLEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123724" target="_blank">📅 17:26 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
