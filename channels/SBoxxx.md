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
<img src="https://cdn4.telesco.pe/file/CU0HsoIjcnpgLaI2qR9Vpb6fNscKa7SN5ozPBbOZdisVBY-8Zl_Zeq5PDXBppymM6TNtpi23tpTCqKeb9pRnjU6d2VezY3_CGEvCwzH6ps-QXQEIM8uPdfo-BsSt6h9l0qPN2-WKFtLBg-tOAmWe6FXXb-HqsF97yPx7P2ABCIp2x2Rnf1rCmzLuBnQWlASKxn5vSgaLKWg3sC3sWwaDI7qw9A7UkoVSMlBgaQ093lKP-7xRXVKEomWg3289D5YjL6376KcCwcv2QG99PhHZq1UZ_431BZUAq-fYbFAJYjg_yHE7Ov32HycvMFM_xkZ7Ik3PJz1dBvOBdoqr39TUEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 19:05:31</div>
<hr>

<div class="tg-post" id="msg-21001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMPPr8PcmrVbXW89MLPXrkAVo3L_VreNm1B6Pl-nQrNNidsyRGS7EaVjXr8hpPYzBiXn6N_Q1hywmyQe-dZJT6hSqa7Iosnzg4dRr8c4iVpGVlvB21loysgZ93MI_zjsCUHtUthzAQMK2_eiTIOr8gWmrz5YcSx3AOHneEq9SVL_rk7TSwi38cPCSV8B-X5KoWhytkgfbX1knHv3YnQiLkhHub4O5jyULvV3km9TL1ypFAaDwkTDslBPq15IQpKZljdxgWxmeHF9eNoRFOt6TaOzY1NbF6RkEMPcuGzK7bMFE_eXDZG5FIvnVL4CYtk-9QprjKq0V8EN7cn2zlStvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت نتایج احتمالی انتخابات میان دوره ای پیش رو در آمریکا</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/21001" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">WW3 is loading....</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/21000" target="_blank">📅 16:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20999">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/20999" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20998">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:   دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/20998" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20997">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/20997" target="_blank">📅 14:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20996">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qggfcxyByXbfb1fGnwbNZj9oT-JCzBfrxQHMNLHEQrI_gcUFWVzLibsHFDQktir3jda49Y0w7IpkhkvxiR03PUdSJrgTLXQKDzWaIxG2y2J-xm_jP0gcDa0gkXkFiqPs0KKku_u-8_weKaCSMeLLL9GiwEBhc9rnA19BWF_6kaGKrFljvL8lTbwLN83JSNPlV2yuyJ3AQLGwrOnMz9F4pouu7xOQ4OY8fT3b4JuLdtiR-zWGgV9F8TN_k5xm_qfn3fTMsYtacgbFSF_VCTsd3pDF-6V2dtBknuVBva24RP-7OHgN099OS18dnY9XWGbWgq2K9hNrlySmxFSGLsGNRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش های موثق، ترکیه چندین پهپاد رزمی و شناسایی برای کمک به سعودی ها در جنگ یمن ارسال کرده که دستکم یک پهپاد کارایل توسط حوثی ها سرنگون شده است.</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/20996" target="_blank">📅 12:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20995">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترکیه مجوز فعالیت بانک ملت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20995" target="_blank">📅 10:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20994">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آمریکا بسته دفاع هوایی ۲.۶۸ میلیارد دلاری برای اوکراین را تأیید کرد
وزارت خارجه آمریکا
فروش تجهیزات و پشتیبانی دفاع هوایی به ارزش
۲.۶۸ میلیارد دلار
به اوکراین را تأیید کرده است.
این بسته شامل
سیستم‌های دفاع هوایی برد بلند، پرتابگرهای متحرک، رادارهای ضد پهپاد، قطعات یدکی، نرم‌افزار و پشتیبانی فنی
است.
اوکراین هزینه خرید را از طریق
کمک‌های مالی اروپا
و
کمک‌های نظامی خارجی آمریکا (FMF) که قبلاً تخصیص یافته بود، تأمین خواهد کرد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20994" target="_blank">📅 08:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20993">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حمله موشکی حوثی ها به ریاض پایتخت عربستان</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20993" target="_blank">📅 06:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">منابع خبر می‌دهند آمریکا و دانمارک به توافقی درباره گرینلند نزدیک می‌شوند.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20992" target="_blank">📅 01:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20991">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منابع خبر می‌دهند آمریکا و دانمارک به توافقی درباره گرینلند نزدیک می‌شوند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20991" target="_blank">📅 00:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20990">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGfh2jfphiBLL_PB_tSz0SKvVKc40zBGN4P5KJUNtApv0QdNdqsovzSo8XhCziWBrOByxu1HbHnau4Pd9tqYpVV33jaEwc4Y_TJMuf9Ia5Tpl-lOpjXZ-m7Z5DE2lVSKWtPKP7XecDw6BHvgQQOcYucCx9rWG8a2AIIvD77o5aqxyaB39nxLTMwlyralZRtGQ2udbMTVhL5BSz2Hkwi4Ove-uUQpuUAG6ML8LuWEu5pAZ0uATdb5Ei4FBsY09kMf6GO8uzXXkjJihPxGW-b5qljeX3J9MwO-XRMY7HVwrXaVNYb5N_Xo8rYyYIKpJjDucvR6uOybMx6w7jpjWDW1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلامتی همه پورن استارهای وطن پرست!</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20990" target="_blank">📅 00:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20989">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAeX5rujRynb0gzDo8MkAViPE7Yx1lpj-viug-lgOmyCm8H-AxveBJMJG44B4NJEpavr63BDbWjq90YG8KD4UrE4CegC25xqrweI9kl_K70gtNzbRa9jPWz3Cc_NDr8XSaNGF4nlkUSB-59Ge4I-2Bmm3V5aR_qCtp-RCy1WG0R5_seT4E0F3zZJHiN1XcVjH95ck2Koy_4gGbDDirzS1uV6YKtj6rt47P--OLPVR5-AdFQ6OLKCg8Jp-FUiRBEAnnhYZrSb86rm_-FavziorsW1J3bt_waFQF5pkkGYX4x2OJvL3iw1P2MVQcGfJt-boiSwNmcVOsesBtXELmSDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثی ها قشنگ دارند خاطرات کتاب های دینی راهنمایی و دبیرستان را برایمان زنده می کنند!  فکر کنید اگر این دوستان ما نبودند چطور یاد طائف، مکه، مدینه میفتادیم؟!  همه شان را زدند.  یا ذی الجلال و الاکرام</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20989" target="_blank">📅 00:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20988">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNIDDzdjotcHDMeHH3qFM1X951Kom_BO06l4mPBhGW59XH1KVVSB25lqVz8QfT6ZLkOnNmAHUADXAgj_eQzI_aahAfrgoPedrUxrsJq-d7gQA1L-DolEmk5P5WRYGPxAQQ8kFUcFQooUdFd6ivG1aXaX_kXpqW2uOCuldsMEXHMnaSsAS0GQy3CcMBrCseGcNkBvPoXmq3v8AgUsqkzP-DvTwxUZQp_JFQmyDtwquTyE_JjCeu3Nu6j4Ganb3crJgO6q303MYapiMzw_htJ0o-eDfyOcTTnCvoFXVOSh14kHFZXvHgSzDfQA87O_qYotXXVcolz5H73HGqraFLnRwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته‌ی شش مقام آمریکایی که با اطلاعات داخلی وزارت دفاع در مورد آمار تلفات آشنایی دارند، تعداد سربازان آمریکایی که در خاورمیانه و در جریان جنگ جاری با ایران جان خود را از دست داده‌اند، بیشتر از آن است که پنتاگون به طور علنی اعلام کرده است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20988" target="_blank">📅 00:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20987">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حوثی ها قشنگ دارند خاطرات کتاب های دینی راهنمایی و دبیرستان را برایمان زنده می کنند!
فکر کنید اگر این دوستان ما نبودند چطور یاد طائف، مکه، مدینه میفتادیم؟!
همه شان را زدند.
یا ذی الجلال و الاکرام</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20987" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20986">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجار در طائف عربستان!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20986" target="_blank">📅 00:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20985">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20985" target="_blank">📅 23:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20984" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">العربیه:
وزیر کشور پاکستان طی ساعات آینده به تهران سفر خواهد کرد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20983" target="_blank">📅 18:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20982">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران
انقلاب اسلامی ۴ موشک کروز ضدکشتی به سمت تنگه هرمز شلیک کرد</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20982" target="_blank">📅 18:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20981">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB5Cg-eEQgOkg0qFM0MvBZQM42Z5VsJUweXKN_i1x5bynyK4jGFKdFkMfQSXvWjQ_HvkJqk9LwxvDUYOYD7CPNEAnFXU5rtheG0grglrKpChq61tQ9m1aK3PmPJBZnQdMLumYv3a9st2L8qp9FK6lMqPVjgV9bjtX4p8dB-KMcCtICWNSaMmL0kuqz4atl0Khnh0QvRA2dNUq5B6HEg7z6PYU5iRx__dhvhTPsGEwIRq6dNin62N_vaBQU4_-cROEQu3DLpbrkPadn48hlrSBoJYJGGv8fgJ3yrKyO6_D1hklFNG-JjQXex7XFFTyeLFCjjwBkZBZdVcnOGuSM1r7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیه دکتر پزشکیان به جانفدایان:  کمتر مصرف کنید!  (پسر پزشکیان هم دیروز همین را گفته بود)</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20981" target="_blank">📅 15:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20980">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=uHLaS6-gG5yneDm0kDpC7GK10hUdPkWFmq_w_k6AWN2FvEdvxPE7Xzeo-6jjakhDETSU80dbi1m7oyrnLoEm4SaXVLFPuiAD_qFsuZNsCdWFyUMpPrWlL58zuFt6xQ6f21b6237DjKnU03jQMVxBeYzW1reRydBeIUCLxyxz2EGx-UDpA15i8POP3YSrxELik1dfnQIQfG5tsFFpWxjRBJw1a9GRQp7YdvevOiVG9oZWt3qRFTPBSondVj6V7KoqU-wYc1bcs57W3feFH0OQROfBs-OJusvo_H56TURHevCPRy034CSnN_R1ZVDC53PJ75V38Pj4FeoG-hndHthENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=uHLaS6-gG5yneDm0kDpC7GK10hUdPkWFmq_w_k6AWN2FvEdvxPE7Xzeo-6jjakhDETSU80dbi1m7oyrnLoEm4SaXVLFPuiAD_qFsuZNsCdWFyUMpPrWlL58zuFt6xQ6f21b6237DjKnU03jQMVxBeYzW1reRydBeIUCLxyxz2EGx-UDpA15i8POP3YSrxELik1dfnQIQfG5tsFFpWxjRBJw1a9GRQp7YdvevOiVG9oZWt3qRFTPBSondVj6V7KoqU-wYc1bcs57W3feFH0OQROfBs-OJusvo_H56TURHevCPRy034CSnN_R1ZVDC53PJ75V38Pj4FeoG-hndHthENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اروپایی بودن همین را فهمیده که یک لامپ را خاموش کند!  در حاکمیت قانون و مدیریت عقلانی و کرامت انسان هم اروپایی بشویم یا نه؟!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20980" target="_blank">📅 15:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:  امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏   ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20979" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20977">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:
امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏
ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20977" target="_blank">📅 14:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20976">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یادداشت بسیار مهمی است و نکته اصلی اش این است:
جهش بهای نفت و افت قیمت اوراق قرضه به تنهایی موجب تسلیم شدن ترامپ برای پایان جنگ نشده و احتمالا هم نخواهدشد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20976" target="_blank">📅 14:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20975">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جی‌پی مورگان از تلاش برای پیش‌بینی پایان جنگ ایران و ترامپ دست کشید
جی‌پی مورگان اعلام کرده است که دیگر برای جنگ ایران یک
سناریوی پایه (Baseline Forecast)
ندارد؛ چراکه قیمت نفت، بازده اوراق خزانه‌داری آمریکا و قیمت سوخت از سطوحی عبور کرده‌اند که این بانک پیش‌تر انتظار داشت عبور از آنها واشنگتن را به سمت دستیابی به یک توافق پایدار سوق دهد.
عبور از خطوط قرمز اقتصادی، به خروج از جنگ منجر نشد
در آغاز جنگ، جی‌پی مورگان بر این فرض بود که افزایش فشار اقتصادی در نهایت دونالد ترامپ را به سمت توافقی برای بازگشایی تنگه هرمز سوق خواهد داد.
مهم‌ترین آستانه‌هایی که این بانک در نظر گرفته بود عبارت بودند از:
• نفت بالای
۱۰۰ دلار در هر بشکه
• بنزین در محدوده
۵ دلار در هر گالن
• بازده اوراق خزانه‌داری ۱۰ساله آمریکا بالای
۵ درصد
شش ماه بعد، چند مورد از این سطوح شکسته شده‌اند.
ناتاشا کانوا، رئیس استراتژی جهانی کالاهای جی‌پی مورگان، در یادداشتی در روز پنجشنبه گفت:
«شش ماه بعد، بسیاری از این خطوط عبور کرده‌اند، اما استراتژی خروج نه‌تنها روشن‌تر نشده، بلکه مبهم‌تر شده است.»
او افزود:
«برای نخستین بار از زمان آغاز درگیری ایران، ما دیگر دیدگاه پایه‌ای نداریم. واقعاً نمی‌دانیم پایان این جنگ را چگونه مدل‌سازی کنیم.»
هیچ نشانه روشنی از کاهش تنش وجود ندارد
جی‌پی مورگان معتقد است شواهد چندانی وجود ندارد که نشان دهد واشنگتن یا تهران در حال آماده شدن برای عقب‌نشینی هستند.
به گفته کانوا، هرچه درگیری به جای کوچک‌تر شدن، گسترده‌تر می‌شود، دفاع از این دیدگاه که اختلال در عرضه انرژی کوتاه‌مدت خواهد بود، دشوارتر شده است.
در همین حال، عربستان سعودی پس از آسیب دیدن خط لوله در پی یک حمله پهپادی که از عراق انجام شد، خط لوله
شرق–غرب
خود را متوقف کرده است.
همچنین شبه‌نظامیان حوثی همسو با ایران پیشروی‌هایی داشته‌اند که می‌تواند موقعیت آنها را در زمینه کنترل یا ایجاد اختلال در تردد نفتکش‌ها در بخش جنوبی دریای سرخ تقویت کند.
ترامپ نیز روز پنجشنبه به Axios گفت که در آستانه تصمیم دیگری درباره این موضوع قرار دارد که آیا عملیات نظامی گسترده علیه ایران را از سر بگیرد یا به سمت پایان دادن به جنگ حرکت کند.
ترامپ گفت:
«یک تصمیم بزرگ پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آنها [رژیم ایران] را نابود کنم یا نه؟ این یک تصمیم بزرگ است. هر اتفاقی ممکن است از سوی من رخ دهد.»
بازار نفت، کاهش بیشتر عرضه را قیمت‌گذاری می‌کند
جی‌پی مورگان ارزش منصفانه نفت برنت را حدود
۹۰ دلار در هر بشکه
برآورد می‌کند، اما شاخص بین‌المللی نفت اکنون نزدیک
۱۰۵ دلار
معامله می‌شود؛ در حالی که در اوایل این هفته به محدوده
۱۱۰ دلار
نزدیک شده بود.
این بانک محاسبه می‌کند که به ازای هر
یک میلیون بشکه در روز
کاهش عرضه نفت، حدود
۴ دلار
به قیمت قراردادهای آتی نفت اضافه می‌شود.
بر همین اساس، کانوا می‌گوید بازار در حال قیمت‌گذاری ریسک از دست رفتن حدود
۴ میلیون بشکه در روز عرضه اضافی
است؛ آن هم علاوه بر حدود
۱۰ میلیون بشکه در روز
عرضه‌ای که هم‌اکنون دچار اختلال شده است.
تصویر کلی بازار انرژی با حملات اوکراین به پالایشگاه‌های روسیه نیز پیچیده‌تر شده است؛ این در حالی است که ترامپ روز دوشنبه گفته بود کی‌یف و مسکو توافق کرده‌اند حملات به تأسیسات انرژی را متوقف کنند.
ذخایر نفت همچنان یک حائل ایجاد می‌کنند
مهم‌ترین عامل محدودکننده برای افزایش بیشتر قیمت نفت، حجم نفتی است که همچنان در ذخایر نگهداری می‌شود.
ذخایر تاکنون
۵۵۵ میلیون بشکه
کاهش یافته‌اند؛ رقمی که به‌مراتب کمتر از کاهش
۱.۶ میلیارد بشکه‌ای
است که تیم کالاهای جی‌پی مورگان در ابتدا پیش‌بینی کرده بود.
بنابراین بازار در برابر یک شوک طولانی‌مدت عرضه، نسبت به برآورد قبلی بانک، همچنان از
حاشیه امنیت بیشتری در ذخایر
برخوردار است.
کانوا در جمع‌بندی گفت:
«خلاصه اینکه، فعلاً هنوز به اندازه کافی ظرفیت ذخیره و عرضه پشتیبان وجود دارد که قیمت‌ها را مهار کند.»</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20975" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20974">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خلیل شیر غلامی، سفیر ایران در ارمنستان؛    «ایران رویکرد ویژه‌ای نسبت به مسئله تمامیت ارضی و حاکمیت ارمنستان دارد و این را یکی از مسائل حساس خود می‌داند. با توجه به اهمیت منطقه سیونیک به عنوان یک مرکز استراتژیک برای ارمنستان، به ویژه در زمینه حفظ ارتباط با…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20974" target="_blank">📅 11:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20973">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خلیل شیر غلامی، سفیر ایران در ارمنستان؛
«ایران رویکرد ویژه‌ای نسبت به مسئله تمامیت ارضی و حاکمیت ارمنستان دارد و این را یکی از مسائل حساس خود می‌داند. با توجه به اهمیت منطقه سیونیک به عنوان یک مرکز استراتژیک برای ارمنستان، به ویژه در زمینه حفظ ارتباط با ایران، هر پروژه‌ای، از جمله پروژه TRIPP یا هر طرح دیگری که تهدیدی برای ارمنستان یا روابط ایران و ارمنستان محسوب نشود، از نظر دیپلماتیک، مشکلی ایجاد نخواهد کرد. در اجرای هر پروژه‌ای، تمامیت ارضی و حاکمیت ارمنستان نباید به خطر بیفتد.
علاوه بر این، حضور آمریکایی‌ها در مرز ارمنستان و ایران نباید تهدیدی برای ایران باشد.
اگر این دو شرط محقق شوند و همچنین منافع ارمنستان در نظر گرفته شود، ایران مخالف اجرای پروژه TRIPP نخواهد بود.»</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20973" target="_blank">📅 11:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20972">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20972" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20971">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">طنز تاریخ در این است که پیمان دفاع مشترکی که عربها با ترک‌ها بسته اند دقیقا ۱۱۰ سال پس از جنگی روی داده که میان خودشان در قالب شورش «شریف حسین» ضد عثمانی ها درگرفت و اتفاقا نخستین شهری که عربها آزاد کردند همین «مکه» بود که نامش اکنون شده لقب پیمان دفاعی اخیر!…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20971" target="_blank">📅 11:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20970">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjun6k54FA5xEShoWtC6IrU3WyTuyJIVH3smSTraJxnyeZC1JYXbfZvQRpiLtkeD2zEcf6ktEvORfo8rm0X6R6cp1VPB_kK3OgEIlOWNxTsn6K6e_e9kpfQKEn4vAFOoXLwmaxBw5RJyEdJjPaxlT-Qyeg0FQcX_BEFZfnxM9xoOx5DzTo-s8rxlce0iNZlL9ewGx8ktbuwUI0LORFOPjJz9LeMUmSucWQDfsgAqsdT_DExPjqDD6cTGqoZ8E7E7lEOawZjqPTwiONvK8m9cyF-Cj2fpbI75QJJ9fke5gCV4D5DaxNy1IDvSZrOSjJg1eZW2QzE-wUftr3ZUoC8h2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.
پس بهترین استراتژی برای امروز:
خرید پس از یک اصلاح سنگین 400 پیپی است.
محدوده های پیشنهادی:
4366
4355</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20970" target="_blank">📅 10:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20968">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxP_g5dIaMH1OAvsbc7-foAxd471MT69Ri4m7puXMfJzOHLMSuXkQaYudDBSgjXMAjZxtS-lE1vYiqLAy52Tlofx9Q0ioYu6goKfF8lI0otW2_FZPdd9gzQMGu_Scr_JrfxlBspTtEmjFzjnipQX_ZSuFaA0gDS83PsgLl78sYw4LOxBuOwx27hsaKpND_Kxc8bqsG8clg_wnJqa6KmorU72O02eKssHRJyf8y1hBTPhGHYOs6y-nhzF1XZ9QJ7eZhbEh3NVLrqRK8IJw46GWbRUFEXLhc8GrQi5VhVtfRZIiFgf5DK7ni3w9CGwNQDEj48FmfOjeBDOxrAfnESBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد و انتظار یک اصلاح نزولی قابل توجه (دستکم 400 پیپی) در طلا داریم.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20968" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20967">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر دانشگاه تهرانی ها</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1dc786c4.mp4?token=WI_q9dNd6fRiPoNq5hNUuP_Y4Frd6nEodazaE1JZ9aHVacyuxneA3tX7AjWR2McszbVSa5pn5aI92qRe87HuOAP0CNE_NifGG6LaZHLZ_1biU65Pab3jKNbi7nAtv0uAbnPTIm99C7WFn20HhMC2HRBEJ8bqx2qL-D0g4gEsSQtoWygsNarGZg8VAs5X6ikbHYOwH8oAUPZSQ3u5Zx6j-HsE8eI1KOvrNf-jD7MNHX9if7xfrlZFb_Y_JAARy4-APH-QfVuoi9H59h7xteuxqTIZL0ue5FKOSp1V-MesgCcFbsd30g2lwcZNQ9vJFIGeUxWNCPbQgDg8JzWAJWyqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1dc786c4.mp4?token=WI_q9dNd6fRiPoNq5hNUuP_Y4Frd6nEodazaE1JZ9aHVacyuxneA3tX7AjWR2McszbVSa5pn5aI92qRe87HuOAP0CNE_NifGG6LaZHLZ_1biU65Pab3jKNbi7nAtv0uAbnPTIm99C7WFn20HhMC2HRBEJ8bqx2qL-D0g4gEsSQtoWygsNarGZg8VAs5X6ikbHYOwH8oAUPZSQ3u5Zx6j-HsE8eI1KOvrNf-jD7MNHX9if7xfrlZFb_Y_JAARy4-APH-QfVuoi9H59h7xteuxqTIZL0ue5FKOSp1V-MesgCcFbsd30g2lwcZNQ9vJFIGeUxWNCPbQgDg8JzWAJWyqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهریار میگه آدمهای پیشه‌وری بچه‌های گرسنه تبریز رو جمع میکردن و می‌گفتن: « بچه‌ها بگید خدایا نان بده». نان نمی‌آمد، سپس می‌گفتند «بچه‌ها بگید
#استالین
نان بده» و نان می‌آمد.
اینها علاوه بر بی‌وطنی چقدر کثیف و کودک‌آزار بودند که با روح و روان بچه‌های گرسنه آذربایجان بازی می‌کردند
_sheshgalani_
@uttweet</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20967" target="_blank">📅 09:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20966">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خریداران جهانی سوخت روسیه در برابر لایحه تحریم‌های ایالات متحده مقاومت می‌کنند
پولیتیکو گزارش می‌دهد که واکنش جهانی به لایحه تحریم‌های روسیه که به تازگی توسط کنگره تصویب شده، سریع و شدید بوده است:
مسکو هشدار داد که این لایحه تنها جنگ علیه اوکراین را طولانی‌تر خواهد کرد. هند قول داد از منافع خود دفاع کند و پکن در برابر آنچه آن را «حاکمیت گسترده غیرقانونی» نامید، مقاومت کرد.
این لایحه که هنوز به امضای ترامپ نیاز دارد، تحریم‌هایی علیه رهبری روسیه، بخش انرژی، صنعت دفاعی و شبکه حمل‌ونقل که سوخت‌های تحریمی روسیه را جابه‌جا می‌کند، الزامی می‌سازد. این لایحه همچنین به ترامپ اختیار می‌دهد تا تعرفه‌های ۱۰۰ درصدی بر ۵ خریدار بزرگ جهانی این سوخت تحمیل کند؛ بندی که از پیش متحدان خود واشنگتن را نگران کرده است.
از سال ۲۰۲۲، چین ۵۰ درصد از صادرات نفت روسیه را خریداری کرده، هند ۳۷ درصد، ترکیه ۵ درصد و اتحادیه اروپا ۵ درصد. اتحادیه اروپا همچنین در آن دوره بزرگ‌ترین خریدار LNG روسیه (۴۹ درصد) و بزرگ‌ترین خریدار گاز لوله‌کشی روسیه (۳۲ درصد) بوده است.
از سوی اتحادیه اروپا، منتقدان لایحه استدلال می‌کنند که این لایحه اختیارات بسیار زیادی به ترامپ می‌دهد؛ یا برای ایجاد استثناها و معافیت ها برای شرکای بزرگ روسیه مانند چین که واشنگتن به دنبال گسترش تجارت با آن است، یا برعکس، برای اجرای انتقامی علیه متحدان ایالات متحده که ترامپ از آن‌ها خوشش نمی‌آید، مانند اتحادیه اروپا، با استفاده از خریدهای نفت و گاز کشورهای عضو تکیه‌گاه (اسلواکی، مجارستان) بهانه می سازد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20966" target="_blank">📅 09:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20965">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به گزارش برنا، در نخستین ساعات بامداد جمعه ۲۷ شهریور در محدوده خیابان دانشگاه زاهدان تیراندازی رخ داد که این خبرگزاری دولتی آن را «حمله به یک ایست بازرسی» توصیف کرد. برنا اعلام کرد در جریان این تیراندازی یک مامور نیروی انتظامی کشته شده است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20965" target="_blank">📅 08:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20964">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
نیروهای مسلح ایران به آمریکا درسی خواهند داد که هرگز فراموش نخواهد کرد</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20964" target="_blank">📅 01:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20963">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حمله ایران به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20963" target="_blank">📅 23:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20962">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک کشتی ترکیه‌ ساحل اوکراین توسط پهپاد مورد حمله قرار گرفت.
بر اساس اطلاعات اولیه، کاپیتان و یک ملوان کشتی در این حمله کشته شدند و ۱۳ نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20962" target="_blank">📅 22:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ساعتی قبل وزارت خارجه آمریکا قصد دولتش برای فروش ۴۸ فروند جنگنده F-35A به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را به کنگره این کشور اعلام کرد.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20961" target="_blank">📅 21:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:   من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20960" target="_blank">📅 21:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:  طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20959" target="_blank">📅 21:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:
طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20958" target="_blank">📅 21:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20957">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20957" target="_blank">📅 21:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20956">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20956" target="_blank">📅 20:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20955">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ:
تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است.
هر احتمالی از جانب من وجود دارد.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20955" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20954">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">— اسرائیل و یونان یک مانور دریایی مشترک برگزار کردند که شامل تبادل خدمه و آموزش برای سناریوهای مختلف، از جمله شرایط اضطراری بود.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20954" target="_blank">📅 20:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20953">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ:
من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20953" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#FairValueCurve  شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.  در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20952" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نخست‌وزیر اسرائیل، نتانیاهو، می‌گوید که اسرائیل رژیم ایران را سرنگون خواهد کرد.
«این رژیم سقوط خواهد کرد.»</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20951" target="_blank">📅 16:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20950" target="_blank">📅 14:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke7hsor1FymGcsuR8dKEdJHUBlsRGj-onGcEZKWRH-e9pHtvlftmA9WBBAqS8ki1-7CPzvEOVpQDAbVL4JIXYhyOCPMbq2daAzqj0yHT9Ap57yFHDwnAromPgU7aBl5BZVrnEkwuywrQb7Y3SPehErNtlw_Wfmb_6zqdhe8M94sv7CnNt-5-IDl3_S195VHg0-4JV6dSkhD1ItAjIenU7fjo-IOnoBWGslh5c7eTge9ru4JWBYakRBEjK6j6UHys6j6Ya38g9QVfo3IysNHCuXLs3oQG7Us8Kr-L365GTVxzit9trhYCnSd_hHDCqmwr9HB3UJsf4KFFLa6olvE6qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.
در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20949" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMqjTCkL-PaQf1I7G9pALnbJKui_QwKTDroj3W4NcdWfLTGMhh_G3PcYr3fS1KVRV4tDM8GNlX0g29aRTut3q8b1P8wXD8Dpecigejm3VTez_0P_7jxS52IrOF8WesJC23fsvuZwjJfUEButdDoiTb-G9nkVFuGR1-tfTvIICOZWivf5hsfG4Mht0oBI0FJ6Tv-UVXTjMnbnb2iU7nVv5fxP6wo3IOUR2QZbBrkUJbsmFxOooQJ1EDSzObrav8aBmS3YipE_ThA7NH4eeQoQSm5V8aTNsem0a3pJGPWPohFUKs2_Y_Sf_2pUZCuRlNIm-fDBDsZXQRKjzyMuRnevyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و انتظار می رود یک اصلاح نزولی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20948" target="_blank">📅 11:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20947" target="_blank">📅 11:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o21AOL0NLuEnmO2c2AHV_ULomK8GXgejIac401b8UoprXF9qFOpYYdvQD3D3cE3DRoWrH-WWilunaPVoiRq9XEpozSARXkKEH-eVPu6PRB-h4owYTdXAN2EAYRlncR7z-sKss2UCWgmp29ef_2YWiTbaGsftx6yJgqYLW0aSBF3fYQsXF_bRzOpJ7EIZbfcrn9ps1OUMCyJhFBaWvlgISUJEMVDmEDw8cuVatFdk9pCEOjXhm9oBg6u1Z1E1IhArKyaQgBxaPScyvHb72bby9XYT5NVfY9M9Gaq1sHxWzNpELM6evdYIOVFSdrR7x-cjKizjK5-cS9EhF1Op_EoprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین توییت برگ افکن دکتر قالیباف</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SBoxxx/20946" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شروع شد:  اخبار فوری: کاخ سفید افزایش نرخ بهره فدرال را «مایه تاسف» خواند</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/20945" target="_blank">📅 00:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20944" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWDIGjjAsul4sXSPFo63BJ6HPBQolZbGRw_CuB4HnbQ-yU3vzNRgPkvgYxz2qop7Ri58pplKXdV6B-Ode9Ky4Al6lT04ebskX01CIO3LhfWnSMdmK3lf4PagWlJ3SzUecHSnUz1Ex0p62ovKVRH5MeV7fgNiwRSgbiiCTMaOY5WnHba-iyN3FPfxnQT3VSjmN2a60rcGbotX9xmylzvvR7jJbtPwghbRq7M8QUGrlrB1vNbBloIfSgjmep2iOcGwraBGAiltFSiEH5lnx7SAdPv2-0yESl0OBp9byiPW5dTwAzv1wvgxh65Eh2ktS-83jsqjEIX1loE2TUB5XMadhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پوزیشن دیشب برای همراهان ما ارسال شده بود.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/20943" target="_blank">📅 23:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/20941" target="_blank">📅 23:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXUtozPmNhBmbLSI4065-LEn_sXuZV4LWgncveKk5BaQolhuzIRWO4if3H9U5f3lZBfG03uo9G3DxpTSWLL7ix0p0hrvXz0u9GoMdxEjUdhN4d8BvGrhZNkJELr9tk0WLY3A8PqSjGxJC3SjpJOi957VWANE-H8RHrXAL-V2mHqdYCG22TnVSwGdIAu3PhQxZKAUXgsfZK_bh5aMAGw7-1-E-18g5sqPsSL0Yt9ro_PSEgz3XieSvDpy1VoRlUbVOfDVRiyPOAR08va1W2QpX56XLQQNun2L-TZ0OXnM_vvo_krXZP0ykZGWp9n3fkZr1Jwvp8Epva6vHh6sPEEjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20940" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20939" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20938" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شبکه کان عبری:
مقامات عربستانی به نتانیاهو اعلام کرده‌اند که اگر اسرائیل جلوی پیروزی یمنی‌ها را بگیرد عربستان سریعا با اسرائیل روابط خود را به طور رسمی عادی‌سازی خواهد کرد/کویت نیز بعد از حملات ایران همین قصد را دارد/اردوغان نیز با محکوم کردن یمن پروازهای ایران به ترکیه را لغو کرده است</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20937" target="_blank">📅 22:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20936" target="_blank">📅 22:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20935" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHBlqH_3B2re0II1kzfx49FaqssB3CaoRdLqC6UBqdvlCLWafPomKr1BiA4MNuViVoSCO3EqIyiXv39nVSTJ9FOrfe13Dlbr3V3I3IyZ-PmVhCODO-n8aMXAI8wQMf6fvXyMRJvinB3-pPqnNp8NOVeZKPJiXb3szwL9M5HzLjOOu26oF66OBB5OMbmFSlJwD2Zg_n4Ep55TsVvHCYxfLpa_KFCOJMh_9lYr7Mls8eag70dCr3hCsMB6iRhqZAxGFWLP42vqV9R_6ahXwS1MtnLlBLma-cXEhEomUtBPspkfBvDgNWXSEy9YTZX5CcbJUR_bTsXmfSTKJlbSbr_pNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20934" target="_blank">📅 22:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9Qluol1OFD88w8KAoqiuG_Mi_y-6pb6yM8Lf5mbgvvUPdwZgVJj0B5-AxugAXm6xklf-mCLhF5abhSWNsA-Fy_UMLayZmMrmeA7_1yR4u49VRwtnpkDFau_HEz9uZbztq3Q0zGgscbYfS8oVk00PIRYaJYG1ZGOJlE61QNFUJvcVE42I_3HgBf_L1QG-4UMT9xaH60Y3IBx3FfNv3JfusEgDE1TBcqc7R6WUl5XDmc6jAY6DM86NPr3h5uKPRT_2KJf-OCXGjsqySE4R7CWY9P1wC30v-K0bXhs6iLsK5uEopP84XhsnygU5UG65r1Lqha8UG8wL02gje8LeN6ofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/20933" target="_blank">📅 21:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yo_yDInIiRfk64bNt2hOSxeYU8Wogs-IOEGvj1xSs3g_J8NNN3pN2vlfhtJR-BupH6rY-LrzSuabfxPE3ucBi3TJ56Jgfg9ZQVQvcLVVoRlcJlpwSnHupkoT06Dy-qKqwTz_kXEPUAFAcaEjscW3N4nvHGhCK2-LH9E7IYySZPaoFpTr5mMxcfvumD8LWaaAQZtbCUais9w5TCG1yWL8AzgotSyUu-VYQzIpIeOhhM2P69G7orn8ueSFF7Tslg2erWxrV2HTsrhqPiuLFtpjELjvnzcFLugE0qQ59fv1tpaJ9-EPQmFdlLzUyTShGjTc2H02xL8m3yyUHmbZOF4PMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20932" target="_blank">📅 20:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=W2WmWY0uquVHWHYyGwH_LXivwCtq0ivNfopetKjDkmvICG42Ug8ygA3pEU8NS8UriuVP-pCyTcePVJH0g_uOJ9hywUwLOooLXSJt0M3smTmuUXt1Pj8czgKcpmQjFjyk9IchBfgn3VcQJR_2U1g4GaGpOYkZeid9_Ah4nOzjabsFGSZv84_NsYXas1akJO5hcw1WDVfHunCaQjEYrM9MnQEQpESYCTZg_NXH3NAR8W_dgagXX5MRsUqUqbs4EXQ5aYMVyYdDsVyu-y6klmlCFIlsxQUsNjJh0ECxfzcmfAhfsSsZNoEmyC1GhdrS5aa_6kk2tT9iAEbOjZgbAbnZgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=W2WmWY0uquVHWHYyGwH_LXivwCtq0ivNfopetKjDkmvICG42Ug8ygA3pEU8NS8UriuVP-pCyTcePVJH0g_uOJ9hywUwLOooLXSJt0M3smTmuUXt1Pj8czgKcpmQjFjyk9IchBfgn3VcQJR_2U1g4GaGpOYkZeid9_Ah4nOzjabsFGSZv84_NsYXas1akJO5hcw1WDVfHunCaQjEYrM9MnQEQpESYCTZg_NXH3NAR8W_dgagXX5MRsUqUqbs4EXQ5aYMVyYdDsVyu-y6klmlCFIlsxQUsNjJh0ECxfzcmfAhfsSsZNoEmyC1GhdrS5aa_6kk2tT9iAEbOjZgbAbnZgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایید شد</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20931" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20930">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntJON5-58Bg2SeoAf4huJl1oTXLiAm50ksEjs15odfK5KGT1JNVVg-nMpbzCysFlkVREdjEq8uj8JE19aZM6yVqhwm29ymkqjRFanD6TCxxy6q5e5Z5oYfl4mWTdZ_rteQxjeMepL37hBaZ7x04TvgNnzmTCTKRf8LIOrhtNQu9yOmA8bYJGy9VTILHgmxIdX8tJdnkcKXEtkdsh5E_B6vlM4GV8TlN184ToLdR3CmC6d1jUe35Ss1OH5nqwIQHo28TcGLMFzy6BTJ7vVT4urCKYJ-iZAtd9GkvgqvGQDnPf-4DsmEnYsIvfzT9m7Vvu3zC60tH-uRa9ls4B9L5NUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20930" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF-BbP_yFbbok8MTNdFkqB9q_px35vrwiZSwkFdTomAhuWx_AWpEvQ3r2y8Ncgg6pDoDVXHYCJ0a9ZvwZF08Aj93QNJDfdXf4yVV6QINO8wOTq9eoikyI9hqdZHb55HfNtL4wbAdckmYaNpB5yeLqH-XDCONoWAiVleO4CXWBSOI58vtf6xbXxEUCZVzNzMZWfwjzTqiYOC_kalMjJW6W4nU2SNy6atSCq9nDhJhG_ya9JMDT5cKul67auqenxMVpTcFjtA4AsR0qFo5Pb7wOk68BX7s0He5Ui6bkDr-dCUFrBKcMhbVoq6I3hNijwONPy-sx7ZjApDBSwRA1PGhFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20929" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdsBqFNohMEx1hT4sQNuZW-JLa0w1Wh39Xm9pUh1GPCagx8WngTHXV3wkl0cj5F2XFUWa3SP1O1qHfH-5opAZ4Tps8k7-IlgIc5xTTulVkwtweAk9tQt4YArXrKRRjPf_EEGMRzXCOKN07MqRwOV5hPDSIIWOBOG7_IBgJNKZjdrqS14VsuOF3FPMBuWGS0-qokgiymim3f1fun2_m8uz1gdnkEnYoosCR1HVUys7P1ICMYxoCnSppa5gjIsKGAe1Yz8woQgB5PZydVOBhNy-XchrQfrYlPEdthqpvUM5I4g3PhIchn2qxroQFgpprsl0LYNOSkPqvMFGVQxUTVj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20928" target="_blank">📅 10:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=iYSBjhcaXm_iCjLQNKqBL63ojS2q16p1o8DV13AZpSomcl6l3nHWEat9p01mnaq-IjOhjoQpbhaTdJQzxZy4r0_l2B_VZmGYoGUf3HVHhGCc-KbYxPOOKgOVt-1sIk6tkaPvQimiSrIJasEkjR9c3MEMjf6Pv19nrortP0iZEWXZpm2MeCg47x_Z0m2j0fpklkRtjtK6bC5KVoHVwbiI6kz-8vDcUxA2FGsq9JU0O2p3bPbJLUEoLsfFWMqKYlgYC0T4PTRBthhnYJGpSI8iFcIISUwsVOVTrybg37pJJuqghl2WgJxvVwY0z06UYlmki9WgUVZe868EsBrT0enHPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=iYSBjhcaXm_iCjLQNKqBL63ojS2q16p1o8DV13AZpSomcl6l3nHWEat9p01mnaq-IjOhjoQpbhaTdJQzxZy4r0_l2B_VZmGYoGUf3HVHhGCc-KbYxPOOKgOVt-1sIk6tkaPvQimiSrIJasEkjR9c3MEMjf6Pv19nrortP0iZEWXZpm2MeCg47x_Z0m2j0fpklkRtjtK6bC5KVoHVwbiI6kz-8vDcUxA2FGsq9JU0O2p3bPbJLUEoLsfFWMqKYlgYC0T4PTRBthhnYJGpSI8iFcIISUwsVOVTrybg37pJJuqghl2WgJxvVwY0z06UYlmki9WgUVZe868EsBrT0enHPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20927" target="_blank">📅 09:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20926" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20925" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsfuZN2lQCc2N-nWA7xT1oDfZS8K6ElCsx0xMUKBxo9uU7irZfO7CDkhOekEXPgR6IZqSi1oOAgVILzgseHMxMTAHxERzwkLlEq7Q8eoQApuJtlnvNha_1-lXTOh8UCOMnVO9FQFbycsHoFLsb7ZCIsRzuiv2rCmrt_8o96UKxrxQrlKyjRQZNQhleVUoY6MGNLuGz2SiJZW8uVHsy7_FTfl-A2XIGu8fjSSTUTJe7DsTwIWPoIz3ljVk7v4HWoRB3izT6Ry23tQLpmGyr4w2RmwiiRKafVIWOW7qon274SssYpP7kIi_ledzJJ-jAoRgh_z1LP9rb7dFjbEDDU_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم در عصر اقتصاد دانش بنیان و هوش مصنوعی، تنگه بندی و راهزنی شاید در کوتاه مدت نتیجه بدهد اما در درازمدت نتیجه عکس خواهدداشت.  (به پست ریپلای شده که حدود ۲ سال پیش منتشر شده نگاه کنید)  اکنون این ویدیو را ببینید و دریابید که چطور بسته شدن باب…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20924" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eahTmLwr5gcrk1aPmWCvxLC1D1LbNlg-6QhdVgQ-6pVwIcerodcbDP9Ux02Ew-KxLJHf241TApSFZhxycxKq_rHqHT0sE9CthA-oM1_S1VFi29w7tZWyu8Q6Pdf3xrhMz40vH4shOAR3Wwt9NhyOL_0YpN2AoUPJCmbsOLHFU6Qw_Y-35UNKI7kqSCxeD85pUGyb0ww1AxFOZoSU1LG5djTH8E4K3TwokgZeRoQV1pEAaNl9HjERSTcd7dXfbIUAGgeT1CMvHFEZWlGizr35xMiBa-HFwdKpsrO67rGBVcpaNtDpf-8ifaKXoJTRbqNEGlzbTGO4Jj3JQ_dwIzCk5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20923" target="_blank">📅 00:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYySFciRvMoGBjtmo_tDz5dlv1a3aDHhkoTyHSUqFwXi5tKy_N86wHI_Yelx_XNbtZl6VGFaUwh17iVcX62HVAsug96c9lYJZxxOp9AgZI1RWoq0Cas7RJHO_7fp5GAZnfXiohdGCSHgS844kD8_Rldql_3fG8kkgztcd-oWKbrjkkTNXu0M9jF8sC9hqzDO7LiWHBlpIJ2lcgbY_mdULDLVQ-5_ETahqI8EbAiAS2Z3RYpSU2W5GNEutfvTQEeIng0MbXhEc-xNbkAAIvnE4UpCzPqPA_XCfbDKWix0xPFXHhL6nkJF6DnnGCACEn6eu2rWVVZ2Vfrb7Yrl7ynQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 27</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20922" target="_blank">📅 00:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNRNjvg9DBtW3UG1WQ6gJMsxwffZyo90-TVo8eeDTEialFASx9POT9Mfav8YlnaOgDWxO1GhQM5HNYQdKcN1fyf19L5UY0BS2oynQO22IQsDDLYuiLlH9KPLt4p4m9qkV_clBgVke3m7lu5GDp0ULScgyQJa1BzsnCygDNDXSzkm3rYeXIpetWP1iNzvuzh2uR2_vFaFcA_Zpb821KnQabJUqSbMrFEiQOK8xmFoblfr7YQDKwzQ1QSycBGjbtFECXnISl-XaGe2CTxpBOg3ULUJ-Ysaur6jKPva77g1Z6ZT3LUX-PwsSw9mIBBAHz-z5k9OLl1SeqDATAYlDTLn0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20921" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20920" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20919" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عراقچی فردا به چین سفر می‌کند</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20918" target="_blank">📅 19:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آکسیوس:
یک پهپاد آمریکایی پس از تلاش سپاه پاسداران برای توقیف یک پهپاد نیروی دریایی آمریکا، دو قایق کوچک ایرانی را در تنگه هرمز منهدم کرد و اکثر سرنشینان آن را کشت</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20917" target="_blank">📅 18:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20916" target="_blank">📅 18:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20915" target="_blank">📅 18:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20914" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20913" target="_blank">📅 16:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0Q8EU2qGAPMHP8aTrIMQuEayC6cxMUJ1M-Q6ADVffGZMFboYy_s1uJ2o9kn3HeQCoammfEwO1gyUWaSPc78cN6rW5BM4_DkID_5rldOihcbjVDbTp-CSJdmICFBNxvy3mKzKFl0c9BhA-UZrMxoVhYYs2RMddbOVsDgqIUMJGcO6KS9XjMligCPQ9b6-JHiwEUkLIMjc2lUG2koLbiNTGaZnL136o4CO8dthQT0ldNQ3wl2KZX9pEPDlsepwPIfPMfGSj3nrCjRaNxhRw0qsVjS-cMhBWFzf8fm3lZKQtcYQEG_OajuB3uYyDq0e7bDcKTW3E5UCvpzvjQsqt0ZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سخنگوی پویش جانفدا :  جان فدایان غیور صرفا برای اهداف نظامی به کارگیری نخواهند شد ، به زودی پیام های جدیدی را به این عزیزان تقدیم خواهیم کرد</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20912" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20911" target="_blank">📅 16:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20910">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20910" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به نظرم بین اسراییل و ترکیه و پاکستان یک تورنمنت سه جانبه بگذارند ببینند کی می‌تواند برنده شده و بیشتر گاو شیرده حجاز و نجد را بدوشد!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20909" target="_blank">📅 16:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رسانه عبری والا به نقل از منابع:   تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20908" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20907" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در سوریه با گران شدن سوخت، اعتراضات مردمی آغاز شده و آشوب ایجاد شده</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20906" target="_blank">📅 15:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 27</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 27
سه شنبه 15 سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20905" target="_blank">📅 13:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/20904" target="_blank">📅 12:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20903" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbE1dkNhEm-ncJd5qXDpG7pajvgF5RCdRR1mpM3UUrbW1visTnX9clrBV7JlBEiK2JgPNggefyt5md02RdPu7ljAmPY88-SsfiWXxcJqJoD-DXknKqSg81xXDGqpvRaTTE4GvQXgNFXzUXI1Y0FbpcOSuRLjYLYFpVn8IMQIJEyuWX2_HN2iOJmTXqQP91kndy78UxfZNU70C4d7UsEZUrqpgv_Byp0zmMXlxoJ2fHaR-kqAFQIp-yRCHIx980hFnGCrKtl9zIBDGSwColQXAvU-O2d2iBFPl1TwD6A3pYfeb7RymznnivNiPxMUQv8_k5My4nWoHM4cYz8Vs5BOcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20902" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw9JzeBuOZ0az1B60h8GJwpsVG-z3iGaAiAs-wcxrtkmtBndIaEKIVD_qbpYROJ3d5nIeVW0HC3cCxo7hN6vJjTa_byxThBwPkp5bEr66aNOIwrBLdcJg4LLGwKRqMSzPcXN9h8zxVpi1W_Kt7Sx3gp4vB90TudeskGjz6Dc-m98av_w62GAZaGL2MJ5T8W8CH6B-8aAEB9UfVPk1QeSkOOSkJg4ELpPNxBiwzVmWXLCQz4XX6thXqF_rLl39O6dVpfLbHt9trZHZNSR-v4MQDyNP7KVyAi8eJTJdNWrZYVxQTGlAXMu3CQ9ktX17HfBcTJCS4iukP_Rg0-4_JpjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران  به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.  در این حمله…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/20901" target="_blank">📅 11:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cmr7Wep4uQYry-g3HM9VVmZqbMTiNXyzuP5h5RynZOKzX0lXhJYz-WbtBVI_Z7valsoW_FaGlk4Hafaryft-y1qvYVdR5i31QmiVsih6d0wPnL1QCi4bwC2HUmE0Ulo-DkiIeyeKDoHsLZqOmsCsnSMJ1RJ6iLFXm5LO0BEcSvHHnCaEaO_vi6fEMBCOmAdtqWy8oeUFAR5i8ScM9CSLa0n_Ud3mNS5FsN2wNXrAW_25IGhUI5f7QgViYfjP3Ol-vxLpFyVVLcs5cVeZRVziNN7EeHXcmoDwJeBJJBOOZbgAvLb0XfJxQjEKtwllVvEEoMcKYvBTUhxlJumnQoxZkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20900" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxKUQ2IziaaCrmn1GDJPuf9MjaPijvmKosT0N9T3z5P7NobCZc1siWds8hGrgC3nCPJpB0JmYlebsY3IWbaqf6Ht5h89jK7J2vCzL1bBNlDaXF_NbJ1lnRMXlKg8BmZQHG-QamJvTcYj-BqxJ3c-5-7QoVLha38vjd8Fo9Ov2tiPWRc3yeRqXK9aTGbp46ZGALU8tmlM0Ih-RYsq00yoN-iuQiwvy0YZjKpMzqsPIdQmRq10Hjv5JRq-CNFTRI0xaDGqOZ3sYujh8JOkm9WcC08bFZ2XusEjMHlFmy1i2WQrnh-MWSmyv7maWkP65cn7sDxWK-Dxlro8yzORKhaEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.
بهترین محدوده خرید از 4280 تا 4250 می باشد.
نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20899" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
