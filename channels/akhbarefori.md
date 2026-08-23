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
<img src="https://cdn4.telesco.pe/file/uOjE-jBvy0SBNKaCgzMCLwWI1S5i3llXovSkYAoRpq2UYvKJ4CzDBbLhkxxB9la7gjyjE7eO-1Vzma93lNGjiRau2JGiTg5b9O2scYlRu9029JH2D7QRLZzrRL8qH5arV6LjHRXvZhDhNnpoAsoGSVUdxCpDX0BKU2LkOIZOYi1gfYBJAyLXQi69Is-oluJJ2Vo4y8kmgb9OH09_Jo2ENL1iT07JjYwW3m6ZfdwaIcno2B-oFOobsXReM9FyDg-IOBBDldmGG6iavVs3EPwbc0TPsC-kf07dM9ZnRCILma0ybP0oaI_pQnHl4jDK0AYy8qp3KaF7W7W2NEsCqUGRMw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 14:42:52</div>
<hr>

<div class="tg-post" id="msg-683649">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21eaf8b00f.mp4?token=OlLaZm2VwzGjXHt5SMl_Iqik0EuQ3-uhOXyaKsB1GXeHNzkr2QFJi_8J1t-n33ORViaofEfZCDiQw2zqmJoaVvM772LV-OjkOASeNa-sPnDZPgFimdA50qnEZquBZRMysIg1NunRaYcYVJunc19LRdh683bb3g7HdO7dlqDRAC-rtzXwe1rqzRkFCu03O8fWW7pSOsIDvPDxkqwnoBluXIodEOob0-LPETeDNbPvHae3FS4zVWJhG_RzTvNRCuXnmQceftdijuIs1byNAub4gwjYYIZ0M1lOyOlEeCoFNs1Th0MXfbqJ5gJRYyO2C5Qp1WSmnHl6qP2sD8Dv0iP62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21eaf8b00f.mp4?token=OlLaZm2VwzGjXHt5SMl_Iqik0EuQ3-uhOXyaKsB1GXeHNzkr2QFJi_8J1t-n33ORViaofEfZCDiQw2zqmJoaVvM772LV-OjkOASeNa-sPnDZPgFimdA50qnEZquBZRMysIg1NunRaYcYVJunc19LRdh683bb3g7HdO7dlqDRAC-rtzXwe1rqzRkFCu03O8fWW7pSOsIDvPDxkqwnoBluXIodEOob0-LPETeDNbPvHae3FS4zVWJhG_RzTvNRCuXnmQceftdijuIs1byNAub4gwjYYIZ0M1lOyOlEeCoFNs1Th0MXfbqJ5gJRYyO2C5Qp1WSmnHl6qP2sD8Dv0iP62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیویورک آمریکا پس‌از بارش باران غرق شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/akhbarefori/683649" target="_blank">📅 14:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683648">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
حذف حبس برای مهریه‌های بالای ۱۴ سکه  نماینده نجف‌آباد در مجلس:
🔹
طرح اصلاح نحوۀ اجرای محکومیت‌های مالی در صحن علنی بررسی شد. با تصویب این طرح، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف شد.
🔹
در خصوص مهریه‌های زیر ۱۴ سکه، امکان اجرای احکام از طریق «پابند…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/akhbarefori/683648" target="_blank">📅 14:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683647">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس مرکز امور زنان و خانواده وزارت کشور: رشد اعتیاد، مصرف سیگار و مشروبات الکی در بین زنان ایرانی زیاد است و متاسفانه نمی‌توانیم آمار آن را اعلام کنیم/ خیلی‌ها می‌گویند اصلا در جامعه اسلامی نباید در خصوص این موضوعات صحبت کنید
پروین داد اندیش، مشاور وزیر و رییس مرکز امور زنان و خانواده وزارت کشور در
#گفتگو
با خبرفوری:
🔹
محققین می‌گفتند غلظت ماری جوانای مصرفی در ایران بیشتر از سایر کشورها است.
🔹
درباره زنان بی‌خانمان نگاه سلیقه‌ای است و می‌خواهند مسئله را پاک کنند، اما تاجایی که می‌دانم اگر به آقای پزشکیان مهلت بدهند، رویکردشان این است که با مسائل کارشناسانه برخورد می‌کنند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/akhbarefori/683647" target="_blank">📅 14:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683646">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5tfF7VlVL_rEAzJSwli012TqEz6QfwPxgLCFfsikkrEN0TCYzD-HNF0aNx3zaZVgBn3uOT31bYaTAdSLfU9fawUDK_6IMLRKHrSqWJ1_f7bbJvx6wmAsytQBbz6NdXWVzNxIBNjsimg87xizscFj_aLCZk8TyZSvENFyMPxco0G3sHGAEPTHn8b8FPjywFZzxIp2AfbOc62qKNNS55lNP2KAgzSONJzggandQq1YWBZjrLwfUGOJ1Z_dp1n691moIgfxf0PAcCnYCFybLSJiGSfpt_9eRJCAd3GTx1qZIjdDwY3lGNhffMuHvj8r7QaMK61FG7WIMvmc_Oa0hesLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد کانال دو میلیونی حامیان پزشکیان از عطریان‌فر و تیم اطلاع رسانی دولت/ آقای پزشکیان همانطور که بارها گفتی. اتلاف افکنی به نفع صهیونیست هاست/ عطریانفر اعتماد به نفس عجیبی دارد و در فضای سیاسی غرق شده است
🔹
انتقاد از دبیر شعام و نماینده رهبری را باب نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/akhbarefori/683646" target="_blank">📅 14:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683645">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405ef17751.mp4?token=PGuMiIH6DRu89MyDlqk0GQOklrb3ZfeGHAnn6_ZxORcAwc5zbXuGuZdFs1x4mWcdQ9PluvwcfcFbUuXu3ROK9uVsrsegpTPgtt64_NAmfG7RotKjdMGX_0a_3qanhi66XOfDNR_v0WNbF7EdlTubxl8nI9-00wCnLdrNm6viOf2sft_B5_afIf7tubX1TRtvL3UKayXgl-LPnxBTS2Q-gYy2DDjjbRBzy5xAGyIb2oLgX-2a4kEa_kpiGkK4Pvs-gzh8xR6Mcw1IoT1EFZ31HamSVEOmqUlnjCh8Q2l-qM0HI_1qAuyt9CtycETZIAkQbuLNnK5QITMMZZxC9M9dgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405ef17751.mp4?token=PGuMiIH6DRu89MyDlqk0GQOklrb3ZfeGHAnn6_ZxORcAwc5zbXuGuZdFs1x4mWcdQ9PluvwcfcFbUuXu3ROK9uVsrsegpTPgtt64_NAmfG7RotKjdMGX_0a_3qanhi66XOfDNR_v0WNbF7EdlTubxl8nI9-00wCnLdrNm6viOf2sft_B5_afIf7tubX1TRtvL3UKayXgl-LPnxBTS2Q-gYy2DDjjbRBzy5xAGyIb2oLgX-2a4kEa_kpiGkK4Pvs-gzh8xR6Mcw1IoT1EFZ31HamSVEOmqUlnjCh8Q2l-qM0HI_1qAuyt9CtycETZIAkQbuLNnK5QITMMZZxC9M9dgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مورچه‌های بافنده با کمک لاروهایشان لانه می‌سازند
🐜
🔹
مورچه‌های بافنده با استفاده از ابریشمی که لاروهایشان تولید می‌کنند، برگ‌ها را به هم می‌دوزند و لانه می‌سازند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/683645" target="_blank">📅 14:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683644">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05a479cdd2.mp4?token=P2EXkI_m9vCvoC1eiKDfNZTtFM2vf0dnVS3r4PfrgZwxkIVpIxWJxO5qNCuJmXuLTbYfKZT_5QWbqZPmdI7Jrr3tlteaJvqFbgzK8yZOyBWxMuqbtEcRrifme4EBJRD5i7zk4SsvfUmUO4GgdaCGExmGh5FTfqsay_TLx3pCGm3eKyiBTar0OJ6biAWCf5W1sQXObcJzb3hVT55eA9sb1pth2DYUzt94h25oLknS7pM4dW5nRrFG3jl6qVYKVT_GjFdClhtkkA4KJFZtI-XnlHlUJMVjrVl9GH_zr90rWUhoboLrsZi6EyVnQ0aWOn0fRy8475KtuHRydf6iLFwqQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05a479cdd2.mp4?token=P2EXkI_m9vCvoC1eiKDfNZTtFM2vf0dnVS3r4PfrgZwxkIVpIxWJxO5qNCuJmXuLTbYfKZT_5QWbqZPmdI7Jrr3tlteaJvqFbgzK8yZOyBWxMuqbtEcRrifme4EBJRD5i7zk4SsvfUmUO4GgdaCGExmGh5FTfqsay_TLx3pCGm3eKyiBTar0OJ6biAWCf5W1sQXObcJzb3hVT55eA9sb1pth2DYUzt94h25oLknS7pM4dW5nRrFG3jl6qVYKVT_GjFdClhtkkA4KJFZtI-XnlHlUJMVjrVl9GH_zr90rWUhoboLrsZi6EyVnQ0aWOn0fRy8475KtuHRydf6iLFwqQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/683644" target="_blank">📅 14:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683643">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
کشف ۷۰ هزار تلفن همراه احتکار شده
رئیس پلیس امنیت اقتصادی فراجا:
🔹
در مدت اخیر قیمت تلفن همراه به یکباره سه الی چهار برابر شده است.
🔹
همین موضوع باعث ایجاد حساسیت و فعال شدن تیم های عملیاتی شد که در یک فقره ۷۰ هزار دستگاه تلفن همراه به ارزش ۳ همت از ۶ شرکت کشف شد که احتکار کرده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/683643" target="_blank">📅 14:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683642">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a36cfee22c.mp4?token=J6HDpxL8SXCi9lxNLFoZ5cZC8gApXaQfBusFIZp_0YJU8UzBdJhqRGsB2UACuUflkWygZyd6ia6QI-fwF329xa64sqcPJm3Ev7REODMKaBvBFgfaKa1Coc_MPTkhdhw7Ut-NnFdkBlCad3hhggnNJ68jdXSsh-vTX-_4RkRpwwHeRTF0iGuHtiAAc0jHH9c91w1q_QUSapCSKvbiGcZdLynuvXs14oPsCTSV_X2V3zxfWn8Bk35kKM2bQ6_4KNBGKfFUwvWmjuM5LRr8MkZEXm-QoelAJRs2dDKSRSy3B86_3KQFWKZttSDcs6Kt1SL1kFkOdW7V3qxvCHPDSAUViiY8zu7iWu2wwqVL673JCPsWSZbSe259kBstquKjqE5yFxCaSaosq4ciIf1cCSY8Ok_V5niCjAUj-lL6-3H8nOj3-BtWv35otTAZdwZ1fVc6MeVZ-_HbjsTN6pAkRTjEqPyZmUTiUeLMvM6G0nSJe0yNn65NqlhQzw-qbn0HBtTN_-GsxF_BPbqYajEEVLLBM4E8QK4pvz5YrcTw9S4-qsrJVUqKiE82wTShDwB1phFkk3JSXSnDfuwIjEHbiGqUTpDs8URsNsAvQVQ6CZpoMxEGgHg3GfBaReasc0gOLZZbDVUJ5sFy6SFbgHMnrPfXqOAknNjuB-jK2X8uq4NlzOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a36cfee22c.mp4?token=J6HDpxL8SXCi9lxNLFoZ5cZC8gApXaQfBusFIZp_0YJU8UzBdJhqRGsB2UACuUflkWygZyd6ia6QI-fwF329xa64sqcPJm3Ev7REODMKaBvBFgfaKa1Coc_MPTkhdhw7Ut-NnFdkBlCad3hhggnNJ68jdXSsh-vTX-_4RkRpwwHeRTF0iGuHtiAAc0jHH9c91w1q_QUSapCSKvbiGcZdLynuvXs14oPsCTSV_X2V3zxfWn8Bk35kKM2bQ6_4KNBGKfFUwvWmjuM5LRr8MkZEXm-QoelAJRs2dDKSRSy3B86_3KQFWKZttSDcs6Kt1SL1kFkOdW7V3qxvCHPDSAUViiY8zu7iWu2wwqVL673JCPsWSZbSe259kBstquKjqE5yFxCaSaosq4ciIf1cCSY8Ok_V5niCjAUj-lL6-3H8nOj3-BtWv35otTAZdwZ1fVc6MeVZ-_HbjsTN6pAkRTjEqPyZmUTiUeLMvM6G0nSJe0yNn65NqlhQzw-qbn0HBtTN_-GsxF_BPbqYajEEVLLBM4E8QK4pvz5YrcTw9S4-qsrJVUqKiE82wTShDwB1phFkk3JSXSnDfuwIjEHbiGqUTpDs8URsNsAvQVQ6CZpoMxEGgHg3GfBaReasc0gOLZZbDVUJ5sFy6SFbgHMnrPfXqOAknNjuB-jK2X8uq4NlzOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک مدل بستن روسری که هم جلوی لباستو نمی‌پوشونه و هم مرتب می‌مونه و از روی سرت تکون نمی‌خوره
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/683642" target="_blank">📅 14:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683641">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر رفاه: معوقات بازنشستگان تا نهم شهریور پرداخت می‌شود.
🔹
آبفای تهران: ذخایر سدهای تهران ۲۶ درصد است.
🔹
نیروهای مسلح یمن از سرنگونی پهپاد جاسوسی عربستان در استان حجه خبر داد.
🔹
طرح ممنوعیت حجاب در مدارس اتریش اجرایی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/683641" target="_blank">📅 14:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683640">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a239b09a6a.mp4?token=vYi08PJYPbOcWNpTCQQHeJj1xUIQ8oa6HlWWx5z1jE9KQEukPDJ-JPApK37eblm5rzq9X8fQ6dOTR3rM72gaBdLBkQO1Ml-UP3_upG2HRXRcs0WoEKpZBz7y6CLg1rP1JAjbJWwf7orknxVuHijGnFSZH8QzPKakXJ7m2aeAQR-zM0p8K1wXYayX9zbwAdIZ3fScVdqv6XY8sqSYZeLl368GVa9kEJOi9QkV5RPnOrNCbYj7_my5QM7NOIJI9Nyo1dTeJMSRksTsaoXcxviyldgpk3vmkZyyS9vMkIx91rsGx89iz3p5wEN-J-2ZKeqLys1WgCCT-ip-DukfvsJbdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a239b09a6a.mp4?token=vYi08PJYPbOcWNpTCQQHeJj1xUIQ8oa6HlWWx5z1jE9KQEukPDJ-JPApK37eblm5rzq9X8fQ6dOTR3rM72gaBdLBkQO1Ml-UP3_upG2HRXRcs0WoEKpZBz7y6CLg1rP1JAjbJWwf7orknxVuHijGnFSZH8QzPKakXJ7m2aeAQR-zM0p8K1wXYayX9zbwAdIZ3fScVdqv6XY8sqSYZeLl368GVa9kEJOi9QkV5RPnOrNCbYj7_my5QM7NOIJI9Nyo1dTeJMSRksTsaoXcxviyldgpk3vmkZyyS9vMkIx91rsGx89iz3p5wEN-J-2ZKeqLys1WgCCT-ip-DukfvsJbdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کینِیو، نخست‌وزیر کانادا: «با آدم بد معامله خوب نمی‌شود»؛ ترامپ با جنگ ایران بنزین را گران کرد
اظهارات نخست‌وزیر کانادا، کینیو، درباره ترامپ:
🔹
افراد بسیار عاقلی گفته‌اند که "نمی‌توان با یک فرد بد، به توافقی خوب رسید"، و من فکر می‌کنم این اصل در اینجا نیز صدق می‌کند.
🔹
رئیس‌جمهور ترامپ دلیل این است که ما همگی در حال حاضر برای بنزین هزینه بسیار زیادی پرداخت می‌کنیم، به دلیل جنگ نادرست او در ایران.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/683640" target="_blank">📅 13:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683638">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c37dfca6.mp4?token=Z1d7Gc2Y2dLRp-XTzG-k290raBgL3qro2CiZse6r8JO0_5o9FeZLi3egpYxNu1R-LRK_p11PnHne4wRi3K-71pt_3LDn7_A6yagfMtXvTt6Ax4iwHoQ-PsN6EU4gtwz3BJaU9gJPj990o-lhQo_J3XoY1C2uifYynN4hvJNUTgZoLh6R7v11rq4jXgNR7ustrB9Mny1V14xO5XNcnbYj0gfZ1aKZoX8uOxgnVc2xWsbAQ5C9CUVv64rD8Odr41bCltUjExG0DyVzOmRDWEXgFGtSQTd3ITA3QHsmFrobtgCoRtYmYUdavH_J5faTBUSlB2pvmtdg_PBZzAuxJ2FngrHPD3TWTdjdgALyz7QPJoTELBF-Qr_hFVBxIyMYhlVkdtKsbkPDF-4Y9SfpaCJCoPGaRv3yRANC8AWe3ArbePPWFgPsxun8Dq-oV9rqN3Lv6w9J7bNb6TKXgYIqFYX31Tj3kOtn5I1-Ve0BfgWYvdRHwsuSL0WbiOWEVSj4-v6RjziHjGbd6ljNgpbI-XDTqdFIVo7mpf5yiM6-fKaWtZ-TpCnB3Mx9Z-isQmqyEi6JOfBCY8xFpZPdiYJF-c3kJ1JYm8ARW-XmaErs-8TEHOmEDkuVQgOgwbhOQ7v5ZoW-UFKGZfcPMbNtxqjiUoTm51EV1yb94oxgiHkdqpeAf0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c37dfca6.mp4?token=Z1d7Gc2Y2dLRp-XTzG-k290raBgL3qro2CiZse6r8JO0_5o9FeZLi3egpYxNu1R-LRK_p11PnHne4wRi3K-71pt_3LDn7_A6yagfMtXvTt6Ax4iwHoQ-PsN6EU4gtwz3BJaU9gJPj990o-lhQo_J3XoY1C2uifYynN4hvJNUTgZoLh6R7v11rq4jXgNR7ustrB9Mny1V14xO5XNcnbYj0gfZ1aKZoX8uOxgnVc2xWsbAQ5C9CUVv64rD8Odr41bCltUjExG0DyVzOmRDWEXgFGtSQTd3ITA3QHsmFrobtgCoRtYmYUdavH_J5faTBUSlB2pvmtdg_PBZzAuxJ2FngrHPD3TWTdjdgALyz7QPJoTELBF-Qr_hFVBxIyMYhlVkdtKsbkPDF-4Y9SfpaCJCoPGaRv3yRANC8AWe3ArbePPWFgPsxun8Dq-oV9rqN3Lv6w9J7bNb6TKXgYIqFYX31Tj3kOtn5I1-Ve0BfgWYvdRHwsuSL0WbiOWEVSj4-v6RjziHjGbd6ljNgpbI-XDTqdFIVo7mpf5yiM6-fKaWtZ-TpCnB3Mx9Z-isQmqyEi6JOfBCY8xFpZPdiYJF-c3kJ1JYm8ARW-XmaErs-8TEHOmEDkuVQgOgwbhOQ7v5ZoW-UFKGZfcPMbNtxqjiUoTm51EV1yb94oxgiHkdqpeAf0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین رقابت برای هوش مصنوعی خودمختار را وارد مرحله تازه‌ای کرد
🔹
چین روز گذشته چراغ «سینگولاریتی» را روشن کرد؛ اقدامی که به معنای تغییر یک‌شبه نیست، بلکه نشان‌دهنده ورود رقابت برای ساخت سیستم‌های هوش مصنوعی خودمختار و جایگزین نیروی انسانی به مرحله‌ای جدی‌تر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/683638" target="_blank">📅 13:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683637">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/369b433627.mp4?token=Je8qAYsnH847YJuPLX1EgGyomjmefNtPFkBAG4cXB1tb0yeZNJXeOGNTdHrdj3F_ANW2KsWJrH2K4jfnbQAytAo1wNIaq1YD48MDe1J4h7YX-niVAqhct_llRRcEhlRLiI-PEZUTsjjMdXMaxVwiZZPyMg5y-tW1ojlw0BhmSwZjU6ibQau37Am1ziVQup51zy5kUYeZbxNHGyQtPvtgNZOMamXWhklFsG4JUXKD8DVRgriw8-hLIGRAmj1hgj8tiLo-xAR0TRvCnXYqzudpcK5aOrYYboCrTvBCAH1EkjIvqRn8_H65Ydhd0VJCpADnQ_vbZHT-ZADYpxcFkFl9ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/369b433627.mp4?token=Je8qAYsnH847YJuPLX1EgGyomjmefNtPFkBAG4cXB1tb0yeZNJXeOGNTdHrdj3F_ANW2KsWJrH2K4jfnbQAytAo1wNIaq1YD48MDe1J4h7YX-niVAqhct_llRRcEhlRLiI-PEZUTsjjMdXMaxVwiZZPyMg5y-tW1ojlw0BhmSwZjU6ibQau37Am1ziVQup51zy5kUYeZbxNHGyQtPvtgNZOMamXWhklFsG4JUXKD8DVRgriw8-hLIGRAmj1hgj8tiLo-xAR0TRvCnXYqzudpcK5aOrYYboCrTvBCAH1EkjIvqRn8_H65Ydhd0VJCpADnQ_vbZHT-ZADYpxcFkFl9ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی: ۹۰ روز آینده برای ایران بسیار مهم است
منوچهر متکی، وزیر اسبق خارجه:
🔹
ترامپ می‌خواهد ایران را درگیر تفاهم اسلام‌آباد نگه دارد تا پس از انتخابات به سراغ ایران بیاید.
🔹
او افزود آمریکا در سه ماه آینده چهار راهبرد «جنگ محدود، آتش‌بس، محاصره و مذاکره» را دنبال می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/683637" target="_blank">📅 13:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683636">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbc6b4c1b.mp4?token=qvK78xx4GUE1dPvzfaiLri85s4CP5SaqdhSrAxeFSK8jTHg1JTxPLpUr3yWaiP31PDzdlr_reUJ7z5tz8bAhEv0KAn8Fx_C3oH3nLP1_WA3rPw5NpC8YXIA18nbFNBHrH_yEK2SN-ep5sHm23dzZTyLcdo8XEKVq_6YddQCx4QkQAkLG6cmEhxwCz4-DrqP9Mo91CTrc90_7qanXivK2n5kQAQ_wrM2SQOlmzUF1EMaSaDdtBZN3ZZ4g3tB51F__DLM-oe3dZwUnMZVqtaKfDu_E7ZuvPmh8OcGc8kR49y-jZiCBfGXg6rPagGKD2T_K9x40kM7JaXpnhrjjOBV-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbc6b4c1b.mp4?token=qvK78xx4GUE1dPvzfaiLri85s4CP5SaqdhSrAxeFSK8jTHg1JTxPLpUr3yWaiP31PDzdlr_reUJ7z5tz8bAhEv0KAn8Fx_C3oH3nLP1_WA3rPw5NpC8YXIA18nbFNBHrH_yEK2SN-ep5sHm23dzZTyLcdo8XEKVq_6YddQCx4QkQAkLG6cmEhxwCz4-DrqP9Mo91CTrc90_7qanXivK2n5kQAQ_wrM2SQOlmzUF1EMaSaDdtBZN3ZZ4g3tB51F__DLM-oe3dZwUnMZVqtaKfDu_E7ZuvPmh8OcGc8kR49y-jZiCBfGXg6rPagGKD2T_K9x40kM7JaXpnhrjjOBV-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار غیرحرفه‌ای و فرار رئیس سازمان غذا و دارو در نشست خبری
🔹
رئیس سازمان غذا و دارو پس از پایان سخنانش در یک نشست خبری، بدون حضور در نشست پرسش‌وپاسخ و از مسیری دیگر سالن را ترک کرد؛ درست زمانی که خبرنگاران می‌خواستند درباره مهمترین بحران‌های دارویی کشور مطالبات مردم را پیگیری کنند.
🔹
مسئولان حاضر در جلسه نیز از پرسش به پاسخ خبرنگار خبرفوری درباره ضعف نظارت ها خودداری کردند و مدیر روابط عمومی این سازمان گفت: «بعداً جواب می‌دهم.»
🔹
خبرفوری همچنان پیگیر و منتظر پاسخ این پرسش از سوی مسئولان ذی ربط است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/683636" target="_blank">📅 13:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683635">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۸ هزار واحدی به ۶ میلیون و ۷۰ هزار واحد رسید.
🔹
سازمان هواپیمایی کشوری: عمان و فلای‌دبی برای ایجاد مسیر هوایی جدید در جنوب ایران درخواست داده‌اند.
🔹
كلید اولیه آزمون های سراسری و پذیرش دانشجو معلم سال ۱۴۰۵ در سایت سازمان سنجش منتشر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/683635" target="_blank">📅 13:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683634">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d313a5cb6b.mp4?token=irUaNe1hp_AV1m7TI5DcjVG0B4X5i0CG_0NMDFaROt2sOoW0WJvdM5fTpgr7As3PO96bpYG6OYTJFx2BOejpwC7FewLckT45UrI-JKL5lwlH3wsxjJ1v2c_q3DiiptjQ9A1EbXxSVtQqNrDaRS4K7PDTy0e2qqPr43Hbx_SUAy-0e1F4A6653dPt7cwNgtZfWRJUba2EdZ8iaAeIdq-nHU3blyaZq2Mjct0ouVvFNjhlxCbgJzSu9MHC_a_rmAIxx7pQllhb50W5OvAVvOgJAC_-nRrGPueYDWV9wlskXn_HMZk0Iuv0J_kiJpRKgVd0_z3JLuak5jd-88QwOI_Omw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d313a5cb6b.mp4?token=irUaNe1hp_AV1m7TI5DcjVG0B4X5i0CG_0NMDFaROt2sOoW0WJvdM5fTpgr7As3PO96bpYG6OYTJFx2BOejpwC7FewLckT45UrI-JKL5lwlH3wsxjJ1v2c_q3DiiptjQ9A1EbXxSVtQqNrDaRS4K7PDTy0e2qqPr43Hbx_SUAy-0e1F4A6653dPt7cwNgtZfWRJUba2EdZ8iaAeIdq-nHU3blyaZq2Mjct0ouVvFNjhlxCbgJzSu9MHC_a_rmAIxx7pQllhb50W5OvAVvOgJAC_-nRrGPueYDWV9wlskXn_HMZk0Iuv0J_kiJpRKgVd0_z3JLuak5jd-88QwOI_Omw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موهایش را کوتاه کرد؛ ظاهر جدید هالند با سر تراشیده شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/683634" target="_blank">📅 13:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683633">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJMfFH3bZ27z_StVaIJQzu0b5ZfA6e-yDMAZ1E4FRpDPKT8uthGbKJHfhCVxc4t2yrWiDfUGMYgMAmggxnGkC_My5ZTqa10JQAQ6dZFzjZFPkyKONVhd9OQueVySzj_CyyIAT5S39Rq7DSQzE0JxotZziYwokG-IxeYQdSGofiA14ZVlGXUh35Zje3fAfCX4sMpN_0kHcItCfB7MkhMz2TAy6KSOErSxL-aBg5A9phPeUrJMrfojhRPCHCvaxrxcQy8sF9I1UFvuYSaoIvD26nkH1eceowjsOh3faVbCArdpPjutm7NSBeuokfIW52ZG4M0se95hOQwvAxNQLgJ8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
150 هزار تومان هدیه افتتاح حساب
اگر هنوز در ویپاد افتتاح حساب نکرده‌اید، با درج کد هدیه WP150k، پس‌از تکمیل افتتاح حساب 150 هزار تومان هدیه نقدی دریافت می‌کنید.
📋
دریافت هدیه افتتاح حساب:
1️⃣
اپلیکیشن ویپاد را نصب کرده و با وارد کردن کد هدیه WP150K، فرایند افتتاح حساب خود را تکمیل کنید.
* بلافاصله پس‌از افتتاح حساب، 150 هزار تومان هدیه نقدی دریافت می‌کنید.
🔗
همین حالا ویپاد را نصب کنید.
https://jryn.me/JvrbAQ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/683633" target="_blank">📅 13:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683632">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
حذف حبس برای مهریه‌های بالای ۱۴ سکه
نماینده نجف‌آباد در مجلس:
🔹
طرح اصلاح نحوۀ اجرای محکومیت‌های مالی در صحن علنی بررسی شد. با تصویب این طرح، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف شد.
🔹
در خصوص مهریه‌های زیر ۱۴ سکه، امکان اجرای احکام از طریق «پابند الکترونیک» فراهم شده است.
🔹
مصوبه برای طی مراحل قانونی و تأیید نهایی به شورای نگهبان ارسال شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/683632" target="_blank">📅 13:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683631">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e0cae6cc.mp4?token=vyhy5RL19_nkUHm0XgmiABs-5Ap4LNPcaukBYJ7VMrvH5e_Jqb-AjJ2d0b_VG_dZp2LYnfOKHm-PgVbHIraa9zk8nmH2KW0Q0zwtIRJKzosKXhjFzqRje9HN5NGkLdfAErbzN8cWcBm9hmZL6nQ3ydS4uRNp45csG83nzmhoQbqiLiKlX1ZhJMT0Qracqh7DW61f0CrOqjyKWEaqrg4UCH0YOazjhzHxbKGXnz2W_1GxhMIA6LUv6q8g7vlsLXdnav7Siikmy5pMzLHQUxCfDNcqLMuh7ZP1rj6IAzLbw2xG7O70kfQ35phSLeSKxA553GSPVnMxO8KMQ6qlWT-WnU4TlfkNf12RpC4XNJvSmSQAXuSFKWoH0ol0zY08bRbA7BDC64y2Ww1BNQiWpd1F6wseBovPYEzNKK14d7YrEzyGr_eUqj_aETNbVZcNQYKTNqN4GxQFcCs4OcFxJXhAbGlzL20qiWcIH3XJellFIH9FWRCzWLfdcDpC7x3_xskVQvgjL-ZERKbXreMgRfN8COsuPxCuhVm8YiJJxJv70R7Q_mcaTtl6mVAEVcawrrEoMITyNxBjeNuE0MHe6uEcH_H0PEJpkVVW-f0kSc012-xKFby9b0bAq8UFnZgBugHOZg9J53hielMXw_WIoqXbNF9evnM2FNYrXsazftQZ4Rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e0cae6cc.mp4?token=vyhy5RL19_nkUHm0XgmiABs-5Ap4LNPcaukBYJ7VMrvH5e_Jqb-AjJ2d0b_VG_dZp2LYnfOKHm-PgVbHIraa9zk8nmH2KW0Q0zwtIRJKzosKXhjFzqRje9HN5NGkLdfAErbzN8cWcBm9hmZL6nQ3ydS4uRNp45csG83nzmhoQbqiLiKlX1ZhJMT0Qracqh7DW61f0CrOqjyKWEaqrg4UCH0YOazjhzHxbKGXnz2W_1GxhMIA6LUv6q8g7vlsLXdnav7Siikmy5pMzLHQUxCfDNcqLMuh7ZP1rj6IAzLbw2xG7O70kfQ35phSLeSKxA553GSPVnMxO8KMQ6qlWT-WnU4TlfkNf12RpC4XNJvSmSQAXuSFKWoH0ol0zY08bRbA7BDC64y2Ww1BNQiWpd1F6wseBovPYEzNKK14d7YrEzyGr_eUqj_aETNbVZcNQYKTNqN4GxQFcCs4OcFxJXhAbGlzL20qiWcIH3XJellFIH9FWRCzWLfdcDpC7x3_xskVQvgjL-ZERKbXreMgRfN8COsuPxCuhVm8YiJJxJv70R7Q_mcaTtl6mVAEVcawrrEoMITyNxBjeNuE0MHe6uEcH_H0PEJpkVVW-f0kSc012-xKFby9b0bAq8UFnZgBugHOZg9J53hielMXw_WIoqXbNF9evnM2FNYrXsazftQZ4Rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید حسن خمینی: بعضی‌ها در لباس دوست یا دشمن نمی‌خواهند نام امام برای آیندگان بماند
🔹
مراد شهید ما خوب به ما یاد داد امام روح و جان انقلاب و جمهوری اسلامی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/683631" target="_blank">📅 13:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683630">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92478c154.mp4?token=pgQWuZT_LPmgLyLh0bgsrSSKviaJxDqsDdh07L4T7w8ouOjuxq77VUhubXC1xtwLTs7QVUj_Pf2-VtTDnd4BezJbRfY-7a1amHukrPyZbB6oYuHVw9Yjo6Lq0Y5cLIrIFGAAJkt5j3xDW56kJ0yOqOczH0eeeu46C4cVtdX457V3Qius9pxmxIWodwaQiMoRLAuG-C39jShMMWQs6EcvUduZWf2DYg5SHgJmfqrnSBzc_S79YiR5wJK75S-PjuNhtNiIU5pdNLXCBTkz2GoitkvipPNPJxoq6yOvxrCWpr0ESLq58ivJPUcwb5YTHGniSYI10BHXoeOwxVvvm6XdZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92478c154.mp4?token=pgQWuZT_LPmgLyLh0bgsrSSKviaJxDqsDdh07L4T7w8ouOjuxq77VUhubXC1xtwLTs7QVUj_Pf2-VtTDnd4BezJbRfY-7a1amHukrPyZbB6oYuHVw9Yjo6Lq0Y5cLIrIFGAAJkt5j3xDW56kJ0yOqOczH0eeeu46C4cVtdX457V3Qius9pxmxIWodwaQiMoRLAuG-C39jShMMWQs6EcvUduZWf2DYg5SHgJmfqrnSBzc_S79YiR5wJK75S-PjuNhtNiIU5pdNLXCBTkz2GoitkvipPNPJxoq6yOvxrCWpr0ESLq58ivJPUcwb5YTHGniSYI10BHXoeOwxVvvm6XdZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی صداها فقط شنیده نمی‌شوند؛ از میان خاطره‌ها عبور می‌کنند و به عمیق‌ترین جای دل می‌رسند…
🇮🇷
🖤
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/683630" target="_blank">📅 13:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683629">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
کره جنوبی مسیر قطب شمال را آزمایش می‌کند
🔹
نخستین کشتی کانتینری کره جنوبی از مسیر دریایی شمالی به سمت اروپا حرکت کرد تا امکان استفاده تجاری از این مسیر به‌عنوان جایگزینی برای مسیرهای سنتی خاورمیانه را بررسی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/683629" target="_blank">📅 13:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683628">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/solpiAhijaDM9FOKV7O82AOcqaXzmSLGtWBP8Fn6xF0NQke5o6Of0JvBK2_qan0G69FKimeH_pO-lnu0BZFFmmLy747XY5B4McFm8COlxBNfqw0esSQQLA7WikdYFvC7lg3UNO4P_wgtcEFsouhxIhfK3ba8kjaakuOIH_ZJ4cRjFDr2GnlZ4wzsFjeFnlBlz06uSQS_3qdsXC0bQQbSlah8wNDSLBEKseOHPnKNM2JbhR_fYcePP5YlFKN4GFvmWaBPK0Z1geRQsxSU1hpW1hqQonfFcfByS7uHscbIDu-bAAPAVZDd5V3Dmb1IBy6ZhTCGiJlL8Wq-R8hhrJFUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین تصویر از مرجع عالیقدر آیت‌الله العظمی سید علی حسینی سیستانی به مناسبت ۹۹ سالگی عمر مبارک ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/683628" target="_blank">📅 12:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683627">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d7a17fbd0.mp4?token=iY-Pv1Kmegc-J8vhMFxUWGfKCrRvyuxtQ0LlHa_WyF8QG0YJKHREN8Iu3IgjpXR-G47iPWYektzEloJCKHiaXY3bfLSOmSCZpV2yBWiHCcM1SCw28eIOt_W7PXHAzdOBlGgC8ttdu-D9-D3OGL2bLDXgbveQFrW7m0KpxVcFtVncyjNKlbCQUyry3aytC9kliOdm3l05Z1zHar_OhvHtDVpCpowCF5zy79RJipWkaPR7DgnIwU2udgnLJgjLVOSk2yHfd3_KgOX24evmx7y-mUz1IlfRseTBD6w83I5Uq5dyWpG-KDxiccrsq1oDd7JEepSqKMK6XTZY2Hag6jtRuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d7a17fbd0.mp4?token=iY-Pv1Kmegc-J8vhMFxUWGfKCrRvyuxtQ0LlHa_WyF8QG0YJKHREN8Iu3IgjpXR-G47iPWYektzEloJCKHiaXY3bfLSOmSCZpV2yBWiHCcM1SCw28eIOt_W7PXHAzdOBlGgC8ttdu-D9-D3OGL2bLDXgbveQFrW7m0KpxVcFtVncyjNKlbCQUyry3aytC9kliOdm3l05Z1zHar_OhvHtDVpCpowCF5zy79RJipWkaPR7DgnIwU2udgnLJgjLVOSk2yHfd3_KgOX24evmx7y-mUz1IlfRseTBD6w83I5Uq5dyWpG-KDxiccrsq1oDd7JEepSqKMK6XTZY2Hag6jtRuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در جاده‌هایی که از دل پارک‌ ملی‌ها می‌گذرد، با احتیاط رانندگی کنید
🥲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/683627" target="_blank">📅 12:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683625">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda69ac8b3.mp4?token=bvEPKwNHynwi3XIBOnJvRZxOKkD10xaFsrv2twnkg7EmbXHFJn6l2EEJN5esZzMgS_jcgt5TKr1v96GhBiYmlJNUoqYKXeL7SDlOCsyq9LOK-0YztlNbZvFHmWIvaY5S3xeFQus2K1lNKgP8O3V4SfIraSRqPTBe1xpTgj42UUtEidvLL3U8OeIRL1b4Yjq11FR9rmMDrwPq4BsdagHALWgBPbR3JwhGr-GSJTlE1zjgAq1ZjmFjaPd4vKU_voUTfTHSAnnhp_29VrobvtjKxKFuEAYLRNZws-a4Oq9vduEyp9eonbjIx3z4kqIb6HvfwrjGaOeqLjJs8LRQbohWqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda69ac8b3.mp4?token=bvEPKwNHynwi3XIBOnJvRZxOKkD10xaFsrv2twnkg7EmbXHFJn6l2EEJN5esZzMgS_jcgt5TKr1v96GhBiYmlJNUoqYKXeL7SDlOCsyq9LOK-0YztlNbZvFHmWIvaY5S3xeFQus2K1lNKgP8O3V4SfIraSRqPTBe1xpTgj42UUtEidvLL3U8OeIRL1b4Yjq11FR9rmMDrwPq4BsdagHALWgBPbR3JwhGr-GSJTlE1zjgAq1ZjmFjaPd4vKU_voUTfTHSAnnhp_29VrobvtjKxKFuEAYLRNZws-a4Oq9vduEyp9eonbjIx3z4kqIb6HvfwrjGaOeqLjJs8LRQbohWqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرانسه: دو دیپلمات ایران طی روزهای آینده اخراج می‌شوند
🔹
وزیر امور خارجه فرانسه در پیامی در شبکه ایکس ضمن حمایت از اغتشاشات دی‌ماه نوشت که قصد اخراج دو دیپلمات ایرانی را دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/683625" target="_blank">📅 12:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683623">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
مصرف خانگی گوشت بوفالو مجاز است
مدیرکل دامپزشکی استان تهران:
🔹
گوشت بوفالو از هند وارد می‌شود و کشتار آن در مبدأ تحت نظارت‌های شرعی و بهداشتی انجام می‌گیرد. این گوشت تا سال گذشته عمدتاً برای مصارف صنعتی مانند تولید سوسیس و کالباس استفاده می‌شد.
🔹
سازمان دامپزشکی اکنون مصرف خانگی گوشت بوفالو را مجاز اعلام کرده است؛ با این حال، واحدهای عرضه‌کننده حق ندارند آن را با عنوان گوشت گاو به مردم بفروشند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/683623" target="_blank">📅 12:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683622">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
صادرات نفت عربستان از رونق افتاد
🔹
براساس رصدها، تنها یک نفت‌کش فوق‌بزرگ در بندر ینبع در حال بارگیری نفت است و چندین کشتی کوچک‌تر نیز در اسکله‌های آرامکو مستقر هستند؛ کاهشی که پس از حملات اخیر به تأسیسات نفتی و نفتکش‌های عربستان رخ داده است.
🔹
بلومبرگ گزارش داده صادرات نفت خام و فرآورده‌های نفتی از دریای سرخ با کاهش ۲ میلیون بشکه‌ای به ۴ میلیون بشکه در روز رسیده و احتمال دارد عربستان بخشی از نفت را به مصرف داخلی و پالایشگاه‌ها اختصاص داده باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683622" target="_blank">📅 12:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683621">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZZ2XxylsVQyPRIhxGdCWdbrYo3aBBYBOHmp8ps6NBmYomZdjKSnmm4p7XWn6NDrbEvxWKBgAm3QUqF-sxBD3UIAImIytjRxcMQ2GmJFOnmmtQba4Vaaiyt6uJoXe8zKFitKL5dZ9qgZGn1jiJdRPEIbwgP_IyHdKRtQRNPd2n_Whe3c0Y08X3x1jfMscnT0npjA-lyi_uEyvWWCDvpxp9N9hAmhgSMAbbk99YrzqQX6K_SXT7MHMnV3hzD6CHRQZzdcn0sBQzu-JGdHrppxDHaza-19GcbK7jd6j2cOHI2BErvsUulbU-Qr7zrQ6Q5z1rhzq0hSLwubTZ1nYTxOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این بیلبوردهای مرموز با تصویر دماوند توی شهر دیده شدن
👀
نه اسم برندی روشونه، نه محصولی معرفی شده.
🔹
فقط یک جمله: «از آنچه دوست داریم، مراقبت می‌کنیم»
🔹
به نظرتون قراره آخر این ماجرا به چی برسیم؟
🤔</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/683621" target="_blank">📅 12:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683620">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTtnwjjFVlPGb56cItXB447h9rN1zFKaeMCvZbEz0UBRr5-EjLxJgifan2SKGG3ibb4WusoHQTxAyEdNi1fL-CUa3xyRHZa56qX2eVeU7efJDIJ2xM4gkHiyTDBTOGhhFOnf3c4XwJzSWHVWTs7vcTiARPnSfNpSa6kMAJZE5Flx2aeog1Wws-B7ZPoMmlnYEaiKXjEZSLJEyNVSoD63-53vHo6Sy4RFA0snM_3djVH8eAFT2G_95JJmJ4bCr1NnGsrzPPkOdg7PXINHlqI_rcj2mvvON1u8epFs30ixYIYqcFH7WJmtOqAoj29gVuPdLkOU6atjKCxLjVBc3g6RCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موبایل؛ ۴ برابر گران‌تر از یک سال قبل شد
🔹
قیمت برخی گوشی‌های پرمخاطب در بازار ایران طی یک سال گذشته تا ۴ برابر افزایش یافته و فشار بیشتری به قدرت خرید مصرف‌کنندگان وارد کرده است.
🔹
افزایش هزینه واردات، نوسانات نرخ ارز و محدودیت عرضه از مهم‌ترین عوامل رشد قیمت موبایل در این دوره عنوان شده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683620" target="_blank">📅 12:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683619">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
درگیری لفظی در والیبال منجر به قتل جوان ۱۸ ساله اصفهانی شد
رئیس پلیس آگاهی استان اصفهان:
🔹
جوان ۱۸ ساله‌ای در جریان بازی والیبال بر سر مسائل بازی با فردی دیگر درگیر شد و مشاجره لفظی آنها به درگیری فیزیکی انجامید؛ متهم در لحظه‌ای از شدت خشم، صدماتی به او وارد کرد که منجر به فوتش در محل شد.
🔹
متهم پس از حادثه متواری شد، اما مأموران پلیس آگاهی با شناسایی مسیر فرار، او را در شهرستان بویین و میاندشت و پیش از خروج از استان دستگیر و برای طی مراحل قانونی تحویل مرجع قضایی کردند.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/683619" target="_blank">📅 12:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqPbHCH39IHmONHIMKZ6nKzqFXJPL4PQ7-Qh4K32djenyPUqKU9Y2pktVCd3hjqj1otl5d_lBabOPT6_C-Ntm9zpTkYca5xsIEsA8M9XZOIFujqzZVoDHNwug0poe-qdnj1_D-9jZJoGAaBwaEeZpJLyTBKfcZSFZY_Jbs6QB3hfs624SVt7LxbqYd3yGqHkW8WKyjOHdh6p5sYPX9HBzKVhSIFkNuEX3pJOS9M2BcSsVXTPHglRpkDEmhMA5irxIhz1IJiq7psAs5htVXDVEsc9KYDKdOXMYhnCLxFKt69-3qtO0xzSUjtM7aviSFTuh45LgrLFVoW6mGkbbDmkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از چند تکه پارچه تا یک کسب‌وکار خانگی
🔹
این بار در #چرخ_زندگی رفتیم سراغ یک ایده ساده، کاربردی و کم‌هزینه؛ ساخت و دوخت هدبند و تل‌های پارچه‌ای دست‌ساز.
🔹
با کمی پارچه کشی، نخ و یک چرخ خیاطی می‌شود هدبندهایی زیبا و رنگارنگ ساخت و با فروش آن‌ها، قدم اول یک…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683618" target="_blank">📅 12:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683617">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
همسر، همکار یا یکی از نزدیکانت همیشه بهت شک می‌کنه؟ شاید این ویدیو دلیلش رو برات روشن کنه… #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/683617" target="_blank">📅 12:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683616">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره تخصصی اتاق تهران برای موفقیت در تجارت بین‌الملل
🔺
معاونت امور بین‌الملل و توسعه تجارت اتاق تهران با ارائه مشاوره تخصصی مالی و بانکی بین‌الملل، به فعالان اقتصادی در کاهش ریسک‌های ارزی و اعتباری و تسهیل تجارت خارجی کمک می‌کند.
👈🏻
88725269| واتساپ: 09102669714 |
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/683616" target="_blank">📅 12:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس مرکز امور زنان و خانواده وزارت کشور: کاندیداهای زن را فقط به خاطر یک عکس بی‌حجاب رد صلاحیت می‌کنند ولی یک آقا ممکن است هزار کار کرده باشد و بگویند دیده نشده است
پروین داد اندیش، مشاور وزیر و رییس مرکز امور زنان و خانواده وزارت کشور در
#گفتگو
با خبرفوری:
🔹
۶۱ درصد زنان ما تحصیل کرده هستند و ۷ تا ۸ درصد آنها در شوراهای شهر و روستاها حضور دارند.
🔹
۱۰۰ بخشدار و ۲۵ فرماندار زن داریم. خیلی از آنها وقتی در جایگاه قرار می‌گیرند از مردان (نسبت به مسائل زنان ) سختگیرتر می‌شوند درحالیکه خانم‌ها این پست را به آنها داده‌اند.
🔹
یکی از پیشنهادات ما این بود در هیئت نظارت، خانم ها نیز باید حضور داشته باشند چون یک عکس بدحجاب پیدا می‌کنند و راحت خانم رد صلاحیت می‌شود.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/683615" target="_blank">📅 12:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683614">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
انشعاب غیرمجاز برای سرقت میلیون‌ها لیتر سوخت در سه استان
🔹
رئیس پلیس امنیت اقتصادی فراجا از شناسایی سه پرونده سرقت سوخت از خطوط انتقال در اصفهان، کرمان و تهران خبر داد.
🔹
متهمان این پرونده‌ها تاکنون به سرقت و قاچاق حدود ۳ میلیون و ۹۶۰ هزار لیتر سوخت از طریق انشعاب‌های غیرمجاز از خط لوله اعتراف کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/683614" target="_blank">📅 11:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683613">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjS5oCzhp_egpUpKMUPmWprETbR11FHJ1Nnhi2JvJ5UDEB0nukE0apLK2bBwEkEZE3PEj5OCvW1crmllaIzrFgvDiqedClL6wojx2248pgGYKs6_ZYX5tSkXPOCmZEaGzwhtNsBc88vOzrwCTo6AvMeoG_cl35y8lbugg5YNcbac-5353IYRbwzLGDMVHVROs-aQ-HYyx9MKjl7k_N0BQM-bh3O4Pl9P1jMCXLIknPiig2u-nMZ3OIHulAA36F_phu7mRO3WtGLZKo1tUAxuSPDHD_PDocov6I8QZRGB6J1H3Yel3m2nlpN_d0ZkB-bBddw-lFWl9CqjY2E9ChMN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: فلسطین آرمانی زنده و تغییرناپذیر است
فرمانده نیروی قدس سپاه پاسداران:
🔹
آرمان فلسطین، از بحر تا نهر، بیش از هر زمان دیگری زنده و دست‌یافتنی است.
🔹
توسعه شهرک‌سازی و جنایات صهیونیست‌ها، تلاشی برای فرار از بحران و بن‌بست عمیق نظامی، امنیتی، سیاسی و اجتماعی در سرزمین‌های اشغالی است و نمی‌تواند شکست‌های راهبردی آنان از ۷ اکتبر تاکنون را پنهان کند.
🔹
فلسطین آرمانی زنده و تغییرناپذیر است؛ آرمانی که به یاری خدا تا تحقق پیروزی حق، پابرجا خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/683613" target="_blank">📅 11:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683610">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
باج‌گیری از مدیران پتروشیمی و فولادی؛ حساب ۱۶ عضو باند مسدود شد
رئیس پلیس امنیت اقتصادی:
🔹
حساب بانکی ۱۶ عضو یک شبکه باج‌گیر مسدود و نزدیک به هزار میلیارد تومان از اموالشان توقیف شد.
🔹
۱۹ نفر ممنوع‌الخروج و ممنوع‌المعامله و ۳ مجوز رسانه‌ای مرتبط با این افراد نیز تعلیق شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/683610" target="_blank">📅 11:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683609">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dd21d1a4a.mp4?token=AHQDnvuTm1lqBNcZAFstdazAtwh_XCooceo7z-FUWktefjScA7FB6xnq9HpP6SfqcKE5LP8ZaUR2SeDEX4Lm6fogVJ-k3SpWCVOW_-vLnAk-ixFmy3DLLx6yOo6FvvTnDZi01z3wV4ayQ_vLSyAYFC7I3iJmtgDDuiUL-n7hnnvIC2_skakAkVyrgT-ope_LKIXN_Uil0uIL-h_Lw3VxffVXlrKSiybN-0355O28U9ewqd7LZpiDs4Eoc6xDVNldBRsgdpn6LSKv6rkRsoSh7ABLrpYvdqYQYDABoy_Co5z8_HROaiSTzJb7H29wZxmzIi6p_4NurL2XFvNns8IbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dd21d1a4a.mp4?token=AHQDnvuTm1lqBNcZAFstdazAtwh_XCooceo7z-FUWktefjScA7FB6xnq9HpP6SfqcKE5LP8ZaUR2SeDEX4Lm6fogVJ-k3SpWCVOW_-vLnAk-ixFmy3DLLx6yOo6FvvTnDZi01z3wV4ayQ_vLSyAYFC7I3iJmtgDDuiUL-n7hnnvIC2_skakAkVyrgT-ope_LKIXN_Uil0uIL-h_Lw3VxffVXlrKSiybN-0355O28U9ewqd7LZpiDs4Eoc6xDVNldBRsgdpn6LSKv6rkRsoSh7ABLrpYvdqYQYDABoy_Co5z8_HROaiSTzJb7H29wZxmzIi6p_4NurL2XFvNns8IbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
روایت مخاطبان خبرفوری از کسب‌وکارهای خانگی؛ تلاش‌هایی ساده اما اثرگذار برای ساختن آینده‌ای بهتر.
🔸
یک پیام صوتی حداکثر ۳۰ ثانیه‌ای شامل نام، شهر، نحوه شروع و نتیجه کسب‌وکارتان، به‌همراه عکس کسب‌وکار برای ما ارسال کنید. روایت‌های برتر فرصت معرفی و تبلیغ در خبرفوری و کانال‌های زیرمجموعه را خواهند داشت
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/683609" target="_blank">📅 11:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683606">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
همتی‌فرد، دادستان مشهد دستور برخورد قاطع با مروجین فساد و برهنگی را صادر کرد.
🔹
رئیس سازمان غذا و دارو: ارز ترجیحی دارو به یکباره حذف نمی‌شود.
🔹
جهاد کشاورزی: هیچ گوشت مرغ تاریخ گذشته‌ای در تهران توزیع نشده است.
🔹
توقیف فعالیت ۲۹ سرشبکه ماهیگیری غیرمجاز در تنگستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/683606" target="_blank">📅 11:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683605">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHDTNfDx8rXQpw6ovCvN9s0AxjvS4hxFxIJ0JGbtzgVxw7SIjmZK2-sP36Eoqc5sichoshotkbTkahJyZ7ZZj4PCnkPpZtIZ3Sdg8bFTQQfzD-LVLxlgeBlQYUuFrnudvVPbTFTpQK8cHymF6cc9g_bmwwF8Mn6HJtuOSzkG7F5x_2-EDt4AOpRF1BmvkeGHrlDlse4mgjPcksHAJ8vzguW9PK28cU9SvNCA0aNlvCf3aJroqZM5pDVe72eKJlGw6p-7B-UTegxujBn_iYRhnCyHVZ7iA2_j6T9By-MPdCltDXJ29jEvf-5iooM88K2I0JndQqtjQzi3QPKpA_Rc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکذیب مشاهده دایناسور در خراسان رضوی
🔹
اداره کل محیط زیست خراسان رضوی در پی انتشار تصاویری در شبکه‌های اجتماعی مبنی بر مشاهده یک دایناسور در این استان، وجود این گونه را تکذیب کرد./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/683605" target="_blank">📅 11:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683602">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IcmknEYQIKAI-g3RCifX5y-qyuT3PmKQ9yDPALOkoIzc7qUhkIXKJ9BnbPLGfB29zR41mwXyQiulWheQsrOKiuqtI7wXf688OeTTk8vlEFaWvASY2Rq8Sp0xIb5dTGeDum8vEcDgFTVBJHzPuEBP4syETBmHkNuXGk1MWehm19BwnJuoFj2iEQyEZZBO5WZBpTNgaAt0l-41e1fKm2esS9U7sZo0SYRD3srsgYDis2qVyXOo9k6-DTACMY_Jnk_buz2xMx65Po3Zt5CUDTEFJzmJoZ_kV6mIaLPpuy2YVid95CUzLhWaBNDERBIuAFUf3IGqVnvu8LE7Q7bdiTQakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ni40k2zFwJOt0W2aHsXU9_u9cTtYVgdYKu1CkikmQ_ULAvIJybm1FGA706A7uMB_44x9lQN5cSEC4ijb59xN-v8h3Zazf6_cYvGZUwib5z7E6Lq-83uU1_xipGuS1Jdyv1wfrqATawFtpapZxjCpohzQVwiky22KxykCIkXdjbppwqFzl3JVA-bOKAzL3gjK4zBHpB7lIRwohxofcYbZEPSGjlnLiZBiUaeH9uX6-7cj5dfvMghzpqH9IvW2jNUGU36JWd-Y43Qr2hh_c7r78zwFb9aUN7pmLCuWOragyFfZD4zEEj2APQQLfJzwb5zW7Pk2cyFCFuJgKKHmJ1jXTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad448831b7.mp4?token=IcIebRx0NuNHeLeP6G-wicX3mNJVwKkwRzaqJ0iccp2InDuXLTpqP3KgOe8gp3I6rKCmySJpTgnMmLgR_rOk3I6yZskGcROYoRq4qFKlUjPVo9JB6AXXsMxj5dlddQFYULvi13BiDFdn2-GkxYJCsuqysB7_S0gnY-VAZFbgw05G4vNQHOxGGb45Ynob9vlT_obXs5qbRqA0RwwUSdqdRM9S73rFSukWXpkZN9XJijYrNyxPhfO7X1zGpiVCUABnXxDKC6n45_Ee3ukOjUFm39DXA0bL_mM9z8-eCaBIVFawGVg9PJNrOtdGlVMXKJnnfYvJzZ9uH8Q0hiJOGxXtcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad448831b7.mp4?token=IcIebRx0NuNHeLeP6G-wicX3mNJVwKkwRzaqJ0iccp2InDuXLTpqP3KgOe8gp3I6rKCmySJpTgnMmLgR_rOk3I6yZskGcROYoRq4qFKlUjPVo9JB6AXXsMxj5dlddQFYULvi13BiDFdn2-GkxYJCsuqysB7_S0gnY-VAZFbgw05G4vNQHOxGGb45Ynob9vlT_obXs5qbRqA0RwwUSdqdRM9S73rFSukWXpkZN9XJijYrNyxPhfO7X1zGpiVCUABnXxDKC6n45_Ee3ukOjUFm39DXA0bL_mM9z8-eCaBIVFawGVg9PJNrOtdGlVMXKJnnfYvJzZ9uH8Q0hiJOGxXtcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از خمیر ساده تا یک کسب‌وکار خانگی
🔹
با کمی خمیر، چند ابزار ساده و چاشنی خلاقیت می‌شود عروسک‌هایی زیبا و خاص ساخت و از دل یک هنر کوچک، قدم اول یک کسب‌وکار خانگی را برداشت. #چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/683602" target="_blank">📅 11:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683597">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c317f9e52.mp4?token=v7taiqHWRxp07ftPkxwyPuFhDO4J-_X-7COfUiCoaUULPHtdcPxZZDsofHQbDW4Hcj5fuXImV-jfGRU3QFuk2Pqmb_UQ6QieS0MxpixxFzPfNp8FZOHMeMcq19qtJDt36gAiIcXCn5m7x7KfMqTDORn__rhBYd8PqbyFY8dxhKXz4TnboEv-LQARO6k9uK8jh3f_LbQ_vrPQ4GaHAXTXKRF9HXvvRUfhArq4VKh-RNyblqQVcTTqUg35PFPOrso8dfmlMHbyFbhQJf1-xJ93NqKJxdejk7L0-_J0TFqY8n2iuAozLdKcfJS3W6fCdHiigFIdpLsgfjcpK_0Bay-jtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c317f9e52.mp4?token=v7taiqHWRxp07ftPkxwyPuFhDO4J-_X-7COfUiCoaUULPHtdcPxZZDsofHQbDW4Hcj5fuXImV-jfGRU3QFuk2Pqmb_UQ6QieS0MxpixxFzPfNp8FZOHMeMcq19qtJDt36gAiIcXCn5m7x7KfMqTDORn__rhBYd8PqbyFY8dxhKXz4TnboEv-LQARO6k9uK8jh3f_LbQ_vrPQ4GaHAXTXKRF9HXvvRUfhArq4VKh-RNyblqQVcTTqUg35PFPOrso8dfmlMHbyFbhQJf1-xJ93NqKJxdejk7L0-_J0TFqY8n2iuAozLdKcfJS3W6fCdHiigFIdpLsgfjcpK_0Bay-jtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قولنج می‌شکنیم، اما این صدا دقیقاً از کجاست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/683597" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683596">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2Emmi9QHOoQXeF44iXx1QgumpKuJnwNPOruT02UJ2BUqtT0zNuhnO-b3lkt3jf6Ms9r8Amx-IEhbDqUy7WOqgSeSEK1szh3ePvQ_Bqhmc7esILGvwNIl_0xVUSYs_A0n7OnAzSwKLxLMV44zkFiWTjcaKXbPZkoMJS6QI8xgUGCTv4fQWg_7TPpZI1qrgtaWu-ILT3h5H9LRd0yoaI-zHygmrGOYThYYvXCyEO52zk6vbOAvdIwT1gq2AJshNXhvgOhO_TvR7oZx0qNJeDyJ6KylRfvh_Tv4yAbQdyMWvbUYytqjNXhbBwY3m0nMpR9g7sbpV7fQyxL7fBD15K50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰ دوره آموزشی مکتب‌خونه رایگان شد.
🔹
مکتب‌خونه در ادامه طرح‌های حمایتی خود برای گسترش دسترسی کاربران به آموزش، در طرح «ایران‌ماهر» ۵۰۰ دوره آموزشی را تا ۸ شهریور رایگان کرده است.
🔹
این طرح فرصتی فراهم می‌کند تا افراد بدون دغدغه مالی، مهارت مورد نیازشان را برای ورود به بازار کار، پیشرفت شغلی یا توسعه فردی یاد بگیرند.
🔹
دوره‌ها موضوعاتی مثل برنامه‌نویسی، هوش مصنوعی، زبان، مدیریت، بازاریابی، مهارت‌های شغلی، مالی و حسابداری و فناوری اطلاعات را پوشش می‌دهند.
برای استفاده از این طرح، کافی است وارد کلیک زیر شوید،  آموزش دلخواه خود را انتخاب کنید و با کد تخفیف IRANMAHER آموزش مورد نظر را با تخفیف ١٠٠% دریافت کنید.
👇
https://mktb.me/k4h1/
https://mktb.me/k4h1/</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/683596" target="_blank">📅 11:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683595">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
عاصم منیر در راه تهران
اسماعیل بقائی سخنگوی وزارت امور خارجه:
🔹
فرمانده ارتش پاکستان برای تقویت همکاری‌های دوجانبه و رایزنی درباره امنیت منطقه دوشنبه به ایران می‌آید
.
🔹
منابع العربیه ادعا کردند: فرمانده ارتش پاکستان، پیام‌های آمریکایی را در جریان سفر خود به ایران خواهد برد.
🔹
این سفر تلاشی برای شکستن بن‌بست و از سرگیری مذاکرات خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/683595" target="_blank">📅 10:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683594">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce468430e.mp4?token=Wk6yApm-zve-zfKq174tqSZvQiYuZ5M8nb9OnM3ZmGT_TtcwDK31TKq-b0u-dpJVa0Pb66c11EVMlV0FbMqS-d8anXieFCTf5QIjq4r5IYShSxbLQlS6zi0JtzOS_cRk9QhOUMt1ptiDvmRMhlp5l7oP8E5Stn5hP9IUEqAtGwB4e5TaPaBBpismn2KgSkf9n8Wr1l1s8_QhQ9uer1TUyTBHgbzYnSRmd4NMjYhdd5Uw_hiW9db6TpoV0Sp2PJQQc6kOrssCRHIw378eHPLBcJXRiKzz7sDlCaCi1K-V76lBvuJYp9wfKSqdj8Sj5gxh8Zw6XfvRzhqa1PcFNz4YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce468430e.mp4?token=Wk6yApm-zve-zfKq174tqSZvQiYuZ5M8nb9OnM3ZmGT_TtcwDK31TKq-b0u-dpJVa0Pb66c11EVMlV0FbMqS-d8anXieFCTf5QIjq4r5IYShSxbLQlS6zi0JtzOS_cRk9QhOUMt1ptiDvmRMhlp5l7oP8E5Stn5hP9IUEqAtGwB4e5TaPaBBpismn2KgSkf9n8Wr1l1s8_QhQ9uer1TUyTBHgbzYnSRmd4NMjYhdd5Uw_hiW9db6TpoV0Sp2PJQQc6kOrssCRHIw378eHPLBcJXRiKzz7sDlCaCi1K-V76lBvuJYp9wfKSqdj8Sj5gxh8Zw6XfvRzhqa1PcFNz4YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسئولیت پذیری اساتید در قبال ایران؛ گمشده دانشگاه های کشور
دکتر جزایی، پژوهشگر دانشگاه سیمون فریزر کانادا:
🔹
«فرد دانشگاهی خودش را جدا از سیستم می‌بیند، اما در تصمیم‌های اساسی نقش دارد و از پذیرش مسئولیت آن‌ها فرار می‌کند؛ من به این وضعیت می‌گویم «دانشگاه بی‌فاعل»/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/683594" target="_blank">📅 10:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683593">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c3bd7363.mp4?token=JfNr7lGegVvfx5b9jWD16ToIkeDBSCSVKBpad-DHk8VJFRdNUXIdf0x3RPDp-Z4ShgRX46d3sUd_r8LQGa0rgZeRhIey7DdJo5z4BK5Je-E4Kf23a47AEl-7UOqjhL5ir5IBAeZcvsxa9LUVaUV593iMkzMmbRnL-T_KImc5KXeQPN7ZmSHj9Uu2LsLwefaDsoWVZntoE2XDS7Ittpw7F_yKTpL-FNPUQzo0TajZjQRCN7gz2DOGEVbPjbhvgE3MIzOjUozyJQte9AhUAM9tt_ZJP97_ww9opEKakNwYVisw_hl4auLeKG6PcsPLqnDOBpN2uPUodVCkgmHmbAShyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c3bd7363.mp4?token=JfNr7lGegVvfx5b9jWD16ToIkeDBSCSVKBpad-DHk8VJFRdNUXIdf0x3RPDp-Z4ShgRX46d3sUd_r8LQGa0rgZeRhIey7DdJo5z4BK5Je-E4Kf23a47AEl-7UOqjhL5ir5IBAeZcvsxa9LUVaUV593iMkzMmbRnL-T_KImc5KXeQPN7ZmSHj9Uu2LsLwefaDsoWVZntoE2XDS7Ittpw7F_yKTpL-FNPUQzo0TajZjQRCN7gz2DOGEVbPjbhvgE3MIzOjUozyJQte9AhUAM9tt_ZJP97_ww9opEKakNwYVisw_hl4auLeKG6PcsPLqnDOBpN2uPUodVCkgmHmbAShyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به احترام آنان که مرهمِ دردها هستند؛ روز پزشک مبارک
🩺
🔹
یکم شهریور، زادروز حکیم ابوعلی سینا، دانشمند و طبیب نامدار ایرانی و روز پزشک است؛ فرصتی برای قدردانی از پزشکانی که با دانش، تعهد و دلسوزی، در مسیر سلامت و زندگی مردم گام برمی‌دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/683593" target="_blank">📅 10:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683592">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef8f783252.mp4?token=G9f9-Rdvl1M2J9Ryoprl543w93MOPczft2MvKyCrXRLhyWp4RQkRXsJ-rph5v1f7PDQmok9rsDo8zK1uo86TEteduFiHFUVrtl6U30_GtIipHmtapIVeQF85Ugeql5opGa5TPhUuzChENGDyR7Rc4thD-RW4XFRAGZ2wwvVEkI7tgVbhPmnhBTLpxQDBrmcCyeuEdCDKQOxB72y7viNzklMaZpXCLnVQLKM70hVMhv9VxLFGvQBwIFB-pxRY9lnUi3iQTF4VKqcZIwqM_h-h742MJaWOfZqnYK7dDA57yYNa95iKWPTj53jRDiuQLcHt9HDTVPHRJps0eWJQssPt4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef8f783252.mp4?token=G9f9-Rdvl1M2J9Ryoprl543w93MOPczft2MvKyCrXRLhyWp4RQkRXsJ-rph5v1f7PDQmok9rsDo8zK1uo86TEteduFiHFUVrtl6U30_GtIipHmtapIVeQF85Ugeql5opGa5TPhUuzChENGDyR7Rc4thD-RW4XFRAGZ2wwvVEkI7tgVbhPmnhBTLpxQDBrmcCyeuEdCDKQOxB72y7viNzklMaZpXCLnVQLKM70hVMhv9VxLFGvQBwIFB-pxRY9lnUi3iQTF4VKqcZIwqM_h-h742MJaWOfZqnYK7dDA57yYNa95iKWPTj53jRDiuQLcHt9HDTVPHRJps0eWJQssPt4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی اسب هم رباتیک می‌شود؛
ربات چینی با ظرفیت حمل ۳۰۰ کیلو رونمایی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/683592" target="_blank">📅 10:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683591">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای خبرنگار وال‌استریت‌ژورنال: ایران و آمریکا احتمالاً دوباره به همان تفاهم‌نامه برمی‌گردند
🔹
لارنس نورمن، خبرنگار وال‌استریت‌ژورنال، ادعا کرد که به برداشت او در نهایت تهران و واشنگتن دوباره به همان یادداشت تفاهم بازخواهند گشت.
🔹
او افزود این بار بهای موافقت ایران بیشتر خواهد بود و تهران در ابتدای کار امتیازات بیشتری دریافت می‌کند؛ امتیازاتی که به گفته نورمن، ترامپ حاضر است هزینه آن را بپردازد./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/683591" target="_blank">📅 10:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683590">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc75a2a097.mp4?token=LfvRcfHUBLecXOIsIg3lNp429hcZQM06i-17wdYrgr2felrJJPAv3HOaDlfcuErzPbgPREcT1R88B4xIsxOtz5KbP52pv79voKiNmtk_0znQLBkz0AKIUPuAkO_6P-P7LtutBMuI8hxXlEosStVasrUcF4DqgvNepznSCkx36sK93005mCNGnAeezV6Cir6EHeDO7rObSbDWb9vF9nuEIWiCamf6LuMDB6Lcsk-37I0fb4T6RNJ02d19eBOzmBh6XBy5FZhZTIEZK9jTWnDtRl5_UoP3lbvyLxPeImxye6GNH334lA61hnatJX4L7e1qo1XB6xj2bj-ljIbr0SrOfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc75a2a097.mp4?token=LfvRcfHUBLecXOIsIg3lNp429hcZQM06i-17wdYrgr2felrJJPAv3HOaDlfcuErzPbgPREcT1R88B4xIsxOtz5KbP52pv79voKiNmtk_0znQLBkz0AKIUPuAkO_6P-P7LtutBMuI8hxXlEosStVasrUcF4DqgvNepznSCkx36sK93005mCNGnAeezV6Cir6EHeDO7rObSbDWb9vF9nuEIWiCamf6LuMDB6Lcsk-37I0fb4T6RNJ02d19eBOzmBh6XBy5FZhZTIEZK9jTWnDtRl5_UoP3lbvyLxPeImxye6GNH334lA61hnatJX4L7e1qo1XB6xj2bj-ljIbr0SrOfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدحسن خمینی: فتح مبین مربوط به احد و بدر و خندق و تبوک نیست مربوط به صلح حدیبیه است
🔹
گاهی ثمرات مصالحه درست از صدها جنگ بیشتر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/683590" target="_blank">📅 10:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683588">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c0b2ab9d.mp4?token=Z63Bo6q5H0JNcauHYHvTbGCJRH1GGpha-LyOhzRmS2gkg1uYQGYj5bDHQQIm_bm7AakfO7R-Y6QEQfWIxqaE7d7OKMM7KQ3Z_uoGj70gqnzfumaFUKddyMt_mReUoYDUvvpLzzAoi4KMw9xnc_1S6qCIe2X39XUt4D7tEWYMPeDdekjfTPZcELSCljuJd7Qwubwu7bD_nb_BGzqFILtzNYgSHJZb7aHVtyjUYginWMqOdvJuRD74iWI0wSSZHv1Pz_AzN1gWZsJ5QEjR3LJdXVTvSsVhdGNllTVSjROq4ceZlW8ftRcBDEmxG5XFZKUuI0W284Cm1pqTowkDQ-Na0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c0b2ab9d.mp4?token=Z63Bo6q5H0JNcauHYHvTbGCJRH1GGpha-LyOhzRmS2gkg1uYQGYj5bDHQQIm_bm7AakfO7R-Y6QEQfWIxqaE7d7OKMM7KQ3Z_uoGj70gqnzfumaFUKddyMt_mReUoYDUvvpLzzAoi4KMw9xnc_1S6qCIe2X39XUt4D7tEWYMPeDdekjfTPZcELSCljuJd7Qwubwu7bD_nb_BGzqFILtzNYgSHJZb7aHVtyjUYginWMqOdvJuRD74iWI0wSSZHv1Pz_AzN1gWZsJ5QEjR3LJdXVTvSsVhdGNllTVSjROq4ceZlW8ftRcBDEmxG5XFZKUuI0W284Cm1pqTowkDQ-Na0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنکیک ژاپنی رو اینجوری درست کن
🥞
مواد لازم:
🔹
شکر ۲۵ گرم
🔹
آرد حدود ۴۰ گرم
🔹
زرده تخم مرغ ۲ عدد
🔹
سفیده تخم مرغ ۳ عدد
🔹
بیکینگ پودر ½ ق چ
🔹
وانیل چند قطره
🔹
شیر ۲۰ گرم #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/683588" target="_blank">📅 10:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683587">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGx3aQdmVV530cWtetFpR16wb0rVTqu36SsYM8Um4Yc1YiEHWPO5L2wQqlhiCiJX0ZYiDrEfvNfd1_1j2QpwkUyQwhzNoY4eBfDetcLdqy_PgoscSqfoipoUlT7lLwccJehdP7_5-zgsJ_JIfqc9qoWjZdLssofX7vThGLpecItQMt1DOoTlQ5b1vVw7f1nTGMUT_4Ls5vGmv6FoIFd4VALy59upAWJDc09F0qn_A2jgFiwtHo7zbBFZonDJEXucUNlpgrB-IWWeDK10hUVnUdLM6SNKxluoqyjLVo0dJKq-iB5WuS_P94YqY9Mt0tzYvJY7T9SisJ_kGa8gELmplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقش‌آفرینی بی‌بدیل
#بيمه_البرز
در
جهش
#توليد
و پویایی اقتصاد پسا
جنگ
شرکت بیمه البرز با محوریت
#مدیر_عامل
این مجموعه و ارائه محصول نوآورانه *بیمه زندگی و سرمایه‌گذاری پروژه‌محور*، موفق شد ظرف دو ماه بیش از
۱۵ هزار میلیارد
ریال نقدینگی را جذب و به شریان‌های تولیدی کشور تزریق کند؛ اقدامی کلیدی که در شرایط حساس پساجنگ، نقش بسزایی در احیای چرخه تولید، ایجاد اشتغال و بهبود شاخص‌های اقتصادی ایفا کرده است.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5089</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/683587" target="_blank">📅 10:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683586">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس مرکز امور زنان و خانواده وزارت کشور: رویکرد مجلس به موتورسواری زنان مثبت نبود
پروین داد اندیش، مشاور وزیر و رییس مرکز امور زنان و خانواده وزارت کشور در
#گفتگو
با خبرفوری:
🔹
ما به عنوان حاکمیت باید به منافع زنانی فکر کنیم که سوار موتور می‌شوند و گواهینامه ندارند چرا که اگر تصادف کنند هیچ بیمه‌ای به آنها تعلق نمی‌گیرد.
🔹
در اظهار نظرم گفتم که شما ترجیح می‌دهید از نظر شرعی دختر پشت ترک موتور بشیند، اما خودش رانندگی نکند؛ این چه تفاوتی دارد؟
🔹
راهور می‌گوید ضرورت دارد که گواهینامه موتورسواری زنان صادر شود.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/683586" target="_blank">📅 09:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683581">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uls5xqTCdrtmnBk1UJ58hwyOJm3TKvVqDrgGeMq4E0LRCZJc5eYSMSGoFQSsVclmLiUUq1ouWVg9bAkUFr9AkFiOZcuODtQNroY5F3FT-aOgzc0LdshNkvxeTQMP4MyNoR6Z1ABvD5MYVMc7jElHHgE4kLrsN7jT9b-LGOO6bQAPAsDHb4a24G-EPxiGXIe3B-aBTWEbH-w8PpyIZs74o3bU7ShcPBuZj7QtYP5OqsmQO5Y4Ja6Ow-AL0nd-Qsuq2JMmxjgTt3tlhlqekoi16oHVNe-EQ7siK49nIAMoExXPrjkWvlDxyuz9QJYUMVVDhrJoTXTh33RtUUCcV0oI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستوفر دیوید؛ افسر سابق نیروی دریایی آمریکا و فعال حوزه فناوری و دفاعی: یک ناو هواپیمابر را «یو‌ اس‌ اس پدوفیل» نامگذاری کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/683581" target="_blank">📅 09:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683579">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5bcc0df7e.mp4?token=IoEbQNdzUxEyn1Cc5vxWVKBLSlfaMGQ3GbOHg__jjisC532gwW7RXe7Dj8nmq17_hAiJH4_Xvs_uGfA3zHGls__rFGnx0j-3O5BAV5dq95oiNrOdSMfvJurpm7qD-7HNBV_I9y8rYoMtBr4M2rqtNVbCB5j2ShpbAeygCbjaTPgUPav8OYgn4clpYfJFNTQWcsw1dYxLbNd6SoqBBlmIpt9skaM9N57wqdrusOssjUBTjOCuJKpx1HBS_HNweIekx59q4ZaZfrjYvFsP3P1SwEULfoWYLdf5Gbw7VwPYyJPtq95n3lW_GXbCEswPHEOMfGhBVOH8f1D_lWRmlJ9fMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5bcc0df7e.mp4?token=IoEbQNdzUxEyn1Cc5vxWVKBLSlfaMGQ3GbOHg__jjisC532gwW7RXe7Dj8nmq17_hAiJH4_Xvs_uGfA3zHGls__rFGnx0j-3O5BAV5dq95oiNrOdSMfvJurpm7qD-7HNBV_I9y8rYoMtBr4M2rqtNVbCB5j2ShpbAeygCbjaTPgUPav8OYgn4clpYfJFNTQWcsw1dYxLbNd6SoqBBlmIpt9skaM9N57wqdrusOssjUBTjOCuJKpx1HBS_HNweIekx59q4ZaZfrjYvFsP3P1SwEULfoWYLdf5Gbw7VwPYyJPtq95n3lW_GXbCEswPHEOMfGhBVOH8f1D_lWRmlJ9fMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آنچه در روند تفاهم‌نامه به آن رسیدیم، بدون استثنا اجماع کارشناسی همۀ کسانی بود که دستی بر آتش داشتند
🔹
تکذیب می‌کنند چون بیان قضیه را نمی‌دانند و یا دستی بر آتش ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683579" target="_blank">📅 09:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683578">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dff09b5188.mp4?token=Tx5JLHs_Fl3nTleqm3d_7Pl5742zDs9WF7eiVn68hCrs4_uMff3JbsMAROG9rMPJhMEAJcGfor5yw5wXztnNRasn5LpcuSEmjLXLKJzWaRAl-Cx3s5NVMC6p8Qg46IqMzjF-6Xs6okRD4ABRh0cuJCOQQnzCa9ojdNFn-DKABy9aEZZo8oF0gYqhGOlFBwfGSpQyZ3nLYmbnBI15KamE5HXeAgZvZH8sLhbmBOzXlru-mx47oPGM9_X3VVB0Gzx_YodiZ8RoLEzlwQQW4tKmQX-zyKIA0SA-v4LHblGlsNdWJPwMfxW3RvOmXQxUtIbMhQ6GkA-L23qGiZ-W0MK1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dff09b5188.mp4?token=Tx5JLHs_Fl3nTleqm3d_7Pl5742zDs9WF7eiVn68hCrs4_uMff3JbsMAROG9rMPJhMEAJcGfor5yw5wXztnNRasn5LpcuSEmjLXLKJzWaRAl-Cx3s5NVMC6p8Qg46IqMzjF-6Xs6okRD4ABRh0cuJCOQQnzCa9ojdNFn-DKABy9aEZZo8oF0gYqhGOlFBwfGSpQyZ3nLYmbnBI15KamE5HXeAgZvZH8sLhbmBOzXlru-mx47oPGM9_X3VVB0Gzx_YodiZ8RoLEzlwQQW4tKmQX-zyKIA0SA-v4LHblGlsNdWJPwMfxW3RvOmXQxUtIbMhQ6GkA-L23qGiZ-W0MK1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: کنار گود ایستادن و حرف زدن خیلی راحت است
🔹
خیلی وقت‌ها می‌گویند این را نگو که اگر کسی می‌تواند بیاید کمک کند اما کنار گود ایستادن و حرف زدن خیلی راحت است
🔹
کمکم کنید بتوانیم گره از کار مردم برداریم. ما هرچه در توان داریم همین است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/683578" target="_blank">📅 08:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683572">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
سهمیۀ بنزین خودروها در سیستان‌وبلوچستان به ۱۶۰ لیتر افزایش یافت/ فارس
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/683572" target="_blank">📅 08:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683565">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbvPB8KfssJxMEPiDVOnDT5AYKDF-MK7d--lVIl8sYFNr5gf6R-xwLJdH5BVrGc-MVaou_DQLm5QKw8qkfjAc7yOr8ZnCyVGZcQlL_QjPsEPgjiZ6dWVWZ9_zoc1QSlATwreeB6pHToUQ0DISKLWbU_mqz2O7APLWJB3vLDGDaiqAHZBVirL64ldS4D61s_3Q52xxLrhvlA8VrZ9mR9Lbl2G1BI_4FoY2v6Zzzpufe_vvE7L1Q83rM5QXf2Qj8x1vZTRtxJM9-c5EptOq4-OWPbQHpwz9-yWKun6BhHgAk4QsoXbWG_WVJSW5r1YcoczZcsxhz9TSOW7F6C8lPMnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hpk6NduKfJ7L1eREZtP4K6v_uWpuLQKA3ZDeqZYLZaOoxMGfp2FdmIMbuskRkLQ7MVeRXHczOUi0myB1ZFFTDHqtsNXmTBwAvRogXSooShd2DGvEafOtLFs_I5Vvz4Hp3TrlYmNhg6GjLpA-kM9oLBcnODXNokziK1bVG1o4uc0xjPev3eZWNjWPVv1_eXOmso4VId23nx5MmUYR-L8EUSKjNTFvIbgcd3DVEgLugdDBewMceFooIezlUTuBs7gKP8PNMMqyVsSSdGkGYdmFpQi7feTcpU5TtOjDLfEnaJpHOnNs2GgARhZPr_Q3p8ZPWaIhmmu1xR5FfDuSc2yZfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8-g6EZUxdM1whOoR4hNDhuurNwR4xnvA9y2zwKWmtRfAav9LiKoCq_q8Iea9ZSBXQVelfq0lThzIws-MwNA2P3hwJ6v6D571T5WIh0DdtcNCC4PNLCHy6iEh2So2lT6I-fco5XB348Y4Dml8Lv3MBWvwV-VP87Fqf-t32d9IP8i2KT1djUe6_a6aLtuO4ey3_qE5DGrQsPmanVSj4auaySpD_bXdv8Dou26FaBjBQhCLOZADDOZV_8-w0gRHsthQzi3A5Tt--x9BYpwFYO3D5IFtq40TUlLXybSDqLCHHpWAr77GjZfKzZkwLJnnq9DcPyrkl2LNfRKw_iSxtdAaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCyjvt5b5M9l1bwHYaKwJ0acEOy3lJiMPdOEBDFceHBu8Hn74dujqJzYDvtHT1K7DsBBZW6bpzZnVQkSNFE_kxFie6x-F8-8bVkbFcsVkjQoEFUbs8Fop8CC4xH89v9YAhXqPTXxm5fF_GNJCjxGOhV_Q9pe6IplWWAcTJRBdeV2zQmE2Zs8nRqjTH968jIn6FX6NJFGXcqhVxDuyXegkPOO8-u6Vt0QpQovVKw4IhgEsEbBOXPegGSiqxnQNxTZUWfS6MKjLJSlLakrBonSwe_3Jrx2sGHXL6pQIxKc2WtgDwTSMIrjVml9fwy8hEPbE10hzmVYLY_XPwj0Wu7NMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QA-eu3cYgod6b5nWwBLkMxGdyOM8Yq0L2_fvuYgdOtGtL0AK-y3Pu1lAtmpMx6GlmUoiVxB-Unv7Afu_MvctDJsY2Jc9pNWZDSCckeZJu-eRmPF_hqtVICoGp1AN99vB-TFxjZFvMTYLMqSqKi9322a_5YCMW96Db9ad1FGyeG6kodIe6eLcL2Nu6mX3cYZkfnnaizS2pAjpLRJoQe9DYxH--Ygv-RBWehgKJW0GdZpL9IPfWBgVBwPmjd-3GnAxbQ65X1HeqQiauymHV3M7S0irHg1H3WzmsybBKLyFVZhPqHBcpq-HE4IfFz3kQimsL0OD96Y0JTN2aYkDxUljzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFYZtB4P83HO99zq4EdySPzLwqyI2GIKjX0KKZn2XDb-BCwonyKtxknAYSB4STcgJgRbSEPQjKNCQNfnxmB5cesStV0lEv_YcEZevys94QnrvX4SSsN9aracPFOvrYFJSnc5basexigrkbqDoIHunb4aZ6XpN9sLcgMhNYNGJF15XDOE0XCfcsBzDHNbmtkdTe_QEVe5I9XdwAXwS9IOuvBmEbjs2nL_gkQ2kIXG4ZHJTnGvVKPXzD_7LREqp0130QNSJUNAieZw5T9uUlOu4lbnyXFS1gbyoIrMWT1x8viF78NmSkuE9ffWcGQfDdqa4TPRbd8dMh5imrehEF3Fvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiB_nJpza2rY0wjv7kV6yJhqhiNATKZ_FANWUEraImI1CbNwesoNASu2miE9LgAVJFWx4rQpdb2Bk25Ws_HkQSj-3bFoNNOs3qeyqs5rRKUcr2ihw34KQrWamziOHfRLr56DkIFJmsHhIn76w-MyB4ufqWQwtMzu77hrtgSFUuVlqdP-kyk1yCVvDKh7ICN7bv7KPzpovD0jfUQTJlECT3oawzc1EkFaphf4R3a_K3DZLvllY-L9Uhur8vWBVyUUci7Dy5RI6goGNIsZYjD1a1hBpS2ihX5hRza8miIlX8kG-YGYkkz27BSUezBU2qt7y-7wNcba4YcVmorggqGCWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دریاچه نیمه‌جان ارومیه، غرق در زباله گردشگران
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/683565" target="_blank">📅 08:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683562">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85989e410.mp4?token=gKSk_WO9nR7pIpmuEk7LZQW_HPRUguc3Ukr1iffCwcI4UJ9qonytszcYStPXke2tO9P8pa5vtYhxhh3ZAj_EDcKkszWlhJMWbFY2MvyjwrdupkRnNZudWsVlgjRC6tamtT5mO4aB5sA6BtgfVFpBRSHY9fw1GEWsDPDzBUa9ZBioqrxMEpsepkN1bCykT4YtobHRLynigwxkl62lcFfqXC9Qemc3N6P0jtHEH8KOMKGZWgd1T0Qpp8HVJGpGo4tOM9Rxn2ArT23MlnC6q6aeUEpsid5Xi1_sACL1iU1tzEC8xgqu4cwTb_06WVWggWl6E3LKVGubA9YPVxcTDRGzlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85989e410.mp4?token=gKSk_WO9nR7pIpmuEk7LZQW_HPRUguc3Ukr1iffCwcI4UJ9qonytszcYStPXke2tO9P8pa5vtYhxhh3ZAj_EDcKkszWlhJMWbFY2MvyjwrdupkRnNZudWsVlgjRC6tamtT5mO4aB5sA6BtgfVFpBRSHY9fw1GEWsDPDzBUa9ZBioqrxMEpsepkN1bCykT4YtobHRLynigwxkl62lcFfqXC9Qemc3N6P0jtHEH8KOMKGZWgd1T0Qpp8HVJGpGo4tOM9Rxn2ArT23MlnC6q6aeUEpsid5Xi1_sACL1iU1tzEC8xgqu4cwTb_06WVWggWl6E3LKVGubA9YPVxcTDRGzlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیم نامرئی یهودیان در منهتن
🔹
ویدئویی از «اروو» (Eruv)، مرزی نمادین از سیم نازک در اطراف بخش‌هایی از منهتن، بیش از ۱۷ میلیون بازدید گرفته است.
🔹
طبق قوانین مذهبی، یهودی‌های معتقد در روز شنبه (شبات) اجازه ندارند اشیایی مثل کلید، کیف پول یا حتی نوزاد رو در فضای عمومی حمل کنند. اما این سیم نازک به یهودیان معتقد اجازه می‌دهد در این روز، در محدوده اروو وسایلی مانند کلید و کیف را حمل کنند. این سیم به‌صورت هفتگی توسط خاخام‌ها بررسی می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/683562" target="_blank">📅 08:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683561">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDdkwRgCpsI43R7K3GxOcsduQQVY0Ldg1Rx9I2DRkBPHa3Cghzf-L5qEanaMh7qmYUqX8QfXhMmHSksAXY-xJrJ0izVz-lkfhQc_f_-wCAkdwvd4HnX06EKHJ-QuF3E4SLjQO0VuuRadjL6bdtArWPfsmzRV5iXlsnhrmqVxTDShqPhKbbT95iFgsZopAjjHMGo5iJFOi9PLq0TR5drOidETMX2O69x7gaAhP111hWMITLuggBitKab29GD_b109gpBCEl8rMg0gAvDi9erlUUOxWUUIvd9F2CwIsCx5b3psDavyGOYRH1BbI8SEIiFGrQdEgUVhLHqrSIyw9n7lyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجید آدینه از تروریست‌های دی ماه اعدام شد
/
آدم کشی با کلت کمری و اره برقی
🔹
دادگاه انقلاب کرج مجید آدینه را به اتهام همکاری عملیاتی با رژیم صهیونیستی و گروه‌های متخاصم به اعدام محکوم کرده بود.
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/683561" target="_blank">📅 08:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO2Zyttbii3-a1KEM20WMJ6Vx2OwgDBcfT1ILfy8YCInOL4NxAIowpuf89h1vdIGGBOr5Qc0myjiTsQU_dlwb8XpbIemF6F2GKPN9DzFhiSc7l6WTf29_sO7RpanCpI4EZXG2dtYOy48FqX2oFrKZqQlcvBtYdiyvxwuXIoRJ9pxwwfFYbXZtqBUYIsYgGsLdLUhMhAATT3bCBiaXNQfgEmTn-gRtaWQrQFQ5DUqcim93mHQzbHkKKrttsksvV6xA1fF9ATlGop3WSbNdFACH2XJGfnEfy019T_BKQNOqVSLC0kXQWwfbx6FYKMNfeIl5zYYhNanaybGI95rmWqovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم: من در حال پاک کردن آشفتگی دولت قبلی هستم تا پایان دوره‌ام، دوران طلایی‌ای خواهد بود
🔹
اوباما: وقتی دوره‌ات تموم بشه، آمریکا از نظر نظامی ضعیف‌تر، قطبی‌شده‌تر، از نظر اقتصادی شکننده‌تر، بدهکارتر و با متحدان کمتری خواهد بود
.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/683558" target="_blank">📅 07:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
مهدی طارمی با عقد قراردادی رسمی به الوصل پیوست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/683557" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683555">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHehp2_etoixUeEO-MI_ZpPK4sBbpLiaWQqv0OosZVOLCB-Ygt8hpR7Q5kaiCU6ygmEE5DgRdniCXHcOQWd0yxp5gwDolcF78TwXCg6TIA6Sz1FJTPe7g5tJvUt1Nek_m1fYofwafazrzUKhbrT2sJrsb_STuf-Y5x3FOL-pTqntuAHqHFZ5VTezYHzDdj5SUcZLUq9QAZkEEvYyt2qlz0kelrR4mZZVFgNt-2GyZKwNyxhfDLMXs-HH7OFvlumc3ViiW0xQ38QZdNr3W7JM7DvbuNYH5-CCa-67QnusKvOrGFyZhKVU0Vo6cxXs3RRPriLNytLPPcrrWKtu3bvrCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دن بیلزریان: ترامپ بدترین رئیس‌جمهور وطن‌فروش عوضی‌ای است که این کشور تا به حال داشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/683555" target="_blank">📅 07:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-FJFZYlm9vjKdHctLYK0t_A9a2EEy97VVpuFn0ccqomej2-aPRppSYNVDMsGYqkJHbxBfiwZr-mqSe9Ih-O1Xrs8xRd51LiQ8z7i7tWlo0M75gYvqrwnkRwCslLXnA_pD3B1-yq72C6xi9bQf9ZGxWQ3Fb-mdnQgiKLo_J3TcnwsFOIjsAXop_-7L7AFr65D-UYnNy9R60W6cZM0SXjGmRq7PFopyva2UFZva9YY54t2nHlsyvLcediYy9OnH-YU7owa5o3-LkJd78UZVvgR9y2PK8bC5WeFYRpXKDF_GwNSC6Wl41_WHcv8RrEUS0n55nUoIZgoiWf7_sjOVcNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش از ربایش رئیس جمهور ونزوئلا توسط آمریکا، غربی‌ها و رسانه‌های آنها اعلام کرده بودند که طلاهای مصادره شده ونزوئلا در انگلیس قرار است از توقیف خارج و به ملت ونزوئلا بازگردد اما حالا اعلام شده این طلاها بجای ونزوئلا قرار است به وزارت خزانه داری آمریکا منتقل شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/683554" target="_blank">📅 07:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJEYZSf-Es-0RmdcFjrLgrYY2Dt_26xfHXGSGzpxO5r8eecLWkjAf72QEo74Iui2Ou97Vt3CDL0k5wZnaWF3rTfCE3mO_yvnZsLjgVeurLmk4neQt8b40g1SeTi0sepCjYywTOQaUJKivppalOCHawai-iy0B_ZwdS0430gTl3pXQQvMyE_ZjGR2Yvl6fnAQK46iwavvxb-n0txmFqjZ5_tILE8Xolw79ykwjdZBcvUuNnPyZyiHNTrIuswLfFgUdbMuEYBwxes6EOon2Fuz0gALTPjUPi9LKqR3_kZ7s2yVfeAOStMD5K3paoiN94CfVglWTxKJBOU6KkV8-SG2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱ شهریور ماه
۱۰ ربیع‌الأول ۱۴۴۸
۲۳ آگوست ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/683553" target="_blank">📅 07:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT5mW13FdiT3IlBWpPw_Lbidz1Bb-p16I8s-TS0Id7i2JGIwKPXBFspXwNrVSHhgVzGa8yVGJre371lmOXjuWDDsCHaZujXouYJrLT_LszQ8CY8n4gqs9nbPeM-bWU-kneNepSisDPtHSILZw2fzNIcqObme5vqb8h8k7s5UH68aanUmgmu1Z5wlqOpgd80ageGBZVtTv4L52nqC4JxHT4LD07fxKv0VP8aXIWKnT3nXb8CytlgIe0lYXRAiafDLzPTk2HC4sGn9ZXNElIZLSubXD5P9BH7v_DnMFYusEz6DqOxTNKbiE6utrCyIYVlrR-BtfuFXa9MZxjBXvCAsCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف مین دریایی در تنگه باب‌المندب
🔹
مقامات یمنی ادعا کردند یک مین دریایی که متعلق به گروه انصارالله یمن بوده، در منطقه‌ای مهم از تنگه باب‌المندب کشف شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/683552" target="_blank">📅 02:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ec443314.mp4?token=ZFopdn7wE8cdbHONsuorVR9sUMs_oZdguwH2FKPMgE9-4Iw3mqYx-pz1R7gdl_Uytx2wpYllioYB1daLtAxQD0MpWD8cTkk-zAfQftgbG0zDOE4a1zcBxWFxb7y0HsWRc4ffkQVQl5NbqgKpLOa77f2NHIpJVhQ13T1CjFaRf-_m5pR7N6uHP530xcnFAFxdAa7UUhxOEuk1mJDBvNcKqTG0blpyB8QK9SR7vLf6f8S-GvAcTKfgKAvkQ_gFeArtRQdhNgTnUq7qW_pg-zDF4VfHnv1GaUZbAeYbwrHuCqXI94WKQPbIfig3CEEqZMThRAzygKCtite9YEmsJ8EZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ec443314.mp4?token=ZFopdn7wE8cdbHONsuorVR9sUMs_oZdguwH2FKPMgE9-4Iw3mqYx-pz1R7gdl_Uytx2wpYllioYB1daLtAxQD0MpWD8cTkk-zAfQftgbG0zDOE4a1zcBxWFxb7y0HsWRc4ffkQVQl5NbqgKpLOa77f2NHIpJVhQ13T1CjFaRf-_m5pR7N6uHP530xcnFAFxdAa7UUhxOEuk1mJDBvNcKqTG0blpyB8QK9SR7vLf6f8S-GvAcTKfgKAvkQ_gFeArtRQdhNgTnUq7qW_pg-zDF4VfHnv1GaUZbAeYbwrHuCqXI94WKQPbIfig3CEEqZMThRAzygKCtite9YEmsJ8EZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت رایزن فرهنگی ایران به کشور که در اقدامی خصمانه و سیاسی از فرانسه اخراج شد
🔹
خانم نیلوفر شادمهری در دوران مسئولیت خود، با برگزاری رویدادهای هنری و نمایش‌های ایرانی و اسلامی، تلاش کرد تصویری متفاوت از ایران و اسلام ارائه دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/683551" target="_blank">📅 02:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683549">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a6f6a7d3.mp4?token=rF_rHGKaDgyLKAc-YWZBme_9qbPIxc_8_mC5QrnIIJReLyruwl4TeTv4SVclf4TSZtgjKhpj6ZCufOyO_GkUH75dMJNt1KhRupL2i1f4Wbvolfz6OhfCZKUYACR0unFX5cPQXS_fG5cpDUZ0Iu2xYSVkdbylDeZY43v-McLbc4roU2TxWaQ1tgdpGQXTFakFpU7EScmWUzELCKEvvs3qXdtbJkofRR0NgtyUiWD6MaD318FWGb54Q07LPonXJ7iajA4iC07nYkDfYJFywNN-wdpKf_IxfRvQbJVuyCyAk3gDoHbyqfvNhu7xbUumRHTVpgOF2domWkJ1J6wrbzFCVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a6f6a7d3.mp4?token=rF_rHGKaDgyLKAc-YWZBme_9qbPIxc_8_mC5QrnIIJReLyruwl4TeTv4SVclf4TSZtgjKhpj6ZCufOyO_GkUH75dMJNt1KhRupL2i1f4Wbvolfz6OhfCZKUYACR0unFX5cPQXS_fG5cpDUZ0Iu2xYSVkdbylDeZY43v-McLbc4roU2TxWaQ1tgdpGQXTFakFpU7EScmWUzELCKEvvs3qXdtbJkofRR0NgtyUiWD6MaD318FWGb54Q07LPonXJ7iajA4iC07nYkDfYJFywNN-wdpKf_IxfRvQbJVuyCyAk3gDoHbyqfvNhu7xbUumRHTVpgOF2domWkJ1J6wrbzFCVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران آب در فلسطین؛ تمسخر مردم تشنه به نام «انسانیت»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/683549" target="_blank">📅 01:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683548">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
لارنس نورمن خبرنگار وال استریت ژورنال: برداشت شخصی من این است که در نهایت، دوباره به همان تفاهم نامه برخواهیم گشت، اما بهای موافقت ایران با مفاد آن، از نظر امتیازاتی که ایران در همان ابتدا دریافت خواهد کرد، بیشتر خواهد بود و ترامپ حاضر خواهد شد این بها را بپردازد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/683548" target="_blank">📅 01:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683547">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سهم شیرینی از سبد خرید مردم به کمتر از ۵ درصد رسید
علی بهره‌مند، رئیس اتحادیه قنادان تهران در
#گفتگو
با خبرفوری:
🔹
قیمت هر کیلوگرم مغز گردو بین ۲ تا ۳ میلیون تومان و مغز پسته حدود ۴.۵ میلیون تومان می‌باشد اما در روزهای اخیر افزایش قیمت جدیدی در شیرینی‌ها اعمال نشده است.
🔹
با توجه به کاهش قدرت خرید مردم، سهم خرید شیرینی به کمتر از ۵ درصد رسیده و قنادی‌ها عملا از سبد خرید مردم حذف شده‌اند.
🔹
حدود ۶۰ تا ۷۰ درصد از مواد اولیه قنادی وارداتی هستند و با توجه به محدودیت‌های واردات و افزایش نرخ ارز و دلار، شاهد افزایش قیمت‌ها هستیم.
🔹
سرانه مصرف شیرینی به ۵۰ درصد کاهش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/683547" target="_blank">📅 01:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683545">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
رسانه انگلیسی: هکرهای مرتبط با ایران برای نخستین‌بار یک نیروگاه بریتانیا را چهار روز از مدار خارج کردند
روزنامه تلگراف اعلام کرد:
🔹
هکرهایی که به ایران مرتبط هستند، یک نیروگاه کوچک در بریتانیا را به مدت چهار روز از مدار خارج کردند. این اولین حمله از نوع خود در بریتانیا است که تاکنون گزارش شده است.
🔹
این قطعی برق، شبکه برق گسترده‌تر را تحت تأثیر قرار نداد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/683545" target="_blank">📅 01:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683538">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArWkFC0Bap3Bp8qnnQ0yacXjiQ9VIy9D-nkLIqz6Thi06GNAZYp9tXxzkYEMpcxWEeASnZwzOyOBzAVgHlYezufyiq_E7IzMDvbbAkJ3DatpBtnHFbKNX17-LruHOto6AjF2p39lcUYkBG5Xl117JxGUiuEW74fyfXL2agAPXFOQkLQDeXrXRDySLX8_sEpqx5iXgaHtl-npQic7dqIf-SqS6jlmcBDZPHflyLJ6awmiPapuJLn7fkCIpng8O7kbYIEfTVSP7pqtG1kUKUF9yy5eqDkgk4ZidQqpz2Jx4CWs7Gchgdz9aIDz6jAdT4PTDhMdDbyRLk2IE3bmYQOa7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYcNJOD7XGw8kXJWPKruzOZSDkE3EhLHjyV6gwtAhakFBtvekyPN3y2Vn4AQ9XHdGBZC5vkW3xm_nTyL2uRGQpsyNnASjsS-JT6JA-Qnsl-GRU3ocGvabFltAnLKtwy15f_UlDIDdCcxAlbQh5wuS_fj253cJ8KM03d2Xmto4dmh5X-SASfyV1LqJ1xZ5bBV9XYDvMGiKi1-xKUCMWjupKJADTqs0V9lKPSYavkduPrGd89VH3tS5orIdXkZmxZjmQxpIG9L95Z0lFIOdz4plGGFnlPstTNEaxef_vT3oYIJD2r4OogqBUZqRpDdqSC36rWfbzwLeJPkD693InI9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4xzimIJfNU_tIzKWTJrpCgcqVKThupJia2TGfGjBHVGayMmBF_WqN2MpfXiGqw7auUHiNvBQ_7Q1Lb4VTBEraso1p8-RtFVXtUqxyAX49nS2YYC_bChz-vfEkTbBGHz_WTUKu83wwOeIV4cUxY66dZdjbkwDxlOQj4XYsc3AUhQw81rC0NRjya82DyoRezxEysA1hNOr1iGpRlSFUvZx7n--qzA7HcYpbI1KjoWV55KIXy6umydUF8BJosOU1uSAHQx8ACUX3uGpQvSJsPAc76a22ymW_NzbW3-rDlCyLhE6tt4xM-Kll_-CwLUpU-dm3CA7JuS_cmkIaag_itqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_rBAwwpg4cH7dglgWpMdmcabI7bUq-bHtnQrpkNpidcsbYeMw6bfKjdLAF6UqvlrzTdLJ5ZKYTpNxBSi7QW7Sjg3cubqW_h2a0dthFtsp_dGEEF5uQOpGusyiodvpp2zM02_d6PIiupsaI2hoZOi_WAWS1Uwdn53CMzEYFwiAqBH-vqWTl7mLCF98buAmAuQkYcEFlQiCkiyuIA0SMGtrzHZDkO-Yk3uTCECNAJzLwBU-eC7HCWnf2lxA4rsVt4jDhH5B0fZFdQ9mN8pkK-hfzIolbRmDkC2UF8unAvi-HiEK9Sx3iZuY8zCMmOsEJ8ElRyYFhs9cyBo57eQ8AkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agxCgIH8T7yZvqa3eB8YO_16mRlXMqROFfZXo56L1g8fgdNGxrIC7WFbhi1Tz_9Doj-PFQkyRVCSZBEkGSVCf0V8Chwzlm4wvz300Xf6WcNdSomiWNGcv7nmjsORYBm9eKg-icAyxnBMKr6UhJVOwJSd3ghz2ONd-pQSioAYEqdu3NP4kYDmAIIRRV4wDk4s-RfZlwJ3DD1ZvIdm8TdyVvmHWwFqcOBWa7ot4aFIGx1VdVzEslqsAkDLo2_MI3a2GIqonmZl3yDErF_gnMh3_MIuQZa-VvkSxVnsfhsaiWVRMrelB1Z8cOxOIVeGz6abck3eQVT14z5B4kOh__NP7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSEiUiPhGhBUBBMNebFfpYywV9QeLku7AQLmXr8hT674lPhnoPsXhWKG1lbHsJnyBH15a0ghemZhStLUN84t9jzrvmRYNEOdCFo7Mi522V78QoQj9ZlbQqr5Df7sa401m0UMfu8w5I2ekcoI5sDD5yFvWk749ZziLfoxwtkVsXXcBymPtPgmyvblJnn01ECV_yg1B5Bwjbjvi4dZoLbIQ7YtsBlERZnfZgJGldncBJfKBBw4OOoRYAW2xgNXe4h7TaA3V9_WWl4LQkyX3di7UX7eZjPjO332GshL30GXuQB85TwZFUXgHMc-5viMNtbJnxoOrRtlejlmJvyrZOwjuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzsN0rdMb6xUlrwTPO8i1BqtA_8JtgdifL5oV-MBdcbv7wmUNar-95jtXHy3snJQfwNgbzaC_kv6-WQtuQUmLPSht4fgzqg56eKej2RfmUtBkk31mjHoG0CdSoQFIMKuHh-RTFwR8vTF1e2QXfGTJ5n-emj6Rmm4rqKXnEspNpG8_1PgaxoWh2yld4pghl-RM8QrYqj1B5pmI-EqHd5xdmLoEvxPtPKOuW3h5OYkGpzTQGA2zz5_JpKCcZpVh3C1ni2Sz0fWu_kMCsBGxMFHvDdcW2YEa2xsFYAwFJqbT1UXxorIzuJzB1mkyok2xUh0DQl7c3VPrsMRvSrXU5qdwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شغل‌های عجیب در زندگی ستاره‌ها؛ رونالدو متخصص خواب دارد!
🔹
فکر می‌کنید فوتبالیست‌های میلیونر فقط مربی و بدنساز دارند؟
🔹
از مراقبت ماهی‌ها تا تنظیم خواب و حتی «دوستی»؛ بعضی شغل‌های اطراف ستاره‌ها واقعاً باورنکردنی‌اند! در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/683538" target="_blank">📅 01:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e48556a24b.mp4?token=ZPn-mM3YMbNkZFE_QAdthHlAgOaLVQ0Jn93diCpNsnRr6peQAJOoeoUbWVGmwheuM-1aJkFfME95Ka5zDX0GWMT2g-2hMW28tYw3eoiKVDpSt33eqNJHYQDJOm3zVe8qdS9cX1OjRTrfYw_WoCEgU9wiMfhpWTlgKBy0IoEJQH-SrM9Z4vSaupM_Ig4vrwJSWng_5O73v7qUQgRwb50K6zRRwWI1Wss2_yrbc2662R7a8B8jy01iR0I30Ghpo6Oa2ueDtXz_uPgtuOBC0sNrpgdS5S6WkkCdrz4ZpASDA6Q9-MFAC49TwsqJGjMxZ_lbPwcMyRoVHSLeCTb2JRGhJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e48556a24b.mp4?token=ZPn-mM3YMbNkZFE_QAdthHlAgOaLVQ0Jn93diCpNsnRr6peQAJOoeoUbWVGmwheuM-1aJkFfME95Ka5zDX0GWMT2g-2hMW28tYw3eoiKVDpSt33eqNJHYQDJOm3zVe8qdS9cX1OjRTrfYw_WoCEgU9wiMfhpWTlgKBy0IoEJQH-SrM9Z4vSaupM_Ig4vrwJSWng_5O73v7qUQgRwb50K6zRRwWI1Wss2_yrbc2662R7a8B8jy01iR0I30Ghpo6Oa2ueDtXz_uPgtuOBC0sNrpgdS5S6WkkCdrz4ZpASDA6Q9-MFAC49TwsqJGjMxZ_lbPwcMyRoVHSLeCTb2JRGhJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات مردم آلمان به صدراعظم این کشور در نخستین حضور وی به مناطقی که دچار آتش‌سوزی شده بود
🔹
فردریش مرتس، صدراعظم آلمان در نخستین حضور عمومی خود پس از تعطیلات، هنگام بازدید از منطقه هورتگن‌والد که به تازگی شاهد آتش‌سوزی‌های جنگلی بود، با اعتراض، سوت‌زنی و بنرهایی از شهروندان مواجه شد که او را به تاخیر در رسیدن به این منطقه متهم می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/683537" target="_blank">📅 00:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbZY9IwJ8LurOmz0l-zxsujbnnGQO3ux-ZMHzO8_azOPplYVpKlg3Hsb18jsI8s2A--cFb5Az5QKGcY9qfDum8zLTSB2cMKCuhl68nyw5AgDB0geKXp4Fx4G8KSRJAu4MywCHNsBZmY7JDY1AdkPy4MwKJ3wP6bKpRZYxC6ZUZUhG0_j4bxOV5LjPLy_a4pNFZFeRJmsYVmXW-Yie7ufv1ll-3Kbkz_p6GHwBxXVPbXlq-4XPAvdktCtgSkeXW6gGEaRJUtaO86sBDSVcKT5yd2ACM5W8QHBdX9ngcMo_KvaRT5P-D4fRaj__e-MGYX4_q0MapxHxPUEBA_AFYRdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دست از خیال‌پردازی برای تنگه هرمز بر نمی‌دارد
🔹
رئیس‌جمهور آمریکا بار دیگر با انتشار تصویری از خلیج فارس «تنگه هرمز» را «قلمرو جدید آمریکا» نام نهاد.
🔹
این توصیف طی روزهای گذشته موجب تمسخر و انتقادات زیادی در محافل آمریکایی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/683536" target="_blank">📅 00:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e4aa207a.mp4?token=RGKJaYqinJyxMcWgK0v096c_g6i42USCXiUHZek6z4BgF8QWy_rJXfccZPJHUT-UtyCytIcQcYbjw4Ih-cBr-iAlOxWJ8-Dtg-Wgyq4QDPVFTq-DbXi46q9cGpRsAZyb8d93nLLmUxgGMwd3LwRUItR1XBUkDDFM2UseiphDP3XhZyuuQNcDlCQjVDvD62ptM9MoOb839PzLe-FFt1SN3C_6DBHnjnv-78HabV0twBYQfdGaWHYRK7Lx-duM7m8tkJN9PyVvrSG2lUq0pvB0CJ-iJ9KW5cNz3xAbocra6ugxwzx2ddGRch-QTwkJpQ6Y29YWeBSMU4PqUR6-aiFPtwRzTstxQdia3fbILyVaL9rsc7QUAkh-M7xaQZ8yiQM8x9wr1FCxL7E9wCYIFwVn5oivUYGXLBXRjlF-bfxsjbLm1G4BY6r31Mm32_W92SWij_0VyqUkGs857Z_TbO2vJkwbI1Cj07fdA0GZU3ppm33c9xvwSjyHYjLclEPsoR4THKXI1eC5ps8DSERUnQWewzjylZE8PDOmaC3LRheOJSPJs1TD_PhShNaKnPBEzIXDD27m5joZMyfMmIv30FH4qDvojUiRKBQ7-TXftnOl71Wu_jlq0iDamVLAGMXuqZqf0CbXeZXUeEXCviqtlyQ6cOM7sX4umKROLbtg5wAS80Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e4aa207a.mp4?token=RGKJaYqinJyxMcWgK0v096c_g6i42USCXiUHZek6z4BgF8QWy_rJXfccZPJHUT-UtyCytIcQcYbjw4Ih-cBr-iAlOxWJ8-Dtg-Wgyq4QDPVFTq-DbXi46q9cGpRsAZyb8d93nLLmUxgGMwd3LwRUItR1XBUkDDFM2UseiphDP3XhZyuuQNcDlCQjVDvD62ptM9MoOb839PzLe-FFt1SN3C_6DBHnjnv-78HabV0twBYQfdGaWHYRK7Lx-duM7m8tkJN9PyVvrSG2lUq0pvB0CJ-iJ9KW5cNz3xAbocra6ugxwzx2ddGRch-QTwkJpQ6Y29YWeBSMU4PqUR6-aiFPtwRzTstxQdia3fbILyVaL9rsc7QUAkh-M7xaQZ8yiQM8x9wr1FCxL7E9wCYIFwVn5oivUYGXLBXRjlF-bfxsjbLm1G4BY6r31Mm32_W92SWij_0VyqUkGs857Z_TbO2vJkwbI1Cj07fdA0GZU3ppm33c9xvwSjyHYjLclEPsoR4THKXI1eC5ps8DSERUnQWewzjylZE8PDOmaC3LRheOJSPJs1TD_PhShNaKnPBEzIXDD27m5joZMyfMmIv30FH4qDvojUiRKBQ7-TXftnOl71Wu_jlq0iDamVLAGMXuqZqf0CbXeZXUeEXCviqtlyQ6cOM7sX4umKROLbtg5wAS80Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام‌های ترامپ علیه ایران را چه کسی می‌نویسد؟
🔹
این زن مرموز ول‌کن ترامپ نیست، هرکجا که می‌رود این زن‌ هم دنبال ترامپ است. او شده همه کار ترامپ، تا حدی که در کاخ سفید هم به او حسودی می‌کنند!
ناتالی هارپ کیست؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/683535" target="_blank">📅 00:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
علی هاشم خبرنگار الجزیره: فرمانده ارتش پاکستان به ایران می‌آید
🔹
منابع بسیار مطلع به من گفته‌اند که انتظار می‌رود فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، طی یکی دو روز آینده بار دیگر به تهران سفر کند.
🔹
به گفته منابع من، هدف از این سفر فعال‌سازی مجدد میانجیگری میان آمریکا و ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683534" target="_blank">📅 00:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
الجزیره: آمریکا مدعی شده که هکرهای ایرانی ۳۱ ترابایت داده سرقت کردند
الجزیره:
🔹
وزارت دادگستری ۱۷ ایرانی را به انجام یک کارزار گسترده سرقت اطلاعات از طریق حملات سایبری متهم کرده است. این کمپین ۱۴۴ دانشگاه آمریکایی و ۱۷۸ دانشگاه خارجی، به همراه حداقل ۴۲ شرکت آمریکایی و ۱۱ شرکت خارجی و همچنین کارمندان حداقل ۵ سازمان دولتی آمریکایی را هدف قرار داد.
🔹
در جریان عملیات هک، هکرها بیش از ۳۱ ترابایت اطلاعات دانشگاهی و مالکیت معنوی را به سرقت بردند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683533" target="_blank">📅 00:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683531">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_A8fm2FZCHEADXHSYk9Hh-zDGsGh0mDfVyeo1hQrwSqIinr153EA5No34-PNea3mNFWQS7Kq6sHr7KlrZlO7QnqFVJj8DXnM-unqOgsZtpchZCMyaqFjWhIg6vWJtTE-ocq-Hq24IRHimw__hLzXB2GsIGjnrlbh4504HNHVG4umE0pBtI-j8aBA2VjH73T9iFn-pmg52Ar5J9nQ6iEUZ0yvcX-YzFRUc_3irUcr-h2qcPWu-88a1YPIntTJL1OYefPnuamkZZvhkixRgCibEXnT4o2vG3XwRgIrkSIkIR__sKUNbwlaUsbrLTT347mYvM6y1Rjy9bZNgI6WlFBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده جنگ
سرلشگر محسن رضایی دبیر شورای عالی امنیت ملی، شنبه شب در گفت‌وگویی تلویزیونی اظهار کرد:
🔹
اگر ترامپ بخواهد اقدامی علیه ایران انجام دهد، زلزله‌وار مقابله‌به‌مثل می‌کنیم، کشورهای منطقه نیز در صورت همراهی با جنگ اقتصادی آمریکا، با هدف قرار گرفتن منافعشان و توقف صادرات نفت از خلیج فارس و تنگه هرمز مواجه خواهند شد.
🔹
هشتصدوچهلمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/683531" target="_blank">📅 00:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683530">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63bd759edf.mp4?token=iOLh_xGFfrPNIYFZ8YhhhnRTQ5AGpnvC3RlOyMcD56FJazdmuPcKZvoOFJjMOOKTB6FrQdCr_23OEIKt4ahaHuLhX-U1XKtMSiEb0R5kYZc05LUEzjoezrjT0ye3OfV5BUvPOhZHE8ikNBp_VwIJpzAOfAcZEb3JN1M5OqaLt9cfpUxs1rnAtq9nmNLp5rt_rNEyY85OeEjUtuPYsH403PVjnpnlwQjRpvPUnKyYpDDFCuaB5hWTlBLX5D0VTDJn9Bbm9Cat9MvAU35FUqK90LODD73hqOM24zCeSZx0B4exen9UF75dDZFo5kF0kuWAEHkX6HUDlpBOj0AMcaoBrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63bd759edf.mp4?token=iOLh_xGFfrPNIYFZ8YhhhnRTQ5AGpnvC3RlOyMcD56FJazdmuPcKZvoOFJjMOOKTB6FrQdCr_23OEIKt4ahaHuLhX-U1XKtMSiEb0R5kYZc05LUEzjoezrjT0ye3OfV5BUvPOhZHE8ikNBp_VwIJpzAOfAcZEb3JN1M5OqaLt9cfpUxs1rnAtq9nmNLp5rt_rNEyY85OeEjUtuPYsH403PVjnpnlwQjRpvPUnKyYpDDFCuaB5hWTlBLX5D0VTDJn9Bbm9Cat9MvAU35FUqK90LODD73hqOM24zCeSZx0B4exen9UF75dDZFo5kF0kuWAEHkX6HUDlpBOj0AMcaoBrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: من با کیم جونگ اون کنار می‌آیم و این واقعیت که من با او کنار می‌آییم، چیز خوبی است، نه چیز بدی چون او ۵۷ سلاح هسته‌ای بسیار قدرتمند دارد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/683530" target="_blank">📅 00:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683528">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پزشکان عمومی به کار تزریق ژل و بوتاکس روی آورده‌اند!
حسینعلی شهریاری، رئیس کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
وضعیت دستمزد و پرداخت حقوق پزشکان بسیار پایین است و به همین دلیل پس از پایان دوره تعهدات‌قانونی، انگیزه‌ای برای ماندن در سیستم بهداشت و درمان ندارند.
🔹
تعداد زیادی از پزشکان عمومی برای داشتن درآمد قابل قبول، به‌جای انجام کارهای پزشکی به فعالیت‌های زیبایی مانند تزریق ژل، بوتاکس، سرم‌درمانی و مراکز ترک اعتیاد روی آورده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/683528" target="_blank">📅 00:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683526">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای المیادین به نقل از یک منبع ایرانی: ایران دعوتنامه‌ای برای پیوستن به «توافق مکه» دریافت کرده و این موضوع در حال بررسی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/683526" target="_blank">📅 00:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683525">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf737fe53.mp4?token=QK7Lv9DvCPhZrfMwuW3YrVr0ixmeTdL5UkOgFHVOE5VI_DVn6ekCK6s5-fqmxvK5oOW2oalG3pW9oFhi81Bx7jwcyOYZeDHdlIKXaECqJiwWk_CpsXpzNtkPdlnUzWCub1rH6Pi8sgu-HUWPj4DrACvt_8wdfKTQ_MGJI3IeUcPbqgM5XvSIBoCKrZv5wNkQVOycJzLSaVDAutjPqCOfRpUTmjZOGJfh8P_xDiqlbEIXP-bww6_3z3TglFGcrnH9AJuoqCYNyi5pJNH9ZUhLV0n5gbE8azUktSaMVJoLBGdO7QLFDPszCXIxY0iKK5-UGmcSnlji3DJuhRWWPbNFrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf737fe53.mp4?token=QK7Lv9DvCPhZrfMwuW3YrVr0ixmeTdL5UkOgFHVOE5VI_DVn6ekCK6s5-fqmxvK5oOW2oalG3pW9oFhi81Bx7jwcyOYZeDHdlIKXaECqJiwWk_CpsXpzNtkPdlnUzWCub1rH6Pi8sgu-HUWPj4DrACvt_8wdfKTQ_MGJI3IeUcPbqgM5XvSIBoCKrZv5wNkQVOycJzLSaVDAutjPqCOfRpUTmjZOGJfh8P_xDiqlbEIXP-bww6_3z3TglFGcrnH9AJuoqCYNyi5pJNH9ZUhLV0n5gbE8azUktSaMVJoLBGdO7QLFDPszCXIxY0iKK5-UGmcSnlji3DJuhRWWPbNFrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهدۀ سه قلاده پلنگ در جاجرم خراسان‌شمالی
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/683525" target="_blank">📅 00:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683524">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag6GVL8hudYbdJj51fJX57G7Tl4raULfxEARM-KlnYKmakYp2G3MturxlwICrsI9IynGxI1UplVSAAjmom6apV6k1eIX5oMg_mpcVOsXCdL353RBfYDV1jsrDiorjerKfJRxmg0rpvrhBMS2AsH9FcOgSwDIeHGc3VZaDqrlG9t5gMELqSnF2JlmIeIyCKWK36SEXBqvreMk_rzVEpXdTkfNcg5feax-1ieLCYtBSG_uXtSx20jHGcNHLwZC_yc5hQEfnI8RjLTpVmlHTEuIj1AKTYqY3YK1UdwwEmq0Ze4VX2BGzOYuSR_Y6NtIFMTlYAHjBrU5V3bXs7dmRAVakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/683524" target="_blank">📅 00:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683523">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6fb907f2.mp4?token=XGJNd56xXFNNJwG4LeSPAw6-7U8XeZudtjsS4Lw6_G4J0oC2Wm1YvUHeNG2R15kKewJzrzlNSKaxHmT3GuCistup-5Yb__-ot0ApKNzLdEcB-mVopCa7iT5eAWeWWVLBTCeQWCvR5rU1gumOeQukhRKVurcRfqNbn3u6fOzlTCgrJtAIpyBwhosk7tQPctA8OmkeeKKwhP84OfcoNtPOgcpeeX-dzKaHp5JWuCXTu83XtEHTynK-T6aG8jwNVQoi9xJoWSdiFDvyV0a-Y2I-HSrV5RXFm8DVibKXHSx1WonwHte4BNgg-ITMHOvooqKEPl062knWhfTBVlfQAJkVrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6fb907f2.mp4?token=XGJNd56xXFNNJwG4LeSPAw6-7U8XeZudtjsS4Lw6_G4J0oC2Wm1YvUHeNG2R15kKewJzrzlNSKaxHmT3GuCistup-5Yb__-ot0ApKNzLdEcB-mVopCa7iT5eAWeWWVLBTCeQWCvR5rU1gumOeQukhRKVurcRfqNbn3u6fOzlTCgrJtAIpyBwhosk7tQPctA8OmkeeKKwhP84OfcoNtPOgcpeeX-dzKaHp5JWuCXTu83XtEHTynK-T6aG8jwNVQoi9xJoWSdiFDvyV0a-Y2I-HSrV5RXFm8DVibKXHSx1WonwHte4BNgg-ITMHOvooqKEPl062knWhfTBVlfQAJkVrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاخص کل بورس سقف شکنی کرد!
شاخص بورس امروز با رشد ۱۰۸ هزار واحدی وارد کانال ۶ میلیون واحد شد.
۳۱ همت ارزش معاملات امروز بود و ورود پول حقیقی به بورس داشتیم.
به نظر شما این سقف شکنی شاخص ادامه دار خواهد بود یا مانند سال ۹۹ شاهد یک تله برای معامله گران خرد هستیم؟
@Titretejarat</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/683523" target="_blank">📅 23:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683522">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رائفی‌پور در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): محبت امام صادق(ع) به شیعیان، محبتی فراتر از تصور است؛ حضرت از شوق دیدار شیعیان سخن می‌گوید / تقوا و بندگی خدا، راه تقویت این محبت و رسیدن به محبت نجات‌بخش اهل‌بیت(ع) است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/683522" target="_blank">📅 23:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683521">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJYaTjw2UPb7P7kMha14VozbID93rp1ejTgryekwHqWunJjASf0gFr7IbaBSRG8-zVMtQkL25beMYw5-6Vg7IqsTammDL2kbomRk7rqVmicAMhY_bbvzXPFIryr6sQ6pUVcc0318vb-sQjv9oeK2sSd-9GROmGA9k7cKryv7h73EESWTuF9lFrtywFZVkzUGVnOz3U_6DU352RMd_aHZC_RrbzU__EsrODjlZmZPfCvhFJzMkoWBQmPCYEmtsKGRhDtd50V6Nt-GTnW3XHPNxQPVMqOIDePzhMXp1PEXMkqzdX9B2wlDn_CdgAbngtr8jbiXItkw5MHreOpCGSvAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله پیش‌دستانه، بهترین راهبرد در برابر فشار اقتصادی / ترامپ از جنگ می‌ترسد / محاصره دریایی اگر با مذاکره نشکست، شاید با جنگ بشکند
🔹
رسانه‌های آمریکایی می‌گویند، آمریکا روز دوشنبه تحریم‌های اقتصادی شدیدی را علیه ایران و شرکای تجاری‌اش اعمال خواهد کرد. در برابر این اقدام چه باید کرد؟
گزارش تحلیلی خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3239679</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/683521" target="_blank">📅 23:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683520">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsDo_yxJ99tQN_apCoXqOUGOFibgmnw-Z-WmJt2Ss6MtlMf8r78GJmkZvMx8__WFoMiV6gqTlpN3ZjxVzkdKxkyrtLpKRNjXdbZECyAgRpDuSYaOcNgW8CSq0h2ZWdVcEjYEbWLt9hI-lz38Eb539bDzhbv6bTy88RE86vhkwy_lIBfr0X6H8sAeN6RHnzeDd2VM8MJezYTyksi_33rgKVwfggFvSeCNBywMrG_KNResp4TMVnpXS_eJEdMxWhgtSvqlfVnu_p0UHLhsbEWJCY8krBBHNmfSSwTPTgNJYntoMnJpWtIQvwvC_EPe_LIoLmsGgWxDGzrt8ywiKuo4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرمای هوا شکست
🔹
از ۱۰ روز دیگر هوا خنک‌تر می‌شه و دیگه گرمای خاصی نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/683520" target="_blank">📅 23:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683519">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfP68qSZqftme1PzRxKOTY14scC8TvR07IQlQbvgYN4QFAGtIW72Ruu8Ectwk-1GwRIWStUO03HxPuLZ3VTdZ6n-20dMGTCCrkiCvVdJZhDIv_IVVjuRGDZLJ-TPFon6PxsUB8MX8LkaD-HbVrt48DdvmY3xVIUtDZco_TLhAF7f37QK8bZrQXhvm5Ln7sjaTKfyBaGL4Jr9hIl8do_-7xjJHT5uHZ41Ns-30hxmXvlAUF6RUd_XD8-t7xvTCqNIPA7NvxfclqiROIa5PN4sgjAfvTL1o8W5GNYPpftXaGPxfactRDLkostBiR_MwT5SCSp9UU2T04kINMha3QsOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز خشت‌گذاری ۱۰ اَبرمدرسه هوشمند در تهران
🔹
آیین خشت‌گذاری ساخت ۱۰ ابرمدرسه مدرن با معماری فاخر باحضور رئیس‌جمهور و شهردار تهران آغاز شد
🔹
این سوپرمدرسه‌ها در مناطق جنوبی پایتخت در زیربنای بیش از ۴۰۰ هزار مترمربع و با اعتباری بالغ بر ۱۵۰۰۰ میلیارد تومان ساخته می‌شود
🔹
معاون شهرسازی شهرداری تهران از تکمیل این مدارس در مناطق ۱۵، ۱۷، ۱۸، ۱۹، ۲۰، ۲۱ و ۲۲ پایتخت تا ۲ سال آینده خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/683519" target="_blank">📅 23:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683516">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
رائفی‌پور در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): برای حل مشکلات و طلب یاری، باید به امام زمان پناه برد و محبت به حضرت را در عمل نشان داد / اجتماع قلوب و وفاداری به عهد با امام زمان، شرط رسیدن به سعادت دیدار حضرت است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/683516" target="_blank">📅 23:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683515">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
قتل پدر، ترک مادر، مهاجرت و بی‌پناهی | اولین زن افغان که به کنگره آمریکا رسید | عایشه وهاب کیست؟
👇
khabarfoori.com/fa/tiny/news-3239557
🔹
منشا صدای شنیده شده در تهران مشخص شد
👇
khabarfoori.com/fa/tiny/news-3239423
🔹
برگزاری مجلل‌ترین عروسی در تهران | عروس و داماد چه کسانی‌اند؟ | عکس
👇
khabarfoori.com/fa/tiny/news-3239376
🔹
عکس جدید معشوقه کاخ سفید | ماجرای ناتالی هارپ عجیب‌تر شد
👇
khabarfoori.com/fa/tiny/news-3239596
🔹
قیمت خودروی محمدرضا گلزار چقدر است؟ | رژه میلیاردی از میان صفِ گوشت
👇
khabarfoori.com/fa/tiny/news-3239571
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/683515" target="_blank">📅 23:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683514">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
بلومبرگ: ایران راه‌های زیادی برای تلافیِ تحریم‌های آمریکا دارد
🔹
رسانه آمریکایی روز شنبه تأکید کرد که ایران در طول جنگ نشان داده که می‌تواند در برابر اقدامات نظامی و اقتصادی آمریکا مقاومت کند و به آن پاسخ دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/683514" target="_blank">📅 23:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683513">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
واشنگتن‌پست: ایران در پی یک غافلگیری اکتبری برای آمریکاست
ادعای واشنگتن‌پست:
🔹
تهران هنوز قدرت آتش‌بار و انگیزه کافی برای حمله پیش از انتخابات نوامبر را دارد.
ایران در حال برنامه‌ریزی برای یک غافلگیری اکتبری یا شگفتی‌سازی انتخاباتی‌ پیش از انتخابات میان‌دوره‌ای است.
🔹
یکی از دلایلی که ترامپ در ازسرگیری درگیری‌های بزرگ تردید داشته، نگرانی اعلامی او از این بوده که ایران ممکن است با پرتاب حملات به اهداف انرژی در عربستان، قطر و دیگر کشورهای حاشیه خلیج فارس تلافی کند.
🔹
این موضوع بخش زیادی از نفت آنها را از بازار جهانی خارج کرده و باعث یک رکود جهانی می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/683513" target="_blank">📅 23:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683512">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
رائفی‌پور در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): هر روز زمانی را به گفت‌وگو با امام زمان اختصاص دهید و محبت خود را به حضرت آشکار کنید / اشتیاق به امام زمان، یعنی با او حرف بزنیم و رابطه‌ای از جنس محبت و دلبستگی داشته باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/683512" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683511">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کلثوم اکبری هَستٍمه.....
بازخوانی پرونده ای که هنوز باز است
🔹
زنی که با ازدواج، سراغ مردان تنها و سالمند می‌رفت... و کمتر از چند ماه بعد، همسرش دیگر زنده نبود!
🔹
پرونده کلثوم اکبری، یکی از عجیب‌ترین پرونده‌های جنایی ایران، حالا وارد مرحله نهایی شده. حکم قصاص صادر شده، اما هنوز قطعی نیست./ خبرفوری
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/683511" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683510">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9b1dcca0.mp4?token=B-VCNWpHELTVLqNPJOEv4a1apRGB5dsjE3oiUQ2QIJSGMuuxvsdgehBnpnMMmfLJ0TMSS4wrGWwvAGiI-7H03pS53OSRj_5RWD9YuqIpCjz2c8o6vilm9J76GehDh6m6twFG1xXXsh0NsWC1inISiw2vp7CrHgRcsWqbFNCFtj4itH5yqZSrIiUBgJJO3Pp1WxH7TR7nyDBkdEFyOarFZ-8D2vyacZF0CoUmBQnepitl17j4SV-E9t8dYc5AcTHtZGcgyjEWfxA92xD-pBo3yr2pSAeP8-6CizDz7XBSeLdVFLxS3SliESLjig5PnMWRkLi9ImSD-RW7UOB_NXlL0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9b1dcca0.mp4?token=B-VCNWpHELTVLqNPJOEv4a1apRGB5dsjE3oiUQ2QIJSGMuuxvsdgehBnpnMMmfLJ0TMSS4wrGWwvAGiI-7H03pS53OSRj_5RWD9YuqIpCjz2c8o6vilm9J76GehDh6m6twFG1xXXsh0NsWC1inISiw2vp7CrHgRcsWqbFNCFtj4itH5yqZSrIiUBgJJO3Pp1WxH7TR7nyDBkdEFyOarFZ-8D2vyacZF0CoUmBQnepitl17j4SV-E9t8dYc5AcTHtZGcgyjEWfxA92xD-pBo3yr2pSAeP8-6CizDz7XBSeLdVFLxS3SliESLjig5PnMWRkLi9ImSD-RW7UOB_NXlL0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: پیمان دفاعی پاکستان، ترکیه و عربستان نشان‌دهندۀ این است که آمریکا به آن‌ها گفته می‌خواهد از منطقه برود
🔹
این دوستان ما گفته‌اند بیایید پیمان را تایید کنید، خُب ما وقتی نمی‌دانیم چه چیزی را امضا کرده‌اید چرا آن را تایید کنیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/683510" target="_blank">📅 23:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683509">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fbc4c891c.mp4?token=FhM-6vljI23LPecwedeIBHdlt5zNsHKmtrEEsxsaj1ajXvDHKac73yRe8Kmh9pZuJFN3Wy9_OKosdEHBAFAB6mgVfwSwk9Fyz3Y7cFs_VTDf65HHEWdj9f3TXRqHtavn4AsyoEREYwbpLbtw-t9MF02KRsvrmS9jzsywgPvBRNPFOeWN-Ewf_0-4Zl-3JcmBwoCmuDctVbdJnYv5ORsOjQ_Z-2NltLfBfFBLnpAkvrWtSkHyF6ZyqhrF6mkv7vLX60_YXLqEfLvIO7FLGyL6k81R70lyOBRu_wjT_IdnnnaMEINNheCnhOUNN9VEFdt2zRmvDNcry-9MqvJdABM0_4E2t5lZlBTCmaC7S3GEDJ1jlc3vtWLohvJdNbYXX9Qk1XNEmTbcFRjg4oFrWiwqYwcFjE1BP2eRKgd_jfw3MUYgL0Z5DiF0VBp9ZzK22d8P785C7UQLqSTzt-9FHMDjTaiOWb_UIW9PuC_5GtX-m9yt2vcR-4niuItPDb8khVQgG0fmyy1aXwNCXjq9ON6nzWV5X_-SbBpVyWybfBs6sWgPa9d9Tyu-McziTqiaj3pINpR2w9eZHTesVxkA9EjIf8VQ8a-sWnz2hNic0WudfVshLnjdYLAt5man98UsEHYpYZECfM57VDaf1AdJaZ1LcImDI90wZNeMw_NeAmseMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fbc4c891c.mp4?token=FhM-6vljI23LPecwedeIBHdlt5zNsHKmtrEEsxsaj1ajXvDHKac73yRe8Kmh9pZuJFN3Wy9_OKosdEHBAFAB6mgVfwSwk9Fyz3Y7cFs_VTDf65HHEWdj9f3TXRqHtavn4AsyoEREYwbpLbtw-t9MF02KRsvrmS9jzsywgPvBRNPFOeWN-Ewf_0-4Zl-3JcmBwoCmuDctVbdJnYv5ORsOjQ_Z-2NltLfBfFBLnpAkvrWtSkHyF6ZyqhrF6mkv7vLX60_YXLqEfLvIO7FLGyL6k81R70lyOBRu_wjT_IdnnnaMEINNheCnhOUNN9VEFdt2zRmvDNcry-9MqvJdABM0_4E2t5lZlBTCmaC7S3GEDJ1jlc3vtWLohvJdNbYXX9Qk1XNEmTbcFRjg4oFrWiwqYwcFjE1BP2eRKgd_jfw3MUYgL0Z5DiF0VBp9ZzK22d8P785C7UQLqSTzt-9FHMDjTaiOWb_UIW9PuC_5GtX-m9yt2vcR-4niuItPDb8khVQgG0fmyy1aXwNCXjq9ON6nzWV5X_-SbBpVyWybfBs6sWgPa9d9Tyu-McziTqiaj3pINpR2w9eZHTesVxkA9EjIf8VQ8a-sWnz2hNic0WudfVshLnjdYLAt5man98UsEHYpYZECfM57VDaf1AdJaZ1LcImDI90wZNeMw_NeAmseMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد شکنی شهروند روس با پرش از لایه‌های بالایی جَو
🔹
سرگئی بویتسوف، شهروند روس پیش از پرش و رکوردشکنی‌اش از بالون هوای گرم، پرچم کشورش را با افتخار به اهتزاز درآورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/683509" target="_blank">📅 23:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683504">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35b1e3ebd8.mp4?token=ZUFd0GxPGXOMZYT-7LS0LNPXiqN6neJ-CTjLV451_waHjnQZGcoTqWKrUJkwaCU4QuIm-WpHPPnPvr0ARaqaGaOr25kAo8p9cjmP-ClAV5MV7Ynvf2jr5huQGv0JL6u0iYBFfmMPU8UYkamGFBnImvMtEfoLOtJNtVsc3d3LXR4WumljO8xN-8vXRIOe7xCLViGEfzzMlw1ivYL5-EcW5NBZg5EaYfFDkopq6uhFgkpkxrh8uisn5LDThzboo8l276Vfvm5YJIIrb906Xr4V-JZCbN7UHrIsO_LbCGe1NFWUBgRydCZ6J44_zd8pkvLuVfTCkc4OXAkKyV5uGob8sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35b1e3ebd8.mp4?token=ZUFd0GxPGXOMZYT-7LS0LNPXiqN6neJ-CTjLV451_waHjnQZGcoTqWKrUJkwaCU4QuIm-WpHPPnPvr0ARaqaGaOr25kAo8p9cjmP-ClAV5MV7Ynvf2jr5huQGv0JL6u0iYBFfmMPU8UYkamGFBnImvMtEfoLOtJNtVsc3d3LXR4WumljO8xN-8vXRIOe7xCLViGEfzzMlw1ivYL5-EcW5NBZg5EaYfFDkopq6uhFgkpkxrh8uisn5LDThzboo8l276Vfvm5YJIIrb906Xr4V-JZCbN7UHrIsO_LbCGe1NFWUBgRydCZ6J44_zd8pkvLuVfTCkc4OXAkKyV5uGob8sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مبارزه ابرهواپیمای روسی با آتش‌سوزی‌ها در صربستان
🔹
رئیس‌جمهور روسیه هواپیمای غول‌پیکر و معروف EMERCOM Il-76 را برای کمک به صربستان در مبارزه با آتش‌سوزی‌ها فرستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/683504" target="_blank">📅 23:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683503">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c69RIpa9Ziwgp6A5Fyzcecq6Tl2Dv3fAkme8LYMhffq9kLu0UpW3zQCQodKRsai_Z-Ly_OgENlS1F0t0_qDQm7NcQBah-_Jce1-Pen9RDtTj4CKbLkzRrzvT1ADo_1Z0EJ_wvUs2KLIQLjwY9fznbzUMgxQYlSa-fEH_SrQJ6vRMCbSIVW1SjTU88PCvpr_igOR1JiSY6ZB2OiV7Or7t19CI3_daOPSnrqH4yEV6UcXq7DvG6tVVcPN1G57NdNvq-KVyD0xnKzq3VFNZ2S-NryTmUEbN_4PMvyyUDvM1xvNvAthoznLxEvkbUKwVlo06woHNn1thp0hkaSqMZ2hXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اندیشه و دانش؛ چراغ‌های راهِ جان
🔹
امام علی(ع) در حکمت ۵ نهج‌البلاغه، یادآوری می‌کند که «دانش»، میراثی ماندگار است، «آداب» نیکو، زیور همیشگی شخصیت انسان است و «تفکر»، آیینه‌ای شفاف که واقعیت‌ها را آن‌گونه که هستند به ما نشان می‌دهد.  #نهج_البلاغه_بخوانیم…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/683503" target="_blank">📅 23:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683502">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0c45907.mp4?token=HLAeKrmJKFR9Sd6hqKLcNXwdd_5tzYPHpIxLng-dxpFfmw5PR5Y7P3h-97VaykzVhY5zcjMg7inEkOqfsz6XGkmldR7foLNtlmEtbcq6psAvtZq003Qx6wTYn_NWmCyVKqjsJnqwV8q6gwXYMaFSwyG2t3YuiF48ZqOAm6cYIBSoLxlJ8HClk5VyNHjaNkr6O8UiRI-qcGXKdkLKlBJwwGTQasVVvHNXk2HK3sRV__9atWvZI8FLojVHk1Kn43wPtCG242KQoXbCvU7N1QSCW9cozhpwSfrYRTRFW4FA7rsSJsyGSP9QwOOcFjj6oPZJEP3GQZB3Eo9qvasAiIpbZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0c45907.mp4?token=HLAeKrmJKFR9Sd6hqKLcNXwdd_5tzYPHpIxLng-dxpFfmw5PR5Y7P3h-97VaykzVhY5zcjMg7inEkOqfsz6XGkmldR7foLNtlmEtbcq6psAvtZq003Qx6wTYn_NWmCyVKqjsJnqwV8q6gwXYMaFSwyG2t3YuiF48ZqOAm6cYIBSoLxlJ8HClk5VyNHjaNkr6O8UiRI-qcGXKdkLKlBJwwGTQasVVvHNXk2HK3sRV__9atWvZI8FLojVHk1Kn43wPtCG242KQoXbCvU7N1QSCW9cozhpwSfrYRTRFW4FA7rsSJsyGSP9QwOOcFjj6oPZJEP3GQZB3Eo9qvasAiIpbZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل بزرگترین مجتمع پالایش بنزین کشور اعلام کرد:
در بنزین تولیدی این پالایشگاه از ترکیب ۳ درصد متانول و بنزین استفاده می شود!
@Titretejarat</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/683502" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683501">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a780ac014.mp4?token=tbJQZZG10mGT-dmn8OlKbV7ATXL-Ow6jWhzaLPynAzPepW_mvbjXd506s19ArjjdVE-aXHTBFW4vfy7eR-R0Nm8y03RGoPjfRhCBjmCyupi_YR1ZKzrhjlxEdxIiQdnXOuBUPGOzs4cpxnUKvdaTUufStCXVgr5PIg8Dhx_5WaAAl8BobOIWw3v55brbPAokFbL4UUlzx8JIT_KP7ksLItjig6GoR-uM1qkrpyU7RWZG9hz0lPW-0VekrbVrC_AZjrLWhJh3KjxpsVKoa9lkJfZCnwxpWWCXGI4qt8aVFO_WoTaZ72LuJjcO8mOvQBttJvlI8CUcZZNNKobrwHFj2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a780ac014.mp4?token=tbJQZZG10mGT-dmn8OlKbV7ATXL-Ow6jWhzaLPynAzPepW_mvbjXd506s19ArjjdVE-aXHTBFW4vfy7eR-R0Nm8y03RGoPjfRhCBjmCyupi_YR1ZKzrhjlxEdxIiQdnXOuBUPGOzs4cpxnUKvdaTUufStCXVgr5PIg8Dhx_5WaAAl8BobOIWw3v55brbPAokFbL4UUlzx8JIT_KP7ksLItjig6GoR-uM1qkrpyU7RWZG9hz0lPW-0VekrbVrC_AZjrLWhJh3KjxpsVKoa9lkJfZCnwxpWWCXGI4qt8aVFO_WoTaZ72LuJjcO8mOvQBttJvlI8CUcZZNNKobrwHFj2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ما تاکنون به هیچکدام از منافع اقتصادی آمریکا حمله نکرده‌ایم
🔹
تاکنون ما فقط پایگاه‌های نظامی را هدف قرار داده‌ایم اما اگر قرار باشد جنگ اقتصادی را جلو ببرند آمادۀ هدف‌قراردادن همۀ شرکت‌های نفتی و اقتصادی آمریکا در منطقه هستیم.…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/683501" target="_blank">📅 22:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683500">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
اشک های الهام چرخنده وقتی که از مردم مبعوث شده می‌گفت
@Heyate_gharar</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/683500" target="_blank">📅 22:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683499">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: در صورت ادامه محاصره اقتصادی شرکت های اقتصادی آمریکا را در منطقه خواهیم زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/683499" target="_blank">📅 22:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683498">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
محسن رضایی: هر خانه میتواند یک لانچر جنگ اقتصادی باشد  دبیر شورای عالی امنیت ملی:
🔹
جوانان ایرانی وارد اقتصاد شوند. هر محله میتواند پایگاه موشکی جنگ اقتصادی باشد. #چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/683498" target="_blank">📅 22:52 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
