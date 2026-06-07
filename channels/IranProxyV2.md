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
<img src="https://cdn4.telesco.pe/file/CpDNCGCBOys_7KCqsyvfevYCMeTzmZYcilVXWSPZd3M1a9g26nkAa4_tWvYIfw4g9QmrPtYkFhum7uTiHghA6pucmb-fLYfidogzw8wbboyv-Iu9nbAorZEqDRLLnJ8k1syoaoINIQnnA-dDkgKznvWOv4jPXuT2ulsKSkZ7U2dhbgJHvMOiihmKC4DoZgRl2leO0VmhYJ-aL5xc0gq3nzMJwJ9WVrJKQGdeFg67p-iGunITkB-zV1K8ycIZfKoIMU8I9whF7AyqghdERxDFygsVfD1KWK4Y1XpVHYOyLJaQ-6SB89tTb-OWRGca-pfmHsvM_Bvp9TAKNIite5ywXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 40K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 01:28:15</div>
<hr>

<div class="tg-post" id="msg-8911">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇮🇱
منابع عبری:
نتانیاهو در تماس تلفنی به ترامپ گفت: اسرائیل به ایران حمله خواهد کرد
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/IranProxyV2/8911" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8910">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♨️
🔴
نخست‌وزیر نتانیاهو در تماس تلفنی به رئیس‌جمهور ترامپ گفت: اسرائیل به جمهوری اسلامی حمله خواهد کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/IranProxyV2/8910" target="_blank">📅 01:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8909">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
کان:
جمهوری اسلامی به اسرائیل پیام داده که حملاتش رو به پایان رسانده و اگر اسرائیل واکنش نشان نده، دیگه حمله‌ای انجام نخواهد داد
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/IranProxyV2/8909" target="_blank">📅 01:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8908">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
شبکه کان اسرائیل: رئیس ستاد کل طی ۲۴ ساعت گذشته دو تماس تلفنی با فرمانده ستاد فرماندهی مرکزی آمریکا (سنتکام) داشته.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/IranProxyV2/8908" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8907">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♨️
🔴
والا نیوز به نقل از یک مقام ارشد اسرائیلی:
پاسخ مورد انتظار به ایران سخت و گسترده خواهد بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/IranProxyV2/8907" target="_blank">📅 01:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8906">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری
جلسه نتانیاهو با سران دفاعی-امنیتی شروع شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/IranProxyV2/8906" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8905">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری-منابع عبری:
ترامپ به اسرائیل گفت اگر توافق حاصل نشه طی یک عملیات مشترک به ایران حمله خواهیم کرد!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/IranProxyV2/8905" target="_blank">📅 01:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8904">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
پروازها در فرودگاه بین‌المللی خمینی تهران تا اطلاع ثانوی به حالت تعلیق دراومد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/IranProxyV2/8904" target="_blank">📅 01:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8903">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر پیشین اسرائیل:
خویشتنداری یا واکنشی نمادین، این پیام رو به دشمنان ما منتقل خواهد کرد که ریختن خون شهروندانمان بی‌هزینه‌ست؛ از این‌رو اسرائیل باید با قدرت و به‌طور موثر عمل کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/IranProxyV2/8903" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8902">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
منابع عبری: پایان تماس ترامپ و نتانیاهو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/IranProxyV2/8902" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8901">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSbe9HHb_2BVkbc-wzuJVhNFJ0PbXIB0vqVGYzTJoE0ZIqjI8WxyxGIz2BuoKjAg67JXRNuD_K107hAd8DBM6Pid_JRvv8LaSpDiFkB6lmPKli2PVA-zVBTDIO2LJNqh6nzfqm18n5GWvkOZmDpNY79xsW1SCVdidA0QuzBsgPYwMR4vj9sA_8H7pFNXpbIMh1i71m9oZY-4kEg1-HxcVoYniF97Mu7vxo76vWrCUGyf_7kTTFra2PTuNArjYDkLCm9ir5nuvOtJMBbrpMu5Z0_kUZGMwhFiG92y_8zXKyNMiQXFT8H0R00E2KmA9Abb4rmg58N-g_w4b1vIhjBxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سفارت آمریکا در اورشلیم دستورالعمل‌هایی صادر کرده و از تمام کارکنان دولت آمریکا و اعضای خانواده‌هاشون در اسرائیل خواسته تا اطلاع ثانوی در خانه‌های خود بمانند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/IranProxyV2/8901" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8900">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
کانال ۱۵ اسرائیل:
بعد از پایان گفت‌وگوی نتانیاهو و ترامپ، نخست‌وزیر جلسه گسترده‌ای درباره موضوع ایران برگزار خواهد کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/IranProxyV2/8900" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8898">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
حمید رسایی:
هر چه زودتر اینترنت رو قطع کنین تا دشمن نتونه به ما ضربه بزنه!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/IranProxyV2/8898" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8897">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
کانال ۱۲ اسرائیل گزارش داد نتانیاهو و ترامپ در حال حاضر در حال گفت‌وگو هستن
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/IranProxyV2/8897" target="_blank">📅 00:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8896">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صداوسیما: به هیچ نقطه از ایران تاکنون حمله‌ای صورت نگرفته
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/IranProxyV2/8896" target="_blank">📅 00:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8895">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری - پروازهای فرودگاه خمینی تا اطلاع ثانوی متوقف شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8895" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8894">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEpgk9nJvCADnbgqHjHwx_iEn20iAMIyO2U0FjTf7QqTlCDsscdWEyVSBztmthhgquX5zj08vlIRzAArpHibzw_IYG7dg7f5ohJKS4ovqxoIc0iEQFEwxpi514YrnCxN-OPplylh56tCaPXmOpgWeSffO0gtUAwq6A1EyCrTX7h3y_sPJ8rb0vmnL5GSgyM7pbcD1CloTcqXzHZWlI-sLDPMH5hpum23eANYTfUAQd_G0ewYhpt-GRDV6iOhRFnA94MEvl15GjYp_fBADKZRMqRp1iBYUwIkLH34S9nEBgD-0ajTNyH24dx2Rp1A8UVij-6Uk-NTt37cj19rdhrfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
-
تمام هواپیماهای غیرنظامی تو تهران برای پیش‌بینی حملات اسرائیل جابه‌جا شدن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8894" target="_blank">📅 00:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8893">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NThUpyporTNB3ICrHPC8vK-dVWbFwep8hl3V_2tILeAEsWrmQC5jFQt_65vl678M-GCRZ35zv4lgijnq1sZh7N2EY9rghRl03mTFcVwqXt8XzPPxTw0JLQJzJlaCJSh-p4WDL2xVL2d3mFs5jyxireWw-otSl4z7lEbsdBnuKwLqDv4ljVKvETjKIct73fGgjECwtCbulj0jOegL236BMlLTv7HaOFKbVIhaMX8Cwr9bsVp5dPRRQ6LDBOYy5DgBf9nUFjqydGkSST1NpxOJjcDhN94q69PZO81uDisfUvt3dFww_nK3tgnadZuevG48qJZ4D2-fDeWs3HTHTH6A3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ما بهش میگیم لبنانو نزن
خو اومد زد
الان دوباره بگیم نزن دوباره میاد میزنه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/IranProxyV2/8893" target="_blank">📅 00:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8892">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری -صدای فعالیت جنگنده ها در جنوب تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8892" target="_blank">📅 00:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8890">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مثل اینکه نتانیاهو ترامپو بلاک کرده
اسراییل مجددا به لبنان حمله هوایی کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8890" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8889">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
تسنیم:
براساس پیگیری‌ها، صدای شنیده شده در‌فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8889" target="_blank">📅 00:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8888">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری-نزدیک سپاه عاشورا تبریز صدای انفجار اومد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8888" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8887">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dbb2f6e4.mp4?token=hbZ_TU5sDVXPI8xu71zFAA_fuiit_n2ZADG_Tzom2tH5HmTv_fsIWHXmzlsNMsWVdciTiPqHA52ANqF_DWXEH3fWtdb9omgWxBaP9nRhHuO7ZJmVjyGLUqgYfSWY3rlc9WIypbwAji8MfpX5NXIVoK4KnC07kuzzT1JDGoKPqzpGdMlM6LjPjyb7LFmpX49k3uu2iuR0o03TUyngywMF6y-hT5MOqvoeea6NZ1V1KegmvalUY1dZ3Hnpr9wfXPIzpGDeZfEXLkvDv2ohYS2e0YRU1bs6M-1tGzc24baPb1DSe728ThwMBjbEw9NXl1UYWWYujZ6mHPlQD9C1cEmE0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dbb2f6e4.mp4?token=hbZ_TU5sDVXPI8xu71zFAA_fuiit_n2ZADG_Tzom2tH5HmTv_fsIWHXmzlsNMsWVdciTiPqHA52ANqF_DWXEH3fWtdb9omgWxBaP9nRhHuO7ZJmVjyGLUqgYfSWY3rlc9WIypbwAji8MfpX5NXIVoK4KnC07kuzzT1JDGoKPqzpGdMlM6LjPjyb7LFmpX49k3uu2iuR0o03TUyngywMF6y-hT5MOqvoeea6NZ1V1KegmvalUY1dZ3Hnpr9wfXPIzpGDeZfEXLkvDv2ohYS2e0YRU1bs6M-1tGzc24baPb1DSe728ThwMBjbEw9NXl1UYWWYujZ6mHPlQD9C1cEmE0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری-فاکس نیوز :
با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8887" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8886">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
یک منبع نظامی به تسنیم: موشک‌های جمهوری اسلامی آماده‌ان در صورت پاسخ اسرائیل فورا شلیک بشن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8886" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8885">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو اگه به جمهوری اسلامی حمله نکنه، باید با نخست‌وزیری خداحافظی کنه!
احتمال واکنش اسرائیل بسیار بالاست...
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8885" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8884">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رادار کلودفلر اختلال شدیدی رو روی اینترنت ایران نشون میده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8884" target="_blank">📅 00:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8883">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
سخنگوی ارتش اسرائیل:
جمهوری اسلامی اشتباه بزرگی مرتکب شد. اسرائیل موازنه‌ای رو که تهران در پی ایجاد اونه نخواهد پذیرفت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8883" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8882">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
کانال 14 اسرائیل: اگه نتانیاهو بخاطر حرف ترامپ به ایران حمله نکنه عملا دولتش تموم شدست چون تمامی سیاست‌مدارای اسرائیلی خواستار حمله به ایرانن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8882" target="_blank">📅 00:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8881">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری
فرودگاه تهران رو دارن خالی میکنن
پشت سر هم هواپیما بلند میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8881" target="_blank">📅 00:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8880">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
ارتش اسرائیل: سیکتیر، ما لبنان رو ول نمیکنیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/8880" target="_blank">📅 00:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8879">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
سخنگوی ارتش اسرائیل: رئیس ستاد کل در حال انجام ارزیابی وضعیته و سامانه‌های پدافند هوایی ما در حالت آماده‌باش قرار دارن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8879" target="_blank">📅 00:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8878">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
سخنگوی ارتش اسرائیل: جمهوری اسلامی اشتباه بزرگی مرتکب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/8878" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8877">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اگه ترامپ چند دیقه دیگه اعلام کرد با همکاری سپاه به اسرائیل حمله میکنن نباید تعجب کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8877" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8876">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa612d6574.mp4?token=Ck3NhpSpz8PxEGhLS1pTa1PwguEljEM9j8aHYJG1C0XJ9cbiavK95MEqi6HhJi9DPt5cYbJ56T7BweXCirwzVReNj_ES2Qi3Qfv5QEsTI6n3vxX3kvnXokf1edb6ZOiWZtZMJGhHR1hLX_FQIeSFXycJnI5TKSjH4lDzsxxt0xmKgszDSLqWgf46pd--3tvmmuN9EjIguYKoeojRf_Qv2KYID7yKXacKjKvrAzSNrRXFUcKdN6X1cEe1CMEPTRtukIdLPd1qfb0nJSBefkzPPrvYGAUScqEEInEokw3_FwfdWIqTP5-nM21mjDja1e-F878QuEZ0nQUeIMIhWqKuMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa612d6574.mp4?token=Ck3NhpSpz8PxEGhLS1pTa1PwguEljEM9j8aHYJG1C0XJ9cbiavK95MEqi6HhJi9DPt5cYbJ56T7BweXCirwzVReNj_ES2Qi3Qfv5QEsTI6n3vxX3kvnXokf1edb6ZOiWZtZMJGhHR1hLX_FQIeSFXycJnI5TKSjH4lDzsxxt0xmKgszDSLqWgf46pd--3tvmmuN9EjIguYKoeojRf_Qv2KYID7yKXacKjKvrAzSNrRXFUcKdN6X1cEe1CMEPTRtukIdLPd1qfb0nJSBefkzPPrvYGAUScqEEInEokw3_FwfdWIqTP5-nM21mjDja1e-F878QuEZ0nQUeIMIhWqKuMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه برخورد یکی از موشک‌های جمهوری اسلامی به شمال اسرائیل:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/8876" target="_blank">📅 23:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8875">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری
اسراییل: تهران آخرین شب آرام‌را سپری میکند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/8875" target="_blank">📅 23:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8874">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngVgYrKsDuMZRg6iwQH2sER7QzvqHEPyM7HPr5BHiNS8WB7773J7jVMP78iFBy4HknbhFS-Hg8bVLLS-rcDnvsU90dtziTAar7teVbrpt9xr_T6cYwp_YhgbEWN5sg3QUu3o6Ee7awQRNdZUswcWJ3XgMjIxR91DsuTIott03XyNvd27M65dsbJ4_OcJs0q9MsMAbP0QQ6_sJB6i_VlmhWzS7od5nArFQSdpib2vAlmvGolM11lvSRLF0vlXdp1fg8bLSS1GdOcv8n_O38JBBjCywZHbs3Twm7ec_f-6JhXAcM-E5PVGUFM-dbPumGWyu5x-HAGJdXxykeeX3Z4_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری-رئیس حزب اسرائیل بیتنو، نماینده کنست آویگدور لیبرمن: «تحمل کافیست، باید فوراً واکنش نشان داد و به زیرساخت‌های استراتژیک ایران ضربه زد»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8874" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8873">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فعالیت جنگنده‌های ارتش بر فراز آسمان تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/8873" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8872">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صداوسیما: خونه نتانیاهو رو زدیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/IranProxyV2/8872" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8871">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری
حساب منتسب به مجتبی خامنه‌ای : نفس رژیم لرزان صهیونیستی به شماره افتاده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/IranProxyV2/8871" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8870">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رویترز به نقل از یک منبع ارشد ایرانی:
تمام پایگاه‌های آمریکایی در منطقه در صورت انجام حملات از سمت اسرائیل، اهداف مشروعی برای جمهوری اسلامی خواهند بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/IranProxyV2/8870" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8869">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری -ترامپ:
به نتانیاهو خواهم گفت به ایران حمله نکند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/IranProxyV2/8869" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8868">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwfSnRvc3Y8SLP2FKAxPv4Snh9ebQzYq0f4hOAeA_YfvpTqG5GNlBsbknS7OiwJp47o-iwzVc2h-dJct0am0Mg2n6u197I0Dhkh7sGOqxtIXqiVa6KVP_UP98TOeocRzZTVD0Adpv9j-owksGLcx6Vr5UD1wPvyhJMrZd35pE_SSwQ6IAjPOiTPBO_VMbyDsUM5mD4gq30iwuCdgk0drwJNJ0XmRANON_kIOOuWlVL6WgqZToH5Ky5P9F8UTA4Sc7gdAA9K4AHft6jNAzSJcgYXrDjDYYV5s7aVH7tHpiegGYPgjMauXmeTGTly6dG0-unTYw-m8f-kApcv7QK_Meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
فوری / عراق نوتام اعلام کرد و حریم هواییش رو بست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/IranProxyV2/8868" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8867">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
سازمان هواپیمایی کشوری ایران:
حریم هوایی غرب کشور تا اطلاع ثانوی بسته خواهد بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/IranProxyV2/8867" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8866">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♨️
🔴
سی‌ان‌ان به نقل از دو منبع اسرائیلی: ما به شلیک موشک‌های بالستیک جمهوری اسلامی با قدرت پاسخ خواهیم داد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/IranProxyV2/8866" target="_blank">📅 23:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8865">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / ترامپ: نیروهای نظامی آمریکا در حالت آماده‌باش هستند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/IranProxyV2/8865" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8864">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
یک منبع جمهوری اسلامی به رویترز:
اگر اسرائیل به حملات موشکی ما پاسخ بده، ما هم قطعا پاسخ خواهیم داد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/IranProxyV2/8864" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8863">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
ترامپ به فاکس نیوز:
نصیحتی که به ایران دارم اینه: شما موشک‌هاتون رو شلیک کردید، این کافیه. به میز مذاکره برگردید و یک توافق انجام بدید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/IranProxyV2/8863" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8862">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری
حوثی ها منتظر دستور بستن تنگه باب المندب هستیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/IranProxyV2/8862" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8861">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
سپاه: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/IranProxyV2/8861" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8860">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTNhDIQ3jhCHIjXKnA3N4J1Rc8Q-3xZUKnSRGdY7en9Z4CrG8Oq_JC3qNOORZpGo2zet4kOdEW28Z91gJbGtU1gGQlUMvLpjTY5yrph3R1GHz0n3DkFYdxSbeEMZ0Pv_sEWWhmJlSHK1YUas5fi415YRW4TmU5syPlqBuDgMVa9yyNS5VNIQb1CK_269ZK62P4f9HdvFKzoaWREFn1728iUFwEvEGZrfsLmhbYujTOC_coAaG5CxgGoeH41Jc-9FYTAt7guTGcDizTl2p7BXmUdJfduHUezFCJW1_xecGlhPDdipfGKZaVWQ23tofodwkde6miN8bn9LBaSroZBa0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موسوی، فرمانده نیروی هوایی سپاه:
الوعده وفا
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/IranProxyV2/8860" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8859">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70b88044e.mp4?token=LV6ncq-bfGl_FLQg3zImYDFBi18FlYMODLKJYYg7nABXSygGSL-QcSjRXvkpKCV_n_zxez7vvJbu8T745nhkbB306wljNTAdcxQIaTZg5-IbLhvTEqZ_5NggRx8hfmN3uHk0I1I2avoMLKmOqMIt98LlrMVJFdJzPR7YYkrlklBhy470VSoR5ZaClTLx2rM68EOmLNaOKFIFosoF1kGbbS64flvsMUR4C22m0leq3MTJIp-cnQGfFPkCCP9Fbn6HUKF5cyFgQbQV3G7leN86V7vX-RUHKl6CN4j-KdkUOZ4U36hDQSeSJNRQFXYDy8Uo1vBIVHowDN8JA8eQbjnnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70b88044e.mp4?token=LV6ncq-bfGl_FLQg3zImYDFBi18FlYMODLKJYYg7nABXSygGSL-QcSjRXvkpKCV_n_zxez7vvJbu8T745nhkbB306wljNTAdcxQIaTZg5-IbLhvTEqZ_5NggRx8hfmN3uHk0I1I2avoMLKmOqMIt98LlrMVJFdJzPR7YYkrlklBhy470VSoR5ZaClTLx2rM68EOmLNaOKFIFosoF1kGbbS64flvsMUR4C22m0leq3MTJIp-cnQGfFPkCCP9Fbn6HUKF5cyFgQbQV3G7leN86V7vX-RUHKl6CN4j-KdkUOZ4U36hDQSeSJNRQFXYDy8Uo1vBIVHowDN8JA8eQbjnnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♨️
🔴
مشاهده موشک در آسمان تبریز، دست‌کم ۶ موشک از تبریز و ۳ موشک از ارومیه شلیک شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/IranProxyV2/8859" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8858">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری-موج حملات موشکی از کرج
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/IranProxyV2/8858" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8857">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری
حملات جدید به ایران بزرگتر از قبل است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/IranProxyV2/8857" target="_blank">📅 23:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8856">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
نت بلاکس:
🔻
ترافیک اینترنت در ایران ۲۵درصد کاهش یافته و اختلال زیادی داره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/IranProxyV2/8856" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8855">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trdlDe2R7bY8ZP9Le3C8hZaHQuR-idgMMCfxGFGmsQd7O-xMEoBr7qwXuiyaSRJWjwroNkaVEa3z6wI-k-EwJGs29gXb8k-t29myK8pAd1i3rAVttmmo8Mjd5eY8Yi0wSMVRcpFodHfBHjh1v4Y1BqACjf_d3LsJHpPHXNtNqngjm5XV-CLsB_YYU4m0TTR4OjHt6LoTNeyw__wYn5tUBBi_JQ3Phvs8RsM2xejjtIAWlUxWR2wCfSB-axdLnNjwOGdziD0Twwi7eW6GeU3kB5O6WyXJM1Sp-xAhAG5_Ee8oB0q_KqtuiNbjca371G5MzphowJi9MMvZH1Co4SnNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
سوخت رسانها به پرواز درآمدند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/IranProxyV2/8855" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8854">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
نت‌بلاکس: بسم الله الرحمن الرحیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/8854" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8853">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری
منابع اسراییل: حملات سنگین به ایران نزدیک است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/IranProxyV2/8853" target="_blank">📅 23:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8852">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری
پمپ‌بنزین های تهران مملو از خودرو شد برای خروج از شهر !!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/IranProxyV2/8852" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8851">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
آکسیوس:
ترامپ در جریان تشدید تنش بین اسرائیل و جمهوری اسلامی قرار گرفته.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8851" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95132def2a.mp4?token=OkOThLNHRiVmlUYmx3VOaOAQJrt4qKASKiNQM8O8QD8L6Yr15adfwkjxgNXl4WYhy_22CterdF2PbSdKl8ASVNP1dCnAQDeI_gJCBSh9hGrjQyVPJjVk1Gs_pmWgdtIntRe-vpszBwCWf7dOznX00v0HoCo-3a_6ky5hKFPNyIA51DS0OZGgWlHQUymqrOxL57WE39VGiUFmA4gyNpdRc-RjMxvwAyTTdypUXR6PzBKkzaRrsQew83s0s2TovEmOtMhfRQSIcrYdgyFJsDWL2QR6mvPUsgrFnDing5ASU7p53zo0PUblbTu2FLen8tUayOp8m3d6p6Tfyh_eCkbQ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95132def2a.mp4?token=OkOThLNHRiVmlUYmx3VOaOAQJrt4qKASKiNQM8O8QD8L6Yr15adfwkjxgNXl4WYhy_22CterdF2PbSdKl8ASVNP1dCnAQDeI_gJCBSh9hGrjQyVPJjVk1Gs_pmWgdtIntRe-vpszBwCWf7dOznX00v0HoCo-3a_6ky5hKFPNyIA51DS0OZGgWlHQUymqrOxL57WE39VGiUFmA4gyNpdRc-RjMxvwAyTTdypUXR6PzBKkzaRrsQew83s0s2TovEmOtMhfRQSIcrYdgyFJsDWL2QR6mvPUsgrFnDing5ASU7p53zo0PUblbTu2FLen8tUayOp8m3d6p6Tfyh_eCkbQ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ساعت ۲۲:۵۰ یکشنبه؛ مشاهده‌ی نور چشمک‌زن یک هواپیمای مسافربری در آسمان کرج، همزمان با شلیک موشک توسط سپاه و احتمال شروع حملات اسرائیل.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/IranProxyV2/8850" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO-zMrePQYhhL2DaRaAgs3RH_bJUssgi9YuXRHDVP0dMPQL2SohLX8xQ8SSe68v5kuSvorsgwRvT9s_ylO7sjGPVCWXe91bxGgpA7aXgQqaDbtXyioC6Tahj87tPXqwNw6GEEoSWfgep92mqm4juR_dNjbbO3IoDQ8H3uXND2iAQ2yU7odppCf1Gvt5azrojEVvau-HiNVN9FV7_ZRQgMgqHUZ1Sz-ypN5zVF7srl7eShI7CaI9r9d286MPLvdB9SGaKoYp2fgsNQ0JvRtyR13wA9SasibDnr4YfDpwMCHRccGq2SX8Mx2xz0EXwkGzpKkqLrJwaBA-w6DytSovRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
♨️
آژیرهای هشدار قرمز بی‌وقفه در شمال اسرائیل به صدا دراومد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8849" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8848">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
#فوری
| ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/IranProxyV2/8848" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانال 14 اسرائیل:
به زودی پاسخ بسیار گسترده در ایران خواهد آمد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/8847" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac124d380.mp4?token=ejlugs2lClbC56Ifs5ZAj3u-Itm1p3-EP-XEHzcf6nApxDmKn_DIYXS4aR6cr3V-mvCb1szzzjpHfIOt6l2IvqPNPBdSU_kyfTvyikyQdP6T4yh7mek1acQnTGfbsPEPt88fgZZ61xR56wGwl6XPl6D96dxpTsOsWJ1AtXgvzPj6hS4R30tPU5-CyZYjvxr5Pc9qyj0S4pDG0LW1sfE9yNzPqmkNGqIp1elRKLb8zb7FZTXoCaadwUeSPv_6cijlacf-qVe_tZlImlHmWnEYNeUl4RvGVKkyGghgpFXlcLUREHu0N42GKhOPXvutmqePH-lF6zxeQHIv2-eaCqe7QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac124d380.mp4?token=ejlugs2lClbC56Ifs5ZAj3u-Itm1p3-EP-XEHzcf6nApxDmKn_DIYXS4aR6cr3V-mvCb1szzzjpHfIOt6l2IvqPNPBdSU_kyfTvyikyQdP6T4yh7mek1acQnTGfbsPEPt88fgZZ61xR56wGwl6XPl6D96dxpTsOsWJ1AtXgvzPj6hS4R30tPU5-CyZYjvxr5Pc9qyj0S4pDG0LW1sfE9yNzPqmkNGqIp1elRKLb8zb7FZTXoCaadwUeSPv_6cijlacf-qVe_tZlImlHmWnEYNeUl4RvGVKkyGghgpFXlcLUREHu0N42GKhOPXvutmqePH-lF6zxeQHIv2-eaCqe7QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/8846" target="_blank">📅 22:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIN-gz1U61rLaU317FpbaWSC3uYL93yxI27ywL9webrwo4VTavMUj_6_zEPEXgf9QvDOY8ifiN3a3ZdlVosFUo93oDwkeAhEG_S3BPtWhYOhtouZfPQU4irUspI0hYXHt_av0Yp0z54Q4wcJy1Q-d5o0rOAcD8E0FCUu53jfJy27sIPamZx8-2mecSiH7Mg6vI2U2FA_w_C0GG8y73TAQWququ2qxlZR6PhnzL7n9dxUhlnQ7GzPRUC__iMfQXWC2Lcbz7YWbGqEmY3yOzFbyOrWmk2VHqmcERKCvceXbpIa1xK2A4OeEm_qr9VSyVDSD4j7-ZqIg0f0BAeLXfpH3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/IranProxyV2/8845" target="_blank">📅 19:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO-JbtKqW5lL-AR5hAk3c0EHpqyrwRqKgsLvvtC7tL-WQIjo0ydriqd6sml6fApaAWEePzLuqY_Sf7mdJXHWbp0_SIWljPQlhoUydU77fXBmG6oY0ZfyAElfgqLTasbN1bYsabDmp2vD-uJ2n0Xx4QUcZNOu3wFfSsQ--kHd2r8TWOPU4wskA6rRt3XEPY1TZSnHhxNanTCIw9XjfrKsPkjo0V3keiftVuUF2ptUhCqp8e5M7TUI4B4bIOex0UGDzBFsbW8WcG3Sl33h0WosFZYRE2dpzkzJOymr4GcxtNPSEVd1fTHDjedwsMBMssuAxyIyos2szf4xC2hgIeoNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دوستانی که سرورا براشون متصله نمیشه، ۵ پورت و ۵ لوکیشن جدید اضافه کردیم، لینک سابتونو بردارین، حتما دامنه جدید رو از قسمتی که نوشته
info.russiaproxyy.shop
به این دامنه جدیدی که براتون قرار دادم
⬅️
doc.midnightfits.com
➡️
تغییر بدید و وارد ساب لینکتون بشید سرور جدید رو بردارین
🔹
نمونه ساب لینک جدید
https://doc.midnightfits.com:2096/reza/xxxxxxxxxxxxx
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/IranProxyV2/8844" target="_blank">📅 16:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جهت آپدیت حدودا تا یکساعت دیگ دسترسی به ساب غیرفعال میباشد ولی هیچ مشکلی در روند اتصالتون به کانفیگ ها نیست، خواهشا تا اطلاع رسانی بعدی ساب لینکتونو بروزرسانی نکنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8843" target="_blank">📅 15:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8838">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Open vpn.ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ open vpn
📱
آموزش اتصال:
😲
کانفیگ رو وارد برنامه کنین
بزنین روی connect
بعدش ۲ تا گزینه میاد بزنین روی continue
عشق کنین
✔️
❗️
. اگر ارور داد چند بار بزنین retry وصل میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/IranProxyV2/8838" target="_blank">📅 11:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8837">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوستان اگه سابتون احیانا مشکلی داشت، حتما برای پشتیبانی بفرستید و صبور باشید همرو جواب میده
❤️</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/IranProxyV2/8837" target="_blank">📅 22:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه خوشحالی میخوام مثل بدبختیام تموم نشدنی.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/8836" target="_blank">📅 22:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HenTNAqljRy-9l4OZke43foy5wR0YRvWKXAUdvxllBJETpI9ol3WJlVrAIX__lX8i8uFUL466bxjRRGcnIwRrNGqSsO5bi6tMpYvlUxEFP-n3XIBVnW6ZJsdPwryfIByF9x_WWhcYKR8jp60eR0c_i7HN1Syt8XAS9sFF1vQRmzVFvBZ0itd4_gQh0a7k6EUhD7KMSeMvd0TqXimkMRIJ9YS-zsE6GRogXgAeoLUSfSrszJ66f0HfRmQVTrq3okk9cw_2wKKlozA6RJ2ckU4xUw9LypCe9b0XIa39YdJ64n-9U4w_kW6X9soMXRTkLb9Q77bQx81y8-8_d83NrgFWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خب حالا سرویس های ما دارای لوکیشن های آلمان
🇩🇪
و آمریکا
🇺🇸
برای استفاده در سایت های مختلف مث جمنای و ترید و گیم و... آیپی ثابت هستند
فقط نیازه تو ویتوری سابتونو رو آپدیت کنید تا از اپدیت جدید لذت ببرید
🍸
❤️
📣
دوستان روز به روز سعی میکنم لوکیشن های بیشتری و سرعت بهتری بهتون ارائه بدم
✅
📍
جهت ثبت سفارش به ربات میتونید مراجعه کنید همراه با تست
📎
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/IranProxyV2/8835" target="_blank">📅 21:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8834">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl5A6nZd3di2yqFjSqpauobJhuYDzakqYKjrgagsw55R9hpZYzlCI3KwuInSnX908zv4Ru_KhzbpFa-2wDGwjLpdFgadrREW_maVyfBwqQI0hMCu6QXwCdfEiwZBYWDbo8sMX9Tcl1rrVzC_FK6fC6lSPdifNLTzvWxvqFGGr2oytiNI2D7Hcbndr9GQV_3JB-TFVxTG58_o6vMP1L4o92A33EGz8BlMBbbd5eK9onp_8PK3REdSnhciWPWkaTEBi4v4uqL9Puaqukw2YC79OT9k7V0sPjD4Fr9myM-jDFToR8_7XpBnRXfBH-H0VD7SDfvzfB8392SxS_Zhy8c2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک چند ماهه نیکا رو تهیه کردی؟
😂
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/IranProxyV2/8834" target="_blank">📅 20:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8833">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستان ساب هاتونو آپدیت کنید،بزودی لوکیشن های جدیدی به سابتون اضافه خواهد شد فعلا درحال حاضر فقط آلمانه
🇩🇪
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/8833" target="_blank">📅 19:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8832">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
دوستان دیتاسنتر چند لحظه برای آپدیت آف خواهد شد، صبور باشید آپدیت خفنتری در راه خواهد بود
❤️</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/IranProxyV2/8832" target="_blank">📅 17:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8831">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDXjoiVM_dyvRrDVoNO_EKDEJqdhIG0wkjRi_TbIwCgK2UZIL9GNfbzJ5HzTwJGXXQWZvUyaNZ5P3r_iqEbsFO8RkzLagXyK_xKATWO-mJmNk1NpyiSCAzz2KwoTDcmgdljeB_wTRVR-gU1quh8lK4TE1Yk5vOFw6PrIxDgaGBkvFwXgHtEMBcw7jmTUeqIXtG8mdqFsah8608kprtFyFRismDkz5Up7sPkwj9x_kvxEkwRyq8X1dKQfawcahRH3d6BWu8Ka7P_4dSGgZSUbtZMPPlOoDiWAZ0wxougx7162aII22UX_x7cO7a2tuZQO-BlUOAEvWDPPfUCp-IsHaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی  10 روز اولی که اینترنت بعد از 88 روز باز شد، مردم تو گوگل نه دنبال قیمت اجناس بودن نه جنگ و سیاست، بلکه دنبال ابتدایی‌ترین چیزها یعنی آهنگ و فیلم بودن!
1. اهنگ
2. آهنگ
3. فیلم
4. عکس
5. ایران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/IranProxyV2/8831" target="_blank">📅 16:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8830">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هزار تا هم که خوبی کنی، همیشه حرف راجب اون یدونه بَدیته.
‌
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/IranProxyV2/8830" target="_blank">📅 14:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8829">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ2YCmVbO1c60rWqlEe_9JWpwck9IFuxdbeTk4AYxME5q2LRHd7bVoSYBj6tPLrUOiACPNU_h-FLoTdZm3ry0PCykPKMBpVrHn3GAzj-85Zosk3iFxqThJNG8FwxkWOJo-nvNdRKzZ_hRUsDwcSAIW5gzj3f0-kLcrz21BZhPoFb7xBai4JOsUpHBvJMRzPZLFyj_wo6Rd6cU5CjS5inBpCC4MeU0sH9QkQ0rmXf2QBw2x8Qq2ucDiTyWeYGM_hoi8eAPGhP3Hf1SvlUg7SpmCuHwiWYyZr3hHrlWMqwuG8VHPcpIjbyG37DvVnODHmJmdQUzQeOAPohQ5_xPh1zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان فقط گیگی 14
👀
▶️
پینگ 147
💵
10GB=140T
💥
🛡
همرا با تست در ربات
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/IranProxyV2/8829" target="_blank">📅 14:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8828">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اِی‌کِه‌بی‌تُو‌خُودَمُو</div>
  <div class="tg-doc-extra">دآریوش</div>
</div>
<a href="https://t.me/IranProxyV2/8828" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/IranProxyV2/8828" target="_blank">📅 13:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8827">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">vless://491bd18b-c1d1-4ec4-94d2-e1a13193d4da@vpn.smartrahand.com:2026?security=none&encryption=none&headerType=none&type=tcp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله رو همراه تست کردم، بقیه رو خودتون تست کنید
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8827" target="_blank">📅 12:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8826">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CIVAX(mci).npvt</div>
  <div class="tg-doc-extra">13.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8826" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🆕
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/IranProxyV2/8826" target="_blank">📅 12:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8825">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">vless://0284cc16-1e0f-40f0-900d-dfada20ff258@45.130.125.192:8443?mode=auto&path=%2F%3Fed%3D80&security=tls&alpn=h2&encryption=none&extra=%7B%0A%20%20%22scMinPostsIntervalMs%22%20%3A%2030%2C%0A%20%20%22noGRPCHeader%22%20%3A%20false%2C%0A%20%20%22xPaddingBytes%22%20%3A%20%22100-1000%22%2C%0A%20%20%22scMaxEachPostBytes%22%20%3A%201000000%2C%0A%20%20%22scMaxConcurrentPosts%22%20%3A%20100%0A%7D&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=vh.mojaz-persian-music.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله رو همراه تست کردم، بقیه رو خودتون تست کنید
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/8825" target="_blank">📅 12:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CIVAX(irancell).npvt</div>
  <div class="tg-doc-extra">14.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8824" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
☄️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8824" target="_blank">📅 12:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">vless://c466ef48-fb57-40c6-808d-ee48d537844d@104.17.121.198:443?path=%2F&security=tls&encryption=none&insecure=0&host=join.kakoolnewsv.workers.dev&fp=chrome&type=ws&allowInsecure=0&sni=join.kakoolnewsv.workers.dev#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله رو همراه تست کردم، بقیه رو خودتون تست کنید
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/8823" target="_blank">📅 11:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دکترنیـک صبحگاحانه.npvt</div>
  <div class="tg-doc-extra">9.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8822" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8822" target="_blank">📅 11:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">vless://c466ef48-fb57-40c6-808d-ee48d537844d@104.18.154.96:443?path=%2F&security=tls&encryption=none&insecure=0&host=join.kakoolnewsv.workers.dev&fp=chrome&type=ws&allowInsecure=0&sni=join.kakoolnewsv.workers.dev#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله رو همراه تست کردم، بقیه رو خودتون تست کنید
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8821" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8820">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرعت بالا🔥✨.npvt</div>
  <div class="tg-doc-extra">2.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
💎
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8820" target="_blank">📅 11:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8819">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">vless://c466ef48-fb57-40c6-808d-ee48d537844d@188.114.97.6:443?path=%2F&security=tls&encryption=none&insecure=0&host=join.kakoolnewsc.workers.dev&fp=chrome&type=ws&allowInsecure=0&sni=join.kakoolnewsc.workers.dev#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله رو همراه تست کردم، بقیه رو خودتون تست کنید
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8819" target="_blank">📅 10:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8818">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">VnexVpn27❤️‍🔥.npvt</div>
  <div class="tg-doc-extra">178.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8818" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">31 Config Npv
⚡️
Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8818" target="_blank">📅 10:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8817">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">vless://c466ef48-fb57-40c6-808d-ee48d537844d@216.24.57.6:8443?path=%2F&security=tls&encryption=none&insecure=0&host=join.kakoolnewsc.workers.dev&fp=chrome&type=ws&allowInsecure=0&sni=join.kakoolnewsc.workers.dev#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله رو همراه تست کردم، بقیه رو خودتون تست کنید
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/8817" target="_blank">📅 10:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8816">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">⚡️𝗡𝗜𝗧𝗥𝗨 𝗩𝗜𝗣⚡️.npvt</div>
  <div class="tg-doc-extra">31.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8816" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🌟
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/IranProxyV2/8816" target="_blank">📅 10:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8815">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇩🇪پخش کنید.npvt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🔝
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/IranProxyV2/8815" target="_blank">📅 09:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8814">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVkQ3Qnmu7dnMNOS8qtvqIVepAbpbJFcjx_1Og75t2qu6wfcs8YjZG3xJLMjsVo8YCLUenrg0LyrR5LuZbzSxXt_BSJObwgKKmd6Imzt2N_oWirdAqLM1UuWJxzgxK-M6_7A1h4M4poXTB0sACc-vjrrmJz16FWGpoJLLJByi6B9A2U-evdbE_V0W1FwdgxOhza6hp3DZ08WvOr0ymM0Oqmk1pX2kpH_1Qky0dwChNtGtgDWNfYDmZg0TgmKY-iKZuKVw11Jlk9pTExpxVBDjHtiY-QkZFJEOmi1is9q8YKYBXEq3AReO44p0RvO34vBewdrc5iScBelNgDCWEqJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 14 هزار
🇩🇪
⚡️
10GB=140T
⚠️
دوستان 50 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot
💎
آیدی ربات جهت ثبت سفارش
👆🏻</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/IranProxyV2/8814" target="_blank">📅 20:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8813">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOucU3bgBCaxLMc9_LS4XN5fw3k_rQR2X2oSyhZmCBDJeszo1z0FepocuNSoCWpY-kxp352deafaA7odk76uKsBzs3oC7wc1WFF5xLQUKY-kpdIhYaCJl_N_IevUHfSLO75O70DIPZyEY1JN-Eh_bUJWNIgxFw24RjvGAfMISZ2UcOsHLRcI2wp7XYtcxKT_DTjPxARmMKxnMwyIHStTYSP25JDfuCkM32cZPXm9bQsYiATP8XWzWvf-9kRwaUVmjkXDHd1tXd6YgCCPgv7EbA6pC7y_shkb3oOLPu71m623lMA2TY0EkroRmPpwDBm5z0TG7xci3rE_gjijLFwS-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 گیگ دیگه رایگان
❤️
vless://a7724efb-50b0-4863-8af8-054ee4a8a7dd@82.38.171.125:10517?security=none&encryption=none&headerType=none&type=tcp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA-99.68GB%F0%9F%93%8A
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/IranProxyV2/8813" target="_blank">📅 17:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8811">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akCUkLOMh1T1cLKJJdnU2uHaN-LlQufX30Hie7lzYPLsliT0kt1__iNdte8kH3iwzky2SsEGn93n_Q2c2dJJuBUhEMLpNUcC2Zrc9197otgkpPgMaR30C6HLW6FZ3H5_4m9b8XExbcbmfUSeIRx7Jx4R4DoLPcoX4FbqLq9fUgtHSOuodFzEJMBnsrYYCVZpr6OH1TTQ9nxP3WAxInJYGNXNm--7ym2sBmXxZNI9lkVXBQAXyctkxj1-o9OxztC-U0Q1JM2my1bnfXac9cDFGqpbQBF9fjmtTQwZLJw9RdWB7Q_b_t9cdEFFM0KBK9dwyA7OIeNET8KWQD8vHokbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرغون شده ۴۵ میلیون.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/IranProxyV2/8811" target="_blank">📅 14:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8810">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">vless://cf6da80a-8e9e-40e5-8897-c2f7fba76179@unknownnn.shop:56885?security=none&encryption=none&headerType=none&type=tcp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA-99.85GB%F0%9F%93%8A
100 گیگ رایگان
😁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/IranProxyV2/8810" target="_blank">📅 14:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8809">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLozTggJ_D7FxQvdq4y_W1kulgQA2wb8bqN3p_CmXPMFD1UosFyKna814TtEptyLQ8X8rDqPsde7pIQ_OVLYiNVcMzLbTfJxCPOcJIVsUj6eTMKEhzezXlbmGstFSjB65-9t1zhznDJEdpw7cIxF_zhbTYEo4CXPqxOPGYkWkfV42G34p7dHRONr4Ik87gAG4z6siEWbeV-oLCTv_eiwUzzI61MILjIAHcuSetj_xql0KGbQIyomr0WACB_Jj7a-TjT4_fxlO342-Xjj56S9Bm_w7x9I-GmN2fiAzsszRABy2iNlVx3bKbg7KKG-SouqfhXrH3kBjZSeu7I5kAF5Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سمت چپ: دیتاسنتر ایران.
سمت راست: دیتاسنتر فنلاند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/IranProxyV2/8809" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8808">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKbcwG3nFid-HJbLSJi6guTuOeAzZvPB54qjN64pj6IR3m7dX6QOTL47RFpGOYu5EZUyDvQ4mC_dQLT5A0zjqdwJooneb9fIaiw3Ta8tite5EDIB7Z0v6PgBocBPkojnwCO01jXpZtJlYgrNIe1w6TuthoYFKVUe2JGrZMvIm7VmuIuVlsUpcZaOAiS_sR0Cqd5faRBCD6pxHDx0am_2UuAK_e7mWMKmcmzfqhFaS3AWClxmZ5pKB3s6DjOvJZKtrifSsiBjxFjROmeC0aWfKV1GLoadlwam1ibuMeFVxRzhhfztLwQp6oQclIvb3v7v-zSd76ePIGWv082MzTaxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی باشرفی دکتر شبستری
❤️
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/IranProxyV2/8808" target="_blank">📅 13:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8806">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">https://t.me/proxy?server=167.233.53.71&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=167.233.21.161&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=188.34.162.30&port=8443&secret=dd104462821249bd7ac519130220c25d09
چند عدد پروکسی متصل
💯
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/IranProxyV2/8806" target="_blank">📅 07:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8805">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1TB.npvt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8805" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🔝
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/IranProxyV2/8805" target="_blank">📅 07:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8804">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">XV2RAY -🐦‍🔥.npvt</div>
  <div class="tg-doc-extra">66.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
👑
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/IranProxyV2/8804" target="_blank">📅 07:02 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
