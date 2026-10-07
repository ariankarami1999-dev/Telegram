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
<img src="https://cdn4.telesco.pe/file/H8s6y4IuNhfdVuJzz6SaScoU6rlPufXKjuRHQi51UEzcm6V3pTXF3SFJKsFtj7Ucf43KKS5VCV4jNHo5MOCITinYxXWiOLd6P_DcfkeIr3oNod0E_TgcoRhRfMUJWpxmkkzhjDZOYL3WmAEplPEJtlxMjjM6Of32hNT8V23ELOvl22hc6LJSREXVHE8j8E3oI8iXcrG--TrNlSRvsiZah8S3Uj_WMrOBKzGU1ElrGN53VOCKgxVMYXY2VqyzruZoF7XwnsCPnNat0DQvDaXG9U-WcTBaURRFQRXKO1qXMkHmbMEHhda4ASMIBuR0adsPrRoXXl_XYS9Gv8_nqmPWSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-21536">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجار با دلیل نامعلوم در حیفا اسراییل</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SBoxxx/21536" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21535">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">— حزب‌الله ماه گذشته ۲۰۰ میلیون دلار از ایران دریافت کرد تا به مردم لبنان که به دلیل جنگ امسال با اسرائیل آواره شده‌اند، کمک کند، با وجود افزایش فشارهای اقتصادی ایالات متحده بر ایران و دشواری‌های فزاینده در انتقال وجوه به این گروه.
واسطه‌هایی که پول را جابه‌جا کردند، کارمزد ۲۰ درصدی دریافت کردند که چهار برابر نرخ معمول است و این امر بازتاب‌دهنده خطرات مرتبط با مدیریت وجوه برای حزب‌الله است.
— رويترز</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SBoxxx/21535" target="_blank">📅 19:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21534">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به نظرم وقتش رسیده که یک بار دیگر بکشیمش.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/21534" target="_blank">📅 17:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21533">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مقام ارشد ایرانی: ایران هرگز حق غنی‌سازی خود را رها نخواهد کرد، اما جزئیات غنی‌سازی می‌تواند بعداً مورد بحث قرار گیرد.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/21533" target="_blank">📅 15:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21532">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
تنگۀ هرمز بسته است و نیروهای مسلح بر آن تسلط کامل دارند و این وضعیت تا زمانی که خواسته‌های مشروع ایران برآورده نشود، ادامه خواهد داشت.
‏حجم نفت قاچاق‌شده بسیارناچیز است و نمی‌توان گفت که تنگۀ هرمز برای چنین فعالیت‌هایی باز است اما برخی با شناورهای کوچک اقدام به قاچاق نفت و انتقال آن به نفتکش‌ها می‌کنند.
به‌زودی، تعداد کمی از مسیرهایی که افراد متخلف از طریق انفجار و تخریب برخی از مسیرهای صخره‌ای موجود در تنگه هرمز ایجاد کرده‌اند، مسدود خواهند شد.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/21532" target="_blank">📅 14:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21531">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نتانیاهو درباره ایران:
کشورها، حتی آن‌هایی که به ما حمله می‌کنند، به‌صورت پنهانی و پنهانی می‌گویند: «(حکومت ایران) باید سقوط کند. آن‌ها همه ما را خفه کرده‌اند.»
ما اطمینان حاصل خواهیم کرد که آنها سقوط کنند. آن‌ها سقوط خواهند کرد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/21531" target="_blank">📅 13:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21530">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/21530" target="_blank">📅 12:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21529">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIvyMKXJ24nGEelK9LDa4gX-qRuMezm2gMSfhJkkWgLZUXqeHhwamPvw9e_SLXkJtu-7XDZ0HWXq3vYWrFy5oQNBQaTkOHhx8vxosLKwTNCGrZEW_JU5OBAY0BkKYJ5BN5X5KETx2mjmiTViGTSGtyzm9mOXB8-iC2UdsjBGyQRlyAdl4YgxsevcDQNE500V4puthJIH5eu7Bj8IxHz0ar3857FXM9hQS0HECUQ3xqjVpGQLINI1tkfcz4bMLBJKynrYgjew8JGkfe4E8dslUZEA2GjoS0l8PW7qVHEN28HNdhj4SrOfb1flbAjZdcCj7YgQU_vwxuTUwwQf2JKOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاره پیروزی اژدها (نماد چین) در جنگ با عقاب (نماد آمریکا) در میدان فاطمی!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21529" target="_blank">📅 12:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21528">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXo9aJHrCSlfCWkOvKeDdJEMiL78EY6BD-r96Bh-GVXk-4meRnrG5lfFlNbMabe4UWJuJbtCYOzrtdINBXzLaT8x3R6GkeruurI14VEsQMl3s7QuQFBc2fMrbkEzh1FCFfNAWVcubUvoJ61ZcwOd1bLw9X4rG9ndR0_tOTO8jNitct3R6RC5SqgUbrd8P1UFYypdRZg7GAK7_X5VRj2-LXSy4arRas-iH9AurTkQO4lvh3UL6eh6gEUzzNZXFV_aEpHBZZlpCMN5r47Fdql9paDXHcpGxQqz87lkbPwrvcHx9b6YrUla3Os82-UUUGnzxrQxIzjNZJpNt5hcCt63hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در محدوده قوی حمایتی است و با تریگر می شود خرید کرد. (مطمئن ترین تریگر شکسته شدن کانال نزولی)</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/21528" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21527">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rERppa_Yn4UFa72qnd6LjPQQ4m0cX8VRKT_3oUtUJX66wVHzgWlhIA4KlHtdD8xKC4RpGJ03bIUJxhEV8VyoCWQbDBwXehvKXNV52-LutcJToe9eXtBq2SBIVMiqN4l1R_SXCQo_X6cNtg_PNUycx9lsWl4RgzuHGJxc-9eZdD_q5fJ6jRZiEHoXq504xOYEAFK4LD_VeJvZC484AO0uTSB_mUXyNyA1MmXY08Zt7rQ0YOABpsPyIQg420khal54jD9Mn9eZrjr5eH8ZEkP4dcvjnSJuYNNT0gIGdLr4FgOn-KxMF1qwPqxMAJliSb-TX94vK7g4g_NJcPOq-bh4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC به محدوده بیش—فروش نزدیک تر شده و این موضوع خرید را قوی تر می کند.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/21527" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21526">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV6zX25X7U_ox0iJVLJkV7y0e0qNmKRlwuUIf1_y1H4lHKSGjHfHAZxUWf_vhyIzvDCS8zHzdOy4MCQuWIUUO_WywMaYPll4Old6_vccu4k5GteuDisSd-5cYLLjnQJ2lPPuZBpPVxpVZYtYnMiThaFwHfhIGrglpQ2czWUw2nvd6Y4PHKhDETden6ro7Kl9GYvg-cZ2FbGOC1Q_PeeKB6OH6tzG9dgb-VcYjG-BVzfoD8zhH5DniRpYpfLV3-5cnB7v9IdIhAiebO56dIzGGSijr1zO-IYPVCYUFRs1F4pwVRl_QZTfHC69FkXnqvOuc09w6BPSzPiVNjmn6rYYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش طلا تا این لحظه، خرید توصیه می شود.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/21526" target="_blank">📅 12:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21525">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLcqfvMOZ2ynim4w3DYnNWH58eGjtV1-iFWuq2SteGCyi6p6uMuIxSQBqXvr55qgh3vhCpMiB2Up0JqLMS65xkzcYp-ifVyE7vSCJuzNjeJJ3LqJUzPmhXdsnZMpMWZj1aladvb37uxJlabUQqoML902WcQ83DZ25JvpRbAirWxdnbTcU4elx5Hmrw9UYlPH8igsA-zDofhVu2ejBLTOyrEX2GKQlEWkWjNGb6MW9qd5UuF9t9yKKcnz67GNTTOka0EFR4aG3EHiDoGG4FaNC4lZROkWIHh5zs1DCAcwlwbo1Ez2F3hgBqi1w4TT2PaasBzy0Ye1owadwr8CC8sN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاره پیروزی اژدها (نماد چین) در جنگ با عقاب (نماد آمریکا) در میدان فاطمی!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21525" target="_blank">📅 11:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21524">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">ذخایر طلای چین در پایان سپتامبر ۷۷.۴۷ میلیون اونس خالص بود، در حالی که در پایان اوت ۷۶.۷۳ میلیون اونس بود
اما ارزش این ذخایر طلای چین در پایان سپتامبر ۳۲۳.۵۲ میلیارد دلار در مقابل ۳۵۰.۰۸ میلیارد دلار در پایان اوت بود</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/21524" target="_blank">📅 09:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21523">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تعز به تصرف حوثی ها درآمد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/21523" target="_blank">📅 09:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21522">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
اسکات بسنت :
ایران وزیر نفت جدیدی انتخاب کرده،
با توجه به اینکه آنها از 25 آگوست حتی یک بشکه نفت هم برای صادرات بارگیری نکرده اند، این وزیر جدید عملاً چه چیزی را مدیریت می کند؟!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/21522" target="_blank">📅 08:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21521">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElYCKzhiXT3QdPaJpc8UOyn3w5PUDCxwrXO4D68StEIYYdIuqpeJ3IDhPqcQ3r90Hja8jvmqwfbjJO_A1XJxtwe87AJQ7-dJiOKTh0Hm1OgNdHbQJpkA7QlpocUERMKUUKqnd4GshFz_2V_498HnvwIqqUMbRB9Q6gPMwxMXQ0mwbgj4e25cNDjmCUaUwUGqV5Gc7aKfaaKHXBzaHw-wuEsNEDsXcRpwE1GlYpn2D_kUcwKTCzAiVZzAyIaEo8bV9MyvM8SYqRPn4sdNOV5mrqY7HvASLSg7xS_0gT54E7jdswPgnX3rrPdUPm0pmxjItXK9g0AgOvOhk_eJe6UYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی خب بعد از اینکه به بسنت این را فهماندیم، دلار 40 هزار تومان کشید بالا که مهم نیست چون مهم این است که ما مجبور نشویم بکشیم پایین.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/21521" target="_blank">📅 08:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21520">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21520" target="_blank">📅 07:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21519">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این مدلی بوده که اردوغان تروریست های جهادی ترکمن سوریه را که تحت فرماندهی «تیپ سلطان سلیمان شاه» قرار داشته اند به جبهه های جنگ قراباغ اعزام کرده است.  پس از ورود نیروهای سوری به جمهوری آذربایجان، در جلساتی با حضور رهبر تروریست های سوری و نیروهای نظامی ترکیه…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21519" target="_blank">📅 07:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21518">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آماده‌سازی‌ها برای جنگ میان اسرائیل و ترک‌ها با شدت تمام در جریان است Damir Nazarov  پس از به‌رسمیت‌شناختن سومالی‌لند از سوی اسرائیل، تحلیلگران این اقدام را تلاش نتانیاهو برای ایجاد پایگاهی در برابر انصارالله یمن و کسب اهرم فشار در دریای سرخ ارزیابی کردند.…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21518" target="_blank">📅 00:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21517">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خیلی حرف های بد دیگری هم زده که اینجا نمی گذارم.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21517" target="_blank">📅 00:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21516">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دونالد ترامپ:  تنگه هرمز به ایالات متحده آمریکا تعلق دارد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21516" target="_blank">📅 00:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21515">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دونالد ترامپ:
تنگه هرمز به ایالات متحده آمریکا تعلق دارد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21515" target="_blank">📅 00:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21513">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کاخ کرملین: رئیس‌جمهور ایران روز جمعه در اجلاس سران کشورهای سابق شوروی که به میزبانی روسیه در ترکمنستان برگزار می‌شود، شرکت خواهد کرد و با پوتین دیدار خواهد داشت.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21513" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21512" target="_blank">📅 19:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ:
آنچه در فرانسه در حال وقوع است، چیزی جز مهاجرت گسترده و بی‌رویه نیست. این موضوع نه مربوط به مدارس است، بلکه مربوط به اسلام است که قصد دارد بر کشوری که قبلاً عالی بود مسلط شود! (رئیس‌جمهور دونالد ترامپ)</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21511" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فیلم وزارت اطلاعات از ضربات به گروه های تکفیری در سیستان و بلوچستان!
قشنگ خاطرات بازی Counter Strike زنده می شود.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21510" target="_blank">📅 18:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دبیرکل حزب‌الله:   آزادی جنوب لبنان را پیش روی چشمان خود می‌بینیم!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21509" target="_blank">📅 18:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دبیرکل حزب‌الله:
آزادی جنوب لبنان را پیش روی چشمان خود می‌بینیم!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21508" target="_blank">📅 18:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇫🇷
سفیر فرانسه در تهران به علت برخورد خشونت‌آمیزِ دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر به وزارت امور خارجه ایران احضار شد</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21507" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇫🇷
سفیر فرانسه در تهران به علت برخورد خشونت‌آمیزِ دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر به وزارت امور خارجه ایران احضار شد</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/21506" target="_blank">📅 18:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21505">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بر اساس گزارش‌های رسانه‌های عبری‌زبان در تاریخ ۵ اکتبر، اسرائیل در حال تدارک برای اقدام نظامی احتمالی جدید علیه ایران است؛ اقدامی که ممکن است به‌صورت مشترک با ایالات متحده یا به‌طور مستقل انجام شود.
روزنامه «اسرائیل هیوم» گزارش داد که ارتش اسرائیل ضمن حفظ همکاری‌های نزدیک اطلاعاتی و عملیاتی با ارتش آمریکا، خود را برای حمله احتمالی به جمهوری اسلامی آماده می‌کند. این تدارکات شامل سناریوهایی است که در آن‌ها اسرائیل یا دست به حمله پیش‌دستانه می‌زند و یا به حمله ایران پاسخ می‌دهد.
این گزارش احتمال وقوع حمله اسرائیل یا آمریکا پیش از انتخابات میان‌دوره‌ای ماه نوامبر را نسبتاً پایین ارزیابی کرده و حاکی از آن است که این آمادگی‌های نظامی برای رویارویی احتمالی در زمانی دیگر صورت می‌گیرد.
هم‌زمان، وب‌سایت «والا» گزارش داد که واشنگتن در حال آماده‌سازی برای اعزام نیروها و هواپیماهای بیشتر به اسرائیل در هفته‌های پیش رو است؛ این در حالی است که هم‌اکنون حدود ۳۰۰۰ نیروی نظامی آمریکایی در این کشور مستقر هستند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21505" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21504">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فوری - قطر اعلام کرد که ایالات متحده و ایران همچنان در حال مذاکرات برای پایان دادن به جنگ هستند</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21504" target="_blank">📅 15:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21503">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترکیه و پاکستان برای حمایت از عربستان سعودی در برابر یمن، توافق‌نامه مکه را فعال کردند
آنکارا و اسلام‌آباد متعهد شدند که به‌سرعت نیروهایی را به داخل خاک این پادشاهی اعزام کنند.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21503" target="_blank">📅 15:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21502">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21502" target="_blank">📅 14:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21501">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خلبان آن هواپیمای فلای دوبی هم که داشت سقوط می‌کرد هندی بود!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21501" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21500">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزارت امور خارجه هند:
۱۲ خدمه یک کشتی تجاری با پرچم پاناما در حمله‌ای در سواحل عمان زخمی شدند که ۱۱ نفر از آنها هندی بودند</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21500" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21499">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و می توان در سطوح حمایتی خرید کرد.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21499" target="_blank">📅 14:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21498">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نشست کارشناسی بسیار جالب و دیدنی درباره روند جنگ ایران—عراق و فرصت هایی که برای پایان جنگ وجود داشته است:
https://www.aparat.com/v/goil745?playlist=27887251</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21498" target="_blank">📅 14:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21497">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انصارالله ادعا می‌کند که در دو روز گذشته حمله دوم به فرودگاه سعودی را انجام داده است
انصارالله اعلام کرد که با یک موشک بالستیک به فرودگاه بین‌المللی ابها در استان عسیر عربستان سعودی حمله کرده و ادعا می‌کند که این ضربه باعث اختلال در ترافیک هوایی فرودگاه شده است.
یحیی سریع، سخنگوی نظامی انصارالله، گفت که ضربه موشکی «دقیق و مستقیم» بود و به شرکت‌های هواپیمایی بین‌المللی هشدار داد که از ادامه پروازها از طریق فضای هوایی سعودی خودداری کنند، زیرا به گفته او این فضا به «صحنه عملیات نظامی ما» تبدیل شده است. ریاض تاکنون به‌طور فوری این حمله را تأیید نکرده است.
این حمله پس از حملاتی رخ داده که انصارالله در شب دوشنبه به فرودگاه‌های جازان و نجران نسبت داده بود و پس از آن حملات، مصدومیت‌ها و خساراتی گزارش شده بود.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21497" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21496">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فرانسه برای اولین بار موشک بالستیک جدید خود با قابلیت حمل سلاح هسته‌ای را از یک زیردریایی هسته‌ای آزمایش کرد</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21496" target="_blank">📅 13:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21495">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUg6EBl_aHM_vmp-d7Kd2jydTTHjW7tGmKxNwK4YUNSmdDVCtRSzZMcHIxdt6rTfVnsC7cABdirCbvm11ob-Q73x6y3cnHfLZJnefQuewZArngveCdWEO-NJ3twFiqTehg_53xrSVb3GeygCPqkQWlVxDuHMUXQpwfZoKTPA9bQObgZEqzMCuRvNoIpOUXlMk3IBqRsjSFBlZLhCjyl8WcVxMFq_JgDC9hnLJctnm7gkPiUF3Zn_vBgP2VyFhh55o1JsjGCSMa9tbNPCu0srKCosc7F7sF7EB4cWHIx4KQKcDMiTPtoOoDRZSa4U0UxkIxsAjhQjliedIRlvSRHQVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر وقت یک نفر که ذهنش اسیر تفکر فرقه ای نشده  فهمید که میان توران بزرگ با اسرائیل بزرگ کدام بیشتر به زیان ماست و آن را بدون هراس بر زبان آورد آن وقت می توان امیدوار بود که پویه های ژئوپولیتیک بر محاسبات کلان سیاست خارجی کشور حاکم بشود و نه انگاره های وهمی…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21495" target="_blank">📅 11:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21494">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">موسسه مطالعات جنگ درباره کوشش ایران برای بهبود و ارتقای توان موشکی خود:
ایران به احتمال زیاد در حال بازسازی و ارتقای توان خود برای هدف‌گیری اهداف نظامی دوربرد آمریکا در منطقه و کشتیرانی تجاری از طریق بهبود دقت، برد، سرعت و قابلیت‌های هدف‌گیری موشکی است. سخنگوی ارتش ایران، سرتیپ محمد اکرمی‌نیا، در مصاحبه‌ای با رسانه‌های ایرانی در ۴ اکتبر اظهار داشت که ایران در حال بهبود دقت، برد و سرعت همه موشک‌های خود است. اکرمی‌نیا افزود که ارتش باید برد موشک‌ها را افزایش دهد تا نیروهای آمریکایی در منطقه را هدف قرار دهد و اذعان کرد که نیروهای آمریکایی تا ۱,۰۰۰ کیلومتر دورتر از ایران جابه‌جا شده‌اند.
مقام‌های آمریکایی در ژوئیه ارزیابی کرده بودند که ایران نسخه‌های پیشرفته موشک بالستیک میان‌برد خیبرشکن را علیه پایگاه‌های آمریکا مستقر کرده است. این مقام‌های آمریکایی اشاره کردند که ایران این موشک‌ها را برای گریز از دفاع‌های آمریکایی از طریق مسیرهای پروازی متنوع، سرعت‌های متفاوت و مانورهای فاز پایانی، و از قابلیت پرتاب متحرک موشک برای ارتقای بقای پذیری و اثربخشی موشک تغییر داده است. ایران همچنین در آخرین حمله خود به نیروهای آمریکایی در اردن در ۹ سپتامبر موشک‌هایی با کلاهک‌های مهمات خوشه‌ای شلیک کرد. مهمات خوشه‌ای در ناحیه‌ای وسیع پخش می‌شوند و برای بیشینه‌سازی گستره خسارت طراحی شده‌اند، هرچند اثر هر گلوله‌ به‌صورت فردی را کاهش می‌دهند. ایران در حملات قبلی علیه اسرائیل از مهمات خوشه‌ای استفاده کرده است که عمدتاً برای جبران کمبود دقت در حملات موشکی بالستیک ایران انجام شده است.
اظهارات اکرمی‌نیا همچنین در پی اعلام ۲۱ سپتامبر دبیر شورای عالی امنیت ملی ایران، سپهبد محسن رضایی، مبنی بر اینکه ایران اخیراً یک موشک جدید با کلاهک مهمات خوشه‌ای را در حمله‌ای به ناو یو‌اس‌اس جورج واشینگتن آزموده و این سلاح در نزدیکی ناو هواپیمابر اصابت کرده است، مطرح شده است. گلوله‌های خوشه‌ای تقریباً به‌یقین نمی‌توانند یک ابرناو را غرق کنند، اما می‌توانند عرشه را آسیب بزنند و به این ترتیب عملیات پروازی را تا حدی و برای مدتی مختل کنند. رضایی احتمالاً به حمله ایران به ناو هواپیمابر آمریکا در ۹ سپتامبر اشاره می‌کرد. رسانه‌های ایرانی در آن زمان گزارش دادند که ایران از موشک بالستیک میان‌برد قاسم بصیر استفاده کرد که برد ۱,۲۰۰ کیلومتری دارد و کلاهک بازگشت قابل‌مانور آن برای گریز از پدافند هوایی طراحی شده است. اشخاص مطلع، 3 حمله موشکی بالستیک ایران به کشتی‌های جنگی نیروی دریایی آمریکا در اوایل سپتامبر را در گفتگو با وال‌استریت ژورنال در ۹ سپتامبر «خیلی نزدیک‌تر از حد انتظار» توصیف کردند.
ایران ممکن است این اصلاحات موشکی را بر حملات موشکی خود به کشتیرانی در تنگه هرمز اعمال کند. ایران از ۲۹ سپتامبر حملات تقریباً روزانه‌ای به کشتی‌های در حال عبور از تنگه انجام داده است. یک مقام آمریکایی همچنین در ۴ اکتبر به وال‌استریت ژورنال گفت که ایران توان خود را برای هدف‌گیری کشتی‌ها بهبود داده و خطر برای کشتیرانی در تنگه را در هفته‌های اخیر افزایش داده است. ایران ممکن است از شرکای خود برای بهبود قابلیت‌های هدف‌گیری خود پشتیبانی دریافت کند، چراکه به‌گزارش‌ها روسیه اطلاعات هدف‌گیری ارائه کرده و جمهوری خلق چین تصاویر ماهواره‌ای به ایران داده است که احتمالاً به هدف‌گیری ایران در طول این درگیری کمک کرده است.
ایران به احتمال زیاد با اولویت‌دادن به بهبود قابلیت‌های موشکی خود، در پی افزایش توان بازدارندگی خود در برابر حملات هوایی آمریکا به دارایی‌های ایرانی، تحمیل هزینه به ایالات متحده و حفظ ابتکار عمل راهبردی در این درگیری است. همان مقام آمریکایی همچنین در ۴ اکتبر به وال‌استریت ژورنال گفت که ایالات متحده کارزار خود علیه نفت‌کش‌های ایرانی را در واکنش به حملات ایران به کشتیرانی تجاری، پس از حمله ایران به پایگاه هوایی آمریکا در اردن متوقف کرده است. این مقام احتمالاً به حمله موشکی مهمات خوشه‌ای ایران به پایگاه هوایی موفق السلطی در اردن در ۹ سپتامبر اشاره می‌کند.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21494" target="_blank">📅 11:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21493">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCmQQ_fdfb4qGiT8STg-h40XLk0WlNbNmxtmuyDXA24b_aJ5np5ww9NzUWMIZ3Sq4nlKlOeAowxKr8qAspqklk2VYaSTLFkHfdhG9uYLbjA6P24fLLkXXTJdlijKZ2vFskRggn76U3DgqnJKUMVDte2r9nsTkaII-a9mqnnTCsdBjYbueLVoHP2uGSj6EQcXNQ-hpahttca9loZa4F0QRfRAOh7ETj3VuEyfmcLNGjO9gwPH6Eecbhsd7UlkLXWgtULHOXMdlQtGml8DTq58TF6tO86HC2FkN4g3-Xh9FfSjo6AIDjrZrQMlClfKq2Kmac5ItR4mzCa3-Ro1xOqljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueGap
نمایه FVC فرق خاصی با دیروز نکرده چون قیمت عملاً همانجا است.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21493" target="_blank">📅 10:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21492">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKWwOHyv4ZOp7DDF8uKbTrErOXDcH65D7B24IrwsE848u4Pm5x3fzCdf76-ySo9aLPR5xIMDVjQYNipC3aTfTfvWZA-cUgchlZzinrrmcu2_A7_7ykkl-gwLIGUviPlLa0pls8r7RTzqphZZRuP2YY_Tqx7Fgu26PGYYmMkz-v_juqpb12QdhOqeSTeBWLTweINSj-Y7A2ZF_2R6vm3TQLcsebAFGRLyeQMVPFNzqCO05MinwBCY40VM5-6HVOc_fyKYQtIzCFYBW3bVlziULVGBszgOaO0f71gTBmoPVarBlUuRHyZiLqQrl4mn11-4OBeICbnwE4fqtGrbhORu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و می توان در سطوح حمایتی خرید کرد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21492" target="_blank">📅 10:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21491">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3zYCK-KGoS27Ls9e2yrP8yJJlsvJKWgQ6FBxs66o34bjZJ9Pzy5rPNbOXSdT7WHMEhcDtPovM7g5zDIoJmoysW-FpiycKbitg6FI0bLLXu2VJqlKo1OVYR06-N9DXkImSROfRHl3h9g66yCj9IOHHkCGsdSx4o0oglK0HyJ3eypFZOb5HPFdGJ9ZFH_H2qE8BrbkKasTIxQZQTdxbcbF3JapxsqCubvBDOQZlyzcJCB8z368A54qbMzIBa9wPUG-FxpiuM1f2QEs23qHL8ID6RgGtj5u39H1pW9QThWyw2gGiGzyBDElsOkexfnD8CxMWuj7f6-_ehXDr11-GewRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، استفاده از اعدام با شلیک گلوله را برای مجازات نیدال حسن، که در پایگاه نظامی فورت هود در ایالت تگزاس، ۱۳ نفر را به قتل رساند، تایید کرد.
این اولین اعدام نظامی با شلیک گلوله از زمان پایان جنگ جهانی دوم خواهد بود.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21491" target="_blank">📅 10:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8qG3T_jcrTppRDJD8U99ltYPAes9nW7KhaW3Hpj813UiA14JAApx43DgDFfSNPV5Gv9wOqCpHGq-Z3jGEHFgAUTmz9YNpfBL8aB8T421rh5OYsDkYAXtqVK3Oo7WXrcf7jQBOFqljzBcPtkxpawf0wKiYUZZbH2ii5n-n49Fs9LYi8Twfxol0e4s2ti-uSc5gdvOnWDTrrPX28QuSvOpyk_9esQ8_mUxOW_aHQ1WMoFVVy344-YPMgQDZABvnoNLvrmlkOsrr5ND-6qsRxzdLpQLzTF_WtNumHvVg9VZa9PB5XvMPf9FmMdWF5KVljO_xqExet1J50Z82_tDcA3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طاعونی که در روسیه از آزمایشگاههای قرمساقها نشت کرده، تا ۱۰۰ برابر کشنده تر از کروناست!</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SBoxxx/21490" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💥
«هدف بعدی اسرائیل ترکیه است»
پل کریگ رابرتز می‌گوید که پس از یک کمپین برای شیطانی‌نمایی ترکیه—مشابه آنچه علیه ایران انجام شد—آمریکا به نمایندگی از اسرائیل به ترکیه حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21489" target="_blank">📅 21:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گویا فاکستان دارد به صورت رسمی وارد جنگ ضد حوثی ها می شود.</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/21488" target="_blank">📅 19:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گویا فاکستان دارد به صورت رسمی وارد جنگ ضد حوثی ها می شود.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21487" target="_blank">📅 19:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👤
مارکو روبیو، وزیر خارجه آمریکا
:
«ما طاعون روسیه را از نزدیک زیر نظر داریم و آن را به‌دقت رصد می‌کنیم. فکر نمی‌کنم دلیلی برای نگرانی و هراس وجود داشته باشد، اما قطعاً موضوعی است که باید با دقت و تمرکز بیشتری دنبال شود.»</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SBoxxx/21486" target="_blank">📅 18:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیویورک تایمز:
بیش از ۲۰۰ پرسنل نظامی و اطلاعاتی ایالات متحده به عربستان سعودی اعزام شده‌اند تا مستقیماً به نیروهای مسلح این پادشاهی در هدف‌گیری سایت‌های پرتاب و تأسیسات ذخیره‌سازی موشک‌هایی که توسط جنبش مقاومت انصارالله یمن اداره می‌شوند، کمک کنند.
این مأموریت مشاوره‌ای مخفی شامل تیم‌های کماندویی است که در طول مرز عربستان-یمن مستقر شده‌اند و در کنار فرماندهان ائتلاف برای کمک به جمع‌آوری اطلاعات، تداخل در حملات فرامرزی و تقویت توانایی‌های دفاعی ریاض در برابر حملات انتقامی پهپادی و موشک‌های بالستیک، همکاری می‌کنند.</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/21485" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21484">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کلیپی از کشتار نیروهای حوثی توسط سلفی های مورد حمایت عربستان   در ثانیه ۳۳ فردی که گزارش میداد می‌گوید باب المندب عربی است و نه فارسی ایران!</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21484" target="_blank">📅 17:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21483">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57336f8d3e.mp4?token=m_o0CIhXEPW7DgozIsrS1IqIYjjHmXCjUv2kGcj9vh_-J40r4fHFU9_P0BXU6I5U5c80gPFSbzqR9Sy9WRzjPbWZwloARJ897ouKd6sWJm3HgRmXETa8CyFV_Rjc4nQFZ4_OsQtXRaB-BIsCzLKE8zOud7SM0gJ6VpigYFmSVcinXV27pKdLaxamHMiyDYlFKATwt27YHBI7S2zO1nrmVKIPdZHk3dd7qctztyc2HXiohXsTjPWORxjR8qH8cMQV6yA4fzHBJPGxboPFAnUgbLy13W7mtOhn-HDSRYWMTas19gHBAhlR4xlSE4kKgKLaMvm1U7vHKGMAYq1auWmX9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57336f8d3e.mp4?token=m_o0CIhXEPW7DgozIsrS1IqIYjjHmXCjUv2kGcj9vh_-J40r4fHFU9_P0BXU6I5U5c80gPFSbzqR9Sy9WRzjPbWZwloARJ897ouKd6sWJm3HgRmXETa8CyFV_Rjc4nQFZ4_OsQtXRaB-BIsCzLKE8zOud7SM0gJ6VpigYFmSVcinXV27pKdLaxamHMiyDYlFKATwt27YHBI7S2zO1nrmVKIPdZHk3dd7qctztyc2HXiohXsTjPWORxjR8qH8cMQV6yA4fzHBJPGxboPFAnUgbLy13W7mtOhn-HDSRYWMTas19gHBAhlR4xlSE4kKgKLaMvm1U7vHKGMAYq1auWmX9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا توضیح داده بودم …</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/21483" target="_blank">📅 17:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21482">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">— مقامات اسرائیلی پرونده‌ای علیه یک استاد ریاضیات دانشگاه که مردی در دهه ششم زندگی  و اهل پتاح‌تیکوا است به اتهام برنامه‌ریزی برای حملات گسترده علیه شهروندان عرب اسرائیل تنظیم کرده‌اند.
بر اساس دادخواست، هدف او اجبار به اخراج دائمی آن‌ها به اردن، لبنان و غزه بود.
او قصد داشت ۷۲ اسرائیلی یهودی را در ۱۲ گروه برای انجام حملات هم‌زمان جذب کند، با حمایت از عناصری در ارتش اسرائیل، از جمله حملات هوایی به مراکز جمعیتی عرب.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21482" target="_blank">📅 17:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21481">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اینجا توضیح داده بودم …</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21481" target="_blank">📅 15:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21480">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…  توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21480" target="_blank">📅 15:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21479">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-text">باب المندب؛ قدرت های بزرگ‌ بر می گردند؟!
وقتی ۲۹ شهریور(۲۰ سپتامبر)‌ نوشتم به زودی حوثی ها ناگزیر خواهند شد از باب المندب عقب نشینی کنند، سخت مورد نفد قرار گرفتم.  البته امروزه روز، مساله اصلی این نیست که حوثی ها شکست خوردند یا عربستان پیروز شد؛ بلکه مهم‌تر این است که باب المندب در حال خارج شدن از وضعیت اهرم یک بازیگر غیر دولتی(حوثی ها) و برگشتن به مرکز رقابت دولت های منطقه ای و قدرت های بزرگ‌ است.
پسگرفتن باب المندب از تسلط حوثی ها، در چارچوب بازآرایی ژئوپلیتیک ی پس از بحران ایران ـ آمریکا معنا دارد، نه صرفا یک عملیات جدید در جنگ یمن.
اگر باب‌المندب توسط مخالفین حوثی ها تثبیت شود و همزمان فشار بر هرمز ادامه پیدا کند، یک نتیجه بسیار مهم حاصل می‌شود:
دو گلوگاه دریایی خاورمیانه، به جای آنکه اهرم‌های مستقل ایران و حوثی‌ها باشند، ممکن است به تدریج تحت ترتیبات امنیتی چندجانبه عربستان، آمریکا و کشورهای غربی قرار گیرند. و این برای ایران از خود عملیات امروز مهم‌تر است؛ زیرا در آن صورت، عمق ژئوپلیتیک ی ایران در دو سوی شبه‌جزیره عربستان همزمان محدودتر می‌شود.
به لینک‌ زیر سری بزنید:
https://t.me/Karimipour_K/6256
#یدالله_کریمی_پور
#karimipour_kپ</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21479" target="_blank">📅 15:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21478">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خوش چشم:
اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21478" target="_blank">📅 14:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21477">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لوئیز ایناسیو لولا دا سیلوا و فلاویو بولسونارو به دور دوم انتخابات ریاست‌جمهوری برزیل راه یافتند
با شمارش نزدیک به ۹۹ درصد از آرا، بولسونارو ۴۷.۲۸ درصد و لولا دا سیلوا ۴۴.۸۷ درصد آرا را به دست آوردند.
دور دوم (Runoff) در ۲۵ اکتبر برگزار خواهد شد. این دور به این دلیل برگزار می‌شود که هیچ‌یک از نامزدها بیش از ۵۰ درصد آرا را کسب نکرده‌اند.
لولا دا سیلوا، رئیس‌جمهور فعلی، نماینده حزب کارگران چپ‌گرا است. فلاویو بولسونارو، فرزند جیر بولسونارو، رئیس‌جمهور سابق برزیل، نماینده حزب لیبرال است.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21477" target="_blank">📅 14:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21476">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اعتراضات گسترده در اسپانیا؛ خیزش علیه دولت چپ‌گرا و سیاست مهاجرتی سانچز  موج تازه اعتراضات در اسپانیا علیه دولت پدرو سانچز، نخست‌وزیر سوسیالیست این کشور، به یکی از جدی‌ترین چالش‌های سیاسی دولت او تبدیل شده است.   کانون اصلی اعتراضات، بحران مهاجرت در سئوتا،…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21476" target="_blank">📅 14:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21475">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📌
بحران مالی فرانسه: قلب لرزان اروپا  فرانسه در پاییز ۲۰۲۶ با بدهی و کسری بودجه بی‌سابقه، افزایش هزینه تأمین مالی و رشد اقتصادی ضعیف روبه‌روست؛ وضعیتی که نگرانی‌ها درباره ثبات مالی دومین اقتصاد منطقه یورو را افزایش داده است.  در کنار فشار بازارها، بن‌بست سیاسی…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21475" target="_blank">📅 12:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21474">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgjJ4vYeA4hKfOTUJle-nHMccwZbWpzx8R3GpGxJZaTLFtMntfdXvd43S9gweVBEj4m-sLCuEF2V6dY4ZwS7RmOTbYFzPqNMZ7EWoLK91N8Pys4PSzcFXh-Yb89sz9Ge7Csj-sqtKCLUpiI50zRUX0zivdBM2yjveL_A_dO7j0vIBb5kXthCiUwpFwhRdJROPIlr5n6jxzfxbuyYTGyx40x4-woeWnGfHtbdOBthThtTFhmZahkvBk1F5-SojX4dSGcsf9i5yO8Cs2FhkUl2l_PWAAKDIDO2CnKFQPrEKtvITvZN35WqZR9D7oqJvLAixM6LiaGDrJbLn3RLvlr2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بحران مالی فرانسه: قلب لرزان اروپا
فرانسه در پاییز ۲۰۲۶ با بدهی و کسری بودجه بی‌سابقه، افزایش هزینه تأمین مالی و رشد اقتصادی ضعیف روبه‌روست؛ وضعیتی که نگرانی‌ها درباره ثبات مالی دومین اقتصاد منطقه یورو را افزایش داده است.
در کنار فشار بازارها، بن‌بست سیاسی و دشواری تصویب برنامه‌های ریاضتی، مسیر کاهش بدهی را پیچیده کرده و بحران مالی فرانسه می‌تواند به یکی از مهم‌ترین چالش‌های اروپا تا انتخابات ۲۰۲۷ تبدیل شود.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21474" target="_blank">📅 12:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21473">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiysnIbkfaZog7v806oIoPvvShyk8LUBgkFK2TUbdlqGLRpAOkHAjWDVcJ5iEvxEmAtKtd96qXM4CbbvwHFwOvsx_Z_BLACdPeaCoSL-kIXAit2yzDSEdO7994YSl00TEFRq4WxubVb-QhpyhXkaJlSq16ZCgstkovH06XHcB5L2Q7HEnvbN_OEBlWLuGfXcZRYK2KNSCLi8-yvgBwy_wKdVGg5UaMCWuyoqp_KTQ9AXSTi-2ipv8Aw871B0EoMVEamDobr1tR48_dziSvQ7pEBQWQVS3m_IvxjtrpwBsqTsWdL42iZGn4tCYl6IMYWqx7wDM3L2F6YtfyzEADo1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله  به گشت پلیس در بمپور  بر اساس گزارش‌های اولیه و به گفته منابع آگاه، یک گشت پلیس در شهرستان بمپور هدف حمله تروریستی قرار گرفته است. این منابع از شهادت یک نفر از نیروهای پلیس در این حادثه خبر داده‌اند.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21473" target="_blank">📅 10:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21472">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و پیش بینی می شود طلا رشد خوبی از همین محدوده ها به بالا داشته باشد. (دستکم 400 پیپ)</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21472" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21471">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR0AIHbFBDYOFDOsEzl-gLuflcgRABxfDSz4-evugYNH9AxgOWjyxwqEdd2LToG4Wc2JnGK_p0nPnpdgX4-41lXwc2xbFdzBGHBfEt92_3WuePHNNY3xslbHSU8RpSh1D6MRYY-d60b4uzgro6eVoZf05a8wcBWa4iy-VyVoiNtgZ0v4opAcAEKEIlO64PabOyBt1Dl4NAdh7ej6gDo56hd3Ss54n-QjtYAMOvFP9-zHmKi9amfzqCRS0Gmk1SrZw-GFO-kL8O5VtcG5tcPvuhl7_sjqPclfCiMbZdmtqXo9ff7iRZ5x_whi0cgWwCMPJ0fOne-luVX1CRXZ_JeVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان در سطوح پایینی قرار دارد و فضا برای رشد طلا هموار است.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21471" target="_blank">📅 10:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21470">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCBWXYT4P_TY72y5lpSv1hQhzntFrViY087CJAkBav-obW1wH4uD-QnZb0Fq2SyVI7LE4l63G5i14V7eXBLsP3d4-89ol_nR6OyI6BcfLbW0yasRURADP8KaztYm6hccr-puIwlaecWWPPYAO_FgbgB6IdqN0eEEy-ry9oALZDqHhkepRxT-KH3PLPde8Qv3oD8KPhdNb9V-D4nERUH9k2KjlR7X993fWCOpA9UEqArA1sdUi4WpgZ4TQWBNvPN28osumVaWPM-7gbPLsCkmnpOGEvDl6P6aqjuyqXBX5nJflbiKTW0_MAomOhs2MMmPTQgpe40ieUkK36GxdeGn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و پیش بینی می شود طلا رشد خوبی از همین محدوده ها به بالا داشته باشد. (دستکم 400 پیپ)</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21470" target="_blank">📅 10:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21469">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزیر اقتصاد:   تورم کاهش پیدا خواهد کرد و وضعیت تولید و ارز خوب خواهد شد</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21469" target="_blank">📅 10:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21468">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزیر اقتصاد:
تورم کاهش پیدا خواهد کرد و وضعیت تولید و ارز خوب خواهد شد</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21468" target="_blank">📅 10:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21467">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21467" target="_blank">📅 09:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21466">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISBWA73Xwmv6eE-vBMBB48h9JT4uVbtH9OvC_2B_z5kDezhimCmTM5c4xRC-bktgOjml2K5GDwuf1BD1BMeA3VmXUOu7WbcAZw1EF50-X1hzlD8gir9srZ-KuctluVTty8sVbTNcWkli1j00Di2_d-yPKJcwbtsaa3mDRVUu8C2IxJaK7YybXn_wB7OKR03b9eL__yLS2u_mkQfSiDTx3C6gD5Z5dPzKFGsaxGTQyedQB1Bem4h8HUGItlGznmiy4SvomHSkVlcvtfp-2u9Pnpy55mLxyjfgg5Nk9NdxKqVTaei0Q5GCXqUyxVPdQkgSdjeVrdOgq1SciSjVNnWPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21466" target="_blank">📅 02:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21465">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حضور نظامی آمریکا در اسرائیل در حال افزایش است. در حال حاضر حدود ۳۰۰۰ سرباز در این کشور مستقر هستند و انتظار می‌رود نیروها و هواپیماهای بیشتری به آنجا اعزام شوند.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21465" target="_blank">📅 01:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21464">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حضور نظامی آمریکا در اسرائیل در حال افزایش است. در حال حاضر حدود ۳۰۰۰ سرباز در این کشور مستقر هستند و انتظار می‌رود نیروها و هواپیماهای بیشتری به آنجا اعزام شوند.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21464" target="_blank">📅 01:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21463">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKDviDLNmWcabeaXriO5Hm4NreJSP1PBIRaMSobHOLXU3WP6TpqPygN-Yqx4pT4G2t7NEltfdDJ-rl2xRq2Oi3BCEa4XyPPzcm0WMnovalpMxVGPr48u3CmzLnwEb1-x-AcGLT7aKBaHtmLkRZk3YLBCAatJllyeusN4UsDXbQEa7U4fncjF4ZOjqOTLMtumIDlof-9r2Xso_jtz3lBvP4P9QM8cQszsOAeiiC80ES6_7zZYbdcQl5z2KUB3vHJysO_wZPBIvQ5PEfgx-vsjR9_DkeCvkaiASUCVEQyg-Q7ErYxtcmbWVDTVlAp2nlwZ_3AdP8zYrBJxUBHJ53NZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر سیاستهای ضدمهاجرتی ترامپ!
طی ۵۰ سال گذشته، دست‌کم ۲۳ میلیون نفر متولد آمریکای لاتین به ایالات متحده مهاجرت کردند. این بزرگ‌ترین جریان پیوسته مهاجرت در جهان به یک کشور بود که در سال‌های پس از کرونا به اوج رسید. دولت‌ها و مردم آمریکای لاتین به این موضوع — و به پولی که ساکنان جدید آمریکایی برای خانه می‌فرستادند — عادت کرده بودند.
سپس دونالد ترامپ دوباره به قدرت رسید. در سالِ منتهی به ژوئیه ۲۰۲۶، گمرک و حفاظت مرزی آمریکا در مرز جنوبی ۱۳۷ هزار مورد برخورد مأمورانش با مهاجران را ثبت کرد؛ یعنی ۹۴ درصد کاهش نسبت به همان دوره در سال ۲۰۲۴ که ۲.۴ میلیون برخورد ثبت شده بود. مسیر دارین — مسیر جنگلی از آمریکای جنوبی به پاناما — همین داستان را روایت می‌کند: عبور از این مسیر در همین دوره ۹۹.۹ درصد کاهش یافت. در کاستاریکا شمار مهاجرانی که به سمت شمال می‌روند تقریباً به صفر رسیده، در حالی که تعدادِ رو به جنوب به‌شدت افزایش یافته است (نمودار ۱). شلوغ‌ترین کریدور مهاجرتی جهان ساکت شده است.</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21463" target="_blank">📅 01:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21462">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش از صدای جنگنده های ارتش در آسمان تهران</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SBoxxx/21462" target="_blank">📅 23:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21461">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش از صدای جنگنده های ارتش در آسمان تهران</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/21461" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21460">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">به نظر می رسد محاصره شهر راهبردی تعز در یمن از سوی حوثی ها تکمیل شده و کار نیروهای مورد حمایت سعودی در این شهر به پایان خود نزدیک می‌شود</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SBoxxx/21460" target="_blank">📅 19:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21459">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏ مهدی کوچک‌زاده نماینده تهران در جلسه امروز مجلس:   به خدا اگر از جهنم نمی ترسیدم خودم را جلوی بانک مرکزی آتش میزدم ‎ ‎</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SBoxxx/21459" target="_blank">📅 19:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21458">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏
مهدی کوچک‌زاده نماینده تهران در جلسه امروز مجلس:
به خدا اگر از جهنم نمی ترسیدم خودم را جلوی بانک مرکزی آتش میزدم
‎
‎</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SBoxxx/21458" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21457">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5d6c545.mp4?token=Goqg5O0TBHZipVzg-t5dEZSHqOluzCUiWzaQIgEvNznepXbhIWEg29Dr1wb_r6_qK9nd9NbZIWMRI_Fk2tjeYQ1gfEppM83dZtPSuqe-pY9tPgcIHE7UOEsQXvYLiRDsxjw3g626LIcz_5-cwkyaQUkpciia2wUi9GCYoVuq_v-vy5aOY0j2ZtuJ3Pw1cm-OKqhxuyV0DwORmPOmAcgsXQET2HlyR5T_msPFKIkj7FWpONP3CfoYM-WCo3pXia2k2DAEFCvZxaaW1VPMUISEHyIV3htzXsl7dvHMkwQgZc316m1pWJ5KhAxFK_crVNOzjBKXOY_K5YuaCNGLCl5-gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5d6c545.mp4?token=Goqg5O0TBHZipVzg-t5dEZSHqOluzCUiWzaQIgEvNznepXbhIWEg29Dr1wb_r6_qK9nd9NbZIWMRI_Fk2tjeYQ1gfEppM83dZtPSuqe-pY9tPgcIHE7UOEsQXvYLiRDsxjw3g626LIcz_5-cwkyaQUkpciia2wUi9GCYoVuq_v-vy5aOY0j2ZtuJ3Pw1cm-OKqhxuyV0DwORmPOmAcgsXQET2HlyR5T_msPFKIkj7FWpONP3CfoYM-WCo3pXia2k2DAEFCvZxaaW1VPMUISEHyIV3htzXsl7dvHMkwQgZc316m1pWJ5KhAxFK_crVNOzjBKXOY_K5YuaCNGLCl5-gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار بالن هواشناسی خودمان توسط نگهبانان غیور!
آقایان صیدی و رضا عصمتی!
احمق‌ها کجای این شبیه پهپاد آمریکایی است؟!
هر چه میزنید ناموسا ۱۰۰ گرمش را برای ما بیاورید</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SBoxxx/21457" target="_blank">📅 17:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21456">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گویا حاج عباس پرینت خیلی مهمی در نیویورک داشته.</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21456" target="_blank">📅 16:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21455">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مدودف:  هرگز روابط خود را با جمهوری اسلامی ایران فدا نخواهیم کرد، فارغ از اینکه چه کسی از ما بخواهد این کار را انجام دهیم.  ما شرکای راهبردی هستیم و برای همیشه نیز این‌گونه باقی خواهیم ماند.</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SBoxxx/21455" target="_blank">📅 14:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21454">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مدودف:
هرگز روابط خود را با جمهوری اسلامی ایران فدا نخواهیم کرد، فارغ از اینکه چه کسی از ما بخواهد این کار را انجام دهیم.
ما شرکای راهبردی هستیم و برای همیشه نیز این‌گونه باقی خواهیم ماند.</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SBoxxx/21454" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21453">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سخنگوی ارتش ایران
گفت جنگ اخیر باعث شده تهران به این نتیجه برسد که باید
برد موشک‌های خود را افزایش دهد
و کار روی
سرعت و دقت موشک‌ها
نیز از هم‌اکنون آغاز شده است.
او گفت:
«در این جنگ به این نتیجه رسیدیم که
حتماً باید برد موشک‌هایمان را افزایش دهیم
و اکنون در همین مسیر حرکت کرده‌ایم.
نسل‌های آینده موشک‌های ما توانمندی‌های بیشتری خواهند داشت.
»
این مقام نظامی افزود که
دشمن اکنون در فاصله دورتری از سواحل ایران
و تا حدود
هزار کیلومتری
قرار دارد؛ بنابراین ایران به سامانه‌های
دوربردتر، از جمله موشک‌های کروز دوربرد
نیاز خواهد داشت.</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SBoxxx/21453" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21452">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SBoxxx/21452" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDsT9rwMkfZDKMeers-vwxCluVaXmjKD74TGyycKlC2f5_--2fFTcPjC2CBlib1oXoVpz9vKVRy7d1SreCkVOSVhvgYesP-C78d9lDChB0UHvCb1hQAd-iOncTNKfirFX27eRLYFrSPiNrUjUGO5WOtoO08j-WDlXblwOU3oy-6-G86mLH5PeJ0sLm3pzGT0dNdLCz5ww4KIcfnwX9zvZxbT0yx1tW88tRIB0_cwOjB3I46fKGbGYr0QBLs2ieovt_60MrqXV3rlOZABbROarCny2U8_6zIgeNQu3ED4AIzlr4kP7px80n0PqgMVWVXWgCFlz11oNfZ9zqffxVvYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بار هم که شده فریب نخورید!</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/SBoxxx/21451" target="_blank">📅 11:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شما ولی قبول نکنید</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SBoxxx/21450" target="_blank">📅 11:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قالیباف:   آمریکایی ها برخلاف حرفایشان در رسانه‌ها، از طریق میانجی ها پیشنهادهایی مطرح کرده اند</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SBoxxx/21449" target="_blank">📅 11:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قالیباف:
آمریکایی ها برخلاف حرفایشان در رسانه‌ها، از طریق میانجی ها پیشنهادهایی مطرح کرده اند</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SBoxxx/21448" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بفرمایید ؛  پست جدید ترامپ تو تروث:   «صبحِ شکوه: آیا ترامپ تو جنگ با ایران میره سراغ مدل کامل “شرمن”؟»</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/SBoxxx/21447" target="_blank">📅 09:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21446">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چون نمی خواهم به وحشت افکنی متهم بشوم، فقط به شما توصیه می کنم این قسمت را درنظر داشته باشید و خود بیاندیشید که در «شرایط کنونی» که کشور تحت محاصره است و چپ و راست اتهامات تروریسم و .... به ما می بندند و همسایگان عرب نیز از حملات موشکی و پهپادی و حوثی ها و…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SBoxxx/21446" target="_blank">📅 09:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21445">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد  من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.  اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SBoxxx/21445" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwFs2BKrMPFOD4Tiid9lLI1TU7hMdjcgsYujy1s3TIOWRppaKuKRYmNteVjQQ7UEMAkoqWvOzMsklxH31s7OTcFMSbQJxypLKvOGr93ycvwlMHbWuR9WjyHiX2BAhC5eiMCOvmjCMySE4w1WW_hduiZ8lESCmM1UQB52d1gpYXZjVLq0i4W-6J1D_TzsATOjQYzDyQ1C7C8tv3V0hRAG9ENy3yikNgUkv-3PeUyridmb8tRg6efAnHXmm2qdNWz6DsupbsqTEis_Ipt0j-q9nvV6u8EJDbpnV17eAKKRFnoca8LsZxRHy5UVx_j7CZENrl3YnLQM7FQ84r2hOUETgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">report_onthe_nuclear_employment_strategy_of_the_united_states.pdf</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/21444" target="_blank">📅 09:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21443">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">report_onthe_nuclear_employment_strategy_of_the_united_states.pdf</div>
  <div class="tg-doc-extra">172.4 KB</div>
</div>
<a href="https://t.me/SBoxxx/21443" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این فیلم از این ماده چپول مزدور را ببینید تا بعدا بگویم چه توطئه ای در کار است</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21443" target="_blank">📅 09:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">توطئه در کار است؛
توطئه بزرگ در کار است؛
توطئه ها در کار است!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21442" target="_blank">📅 08:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21441">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد  من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.  اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای…</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SBoxxx/21441" target="_blank">📅 08:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21440">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد
من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.
اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21440" target="_blank">📅 08:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">— وزیر دفاع بریتانیا:
«حکومت ایران نیت‌های خصمانه دارد و تهدیدی برای کشور ما و متحدان ما محسوب می‌شود.
تحقیقات در مورد پایگاه هوایی RAF Fairford ادامه دارد و چندین سرنخ در حال پیگیری است و این موضوع بسیار جدی است.
ما پس از رسیدن به نتیجه‌گیری قطعی در مورد RAF Fairford، به یک پاسخ مناسب فکر خواهیم کرد».</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/21439" target="_blank">📅 00:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21438">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👨‍💻
کارشناس صداوسیما:
چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است
چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SBoxxx/21438" target="_blank">📅 23:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">1-USA 2-PRC 3-N/A 4-IRI</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SBoxxx/21437" target="_blank">📅 19:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">1-USA
2-PRC
3-N/A
4-IRI</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/21436" target="_blank">📅 19:21 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
