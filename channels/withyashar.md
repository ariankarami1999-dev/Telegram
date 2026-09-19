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
<img src="https://cdn4.telesco.pe/file/Y_pPS72kVjp-fxgM73Uv4hLPJ6HVnl3m5oOD2Lu1hqZaIXDZltJu9Jg8BrFPtPkSCNW8LzjRJegKne6yrWs3fn5ANIZHwE73R9AIZVwd_M_9hZ5uWe01em77Ze2u_4XsBg1p1oQ8FSw67zOhof2TIFZ84Qs1unIGoDeX4tcFJBwING8nSLFpLbKtC1hL2YZDrym9HkWZwDQfXRrGhfaNMR-5wkyiQLnUvCjNDRni3VbKiiSdN-BREUsICpwWRxTamJL4AbgOsgHtTJiqZikTzDh_73u8RL2qp2beGWYGDUyBFPiUGjt7GLpLo8x_pAt5xuGPqFzsKivxKxYHT2X2Cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 21:48:15</div>
<hr>

<div class="tg-post" id="msg-23548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رویترز: کره‌جنوبی اینبار اعلام آمادگی کرد در بازگشایی هرمز مشارکت کند
؛ وزیر خارجه کره‌جنوبی در دیدار با مارکو روبیو اعلام کرده سئول آماده است «مشارکت اساسی» در بازگرداندن عبور آزاد کشتی‌ها از تنگه هرمز داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/withyashar/23548" target="_blank">📅 21:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23547">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آسوشیتدپرس: زنان بدون حجاب در یک مسابقه دو در تهران شرکت کردند
؛ صدها زن بدون حجاب اجباری در یکی از بزرگ‌ترین نمایش‌های نافرمانی اجتماعی در سال‌های اخیر در یک مسابقه دو در بوستان ولایت تهران شرکت کردند. همزمان در همان روز تجمعی حکومتی در تهران برگزار شد و زنان محجبه در حمایت از حکومت و جنگ حضور داشتند.وزارت ورزش از یک ماه قبل مجوز داده بود ولی دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/23547" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الجزیره: ۱۱ سرباز سوری در انفجار انبار مهمات کشته شدند
؛ انفجار در یک موضع نظامی در منطقه عیّاش در استان دیرالزور رخ داده و ۹ سرباز دیگر زخمی شده‌اند. علت انفجار هنوز مشخص نیست و تحقیقات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/23546" target="_blank">📅 21:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94774fe4a2.mp4?token=k6s5or3w3pGBPnxjmAUwTingOo6fv6hgytcbHu8zpqTs3nc3X12aFx7heEMI2cCwYNPAiH3K16Z7ha33yI7vl51SFp6nQx_Gj35QZs_aZE5CoKchqyRquLE8wq6Xv4x50cWJKO6B7SkecCsRmgLYT4SS1HaM2DCq6-YSPtk9RJJvR2HhZ2FXVz0TGnfwpOiNyBHve7xIibAt2oF9uFk8T9XT7OTS33CGJWZYLwr5S_uka_ZshEu_4moGLNj5hQaeWzBxlFARmllPTSgHMh6ueR0A9r4zGzdgoV-M2vDT0VYoNpQTe5a4jwLUEG4wDnv3ZihJPeVe8pUfRkrrajuTk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94774fe4a2.mp4?token=k6s5or3w3pGBPnxjmAUwTingOo6fv6hgytcbHu8zpqTs3nc3X12aFx7heEMI2cCwYNPAiH3K16Z7ha33yI7vl51SFp6nQx_Gj35QZs_aZE5CoKchqyRquLE8wq6Xv4x50cWJKO6B7SkecCsRmgLYT4SS1HaM2DCq6-YSPtk9RJJvR2HhZ2FXVz0TGnfwpOiNyBHve7xIibAt2oF9uFk8T9XT7OTS33CGJWZYLwr5S_uka_ZshEu_4moGLNj5hQaeWzBxlFARmllPTSgHMh6ueR0A9r4zGzdgoV-M2vDT0VYoNpQTe5a4jwLUEG4wDnv3ZihJPeVe8pUfRkrrajuTk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق روایت و ویدیو منتشرشده، چند جوان در خیابان دانشگاه زاهدان با خودرو در حال تردد بودند که ناگهان گلوله‌ای به سمت خودرو شلیک شد؛ گلوله گردن سرنشین صندلی شاگرد را خراش داد و از کنار گوش سرنشین عقب عبور کرد. گفته شده حال افراد داخل خودرو خوب است. در مقابل،
خبرگزاری فارس
گزارش داده بامداد جمعه حدود ساعت ۱۲:۳۰، نیروهای امنیتی به یک خودروی پژو مشکوک شدند و پس از مشاهده سلاح در خودرو، درگیری رخ داد که در جریان آن
۳ نفر کشته شدند
. درباره ارتباط این دو روایت، اطلاعات مستقلی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/withyashar/23545" target="_blank">📅 21:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">واشینگتن پست: رئیس‌جمهور ترامپ در اظهارات علنی خود همواره تأکید کرده است که سیاست‌های انتخاباتی میان‌دوره‌ای بر تصمیمات او درباره ایران تأثیری ندارند.
اما ترامپ در محافل خصوصی نشان داده است که می‌داند تصمیماتش در شکل‌گیری فضای سیاسی نامساعدی که حزبش با آن مواجه است، نقش داشته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/withyashar/23544" target="_blank">📅 21:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: متأسفانه دیوان عالی آمریکا شجاعت لازم برای «دوباره بزرگ کردن آمریکا» را نداشته است. آنها در شش ماه گذشته با تصمیم‌های سیاسی، نادرست و مضحک خود درباره تعرفه‌ها و حق شهروندی از طریق تولد، تریلیون‌ها دلار به ایالات متحده خسارت زده‌اند و برای همیشه به نحوه شهروند شدن افراد در کشور بزرگ ما آسیب وارد کرده‌اند. این فصل غم‌انگیزی در تاریخ آمریکا بوده، اما ما پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/withyashar/23543" target="_blank">📅 21:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBvq1klMmSxPqPE73P7FDxrSEy-2PlIcFxEwBAkTtSiiNosom113tdLDkfZPJnkphSNXlUctRWj2y-efCsIG-TC5upr6iPGRxaRD8T_lF83YJ7bpGMB7J8eJV_u-i6va2eZ33JoAK6a4T61aw6L7djTTdMZtn1EL4dl02m_3ocFyG0I33-A0u6H4K6PNeYfFcnN0hYzv73M6P1Xg6JEYx1KsqoZF5zS4AMxsWi9jLwa24u0xrEmX11vt8nEBu1_kkT_XSPMrWWvUHYp6KFOQ7Et_6K9qgb3XcxeKX9P5uLCazyg4D9TC5_dlpUOAfDSF0YQLgAFTLpYPHGnErHuwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژه جن فدا ها ، اخطار اگه تصویرو زوم کنید ‌شب ادراری‌ میگیرن
@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/23542" target="_blank">📅 20:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانال 13 اسرائیل:
قطر شروط تهران برای پایان جنگ را به آمریکا منتقل کرده و ایران اکنون منتظر واکنش دونالد ترامپ است
@WarRoom</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/23541" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبرگزاری i24news : بنیامین نتانیاهو سفر خود به آمریکا را کوتاه کرده و برخلاف برنامه قبلی، به تگزاس نمی‌رود و دیدار برنامه‌ریزی‌شده با ایلان ماسک نیز لغو شده است. نتانیاهو اکنون قرار است پنجشنبه مستقیماً به نیویورک برود، در مجمع عمومی سازمان ملل سخنرانی کند و بلافاصله پس از آن به اسرائیل بازگردد. در برنامه فعلی همچنین دیداری با دونالد ترامپ وجود ندارد؛ مقام‌های آمریکایی دلیل آن را محدودیت زمانی و تفاوت برنامه سفر دو رهبر اعلام کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/23540" target="_blank">📅 20:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db86a12457.mp4?token=PbSUUtf8FVDiUpayrVkMWg6oeCqITFw0K66u8KCl39bctEp523X8GHUay_wDB-Fk_RetAnGIiPcIin5vUKUkD_MsOtiJ1rxTcvESnQU1eTHc3S0uNzbKJYhfriZPaAo98ameQA37mGpViSwHB9WuTkhAe6oTZxs9LcA_hTXiXDhwOk_mInCNxqhvewkEj_CLw2s9spWodv4sRs3w5jqTQWpFij_9akoq-TkNw5WE9_x1fXQkKClNIz5NbOHyAyg51zFJ1gxoMYxkqyNOzJGYFG60yh7b9DByBGzEpp04SESIIVGOZ37kzKzndXKnieMweDuJCMYuRgRpcRUK0sBB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db86a12457.mp4?token=PbSUUtf8FVDiUpayrVkMWg6oeCqITFw0K66u8KCl39bctEp523X8GHUay_wDB-Fk_RetAnGIiPcIin5vUKUkD_MsOtiJ1rxTcvESnQU1eTHc3S0uNzbKJYhfriZPaAo98ameQA37mGpViSwHB9WuTkhAe6oTZxs9LcA_hTXiXDhwOk_mInCNxqhvewkEj_CLw2s9spWodv4sRs3w5jqTQWpFij_9akoq-TkNw5WE9_x1fXQkKClNIz5NbOHyAyg51zFJ1gxoMYxkqyNOzJGYFG60yh7b9DByBGzEpp04SESIIVGOZ37kzKzndXKnieMweDuJCMYuRgRpcRUK0sBB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارک لوین بازنشر کرد
صحبتهای
، رندی فاین، نماینده کنگره آمریکا:
شبکه‌های اجتماعی، اینفلوئنسرها و اعتراضات، همگی برای
بی‌ثبات کردن آمریکا از داخل
طراحی شده‌اند. بخش زیادی از این اقدامات توسط
روسیه، چین، ایران، ترکیه و قطر
تأمین مالی می‌شود. ما باید همین حالا درباره این موضوع صحبت کنیم تا مردم
قبل از اینکه خیلی دیر شود، بیدار شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/23539" target="_blank">📅 19:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23538">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای انفجارهای کنترل شده در ملارد
@WarRoom</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/23538" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آکسیوس: جنگ ایران باعث افزایش شدید قیمت بنزین و گازوئیل در سراسر جهان شده و فشار اقتصادی و تورمی را حتی به کشورهایی که مستقیماً در جنگ دخالت ندارند منتقل کرده است. دولت‌ها اکنون با افزایش هزینه سوخت و فشار عمومی مواجه‌اند و در صورت ادامه جنگ، احتمال تشدید این فشارها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/23537" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">محسن رضایی به شبکه الجزیره گفت:
از نظر واشنگتن، پذیرش شرایط ما برای خروج از جنگ، کار درستی است. تهدیدات ترامپ هیچ نتیجه‌ای نخواهد داشت و ما برای یک جنگ قاطع آماده هستیم. ارزیابی‌ها و محاسبات رئیس جمهور آمریکا درباره ایران نادرست بود و جنگ با تحریک نتانیاهو آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/23536" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd58a1e73c.mp4?token=g_BBbtC-iP1QXmkhbTYk0OHkBPwT3j-h4Matfb7c1mPYaUx_Y43VOArrqZAL4CMzNX_4HbvayJ_JUYklN-yb4lxPbhnb0TqhqzLB6MvmWEJIs7ygAxr3mkLNCRCo9PUyUoBtsAAlRbDWvXNTh0xnHlDr791fCpVfYIxJxw_S-NM5kBP6BeaiE52m52_Y9r4DTDUjXC6tgAy1wGgKUvzi_8ZXS0C_-kHy3GWyqH8qXqN9g9CDRmyE3XWMejxzw0kqOcse2AhKwH6GLFw-xqD-Y7Nk7TsM5k8GNxzNzqwkri5p1JPLCS9aXJzUapqKWHHCaJ9y_XvHqLZ2mskZI08SUbn1ZpRJb0_OWf-_m4qND_VH5ewW0_amXxYpguHfvmMB5nY6DRW37DUNxa78wdqC_NT0_BwZmwiyFGO_jOmLUWMO2VSWOt1nmcj00eVKtIoZ3hZGJ2XHeEuizwr_Rv_AA9n2OjsMjEJ6ctfzWaWPxfu6Uq3W2kUww5AMVfIEXV1eluxbUzDEqOjiQuzgbSPoSLtBH2mYLeavZsMi3NV3SBWpfad4l5Hfi7eSUAJJ4Q2AaOgLiMdEmZ-YDuGAOcPuSFdRAjKiSYqigLmSo1coAd2gySsvnAZTC-eH9QxGtcKBCRT9VUjnhFzb-46_11oJVu6f3cEkfsxthPK6pNFkEkc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd58a1e73c.mp4?token=g_BBbtC-iP1QXmkhbTYk0OHkBPwT3j-h4Matfb7c1mPYaUx_Y43VOArrqZAL4CMzNX_4HbvayJ_JUYklN-yb4lxPbhnb0TqhqzLB6MvmWEJIs7ygAxr3mkLNCRCo9PUyUoBtsAAlRbDWvXNTh0xnHlDr791fCpVfYIxJxw_S-NM5kBP6BeaiE52m52_Y9r4DTDUjXC6tgAy1wGgKUvzi_8ZXS0C_-kHy3GWyqH8qXqN9g9CDRmyE3XWMejxzw0kqOcse2AhKwH6GLFw-xqD-Y7Nk7TsM5k8GNxzNzqwkri5p1JPLCS9aXJzUapqKWHHCaJ9y_XvHqLZ2mskZI08SUbn1ZpRJb0_OWf-_m4qND_VH5ewW0_amXxYpguHfvmMB5nY6DRW37DUNxa78wdqC_NT0_BwZmwiyFGO_jOmLUWMO2VSWOt1nmcj00eVKtIoZ3hZGJ2XHeEuizwr_Rv_AA9n2OjsMjEJ6ctfzWaWPxfu6Uq3W2kUww5AMVfIEXV1eluxbUzDEqOjiQuzgbSPoSLtBH2mYLeavZsMi3NV3SBWpfad4l5Hfi7eSUAJJ4Q2AaOgLiMdEmZ-YDuGAOcPuSFdRAjKiSYqigLmSo1coAd2gySsvnAZTC-eH9QxGtcKBCRT9VUjnhFzb-46_11oJVu6f3cEkfsxthPK6pNFkEkc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
کنگره از چه زمانی باید وارد عمل شود و درباره جنگ ایران تصمیم‌گیری کند؟
مایک جانسون، رئیس مجلس نمایندگان آمریکا:
ببینید، دولت این را یک جنگ در حال انجام نمی‌داند. چنین چیزی نیست. آنها در تلاش هستند یک عملیات را به پایان برسانند؛
عملیات «خشم حماسی» که موفقیتی بزرگ بود.
من فکر نمی‌کنم در شرایط فعلی نیازی باشد
دموکرات‌های مارکسیست لیبرال در کنگره
به فرمانده کل نیروهای مسلح بگویند با ارتش چه کار کند.
@WarRoom</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/23535" target="_blank">📅 18:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75e72d7fb2.mp4?token=dYfq_qKCnhQftbX6bQE4wjHs6nHKfdJUwze3sBhP-8vFk69JbBcFbbS5VFxl8WDRaadcUe4wOhpZA92hshdYxDvyg1hWv6WG7-tHOJZMAF02i7rC_xRP7uuEEG4T6hs_obhOj1AZ5NZBRcKya1G90Vec8kMeGXIwnDOGzI-NiO6Q74G3wfZs6PX9Bgh0vMHYd68GPkCRw1bauB5DZ8bTHsQSt0M7h2SqmmFGJMwIVqWt3eICc00JErfbkXeOPn_-RrOjLeM4pkgzRsBN6Zz4a2EaBndZvYRAiRFqTMdOs8KkXTTkRinOYGRrBEV5Zxwg372wFWJ5IL-50GHEPge1-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75e72d7fb2.mp4?token=dYfq_qKCnhQftbX6bQE4wjHs6nHKfdJUwze3sBhP-8vFk69JbBcFbbS5VFxl8WDRaadcUe4wOhpZA92hshdYxDvyg1hWv6WG7-tHOJZMAF02i7rC_xRP7uuEEG4T6hs_obhOj1AZ5NZBRcKya1G90Vec8kMeGXIwnDOGzI-NiO6Q74G3wfZs6PX9Bgh0vMHYd68GPkCRw1bauB5DZ8bTHsQSt0M7h2SqmmFGJMwIVqWt3eICc00JErfbkXeOPn_-RrOjLeM4pkgzRsBN6Zz4a2EaBndZvYRAiRFqTMdOs8KkXTTkRinOYGRrBEV5Zxwg372wFWJ5IL-50GHEPge1-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلاغ پر بازی کردن ناتنیاهو در سخنرانی :
نتانیاهو: حسن نصرالله کجاست؟
جمعیت: حذف شد.(پرر)
نتانیاهو: یحیی سنوار کجاست؟
جمعیت: حذف شد.(پررر)
نتانیاهو: اسماعیل هنیه کجاست؟
جمعیت: حذف شد.(پرررر)
نتانیاهو: علی خامنه ای کجاست؟
جمعیت: حذف شد(پررررر)
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/23534" target="_blank">📅 17:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23533">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رویترز(کل ماجرا): اروپا در پی تشدید حملات روسیه به اوکراین وارد مرحله تازه‌ای از آماده‌باش شده است. روسیه حملات موشکی و پهپادی را افزایش داده و کشورهای اروپایی نگران سرایت جنگ به خاک ناتو، حملات سایبری، خرابکاری و حملات پهپادی هستند. لهستان امروز برای احتیاط جنگنده‌ها و پدافند هوایی خود را به حالت آماده‌باش درآورد، در حالی که حریم هوایی این کشور نقض نشده بود. بریتانیا از مردم خواسته برای شرایط اضطراری آب، غذای ماندگار و وسایل ضروری در خانه داشته باشند؛ سوئیس نیز راهبرد امنیتی جدیدی تصویب کرده و ذخیره آب و غذا برای شرایط بحرانی را توصیه کرده است. فرانسه و دیگر کشورهای اروپایی نیز حفاظت از زیرساخت‌های حیاتی و توان دفاعی خود را افزایش داده‌اند. با وجود این اقدامات، اروپا رسماً وارد جنگ نشده است؛ اما سطح آمادگی نظامی و غیرنظامی در برابر احتمال گسترش جنگ روسیه و اوکراین و بحران‌های منطقه‌ای به شکل محسوسی افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/23533" target="_blank">📅 17:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23532">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b85e47807.mp4?token=cMWmA5kK94SNhWw5xfmdcJ53YVbWZTGSNLuwq46_VBi3WQR8k2JAvZsKBZLBZ_qCRBK_IxIw6-Irpr7JL1dwLGreGF4JYd2cdiLOjM-irm0CrYdVwYHS6sKoxWmoPe20tn6tvjatq0Cj3xhkDmBAE_ojh_6yqcEC2jJfB8b6tplQeJUHkuNHaamMQqbBXQWbPom-6tj7D9nhR1fmKhTgcsdMZSMykpdBFYKfcusLUrAe6SDcKqkajTfW7dpvhLf6fdlD_OLM0ftKR3R0R0S9yOOraYl1OOR-XCm1t9LmBZaFrnqZ0iX0jE7RehXng8OvCW3PV5BotL2uKqdodu6opQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b85e47807.mp4?token=cMWmA5kK94SNhWw5xfmdcJ53YVbWZTGSNLuwq46_VBi3WQR8k2JAvZsKBZLBZ_qCRBK_IxIw6-Irpr7JL1dwLGreGF4JYd2cdiLOjM-irm0CrYdVwYHS6sKoxWmoPe20tn6tvjatq0Cj3xhkDmBAE_ojh_6yqcEC2jJfB8b6tplQeJUHkuNHaamMQqbBXQWbPom-6tj7D9nhR1fmKhTgcsdMZSMykpdBFYKfcusLUrAe6SDcKqkajTfW7dpvhLf6fdlD_OLM0ftKR3R0R0S9yOOraYl1OOR-XCm1t9LmBZaFrnqZ0iX0jE7RehXng8OvCW3PV5BotL2uKqdodu6opQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریادار برد کوپر، فرمانده سنتکام:
ما با تمرکز کامل و جدیت به کار خود ادامه می‌دهیم و با نهادهای مختلف دولت آمریکا، کشورهای عضو شورای همکاری خلیج فارس و همچنین شرکت‌های بیمه و کشتیرانی همکاری می‌کنیم تا
حجم تردد کشتی‌ها از تنگه هرمز افزایش پیدا کند.
این تلاش‌ها نتیجه داده است؛
حجم عبور نفت خام، محموله‌های تجاری و گاز طبیعی مایع‌شده در دو هفته گذشته، از هر زمان دیگری در شش ماه اخیر بیشتر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/23532" target="_blank">📅 16:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23531">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5c1e187f.mp4?token=TVTtooM6et3LTf7sUlKsT5J-k3CIrDKFSGlI6iKeXoCP2c6xKfgcqcIN5M3qw5liDRBPTVDcqPdZd6HFRG7yqtKetP_bu9iZ09aXB4Sfev_eN643T09n0o7KoftVaPtW8cGL5fLGuUx9_cId_5_zTduf3Jy97ptAK7nrdXQ0LhDK0HLv9Gh0yZiLS1D78rEldotjs-Cms_jgEzv9gxSY1GqAq6FBsuLfO2GYbGGQTNFsQS_1xn7y8F8qjrG1Tm8Y-CbsvCbV3Y3ta2E_JZQw0jnknTsXR2NijZuGQyU_ZzuSI_b5cH0W6_JOm3fPEBbdFjTCUE5EDnkJS2kKjbXN6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5c1e187f.mp4?token=TVTtooM6et3LTf7sUlKsT5J-k3CIrDKFSGlI6iKeXoCP2c6xKfgcqcIN5M3qw5liDRBPTVDcqPdZd6HFRG7yqtKetP_bu9iZ09aXB4Sfev_eN643T09n0o7KoftVaPtW8cGL5fLGuUx9_cId_5_zTduf3Jy97ptAK7nrdXQ0LhDK0HLv9Gh0yZiLS1D78rEldotjs-Cms_jgEzv9gxSY1GqAq6FBsuLfO2GYbGGQTNFsQS_1xn7y8F8qjrG1Tm8Y-CbsvCbV3Y3ta2E_JZQw0jnknTsXR2NijZuGQyU_ZzuSI_b5cH0W6_JOm3fPEBbdFjTCUE5EDnkJS2kKjbXN6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریادار برد کوپر، فرمانده سنتکام:
نیروهای سنتکام طی دو ماه گذشته از خروج
بیش از یک میلیارد بشکه نفت خام
از خلیج فارس از طریق تنگه هرمز پشتیبانی کرده‌اند. سنتکام همچنین با تأمین حفاظت و هماهنگی، به عبور
بیش از ۲ هزار کشتی تجاری
از تنگه هرمز کمک کرده است.
مسیرهای اصلی عبور در تنگه هرمز عاری از مین هستند
و هزاران کشتی از این تنگه عبور کرده‌اند. بیش از
یک میلیارد بشکه نفت خام
از کشورهای شریک در خلیج فارس از طریق تنگه هرمز صادر شده، در حالی که
ایران به لطف محاصره کامل و مستحکم آمریکا، حتی یک بشکه نفت هم صادر نکرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/23531" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23530">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرگزاری i24NEWS: جزئیات بیشتری از پرونده مرحوم حسین پدران منتشر شده؛ طبق روایت مقام‌های ایرانی، او از طریق واتس‌اپ با فردی که خود را «بن» معرفی کرده بود ارتباط داشته و متهم به انتقال اطلاعات حساس نظامی به موساد شده است.  @WarRoom</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/23530" target="_blank">📅 16:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23529">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حکم اعدام حسین پدران، فرزند حمیدرضا اجرا شد؛ رسانه‌های ایران به نقل از مرکز رسانه قوه قضاییه اعلام کرده‌اند که او به اتهام همکاری اطلاعاتی با موساد و انتقال اطلاعات درباره سایت‌های موشکی و نظامی در اصفهان محکوم شده بود. @WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/23529" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23528">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رویترز: بانک ملت تنها تحول مالی امروز نیست؛ ترکیه در هفته‌های اخیر تحت فشار واشنگتن برای تشدید محدودیت‌های اقتصادی علیه ایران قرار گرفته و لغو مجوز بانک ملت در همین فضای فشار اقتصادی انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/23528" target="_blank">📅 15:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23527">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/23527" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23526">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝘼𝙢𝙞𝙧 𝙎𝙩𝙧𝙞𝙠𝙚</strong></div>
<div class="tg-text">داداش دیدی شاهزاده یه چیزی میدونست از اعتصاب کردا حمایت نکرد</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/23526" target="_blank">📅 14:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست. @WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23525" target="_blank">📅 14:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363a420621.mp4?token=RQil0y_A2Tkq3vdZMn-ULNGVzOxybAhqgnfPuUgFExINsysEyp1IwzMnR2XP8WJOXhNJy2rSAtEk1k1MowlDtu2RquC51zyjQ8qxOFjS7jMfXJtCnlV7Q3iB7JKkfbXUl9yJYUTmsnbpubAiUM0XeMwJF4LcV1CfhzPXXkmG6Z-wgH62KHyn5XMohYIH48r5xCRYcv0YDFqMmtmfLFf6L5Np3BunNfWxp5CHaRTiYaRoZR5r5mTNjBJD4CxSB3kbfyLEO2_zVFG3gYw5Y6PNVFC33dP62w_7pLKqYZX4-T8MwGZs_yxOxpZ8vQQD3KTRPMFW_fp9k8Um1A-ARGuNDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363a420621.mp4?token=RQil0y_A2Tkq3vdZMn-ULNGVzOxybAhqgnfPuUgFExINsysEyp1IwzMnR2XP8WJOXhNJy2rSAtEk1k1MowlDtu2RquC51zyjQ8qxOFjS7jMfXJtCnlV7Q3iB7JKkfbXUl9yJYUTmsnbpubAiUM0XeMwJF4LcV1CfhzPXXkmG6Z-wgH62KHyn5XMohYIH48r5xCRYcv0YDFqMmtmfLFf6L5Np3BunNfWxp5CHaRTiYaRoZR5r5mTNjBJD4CxSB3kbfyLEO2_zVFG3gYw5Y6PNVFC33dP62w_7pLKqYZX4-T8MwGZs_yxOxpZ8vQQD3KTRPMFW_fp9k8Um1A-ARGuNDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی دیشب رفت تجمعات
😂
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23524" target="_blank">📅 14:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بانک مرکزی واردات خودروهای لوکس را متوقف می‌کند
بانک مرکزی اعلام کرده است که برای واردات خودروهای لوکس مانند لکسوس LX700، مرسدس‌بنز کلاس S و بی‌ام‌و سری ۷، کد ساتا صادر نمی‌شود.کد ساتا مجوزی است که پس از تأیید منشأ ارز صادر می‌شود و برای ترخیص خودرو از گمرک ضروری است. بنابراین، خودروهای مشمول این تصمیم تا زمان دریافت مجوز امکان ترخیص نخواهند داشت.این تصمیم برای جلوگیری از سودجویی در واردات خودروهای گران‌قیمت و کاهش فشار بر بازار ارز گرفته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/23523" target="_blank">📅 14:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ان‌بی‌سی: مارکو روبیو، وزیر خارجه آمریکا، برخلاف جی‌دی ونس، در طول جنگ از قرار گرفتن در کانون توجهات درباره جنگ نامحبوب ایران اجتناب کرده است؛ رویکردی که ممکن است از نظر سیاسی به سود او باشد. به گفته منابع نزدیک به روبیو، او در تمام مدت جنگ یک «دست پنهان» بوده و در تدوین راهبرد دولت ترامپ نقش داشته است. این منابع همچنین می‌گویند احتمال نامزدی روبیو برای ریاست‌جمهوری در آینده می‌تواند همچنان روی میز باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23522" target="_blank">📅 13:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حریق در انبار کباب‌سرای محمد در تهران، در خیابان دولت (کلاهدوز)، نرسیده به سه راه نشاط (پلاک ۳۳۵) @WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23521" target="_blank">📅 13:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23520" target="_blank">📅 13:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش‌ها از کشته شدن ژنرال فراق العسّار از فرماندهان ارشد حوثی‌ها حکایت دارد. این گروه در بیانیه‌ای از او به‌عنوان فرمانده تیپ یکم کماندو یاد کرده است. العسّار در جریان حمله‌ای در جبهه کَهْبوب، در نزدیکی تنگه باب‌المندب، کشته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23519" target="_blank">📅 13:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79606f3b2f.mp4?token=Mg15zS6o9ayD4Jp7Czp7aX8pKhyX_WDAPpPMXQjkR7YP1ckdgDOvlFtuvEYAo-MO1JguEYQFfXOhuvOLxGySceLe52k-uDM12eNA_5wxiiUQf1iTOsUVhKpkOPpfcsniq2V06600m0hElskX1BcQrO-kRtaDNxmZ2m5_4bwmgBDpkluctH_nhk_6IpE7WPg2DbvNvAFg7WacFil5dKG5GXTQqme1JBTJDc36asjaOIwHcWAlEmAfDizLj7XfSA3kX_t2P_iZPk6kE_FFN0EqyuMNxrgg5IIyne_pUDh-bbIF0dXA6_CyWXZjdXmgRMjcVeNC3QOJOy5bZ8oSeR47vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79606f3b2f.mp4?token=Mg15zS6o9ayD4Jp7Czp7aX8pKhyX_WDAPpPMXQjkR7YP1ckdgDOvlFtuvEYAo-MO1JguEYQFfXOhuvOLxGySceLe52k-uDM12eNA_5wxiiUQf1iTOsUVhKpkOPpfcsniq2V06600m0hElskX1BcQrO-kRtaDNxmZ2m5_4bwmgBDpkluctH_nhk_6IpE7WPg2DbvNvAFg7WacFil5dKG5GXTQqme1JBTJDc36asjaOIwHcWAlEmAfDizLj7XfSA3kX_t2P_iZPk6kE_FFN0EqyuMNxrgg5IIyne_pUDh-bbIF0dXA6_CyWXZjdXmgRMjcVeNC3QOJOy5bZ8oSeR47vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر پزشکیان: من هم جان‌فدا هستم
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23518" target="_blank">📅 13:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23517">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/23517" target="_blank">📅 13:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23516">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/23516" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23515">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23515" target="_blank">📅 13:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23514">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝘼𝙧𝙖𝙙</strong></div>
<div class="tg-text">داداش یعنی چی که میگی تجزیه طلب
تو حق مردم کردستان رو بده بهشون چرا بخوان جدا شن؟؟
وقتی رضا پهلوی دوم بتونه برابری ایجاد کنه و عدالت ، هیچ قومی خواستار جدایی نیست بلکه اونایی هم که هستن میشن طرفدارش و طرفدار کشور.....</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23514" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23513">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromℛℯ𝒷𝒾𝓃 𝒟ℯ𝓁𝒶𝓋𝒾𝓏</strong></div>
<div class="tg-text">وقتی خاکمونو پس گرفتیم توهم تو همین کانال کونت میسوزه</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/23513" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23512">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23512" target="_blank">📅 12:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23511">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏بهمن کارگر، رییس ستاد مرکزی گرامیداشت «مناسبت‌های دفاع مقدس و مقاومت» گفت که امسال با توجه به شرایط جنگی، رژه نیروهای مسلح برگزار نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23511" target="_blank">📅 12:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23510">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">داداش نگو ریاکار عقیده خودش رو داره بچشو همشریا و هموطن خودمون کشتن</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23510" target="_blank">📅 11:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗬𝗮𝘀𝗶𝗻</strong></div>
<div class="tg-text">داداش نگو ریاکار عقیده خودش رو داره بچشو همشریا و هموطن خودمون کشتن</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23509" target="_blank">📅 11:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23508">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23508" target="_blank">📅 11:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23507">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الجزیره: قانون جدید تحریم‌های ترامپ، تمدید ۵ساله «قانون تحریم‌های ایران» را تصویب کرده و اختیارات کلیدی تحریمی آمریکا علیه بخش‌های انرژی و تسلیحاتی جمهوری اسلامی را تا پایان سال ۲۰۳۱ حفظ می‌کند. این قانون همچنین ابزارهای جدیدی برای اعمال تحریم و تعرفه علیه روسیه و خریداران انرژی روسیه در اختیار رئیس‌جمهور آمریکا قرار می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23507" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23506">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست. @WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23506" target="_blank">📅 11:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23505">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWfoOa-fm9fkGtKRklb_abDflUCg--0ShcZTvnh-hevrzcdwaKZoA1smDM6pw47ypyUEsaTH-N4VJ79znw_u3KXkrjdNnNd39iv0BYeiAwL8c1IOJYtkPwjt_TXCm4iNNKuBhyDkCaw06Oj1PWYXY7uHYZ6kkODCWiYUfoZvTyhS-zOftcgQqdzXy35g6iOMS-OD-v0zR1P3HVyFd59mdylwVAkulh19TSkMgxjBUM3BoGsD_h1KEi6vHz4R4NysHULEP7ZQjzGTh5v0nOVMbeJEJ26KZTBBEatpVw-g-BetkmekArhvABLEPvkgrXczsxW4U9vab_oTiZ05A-piEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23505" target="_blank">📅 11:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23504">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هم اکنون تهران ، خیابان دولت ، چهار راه نشاط @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23504" target="_blank">📅 11:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23503">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23503" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23502">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23502" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23501">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc408f38d4.mp4?token=YzGbRYJD6f3eJMyIiXJEkNVAM_tPfESxTMi3WBxROKFsBnHhHbxVI4PK2dNjBiAKOebcykei50bIqDleaHTBiCFv6alQBS-xCh3cLdDp_0pVGc7JurYDtW75iXmq-mIFHaiwnQ7PKPzt3omt1notSmjGxWTWcMffR2FI0GZOBIQFXhkUtzvsP2OQvXAKCQ9hf20-Qm1IwG1PRfkN-kwtYpI9_jVFAmaiiTsq6cwHs06bdWW9Vj40o0dUZsCHHgV65C6EYrPlfhzIkWXoQBYOPNgNnr8EkMxeuYVJ0-6Xpos5hIfToGX22p5HwO2WQeStPFhOl6BCwJiZ_olH4KD96XsSr_5VVi-n0JoUPzPvqxQHl6TR1i02ZybA86eMPRRntW0b625L-iq074EfQlOSfcbjgVOdTnwic12QIGD-5OQumxvjWwDgugIw1GzEVdYGd07TpKl4dpRUgYH8YaElQocpvZhp4eCgnIAH4MtBb92dCq_cpph_VUQ6k1vlTjMvXkb-GRFAo4yT5YTs46bJDPKUH5s4B51yN1mQdHg3pWGkTn5Bwk5dORO8HWesJnqPTiYe42hzWidNsKp0n8u4qf9Q3EoTG47cSf-v9cBao2vPTNwTCZXiPBtwEK-XH6MPOJ5CT9yd6k3JvYdQiFvaksVk74Zm0_kY31iFunXDvFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc408f38d4.mp4?token=YzGbRYJD6f3eJMyIiXJEkNVAM_tPfESxTMi3WBxROKFsBnHhHbxVI4PK2dNjBiAKOebcykei50bIqDleaHTBiCFv6alQBS-xCh3cLdDp_0pVGc7JurYDtW75iXmq-mIFHaiwnQ7PKPzt3omt1notSmjGxWTWcMffR2FI0GZOBIQFXhkUtzvsP2OQvXAKCQ9hf20-Qm1IwG1PRfkN-kwtYpI9_jVFAmaiiTsq6cwHs06bdWW9Vj40o0dUZsCHHgV65C6EYrPlfhzIkWXoQBYOPNgNnr8EkMxeuYVJ0-6Xpos5hIfToGX22p5HwO2WQeStPFhOl6BCwJiZ_olH4KD96XsSr_5VVi-n0JoUPzPvqxQHl6TR1i02ZybA86eMPRRntW0b625L-iq074EfQlOSfcbjgVOdTnwic12QIGD-5OQumxvjWwDgugIw1GzEVdYGd07TpKl4dpRUgYH8YaElQocpvZhp4eCgnIAH4MtBb92dCq_cpph_VUQ6k1vlTjMvXkb-GRFAo4yT5YTs46bJDPKUH5s4B51yN1mQdHg3pWGkTn5Bwk5dORO8HWesJnqPTiYe42hzWidNsKp0n8u4qf9Q3EoTG47cSf-v9cBao2vPTNwTCZXiPBtwEK-XH6MPOJ5CT9yd6k3JvYdQiFvaksVk74Zm0_kY31iFunXDvFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران ، خیابان دولت ، چهار راه نشاط
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23501" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23500">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc97b83ba.mp4?token=S1O17RHT6s0JWzQyscz9p5TdT_amuT1BlNhahZ8U90OK2MgWXq8GI_qmUiACD-cq6F9RrQuwbSwxQMVOGQSAEsocQryVN20LFyNLw9-IfY5BmWB7kEmgTNT5UJWFjves2gumxjguOWUN0JpoUZdpQxQ4d8sSiSnGEH7muhXMrjTs9i03Ky4Y_Wi_FVB_fZlT3KpzaDvDiUxd2YLnSc9Yy33v4R25rTgjzoSggJOh_OFT86h8HdHudImPk_TaJk15uPxlWtLFHiP6wzHVCthGbS5ROvCYU7f1eEYG9TGlFS6VnYqlorNWvASk7Q7uRBht9eCR1Y4KfbNLcb8MsquQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc97b83ba.mp4?token=S1O17RHT6s0JWzQyscz9p5TdT_amuT1BlNhahZ8U90OK2MgWXq8GI_qmUiACD-cq6F9RrQuwbSwxQMVOGQSAEsocQryVN20LFyNLw9-IfY5BmWB7kEmgTNT5UJWFjves2gumxjguOWUN0JpoUZdpQxQ4d8sSiSnGEH7muhXMrjTs9i03Ky4Y_Wi_FVB_fZlT3KpzaDvDiUxd2YLnSc9Yy33v4R25rTgjzoSggJOh_OFT86h8HdHudImPk_TaJk15uPxlWtLFHiP6wzHVCthGbS5ROvCYU7f1eEYG9TGlFS6VnYqlorNWvASk7Q7uRBht9eCR1Y4KfbNLcb8MsquQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان تهران شمال شرق ، محدوده شریعتی میرداماد ستون دود عظیم @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23500" target="_blank">📅 10:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23499">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzINSDC9qToVuVgC2obXqeTGnRed9sR88TtwvSo-9fCnUwbjRaYB1aWL8kPiSq53JJvkLaAVaRP80zBKSW2NQAfWngK6TyACAGvDHr_t3USsx1jVABewflV2eLAd3oB3_LsH0248yTVVvuKXYx4MaqmhLNNsGVsbzDbig-BsCyOMpP6j4J2cS0FX1aTLwcAQt22-V5WJ2efJf9wvSl-aLeucmBBDv-RXssOw3d4juSknrDluyqxkO-c3c5pT0-uSn6iyh56E8AjW6V-pwFMTqxBbqB3slmjAJTxgsYzF--vveqSJ5oNpgvC8nwEx6GnH7XEWWZ2ePREtrvxqcD_4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان تهران شمال شرق ، محدوده شریعتی میرداماد ستون دود عظیم
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23499" target="_blank">📅 10:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23498">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC3hLAdqUmC3O1qOFDYDCuFJqazIRf1kibxIfjfDAzKvuyaK8Si0AkciZ0h3-hM0anNUhSF3ti7mHLRXaSXHPqMShYTzUnRlx-HdxbHN-4VP-u1fr0oZIAOMDtkgYvFZSFuTgFTqf_AU9Q5LMI6g4jtzszJ0B2dIHG9jxi3DUa-vwIj98IXzp1mR7EcjHw2XVu7wA-qhGMOlGJqT9Ov5NYQMTsqXBfsKGBueenJmb0ysRxjWTrZpZUEIwlBzTNBzIc9VtJki_k3Tt8HmYO2GrI1Tk6ZJThCgGpUsyZvxG1blsW0nfuUeiPTJRf3pMJWyGnjcyu9wqwhnnyh5iXgQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن‌ کج بند رضایی: منتظر موشکای با سر‌جنگی ۱ تن به بالا باشید
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/23498" target="_blank">📅 10:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23497">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b8923ab5.mp4?token=OvKIPcL2_BG5yPuHYb86tPvv_Z5FrFlYgcT2zV7uW5eyYsMsb1W2RCsv2NjgHoLmc-w1iVde5gj8LVuluyzlUwlPbfnrjl93mdJ2qKc4zqIfjPRwA8mAEU2hNPGdncHd9fAFWnP7gzygXc3ffETM1PwipA85rjUFkcKRL7UKTuty-SdAAbCoXPwL1JGIOnZ6RRqxXY7tk7AxTjxNYOkwUSrx_YdKLOhdSZum9V4thHr9LMKbN8wevxJx9yX2DoDOZF9WXPr76ti7diKjW_3bt8hldMK9qyAVXd3eQri-UNf0mI7p_xq2yv8w838l-izIqTRlgJh6fU8y13k6YdbdnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b8923ab5.mp4?token=OvKIPcL2_BG5yPuHYb86tPvv_Z5FrFlYgcT2zV7uW5eyYsMsb1W2RCsv2NjgHoLmc-w1iVde5gj8LVuluyzlUwlPbfnrjl93mdJ2qKc4zqIfjPRwA8mAEU2hNPGdncHd9fAFWnP7gzygXc3ffETM1PwipA85rjUFkcKRL7UKTuty-SdAAbCoXPwL1JGIOnZ6RRqxXY7tk7AxTjxNYOkwUSrx_YdKLOhdSZum9V4thHr9LMKbN8wevxJx9yX2DoDOZF9WXPr76ti7diKjW_3bt8hldMK9qyAVXd3eQri-UNf0mI7p_xq2yv8w838l-izIqTRlgJh6fU8y13k6YdbdnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران: ویرانگری حملات نظامی ما علیه ایران تاریخی و بی‌سابقه بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23497" target="_blank">📅 09:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23496">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ec58e117.mp4?token=H51OQnTlE8uaESx2qCq_PjuVLmDv-o6EAYyrjJvd8CcoolndxeCJRtk_mAr8MLenJ0UzsHjNjRDG1-CM_XjiC5_uA5EyQ8GrkhUn9hkEaJw34IuMPlcSoTOzroUJ52rU8e-p7nycxWpVZvxAm_n_2Dxp0DRyZwyBzKoO2eVsXMnmWYRhLFXPHN1kDooqBKpbN02j5mV2dnk6yqhdmr0IP6it00gPD43XOek-4wooD7QSn9xBruK4DHaWS9mOhez_FhWchnxCjF9pVX4BZ1p5haZt5Gx4G070X83jUb1LxOUAfuop_x_YwiRenoZKR_lHPhQsZt6b_7cobxa4sr5Tjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ec58e117.mp4?token=H51OQnTlE8uaESx2qCq_PjuVLmDv-o6EAYyrjJvd8CcoolndxeCJRtk_mAr8MLenJ0UzsHjNjRDG1-CM_XjiC5_uA5EyQ8GrkhUn9hkEaJw34IuMPlcSoTOzroUJ52rU8e-p7nycxWpVZvxAm_n_2Dxp0DRyZwyBzKoO2eVsXMnmWYRhLFXPHN1kDooqBKpbN02j5mV2dnk6yqhdmr0IP6it00gPD43XOek-4wooD7QSn9xBruK4DHaWS9mOhez_FhWchnxCjF9pVX4BZ1p5haZt5Gx4G070X83jUb1LxOUAfuop_x_YwiRenoZKR_lHPhQsZt6b_7cobxa4sr5Tjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما در جنگ با ایران با اختلاف زیادی در حال پیروزی هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23496" target="_blank">📅 09:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23495">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8ba38435.mp4?token=eybqIuZX7eT6C23UvhlKdZKDC1xdEvr2llB2B0DEOiVp3NgpsXC1NNdE1o-Zeamw1zw0du2-kdKHj4ga-2wLsHeub97Po_r79CgtHbU5vAfVVJLc1dSmSnw3t0Yrd59giGvncgjcSJztfNL0DFdymR_T8sRQtcWrRMBoGHC-qmayKb6GBr7W0iNaTmT-Lk348qkiMzR4SRSH2ue2RX-8Z1rVkRO9sWfTTPgRg1HH9TpXwdJrJWn5P9Kx4dHTFuxIhdaayXg-_-McRBvvpikV1dqZdvG3PRc1Wn7pq3q4nQDhhmeD_c5MWltXpDEp6jY3sG2K33dXzdKSFv6sKRQ9cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8ba38435.mp4?token=eybqIuZX7eT6C23UvhlKdZKDC1xdEvr2llB2B0DEOiVp3NgpsXC1NNdE1o-Zeamw1zw0du2-kdKHj4ga-2wLsHeub97Po_r79CgtHbU5vAfVVJLc1dSmSnw3t0Yrd59giGvncgjcSJztfNL0DFdymR_T8sRQtcWrRMBoGHC-qmayKb6GBr7W0iNaTmT-Lk348qkiMzR4SRSH2ue2RX-8Z1rVkRO9sWfTTPgRg1HH9TpXwdJrJWn5P9Kx4dHTFuxIhdaayXg-_-McRBvvpikV1dqZdvG3PRc1Wn7pq3q4nQDhhmeD_c5MWltXpDEp6jY3sG2K33dXzdKSFv6sKRQ9cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: هفته آینده در سازمان ملل سخنرانی می‌کنید. پیام شما چیست؟ ترامپ: سال گذشته، اپراتور تله‌پرامپتر من را از ورود به سالن منع کردند. بنابراین مجبور شدم بدون تله‌پرامپتر آنجا بایستم. جالب نیست؟ خبرنگار: پیام شما چیست؟ ترامپ: یادتان هست؟ آن‌ها پله‌برقی را خاموش کردند. خوشبختانه بانوی اولم خیلی محکم بود و توانستم پشت او یا بخش دیگری از بدنش را بگیرم. در واقع، دستم کمی پایین‌تر از پشت او قرار گرفت و محکم گرفتمش.
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/23495" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23494">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f409e707.mp4?token=ZYouM50LTWcvY2c_Mr-aTYHJS1W3yzW8KQb7MUc1MokChlMxe6VL768VLqgiTJxvDdi6qgcuxGxf4gbYXjz5vnGXZpQmTbbJsZPzFlNmoZwTIZpMFv3e2DQHh0wHrcOzS5o-MYCaFmDqxERuFOptRlwftXRA_aqUxQ42Zx6NySiUbn5HfwmLNDsJXk5hkq3kwTATAVXc3nBkl-LAxsQlAnZo5k7aTBCFJsuxRnZIM90_5aMJX3LtFhGH7AGsdLbjpH1FEWNO0PcAPJL0ciPRghsaB4w4ZyvjbW5lCys9hfV_SSn-NUOnz5CP7ncyXu_nUFJ7TFyOSjoRLMwYD7Qhug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f409e707.mp4?token=ZYouM50LTWcvY2c_Mr-aTYHJS1W3yzW8KQb7MUc1MokChlMxe6VL768VLqgiTJxvDdi6qgcuxGxf4gbYXjz5vnGXZpQmTbbJsZPzFlNmoZwTIZpMFv3e2DQHh0wHrcOzS5o-MYCaFmDqxERuFOptRlwftXRA_aqUxQ42Zx6NySiUbn5HfwmLNDsJXk5hkq3kwTATAVXc3nBkl-LAxsQlAnZo5k7aTBCFJsuxRnZIM90_5aMJX3LtFhGH7AGsdLbjpH1FEWNO0PcAPJL0ciPRghsaB4w4ZyvjbW5lCys9hfV_SSn-NUOnz5CP7ncyXu_nUFJ7TFyOSjoRLMwYD7Qhug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: اگر از مردم بپرسند که کاهش قیمت بنزین را می‌خواهند یا اجازه بدهند ایران به سلاح هسته‌ای دست پیدا کند، نتیجه رأی‌گیری با اختلاف بسیار زیادی به نفع جلوگیری از دستیابی ایران به سلاح هسته‌ای خواهد بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/23494" target="_blank">📅 09:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB25LaHq3O62YegFmKuA7ADmX-ezg1C-H-W__NhmcfVvYI_OrYNFm_wGVqImcTCp_VOC-bFRweEIMAdJliz4i8eeDYw5RGiaaEt8EzgfGVuABU612XUPVEZ62s1MY1xa9_NA3uF27XhHED63UjUbKKLHL231IlNuP6Oy9Votl85B-HZsGpDwT_uefVxR_95DeG8v1VNtd_5y9HjX6wJzyE32AkXgkdDk4nTMG4Je9J226tOVoHx4MXCP8xv5rf1YOGVfTbilKZ024zO6g7ZHtqDqysRNQoagDAhzcBDkQ8OchTk_nrPBXGj5RtwOzRiEjZ1W8cRuueNXFQTcW3TdSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام
حسین پدران،
فرزند حمیدرضا اجرا شد؛ رسانه‌های ایران به نقل از مرکز رسانه قوه قضاییه اعلام کرده‌اند که او به اتهام همکاری اطلاعاتی با موساد و انتقال اطلاعات درباره سایت‌های موشکی و نظامی در اصفهان محکوم شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/23493" target="_blank">📅 09:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23491">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOh0_lNM9z_VH_stvkcIbPQQ4w_LC6cFvkZWLzErGAEOGwbzaX7BZiZK_xPsrc8GVEo30iLbacerE9SW_hZ5wRe7bhfCp45KS3YGBvqt51aRSVuaaexAoWfXbpKWaA7OUiGxlsTTWh1FoMXDXl1PlAmaoID_Jh-Rq9Nv-Ac663oU6Haz6gs6T_QTO0uNwyX7aDJQNYIsSihpfeLG3uOBDxWgAuEEvNS4RPJDOng6-QdK1hToq8mFE67rHLMnd2uy5QVCisApNdgM8A_yXAhIK6dotOySixl5Qlya46FmXvQyNqZsjkAa50K9PBaRhTtpJc4d4cH9DqAjOfRT2yUriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukv7zUOGMJ2No7aK7w9iiIZJ8-Bg0KMgqlnwEURbKwzxKmaULlQdIaG6ZVGhfiIKoxxiQsJV7U8Wb0eWc5OqNpG5SolZau6HMnYMEFeOIGgxcLdZQ04fRAe66vMFfRWDQd9pW-UsbIG8IUsXjrmSPI0mu6vKcYcmbt3oFJUQ0xR32vvAgn5mD_fE1s2tJPE-bp0nOmsXAqIx3lnyrsSIEFxJZWeILkSTTjjMlYzjl4EmF8GFl2RpNrhrJuv19CJ20QwD_gVArp1JnBZ24SCldj2FdZ_0mHbcRKTANG3zpWW0P1IbsGETV4_QvYl8CHinlhrIN4D04QLOEh2eqIp9Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی در شبکه اجتماعی تروث سوشال، فهرستی با عنوان «۲۵ دستاورد برتر ترامپ در سال‌های ۲۰۲۵ و ۲۰۲۶» منتشر کرد و در آن، از سیاست‌های مهاجرتی، کاهش مالیات، اعمال تعرفه‌های تجاری، افزایش بودجه نظامی، گسترش حفاری نفت و گاز و لغو برخی سیاست‌های اقلیمی به‌عنوان دستاوردهای دولت خود نام برد. مورد مرتبط با ایران در این فهرست، بند ۱۱ است؛ جایی که ترامپ مدعی شد آمریکا در عملیات‌های «چکش نیمه‌شب» و «خشم حماسی»، ظرفیت غنی‌سازی هسته‌ای ایران را نابود کرده تا به گفته او، ایران «هرگز» به سلاح هسته‌ای دست نیابد.بند ۹ نیز به افزایش بودجه نیروهای مسلح آمریکا تا یک تریلیون دلار در سال جاری و برنامه برای رساندن آن به ۱.۵ تریلیون دلار در سال آینده اختصاص دارد
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/23491" target="_blank">📅 09:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23490">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kh0eRZ3McK-eLxdyxcOfRg1axkloBavCemMxr9uVHlRKqm8yB00hxp8AvmfDFkpeUpzZ4rdPMHJepJ_qyUYGIjYKqvOkOpvhxdSilDc5ZMiJbcGYxVAeLiHKwtKdD_kwPHuDstGN12HcB3k4CV_FD2KIZ4pGvqFLfHX_T0rJLZXSa9dDDKAcNu3DYP24EInVd3ZM-UV1oOR3iQbOxJ90iyy80A2hjDeh2cRi8MrSa6m3zcXbeFo5ZquLFMxHJYYVOaCyipHqJL8OT_E7ZpEwWFgPuHvaJEcV_-RcF3Xco22uPS7ZQKcJjP_fYtwFszs4RmtAVlf5WA76w_a6a3v3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیم جونگ‌اون از خط تولید پهپادهای انتحاری یک‌طرفه بازدید می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/23490" target="_blank">📅 09:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23489">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6zAS0dPkn2CJi5j2CprjH2IhblHx_9DZXV2cTKa3Lj2958YPOm9JekSISmYOjis70gfwS8bVTeBfqTlmiDifrK94p_Deilg3q0W8-syuLnFv9z3N6dW9SLdsRPTt46LYEiVLAZ8o9LVkpbPa3lVTk1ds4WUR_Dcg-fqrMpULmS1qMownBEJbQDxIzf89aKFCBlZHBqXD5Dq5ovXsB2RI-b3xswYrDi1RTz6fBcYF0vgPRj6uv37vRiQJfBCQg_n47U0FOCxk-haBdfFvx8zN-xBF7_3ALj0LgOE-eDtV-k3DVUIgqRd6b4mspJE9NEKHCkZi2enBXvwaQokZMnfcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد ناظر بر امور بانکی ترکیه مجوز فعالیت شعبه استانبول «بانک ملت» را لغو کرد؛ بانکی که صددرصد متعلق به دولت ایران است و از سال ۱۹۸۲ در ترکیه فعالیت داشته است.سازمان تنظیم مقررات و نظارت بانکی ترکیه (BDDK) دلیل این اقدام را تهدید علیه ثبات نظام مالی عنوان کرده است.این بانک پیش‌تر و در پی تحریم‌های آمریکا تا حد زیادی از شبکه بانکی جدا شده بود (قطع دسترسی به سوئیفت و حذف از سامانه انتقال الکترونیکی وجوه یا EFT ترکیه)، اما این تصمیم به معنای پایان رسمی فعالیت‌های آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/23489" target="_blank">📅 08:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08184bf9e6.mp4?token=uoRNp-VV91ikJam72JM-IlCAIq70hRk3aZbuziUkr6gA2U4mUpjsFWzNkP6tr-vQLbNRQHjyHEikTldsAB6HH4Dfht49TrGUV1Bdfh1XaamhDlhZFL5gk6rRbEPmH1qtbuKZJ1dslmNgvG6QH1prVvyUAJme1sde7IZt52f2BsNHOtsSqwWRyrCx3y4cvJz1gISIj9NHDbjvtq_DODq66FcUTFJDHoipw3gTyikR85Df6YGzyX4InNLcz6nOQEQc1NuZR27gPppTu8naYvVA7VMDh4S5ayo9jDh7lMAtHr9e3VJ_k5ccvEeCzmuLfp4EyYJflW5knOkzM3zTmgJZEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08184bf9e6.mp4?token=uoRNp-VV91ikJam72JM-IlCAIq70hRk3aZbuziUkr6gA2U4mUpjsFWzNkP6tr-vQLbNRQHjyHEikTldsAB6HH4Dfht49TrGUV1Bdfh1XaamhDlhZFL5gk6rRbEPmH1qtbuKZJ1dslmNgvG6QH1prVvyUAJme1sde7IZt52f2BsNHOtsSqwWRyrCx3y4cvJz1gISIj9NHDbjvtq_DODq66FcUTFJDHoipw3gTyikR85Df6YGzyX4InNLcz6nOQEQc1NuZR27gPppTu8naYvVA7VMDh4S5ayo9jDh7lMAtHr9e3VJ_k5ccvEeCzmuLfp4EyYJflW5knOkzM3zTmgJZEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست: در طول ۲۵۰ سال گذشته، ما همواره به آمریکایی‌هایی نیاز داشته‌ایم که برخیزند و بگویند: «مرا بفرستید.»
چه کسی با «قرمزپوشان» (نیروهای بریتانیایی) خواهد جنگید؟ چه کسی به نبرد با کمونیست‌ها خواهد رفت؟ چه کسی با اسلام‌گرایان خواهد جنگید؟ چه کسی مبارزه خواهد کرد؟همواره آمریکایی‌هایی بوده‌اند که گفته‌اند: «مرا بفرستید.»
@WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/23488" target="_blank">📅 08:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfiPlIb0TK-xOojT1Ujx5uxzJEEE-BaWkev5KETC-NmUjdr7YFEJtM5UGMBIg_m23OXCJpmcULSz2BvOh-csPWavKCSVFXnRCJUcBQa06PBtp5FpUbb18zi7F0eenJU9Jp7GiZwcnCFCCRX906-T6u8TdFZqF3bGAnPB0HMdCGDkCOur843KTwHA29pBGWTEdZwRDa5pmiR7ZQmiNnTCaLCIQAgE--dLn0mW91rp7pzGl7CAcyilDIVtoKcdQDdOkj_gTKANtKGdGTXJESQOf9JczPCapHLfDdSmN9G-caVfKieozHQhIqj9wYkcmBO_lUsrP-x62M3EjgxlVcrHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون پس از توقف موقت این طرح در اوایل ماه جاری، اکنون در حال پیشبرد برنامه غربالگری اجباری سطح تستوسترون برای نظامیان مرد ۳۰ سال و بالاترِ ارتش ایالات متحده است. بر اساس دستورالعمل‌های جدید، این آزمایش در معاینات دوره‌ای سلامت و ارزیابی‌های سالانه گنجانده خواهد شد و مسیرهای درمانی استانداردی نیز برای موارد کمبود تستوسترون در نظر گرفته شده است. نظامیان جوان‌تر نیز می‌توانند به‌صورت داوطلبانه درخواست انجام این آزمایش را بدهند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/23487" target="_blank">📅 08:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23486">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdQWk7U_KX3sBEETIH8J06abZOpz24LMIWJmo6vowwuqKKjFS4myYNJxk0FXQBVfXl1_NWYlo-dl_gcUxlKdZahmnvaSpTVEjwsyWjVR5yqXQukTy80XanSGFOcEnhb2F-Zs9SyQFGP5nFsL41MMZF4r5s1KKHMhv4wYHQbFOdckJbIIQPTb5WqNHSvKGlZoJpq9yT58HHw1dgqxp2teqvuCGETkRc7nypPjsMrrxsuEm-jyKArFWcM0LIyp_v4Hsk2P-AFzS1rI_jMWc8M368JG4Ew-oV6LEBrzaW-M0TSe3KU-Pi9W1czCuS2quFOOawWLHHPxlGQdlQQGDSQC3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه ایالات متحده با فروش تجهیزات پدافند هوایی و خدمات پشتیبانی به ارزش ۲.۶۸ میلیارد دلار به اوکراین موافقت کرده است.این بسته شامل سامانه‌های پدافند هوایی با برد بیشتر، پرتابگرهای متحرک، رادارهای مقابله با پهپاد، قطعات یدکی، نرم‌افزار و پشتیبانی فنی است.اوکراین هزینه این خرید را از طریق کمک‌های اروپایی و بودجه‌ای که پیش‌تر تحت برنامه «تأمین مالی نظامی خارجی» ایالات متحده اختصاص یافته بود، تأمین خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23486" target="_blank">📅 08:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23485">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ قانون «تحریم روسیه و ایران، لیندسی او. گراهام» در سال ۲۰۲۶ را امضا کرد. این قانون تحریم‌های موجود علیه ایران در حوزه انرژی و تسلیحات را برای ۵ سال تمدید می‌کند و امکان تحریم پوتین، الیگارش‌ها، بانک‌ها، شرکت‌های انرژی و دفاعی و ناوگان نفتکش‌های سایه روسیه را فراهم می‌کند. همچنین به رئیس‌جمهور آمریکا اختیار اعمال تعرفه تا ۱۰۰ درصد بر کالاهای کشورهایی مانند چین و هند که نفت و گاز روسیه می‌خرند و تا ۵۰۰ درصد بر برخی واردات روسیه را می‌دهد. ترامپ می‌تواند این اقدامات را تعلیق یا لغو کند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23485" target="_blank">📅 05:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23484">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ برای گذراندن آخر هفته راهی کمپ دیوید شده است؛ طبق برنامه رسمی، او شنبه و یکشنبه در این اقامتگاه خواهد بود و برنامه‌های این دو روز با عنوان «زمان اجرایی» و بدون حضور رسانه‌ها ثبت شده است.  هم‌زمانی این سفر با تحولات جنگ ایران مورد توجه قرار گرفته
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/23484" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23483">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش ها از
هدف قرار گرفتن نزدیکی اقامتگاه بن سلمان
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/23483" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23482">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa371e84.mp4?token=b7T12cFYQO72Zm4Cd0mbZezDBFxxUfV8XGbIWrT0WoyT57SYT-woF2N9YaSlBl21plRDf7SMyiTlIdoyrEM0czoJ85EvEtxmQTM3sK3BstLDvjXihw2BfR3ScJ0tdMOpQUtswQcq3-BSsbUdQ_RLOoQjrGwW5oe95wDvt9XHNPzCAZYu48oFI8apqdAx60UKwauxBYWxoqQ_rUoRsNSc5qoU-6-1YAWziFoq0ZaXZFe5URdJOGgtInfVlXkK89zuuXUcggyXTHUIxH9K-an6AodjPO6R0VS3ao3i2LFLmduZGD231BGWIHQoB2Zy_R_gIV-a79_K6Bnb54Q_448JVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa371e84.mp4?token=b7T12cFYQO72Zm4Cd0mbZezDBFxxUfV8XGbIWrT0WoyT57SYT-woF2N9YaSlBl21plRDf7SMyiTlIdoyrEM0czoJ85EvEtxmQTM3sK3BstLDvjXihw2BfR3ScJ0tdMOpQUtswQcq3-BSsbUdQ_RLOoQjrGwW5oe95wDvt9XHNPzCAZYu48oFI8apqdAx60UKwauxBYWxoqQ_rUoRsNSc5qoU-6-1YAWziFoq0ZaXZFe5URdJOGgtInfVlXkK89zuuXUcggyXTHUIxH9K-an6AodjPO6R0VS3ao3i2LFLmduZGD231BGWIHQoB2Zy_R_gIV-a79_K6Bnb54Q_448JVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: جنگ به زودی به پایان خواهد رسید و وقتی این اتفاق بیفتد، قیمت بنزین شما به سطحی که قبل از آن داشت، کاهش خواهد یافت، شاید حتی کمتر از آن.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/23482" target="_blank">📅 23:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23481">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">العربیه: وزیر خارجه پاکستان محسن نقوی در ساعات آتی به ایران عزیمت می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/23481" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23480">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">المانیتور: یک منبع ارشد اطلاعاتی اسرائیل می‌گوید نهادهای امنیتی اسرائیل در حال حاضر با
حمله پیش‌دستانه علیه حوثی‌ها مخالف‌اند
. به گفته او، حوثی‌ها اکنون هیچ بازدارندگی مؤثری از سوی آمریکا، اسرائیل یا عربستان ندارند و به «اسب تیره» منطقه تبدیل شده‌اند؛ تهدیدی غیرقابل‌پیش‌بینی که می‌تواند عربستان و متحدانش را به اسرائیل نزدیک‌تر و وابسته‌تر به توانمندی‌ها و اطلاعات اسرائیل کند
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/23480" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23479">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آسوشیتدپرس:
سقوط بقایای یک پهپاد حوثی پس از رهگیری در عربستان باعث کشته‌شدن یک نفر شد.
پدافند عربستان پهپاد را منهدم کرد اما بقایای آن روی منطقه مسکونی سقوط کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/23479" target="_blank">📅 21:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23478">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الجزیره: یک منبع مطلع آمریکایی اعلام کرده حدود
۶۰ میلیون بشکه نفت ایران، یا نفتی که مشکوک به منشأ ایرانی است،
روی نفتکش‌های تحت تحریم سرگردان مانده است. به گفته این منبع، نفتکش‌هایی که خارج از محدوده محاصره دریایی قرار دارند نیز در معرض رهگیری هستند و به همین دلیل با سرعت کمتری محموله‌های خود را تخلیه می‌کنند. همزمان، واردات نفت چین از ایران یا محموله‌های مشکوک به ایرانی بودن به حدود
۴۴۰ هزار بشکه در روز
کاهش یافته است
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/23478" target="_blank">📅 21:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23477">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOj9Yr-CG-zQSMVXMpR_hk3H53tv6AOMuwKN8-XwzBfIPNi8dM3SLujhxFysW3a4Nd9XNw2DFBHLXrzlM-Et3WUgUUrfrePOciqxZWCggqXwL7u-F0JrsT0xg9nSSn1O5UI77zvwiKM--l_BmMxNa2hFGQWbCM_jNaHNHTY8kd1OVaiJA83QeaYQ5Vh6rxVN94mjyh6quctkihUpTlhl_YX_JIH405OHbUjYuQSY63RKrDmjiuMgbPUBiASceD86ogayHS0UlRJCnFpLeYDngzNbjtnQUQg0At1Eoc35ZXtfO7fQxXqfffkqDPaPeSCpt7UdKo651AW0PKJuePjBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف
:
دوره‌ای که در آن F-35ها و F-15های شما شکار می‌شوند و مجبورید گزارش دهید که آسیب دیده‌اند
🤏
از قبل آغاز شده است.
آنچه زمانی سوخت خالص کابوس بود، اکنون واقعیت روزانه است. با آن زندگی کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/23477" target="_blank">📅 21:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23476">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الجزیره: وزارت خزانه‌داری آمریکا اعلام کرده اقدامات سختگیرانه‌ای علیه بانک‌ها و مؤسسات مالی در امارات و ترکیه که به گفته واشینگتن از ماهان‌ایر و شبکه‌های مرتبط با آن حمایت می‌کنند، آغاز کرده است. این اقدامات با هدف قطع مسیرهای مالی و خدماتی مرتبط با جمهوری اسلامی و ماهان‌ایر انجام می‌شود. آمریکا پیش‌تر نیز چند شرکت در امارات و ترکیه را به اتهام ارائه خدمات به ماهان‌ایر تحریم کرده بود. هنوز نام بانک‌های هدف، نوع دقیق محدودیت‌ها و زمان اجرای کامل این اقدامات اعلام نشده است. همزمان، ماهان‌ایر اعلام کرده از ۳۰ شهریور پروازهای خود به استانبول و آنکارا را متوقف می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23476" target="_blank">📅 20:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23475">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بر اساس گزارش رسانه‌های تحلیلی مستقل، دولت ترکیه ابلاغیه جدیدی به سنتکام ارسال کرده و هرگونه بهره‌برداری از پایگاه هوایی اینجرلیک برای سوخت‌رسانی یا هدایت پروازهای رزمی علیه هدف‌های منطقه‌ای را اکیداً ممنوع اعلام کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23475" target="_blank">📅 20:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23474">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ به نیوزنیشن : باید ببینیم که آیا ایران نابود خواهد شد یا خیر
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23474" target="_blank">📅 20:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23473">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ در پاسخ به سئوال نیوزنیشن درمورد گزارش روز پنجشنبهِ اکسیوس درباره «تصمیم بزرگ» او: «آنها حالا می‌خواهند به توافق برسند. اگر این توافق، توافقِ درستی نباشد، حتی به آن فکر هم نمی‌کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23473" target="_blank">📅 20:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23472">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: ممکن است به سمت جنگی تمام‌عیار با ایران پیش برویم.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23472" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23471">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: ایالات متحده در حال مذاکره با حوثی‌هاست و آن‌ها نیز به دستیابی به توافق با آمریکا تمایل دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23471" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23470">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">برنامه «پاداش برای عدالت» وزارت خارجه آمریکا برای اطلاعاتی که به مختل کردن سازوکارهای مالی سپاه پاسداران، از جمله حساب‌های رمزارزی، متولیان نگهداری دارایی‌ها و شرکت‌های پوششی، کمک کند، تا سقف ۱۵ میلیون دلار جایزه تعیین کرد. و همچنین اعلام کرد سپاه پاسداران…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23470" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23469" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رویترز: آمریکا به هیات اصلی جمهوری اسلامی، از جمله مسعود پزشکیان و عباس عراقچی، اجازه داده است هفته آینده برای شرکت در مجمع عمومی سازمان ملل به نیویورک سفر کنند. این هیات کوچک‌تر از سال گذشته خواهد بود، اما اعضای آن با محدودیت تردد در مناطق مشخص نیویورک و ممنوعیت خرید کالاهای لوکس و برخی کالاهای دیگر، از جمله عضویت در فروشگاه‌های عمده‌فروشی، مواجه خواهند بود.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/23468" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23467">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وال‌استریت ژورنال: تلاش جمهوری اسلامی برای دور زدن محاصره دریایی آمریکا از طریق انتقال تجارت به مسیرهای زمینی با مشکل جدی روبه‌رو شده است. صدها کامیون در مرز پاکستان و هزاران کامیون در مرزهای ترکیه، ترکمنستان و افغانستان گرفتار شده‌اند و تأخیرهای گمرکی و افزایش هزینه‌ها روند انتقال کالا را مختل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23467" target="_blank">📅 18:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23466">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حکم اعدام امید گودرزوند چگینی، ۳۷ ساله و از بازداشت‌شدگان اعتراضات ۱۸ دی در قزوین، در دیوان تایید شده است. او در زندان چوبیندر قزوین محبوس است و پس از ۴۰ روز نگهداری در سلول انفرادی بازداشتگاه اطلاعات سپاه، بدون دسترسی به وکیل محاکمه شد. به گفته این منابع،
این زندانی پیشتر از کارکنان نیروی انتظامی بوده و استعفا داده بود
.
@WarRiom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23466" target="_blank">📅 18:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23465">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تنگه صدای زوزه ابومهدی المهندس میاد
@WarRoom
😂</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23465" target="_blank">📅 17:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ادعای رسانه های رژیم :  شلیک ۴ فروند موشک کروز «ابومهدی المهندس» از جزایر ایران به سوی اهداف متخاصم در دریای عمان
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23464" target="_blank">📅 17:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23463">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیانیه نیروی انتظامی‌ ، فرد دستگیر شده در ماجرای تبریز دارای چه سوابقی بوده؟
نوامیس مردمو تو تاریکی با قمه خفت کرده! با چاقو زده لب و شکم یکیو پاره کرده
با قمه زده شُش یه نفرو سوراخ کرده، یکی از آنها با شیلنگ نفس می‌کشه!‌
مواد فروش هم بوده و
….
نیروی انتظامی همچنین اعلام کرد این سوابق به هیچ عنوان رفتار خارج از قانون مأموران را توجیه نمی‌کند. مأموران خاطی تنبیه انضباطی شده و پیگیری‌های قضایی ادامه دارد.
@WarRoom
یاشار : من انقدر به این مامورای نیروی انتظامی پول دادم که تمام رفتارشون رو توی شرایط خاص می‌دونم. از لحظه اولی که ویدیو رو دیدم کاملاً متوجه شدم که این قضیه ناموسی هست. در نتیجه با این‌که پیام های بسیار برای انتشار این ویدیو فرستادین ، از انتشار اون خودداری کردم. مثال خیلی ساده‌ای از طرز فکر و نگاه من و کسانی که این ویدیو رو فرستادن و بارها اصرار کردن تا منتشر کنم.</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23463" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش فاکس‌نیوز : دونالد ترامپ، رئیس‌جمهور آمریکا، در حالی وارد
هفته‌ای سرنوشت‌ساز در سازمان ملل
می‌شود که موضوعات ایران، چین و هوش مصنوعی هم‌زمان در کانون توجه قرار گرفته‌اند. نتایج یک نظرسنجی جدید «فاکس‌نیوز» نشان می‌دهد که ۷۱ درصد از رأی‌دهندگان معتقدند دولت ترامپ فاقد راهبردی روشن برای پایان دادن به جنگ با ایران است؛ این در حالی است که ترامپ در حال بررسی احتمال انجام حملات بیشتر علیه تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23462" target="_blank">📅 15:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فایننشال‌تایمز: ایران برای دور زدن محاصره دریایی آمریکا، انتقال بخشی از تجارت خود از مسیر دریا به مسیرهای زمینی، به‌ویژه مرز ترکیه، را افزایش داده است؛ ترافیک واردات از این مسیر در اوایل سال ۲۰۲۶ حدود ۲۵۰ درصد رشد کرده، اما تأخیرهای گمرکی و هزینه حمل‌ونقل افزایش یافته است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23461" target="_blank">📅 15:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آسوشیتدپرس: چندین هزار نفر روز جمعه ۱۸ سپتامبر در تهران در تجمعی حکومتی علیه آمریکا و اسرائیل شرکت کردند؛ مقام‌های جمهوری اسلامی از ثبت‌نام بیش از ۶۰۰ هزار نفر برای آموزش نظامی خبر داده‌اند، اما این آمار مستقلانه تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23460" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شرکت آرامکو سعودی به پالایشگاه‌های نفت اروپایی اطلاع داده است که در ماه آینده نیز هیچ محموله‌ای از نفت دریافت نخواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23459" target="_blank">📅 14:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو درباره ایران: اول از همه، ما باید رژیم ایران را سرنگون کنیم. این مأموریت من است و این مأموریت اصلی ماست. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23458" target="_blank">📅 14:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رویترز:
کره جنوبی اعلام کرد هیچ نیروی نظامی را برای ورود به درگیری خاورمیانه اعزام نخواهد کرد. سئول در عین حال در حال بررسی راه‌هایی برای حفاظت از کشتی‌های تجاری، مسیرهای انرژی و شهروندان خود در منطقه است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23457" target="_blank">📅 14:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایلان ماسک: «یا باید ویدیوگیم بازی کنید یا احمق بمانید؛ فقط همین دو انتخاب را دارید.» این اظهارنظر در واکنش به پژوهشی روی ۹۲۳ نفر مطرح شد که نشان می‌دهد گیمرها در عملکردهای شناختی، مشابه افراد حدود ۱۳.۷ سال جوان‌تر عمل می‌کنند. این مطالعه همچنین ارتباط بازی منظم با عملکرد بهتر حافظه، استدلال و سرعت پردازش اطلاعات را نشان داده، اما ثابت نمی‌کند که بازی‌کردن مستقیماً باعث جوان‌تر شدن مغز می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23456" target="_blank">📅 13:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzX9OfvAgTt-MVupiQbHy5dDVFnu8q8gUtJ5iLOpKFM2dI3FodKDBlzsoeBICkP5ZFo9HQvwzuTupTUGW5ZrxxfqM6S7fvSplY238_oixDOiACS-XF9P0maqQJHR_fqx-BZVO-7Z56kAIfUujrZEvHQdzK2KjhsDhcaN3EsjblomAIHwvDrR4JHZR3Pi9MfMe9GO1LlRJIdEgUoFSvHiD2977ejS5KJ60WUvHFpWc3ZuXSMX1e3DYHNEutMCGfECdVW-mMHE1sKg1FWMhmP5idn2fXhWlXzwdUs-mc2Z3lS7Q-i5YCMtbVgS-5lDZDb-bC1FD7L98fxz47TUKauGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود شرق تهران
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23455" target="_blank">📅 12:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23454">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جی‌پی مورگان: بیت‌کوین می‌تواند از طلا جلو بزند؛ تحلیلگران این بانک می‌گویند اگر سرمایه‌گذاران از مواضع دفاعی خود در
صندوق‌های قابل معامله در بورس (ETF)
بیت‌کوین خارج شوند، احتمال افزایش تقاضا برای بیت‌کوین و عملکرد بهتر آن نسبت به طلا وجود دارد. این بانک همچنین اعلام کرده صندوق‌های طلا بخش عمده خروج سرمایه‌های سال ۲۰۲۶ را جبران کرده‌اند، در حالی که صندوق‌های بیت‌کوین تنها حدود نیمی از خروجی‌های قبلی را بازیابی کرده‌اند.
بیتکین در این لحظه از 78,000$ عبور کرد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23454" target="_blank">📅 12:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUj_B4vyyPhbK4uD4Vi6rj1dA7tYrZiiWJZzosAQHkddik_MNjQ0KyG8xqDz4e5b58nWEp3W1qxsIbO6K9y-YmnPrAas_AWYZl_xYNorkCH1RL3tklRnCSf7Zo2IKkjGKe7vfwGptC29BcPq4ll1YE2ebbag9HLyTnb90Gmk6Q7b4_540-cD0ghUSyoippabbxuC7kU1Vvkdmv74XKYQLREDeS6NOa8fkDy5QNKnniBU3R1vCzXwEcY2xRI_rNl6zUeibZtTgu-TBGTOYh7HRb62ivgPDJuw0MzHnH6N5ExI2llGPdSw3an7tbchHtLehRsetA2KW1E9USyMXdhVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز جان فدا ریختن بیرون، رژه میرن. این وسط هم دوتاشون مزدوج شدن. قیافه داماد شبیه کندفیله(یه مار حشره خوار) نمیدونم بشناسینش یا نه
@WarRoom
😂</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23453" target="_blank">📅 12:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSJ7DcgAJqAc_t0NnDTUB4AI-dNx1ETT8TGDcC2zzrba6X0m8lklpxI3XCTa1ddw7-W7ePPdjcLxZ3mgKj-04o_eM6YCMZknJU2ONBHDFWSv6ATKmGxX9Xo0BKVCu8K1WCsOZs1Ul21EqIgzoI3JfE_5b5lHBBmzyX1IA3j3mHkG4KPUK_4G5g6d4PXGebz432n8pXgNha4NugK2hfpCg685Uc8OXOU3ineVd6zvsLV2TXkIDMP_A7soU6dAPaqUuMq5Ctkl2u28Ayy1I8UV-uUC2R4v7ug3khs7hMHyGi03sEDyr9oJavoMczXsZhdCi7_NesaK2mVxGjT3Ul2c-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sR6_GiRI_4jaqnqzKRZ0B4nzz7te0OFUUdEpjyYKtlWWErX5b3xNjgBwbInrK99bScVAlIVe1Vplio8boHWfbmKmOmUSFVUdN3SOXrDA8Yz7F9n8yDWAVQsLMDJ4WWZR7cJL2w3r8BfhqjDntFVVIqd8gNFnzFPlYLmgpSoEuprdwcKUnu5PVii8DHzolEteH9mTxFyuNo-U4D6Tu_l93Cv9nJHuyFaM7gm5X9gNU2D_aKjof7D3opg4iiPPpZZ_4lD8iauUY_m_JUudozWgbHhX_Om6SXRN-U-ecDzoJW6MayWiDkgcjz54efhJeRkm03OojdzjgiCzvZMirtFWUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمله به سه نفتکش در حوالی تنگه هرمز
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از دو حادثه جداگانه علیه نفتکش‌ها در منطقه تنگه هرمز خبر داد.
حادثه اول: طبق هشدار شماره ۱۳۸-۲۶، یک نفتکش در تنگه هرمز هدف پرتابه‌ای ناشناس قرار گرفت. اصابت پرتابه باعث آتش‌سوزی در کشتی شد، اما آتش بعداً مهار شد. خدمه سالم گزارش شده‌اند و میزان خسارت هنوز اعلام نشده است.
حادثه دوم: طبق هشدار شماره ۱۳۹-۲۶، یک نفتکش در هنگام حرکت به سمت خروج از تنگه هرمز، هدف پرتابه‌ای ناشناس قرار گرفت. در این گزارش، آتش‌سوزی اعلام نشده و جزئیاتی از میزان خسارت نیز منتشر نشده است. خدمه کشتی سالم هستند.
حادثه سوم : تایید نشده دیدبان های اتاق جنگ به من از حمله به کشتی سوم هم خبر میدهند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23451" target="_blank">📅 11:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM3ceEhSzTjNBaZ_l8kW75nLP7n-KvZ2woQpA2l9OC6D7vSFrOBQ_27mvR5neaQZF865-Qbl972lP7BlusX9xU_tZ7PjWPPrWJjzeLqtzk8Lj9cM3Uwk2bQZu0avsCDnSm0WKU2xbQcYC0UyArLVR2iyX6YIUVyJFY6vxR0pgitINqd4skC19gSDVEJcsB2A5KHE7uU5kfQbBN8QaI2_olhtLyEG-YiachDiydNCsnuHgmRjG1kbEB_gkpn333KOh6GwetebSEdbIHOwKumZEqUh7QHYQOtJWhojiS_c1vdF156FtYA1K0hy4IXzt8ZhBwQnA-EPdNOPtHuaGrfmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌ با بازنشر مقاله‌ای از واشنگتن‌پست درباره افشاگری‌های داخلی پیرامون جنگ ایران نوشت: «خیلی جالب است. حتماً بخوانید! به افشاگری ادامه دهید،
سگ‌های کثیف
!
وقتی شما را پیدا کنیم، بهای سنگینی خواهید پرداخت!!!
» مقاله مارک تیسن، ستون‌نویس واشنگتن‌پست، استدلال می‌کند افشاگری‌ها درباره هشدارهای تولسی گبرد، مقام‌های ارشد نظامی و جی‌دی ونس درباره خطرات حمله به ایران، به‌جای اثبات اشتباه ترامپ، نشان می‌دهد او برخلاف توصیه‌های مخالفان جنگ عمل کرده و تهدیدهای حکومت ایران را جدی گرفته است. تیسن همچنین اقدامات ترامپ علیه ایران را یکی از جسورانه‌ترین تصمیم‌های سیاست خارجی یک رئیس‌جمهور در دوران زندگی خود توصیف کرده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23450" target="_blank">📅 11:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23449">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقامات آمریکایی:
ترامپ در حال تقویت رویکرد متفاوت برای پایان جنگ اوکراین است؛ پیشنهاد قرارداد تجاری با روسیه
کاخ سفید در حال بررسی امضای قراردادهای تجاری با روسیه، حتی پیش از توقف درگیری‌ها ست
ترامپ می‌خواهد انگیزه‌های بیشتری برای نخبگان روسیه ایجاد کند تا برای صلح فشار بیاورند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23449" target="_blank">📅 11:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد ایالات متحده رسماً از
شورای حقوق بشر سازمان ملل متحد
خارج شده است. واشنگتن این شورا را به ترویج «ادبیات ضدآمریکایی» و اتخاذ رویکردی مماشات‌گرانه در قبال حکومت‌هایی که به سرکوب مردم متهم هستند، متهم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23448" target="_blank">📅 10:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJUPgXebz-1xxNtBRLVAiXoI48nK3m9PbgXxIKSNTTtZb4NPlk_1CjyhbuhYEt2XP5niHFvulpEnmbWJ1GpkodyIXKWVGTO0th3FvJnyf-iA3t_LvMWKJZ4IlSFzn9U3eJe7MjYDA7HBN1ihnRAZmMtBCX1pA57KV_cqLkuFsSQkYyGn55VIIxzInDmBx1mMVkW_3cJCxlaAh7wrXfXQi57FhtTb_E-Ie7HeXX3y-oMh-Ej8t9i9weEUp4RpUEg9fkF56o9olAijWyjpaFz03jmTaX3Uo9PCalBd7L7G7oFXXl3JUZb-YIJw2Ef56X8GkeL6tcWLy1I1YWNitaDW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EwBMDgi7zxEn1dtAaP9RFAfkKdx2NLwZbJCxXvVfsL70VAvlaj0XhJtLLdPfwW5cmhYc95UgQ6Rbq6E_ctc6UJk0WFM9py0KCXCR-f6AkkXhNhX6FKqfm-xItFgBnQQHTpI6r2G6fLP6SUyOPqLODefJk0Hq9VVMnIdBeu79LKgjRhegtn4L--3V7q7N6ZPIjRpBtbsxoVWvsTyqA-mMrgJ7ihiK2e6aEmYrGKWNQIRkdn5hpe4xs4-8ZJvH42EoGHIzAudcMBAFAzqNVjH2pY91sUJARlOyNXwHNpqOBimrBwem2l2Jzly0u1CP-z-F2zS8T8r6qIn8a7pgkG2W_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRq88fbMIaFDSTZjPlfKcgGs9HsT_xn7EP8DI8IdQ7HCMdQwkr-fdlc10NreAf0AO0oo5_fE9CtfHIQxfeMHoZp2TQnViLV4OhRAIvJl4GUi3J6Jg6zbjKUKWwfIrnJleBABFJE0ANWf08oAeD0b5Obm-xkfJgJQFfH46zmsUB5pb0FGF3j2dBFuKWjdbvMLWblfpGxh8xGHiJoLIdjZ-4LzEnHHxW1zalhzonj-ZfuUme4MDXeTPNSyLGTuo5Rpr8Ed8ZxCMU1dw-3ccAiOOoawAf5PjASID4eoISS1SG5MAanQW5yHOt8wnJhevqI0OnCHiQNnm3BUrtdnnjoZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQFCrnmQHC2cMNqHoNS2UtUGeCPdJaH2in8iSMscQbr0t9kcjvX4MiwK6bKoks5yh4UbZ1CQd7CHpBQiOR8D0hqSFltu_-nmfS5Ad_OnJTyeh3BOsBjfWlRlJP5DZ5wq-Loxe_KbOzgnqhp54dgDGQGKWkUYsKa-dlSNQneC14WQ66au5vKtdc58TAQErdml4DBpQUynp-_Ax-iMqgfuQctp68YDXGDv1sVSTbw7uIOtby7k_43rS5ucsa98Jyf9Lr8l5jL6Uhx44VVKrz0OaP0RyfLLb2iYbL5RVsJEgUgYDosv8N6yM5WkbC5JMo2lY95SdKQk9InNcZnoYjcF7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آسوشیتدپرس: آمریکا در حال تکمیل خروج نیروهایش از عراق تا ۳۰ سپتامبر است و یک مقام نظامی آمریکایی گفته صدها نیروی باقی‌مانده در شمال عراق عمدتاً به اردن و دیگر کشورهای منطقه منتقل خواهند شد. تجهیزات نظامی، از جمله سامانه‌های پدافند هوایی نیز از عراق خارج می‌شوند. روز گذشته گزارش داد یک کاروان تجهیزات سنگین آمریکایی شامل خودروهای زرهی و کامیون‌های نظامی در غرب عراق مشاهده شده که در حال انتقال به سمت اردن بوده است. جزئیات دقیق نوع تجهیزات و مقصد نهایی آن‌ها هنوز به‌صورت مستقل تأیید نشده است.
یک مقام نظامی آمریکایی گفته خروج از شمال عراق «ریسک ما را برای عملیات‌های پیشرو کاهش می‌دهد».
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23444" target="_blank">📅 10:22 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
