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
<img src="https://cdn4.telesco.pe/file/lHjXCm15g_ZmsLKrDgTkaWYaGBNyXs7AkZgnlAReowFgaE8j5-_foP-Zb5nOI2M8kn4_jQT1y_AkoFHK9SSf2l64Sa7T3oa-4V6GjjKJjJ4VcWzteSxTYNwIPvHpJC7iDtf2d951up25tbnbxihuU4uMRS1w-Uhpx4GplZyCUnWuCqUeJ7tFHr21JtF4xh-hhkK6eTWSnJHhXrAJjO-L--4x_13_fsKz2-jRtqZfS6fQ_1DmF9fDEupHC229Ox7Qa3ZX_Z42Xvy_emzrjg-Ihgf3UbbJI9bDy-AmeqL0akYb9dV9hM3-CzNYlBhbSXqO5zTFlrIcNhMJt2NbZL5Rjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 00:32:11</div>
<hr>

<div class="tg-post" id="msg-65972">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک  @News_Hut</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/news_hut/65972" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65971">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/news_hut/65971" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65970">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=o4FQ1pMI9-jYmkkBniyqYi7oBdy3CTom-Dzv5OKi6YF_07CR2U8KczPiN7uGSuLJIvbzorZmbxbPrbnF058DiH0f0V5sL_gZZQOXVivvJ-A_0SsYjruGKBvwHfsWNbdbmbnGbkYor7j4HUkWl5VCjI2wv_RE_Et1IGzCZL1fVxRZ1_nIYeniXN7CR1HlKr72N2iEuPbLtg_m8odNHs4hSs0XrH2xCx9JMDzn2GTaL02a4y7rMu-SutG17DsU9LxH0txJLUafhsuRhIpaSZ4SBY4ch17Ltf4FVXrLChBiAYhMTkpadR2UadSFhWLBudoP7oz0aEhO_yhWsZqnVYmYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=o4FQ1pMI9-jYmkkBniyqYi7oBdy3CTom-Dzv5OKi6YF_07CR2U8KczPiN7uGSuLJIvbzorZmbxbPrbnF058DiH0f0V5sL_gZZQOXVivvJ-A_0SsYjruGKBvwHfsWNbdbmbnGbkYor7j4HUkWl5VCjI2wv_RE_Et1IGzCZL1fVxRZ1_nIYeniXN7CR1HlKr72N2iEuPbLtg_m8odNHs4hSs0XrH2xCx9JMDzn2GTaL02a4y7rMu-SutG17DsU9LxH0txJLUafhsuRhIpaSZ4SBY4ch17Ltf4FVXrLChBiAYhMTkpadR2UadSFhWLBudoP7oz0aEhO_yhWsZqnVYmYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدا سیما: هک تصویر انفجار اتمی در تلویزیون، سیگنال آمریکا بود
!
@News_Hut</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/news_hut/65970" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65969">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060800d75a.mp4?token=MPwswvn0dhBAkEIELp3SRecbcsXPd-uUHI5yGKCjzrYYhpYdONyikpB8paa-clDz3iYfM0pEzazrb-BDcXEzmD8k919lc2MYX4ZJk-1Dv0V3wuWm4pj4vnvxxpWaWiqGBj2I2g9H9cnCqXxrUGJM-VFFb3kq2nrkOftg1jaFYOGUAh7T7OoEz0abUfPmLn6tFbfFjXyI7KrLI9qorAueeGV95TFaDzzEUUJMjIaHxsKJZ2R1YmFT0XKqMgGyiRajm62RuDnfV5b0FGRH7NXynrfPNGwtvQPA5eFauDs9BY9pNm1Ev6N-JWif4ZU_i39jVq4OmgGRiDHHuD9UeUMu9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060800d75a.mp4?token=MPwswvn0dhBAkEIELp3SRecbcsXPd-uUHI5yGKCjzrYYhpYdONyikpB8paa-clDz3iYfM0pEzazrb-BDcXEzmD8k919lc2MYX4ZJk-1Dv0V3wuWm4pj4vnvxxpWaWiqGBj2I2g9H9cnCqXxrUGJM-VFFb3kq2nrkOftg1jaFYOGUAh7T7OoEz0abUfPmLn6tFbfFjXyI7KrLI9qorAueeGV95TFaDzzEUUJMjIaHxsKJZ2R1YmFT0XKqMgGyiRajm62RuDnfV5b0FGRH7NXynrfPNGwtvQPA5eFauDs9BY9pNm1Ev6N-JWif4ZU_i39jVq4OmgGRiDHHuD9UeUMu9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گفتگوی عراقچی هم اکنون شروع شد.  @News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/65969" target="_blank">📅 23:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65968">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود
دارایی‌های مسدود شده طبق یادداشت تفاهم اگر امضا شود، آزاد خواهد شد
هیچ‌یک از دارایی‌های ما نمی‌تواند مجددا مسدود بماند
برای جبران خسارت ایران طرح بازسازی در نظر گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/65968" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65967">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
عراقچی:
به زودی ایران و عمان بیانیه ای مشترک در رابطه با تنگه هرمز منتشر خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65967" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65966">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
عراقچی:
به طور قطع تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65966" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65965">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
عراقچی:
پایان جنگ در توافق همچنین به معنای خروج اسرائیل از مناطق اشغالی در جنوب لبنان است و ما این موضوع را صراحتاً به طرف مقابل اعلام کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65965" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65964">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmhRk2NC8w0HBaCKgdLjcWuyfGqYriB3tPF6FXi0uivKzx_1EVxIycVlmv8z4fZHQi4GktOAatiV8OkmaQrPnzlcuFg4nfLVQq3nE4-V6HNVRxRWUrU5uPvfey6nJg9sCojtxkoN-fZbQo3Iai58TMF10TaNpEge0DWXJr_55WCBVABYV8N_xqCvCUcmV5tpNAZ7MsoevIwWbTq6fwKf7O4S8AssDYUrccrlcBlP1OeJHpve7wz0rLHY18w-fkscBOjXiAwspL30XFp2QFYv3F4291X71wbV2v43VLXurAe4XNL-a0Xfv-B5iP6wg8rpnquGQ9ZkyOxxgGtfMyugGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
هر چه بکاری، همان را درو می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65964" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65963">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/65963" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65962">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما پیروز میدان هستیم؛ مقامات خارجی به من می‌گویند که ایران را این‌گونه نشناخته بودند و ایرانی‌ها شگفتی آفریدند و با قدرت بیشتری از جنگ بیرون آمدند
من می‌توانم اسم ببرم که کدام مقامات این حرف‌ها را زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65962" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65961">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
هیچ دوگانگی بین میدان و دیپلماسی وجود ندارد و هردو در یک‌راستا حرکت می‌کنند
به این ۲ رکن، رسانه و خیابان‌ هم این‌بار اضافه شد و ۴ رکن باهم در یک‌سو حرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65961" target="_blank">📅 22:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65960">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
همهٔ ما مدیون تک‌تک نیروهای مسلح هستیم.
همین‌طور ما مدیون مردمی هستیم که ما را تنها نگذاشتند و هرشب در خیابان‌ها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65960" target="_blank">📅 22:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65959">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
عراقچی:
دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65959" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65958">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
#فوری: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65958" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65957">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
خبرگزاری تسنیم وابسته به سپاه؛
حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است
«حسین الحاج حسن» نماینده فراکسیون حزب‌الله:
بر اساس آنچه از سوی مقامات ایرانی به روشنی به ما ابلاغ شده، لبنان نیز شامل آتش بس است.
بر اساس آنچه مقامات ایرانی به ما ابلاغ کرده اند، اسرائیل از خاک لبنان بر اساس این توافق عقب نشینی خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65957" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65956">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری @kavianivpn  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65956" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65955">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9YbW_w_xK9D19ZQEzwyPHp10TFfoRC6lefA9yimeBGGuYYje8V2mRVw0MfFXcLA23P1uxoXyymuX_vZcef39IbvHrEy7Ks9DOBmBmGJionTkGM8BioxKLRK9UDS1uh300r2s24NACLhf0sLqNQlC1Gexie5NcW-kK6dBs88ZRIXMfJoGYot3Rz-XKd6D_QbA43cFteF48PpGpl6WSpNePchxpe3KGDQbboQ2lu77iPyI104u3yzdvTx0jrIygXCMl52glDJzM0COt1NfrCaAmwdv3EpXUInpjJKMsqzYzf9YWbOj-Nfeu0PnIBS37fcvwPdUtWZIbMR1Fxtn6FFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری
@kavianivpn
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65955" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65954">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
کانال 12 اسرائیل :
توافق قطعی است و این به نتانیاهو اعلام شده.
ترامپ از ایران خواسته به صورت علنی درباره توافق شفاف سازی کنه و هشدار داده انجام ندادن این کار پیامد هایی رو به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/65954" target="_blank">📅 22:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65953">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
رویترز: امارات ۳ میلیارد دلار از دارایی های ایران را آزاد و به آنها تحویل داده، این اقدام تضمینی بوده در ازای اینکه دیگر به این کشور حمله نشود
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/65953" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65952">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu8yG4rUfCx3YntLOhRAuriJw0rk3t2jNg1lrEcuKk7A1NVpMUA9xY256ZL22-3nPRxwOso5CeHtHEuXZ68vmclhbwMWNZHPuowjTRNUVwG5SB105cvKr055z2rMuPwNtUQMJcVpb-VYUfquNQ6lYeXI8ExlmMZJV-T7trpWpMk4JjJ-bGVv9yshvqt8LLMngedI6llDD-64mNEn8ATWRKO6rCY8KgjEH7aE4tBlHlvVF1L0pIk8fGGg6FZJ7tAUEqncAQdMUcL-rm_BcR7UTqk6cV1id3oMsFvK0KXWiWRohiYWKDr6cmuxMsWrPhvPiJaUUE6BHEc_rTsVGXFlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوری
: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65952" target="_blank">📅 22:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65951">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmcFuz9GPyguD91iLSJ4l9vywYw3ANJ8rFLtYIsg-Vrqr32MAYE6mAzAvYFso7HcCDxFxUFFc_74kFnoxCJUSfgvVI_WytS7dC6O_Ir2ltZ2rBhuXROSbEaErTfKvLt6Kh3oXJ4aQOgusXt9xdB1ic5NUWNvX_RzeO9ibkuDpIRNQiYIL1c4t13z5gW8SqZ00WRdye6CVqMHmGKs5e6os6V-Hn9KteO2nAhTyZMQJXG3kDLeBXmLNFdVkRFGakagMS7L2U49JGtj1_qATkqNsJDIAIuKREdg-Fkzw0evnBaQHHogtNcBNTgl8muy7UF_3MWWfbKQOOr1eZJybg55fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا به شیرمردان سپاه اسلام و حضرت آیت‌الله العظمی سید شیرمردان حاج آقا مجتبی حسینی خامنه‌ای، خوب دارین کیر می‌کنید ترامپ زن کصه‌رو #hjAly‌</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65951" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65950">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHlwQxF_Vqsl0YtcxnHNAFcKxJqJFawv5PT_fnMEMp3LkL8wCzMboNBay97cb-6yBWMdyUbgEpiu5MkS9Nee3c5iqQkmcWiMYCbBIMqrS3BNn57rG_R7rxDXeJiPoJjA4VZy2RYw10kTg6OoB29Rd-BsUq_k8V7OsIB0k8cnAyHqsjF2lbU5i-n4w92_-qcZJg6i2Swb__SIp3X2H8gt-6sHLFEGJZ7saapwTsSdprPzizuP4Yqvmp5dak1NW7-jg4PeZlwGmU3EA6Esgx2kxM9dS-sbHWiivBqGglpyLSPxTXcWC-BJEnQDO9p3ZBqKFvAgQAbjL4FF3gacP0e_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است.
نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65950" target="_blank">📅 21:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65949">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
الحدث:
وزیر خارجه پاکستان امشب عازم ژنو میشود
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65949" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65948">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز هفتگی پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65948" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65946">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwt5oNeFK9uD--4YpgpZ546iXIsxFdFDZqC3TKcPwvU8yiLv3yCf8Tx0SPsPfOfZaNZ6L9LIRMNoaczXxWyp2PXi_f5xwgm1xe4L5OI-Aczlgi98OmU4ohF1LtQqr1S4DNhGZjU3AKJkuctVPOQUlKumOwmnUD0uHwv2wpEi6Fjt0tlp61jXv72doEPJfB9V7_Wh_-C03hTkl3oROWH9j8G7kyW9qny3uDtM6_FoJtLUn4I31qhJwhhQO9Lzvh_IzblZwJ7dLr8JvmK4N1djS0dzb6CrK49R1h0ZBtfrJFDKEsn3_CmtIYqWh2eLZqNZJmKU65YX4hEW3XEyr6qUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز
هفتگی
پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
نفر چهارم تا هشتم ۲ میلیون میلیون
📈
۵ نفر از اعضا به قید قرعه ۲ میلیون
🏆
فقط پیش‌بینی کن و برنده شو
👇
➡️
@PishWin_Bot
➡️
@PishWin_Bot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65946" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65945">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=OwWmCLLc4AgM7UpmtIunX8bROhMS8u68ZXnP-wD6VU6VndeNthNN5eMy1j6P5kTFRNWuBwhuv1HTGc_3gnSnzuwwACuqvCp8RR020P2tAn4maq4cq98vyVxisKstZd5xKyf_0fVvWWwdZhiv5VmE5BbU6kyBRYAOb2MvJTZsnWW8vkcxJxpZ8tgIK60E5gEBRfn82slejpnS21DeF4wTubNIdDS033jsQ_lb3TVthSjSPouH7p-IWGkr3AjSw3b8DQmTE6bmPvy1Eb2jw1G-WUoSxH4QSE4GwKM3ABNYE9Xx5HJEGhs-R7VZJvlufT4xfAzfjolCj7PRcqbSs0-Iag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=OwWmCLLc4AgM7UpmtIunX8bROhMS8u68ZXnP-wD6VU6VndeNthNN5eMy1j6P5kTFRNWuBwhuv1HTGc_3gnSnzuwwACuqvCp8RR020P2tAn4maq4cq98vyVxisKstZd5xKyf_0fVvWWwdZhiv5VmE5BbU6kyBRYAOb2MvJTZsnWW8vkcxJxpZ8tgIK60E5gEBRfn82slejpnS21DeF4wTubNIdDS033jsQ_lb3TVthSjSPouH7p-IWGkr3AjSw3b8DQmTE6bmPvy1Eb2jw1G-WUoSxH4QSE4GwKM3ABNYE9Xx5HJEGhs-R7VZJvlufT4xfAzfjolCj7PRcqbSs0-Iag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهباز شریف:   در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65945" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVHpBXo4DLuq-qNomU3VvbYdzSRb1tZhkxwh_MJHwRlvTsqzD-Ieyqu4g7Rj0UJ7iqR6u9-4Bnge-gU74yhG1j6nXhzCWcWufchNP3a31A--ND8mL5cMaP6ZiBas8KFMIjMkHBi6lClZjH4Jkg_-U0dj9OIkRNnRaBcouQfukl1Xqp2ylg4hOrBRYuEObUUrYSKwqtafInP7YY3VzIr5iQ1iMUaAIpA-IfSbOGdDPgFwP2sxPRtbh96VHhw7Coi-zMnzLLO7oDM38HVGXmeA-D33yxMtcaYn2879REw1C1jJbROsgfqhm7ofDXsBXd9rue8IuzTi0-5OQDyscpYDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهباز شریف:
در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق توافق صلح حاصل شده است و پاکستان اکنون از نزدیک با هر دو طرف برای نهایی کردن مراحل بعدی همکاری می‌کند. صلح هرگز تا این حد نزدیک نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/65944" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=nbG0Oymmfzulz_6Q4mboysczj1ZPQmXBuw9pTAZRPfbVcBcGzwkW-Nfblulw6JnnNR2O5l9E9lJ6z4EolBHA5g9FdR-90DJ6OrMtlVsNIF32ivWqRRcXyjmBuRGf6xcxvvTFnUuRDazsLniK_BlKM98QGKbESpXNbQcUVOk-Iiy_sr8YBH6UF8Zj_e746jhm_HzNwaJGuK8XzGDrFRZ0keWR14XnGcb-_JFARpFOG78aN4wpYEUGsFNVr_E1XIF-pTsDByP9jwk9Sifmhnc3UNYJTnH5IThKbSXrNAKOS9R3C2ypRAqRdvHx8ak_PkcdrfZday3oxOhq9nUdKG1JNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=nbG0Oymmfzulz_6Q4mboysczj1ZPQmXBuw9pTAZRPfbVcBcGzwkW-Nfblulw6JnnNR2O5l9E9lJ6z4EolBHA5g9FdR-90DJ6OrMtlVsNIF32ivWqRRcXyjmBuRGf6xcxvvTFnUuRDazsLniK_BlKM98QGKbESpXNbQcUVOk-Iiy_sr8YBH6UF8Zj_e746jhm_HzNwaJGuK8XzGDrFRZ0keWR14XnGcb-_JFARpFOG78aN4wpYEUGsFNVr_E1XIF-pTsDByP9jwk9Sifmhnc3UNYJTnH5IThKbSXrNAKOS9R3C2ypRAqRdvHx8ak_PkcdrfZday3oxOhq9nUdKG1JNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از مراسم دیشب افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65943" target="_blank">📅 20:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65942">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ1RCzmTs-FcRd7mbFrTT4fCXp1uU67AiqEV5DWmiN9gse247_hFP_gaaYLX6gJNRaqq0Xt5rNswUgy3bF_mdipzVRwfc-ZOD0k9LRg_bM3czD2aYi_Hv_26GIzyel-Bdm2C-r4CCM2zS1g_xdrm6bjVShdmNlKRALSghs7b9XpT7ZElQjqFoiwV-Hm3tt08iHjaUBLBoSqD3BA_EMRqBk1hgEgk87T-oDnUGDRxwnL8kHr8PkM43-sFXlvCUNfo785bYQqE-KUjfdbj-oQvG34bKSAX4mgW11qlZZ3J9oRtXRmxRBdOg975n3MvhCx57y4_l_kKWFI0D2rJw4OmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندزی گراهام:
ایده یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی مسئول ایران است، به نظر می‌رسد بی‌معنی باشد. این شبیه طرح مارشال برای آلمان با وجود نازی‌ها در قدرت خواهد بود. آن زمان این ایده خوبی نبود و هر صندوق بازسازی که به نفع این رژیم تروریستی باشد، اکنون ایده خوبی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65942" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65941">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65941" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65941" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65940">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/samNzQYV8ACxELDw41PWpWpmwzcAumlSLJOUvL44FugvICzXxxOwfEyontXBpZXr1cKtrB3KBui8JUOVRV5of7DQUDjMbQbskVSNRfvCsw3uush4TyBqjyZ4dF44NtLoCtfVPUvLAxMZ3nljtqqHwM2BRXXV053a1eVwEihTkLbMeA3GpeA5ao33KLUMtQjaIvVG0b1HmHaTRVdWzf9Dmem9OdsFL21_7QRH9kwJAuKtUcp9IjM2rqi2XryvUzvu_lK9JklygbqteQ6BLlo1WJ1Hu2-92fhQb7tPYhpwwVwgn0RnvlT4j9fem_Jk3tjaHrgwxV-d_U7tmNepsI5Htg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65940" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65939">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oujOM9tE_s8MDhmD8jfsEjObMj-8P8jPbFTs2igpms3I5Blh7dAtEEWJfBStFjgFcc8qGIaoqoJqZAGdIHItVLx2mJ8liJR3NPCjYuqf0aBYap7fJ5KjiPjcyyE_RoNo10YvZdz9tpr2XdK2syhE-zUmyjNPtR-hUz2FeirxXT_K_0pXzRIqQq1-uDKrHyRE1KltYLHnuqJVdI7vpkqiIt6li5a34MBKy99EAdpLpPSVEP61TLlmdrUCvIIVsnNXtbH5aqJay8F-83foW1eSUQxDj3EdxvQoONgz7rE-Yw4rOsqxpcUdgW8GyTYrlgRieiXCfqPOHzvJPB0X2J3leg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ناوهای جنگی و دارایی های هوایی نیروی دریایی ایالات متحده همچنان به گشت زنی در آب های منطقه ای ادامه میدهند و محاصره علیه ایران را اجرا میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65939" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65937">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=gqrpGCYTwbHXr755tqNulWdTzXfMER1kiLuRhNZIMtazagw6oR6LmCuabAnL4TL2ZOsO1OWzELlGYXtdoAvg-qP0CUmsAVJ417kRcTBbvFdX9fiP31WRcDI4EZfHimUsRroU-3TqNTbg7ZjaIoXzq2a-m2wpuuRgERzOPdqHnOzDFysnjQ_FRvK833B9xEwYnanOlJyhkcwJyZq3Cnh2wALskWG6bfo0bxZnnssXlXXits7hQHzZT3Th8QkU8bDcYQlXhuUl1bJM-NAkwbkfD3WPALufCj_nRaN2Qy7YydbxvOeyUU2Q4MTnU8Ay1yrou_LdtEhgZldmle0P6PEemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=gqrpGCYTwbHXr755tqNulWdTzXfMER1kiLuRhNZIMtazagw6oR6LmCuabAnL4TL2ZOsO1OWzELlGYXtdoAvg-qP0CUmsAVJ417kRcTBbvFdX9fiP31WRcDI4EZfHimUsRroU-3TqNTbg7ZjaIoXzq2a-m2wpuuRgERzOPdqHnOzDFysnjQ_FRvK833B9xEwYnanOlJyhkcwJyZq3Cnh2wALskWG6bfo0bxZnnssXlXXits7hQHzZT3Th8QkU8bDcYQlXhuUl1bJM-NAkwbkfD3WPALufCj_nRaN2Qy7YydbxvOeyUU2Q4MTnU8Ay1yrou_LdtEhgZldmle0P6PEemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی قبل از جنگ ۱۲ روزه و ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65937" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI7shHJDCXge3eFqBHAw44OP0CHP8nphkjI2PKoSedoascBW7ZhHr8EvD4Yzq7YAituchejgRoJ634xGGBBiGInIhvc4kia_W2sVBI703P0DNxpdHnMTpbK22n2sLGWGg6AQHk-XCrshLTUcM8CAp3HhE0fw52JSqmqdXtfQHSJkn4tKgubrYMqyeizY1UuTFfZrlb6FlKDvpSgAyyVzRrBiZ55lnXNjVQFJdzPIZbD27FutIJBDdO3G76Vx5S0EOim-DiC8P8kBGAIR8JXlKp25dS0SGYrK7EatSbJ6CGVfj_AgK63wzYz52Wzm6s6mykRRpADpeQR8UjE8W4Rihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: تفاهم‌نامه اسلام‌آباد هرگز تا این حد نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی در مورد محتوای آن خودداری کنند  @News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65936" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65935">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
جی‌دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود. این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65935" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65934">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تا دیدن اعصاب ترامپ تخمی شده عراقچی یه توییت زد گفت رسانه ها چیزی در مورد جزئیات توافق نگید :)))) #hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65934" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65933">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65933" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65931">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-1pIGIJo-rT8sJOFp4Hs7pI16xzSVXV00i5qQgHMBS8qkuLVd-HmcyXz9lEFLl2RIwDKr-h9afFyEgaypFGBuF7095kucPw-kCpBeEq4PRLyzXAyEhOxUKD5piuBmhe-b3RGwhKMqW2_44EBFMVs-C4M-LlhEFddUhSLivNVq2f-lDlptBwKF3DXrMjDmwG7Wu7b_aWib5hMsowFpPW_WGskF84G2dWNXhk78IBzVAfodIC9iU0q-JAsn31UAcne1_xcB9vzYYi8IQUbyVKlkUC4s5lt9rbsQxFvRQp65kB7_c_ca54xKdSumYGMMweqL16Fi96KguEG5A4fMLC3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjBx_i-GLaGVL2LBNDckhYKICMRP2Qi-y3sYKh0UtAV2q6B_IWZoiIPKfTdhB99R7MmMxo7TRVGJHiU9636egytmfQ7g5D2AWtAuXID4r6qQZ8LIq3PE7UlIg4mP3iVW-I-VvInFO3pwTXGs2_FVQ5vYlvP5tPPKp9hoR8POjDt2p9V_35YB3Tmi1KofEoDX2WqTX6XUUklCtlb--nLQKj8Fkg84t7MxvknlfXosBUhmBzNuqNyvCVwNZc1wVMgY9NNLuBQbosLz2nFyxfwd0V0LrFG9znLgZ4bBU-LdGFZVPYok3AZTEcxnOwgHBitDoFs4O_o6pYs1pcPYWO5cPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برنامه امتحانات نهایی پایه های یازدهم و دوازدهم منتشر شد.
شروع امتحانات از ۱۳و۱۴تیر
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65931" target="_blank">📅 17:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65930">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=bi54Q0r-40p4gf0L6DxE39m3AmKCFhHrXZDu7NpsZjPb8cxtYxelRxqdqqq48uWwtwrXz1jAcy8AHPTaPuQNzXnHQX9WMX7G_Q_pYBbBTWOYIhbKM3i3YmmCj63sA519O9ktyvQlVNDQqU5XhsnjQpQt3QihJhLgm8HRVixwkOADnnxGxz46MsXuzF4Pt6TQ-h1T4qKJNM3kgKTGjYC6QhFGctC5twKFg1UrBIb_2cdWK6wLCUtg6PJeHKMqu-ogTkrKiuV0VtSG8JU8MPzBgZi71UCnY7dGt_wxvZmvZ9wEGl1FpEHOO-3cRL9DQ9TKEe8_V-MvIYJEMREf5a9Wzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=bi54Q0r-40p4gf0L6DxE39m3AmKCFhHrXZDu7NpsZjPb8cxtYxelRxqdqqq48uWwtwrXz1jAcy8AHPTaPuQNzXnHQX9WMX7G_Q_pYBbBTWOYIhbKM3i3YmmCj63sA519O9ktyvQlVNDQqU5XhsnjQpQt3QihJhLgm8HRVixwkOADnnxGxz46MsXuzF4Pt6TQ-h1T4qKJNM3kgKTGjYC6QhFGctC5twKFg1UrBIb_2cdWK6wLCUtg6PJeHKMqu-ogTkrKiuV0VtSG8JU8MPzBgZi71UCnY7dGt_wxvZmvZ9wEGl1FpEHOO-3cRL9DQ9TKEe8_V-MvIYJEMREf5a9Wzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین طهلیل ویدیویی بنده از شرایط خاص منطقه برای عزیزایی که تو دایرکت درخواست داشتن
🙏
🙏
🙏
#hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65930" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65929">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=LCNmPyPZ68inCAezB_hgbPSsSn7ARWhMwrTr3Rtg9e6ywGJAdOFN1zKWY7hL6Bygte3ODEwz97kmJYSkjB3zWLe5qyr1kQ5kB_ovPBXUpiS8saGAgezLzfzN3v2uZEvU-Tf2PNL_hQRF5jfUPZ52kCCAf1Dfw_9nUXv4WXFts2D6h55cFihbyc7aC65O1RmZJc94nW1T5tc5ZXn0OHk72jyN2yLmHpDSlpZI1EKuaKmHKbFmkpOlAeiwNk6m4v0xXJ1cvbablB_BYS6ua65amahteEJK570WXp_nSBOgf2T5gDvepWhCtocV0x45VE3lTPVUOu5WXkMEtFGsv1d39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=LCNmPyPZ68inCAezB_hgbPSsSn7ARWhMwrTr3Rtg9e6ywGJAdOFN1zKWY7hL6Bygte3ODEwz97kmJYSkjB3zWLe5qyr1kQ5kB_ovPBXUpiS8saGAgezLzfzN3v2uZEvU-Tf2PNL_hQRF5jfUPZ52kCCAf1Dfw_9nUXv4WXFts2D6h55cFihbyc7aC65O1RmZJc94nW1T5tc5ZXn0OHk72jyN2yLmHpDSlpZI1EKuaKmHKbFmkpOlAeiwNk6m4v0xXJ1cvbablB_BYS6ua65amahteEJK570WXp_nSBOgf2T5gDvepWhCtocV0x45VE3lTPVUOu5WXkMEtFGsv1d39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه ای ۶سال قبل:
هیچ پیام مستقیمی برای ترامپ ندارم چون اون رو شایسته مبادله پیام هم نمیدونم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65929" target="_blank">📅 17:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65928">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65928" target="_blank">📅 17:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65927">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:  ۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65927" target="_blank">📅 17:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65926">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIHWYavKfK2dpn_KAtmhBmvxkdh9_jEfWS9owfo-3w9llHp2HHN5P__KWstpc4f0mLL7MkSKf_GsLbIxdBUrqVkF_azrm8eMX1A2wzlT2PoLyXElar1nWwHZfsuEJbiLAxd0sDsKPs8VwnJNvJy58GjPBo9feMHUIZIT6wp02GKuVI9BjObIdIHvZhp3E2wZAmySW1sFwbyq1P2QdTP5u269By54ncgYggrprSA0IXHzqXzw7QV-BmuWdqLqEfyegb4XLgJan31yze0yuiv3rOIQvpU-qE6maXdHowdtlzN5djm_vaAOZp-HVx1hnqqZkNgPvs6XxwBNmGCVO9Fbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلاکاردی عجیب در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65926" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65925">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFSpSy5i_JmU5Y73KbHzTz-4sxBMZGrn7EKbZIdoQIjMrnjBgerXHzhG14gyvCUAU4IYAR3_Pv-KhMOt4B7ySCYU82ioG7YyCnhLnBu9TpIxIz2l33BasuJfCWc6K0bT6boEAgiCzRU5Ye7OTaFuNd54xlbr_tNF8KRg96Mq6jPzyVBS5Cl_H2hkhYbn_DW10mgYLYZAkLseQ3szQV1beKsTEWjkVBU0tKlbQbcHQpNTO0z3yg9r_I_Ik334gJfBwe8cFbMvOn12j3Ylt1tZl15Wo8cQ_Qhdw7e6mQWoicGhy7B79nNJa_HyB70Xr2NuVZnpX4ZmRxXZ1TItxZgvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
ترامپ در سال 2049:
ایرانی‌ها هر لحظه ممکن است توافقی را امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65925" target="_blank">📅 17:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65924">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXxkPlwWypCOSnXq-UCtMmeatdIQJbCN4mN1uwPiWJAbTu-et6OIMfkDHDq4N8s2EsVEYWxDWwt1l4ADZd4UX4u4iPCreIFxaka6cURKzxGzRwHq1syS3Q8UDbCAIY53eYkXWXSwipXaNbb1J9uLaLfdtsRVRgvzFznNnmKsvktnDylKGkWRsVrB-e6P2SE5pxAe5zKoLNHEh4RAS4kRVxwRuNn0qmshMk1mq7hpXfa2fQIslES2Fo0BwS9qkpHyqJqxHY-aDPtDyF8oOEjusEaVsNcCnlg1sRzK5PrPUTOOtNaj4P7NfYKrIEIdWVA_X4goRKvXw3vuL0dbdA8T-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
مرندی، عضو تیم مذاکره‌کننده: یکشنبه در ژنو اتفاقی نمی‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65924" target="_blank">📅 16:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65923">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=QoPp8IGnvXTWin18bsWuaUU_HSqpFhdpn-TNxi5j90un7D55UhPsGm4gxDwaWA0f9Y30z_i5R-ntdOKOehnu2LYzaUPZyNazfbHSvFnjrFYEmGhNuTAhp5Iwu_IxRrFw4upRCHFpy0OA052sser5UhcSXVhjLhA4uvsLwzrrkhopstXVchfT4rVFIC5YwsRgUGMhz5DMhrOXiOlLAVeBd5jDct2YGSJM-0TRkhCdnjhVTbIPJJW106hqx8izthGbffQXKwsti_w7hfj0COwFfnehksAj79RAC6wNvxZdcyADnnjymY2F5DLmDbzzIO-Pr0FyDi0iJBM0d4dOy5X7JmD58rZWLDVpkyY_G5gtUMYO8czabJFXEBEbd7YLhJTMrs03Kpb-5hmhFr7Td8jNjwAKwx8mpsGJLm-3aM9Y6V-uXvjkPynr7NahMM9coxLJF1q7ByToBb-y8_PbMvXcYCNO7elx_zauJ99ta0DsY3wNu9557-xgfwkhdd5KWrkQ134Q0QUlUuRLZqr11kMOH6UltV1qMaPer3KWUkRTPm_YOrn6QwtmeJonx_M6aLj_6W8GALjKsV1nDZl7qQIzwM1jFnJcHpvDKcxyvlYichzRibTgic3yK5k2KivgOk96tR7JG7M0G03qppswSDR4cH2evyq1auYAooy3HR7e4QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=QoPp8IGnvXTWin18bsWuaUU_HSqpFhdpn-TNxi5j90un7D55UhPsGm4gxDwaWA0f9Y30z_i5R-ntdOKOehnu2LYzaUPZyNazfbHSvFnjrFYEmGhNuTAhp5Iwu_IxRrFw4upRCHFpy0OA052sser5UhcSXVhjLhA4uvsLwzrrkhopstXVchfT4rVFIC5YwsRgUGMhz5DMhrOXiOlLAVeBd5jDct2YGSJM-0TRkhCdnjhVTbIPJJW106hqx8izthGbffQXKwsti_w7hfj0COwFfnehksAj79RAC6wNvxZdcyADnnjymY2F5DLmDbzzIO-Pr0FyDi0iJBM0d4dOy5X7JmD58rZWLDVpkyY_G5gtUMYO8czabJFXEBEbd7YLhJTMrs03Kpb-5hmhFr7Td8jNjwAKwx8mpsGJLm-3aM9Y6V-uXvjkPynr7NahMM9coxLJF1q7ByToBb-y8_PbMvXcYCNO7elx_zauJ99ta0DsY3wNu9557-xgfwkhdd5KWrkQ134Q0QUlUuRLZqr11kMOH6UltV1qMaPer3KWUkRTPm_YOrn6QwtmeJonx_M6aLj_6W8GALjKsV1nDZl7qQIzwM1jFnJcHpvDKcxyvlYichzRibTgic3yK5k2KivgOk96tR7JG7M0G03qppswSDR4cH2evyq1auYAooy3HR7e4QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هگست وزیر جنگ آمریکا امروز ۴۴تا پرس سینه زد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65923" target="_blank">📅 15:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65922">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
خاورمیانه در این مدت
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65922" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65921">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:
۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند
هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت ۶۰ روزه پس از امضا انجام خواهد شد.
۲. تنگه هرمز؛ نه واگذاری، نه نقش آمریکا
ایران هیچ تعهدی در مورد واگذاری مدیریت تنگه هرمز نمی‌دهد. آینده اداره تنگه در چارچوب یک امر منطقه‌ای و از طریق گفت‌وگو و تصمیم گیری مشترک تهران با عمان حل و فصل می‌شود.
۳. پایان قاطع جنگ در تمام جبهه‌ها، از جمله لبنان
هدف اصلی تفاهم‌نامه، پایان جنگ در تمامی جبهه‌های منطقه است. آمریکا تعهد می‌دهد که اسرائیل را وادار به پایان جنگ در لبنان کند و عبارت «تمدید آتش‌بس» در متن جایی ندارد.
۴. آزادی دارایی‌های مسدودشده با ساز و کار مشخص
بخشی از دارایی‌های مسدودشده بلافاصله پس از امضا و بقیه به تدریج در طول مذاکرات آزاد خواهند شد. تهران تضمین‌های روشنی بر اساس ساز و کارهای مورد نظر خود دریافت کرده است.
۵. غرامت جنگ در دستور کار
خسارات وارده به ایران در تجاوز آمریکا و اسرائیل از جمله موارد مورد اشاره در تفاهم‌نامه است. ساز و کار اجرایی دریافت غرامت در مذاکرات ۶۰ روزه پس از امضا مورد توافق قرار خواهد گرفت.
۶. جزییات رفع تحریم‌های اولیه و ثانویه؛
موضوع مورد بحث در توافق نهایی
رفع تمامی تحریم‌های آمریکا و قطعنامه‌های بین‌المللی در مهلت ۶۰ روزه مذاکرات هسته‌ای بررسی می‌شود.
۷. سه موضوع و ۶۰ روز برای توافق نهایی
در مذاکرات ۶۰ روزه تنها سه موضوع بررسی می‌شود: استمرار برنامه صلح‌آمیز هسته‌ای، رفع تحریم‌های یکجانبه آمریکا، و ساز و کار جبران خسارات. هیچ موضوع دیگری در از جمله توانمندی موشکی ایران، دستور کار نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65921" target="_blank">📅 14:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65920">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
متن توافق پایان درگیری میان ایران و آمریکا تقریبا نهایی شده و منتظر تایید نهادهای مربوطه هستیم.
متن نهایی تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65920" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHILFyKe6RlgAK10JotHAuHKuOm2A86mD57ZA-rJ_YTEQEiQvlttTBWepeJqD5IWIozMA8HievO8LICfKAaXT_vvD6W6UvRDlnVkNU7ksBOYWrfnw302VJuR_vCTRFYr1dKMes4MSFIQc4lV2AfFuKGjp6iFvw_vPISLnGwa6hea_oaIe2Wp2ac7YQPLtE245zQTZB3oX_biWoudAOgWNWHjgTszLJpxMWU7FsNMtNSrpFDdsOgBbAOKU22VKi7bpJOxqQ929gCb4Ei_vbGjwwNFqUpcd-hs7GVoe10M7xJVZErk0Bx8x59DiIbOZVaIHwAHA8d_ExcZVvcZ-rV4aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lg7YmHqnOTRcmvlQ0yOBOK95NEqi409lb3W5G9RbEzfsm8rUFH3EwSpMKH7aOIIoIvumL4vVBvCdYIVgSnmCz2godQeOLRipDHQLgSmooe5wW94p84GaXX_uyTRjOaK5S0RLo44_WMjjNq_ZVkpZxLjG8CuTexx3U6amzksawiV7Gcl6sUS9ILVIvqD_OUGUKg3_MVHKLpk_eiVRYSCMLH4Y33_1Cs6PHTPMGYKq6rCbtvMYfrHY0Jb98fnZomARMOky2qbt6MeytdIRxdTEgipDjlquDR3BviwYsK6dYJLpD5ZrLTIc7VlNKH64unawm7iZDmYrm1Pjj5D3wqg0JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصویری که یک پرستوی نظام در تجمعات شبانه از خودش منتشر کرده درحالی که چاک سینش پیداست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65918" target="_blank">📅 14:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=eMAi9-CexRuGvNT-6KmIqusrV97ytz5x8iySr0hXNSAweGP_f-WWhN9pfvJUHXZaF5QfwqQcrfMoa8CkZQ4gLpyxMkKmVNBBiinCyhKpX2sUMMoOdYrZZczEAMr9bjseVcAcnRrAY-Y6xA6Ug_JbCFwhPKERtlamnXH-iO3cuIRuAFMX3kiYGgblA2WXJC6Bf5xG6sgNBkvvTD49-dy_e96G0CrKTEwNSQEA_bK61qo06Nxscp7tDJdtR9czWxheeCr2styVOTe3_xe4eDIYBrJfWN1v6Ce9dmc_nYkIUYzB8l0TLQ-iFd4FPY-p9q-rAbzD6ZekuwaajC5it8N5Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=eMAi9-CexRuGvNT-6KmIqusrV97ytz5x8iySr0hXNSAweGP_f-WWhN9pfvJUHXZaF5QfwqQcrfMoa8CkZQ4gLpyxMkKmVNBBiinCyhKpX2sUMMoOdYrZZczEAMr9bjseVcAcnRrAY-Y6xA6Ug_JbCFwhPKERtlamnXH-iO3cuIRuAFMX3kiYGgblA2WXJC6Bf5xG6sgNBkvvTD49-dy_e96G0CrKTEwNSQEA_bK61qo06Nxscp7tDJdtR9czWxheeCr2styVOTe3_xe4eDIYBrJfWN1v6Ce9dmc_nYkIUYzB8l0TLQ-iFd4FPY-p9q-rAbzD6ZekuwaajC5it8N5Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وزیر ارتباطات: بستن اینترنت امنیت نمی‌آورد. وقتی اینترنت قطع بود، وزیر اطلاعات، لاریجانی، رییس اطلاعات سپاه و بقیه ترور شدند. با بستن اینترنت، جوانان نخبه مهاجرت می‌کنند و این ضد امنیتی است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65917" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65916">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
ترامپ از زمان شروع جنگ ۳۹بار گفته با جمهوری اسلامی به توافق میرسه
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65916" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65915">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=Qrf4SH2i1Fq8DH2TmFU_9aWa5kHakqWdFbYdiQaEEDnHSjIJxI6nTMB9moGanO3M8edVhea_z8pZEq1ZUGMbPtON2ZisnYsbdsnFkael45mBjQQQSuHJnnEfw9-NOlcjAgwuKx_NqN5F7pwKRoX3rNP_BmDCYEYud_Y6mlG7TIl0eyNxyLC0TgUtmAcgSvDAWJhP3XwFTEfwq_5Zvjy8pBCI1iv4Sc5J7anPL_rqG43k_GDJ_G0iv96Xmirh7fDgjJhnboPPY7jA20l1xEEOJXtPHfUZ3nM5BfNAMgEPHKMKsn3jDlaravxuZLEW7VQYL1RdV6zzwhwy3usadFJFzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=Qrf4SH2i1Fq8DH2TmFU_9aWa5kHakqWdFbYdiQaEEDnHSjIJxI6nTMB9moGanO3M8edVhea_z8pZEq1ZUGMbPtON2ZisnYsbdsnFkael45mBjQQQSuHJnnEfw9-NOlcjAgwuKx_NqN5F7pwKRoX3rNP_BmDCYEYud_Y6mlG7TIl0eyNxyLC0TgUtmAcgSvDAWJhP3XwFTEfwq_5Zvjy8pBCI1iv4Sc5J7anPL_rqG43k_GDJ_G0iv96Xmirh7fDgjJhnboPPY7jA20l1xEEOJXtPHfUZ3nM5BfNAMgEPHKMKsn3jDlaravxuZLEW7VQYL1RdV6zzwhwy3usadFJFzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آتش بس در خاورمیانه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65915" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65914" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65914" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=KAW4Ox3q99hMOKwxYMCxet8PmjzdrCNA0LN4259EO9xalpx5Oiyyz2cVk6Wvjow2hQozHHFusxduhMwDlGcow4AG4-DGo1iYzJabWhnEfP4Mh8pX3Mtde6WLj0SYnWpRSL91cKY0oGOZIZdP8Q9CcM7itEofJcAilc_lTuY2W5cS1y_MIEAAzXwZFq_7ZLOkBNEQfUKyCTR1Y-Lj0DsgJ8VYcBXdN_ZXkER80WwCwd0K8O2yPn-YSzELpU8qH447T0OOWTX_11LnIMQYEkkQ6WAFIo2Fa6pFON8ZGOg5ysMjACVBFaslid4ZB6lww0oAgyDUOd8rpctKhakLFaJJtgGhTuu0UzeRiiSH5-Pi9zn9jxbTVhFOej0Ij-SkrpmCMtXIoBhUrWIJk6NbbP114hvgrz7tM7Qs17NLw5LcLQ7MuVd5bYW52_1knIfZyw4gGn74AC-xhRh_UCivb_hAiTBUxNU7gNzlZl0TCTpMmsdIL3IMzSks8beoFUBHgAIFHstSuRvB9lwGxjf9ch0_opIzKo9MMfAeUNAXA1_-KFDPgCpj2IWEx63dbR1Gb3OyqtQxvzST3cnEobVOuFMcaI7zS-PDXze0v7k5AmNYiEAhMOMVJ1wYxApE7IlU05GBkIubQ2w-Bw-1qRIvHxezOsnC-Nha_sCa635zUkq3Xh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=KAW4Ox3q99hMOKwxYMCxet8PmjzdrCNA0LN4259EO9xalpx5Oiyyz2cVk6Wvjow2hQozHHFusxduhMwDlGcow4AG4-DGo1iYzJabWhnEfP4Mh8pX3Mtde6WLj0SYnWpRSL91cKY0oGOZIZdP8Q9CcM7itEofJcAilc_lTuY2W5cS1y_MIEAAzXwZFq_7ZLOkBNEQfUKyCTR1Y-Lj0DsgJ8VYcBXdN_ZXkER80WwCwd0K8O2yPn-YSzELpU8qH447T0OOWTX_11LnIMQYEkkQ6WAFIo2Fa6pFON8ZGOg5ysMjACVBFaslid4ZB6lww0oAgyDUOd8rpctKhakLFaJJtgGhTuu0UzeRiiSH5-Pi9zn9jxbTVhFOej0Ij-SkrpmCMtXIoBhUrWIJk6NbbP114hvgrz7tM7Qs17NLw5LcLQ7MuVd5bYW52_1knIfZyw4gGn74AC-xhRh_UCivb_hAiTBUxNU7gNzlZl0TCTpMmsdIL3IMzSks8beoFUBHgAIFHstSuRvB9lwGxjf9ch0_opIzKo9MMfAeUNAXA1_-KFDPgCpj2IWEx63dbR1Gb3OyqtQxvzST3cnEobVOuFMcaI7zS-PDXze0v7k5AmNYiEAhMOMVJ1wYxApE7IlU05GBkIubQ2w-Bw-1qRIvHxezOsnC-Nha_sCa635zUkq3Xh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65913" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
کانال۱۲اسرائیل:
مذاکرات نهایی آمریکا و جمهوری اسلامی در مورد برنامه هسته ای و مسائل اقتصادی است و برنامه موشکی در آن جایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65912" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
یه‌یارو بیکاری بلند شده تمام اسکناس‌های کشورای مختلف دنیا رو جمع کرده و باهاش ویدیو ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65911" target="_blank">📅 12:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65910">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
رهبران قطر،امارات و پاکستان کسانی بودند که مانع حمله دیروز ترامپ به ایران شدند.
سران این کشور ها به ترامپ وعده دادند که توافقی اولیه با جمهوری اسلامی دردسترس است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65910" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9247426e69.mp4?token=lb5MopSu5suaTrDYCkrYL-Tgu2MhQI0mc40-fY_t6v9324PNLI2y796yL8tnAnDW-UiRVgB28-tp4DpU2V6UVBNVla4W4EKTX6K6rVH34Q8vQvwGVGSYrv1PuqNEXvrYuUBeRbV3Lc35tOKW7ajONS8Y1woCWCmg60H_TdhCcPmyzMtHd0D-Mbn0MsHFlK4n9q4tQJBy3v52EGHxsf_DqHg2Ulugl3Qru_oE4urR43e_R8YI61bJ7EPDMZDoTwg10OvtJfNO1QqhlLV-e4SJKovmfOP4xPL6TXaNdLD_CjP55SE9Wme8yykPNCStBz-waYKXPBOQBtTR2dKN-xnUsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9247426e69.mp4?token=lb5MopSu5suaTrDYCkrYL-Tgu2MhQI0mc40-fY_t6v9324PNLI2y796yL8tnAnDW-UiRVgB28-tp4DpU2V6UVBNVla4W4EKTX6K6rVH34Q8vQvwGVGSYrv1PuqNEXvrYuUBeRbV3Lc35tOKW7ajONS8Y1woCWCmg60H_TdhCcPmyzMtHd0D-Mbn0MsHFlK4n9q4tQJBy3v52EGHxsf_DqHg2Ulugl3Qru_oE4urR43e_R8YI61bJ7EPDMZDoTwg10OvtJfNO1QqhlLV-e4SJKovmfOP4xPL6TXaNdLD_CjP55SE9Wme8yykPNCStBz-waYKXPBOQBtTR2dKN-xnUsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یکی از کشورهای آمریکایی پلیس به یه زن مشکوک میشه که ازش اسلحه بگیره. تهش طی تحقیقات زیاد متوجه میشن اسلحه رو تو واژن خودش مخفی کرده و با تهدید پلیس مجبور‌ به تحویل میشه
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65909" target="_blank">📅 11:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا منتشر شد. این تفاهم شامل تعهد آمریکا به رفع تحریم ها، خروج نیروهایش از اطراف ایران، رفع محاصره دریایی، بازگشایی تنگه هرمز، لغو تحریم های نفتی، و پول های بلوکه شده ایران است.  آمریکا موظف است طرح بازسازی اقتصاد ایران را ارائه دهد و در حالی مذاکره نهایی میان دو کشور باید در مسایل هسته ای و اقتصادی انجام شود، بدون بحث درباره برنامه موشکی ایران. این پیش‌نویس نیازمند نهایی شدن در نهادهای مربوطه است
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65908" target="_blank">📅 11:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک دیپلمات از یکی از کشورهای میانجی که بندهای متن فعلی را با من بررسی کرد، گفت که «ایالات متحده و ایران در مورد متن توافق به توافق رسیده‌اند»، اما اذعان کرد که هنوز تأیید نهایی لازم است. با این حال، هواپیماهای نیروی هوایی ایالات متحده دیشب با تجهیزاتی به مقصد اروپا به پرواز درآمدند تا برای احتمال سفر معاون رئیس جمهور ونس به مراسم امضای توافق در ژنو در روزهای آینده آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65907" target="_blank">📅 10:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
⭕️
توافق قریب‌الوقوع جمهوری اسلامی و آمریکا بزودی در ژنو امضا خواهد شد و به‌نام توافق "اسلام‌آباد" نامگذاری می‌شود. طی این توافق یک آتش‌بس ۶۰ روزه که لبنان هم شامل شود، شکل گرفته و ایران می‌تواند با پول‌های بلوکه‌شده خود کالاهای بشردوستانه تهیه کند
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65906" target="_blank">📅 10:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=J5FeiHPX1UoxH0xBXM4Cgb6jV696MTPxkq9I_zYGm7Q4RR42ypKkt5Die7-Zwt1lCfT8qgp8Hnkljp9tvUbgkMVYD4HCoYAAVVNfF3pdKGeFHqkJIjQ37g7CYZrLNafaGPGmFNi4P49t71riDtHg8T-zRQDPLIh9S9buJrgtidcwTL_KeHDmmd3hLDGsCoD620G30E57Bk3qQoXLMyI3BfsY-bm00U2RhcHroy4T3F5YTSzxqgo4wAvaIVm6pNKjLf5JKjGdNZWHIbocAtiTorswAEnujrPMyExJ3mhdU-H0J-gvjZHyxbLPIxajffxQEYuGfZfAzmkYN-LuIcZGHRqeVPsDaW5AYbv2lVdE0UM4nNjQRH2sh4Ep988ZveE_XVxn7lSl9MeFiT6bSV_tQHlp2_S9hxIBSuq3GHkY-abZNuJ4mm-EBkcnW8vxN41oGiehadpgnFXlIb18-NT8YVQ1l2aWAu52wa1hodat3_5YXj-Dmjd2mdRjVqpOlMpQAKGzhEfhHgZPmxliW63rLo4KERIOKVTBoJ5BNHaa09znTuIiIHw3ElZUd2Tm_OLNmnLGhcsgtc5dFRktbR68n_6F81I3B2RjZKqlH1ZG2dpyly4GzUJS32UOauVrCW7xHnbyHtq7gTVRmv-HsfMMXm2PTMV_mZZCZ-jRH-cPByo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=J5FeiHPX1UoxH0xBXM4Cgb6jV696MTPxkq9I_zYGm7Q4RR42ypKkt5Die7-Zwt1lCfT8qgp8Hnkljp9tvUbgkMVYD4HCoYAAVVNfF3pdKGeFHqkJIjQ37g7CYZrLNafaGPGmFNi4P49t71riDtHg8T-zRQDPLIh9S9buJrgtidcwTL_KeHDmmd3hLDGsCoD620G30E57Bk3qQoXLMyI3BfsY-bm00U2RhcHroy4T3F5YTSzxqgo4wAvaIVm6pNKjLf5JKjGdNZWHIbocAtiTorswAEnujrPMyExJ3mhdU-H0J-gvjZHyxbLPIxajffxQEYuGfZfAzmkYN-LuIcZGHRqeVPsDaW5AYbv2lVdE0UM4nNjQRH2sh4Ep988ZveE_XVxn7lSl9MeFiT6bSV_tQHlp2_S9hxIBSuq3GHkY-abZNuJ4mm-EBkcnW8vxN41oGiehadpgnFXlIb18-NT8YVQ1l2aWAu52wa1hodat3_5YXj-Dmjd2mdRjVqpOlMpQAKGzhEfhHgZPmxliW63rLo4KERIOKVTBoJ5BNHaa09znTuIiIHw3ElZUd2Tm_OLNmnLGhcsgtc5dFRktbR68n_6F81I3B2RjZKqlH1ZG2dpyly4GzUJS32UOauVrCW7xHnbyHtq7gTVRmv-HsfMMXm2PTMV_mZZCZ-jRH-cPByo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه خبر:
با صراحت میگویم بخش عمده ای از شروط ده‌گانه در توافق وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65905" target="_blank">📅 09:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=i9m-fnujyXyI67JM-FVBowWw4HKk4Dn1C-HleyLhEjfG9xhfH5xVFd-y6ihtBKeVhXBevSYeXGzLbKcjUv1UCJA1KA90y2od5nz1ugzYKcjl3PoeK6tyvpMTaHOL4evhP6CB3vUCd6Ukb3fMtaIfpdSs7tX7oI3OBoK8HEvzQUyT57WaFEiL3FtIeMPEi8RDRU6Ag29pBV0Nt2CC9MZP80bC0XPCzuHA45SCEZhgRtdtrtG_DTJaKQfusibeSIK3AXoRCTkyxOx1eRDeP5JzAQIeUG0kQMyBfbKTg_SjPR1FqkGyMsTUA3-xoyObYX5kAnoQg3iqLCGID2vwbGIFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=i9m-fnujyXyI67JM-FVBowWw4HKk4Dn1C-HleyLhEjfG9xhfH5xVFd-y6ihtBKeVhXBevSYeXGzLbKcjUv1UCJA1KA90y2od5nz1ugzYKcjl3PoeK6tyvpMTaHOL4evhP6CB3vUCd6Ukb3fMtaIfpdSs7tX7oI3OBoK8HEvzQUyT57WaFEiL3FtIeMPEi8RDRU6Ag29pBV0Nt2CC9MZP80bC0XPCzuHA45SCEZhgRtdtrtG_DTJaKQfusibeSIK3AXoRCTkyxOx1eRDeP5JzAQIeUG0kQMyBfbKTg_SjPR1FqkGyMsTUA3-xoyObYX5kAnoQg3iqLCGID2vwbGIFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته شده ترامپ بعد دیدن این ویدیو تصمیم گرفته که توافق کنه
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65904" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0auxZR6F2XShr1W8NGysaoLY3e0jckgpwEzXUgLo2430sVLN_WEOHOSOGuzl1D-oJbWWZu-1Rfz9nGdHArBTZEp1r2eLIBmW5yeZ5r4w9YWUaqwWRLlGsayPJxAvfG3PIAZ5LQbFv6fMv5z5cClR6ZzMloOaZWz0wuIoFRvkYMZRv3c7BWbBA_uYDyU6gVB9nMTgxvlj179KI1E362Y4h_5XDlwCofkp1SrLvrA4WeOpl32RNVua7bA0YnbiyExT9MEXYYoSTPNGgfHdWDlejY_z4gC2o-L_cV7h-mKCVt4yvaOrXRkoXcCv0-9fcIanjmNxDgM50b3wtEcxq00IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین:
اگر همه این دولت‌ها با این توافق موافقت کرده‌اند، شگفت‌انگیز است که چگونه همه این دولت‌ها به این سرعت امضا کردند در حالی که ما اعلام می‌کردیم که در اسرع وقت بمباران خواهیم کرد.از آنجایی که این توافق انجام شده است، آیا می‌توانیم آن را ببینیم؟
در این توافق چه چیزی هست؟میتوانیم آن را ببینیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65903" target="_blank">📅 04:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTaCgmXx_YkVBHp1UM9otx_s4pSCYCm3p2fEUXpiW6ljXc3WKh1Fxns6fKLkH2KWoQGYNRRIcLPrrwydsnLCiLkB-w-kJMBF0FmUWigaKycgeUduvDlU5pvz6kxvv3tlfqYMiwVjulznF9xTiF4op6ezBVDHzFsLofCcdes5N1IMl7mN624i7lr05pCHreWnoAQRdaeequ664zNSRCpqSE71ZJk5yU9cCF-K2rAuaqI7XZSzRU7AvXJ5FOdbgGzmCPn4WlOrUHHxMQx9nql14MeVMJJmfKmMmb11FIDbffcDK2QYD2LRlCS5F6PHn-mz6Kmp45_Kk7W5Zg_HlFenhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دقایقی پیش زلزله ۳/۱ ریشتر در پردیس تهران به‌ وقوع پیوست
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65902" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
رئیس‌جمهور ترامپ درباره ایران:
ما با ایران توافق کردیم. معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
مردم خیلی زود به خانه‌هایشان بازخواهند گشت. تقریباً همه چیز تکمیل شده است. ما هر آنچه می‌خواستیم را به دست آوردیم.
نکته مهم این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت. یعنی نه توسعه یافته و نه خریداری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65901" target="_blank">📅 03:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65899">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=EnOF9DzRCDOlUocOjGFnxkiCRiANl86FvlwSPpisc1pB1pu3l1n8-lvdiQslXpBJHbtVw7eU2Klz1_VwehgzWAAAT7qptppHo4hh1d1Cimb441TfVAw9vGPnGXCRptwvfPNUxl-MLuaoKRxcUraU7IexUWLctf1xn1eTAjOsBF5JYuUSr79y_LZ57KgUH8HIB6u8Sk84mXB39ZH-1eGS9g-5B3Cw8JtE7znIwdq6tkjXJMizdShIziXnRREzXpVmPk0jNJSjDKxgJ3iXkCyzHXRM_U-fYw0OlafmHjAmg2lPh5GpK63lDv5Nsp7BIOotaCkwEWbEv3KxyHVZi0xBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=EnOF9DzRCDOlUocOjGFnxkiCRiANl86FvlwSPpisc1pB1pu3l1n8-lvdiQslXpBJHbtVw7eU2Klz1_VwehgzWAAAT7qptppHo4hh1d1Cimb441TfVAw9vGPnGXCRptwvfPNUxl-MLuaoKRxcUraU7IexUWLctf1xn1eTAjOsBF5JYuUSr79y_LZ57KgUH8HIB6u8Sk84mXB39ZH-1eGS9g-5B3Cw8JtE7znIwdq6tkjXJMizdShIziXnRREzXpVmPk0jNJSjDKxgJ3iXkCyzHXRM_U-fYw0OlafmHjAmg2lPh5GpK63lDv5Nsp7BIOotaCkwEWbEv3KxyHVZi0xBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ درباره ایران:
امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود. این ۹۵٪ از موضوع بود و آنها این کار را به قدرتمندترین شکل ممکن انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65899" target="_blank">📅 03:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65898">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65898" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65897">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aAM72pUl6TTtb0RyIGXIy9yeP5EU1aW_fdymBu80DpPGXSwMVKHS7h7_AkNaPwOrTPQc0mEQ7gEZbA1Gg2GxxvqG0MwSPnVY47r1jgGm_zYg7QBzo_oShfctEF0nytI3QILD2IKx62VaGG0SuLXBj46DBVA2IvJmv-RS8gG9pnWbFF-oq7AbYwSMEyceLORPETv51sIKula936BzeE1qThoEXZDRaPdDY_gyj-lRn5-RWscfNCxnCSIaErWJy4chtk0-J-VAv-gHoZ-_UJLPeoNmr5eOFNVOIPqxQS7KLMZ_nwRqZTvp7mJ93nC4kycYWWD1MuBJuIjw6G6q28MbFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65897" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65896">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
صداوسیما:
شنیده شدن صدای دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65896" target="_blank">📅 01:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65895">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdfTIY-KBBVXk-yki2nW4uUB5ODSSi6P8tyzVebaVNy-zaqWX4Fn3w-zgkleRJ4myFfAFS0SGrmFm-Caa4qN3aCGqA8Cok1UyFB0aXwomBkTuQGw4mnOQFwbMSWWNNUw9xktqmEZPsFmjj2qUm5Um0OKETSmPnUXzypYPzWhw3Yd9wVsV64q4rgh16e3IDdRV_G6n0rHhM5NGtpEY3_C7dTXEBsNSZdKIKv6ceuw20DIZWS-SAOjVyQMe1_IpGH10EvlOkfSIAC9MjNeNdLcc6C5sDcz8d27jmhlUaMXTRxJxauCgoEyRtibF2FJBb8fM5w1zpbIH6_gyKsp68mHVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام کد اضطراری یک F35 در آسمان امارات
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65895" target="_blank">📅 01:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65894">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دیگه نمی‌زنن
😭
#hjAly‌</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65894" target="_blank">📅 01:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65893">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
فعالیت سوخت رسان های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65893" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65892">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
مهر:
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65892" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65891">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی تایید نشده از انفجار در گناوه
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65891" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65890">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
منابع محلی در سیریک صدای انفجار شنیده اند اما هنوز علت این انفجار ها مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65890" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65889">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvznYP9KZsS7Ng2Cox_Xxsfxa0lMMzqihRLyBoY9cST_NL0sAUGBCjevfRKqAot6tiwTUuJkeEmgTsmUkgzWPWNuRHMMeJRY7McXWq44SNQF6wJ86iBVVkhG8Imqdmr-oqQ44ooSwrw5WdNWxa4WRLpfFVbduhKm9OKQO4Z41n7cxiIo_UYea0hXoh2bI6je-wvlt2_TddePxZn-JV-eF-qjcTgkHt11gqAGtbwdP_UHFev6NITYlQDJXBydLVioL7w_ilhqI-qdumWksNN5W0mFqqB0tdcWxHCPdLE6NxJGhSiIbMzsm3EidbkUgwmbezE7UanUoT4pClOVB2595g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
تنها یک پست از ترامپ امروز 1.3 تریلیون دلار به ارزش بازار سهام ایالات متحده اضافه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65889" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65888">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐌𝐈𝐑 𝐌𝐀𝐒𝐎𝐔𝐃</strong></div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65888" target="_blank">📅 00:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65887">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما به نقل از سخنگوی وزارت خارجه:
قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی ندارد.
مواردی که درباره توافق مطرح می‌شود گمانه‌زنی است و موضوعی نهایی نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65887" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65886">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEZ6qWxP1Rk_XJLyOm2vKmHodWdKM2635GJt_CC20lv_l0ENTfyz1NsVIWJXOzQZpYtxVG2Nso0Oo_6wAswUuz_0uE3XnJvlaI-xO6F8-9-bhNCC6AL3XS4Ricr2wi9o9v4TUEutxYxuBZovOieuS0t3ZKSio_pfUylS3yxZ-bLbBMmLaWSTms5ihjk-wxM5_Hr3mgtSx0bUv0wSBXoFL0oIrBDmOQm2QPTCWLQlcRg-MQN4VT2IgRNaUSOe50Ve25l_MoFBjxvZfRNZVoj1YZmwMu6O8QCuRSztdjxatsvmUn_-YP9Sl9GQpOPLFk-JrXHSSehpSL80z_sXtHGmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:   رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد. اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65886" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65885">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65885" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65884">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:
رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد.
اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات شامل حذف مواد غنی شده،برچیدن زیرساخت‌های غنی سازی،محدودیت تولید و برد موشک و توقف حمایت ایران از گروه‌های تروریستی وابسته به آن در منطقه باشد، ابراز قدردانی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65884" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: بعد از توافق سریع محاصره رو بر می‌دارم
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65883" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65882" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ نورالدین الدغیر خبرنگار الجزیره در تهران:
دیگر همه چیز قطعی و تمام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65881" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65880" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=K_e2TS_e6cqgzxXg_1gi-lkpjsPUhCsobL40K9oZcx7iJgcWWuWUkmD82XLxMa5tLvMp9f9NUutnmlnls0Ml0UTyTNH1sp5S-37IaN7pkNIg53Rwo1Wx7OX19iFBOWpJrrBos5hRspZBUViYKuqNyhk4N9oOxyPgzUoCoYhCY56tX2ooyx7kfmVeE3Cy9orRma0BOrZov5ad7AG_ahvDbbSl4kk-xxAB8iB8RXU8l0Wrhj8SI9hokBhTI9uYuIGbLydgX_9-nMcV_yQNOqIxzPOD6iWfIIsqQGos77VK78HcOeEtdPjpoa6cd15aH9LJkzFTnu12LKldNkZ6izA23Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=K_e2TS_e6cqgzxXg_1gi-lkpjsPUhCsobL40K9oZcx7iJgcWWuWUkmD82XLxMa5tLvMp9f9NUutnmlnls0Ml0UTyTNH1sp5S-37IaN7pkNIg53Rwo1Wx7OX19iFBOWpJrrBos5hRspZBUViYKuqNyhk4N9oOxyPgzUoCoYhCY56tX2ooyx7kfmVeE3Cy9orRma0BOrZov5ad7AG_ahvDbbSl4kk-xxAB8iB8RXU8l0Wrhj8SI9hokBhTI9uYuIGbLydgX_9-nMcV_yQNOqIxzPOD6iWfIIsqQGos77VK78HcOeEtdPjpoa6cd15aH9LJkzFTnu12LKldNkZ6izA23Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری
: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65879" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=fgvjNqGswovORTMWVspy0YsD-lvB5f5IW3aKx9eXu3tuhFCDtjqcq89VsdFRO2mRJ9l30xiM7CdtdLMkRFjvh7EAP6hEm_UlSt4XI58KKegC-k0uvzG1QAIDzTCkdE2rdQs_G_Kr6nxik6Mk_bunxeDqsu_EJfMvJ84bXcGOysGJjntbvl_MRaZlzmjNtPpXfIkxUQ2km8Z0HxzCSsbQyzsP2GTJrztel1NCZhRo32ApkL7acckryTZ7FY_ca7-CrZwSUM_hCBJLlUUgkmfec7vTROJsqiAjIxAqQQZqutmVWsIalVzH2ouQMERx029WB2nqVLgVGvkpxRIvATltVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=fgvjNqGswovORTMWVspy0YsD-lvB5f5IW3aKx9eXu3tuhFCDtjqcq89VsdFRO2mRJ9l30xiM7CdtdLMkRFjvh7EAP6hEm_UlSt4XI58KKegC-k0uvzG1QAIDzTCkdE2rdQs_G_Kr6nxik6Mk_bunxeDqsu_EJfMvJ84bXcGOysGJjntbvl_MRaZlzmjNtPpXfIkxUQ2km8Z0HxzCSsbQyzsP2GTJrztel1NCZhRo32ApkL7acckryTZ7FY_ca7-CrZwSUM_hCBJLlUUgkmfec7vTROJsqiAjIxAqQQZqutmVWsIalVzH2ouQMERx029WB2nqVLgVGvkpxRIvATltVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرِ واشنگتن #hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65878" target="_blank">📅 23:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
منابع شبکه العربیه: طبق توافق، آمریکا تحریم‌ها را کاهش می‌دهد و محاصره را برمی‌دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65877" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65876">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGb7GvrvBLeljILoJoMIVX5ZgNcjbMzqelThM_kN9o_X6DD6HDSHduaFQJMz36A45bHZyu4t5QZcmisBlzl-XwRG_nEU6VuejvAM0nG6-LpGYQjq-2ZQuWO4acyPnR56AawrvozBvPgD6PmPY_JGHIulEX8PaoEle_OTK7z6CZF7cW9FrHvlcSphuomyGnL_MttPAOx8-KqbxheErAUhE0lq-s5O7k5aPh5NvUrrQlU94RKQmEPBYBrtgiOttbt087P8lXQh_tt5oHmQRlvnJVVP89dNX3mkjQ46-Vo4L7TbfWY4uzc9lGNgM9jRvCnZBLQ5BRD1gfLBfTfYTQqk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیرِ واشنگتن
#hjAly‌</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65876" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65875">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=LTOhi77fpamjkarNODk1pK142a1auWQMQGpkKtIWUp-v61I_g8nhT9L-jDQHQOccud7HfZGdDx1Vetiejs4nJrMBEvBQX8aqi4wUhkLU8QKtmvavDgwJrRhEFZqcoPHlaEUhYIiipOz_pQKqyMk2r8WkUXc_dR4iSuG7IkiTSfbs00tU0nJ8PGLV8PtZp9IP-freBC3jcFYPDe8XVLzdjfXwVqD8z3apvDSz5RXwoXAi4v-glbwBlGAy-y9GXg5nUbjYDNPaHMIOzkcu4tX19VmILG9MWue0x7Nj8RcJClFqrOPmYzOs-w8-EyDcThDAD3ZINcEplrjfs5YCHnYCgonc2Kt0mEFqKiLZKaeQe4EnzYPeLIs00vwfHh9qyDJopgmlENmcgHAcOopyzQDXG53owW3mu4KL2RqA9MSKGIVqTy7smVgwD1SvpS1dqL6ByHOg0qJSsQPoN9nujjypk9GdNmYJqoNtCeId8Q_Fp6Dw7NjJN-GRkb9vafVRWKZJBj3BaeqyMbmVCw_prSjUXn73wjgpwD3OsZujoO85BkbuFqa4xYnNlh61eNJBkSHtLmUt78NJ-uwibsv2gnqr62bJpm9kdL5ggqudwZrQCrM3_aDZWLB7ZVu_Ay3RkvePnbJh5nkSecFGqNpaC5rxUWOgdP8yuYGjPm3tQxsQuTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=LTOhi77fpamjkarNODk1pK142a1auWQMQGpkKtIWUp-v61I_g8nhT9L-jDQHQOccud7HfZGdDx1Vetiejs4nJrMBEvBQX8aqi4wUhkLU8QKtmvavDgwJrRhEFZqcoPHlaEUhYIiipOz_pQKqyMk2r8WkUXc_dR4iSuG7IkiTSfbs00tU0nJ8PGLV8PtZp9IP-freBC3jcFYPDe8XVLzdjfXwVqD8z3apvDSz5RXwoXAi4v-glbwBlGAy-y9GXg5nUbjYDNPaHMIOzkcu4tX19VmILG9MWue0x7Nj8RcJClFqrOPmYzOs-w8-EyDcThDAD3ZINcEplrjfs5YCHnYCgonc2Kt0mEFqKiLZKaeQe4EnzYPeLIs00vwfHh9qyDJopgmlENmcgHAcOopyzQDXG53owW3mu4KL2RqA9MSKGIVqTy7smVgwD1SvpS1dqL6ByHOg0qJSsQPoN9nujjypk9GdNmYJqoNtCeId8Q_Fp6Dw7NjJN-GRkb9vafVRWKZJBj3BaeqyMbmVCw_prSjUXn73wjgpwD3OsZujoO85BkbuFqa4xYnNlh61eNJBkSHtLmUt78NJ-uwibsv2gnqr62bJpm9kdL5ggqudwZrQCrM3_aDZWLB7ZVu_Ay3RkvePnbJh5nkSecFGqNpaC5rxUWOgdP8yuYGjPm3tQxsQuTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره جمهوري اسلامي:
ما توافقی داریم که ایران هرگز سلاح هسته‌ای نخواهد داشت، که این کل هدفی بود که باید از آن عبور کنیم تا به این برسیم.
اما ما به زودی امضایی داریم و اسناد تقریباً در شکل نهایی هستند. بنابراین خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65875" target="_blank">📅 23:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65874">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
دونالد ترامپ: در مراسم امضای توافق حضور نخواهم داشت و جی‌دی‌ونس قرار است عازم اروپا شود  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65874" target="_blank">📅 23:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65873">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKeHfSvp1NwA_AxTdqNQulzQAM8AA_XNvGvWwI_Hprc9Ic_m15iT4yOxqSemtLBEpjr3434ntNw5yFsDZCuATYaXlCF4yjLB9H5fm89--5syKu3g_ygSmd90jf5TRSW-g_U7JH7fPDuPxmNx461sQXkXv5otJ1AukcNzVyOREXS6A4Sz7gz7N8XuwjcS8yhlz-goGpC85X4uyxzHMccUNxwevF3P4OVTZMcNWV_Z3MIWeQOF1OcBu2U9k4kW5STk9t81G2YE6blYMCnuZ7mZT0Tad2dg0zwdWDQfLqMaEhNAKaQfT5FVVnflObbajrDeu9EmIwK-DCBog7GbAai__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره داش آخوند های حرومی تسلیم شدند هفته دیگه جشن آزادیه
🤡
🤡
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65873" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65872">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ترامپ: توافق با ایران بزودی در اروپا امضا می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65872" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65871">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ترامپ: توافق با ایران بزودی در اروپا امضا می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65871" target="_blank">📅 23:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
دفتر امیر قطر: تمامی کشورهای منطقه در خصوص تفاهم ایران و آمریکا رضایت دارند
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65870" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqcEq6WhPpYgrKk2KsoebxsaHtckrDLGm1HkgAwdcOJMKfTjgkpmJSevzz2Lw0n7WI-LL7Sw7Q8x94HJnxuWinAfjO7qtAOMNThtBEirt43tCKuT5TKSLWbcL21O9qv6X9v4FK1JCCVb7FlJf72pSyUBEuYVRbX5ERH53RRhLSy8r5WRdPdDnV1EhlXVbYX3UN01zq-q4UxcNYmPcsf1zls017ZKK6GU77qO9rYc6tfl1UCmeeVhPYrbOJBtKukzhpHpTIopf0D51B0XnPL32HtA4yfJWNqw6zPen6KIuHc1bdYYYdvMStTD5iP4jtgCXrCnUL7rcDdaoIvBdJthcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
صد درصد بیمه ویژه مرحله گروهی جام جهانی ۲۰۲۶
🔥
⏩
تا یکشنبه هفتم تیر ماه، روزانه با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های مرحله گروهی جام‌جهانی ۲۰۲۶، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد در هر روز از رقابت‌ها ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCUP1
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
✅
دریافت سرورفیلترشکن اختصاصی
💻
@BetForward</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65869" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
ادعای اکسیوس:
منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65868" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
