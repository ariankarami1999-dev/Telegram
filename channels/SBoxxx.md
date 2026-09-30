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
<img src="https://cdn4.telesco.pe/file/JPsNVCGdf6Z7Zv6IjdFRmcUkjSbO2kLyQl0vH5ofQGXUWOtMMvYcCVtwf0yT0H1oFN0gTjMDiQifRrTs6HIMBUC-uqJE8JSM8_M6S0X06wLgZidBe8BZ-lyw_8yEquQGplh0VQd5OktJ_DcebBfnVlZJt7GXBgqLDFqWg7OIE_jYduvZywHkgWlxSsqazKAzGGlgRNVFL09ABCEuyDnAfZx7ujxIfLVWvz88gTAAvPPZQMURKxA4SX9nA24LLMpGchmXhp_aX5UPUgXWQC0W4VSjaOonTFErasfNNhR7XR6D9QG3sdCpBk_WTbgj8ZnwLjQgLzFzH4LYe8wUuUg-cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-21381">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 152 · <a href="https://t.me/SBoxxx/21381" target="_blank">📅 19:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21380">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:  فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.  بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود…</div>
<div class="tg-footer">👁️ 275 · <a href="https://t.me/SBoxxx/21380" target="_blank">📅 19:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21379">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SBoxxx/21379" target="_blank">📅 19:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21378">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حالا آنهایی که دلار را ریال کرده و در بورس بردند برای برگشت به دلار باید تا آخر پاییز صبر کنند!
یا ذی الجلال و الاکرام!</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SBoxxx/21378" target="_blank">📅 19:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نامه بانک مرکزی به تمام صرافی های دیجیتال :   هر کاربر فقط روزانه اجازه خرید ۲۰۰۰ تتر را دارد</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SBoxxx/21377" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">معامله تتر از ساعت ۹شب تا ۹صبح روز بعد ممنوع شد</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SBoxxx/21376" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دبیر شورای عالی امنیت ملی خطاب به امارات:
میزبانی از قصاب غزه پیامد‌های مثبتی ندارد/ از جنگ اخیر درس بگیرید و از آغاز جنگ دست بردارید</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SBoxxx/21375" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">— لحظاتی پیش پرتاب یک موشک بالستیک ضدکشتی از فارس، ایران انجام شد.</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SBoxxx/21374" target="_blank">📅 19:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">معامله تتر از ساعت ۹شب تا ۹صبح روز بعد ممنوع شد</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/SBoxxx/21373" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به همراهان ما روی ۴۱۸۷ سیگنال سل داده شد و اکنون نزدیک حد سود نهایی در ۴۱۴۸ هستیم</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SBoxxx/21372" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شکست جعلی که در سقف کانال روی داده، اتفاقاً فروشندگان قدرتمندتری را تحریک به ورود کرده است.</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/SBoxxx/21371" target="_blank">📅 18:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5q33EIWcl4Bglotym37Gapcb6g9Rcmy9OhHdAuFkIdWybFxwEnRKHEO6wJRwS5OVaWS_XOkipFk7wsjC17_9XVhyhQdDgAHjC0RdlPcNK55JryhVPCqxM39mcB5dnPdh9Io8v0DZfZMO1f3PSjleiFpwWXznFV-zoMoOfsFgWammroL2e9JCnPU9lZNzD2S7Yxc1Qp_8B5zkDIzGwlm5c9P-3lEnA1cpEcoJh4uXCkk3WoXfSyp88OVLem2xDKbX4S8b17WyOAGkfnTr1Lj2euYO9qmISht_8bOgGH1qcBclb4CKqfNzXy1UmydO88TUKMmoroy1FBo02aj3_P02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر احتمالی طلا تا آخر هفته</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SBoxxx/21370" target="_blank">📅 18:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21369">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTMydS4lbhdTBTi47YjqB1Dggxpy-xnTPpOEoKUZVQL4AS2vHnxwFdf90LWuMiFhS3lOi8UALw3-ow88sCJp5FGrmKUi9B3x_yQ3a-d5iMWd7NRBQndHg22rGkSGGWdcH36WgB27dZkLAi7myEot5_OkPB8vE4TiPqQTBpn63GT4KPyO1V2GQ1doFFPmwOX2ZqUJ8vA_zaVan7QetZnVtP949iyLfxDiTl1gy18ySQ3wa4i9rUu8m9xtWpdTldLunwU8b0ael_b8v7BDnCXnyriAoo8wIJUIXo6kTY64Q6nFGaeohvB6pb1X3AJEVHdyE-iwbjFmFr0nOaeWpjX14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول سناریوهای قیمتی</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/21369" target="_blank">📅 18:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21367">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sunrun_RUN_Democratic_Congress_Scenario_2026_Revised.pdf</div>
  <div class="tg-doc-extra">84.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/21367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/21367" target="_blank">📅 18:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/21366" target="_blank">📅 18:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df6804c1e.mp4?token=Yj6Zt2abXZAeHuHxP2cXDixUZ2MtUOVMqbNRZ-Lj5kmbeINVqoEH3kHc45ufFw21R6BYr6AGFXLr6ULlzRx4kr4WtdAwNy4ZqWnFpNyxxci01276Z_c9qkxFfC33U0jsTkvJCDAwVIm35QnA0HsVr_R7vmOKVR-yDkEIzys0ppuChTZyq-yj5jTF9hflyKwmxd2BVP4I6OhJkKumHkI9nR6xUIFPW--F3w5r8tgkJNC0mI_Ev_gaHp-Pnz_cm0xt6B6XKD7QgPjWgYr0D9q0rlgBna5iYfWmbqOK70SrbmDiOu9gkQNfmPiZuqhhqcfSXfJXP-uG3bYZv6JgnzRrgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df6804c1e.mp4?token=Yj6Zt2abXZAeHuHxP2cXDixUZ2MtUOVMqbNRZ-Lj5kmbeINVqoEH3kHc45ufFw21R6BYr6AGFXLr6ULlzRx4kr4WtdAwNy4ZqWnFpNyxxci01276Z_c9qkxFfC33U0jsTkvJCDAwVIm35QnA0HsVr_R7vmOKVR-yDkEIzys0ppuChTZyq-yj5jTF9hflyKwmxd2BVP4I6OhJkKumHkI9nR6xUIFPW--F3w5r8tgkJNC0mI_Ev_gaHp-Pnz_cm0xt6B6XKD7QgPjWgYr0D9q0rlgBna5iYfWmbqOK70SrbmDiOu9gkQNfmPiZuqhhqcfSXfJXP-uG3bYZv6JgnzRrgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
آزمایش و رونمایی گسترده چین از نسل جدیدی ربات‌های انسان‌نمای پیشرفته با قابلیت‌های نظامی و امنیتی    این ربات‌ها در نمایش‌های عمومی شامل حرکات رزمی، تعادل پیشرفته، پرش، و تعامل مستقل با محیط هستند و توسط چند شرکت رباتیک چینی به‌عنوان نمونه‌های «آماده کاربردهای…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/21365" target="_blank">📅 18:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21364">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این چه پاییزی است که هنوز پایانش نرسیده!  نکبت ها تخمهای خودمان هم جوجه شد از بس که در بحران زیستیم!</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/21364" target="_blank">📅 17:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21363">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⁨ پاسخ همتی به وزیر خزانه داری آمریکا:   جوجه رو آخر پاییز می‌شمارند!</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/21363" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21362">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⁨ پاسخ همتی به وزیر خزانه داری آمریکا:
جوجه رو آخر پاییز می‌شمارند!</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/21362" target="_blank">📅 17:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رسانه‌های اسرائیلی گزارش می‌دهند که هواپیمای شرکت FlyDubai دارای یک خلبان روسی و یک کمک‌خلبان اوکراینی بوده است، که ممکن است دلیل درگیری ایجاد شده باشد.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/21361" target="_blank">📅 17:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKcyqrLoJXAutOzG51LxXx_xV63Kk94zAyRJZ-5w9_ie0gJt0jlBXKETXtku_PbznpD6N-pUGm9NXHyRzQeEXN-jwYyIlsl2sXRbIT14yAAFmawnF-l4aCQwqqxozp3QSgGVBYVfOUTPdtnqiLvXNy7StYzUNzlsisQujtrsoj4fJwg6E0nlYynUV_PELkr2Fki7Bexo4rsR-wMgSXPrEz7oLi2ANMGa7BgcblQAzX3JYn2fTydRJUlW4wT2jdyASr4KEvoG4tdO-1Hpv2QO83oSHGnRYn8XPen80u6AkKzjsWM1j_2wjChxHuSN2v44avwauQkieCrYVDAEhB30vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر احتمالی طلا تا آخر هفته</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/21360" target="_blank">📅 14:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فلایت‌رادار از تغییر مسیر یک پرواز دیگر شرکت «فلای‌دبی» به مقصد اسرائیل خبر می‌دهد
بر اساس این گزارش، هواپیما در حال بازگشت به دبی است</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/21359" target="_blank">📅 14:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در فاصله میان حباب منفی تا ارزش منصفانه قرار دارد  در این شرایط، فروش در مقاومت توصیه می شود:  یک مقاومت همین محدوده 4197 الی 4203 است  بعدی 4257 است (احتمالاً نرسد)  تارگت ها:  4182 4148 4124</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/21358" target="_blank">📅 14:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21357">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فردا ساعت ۱۳:۳۰ با نیما درباره آخرین تحولات مربوط به جنگ گفتگو خواهیم کرد  لینک تماشای نشست Live</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/21357" target="_blank">📅 13:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21356">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رسانه‌های اسرائیلی گزارش می‌دهند که هواپیمای شرکت FlyDubai دارای یک خلبان روسی و یک کمک‌خلبان اوکراینی بوده است، که ممکن است دلیل درگیری ایجاد شده باشد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/21356" target="_blank">📅 12:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ارواح عمه تان آخر هواپیمای در حال پرواز هم جای دعواست؟!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/21355" target="_blank">📅 12:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1Sn3-OXEbIUcpe97EmaTw6rWeEatPaf0Bcph-CSG5UkU4cGEvZ3HsREaodBWgv_2QAoCU2GkrNNjBxzUHNuCR5El13SlKEtFHk-jWdHBreuoKLY8XJvuvNzgeKhL6Rthd-Wigw2F0JCjLKXtTWNhzO6kcGhv5xuEJfKlRqRTQ6v61-70VU-szc7ef-o6dNzavRODYhBvRCra4z4GmxscVudJZhH5MfnQ3R_NFTwOp5_uW7Nz2Nr1U7VEowFhQl45RuQYkTteQqOT3Om8uscUwr_IlGZVTMIj7yEea93pgH02qcq97gbY3AGyUqnwqpNyFEh24IkSPe0Lq38bzndRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در فاصله میان حباب منفی تا ارزش منصفانه قرار دارد
در این شرایط، فروش در مقاومت توصیه می شود:
یک مقاومت همین محدوده 4197 الی 4203 است
بعدی 4257 است (احتمالاً نرسد)
تارگت ها:
4182
4148
4124</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/21354" target="_blank">📅 12:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNLBXV5p8zNYvpwbpaHjIM4Q3haU_7Sj9Ej3ZZNArTwg7HM-Wq0wwDfSgoF3ZEXxSlUnVb83NReVzAl5jziJGbYtVTOzhTg30YESfNMKVI-aI-TVuq_vpVhix5PDcapnoNGJBMrput2gOR59m3NkQJwbWJaE2_XiOAjrSGsRTIcEIlbO6splAzeQt0TRrW1HI0n2kJ0Lgh_us-u7hDHfyn5wnnR05sFnyKZRQbLQgbftob_fo8SkjHZk7HZrhsFOcPoQiinDUS7kCA3LkvwzaJdvdJPgH3RdbWTRTEwG8uV5OTvmAG6wlrjpJTizRntspveqxC3j1OfxBmLyNyPI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/21353" target="_blank">📅 12:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21352">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f193b66f88.mp4?token=Pqd-uG6K_wTiCfjsJ-Kk44RI7ByXLUVxfH1rUH4l9cIwVSP_EBQNLrq1jvgtZVhzFzqOZv0IVX2UqMTz8s_9a5XBKTrCd72Zw7M7oZN0hlAyJnBFxXv4_6PPlAhm_2zk8MgbDXlZZ8yXy7WpGpEOkB3rfAkG-3xVrcJV-UpRp5ksBvZRLq7fQWVIpIeO6UB8P2-2wOEW52L9GRoIBsTJWyH9JukduGj71AGYGDPH-X9EavKDO3vLRvrJ2H47B1al6ytlZbJtvEG7FRveVHx1_hu7LH2WfU7ko2nLa5DEW0zEzOiDQBIQdlKXGWpiWKSrdNyYKX7_5UrW7ux0ZanA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f193b66f88.mp4?token=Pqd-uG6K_wTiCfjsJ-Kk44RI7ByXLUVxfH1rUH4l9cIwVSP_EBQNLrq1jvgtZVhzFzqOZv0IVX2UqMTz8s_9a5XBKTrCd72Zw7M7oZN0hlAyJnBFxXv4_6PPlAhm_2zk8MgbDXlZZ8yXy7WpGpEOkB3rfAkG-3xVrcJV-UpRp5ksBvZRLq7fQWVIpIeO6UB8P2-2wOEW52L9GRoIBsTJWyH9JukduGj71AGYGDPH-X9EavKDO3vLRvrJ2H47B1al6ytlZbJtvEG7FRveVHx1_hu7LH2WfU7ko2nLa5DEW0zEzOiDQBIQdlKXGWpiWKSrdNyYKX7_5UrW7ux0ZanA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخستین خبری بود که در ۹۳ سال گذشته از سمنان منتشر شد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21352" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21351">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بانک مرکزی گفته از امروز به هر  کارت ملی ۱۰ هزار دلار تعلق می گیرد.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/21351" target="_blank">📅 10:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21350">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IMG_9815.PNG</div>
  <div class="tg-doc-extra">4.8 MB</div>
</div>
<a href="https://t.me/SBoxxx/21350" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali_SharifAzadeh – Podcast</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/21350" target="_blank">📅 10:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21349">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Podcast</div>
  <div class="tg-doc-extra">Ali_SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_444
🗓
September 30, 2026
✔️
دو گزارش نسبتا ضعیف اما کم اهمیت از اقتصاد آمریکا
✔️
تحلیل مواضع اعضای فدرال رزرو
✔️
دلایل عدم ثبت سقف جدید برای نفت
✔️
بررسی تقویم اقتصادی ‌روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/21349" target="_blank">📅 10:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21348">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مادر… ها!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/21348" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21347">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">— واردات خودروهای لوکس خارجی را آزاد می‌کنند — دلار برای تقاضای وارداتی رشد می‌کند — خودشان در قیمت ۲۶۰ تومان دلار را به ملت می اندازند — با پولش سهام ویران خودگوه و صایپا میخرند — مجوز را لغو می‌کنند  — سهام خودروسازها صف خرید می شود</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/21347" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21346">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">— واردات خودروهای لوکس خارجی را آزاد می‌کنند
— دلار برای تقاضای وارداتی رشد می‌کند
— خودشان در قیمت ۲۶۰ تومان دلار را به ملت می اندازند
— با پولش سهام ویران خودگوه و صایپا میخرند
— مجوز را لغو می‌کنند
— سهام خودروسازها صف خرید می شود</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21346" target="_blank">📅 10:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21345">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رسانه‌های اسراییلی ادعا کردند علت درخواست کمک، دعوا بین مسافران بوده</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/21345" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21344">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مقامات اسراییلی منتظر نظر کارشناسی کاپیتان شهبازی هستند</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/21344" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کاپیتان شهبازی:
با ۲۵ سال سابقه میگویم؛ علت این حادثه این بود که سوخت هواپیما گران شده و تصمیم گرفته شد در مقصد نزدیک تر فرود صورت بگیرد تا در مصرف سوخت صرفه جویی بشود</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21343" target="_blank">📅 10:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21342">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مقامات اسراییلی منتظر نظر کارشناسی کاپیتان شهبازی هستند</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/21342" target="_blank">📅 10:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21341">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Middle East Core</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/21341" target="_blank">📅 10:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هواپیمای «فلای دبی» که از دبی به مقصد اسرائیل در حرکت بود، در فرودگاه تبوک عربستان سعودی به زمین نشست.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21340" target="_blank">📅 10:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هواپیماربایی در مسیر امارات—اسراییل!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21339" target="_blank">📅 10:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هواپیماربایی در مسیر امارات—اسراییل!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21338" target="_blank">📅 10:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آکسیوس به نقل از یک منبع آگاه:
هیچ پیشرفت ملموسی در مذاکرات روز دوشنبه حاصل نشد و ایرانی‌ها خواستار مواردی هستند که واشنگتن نمی‌تواند آن‌ها را بپذیرد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21337" target="_blank">📅 02:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بوئینگ مسابقه F/A-XX نیروی دریایی ایالات متحده را برنده شد و با شکست دادن نورثروپ گرومن، قراردادی با ارزش بیش از ۲۰ میلیارد دلار برای توسعه جنگنده نسل بعدی ناوهای هواپیمابر نیروی دریایی را به دست آورد.
پیش‌بینی می‌شود که این هواپیما در دهه ۲۰۳۰ وارد خدمت شود و جایگزین F/A-18E/F سوپر هورنت و EA-18G گراولر شود.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21336" target="_blank">📅 01:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فردا ساعت ۱۳:۳۰ با نیما درباره آخرین تحولات مربوط به جنگ گفتگو خواهیم کرد
لینک تماشای نشست Live</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21335" target="_blank">📅 01:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تتر = ۲۵۷ هزار تومان!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21334" target="_blank">📅 00:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">روس‌ها همیشه موقع مذاکره ایران با آمریکا کرم میریزند</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21333" target="_blank">📅 00:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برخی منابع روسی از احتمال قریب الوقوع جنگ با اسراییل خبر می دهند</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21332" target="_blank">📅 00:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برخی منابع روسی از احتمال قریب الوقوع جنگ با اسراییل خبر می دهند</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21331" target="_blank">📅 23:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkeRlcqwUXv1ClVtbgnvP10kiUEAVxH1OsxMYaNYMqpN30UZJBw8Pv1xFbs7yv5wG4YJFsn3htCHcPR0EavP9OgBEbDHryA_raby5hSMgVN14Z_H0X9CHuPBlJ_4brjg8jWZf-0IG5mwlFpkz0vvoqzNfj3s--Xv2D7TNIz5qYFXJoSrSwwhzMlcwK9-Zojt0p10C0zyJpmA8wa3hvelocYAe0DxpzzVeV_LrGqEKiY55hG1r50jsdobxTYs-FtifA-ORiahTzgRVfd5iUB2AKGRi4JQPBgNeVDewMsFyr-3GNysAGn9vJLZVFNpggsn47j_XDD5q6EQ-wST8ejatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SBoxxx/21330" target="_blank">📅 22:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آغاز دوباره حملات موشکی و پهپادی سپاه به سمت کشتی ها در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21329" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اظهارات جی.دی. ونس درباره رهبری ایران:
در ایران شما جناح‌های تندرو را دارید، محافظه‌کاران، میانه‌روها و روحانیون.
و همه این افراد در فرآیند تصمیم‌گیری نقش دارند.
و البته، رهبر عالی‌مقام جدید نیز حضور دارد اما بسیار منفعل است. او در امور روزمره دخالت نمی‌کند.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21328" target="_blank">📅 20:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21327">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اعزام دو اسکادران جدید جنگنده‌های F-22 ایالات متحده به اسرائیل
خبرگزاری‌های بین‌المللی و رسانه‌های عبری از جمله i24NEWS تایید کردند که ایالات متحده در یک حرکت بی‌سابقه، ۱۲ فروند جنگنده رادارگریز نسل پنجم F-22 Raptor را همراه با ده‌ها هواپیمای سوخت‌رسان پیشرفته (از جمله تانکرهای KC-46) در پایگاه‌های نظامی اسرائیل مستقر کرده است.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21327" target="_blank">📅 20:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21326">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21326" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21325">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">باز تنگه بندها ریختند تو فضای رسانه ای!  احمق های نفهم شما تنگه ترمز را ببندید اولا چین زیان سنگینی می‌دهد و شما را برای همیشه از فهرست متحدین خود حذف می‌کند و ثانیا دو هفته بعدش، جزایر سه گانه را از دست خواهیم داد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21325" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21324">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">درگیری مسلحانه میان شبه نظامیان بلوچ  و نیروهای نظامی در ایرانشهر</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21324" target="_blank">📅 19:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21323">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">درگیری مسلحانه میان شبه نظامیان بلوچ  و نیروهای نظامی در ایرانشهر</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21323" target="_blank">📅 19:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21322">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بهترین محدوده مقاومتی = 4169 الی 4175</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21322" target="_blank">📅 19:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21321">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdwTkS_QuuKuY2VO3Vm3iMT5b8Sh_V72WLfq5oicpXYnkoYaE2H5aE-BqYBOi9NhvgsiddVMzoBpG6nH3TafhsfxSafV7_vsgVsK0_xvdDvsBhrbdXLW4hzVHJwhrOjdo3fDwlmSMOd0Hge257tKfeKyJFHE8IK_5AMXdB1sckt_SEOwwJ4yL0SBcm_Gv7DsMI7i_G9YHiIq7ecsIhO8ZI7Uq479UFUVODpImvtwkY-diKL-gA9JZ_TihwOGsJ_jaU8iVAiyYCE_zlP0-9je2aA82EpvnZ08fM2-r3mjJZd07-d7MIn7TAenITYhz5LqlBzGl9vcm9eRfyv_oU9x5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥹
🥹
🥹</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21321" target="_blank">📅 19:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21320">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنگوی ارتش ایران: اگر تشخیص دهیم که یک حمله دشمن قریب‌الوقوع است، قطعاً یک عملیات پیشگیرانه را انجام خواهیم داد. - خبرگزاری فارس.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21320" target="_blank">📅 18:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21319">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: ایران به شدت در حال شکست است و به زودی از بین خواهد رفت. قیمت نفت به شدت کاهش خواهد یافت.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21319" target="_blank">📅 18:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21318">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دیدار بن‌زاید و نتانیاهو در ابوظبی در قالبی «گسترده‌شده» برگزار شده که شامل کشورهای عربی دیگر و برخی کشورهایی که روابط رسمی با اسرائیل ندارند، بود.
بر اساس گزارش کانال ۱۴ اسرائیل، نمایندگان عربستان سعودی، مراکش، کویت، بحرین، لیبی (حفتر)، عمان و مصر نیز در این نشست که در روز یکشنبه برگزار شد، حضور داشتند.
نتانیاهو و بن‌زاید ابتدا به صورت خصوصی با یکدیگر دیدار کردند و سپس مقامات سایر کشورها به جلسه گسترده پیوستند.
بحث‌ها بر روی ایران، همکاری نزدیک‌تر بین اسرائیل و کشورهای خلیج فارس، مسائل اقتصادی و سیستم‌های دفاعی اسرائیل متمرکز بود.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21318" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21317">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس:
اطلاع داریم که کشور های عربی حاشیه خلیج فارس با تأمین مالی آمریکا و اسرائیل برای جنگی تمام عیار علیه ایران موافقت کردند و در حال فشار به روی ترامپ برای آغاز هر چه سریعتر جنگ‌ می‌باشند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21317" target="_blank">📅 17:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نامه سپاه پاسداران انقلاب اسلامی به مردم آمریکا
این دولت خودکامه، کودک‌کش، هوس‌باز و نادان را کنار بگذارید؛ امور خود را به اندیشمندان بسپارید، نه به زورگویان، و به آنها یادآوری کنید که جهان تغییر کرده است.
مردم جهان بیدار شده‌اند و دوران غارت ثروت ملت‌ها با زور و شمشیر به پایان رسیده است؛ این، قرن پیروزی اراده ملت‌ها است. ادامه دادن این مسیر غیرانسانی، سرنوشتی دردناک را برای آمریکا رقم خواهد زد، زیرا روزی که مستضعفان علیه ستمگر قیام کنند، بسیار وخیم‌تر از روزی خواهد بود که ستمگر علیه مستضعف عمل کرد.
هفت ماه پیش، ارتش متجاوز آمریکا —با نقض قوانین بین‌المللی و ارتکاب جنایت جنگی— جنگی علیه ایران آغاز کرد و با حمله به یک مدرسه ابتدایی در میناب، 168 دانش‌آموز را به قتل رساند، در حالی که همزمان به دفتر آیت‌الله سید علی خامنه‌ای، رهبر انقلاب اسلامی، نیز حمله کرد و ایشان و خانواده‌شان، از جمله نوه 14 ماهه ایشان، را به شهادت رساند. از آن زمان تاکنون، بیش از 3600 نفر —که بیشتر آنها غیرنظامی، از جمله 400 کودک— به شهادت رسیده‌اند، و هشت دانشگاه، سه بیمارستان و هشت مدرسه بمباران شده‌اند.
اگر در صحت گفته‌های ما تردید دارید، می‌توانید سفری کوتاه به هر نقطه از ایران که مایل هستید —حتی تنگه هرمز— داشته باشید تا از نزدیک صحت اظهارات ما را بررسی کنید.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21316" target="_blank">📅 15:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21315">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">علت تاخیر در ارسال GRI و FVC این بود که در نشست لایوی با نیما و امین و پیام بودم.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21315" target="_blank">📅 15:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21314">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#FairValueCurve  نمایه FVC اندکی از محدوده بیش—فروش فاصله گرفته اما حباب ندارد و کماکان زیر ارزش منصفانه است.  در این شرایط بهترین راهبرد، فروش در مقاومت ها است.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21314" target="_blank">📅 15:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21313">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aagzy0NTtM8haX2-H-wDD4zNzAykE1M5eSdQTlYrB_YlIfYRZFZkpkxlTaF0q4tuI01hGasieYv6U4Hosekfdx-3WnKR10wtebWS05GFgIBoDaUyvGcSjcLTAgrvC4Sj4xACufAi4Lc_zpNoR87-Zey8bnrEJtUhQaJSSPhx1hhTugykQ4oH316UOYkFUr4yYDdgCXPLPuHuIrJFteIIBDjwheYO93tnZMnaqtq4JUVdOxk203jAB1T1ydZB5qtwNYERSd69--0yW-6_aKqphM9TlCmOUfOVVyXqQGaqrNq0xCdCnX_H-gxm8oc5hVWBaRGU_dlE73xnOtUHmfBr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC اندکی از محدوده بیش—فروش فاصله گرفته اما حباب ندارد و کماکان زیر ارزش منصفانه است.
در این شرایط بهترین راهبرد، فروش در مقاومت ها است.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21313" target="_blank">📅 15:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21312">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSCoV_yVbEqU3sNH8hpFxlBH_s1Pf2zAgFMiNQOBna5c6VolHXSGjPNfpbFVck041600ycp15K_WexIH4mCJJt3q_0lgeQAg-QQ5zPj8PF2tNsw55eoWOIFI7ld_ovF-E3d7gztxuTkNjdpzc19S0jMDiBZVzZT2IoD-X4yondUZm8RH_0nEyhgks3YZPKXbM1M3WiBDamluqEp7w7-TrkJ8oJYKt5qTEp1hVGbusk7XTQ-T54tts-U-LyDPNeoAuQ2ooh2vNTtCR75yAVQx549gKAQxAEG59kr0fboTxk8CGWnZy983zi_3WL6xdixC-o-zwM_ja14VzEDknYd4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیکی + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و بالاهای طلا سل دارد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21312" target="_blank">📅 15:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21311">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebSbyQPxr3xpbrl2nyxisvIYmdv6AAi_1b3gIv1H_LmPW8Q2u2xlWPx82IKXd_BAx7jDidpeHqOs6jdb_tki7K8Cv3Xs2ZQHM5u8qvKtInYBM-U5EsdKuPOSCOz-VdWKPyuhlum_Pjo8LnwRNAJAJz0D9lCa4xWzAGAMDpuEBW3qpOy4ORByvkP2QRG_GxhMwAjp3Xu73EFALdcyM3r8YfiQytwNZnaT4ilURr_iu2SkGjvubUTMVAZibTOyVF0PxrGAvTxU5e88U2U4tAagWx1AlajRuzI3uuNbzdn339YKc_YQPRT074SGlMahuA-i9WmXDqNZ3kGoqQxQL4NAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش امت مبعوث به حکم حبس حاج آقا رسایی!</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21311" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حبیب‌الله سیاری، معاون هماهنگ‌کننده ارتش:
مردم جنوب آماده باشند و اجازه ندهند دشمن وارد خاک کشور بشود</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/21310" target="_blank">📅 09:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21309">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تتر = ۲۵۰ هزار تومان!</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SBoxxx/21309" target="_blank">📅 08:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عراقچی: پاسخ آمریکا به تهران از طریق میانجیان قطری منتقل خواهد شد</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21308" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21307">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نماینده امارات در مجمع عمومی سازمان ملل:
«امارات خواستار پیگیری اشغال جزایر سه‌گانه تنب بزرگ، تنب کوچک و بوموسی توسط ایران است</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21307" target="_blank">📅 01:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21306">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عراقچی: پاسخ آمریکا به تهران از طریق میانجیان قطری منتقل خواهد شد</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21306" target="_blank">📅 01:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21305">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزیر امور خارجه ایران: تهران پیشنهاداتی را با میانجیان قطری مورد بحث قرار داد تا به ایالات متحده ارائه دهد - ایرنا</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21305" target="_blank">📅 01:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21304">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اگر عراقچی به تهران برگردد یعنی دیگر مذاکرات شکست کامل خورده</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21304" target="_blank">📅 01:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21303">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ اعلام کرد که گزارش Axios مبنی بر اینکه ترامپ پیشنهاد لغو تحریم‌ها را به ایران داده است، یک "دروغ" است.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21303" target="_blank">📅 01:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21302">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLRUU_I2zNxItJRhutW_F7XbPeY1xOqpaxHg7mthLpwCdMQQeO-M3C-_Y7SZkwCmnwn9BVFDMrgCzg9Um31zBs2DE8O4eRKkna6O0M5BAOejUM3vcbptFDpkgvWlzwZHntahMacEkRyBZLNFDzDYooUbB__R89ZWOzL1WiCGobfl_gaGV2KasuBEHX94o519vmRSc719sYbX1FsoMiYpSqj4TibReDAIRGTZpt8-pVRRZBY0Ugz5JDEUYRTbk4Kj5G136fY90Gy8IuD8pwly7hKqZtqxBv6TmDK8YkaMT4bY3wE4Udld2t1UFD3rx7IWQWyND8KgOWZg8ZhhmM1vPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدای کعبه سوگند که دروغ و فریبی بیش نیست! همه اش فریب و نیرنگ ترامپ است تا زمان بخرد و نیروهای بیشتری به منطقه بیاورد!  خواهیم دید چه خواهدشد!  عجالتاً طلایمان برگردد حالا خوب است</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21302" target="_blank">📅 01:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21301">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uANDdca-6fV8P1wJCfgIOcZthJkIgMqWn8y1aUa8qYa2iM3bPZbRL7ifmfwAn38k3P6S0IgkwytSDd0SdzMQntqMv-hptCAzOPFHEMwl9_S_boFO_yjtlWpi5uUdNU3DEjASa0nHus7Oa2lQyihfyPFr6p6tDIwwAhrj6FRWn_-9S-JmML0fqZc8w2SRhHf36dI13tMuOABwVP20Lz3nVEZF6QKwiGmqwQ0PN72eJNn4elbByxYvv9zg5RaCfmy0UYKekI45sThAnbnnB_jZli6--yF8vNkrs8CCsquNRX7iFY9EmfxepAoWmHRinK9S47iBy94tlaaU3_MA1j18aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   برای اولین بار موشک خاص و ضدناوشکن ایرانی آزمایش شد  ۴۸ ساعت پیش برای اولین بار موشک ضدناوشکن ایرانی را بالای سر یک ناو آمریکایی آزمایش کردیم.  این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/21301" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21300">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ درباره ایران:  «آنها دیوانه هستند. هیچ شکی در این مورد وجود ندارد.»   «من همیشه به آنها می‌گویم: «شماها دیوانه هستید، آقایان.»»</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21300" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21299">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ درباره ایران:
«آنها دیوانه هستند. هیچ شکی در این مورد وجود ندارد.»
«من همیشه به آنها می‌گویم: «شماها دیوانه هستید، آقایان.»»</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21299" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21298">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:  فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.  بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21298" target="_blank">📅 22:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21297">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:
فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.
بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود ندارد که ایران یک نیروی شرور است که بریتانیا، منافع ما و متحدان ما را تهدید می‌کند.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21297" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21296">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">احتمالا امروز ترامپ خواهدگفت مذاکرات خوب پیش می رود</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21296" target="_blank">📅 21:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21295">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بخدای کعبه سوگند که دروغ و فریبی بیش نیست! همه اش فریب و نیرنگ ترامپ است تا زمان بخرد و نیروهای بیشتری به منطقه بیاورد!
خواهیم دید چه خواهدشد!
عجالتاً طلایمان برگردد حالا خوب است</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21295" target="_blank">📅 21:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ایران با توقف غنی سازی موافقت کرد!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21294" target="_blank">📅 21:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE5rGpX1OsCsffabCWrulCd200GxrK3E5H9I9jXtjbgepFbIjykYLIv7IKwEDgqberN3CdQ3jUZq0R3ho3bivI1AqoGJo4-DR31gdYgl5L-ReAPTyebiqzzpRjkBcNHn4uT-9VgfT8H8H8AeZOGC3rPuI47of_1DzEKp7T2KDaoeYnVZ6r25oVm5TnAWOO0SsaYhdPUU2Wa7U-jxRaLaipVuVoB2SKF9-Bp7i_RSSpdy7RfCgBFHNqwYQkrVFtR0rsesmpWlwPznttvo07FdhdpiswGQ6lcOlg3Sm7TxucMKlEKNbqciGqPDuE7t3V58y--jO8Ihh6jK64BRmXIlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران ارزشی تازه دارند می فهمند چرا دکتر پزشکیان آن روز در سازمان ملل از ماتریکس خارج شده بود!
یا ذی الجلال و الاکرام!</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21293" target="_blank">📅 20:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21292">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">در ۲۴ ساعت گذشته، دو اسکادران جنگنده آمریکایی به پایگاه هوایی اوودا نیروی هوایی اسرائیل در جنوب این کشور رسیدند و به نیروهای آمریکایی دیگری که از قبل در این کشور مستقر بودند، پیوستند.
مقامات امنیتی اسرائیل اعلام کردند که این استقرار بخشی از تحرکات گسترده‌تر نیروهای هوایی آمریکا در سراسر خاورمیانه است و نشان‌دهنده آمادگی بیشتر یا تشدید تنش با ایران نیست.
یک منبع امنیتی گفت که حضور نظامی فعلی آمریکا همچنان بسیار کمتر از سطح نیروهایی است که قبل از عملیات «خشم حماسی» (Operation Epic Fury) در این منطقه مستقر شده بودند.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21292" target="_blank">📅 20:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21291">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗
عربستان سعودی پس از تعمیرات، صادرات نفت خود را از طریق خط لوله شرقی-غربی از سر گرفته است</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21291" target="_blank">📅 20:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21290">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دیدید؟! این کله زرد حرامزاده را من بهتر از پدرانش میشناسم!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21290" target="_blank">📅 20:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21289">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش‌ رسانه‌های عربی از شلیک موشک‌ از خاک ایران</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21289" target="_blank">📅 19:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21288">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترکیه یک هواپیمای ایرانی را به دلیل تحریم های آمریکا توقیف کرد.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21288" target="_blank">📅 19:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21287">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کار طلافروش آنلاین به شورای عالی امنیت ملی رسید  پلتفرم فروش آنلاین طلای میلی‌گلد در نامه‌ای به محسن رضایی، دبیر شورای عالی امنیت ملی، خواستار صدور دستور فوری برای رفع محدودیت دسترسی به طلای کاربران در خزانه‌های بانکی شده است.   این پلتفرم می‌گوید محدودیت‌های…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21287" target="_blank">📅 18:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21286">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnSud1AVFCjNSkJL9XsFS9rg5imdjdLdfMdSzQRA0CH7txnTazMO_q-XWGg1qmjIpyokaaFud7xCntYgL5mIT-a1uabVp-fJbsP52JCp8NB044ct1MUBg00b5je5Uy0Sl5FimKKjmvx1jiGlKtycQBh8Hc2J_HZ2B7C4ORiJmekFu-Fd_fvB2-eVDApy0FanE1WGuQ5z5SB8j1HuiMpQ2xgMFfjdNtxzAx8HKaqGsCTQNMzlCpNOSUblZh2iXhSD2LrVGHhQ2_Nye32GoZKjc5rBy_JPPehu-uEI7dUHcDlzjSZfSRdn5vn4TMP7DEepANsYrH-Xj1WxeQkVz1p8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
صادرات نفت خلیج فارس به ۸۰ درصد سطح پیش از جنگ رسید
🔹
خاویر بلاس مدعی شد: صادرات نفت خام عربستان، عراق، کویت، امارات، بحرین و قطر با کمک نیروی دریایی آمریکا، به ۸۰ درصد سطح پیش از جنگ بازگشته.
@khate_energy</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21286" target="_blank">📅 17:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21285">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21285" target="_blank">📅 17:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21284">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فوری | فرماندهی مرکزی آمریکا:   ایران کنترل تنگه هرمز را در دست ندارد؛ شواهدی مبنی بر عبور بیش از یک میلیارد بشکه نفت در طول چند ماه وجود دارد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21284" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21283">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فوری | فرماندهی مرکزی آمریکا:   ایران کنترل تنگه هرمز را در دست ندارد؛ شواهدی مبنی بر عبور بیش از یک میلیارد بشکه نفت در طول چند ماه وجود دارد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21283" target="_blank">📅 15:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21282">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام تند آیت الله خامنه‌ای:   دشمنان جرأت ورود به خلیج فارس را ندارند  رهبر جمهوری اسلامی ایران، در بیانیه‌ای اعلام کرد نیروهای دشمن جرأت ورود به خلیج فارس را ندارند.  او همچنین گفت دریای عرب به‌زودی از حضور «دشمنان» پاک خواهد شد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21282" target="_blank">📅 15:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21281">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هیچ کس را امین تُِن های ماهی تان قرار ندهید.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21281" target="_blank">📅 15:38 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
