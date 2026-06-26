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
<img src="https://cdn4.telesco.pe/file/NaYTvHoa1w6nI-dbIMTPVjIzvNm5vDMpCuDMz_WRBW68T39iSlpjl2a3ayDPAHH5ORIKwvxBitZFEDa75kZkItA6fNfZmN0PFptp5s0FC36l-nlwbUf8TaWbUuazLq3k2zLeqrqQlEY4aBAV4hlq8qYwA_GTB27vcisPR4nzPTJtVPiKuZq80Mzv3q-8gLj4gCVRr6yI1UDRDRBnIs5ODs5RdKm44GKAtUgYepsCbhi1yQh_e1q6iY3MEyHlEL9oblcYApEWamZH19YQVYqP6cdtxKirnYQLNwlc63dSa_dgMjDu8lKot96VoI0tjae610L-HybiZiz_yfmpS7ZLRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 20:43:45</div>
<hr>

<div class="tg-post" id="msg-130368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نیروهای مسلح لبنان در دو منطقه «آزمایشی» که توسط نیروهای اسرائیلی تخلیه شده‌اند، طبق چارچوبی که در واشنگتن به توافق رسیده، مستقر خواهند شد و نیروهای اسرائیلی تا زمانی که حزب‌الله خلع سلاح نشود، در «منطقه امنیتی» گسترده‌تر باقی خواهند ماند، طبق گزارش کان نیوز.
🔴
طرفین همچنین به تفاهماتی در خصوص مقابله با شبکه تونل‌های حزب‌الله و افزایش توان نظامی آن، و همچنین آغاز مذاکرات آینده درباره مرز زمینی بین اسرائیل و لبنان دست یافتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/alonews/130368" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خبرنگار i24news: توافق لبنان اسرائیل حدود ساعت ۲۰:۰۰ به وقت اسرائیل در حضور وزیر امور خارجه آمریکا روبیو امضا می شود
🔴
یک منبع رسمی لبنانی به الجزیره گفت: جدول زمانی برای عقب‌نشینی از این دو منطقه مقدمه‌ای برای عقب‌نشینی کامل اسرائیل در آینده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/alonews/130367" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130366">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ : نمایش هوایی چهارم ژوئیه، بر فراز واشنگتن دی.سی.، پایتخت بزرگ ما، بزرگ‌ترین نمایش در تاریخ ایالات متحده آمریکا خواهد بود.
🔴
صدها هواپیما، از انواع، اندازه‌ها و سرعت‌های مختلف، به نمایش گذاشته خواهند شد. من تقریباً ساعت ۹ شب سخنرانی خواهم کرد، پیش از آتش‌بازی که مانند نمایش هوایی، تقریباً ده برابر بزرگ‌تر از هر آتش‌بازی در تاریخ کشور ما خواهد بود.
🔴
پس اگر به هواپیماها، آتش‌بازی و رئیس‌جمهور ترامپ علاقه‌مندید، حتماً آنجا باشید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/alonews/130366" target="_blank">📅 20:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130365">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزارت بهداشت لبنان: از ۲ مارس تاکنون، بر اثر حملات اسرائیل، ۴,۲۴۳ کشته و ۱۲,۱۸۶ مجروح ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/130365" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130364">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCkomMEcP-1iQiUcInpB7CCshgfOlAFimylpAZuAffO4nujFADbOXAOpc724Pmr7mGLY2Gga9i-qHu6nE2pqL0i5YmKLmR4nG-ZhWCd_ogr3ldvhrNsAyiMlBubEFciJyE7GURmoWFB-UsRQKHspOPmrxAqbS2cLa6ObW2ufontnxqA_IcmDhIkD_SSGDD6p203Euhm1xgvBVj3GdG614hE2v9fBtu4pzEJhBzaXLfeIIevm9rAhgI-4fS5nLmSfCaMv2E3q44J-6sLkd-FHT3j6NO947YDT28eP2AiWahPrOcNwU8UZnu8XSs8BdHQT8yP_rzgDvq8e8IyKl4DNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130364" target="_blank">📅 20:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130363">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI6Qczlei1OZIS97M72B920Cw6YE7MN8PmAkVW_xE5EINY8LpW0I44rGF44DyxLAadBzbyhSKFzkYRSop049u9dntMqp3vKYrh_kFOyThsW217RtPm204ZyzBiOJpPmOXzhHyUoOtvoSkzqa_TGwH4w7o-t3HcibOfqfZTMPD-OUtfD8p3_2dgCIP85kSg6ZYm1e9ZrnEQhu4yvAgRwkSBe3E_w-68FHDGRbZuYZWcO378bZ5bqshpAkBC15VzOwzbo_GFshRGPtB6kFabWooMl5UhNdjxFtCpFUT8qWKjWQRwnZH45Q2vcAjc1y6wDEUd77a4AgdD0LGppDeJymVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی، کشورهای حاشیه خلیج فارس را تهدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130363" target="_blank">📅 20:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130362">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1winPD-PosD-PftPg54CHMoJl8X_iX3MoQmn15C3tBWRuNvKG0XiFZ9IeZeC6sslL_dPRBKY5m1DKqf4QsogLpAtq53nvJ67rS6lIsgLUGBx7GSozQQ0uXZTG3Bt9L3FFJmDhRu3fJCo0gERMuYU-Su05LFPmA7Co34ZudKPTSNvxzbidDnpP_GT6AUO6KWTGGXBRTbN1Mc-GRUoYbfzhFuEPJu73fA7m6yUaJg3MYoZPWiDHpNnvwHcNY79RV2fsUpoaHvxGXA-2smxFx3G0yBB1nKturhIgmGctTsyzgP2cJSvRy71Syag9MZskBdNa261ZTHnUEcpASyujwucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: کشورهای اروپایی متعدد در حال بحث درباره اجرای فوری مالیات خدمات دیجیتال بر شرکت‌های آمریکایی بوده‌اند. برخی از این کشورها به انجام این کار نزدیک هستند.
🔴
لطفاً اجازه دهید این بیانیه به نمایندگی از هر کشوری که چنین مالیاتی را اعمال می‌کند، نشان دهد که بلافاصله با تعرفه ۱۰۰٪ بر هر و تمام کالاهایی که به ایالات متحده آمریکا ارسال می‌شوند، مواجه خواهند شد.
🔴
این تعرفه بر توافق‌نامه‌های تجاری انجام شده با کشور، چه اجرا شده باشند، چه امضا شده باشند و چه نه، ارجحیت خواهد داشت.
🔴
علاوه بر این، اگر آنها پیش بروند، تعرفه ۱۰۰٪ بلافاصله اعمال خواهد شد. از توجه شما به این موضوع سپاسگزارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/130362" target="_blank">📅 20:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130361">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d110c5d9.mp4?token=mtB3Gbyj8-nRsPrLcq-F3O80eMwRSXI2bkhPAcNQYV_BDsOQ6YCMCQWCAPxuhQzQ7Cu-K9QQVg2aYUthpDAvKW_geQjRliA20sh8Mv6t2L3jTkLK_5UEgfncSDe3Mtkzm6dNajlxqL7FLYM2UfOIRAXOHRO6ZnroWn-rKRX2orMKbIj3ZGklFM1366xw-fPIOcnwbq3iAIN8xr8EqeIQcwItRF1h5nn1H4hbLG-zjAXNFHCxNWTqWGJT0aAmancScmL-29L-T1yW7sGZE4_y-fmaT0hscprRqznTDBC_yyaGr0lJp4oIySQ3QpD3sfmafaRYDu0DvCvtzzyOR4xQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d110c5d9.mp4?token=mtB3Gbyj8-nRsPrLcq-F3O80eMwRSXI2bkhPAcNQYV_BDsOQ6YCMCQWCAPxuhQzQ7Cu-K9QQVg2aYUthpDAvKW_geQjRliA20sh8Mv6t2L3jTkLK_5UEgfncSDe3Mtkzm6dNajlxqL7FLYM2UfOIRAXOHRO6ZnroWn-rKRX2orMKbIj3ZGklFM1366xw-fPIOcnwbq3iAIN8xr8EqeIQcwItRF1h5nn1H4hbLG-zjAXNFHCxNWTqWGJT0aAmancScmL-29L-T1yW7sGZE4_y-fmaT0hscprRqznTDBC_yyaGr0lJp4oIySQ3QpD3sfmafaRYDu0DvCvtzzyOR4xQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طبق گزارش ها هنوز 50 هزار نفر در پی زلزله های دیروز ونزوئلا مفقود هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/130361" target="_blank">📅 20:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130360">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91151c5fc0.mp4?token=DtSDiSAONHLfZLjxxcXvVIgjZD02L9jNvuFTMbMqTYDOGtsH_nI21SwvOhlL6T1I1MQCcSUpgIHVpQg6ULQI3TAzXWE6IxgiraqPkpVB1pHdlo9HUTqxLNbd6cswhH-c4_2I9zJaaXNgL7WF7cWVMi18iREoBWdjOUu36HnwAHUkuplYvtbi-FVAekqxwP4iUuBPeqOId46LFJgiE8GsPBTfTmYejmKAJE9gHG3bS4v7QoN3AIXuySDx1H6hmtJSIveYjE5zGjUBFYK6EasofP56LArCzVBnFYB6U_oh-NwmPZI6bavCEtwtWb5Z24imstm6-EkjoDwxOn7b0ZMNoxFSU8NGl2KCczAgM1GrcxE6SFO_DpRibmYxRHCakxAKZehLRgxu6C_pln8DqNV6a7l2brDP12vZZzizBUMuyopAHQ3bK0TxE4N_iuN_auSltOzctWP9ra5aGup05IsZI2ManSvCV2zoZnFI5n0gUI7hsEn_nQg_MiRmf0n7wTMTrd4_nlJAbUCWLIVPYpSP8PRQAFuDEeVHgkeX1TQCYDHRQ7ztQfjyGXFHc62Sa9VtsvBD1TskCsxLC8rP5Stx8xFGUf6pWm4HiIc8iFrAObAaH1-iFNkAMFjvurlvUo4oPwYaJ9M3YpnK0VYHu54Kbk22URPVoV_9-eETRx_l96U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91151c5fc0.mp4?token=DtSDiSAONHLfZLjxxcXvVIgjZD02L9jNvuFTMbMqTYDOGtsH_nI21SwvOhlL6T1I1MQCcSUpgIHVpQg6ULQI3TAzXWE6IxgiraqPkpVB1pHdlo9HUTqxLNbd6cswhH-c4_2I9zJaaXNgL7WF7cWVMi18iREoBWdjOUu36HnwAHUkuplYvtbi-FVAekqxwP4iUuBPeqOId46LFJgiE8GsPBTfTmYejmKAJE9gHG3bS4v7QoN3AIXuySDx1H6hmtJSIveYjE5zGjUBFYK6EasofP56LArCzVBnFYB6U_oh-NwmPZI6bavCEtwtWb5Z24imstm6-EkjoDwxOn7b0ZMNoxFSU8NGl2KCczAgM1GrcxE6SFO_DpRibmYxRHCakxAKZehLRgxu6C_pln8DqNV6a7l2brDP12vZZzizBUMuyopAHQ3bK0TxE4N_iuN_auSltOzctWP9ra5aGup05IsZI2ManSvCV2zoZnFI5n0gUI7hsEn_nQg_MiRmf0n7wTMTrd4_nlJAbUCWLIVPYpSP8PRQAFuDEeVHgkeX1TQCYDHRQ7ztQfjyGXFHc62Sa9VtsvBD1TskCsxLC8rP5Stx8xFGUf6pWm4HiIc8iFrAObAaH1-iFNkAMFjvurlvUo4oPwYaJ9M3YpnK0VYHu54Kbk22URPVoV_9-eETRx_l96U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تام هومان وزیر مرز های ایالات متحده آمریکا: من به اندازه‌ای که به پدر خودم احترام می‌گذارم، به رئیس‌جمهور ترامپ احترام می‌گذارم... من می‌دانم که در درون او چه چیزی وجود دارد.
🔴
اگر می‌خواهید رئیس‌جمهوری بی‌نقص داشته باشید، بهتر است منتظر ظهور دوم مسیح بمانید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/130360" target="_blank">📅 19:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130359">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
تام هومان، رئیس مرزهای ترامپ
:
من نمی‌خواهم حتی یک کلمه دیگر درباره دروغین بودن رفتارهای غیرانسانی رئیس‌جمهور ترامپ بشنوم. او هر روز جان‌ها را نجات می‌دهد.
🔴
وقتی رئیس‌جمهور ترامپ مهاجرت غیرقانونی را ۹۷ درصد کاهش داده است، چند زن تجاوز نشده‌اند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/130359" target="_blank">📅 19:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130358">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروهای ما در حال تحمیل یک واقعیت امنیتی جدید هستند که به حضور حزب الله در این منطقه استراتژیک پایان خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/130358" target="_blank">📅 19:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی تسلط بر تپه علی الطاهر در جنوب لبنان شد و گفت که نظامیان اسرائیلی کنترل این نقطه را به دست گرفته‌اند.
🔴
این ادعا هنوز از سوی حزب‌الله تأیید نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/130357" target="_blank">📅 19:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130356">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIz29DKGTJQZlgI9608X3bECOhn7slUofcYz_DWnm9Yx2McNUiD5odLJ51bH6WNmg1UjW4zQ0RdFBkhnD7yp2gLjPUdfOIy1hHh_kpYt2J4zy7eVQz61lrQmW-soZF7ZniIFqVFHQ1oRASGy16IUg0fzCZ9pmaMBBpLLDUbvCqB6tj0Ed9kPOWteDQ62d7Hg9puYl_ZPdIDNve1SSUvYRH_Pm0z72HHLThPejZKY7sRfnp2dLOKzEFfDpYakowgH-udXT_SgPsV6zWM6F7qJ0_PMGSM1dyhvsFsjm8YEy_ys-HCKxb5FnFgQdTL4wmRTDHOnEbRKcY_sTMKfCJlHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ:  ایران حداقل چهار پهپاد تهاجمی را در یک جهت به سمت کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
🔴
یکی از پهپادها به عرشه یک کشتی باری برخورد کرد و ایالات متحده سه پهپاد دیگر را سرنگون کرد.
🔴
این نقض واضح آتش بس است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/130356" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130355">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
فلاحتی، امام جمعه رشت: شعار مرگ بر آمریکا همیشه باقی است.
🔴
ما با مردم امریکا مشکلی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130355" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130354">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پرس تی‌وی: یک خط ارتباطی ایران و آمریکا در تنگه هرمز ایجاد شده است تا از حوادث نظامی جلوگیری شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130354" target="_blank">📅 19:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130353">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
منابع داخلی: حملات امروز اسراییل به لبنان نقص اتش بس محسوب میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130353" target="_blank">📅 19:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130352">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZq5nKT9O9h8zupCLrcf3u_QjN_sRe-j6fPZUVf0fX4sOfczie6UBo3TahhkSSrrF0OdImUSyKkdqZbe7UymjxLHe0dJMb52Op6oKLoqA9MpktRj5GzmMGWz7eB2d9nRfogHGFNhFnIn2XVUOWMNehdEaDkZwr-92NVQtonZo_dNJQE9Cyerodbw0W2JgsoSLyK781EHQIqdyIzVU7MZ1mYPWHHfTgIHfBoBnQD1733mtWpa_GSygLj0QyIGh5b8yM37m31XsuXncakLRCyDqFyNYfeoLUVqgfXzSfT512_-Jx2ZSYEUIowW1inUFppPiHab6DnbYNcg6Qck7XbsTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: همین الان اعلام شد و من لزوماً از صحبت درباره آن خوشحال نیستم، زیرا اصلاً خوشایند نیست، اما دولت ترامپ بالاترین میانگین نرخ بازداشت روزانه توسط اداره مهاجرت و کنترل مرزی (ICE و CBP) را دارد، از جمله کل بازداشت‌ها و دستورات نهایی اخراج، که به مراتب بیشتر از هر رئیس‌جمهور دیگری است!
🔴
دستورات نهایی معلق به دلیل دادگاه‌ها به شدت به تأخیر افتاده‌اند، اما این نیز یک رکورد است. دونالد ترامپ با وجود اینکه اعداد خود را دستکاری می‌کنند و افرادی را که هرگز حتی تلاش نکرده‌اند وارد کشور شوند نیز در آمار لحاظ می‌کنند، بالاترین مجموع اخراج در ۱۲ ماه را به مراتب نسبت به هر رئیس‌جمهور دیگری دارد.
🔴
همچنین، میانگین روزانه دستگیری و بازگرداندن به کشور، به مراتب بالاترین میزان تحت ریاست جمهوری ترامپ است. هیچ رئیس‌جمهور دیگری به این ارقام نزدیک نمی‌شود.
🔴
بنابراین، وقتی این لایه‌های خبری، کارشناسان، دمکرات‌های احمق و کمونیست‌ها سعی می‌کنند استدلال کنند که ارقام باراک اوباما با ارقام دونالد ترامپ قابل مقایسه است، خوب است افرادی مانند «شانون بریم» که به «شیر و نان» (Milk Toast) معروف است و دیگران، کمی مقاومت کنند — فقط کمی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/130352" target="_blank">📅 19:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130351">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
منابع العربیه: دور آتی مذاکرات میان آمریکا و ایران به‌طور فنی در سطح کارشناسان و با حضور میانجی‌گران طی روزهای 28 و 29 ژوئن در بورگن‌اشتاگ سوئیس برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130351" target="_blank">📅 18:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130350">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وال استریت ژورنال: پنتاگون در حال بررسی انتقال نیروها به پایگاه‌های دورتر از برد موشک‌ها و پهپادهای ایران است
🔴
ارتش آمریکا در حال بررسی بازسازی پایگاه آسیب‌دیده در بحرین، کاهش حضور در کویت و عربستان و انتقال نیروها به پایگاه‌ های دورتر از برد موشک‌ها و پهپادهای ایران است
🔴
به گفته مقامات آمریکایی، احتمال دارد برخی از ساختمان‌ها بازسازی نشوند.
🔴
مراکز فرماندهی و کنترل ممکن است به زیرزمین منتقل شوند و سایر قابلیت‌های نظامی‌احتمالاً به طور گسترده‌تر در سراسر منطقه پراکنده خواهند شد.
🔴
اسرائیل یکی از مکان‌های مورد نظر برای ایجاد یک پایگاه جدید است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/130350" target="_blank">📅 18:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: از کشتی‌ها می‌خواهیم که با پیمودن مسیرهای غیرمجاز برای عبور از تنگه هرمز، خطر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/130349" target="_blank">📅 18:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
عمان به متحدان اروپایی هشدار داد که ممکن است نیاز باشد هزینه‌های کشتی برای عبور از تنگه هرمز را پرداخت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130348" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130347">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
روس اتم: متخصصان در هفته‌های آینده به نیروگاه هسته‌ای بوشهر بازخواهند گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130347" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130346">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=JMjREAO0_vWokp1_DWyPRhtJAjWI_tQgttjRGmdr--pQLn4U_h7-zilgSkHJeLMq2KPYLrS_jqAaTDBSp18qw0eMfesimBVqdRS0lz-SVKB3NNuF7QQDLq9Ozyo5RmM8L9aG2tMOMBVkq_qGx05Wqcu4RN6DNvWSr47edbrb56-FhV55bQ_3Blr7mxrlnelzWNNKZQ1PFw7dV-cD2XGKcxSAoh6aZKc2tvvq1XyPxDXX7YlUabP-UzmD8WDD0p972coXEjGJinf1DSHaZ1pyToWYCexEsm5C94adPsn3dkUIZD_edT4ozJ5vE-xVsx9aZ5b9BnCEwWRMkez6gvTWHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=JMjREAO0_vWokp1_DWyPRhtJAjWI_tQgttjRGmdr--pQLn4U_h7-zilgSkHJeLMq2KPYLrS_jqAaTDBSp18qw0eMfesimBVqdRS0lz-SVKB3NNuF7QQDLq9Ozyo5RmM8L9aG2tMOMBVkq_qGx05Wqcu4RN6DNvWSr47edbrb56-FhV55bQ_3Blr7mxrlnelzWNNKZQ1PFw7dV-cD2XGKcxSAoh6aZKc2tvvq1XyPxDXX7YlUabP-UzmD8WDD0p972coXEjGJinf1DSHaZ1pyToWYCexEsm5C94adPsn3dkUIZD_edT4ozJ5vE-xVsx9aZ5b9BnCEwWRMkez6gvTWHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌کمانی و برگزاری مراسم حمایت از جامعه LGBTQ در ورزشگاه سیاتل
:
ما اینجا برای فوتبال هستیم، نه مسائل دیگر. تمرکز ما بر روی مسابقه و کسب موفقیت است. درباره موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
@AloSport</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130346" target="_blank">📅 18:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130345">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130345" target="_blank">📅 18:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130344">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwdmNYLYPFdWvWd_1tt5R2Hl_-rvVRsjWZS6IKA8Y1KE0qwdgm_EYyAeJaam-48jfq3DFhLGKQrIdWLHP9IYwOSnKoAZjtVm-iPJOxGxi2pgUDSfSYahCQ00xlPKH7TjLPuhwAtpPoMIa9uhlL4SzhVE4J8B8HgSpGeawd07pDTtrRTHzEgYWNT3E5U5CT_2GRK47yawNSTslbYmmAdCHwlclhgPlTgdx5r6xx5YqwWSsFquQqWKh5Ya-n1jmnsk8B9zAuIAh3Is9ChsDdOf3ElT25gY9EiZHnPG3gBtEStebqdln_OaIFVloc6cJNbdtsJ7Jl77PoqslMIqTJwYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان به همه مشاغل علاقه داره به‌جز ریاست‌جمهوری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130344" target="_blank">📅 17:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130343">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
۲۲ خدمه ایرانی نفتکش توقیف شده توسط آمریکا، در کراچی تحویل سرکنسولگری ایران شدند
🔴
۲۲ خدمه ایرانی یک نفتکش که توسط ایالات متحده در آب‌های بین‌المللی به طور غیرقانونی توقیف شده بود، با پیگیری های سفارت جمهوری اسلامی ایران و اقدامات تسهیل گرانه دولت پاکستان، امروز به نماینده سرکنسولگری جمهوری اسلامی ایران در بندر کراچی تحویل شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130343" target="_blank">📅 17:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130342">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نعیم قاسم، دبیر کل حزب‌الله:
«ما در کنار ایران خواهیم ایستاد و می‌خواهیم متحد باشیم زیرا مشخص شده است که قدرت شما، همراه با قدرت رزمندگان مقاومت در میدان، به ایجاد تعادل مناسب برای شکست اسرائیل و اخراج آن از سرزمین ما کمک می‌کند».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130342" target="_blank">📅 17:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130341">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">دعوا سر نذری تو همدان
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130341" target="_blank">📅 17:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130340">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی:
همسایگان جنوبی باید پاسخگو باشند: چرا خودشان برخلاف اصل همسایگی خوب و قواعد بنیادین حقوق بین‌الملل، به تجاوز علیه همسایه مسلمان خود دست زده‌اند و اجازه داده‌اند از خاکشان علیه ایران استفاده شود یا موشک‌هایی از آنجا پرتاب شود؟
و چرا چشم بر مسابقه مخرب تسلیحاتی و خرید و انباشت صدها میلیارد دلار انواع سلاح‌های پیشرفته که هیچ توجیه دفاعی ندارد، می‌بندند؟
و چرا تجاوزات مکرر رژیم صهیونیستی به کشورهای منطقه و اشغال سرزمین‌های فلسطینی، لبنانی و سوری را نادیده می‌گیرند؟
چرا در برابر زرادخانه هسته‌ای اسرائیل که خارج از نظارت‌های بین‌المللی است سکوت می‌کنند، در حالی که توان دفاعی متعارف کشوری که بارها تهدید و حمله از سوی کشورهای همسایه را تجربه کرده، به عنوان «تهدید» معرفی می‌شود؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130340" target="_blank">📅 17:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130339">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8be098ed9.mp4?token=qdflj8Dy5x44rRuxz66sl3WsjtNnyvV6JiwuZihy96Z5-FiSYEFIqBjM-LvNAlYHGzjyQ-sC_CGv7XE_OY63cwmw_-WpgSLB1bDPYPIJUgfGgV1AE94c5ZZN5P9MxEwS8EGkwxfwwcPATtRwNuoN8nieQ-QucygOlCSfHG3svwkG8bkKQGcq63MdXN3mgZM_rAyVdN0nkgKyhI-JdYCK8Vf-FYO_A4PVz-3GyVL5jnBocBPic1lXdlsz8m432fq0ItSPkM08idTu-FuCjhctR0Kv-bI-Bfj7KcCt_zKxHe9lj0TOR6gcbMm8iZGAmJR5DUy4q-H0uOv4q-b441X54w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8be098ed9.mp4?token=qdflj8Dy5x44rRuxz66sl3WsjtNnyvV6JiwuZihy96Z5-FiSYEFIqBjM-LvNAlYHGzjyQ-sC_CGv7XE_OY63cwmw_-WpgSLB1bDPYPIJUgfGgV1AE94c5ZZN5P9MxEwS8EGkwxfwwcPATtRwNuoN8nieQ-QucygOlCSfHG3svwkG8bkKQGcq63MdXN3mgZM_rAyVdN0nkgKyhI-JdYCK8Vf-FYO_A4PVz-3GyVL5jnBocBPic1lXdlsz8m432fq0ItSPkM08idTu-FuCjhctR0Kv-bI-Bfj7KcCt_zKxHe9lj0TOR6gcbMm8iZGAmJR5DUy4q-H0uOv4q-b441X54w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوروش احمدی: اگر توافق نشود، ترامپ به سمت محاصره می‌رود، نه جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130339" target="_blank">📅 17:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130338">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130338" target="_blank">📅 17:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130337">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130337" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESkIfoLUtO5zKbXFH_4ynWatLtMsAdj5IB8HbOijX2XjEiicTRqWxok0NSiG4WvxEZZErSGVxdoJSPTTiQc90hrwjwTG9Yx0_uoa7ojDVq6sRKmB6adsSxs0ahjWN1QTFYuRXUGftk3J_SowWxlGZ4vFQB_mqsJ46g4rGqTl46eW154UVzQPjVBNyfXtIGixr-ADF0SgXILQMUuN0W_ZC3aflG4qqnSgamPiBoLNdI_ezoYRd_bSjI1oS7_XzcbvMR3QQWYK52MLkB1-EgWhr_VynFLZhe4pPeKE0qTBsAyapi_7v0nfQr4VIi2WFP8N_YxVHcD4aUkw4YX23U4pAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130336" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130335">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
العربیه: دور بعدی مذاکرات آمریکا و ایران در ۲۸ و ۲۹ ژوئن در بورگنشتوک برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130335" target="_blank">📅 16:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130334">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a208c87a.mp4?token=kuNSzJn73GUvRDzItgvueAUxh1nfuEXgPOtrGIb7F5jIAZuI1MK1Z_O2_WQclXt6kELlFfNLh9AEzwpSfR4XucNiIal0jtFfpQoxWV0Bionl9EfC-hI7jV-LERD2-rR0wJoTa0yrKEIWvtaH9bKdWKpXssXsW9ZSqXNWfCcEdjPdiyoOum-UZPNlGsC0u5-cegnpPVNuL7WrdHO8L8x1DYFC3TPfPSzKDHb4E_ddj5EArquoFjNbSTt7tCQley24vamlpbidUDlK3KdDOfgPkp6XSBseKoXPX6UNZsFZmrte8JzBcyrRQNDiGDbRMbmT9v-Ku7A1uCYOt7mZ0XX6eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a208c87a.mp4?token=kuNSzJn73GUvRDzItgvueAUxh1nfuEXgPOtrGIb7F5jIAZuI1MK1Z_O2_WQclXt6kELlFfNLh9AEzwpSfR4XucNiIal0jtFfpQoxWV0Bionl9EfC-hI7jV-LERD2-rR0wJoTa0yrKEIWvtaH9bKdWKpXssXsW9ZSqXNWfCcEdjPdiyoOum-UZPNlGsC0u5-cegnpPVNuL7WrdHO8L8x1DYFC3TPfPSzKDHb4E_ddj5EArquoFjNbSTt7tCQley24vamlpbidUDlK3KdDOfgPkp6XSBseKoXPX6UNZsFZmrte8JzBcyrRQNDiGDbRMbmT9v-Ku7A1uCYOt7mZ0XX6eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این سکانس مختار دقیقا برا این روزهای جلسات دورن نظام ایران ساخته شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130334" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130333">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554e768468.mp4?token=XZvarDJKSDZF7n_BPmobNt1TeXaXY3PAmzDfbS6OImbGQKB6_ZMMEQ610Q5XvVuDZeSVJ9dbC2yhiXTRA0Ka6GbSh5X_Y1U4HZEKMVfGk0hSGrZayN9Ui47lG6XX_dLvtTcqF5IhDSJ3qCCufVzXw1fBt-0gWw_SQGHQAPMHKgt1kWuYiYmj0g_z7jVahHGd3m7zaU3WI8fFtNAUG-6sHj0ua504pxIQnJCc_pUWMG2pa0jeu4Kc7dxEjA6YN1OTocNQ57LrWHUaKXs6zb-XAQqLhY9BLJJKPi_FOGfTmyFbb3NkEqIPdbzEUqAFRb0oabv_E14PeP5cSPqTnb1asQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554e768468.mp4?token=XZvarDJKSDZF7n_BPmobNt1TeXaXY3PAmzDfbS6OImbGQKB6_ZMMEQ610Q5XvVuDZeSVJ9dbC2yhiXTRA0Ka6GbSh5X_Y1U4HZEKMVfGk0hSGrZayN9Ui47lG6XX_dLvtTcqF5IhDSJ3qCCufVzXw1fBt-0gWw_SQGHQAPMHKgt1kWuYiYmj0g_z7jVahHGd3m7zaU3WI8fFtNAUG-6sHj0ua504pxIQnJCc_pUWMG2pa0jeu4Kc7dxEjA6YN1OTocNQ57LrWHUaKXs6zb-XAQqLhY9BLJJKPi_FOGfTmyFbb3NkEqIPdbzEUqAFRb0oabv_E14PeP5cSPqTnb1asQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقلیت کم عقل در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130333" target="_blank">📅 16:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130332">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv9Qbw6yMnKRjrnlGJ_0pkZ0BCk0iPLzfuenfSZw5S9Ix5a742_pyGixOt-gG4L1LRuLatJN6L43hpl3oBjhPTEL4KML7SD-PbI9hUm_7vyNpgXdh3r71guxg4EotPcaZafFiWmPzgpmxkdmtfsJfeLaJHjZ1VlRRzBzW66Lj7RI0lWiXgAodDGiX5ZM0dTFP2QlBdXo1_OHyrS2eQUGxBtRX_3u2fpmMo5s20GEMdYrH-ruQUez2Y7jNuQiXh66S7rtBqDYtV0Z7HB18CJn2AHZDNttw3vhyjNdPPoiM4ttZ8bU4ZxphMPXGVXTm2D2H7KNQD6dOOL0hyKaVTBzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش وزیر دفاع اسراییل به سخنان سردار قاآنی: اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباهی خواهد بود که تاکنون مرتکب شده است.
🔴
نه هرمز و نه شلیک به غیرنظامیان در اینجا به او کمک نخواهد کرد. هیچ چیزی ما را متوقف نخواهد کرد.
🔴
نیروهای ما آماده‌اند تا کار را تمام کنند.
🔴
وی در انتهای توییت، پزشکیان، قالیباف و عراقچی را تگ کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130332" target="_blank">📅 16:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130329">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkTAjy9CKjy_DUszSCx53fSeLtx7t31IRWHdOVUUwSafzjdgmU6AQhjuTMro-vIXR2V2OevIrWVt3N1x_dGjVRL6kROuJCsx1hs3lkY6r6SNIlAu17ICgf6VcZmkqYxPzWTjYjpWK742XEi3qi0ZEQbZlmgaQK6lSiXSmP00SGO6et8dwA-K_wbPWdv6t79bx8lx1xLLbv0mKz11hBvHaKj-ABf4QxQom6qTLCVUZNGcBIL_cNER7VKtmcVXljnezxQbl7oSdxNr9bWoJeT9BwZeyTos3th5aiF8qEwDzn8xv8kbY0zOs1uFmZdZ-4kd4ASashLJZW445vhRDDdwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOhKwUB3M6hSKZonk-w-HTbUW5AzVR5dOvgCS_QjaMPUOv2Zk61YOunycYB0hrCRj_i2R9EGZl0xkjF9SrK-FosMpsYBjhfAKygymGYFV4plm8VjS0RjULbMT2FEqicBwwYZU9VF5rSs3R6w73OLbKVKTYDWIa5gD97qka8K9TPDNjzD9txIizUKe19NWjIqwWiDc4HpYWUg4nh7iAjjjUgC6bMGqURa8XsErRlxKAfww_f4CvF6W7vgjWi8aX161uhla6tM7aLezS0G0d_fKDFBaK9JFBF2kmu9ZylV3vA12ZrzzDKLfBEYMh9xR_X0XXIuYvslCuIvYGVnGKZw6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=PZ6iqmxdQBjL_4xoPhvxijCEJ8pKrqbbxde_qqGZrzjyzdEsfTBkRZ9KxDcOiuhAbx2Z2i4h9piBswGUnVeE6jU2RcgqZlVe5bBvttNk8k1qJkT5Ub5TmhYNzJg8-boXPEnqiv2cU_0GdY2A92UZh8V1UsTLi5eVuXDZY4MpmgXTlwrlDATJICf8mSJfpeTUGZLntY0e-O5gLenM1tx6DNYdl-HNCUNDOy6uIxF1uw3fXwNKS7gBsfzgk3dZGVSj7_DiPqy9ocwnfe8Z5AwFeSHt8RlV8C5ri5SkAXXK55t252sMoB1BL1RItSvvQQ9zO3zQJfssRRR-8kUAJ_-ILA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=PZ6iqmxdQBjL_4xoPhvxijCEJ8pKrqbbxde_qqGZrzjyzdEsfTBkRZ9KxDcOiuhAbx2Z2i4h9piBswGUnVeE6jU2RcgqZlVe5bBvttNk8k1qJkT5Ub5TmhYNzJg8-boXPEnqiv2cU_0GdY2A92UZh8V1UsTLi5eVuXDZY4MpmgXTlwrlDATJICf8mSJfpeTUGZLntY0e-O5gLenM1tx6DNYdl-HNCUNDOy6uIxF1uw3fXwNKS7gBsfzgk3dZGVSj7_DiPqy9ocwnfe8Z5AwFeSHt8RlV8C5ri5SkAXXK55t252sMoB1BL1RItSvvQQ9zO3zQJfssRRR-8kUAJ_-ILA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
🔴
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
🔴
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
🔴
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
🔴
شمار تلفات هنوز مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130329" target="_blank">📅 16:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130327">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9KsudorPoSM-JdC9319HZYImXA1G0pILXnoxj3TXrLTKFh2OrZYC2kPR63bAb5NiNVXBM0T0io1XlljBQizcUhVKqYJ6eZ_UoIbT-RtkFIQ_ZWcQbAzlrhcp0FcehAuNN0mV7sJFN_nlKFS7hniZfUVBNyxKUJXVvNpbc_YXCdITLu0r28UR7Tow3rI_qXO22YlknPYY3es7PfamOPNNAt4wC0nr-Un01SbOcWqtN_gUcsMxEk_OtmV96nd3COPVn4_qGTthX78RzMizRKNbj_9wRcUNb-FE27vvBVdSvnkEcJbOwo-qVvCCr02GO_aU7q6x4l4wJ4nB6MuVD2FmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازی ایران و مصر که به عنوان مسابقه «افتخار همجنسگرایان» نامگذاری شده؛ فیفا اجازه داده فردا همه با نماد و پرچم رنگین کمان
🏳️‍🌈
بیان ورزشگاه و معلوم نیست صداوسیما چطور میخواد بازی رو پخش کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130327" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130326">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3a84c436.mp4?token=FIVnxc69AUCo16QHIT-ubrKd1cxzmqPDN0D6iPnWn5AIIYLgLVJrkgpr_HK2R3Y8_PCRbfsi02v36JMjif-ZdwnNSLsAj2yEzQmSjVACi9OoCPS2iwaiuA5262s0rLHaYcDS2hwGOnh4yrPcermgBPyU_GFITOxXf28FcYSSYbivHs5mRt-vL4-tQHGsmRae6j0aXbnXfG2ry-5RaM-IOvmD9-WyePIsHm5J8NfRzZPxYKC3iqB1v3Uk5ej5eUz5TlwXqXlzi3_z8pkvoKov3TbSHlubCgk576sgD5eogfNTKPRXJ5yOqwRLX7jvHxW4gha_PVl52uBcVAaYMetyYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3a84c436.mp4?token=FIVnxc69AUCo16QHIT-ubrKd1cxzmqPDN0D6iPnWn5AIIYLgLVJrkgpr_HK2R3Y8_PCRbfsi02v36JMjif-ZdwnNSLsAj2yEzQmSjVACi9OoCPS2iwaiuA5262s0rLHaYcDS2hwGOnh4yrPcermgBPyU_GFITOxXf28FcYSSYbivHs5mRt-vL4-tQHGsmRae6j0aXbnXfG2ry-5RaM-IOvmD9-WyePIsHm5J8NfRzZPxYKC3iqB1v3Uk5ej5eUz5TlwXqXlzi3_z8pkvoKov3TbSHlubCgk576sgD5eogfNTKPRXJ5yOqwRLX7jvHxW4gha_PVl52uBcVAaYMetyYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده تا از مزایای عدم توافق و مقاومت و بدبختی بگه
🔴
نون این جریان تو بدبختی مردمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130326" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130325">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
مهار آتش‌سوزی در پتروشیمی کارون
🔴
روابط عمومی پتروشیمی کارون از مهار آتش‌سوزی امروز در این شرکت خبر داد و گفت: این آتش سوزی تلفات جانی نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/130325" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130324">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ایتمار بن گویر وزیر امنیت داخلی اسرائیل به کانال 7 گفت: آتش‌بس در لبنان نمی‌تواند پایدار باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/130324" target="_blank">📅 15:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130323">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
هم اکنون، هشدار تخلیه ارتش اسرائیل برای شهر منصوری در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/130323" target="_blank">📅 15:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130322">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فارس: مذاکرات بر سر بحث هسته‌ای برای بعد از حاصل شدن توافق نهاییه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/130322" target="_blank">📅 15:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130321">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955a11f8e7.mp4?token=MT67oYDsz1A1Jsl7X5_4bai6SAhl51c3XsHbRmiI5ZXpOwhUHoCn22N8KwexdBb15bqCCCyNGgYR6O0JhFsmYaCpl6AOg7aRLIzsihaF5XsjVZIUtOQoo0ytp7NR_4ElHCxY78z0rn8OkAWT8nqmja8-pOK7htLY3-nViZ2hsyI1b4OpsHqZZzAPdUgHERVHvBdI0NhmzBgoD99Tceq86_WKxVqtm0Nsf-ZdG18LP3Oz_gsHyQwD02PDO3rOctOAIrHKquyhYLLEZvnrcv9XjHiBD63mGyFYdtmP9l5yTtLpfFEX1Zg1MNylpRaVtkP7ncBSoM7LlyBn5vadPqsHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955a11f8e7.mp4?token=MT67oYDsz1A1Jsl7X5_4bai6SAhl51c3XsHbRmiI5ZXpOwhUHoCn22N8KwexdBb15bqCCCyNGgYR6O0JhFsmYaCpl6AOg7aRLIzsihaF5XsjVZIUtOQoo0ytp7NR_4ElHCxY78z0rn8OkAWT8nqmja8-pOK7htLY3-nViZ2hsyI1b4OpsHqZZzAPdUgHERVHvBdI0NhmzBgoD99Tceq86_WKxVqtm0Nsf-ZdG18LP3Oz_gsHyQwD02PDO3rOctOAIrHKquyhYLLEZvnrcv9XjHiBD63mGyFYdtmP9l5yTtLpfFEX1Zg1MNylpRaVtkP7ncBSoM7LlyBn5vadPqsHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی سپاه: عبور از تنگه هرمز فقط از مسیرهای اعلامی ایران ممکن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/130321" target="_blank">📅 14:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130320">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d81ff4ef1.mp4?token=bjc4NjpMm9qYenhPQc5aLLH47bUuWpI7q35c6PrHCgLYdN9CST2mxS5k3VFmEl_M8HFCjAxzOTfb9IqACihdjJfkRlt3VYeQh6sfoPXzZu9aKwlCf1m7X0gizaZ0rVeeZi4rbM9At-r7vGCB6oUi8LBrEABxKtEr7Y0CRqLE7wxWF-J6WXXphOwANlDsDa4ZioMcVukgqcosAa7QBbtx0xvyPF571xpE80mwpwgDjgV_cDZWllilLKa_EqgzDtHxhDvW-KXCML6jEYRmjOjFPc9G_F8b1oIDcW8Cb8mTj-z_IcwBy3I7mARQV_Zaixtx5Pxcgw0Og1cJ1QGrMJZBCmbboCk0jx_Gdz9RXRwwWX_Lr4sgywbqyxdLJVIOE6Eygg8z6gSr7oJV02P5ru6Ds7BhEVWf6OEmvnPY3RSLAp7_qjmMhLzaeD0TmTVb-U3QsXCvpk3W3tAsNmMBrzXA9Ujn8uY3RuMSCBNO3dkkNeES0JMWOotWrVStJ9peyGM1GZOwfxZhQC09uJYe5yDuhZvzPpd9oX9A4S4KWyWgxe4Oi90GtJPswvBgBp_5lM3L5H-Z4omrpOAXbW2s8YAyYZ8Ja56yawpW1aYJ_LdK9XDtyIB2s4dQNu2Br766u4Idz9dBhMZj5Bv4oyi6VGaJq40dZ_jpSCLqpRPieHGZ7AE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d81ff4ef1.mp4?token=bjc4NjpMm9qYenhPQc5aLLH47bUuWpI7q35c6PrHCgLYdN9CST2mxS5k3VFmEl_M8HFCjAxzOTfb9IqACihdjJfkRlt3VYeQh6sfoPXzZu9aKwlCf1m7X0gizaZ0rVeeZi4rbM9At-r7vGCB6oUi8LBrEABxKtEr7Y0CRqLE7wxWF-J6WXXphOwANlDsDa4ZioMcVukgqcosAa7QBbtx0xvyPF571xpE80mwpwgDjgV_cDZWllilLKa_EqgzDtHxhDvW-KXCML6jEYRmjOjFPc9G_F8b1oIDcW8Cb8mTj-z_IcwBy3I7mARQV_Zaixtx5Pxcgw0Og1cJ1QGrMJZBCmbboCk0jx_Gdz9RXRwwWX_Lr4sgywbqyxdLJVIOE6Eygg8z6gSr7oJV02P5ru6Ds7BhEVWf6OEmvnPY3RSLAp7_qjmMhLzaeD0TmTVb-U3QsXCvpk3W3tAsNmMBrzXA9Ujn8uY3RuMSCBNO3dkkNeES0JMWOotWrVStJ9peyGM1GZOwfxZhQC09uJYe5yDuhZvzPpd9oX9A4S4KWyWgxe4Oi90GtJPswvBgBp_5lM3L5H-Z4omrpOAXbW2s8YAyYZ8Ja56yawpW1aYJ_LdK9XDtyIB2s4dQNu2Br766u4Idz9dBhMZj5Bv4oyi6VGaJq40dZ_jpSCLqpRPieHGZ7AE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه ۳: این تیم پیر دفاعی، ابزار بازی جسورانه با مصر را ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/130320" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130319">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V05oyUP-t3j-gStrFqT_D0RhOTzWtyI2yIRc_ZEdV-AREmVvO2jOV4OCtKuTzUS131-MQXUbdnA5XPpja8jBZ7NJJQzQaGcBmOsztLmh0CsrRf5a1XTrKxi_PGeZHes2-wT3iufUxCqG7v3Uqy7oQfp5JHwHop9NbprjSQCeCMsujDrNT0bnqyoIA-w9yHKBN39RFQNAF8coe-ulLCszSVyf2RZ8V0EeU2YTY7vbAjhXqKx2pivCxoox_Yu_LDX6S0a37qQG1RanLPetaA67os75LizaglL_y7jXRchTIplMpXj7UduTrOFOsliE6qVZlys8siLH5Lq_fShZWmUboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آغاز پروازهای فرودگاه کیش پس از ۴ ماه وقفه
🔴
پروازهای فرودگاه کیش پس از چهار ماه وقفه با ورود نخستین گروه از مسافران و گردشگران در سال ۱۴۰۵ از مسیر هوایی به این جزیره آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/130319" target="_blank">📅 14:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130318">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل:
در طول این هفته ، بیش از ۱۰ ترور در غزه؛ ۶ حمله در جنوب لبنان؛ بیش از ۱۰۰ بازداشت در کرانه باختری داشته ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/130318" target="_blank">📅 14:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130316">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSrNgRpgQl9SlJFl5H2FAhL-BXPXUqbomTK-Zr94kx3YdQWG9Dup_vipnV169mjzrHDNvJeTs2Wfv_uNhXFD0zbbRynEVAGpkcOP1JnvnFBlde-x21J6U81zquebGyneff_nSTk6SjY-DHDUGx7gddrX1P8CUZwz8fT8BsJq-cnWmhCF6oCtBxZXJJ4V3yrQgMmYJpDkaQHRfHezqoq9fEJRr0OEfiG3VUO74Oj6uIuJKl-o-1DZAV8JgQyN5oH_7Sk289XoSYevzg_C6dmbziWDeqXj6t2WchSKVmcm6_JO0YNwyQZO9tgkLAFOhdurznEmuVtWorMdti2OjP_g3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس شِلتر:
مذاکره‌کنندگان وصل به شبکه یهود هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/130316" target="_blank">📅 14:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130314">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52da7df95b.mp4?token=O83G5KsPAamuItBWM0UaVKXeLEvVXeIbiQEIWO14qNFNFYziIwFKFrMQO9OOfDVrLd-RpyavfLV3QtfNk32aSbliOgA0xACUbCFQ8IF3PIx021j9FQttH5XBeE3KViOZheEMm8GGiulFsTInzYftBC-2dmapvXYFlsh04YQVp33boezZi-1dAV9D6TSMSNPdzhBILPBRsu-7xp3V5Il4zoBAhEIz5r_1nighNOLvK0ryHgF2Fn38f3NB-uzzG9LwDm90BNMhyKZ8EMetnN6ZFpmVu8SUKNgZ4TVYGj9AH7g9XnrUzW7w_Ujlkto26FvdhW4HISiSOjurUoEAj3Kc1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52da7df95b.mp4?token=O83G5KsPAamuItBWM0UaVKXeLEvVXeIbiQEIWO14qNFNFYziIwFKFrMQO9OOfDVrLd-RpyavfLV3QtfNk32aSbliOgA0xACUbCFQ8IF3PIx021j9FQttH5XBeE3KViOZheEMm8GGiulFsTInzYftBC-2dmapvXYFlsh04YQVp33boezZi-1dAV9D6TSMSNPdzhBILPBRsu-7xp3V5Il4zoBAhEIz5r_1nighNOLvK0ryHgF2Fn38f3NB-uzzG9LwDm90BNMhyKZ8EMetnN6ZFpmVu8SUKNgZ4TVYGj9AH7g9XnrUzW7w_Ujlkto26FvdhW4HISiSOjurUoEAj3Kc1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم وایرال شده از صف نذری تو الهیه تهران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/130314" target="_blank">📅 14:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130313">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4fae070c.mp4?token=SkAc9JARKJ-kJuMeLOgTsp45qDufeAXe8gyMome6vqrU_WySEJ4ZgfktjBm1uR7HWAxahAUUNWnzfP2VdAenMFfEauupRzVeEBXxtETTq6O-7V2JD9cZGCrkTDId5YNgFhoI06vGA-YFMk_pcSGx30JSk4bcLx9dRionjn-1nC0NGH0qS2OLdMSqg3OWy56gGXot3BK1wjpZ9tuIhBgn9tJVnsXQceMo16RmOsgRg2OYsZtxrR9tNCcP29Qb02LY75iGqmZ3HrUaV3oC7eVduUpLCmwdqr3FiacUeleXnOio9LT6yQKOVidz8xzUPwB7toTjSCOF5NuUBOt-9eIZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4fae070c.mp4?token=SkAc9JARKJ-kJuMeLOgTsp45qDufeAXe8gyMome6vqrU_WySEJ4ZgfktjBm1uR7HWAxahAUUNWnzfP2VdAenMFfEauupRzVeEBXxtETTq6O-7V2JD9cZGCrkTDId5YNgFhoI06vGA-YFMk_pcSGx30JSk4bcLx9dRionjn-1nC0NGH0qS2OLdMSqg3OWy56gGXot3BK1wjpZ9tuIhBgn9tJVnsXQceMo16RmOsgRg2OYsZtxrR9tNCcP29Qb02LY75iGqmZ3HrUaV3oC7eVduUpLCmwdqr3FiacUeleXnOio9LT6yQKOVidz8xzUPwB7toTjSCOF5NuUBOt-9eIZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن رحیم‌پور ازغدی: تُف بر روزگاری که رهبر ما را شهید کردند و ما از صلح با آمریکا حرف بزنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/130313" target="_blank">📅 14:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130312">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فارس: درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/130312" target="_blank">📅 13:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130311">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td5w0i6mXR3I3XlY6IQZnpswh_3mH5aWdgjCtqNzsj_4lpWM684iCnek6dkcSBBALssbyaZBthWDyLsEaRHRUAMP-aR9FkwrELYE3bm5G2dCYIAlQ9bVsSu8pVZwOLoq3aL-DfFgOYH_EcBN5u3C0usOxvm999i5GQli_KvPw9PN-lYYH4qqG6mcPzFbP-6uLjtFTXgkyp93ftEwaaUVSLHcuA_nw5hFklhsImbSDwWfUZKEjh8Mm2aIcRL0kdxpt7VM3DilxwYyXBUW3sYb7z9govViCUVTIG8w00fEv2Vn8kLB64u0OsHhh2TA_uOhFwTvG7UbMjM1l4cfxOyhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :
ما یه بازار جدید داریم که داره شکل می گیره و اسمش کشور دوست داشتنی ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/130311" target="_blank">📅 13:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130310">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNij_NU8aP6f7oouHuEwIrSYd2bq-4EqjLsKEgtEWVwpET-7KjplLWaaegnox2Rf18fCaIJ2Jai4tle5MXVWYaVV5a4cNJUEqhIk7JyOXYzI1Kf2zgKTrKqYJMogO5RmvXI5NsdBXbYa4wqx50ao2MUBvxboa7br0s5hot9a--kRBGqL52jRFa_NqPP-YVqt2W5wArHCU9ULOWS4dzd_-Euryr8z_iBvXhVBukXKc8Hw0WaU3ja9pT2Zdll_8k9HMtuYtzHDG8WMaFN9ShdgBbegUJ4ZfdZyf9uhzJAH09DTrwL7Ht4iR2i1knmpC4JH2eynKN6cVjeZmvOSpNLdgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روحانی: امام حسین هم روز عاشورا رفت با عمر سعد مذاکره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130310" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130309">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=Kg35v6ywghDE_kwNMEul_s8Y7-vubLcR6a_EHEeVB5MrwdCU44-6soYkeQX5-XEHQaycFFFXyV3g75pAZI7HJ07dP98wSx48JfI-yJ6_TIqFDulJBIRVOETGRnACSUF77p-vWiMI-9OlA0Wu2mf1D0A3MsRb1BMv7VZK-NVqVTu_hgMnJCg-WQRTKq0hMTXwptcafNaXIMlgHKOvFdqMkaqaDGsI-rsqxMkX2raG7TmWNHkPF2uXeSGPfkJWOeJL5JmYVC6XI0IdlXzykH0TjTr-_uL8gZzWs9TaIIjbrUpAOwesv_tQfVwoc03prW3ysR-tCRTTimTjgfFgWLTh8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=Kg35v6ywghDE_kwNMEul_s8Y7-vubLcR6a_EHEeVB5MrwdCU44-6soYkeQX5-XEHQaycFFFXyV3g75pAZI7HJ07dP98wSx48JfI-yJ6_TIqFDulJBIRVOETGRnACSUF77p-vWiMI-9OlA0Wu2mf1D0A3MsRb1BMv7VZK-NVqVTu_hgMnJCg-WQRTKq0hMTXwptcafNaXIMlgHKOvFdqMkaqaDGsI-rsqxMkX2raG7TmWNHkPF2uXeSGPfkJWOeJL5JmYVC6XI0IdlXzykH0TjTr-_uL8gZzWs9TaIIjbrUpAOwesv_tQfVwoc03prW3ysR-tCRTTimTjgfFgWLTh8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسم محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130309" target="_blank">📅 13:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130308">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
حزب‌الله: با تفاهم ایران و آمریکا، ما به یک پیروزی بزرگ رسیدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/130308" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130307">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh8c7Q2Js99enYX5dd93_2L235xob4WFZeovi1UVGHkpXcy_xkeZYqWhnTBCI6pfsi8dkLAk5tXXxHnBr2_czsZ_Iu3Ifgxz9j2ucGV3Y47enPkSipzxY3IgCT-enQez8mm4240dUEQ9Uwmvage5Ak_8sL42bhrDFF0Wq1AV5NK5fwXVX48maXNqu2BqwNKeg53jLbkudO068WPUhyZHDeSeY8kI2trhipkTNgg7TDXuK2ssmpLhoUWYsDDKOk664acsMVcQs-j6O03o33stBI35znWEyVSs3x7_3NXgbqnFs43zKD-HFPYICH3g2wGsALnwOqlRT1RSrQpdgKPdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۳ عبری به نقل از یک افسر ارشد اسرائیل: فروش جنگنده‌های اف-۳۵ توسط واشنگتن به ترکیه، آزادی عمل نیروی هوایی اسرائیل در خاورمیانه را تهدید خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/130307" target="_blank">📅 13:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130306">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
قاسمیان: به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/130306" target="_blank">📅 13:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130305">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=Bi6Q6dhfCvKx-c05tJIxAZBbSzcjRPSah88e0SOg-fdC80kJtLInzMONL720yr1DU1xOfhu9baZJo7kSNlgVMFi4Noj-cZ1aXQlcqu3v0qGOYcXL7e6AtVtkxYAEqvIUIKfbRnXwJwusSvvZJW1gsXUGF9wL9WXxuIzBh2RkKwIDlOvSOrlGvtya2JlO-hjUIoV_U94wWwIpqhCwA98X7jaOhZ3oUivnBlz6fog-hcgof1zp8V95__lsA9ZrOWm9l6c8seLwvLuiz5aX-sYiv4noArQBh_uHWT9g7ZUTK49XAYQJoxOfAkJXoJERo3N-NQMYD71yOC8BCI3j5Krv-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=Bi6Q6dhfCvKx-c05tJIxAZBbSzcjRPSah88e0SOg-fdC80kJtLInzMONL720yr1DU1xOfhu9baZJo7kSNlgVMFi4Noj-cZ1aXQlcqu3v0qGOYcXL7e6AtVtkxYAEqvIUIKfbRnXwJwusSvvZJW1gsXUGF9wL9WXxuIzBh2RkKwIDlOvSOrlGvtya2JlO-hjUIoV_U94wWwIpqhCwA98X7jaOhZ3oUivnBlz6fog-hcgof1zp8V95__lsA9ZrOWm9l6c8seLwvLuiz5aX-sYiv4noArQBh_uHWT9g7ZUTK49XAYQJoxOfAkJXoJERo3N-NQMYD71yOC8BCI3j5Krv-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قاسمیان: به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/130305" target="_blank">📅 13:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130300">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fInGOL7shV-sZj-He61DG3jA8l1So-j7eFseRqsdMrDrerWanvS3bFg68Uv534WdpY0xMXqOk4c_rrR9a1EXVh-8IRJZwcTWL_A9RNgAweaPuLKqkpzDRLn75ChMgbp2Co3FIy13bHE3A-rXGpxWH75_bTbpoaDQC7nJq2nhawuv8YntlQO6rI1kfO8AhwM0BsEaGvbVRcW82E_xG5dMW5Ph0jnopPsJum41M3h4DWzZGE4CPQCg1fTMIPeq2bbO6GYRHi3pH4j788nnd26Ow2YoEVtzwP-fIPqnufUvGNySJzeAmiAyyvwD3efOjd8p4h4bX4jTofypmLGAJNIKAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEhZVhJFkc_7aUs5-Y9imo8iMBaQXLbuBFJ7FowoKy3KfQmL2VNE9_YUED5AUmLo6e9ZqwjFdkR6F-sx91I0Ux_iSTVjRe_CcLOs0hxIxXv4c20yvoNDnk-dWitlw1Wrrmci5VH7t473HJva7R4F94qpVjjoT4hXXDGWCFUr8BvdC26-S1v1o-8hwxeckn5D6N5ZQZZkujRK0jIRfpW0xmgh8zDLpr3pswsBPSonZGPWJgxZD67TDZqVswNgTEgsBW3f3RGHH9fnnjhXicxkiY7h80oLl8NN8267IWQuVDYfE00PCtXF7rT1X_Q3g15nV_eij52es5zIPdju0arU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LpR9Lhg2xYrxYLFYtJ9vtyyh_2Uap9saLXeEbfHDUaaL_2JnJJGQ63lhw1xsxWPBE7qjBB_f12YXOgrSYDHsZf9KcMozmVplQCXDDob10b6rJs41iVuE4KNu4QTXLB1F-ahSMwfxnARdI6Qg4x0rtI4b_Ok1bfQfq1YchwWaUCMK9WuBgZGeCijrwH1-iTPWv0ZzRnMq_1WlHp1UmlalRZQKO82lYbCXy3QaaFk445NbscmCH8ptoFUApVEf2kpS6LVzDqgUS5ORWDcUK3CO9OihxPcSikQNZLRCCb0P8WHTyKhBoWZQyQPFFucwaWmnkQk1bWBqK8k0pBSZJCH2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfUx77xITt-HeLrbiqQVrztuxtVrrT-PnOuHnSOSC0uBZ_EiyPfFA9ZoViEOMjkbEcDYhS_pk2giu2Te9a6nuu5uvTxNEoIJekVGFkXnTA9du2poXxDgONRdB20xfg9Zc-nOVGFslblEPl5bIv2pKoXRguRyzfHSdAtMUo9jD04jPTGFFnfFY9U0GdLtk8IbaIKNnwlPSyYuOAEaDwtZhNw_Kk6NPPRS6H7YyzxgaDlwbpaJGarZhdtf0JyfI3Bffo4ETeOgzz9saQHa8z629nFyPw2ILSi48Ekjxfb_LTpSOaBurEZVuvNnRxZ5ces-y9mon2XB-_vbHdcuGoleIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqwdNH4tC0T1pdq7CvXyw5EBKXkbvUxpDP0nXtmFvUBdmuIl3gN9luWn5Uk5XQ1aJC0019v2ioQJrZldFMqWUytmQdO_5naPl5_mvQ1oOYox_Oi2WphdBvXZj0AupReWZmOOm-kCoX-ivY3uhXkxYds3uRwaNmzvO2U-BwTbIDJe55FKidwWOAyZ_IFaAFomf_Gg5DUPM6f_mM3JoCIzYnpvs8wRZlmzfCSxZryma-WeubVMV_lnvDjopNUYPc1zh1WNTE6AhfS6S4dfgKGNX6kDZVJ9kKI_mY6A9QjDpYbjKbi7uTsTZvfDYeDGC0ZBtGPHn5P_7-c1zvHqZ5dcAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید ماهواره‌ای از خسارت های سنگین حملات ایران به پایگاه پشتیبانی دریایی آمریکا در بحرین
🔴
در این حملات، ساختمان فرماندهی پایگاه، دست‌کم ۱۲ ساختمان دیگر و همچنین دو پایانه ارتباطات ماهواره‌ای به‌شدت آسیب دیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/130300" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130299">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
استارلینک به زلزله‌زدگان ونزوئلا یک ماه اینترنت ماهواره‌ای رایگان ارائه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/130299" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130298">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
طبس گرم‌ترین نقطهٔ جهان شد
🔴
براساس داده‌های منتشرشده از سامانه Relay Weather، ایستگاه هواشناسی طبس با ثبت دمای ۴۶.۸ درجه سانتی‌گراد در ۲۴ ساعت اخیر، در صدر فهرست گرم‌ترین نقاط جهان قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/130298" target="_blank">📅 12:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130297">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDYDBd6PRPiClGK8ngbAoZmkPm9wJyjeOrhgQWYozuAulFYvh8jSEKtZD5wYfAa7sdhHzMbPqy4sFTK0Art9wTPBI42gFz-RjccStwJtEzKtKPBHsh0zwePChjBXEzT26b9_R-IO2s1Z3VqKgovUkD40rswjMJCOa_RU6F57kFCs4kOEA_z5CDf_RDmFrVL3rM3yBAG5WeDI_qLMMWqxPhHe_FIU86SRCUIKBW-IObD64mOY1lLpDhyjYZ-pyu9SF0Bjj1ZIFLyW0lXyj65Yo_4rlvOqYpbN9BE66J2VcZ_TXUAQM1zhyrQjRTqwXPlqdQBGXNmD2JDVKvnRbg_56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده مختاری، خبرنگار: سال گذشته بانک مرکزی رکورد ۱۵ ساله چاپ پول را شکست
🔴
پ.ن: چاپ پول، یکی از اصلی‌ترین دلایل تورم در حالی به اوج خود رسیده که کشور ما در ماه‌های ابتدایی سال گرفتار جنگ و محاصره دریایی هم بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/130297" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130296">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
عراق شایعه خروج احتمالی از اوپک را تکذیب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/130296" target="_blank">📅 12:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130295">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2e1ef960.mp4?token=m0FZeIzmil6hOu05tbs1LWElpYq-g2asV9MKSLuzIWdfeDoMB69P4Lzl6eCNkc6szK4p-ZE0Gp98gyKiwI2JI2BteF4MciAC9rKRXZqqy3ueJl7jA8iF03fJBgTH6bEIGd_5k9k9gXeR0HaARMI0gO7FRAhFR7BWJnOV_zmeeSbwKHrAwwB9-do086gtJqQ66eO-nnkuVEoer21aFef4E4Q7cACUht9kwGgEXWvzYv9oZCdXgdN_CqiEw-DbBQRFRLVTdnrycyuVA9vfz-PkRkSaRNvph0o_NlXEUqqx6CdSutsvaiDun1qOSvpU7VuGTPlUdzvNE4IsR60S1GMZkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2e1ef960.mp4?token=m0FZeIzmil6hOu05tbs1LWElpYq-g2asV9MKSLuzIWdfeDoMB69P4Lzl6eCNkc6szK4p-ZE0Gp98gyKiwI2JI2BteF4MciAC9rKRXZqqy3ueJl7jA8iF03fJBgTH6bEIGd_5k9k9gXeR0HaARMI0gO7FRAhFR7BWJnOV_zmeeSbwKHrAwwB9-do086gtJqQ66eO-nnkuVEoer21aFef4E4Q7cACUht9kwGgEXWvzYv9oZCdXgdN_CqiEw-DbBQRFRLVTdnrycyuVA9vfz-PkRkSaRNvph0o_NlXEUqqx6CdSutsvaiDun1qOSvpU7VuGTPlUdzvNE4IsR60S1GMZkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاسر ، جبرائیلی: اگه قراره با آمریکا ببندیم؛ ظریف رو ببریم
🔴
یه بچه و بساز بفروش و پاساژدار رو به مذاکرات فرستاده‌ایم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/130295" target="_blank">📅 11:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130294">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ddgf50xvAN1LFepWvnoqPRBwY_c6TkNFgIRVXyaNIDOkNfEgt_-jUtKtutLKbj96bmGO0uA7Pw6ZLTcshUOyfoJWtVOUMJqd0e9DDXmFIjf2pRATgsREqb7aK44Nit6gluK5I0NemGMFDvhp4fPhOEinCQfXMDkL_N32DHhGdz9pvdLoqmBVMFrnQUpYgukZOrTleH9VFojyt_lssVe-lKkS5aOVYCIa9QhQF9Gxb8a-P80U3N0Vwsstki1ASj84ya1lQqwdD2mbvyqqThc_lcahlwHHx_-2yaPHqiVEIX9aZkd4wKXLy99Xqti1H1EBXbuhetWiUmBsg-dG8B_bWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: امام حسین سیدالشهدا شیعیان بود و امام خامنه‌ای سید و سالار کشته‌شدگان انقلاب اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/130294" target="_blank">📅 11:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130293">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d80C1q-SwIUnLR3EgswI-JEMRlUqfnBM7xVwS6sgy17JAQAu6wUfqeHuljVjVD8ErTn4lSXgy44UPlaMO3ymaQYR2NMAUJH6OS5Mfh40Eak4mGWFxv4XLq7ZEo7Dd8CmsTSi3pV_CJ5SfNTbkq3U2Rzm7aRnnQtzL5-TJvFjlHtWhdIq2VMgHpj_Phb6dCIFp0bGGFnmvoELhx-A3Iun4yEAglH0si4nK6Q1sakNP0UoeZDZoAuujq8nPzmHOXwIWfz7JbVV_PyYBZKm2lMQSEMs_HiZArrp6AR32xXCP6UiKlBGmDWwXtsZUdxE6vUD9fKNA-u_2jkPU5MhsUbyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵ زلزله بزرگ در نقاط مختلف جهان طی ۳۶ ساعت گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/130293" target="_blank">📅 11:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130292">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا اعلام کرد مذاکرات غیرمستقیم میان لبنان و اسرائیل که قرار بود روز گذشته در دور پنجم خود پایان یابد، برای چهارمین روز طی روز جمعه تمدید شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/130292" target="_blank">📅 11:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130291">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
استارلینک به زلزله‌زدگان ونزوئلا یک ماه اینترنت ماهواره‌ای رایگان ارائه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/130291" target="_blank">📅 11:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130290">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
بلومبرگ، با استناد به داده‌های ردیابی کشتی‌ها: ترافیک کشتیرانی در تنگه هرمز روز جمعه در هر ۲ جهت ادامه یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130290" target="_blank">📅 11:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130289">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مذاکرات لبنان و اسرائیل در واشنگتن باز هم تمدید شد
🔴
این مذاکرات که پنجمین دور گفت‌وگوهای مستقیم لبنان و اسرائیل در آمریکا است، قرار بود روز پنج‌شنبه در سومین روز خود به پایان برسد، اما اختلافات همچنان باقی است؛ به خصوص در خصوص نحوه عقب‌نشینی ارتش اشغالگر از جنوب لبنان که تل‌آویو همچنان بر ادامه اشغال این منطقه اصرار دارد.
🔴
هیئت‌های مذاکره‌کننده لبنان و اسرائیل امروز (جمعه) نیز نشست‌های خود را از سر خواهند گرفت تا به ادعای این مقام آمریکایی به توافق دست یابند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/130289" target="_blank">📅 10:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130288">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌: تحرکات و حضور هواپیماهای نظامی ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران، اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
🔴
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد، جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/130288" target="_blank">📅 10:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130287">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw_ihGCcj7o-piJo0ojGfou4b-FSNAjNeU0_c74qyPQcPCqwpb28JKcs8AZVyyLiougq3IyhLHeCrODn5Lnr6W78C9ARj3iHEHs0BQav9SYiSSt9OZOY-YQng1VT8xxYRYwQwq6shpu63RmZWC3IUeXhr6oS2ei30dl_WMK-7XdxjuZf6s-pX_HU1h0tDD4JchOXW9PefQ_CYh6VM9ZPt_0xtVQK_2g9fbP6beJ_cvNh1KfKRWOzpJHShqPg4ZGN7OFVlNWvdz9nBbhbeu6z9NLjxLCh329ooOtl_LWrB_cafJmP12XeYqaRVqOkFydrrOAd8Kx-pIOXLuMUKLZx1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان پیداش شد: مذاکره‌کنندگان برای هفته بعد قرار مذاکره گذاشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/130287" target="_blank">📅 10:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130283">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaePSaBn8lBjNAJuSGybb1JzFOX8yejDRVp5R_F2ZTivMnkvhqa73IGhPkGX0R1v3pb4B4ZWE9chK3bWoUPaGu61lNnzMcIsGMNmuRvEhipMlEZctORxoeSBxlxZow9ula5-tQkHCh0f2iUpxe3t5LOCQE_3QpDEVrOqxdVXMB7Z5FLdMn9p07_ww14kFXBFsuYeVOuScjSDZOfUb2W_2IzIRuAyy8f14-E6HJlwiOdzpCjppSgd4lrhp6eANTdgGYakXKUE7TEtrqd55b5MgKrBQ5S0hp25nFr9ztimod5kTAqPAdRJjxuhPIIbKLz2YoSkTSx9ZhBVq-bG536azA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAGzTg_QFJGzmHVr8qdpzDlG0c6vDItGL-4UnJDxInbenwldQ5nBKPANlOOs3VTD4N_WK_uNouVjEmurrXvd6ScA2-jrwHBh0IAryk4d4Fg30n7yrlrSMnHeq5ViXI0EeldYLtoq8CjnzQmRFi1W6t8sQ-2PJ5YyhKfDEjFHYBV9RmTkIZsmetYO2qzJUHwY8aVWt58pNw82_DeG4NlBypLg1NlQQBA-dRPXET31X09sIo-PQxH7m3-d3X-RKNSiaJjKAyhpw7XqzAOuDCEObmh5HgV1m07p4LclI9RBZS1iQSxffHd5lEqx_fr8XG24oLzt5xyr-JsmDFDrANgfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-s5C5GXk-OvxnvvdmvdK3tb_MohsqtFapKeElPUMbsWee9DFtE_KASb98KbvbvojpTDAdXlGTjTFJakpjSHQGygsywxt3oSQyHQvSerCiIvWA3i1toVRp_JmI8j-PdMLXv2TLxUL1OFadenx1FkOgl2fkeeejV3I_seSFmvSlh4G0P58fwHacmooK4h3EgnahKHEzdwcejpT7MpagkyVFzyMi8LUuxs0HFRzB2a6B0B5M1t1SypQ8tllRLuELSM37IIIhHSQ9vGIb4-j32vwYGs37etddyJtv_7i59g_ebabx7jrrYLPjzeJ3lF4RLvdowwAdRKTrOyIvnekBs5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIFZecin3t4ebk_7MpP6INV9dCBTFObk-1S3Ou2MaBf7zfSlGYT2erHvIv_irjRhINTDqXO5Y1fuMm18nlgwg0gEi_BqLwb1vSxSOojX82YMxDm-5Wqun8eSJvvPUFkdJtTT6nArzeFHKEWtpaRsoOB69PD9GHlJBSVok65rnGyA1VeI1Xygl0rUGc5r_uIaoRBU8UnUrk9Ya3VDpT-pfM_806izOvRU3qtqfWZhULHkvcCOX9eLRVPAZEoCT4TTUrYT2alHlaZLWU2Q1Jwv_XR4L4XZsk7vv9BhaOxY_hOd2_4VUluhOYq1_D2ALUod4fUGssImG5ySerOGUo2OSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون، رهبر کره شمالی، بر آزمایش‌های جدید پرتابگرهای چندگانه موشک، کلاهک‌های موشک بالستیک تاکتیکی و سامانه‌های توپخانه‌ای با برد افزایش‌یافته نظارت کرد و بر لزوم تقویت قابلیت‌های تهاجمی «مرگبار و مخرب» کره شمالی علیه دشمنانش تأکید کرد.
این آزمایش‌ها شامل یک پرتابگر چندگانه ۲۴ لوله‌ای ۲۴۰ میلی‌متری ارتقا یافته با سیستم هدایت دقیق خودکار و برد تا ۹۰ کیلومتر، کلاهک‌های ویژه ماموریت برای موشک‌های بالستیک تاکتیکی طراحی شده برای وارد کردن «خسارت مهلک» به فرودگاه‌ها، بنادر و زیرساخت‌های برق و گلوله‌های با برد افزایش‌یافته ۶۵ کیلومتری برای یک هویتزر خودکششی ۱۵۵ میلی‌متری بود.
کیم گفت که این آزمایش‌ها پیشرفت در چارچوب طرح نوسازی نظامی پنج ساله کره شمالی را نشان می‌دهد و «تغییری در وضعیت آتش در مرز جنوبی» ایجاد خواهد کرد.
او افزود که سیاست دفاع از خود پیونگ یانگ نه تنها با هدف تقویت توان دفاعی، بلکه با هدف ارتقای «وضعیت تهاجمی مرگبار و مخرب» آن نیز هست، به طوری که «هیچ دشمنی جرات رویارویی» با این کشور را نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/130283" target="_blank">📅 10:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130282">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل به نقل از سفیرش در سازمان ملل گزارش داد که طرف لبنانی اظهاراتی قاطعانه مطرح کرده
🔴
وی افزود: «هنوز به مرحله صدور بیانیه نرسیده‌ایم، اما درباره مسائل اساسی گفت‌وگوهایی در جریان است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/130282" target="_blank">📅 10:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130279">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_1erjh7he9XjmgXwv23zSGQa48tRMahR-BISpH0E2WdhSpiwPnLnCm-Ixntx9G-LyyNVhedA2VTazHXb_fi0UtHmQOjG3zZ2FsBSY28bqKwZH6M8AXbZMPT_ff1mKB10Jd2shpkGDp5O7ILotf3NQmlQ3xUvcp0KDs8xiXEM2oIABjkxeAoqhyLT8MVvSIrL7BMYlQ8sHGxgG5clAmRPHvZrbk55UlAuvGImTy-IEWtCRgMeLHfjxwQ-y-Kz-fY_aT1nTv7K3idQKNQEyx3tHq_Z6FIUTb9QfmXxUfpEYZXFIHJVkKMt10fVy_KNTR1eH7lvejnUKCu_YyvWOg6ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AA-LeW3S6YniOBPKfSnF2wVzG4yW9t_aCz48oATRHCCCk_wZijVr1brCjnuWw4g1v9ldXQWdtZ4PlLDb2mp_W9mNkPoH2jE9PuT7VEVHHEpEJIx4D7LLpTpE0qZE-L_tl9bg5k5JV8K_yxnjesEccCkcZJGhng3O-mi6484dlD5Ge9u6y9e8evpn3mI04ALF2bOCf_W8rSu1QQC4v9OQk-DSXzv6aieIfaFQizFx2Z8Fsl36yyO1qUaxRp6LOSbxLPOk5Vohw9QvMyL_hLEvtNdre0ajWVacQ9fTKvNhsYu3UWUPqdw3H9Nij9MDS_NFP9BwDjiN_sofD6CLDT4eVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bc2eaf0b.mp4?token=vsaxIMh5x_V0txu70QyANCI1grgh_hgzM5BIn_aYvC3EWaVRilgSxRg6usrK57ohuzkUoyaIDzesCHUtLQGjiuhRD7gOH6dCqlhKRwShMa9QgTwp3n9trC_KTRRpv__QWeVLdYpJuBckUziJaWQcUTvwhw8oyR7fc3esOS8SpmBAPgGCeF3q8xyqMl-1aLvVHRdKwjgpX0NMbcglYYXJYY2DGiSdG2s9as84QO0_41GLGsA_AtEixquWqTF16JDsGbS7d_WStrEn4j1vgcztxUEnXGSVYGyYbqAM7Hu9bin-MREgB56yNDnK00anBYFxYYMPRoF2Fj2Lriz3jfNKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bc2eaf0b.mp4?token=vsaxIMh5x_V0txu70QyANCI1grgh_hgzM5BIn_aYvC3EWaVRilgSxRg6usrK57ohuzkUoyaIDzesCHUtLQGjiuhRD7gOH6dCqlhKRwShMa9QgTwp3n9trC_KTRRpv__QWeVLdYpJuBckUziJaWQcUTvwhw8oyR7fc3esOS8SpmBAPgGCeF3q8xyqMl-1aLvVHRdKwjgpX0NMbcglYYXJYY2DGiSdG2s9as84QO0_41GLGsA_AtEixquWqTF16JDsGbS7d_WStrEn4j1vgcztxUEnXGSVYGyYbqAM7Hu9bin-MREgB56yNDnK00anBYFxYYMPRoF2Fj2Lriz3jfNKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیلی صبح زود امروز به ناحیه النبطیه الفوقا در جنوب لبنان هدف قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/130279" target="_blank">📅 10:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130278">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وال استریت ژورنال مدعی شد:
حمله ایران به کشتی باری در سواحل عمان، آزمایش توافق ترامپ برای بازگشایی تنگه هرمز بوده است.
🔴
به گفته دو مقام ارشد آمریکایی، سپاه پاسداران انقلاب اسلامی ایران روز پنجشنبه در تنگه هرمز به یک کشتی باری با پرچم سنگاپور حمله کرد و توافق امضا شده هفته گذشته بین ایالات متحده و ایران برای پایان دادن به درگیری و بازگشایی این خط حیاتی کشتیرانی را آزمایش کرد.
🔴
این حمله تنها ساعتی پس از هشدار ایران به کشتی‌ها مبنی بر عدم استفاده از مسیرهای تأییدنشده از سوی این کشور انجام شد.پس از حمله به کشتی سنگاپوری که از مسیر تعیین شده از سوی عمان عبور می کرد، چهار نفتکش دیگر که در این مسیر حرکت می کردند، بازگشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/130278" target="_blank">📅 09:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130277">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZti5pmSy7bOKpzShzZYV-8sUO4OT2DSby3BSI8nQObYFxsYow2i9NhmbzBaJX_3veeg-AxHb8GyIgBnnkQkd2tq_JksdnCmaDfTPdAAitb6C_cZ_VwHC1hLNQw48lwY6Oj6KitUGiiX_HpujddHfabjdNvcvDWbs3n7ZVmGiygz-eC7zIrCztS4vXGFpwCQHmNSLJ1WHQSo8Ff6N0PYFnVFpAWW-FtiSa5fO_hoKeb17-B51aO7TkfHaSRF9Ilgd9unuxJUlW9pBMNpH5ViCqcHfLF7gzf3-1tOhi2tBVN5bX6x8_dl-cDfF8ksTSDbnNH4GyGD9ibakud3a8yiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز ۴ زمین لرزه مرز بین عراق و ایران رو لرزوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/130277" target="_blank">📅 09:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130276">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بهای نفت برنت با کاهش ۱.۷۴ درصدی به ۷۴.۱۹ دلار و نفت خام وست‌تگزاس اینترمدیت (WTI) با افت ۱.۹۶ درصدی به ۷۰.۵۱ دلار در هر بشکه رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/130276" target="_blank">📅 09:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130275">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apdqnNXcFKbTh8ksqsMqWUBXM8zzGs4b11bZ2VA-XfbAoPkx37nlaGFkCkt7a4ZlVq4P2bj0jCikBcWIUzw5Kxs8b-nHWl1wBVjh7nwqP0_emMfIhLL1sP6Cocs7RetMFuWiSQ_7LVpmdL6HStBzWDcuwhB63keZ-rHvOeyYHXb_cmevLGLdV6DuvJyoicpHuuCJ0KAF76Qbe3HRtRHWcWGwX6WRNauq0sKNEKDK7PpZe-Chsa0kYD2bCyFL1ZYykgz5wiDOG4HBC9Qm07MuvvuLnDj-J-jDP5FWtsnACVLIr8SjBNw7FC_X1xlnCrbB3eU77fpmQ-mhvWXIlVQSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون وزیر امور خارجه آمریکا در امور شرق آسیا:واشنگتن، علیرغم اعتراضات چین، مرتبا کشتی‌های جنگی خود را به آب‌های مورد مناقشه در منطقه آسیا-اقیانوسیه می‌فرستد تا «از آزادی ناوبری دفاع کند!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/130275" target="_blank">📅 09:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130274">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نخستین پرواز دیروز پنج‌شنبه ۵ تیر از مبدأ تهران در ساعت ۸:۰۵ صبح در فرودگاه بین‌المللی کیش به زمین نشست و ورود گردشگران به جزیره به‌صورت رسمی آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130274" target="_blank">📅 09:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130273">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-jADe3XAz2raw8NKDgeNgr7UABjcjYWt9JL_SNjfxoFv2BTXnZJy33TwipNwQpvn5rqy7CnnckT_D6K0A5XiGpb2ttuQpOSLLJQybvJMXNWl60yaDfSUScHnVX0AGL7dgTykjiHWE1nFWMQ04PBSlgEHei9GOprfLIxViMU44XPk-k8tAQefgBqLU3aCijUL0hfVWix-4oLgwgNbq5uzE5UX-9SKAmJRevTVbdfSiyqfCBlz0PTPALVAulzVTGtSsnLDfNG4M5S3Aq4VxeYCfFdGlMM0eoVBalndBtLWbTddC2baLqPz1VO8l1h5_-ir-yBwp35Z-3ODPXEaJmg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله شدید اسرائیل به نبطیه/ در ساعات اخیر چندین حمله به جنوب لبنان ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130273" target="_blank">📅 09:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130272">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل: به هیچ وجه قصد خروج از لبنان را نداریم، حتی اگر ترامپ درخواست کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/130272" target="_blank">📅 09:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130271">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
افزایش کشته‌های زلزله ونزوئلا به ۲۳۵ نفر
🔴
سازمان زمین‌شناسی ایالات متحده:
فاجعه احتمالا گسترده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/130271" target="_blank">📅 09:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130270">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6157f55c.mp4?token=gNg7_60Hm98rQwSSPHERmSEFu9z4MRetQvwLWPY2Exxs1gOAInkuVqT8y7lcOw-481Rk92ptYQRRCbwFXo_rxJrZQ0Z6fgBNkCO5YfkxbfzqvrWgRyVKJJJFZEyY-hD6cbXqxoTBLbatw96oRXDeGdK-Luq9qrFvrMlXodZ4rRN_6q2uGCYIlWRH-xCaT2hLyPBMvkhTn-WqCczuPDYi1B4UCzGPHCj3vK8UIMsRVMMrGppIc3wunayEwdAuFy0PALzg06CoNTZj6s9DLs_05WTR8xlszSiD0sWzex7ljcJ6xzw_qrKWUtZATx1NfjcEZ6eR_n5E10RCUpjP4YAT1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6157f55c.mp4?token=gNg7_60Hm98rQwSSPHERmSEFu9z4MRetQvwLWPY2Exxs1gOAInkuVqT8y7lcOw-481Rk92ptYQRRCbwFXo_rxJrZQ0Z6fgBNkCO5YfkxbfzqvrWgRyVKJJJFZEyY-hD6cbXqxoTBLbatw96oRXDeGdK-Luq9qrFvrMlXodZ4rRN_6q2uGCYIlWRH-xCaT2hLyPBMvkhTn-WqCczuPDYi1B4UCzGPHCj3vK8UIMsRVMMrGppIc3wunayEwdAuFy0PALzg06CoNTZj6s9DLs_05WTR8xlszSiD0sWzex7ljcJ6xzw_qrKWUtZATx1NfjcEZ6eR_n5E10RCUpjP4YAT1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از زلزله ۷ ریشتری ژاپن، امروز صبح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/130270" target="_blank">📅 09:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130269">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
استیون میلر، معاون رئیس کارکنان کاخ سفید: ایالات متحده در مسیر بستن کامل پرونده پناهندگی قرار دارد و پذیرش تمامی اتباع خارجی را که به دنبال یافتن پناهگاهی در آمریکا هستند، به‌طور کامل متوقف می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/130269" target="_blank">📅 09:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130268">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4bc8bdc23.mp4?token=Z_J0uLfOMnSjIs-TzM2ZljYO39IU7vHsupioSCfB1BXX-l-39Ai2GzZYdUm6u5zXts7myAJUAfNk-MS0rwk8vbo8AL4f0M6OgXy3wSC7vnlAE4mZ9Ls17G-oVKDBhN5kIOfl72i0lodX__EyHg0c6panekcaItIGKS7GzdaWBKZk9eni9M90TfV7B38HZFw8PoAmnUyLb2N3f2cnoVVsT8j6EKfwFOqCQ0p8_n-JkDxOA8eeSdNu8iHwaAyIWvDoOthk5EKt8JHUnIAUYfiC1_mVYi3ySn1puKjYkyhFVGNBbAVkaHoEwklBQzUcu-3pMMVv76ttjB_v4svbU7SXGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4bc8bdc23.mp4?token=Z_J0uLfOMnSjIs-TzM2ZljYO39IU7vHsupioSCfB1BXX-l-39Ai2GzZYdUm6u5zXts7myAJUAfNk-MS0rwk8vbo8AL4f0M6OgXy3wSC7vnlAE4mZ9Ls17G-oVKDBhN5kIOfl72i0lodX__EyHg0c6panekcaItIGKS7GzdaWBKZk9eni9M90TfV7B38HZFw8PoAmnUyLb2N3f2cnoVVsT8j6EKfwFOqCQ0p8_n-JkDxOA8eeSdNu8iHwaAyIWvDoOthk5EKt8JHUnIAUYfiC1_mVYi3ySn1puKjYkyhFVGNBbAVkaHoEwklBQzUcu-3pMMVv76ttjB_v4svbU7SXGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ونزوئلا: ما ونزوئلا را در کمتر از یک روز تصرف کردیم و نفت در حال جریان است و ما با آن‌ها بسیار خوب کنار می‌آییم.
🔴
ما می‌خواهیم به آن‌ها کمک کنیم — آن‌ها دیشب زلزله‌ای عظیم داشتند که در مورد آن خواندید، مانند یک زلزله عظیم در کاراکاس. ما می‌خواهیم به آن‌ها کمک کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/130268" target="_blank">📅 09:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130267">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گروسی: معتقدیم که مواد هسته‌ای از زمان آخرین بازرسی که در سال ۲۰۲۵ انجام دادیم، منتقل نشده‌اند، اما لازم است این موضوع را به‌طور قطعی راستی‌آزمایی کنیم
🔴
جزئیات فعالیت‌های ما در ایران و ترکیب کمیته هماهنگی ویژه مربوط به روند بازرسی، در جریان مذاکرات مشخص خواهد شد
🔴
آماده‌ایم تا فعالیت‌های فنی خود را در ایران پیش ببریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/130267" target="_blank">📅 08:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130266">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: ایران کشور زیبای دوست داشتنی و بازار جدید برای آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/130266" target="_blank">📅 08:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130265">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuLRMI7fS2FDqzgxdLOJO71_8KdMzB_g4k6yTduP5eJhJoZYNgRu3cQNRWGr1a5qqP640Gy7JG-iWcZf1KwT0gduwFlJkdlpf0iuNtf8uhckpXZRAMqFogV9XBjeJHg-qqSWZS5ztiY44rMOVLAizMmB4okJoz0o9SOFcuUzl4LfO8H2OXaey-3L3TaDtgGFnyD3KX6TG83KJjAEfGJgHwmtFeqzfFoDgf6EqExWnwsvxlq3x5foJ0K-EAurKzPEWvXImCwFT20wXY2rzCHwIvdxZSwWsbkbI2xxbXuTHdtSv4HA_ECgkc9o9v9gnwRW-arfH-Ml5-6znxIAuQQ5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا اعلام کرد
تماشاگران می‌توانند در دیدار تیم‌های ملی ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶ که روز جمعه پنجم تیرماه در سیاتل برگزار می‌شود، پرچم‌های رنگین‌کمان را به ورزشگاه وارد کنند.
به گزارش رویترز، این مسابقه هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود و کمیته محلی برگزاری جام جهانی در سیاتل آن را «بازی افتخار» (Pride Match) نام‌گذاری کرده است. ایران و مصر پس از قرعه‌کشی مسابقات با این عنوان مخالفت کرده بودند همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای تاکید کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه را دارند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود در دیدار ایران و مصر که از سوی کمیته محلی جام جهانی در سیاتل با عنوان «بازی افتخار» (Pride Match) معرفی شده است، از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی جلوگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/130265" target="_blank">📅 08:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130264">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24211a974.mp4?token=i7i4VxrPWXvgb8IEm13PeW3WghQEi-ISBUubG8147hfCjyM8vm6AW_PxbVk1VJGWO83559WBKTFzKNBvy9KvNQ42GnXmc3CHDq9QVRfucfTY8R3RK8d7Z-V9Oeeojl-CnVHUwQg7tYo8dRSWrn89Eebixg_zsWXFSePXYvghssabZBSUTNshQY9S9ZUAJtF95HnftOxcg7S8krg0ReYkk8ies62ujVXMNWxJQ_0Xh_pgTBg0-z4hX67UqPy2S7mTeyfbtKaMee4d0id4RnocXeU8R0lxODOtCOA9wsDSSztewCiMvPTet8e_2D7uhXJBrGPiQEWM_laarfKXkdSNmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24211a974.mp4?token=i7i4VxrPWXvgb8IEm13PeW3WghQEi-ISBUubG8147hfCjyM8vm6AW_PxbVk1VJGWO83559WBKTFzKNBvy9KvNQ42GnXmc3CHDq9QVRfucfTY8R3RK8d7Z-V9Oeeojl-CnVHUwQg7tYo8dRSWrn89Eebixg_zsWXFSePXYvghssabZBSUTNshQY9S9ZUAJtF95HnftOxcg7S8krg0ReYkk8ies62ujVXMNWxJQ_0Xh_pgTBg0-z4hX67UqPy2S7mTeyfbtKaMee4d0id4RnocXeU8R0lxODOtCOA9wsDSSztewCiMvPTet8e_2D7uhXJBrGPiQEWM_laarfKXkdSNmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رجزخوانی وحید جلیلی برای ترامپ
#گنده_گوز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130264" target="_blank">📅 08:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130263">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: باید علیه ایران اقدام میکردیم چون داشتن سلاح هستهای به معنای نابودی اسرائیل و خاورمیانه و به خطر انداختن جهان است‌‌
🔴
اگر ایران سلاح هستهای داشت ، ظرف یک ساعت اول از آن استفاده میکرد و ما هرگز اجازه نخواهیم داد که این اتفاق بیفتد‌‌
🔴
ایران سلاح هسته ای نخواهد داشت و به آن موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/130263" target="_blank">📅 02:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130262">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ: ایران خیلی می خواهد با ما توافق کند و فکر می کنم احتمالا با آنها توافق خواهیم کرد‌‌
🔴
ضربه بسیار سنگینی به ایران زدیم و اکنون از موضع قدرت مطلق با آنها مذاکره میکنیم‌‌
🔴
قیمت نفت به شدت و به طور قابل توجهی در حال کاهش است و کاهش قیمت نفت با کاهش قیمت تمام محصولات دیگر همراه است‌‌
🔴
تنگه هرمز باز است و دیروز شاهد خروج 19 میلیون بشکه نفت بود که بالاترین رقم در تاریخ آن است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/130262" target="_blank">📅 02:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130261">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: 159 کشتی ایرانی را کاملا غرق کردیم و همه در قعر دریا هستند‌‌
🔴
تنها در یک هفته و نیم ارتش ، فرماندهی ، هواپیما و نیروی دریایی ایران را 100 درصد نابود کردیم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/130261" target="_blank">📅 02:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130260">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ: روند خرید محصولات کشاورزی برای ایران خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
🔴
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/130260" target="_blank">📅 02:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130259">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566bfa2ebb.mp4?token=jrIZvr-l_3DGn_-IZN9kAJlwtB2zsJMF3dGkHFSfenphFERCHMJiWSFaifpmYwR6AUXv0P_IrCzXmcT1KS3yOc56kZq6sUSzw309OlzGVOls5PAEkGAi9ULrp5_5dfkjFuz_7-nd7X4VmKsmV1Bfzzq98IDJheBgmMog3yzIbUGuo6dj42Q1XLsUfsX58KUP_iQQAGuwX912iV8T9UvteMU14EvftrKP3jtg8O32xW4FCXnAGkZTMermvuwFvwVrABV6vIPP0yodiiHB5mImDeCrz96ES3mOfXLu0xkmorwsbrpirCDqwjN7A8veV5RIKIHVbbNcVkkhu5LYDObL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566bfa2ebb.mp4?token=jrIZvr-l_3DGn_-IZN9kAJlwtB2zsJMF3dGkHFSfenphFERCHMJiWSFaifpmYwR6AUXv0P_IrCzXmcT1KS3yOc56kZq6sUSzw309OlzGVOls5PAEkGAi9ULrp5_5dfkjFuz_7-nd7X4VmKsmV1Bfzzq98IDJheBgmMog3yzIbUGuo6dj42Q1XLsUfsX58KUP_iQQAGuwX912iV8T9UvteMU14EvftrKP3jtg8O32xW4FCXnAGkZTMermvuwFvwVrABV6vIPP0yodiiHB5mImDeCrz96ES3mOfXLu0xkmorwsbrpirCDqwjN7A8veV5RIKIHVbbNcVkkhu5LYDObL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف امشب با روسری در هیئت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/130259" target="_blank">📅 02:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130258">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
جی‌دی ونس در مورد جمهوری اسلامی ایران:
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/130258" target="_blank">📅 01:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130255">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLaYANTESJrvx9rUYh7fm1lhizVlg-r9l1CH3cuK-Q3s5swliYnTZ2SsQ2uYGI2c0mJc05sWzNngP8Gq52xplwAazjCW6GXEJkK1Z9DtGhcinLlBuSyi1-WX_pQynhPAa02y9JOrxtV4xJ4yUKzZBHdDSEYeVZaRk8iB9VCKjppwjfOyX_0f-gad4PyVUUmBWzqo5HJra3ZMkX9H0fqGt7Vhbdk2LU_LhErE9oidEhumQfyympnwot2G10TGMvy5DLTMVjzh6vPOEh27cReC2aKM_19d3X9-pL5d_C3ej9Z5E671g4fcCy4tmm4lXdY-VJi95kShnjlCotX4QStfqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSTCIphNKhJPSj_LalUR0OZHCQx883Wu9aMHDAFP5ZntUdnRvcfOTfV0um6f9j4fxzR5q1K5jkgNkRLUw4HZgM4aN0ehhb7-IZv_MlLcle3C4cd5vo_zK72KZ1Dt-XlNedtzDbPZLYEkNzNIWVUkQ_Rit_C0FPz2IilT1li6hlAucPZMvV-t5-OG5HC93KsS2P780wMkUrBtXIarw1cbOjfQunpYptLtHes-NTCeiQR_nXb-AImYsgdxiDecjO81HkIpCtyH9cmselJonXx16539MJJ9WYrxFQyPSHIulkZRy2gUk33DeLW8lWpQq6_u8sLGxjp6loj-n_k9u71GEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojB8Cf74HSAPaqnGt_bxWR-Aur924yKVAPmE4io4ZyRPqkvkG7eRyS-LGkpW2m1xnlw9GSRGTZ2R4k2Htpyu9DmB7b26QLTlJ9svZ0FWqk-qa5ezLys8yfByqx7iJqOFc6-1WSU3TLzwiGIkWvRhAjQWCbwXydI6uHYA0ZnazfvU9sFEc6aOWSe-2fOg9g9oNV9fMu4J0k5rYG7P223Yn484IRbHAayodyDd5lbH34CtkwT9kIuuxuT1gm1kkAZ6irzQRvziU1URcWA9duRhDn46LnAm0DczqdWA7Mw_JxHsk8Bg2TUg4pyDAUNh3qjCHc6jfWk2AP9VPjVO26r1Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شهباز شریف هم نتونست مانع بیل زدن پایان ناپذیر پزشکیان برای کاشتن درخت تو اسلام آباد بشه
🔴
شهباز هی میگه نمادین هست ولش کن اما مسعود ول نمیکنه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/130255" target="_blank">📅 01:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130254">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e31799d4.mp4?token=SZCQJAYNqPVUP-PAD9WlBFzBIUZgsxcZ8wek28Klg5OcPOlSGobSguk7k6SjmkWvIJM9Xmf0GilXLHL1Bdoy9r9eH2e5Wo45LeqxEog-vFlAjcOwZcxgzSQvvkuW6-Qi-5k2gRAJ-0_Ylz1hUsRtDbF5fRQLIoZDeUrboRAkkE9bHEpM0Fgef7TiyAhIoVygWAsZ1sNndl9KMoyBSX-s5jo2uMK02OZTBXrbjW_RJn1hSv5ckkXjpEXOzY6vZhCTBt9erYLuvHSG0qK1YYgD9OC1tPJylB0p80VLLLB8ubFr5mWutN4_PWhx62GyoKpAXA44kS-78_7nlDCKzPUasg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e31799d4.mp4?token=SZCQJAYNqPVUP-PAD9WlBFzBIUZgsxcZ8wek28Klg5OcPOlSGobSguk7k6SjmkWvIJM9Xmf0GilXLHL1Bdoy9r9eH2e5Wo45LeqxEog-vFlAjcOwZcxgzSQvvkuW6-Qi-5k2gRAJ-0_Ylz1hUsRtDbF5fRQLIoZDeUrboRAkkE9bHEpM0Fgef7TiyAhIoVygWAsZ1sNndl9KMoyBSX-s5jo2uMK02OZTBXrbjW_RJn1hSv5ckkXjpEXOzY6vZhCTBt9erYLuvHSG0qK1YYgD9OC1tPJylB0p80VLLLB8ubFr5mWutN4_PWhx62GyoKpAXA44kS-78_7nlDCKzPUasg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یک مداح دوزاری دیگر به پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/130254" target="_blank">📅 00:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130253">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHysa2MlqLvPa4wCpn0ooxiRKh7Ad5RBfZxkoFx80WsEy6iZFQ4PPlbfE_0O3g_lmbWMtJD4npzrE8v9Yp-QAD78d3RwpU5oafwvbg00JYLmGB1dJCUYnSRl2ukNobOUmJe07pHXQo4u_tY6YxH3qzRDgATgu_cZiQKr7N8uDVwxeZW28aXQvmFzq9lzOBMmDxL1zs1qQpIOPOX7Y0eGAiKXWiqU1GHecsieeYeTazd-tWnvyIdEC8m_2566FKloit8eJN1LQLP_q4LswPa7GoQ-nQMlbxCwVJbwoq0-yam7vI8kGtRA7_IJGKGCiJvp62_-pQbk1SphJzEjRB8XLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما برداشته یه آخوند که تنها رزرومه‌اش افتتاح شلتر(خونه صیغه یابی) هست رو هر شب میاره راجع به مذاکرات نظر کارشناسی بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/130253" target="_blank">📅 00:45 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
