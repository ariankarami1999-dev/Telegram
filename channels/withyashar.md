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
<img src="https://cdn4.telesco.pe/file/vW5qaF4FzAEC_Fw2rxqskDyfH-buzcl70EUuCnBuT31Y5g4wPr46P2kRUMfiIqEvJGukFbkLjxrsLUygZFMgAhHKZvm84_LHg5dlHhWFdcfOcIDInkx_DYaHyCo2aFRnnfasowyps7HWjUt-IqroB2N8an1ugv9x7DDgs18O-L6jEOVrbsnJjbOyhkv0BGKwdkLMl_oVFS-xPj8-uPWoWt7ZntDSwttrz8JfTyDnqyABfUyDEnT43cxQnY9KxRi9y2wXZPdfoT3oskot3Ls1Lx8LF8L9qYgDiDBX182zLUwp7XXJSgFOkoVVXZXSk1F-7EQtKH4sPS_vf23a6thl1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 290K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 03:13:42</div>
<hr>

<div class="tg-post" id="msg-13606">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/withyashar/13606" target="_blank">📅 03:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13605">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/withyashar/13605" target="_blank">📅 03:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13604">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb45455c0d.mp4?token=IZbAnW0gJ4QYmr25bjuu7_i_G8lRaIUZ1-fGrwgKKctMWP5sbmeCNw0C5IXUK5CLhWYe99Fi0V26iU--xV3S5Z6S8EfmLsaT4q4OITn5F2HVbt53Oa6W6_r9PDE-NlTcR-Ul9jKyQIEp8aQUtORnbPAAF3E-d23FxqEcdwyrTRLWfkK7wh1Qe_BJ0uEkF8XbQaO_zPmPqD_F_-Tdvd2b6UiE4_5YfwMHt5dnb29Vh1FqtBCoLOQyiyQxuLoujbB4xWGh1eeTx2UMbJJx6fe63rA96Qcs4YLXlaf_mjZ6s12OeD7f0siZpe4dD3c95_T4R5p_Jf8E5c8isTyXplXrGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb45455c0d.mp4?token=IZbAnW0gJ4QYmr25bjuu7_i_G8lRaIUZ1-fGrwgKKctMWP5sbmeCNw0C5IXUK5CLhWYe99Fi0V26iU--xV3S5Z6S8EfmLsaT4q4OITn5F2HVbt53Oa6W6_r9PDE-NlTcR-Ul9jKyQIEp8aQUtORnbPAAF3E-d23FxqEcdwyrTRLWfkK7wh1Qe_BJ0uEkF8XbQaO_zPmPqD_F_-Tdvd2b6UiE4_5YfwMHt5dnb29Vh1FqtBCoLOQyiyQxuLoujbB4xWGh1eeTx2UMbJJx6fe63rA96Qcs4YLXlaf_mjZ6s12OeD7f0siZpe4dD3c95_T4R5p_Jf8E5c8isTyXplXrGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
منتظر زارتان زورتان</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/withyashar/13604" target="_blank">📅 03:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13603">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">۳پا باید یه جوابی بده چیزی‌ دیدن یا شنیدین بگین</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/withyashar/13603" target="_blank">📅 02:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چندین انفجار در سيريك
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/withyashar/13602" target="_blank">📅 02:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال ۱۴: همه امیدوار بودند که آتش بس برقرار شود، اما بازی به طور کامل در حال تغییر است. برای یک آخر هفته فوق العاده گرم در خاورمیانه آماده می شوند، زیرا ایران و آمریکا از اعتصابات تصادفی شبانه به رویارویی های روز روشن تغییر می کنند!
@withyashar</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/withyashar/13601" target="_blank">📅 02:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سنتکام : چند لحظه پیش، نیروهای سنتکام چهار پهپاد تهاجمی یک‌طرفهٔ ایرانی را که به سمت تنگهٔ هرمز پرتاب شده بودند، سرنگون کردند. این پهپادهای تهاجمی تهدیدی فوری برای تردد دریایی منطقه ایجاد کرده بودند. در ادامه، نیروهای آمریکا برای دفاع در برابر حملات بیشتر، سایت‌های رادار مراقبت ساحلی ایران در گورک و جزیرهٔ قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ‌دادن به تجاوز بی‌دلیل ایران در چارچوب دفاع از خود، در حالت آماده‌باش قرار دارند.
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/withyashar/13600" target="_blank">📅 02:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
سنتکام از حمله به سایت های راداری قشم خبر داد!
@withyashar</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/withyashar/13599" target="_blank">📅 02:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13598">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">چندین انفجار در سيريك
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/withyashar/13598" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13597">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سی‌بی‌اس نیوز به نقل از یک مقام آمریکایی: نیروهای آمریکایی حداقل ۴ پهپاد را که توسط ایران به سمت تنگه هرمز پرتاب شده بود، سرنگون کرده‌اند.
🚨
@withyashar
بچه جنگ شده باز</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/withyashar/13597" target="_blank">📅 02:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13596">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚠️
@withyashar
گول نخوری !</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/withyashar/13596" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13595">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فقط در ۴ ماه ! بسوزید عرزشی ها</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/withyashar/13595" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13594">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">💥
290k عرزشی سوز ترین کانال تلگرام</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/withyashar/13594" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13593">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش هایی از قطع شدن اینترنت
@withyashar</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/withyashar/13593" target="_blank">📅 01:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13592">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سی ان ان : منابع می گوید ایران چندین پهپاد را به سمت تنگه هرمز پرتاب کرده است. نیروهای ایالات متحده حداقل 3 تا از آنها را رهگیری کردند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/withyashar/13592" target="_blank">📅 01:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13591">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوتا صدای انفجار الان ومد همین الان قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/13591" target="_blank">📅 01:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13590">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مجری ان‌بی‌سی: رهبران جمهوری اسلامی معتقد نیستن که به‌طور کامل شکست خوردن.
ترامپ: ایران به دلیل تصور برخورداری از قدرت کافی، از امضای توافق خودداری کرده. ایران در نهایت گزینه‌ای جز توافق نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/13590" target="_blank">📅 01:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13589">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به ان بی سی:
خیلی از مقاماتشون مغرورن، یه سری کارها هست که هیچوقت فکر نمی‌کردن مجبور بشن انجام بدن ولی الان مجبور شدن، راه دیگه‌ای ندارن و این قضیه زمان می‌بره.
داریم درباره 47 سال حرف میزنیم که هر کاری خواستن انجام دادن.
@withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/13589" target="_blank">📅 01:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13588">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ به NBC : وضعیت برای اونا واقعاً سخته
یه جورایی استقلال زیادی هم دارن، ولی سال‌ها با یه رهبری ضعیف و بی‌اثر از طرف آمریکا و بعضی کشورهای دیگه طرف بودن؛
طوری که عملاً گذاشتن هر کاری دلشون خواست بکنن.
من فکر می‌کنم خودشون هم الان باورشون نمی‌شه به اینجا رسیدن؛ جایی که عملاً خیلی ضعیف شدن
@withyashar</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/withyashar/13588" target="_blank">📅 01:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13587">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: رهبران ایران چاره ای جز رسیدن به توافق ندارند‌‌
@withyashar</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/withyashar/13587" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13586">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌ @withyashar</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/withyashar/13586" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13585">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌
@withyashar</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/13585" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13584">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به نظر می‌رسد جنگنده‌های اسرائیلی از عراق به سمت ایران می‌آیند
@withyashar</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/13584" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13583">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ارسالی : پدافند ۱۷ شهریور گنبد کاووس فعال شد @withyashar</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/withyashar/13583" target="_blank">📅 01:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13582">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارسالی : پدافند ۱۷ شهریور گنبد کاووس فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/withyashar/13582" target="_blank">📅 01:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13581">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به خبرای هست ولی نمیتونم ثابت کنم</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/13581" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13580">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/13580" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13579">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارشهایی از صدای جنگنده و پدافند در شمال کشور
🚨
@withyashar</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/13579" target="_blank">📅 00:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13578">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: ما خیلی سریع از ایران خارج خواهیم شد و نتیجه آن، به هر شکل، بسیار قوی خواهد بود؛ چه از طریق یک تکه کاغذ (توافق) و چه از راهی بسیار سخت‌تر. شاید حتی راه بسیار سخت‌تر، آسان‌تر هم باشد.
اما ما از این مسئله عبور خواهیم کرد و قیمت کود شیمیایی شما به‌شدت کاهش خواهد یافت، درست همان‌طور که چهار ماه پیش بود. قیمت کود شیمیایی اکنون هم کاهش یافته است.
قیمت انرژی، نفت و گاز نیز همگی به‌طور قابل‌توجهی پایین خواهند آمد. و صادقانه بگویم، من تصور می‌کردم قیمت‌ها بسیار بیشتر از این افزایش پیدا کنند.
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/13578" target="_blank">📅 00:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13577">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش های تایید نشده : چندین جت جنگنده آمریکایی حمله‌ای را به بندرعباس و مناطق اطراف جزیره خارک آغاز کردند و چندین بندر از جمله فرودگاه بندرعباس را هدف قرار دادند. پدافند هوایی فعال شد و درگیر نبرد شدیدی با جت‌های جنگنده شد.
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/13577" target="_blank">📅 00:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13576">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش هایی از شلیک نیروهای ایرانی به سمت ناو های آمریکایی
🚨
@withyashar</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/13576" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13575">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره خارک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/13575" target="_blank">📅 00:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">@withyashar
only for pro members</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/13574" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13573">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">@withyashar
operation economic fury</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/13573" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13572">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/13572" target="_blank">📅 00:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13571">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجار ناشناس در نزدیکی کنسولگری ایران در استان سلیمانیه در شمال عراق.
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/13571" target="_blank">📅 23:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13570">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlMRvtzoF7rVhI9GGwQkcLEV3yuHzJFm4WNdWV_4PE3u0PJ5tVKJCbDIY7jr6j8ARx43PSBnedNLftIuFD6P-SwZKwuAsykPZJrjordISKgukP3bjZdJZCq9Cs7tgZu0IGMG3LWezoYltY5XqUelqtfrDeLO2RtyYVVmCL4qEQ8bxagJhKbuDkOyoRJtxwDqZ9p4dwdJF_Gkfw7tgO8onuNDcO-MZh2Qxfg0LwEK9vHLqzbalrVeU86_xLYLzGmzHmbpDFvIafaIZO2qTGsJAFf_4jalopQ4ulbYG25Iuez6aKli_DnLEV7YwlxOdkHgVcG4kgwhsp7umGVSQ8NCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواستگاری جنجالی قیصر از الهام چرخنده در تجمعات حکومتی
قیصر در یکی از تجمعات حکومتی، به‌صورت علنی از الهام چرخنده، بازیگر سابق تلویزیون ایران، درخواست ازدواج کرد. این اتفاق غیرمنتظره خیلی زود در فضای مجازی و رسانه‌ای مورد توجه قرار گرفت و واکنش‌های زیادی را به دنبال داشت
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13570" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13569">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شبکه ۱۲ اسرائیل به نقل از رئیس ستاد ارتش این رژیم: قصد نداریم از سرزمین‌هایی که در لبنان پیشروی کرده‌ایم، خارج شویم
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/13569" target="_blank">📅 22:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13568">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اکسیوس: استیو ویتکاف و جرد کوشنر به طور مخفیانه از تأسیسات هسته‌ای اوک ریج در تنسی بازدید کردند تا با برترین کارشناسان هسته‌ای آمریکا دیدار کنند، در حالی که مذاکرات با ایران وارد مرحله حساسی شده است. @withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/13568" target="_blank">📅 22:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13567">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اکسیوس: استیو ویتکاف و جرد کوشنر به طور مخفیانه از تأسیسات هسته‌ای اوک ریج در تنسی بازدید کردند تا با برترین کارشناسان هسته‌ای آمریکا دیدار کنند، در حالی که مذاکرات با ایران وارد مرحله حساسی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/13567" target="_blank">📅 22:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13566">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارشگر: بازی که شما می‌روید  ببینید ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند بلیت این رویدادهای ورزشی را بخرند.
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است.
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/13566" target="_blank">📅 21:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13565">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ درباره پوتین و زلنسکی:
بگذارید خودشان حل کنند. من کسی هستم که آن‌ها را به این موقعیت رساندم.
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/13565" target="_blank">📅 21:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13564">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ درباره جان بولتون:
فکر می‌کردم او در زمینه جنگ رادیکال است، نه در زمینه چیزهای دیگر.
او می‌خواست با هر کسی که دهانش را باز می‌کرد وارد جنگ شود.
او همیشه می‌خواست مردم را بکشد. من هرگز به او گوش ندادم.
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13564" target="_blank">📅 21:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13563">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ درباره ایران دم مسترا:
ما در رابطه با ایران موفقیت‌های بزرگی کسب کرده‌ایم.
آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
ترامپ:
پیت هگستث معلوم شد که یک گوهر است.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/13563" target="_blank">📅 21:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682cd2dd57.mp4?token=PqpY3E2IjKmP6zdv-KdItHUsPOgxAbWpx21aFn1wv3kTb6kTGJCbrzsQjZO_3_CMbPGuEmqImD_5wQldoqkOPNJmpMkcnRGJMvlMcg_2hiv3Bxsnvit-EqK4fmInYNOazZIstr9W6nyJpa2_-eKVVBCEugfe5OTEDYm5WWyTRbCDowhj0Zn4V5Jcq0ydIp5--F32cxIbYD1gr0WHi9mh7sJieMTY9YS3XTgD9cv4WG9EkXTmSScW_81yLltJ3Zw_fh3jjQb6moNFy_6R4UgvK-0TYz3_UxSe1o7dJyFIQlyFdGnuaEsnuNGwMP07AjfxC4q6Uypbt8N-cNt2VbYWuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682cd2dd57.mp4?token=PqpY3E2IjKmP6zdv-KdItHUsPOgxAbWpx21aFn1wv3kTb6kTGJCbrzsQjZO_3_CMbPGuEmqImD_5wQldoqkOPNJmpMkcnRGJMvlMcg_2hiv3Bxsnvit-EqK4fmInYNOazZIstr9W6nyJpa2_-eKVVBCEugfe5OTEDYm5WWyTRbCDowhj0Zn4V5Jcq0ydIp5--F32cxIbYD1gr0WHi9mh7sJieMTY9YS3XTgD9cv4WG9EkXTmSScW_81yLltJ3Zw_fh3jjQb6moNFy_6R4UgvK-0TYz3_UxSe1o7dJyFIQlyFdGnuaEsnuNGwMP07AjfxC4q6Uypbt8N-cNt2VbYWuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بیرون کاخ سفید با خبرنگارا حرف نزد، و قبل از سوار شدن به ایر فورس وان هم هیچ مصاحبه‌ای نکرد، ببینیم دم توالت چیزی میگه یا نه
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/13562" target="_blank">📅 21:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جروزالم پست:  منابع اطلاعاتی اسرائیل معاون رئیس‌جمهور جِی‌دی ونس را متهم می‌کنند که نقشه موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً به اردوغان لو داده است، که سپس اردوغان به ترامپ فشار آورد تا آن را لغو کند. خط قرمز اردوغان: هیچ نیروی نظامی کردی…</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/13561" target="_blank">📅 20:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جروزالم پست:  منابع اطلاعاتی اسرائیل معاون رئیس‌جمهور جِی‌دی ونس را متهم می‌کنند که نقشه موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً به اردوغان لو داده است، که سپس اردوغان به ترامپ فشار آورد تا آن را لغو کند.
خط قرمز اردوغان: هیچ نیروی نظامی کردی در نزدیکی مرزهای ترکیه نباشد.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13560" target="_blank">📅 20:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بلومبرگ: طبق داده‌های ناوبری، رفت‌وآمد کشتی‌ها از تنگه هرمز تو ۲۴ ساعت گذشته به‌شدت کم شده
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/13559" target="_blank">📅 20:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13558">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">️حمام خون در بازار کریپتو!  بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است. @withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/13558" target="_blank">📅 19:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آلمان با صدور هشدار امنیتی برای شهروندانش، نسبت به سفر به خاورمیانه هشدار داد و دلیل اون رو احتمال تشدید دوباره تنش‌ها و اختلال در پروازها عنوان کرد.
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/13557" target="_blank">📅 18:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سنتکام:
ادعای نادرست: ایران ادعا میکنه که به سمت کشتی‌های جنگی ایالات متحده در خلیج عمان تیر هشدار شلیک کرده و کشتی‌های آمریکایی رو مجبور به «عقب‌نشینی» به سمت اقیانوس هند کرده.
حقیقت: نیروهای ایرانی به کشتی‌های جنگی نیروی دریایی ایالات متحده حمله نکرده یا به سمت آنها شلیک نکردن. انجام این کار نقض فاحش آتش‌بس خواهد بود. نیروهای آمریکایی همچنان آزادانه در آب‌های منطقه‌ای فعالیت می‌کنند و در عین حال محاصره مداوم علیه ایران رو به طور کامل اجرا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/13556" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gloria2018Remaster(IG @yashar)</div>
  <div class="tg-doc-extra">Umberto Tozzi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13555" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/13555" target="_blank">📅 17:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f252f83e0d.mp4?token=iIiY1AUOy_ooaGFaW1i1t43kGrVo57rJdwaoHxhi5-sAzZ8CvdldFHhYiy0HAv0zGm8NABzYiLrkxYiIOOOv8numebuYghlXj36L1b_S3Zs4VP3gkI8m_vq3bISqiXv1sxjSIUpBnlm0gkLe4Z1PEBDXnvWSXy__8_xgoSeA8jXXC6FWBiosoYcRGGXSW7AaPg7MWISnlaHRTZL6p8hHtXTOkL5kn2P67VkWFPeqy-vgWXUYwcpVzn7IbBVvaFQ4zodOye7BzZPphvC2Y_WYIN0_-ss03oUHOT5GWYdk4v1RCwL1JotB7XkMPcM2AkXMvURdFVyP1WjorZywA2RQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f252f83e0d.mp4?token=iIiY1AUOy_ooaGFaW1i1t43kGrVo57rJdwaoHxhi5-sAzZ8CvdldFHhYiy0HAv0zGm8NABzYiLrkxYiIOOOv8numebuYghlXj36L1b_S3Zs4VP3gkI8m_vq3bISqiXv1sxjSIUpBnlm0gkLe4Z1PEBDXnvWSXy__8_xgoSeA8jXXC6FWBiosoYcRGGXSW7AaPg7MWISnlaHRTZL6p8hHtXTOkL5kn2P67VkWFPeqy-vgWXUYwcpVzn7IbBVvaFQ4zodOye7BzZPphvC2Y_WYIN0_-ss03oUHOT5GWYdk4v1RCwL1JotB7XkMPcM2AkXMvURdFVyP1WjorZywA2RQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ویدئویی جدیدی در شبکه تروث منتشر کرد که در حال بازی گلف است و یک ضربه فوق‌العاده میزند. همچنین از آهنگ معروف گلوريا لذت میبرد.
یاشار: آخرین باری که این آهنگ ویرال شد در فیلم گرگ وال استریت بود. مضمون این آهنگ این است که
کنترل نکردن زندگی احساسی می‌تواند خطرناک باشد
توجه زیاد دیگران همیشه خوشبختی نمی‌آورد
باید قبل از اینکه دیر شود، آرام‌تر شد و به خود رسید
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/13554" target="_blank">📅 16:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13553">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رئیس‌جمهور لبنان، ژوزف عون، در مصاحبه‌ای با سی‌ان‌ان ایران را متهم کرد که در رویارویی با آمریکا و اسرائیل از کشور او به‌عنوان یک برگ چانه‌زنی استفاده می‌کند و گفت: «این کشور، کشور شما نیست.»
عون همچنین افزود که مردم لبنان از جنگ میان اسرائیل و حزب‌الله خسته شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/13553" target="_blank">📅 16:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13552">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ماجرای پرواز جنگنده‌ها در ارتفاع پایین بر فراز اصفهان چه بود؟
دقایقی قبل پرواز چند فروند جنگنده در ارتفاع نسبتاً پایین بر فراز برخی مناطق شهر اصفهان مشاهده شد که صدای آن نیز توسط شهروندان شنیده شد.
این جنگنده‌ها متعلق به نیروهای مسلح کشورمان بوده و پرواز آنها در چارچوب مأموریت‌های عملیاتی یا تمرینی انجام شده است و جای نگرانی برای شهروندان وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/13552" target="_blank">📅 16:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13551">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130435eef7.mp4?token=ktU8NiTK6-qwCYQV1_gLyEig4ziFy5Dj7FFnyOGTCu-Pm1hxYhaEnaLDxaeVEeTKbKsA_jT7kqMF7rePjpjBemIhhrlkL9OEJQQ2tznMX-MA7zgU-0qiHEQFk56TxIDE4NR-5MGtSnNZu6AF13IwxwN9V83wEXMYytqXkF5Qtkgry76PVqPGbJTPBqlXVVbDngMIyK8fX9D1FxL4h3x8QMpyWZXEqtsTcd_A-fcnIyElAg7QA9DEVeuUT6BCokXr9BUn3Qpy2LL8idGDPB3XNYCme3O35c9sNMFON2aR6gymmo-beR92ObObSFt444FfAz-rg7TR6MCwcIcfoxTIgIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130435eef7.mp4?token=ktU8NiTK6-qwCYQV1_gLyEig4ziFy5Dj7FFnyOGTCu-Pm1hxYhaEnaLDxaeVEeTKbKsA_jT7kqMF7rePjpjBemIhhrlkL9OEJQQ2tznMX-MA7zgU-0qiHEQFk56TxIDE4NR-5MGtSnNZu6AF13IwxwN9V83wEXMYytqXkF5Qtkgry76PVqPGbJTPBqlXVVbDngMIyK8fX9D1FxL4h3x8QMpyWZXEqtsTcd_A-fcnIyElAg7QA9DEVeuUT6BCokXr9BUn3Qpy2LL8idGDPB3XNYCme3O35c9sNMFON2aR6gymmo-beR92ObObSFt444FfAz-rg7TR6MCwcIcfoxTIgIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/13551" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c96db917.mp4?token=gI3N8MG9ADkpb06uN1b4yhIazdO79M4dpQ_E41Xnserx5-MgHVcuUMrdaFWM1zJxfKlsR46MnT2O3g9DGkUGpu9KeBlHO_FUxaWwRLPRnCzciOmgh2yrgcYUNnwTVD3QXdVrwLEgu54I7flYPOSPseV2nH5Sfv2VlYNE-RqhH7EWRsFGMB_uHHAj6DcM21NwNyJIP6j3CHxDi--i-QQnso4H2TO7qU9ZaSnKSjLnFRazaKL60SAHYHmEW_Q0pvOHpkWO_mtJKbHoewEvJ9J6qtE7Bl5_C8bSzePo9XFRE25Z1uyX-C8M6ls02aUZvQyDD_LuOIEHKv8WiVhvrqjHtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c96db917.mp4?token=gI3N8MG9ADkpb06uN1b4yhIazdO79M4dpQ_E41Xnserx5-MgHVcuUMrdaFWM1zJxfKlsR46MnT2O3g9DGkUGpu9KeBlHO_FUxaWwRLPRnCzciOmgh2yrgcYUNnwTVD3QXdVrwLEgu54I7flYPOSPseV2nH5Sfv2VlYNE-RqhH7EWRsFGMB_uHHAj6DcM21NwNyJIP6j3CHxDi--i-QQnso4H2TO7qU9ZaSnKSjLnFRazaKL60SAHYHmEW_Q0pvOHpkWO_mtJKbHoewEvJ9J6qtE7Bl5_C8bSzePo9XFRE25Z1uyX-C8M6ls02aUZvQyDD_LuOIEHKv8WiVhvrqjHtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ایران اعلام کرد که به دو ناوشکن آمریکایی (DDG-103 و DDG-87) در دریای عمان شلیک هشدار انجام داده است  موشک‌های قادر و پهپادهای شهید دانایی.
هر دو ناوشکن به سمت اقیانوس هند عقب‌نشینی کردند.
ایران همچنین ادعا می‌کند که ناو حمله آبی-خاکی یو‌اس‌اس تریپولی مجبور به ترک منطقه شده است.
هشدار نیروی دریایی ایران: اگر کشتی‌های آمریکایی بازگردند، از موشک‌های برد بلندتری استفاده خواهد شد.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13550" target="_blank">📅 15:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13549">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmWHIvxBSbvOQH0dP6QIEFtdN0WgMaOY1cZUsDSggvhO9NJ4GMivu5En4sqNG9lPPbWA7uLTEEZWUg2iSYB6YK1eyzf61M9VGkrKlQ-piZN97_wbq65AbvyttEKQF5TIT2diOIaxvNYOXLrFccXoj0GYgtK4noehRPjGFcLb6rB1IDElW6vqbYmn7R5sUXs46ndxLdQijU5tT982ROmX68tQsRgu55UAKjHchrlvLzvUCrHIJG04TJuY3fgHTeoO-QYIX4FGPo3wolq5-n2KvLLLTwFTvBXRvqvLPYVqexLvnwUHVw6HIHnDSHNb6_H1wse1yvq9ixBeeZAx94icsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️حمام خون در بازار کریپتو!
بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/13549" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13548">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb4336455.mp4?token=uonIwMOzWIj4XFvvlNmkp8KflBTUW22HeJi4KsSs2bH2DwFQ8iIFGmAxg-9S6E1Vi-q0ECVLlnhnJ5s8UhVNYg58GGRqinPIx44ndgUBQjRoerAPej2qaS1qE3XpnCbriSg6uw7ESrNPW_IaHOgO-eqkkZZ9ZshmnLzdNgDzjrFwUFdzBF9-9tfVHxR1pTihHdpGT6Q8vh6ykEkVs_XBxfDYwwXjrwzwxwEiOVJpJ2z1mxMClFUfo09mukWzmrwshBuhP7JTrgNmqjUEKWkj16AtegnC6_ScgG9WLI3B8sHtxi7_9HjDInla5TB3laM-yrK2dYeLeYWFCa1XI8WmlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb4336455.mp4?token=uonIwMOzWIj4XFvvlNmkp8KflBTUW22HeJi4KsSs2bH2DwFQ8iIFGmAxg-9S6E1Vi-q0ECVLlnhnJ5s8UhVNYg58GGRqinPIx44ndgUBQjRoerAPej2qaS1qE3XpnCbriSg6uw7ESrNPW_IaHOgO-eqkkZZ9ZshmnLzdNgDzjrFwUFdzBF9-9tfVHxR1pTihHdpGT6Q8vh6ykEkVs_XBxfDYwwXjrwzwxwEiOVJpJ2z1mxMClFUfo09mukWzmrwshBuhP7JTrgNmqjUEKWkj16AtegnC6_ScgG9WLI3B8sHtxi7_9HjDInla5TB3laM-yrK2dYeLeYWFCa1XI8WmlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستون دود حجیم جنوب مركزي تهرانه  همين الان
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/13548" target="_blank">📅 15:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13547">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بر اساس نظرسنجی‌های معتبر آمریکایی حمایت افکار عمومی آمریکا از پایان جنگ و حرکت به‌سوی توافق، از ۴۹٪ پیش از جنگ به ۶۸٪ در آستانه توافق رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/13547" target="_blank">📅 15:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه. @withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/13546" target="_blank">📅 15:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13545">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فیفا: نقص سایت باعث صدور بلیت‌های رایگان شد
‏فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/13545" target="_blank">📅 14:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13544">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/13544" target="_blank">📅 13:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13543">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرده
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/13543" target="_blank">📅 12:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13542">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سازمان ملل از حزب‌الله خواست به تصمیمات حاکمیتی دولت مرکزی بیروت پایبند باشد، به حاکمیت کشور احترام بگذارد و روند انحصار سلاح در دست دولت را بپذیرد و از اسرائیل نیز متقابلاً خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت این کشور احترام بگذارد.
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/13542" target="_blank">📅 10:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13541">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=gBQCSJ1MlsKyUm9Fmt_xt1cqwLgxJ7HjdloJeRC5nXwPpCamKh46hA7jJ40k9B5J4YdlQRDaB6il_LDf6DA2P5geWkHLJp_0RgRD0jEZhj99mh6NFAyRuvTicc8O-eeef8k0wKdjOAtq0bEdYADlfx4o2xOFfI2Yzdsrbtb6G7Ye9LQh4T9ojDeM7ep48wpPM6iMrXU8OdUGkGrrtJwYBuXhAFwURa4RoPSmp6W0mngf4_HWgKcdFxaSCGaRNWVA5H3g7ZrADlVT9gpcHaun1lY2QW-sEuC-L71SEDKGQiI-H58FV5rnt5Tqd_vG7AxcQ4C-wB4tTHivQsHKY_b1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=gBQCSJ1MlsKyUm9Fmt_xt1cqwLgxJ7HjdloJeRC5nXwPpCamKh46hA7jJ40k9B5J4YdlQRDaB6il_LDf6DA2P5geWkHLJp_0RgRD0jEZhj99mh6NFAyRuvTicc8O-eeef8k0wKdjOAtq0bEdYADlfx4o2xOFfI2Yzdsrbtb6G7Ye9LQh4T9ojDeM7ep48wpPM6iMrXU8OdUGkGrrtJwYBuXhAFwURa4RoPSmp6W0mngf4_HWgKcdFxaSCGaRNWVA5H3g7ZrADlVT9gpcHaun1lY2QW-sEuC-L71SEDKGQiI-H58FV5rnt5Tqd_vG7AxcQ4C-wB4tTHivQsHKY_b1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اصابت یک پهپاد به تاسیسات بندر الفحل عمان که موجب توقف بارگیری نفت در این بندر شده است
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/13541" target="_blank">📅 10:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13540">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یدیعوت آحارونوت: کابینه امنیتی اسرائیل شب گذشته به قطعنامه آتش بس در لبنان رای نداد
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/13540" target="_blank">📅 09:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13539">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">طبق روال هر روز صبح حمله سنگین اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/13539" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13538">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL00r_x6xF_ubztutT7lNj5gMEknldpN9ykUQzd0dFmpAOJ7haN-FZqcXY-uFBJLrhJXwC59CLxGNrxu3At6R4qmXoh_tsfPbxKC01pFEOdW2uYwLdVJlTNRhEGVSiuYVb9xi6Qvd_aBXic7GBTtMmFd85PtLk0kkZDUruS3QODRMcmT47Gi7nVWiWMu8RhWwTNXiI2dOA3BTzz_AvQE56GfSF1fmy7un58bltKrb0vNpinHF2lXk01mWBT-I2Az0gK_y1_8H6Y-CeEvxcXjbcowNxTydVzx4uEBpbYq45L7IAqT5zguZ7r8QzZRvpaVS-_-sOps7KAolj7TPbcJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشهای زیادی برایم فرستادید که از پدافند سنگین ۳-۴ صبح و چندین انفجار در تهران ولی مدرکی نیست… فقط چندین عکس از اینجا برایم آمده.
آزاد راه پردیس به تهران
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/13538" target="_blank">📅 09:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امشب بیداریم ، ردبولم میزنیم
🤣
💥</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/13537" target="_blank">📅 09:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رویترز: بامداد جمعه انفجاری پهپادی در بندر الفحل عمان رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/13536" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نورالدین الدغیر خبرنگار الجزیره در تهران:یادداشت تفاهم در مرحله نهایی خود قرار دارد
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/13535" target="_blank">📅 08:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fcaccf1cd.mp4?token=b23RU9Quw9kKqNrzxLbl70MQ7MO8ovYAM6ZbqANLKsUPuLdWruAGbUayKlaJhiRCjlyRNB6tmoTdBo1c9qQ5hKXjdlFaL4aG1Pd75RW9QeJqmT_nVvkueXsOEI9LpsiMScb_yAQg6Glbrs-oKjis34zbaV7yL52Aushz4im3zNkJTkvplvmUMUPY_D03_BOdwX-3i9bEUfkGol9gFRKNg21cWJWiiweC78I9LAhr-904T5CntAvJAPA-_PRY-MEAJZFhfNixZshKsS0HlCPJTHAwEMZbMrZc6Hur3qbtM9_MttQk9m5733WxKbIXPSoDMNzRgDOMCT_Jxvcl01ih4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fcaccf1cd.mp4?token=b23RU9Quw9kKqNrzxLbl70MQ7MO8ovYAM6ZbqANLKsUPuLdWruAGbUayKlaJhiRCjlyRNB6tmoTdBo1c9qQ5hKXjdlFaL4aG1Pd75RW9QeJqmT_nVvkueXsOEI9LpsiMScb_yAQg6Glbrs-oKjis34zbaV7yL52Aushz4im3zNkJTkvplvmUMUPY_D03_BOdwX-3i9bEUfkGol9gFRKNg21cWJWiiweC78I9LAhr-904T5CntAvJAPA-_PRY-MEAJZFhfNixZshKsS0HlCPJTHAwEMZbMrZc6Hur3qbtM9_MttQk9m5733WxKbIXPSoDMNzRgDOMCT_Jxvcl01ih4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر اختصاصی جدید CNN خسارت ناشی از آتش‌سوزی در ناو هواپیمابر USS Gerald R. Ford (CVN-78) را نشان می‌دهد؛ آتش‌سوزی‌ای که در بخش لباسشویی کشتی رخ داده و در زمان استقرار آن در دریای سرخ و در چارچوب عملیات آمریکا علیه ایران گزارش شده است.
این حادثه در ماه مارس حین جنگ با ایران  رخ داد و نیروی دریایی آمریکا فوری اعلام کردن آتش «مهار شده»، دو ملوان با جراحات غیرمرگبار درمان شده‌اند و ناو همچنان «کاملاً عملیاتی» است.
اما ویدیوی جدید CNN نشان می‌دهد خسارت بسیار شدیدتر از گزارش اولیه بوده است و منابع به CNN گفته‌اند سامانه اطفای حریق ناو از کار افتاده بود.
یکی از ملوانان گفته است خدمه حدود ۳۰ ساعت به‌صورت دستی با آتش مقابله کرده‌اند و حتی نگرانی درباره احتمال از دست رفتن ناو وجود داشته است.
مقامات تأیید کرده‌اند این آتش‌سوزی به‌طور موقت عملیات را مختل کرده، پرواز جنگنده‌ها را دو روز به تأخیر انداخته و باعث شده ناو برای تعمیرات اضطراری در یونان پهلو بگیرد
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/13534" target="_blank">📅 01:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ می‌گوید دولتش بررسی کرده بود که نیروهایی را برای تصرف اورانیوم ایران بفرستد، اما در نهایت این ایده را رد کرد چون خیلی پرخطر بود و می‌توانست به تلفات آمریکایی‌ها منجر شود، و این موضوع را با مأموریت ناموفق نجات گروگان‌های کارتر مقایسه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/13533" target="_blank">📅 01:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ ۲۵ بهمن ۱۴۰۴: میخوام با آیت الله علی خامنه ای دیدار کنم.
۹ اسفند بخارش‌ کرد.
ترامپ ۱۴ خرداد ۱۴۰۵: میخوام با آیت الله مجتبی خامنه ای دیدار کنم.
چه تاریخی بخار میشه؟!
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/13532" target="_blank">📅 00:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13531">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: ما به ایران رسیدگی خواهیم کرد، و به‌محض اینکه کارمان با آن تمام شد، در مسیر بازگشت، برای مدت کوتاهی توقف می‌کنیم و به کوبا رسیدگی خواهیم کرد… باید از شر این نظام خلاص شویم
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/13531" target="_blank">📅 00:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13530">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: برنده این جنگ ما هستیم حالا چه روی کاغذ چه با قدرت نظامی
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/13530" target="_blank">📅 00:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13529">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: جابجایی مواد هسته‌ای ایران مستلزم حضور یک یا دو هفته‌ای در منطقه درگیری بود، بنابراین ما این کار را انجام ندادیم
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/13529" target="_blank">📅 00:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13528">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ : من دنبال عملیات مخفی برای گرفتن اورانیوم ایران نیستم اون اورانیوم عملاً دفن شده و از بین رفته
اعزام نیروهای نظامی برای تصاحب ذخایر اورانیوم ایران؟ نه من نمی‌خوام جیمی کارتر باشم
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/13528" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13527">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ:
راستش نمی‌خوام با آیت‌الله دیدار کنم، ولی اگه ببینمش، برام افتخاره. با احترام هم باهاش رفتار می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/13527" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13526">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSiamak</strong></div>
<div class="tg-text">عمو یاشار اتاق جنگ نمیری امشب؟</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/13526" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13525">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ:
من در امور امنیت ملی خیلی تجربه زیادی نداشتم، اما فکر می‌کنم واقعاً کار خیلی خوبی در این زمینه انجام داده‌ام.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/13525" target="_blank">📅 23:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">منابع عربی:ظاهرا چراغ سبز برای بمباران حومه شهر بیروت گرفته شده است
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/13524" target="_blank">📅 23:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح هم اینا برن، طول می‌کشه. این زندگی واقعی هست و رؤیا و خیال‌بافی و وعده‌وعید نیست! حتی مانوک هم گفت بعد از مذاکرات تازه بازی شروع میشه، پس ما اولش هم نیستیم.
ولی با من این مسیر رو راحت‌تر از تمام حالات طی می‌کنید
❤️‍🩹
🙌🏾
ما بقی بازی سیاست و خبرگزاری‌ها و مارکت هست که ما هم به ناچار توشیم و انتشار می‌دیم! ولی این اخبار به هیچ وجه نه حرفه منه، نه کلاً تأیید می‌کنم؛ چاره‌ای هم نیست، این مسیر باید طی بشه!
از توجه شما به این مطلب ممنونم.
دوستدار شما یاشار</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/13523" target="_blank">📅 23:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فقط‌منننن خیلی‌رک میگم عمو ترامپ ۴۰ تا ملغ میزنه اخرم نمیگه
😁</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13522" target="_blank">📅 23:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد @withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13521" target="_blank">📅 23:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13520">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4113f62c.mp4?token=M-zz2oicuLuq6Ax__aLTidRnncTf4D7cmWyh4XnXRTezDpmPNDIbs9t4FdYMWHN5KSQUZ66xS_xcLgCnm1hibe4sjoltTush-ZDhBO_LaOTHieKaFAqTquQ3hoYBP0wx-oCuGVrbQ0kXkykK_KSDdAUbIJiCp4xHRGuMDNP7GbtaXGaTMR_qEitPFvGVjr8gzb7vdhHEPQAtHlJR6sb3iUf8SIKqSy3C9s4uAiZgNWVMh8PW3q34RgkC__Ys-sEQewooHTpFi80N5RDVdHGcsg0Gq4UXch7IlYHcLE1ShnJrx_BW59pSqEUGzizvsJMXoujt95Lre0jsKA_TsDEfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4113f62c.mp4?token=M-zz2oicuLuq6Ax__aLTidRnncTf4D7cmWyh4XnXRTezDpmPNDIbs9t4FdYMWHN5KSQUZ66xS_xcLgCnm1hibe4sjoltTush-ZDhBO_LaOTHieKaFAqTquQ3hoYBP0wx-oCuGVrbQ0kXkykK_KSDdAUbIJiCp4xHRGuMDNP7GbtaXGaTMR_qEitPFvGVjr8gzb7vdhHEPQAtHlJR6sb3iUf8SIKqSy3C9s4uAiZgNWVMh8PW3q34RgkC__Ys-sEQewooHTpFi80N5RDVdHGcsg0Gq4UXch7IlYHcLE1ShnJrx_BW59pSqEUGzizvsJMXoujt95Lre0jsKA_TsDEfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/13520" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13519">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ببخشید درود و ادب خسته نباشی</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/13519" target="_blank">📅 23:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13518">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM H</strong></div>
<div class="tg-text">ببخشید درود و ادب خسته نباشی</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/13518" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13517">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM H</strong></div>
<div class="tg-text">پدافند سمت وزارت کشور فعال شد الان</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/13517" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13516">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">منظورشان 3روز دیگست یا 10 روز</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13516" target="_blank">📅 23:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13515">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAMIR</strong></div>
<div class="tg-text">منظورشان 3روز دیگست یا 10 روز</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13515" target="_blank">📅 23:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13514">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کانال 12 اسرائیل:
مذاکرات به نتیجه نرسید، آمریکا تا آخر هفته پاسخ میخواهد و با ایران اعلام کرده یا توافق می‌کند و یا درگیری از سر گرفته می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/13514" target="_blank">📅 22:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13513">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Co00_nQd-_AvylYilrt7OecWsNvmt7MIlTofZg2EySY-I04AoV9suTe8D5Ss9ay3yq2yqdew1e-D-GLIPBr-UpZ9FsTatSJrtFGmf25-ZhdNyrKaRGei2pmvrg7QE7nHMl0ZSrj354LqOi1PmQq23xcZ89-Qqkwtq75yXktm0FwGjBGspxOBYbBHMP940yRPZLVr8SSrDX0jkjnSeJuzyqT_mDfUYfCw1gaNiKx9gp4RgHebn9tjBC4fDbtZJozPXtiW8vNR2op4A9B4lOgknodrjXajZpgS41YV-Mn3e4Jg2S6s749jGpSLBkXi650bG3UyYlTC8hJ0B2QgQ6rCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده هشدار امنیتی برای تمام کشورهای خاورمیانه صادر کرد
دلیل این هشدار محتمل بودن درگیری اعلام شده و از همه شهروندان آمریکایی خواسته شده که نزدیک‌ترین پناهگاه را پیدا کنند
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/13513" target="_blank">📅 22:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13512">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaWBbbwl7QK5CRRw5_jTYJvQdJ5kilVaXmVGzd4VDX58aB6UaUdgtlViPW1jPfWHlq-G9ZPcOJkdrpuQXYXz89uFQ9POJCFP6lFu0sxDg_VA1veTy45yLvGGGSOU7hLMDSQiUwO-Gl-6rJeouHakiypniH_1VhrDClApi679ywK4mht8qUMI6wnI0_v4em4ImnZ_U7SF4JpAvPHJajnVfXYQPFkbWWJDqj4dzUgyjqKOIkPNDnOmGrGqtYJarDu1DBgXzAIGFRnJRPvglH5r1blorupq7yF2iDL-xKrWSgBKfGoIQeB5IXTnFXj962YGbOxCj2russpEK1IbjEbHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرشکیان و دخترش کشمش
🥴
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/13512" target="_blank">📅 22:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13511">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عراقچی: ایران و عمان مدیریت تنگهٔ هرمز را براساس معیارهای حقوق بین‌الملل تنظیم خواهند کرد
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/13511" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13510">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سفارت ایالات متحده در اورشلیم هشدار عدم سفر جدیدی برای اسرائیل منتشر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/13510" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13509">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سی‌ان‌ان: ایران می‌گوید در تنگه هرمز هزینه خدمات دریافت خواهد کرد، نه عوارض
ایران می‌گوید به دنبال دریافت هزینه خدمات برای کشتی‌هایی است که از تنگه هرمز عبور می‌کنند، در ازای تضمین امنیت کشتی‌ها، به جای عوارض ترانزیت.
این کشور به دنبال جبران خسارت برای خدماتی است که در کنار عمان انجام می‌دهد، از جمله کمک‌های ناوبری، جست‌وجو و نجات، خدمات امنیتی و ایمنی و خدمات پاکسازی محیط زیست در صورت آلودگی.
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/13509" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13508">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ادعای رویترز بر اساس داده‌های حمل و نقل: صادرات نفت ایران به پایین‌ترین سطح خود در حداقل ۶ سال گذشته رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13508" target="_blank">📅 21:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13507">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۲ اسرائیل: واشنگتن به تهران گفته مراسم امضای توافق با آنها در سوئیس برگزار خواهد شد!
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/13507" target="_blank">📅 21:13 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
