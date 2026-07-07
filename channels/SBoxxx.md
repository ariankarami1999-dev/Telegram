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
<img src="https://cdn4.telesco.pe/file/Q5bQerLrruWcGnfcM4v_BY8UMdOi70z9JWx__wsBi80nM3yiHVvOT3lgG9jgki6p7RCn5vznReU25PHUM_lvD-rMvj4Y7EaiLb1afDicLOc0dD3RYE6hKA4GsJqP8hC1Sm1UeScdswNAhsHFsPtp-S-x6R15YiMKz-CVnBna9QqwnLxySnb_0KHxDWjNUHmk4MRx14HMylMIxH36qE7S7sXQIfMknenwz5qMTAYuUPmaFMOfOobYb7uuD3aG3HafYwibTiG5p26N9KZrhrX0olPQiNwqG-iPC50-vESL9zm6ep3CrxDtrDgXnveMhtr5hELgfawoNxeiw7h0_KvVIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 19:49:56</div>
<hr>

<div class="tg-post" id="msg-18283">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دبیرکل ناتو در مورد ترامپ:  من از این مرد خوشم می‌آید.  به نظرم کاری که او برای ناتو انجام می‌دهد خبری عالی است زیرا، بله، یک تهدید روسی وجود دارد، اوکراین وجود دارد، بنابراین ما در هر صورت مجبور بودیم در اروپا گامی برداریم.  اما او چیزی بود که برای ایجاد…</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SBoxxx/18283" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18282">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">روته، نماینده ناتو در آنکارا:  ما روز سه‌شنبه در مجمع صنایع دفاعی، ده‌ها میلیارد دلار قرارداد جدید را اعلام خواهیم کرد.</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SBoxxx/18282" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18281">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFJZUuA5-HPoYEnAQpUEzb2LdJYeQSg7rY4-g9-MPmvcWV7apzMoe_uhP4SQz_-Oz4XcJEsBdE1jTDyQYRyv8AcPB4z9F8l8tq4sA6abofnB8tXZzGYg71FheDC96xeHuqY9JMbrAzqASo1Mrt6o5MrPUCt9vpintB3ls982t87rgCAzTV2WQJ9fov_9wo3Y1ql_8EoSqlCB36ElAv8VgvTNv40F-_NknkElNXVBqnVgZ9bxPDQG85Cb9KgaOhQ1IrWCKWoC0qs6SYs3pi4ttq0nnxhm16HA2yB570Est3I6vJ7e84u0lSiAAWkR-6fY7gq0UGqlchxZ8YjaBKjNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SBoxxx/18281" target="_blank">📅 18:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18280">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6EkR859cERWqDK3cbblxpK4kJgmLtpTiusSb7vtEANf4Zi57JuXTqUGP1DG0hNQcY7NhsTB4Wv2E0DGCA622fbaH4rYhz0aLdmI_xz3fjtxz9Ga0aJpAYUW9hceMpvdflpBCrGSiOnz-9_SMtGVPfjcgyf57zB_8fWJpVbeQt5nO_ONca7OhgTb-NpqHUgu87PF1lcpdbsBJ25lCrJvR_7nynIDyHAKgR63oPzEmP1yaVIN0PxdrIt3cRKyyD-srkZ5p10QAv3a8H0VUnZXzi7ogxVC_Ecxe76Z4m0rA_3MA-PLoqoVg5r1H2Hu_xg1hnAIMUS0AGuYXAcDMXwmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">90 درصد این دولت ها را زردپوست هایی تشکیل دادند که از دید چهره و ریختار هیچ شباهتی به این دلقک های اردوغان نداشته اند.</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SBoxxx/18280" target="_blank">📅 18:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18279">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سیرک جدید اردوغان!  لباس‌های تشریفاتی که نمادی از ۱۶ دولت بزرگ ترک در طول تاریخ هستند، در محوطه ریاست جمهوری مشاهده شدند و در صف ایستاده بودند تا از رئیس‌جمهور ایالات متحده، ترامپ، استقبال کنند.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/18279" target="_blank">📅 15:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18277">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSjLhTZFyaOcRnwNv1cTJeHmzLGpoVCjFbLiE4NPAT2I3rDnnCTnD_vtSVi6tSh6G_Evt7BEKRbv0lzJs2CSRoQ_jF7VsvKbkrH-tHZ1xlObLQdofhtl6-zAQ-JzMysj3ZOALNS4U7BXicBkojNhIRnczeIRbQINGIEmcOE9losK5_MaiQabsCVJWmVYAs_cuQnFQ1yU9_K2tsYrj79bkDYvBLpUBduDI1ac1WSGyjxH7uCVZm95SXDs49NAjTMD9FFpot8X0Vev-f9OU7SDIfmzpQg6QFi36n_7qS-HL9S_U62WF_PqdL4MO2GNWrSy5W3QdGYFVPlLiBQXPfNAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NC-KvMl2FwgA-TL7Atz2_77WlYiQCvP25OQtMjpnyaDuav_LVRHZSs2gO1lriRWIrCYjkvk6EBgnlBUn93tedAbHxCU8IPYLYz4gYB1MaP9Ie3Y7X1T7pzEFRwD1Xfed4KiiMBbrnsdK0FjS2dqmcVLfU6QXlz3xHhw0rnl5Log7Ht9jepuv3XGe9G8wNW345bABk9MIjHO_mHS5g2oWmAZ5DEku-bztTAGDAsrSfxchKdPC-qOA0KakWjUEF4K7oNQ-kTg164XZQOJQxlJmhugE6t5F4di6A1c1rUxizqCS-KfMziasfvL2n7zchEEuqjOqz5gA0mNbKYDfFBshLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جدید اردوغان!
لباس‌های تشریفاتی که نمادی از ۱۶ دولت بزرگ ترک در طول تاریخ هستند، در محوطه ریاست جمهوری مشاهده شدند و در صف ایستاده بودند تا از رئیس‌جمهور ایالات متحده، ترامپ، استقبال کنند.</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/18277" target="_blank">📅 15:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18276">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/18276" target="_blank">📅 14:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18275">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/18275" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18274">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/18274" target="_blank">📅 14:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18273">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoC51aRkhxWlQjZ4gRv3fg4K2auD4NMrTXxFSOHFuzjUjoSl7BsgNdl37i3wk27vlyYoN2iriT48sK9ZrTUWsKWI9vSBHWBwCn-ofON11eU_1qPbDBDkmWtKmQ_U6QEEFZ-KiIicMl-Hk374bMGqZLScTCkCraglmYIv2fLWgL_dFEasBe6H6o3d0i7_uXm0OVpfNdMMF0Q5BQKaSIn_swO65OZy3WDSmS9MSO7IzfoacUjgQ4UCUf8I1jkfIBvcJOI7_COcsr7tXBnnRL1VEKstqjROH1FK1r9M7JSLqlZOvhM8GbnZHfQ7dFFKJAlTiDF0wSYz8e-u95GCCG-Eew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایه کشتارهای قومی بر اتحادهای ضدروسی
تنش‌های اخیر میان لهستان و اوکراین نشان می‌دهد که حتی نزدیک‌ترین متحدان نیز نمی‌توانند از سایه تاریخ بگریزند. در حالی که دو کشور از زمان آغاز تهاجم گسترده روسیه به اوکراین در سال ۲۰۲۲ همکاری‌های نظامی، امنیتی و سیاسی بی‌سابقه‌ای را تجربه کرده‌اند، اختلافات مربوط به حافظه تاریخی بار دیگر به سطح روابط دوجانبه بازگشته است. مصاحبه اخیر کیریلو بودانوف، رئیس اطلاعات نظامی اوکراین، با شبکه RBC-Ukraine نیز بازتاب همین واقعیت بود. بودانوف در واکنش به آنچه «اقدامات نابالغانه» لهستان خواند، تأکید کرد که کی‌یف نباید با واکنش‌های شتاب‌زده تنش را تشدید کند و امیدوار است پس از دوره‌ای از افزایش تنش، دو کشور به سمت کاهش تنش حرکت کنند.
زمینه این اظهارات به مجموعه‌ای از تحولات اخیر بازمی‌گردد. در آستانه یازدهم ژوئیه، سالگرد
کشتار ولین
، فضای سیاسی لهستان بار دیگر تحت تأثیر مطالبات مربوط به بازخوانی گذشته قرار گرفته است. هم‌زمان، اقدام اوکراین در نام‌گذاری یکی از یگان‌های نظامی خود به نام ارتش شورشی اوکراین (UPA)  واکنش‌های تندی را در ورشو برانگیخت. برای بخش بزرگی از جامعه لهستان، UPA  نه نماد استقلال‌خواهی، بلکه مسئول یکی از خونبارترین فجایع تاریخ معاصر این کشور است. در مقابل، بخش قابل توجهی از جامعه اوکراین این سازمان را نماد مبارزه برای استقلال در برابر سلطه شوروی می‌داند. همین تفاوت بنیادین در برداشت از تاریخ، بار دیگر شکافی عمیق میان دو متحد ایجاد کرده است.
ریشه این اختلاف به سال‌های جنگ جهانی دوم بازمی‌گردد. ارتش شورشی اوکراین (UPA) در سال ۱۹۴۲ به عنوان شاخه نظامی سازمان ملی‌گرایان اوکراین شکل گرفت. هدف اصلی این نیرو ایجاد یک دولت مستقل اوکراینی بود؛ دولتی که نه تحت سلطه آلمان نازی باشد و نه اتحاد جماهیر شوروی. اما در کنار مبارزه با این قدرت‌ها، UPA  وارد درگیری خونینی با جمعیت لهستانی ساکن مناطق ولین و گالیسیا نیز شد.
در سال‌های ۱۹۴۳ و ۱۹۴۴، نیروهای UPA مجموعه‌ای از حملات گسترده را علیه روستاهای لهستانی آغاز کردند. بسیاری از مورخان معتقدند هدف این عملیات‌ها حذف جمعیت لهستانی از مناطقی بود که ملی‌گرایان اوکراینی آن‌ها را بخشی از سرزمین آینده اوکراین می‌دانستند. اوج این خشونت‌ها در ۱۱ ژوئیه ۱۹۴۳، موسوم به «یکشنبه خونین»، رخ داد؛ روزی که ده‌ها روستای لهستانی به طور هم‌زمان هدف حمله قرار گرفتند. برآوردها نشان می‌دهد بین ۵۰ تا ۶۰ هزار لهستانی در منطقه ولین و در مجموع تا حدود ۱۰۰ هزار نفر در ولین و گالیسیا شرقی جان خود را از دست دادند. در مقابل، عملیات‌های تلافی‌جویانه نیروهای لهستانی نیز به کشته شدن چند هزار غیرنظامی اوکراینی انجامید، هرچند از نظر ابعاد و سازمان‌یافتگی، بیشتر پژوهشگران معتقدند خشونت علیه غیرنظامیان لهستانی بسیار گسترده‌تر بوده است.
همین گذشته، امروز نیز منشأ اختلاف است. پارلمان لهستان این کشتار را رسماً «نسل‌کشی» توصیف کرده و خواهان پذیرش کامل مسئولیت تاریخی از سوی اوکراین است. اما در اوکراین، اگرچه بسیاری از پژوهشگران وقوع جنایات گسترده علیه غیرنظامیان را می‌پذیرند، بخش مهمی از جامعه سیاسی همچنان UPA را نماد مقاومت ملی در برابر سلطه خارجی می‌داند و با اطلاق عنوان «نسل‌کشی» به این رویداد موافق نیست. این دو روایت متفاوت از گذشته، امکان دستیابی به یک حافظه تاریخی مشترک را بسیار دشوار کرده است.
با وجود این اختلافات، بعید است تنش‌های کنونی به فروپاشی همکاری راهبردی دو کشور منجر شود. لهستان همچنان یکی از مهم‌ترین مسیرهای انتقال کمک‌های نظامی غرب به اوکراین است و امنیت دو کشور به طور مستقیم با نتیجه جنگ روسیه و اوکراین گره خورده است. از سوی دیگر، ورشو نیز به خوبی می‌داند که تضعیف اوکراین، فشار امنیتی روسیه بر جناح شرقی ناتو را افزایش خواهد داد.
با این حال، تداوم این اختلافات می‌تواند پیامدهای ژئوپولیتیکی قابل توجهی داشته باشد. نخست، شکاف‌های تاریخی میان دو کشور می‌تواند انسجام سیاسی جبهه حامی اوکراین را تضعیف کند و روند تصمیم‌گیری در اتحادیه اروپا و ناتو را پیچیده‌تر سازد. دوم، روسیه همواره تلاش کرده است از اختلافات تاریخی میان کشورهای اروپای شرقی برای ایجاد بی‌اعتمادی و کاهش هماهنگی میان آن‌ها بهره‌برداری کند و چنین تنش‌هایی فرصت مناسبی برای عملیات اطلاعاتی و تبلیغاتی مسکو فراهم می‌آورد. در نهایت، اگر ورشو و کی‌یف نتوانند میان ضرورت‌های امنیتی امروز و اختلافات تاریخی دیروز تعادل برقرار کنند، یکی از مهم‌ترین شراکت‌های راهبردی اروپا ممکن است با چالش‌های فزاینده‌ای روبه‌رو شود؛ شراکتی که حفظ آن نه تنها برای دو کشور، بلکه برای معماری امنیتی کل قاره اروپا اهمیت اساسی دارد.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/18273" target="_blank">📅 13:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18272">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟   هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/18272" target="_blank">📅 12:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18271">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟   هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز…</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/18271" target="_blank">📅 12:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18270">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Okm4u0sbByaeCd0VUIJOaZsfpcr7NNaqATVWCOn7GiE_QurTyOq9ocMT7inOXZULT6Jn8bYLhV3wH8zEWFAYbiZu6bERqRYISe4FR7V6Vgjw4I2Cv32aAwP7JI6kUH5yEAfNHVecRd_f105jFse-Ai_53XYoCuReInDC5MmXmiNZ0syR6i27IrCnrhAguyKbpVBACMx5Kn0lY-I7mWow95J4ZnQ8U_0NkTXHEZo2YxKOOIANKM5ojrKPZy0bJXx2wiyLDL0aV4d3nxBRA6aOEgWhzkRf_1boW7luoktiaLbi82I2ZJcjEMIjVby_4VAJS1Gu98XMGnD-B2iXGKFoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟
هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز دارد و میلیون‌ها درخواست روزانه کاربران، فشار بی‌سابقه‌ای بر مراکز داده وارد می‌کند. نتیجه این روند، رشد سریع مراکز داده و افزایش چشمگیر مصرف برق آن‌ها در سراسر جهان است.
این تحول باعث شده است که انرژی از یک عامل جانبی به یکی از مهم‌ترین چالش‌های توسعه هوش مصنوعی تبدیل شود. در بسیاری از کشورها، شبکه‌های برق برای تأمین نیاز مراکز داده جدید با محدودیت مواجه هستند و شرکت‌های بزرگ فناوری سرمایه‌گذاری‌های گسترده‌ای در نیروگاه‌های هسته‌ای، انرژی‌های تجدیدپذیر، سامانه‌های خنک‌سازی پیشرفته و طراحی پردازنده‌های کم‌مصرف انجام داده‌اند. امروزه دیگر تنها پرسش این نیست که چگونه پردازنده‌های سریع‌تر ساخته شوند، بلکه این است که چگونه می‌توان انرژی لازم برای به‌کارگیری آن‌ها را فراهم کرد.
در چنین شرایطی، توان محاسباتی به یکی از مهم‌ترین منابع راهبردی جهان تبدیل شده است؛ منبعی که می‌تواند بر رشد اقتصادی، پیشرفت علمی، توان نظامی و رقابت میان قدرت‌های بزرگ تأثیر تعیین‌کننده‌ای داشته باشد. از این منظر، رقابت آینده تنها بر سر منابع انرژی نخواهد بود، بلکه بر سر تولید توان پردازشی نیز خواهد بود.
همین مسئله موجب شده است که پژوهشگران به دنبال الگوهای کاملاً جدیدی برای رایانش باشند؛ الگوهایی که بتوانند با مصرف انرژی بسیار کمتر، توان پردازشی بالایی ارائه دهند. یکی از جذاب‌ترین این مسیرها، رایانش زیستی یا Biological Computing است.
مغز انسان نمونه‌ای شگفت‌انگیز از یک سامانه پردازشی بسیار کارآمد محسوب می‌شود. این اندام تنها با مصرف حدود ۲۰ وات انرژی، وظایفی بسیار پیچیده مانند یادگیری، تشخیص الگو، تصمیم‌گیری و پردازش هم‌زمان حجم عظیمی از اطلاعات را انجام می‌دهد. در مقابل، آموزش یک مدل پیشرفته هوش مصنوعی ممکن است به هزاران پردازنده گرافیکی نیاز داشته باشد که هفته‌ها یا حتی ماه‌ها به‌صورت مداوم کار می‌کنند و انرژی بسیار زیادی مصرف می‌کنند.
همین تفاوت چشمگیر باعث شده است که برخی مراکز تحقیقاتی، امکان استفاده از نورون‌های زنده، بافت‌های عصبی و اندام‌واره‌های مغزی را برای انجام برخی وظایف محاسباتی بررسی کنند. هدف این تحقیقات، ساخت سامانه‌هایی است که بتوانند از ویژگی‌هایی مانند پردازش موازی، یادگیری تطبیقی و بهره‌وری فوق‌العاده انرژی در سامانه‌های زیستی بهره ببرند.
البته این فناوری هنوز در مراحل ابتدایی قرار دارد و فاصله زیادی تا کاربرد عملی و جایگزینی رایانه‌های مبتنی بر سیلیکون دارد. افزون بر این، مسیرهای دیگری مانند رایانش فوتونی، تراشه‌های نورومورفیک، شتاب‌دهنده‌های اختصاصی هوش مصنوعی و رایانش کوانتومی نیز با سرعت در حال توسعه هستند و هر یک می‌توانند بخشی از نیازهای آینده را برطرف کنند.
با این حال، یک واقعیت بیش از پیش آشکار می‌شود: در عصر هوش مصنوعی، توان محاسباتی در حال تبدیل شدن به یکی از ارزشمندترین منابع راهبردی جهان است؛ همان‌گونه که نفت در قرن بیستم نقشی تعیین‌کننده در اقتصاد و سیاست جهانی داشت، ظرفیت پردازش اطلاعات نیز می‌تواند به یکی از عوامل اصلی قدرت در قرن بیست‌ویکم تبدیل شود.
اگر روند رشد هوش مصنوعی با همین شتاب ادامه یابد و محدودیت‌های انرژی به یکی از موانع اصلی توسعه تبدیل شود، احتمال دارد پژوهش درباره معماری‌های نوین، از جمله رایانش زیستی، از یک حوزه صرفاً دانشگاهی به یکی از مهم‌ترین عرصه‌های رقابت فناوری تبدیل شود. هنوز مشخص نیست که آینده رایانش بر پایه سیلیکون، فوتون، سامانه‌های کوانتومی، نورون‌های زنده یا ترکیبی از آن‌ها خواهد بود؛ اما آنچه روشن به نظر می‌رسد، این است که رقابت برای دستیابی به توان پردازشی بیشتر با مصرف انرژی کمتر، یکی از مهم‌ترین رقابت‌های علمی و فناورانه دهه‌های آینده خواهد بود.</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/18270" target="_blank">📅 12:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18269">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry1lEMG-jWUn8-0hpL9IywftrgXq028Nnbwf-UA1wraJm_3MbgMl-tXmuy2YO3bt25gC4J6xDF3ngHNT1vEzIV0nvOhH4nTrsNKD8-5-ZUuOXdYY4onwdwLH_qwi-XekR9wtDSBiSQG84gOJIPI_vf0INJcUzvQ64htKRlBfcQQsoUgHtueA19zIK4Zpmbk9SRIqFxi8F1B5B2stSrP4ak4fpHLelsa6f4ViZvi41AGiCSQlKW9EwaJMi_M9pXeAXC-2rzhfesfCjArskmlkF4E7CqPSiIv-UgyIoMHLK0IAjKDNSXXnxBblMHFyL2YgNeqX_XORGDt_SkwyL_l6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای پرشمار در دمشق نزدیک محل اقامت شیفته صبیه رفیق بهزاد.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/18269" target="_blank">📅 12:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMOQ-hKDZqLtR5bGEPm8y6ksZIvXplG2osjY_JG0Yrq9k2FQ4BwANqgvBtAJPiojhHbfm3p8Uv9NucTUKMiHatGT1I5oLXOJWjWv8Y9EMAQlhPyDfLElHtIBFCs2QlsFoUMg2orLkoRK6cP9X11_3QGyIKDD0Bi9ZIZ4PxaXyy7zUmd32cG4Nt7ReUtIFgLQp7hHDabcQLLW0I8EVbHQTGq3aBgzljAtQileCLcaz2Ya0mWKhG8cT43NN4XPD8Ose1JfqRDG_HaWU_7MlmdACrLeuURFtPFVHbWgukXjPEdsChM9pQjSFskvOsCFKZ8xsqmsN4uYuMAB10OrocqR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهید لاریجانی اصرار داشت با مال دیگران داماد نشوید ولی خب.</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/18268" target="_blank">📅 11:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">راه‌حل شاید ملانیا باشد!   تهدیدهای تکراری ترامپ در مورد تخریب ساختارهای اقتصادی و زیربنایی ایران در صورت شکست مذاکرات، تنها کارکردش این است که جمعیت اصطلاحاً خاموش کشور را به حمایت از جمهوری‌اسلامی و بیزاری و نگرانی از آمریکا و اپوزیسیون وابسته به آن، ترغیب…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/18267" target="_blank">📅 11:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این زیدآبادی دستکم ۲ تخته اش کم است!</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/18266" target="_blank">📅 11:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18265">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">در سوریه، ایران و اسراییل مشترکا از گروه های ضدجولانی حمایت کرده و او را یک قاتل داعشی کت شلواری میدانند!</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/18265" target="_blank">📅 11:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18264">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY4R0Bv86qbqnxNFyQXAsVnFnXEcmfooW9Z8Zu3VvVN0wOvgJq4UpsCrsjj7_RFXBBbR7eqsUhhONLRb_N5S2yciDV7qjMUvgJLjwRsDCSCFWtfedMmt5819_K1qUV-xpm1wY1sSoGnhICPPyn9d0DN2SyNgvQxqamiHQFjkO-FpVVIBPB6VH97cqYYzUZl7Ys8MiPum0FDKyrXEmaKSdDXXl3k3NVHXZqoFDdmLI3znuReTOfzlCNmRM9oYL6ot4DcnLhTN4zu0F8WF40QOCk_gNr2mXpaef-8YUEBVFJQqh5KaMWAK4Iko0VDXWi1RN8RnEx72G2Y_YlVxCX_mlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایین قرار دارد و ادامه شرایط نرمال پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/18264" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18263">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 2  دوشنبه 6 جولای 2026</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/18263" target="_blank">📅 10:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18262">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">◆ روزگاری وقتی اف 14 فول تراتل روی دریاچه ارومیه پرواز میکرد ،نعره موتور تی اف 30 تا اتاق خواب مادر الهام علی‌ اف میرفت . اما امروز تاندر تحویل گرفتند و با وضعیت فعلی آسمان ایران،می‌توانند تا تهران بیایند سلفی در کابین بگیرند برگردند . این حجم از اختلافی که…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/18262" target="_blank">📅 10:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18261">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParvaz dar oj</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1a9F2v78hZAyRh8Qntbl1jBlppLHoNn-irS2rEBt0ad67RH9hnt7UYK0PZIJSC_rY2O1CsVBzPgtqaBGodPCVgGnn_8e-V3WZl643jDeJ8QI0e_unk8Az05E-aGzsxeMTvqRxq7BTZgTiSp0385YoJ8oTpiQ3byKkjHbC-63A5rbAIrnmIsXrTuAbbS9Ec60UlliN6dCFfSHDcfL-9umKfd6aKNeffuM1v574Hllycfsse8iaxhIRHfP5_719cFezZ5Yof8fJbt5lhpd-BxYilWWjQlARaL_tinNSLFNje4QcPvdPcM2JUlvdxzLGIr6UinzCeLX29AseVA51n1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◆ روزگاری وقتی اف 14 فول تراتل روی دریاچه ارومیه پرواز میکرد ،نعره موتور تی اف 30 تا اتاق خواب مادر الهام علی‌ اف میرفت .
اما امروز تاندر تحویل گرفتند و با وضعیت فعلی آسمان ایران،می‌توانند تا تهران بیایند سلفی در کابین بگیرند برگردند .
این حجم از اختلافی که افتاد واقعا خرابکاری نیست،شاهکار است!!!
@PARVAZDAROJ
| 𝐀.𝐑.𝐀</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/18261" target="_blank">📅 10:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18260">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جمهوری باکو به برنامه اوکراین در زمینه پهپادها پیوست     معاون دبیر شورای امنیت ملی و دفاعی اوکراین، دیوید آلوویان، در مصاحبه با گاردین اعلام کرد که در ماه‌های اخیر، کی‌اف توافق‌نامه‌هایی در چارچوب برنامه Drone Deal با شش کشور امضا کرده است و به گفته او جمهوری…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/18260" target="_blank">📅 10:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18259">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جمهوری باکو به برنامه اوکراین در زمینه پهپادها پیوست
معاون دبیر شورای امنیت ملی و دفاعی اوکراین، دیوید آلوویان، در مصاحبه با گاردین اعلام کرد که در ماه‌های اخیر، کی‌اف توافق‌نامه‌هایی در چارچوب برنامه Drone Deal با شش کشور امضا کرده است و به گفته او جمهوری باکو نیز در میان این کشورها قرار دارد.  این برنامه شامل توسعه مشترک، تولید و صادرات پهپادهای اوکراینی و همچنین تبادل تجربه جنگی بین کشورهای شرکت‌کننده است.</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/18259" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18258">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پاسخ دبیر شورای عالی امنیت ملی به ترامپ</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/18258" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18257">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPbzYpqDxoEBJxSsna4j6DQlKmlV7OfOb6JfFd8RyuWtKaDf9OwSiamcaPaDe0oXmaepQnbxASY3pq4qNiB588YEGPJd0rOoKiQSmsP162IOh3H25HhMbpd_JlxfjXGeqcPCd5WrrrdNrs8DstV9CTW4uJ4VBvh1ienIXZBKOlB_Tfefa6WbTk09BflrUPXnOIx0ZlIHKm_k5EgslVMRDbd00kUBgPnbx9xrHlAW1OE_04bzeDzLx6ygcXfqydHQMuDB2Lm0ys519C47LtIZHvDx32ur77OYpnYTisXtGhQ0zEsXwZJCRASsE_g0q6nO33priCHT0aMEDwHQ-akyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ دبیر شورای عالی امنیت ملی به ترامپ</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/18257" target="_blank">📅 09:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18256">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/18256" target="_blank">📅 09:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18255">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مسئول آمریکایی به اکسیوس:
بیبی وعده‌های زیادی درباره جنگ با ایران داد که محقق نشدند.
اما چه کاری از دستمان برمی‌آید؟ او خواهد آمد. او وعده‌هایش را می‌دهد و سپس ما مجبور خواهیم شد همه چیز را بررسی کنیم.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/18255" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18254">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18254" target="_blank">📅 20:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18253">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEmosCOwFDN6mu1KjGorrFCLxGexOm74qn0xzQEufzOZAjhdaqjAOnR4Yd-j8VPpIrih6Us47hxEW-lb-q7l8vc49fanFuKBk2Wcw9dxqEmEgE6xtp1Fy2-GgeYue_1k6o8RPuE5jjJnQS6Wg8yU_2cvYIamatmRwIdiEOaQus3jpdBcpicG-Q8L7c3T6IkPXHXZuDc_13HsrcQwiK2IUEnD_LsEwpzcMYAxY1F-cr7fjkLoIKgTvqmsyehNaBVFX9fsNR7Jg80YWm_6_-5x7aOrKOT-ifTEH6zunnBOB9fV5Lpl5UUQ-vFYa3jsDx0EbjNN18OD5lpE8O-Ih_bGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما در کل این سیاره خاکی بگردید هر جا کمبود برق و انرژی باشد احتمالاً یا کمونیست هستند یا دوست دارند شبیه کمونیست ها باشند و با شکم گرسنه و خشتکی پاره مرگ بر آمریکا و مرگ بر سرمایه داری سر بدهند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18253" target="_blank">📅 20:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18252">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شبکه ملی برق کوبا روز دوشنبه دچار قطعی شد و حدود 10 میلیون نفر را بدون برق گذاشت.  مقامات اعلام کردند که علت این قطعی همچنان در حال بررسی است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18252" target="_blank">📅 20:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18251">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گویا آمریکا می خواهد در این مدت آتش بس موقت با ایران، تکلیف کوبا را یکسره کند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18251" target="_blank">📅 20:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18250">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نشست ناتو و 3 پویه اقتصاد دفاعی روز  افزایش هزینه‌های دفاعی در کشورهای عضو ناتو در حال تبدیل شدن به یک روند ساختاری و نه صرفاً واکنشی به تنش‌های مقطعی است. هرچند در ظاهر، این افزایش می‌تواند به‌عنوان یک محرک کوتاه‌مدت برای رشد اقتصادی تعبیر شود، اما واقعیت…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18250" target="_blank">📅 19:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18249">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ در مورد جنگ اوکراین:
به نظرم ما بسیار نزدیک‌تر از آنچه مردم تصور می‌کنند (به آتش بس) نزدیک هستیم.
پوتین می‌خواهد که این جنگ پایان یابد. من این را به شما به شدت می‌گویم. ما یک تماس خوب داشتیم.
زلنسکی در واقع می‌خواهد که این جنگ همین حالا پایان یابد.
ما می‌خواهیم به ناتو برویم و می‌خواهیم در مورد آن صحبت کنیم. و من فکر می‌کنیم که می‌خواهیم آن را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18249" target="_blank">📅 18:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18247">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
بمب خبری ... اولین حضور رهبر معظم انقلاب آقای مجتبی خامنه‌ای در تشییع و نماز برای پدرشان در مصلای تهران  https://t.me/+SV6YYFA0zX1kOGZk</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18247" target="_blank">📅 15:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18246">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan Movahedian Channel</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a018aa532.mp4?token=UZwqlZAILg2a9ECFsvySPVXHLBzuBo7x1_eAKj6mnon2IenGS5dJzllcK3ihH-E31z-kJLsX8BwwxRc17lhsIYhV0R9LNkEAFi7TOAKkdUkn6mRSkmLlSTP9_S_GlWQg23F7fWrULz2XtA1qT_xyN5IuvI6YZumw05t9MXx4HSRrEPsrJRDxnRndKIcYN3fdBb8h5VJVZNV_rsfgoRSP3SNuMzAXRK_JxDd-8WpS9mpMI-n6cnrZBHE5Har7IiIUyQCEQH0gpaZSoMwwHHTURbPgi80iWzYukVSIM2DfCd6zbiRNu1bwUKQCBWa1lZ__-15XQ2gm3h1ImGLF4y9Wyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a018aa532.mp4?token=UZwqlZAILg2a9ECFsvySPVXHLBzuBo7x1_eAKj6mnon2IenGS5dJzllcK3ihH-E31z-kJLsX8BwwxRc17lhsIYhV0R9LNkEAFi7TOAKkdUkn6mRSkmLlSTP9_S_GlWQg23F7fWrULz2XtA1qT_xyN5IuvI6YZumw05t9MXx4HSRrEPsrJRDxnRndKIcYN3fdBb8h5VJVZNV_rsfgoRSP3SNuMzAXRK_JxDd-8WpS9mpMI-n6cnrZBHE5Har7IiIUyQCEQH0gpaZSoMwwHHTURbPgi80iWzYukVSIM2DfCd6zbiRNu1bwUKQCBWa1lZ__-15XQ2gm3h1ImGLF4y9Wyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بمب خبری ...
اولین حضور رهبر معظم انقلاب آقای مجتبی خامنه‌ای در تشییع و نماز برای پدرشان در مصلای تهران
https://t.me/+SV6YYFA0zX1kOGZk</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18246" target="_blank">📅 15:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18245">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ونس: ظرفیت تهاجمی روسیه نزدیک به صفر رسیده است   در مصاحبه‌ای با تایمز بریتانیا، جی‌دی ونس، معاون رئیس‌جمهور ایالات متحده، وضعیت نظامی روسیه را ناپایدار ارزیابی کرد.   ارزیابی او: توانایی روسیه برای عملیات‌های تهاجمی بیشتر «ناچیز و تقریباً صفر» است. این می‌تواند…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18245" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 2  دوشنبه 6 جولای 2026</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18244" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBjoILfOpezlA9dQdRhM8ul1n1o1a66Jxlxf3Xf3HkgkWijH0QPtf4xDM1fIxX6dgK19y7nEjaxPqozJpFOrnzBNyuUQfdRhi8yJwZRZrlLUlvi-ahvhtDyAPRZoyvUfyGtwaTYk44sHuWQ53zonaiCgWHls6UogeewUyQVuNXbdB2m0zfZmFrf5LxWXKWFS9k_UcG-EmBeC5QYVmvpIZn9C70jn7fKaUarcF1SLJZqZFEjn8TXvNieEgzqlHrzRA6W44a4WIxK3SNxZdr_X4OyNgVXenp8IVVP8xXcCnH-3RHRw8tbTxra6GRHMdAYbjv_FXhXCGkSHM9v3r15iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.  به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18243" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18242" target="_blank">📅 12:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نشست ناتو و 3 پویه اقتصاد دفاعی روز
افزایش هزینه‌های دفاعی در کشورهای عضو ناتو در حال تبدیل شدن به یک روند ساختاری و نه صرفاً واکنشی به تنش‌های مقطعی است. هرچند در ظاهر، این افزایش می‌تواند به‌عنوان یک محرک کوتاه‌مدت برای رشد اقتصادی تعبیر شود، اما واقعیت اقتصادی پیچیده‌تر از این برداشت خطی است. هزینه‌های دفاعی معمولاً با تأخیر وارد چرخه تولید و تقاضا می‌شوند و اثر آن‌ها به‌صورت تدریجی در اقتصاد پخش می‌شود. تجربه‌های تاریخی، مانند بازسازی ذخایر تسلیحاتی آمریکا پس از جنگ خلیج فارس که چندین سال به طول انجامید، نشان می‌دهد که این نوع هزینه‌ها به‌جای ایجاد شوک‌های فوری، بیشتر اثرات میان‌مدت و بلندمدت دارند.
در سطح ساختاری، ماهیت خریدهای نظامی نیز در حال تغییر است. جنگ اوکراین و استفاده گسترده از پهپادها در عملیات علیه روسیه و کریمه، نشان داده که فناوری‌های کم‌هزینه‌تر و غیرمتقارن در حال بازتعریف اولویت‌های نظامی هستند. این تحول به‌طور مستقیم بر زنجیره تأمین دفاعی اثر می‌گذارد و تقاضا را از سامانه‌های سنگین سنتی به سمت فناوری‌های سبک‌تر، هوشمندتر و مبتنی بر داده سوق می‌دهد.
از منظر ژئو‌اقتصادی، یکی از روندهای مهم، بازتنظیم روابط تأمین‌کنندگان تسلیحات است. اروپا به‌تدریج در حال کاهش وابستگی به تجهیزات نظامی آمریکاست و به سمت توسعه ظرفیت‌های داخلی یا تنوع‌بخشی به شرکای خود حرکت می‌کند. این تغییر می‌تواند در بلندمدت ساختار صنعت دفاعی غرب را دگرگون کند.
در این میان، خاورمیانه نیز به‌عنوان یکی از بزرگ‌ترین واردکنندگان تسلیحات، نقش تعیین‌کننده‌ای در جهت‌دهی به جریان سرمایه و فناوری نظامی دارد. این که بودجه‌های دفاعی کشورهای منطقه به چه نوع فناوری و از چه کشورهایی تخصیص یابد، می‌تواند بر رقابت جهانی صنایع دفاعی اثر قابل توجهی بگذارد. در مجموع، آنچه امروز مشاهده می‌شود نه صرفاً افزایش هزینه، بلکه بازآرایی عمیق در معماری اقتصاد دفاعی جهانی است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18241" target="_blank">📅 11:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5YGfFpKvzWQdtlXw8wKZDYz7k1v9qtnCenoV1-3pg4587JqR-KBIj3LJPzXNGNqJDQkP9n-QucGV7GtWMr8YFuK-hM-BviZHpcxNRK0WCJPdd6GlBBKKkBt63D7D6LEruVab_PIINlPfRZDRAKRqsddZQ0tRaubdtdlYuMSP33_v_TBowRNAxyr1sLphq9KoNMcZxfrn3nA-3GPWy8kX2_-rGIUnpqDEGf76AwnaImpgTAWcBqc69JaZvtfK2i9-WxmlUD0tpwRcQPZBhpdXmtz1AB6GSfieWMoNB9DlCsbFwtjG_f9nhCzR2CxoVMtdENGqpLaZWFMerTRYjsoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتک برای امروز در سطح میانه پایین قرار دارد و ریسک پذیری بسیار ملایم پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18240" target="_blank">📅 11:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18239" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شبکه ۱۴ اسرائیل:
سپاه قدس واحد جدیدی به نام « یگان مختار » تشکیل داده است که با شهروندان مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18238" target="_blank">📅 10:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18237">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18237" target="_blank">📅 10:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18236">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g45tRmF9vRdlAkE8lmP91HVBSp_BPFq3ay2StKQ6ojwG_bjM9_GKBs9wwoSdWVrntLlac6zdTYYE0WTeIp-8N7UdBERQ46h9sNR_604Oij2QCkLcbki1In-NaHVH4tSc9NxJJjXgQFUMrDQRMh0Td67AjEbroWCf6Ka6j6ydVB2g0DJcebKg1m9wInj96qBfoaZjlv-bNEqSXWHQ4w1LT1Sa2gDnw2WKV7SuM7tLYYqv4QPz095vk_DAhj33qxeqqjH7aeZfk-bHcGIjboI9hpJ92s6VHTQ7gwh2nQQB9CVT-SDL-F7gyUrIONHgP4wBvRLJ4i-CYomGTAEK1bYU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گویا واقعاً زنگ زده اینفانتینیو و گفته یا بازیکن اخراجی ما را می بخشید یا بازی خراب!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18236" target="_blank">📅 09:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18235">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18235" target="_blank">📅 22:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18234">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2cWXyhfgGiHGq8ORVgRd8fWA-bjc2X-7ntcscUQ-uhYx_pc5dgUpSKwJs5qKurfXKT30-0Gh2gPMs1e9wY2yNNje13qigI4lMz45D950jASDK2M4kZia6WSufuMFSGLMrsaqSAdqeb30f8ne0zTH5-RNnnM3NB-19C2FWthkzjlocUlW1EXPqbo4fR7EL94adE9-4PIczQ_lyVdvn1KqktKDNOYGtF0bWLeJtByGqkpQ5GO4hWMei7Eg8otFSGAB3rqYp2epFOG-deWnPJHeuq5LkeOPmw2Lyu-nMZDK2uJc-tT8vLQE2O-nrryIwteGBk-2AMQ-PrF4HwJ_-5PPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
استقرار بالن نظارتی (الکترواپتیکی)  در آسمان تهران</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18234" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18233">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو:
«برخی روستاهای مسیحی‌نشین لبنان در واقع درخواست الحاق به اسرائیل را داده‌اند، زیرا ما از آنها در برابر حزب‌الله محافظت می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18233" target="_blank">📅 21:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18232">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ایران می‌گوید از آتش‌بس با ایالات متحده برای تقویت آمادگی رزمی خود استفاده می‌کند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18232" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18231">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دو نکته:  — از این میان ما سومی (J-20) را داریم. (البته ماکت ش)  — آخری (جنگنده کان یا خان ترکیه) فقط یک مشکل کوچک دارد و آن اینکه موتورش هنوز پیدا نشده که انشالله این هم حل می شود.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18231" target="_blank">📅 17:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18230">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
چرا نتوانستیم از صدام حسین غرامت بگیریم؟  حمزه رحیم صفوی.  @MonazeratChannel</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18230" target="_blank">📅 16:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18229">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمناظره‌ها</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f11f469c.mp4?token=vjSL4YhrKSn18v6YK_38_vwiVMnF4MMB6YErl-sLT3cJVCOszO-IOAVSUYU3MYk9IVbful2nvsA3BBU7MWfmN5HoQI4clf_rRRkbkSvN9Hl2ow4Ywreoi2ZfdmhVWvfYWdtTZWLk3JPVRsn4Vi4mNz4aXuaMUaY00RTCvkZDelEnbF7mXiPRJLCuLQLnQ16mhU88n3LZeSuA7gEZ2Do7wHLFpQLJykq7rPhwLM2Yzven1dj8nw4GgrSlvC-4rNP3WeRzTMJwWr7HhRr3KWchqaPCgT-YszYWSc75VL7eQ4hXLM5oD09f0k05_dZc5zcGkwRZXIHTH-WsIPogTaxvGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f11f469c.mp4?token=vjSL4YhrKSn18v6YK_38_vwiVMnF4MMB6YErl-sLT3cJVCOszO-IOAVSUYU3MYk9IVbful2nvsA3BBU7MWfmN5HoQI4clf_rRRkbkSvN9Hl2ow4Ywreoi2ZfdmhVWvfYWdtTZWLk3JPVRsn4Vi4mNz4aXuaMUaY00RTCvkZDelEnbF7mXiPRJLCuLQLnQ16mhU88n3LZeSuA7gEZ2Do7wHLFpQLJykq7rPhwLM2Yzven1dj8nw4GgrSlvC-4rNP3WeRzTMJwWr7HhRr3KWchqaPCgT-YszYWSc75VL7eQ4hXLM5oD09f0k05_dZc5zcGkwRZXIHTH-WsIPogTaxvGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چرا نتوانستیم از صدام حسین غرامت بگیریم؟  حمزه رحیم صفوی.
@MonazeratChannel</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18229" target="_blank">📅 16:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18228">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18228" target="_blank">📅 15:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18227">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مسؤولان آمریکایی نگران بودند که اسرائیل ممکن است در طول مذاکرات صلح حساس در بهار امسال، از جمله وزیر امور خارجه عباس عراقچی و رئیس مجلس محمدباقر قالیباف، رهبران مذاکره‌کننده ایران را ترور کند.  با نگرانی از اینکه چنین حمله‌ای مذاکرات را متوقف کرده و جنگ را…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18227" target="_blank">📅 15:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18226">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📌
وخیم تر شدن وضعیت صنعت آلمان در اثر جنگ خاورمیانه  صنعت آلمان که پیش‌تر هم تحت فشار بود، با آغاز جنگ خاورمیانه، افت تولید صنعتی، کاهش رشد صادرات و افت محسوس مازاد تجاری در مارس، وارد وضعیت ضعیف‌تری شده و احتمال بازبینی نزولی رشد اقتصادی سه‌ماهه اول را بالا…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18226" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قالیباف، در مراسم تشییع رهبر سابق ایران:  «ثمره خون خامنه‌ای آزادی بیت المقدس خواهد بود».</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18225" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18224" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18223">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کلا خاطره خوبی از محاسبه خسارات و جمع آوری شواهد نداریم.
بار پیش
هم که جناب عراقچی داشتند خسارات اشتباه محاسباتی اسراییل در جنگ ۱۲-روزه را محاسبه می‌کردند که اشتباه محاسباتی بعدی روی داد و اصلا محاسبات ما به هم ریخت.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18223" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18222">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18222" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18221">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:
"ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18221" target="_blank">📅 12:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18220">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Trump Accounts
سرمایه‌گذاری بر نسل آینده یا
پروژه‌ای سیاسی؟
دولت دونالد ترامپ با معرفی طرح «Trump Accounts» تلاش کرده است ایده‌ای را به اجرا بگذارد که در ظاهر، حمایت از آینده مالی کودکان آمریکایی را هدف قرار داده است. بر اساس این برنامه، برای هر کودک واجد شرایط، حسابی سرمایه‌گذاری ایجاد می‌شود و دولت برای نوزادان متولدشده در بازه زمانی تعیین‌شده، مبلغ اولیه‌ای را به این حساب واریز می‌کند. دارایی این حساب‌ها نیز در صندوق‌های شاخص کم‌هزینه سرمایه‌گذاری می‌شود تا در بلندمدت از رشد بازار سهام بهره‌مند شود.
طرفداران این طرح معتقدند که ایجاد سرمایه از ابتدای زندگی می‌تواند فرهنگ پس‌انداز و سرمایه‌گذاری را در جامعه آمریکا تقویت کند. از نگاه آنان، حتی یک سرمایه اولیه نسبتاً کوچک نیز در صورت رشد مستمر بازار، می‌تواند هنگام ورود فرد به بزرگسالی به منبعی برای تأمین هزینه تحصیل، خرید نخستین مسکن یا آغاز یک کسب‌وکار تبدیل شود. این رویکرد همچنین می‌تواند وابستگی شهروندان به کمک‌های مستقیم دولت را کاهش داده و مشارکت آنان در اقتصاد و بازار سرمایه را افزایش دهد.
در مقابل، منتقدان بر این باورند که اثر واقعی این برنامه به توانایی خانواده‌ها برای واریز مبالغ بیشتر به حساب فرزندانشان بستگی دارد. از این منظر، خانواده‌های پردرآمد بیش از دیگران از مزایای رشد سرمایه برخوردار خواهند شد و در نتیجه، شکاف ثروت میان طبقات مختلف جامعه ممکن است کاهش نیابد و حتی در بلندمدت افزایش پیدا کند. همچنین برخی ناظران، انتخاب نام «Trump Accounts» را اقدامی با رنگ‌وبوی سیاسی می‌دانند که می‌تواند این برنامه را به بخشی از میراث سیاسی رئیس‌جمهور تبدیل کند.
در مجموع، موفقیت یا شکست «Trump Accounts» به عملکرد بازارهای مالی، میزان مشارکت خانواده‌ها و نحوه اجرای مقررات آن وابسته خواهد بود. اگرچه این طرح می‌تواند گامی در جهت گسترش سرمایه‌گذاری عمومی باشد، اما قضاوت نهایی درباره آثار اقتصادی و اجتماعی آن تنها پس از گذشت چند سال و مشاهده نتایج عملی امکان‌پذیر خواهد بود.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18220" target="_blank">📅 11:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18219">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون:
فرانسه دارایی‌های ضد مین را به خاورمیانه اعزام کرده است، از جمله به‌ویژه دو کشتی  ویژه جستجوگر مین
همراه با دو ناوچه و یک هواپیمای گشت دریایی، این دارایی‌ها آماده هستند تا در کنار شرکای ما، به از سرگیری کامل کشتیرانی و تضمین ایمنی ترافیک در تنگه هرمز کمک کنند</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18219" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
پناهیان ؛ مشاوره ریاست نهاد نمایندگی رهبر در دانشگاه‌ها :
حاضریم تمامی منافع ملی را فدای خونخواهی رهبر شهیدمان کنیم</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/18218" target="_blank">📅 23:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18217">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
بابک زنجانی
:
به زودی خونخواهی رهبر شهید شروع خواهد شد و آن خون خواهی اقتصادی است</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/18217" target="_blank">📅 23:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18216">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ایران قصد دارد به چین تعرفه‌های ترجیحی برای تنگه هرمز ارائه دهد
تهران قصد دارد به چین و سایر کشورهای دوستانه تعرفه‌های ترجیحی برای هزینه‌های عبور و مرور ورودی تنگه هرمز اعطا کند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18216" target="_blank">📅 22:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18215">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به گزارش کانال 15 اسرائیل، دونالد ترامپ از اسرائیل خواسته است که فعالیت‌های نظامی خود را در لبنان افزایش ندهد، زیرا نمی‌خواهد این امر در مذاکرات جاری او با ایران دخالت کند.
به همین دلیل،  نتانیاهو یک عملیات نظامی که پیش از این برای منطقه علی‌الطاهر برنامه‌ریزی شده بود، را به تعویق انداخته است.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18215" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18214">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رئیس‌جمهور عراق:   عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18214" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18213">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18213" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18212">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، گفت که آمریکا می‌توانست رهبران ایران را که برای مراسم تشییع آیت‌الله علی خامنه‌ای، رهبر پیشین، جمع شده بودند، هدف قرار دهد، اما این کار را انجام نمی‌دهد زیرا می‌خواهد مذاکرات هسته‌ای را حفظ کند.  «همه آن‌ها آنجا هستند. با یک…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18212" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18211">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، گفت که آمریکا می‌توانست رهبران ایران را که برای مراسم تشییع آیت‌الله علی خامنه‌ای، رهبر پیشین، جمع شده بودند، هدف قرار دهد، اما این کار را انجام نمی‌دهد زیرا می‌خواهد مذاکرات هسته‌ای را حفظ کند.
«همه آن‌ها آنجا هستند. با یک شلیک [می‌توانیم همه آن‌ها را از بین ببریم]، اما این کار را نخواهیم کرد زیرا در آن صورت کسی برای مذاکره باقی نخواهد ماند»</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18211" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18210">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اردوغان به اسرائیل هشدار داد: "نباید اجازه داد اسرائیل منطقه را در خون غرق کند."
رئیس‌جمهور ترکیه، اردوغان، در سخنانی مشترک با نخست‌وزیر پاکستان، لحن تندی علیه اسرائیل اتخاذ کرد.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18210" target="_blank">📅 20:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18209">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18209" target="_blank">📅 18:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18208">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترکیه با موفقیت موشک بالستیک TAYFUN Block-3 را علیه هدف کشتی متحرک با سرعت هایپرسونیک آزمایش کرد.
شرکت ROKETSAN یک آزمایش آتش‌زنده از موشک بالستیک TAYFUN Block-3 انجام داد و با موفقیت یک کشتی سطحی بدون سرنشین آزاد در حرکت را در دریا با یک سر جنگی زنده با سرعت هایپرسونیک هدف قرار داد.
هدف حدوداً ۷ متری — که یک قایق ماهیگیری کوچک بود — با آنچه شرکت آن را «دقت جراحی‌گونه» توصیف کرد، نابود شد.
این آزمایش نخستین مورد از این دست است که در آن یک موشک بالستیک که با استفاده از سر جستجوگر برای هدایت در مرحله پایانی، یک کشتی سطحی متحرک را در دریا درگیر و هدف قرار می‌دهد.
ترکیه می‌گوید این نخستین یکپارچه‌سازی چنین سر جستجوگری بر روی یک موشک بالستیک در داخل کشور است و یکی از تنها چند نمونه در سراسر جهان — قابلیتی که به طور موثر یک موشک بالستیک را به یک سلاح ضد کشتی تبدیل می‌کند.
سرعت پایانی هایپرسونیک TAYFUN آن را تا حد زیادی در برابر پدافند‌های متعارف دفاع هوایی مصون می‌سازد.
نسخه Block-3 پیشرفته‌ترین نسخه از برنامه موشک بالستیک توسعه‌یافته داخلی ترکیه را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18208" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18207">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک کارشناس:
به نظر می‌رسد که ایران در مراسم تشییع جنازه رهبر خود هر هیئت خارجی را با یک آیه قرآن مرتبط کرده است که هدف سیاسی خاصی را دنبال می‌کند.
عربستان سعودی: آیه ای درباره دو ارتش که در جنگ با یکدیگر روبرو می‌شوند، یکی مومن و دیگری غیرمومن.
ترکیه: آیه ای که کسانی را که در راه خدا می‌جنگند، بر کسانی که "نشسته"اند، برتری می‌بخشد.
دولت لبنان: آیه ای درباره افرادی که در صورت درخواست، از انجام فداکاری خودداری می‌کنند.
حزب الله: به آنها گفته شد "ضعیف نشوید یا غمگین نشوید، شما برتر هستید."
حماس: آیه ای که مردانی را که عهد خود را با خدا وفا کردند، مورد تقدیر قرار می‌دهد، "برخی از دنیا رفته‌اند، و برخی دیگر در انتظارند."
حوثی‌های یمن: آیه ای که به مومنانی که بدون سستی جنگیدند، ستایش می‌کند.
قطر: آیه ای درباره بخشش و لطف الهی، که به عنوان اشاره‌ای به نقش میانجی‌گری این کشور خوانده شد.</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/18207" target="_blank">📅 13:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18206">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اظهارات مدودف، نخست‌وزیر روسیه:  ایران به جای سلاح‌های هسته‌ای، سلاح دیگری را کشف کرده است که از نظر قدرت، نه ضعیف‌تر از سلاح‌های هسته‌ای است و آن، تنگه هرمز است.  بحث‌ها حول این موضوع است که چگونه باید به توافقی دست یافت تا این تنگه در آینده به چه صورت عمل…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18206" target="_blank">📅 13:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18205">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جناب الکساندر سرگین هستند از گه خورهای اعظم که بیرون گود نشسته و به ما میگویند لنگش کن!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18205" target="_blank">📅 13:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18204">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngjHlZPoqO49Nj8-PqAgIArn7UTow2DKPO1avzZgYWL4msjs2k3ISRt_vwsCvKBZ3i3X4hqUlsMoDepnF_GviZsF4Js6tQWexrMydlXkKnufHGMxg0Sv1KC0kDQ9aJ9KPfEIWTj4TiLX8Eqm0TOcIRazN3hgE3zbto-wC2PorrxzI9DdTtx5t_t_DmVZ-HwcvN8_8PdYbY1CHr0ctreOpBxIfQA-mhuxzR-o7DV6WYximcMhquSaoPulwsIItqxkU1Gmate7KUrMFqx7nL1Zs43rveAxl_7cVN7JGA6Bf42L_CVedB6z2RM05cEaxPquTbjvSPiLhIbSvJJWmPFkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس ترنس هست اما نجس هم هست؟!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18204" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18203">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رسانه‌های غربی:
عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند و از آنجا که ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد.
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/18203" target="_blank">📅 10:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18202">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امروز پوتین با لباس نظامی با رسانه ها گفتگو کرده و عملاً می خواهد از اعتبار و جایگاه خود دفاع کند.  حس خوبی ندارم....</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18202" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18201">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ
:
ما مناقشه با ونزوئلا را در یک روز حل و فصل کردیم و ضربات بسیار سختی به ایران وارد کردیم.
طرف ایرانی بسیار مشتاق است و به هر طریقی به دنبال دستیابی به یک توافق سیاسی با ما است.
ما از روی حسن نیت به ایران یک هفته فرصت دادیم تا عملیات را متوقف کند تا مراسم تشییع جنازه برگزار شود.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18201" target="_blank">📅 09:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18200">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIQu2wnt9akZ3-ebwKTHR5LmyE9B-92WjnSvKSiksXwkGN-ZAXs9xZ7_Xf7o8kdSCj97_d_L09k2Ior9dEia0j_ahf2e-bDv1IIp3xJgMXiqQ_lG1t6WX7Yl11lFcRgKiqNN8JEGmdvPX1v1UjAnAONz0xT6wjwWsQSKgLeTcvhEaVV4iAAZkpJgyQ3RbAsF-SNsg0kcwtJnD7lm-Vy1_U0FhbJmCa1ZtxU8q2uLovIgoUCQRzj5Q9TuwhgX8ra2ekxFugrUrYgDm_H3jttmXg-xhtdNs0ONfS4dy05tCh_rAL4vQG550RXmqm56gcFzDbxe3Rwd-xubgcJEkhpw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر جنگ هسته ای؟!
ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. د
ر ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی»
عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که نزدیک‌ترین فاصله به نقطه نمادین فاجعه جهانی در تاریخ است. این سازمان، تضعیف امنیت بین‌المللی، ضعف چارچوب‌های کنترل تسلیحات و رفتارهای فزاینده پرخاشگرانه قدرت‌های بزرگ را به عنوان دلایل اصلی این تصمیم ذکر کرد.
یکی از واضح‌ترین نشانه‌های این تضعیف، افزایش بکارگیری اصطلاحات هسته‌ای در گفتمان سیاسی و پوشش رسانه‌ای است. عباراتی مانند «حمله هسته‌ای»، «ضربه هسته‌ای»، «تهدید اتمی» و «تشدید هسته‌ای» بسیار بیشتر از چند سال پیش به کار می‌روند. در حالی که عبارت «حمله اتمی» بیشتر با اوایل جنگ سرد مرتبط است، گزارش‌های مدرن ترجیح می‌دهند از اصطلاحاتی مانند «حمله هسته‌ای» و «تهدید هسته‌ای» استفاده کنند. این تغییر نه تنها نشان‌دهنده تغییر زبان، بلکه نگرانی مجددی است که سلاح‌های هسته‌ای دوباره در محاسبات استراتژیک نقش مرکزی پیدا کرده‌اند.
جنگ در اوکراین نقش عمده‌ای در این روند داشته است. از آغاز این درگیری، مقامات روسی بارها امکان استفاده از سلاح‌های هسته‌ای را مطرح کرده‌اند، در حالی که دولت‌های غربی و تحلیلگران درباره اعتبار این تهدیدات بحث کرده‌اند. بولتن به طور خاص اشاره کرده است که جنگ روسیه و اوکراین با تحولات نظامی بی‌ثبات‌کننده و ارجاعات مکرر روسیه به سلاح‌های هسته‌ای همراه بوده است، که خطر محاسبه نادرست بین کشورهای دارای سلاح هسته‌ای را افزایش داده است. شکست‌های نظامی اخیر و فشارهای اقتصادی رو به رشد، بحث‌ها درباره گزینه‌های استراتژیک روسیه را تشدید کرده‌اند. گزارش‌ها و تحلیل‌ها بر فشارهایی که یک درگیری طولانی‌مدت بر تولید صنعتی، تحریم‌ها و زیرساخت‌های انرژی تحمیل کرده است، تأکید داشته‌اند. این فشارها باعث شده است که برخی تحلیلگران گمانه‌زنی کنند که مسکو ممکن است برای بازدارندگی از مداخله بیشتر غرب، بیشتر به سیگنال‌های هسته‌ای متکی شود. با این حال، فعلاً و در شرایط کنونی گمانه‌زنی درباره تصمیمات آینده روسیه نباید با شواهدی مبنی بر استفاده قریب‌الوقوع از سلاح‌های هسته‌ای اشتباه گرفته شود. کارشناسان نظامی و سیاسی عموماً چنین گفتمانی را بیشتر ابزاری برای اجبار و بازدارندگی می‌دانند تا نشانه‌ای قابل اعتماد از استفاده نزدیک از سلاح‌های هسته‌ای. با این حال کمبود گسترده بنزین و گازوئیل یا صف‌های طولانی سوخت در سراسر روسیه  بشدت روی روحیه و غرور ملی روسها تاثیر منفی گذاشته اند و برای نخستین بار از سال 2006 به این سو، مردم روسیه تصور می کنند استانداردهای کیفیت زندگی شان رو به نزول نهاده است. این مسئله روی پوتین و هیات حاکمه روسیه فشار می آورد تا دست به اقدامات تهاجمی تری برای تسلیم کردن اوکراین و ناتو بزنند که یکی از آنها می تواند بهره گیری از سلاحهای کشتار جمعی باشد.
از سوی دیگر، ناکامی نسبی آمریکا در دستیابی به همه اهداف نظامی اش در ایران نیز می تواند از دیگر حوزه هایی باشد که نهایتاً ترامپ را به استفاده از سلاح های هسته ای وادار کند. در این حوزه می توان به اشاره ترامپ به راهبرد «شرمن» استناد کرد که استعاره ای از یک استراتژی ویرانگر مخرب با تلفات بالا برای به تسلیم کشاندن دشمن می باشد. (
لینک
)</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18200" target="_blank">📅 02:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18199">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyP2bypP64cO8_sFd20SEtzb864d-GCmOj4Sb_ufh_m2ARmP9cvE8H-fmUH_SvJumd6xBV_0sQ2SQvxp_lDRE9IXaemH9Yf0u2VSSMXuXvBPRHMnh8QkkoASrlonrqqsLL0CFcLR3Y4dPFSnA2D0bNJa1GsKs-Y07V8QBLAi2tNOgCnf8gpuRWHfg2Fi9Sr6SmPGls28UzpJsktFs-uSXZZEFSPAEbA4W30WCIMzwNqK3kZm0GLCb4EBNXaeU705sE1BYaoRQ3SXKdFPM-llt3DACwpvXiN7mUZqQqqAWgPeS-EyIA79kKrdej7B4ufH3L-GN94MEHjmvhkhHMUz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در اینجا گفته شد که پوتین مانند گربه ای در گوشه اتاقی بسته گیر افتاده و این خطرناک است</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18199" target="_blank">📅 01:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18198">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/up5wBHQHGFKm50fqdOgedFoVeIilJIfyKnZRl1ZkaSBr6mERj30eklYgAvfPFWrCt8no_fKoAIpBYl10Un1ZqqFW_tXMfm-YUEW3lh9MFbgp6dB0SxearTzxdHGlGtSkz-tMQvs6p9KY1oMinhroDdAaUXC0EAXIRSJQkJ6t1e4MJFaGFmU_gMNNC5q4a0BpCSh9I8Tdeljfkvf0aGZ5flZUR3YlcemQ-aE4xZCwPD7-XdiqKsDpDLfCqNBNz8yVAYRjrjmISzdJ5c0eDT5xoDqoWBcOoJl4A9m82xypYJ4dwrvEt6eyWKbeDYtp73Uz5IGxIV8Osy7sO4NLNtJ7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18198" target="_blank">📅 01:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18197">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دونالد ترامپ در آخرین افشای مالی سالانه خود گزارش داد که در سال ۲۰۲۵ حداقل ۱.۴ میلیارد دلار از کسب‌وکارهای مربوط به ارزهای دیجیتال و میم‌کوین‌ها درآمد داشته است. ارزهای دیجیتال به‌وضوح بزرگ‌ترین منبع درآمد او بوده‌اند.   این گزارش همچنین نشان داد که او ۲۶…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18197" target="_blank">📅 22:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18196">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18196" target="_blank">📅 22:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18195">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18195" target="_blank">📅 22:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18194">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">امام جمعه کرج:   اورانیوم غنی‌شده را رها نمی‌کنیم وتنگه هرمز را رها رها نمیکنیم</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18194" target="_blank">📅 20:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18193">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امام جمعه کرج:
اورانیوم غنی‌شده را رها نمی‌کنیم وتنگه هرمز را رها رها نمیکنیم</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18193" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18192">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">موسسه رتبه‌بندی فیچ، ریسک‌های مرتبط با ایران برای بخش‌های شرکتی در سطح جهان را مجدداً ارزیابی کرد
از دید این موسسه، شکنندگی توافق موقت ۶۰ روزه، به همراه عدم مشارکت اسرائیل، نشان می‌دهد که درگیری خاورمیانه همچنان تهدیدی برای صادرکنندگان شرکتی محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18192" target="_blank">📅 20:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18191">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو و ترامپ توافق کردند که به زودی در ایالات متحده با یکدیگر دیدار کنند - رسانه‌های اسرائیلی.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18191" target="_blank">📅 20:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18190">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتانیاهو و ترامپ توافق کردند که به زودی در ایالات متحده با یکدیگر دیدار کنند - رسانه‌های اسرائیلی.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18190" target="_blank">📅 20:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18189">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPuVDawd9HdTbEGn4v033oAsaHrOlQPRpxz7wKGA8s8Sd9h-LhqfEu5U6awoEOjJxcW4nFnYxDw6pV9KFkRCJScAsT9jg36vfLrTXpDjQTrluBnR-l44CUTh167xlVTqczQz_KX9kYXDYdBTG44Yy8xcwYq24zwjeUYyP-rHnlbYiXb-ew7KSw5wi367qj__InclR_zVioxn-JHs4ICrnrXwIxWIpUFknEcOoYjuGmDxcpTCF5X6SI5_U3N4fYpwxFAhUZ9dGnQkehsDzvOJH3StRPJtDNHU727oIEDVGc-zeBPyC8j9yzs9V5C6z8qEZ0XJtghXAva6XXagY9yMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه اندازی ساختمان عظیم وزارت دفاع مصر!
افتتاح مجموعه «هشت‌ضلعی» (The Octagon) به‌عنوان مقر جدید وزارت دفاع و فرماندهی راهبردی مصر را می‌توان یکی از مهم‌ترین نمادهای تحول ساختاری نیروهای مسلح این کشور در دهه اخیر دانست. این مجموعه عظیم که در پایتخت اداری جدید مصر ساخته شده، قرار است تمامی ستادهای اصلی نیروهای مسلح را در یک مرکز واحد گرد هم آورد و با بهره‌گیری از سامانه‌های پیشرفته فرماندهی، کنترل، ارتباطات و مدیریت اطلاعات، سرعت و هماهنگی تصمیم‌گیری‌های نظامی را به شکل قابل توجهی افزایش دهد.
ساخت چنین مرکزی تنها یک پروژه عمرانی نیست، بلکه بخشی از راهبرد بلندمدت قاهره برای تبدیل ارتش مصر به نیرویی مدرن، شبکه‌محور و آماده مقابله با تهدیدات متنوع منطقه‌ای است. طی سال‌های گذشته، مصر سرمایه‌گذاری گسترده‌ای در نوسازی تجهیزات نظامی، توسعه صنایع دفاعی و خرید سامانه‌های پیشرفته از کشورهای مختلف انجام داده و اکنون ایجاد یک مرکز فرماندهی یکپارچه، حلقه تکمیل‌کننده این روند محسوب می‌شود.
از منظر ژئوپلیتیکی نیز افتتاح «هشت‌ضلعی» پیام مهمی برای بازیگران منطقه دارد. مصر در سال‌های اخیر تلاش کرده جایگاه خود را به‌عنوان یکی از قدرت‌های اصلی نظامی و امنیتی خاورمیانه و شمال آفریقا تثبیت کند. تمرکز فرماندهی نیروهای زمینی، دریایی، هوایی و پدافندی در یک مجموعه واحد، ضمن افزایش کارآمدی عملیاتی، توان مدیریت بحران‌های هم‌زمان در جبهه‌های مختلف را نیز تقویت می‌کند.
همزمان، انتقال وزارت دفاع از مرکز سنتی قاهره به پایتخت اداری جدید، نشان‌دهنده اهمیت این شهر در ساختار آینده حکومت مصر است. دولت مصر با انتقال تدریجی نهادهای حاکمیتی به این شهر، در پی ایجاد مرکز سیاسی، اداری و امنیتی جدیدی است که از زیرساخت‌های مدرن و استانداردهای بالای حفاظتی برخوردار باشد.
در مجموع، افتتاح «هشت‌ضلعی» را باید فراتر از افتتاح یک ساختمان نظامی ارزیابی کرد؛ این پروژه نماد ورود نیروهای مسلح مصر به مرحله‌ای جدید از سازماندهی، فرماندهی و آمادگی عملیاتی است و می‌تواند بر موازنه قدرت و معادلات امنیتی منطقه نیز تأثیرگذار باشد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18189" target="_blank">📅 20:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18188">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حوثی ها می‌گویند جنگنده‌های سعودی را از آسمان یمن بیرون کردند زیرا سعی در جلوگیری از فرود یک هواپیمای مسافربری ایرانی در صنعا داشتند.
آن‌ها هشدار دادند که اقدامات آینده سعودی با حملات به فرودگاه‌های سعودی و سایر اهداف حیاتی پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18188" target="_blank">📅 18:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18187">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">از زمانی که روس‌ها تلگرام را محدود کرده اند و ایلان ماسک هم استفاده دزدانه شان از استارلینک را محدود کرده، توان آفندی پهپادی ارتش ظفرنمون مسکووی بشدت کاهش یافته است.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18187" target="_blank">📅 16:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18186">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسرائیلی ها، تاسیس پایگاه نظامی از سوی ترکیه در عمق خاک سوریه را به عنوان تهدیدی برای خود ارزیابی می کنند!  حملات ویرانگر اسرائیل ضد پایگاه T-4 نیز در همین راستا ارزیابی می شود.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18186" target="_blank">📅 15:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18185">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYsHlSvMDViXlF0BC0j3827IXKzqDuKjmdX830NOB32BRDlUd55wTc8ZiBUWQt8HnzshUZ0xKP4PJ8i2WiOmkmCuVTh-00M89Ri6R32x9pHiSwbMtXnn4yRs78QTN6YCvlZR3qB853sBuUeNxL4rQ40fn9MA0pSFN3p-0xkAPylCtm1uAXY_EBy2ZJwJuSFsHg7HSFzvmAGZtWx8Em4NpasDANvMWfSxmaVexzH0yFFvsHNxN1v4CZXg7XCDQp0KcjAp9pZ_ngCinNX7lLvF9W6rLmNh7RJHX5npFRT54rrZA393CHkPZFEs2AQV67YKyQIo1xf8Md5IXTvZj3lbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18185" target="_blank">📅 13:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18184">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-poll">
<h4>📊 مدت زمان و محتوای پادکست مطلوب است:</h4>
<ul>
<li>✓ کوتاه تر — بازاری تر</li>
<li>✓ کوتاه تر — بدون تغییر محتوا</li>
<li>✓ بدون تغییر در مدت زمان — بازاری تر</li>
<li>✓ بدون تغییر در مدت زمان و محتوا</li>
</ul>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18184" target="_blank">📅 11:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18183">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 1
جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18183" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18182">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGQ5GwbKGyuz3FvGjUPwzLiWUEnE6BVVtYdo7D74LY8I9ntMy40wG08N0fL4b6BaWqucoDbO5h2aZL9l2JNHGn7E9qVzsR4mTdMHZ4FqQAjdY14G7iKRi-bHAhx_mtDISGzHjtQhPCc5k_ZvnByz7HbCSoUxMlLImFgDDVJ44_VWGUuL0bfL6mJjXFAjMJNRKWBjpM09GPc__zDLru3ObZaiZYgAkqcyJw9PF_2TKVwoAYlmhvasQS0GBbgehHH9RvMSBUmm8RjMMg_Cu_vuggsFGAkFdWwu4Zu56SIFm6YRa8rAfhQ6AHmdd3-himehiL2pJPhsl_XKQu5z8BmhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز نسبتاً پایین است و ریسک پذیری ملایم پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18182" target="_blank">📅 10:48 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
