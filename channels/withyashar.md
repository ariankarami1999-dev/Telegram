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
<img src="https://cdn4.telesco.pe/file/ibnf0F9-tf6r2wrUf8JY-Sr5svkjz_sBvxtmdvzkiEQ60wtDTR9u6zqMHOIx_CuPmvZmFNUkBM-IJF4MuSc_TXpNIylZ4WXVQtR7wGJIvTFXrcclxDGLKwjqKpFeQq0ANz0CSR_99UUCysWvTJCJ54zoAbERpwM3NqUuM1FXQmsvKre0OLmXw7yvyaepOv0vht88u3VzddDQ6bfR_Zrw5ywuc3paHMPdrhStciXsYFnGx0bIK706qsP2BekQKI-AEeH323FT6punZ9IOPRYMnesySnv2HQYe2xuXWm0IoE_QPXqjFNg0_vnzPDi_UQAZcaAcVHzxcmXUN19Evyp9kw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 329K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 00:14:42</div>
<hr>

<div class="tg-post" id="msg-14889">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ در تروث : ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او مثل کمتر کسی این موضوع را درک می‌کند. ویکتوریا، متشکرم. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز خیلی زود برای تجارت باز خواهد شد!!! رئیس جمهور دی‌جی‌تی
@withyashar</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/withyashar/14889" target="_blank">📅 00:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14888">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال ۱۲ اسرائیل: دقایقی پیش ترامپ و نتانیاهو گفت‌وگو کردن. ترامپ، نتانیاهو رو در جریان پیشرفت‌ها برای امضای توافق با جمهوری اسلامی قرار داد؛ توافقی که ممکنه حتی از امشب امضا بشه.
@withyashar</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/withyashar/14888" target="_blank">📅 00:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14887">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک‌تایمز: قطر در تلاشه تا اختلافات باقی مونده میان آمریکا و جمهوری اسلامی رو حل کنه تا همین امشب توافق امضا بشه.
@withyashar</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/withyashar/14887" target="_blank">📅 00:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14886">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuwmwKFCVMNtFZdGrJmk1UQ76IneR1QkCAq7Y7l3B9XkJqExa1Fq03DGzop63oqFQY6I7943T0CABeihAKODcUhsU-0qMtVjJ9tQTpnFGa7_ySV9xoN98QLM3kbEPoSVu6BtkzXYg8eMUQaECn3T0BmmdFpPvE-rXocMq6KGsbgljxd8xIw_8RUi8yTER43bC3Sd6MBntBLnLLrJ2qzleahQgVYEZfzJ65fyyIZyl9ZIcQRI6LS2qB4ruxlFhF5j8hQ_TKZY6Fg5eG-UJVQSSy8Feu3IxjU39LzZ3GhjanTmoDYSpf_zMjxFnNHSS7GAOZs2VL84iXJc6rq0Emu_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : جک رید، سناتور رود آیلند، گفته توافقی که الان بستیم از توافق زمان اوباما هم بدتره
به نظر من یا داره عمداً دروغ میگه یا اصلاً نمی‌فهمه موضوع چیه
توافق اوباما عملاً راه رو برای رسیدن ایران به سلاح هسته‌ای باز می‌کرد و کلی پول هم بهشون می‌رسوند؛
یکی از بدترین و احمقانه‌ترین توافق‌هایی که آمریکا تا حالا بسته بود
اما توافقی که ما الان انجام دادیم دقیقاً برعکسه؛ مثل یه دیوار محکم جلوی هرگونه دسترسی ایران به سلاح هسته‌ای رو می‌گیره
مقایسه کردن این دو تا اصلاً منطقی نیست. جک رید باید پاسخگو باشه
@withyashar</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/withyashar/14886" target="_blank">📅 00:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14885">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/withyashar/14885" target="_blank">📅 23:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14884">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏سناتور لیندسی گراهام به انتقاد از ترامپ‌برای سرزنش بی‌بی:
«آمریکا در شرایط مشابه چه می‌کرد؟»
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/14884" target="_blank">📅 23:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14883">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کارشناس شبکه افق:   امام شهید ما چونش را برای اورانیوم گذاشت ولی امروز مسئولین جلسه می‌گذارند و می‌گویند اورانیوم به درد نمی‌خورد/ کسانی که امروز به ترامپ امتیاز می‌دهند بدانند که حتی آن‌ها را هم ممکن است آمریکا ترور کند @withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/14883" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14882">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کارشناس شبکه افق:
امام شهید ما چونش را برای اورانیوم گذاشت ولی امروز مسئولین جلسه می‌گذارند و می‌گویند اورانیوم به درد نمی‌خورد/ کسانی که امروز به ترامپ امتیاز می‌دهند بدانند که حتی آن‌ها را هم ممکن است آمریکا ترور کند
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/14882" target="_blank">📅 23:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14881">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q87h9trelWbs8HwI1AxW9pcHiP8Y-C7pTY2lgNvQsZ8yAzTuBEEknr3wmzQ7H7xIkSQaBD1sGPNxqFVt_svYVH6NBHSUOc9DvsidPzfg5P_8-v4wcH9ahEZEBYWKpgj4k7VNs6SD4_BpssDxX0E9f78tbfla-CRlX73MZkZhKbelwU_2oJmsDTOrjpBf2soj_ao5SCaJkH32btXbf5QkSFm-A_mYuPIKjtrRxzg7YIKTxOQgXkyLGv8wYqQWofnadtZ0Ho4AvJBJcGfzcyaWU77Za_MPUOKLTaruu-PyVKviKppw9p7TK2DewUsqVXvocIBqPWw79vwEe1rBvOVPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: فرمان صادر شد؛ لانچرها آماده پرتاب میشوند
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/14881" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14880">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تیم جمهوری اسلامی با ویزا ساعتی عازم لس آنجلس شد برای بازی با نیوزلند
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/14880" target="_blank">📅 23:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14879">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وای نت: ممکن است ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایرانی به اسرائیل جلوگیری کند
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/14879" target="_blank">📅 23:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14878">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07020c75c7.mp4?token=NeyYFpfV0xcNQVedXPhnBUjTww7A3m0VRmcdjCTYJ6sNUwARx3d3jBpG982QDTn3ttSX8zHazQRmgxhkIWVE-wUyrV-Q_1dw7TKmxJ-PkUbp0A3IFj1HhOq1k6959lbfno6X6R2CasivtqJthexI56QYwBP3Vkw0PqgAx2UPs3fkrX9DwBNdFF2-vEP2_qI23GAkyDyxfKPYUbtg6iuJEfdHpsFDVDCKw-z6gOXfhuJ1_OvI5LE9qWhiWb12AQYCAXaznhrV-WcAlt8QoLt2fHHxTl4kMnAXcHUxeMkkVItqaxaiJWupC60pQOVB2MoEZgCmbHMjdp-4_2F2p6f5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07020c75c7.mp4?token=NeyYFpfV0xcNQVedXPhnBUjTww7A3m0VRmcdjCTYJ6sNUwARx3d3jBpG982QDTn3ttSX8zHazQRmgxhkIWVE-wUyrV-Q_1dw7TKmxJ-PkUbp0A3IFj1HhOq1k6959lbfno6X6R2CasivtqJthexI56QYwBP3Vkw0PqgAx2UPs3fkrX9DwBNdFF2-vEP2_qI23GAkyDyxfKPYUbtg6iuJEfdHpsFDVDCKw-z6gOXfhuJ1_OvI5LE9qWhiWb12AQYCAXaznhrV-WcAlt8QoLt2fHHxTl4kMnAXcHUxeMkkVItqaxaiJWupC60pQOVB2MoEZgCmbHMjdp-4_2F2p6f5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما:
امشب اسرائیل به شدت بمباران خواهدشد.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/14878" target="_blank">📅 23:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14877">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">راشن تودی: ورود اضطراری «جی دی ونس» به کاخ سفید همزمان با اوج‌گیری تنش‌ها در منطقه!
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/14877" target="_blank">📅 23:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14876">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کابینه اسرائیل: اگر ایران حمله کند، ما نیز حمله خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/14876" target="_blank">📅 23:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14875">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارشهایی از شما مبنی بر مشاهده موشک در آسمان
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/14875" target="_blank">📅 23:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14874">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اسرائیل بی‌اعتنا به ترامپ عملیات خود در  لبنان را ادامه می‌دهد ، سه انفجار مهیب در شهرک الطیری در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/14874" target="_blank">📅 23:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14873">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ادعای رسانه‌های عبری:
تحرکات موشکی سپاه پاسداران در یزد، شیراز و اصفهان درحال مشاهده است
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/14873" target="_blank">📅 22:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14872">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e1cd002a5.mp4?token=vwI4p_TMemc_3M_m_BDHI96mKLvyd8ECQ24VrsTOTN77MCuqr5a1Ne7cxEHPF37TpbBHgWAA-XJbEH_GqUGPPEz-5wqDjlH4lwX9-a2qoZFnl2m8im3ANUjvFkUZNhbyGWVCvii_xsZz9UqzsXCxMED3efOcpeUOlrGvMedb17Br6g9dccmPjDJ71yK2glKw0JWO6AuryxrxC_7gGyzoRtgszJgAI587FV0umNkQItkdyT72cHN5WobacLw-R0JsLHhWyJIfgpumq4pphE0Ht844jetwce58oAawQ_jXf9bmg9uucho_oYLBAKJzbnoNa7OYg6NEQxsHvZPVRjcjKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e1cd002a5.mp4?token=vwI4p_TMemc_3M_m_BDHI96mKLvyd8ECQ24VrsTOTN77MCuqr5a1Ne7cxEHPF37TpbBHgWAA-XJbEH_GqUGPPEz-5wqDjlH4lwX9-a2qoZFnl2m8im3ANUjvFkUZNhbyGWVCvii_xsZz9UqzsXCxMED3efOcpeUOlrGvMedb17Br6g9dccmPjDJ71yK2glKw0JWO6AuryxrxC_7gGyzoRtgszJgAI587FV0umNkQItkdyT72cHN5WobacLw-R0JsLHhWyJIfgpumq4pphE0Ht844jetwce58oAawQ_jXf9bmg9uucho_oYLBAKJzbnoNa7OYg6NEQxsHvZPVRjcjKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست : ما در تمام این مدت کنترل تنگه‌ها را در اختیار داشته‌ایم.
‏مجری : اما شما در حال مذاکره با ایران هستید تا تنگه هرمز را دوباره بازگشایی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/14872" target="_blank">📅 22:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14871">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هاآرتص: نتانیاهو به ترامپ
نه
گفت
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/14871" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14870">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خالیباف خطاب به اسرائیل بچرخ تا به بچرخیم
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/14870" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14868">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👻</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14868" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14867">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
مجید اخوان، سخنگوی سازمان هواپیمایی کشوری در گفتگو با خبرنگار مهر درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14867" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14866">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تسنیم گفت ایران با هشدار NOTAM پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است. @withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/14866" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14865">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLKr4ONChqRiTRauDKkBWd-Xvc2IojQFkT45jSCP_4nuiNOnfWf_5URxKvgGPsE2Lknt_NCG2YgIdjKygRBTikoGddNwPwHuSPbqwk4Lkoj8Iz9IP2rCiqU0gKT4dpgnRUNDUstaaxE9Btf1ORolcLMWZJCq86VHE8JaKfbJ-bzurvY2A-sQTG81bcnzqVRRVoODQNrVd1W2Gh7U1uEC3-1S65KN_BtIqE24rWt4dRF37yNmImxXWXihZt-NzzKCtDuLpoWqYW46mKIPsM4Cfj48Ig61enO9Ifx-oDIP1W-L6_TNKCniilM16NwvsWlDPyuZ1nDjCdDu9jwOlCClaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ از بالا پشت بام : آخرین پرواز در تهران نشست
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/14865" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14864">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تسنیم گفت ایران با هشدار NOTAM پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/14864" target="_blank">📅 22:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14863">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ea26e8e3.mp4?token=cJI8570MsIVYL08T7k9YCgQ5ojFI29VJopNBB097U3yTshQWKplb9iwnGC1-haS5r1ijig8cIPLqxHxAJLrzotLPdBZcjhKyQYdFNMWpqqp1U6TzCYKwy9Oy2dWttHRblueAYT9TPrJe66rvgGsU1OricXmr6gn7yRr-ygVgigq8EmRLoX9kUR_muUDfWaYqYAWvMv_APIe6ICZ4cfx-9UFnH6_VBTLaaF0yO4W2kBR4tZKT8yUjtXAeaZLdsKotiNE_DbGDkLCKzaXVSenSEl1e6htvedIkMAZzMtawtE3Vyu9vSpPohwCP4sL6oatU6jkGg5y_8XpbnCN9REr1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ea26e8e3.mp4?token=cJI8570MsIVYL08T7k9YCgQ5ojFI29VJopNBB097U3yTshQWKplb9iwnGC1-haS5r1ijig8cIPLqxHxAJLrzotLPdBZcjhKyQYdFNMWpqqp1U6TzCYKwy9Oy2dWttHRblueAYT9TPrJe66rvgGsU1OricXmr6gn7yRr-ygVgigq8EmRLoX9kUR_muUDfWaYqYAWvMv_APIe6ICZ4cfx-9UFnH6_VBTLaaF0yO4W2kBR4tZKT8yUjtXAeaZLdsKotiNE_DbGDkLCKzaXVSenSEl1e6htvedIkMAZzMtawtE3Vyu9vSpPohwCP4sL6oatU6jkGg5y_8XpbnCN9REr1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل اختلال در سامانه‌های موقعیت‌یابی GPS را در شدیدترین حالت قرمز قرار داد برای دفاع از خود و ایران نیز این روند را هم اکنون شروع کرده و در حال شدت بخشیدن است.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/14863" target="_blank">📅 22:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14862">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گروهک هکری حنظله وابسته به حکومت : امشب سپاه قطعا میزنه
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/14862" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14861">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4hrzZ4LxzQTJoeSFP1xQUltM21WoWmsmVXaXdwIEiZfGJ_mZonHun6aGCXG9tlZm2Y_uiUz3hkUxSubfg0sTjW42WU8QAm-bTjXyn7tXwfWeFmwOXLjZQiaPeuOjOOw_FOqrzUY5RxZ-ShPcjlufBf5F6cU0A40LJ3hZfvLjP_iem7yyWkUF2I2QTmQplDTQSUq8iR0sEcQFK2e2d2Fs_CsQ-bTlIT6kqj_g0Faq5XnGG4huwUWnHRuppmTfMkMTdyffgUn7gIbPntXNgVPUhbY8uGG2D1STQyvsTzUX0kS4mMi55vRKfAa0nmCNq1moxC9xTLyARZy151embXBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا دقایقی دیگر آسمان ایران کلیر میشود. یک پرواز در تهران میشیند و یک پرواز از مرز غربی خارج میشود.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/14861" target="_blank">📅 22:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14860">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ارسالی : دوست پسرم سربازه میگفت که لانچر اینا اماده کردن
🤷🏻‍♀️
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/14860" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14859">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دیده بان اتاق جنگ : اطراف سایت موشکی شهرک مسکونی ویلاشهرنجف آباد  تحرکات زیادی دیده میشه ورود ماشین های سنگین به پارک‌‌ کوهستانی پشت سایت
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/14859" target="_blank">📅 21:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14858">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/14858" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14857">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یدیعوت آحارونوت: ایران خبر درخواست ترامپ برای عدم حمله به اسرائیل در ازای مزایا در توافق را رد کرده و گفته است که به اسرائیل پاسخ خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14857" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14856">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🥊
UFC Freedom 250 + مراسم ۲۵۰ سالگی آمریکا (White House Event)
UFC فریدم ۲۵۰ همزمان با جشن ۲۵۰ سالگی آمریکا و برنامه‌های کاخ سفید برگزار می‌شود و به وقت تهران از حدود ساعت
۰۲:۳۰ بامداد روز دوشنبه
با بخش‌های قبل از رویداد و برنامه‌های طرفداری شروع می‌شود، سپس بخش
پریلمز (مبارزات مقدماتی)
از حدود ساعت
۰۴:۳۰ تا ۰۸:۳۰ صبح
پخش می‌شود که شامل مبارزات سبک‌تر و مبارزان کم‌تجربه‌تر است و نقش آماده‌سازی فضای اصلی را دارد، بعد از آن بخش
مین‌کارت (کارت اصلی)
از حدود ساعت
۰۸:۳۰ صبح تا حدود ۱۲:۳۰ ظهر
ادامه پیدا می‌کند که شامل مبارزات مهم‌تر و ستاره‌های یو‌اف‌سی است و در نهایت مهم‌ترین مبارزه شب یعنی
مین ایونت (مبارزه اصلی)
معمولاً نزدیک ساعت
۱۰:۳۰ تا ۱۱:۳۰ صبح به وقت تهران
برگزار می‌شود و کل این رویداد به‌صورت زنده از طریق سرویس
پارامونت پلاس
پخش می‌شود و در آمریکا بخشی از آن هم از شبکه
سی‌بی‌اس
پخش خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/14856" target="_blank">📅 21:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14855">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb472a4ecd.mp4?token=r5A4CXdfCeT_P8OgKd8_f0M-7Ah9R9lDRjAeKpdlzysfpVqSZgdb_Oovcxjnl-fiVOl65yKW8Gp0yWI10_jQO4USGDtOA4-fXtIKHNjD8Jvsq2g50cm4FpK4kWooSSU1-Fjn6bCt0rkHRjGIpMbfdKfTUzgM898Ev_qG0ZdGGbu4YNBBJ-b6JP-K-TzvsLaxCnZjl9fitFFDadfmXbRsi1CAYIIrBlmTLeaOuCbqRYFmuoVN3g4cd8D5Jj1cyzivh87Tfw87JZ90T4wOyDFlB3nRHIKB6_1aQbj9rkddqlfaUMYVU_fcrkdjtH1_6hX7KpKLLq0rToSLGR0f60iySA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb472a4ecd.mp4?token=r5A4CXdfCeT_P8OgKd8_f0M-7Ah9R9lDRjAeKpdlzysfpVqSZgdb_Oovcxjnl-fiVOl65yKW8Gp0yWI10_jQO4USGDtOA4-fXtIKHNjD8Jvsq2g50cm4FpK4kWooSSU1-Fjn6bCt0rkHRjGIpMbfdKfTUzgM898Ev_qG0ZdGGbu4YNBBJ-b6JP-K-TzvsLaxCnZjl9fitFFDadfmXbRsi1CAYIIrBlmTLeaOuCbqRYFmuoVN3g4cd8D5Jj1cyzivh87Tfw87JZ90T4wOyDFlB3nRHIKB6_1aQbj9rkddqlfaUMYVU_fcrkdjtH1_6hX7KpKLLq0rToSLGR0f60iySA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پدر و  دختری،  احمد ایراندوست(غول برره)، وسط این هیر و ویر‌…
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14855" target="_blank">📅 21:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14854">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قالیباف : بازی پلیس خوب و پلیس بد قدیمی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/14854" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14853">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خضریان، نماینده مجلس:
ارتباط واتساپی عراقچی با ویتکاف باید کاملاً قطع شود!
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14853" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14852">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">زیرنویس شبکه خبر :
پاسخ به حمله اسرائیل قطعی است.
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14852" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14851">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">لارنس نورمن خبرنگار وال استریت ژورنال:
در عرض دو هفته، ترامپ از این موضع که «لبنان از موضوع ایران جداست» به این موضع رسیده که «لبنان مرتبط است اما اسرائیل حق پاسخگویی دارد» و بعد به این موضع که «لبنان مرتبط است ولی من فکر نمی‌کنم اسرائیل حق پاسخگویی داشته باشد چون باید توافق را منعقد کنیم»
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14851" target="_blank">📅 20:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14850">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ادعای ترامپ در گفتگو با اکسیوس:
این توافق به نفع اسرائیل خواهد بود، زیرا مانع از دستیابی ایران به سلاح هسته‌ای شده و این کشور را ملزم به رهاسازی مواد هسته‌ای می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14850" target="_blank">📅 20:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14849">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یدیعوت آحارونوت: کابینه امنیتی اسرائیل امشب تو یه مکان مخفی تشکیل جلسه میدن
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14849" target="_blank">📅 20:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14847">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">https://t.me/withyashar/s/5</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14847" target="_blank">📅 20:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14846">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ به پوتین اعلام کرد توافق پایان جنگ با ایران تقریبا کامل شده. پوتین هم از پیشرفت این موضوع ابراز رضایت کرد
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14846" target="_blank">📅 20:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14845">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فرمانده قرارگاه خاتم الانبیا: فرزندان ملت در نیروهای مسلح «دست به ماشه» آماده شلیک به قلب دشمن هستند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14845" target="_blank">📅 20:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14844">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل توسط جبهه مقاومت قطعی است
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14844" target="_blank">📅 20:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14843">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
توافق با ایران از راه دور امضا خواهد شد، سپس امضای حضوری آن ممکن است یک هفته بعد در اروپا انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14843" target="_blank">📅 20:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14842">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بن‌گویر خطاب به نتانیاهو: قوی باش، نترس
@withyashar
🥥
🥥</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/14842" target="_blank">📅 20:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14841">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ به باراک راوید گفت: چرا بی‌بی (نتانیاهو) باید یک حمله‌ی لعنتی انجام می‌داد؟ من خیلی عصبانی شدم. به او گفتم.
او اصلاً هیچ قضاوت لعنتی ندارد. من این را به او گفتم.
اگر توافق امشب امضا شود، فوراً دستور لغو محاصره دریایی ایران را خواهم داد.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14841" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14840">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ در گفتگو با فاکس نیوز اعلام کرد که از ایران خواهد خواست که به حملات اسرائیل علیه حزب الله پاسخ ندهد. ترامپ همچنین اعلام کرد که توافق با ایران ظرف ۲-۳ ساعت آینده به صورت الکترونیکی امضا خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14840" target="_blank">📅 19:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14839">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: از ایران می‌خوام موشک به اسرائیل شلیک نکنه. این توافق در ساعات آینده امضا خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/14839" target="_blank">📅 19:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14838">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صابرین نیوز تایید کرد :
برکناری سعید جلیلی از شعام و جایگزینی باقری کنی با وی
@withyashar
یاشار : پوست اندازی رژیم  ادامه ‌داره</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14838" target="_blank">📅 19:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14837">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ به باراک راوید از اکسیوس گفت:
قرار بود امروز صبح توافق را امضا کنیم، اما حمله اسرائیل به بیروت آن را به تأخیر انداخت.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14837" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14836">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ به آکسیوس : به او گفتم، او هیچ قضاوت درستی ندارد
وی همچنین به ناتانیاهو گفت هیچ حمله دیگری به لبنان انجام ندهد و هشدار داد که این حملات می‌تواند توافق را به خطر بیندازد.
ترامپ می‌گوید از ایران خواهد خواست که در پی حملات اسرائیل به لبنان، با حملات موشکی پاسخ ندهد.
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14836" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14835">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: من با نتانیاهو صحبت کردم و بهش گفتم:داری چه غلطی می‌کنی؟
@withyashar
🤣</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/14835" target="_blank">📅 19:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14834">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کرملین: پوتین و ترامپ درباره ایران و اوکراین گفتگو کردند
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/14834" target="_blank">📅 19:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14833">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در تماس اخیر با رئیس‌جمهور ترامپ گفت که اسرائیل با عقب‌نشینی کامل از جنوب لبنان، از جمله پنج نقطه‌ای که در حال حاضر توسط نیروهای دفاعی اسرائیل (IDF) در اختیار است، موافقت نخواهد کرد، طبق گزارش معاریو.
نتانیاهو همچنین عقب‌نشینی از خاک سوریه را که اسرائیل از زمان سقوط بشار اسد اشغال کرده است، رد کرد
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14833" target="_blank">📅 19:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14832">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شبکه ۱۴
:
ایالات متحده در حال حاضر از طریق واسطه‌های مختلف تلاش می‌کند از هرگونه حمله احتمالی نیروهای نظامی ایران به اسرائیل جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14832" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14831">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">باراک اوباما : توافق ترامپ که از ماله من زاقارت تره
باراک اوباما، رییس‌جمهوری پیشین آمریکا، در گفت‌وگو با ای‌بی‌سی نیوز گفت بعید است هر توافقی که میان آمریکا و جمهوری اسلامی حاصل شود، تفاوت چشمگیری با برجام داشته باشد یا نسبت به آن بهبود قابل توجهی محسوب شود.
اوباما با اشاره به برجام گفت این توافق بر محدود کردن برنامه هسته‌ای ایران، تعیین سقف برای غنی‌سازی اورانیوم و پذیرش بازرسی‌های آژانس بین‌المللی انرژی اتمی در ازای رفع بخشی از تحریم‌ها و آزادسازی دارایی‌های مسدودشده ایران استوار بود.
او همچنین ابراز امیدواری کرد بمباران‌ها متوقف شود و مردم عادی دیگر از پیامدهای جنگ رنج نکشند.
رییس‌جمهوری پیشین آمریکا تاکید کرد دیپلماسی را به اقدام نظامی ترجیح می‌دهد و گفت نباید تصور کرد که می‌توان با زور یا بمباران به راه‌حل دست یافت.
اوباما خواستار بررسی کامل گزینه‌های دیپلماتیک شد و گفت توافق‌هایی که همه مشکلات را حل نمی‌کنند اما ۸۰ یا ۹۰ درصد آن‌ها را برطرف می‌کنند، می‌توانند از جنگ جلوگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14831" target="_blank">📅 19:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14830">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رسانه‌های اسرائیلی: شهرداری‌های ایلات، تل‌آویو بزرگ، نتانیا و حیفا پناهگاه‌های عمومی را باز کرده‌اند.»
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14830" target="_blank">📅 18:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14829">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">منابع عربی : امریکا در پیامی به اسرائیل گفته امشب ایران حملات موشکی انجام خواهد داد
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/14829" target="_blank">📅 18:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14828">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1fbuXsikBY6sQ54CRt5zCh-cXtibL164ss5QNSV2UODHmos29M3hmBljZ7wZPpwJWAy9Rsqz_jZN5eyXMlS0jq1zzjmVIqePhWDO7IZrA0h80bu5gLA0b0J7SJMavZuBLWKreFwrehx3R4Zk5WrpRPi-Yk0ekpqryC7xTJWXjSf0Idvib9G_yu0LoXmVke2NfBlyzJbUWDpL9LRFYqyBbXbD2_e_aWBmbmcI2lW1rICfQn2u5wprDD3-hNQODuL1Vm5otySvujlqtlLg12FPmNp3XmCZ5VQz_sH4TWXdPJX80Nl8exFPfG9_ZmamiRlIIKJFTkadNipRHC7gUvl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در چنین روز مهمی که ما تا این اندازه به دستیابی به یک توافق صلح با ایران نزدیک شده‌ایم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در واکنش به آن انجام شد بسیار کوچک و بی‌اهمیت بود؛ هیچ‌کس آسیب ندید، مجروح نشد یا کشته نشد و نباید این روند مهم را مختل کند. ما بسیار به توافقی نزدیک هستیم که صلح را برای منطقه، از جمله لبنان، به ارمغان خواهد آورد و همه طرف‌ها باید از درگیری و تشدید تنش خودداری کنند. نباید هیچ حمله دیگری از سوی اسرائیل در هیچ نقطه‌ای از لبنان انجام شود، اما در عین حال نباید هیچ حمله‌ای از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل صورت گیرد. این می‌تواند آغاز یک صلح طولانی و زیبا باشد؛ نگذارید این فرصت از بین برود! از توجه شما به این موضوع سپاسگزارم. دونالد جی. ترامپ، رئیس‌جمهور ایالات متحده آمریکا»
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14828" target="_blank">📅 18:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14827">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هگست، وزیر جنگ آمریکا:
من انتظار ندارم که حملات اسرائیل به حومه جنوبی بیروت مانع توافق با ایران بشه؛ اگر ایران میخواد این موضوع ادامه پیدا کنه، باید حزب‌الله رو مهار کنه.
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/14827" target="_blank">📅 18:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14826">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14826" target="_blank">📅 18:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14825">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromALIREZA</strong></div>
<div class="tg-text">تو ویس گفتی یه سری بزنیم به کانالهی رژیم اسگولا اینو منتشر کردن</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14825" target="_blank">📅 18:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14824">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlcDyNhTaIpe2kuwQj7Benq0H2c36WFZ80mOxioZFUGe1lFMIzvDhY4W_Y5pGbezoWdXwi74B2lFUz01t6jhwJ21QE7g_U87faDNhC8U6JzScS-_4LiDtjRv4MVMLQuxvJN0q2KGPnRt-4RlhmH8J3Nej1OaPPGdmsEcKrvL9KxqjtRohT-KoWnNTpd74N-HcKgWKJFBkZQd1lBHVcc6HICFX7TVL-vdtaQOJEtAc6Lr84OUHsrLwSZfvhRx6gVIiDAyutHhx1J6DMzbJ5VkwEJa2T7W4g7fKIgOnGBuK6kLUTBN5FMLPDgWPZ4Ohxw6EPur--cDYnIAK7VNrXIbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی‌پیش ستون دود جنوب‌کرج
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14824" target="_blank">📅 18:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14823">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1de42f04e.mp4?token=PmY3zlamaTpyerBCGIUsS6fhqWGGOCU_j4DldkGJde_sLxbkZJ58ZmHiyk2qubnwwJlUb25Kent9SYxZ9egiBy9YKIKCTo5jfpznGIaQIpkAi97Qcro6PqW2idREz3gdiunXXSmiEGHs1drfueZm8aUk1fIpfKfErdg6resEhWGf8QFVf07bPHIt8W2BY_NGWIPfT5GM1X09m0DdUJPclSynPYgjpJQ0f5gn2gOH2X2yD2vCVYSO1btQuYqq8o6lZETbsxi6aKnZk2MMBHW9QdAfKB1Ik3pEPS8rlPHtB0tFGW3siWgLPn0E1COV8iRjWbU_1wYqiSf8o1ngaA9VDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1de42f04e.mp4?token=PmY3zlamaTpyerBCGIUsS6fhqWGGOCU_j4DldkGJde_sLxbkZJ58ZmHiyk2qubnwwJlUb25Kent9SYxZ9egiBy9YKIKCTo5jfpznGIaQIpkAi97Qcro6PqW2idREz3gdiunXXSmiEGHs1drfueZm8aUk1fIpfKfErdg6resEhWGf8QFVf07bPHIt8W2BY_NGWIPfT5GM1X09m0DdUJPclSynPYgjpJQ0f5gn2gOH2X2yD2vCVYSO1btQuYqq8o6lZETbsxi6aKnZk2MMBHW9QdAfKB1Ik3pEPS8rlPHtB0tFGW3siWgLPn0E1COV8iRjWbU_1wYqiSf8o1ngaA9VDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/14823" target="_blank">📅 18:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14822">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02564fdd83.mp4?token=KaG3wGsWs6bffCncTXR78RaRPDpLepjbgJ1sdgZ2A3tpSN0UASdYntHu1W7B9Uovzlfdl5Jl8KYazS2vKlkRROuVflXz384IwYm1kMxIphhQL40_fNhFTTtRAe_Hocj5537F-tHBWlU1MD9fOpbo4dNN_WdQGYVLcFanM_dxlpr09x6-GN2WC_ledUbjRzuRWGG3BOqIbfZysWyyGbFsVd709fHiPLhHPUIBgf8taNN6Qm9mKpLVeaqvNOdarLYKpBgEGcPgLofQ55glNSSl1ULSHw5zuWdkx9wHPRVn3I47Qjf-kk8pKx8vPgwZJlwZA-j9nnUa6bVbiYNPfoTC_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02564fdd83.mp4?token=KaG3wGsWs6bffCncTXR78RaRPDpLepjbgJ1sdgZ2A3tpSN0UASdYntHu1W7B9Uovzlfdl5Jl8KYazS2vKlkRROuVflXz384IwYm1kMxIphhQL40_fNhFTTtRAe_Hocj5537F-tHBWlU1MD9fOpbo4dNN_WdQGYVLcFanM_dxlpr09x6-GN2WC_ledUbjRzuRWGG3BOqIbfZysWyyGbFsVd709fHiPLhHPUIBgf8taNN6Qm9mKpLVeaqvNOdarLYKpBgEGcPgLofQ55glNSSl1ULSHw5zuWdkx9wHPRVn3I47Qjf-kk8pKx8vPgwZJlwZA-j9nnUa6bVbiYNPfoTC_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای عراقچی‌ شما گوه میخورید
🤣
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/14822" target="_blank">📅 18:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14821">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14821" target="_blank">📅 17:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14820">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارتش اسرائیل: آماده شلیک از ایران در ساعات آینده هستیم، در حال حاضر تغییری در دستورالعمل‌ها وجود نداره.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14820" target="_blank">📅 17:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14819">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانال 15 اسرائیل:تمام سامانه های پدافندی در اسرائیل به حالت آماده باش کامل درآمدند و در انتظار پرتاب موشک قریب‌الوقوع از سمت ایران می‌باشند
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14819" target="_blank">📅 17:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14818">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل دستور تشدید عملیات‌های زمینی در جنوب لبنان رو صادر کرده و به نیروهای دفاعی اسرائیل دستور داده که عمیق‌تر به خاک لبنان پیشروی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14818" target="_blank">📅 17:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14817">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سفیر آمریکا در سازمان ملل متحد:
رئیس جمهور ترامپ و معاونش جی‌دی ونس، کاملاً به امضای توافق امروز متعهد هستن.
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14817" target="_blank">📅 17:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14816">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگر در کار نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14816" target="_blank">📅 17:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزارت امور خارجه‌اسرائیل در واکنش به تهدیدهای ایران اعلام کرد: “این حکومت طبق معمول دروغ می‌گوید. نماینده ایران، حزب‌الله، همان طرفی است که به اسرائیل حمله کرده است. ما شلیک آتش به سوی خاک خود را تحمل نخواهیم کرد.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14815" target="_blank">📅 17:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ بیدار شد
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14814" target="_blank">📅 17:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الحدث: علی الحاج، از فرماندهان ارشد حزب‌الله در حمله به ضاحیه بیروت هدف قرار گرفت. تداوم ضربات سنگین به بدنه فرماندهی گروه‌های نیابتی رژیم ایران در لبنان. @withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14813" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الحدث: علی الحاج، از فرماندهان ارشد حزب‌الله در حمله به ضاحیه بیروت هدف قرار گرفت.
تداوم ضربات سنگین به بدنه فرماندهی گروه‌های نیابتی رژیم ایران در لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14812" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد ارتش اسرائیل اندکی پیش از حمله به منطقه ضاحیه بیروت، فرماندهی مرکزی آمریکا (سنتکام) را از این عملیات مطلع کرده بود.
ارتش اسرائیل پیش‌تر در بیانیه‌ای اعلام کرد در واکنش به شلیک پرتابه از سوی حزب‌الله به شمال اسرائیل و نقض آتش‌بس از سوی این گروه تحت حمایت جمهوری اسلامی، یکی از مقرهای حزب‌الله را در ضاحیه بیروت به طور دقیق هدف قرار داده است.
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14811" target="_blank">📅 16:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الحدث به نقل از منابع:
علی الحاج، فرمانده حزب‌الله، در حمله هوایی اسرائیل به حومه بیروت ترور شد
@withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/14810" target="_blank">📅 16:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14809">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبر ترور ‌نعیم قاسم تایید نشده است منتظر تایید هستیم @withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14809" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14808">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانال های امنیتی: فرماندهی موشکی هوافضا ایران در حال آماده سازی یک حمله گسترده
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14808" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14807">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">موسوی، سخنگوی پیشین هیات رئیسه مجلس:
هدف حمله امروز اسرائیل به ضاحیه بیروت در روزی که قرار بود توافق امضا بشه، تحقیر جمهوری اسلامی بود.
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14807" target="_blank">📅 16:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14806">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فاکس نیوز به نقل از  دیپلمات شرکت‌کننده در مذاکرات:
حملات امروز بیروت مانع از نهایی شدن توافق شده‌اند
این یک تلاش آشکار اسرائیل برای خراب کردن توافق رئیس‌جمهور و کشاندن مجدد ایالات متحده به جنگ است
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14806" target="_blank">📅 16:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14805">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsLwKioMWy6RHoRZb4gLFqBlWvREwz95jNtnUiTHmgVnkENVSHBWM52-qi8jMppYhD6IAFpf7_VTbKcIJ47GcIzLSIP7BBb40ggnS3JWVTxOOWDFsE54MGlQxLFX1O45DBSoOc6xRs2FfWkDd7wKDkquj8bJTk7QH3un1OfH_3BymLo2A4nQtkWEjVH1Z3HuO_KYwF_7lgOFVE1SrOtUi4qVqx12BVkf6LGWN_j0iI4jkxmAem9X8RstqAY2VjdGZmlrR0tXmsWHwsxWoLMcqOukrWgr6rX7Jt-efdpwWCagmNfAVRaoHhX6vPAxiqgYXU-rv1MgEqXhk_-JrTboFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد بزرگ شطرنچ نتانیاهو اول تصویری از حمله به بیروت رو منتشر کرد و تو پست بعدی تولد ترامپ رو تبریک گفت :
@withyashar
😁</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14805" target="_blank">📅 16:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14804">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14804" target="_blank">📅 16:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14803">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14803" target="_blank">📅 16:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14802">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14802" target="_blank">📅 16:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14801">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قرارگاه خاتم: پاسخ کوبنده میدیم
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14801" target="_blank">📅 16:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14799">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فاکس‌نیوز: یک دیپلمات حاضر در روند مذاکرات گفته حمله اسرائیل به بیروت فعلاً توافقات رو به گره انداخته و به همین خاطر امضای توافق تا این لحظه انجام نشده.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14799" target="_blank">📅 16:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14798">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبر ترور ‌نعیم قاسم تایید نشده است
منتظر تایید هستیم
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14798" target="_blank">📅 15:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14797">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانال ۱۲ اسرائیل به نقل یه مقام امنیتی: حتی یه موشک از سمت ایران پرتاب بشه، با حمله‌ای گسترده به اونا پاسخ میدیم و آماده هر سناریویی هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14797" target="_blank">📅 15:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14795">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14795" target="_blank">📅 15:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14794">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبرگزاری رسمی اسرائیل: حمله به حومه جنوبی بیروت توسط دو هواپیمای جنگی انجام شد که چهار موشک هدایت‌شونده شلیک کردند.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14794" target="_blank">📅 15:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14793">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdAowKtwUvvxQKeMSS7Iq8weeUP2xs38aFxmTKt1XhIqizcG1jH1LJyYM9pCBGsP0RDFad8f4WYafuFPy7_3OAufU_qxXA7I7njwUA7XoP3xbtRUFpCNOIA7ZdqpYERX7Q1uBS3dtTIA2-E-Du9eXVbPHBGxbpYAjT6CyUXBurxYgdHCyc42M7Hm-TDJbepucdo9G_Be-05J4P_A3yzo3gAJ0pPbWJjnFhLiqkcsDbCEkSadXgkej3qaDrElm8ls_RgTmCd8g140ityn_9Is45e4KzdqAoziqNQ4pg5HqofI2I7uDP9iXcE9-6yzNO76jMuKSQDWK-w1VNDYa0syQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان دید از ملک شهر الان
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14793" target="_blank">📅 15:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14792">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرنگار صداوسیما: تنگه هرمز طبق اعلام نهاد مدیریت آب‌راه خلیج فارس تا اطلاع بعدی همچنان مسدود است و هیچ کشتی خارجی حق ورود و خروج ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14792" target="_blank">📅 15:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14791">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">العربیه: قطری ها و پاکستانی ها فشار زیادی می‌آورند تا تشدید تنش رخ ندهد!
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14791" target="_blank">📅 15:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14790">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f830c996b.mp4?token=jnRns7hNBgGb9NEui4WOGUbFG-JQZUp1x1zZx7xSS4V7gkV2YrFCdbaUZaAHdCfUP4Ja8MPbvvTjG0LnyusN2hHimB33IA8wgC8fPAriWcQ-YS5Y93zePUrrLeQZNCluZn_KlQft1uN2gX71qu4OGneGKIxBEWwxdT7yJNIDB_kNVvlmGtv8G0v1ZDpauURkCvO9BhRKMp4q-DRt3K7A_qMaK6XxAj6iGRt3j59GF9gWrZHmJo3aMpa0C143RFDPAQWM_0SCl3317H1LGs7CaXcyHBengyXqrHEBxeHdcQT-ojzJjuQ-9GSSuqk0Ylha9-OnziR0NKuEN0DiD8mE4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f830c996b.mp4?token=jnRns7hNBgGb9NEui4WOGUbFG-JQZUp1x1zZx7xSS4V7gkV2YrFCdbaUZaAHdCfUP4Ja8MPbvvTjG0LnyusN2hHimB33IA8wgC8fPAriWcQ-YS5Y93zePUrrLeQZNCluZn_KlQft1uN2gX71qu4OGneGKIxBEWwxdT7yJNIDB_kNVvlmGtv8G0v1ZDpauURkCvO9BhRKMp4q-DRt3K7A_qMaK6XxAj6iGRt3j59GF9gWrZHmJo3aMpa0C143RFDPAQWM_0SCl3317H1LGs7CaXcyHBengyXqrHEBxeHdcQT-ojzJjuQ-9GSSuqk0Ylha9-OnziR0NKuEN0DiD8mE4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل به فارسی با انتشار این گیف از ظریف نوشت:
هفته خوبی داشته باشید
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14790" target="_blank">📅 15:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14789">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">منابع عبری: ارزیابی‌های کنونی در اسرائیل نشان می‌دهد که ایران تعادل را حفظ کرده و به حمله در حومه جنوبی بیروت پاسخ خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14789" target="_blank">📅 15:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14788">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مقام اسرائیلی به نیویورک تایمز :
توافق آمریکا و ایران آخر بازی نیست و هنوز ماجرا ادامه داره
ما از آمریکا خواستیم تو محدود کردن عملیات نظامی‌ تو لُبنان دخالت نکنه
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14788" target="_blank">📅 14:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14787">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سخنگوی آتش نشانی تهران: دود مشاهده در قسمت شمالی شهر تهران، مربوط به حریق فضای سبز در محدوده ولنجک است.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14787" target="_blank">📅 14:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14786">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57768c317.mp4?token=MSmHqAxPE-7AcYBPO1v6Gb_oUNt_EmkuVVRP1P0aATOIyeaNwB6xaz9icUhCp3Pp22cs6o0LUKXWuw_Y3XKcU-VW-B4aqldF6IpLWmO6Wo2neccd9GxPM7fzAD6jN1KPsB1kte-upQjCA5vh3YFu2dZr7Mm4waJfgJq2IMDWUk1LCqQVwltScpuZL6n7hKXEr4_XHz2hlvGh9Sg4p4fcjlX2sBV75LKmrltsSS5sGWL3sc0AuTHTgsEnDFnv0z65GeoNLeskgIpw-yZD1yUA3A3sx0o4682tw31Ua8a7CKs_HZMBxqs2CXH4iJcrZcI-9imFzggUyucaCVsMWxq0Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57768c317.mp4?token=MSmHqAxPE-7AcYBPO1v6Gb_oUNt_EmkuVVRP1P0aATOIyeaNwB6xaz9icUhCp3Pp22cs6o0LUKXWuw_Y3XKcU-VW-B4aqldF6IpLWmO6Wo2neccd9GxPM7fzAD6jN1KPsB1kte-upQjCA5vh3YFu2dZr7Mm4waJfgJq2IMDWUk1LCqQVwltScpuZL6n7hKXEr4_XHz2hlvGh9Sg4p4fcjlX2sBV75LKmrltsSS5sGWL3sc0AuTHTgsEnDFnv0z65GeoNLeskgIpw-yZD1yUA3A3sx0o4682tw31Ua8a7CKs_HZMBxqs2CXH4iJcrZcI-9imFzggUyucaCVsMWxq0Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل: مرکز فرماندهی حزب‌الله تو ضاحیه بیروت رو زدیم
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14786" target="_blank">📅 14:51 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
