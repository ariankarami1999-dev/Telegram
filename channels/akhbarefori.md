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
<img src="https://cdn4.telesco.pe/file/hkrjOUuyViZ1jjCuqIc5TQOzPN2GPYLfNrJcxx3WrsjQ6BUhD-liLfk7oKMaTa7UT4PFsaTSDkP1VwKdpuJeZUXITLCuOy6OUskod1Aj8PxSJZbXhQDxi8AzkM4b6CCvop4PhEmAoMaX6RG-usuhJFJHzTr2VO8eU3SYr794TUtkLLr75ub0se212NSQkwsBmU5UBljNcRDXs3OcAp3khcL_gII6deVcw1vaK69EmXV9kBucpevIIm2nJQbZxJndjdo1kIKc8uN8obIQV1vf4dfMnlo4q39LeXGZ2I44xv7DEtIxHj_GbG92M6b23t19xyouISdl7NlZQFLDKElZJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.16M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 08:19:41</div>
<hr>

<div class="tg-post" id="msg-676567">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a211f83490.mp4?token=IkqamzEutath2UZ6zKC73dXy9u6tOSaQ-6LIX0UdkJEAzF8e3XhnHqArzvr-TEm9sKj7pWByJW0JSj5MgLy1hpQ21ojA5yw0LZGnXYLLzwb5xWzOAJGbuxwlnFgbi58_IfxP0M0r9DPo1kNw-y1NfEsyvMJAF9CT0vDxMd0gqhnh4EwC5FZLgUdTrAhwcDDOt-c1XiMalEPc-d1UXmN3SSMEVu8I4r69XWifKjcY4ZxpoMH68-twdDms2zzKhTLMlsURrJJP87OzmOeszI8vhip3uapMsRJR0e-mIDxhbDVrRBH66vUXUNnX34cDu65_CN8GLgZkDtMD57UM8cBeXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a211f83490.mp4?token=IkqamzEutath2UZ6zKC73dXy9u6tOSaQ-6LIX0UdkJEAzF8e3XhnHqArzvr-TEm9sKj7pWByJW0JSj5MgLy1hpQ21ojA5yw0LZGnXYLLzwb5xWzOAJGbuxwlnFgbi58_IfxP0M0r9DPo1kNw-y1NfEsyvMJAF9CT0vDxMd0gqhnh4EwC5FZLgUdTrAhwcDDOt-c1XiMalEPc-d1UXmN3SSMEVu8I4r69XWifKjcY4ZxpoMH68-twdDms2zzKhTLMlsURrJJP87OzmOeszI8vhip3uapMsRJR0e-mIDxhbDVrRBH66vUXUNnX34cDu65_CN8GLgZkDtMD57UM8cBeXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌های آمریکایی از خاک کویت به ایران
🔹
پایگاه عراقی المحورنیوز با انتشار تصاویری ویدیویی، از همدستی کویت و بحرین با آمریکایی‌ها در تجاوز به جمهوری اسلامی ایران خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/akhbarefori/676567" target="_blank">📅 08:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: در پی حمله آمریکا به یک منطقه مسکونی، یک خانواده ۵ نفره زیر آوار قرار گرفتند که تاکنون ۳ کودک از زیر آوار بیرون آورده شدند.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/676566" target="_blank">📅 08:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TymzKJ3xsFVDglqbl_Vq5IM6cBdnTFM_9KpzRqpMJHTnVnMDe7GD_Mt1CBjczJUW5yML3-a3-Ukq-2PF2FwkHllGQURC8RACJTCVT34itK_11XVFb3YAbmtq4RqS7v7BKO_jzGn3nI4Ns4EzTz5YhDtAUz4uQEwfMbOnZEg8MGaTyB9Bi7s_u7ocT8ZibDn5Z22vbIv6D1bovSCWfJa_51pzk4TW9NTCYctX-HxaxUjJTHtgdwM41krg1Tbqd6MFMwjg1NvwFXUKGUubaYU60tNsXODykeC7ouRKRY1MvTyO6YHj1sSaoxi3qGM13ex8tFbQ3Yi23TIWgq77mCu0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: ترامپ با ایرانی مصمم‌تر در حالی روبه‌رو است که دامنه جنگ گسترش می‌یابد
🔹
با نمایش قدرت از سوی ایران، به نظر می‌رسد دونالد ترامپ بار دیگر در حال بررسی گزینه‌های نظامی است؛ این در حالی است که پیش‌تر طرح‌های تشدید درگیری را رد کرده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/676565" target="_blank">📅 08:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بوشهر  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/676564" target="_blank">📅 08:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8238f76942.mp4?token=jFuuRMY5HsVU5CQdary5KMoG6IPiiX0sKG873JLQ-gPBm4Zo5olXM2TDxg2s_jPk0a6NHLtfxZ8dkw0FXQTUTJX_gj4yKb8kWNDovnunwvj0SsO8zWxvbqLJPJA5YG0HHFCsnv9qmoWN9wwYm4RIEyhWVD4m8xdS-RmP2-cTHDj_y-hlt9zhm6i5ULJciIlNq8f7apGK7b_aC-PF8KEIB2J3CRl_azbytDsBOyi16a1-SuDRFeoX8b3Ui6cPG69GNfDa0Hbkn93ppucZrOak-SBjL56twYhWBvNo0droIrlz6SVbYyyrZGBsAnpKi7xocBpTPbk-lH7i4BFeLJJCQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8238f76942.mp4?token=jFuuRMY5HsVU5CQdary5KMoG6IPiiX0sKG873JLQ-gPBm4Zo5olXM2TDxg2s_jPk0a6NHLtfxZ8dkw0FXQTUTJX_gj4yKb8kWNDovnunwvj0SsO8zWxvbqLJPJA5YG0HHFCsnv9qmoWN9wwYm4RIEyhWVD4m8xdS-RmP2-cTHDj_y-hlt9zhm6i5ULJciIlNq8f7apGK7b_aC-PF8KEIB2J3CRl_azbytDsBOyi16a1-SuDRFeoX8b3Ui6cPG69GNfDa0Hbkn93ppucZrOak-SBjL56twYhWBvNo0droIrlz6SVbYyyrZGBsAnpKi7xocBpTPbk-lH7i4BFeLJJCQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر زانو درد، درد هنگام راه رفتن یا احساس ضعف در مفصل زانو دارید این ویدئو رو حتما ببینید #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/676563" target="_blank">📅 08:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون وزیر تعاون: بدهی فروشگاه‌های طرف قرارداد کالابرگ در حال تسویه است.
🔹
رویترز: چین برای عبور امن نفتکش‌هایش از دریای سرخ با انصارالله وارد مذاکره شد.
🔹
تعداد قربانیان زلزله ژاپن به ۲۸ نفر افزایش یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/676562" target="_blank">📅 07:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
منابع عربی از شنیده شدن صدای چندین انفجار در اردن خبر میدهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/676561" target="_blank">📅 07:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
وال استریت ژورنال: حملات پنجشنبه به معنای بازگشت به عملیات گسترده نظامی نیست
🔹
وال استریت ژورنال در گزارشی نوشت با وجود گسترده‌تر بودن حملات پنج شنبه نسبت به عملیات‌های پیشین آمریکا، یک مقام آمریکایی گفت این اقدام به معنای بازگشت به عملیات گسترده نظامی نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/676560" target="_blank">📅 07:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676558">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b11a7b7d.mp4?token=aB2pPzccIY6j9NUjMgHmn7bhjTQCHAfgHeVC6UK43T_k0c2w8ioGuAOD-WkyY2URNRCQP7GFHqA9cZijypMrwNZEdgkDPmRsQkTmGbDeDay3XMeH3vyDZOWoECRzQrpwcfjt-LDSknxCV77SLbtxXspSwZn4WH2yADivL5Jo8cGpwpQqIhljWI7Y7p5T2wc9_VvxGYPj17A56dSzO7MGtlYgwPCznWniYx73BNl6Tbs7pVJ4i8xkwDwK1r_dVWHj0Lnj2ZH3avSG709FALYbDoNe3ljTKdhaTBneacJB8H6nuepXSJU7AvoD9IHjb6DoKRSO8KMV0_riFSgBSQP-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b11a7b7d.mp4?token=aB2pPzccIY6j9NUjMgHmn7bhjTQCHAfgHeVC6UK43T_k0c2w8ioGuAOD-WkyY2URNRCQP7GFHqA9cZijypMrwNZEdgkDPmRsQkTmGbDeDay3XMeH3vyDZOWoECRzQrpwcfjt-LDSknxCV77SLbtxXspSwZn4WH2yADivL5Jo8cGpwpQqIhljWI7Y7p5T2wc9_VvxGYPj17A56dSzO7MGtlYgwPCznWniYx73BNl6Tbs7pVJ4i8xkwDwK1r_dVWHj0Lnj2ZH3avSG709FALYbDoNe3ljTKdhaTBneacJB8H6nuepXSJU7AvoD9IHjb6DoKRSO8KMV0_riFSgBSQP-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت دوباره آمریکا علیه کودکان ایرانی/ ۲نفری که در قشم به بیمارستان منتقل شدند، کودک هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/676558" target="_blank">📅 07:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676557">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
منابع عربی از شنیده شدن صدای چندین انفجار در اردن خبر میدهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/676557" target="_blank">📅 07:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676556">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ-uw8CHcNubbpgpti8sqBcxhCoAbRa0Re5ufShq_infdgxmtICWCwM-pBkVV8btnn5ezWYS_nDlBsXcCVe4_GSQwjSXmpaVKPT1XA_axTyltZ01vPVBUNVofODL_LDLRbucIzJ3fAQhGjDnlGXrVkgmjdMF8sTrisGCDuShpqeLsR1t-eyELvMIWQB-6d7c9BHjrvCeQBq5CJcY3wu-WM8tiI693DyI5qHM-4sWZpjwXJ2PffR35UxdiVQUJGtOpdgNisZP1tgv7bdJe2Wj_er7ubYPSeSwDWoX1PtW_cSmJ1xyZnByfVk21EVvvaPoHj7gCfcYa8iJey2-BpdZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی ان ان: عربستان سعودی در حال کشیده‌شدن به جنگی است که به شدت تلاش کرده از آن اجتناب کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/676556" target="_blank">📅 07:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676555">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISAVU7tg-OCLTHuxOTw7YqjjGbwJEJAqW4RwGmh6uIrJLiEXX4sp5qm-3QCHzLHxKhrJixv1QDj5nCBowHt5LbWnhl4gwGCalaV1-K9r3WHIY8tdWuNpAvYP6ZGf466MGPeySJ-NuQ8cUuj_BchB7-LX32pgeV39AiAezX4fpRp0visR2DkzKDGoqZMvcKekb8agAxbABY_EnsIDLE9lpUqz1wgqsLQgk3QC9-TDZCaT0jQPiPg9cBuKradIEXp1IG6wPOz-viZhG6FiPfPQkK5ebGtSeuSYnJBsVMTSGnLI7s4OyVNwuhDZlUbzPnNq6GyIW67CzDJmyNYJ_ffewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۸ مرداد ماه
۱۵ صفر ۱۴۴۸
۳۰ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/676555" target="_blank">📅 07:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676553">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0654b37ac2.mp4?token=RjZArAHkyzeqw5Vjk6TyLcknrj90HJhW5q79hV4aoCXCGBzUyfx-ANE4t-e73POHMi7LdthHQHoCMiqMhMg-n9WNaDmjxhCEi3nTDoGtv2QAlhl62GIO7MeHCH-eVKlluDqUHDhZBKejQm0yYIwRveR4j1-OABQfJ6-KTPi7Zxa6qk2DRH4M5TK8qlwnCvMZ_6qLwJP0_cZiOHWZxG9-3EzK9POInoH-soVm7EFCVpgDy6c4HjydVioggZef4kSoa49HRQg1pVdnOaVHuFTe_jhBap0e5ACqfkDgY6tbWK8gdJrR7WkN1imrkiuqNZ8Ugnyk42levLwGaaGSHQvYQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0654b37ac2.mp4?token=RjZArAHkyzeqw5Vjk6TyLcknrj90HJhW5q79hV4aoCXCGBzUyfx-ANE4t-e73POHMi7LdthHQHoCMiqMhMg-n9WNaDmjxhCEi3nTDoGtv2QAlhl62GIO7MeHCH-eVKlluDqUHDhZBKejQm0yYIwRveR4j1-OABQfJ6-KTPi7Zxa6qk2DRH4M5TK8qlwnCvMZ_6qLwJP0_cZiOHWZxG9-3EzK9POInoH-soVm7EFCVpgDy6c4HjydVioggZef4kSoa49HRQg1pVdnOaVHuFTe_jhBap0e5ACqfkDgY6tbWK8gdJrR7WkN1imrkiuqNZ8Ugnyk42levLwGaaGSHQvYQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌های آمریکایی از خاک کویت به ایران
🔹
پایگاه عراقی المحورنیوز با انتشار تصاویری ویدیویی، از همدستی کویت و بحرین با آمریکایی‌ها در تجاوز به جمهوری اسلامی ایران خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/676553" target="_blank">📅 06:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676552">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
عبور تنها ۱۴ کشتی تجاری از تنگه هرمز در ۲۴ ساعت گذشته
🔹
شبکه سی ان ان آمریکا با استناد به داده‌های سامانه ردیابی دریایی مارین ترافیک، گزارش داد که ۱۴ کشتی تجاری در طول ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/676552" target="_blank">📅 06:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676551">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اعلام پایان حملات امشب به ایران توسط سنتکام
ارتش آمریکا:
🔹
نیروهای سنتکام در پاسخ به حملات موشکی دیروز به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند».
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/676551" target="_blank">📅 05:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676550">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
معاون استانداری خوزستان: نقاطی در اطراف شهر آبادان توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/676550" target="_blank">📅 05:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676549">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
عملیات جستجو برای نجات افراد در زیر آوار
🔹
دو نفر از مصدومان در این حمله توسط نیروهای امدادی به بیمارستان منتقل شدند و تلاش نیروهای عملیاتی برای یافتن افراد در زیر آوار ادامه دارد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/676549" target="_blank">📅 05:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676548">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
حملات تجاوزکارانه آمریکا به نقاطی در ایران
🔹
خبرنگار صهیونیست وبگاه «آکسیوس» بامداد پنجشنبه به نقل از یک مقام آمریکایی خبر داد: «ارتش آمریکا در حال انجام حملاتی به ایران است».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/676548" target="_blank">📅 05:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676547">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d85cad8f07.mp4?token=bNX7z0P09k6kkyCYxvMXZ6CXMTQvniULGXGZPA-hiZcEs3eIDNpzwg6uzaIjn1Rp31umtNPoGYPMD03xhVkUBkvpEvCL6cfs9w4LVCs9vtuTxLRM9v5AoMMnzZ-L52wFxj2THIvAjlYyzSrlX9k5kUqNSC2lpPy_BsEdLQ-jiLBnoZvaTbPHd4gTUpxCunMnTcpInuydC4KEDbpjfVBjZ9ZQ3GMeC__6F6toFPbzIsSCvRqih0MetC8UshT9d1xHRjcbDh7lrhfcRQK7BdazVu9NUSHFRZ07QG2SB_iPa0NhGvuxLpAwAgFz44naXeYjwUUIFoyt3liBcvuPDz-25w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d85cad8f07.mp4?token=bNX7z0P09k6kkyCYxvMXZ6CXMTQvniULGXGZPA-hiZcEs3eIDNpzwg6uzaIjn1Rp31umtNPoGYPMD03xhVkUBkvpEvCL6cfs9w4LVCs9vtuTxLRM9v5AoMMnzZ-L52wFxj2THIvAjlYyzSrlX9k5kUqNSC2lpPy_BsEdLQ-jiLBnoZvaTbPHd4gTUpxCunMnTcpInuydC4KEDbpjfVBjZ9ZQ3GMeC__6F6toFPbzIsSCvRqih0MetC8UshT9d1xHRjcbDh7lrhfcRQK7BdazVu9NUSHFRZ07QG2SB_iPa0NhGvuxLpAwAgFz44naXeYjwUUIFoyt3liBcvuPDz-25w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفیسی، معاون استانداری هرمزگان: یک منزل مسکونی در قشم هدف حمله دشمن قرار گرفته که تاکنون دو نفر مجروح گزارش شده و احتمال افزایش مجروحین وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/676547" target="_blank">📅 05:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676546">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
انفجار دوباره در اهواز
🔹
مجددا صدای انفجار شدید در اهواز شنیده شد./ جماران
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/676546" target="_blank">📅 05:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676544">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLhLdmMXenjY8gfNw_jPOLGJEQqOo-_Y78C1QUHMbHkwHdzUuPl4poCtI7TW_f0wb9CjHhbMENwet3qmKe0UfkIIMLbvPQPBL3FQVULKsxrt2bdKrYHFIPvGjyRPa_EVs6Mw7E_bm6dCKoyuYSGkxyiPss1OG-2XbEwRovzPOlwUawCl8b0y_l8tWBuGh7bqLqLCF7hRvlXePkaRXcXJjARvSz2yi2pFbOzIrJU8LDlU9NnLLmzdmRGMRHZb9v-QFLSYiwWJ_GIWpz8jONywy9xrEvqyIBn47znepsEM4LdlY9QYS29hUdlPLAFpWJSN302YfPexKRaenET9xzUKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sP9kCskpQYpSzCdP1p6mrbhbFVGRMIKrlDSvrocuItDtvt2D1nZxLMZh4XC0p_9f0dVWL0TiV7jHeDota0GkWe0TzMnnO0UQ-OG63QxL9CFgrc9A1q_w9bQ1E22H64xjMlflMRPOnIMzOglU0n6KsXr1SbDOGQ3lbu5SQn0bzcoA-CcwEV8EFi_zim80aFTiEnJlmceBo13Ji9nqUMSNPZ0umsiciV4pTVxmW9faHFClIdy6WFHfI_IZoPr-0YB069P6Ng201mBzP5aDBSbKfxFAS5kQQTbvy2aykud63D0iRf2HGj5F2s-Gi_ffFzsHMpPDkZzCUwrdu73iVinOZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر اولیه از حمله دشمن آمریکایی به منزل مسکونی در جزیره قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/676544" target="_blank">📅 05:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676542">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3995d7f98b.mp4?token=OxMl0uSdJWktnaSmJSq3jqOU1BkQjJPbFFurFUsgvfz2OivjpfdCz4v7GNOxvpyszsMOrHC764t7cfDLh-Bl12fa8hIlVPB67A9oD5EUhkNmxx6l0O0oqVVlKdHo4eMzdDYVnNnENU5qkypWxZV49eQLJZX8JU8X54_Qx9nif4tsW_DcfykjclnbBG-N3RsVS0fcssKxifEMXS4TjcUnE79IxHIAKC5kQoaZS5jUmtVuHAzixTZXfe-Mpb4qIfs30rRvswOqt3ZSzE2In8YhAeIHVbVhK3e6agS5PXdK-puZK0hG5zO1gPLpTXyJi8vcxUgfVzW8KXMvcHHO2bQcNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3995d7f98b.mp4?token=OxMl0uSdJWktnaSmJSq3jqOU1BkQjJPbFFurFUsgvfz2OivjpfdCz4v7GNOxvpyszsMOrHC764t7cfDLh-Bl12fa8hIlVPB67A9oD5EUhkNmxx6l0O0oqVVlKdHo4eMzdDYVnNnENU5qkypWxZV49eQLJZX8JU8X54_Qx9nif4tsW_DcfykjclnbBG-N3RsVS0fcssKxifEMXS4TjcUnE79IxHIAKC5kQoaZS5jUmtVuHAzixTZXfe-Mpb4qIfs30rRvswOqt3ZSzE2In8YhAeIHVbVhK3e6agS5PXdK-puZK0hG5zO1gPLpTXyJi8vcxUgfVzW8KXMvcHHO2bQcNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله آمریکا به یک محله مسکونی در قشم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/676542" target="_blank">📅 05:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676541">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
حملۀ موشکی به نقاطی در اطراف شهر اروندکنار
معاون استانداری خوزستان:
🔹
نقاطی در اطراف شهر اروندکنار توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت./ فارس
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/676541" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676540">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d885c0805a.mp4?token=UFLjE_joQ3f8fQdNPcRD-5zUsNKTtzkpadWGy6rnXJU_7DaFzgErIeFqJ40WSTwUVr3EM-fBynBpMZqoLnBIyMo7NP2t3ytsiL5ttSwk4JZP6_Tb4IspRc814rgznlajLdWwzAn6m625vlhGyoOowNWhCyIklHF16rMMqbpC__GX0bKQoTIyvjiAgMEbnNpkP0GvDb7cM0MA4_hi8C37porzTP0I0i9yZxY9fXgPmeECkDQZ7aA2d7AxR4hm9u4TpsMk7eCeOM57yRJmqVJcqmEXRjmVUFidk6mQ6DQL4kmHHXKM-vsbGU3gPnN9HV132DmJB3Bt_JWilDza3E8B6nKd1JoTYY7ee7qEaQ8YKmUJPa_UxwrT-q38hsODwWwMgoojZMBFZMNzVipxY_SbTJSRFK1HG-4WbuhwMdQEEMDRNpyqDybNVVuKrfSVvEqi6FTVexUjwC02naaoX8JFsde_fXaU6lVl5s53so5cw9CKDpjK7Z0auIJWIOPjDiC_DM-zBHuCNqu5EmLJu1nPguy_FGxNz3kERMprAbH7sM8JQ8ZKElxZIAYLfmpzdgYFAV6UtT9Fl_fB3o1wouV1VyznZFE7ur_xtcBnBx27Zkom28JV572ifHCNAdrdlun7uMVXFJ8-nw2AX6Bw5QP3_wMPpjgSMKih7M6-anLnofI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d885c0805a.mp4?token=UFLjE_joQ3f8fQdNPcRD-5zUsNKTtzkpadWGy6rnXJU_7DaFzgErIeFqJ40WSTwUVr3EM-fBynBpMZqoLnBIyMo7NP2t3ytsiL5ttSwk4JZP6_Tb4IspRc814rgznlajLdWwzAn6m625vlhGyoOowNWhCyIklHF16rMMqbpC__GX0bKQoTIyvjiAgMEbnNpkP0GvDb7cM0MA4_hi8C37porzTP0I0i9yZxY9fXgPmeECkDQZ7aA2d7AxR4hm9u4TpsMk7eCeOM57yRJmqVJcqmEXRjmVUFidk6mQ6DQL4kmHHXKM-vsbGU3gPnN9HV132DmJB3Bt_JWilDza3E8B6nKd1JoTYY7ee7qEaQ8YKmUJPa_UxwrT-q38hsODwWwMgoojZMBFZMNzVipxY_SbTJSRFK1HG-4WbuhwMdQEEMDRNpyqDybNVVuKrfSVvEqi6FTVexUjwC02naaoX8JFsde_fXaU6lVl5s53so5cw9CKDpjK7Z0auIJWIOPjDiC_DM-zBHuCNqu5EmLJu1nPguy_FGxNz3kERMprAbH7sM8JQ8ZKElxZIAYLfmpzdgYFAV6UtT9Fl_fB3o1wouV1VyznZFE7ur_xtcBnBx27Zkom28JV572ifHCNAdrdlun7uMVXFJ8-nw2AX6Bw5QP3_wMPpjgSMKih7M6-anLnofI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان: حمله دشمن به یک منزل مسکونی در قشم، چاه‌تنگو؛ عملیات جست‌وجو برای یافتن دو نفر زیر آوار ادامه دارد./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/676540" target="_blank">📅 05:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676539">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
برق مناطقی از قشم که بر اثر حملۀ دشمن آمریکایی قطع شده بود، پس از مدتی کوتاه وصل شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/676539" target="_blank">📅 05:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676538">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
انفجارهای مهیب و پیاپی در اهواز
🔹
دقایقی پیش صدای چندین انفجار شدید و وحشتناک در اهواز شنیده شد./جماران
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/676538" target="_blank">📅 04:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676537">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01ec2c1ce5.mp4?token=WOpMpdOTqGsCgdF-mfGx36DGrWgAoGpp_b6pnjOTZxNBIwtpvQRq5t2une7VnjVMryOIIxYhzIRJs-JCePYf_BmdJZ0rHmeTPTGJ1CUeNrifv5W4rq0eDrXMPwdQRnWbN-O9623EzsuIJqG_0ijqoITK1z_CHtXKl_bl9rVOYB0_Y-Z07GqFNLYc3gFCfF2Hh368TB2fg1qUydQjjyMAgzKoa5_LW3SfAma41j-9OuafsXW1WKPfTfisjfcWT_IDPPL7Jc_F9OgvynbnwW7wTllywqBZ5bdEnVvyrprpi8ZapzNeR7xOnH9Qn79PerKGaxFs5laoB68n-0PJym6Tpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01ec2c1ce5.mp4?token=WOpMpdOTqGsCgdF-mfGx36DGrWgAoGpp_b6pnjOTZxNBIwtpvQRq5t2une7VnjVMryOIIxYhzIRJs-JCePYf_BmdJZ0rHmeTPTGJ1CUeNrifv5W4rq0eDrXMPwdQRnWbN-O9623EzsuIJqG_0ijqoITK1z_CHtXKl_bl9rVOYB0_Y-Z07GqFNLYc3gFCfF2Hh368TB2fg1qUydQjjyMAgzKoa5_LW3SfAma41j-9OuafsXW1WKPfTfisjfcWT_IDPPL7Jc_F9OgvynbnwW7wTllywqBZ5bdEnVvyrprpi8ZapzNeR7xOnH9Qn79PerKGaxFs5laoB68n-0PJym6Tpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه شلیک گسترده موشک‌های آمریکایی از خاک کویت به سمت ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/676537" target="_blank">📅 04:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676536">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
معاون استانداری خوزستان: نقاطی در اطراف شهر شادگان توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت
./ فارس
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/676536" target="_blank">📅 04:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676535">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
حمله دشمن به نقاطی حوالی قشم  نفیسی معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان اعلام کرد:
🔹
در ساعت ۴:۰۰ نقاطی در حوالی قشم مورد حمله نظامی دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد./ مهر  #اخبار_هرمزگان در…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/676535" target="_blank">📅 04:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676534">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای فاکس نیوز به نقل از یک مقام آمریکایی: حملات هوایی آمریکا به ایران طیف بسیار گسترده‌ای از اهداف را هدف قرار داد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/676534" target="_blank">📅 04:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676533">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
دقایقی پیش صدای چند انفجار در کیش به گوش رسید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/676533" target="_blank">📅 04:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676532">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کازرون
🔹
منطقه‌ای در اطراف شهر کازرون هدف حمله دشمن آمریکایی قرار گرفته است.
🔹
اخبار تکمیلی متعاقبا‌ً اعلام می‌شود./ تسنیم
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/676532" target="_blank">📅 04:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676531">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
منابع محلی از شنیده شدن صدای چند انفجار در بوشهر و بندر عباس خبر می‌دهند ./ همشهری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/676531" target="_blank">📅 04:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676530">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d49cdbe6.mp4?token=Rr5eC5o-VF8622374D51PvFRLNQFvxltCBIrOVaVy4xgWEUSKR0rVCS2iXaWyimaPpJDgT72TrahORPAaKJVaLsQTEy8c7lAFSdwTbCnDMTo3Bt5vMcv5JvrNOtE91rFVhyTDMcJkcAZLG_ZGXkWdYn97qFaPQjY5merHNp41J4ik6nWbK4_8WtKaGEJ7phobEZupNHInmQfYRPIk1ajb6FlZQHTVdCRJnPAeiP43nDDaONJjP7ynhvMNJaFi1X9CV1oDCoWiB09HklRGYfAHl7b0VLwcOW8xwPWelcvoqvuoKLTI8_HSSjoevKBvsahTOnXUMd4EdZ0tftnA59A-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d49cdbe6.mp4?token=Rr5eC5o-VF8622374D51PvFRLNQFvxltCBIrOVaVy4xgWEUSKR0rVCS2iXaWyimaPpJDgT72TrahORPAaKJVaLsQTEy8c7lAFSdwTbCnDMTo3Bt5vMcv5JvrNOtE91rFVhyTDMcJkcAZLG_ZGXkWdYn97qFaPQjY5merHNp41J4ik6nWbK4_8WtKaGEJ7phobEZupNHInmQfYRPIk1ajb6FlZQHTVdCRJnPAeiP43nDDaONJjP7ynhvMNJaFi1X9CV1oDCoWiB09HklRGYfAHl7b0VLwcOW8xwPWelcvoqvuoKLTI8_HSSjoevKBvsahTOnXUMd4EdZ0tftnA59A-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکمیلی/
همدستی دولت کویت در تجاوز آمریکا به ایران
🔹
شلیک سامانه‌های موشکی آمریکایی از خاک کویت به نقاطی در ایران همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/676530" target="_blank">📅 04:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676529">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بوشهر
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/676529" target="_blank">📅 04:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676528">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
معاون استانداری خوزستان: نقاطی در اطراف شهر آبادان توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
/ فارس
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/676528" target="_blank">📅 04:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676527">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
حمله دشمن به نقاطی حوالی قشم
نفیسی معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان اعلام کرد:
🔹
در ساعت ۴:۰۰ نقاطی در حوالی قشم مورد حمله نظامی دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/676527" target="_blank">📅 04:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676526">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5fc7618d.mp4?token=EJI0pmaQjhGoLB7r7h6xZOTlS-5dGsKvwLw1w1s3Kk9lFMexAQ3e6He42glzs3kfd9_dcwnN1gqv0EM3v23sNNRPEqnPG22LR8-NkkqgneZdjuqd5uVHUeS9cMJ4FeEdNIHHR_fX4pDD9AhLWo3zyGkNUPn_fxNwX6HFG7h9GZY-fGr_332F5-7R-7U4cSWctfHIJC1xZhnoLOENWJpxuCby-uYsOqh2-wjeO0tES434bSM7yf4R5NhvVRmZ5SmQCLEpjEAUWUoH8k9CLYfzESXgMANBx2zsTdz0GKaa_jZwrcKbdl6XdViHTHRUpTrcw8eTS0KIzhfFaAxL0aN6GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5fc7618d.mp4?token=EJI0pmaQjhGoLB7r7h6xZOTlS-5dGsKvwLw1w1s3Kk9lFMexAQ3e6He42glzs3kfd9_dcwnN1gqv0EM3v23sNNRPEqnPG22LR8-NkkqgneZdjuqd5uVHUeS9cMJ4FeEdNIHHR_fX4pDD9AhLWo3zyGkNUPn_fxNwX6HFG7h9GZY-fGr_332F5-7R-7U4cSWctfHIJC1xZhnoLOENWJpxuCby-uYsOqh2-wjeO0tES434bSM7yf4R5NhvVRmZ5SmQCLEpjEAUWUoH8k9CLYfzESXgMANBx2zsTdz0GKaa_jZwrcKbdl6XdViHTHRUpTrcw8eTS0KIzhfFaAxL0aN6GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اطراف بندرعباس
اژدهایی خبرنگار صداوسیما:
🔹
گزارش‌هایی از شنیده شدن صداهای مشابه در جزایر بوموسی و کیش و همچنین محدوده دریایی قشم و تنگه هرمز منتشر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/676526" target="_blank">📅 04:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676525">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای سنتکام: نیروهای آمریکایی امشب ساعت ۸ به وقت شرقی، حملات خود را علیه ایران آغاز کردند. این حملات پاسخی قدرتمند به حملات دیروز ایران علیه نیروهای آمریکایی مستقر در خاورمیانه است.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/676525" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676524">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
برخی منابع محلی از شنیده شدن صدای انفجار در جزایر کیش و قشم خبر دادند
🔹
مبدا و دلیل صداها هنوز مشخص نیست./ خبرگزاری دانشجو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/676524" target="_blank">📅 03:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676523">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e2d8b313.mp4?token=Zu7yYkbm2xny-YVsgZGsheTSkMWCSe5ft4wLXRVDkkKraT_I7ktvCcmzd7d1GObd1jUnFMfTYMzfkFQV3BN3Fzpjg_TWJYe21QE-N4DOWwrbr91y2WJWsy4NCtHgytunmAitBv4_eYkSAVLFDDLIp9lhiVj_BAD1HCTPXGrLNu7mPgAehqzCva4FhZ9Rn2itr49KxF8Qavcil3kVwgyz5ZsIZhD1qb4Wk-zmOis9WCwWZ2uhfWAWbYWmvlZDPWX2zDaLTUa2Hp7t_Z62jiNEmantSFWLB5A47Tvn3IYoCDemFl_O_-MhzkCx48ao1bbeYvf3dcDltoSFFkYDbqRUgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e2d8b313.mp4?token=Zu7yYkbm2xny-YVsgZGsheTSkMWCSe5ft4wLXRVDkkKraT_I7ktvCcmzd7d1GObd1jUnFMfTYMzfkFQV3BN3Fzpjg_TWJYe21QE-N4DOWwrbr91y2WJWsy4NCtHgytunmAitBv4_eYkSAVLFDDLIp9lhiVj_BAD1HCTPXGrLNu7mPgAehqzCva4FhZ9Rn2itr49KxF8Qavcil3kVwgyz5ZsIZhD1qb4Wk-zmOis9WCwWZ2uhfWAWbYWmvlZDPWX2zDaLTUa2Hp7t_Z62jiNEmantSFWLB5A47Tvn3IYoCDemFl_O_-MhzkCx48ao1bbeYvf3dcDltoSFFkYDbqRUgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک موشک‌های هیمارس از کویت به سمت ایران
🔹
منابع عربی تصاویری از شلیک موشک‌های زمین به زمین هیمارس از خاک کویت به سمت ایران منتشر کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/676523" target="_blank">📅 03:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676522">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
گزارش‌هایی مبنی بر وقوع انفجار در آبادان و کیش./ همشهری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/676522" target="_blank">📅 03:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676521">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
گزارش‌هایی مبنی بر وقوع انفجار در آبادان و کیش./ همشهری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/676521" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676520">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1001d1ab.mp4?token=ruIE9BPuDxK7Fudr9w9lbu3J7glEVeleERlCOfjaJavvvkQKnxK103MkLogbFm6rDyr4OzdAmTrRy4kie7n5s6SbVAGI-UZaGd40kzOmTqEA1Txulz2Erjna7qpOf1iFt90wokOtP7OGQJpP5b9xCNRag1TVhmYApJ3fxPq4DqB73xQ6ysmKXIK3PHguayakbyt8kmC1pOjnnUJTKE7pCTgfYKiQRKOVX8LJp_juNPOhCBN5IqvW9rw1Y1sJG-ra6UCHuXDOdP3rLR0a-K-GVwUedvVeE_MxHhGeP3E048J21taadlxb1kU_1Eqw0FG_CrnlJHEuDgjvP9fFbSC-NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1001d1ab.mp4?token=ruIE9BPuDxK7Fudr9w9lbu3J7glEVeleERlCOfjaJavvvkQKnxK103MkLogbFm6rDyr4OzdAmTrRy4kie7n5s6SbVAGI-UZaGd40kzOmTqEA1Txulz2Erjna7qpOf1iFt90wokOtP7OGQJpP5b9xCNRag1TVhmYApJ3fxPq4DqB73xQ6ysmKXIK3PHguayakbyt8kmC1pOjnnUJTKE7pCTgfYKiQRKOVX8LJp_juNPOhCBN5IqvW9rw1Y1sJG-ra6UCHuXDOdP3rLR0a-K-GVwUedvVeE_MxHhGeP3E048J21taadlxb1kU_1Eqw0FG_CrnlJHEuDgjvP9fFbSC-NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها درباره شلیک موشک از کویت به ایران
🔹
رسانه‌های عربی از جمله «صابرین‌نیوز» با انتشار تصاویری گزارش دادند که سامانه‌های موشکی تاکتیکی ارتش آمریکا از خاک کویت به سمت آبادان شلیک کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/676520" target="_blank">📅 03:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676519">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
حملات تجاوزکارانه آمریکا به نقاطی در ایران
🔹
خبرنگار صهیونیست وبگاه «آکسیوس» بامداد پنجشنبه به نقل از یک مقام آمریکایی خبر داد: «ارتش آمریکا در حال انجام حملاتی به ایران است».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/676519" target="_blank">📅 02:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676518">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
پیشنهاد سنتکام به ترامپ برای حملات دو هفته‌ای به ایران
نشریۀ وال‌استریت ژورنال:
🔹
فرماندۀ سازمان تروریستی سنتکام طرحی را به رئیس‌جمهور آمریکا پیشنهاد داده که ذیل آن، تا دو هفته به زیرساخت‌های موشکی ایران حمله شود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/676518" target="_blank">📅 02:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676517">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
چند انفجار شدید اربیل عراق را لرزاند
🔹
به گزارش، شبکه اخبار عراق اعلام کرد که پس از شنیده شدن صدای این انفجارها، ستون‌های آتش و دود از منطقه قسری در اربیل به آسمان برخاسته است.
🔹
براساس اعلام رسانه‌های عراقی، هم اکنون سامانه‌های پدافندی کنسولگری آمریکا در اربیل نیز فعال شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/676517" target="_blank">📅 01:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676516">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjCXb3aBdhceoPe6i5T6J3xziAt5H5mCgR6NPiKgVVn16GH_Ziz5DTrqR9K1ifbtXdc3bQ0YNKcexeYldy6Zc1gVzfXr81o9gRMoCXQ6lZDdwKGtSdVHoEjO4WrO1dbjnemhBEwe-LwM-SYZGwKdYNunIfNNGuhTKLcSjL0aLUD4CegXl-AGDRG_t148GrlDhyYTuEVDhZ3XU7FzgTUpwHbxA8UG5YD8mbDX__vK7ksqIquraCViFmlWyD3gHkiM-2bsav0mMuW03x8XtuamRUhWR0pFrNlAZt0Pl4eRLx_1ZKgJyayBQj36oy1-6UKgZM1I1F8c2pUZ_yfJIZ8jGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر فروشگاه آنلاین داری، این پست می‌تواند هزینه تولید محتوایت را نصف کند.
قبلاً برای هر محصول باید:
❌
عکاس می‌گرفتی
❌
لوکیشن پیدا می‌کردی
❌
ساعت‌ها زمان صرف می‌کردی
حالا کافی است یک عکس ساده با موبایل بگیری…
رقبایت دیر یا زود از این ابزارها استفاده می‌کنند؛ سؤال این است که تو زودتر شروع می‌کنی یا دیرتر؟
@digitall_cast
ارتباط با پشتیبان :
@Digital_cast_support</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/676516" target="_blank">📅 01:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676515">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a98Y-UX7SNllfACX9ACm2f0_zK-K93mwjkjX--N3f3Y2ypAKyX_-xl8be4qyDlY0RtEBQswBrdCvBT2HbyeoByPCTkeUhabZsmHA2fMzWu4QrYwTup_9f2SNLbXoAolhsBtvE_31aqtW3nQSqDLApwpb9AhPSv-kS_JsO5Jxd_ADvEfIHoNAYWLqUu5nxtOyoWyIU00Zb_g1NMVYUKHaFMefSw-fOH2_M7kWZxIsF2rOgfDlA0rI5MV0vStYIdaQRu489jJy8tGJFB7vSHIWmsOrEGw6OkGNdqIUr9dn4tV3RfbBA3rVTSkvsPxWO_ztzYS8iEOXC50PufV6lNlKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسیاری از هواپیماها در خارج از فرودگاه ریاض در عربستان سعودی متوقف شده و فرود نمی‌آیند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/676515" target="_blank">📅 01:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676514">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKXPOaRheJO9ckjHz5e_G_JBI02DGQ8OD94wU6FpMJFmlpXzMW_N1Y3hvcegzszomiHvdWa8Ynuu2sg16ESrSGeK-FRT2jtVmp2o79Mxgxx_audp0OTwIOBnI3awc0eymfI9PyX4YxllXmUdKfgZySpLMPHQffn0L4myFan1P9irPlVpEtldCibtfZ4QjWR3Lo052mt3nm-em0zNAcDAHqUfv8UZtItmIRD8k7F7FLTNIQv2IU00XogIKlHFezDlFYStaR5FMbhvWIMZkde8bkRPkZg93Z9SgM8_IIGRZ6s6V_BJQM0k8s4ej_YE59qhkAMHdVDSL6GAHfkpJrtAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعلیق فعالیت فرودگاه «ملک خالد» در ریاض
🔹
منابع عربی می‌گویند که فرودگاه بین‌المللی ملک خالد در پایتخت عربستان سعودی، بعد از شنیده‌شدن صدای انفجارها در ریاض، موقتاً بسته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/676514" target="_blank">📅 01:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676513">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع انفجار در ریاض
رسانه عراقی «نایا»:
🔹
صدای دو انفجار نامشخص، به وضوح در ریاض، پایتخت عربستان سعودی، شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/676513" target="_blank">📅 01:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
روزنامه وال‌ استریت ژورنال به نقل از یک مقام دولت آمریکا ادعا کرد که
دونالد ترامپ همچنان در حال بررسی گزینه‌های خود است و هنوز تعیین نکرده که حمله به ایران در کجا و با چه شدتی انجام شود
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/676511" target="_blank">📅 00:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ترور ناجوانمردانه در شهرستان ایرانشهر
مرکز اطلاع رسانی پلیس سیستان و بلوچستان:
🔹
ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی که متأسفانه استواریکم "مهران سالارزاده" به درجه رفیع شهادت نائل شد.
🔹
تلاش برای دستگیری عاملان این سوء قصد ادامه دارد و اخبار تکمیلی متعاقبا اطلاع رسانی خواهد شد./مهر
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/676510" target="_blank">📅 00:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3c2975d3.mp4?token=E_0CTGRypleKqo-HQQhYYVd8jI0nBioL1ZsdNpwZIDNfYvUPOMO9r0anOHCktcV0Bj8OcrTkRlPrEylgdxvmIs6xeT2NXbdD2WKKllck5iu0jz7byx8trNmzph-ZLp-xoRuQreXGsZcEiJDuu3dym0TF4qTsw_5ESNMnmvYXSoFMZv5haTibtSJ7-Ser16KDS_bvDppUhNWovToMW3qCzwYC5dOYrQ-I8XY9sbqGuR5L9bKv9nDGZ7U1-ZkORZBMSowSX0yGyHDN31iLgU8bcX7HhNHCbHxlBnVq7PY0MK_663n6KlX1taJkKr0WK-ggvZ-98xv42sBU-4ZOS-Fnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3c2975d3.mp4?token=E_0CTGRypleKqo-HQQhYYVd8jI0nBioL1ZsdNpwZIDNfYvUPOMO9r0anOHCktcV0Bj8OcrTkRlPrEylgdxvmIs6xeT2NXbdD2WKKllck5iu0jz7byx8trNmzph-ZLp-xoRuQreXGsZcEiJDuu3dym0TF4qTsw_5ESNMnmvYXSoFMZv5haTibtSJ7-Ser16KDS_bvDppUhNWovToMW3qCzwYC5dOYrQ-I8XY9sbqGuR5L9bKv9nDGZ7U1-ZkORZBMSowSX0yGyHDN31iLgU8bcX7HhNHCbHxlBnVq7PY0MK_663n6KlX1taJkKr0WK-ggvZ-98xv42sBU-4ZOS-Fnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بین‌الحرمین میزبان زائرین پرشور و عاشق اربعینی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/676509" target="_blank">📅 00:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1a77561e.mp4?token=cEqltR7L2jKL37zBPJKVAUjYdtzs7oWSEbuYGFFqX6HBuKIAupl5GoVD3ZuKFBjBdUrtAnmBMhxRQw9o-SXDXNeUMSq6hyMNjN6N_-N4X_V_TtHVewPxUBkWCf4DoKCK2RjOcgeg2y43wJwm2bGqElnp68b6KCmZM4MerZKuDXWK_83zAFCXwBrvDQdyw5M3iI4ym0-v8vE01rRY9Cqn2r98IE_4F6s0Mp7RwNw2DAyE95qPXWEzbCVTt3MtxXV0zi3rc1dx9a5WhAr0VqnyKCdFuPDRuftjhgvreg4AuDLwe7EfVwMF1tkeR_mjweZlcsyiLr7ivADvcpX448fRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1a77561e.mp4?token=cEqltR7L2jKL37zBPJKVAUjYdtzs7oWSEbuYGFFqX6HBuKIAupl5GoVD3ZuKFBjBdUrtAnmBMhxRQw9o-SXDXNeUMSq6hyMNjN6N_-N4X_V_TtHVewPxUBkWCf4DoKCK2RjOcgeg2y43wJwm2bGqElnp68b6KCmZM4MerZKuDXWK_83zAFCXwBrvDQdyw5M3iI4ym0-v8vE01rRY9Cqn2r98IE_4F6s0Mp7RwNw2DAyE95qPXWEzbCVTt3MtxXV0zi3rc1dx9a5WhAr0VqnyKCdFuPDRuftjhgvreg4AuDLwe7EfVwMF1tkeR_mjweZlcsyiLr7ivADvcpX448fRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک شهاب سنگ آتشین عظیم در آسمان نیوزیلند مشاهده شد
🔹
مردم محلی می‌گویند: «شب هوا کاملاً صاف بود... و ثانیه‌ای بعد، یک چیز بزرگ، شعله‌ور و آتشین در آسمان ظاهر شد.»
🔹
کارشناسان معتقدند که ممکن است بخش‌هایی از این شهاب سنگ به زمین سقوط کرده باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/676508" target="_blank">📅 00:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiDJwnQQe0jqGj5n6ToTF7-TS4_Zn_B9cvcyFcT_KMmNgkfyA6tMznRiqPs5XhqvezbnEq2MqtDfXyAzmsX7TQ9xVLyTqpr_vUQ3DqnqBjTGVhpSHi7d1wJDJeebukVJqknxJorl9NQNBU_p3pwlD7lAEBmDGTNwNo0ohYy4Esd5w7lIhdbaCIIvvXQ8VMBB2LNzX_rzOg73AaANjc8WnoGbTFmbdLYmrXKiGLNYgPuxsgktd8v4E7XdLMoDOW6S9yZR8x0RMyGp6WSA-Z_SCdNs5z43gsg85pQCT-T8gVLybvE_nYNeWKmTtuRx9JpUMVXPIPZalHGon-WCVENWYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/676507" target="_blank">📅 00:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676506">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoZ-jaDt1CwyGp6hTxjdqycheM1Xrj0LzH_plazGLAwaO14XYiz8ij6wCgEpaZwh6UQLC94uYtL1h8RNTVM9AMgA3aJbOCV_uApb_TOIV-aQuNAPTgjTDmEDU_t1oQbtwD9YTZbDC6ghdhWSKIFOymAwR30Tw6gxKcDMKSJHyArHf4E2Nzffq8RxN5mXEhXBVFSvBQWhOtgyB0IKcIvo5hjFTW7Q1xBTrBNH95ax0azd7IpzFRueN06bwDZHVO9QcuYwhM55CPu1N1uHkFyWv-iZeBoGQulsqQHTddrJKe5MpCg2SGqLfoEx8dO6NLhRQkQXVSIYJPUDPa_x3C908Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده حمله به عراق/ پروژه مرموز «اختاپوس» توسط موساد فعال شد؟
🔹
درگیری شب گذشته در یک زمان بسیار حساس رخ داد. آنطور که کاظمی قمی، سفیر پیشین ‌ایران ‌در عراق گفته است: حمله به عراق، آن‌هم در آستانه سفر نخست ‌وزیر این کشور به عربستان، نشان می ‌‌دهد، دستی در کار است تا جنگ منطقه‌ ای را تشدید کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3234193</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/676506" target="_blank">📅 23:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676505">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9oW2gikRqE4R2Ti5hXJhZY4wIJTyfgc1TFKJAwEWoUxQRGBzEhMeAMLLAKa3Fn7jAh_O6BTQhWF46JYzIsASnWsNriEDNnvmoJGWZT4dyVsIxP_c1Qdyy15lKd3PNgxv6VQzxCIlzYGRv8MlrL-YgtY7y0SlW_uEDB4Kq1YhiZEK6d-La3tMvdRWiJ_3DWQxDTH-NZr4zk3rMwZ37WN6JH7Pnp05ziZDcuHMmGiBpiwFSrUzZbV8QJhdylxGxBLwfPTBFI_rwYZrXWid212GX2bMaekLDlVNnuNkJB8P2RSA-43pQSM4HUbs2z4Y1ZjRbLKGzEjh_vzScSrs7KwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب جمعیت عربستان و همسایگان؛ چالش‌های پیش روی ریاض
🔹
عربستان با ۳۵ میلیون جمعیت، میزبان ۱۸ میلیون مهاجر پاکستانی، بنگلادشی، هندی و مصری است و از ۱۷ میلیون شهروند سعودی، بخش بزرگی شیعیان هستند که از سیاستهای آل سعود ناراضی‌اند.
🔹
این در حالی است که عراق ۵۰ میلیون و یمن ۴۳ میلیون جمعیت دارند؛ رقمی که موازنه منطقه‌ای را تحت تأثیر قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/676505" target="_blank">📅 23:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676504">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
‏
معاون سابق وزیر جنگ آمریکا: نتانیاهو با کارت اپستین، با ترامپ بازی می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/676504" target="_blank">📅 23:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676503">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
پشت پرده حمله به عراق/ پروژه مرموز «اختاپوس» توسط موساد فعال شد؟
👇
khabarfoori.com/fa/tiny/news-3234193
🔹
ترامپ در مواجهه با رضا پهلوی در مراسم خاکسپاری لیندسی گراهام چه کرد؟ / ویدئو
👇
khabarfoori.com/fa/tiny/news-3233989
🔹
موشک‌ های ایرانی، همسر دوم مرد اردنی را لو داد
👇
khabarfoori.com/fa/tiny/news-3233917
🔹
خواننده پاپ برای همیشه از ایران رفت
👇
khabarfoori.com/fa/tiny/news-3233955
🔹
خروج پردردسر علی دایی از مراسم بزرگداشت اکبر عبدی
👇
khabarfoori.com/fa/tiny/news-3234155
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/676503" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL5ejQ_wW5R4QSbKZUQ27s4RVbPU8XS5ZE8HqLzA3rtCLDJmuNV3ZKpl4QjRGLaPvImn0c3CYhXK-bpyzeXG4bxNB-fCVxo0GGLDsiYZazj2N3wXfEyvS-Qhn-CG__W1Tym5AFPFHRpcraKgAzkmWK9l8aSD6ZqAAvKlIujm2q731Gc5B9uyPtL_gsVLjJkEEy0aK5zCEYiFCSlgObmLfcDAIBifDw4gRpAVyZ-Mn8xhzApK0zXzvALopc2yp0uIbEXNtuez_1Kg_R7nrnYG5LJYTOZzOEbRPf1F0qDfiFaCwM8zt6uWsDIjmeMzqBXz9Qu1EAzunwLpXORpenJO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سندرز، سناتور آمریکایی: ترامپ گفت که هزینه دارو را ۱۵۰۰ درصد کاهش خواهد داد، دروغ گفت
🔹
دولت او در حال پایان دادن به برنامه یارانه مدیکر است که هزینه‌های تجویز دارو را برای حدود ۲۵ میلیون سالمند افزایش می‌دهد.
🔹
شرم‌آور است. ما باید هزینه‌های داروهای تجویزی را کاهش دهیم، نه اینکه آنها را افزایش دهیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/676502" target="_blank">📅 23:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676501">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haOQYjdDf18YzzjBh4tiOZL3eLsqS1z3edfbUXpe7gpeucCkqRG2TiVfou7FfBMpNAyvWtZE4xUsNWPX6Mu5qlyfnGvVr7nEpHv6DIVPqLDFKcKX9i4snJT1-VN8wJ8_SlHSiuxAcFtLlhdXFrZQv-YCLxTAhsDc-QXek3SfrdC4avRFnZweqymyYDc3j1D6u6WlNZG5lnQJwKufYquEAD6RJ7u-GjlTi-s0IIKg0DNULM3N5oWAsNjJypy4qnbKRIskX8BDD3Jim3S2JVWr4ocCVyWZRM-9ZZLpdg2FG8aORLcrZBvGAxIyY0nz-pGU3ni5lOOUDNGlbc8Q8hU4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیمی از انگلستان اسیر خشکسالی شده است
🔹
دولت انگلیس اعلام کرد به دلیل«بارش کم سابقه باران و دمای بسیار بالا»، بیش از نیمی از انگلستان دچار خشکسالی شده است.
🔹
این کشور چهارمین موج گرمای گسترده خود در سال ۲۰۲۶ را تجربه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/676501" target="_blank">📅 23:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676499">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etCPak3J73XC0u1gjcB1IunHN06UgloG-_a26doGLHnHoYsN7agBP_y1witMrGZDrtN0-cT6LEz7Y8jZbrzzR21dY8qvQnkpnChQi1KfTp_BSC2UtWiMPd1ESTJOz737MHk0GPUgZG7cB4G674Y8aP2bHDC5SFrJZOF1-o0htKQ0W0jWMEjAWIc6BSY--uULRWA3hbGooN83i2w2cocpyUqxMQ0JYgxcqxs41GNekm2BEF6ODfV3LNF5CRG7OhS1nJ5rA4FEj459pg0AJOWoe3Fv2g_66JGif9qkr7YlDgOyob7KjRmJZRv2oA2idCATk0dwvFYuEBesepvzrO2R9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_5hd69tYU3adUPXbT8qcos4Y80Jo2P33jM140eA4cAe6duyk0M_Zvyy8dQutFDfpCTKLS39OGKqs_H43KgGbOhXc018wH-8ThGcDX4GisCQhNWrS4vYbQQia-2_v3Lf8gDK1OyNzrW_Va-z-dwD2p7cGjVrYWHIzwIuHFif1pM1_w1OVpZB_dJNrn4xOiJPQt8L7a0qYkWAdmaOq0yHRyJRphkQS1GKmMN07nXalCkVUPWTYAfsjVpRnfyQtqcHk4O7AOGjGzUZKpVlNI5XnBDH7qzq0fuZ0cWDslgZJB76Q6GCRiKPUm1cLLYwYg7bLBy7CDpC2xkjMVkfX87Yvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر برای تربیت دینی نوجوان خود چالش دارید، این کتاب را به فرزندانتان هدیه دهید
🔹
«نامه‌های بلوغ» میراث فکری و تربیتی اندیشمند بزرگ، علی صفایی حائری برای همه جوانانی است که در آستانه انتخاب‌های سرنوشت‌ساز زندگی ایستاده‌اند. او با زبانی صمیمی و عمیق، از بحران‌های…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/676499" target="_blank">📅 23:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676498">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9tqzqniFBkhfTeoZUcDnLf-PmcAQ9gFAGcjEDDHiJIN_l2mzxWoRxpFfOijyUOMqc_J5frVGmu1VWTXMYCNnM5oQa2ku5r5y__6MZQ3wZMEHttt_0V_2G_FsJoSErQ1PTRZYVgyoYT4cpNQTwO0EUhCt4qBOd4T5POu5-D7U1YCf4-9BdpIe7KWgdkocQqqwWadMFUh7Ijm1QVW835GaJ957t2xlsOS8bdCBjaTaz0rsUde7xHvAAFrdKpCmfcTr7nx_3WVIxJolNrxr3tx_t4Uj_xHgdRlst6blyoPGnSgO0kW2wDoOOfzo5Q-OXILnBG7b4a2Yw8DBFgLwlT87A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واگذاری هفت تپه متوقف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/676498" target="_blank">📅 23:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676497">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
خوک هار درباره ایران: من دوست دارم تعرفه‌هایی علیه ایران اعمال شود
🔹
این واقعاً همان چیزی بود که لیندسی (گراهام) می‌خواست./ انتخاب  #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/676497" target="_blank">📅 23:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676496">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
روابط‌عمومی سپاه: بستن حساب کاربری روابط عمومی سپاه، نشانه‌ وحشت از داده‌های دقیق ملت‌های آزادی‌خواه منطقه از مواضع آمریکایی است
🔹
به‌زودی درگاهی جدید، امن و مطمئن برای ارتباط مستقیم با ملت‌های آزادی‌خواه جهان معرفی خواهد شد تا مسیر تبادل اطلاعات و آگاهی‌بخشی، مستحکم‌تر از گذشته ادامه یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/676496" target="_blank">📅 23:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15f83dac0a.mp4?token=Dzi1cJ9voS75JGrm-Cm4F3j-RErpYlHR0m_UoN7FufXs74rEhUYZxGqBa4Ohp6F5iTPidy0GNNDP4X6FWQ1snUcYaQttr8lhuBHJsoTBxsXnOWOlydKl8gyQkmlhPACQIDogNRCu9S6opRGLRgpQWzFQ7RGj46X8jvS02Nw9_k5Rr_HmcSdcv_JXXH-9qc-7axiK8tzfa82wZte7StkwGqU5Vjzz2hUUsiaeVCqiP8g7xmph3R5098oKX_q-5bwjOTU2BIpk31hlrNanLf3Tl0VFkiDJ-nfy9Bitkj4PKK4oQVnKQu_vpZE2lkqVeYvkWvMFhYNjB4-ABAEh2-Oucg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15f83dac0a.mp4?token=Dzi1cJ9voS75JGrm-Cm4F3j-RErpYlHR0m_UoN7FufXs74rEhUYZxGqBa4Ohp6F5iTPidy0GNNDP4X6FWQ1snUcYaQttr8lhuBHJsoTBxsXnOWOlydKl8gyQkmlhPACQIDogNRCu9S6opRGLRgpQWzFQ7RGj46X8jvS02Nw9_k5Rr_HmcSdcv_JXXH-9qc-7axiK8tzfa82wZte7StkwGqU5Vjzz2hUUsiaeVCqiP8g7xmph3R5098oKX_q-5bwjOTU2BIpk31hlrNanLf3Tl0VFkiDJ-nfy9Bitkj4PKK4oQVnKQu_vpZE2lkqVeYvkWvMFhYNjB4-ABAEh2-Oucg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ زرد: باز کردن چاه‌های نفت دریای شمال بریتانیا را ثروتمند می‌کند
‏
🔹
ترامپ جنایتکار در پاسخ به گزارشگری که درباره توانایی آندی برنهام، نخست‌وزیر جدید برای رهبری بریتانیا پرسیده بود، از تصمیم او برای گشایش نفت دریای شمال تمجید کرد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/676495" target="_blank">📅 23:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676494">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a062f9cc.mp4?token=KRV-QNuQRdukYSHUWIpsvdriBUckijCkr9AfwIUZ-cVLFt6knKdHXj7mtQP9crhlVKNXunxpi_mAAeiRRCXGQbPahiZm3KLAqZ6gGfjXspF-mtxo0-lFAaz-Kjn9C93iWJ4kwuviqxO5DL93S5q-2VywwB7Ua4SCUfJGUu5-9JVwto41jLW_4x-ah5Ncl5kFGlDiGgJ-N2oCUI0mucZ-kxQvCUKyvG-T-yXmdNlGMHlK8YXwvZ-S-F-IRD77FC5mQ2HqDE4VQDMvzgNjs8j2D_laQVE6h8q9YWOQWaZbyesfy4FGz363GpyMLy2gOtat63_9z3DzCTlg7F1tTepzVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a062f9cc.mp4?token=KRV-QNuQRdukYSHUWIpsvdriBUckijCkr9AfwIUZ-cVLFt6knKdHXj7mtQP9crhlVKNXunxpi_mAAeiRRCXGQbPahiZm3KLAqZ6gGfjXspF-mtxo0-lFAaz-Kjn9C93iWJ4kwuviqxO5DL93S5q-2VywwB7Ua4SCUfJGUu5-9JVwto41jLW_4x-ah5Ncl5kFGlDiGgJ-N2oCUI0mucZ-kxQvCUKyvG-T-yXmdNlGMHlK8YXwvZ-S-F-IRD77FC5mQ2HqDE4VQDMvzgNjs8j2D_laQVE6h8q9YWOQWaZbyesfy4FGz363GpyMLy2gOtat63_9z3DzCTlg7F1tTepzVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
قبل از حرکت، مسیرت را هوشمندانه انتخاب کن
🔹
در سفر اربعین، انتخاب مسیر مناسب می‌تواند زمان سفر را کاهش دهد، از ترافیک و ازدحام جلوگیری کند و سفری ایمن‌تر و آرام‌تر برای شما رقم بزند.
🔹
با مراجعه به سامانه ۱۴۱، مسیرهای مختلف را بر اساس آخرین وضعیت تردد، ترافیک و شرایط جاده‌ها مقایسه کنید و با آگاهی بیشتر، بهترین مسیر را برای رسیدن به مرز انتخاب کنید.
🔹
برای اینکه بهترین مسیر را انتخاب کنی، بیا ۱۴۱
#چشم_به_راهیم
#اربعین
#سامانه141
#انتخاب_بهترین_مسیر
#سفر_ایمن
#مدیریت_سفر
#سازمان_راهداری_و_حمل_ونقل_جاده_ای
#حمل_ونقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/676494" target="_blank">📅 23:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
سگ زرد درباره حادثه در مصر: از این حادثه مطلع شدم. این مثل سایر موارد است. در این شرایط، ما ایران را به شدت تحریم خواهیم کرد. آنها می‌دانند که این عواقب اعمالشان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/676493" target="_blank">📅 23:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676492">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
احراز سن کاربران شبکه‌های اجتماعی از سال ۲۰۲۷ در نیویورک اجباری می‌شود
🔹
از ژانویه ۲۰۲۷، احراز سن برای دسترسی به فیدهای الگوریتمی (مثل اینستاگرام و تیک‌تاک) و نوتیفیکیشن‌های شبانه در نیویورک اجباری می‌شود.
🔹
متخلفان تا ۵۰۰۰ دلار جریمه خواهند شد و کاربران زیر ۱۸ سال نیاز به رضایت والدین دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/676492" target="_blank">📅 23:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676491">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
استخدام در آموزش و پرورش برای امسال منتفی شد
محمدرضا احمدی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
امسال جذب نیرو از طریق ماده ۲۸ انجام نخواهد شد. توجه به کمبود معلم، پیشنهادی مطرح شده تا نیروهای نهضتی، پیش‌دبستانی و خدماتی به‌عنوان نیروی شرکتی جذب آموزش و پرورش شوند تا دانش‌آموزان در سال تحصیلی جدید بدون معلم نمانند.
🔹
همچنین پیشنهاد شده دانشجو معلمان سال آخر تحصیل بتوانند با طی فرآیند ارزیابی و آزمون عملی یا تئوری، در مدارس تدریس کنند تا هم تجربه عملی کسب کنند و هم بخشی از کمبود معلم جبران شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/676491" target="_blank">📅 23:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676490">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
تشکر راحله امینیان، مجری صداوسیما از مردم عراق برای بدرقه باشکوه رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/676490" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676489">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
فرمانده مرزبانی استان بوشهر از توقیف چهار فروند شناور با محموله کالاهای قاچاق خبر داد و گفت:ارزش ریالی این محموله برابر اعلام کارشناسان، ۲۰۳ میلیارد ریال برآورد شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/676489" target="_blank">📅 23:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سگ زرد درباره حادثه در مصر: از این حادثه مطلع شدم. این مثل سایر موارد است. در این شرایط، ما ایران را به شدت تحریم خواهیم کرد. آنها می‌دانند که این عواقب اعمالشان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/676487" target="_blank">📅 22:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d107593ce.mp4?token=ZSHh94jN_zTk7-LFZ9SxvLG5KKBNOsU4wCRWP5zJWRZ0WNFkuk17DiYSqxPbt9kp0U-gJuwEZJw16xJqXWRlQIjm0hX7vGETI120Vj0qb4EPvObaVrdLPjBxtKb-ApXOCwgVlPt3bsPq3I_EmFgekcKiS2OHN-s0tFDZLnf_LSzGup3DLuChSubtLjpV3xBtUv5AjVHtUC3WOBj4rsYokR_bVxjOHd2Dgd_us6arkmFGVCgceQ2cYRy0kd-CR7zLp1K-LXp1nKoI7zYorUKV631vcVWmvzCtKpVlxcsWpy7rFX9W7PX3BCmIdRyXw9ZuVlK9ees9tnvshcu3RuGYzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d107593ce.mp4?token=ZSHh94jN_zTk7-LFZ9SxvLG5KKBNOsU4wCRWP5zJWRZ0WNFkuk17DiYSqxPbt9kp0U-gJuwEZJw16xJqXWRlQIjm0hX7vGETI120Vj0qb4EPvObaVrdLPjBxtKb-ApXOCwgVlPt3bsPq3I_EmFgekcKiS2OHN-s0tFDZLnf_LSzGup3DLuChSubtLjpV3xBtUv5AjVHtUC3WOBj4rsYokR_bVxjOHd2Dgd_us6arkmFGVCgceQ2cYRy0kd-CR7zLp1K-LXp1nKoI7zYorUKV631vcVWmvzCtKpVlxcsWpy7rFX9W7PX3BCmIdRyXw9ZuVlK9ees9tnvshcu3RuGYzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراسم بدرقه زوار حسینی در میدان آزادی تهران برگزار می‌شود
🔹
آیین بدرقه زائران اربعین، روز پنجشنبه با حضور خانواده‌های تهرانی به ویژه نوجوانان زائر از میدان آزادی تهران در قالب برنامه «محرم شهر» برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/676486" target="_blank">📅 22:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستان مشهد: قاتلان ۲ بسیجی مشهدی دستگیر شدند.
🔹
فدرال رزرو آمریکا نرخ بهره را بین ۳.۵ تا ۳.۷۵ درصد ثابت نگه داشت.
🔹
شبکه CNN: وزیر دفاع عربستان سعودی امروز در واشنگتن با ترامپ و ونس، دیدار کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/676485" target="_blank">📅 22:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7db80720e.mp4?token=nkGz5_WdbrmoZwpMY7ePXZklVMUKfE8tCNNMmVTDbok58aI5oFiNt6xLKQbZ1LydG_h1tXkoh5e-4pbQWb-upr6c3mbNymIoFPAFlx98PD3bookDB7crpNs00ZutGWC37i8OmmB9_9MgNutI6r1TPoBOH-OxqxhZybYgg4-lewajYyIBDwXi-fyTXnpc4-bGbkEXZDEGKq397BE1EqGZQyCR20mmKKfvdI5anGjUnz9sAngvn29OlUVMvBvnqbsidbPaKwfWlKoU4A2tL_vv0eKWxBxpaAZ-fknCobP-Ku4KeYgiHAu-BGTcMbF3vI1pTSUwZdjNXBWNS0FfKdLPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7db80720e.mp4?token=nkGz5_WdbrmoZwpMY7ePXZklVMUKfE8tCNNMmVTDbok58aI5oFiNt6xLKQbZ1LydG_h1tXkoh5e-4pbQWb-upr6c3mbNymIoFPAFlx98PD3bookDB7crpNs00ZutGWC37i8OmmB9_9MgNutI6r1TPoBOH-OxqxhZybYgg4-lewajYyIBDwXi-fyTXnpc4-bGbkEXZDEGKq397BE1EqGZQyCR20mmKKfvdI5anGjUnz9sAngvn29OlUVMvBvnqbsidbPaKwfWlKoU4A2tL_vv0eKWxBxpaAZ-fknCobP-Ku4KeYgiHAu-BGTcMbF3vI1pTSUwZdjNXBWNS0FfKdLPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سه انفجار متوالی در سلیمانیه عراق
🔹
انفجارهای شدیدی دوباره در منطقه رانیه، واقع در استان سلیمانیه در شمال عراق، رخ داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/676484" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XU5MQprNCQ7eysYQwFUD359S9ESZuEQ7zrNpehurnxZm7oIt-eEd50eLeVovWPwTwQ92Uh2RHDqVu1yC9EUTNLgPrSGBmJq5pV-1fDxyHbIm-UQ7KQILigitBmOD2PTPHczGqmIikajWDsE6_HS2vbmQF4Eq8NZaJXlpT4t3icDFcov8U2M-SzqcyA5PcmefhsZP1zU8MXpuCodti7SdDaynGLLENhmccqI1ZRYtoN62SHv9pmfFRvY09UWn2VRP8Udp5lV__FT_q7ucBj_fSGb5UgWgPidl0amyigwVayzX3wf1EsYitUbWf-nbyg7XXH1-S-MnmrfXFa4WXMJYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ شبه جهانی
🔹
تنش‌های میان ایران و آمریکا وارد مرحله‌ای شده که ابعاد آن از یک تقابل دوجانبه فراتر رفته و به یک بحران منطقه ای تبدیل شده است. در تازه‌ترین تحولات نیروهای آمریکایی و عربستانی عملیاتی خباثت گونه را در عراق انجام دادند درگیری های یمن و عربستان همچنان ادامه دارد و همزمان تنش ها در جبهه های دیگر نیز رو به افزایش است. از حمله اوکراین به یک کشتی ایرانی با ادعای حمل تجهیزات نظامی گرفته تا حملات متقابل ایران به خاک اردن و مقر نیروهای آمریکایی همگی نشان می دهد دامنه این رویارویی در حال گسترش است. در این میان اسرائیل نیز همچنان به عنوان یکی از بازیگران اصلی این بحران دسیسه چینی میکند.
🔹
هشتصدوبیست‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/676483" target="_blank">📅 22:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
الجزیره: نقشه‌ای که نتانیاهو برای ایران کشیده بود افشا شد
ادعای الجزیره:
🔹
جزئیات جدیدی در حال آشکار شدن است که نشان می‌دهد مقامات آمریکا و اسرائیل چگونه معتقد بودند جنگ علیه ایران سرراست و کوتاه‌مدت خواهد بود.
🔹
مگی هابرمن، خبرنگار آمریکایی می‌گوید بنیامین نتانیاهو سناریوهای تغییر حکومت را به دونالد ترامپ ارائه کرده بود. لیندسی گراهام یک جدول زمانی چند هفته‌ای را برنامه‌ریزی کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/676482" target="_blank">📅 22:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676479">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رزاقی: بنادر عمان دست اروپاست، اروپا هم ایران را تحریم کرده
جمال رزاقی، رئیس اتاق بازرگانی ایران و عمان در
#گفتگو
با خبرفوری:
🔹
عمان بنادر بسیار خوبی دارد ولی این بنادر در دست اروپایی‌هاست و به علت تحریم نمی‌توانیم در این بنادر کار کنیم.
🔹
در طول جنگ عمان چهار بندرش را به تجارت با ایران اختصاص داد. منتهی تمام این چهار بندر روی هم نمی‌توانند مانند بندر جبل علی امارات عمل کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/676479" target="_blank">📅 22:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676478">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390179d40a.mp4?token=oNIKzwWmDOMjDFlZDWOU2FpAv4HfmMQUbkJNuctQEQhZn2XTMjLmTAjKsZUHRZrv581YnDYJcS21Ps8ANpJNRsPVYgQIdsIAbmLt7J9xEGa3eap7yEigL1-luNKyJQDldn4yYHpXpa9TMHiqlQfE94ILsgGjBwfGGvAiTI6xMaihCUb5S_exYZZR2t1iAyEJuaOsb-acJzlz71ebQGjRqlLc6huqKG82pVTEOXg1ZfUjRz-pb0CEW1xXNUu0s0OZ3tTehIwHkWHvK4ABCL71arDXsR3N4OnUmHEeqm-MOuQNzFGVQ_BRZjQq3sdMAqKmd969JKr2sWBukRqJpeSHhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390179d40a.mp4?token=oNIKzwWmDOMjDFlZDWOU2FpAv4HfmMQUbkJNuctQEQhZn2XTMjLmTAjKsZUHRZrv581YnDYJcS21Ps8ANpJNRsPVYgQIdsIAbmLt7J9xEGa3eap7yEigL1-luNKyJQDldn4yYHpXpa9TMHiqlQfE94ILsgGjBwfGGvAiTI6xMaihCUb5S_exYZZR2t1iAyEJuaOsb-acJzlz71ebQGjRqlLc6huqKG82pVTEOXg1ZfUjRz-pb0CEW1xXNUu0s0OZ3tTehIwHkWHvK4ABCL71arDXsR3N4OnUmHEeqm-MOuQNzFGVQ_BRZjQq3sdMAqKmd969JKr2sWBukRqJpeSHhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی جنگلی به ترکیه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/676478" target="_blank">📅 22:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676477">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d69eea63.mp4?token=WFIaAlcyWJeoZp-UJOQDA4GiR_SaegF-t2jLHOhb5Od7X6hpRXThkFXqh-D370Y6Vlqcu17g5r0iEXGz5VC_IH95HHX7Iurtgmo_sTrhH85OoCp8Olg_hhVmJ6KYaftTmNft-yIWqieEnFa4ZIi_mskVX7LWb3oSLfGclJE31Dgu9sCQNDvHaq-gPXzRRLglvOVK9SKfRHR2h5wNJ9FvzYyrKQTwLLxMnN7ZUSCq3c5aHbAqQj-XLSgaknn1dd8kjpeNUj7xIGqw2pmCCQFPl03GrN_AVfcqTrg-_2O3Wtl3Dj442xjopp5GLI6vtPCi76HvpTBPB46YvVU7R3ogVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d69eea63.mp4?token=WFIaAlcyWJeoZp-UJOQDA4GiR_SaegF-t2jLHOhb5Od7X6hpRXThkFXqh-D370Y6Vlqcu17g5r0iEXGz5VC_IH95HHX7Iurtgmo_sTrhH85OoCp8Olg_hhVmJ6KYaftTmNft-yIWqieEnFa4ZIi_mskVX7LWb3oSLfGclJE31Dgu9sCQNDvHaq-gPXzRRLglvOVK9SKfRHR2h5wNJ9FvzYyrKQTwLLxMnN7ZUSCq3c5aHbAqQj-XLSgaknn1dd8kjpeNUj7xIGqw2pmCCQFPl03GrN_AVfcqTrg-_2O3Wtl3Dj442xjopp5GLI6vtPCi76HvpTBPB46YvVU7R3ogVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار مهم پلیس فتا که حتما باید آن را جدی گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/676477" target="_blank">📅 22:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676476">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سه انفجار متوالی در سلیمانیه عراق
🔹
انفجارهای شدیدی دوباره در منطقه رانیه، واقع در استان سلیمانیه در شمال عراق، رخ داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/676476" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676474">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEECa18z9zSeLmYi484mMffhL9eGL9bGJAhV1CzmW9gXyG-BqO_gzkd8xhUBbQXUWmEXwpuw2KOhNz1vcW56LChSfCubfOqTBthuhybAcSTuK1falM1Nr-aQsNzI0gRZorptFx4R4GjDfSYxxG62vXlWehC69eoYSF5_ehN0Iicu6JCXg58rTzAPBe0zJXvI7hp4xIwEPQvQk4il3uorwDgFOy9QZnlTEYS0Y5jyhFK8WqtBj1zyGZ-BI-OQgFAVfVKkljKSzWTCHdaBCF_FrAw0P_UShWCROmgJzxQLWZ7aAeGrR0Xvl8FIaReQg-xTyKGiEpifu-66gXbOuw2Uxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
آخرین اخبار اربعین را از «چشم به راهیم» دنبال کنید
🔹
در ایام اربعین، اطلاع از آخرین وضعیت جاده‌ها، مرزها و تردد می‌تونه مسیر سفرت رو سریع‌تر، ایمن‌تر و بدون دردسر کنه. آگاهی، بهترین همسفر شماست.
◽️
به‌روزترین اطلاعات از:
🟡
وضعیت لحظه‌ای محورهای منتهی به مرزها
🟡
خدمات و امکانات مجتمع‌های رفاهی بین‌راهی
🟡
هشدارها و توصیه‌های ایمنی سازمان راهداری و حمل‌ونقل جاده‌ای
🔔
همین حالا به «چشم به راهیم» بپیوندید و با اطلاعات دقیق، سفری ایمن و آرام را تجربه کنید.
✅️
@Cheshm_Be_Rahim
✅️
@Cheshm_Be_Rahim
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/676474" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676473">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoFF0Di7J9JHo8jRDwcCnTRLp79pAv_vuf4wx68r46szlG99YY5gbT5HvH1f_EoqLcgUZiqpzMcIWXPM9x7VRJb6GOSzDR9BrGnYAEIiEIzfulnuS3fCbt49Vo3ubPktW-6M_2clYOwDvETkd4jTYwKN-KCHfhkyVFM9c7y7daEHvMaBwIqWHXgYNHRpXhuGr5TU_dHDKs372s0kkOqyMftMi23zAKBzk3gIDMuWXLsOtUvQcvO8b6uTQKR3fiNTdofdhIKvdofjT3mF5ZUJalmuv4bJsEk2PX1QTyj1JdbhdVxrStQbS0QOn8KD8DiovwbvSj7nMi0hVvaMffo3xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر چهار شهید ایرانی در پی حمله مشترک عربستان سعودی و آمریکا به استان کربلای معلی در عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/676473" target="_blank">📅 22:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676472">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
شوک قیمتی؛ بازار قهوه انفجاری شد
🔹
بازار جهانی قهوه این روزها رفتاری کم‌سابقه از خود نشان داده و به شدت صعودی شده است. پس از اعلام وقوع پدیده ال‌نینو، قیمت قراردادهای آتی قهوه عربیکا حدود ۲۷ درصد جهش کرد.
🔹
افزایشی که با نگرانی از کاهش تولید در برزیل، بزرگ‌ترین تولیدکننده قهوه جهان، آغاز شد. شاخص نوسان بازار قهوه حالا به بالاترین سطح خود در ۲۶ سال اخیر رسیده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/676472" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676471">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d599cd43c2.mp4?token=veKpl6XqR9haMtKoZz1upD4sLJnkaed-nEvqRsZxtXwp8Wv9BE-eSbk6PK9qT2WJsi_VnknoBQnBQ-ThcZIi92NAcvChn5mxRYRSzOnxE3RnckERsAuSqIuzLPG4ElX2V4KYja28XqVrCpdz5IE-q288YM-0PTTZCUYaQJw0wc2KYXMyrxBp2A0pY0wYR70EHO2_g8ESl9ehED-fXt8EsqhgVVOQX_BE274Prhnz_EAZ4BQ4FwY7STe1wPOPkwCf1K21RmWCIfXgS5rBI93K63G3b6jfdnspQFtoNtMfwcYFP-LubXpyrKuUVxXIIZ89--zLKtVLmFZPI--jz9TJHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d599cd43c2.mp4?token=veKpl6XqR9haMtKoZz1upD4sLJnkaed-nEvqRsZxtXwp8Wv9BE-eSbk6PK9qT2WJsi_VnknoBQnBQ-ThcZIi92NAcvChn5mxRYRSzOnxE3RnckERsAuSqIuzLPG4ElX2V4KYja28XqVrCpdz5IE-q288YM-0PTTZCUYaQJw0wc2KYXMyrxBp2A0pY0wYR70EHO2_g8ESl9ehED-fXt8EsqhgVVOQX_BE274Prhnz_EAZ4BQ4FwY7STe1wPOPkwCf1K21RmWCIfXgS5rBI93K63G3b6jfdnspQFtoNtMfwcYFP-LubXpyrKuUVxXIIZ89--zLKtVLmFZPI--jz9TJHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، سرزمین قهرمانانی که شجاعت را نه در حرف، بلکه در نجات جان انسان‌ها معنا می‌کنند #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/676471" target="_blank">📅 22:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676470">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نمایندگان مجلس در پی زنده کردن R&D در ایران
رمضان رحیمی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
طرح جدیدی برای ساماندهی کارآموزی دانشجویان داریم که با باز شدن مجلس آن را پیگیری خواهیم کرد. ما می خواهیم R&D را در ایران زنده کنیم و رابطه صنعت و دانشگاه را بهبود بخشیم.
🔹
منابع مالی برای حمایت از دانشجویان شرکت کننده در طرح در نظر گرفته شده و صنایعی که در این طرح شرکت کنند از معافیت‌های مالیاتی برخوردار خواهند شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/676470" target="_blank">📅 22:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676468">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
کمک فوری برای درمان کودک 4 ساله ای که سرطان دارد
🔹
کودکی ست 4 ساله ، چند ماه است به سرطان خون مبتلا شده است ، چند جلسه شیمی درمانی انجام داده ، ماهانه حدود ده روز باید در بیمارستان بستری شود که حدود 15 الی 30 میلیون دارو احتیاج دارد.با کمک اقوام تا الان توانسته اند دارو ها را تهیه کنند. اما به دلیل گران بودن داروها و برای ادامه درمان و اینکه این بیماری طول دوره دارد نیاز فوری به کمک مالی دارند.
هموطنان عزیز این کودک بیمار برای بهبود در انتظار کمک های شماست.
🔹
مورد دوم: مادری ست بی سرپرست دو دختر مجرد دارد و وضعیت مالی خوبی ندارند.دو سال است به سرطان روده مبتلا شده ، پدر در حال درمان است.مدتی پیش عمل فتق و صفرا انجام داده و هزینه عمل بیش از100میلیون تومان بوده که با قرض از اقوام توانسته آن را پرداخت کند ایشان برای درمان سرطان باید دارو مصرف کند.
✔
پرداخت انلاین خیریه نسیم وصال:
http://www.nasimevesal.ir/payment-new
شماره کارت بانک ملت : ۶۱۰۴۳۳۷۸۱۱۴۱۶۲۳۷
شماره حساب بانک ملت: ۵۸۹۸۷۷۱۴۶۵
شماره کارت بانک ملی: 6037997599156198
شماره حساب بانک ملی: 0219934010000
شماره شبا: IR310120020000005898771465</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/676468" target="_blank">📅 22:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676466">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: راه شهدای اقتدار با اراده راسخ رزمندگان و خادمان صنعت دفاعی ادامه خواهد یافت
سردار ابن‌الرضا:
🔹
بازگشت پیکر مطهر شهید والامقام امیر سرتیپ‌دوم خلبان مجید کاظمی پس از ماه‌ها چشم انتظاری، روایتی نام آشنا و کهن فرزندان ایرانی است که عهد خود با ایران، اسلام و مردم را تا واپسین لحظه حیات حفظ کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/676466" target="_blank">📅 21:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676464">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0vQoBfUsb214t5OuHawe2z0H2WMWbPTjn_alYyLFBQw_hGXu16Yb_WIGhOwKSWzvYtU_jIs2H5zMrhm0bls_qLWFme62Kjjfcl0JmMWLyhA-rP86CMWf0w8DK1vAJ_uyEUDfKjz4e50BYSvJGaFhmwT09YISkq1ddtlNC9dMGUU3n4wIadJBwEkkgrjfy8nPzEhK-pDILBVqs_v9lxQ_CY6HVKK3A8h2Gxu2DqJverV4bRKaGFS1hJfeXFc4p6nokcRzU4upzgjQi0AW0ODnCHUklABeqUFBGnYIpdc4j2jh6tLmuVf-I8Bn0C2jEruDz2TqtiMCX2FCdro5wpnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۵.۳ درصد ایرانیان کاربر اینترنت هستند
🔹
روند ۳۰ ساله استفاده از اینترنت در ایران نشان می‌دهد ضریب نفوذ اینترنت از ۴.۶ درصد در ابتدای دهه ۸۰ به ۸۵.۳ درصد در سال ۱۴۰۳ رسیده است.
🔹
این روند افزایشی تا حد زیادی قابل انتظار است؛ چراکه هم‌زمان با گسترش زیرساخت‌های ارتباطی و اینترنت همراه، دسترسی به اینترنت در سراسر جهان فراگیرتر شده است.
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/676464" target="_blank">📅 21:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676463">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcFwnmDIu55-_h_CI9y4PA9w4pyjT77pHkQ2Y0FrEVjldEjN35MC10fKrMz9e35ptFhhGQJoelZleij0jfE9s9X3iub2tzMjMSU_-JElySsYA5VdmvJRtgzzXWujkHHDOn472iuWtcvJ3oGHQSufK7JESKpRNSTyW-S0qkcW5MQBu98w9WsBiiHln0AvkNstL-WGMWneTem4SEa14x__msE6yzoGgUG1Pgvj35kcOtryqct0AimxnqFMC1E9LO7oduF_Pea05LTSAqKgikAtz2BVqd9pm9VMSzfEmS8njxlcmvp1zsi6Pv8z_U253Dm_La5PRjoe1ttNvId5HdcSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد بی‌سابقه جستجوی سَم برای کشتن ملانیا
🔹
پس از وایرال شدن ویدیوی جنجالی «ملانیا ترامپ را کجا و چگونه بکشیم» و پیشنهاد استفاده از عامل اعصاب VX در آن، آمار جستجوی این ماده سمی در سطح جهان به بالاترین حد خود رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/676463" target="_blank">📅 21:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676462">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آثار تورمی ارز ترجیحی چگونه تخلیه شد؟/ کاهش تورم ماهانه برای دومین ماه پیاپی
🔹
زمستان سال گذشته بود که با پیشنهاد دولت، هر سه قوه به توافق رسیده‌اند که نظام چند نرخی ارز را حذف کرده و به یک نرخ واحد تبدیل کنند.
🔹
همچنین رهبر شهید انقلاب در ایام حذف ارز ترجیحی فرمودند و هشدار دادند: «درخصوص مسئله حذف ارز ترجیحی که اقدام لازمی هم بود، می‌بایست دلایل این تصمیم به روشنی برای مردم بیان شود»
🔹
اعتماد در گزارشی نوشت: اخیرا انتقاداتی به تیم اقتصادی دولت درباره سیاست‌های ارز ترجیحی مطرح شده و هم زمان با آن، وزارت اقتصاد در پاسخ رسمی به انتقادها تأکید کرد: «فلسفه حذف ارز ترجیحی دقیقاً مقابله با سیاستی بوده که طی سال‌های گذشته نه تنها به هدف کنترل قیمت‌ها دست پیدا نکرد، بلکه خود به یکی از مهم‌ترین بسترهای ایجاد رانت، فساد، قاچاق کالا و توزیع ناعادلانه منابع تبدیل شده بود.»
🔹
این وزارتخانه همچنین به آمارهای رسمی مرکز آمار ایران استناد کرده و روند تورم ماهانه ابتدا از ۷.۹ درصد در دی ماه به ۹.۴ درصد در بهمن‌ماه رسیده اما در اسفندماه با وجود هم‌زمانی با شرایط جنگی، به ۵.۶ درصد کاهش یافت و نتیجه گرفته که اثر مستقیم اصلاح ارز ترجیحی پس از دو ماه تخلیه شده است. البته در اردیبهشت‌ماه به دلیل تشدید آثار جنگ و محدودیت‌های ناشی از محاصره دریایی، دوباره افزایش یافت و به ۸.۸ درصد رسید.
🔹
همچنین آن طور که «عبدالناصر همتی، رئیس‌کل بانک مرکزی» در تازه‌ترین گزارش خود به کمیسیون صنایع و معادن مجلس اعلام کرده است که تورم ماهانه در تیرماه نسبت به ماه قبل تقریباً نصف شده و این موضوع نشان‌دهنده اثربخشی سیاست‌های پولی و مدیریت نقدینگی است. یاداور میشود در خرداد تورم ماهانه بار دیگر کاهش پیدا کرد و به ۵.۹ درصد رسید.
🔹
در روزهای گذشته «حمید رسایی، نماینده مجلس شورای اسلامی» مدعی شده بود که «نرخ تورم ناشی از حذف ارز ترجیحی بسیار و درحال افزایش است» و این البته در تناقض با گزارش های رسمی کشور است. گزارش‌های منتشر شده نشان از کاهش تورم در تیرماه دارد و ادامه روند کاهشی در مردادماه نیز قابل انتظار است./ اعتمادآنلاین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/676462" target="_blank">📅 21:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676458">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
خروج ۲.۲ همتی پول حقیقی از بورس؛ مقصد پول‌ها کجاست؟
🔹
بازار سهام امروز شاهد خروج ۲.۲ همت سرمایه حقیقی بود؛ در حالی که ارزش معاملات خرد به ۲۷ همت رسید. همزمان ۱۹۲ میلیارد تومان سرمایه از صندوق‌های طلا خارج شد و صندوق‌های درآمد ثابت با ورود ۱.۱ همت پول، مقصد اصلی نقدینگی بودند. در پایان معاملات نیز ۵۳ درصد نمادها سبزپوش و ۴۷ درصد منفی بسته شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/676458" target="_blank">📅 21:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676453">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6baeacb7c.mp4?token=X_5f0qQVvxWcVklMPpBmxSlP167K3BMtJJDuXo17J8F-HhfURNDtOjktEZNv-G2eDKWimcX30nsSxRJ22Gc6qjI2Hx4NJnFF-_0yL4dq2jnG1dX9Z1uAYkt5OJKV2j8OQhkPLUyCfe5IX3zKEzJQL04SDK55_zFUKY2TMkwgYgTBJR2cXg2rYYPDkRA02phDbR0g4fZLGvRTapTRLqyF30dzGLGZtJ7ySf5iFCPMBGkKzGOemmC9IweSflPLmqBlA-or-J34TnDGt9to_32BKmPNofbg85l8zGhMaW-3r0OalvLuK6Bwa4yv1Zf-ifQfyr-lYDgONqaw49cChuZZSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6baeacb7c.mp4?token=X_5f0qQVvxWcVklMPpBmxSlP167K3BMtJJDuXo17J8F-HhfURNDtOjktEZNv-G2eDKWimcX30nsSxRJ22Gc6qjI2Hx4NJnFF-_0yL4dq2jnG1dX9Z1uAYkt5OJKV2j8OQhkPLUyCfe5IX3zKEzJQL04SDK55_zFUKY2TMkwgYgTBJR2cXg2rYYPDkRA02phDbR0g4fZLGvRTapTRLqyF30dzGLGZtJ7ySf5iFCPMBGkKzGOemmC9IweSflPLmqBlA-or-J34TnDGt9to_32BKmPNofbg85l8zGhMaW-3r0OalvLuK6Bwa4yv1Zf-ifQfyr-lYDgONqaw49cChuZZSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
پیام‌های صوتی شما در پویش «همه باهم برای ایران» جلوه‌ای از همدلی، مسئولیت‌پذیری و عشق به میهن است؛ روایت‌هایی کوتاه اما پرمعنا از شهرها و لهجه‌های گوناگون ایران که یک پیام مشترک را فریاد می‌زنند: ایران، خانه مشترک همه ماست.
🔹
این صداهای صمیمی نشان می‌دهد که مردم ایران، فارغ از تفاوت‌های قومی و زبانی، در روزهای سخت کنار یکدیگر می‌ایستند
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
#همه_باهم_برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/676453" target="_blank">📅 21:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676452">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud-0QSac3H5BFTBG2ddG8jkVSaZsmQzQghJ3-l4ZziMVnPr6agvIHn2uDfbJtlWwXCZK-phxj7pr9Vi08D1mpjRH-q5iDb926sOm4DlfXvCOIMjlymBSO54rQipmRTM05a74g5S78FM4rtpolXtneYEDAlnt3gn33R5gJWZsYOlsVNq8lDr8MqQw85dzi9iS_Bf_SWxSM23AJQt4I7URYdtAd0xY9Nfxo-ogC3C61YkiJkSSqA4UI1sVK59TGpViWlFe_HhQdiXeFRWyPwiqYppq2kwAd5f2Nuc2OwMpVPMUGUTQiFMMRpRQkIVRSNSIaG86_ItTNuDVLdvgK0VENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع پیکرهای مطهر پنج شهید ایرانی که در حمله شب گذشته آمریکا و عربستان به شهادت رسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/676452" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676450">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112ce0f51e.mp4?token=FBUp-nsdyWosGpa5uI035l8k2o7d-GCpl2t3s3C_HPDxHT2f1aNyLdvBXd0_-VCIOSGrqWHP2fzRJrF67pHUE4oAZsvv7TR1xa8TEr6m61IUKtogqpnd07SUYGl1wkW9ZUeRPHOTso76QHJAWYPJ-bWbJJkzMWkmpjdr7F9T4uXRDtB3l6bmF8ikSRQPGsin8JY4MYRJtl6939pVbKEhxqWfdIvKC8URTqLbSDEQ8fOrekoq_wy9uvzEyMECoIHdQIlGq-nZsx9UiHzaXQx6b7_Kue4fwNObTGIIyK9yqNPdvrfPLZUq4VuTqNVqS3kc3htLJJkdwMeSrZwpdT784CG-xgo1z_bUMy4K4Zdxt1j6tM8-1YyIyIvPXrU2iPb-ukGSeQrgWysMlsYryVppL6KwXkA6R4suctJf8aimttlVTiKD89M0QTvjgaApxsV6x8p4ToGXVn8LWgn53enjNXSLVxtOOSZrBYAslwPWjav-92nS28Kt3KZarVwoofI1u7wbdhEOYZm_4iqaYh_sITMMY-Fz-9ObEDb5DWEaBXtn4euF1PEhNAiuZXDDjbhEQwsA04GY6YawRYfPsdwYuENElzwF_ogwYmwZ-RS68senuNslV-e7hkvO5NRqJ4_DOmZm7B2NMRanlRM9tsdq56NyNG9q-Qj-3kjqtmI-Fok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112ce0f51e.mp4?token=FBUp-nsdyWosGpa5uI035l8k2o7d-GCpl2t3s3C_HPDxHT2f1aNyLdvBXd0_-VCIOSGrqWHP2fzRJrF67pHUE4oAZsvv7TR1xa8TEr6m61IUKtogqpnd07SUYGl1wkW9ZUeRPHOTso76QHJAWYPJ-bWbJJkzMWkmpjdr7F9T4uXRDtB3l6bmF8ikSRQPGsin8JY4MYRJtl6939pVbKEhxqWfdIvKC8URTqLbSDEQ8fOrekoq_wy9uvzEyMECoIHdQIlGq-nZsx9UiHzaXQx6b7_Kue4fwNObTGIIyK9yqNPdvrfPLZUq4VuTqNVqS3kc3htLJJkdwMeSrZwpdT784CG-xgo1z_bUMy4K4Zdxt1j6tM8-1YyIyIvPXrU2iPb-ukGSeQrgWysMlsYryVppL6KwXkA6R4suctJf8aimttlVTiKD89M0QTvjgaApxsV6x8p4ToGXVn8LWgn53enjNXSLVxtOOSZrBYAslwPWjav-92nS28Kt3KZarVwoofI1u7wbdhEOYZm_4iqaYh_sITMMY-Fz-9ObEDb5DWEaBXtn4euF1PEhNAiuZXDDjbhEQwsA04GY6YawRYfPsdwYuENElzwF_ogwYmwZ-RS68senuNslV-e7hkvO5NRqJ4_DOmZm7B2NMRanlRM9tsdq56NyNG9q-Qj-3kjqtmI-Fok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات ضرباتِ ویرانگر ایران بر پایگاه دشمن آمریکایی در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/676450" target="_blank">📅 21:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676448">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e12a6efbc.mp4?token=dVHc0paLSfeW2Vti_M-BJFZt_jGAq8A2vyMKVAzveH5DWSkWVZHTpf16cKbKcvxgMYPM7l8zqDpj84_OSKozfvtM9Hag8oK3UawvXO2wKqyEdrmps6asB0EFIAcKz1Pz8lDs3rWPLhbWJQm6qmLarW3ZLC4FQxr70S_I4yVNa3ZxlLkOhLrG9evgbTBDJJsl7aJ34wJdQ8-hP_3N-xF_acXM18xfHLIvILJjMEvhJln7yxQ5Mdb-ltg1zitazOg24RezvLdM_bazaeRLukNEl41Cy341hUNM5ole65qpykiim1pqu4p8OV8BlvhTiNNweUOz4GDlBOLpbRXoAWCr5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e12a6efbc.mp4?token=dVHc0paLSfeW2Vti_M-BJFZt_jGAq8A2vyMKVAzveH5DWSkWVZHTpf16cKbKcvxgMYPM7l8zqDpj84_OSKozfvtM9Hag8oK3UawvXO2wKqyEdrmps6asB0EFIAcKz1Pz8lDs3rWPLhbWJQm6qmLarW3ZLC4FQxr70S_I4yVNa3ZxlLkOhLrG9evgbTBDJJsl7aJ34wJdQ8-hP_3N-xF_acXM18xfHLIvILJjMEvhJln7yxQ5Mdb-ltg1zitazOg24RezvLdM_bazaeRLukNEl41Cy341hUNM5ole65qpykiim1pqu4p8OV8BlvhTiNNweUOz4GDlBOLpbRXoAWCr5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک
سنجاب مسابقه بیسبال را به هم ریخت
🔹
این سنجاب از اواخر اینینگ ششم وارد زمین شد و با فرارهای پیاپی، بیش از ۱۰ نفر از عوامل اجرایی ورزشگاه را برای دقایقی سرگردان کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/676448" target="_blank">📅 21:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676447">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02937f3d0b.mp4?token=N1Ps4DAAnFwoipMUc2SQ6M8-EUUjy3eCpCGw8DPmKthScKEg-hHaSBIdTW3UC1TPdmymB1NipHdveQvy_agW58UXOkSKqiHzvHVjzdVBLlE0JPUUABYgnCwmZweK_dpzO71iOms2_8i--raeUwwMduK_MDRMS9RCsNGVmsRgGMK_POSsL1L7MLrLf7Qz6tOjo993mj9yJACgl_4RLlyerYn5r4Q90mk8DFxzNjYApA9aqQs6KSe9XgeFR6wSPXeG7tOOMP7fkI9YNVmKXgQ9ZbPuomdRCSacMaJkiBiKsDl6VKooYjMup1oF1cT5oxOA32y3GjDLTBdMJgb8_6zD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02937f3d0b.mp4?token=N1Ps4DAAnFwoipMUc2SQ6M8-EUUjy3eCpCGw8DPmKthScKEg-hHaSBIdTW3UC1TPdmymB1NipHdveQvy_agW58UXOkSKqiHzvHVjzdVBLlE0JPUUABYgnCwmZweK_dpzO71iOms2_8i--raeUwwMduK_MDRMS9RCsNGVmsRgGMK_POSsL1L7MLrLf7Qz6tOjo993mj9yJACgl_4RLlyerYn5r4Q90mk8DFxzNjYApA9aqQs6KSe9XgeFR6wSPXeG7tOOMP7fkI9YNVmKXgQ9ZbPuomdRCSacMaJkiBiKsDl6VKooYjMup1oF1cT5oxOA32y3GjDLTBdMJgb8_6zD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مازیار لرستانی در مراسم بزرگداشت اکبر عبدی: اکبر عبدی نه‌فقط نابغه کمدی، اسطوره‌ای بود سرشار از صفا و مردمی‌بودن، تکرارشدنی نیست/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/676447" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676446">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ترامپ اعتراف کرد که جنگ با ایران محبوب نیست
ادعای هاف‌پست:
🔹
کیلمید مجری مشهور فاکس‌نیوز در یک پادکست اعتراف کرد که دونالد ترامپ، کاملاً از عدم محبوبیت جنگ  علیه ایران آگاه است.
♦️
رئیس جمهور گفته است که سایر کشورهای خلیج فارس «در حال حاضر از یک حمله بزرگ هیجان‌زده نیستند.»/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/676446" target="_blank">📅 21:02 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
