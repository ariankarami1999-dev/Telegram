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
<img src="https://cdn1.telesco.pe/file/KX0vzHgzK93zAOZQFHggn1j83XIK3-YbSRYOr9_3Kg--LFAlvQiu0pozo1IUJ_zbiwLrJLwSODycToMuyQT8knprX3Gy2bvx3BN_rU_h5-ApJw98ZntarTFQbOv_7oITlR35l7XWDGEUeXTPbG6je19im_fDAMWOgK1L8FnrflhKWn2VFtgOK2xLviYwGxARR-kgDK6LLnCkDrujZ9IYS9OzieXU8MeIBhJMVMyTbNCeECYAXGS3W2--uz7zeyJHi_L-Y-mDE3TTDLvQS5vBj6quZl8FDZj6-O6SthkZg6Kh_GjSFqVMJ8u8i5whRGENtnH02vOjP3JDOjik98cA-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 14:19:37</div>
<hr>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FBLI5oe941kVaiXfj0DFFxA0oaYPrH3QgjQAi8SaSW_g7sfZU9UuWlIF6wpJcsgheljBIk8INNwJJYGc7-fq62ekYK6_tQcTqe7d4BJDKKWC-ZkkRkzArwR5Ev4o9NmZZUoreDIB5Iz9EnRfh64l4cj_aw0L6SVI82LuKbamnWDgxiWtv8Ge1iIFNkGsNG_QRscOo7lIP9DFDYbC5zii-vbLsQAXJPXHJFJOXJKBglMR3E9wiVlJA8UdV1wnRylo10JYYGck-SUs2dEw9GU3133ED81voaiHHMDv1kxHCY0Vp6ibpodkAHiHqOLTQa15v4ndO-VSjF4QJn_Qt86ZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WlQ8_1sn26p7m3MC6bzPC3Ss0zBzV_bT0TFlXxRqpi_bEc5kmL21MtyPQykf3OloVwu62F8HamR1Q-HgPA3fNrzODTp3xrGfgk47mXq4VFpBhG3BCiJcZb4UcTnp9savDUT22pIa5MhA0urXtiE_ZAVuKaTPxlAA6_siXYLMBu_vzkFXDubvQ4M9gr4AmHgo8d9QNdVB2ikAmeNnePBmPPMZuK027ALenMQ2dZfz_sMayR0SwXhOXGd3CZGYnXrFERqbZktd-w5A-pFh2KbQDm0DVBYd7PMGa3DY4NtYBY9uT6J3FYgzTn1qBmp3tm3-aT5JHkGSfydrNS1866w7UA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واشینگتن‌پست در سرمقاله‌ای نوشت توافق با جمهوری اسلامی و تزریق منابع مالی بیشتر به تهران، به رفتارهای «مخرب» این حکومت پاداش می‌دهد و زمینه‌ساز دور تازه‌ای از بی‌ثباتی خواهد شد. این روزنامه از دونالد ترامپ خواست مذاکرات را متوقف کرده و سیاست مهار جمهوری اسلامی را ادامه دهد.
هیات تحریریه واشینگتن‌پست جنگ آمریکا علیه جمهوری اسلامی را از نظر راهبردی ناموفق توصیف کرد و نوشت این درگیری نه به تغییر حکومت انجامید و نه توان موشکی و فعالیت نیروهای نیابتی تهران را متوقف کرد. به نوشته این روزنامه، هرچند حملات برنامه هسته‌ای ایران را به عقب انداخت، اما انگیزه تهران برای دستیابی به سلاح هسته‌ای را نیز افزایش داد.
واشینگتن‌پست همچنین نوشت تفاهم پیشین میان واشینگتن و تهران نتوانست اختلاف بر سر کنترل تنگه هرمز را حل کند و ازسرگیری حملات نیز تغییری در واقعیت‌های میدانی ایجاد نکرد. این روزنامه با تاکید بر تاثیر تحریم‌ها و محاصره دریایی بر اقتصاد ایران، پیشنهاد کرد آمریکا به‌جای توافق، فشار اقتصادی، محدودیت صادرات نفت، مقابله با نیروهای نیابتی و سیاست مهار جمهوری اسلامی را ادامه دهد.
@
VahidOOnLine
شورای سردبیری واشنگتن‌پست در مقاله‌ای با اشاره به موثر بودن سیاست مهار حکومت ایران و اعمال فشار اقتصادی و محاصره دریایی و در مقابل کاهش کارایی کارت تنگه هرمز در دست ایران، استفاده تهران از این اهرم را به گروگانی تشبیه کرد که از پیش گلوله خورده است.
در این یادداشت آمده است: «تصرف تنگه هرمز از سوی ایران را می‌توان نوعی گروگان‌گیری دانست، اما گروگان از پیش هدف گلوله قرار گرفته است. بازارها عملا بسته شدن تنگه را در قیمت‌ها لحاظ کرده‌اند. قیمت نفت، هرچند بالاست، اما فاجعه‌بار نیست.
علاوه بر این، تأمین‌کنندگان نفت در حال دور زدن این مشکل هستند. دولت ترامپ مدعی است که اکنون روزانه ۵ تا ۷ میلیون بشکه نفت از طریق خطوط لوله ارتقایافته و پایانه‌های جدید صادراتی از منطقه خارج می‌شود. عربستان سعودی نیز در حال تشکیل ائتلافی چندملیتی برای حفاظت از کشتیرانی در دریای سرخ در برابر نیروهای نیابتی ایران است؛ اقدامی که واشینگتن باید با ارائه پشتیبانی اطلاعاتی و فرماندهی از آن حمایت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/77858" target="_blank">📅 05:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QDY7v2491Qln3Cpw5E8E-QanXBU_EAk4KuvntVDNt-VLOdJbvZyNM5WIsogEP3p1H_koiTUVqBEAw7tiUM_jNq0e_pTUJaVItslwZxKg3XHVkP3PjvPcnHydD6VrdMq_iDqeqEKt6DPvAwS0MwIkwghvWeoqyjRbafLraS-6EehGuqLICPpaVAHN1-d42YJhlHfdV-qc1tHsyjA7Zj_royHhAVdr3BBJA4-xbcmryzTyuhWMTpm5b8UPZhbsSw-rNRIuGZLxBiPuUvioRxoZMjW2gJurNiqwx4PK7pgNGtWvNVZGpKDgBqyXQAVkFw2QRopQ6E23Xn_9rmd8kV2oKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان سعودی (واس) گزارش داد شاهزاده محمد بن سلمان، ولیعهد و نخست‌وزیر این کشور، جمعه ۲۳ مرداد با دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده، سنتکام، در جده دیدار کرد.
بر اساس گزارش واس،  شاهزاده محمد بن سلمان و برد کوپر در این دیدار درباره همکاری‌های دفاعی عربستان سعودی و ایالات متحده گفتگو کردند و آخرین تحولات منطقه را مورد بررسی قرار دادند. دو طرف همچنین درباره تلاش‌ها برای کاهش تنش‌های منطقه‌ای و تقویت امنیت و ثبات گفتگو کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/77857" target="_blank">📅 05:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mkTGALm4gepwGgNLGZmDDy8lmlHiWyzEtxuHf97JHUcTrOmxEfEjDAMv4V_7KlOgw-9la8QqccaeiLOi6Rz6-Mr8wG9Snpj75bAxrErKlNHW-2Fm9rX7iLK4zSa_RD6gnI45SpkTo6XFlX0mzWyWBPt90q4FzU0tr0ao86h1d5iV_AKwYggmBDGZSn9D6yQzx8JnE_gQtO8WplyiFnNKU18yNLmbvfm4HBd6dzM7xMk2b7y1ItZhJZjjpc4D6i0iEqmvozuzdpxhu-QKbZwcFz4Nzv_ct59Jxbxe17qz1VVC5JNBYIYh21Vg71zRENiSTIVV9TwmEv5JVoHUDbXPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون رئیس جمهور آمریکا درباره تنش‌های جاری میان کشورش و ایران به شبکه خبری فاکس گفته است: «می‌توانم با اطمینان بگویم که به اعتقاد من، آمریکا در نهایت دست قوی‌تری در این ماجرا خواهد داشت، ایران سلاح هسته‌ای نخواهد داشت و وضعیت تنگه هرمز هم به گونه‌ای خواهد شد که قیمت‌های گاز و نفت برای مردم آمریکا ثبات پیدا خواهد کرد.»
او همچنین گفت: «مسئله اینجاست که ایرانی‌ها گاهی تعهداتی می‌دهند اما به آن‌ها پایبند نمی‌مانند، توافق می‌کنند اما آن را رعایت نمی‌کنند.»
معاون رئیس جمهور آمریکا اضافه کرد: «متوجه نکته مربوط به ماهیت پر از نوسان و بی‌ثبات این موضوع هستم اما فکر می‌کنم ما راه‌ها و ابزارهای زیادی داریم که اهدافمان را عملی کنیم. اما گاهی تمرکزمان را روی موضوع انرژی می‌گذاریم چون می‌خواهیم آمریکایی‌ها از پس قیمت نفت و گاز برآیند.»
جی دی ونس به فاکس گفت: «طبعا گاهی هم بر جنبه نظامی موضوع تمرکز می‌کنیم. گاهی هم توان خود را روی برنامه هسته‌ای ایران صرف می‌کنیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/77856" target="_blank">📅 05:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vCyhu06emU3YTQ8Gz-bkQBdMj_soXj6P79SJRfvUvwwSkiD5HFUzzjJu1pwlLovAVm1QeHeRd5mNlCffeUvixX6sg1iJ2MyRk9Mw7VncXn72fuXF3OAtdVcnR3yl7PwycXnusdY385QjIRGWaWMyn4QX2BfN9CjRex_KsbUIAYo2-viakvCMQl7TDM25jIqgv0s4J0RzH3IL7e0tjKy7XXz0DOn0nt0WwQRTggThHr84y6rhNA6kcUJmricuGwe2QX6DYFW4yS3RE6IwBHUcuYBlmiDekI-_h-cABdloWk51Mo7u8Nn2xGZS_V2UpcpcZANPrWk4q1a3Mxp8I57P6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پیام‌ها از زمین‌لرزه حوالی اندیمشک و دزفول در شمال استان خوزستان خبر می‌دن.
آپدیت:
تصویر و پیام دریافتی:
بزرگی زلزله: ۴.۵
حسينيه، خوزستان
عمق: ۸ کیلومتر
زمان زلزله: ۱۴۰۵/۰۵/۲۳ ۰۰:۵۳:۴۷.۹
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/77855" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PT5-f2UuZZ2lXyoZ9QdOLybrRl6SiekVZDsGHY6i0eGbbmpsDGsrkpyPXqrbZTlSFF5dAbqwmrk4iU_JvkMfNihYL8xtqewckRrWRyKbsPKr2ejBFNe8CenIBHkH2xrR_oQJUPxqe-sIjfeNaI-nuqS0xvkKDKYjtiK0XWpPEqtFFSLnn6y5jgekdO7MZGAg_e7XFDNxxfA9JDM0ClTOv-itcHjC3JhWk69ATyAbg-x8XwDlqFoAxbkKmivQU5OxDVyblHXo1zYGdJsz8IOx46fJup6Kq0BPSzkRK1zEqCsyF6kXk6MCVN7u2VbMK4B15uLeXLyjpH3TENcFxrrm7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، سنتکام، روز پنج‌شنبه ۲۲ مرداد از آغاز روند تشکیل نخستین یگان چندملیتی و چندحوزه‌ای پهپادهای تهاجمی خبر داد.
این یگان با نام «نیروی ویژه فالکون استرایک» از پهپادهای یک‌طرفه تهاجمی و سامانه‌های بدون سرنشین هوایی، سطحی و زیرسطحی دریایی استفاده خواهد کرد و نیروهایی از آمریکا و شرکای منطقه‌ای در آن مشارکت خواهند داشت.
سنتکام اعلام کرد رایزنی و دعوت رسمی از کشورهای شریک در منطقه برای پیوستن به این یگان آغاز شده است و با پیوستن آن‌ها، «فالکون استرایک» توانایی‌های پهپادی تهاجمی در خاورمیانه را در قالب یک ساختار چندملیتی و چندحوزه‌ای ادغام خواهد کرد.
«فالکون استرایک» ۹ ماه پس از تشکیل «اسکورپیون استرایک» راه‌اندازی می‌شود. به گفته سنتکام، این یگان پیش‌تر از پهپادهای یک‌طرفه تهاجمی در عملیات نظامی علیه ایران و همچنین از شناورهای بدون سرنشین تهاجمی در حملات ماه ژوئیه به تأسیسات بندری ایران استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77854" target="_blank">📅 21:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/scnZLdw9x-fDdhfjhZB3IT0HzSKJz30tONRQYETqKrS2zcjDHF220MCaGZggVWSCGzSi98JQpYCFKXHKYSyDxycpIRoZ6_51L9urU7ZWZqF0kEaxyrqlC_JeNmhDHJWtqGn9lD5lGDdbU3GaoqlJfDmmN1KDYNzAGTlkIHzoJ9iQBnHcBxY0cmMU_MVsb5sBZ-f0hP2Wjopmmn_tOgxT3BhgEEc7I5GGKfUjQFDP4hilg9v6v23DleJrBXFGhCquEQNUt8I2o6F6U41_zDfMuKCAWJv8DHtVV76eiCv2dXr71JFlEAukWA3q7RBsj62KXGlFdeOPW7ybbkCP1Dko8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها چهار روز پس از یک حمله پهپادی به بندر جیزان در عربستان سعودی، خبرگزاری وابسته به حوثی‌های شیعه یمن روز پنج‌شنبه از حمله‌ای دیگر به پالایشگاه آرامکوی مستقر در این بندر خبر داد.
در حالی که هنوز منابع خبری سعودی در این باره اطلاع‌رسانی نکرده‌اند، خبرگزاری سبای یمن نوشته است که این پالایشگاه «با دو پهپاد» هدف گرفته شده است.
روز یک‌شنبه هفته جاری هم این پالایشگاه در پی حمله پهپادی حوثی‌ها دچار حریق شده بود.
جیزان در ساحل دریای سرخ و در نزدیکی مرز یمن و در تیررس حوثی‌های شیعه یمن قرار دارد که از حمایت جمهوری اسلامی برخوردارند.
آرامکو روز پنجم مرداد پس از حمله حوثی‌های یمن که به مجتمع سیکل ترکیبی یکپارچه گازسازی (IGCC) و بخش مخازن پالایشگاه آسیب رساند، فعالیت این تأسیسات را متوقف کرد.
حوثی‌ها در آن زمان اعلام کردند که تأسیسات آرامکو در جیزان و ینبُع را هدف قرار داده‌اند.
پالایشگاه جیزان ظرفیت فرآوری روزانه ۴۰۰ هزار بشکه نفت خام را دارد و فرآورده‌های پالایشی از جمله بنزین و گازوئیل با گوگرد بسیار پایین تولید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77853" target="_blank">📅 21:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qcMwny98MCCaxPpNH0SbKH80iOWpo5m5q-Do3bUiLJcGhGTMLShKfJT2t1Eixe623sp0asT2G2mTgaSt7mxj2Pn-m-RRMyTm9RRvSa_ptjc5o3IfOCxh3_uVA8y1HDT-PofmAzDh1uKrteHoFkxLe4aNpt6DW_7mWDBwmUW8pSgzzc_JIs2_CXZAkAbZkrea3icBAvlLnYr11Q1DqLkCOe-a7WzRpKAkrquOQ7vgUBKr96kha4k-8uv9kl186e3ME4Kin09weR198lU3Jf6yX0NCYfvLkl5FziegcfhKmo0RY3jkNhMqQ84frfpRHwWoFDxxbRdFuscKsJbzB_TK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dP-YG07xQ1u414iCmZw4H_hJEr5eThP7ACTVN9J9_2AnpxFHV5hNTYv25EkU72EEqAjdD2UEIIke8A1dQyGwILVECCIrOG-OHXZPjFtUq61G3ebnAxpGuQC34X0PrhaYuHpCIGn6xU-MqkhQcA1zyiBktWbpN4HYbIL0r41cl9uLn1-Y-IdUYwSpPhwDrNzjnpsR6sNUsJ7LBaZYRfdug0o-9IJwaCXfURB6kD1c0hMPgcAWyuftbvyPVRJq4XGckFI_8piirgz9fqiax__8Ju4xZecQmoA9Iylc0f82HnTmLX0maXs9gs6ZYXUebZOPfpKE_3nRbSza0wZ_SwOIpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا،‌ روز پنج‌شنبه در گفت‌وگو با خبرنگاران تأکید کرد که ارتش این کشور قادر است «تا زمانی نامحدود» به محاصره دریایی بنادر ایران ادامه دهد.
هگست گفت: «نیروی دریایی آمریکا قادر است به طور نامحدود به محاصره دریایی ایران ادامه دهد، چون همان طور که تا الان کرده‌ایم، می‌توانیم کشتی‌ها را [عوض کرده و] وارد و خارج کنیم، و به این کار ادامه خواهیم داد.»
مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، در هفته جاری ضمن هشدار درباره این‌که «زندگی در محاصرهٔ دریایی به سطح نازلی سقوط خواهد کرد»، گفت انتقال بار از چین به ایران از راه زمینی «حدود ۱۸ میلیارد دلار هزینهٔ اضافی به اقتصاد ایران تحمیل می‌کند».
@
VahidHeadline
روزنامه وال‌استریت ژورنال به نقل از مقام‌های آمریکایی آگاه گزارش داد که ایالات متحده در چارچوب یک برنامه از پیش تعیین‌شده، ناو هواپیمابر «یواس‌اس جورج واشنگتن» را برای جایگزینی ناو «یواس‌اس آبراهام لینکلن» به خاورمیانه اعزام می‌کند.
ناو آبراهام لینکلن بیش از ۲۵۰ روز در ماموریت بوده و طولانی شدن استقرار آن و محدود بودن توقف‌های بندری، نگرانی‌هایی را در میان شماری از قانون‌گذاران درباره شرایط زندگی خدمه ایجاد کرده است.
در همین حال پیت هگست، وزیر دفاع آمریکا نیز گزارش‌ها در مورد شرایط بد در ناو هواپیمابر آبراهام لینکلن را «کاملاً تحریف شده» خواند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77851" target="_blank">📅 19:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T93uf9-cWYxG2uLGws8sljc6Jd7G_4PPWwKJpYY7n-5fZfaK07oOb9ljBykuKHGLVBoS47vaW54azcoboJ6vqdKJAEizox6gRRh4PrjymVqCVN0KIyKj0H5NswquKu5tZdiw1WTd4a8sQOY5521EbJlQf4ojMkNmQ7QuWesKYyezKdT4ZEIe6GtSpObBfMVS1L1syUJnluGEI-LGyW5cmibA3BCh1Wxlm2KxOBHPd03JYD0yaHUFmhQGa7qBdIIoX4JT8Ua6fQeKTbgHjTO4ckNmLkYogJkH7xMxg7tBAqV-6GzmQBoFU4lFWx5GWPDYkolHBx3mqGcdRO4T2TPwRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور مجتبی خامنه‌ای، روز پنجشنبه ۲۲ مردادماه در شبکه اجتماعی ایکس نوشت که «راهبرد قطعی رهبری» در صورت تحقق نیافتن شرایط ایران، تهاجمی شدن جنگ است و این راهبرد «معادلات قدرت را در جهان دگرگون می‌کند».
مشاور رهبر جمهوری اسلامی در ادامه ادعا کرد آمریکا در محافظت از متحدانش در خلیج فارس ناتوان بوده است. او اجرای «سازوکار اقتصادی-امنیتی هرمز» مستقل از تضمین نظامی واشینگتن را پایدارترین راه برای ایجاد نظم جدید در منطقه دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77850" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77842">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDB32kKkbRoBPY9FPau0iQ-1baFPf2eJ9hHqnVeWFzP1hfd9616itih0qYfC07JXq7QcaIu2U-tq9Zfx-v2a5OOYjL6RIiOC0If6ojJSBNrrFNUz-dJ6hqpf3aq0IuOsRsHxR9OYcm7kHehKD1bl7NxBBsjFeGSaIlk1NZReRcUjL9lde987RwLwplpBbaHuf4wlV05s48BHFEwSmoqSrcB35zTx2dTr2V-5gp8qEyBQMIMJiX0wOuUeZdgh6UB5FOaIpYGQkDX9_9zgur-JF9jhAPYJjFaz90fnvwBII9DZ5iJbvESmAQmy9P-wgVmd0YJyPR3QwWexbOQ_jOGGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWpBDNfMrt2moWfSSElHDwCN725MJiu1MplvGrMI3fzzZ2sE_wzHI7xb5-3jT5zRlNcD9YQWj_BLnyWJrWEp7f5F3pLfkER63l0wDeHrYdMJzcgc5VGrpPd37FPMsBM_zFt3Cv9VWzaQhGLOy21jvq5R-0gj9AECqPR2ov1oqunqUi6Ms3zJHLfwv91J2SYQOnuTd6ZX7-FNI_dP8i65qnpr6VgL-Nh-6eWB3JYNlMQVJaPyB4FNAlSS3XmeDFvoRyaUtqRl1yVpLhhAKYdVpteI64fr9TqNoxn_gb2vn1WWp2gjRBO1TUrR5rVZkMBGNun0d0g_mWDFWlxnkRd6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7u0oZHhOAM9oAUdgMN7ZHJCzufQgut-uAWtpSwNvr7dw9YF6EFurTOvo5ndixN_8PNR0SLT0_2afa7P9TxsqllvpEmwxwK4UUnupvTi9zaYZpijhgoZ6DreWoIZUWPEh8f9mz5FdbH_N4_bDf0cXHuc8Nr6ZoTfx4xgGXzpmN2D2yFKvnXKjQ8utKETSglXKYEgL3BRoMLKZKC89uYjoBNBQ2WTdXiR7800Wgk9xMss4yECKkCE3spEj5MhVJoT-LUnSTsRWCzaMVlMPSxhms_g3fd9D8RCNjfoluV0OPZCnOBdkdI1SL62WWXqq5brFKYv1siQJaIWPErIL2aTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVfFSCpMFPbY0RmlBC0gnFOSiOU_VSGlD0VFg8if3gV3lw-C9vtFKscQC8FlVvjzATf6-w6NcguOBq5pPHYaEtBzVROPQuImD3pT7Prm-rjtdgOg2M-Zr7M8_MuTmuQ8b_GQOVy0scC6aGKcLu1-YIMT3UNnj0Wya0emJHO_Oey9WtUBLYG6zModd7eLnlONMrywnxbvEMLP2YOmGWsG2Cij-wnz0ABh2S3FG1HgXik3Lxla0n09IH1yibH17kXceumoanfTIZxsNB3cDGcodIm58ZMnaEI8sUyKjO6ZCzA4KsCcb5q_UBUeGk8yQfTE9yMWNUpzSiq5Hx-jpfWLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9ufPFSJEihHUb7XRjT_6eOvVUJerwxBgmLRLsn2wVef8L7ryhWNcZ-51_I-QiGM6LhEBozeKK07ZGTRaaq_FMHx_fekj827uDNYEb4tpcro8_IfkRu8aWqPcNS6JVh7VhCKG7xBntP8jjyfyNLbe-umknwmduPSxIJnkiIm5nAGGLobS2ihPqzHrngPZCz7l8wvFKRqgLBeQfPoOs_5Pyxx9cJOmzKcO4fU4fTv0Xfndtb0UgbNlUoQX_54XiiKaLnL7WvRvue3jjq3yIZvGrMtJMTap_esifPxuH0cdxAr7UZvAqpt350gfKUDnuxUGDrvQhiPozyu_Uv2rZMgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UweOF9eQZYB927lXNOco1bZU6I_IBEfHLzV7WI3cgNxhcQkVKGWfYoaQkvks_px1bvMa17Zaa5lqd5TlCvSco4EtWwhH3Ws1W8UfO69GeiCXWnHEM9rHp6WZnfPy0ycqWc4BkQzxyVXQSgG8hOA7XzzY0I6UvrXuU6ChveXe9Z1Oq_Mmyi0hszNZCmwcdQrVwHfSKGiDEu3MikThwnHLXAVnXbuPmru1tgp2ZVYsQqmVSKAf1XrCRJHKod-ohIhVMmC_fwS0GbfVjlf8ffotM3EJ23ei76O_95Hpb3rFS3VRQQeik8_tNi9eD1BxG-ZDCm2kkqITMYqYyD90Hxku7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kl29llsJUaNTEw7M1yC6gj5RPdCR02Mpgo0r6415AW7zgUudxZ50yCw0Gk2ymcbZB-ZPPrC2Z8Z642Rxgwo9tTFOzGkX4GbPR0asuM7zSgyAP6uBnswYqKzX9Ikzkw7j35-ECz9Hfxu0wI1kVYIkGA9cuZDsgv4zF3VMVljj-8yCj9QfSmLJgT64HWl4slknlLIa8bd7otNuyzURReZlvSGTh3qnF0h5FkBfLcjtGwovhYi09cu-xWd3v0boubWocmSJljpcDIRTYCG4x6ltkxb_E1V3cVaxFMISWTHCuaWn2u4yc6ZQV8hlOd5bfmue-owN3_j70U-MA5ExkFyP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpk5HNWD7eS69r5u0v8w_Za_MyOAIxSN-uW-QsEh8Zudpm5MWLsJFk-JpM7YMv3FpZugBxH1nQaLLGAKJzBFgnhFqmuitB5cuGddBTGoPvDKlejaSnoTAoX3LgqhaTGRm_8bX00J-Pn_7IhxMCgXCSbeJRO88ECj_j731utp9V_Z1oSCXywKcSseIEnfrVpxr2UbGWb25_ZoLGc0RX0uzalc3OUd0f791NUENsc4DeJWTXM9EAjMEHR_syOVf049prDyd1Xv-MQw5Kewi1nd8JOa3OsItCFAahJG2B-HqtLe7EHElhZCMSeXYUaQnxXkdANDOv3sg0KkWWMVX37PZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شلاق مجازاتی بی‌رحمانه، غیرانسانی و تحقیرآمیز است که طبق قوانین بین‌المللی به‌طور قاطع ممنوع شده است. با این حال، جمهوری اسلامی سال‌هاست از شلاق استفاده می‌کند؛ نه‌تنها برای جرایم عادی، بلکه به‌عنوان ابزاری قضایی برای سرکوب معترضان، زندانیان سیاسی، زنان، هنرمندان و مدافعان حقوق بشر؛ ابزاری که هدف آن نه‌فقط وارد کردن درد جسمانی، بلکه تحقیر، ساکت کردن و بازداشتن افراد از مخالفت و اعتراض در آینده است.
🔸
بنیاد برومند پس از اعتراضات «زن، زندگی، آزادی» دست‌کم ۱۷۳ مورد مجازات شلاق مرتبط با اعتراضات را ثبت کرده است و در پی اعتراضات دی ماه ۱۴۰۴ نیز در حال مستندسازی همین الگوست.
🔸
از آنجا که روند رسیدگی قضایی شفاف نیست و بسیاری از قربانیان و بازماندگان تمایلی به گزارش چنین مجازات عمیقاً تحقیرآمیزی ندارند، مستندسازی ابعاد واقعی استفاده دستگاه قضایی از شلاق همچنان دشوار است. با این حال، این کار برای آشکار کردن الگوهای سرکوب حکومت، حفظ شواهد برای پاسخ‌گو کردن عاملان و به چالش کشیدن استفاده جمهوری اسلامی از شکنجه، اهمیت حیاتی دارد.
@IranRights</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77842" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t-AXrr2TMQ6Yn1eR0Bynocfhuimk9pgjp2sNmQK4cf2WfaVSh8jmU453cunnPJlINr3Rf4u7zQMr4ht3ilRVg1LdAxbMUxqpDopK4ygc8X-nUt5RTSKFxXtubmdf4F9TvhiXrZ6kcAQl1GwL3Ng13BAcal3w0yamC1AmGDSgXN4zlqxG6IutgAmtd_c6Xyfncebg00UOdkC2ub_xxD3GEtEeznivGpTnu0p7nBCfdH5mDtYZwKfG2XVQST_CLadMoXCZXKKqAaDgacrxwiVR-3Xm6A3FByaadf3jnDVxl8hfa7ca_dBFJQO5zDiupdrxq2D7VxNzYVFIiLnaRaXpig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیما:
«توقف اجرای طرح عرضه بنزین با نرخ پالایشگاهی در کرمان»
مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر در خصوص طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضه بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77841" target="_blank">📅 00:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/STRO8bAVf5l0CWpbE5ffFmgMseQxK2l76zE9kXaPGZQ4h-CTAqexc2GdPpKRD7Hb_X9EG-yq19BDqTq1pMmipx8pAYswtD9-ylRfiXd6XXVPwm7Qg6uymLGgk5hjczq7BKr9cBeCm1SCpYPAOu5o65f-ugbTk7roTTRD7vKY_DC6jNGbxIUyaGaDrbwR7uxdMtczG4HMW4GcrQqKfCu2wzWY5STOvtrk_-A_D4rYyV65HULhvVw-hfZWcDvwsD0_j3iIlaihznotNX4n9eF77Q7lprNQwD1WKsl_NkrKVv0SfVkBmVLKT4pJfVjaTVTN5vSg648sCwA3Day_J0M9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون هماهنگی امور عمرانی استاندار کرمان از آغاز عرضه بنزین با نرخ تمام‌شده پالایشگاهی، هر لیتر ۸۷ هزار و ۲۰۰ تومان، در ۲۰۴ جایگاه سوخت این استان خبر داد.
به گزارش ایسنا، علی‌اصغر ذاکری‌هرندی اعلام کرد که عرضه بنزین بدون یارانه از ساعت ۲۴ چهارشنبه ۲۱ مرداد، بامداد پنجشنبه، در جایگاه‌های سوخت استان کرمان آغاز می‌شود.
@
VahidHeadline
🔄
آپدیت:
متوقف شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77840" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jGsoKS8h4O5ySsqzglMLFWdbK-OXj3VThCdxG0Sotgc_5fDU57ithg9CR1iGNkEFHaG_EJ8aagoWtbSMwjUoi34206fCDFI7fK4F-T6gfD9Yi8FUrUBt3uG_vv_Gqc5Zgd3LUTsEhAakLl1YzlCXbAJBIiSV7fmE4D3LT4Ozt0nH4nIqGCAjGemgndkgo0iW267-XBFMuM7eFJQBIpbqICMG5pUjLYxvADGjOPpQId2PsFBYos9219pS2Y3rU28Jfl9UBVzkHZtlfDvHzSx3CM5hqA-J8aKKAOknnX_YS24wp-3dal1iEDznW8kMwTVoqf-wvgg7UND540vOAItEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LMeECZ1ZcXkx4scz4FiZ9vRpQ7Vz8oUCHHmi2cm-8uPkCx3lATiqx_G8EqTlG-gvtceZn-fFE-UF9Uqbpip_YirkxH-H-AfW8IdZ00N-WYldiHKI-g0htT7lQZwE8CuRf7hXB5rDpqPcZW8qkUZ2pEF-C9rCG6BS8_bjuyHUFGOlN2HzCdmF7LXxultunm_LI0a_-I3xWBH9xvb-EjtCDrwkMN6DMKORWTQGnDv1oT5gIt1J3dFcF-N2XJuweYgzeQJC6ub7HNy-wiSKf4ibfiHXjlKLxYJ5M2yF0kVMi99ypDwkYrgeYV1q9PcfSkceoAt3b8-pTHNVuGhb-457SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتحادیه اروپا و شماری از کشورها، از جمله کانادا، بریتانیا و استرالیا در بیانیه‌ای مشترک، با شدیدترین لحن ادامه اعدام معترضان در ایران و سرکوب افرادی را که برای عدالت و کرامت انسانی اعتراض کرده‌اند، محکوم کرده و خواستار توقف فوری اعدام‌ها و آزادی تمامی بازداشت‌شدگان اعتراضات شدند.
در این بیانیه که روز چهارشنبه ۲۱ مرداد منتشر شد، آمده است که استفاده از مجازات اعدام برای خاموش کردن مخالفان، ایجاد ترس در جوامع و مجازات افرادی که از حقوق بنیادین خود استفاده می‌کنند، به هیچ‌وجه قابل توجیه نیست.
کشورهای امضا کننده تاکید کردند مردم ایران باید بتوانند بدون ترس از آزادی بیان و آزادی تجمع مسالمت‌آمیز خود استفاده کنند و از جمهوری اسلامی خواستند فورا به استفاده از مجازات اعدام پایان دهد و تمامی افرادی را که به‌صورت خودسرانه بازداشت شده‌اند آزاد کند.
فرانسه، کانادا، آلبانی، آلمان، استرالیا، اتریش، بلژیک، قبرس، دانمارک، اسپانیا، استونی، فنلاند، ایسلند، لتونی، لیتوانی، مقدونیه شمالی، مونته‌نگرو، نیوزیلند، هلند، پرتغال، جمهوری چک، رومانی، اسلواکی، اسلوونی، سوید و بریتانیا از جمله امضاکنندگان این بیانیه هستند. نماینده عالی اتحادیه اروپا نیز به این بیانیه پیوسته است.
در ادامه بیانیه آمده است: «مردم ایران باید آزاد باشند تا حقوق خود برای آزادی بیان و آزادی تجمع مسالمت‌آمیز را بدون ترس اعمال کنند.»
کشورهای امضاکننده همچنین از جمهوری اسلامی خواستند صدای مردم ایران را که خواهان تغییر هستند بشنود و برای تضمین رعایت حقوق بشر، اقدامات عملی انجام دهد.
ژان نوئل بارو، وزیر خارجه فرانسه، نیز با انتشار این بیانیه در شبکه اجتماعی ایکس نوشت که هفت ماه پس از «جنایت‌های گسترده» علیه مردم ایران که برای عدالت و کرامت انسانی به خیابان‌ها آمده بودند، حکومت ایران با افزایش اعدام‌ها به «ریختن خون» مردم ادامه می‌دهد.
بارو این سرکوب را «غیرقابل‌تحمل و غیرانسانی» خواند و خواستار پاسخگو شدن عاملان آن و آزادی زندانیان سیاسی شد. او همچنین تاکید کرد مردم ایران باید بتوانند آزادانه آینده خود را تعیین کنند و حقوق بنیادین آنان محترم شمرده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77838" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uxrb-mhEl4_tv-wpVB99vzDJcUHRwpVjuc8d30dWFpxmygnPIpikOJ1ovl_M5q0LZi9VKecze8aVh5bdlkV4Ub4pe_3jKTJrwy-hXv7k2G6g0tdV7ccFiblWhURXyVyaofQ4LOuz1598Ml_KCBBsaoXZ1_sJGkxLMb4fDZdAy_iJK7PpfCyFhyNIsCndF_HflNphPmH4Mku7woPKg0Dz7n0SSrT0OaUn3U3l-JMoidZLSZDMeq-_XoaaXN8fDx-zO9sIwv-iyu1TKWb0CmT1whLCYFYzj8k9mIychtinFFoJUuUEGsFNmPF7NZk_BQbpSgVliPU8OlfOaeYQyaUIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایالات متحده آمریکا کنترل کامل تنگه هرمز را در دست دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
محاصره دریایی ما را همه «دیوار فولادین» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است، و «رهبری» آنها، در بهترین حالت، نامطمئن است!
آنها هیچ پولی ندارند — کشورشان «از پا درآمده» است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است، که دارد بدتر هم می‌شود!
ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. الحمدالله!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. has total control over the Strait of Hormuz. I THINK WE WILL KEEP IT! Our Naval Blockade is being called, by everyone, “A WALL OF STEEL,” and there is nothing Iran can do about it. They have no Navy, they have no Air Force, their remaining soldiers are unpaid, the IRGC is decimated and fleeing, and their “Leadership” is uncertain, at best! They have No Money - Their country is “shot.” All they have is FAKE NEWS and 300% INFLATION, and getting worse! Iran is all talk and no action, the Bully of the Middle East No Longer. Praise be to Allah! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77837" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77836">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=Vun9UcGFl-wUSQWR_eG_WzrNFzQ4m7QDYemQ39KDXDhfo20hnUobUYyoHjjUkdS8eYg_JJPO9fcjJ4kZyrADw2wQKjaJnpmbF9fAiQ6bSUypg7fdS5Ll6In2pbq3vwBIkKv87M0Up52MNSSavOrV7H6Tq9QAT0vxZcJr0rLMUAPphlWCIlaSfgkufZz5ts_AkG9vJlQ1pr6GtQf4K6dY1VXjU2_UNpRQ82J3kampOmof8wgCyMsAwkiRO7RHzH1iqZoDQWf_Cfx92Nmcht4mTBdfhnO4TtmvlNcrLRayzrsdtp8NIzzYk9F9tk1BWfBxhz0E5ijh25LCeI-OdGZDhx96v5PszQ72sdPRURlYs3wAi5IJSJ48fbKo7Yq4tqmwKapTGgZN5YJ8JKSqgvklSqVUthP2BsQijM9JkXwAdkC2E32pMmuffK00pfDpKqxPjNlwzxvI7Rg3nvgP2aJbJtvL3al7ZTZJ8LRooTVmMY8kHMMT1687q8IqW-3zdvl469HhqdOvOR0_rRZerfwNk2uD0Rp6RomV05AyZta5VFAbyYtXVaw-FqhsLSFjhBbiWYcP_FANSVx_AoOKzf9AXIY4rOcWc13zIKQZUX0ST6Qv12V3Xu-Xlk7cYNkNfIw0TfRSa3XtagLPNybERq_UJOy7WLvJR5LHms4reuwsTOE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=Vun9UcGFl-wUSQWR_eG_WzrNFzQ4m7QDYemQ39KDXDhfo20hnUobUYyoHjjUkdS8eYg_JJPO9fcjJ4kZyrADw2wQKjaJnpmbF9fAiQ6bSUypg7fdS5Ll6In2pbq3vwBIkKv87M0Up52MNSSavOrV7H6Tq9QAT0vxZcJr0rLMUAPphlWCIlaSfgkufZz5ts_AkG9vJlQ1pr6GtQf4K6dY1VXjU2_UNpRQ82J3kampOmof8wgCyMsAwkiRO7RHzH1iqZoDQWf_Cfx92Nmcht4mTBdfhnO4TtmvlNcrLRayzrsdtp8NIzzYk9F9tk1BWfBxhz0E5ijh25LCeI-OdGZDhx96v5PszQ72sdPRURlYs3wAi5IJSJ48fbKo7Yq4tqmwKapTGgZN5YJ8JKSqgvklSqVUthP2BsQijM9JkXwAdkC2E32pMmuffK00pfDpKqxPjNlwzxvI7Rg3nvgP2aJbJtvL3al7ZTZJ8LRooTVmMY8kHMMT1687q8IqW-3zdvl469HhqdOvOR0_rRZerfwNk2uD0Rp6RomV05AyZta5VFAbyYtXVaw-FqhsLSFjhBbiWYcP_FANSVx_AoOKzf9AXIY4rOcWc13zIKQZUX0ST6Qv12V3Xu-Xlk7cYNkNfIw0TfRSa3XtagLPNybERq_UJOy7WLvJR5LHms4reuwsTOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرج درگذشت؛‌ جناب سرهنگی که «پهلوان آواز» ایران بود
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در ۹۴ سالگی درگذشت.
درگذشت او موجی از خاطرات دوران طلایی موسیقی و سینمای قبل از انقلاب اسلامی ۱۳۵۷ را زنده کرده است، به ویژه در نزد شنوندگان برنامه‌های رادیویی و یا انبوه تماشاگرانی که آواز برخاسته از سینه ایرج را از لبان ستارگان فیلم‌های آن موقع می‌دیدند و می‌شنیدند.
افسرآوازخوانی که حسن کسایی، اسطوره نی را واداشت «پهلوان آواز» خطابش کند و صدایش برای محمدرضا شجریان، خسرو آواز ایران، «متر و معیار سنجش کیفیت صدا در تاریخ آوازخوانی ما» باشد.
ادامه مطلب
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77836" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77835">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cHYzDyubFOGLd9dhDnKNEbxSNl9vqdEmBDChKTPwR9n8Pu953BXVw-5mrMdEvVb6W3hc6TltZ6TxJBMbqsa4iYA1KSbgXNcY_FKyqsSEgem6_A57wGzAMYBa6TvVkhFnbLdijFPvGD07EPC18vshxnvKC-ilahOZ6QAVQSogpe1NTYdneCe2HbBL115t7EBtjbSu5D8VrZVQvRR0ncmpizWXJ5f6GvffWpA5-64YruqQNF_XecherWBYxSbkftyRO79PCW18XFSIaFQdA79n9dHGxWlUaBr7sPS2W7o83PTl_Bd41YeLM351dKlKNpAtXFwPh7hiXodUduYbVvFaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت جمهوری اسلامی می‌گوید هند در واکنش به انسداد تنگه هرمز توسط جمهوری اسلامی، حتی در طول جنگ یک کشتی مواد اولیه تولید دارو نیز به ایران ارسال نکرد.
محمدرضا ظفرقندی در ادامه تصریح کرد هند ارسال مواد دارویی به ایران را مشروط به عبور کشتی‌های مرتبط با هند از تنگه هرمز کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77835" target="_blank">📅 16:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XQGj7RWPkwioYsk2K3XH64rfw15ne6bnHcQr5WY1zQYNJIuRYeThFctlVaYFVXVa3Yg-fGn7Lws-Fn_MPQRigrKCXsuapRSdal41Dwrg99bHK-qkH-OYLrn0SIBFjm-8CENKPMDy_-EavHDypJ0tU54L2iHg5Tbc3fvY30Q-0sVBaI502Pmyq8rVVitfz78VhTDN4YYyIFWO0HQRXzdY--w_P1-ZJZS4A1XmhSHxerhs34t3ZmMKquKjjkZ5mOPUtflOeaJcDXmexthCwHa8NdWmsjSy6OtzQFiqWotYE95-q4wVM39zdzWkGvqPgCgDWWEDPIBtVA4OPlkcOJ3WZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای مسافربری پهن‌پیکر چینی، قرار است روز چهارشنبه ۲۱ مرداد اولین پرواز تجاری بین‌المللی خود را انجام دهد.
این جت جدید که به عنوان پاسخ چین به هواپیماهای مسافربری بزرگ بوئینگ یا ایرباس معرفی شده است، کوماک سی‌ - ۹۱۹ نام دارد.
این هواپیما اولین تلاش چین برای ورود به این صنعت پرسود است که تاکنون تحت سلطه غول‌های هوانوردی غرب بوده است.
پرواز هواپیمایی چین، ایر چاینا، صبح چهارشنبه پکن را به مقصد اولان‌باتور، پایتخت مغولستان، ترک خواهد کرد.
این پرواز رفت و برگشت به صورت روزانه انجام خواهد شد.
برخی تحلیلگران معتقدند که ممکن است سال‌ها طول بکشد تا جت‌های چینی به رقیب جدی شرکت‌های شناخته‌شده‌ای نظیر ایرباس و بوئینگ تبدیل شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77834" target="_blank">📅 16:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77828">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A3Mu-aungiOcCnLYxkB7PLo0ZjGnZLrXDtOLlEVT9aftmiOhYMOUQT8IJn3tW7cVccuLdrb-nNDAaDwcSUyrLXBU1tZpZdeLhBPyV3AAH2eWLV3hRSurzAj5lfVHgXIJGr0gXGhFtlB3VQSiP8uGxnf6YoVud6hWeD2AieJRfTgtK2G3RXkq1KAWMKLH2jzyKV_Bc7U12TWSRTD_J1dkL5UZ1c7_iB7XgZDxFeFmFRMyrgJSL0rIx9-LboWzTxWUEPYjVqkO6ZguDdvNsZb3bsIFXZ5n5FO6rH6z1h-cVObAl_jmCr9OEil3WZS6GbEeF8dUF3pW4sPLMAR3qnuBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lm7m-UHuwLnP2acxF7YavDMcHQ3cA_BI7nQGhhbQfQcwYqacGZ-lbLhobNcVolr5BegMG8xqIMC3xxTvNSq93QFvssYBKXaYyNfZ9lw9LRRSkkhY4csHrrM8QD9O7Im9u9nBMsSynSyGyduoUh3n1uCrdyrwHan9JvD8OJ_JkKQ3l8yfSNydbSsm4qFXafbvJJRKET3qW22-irqh6LEuDAfjWIYlv2svBh49sK06MqnJifyeTtigx97kyMxF7sG7qMRld1LWVRdpgYd8d2iZenGCS5HXcHcl3utOZ48UUiRRUhvcmo3aJDTxc317WeATS-imghIe_USaLSk5YFin3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NYHGxRgPX8tn1kDk3BzdWHwOFXkh12akIVm9vnwm-Lqo-sSAXlX09RLaYri4B1jptQwZNBg1qxEEOXvHDLxbn704nWxlhpW_MkRipTGvXA6dnDJizBS-gUJJ6brIV_saT9pgltLxV-ud2QST0e-y_2ZFRJkbJbcj7JxCpzHk4cwoVp8qm2P3lF78vu0r9pyDv4KUPhZWA8He4DYCd8prgf8zTnzWJyPW7IitLAdG0gTOlH6DrgzJ3EoZrj7STnQyJVRdrYdRgeOKlS0o2qHhxD9r7niUItKptZmNf7FfoKrlIo-EIaSH-qtwf1zPJNh2rH6xpc48EAVVn2J51yAC1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IEIprKFDSgIImswbDcX5PlXTX3uzkwTb0FKPovPzMj7yZuUBJziGSPhrv2V7jYxtyLSUf8XPYGkzFYYCvXTO1tXmFCqWQhgti4abQxoGiBv3h2cwUKZGJovmMD5mjfnWTmf1CEIwGGSbrEkrvjCMa2aS_k_ponHaVdb4x5b1tQZzE2DkSB7Gabw1cVX2clu8SMRq3bhix2cwRXHZBJsphyd15_KCsqYEFWqj19UY8gwfpGUep4K9YWbto0Qs7wqGK3fvDT7UdtuCFoR4q73LCU-RkX7tDZ3XZwiL4APJwhmB9PW_UV5CRXiXw6yo8CJwXBddRfYELZNqKvOF0fDbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PlbLBdLNdVQYxtUz_Y1mhHrqpjXsYe-8Ci3i0_3E8stSSSGwdvBLELf9kCala3dRMCIoKFrmDly_e6MsSSNLT-EnpafP6vQ1eQQ3TIcHaOhe5HhTDNiWcEHBWJN0dIhuqPvJboGFl9NfNTm1WroSoS8jEfsgjKI85HtY2W3_BnSBXZXYl3YGLYsjj87GhU77WloZTXz9uqgNwPDjxm5Np73nfAj4trUuj_XVwqxD8SCRTbEczXlAnKm5p0K-o7RUoF8f8SC7ylUSNFX_vWkQVh94jRO_bvwyqt5GonkofSvjjHA_PSMSVSFeedRrAiSlhNMt8KOhhTZ_GxX1DxHPcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=srfcoatwYFz4D6oRM-KFdXtXjiuzCwWKRdJRO8i9yBp_MGSUEmSOxIRkAHFJ75mCqkkGlOkBBVml97UA_EIECz_UBrA0Ihi619D1t-_kR-S91xOpZezkT05b835ZrL-PxZEhYTUujlNJkDS0Tg9q7lA63AZ-17v09Fyi4ft5qWcLWwbmzxNnvhfyWhttOKi1nISA3eyn07lvQfpwHI22s3k4MLY5ii_yoNGg7DyHuy02ICszanwgnmdS0oO-_rcX4HVTXFKVL5xUJzegALO8gdOQT6qXF2BxTml64_7Z3FGWediPiR2MC2QPl_wY9lrK-p6IEnjyxrw1q37Fd3dnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=srfcoatwYFz4D6oRM-KFdXtXjiuzCwWKRdJRO8i9yBp_MGSUEmSOxIRkAHFJ75mCqkkGlOkBBVml97UA_EIECz_UBrA0Ihi619D1t-_kR-S91xOpZezkT05b835ZrL-PxZEhYTUujlNJkDS0Tg9q7lA63AZ-17v09Fyi4ft5qWcLWwbmzxNnvhfyWhttOKi1nISA3eyn07lvQfpwHI22s3k4MLY5ii_yoNGg7DyHuy02ICszanwgnmdS0oO-_rcX4HVTXFKVL5xUJzegALO8gdOQT6qXF2BxTml64_7Z3FGWediPiR2MC2QPl_wY9lrK-p6IEnjyxrw1q37Fd3dnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آلودگی نفتی مشاهده‌شده در سواحل جنوبی جزیره قشم به محدوده جنگل‌های حرای روستای «نقاشه» گسترش یافته است.
خبرگزاری ایرنا روز چهارشنبه ۲۱ مرداد گزارش داد بخشی از لکه‌های نفتی وارد محدوده این جنگل‌ها شده و عملیات پایش و پاک‌سازی با هدف جلوگیری از گسترش بیشتر آلودگی آغاز شده است.
به‌رغم گذشت دو روز از گزارش شدن این آلودگی، رئیس اداره منابع طبیعی و آبخیزداری جزیره قشم اعلام منشأ دقیق ورود لکه‌های نفتی را به «بررسی‌های کارشناسی و جمع‌بندی گزارش دستگاه‌های مسئول» موکول کرد.
جنگل‌های حرا از زیست‌بوم‌های حساس ساحلی قشم به شمار می‌روند و نقش مهمی در حفظ تنوع زیستی، پایداری سواحل و زیست و تکثیر گونه‌های مختلف آبزی و پرندگان دارند.
سواحل هرمزگان در بهار امسال نیز با آلودگی گستردهٔ نفتی روبه‌رو شده بود. مدیرکل حفاظت محیط زیست هرمزگان در ۱۲ اردیبهشت اعلام کرده بود آلودگی آن زمان در پی حمله به پالایشگاه نفت لاوان ایجاد شده و مواد نفتی به نقاط مختلف سواحل استان، از جمله قشم، لارک، هنگام و هرمز رسیده بود.
@
VahidHeadline
در عملیات پاکسازی نفت از سواحل قشم، از پدهای جاذب برای جمع‌آوری لکه‌های نفتی استفاده می‌شود.
این پدها معمولاً از الیاف مصنوعی مانند پلی‌پروپیلن ساخته می‌شوند و نفت و روغن را جذب می‌کنند، در حالی که آب کمتری به خود می‌گیرند.
پدهای جاذب می‌توانند با جمع‌آوری سریع نفت، از گسترش لکه روی آب و رسیدن آلودگی به ماهی‌ها، لاک‌پشت‌ها، پرندگان دریایی و مرجان‌ها جلوگیری کنند و آسیب به سواحل و اسکله‌ها را کاهش دهند.
با این حال، پدهای جاذب به‌تنهایی برای مقابله با نشت‌های گسترده نفت کافی نیستند و معمولاً در کنار بوم‌های مهار نفت، اسکیمرها، تجهیزات مکش و دیگر روش‌های تخصصی پاکسازی به کار می‌روند.
پدهای اشباع‌شده نیز باید به شکل مناسب جمع‌آوری و دفع شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/77828" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77827">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPMjpnmvQxxd1Oe9gMawYjL7h3DRi_jchb4QbCInwevwJh7KAuPHUVSzUGFXS3KSfuN-DtnW3Pa_OgddQuSTD87sJFcPPiKZBwIoL0nbApshxY8lMx7Rxh9TtGlbyklv0CnJFqffmvAfaJQgIGWTSNQImW86uTfusQsppWOj7HglboIM06tPDHKMED2sBkFqJj-yFHdZCXd5oz_aFhEFJW9foxwDTk4tzVApReTU6iroHceVO6b5-bs7Su2icSB5oOn6StsQPQg2-bwlA_TAVEw_blrKO3cP1XIH6LxkwPBtmJoEnTEK9UEFQsnvFIPpmQXHU8vu8dEZH4wEtBAU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جمهوری اسلامی ایران از ابتدای سال ۲۰۲۶ تاکنون دست‌کم ۹۱۶ حکم اعدام را به اجرا درآورده که از این تعداد، ۱۵ مورد در ماه اوت رخ داده است. شمار واقعی اعدام‌ها احتمالاً به‌مراتب بیشتر است؛ چرا که حکومت ایران برای جلوگیری از افشاگری، نظارت بین‌المللی و واکنش افکار عمومی، آمار واقعی اجرای اعدام‌ها را پنهان می‌کند.
🔸
هم‌اکنون شمار زیادی از معترضان با اتهامات سنگین و خطر جدی اجرای حکم اعدام مواجه هستند. روند صدور این احکام بسیار شتاب‌زده، ناعادلانه و بدون رعایت آیین دادرسی منصفانه بوده است.
🔸
جمهوری اسلامی از صدور و اجرای احکام اعدام به‌عنوان ابزاری برای ارعاب جامعه و پیشگیری از شکل‌گیری اعتراضات جدید استفاده می‌کند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77827" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77825">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MkXZlGAM0c32_uJKPmdfSKe3A2WItyW_sWBk8igcLMZtPBCTUi2tHZWUz5PiGqpblddpZkXHDZA9ODUp30mlOzStxC6FT1pitMeJqYhZVqOY2JZf3mPMhQJCJC-Qr-0EJHxMVqTvQ9CjvzyzQl-wkE8jYzUJBBi3cuJG-JTZC8GYaQYWcBWIf42WZsWAGEDOPOusp7XEavhi-3LPDOWLWGUv0ejsMmHW3Lih4AMZpL5GdMiq0XS3tZ5e_lKQIUOLHgWzT7x0azjNDsuwr_c4UsoNWg9Nf9HUKZNOclu6dpLJmqQCKy1QSenAN-rBNi1P3IZd1LeTxd0fhg32Co0JxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GHzTv9ZHJSxLHlCnniTZ2cuz7dT_n6Tt88i7VaN-5pLPJPZDCY4EzvYTVKblU3IOfWZgmNlyWG0nvxJct2JMqXTOWuOe571Rs6td2ktbw-CyX6_NH6CopIOYgEfenSuxT7SBuIgXnef5jkvbzscLUo9zO5S5uyu7vO1yEDIb3hkDepENTek52zjTmWTk9FL6LSFU-ZEMihBt0XXO6HqEGujeCTd2p0h61gx-8P803Y5CbcMGPK6Mo9ta8WjgAmAalg98RYZr2VqtOA6fmotioszOPwT2GL19fG2ssclGIBUIE8VWv7U_pQC3K4_P3nhERtOURubeRXjJP62MYySh0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد  ترجمه ماشین: واشنگتن‌پست دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با…</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77825" target="_blank">📅 08:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49def3f074.mp4?token=PI__bGLjJXwNBgd73gdt7x0y_GmwdIa1HgCw0awSCt_qP8LDbkwbSvSaOvQ0rxKCFbTcMbGUI4EcMAsefSkxQ2bYinNAoWcAKoR74mLjvMpLYLPc3yjakVeU3-xjlDJMFOlEonmzLF3ip3LPvn_gjWqUMfXvdZpiHg1KjNxfBfFFW2Q6AsHAd1Q8pSnYr9cn2PH71N-LKbyxXEfCPRN5NBOKtj3YR8hIE-5sjQZQpf1_elbCQpFmm7-dPVm8tAkjVTi7PER8XSzJ4A925LCNWZjY24vh7vuxwj49sz2X-4rnCgSz-X9FzS_0Sap-EbMpRqh9YvBzfb-rtIV0LT2d_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49def3f074.mp4?token=PI__bGLjJXwNBgd73gdt7x0y_GmwdIa1HgCw0awSCt_qP8LDbkwbSvSaOvQ0rxKCFbTcMbGUI4EcMAsefSkxQ2bYinNAoWcAKoR74mLjvMpLYLPc3yjakVeU3-xjlDJMFOlEonmzLF3ip3LPvn_gjWqUMfXvdZpiHg1KjNxfBfFFW2Q6AsHAd1Q8pSnYr9cn2PH71N-LKbyxXEfCPRN5NBOKtj3YR8hIE-5sjQZQpf1_elbCQpFmm7-dPVm8tAkjVTi7PER8XSzJ4A925LCNWZjY24vh7vuxwj49sz2X-4rnCgSz-X9FzS_0Sap-EbMpRqh9YvBzfb-rtIV0LT2d_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با خبرنگاران گفت به ایران اعتماد ندارد و افزود: «من آخرین کسی هستم که به ایران اعتماد می‌کند. آنها پیوسته به من دروغ گفته‌اند.»
ترامپ همچنین گفت ایالات متحده در حال حاضر «کنترل کامل» تنگه هرمز را در اختیار دارد و افزود: «آنها کنترلی ندارند. ما کنترل کامل داریم. اختیار آن دست ماست.» رئیس‌جمهوری آمریکا در ادامه گفت ایران دیگر «قلدر خاورمیانه» نیست
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77824" target="_blank">📅 07:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=Z73p4geT9wdzrjjSVz0bhlFE_t-G8vhlYbyZWzk1D-U7vMyiGjY-tDavq_0D5BgQ45ecvesNpisjYY-xouUVc30QWc2PEMwJZyOEtnTr1gHjV7KZpKzRMPY2M89ACzndK-Hw2noAG1kaOPZkrDrASBqSJmyDv2qUDgxrYVi-x8iDMCXn-QdZu2AU6s0cgwvX7O53V8J7YSNhpphmcobF6TWPGj_fmyizVoDDdY8WobUO8uUYsIJpIAsfNSijzh3RI50k6uPk_Z_7lnmqSoTXtzbIp-sAHxTa28CIfq-zJn9XStsTBUnoPSw-QJd_dYt3u4B7S2wHUC6Nndvvapz8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=Z73p4geT9wdzrjjSVz0bhlFE_t-G8vhlYbyZWzk1D-U7vMyiGjY-tDavq_0D5BgQ45ecvesNpisjYY-xouUVc30QWc2PEMwJZyOEtnTr1gHjV7KZpKzRMPY2M89ACzndK-Hw2noAG1kaOPZkrDrASBqSJmyDv2qUDgxrYVi-x8iDMCXn-QdZu2AU6s0cgwvX7O53V8J7YSNhpphmcobF6TWPGj_fmyizVoDDdY8WobUO8uUYsIJpIAsfNSijzh3RI50k6uPk_Z_7lnmqSoTXtzbIp-sAHxTa28CIfq-zJn9XStsTBUnoPSw-QJd_dYt3u4B7S2wHUC6Nndvvapz8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری‌های ایران تصاویری از «آلودگی نفتی» در بخش‌هایی از سواحل قشم منتشر کرده‌اند.
به گزارش این منابع دادستان قشم دستور شناسایی منشا آلودگی، مهار، جمع‌آوری و پاکسازی نوار ساحلی را صادر کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77823" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_kVrk0uJKneSx_3_sxBeNtmXlaxN_wIBjo4IlRPam69uG9FreiGSpljaMEufaIChh3cSmfsDPOpOMQK9QwnGMb23RfxT8lDRhuHJdZapEG99IgI2tY97TlnVVbKWQtSd56kfrpKcloJZ6uheGIS0HKfFgiYipzzt_PUH_9z2OlWxlrB39nofATau9BKYS4PC7fsvTTX8fwC73vkdYfK5yDyipR6_fJ2bBDw2-vHJsPksu5RBQb8YI0pDDcVckVfnWdkGnwvm1NW2nB6-NH5qhvIFQaqzo8B6aODC8X3nphmyCulnINGsNh7N06dpNgkGPeup6ofObsBigJEOrUuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر جدید شورای عالی امنیت ملی جمهوری اسلامی، در نخستین موضع‌گیری پس از انتصاب به این سمت اعلام کرد برای باز شدن تنگه هرمز، آمریکا باید جنگ را پایان دهد و پول‌های مسدود شده ایران را بپردازد.
به گزارش رسانه‌های ایران، او در دیدار با سفیر چین در تهران گفت تا زمانی که آمریکا «رفتار خود را تغییر ندهد و شروط ایران را نپذیرد» ایران اقدام به باز کردن تنگه هرمز نخواهد کرد. او پایان جنگ و آزاد کردن پول‌های مسدود شده ایران را دو عنوان از شرط‌های ایران برشمرد.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در کاخ سفید به خبرنگاران گفت ایالات متحده کل تنگه هرمز را «مین‌روبی» کرده و کنترل کامل آن را در دست دارد.
محمدباقر ذوالقدر، دبیر سابق شورای عالی امنیت ملی، که رضایی جایگزین او شده است، هفته گذشته شروط مشابهی مطرح کرده بود.
محسن رضایی درباره مذاکرات جمهوری اسلامی با سلطنت عمان درباره عبور و مرور در تنگه هرمز که طی هفته‌های اخیر در جریان است، نیز گفت اگر بین دو کشور توافقی در این زمینه حاصل شود، «این توافق موضوعی جدا از انسداد تنگه هرمز خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77822" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FhKYyNNClnWWmIOJvj2uu7q5PLfnZCju9lyFsaOMQXk2a-QBN4RSd96hMkpqul1tJRGwBwNJV0BTJAI5yEooaDu-4143D_4JLyL4OXNO2U-wbPr_yK5dugQ46p5DQ1PvTKpcNTd4-4dhOtSGpaCaeftwDhiZ27Jfm1m8YorinhHIGvO9wy1PQY3dGlE0zP-9e_QpfDUlRIlPUTjDfXCy9gv92cFUgwO1wTNVPu4JsfVqqrJBYFiierYwSJ8vzLsANGxYB65o2t9M5JsPtJeHRU7Igdqpby0nnvEB63JSbhiWSmXwwrintfsL3wVBUSySisoUnMIomhgFkokfDEAKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر مانع دستیابی آن‌ها به سلاح هسته‌ای نشده بودم دیگران ناچار بودند رهبران جمهوری اسلامی را «آقا» خطاب کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77821" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77820">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VY1IHSG-A9C0eXfoFzO_TtySujnSGgGsgJy_yPIznzEmdOHwWlH6gaR_iakbsjMjKkO3RLSMW6ISZ-q3hmaOyrA9MS-ZZI_EhcLcCtm6nerabfZ6LzAntxB9AkFkemRPQU2n0Uk_eeFnKGcTnFALt8ZntHxwSQ6zh83_YRqM8arm827uO27TMjhNdPgaTz5nm9BoAgDywdWeW938dPN20ptCGHksr89CHht3SydbS936YQEDP78kRoQnoedUPCa6VtfUW1uHchJnRZEnAri2Y71GQoVOJtie3TmoDv0BsLLR89ERt6Dcfz4c1ml1UO6kjaC-4LLuY2P5MBaxauEsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسی کوهن، مدیر پیشین موساد، گفت ماموران این سازمان در گذشته چندین بار از تاسیسات غنی‌سازی اورانیوم فردو بازدید کرده بودند تا اطلاعات بیشتری درباره این مرکز هسته‌ای به‌دست آورند.
به گزارش تایمز اسراییل، کوهن، روز سه‌شنبه ۲۰مرداد ۱۴۰۵، در نشست «مجمع جلیل» در شهر صفد، گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک کنیم.» او درباره زمان این بازدیدها و این‌که چه افرادی از سوی موساد در این بازدیدها حضور داشتند، توضیح بیشتری نداد.
او همچنین درباره حمله آمریکا به فردو گفت: «بمباران آن توسط آمریکایی‌ها تحقق همه رویاهای من بود.»
تاسیسات فردو، همراه با مراکز هسته‌ای اصفهان و نطنز، در جریان جنگ ۱۲روزه اسراییل و ایران در ژوئن ۲۰۲۵ به‌شدت آسیب دید.
گزارش‌های پیشین حاکی از آن بود که حدود ۴۴۰ کیلوگرم اورانیوم با غنای بالا که در این تاسیسات نگهداری می‌شد، زیر آوار مدفون شده است. با این حال، اسراییل بر این باور است که ایران پس از جنگ بخشی از این ذخیره اورانیوم را به سایت «کوه پیک‌اکس» منتقل کرده است.
کوهن همچنین گفت اورانیوم غنی‌شده تا سطح ۶۰ درصد همچنان فاصله زیادی با ساخت بمب دارد. این سخنان با ارزیابی برخی کارشناسان هسته‌ای تفاوت دارد. دیوید آلبرایت، کارشناس حوزه هسته‌ای، پیش‌تر گفته است اورانیوم ۶۰درصدی ایران می‌تواند در صورت تصمیم تهران برای ساخت سلاح، ظرف چند هفته یا حتی چند روز تا سطح مورد نیاز برای تولید جنگ‌افزار هسته‌ای غنی شود.
کوهن پیش از این نیز به‌طور علنی درباره فعالیت‌های موساد علیه برنامه هسته‌ای ایران صحبت کرده بود. او چند روز پس از پایان دوره ریاستش بر موساد در سال ۲۰۲۱، در مصاحبه‌ای کم‌سابقه با تلویزیون اسراییل، جزئیاتی از عملیات این سازمان علیه ایران را بیان کرد.
او در آن مصاحبه از انفجار در تاسیسات زیرزمینی سانتریفیوژهای نطنز سخن گفت و توضیحاتی درباره عملیات سال ۲۰۱۸ موساد برای سرقت آرشیو هسته‌ای ایران از یک انبار در تهران ارایه کرد. کوهن همچنین گفت محسن فخری‌زاده، دانشمند ارشد هسته‌ای ایران که بعدتر ترور شد، سال‌ها در فهرست اهداف موساد قرار داشته است.
کوهن در برنامه مستند «اوودا» با اجرای ایلانا دایان در شبکه ۱۲ اسراییل نیز گفت که با تاسیسات مختلف هسته‌ای ایران آشنایی نزدیکی دارد. او در این برنامه گفت اگر فرصت پیدا کند، دایان را به بخش زیرزمینی نطنز خواهد برد؛ جایی که به گفته او سانتریفیوژهای ایران در آن فعالیت می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77820" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kvg40WWK6btwLvsfxufg3w0dVm0CgH8fmfQaZg4824xA_8dRj2bEOYAJSszVWKDd3DTkbmSByzP04dAQR0zBTOVcfpduCnySXKhxVyqgkLQmPE1ZdSLci7KCxaD5Lw75-XPpDD5tzy4-xGzNLn25WOg0CZF0VyFh1bmi7A51Nj2xRgbdRKv0SU5ZpVaoeC_CYX4mr9aPctrgxXN3s__twjaWU42MO3QX4dT_vkQZPjgh9z2c3fMsFUruar2g4KsR3tplUWFduVmc9CY5Y74grz8V4SdnozbzGkcDzFkv6gnESlHf-BlbcXFfXBePjV0VjF_YWuINx_lJJhf6ouiS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار شبکه‌های تلویزیونی العربیه و الحدث عربستان سعودی روز سه‌شنبه، ۲۰ مردادماه، گزارش داد که در پی اصابت یک موشک بالستیک  حوثی‌ها به یک کشتی تجاری در تنگه باب‌المندب، سه نفر از اعضای خدمه این کشتی کشته شدند.
بر اساس این گزارش، قربانیان دو پاکستانی و یک تبعه اندونزی بودند. الحدث گزارش کرد این موشک از شرق استان تعز شلیک شده و کشتی تجاری را هنگام عبور از باب‌المندب هدف قرار داده است.
این حمله در شرایطی رخ داده که تهدید علیه کشتی‌های تجاری و مسیرهای کشتیرانی در دریای سرخ و تنگه باب‌المندب همچنان ادامه دارد. باب‌المندب یکی از مهم‌ترین گذرگاه‌های دریایی جهان برای تجارت و انتقال انرژی میان دریای سرخ و اقیانوس هند است.
همزمان، درگیری‌ها در چند جبهه یمن نیز ادامه داشته است. بر اساس گزارش «العربیه» و «الحدث»، نیروهای دولتی یمن مواضع و تجهیزات حوثی‌ها را در چندین جبهه هدف قرار داده‌اند.
@
VahidOOnLine
شمار کشته‌شدگان حمله حوثی‌ها به کشتی تجاری در باب‌المندب به ۴ نفر افزایش یافت
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77819" target="_blank">📅 18:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g_TGpSKRsQQZae1HC-mVg7QhM_la3xT2BP2TdcGUshj840PQb8KbvH7vFpB6-6zL9B8BefphKU8bvL1QhVFTrFiy5KPj2DzvwX6nRj6IYJgBGVQGkLxZYw1V8RuovPJSITNgEC_aGJHo1mKX4unQlxFG8mg3F1Y2CjRLReOec5oOIZDg4v5JgZUo7Ck3dgIUoGEhA9H_N4XOl2HkoaMNJEI83Pby_kEJHUFEjwN_NkA1h9cJ3gMGdbZiPA79h0IoEMz67AlH0vCkU_O8OXct0O9CBk_MRCKlTgpa6AKSJGp94WFlaX2xMiCORuZRm2v5leUKFUp3YVc5J_ja4KO-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی و منابع امنیت دریایی از هدف قرار گرفتن یک کشتی کانتینربر با پرچم پاناما در دریای عمان خبر داده‌اند؛ یک مقام آمریکایی می‌گوید این کشتی به هشدارها برای توقف توجه نکرده و در تلاش برای شکستن محاصره دریایی بنادر ایران بوده است.
همزمان، روزنامه وال‌استریت جورنال به نقل از یک مقام آمریکایی گزارش داد که یک بالگرد نظامی ایالات متحده پس از آن‌که خدمه کشتی هشدار نیروهای مأمور اجرای محاصره بنادر ایران را نادیده گرفتند، به سکان این کشتی شلیک کرد.
@
VahidHeadline
آپدیت:
پست سنتکام ترجمه ماشین:
اوایل امروز، نیروهای سنتکام تجهیزات هدایت کشتی
M/V Vela Nova
با پرچم پاناما را از کار انداختند؛ این کشتی باری در حالی که می‌کوشید از خلیج عمان عبور کند و با حرکت به‌سوی یکی از بنادر ایران، محاصره آمریکا علیه ایران را نقض کند.
پس از آنکه خدمه غیرنظامی کشتی هشدارهای مکرر نیروهای آمریکایی را نادیده گرفتند، یک بالگرد
MH-60
نیروی دریایی آمریکا دو موشک هلفایر به موتورخانه
Vela Nova
شلیک کرد. این کشتی دیگر برخلاف محاصره آمریکا در حال حرکت به‌سوی ایران نیست؛ محاصره‌ای که همچنان به‌طور کامل برقرار است.
تا ۱۱ اوت، سنتکام مسیر
۵۵ کشتی تجاری
را که می‌کوشیدند محاصره را بشکنند تغییر داده،
۳ کشتی
را که از دستورات تبعیت نکرده بودند از کار انداخته و وارد
۲ کشتی
شده است.
نیروهای آمریکا که در خاورمیانه فعالیت می‌کنند، به‌شدت هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/77818" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77816">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cowF-tregJeEn1Jl_j6ajTFug7_oxWma-gbuzZijaQ3Xk2e2ngf5SnzurR9Juo_ya-49uw1Rc6DpfLkgEldmA0Ap2WUAAV2zHzVaeVAnQrmUYw3aBfhU4KQnH5Lo6lmOcOWRZecBUP-35mnqk04mUsMXRGojAA6oVauIUzM5McRgbdOSB6YnlUphe1fL9MyJ55IzbTFN0WmjZ5REHnjrKMXyJsehaX8Ihr-3eheNuQv0r_FW3whCfIp9bvlbjfwucBLLmosLl50IV7_jA73uY2M271rH8XrjO7yDDMuLw2PeSxyIX5FC2knwhzDGgCTt3s_ZrWH7sGDK7dphbuJ_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bIexZqRMtu_-kLMLrTWDSzZrEcnPLPLylcGNfMa0ViAm9osyXD5OPu3n8rcV3kCPtX_SIgTczESVLsuPl8o2kSvg2uuhmPsNc81vWKsVOR2zUkpDN_cvVklyV6_rSZmIP2jQHbKc_7R1qjnbKIReQI0I64JUS6hGnZWmq1cOdpVrl9CVDtOnuFBgrt-QNTlgCXLsMXFNzsi4UB08F3OtjzG3pVr9WUagVYhnheWOYCTDcLE_eduwdfAAR79OJkAz1Xlg7jLmlKF5M74ywo5zIhHeRamrS075O9YvYdIfR_Ks8IhfQqaoxjcz9xEd0_zwLxMEO49LJtCdbn29srtH8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی وزیر کشور پاکستان، پس از ورود به تهران در عصر سه‌شنبه ۲۰ مرداد ماه با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران دیدار کرد. محسن نقوی پیش از دیدار با عراقچی، در تهران مورد استقبال اسکندر مومنی، وزیر کشور قرار گرفته بود.
@
VahidOOnLine
وزیر دفاع پاکستان می‌گوید ایران و ایالات متحده به «شکلی از توافق» نزدیک شده‌‌اند.
خواجه محمد آصف این موضوع را در قالب گفت‌وگویی با بلومبرگ، که روز سه‌شنبه ۲۰ مردادماه منتشر شد، عنوان کرد.
این مقام بلندپایۀ پاکستانی گفت: «روند تحولات جاری، بار دیگر به سمت‌وسوی یک توافق یا تفاهم صلح شکل گرفته است».
وزیر دفاع پاکستان تأکید کرد که «نشانه‌های مشاهده‌شده طی دو، سه روز اخیر حاکی از نزدیک‌شدن به نوعی توافق هستند».
هم‌زمان خبرگزاری ایسنا می‌نویسد که محسن نقوی، وزیر کشور پاکستان، «در چارچوب تعاملات دو جانبه و میزبانی اسکندر مومنی وزیر کشور» عصر سه‌شنبه وارد تهران شده است.
@
VahidHeadline
همزمان با ادامه تنش‌ها در تنگه هرمز، سخنگوی وزارت امور خارجه قطر روز سه‌شنبه ۲۰ مردادماه اعلام کرد که مذاکرات میان تهران و مسقط برای آینده کشتیرانی در این آبراه راهبردی بین‌المللی، به مرحله «پیشرفته» رسیده است.
به گزارش العربیه، سخنگوی وزارت خارجه قطر با اعلام این خبر گفت پاسخ‌های مثبتی از تهران دریافت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/77816" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OKDqc3WeEB-WOUbaVkZHDwMoHw33C5yrfDd7cyO5c-aD8mnqdpl_0WkByJjS4KdqgVGhZ8xOVHRw41yOVFXfIbPcDPBIsLB5AJEhKkvELQ3vqbnQpbmGGij0YQyWLtl2hmzx_0QM-xdIagDaap3m_CMye65XOCbjliZFWr1E047mmWbA9OojtE2CJyVYCLGL4tx6oncT_-dO4Y46m2_7jvTyYIZ5bReDOOcRYl7xeIkmsYT_CRs9f3R5tIX6MK8lZhZ-3ef57d53WMI7SOvTwXOwXwa7XgFWeIkYHNBDl4ud3N-Eat22-wFZxhwvmr9GkJ1a8HPfFU_jwt_bUhUctg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=kGTKImpk1yUYoolRNBSdKfgg3CJTJxzpxMd-yYU39SqZdIKosE9d9cRKD2LUNV9nfxA_TkfPySsLHJLVg7sv2guRL-97emKxF1uWB31i-rqcsPiBL_ZwqUqtN1YfFxfHc6zVaHH2m3q5eu4HY3A5p8DIEYa7quts2YPazFPgPaWrjGgkYqnBEExlZ2mcR_XSefqb8z7HKSf_kwQdS1gH9ZonGxilSnB-FzIwlaRcSzys4HCFLv76CS-36ZLQSKIg3X9_UWpMB-xPhzPO80fxAxK3Lpy2dYiBHubrYB5trZIMKcFiYXiok1y1_WgNKo6XNyTHVcj1liV5WeL7pfYu4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=kGTKImpk1yUYoolRNBSdKfgg3CJTJxzpxMd-yYU39SqZdIKosE9d9cRKD2LUNV9nfxA_TkfPySsLHJLVg7sv2guRL-97emKxF1uWB31i-rqcsPiBL_ZwqUqtN1YfFxfHc6zVaHH2m3q5eu4HY3A5p8DIEYa7quts2YPazFPgPaWrjGgkYqnBEExlZ2mcR_XSefqb8z7HKSf_kwQdS1gH9ZonGxilSnB-FzIwlaRcSzys4HCFLv76CS-36ZLQSKIg3X9_UWpMB-xPhzPO80fxAxK3Lpy2dYiBHubrYB5trZIMKcFiYXiok1y1_WgNKo6XNyTHVcj1liV5WeL7pfYu4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاهی در دمشق، پایتخت سوریه، روز سه‌شنبه ۲۰ مرداد ماه، بشار اسد رئیس‌جمهوری پیشین این کشور را در یک محاکمه غیابی به اعدام محکوم کرد.
فخرالدین العریان، قاضی دادگاه دمشق، روز سه‌شنبه اعلام کرد اسد به اتهام‌هایی از جمله «قتل عمد، کشتار عمدی بیش از یک نفر، قتل عمد کودکان زیر ۱۵ سال، شکنجه، شکنجه منجر به مرگ و سلب آزادی به دفعات» مجرم شناخته شده است؛ اتهام‌هایی که دادگاه آنها را «جنایت علیه بشریت و جنایت جنگی» طبقه‌بندی کرد.
دادگاه همچنین شش مقام نظامی و امنیتی سابق را به صورت غیابی به اعدام محکوم کرد که در میان آنها ماهر اسد، برادر بشار اسد و فرمانده لشکر چهارم ارتش سوریه، نیز قرار دارد. ماهر اسد نیز پس از سقوط حکومت برادرش از سوریه گریخت.
دادگاه کیفری دمشق از فروردین گذشته روند رسیدگی قضایی به پرونده اسد و شماری دیگر از مقام‌های سابق این کشور را که برخی از آنها در دادگاه حاضر بودند و برخی غیابی محاکمه شدند، آغاز کرد. این افراد به ارتکاب جنایت‌های گسترده در جریان جنگ داخلی متهم شده‌اند؛ جنگی که در سال ۲۰۱۱ با سرکوب شدید اعتراض‌های مسالمت‌آمیز علیه حکومت اسد آغاز شد.
در جریان این جنگ بیش از ۵۰۰ هزار نفر کشته و میلیون‌ها نفر آواره شدند و ده‌ها هزار نفر نیز ناپدید شدند؛ بسیاری از آنها به زندان‌های حکومت سابق منتقل شده بودند.
اعتراض‌های سوریه در مارس ۲۰۱۱ از درعا و پس از آنکه ۱۵ دانش‌آموز به اتهام نوشتن شعارهای ضدحکومتی روی دیوارهای شهر بازداشت شدند، آغاز شد. ساکنان درعا اعلام کردند این دانش‌آموزان شکنجه شدند و در پی آن، اعتراض‌هایی برای آزادی آنها شکل گرفت که با خشونت سرکوب شد.
نیروهای امنیتی برای متفرق کردن معترضان از گلوله جنگی استفاده کردند و اعتراض‌ها به دیگر استان‌های سوریه گسترش یافت.
خانواده اسد بیش از پنج دهه بر سوریه حکومت کردند. بشار اسد در سال ۲۰۰۰، پس از مرگ پدرش حافظ اسد، به ریاست‌جمهوری رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/77814" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g99xe32JvQ3hsL_xF-Phow4WyryQ11HNIJ8LLDIBRC16Oi594dcembVg-VL2M2Swzvj5XeMZpR6pLKRl_Nqu3WIIHS0_dfRDI8FDZErvZXY1KCxdeTjbREKBmNONLhjweTq7eAZtyMlFyQgPqF_f2FkNvHXn8YOBnMCnXKB-QBxjOm1NfixVtyL4Lw9IJoOfHW3uTW8K8KQ_Vl90kUhTUc24bPqXdevHI1XvXaQGAs-R_gPre-Z4sLaWs04ic5izuDnYepLr57SQ-EY13CcJLR-Lf4DWvRAzTr8JYkg0XqABE-DtEdvsA9-jRg0Q93pOspV-EiGISKf58uiS6Pgx8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارلمان لبنان روز سه‌شنبه مجازات اعدام را لغو کرد و این کشور نخستین کشور جهان عرب شد که این مجازات را با حبس ابد همراه با اعمال شاقه جایگزین می‌کند.
اکثریت نمایندگان پارلمان ۱۲۸ نفره لبنان به لغو اعدام رأی دادند.
فراکسیون حزب‌الله تنها گروهی بود که با آن همراهی نکرد.
عادل نصار، وزیر دادگستری لبنان که در جلسه حضور داشت، آن را «گامی تاریخی» برای کشورش خواند.
سازمان‌های حقوق بشری که خواستار رسمی‌کردن توقف اجرا یا لغو کامل اعدام بودند نیز از این رأی استقبال کردند.
@
VahidHeadline
بر اساس این مصوبه، مجازات اعدام با حبس ابد جایگزین می‌شود. با تصویب این قانون، لبنان از کشوری که سال‌ها اجرای اعدام را عملا متوقف کرده بود، به کشوری تبدیل می‌شود که این مجازات را به‌صورت قانونی نیز از نظام کیفری خود حذف کرده است.
عادل نصار، وزیر دادگستری لبنان، تصویب این قانون را گامی تاریخی توصیف از لغو مجازات اعدام حمایت کرد.
لبنان آخرین بار در سال ۲۰۰۴ حکم اعدام را اجرا کرد و از آن زمان، اگرچه مجازات اعدام همچنان در قوانین این کشور وجود داشت، اجرای آن عملا متوقف بود.
حامیان لغو اعدام می‌گویند این تصمیم علاوه بر جنبه حقوق بشری، می‌تواند در روابط قضایی لبنان با کشورهایی که اجرای مجازات اعدام را ممنوع کرده‌اند نیز تاثیرگذار باشد؛ از جمله در روند استرداد متهمان و مجرمان، زیرا برخی کشورها مجرمان را به کشوری که احتمال اجرای حکم اعدام در آن وجود دارد، مسترد نمی‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/77813" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77812">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mRFHOVEZLI4BzvjMtY0HkEBR-35V2Xkbl8cAePczsbFbv0YwyVKZ7m_x6_B05NImSEEUz7G5kBwcmDa9WA3H9jw7HT3lgx7IIaNy2N0rAXcm8E0I9NMAsoEW7sch3bKsTD0GbXmdRI4CaW_9c7Je3jWArnO4072mehTnCsuFcDjW9eH3p6oTj1Q7ABT2cWFZmAu2EDQI8jgf2XhDYe0jUouc2xQ9RKcqvNqC0CtzPxNAxLLMEeH4NhtFpvByTmjPvKooudn16RYeXiWosybQMg-s1kfTlt74GY-blt49DSyiYWQ9Cqpt9OVDPs-so3QK9Yfi-0lPZsg9kNI18hBo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا می‌گوید واشنگتن سه راهبرد برای جمهوری اسلامی در اختیار دارد و در این مرحله بر محاصره دریایی و فشار اقتصادی تکیه می‌کند.
دونالد ترامپ در گفت‌وگو با برنامه «آمریکا سخن می‌گوید» در شبکه «صدای واقعی آمریکا» گفت: «می‌توانیم همین‌طور رهایشان کنیم و آنها شکست خواهند خورد. می‌توانیم همین کاری را که الان می‌کنیم ادامه بدهیم؛ به‌نوعی آرام و راحت جلو برویم.» او گزینه دوم را «واقعاً سخت ضربه زدن» و گزینه سوم را «شکست‌دادن آنها از نظر اقتصادی» خواند و افزود گزینه سوم هم‌اکنون در حال اجراست.
ترامپ گفت: «از نظر اقتصادی، آنها به‌هم‌ریخته‌اند. نمی‌توانند پول قرض کنند. ما پولشان را کنترل می‌کنیم؛ پولی که داشتند و مقدارش هم زیاد بود. من بانکدار آنها هستم.»
او افزود: «آنها ۳۰۰ درصد تورم دارند. پولشان هیچ ارزشی ندارد. به سربازانشان حقوق نمی‌دهند. سربازانشان دارند ترکشان می‌کنند. فقط همین وضعیت را ادامه بدهید، چون قابل دوام نیست.»
ترامپ مذاکره‌کنندگان جمهوری اسلامی را «بسیار فریبکار» خواند و گفت: «با چیزی موافقت می‌کنند و بعد می‌روند به رسانه‌ها می‌گویند که چنین کاری نکرده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/77812" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77811">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mvV5kujAH4D2R2hXVIzpam1DI8Tnpp5iaD-tHH7I1_eAUHHAsMuYX4cdwG2198L09zjxpTN4vbzZH4OELvEbesnCcfn22mJJSWkThczKgKKlI4i_QqzFX3YFzd1Ov8sSczYaT5lT0CJSrzm-VBBec6hlb3B-hmGG06-ilzqh32-coiDcVCOIlpLQK338GdUq50yQ48WX79HXoPKMC-NU7nu41T0sdIsVs9MfZfo2Vr1WYt90zlxxJn_ZQed_Bl7GHS1hWjgrtG-nNCfNAfYl4d9dTGZNbdlEHoGS2OW-7THM77pY3kFcckWBLYoR0MQdOTZS9ZxogsulxhIzZoj1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی احمدی، معلم بازنشسته ۷۱ ساله، پس از بازداشت در ۱۵ اسفندماه در ممسنی، همچنان در زندان عادل‌آباد شیراز نگهداری می‌شود و نگرانی‌ها درباره سلامت او ادامه دارد.
احمدی هنگام بازداشت در دوره نقاهت پس از دو عمل جراحی چشم و پروستات بود و بنا بر این اطلاعات، اکنون با مشکلات قلبی نیز مواجه است.
او با اتهام‌هایی از جمله «افساد فی‌الارض»، «همکاری با موساد» و «تخریب اموال عمومی» روبه‌رو است.
با وجود داشتن وکیل، پرونده او از زمان بازداشت پیشرفت محسوسی نداشته و دسترسی وکیل به پرونده محدود بوده است. وکیل او نیز پیشتر یک بار بازداشت شده است.
بر اساس این اطلاعات، از زمان بازداشت احمدی هیچ ملاقات حضوری با او انجام نشده و تنها یک تماس تلفنی چندثانیه‌ای در روز عید برقرار شده است.
همچنین درباره وضعیت جسمی و روند پرونده او اطلاعات دقیقی در دست نیست.
احمدی پیش از این نیز چند بار به دلیل پیگیری مطالبات صنفی فرهنگیان بازداشت شده بود. ادامه بازداشت او همچنین خانواده‌اش را با مشکلات مالی مواجه کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77811" target="_blank">📅 18:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77810">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=kTfRnPhbHzLZanpvpfdIwex43wkwcgYFg3a82ukb0u1_ildi7nGKQnCMEPZgdQsBNOFwvo3vPUNdsVlEuyOSbtnyAwuh5z3xFJByKd7jzIieyjAjIxeeSQ8Ex-P5Hgtqn0bovzNtAVzdFAATam4K_w8Nm3v66VcFMSYyHNVy5o95YaHz2-DdZMhapjJCZlyhDAxPjXU9li2T3tswRw7RW3y1SkoGp-c_xzLvGGdSxNkU2vZ9Rd1rt8EXZcL6S0Pz1pdTYqL9RJTuSj352gjN6IwO9lbk1eaqSfp2ffx7wrozWK3vSAkxbJNd3aLDOmshLkQoIGy3StUgurmVGDhMxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=kTfRnPhbHzLZanpvpfdIwex43wkwcgYFg3a82ukb0u1_ildi7nGKQnCMEPZgdQsBNOFwvo3vPUNdsVlEuyOSbtnyAwuh5z3xFJByKd7jzIieyjAjIxeeSQ8Ex-P5Hgtqn0bovzNtAVzdFAATam4K_w8Nm3v66VcFMSYyHNVy5o95YaHz2-DdZMhapjJCZlyhDAxPjXU9li2T3tswRw7RW3y1SkoGp-c_xzLvGGdSxNkU2vZ9Rd1rt8EXZcL6S0Pz1pdTYqL9RJTuSj352gjN6IwO9lbk1eaqSfp2ffx7wrozWK3vSAkxbJNd3aLDOmshLkQoIGy3StUgurmVGDhMxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد
ترجمه ماشین:
واشنگتن‌پست
دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه پرواز کرد، در حالی که کاخ سفید اعلام کرده بود او سوار ایرفورس وان است.
این مأموریت محرمانه که پیش از این گزارش نشده بود، بدون اطلاع خبرنگاران و حتی برخی کارکنان کاخ سفید انجام شد؛ افرادی که تصور می‌کردند در همان هواپیمایی هستند که رئیس‌جمهور در آن حضور دارد.
دولت مدعی شده است که ترامپ روز ۸ ژوئیه با «ایرفورس وان سابق» ترکیه را ترک کرده است.
در آنکارا، ترامپ در برابر دوربین‌های تلویزیونی سوار ایرفورس وان قدیمی، هواپیمای غول‌پیکر جت، شد. اما به گفته مقام آمریکایی و بر اساس مطالب تأییدکننده‌ای که واشنگتن‌پست بررسی کرده، دقایقی بعد به‌طور مخفیانه با یک کامیون پذیرایی فرودگاه ــ از همان نوعی که معمولاً برای بارگیری غذا و دیگر ملزومات پیش از پرواز استفاده می‌شود ــ به هواپیمایی کوچک‌تر، یک C-32A نیروی هوایی، منتقل شد.
به گفته این مقام، در نتیجه ایرفورس وان، با حضور خبرنگاران و برخی کارکنان کاخ سفید در داخل آن، نقش یک «طعمه» را ایفا کرد.
متن کامل ترجمه فارسی گزارش
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77810" target="_blank">📅 04:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sma7aKtL5qB0GCoKi5p_l71R4FADhxPst25XHm8aaiYvRuctPYVnFFOyfaQbCuZiqf444iRQEotgcLg2vWbeIPIBNjf1viHGDE9dfKpb5vvhqggJufAXX4igRDW7drX2ZBCAiTpKrk7ohsoWsMymzygRFJGczchqfM5wa_NhHjZR5lD1XXoR1Vys833MtbLg4bSQasOqC3AeHmobqI3iwo8kW_vd9pyRQmQlvaYKMSXndKiYCfcDL72vIgtV_NXbVf72urqKbBtLn_QSRbsAJC4TMzj-2bsGgxlUkuY5VSdsncxu2Ri10IO_Eyok0J1-zAyXaGXvAVwHUYLhCC9jmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا بار دیگر نموداری را که نشان می‌دهد ارزش ریال در ایران در دوره دوم ریاست جمهوری او سقوط کرده ‌است، منتشر کرد. این نمودار نشان می‌دهد که ارزش یک میلیون ریال از یک دلار و یازده سنت آمریکا به ۵۳ سنت کاهش یافته و به «داخل زباله» رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77809" target="_blank">📅 04:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrEbFEEmDyfxFJXPWpO8UX_1w9y1jWklgmLxwbKvGIm-LxIkQv53U8cR9NRhqjo4CHXY7YMIx9RWHwvhoCidqaL0EVQSmzIpD_8WowguVcTOkeXxF-zRaJFLmzf4o-i3aoX1EHhOfoAZl2KB41L1s3RfcR64cqJ_Q038OViTzLKYFpjeEn9IDS-kdCSXr4qJPyZzGb-14JcJ-b7bKkuwcvW-sylBbo1LAFiSiJB244hn4bvuEgsoIF4IuaQnmg-WtgQZJBMC8zJlGYeaStHDN-XlhaUCBlEY50zHoUWTota-4t6bHf9i5a9CRWIUcRvnG4JFYmTPKRWjuQoMjok9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «آکسیوس»، آژانس بین‌المللی انرژی اتمی به‌زودی مواد هسته‌ای باقی‌مانده در یک سایت مخفی در سوریه موسوم به «سایت ۹۹» را پس از توافق‌های محرمانه دولت ترامپ با اسرائیل و سوریه، از این کشور خارج خواهد کرد. این مرکز که در زمان رژیم بشار اسد برای نگهداری کیک زرد و بقایای رآکتور هسته‌ای «الکبر» استفاده می‌شد، پس از سقوط اسد به شدت تحت نظر اسرائیل قرار داشت و حتی ارتش اسرائیل برای جلوگیری از دسترسی به آن، ورودی‌های سایت را بمباران کرده بود. اگرچه این مواد برای ساخت سلاح هسته‌ای کافی نیستند، اما مقامات آمریکایی و اسرائیلی بیم آن را داشتند که در ساخت «بمب کثیف» و آلوده‌سازی منطقه‌ای مورد استفاده قرار گیرند.
براساس این گزارش، در ماه‌های اخیر و پس از مشکوک شدن اسرائیل به تحرکات حکومت جدید سوریه و احتمال مداخله ترکیه، تل‌آویو تهدید به حمله مجدد کرد، اما دولت ترامپ با مداخله به موقع و وارد کردن آژانس بین‌المللی انرژی اتمی به ماجرا، مانع از تشدید تنش و بروز بحران نظامی جدید شد. در نهایت، سه هفته پیش توافقی میان دمشق و آژانس به امضا رسید تا این مواد خطرناک به صورت ایمن بارگیری و منتقل شوند. مقامات واشنگتن این موفقیت دیپلماتیک را نشان‌دهنده رویکرد موثر دولت ترامپ در تعامل با حکومت جدید سوریه و حل‌وفصل بحران‌های پیچیده مانده از دوران اسد می‌دانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77808" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=iFCrOrqVuMtQVkBEWKSE_PvndcmfPT86EgNO4NkQ_XxxlY1xcE0YtSe7W4PhVIZ5jkbXfXMcztSV_hLRF_4ECkRYJyjx9lqYBP9tW4x-C7-1jcrTKNqYA5MVqi2PRO8tsGNGhN31bx1aAfYw509yRrIa5xd4KuSzA7cinOp_doEtt-etBt7rx8HnyKVrFUZ2XnW7XkANcOubDrlwUamPFnduQyRSl9C27RerKw6XL92tvj5Os1zhpUnxiJZkCk7b4ITYpfvx-lE2fsxZn-CNdJ_b4IWU3AJVLYQEKOZ9G0krQDehdtGhEafRRJNm5tiEo5uqixCiSzQYxjHDShA7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=iFCrOrqVuMtQVkBEWKSE_PvndcmfPT86EgNO4NkQ_XxxlY1xcE0YtSe7W4PhVIZ5jkbXfXMcztSV_hLRF_4ECkRYJyjx9lqYBP9tW4x-C7-1jcrTKNqYA5MVqi2PRO8tsGNGhN31bx1aAfYw509yRrIa5xd4KuSzA7cinOp_doEtt-etBt7rx8HnyKVrFUZ2XnW7XkANcOubDrlwUamPFnduQyRSl9C27RerKw6XL92tvj5Os1zhpUnxiJZkCk7b4ITYpfvx-lE2fsxZn-CNdJ_b4IWU3AJVLYQEKOZ9G0krQDehdtGhEafRRJNm5tiEo5uqixCiSzQYxjHDShA7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز دوشنبه در گفتگو با خبرنگاران در کاخ سفید با تاکید بر تسلط نیروی دریایی ایالات متحده بر تنگه هرمز گفت: «تنها نیرویی که در حال حاضر بر تنگه هرمز تسلط دارد، نیروی دریایی ایالات متحده است. ما محاصره‌ای برقرار کرده‌ایم که خطاناپذیر و مانند یک دیوار فولادی است.»
رئیس‌جمهوری آمریکا با بیان اینکه اجازه رفت‌وآمد کشتی‌ها بر اساس تصمیم واشنگتن انجام می‌شود، افزود: «ما اجازه ورود کشتی‌ها به ایران را نمی‌دهیم و آن‌ها اجازه ورود به تنگه برای رفتن به سمت ایران را ندارند، اما مسیر برای دیگران باز است.»
او همچنین با اشاره به پاک‌سازی مین در این آبراه راهبردی تصریح کرد: «ما تنگه را مین‌روبی کرده‌ایم و ۱۰۰ درصد بر آن تسلط داریم. آن‌ها ممکن است مشکلاتی ایجاد کنند، اما ورشکسته هستند و هیچ پولی ندارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77807" target="_blank">📅 00:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLxgDSMTNd3ZBa-az-3wzfU6Q3WpKXGx-Qh0JjbDsFjouhxym-AQmQaBZjCzsrTn3NhZSgAgSE7rgv7LGxDc9aJdPLiklkEhyDn_ja7mY2zP4-_5dWznnisPNDcmErsWcPBwXIF7nhVMP7jCjk6kThycVwURYWFK7YHTlhTEdduWrisic9yzwthwbgYAW7Xg5w3R7fzPwLveVOv9NT7HVUcY3uWWdx9eJTlkJgUABzQ5XKgNYbnWRriL1oq0NcoecA9Z_OEyCXprJnV7zilppzml--hjNo7o1SyoY9NBDNnDQ0h-m3fdcA87zTG9d0VW0IwPsm5qVluwnJAWOaW6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه ۱۹ مرداد و پس از مطرح شدن موضوع پرداخت غرامت بین ایران و آمریکا و کمرنگ شدن امیدها برای بازگشایی تنگه هرمز حدود ۵ درصد افزایش یافت.
ایران اعلام کرده که آمریکا باید تحریم‌های اعمال‌شده علیه تهران را لغو کند و برای بازگشایی این آبراه حیاتی، چند شرط دیگر را نیز بپذیرد. در مقابل، دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت ایران باید بابت «تمام افرادی که کشته یا به‌شدت مجروح کرده است» غرامت بپردازد.
قیمت هر بشکه نفت خام برنت در پایان معاملات با ۴ دلار و ۱۷ سنت، معادل ۴.۹۹ درصد افزایش به ۸۷ دلار و ۷۲ سنت رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز با ۳ دلار و ۹۵ سنت، معادل ۵.۰۵ درصد افزایش، در قیمت ۸۲ دلار و ۱۳ سنت در هر بشکه بسته شد.
درصد افزایش قیمت هر دو شاخص نفتی، بالاترین میزان از هفتم مرداد بود.
هر دو شاخص نفتی هفته گذشته بیش از ۷ درصد کاهش یافته بودند؛ زیرا امیدها به نزدیک بودن ایران و عمان به توافقی که می‌توانست به بازگشایی تنگه هرمز منجر شود، افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77806" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gCUVd6J4r1FlyHdKoJ15lLJrNMprt44HBAAnRbUh_A_W5EWKbNHAqTBruOZXkD4sX0VWn70sQGyBL-2NU07sLdcuGt-JzuJy3LjvJo3AbGEOwV1KS47fgCN1dTe7wJDBhggF5c3pC91xWOiy1TzdSnne7L_36AcQsGskhsW-vOkaH_m0GpxKCP4AykyR37bCKhjYPQjn1Go2GHT5IknPlR2VLJNoL-2ks9K5RrWHc1yeW2NdcQPJURojfYmfNxJZCnG7sxMUqc-RWgmPzDxZpbceMgN8hiDcURi_ad9T3MpBMXOe7_IP1aMYov3Isekg_kxiRuwGENRHJ3WFSncCZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست تازه ترامپ در ادامه متن یک ساعت پیش:
همچنین، در ارتباط با مذاکرات با ایران، ایران باید مسئول خسارت‌ها و مرگ‌ومیرهایی باشد که برای مردم لبنان، سوریه، یمن و غزه به بار آورده است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77805" target="_blank">📅 21:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77804">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iGIWiB7ZQg8zqxC6SPe4I1Rp9C2dbGjlfCFReWrKjNMH1GNZ6FlY9GEGm50IUR49fo84Ddh5_ebo20gPzWzvKhzVJBt5J03J6faJq8L_CInWwoUaKWvCCIEmjHe2WTnui6-l5elCcLFaVbP3_quJm2f5mv_Ot7D8JGTvVHo6rb-dau6AWlqYX8MAKMYdOU2cIZsxbDyCOFEFEYW9a_m-AzvUUWoO3jo9bUunqgrIzWTWreHD7PgRuED7P8bMZ70fpxCmNvrETTjpjcWgwKn5qccEHAzaNrT8JNNOh2vqVQ3brtMuL-bHDz_42YR90UJ18rQm6Qi-P14KlVG-LIOARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در مذاکرات موضوع پرداخت غرامت به ایران مطرح نشده، جمهوری اسلامی به خانوده‌های کشته‌شدگان غرامت بدهد
ترجمه ماشین:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج‌ماهه اخیر به آن‌ها وارد شده است (درگیری‌ای که به این دلیل آغاز شد که، آن‌ها
سلاح هسته‌ای نخواهند داشت
)؛ با اینکه این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما ایده جالبی است، چون حالا من نیز به همین ترتیب از ایران غرامت مطالبه می‌کنم؛ بابت همه افرادی که با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد ــ که به آن‌ها شهرت دارند ــ کشته یا به‌شدت زخمی کرده‌اند؛ اقداماتی که در ابتدا تحت رهبری ژنرال سلیمانی انجام می‌شد، از جمله بابت خانواده‌های کسانی که در ناو «یواس‌اس کول» کشته شدند، و هزاران نفر دیگری که در نبرد جان باختند.
علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه رسد به ۵۲ هزار نفری که در پنج ماه گذشته کشته شده‌اند.
به نمایندگانم دستور داده‌ام که این موضوع را قاطعانه در تک‌تک مذاکرات آینده مطرح کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77804" target="_blank">📅 20:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVDtNgGKTzutmih23bHaeT88ymIvRMOwnP5LN622N3-KeIaTYJJ2Lnv9CFra_aK1uae8C1Ytu0tRkjIppqu-a9A2NtkexIzWZ3zCakEzey5dxcP9oFO1WEECc2qBL-zqk-RCdg2_xzIzaJZYLvSglGJO6YAkVIzP9ZbZPlaOqAJLZQniR6EwfOa6B1ivIJHh5om2M4foGMjITKZ1lRDr5--EDWox9inarFt0jdmwvxIztp5EzBqwniTPMOPK_QbZNHftJvsIw8wCTdQ7ksshRBUaMA2C74ci2aZCQi49CrgwJT8EdUDEhVTA0mpe47QB_qJEcAZ9uraUTJsaeL7N3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احکام منسوب به مجتبی خامنه‌ای برای انتصاب شش فرمانده ارشد نظامی؛
بازگشت رسمی حسین طائب به قدرت
دفتر رهبر جمهوری اسلامی روز دوشنبه ۱۹ مرداد خبر داد که مجتبی خامنه‌ای احکام انتصاب شش فرمانده ارشد نیروهای مسلح را صادر کرده و خواستار آمادگی برای «عملیات تهاجمی پرقدرت» علیه آمریکا و اسرائیل شده است.
بر اساس احکام‌ منسوب به مجتبی خامنه‌ای، علی عبداللهی که فرمانده قرارگاه مرکزی خاتم‌الانبیا بود، به عنوان رئیس ستاد کل نیروهای مسلح و کیومرث حیدری به عنوان جانشین رئیس این ستاد معرفی شده است.
رئیس قبلی این ستاد عبدالرحیم موسوی بود که ۹ اسفند سال گذشته در نخستین دقایق حملات آمریکا و اسرائیل کشته شد و ستاد کل نیروهای مسلح ایران در حدود پنج ماه گذشته بدون رئیس به کار خود ادامه می‌داد.
موسوی تابستان سال گذشته جایگزین محمد باقری، رئیس پیشین این ستاد، شده بود؛ باقری خرداد سال گذشته در حملات اسرائیل در ابتدای جنگ ۱۲ روزه همراه با شمار دیگری از فرماندهان ارشد نظامی جمهوری اسلامی کشته شد.
مجتبی خامنه‌ای در حکم صادر شده برای عبداللهی خواستار «تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیا» شده که به گفته او «تدبیر» آن در زمان رهبری پدرش آغاز شده بود.
او همزمان با انتصاب عبداللهی در سمت ستادکل نیروهای مسلح برای فرمانده جدید قرارگاه خاتم‌الانبیا حکمی صادر نکرده است.
احمد وحیدی که از آغاز جنگ و در پی کشته شدن محمد پاکپور، فرمانده‌ کل سپاه پاسداران شده بود، روز دوشنبه بر اساس حکم رهبر جمهوری اسلامی درجهٔ سرلشکری و حکم فرماندهی این نهاد قدرتمند نظامی، امنیتی و اقتصادی را دریافت کرد. او پیش از آغاز جنگ ۴۰ روزه، جانشین فرمانده‌کل سپاه بود.
احمد وحیدی از اعضای ارشد و تندرو سپاه پاسداران سابقه فرماندهی نیروی قدس سپاه پاسداران را دارد و به اتهام دست داشتن در انفجار مرکز یهودیان، آمیا، در آرژانتین از سوی اینترپل تحت تعقیب است.
او به جز مناصب نظامی، در دولت ابراهیم رئیسی، رئیس‌جمهور سابق ایران، به مدت سه سال وزیر کشور بود.
در حکمی که به نام مجتبی خامنه‌ای برای احمد وحیدی صادر شده است، رهبر جمهوری اسلامی خواستار «ارتقاء مستمر و همه‌جانبه‌ توانمندی‌ها به منظور بازدارنگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن» شده است.
بر اساس حکمی جداگانه، مصطفی ایزدی نیز مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفته است.
مجتبی خامنه‌ای در حکم دیگری علی عظمایی را به عنوان فرمانده نیروی دریایی سپاه منصوب کرده و او جانشین علیرضا تنگسیری شده که فروردین ماه در جریان جنگ ۴۰ روزه کشته شد.
مجتبی خامنه‌ای حسین طائب، رئیس پیشین سازمان اطلاعات سپاه، را نیز به عنوان فرمانده سازمان بسیج معرفی کرده است.
از طائب که کار امنیتی را از وزارت اطلاعات آغاز کرد و سپس کنار گذاشته شد و سپس در سپاه پاسداران نهاد اطلاعاتی موازی ایجاد کرد، به عنوان یکی از اعضای حلقهٔ امنیتی و سیاسی قدیمی اطراف مجتبی خامنه‌ای یاد می‌شود؛ حلقه‌ای که سابقهٔ آن به بیش از دو دهه پیش باز می‌گردد.
محمد سرافراز، رئیس اسبق صداوسیما، دربارهٔ نقش پشت‌پردهٔ مجتبی خامنه‌ای در تصمیم‌سازی‌های سیاسیِ مقام‌ها، سخن گفته است. او که خود در مقطعی عضو این حلقه بوده، از ارتباط مستقیم مجتبی خامنه‌ای با حسین طائب یاد کرده و گفته او به گزارش‌های امنیتی طائب علاقه‌مند بود.
او در تیرماه ۱۴۰۱ از سازمان اطلاعات سپاه کنار گذاشته شد، اما بر اساس گزارش‌ها یکی از چهره‌های مهم و نزدیک به مجتبی خامنه‌ای به‌شمار می‌رود.
مجتبی خامنه‌ای در حکم خود برای حسین طائب گفته چند مورد را «مورد انتظار» خود خوانده که یکی از آنها «تقویت شبکه‌ی اطلاعات مردمی، افزایش مهارت‌ها و آموزش‌های لازم توأم با بصیرت‌افزایی و بهره‌گیری از فناوری‌های نوین برای مقابله‌ی مردم‌پایه با تهدیدات دشمن» شده است.
او همچنین خواستار تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت حامیان جمهوری اسلامی که از ابتدای جنگ ۴۰ روزه در تجمع‌های خیابانی حکومتی شرکت می‌کردند برای «حفاظت از انقلاب اسلامی» شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77803" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77802" target="_blank">📅 18:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77800">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0943082a05.mp4?token=TJ_i6cfe7soSC3qVy62HaqYXOn5JkD_Bk74nIqJjKPQtDe1DE_qm6wzZi0eypaUfncda_r2GZJEfQy841G8fbGEYhdELGZlnDbU_7OAFO2EWU9QIs7d81jwHHlRYvTf3ZSXSqiZCoPFicWvjzjFbt1x-aliIZbAQmwuuhakaexZJfXPTfWUSCQDSaDD0YYlrmQ7c6_Z2tH620AmulH8OoJ-YDFik-SE5ZExtDYIIH0C8PBpFWPQTu0zXRZQEfbIUxVg2rodTjtpLlZOt97cS6WxmO35vT-Vj1HYIlR8A0cCG4twmFdXKMf8uo7NuUm5fowvDnhFUUyS11UYyyyy0DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0943082a05.mp4?token=TJ_i6cfe7soSC3qVy62HaqYXOn5JkD_Bk74nIqJjKPQtDe1DE_qm6wzZi0eypaUfncda_r2GZJEfQy841G8fbGEYhdELGZlnDbU_7OAFO2EWU9QIs7d81jwHHlRYvTf3ZSXSqiZCoPFicWvjzjFbt1x-aliIZbAQmwuuhakaexZJfXPTfWUSCQDSaDD0YYlrmQ7c6_Z2tH620AmulH8OoJ-YDFik-SE5ZExtDYIIH0C8PBpFWPQTu0zXRZQEfbIUxVg2rodTjtpLlZOt97cS6WxmO35vT-Vj1HYIlR8A0cCG4twmFdXKMf8uo7NuUm5fowvDnhFUUyS11UYyyyy0DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز دوشنبه ۱۹ مرداد اعلام کرد دیدار اخیرش با مجتبی خامنه‌ای، رهبر جمهوری اسلامی، «حدود هفت ساعت» طول کشیده و به گفته او «از هر دری گفتیم».
مسعود پزشکیان در گفت‌وگو با تلویزیون حکومتی ایران گفت: «تقریباً حدود هفت ساعت خدمت ایشان بودیم و دربارهٔ تمام مسائل کشور توانستیم گفت‌وگو کنیم».
از این دیدار عکس یا صوتی منتشر نشده است.
پزشکیان در ادامه درباره وضعیت جسمانی مجتبی خامنه‌ای اعلام کرد: «از نظر وضعیت سلامت کاملاً سالم بودند. کسی که می‌تواند هفت تا هشت ساعت بنشیند و بحث کند، نمی‌تواند از نظر سلامت مشکلی داشته باشد. بسیار راحت حرف‌های ما را گوش می‌دادند و بحث می‌کردند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77800" target="_blank">📅 17:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXieyDLl0cYd5LKCUvvYIRto6BU1PSWac4cP2aG7fTdlA5mbL4IXVog4lIdpcLlBKrkERiTGX1RJhsa0H5vR7_PnQBZpjC5K22V7dyGAfPp06j_3JzA6Xb4ZpNLuZp_ykimWz_JHK7Tg6rtBY7pdljE-hO9bo-iuT9UhuEZp6Jb1oKao_zx-SPtfvDAsRGhFh9n909LSsbtLJQt9-RtaUxFjnVfCEDVZdjAJC6jAEYVBLfEB9ICsjx2uc7NaU5wtJXA89mOelrkTkzJcyhRJZ5biKkYVJaV6WK1YY0YRfs8a3P7syFzHFCwL5cVTRlZIZLddzrU7jhpbBeI6hRhNbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، یک کولبر ۲۵ ساله بامداد دوشنبه۱۹مرداد۱۴۰۵، در پی تیراندازی نیروهای نظامی جمهوری اسلامی در منطقه مرزی «هنگه‌ژال» شهرستان بانه جان خود را از دست داد.
خبرگزاری هرانا به نقل از کردپا، هویت این کولبر را «محمد توحیدپنا»، ۲۵ ساله، فرزند عثمان و اهل روستای «وزمله» از توابع بخش سرشیو شهرستان سقز اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77799" target="_blank">📅 17:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k58SAXO0yXqwRlHcoKXn-O9pdoiKhlbUqhNNoNJ2bdlckk5yfksuXZ8tDyEfSoIiNamlZVrqrI3zkAE4QwWVcZhWnxg5P1m8ZlRQ6hcDB2TAnc51GKb0Def1uG9yDt7rNNmyu7E175FBakjO7Y7w8o4JVdbgCpYkQmiDa4AbofdO6p7j099DA0Wr1xHdehBX34ltGYzqWzq_fr3lN51IqDTGmpsiKjRWmOgg3g9ef0DBF20jVuIj6vTp2pIrEX4rJyDcOxuJVn5J7QU2XCi0uklTPo9DfkdfD3Un92jFjb_YVFE3mtuV82Y9RjErcSkMcB239VGN6nh0Di12AOSXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، یکشنبه بعد از ظهر به وقت شرق آمریکا با انتشار نموداری در شبکه اجتماعی تروث سوشال، به کاهش ارزش پول ایران واکنش نشان داد و نوشت: «۵۱ سال رفتار بد!»
realDonaldTrump
در تصویر منتشر‌شده، با عبارت «ایران هیچ پولی ندارد» تاکید شده است ارزش یک میلیون ریال از حدود یک دلار و ۱۱ سنت در سال ۲۰۲۵ به نزدیک ۵۳ سنت در سال ۲۰۲۶ کاهش یافته است. ترامپ توضیح دیگری درباره منبع آمار این نمودار ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/77798" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j6VkC9R7HS2qeHkWrqfKYteeJbcjRev4S05CxGD2-iOfIU8tE90yR7rVU8Wyqph145p34CRy23jVku3JuLJu8Qrd5tpIfTu6_A0P_XpheUMsLKHrMPEHvySjGJip--Jir-knYQBWIYxPoSR95bxSsVsel1uCUVBw_kMHnXk6yPSqATobFmvr9CzNvoZ4H3JkgYCDCmOzR-kaCcvzULqhEPi0hmrFzvBGaNsnCGvc9pgTTUh1surfDMH5jFnEQ1uhE49YC9-jXQytRG-0f4wCjf4Ugms6djFmQOr8mmSEm4vcCzZY7anbW_QYB4vX6aIdJ77Mj9tx4Rem5HEUH0phJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J2olvoaj43KNoATTBeS_C2AUGSqUNzWBJSxXpVRPNtjE5upFc8-N74xsIeRZJohv7uUKrwb0rEbj-ABYUpgHhU1RdvIfPw_59Z1Q4VN5Om0qhJjnJoI9X_i0LNGgPfHbi7Vo1s8bSC7S2RD6q0HIy2-kxT9rK3ez_lp73HtLhoZaDaq9rrHDtlv060g0pRRykSjkQ-8SFQBI_nasBW-WDgdXNjFp7_TDzw1iFZ6l6YqQsSNtL0fNdZWc3PdB9llYyDHWocipBsSshYTqIaI40DIZU4oZ8bPHcPWlAUkB9ccXvdOr9_hoyEjNxMbeU3kcuQufTY-raNlbihyWaY2Qxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در بحبوحه گمانه‌زنی‌ها درباره استعفای محمدباقر ذوالقدر از دبیری شورای عالی امنیت ملی، روز یکشنبه ۱۸ مرداد ماه، پیامی منتسب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در خبرگزاری حکومتی تسنیم منتشر شد که در آن محسن رضایی به عنوان «نماینده رهبر» در «شعام» (شورای عالی امنیت ملی) معرفی شده است.
در ادامه این پیام مکتوب، بدون اشاره به استعفا، از محمدباقر ذوالقدر «تشکر» شد.
این خبر در حالی منتشر می‌شود که از دو روز پیش اخبار غیررسمی درباره استعفای محمدباقر ذوالقدر از مقام دبیری «شعام» و جانشینی محسن رضایی،‌ منتشر شده بود.
خبر انتصاب رضایی در شعام، صبح یکشنبه در خبرگزاری‌های رسمی ایران منتشر و کمی بعد در بسیاری از آنها
حذف شد
.
آخرین گزارش‌ها از فعالیت ذوالقدر به عنوان دبیر شعام، مربوط به پیامی منتشر شده در روز شنبه است که بازگشایی تنگه هرمز را به پذیرش ۶ شرط جمهوری اسلامی از سوی آمریکا منوط کرده بود. پیامی که بازتاب گسترده‌ای در رسانه‌های بین‌المللی داشت و تلاش‌ها برای بازگشایی تنگه هرمز را با ابهام‌هایی مواجه کرده بود.
@
VahidOOnLine
🔥
رجا نیوز نوشته:
در اعلام بدون تاریخ این حکم نشانه‌هایی است برای اهل اندیشه...
🔄
آپدیت:
کانال خامنه‌ای نوشته به ذوالقدر پست مشاور سیاسی  رهبر جمهوری اسلامی داده شده:
📝
انتصاب دکتر ذوالقدر به عنوان مشاور سیاسی رهبر معظم انقلاب
💬
رهبر انقلاب اسلامی در حکمی آقای دکتر ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔻
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
✏️
بسم الله الرحمن الرحیم
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر
باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید.
✍️
سیّدمجتبی خامنه‌ای
🔄
و در نهایت حکم دبیری رضایی صادر شد:
معاون ارتباطات ریاست جمهوری:
محسن رضایی دبیر شورای عالی امنیت ملی شد
🔥
اما بخش جذاب ماجرا
محمدباقر خرازی
است.
او پیشاپیش گفته بود ذوالقدر می‌رود و محسن رضایی جایش را می‌گیرد.
درست درآمدن خبری چنین مشخص، همه ادعاهای خرازی را ثابت نمی‌کند؛ اما حالا دیگر دشوارتر می‌توان گفت او از پشت پرده قدرت هیچ خبری ندارد،حتی اگر خودش مدعی باشد کلیپ‌های جنجالی‌اش را هوش مصنوعی ساخته است.
@
pourostadv
🔥
امیرحسین ثابتی (نماینده انتخاب شده برای مردم تهران در مجلس شورای اسلامی) علیه پزشکیان با عنوان «علی الاصول ۲»:
پزشکیان مقابل خواسته مجتبی (رفتن ذوالقدر و آمدن رضایی) ایستاده بود.
علی الاصول ۲؛ انتشار حکم محسن رضایی توسط رهبرانقلاب
با آشکار شدن حکم نمایندگی رهبرانقلاب برای محسن رضایی در شورای عالی امنیت ملی، یک مساله دیگر آشکار شد و آن اینکه مدتها پزشکیان به عنوان رئیس این شورا در مقابل این خواسته رهبر انقلاب (رفتن ذوالقدر و آمدن رضایی) ایستادگی می‌کرده است.
به لطف خدا، تقریبا همه چیز برای مردم آشکار شده و دیگر کسی فریب "همه امور با رهبری هماهنگ است" را نمی‌خورد و اتفاقا مردم فهمیده‌اند کسانی که تحت پروژه وفاق و با چوب وحدت، میخواهند مردم مطالبه‌گر را سرکوب کنند و مقابل دوربین همه چیز را گردن رهبری بیندازند، در عمل خلاف نظر ایشان را عمل می‌کنند.
آقای پزشکیان! حرکت در مسیر رهبری با حرف زدن نیست، دست فرمان‌تان را تغییر دهید تا مردم تغییرتان نداده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/77795" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d-X6QxsAiutKHp1eOjwoeeHeB9pQkwqPfuF3m_cYHCKCTIJMASIJ5JhgW2Boe4ak0WqNAVPE8P0vpYM_S_q0f1OnXTgM4QRjArSizC2sp0mmzphLkejKgdLkn6J5EVCNaH1-Z_QLdiPjmEFK-RnjurH_CPBzjnncSKfKA3pP05v1CBA5Q28c5DE_G2S6oj4afNY0BkWKZBoUXEBtZrIXMtFoVcuSIcKe3QyQqBHB1HsZ3H_m3vspT-u6ikkbw5hrkeNbR384x6vc83x8Kul7H54LizF9lphDkCV4Gzpjnp2G8smWlMgqVXtTxL-fQbtFoxSOo-V5ERPiqOlFPRTzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس: درباره ایران «داریم قضیه را کم‌سروصدا پیش می‌بریم»
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، روز یکشنبه نشان داد که آماده است اجازه دهد فشار اقتصادی بر ایران افزایش یابد — به‌جای آنکه دستور یک حمله نظامی تازه را صادر کند — حتی در حالی که این کشور همچنان در برابر آمریکا سرپیچی می‌کند.
چرا مهم است:
تنها یک هفته پیش، ترامپ در آستانه صدور دستور بازگشت به عملیات رزمی گسترده بود. اما او در گفت‌وگو با اکسیوس هیچ تهدید نظامی تازه‌ای مطرح نکرد.
▪️
ترامپ همچنین از اینکه ایران اعلام توافق با عمان برای بازگشایی تنگه هرمز را به تأخیر انداخته است، هیچ خشم یا نارضایتی‌ای ابراز نکرد. ایران روز شنبه فهرست تازه‌ای از خواسته‌ها را برای اجازه عبور کشتی‌ها از تنگه مطرح کرد.
ترامپ چه می‌گوید:
ترامپ در یک تماس تلفنی کوتاه گفت: «داریم قضیه را کم‌سروصدا پیش می‌بریم.»
▪️
«ما فقط یک‌جورهایی، نیم‌بند با آنها مذاکره می‌کنیم. فقط داریم ایران را تماشا می‌کنیم، با آن تورم عظیمش و این واقعیت که هیچ پولی ندارد.»
▪️
او تأکید کرد که ایران از نظر اقتصادی «در وضعیت بسیار بدی» قرار دارد و پولی برای پرداخت به نیروهایش ندارد. ترامپ گفت محاصره دریایی آمریکا بحران اقتصادی حکومت ایران را تشدید کرده است.
▪️
در عین حال، ترامپ گفت با کاهش قیمت نفت به اندکی بیش از ۷۵ دلار در هر بشکه، مصرف‌کنندگان آمریکایی فشار کمتری از جنگ احساس می‌کنند.
▪️
ترامپ درباره کش‌وقوس با ایران گفت: «درست می‌شود. همیشه درست می‌شود. مثل یک بازی شطرنج است.»
اصل خبر:
توافقی برای تنظیم تردد در تنگه هرمز میان ایران، عمان و آمریکا مذاکره شده و چند روز است که در انتظار نهایی‌شدن قرار دارد.
▪️
بر اساس توافق جدید، ایران کنترل بخشی از تردد در تنگه را به دست می‌آورد — چیزی که پیش از جنگ در اختیار نداشت.
▪️
میانجی‌های قطری و پاکستانی مطمئن بودند که توافق روز چهارشنبه اعلام خواهد شد، اما از آن زمان چشم‌انداز آن رو به افول گذاشته است.
▪️
مقام‌های آمریکایی همچنین می‌گویند اختلافات درون حکومت ایران رو به افزایش است. یک جناح به رهبری مسعود پزشکیان، رئیس‌جمهور، به‌شدت نگران فروپاشی اقتصادی است و معتقد است ایران باید با آمریکا به توافق برسد. جناح دیگری به رهبری احمد وحیدی، فرمانده سپاه پاسداران انقلاب اسلامی، هرگونه امتیازدهی را رد می‌کند.
وضعیت فعلی:
محمدباقر ذوالقدر، رئیس شورای عالی امنیت ملی ایران، روز شنبه شروط تازه‌ای را برای بازگشایی تنگه مطرح کرد — افزون بر شروطی که در توافق عمان درباره آنها مذاکره شده بود.
ذوالقدر در بیانیه‌ای گفت
برای بازگشایی تنگه، آمریکا باید:
▪️
«هرگز با هیچ زبانی ایران را تهدید یا به آن توهین نکند.»
▪️
«جنگ علیه ایران و متحدان ایران در لبنان، غزه، یمن و عراق را برای همیشه پایان دهد.»
▪️
محاصره دریایی را لغو کند و نیروهای نظامی را از اطراف ایران خارج کند.
▪️
او همچنین خواستار پرداخت کامل غرامت خسارات جنگ، لغو همه تحریم‌ها و آزادسازی تمام دارایی‌های مسدودشده ایران شد.
▪️
تا چند هفته پیش، این خواسته‌ها پیش‌شرط دستیابی به یک توافق هسته‌ای بودند. اکنون ایران آنها را صرفاً به‌عنوان شروط بازگشایی تنگه مطرح می‌کند.
▪️
یک دیپلمات از یکی از کشورهای میانجی گفت بیانیه ذوالقدر بازتاب‌دهنده کشمکش سیاسی درون حکومت است.
پشت پرده:
مقام‌های آمریکایی گفتند ترامپ یک هفته پیش متمایل به ازسرگیری عملیات رزمی گسترده علیه ایران بود، اما متقاعد شد که فعلاً تنش را کاهش دهد.
▪️
یکی از این مقام‌ها گفت ادامه درگیری به حکومت ایران اجازه می‌داد از مواجهه با پیامدهای جنگ، خسارت‌های واردشده به زیرساخت‌ها و بحران عمیق اقتصادی ایجادشده اجتناب کند.
▪️
این مقام آمریکایی گفت وقتی ایران درگیر جنگ نیست، ناچار می‌شود با واقعیتی تلخ روبه‌رو شود که هیچ راه‌حل واقعی برای آن در دسترس ندارد.
▪️
در عین حال، این مقام آمریکایی گفت هر شب حدود ۸ میلیون بشکه نفت با هماهنگی ارتش آمریکا از مسیر جنوبی تنگه هرمز از خلیج فارس خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
موضوعی که باید زیر نظر داشت:
جی‌دی ونس، معاون رئیس‌جمهور، روز شنبه به فاکس‌نیوز گفت: «این ماجرا تمام نشده است. واضح است که دیگر در ابتدای آن هم نیستیم. ما وسط بازی هستیم و مجموعه کاملی از ابزارها — ابزارهای دیپلماتیک، اقتصادی و نظامی — را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77794" target="_blank">📅 20:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77793">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77793" target="_blank">📅 19:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8_RaDuU2z-GvZQ4P7PjcvWcjj3HlIUzsyvra-asAn9noe90va_E4I2vduAvc5zIyKbWakeTWzYRAKzrWCMQ6-e4eTvHpvUKR9ciSC7B6Mv0xjcxlnYj-200cgy3J59f12dkowEq_AV4HUqescmxuuvJ8ohpYeQ01dBRP77QzTjXhQ3RsHBwDOJjBmuQZ4WoR_-9ipyIjHo8Dq3J6aWigCkhkw4FwCQ_vVv5Kzs4wvEhnsPoopqePNsjXOjNbi_K3QAndmStsJuZj9FIRRMdB_AFIo6WC8PzZ3LdGtHqH4oiCyTGFOS7CHRxJkPbACDeYSnoSWU1xUb7ncksFEE8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه اطلاع‌رسانی دفتر رهبر جمهوری اسلامی روز یک‌شنبه ۱۸ مرداد ۱۴۰۵ اعلام کرد پزشکیان هم‌زمان با آغاز سومین سال ریاست‌جمهوری خود با مجتبی خامنه‌ای «دیدار و گفت‌وگو» کرده است. خبرگزاری مهر و ایرنا و دیگر رسانه‌های حکومتی نیز این خبر را بازنشر کردند.
بااین‌حال، از این دیدار نیز هیچ عکس، فایل صوتی یا ویدیویی منتشر نشده است.
پزشکیان پیش‌تر نیز گفته بود پس از انتخاب خامنه‌ای به رهبری، با او دیدار کرده است؛ اما از آن ملاقات نیز سند صوتی یا تصویری منتشر نشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77792" target="_blank">📅 18:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77791">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vJpm0YkN_0Ls4rcidyqrmKwp9Z9VGOaDp4OAg2RjrFS43AmRWI8vCE324PfNmvyqx1qidtp2Wtbhi4twzvkXa0q2O4uS3w4Nagl2nD1hAKnGfUNo5snCfDEilVpwp6BBNjH5n6yuwCVFShqNKWZZEZyt7Mh6N5XWTJx8RDyCn_1RY_XUXTSMB-KYaBBb0efSsuqLABbEOP62xqUxRZFXeGgdlLastO3JdGchphR4xhyGRvptER-GAJrpkrpShng7JNhbxw4IuzN3F6KltGompfKJu5MmGAFa1e3eYLOBbdnkM1sGXHCOmvc9U4WHM4LYwvJXGKLT8-hjyRwY5Zm8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماری از رسانه‌های حکومتی یکشنبه ۱۸ مرداد از انتصاب محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، رهبر جمهوری اسلامی، به‌عنوان نماینده او در شورای عالی امنیت ملی خبر دادند، اما دقایقی بعد این خبر را حذف کردند.
خبرگزاری تسنیم، وابسته به سپاه پاسداران، به نقل از «شنیده‌ها» نوشت که با این انتصاب، محسن رضایی و سعید جلیلی دو نماینده مجتبی خامنه‌ای در شورای عالی امنیت ملی خواهند بود. تسنیم پس از چند دقیقه این مطلب را از کانال تلگرامی خود حذف کرد.
رسانه‌های مهر، ایسنا و جماران نیز خبر انتصاب رضایی را منتشر کردند و اندکی بعد مطالب خود را برداشتند.
انتشار و حذف این خبر در شرایطی صورت گرفت که در روزهای اخیر اختلاف‌ها در ساختار جمهوری اسلامی بر سر روند گفت‌وگوها با آمریکا، از جمله پرونده هسته‌ای و چشم‌انداز تنگه هرمز، افزایش یافته است.
@
VahidOOnLine
🔄
آپدیت: خبر شش ساعت بعد از حذف دوباره
منتشر شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77791" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=r7bWIJpOPIix_R3MBTiQE-DtI7zYE0NvodvcF9e0AbagqQTbT1Vhcu_LqbAiYz9IHqkd9I4ceMqeeItU6x1v79j_IEds6yWlPgjuArHqByKXY5wKzufurY0JEBAW62XHySs1_LYZjg4C6xdazt4UOU1NQbJsIkGUM2tYVO-Sb7dYD8WIP0_Y0riK3TAXH79ivrrmOugZAGha1QhKC4wFNYJJcyYjOs1UYPW0Z5D5LUJKQumOMp4Ez0UmtV1iSu9eFMBUmLlGzH4LeCjZUjj_u8q5clpfEV7MokQGelV3oz55NRKmSWcIZ3CNdmLrrwLnFaGS0mQJTHtDlHas_nU-Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=r7bWIJpOPIix_R3MBTiQE-DtI7zYE0NvodvcF9e0AbagqQTbT1Vhcu_LqbAiYz9IHqkd9I4ceMqeeItU6x1v79j_IEds6yWlPgjuArHqByKXY5wKzufurY0JEBAW62XHySs1_LYZjg4C6xdazt4UOU1NQbJsIkGUM2tYVO-Sb7dYD8WIP0_Y0riK3TAXH79ivrrmOugZAGha1QhKC4wFNYJJcyYjOs1UYPW0Z5D5LUJKQumOMp4Ez0UmtV1iSu9eFMBUmLlGzH4LeCjZUjj_u8q5clpfEV7MokQGelV3oz55NRKmSWcIZ3CNdmLrrwLnFaGS0mQJTHtDlHas_nU-Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در نشست روز یکشنبه کابینه، با رد صریح طرح ۱۵ ماده‌ای «شورای صلح» دونالد ترامپ برای غزه گفت: «اسرائیل طرح ۱۵ ماده‌ای را رد می‌کند. ارتش اسرائیل تا زمانی که حماس به‌طور کامل خلع سلاح نشود، هیچ‌گونه عقب‌نشینی انجام نخواهد داد.»
او با تاکید بر لزوم خلع سلاح واقعی حماس افزود: «منظور از خلع سلاح، شامل تمام تسلیحات سنگین، نیمه‌سنگین و سبک است؛ ما از یک خلع سلاح واقعی و نه فرضی صحبت می‌کنیم.»
نتانیاهو همچنین با اشاره به رایزنی‌ها با طرف آمریکایی خاطرنشان کرد: «ما در حال گفتگو با آمریکایی‌ها هستیم. آن‌ها ایده‌هایی دارند که برخی از آن‌ها برای ما قابل قبول و برخی غیرقابل قبول است. امنیت اسرائیل قابل مذاکره نیست و ما قاطعانه بر سر منافع خود ایستاده‌ایم.»
نخست‌وزیر اسرائیل در پایان تاکید کرد: «تا زمانی که من نخست‌وزیر هستم، هیچ کشور فلسطینی تشکیل نخواهد شد؛ نه در غزه و نه در کرانه باختری.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77790" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4MHr4fjYaGlXhFGZfDojOw7QhtIfJSc6o7DPv6N4mahOqCd1s48FWYqTSIvr0nhaTekE3KBdl0y1klVl-bq779Ixc33P_oneaFs7axoZyucrBwLomgGrxTzS5l0XRlNdTF03b9aaLEIejBA6f7M6FqQH55Yrj-d1puwywuQXsaJHSTL7HvFBTMxayDzFntWtswLYKEfmlFJ4gMNNbMx3vB0pOR5urvqLuGnrrUqnpXEUdjWyTTRuXzrAJggG61wlPeeKjpWT-1d7fjmJ71ytBmpflWEtzQ0pIEB421Yah8-qjsFGW3_r4gu_weFePdCRV_IoU_bNQ18IWfKcTr3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان امروز منابع حکومتی درباره قتل مداحی که ۶ ماه به بهانه "دعوت به حجاب" مزاحم یک "دختر بلاگر" شده بود تا رفت سر قرار باهاش:
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شده بود اما ۴ روز پیش ویدیویی از پیکر آسیب دیدهٔ این فرد در یک کانال ضدانقلاب منتشر و در فضای مجازی دست به دست شد.
مرد گمشده مدتی قبل در فضای مجازی با خانم بلاگر جوانی آشنا شده و به او امر به معروف و نهی از منکر می‌کرده و می خواست حجابش را در پیج اینستاگرامی حفظ کند و به مسائل سیاسی نپردازد که در روز ناپدید شدن نیز این خانم بلاگر از او درخواست ملاقات حضوری داشته است.
تحقیقات کارآگاهان نشان می‌دهد زن جوان با طراحی قبلی و با دعوت از مرد سرشناس به محله خلوتی زمینه حضور وی را فراهم کرده و پس از رسیدن مداح جوان به محل قرار با تعارف خوردنی مسموم ابتدا مقتول را بی هوش کرده سپس با همدستی 5 مرد او را به قتل رسانده اند.
خانم بلاگر در بازجویی ها گفت : من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و... من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند.
...
تحقیقات همچنین نشان داد این افراد پس از قتل، اقدام به فیلمبرداری از صحنه جنایت و جنایت بر میت کرده و فیلم تهیه‌شده را در ازای دریافت پول برای  شبکه‌ معاند منافقین ارسال کرده‌اند چون تصور می کردند برای این فیلم ها که در آن بسیجی ای کشته می شد پول خوبی می توانند دریافت کنند.
بررسی‌های کارآگاهان در این مرحله نشان داد مقتول با ضربات متعدد چاقو به قتل رسیده و پس از مرگ، با آتش زدن جسد جنایت بر میت رخ داده است. متهمان همچنین درباره نحوه انتقال و سوزاندن جسد در بیابان‌های اطراف پرند توضیحاتی را در اختیار تیم تحقیق قرار داده‌اند.
براساس ادعای افراد بازداشتی، یکی از متهمان که به عنوان عامل اصلی جنایت معرفی شده، ضربات اصلی را به مقتول وارد کرده و پس از آن سایر افراد نیز در این جنایت مشارکت داشته‌اند؛ با این حال، متهم اصلی پرونده پس از ارتکاب قتل متواری شده و تلاش‌های پلیس برای دستگیری او ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77789" target="_blank">📅 18:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TH4E0RWbrrsSS-HyRlXV6jsjtmfaZKIr43-R_2fq8J4nAkchjr2TdRX5YbbidOfZad4B7J_JEG82h8OngzDbnOkvLJCWfPx_JDPOhrjWfuPslaNRwvy1Sc-rcJdS4JFg50CDmhNKHkR6fn6lEvd0kupL1W7A_iOCgxcmGirM8LxXxSa8OioMDVKZKBNY2i5co1LSnYTpu3jIjxPCFlI0KU5Y6FLiNECJHu9Gr3G7jpXp2eebMVqxWf6_O2C0dATj-pBKVH64xDmQNlc_HqIJV9g60uf_5y9s7yDRrNe4ZSOR9hRigiMEmVxigTJSPnOEridVSg_nMDVfknGWsllVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات حکومت ایران در عین اعلام پیشرفت در مذاکرات ایران و عمان درباره تعیین مسیر کشتی‌ها در تنگه هرمز روز شنبه، ۱۷ مردادماه، شرط‌های تازه و گسترده‌ای را برای باز شدن این آبراه مطرح کردند.
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه گفت تا زمانی که آمریکا به گفتۀ او «رفتارش را تصحیح نکند، تنگه هرمز باز نخواهد شد» و تأکید کرد این شورا «چه در جنگ و چه در مذاکره» از این موضع کوتاه نخواهد آمد.
او شش شرط را برای بازگشایی تنگه مطرح کرد که از جمله شامل پایان جنگ و حملات آمریکا به ایران و متحدان جمهوری اسلامی در لبنان، فلسطین، یمن و عراق، رفع محاصره دریایی، خروج نیروهای نظامی آمریکا از پیرامون ایران، پرداخت کامل خسارت‌های جنگ، لغو تحریم‌ها و آزادسازی دارایی‌های مسدودشده ایران است. ذوالقدر همچنین خواستار پایان تهدیدهای آمریکا علیه ایران شد.
ساعاتی پیش از آن نیز سخنگوی سپاه پاسداران اعلام کرده بود که بازگشایی تنگه هرمز اساساً «ارتباطی به مذاکرات ایران و عمان ندارد» و تنها در صورتی انجام خواهد شد که آمریکا «شرایط ایران» را به‌طور کامل بپذیرد.
@
VahidHeadline
شرایط شورای امنیت ملی ایران با یادداشت تفاهم با آمریکا چه تفاوتی دارد؟
انتشار شش شرط ایران برای بازگشایی تنگه هرمز، چشم‌انداز بازگشایی این تنگه در کوتاه‌مدت را در ابهام بیشتری فرو برد.
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، گفت که این شورا چه در جنگ و چه در مذاکره «هرگز کوتاه نخواهد آمد.»
شورای عالی امنیت ملی ایران زبان صریح‌تری در مقایسه با تفاهمنامه با آمریکا به کار بسته است.
در یک مقایسه سریع با یادداشت تفاهم، ایران این بار به شکلی صریح خواستار پرداخت «بی‌کم و کاست خسارت‌های دو جنگ» شده است، موضوعی که در نص یادداشت تفاهم‌ دیده نمی‌شد.
پذیرش آمریکا تقریبا ناممکن است چرا که آن کشور را در موضع «متجاوز» قرار می‌دهد و به زبان سیاسی هم به «شکست» تعبیر می‌شود. در عین حال، پرداخت غرامت، تبعات حقوقی دیگری هم به‌عنوان آغازگر جنگ و همچنین اقدامات غیرقانونی بین‌المللی دارد.
این در حالی است که دونالد ترامپ گفته بود که خسارات حملات ایران را از پول‌های بلوکه شده ایران می‌گیرد. این موضع آمریکا عملا نفی ششمین شرط ایران برای آزادسازی تمامی‌ دارایی‌هایی‌هایش است.
شرط دوم ایران هم اگرچه به بند نخست یادداشت تفاهم می‌ماند، با یک تفاوت بنیادین. در تفاهمنامه دو کشور تنها از پایان دائمی تخاصم در ایران و لبنان نام برده شده بود. این بار اما جمهوری اسلامی خواستار پایان دائمی جنگ در «فلسطین، یمن و عراق» هم شده است.
به نظر می‌رسد شش شرط ایران نه موضوع مذاکره که موضع این کشور است.
پیش از این، اگرچه مقام‌های ایران اعلام کرده بودند که توافق با عمان به معنای بازگشایی تنگه هرمز نیست اما رئیس‌جمهور و مقام‌های وزارت خارجه تا حدی این موضوع را به بازگشت آمریکا به تفاهمنامه و تعهد عدم نقض آن مشروط کرده بودند.
حالا به نظر می‌رسد شورای عالی امنیت ملی مطالبات را افزایش داده است، اقدامی که حتی اگر با هدف فشار بر آمریکا و امتیازگیری در مذاکرات باشد، مخاطرات خود را دارد و مشخص نیست که واکنش آمریکا چه خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77788" target="_blank">📅 18:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrNjXESJ2DfuqNRmOBJ0vqFLXn5Mau0WEXcljjXV8r8bpc0d6Aj-wzyE9C8GiilQwW3KuFdiq5AKYUGvMD6-UotWp4lJ3ebLMrqoRmIEONdJtAkNMRD3Yluy1GYI7HrK50iEvA89L-XRyMpuTkWmXTq0G1oNz2tTyWlzdfVQhz0bm7ag_qqggSeL1O6qhVV5ym06iqySQ8YpzPv4sgaMtyrT_c0UJq8zL4GtYtNrPJAZdowdRwtXclj7Dn5R9ixGIKTR4TK5JCPAkRCy3Z16Ld2MaSxubHO-8IVzFdlYMatIj1d_qvOhSPNUoLFHqPFbjo9BnSWLxPtLFpNwoErL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام رسول رضایی، شهروند ۲۸ ساله اهل فریمان و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در دیوان عالی کشور تایید شده است. او پیش‌تر از سوی دادگاه انقلاب مشهد به اتهام «محاربه» به اعدام محکوم شده بود.
خبرگزاری هرانا، روز یکشنبه ۱۸مرداد ۱۴۰۵، گزارش داد، رسول رضایی که در حال حاضر در زندان وکیل‌آباد مشهد محبوس است، پس از تایید حکم اعدام در دیوان عالی کشور در معرض اجرای این حکم قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77787" target="_blank">📅 17:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=jQ6zdJoS-uHH_TqH6ChCgJopWs3D6yC_--BUD1JFgUcMeDYSU32cchCzt4LPU78cGEdMMsfLv33KPCdt09o8uCrkWaPGK293WosIHZTMlgid2J46AyR7zIRJ185tU0ghhqyLndFoeK6HfilReN9iwrWTXtflwQldMsIZuOzL3-niKe41XxHUv0jzOcHtenrFFGrjuYMVR14w6ricXyfQZvbhzkIJGYfmZoVFNElwEIv1l6Z3TJa8-5eAN4DcVCJfBgHpBTxLSSEz7r5pFJrQtinWxP8N6IA6fmFJrG-Ey0j1c3uGTjNoEH8SfzXvU9T2JrDRHstKyaeUmnSNvMfPLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=jQ6zdJoS-uHH_TqH6ChCgJopWs3D6yC_--BUD1JFgUcMeDYSU32cchCzt4LPU78cGEdMMsfLv33KPCdt09o8uCrkWaPGK293WosIHZTMlgid2J46AyR7zIRJ185tU0ghhqyLndFoeK6HfilReN9iwrWTXtflwQldMsIZuOzL3-niKe41XxHUv0jzOcHtenrFFGrjuYMVR14w6ricXyfQZvbhzkIJGYfmZoVFNElwEIv1l6Z3TJa8-5eAN4DcVCJfBgHpBTxLSSEz7r5pFJrQtinWxP8N6IA6fmFJrG-Ey0j1c3uGTjNoEH8SfzXvU9T2JrDRHstKyaeUmnSNvMfPLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی جی‌دی ونس، معاون رییس‌جمهوری آمریکا با فاکس‌نیوز، بخش مربوط به ایران با تشخیص و ترجمه ماشین:
🔻
ونس: ... ما با ایرانی‌ها در حال گفت‌وگو هستیم.
تلاش می‌کنیم میزان نفت و گازی را که از تنگه هرمز عبور می‌کند به حداکثر برسانیم. در حال حاضر بیش از هر چیز روی همین متمرکز هستیم. فکر می‌کنم می‌بینید که قیمت نفت امروز به حدود ۸۰ دلار در هر بشکه کاهش یافته و گاهی کمی پایین‌تر هم می‌رود.
بنابراین فقط تلاش می‌کنیم مطمئن شویم آنچه را که از این درگیری نیاز داریم به دست می‌آوریم.
اگر به عقب برگردید و به یاد بیاورید که اینجا چه کرده‌ایم، برنامه هسته‌ای آن‌ها را نابود کرده‌ایم، نیروی نظامی متعارفشان را نابود کرده‌ایم و آنچه را می‌توان توانمندی‌های نظامی نامتقارنشان نامید، به‌شدت کاهش داده‌ایم.
و اکنون می‌خواهیم ببینیم آیا حاضرند آن نوع تغییرات بلندمدتی را انجام دهند که برای داشتن رابطه‌ای بهتر با ایالات متحده ضروری است یا نه. اگر هم حاضر نباشند، اشکالی ندارد.
ما همچنان هر فشاری را که بتوانیم وارد می‌کنیم و تلاش می‌کنیم تا جای ممکن نفت و گاز بیشتری از خاورمیانه به جریان بیندازیم تا آمریکایی‌ها بتوانند از قیمت پایین‌تر بنزین و انرژی بهره‌مند شوند.
این همان موازنه ظریفی است که باید برقرار کنیم.
آخرین چیزی که در این باره می‌گویم، کیلی، این است که همیشه سعی می‌کنم به مردم یادآوری کنم که واقعاً هنوز وسط بازی هستیم. این ماجرا تمام نشده است. دیگر در ابتدای کار هم نیستیم؛ وسط بازی هستیم و مجموعه‌ای کامل از ابزارها—دیپلماتیک، اقتصادی و نظامی—را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.
کاملاً مطمئنم که به آن نقطه خواهیم رسید، اما هنوز تا حدی وسط بازی هستیم.
🔺
کیلی مک‌اننی:
ایرانی‌ها هم از راه‌های مختلف این پیام را داده‌اند که می‌خواهند کنترل خود را بر تنگه هرمز محکم‌تر کنند. بنابراین در یک توافق فرضی، وضعیت قابل قبول در تنگه هرمز چه خواهد بود؟
🔻
جی‌دی ونس:
انتظار ما این است که همان میزان نفت و گازی که پیش از آغاز این درگیری از خلیج [فارس] خارج می‌شد، دوباره از آن خارج شود.
ایرانی‌ها به ما گفته‌اند که قرار است همین کار را انجام دهند. کل ائتلاف کشورهای خلیج [فارس] نیز همین را می‌خواهد.
اما می‌دانید، ما اعتماد نمی‌کنیم؛ راستی‌آزمایی می‌کنیم. به حرف مردم نگاه نمی‌کنیم، به عملشان نگاه می‌کنیم.
می‌بینید که برخی افراد در داخل ساختار ایران درباره گرفتن عوارض صحبت می‌کنند. ایرانی‌ها به ما گفته‌اند هیچ برنامه‌ای برای گرفتن عوارض از عبور و مرور در تنگه هرمز ندارند. اما باز هم خواهیم دید در عمل چه اتفاقی می‌افتد.
آنچه طی حدود یک هفته گذشته در جریان بوده این است که ایرانی‌ها و کشورهای خلیج [فارس]، به‌ویژه عمان، درباره چگونگی تضمین عبور و مرور امن گفت‌وگو کرده‌اند.
البته یک مشکل این است که ایرانی‌ها در آغاز جنگ تعداد زیادی مین کار گذاشتند. بنابراین آنچه اکنون واقعاً داریم روی آن کار می‌کنیم این است که چگونه می‌توان سازوکاری برای تردد ایجاد کرد تا کشتی‌هایی که عبور می‌کنند بتوانند با ایمنی عبور کنند.
این طبعاً شامل مین‌روبی هم می‌شود. همچنین شامل تعهد ایران می‌شود که به کشتی‌های تجاری شلیک نکند.
آن‌ها به‌شدت آسیب دیده‌اند. می‌خواهند این ماجرا تمام شود.
سؤال این است که آیا قادرند—آیا نظامشان قادر است—چیزهایی را که لازم است ارائه کند تا ما راضی باشیم و احساس کنیم آنچه را از این رویارویی نیاز داشتیم به دست آورده‌ایم.
این هنوز مشخص نشده است، اما فکر می‌کنم طی چند روز گذشته مقداری پیشرفت کرده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/77786" target="_blank">📅 18:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3_S5c_YALGLGphISnEzzNp-f7KOzqMe9l7RgsTNsZDRdpbP4s_CcG81QRFkGQxSspx2OXo97nAAoi0AQUuF-qd7ct6mliyRaPYhcs207WzacMURs_SbExNm_jSHVMSlBJyw45xQLGX382PpVZtB2blMVJ2d8rRvFtSzAGNaLO44KT6QNCil2avlc98W4BwalIngds70aW2b7BkkTnhn9MVu2kTPBTX37xazICGjZ9N4zdBTWw2td0-69FqWEx6i9XR44vdGNkbilYDCWaViQKH7Wn8DbMm3lgnDJyY4qQLCTMHwL2DfY_oolDkQ_avYxZVF4QbPYjNjL_wY5mcDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از هدف قرار گرفتن یک شناور در تنگه هرمز، در فاصله حدود ۱۸ مایل دریایی شرق خصب در عمان، خبر داد. هم‌زمان، امارات متحده عربی اعلام کرد یک نفتکش متعلق به شرکت ملی نفت ابوظبی، ادنوک، هنگام عبور از تنگه هرمز هدف حمله موشکی قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77785" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keNu6G0SulxkHyT3m-iWmKgFnlr_qMPPeayHlvPkDZsdMa5QCjNcH9DtjPzVxoff91QsiwFhPOJzN2tZpSeXXIbnTKG8a_8an9v6Sat7WPUTs2A6Vgvb_NUJ148cR-yjTT-CE9koTtskZSyMKrxYHfJFsHMYLG7qnEGwKZEpIJqudc2l1nqlFHgpfqiNXxW6Q5tVIijgVUl5Q5Qgt1jWrTHh9WiF3liw2DBUuisgz8vv6WjTqIge76LotuLFoD4woLGv29BUU3hgfmycz4z8PwaRbQhY92ZLuy2Lphw9MKg4iNKqLz-G62o_A1VWDp6VtAi_kp8nfhJU2pbduvNbSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه ۱۷ مردا ماه، با انتشار پیامی با تشریح شروط جمهوری اسلامی برای بازگشایی تنگه هرمز، تاکید کرد تا زمانی که ایالات متحده آمریکا رفتار خود را تصحیح نکند، این آبراه راهبردی مسدود خواهد ماند.
دبیر شورای عالی امنیت ملی تصحیح رفتار آمریکا را مشروط به تحقق ۶ بند اصلی دانست و اعلام کرد آمریکا باید تهاجم و جنگ علیه ایران و متحدانش در منطقه از جمله لبنان، فلسطین، یمن و عراق را متوقف کند، محاصره دریایی را برچیده و نیروهای نظامی خود را از اطراف ایران خارج کند.
او همچنین پرداخت کامل خسارات جنگ‌های تجاوزکارانه، لغو تمامی تحریم‌های غیرقانونی، آزادسازی بی‌قید و شرط دارایی‌های مسدودشده و پایان دادن به تهدیدها و توهین‌ها علیه ملت ایران را از دیگر شروط اساسی ایران برشمرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77784" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRjE7SQTgIDAoaA_BXaYCWh3hTXDF8FzQHe2_2hGG8xp1i0QH4kI9SW_cjkV6QNLfPWv2yJqqxPb5DCP_1D1BGvIOK0DXu5uoEK9PROcdMSwyiBCalO3yoP59Cr7PE5uTzmWr5BpcWDPdEnQJud2M4cWlzXfqZjBhCgJF8ksxeHw9nGoVek40v9PMfMShokSmVpktA7HYaNrZxhRdhqJwjjPWHc1EMr16gKknxPl5Zo6MeKn0Zb2gttJ4deY4x6FlHXyMA17seLlENlOTncrJLTZPIEJEZbNqHcyaiI7eGUPcvawvbRioenmjFESlE6yhWDJJbi0jdhR6J50wJFpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه سازندگی روز شنبه به نقل از یک منبع آگاه اعلام کرد که مسعود پزشکیان، رئیس‌جمهور ایران، با استعفای محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، مخالفت کرده است.
در روزهای اخیر برخی رسانه‌ها از کناره‌گیری ذوالقدر و انتصاب محسن رضایی به عنوان دبیر جدید شورای عالی امنیت ملی خبر داده بودند.
این روزنامه که ارگان رسانه‌ای حزب کارگزارن سازندگی است، در گزارش خود به نقل از منبع آگاه نوشته خبر استعفای دبیر این شورا «صحت ندارد» و پزشکیان به او گفته است که با «قوت و قدرت» به کارش ادامه دهد.
با این حال سازندگی تأیید کرده که ذوالقدر پیش‌تر استعفای خود را ارائه کرده بود «اما این استعفا با مخالفت مسعود پزشکیان روبه‌رو شد و در نتیجه او همچنان در سمت خود باقی ماند».
محمدباقر ذوالقدر در پی کشته شدن علی لاریجانی در اسفند ماه گذشته در جریان حملات آمریکا و اسرائیل، به عنوان دبیر شورای عالی امنیت ملی منصوب شده بود.
علاوه بر برخی رسانه‌ها، محمدباقر خرازی، روحانی تندرو نزدیک به بیت علی خامنه‌ای، نیز هفته گذشته در یک سخنرانی خبر استعفای ذوالقدر و جایگزین شدن محسن رضایی را اعلام کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77783" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eECY-CjKq5sx1N_MTZ-ddPCIRxLF3Hq-XDq724H-YjB4vrEk2MMvZosxLSzYwQzrPJYeLcJVtFk1sgdBos8gZ1uYaT7JgNLeq-GrssCicTZ_gxxq5gh3y7ACw4cxGd6WdWzXWc7Pwj4FZg0u6oFbAMlyAoZBg7XuWJMISbS0Fuzz3QNLrTIgsfyIunnNw3FzZZi_mkOSRRZVK2BDBxEg1_9QWpqEYUrypUYx0m6C36DgNPjaEsYIaDROe6qudronJ9AWLhSL9m3gediiEAYRRmCdjHpY-3rU13lQJR3F7nLefHVTQdqOSqrcNHdw5RJ4rcJ2vqQQhV3z03Q3nbMtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌ها در مورد حمله موشکی روز شنبه نیروهای مسلح جمهوری اسلامی به نفتکش اماراتی در خلیج فارس، وزارت خارجه امارات متحده عربی با انتشار بیانیه‌ای ضمن محکوم کردن شدید این حمله اعلام کرد، این حمله تلفات جانی نداشته است.
وزارت خارجه امارات، روز شنبه ۱۷ مرداد ماه، در بیانیه‌ای این حمله را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل متحد دانست؛ قطعنامه‌ای که بر آزادی کشتیرانی و مخالفت با هدف قرار دادن کشتی‌های تجاری یا ایجاد اختلال در مسیرهای دریایی بین‌المللی تاکید دارد.
وزارت خارجه امارات همچنین اعلام کرد هدف قرار دادن کشتیرانی تجاری و استفاده از تنگه هرمز به‌عنوان ابزاری برای فشار یا باج‌گیری اقتصادی، «اقدامات دزدی دریایی» از سوی سپاه پاسداران محسوب می‌شود و تهدیدی مستقیم برای ثبات منطقه، مردم آن و امنیت انرژی جهان است.
امارات از مقامات تهران خواست این حملات را متوقف کند و به‌طور کامل به توقف تمامی اقدامات خصمانه پایبند باشد. ابوظبی همچنین خواستار بازگشایی کامل و بدون قید و شرط تنگه هرمز برای تضمین امنیت منطقه و ثبات اقتصاد و تجارت جهانی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77782" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l5SsD2v9IVubAOBHkKYQRoeFmTP0nv_kVhoTQ8e8XZx0h8ddj2KXV4idt1PuWBMxUMg5LsGA_mLth0oyemV22F_w9P7YvF56NLu4Yo8nFuFg3BHk8TS6EMGRcCRkTBB5k4ymewkBfZCX7-keJTb_Q9R3HyMhWuKFc9AZKkoKCc3qIxpaf4ruwRiMefZTCAiMthN1Q36ulpLMRdE3MKv4TAGxa-IrN53SErlELqBg6ipfvEEkCpcwUxvI29mqDICvUl4cH0SAAOI7CFEnwI_jbCXBULX3CRVzFZDNaM0S20b5MO74tbiyNhLj4ITZW-dsigTJOO6mHtj6-Hif4aEfVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JF_vOUNdWtcrc0TesWgG0JM_HWi0tkf3BAsjRIPhfRXMqdzhxcTmFP7nVpzkCb-EA0Aa_3trpNdP0ZzwVRJA88t4M0xyH5jlp7VSRzuZ-ppNZau7gPDeTfJtWMv9o047Ajl5F7Px9I3BGiLw_rkLVlrEOO-gyBs-o1m8IyhCFywEWKTVnFr4z_03lPG9dIo2rR5SGN6cU4Q2Haet4pAGvodWl4J-qKz-HIhRAGNcv-ysAuYsIOAPWD1VuZGQAt70SHBQLwC5QXN_IzLx5zsLcuxcNlRKhTO1OU5KwfXPrGm21FPlzhwz2ceC-SV1nD5k5ZJgDY4eOQv4mKhgcmFPeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNz7Qr5L4RX83NmyIkWCq5Yc3BAgNVs4AE6QxUwU6mbWuSuKNQZltqsTu5dtXLkS7GiKQKrNC5Hw6lhmGj5ixYCRWJSKUsbtrUFwVd9chWElVNoy-N8YTREfzZ8KC85jLo6s7N1PDVLNlvixQgzyVpaL-tjKPmQljpPnFFTmCBI1hH7VAWezYKhoJUMaR_74xo7p9w2lvwwEoP2vFb7pYvLbLKexv-_EnVLoqHIyyl151h1cr423HB__VEnVm-wpEsk-nQ_lOB0AwB5Cy9u09A9GABApyPNYNMoxsBi8Jeg1RS0yi9G3B6qB3YO8Hi-QR-VGN24wl1iioxnlYmjtVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXyfaHlIIH9bh8xD-hhi1f4wp9H6KvAjLDpg3ay5zbfFBF-A4W5hh2Hg3pABWB6TeAikDBzQfbkCbATdWQKXEO47hp3V6ME4jVU030814tk5pcug7fgJkoI41lFs_A0k7BJRNOQtvqvWxGldGcPJ8yAT_hUYjgZIv0EcmmbuPN8bnqFYs7B-h_iJz78SFRPmCxanpadE5H6yxoNUpAEGX8GME705tPkmHSTZ7_h7RFqB_NvMs9r60eTg5vwySU-elx2YxTQ9xkp910T0TxvssqqTgvj99f99Q0Zy_NLtEP4nZEMpGTXp5ObJMbGeT89sa7Y4BdrDV7iqeelhqtqemw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhKejch-_YJb0zB4JEZ1u9s5hj43pvu8lyesaD5PH94B-FTaidJ2MvEIJ1ErZyYibG2w7cekz1pbuImMAKQS_UNctZKT87mHhBWCaZadojXlV_P_8hIngJlvqFe5v07VdHmu9CY01WWvqjtdBd9HNAiQk8puoY9dJJObIhzSj2o4qsLFn8PbQG--ApvGk5ODSYz4bOyOj0if3zhU27CE-9AVDUbDYmA8Ici9BaF_OmVysN1Nu9Z8YZ7SE_cskZt1xde1QX4SOPYTJyXFXzYZP6l-P-inR4C8alFq7etplKqeSr--3Cr-P6sV5kD82fvUn5j4gfy93LiT3ALzvlMLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eznVLatlqVzrToH-lF5WxH5cI26u4SbUWtST37gBW5pk28wqoq0aJHHb_TRJM6byziaHFcMTSPkauYc7DaN3gaFGCw_8OwOlAZ-MLMNFOQxTL-QzMXrGjn_V4pbCorIUBYG_Rg0hZVzk6qml3eEbUn5Zuu4IapybVW2zIErDc-0yyUVediu4ErweFalyT7YDZsBb0YhxgZMLRcD88lh30TpVlIuOUxzFM0mAxZKLd7zgQTyZkDwRSB06Pmey2QYj9XmhNpkCSc7lrdaipvpZhjs5_mqaw8fIw7GezcNqifhTFyQJzbp1hzIK29v6G6Y653dnaAVM_WsiRsLVEsWwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsN74cNeNIzxSG3V_QBDO9MW5L69M-aJwpw9HL7J_5lySRH8jHGMK2_TijQ4HTmStI9NMai_jDpBfg22MB8dtq730NJUogqaZ6BHBuwZa_crV3H5zLpn9Wb-GDpFAUXtBzM_8vhClPV95i67aYT-3SzSjBSKQe5nq2-_FRRsgpiD38oFPKwH1CtSr45LAeMi6Pi-YyDvuQq8_xIDx35vvzVKJ_8cPc4gew2coYD2oCbZMfohIoG04P1yqEWewFZM6a7stWEPHe7NFDBc-TVTChoP_o4iDOAUYAgteBobo0BFrnba-2ckkzuTLk1e8XDDmbgLRQeAkmYmtca3Z8kWCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی
قوه قضاییه روز شنبه اعلام کرد محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در پی اظهارات اخیرش به دادگاه ویژه روحانیت احضار شده و تحت تعقیب کیفری قرار گرفته است.
به گفته سخنگوی قوه قضاییه، با توجه به روحانی‌بودن محمدباقر خرازی، رسیدگی به اتهامات احتمالی او در صلاحیت دادگاه ویژه روحانیت است. او همچنین گفت خرازی «می‌تواند اتهامات متعدد امنیتی» داشته باشد و در صورت حاضر نشدن در دادگاه، برای او حکم جلب صادر خواهد شد.
@
VahidHeadline
در حاشیه ساختار قدرت در جمهوری اسلامی، همواره ردی از «خودی‌های دردسرسازی» پیدا می‌شود که مقام و جایگاه رسمی ندارند، اما آن‌قدر به حلقه‌های قدرت نزدیک‌اند که نمی‌توان حرف‌هایشان را نادیده گرفت.
نسبت خانوادگی، لباس روحانیت یا وابستگی به یک تشکل حتی کم‌نام‌ونشان، به آن‌ها امکان می‌دهد از تصمیم‌های پشت پرده خبر بدهند، مقام‌های حکومتی را متهم یا تهدید کنند و سخنانی بگویند که واکنش و تکذیب بالاترین سطوح قدرت را برانگیزد، اما خود در حاشیه امن قدرت باقی بمانند و پس از مدتی با ادعایی تازه برگردند.
محمدباقر خرازی بسیاری از این ویژگی‌ها را دارد.
روحانی بدون منصب حکومتی، دبیرکل تشکلی به نام «حزب‌الله ایران» که وزن و جایگاه واقعی آن در فضای سیاست ایران چندان روشن نیست، و عضوی از خانواده‌ای که با حوزه علمیه، دستگاه دیپلماسی و خاندان خامنه‌ای پیوند دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77775" target="_blank">📅 18:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSo-EqmdfiaoZ-QAYCuLhxCLd_0iRCITwsSxDjjdSBeiwBIg13U5OlzWydaWLpSwns-Qapr4cmag15Tmd0k68DuwpMWUoHZUxuHp3fcmpVAzQ_5GhvJdR0NMoP_a2MK0x31otfBfUceFBoR1sVN9bHDd26XuMeQBsDxTcucbKVffsBVPK4S2mcnwfmb2Ab7x9KjzuC--3dMuOb4WyGTy7Q1cz20olfWgGZwbALCTwh58YVwNXC8eXjjxPfdn0O947znA05vxaHvVNa6W8vfMVZd2EhJuykkgSYmO8a_7C3P0fvfM_K49ca_scoZ0LZvXmWM1C-BTUGIUyAOqMBTPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم روز شنبه ۱۷ مرداد از ربایش و قتل حمیدرضا رجب‌زاده، از مداحان حکومتی، خبر داد.
تسنیم به نقل از یک «منبع آگاه» گزارش داده است که رجب‌زاده چند روز پیش ناپدید شده بود و پس از آن، ویدیویی از لحظه قتل او برای خانواده‌اش ارسال شده است.
بر اساس این گزارش، پس از اطلاع از این حادثه، تحقیقات پلیسی و قضایی برای شناسایی و بازداشت عامل یا عاملان قتل آغاز شده است.
با این حال، تاکنون اطلاعات رسمی و دقیقی درباره نحوه ربایش رجب‌زاده، محل وقوع قتل، انگیزه عاملان، هویت افراد دخیل در این حادثه و جزئیات ویدیویی که برای خانواده او ارسال شده، منتشر نشده است.
@
VahidOOnLine
🔄
ادعای دقایق پیش تسنیم:
🔹
پس از ارائه اطلاعات جزئی از سوی خانواده وی درباره آخرین برنامه رجب‌زاده و مسیری که قرار بود طی کند، پیگیری‌های تجسسی صورت گرفت و نهایتا، خودرویی که رجب‌زاده برای آخرین بار سوار شده بود، شناسایی و مالک آن دستگیر شد.
🔹
این فرد که در ابتدا منکر هرگونه ارتباط با این ماجرا بود، نهایتا اعتراف کرد که با تحریک شبکه‌ای تروریستی در خارج از کشور، به همراه 4نفر دیگر اقدام به ربودن حمیدرضا رجب‌زاده کرده است. آنها در ادامه اقدام به شکنجه و قتل او کرده و تصاویری را هم برای خانواده او ارسال کرده‌اند.
🔹
به گفته این متهم، آن‌ها با وعده دریافت چند هزار دلار، اقدام به ربودن و قتل رجب‌زاده کرده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77774" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پست زلنسکی، ترجمه ماشین:
ما از سنای ایالات متحده و از همه کسانی که از اوکراین حمایت می‌کنند بسیار سپاسگزاریم. تصویب قانون تحریم روسیه و ایران، طرح لیندسی گراهام، قطعاً به افزایش فشار بر متجاوز کمک می‌کند تا این جنگ جنون‌آمیز روسیه علیه استقلال ما و مردم ما پایان یابد.
اوکراین قدردان
تمام
حمایتی است که ایالات متحده از اوکراین به عمل می‌آورد — از سوی هر دو حزب و تمامی مردم آمریکا. و اکنون، زمانی که پوتین آخرین امید خود را به موشک‌های بالستیک بسته تا جنگ را طولانی‌تر کند، و زمانی که ما برای یافتن موشک‌های پاتریوت به‌منظور دفاع از خود، با تمام توان وجب‌به‌وجب همه‌جا را می‌گردیم، هر نشانه‌ای در حمایت از حفاظت از جان انسان‌ها و پایان دادن هرچه سریع‌تر به جنگ، اهمیتی فوق‌العاده دارد.
فشار واقعی و قدرتمند آمریکا و تحریم‌ها علیه روسیه بیش از هر چیز دیگری کمک خواهد کرد. با هر گامی که برای افزایش فشار بر متجاوز برداشته می‌شود، دیپلماسی نزدیک‌تر می‌شود.
از همه کسانی که این را درک می‌کنند و از طریق
قدرت، صلح
را پیش می‌برند، سپاسگزارم.
ZelenskyyUa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 470K · <a href="https://t.me/VahidOnline/77773" target="_blank">📅 23:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
نیروهای مسلح قدرتمند ایران آمادگی، توانایی و اقتدار خود را در برابر گران‌قیمت‌ترین ارتش جهان به نمایش گذاشته‌اند.
وقتی مسلمانان در کنار یکدیگر بایستند، می‌توانیم با هر چالشی که از سوی بیگانگان بدخواه ایجاد می‌شود، رودررو مقابله کنیم.
وقت آن است که فقط به خودمان تکیه کنیم و برادری واقعی را در آغوش بگیریم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/77772" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرنگار اکسیوس:
یک دیپلمات از یکی از کشورهای میانجی به من گفت که تیم مذاکره‌کننده ایرانی در انتظار تأییدهای نهایی شورای عالی امنیت ملی ایران درباره توافق با عمان و ایالات متحده است. این دیپلمات گفت: «انتظار داریم این تأیید به‌زودی صادر شود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/77771" target="_blank">📅 21:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cJ2iFWSYXACkxOmpVMIQ_ywqlvsFInlH2Kca0F9FKJh8KoXLS22iOM47KM4RwwpW2d3IRwpODAG2yCXaazUaDl4XLuxJSsXYA8uKmfTGpj3hRClzwhLGQsNR4dv1RrclwhmcfiwjPimkqSOQ1KICUpXKddOxO-4RLYgPpUibUGUC-OasD-F_nbDOHKf7lTK-NoRuwlRrEUtEwtBQlMnJk2n4_JcajLJ7eWysKdzHMPpwVrbSRbhQUHx5hO90PgKvHxNzVHVfOAKMSZmyA_VcaDLKJC6NIRC2Ts-uEVEnf_Fa5tj3gON2IzyCFFj-bBdr-mgQPR_z8AutH8HskhbLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده آمریکا در گزارشی که روز جمعه ۱۶مرداد۱۴۰۵ منتشر شد اعلام کرد که «شبکه‌ای از صرافی‌ها و شرکت‌های پوششی مرتبط با جمهوری اسلامی» را هدف قرار داده است.
در بیانیه منتشر شده از سوی این وزارتخانه تاکید شده است که ایالات متحده در حال اخذ تصمیمات قاطع با هدف «قطع شریان‌های مالی» است که حاکمیت جمهوری اسلامی ایران را سر پا نگه می‌دارند.
این وزارتخانه در بیانیه خود نوشته است که این اقدامات با هدف برچیدن شبکه‌ای از صرافی‌ها و شرکت‌های صوری انجام خواهد شد که به ایران کمک می‌کردند صدها میلیون دلار را به‌طور مخفیانه از طریق نظام مالی بین‌المللی جابه‌جا کند.
در بخشی از بیانیه وزارت خارجه ایالات متحده آمده است که «تهران از طریق این شبکه‌ها به درآمدهای نفتی دسترسی پیدا می‌کرد، تحریم‌هایی را که با هدف مهار فعالیت‌های بی‌ثبات‌کننده‌اش وضع شده‌اند دور می‌زد و با استفاده از شرکت‌های پوششی، منابع مالی خود را پول‌شویی می‌کرد.»
هدف قرار دادن بانک‌ها، صرافی‌ها و افرادی که این شبکه غیرقانونی را اداره و تسهیل می‌کنند از سوی آمریکا چنانچه در بیانیه منتشر شده آمده راهی روشن برای اعلام آن است که «هر کس به ایران برای دور زدن تحریم‌ها کمک کند، با پیامدهای جدی روبه‌رو خواهد شد.»
وزارت خارجه آمریکا اقدامات انجام شده از سوی وزارت خزانه‌داری این کشور را نشانی بر تداوم سیاست «فشار حداکثری» دولت «دونالد ترامپ» علیه ایران دانست. سیاستی که بر «قطع منابع مالی مورد استفاده حکومت برای تهدید ثبات منطقه، حمایت از تروریسم و تقویت توانمندی‌های نظامی‌اش» تاکید می‌کند.
@
VahidHeadline
پیش‌تر:
وزیر خرانه‌داری آمریکا روز جمعه گفت که ممکن است «امروز یا فردا» توافقی با ایران برای آتش‌بس و باز شدن تنگه هرمز منعقد شود.
اسکات بسنت در گفت‌وگو با شبکه «۱۲ نیوز» با اشاره به وضعیت وخیم اقتصادی در ایران گفت: «فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد توافقی برای برقراری یک آتش‌بس ۳۰ تا ۶۰ روزه خواهیم بود و تنگه [هرمز] باز خواهد شد. قیمت انرژی هم باید کاهش پیدا کند.»
او با تأکید بر این که ایالات متحده هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست یابد، گفت تحت تاثیر عملیات نظامی آمریکا و اعمال تحریم‌های شدید علیه تهران، «آنها با تورم ۱۵۰ تا ۱۸۰ درصدی مواد غذایی مواجه‌اند و دیگر توان پرداخت حقوق نیروهای نظامی‌شان را ندارند».
بسنت همچنین درباره وضعیت زیرساخت‌های نظامی ایران گفت: «نیروی هوایی نابود شد، نیروی دریایی نابود شد و بخش بزرگی از موشک‌ها و مهم‌تر از آن، توان تولید موشک آنها از بین رفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/77770" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#توافق_مکه
:
وزارت خارجه پاکستان در بیانیه‌ای اعلام کرد جمعه ۱۶ مرداد، پاکستان، ترکیه و عربستان سعودی، توافقنامه مشترک دفاعی امضا کردند.
توافق امضا شده تصریح می‌کند هرگونه حمله مسلحانه علیه هر یک از سه کشور، حمله علیه همه آنها تلقی خواهد شد.
در این بیانیه آمده است این امضای این توافق‌نامه «نشان‌دهنده تعهد سه کشور برای تقویت بیشتر امنیت جمعی آنها است.»
وزارت خارجه پاکستان همچنین در این بیانیه نوشت این توافق با هدف تقویت صلح، امنیت و ثبات در منطقه و فراتر از آن و برای دستیابی به آینده‌ای امن و با رفاه بیشتر تنظیم شده است.
همچنین رویترز به نقل از یک مقام ترکیه اعلام کرد «توافق دفاعی میان پاکستان، ترکیه و عربستان سعودی ماهیتی کاملا دفاعی دارد و هدف آن، ایجاد تعهد برای حمایت متقابل در زمینه دفاعی است.
این مقام به رویترز گفت: «این توافق علیه هیچ کشور یا طرف مشخصی تنظیم نشده و کشورهای دیگر منطقه نیز امکان پیوستن به آن را دارند.»
به گفته این مقام، این پیمان جایگزین یا لغوکننده هیچ‌یک از توافق‌های دوجانبه یا چندجانبه موجود میان کشورها نیست.
@
VahidOOnLine
ابراهیم رضایی، عضو كميسيون امنيت ملی و سياست خارجی مجلس شورای اسلامی، عربستان سعودی را به طور غیرمستقیم تهدید کرد که پیمان دفاعی مکه برای آنها امنیت به همراه نخواهد آورد.
رضایی در شبکه ایکس نوشت: «سعودی‌ها باید بدانند که توافق کاغذی با ترکیه و پاکستان برای آنها امنیت‌آور نیست، همان‌طور که سال‌ها شیردهی یکطرفه به آمریکایی‌ها برایشان امنیت نیاورد.»
او عربستان سعودی را به «گدایی امنیت» متهم کرده و به مقامات این کشور توصیه کرده به جای آن، سیاست‌هایشان را «اصلاح» کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/77768" target="_blank">📅 18:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=rQSj6krASKBDveTWEQ3EVb8fHvSXJ1XgVxmAD5u4yEuOnPwHLiMTjfEQBJU58HpCe8oXJi2c3SZl3nhXbhyJ9Q9CYG3KrJdi9JVJ1EgppIiRxK1eXFJxfb08oj1wvdyL46eKq0zsOaF10rJDZ5NmCtSz73eMC0M99ZxSl-yA7bzv1PHat7sPuVbMGgdVOlUp5paBlCLgIj-rEFF6IMkBj8b1fWYhK7YOwADK_lgIBzuGMQBHhrxKved8lzIoHmWBwqYyLaZ3t0_428IIWp89tMzn--YBcPX08KaLqN5CHvenjDpeCEyif1Gl_JVntLJoqHtxYUWe23_F9DteNO4ySA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=rQSj6krASKBDveTWEQ3EVb8fHvSXJ1XgVxmAD5u4yEuOnPwHLiMTjfEQBJU58HpCe8oXJi2c3SZl3nhXbhyJ9Q9CYG3KrJdi9JVJ1EgppIiRxK1eXFJxfb08oj1wvdyL46eKq0zsOaF10rJDZ5NmCtSz73eMC0M99ZxSl-yA7bzv1PHat7sPuVbMGgdVOlUp5paBlCLgIj-rEFF6IMkBj8b1fWYhK7YOwADK_lgIBzuGMQBHhrxKved8lzIoHmWBwqYyLaZ3t0_428IIWp89tMzn--YBcPX08KaLqN5CHvenjDpeCEyif1Gl_JVntLJoqHtxYUWe23_F9DteNO4ySA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین:
🔺
خبرنگار:
و آقای رئیس‌جمهور، جمهوری‌خواهان اکنون بحث زیادی درباره قدرت خرید و هزینه‌های زندگی دارند. پیام شما درباره این موضوع در آستانه انتخابات میان‌دوره‌ای چیست؟
🔻
ترامپ:
سؤال خوبی است، اما پاسخ آن تا حدی ساده است. من بالاترین قیمت‌های تاریخ را به ارث بردم. بدترین تورم تاریخ کشورمان را به ارث بردم و ما کار فوق‌العاده‌ای انجام داده‌ایم.
قیمت نفت اکنون به‌سرعت در حال کاهش است. اگر به اوضاع نگاه کنید، تا ۷۵ پایین آمده است.
وقتی آن اقدام بسیار مهم را در جمهوری اسلامی ایران آغاز کردم، اقدام بسیار مهمی بود؛ چون آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. در غیر این صورت، تمام جهان منفجر می‌شد. ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. مسئله فقط ما یا خاورمیانه نبود؛ برای تمام جهان فاجعه‌بار می‌شد. چاره دیگری نداشتیم.
قیمت بنزین در بسیاری از نقاط، مانند آیووا، به کمتر از دو دلار رسیده بود؛ قیمت‌هایی که مردم سال‌ها ندیده بودند: یک دلار و ۸۵ سنت، یک دلار و ۹۵ سنت. سه‌شنبه در یکی از توقف‌هایم در آیووا، در یک محل قیمت ۱٫۹۵ دلار و در محل دیگری ۱٫۸۵ دلار برای هر گالن بود.
بر اساس هرچه می‌بینم، به‌محض پایان جنگ، خیلی زود دوباره آن روزها را خواهیم دید. فکر می‌کنم جنگ به‌زودی پایان پیدا کند. تصور نمی‌کنم آن‌ها بتوانند مدت خیلی بیشتری ادامه بدهند. بله، بفرمایید.
🔺
خبرنگار:
آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
🔻
ترامپ:
نمی‌خواهم بگویم که توافق حاصل شده است. تنگه در حال حاضر تا حدودی باز است. می‌دانید، چیزی داریم که «محاصره» نامیده می‌شود و نیروی دریایی آمریکا آن را هدایت می‌کند؛ ما آن را کنترل می‌کنیم.
اکنون کنترل آن با ماست، اما آن‌ها همیشه می‌توانند به چیزی شلیک کنند یا مینی در آب بیندازند. حتی اگر فقط یک مین آن بیرون باشد، اوضاع را به هم می‌ریزد؛ چون مردم نمی‌خواهند کشتی‌های میلیارددلاری خود را وارد منطقه کنند و تصادفاً با مین برخورد کنند.
اما فکر می‌کنم عملکردمان بسیار خوب است. خودم در مذاکرات دخیل هستم و فکر می‌کنم اوضاع خوب پیش می‌رود. ممکن است توافق حاصل شود؛ ممکن است به‌زودی باشد. بله.
🔺
خبرنگار:
آقای رئیس‌جمهور، درباره مهمات؛ شما شب گذشته نوشتید که آمریکا مقدار عظیمی مهمات دارد و وجود هرگونه کمبود را رد کردید. در عین حال، یک درخواست بودجه تکمیلی ۲۱ میلیارد دلاری برای پرکردن مجدد ذخایر وجود دارد. اگر کمبودی نیست، چرا این درخواست همچنان مطرح است؟
🔻
ترامپ:
چون همیشه به مقدار بیشتری نیاز داریم. منظورم این است که مهمات بیشتری لازم داریم.
ببینید، دولت بایدن مقدار بسیار زیادی به اوکراین داد؛ رایگان، بدون دریافت هیچ پولی. میلیاردها و صدها میلیارد دلار.
خوشبختانه من در دوره خودم ذخایر بسیار زیادی ایجاد کرده بودم. نیروهای نظامی را بازسازی کردم و مقدار زیادی تجهیزات و مهمات نیز در اختیارشان گذاشتم.
از بعضی انواع مهمات بسیار قدرتمند، ذخیره‌ای نامحدود یا تقریباً نامحدود داریم. در مورد بعضی انواع دیگر، وضعیت کمی محدودتر است و هر روز محموله‌های تازه دریافت می‌کنیم.
همان‌طور که می‌دانید، شرکت‌های دفاعی ما اکنون بیش از هر زمان دیگری در تاریخ کارخانه می‌سازند. برای موشک‌های پاتریوت، تاماهاوک و همه‌چیز کارخانه می‌سازند.
در عین حال، انواعی از مهمات داریم که ممکن است به آن اندازه دقیق نباشند یا در آن سطح ممتاز قرار نگیرند. نمونه‌های ممتاز را هم داریم و این موضوع را بسیار دقیق زیر نظر گرفته‌ایم. اما بعضی از انواع مهمات ما بسیار قدرتمند و بسیار خوب‌اند و ذخیره‌ای نامحدود از آن‌ها داریم.
بنابراین در وضعیت بسیار خوبی هستیم. بااین‌حال، همیشه مهمات بیشتری می‌خواهیم و باید مقدار بیشتری داشته باشیم. ممکن است مسائل دیگری پیش بیاید و ممکن است هم پیش نیاید. امیدوارم هیچ مسئله دیگری پیش نیاید، اما ما در وضعیت بسیار خوبی قرار داریم. واقعاً مقادیر عظیمی مهمات داریم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 487K · <a href="https://t.me/VahidOnline/77767" target="_blank">📅 01:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jWalZzVcVibnRSCWl_YqrpgpL8ggGayHOFwVQFGK7HIL73sL9s4VrDC5xP1SlsB8rJW-wHN1P0_XklPuULKBRbwf-mK6ursQuKKBpud6PuzwvBTZoUzRwU4Agi38M8u1YYrGtOAslgCiuKJ8FFjb_uib0t3HcolgYjsKFDitg2eCJtIyR7Jme7uHbKjda2Ox5vLt68O4Os4w02B4bfxpu63DfLVaxbgaZIM8hLkyCwvl75krcvAUpGrD64o97-pDj5koE0GQKQSDaBbEIzTWMjgTeKqn7mZarkHs7fvThggRwbVVnTghGcE2uw-R47kL_hj63uGJg6jP9N4pRwTGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی: سلام وحید جان  همین الان دو صدای بد انفجار شنیده شد قشم  سلام ساعت ۲۱ و ۴۳ قشم دو انفجار نزدیک شهر   سلام وحید جان الان قشم صدای دو انفجار بد اومد صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن  وحید قشم رو زدنننننننن [لطفا صداها…</div>
<div class="tg-footer">👁️ 495K · <a href="https://t.me/VahidOnline/77766" target="_blank">📅 23:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fDTVRVcVX30S8BlozWi5oSkOHJuYCEin32xAxeFoZI7DAw4K6RWo6QEdU4KsmMcl4y9J9Kpbuh__9pdQFEONSHM9aqwA3nPXxLdMJICj6V7IryTrul7DqL5yRBGFnA9lvtYWLsRzuOTiSRCdoKeKTKlkwhruC99SDXc4PZMCQzh0mN8cJpThS8FXJQFR32Kndur9qSERZp2TrNWu8xLUaa_BXZm6uB5odZaoafGaUMjShcu8zaEInBQ4YEPff0GBIL1UHhz2HYBYfFbq3r0KE6tZq3GCHmG1_oylf862H3VtFt4u029o2fqaM7JgwSuoeJPFBVMSXyVmHMCVOX0BRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
«حمله‌ای عظیم در راه است... صبر کنید، بی‌خیال؛ آنها می‌خواهند مذاکره کنند.»
این همان نمایش دیپلماسی است که مدام تکرار می‌شود.
استفاده از زورگویی، وعده‌های نقض‌شده و اخبار جعلی به‌عنوان اهرم فشار، راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتری نیاز نداریم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 480K · <a href="https://t.me/VahidOnline/77765" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
همین الان دو صدای بد انفجار شنیده شد قشم
سلام ساعت ۲۱ و ۴۳
قشم دو انفجار نزدیک شهر
سلام وحید جان الان قشم صدای دو انفجار بد اومد
صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن
وحید قشم رو زدنننننننن [لطفا صداها رو تفسیر نکنید]
۴ تا انفجاررررر
قشم هم اکننون سه انفجار
ساعت ۲۱:۴۱ قشم
دوتا انفجار یکیش خیلی قوی تر بود، اسکله بهمن بود یا کشتی‌های نزدیک اسکله
بندرعباس ۲۱:۴۳ دو سه تا صدای انفجار [که لابد همون قشم بوده.]
همین الان صدای ۴ تا انفجار اومد قشم
دوتاش خیلی شدیدو نزدیک بود
دوتاش خیلی دور بود
سلام وحید جان ساعت ۹ و ۴۲ دقیقه قشم دوبار صدای انفجار اومد ،نمی‌دونم چی بود ،خونه لرزید
ساعت ۲۱:۴۰ صدای ۲ انفجار شدید شهر قشم درب و پنجره ها لرزید
سلام وحید جان صدا سه تا انفجار تو قشم اومد دوتا شدید بود یکی انگاری دور بود
🔄
منابع حکومتی:
🔹
معاون امنیتی استانداری هرمزگان،: تاکنون هیچ‌گونه اصابت یا حادثه‌ای در جزیرۀ قشم و شهر بندرعباس گزارش نشده است.
🔹
بررسی‌های لازم توسط دستگاه‌های مسئول برای شناسایی منشأ صدای شنیده‌شده درحال انجام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/77764" target="_blank">📅 21:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bXE78L_K1iizyfdjncwFxiRUZr0Y81JnUOmR7t_O1V9d97hWKHFCI8zGL2WXNylK9hcOuZjCC5F8eRdJXWfICp_Aq5aOSzlK7jO-zOviyFLH3vHfkeRi7qqz5FORQDO0wnHSUO-qJFFsDpJXikkBwyYEl_Op_zppGKIAVOLiL21NlLtkEDkDeq_pObEh4aNAefa0L1HyYGe_kEiSeqmX6h-wjQVF0UbX_X8tfcSM209AhY2REGZQVx9o6laadjTOrYJkJ8DyxKwA0ooV0VKhALb_HLl8Ja_6ZUc9HCR_zDyjeFWeQ77OGYpvcQtnFAYQJWSASZAPonfJdXqVwjxZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اخبار جعلی، طبق معمول، در حال انتشار شایعاتی دروغین و کاملاً بی‌اساس است. من از عملکرد پیت هگست به‌شدت راضی هستم. همه‌چیز فوق‌العاده بوده است؛ از جمله حمله ما به ونزوئلا که نتیجه آن در کمتر از یک روز حاصل شد و به ما امکان داد نیکلاس مادورو، یکی از بدترین جنایتکاران در سراسر جهان، را به دست عدالت بسپاریم!
همین‌طور اوضاع ایران، که برای هرگز اجازه ندادن به آن برای دستیابی به سلاح هسته‌ای به‌شدت درهم کوبیده شده، بسیار خوب پیش می‌رود! پیت در میان نیروهای نظامی از احترام بسیار بالایی برخوردار است و اصلاحات عظیمی انجام داده؛ از جمله برچیدن سیاست‌های تنوع، برابری و شمول (DEI) و افزایش جذب نیرو به سطوحی تاریخی.
این شایعه را «واشنگتن کام‌پوست» ــ یکی از بدترین رسانه‌های این حرفه ــ به راه انداخت، آن هم با وجود اینکه به آن‌ها گفته بودیم گزارششان کاملاً دروغ است. در واقع، من واقعاً معتقدم این «گزارش‌گری» جعلی آن‌ها خیانت‌آمیز است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 471K · <a href="https://t.me/VahidOnline/77763" target="_blank">📅 20:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZWyXcVUOGOnF7KScQAkfRV9mVD2w_FwUhh6YsizxJhMhGAKFsKT2SfdC5cqD86iaaThPNdBjgd58JfKTtTtB375nH64tA9PI8SKXKXqEScp_fLoCPTMHoFYSvX1Gcimim5oVqHbVPwXzIi5MjXO2xrqz8KS_5I-8fzjCXUUURCGZS3sZ-_cGUwZ0-45ZrhX_B6fQVle2PlvU6EuP5vd66sv0YR2pI8ioW90Twr7pz3dFxoKquIcIcs0Tkk55jBIGL_EblDcCGmNCM_E6M4CpGQpldgC_ntI5Q1T96h0M9EHCeTgtAh7pf6MB1o5phY2sHCRmEzeE_6l3yOaGCn8R-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
ایالات متحده مقادیر عظیمی «مهمات»، به‌ویژه از برخی انواع خاص، در اختیار دارد.
افزون بر این، هر مقدار که نیاز باشد، حجم زیادی مهمات تولید و به ایالات متحده ارسال می‌شود.
شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات تولیدی در تاریخ کشور ما هستند.
کسانی که این اظهارات خیانت‌بار را درز داده‌اند، تحت تعقیب قرار دارند.
برای آن‌ها درخواست محکومیت‌های طولانی‌مدت زندان خواهد شد!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 475K · <a href="https://t.me/VahidOnline/77762" target="_blank">📅 09:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WTdu3wS_CEck0jMEZfQmA2H6SmUZow6euODjeF879yif4ELat10E_naZHUM8ZEjObYqlGxio41YuIuf3hikOpVzLgNzUwGA0AFquDJDrIY0UvNN6Mk_oB0_Xvmb_PEGYPYzj7OBmpzo1M6CiTCb98KVmdIh1hD1OBmbfWGmLiHfOXtxi9Mx2sYMLYWUi8omQYYRZpt-5G6UBwsS1ofO1-ltCaYvA7cedxCfUQpvoeU1h7fQ9ssQG1CcapDZ71J0AdfdyWpgPE8nBt3Acb1329SmIFd3anMZ4qCxVk24RIjdwIsZxagxJRcMf0-KdaWXMQarSSWRT0Bu_Ui8XsHSVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشینگتن پست
:
درگیری ترامپ و هگست در کمپ دیوید بر سر نگرانی‌ها از کاهش ذخایر موشکی در جنگ ایران
ترجمه ماشین:
در نشست این آخر هفته در کمپ دیوید، رئیس‌جمهور ترامپ از پیت هگست، وزیر دفاع، درباره کمبود شدید مهمات توضیح خواست.
به گفته دو فرد آگاه از این گفت‌وگو به روزنامه واشنگتن‌پست، سرخوردگی دونالد ترامپ، رئیس‌جمهور آمریکا، از جنگ ایران هفته گذشته در کمپ دیوید فوران کرد؛ جایی که او از پیت هگست، وزیر دفاع، خواست توضیح دهد چرا ظاهراً درباره کمبود شدید مهمات ــ که اکنون گزینه‌های نظامی در برابر ایران را محدود می‌کند ــ گمراه شده است.
این رویارویی روز جمعه و در حاشیه نشست کابینه ترامپ در کمپ دیوید رخ داد. به گفته هر دو فرد آگاه از گفت‌وگو، ترامپ با عصبانیت به هگست گفت تصور می‌کرده مشکل مهمات «حل شده است». این افراد نیز مانند دیگران، به‌دلیل ترس از تلافی‌جویی، به شرط ناشناس‌ماندن صحبت کردند.
به گفته یکی از منابع، کمبودها، به‌ویژه در زمینه موشک‌های هدایت‌شونده دوربرد و موشک‌های رهگیر پدافند هوایی، از دلایلی بوده است که ترامپ در روزهای اخیر از اجرای حملات گسترده‌تر علیه ایران عقب‌نشینی کرده است.
کارولین لیویت، سخنگوی کاخ سفید، در پاسخ به پرسش‌های واشنگتن‌پست گفت: «این خبر صددرصد جعلی است. واقعاً هرگز چنین اتفاقی نیفتاده است. رئیس‌جمهور ترامپ نیز نهایت اعتماد را به وزیر هگست دارد.»
متن کامل فارسی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 489K · <a href="https://t.me/VahidOnline/77761" target="_blank">📅 08:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=Y0j9vDdrFNmbR46T70337pKHVseD8Lh0U3BITtnJyb9Yw5n_5OwH4fio9G7_b9mMsWetEvePX4Gbd7zgQ-OAETs2xzCJZcDXLTQIgSCHsglPSugBDJ6dGI_xOfqrm4zGapJteuTBURY13E6iL8tZw3c_VEAJy3pqG3BkRXbOI_8t9NrsbfJ2OUAXqMQrzzSFRdt1xRb32f4cfIUJlHnzndiP0PDkvceAXHcybIl7KnG58CZQ-YgHgXm0iyn02IHvtsYVHd03KMhZCUIibzNFlr1_8lEIwUez84WzzD7aFYKGHGp6VHmhJJUZhzWtfs2hCssK-ShfFfz0Q0mHguELqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=Y0j9vDdrFNmbR46T70337pKHVseD8Lh0U3BITtnJyb9Yw5n_5OwH4fio9G7_b9mMsWetEvePX4Gbd7zgQ-OAETs2xzCJZcDXLTQIgSCHsglPSugBDJ6dGI_xOfqrm4zGapJteuTBURY13E6iL8tZw3c_VEAJy3pqG3BkRXbOI_8t9NrsbfJ2OUAXqMQrzzSFRdt1xRb32f4cfIUJlHnzndiP0PDkvceAXHcybIl7KnG58CZQ-YgHgXm0iyn02IHvtsYVHd03KMhZCUIibzNFlr1_8lEIwUez84WzzD7aFYKGHGp6VHmhJJUZhzWtfs2hCssK-ShfFfz0Q0mHguELqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش مربوط به ایران،
تشخیص و ترجمه ماشین:
در ونزوئلا خیلی خوب پیش می‌رویم.
نفت زیادی از ونزوئلا می‌گیریم و رابطه‌مان با آن‌ها هم بسیار خوب است.
میلیاردها و میلیاردها بشکه نفت از ونزوئلا خارج می‌شود. ونزوئلا یکی از غنی‌ترین نقاط جهان از نظر نفت است.
و همان‌طور که می‌دانید، آن یک جنگ ۴۸ دقیقه‌ای بود؛ ۴۸ دقیقه طول کشید.
و هزینه جنگ را با آنچه از آنجا بیرون آورده‌ایم، چندین و چند و چند برابر جبران کرده‌ایم.
قبلاً کجا چنین چیزی شنیده‌اید؟ هیچ‌جا نشنیده‌اید.
همان روش قدیمی است، درست است؟ همان روش قدیمی.
غنائم از آنِ فاتح است، درست است؟
و ضمناً همین کار را در جمهوری اسلامی «دوست‌داشتنی» ایران هم انجام می‌دهیم.
داریم حسابی می‌کوبیم‌شان.
ترجیح می‌دهم توافقی انجام شود، چون نمی‌خواهم مردم را بکشم. نمی‌خواهم مردم را بکشم.
اما بالاخره در مقطعی قرار است... ما... ما برای بزرگ‌ترین حمله در میان همه حملات آماده شده بودیم و طی چند ماه گذشته ضربات بسیار سختی به آن‌ها زده‌ایم.
اما کاملاً آماده بزرگ‌ترین حمله از زمان جنگ جهانی دوم بودیم.
آن‌ها با من تماس گرفتند و گفتند: «لطفاً این کار را نکنید. بیایید گفت‌وگو کنیم.»
بعد می‌گویند: «ما هرگز چنین چیزی نگفتیم.»
می‌دانید چیست؟ رسانه‌های جعلی می‌دانند که آن‌ها چنین چیزی گفتند.
اما در حال گفت‌وگو هستیم. ببینیم چه اتفاقی می‌افتد.
ولی آن‌ها برای ما احترام قائل‌اند. به ما احترام می‌گذارند.
۴۷ سال گذشته است؛ ولی در واقع ۵۰ سال شده، چون سه سال است که می‌گویند ۴۷ سال. ۵۰ سال شده است.
هیچ رئیس‌جمهور دیگری کاری را که باید مدت‌ها پیش انجام می‌شد، انجام نداده است؛ زیرا ایران نمی‌تواند سلاح هسته‌ای داشته باشد. نمی‌تواند داشته باشد.
---
و به‌محض اینکه این وضعیت با ایران پایان یابد، قیمت نفت به‌شدت سقوط خواهد کرد. قیمت بنزین هم پایین خواهد آمد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 476K · <a href="https://t.me/VahidOnline/77760" target="_blank">📅 01:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urkpmjf4gMY3Fh1YlZc5f5H-X1CohX7lO-rb8RfKkeTdr7UIA4BOi_M877HTb6weLA-DyRxml8I9CyS7Ptj5ve3w1KZ-rb4LB9w1XlgTmi94I5ClawkjyHHJbTvwafztgKIUEWRYSAO3LZ4TaFBoglzAm572786lQgSkdcf-uarHSBqzarn-a2bnQo1gEsP8GuwGw3Xwd2EgIcIAZbYYg-1ImEJjCEzMsv0FomWDWCgWaR3iB1FiSDMDGmsr99H9LWkOAz75CCyTjtASBwFsqruGDpxO0WRgvf2glWv5l7ht_kUQRkdaQ7ZlPXgIpoaZQD_kdrvReKAs001HyduPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز چهارشنبه ۱۴ مرداد، حملات جدیدی را به جنوب لبنان آغاز کرد و دلیل آن را «نقض آشکار آتش‌بس» از سوی گروه حزب‌الله دانست. این حملات که با صدور نخستین هشدار تخلیه پس از هفته‌ها برای ساکنان شهرک «منصوری» همراه بود، دست‌کم یک کشته و ۱۱ زخمی بر جا گذاشت.
این رویارویی‌های جدید در حالی رخ داد که نمایندگان لبنان و اسرائیل با میانجی‌گری آمریکا در رم مشغول گفتگو برای پایان دادن به درگیری‌ها و عقب‌نشینی مرحله‌ای اسرائیل از جنوب لبنان بودند.
یک منبع آگاه از روند مذاکرات به خبرگزاری فرانسه گفت هیات اسرائیلی، سه ساعت زودتر از موعد مقرر خواستار پایان جلسه شد. به گفته این منبع، یحیئل لایتر، سفیر اسرائیل در آمریکا و رئیس هیات مذاکره این کشور، درز «اطلاعات گمراه‌کننده» از سوی طرف لبنانی را علت این تصمیم عنوان کرده است.
با این حال، انتظار می‌رود این مذاکرات روز پنجشنبه در سومین و آخرین روز خود استمرار یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/77759" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrL1O_q9AgtSu8jBuugrFMNRgxiyXWkEm548sF7OwXaJZrkdiha0kVpsiFx4z6Ro_hBbi_H-Sti5rMhYHqPwFmm4fvJaMw6qS-i6Wmq24CPB5C37ubt-ORei1xfc3M-9aRJD8IiWXElT4tPxQqnGwhaABU61Klhsz9k8IJ6pToj_gtGqaGQaDPNNpFCsrids5RpJPUSzI1wLAGxJCJ2jmB_vj16WSW9xqdl_TzQecptv4E_UGHSSgqVBFgEKsq5Ku5AzOCw4BQs6qoC_C0wjPhvbId30q-dWgQMBFNg_Q5-IS-bHIuZsMvYBYvxRN8PhTbThphHNPASjU4w1dkanXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده روز چهارشنبه ۱۴ مرداد تحریم‌های اعمال‌شده علیه شرکت هواپیمایی عراقی «فلای بغداد» را که پیش‌تر به اتهام همکاری با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بود، لغو کرد.
ا این حال، تحریم‌های بشیر عبدالقاظم علوان الشبانی، مالک معرفی‌شده این شرکت، همچنان به قوت خود باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77758" target="_blank">📅 19:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=M1JD1siKUVmoCIDa1CPoaxBMsTqEmp20Od6w59vAHCLlrMYvACv9df93UBdatisRNU34fERTy68WX6VUetH9qTqC5GNmnNNBAaIQjSkK_sk-Vstz7fSFf8DurmILNdo66q4CoCodcxkcP6WdwbjgA47g8fXcKOkvVb1zD5kVGCkNSeWKRYaQscfp_Yb2aONJ3mwVmmydK7SPyaTv1HLzRPOpsEA62-n1Zl-jV0EWGxGoDMz53Ef5b9PcwfQHtr4gah6tn9VpKhbbZrx3P12kUe4N8XVko43MMIgjjh6S1IvzFwelm1wX2W_3Fla5TDNYLpjDerHhtEZ2SvQFAfufpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=M1JD1siKUVmoCIDa1CPoaxBMsTqEmp20Od6w59vAHCLlrMYvACv9df93UBdatisRNU34fERTy68WX6VUetH9qTqC5GNmnNNBAaIQjSkK_sk-Vstz7fSFf8DurmILNdo66q4CoCodcxkcP6WdwbjgA47g8fXcKOkvVb1zD5kVGCkNSeWKRYaQscfp_Yb2aONJ3mwVmmydK7SPyaTv1HLzRPOpsEA62-n1Zl-jV0EWGxGoDMz53Ef5b9PcwfQHtr4gah6tn9VpKhbbZrx3P12kUe4N8XVko43MMIgjjh6S1IvzFwelm1wX2W_3Fla5TDNYLpjDerHhtEZ2SvQFAfufpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل روز چهارشنبه ۱۴ مردادماه با انتشار پیامی ویدیویی اعلام کرد این کشور با طرح پیشنهادی آمریکا برای خلع سلاح حماس و مدیریت غزه موافق نیست.
نتانیاهو در این پیام گفت: ««رئیس جمهوری ترامپ و تیمش فکر می‌کنند می‌توانند حماس را به خلع سلاح و غیرنظامی کردن غزه وادار کنند. ما در حال بررسی این موضوع هستیم. آنها پیش‌نویسی برای ما فرستادند، ما موافق نبودیم، این پیش‌نویس ما نیست؛ ما نظرات خود را ارسال کردیم.»
حماس هفته گذشته اعلام کرد به شرط خروج اسرائیل از نوار غزه، خود را خلع سلاح می‌کند. با وجود واکنش مثبت ترامپ، اسرائیل همچنان با این پیشنهاد حماس مخالف است و چند وزیر کابینه ائتلافی، پیشاپیش تاکید کرده‌اند که ارتش این کشور از غزه خارج نخواهد شد.
@
VahidOOnLine
نخست‌وزیر اسرائیل در سخنرانی خود در خاکسپاری رسمی پدربزرگ و مادربزرگ تئودور هرتسل، با اشاره به تحولات جاری تاکید کرد که این کشور در میان رویدادهای حساس نظامی و سیاسی قرار دارد.
بنیامین نتانیاهو با تمجید از رئیس‌جمهوری آمریکا گفت: «می‌خواهم این موضوع را روشن کنم؛ رئیس‌جمهوری ترامپ بزرگ‌ترین دوست ما و بزرگ‌ترین دوستی است که تا کنون در کاخ سفید داشته‌ایم و ایالات متحده نیز بزرگ‌ترین متحد ماست.»
با این حال، نخست‌وزیر اسرائیل با تاکید بر حفظ منافع بنیادین تل‌آویو افزود: «اما موجودیت اسرائیل — چه با توافق و چه بدون توافق — قابل مذاکره نیست. من مصمم هستم که هر آنچه برای تضمین امنیت و آینده‌مان لازم است را انجام دهیم.»
اسرائیل در حال حاضر در میانه گفتگوها برای دو توافق قرار دارد: توافق با لبنان برای خروج تدریجی نیروهایش از جنوب این کشور و توافق صلح غزه برای واگذاری مدیریت این مناطق به هیات صلح مطابق طرح ترامپ.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز چهارشنبه ۱۴ مرداد، در جریان بازدید از مرکز جذب سربازان جدید با تاکید بر اتحاد داخلی این کشور پس از حوادث هفتم اکتبر، تصریح کرد که تل‌آویو اجازه تشکیل کشور مستقل فلسطینی را نخواهد داد.
نتانیاهو با اشاره به این موضوع گفت: «ما در اینجا یک دولت تروریستی فلسطینی تاسیس نخواهیم کرد؛ دولتی که می‌دانیم قصد نابودی کشور-ملت یهود را دارد.»
نخست‌وزیر اسرائیل در ادامه افزود طرف مقابل در پی نابودی اسرائیل است، چرا که این کشور ترویج‌کننده ارزش‌های پیشرفت، دموکراسی و آزادی است؛ ارزش‌هایی که به گفته او، مورد نفرت «دشمنان بربر» قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77757" target="_blank">📅 17:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF-VTvYC5A9v3pUzgANjPonbr3qYi35vFDH38T9hBJLLn-gTil5VD-Ds4HxefsjeXoRAEYbCZIGPyhQIARFDnHUWQgJVsYhDClXzw-R9wamO3CItJWwwQzN-OB0ppMEPerQDPC0vuB69GulT1ChRazIiuaZtIcl3ZVLLCynGUd2KEwca3jhR_V6QDFu4cNCXKGAmASXIUSXUBCSG0xTKKN1NprSRCzVitF3I9gKNUGnM1LkJb-3KoGQFxUSWBsZlyEXVzl_ZBkPXzwLMhPF4SWBEhVBy-aEWBUNBL0THqHLi2hzolnUO6Ek0cvMfkQuvSZq0DGbQe4mxqg5T5yQ6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77756" target="_blank">📅 17:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeBVyJ8HVCPKvXCiWdoxrxBF4Sad3EsdeQQ12W63XY12iWVfIPL9a03SPz0f3rMI1TFAGInJ7uPLJC6uK6nJYT4eQEpnIjYt8D6Fgw1JV7PcVRDu5PZkD5g9iBpPDdcPGuAOT55wkqy9MOt9rGBk4HZ2nuT0KZ4F0zXDzbPhY-A87Pvtf3WcXx18HzrjQnISzlxh_alq7xqZtDAbgJyj-FydoN8aBR6_4aPoqvof1XSaJ7gB5jxTTzdNXB39bjFUtTprDIbTycCoBCAq_c0dfa-In7SYM-yWzfSx3J1QE4iogy7dyq5LAVzOdCbfzCwiF-u9KKDvn9sZHbRb9QO3SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در واکنشی دوپهلو به تکذیب دفتر مجتبی خامنه‌ای، اعلام کرد این تکذیبیه را می‌پذیرد، اما ابراز امیدواری کرد پس از «تغییرات مهم آینده» این دفتر نیز همچنان پابرجا بماند.
این واکنش شامگاه سه‌شنبه ۱۳مرداد۱۴۰۵، در صفحه اینستاگرام دفتر خرازی منتشر شد.
در بیانیه دفتر او آمده است: «گرچه به احترام قائد شهید و نیز رهبر معظم حاضر، تکذیبیه روابط عمومی و دفتر نشر آثار را حدوثاً می‌پذیریم، ولی امیدواریم پس از تغییرات مهم آینده در حوزه دفاتر فوق، این تکذیبیه همچنان باقی بماند.»
در ادامه بیانیه آمده است: «خداوند ما را در صورت استقامت و صبر در راه اهل‌بیت و ولایت معظم فقیه یاری خواهد فرمود.»
فرستاده است.
دفتر مجتبی خامنه‌ای ساعاتی پیش از انتشار پاسخ خرازی، ادعای او درباره هشدار رهبر جمهوری اسلامی به مسعود پزشکیان بر سر استعفا را تکذیب کرده بود.
در بیانیه این دفتر، بدون نام‌بردن از خرازی، آمده بود: «مطلب منتشرشده در فضای مجازی که در آن فردی، ادعایی را درباره واکنش رهبر انقلاب اسلامی به نامه رییس‌جمهوری محترم مطرح کرده، از اساس کذب و خلاف واقع است.»
دفتر مجتبی خامنه‌ای انتشار این ادعا را «زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه» توصیف کرده بود.
یک روز پیش از انتشار این تکذیبیه، ویدیویی از سخنان خرازی در شبکه‌های اجتماعی منتشر شده بود. او در این ویدیو مدعی شده بود مسعود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده است.
خرازی همچنین گفته بود مجتبی خامنه‌ای در واکنش به این موضوع نوشته است: «یک بار دیگر پزشکیان استعفا کند، استعفایش را می‌پذیریم.»
او مدعی شده بود پس از این هشدار، پزشکیان و دیگر مقام‌های دولت از مطرح‌کردن دوباره استعفا عقب‌نشینی کرده‌اند.
@
VahidHeadline
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77755" target="_blank">📅 17:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt_tMH6604WnPe9lfHYp_8unbEXUx3JtjiLTHC6kK5t3GRVnZdndQYz22ZwHwl2JRV2jOzUFnTJTdZ7fDgiFNENIVU1nT-wTdqBIGXYbBF0L_jpDAUES3druJomeie-gxRz083OBDXn0zjmOv6iOPjToeSfdmHbWUGo8zUxIl4NJ0RoMgQ4nO3u9cSr99NXt0qZVZCYJKWo8tL62ZcROUJYL0waaqkNarx5PwS6b5papZvybMRkubmRQNiZDhUgM8caNj7J2WJkI5aBVnDP8M2Peiz7DuCNj1L14meOgMiUEOeo9-HSg6J2orTU9tI5XB1gOVY7ocFJbj7n01WXe9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل متحد، اعلام کرد که از ۲۹ اسفند ۱۴۰۴ تاکنون، دست‌کم ۵۶ نفر در ایران با اتهام‌های امنیتی اعدام شده‌اند.
ولکر تورک با صدور بیانیه‌ای یادآور شد که از این تعداد ۲۷ نفر از معترضانی هستند که در تجمعات اعتراضی دستگیر شده‌اند.
او اعلام کرد که در این مدت روند صدور و اجرای احکام اعدام در ایران افزایش یافته است.
کمیسر عالی حقوق بشر سازمان ملل متحد از مقام‌های جمهوری اسلامی خواست تا همه اعدام‌ها را متوقف کنند و در مسیر لغو مجازات اعدام گام بردارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77754" target="_blank">📅 17:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B4N0e3_grArywAbwyp_va_fCpcLnmgNqLChh9Hu7r9c2mwG3cmbljSHPTFi0W-lJCT7IHrm3BhDzGNzQ6NZ94i2i9qqWtzbZtC2bnZBcMnQlAX6RRribxir-3wXIXx3yIYo0BAJ5vxc2LrJWOewc_Vq_u-SHwcf0-ezyj0Jex4x7Kr4ueGJtzot9YFbQevDUiQx2lN86pQMV8P5lOhf-8gXFEMAQCkcMo36gN4YuqTLX2G5v3GpHcmPvokKifsyL6kp7WuH8OIrrgQXvswjfjocGB4hLPjmy1Q6YAoITVLUToI-8FmG7tdAksfSH2j-97gbnCgKCOpzw1VGXq2XP6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی قاسمی حسنوند، شاعر، زندانی سیاسی سابق و شهروند اهل شهرستان الشتر، روز یکشنبه ۱۱ مرداد ۱۴۰۵ پس از اقدام به پایان دادن به زندگی خود مقابل دفتر سازمان ملل در اربیل جان باخت.
منابع آگاه به ایران‌وایر می‌گویند او پس از آزادی از زندان با مشکلات روحی و فشارهای ناشی از پرونده قضایی خود روبه‌رو بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77753" target="_blank">📅 17:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04787365a6.mp4?token=aoQKV2EzIjei3z_mx_bvgwtzBbRCtloGeELDg_huIIts_bvaHf5ih0dJeYX2HqtHlhYsjQFk4CUF4oZITKIYuCCu_PWRBn_xrqQGRS1IWOYqK0sNnZcgaKb9wxSHgUZzmfMvzcwzVYtbgjZ1MY1F-5U1e9uvLzXsB_WVDTcM7BX9je4KsBSGqGjA1TDcVjAXpJzztGw3l5g7Ps5KpcbIG36KnkEOBrCwMs7iv6BRtES3GGLKujZ5K50aei06Om7UbTzVi_A6JDPfL8RPzHq7P8bMtU1Rq5KzRY_MI-6fC0eAypQBmf3FZF1rueECt2Q5aVh1awjZQ5g_dD_94JWRlg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04787365a6.mp4?token=aoQKV2EzIjei3z_mx_bvgwtzBbRCtloGeELDg_huIIts_bvaHf5ih0dJeYX2HqtHlhYsjQFk4CUF4oZITKIYuCCu_PWRBn_xrqQGRS1IWOYqK0sNnZcgaKb9wxSHgUZzmfMvzcwzVYtbgjZ1MY1F-5U1e9uvLzXsB_WVDTcM7BX9je4KsBSGqGjA1TDcVjAXpJzztGw3l5g7Ps5KpcbIG36KnkEOBrCwMs7iv6BRtES3GGLKujZ5K50aei06Om7UbTzVi_A6JDPfL8RPzHq7P8bMtU1Rq5KzRY_MI-6fC0eAypQBmf3FZF1rueECt2Q5aVh1awjZQ5g_dD_94JWRlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
▪️
تنگه هرمز به‌زودی باز خواهد شد
▪️
مذاکرات با ایران به‌خوبی پیش می‌رود، اما تهران تمایلی به تایید آن ندارد
▪️
اگر بار دیگر عقب بکشند، ضربه سختی خواهند خورد
ترامپ:
اگر به اقتصاد نگاه کنید، اگر به اتفاقاتی که در حال رخ‌دادن است نگاه کنید... برای نمونه، ایران هرگز سلاح هسته‌ای نخواهد داشت. همین حالا هم دیگر نمی‌تواند داشته باشد، اما قرار است این موضوع رسمی شود.
تنگه [هرمز] خیلی زود باز خواهد شد؛ وگرنه ضربه بسیار سختی خواهند خورد و پس از آن، تنگه باز خواهد شد.
ما آماده انجام حمله‌ای عظیم بودیم؛ بزرگ‌ترین حمله از زمان جنگ جهانی دوم. بعد آنها با من تماس گرفتند و بسیار مؤدبانه گفتند: «لطفاً، می‌توانیم صحبت کنیم؟ می‌توانیم گفت‌وگو کنیم؟» آنها نمی‌خواستند... [جمله ناتمام است].
من هم گفتم: «بله، می‌توانیم صحبت کنیم. بیایید بالاخره این کار را تمام کنیم. بیایید انجامش دهیم.»
این کاری است که رؤسای‌جمهور دیگر باید طی ۵۰ سال گذشته انجام می‌دادند. می‌دانید، مدام عدد ۴۷ سال را می‌شنوید، اما سه سال است که همین عدد گفته می‌شود؛ حالا دیگر بیش از ۵۰ سال شده است.
رؤسای‌جمهور دیگر یا کشورهای دیگر باید می‌توانستند این کار را انجام دهند.
من کاری را انجام دادم که مجبور بودم انجام دهم؛ چون اگر آنها سلاح هسته‌ای داشتند، تمام این جهان جای متفاوتی می‌شد.
خبرنگار فاکس‌نیوز:
اگر دوباره عقب‌نشینی کنند و زیر توافق بزنند، کارشان تمام است؟
ترامپ:
اگر دوباره زیر توافق بزنند، ضربه واقعاً سختی خواهند خورد. خودشان این را می‌دانند و درک می‌کنند. من انتخاب دیگری ندارم. آنها نمی‌توانند سلاح هسته‌ای داشته باشند. موضوع بسیار ساده است.
این‌طور نیست که بگوییم: «خب، بیایید درباره چیز دیگری فکر کنیم.» نه؛ رؤسای‌جمهور بسیاری باید طی سال‌های طولانی این کار را انجام می‌دادند، اما انجام ندادند. حالا من دارم انجامش می‌دهم.
اوباما را کاملاً سرکیسه کردند. او فکر می‌کرد می‌تواند با پرداخت پول خودش را از این وضعیت خلاص کند. میلیاردها، ده‌ها میلیارد دلار به آنها داد؛ آن‌هم به‌شکلی بسیار احمقانه.
۱٫۷ میلیارد دلار پول نقد، اسکناس‌های سبز، در یک هواپیمای بوئینگ ۷۵۷؛ هواپیمایی پر از پول نقد. احتمالاً وقتی آن را دیدند، گفتند: «حتماً شوخی می‌کنید!»
نه، نمی‌توانید با پول‌دادن خودتان را از چنین وضعیتی خلاص کنید؛ تنها راه این است که با جنگیدن راه خروجتان را باز کنید.
اگر ما این کارها را انجام نداده بودیم، آنها مذاکره نمی‌کردند. ما ضربه بسیار بسیار سختی به آنها زدیم. اما ضربه سخت‌تر هنوز در راه است و امیدوارم مجبور نشویم از آن استفاده کنیم. امیدوارم مجبور نشویم.
گفت‌وگوهای بسیار خوبی داریم. آنها دوست ندارند به این موضوع اعتراف کنند، اما این کمی آزاردهنده است. به افرادی مثل شما می‌گوییم که گفت‌وگوهای فوق‌العاده‌ای داریم، بعد یک نفر از ایران می‌آید و می‌گوید: «ما دیدار نکرده‌ایم، ما...» [جمله در زیرنویس ناتمام است].
تمام روز چنین دروغ‌هایی می‌گویند. متوجه هستید؟ باورنکردنی است. می‌گویند: «ما این کار را نکردیم.» می‌گویند درباره موضوع هسته‌ای صحبت نکرده‌ایم.
خب، پس درباره چه چیزی صحبت می‌کنیم؟ آنجا نشسته‌ایم و بی‌کار انگشت‌هایمان را به هم می‌زنیم؟
اما اهمیتی ندارد. اینها فقط حرف است. تنها چیزی که اهمیت دارد، عمل است. آنها می‌خواهند توافق کنند. خواهیم دید چه اتفاقی می‌افتد. اگر توافق نکنند، برایشان خیلی بد خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77752" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dnXdJ7rvwM03kXK9DDHMdaIPJ_GAhm5Z0jcez3DBp-sVtx5oVo_MYsMRTKVL27wuoSMfin6hZdrxBbqL1vwD6WmXtMRmnSEawl6_Ex6tzi_r9NI9YJfEKdsbkr76m1kDMoWxeruRG2JIfU84vZOPEQOAJz8uoraJ48aqwBztOvskYLgWoa-ljqfFcnE-DZhhHSmzLfm1QNSifMA43qUZ1xNe5fPYQs0xWol5zYuld7k7NagDcOt_BoJtyzEJgGtMPMS5Ms_TsO26c3X-n7f7OwtZggfuiDJEVwJ7pd9lwek7i0gt5B-6gl346yLVYWxp-FKWCiEySFS1Lmpa8d4UWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"آمریکا به توافق درباره هرمز نزدیک شده و به‌دنبال اعلام آن در روز چهارشنبه است"
اکسیوس، ترجمه ماشین:
به گفته دو منبع منطقه‌ای و یک مقام آمریکایی، آمریکا، ایران و عمان به دستیابی به یک توافق موقت برای بازگشایی تنگه هرمز نزدیک شده‌اند و آمریکا قصد دارد این توافق روز چهارشنبه اعلام شود.
🔻
چرا اهمیت دارد:
هدف از این توافق که چند هفته است درباره آن مذاکره می‌شود، ازسرگیری آتش‌بس میان آمریکا و ایران و آغاز دوباره مذاکرات بر سر یک توافق هسته‌ای است.
▪️
رئیس‌جمهوری ترامپ روز شنبه تصمیم گرفت تهدیدهای خود برای آغاز یک کارزار بمباران گسترده را عملی نکند تا فرصت بیشتری برای دیپلماسی فراهم شود. با این حال، اگر به‌زودی توافقی حاصل نشود، ترامپ ممکن است با حملات بزرگ موافقت کند.
▪️
توافق در حال شکل‌گیری برخی از خواسته‌های ایران برای کنترل بیشتر بر رفت‌وآمد در تنگه هرمز را تأمین خواهد کرد؛ کنترلی که ایران پیش از جنگ در اختیار نداشت.
🔻
اصل خبر:
به گفته دو منبع منطقه‌ای، توافق مورد بحث یک سازوکار موقت ۶۰روزه میان عمان و ایران در تنگه هرمز ایجاد می‌کند که امکان تمدید آن نیز وجود دارد.
▪️
همه کشتی‌هایی که از طریق تنگه وارد خلیج فارس می‌شوند، از یک مسیر شمالی در آب‌های ایران عبور خواهند کرد.
▪️
همه کشتی‌هایی که از تنگه خارج می‌شوند و به دریای عرب می‌روند، با هماهنگی ایران از یک مسیر جنوبی در آب‌های عمان عبور خواهند کرد.
▪️
در دوره ۶۰روزه هیچ‌گونه عوارض یا هزینه‌ای دریافت نخواهد شد.
▪️
طرف‌ها تلاش خواهند کرد ظرف ۳۰ روز مین‌های دریایی را از مسیر میانی تنگه پاک‌سازی کنند.
▪️
پس از پاک‌سازی مسیر میانی، این مسیر بر اساس مفاد یک سازوکار دائمی که قرار است میان عمان و ایران درباره آن مذاکره شود، برای رفت‌وآمد کشتی‌ها در هر دو جهت مورد استفاده قرار خواهد گرفت.
🔻
بله، اما:
کاخ سفید، عمان و میانجی‌های منطقه‌ای سه هفته پیش تصور می‌کردند با ایران به توافق رسیده‌اند، اما ایران حملات به کشتی‌ها را از سر گرفت. این موضوع به دو هفته درگیری و وضعیتی نزدیک به جنگی تمام‌عیار منجر شد.
🔻
پشت‌پرده:
به گفته منابع منطقه‌ای، علاوه بر مذاکرات میان عمان و ایران، مقام‌هایی از قطر، پاکستان و عربستان سعودی نیز در تلاش‌های میانجی‌گرانه مشارکت داشتند.
▪️
منابع منطقه‌ای گفتند کاخ سفید به‌طور فعال در مذاکرات حضور داشت. در روزهای اخیر چندین تماس میان استیو ویتکاف، فرستاده ترامپ، عباس عراقچی، وزیر امور خارجه ایران، و بدر البوسعیدی، وزیر امور خارجه عمان، انجام شد.
▪️
دو منبع منطقه‌ای گفتند عراقچی در پایان هفته گذشته در اصل با توافق موافقت کرد، اما همچنان به تأیید مجتبی خامنه‌ای، رهبر جمهوری اسلامی ایران، و شورای عالی امنیت ملی نیاز داشت.
▪️
یک مقام آمریکایی و یک منبع منطقه‌ای گفتند رهبری ایران روز سه‌شنبه روند تأیید توافق را تکمیل کرد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77751" target="_blank">📅 06:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idw7UMzt1MiMUzX1ykP4fCMdJPc9szWyRHWbGTG44Fu9ZReAvdwhHh_ZnDtqn8bw2fbI626pjxBMbuFfhmXt2j7WYQYUR5OlNsMfB4-eYE1KQgGDOwHyOUFcu3RdA1IsA4llVJPKTRX_SytjT2jc62YERFqowoPOiKZQwt5n_2bkiOIVc5DXrZ_4AS57eS7ivmn7Q5BwT-Tl4kCaozbibFmowhvME-pTAzQSxKPKq14Q1ZDX3Uj5dSHGyLZMR71GXEmtMnHna9-g5WIzHNjCk3kMWw4bK4o7ibQYXl0fy1mk39menoqqyQa_3weSMUgRrKo_tMUWmxu1i3k7CdMsEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
مسیر جنوبی عبور از تنگه هرمز همچنان برای همه کشتی‌های تجاری که قصد گذر از این آبراه بین‌المللی را دارند، آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی با وجود تجاوز بی‌دلیل ایران، به بیش از ۱۰۰۰ کشتی کمک کرده‌اند تا با موفقیت از این تنگه عبور کنند و این ترددها امروز نیز ادامه دارد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/77750" target="_blank">📅 01:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77749">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=Md_4NTnpJ-rL4lA2YSM0PwcEJpG0rUjBF7x1Kida04l1FDn-vhUrOhKGoii0nrdyOX8bk4gTg6o0Dk8RO3IYgtuE2m1HpR7FTEQD7di7qr3RF-JH6FzigguU1sQgKLAI-tY6kkCE49sRT9sVINzaayJfqrlMfCvjA_KsprD6eHFVBd3peMjnKevoRMdsDAKjLBjJ_Q8hdKekG-MJ5HbaOWsvy6NDzL9XmDptTFXEl4wRtTcZUeR-jwNVjKs3589aPa7dEldZUF8o9c0XKHjrrX4H7Iv-cZxmuzT_JLUlzFsCOZFswpI-GPi5CskW-SWuD6z6QYnaCHLjkIePMYKShoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=Md_4NTnpJ-rL4lA2YSM0PwcEJpG0rUjBF7x1Kida04l1FDn-vhUrOhKGoii0nrdyOX8bk4gTg6o0Dk8RO3IYgtuE2m1HpR7FTEQD7di7qr3RF-JH6FzigguU1sQgKLAI-tY6kkCE49sRT9sVINzaayJfqrlMfCvjA_KsprD6eHFVBd3peMjnKevoRMdsDAKjLBjJ_Q8hdKekG-MJ5HbaOWsvy6NDzL9XmDptTFXEl4wRtTcZUeR-jwNVjKs3589aPa7dEldZUF8o9c0XKHjrrX4H7Iv-cZxmuzT_JLUlzFsCOZFswpI-GPi5CskW-SWuD6z6QYnaCHLjkIePMYKShoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت امیرعلی حیدری و سروش کرمی، دو نوجوان کشته در اعتراضات دی ۱۴۰۴ که هفته گذشته برای دومین بار به خاک سپرده شدند.
یکی از خانواده‌ها بعد از هفت ماه متوجه شد جسد اشتباهی به آنها تحویل دادند و خانواده دیگر دریافتند فرزندشان در بازداشت نیست و کشته شده.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77749" target="_blank">📅 01:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=SUo520L1fWOtALr5lW2yeerDuI7-MnLdQlpKKUXvyhKN2GZJr15kM2mvHYKXnRofFHK-h7G3BUnDgbphHi8U3SKi8gPcjjHe5dHN1qKE02B2-tO5P4JBerN34m2GPw2uVH5H84R4333aFrrkYNlQEMOWGAumKnBbXwfjdA114BLH9IRerx9aNH6jl5LwVe7pR0j7dtIqAuJDEhJSwqCa767alyTKGBusr6CfSHYdpRtXTS1EWO9rdbmJLXuAU7UZhSqaQ1SCbAg4opaOReh1-mwQ-l54lufi0nr88WqPzU3ijshoIS2CaSmA8hrFexRweP2Jvp7tst3ILpY2uwB7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=SUo520L1fWOtALr5lW2yeerDuI7-MnLdQlpKKUXvyhKN2GZJr15kM2mvHYKXnRofFHK-h7G3BUnDgbphHi8U3SKi8gPcjjHe5dHN1qKE02B2-tO5P4JBerN34m2GPw2uVH5H84R4333aFrrkYNlQEMOWGAumKnBbXwfjdA114BLH9IRerx9aNH6jl5LwVe7pR0j7dtIqAuJDEhJSwqCa767alyTKGBusr6CfSHYdpRtXTS1EWO9rdbmJLXuAU7UZhSqaQ1SCbAg4opaOReh1-mwQ-l54lufi0nr88WqPzU3ijshoIS2CaSmA8hrFexRweP2Jvp7tst3ILpY2uwB7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه ۱۳ مرداد اعلام کرد نیروهای این کشور تا خلع سلاح کامل حماس، از خطوط فعلی در نوار غزه عقب‌نشینی نخواهند کرد.
نتانیاهو در ویدیویی که در شبکه‌های اجتماعی منتشر شد، گفت: «ترامپ و تیم او بر این باورند که حماس می‌تواند کاملا خلع سلاح و غزه غیرنظامی شود؛ ما در حال بررسی این موضوع هستیم.»
نخست‌وزیر اسرائیل همچنین با اشاره به طرح پیشنهادی آمریکا افزود: «آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم، چرا که پیش‌نویس ما نبود. ما پاسخ‌های خود را ارسال کرده‌ایم.»
او تاکید کرد که نظرات و پاسخ‌های تل‌آویو پیش از رسانه‌ای شدن این موضوع به طرف آمریکایی تحویل داده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/77748" target="_blank">📅 23:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRBI2RBZeZrFVdiZ5PXDiCvKrQ92V4hvNS1da9tLwX2ABaKovOZ7gKx2-oqDhAOvD89nfmgIEK2c_l-_YCzFWHb-5SYSWZTBMCBrCxQwnBa61mGF3m1LNcTuuB1ZidIDWmmcDMMkRRUQfzIfg0gVG8PKC6PBElmqyv6kpGpN710lOL9preeLgu8FKWFhiRE2duqxbB4k5RGiL95kRdmW3grngypq4B1m5AOnf-vTR95oCZNDjLGD3CZeN1QO10DCnQTOLLb8hDcaqd7zBLX3z8onYI3zLJ_wm5nUr93dcnuMcYDAFavOb3aCHS8lRkM8mwIw1q-F4uVCzZlaT_hy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی قطر گزارش داد تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه در تماس تلفنی با دونالد ترامپ، رییس‌جمهوری آمریکا، آخرین تحولات منطقه، به‌ویژه تلاش‌ها برای کاهش تنش میان آمریکا و جمهوری اسلامی و نزدیک کردن دیدگاه‌های دو طرف را بررسی کرد.
بر اساس این گزارش، ترامپ از نقش قطر در حمایت از تلاش‌های دیپلماتیک و تسهیل گفت‌وگو میان طرف‌ها برای تقویت امنیت و ثبات منطقه قدردانی کرد.
امیر قطر نیز بر اهمیت ادامه گفت‌وگو، استفاده از راه‌حل‌های دیپلماتیک و پایبندی همه طرف‌ها به مفاد یادداشت تفاهم میان تهران و واشینگتن تاکید کرد. او همچنین خواستار حمایت از ابتکارهای بین‌المللی برای مهار تنش‌ها شد.
دو طرف همچنین درباره شماری از موضوعات مورد علاقه مشترک گفت‌وگو و بر ادامه هماهنگی و رایزنی درباره تحولات منطقه‌ای و بین‌المللی تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77747" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIm8qv06Zy_9VOakGTsnByLvKkGcgZnHXj1cw8G3bxosfZxYTe_kCqhZ51jEaI-a7bHgP4jneRROZZNWD3c6G0p0IADJB67KPhw7bRB7HSijRnWtsLIaRa7an7GYbeUVKApTO_pjUOYHQIHbmCsiWbxK_J-II45WK2pMXLyamsg9p7ZjpnegC8rSkrwtKNrr3MRd7BfKaDwUx5jREkvaQ9m3JO87gqcoTCUqNTuzX2zt2ZIwuvWhgLDMXMUvcHaS6rbSB2Crua4407tt829UegwHS4l8hg7gT1aqqXjvQOldNfQQVLKnmJ52jsVCTUa6-8jv33UEVj4-91pxHeVftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشتیرانی هند روز سه‌شنبه ۱۳ مرداد اعلام کرد که یک پرتابه به یک کشتی با پرچم هند در نزدیکی یمن اصابت کرد که باعث واژگونی و غرق شدن آن شد.
ساربانا‌ندا سونووال در پیامی در شبکهٔ ایکس نوشت که اما هر ۱۴ ملوان حاضر در کشتی، از جمله ۱۳ تبعهٔ هند، توسط گارد ساحلی یمن نجات یافته و به بندر مخا منتقل شدند.
وزارت خارجه هند نیز اعلام کرد که این کشتی تجاری به نام «ام‌اس‌وی فیض نور علیا» روز ۱۳ مرداد در دریای سرخ و در سواحل یمن غرق شده و این وزارتخانه در حال هماهنگی با مقام‌های یمنی دربارهٔ این حادثه است.
پالایشگاه‌های هند از زمان حملات حوثی‌ها به چند نفتکش سعودی، به دریافت محموله‌های نفتی خاورمیانه به‌صورت تحویلی روی آورده‌اند.
تردد در دریای سرخ در نزدیکی سواحل یمن به‌دلیل اقدامات حوثی‌های همسو با تهران مختل شده است. حوثی‌ها با ایجاد اختلال در صادرات نفت عربستان، دامنه درگیری میان آمریکا و ایران را گسترش داده‌اند. پیش‌تر نیز عرضه نفت از طریق تنگه هرمز مختل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77746" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bhWzLBc_rpE4Pgc9MGlRcGYPpiJwG0eQ4-9IMfUieb8CvZ1Ok5nxhyxhJ3zf8z0_VHRpJ9Hez3NKpkPB5BkDPeKehKQBnkiuqdEOvVpSwZ25o8hL6pNmd1DjNqnY0BFMOu_1vxDOeFXMKXGHZYUUnVx9wSOfZ2mILIoGJ5WY2bLKCGDUGVUOsKksNr1jmie2nB_wUrZDCLObQQ_rGIt_3uaYKRXgwNOKXfV01hU8TEDvn3HKxQjdP5iXHtMZ2Ir4djto0Gwl_LkYOjmRtQ120h_gpMZqVU6F1KTaj7m4wWwXucm8X1DOXElhjMYpVIRkLwwq22qz-gfOEbKNudL0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZRHXdDdxxmiFskszGr7Rhqdh4eW5fGGaMESN9SGHl-jJHtyUeBqUnQD88dpvuLU64tzyhe0G2XUI3EdfRmvsgkdQZm-YowBxooeZPX2qLnZN9yykGW9EbvBigGxTCALDiknzExLHjLc7TiAN-mNjG6mp_u6RV69DeTtvXtEbo8inWX3xNqjvb1vMyUUZ1sikpG57T67wNOH9HgLKZmrAa6GxYQ2tKu3qQWcQwbPtC_lpr0BweuIQg3aLKO8P_wB7WhZ-fyVuHoJifXXZvEeeh9aE7jkGtntDRHGWSEnANSYM-_IC5QbcH8xDBRsFqQffA-LnPwYdomfVAWcHUkfKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LeidoPg-uo5gZaUehIL11-qKI-eh_YVjgtHsBk5M9olNL9WGkoD_Ve08bqlOOg9SXcgwPDRQkEQvwPovGFNxtz_7vRSFWytEnO_LEsRU4eiKqmaFF6FIOBjd5GfQ-WoIVN2Ix7Jx5zI9saqLx2jEEBLTo3BJmVJBWWr6TjjarOiC7jRyw5CIOUAcRM1iTQsWRNiTpbjyxRd_5WaXiWBYaNDsLsvLyw8zGU1BT_swPkqcKMQmy_I3lZvmyelUKVowZyfxmOElC1b4o3-IQVMOtrp_wkSUI4VLOSr5MRvfnnA4RQhrHDuJMncRy_Kn_kyQIo8d9qNfHyhx4x-AEfFTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LA_dP4PqovfdhlKQU7VRxUTO-_iHNvnZKR9nhNFrOjoghKjAiKgeGtM1AoqUl4g1O9DKiP4v2ZDtCGI5h8QZq1eWwXXHlUyN7ZeAohUpp7hcLs-wok45VYXZ102QMRy5Uez2HjmUdP-maEY0tcgOyjXxHvsgwEIvFVcvJOdQLo5-IbrQm3gbnh4a2a1goTWN3Y_o7M3-uVvv9GIcgO07uQz4ZOoQQ0_1iw2Rz1SfS6buG07TFfXp3kVf4litVmobXfaQCdUhTFwZI--AnUzSvSJ3GB50xRZMdDM2FibEptN5yQ6zouv1613hgKL0QwYkIURjVILxo9mMw_3MBZCpDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=bSkTxTYvxizlWfdeGRp33QzzCwnjXhDkAmA3iun4EbzEzW7clTtpuaEXNCy5wotw_JpEwoPVu2MkDuAFb9UpXj0EOBvqKGn7ZX8ZbCzxQZBExpdukpIaffwuUtvO-tX43APtsaFOkd8-GRCUs8KctzHw8XL3sq_3nx0I0Gm3q-JOkyuFWDnN1-11AUu1SKMjHXE10AN2NuOPFTnTOpF2Dm8m0iy58eyRMWWDAVKlwDC2Ny-9gDw3B2O9h_ThHRog1VWiu683EwrPQhuo-45ZNF-Cq4I6mfKhdLQJIPjya3aqXd6se9-5eGvIhbgjnJAuw4pO62pvuBnSeH9A3tdrDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=bSkTxTYvxizlWfdeGRp33QzzCwnjXhDkAmA3iun4EbzEzW7clTtpuaEXNCy5wotw_JpEwoPVu2MkDuAFb9UpXj0EOBvqKGn7ZX8ZbCzxQZBExpdukpIaffwuUtvO-tX43APtsaFOkd8-GRCUs8KctzHw8XL3sq_3nx0I0Gm3q-JOkyuFWDnN1-11AUu1SKMjHXE10AN2NuOPFTnTOpF2Dm8m0iy58eyRMWWDAVKlwDC2Ny-9gDw3B2O9h_ThHRog1VWiu683EwrPQhuo-45ZNF-Cq4I6mfKhdLQJIPjya3aqXd6se9-5eGvIhbgjnJAuw4pO62pvuBnSeH9A3tdrDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت ایالات متحده ممکن است تا روز چهارشنبه برای بازگشایی تنگه هرمز با ایران به توافق برسد؛ توافقی که به گفته او می‌تواند قیمت انرژی را تثبیت کند.
او روز سه‌شنبه در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «ما با ایرانی‌ها در حال مذاکره هستیم و فکر می‌کنم این احتمال وجود دارد که امروز یا فردا برای بازگشایی تنگه و حرکت به سوی وضعیتی عادی‌تر در این درگیری به توافق برسیم.»
بسنت در پاسخ به این پرسش که آیا چنین توافقی به ایران اجازه خواهد داد از کشتی‌های عبوری عوارض دریافت کند، گفت: «فکر می‌کنم منظور، آزادی رفت‌وآمد خواهد بود.»
@
VahidHeadline
مارکو روبیو، وزیر امور خارجه آمریکا، روز سه‌شنبه ۱۳ مردادماه اعلام کرد هدف نهایی مذاکرات با ایران، دستیابی به توافقی برای خلع سلاح هسته‌ای این کشور است و گفت توافق کنونی که تمرکز اصلی بر آن قرار دارد، به تضمین عبور امن کشتی‌ها از تنگه مربوط می‌شود.
روبیو با اشاره به ادامه تردد کشتی‌ها و انتقال نفت از تنگه گفت: «همین حالا کشتی‌ها از تنگه عبور می‌کنند و صادرات نفت ادامه دارد. تنگه باز است.»
او افزود: «خلع سلاح هسته‌ای ایران توافق نهایی است. توافق فوری، که اکنون بیشترین تمرکز بر آن قرار دارد، مربوط به تنگه است.»
روبیو همچنین گفت مذاکراتی میان عمان و ایران درباره فراهم کردن امکان عبور امن کشتی‌های بیشتر از تنگه در کوتاه‌مدت در جریان است که آمریکا نیز در آن دخیل است. به گفته او، این مذاکرات پیشرفت کرده، اما هنوز به نتیجه نهایی نرسیده و واشنگتن امیدوار است به‌زودی به جمع‌بندی برسد.
@
VahidOOnLine
قطر اعلام کرد تلاش‌ها برای دستیابی به راه‌حلی دیپلماتیک میان ایران و ایالات متحده ادامه دارد، اما هنوز توافقی حاصل نشده و هیچ مذاکره مستقیمی میان دو طرف برنامه‌ریزی نشده است.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، روز سه‌شنبه ۱۳ مرداد ۱۴۰۵ به خبرنگاران گفت رایزنی‌های دوحه با ایران و آمریکا همچنان ادامه دارد. به گفته او، این رایزنی‌ها بر دستیابی به «راه‌حلی کوتاه‌مدت» متمرکز است تا زمینه ازسرگیری گفت‌وگوها و احیای کامل روند میانجی‌گری فراهم شود.
اظهارات سخنگوی وزارت خارجه قطر یک روز پس از آن مطرح شد که دونالد ترامپ، رییس‌جمهوری آمریکا، گفته بود مذاکرات با تهران در جریان است و ایران با «آخرین فرصت» برای دستیابی به توافق روبه‌روست.
ترامپ گفته بود این مذاکرات به درخواست ایران، عربستان سعودی، امارات متحده عربی و قطر انجام می‌شود و افزوده بود: «این آخرین فرصت آن‌ها برای امضای یک توافق خوب است.»
در مقابل، مقام‌های جمهوری اسلامی تأکید کرده‌اند که هیچ مذاکره‌ای با آمریکا در جریان نیست و گفت‌وگوهای کنونی ایران تنها با عمان و درباره تنگه هرمز انجام می‌شود. تهران همچنین اعلام کرده است که این هفته هیچ نشست مهمی برنامه‌ریزی نشده است.
@
VahidHeadline
قیمت نفت روز سه‌شنبه ۱۳ مرداد پس از اظهارات مقامات قطر و وزیر خزانه‌داری آمریکا که امیدها را برای حل دیپلماتیک مناقشه خاورمیانه و بهبود عبور نفتکش‌ها از تنگه هرمز افزایش داد، حدود ۴ درصد کاهش یافت و به پایین‌ترین سطح خود در سه هفته اخیر رسید.
@
VahidOOnLine
—-
ترامپ هم دوباره چندین پست پشت هم منتشر کرد که یکیش لینکی است مربوط به مطلب ۲ روز پیش
breitbart
با تیتر:
ترامپ: «توافق قریب‌الوقوع است»؛ مذاکرات با ایران درباره خلع سلاح هسته‌ای و هرمز دوشنبه از سر گرفته می‌شود
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77740" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWx5Votm5X1sWjk4EOHVDsAedCrbtjmMubvRrqN4xcn22Gk693K5mwSuUW3PwTswLCXZACycOyJnbhBYhBN53SG-SgIVTyuvyC4sHqm_jKfdxBx4PwoswPNyfO0d2e8Cmbq4HhGePN-lIq3lw6FIa9Nj6J5-pHVnXY92Hvm1hgn7tzXAZsHxhH95j9z4FrlBYMIYXz7BzKphrPDUAqnF_4nYKpH6Najdhj4pcADwwgRbpXvqNDWRUc8diIIxYDYKGEigofo5SS_4V61gcOPHSljOt-s6XVRzgzTdQQ4pSQBLHFh2LEFi9oCXL4pLKxvSe_QVSmHwlvt7QqAuCWEHGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=hIvOmBpBiQet9XVbDU5MkK1P4M8IUC11JPngwUaKKdfgJ6v5qLO0TgIwFHqeG6a2dkBuer9QXap667Fvbrs5kVXjbYDO6l5wnkaq4PmFcBBVYz_n8rQiFiq3gLtPqDOyBnL85MGLV61LotzS-kIh2fKXZIvoAID9bOUyPjACJHWvF1U518-feAC4Bp3vXq1QUdqEZjajY4v9V2033LPrhXiudShY7tPbFx5XeAVLFjiIpay8MbQCkVjNbSu9T-RVpOmRl_zfoj_9V0GfdXXKA6-6zLtgS-0jrbHGRNzTDwrmTkL__NnSebmCA7enLYKJt-hLHFRkCsmPQ6mmAbghzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=hIvOmBpBiQet9XVbDU5MkK1P4M8IUC11JPngwUaKKdfgJ6v5qLO0TgIwFHqeG6a2dkBuer9QXap667Fvbrs5kVXjbYDO6l5wnkaq4PmFcBBVYz_n8rQiFiq3gLtPqDOyBnL85MGLV61LotzS-kIh2fKXZIvoAID9bOUyPjACJHWvF1U518-feAC4Bp3vXq1QUdqEZjajY4v9V2033LPrhXiudShY7tPbFx5XeAVLFjiIpay8MbQCkVjNbSu9T-RVpOmRl_zfoj_9V0GfdXXKA6-6zLtgS-0jrbHGRNzTDwrmTkL__NnSebmCA7enLYKJt-hLHFRkCsmPQ6mmAbghzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوها از کانال‌های غیررسمی حکومتی
درگیری میان حامیان جمهوری اسلامی و مقلدان صادق شیرازی، از مراجع تقلید منتقد جمهوری اسلامی، در جریان مراسم اربعین در کربلا به بازداشت ۱۴۰ نفر و مجروح شدن ۵۴ نفر انجامید.
شبکه تلویزیونی «اشعائر» عراق، رسانه نزدیک به "آیت‌الله صادق شیرازی"، صبح دوشنبه ۱۲ مرداد ویدیویی از این درگیری منتشر کرد.
بر اساس گزارش این رسانه، گروهی با در دست داشتن تصاویر علی و مجتبی خامنه‌ای و پرچم‌های «یا لثارات الحسین» و «یا لثارات الخامنه‌ای» مقابل دفتر آیت‌الله صادق شیرازی در کربلا تجمع کردند و علیه او شعار سر دادند.
این رسانه می‌گوید حامیان علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، و فرزندش مجتبی خامنه‌ای هنگام عبور از مقابل دفتر صادق شیرازی این شعارها را سر دادند که با واکنش هواداران و مقلدان این مرجع تقلید روبه‌رو شد.
به گفته کاربران شبکه‌های اجتماعی، این درگیری ابتدا با مداخله پلیس عراق متوقف شد، اما در ادامه میان حامیان جمهوری اسلامی و نیروهای امنیتی عراق نیز تنش و درگیری رخ داد و پلیس عراق در نهایت با استفاده از قوه قهریه به آن پایان داد.
بر اساس گزارش‌های منتشر شده، در جریان درگیری مقابل موکب منتسب به آیت‌الله صادق شیرازی، ۱۴۰ نفر بازداشت و ۵۴ نفر مجروح شدند. این آمار تاکنون به‌طور مستقل تأیید نشده است.
همچنین در برخی گزارش‌ها ادعا شده است که حسین ستوده، مداح حکومتی، از چهره‌های حاضر در این تجمع بوده و تلاش داشته این مراسم را به موضوعات سیاسی پیوند بزند.
"آیت‌الله صادق شیرازی" از منتقدان نظریه ولایت فقیه است و رسانه‌های جمهوری اسلامی او و جریان منتسب به وی را با عنوان «شیعه انگلیسی» معرفی می‌کنند. او ولایت فقیه را محدود به امر قضاوت می‌داند و با تفسیرهای جدید از اسلام و مذهب تشیع مخالفت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77735" target="_blank">📅 18:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aEvpbEwtJWggvAHDV9R_4Jxvaf4Z8vHuX6ptxALRbzho75M8CH6tIeSZ9IxRS6VrmjvoeMWeDk3QLSoH8w85k4p472XY4WEEai7E-ZpnNTAshX6d9O0ry_eCkEzcpFhzRL3uLeCJDjhyetPFsYiNDOzJpT5QAFeVZUYUXu4Oghk5xik0I1FrzeRo_Yvcs4zxdvfiSFuMpSlmQIFV79ggtqRH14ZlhY_FF_uXljNpVK0iLA52up4WwMQa2mZZIy1uPyfLH3aIWY_hy24ckiax7tusrjdnjB8Y2rK8zcmw9Fk6ucbfN1C8wZY1-NCpCQ5SDTZskpSiEsk97jIE06C4GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vQ3kG5AYDv_Iwv2x3dkGHhKGuHJZYHTSNVUqeaPXkzSnVfKvn5SZl57KikbSpjTF7mDJ512v7NDl9Syq3MhCxnJCNHuYXS5h4PLye7eW_Rz9MM_XpTmgcT6Z6zeMg_nrEtY_FLpBsZvY3nzgfA3-9Q2OAJttpiFIBd6oiPzArcPYEw-9Dkj7u8JpgsmixO8WDLZhJRdy_0h5oZ9fQpcDUYhzaEWUonUA5rDsq2Ibri_TPIK_HEyE5c-Muz3NnLRGgd_iVvEpMqpmKYd6B9NJdtgs0STMQ7DIwVRFIGtXGzcHlzDsNnA11IxWytrjjDbFhevfphg5kQYGo4bJjHyidg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شرکت نفتی آرامکوی عربستان سعودی روز سه‌شنبه اعلام کرد سود خالص این شرکت در سه‌ماهه دوم سال جاری، هم‌زمان با افزایش قیمت انرژی بر اثر جنگ خاورمیانه، ۴۴ درصد رشد کرده است.
بر اساس گزارش مالی آرامکو، سود خالص این شرکت از آوریل تا ژوئن به ۱۲۲ میلیارد و ۶۰۰ میلیون ریال سعودی، معادل ۳۲ میلیارد و ۷۰۰ میلیون دلار، رسید؛ در حالی که این رقم در دوره مشابه سال گذشته ۸۵ میلیارد ریال بود.
امین ناصر، مدیرعامل آرامکو، گفت این شرکت با وجود اختلال بی‌سابقه در عرضه نفت از مسیر تنگه هرمز، توانسته است با استفاده از خط لوله شرق به غرب، ظرفیت‌های ذخیره‌سازی و پایانه‌های صادراتی، فعالیت خود را ادامه دهد.
اعلام افزایش سود آرامکو هم‌زمان با انتقاد دونالد ترامپ، رئیس‌جمهور آمریکا، از سود بالای شرکت‌های نفتی صورت گرفت. او گفت این شرکت‌ها به‌دلیل کمبود نفت ناشی از جنگ «بیش از حد پول درمی‌آورند».
@
VahidHeadline
شرکت بزرگ انرژی بریتانیا، بی‌پی (از بزرگ‌ترین شرکت‌های نفت و گاز جهان)، اعلام کرد سود خالص این شرکت در سه‌ماهه دوم سال ۲۰۲۶، هم‌زمان با افزایش قیمت انرژی در پی جنگ آمریکا و جمهوری اسلامی، بیش از دو برابر شده و به سه میلیارد و ۹۱۰ میلیون دلار رسیده است.
سی‌بی‌اس به نقل از خبرگزاری فرانسه نوشت پنج شرکت بزرگ انرژی غربی، شامل بی‌پی، شورون، اکسون‌موبیل، شل و توتال‌انرژیز، در مجموع نزدیک به ۴۷ میلیارد دلار سود خالص در سه‌ماهه دوم سال ثبت کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77733" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WVLwwX3pGEqyw7I5m_Y3lfVZ146tTobHOvVoMXdxK_x8Yl14YOUoI6aAjoW2N1vBLsclUqG2honwPl1u_Aohkk8pQS5tpu-zLrWocZvjLX47dtD701unZRnM8IRNf4w5rVFof5Y9gs66VpaAqYn8ZCirzy7n6tIScqC7VfTz6VF47xvu3ppvlSya9_Ki0HTI6r3P9HoFmhB-eVITogIl_QP5lZ5_X0W_mXfdlmMa2diEQAJFANuvd_oUk_3B-59I3BiUof-gvq4hPqM1feeoY8mezmJugbiXBWyHY1slZQfOuDmchMPxGUDTP21RioMHDvij4OKs4BDr48XXhR9OsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u2Ypl6-AA5X8iBSID1Yr8RWbQsLwmglAccVn_Xh7nvd654FE1XIEYQK9h9iJoTjEC29RA8KeN27c7ec36l0wCG-fG4Jj13-sgbLHa_Hi80_KfzG_xjHKXrsYI63NfcKNtBIcIq0KZXqTg8519xxtr7TMRFW2fq7QokcM0cyxRqAIpkkdwrrD8iGCermLPW3DDsLV4UaEnJq1cixf_vGfeKTvvmSAT0TkhKT_hxwbRTyyjfFjdik1XozXZYvhB1LcXnCmzlDtC9SvHDMSDdKc4Bge0Tv3uxQMo5tCGMKLEMDQzDvjIoGQ5FoN24537MsF_sdaWXIx2Ndb3oUH1756RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/616a7ca97f.mp4?token=UR3U3XFzTIwhJRme_MsYudko-aVfgUBpO22mVvOQB46QQnIfSE95HHD6itdmCcxFZzn--niwzzpUCxSK_exasJU0tb2UWUZafwhxneFog6oEJHkQIKApnVn1ahGsffmsUgzsSSk4_pzzjNkLFlspsM3bDn6ti5fhThDIZmGu_6GuM3iAIsYyL8sipdFXzSkzRunph53zCxUR4dRJIM1eKivbUw-3NHMJiDgVJIwY09BBnBR3-nUfNKsIv3OHtz2wAQ2YRqWoOlaJE1svsH3rScpwaltsFjU0eAlgD1ItRxHQuR_8zqkTeg-78MwnEGxB7gSgHWTno0yDbAEalSZDBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/616a7ca97f.mp4?token=UR3U3XFzTIwhJRme_MsYudko-aVfgUBpO22mVvOQB46QQnIfSE95HHD6itdmCcxFZzn--niwzzpUCxSK_exasJU0tb2UWUZafwhxneFog6oEJHkQIKApnVn1ahGsffmsUgzsSSk4_pzzjNkLFlspsM3bDn6ti5fhThDIZmGu_6GuM3iAIsYyL8sipdFXzSkzRunph53zCxUR4dRJIM1eKivbUw-3NHMJiDgVJIwY09BBnBR3-nUfNKsIv3OHtz2wAQ2YRqWoOlaJE1svsH3rScpwaltsFjU0eAlgD1ItRxHQuR_8zqkTeg-78MwnEGxB7gSgHWTno0yDbAEalSZDBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در تیزر تبلیغاتی حاوی بخشی از سخنانش که قرار است در چند قسمت و از امشب به وقت محلی از تلویزیون ایران پخش شود، ضمن رد گزارش‌ها درباره استعفایش گفت: «استعفا نخواهم داد و خواهم ایستاد. اینها می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و اینها یک چیزی می‌گویند.»
این سخنان یک روز پس از انتشار کلیپی پربازدید از سخنان محمدباقر خرازی، دبیرکل تشکلی موسوم به «حزب‌الله ایران» که برادر همسر مسعود، برادر مجتبی خامنه‌ای، رهبر سوم جمهوری اسلامی ایران منتشر می‌شود که او درباره «۲۸ بار استعفای پزشکیان» و «تهدید مجتبی خامنه‌ای به پذیرش استعفای بعدی» سخن گفته بود.
این سخنان واکنش‌های چهره‌ها، جریان‌ها و رسانه‌های حامی و منتقد دولت را برانگیخته است؛ از جمله حمید رسایی که از آقای پزشکیان خواسته بود برای راستی‌ازمایی سخنان محمدباقر خرازی استعفا کند.
مجتبی زارعی، نماینده عضو کمیسیون امنیت ملی مجلس ایران در واکنش به طعنه آقای رسایی نوشت: «از ۹۰ میلیون ایرانی فقط یک شاهد برای تهمت خرازی به امام سید مجتبی شهادت داد ؛ سرکرده شریان!»
@
VahidHeadline
حمید رسایی نیم‌ساعت پیش، یعنی پس از انتشار ویدیوی پزشکیان هم تاکید کرد که هنوز تکذیب نشده:
بعد از اینکه سیدمحمدباقر خرازی درباره نحوه برخورد رهبری با استعفای پزشکیان - که تاکنون تکذیب نشده - ادعایی کرد، اطرافیان رئیس جمهور برخوردهای متفاوتی و گاه توهین آمیزی داشتند.
تصور کنید اگر وی ادعایی برخلاف آنچه نقل کرده به زبان آورده بود (مثلا رهبری به پزشکیان گفته شما باید محکم ادامه بدی) چه اتفاقی می افتاد:
rasaee
👈
بعدش، یعنی دقایقی پیش، این خبر منتشر شد:
دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، با انتشار بیانیه‌ای، گزارش‌ها درباره هشدار به مسعود پزشکیان در خصوص استعفا را تکذیب کرد. این بیانیه یک روز پس از انتشار ویدیویی از سخنان خرازی منتشر شد که در آن مدعی شده بود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده و مجتبی خامنه‌ای اعلام کرده در صورت تکرار این اقدام، استعفای او پذیرفته خواهد شد.
@
VahidHeadline
نسخه منابع حکومتی:
دفتر رهبر انقلاب: مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور مطرح کرده از اساس کذب و خلاف واقع است
🔹
متن اطلاعیهٔ روابط‌عمومی دفتر رهبر انقلاب:
بسم‌الله الرحمن الرحیم
🔹
با گرامی‌داشت اربعین حسینی و ادای احترام به روح بلند رهبر شهید انقلاب به‌اطلاع مردم شریف و مبعوث‌شدهٔ ایران می رساند در روزهای گذشته برخی نقل‌قول‌ها از رهبری معظم انقلاب اسلامی در فضای مجازی منتشر شده که متاسفانه زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه است.
بر همین اساس برخی نکات را درباره اخبار و مطالب مربوط به مقام معظم رهبری بیان می‌داریم.
🔹
مرجع رسمی انتشار پیام ها، اخبار و مطالب مرتبط با آیت‌الله سیدمجتبی حسینی خامنه‌ای، پایگاه اطلاع‌رسانی دفتر رهبر انقلاب و یا پایگاه حفظ و نشر آثار رهبر انقلاب است و هرگونه مطالبی که خارج از این چهارچوب منتشر شود، فاقد سندیت و صحت است.
🔹
رهبر معظم انقلاب اسلامی در پیام‌های خود از جمله در پیام اخیر بر حفظ اتحاد مقدس و حفظ حرمت مسئولان دلسوز و خدمتگزاران نظام اسلامی به‌ویژه دولت محترم تأکید داشته‌اند. مطالبی که برخلاف توصیه‌های مؤکد رهبری، موجب انشقاق و دودستگی در جامعه و زمینه‌ساز نسبت‌های نادرست به مسئولان محترم می‌شود، در جهت اهداف بدخواهان و دشمنان قسم‌خوردهٔ ملت ایران است.
🔹
بر همین اساس مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور محترم مطرح کرده از اساس کذب و خلاف واقع است.
روابط عمومی دفتر رهبر انقلاب اسلامی
۱۳ مرداد ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77730" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lleKlR7jb4MAO7Jh4x_YyBMz-y9lFyyggEw7jbSGZvl00O76NIbU2nYev8lLGEQErV-ZVBb0z8YR9zq9ttZloEFyZHpUkgxedcI_Cl7hT8ISxJbEljJhHH_yE13wtsCBFSVX0iAvzt_JgvByZSwPTfzqqd2VoRh0mA0Z26nu6A4xLSHdNLXDDMyN_DHQ6SoQTsrcg6CIRUjYVxgPLxyddv6YwWVpcG59XTtDsNY_7pKrC4EIhlRfZmeR9xJutxvNbhO_7CL0G7WlzAeztlOUOe-mzllCRWZ4NiG77sHoP8FGX4cBk-iRV7jKBEBlkfCT_gNY53WPR0P6TdeuSOyRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساکنان شماری از روستاهای جزیره قشم حدود چهار ماه است به آب لوله‌کشی دسترسی ندارند و برای تامین آب مورد نیاز خود ناچار به خرید تانکرهای چندمیلیون‌تومانی یا استفاده از منابع نامطمئن شده‌اند.
براساس گزارش میدانی آوش، یکی از ساکنان روستای طبل گفته است: «چهار ماه است شیر آب خانه‌مان باز نشده. حالا فقط با تانکر زندگی می‌کنیم. من توانستم سه میلیون تومان بدهم و آب بخرم، اما خیلی از روستایی‌ها حتی همین پول را هم ندارند.»
پس از آسیب‌دیدن یکی از تاسیسات آب‌شیرین‌کن در جریان حملات ماه‌های گذشته آمریکا به نوار جنوبی ایران، وضعیت تامین آب در بخش‌هایی از جزیره به‌شدت بحرانی شده است. او گفته آب لوله‌کشی تقریبا قطع شده و مقدار آبی که با تانکر توزیع می‌شود نیز پاسخ‌گوی نیاز ساکنان نیست.
این اظهارات در حالی مطرح شده‌اند که عباس علی‌آبادی، وزیر نیرو، ۲۹تیر۱۴۰۵ و در جریان سفر به هرمزگان گفته بود همه آب‌شیرین‌کن‌های منطقه در مدار بهره‌برداری قرار دارند وهیچ‌یک از جزایر کشور با کمبود آب مواجه نیست.
او همچنین گفته بود با وجود آسیب‌دیدن زیرساخت‌ها در حملات اخیر، خدمات آب و برق پایدار مانده و شرایط مدیریت شده است.
عبدالرحیم رضوانی، نایب‌رییس شورای اسلامی بخش مرکزی قشم  گفته است ساکنان برخی روستاها بیش از سه ماه برای وصل‌شدن آب انتظار می‌کشند و پس از آن نیز تنها چند روز به آب شبکه دسترسی دارند. به گفته رضوانی، قیمت یک تانکر چهار هزار لیتری آب به حدود یک میلیون و ۴۰۰ هزار تومان رسیده است.
در همین حال، یکی از ساکنان قشم گفته است برخی خانواده‌ها که توانایی خرید آب ندارند، برای مصارف روزمره از چاه‌هایی استفاده می‌کنند که از سالم‌بودن آب آن‌ها اطمینان ندارند. او به نقل از یکی از اهالی گفته است: «آب تمیزی نیست؛ حتی حیوان داخل آن می‌میرد، اما به‌هرحال آب شیرین است. برای خوردن استفاده نمی‌کنیم، اما برای کارهای روزمره مجبوریم همین آب را به خانه ببریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77729" target="_blank">📅 18:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77728">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPu0_okFZiOcGJ6-LYpoHVZWjgH3EMU24ZIgpSHQ_YEdzUpj95jhXlJTrXFaUR_z0aJlVDgMeWFA5pv8IJFnGnchz4O0Ep6nOAzg2PxHMZOv6vbsxnb_kLM6IY_8AnvyKfYVQ-UhEQ4HZbGD1xGt1O2YGAd9nuBT8Iq9ccCMWI9M1XDijNtgeCdss1lZ2RNS9Sf4BjxNm92XEY73UtEuQVpCpJMZ1j-f-sNULJUAhq0NIx8wUHIMwiY35vT6Cn-GAxowj1dwXkjg5bQntzH5EhfKLB3j13IiankF9QkVmLxm7YUhaLijakdL5mr_XjLvGoaLxByxP1BT4B9NBNe0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه موج پلمپ واحدهای صنفی و مراکز فرهنگی در ایران، در روزهای اخیر، دست‌کم سه مجموعه فرهنگی و صنفی در بابل، مشهد و تهران با دستور مقام‌های قضایی یا نهادهای ناظر پلمب شده‌اند.
هرانا خبر داد مجموعه «شهر کتاب» در شهرستان بابل، با دستور قضایی و به‌دست اداره نظارت بر اماکن عمومی پلمب شده است.
هم‌زمان، گزارش‌ها از پلمپ «کافه معماری سکنج» در مشهد حکایت دارند؛ فضایی تخصصی و فرهنگی که محل فعالیت معماران، هنرمندان و دانشجویان بود. تاکنون درباره علت پلمپ این کافه اطلاعاتی منتشر نشده است.
مجموعه «خانه ارغوان» نیز اعلام کرده است که به‌دلیل «پلمب موقت از سوی مراجع ذی‌ربط»، فعالیت خود را تا رفع محدودیت‌ها متوقف می‌کند. این مجموعه در خیابان فرشته تهران فعالیت داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77728" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IY3qT5AWhMCgD1AdKuP5xqAbLdcBf7DE1Fr5aCthkrh-WJlZBjRw5gHIlMfMVJ0da-bQBioH_tht0yChZhauptZPqvKpstGMgGwAJQJE_SLNPVABRTq2lnG8PXoNb_V_dliqmZWOdnwpSQiWEQLMRnAd7qYNqfS0iD12QBlTAp-OxS5vIMSvG4oa20WVKky9LM6Is6QktOyAHSTPTTNr3WVG5PP59G9EKxmY9u-vtSjdgYtutrpAbB00T7cqo9b8QLzSs6DHLsl-_d4G8knKcY67c2v5CQSriV2QF4iGhd57FH9JdqLl4RbCtE-rd0P0SYGrxa52fcNqTv8pQHoAUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سازمان حقوق بشر ایران» اعلام کرد «مهدی روشنی»، معترض بازداشت‌شده در ارتباط با اعتراضات ۱۶دی‌۱۴۰۴ در شهرستان ملکشاهی، با اتهام‌های امنیتی به اعدام محکوم شده است.
این سازمان روز دوشنبه ۱۲مرداد۱۴۰۵ گزارش داد مهدی روشنی روز یکم بهمن‌ماه در منزل خود بازداشت و به تهران منتقل شد. به نوشته سازمان حقوق بشر ایران، او پس از بازداشت، دو ماه در بی‌خبری مطلق نگهداری شد و برای گرفتن اعترافات اجباری تحت شکنجه‌های شدید قرار گرفت؛ اعترافاتی که به گفته این سازمان، مبنای صدور حکم اعدام قرار گرفته است.
سازمان حقوق بشر ایران به نقل از یک منبع مطلع مدعی شده که یکی از افرادی که مهدی روشنی را پس از بازگشت از تهران دیده، آثار گسترده شکنجه را بر بدن او مشاهده کرده بود.
این فرد گفته است: «اگر بدنش را می‌دیدید وحشت می‌کردید. جای سالمی روی آن نبود. پر بود از آثار شوک الکتریکی و شلاق، اما حاضر نشده بود اعتراف کند.»
بر اساس این گزارش، مهدی روشنی اواخر اردیبهشت‌ماه ۱۴۰۵ با تودیع وثیقه آزاد شده بود، اما حدود دو هفته بعد بار دیگر نیروهای امنیتی او را بازداشت کردند و از آن زمان تاکنون در بی‌خبری مطلق به سر می‌برد.
این منبع همچنین گفته است خانواده مهدی روشنی تحت فشار قرار گرفته‌اند و به آنها هشدار داده شده درباره پرونده او سکوت کنند. به گفته این منبع، حدود یک ماه پیش به خانواده او اطلاع داده شده که وی با اتهام‌هایی از جمله قتل «احسان آقاجانی»، مامور پلیس، به اعدام محکوم شده است.
بر اساس گزارش‌های منتشر شده، احسان آقاجانی در جریان اعتراضات ۱۶دی‌ماه در شهرستان ملکشاهی کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77727" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahb3u1sbOqFn4z6m6annwrT-pjT-gWjuYSfRR1OoJilsyb_esBNkJWsK2-xasczuodCZySp7lkp7ba2i6Jo8IKlHN4NRo0o3qZjlCMTWrzIhcaqG_Kp3Lw0_ONo19iDmYjMeb7KjoCWlBSnyxY2CA3NQxbnqwnqIBoVPwCwmQjKFaRkNoZj16f3QB6xGITOhq5TcrzyoNsKDuygainqxtvi0I7k7ohlay362X7L6zeX448DvncPYYBwDFOzGSJXhRgGHdLZQ1S9nf7wA03RyWXcalAB9CK9L38B_RI6re_U4ylgLd6QbXCxRspmc8lLQmS_WuGZY97Jk1B6KmKZIng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
آپدیت: برگشت
پیش از آپدیت:
نرم‌افزار پیام‌رسان «تلگرام»، روز دوشنبه، به‌طور ناگهانی از فروشگاه «اپ‌استور» شرکت اپل در سراسر جهان حذف شد.
بر اساس اعلام کاربران شبکه‌های اجتماعی، جست‌وجوی نام تلگرام در اپ‌استور با هیچ نتیجه‌ای همراه نیست و
صفحات رسمی دانلود
این برنامه با «خطای ۴۰۴» مواجه می‌شوند.
اگرچه این پیام‌رسان روی دستگاه‌هایی که از قبل آن را نصب داشته‌اند کماکان بدون مشکل کار می‌کند، اما امکان
دانلود تازه
یا نصب مجدد آن روی آیفون و آیپد فعلا وجود ندارد.
تاکنون هیچ‌یک از شرکت‌های اپل یا تلگرام بیانیه رسمی درباره دلایل این تصمیم صادر نکرده‌اند و مشخص نیست که این اقدام دائم است یا موقت و آیا ناشی از بررسی‌های قانونی و محتوایی است یا یک نقص فنی.
پیش از این نیز در سال ۲۰۱۸ اپل برای مدتی کوتاه تلگرام را به دلیل «نگرانی از انتشار برخی محتواهای خلاف قوانین» از اپ‌استور خارج کرده بود که پس از اعمال اصلاحات لازم، این برنامه مجددا بازگشت.
@
VahidOOnLine
🔄
و آپدیت چند ساعت بعد:
شرکت اپل اعلام کرد پس از آنکه در یک بررسی مشخص شد محتوایی مغایر با قوانین این شرکت در رابطه با «ممنوعیت سوءاستفاده جنسی از کودکان» در تلگرام قرار گرفته، این پیام‌رسان را به‌طور موقت از «اپ‌استور»، فروشگاه نرم‌افزاری اپل حذف کرده است.
به گفته اپل، پس از آنکه تلگرام «محتوای متخلف را به‌سرعت حذف و حساب کاربری منتشرکننده را مسدود کرد»،  دوباره به اپ‌استور بازگردانده شد.
تلگرام نیز در واکنش به گزارش‌ها درباره حذف این پیام‌رسان، در شبکه‌ اجتماعی ایکس نوشت: «گزارش‌های مرگ من بسیار اغراق‌آمیز است.»
@
VahidOOnLine
🔄
پست پاول دورف، مدیرعامل تلگرام درباره این موضوع، ترجمه ماشین:
🍎
دیشب، اپل برای مدت کوتاهی تلگرام را از اپ استور حذف کرد، زیرا یک کاربر به‌تنهایی محتوای پورنوگرافیک غیرقانونی را در یک گفت‌وگوی گروهی عمومی جاسازی کرده بود.
⬅️
تلگرام ظرف چند ساعت دوباره در دسترس قرار گرفت. اما می‌خواهم توضیح بدهم چه اتفاقی افتاد؛ هم برای هشدار دادن به دیگر توسعه‌دهندگان اپلیکیشن‌ها و هم برای کمک به محافظت از جوامع آنلاین در برابر حملات مشابه.
🧹
از آنجا که تلگرام با استفاده از گزارش‌های کاربران، فیلترهای هوش مصنوعی، هش‌های محتوا و دیگر ابزارهای نظارتی، محتوای غیرقانونی را به‌سرعت از گروه‌های عمومی حذف می‌کند، مهاجم ناچار شد به یک ترفند فنی متوسل شود. او با ویرایش یک پیام قدیمی در یک گروه فعال، محتوای غیرقانونیِ تغییریافته با هوش مصنوعی را در آن قرار داد. در نتیجه، این محتوا عملاً از دید اعضای گروه پنهان ماند و آن‌ها نتوانستند آن را ببینند و فوراً گزارش کنند.
💰
مهاجم یک «باج‌گیرِ حذف محتوا» بود؛ کسی که از صاحبان گروه‌ها باج می‌خواهد و در ازای آن، جوامعشان را هدف قرار نمی‌دهد. این باج‌گیران با استفاده از حساب‌های خودکار، محتوای غیرقانونی را در گروه‌های عمومی قرار می‌دهند و سپس مستقیماً آن را به اپل گزارش می‌کنند تا باعث حذف جوامع مشروعی شوند که صاحبانشان از پرداخت باج خودداری کرده‌اند.
🤝
از نظر عملی، محتوای پورنوگرافیک غیرقانونی در گروه‌های عمومی تلگرام یک مشکل نظام‌مند نیست. نظارت ما مؤثر است (
https://telegram.org/safety
). همین که مهاجمان ناچارند به محتوای دارای تاریخ گذشته و عملاً نامرئی و دیگر ترفندهای فنی متوسل شوند، این موضوع را ثابت می‌کند.
⚠️
با این حال، دو درس مهم برای توسعه‌دهندگان اپلیکیشن‌ها و جوامع آنلاین وجود دارد:
— باج‌گیران راهی پیدا کرده‌اند تا اپل را وادار به واکنش افراطی کنند. اپل پیش از تماس با ما، تلگرام را از اپ استور حذف کرد. این موضوع برای هر اپلیکیشن موبایلی که میزبان محتوای تولیدشده توسط کاربران است، یک خطر بالقوه و نظام‌مند ایجاد می‌کند. اگر اپلیکیشنی که بیش از یک میلیارد نفر از آن استفاده می‌کنند بتواند بدون هشدار قبلی از اپ استور حذف شود، هر اپلیکیشنی ممکن است حذف شود.
— تاکتیک‌های مورد استفاده باج‌گیرانِ حذف محتوا در حال تکامل است و جوامع در سراسر پلتفرم‌های اجتماعی را در معرض خطر قرار می‌دهد. تلگرام تجربه گسترده‌ای در شناسایی ترفندهای باندهای هماهنگِ گزارش‌دهی و محافظت از جوامع مشروع دارد؛ حتی وقتی این کار خطر حذف موقت خود اپلیکیشن ما از اپ استور را به همراه داشته باشد. ممکن است دیگر پلتفرم‌ها به همین اندازه آماده نباشند.
هوشیار بمانید!
☝️
durov
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/77726" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H2HYEYdAuHYxafqhPe54fqGMYvrBqmFqIxrf3o8_BIrs0vR_20zF4Bb6X-3UwHepPKxZum9CX9xwr-7Z7zJMyhfqEcfbrwtVONFpS52plnE-uzSVMsN8lqEfm83YDKbgXgTmbvskuwNwsiWJ81hVz9Lq-FWbAu3y0rTtRFDsAbnTvfCy_hhYD7IcfJ2D4OrFS5XFyuVdULzC__QlzHI1kSH_QiJJeccdxjNyJJhSg-bqoBN84OpxpGvWZNGSY0oRo7fjw_0Rqo17hJn4bxjrlNJLvLNnl-duAf0yHfIq-G8RUdfKX5n1BXNNkYFR0r9pLvAhOgt5OUEI3ANY6t1pgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)  گزارشی درباره وقوع یک حادثه در ۲۰ مایل دریایی شمال‌شرق الخصب در عمان دریافت کرده است.
یک کشتی باری از طریق کانال ۱۶ بی‌سیم VHF اعلام کرده است که با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
مقامات در حال بررسی هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77725" target="_blank">📅 03:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuzumYA7GLA-SQckJWZ6P8noM6ERGWa50btio20KmBMn3SZsH12t_IlSYCd7Nzh8zh7n39jByc2XwrN9hSiV9kTHMcUxBtTHp7YymjK3PllMScsXfuY5ANIOfQYuSpf0lw6rNktbMMKb5AehDGVhJXIdUnJ-ZXV42A3use1BEUWX1JGRVggBPLoYPZ-vrIWlpLhTcJVLHPU-eW552V3iiBI11hkto3i0CRJb6Ga4rtu5B6Y0KND8SqnzveAmo-PD3JGirORJGUbZfQjPEz_bG8k9GOIOs8ZE7SBnikWT6k19zo2Jz2UjvCE7LFDJyrcm1pGJENk9Z8j0GDv86iF90QXU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuzumYA7GLA-SQckJWZ6P8noM6ERGWa50btio20KmBMn3SZsH12t_IlSYCd7Nzh8zh7n39jByc2XwrN9hSiV9kTHMcUxBtTHp7YymjK3PllMScsXfuY5ANIOfQYuSpf0lw6rNktbMMKb5AehDGVhJXIdUnJ-ZXV42A3use1BEUWX1JGRVggBPLoYPZ-vrIWlpLhTcJVLHPU-eW552V3iiBI11hkto3i0CRJb6Ga4rtu5B6Y0KND8SqnzveAmo-PD3JGirORJGUbZfQjPEz_bG8k9GOIOs8ZE7SBnikWT6k19zo2Jz2UjvCE7LFDJyrcm1pGJENk9Z8j0GDv86iF90QXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مربوط به ایران
متن مکالمه با تشخیص و ترجمه ماشین
:
به دلایلی، وقتی در حال مذاکره‌اند، دوست ندارند بگویند که دارند مذاکره می‌کنند. من می‌گویم: «صبر کنید، ما در حال مذاکره‌ایم. چه اهمیتی دارد؟ داریم مذاکره می‌کنیم.» و آن‌ها گاهی آن را انکار می‌کنند، با اینکه ساعت‌ها و ساعت‌ها کنار یکدیگر می‌نشینند و مذاکره می‌کنند.
مذاکرات در حال پیشرفت است.
قرار بود دیروز آن‌ها را به‌شدت هدف قرار دهیم؛ بسیار بسیار شدید. حمله‌ای شدیدتر از هر حمله دیگری.
فکر می‌کنم می‌توانم بگویم—و ژنرال‌ها از روی آگاهی می‌گویند—شدیدتر از هر حمله‌ای از زمان جنگ جهانی دوم تاکنون. این خیلی بزرگ است.
ما آماده اجرای حمله بودیم که آن‌ها تماس گرفتند. علاوه بر آن، عربستان سعودی تماس گرفت، امارات تماس گرفت، قطر تماس گرفت و افراد بسیاری با من تماس گرفتند. نمی‌خواهم از کلمه «التماس» استفاده کنم، اما به‌ویژه ایران نمی‌خواست هدف حمله قرار بگیرد.
آن‌ها گفتند: «می‌خواهیم مذاکره کنیم. می‌خواهیم درباره تنگه مذاکره کنیم.» اما از دیدگاه من مهم‌تر از آن، می‌خواهیم درباره هسته‌ای‌زدایی ایران مذاکره کنیم، زیرا اصل ماجرا همین است. دلیل اینکه این کار را انجام می‌دهم همین است.
این کار باید مدت‌ها پیش انجام می‌شد. اکنون ۵۰ سال شده است. همیشه می‌گفتیم ۴۷ سال، اما سه سال دیگر نیز گذشته است. ۵۰ سال است که رؤسای‌جمهور دیگر باید کاری را که من انجام می‌دهم، انجام می‌دادند. یا کشورهای دیگر؛ لازم نبود حتماً ما باشیم، اما کشورهای دیگر باید این کار را می‌کردند. هیچ‌کس انجامش نداد و زمان آن فرا رسیده بود.
ما درباره تنگه صحبت می‌کنیم؛ بازشدن تنگه و اینکه به معنای واقعی کلمه تا فردا کاملاً باز باشد. این مرحله اول است.
مرحله دوم این است که پس از آن درباره موضوع هسته‌ای  صحبت کنیم. اساساً هسته‌ای‌زدایی ایران باید انجام شود. باید انجام شود. این مرحله دوم خواهد بود.
اما
مرحله نخست، بازشدن تنگه است. مرحله دوم هسته‌ای‌زدایی خواهد بود. آن مرحله کمی زمان می‌برد، اما ما در این زمینه بسیار قاطع هستیم.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من هرگز موضعم را در این‌باره تغییر نداده‌ام.
درباره کشتیرانی در تنگه هرمز: من اجازه نمی‌دهم از کسی پول بگیرند. ما طرفی هستیم که کنترل کامل را در اختیار دارد. ما کنترل کامل داریم.
می‌دانید، چیزی به نام محاصره داریم که با این نیروی دریایی اجرا می‌شود و به آن «دیوار فولادین» می‌گویند؛ «دیوار فولادین ایالات متحده».
نه، نه، هیچ پولی گرفته نخواهد شد. اصلاً درباره گرفتن پول صحبت نمی‌کنیم. پولی گرفته نخواهد شد.
فکر می‌کنم به این واقعیت بسیار افتخار می‌کنم که به مردم فرصت می‌دهم. به مردم فرصت خواهم داد. انجام حمله‌ای به آن بزرگی علیه یک کشور، تصمیم بسیار بزرگی است. ترجیح می‌دهم اکنون آن را انجام ندهم.
امیدوارم سر عقل بیایند
قرار بود حمله دیشب آغاز شود و مدت زیادی ادامه پیدا کند و در نهایت عملاً چیز بسیار کمی باقی بماند؛ هیچ‌چیز باقی نمی‌ماند.
اگر این فرصت به من داده شود که اجازه دهم افراد زیادی زنده بمانند، می‌خواهم آن فرصت را به آن‌ها بدهم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/77724" target="_blank">📅 23:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LGE7YLgteWEquWOB6oN2EJWg42XiB7rKqVDbzKFDuhoT6jX-_0TtUiSfiS9OKO7dToPbNa2ItW4jhDcheLihzDtredmHAHDBWAsxqenNgm1dD_bzhexwi4Cy8KlbAp7hq41lFCFU6oDCM1dDr7dxg-wUxUUm66UHiFQVilMoiuCWkNZMPdmKR6KGEqSdj6GBXB2A9HtobupG8PwLQ4DSgQOmdGTeiGwsXPq4o_8RcN_75YTzVXU-YiLU7t9Mkf-6oZQVQl49DH8UUXk8ogv3-ksD5J2qK-O_RNUv7LD7urNwsxcHrMkneQafYudiu3qz8S_xZseCqE3yNbQHMCtb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه ۱۲ مرداد در حاشیه نشستی در کاخ سفید، به خبرنگاران گفت مذاکراتی که در حال حاضر با جمهوری اسلامی ایران جریان دارد، «آخرین فرصت» تهران برای امضای یک «توافق خوب» است.
ترامپ که پیش‌تر حمله‌ای که به گفته او «بزرگ‌ترین حمله نظامی از زمان جنگ جهانی دوم تا کنون» بود علیه ایران را لغو کرده بود، با انتقاد دوباره از مقام‌های جمهوری اسلامی که انجام مذاکره با ایالات متحده را تکذیب کرده بودند، گفت: «ایرانی‌ها تماس گرفتند، بعد از آن از عربستان سعودی، قطر، امارات و بسیاری کشورهای دیگر با من تماس گرفتند که یک فرصت دیگر بدهم. نمی‌خواهم بگویم «التماس» کردند ولی ایران واقعا نمی‌خواست مورد حمله قرار بگیرد.»
ترامپ تاکید کرد که این مذاکرات «با درخواست ایران» و حمایت کشورهای منطقه و جهان انجام می‌شود و «آخرین فرصت» برای جمهوری اسلامی است که انتظارات او درباره برنامه هسته‌ای را برآورده کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77723" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JNUCZqiF4O3mRb_k5I-3HtRoiCp1sXU9DkQvKMcXDNx3ZQZM90fT00bEWL3jAV5RpcmzBgnt-pOdzdqtbYweQpq-ET8KN4Sk-ulHgmjOfCKewBtx-xzSRYbA54KiWimBKsHwbQAcIUXQEyrLbICFm34XZes6FSc00JrjuaexyD3UgicCsZbjQjwvi6EILGNGkGfeMscU6VpybftalLFTa3XsseqWweCAF3derutturycK6PC0i9o38LXNWrH9tsVSTHQ22tn229yaFilbuqhIsU8CWiXgVBVcV9CbYvO9Ac52CQAWED8t8D1IzP_d8_OXm400B7myo2rXELnSzo90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رهبری ایران به‌طرز باورنکردنی دورو است!
آن‌ها درخواست جلسه می‌کنند ــ بعضی‌ها می‌گویند «التماس می‌کنند» ــ مذاکرات آغاز می‌شود و جلسات بیشتری نیز برای آینده بسیار نزدیک برنامه‌ریزی می‌شود، اما بعد آشکارا و با افتخار می‌گویند که هیچ گفت‌وگویی ندارند، درباره هیچ‌چیز صحبت نمی‌شود و فقط با «عمان» سروکار دارند.
سپس همان یاوه‌گویی‌های همیشگی‌شان را ادامه می‌دهند و می‌گویند تنگه هرمز با قدرت توسط آن‌ها اداره خواهد شد، در حالی که این تنگه همین حالا نیز کاملاً تحت کنترل نیروی دریایی ایالات متحده و «محاصره» ما قرار دارد؛ یا همان‌طور که بعضی‌ها می‌گویند، «دیوار فولادین ایالات متحده»!
هیچ‌چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ‌چیز نیز نخواهد رسید، مگر آنکه توافقی حاصل شود یا تسلیم کامل صورت بگیرد. چه ایران بخواهد این را بپذیرد و چه نخواهد، ما در واقع در حال گفت‌وگو درباره راه‌حلی برای مشکلی هستیم که آن‌ها طی چندین دهه ایجاد کرده‌اند.
موضوع بسیار ساده است: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77722" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t18ANSOZToi98lyKeVliXo8xfsmV4At8yz3DFNbsGxvRUFAPF2FysasBybUJqMqDPtirkKTSckqwzh185LVx-5B9waIPBz6_Zzq7ADOS5rn0JnFMleisXGROmAdND6z0o1o1kwTOP8PxgVRHqEacinDP64pM9tkq29duyieWeXp93WS3aFIU_6biPgPQf5gFqUui9HdKCVo71U_AIaafXZ5HXkDyepj-L2m0xqfCqw0c7vlonle2ktc5XlGGD2GVsUBdh5_V30dhNU064AhDA483zLQuYlXWfh649u5mlzz_6Zx7gCSIWczDClMKBHMv9vcZCuwmOQh4a85bw4GX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیران امور خارجه جمهوری اسلامی ایران و پاکستان در گفت‌وگویی تلفنی درباره تحولات منطقه‌ای و روند تحرکات دیپلماتیک رایزنی کردند. در این تماس، محمد اسحاق دار، وزیر امور خارجه پاکستان، از عباس عراقچی برای سفر به اسلام‌آباد در نخستین فرصت دعوت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77721" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL1sDiY5s58UJJ7r1JJ8XmFIjlCLln46nO4BsuBGRUfWZjGjL6z-CJDbCgN8jPVNE1H7MJX8lE6-ISs7zAHKzWUvnKk4hyqL1AiQf6-taaA-qoPBKsu-ne37r-sW5jrBnljNQuLQ7d2HqMazkyENVk-y2g_MCCl2MP6rvV61Q3YLZYlCjwheEf7teUu3wccIKWgNxXtL6uTlZFgZ8EBVDz1qjOStsbkkPDvrYs2H8jIYXjnYVhhvZPHYeECPhaRdrTxp3q5Mx1Y4aiJhWmJSUHkyZocHkHfb7HaJzpL84qb3W4zx8Cee9jTmDm-WFKpmiA_BoqbaXJc15Iau-kBSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا روز دوشنبه ۱۲ مرداد بار دیگر از شرکت‌های نفتی خواست قیمت بنزین را برای مصرف‌کنندگان آمریکایی کاهش دهند و مایک ویرث، مدیرعامل شورون، را به‌دلیل قدردانی نکردن از تلاش‌های دولتش در حمایت از صنعت نفت مورد انتقاد قرار داد.
دونالد ترامپ در یک مصاحبه تلویزیونی، ویرث را سرزنش کرد که به نقش دولت او در کمک به شرکت‌های نفتی اشاره نکرده است.
او در پیامی در شبکه اجتماعی خود، تروث سوشال، نوشت: «تنها چیزی که او به‌راحتی از گفتنش صرف‌نظر کرد این است که بدون نبوغ، دوراندیشی، قدرت و ثبات دولت ترامپ، صنعت نفت و حتی خود کشور ما نابود می‌شد!»
ترامپ افزود: «برای مثال، آن‌ها مایک و شورون را از ونزوئلا بیرون کردند، اما حالا بازگشته‌اند، بزرگ‌تر و قدرتمندتر از همیشه، و انتظار دارند ثروت هنگفتی به دست آورند!»
به گفته ترامپ، «این موضوع شامل سایر شرکت‌های نفتی هم می‌شود... و همین حالا قیمت نفت برای مصرف‌کننده را پایین بیاورید!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77720" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
