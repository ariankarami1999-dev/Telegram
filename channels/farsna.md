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
<img src="https://cdn4.telesco.pe/file/Gp3qmQy6DC_021UOMH26IRfSipgIgLWN7FYgSfbCq5M2Dx78dIXXYe3fE_LWgMkUTS2C0etB6YMRUfNa_ZAubv2ofnXIPCg1LRl3kGbQyoJXawEayspiS1FqUQnbmulePoIvaaP7MJr-1w_9Ohxd7q_kdmoD9QqymROvreta6cR_XOkATh2fpaDtZy83-u_iNZ7_CAH94akpM0bgEZ9gO_a3ejpmsLxZWDuyV3y3CEV-qvsiQ9jA3W_kbWBAncPnUzKbekGXkLTcXuZibti09wnzIm3OM68KrVAXsbUefAcz8QqD9uyNCW6Wtc1k3ZrcPiy05pMNijZsWpC18pACrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 11:35:11</div>
<hr>

<div class="tg-post" id="msg-453825">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e157b43618.mp4?token=L9syAPcSHHQYcIK3vAqAxrxxZ_vV50iqe6ivLRSSR3HMfDjY7PLgKIqqyWNEYm54HT6xC--3AqAN60-cjMbYCVLh6KZhN3aCgcXL6QkBGnaUkX2jd0k_JP3bO6XLJEoGocv54tjhazCz_OPTQNoH8PUrjnMwfrnWjBJlIGeB5dKxyiKzHaQLWrOSsZi0lDsohl63ZtgBcCy22N4Yg5mPGnISdRlr4Gys7py7dhwmICZu5wKZxAfqSzf-Dn8v-OKwVIL-FhBHMB6kyaHj8gDcQpGPSgxlLll9Tf8VOj90KuRcz0TjlDNMG6VaJdelyZC8vd69Hn_WTh9IFInufflWMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e157b43618.mp4?token=L9syAPcSHHQYcIK3vAqAxrxxZ_vV50iqe6ivLRSSR3HMfDjY7PLgKIqqyWNEYm54HT6xC--3AqAN60-cjMbYCVLh6KZhN3aCgcXL6QkBGnaUkX2jd0k_JP3bO6XLJEoGocv54tjhazCz_OPTQNoH8PUrjnMwfrnWjBJlIGeB5dKxyiKzHaQLWrOSsZi0lDsohl63ZtgBcCy22N4Yg5mPGnISdRlr4Gys7py7dhwmICZu5wKZxAfqSzf-Dn8v-OKwVIL-FhBHMB6kyaHj8gDcQpGPSgxlLll9Tf8VOj90KuRcz0TjlDNMG6VaJdelyZC8vd69Hn_WTh9IFInufflWMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: گرینلند تا ۲۰۲۹ مال ماست!
🔹
رئیس‌جمهور آمریکا که از بدو ورود به کاخ سفید به‌دنبال تصاحب مناطق مختلف جهان بوده، این‌بار گفته که گرینلند دانمارک را پیش‌از پایان دوران ریاست‌جمهوری‌اش تحت‌کنترل آمریکا درخواهد آورد.
🔹
ترامپ در یک مصاحبهٔ تلفنی گفت: «مردم گرینلند می‌خواهند کاری انجام شود؛ گرینلند از دیدگاه ما مهم است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/farsna/453825" target="_blank">📅 11:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453824">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
سرلشکر عبداللهی: هر کشوی با آمریکا همکاری کند، در آتش جنگ خواهد سوخت
🔹
فرمانده قرارگاه مرکزی خاتم‌الانبیا: آمریکا با شتابی فزاینده، مسیر آتش‌افروزی فراگیر در جنگ منطقه‌ای را دنبال می‌کند. این رویکرد، برآیند یک راهبرد خطرناک با هدف توسعه و سلطه نامشروع در کل منطقه است.
🔹
آمریکای جنایتکار در جنگ اخیر علیه ایران اسلامی ثابت نمود که در مسیر دستیابی به مقاصد و اهداف شیطانی خود، از هیچ‌گونه شرارت و ویرانگری علیه منافع و منابع مسلمانان پرهیز نمی‌کند.
🔹
کشورهای مسلمان منطقه باید بدانند که آمریکا با بهره‌گیری از سرمایه، ثروت، زیرساخت‌های حیاتی و منابع راهبردی آنان، به عنوان سپر دفاعی ارتش فرسوده خود و همزمان تقویت ماشین جنگی و امنیت رژیم کودک‌کش و تروریست صهیونیستی بهره می‌برد.
🔹
جمهوری اسلامی ایران و فرزندان شجاع و قهرمان ملت در نیروهای مسلح و جبهه مقاومت ثابت کرده‌اند که موازنه قدرت در منطقه دیگر از مختصات پیشین پیروی نمی‌کند و ناتوانی آمریکا در تحقق راهبردهای تجاوزکارانه و نامشروع علیه ایران اسلامی، باعث گردیده است که ارتش مضمحل آمریکا و رژیم جعلی صهیونیستی از پشت خاکریزهای کشورهای مسلمان، اقدام به جنگ، خون‌ریزی و شرارت نمایند و هزینه جنگ را بر دولت‌های منطقه تحمیل کنند.
🔹
به صراحت اعلام می‌گردد؛ کشورهای مسلمان بایستی با دوراندیشی، جنایات آمریکا را زیر نظر داشته باشند و در همکاری و همراهی با آمریکا تجدیدنظر نمایند؛ که در غیر این صورت، هر کشوری که خود را سپر دفاعی آمریکای جنایتکار و متجاوز قرار دهد، در آتش جنگ خواهد سوخت.
@Farsna</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/453824" target="_blank">📅 11:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453823">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkisrljDTbV7LH9CgWcyRSpv6yTIJTfk4AqjZQDQtoo6jj8Hgfl8Q6NH-CFU1ON10kV9Kau63is4zW-D0xclLZ6EugmVy10TMHP3GgZCmORNy8m7vrhOom351OTNG3BnZJFBNiUvqD5EPuadnKDX5rSffXZ1wnSFhS8m8kmZfcW2jwVdDaWi1hhDGEvI0ybzB7TXe2-u6kOWExcRqrziSo-FtKtKF8KZe06xZHWkYkdCd7-rdvwTsQ2rPm5JQmhoVyeWqw27Ei2o0yamez2M4k7OIJEy3f_gYNNFLoPgyCepHE_1jimkIpwY1WpQ1ToDzCUgsKwWBjD1bSgjc_YHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوفا، فیفا را تحریم کرد
🔹
اتحادیۀ فوتبال اروپا و ۵۵ عضو آن در واکنش به پیشنهاد فروش سهام فیفا به سرمایه‌گذاران خصوصی، بیانیه‌ای منتشر کردند و اعلام کردند که در صورت انجام این‌کار در مسابقات جام جهانی ٢٠٣٠ شرکت نخواهند کرد.  @Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/453823" target="_blank">📅 11:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453822">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DscUc3M208KqxRDZ8C6CpW176_Q-Mg8z1BEBDkmlmKFv6T-wl6OKghGDmB8VJZzH9Rep8GE-eIuOsM3G0h4fC9KDu5rA8MB0EqPTvohM0-PQN3vVm71aOWDuGgTNmk1BhnQD0VdDq5zoeuMKONPKyW6o4EBi62mktWa6RxSwf5poL4ZY2BGIyKpXwj7McpSjqSEqgqfcpXa0uSGyHPMR2Y3_p2NDkjRx9qmYvNe09LLv7XVCoiUn6KEo1rabVdA-NWZtC8KwBgOS2yVuvNkNm_PsDMbG0RlKZhq-ZxUYQUwYQ_P07_63hcMhT1bIovvu27lTWwCCEOVi0PMTBmadMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ بازی خاطره‌انگیز آتاری، فیلم می‌شوند
🔹
ددلاین، از معتبرترین رسانه‌های تخصصی صنعت سرگرمی در آمریکا، گزارش داده که شرکت آتاری در همکاری با Entertainment 360، قراردادی با یونیورسال پیکچرز امضا کرده که در آن، این استودیو حق توسعهٔ سینمایی ۱۰ بازی کلاسیک آتاری را در قالب فیلم‌های سینمایی اکشن و ماجراجویانه دریافت می‌کند.
🔹
فیلمنامهٔ این پروژه را «مت رایلی» و «کارل همپه» نوشته‌اند و هر دو علاوه بر نویسندگی، در مقام تهیه‌کننده نیز حضور دارند.
🔹
وید روزن، رئیس هیئت‌مدیره و مدیرعامل آتاری، با تأیید این خبر گفت «بیش از ۵ دهه است که آتاری بازی‌ها و دنیاهایی خلق کرده که مدت‌ها پس‌از انتشار اولیه همچنان بخشی از فرهنگ عامه باقی مانده‌اند. از همکاری با یونیورسال و Entertainment 360 برای انتقال روح برند و بازی‌های نمادین آتاری به رسانه‌ای جدید هیجان‌زده هستیم.»
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/453822" target="_blank">📅 10:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453821">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440afe73b7.mp4?token=uNVZazudwGHRKs5ToCADE-zt2dmIOIH2xAgllMTjEyKt7Cju6EmqPpsR8YvPtJibLo4tbIWeaPPu0S9PptMCzxZGBmaQbbCobN-_NiEl5JPQiP3yBU6FHFeVuiPYaqiJiZtVmgDwEpYS5C47L0UoFrb58-ftRySiYrbr7jFRuSJs442LVfeZSRhWBkN9Arm-muuRv6P9vwCgc6KaXc-PsZTbFu5eGSYC6Fa9glhidhI6r-dI_yEqidGVCtMwNcdOXukxi1cOLX3xRkjUrUmjbts4boYoMpkX6iVrISHIQ7ZEKapFV5EzT5rOD6rwIsdFi0P0TG8vbXBRlD8jS0N-ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440afe73b7.mp4?token=uNVZazudwGHRKs5ToCADE-zt2dmIOIH2xAgllMTjEyKt7Cju6EmqPpsR8YvPtJibLo4tbIWeaPPu0S9PptMCzxZGBmaQbbCobN-_NiEl5JPQiP3yBU6FHFeVuiPYaqiJiZtVmgDwEpYS5C47L0UoFrb58-ftRySiYrbr7jFRuSJs442LVfeZSRhWBkN9Arm-muuRv6P9vwCgc6KaXc-PsZTbFu5eGSYC6Fa9glhidhI6r-dI_yEqidGVCtMwNcdOXukxi1cOLX3xRkjUrUmjbts4boYoMpkX6iVrISHIQ7ZEKapFV5EzT5rOD6rwIsdFi0P0TG8vbXBRlD8jS0N-ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت قالیباف از چگونگی شکل‌گیری میدانی به‌نام خیابان در جنگ تحمیلی سوم  @Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/453821" target="_blank">📅 10:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453820">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656e493994.mp4?token=cRu8iqsc_NFr3Lu2BCh-6bxhDnmtLZUrtFi8N2DnNt2REmrzcdyo1oDtdEneVUUThHQR2AHmGBuMjO3wUOzNPyWO96AxIDni_auF_dpVWN0ZHDA3xuVWpkOBtb4hXr2_vYfEDjFfWKK6NPYxbRsgGuHgtf3T8RUQGMjZ_LX7rxwUSbZxaZgUEuTW8GK10Oput2k-nWlScABx-JblZYf8vYd1pGRrblN0tvUb-R1ffxCdGETJZvgBm0eRtkAEycDWae59vc1B6maX1fqABw0K47qn07lsK1IIxtsiySmKVO2X8LMiqBvEO1FFo9Cj4wvpsZ-fUzb3t01ThG2-FLGmaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656e493994.mp4?token=cRu8iqsc_NFr3Lu2BCh-6bxhDnmtLZUrtFi8N2DnNt2REmrzcdyo1oDtdEneVUUThHQR2AHmGBuMjO3wUOzNPyWO96AxIDni_auF_dpVWN0ZHDA3xuVWpkOBtb4hXr2_vYfEDjFfWKK6NPYxbRsgGuHgtf3T8RUQGMjZ_LX7rxwUSbZxaZgUEuTW8GK10Oput2k-nWlScABx-JblZYf8vYd1pGRrblN0tvUb-R1ffxCdGETJZvgBm0eRtkAEycDWae59vc1B6maX1fqABw0K47qn07lsK1IIxtsiySmKVO2X8LMiqBvEO1FFo9Cj4wvpsZ-fUzb3t01ThG2-FLGmaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: سرنوشت ۳ خلبان حاضر در عملیات ۱۱ اسفند ارتش هنوز مشخص نیست
🔹
پیگیری‌های ما ادامه دارد. طرف قطری اظهار بی‌اطلاعی کرده؛ از ارتش و دولت قطر می‌خواهیم که با مسئولیت‌پذیری بهتر برابر با کنوانسیون‌های بین‌المللی اقدام کنند. @Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/453820" target="_blank">📅 10:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453819">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=X9QGQjF42dlKbWDALadFwn5oyEXNr9c4Sf7CwHITZ-HPjT90iG_AQ3WuvfXY94JF65WxxWBCeOVo14EyalOFD_Flmbe3yfYxRskuHeAKiHPHhWs-itawpu-3-ghwBP1FxbcmxhMv_pEFznwbanGv3JqkWEbqay7pVMZhIV0mMh3f65m3suF1SuXPZxWH-BIByvKVekEgUw7IJRVZrXj9RUv2qP4yC6AbSZeBxNX8B8Oeb-nXpmoyOB4QsMWRpg9FCZE30Gj1R5D_ZaafyPRDTujScqs_iDpF7tsZK3qK_ENDE_tQc1fxZchJdRXIKJ9dxiCC0Qkru1Jjcw-7ZRhztQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=X9QGQjF42dlKbWDALadFwn5oyEXNr9c4Sf7CwHITZ-HPjT90iG_AQ3WuvfXY94JF65WxxWBCeOVo14EyalOFD_Flmbe3yfYxRskuHeAKiHPHhWs-itawpu-3-ghwBP1FxbcmxhMv_pEFznwbanGv3JqkWEbqay7pVMZhIV0mMh3f65m3suF1SuXPZxWH-BIByvKVekEgUw7IJRVZrXj9RUv2qP4yC6AbSZeBxNX8B8Oeb-nXpmoyOB4QsMWRpg9FCZE30Gj1R5D_ZaafyPRDTujScqs_iDpF7tsZK3qK_ENDE_tQc1fxZchJdRXIKJ9dxiCC0Qkru1Jjcw-7ZRhztQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ خلبان سوخو ۲۴ ارتش چگونه پایگاه العدید آمریکا را به آتش کشیدند؟
🔹
۱۱ اسفند سال گذشته، ۲ فروند بمب‌افکن سوخو ۲۴ نیروی هوایی ارتش ایران، در پاسخ به حملات ارتش آمریکا و رژیم صهیونی، در عملیاتی از پایگاه هوایی شهید دوران شیراز برخاستند و پس از عبور از سد سامانه‌های…</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/453819" target="_blank">📅 10:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453817">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-jmEXHeiY_ch88t2fPHEEsLXocfnZyYDc0b1wuV8Xe2vMhda6TRAAcf5oWhC0sOMHw_UZhSuPCKOjyr0u45WA1qYaIJofVryV-AsDMdS-eHSzo7eeMno2g9ag1fVKrMGUlui920vKpZnktLUcfyrY-Upm4RVfr8aBLgqBvpd8R64Pfvl1iPnneKOq2p4q67znWRSEgXsBrwJxDz9qvX7mYfWjP5snzAHNUGIbBSNH-v6Y9CkwgI7UhW-cIopETR7jj6nW1ENjhXvZfen-RDDnkthF1EdvrJlGptqA68DhSLSNnPLwoOklVyvD5SW0bM74ILgmeJPjc7l2kjz_kG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار افغانستان در تسخیر کالاهای ایرانی
🔹
بانک جهانی اعلام کرد در پی اختلال در مسیر تجاری پاکستان، تجارت افغانستان به‌طور قابل توجهی به‌سمت ایران و کشورهای آسیای مرکزی تغییر مسیر داده است.
🔹
براساس گزارش بانک جهانی، ۴۸ درصد از واردات افغانستان از طریق کریدورهای آسیای مرکزی و ۴۶ درصد از مسیر ایران انجام شده، درحالی که سهم مسیر پاکستان از واردات این کشور تقریباً به صفر رسیده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/453817" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453816">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
ارتش کویت از درگیری پدافند با پهپادهای «متخاصم» خبر داد
🔹
ستادکل ارتش کویت اعلام کرد که سامانه‌های پدافندی این کشور در حال مقابله با «پهپادهای متخاصم» هستند.
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/453816" target="_blank">📅 10:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453814">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8jYkhZQiK3yfoVVsGti5GpV5zngG2iy3NW6by0E3gdUVGCh-qEi-0jNqXZErobBN9FZQ4tKgR-j2MdPf_PF7-UhvsSicp1aCEEz9bb7di2JW30ejWcjybCxo4dyZ4ZEzvOmMB8SE0CWkqwH1DzqpL82B_mjqXDz_b_5slo9uopOTqwnyiUrRMyZk9A5aRR8EK9c1MeCdZ4aUO_T40YmTgLcFwz6kgWeX60hYOzzxlYRqOtElM4QHUb6fZJ3jPlfqGP-JdzwzXGC_LF_0VUiS4xFixv3USFR-VwgLu0nToXOLaPb9biyslTUKZDiezM5QIp8EkETsEKqr2HT12QqwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شهید مصباح‌الهدی در کنار رهبر شهید انقلاب
🔹
این عکس متعلق به آرشیو شخصی خانم سیده هدی حسینی خامنه‌ای است.
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/453814" target="_blank">📅 09:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453813">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oROnfMLAFzKjJJ66pJixdkQjjpu3dQjFoGXrrw63TiYtJNwR1XQLt15h6gcn2SmzlcAL54Z8H9ZQGnl9t11lzuD0EfehjztZ5PGYSmCm59p00GXj6K8iv6hEzf4gwCErib5PouDcX9XlhMkoa4olKj2wpHsXUxzbuY1ytLigB3LVWMUgRBgtSnrjvkzng6jETX_gwB01np67sixxJTLNsTV0yhr8B_dlqxzaYeFZbmzgUGx1qlgRnnJqowhwzLmPNwPiASenjPb0zucSxf66w-siGmxJil2QfBrm_CKUHufdbHAbI-ZiCVPzOXxkWPCdT2EMVt4pepV0AuZ_xmA_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تراژدی در ارتفاع ۸ هزار متری پاکستان
🔹
یک بهمن سهمگین در ارتفاعات برودپیک پاکستان، یکی از تلخ‌ترین حوادث سال‌های اخیر دنیای کوهنوردی را رقم زد؛ جایی که یک تیم بین‌المللی ۱۰ نفره در ارتفاعات این قله ۸ هزارمتری گرفتار شد و سرنوشت چندین کوهنورد همچنان در هاله‌ای از ابهام قرار دارد.
🔹
در میان افراد این تیم، نام نیرمال «نیـمس» پورجا، اسطوره نپالی کوهنوردی جهان و رکورددار صعود سریع به ۱۴ قله بالای ۸ هزار متر، بیش از همه توجه‌ها را به خود جلب کرده است.
🔹
برودپیک با ارتفاع حدود ۸۰۵۱ متر، دوازدهمین کوه بلند جهان و یکی از دشوارترین قله‌ها محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/453813" target="_blank">📅 09:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453812">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK_NxCotUJ_Rk7Q8SK1XbuBipN5TohrMyydLmWIWGC_MRQPIQAfzJ4j6l5SogpvtTwSioRCfWPjoK7fjRAhToGxu-bhHCOAaRgaykESAovOJZHRStfMipo2ZOCn_f3rYULICWc6gPJOmbd6KB8mLsssaGYxDFpY5TP4mOQyRTzgZant7bmZeZ3ZRWnGR7pPjIwYDlJYm781v937ShpJsnhyG80XORVVwKc8uJd2oJfFWbxhP6vdRxvBs0-dmQCpPz4vmwrViL2_2Ysx9glGb2vFq8rQvGxoAbEdKlSg8nLWt4CRhdBbI6NX_4stNxtOsD3vJZWuIGXmVZT0GGA9Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متروباس ۳۰۰ نفره به تهران رسید
🔹
شهردار تهران امروز با اشاره به خرید متروباس برای خط آزادی-تهرانپارس گفت: تاکنون ۵۰ دستگاه از این اتوبوس‌ها وارد کشور شده و روند تکمیل ناوگان ادامه خواهد داشت.
🔸
متروباس که در واقع نسل جدید اتوبوس‌های تندرو (BRT) است، به‌دلیل…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/453812" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453811">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ثبت‌نام کنکور ارشد علوم پزشکی به تعویق افتاد
🔹
ثبت‌نام آزمون کارشناسی ارشد رشته‌های علوم پزشکی که قرار بود از امروز آغاز شود، به‌دلیل مشکلات فنی حداکثر یک هفته به تعویق افتاد و زمان جدید آن متعاقباً از سوی وزارت بهداشت اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/453811" target="_blank">📅 09:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453810">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1732ea92f.mp4?token=ScifpMjbFkVjaKkn7lPnr0SnhAlEpg4H634Qzmn_-E46C7Uwcki1sFHpx1hTcuVDJ3QtHTAmTAU0aIHq3G0RXUiwIgH5I0jX6I9rTYZB13ag3U2pScrid-61tOdufGw-4Vc5CXPjm1QZzl0xFKOGemvAJAUUmxndS8vIHLxKPvxR7ye9W7Qnc17ZDUUsQ3LLwgOTtTpujSXoDV-6JncR7uCKttF7ESh89Xzr0KM-AqhyCcq_W4rUUg_ozHLS7Fp0HYGtQ5m2mdkIM7Qu3-uaSD71N7S2sVWscpS75IujlwRUlXKAFaCihrN9Lvw72OHPIX-ywAScPDQEsnX0eqyewgtrlyuYYW6P33xHghRDQvNduRkaX6wOH9rPDaDsh9cAQa6-e_7EzVRCpO6SwplKy7qIO-u6IF9BDvJCxl4VL6Yd1yKr9FmI8_xLbIL3G7K_0j1rcYttkW804GERF03m9CA1CbV2XTN6cSHQ3693nEiDtVDGgmGy1SMRGhbczdX2lDeh34AoxkAFrkcNewLHmhz3OgVVAWVbEogz7WQshwZbQzkgdHwYe1ab_bCaoQNMAEu2xTvu7LNKlTQYwK_kYYMX_3Rm5Z-lKAAt1cNUqnxYBbu_ZB5sk7xHxhoLI4_e5v65kBVJMy93hhlZbL4OF3YsaIryi5WZfnX_eIlLTN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1732ea92f.mp4?token=ScifpMjbFkVjaKkn7lPnr0SnhAlEpg4H634Qzmn_-E46C7Uwcki1sFHpx1hTcuVDJ3QtHTAmTAU0aIHq3G0RXUiwIgH5I0jX6I9rTYZB13ag3U2pScrid-61tOdufGw-4Vc5CXPjm1QZzl0xFKOGemvAJAUUmxndS8vIHLxKPvxR7ye9W7Qnc17ZDUUsQ3LLwgOTtTpujSXoDV-6JncR7uCKttF7ESh89Xzr0KM-AqhyCcq_W4rUUg_ozHLS7Fp0HYGtQ5m2mdkIM7Qu3-uaSD71N7S2sVWscpS75IujlwRUlXKAFaCihrN9Lvw72OHPIX-ywAScPDQEsnX0eqyewgtrlyuYYW6P33xHghRDQvNduRkaX6wOH9rPDaDsh9cAQa6-e_7EzVRCpO6SwplKy7qIO-u6IF9BDvJCxl4VL6Yd1yKr9FmI8_xLbIL3G7K_0j1rcYttkW804GERF03m9CA1CbV2XTN6cSHQ3693nEiDtVDGgmGy1SMRGhbczdX2lDeh34AoxkAFrkcNewLHmhz3OgVVAWVbEogz7WQshwZbQzkgdHwYe1ab_bCaoQNMAEu2xTvu7LNKlTQYwK_kYYMX_3Rm5Z-lKAAt1cNUqnxYBbu_ZB5sk7xHxhoLI4_e5v65kBVJMy93hhlZbL4OF3YsaIryi5WZfnX_eIlLTN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: شرط ایران قوی وحدت حول محور ولایت است
🔹
در دورۀ سوم انقلاب، قوی شدن ایران موضوع اول است، بعد از شهادت سردار سلیمانی، امام شهید ما متمرکز بر ایران قوی بودند و به آن تأکید داشتند. در گام دوم انقلاب باید متمرکز بر این قوی شدن باشیم که یک شرط آن وحدت…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/453810" target="_blank">📅 09:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453809">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a503cf789.mp4?token=EZclU0wJLV8_FmVaUuXlZx4ZwN0f3tqf1kEEQOPf52LF716qgtu6Re0B-9MdSO5-aBmRayUg_DbPD3NWtIi9H0jqDo_TNmzC01ocJxyH_pAZ838GTR1W6UfWsB-ZFLQx3hQHkM9ahpXAEt3hzQ3_2-xux2wbjiWrQMi-yjABSQlOMElOn1UMBz5HF2ctk2lv9gqYX4DaKbbZluHXBuf5Ilfv8qaqblUvVrC5RWHNJQQV9huMyKQvTQ1XPH9fvM0TerJXvymL5ykK5m9WpM5e5UYldg5kkcnDVo1EnGsYNXgRiVDvtF2XbdYZ2MrtcyVMLHHdkVCb4ejwfvn4yfkuJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a503cf789.mp4?token=EZclU0wJLV8_FmVaUuXlZx4ZwN0f3tqf1kEEQOPf52LF716qgtu6Re0B-9MdSO5-aBmRayUg_DbPD3NWtIi9H0jqDo_TNmzC01ocJxyH_pAZ838GTR1W6UfWsB-ZFLQx3hQHkM9ahpXAEt3hzQ3_2-xux2wbjiWrQMi-yjABSQlOMElOn1UMBz5HF2ctk2lv9gqYX4DaKbbZluHXBuf5Ilfv8qaqblUvVrC5RWHNJQQV9huMyKQvTQ1XPH9fvM0TerJXvymL5ykK5m9WpM5e5UYldg5kkcnDVo1EnGsYNXgRiVDvtF2XbdYZ2MrtcyVMLHHdkVCb4ejwfvn4yfkuJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف:
شرط ایران قوی وحدت حول محور ولایت است
🔹
در دورۀ سوم انقلاب، قوی شدن ایران موضوع اول است، بعد از شهادت سردار سلیمانی، امام شهید ما متمرکز بر ایران قوی بودند و به آن تأکید داشتند. در گام دوم انقلاب باید متمرکز بر این قوی شدن باشیم که یک شرط آن وحدت حول محور ولایت است.
🔹
ما مسئولان در درجۀ اول باید بسط ید برای ولایت فقیه ایجاد کنیم اگر می‌خواهیم ایران قوی داشته باشیم باید از این نقطه شروع شود.
🔹
ما جنگ را پیروز شدیم ولی باید پیروزی را تثبیت و ثبت کنیم و حتما کشور هم باید امید به آینده داشته باشد و چشم‌انداز آینده آن روشن باشد.
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/453809" target="_blank">📅 09:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453802">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0ppQ2TlZxwl9RZjXH1xY9zfa6dPuOzkIRKEoYxlMNGTyb8TINimePZ-rLJMDFY7DB4Dc-pKZac0TEjXEicsNBKrJKQEqZSNb_W2d5xLQpdC95M4B_FiHt5dmc2riI_eKCHX53VWmjNEdi0ajNDl77GdDjOx2qcHhRWmNapc5nBrH8CODNmrDEFx36mC7mLsNTMIqkP2cOBPAp00Pt1D2cdT-snhhr8NX9EluHt_ZnPEaUoUFV3Xey7PdAg6uA7tYa_pVgKWxqK22ipJ6mXKircqXPSQJCQLfdVsxrFV7QbrQHGoVeMGaamWvxPQN-Vu4Phque-zlijlazC1QQlfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1sVAzR3sV1oI7krFljcBvutjjgVDooxOJSFGd1aZxKSv77aTT7nFNNHVAxSwaQNkjuPL_dy-pXse0FWGy1tbz_eLEK7hm51WX_wWCI7QBK0j5pDzNCI4GKWLP5j4NrBiUh5_rbg_pafBtqC4eCughNQY50Vs77MeMotbOUDVAcojeW_4OSoccwjwcU6L7ByZTeoLcJqFz-8t2Lslmvs7xhhYZ22Hh_lNnl_zW3-7ZrgoJHhbnSJa8htNZxDifpL_TrFZ614ytRlyeZKvJJqQ3t2GbMP2gmagxyjP46rPad7gXNYiE6eReZIyTFRWgIPOrG1mL43VZVRdgFIvrrppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3GYH3rVtzOmY1p4ASR7LmsWufa-Vsl5ODnTm-cnMGi_VYepOveIFWu9D-nPjVyIpSIDA6lOFCEtN1YF2assPWtSgco8D6SvGRMUj17Zy3QFr0EWRA18glRbvIFDNk4BgO7zjlQ--IjECAl6bc-ayBbUUKn76jkrmIeO6G_58EdAsmXYUqDTEfP3jLUYPeL7ObVzHBfAk8QK-u6quRO3iVCLWy9gpjKULg4fI8mltgfN-y8Y56M5fAN-uuOAlp13l28Kpmo3i80OHiza6VY_3AEtxkpi1FbtKQh9sN5o7QsGqNQ2jbKBLlw6wG6od8ZNMhAoJZ1twbQ-LyomMMkC6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xq4hTXl-HkW9jzA9gu9E7HdLmslIMK_sDO3L8Z2KJWkDhMcZICdQHFytzHSqwZNdR1PWloKreUseBp-nt2EldxW1P5oFex4xZNjmCRBPZImk_tImttKjyb9aBTg8SAWY_sHKtcwJiEwK5gAPY9a4G6-1IwtF-tWtLgkTnuLmGeIN2GEKwJEYpbwTIDuJwCy7QFKtycrjb6SQNdVQCg-RbL6qyWqrcxXQ9UAcpZrLw40bAtYsnzUyGPA0WOWBjO9J4Qde5BNdAUD39hV0PFg_r3J1Pihn1tVerB-a17gUc_iR5SknQiDxqvD271FbxP3g8CZqGONi6ITmUwf0cDVP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7m2dcwuMrDEcQRs0uDCjL54T1gErBo5voRjcIgFQ3mY3e-HDUWhH0gBRRF6vN9Vx6BFMr1V64_nxUb8pzciWIo39E6rPazHbbm327rlwoFBe1g2k1wUa6tDwlFVUOxi2DnPi1WSwEfpROV298CtZhDsvIUn7Rloqr9EsG2zPgKGtiXAx6C8LZTuDqOzn77eT4LGKN9r9pZZ-zoS3LXPGYv9d-A9wRGvBt5Y5NpYdDh0NkOo6eSmIfOJ-vW0_1aY6ucYWxLqvHS4fZ_2QEaQI9RHBZWl3FI5PETscWR30cXil24IAImRBDuUV53YefXP53edxnSllJ1_mACqikYFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvBO8-TZx39tyj8ODFGTVIcWCxnobM3Q9rOPJfgau8kz3FeIFGmdQLIF4ld5l4bm3ZGN89psbmiFjGfotYANbVd8x4gqAFX156P8SXq_14332GB_j_z6ns7nz1wGaGAITY0ri8wAvH2jcV4TC8tGUXzugQPzzVWBFCE2ys9eTmALWB8F2aRGFAm0qBq8qOlSHu-LhhU_aeAPSCuBE_A3r41Y9sm0cnkMUgRHICqGGS4hPeWoB2CpPOAJyIZVfND-TJAhWNZlKVc_1ivgeXcfHEB4lqJ_5M2X1xvkVOD1g0JwE-h0c-A3qBd_kFGaLZ7G-_dSY0qx8KBtYIrc6MWRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWeXtnyQTiJ2-2InJgMaMiiR79hnjK-zlMMrTr1qfBA9Ypvt5TmLTacjh5MGpSTKWgvR-S91sZBIa4DwoiFKf7Gq81DNfowu9rZO9TXv10DcS0RnBeyv8qdLwM-ejVOwN1hPxpsLR_uOeWNXjVaGg32E5YxRbqmH-pfnFL-v2ICR90jrVgz_Sb6hZ6k2yEEepgDi_8kFBUyvY2LfqmKD-Uo32NZZfxf69cSZBVQiG-sy5Oq3x2DBuwz5rGlh7KCyHb1h4SNBM-1MxwpnWFqa1bVNvR3SQZGfVHNHaIkZ2PYBsQjjjOlXEyVIdlwQl304K_duYI9x61wxOLfZpMLtSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طریق‌الحسین با یاد و خون‌خواهی رهبر شهید
عکس: مهدی ایمانی
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/453802" target="_blank">📅 08:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453801">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/605ec7287f.mp4?token=M-c0oeDTlYalRKBCRIZMfAuiZMXPO1sDmJ3Suhmf72G-CzFGpBS3Q_6Wtp8InmSBiXhs9hU9wlyJTCXSgnVH0hXBwKa51tnVLSHKnr0dt9D1nrpgVseJJkhxjaDirsx8_7m_BhMj7Gzuexq2kemrvpt3jFc0yaiel5hcTRBV_UYJWVcm5DT6AJntAZFYClyfaT-12uHxMp1lDlXttSgKpTWsDRubTUPj7gJi9xCAfMCt_dPMvXxlEHc62womwdqeF_qwNK03Lvh_SyeXvx7FY1Z3TD5R3aNZj2KavBLkgeiSnp0AUVXGinTY7FLRTeGkL1TQCzpb3D72Ik6FjhIwUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/605ec7287f.mp4?token=M-c0oeDTlYalRKBCRIZMfAuiZMXPO1sDmJ3Suhmf72G-CzFGpBS3Q_6Wtp8InmSBiXhs9hU9wlyJTCXSgnVH0hXBwKa51tnVLSHKnr0dt9D1nrpgVseJJkhxjaDirsx8_7m_BhMj7Gzuexq2kemrvpt3jFc0yaiel5hcTRBV_UYJWVcm5DT6AJntAZFYClyfaT-12uHxMp1lDlXttSgKpTWsDRubTUPj7gJi9xCAfMCt_dPMvXxlEHc62womwdqeF_qwNK03Lvh_SyeXvx7FY1Z3TD5R3aNZj2KavBLkgeiSnp0AUVXGinTY7FLRTeGkL1TQCzpb3D72Ik6FjhIwUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اَبَرپرچم باید برخاست در مسیر عاشقی
🔹
هنرمند اراکی با خلق اَبَرپرچمی با عنوان باید برخاست روایت تازه‌ای از عاشورا و خون‌خواهی را راهی مسیر اربعین کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/453801" target="_blank">📅 08:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453800">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اعزام رایگان زائران‌ تهرانی به مرز ‌مهران، از امروز
🔹
شهرداری تهران: از ساعت ۱۶ امروز، ۶۰ دستگاه ون زائران اربعین را به‌صورت رایگان از میدان آزادی به مرز مهران منتقل می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453800" target="_blank">📅 07:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453799">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">منابع خبری از وقوع انفجارهای شدید در کی‌یف پایتخت اوکراین، خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453799" target="_blank">📅 07:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453798">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199ab599f9.mp4?token=qQTAUiJ8fcUqcTkt_tZuFH_kWc8H-ZCFo-CvZT9XXdXDynOhnSJkrGCJNhkZ7iSA6gwE18ArOK8o254TWlgSWJ0WE_w4GJhN5q-xbSpuVZ-2rbJFFqjO64666v_d3hOghz1L1JOUpLZB0tqOXgbpXIIlvW7crSxT-qKZ3lR_T5QsD2OzqqOXKu1Mv-6Iva-SVdfzBJ8jXHqaEopO4ZD-zyiTrY64AQ_xLall-bcGBM6iLnBP7hzm4ddoOtAjCO7CeGMjj61rwtLJ88zBEpzJT-PDdEbczq4sNVonPsWiyhk6uCKwyLI5l5V04vHKye99rZ-EWJiP93LM0-dbpBJ920b9Hhi3Q_hz-JRC0FqVj2lcLmzMWCH8hU2lgbBsMdPHpU9l8lzPGXcwFXP0-dlyrlfudTyExhtBfv6uwLD-RZfpj2CEFSOPy9HBH_a-oRzhnsFaHIa-UP0tAqi7tq-FgLrdAH983GDuztTzQC-ZAe6RJJw_xC_NqhkjWs4kJUg0r0THpWdPRceSC6osoW929djzZpSsbeOpsyiq8yzqk-JrNK5o0kLLGx7Fl57KMsyRdK7ewrOoWfUI4r8J2xZTZdMC28hgjuLxG6WXIRQ37zLrKFqj8cBnwomuMDIyTGJ1wbt3FWIEvcp1xtm01WjW_k2Mzu-w5ohuKnDrL5QqNUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199ab599f9.mp4?token=qQTAUiJ8fcUqcTkt_tZuFH_kWc8H-ZCFo-CvZT9XXdXDynOhnSJkrGCJNhkZ7iSA6gwE18ArOK8o254TWlgSWJ0WE_w4GJhN5q-xbSpuVZ-2rbJFFqjO64666v_d3hOghz1L1JOUpLZB0tqOXgbpXIIlvW7crSxT-qKZ3lR_T5QsD2OzqqOXKu1Mv-6Iva-SVdfzBJ8jXHqaEopO4ZD-zyiTrY64AQ_xLall-bcGBM6iLnBP7hzm4ddoOtAjCO7CeGMjj61rwtLJ88zBEpzJT-PDdEbczq4sNVonPsWiyhk6uCKwyLI5l5V04vHKye99rZ-EWJiP93LM0-dbpBJ920b9Hhi3Q_hz-JRC0FqVj2lcLmzMWCH8hU2lgbBsMdPHpU9l8lzPGXcwFXP0-dlyrlfudTyExhtBfv6uwLD-RZfpj2CEFSOPy9HBH_a-oRzhnsFaHIa-UP0tAqi7tq-FgLrdAH983GDuztTzQC-ZAe6RJJw_xC_NqhkjWs4kJUg0r0THpWdPRceSC6osoW929djzZpSsbeOpsyiq8yzqk-JrNK5o0kLLGx7Fl57KMsyRdK7ewrOoWfUI4r8J2xZTZdMC28hgjuLxG6WXIRQ37zLrKFqj8cBnwomuMDIyTGJ1wbt3FWIEvcp1xtm01WjW_k2Mzu-w5ohuKnDrL5QqNUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائران اربعین در عمود ۱۴۴۸
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453798" target="_blank">📅 07:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453797">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxfdN1Vs-C_Al8NNb4J8woVRivRqhiZaPzyOq4JiFJAJdMZQO4P2nN5DdpKkfy4o1ov2UeOdJPhdmHMauKsACWuXZHH4pwe3by2-1wGeRM8k0xunRt8aiRH_yPbKZHHhroKR46icbo-u9SL0zSbNttOnLdJLLCAtCrCgLipEGzmcPXXmgs_vTJS4m_eQQkQd6mYnURnbjGp12QJqojudSIc5QT9ikJzSlR-SBNcix2b_FQ6KnA43HCOxu2y_nPXU9X85qAyJ4ouhW1cVs4IRC2497s-yTRpefHUJhkw7mNa-ChNSNLJpFtP1Dm59Bn1WvZ4oiSbbaRqJmfK5YEIGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش سی‌ان‌ان از عصبانیت و ناامیدی ترامپ از عدم پذیرش خواسته‌هایش توسط ایران
🔹
سی‌ان‌ان نوشت: با وجود ادعای ترامپ مبنی بر اینکه ایران برای رسیدن به توافق «التماس می‌کند»، برخی مقام‌های آمریکایی نگران‌اند که مقام‌های ایرانی بیش از هر زمان دیگری مصمم باشند از کنترل بر تنگۀ هرمز به‌عنوان اهرم فشار استفاده کنند و همچنین به سمت نیروهای آمریکایی موشک شلیک کنند.
🔹
به گفتۀ مقام‌های آمریکایی، ترامپ از خودداری تهران در پذیرش خواسته‌هایش به‌شدت ناامید شده و این موضوع به برگزاری نشست‌های پرتنش پشت درهای بسته و تماس‌های تلفنی همراه با الفاظ تند با متحدانش منجر شده است.
🔹
همچنین تهدیدهای مداوم ایران، ترامپ را وادار کرده است برنامه‌های شخصی خود را نیز تغییر دهد؛ از جمله تعویض هواپیمای ایرفورس وان در مسیر بازگشت از ترکیه در اوایل همین ماه. به گفته مقام‌ها، این تغییر به دلیل افزایش تهدیدهای ناشی از ایران انجام شد و انتشار گزارش‌های مربوط به آن، رئیس‌جمهور آمریکا را خشمگین و شرمنده کرد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453797" target="_blank">📅 07:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453796">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnUXwRZMcXvEGiFRFxVmYTc7hQPJQ5Ifa1hStV9FujzpEV1ZwBx5q4zDuKilbHj7vm_oxQm_8UhlItXHoByl00d2DLoZ52UuJZAPZl2smuY4n3-aKgTeO-LI6m6Qgz4tFVUWccd7sNH0_qrX6Dx3z87FS_Ftxo3RdSFsOsSLpeVAylNCfqdGC0wbKN4hul5AWpuQ4WtRzYqcYUHNWQmr6zENc44QyvBAGJ810C1KKfA3O83vqVTsCkovvOBq4dGIc2uzRDenp6lbtF18REPnrY7gLZki8_BSE4AYqYHUHgKJXDU8lAVR42KP2uF71iqgCAONDpli2VZY_YT_-Pb5lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در دریای عمان
🔹
مرکز عملیات تجارت دریایی انگلیس: در پی اصابت یک پرتابه به یک نفتکش در نزدیکی سواحل عمان، موتورخانه این شناور دچار آسیب شد و کنترل خود را از دست داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453796" target="_blank">📅 06:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453795">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca23ce6aa7.mp4?token=nIt2Ich2bxgrv1DENJEtDh7vRAXxIhzvkYDxVO6lFgrlcSgys-8ogWIJRTZSgiYNalCJ48CKl2yBIcdblS-MD4-dsUwf0VQRfyjDNOZZK93T0fJ6uWvKyVJJKr9HAKfL1rCWozav6Wt04PKqy3QIt_IbbO7pUthIon4yMhjJVPRCJ0CXvVG_ISn1bx7KivSsx8TccHnrx_sAmxeXDoELvi7rd5oatrp0Wj3RynYTg_lD1lYF3Lgh8iIRABgYIwYOZN_peMfHr0DBYn60A5gc7Lgd-KYKr8h2nk6fgSh9SZ72IHnBLg5EPCuzwYwj3Z9UDcQyPbmsW3XZoVazlznNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca23ce6aa7.mp4?token=nIt2Ich2bxgrv1DENJEtDh7vRAXxIhzvkYDxVO6lFgrlcSgys-8ogWIJRTZSgiYNalCJ48CKl2yBIcdblS-MD4-dsUwf0VQRfyjDNOZZK93T0fJ6uWvKyVJJKr9HAKfL1rCWozav6Wt04PKqy3QIt_IbbO7pUthIon4yMhjJVPRCJ0CXvVG_ISn1bx7KivSsx8TccHnrx_sAmxeXDoELvi7rd5oatrp0Wj3RynYTg_lD1lYF3Lgh8iIRABgYIwYOZN_peMfHr0DBYn60A5gc7Lgd-KYKr8h2nk6fgSh9SZ72IHnBLg5EPCuzwYwj3Z9UDcQyPbmsW3XZoVazlznNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها هم در حمایت از ایران، پرچم خونخواهی امام شهید را به دست گرفتند
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453795" target="_blank">📅 05:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453794">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رسانه‌های صهیونیستی از وقوع یک حادثۀ امنیتی برای ارتش این رژیم خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/453794" target="_blank">📅 04:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453793">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رسانه‌های آمریکایی از بسته ‌شدن بخشی از فرودگاه بین‌المللی دنور به دلیل یک تهدید امنیتی احتمالی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/453793" target="_blank">📅 03:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453792">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حملۀ اسرائیل به یک فروشگاه متعلق به اردوگاه آوارگان در غزه
🔹
المیادین: جنگنده‌های رژیم صهیونیستی یک فروشگاه تجاری متعلق به اردوگاه آوارگان در غرب بیمارستان شهدای الاقصی در نوار غزه را هدف قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/453792" target="_blank">📅 03:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453791">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">واکنش عراقچی به رویکرد انگلیس در جنگ تحمیلی علیه ایران
🔹
عراقچی در گفت‌وگوی تلفنی با همتای انگلیسی: رویکرد ناشایست انگلیس در رابطه با ایران از جمله مصوبۀ اخیر این کشور در برچسب‌زنی علیه نیروهای مسلح جمهوری اسلامی ایران و همچنین همدستی انگلیس در ‌دو جنگ تحمیلی…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/453791" target="_blank">📅 02:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453790">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">واکنش عراقچی به رویکرد انگلیس در جنگ تحمیلی علیه ایران
🔹
عراقچی در گفت‌وگوی تلفنی با همتای انگلیسی: رویکرد ناشایست انگلیس در رابطه با ایران از جمله مصوبۀ اخیر این کشور در برچسب‌زنی علیه نیروهای مسلح جمهوری اسلامی ایران و همچنین همدستی انگلیس در ‌دو جنگ تحمیلی آمریکا و رژیم صهیونیستی علیه ایران را محکوم کرده و بر ضرورت تجدید نظر دولت انگلیس در این زمینه تأکید می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/453790" target="_blank">📅 02:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453789">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
اجتماع خون‌خواهی دیّری‌ها در شب ۱۵۳ حماسۀ میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/453789" target="_blank">📅 02:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453788">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">منابع خبری از وقوع انفجارهای شدید در کی‌یف پایتخت اوکراین، خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/453788" target="_blank">📅 02:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453787">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی
🔹
در طول جنگ ۴۰ روزه وقتی تأسیسات پارس جنوبی هدف قرار گرفت، ایران مهمترین پالایشگاه گازی جهان در قطر را بمباران کرد و بلافاصله ترامپ در توییتی از ایران عذرخواهی و تاکید کرد که «دیگر تکرار نمی‌شود».
🔹
حالا…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/453787" target="_blank">📅 02:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453786">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی
🔹
در طول جنگ ۴۰ روزه وقتی تأسیسات پارس جنوبی هدف قرار گرفت، ایران مهمترین پالایشگاه گازی جهان در قطر را بمباران کرد و بلافاصله ترامپ در توییتی از ایران عذرخواهی و تاکید کرد که «دیگر تکرار نمی‌شود».
🔹
حالا در میانۀ تهدید ایران، آمریکا به خوبی می‌داند، مهم‌ترین تأسیسات انرژی جهان واقع در کشورهای عربی و اسرائیل در تیررس موشک‌های نقطه‌زن و مخرب ایران است.
🔸
میدان نفتی غوار در عربستان
⤴️
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
🔹
تأسیسات ابقیق و خریص عربستان
⤴️
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
⤴️
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
🔸
پالایشگاه الرویس و میدان نفتی زاکوم در امارات
⤴️
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
🔹
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
⤴️
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
🔸
میدان نفتی برقان کویت
⤴️
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
🔹
پالایشگاه ستره و تأسیسات المعامیر بحرین
⤴️
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
🔸
میدان‌های گازی لویاتان و تامار اسرائیل
⤴️
لویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/453786" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453785">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qADXkQgJn1hr6JVVBfCp9UMIzJGaq76FE2rPcmAR7dd6Pilfzfd5a1QJqJg-0Bq4dLWoLmPNR7UP2wV73aMBc5eqkidCRNt1S_T8yFb0jrOZClLoksKH1vZJJSuFMeESU7w1aMM8x3QOOFY3hxl8OUHugbBxa63xkgyi_l3TwTV0b0i0PA9HIe8Wyx8roei-L_WKwzZ-Q5KmPWBPSPLpQkypMjpLfSEhI0EUZyNTeXGIONfUWohMh5ByDUY1IIEpvNqEQn7PQeuhRvi70EYW8P0K0aI22uXbbxXKlKmeruaUNRGD_MU34ynizw2jnYndmGsy8M5vb6PLvRNHnLXD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت مدافع پرسپولیس در هاله‌ای از ابهام
🔹
در حالی که قرار بود روز گذشته مرتضی پورعلی‌گنجی، مدافع  پرسپولیس، با مدیرعامل باشگاه پرسپولیس، جلسه‌ای برای تعیین تکلیف وضعیت خود برگزار کند، اما این نشست انجام نشد.
🔹
پورعلی‌گنجی که در فهرست مازاد مهدی تارتار قرار گرفته، در آستانۀ جدایی از پرسپولیس است. در صورتی که قرارداد این مدافع با پرسپولیس به صورت توافقی فسخ شود، او راهی تیم دیگری خواهد شد تا فوتبالش را در باشگاهی جدید ادامه دهد.
🔹
تکلیف نهایی این بازیکن پرسپولیس پس از برگزاری مذاکرات میان نمایندۀ قانونی او و مدیران باشگاه در روزهای آینده مشخص خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/453785" target="_blank">📅 01:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453784">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd2a1c1bc5.mp4?token=af4z5MhrLQHUwGF0hu1rN8LuzhqQ8fjUuhro9U8GVlBg-2L-4LxxsF0hdHRUQLT4RtwbXJUIAN3GP-ED8EDIp4ZsyM2mjWXUEK9YGRifeQFEXHLCAcPbYIf-cP3OGPIISwQTw4GN0l8ab2z12F8YkNpmG_7Z2_KoqMLaj-xXW7QIM6jEmgzoEKEE9wZiKcAdjFNRvNmNhwG6bXUDvMQIfngAfI6MpX0Nu0M_Rnaj-b3yoHy4aY6XSw5rE_j8Mf6i209fBgHt26FyEecHKgqg1A1Zo8MT1pnJkuGAKZc9J5KCP5HMcZsr7cb9xXPGsIdYWK1on10iybhHbvM_qIYAEljzDznBf2TZS5q-WsuOmwy5IC2_g7c-XJ5jtvQis-GudTd032Tw5Yn646TIwPIJGpCDgrlcRcka4OQSpUC3eVkGZOCdtXDnW4vp3NPyfugwqdUT6VHTvS6oE0UnRyspmH2IHYw6wehhasvoEyXT7_xo7VB8XEyhHJCRJH-Sa_5p3nxh4Xkwk74_NM6e0jTtWnjBb3SHZ7pNEXbAGMYBD0kCY8SkhFucN1CVgvnEVx114rXzzaQHLEnqlqEl1KlcYYLIRgumzymHcnxwsZ5-UopIKaB-yAW4hx9qOV1xviuigpXSNCtS_3NFsfRh-LUIyLLg97G8x6SlZCWoTY88s7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd2a1c1bc5.mp4?token=af4z5MhrLQHUwGF0hu1rN8LuzhqQ8fjUuhro9U8GVlBg-2L-4LxxsF0hdHRUQLT4RtwbXJUIAN3GP-ED8EDIp4ZsyM2mjWXUEK9YGRifeQFEXHLCAcPbYIf-cP3OGPIISwQTw4GN0l8ab2z12F8YkNpmG_7Z2_KoqMLaj-xXW7QIM6jEmgzoEKEE9wZiKcAdjFNRvNmNhwG6bXUDvMQIfngAfI6MpX0Nu0M_Rnaj-b3yoHy4aY6XSw5rE_j8Mf6i209fBgHt26FyEecHKgqg1A1Zo8MT1pnJkuGAKZc9J5KCP5HMcZsr7cb9xXPGsIdYWK1on10iybhHbvM_qIYAEljzDznBf2TZS5q-WsuOmwy5IC2_g7c-XJ5jtvQis-GudTd032Tw5Yn646TIwPIJGpCDgrlcRcka4OQSpUC3eVkGZOCdtXDnW4vp3NPyfugwqdUT6VHTvS6oE0UnRyspmH2IHYw6wehhasvoEyXT7_xo7VB8XEyhHJCRJH-Sa_5p3nxh4Xkwk74_NM6e0jTtWnjBb3SHZ7pNEXbAGMYBD0kCY8SkhFucN1CVgvnEVx114rXzzaQHLEnqlqEl1KlcYYLIRgumzymHcnxwsZ5-UopIKaB-yAW4hx9qOV1xviuigpXSNCtS_3NFsfRh-LUIyLLg97G8x6SlZCWoTY88s7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع شبانۀ ایرانی‌ها در کربلای معلی، مجاور سرکنسولگری ایران
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453784" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453783">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJNpdY_996N7M6EdJ98DHTRyKrbU7luc20OVVwzjQhHTADr-o6mOXLCg_4Q9MNuLwvkEbkvDO1KitpyXUdvjpKBs_AZ6EWVrEtW6j2v3LtirXkkoacGrX-ICPSXRqinKA-K9L5W8fcUHh03o5jZKWSpVfIEEn5hwaP_ZzX54ou0pTSHdXAA6GDezSGsTzi4i_GLD6Z1Uu5-4iTldMD54B5i5EoBoRiJai7bEHU4UNafAfFOsa4hoFRCcrzGQzUsqSczmuzcFUHghsSr4eIkImWPyHi7EUZkyQu0QLcsriw7504DoskJG6HWdfqV16hlrg9MtQwkFDaipraBzFFujgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای وال‌استریت ژورنال: ترامپ دستور حملۀ جدید به ایران را صادر کرده است
🔹
روزنامۀ وال‌استریت ژورنال مدعی شد رئیس‌جمهور تروریست آمریکا دستور اجرای دور تازه‌ای از حملات نظامی علیه ایران را صادر کرده و این عملیات ممکن است از پایان هفتۀ جاری میلادی آغاز شود.
🔹
این روزنامه مدعی شده هدف از این حملات، ازسرگیری فشارهای نظامی گسترده برای وادار کردن تهران به تسلیم و بازگرداندن ایران به میز مذاکرات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/453783" target="_blank">📅 01:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453782">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiuQCFID-BAFWjMT_xv9SmXAiW3bXQlRu2wKlTnMkxQXUfpLq7WWoZNLIMT4F3CKLnNcEz1tFqcC2HuGlEnhDodiYgykPu3CYVLYbPr0UZUXWCcMd0eqaxYzoYbOR6VwtduJz_aVlhwSiShYGq4EiuDN_ThUgc2esT3_yMLPU7Ls8mzy2epqie7DaGvsC4fUEJyk4U39e3PAP2VDlXHfygfGr8XVu-i0-A6EFajXehsWeMGg6FPN3a_YNd2ulvClpbw5jjh5jXCSRFb84CWJuO2I1WVbQuKElup5LaizaMNeFKJiFpAjcG3V3x3-tMdJQz_WUm2r3_IKsQi_ciWlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی: ادامۀ آتش‌افروزی آمریکا قفل تنگۀ هرمز را محکم‌تر می‌کند
🔹
محمدباقر ذوالقدر: ادامۀ محاصرۀ دریایی و آتش‌افروزی رژیم آمریکا، هم قفل تنگۀ هرمز را محکم‌تر می‌کند و هم تنگه‌ها و گلوگاه‌های دیگر را می‌بندد؛ و تاوان آن‌ را اقتصاد جهانی، بازار انرژی و رای‌دهندگان آمریکایی خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/453782" target="_blank">📅 01:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453777">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F174QkTlibTOqwkEyZtFWl8SY9d3ZCE21p3UopFKE5JV1YQXAT8RHoVhGaH_M78MVrJZyG0yHcaY6xxRpDImIz3_WABlGG89RaYBEeQYQ6FlSSAGZdxrpJ7npB2As4X4mz_kbdW4hNuxOLvBM3WqSrIde35cKazr3vJJIjX8Nal32yFwQhtibYtIa21Ld4S6BMigx0QPrHpfF4r4BehdGh15e34M4HqyD_hWfV116WoI3qJMpDAS3Y3f43DJtXTK0NJZ1vOpTxiR4EtMuO55PmhPzWnC36939KNJOz6xjPp12aWrcGkycFPUx-cdOoWCv6Y5aDFqyjfXuCIu_z2_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILf-r4DtQDv68hGG4xMoCcDSkyTkRgl-KX2J31WSL6ocZCXxINpV0PetNYr9v8KY20eBlIFUnpT-omzOAR0xNRvjJRyGTNkOnS-gpbErusj2gi1xzkLlzx7rlSpFzuNPQKjkvCqKCrcQ_id-5nOrIEaiIDVS4bKcIQ6n1CpMSKPS28e-LipmOArJMk4bcskyNRE_gYxOJ1_tnKJCoTmy1YRPw6D6tDBbsWEAT8Maj17Eu6N10bJ5meFgfGiX73IhvrPkwpuZnc1RW2XvVAJgk6QevepZBZ6X9S41b8bP4S5VfAZJxteculX6Ta1dabvnCHMEi0Nhk3xcub-cJDqK7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBMNwuzK1niC0q076boLM_oOwSNq0w-9qjovnLWYv-5Tyw0WwYTVElz34-KM6JeLzfsqKtbTbZyi_4BnG1zIXixtc0Ksf5Kco1q6zbakbHAjahiMSn0kauDmJowB1-KxTq1WxlHhfok7vT0YLlu_DqS6Ba75ueQma_Etz6LUm12vZMYnoYEEK2N7vNlZpDfR3Fvfa-eupLmkcu7m8xq1MmtxrG7Sj33_Bz0x12jHdYS8UaS3kX4PqMo_bytF8fGCfE3a-LzDKv6KbvehOcrK4CKG6NP6OTLy4dRQKysCZQ1BCez0mNWfvj-X27WpVe4WyzAshO9zjCwooKJhGtbi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vIEaRK9jhP9Pj9Oj18WPoysl99QNuBDqqS5exbzZIRbNyUkF0s807pRjlAVIBqoD6HlOmUnIUp_Zcy9Srd4Dkm2kbYiueY5-my00gYZk4zsuj60uuG8Q48rMI6y9LdndotCkuyqRzYpke-UzaJOS3Xci-4a76ljrmSS9EGztfwbQt8mNZoJ3STOMr77FpTFgeth8CktsXzBgJoqYilAUfHbpx4d3KikKSo8Kp0GH42nh43rFL5FLb7grkdz7YvKGySqpBshos3MJHZ_jKXA6UTQmgbn66XTACvtm7YqjESJwTo4H_N8gUgucTw8Mbax90ctMzvFEWbDAZgWG4DSMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HI13V-y6hCSce2RMPQX-UfKQL14bUEzGdVKI1PoXrpUHh4Iq3_oRLN6bY6slZeCiIGeioFs-J2ZXZQeL5gyievIyHu8dzHR-FI9YraQe-iB6DRARll62RrdfH4comSdze1FBP61ZyRLDmrre6otWvGPHzxRX75GIoaLALVJitNiCLjyKljOEndCr8mGOAcyNhROPzjNqNQG4OU0qpbwF0Gw7sS7Xax_yddaA1rbfJBXuYRLT5bbDs4m3sF9r7zB6FXgUtxlSbznec1zqGBWIZ0YDUrzNEW6P-mocSkvZ5BWDZwMWlhjWHJZx5zVzjTzsAQ1K8GkMY05E2fNiOeKRGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۱۰ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453777" target="_blank">📅 01:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swUKMU6EG9saJDWtLX1p35aLGANUKaNmn0-zzD5IKVp43ydeawvGyDEObHZsWKoojNN8lSBHst-jhGbKErYvEpfas00ZLXQ0--ifv3FQ_OrizgH7cXkcUR815TWpCUT_qtzOvG10n1BG4B1Q3_A5DHeObNgYsQlmAOy2e_a7B_v2h8nTzattyN0xvqn5l91YbigEuvgUO7wxWPaSE85ktht8R-Up4wkDLA_Qx8fKHcBbPFzC9_0HROAfL0YOr5Wu22A2q3kg4zurr08lSq-3txOflu62QFg_dM82PcDsBai1LbK5DUGNyEpSudoGgpY5t2wo1ljO6P7Vz7epkB3Eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYjFu3N1e43t8yvAxtlVMRJ4VwuhITPKTiUwDVlM-OH2Pn9yIuO-DmCGrm2Utd5YY-q6Hr1ZAcAVoRSG_LABAuCwGCdyFSKboepslpS2RWn-5xJu6z5gMGAy7okwThjCb2peeG-AqL8q4tDqEfrXX7wAe_rutp3Mv9VlOkfD1lDAJh0OfUmUFwJc9kdh_dB7aJuVmc0oIzOzKdSGRG4--TLCPCCiYsRH6hkLQR9HO5ufO85M4P6AN1nHmRL_Vi92HICSLeArDAyn5sAUeZpx3C8fwdl5PiPadkuaPo0D29fEbOl-2g2V2pz3jpj3k2eoU0mQWwQ2pIKC_YNKtLwkIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiWabQGJzwSQO2t3fnw66Th2mm_CePNzsXjXQgvha9gJHJmRbDdEys5NYCQBaqMP1VMyvvcu2nBRzfE6FAgJzVUS0cga2eDcrOg3_j-ng3FHWmU1cfbXOcrhJT9t6boWFsxg3OAfk-hSrvIjOMYRhbGjKv9IsS-9i_JSe-Mo1y8q3w2jmiYKd7bf6i1Aa8hQeAVHoY2IPvp3z1tGcYKjLe_ObGfgWqo0-6JOCBAugecLdEyuzJ9tpvkiEWHzaZ4N17oNTO8IxeL47KdU3-z8a8KyZaay3z0-JCdY5VWnZuEbnXrVVgmlgPDPsLxF4fUPn9mhpczhm0KUWZxS5zdo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtPrD4GfLRLw195sfqyb-efXcjew4J0aRFjCPuuGCoEm8wIHoubSCauJupPnjl8BiLq_mqLIya8s1PcuUsIk2zfr69KpTva78jOs6YB-Yb9IKXkh5OJSsx18EUm4CbRHJCIhWhggAzZL-gGWnKC2dqkMLgcrFsBntWclKtWveE7GCRRVTQN3DDgabngGP5ndBGSjYa5DVZB_ge_x78GSI62KkJaSATwbFScavufNWQvjpNdWCzh56oe-Crzmjh8Tdrg4GmxMiYEYO9Fwrf1pFJwCEgnb0uMh5spjIF1AaLZVJy-D175nPhE7ukO_pWvGMVFJ4YVgKAq4nnCAgWCB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQJHqprAR9WlSV1i0Pf3xLHy8ihHLzZTq8onKommuQ6iEj11sMeeT1wUPEiR_66BogIZt-K_WO43n0JkOaDd_a7Ca0BKS7yN_biU3E_uhQy9eDOERloekP9_PNDubxPjOuuXnw7BWqU0NFBxWdBSaXwIVta-zb3kfuSytc8lYfBy7riPRfqLfcX0IqMDMJJGFjvHXwVkjEJ96v6Q2hqScwh8sLlNAdRsylNKt1Jl0mwj9SYdO4lwDQZDireWC7aKCyjLQ1GPggOCl5lPArmfIE1RhmYrdOZCXg3KaP3s9amhqNlNAPNBVCpeZ7cVETSQ6wdBozh7A_dgLh7HA5DFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKRtWZkkAYsS4AO13h0b2KkHzXmSfnxOe_JgnAXuo1X5grYzuEYUNOMs8wCjzfQX8JtzW4DeoR70Llb6adJgRJAuqrCVzVxZvWInDkguQi2WRdzUAWW6iHrZXBemP0U-_xd6KPOEWTNGPar8OcXFTKR7gIXKin_FYSRL7i44oOyvzeAX9mhKuXtGaAAoDcgPx-E-jmseR8DYdpeLctL2WYwSqJoDyCtS2cWDPm2LLL_OnL4IdMJSY_2R5d9YHhI0QjSVLEHjhn7y8DBXQqyFKq35B20tJo1l5RGGkZbTR8M5k42tJWUq-FkcSHyRWVutLfK2F9cHK7XY5r-pDDI15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwOyMUNs9_R4jwkiNfZh3aGZoPzX9Jcqe1HQmgunrWdynjADZZSWTZcIAURmVGHWKVxjNRh12yF9X8ZgrHHhJrrtl1MeQ79yXZfrW4fKMFOpBcV-L4hMNO3RQNZCGkq5fU-8SgrmJUk3XDnupAqAPwzgtdoTnq9hEu_9Cpr4WEdizz02pZxPXD0vX_THFcu4UwuYnWNHcg2WeKkc5hNZnEU_m_bGFUaXdNkdqzSKn-m6VtYYhujwy9O-pGdOJmA1XJ28MfyL1boYt6D-GEVghaw40_5NKYOuYHECnBV3mnBQguKEu8OQMlptPJoqsVXTkRR7DB1PQF1NHyJKkpz4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuktP_i9bcsi-RGp0Sl9jvWSUjOuAe1rNJ2xy6DOfXG0j7B5n_DMfHCIWtfylwDkOlIu9qy6sOA1zedMT3-RLwtFB2fCi8VGy6BKNhrkLPwH1kz1_KOAeTObTAzI0xbJK7UhSEnbCdlMpsEUNScklopQJgRndL6aNBCzn_t98B8X6o4aHpqaRIxbMJgeePI--s5c8-S3FD7KAecTUjlZHny0DYLtg3hhUMbbM0a2AWgnQqW5uz9ddaJ7NB2sICtI6GyQOfupgwDIpam9gE7Dmy0kbCurz7XKVsiTq8JRJVQnFl20H-w692Hi_LPAHCOHAItbPk61_k8GgQF7uCyRSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJ9JQvgmn_kz_SV7Jm8S015OhcpSkqweQO8kutlPb0uUOKDF_1MiEvEKsH6uT6ryX7oTGmPu5_h5LbGnwkfFAy4GLxJP5phJqbPr5Yi-qDEzV-XmtlTolg8xyztaLkKeGJpgLa5G9z7P2A3xzNWFi43aJNeBDLK338KRUQ6tWuumoPgXI3bUxfY1Sr1mDgRsIvuwxlgUdTTIfyvWyfOE5e_mFHgC_KEinh9Fo12QnMdMEMtU2JeBvqXz8s0WduqsTwbTqP_ThREYpbMxIRhwqBVus7xjb1em2RLwModiH4fHoLFI_Hp3yL09BPXpgUwYcaDoJcHSNH01d1TLONx7gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/In0xXLBDVAcmXx2GAIssg5YjuYlaIE1ZJoMiPAULQIOe9Kp-mDFCc1D3H5Abwl9-lMW1yfzKD_1rKlYXVS-2pACmR3PAAyVXmd8LfveJN2p1AggUszFCyESk2jjCkYDcjg4dgOL08KVE7QcwZXtQUZRPML4E0hRKXycHveUC-SSvfthC8dkEKjOt7v3QkRxSrtzdH7gSi8fuJJDBkNArhIlDLIxzRkJd6Htq6aannTvydvgk5xhfpAxt0hK1UDacoqZ7KD-dbNUyADFjptl0HQaYLzFnVwVc4dnJan9JVfUfx4HTTWQC6CoTSW6NmPHZpHSxUzuEANDzi2kqca6zmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/453767" target="_blank">📅 01:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00813dee2d.mp4?token=HqVx3sZTXEYdkL6bWDYuTGP_EfgceEn2NKwvQx_PksoLO8TFVJIDSJ2csvBGMh7VCkA85LLrsZYubcbRVmcdshzL7xyETftKNfWS9I1pmTSFanmJnfjJUefdP31boR_xkjEIFFm3b0uD0DkRcFAQJuWnRKGfiXFECmnW5Fy5PWpfd4LMWCL1c9JAOcxXPR5CudyabalDn_KocfBzABzbIf11g68o0ZWL3FG3g9uT3xsoJw_FWZJtDIdGP3nxPnb3C_cKvnFBKEUmsqvBYAi9BjTwdvoVPeYhTq9E6qh9AU5AIFGwWLu67iBKW5wSRjEA-1d-LPi-eyZguD4u3R8-KDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00813dee2d.mp4?token=HqVx3sZTXEYdkL6bWDYuTGP_EfgceEn2NKwvQx_PksoLO8TFVJIDSJ2csvBGMh7VCkA85LLrsZYubcbRVmcdshzL7xyETftKNfWS9I1pmTSFanmJnfjJUefdP31boR_xkjEIFFm3b0uD0DkRcFAQJuWnRKGfiXFECmnW5Fy5PWpfd4LMWCL1c9JAOcxXPR5CudyabalDn_KocfBzABzbIf11g68o0ZWL3FG3g9uT3xsoJw_FWZJtDIdGP3nxPnb3C_cKvnFBKEUmsqvBYAi9BjTwdvoVPeYhTq9E6qh9AU5AIFGwWLu67iBKW5wSRjEA-1d-LPi-eyZguD4u3R8-KDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مکالمۀ اخطار نیروی دریایی سپاه به کشتی‌های متخلف، و بازگرداندن نفتکش‌ها از مسیر غیرقانونی
🔹
تنگۀ هرمز بسته است و هرگونه عبورومرور صرفا با هماهنگی نیروی دریایی سپاه امکان‌پذیر خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453766" target="_blank">📅 00:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453765">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌ تعداد مأموران شهید درگیری مسلحانهٔ دیروز در شادگان به ۳ نفر رسید
🔹
فرمانده انتظامی خوزستان: شهید علیرضا فتحی که دیروز در مأموریت مقابله با قاچاقچیان مسلح مجروح شده بود، با وجود تلاش کادر درمان، بر اثر شدت جراحات به شهادت رسید.
🔸
پیش‌تر هم شهید مهدی مهدوی‌کیا…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453765" target="_blank">📅 00:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453764">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd902523ca.mp4?token=V1n4-S5SCfa-z_BO6G66xi4qP0-KgzMvEB6PDB6acLVh30UQr1GowRZuCD43x2tJlRaqmBxrey3gHJR7rfVTJgzBJ1Gw-qGQjyDG_cKY9bJWEVTlN8kGSKAV0EvRs0OpCd5SWtUexJb4vj_8XjnmqgpTqr314QE7OKqujv_5B87eAHkIkR5ipfppAcsZu_2iCvNvCpjOHfOeIAJpuJmiUYEbJv27Qrtxw8GnEIEb96TK22QmXs8BMN0nFy2SWqNy7v4bEhIhtCatId6vUcjOES4MKUi6fJaF_2v3wsZ5vRsnEJf8XUzRGxPeSyV0UqE8L6NJJqXVpsMIxUrAQz-gyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd902523ca.mp4?token=V1n4-S5SCfa-z_BO6G66xi4qP0-KgzMvEB6PDB6acLVh30UQr1GowRZuCD43x2tJlRaqmBxrey3gHJR7rfVTJgzBJ1Gw-qGQjyDG_cKY9bJWEVTlN8kGSKAV0EvRs0OpCd5SWtUexJb4vj_8XjnmqgpTqr314QE7OKqujv_5B87eAHkIkR5ipfppAcsZu_2iCvNvCpjOHfOeIAJpuJmiUYEbJv27Qrtxw8GnEIEb96TK22QmXs8BMN0nFy2SWqNy7v4bEhIhtCatId6vUcjOES4MKUi6fJaF_2v3wsZ5vRsnEJf8XUzRGxPeSyV0UqE8L6NJJqXVpsMIxUrAQz-gyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار تجمعات شبانه به حرم امیرالمومنین(ع) رسید
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453764" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453763">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1c_UJ_4K1_fGgkA9mOI0bbrOHbua4txticXJ8UNEWYQFwCIDzFDRjBIZAM3VTw5ADxgIvygc3EzTVFXtYtDWhemSMGVbVGa3mAwkur2ZawQ_mqXuIidLfhmsu9gYiCZFVkYnJbHb9XvDbRNTZ1GzHKTIeTp-1mvJwpCdh_r-RK89v6DVGUwBprhftxD6pw2rraAAohRledSMMO_Z_ao8TDlXe5SA2V9X4ErpYBRK6kaqhGB395zPIL7wRmTzxBB-qZ5BiLQKtXDnCPQXjkt8oovWn6vQ4hRH0wzHnr8iOndCHyTJ6zSgxODiZJ7mlziWEDk_46Rfiz9VVwmku6stg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: ۸ نفتکش سعودی مجبور به تغییر مسیر شدند
🔹
یحیی سریع، سخنگوی نیروهای مسلح یمن: در راستای تثبیت معادلۀ محاصره در برابر محاصره، ۸ فروند نفت‌کش سعودی مجبور به بازگشت و تغییر مسیر خود شدند.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453763" target="_blank">📅 00:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453762">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شهادت یک مامور در درگیری با سارقان مسلح شادگان
🔹
فرمانده انتظامی شادگان: در پی درگیری مسلحانه میان مأموران و سارقان در شهرستان شادگان، یکی از قاچاقچیان به‌طور ناگهانی به‌سمت ماموران پلیس تیراندازی کرد.
🔹
یکی از کارکنان پلیس در این اقدام ناجوانمردانه به شهادت…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453762" target="_blank">📅 23:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453761">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b7691d1c.mp4?token=V0EnRPT-Bdab5n1lZOTj0O2eoKTFv8B8Dnd_epUxiO9pnYNn1uUdIZhzYaWlxjMa3HGyak6KpYUHz34MOU9q-bTk-cVGANoTVHfnesDA85pDEcPVveSL3hE0kLHgZe_4Ag3NRyJORimUIntSTbz0tDNUSQr9n80pHNUJC7SY6symGTKmJS9uM0U_ptLKh57yzXWyb7biQsz2abU58gXACpkIFVdxPtgj7y_3gvqiBOo5-AmEeoQpYRnFo8UFC6sROicopbMzd52I2EqO8ciNhiJMoX1sNjDb37rRGViwZCPzKHtkvIi-nK0pLQQUqSMCR2yMpbv6UHPTGK1fvruKrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b7691d1c.mp4?token=V0EnRPT-Bdab5n1lZOTj0O2eoKTFv8B8Dnd_epUxiO9pnYNn1uUdIZhzYaWlxjMa3HGyak6KpYUHz34MOU9q-bTk-cVGANoTVHfnesDA85pDEcPVveSL3hE0kLHgZe_4Ag3NRyJORimUIntSTbz0tDNUSQr9n80pHNUJC7SY6symGTKmJS9uM0U_ptLKh57yzXWyb7biQsz2abU58gXACpkIFVdxPtgj7y_3gvqiBOo5-AmEeoQpYRnFo8UFC6sROicopbMzd52I2EqO8ciNhiJMoX1sNjDb37rRGViwZCPzKHtkvIi-nK0pLQQUqSMCR2yMpbv6UHPTGK1fvruKrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مرگ بر آمریکا و مرگ بر اسرائیل زائران نجف در موکب امام رضا آستان قدس رضوی
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/453761" target="_blank">📅 23:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453760">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b386fe25.mp4?token=nJtmjSTO2gUEq_mUko9AuVKfj37nyLv89caGrwbEQIlUIA7fmEt-MdD3qp_SKEFlYwEl8SlfcnrBhcDPxZxtqYYoA9nZKadEc7AMPIWCC1p12Fl8BdHtwZVsI84yw2Wq7VaiS5mUdWyrcbQL35QtvSnBJyA8yTOqDahXY0ngPJJ8djcM3_Ezq81h89o2Ofs7t_TaQTD38g5CbRBP2SItzhfNbnwH9BZbyxlhT_WihsOecy3OUx4mPJItQUPchGvmqKDFvbHwocIIoSMLgvjMew8ZBkuFuS8-02L9z0_y3jYs2RTi1WQvXWiVVPD45IT4Ya55agJr34gS-JhrwLNWHT9fu7mNDf6ZHJf0Wsw69sawEzpgo45ot7pPPun3LtjWQFRpbwL8GUsws2t9M3HvlPaFGrhpiIyAJZ-AJwHunJQomkeIRNA6RHnbwEn2P2GJRnvv1ob2bxY7ejlLBeCPJVlzF3D2Rpj9hppMScVRjJVqcecqQwS9i8q-ZlVt8TgkSaFBX749fsUD9vwJ_Q4XBsduPBpBJI_X9kaFFRRNjUUexcwiuz8DZtymJskJkM1aBQ-7rQjgYmDjpuC9xbb5zzrqw3lERNYsRS9XpiPDLKXEQ1ySqbp_sf20px2_2Tq2fPUf9aI4DaBGkAohh8EAUQwyMXZiOUWJC63A9QGK_Fc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b386fe25.mp4?token=nJtmjSTO2gUEq_mUko9AuVKfj37nyLv89caGrwbEQIlUIA7fmEt-MdD3qp_SKEFlYwEl8SlfcnrBhcDPxZxtqYYoA9nZKadEc7AMPIWCC1p12Fl8BdHtwZVsI84yw2Wq7VaiS5mUdWyrcbQL35QtvSnBJyA8yTOqDahXY0ngPJJ8djcM3_Ezq81h89o2Ofs7t_TaQTD38g5CbRBP2SItzhfNbnwH9BZbyxlhT_WihsOecy3OUx4mPJItQUPchGvmqKDFvbHwocIIoSMLgvjMew8ZBkuFuS8-02L9z0_y3jYs2RTi1WQvXWiVVPD45IT4Ya55agJr34gS-JhrwLNWHT9fu7mNDf6ZHJf0Wsw69sawEzpgo45ot7pPPun3LtjWQFRpbwL8GUsws2t9M3HvlPaFGrhpiIyAJZ-AJwHunJQomkeIRNA6RHnbwEn2P2GJRnvv1ob2bxY7ejlLBeCPJVlzF3D2Rpj9hppMScVRjJVqcecqQwS9i8q-ZlVt8TgkSaFBX749fsUD9vwJ_Q4XBsduPBpBJI_X9kaFFRRNjUUexcwiuz8DZtymJskJkM1aBQ-7rQjgYmDjpuC9xbb5zzrqw3lERNYsRS9XpiPDLKXEQ1ySqbp_sf20px2_2Tq2fPUf9aI4DaBGkAohh8EAUQwyMXZiOUWJC63A9QGK_Fc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها دوست دارند روی موشک‌های ایرانی چه بنویسند
🔸
درخواست مردم عراق از سردار سیدمجید موسوی و نیروهای پای لانچر
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/453760" target="_blank">📅 23:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155545352e.mp4?token=OH1s21KiyTwKt3Dqvo406cibR0Q0z7eBw4fuzsMPN884d6u3XqKZ8YSTfY_e6BYumVXRUrDuVcsX--OnE6VIm1niR4bL20rZQ8o4Lk3bwNAuUAHxRVipXgagxvuH_Y2BcywsQ5Ug6g82JZ2UgNP_gk9VNfaNSyKTzNcn9T4IvztHwzCXdEF8Vr8b-skxom_ETCkYOc3_WeneXj2QI3C6Psm-rLeSBe52RS72sy0coINQXBwOAsEA7hLed40v_MreV7YQByclODQepZaFf_3rvDq3jPxmXEmE84NRxtno6ZlhRMfD8bxToPNiEMsSQCbZ36f6bytJLox_6o7AxsQUog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155545352e.mp4?token=OH1s21KiyTwKt3Dqvo406cibR0Q0z7eBw4fuzsMPN884d6u3XqKZ8YSTfY_e6BYumVXRUrDuVcsX--OnE6VIm1niR4bL20rZQ8o4Lk3bwNAuUAHxRVipXgagxvuH_Y2BcywsQ5Ug6g82JZ2UgNP_gk9VNfaNSyKTzNcn9T4IvztHwzCXdEF8Vr8b-skxom_ETCkYOc3_WeneXj2QI3C6Psm-rLeSBe52RS72sy0coINQXBwOAsEA7hLed40v_MreV7YQByclODQepZaFf_3rvDq3jPxmXEmE84NRxtno6ZlhRMfD8bxToPNiEMsSQCbZ36f6bytJLox_6o7AxsQUog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عطر غذای متبرک رضوی در مسیر اربعین
🔹
آشپزخانهٔ مرکزی آستان قدس رضوی این روزها در مرز مهران بی‌وقفه مشغول آماده‌سازی وعده‌های غذای گرم جهت توزیع بین زائران اربعین در موکب‌های امام رضا(ع) است.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/453759" target="_blank">📅 22:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c8ea306a.mp4?token=cZBRMvUdspbrQnnbaKBpIH1rd3Sly3UIhe--POL4bOfeCYP1FIQFElJwqPyrs3BO1_afmteVfDgQ1Ep7Q1UjlLgkcDCo_qjyMff1ynBHmVmwwPR-d942dVkIClY7FAIV-F-tRY3ppwUj4mxOjeXB14qqeR6kqlUhwVm0RanhfbwNc21Qx-20BpYBXrPgN0wmk-_FDAsCMvcQVyo00ojCWeqg_TRJ5nuDfYtlCyTsZbH7T3h0c1vkI0m8bsQVfGVxidJV5x-ioi8xEPFEVEm_orp1mWtCsKXWfR8QIpiSksdoFTKxDS1gldEWyVJsJafE1lrSMqXwLTmzbaVq5YwFIgHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c8ea306a.mp4?token=cZBRMvUdspbrQnnbaKBpIH1rd3Sly3UIhe--POL4bOfeCYP1FIQFElJwqPyrs3BO1_afmteVfDgQ1Ep7Q1UjlLgkcDCo_qjyMff1ynBHmVmwwPR-d942dVkIClY7FAIV-F-tRY3ppwUj4mxOjeXB14qqeR6kqlUhwVm0RanhfbwNc21Qx-20BpYBXrPgN0wmk-_FDAsCMvcQVyo00ojCWeqg_TRJ5nuDfYtlCyTsZbH7T3h0c1vkI0m8bsQVfGVxidJV5x-ioi8xEPFEVEm_orp1mWtCsKXWfR8QIpiSksdoFTKxDS1gldEWyVJsJafE1lrSMqXwLTmzbaVq5YwFIgHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی مرد عراقی برای ترامپ که در رسانه‌های عراقی بازخوردهای فراوانی دریافت کرده
🔹
در هر دورانی افرادی همچون امام حسین و یزید هستند؛ در این دوران امام خامنه‌ای شهید، امام‌حسین بود و ترامپ، یزید زمانه. کودکان ایرانی که شهید شدند، ادامه‌دهندهٔ راه علی‌اصغر شیرخوار هستند و ما خون آن‌ها را فراموش نمی‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/453758" target="_blank">📅 22:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/132371cca5.mp4?token=R76eK7GoretdnaD8u60LnB2p1pD0IDXNNShU_otDbeh1_miJngrP_nDvttpgkE4VVaLKS9UG5z-j5GhYRLV7_5gq8x0eoTJKffFer3fA34f0ohKRgTWtDBM8CtPpHSf7RAX-Ha7Y-31LKKo_75dvXCrchY41KI-uo1XJT7kTlHOR-c5vuSy8OVDLt-XarJzvIhAifZRnA59vmjH0F1RiMbpYMFiItWOf1ZX_FrCvcofg6jaDBV3Ge7evR9_RRsgbqeIl8a-rDf4l5l0FX785kJp9H4Xz6L173VJdkGrFUVFtd3jkj1-Fm2VUiriqI8hnx-g0d10s5imfk14p7FK2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/132371cca5.mp4?token=R76eK7GoretdnaD8u60LnB2p1pD0IDXNNShU_otDbeh1_miJngrP_nDvttpgkE4VVaLKS9UG5z-j5GhYRLV7_5gq8x0eoTJKffFer3fA34f0ohKRgTWtDBM8CtPpHSf7RAX-Ha7Y-31LKKo_75dvXCrchY41KI-uo1XJT7kTlHOR-c5vuSy8OVDLt-XarJzvIhAifZRnA59vmjH0F1RiMbpYMFiItWOf1ZX_FrCvcofg6jaDBV3Ge7evR9_RRsgbqeIl8a-rDf4l5l0FX785kJp9H4Xz6L173VJdkGrFUVFtd3jkj1-Fm2VUiriqI8hnx-g0d10s5imfk14p7FK2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت زائران از مرز مهران با بوسه بر پرچم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/453757" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453755">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۰۹.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/453755" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۰۸.pdf</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453755" target="_blank">📅 21:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453754">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7590dc25b1.mp4?token=ddUaEccCKgJyfVswQHay66G15FxvJKgLR1MvvAamdUbq1ebr1X-9J-IfFFSDDe89Z8VvDv5ZujdhnLR0o4R4Ao_yppTGuM8IhNylj19qf2MzlvsPyJp_xPWwFQmn9vTGrw3vtJwnFiIpQfd9JIE-_bCAIFTSrkgRjb7PVZX8YdaE_HAnDFsR6VyNZQ_dtRyAgBL9qxH4qBgsXp0XcEDiQt8rnqfHYofz_QnxlSKIuhU6DILFFCzqiO2cF2pHp8eTqd1IN1a1dMtCjdRKIYdTHrujtJLa2_lbp7g8qyeyV_mtS2vpAM8UZEvM7w5lRt4vQtqjoMGQygEIIow_iGsIMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7590dc25b1.mp4?token=ddUaEccCKgJyfVswQHay66G15FxvJKgLR1MvvAamdUbq1ebr1X-9J-IfFFSDDe89Z8VvDv5ZujdhnLR0o4R4Ao_yppTGuM8IhNylj19qf2MzlvsPyJp_xPWwFQmn9vTGrw3vtJwnFiIpQfd9JIE-_bCAIFTSrkgRjb7PVZX8YdaE_HAnDFsR6VyNZQ_dtRyAgBL9qxH4qBgsXp0XcEDiQt8rnqfHYofz_QnxlSKIuhU6DILFFCzqiO2cF2pHp8eTqd1IN1a1dMtCjdRKIYdTHrujtJLa2_lbp7g8qyeyV_mtS2vpAM8UZEvM7w5lRt4vQtqjoMGQygEIIow_iGsIMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط اف-۳۵ آمریکایی در سن‌دیگو
🔹
یک جنگندهٔ اف-۳۵ در پایگاه هوایی میرامار سن‌دیگو دچار سانحه شد و بقایای این جنگندهٔ بیش از ۱۰۰ میلیون دلاری هنوز در آتش می‌سوزد.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/453754" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453753">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515709c4e4.mp4?token=Sx-3evW5GPVBEbxQPZHvg04rbisxLKXBS_7S5hrOzZtxOoiJRKEyR7rRS2wZgaAwLCLdV2RHIvGGeKpvJ3Q160RxhQ4w0EpXCLBmeBAcn4vZQatR9LFIRG1Kpq10y4ydPuE2uXJnwPovdHsAkmIDmkNP2h-Dyqv54JcBqiLB3eZVce6PJZ84DnA3JZJrPcehUF33BDhlqkIuqiMi3arwCDFFYIvda4jnb7LoaipIxHjUiixH1F2I6QnfF2GM7WnsQ4O7wJGVHxUJfZHtsu94hqnYsxTrU81-B_28BRLDEoLPwO4HcTnJRBwU1zp-9vaaKJqcPaMugr9hqkjC7acPNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515709c4e4.mp4?token=Sx-3evW5GPVBEbxQPZHvg04rbisxLKXBS_7S5hrOzZtxOoiJRKEyR7rRS2wZgaAwLCLdV2RHIvGGeKpvJ3Q160RxhQ4w0EpXCLBmeBAcn4vZQatR9LFIRG1Kpq10y4ydPuE2uXJnwPovdHsAkmIDmkNP2h-Dyqv54JcBqiLB3eZVce6PJZ84DnA3JZJrPcehUF33BDhlqkIuqiMi3arwCDFFYIvda4jnb7LoaipIxHjUiixH1F2I6QnfF2GM7WnsQ4O7wJGVHxUJfZHtsu94hqnYsxTrU81-B_28BRLDEoLPwO4HcTnJRBwU1zp-9vaaKJqcPaMugr9hqkjC7acPNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده عملیات هوایی حمله به پایگاه آمریکا: به ما گفتند که دو گردان پاتریوت در مسیرمان است و هیچ برگشتی وجود ندارد
🔹
برای جلوگیری از رهگیری مجبور بودیم از بین دره‌ها با ارتفاع‌های کمتر از ۱۰۰ پا و ۵۰ پا پرواز می‌کردیم.
🔹
وقتی روی پایگاه آمریکا شیرجه زدیم…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/453753" target="_blank">📅 21:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453752">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4c1af480.mp4?token=HVgA3jnTFZdspoOwMjaQH_AeuqFwCHCk5CfTqWL2iwaT2LoLsG6eaeJcdxeCdkNn3HRKPoCbmzIk_ZWFpAkd9bvZKQi5U69AvRUE31MHKWzy9VX3O6v17iopOmvstHK0IRmtZ2E0jxUStRt6bYAQgvixY_7bVLExpnBz0vm6JtZr15fqovlQUOPpLCVKhhd9uhwsakAC7M9yXAgqruzYuhr0f6IoKBr39kLaUrXWeD-GStxjELmGcBbqIN1EE6AUC60cNYW2mEovX60_TK1SUool9ako-6oTr1vyKJug0MUWXgJmBhLVZbRs77yMjkxc9tzl60EPTERFzfEU3LxRlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4c1af480.mp4?token=HVgA3jnTFZdspoOwMjaQH_AeuqFwCHCk5CfTqWL2iwaT2LoLsG6eaeJcdxeCdkNn3HRKPoCbmzIk_ZWFpAkd9bvZKQi5U69AvRUE31MHKWzy9VX3O6v17iopOmvstHK0IRmtZ2E0jxUStRt6bYAQgvixY_7bVLExpnBz0vm6JtZr15fqovlQUOPpLCVKhhd9uhwsakAC7M9yXAgqruzYuhr0f6IoKBr39kLaUrXWeD-GStxjELmGcBbqIN1EE6AUC60cNYW2mEovX60_TK1SUool9ako-6oTr1vyKJug0MUWXgJmBhLVZbRs77yMjkxc9tzl60EPTERFzfEU3LxRlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدون‌تعارف با دلاورمردان نیروی هوایی ارتش همراه با تصاویر منتشرنشده از حملهٔ عقابان تیزپرواز نیروی هوایی به پایگاه آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453752" target="_blank">📅 21:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453751">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
بدون‌تعارف با دلاورمردان نیروی هوایی ارتش همراه با تصاویر منتشرنشده از حملهٔ عقابان تیزپرواز نیروی هوایی به پایگاه آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453751" target="_blank">📅 21:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453750">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06dbcb972.mp4?token=LlCTWUtjcYHCbSs3ErfQ_Ru5ukjuuyFCE533Xg5r-EkwWPidh-8cUjOxm1VBdKGXh24_1fIonCN2YpwancQQcHHUBH67AvTG4qwFhW7jjdmQ0dQJdZVYvBZkHT5x9b3MJCv7hZyB82WqIXtR5QlOqZq9PCmKehLmKVXdTfuM_zVfIcSmtS_UNgj9CrNNwYn2yWELc2vgX_rWenBdIED7yIeI-TyaNhHFAPpOIe8b8LzQvAk8vBAJUjWUbsRm9D2eJX9pbGBc10d3yEuUemKa2kf3b4NwWizPE9UfIN42rJzu-N9vKWJokc5sOqVadwrgvbwXQgoCDyOl96amstQ_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06dbcb972.mp4?token=LlCTWUtjcYHCbSs3ErfQ_Ru5ukjuuyFCE533Xg5r-EkwWPidh-8cUjOxm1VBdKGXh24_1fIonCN2YpwancQQcHHUBH67AvTG4qwFhW7jjdmQ0dQJdZVYvBZkHT5x9b3MJCv7hZyB82WqIXtR5QlOqZq9PCmKehLmKVXdTfuM_zVfIcSmtS_UNgj9CrNNwYn2yWELc2vgX_rWenBdIED7yIeI-TyaNhHFAPpOIe8b8LzQvAk8vBAJUjWUbsRm9D2eJX9pbGBc10d3yEuUemKa2kf3b4NwWizPE9UfIN42rJzu-N9vKWJokc5sOqVadwrgvbwXQgoCDyOl96amstQ_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی عبدالرضا هلالی در رویداد محرم‌شهر
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453750" target="_blank">📅 20:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453749">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA-0xRaeFP74rNKjIzbDWkVTwoL__S0OjZMhaW2I0-Qm6NREFpwiGTq88-V_oNMZFTzKdsNwHLNz1oUd-KRPO_Mhrv14v4aLQkgBxA7bCHAJ_MoaEaOqtzHPSP75TIijNWEVpCJn3phWfsWcnbepuocjcFjOBJEZDRIbMYoGnJkOnqpXte2ChSPBhGl5lnhQPQqkHmnHopbGVH0UeBCV0ya315mdr0v1F9c7y_SA4EoQ2H-cOiv_BYf5eYY7oAVoBW6nZO3s5DKaqM5Rlb8FwJCNy4VEa8oS7HF4RTrv5tt7une9so4QyG3LbV70SU2L0t11a4_31mr5HAaYwSXK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: دولت لبنان باید کاری کند، وگرنه صبرمان لبریز خواهد شد
🔹
حزب‌الله لبنان گفت که دولت بیروت با سکوت و انفعال خود در برابر جنایات رژیم صهیونیستی، مردم جنوب را بی دفاع رها کرده است و صبر مردم نیز حدی دارد.
🔹
در این بیانیه آمده است: «دولت لبنان با سکوت، غیبت و حتی همراهی خود و نیز با امضای "توافق‌نامه چارچوب"، به اشغالگری و اقدامات متجاوزانه دشمن مشروعیت بخشیده است. مسئولان لبنانی گویی صدای گوش‌خراش انفجارها را نمی‌شنوند و در برابر این فجایع هیچ واکنشی از خود نشان نمی‌دهند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/453749" target="_blank">📅 20:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTk_sYWdp4vcvYcR0jEmG6B-QV9F0b8Ip0jDRzJ23aMO3Riin4b-QseyYQgrA5olgiciITZI-l9w6pvbtJanoyVT3YFvv0QUj15Q76oEwYbeVSLEA9XNddnP79x3f3wbnlBESb9ACNOcY_sTGZ5hHiqYS6q5U7q1tnX-WRKBF4OxZ81XtrMOJgIEx_drTXrVsTr8AvSftsCzyqJUSYczsJrEoJ-8xKuYrsW5btjCinD-32SkfaLbGj6U2tdbCIMdZP5OhUbiEGnv7cFjCXVKTUBAGCfjNfW33PPL2Dy5S9eRiYIcNvHcfjzUHUXmVMZ6NbqbyHUREE_IgQ3nkKfpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjzxiWiGlVzOKkmRvx0-5vRk0BA_dlukYAL6qpuqXwfnFma34MryL0igfOHBh1zveRZp2VklNArBkIFofeapMQaOxP2eDtP3QAQpImfpPKOzPff_yJ6qIH7zREZ28kVT6hAEz8aJ-5FlpC51gGIZTbM1lSKwVVKpXjFhHNuZ0C86VIdNW_T8Psl_Rec67L_YFtqEgl7svXdLVtoZ4pIG8KK3elidtJm2RLcYiaxfIFGjQOmNL8162xsFa0aR3v9418Au_DtlhgjgFEXQTImif03dL0ewBKY2oZEX7q1tCXK0f-7HoGAVf_BprK7_8et3t3tB_A51nMn1CSvfqoKuew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcVZXyRENvdFlEWAu2In-9tUL3fLri_ypxqHPRygFzdbKAUKfzxu0a7GR1biSklqc8ENqF8AxMhj_xFH7-MA_YbMp-xMtBXxv1xZ6lhtxo-_pVU5ckU5mIjF-KYVjopmwwuCpoycHd0teJPEOqmt_b9RI72tGq2g5oHkqSQsX2mBcALeubDi2GWZqqH1sHSCLa_gaJjFn5SanYA-FAn5MNXvr-IO38KnT-OVytENFNk7KGoC8Bp7KW_I3syQyoUwWA3GqnTfQvTa99UopggWjVFqCN9EkmJpDdGv6qwr6lx8uT5vdIkhuPdmxnP6Y7-GdnwM9P4pSThBePX13H3ylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dC6UUBHZC_IVEEBcRt6mLfroS3W2WEEZtqhlmDqP-ANU5naT0XoeJ5S8xO8FfKtb4dumxJ27_0uXGBhWn0zjKefV0d9H3qXpR2b4_bSknHdLH2wIsqfIqmLz6r21Qk9CqqHBKZGflMEJIzsOc2I8H0Ecs8FqpMMofXa5NeCS-eXZwG6vec3F--sKAcAX8k9pgT5aaRJLrVu8LgenBorlsUpHurAUt9W1HNFDMXA-MUatcH8YMkc0xG09XYBxp3PbgRzLuejS5w5TUBDPDJTg7UmWNem1KBLekLHCyybLjLhTRqNnOb7G7h1xYQlIeaOgH0UHg98FvVOly16sA8bNEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای بین‌الحرمین در آستانهٔ اربعین
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453745" target="_blank">📅 20:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4de050bc1.mp4?token=JKaoIjygrBWPCVqMHmJjvpNbxpl23oFbtfTlGL4HspGCv-L2I-CgCmbKUdJYhdXjyj5sd-xvOi2UqhxxneHdYdFRBi6z3doEhhlVdKzf1boeOizk7Mne_g1ej8T-D-HbWJO1iUHZsQT4ahvjJfzQyOnE749ssFBz1qCghfhsI5oULaYnTx9MIsqMS7o5Nuz70zIAjVCEjAP_SkZYwvqnBsHzIIzXIO4AlGJ1f5zykQEJKxXQhtRWKwYU5ylGNELTvx9skVKSPprQ0k_Km4j-2MPrt64uaEq2lBwCc8xt0hhwWRobpL70jU0B5jDeNcW2IpLT1UmG0o8p_t5b4wcAwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4de050bc1.mp4?token=JKaoIjygrBWPCVqMHmJjvpNbxpl23oFbtfTlGL4HspGCv-L2I-CgCmbKUdJYhdXjyj5sd-xvOi2UqhxxneHdYdFRBi6z3doEhhlVdKzf1boeOizk7Mne_g1ej8T-D-HbWJO1iUHZsQT4ahvjJfzQyOnE749ssFBz1qCghfhsI5oULaYnTx9MIsqMS7o5Nuz70zIAjVCEjAP_SkZYwvqnBsHzIIzXIO4AlGJ1f5zykQEJKxXQhtRWKwYU5ylGNELTvx9skVKSPprQ0k_Km4j-2MPrt64uaEq2lBwCc8xt0hhwWRobpL70jU0B5jDeNcW2IpLT1UmG0o8p_t5b4wcAwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنار ما حسین، شما کنارتون کیه؟
پناه ما نجف، شما پناه‌تون چیه؟
🔸
مداحی محمد اسداللهی در محرم‌شهر
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453744" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453743">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261429c1dd.mp4?token=t6-4MbOa8_ATFLz82TnDNyR1Pdq9P9y1NcbeR8AKe-q9uksJOyxPzHJ506zL3YZooJOvORb2IrebjtIrkRH0zR3LjkdXmUeTzmsY36nF1h2dIKQgLL7wJZ2RJxxARkMKKdTGfAD8tNBO1IiaaZOHr3xL9nVraFkhHOqYZWtJv9bhTkfiyEr5JE9WyJM-oDeOOIj34QzjW_a_0zkihNsOL5jXJvTes44_9UqHBEWykJp7mee91kWGH3DKiAlgW9qdzjI1ek3Fn0BK3RWyiQzg1UeALH6HbUpdLxyodwKPwGbm_ynuaMRZ58LPDa9JgmIwe02qCgHNFyPdwZYLt4MjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261429c1dd.mp4?token=t6-4MbOa8_ATFLz82TnDNyR1Pdq9P9y1NcbeR8AKe-q9uksJOyxPzHJ506zL3YZooJOvORb2IrebjtIrkRH0zR3LjkdXmUeTzmsY36nF1h2dIKQgLL7wJZ2RJxxARkMKKdTGfAD8tNBO1IiaaZOHr3xL9nVraFkhHOqYZWtJv9bhTkfiyEr5JE9WyJM-oDeOOIj34QzjW_a_0zkihNsOL5jXJvTes44_9UqHBEWykJp7mee91kWGH3DKiAlgW9qdzjI1ek3Fn0BK3RWyiQzg1UeALH6HbUpdLxyodwKPwGbm_ynuaMRZ58LPDa9JgmIwe02qCgHNFyPdwZYLt4MjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ از تکرار ادعای «نابودی توان نظامی ایران» خسته نمی‌شود!
🔹
درحالی که ادعاهای ترامپ دربارهٔ نابودی توان تسلیحاتی و نظامی ایران بارها پس‌از حملات دقیق به پایگاه‌های آمریکا در منطقه به چالش کشیده شده، او امروز بار دیگر همین ادعا را تکرار کرد.
🔹
ترامپ گفت: ما فقط ۵ ماه است که وارد شده‌ایم و توان نظامی آن‌ها را نابود کرده‌ایم.
🔸
ترامپ این ادعای نخ‌نما را در حالی تکرار کرده که پایگاه‌های ارتش تروریستی آمریکا در منطقه هرروز زیر ضرب حملات ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453743" target="_blank">📅 19:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453742">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e5f41929.mp4?token=cDxBxuylvKZTewd76scM8OpTdz4JtidaQUcFajQEwlYUzVyAr60o630dZsOfh9TOzTBe4Ra-13wFQdqzfnyvTCOUoNXSzNt4QlCvOJQrZ-SDOz82X3MmUXNPHaPLZ6t55bi6GOOq8yUc9wov4dKlQyCrYs8xCuIyarFYmdj_Our0TXhRdoVkE7Rco6yreuYAAe7-nZRjv6xrJGu1GBPqBXTAHdu91EOPVSB0PEUfwHrleDZD8ER3R42-42Tra6Tvi4hleu5QxVEbAGrdwQ_yIXK9r5KZlwOd6YCZUqV7R4Yk7lJ0IEsb8xtpyCqXnjgutjKAct2rN2AeqbZzzX86OLRLJgi_d5DlJrPnRKAqZ0lRnBBUqCHlNBz9YsjVgX9JjKJUZAePNGtVqhCsB5q-IeOPrNKsD9i3wqQtJ1-sgM7jO1rAnWYz2P1CJxvdtB-uGmi3bpBW4UstTQhijzbEO6Lw9V57oMIt_nLie7QFxxSskyz9kbAz2izC3PFIhmmilUim0PVnR58foZDjDLhz10zf92G34R_TB_crtmXTin6PH9kmqITrpDkPniooFUDCWcGF4ExEhxWnF6Netv_zRysN230cT7QtpJMUFawfTg57jKg3tBCYXBENuTAGH5cSW9AUEyEBYm6gDM3UKpnlUxRrXqZUW6yfeugAkax8VMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e5f41929.mp4?token=cDxBxuylvKZTewd76scM8OpTdz4JtidaQUcFajQEwlYUzVyAr60o630dZsOfh9TOzTBe4Ra-13wFQdqzfnyvTCOUoNXSzNt4QlCvOJQrZ-SDOz82X3MmUXNPHaPLZ6t55bi6GOOq8yUc9wov4dKlQyCrYs8xCuIyarFYmdj_Our0TXhRdoVkE7Rco6yreuYAAe7-nZRjv6xrJGu1GBPqBXTAHdu91EOPVSB0PEUfwHrleDZD8ER3R42-42Tra6Tvi4hleu5QxVEbAGrdwQ_yIXK9r5KZlwOd6YCZUqV7R4Yk7lJ0IEsb8xtpyCqXnjgutjKAct2rN2AeqbZzzX86OLRLJgi_d5DlJrPnRKAqZ0lRnBBUqCHlNBz9YsjVgX9JjKJUZAePNGtVqhCsB5q-IeOPrNKsD9i3wqQtJ1-sgM7jO1rAnWYz2P1CJxvdtB-uGmi3bpBW4UstTQhijzbEO6Lw9V57oMIt_nLie7QFxxSskyz9kbAz2izC3PFIhmmilUim0PVnR58foZDjDLhz10zf92G34R_TB_crtmXTin6PH9kmqITrpDkPniooFUDCWcGF4ExEhxWnF6Netv_zRysN230cT7QtpJMUFawfTg57jKg3tBCYXBENuTAGH5cSW9AUEyEBYm6gDM3UKpnlUxRrXqZUW6yfeugAkax8VMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی جدید بنی‌فاطمه منتشر شد
🔸
تیتراژ برنامهٔ اربعینی «مخاطب خاص» با صدای سیدمحید بنی‌فاطمه
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453742" target="_blank">📅 19:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453741">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZUselM6OqshQARdbjRbdo_LimDcHASuby9UAURE-dNh86eFqBlw8U_h2tZKKkxja8U-2uYpNjb76ZYv4ogU3KlrKRg_IXonD22Wq1e2gfS-c-_oV-T30XX4M2jMvJfPyO7K1-MzzVh_dGZvWkIyfN5-X__LsoQQ8Xlf3S3cyEZ_XIcA9m70n_W5eUGg37ah6tTB96-aWYLhkYKtlyCy3MoRUchMtsH-ltCPbHsx6ZI_JziebcxeivF_llzQETFlFMhoLht-FbloNBk1nEKOiduD-zkLIA-iCE970LH2lmsB9wjhajVlnnvmKPX-2rf5Nh1tGkhMPJnpzCTq6Jezig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سيل جمعيت در صنعا در میان سیلاب باران
🔹
صدها هزار نفر از اهالی صنعا و مناطق اطراف امروز در میدان السبعین همراه با بارش شدید باران گردهم آمدند و در دفاع از مقاومت و نیروهای مسلح یمن شعار دادند.
🔹
آن‌ها با شعار «محاصره در برابر محاصره» و «تشدید حملات در برابر…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/453741" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453740">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6dfac1cc1.mp4?token=vPpAn27XHwsMq1LwcAF9B1JMu0Cu3Wc2WuZdMVvXBTc9dx1zf7y9RuqfDbBDkS-BE5o_W0Drnss4mckisTQJrcbrMCi8HJmwucuigmpcuMpc6hDdt8olLGvT-Y0PIQ-qUKJ0iLOqq1OQ57attxMmAdmtRCjSPRMwssSWxw26oIDh5aWwIjlgULkE5lSs51DAUyWBmoWOOp7_THc6vjNjJAfDj5L3y6yc9FJabAeEOIlZP3bWLpuptxnVXVwD2sIZZEWmnIUmhKEDutvrJO3NTJ0xD3XDZvA5lrQR-3LOdEUBTknWc6mXtSAkl0FBA0zOd7HSCjl3SFlr-cPXlMz-xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6dfac1cc1.mp4?token=vPpAn27XHwsMq1LwcAF9B1JMu0Cu3Wc2WuZdMVvXBTc9dx1zf7y9RuqfDbBDkS-BE5o_W0Drnss4mckisTQJrcbrMCi8HJmwucuigmpcuMpc6hDdt8olLGvT-Y0PIQ-qUKJ0iLOqq1OQ57attxMmAdmtRCjSPRMwssSWxw26oIDh5aWwIjlgULkE5lSs51DAUyWBmoWOOp7_THc6vjNjJAfDj5L3y6yc9FJabAeEOIlZP3bWLpuptxnVXVwD2sIZZEWmnIUmhKEDutvrJO3NTJ0xD3XDZvA5lrQR-3LOdEUBTknWc6mXtSAkl0FBA0zOd7HSCjl3SFlr-cPXlMz-xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همسفران رهبر شهید...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453740" target="_blank">📅 18:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453739">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3fb4494f8.mp4?token=VZWSrUsSWLZXnmoDkOqDUdoLncpGSX8SkPuQ45b4DKofJkCGftHMiT3N1BWdX28L1NrnGh_TMZe3tG_cVQ5QJbIxFDKQLe7O1VSrxzn23DOFM0ZJNiJQpfGj7XEvmkdqKMLb3sw8Ytu4h359JFzwOe3PSZp_vGvOmM2dCvKdeeGqFlyPuC10G091BGRA__doQiq9LtOmd6DHx8m7d6bQ3VlkmhD0HQRZChXpDA6BW8fVVwAGgZWpwUqhWIzL7duwuOSsb9yvtAcVDVtsbGCuEGFB4lKTENN6PsrMmiap2ojF8wnLIAqE0H8WmfChM4knYXQ8WzKN7suswUBs1cM3Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3fb4494f8.mp4?token=VZWSrUsSWLZXnmoDkOqDUdoLncpGSX8SkPuQ45b4DKofJkCGftHMiT3N1BWdX28L1NrnGh_TMZe3tG_cVQ5QJbIxFDKQLe7O1VSrxzn23DOFM0ZJNiJQpfGj7XEvmkdqKMLb3sw8Ytu4h359JFzwOe3PSZp_vGvOmM2dCvKdeeGqFlyPuC10G091BGRA__doQiq9LtOmd6DHx8m7d6bQ3VlkmhD0HQRZChXpDA6BW8fVVwAGgZWpwUqhWIzL7duwuOSsb9yvtAcVDVtsbGCuEGFB4lKTENN6PsrMmiap2ojF8wnLIAqE0H8WmfChM4knYXQ8WzKN7suswUBs1cM3Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواداران پهلوی این فیلم را نبینند!
🔸
یادبود کودکان شهید ایرانی در حملات آمریکا و اسرائیل در حاشیهٔ رویداد محرم‌شهر
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453739" target="_blank">📅 18:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453733">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0fqyl-NWZQeRSi1_LFXZd-PKY6c_XlYWgUBLRvQKDFIU8xkud2O382lHX2ZZUlZT0b48G59LUFQ0_esegyZ1Cr1rvfv3Sil7aaS3gmlDMOLQKWHz8ZIywxpvKK9cXZRPo54pB3SujvLqTK95DnfNA9lTi1RcqpHObjCN_DBIUSieRrCPrajsbaRotCnxOi0q8urBfn3cHWq-K1iqDCQs1gxfduPEAyJKhJojJpFYsA7Ji2hp2Neq9Uf--ePs26GZK0XGkm5y-lBgeWCafP0hBfYs6sg9LDACgq_eIBXo_PpcyW6reolqXhgsvPFJVBkkYV7wpxxNgJqhqzw6v5LXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnflCH_PsMLeoxlK18ScgoeQuBRKaoIDbfvGOzqBCRUCBdj9hMlUmb7GIYzOCUf-P-e6KgK4XlN-YDpKDVI5_bxtm9eU3_WqLCHiBTIHajEyCnqukpHz08WG3CDo4mz02Ttn3FiOK0Zkit0h-aZckN_7PRPjHxavzAkM6f5mTr2fJ97VVHbUyJBGLjK9xwMKJ1mluDEiO-p9TKxlGxfVr5X5pyqGI--aiLSHTR0012UGTdLBk-uJF35xl4V8lDcOaeKY8qer-ThILjq4zSdPMQZNfW4yFWN8Krr_OEsVqUh0jXf0kTc8r6pPsgSk-bH8WWtOz_y6D5ttS-dpdmVQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jb3Aug3SFu8yeGv-BhAKCLixZKgRNkpuSiUwUOYXj0s1eTcQILu5sJzgFYzTAhAvHGAUYcu3RkFOh8W-AvV5FW_qfkhDh_x1XlbBOKwt9oz8sIOJu7CifdOuRIEcE2swwYsompG7Ou8AxC1NDgs2hdslkhocR86ROeszkv8PvBGEJsh31o0SxNaQs99qg_6bBeu0GOC0sBsc-TMKR-um04gcM61Evs1JIIVcqg6BHjybxtrZrW4tv3Z6eFEQs3JyKWJaRvUCIfTUifs33KjxgQiIIOmhBzh1JfQb1cagDJJ_HGGfJJ3t0YuVVoO5fOGDuZIl4eUdEUT2wqOBRrAdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpTKSGu7qk5dosR507HsyQ2sjVGLy4ekyXmP8VPfBxgM5aYAHv3c-DcTbOovQ4adQN6Nq2-EUDKDvEr24uWL_uXXVWyR0LNQD1-yLPtXx7gdx1wgyJeNaTIBGsb0I8wzNE3PZG_yZuJ2VL6th-H8WDmVSJ2N9jBf73-NK6dW9l2r4Es66q5HKFnk6ShXqp6tjsu2bdseTl_oJST2mbyRQrsxpvCPpP8yB2wGb_RXpAaUaXkg52RzOKL-IAlaOguKxTO9dv7xw5Jh9LcseGUceXKmqUbitjMwtP-vFFxVja2Cgq8D1yfaNp1G4DMH5uSz5rAptz8mmRuzsKxJtUcRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqtLw6x7rmkQQ1gI19t6MFzizB-Qr5gjXZTe2ozLnuizjs-fVChbluCU1slU8vgjq9xcuyrcZu6EtAbxk1kEsjHU3DbMob83j7EDsgzcNgOyFYSjnIZnEb0uDUxpwLznK_5RXOJCx29rRNwGfcrbM8TN9_in9tj3ythFyqiR9HDsqGVx4yg53_UnGajClSjpJAGU1CRYzvu2pL2Sew4hxMg8NRoPXdg6I6DyKE0-_ZaUpT_X40D_DX6Pi_bPpGtkRGb_cZ0P4Pzvc59rVOiOvAZgZvBVsDa_ovLc8-Urebrtzd6nySpdxZTCSZWBcwkwfXf27TN7BuQKWtryQV6Aqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22128b0209.mp4?token=lb8Ee5PufKdCa3hkmeYc-J8OkKeVoBqTvFi86AfH55ytuvvJB0KnqyBUl9FiHk3A9gOjAovjw8gB3DecamwrpBzckzrN8cH3VG9-Nj-xUYbuOSVqBpYAd8pKdm4tXC4Z4g5M8uIzFkUKnZq1KIcduX-OTnr5zmsxokAM5oKkDVB0zajz_SZYoBrmyIqZqwID6FEt6pqTYbkzcoVv1IL6dloGKbD5gUA62n5a_izFctpPJh3SeWw16-826ic3gDXM70b08Zo889lU1ES0aBKiUnY4DHYCykml8sdJPSkC8yBNOH-YlutpHCMO1Vt8j-LsxW_1_1vSc2GtwIUhHpVFGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22128b0209.mp4?token=lb8Ee5PufKdCa3hkmeYc-J8OkKeVoBqTvFi86AfH55ytuvvJB0KnqyBUl9FiHk3A9gOjAovjw8gB3DecamwrpBzckzrN8cH3VG9-Nj-xUYbuOSVqBpYAd8pKdm4tXC4Z4g5M8uIzFkUKnZq1KIcduX-OTnr5zmsxokAM5oKkDVB0zajz_SZYoBrmyIqZqwID6FEt6pqTYbkzcoVv1IL6dloGKbD5gUA62n5a_izFctpPJh3SeWw16-826ic3gDXM70b08Zo889lU1ES0aBKiUnY4DHYCykml8sdJPSkC8yBNOH-YlutpHCMO1Vt8j-LsxW_1_1vSc2GtwIUhHpVFGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سيل جمعيت در صنعا در میان سیلاب باران
🔹
صدها هزار نفر از اهالی صنعا و مناطق اطراف امروز در میدان السبعین همراه با بارش شدید باران گردهم آمدند و در دفاع از مقاومت و نیروهای مسلح یمن شعار دادند.
🔹
آن‌ها با شعار «محاصره در برابر محاصره» و «تشدید حملات در برابر تشدید حملات» به خیابان‌ها آمدن و از ادامه محاصرهٔ دریایی علیه عربستان سعودی حمایت کردند.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453733" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453732">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fsr5NdYMsfqNrec46Yu1KApwC46IlRxE6A9XnFCRvwq-mQDWk5l2Z8PO8P5v5L8IRgccGKdU4DojAKeucfo5OBH0H8LfcUTQH1W0byBvGJR2oi4Vcarhvt-50fH-9Xb-GWPqQH2__9Qfb_Ng6G2P7nEaJRQ3e550SvwBv1WKU0mcfku5Rdd4WQhgtI-198ThjK_gSNvJeoO_RLCgwWABk1OHvasC_SnhaYdr556GeYMXvr9slInfmkRsHGzwmTuZYhA52v4J1_iepDNJxOKy6-cocH0gCzFYPbXLrEuu905oDBq7ThqFRVQnjDAEqh0w06RDkDfF-q1cGBrbshdOrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی با همتای انگلیسی گفت‌وگو کرد
🔹
وزیر خارجهٔ ایران با میلیبند، وزیر خارجهٔ انگلیس در خصوص موضوعات دوجانبه و آخرین تحولات منطقه‌ای و بین‌المللی به‌صورت تلفنی گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453732" target="_blank">📅 17:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453731">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d276028d.mp4?token=kvke8fK7CK_vn5h0eteB33A3AHC_CtMoF5IIrZRjcQexraqcWeYt44ElWCVV7QarOm5owESCE8d0ekrQ1P-CS83lGlq8iJ1DF71QARa5Y2-ONixSI8_jdMAKUVO3ifWFfE1psb-F4ZPVgOGUra1cgn7wB46arl5pfTRVRjsFRfKB8NKJe5M9E8H7PbPsQWYKndpk6b5mddr-RgJO9co9mheJ7WFqKxsNU2lRnoh4Bj-iddqZIgGyrbD91d1Wcv0sSfibmr_eebIvwkhsoJZmAhzbUP2zo6D9sf_YK9FC_5MvhRZ5T1dxcvfuuXReBPAhOSDSFycUp5k1kiX5auezaoQBm5WbrVWIx5Jx7GUQc6lrWmbWu2j9qjFpKCmkoYhfFcQaMziEjHbf3tOxHlcMa0PnXQ0dK04YIyweiSk0R4NFOm-n-RSD1xgdY0cVHOx5zm_pQjnP0vDjqm9WR-VUhMjgDn_yWGDLMGmp8COJw94A2yZ80hZkr5amt4Bcs_gIk4TQCEm3NL6aPEoI54wpq4khauzNyGBJ-CyWVcWJkSLlgeQQ13jTNPXlq4SrqeW82tzXMG_LrzhFSy61AI0rU-9BVuizxjK-_92vCMb-K1R_61LFbbLEvKYSmo8P3PgM4ukY1MZowWOG-0NY8_JY61UgdOG3F8pinWVG2wIFmVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d276028d.mp4?token=kvke8fK7CK_vn5h0eteB33A3AHC_CtMoF5IIrZRjcQexraqcWeYt44ElWCVV7QarOm5owESCE8d0ekrQ1P-CS83lGlq8iJ1DF71QARa5Y2-ONixSI8_jdMAKUVO3ifWFfE1psb-F4ZPVgOGUra1cgn7wB46arl5pfTRVRjsFRfKB8NKJe5M9E8H7PbPsQWYKndpk6b5mddr-RgJO9co9mheJ7WFqKxsNU2lRnoh4Bj-iddqZIgGyrbD91d1Wcv0sSfibmr_eebIvwkhsoJZmAhzbUP2zo6D9sf_YK9FC_5MvhRZ5T1dxcvfuuXReBPAhOSDSFycUp5k1kiX5auezaoQBm5WbrVWIx5Jx7GUQc6lrWmbWu2j9qjFpKCmkoYhfFcQaMziEjHbf3tOxHlcMa0PnXQ0dK04YIyweiSk0R4NFOm-n-RSD1xgdY0cVHOx5zm_pQjnP0vDjqm9WR-VUhMjgDn_yWGDLMGmp8COJw94A2yZ80hZkr5amt4Bcs_gIk4TQCEm3NL6aPEoI54wpq4khauzNyGBJ-CyWVcWJkSLlgeQQ13jTNPXlq4SrqeW82tzXMG_LrzhFSy61AI0rU-9BVuizxjK-_92vCMb-K1R_61LFbbLEvKYSmo8P3PgM4ukY1MZowWOG-0NY8_JY61UgdOG3F8pinWVG2wIFmVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیدبشیر حسینی: آمریکا با ترور رهبری، پدر ایرانی‌ها را به‌شهادت رسانده و ما با آمریکایی‌ها پدرکشتگی داریم.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453731" target="_blank">📅 17:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453730">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5cde0fb8.mp4?token=BWNSN1VxhLMGyBLf2o_eTKPJONePDEMBWxNDNgyhYhMFqEpCVt6NRbxMjjYrzdqhkAmCL3hGg47W0CkXkaokI2lRIU0Xujt8ssN3RSm-TigBUnba1QR2jIvhvhmKsHmcyxXtlfgR-83Ns_alk-S0s6AUH43ZswRqB0832uNklwsZmaVoll0rOHt9pcj0YqqwbbEqsuM5VXd7DW3fS8V85rnWAuk3F1pM74kLByoBO8LJpQrSrgRPTeIhPli_gtGP2s9n84kUywlgYOPhATMnkZd-v9k54yuVIUaWt8HHi5XnDn0HC94JlEdnawkpnESCVoxvatkr85CzM5xM9cz7nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5cde0fb8.mp4?token=BWNSN1VxhLMGyBLf2o_eTKPJONePDEMBWxNDNgyhYhMFqEpCVt6NRbxMjjYrzdqhkAmCL3hGg47W0CkXkaokI2lRIU0Xujt8ssN3RSm-TigBUnba1QR2jIvhvhmKsHmcyxXtlfgR-83Ns_alk-S0s6AUH43ZswRqB0832uNklwsZmaVoll0rOHt9pcj0YqqwbbEqsuM5VXd7DW3fS8V85rnWAuk3F1pM74kLByoBO8LJpQrSrgRPTeIhPli_gtGP2s9n84kUywlgYOPhATMnkZd-v9k54yuVIUaWt8HHi5XnDn0HC94JlEdnawkpnESCVoxvatkr85CzM5xM9cz7nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: هرچه جنگ با ایران طولانی‌تر شود، موقعیت آمریکا ضعیف‌تر می‌شود
🔹
استاد علوم سیاسی دانشگاه شیکاگو، با انتقاد از اینکه ترامپ چند فرصت پایان جنگ با ایران را از دست داد، گفت: ادامهٔ این جنگ موضع چانه‌زنی آمریکا را تضعیف می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453730" target="_blank">📅 17:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453729">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3qJRG7ZKZQ_RYbqPFQAd41Szp3gBK_xiNiyaAxCJvdoX8MtoQNx4QFl4ToKyPfBg1TECLufomDhPqksvv1f2yXlpMaTu2dtHEDzVF-yEQkh_cvceRAB0BDhwgKCerLv6j7tD6XSOtUbqhg7Nm8yFN9Pw2YH9G_udurafwYhM-yki9v3r-y5r2ERPWQNTul9YGQjDnykdcOIsWabShtFX_JJUMldsDHywQPilia8kw2AvIzjwIhUcAvsS0mkgGLfe40hQ_sO89J0oDi9BWkojutE-_5eM-j8s4dqS_iAvNHzIOME232q2nAjVIVL5TAJenzqHGLFUSdw7aCXQe46hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
به‌دلیل اقدامات تجاوزکارانهٔ آمریکا، تنگهٔ هرمز همچنان بسته است!
🔹
نهاد مدیریت آبراه خلیج فارس: به‌علت تداوم اقدامات تجاوزکارانهٔ نیروهای نظامی ایالات متحده در منطقه، تردد از تنگهٔ هرمز امکان‌پذیر نیست. به‌محض برقراری ثبات و آرامش، کلیهٔ درخواست‌ها براساس ترتیب و زمان‌بندی بررسی و مجوزها به‌مرور صادر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453729" target="_blank">📅 16:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453728">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyaip3YLBWKee6IO3YCkMX0JP6Prxww1BMNginC7aZWADBY_XUAHwM1_3TlFuQgYDVoSkiAM1QMWuHMj58DPORmz89EY3nOvEHZ6XYHpcrbJSB5N62DK4M3qJvssOqcxtLgXbXmzfsrLxn5sjd-NqKzNyDUE-kaNq_s8WFSuakC50Rk1IiPOh8StqprGkhJ-i6aMCmN2e3GhLxhEMdJrSGdoLrVeZBZsimV_4hYWS3wIiWlXem1YSfxX-qgZciOd9L6bQxUkoI2PAhz28DWJV3PRqZUROel16aqW7PbL3JfsxGSUJypfHOExbixsheTQ2JqKHWLDWvkbB-1kJ-qhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دل‌نوشتۀ معاون ارتش برای قهرمان ایرانی سوخو ۲۴
🔹
امیر سرتیپ علیرضا شیخ، معاون اجرایی ارتش ایران، با انتشار یادداشتی در رثای سرتیپ خلبان شهید مجید کاظمی نوشته: اسطوره‌ها ساخته نمی‌شوند بلکه در بزنگاه‌های تاریخی یک سرزمین، از دل حوادث، متولد می‌شوند.
🔹
ادای احترام می‌کنم به تجلی واژه مردانگی، شجاعت و غیرت در شولای قهرمانی بر قامت خلبان شهید مجید کاظمی و ۳ هم‌رزم ایشان در خلق حماسه ۱۱ اسفند ۱۴۰۴ منعکس شد.
🔹
خلبان شهید مجید کاظمی از نخبگان پروازی نیروی هوایی ارتش بود که نامش را  تا همیشه بر نیزه افتخار این خاک حک کرد.
🔹
او می‌دانست هرچه بیشتر اوج بگیرد حلقه محاصره موشک‌ها و چشمان بی‌خواب پهپادها، مسیر او را چون خط سرنوشت خواهند خواند اما با چشمان باز به حلقه دشمن زد و هواپیما را چون اسبی تیزتک، در دل اژدهای فناوری فرو برد و نام سرباز ایرانی را بار دیگر به رخ جهانیان کشید.
🔹
این حماسه زمزمه مادران این مرزوبوم خواهد بود در گوش نسل آینده، با ترنم این اشعار بلند تمدن کهن ایران:
به پاس هر وجب خاکی از این ملک، چه بسیار است آن سرها که رفته!
زمستی بر سر هر قطعه زین خاک، خدا داند چه افسرها که رفته!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/453728" target="_blank">📅 16:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453727">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM3L88ObyH5Nt2BUYNn22nC8TlCHRnY90dDa1VmIudQOOpvj1FX5wTVLZjuL4XXJbvkSKzZtIxySMKdrr9KnJoTV7Cj1k3dS3mB9Pc2CY5WihlkjIBQICsruSqdO-aPiFUr6rrsnk-_aaixPXKQ7fttvdzgQh90dIlYNWskXzQkcXB4TIUeG-bXDrCXkIKAnOmOFmk1O_6nylEisamm8yk9llmkGU5BDEGdFdemjfzGCuM2TZwkf9LKr5fyA-I___ArPNn_5jULx810A3iOcw2eUmO8s8M7tLGonwidzE1gNUXsq1EjY_JvvZ2HhQ5PWvwD7jKe1pNAjOuNZVWgEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاتز، وزیر جنگ اسرائیل: اگر ترامپ از ما بخواهد، به جنگ علیه ایران خواهیم پیوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453727" target="_blank">📅 16:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453720">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0FrinV6-m8U0RLIxCx77BPYF8Bo9osugrmkIGleTnXAnJ_F3zYr2rytwuo-rTouFn1XR3luQ9Adaq9Cd9NonZlupRqtUxXDHzDLnd7Pjyg3tbZ2MFpwh86cLywtR7-47MRqTQP4qGn_U2H123gpM2_rcVGhhrK_EVceZIzajIJojidFubACGeSV-lD47GLIRmW-r6faSOtjNUCPRdwhdbpsVxZ2NuejLDValE__Hpk6AeFHPi7ynMPV80LIYqaDSbBge3wiGAbYUZJTCa0SCqq2NkZZBX-vAykNvL0GQVwQOckVITj2Vu84OYRslqvmguTySIIpqXLVsgScF3Lsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hj4pDJ3uuvCaBLHb7kQiy2xxdIwDUsp2pERwLxXZ1haFBFyLhvNtDfb8NnQGdk80AVmNJVhhuz4tD-oLL7wNoAP8mFtK0rn_RekhqEqDKDjCijr2ii_iaww3MtnX4oaz18foWakEjwiN2jF9aODHNLEmcK2JoqaPACewJVj62DyyPsiRPdqMMPowqOqoBwJr_ymK8f6YyxyDjIq37jow_lZuNHrg3hOsk2c5eIO2TXc4TmsHAfN_IHLi0qm4iZSY8RQ9IxMpXKEi7TegbUjRnNcdFg9JEMNSOyp893NeH9ywr14LXF18tsq_P6KnHpddr1D711rSIx1E3oJK8klbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0ubDXNvmsTt57oe6AwLptDSC5lmn7sRHXCMaI5d8P3ORfJiyAjAun2VGm0fbHTe2CcpZLgaO0xdQ06fwg8gRBV-Is4DlfmNGcrqbLTLcNjk9wFmyy_mEnhLO4cg0nxjnsA1to73KAOo7xKLp-oNOK9fOi0PTw27Urbzgjd8JAf7MYxrF_knfGQM6koZZB2j6rZ1_d3wrskJ0EudG3PEWSZD9yPfeJU8OhQ3NNKQg2fJqCUmv6nuI8AzroT15-yX95UPqEVdimwdXsChCt5sXWDxPea6UHhfKF-M_Ere5Yj8NPI1fCFkdiyYs-hORZdEDuF0crH55Kd_qUqVtx0jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpCzjnOZwoOTW1VcIO_iokfEEzgcH4eKxjPGgLDkslZG-2_5UlMpw9jetgi7Y0kIm464oDFqVosokARvyCpQPr-ZPa80EHu2IGfnXcnuhfEg78THoIk-_83qV9rCBqtTyq_Dcp3YNi-iBe5vZj4Ml_s1izEewsL5t7Evl8d5i6GPmbGCiCxkdZMAp52k9z_6iD7RSNpUhcVdKvSxfXhFilnhDcTpeFQEk-Ff5b3Z2GaPSgmEAwTgJTjiRJ2BK6gYaYcJ39kHdjtDhWTzCPZfq8KOKdFg78UCjcx3I0ZT4__eI7tBynadTm-NSeSAhnMrkOiv1NurMdtjn8pxT8gVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxdWkMj-XZwYKNmbBb7zlbPXSQHN37iPmTevNRKc1daEzYmTvAuE6ynyIWZKqvLMWKjV6d0xfKC0kiRCEg7cVNA36RVvFNP6rGmNKhZ7ca8z8K4YlVtPQaBUnjlTs7-cFdvV-DFKI6mHjwTtbxYIU6EvwexYyQfkA0m3hq3xuO03pLeWfT7dYQcXl4pJ60oW6ua5xWhuLO-GZaMplP3r8MS_hUroUhyezEgWkBuoUUNlRTYvW7a2-V43xDOq0sVS3A9oQa6lN1d4h6ShF2oZ_w0_02WDdXUm5NHzGvhzCWU8ybJWQ8Nw59AiB4XuFVWa3WPxu0oucJvpZkLJclBWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oyx31_n2wszL5vxxHONRD-4qkk9EjdeFaBaZqLZmIkf4d776lMBBVzyDoD9aXnv2_Nd1SnG0T-Mi_dlO7YVaD8K38JQCJ9NQcppftaDKL1xbMOZsAvAC_u99w6TImcexKqviD9bPXR0jztS2VyKHvp9Ls93qAPgDdESTC_f0L9pK1CONs0_GDjiEfz9zJ7FzWP0zF6cik9mPBRC0Jj3fRaUxJFiYv810MCMrnu4EcJnCYJHGdiEfs3e_uPn_-UXC9QUY5xW6ZwmszBs4TNuZPtz3SEMXcLBuwazrITj4ezjZFp8depPb45QA6b6cd_TKr_aljN531n6umznQ8tF8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwm-2r0LdXqqNGYiyHq1tjTF1cIoWnuq_LJKjlGN6EmwOqDx2F1Obs5ACUKE5q2ZFg9PGQbDYJLJwLADOYEKUOT4qAZyyctHPzxTo3iJl_EhULNAEN6N0psKvbQdFOtJL-fMqI9pXNsRts2wuylDzgb1DBSmcgPU1L9OSBcWc6tNgf7v2XRypGEjFUDerL4MJ9SdAPKf1BAgL9_q4ySoU0huP17c6EI6ZZDUemPo_l-_zaYzi00StcqsD6I0fMh_XbV0IKNzf-UGLvYTTQO1sqjRVbd1zOoPi2WIe8GoHxdaFUdVGZyFvOPYY_U3QmlgcYczzrL9eiIlT4maO3ufXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد زائران اربعین از مرز خسروی-منذریه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453720" target="_blank">📅 15:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453719">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqh2_vfo1Sf8GO2atxCW1uaeRtsrDyJeZJbW36v3e1PTU5P9LfZK84jTaQsOITRYvkwiQD100WNfPfc3bd2YJJRcNa8mUjrHF81hotBewLkZ9vnsmL6cZBA7BUQ77O5qLG9DMcQLm5nQVjuhraBKNHvMs4NfhhotMO1P_Wr2Mjoiky8cPkQZd24xBPKOAH-Tdfp_CWPwfxpXGEIw44NbSzQ3XWG8TLxtcSouR0RI3TM5vySTyvWpQ4iu1_XCt3ej2p21435ikh9E9v6T08Yvrug0JX_1jy8e9Z0z_IeCj4GzeOVdWLZI25SGBpxcZWnIYQEGrRoBGioitXy43J35Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار کره شمالی به آمریکا درباره جنگ‌افروزی در ژاپن
🔹
کره شمالی امروز هشدار داد که گسترش فرماندهی نظامی آمریکا در ژاپن، خطر جنگ در شبه‌جزیره کره را افزایش می‌دهد.
🔹
خبرگزاری مرکزی کره شمالی (کِی‌سی‌ان‌اِی) در بیانیه‌ای به نقل از دولت پیونگ‌یانگ، گفت که واشنگتن، نیروهای آمریکایی مستقر در ژاپن را به «فرماندهی جنگی بالفعل» با هدف درگیری منطقه‌ای تبدیل کرده است.
🔹
کره شمالی با اشاره به اولین آزمایش موشک کروز تاماهاک با قابلیت حمله به این کشور توسط ژاپن، توضیح داد: «درگیری نظامی در شبه جزیره کره دیگر مسئله احتمال رخ دادن نیست، بلکه مسئله زمان وقوع آن است».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453719" target="_blank">📅 15:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453712">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSWQNedgq0b96oo10Bnu11LYikf5rt_fhboekNeGtDprsDLIBVcF-sdbF8f4AoAiZPplyXqso0lM-Bo_u1bicUdlH8cC_YjNyLqt_4yWN9iUhFyhIOjDHb8l0BrTR2Dab79v08MOgn0UQ9XQ5IWIse247lT5AunqKi-KlTBpmdPhGzOp3oSVKdg1ovjDv72E4h52TVkVJyw5ZvMOx184Nr7VOgQWfcHSHyQ83fCCjRwDDuN9c0KfEvXr19BRTGJTjiKjYKkZQLP5AjgtKTMQRKnLDjed2h4c1DjvT2dL2DQ6dEypQJd8hvzdY6uAhOBqGDADe50HszGxRbLSe055TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0ATSCyiwjJ0tGVXNcmT0BZxCzpUCP06-fNXzQzsY61a2aCcG2L-4dVi52xEOR91URYvtb3mWFya5yDJTnyve9k5dLd0_3ZnqeoZctzC07uzdfyNe20hbQ--W4z4wZ-eZ24fWqDtvzEeIiOuf7IxzaiXpHSR6b4vq2poEqgKdY1v5U-9ghHyP1Yc6xly8bk-DqPPrheYixfnIa4d7sYXMRrioJPtsbRiwdk8eyM1uqnDgJQsk3g02DFvSfJ2bAxXepP_4mBk6VYgsizTecjc4o0nDZAqpM9dSVYO-ld9SnIY3vQIh2I8-mszgUB5cio1a5LRddedClQLMqYgklXIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jpk5NdChYqopPFp0_mZs22f8z_rgjkuYww776ksx4o7QCHVu6e2TXRvtJNQZwpFP-VCwIAcM-_IBxFqVm7TkmaqH9hiEUMIESVCpRca0keM37N3qBydaswo0brD74wSrnhtQCGWxguSXgwGdp-5yUAoIjIr1Eg69OnjBb7nmAfq5JHwvZgfpmyk8LKShfiYNYRkhWEYvYjBgYw_8q0wkv6azZWBBt5XBS43gQp9VYuB2QUxzmk_8Y1TMW4g-RIkRV8EFbQth07wN74Zp0EEEejfvTqUM_1b8CYUxZwBm6nH6irssaWijgdobHMlcmKZ1ZKF9hNxBWLnOHnK5P_6uVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/If-NZ4wZONhbSchv27jaKb9YkQCS2h5eDI5f8hcZJHc_n8y3u2gHK9djfUsVzqzshfrdw2BkksaGfnYNVOdKgMk4HmNTEk-cQAZeLUnXX4oqsQRBK0AxVay_YFQdLNQN2Xi7DF3ko3SmSu4U1aHcPV-Ckwge-c5QBQIlmvIYrw8m-ex_1T1MHstVwR7gCQZinmLpCRkybzEQy-uSuYKUNfRvnTXEUHClLgY75VEvH9v42-Tk1X6wisukGBjBy2BC2S4YUEtr4Z87Gre9Yppwf2iwbaY2WPVlmNTpw91y_niINbKuLnIDIydXeI3OK_7FJGyLB1C1QvR_yF_7_dxE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caiRFPaNVbaUs9DtVH0hSR-OzJth6KZT9orje89WVBBR9ypYCJF2wQCwiU-PJCJ_DcMlnh8Zth5YaiHrr09rL7iNunxbNY_pkKXPuA0l-87ptrRbNPLBoq0U9ofDDHNCsPiIhnC1Kb8i0faVI_UW6QnBQBkWfL_An6xxNb6_aQ8ltcIypaIfs8-laPq9IRE7QuEJmQzAP2dFWBXJjGnsKH2vkeRL5o2Cc3xQs1oyTblnqQWHcxQrdcTSHiJ9kpD0RGGWFNGQGvUlyaYU_YePysT0Tzod36Fp-LTDnfjAdEKXHRhTxZsX3pE5eu40TVAfyDjguYYvcwf0BkNhupq-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjBTiJuQkpfYLVF7vSzdB62hP_0d8mEj_ghJbvNwrjE578hbUTRLmTtbgizO5jiJIsL8vNnkzj3sJB_cEIAqvvASdj3CzGjVUro2MNdtLsabA2JL6UQua8AtdiARNB4f9QwtSxUukGFU1pW380IF3TNig7ssTLQkfV_mdfuVcrLw4Rp1d6Z-MaTE6QHSXDL2dOkaXBNRjaySa4YOEDbBW0iKRgvRjsuaITHja9I4kIGkSWTBN86rvEMxuvbf_AO3ZIBEKjzbEckBPjbBmkD11TeIkz9nNfHDlOpnlm9jMfL6vrIAku1CFnv3VYJ2aaPVaHfx7HboLxgK-SyjyXCX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm6L0UD6RVD5Qb6x-_Eg3VbP4ngYvyhhxFl5q_GeuwgIphreM3z57biiCLd95TeDTK-RDjWlILGNwQwyc1jG7_R9yHmT--3MRxJcOXW_9dF0QeZ5V78E9Ajg45XJDqJfPqQRK0zFRHI5XzgFhu3vj1crbWujIQdXUEJZn7Fa4nP-Pvp1Gxf0vflScwypVMwPShGDikChZqAkiRs6FNNOy6wV_jJtqa-hioLlxX0e8O9pEQUHEuiGR9qN8hjYzPj1Uv6fmqtybcZFkITV7Kkw2XnXN2Su2dxD_dPDk4kW1lFiQq4YmXKqbAGwUs4pskXEGWTdTMNKsm9sT8is5SNdnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیوند موکب‌های مشایه و تجمعات شبانه ایرانی‌ها در مسیر اربعین
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453712" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453711">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8NjwTbWQFpDwHrK7BfjdvE-EfduJS2yZwC3FL4RIcMplrlFc-Bnh1nqln27He1AX7FGAuXcj0zAOvq_5B6RLpZCEfSd_eGMZ79-Np1fndHGTJk2qtyOY6LogNe7aUyewmzI_MV2n4m3_BQBEv9OzRolhvl0x0lY3jrBfXifwzLJA8srSVFwiDkMoHNUFOGhOjppSvHXuU1lh99QaF5U8aFxqRyfCD4GzQMulrhkVor5c-blW_H1h-ebZUt_DQkOgslLRkfEBsd9X6FVHlM9e7LbZAcepipG6ULW_9kPcSut6LPVRBfH78JpJY_iCl0Dw8avw8KBLx2ecA64PJ3cmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایدۀ «محاصره زمینی ایران» خبرنگار اسرائیلی را هم به تمسخر واداشت
🔹
باراک راوید، خبرنگار اسرائیلی آکسیوس در واکنش به گزارش‌های ادعایی دربارۀ بررسی امکان محاصرۀ زمینی ایران نوشته:
🔹
«آیا کسی پیش از آن‌که همه رسانه‌های خبری اسرائیل اعلان‌های فوری درباره اینکه اسرائیل و آمریکا درحال بررسی اعمال محاصره زمینی علیه ایران هستند را منتشر کنند، زحمت کشید نگاهی به نقشه بیندازد یا حتی یک لحظه از عقلش استفاده کند؟».
🔸
پیش‌از این  مک‌فارلند، ژنرال سه‌ستاره بازنشسته آمریکایی در واکنش به این خبر، محاصره زمینی ایران را غیرممکن توصیف کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453711" target="_blank">📅 15:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453710">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-gL92pU1GrKH-0ATM6rQ8lkOOW3ZjifMFYrBICaX2PpHLispqngbVwBMHskx3faG1eztwX3NXHqKFrjbDAKb4X2kcyyAK5tg71yTit87qvOhYzcdJsQFzkjBk3E3W_STi4JyfHeKpRA291vxAzTVh1Lh_tKzbxfW-zG85EI_YFFpVRpKBmZ8fDA-b2XFAKjlDKHnzMJp7t_7eMp71K9DUfgtEYP3xakrgbkuV7_wvStiqJMhOyD-xevDntISkXeBptz5E8YSWaFkK_ykZ2nhrO-rSwKJ03DoBanzPZaBJPRYxUbpBn6ONeSNWejEp24KFI78L4ZNCOzwC_hlb_D6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ارزان‌تر چت‌جی‌پی‌تی از راه رسید
🔹
اپن‌ای‌آی در واکنش به افزایش حساسیت شرکت‌ها نسبت به هزینه‌های استفاده از هوش مصنوعی، قیمت مدل‌های کوچک و میان‌رده خود را به‌طور قابل توجهی کاهش داد؛ اقدامی که می‌تواند رقابت بر سر ارائه مدل‌های ارزان‌تر را در بازار هوش مصنوعی وارد مرحله تازه‌ای کند.
🔹
بر اساس قیمت‌گذاری جدید، هزینه استفاده از مدل جی‌پی‌تی ۵.۶ لونا تا ۸۰ درصد کاهش یافته و قیمت مدل ترا نیز حدود ۲۰ درصد پایین آمده است. در مقابل، اپن‌ای‌آی تغییری در قیمت مدل پرچم‌دار سول ایجاد نکرده است. اکنون هزینه پردازش یک میلیون توکن ورودی در مدل لونا از یک دلار به ۲۰ سنت رسیده و هزینه‌های خروجی نیز کاهش یافته است.
🔹
اپن‌ای‌آی اعلام کرده است که بهبود بهره‌وری در مدل جی‌پی‌تی ۵.۶ و بهینه‌سازی زیرساخت‌های پردازشی، امکان کاهش قیمت‌ها را فراهم کرده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453710" target="_blank">📅 15:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453703">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WSDOeMhtkShOjPMTnvTg20sSA6n6fvEIksLqVrqTdGrS2KrHVIKB1bqfAknhSbpon5azIB_Q2ir79dDnLstTmaHHUG4uqm3It4IrSfXN2OWLYmW1tchAqPRsLCY4kU1PCoVuxE0pzkH5yyixRKYRi5FiKBGcMK0dZUMNBk-y58UsHQm12ZREY4h-2VmBKKNw5PrU2CVImpqd5DbW5ZtMXrGMYNAYIRnaw8fXOWST0QVWsobwdEwK3oUH2qkricusqv_0Pmo1G009Z-XYYtctqc5j59jJ7R4Tm-CuUuAENj09LEQQPqYRxiz85Z2QQ13rpIz9qt3_ymCcUmIeiVeRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RFi2Qujs70QTenRvEWHet7I8Lc1jwDuZ-RVxDP10XLKRYEaDXyEon6HXGSe9KwLDv8V-xBAkCYWKWlGcUo4FPrRoPF5-GB0xyisarmxLdh4AG_odrRywCN2va4BXNtAGrNrSe9hQLdQ8_Tp_-T4dkIuEg4EeNzJkIeQzzapJAEiAiZ8LvxGw-E92KlXH1n5x48Th5bnFVFM7fGgX_XzQqTSmNn4Gc9LAqAwYUk8SNzJYFaVP0A-VQE2qujh5rKoRCJcSFqZpDeFyHlv0voyMU0rRc7bs_OYmmTO4A89T0je1jNg6_nJgdvq9uzrJSh5sb-co8u--XSBtJzX02JYGgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbFrDyP8Y0MmIscAJDuEMGeiKRFTlrP8SLrz_wyqbwW-iIpvT4Ir2DAlUlqxcX5pOor5-1Q0zQD_G8Bc42lEv8UG-6yP8-CZ67eZ3EdGPVm5JdU8TbFCNSaJB60gq1IRITvu6p6lkh7BMJmFD6ehwPD7NZ96mD7j7sZtFas9iz-F7B8SrHBbN0CGzw9aP6dqnSQoTJqVmGRH6OHOMoSgzaWB7Jp_hBhcaMSpXku5vVOK3HBTV0-2X_kNNURtXW8s090PQfYWPuHN1aoS-sbbC1t5DzmkXUNtnEXw6BObLHTXhPa-908rwx6MrO56FRbe1dmFJHmbvCQZgyHHj2_4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6NJe6PQAKHPTC0x4RuGnWtbhREp2DmQoGSsUtsc6M0-R94GS_L1sfH9C1BnELq3qo6npUyTuFuYubCKSSXw2Sxj9yGAWDP8QxYOBiujE1eIzt-6kBZQI1xkuvqYueSVoC6IbR9ZI2jnX2Tbn7v5FrMZSlwDbOTfarZIjoHwfkMgMv7kTn3dgzpWDof_neGdAPjtCC1t2au6Gun7m-6PABO-h153u4853B8prrR5qPWZy13BjEvDqGgi2jkQJOVbmo_oXQOBwyf1KFdIhPmem4AaQtgFP1cyeo5ktejg9FOuGWqJWtrm7rJGd1CzHcn-C_DR2rUlFG-mLCREHo0dyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uj2cE6kG_KY4H1qA5aI_FxIWyMuuIU3yKEbIb0EOyPZkBBJsZEQsiNh7yXJm8SmLTm5cBWNlN-0WgndhS5Cj9QdenJSAwDDiq5T4A1cpthXBUnDU8VztProbokxfRIYGASffNxdbdPL4qjnYIZJQb0qF86TaQeKJ7SJNDG0xD3RO9su550k5apqYp7744wZmFCPJf392KcRgBjcwV3Vy2QnakDkAe4r-CC0P77E-A6OfdPoFe1Ih_VJKjhhvVhmdGWR1m6yEDZq4523UNHuZSytoGXdKdFGk3L7GDUyJC6AlRUGN2xhtKgJpuwQcrupobK-D7Ti9kQcN_UMljh6fcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-CtyO3TnXv0qsr20qMGXrUaURHy4f8HL2ChS0PoLUzySFh0tVC_2t-k_LT73yW0AcIKuGY1HaqHlylZg1qytMMGds54huEcwGWYhZkw5g8WAUBpcCyWti36ZdRwm9OIa3cC9DzBdCy2Ev4D-74TJKxfpccfTCP1qU-9EojCw0F-IwMxotIw5UCfvLFij9y2Ie_JilR9d_gWSz_LzdKA-1zKnDQpbQbJyijD2hHzilj26NxxVv140OsrMV8uQnLPJI_QxNhD1gsyhv1k_3w2e0TKRCuqk3rKz047Q85eiFF2P3HvJIwKryVC29Yj-fZyHdFA5Hw03fOcNF0sgjkbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPV5PkbEwImckttG2fHQFuwfXKg9lq9JUIOxUQaBTdsN7IsQVzRGGyIhzUFfUWkIpDTnLe3RwrsgoRf-wUinrg4yXZ3E8zFvMcQ_LgnpBpa36ESv8RmylljttMdLDbKUrdVlG_txQ-3bSDZl12JvE70xojk_FQfhPp3WlNNFs3zbHT9b--ZENfM8Yi17BfATxKLy_iAP6L9F1YJQY56J4zCH1iNj8YIp1QvEP9DMAf8uqacfx_3OmB5955qypAelJL7DRb2i7Q0bhx-XDuc67WNOEaLzorTgvyHItxmQkw4jtJe2AgJPDt1TagCy56h28rYZAvOuyddtAQOZw_L5Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع ۳ شهید در زنجان
🔹
پیکر پاک ۳ شهید که در حملۀ ۸ مرداد دشمن آمریکایی به شهادت رسیده بودند امروز بر دستان مردم زنجان تشییع شد.
عکس:
عرفان تقی‌بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453703" target="_blank">📅 15:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453702">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247bdfee34.mp4?token=HV9bCfYqugtNQXlnmYq14i9oXlWs7JVoqBEh2vo4CurozFkx2Zp79ygAM0NWKqUsSR2mzOtdgxV-3uzvKbyLtzEYsrC2-20ZpNFCzmNwA76cFwyMi22oY0Bcmrog5Y2SZcT0GECNW7ETQQnf2zcGEnQni6A-2X2lNCAevb58CfaRCSSvcrrgR380UJqntR3DLEIiAqJp5mQeyGVYYvouMgl0rcF76KLAAR4qeKrrGybM1gfbh3ExcnZcptZ6qyOxTMH9hhljgo5aaEJT5-WoU7ENqspKuElqews7RCcQNPvbIO_KvmF94mmzHuW-EXbmnoBwyJ_WhlDDBTBu2KumhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247bdfee34.mp4?token=HV9bCfYqugtNQXlnmYq14i9oXlWs7JVoqBEh2vo4CurozFkx2Zp79ygAM0NWKqUsSR2mzOtdgxV-3uzvKbyLtzEYsrC2-20ZpNFCzmNwA76cFwyMi22oY0Bcmrog5Y2SZcT0GECNW7ETQQnf2zcGEnQni6A-2X2lNCAevb58CfaRCSSvcrrgR380UJqntR3DLEIiAqJp5mQeyGVYYvouMgl0rcF76KLAAR4qeKrrGybM1gfbh3ExcnZcptZ6qyOxTMH9hhljgo5aaEJT5-WoU7ENqspKuElqews7RCcQNPvbIO_KvmF94mmzHuW-EXbmnoBwyJ_WhlDDBTBu2KumhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرگ ۱۸ نفر درپی هجوم مهاجران از مراکش به قلمروی اسپانیا
🔹
دست‌کم ۱۸ مهاجر در جریان تلاش هزاران‌نفری برای ورود از کشور مراکش به سَبته، شهر خودمختار در جنوب اسپانیا، جان خود را از دست دادند.
🔸
اسپانیا یکی از اصلی‌ترین مسیرهای ورود مهاجران به اروپاست؛ آن‌ها برای رسیدن به سبته، معمولاً از شهر فنیدق در مراکش شنا می‌کنند و با پیمودن حدود ۵ کیلومتر خود را به قلمرو اسپانیا می‌رسانند.
🔹
قرار است پدرو سانچز، نخست‌وزیر اسپانیا، امروز به همراه وزیر کشوش به سبته سفر کند تا اوضاع را از نزدیک بررسی کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453702" target="_blank">📅 14:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453701">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
مراکز راهبردی آمریکا در کویت هدف پهپادهای ارتش قرار گرفت
🔹
ارتش: در بیست‌وهفتمین مرحله از عملیات صاعقه و در پاسخ به تجاوزات اخیر ارتش تروریستی آمریکا به کشورمان و حملۀ وحشیانه به منزل مسکونی در جزیرۀ قشم، ساعاتی قبل، آشیانۀ جنگنده‌ها، سامانه‌های ارتباطات…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453701" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453700">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLfwo-jwBCWh6uUPJwztPHud0ENw1Xxc9VAKYyERuulcsYdxtOCFlRvPwrHQtqNsbei5tTQHB7ETnCzwIo_NMNQkbGSSuG7PUubS9xHE02Shm11wNBSVKIVjGCYH6VETUMzZmrGSu8GGKT2KuBORJazU5YBqrRegpgkswZAnrotTAyV3rShonXXMSUVw-tgK0D9U1_7HnF_Z2JsyO-nheoNUCiXdPCM0cD1BbAy_fxZ33wpFrTcmaVqoz07ENAfwoZXPr26tVxJFBqnGUmpsDWXSlpSI2F5NHyTbZWBmjQ1TpfKqOOkU-uv2v4uVIzQuiP8-l7CkwiY53C_Y3zyH2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حماس: فقط به شرط عقب‌نشینی اسرائیل  سلاح خود را تحویل می‌دهیم
🔹
درحالی‌که ترامپ مدعی شده حماس و سایر گروه‌های فلسطینی با «خلع سلاح کامل» موافقت کرده‌اند، غازی حمد، از مقامات ارشد حماس در گفت‌وگو با رویترز گفته حماس تنها در صورتی حاضر به تحویل سلاح‌های خود می‌شود که اول اسرائیل به تعهداتش عمل کند.
🔹
به گفته او اسرائیل بایدکه حملات خود به غزه را پایان دهد، نیروهای خود را به مواضعی که تا پیش از ماه اکتبر در آن قرار داشتند، بازگرداند و همچنین جریان کالاها و کمک‌های وارداتی به این منطقه را افزایش دهد
🔸
حماس درحالی خواستار پایبندی اسرائیل به تعهداتش شده  که دیروز، یک مقام اسرائیلی گفت که این رژیم تا پیش از خلع سلاح حماس و غیرنظامی‌سازی نوار غزه با عقب‌نشینی به پشت «خط زرد»، موافقت نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453700" target="_blank">📅 14:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453699">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_9OBV4TZsxR2M7IQxxRIEYYWfTXZ70vS_vigGk0gwLYdU3kJehwnLkUUyVFo2SP0PriTzH1WZVEdHJe6t1vTuE2WIwlV7yg739uF8uAzZpuE6g0OByKxyi7u6Mj2etqXr6-vcoO6YlXGS2QlbAMcHN33KpMQmZ0blwRsiSNh5zdAyNkt3YVeqW3uvYimFcyAaqhux_pZ7-ax5r-84UWWE-44fD8NeqePEByyP50VAi64EZzYhU4GMizzgRhUfWh_2MYT32aETKkS9flRwliwkHJIIGTsDOTrYxVe-Z_Br-rxvfNA79U63ZxJZZjiIgKcZCpzoSvsMwnD-IZ2WuqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب جمعه تهران: حملات موفق ایران نشانۀ این است که ابتکار عمل در دست ماست
🔹
ابوترابی‌فرد: عملیات‌های موفق نظامی و  اقدامات پیش‌دستانه برای برهم زدن آرایش نظامی گواه روشنی بر این حقیقت است که امروز ابتکار عمل در دستان توانای ایرانیان و هم‌پیمانان آنان قرار دارد.
🔹
آمریکا دیگر بازیگر اصلی منطقه نیست و نمی‌تواند بدون دریافت پاسخ مناسب، دست به ماجراجویی بزند.
🔹
غیرت مردمان جنوب بخشی ماندگار از حافظه تاریخی ملت ایران است؛ امروز که دشمن استان‌های جنوبی ایران را هدف حملات ناجوانمردانه قرار داده بازهم شاهد ایثار مردمی هستیم که همیشۀ تاریخ پیشانی مقاومت ایران بوده‌اند.
🔹
باید با همبستگی دستاوردهای خود را تقویت کنیم؛ نقشه راه اصلی دشمن تمرکز بر کاهش سرمایه‌ی اجتماعی، با اختلافات سیاسی و کاهش اعتماد مردم به مسئولین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/453699" target="_blank">📅 13:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453698">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np2gC3EA5vqnm96MOO8q9nrZXVWb99Z8g5dSLq6-R-cRb2l5JFxCD_Dj9KFH2OurccUQrR36kEe_mFGvk1dXOu6J0quE1MqcYGnQCDyqDte9Txgl33ciB4uYZATCYVmIZ2xDXLewBZelU5h14-h9gUXlCJVkKXQihGv45msn2xfSCilL2DXowXnSRf4rJXQ0LSUvX24nUycz5VkdTNc8qTxD8fJ2GlhVk1nFjt0tSwRD_FQhd-aQSEEwbqhqEAkjEimm2yxdEohFMmLFbXOd7iKqCUcv6qMXqUoPGYyGGuA2ymYbLr37CU5QaPwiRmS2EPLrteQiWEPWDPbdh_Oiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر مجبور به دلالی گاز شد
🔹
قطر به‌عنوان یکی از بزرگ‌ترین تولیدکنندگان گاز جهان، برای تامین قراردادهای فروش گاز خود مجبور به خرید گاز شده است.
🔹
دولت قطر ۳۳ محموله ال‌ان‎جی خریداری کرده تا آن را به مشتریان خود تحویل دهد.
🔸
این اقدام درپی ان رخ داده که بزرگ‎ترین پالایشگاه گازی جهان در قطر توسط ایران هدف قرار گرفت و تنگه هرمز بسته شد.
🔹
قطر مجبور است برای فرار از جریمه قرارداد تامین ال‌ان‌جی با مشتریان خود از هر راهی این حامل انرژی را تهیه کند و با دلالی به دست مشتریان برسد.
🔹
طاهری، کارشناس انرژی می‌گوید که اگرچه دولت قطر خسارت زیادی متحمل شده  اما فرار از بن‌بست تنگه هرمز حتی با راهکار دلالی رویکرد قابل‌تاملی ازسوی قطری‌هاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453698" target="_blank">📅 13:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453696">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۴.۶ ریشتر حوالی شهر دیباج در مرز استان‌‌های سمنان و مازندران را لرزاند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/453696" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453695">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usE2X2B5OJnt3QpAYbo_DQoWqeNrfZENEG3OfhhaieY0hcmVluMSIjbzeQM2kd4NrsaTK7dOXq6awh8bIyfJSyo-I_hjULXXqejmzA64UviTmB81PzJBqw0Wu3HkP3MU2oc2SbErCTuWBJh4AJJg2zNck2dWC_JG85KPe7uqMLA0TL2ij5b38qgUelvhhgFojDNvksX02tXJX0ibcHGOfYR6JuQBi9w4fcv29vVxhcYGd5udnKVgJ7E6S8Sgf3XZtgIOmxxL0Qh9-YlEL48VyssV8s1yo3gddt3KiOCDxDA3QPFV9xjc-EY0NFbQi_NyZ-izQbLhMaCmGZzyBREQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عاقبت عدم توجه به هشدارهای نیروی دریایی سپاه و حرکت به اعتماد سنتکام  @Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/453695" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453694">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19002cccb9.mp4?token=P26p3luvnxuTz88CAlOWOCRCSotXSqqmEG83w65KH00TNnUTVJvD1wD7d0zUjY0p6BnF2CA1LjO3d1vyzUAATfinZHCjFufYvVBGs1InbOmxF6OK67DhB6T8DcfA4gy7ky-4if18snRPwS0ULPNX2iActTsagL9B4NlB5FwMMxNbpeN2Df9zXnNCbqR0Y6q3n8EG0JK-RQNaqdFhktD7bGBKa1BuvgNM5mi0VzlQl5rxB1hPC-ewBslQz0PF28S1NzKlFtJhg8_tTi_pSD674Zrkhw60-rueeH4icDD5f6c_txOGa3UDTZAW5-F6PIWhRA4t0Hh2Drcptnswcqxgig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19002cccb9.mp4?token=P26p3luvnxuTz88CAlOWOCRCSotXSqqmEG83w65KH00TNnUTVJvD1wD7d0zUjY0p6BnF2CA1LjO3d1vyzUAATfinZHCjFufYvVBGs1InbOmxF6OK67DhB6T8DcfA4gy7ky-4if18snRPwS0ULPNX2iActTsagL9B4NlB5FwMMxNbpeN2Df9zXnNCbqR0Y6q3n8EG0JK-RQNaqdFhktD7bGBKa1BuvgNM5mi0VzlQl5rxB1hPC-ewBslQz0PF28S1NzKlFtJhg8_tTi_pSD674Zrkhw60-rueeH4icDD5f6c_txOGa3UDTZAW5-F6PIWhRA4t0Hh2Drcptnswcqxgig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران: ۲ نفتکش متخلف مورد اصابت قرار گرفتند و ۴ نفتکش به سرعت برگشتند
🔹
روابط عمومی سپاه پاسداران: ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/453694" target="_blank">📅 12:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453693">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سپاه پاسداران: ۲ نفتکش متخلف مورد اصابت قرار گرفتند و ۴ نفتکش به سرعت برگشتند
🔹
روابط عمومی سپاه پاسداران: ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
🔹
۴ نفتکش دیگر به سرعت تغییر مسیر داده و به محل خود بازگشتند.
🔸
شب گذشته در پاسخ به بیانیه کذب سنتکام به اطلاع همه مالکان شرکت‌های کشتیرانی و بیمه رساندیم که به اطلاعیه‌های سنتکام توجه نکنید و از کسانی که فریب خورده‌‌اند و دچار حادثه شدهاند سوال کنید.
🔹
نیروی دریایی سپاه بار دیگر اخطار می‌کند، مداخلات و امر و نهی‌های غیرقانونی ارتش کودک‌کش آمریکا به شناورها در منطقه بی‌پاسخ نخواهد ماند.
و ما النصر الا من عند الله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/453693" target="_blank">📅 12:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453692">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJXEzeiCRttNtvwEv0Y8rbS07O2nfay77rzGz9tPTqAgssyMX8deHdlyRh8I-GWPut0-kwcWd42t1woY8YV84bd7qGrP7LjYK28B_wJmgVHaHiG79oefe_ME7fNqcI4N3HL5vdyO02HbEZxQFjUawwuz4APJpxiJZ8i7DVNP4lGcNgC4sjthaIv2Mkff1MI0sp-f1XGfEMpXIBg_HpyGhGAYxqfEc_gMTeOPIkUPepi5JU_odgl-r2QqkG2CCQjir8jIFsbm9oqoGazLYL_OGPMnw23MrgtAW5j8qacBfxcqOii7PP0xTiWLcChoUAmJ-SWeM9HxmHqyHguPJTaAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استراماچونی جای قلعه‌نویی می‌نشیند؟
شایعه است
🔹
روزنامه ایتالیایی توتواسپورت مدعی شده فدراسیون فوتبال ایران هفته گذشته با مدیر برنامه‌های آندره‌آ استراماچونی، سرمربی اسبق استقلال تهران تماس گرفته و پیشنهادی به ارزش سالیانه ۲.۵ میلیون یورو تا پایان جام جهانی ۲۰۳۰ برای هدایت تیم ملی ارائه کرده است.
🔹
بااین‌حال طبق پیگیری‌ها از فدراسیون فوتبال، تاکنون هیچ‌گونه تماس یا مذاکره‌ای با استراماچونی یا مدیر برنامه‌های وی انجام نشده و چنین موضوعی در دستور کار مدیران فدراسیون قرار ندارد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/453692" target="_blank">📅 12:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453691">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHz_QHPzy9j1zeU6iXsQWGzKETf_7Hp4at1ItUd6zP4aDyioZvAg81GWPESQGLrzv4FLLue3qzxQn7Cocy7Few8UPNGTGdP5P12kGJj-DNnMYs1uowzkkllhoXmp0kUKB6q9vmv1ZM-Nv5j-PvHvZ9fmS43XXJpdJTAUegHt3zfWSspAScw4ZCIQTtdJP59MkIiSD4xzCwFPXCvTQ9epTpnyEG61Bu2L16z_TzMNM3A3WmHPeQ8_UZbd5DfqwK2un_iAr4e4R2O5h66LvZ_2uLfxOM5lNkfjtPt1p-IBdTTqYmsCoXnLN6fJR46d815zHgqspJjNUQugrb03WEKkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار ترامپ برای عقب‌نشینی اسرائیل از غزه
🔹
بعد از انتشار گزارش‌های ادعایی از موافقت حماس و گروه‌های مقاومت فلسطینی با خلع سلاح، رسانه‌های آمریکایی می‌گویند که دولت ترامپ از رژیم‌صهیونیستی انتظار عقب‌نشینی از نوار غزه را دارد.
🔹
یک مقام آمریکایی «نیوزنیشن» گفته که اگر نیروهای اسرائیلی بعد از خلع سلاح حماس، از نوار غزه عقب‌نشینی نکند،  ترامپ ناراضی و مأیوس خواهد شد.
🔹
نیوزنیشن همچنین نوشته طبق متن آنچه توافق صلح در غزه نامیده می‌شود، نیروهای بین‌المللی تثبیت‌کننده با ۵ هزار عضو از کشورهای مختلف، جایگزین نظامیان صهیونیست در نوار غزه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453691" target="_blank">📅 11:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453690">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2aba7a874.mp4?token=AfQEwKI5CbcWYE5DMyA19pu-3nI1MeD2iyslbVi8P1NYcstGkvuSt1siKtGW9-H1RE1U5j60SjSubkkb_thFKhxISXvhBFFOOV_TCiwWij_vqOltf0zfY5K_NrwmpX77UPyp_Y3Moj0kGEzqqlFt_-nvtXED30EprOOgMNG1XlZRd8jDiZhdbGDtXSaZXccmJFfGPYYv_9f_q_elBNTJ2Y0cADSCdtXB6AaU4d4ebySQ4aX_CgtePhkqPdwvqjGrU2NwcmyAPy3oNfAKctJt4gLq3Uu2zznG-DrIb1rl5QSCsQkqHd00QJxCFy8akxGVl72zTQgTpbYYncR_ulhQOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2aba7a874.mp4?token=AfQEwKI5CbcWYE5DMyA19pu-3nI1MeD2iyslbVi8P1NYcstGkvuSt1siKtGW9-H1RE1U5j60SjSubkkb_thFKhxISXvhBFFOOV_TCiwWij_vqOltf0zfY5K_NrwmpX77UPyp_Y3Moj0kGEzqqlFt_-nvtXED30EprOOgMNG1XlZRd8jDiZhdbGDtXSaZXccmJFfGPYYv_9f_q_elBNTJ2Y0cADSCdtXB6AaU4d4ebySQ4aX_CgtePhkqPdwvqjGrU2NwcmyAPy3oNfAKctJt4gLq3Uu2zznG-DrIb1rl5QSCsQkqHd00QJxCFy8akxGVl72zTQgTpbYYncR_ulhQOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماد کوله‌پشتی کودکان شهید میناب در نجف اشرف
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/453690" target="_blank">📅 11:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453689">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApFOauNVCK6BT41n_87o5ywEuZs57-VvirTwXStdOHuqlyp2S0KoxmOYQPFN9_QCmGC4RHrFKBNKgjVKbpLzOmUjr0GgEpylg2I6pN52MryPQgKqJnGRbaJvbgFSW5uefXeWcMLqD4sSgj9M_WAJMqYXrq9U5rGs901SQTxZWBOdeK811TIhJycvbptOMd5o0lKVSB8uTeu85Kz5q2O6XtgC8o3il9Uw4dVukt2FqjM_r0vSWu1JYQ7P_RTs2nAHcekgwtrC_GpXo9cQp2VolDPCXFGL2kRGU7RxIyajxS2LoplIi6v5oEdjmQyL0z9nBTgxDLoylDKTI-EBOHqNVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خصوصی ونس با نتانیاهو درباره ایران
🔹
مقام‌های مطلع می‌گویند که معاون رئیس جمهور آمریکا جلسه‌ای صریح و دوستانه با نخست‌وزیر رژیم صهیونیستی درباره اختلاف‌نظرها حول جنگ با ایران برگزار کرد.
🔹
مقام‌های آمریکایی و صهیونیستی مطلع درباره این جلسه، به وبگاه آکسیوس گفتند که هر دو طرف توافق کردند که به همکاری درمورد اولویت‌های مشترک در غرب آسیا ادامه دهند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453689" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453688">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUQvXSP91P0smLm6slyPuzc8RlPbLiOyk22NwpUUOtBKYNWOMNr-fJ-ANSxkI7AdOSLKtCtzOrFSdQ4ETMArmYU6BtwZMx1ksYEWbHNb20visytLKk3IXOEA0oyH3N-Q6WEa4fI0D4ZnYCgU2aTdbq-DaiSbs8DHQqgf68VI8eBfLErI6SvRFX6DJjT8z3PbkYaW6_RQJJt9Nq1wd7vKp7HNakIgMSY1PDyR1qNUeghdmgY177LpLr7LlsfU4c_a0GZ6k63Q4DzcoeBODfGHcPihCxCH6f7YbKDM-TXfV0y4gUM5Ymfs8nThcqw42YihG4HZVCuffmWqXdyUPEnODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان به عون: در توافق با اسرائیل شتاب نکن
🔹
روزنامه «الاخبار» نوشته اردوغان در گفتگو با عون، رئیس‌جمهور لبنان، به او توصیه کرده در توافق با اسرائیل شتاب نکند زیرا اسرائیل هدفش صلح با هیچ‌کسی نیست.
🔹
اردوغان به عون توصیه کرده که سعی کند با سفر به دمشق و دیدار با الجولانی، سرکردۀ شورشیان حاکم بر دمشق، روابط خود با سوریه را تقویت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453688" target="_blank">📅 11:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453687">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff8f2865b.mp4?token=vbJbtODgG_VFdATrtaMBlhu9w9JbGx7V2_0bPa1WbC6lwRFZFW5WQBWHGG-pOF7Okao00z7DkVG56Q-bg2X5IBwwSbI8nTGx2Pcb10jSNvsyf5Z2cwEgoqDr8wRWXtZopeIHw-bJrXhj6XQtK-4gVgo2xYHhehk_aOTRzhSMZyYVzMY_svbvMc5gj5iTMUp5SU8SGqxh2FLgnBMMI9bmFPKoG1gYEb6n9mfD4dobRHWBlbi2NxXGycUR2VonUldPoNfDDxWuJBs4hCNtFtYWlBWq98dWOt0AgIVnC7FWX98hw31atsPUu7B2zleVVOj6J5QX37b5FLx8AMuj50pq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff8f2865b.mp4?token=vbJbtODgG_VFdATrtaMBlhu9w9JbGx7V2_0bPa1WbC6lwRFZFW5WQBWHGG-pOF7Okao00z7DkVG56Q-bg2X5IBwwSbI8nTGx2Pcb10jSNvsyf5Z2cwEgoqDr8wRWXtZopeIHw-bJrXhj6XQtK-4gVgo2xYHhehk_aOTRzhSMZyYVzMY_svbvMc5gj5iTMUp5SU8SGqxh2FLgnBMMI9bmFPKoG1gYEb6n9mfD4dobRHWBlbi2NxXGycUR2VonUldPoNfDDxWuJBs4hCNtFtYWlBWq98dWOt0AgIVnC7FWX98hw31atsPUu7B2zleVVOj6J5QX37b5FLx8AMuj50pq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شریان‌های حیاتی جهان در دستان ایران؛ اقتصاد آمریکا و عربستان در لبه پرتگاه
مرضیه حسینی، خبرنگار اینترنشنال: تبعات اقتصادی ناشی از جنگ علیه ایران جهانی است!
هم‌اکنون به دلیل انسداد تنگه هرمز، اقتصاد عربستان ۵ درصد کوچکتر شده‌ و از طرفی ۲۵ درصد از صادرات نفت این کشور نیز کاهش پیدا کرده‌ است؛ اوضاع برای آمریکا نیز مشابه است.
اگر ایران بخواهد باعث ناامنی در کانال سوئز شود، اوضاع فاجعه‌بار اقتصادی ناشی‌ از انسداد تنگه هرمز و باب‌المندب تشدید خواهد شد.
@Fars_plus</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453687" target="_blank">📅 10:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453686">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بازداشت یک انگلیسی به اتهام جاسوسی برای ایران در پایگاه‌ هوایی انگلیس در قبرس
🔹
دادستانی سلطنتی انگلیس اعلام کرده یک شهروند ۴۴ ساله انگلیسی به جرم به اشتراک گذاشتن اطلاعات مختلفی با ایران از پایگاه هوایی آکروتیری انگلیس در قبرس، دستگیر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453686" target="_blank">📅 10:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453685">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijbzw3R_iDuKWHyYb3u6PGHz_qTZ-RMQXZo9xM0hHHNhm6JQkNqkq4Z0kYJIc9lXUx8h5reqYmknuSuoq9p_36UZCBuDVsB6JUUrIUh1MkgjA9rAmGEeWGsGBzvOr5e0cgN0RDQrGj0xpLDl_ikiCNmE08ETgD0lv3TGc0UHPZpJA3wtO3V-PXDdGUK3NVIO6Rs4OZuRjGm5JuzAld1qmP0K6_OExYn5uHTh6aazdEXpR4P5vwyOQDoPtrKdS4hUfPSeqHCN0MVpZxQzpY8wk8uHIMDE4dlI3JHW49VeQFbAG4Dyzgc4Tfbjk1ILxntDieJtQllon3goVN-PfGdNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار جان حداقل ۳۲ معدنچی پاکستانی را گرفت
🔹
در پی انفجار در یک معدن زغال‌سنگ در استان بلوچستان پاکستان، دست‌کم ۳۲ معدنچی جان باختند؛ گفته شده امیدها برای زنده یافتن سایر معدنچیان بسیار اندک است.
🔹
به گفته بازرس معادن این منطقه، هنگام وقوع انفجار ۳۶ معدنچی در داخل معدن حضور داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/453685" target="_blank">📅 10:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453684">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb9f1bc0e5.mp4?token=haQc0vmuUo3CU8q0CdKbPkroz6Arb34AJmmVGiANp5xVPGUPo5vaXoiVVA-7q9sHvD3r_jj_BXx6tATSbQt_cmIF4nwC7qBRJWy_9chwmbKoopmBFOmtgc-0VbbdTgL_G0Pqany_UJbIRuea3w0X64pyKb6M8Jtr1cjuiTrL5jcwnGpATC3MGRb1mGy0NZ0M7uTLnkcgQLUlhY0K6iOcW0jlNabx35zT45LiMhQ7aURMzsdxPCh0Vra54zhjLNHcaDQgVC1I8deZGhcIM8X1RUCcl3NE0JAV14a23xNnajSPj97XBvPwMQZjGjyruo3EakaPWuofImUlQGyT8DnUOjNvXqG44vbH7ZzPHLTGITUhAsDNkjV27xjOgxI-LxE8ofM5edZMS71wp9onyaGiJPadatuRgScDKb4ZtdbAUN8zbkl0Hqf3IILAK3wWhcBg3xTZG172pVPbWUL5AYsJ7galDPeIV7lDWHm4oDNxT_5_vZ17iByenJwHHcnisGoNUksg3u1hY4WbfgxXOEiz7qjXmZM9ame14szolrbi8RkLlw30nz84eqLCUHmaa8VB0IMZDAD86LY1JWVlj5xEIz2A3I8NlT_41m7E9-dP8lh9njV0h8XJzu79cRXI1zeRK8I7J95sVM-_gDtabPLVSKBd8hWgB7mRvHXBmsJgOmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb9f1bc0e5.mp4?token=haQc0vmuUo3CU8q0CdKbPkroz6Arb34AJmmVGiANp5xVPGUPo5vaXoiVVA-7q9sHvD3r_jj_BXx6tATSbQt_cmIF4nwC7qBRJWy_9chwmbKoopmBFOmtgc-0VbbdTgL_G0Pqany_UJbIRuea3w0X64pyKb6M8Jtr1cjuiTrL5jcwnGpATC3MGRb1mGy0NZ0M7uTLnkcgQLUlhY0K6iOcW0jlNabx35zT45LiMhQ7aURMzsdxPCh0Vra54zhjLNHcaDQgVC1I8deZGhcIM8X1RUCcl3NE0JAV14a23xNnajSPj97XBvPwMQZjGjyruo3EakaPWuofImUlQGyT8DnUOjNvXqG44vbH7ZzPHLTGITUhAsDNkjV27xjOgxI-LxE8ofM5edZMS71wp9onyaGiJPadatuRgScDKb4ZtdbAUN8zbkl0Hqf3IILAK3wWhcBg3xTZG172pVPbWUL5AYsJ7galDPeIV7lDWHm4oDNxT_5_vZ17iByenJwHHcnisGoNUksg3u1hY4WbfgxXOEiz7qjXmZM9ame14szolrbi8RkLlw30nz84eqLCUHmaa8VB0IMZDAD86LY1JWVlj5xEIz2A3I8NlT_41m7E9-dP8lh9njV0h8XJzu79cRXI1zeRK8I7J95sVM-_gDtabPLVSKBd8hWgB7mRvHXBmsJgOmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از روضه‌خوانی محسن محمدی‌پناه به‌یاد رهبر شهید در یادبود حسینیه امام‌خمینی(ره) در مسیر نجف به کربلا
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453684" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453683">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKJx9sYvWkhF0v74HgbCc0dJPqNU4PZ8tjA0abERvNekM4wmZLIXwCTIctAmHWbeDaNAw-MYYUu7m0T-y_4NwdLDelkbK5AYaCksg3XcTs2eG193XT4bZtsv65dxolPQU7YszN-W65npXrwLDTUZtl91SoM0ZVZc6LCNtxq4Rl_TT0o7R112f__Jd2w8ptpb8WOxFWljSTINGwOKQw82PwYqkqLpHe3bAD5VjDXtNNn4pVQcURh-3s7I0nDcKZkoTZjm-cDPYXeKTcH_KVRrUZuNhUXmNmsYkXx5iJNDhK5Z26OmLtibh2UTIzyZ8yJXu8ow4HFHbRDnSzE5yF9yoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطورۀ آث‌میلان درگذشت
⚽️
فرانکو بارزی، اسطوره تاریخی فوتبال ایتالیا و باشگاه میلان در ۶۶ سالگی درگذشت.
⚽️
بارزی که یکی از برترین مدافعان تاریخ فوتبال شناخته می‌شود، تمام عمر فوتبال خود را در آث‌میلان سپری کرد و با این باشگاه ۳ قهرمانی لیگ قهرمانان اروپا و ۶ قهرمانی سری‌آ کسب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453683" target="_blank">📅 10:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453682">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkyQPP2S8R3Tv-8k6a8skiuc3X7npJJ1_W-miB5CVioGIAfypkprf3c3qu0mmrF7Gv-WchZmjuoHATZ0RI_rjvVnNl8hvK6AC6a-8Rz_Kxpk0wBcJpw9aziYmsUQr6kHEcgfwSler8AwhlP8XaAQAsjSQ5zYKByv-4_OpUwU1UztljXVd8ydW0qEgK0JROGzfq1WSrKxwo7tvUbMPPtMtgalpVWqCrxBHASy60rYHAAsXFnAIZdHVWGr-t4j26rnQcW8cYBU034CApW0XlinCsp2vVOajDCZ9B6FS6WE2N7kCG4-iP5j2T-O6NVhQVmfWqHdaKfjPFxUplJzUZ--0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: ۷۰ درصد نفت خاورمیانه جایگزینی برای تنگه هرمز ندارد
🔹
رسانۀ قطری الجزیره در گزارشی نوشته اختلال‌ها در تنگه هرمز باعث شده تولید نفت کشورهای منطقه به میزان بیش از ۱۴ میلیون بشکه در روز کاهش یابد و این موضوع فقط در هقته‌های اول جنگ علیه ایران بیش از ۱۵ میلیارد دلار به آن‌ها ضربه زده.
🔹
الجزیره نوشته  برخی از کشورها مانند عربستان و امارات تلاش کرده‌اند با استفاده از خطوط لوله موجود، اثرات این بحران را تعدیل ببخشند اما درنهایت بیش از ۷۰ درصد نفت کشورهای حاشیۀ خلیج‌فارس راهی برای دور زدن تنگه هرمز ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/453682" target="_blank">📅 09:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453680">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoOlTdtAMwTXWsGip2J4tUePJhjvSITDUxlRcDUBxEL39nf-ZrHFINFYVgwK9Evgmf_VOxLPd0guxAKKHYZarHIPrtvrkbw5neny6GSv7WOlyzzIu4pMvJOqI0aIdX-38GzKHISJyoQX4YvF-ZpmHNl_FR7vD8BCX_a1qhwMdvURyGxhUT-Mn4SkIWsH-tgiApeTUZ1C6xh033Wf0o3jwkC1KpuuMQLDNIuuz-UukvfIab41soSk66VssAu4PrGNcO9EkRRGkK5w2044oOGD40zWAC2fXNHYLtb1eHcanBUObuF5EWU1UMLeIyk-9BljO-Mzm36m58N3TMEyqCFkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عجیب‌ترین صحنۀ لیگ ملت‌های والیبال
🔹
در دیدار شب گذشتۀ تیم‌های ملی والیبال لهستان و اوکراین که با برتری ۳ بر ۱ لهستان و صعود آن به نیمه‌نهایی لیگ ملت‌های والیبال همراه شد، یکی از امتیازات حساس بازی با صحنه‌ای میلی‌متری همراه شد.
🔹
درحالی که بازیکنان لهستان نیز تصور می‌کردند اسپک بازیکنشان به خارج زمین رفته است، بزرگ‌نمایی تصویر بازبینی ویدیویی نشان داد توپ به‌طوری باورنکردنی با خط مماس شده و آن را لمس کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/453680" target="_blank">📅 09:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453678">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c30549b220.mp4?token=aHqSIijIK5Qs5H4ZUZeFiN4ifGW5JjFue1NUysFK4BPHffldeEf7Pn7TORwhW7oj8FSbsNukmSZtIbxe2r6xYdpUd8RNvl6KyGSCLbz3uMI41Uo8Muz3S5LxrERqJkz0rGvLvIlgpgYoBTaCS3xEEB-0-gTRPWoVVUcd8DulGrzaX7d2yq97mRaYan1D4pu_qvCl7t121ixcyd_cBS8USbseZsUnpxVuBuvN0Kzr8jCIrvFcQC7ou9RcHrooTvZiUPEsVjXy9nTlGypvKJf90woKqWdvPwBkm0F9LPSZbvZsF5CsFj1i9SreEM4qCxIviswMDueOVT4yqD5_IKZAPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c30549b220.mp4?token=aHqSIijIK5Qs5H4ZUZeFiN4ifGW5JjFue1NUysFK4BPHffldeEf7Pn7TORwhW7oj8FSbsNukmSZtIbxe2r6xYdpUd8RNvl6KyGSCLbz3uMI41Uo8Muz3S5LxrERqJkz0rGvLvIlgpgYoBTaCS3xEEB-0-gTRPWoVVUcd8DulGrzaX7d2yq97mRaYan1D4pu_qvCl7t121ixcyd_cBS8USbseZsUnpxVuBuvN0Kzr8jCIrvFcQC7ou9RcHrooTvZiUPEsVjXy9nTlGypvKJf90woKqWdvPwBkm0F9LPSZbvZsF5CsFj1i9SreEM4qCxIviswMDueOVT4yqD5_IKZAPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیشترین پرچمی که در اربعین دیده می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/453678" target="_blank">📅 09:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453677">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae415fca5.mp4?token=obGHXmA4TItz6Fjxiu7bOmmEv_W-K0kjUacszV_2XTGs8FCSLIi_ssseSFj71E3vow6DE9kqUZMj0ZnCDJlUW-uoIn33PL7aUqVWtZUA3TaxXRJAUCjr5P0vJb0TZXvv6uHpVHLwKjIi5UTnvefCa0891TuMwKQwBphza-FkLvUsmH1lizULg_Q8fZ17ikklV8KSvMRrpxIITqSJ9tcOiuKyOgY-zyDzG_OBrM6-o0FHsEYZn92f84ZIAwFo4Rwx5-207RE5zRB_vvhIjl-TvwoS8EBRXVplpdFIWtBlIR4FbCi72aVb-fHCXQaNGc0WHxEK31GJ0OPysEThJcK4C4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae415fca5.mp4?token=obGHXmA4TItz6Fjxiu7bOmmEv_W-K0kjUacszV_2XTGs8FCSLIi_ssseSFj71E3vow6DE9kqUZMj0ZnCDJlUW-uoIn33PL7aUqVWtZUA3TaxXRJAUCjr5P0vJb0TZXvv6uHpVHLwKjIi5UTnvefCa0891TuMwKQwBphza-FkLvUsmH1lizULg_Q8fZ17ikklV8KSvMRrpxIITqSJ9tcOiuKyOgY-zyDzG_OBrM6-o0FHsEYZn92f84ZIAwFo4Rwx5-207RE5zRB_vvhIjl-TvwoS8EBRXVplpdFIWtBlIR4FbCi72aVb-fHCXQaNGc0WHxEK31GJ0OPysEThJcK4C4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ‌جا کربلا نمی‌شود
!
🔹
روایت دلدادگی زائران کربلا را از دریچه دوربین خبرگزاری فارس ببینید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/453677" target="_blank">📅 08:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453676">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae919478b.mp4?token=fFbxQkZ2OtWfWsQXmJku6UEc6VfSP4AntLc8jiuHmBzg-IYcVm7CypQptKp2lNH3Yuup_fE6v7wFGizPTHN9yj03ta4U4W7UVWsw9zTBg_2WUyDU16OrIgDLUyIdrH1AhhI5j8bmZa3HGLvDYq_krrcUT1zLAYxWn3UsjbADA8gPcxQtvPGtNFIrhkut5IYOrax6EYXZh04IHaALWKR5d5g6rrAniIx8hGw8H3jFEVVrpLHBoZF4krMAkV_cbICYjrStYak1ReQUe3kj37kDcaxe4jCC2zND7WgTjk56i6nGVhTqKAiv6ulkWCjGBgekf3L1NbU3Fji9yIlguYDrIDfK7ANQQKypkHDPXiKKUINc5Wz0yzt4jAGpalJ4a04pBRms4c7bmec4XayjHOqdMbG6hjGN7fUXe1oOfWNXSHk3Tlf8qjw6mr4Qtz1UIwmteb0uDBT-PSyB7T2V4dJ9MJwVLM6y6jcyZAurIQi_v880Q9E50WIYbbS5uQbXq5vz6c12ACcTC7wCF2HgcImIGbux2W0XtetawoIiICv4wt-6w0AWdStFdCknrCzuC0bGPrwdz9Rf1b3XpLPx4lN5e7KDHViQCmgvIvjA5fbmrYi_noLZSxemXquEb4mPk9dOg4U6tDpBHiHr87YWGO75t7YmCkB5NK8ehkEC6eH2QOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae919478b.mp4?token=fFbxQkZ2OtWfWsQXmJku6UEc6VfSP4AntLc8jiuHmBzg-IYcVm7CypQptKp2lNH3Yuup_fE6v7wFGizPTHN9yj03ta4U4W7UVWsw9zTBg_2WUyDU16OrIgDLUyIdrH1AhhI5j8bmZa3HGLvDYq_krrcUT1zLAYxWn3UsjbADA8gPcxQtvPGtNFIrhkut5IYOrax6EYXZh04IHaALWKR5d5g6rrAniIx8hGw8H3jFEVVrpLHBoZF4krMAkV_cbICYjrStYak1ReQUe3kj37kDcaxe4jCC2zND7WgTjk56i6nGVhTqKAiv6ulkWCjGBgekf3L1NbU3Fji9yIlguYDrIDfK7ANQQKypkHDPXiKKUINc5Wz0yzt4jAGpalJ4a04pBRms4c7bmec4XayjHOqdMbG6hjGN7fUXe1oOfWNXSHk3Tlf8qjw6mr4Qtz1UIwmteb0uDBT-PSyB7T2V4dJ9MJwVLM6y6jcyZAurIQi_v880Q9E50WIYbbS5uQbXq5vz6c12ACcTC7wCF2HgcImIGbux2W0XtetawoIiICv4wt-6w0AWdStFdCknrCzuC0bGPrwdz9Rf1b3XpLPx4lN5e7KDHViQCmgvIvjA5fbmrYi_noLZSxemXquEb4mPk9dOg4U6tDpBHiHr87YWGO75t7YmCkB5NK8ehkEC6eH2QOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله صفایی بوشهری: قصاص جنایتکاران بزرگ وظیفهٔ همهٔ مسلمانان جهان است
🔹
هر مسلمانی که شرایط و توان این را دارد که قصاص خون رهبر شهید را بگیرد باید دست‌به‌کار شود.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/453676" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453675">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmIi4uEO_hciM9oqdyUm7YVPr0e5bAFfBf8EegpQCnKx2b8Y4gl3-t6W-PYnT_fmuyan6HkdoBLaJzWJivLlUooKUMf6yYw8F7Efumww7byAp2VDpeurljqXTqO5x08InWMGPUQZBON3IzeSeI20lYHslmIBOrR84YrjWxWjvEXmoFNQDc38CiVP4jmEzS0tJQL1Iv-q4t8SvijEVEZWZw5kugOYtWJy10ybjxWHMPutaN2Vxjpr9AvBrEMeS6FV22vvTLBYA7fkPw86lAbcbISzG-I9HJMFeBTvqNomjMAjjYPDDw87mDQjctnL7ScW63kJHF0A_bt8rgyL9_y-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان سفیرش را از کابل فراخواند
🔹
روزنامهٔ «نیشن» پاکستان: اسلام‌آباد در واکنش به تحولات امنیتی افغانستان، سفیر خود در کابل را برای انجام رایزنی‌های سطح بالا فراخوانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/453675" target="_blank">📅 08:26 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
