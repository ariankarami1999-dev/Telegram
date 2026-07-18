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
<img src="https://cdn4.telesco.pe/file/MMiBcX7SbWP4nLRHFmLrq9qswXnoneZZhpvw8kfiwCd5jiBhwP2m_lyXnuPZeBBA-aYPtMpdcw4JaiiVLdvCO17bdBRZVLDJ1X1eV2h7EruB7aXrHqHc-RHYGaJLjBx7VQKk12W8jLbSW4A1OchjzjK-t9VB8Bwgxf_onNWexUypb4ZStaZR1OgLA69xlOiYG9m8ds8O6e1-9zo3kRMUhQmJurGlNoScaUNts7p0w6TySmf9Mpi5gGlgE0I4drUvBepwK7cQf9IpNIM26SfD6p7WUxQxRj5PNkJGCxwqV0pEBjWlxCJRElNAumsB0JcdvWI5AqXnUGAMd9I7V_NOKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 10:24:21</div>
<hr>

<div class="tg-post" id="msg-450816">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">توجیه وزیر خارجهٔ اردن برای وجود پایگاه‌های آمریکایی در این کشور
🔹
ایمن الصفدی: آمریکا هیچ پایگاهی در اردن ندارد اما سربازان آمریکایی در چارچوب همکاری‌های نظامی میان امان و واشنگتن در کشور ما حضور دارند. @Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/450816" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450815">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
وزارت دفاع بحرین از حملهٔ موشکی به این کشور خبر داد و طبق معمول مدعی «رهگیری حملات هوایی ایران» شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/450815" target="_blank">📅 09:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450814">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تعویق آزمون‌های نهایی ۴ استان جنوبی در ۲ روز
🔹
ستاد عالی آزمون‌های وزارت آموزش‌وپرورش: امتحانات نهایی پایه‌های یازدهم و دوازدهم در استان‌های هرمزگان، بوشهر، خوزستان و سیستان‌وبلوچستان در روزهای ۲۸ و ۲۹ تیر لغو و زمان برگزاری آن متعاقباً اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/450814" target="_blank">📅 09:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450813">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌
🔴
آژیرهای خطر باز هم در کویت فعال شد
🔹
منابع خبری گزارش دادند پایگاه‌های آمریکا در کویت هدف حملات ترکیبی موشکی و پهپادی قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/450813" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450812">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فرمانداری دزفول: به‌دلیل انجام عملیات انهدام مهمات، احتمال شنیده‌شدن صدای انفجار از ساعت ۱۰ صبح امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/450812" target="_blank">📅 09:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450809">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMN9eNkee14zukAu1Y8iuNti-m6pucN3xzfHjn5LvLF6_v6oYbHuqCRBw0DI2ZEN-XcKXNIoUvz5Mt2nueNPloxV7p8y1-qkrKxxE4c9I0YNN3978zjZ36kTeyLrTVUCxr6qp5zoTsBKJF7iBG8xdYrXNJbKKb5WmZkoD0XG5245oWfHJOZMU05oWJuhsLFdHoZJOV99EIdvTTWTZHryWe9_uoVwhUJuIb3esxzqWHZ7GARDuG1VwG9O48B3ZgAWLh7v3wVVdOw97HPD74nJPhETpvj8StM9OHXrKBgvFLbmWUt9lfhxhAFyeB4OWKuYrr01RdhjDZ1EeMAxv5ipyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQmcsZ0Sv1POB40gRKn57FMkbxsg3r7sAe9CN0dy9dvsxLftf87XcTVQ2FdmYa-h57dQw1l_HwbeblSOBNUT4J5azSn11pSzX4LNT4MfjoYkDvfBJFXezK3aAPRcp9T1Gsab3rC3LFFn4-1gQ1xo7LjImIPwQvpj4jyGsNh852XBA1GrDZ1VuKFe6LIl66QzvMU0edzwPfSkRsBQX7IRJ09Lx5gJ6_trTglVFpDI-OYIgVffQAh0DL1pu_Jl4rKHGrBZ3tHhCeOTUaJDLrK9l9W6uN8rupEBSDlAIUC1HSoh5sudUcM6ZMKOwdXmx6Lh2KW7NtGpNOL2vUYV5Z2jyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8181cca6e3.mp4?token=nCLdM84gMUHgfC78l9C_sG9-aIym9Uvgotc68WNsAvlWbPoVo44ugdULmvHSirZFDgdK2ot8tp0r0HBE0tQQjN9sdRpJDNqjKJL2F_Snr1315Oid8Cn4ury1wezPod1r56Gtuv9AJK0khkL1yDOire84qx7qrojFgoeN-xQtvhzNqTEiS2UvIZSlaPxu4qTDLHZyQs3suc2_LyGRUFub2FPOPg717OeZO30s2aoxpIEtogjajpoYoUwsE9-BSiB_Mg2QTG-_nUMlAbw5y3lQccs_MRB5kc1grB3GZtphxDqS2BMb42_irfbfI2Gu4txNXP3jv8uuz7U0YJz3ips-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8181cca6e3.mp4?token=nCLdM84gMUHgfC78l9C_sG9-aIym9Uvgotc68WNsAvlWbPoVo44ugdULmvHSirZFDgdK2ot8tp0r0HBE0tQQjN9sdRpJDNqjKJL2F_Snr1315Oid8Cn4ury1wezPod1r56Gtuv9AJK0khkL1yDOire84qx7qrojFgoeN-xQtvhzNqTEiS2UvIZSlaPxu4qTDLHZyQs3suc2_LyGRUFub2FPOPg717OeZO30s2aoxpIEtogjajpoYoUwsE9-BSiB_Mg2QTG-_nUMlAbw5y3lQccs_MRB5kc1grB3GZtphxDqS2BMb42_irfbfI2Gu4txNXP3jv8uuz7U0YJz3ips-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انبار نفتی مسکو در حمله پهپادی اوکراین به آتش کشیده شد
🔹
ارتش اوکراین در ادامهٔ حملات پهپادی به روسیه، دیشب زیرساخت‌ انرژی در مسکو را هدف قرار داد. رسانه‌های اوکراینی خبر دادند که در این حملات پهپادی، انبار نفتی پایتخت روسیه آتش گرفت.
🔹
تصاویر منتشرشده در رسانه‌ها نشان می‌دهد که دود سیاه غلیظی از یک انبار نفت در شهر نوگینسک(واقع در ۵۰ کیلومتری شرق کرملین) بلند شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/450809" target="_blank">📅 09:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450808">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
منابع خبری از وقوع چند انفجار در کویت خبر دادند و آژیرهای خطر در مناطق مختلف این کشور به‌صدا درآمد
🔹
این منابع از اصابت موشک و پهپاد به مقرهای آمریکا در کویت خبر دادند. ارتش کویت هم مدعی شد که درحال «رهگیری موشک‌ها و پهپادهای ایران» است. @Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/450808" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450807">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
منابع خبری از وقوع چند انفجار در کویت خبر دادند و آژیرهای خطر در مناطق مختلف این کشور به‌صدا درآمد
🔹
این منابع از اصابت موشک و پهپاد به مقرهای آمریکا در کویت خبر دادند. ارتش کویت هم مدعی شد که درحال «رهگیری موشک‌ها و پهپادهای ایران» است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450807" target="_blank">📅 08:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450806">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
سپاه: اسکلهٔ پشتیبانی سوخت ناوگان آمریکا، محل تجمع پرنده‌های جنگی، مرکز داده‌های اطلاعاتی و یک مرکز سیگنالی و مخابراتی آمریکا درهم کوبیده شد
🔹
روابط‌عمومی سپاه پاسداران انقلاب اسلامی: مردم قهرمان و با ایمان ایران! دریادلان غیور نیروی دریایی سپاه در امتداد حضور حماسی شما ملت بزرگوار در خیابان میدان رزم را هم به صحنهٔ نمایش عجز دشمن جنایتکار تبدیل کردند و علاوه بر کنترل قدرتمندانهٔ تنگهٔ هرمز، در موج ۱۹ عملیات نصر۲ در پاسخ به تجاوزات دیشب ارتش کودک‌کش آمریکا، اسکلهٔ پشتیبانی سوخت ناوگان آمریکا در بندر الاحمدی کویت و محل تجمع پرنده‌های جنگی دشمن در پایشگاه «شیخ عیسی» بحرین را هدف عملیات کوبندهٔ پهپادی و موشکی خود قرار دادند و مرکز داده‌های اطلاعاتی دشمن در بحرین با عنوان باتلکو را در هم کوبیدند.
🔹
رزمندگان نیروی دریایی همچنین یک مرکز سیگنالی و مخابراتی آمریکا در کویت را منهدم کردند.
و ما النصر الا من عند الله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/450806" target="_blank">📅 08:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450805">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
برخی منابع از وقوع انفجار در بندر صنعتی ینبع، ‌و پایگاه‌های آمریکایی در الخرج عربستان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450805" target="_blank">📅 08:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450804">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeYRKgS-T-vWe9c3WEhyNIzja8Z8vxnOgg7Maf1Xd40_H9ul9hxeClno9OZXP8B9zKJFmbvW1kD8y-axEIlc6RAWoWg0Izcc0ACETSvXmGLuHCO_NMrUoMLMg2tz3rGbSftPs2dDRx6lNstQ2UM7vu-VATBtoMWLp5yGQzgJ100RbRUMCFweJ2_IqWg2mFZ2mHngigOn2Q17EG1rB52sXhdJwTkNlc6wCRTX1frYh8cWBiK_IldsNuxFaLEUvs0IIcdZbAKVHWjIgCnJOIPwbWLQwNkY-ZBom1kFLGW8QEzPRD365WMb63AaEHoXj51DQBmRo9dyFYiS1YIxJ3ldOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیفیت هوای تهران قابل‌قبول است
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای پایتخت امروز روی عدد ۸۵ قرار گرفته و در وضعیت قابل‌قبول است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450804" target="_blank">📅 08:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450803">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
نیروی دریایی سپاه: در ساعات گذشته ۴ کشتی متخلف متوقف شدند
🔹
در ساعات گذشته، ۴ فروند کشتی متخلف با حمایت ارتش تروریست امریکا قصد عبور از تنگۀ هرمز را داشتند که طی یک عملیات ترکیبی موشکی و پهپادی هر ۴ کشتی درجای خود متوقف شدند.
🔸
نیروی دریایی سپاه با قاطعیت…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450803" target="_blank">📅 07:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450802">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🔴
منابع خبری از شنیده‌شدن صدای انفجار در کویت و اردن گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/450802" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450801">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
صدای انفجارهای جدید در بحرین و کویت
🔹
منابع عربی از شنیده‌شدن صدای پیاپی انفجارهای شدید در کویت خبر دادند.
🔹
براساس این گزارش‌ها، پایگاه نظامی علی‌السالم کویت آماج این حملات قرار گرفته است.
🔹
شبکۀ الجزیره نیز از به صدا درآمدن دوبارۀ آژیرهای خطر در کویت خبر…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450801" target="_blank">📅 07:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450800">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در محدودۀ جنوب اصفهان
🔹
سپاه استان اصفهان: از ساعت ۸ صبح تا ۱۴ بعد ازظهر امروز احتمال شنیده‌شدن صدای انفجار کنترل شده در محدودۀ صفه، بهارستان و اطراف وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450800" target="_blank">📅 07:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450799">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
🔴
منابع محلی از حملۀ مستقیم موشک‌های ایرانی به تأسیسات آمریکایی در بحرین، و انفجارهای مداوم در آن محل‌ها خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450799" target="_blank">📅 07:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450798">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjIty5AcYUYj9_y_izEP3sl1BIcw4GZ7H92NluAIeZ-mzfqY4hvEDZl85B7Xwz08OUL2FhTDtdlPdJbKa0vB9kvzmlQ3D9t-FBL62P3QJMjm0eIPdGd4BQkgAbmsgNCApUGvxR0SdDlqH5hym6qYRl8iJ_1OTbKi2saMJOejnPmzh0NmmcEkFvnJfcBwVThQbh550WxRH0Or1fNh6zLlLJgvVyDerhahSfCx3QW5OwKIoI3jPz8sy1JOvYbt1zohBFziYnvvxWxYI9DURQl68KDecjQEuvhgIdv2YU85jDmTuYFgfe0SZgXczBNXJFzkU0T-U004T3UrMjWOgc0n0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویر منتشر شده در فضای مجازی از برخاستن ستون‌های دود در کویت
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450798" target="_blank">📅 07:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450797">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz0rhi_1hML4NDgiD_C0XGonLMsLbvP9OaNq2YJBbYcg1bxC2rqEvUy56kVBDcaxqTCkr5AD71aTXY-hzq9-3dJjNavp8ESmvIzRoZclOvNXpNaiQraH0s2TnmM9K6obY6hQVmVb1p3Y1n6lG0PrhL39FhfY_qPVcFk76RMzNBHmy9lWZmPkKFXpUt7pLrOflb_q0gViAlweGaE5OjxmcbUWQHsa2I4wHUwySZlUIjYyqRtltYNXnjXYlhCmfcQOjZpu5IQj7f8M5kSKvis8opj_JFIEF4Uv_ELPRrT9VSyx0Y0AidJVlE9sYiDfalsPf-LwEofY-IgvNM_YvdODbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۳.۵ ریشتر، صبح شنبه حوالی شهرستان بندرخمیر در استان هرمزگان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/450797" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450796">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
رسانه‌های عربی: ناوگان پنجم نیروی دریایی آمریکا در بحرین، مورد حملۀ هوایی شدید قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450796" target="_blank">📅 06:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450795">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fd1266d40.mp4?token=nusexP2ATpDOiodhp8i0MeYbXRoYCLIc97Xz5p1OUMjevRVi1MAK4BgNX8ed-E9rGx2WfXssLjv5vFjLBGx4BvZWAWwH2nCBwy6i6wB1B5nRf_HEpzrXiFsv5Y_etl9Ul14-tmo48QikD8wxg3jsNoVYjxYtTSz1KkrVyRMzwp9LiIJ7PkTT3qiUKYIl9EVIYkhyeGrvmGBGP3_agkqDbHRhQepCgprPfz5a-wLp2EKgsKTm22ypTF0GRFd-rRre4EsouWRpBlIl-q-7kBUCZfgdsvFn9BnwgL-vBgtTDGwVFXZBsLuUNKP6Pqo5yAi6REChvFyaZrBvYxN7b4YqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fd1266d40.mp4?token=nusexP2ATpDOiodhp8i0MeYbXRoYCLIc97Xz5p1OUMjevRVi1MAK4BgNX8ed-E9rGx2WfXssLjv5vFjLBGx4BvZWAWwH2nCBwy6i6wB1B5nRf_HEpzrXiFsv5Y_etl9Ul14-tmo48QikD8wxg3jsNoVYjxYtTSz1KkrVyRMzwp9LiIJ7PkTT3qiUKYIl9EVIYkhyeGrvmGBGP3_agkqDbHRhQepCgprPfz5a-wLp2EKgsKTm22ypTF0GRFd-rRre4EsouWRpBlIl-q-7kBUCZfgdsvFn9BnwgL-vBgtTDGwVFXZBsLuUNKP6Pqo5yAi6REChvFyaZrBvYxN7b4YqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پایگاه‌های آمریکا در اردن و کویت، آماج حملات پهپادی ارتش
🔹
روابط عمومی ارتش: ساعاتی قبل، پهپادهای انهدامی ارتش در مرحلۀ چهاردهم عملیات صاعقه، انبار مهمات ارتش متجاوز آمریکا در اردوگاه العدیری و ساختمان‌های ستاد و انبارهای مهمات این ارتش کودک‌کش در پایگاه…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450795" target="_blank">📅 06:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450794">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
رسانه‌های عربی:
ناوگان پنجم نیروی دریایی آمریکا در بحرین، مورد حملۀ هوایی شدید قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450794" target="_blank">📅 06:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450793">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چندین انفجار در بحرین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450793" target="_blank">📅 06:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450792">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
تأسیسات برق و پمپ‌های آب‌شیرین‌کن اسکلۀ روستای بونجی هدف حملات موشکی قرار گرفت
🔹
معاون استاندار هرمزگان: در تداوم حملات دشمن جنایتکار آمریکایی به نقاط مختلف هرمزگان، این‌بار تأسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکلۀ روستای بونجی از توابع شهرستان جاسک هدف اصابت موشک  قرار گرفت.
🔹
بر اثر حمله به این تاسیسات، آب شرب چندین روستا در غرب شهرستان جاسک قطع شده است.
🔹
بررسی‌های اولیه برای ارزیابی میزان خسارات و آثار این حمله در حال انجام است و تلاش‌ها برای پایدارسازی وضعیت آب شرب منطقه آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450792" target="_blank">📅 06:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450791">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
منابع عربی: انفجارهای مجدد پایگاه‌های نظامی آمریکا در بحرین و کویت را به لرزه درآورد.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450791" target="_blank">📅 05:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450790">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
حملۀ هوایی دشمن آمریکایی به جزیرۀ هرمز
🔹
استانداری هرمزگان: در ساعت ۵ بامداد، نقطه‌ای در جزیرۀ هرمز هدف حملۀ دشمن آمریکایی قرار گرفت.
📝
جزئیات این حادثه پس از انجام ارزیابی‌های اولیه و جمع‌بندی اطلاعات، متعاقباً اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/450790" target="_blank">📅 05:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450789">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
صدای انفجارهای جدید در بحرین و کویت
🔹
منابع عربی از شنیده‌شدن صدای پیاپی انفجارهای شدید در کویت خبر دادند.
🔹
براساس این گزارش‌ها، پایگاه نظامی علی‌السالم کویت آماج این حملات قرار گرفته است.
🔹
شبکۀ الجزیره نیز از به صدا درآمدن دوبارۀ آژیرهای خطر در کویت خبر داده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/450789" target="_blank">📅 05:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450788">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به‌صدا درآمدن دوباره آژیرهای خطر و شنیده شدن صدای انفجار در بحرین
🔹
منابع خبری اعلام کردند پایگاه پنجم نیروی دریایی آمریکا در بحرین هدف موشکهای ایرانی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450788" target="_blank">📅 05:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450787">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
حملۀ موشکی دشمن آمریکایی به حوالی جاسک
🔹
استانداری هرمزگان: در ساعت ۴:۴۴ دقیقه، نقطه‌ای در حوالی جاسک هدف حملۀ نظامی دشمن آمریکایی قرار گرفت.
📝
جزئیات این حادثه پس از انجام ارزیابی‌های اولیه و جمع‌بندی اطلاعات، متعاقباً اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450787" target="_blank">📅 04:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450786">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
حملۀ مجدد دشمن آمریکایی به حوالی بندرعباس
‌
🔹
استانداری هرمزگان: در ساعت ۳:۵۰ دقیقه، نقطه‌ای در حوالی بندرعباس مورد حملۀ نظامی دشمن آمریکایی قرار گرفت.
📝
اخبار تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450786" target="_blank">📅 04:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450784">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
رسانه‌های عربی: انفجارهای متعددی بار دیگر پایگاه‌های نظامی آمریکایی در کویت را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/450784" target="_blank">📅 04:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450783">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef9c760ee8.mp4?token=uVtPTY6dnINctPdHzgmUN521bz04WNzUhMxB5vCnc2CWU-nTmbObQGVuNVjttVLyAtTQqI72uGg8nFR8d_6-3VyMDyCCm5GZobfeFUhOlwAxAMo5VD0zeVNMEqhPNHdzGBLAWorciBZg9xQO-c9Wqio5BzEEbi9-JZAePhI-7k1KYIP9LaXPuK9jWT7HZxy1e49mepDFWxvjAPQOCQgxgJnwajsGbH2WFaig_0e32OlIwcLlDqvsj39kcFxDqGgYHeY3xzw1a796XLWKsxeogjM4Ss4_iTG_QMAJFboVSPtfNCtB1M2YJpL3vDjQIhnPgXRwrs1BHCSv86DizkVrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef9c760ee8.mp4?token=uVtPTY6dnINctPdHzgmUN521bz04WNzUhMxB5vCnc2CWU-nTmbObQGVuNVjttVLyAtTQqI72uGg8nFR8d_6-3VyMDyCCm5GZobfeFUhOlwAxAMo5VD0zeVNMEqhPNHdzGBLAWorciBZg9xQO-c9Wqio5BzEEbi9-JZAePhI-7k1KYIP9LaXPuK9jWT7HZxy1e49mepDFWxvjAPQOCQgxgJnwajsGbH2WFaig_0e32OlIwcLlDqvsj39kcFxDqGgYHeY3xzw1a796XLWKsxeogjM4Ss4_iTG_QMAJFboVSPtfNCtB1M2YJpL3vDjQIhnPgXRwrs1BHCSv86DizkVrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی منابع خبری می‌گویند که سامانه‌های دفاعی آمریکا و اردن نتوانسته‌اند هیچ یک از موشک‌های شلیک شده به پایگاه موفق السلطی را رهگیری و منهدم کنند.   @FarsNewsInt</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450783" target="_blank">📅 03:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450782">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
حملۀ موشکی دشمن آمریکایی به جزیرۀ لارک
🔹
استانداری هرمزگان: ساعت ۱:۲۷ بامداد نقطه‌ای در جزیرۀ لارک مورد حملۀ دشمن آمریکایی قرار گرفت.
🔹
گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450782" target="_blank">📅 03:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450781">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552459cf22.mp4?token=KGYEVWEJ8T46DqTMiIcL5BHnv72DO6o3yq1SUdr-n0uXOmtxDoKNrbYungRzSqINvi_Fxnmf8HMexrtxKYQ93PezUHf3-nadwhxdmmC4-jfx__t8Xhya9waNmYUp8iQPjgIahyNzRz4Tt9DYCYMkd7Rwaj3FYFgqXXC-7-HWmxr5xu16gnpX0ysTzlmB9sEsC1f8aZ8aVWoq9-KUMITTDRPJvKsNeT89-gf-n3J39QlsfFRDe8tjFe-7J9YVkxYGFZJsun-Hg54kQo13DW9KhJql05Btx007-9-jaqU3SlCn9AQpcJwOlpm1WWlP12eTGXE3FoePey0CSnyQADhD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552459cf22.mp4?token=KGYEVWEJ8T46DqTMiIcL5BHnv72DO6o3yq1SUdr-n0uXOmtxDoKNrbYungRzSqINvi_Fxnmf8HMexrtxKYQ93PezUHf3-nadwhxdmmC4-jfx__t8Xhya9waNmYUp8iQPjgIahyNzRz4Tt9DYCYMkd7Rwaj3FYFgqXXC-7-HWmxr5xu16gnpX0ysTzlmB9sEsC1f8aZ8aVWoq9-KUMITTDRPJvKsNeT89-gf-n3J39QlsfFRDe8tjFe-7J9YVkxYGFZJsun-Hg54kQo13DW9KhJql05Btx007-9-jaqU3SlCn9AQpcJwOlpm1WWlP12eTGXE3FoePey0CSnyQADhD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی منابع خبری می‌گویند که سامانه‌های دفاعی آمریکا و اردن نتوانسته‌اند هیچ یک از موشک‌های شلیک شده به پایگاه موفق السلطی را رهگیری و منهدم کنند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/450781" target="_blank">📅 03:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450780">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c3e5dae0.mp4?token=cXhRnW-n2hAibgB8KLWgdVdLgBWetRSNYMx6nL05iGC-PMGH3hjCEytyzLjE4fRgO6LNzUC2GCaWW_Wg1E2w7h9AynKElnPbUoq2GjiLMT0miP5B4K8K8ij3-X8rK5k2bKOxhLjJaZYBKDOiK4wX7CqbNlp5BUj09HZ-vNTas1DyyUacW7YJSowAiOo341M3ZQWdFgc6OXycQ2bmwVF4lbrJFNUuvoAzw_2m6Jgb40XEL2GPb7OwRTco5iDT6dbpnzHoEX48nNR6x2PPk4h3UdaqiPEmk1WEQGIlGBXW9wsI3FPbS31xUziQE7Z2ggAsKDjzLedTXx_2l6ypBMWNBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c3e5dae0.mp4?token=cXhRnW-n2hAibgB8KLWgdVdLgBWetRSNYMx6nL05iGC-PMGH3hjCEytyzLjE4fRgO6LNzUC2GCaWW_Wg1E2w7h9AynKElnPbUoq2GjiLMT0miP5B4K8K8ij3-X8rK5k2bKOxhLjJaZYBKDOiK4wX7CqbNlp5BUj09HZ-vNTas1DyyUacW7YJSowAiOo341M3ZQWdFgc6OXycQ2bmwVF4lbrJFNUuvoAzw_2m6Jgb40XEL2GPb7OwRTco5iDT6dbpnzHoEX48nNR6x2PPk4h3UdaqiPEmk1WEQGIlGBXW9wsI3FPbS31xUziQE7Z2ggAsKDjzLedTXx_2l6ypBMWNBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پایگاه‌های آمریکا در اردن و کویت، آماج حملات پهپادی ارتش
🔹
روابط عمومی ارتش: ساعاتی قبل، پهپادهای انهدامی ارتش در مرحلۀ چهاردهم عملیات صاعقه،
انبار مهمات ارتش متجاوز آمریکا در اردوگاه العدیری و ساختمان‌های ستاد و انبارهای مهمات این ارتش کودک‌کش در پایگاه علی‌السالم و چند پل ارتباطی در کویت
را هدف قرار دادند.
🔹
اردوگاه العدیری، از مراکز مهم پشتیبانی و تجدید سازمان رزم نیروهای آمریکایی و پایگاه علی‌السالم نیز یکی از بزرگترین مراکز پشتیبانی و هماهنگی عملیات هوایی آمریکا در منطقه خلیج فارس به شمار می‌رود.
🔹
در ادامۀ این حملات،
مخازن سوخت ارتش متجاوز در پایگاه الازرق اردن نیز
هدف حملات پهپادی ارتش قرار گرفت.
🔹
پایگاه هوایی الازرق اردن به دلیل موقعیت، زیرساخت‌ها و استقرار تجهیزات نظامی مدرن و سرمایه‌گذاری کلان آمریکا، به یک پایگاه حیاتی برای ایالات متحده تبدیل شده است که برای کنترل منطقه و عملیات‌های نظامی در غرب آسیا نقش کلیدی ایفا می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450780" target="_blank">📅 03:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450779">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
همزمان با حملات به کویت، عربستان و اردن، منابع عربی از شنیده‌شدن صدای انفجار در بحرین نیز خبر داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/450779" target="_blank">📅 03:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450778">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رسانه‌های عربی از ادامه‌دار بودن حملات به کویت و اردن خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/450778" target="_blank">📅 02:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450777">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌ رسانه‌های عربی: حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.  @Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/450777" target="_blank">📅 02:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450776">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رسانه‌های عربی:
صدای انفجارها در پایگاه‌های آمریکایی اردن به حدی بود که در مناطق اشغالی شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/450776" target="_blank">📅 02:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450775">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
منابع محلی از
حملۀ موشکی به پایگاه‌های آمریکایی کویت
خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/450775" target="_blank">📅 02:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450774">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
حملات دشمن به هرمزگان تاکنون ۳ شهید و ۸ مجروح برجای گذاشته است
🔹
معاون استاندار هرمزگان: در پی حملات دشمن به برخی نقاط استان هرمزگان سه نفر شهید و ۸ نفر مصدوم شدند.
🔹
دستگاه‌ها و عوامل امدادی و انتظامی از دقایق اول در محل حادثه حضور دارند.
🔹
گزارش‌های تکمیلی پس از جمع‌بندی نهایی و بررسی‌های میدانی اطلاع‌رسانی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/450774" target="_blank">📅 02:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450773">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌‌
🔴
منابع عربی: پایگاه‌های نظامی آمریکا در عربستان سعودی، هدف حملۀ موشکی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/450773" target="_blank">📅 02:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450772">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در امیدیه خوزستان
🔹
دقایقی پیش اهالی امیدیه از شنیده‌شدن صدای انفجار خبر دادند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/450772" target="_blank">📅 02:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450771">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
رسانه‌های عربی از وقوع چندین انفجار در عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/450771" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450770">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
رسانه‌های عربی از
وقوع چندین انفجار در عربستان سعودی
خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/450770" target="_blank">📅 02:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450769">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
برخی منابع از وقوع انفجار در پایگاه‌های آمریکایی اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450769" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450765">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6QNIoL_qS3d1gin-efmWjqYreAjVJFQJRIqBdGVHjC4nPZjS5GhHA8QNnHbtLSNzJ7ld9p52Ju-X73RJiItg148dsHLDVivmON4knvlDifuN4hpojapQZl-WjAeO2N9xkNIum_C9Jo3WHVonq6PZ9LuZFumiikjABxQm5uY4rmSH2TZLS05CB8PRsA58kNH9TRKo-b64eA7AG54p5Pa7HXQzLk8cEUTg1TI7vnR7OD8LcK-7Fd_JgwW6SJCcVl9viONbyHDqsz8Hqqr3hiJxEEA5OIFQ3wRxaf37Sqtxnc9HkwdMlGQv3O0iKZ3fCCPnZlYRaGClrTjXB-OpDsHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GS3e4n5LjFo5zzH960u7jGgwz6lfk86_QPF7MsE9iYgJt1487u9mEh8vb28DbPL4mKPEFjG2ZRR4J751ThEj6xKBUgOnfBDwbfWDG1KHigcFlOkvO1jrvRfMAGOaMWh5QSMehkRc5HYmGxS1mYrHC-LIz4BcGl1kfqsUwL8DWDvK8pQTdiF5TX0kTMo0fbo89u-WmhoMz1ergBzzbYL167QLc-Cfn9qguC7p4NDMFnaxNt35fED5uCpTG7wtMh4A5N7w5A8B9QsaHLAZNLPQQuZRkOIkuysFN6fkeVB8n6Xc3Z52eXFQfZYXg6cv1BWAMRjkmjcb4kn_2YY4tvTquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbJITzmxRvzqR1HtmQ31nVk550gO6M6E6ZFLK_u6hboGdtb3jbfQXN067AW_EDR23acGxn4gNLshgTIKT-UnzbuSNo4rJLY-4h0R7qF2Fclk5152EB_izGWCdp240B9IXEDw_a6POsID2zz9RTl3Z-SReOvpoAU-4ayBnxn6Rn_hOzMTJQ0yg3NtNLCHfGC01TPb3xDOXT8FP3L561jeQKdD1UrgugCcd46QaE67YbBOYi5QJkIaetn4F6uaiDshNSnVJJ58gY7NuYSNjpS8z3nF1TGVZpYVnK7ajXIiyeJinpgTCDtkROb7PER0nVeBwNeA4fL15J3ToRbm34HDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-w0nZL3e70aasuRVU5a7cu_D3kGnL2jY1_ASftKHvSIxoquUx2HDezEQOaaO3cPv3xCiVVK6wmOFIuMiqAkafByi7uHtemT7sDaJ61Dg-OJThltn6X9m_-XjZBBQYGaxDN9E1UHni130Je_HvaK4CXmIpimGBfSRNGc0hsGABsjHAjqsiJfPkP7BWUfXkMnbJcJ09f1LbPhAVNRNAtPblJzY83MTzS4CWAzz_PoaaD7lPKwq7xc6mQb-IaShBvyOj8ea-aVsuNVUUXmH0wY0xKY6pH1X51yDohSDTyn_DbdbBDn8dqHy6MQ6cqIkL1I30UTFbRAFGmTGihU2JXfZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۷ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/450765" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzUkdG2PpF5OYJ1eYbUGyRaUHLvQtfTpXhRb_10a8atlYeNjWps-1bWkVBhL62Mix6IECQ6VZVR57tnq_r-z-VzUOlpdjfziwQlwB1Bqu8LvJJ-e-tMXwlOQCOeexqy_p7fyjExIZav1DWKcNrwt9FWDcFGQwOQW64o-Lh_c41hBJ8WZ2_2Z4Jq_DXQyHkYxBF-le6Zxqtl92EIn42vD26_vVZBLYBATVDbLzi5UtCl-ZVCp_pZG7C7kGDBAEZKVhCrY1xHu1kId8ZST6i5itLhTkNSUqL0s6zcfaa0JSyPQ9g3V0ikj-JVxKG0AH9wN4VtOET-1wFBa4r6dJ1sivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_ylE_H9kbtqskpbLVihMt9Z42BLFPYuHsIJ0PJydr6FJEwAfVnTyEdGr5E7zZZucoT5zhf3ExfDDd4aWXlfpbEYHSYshnUoM-IA2Fr2VusRa6wZjIoTCOWcCrc8bXA4nCUWErv1ocyHJvDuQCuUnd-nyV_htFuTuwe2GvrdG2QiZAgDdA036__tYpOQ5y5ubJ4phx7-RHMY4-P4CimRVkDrZDx58ynYMESlKMCuZRCc_6cavZ0JzzfBoSAfZe7V5qKfJOOhkObDDxgWlc4Pw0t14OJY1kBGXa0-gQBQS7wMDmBwzMpsWcFXSlGxJckRMcSk9LnSnngUsC_2vwr88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nE43XmQXhPWHOX8YeDf30ZrFtJWdKBRIwiZc5-pdxzPqoAX03aQw39FcXLlF7gDLR04gsszLpiiT9Xjk6KMAMtx1-_FArIZDOFkkP1pv4j7chkfuil0Bv12iVS6Cw4Vs5pYvns0m-jYmXIIdTUWxCFpHbp6Nu1Uug44cLKixyZhM9onlgg6D37zyR2H99RdktHSdd4Ldv7g-u2LsWrj8jxvyo3vGNxjvuBdwHXHn-3Wy3yMVbqaLPaVk5JBP4zdgCppVU5K6Tt0afQh07_6VMxDMWz-CVrxkDmghAL63begi05QBmJQXGTNawT490ufLWPwlMquqhyExveBf9pm5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vf2zSil8UxErE_vksbyn9y0OmLIyj-X14t7vABXW4euiFSrPXMr7cKFj6pWCvLmfqBPhMGtG3Ff2wYWf16eq7hf3HKli0QH0_hNQspE5WqrZIuT7CgbakuGD-r94XY2ZVH_m7o66j8zIZaLMptFtPjL1GGbt5FrQZS9YUbjrFpo2qWSJB4RF53SVWMuTlM3efSJmml0huohE7ooYvbXPAqIOPt1MBo1w5H3bWRs7hl5f59EYpu2Oe89XqSjGYXE_DUMlw4u27YQ0wYBQPt6kPJUGZ94SyfQwT_thE0WhRGxr3sTy18pY5jc9_NblPYNkMA9ystag7Y9M_1MKHZX95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNp9GrycFHLfjhUqgc9kb0gOymD3hvAFjSRiN0G0OojsMoe0wVBIAYvj5xumHATteQW1zOR2QDzKcLK4J5DWd87jMClbvUbByXpN-35kuPykYHBS_b3r4oDZkMblygVN-cnxUidwCUPl05jAhDOTj_oNNSnwaZdgWoW-SA44PnvcmKrdAt63L90820-nLXAsTS8Cq98i0P9pxk3LWKS6TWXIvgK35YZ3plDqZttGw5jxYl1KI8NNKEyKIBbszF45-5ESTXwoMude8_GM2p0gGhug8piGe7tqpK1jtboa7HPxAfWIKNcvaHLnjqCFAqboNkSSVrQAFTevhKEbd5ZHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsx5h-lUiPolnYigo13vhPtgDFJDpY1VZrOHF_YPTqOuDTvODVzWW0tPA-6dkecjecPXOWadNWlhrIkzHmNXkSfjSj5rxSVI0tQdZ5LomuBNh3KYjNtqE5K2nQkRQJuDFnSneRR71YZVjUxKy2ex_eJXIezvpp3zjNXlihTFPfoY3twf_DtmAuel1YQ1Seh-Zb9WKR7mbGkW4MUcNXk1Abgqh8p7AfQI4dNDAqtVGiprRJFapJrFIW5ie3sIHCF4Vce2Ea3NVUXozNTCmOVUtyt6Ecjw6jZsKYMjNUvEidXVNM5C0SfHW7_ff4NunQHMlX-lrGd2iZ3TXqUm6OhorQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vd4_XzjamMaUEhzsru5eodtwYSIvj7JpJVzdpH0CMJkgrSkfXsYnGfsSbRrhvQSRKzZuGPtB7JsSUbzUA4xlObbpP2RrMHtopBmgL-0EAp_upME9Lacmaat4oVybYeOtbxBBNnaGe3o-mToetgwExme2TOM-qhKM3FBSuXFX4YCwWAN_OLVQ83s-gVNUyGJj3wD_QM0dYQvFR7L_MDwo10GgZcUf0CIfyWwZTRK5aI_MdymyinXLsfcdouG2WXV8-xx0_hAyh28stz7dR6T2sXQl0D--SB6CefIqijbNcBTbW5VO-CBUslNH4-unPL9LzgZT1gTERkEYQohdVLzDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQrfMhdVKZTtd7eVWzsY5ssDzdMoc3_WiK6rtNLX8EbaRBk-b4K5ZSZpIOEzlsjnjV-fGICwYWt-MxYRy0zAR-Hn0xkrTx-n30dQPmnVMhLbVYDzsn4hv8m0f-LqQ6_h8D7EDVyYAb72zqLQmRZexZ5VqDURkTAzHamJHed1VQFVReEuE_JWjrAevaN1yQxeIBVBmYapHKhsN-d2HcqrAonoRkBiCw4ZJqaYua6EpF_l0khIcJpbe7lR618J1pFIlowLGrd1Ap1TYdTqnDQOy1y84kGYSELjjaMIpD--RRSAd54VraIjbrhg2xWROoqHDdr6_WGR_IRKW9ZKn3jlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cy-0wMkPiyMURMgP2abBf_6B4NikMlMadn1qWtWmeeygRcWDuzpNyu4hY_Z50sJrqc0MaU-DirfANXEOl1-oY5s4l7M10aJk-l5QrK-L-1VOncuzxhCsDTvTMo22urMkcWuCguLPFmjsOOFvCATRhtC1K1_pUA5dQFzW24g7La8TrPFfmyuBKNFIdDh4EEiaosGf43tv6nIH4Jb7tpQzv_aklUK2tIHSRBEqNEnEuvpdNpnRf_vC24gS8EVnGxcIfvLQDbQo1hECuHgnN3-GYmYclsQycKo-HhjdO3y6gPVeVYYwEnNWwCryofjgLNYTN2OEqKsDDIqhViDFJ38Sgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/450756" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9SspkQh8KckNg3n06gs6-R2nu05A-ziMS98fjghg97pwtDeIXAEeUjVZMYV5Ri7cVUhhFKrOk2ReH541WVQDre-UaES2VLdlp85mHpjoxBi_FHxI5sHklyCUv7cgrHGvmLO1K9Wk-EdVA6JYAicz5bHtrPZdafi9vthzOivg4XEiXCMY_bYhhZBemx76aQZ-YUlC2lxCCHMucdtjEgLMtLHlDqCMQlPWK2kdokc0Su7Dd5jiAqPG0wV4s2SFVNcS_62A1sJ6AIaSBvKIbGy16dnsBSaIetMrAM3cPlw8EcyRX7xkuhk1fk3IK8u6zm43QC9aRP5KOE7q96MrJPQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سپاه: دو فروند کشتی نفتکش با عبور از مسیر مین‌گذاری شدۀ جنوب تنگۀ هرمز منفجر، و دچار آتش‌سوزی گسترده شدند
🔹
ساعتی پیش دو فروند کشتی نفتکش که با فریب سازمان‌های جاسوسی آمریکا قصد عبور از مسیر مین‌گذاری شدۀ جنوب تنگۀ هرمز را داشتند، منفجر شده و دچار آتش‌سوزی…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450755" target="_blank">📅 02:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
منابع عراقی از حملات جدید به مقرهای تجزیه‌طلبان در سلیمانیۀ عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450754" target="_blank">📅 02:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ec623ab8.mp4?token=iqRGEe_D2BpNkVQhxLLlAVsa7_SzdgcNZtppT1nuSGJ2iUU8IOmq3FuTU5xjMPHIGlMmts9I1llBQVcWtQnvt7GEGZ6L_n-xqvLctLNs_S8e3HqvDCJj4Mm_BbMTMZT95V7ozYoqyaelDBkcRVhKa0d4_W5PnGAO0EUvFHg4sCiFKtWA4ys9nDfwygzqQWlKM3_t812WysfWVXWqpLAM1kRWg4fJOlfGlHGL424V-2rXHsumcOF12YRWzBPxo9MDC3WETaR3mTU8H4JFRxKIhu-n0qJ0JcqJYQF9H5LaTT45RbPd8A41Mxfjj99dzWApItfdzs65lzM8H4jpUSf1AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ec623ab8.mp4?token=iqRGEe_D2BpNkVQhxLLlAVsa7_SzdgcNZtppT1nuSGJ2iUU8IOmq3FuTU5xjMPHIGlMmts9I1llBQVcWtQnvt7GEGZ6L_n-xqvLctLNs_S8e3HqvDCJj4Mm_BbMTMZT95V7ozYoqyaelDBkcRVhKa0d4_W5PnGAO0EUvFHg4sCiFKtWA4ys9nDfwygzqQWlKM3_t812WysfWVXWqpLAM1kRWg4fJOlfGlHGL424V-2rXHsumcOF12YRWzBPxo9MDC3WETaR3mTU8H4JFRxKIhu-n0qJ0JcqJYQF9H5LaTT45RbPd8A41Mxfjj99dzWApItfdzs65lzM8H4jpUSf1AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما: صدای پرواز جنگندۀ‌ دشمن در بندرعباس به گوش می‌رسد.
🔹
دقایقی قبل صدای دست‌کم دو انفجار در بندرعباس شنیده شد.
🔹
همچنین در سیریک صدای ۳ انفجار و در جزیرۀ قشم صدای چند انفجار شنیده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450753" target="_blank">📅 02:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
حملۀ دشمن به ۳ پل و تونل دیگر در هرمزگان
🔹
استانداری هرمزگان: تونل شهید میرزایی در مسیر رفت و برگشت به دلیل حملات دشمن مسدود است.
🔹
پل رودخانۀ شور هم در مسیر بندرعباس به سیرجان مورد حمله هوایی دشمن آمریکا قرار گرفته است.
🔹
همچنین پل محور رفت سه راه‌میناب به‌سمت رودان بعد از دو راهی سرزه مورد حملۀ دشمن واقع شده است.
🔸
مردم از تردد در این مسیرها خودداری کنند. تلاش ها برای ایجاد راه کنار گذر و راه‌های جایگزین در جریان است.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/450752" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
شنیده‌شدن چند صدای انفجار در بخش‌هایی از یزد
🔹
صدای چند انفجار در بخش‌هایی از شهر یزد به گوش رسیده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/450751" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450750">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
حملۀ نظامی دشمن آمریکایی به بندرعباس
🔹
استانداری هرمزگان: در ساعت ۰۱:۲۰ نقطه‌ای در بندرعباس مورد حملۀ نظامی دشمن آمریکایی قرار گرفت.
🔹
گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/450750" target="_blank">📅 01:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450749">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
سپاه: دپوی شهپادهای آمریکایی (شناورهای بدون سرنشین) در بحرین در هم کوبیده شد
🔹
ملت مجاهد و خستگی ناپذیر ایران؛ همزمان با حضور هوشمندانۀ شما در خیابان، فرزندان غیرتمند شما در نیروهای دریایی و هوافضای سپاه به عملیات پیروزمندانۀ خود ادامه می‌دهند.
🔹
شب گذشته…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/450749" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450748">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
🔴
منابع عراقی: دو انفجار مجدد پایگاه آمریکایی در اربیل، شمال عراق را لرزاند.
🔹
پدافند هوایی آمریکا در تلاش است تا با پهپادها در آسمان اربیل مقابله کند.  @Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/450748" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450747">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎥
منابع عراقی: شدت آتش‌سوزی در مقر گروهک‌های تجزیه‌طلب به‌حدی است که آتش‌نشانان کنترل گسترش آتش را از دست داده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/450747" target="_blank">📅 01:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 در آسمان بوشهر
🔹
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانۀ نوین پدافند پیشرفتۀ نیروی دریایی سپاه در آسمان بوشهر رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/450746" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
رسانه‌های عراقی از وقوع دو انفجار در نزدیکی فرودگاه اربیل و کنسولگری آمریکا گزارش دادند.  @Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/450745" target="_blank">📅 01:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
شنیده‌شدن چند صدای انفجار در بخش‌هایی از یزد
🔹
صدای چند انفجار در بخش‌هایی از شهر یزد به گوش رسیده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/450744" target="_blank">📅 01:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بخش‌هایی از لار
🔹
دقایقی پیش اهالی جنوب لارستان از شنیده شدن صدای چندین انفجار خبر دادند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/450743" target="_blank">📅 00:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
حملۀ موشکی به نقاطی از اطراف شهر اهواز توسط دشمن آمریکایی
🔹
معاون استانداری خوزستان: دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
📝
اخبار تکمیلی متعاقبا اعلام می‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farsna/450742" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc426d520.mp4?token=cVWtjyfWTcJsLuLPqR0YICo1bTGreeAVvk4vJHKbGFuV9NYSRJPH8B6e3mdWcxjgXs9IX3ONnfm0hccQwTs52Yh1PqYSqCEfWCAWfGgPDOO21UMDvimdh9b_QAlmuG4RBgtCAGDAMTzOGLRQrqNnIidqaRmHWYloyo-xcXgaunK6gOBwFxh8mT00hnceU35-9IfCqE2ab6q5HbtCsDAdb8au06JgmnOylU3JEcPftKWirWdKCzJrnac7AzAhTG0A80wtehFue-unr3UP3J64gwPsQ_fSoCe9YIWjCKmMmfUadK27LZ-M2wHi4eal2ZdA7MI0iGPr3V_8qEQ_2UXL2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc426d520.mp4?token=cVWtjyfWTcJsLuLPqR0YICo1bTGreeAVvk4vJHKbGFuV9NYSRJPH8B6e3mdWcxjgXs9IX3ONnfm0hccQwTs52Yh1PqYSqCEfWCAWfGgPDOO21UMDvimdh9b_QAlmuG4RBgtCAGDAMTzOGLRQrqNnIidqaRmHWYloyo-xcXgaunK6gOBwFxh8mT00hnceU35-9IfCqE2ab6q5HbtCsDAdb8au06JgmnOylU3JEcPftKWirWdKCzJrnac7AzAhTG0A80wtehFue-unr3UP3J64gwPsQ_fSoCe9YIWjCKmMmfUadK27LZ-M2wHi4eal2ZdA7MI0iGPr3V_8qEQ_2UXL2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عراقی: شدت آتش‌سوزی در مقر گروهک‌های تجزیه‌طلب به‌حدی است که آتش‌نشانان کنترل گسترش آتش را از دست داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/450741" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
رسانه‌های عراقی از وقوع دو انفجار در نزدیکی فرودگاه اربیل و کنسولگری آمریکا گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/450739" target="_blank">📅 00:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLyac0GBR9ctT3ORWJHjCxAC4IYq87myUxv_WEt-aBUUu8fmN6TBWe4gNN8jceRgZGJrucvjEX7qNDijFXxClmd66wXuEk6AF_endJ_6Km9GrI8saoQiyIV7JryVzj5HMh-Sc-Z1mnJo7L0C9wGw2UMl4yo4xtQ9p0l82ZJF-OBnTEVywl7RwKrd0nEUZ7-XxXX3M3hCZsLa7EGC8UPe3NwgBBiYGIZqsouQ0VUB2N9fjfr2Pe3lAoOcETf6-mINMAk_9QJByeRTIz5InIjCaDzCaxTjKywU4esZZ5QhxF0Eixk0TACEQFofJ9fG3Y5N96bh775WL8lcVprYZcxH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر ۳ تن از شهدای حمله آمریکا به پل بندر خمیر
🔹
این ۳ شهید اهل روستای نیمه‌کار بودند که درحال رفتن به منزل خویش روی پل به شهادت رسیدند.
🔹
در جریان این حملات ۸ نفر شهید و ۱۹ نفر مجروح شدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/450738" target="_blank">📅 00:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmPsbDKgt0-zJEWHea6vyhLZ0DMd-XdojvjwsBFLFlRRmcMQB7JiMSPPdR30Kq-MhoXO9f4Y0g_ZDV4KQSytqtQqGnJgj1pWhJhBzqj7Vn3fTtIWKbFeE2te9-fCFwvABT_pjfd0ERxtfvpnJVbWIZDkfeY81iaeTU3uk25iNsI5WGeMssJocSEfXKpYBfTcYwCUhN5k5h8L7iXQbyonw9hw_Hs7dLsSyw4Eb6Al2uPoFEVnHH088wzr4bRqrTenqFlEXpNvUhYED2GqfmCABFCyes1rkY4aed6941uJfYKHyk8DvsmijUo4QtX_grej9VIHGwbYi5CqnDBeYEQMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت خارجه: ملت ایران امروز بیش از هر زمانی متحد و مصمم است که قاطعانه دشمنان وحشی را از تجاوز نظامی جنایتکارانه علیه میهن عزیزمان، پشیمان کند.
🔹
آمریکا می‌خواهد با حمله به زیرساخت‌های غیرنظامی و کشتار بی‌گناهان، به اصطلاح «قدرت» خود را به رخ بکشد.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/450737" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌   سپاه: سامانه راداری برد بلند و چندین فروند هواپیمای راهبردی سوخت‌رسان آمریکا منهدم گردید
🔹
سپاه پاسداران: در تکمیل عملیات مقابله به مثل شب گذشته رزمندگان غیور نیروی پرافتخار هوافضای سپاه، در موج ۱۵ عملیات نصر ۲ با رمز مبارک "یا اباصالح المهدی ادرکنی" و…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/450736" target="_blank">📅 00:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">استانداری هرمزگان: شنبه تمام اداره‌ها، سازمان‌ها و بانک‌های استان با حضور ۵۰ درصدی کارکنان، فعال خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/450735" target="_blank">📅 00:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450734">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ادعای کویت درباره حملۀ ایران به نیروگاه و تأسیسات آب شیرین‌کن
🔹
وزارت برق و آب کویت مدعی شد در حملات ایران، یکی از نیروگاه‌های تولید برق و شیرین‌سازی آب کویت هدف حمله قرار گرفته و شمار زیادی از واحدهای تولید برق آسیب دیده‌ است. @Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/450734" target="_blank">📅 23:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در سیریک
🔹
دقایقی پیش صدای چندین انفجار در سیریک به گوش رسید‌.
🔹
همزمان سازمان تروریستی سنتکام اعلام کرده که برای هفتمین شب متوالی حمله به خاک ایران را آغاز کرده‌ است.
@Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/450733" target="_blank">📅 23:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c078d3cff.mp4?token=vhDpi7XWOeFcVe-wQ76pztoJpVhIXZCL6vMbQPDDXjdDsTfcBPEXnzcPY1ij2LdxobBiG1D3vd9FLRjsFymEV1lWsrIayqKpIEF86hY248Kn1jTwDLQQWdPNkhxGLNXa-PtDKlF3krrUC3y22TIdPdsMmSrhI52n_w7dNMSjWQvfOKHLwn-NRjNdi9S3xsc-KJ-eEn_JfzdW5rcpXpTZQPcn9mhy8Dh8-v7EN_v-XDl91_ln3vx3-F6WbSCUW7BvO1HXG0Ybx5ryg_dvKixD_doMc1FfMLRLyMU9eQq89rlj_gyTAtW1drg25bzi6OVnmT3T5YNgau4ShEDtGtpAUHq1WvhCgh8fny8iy4zODCV96c_ViARJ9XyTrlrkbWbq_kBkWC0flQhBXfVYTBXWDO0Fv_lGRuOMZdNwUSTKOR1QWImQt-F3PCr9g7BzV0vRCA1qulUIW5efgKKumWjFOW1ywVyX7MItmL-yRKBco8kT9J6oaGY04s0u6x1vGucOajSqJFUSSxpKJGrDRX5qIA4tPMceAw2BaqJPNCAWMmcYs6Lfg0DLsxcDt9_FDX3DOT7JgJdNVkzJcM9jIqhnSc9Y-mSukk3-cTpYg0b9MyEkLrsky6rcUojjOsSk2ijuThsH4u3R1UnU_ZTaLwkJzqpce6iAoWXGtSYN8hdZh-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c078d3cff.mp4?token=vhDpi7XWOeFcVe-wQ76pztoJpVhIXZCL6vMbQPDDXjdDsTfcBPEXnzcPY1ij2LdxobBiG1D3vd9FLRjsFymEV1lWsrIayqKpIEF86hY248Kn1jTwDLQQWdPNkhxGLNXa-PtDKlF3krrUC3y22TIdPdsMmSrhI52n_w7dNMSjWQvfOKHLwn-NRjNdi9S3xsc-KJ-eEn_JfzdW5rcpXpTZQPcn9mhy8Dh8-v7EN_v-XDl91_ln3vx3-F6WbSCUW7BvO1HXG0Ybx5ryg_dvKixD_doMc1FfMLRLyMU9eQq89rlj_gyTAtW1drg25bzi6OVnmT3T5YNgau4ShEDtGtpAUHq1WvhCgh8fny8iy4zODCV96c_ViARJ9XyTrlrkbWbq_kBkWC0flQhBXfVYTBXWDO0Fv_lGRuOMZdNwUSTKOR1QWImQt-F3PCr9g7BzV0vRCA1qulUIW5efgKKumWjFOW1ywVyX7MItmL-yRKBco8kT9J6oaGY04s0u6x1vGucOajSqJFUSSxpKJGrDRX5qIA4tPMceAw2BaqJPNCAWMmcYs6Lfg0DLsxcDt9_FDX3DOT7JgJdNVkzJcM9jIqhnSc9Y-mSukk3-cTpYg0b9MyEkLrsky6rcUojjOsSk2ijuThsH4u3R1UnU_ZTaLwkJzqpce6iAoWXGtSYN8hdZh-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین حمایت مردم مراغه از میهن در شب ۱۳۹  @Farsna - Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/450732" target="_blank">📅 23:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74a2e91699.mp4?token=TUJ5S7wYsqcbm-_ADr9F3O7JvKg3gD1W_cTdpnK0zgD-r9NYCLUjMiz1mmUzlxGYj_pprlFeARPEc8bK26CGV_hPYc7UMBgRhqJzEJc2hdVmBjog1hCLHH9Ia1BIC1GxtuC0phJfonHV3Ruk8_34MiYWsspZEKye9W2dUA-XRt1scNtRtWUDaJygf2hGOlGrecOpSdkg0o_VlvlRn_qW_yyfXFUG0Fx5yJ_rNN5pBwjpKs0-QvqF8yY8Mjia-vHFXG97Miq8vsI14AHi87DuwmJTxMTtTGwBKXg5epmEYWBtUsnxGRgXyNMdKimHmV30UaDEPrAQHKxp0kk9oHBvwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74a2e91699.mp4?token=TUJ5S7wYsqcbm-_ADr9F3O7JvKg3gD1W_cTdpnK0zgD-r9NYCLUjMiz1mmUzlxGYj_pprlFeARPEc8bK26CGV_hPYc7UMBgRhqJzEJc2hdVmBjog1hCLHH9Ia1BIC1GxtuC0phJfonHV3Ruk8_34MiYWsspZEKye9W2dUA-XRt1scNtRtWUDaJygf2hGOlGrecOpSdkg0o_VlvlRn_qW_yyfXFUG0Fx5yJ_rNN5pBwjpKs0-QvqF8yY8Mjia-vHFXG97Miq8vsI14AHi87DuwmJTxMTtTGwBKXg5epmEYWBtUsnxGRgXyNMdKimHmV30UaDEPrAQHKxp0kk9oHBvwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین حمایت مردم مراغه از میهن در شب ۱۳۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/450731" target="_blank">📅 23:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp6LwuY95OFo45ztj50LlJKjA_EhyBAkwK1HpbQA_d_s7RluqeJ7hhDs0uCYaHfggFmieHXj96hjGTnqMJx5fbwxrWzPI7uxxIu4vCpK0Fb0SHU3O6UFD_iLbSzTuUQJCZb_TX_xaYfSZouKvchHh8TqK-Ze12OXOvyy4260ZCLIJ7yKJ1LJiWrEX6g3qy_AId1NnLJ_-TjSuGCg4i2fw0QIAuv2gGubgyG8rKOdGEtXKsMkxFcyGzZmt23u-dK0yLPRqpa75ez4NmQUSOtyM_zTF4fUpAIDzTfNGFSTcohylUEA0spCfBIStvyMyUDtaSqQ7KuRm6DDqqTS8ZQsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سازمان تروریستی سنتکام: از ساعتی پیش برای هفتمین شب متوالی حمله به خاک ایران را آغاز کرده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/450730" target="_blank">📅 23:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818b30dc1e.mp4?token=tTo_GiXhZ7VIPLSOcSrEl7E7TzdZ-4vgbx35g0VaqLIJfMPIr8RRPgywJJgTLqYCzW2cpyjwmzUkkiaBnLhkPvuksNdLDi_Rowh_0XSK5_ZociANIr6ykM7KVntvsb1xk4ZwM8rLHpPR1K0mImjXoEVDqzYyiqe0IziIJd1RUGYKRFaldzcRXOcOmyCvqUoaBNj1j5EkPzcvK2Xpk3rTszvQ9lLTi8upZlaRLASKRrrbsBK1TniV08bX5rsSqfkmcX0mV7GEJAhJwtHOsb0bu11Fl4n6s28X2aKR10HmIz5xvd9m7oaYgg4MkcE-537C5_6W4CfnSGPV9iQtb-CPFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818b30dc1e.mp4?token=tTo_GiXhZ7VIPLSOcSrEl7E7TzdZ-4vgbx35g0VaqLIJfMPIr8RRPgywJJgTLqYCzW2cpyjwmzUkkiaBnLhkPvuksNdLDi_Rowh_0XSK5_ZociANIr6ykM7KVntvsb1xk4ZwM8rLHpPR1K0mImjXoEVDqzYyiqe0IziIJd1RUGYKRFaldzcRXOcOmyCvqUoaBNj1j5EkPzcvK2Xpk3rTszvQ9lLTi8upZlaRLASKRrrbsBK1TniV08bX5rsSqfkmcX0mV7GEJAhJwtHOsb0bu11Fl4n6s28X2aKR10HmIz5xvd9m7oaYgg4MkcE-537C5_6W4CfnSGPV9iQtb-CPFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ موشکی ارتش به شناور آمریکایی
🔹
ساعاتی پیش در مرحله سیزدهم عملیات صاعقه، نیروی دریایی ارتش با موشک کروز ساحل به دریا، شناور متخاصم دشمن متجاوز را در شمال اقیانوس هند، هدف قرار داد.
🔹
شلیک موشک کروز توسط نیروی دریایی ارتش موجب ایجاد رعب و وحشت دشمن و دور شدن شناور متخاصم از تیررس رزمندگان دلیر این نیرو شده است.
@Farsna</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farsna/450729" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370adce3dd.mp4?token=bDeLCAUe8WX2e_4sSNoG79uG6AVuxUXoQn_N_wHXp_XCf9--LpvYoOvVNxB_lzLNaxavXgxdMKJAhgsoH_WqvPGx-TFjHX4ddJhhPSd_wOpZcMssthh3PM16sHjGi2Ksy5rKYlD1BXqK3SU7ZtxsC7BFVBgkyy3LD0A0yPZeE6Qzcym6xMze4-B30rmqsbmftPFxSaI7gh2BU4GlrCLhQjJG584k8Iwv9Vn-BNEJO1Ld7DFxm2BSdVutiKzSAvRSw1gtXbYs0h21Jo5BUCc7es6Gtk4GVt53Es_h5iCKp-I9u-oNdXYJf5fiy-f-KDQDgavns9EZdHUs64hMdVRlWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370adce3dd.mp4?token=bDeLCAUe8WX2e_4sSNoG79uG6AVuxUXoQn_N_wHXp_XCf9--LpvYoOvVNxB_lzLNaxavXgxdMKJAhgsoH_WqvPGx-TFjHX4ddJhhPSd_wOpZcMssthh3PM16sHjGi2Ksy5rKYlD1BXqK3SU7ZtxsC7BFVBgkyy3LD0A0yPZeE6Qzcym6xMze4-B30rmqsbmftPFxSaI7gh2BU4GlrCLhQjJG584k8Iwv9Vn-BNEJO1Ld7DFxm2BSdVutiKzSAvRSw1gtXbYs0h21Jo5BUCc7es6Gtk4GVt53Es_h5iCKp-I9u-oNdXYJf5fiy-f-KDQDgavns9EZdHUs64hMdVRlWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
در والیبال حریف اسلوونی نشدیم
🏐
ایران ۰ - ۳ اسلوونی
🇮🇷
۲۵ | ۱۹ | ۲۴
🇸🇮
۲۷ | ۲۵ | ۲۶
@Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/450728" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450725">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a00UKY2Xc2Ceb_o6855O_jXkPl4u8h34FOZF1gTGYLPIkDZ8NfU_GCm9lLLG9QDkBWXLkE3Uj4TpVRhdkyFly0ZDUXzuG-Obq9go4AkK3FY_DubN-X4_V6s6mjof87_wOHlh5DxOoM4RSRv-Zbm_9Xg_4PXLXFqMOr2MkpYAvDNGKg82TcoJ8bYFic02juYG2zfHsRoheE1Is9Eq68q1S6RFFQr5PuO6loxspSE4Okfdhk-bOt4vrhtnFSsRw-UuXS7kAeu2wGZFh2FJge2zoLi1nwJFuPbBmG5SML0MbIzH1J23SraFgGwJw3CtE_N_1yElgjfYyGLDeWSU8a948A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PT2NdNy81HDEj32kYUtZLIebNI6OQo68YnIVfjirmnUTaRi6nmeAIW3plMcGbUk__fg37zjOG7tWRtULZw9eIFwKmuU4_CoSpP55RY19E2q8pjcvU61rSaAp8y3FjvpmczxKjqtpdYQlJIvf5qFQVjMDEYqLh5AAFaDpxxtFa3K7GUGhg3NZdRdQwu8SXi4o-8qHRsaybqt4e_J-Pg5YAUGV0KqGu3mP7Qhw2Ny8k9702uAGrO6pJBTKWfI4q3pvszPpkIdfoFAy9ec76T6cftCmUaZaVzgPxWh9ME_BLGEe-ZHvy9Bctu9PWrf_BC-sGPw1tUcwX2_qbZ4Gl0FosQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حجم سنگین آتش در انبارهای مقرهای گروهک‌های تجزیه‌طلب در اربیل و سلیمانیه عراق  @Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/450725" target="_blank">📅 22:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkyGLxqMkDjkR-O1AkE6fowiXyw-jMTf-W8wW4GTBrZ2FcPblvDxKVylo7mDKjWcJqxPpOEPY7_8SM9jL4G4Qct4SMoWwTykv8gphSOjC1AXsMqd_bnpEtp6uFeYxTODeFE8zuEUW_lAhBEx17jXKWUbf3CxPKzu7UnjODm3TzxukkoqSNa6CXvYAIkfcU_-iNYJM8d2IV1-LIOPcWiH7l8ZZ9HlnC_2tNM17Q5rJvO-OUxyB7nC-U4waOWi104K__wfKX60uoCHiWSaoZlqX1vv2kss4OOeMjbU_9Gl0veRQ-xa-uCwQsjlhoV8WU8C69F1uZC-9lWWYxiFTMH8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو هیئت رئیسه مجلس: وزارت علوم باید درباره پرونده دانشگاه علامه پاسخگو باشد
🔹
سلیمی، نماینده مردم تهران  در واکنش به خبر اخراج یکی از کارکنان دانشگاه علامه طباطبایی پس از تذکر حجاب به یک دانشجو گفته: وزارت علوم تاکنون در قبال این خبر سکوت کرده اما باید هرچه…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/450724" target="_blank">📅 22:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450723">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ77QS2JOnCF_aQ4YiZPl8oqsLM1lMeAGBHtBWdg_ljA2ur1DMDyibpHjm_slaDLLMRjpmDxyYtEP8xU_5tNCUXGdgl76wmp2pp7yGl8KNphTReuIsI5WFRd73qIydx4zZso9Wy_ml7PwlCL3eJyyJyWoWW5mCFlGM7dkjYCdX91uEHrxJ2rwQLg5L9V_PGhRS2NqNXtwXiqSG2FuuWWKvfUNTEMomtl8Yf5VVeu_aT6Ww-o85ZOKeHuZOsIqLgTra6vxYN2L16w19-KprnRSWbNyZ7WkeK--9CE8IRFEbS3BXcWtSd4VZWDDC3UwKZi6fl03jxsjTev2pN9pFDn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📲
واکنش تند بیرانوند به صحبت‌های علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
@Sportfars</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/450723" target="_blank">📅 22:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450722">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎥
حجم سنگین آتش در انبارهای مقرهای گروهک‌های تجزیه‌طلب در اربیل و سلیمانیه عراق  @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/450722" target="_blank">📅 22:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b25a6150.mp4?token=aNb_64x4eA1rYeX_OzBRpLmId_W5vxSDoI3Gb0IjYr8aUxPOs6HFBWqYzV69lA2POaiABFOEajStwvGAKTpC2nhS7JTp-w7bxL0uaLoKVUHiNywMhLd1pxOpGWCsd9Yaxdo31Dz86XdRmIdME6ebcn9bfEgut0TiHYRCl9TxB-mp79HQWx3CF216SyQQyrP2fcYpyREO52nawiJMpUCzp1DAX3AnDlbsNa8-eH73balShWn34sf7FQg_H1wuDm_8cHOXYAuYldAIPKX49e72meO_Q-AJbrZJPCohA0gEbKMXgkHcjVwzPP0e3f7ZC_4CRpt231SBtbjTzEMBhTUWUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b25a6150.mp4?token=aNb_64x4eA1rYeX_OzBRpLmId_W5vxSDoI3Gb0IjYr8aUxPOs6HFBWqYzV69lA2POaiABFOEajStwvGAKTpC2nhS7JTp-w7bxL0uaLoKVUHiNywMhLd1pxOpGWCsd9Yaxdo31Dz86XdRmIdME6ebcn9bfEgut0TiHYRCl9TxB-mp79HQWx3CF216SyQQyrP2fcYpyREO52nawiJMpUCzp1DAX3AnDlbsNa8-eH73balShWn34sf7FQg_H1wuDm_8cHOXYAuYldAIPKX49e72meO_Q-AJbrZJPCohA0gEbKMXgkHcjVwzPP0e3f7ZC_4CRpt231SBtbjTzEMBhTUWUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوروحال مردم نیشابور در ایستگاه ایستگاه ۱۳۹ تجمعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/450721" target="_blank">📅 22:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450720">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djoJfBW0q2khELhkERSZV143iDqthLa2LqSrVgVtlHPPnadm5JAc6Nl_SmUmiLA_ChTEzhdONycmIk3ciY2OEkX6qXX4N1lhxWMVfLf0j3WdapEWjnkpUbt92JmIbNmnhvRePAGNi1TKeEhGOQf487MaTBr1bPFcnb1VDZHUQ1_Yf0UkR1IlAHGSF65dYfzEOjqpCk-rF5vsXC8pYUaikg5MejpWl6qGOWnw83mpliRjTZ0ef7Vv4WwF42g6i_Lh9KCHMLey9zfyCsEV2FY5H9Gj1FvbjP9jx4SNbpfs8kobDqswyfuKpew_xlyqrG16v7RU7ymaTaUKA7MqaU4aKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر ۳ تن از شهدای حمله آمریکا به پل بندر خمیر
🔹
این ۳ شهید اهل روستای نیمه‌کار بودند که درحال رفتن به منزل خویش روی پل به شهادت رسیدند.
🔹
در جریان این حملات ۸ نفر شهید و ۱۹ نفر مجروح شدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/450720" target="_blank">📅 22:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450719">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22204aa445.mp4?token=s9HDN5LDct5Unn2Xk6qWLrLlfia0UOcYklK9rIdqn9-0QklI3HapPWbMuGSnXyg30s1lOknfEcPYV63QCL38OLWHsH5TM8HhYoykVp1WR012RUld28OX8orSB1kqx0rzM_R-zT65FM6J5heAfGxlz3vJkwpjBcCk5onGKCO_DfnU9X2hdcD-DG_cbYMcPVDrW1u4c-csGgzClqzZxwUfSrT7nQae5oY6O_I5oPxBb2mrBrwpQTm4NvwGS6f0o0QLn0oVgDDAlosSQ8v8dNhrnNgXTzQ8MzIl2ifPhj39LCQaJ7FlvbZgk3vwpAxEdr37Mze-A9boH63kUlkZ6jgXNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22204aa445.mp4?token=s9HDN5LDct5Unn2Xk6qWLrLlfia0UOcYklK9rIdqn9-0QklI3HapPWbMuGSnXyg30s1lOknfEcPYV63QCL38OLWHsH5TM8HhYoykVp1WR012RUld28OX8orSB1kqx0rzM_R-zT65FM6J5heAfGxlz3vJkwpjBcCk5onGKCO_DfnU9X2hdcD-DG_cbYMcPVDrW1u4c-csGgzClqzZxwUfSrT7nQae5oY6O_I5oPxBb2mrBrwpQTm4NvwGS6f0o0QLn0oVgDDAlosSQ8v8dNhrnNgXTzQ8MzIl2ifPhj39LCQaJ7FlvbZgk3vwpAxEdr37Mze-A9boH63kUlkZ6jgXNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: سیاست هم مذاکره هم جنگ تمام شد؛ اگر آمریکا طی ۲-۳ روز آینده جنگ را ادامه دهد وارد مرحلهٔ «تهاجم و انهدام کامل» خواهیم شد
🔹
در صورت فعال‌سازی این راهبرد دیگر به مقابله‌به‌مثل اکتفا نمی‌کنیم و هیچ مرز سیاسی در مقابل نیروهای تهاجمی ایران امنیت…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/450719" target="_blank">📅 22:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450718">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=sWYH2kUET2z820HtPMY2uQhFtKAE3whQvHyXu4wtWRMUHo8rcE09rQk3hXPv-qtCxvIQiBK0kjSgudq7uZrweAELnh2xtF-GuXnoro7dDCDBOHGDT_JF0y8XzY2QAApj7xdKY_jSLOr2u9FfXIVyTKy1k7-mZuYXG8zCLvFtVuxdcIlwQJWBomEj4AY78n2vEMs3IRnp6YOQbBeRlcGcOlfxD2YOeOlb94Z7n_pfsWQkzBIBKVdr_ATp-n-7enAWJ29lgq3RdnL0ns9fMcMWI2SrZJg1efbERxUXXSBeHvxVhOEvSYKzIz7yLQgRUh-2e_4Yh9UGufMqYnRTTC19wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=sWYH2kUET2z820HtPMY2uQhFtKAE3whQvHyXu4wtWRMUHo8rcE09rQk3hXPv-qtCxvIQiBK0kjSgudq7uZrweAELnh2xtF-GuXnoro7dDCDBOHGDT_JF0y8XzY2QAApj7xdKY_jSLOr2u9FfXIVyTKy1k7-mZuYXG8zCLvFtVuxdcIlwQJWBomEj4AY78n2vEMs3IRnp6YOQbBeRlcGcOlfxD2YOeOlb94Z7n_pfsWQkzBIBKVdr_ATp-n-7enAWJ29lgq3RdnL0ns9fMcMWI2SrZJg1efbERxUXXSBeHvxVhOEvSYKzIz7yLQgRUh-2e_4Yh9UGufMqYnRTTC19wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: آمریکا دنبال این است که همراه با محاصرهٔ دریایی مقاومت ما را بشکند
🔹
آمریکا یا می‌خواهد عملیاتی مشابه اصفهان انجام دهد یا سایت‌های هسته‌ای را دوباره بمباران کند یا قسمتی از سرزمین ما را بگیرد و بعد بگوید بیایید با شرایط جدید مذاکره کنیم. @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/450718" target="_blank">📅 22:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450717">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc787565e8.mp4?token=dv8GqHqg7r9Hka9t55-F-uz4TuiymmYXlUQ3x8RkDDi2iis3f7q1sLBtI-6o0Z_bXnIPCrJ6ZOPqYgUmpA13cmJ80XT1lkApe5dj8Y7-ohSPrY008Aha3vVKsxHRZHTQeVNAVmM-uiPieWn0jBdvGr_G3-Rx_ZBKEo60c6hXsMtguNByQney6EFpEih5cTYpB7m3SGXt1hTBTzhjYf-eocFehOtxjKufCMNR-p3RYrB9g7up5Xy9GnCd4ouyRRDcuKRX7qmLAIBma4xZxl5pTuAkM2-y92FhaedMHoTpflXuYlYc1DLFeoE_8pD_aNAGzbIA_3PkHKt9p7CNzrKzgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc787565e8.mp4?token=dv8GqHqg7r9Hka9t55-F-uz4TuiymmYXlUQ3x8RkDDi2iis3f7q1sLBtI-6o0Z_bXnIPCrJ6ZOPqYgUmpA13cmJ80XT1lkApe5dj8Y7-ohSPrY008Aha3vVKsxHRZHTQeVNAVmM-uiPieWn0jBdvGr_G3-Rx_ZBKEo60c6hXsMtguNByQney6EFpEih5cTYpB7m3SGXt1hTBTzhjYf-eocFehOtxjKufCMNR-p3RYrB9g7up5Xy9GnCd4ouyRRDcuKRX7qmLAIBma4xZxl5pTuAkM2-y92FhaedMHoTpflXuYlYc1DLFeoE_8pD_aNAGzbIA_3PkHKt9p7CNzrKzgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: هم اسمی و هم عملی دیگر چیزی به‌نام تفاهم‌نامهٔ اسلام‌آباد وجود ندارد
🔹
اگر مذاکره‌ای آغاز شود پیش‌بینی من این است که آمریکا می‌خواهد تفاهم‌نامهٔ جدیدی با اصلاحات جدید بنویسد. @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/450717" target="_blank">📅 22:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450710">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3or04aNEQiP0hIXpTfgndYCKAeShCF_uovF8DrEudlycreMoFWkxRcx5969Mx5rqX78nv_9tCxRs4OrT0SUqIVtzWg85Hoas9cqgEAoChtaDrHTFy2YyO67S6cHmR14jwWVkiCy2D8dW4VIXbfwrhwNvZfRqJ-lc3NAAPHlQChTxnRYb435hJFAyLjO5rkwXmWLjh1KftkSR4weXcpecdonaozBxKpaadADHxAeSPiMNnmmsXQRAvgV4gX9mfD8bm9TYWyJBv_9No3vCtOf_eG9BudlVDlJSEovstBlKi3tf_eUVKfgHjTe8N-jcdCo0cGITZEx_TeLGYvH5xqfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7SR-0brbEEvmWIXIFxzDKYV9eXw04PwbKb4_-Rpq2Ee96_cjQyro9KHyBDGMMd542uea15gzfjG8Ym8YvFPWMJg5Uea6VZ8rgPj5y_8FddmnQ542C26OtFy8o-TajUhQ5R8JeE2UWT_-9dHR0nipg7q4d_nD8BKiF5lE2k_nRXn-apOUE8CcKGenRJg0AOwJDxx6rMiEI42zfYxR8TcOx7F36dZanhVY6wJz3ZlV1M35efy41jfvQC8B_XcnASNjA33Xq-PJ7yZ7RR75xg5yPpc8WgJ61k_sv4I5tL24DN4S83nhluLouhmuT78o0Bs5Tfv945Kb3lYPru5U2RgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZkoM8dZfmaq1EWLdChfkr9vH5uEYoEkfSpkcz8eFuHZX8tpyXsXPrlfuX_7f_LJrl4CryIYYI1nwh06gZxIXjxLbd_GWHFc79H27oqL3XP663N59XJGhFRab3euV902GyNG4fp8JG8KKEDzqs5wE2-3epIpmiZyxm25kVm7a8gD52ChAWK6rj84HivdSa4uUHIKrjUuFWW8OHtwf2Nrh2XwG1-UCOS31yIJ8nb3T-SVYTemJyW2ydJ8-cl6GhnwtIQ9F3C32VWp75riP_ph_cF_HX_foMvyIouob4m6cs_gyYswHfZUvSch3wNvRWHE-YULCz4h8JEaCn_sL9WEoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQ2ibRv8nC9-o9GIcgUMwCOmXcsElN3Uwq_h5m7IcPQNmg6EA54rSiwb3pkv32riIUhjXfY1PwvhzY53y2nIVaQKRTiWwBKbpFlB90Ech4onTqr1L8u7amSkoFVdPtKo1GvbOxH7fYhwraQwBb0cNLNyJwpkEttz_GyDf5jxxW1aWwOLXdaBD0BDsWe4VKq1oT-Tks_nCAmX5pca4YGVliQHH0Xz42YKSwwxOwDKx4iLZe0K6dAnbmdjWX1M4D8htLJu590Bt81zsNrnGh3xCcdQhS7IgQRNWNRjZk2-KZ9JPFhA1rL2zOiS9XEzKN4fihHOG_37JLJ0H-9nQTJEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qi8BGGcRaC3HNvnNLoKdJv__iIQrH7Lm-ByeAMMBmdiFg6kjcZwm_GVvPHCXyPe0Vud8nPZUGc45m-h-PfdioVGkLOPvuxuGegmVue-cemaMBlmsa7ikjXCtjUEyqLkcVkrWvzBZ367NJ_VB_sM_OIi5QggUiNmqVD6i6eGti4sfpmtTiUlyiK8SwdtYTAqrxXrp6nbf6BigGOiCTafw5gNfqjh6TSDZ7eRlHjyIvELTWl1UffyikgDhbNDzVf-vIVtvxNxvD0-W4RoydkuteEH6vVuZLyI5elwAUWHrgyWhnasW0Yv_kU7jbK4HtCAKu-tc57mluy4iJaFvELg3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a6axa8RbPUrY9DWGREdBybvhK9b1YZeDbBHBW4GooZU3Hc3l_C3WW3BdZ6DNB0UshRMJhZyGk8EXxV3MMOmUA3DZsEzk76pGpGHyP-BN0VhhHlQHSi2eJxwkV393ApikXErmCkGapbW1n0VT4_BXrjj1isRG8A8U5a0GgOpeU3ApenQuGmxhlDMDz1Ir6KyZnLRFEb8zokrC1A7DAwc4jIGaQyuZhimUnduOdSJt0LCm6l72sPTeZ5gL-aWAG9DLzOCQd_YzbfWCRCxAeFucomwZH1OYMKH3ye1OYMhIGs4vwgIe-ktJi68GE7xq_QWkVQz8h0qHv4LUKtSEH6z0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gr2hQOqJ5iu_fN6Kly9rnvhdtOc1A5U3kIVevtpTO7int9U1ivxo9Q4Ss2Hzjgv4Hbolzkkg4YicrTBan2YUkvL35aG46ngwlzHdC4__F7DeWLQYuz_2GzNpYBkp6cdNZJEDTKC7M_LDqgMIxlTptgvcYG2uRhS8njb1EukugtGbZi433jUz7p1PR7ro3ZY6g_vgornWaZFL3Mmxi1mSlbjzMOkAINmhqqL97Z5Dx1jb7N8QiuMZckelQKQrB2knTcLtq6hAsSsrC2J6H9rtKe5aKPPPpvigN19VByHuL8HDcRs-SJdL6z-g53A8zU9IhdxT19lahMTxFlD5zwUYOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگ‌ترین سفرۀ نذری در زنجان
🔹
مراسم بزرگ‌ترین سفره نذری حضرت رقیه(س) امروز جمعه مصادف با اولین جمعۀ ماه صفر در زنجان برگزار شد.
عکس :
عرفان تقی‌بیگ‌لو
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/450710" target="_blank">📅 22:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450709">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e9c748365.mp4?token=ElFpGdyTfAvOIe-G6QHISQ2tksmouvcxjQ3VEFnYBsbke77u8I6i4WoIc-_G7nHMrmpVY8sIH-rsCbKFzIAySmYY093_cQ3kzpsvg9_XG8zHoLTehd2EuKLla_dTefU13RcMvxslvcxEPZOPiU6-wYY3bRDdxW0njc54v6TfECjz5Dm9UOe73OfH8-Dpd9F47RFgglp3TMSw3PZJEyQoHdvmeKwChTcWMZ1rTE2rkSRaqJSL7Dma4s0BiNxXKFWXjkuFdLLhZh3LzgQXU0PMX8HWcygvhqpeheC2hdhtQWtwcu1wCtTkUtSzRpZ-AOxkW1t6hskdxshfbFGxYtg6yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e9c748365.mp4?token=ElFpGdyTfAvOIe-G6QHISQ2tksmouvcxjQ3VEFnYBsbke77u8I6i4WoIc-_G7nHMrmpVY8sIH-rsCbKFzIAySmYY093_cQ3kzpsvg9_XG8zHoLTehd2EuKLla_dTefU13RcMvxslvcxEPZOPiU6-wYY3bRDdxW0njc54v6TfECjz5Dm9UOe73OfH8-Dpd9F47RFgglp3TMSw3PZJEyQoHdvmeKwChTcWMZ1rTE2rkSRaqJSL7Dma4s0BiNxXKFWXjkuFdLLhZh3LzgQXU0PMX8HWcygvhqpeheC2hdhtQWtwcu1wCtTkUtSzRpZ-AOxkW1t6hskdxshfbFGxYtg6yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: هم اسمی و هم عملی دیگر چیزی به‌نام تفاهم‌نامهٔ اسلام‌آباد وجود ندارد
🔹
اگر مذاکره‌ای آغاز شود پیش‌بینی من این است که آمریکا می‌خواهد تفاهم‌نامهٔ جدیدی با اصلاحات جدید بنویسد.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/450709" target="_blank">📅 22:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450708">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xzv2ZepON9Fq8b-XWMOObSp40s2IeMfdB1nd-HiW4O8wCfi33VYs4Fdg37KoiodY9fL7TQpVPoCn9BiCnWc2SHj45QSgL0JbjdIjJEvudi7Iq9PmHmFQ5gHlKw2rlPFW3wH0uv-s789nGuksJ4oQIrdbSpUQMEkj2pqMxenMsLjUKkuhEyEIT1O0fJNXnjme0ay-gNefXatyItc9LwqT3svJrtB_QyeKRqgSA3QyeseCKpBt8s5Hxo0533PHyITwt-J3YXhlYahWq05Q3U5KVEdG1fWmpxTMsrpG3JSKKYHg4IYAH_ljLLFQWk02ixfYc-HkpQKL8yFaOi35Dx9zCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت آمر به معروف از ماجرای جنجالی دانشگاه علامه
🔹
ام‌البنین کشاورز، آمر به معروف دانشگاه علامه طباطبایی، در گفت‌وگو با فارس: ماجرا از تذکر حجاب به یک دختر دانشجو که با لباس آستین‌کوتاه، که قسمتی از بدن نمایان بوده، آغاز شده است.
🔹
این دانشجو جزو دانشجویان…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/450708" target="_blank">📅 22:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bnp7ujigom9_bk4qZXnTZcjVsz3qdGdMIbvpOJewLuM92f9RMIQlE--WtojpZzOrvacY5RhX9_erMp3hocc1pfX_IeqfWJ6Grc29ZAwIJAeDjbOjMrX2Bk6nQUpyFK0-C5n25ALjBBoV3ogQCjXYDyunvb6oJah8Q--58264cFz5yB6DW85NTA86cD8yQPBeBI7AlBabfDpWFknLldxDKVHpLrAOmcwGIywJc132GvBdTeRsCshpEqLUovso3Xv9JP2de_rGb2actRdu1hB0B7YJQDX9U5j5qffrOIgYXsBitg0mDU8ZZQe87XYa5rvv3v5gwD9rgLfOuUWoayeoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWdijb0_x3dlTxiJJ1hgaf_HJubV-8uAxfAyIWQWp9jhHawI2VHBI2_bZueGaYZS6K8C3PueYgb78W49uiI8ptepyxdTDbDnndAQ3QD_Xyq2ipclH6JEVG8vOWqVmzRbJW22itnF9JK6_6FdoAbbTRwDaJxrKS51Hlfm29jajY2qQvoIZyYzg9c_Et4jRp-Z7EJkq5eeMoZZL6WKOVwFK8w6vfyvtcBRefUjHZ_GA3rrE2BKwRYoaOglTISyBgBa1hbip_WNgQUU39XeQcS3CHUGUd6aC4olRFKp-7hTu62gAT1LdpddG30Ynr_Af0NiaXur4c5MDeiekJ-WDC98qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mn1H7OwoT5xwl4a7pZcNGNoR0BsGGGFuzjjHO2cPSMh4nTLrFaJRf5WSBz1zaEKphltKm6j7bsA9CcXbf6LsQKytlYEmZWl1N4KjGHD6wK5bPn1yN0NVDtVMciret-QFNm_6WVxjkls5D9fb_50cWxf3AVv6u6RL9-A4cmF0HvJGt5Duhi1dIPyMWx0yBpouaIMxjTmQs8oApAFXF-RuY6Yjv4ZR74g-66sSF-ymrf2oYHIvEmR7ywNQbcO_2OEGhCwCXG4qiplvRYZVGF_VaJf4625rHEsAa7DYORBf4KU0SdfdW_cyZ4oQ1Yn4gbr0Lh6txgLHGsrmAtAxxAEABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjTkHUOfysJLgrqAeKNolqHq30RjgCEMQFHSkOr468TXx_CWK_-h6W7B7KWUwG7glQPEOAa5oruB9gp3vhySkiX9KRAog8yIilCjUVqUfUsU8lOo0mktG1avsYMbYw_Y-SGc-RJGKjNQBKjkU0JsKl0e41YYLZgdc9ZWMFLdb78HiCPcspo5hKmisehRIWVYfhtZqi38GGRzIZZ6YDnc-fpxBDnxWMfrKQkdaYUXeYRCS-qAk38--4SiKX2gm2Z7kD9mlwb2XLQfL-b2i_KAcJCFR4hfJWm9m8kA5Mfbn9nEeXLEVaxJpZXzGrBxqsiJwKVVZR9AcpztfupuXTzGxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJuMBWKfhXxHERxTpVlo-22QTYcS0svZDgzP6ELntwlvQthmU-Qu6qq2lv2rsAvS4kX9v9Zh_1dxdRtZ1aJ4M0bIXLbEO4knzn6_M5-hXH-qeyWrlAEHD9kwXd-0D4smSC8Tq3L3IQoq-ilz8k88EWqq_Irjb4wMn9IOLBvk2f3ZgxMdJJpzHW5VZyGIHhkBMseFS_ppwf-Tp2_xgoMblKPdkh_DJz7qVbftZiWh1ahyLpWbM0JbPBcr4h3CtpiaPlzasAG_GMzOlf-Zbn0DpdG-aJkHS7xy3_qZTIGIbfq6mNglE2_NHnZL22VpDlvF3TlNQHlAlg9p8gE8rSwvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uS32m2-kTv1PP5i9pvjib7gjzSjuIQtO6vnkpwc8jTjBUsubCgoRWFJezv2hArrxwWsTRkYxhKei8Il0DIjRBefVobzCXBr3ZssE0LLplsThZGWdSEF1L38Ft5pvmVZ22kBKNYcMnWg1ER9pJifxP4DyKbWTxK_jPsPXJQupbimV7ZwFwvv5vpMOLaJtw2gSg1XxWMcr9J8bUVNM-tInOPoFnyFB5hcJ3QDii2ZtbaQoeVrjJGShw2dDwbuiSScJfZXth-XAnleoDjt6bo_3RcPi-l8FC2JQWKXPkJKjbt9O_0RJM6TSYxswnaEQN0IgoUgCrB797CxKdGDIsdHlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzGnyBnbk6mUKWplM8hI2sPAj3aNKwM27ErsUlebT0SgtO0Z7AyhbXS-dlVqCX_J9RAJkDPZMEjZqNMAvwmBUhZ0YFw4ifkpLRiUGrAV5uUSvQMjD8yJdtgrk6CnwPB4YTHFLNxfInq86ZO3XmGYVCBoLA0I_h38qEVs0hZtbqmrcHfY7f1IUfRzTWrps3x5Hi8xfz_GBAQtLzpS37EWP9E3_Kyt0Iq-U2fXU-jNrU7N_3I3yVx0-p7EKUvrwfW7_XE4kcWQOEy4hWjtgrSkqeuteQOmU04NouXuO44AY0zaardUmdTP1S3EixIhA6zDTr14u7qpmuXHg_z0PPmo4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اولین سالگرد شهید حاج رمضان
🔹
اولین سالگرد شهادت سرلشکر شهید محمدسعید ایزدی امروز در مسجد امام صادق(ع) تهرن برگزار شد.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450701" target="_blank">📅 21:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c71764ae7.mp4?token=haraJ5QtKr9GwmGiZrgNtZT0V4LDS4pMRlgQzVn7U0Uw9od1LjnWLfaUN_hgunVuHsC179c7KtjPHj9oxIygi_bg6NLDpLnTupQ8OwqXJsr4WA30OXT4FXlNMZlK0BKgLrZywztyDD_ilWAOSCokAmgedHq5raaT4ec15pE43-Iv8jYzav5UurIGzs1iL1b-RbsQFyIuSf1OP-48q4R9uNX25qyUsi0bTUkqQFYwqIIINChkp0TE330ELJ7iS_J75XuloXVHD_NH85hxxtpnUDuUv9pFzZTrL57iDyLSimOyzgQSf9vVglgXNoHL7pMOUKYm1DWdHVl0IJQfnbo9b3T1C8FzpULhwPlgDA4EvXKQbZdcEUqigghxNwcb7QcKsbVZUExO6b-4vizj8-B33hv6T95-9EWa2LXJqhbJYDcGF9wX6Ok8eEo65ol_mPntx9NvmcKBDeGq5tz3oqfve1XWwRd-sR6YD2yCA5Uec9bB0riXmcLsX_cr5vWsy5sBcB_ioiwY4KuxdAiXBFKte-2v2DCPqXJcY0A9GJgOqnkMGxddPxLLsF52E1LRDr-T_e7kIaFTcwXFG7-n8ZkEPP9uW6WQ3xU7eB6KBEcBFdAaoUDRCoivnGeb4RWF5TyjTFXjaQtEas4hXzh3zoq1IF3x5WKz8Veaid2v3leb_eM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c71764ae7.mp4?token=haraJ5QtKr9GwmGiZrgNtZT0V4LDS4pMRlgQzVn7U0Uw9od1LjnWLfaUN_hgunVuHsC179c7KtjPHj9oxIygi_bg6NLDpLnTupQ8OwqXJsr4WA30OXT4FXlNMZlK0BKgLrZywztyDD_ilWAOSCokAmgedHq5raaT4ec15pE43-Iv8jYzav5UurIGzs1iL1b-RbsQFyIuSf1OP-48q4R9uNX25qyUsi0bTUkqQFYwqIIINChkp0TE330ELJ7iS_J75XuloXVHD_NH85hxxtpnUDuUv9pFzZTrL57iDyLSimOyzgQSf9vVglgXNoHL7pMOUKYm1DWdHVl0IJQfnbo9b3T1C8FzpULhwPlgDA4EvXKQbZdcEUqigghxNwcb7QcKsbVZUExO6b-4vizj8-B33hv6T95-9EWa2LXJqhbJYDcGF9wX6Ok8eEo65ol_mPntx9NvmcKBDeGq5tz3oqfve1XWwRd-sR6YD2yCA5Uec9bB0riXmcLsX_cr5vWsy5sBcB_ioiwY4KuxdAiXBFKte-2v2DCPqXJcY0A9GJgOqnkMGxddPxLLsF52E1LRDr-T_e7kIaFTcwXFG7-n8ZkEPP9uW6WQ3xU7eB6KBEcBFdAaoUDRCoivnGeb4RWF5TyjTFXjaQtEas4hXzh3zoq1IF3x5WKz8Veaid2v3leb_eM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر ۲ شهید حمله آمریکا به بندرخمیر در اجتماع شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/450700" target="_blank">📅 21:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivwPY6sjYtn7lu-gVH5C8AcbvlIPVpWsw9TYE5fE2Fo7dp3NVre4D_UuZZnMhaIEz2dkzMInH8IpJBRRM1w5Ghl7L7uOltiZKiHROgcMUscXm9A60o0YKcYB4cPoanSStMdEnUyt5syxQTluNTbqf51dhJG4ewapO-NTSHG26Gzh6jHdefOUD1R4bfyPqFmdygdK6QvJJ1xxQn9qEBnZBTNjjmoQwJkk5CxD_NgUo0FTpF3uWHAD1oRLkl67TbudULcvYwVMGFuM0Xwa3tzuWZXPrMT34nEZwFKejN64P9ETC1VU-rJGeVchvNX1d4gBOnghYIq9FnQoJubnI8A9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت نفت ۸۸ دلاری شد
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/450699" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2718c3b5b8.mp4?token=V1oV2GeH9R3ex0kwSei8Y9QsEp4V9bF17X7mf20N6kxH3BB6NWKYheMiVxLLmpPodnWHKVmN6sqEgASybYnH7Mt3pao9iplnllHC3JghUu4IxjBbdqo8vBk3tRTNlW_xgVrhNj_toNKJBhLdXsUvOh-ehOK-yf1aQdbgmlAxmzB8yT-crcPyG5_2YjaXsKAOL6_4Uzyj0AMwvfxubkSbRUm8Cw9EemfHbv95mErP_yJHOQkRCbyA3nCONpfmtoC4X-AxIapZ5a1Ca5yT7aNp9brXyLk-screkLfhXRRHYz2TpA5cflBHPOO86FfEF8ZoGBidv8kKrRrqCcm-ccA9czzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2718c3b5b8.mp4?token=V1oV2GeH9R3ex0kwSei8Y9QsEp4V9bF17X7mf20N6kxH3BB6NWKYheMiVxLLmpPodnWHKVmN6sqEgASybYnH7Mt3pao9iplnllHC3JghUu4IxjBbdqo8vBk3tRTNlW_xgVrhNj_toNKJBhLdXsUvOh-ehOK-yf1aQdbgmlAxmzB8yT-crcPyG5_2YjaXsKAOL6_4Uzyj0AMwvfxubkSbRUm8Cw9EemfHbv95mErP_yJHOQkRCbyA3nCONpfmtoC4X-AxIapZ5a1Ca5yT7aNp9brXyLk-screkLfhXRRHYz2TpA5cflBHPOO86FfEF8ZoGBidv8kKrRrqCcm-ccA9czzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات کامل حملات ۲۴ ساعت گذشته ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/450698" target="_blank">📅 21:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de649e10f.mp4?token=uCfOng6qgVX1JRnvSsGQ72Qxx5kJZKZz1LQ16Fh3_m0Bwf0c39gC6lz3uqamto-7gNJwPINyDaPA0fA1BMGDY_1r9Rpw6BVwzlcby4Acsbtn86SZItyc7KEnkQxyB1VC70f_AVRcClBUqeEJwTzTF3YjV0Qrpy-6LPm_xFRhIJ8IJHDlQjpYbdITymCZsSQyoMbzDjxccSS2dziLrQyIFS-1iKV7ASAZeUimHoAMWefOgOovEO007fv9rCwJL-aEusfuQUorXaGQFmTvweopGFsdBFM4czJMcVIhp8DJYPKrHDnQ5vI1bCaW8slCdDYmUbxUHUvQ2IaJsNYmg1-4vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de649e10f.mp4?token=uCfOng6qgVX1JRnvSsGQ72Qxx5kJZKZz1LQ16Fh3_m0Bwf0c39gC6lz3uqamto-7gNJwPINyDaPA0fA1BMGDY_1r9Rpw6BVwzlcby4Acsbtn86SZItyc7KEnkQxyB1VC70f_AVRcClBUqeEJwTzTF3YjV0Qrpy-6LPm_xFRhIJ8IJHDlQjpYbdITymCZsSQyoMbzDjxccSS2dziLrQyIFS-1iKV7ASAZeUimHoAMWefOgOovEO007fv9rCwJL-aEusfuQUorXaGQFmTvweopGFsdBFM4czJMcVIhp8DJYPKrHDnQ5vI1bCaW8slCdDYmUbxUHUvQ2IaJsNYmg1-4vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت دقیق پهپاد تهاجمی نیروی دریایی سپاه به یک فروند نفتکش متخلف در تنگه هرمز
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450697" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2480db1ed.mp4?token=seSqve_2-d8Z4hq_E698v1vQFdbYrIfQEJVkDSicov1-b4xcZw7VoLMqBLKUy6Dtqz6gDH-W90lKPo8fhK5pTuaiieLATmw-4jpV2kmt3r2jkYsQQGL824Hq6NoC_GQBVYJEI-LIZ5RtgtlzbB6donIOiCgpqrkAent80j-VFyp6yJmSPerAO6PSDSchLYw9w5z_MEVEhr0vxPnznSHXoj_rjk_HKbln0VdMXaZurr9LZCGuJlpJNZdrTmjbNi7cqo-RHaqAzukRBCnpaWgWJtObnqmKLYcmxyRU1PwRE9saGB86uCrw_71VmHhzcQLrs1VlsSY_YKy4tgsNkzRkBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2480db1ed.mp4?token=seSqve_2-d8Z4hq_E698v1vQFdbYrIfQEJVkDSicov1-b4xcZw7VoLMqBLKUy6Dtqz6gDH-W90lKPo8fhK5pTuaiieLATmw-4jpV2kmt3r2jkYsQQGL824Hq6NoC_GQBVYJEI-LIZ5RtgtlzbB6donIOiCgpqrkAent80j-VFyp6yJmSPerAO6PSDSchLYw9w5z_MEVEhr0vxPnznSHXoj_rjk_HKbln0VdMXaZurr9LZCGuJlpJNZdrTmjbNi7cqo-RHaqAzukRBCnpaWgWJtObnqmKLYcmxyRU1PwRE9saGB86uCrw_71VmHhzcQLrs1VlsSY_YKy4tgsNkzRkBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانباز یک‌سالۀ ایران در بندرعباس
🔹
روایتی از «میران» کودک بندرعباسی که شب گذشته در حملۀ آمریکا مادرش را از دست داد و خودش هم به‌شدت مجروح شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450696" target="_blank">📅 21:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFpyVDAzsBE_LQs82hCDMASsGjeSQaD3rvHIqCFF72o9Jrjc9j4_uM0OHB-LOlNTIqkJIMzKI2KoUFX1a0USIvpVR1-Ggq9rCS7BQI7adxFpsEBx6E3cFKqeHrNZZmQFFroiiN4IvzoQLTEpaTvlKkDwPZBjOCcQVczJ74gXn0GhAt_gOcKoywli1sxpTssmwwCFT6zXdBkV4Bzic9evuZ9JJWd-67Xsyvze0AW42av1YvAxoBQv9ChsotLhR-cF8ZxruLM8AypSBMUuVuDyWj_2lUWNbt4cBdJ595yHrUETUnBgmLvkzmqNNnmKPO3ikxVlca48bRBPmKoLz31CTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ec42a43b.mp4?token=O1QJ4uP8MrwX-XO3K0LyKude4VkMwqeusUYvU0j5SuBIJns67anwD8L_XNdbTxKlqlc6sExI3gav3GMzSQzsDMnnOcon6KvmfdKa7J4MnRvg_8IbZqgAkr8OdD44IC4X5zX3ZX_U5fnXyx8pMxbfbklA7Q0SMYXrGP_LOqeaZHqa4T7OcqTwvlIQ96YQ2fgkDWQTyIgfPe2oGI1E5YLFoRQwZ_sfQmaqgklsjHS5mVHgBa_epuBkT2q5RnbccF3AKBKoNhWxYPP9HXJVwyYAXpc355wsELp7vo-d9VuK6M6Q9CBJkpv2PdEkrxcNGFy1_WZnz6B1_4W1m5tyjLYVXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ec42a43b.mp4?token=O1QJ4uP8MrwX-XO3K0LyKude4VkMwqeusUYvU0j5SuBIJns67anwD8L_XNdbTxKlqlc6sExI3gav3GMzSQzsDMnnOcon6KvmfdKa7J4MnRvg_8IbZqgAkr8OdD44IC4X5zX3ZX_U5fnXyx8pMxbfbklA7Q0SMYXrGP_LOqeaZHqa4T7OcqTwvlIQ96YQ2fgkDWQTyIgfPe2oGI1E5YLFoRQwZ_sfQmaqgklsjHS5mVHgBa_epuBkT2q5RnbccF3AKBKoNhWxYPP9HXJVwyYAXpc355wsELp7vo-d9VuK6M6Q9CBJkpv2PdEkrxcNGFy1_WZnz6B1_4W1m5tyjLYVXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجم سنگین آتش در انبارهای مقرهای گروهک‌های تجزیه‌طلب در اربیل و سلیمانیه عراق
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450692" target="_blank">📅 21:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450690">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcjdBUZpDbI8h3vhFqAgAaWIKrGgu0Y2pV-f9sr0a32JYX-eGPngAEKo1eb6Pm16b9ar0oTPYvBTJE5HR339oY7ka94h4-A4EM4LAKrLAZL5pGC-sOJFYFSp9zr9vRvFOkAeR9Dq4eS7PlbMms5-FM6fzRp9AefoSH6ZCaqZQeyfdZ41X1Dx79IFcGPR6O8KxrlMwlYOg-hGsg8AQot8hbW1EVG7X6yKDUfrAElTqpLw9d0oKrwLZ6bJ4AGL08FzraSn2Cb7e3uply8NQXuEdPFtlpVPVUMmKpfAD0FVcF7kOhnMnbfnTo7uaOR6o7kaFJbI3kEHscShUBvAMwqRTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شورای آتلانتیک: باید تسلط ایران بر تنگه هرمز را پذیرفت
🔹
کارشناسان مرکز انرژی شورای آتلانتیک در تحلیلی نوشته‌اند: بازارهای نفت و مصرف‌کنندگان باید خود را برای احتمال تحقق بدترین سناریوها آماده کنند و بپذیرند که دیگر چیزی به نام وضعیت «عادی» شکل نخواهد گرفت.
🔹
پس از شکست راهبرد اولیه ترور رهبر و فرماندهان ایران، کاخ سفید به دومین گزینه در جعبه‌ ابزار خود روی آورد؛ «استفاده از مذاکره برای خروج از بحران انرژی در جهان».
🔹
ترامپ گمان می‌کرد با استفاده از یک یادداشت تفاهم و دادن امتیازاتی روی کاغذ می‌تواند ایران را از تسلط بر تنگه هرمز منصرف کند اما این یک اشتباه محاسباتی بود و ایرات از تسلط بر تنگه هرمز عقب نکشید.
🔹
ذخایر راهبردی آمریکا و دیگر کشورهای جهان، پیوسته کاهش می‌یابند و دیر یا زود، واقعیت مربوط به میزان فیزیکی عرضه موجود در بازار دیگر قابل‌چشم‌پوشی نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/450690" target="_blank">📅 21:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92ab54e9a.mp4?token=IsUCVaRnr6Z6pre9Ywrkikr9pUXJQq40RNSgnA6Zcq_TKlhE-RuEtEnkfronr7gb8mzJjwHElfa3duttAeer4EV1Kso0sJYu7dHP0Yw8n-6ef_osFtu5rHf0f9czpIlx0KKSubaGwyVR0plRuftISqbwzJoER7s6YxrZahUv-lPVFOGZhkozid89juE_D4JraNYEyFQEh4Gg-LMh0CC4Qcgkd2ntRlGQWVYpE3zMsTl34tf1J7pZj9pXDMwAl64XyOeVBePhtr4oeV2ZT0Uy_ydgb8Pjv0-Mpd5lUJFgGvLPL-8AamEAGZxOEDsR9icHOKxivHijn9gBIRz5ZhlyhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92ab54e9a.mp4?token=IsUCVaRnr6Z6pre9Ywrkikr9pUXJQq40RNSgnA6Zcq_TKlhE-RuEtEnkfronr7gb8mzJjwHElfa3duttAeer4EV1Kso0sJYu7dHP0Yw8n-6ef_osFtu5rHf0f9czpIlx0KKSubaGwyVR0plRuftISqbwzJoER7s6YxrZahUv-lPVFOGZhkozid89juE_D4JraNYEyFQEh4Gg-LMh0CC4Qcgkd2ntRlGQWVYpE3zMsTl34tf1J7pZj9pXDMwAl64XyOeVBePhtr4oeV2ZT0Uy_ydgb8Pjv0-Mpd5lUJFgGvLPL-8AamEAGZxOEDsR9icHOKxivHijn9gBIRz5ZhlyhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتار در غزه، در خیابان‌ها خون جاری شد
🔹
در حمله پهپادی ارتش اسرائیل به یک مراسم تشییع در مرکز غزه، ۸ نفر شهید و ۲۰ نفر دیگر زخمی شدند، حجم انفجار به حدی بود برخی پیکرها متلاشی شدند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450688" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌‌شدن صداهای انفجار در اربیل عراق خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450687" target="_blank">📅 20:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu0IHUHXbveSsQtOW1XLhMCNxcNxeuHMf-gRcvbiXXJBhxgO1UCcl7uqVGMc7siLjRZPRs-EtcYWHwdCyjKmWyxbinD_YkHSi42lIsfvG1hN5Fe8QiCklKzSHarzUSZYySgoMEWMWRle0bcKf_KShUJGtK8oDOm6zxqIDwYjhSxYbc7mznF6pJU2b4O-GBD6vZr-LlwtVSAZlT_gG4SWO93odwRGrfzoBmIKDIhEwVeiKh35ZTFjws4LfwaUTI0Jo4XtUP35M-N-uodle_Tx5iEzze_npy9vcV_keTLbmjbjcwACFjC1gqHloqYLoCWxGtbReq_Bk3BF9GoU0awdDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر ۳ تن از شهدای حمله آمریکا به پل بندر خمیر
🔹
این ۳ شهید اهل روستای نیمه‌کار بودند که درحال رفتن به منزل خویش روی پل به شهادت رسیدند.
🔹
در جریان این حملات ۸ نفر شهید و ۱۹ نفر مجروح شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/450686" target="_blank">📅 20:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWDIX747ZkA_YNB1EaOqgtYpjMdfaAoYIHTkTbyvmAtmOdMOyjjafRGZxxavZbsSqkgDcG0yvC_pL0nBn5jG5pq1yi4mX8eBg0UudYx3NBOICY3qR8BIEWpTJy9NqXazWHLnfAe-l1iE7scknw2dl0cDDUtZolXsqoX0vaai7YYRuzzX2N13_X4k5VbAQeTdy3p9t3Tz7ZP6ItGQhUnAU2HNmw_wgcLhED-_oLYMbLN0IyH0lZw6JRoTPKBsMRDjsAsLKtYIq_8g6ILhIsfCH4BkbaVHqkSRjMXKWY126ics_j4wS3RrpPHCt6ISImKvQJc8nsL1-0n26dRhk7_F8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
۲۶ تیرماه؛ پنجاه‌ونهمین سالگرد تأسیس ایدرو
🔹
توسعه سواحل مکران با حمایت ایدرو
🔹
سازمان گسترش و نوسازی صنایع ایران (ایدرو) در قالب طرح کمک‌های فنی و اعتباری برای ایجاد و توسعه مجتمع‌های تولیدی در سواحل جاسک تا گواتر از سرمایه‌گذاران بخش خصوصی و تعاونی حمایت می‌کند.
🔸
وب‌سایت
|
آپارات
|
تلگرام
|
بله</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450685" target="_blank">📅 20:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450684" target="_blank">📅 20:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450680">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۹۶.pdf</div>
  <div class="tg-doc-extra">3.7 MB</div>
</div>
<a href="https://t.me/farsna/450680" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/450680" target="_blank">📅 20:21 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
