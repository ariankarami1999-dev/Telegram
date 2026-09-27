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
<img src="https://cdn4.telesco.pe/file/YvpQwkNQREldzQAtgSwaqaxZ0gsUzOaPoWmu8aVjFhNAhG6jP1scntY2wqig8F7UwjOfkCYu4CWvT_ImlWIy4P0wBIyBEEPSJ7aaTLL4XeWpEkypondiyRLSad2zLp4Ybhab23pmJRNZLf_s17lF7O5xKLepyiBthM-4yI0FqDNNwqVYGR5tdcs1whQNnJiqgdV2PKpxYbJ6oPf02PvGzosiv7RzHoOCJ0Lhjhry5Fu0qBCDXWOm0wX2CyL6SyAY23bK9imliDliotoDSo00Kq1awxipRiTfpGM2xyVqBjUcpPsHK-R2Qj5ILeh4KReqmpm01_7htFFE0bVrFcPJUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-149703">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c70d8cb102.mp4?token=L7FliKasY9gJTk4ny3ieTSYWoHJ_f3PWfXopjQlasBlO7uGBis5Pp89bfGph1CMRnTWrzqwKO-pw-flnwmNlisMDc2P_HevPXD49bSlpTvaX8Izq4zFnEqIyAQlflJGmVXpiHdaGi91hbgcCnDBMrmMNI6asNCUmUmKgdv5lMZwG_LGf9Cj-COBBYnh9HiD3bk_Ic4-2Iklf8HNAhiDrvde3_SYL6VwwAc689_EYXMo_1H5Tq8jyKAvbpj_a6o7WtBxQXx3en51LT7209vE0oc7C4sPrkabxJivr-Qtecx1oHnEZoV4jELwv_GiI4wDMRi8kh_VIFGJHt-tqSVCj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c70d8cb102.mp4?token=L7FliKasY9gJTk4ny3ieTSYWoHJ_f3PWfXopjQlasBlO7uGBis5Pp89bfGph1CMRnTWrzqwKO-pw-flnwmNlisMDc2P_HevPXD49bSlpTvaX8Izq4zFnEqIyAQlflJGmVXpiHdaGi91hbgcCnDBMrmMNI6asNCUmUmKgdv5lMZwG_LGf9Cj-COBBYnh9HiD3bk_Ic4-2Iklf8HNAhiDrvde3_SYL6VwwAc689_EYXMo_1H5Tq8jyKAvbpj_a6o7WtBxQXx3en51LT7209vE0oc7C4sPrkabxJivr-Qtecx1oHnEZoV4jELwv_GiI4wDMRi8kh_VIFGJHt-tqSVCj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
قیمت نفت اکنون پایین‌تر از دوران دولت بایدن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/149703" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149702">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c275c1a77.mp4?token=TghLUHKK-thw-V88UL2zsuw7Y07qaqEwo0gUaP7Lp4plGL23qqaijgRk-kqry_BkjZD3iuD90mIwLAmm_9T0ib5JEZmD0hH0Ftbst4bUM7uCvboTEL-jnGLstcWlUkvPyF2YNmF0x0B-loDSfIcYPIqlaQaABlQveGFfq_79JQGjST8vDP6VaO91DGFk-QafiCphWK8E8DjmpSPFgUPisbYlZ10GkUZJCjlXF9b0er8TRfg7wVo9QbgoVgVsyLbo9uvlngvA3NxjbVFzruGlDwMiaKaDRurW4KsehAAvJRW5DJgmhuXmXVl-Q7R3a9xjKHUCNYx9_QUesr1jEVZWzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c275c1a77.mp4?token=TghLUHKK-thw-V88UL2zsuw7Y07qaqEwo0gUaP7Lp4plGL23qqaijgRk-kqry_BkjZD3iuD90mIwLAmm_9T0ib5JEZmD0hH0Ftbst4bUM7uCvboTEL-jnGLstcWlUkvPyF2YNmF0x0B-loDSfIcYPIqlaQaABlQveGFfq_79JQGjST8vDP6VaO91DGFk-QafiCphWK8E8DjmpSPFgUPisbYlZ10GkUZJCjlXF9b0er8TRfg7wVo9QbgoVgVsyLbo9uvlngvA3NxjbVFzruGlDwMiaKaDRurW4KsehAAvJRW5DJgmhuXmXVl-Q7R3a9xjKHUCNYx9_QUesr1jEVZWzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
شب گذشته، رکورد تازه‌ای در انتقال نفت از تنگه هرمز ثبت کردیم؛ حتی بیشتر از میزان نفتی که پیش از آغاز جنگ از این مسیر عبور می‌دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/149702" target="_blank">📅 16:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149701">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=fGXNba4QZk2H6y-k3nuYW4fCAfdeQWaivTxIhhpK5B5j6kPAv4LnP74qv4bCKjWBluFmXqk6TBa_OFeRkJsiPQxUftGptg_VLuds1ELQBK_LdFp8kOCKQ4N52FbyxMXNvOQ57d5oBG-KTgx_pw7_ecKh9Hhrp3_tDe81s4Ev3o_-Q3bckpGpHdbOIiXj6RC47o9PF6rhCpNGrCozUG_L2qpFwe00-r6FxMaZ2jroiA9PnE1kMjr7XBrBE7GdrpKSsiX9vCZy0BYpCWZRcUL8dNKdtc6nf7ieVp4vKwtbstz_2omLXC1GK8mOXjA1YyVHs7ZwQgyLA4hA8XKHx1sjew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=fGXNba4QZk2H6y-k3nuYW4fCAfdeQWaivTxIhhpK5B5j6kPAv4LnP74qv4bCKjWBluFmXqk6TBa_OFeRkJsiPQxUftGptg_VLuds1ELQBK_LdFp8kOCKQ4N52FbyxMXNvOQ57d5oBG-KTgx_pw7_ecKh9Hhrp3_tDe81s4Ev3o_-Q3bckpGpHdbOIiXj6RC47o9PF6rhCpNGrCozUG_L2qpFwe00-r6FxMaZ2jroiA9PnE1kMjr7XBrBE7GdrpKSsiX9vCZy0BYpCWZRcUL8dNKdtc6nf7ieVp4vKwtbstz_2omLXC1GK8mOXjA1YyVHs7ZwQgyLA4hA8XKHx1sjew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
به محض اینکه ایران تسلیم شود، به محض اینکه جنگ به پایان برسد، که این اتفاق به زودی خواهد افتاد، قیمت نفت به شدت کاهش خواهد یافت.
قیمت نفت به طور چشمگیری کاهش خواهد یافت و تمام قیمت‌ها پایین خواهند آمد، اما قیمت مواد غذایی به میزان قابل توجهی از زمان ریاست جمهوری بایدن کاهش یافته است. تقریباً تمام قیمت‌ها به میزان زیادی کاهش یافته‌اند.
ما حجم بسیار زیادی از نفت را خارج می‌کنیم؛ شب گذشته، ما حجم بی‌سابقه‌ای از نفت را از تنگه هرمز خارج کردیم، بیشتر از زمانی که قبل از جنگ این کار را انجام می‌دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/149701" target="_blank">📅 16:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149700">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tqMsLAudRUn9b1bEriXZAzQ2gGuDP8AMmnnoQW_oaAXGYOhGPGBXrwkiSZy_FZJmtmACgcIWwi7pISYLveiNkf6f9cpJSvPpo-tSlMP5-_TUfYe54fliStXW4rQnBWrz_voaxRXFZbtkI8r72p8Wy_LZoeSv7wsX2GwxVdfzh_qncoMd2fnWAGRU7PC2-QAkJBCTlTrVOfTi_VkDz-My7_e7MmTXIZV-uBE4PBaNgWEeao_p-euMiI4KRaNh-H_XET5mZaEXfcvnPnNp4vEyP3thoBOTKHYqXaURPQGBIMUn8JSdDm-6pnbJlMFKXkVk7Fqpn-tr7GGN8P3OIhARwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاطمه معتمدآریا بازیگر هم به ایران بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149700" target="_blank">📅 16:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdZiH0ENmW_VNp9lUj5BYY_J3w4SlqAWOeRr9G8IqNV98wCswaO5hbzycyZ59m4VIhwxlHLx34qvmzEowkmGkWnvR7lv3tF2fUML1yEtLFXcYnCjS75SrFemHUZnw-2o8DgN0998Bu6XV3pcmDByNsymMnNn95ZY2iVU_OYm4dYCzDB3Pm2ga-FVyBW10g5-Hr5HFnlu2DLswajZenMlJugOQpwCp_86ShZBvsdyjaEWvXR_0s4xVIlpesVqxhcXuHoRTe_Stp7GA3MBbtuj2PfgBuvR27lw5v7A9mLBBsANPrg_L_CpliRScLoCWO-ncOvEeP16tN_gF0KGNvegIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: هیچ‌وقت در تاریخ آمریکا این‌قدر افراد شاغل نداشته‌ایم
!
🔴
همین حالا افراد بیشتری در آمریکا مشغول به کار هستند تا در هر مقطع دیگری از تاریخ کشورمان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/149699" target="_blank">📅 16:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjzuVFmv4CX0EyAjvDF0DAZaZ8-0Uw6xbZmcJ3NJldv3Nqc82s2syQfwYOo91sD87LTuyGd1AAMKMvPRr3iBVT31l31YmuNtkQF_ZpCloPMQ0DMCnZ832XmSPR9kiaa4iEtpKijY1Cr2InReeeL3PEMfLNRIklrkw5TxpTR7bOdIjpHAh0WxARh5221h2keD1C0TdSHcff8EQJbqkcs6rVa5D5ECoFoari8lrBzLSZLOHCk8ruCt5TudI8Hl99lD_h7EuH-9uKDvifHUkxFo-k_6kBT0yQvYeimZFqGrraiFFUIWLDqTRpzRUVX1SiQZocr3AMNfl95LtX0bURfHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت بیت‌کوین به ۲۰ میلیارد تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/149698" target="_blank">📅 15:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2OG4RqCnEqPms4WZRAOIYkcUlrP15vXKIpquRXjvfqdZB4uvekJ5xqpa5OPj_qMGr2MXkDpulJ9ZgMxAXWFtz6zb2Vj2rrbKRbZXNYCqMh1TI6zWRxE0hy__h_ZqVJ91jTFASfrkJy7BPA72_MRQZ4EkhyJAlspz4jabeb4tYyj0BFA891Nd9kMGXJlxgRAnMRGS53CdvVMHpUnDqJgyz1bgC3F6numH6FaZiG0Y2QWrDaqzood9BgSCErkIPPP4jHUSiOMOO0RdlWtjAKgu3TB4Alw9mYxkroanXFpbbiF9MHunGHtlHiiabId3_p59pli3qLXPYry_XrYPh0Spg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای ثابتی هم پرونده قضایی تشکیل شده و احتمالا بزودی اونم محکوم میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/149697" target="_blank">📅 15:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
طبق گزارش برخی از رسانه های خارجی؛
آمریکا قصد داره با فشار آوردن روی کشورهای پاکستان
🇵🇰
؛ افغانستان
🇦🇫
؛ عراق
🇮🇶
؛ ترکمنستان
🇹🇲
؛ آذربایجان
🇦🇿
و ترکیه
🇹🇷
مرزهای زمینی ایران رو هم محدود کنه و محاصره زمینی هم به محاصره دریایی اضافه بشه.
چون الان ایران با وارد کردن کالا از مرزهای زمینی تونسته دووم بیاره و اگه مرزهای زمینی هم بسته بشه؛ عملا هیچی دیگه وارد نمیشه و به یک زندان بزرگ تبدیل میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/149696" target="_blank">📅 15:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-qF8v4MYsyvhO6MsP_3Vq6omq9Icuh8hZjHjRwgOHJMEnNtRGQeefUexQgXvHfWsmfRb9HtXgCWvWkeSYnqON5tQcPBhTW_dnsnTc0y_DyNjtr9T1qlOdszzaBN1jToQ92Hl8R3JvmjQb7haK_TP9o-LunfotXpX_3Kreey5kZXx1_CCTMMEb-c9x7C-2Cu8tveQaqvmzh-dsn5QGiPxKnQ-BJ-5ByV__0ZSLfusZKW2IuZGOAGFqNVVxKoO4DJ-VsU11dS6KREzJMiTeC-rJgDPjyvj9-FtCSef093E7B4jhlF3-cwpWE5gPGGIaLsXj_GAxuVdGW3upNKfKiEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی بخاطر شکایت قالیباف و چندتا موضوع دیگه تو سال 1402، به 10ماه حبس محکوم شد  #عروس_زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/149695" target="_blank">📅 15:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlBGM6qUkVRDLm4eSgmViEHReaEH_2N8Bs9nCSMKfEXxeHOT_RL00qa51FsGRmODKHO6kx80mRKFRdxSooz8m7B1wv615dYnPQ9i_DEKp4zN6hPcThtdSOdC7X2kOUqVCbrfeHQcQrq3U6Cbk3da9bmHhVydBQtvrBeixcIegcHcVSL0Q3HP6Ayxb7nKR5wQW_z2MHzjWmGx3SasivO39UgG0wWYiN8cK1UcBuPdEa1ZwI1YopSX60Xg3nXhHjEjfc4rR5eWHmUmLpjMv6VLaG9YmMnd0fgh-3NXRy6zGyMCGnPISHCCDosgoJeHnhOmBcTmWYyfbcpGyK91xq9xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامنت وایرال شده از مرضیه حسینی، خبرنگار ایران اینترنشنال در کنگره آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/149694" target="_blank">📅 15:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
فارس: شب گذشته ۷ کشتی و شب پیش از آن ۱۲ کشتی هدف قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/149693" target="_blank">📅 15:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149691">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRiv0Kvot3cxVmHDvNRoSFSTtzyDx_5Ois4L8nvcKVsorZLZgZjEWCB0Rp54SfmZUS2MeBHxU1K1JYh3sA6q7L_JkDyV54zNTouPDLml0fr6lt4YDAgLVnm0Z8HwUeYpYSiDCnlUVOAbBIw3EbGk7v-Brp9vSwf9FjhSQQJ08dm45LAy8ivECLAMtOjtse0dQmzIZQtpKS6Rww8Q__Ys2BxHGoNPeG5pxKLF7Ea1LD49tZCPzL7DLLOXKdNnqYPq6abQmONlDMnN4O4g_bBW8LtAV13zLsklXaeKN-LRnvxJo4XYTXzL3Qcs4v3uRWMgoU2K_llfUSyzrZQVlIfBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e744fd9.mp4?token=bZ1xH85KtBk-qkJDaOeGah6gP5vSmwabs9huphWdIh5mtmiNybRiz7pDOTtKguKIe9k-w7sth5gO_4wWPCFR_aL_oEHBImT0oxteW4PN07S1EleLoNy7kvDa9KgAqYI7dyMwbQX3Hb_uQJzMho8j6AgbUdIgtANSbpTamykwN7SaMh0BD9QS11kV9t0PNl88a_b0k5RJ-ezxiHu1sdNccaEj51aiWKS4M04DRixP4syzpW3aL_bPH9i7FceaeCT7hF7HXltop6ham1vUqu5AFFEpmCfsN7qBUjidd65i4gZzJaZ2r8ruD4BBM0deOBidsnKsg3jN3VYoDIRuKfL3XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e744fd9.mp4?token=bZ1xH85KtBk-qkJDaOeGah6gP5vSmwabs9huphWdIh5mtmiNybRiz7pDOTtKguKIe9k-w7sth5gO_4wWPCFR_aL_oEHBImT0oxteW4PN07S1EleLoNy7kvDa9KgAqYI7dyMwbQX3Hb_uQJzMho8j6AgbUdIgtANSbpTamykwN7SaMh0BD9QS11kV9t0PNl88a_b0k5RJ-ezxiHu1sdNccaEj51aiWKS4M04DRixP4syzpW3aL_bPH9i7FceaeCT7hF7HXltop6ham1vUqu5AFFEpmCfsN7qBUjidd65i4gZzJaZ2r8ruD4BBM0deOBidsnKsg3jN3VYoDIRuKfL3XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خنثی‌سازی مواد منفجره در نزدیکی پایگاه هوایی فیر‌فورد بریتانیا
🔴
نیروهای امنیتی بریتانیا در حال تلاش برای خنثی‌سازی مواد منفجره در نزدیکی پایگاه هوایی فیر‌فورد هستند.
🔴
در تصاویر، یک ربات کوچک خنثی‌کننده بمب در نزدیکی چند کامیون دیده می‌شود که احتمالاً حامل مواد منفجره بوده‌اند و به سمت پایگاه هوایی در حرکت بودند.
پایگاه فیر‌فورد محل استقرار بمب‌افکن‌های آمریکایی بی‌۱بی و بی‌۵۲اچ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/149691" target="_blank">📅 15:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149690">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فکت  فرودگاه نجف رو جمهوری اسلامی ساخته ولی الان هواپیماهای خودش نمیتونن برن اونجا.  [@AloTweet]</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/149690" target="_blank">📅 15:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149689">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
رئیس دانشگاه تهران: در جنگ اخیر ۲ استاد و ۵ دانشجو را از دست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/149689" target="_blank">📅 14:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149688">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سپاه: شکار دومین زهپاد [زیرسطحی] ارتش آمریکا در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/149688" target="_blank">📅 14:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149687">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUqBVlZ8ILytRkwGZRjX6kFhycBn6oh7plnl29sHvoLTg1htOIEcZVZXQoXUqLn3iKfXtrfB-uevaEbkmWK-NgKvfUwhj37K9g6qNrKjfo-pr8KN-wHtGyPXRE1_jxca1rpQAcqxrP5Nwiat6JxY3AAOJI7RW4P86cRkQrMmvCJ8x7PQbocOI2OO_HqeY13sZbBl8-hS1k6PgvoPm309gpvHCqlzUZes-3G_9ATTa-_mTGNjJBWO3JhnQS3IMHMeVEAHDFABmqR63Yv-7x_FzXAZPwHYVFA2pMn8sJDa7_YkcdW2QIbjyouQ9nUkFmjjnOG1zGZRqF2PjCDWtgdmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی قبل، پرواز ۴ هواپیمای مسافربری ایرانی به مقصد ترکیه
🔴
مطابق گزارشات، باوجود توقف پروازها در مسیرهایی مثل عراق و امارات، مسافران ایرانی می‌توانند با هواپیما راهی استانبول ترکیه، اسلام‌آباد پاکستان، کابل افغانستان، پکن چین،‌ دوشنبه تاجیکستان، ایروان ارمنستان و مسکو روسیه شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149687" target="_blank">📅 14:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149686">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رویترز: بوئینگ یک نقص نرم‌افزاری را که پیش‌تر افشا نشده بود، در هواپیماهای ۷۳۷ مکس شناسایی کرده
🔴
بر اساس این مشکل نرم‌افزاری، ممکن است خلبانان هنگام فرود، به هدایت خودکار پرواز دسترسی نداشته باشند
🔴
هنوز مشخص نیست چه تعداد هواپیما با این نقص در حال فعالیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149686" target="_blank">📅 14:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149685">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
فارس به نقل از  یک منبع آگاه نزدیک به تیم مذاکره‌کننده: پیشنهاد اخیر ایران [به آمریکا] دربرگیرندهٔ مجموعه‌ای از اقدامات متقابل و مرحله‌بندی‌شده است و ایران مواضع و ملاحظات خود را به‌صورت روشن به طرف‌های مقابل منتقل کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/149685" target="_blank">📅 14:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149684">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نقدعلی نماینده مجلس: مهدکودکم حضوری شد، چرا مجلس حضوری نمیشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/149684" target="_blank">📅 14:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149683">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO8SnO57ofXVxmd7dcNKXA2j64_JPw9QCjb3RhRlOq8yUu_7J_4n3kagP_59i6uXCjFBjWMi42V7LOb5QHCYgrUedOAr64mhVgo4dWz3aNLHm0SZO-hXkQr66KqwJqbaxS0eGrO7dqY6l8uqJ5FgOna6aLvUJas9v2mCYL8jXUd1qzK5HNTyvF2vdjuP5sZf494ANAc6wPrcPOcls7wFmfozG2lhPmHC4OmVQD3o4u7SPKojFahgCeAiFN31kqritbJifMlJ17KYEYFQGzgBdC8rzSytz_2balSa4Up2foyLhXhaSvlwTXuVRASsDST_am4GPo7oDaU1c-lLvntPfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با حملات هوایی سعودی که به کشته شدن و زخمی شدن حدود 50 نفر منجر شد، یک هواپیمای سوخت‌رسان بریتانیایی بر فراز دریای سرخ برای پشتیبانی از هواپیماهای سعودی فعالیت می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/149683" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149682">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ugaim_Vw8TDIV1xlCXBuTLVErH0-Hy3oSEbAO8tTiWEXk1QXHhFJMHkwRGRGBC3yprwu39pUcjvUbDdo1LKbLbZ_NaVuDsdUeUO6TXjrAMukh1xNMpnHsqQV2O4bIeyWtdGpd8V5aJGIv-LSGm39heepIDitEYQKZp6pelgMOKXwEYwNH_aDfhtacyNl1N8Chg9Gr4GbPRvn9OHrRD9E7Hmu0tKrOA4aiQkej5WjkbnWm89IK7G-eBFXTTWtcaZXXyjDs02djeaCXbMk82rJetvRvEyw5rYGfRvY-b5AtJN0Lrw5-DMisYrGPme8smCjMxyLMUQpeYCiGp4n-kFpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سپاه: شکار دومین زهپاد [زیرسطحی] ارتش آمریکا در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/149682" target="_blank">📅 14:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر انرژی امریکا : روزانه حدود 13 میلیون بشکه نفت از تنگه هرمز عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149681" target="_blank">📅 14:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmtnrTMAzrAfEUymVtATLB1DLJLMco8RQfDbjbtg_ZjLwxvauXiyo71jKFR83v_ocuumL2LBZ_Klx1J_AWknlyL0JdoWGxAOotKB-32Bpy8_HNyvqaO98JnLKVju_8-QsivSF1mb_fshM_xD-X8BQmAMSGzAM3FDQxC4BeOe7ZNnnH49xINWpn1AytuAgLNKTG-bU34-1_IIV-Rqg1fh9VgknjrbRtSA3FNlsG8AKoFiYmej5xk0ZQcbn6fTA5xXLzH2M0dfQDtaMZpB7dSyPmgKT9ThTB12hHReAhOjsVQ71WtAfBlc9qRAlhPMhk9GfEPop3xL2QMIRA6j1arQrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نامه میلی گلد به محسن رضایی: بانک مرکزی یک تن طلایمان را نمی دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149680" target="_blank">📅 13:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بی‌بی‌سی: در پی اعلام «حادثه بزرگ» در نزدیکی پایگاه هوایی سلطنتی فیرفورد (RAF Fairford)، پایگاهی در بریتانیا که میزبان نیروی هوایی آمریکا است، چند مرد بر اساس «قانون مواد منفجره» بازداشت شدند.
🔴
هم‌زمان با بررسی چند خودرو توسط متخصصان خنثی‌سازی بمب ارتش،…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149679" target="_blank">📅 13:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
امیر حاتمی فرمانده ارتش: جنگ هنوز به پایان نرسیده است و ما باید برای وارد کردن ضربات قوی به دشمن آماده باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/149678" target="_blank">📅 13:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099d500c99.mp4?token=HMZJICy49RFzDqZ6QzmoQQUjqUiRisOP1T0h0DcVlp_5ZhNLH49SuolN2HxUHhW3LqytfnDcZI55Fpr6SBXSNvKTxCSQ72e7HKMpidc7rq5fEZ98X3wGQSdAUbAxi2zwr43D-_ZERwMUr2DQ_ZIauFmre8TGLNXkcNDASAS7ud0ebpRxSd_83JtZPAjqGfEbKULv2fwjYElv8xlOeJc4_Oqqe4K-YVHALzHiEL9xRsaDmNcnEBXWvpmI0qOO87k_3K9cxQ0QY_zagup8yzJl5toQQX7sVC0bIYaYVJrUdy3ge9Mz_5z1MYHqezpcmX8GqiV_Lb5sFu33zM-oAcxmimlrZ4PvWy2TzWxDlP-Sq0TNyIWnB57re0jpUkbQpZKgp2eE7Lf2eUUa07lImJiTlIWDLEnsqzpWNKoGcZLQL_nM5bYgmbFgYXSRqhih2rfsS0-hnmzVtt19-Iu09Yo9VsKpq-2mGIGgvMwjRbEAsA0XAy9mC5174PDFUWW_BFRWAe2N0dYTw0y5lfSb6P1lg29l0xEXDjbJT68sAHA3zdv_3-bjvVwXoq1rRuuSV6i8fc_JmAKKAgWSllSgj3ofABySAK4itaPu3PrZWbPa1AdI01dKhkxp2sPmhPpWU65kXvGJrW72g3hOOCESoRqrg_-0nIkc20xWMgBfCKvxfMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099d500c99.mp4?token=HMZJICy49RFzDqZ6QzmoQQUjqUiRisOP1T0h0DcVlp_5ZhNLH49SuolN2HxUHhW3LqytfnDcZI55Fpr6SBXSNvKTxCSQ72e7HKMpidc7rq5fEZ98X3wGQSdAUbAxi2zwr43D-_ZERwMUr2DQ_ZIauFmre8TGLNXkcNDASAS7ud0ebpRxSd_83JtZPAjqGfEbKULv2fwjYElv8xlOeJc4_Oqqe4K-YVHALzHiEL9xRsaDmNcnEBXWvpmI0qOO87k_3K9cxQ0QY_zagup8yzJl5toQQX7sVC0bIYaYVJrUdy3ge9Mz_5z1MYHqezpcmX8GqiV_Lb5sFu33zM-oAcxmimlrZ4PvWy2TzWxDlP-Sq0TNyIWnB57re0jpUkbQpZKgp2eE7Lf2eUUa07lImJiTlIWDLEnsqzpWNKoGcZLQL_nM5bYgmbFgYXSRqhih2rfsS0-hnmzVtt19-Iu09Yo9VsKpq-2mGIGgvMwjRbEAsA0XAy9mC5174PDFUWW_BFRWAe2N0dYTw0y5lfSb6P1lg29l0xEXDjbJT68sAHA3zdv_3-bjvVwXoq1rRuuSV6i8fc_JmAKKAgWSllSgj3ofABySAK4itaPu3PrZWbPa1AdI01dKhkxp2sPmhPpWU65kXvGJrW72g3hOOCESoRqrg_-0nIkc20xWMgBfCKvxfMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظات اولیه حمله سعودی که بازار تعز در تقاطع الماوية را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149677" target="_blank">📅 13:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149675">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Os0J4O4u58ahxhD_K5MRPCXAJGepIZdiRCiAVL5Lq5SAXa9wUbwRoFlIAyvg_Ft-HASqcEHZKuGJ-SDnMSjWyjUBNJWjRagpXO6s4oxMVqPm1J3sCSZnGXyPKpFfyQtMZhPO-_Ry8OlBDYqjt7Rch9wX3Sp2nuk2ajIQaVN13qwaBjJwPjR6wbG_sEx07QeL6Y31mOkg6O_TLWNWT9jJWOu6oZ_Y74nS1wqtwxH7lciWNeNTJ9MXTSK7UHsNoWI8IKjflGC77hxk5mID7qUIMYrJ7xqLZQIDAC2NdeyOnPMh-EjyDH-HhkcF7HXV9rh9yxPTLo2Qx0bbkHY8yOdKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyxYvjOSOzQOi_7Gwkq1OJxlF_NxKQmRwgxIZl2_e1nNG4LuqL6qej7GmnU7oW9stWTqVAHAXa9xb-7nXW-ZQAH2ENDY7MuBGB1lPMycLEwIY9UFAn9cORKzkaYPmFBb1gbLarTIiNokDRayiv6UDCCfck7qFhVrGuH8H_hngqyVGQ9ICIYR0uqhbe5Rss9jBGm4WhMsFDqQG5Cggbp4OY8Sge1na4jEUh7LVchsMmxL6vv5Pka9Q_9TMDiz0IcpIZP9lKILqMnH4oTpFRHtY-vuVypJrM8-4dP_i5MT5_KMN2lRoMvjasjQcsW773Q_P7hM4SS4gFcXkGRD3vDUXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌ای هوایی گسترده از سوی نیروی هوایی عربستان سعودی، زیرساخت‌های مدنی را در استان تعز در یمن هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149675" target="_blank">📅 13:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149674">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نیروهای هوایی عربستان سعودی با سلسله‌ای از حملات، فروشگاه‌های تجاری در منطقه "المؤسسة الاقتصادية اليمنية" در تقاطع "ماویه" در منطقه "التعزیه" از استان تعز را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/149674" target="_blank">📅 13:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
حاجی‌بابایی، نماینده مجلس: ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/149673" target="_blank">📅 13:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149672">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841e48be90.mp4?token=k5VS5GUW9lAOwrNJhJFQy9kXsHZlWMtJSuP-ENNF7veGqO8ZHfd9irrfB2X4gsNB7QwUmNzAc4jvetPbDK4CHJZfAYdQm8aEqNj4rEX5tMq3q7I2FDLMKQD47-m7puLe0dUba9vjw4933DCKDuN0f4gLNokEydEmRsC4pro_7pb5hQK9vrBTY_DkfafOMsdIQp3yLEiBMPIb7okepzDx1nCzZ6p9_lgGFWAVaOQVCQkXA3lPio9fACfWQYjpLRbk35q20oV3j62NsmyopVmvTBKffL4G4XDr0_d7-4ZNErvuSLKnJHbjG_gfn2xOIrvOewvvXmtNMATneNtf_weMxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841e48be90.mp4?token=k5VS5GUW9lAOwrNJhJFQy9kXsHZlWMtJSuP-ENNF7veGqO8ZHfd9irrfB2X4gsNB7QwUmNzAc4jvetPbDK4CHJZfAYdQm8aEqNj4rEX5tMq3q7I2FDLMKQD47-m7puLe0dUba9vjw4933DCKDuN0f4gLNokEydEmRsC4pro_7pb5hQK9vrBTY_DkfafOMsdIQp3yLEiBMPIb7okepzDx1nCzZ6p9_lgGFWAVaOQVCQkXA3lPio9fACfWQYjpLRbk35q20oV3j62NsmyopVmvTBKffL4G4XDr0_d7-4ZNErvuSLKnJHbjG_gfn2xOIrvOewvvXmtNMATneNtf_weMxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر بیشتری از حملات هوایی عربستان سعودی که استان تعز در یمن را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149672" target="_blank">📅 13:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پزشکیان: چیزایی که تو سازمان ملل گفتم کار من نبود، خدا بر زبانم جاری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149671" target="_blank">📅 13:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نیروهای دفاعی افغانستان اعلام کردند که 28 نفر پس از عبور از پاکستان به شرق افغانستان کشته شده‌اند و افزودند که بیشتر این افراد، اعضای سابق نیروهای امنیتی افغانستان بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149670" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e72d805d.mp4?token=tq58REbkNAqZ7Rm_Aa1Tt30CL0NI6uZ5gf3fuXrU9_VfNGz0nQuAQNBXGg7jMXCLiSYrKr5QOAyPQWJwkWHYEzQXbZSQfnrQKLHFpIqYIrNLT4pwVkWlvHBbiRH2hLioJ-Hl2UTMP_kcXS8ee8qEQHKNLGmR7rwFK9hPU4J0Kpa9bkVoyy3Vvw5cVRbwYYPrYlsi7NyN80VCwbaoa5Sep7KwYQmbM7W2t3sH4Ak6rtZ98owBkyufxnA9g0Q1ppt0n_YfLvlZIgpAmLUojD3TCNrg50EjLnc9qC9m4Mb_Pj0vjgFNUIJeH5fbZoT7HKXDPQoMtocp1Qv9AaYJkU6SkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e72d805d.mp4?token=tq58REbkNAqZ7Rm_Aa1Tt30CL0NI6uZ5gf3fuXrU9_VfNGz0nQuAQNBXGg7jMXCLiSYrKr5QOAyPQWJwkWHYEzQXbZSQfnrQKLHFpIqYIrNLT4pwVkWlvHBbiRH2hLioJ-Hl2UTMP_kcXS8ee8qEQHKNLGmR7rwFK9hPU4J0Kpa9bkVoyy3Vvw5cVRbwYYPrYlsi7NyN80VCwbaoa5Sep7KwYQmbM7W2t3sH4Ak6rtZ98owBkyufxnA9g0Q1ppt0n_YfLvlZIgpAmLUojD3TCNrg50EjLnc9qC9m4Mb_Pj0vjgFNUIJeH5fbZoT7HKXDPQoMtocp1Qv9AaYJkU6SkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) اعلام کرد که در حملات جداگانه در نوار غزه، دو عضو حماس را کشته است
🔴
در نصیرات، «ابراهیم فوزی اسماعیل محسن» که به گفته ارتش اسرائیل فرمانده یک دسته از یگان نخبه حماس بوده، کشته شد.
🔴
در حمله‌ای جداگانه در خان‌یونس نیز «محمد کامل سلیمان محسن»، از اعضای شاخه نظامی حماس، کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149669" target="_blank">📅 12:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
عباس عبدی به یک سال حبس محکوم شد؛ توقف دوماهه فعالیت روزنامه اعتماد
🔴
خبرگزاری فارس گزارش داده عباس عبدی به یک سال حبس تعزیری محکوم شده و دادگاه همچنین حکم به توقف دوماهه فعالیت و انتشار روزنامه «اعتماد» داده است.
🔴
براساس این گزارش، متهمان نسبت به رأی صادرشده فرجام‌خواهی کرده‌اند و پرونده برای بررسی به دیوان عالی کشور ارسال شده است.
🔴
بنابراین این احکام هنوز قطعی نشده‌اند و نتیجه نهایی به رأی دیوان عالی کشور بستگی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149668" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439e435273.mp4?token=Z69GhuDZ-8GmxIDxcEqra1gb1TNrTViL6D4zrwMRpugAkTAWY9Y_qj6LjGBemU9Hhc7T9sz_yoaz9V2Xfvh_f9x-rDKeqPGFeUKaONYUTjxT4p6z8Pu5uGfVgxGNVXG79ojT0ucdLwfeKA0zo_Gf3Oeh7aI7PNr59xX-WZw5BVzn4N0bGe6TW-xdc0Emm4_88vnB6tfqPacxlXzdKfXY6VbEwd5INfap79Q47SBC7W8RIpjKNWCO5PqbPAE0BYaVN6ln3PFce_Wypfywscnm52Yyasz0jnj9HkluX9pdca9XztIfFEWOsEnKaS5gjmcHmONlLl3jckdmqaEWHasODjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439e435273.mp4?token=Z69GhuDZ-8GmxIDxcEqra1gb1TNrTViL6D4zrwMRpugAkTAWY9Y_qj6LjGBemU9Hhc7T9sz_yoaz9V2Xfvh_f9x-rDKeqPGFeUKaONYUTjxT4p6z8Pu5uGfVgxGNVXG79ojT0ucdLwfeKA0zo_Gf3Oeh7aI7PNr59xX-WZw5BVzn4N0bGe6TW-xdc0Emm4_88vnB6tfqPacxlXzdKfXY6VbEwd5INfap79Q47SBC7W8RIpjKNWCO5PqbPAE0BYaVN6ln3PFce_Wypfywscnm52Yyasz0jnj9HkluX9pdca9XztIfFEWOsEnKaS5gjmcHmONlLl3jckdmqaEWHasODjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیک موتوری؛ شغل دانشجوی ممتاز دانشگاه امیر کبیر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/149667" target="_blank">📅 12:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149665">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c69bc7a57.mp4?token=NOf0sQTGVMfgxmGu1evCULBFmCpTHpY8zkjxIFbJSQzfnQ2jPIIirSrwbSwQlUHtPj3tuSJGTxHzwtaTvMAZVkE2XJuNI0480qfv1NUcVvd6N0o6sKBXQyUnwDV-YjeLgYVV9za3ZLt6yA-NQ-J3F7HkUdsgQz-YhBcwA7jHfFAhGvMi6M4fReJcmv49syNIybOyQ6U-Ta6wJosYGh5bwhWPLW8f67cL_Rb4uJiKWRQ8G3FIvZPqtKPoE9EHMb4AiVKJ3f3_Nm0XBaPYbftnc43qbCB-H6-e4w1iHrqAgvQpVXMm5Ek9KysdCOOMKq4fM4xYW9WCLlVqh8HweoY8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c69bc7a57.mp4?token=NOf0sQTGVMfgxmGu1evCULBFmCpTHpY8zkjxIFbJSQzfnQ2jPIIirSrwbSwQlUHtPj3tuSJGTxHzwtaTvMAZVkE2XJuNI0480qfv1NUcVvd6N0o6sKBXQyUnwDV-YjeLgYVV9za3ZLt6yA-NQ-J3F7HkUdsgQz-YhBcwA7jHfFAhGvMi6M4fReJcmv49syNIybOyQ6U-Ta6wJosYGh5bwhWPLW8f67cL_Rb4uJiKWRQ8G3FIvZPqtKPoE9EHMb4AiVKJ3f3_Nm0XBaPYbftnc43qbCB-H6-e4w1iHrqAgvQpVXMm5Ek9KysdCOOMKq4fM4xYW9WCLlVqh8HweoY8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) اعلام کرد که حزب‌الله بامداد یک پهپاد انفجاری را به سمت نیروهای اسرائیلی مستقر در منطقه امنیتی جنوب لبنان پرتاب کرده است. در این حمله کسی زخمی نشده است
🔴
در واکنش، ارتش اسرائیل از انجام حملات هوایی علیه اهداف حزب‌الله در چند منطقه از جنوب لبنان خبر داد؛ از جمله مواضعی که به گفته اسرائیل برای پرتاب پهپادهای انفجاری و موشک‌های ضدزره علیه نیروهای این کشور استفاده می‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149665" target="_blank">📅 12:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149664">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZ-R29B3CgdzTdmt0xLlf_VWQ35sBcVnpXsjzllgBjPHY-1kH2dtJhVJJL6eqnK9LmP8bcra7tMpMuGjhjqSqw_g8_PYjgM7OEi-wGqyoc11Q_HQPe6Yq6MZCg8tQWHv7DWL_VQg0B5YZlGOfijIcAKBGTw6LYF-t45B_6l81ldrpKHyIxtQudKU-beWuDetJcDnfPPgx9A4W0_uJAeIVKIambqabAge5JuoDdPt8TDm_nNDBddDmFcXB4a8RTwd_iTVVFZg3M-byHsfPJKWSEAiWRjDGXT3Un6u0Ba0ARosALgYuyj25JdCaHwYWnYbcrP_4BQNGPTh0vRlwGmQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌های هوایی عربستان سعودی، چندین منطقه از استان تعز در یمن را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149664" target="_blank">📅 12:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149663">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رسایی بخاطر شکایت قالیباف و چندتا موضوع دیگه تو سال 1402، به 10ماه حبس محکوم شد  #عروس_زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149663" target="_blank">📅 12:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149662">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مدیرعامل شرکت ملی نفت ایران:
بر اساس اطلاعات به‌دست‌آمده، اسرائیل و آمریکا برای ضربه زدن به تاسیسات نفتی برنامه‌ریزی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149662" target="_blank">📅 12:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149661">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
کارولین لیویت سخنگوی سابق کاخ سفید:
گاهی فکر می‌کنم ترامپ شاید بیشتر از مردان به حرف زنان گوش می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149661" target="_blank">📅 12:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149660">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
برخورد قطار با یک عابر پیاده در ساری جان مردی ۳۵ ساله را گرفت؛ علت حادثه هنوز اعلام نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149660" target="_blank">📅 12:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149659">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / گزارش‌ها حاکی از آن است که پایگاه RAF Fairford در بریتانیا به سطح FPCON Delta، بالاترین سطح حفاظت نیروهای نظامی آمریکا، منتقل شده است.
🔴
این اقدام همزمان با حادثه‌ای امنیتی در ولفورد و بازداشت چند نفر به ظن جرایم مرتبط با مواد منفجره انجام شده است.…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/149659" target="_blank">📅 11:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149658">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK3RDm1lG9NugivaqtIjPNKwtuDgq5hjDrMirihioAteXdpWmzMy4JZqhdLvxfqdl4W-B7qX-16oQQCMDOY8_S42cZuEZhfH5MBLkPUZZCqHtlDXbGQDBJvxbFsP4N1j-o52avpZ3LWNiufffsnGc0KJk0zrCWOB4MBozkUepcTI6bkhFjxeG7l6f41qvVNZkSQCIG8EXbioMKfEkX4FOhif3GMqBXzzSzRRfFfrD7iyhUGC3UMTIEvkPFvh9yzH7d5blGtCc7FiyVqWLj9P6KyXrU4S1Sc8bklH0Kc7tkKfOGjriBOpRb-noWCIoKDx9uXACq1FJAdl27HMkxerXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی بخاطر شکایت قالیباف و چندتا موضوع دیگه تو سال 1402، به 10ماه حبس محکوم شد
#عروس_زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149658" target="_blank">📅 11:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149657">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44476a7f42.mp4?token=cRtAf49BNlqHXly7P4QaBoOkhAvmlq8PLRBPTAgj0XAigz9MhNJk0Ke5FfhUv54Q3TTDYb1G8hnd0zS3sb1k9gx3ttMnnlrxQkmH6BTOtJ4mIlE6jBKtoRbyLha0jTHj_PFCtD7bMDLyj6PRL8hTQz5Rm9U-px2rfr02Le535Ec8NffKRdSk8pLsojLroExbFxh9pcCJpSEaEbibDxxqBjOqxM6CA4y1aHS1dwFHU0C8oYxYoLdpYal0vxoMTbGxYq8R_XobLW_5R0ySmBsAYRJIxbaH6qtdV7Zz1vWq069YmO-fHQS_p2QTlSsspuDdOjW2NSwBzm3mh9VtowMK8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44476a7f42.mp4?token=cRtAf49BNlqHXly7P4QaBoOkhAvmlq8PLRBPTAgj0XAigz9MhNJk0Ke5FfhUv54Q3TTDYb1G8hnd0zS3sb1k9gx3ttMnnlrxQkmH6BTOtJ4mIlE6jBKtoRbyLha0jTHj_PFCtD7bMDLyj6PRL8hTQz5Rm9U-px2rfr02Le535Ec8NffKRdSk8pLsojLroExbFxh9pcCJpSEaEbibDxxqBjOqxM6CA4y1aHS1dwFHU0C8oYxYoLdpYal0vxoMTbGxYq8R_XobLW_5R0ySmBsAYRJIxbaH6qtdV7Zz1vWq069YmO-fHQS_p2QTlSsspuDdOjW2NSwBzm3mh9VtowMK8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دوربین مداربسته از سرقت موبایل یک خانم در پیاده رو
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149657" target="_blank">📅 11:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149656">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b665c32a7b.mp4?token=SCRXRIKJ5VrhGBnLexF3PTn3hOlI7nE_OTV3s9se5GE_YIaxJ4N69IUxMe44HEPljMRfrCCtC2RN99ikbytS5UWR854g_vqLORY2D4xiI53d0m--w9EGDmOtaJfVAKXseg3i_r3T9bmaMhvcWzvuEqlBsFrb7cd8wO1PVsZNBggrNBtoK_KR23rjHmNeMLw7oIMw7x5EpNHtwjMMA_bYJgTHWI8dVXxG-TP0curX00YcVbUAL0w8wBIxLkoj8GX-c8ZUv27Zmd5WI1Frm5qpH-qdbYTyvz8_8PrwY3ZUhMVCn_80ZPQ485fYuRUNYp1Rls5GgqGihr6XFYBANx0cmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b665c32a7b.mp4?token=SCRXRIKJ5VrhGBnLexF3PTn3hOlI7nE_OTV3s9se5GE_YIaxJ4N69IUxMe44HEPljMRfrCCtC2RN99ikbytS5UWR854g_vqLORY2D4xiI53d0m--w9EGDmOtaJfVAKXseg3i_r3T9bmaMhvcWzvuEqlBsFrb7cd8wO1PVsZNBggrNBtoK_KR23rjHmNeMLw7oIMw7x5EpNHtwjMMA_bYJgTHWI8dVXxG-TP0curX00YcVbUAL0w8wBIxLkoj8GX-c8ZUv27Zmd5WI1Frm5qpH-qdbYTyvz8_8PrwY3ZUhMVCn_80ZPQ485fYuRUNYp1Rls5GgqGihr6XFYBANx0cmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که انصارالله یمن طی چند روز گذشته، یک مخزن ذخیره‌سازی نفت را در ینبع عربستان هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149656" target="_blank">📅 11:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149655">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نخست‌وزیر اسلوونی: تغییر حکومت در ایران برای صلح پایدار ضروری است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149655" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTM7woPb1ZlFXfgdFvn1-cCPCbyo4NwAfLh4oskcr1OAInG64vLuHwHtkp_NTWGmYtfTcSl1rinVvjZRd0J-uO4MW7qJ_rcMJaKFEdCueMmtoDFiozJRKyUkZrzpR_nFsa9qNBtcbQ6Uz0HjwJWZ9GOOgG4Tr3RcaphQzQnhDV16M2udJZar3BSXCUd_hl2CHih8S500iI5eajIa03MCLLnUQz5tuk5iiAYVHc1WgZPgkm_KOMexHhd8VTbcr8xf_kcD_n7v8dKA7He0YXjFJEkKkdPApyyXcWbhJtIZH9rgddpWWQAVbx4M9ECLoc8vBRegLkDYaMCgqO4VyRVN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f40191a121.mp4?token=HwVFhcqrBtoidlM_QuOVjjn8cybD1FsVUfxWqM_Ka9pNqrFV9BfPmvooxllA0mtSiAbjVdGdy9UJsaVLpNPP-8UU15yxMvlSV_ImfOB0YMgRXMZ0U2YqjdSQAyoyVEs93p1qZteoxYroDBXEASjkTJODl9iW6CIo6XKfH9fUvKcQbDDZwrHWR3ImfxBlmIQ-TdfUOOe1-mjHhxVpppi5psCPWs3FI9EDJW6rqHBUMp7fFJKZaCaK3H4LzI54deSrRxXmEUAmDpTLXAapKk8cAzfBDWbjlEhfTGeT-asGNT2k7vWklb6YEat72x2DeWHB5UEvWLZoz68WNgQGWkRDsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f40191a121.mp4?token=HwVFhcqrBtoidlM_QuOVjjn8cybD1FsVUfxWqM_Ka9pNqrFV9BfPmvooxllA0mtSiAbjVdGdy9UJsaVLpNPP-8UU15yxMvlSV_ImfOB0YMgRXMZ0U2YqjdSQAyoyVEs93p1qZteoxYroDBXEASjkTJODl9iW6CIo6XKfH9fUvKcQbDDZwrHWR3ImfxBlmIQ-TdfUOOe1-mjHhxVpppi5psCPWs3FI9EDJW6rqHBUMp7fFJKZaCaK3H4LzI54deSrRxXmEUAmDpTLXAapKk8cAzfBDWbjlEhfTGeT-asGNT2k7vWklb6YEat72x2DeWHB5UEvWLZoz68WNgQGWkRDsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو سال پیش تو چنین روزی حسن نصرالله با 80تن بمب سنگرشکن ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149653" target="_blank">📅 11:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149652">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez4Uz5gS8BHQK7nQkl0JwpUs93dj668KUMh4LoI7PLjS3FwuWPHiJKcHG726QQek1m-6yopCMwYIGfM8KJGMG1-xCqV11e0_BB9GYdBDv11mvcNYseRjqw5O01xcI_FiBADcBCsC2YcoWW_Is0sy5lymrmzA0T8u0RZALDOiuRZOb12qtMUrTg4TFVsqelt7ctdckSoacfhaQmwfmH-WzvaZDRv2gYb1zR55fa315CcGKGnl4FAcB2c0qZZDiOdVlbNHdrh3z34M_EsLCmOPbMeH8YT2OM5-e8LNvv_DZogo8WRmE9r4ZHPvs81v0tYRiCigONt2QR6feZIg5VJ5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / گزارش‌ها حاکی از آن است که پایگاه RAF Fairford در بریتانیا به سطح FPCON Delta، بالاترین سطح حفاظت نیروهای نظامی آمریکا، منتقل شده است.
🔴
این اقدام همزمان با حادثه‌ای امنیتی در ولفورد و بازداشت چند نفر به ظن جرایم مرتبط با مواد منفجره انجام شده است. چند ملک تخلیه شده و تیم خنثی‌سازی مواد منفجره در حال بررسی خودروهاست.
🔴
سخنگوی نیروی هوایی آمریکا اعلام کرده نیروهای پایگاه در حالت آماده‌باش و هوشیاری بالا قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149652" target="_blank">📅 11:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149651">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoK0xYK0a36FW3fPBuuLqOlqGEpGOmA_dtlRjC_qcvk173ZMoya7usqmzXS4oHleoj6CE4pEYNqv2Om0ehVpm-wG2ZaW2aiyOjbYVx8X9slD-GTUaZqnj4HCGTUu5D_8wvw_4c6i5CB50HnB_qfFBkq1Zufie6ZDWfioKaZcPXf27cmQAHqmB0IivzyJ384tuKWmC6QAexkITio-_yjvzkWAojsIFM9cWT9OyfPTDeahqul6efvqGS3FJjpgOwmaF9w75OLy40e7uUFBqrabWw6SEIjK-0uEjLgVR1kjxWUEXk2Jt6GFy8osGpSxEOAu7G4j3ddqpwFAqdyC3nO1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی رغم پایان فصل تابستان، قطعی برق برنامه ریزی شده در استان خوزستان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149651" target="_blank">📅 11:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149650">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWcmUuo_V380A6TTT1Ku78-c_2Fcea4HGCaOMjwoPFLnrsyXysjKNKuFDMdW7uFmIpsFB1_GwLyjas58qGISad8NL35Rc-CtkMW4CPWtpdLotVZVbINcE0GkRcPSk6zr2u55ebm1Bm4f_vKr676ciTqqUtr5P-gNE2QDKOuuulj_PtAn5KTJ8XAs7bFZl4wBGCcbNfaGR3z_kZLUQPKn90sc677oyeqyWeYH9kBzVZFQnX5ezBSat5yICQDAAbm5TZtMqvNO2p3d6OnNYTZAZyvxF5_QxpC6buMOmuTraYcSXA6gnDbOy8Fqd_fR1K2CZmXRwNH_2JsDUcGG2Rd-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گوگل تولید ویدیوهای ۱۰۸۰p با هوش مصنوعی را برای همه کاربران فعال کرد
🔴
گوگل امکان تولید ویدیو با وضوح ۱۰۸۰p را در Google Vids برای دارندگان حساب‌های عادی و Google Workspace فراهم کرد. این قابلیت با استفاده از مدل Gemini Omni ۱.۱ Flash، امکان ساخت ویدیو از روی متن، عکس، صدا یا کلیپ‌های موجود را فراهم می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149650" target="_blank">📅 11:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149649">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qO_4nSC-2OaNZZE8xMA9Vz7-0gZmznEcw6-b33M2gLDrq_muD4-D-c6W7UddTcaURsYheyl_y-jOPc2OTAI0wmemWGYrp3arDI4nIAILU8XfsC8x0Qc1XqCmZ0_hBO1QuohpvEhFNKBwKEiopivRgzxSOnr7Bk_bAmchCHEd_3tl5PT9_h_13XRqMcRSW3_cHPjjnohMHD8tW3mHvNlDXcJ6EpzlTFg1VQWEAYDgvtlcZp5wfyXPjopsFc_AZ6XhEIz8AHa_GLSh5qyENFo7ub7jmDNs3IpEahSsrbSCbfIdPskt68oQ0p9olam-pXKMetetgRzGhp8WKBvpy1AmJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه عبری والا: ارتش اسرائیل در آستانه عید یهودی سوکوت (سُکّوت)، سطح آماده‌باش خود را در کرانه باختری افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149649" target="_blank">📅 10:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149648">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lczCjFqzOiiHYLlxCTwbjgfOhvjQQJWRreTl6uz4UXm9UChRn3m3rjTJshYA-C2P6rAaITfMbXI2L3vLJ1HrHka9EBoMAOD-MrS345pTlaqJtgCwOEgv4yrBIzWuM3VmNsAZTjVldncybBHcN2MMY3TZfTKMgQjJKqiLxvwwVKpXippAkIphjP0XgrKN2Vfv5kwr5ew9u-ChVRiFjzt5emvXfdaiC_OVj2cvPbpTWJmhRb9yqGzC2RcgZG1by6eU09OXnNBMReDjuhKfIwkmOCupFTNBzDs6jcbs8OTxvsHg8rKjKPB0L5HWbtNqiPttgZf-f1vSwQ0rRgXVsaeMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای اسرائیلی مناطقی در جنوب لبنان را هدف حملات هوایی، توپخانه‌ای و تیراندازی با مسلسل قرار دادند.
🔴
حملات هوایی: نبطیه الفوقا، میفدون و کفر تبنیت
🔴
گلوله‌باران توپخانه‌ای: وادی زبقین، منصوری، وادی السلوقی و حداثه
🔴
تیراندازی با مسلسل: بیت یاحون، صری‌بین و وادی زبقین
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149648" target="_blank">📅 10:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149647">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rSlVi7BNyRSvmt5F9Og5Dsd5kSJSnTwJ94dHiVlHqjYKlE_G6z7h8W9ngLrbKrwuKoccDTrNi7jevwUxV4w5k2pNRd1uMSRUL_oByq_jxtkr5jPUuqKCC7KPcLJwn25hutgY2KFqaLfGIOrQ3t2aJwC64ZOo20pz2iOdQRLN7kNzaopsgVI7YlN9TfMJAI73k7-BTRgfTelYUVgG0kkQZXMTVMZvP_8_TRuRrB0ArWvI-Rho8_9_quoEcZ5moK-oyQNlwCSiERKiAtBJ3oET4IV_dCWCJLFvFLPyNmwzOCYwNunwhLSndl_KpzxR_P6ImpKGoTVlOvzc-s0AVNDNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لهستان و لیتوانی در حال تدوین طرح‌های مشترک برای تخلیه گسترده غیرنظامیان از منطقه بالتیک در صورت وقوع حمله احتمالی روسیه هستند.
🔴
این طرح‌ها شامل رویه‌های اجرایی، لجستیک، زیرساخت‌ها و مسیرهای تخلیه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149647" target="_blank">📅 10:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149646">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
تورم نقطه‌ای شهریور به ۸۳.۸ درصد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149646" target="_blank">📅 10:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149645">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
توافق بغداد - واشنگتن با ازسرگیری ارسال محموله‌های دلاری به عراق
🔴
سخنگوی دولت عراق: بغداد با آمریکا به توافقی برای ازسرگیری ارسال محموله‌های نقدی دلار به عراق پس از چند ماه تعلیق دست یافته است که به تامین تقاضای داخلی این کشور برای ارز خارجی کمک می‌کند.
🔴
یک محموله جدید در روزهای آینده خواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149645" target="_blank">📅 10:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149644">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رویترز: با ورود طوفان شدید از سمت سواحل شمال شرقی به آمریکا که سبب بروز سیلاب و وزش بادهای سهمگین شده است، برق بیش از ۱۰۰ هزار واحد مسکونی و تجاری قطع گردید و بیش از ۴۰۰ پرواز فرودگاه‌های ایالات متحده لغو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149644" target="_blank">📅 10:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149643">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fhOseeQ50tEmhV_E0pcVlmaz6i7qQLGUPKHIFRl0yfa-KERZaruWJSfEs2-a54chXy8prsM1AQ6FWDLoN9BfelATwNweDFtjjhGGNmxvrG8iIV-1qgn2wkoWElPb5CEZMQ7YoZDxYBeTkagNCquCchGIEs74QA3WLLK9QdJ4QgeFi6UgbQx-ouVQWvomyEz7jj2TMw8dKqP_wEMR0zQSyV1BzB0TUrOprWjc0k4KdMMWjKbqxnVTlBKfktc-bW6ydAboah6K7CVnGh7ta8iTUPVDgZ8y_OStNjtqyZQVVFXCB06bRDb4JE6V0ZLlsP2eHEnVKgJ0R1_ovIAgfU-TNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین محکومیت اقدامات این کشور از سوی آمریکا در نزدیکی آبسنگ دوم توماس در ۲۴ سپتامبر را محکوم کرد
🔴
سفارت چین در مانیل، آمریکا را به حمایت از «اقدامات تحریک‌آمیز و غیرقانونی» فیلیپین متهم کرد و گفت گارد ساحلی چین کشتی تدارکاتی فیلیپین را تحت نظر گرفته، تعقیب کرده و به آن هشدار شفاهی داده است
🔴
پکن از واشنگتن خواست از «شعله‌ور کردن تنش‌ها» خودداری کند و اقداماتی را که به گفته چین صلح و ثبات منطقه‌ای را تضعیف می‌کند، متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149643" target="_blank">📅 10:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149642">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKC8KTolNg8xSr_VZHJxPdM5QHAHrNXE8ogWlMRl9TOljDAJKUKt3m9dCOivKKQDkjHNyE1jHae7UwOAy-1QQx1lPV67nCC993ve49WUcrmuoWE7fQNKhqVgzA63PMbulkzdi4nbATz18wLv0u9D27Gr8AG8dz1SprbVwJSyXCgcfpiKHhsbb20nqV9FuYkaanYKd2x87kyvyVthTnK9aSWTDYjsrz-07ryQZhSFOmsmLr60kKkuzOGe7KAg7kXn6BTDQQYfCiFGtWVDlJ5M2du-1P7PsNa189_bihnR6KnwAedZba7pW47J64vor5eyu2Ysrzn9rD6f1XPTkC58oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی با معاون دبیرکل سازمان ملل در امور بشر دوستانه در حاشیه هشتاد و یکمین نشست مجمع عمومی سازمان ملل
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149642" target="_blank">📅 10:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149641">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سازمان هواشناسی امروز برای شمال کشور رگبار و رعد و برق و برای استان گلستان و شمال شرق سمنان هشدار نارنجی صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149641" target="_blank">📅 10:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149640">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هاآرتص به نقل از مقامات اسرائیلی : ابراز نگرانی نسبت به توافق هسته‌ای غیر نظامی دولت ترامپ با عربستان
🔴
این توافق به ریاض اجازه می‌دهد اورانیوم را در خاک خود غنی‌سازی و دیگر کشور‌های خاورمیانه را به دنبال کردن قابلیت‌های مشابه ترغیب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149640" target="_blank">📅 10:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149639">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کارشناس صداوسیما: ایران می‌تواند روزانه ۲۵۰۰ پرواز را مختل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149639" target="_blank">📅 09:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149638">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
فایننشال تایمز: ارزش ابرنفتکش‌های قدیمی برای نخستین بار از کشتی‌های تازه ساخت فراتر رفته، زیرا مالکان کشتی برای بهره‌برداری از نرخ‌های بالای حمل و نقل در خلیج فارس هجوم آورده‌اند
🔴
بازار کشتی‌های بزرگ حمل نفت خام، به وضعیتی «دیوانه‌وار» رسیده
🔴
قیمت نفتکش‌های ۵ و ۱۰ ساله به شدت افزایش یافته
🔴
چندین کشتی که پیش از سال ۲۰۱۶ ساخته شده‌اند، با قیمت ۱۵۰ میلیون دلار یا بیشتر فروخته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149638" target="_blank">📅 09:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149637">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فرانس پرس: عربستان مدارس ریاض را به مدت یک هفته غیر حضوری کرد
🔴
هنوز هیچ توضیح رسمی و فوری‌ درباره علت این تصمیم ارائه نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149637" target="_blank">📅 09:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149636">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
آنیتا آناند، وزیر خارجه کانادا: «اینجا در سازمان ملل متحد، کانادا در همین سالن مجمع عمومی سازمان ملل، قطعنامه‌ای درباره حقوق بشر در ایران را رهبری خواهد کرد؛ زیرا ما قاطعانه در کنار مردم ایران در برابر سرکوب و در حمایت از حقوق بشر، کرامت انسانی و خواسته‌های آنان برای زندگی بهتر ایستاده‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149636" target="_blank">📅 09:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149634">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید:
«ما در بریتانیا بودیم و من در یک ناهار با
دونالد ترامپ و کی‌یر استارمر
حضور داشتم. دور میز نشسته بودیم و همه مشغول ناهار بودیم که رئیس‌جمهور ترامپ ناگهان شروع کرد به انتقاد شدید از سیاست‌های استارمر
🔴
ترامپ گفت: «سیاست‌های شما اینجا خیلی احمقانه است. باید مرزهایتان را ببندید. باید افرادی را که در کشورتان هستند اخراج کنید. من کشور شما و مردم شما را می‌شناسم. آنها از کاری که انجام می‌دهید متنفرند.»
🔴
استارمر فقط آنجا نشسته بود. این اتفاق در خانه خود استارمر و در کشور خودش رخ می‌داد؛ ما حتی در کاخ سفید یا در خاک آمریکا نبودیم.
🔴
البته من از این صحنه
لذت بردم و برایم سرگرم‌کننده بود
.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149634" target="_blank">📅 09:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149633">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
انفجار مهمات کنترل‌شده در دزفول خوزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149633" target="_blank">📅 09:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149632">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf9976c70.mp4?token=feTzfQWroVvVBlkvDD9WdOmQ9_wrds4UoYmpHzOjF4zoZ_uoU_UpeAaYeIw6BUyyZgsZj8GUJUOL1tWw1tl_SJ6u_QIjj3a-2A1_AbW3hoQEplm-iwDwYHx6yoRMD9qh8Ja7AZQKMTWNAU8vbVGAA1j_glsKJb6GF1EcYYnk0AjcGY2W7MV0Vl2K5AYUyPljzlLcKmnt3fz5846u_IJJOBYD6yNsKZu1OKWBK4ufRDneI4zCKqYkdgAskk08A1Wn_yxsDlP9KVyOB9YMQkeH_0rnuXheN-q_XQ72tCMMz_D1W1PgSM-quiZtEI-gs8Z0Kj1uw02pAicNjWbtMdObHmGmXGArTl7YDGeALypbZfiyXpo52nbE8S9vsW_O6Wca-6ZYOMal6alQ74DLouh0l0UScjfmHKU85pmD0_o_4OKZ_Hluik9IsftiptnSgWdrPv0sZaI7LRKVK1mXk87Qu5yEVdlE3uEoKKH3t1opEKxwSBFWm_BI44gp0H6nu56M-BGqv-jSXgra59XTmlvPfA3heFjm-bZ03XQN6xztbd3TPJ1Udebnlu4EJveiahU1G93utzdfU_CglJgrTShasKyZEztQB25FqdyQ9sZaitfaMiU5i2fJ2PqDkLS4CcvkpeQ64mfI4_TndDsGN93g5HVBfAauFt8XbjgX_b12mfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf9976c70.mp4?token=feTzfQWroVvVBlkvDD9WdOmQ9_wrds4UoYmpHzOjF4zoZ_uoU_UpeAaYeIw6BUyyZgsZj8GUJUOL1tWw1tl_SJ6u_QIjj3a-2A1_AbW3hoQEplm-iwDwYHx6yoRMD9qh8Ja7AZQKMTWNAU8vbVGAA1j_glsKJb6GF1EcYYnk0AjcGY2W7MV0Vl2K5AYUyPljzlLcKmnt3fz5846u_IJJOBYD6yNsKZu1OKWBK4ufRDneI4zCKqYkdgAskk08A1Wn_yxsDlP9KVyOB9YMQkeH_0rnuXheN-q_XQ72tCMMz_D1W1PgSM-quiZtEI-gs8Z0Kj1uw02pAicNjWbtMdObHmGmXGArTl7YDGeALypbZfiyXpo52nbE8S9vsW_O6Wca-6ZYOMal6alQ74DLouh0l0UScjfmHKU85pmD0_o_4OKZ_Hluik9IsftiptnSgWdrPv0sZaI7LRKVK1mXk87Qu5yEVdlE3uEoKKH3t1opEKxwSBFWm_BI44gp0H6nu56M-BGqv-jSXgra59XTmlvPfA3heFjm-bZ03XQN6xztbd3TPJ1Udebnlu4EJveiahU1G93utzdfU_CglJgrTShasKyZEztQB25FqdyQ9sZaitfaMiU5i2fJ2PqDkLS4CcvkpeQ64mfI4_TndDsGN93g5HVBfAauFt8XbjgX_b12mfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا: «در هفته گذشته، یک روز داشتیم که بیش از ۲۰ میلیون بشکه نفت از تنگه عبور کرد؛ رقمی که حتی از سطح پیش از درگیری نیز بیشتر بود.
🔴
میانگین روزانه در حال حاضر حدود ۱۳ میلیون بشکه است. بنابراین نفت و گاز همچنان از تنگه هرمز خارج می‌شوند.
🔴
مشکل قیمت‌گذاری امروز، بیشتر به ظرفیت پالایش نفت مربوط می‌شود تا میزان جریان نفت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149632" target="_blank">📅 09:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149631">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b927aa45da.mp4?token=dXsxJvxEJo5TNDABlHrxyfu9Qjkh2s9LxLT3rEVYnZ3lWHfzv9u7CdFO_o1pBTQkjsDXCgf5wgGJf24nMxFVElFALrgtXtx6IJkaE4GNiy0TkWSsxq1G-laxHj1bMlAwnTj_zSjrZeOad5O54puinnfPVI33lU8C8Ivbtwqu2ORLh_Jm-uFMtrHqxqSHVbUzT2OZukMDV5K_S1QwHMnn3jH6tdkABwO5Sc-DH54Vw2Jdzir1gOg10mFe7bdNdkNt0nC0qypV12ldjzJ_a6hMHCTqWEKT7ENo5kI0OZoVN8AgqeN3YayG9cZ5bHtoFsuD-3aE0MqGY7b05R9rjlPPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b927aa45da.mp4?token=dXsxJvxEJo5TNDABlHrxyfu9Qjkh2s9LxLT3rEVYnZ3lWHfzv9u7CdFO_o1pBTQkjsDXCgf5wgGJf24nMxFVElFALrgtXtx6IJkaE4GNiy0TkWSsxq1G-laxHj1bMlAwnTj_zSjrZeOad5O54puinnfPVI33lU8C8Ivbtwqu2ORLh_Jm-uFMtrHqxqSHVbUzT2OZukMDV5K_S1QwHMnn3jH6tdkABwO5Sc-DH54Vw2Jdzir1gOg10mFe7bdNdkNt0nC0qypV12ldjzJ_a6hMHCTqWEKT7ENo5kI0OZoVN8AgqeN3YayG9cZ5bHtoFsuD-3aE0MqGY7b05R9rjlPPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا: «تنها راه برای ساختن آمریکایی بهتر، انرژی بیشتر است؛ یعنی افزایش ظرفیت تولید انرژی.
🔴
آیا می‌خواهیم در زمینه هوش مصنوعی از چین پیشی بگیریم و از مزایای آن در کشف دارو و کاهش هزینه‌های مراقبت‌های بهداشتی بهره‌مند شویم؟ قطعاً.
🔴
اما این هدف به ده‌ها و شاید صدها گیگاوات ظرفیت جدید تولید برق نیاز خواهد داشت
🔴
این دولت تمام‌قد پای این هدف ایستاده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149631" target="_blank">📅 09:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149630">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تمام بانک‌های تجاری بزرگ در امارات متحده عربی و ترکیه انجام تراکنش مالی با ایران را متوقف کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149630" target="_blank">📅 09:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149629">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b9049d7e.mp4?token=knCj1xenBDibX6FSpBGM6KM_y7TeFq8BWELempnsTi28h46mkYyaXAeqMrCAyiLlWuEnPLL31Z7l4N9XCnjgJQrpk0XgdRzD430SIu4iPLVT6J_hzTgjywmnLT3vjoUHfhcUleYAzRwffJz1tqH0YXb0nr2Jt2MFW75mQYPoZv7sWVDI2XmqMVlFmH0o15I5eZj0FaF4whRzngC-ajbK6wIIB5sQ1_jHbSsgPYUuemjUeXOmwx6eyXnxgekhloChmzrrlonPjdnS6p4Ks7FmtIfvMfCh2TuOPhE4k2Je1TpH4ETbtUtC7k9rz_UIu3IkWZgLdVS4irsQ9al2ogcFIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b9049d7e.mp4?token=knCj1xenBDibX6FSpBGM6KM_y7TeFq8BWELempnsTi28h46mkYyaXAeqMrCAyiLlWuEnPLL31Z7l4N9XCnjgJQrpk0XgdRzD430SIu4iPLVT6J_hzTgjywmnLT3vjoUHfhcUleYAzRwffJz1tqH0YXb0nr2Jt2MFW75mQYPoZv7sWVDI2XmqMVlFmH0o15I5eZj0FaF4whRzngC-ajbK6wIIB5sQ1_jHbSsgPYUuemjUeXOmwx6eyXnxgekhloChmzrrlonPjdnS6p4Ks7FmtIfvMfCh2TuOPhE4k2Je1TpH4ETbtUtC7k9rz_UIu3IkWZgLdVS4irsQ9al2ogcFIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا: «ما هنوز قیمت‌های انرژی بالاتری از حد مطلوب داریم و هیچ‌کس بیشتر از رئیس‌جمهور ترامپ از این وضعیت ناراضی نیست.
🔴
او رئیس‌جمهورِ انرژی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149629" target="_blank">📅 09:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149628">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBeq3zaNuRpcWokRBPRE3PDBGgBO202ELbbXKKHnFlOXS7o38Yc8H_6RUIOOuPW7EWmDP7bCm5r-N_In6aotDDrNPF8vmPbs-BfLEYAFRbJBizu8h0Ad7UlpzbSNpCS2BIFSwe3hxKPpq1hstOk2jZ8WSISQsrQGEEgFpTK2PWC_OxpvsxoxKXkfAL0OBwZ6gs6jjOUw5RWKlPTMG1cUpBGht_9wkpA3EJJm3pwvq0F-DlLzN5jnnx6jNX6DnSAsxFVK3kaZrjhEwLmc0fnsjDCFXjPX1ODg_Ah2yqxnxj6FfYL35kCcdqWzmiZuaHIlYlBYX9Guyv2ODUe3AZaWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : «ما بهترین شاخص‌های مالی در تاریخ را داریم، اما رسانه‌های خبری جعلی حاضر نیستند آنها را گزارش کنند!!!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/149628" target="_blank">📅 09:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149626">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_RoAJKDISQ2LMjCe1eylrTdVXkFM_16jCAs_8yKnGVLkXZGIHsETQjyAsXHArAgqtNgOcQ3fzcCcYDfRNDShOFFn-5AIg53NKca8mCdbXEcSCX1NR-lup0lns3aPoMZT8kUJEKU_tGzHf78Hv6tSdQhsE3MhmMWsoT0RLS1dlS-Bv1Hk1cdC3HVamSj1vgZKtHzHGMFdObq27zq_Waheb824QF4lwUWh09SKYanSl8qDdLkbcKZJTtcNDFtQxpTw8G7KbR_Ac8nnjdyJNyR87opNsJuyk2O7VtLmwBIwwKv3-0BLf4t28cZyhShv_qzJSZZALezQaYTnxJydwf-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن‌پست
:
جنگ با ایران مصرف نفت و گاز در جهان را به شدت کاهش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149626" target="_blank">📅 08:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149625">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/B-IMmVElbE9yg_otjt4bpHixQRoUpkTQoEUdkIfXFyAggf5EZ6vQdnMsq8_ytlsKMjqfm_pCwZswcX_iOV_KC4Kv5yXeRKJZBQKyexG-rOJ93_V6ZSU_K7qZrw2sdYF4yZS7O3CDKR2OIYugZ7FwJru9H2tNs1a7El4Mooz8v03SWcGd6oujoKpF6C78dAnwiSQeW6_3U_h6bYrOaLtoH-6iNvVt8By3vkfXA_g_MclzyVjzX9AJkxGYyyTudvZHjdWLmZ6I0n6Q7UScHGA-WdegrqFO65yzhV2otX76GAzdy2Iq66XiuDjkJ-6W-QIKrPg4i5SFII3E7910ii4f4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیش از ۱۰ فروند موشک کروز ضدکشتی به سمت تنگه هرمز شلیک شده است.
🔴
گزارش‌ها حاکی از آن است که دست‌کم برخی از این موشک‌ها حامل مین‌های دریایی بوده‌اند؛ مین‌هایی که هدف از آن‌ها تغییر مسیر کشتیرانی در مسیر دریایی عمان عنوان شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149625" target="_blank">📅 08:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149624">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عراقچی: شروط ایران برای باز شدن تنگه هرمز تغییر نمی‌کند
🔴
هنوز پاسخ قطعی میانجی‌ها به ایران منتقل نشده و تهران پس از دریافت آن تصمیم خواهد گرفت
🔴
شروط ما مشخص است و هرگونه حرکت رو به جلو برای باز شدن تنگه هرمز منوط به محقق شدن این شروط است و از آن‌ها هم کوتاه نخواهیم آمد.
🔴
ایران هیچ‌گاه مسیر دیپلماسی و مذاکره را نبسته، اما از حقوق خود نیز کوتاه نیامده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149624" target="_blank">📅 08:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149623">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا : تیم‌هایی به نقاط مختلف جهان اعزام شده‌اند تا از کشورها بخواهند علیه ایران اقدام کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149623" target="_blank">📅 08:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149622">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-qH3c3HyEDuY_rShltkr68VeOHdUys1MzhEmU4l1H5EWM62JiUL-D10LnF-lRfxmsLRD0LXCb6RDs7PacEeNP3IAiYIK8lvQxuI8fZ9iLfB4bYoh4FFZGqq75S5CMC7BjbbFAn_rzeBsoZffWrX1K-9rRmruSFwok6gS_oqcXJX0hL3v17oMBlsTOi2pCR-UAl1wCfSfGKhLZfg98coZAsQCeoAjFkAXKmHNrgO3nJBNGZ3mGBxYDm7RUG-NwW7yrFZkfe99uLHXhK7nrJFRc9NBrtD_b2OG0bgu4YY1WCPPxx_5jc7GRK0y1JxCLEiQY2UPHI2np7hYS3CwdRRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: در انتخابات میان‌دوره‌ای به نامزدهای جمهوری‌خواه و نامزد های مورد حمایت «ترامپ» رأی دهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/149622" target="_blank">📅 08:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149621">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgI2-c44AyGQJAP5LAprHXarZPeu6jqg09Gd29bTPXVD-Kr34Ltpd6-Ri6fC5FOvo4l4-SHLg3o9Jo4rIe_1f1qj-rFAOgHCy68-BPY-iiC95S9cVZfa9ul6exNyNP0jimnjihHd7AXrBaFpjUxVviwBx-rmlmsZd6RxJfQqPigd_zp4iFYsAew_WitunNBDVQOUmo2ewCz3IagpL2S9_S0cEzz2B_kjKXtX8FW-GAw79XG_XUkCltGXplAtH40yowOtrTdb6Yr3D9aw0nHnQenfcvcJHkQEnYoUfuoXd2UOh3mndik5bxkD85NBvkdvGBHRxD7PzX5LnEaNj7JjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تام کاتن، سناتور جمهوری خواه: یک درگیری جدید با ایران در پیش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/149621" target="_blank">📅 08:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149620">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJPeTjIoODZM6oYiI74PUjowOB-wt4id46bS9qv-U0pRUaTeDsoJLTX6hFFOrQwwlFUuLB0jv_z3cZ7LB7H4TkdutCMebeVXeltLmUsqkdfQgePwFlZrSekpMLJxTzoHR0Sp8SQtnWGlz0NhNmrWbGHBVdHPLmORNzuZDuSunGuq7cl7iVAOFJqxPyqtfXmKwB-nYpSTybAkr5TOG8RvsJBV2YjtM6UdAHiXae2TZd7MCF488XOZe6Ji4Axs2UjZyjoB4xpfiVfTKAMjKqkQv3Cwi2GIySA3-kcMCRtuQAHgs60Pm-NoonLDwX5Jwb9ArX0OuUrQNJ0SiwrryqmHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بسیجیای دانشگاه تهران قرار گذاشتن از امروز تا زمانی که دانشگاه باز هست نذارن این پرچم زمین بیفته و هر بار یه دانشجو میاد نگهش میداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/149620" target="_blank">📅 07:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149619">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
خبرگزاری اورشلیم پست:
عباس عراقچی، روز جمعه در پاسخ به سؤال خبرنگار فاکس‌نیوز درباره اعدام بیش از ۹۰۰ شهروند ایرانی در سال جاری و همچنین شکنجه و زندانی کردن هزاران نفر دیگر، لبخند زد و سؤال را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/149619" target="_blank">📅 07:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149618">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea1ac8cce.mp4?token=UEgh3cqbO0SO39J4ctG7ORektAxGGPE-I0Pw55Z74XRhC2g60oPDwV-hCacqDpTrTEmkbdydzfGezb_OmQBZd77_KNcXvfcFpXrjqpfCErP7CytsybkBYmLjxEDoJ9Fbrdj303bTF3hEZa-sg3M1spsAclI8ABMvQ9yB99e36F9NonXiLWcTBKvTlR-hv2RQMXomXjZCORMXXHiQoNpEhDMp106f_GrQw5Ovvk5tA92WhkTCxk9wlVdvtJ42z6KMAIfhBt2VUqXndFHfOQcQ_-EDEUk_tfX2zNBwgmoXGzTMxAJZy5s78XpSw17pSB8rQwGlL52nINsBPliZsARkz7IiAr-6btNZTsGIr6hyImAOCy6vFNcMJssWWi9egoWg1ZFOa65QXTyorWym84ds97wYWwkiArFY3-4m6rJppfe9Msq422DJhPsNdNiP4z6DzCuzFocHDzC3uATP7ulFQE7iYBi5oSRi2D1B40J4XjQaiNy-1bE7HmkXquVINsXXrDHoBxfEy6YF-uuYPOpC6EHeXeHsTV_xm42ZPHWh9S4tTgoMwq2o5qgoafBcSNga98AMx15PzqVZ2eIzefu7Nry3WICukzOaC0y3cjPA8Q3jMCU0u3l5DoV8AloiAAdt3u1Fbet9sfiZlkgidCPd_BYbBU6Cq_9q8BU42hqvA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea1ac8cce.mp4?token=UEgh3cqbO0SO39J4ctG7ORektAxGGPE-I0Pw55Z74XRhC2g60oPDwV-hCacqDpTrTEmkbdydzfGezb_OmQBZd77_KNcXvfcFpXrjqpfCErP7CytsybkBYmLjxEDoJ9Fbrdj303bTF3hEZa-sg3M1spsAclI8ABMvQ9yB99e36F9NonXiLWcTBKvTlR-hv2RQMXomXjZCORMXXHiQoNpEhDMp106f_GrQw5Ovvk5tA92WhkTCxk9wlVdvtJ42z6KMAIfhBt2VUqXndFHfOQcQ_-EDEUk_tfX2zNBwgmoXGzTMxAJZy5s78XpSw17pSB8rQwGlL52nINsBPliZsARkz7IiAr-6btNZTsGIr6hyImAOCy6vFNcMJssWWi9egoWg1ZFOa65QXTyorWym84ds97wYWwkiArFY3-4m6rJppfe9Msq422DJhPsNdNiP4z6DzCuzFocHDzC3uATP7ulFQE7iYBi5oSRi2D1B40J4XjQaiNy-1bE7HmkXquVINsXXrDHoBxfEy6YF-uuYPOpC6EHeXeHsTV_xm42ZPHWh9S4tTgoMwq2o5qgoafBcSNga98AMx15PzqVZ2eIzefu7Nry3WICukzOaC0y3cjPA8Q3jMCU0u3l5DoV8AloiAAdt3u1Fbet9sfiZlkgidCPd_BYbBU6Cq_9q8BU42hqvA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
وزیر امور خارجه کانادا:
موضع کانادا در قبال جمهوري اسلامي ایران کاملاً روشن  است. تهران تهدید اصلی صلح و امنیت در منطقه خود محسوب می‌شود. این کشور هرگز نباید به سلاح هسته‌ای دست یابد.
🔴
تهدیدهای آن به حقوق کشتیرانی در تنگه هرمز، یک توهین مستقیم به حقوق بین‌الملل است.
🔴
کانادا از تمام ابزارهای در دسترس، از جمله تحریم‌های هدفمند که این هفته اعلام کردم، برای مقابله با رفتارهای نفرت‌انگیز رژیم ایران استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/149618" target="_blank">📅 07:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149617">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPAYONET | VPN |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ59hp4dbvkBOwS4NT_mriuISRaLX55CyqaWzY846CJmoQZ_PkolPMD6W5iHLrR9rHCJtrIT_zzxLj55TuL6vNiR5FzH6NhT-tDAK_7Cn4I5M5KhvfJ3cTA9llMJ2lyTYnEA1M5-EZv0Mb4wreJ38N1_eDmUEs3yzdXFVjLO6miXVCZrgDPp49C3Ev9WPX7P6NDe8VYU2ILQVZs1oHfB5xi1W__sxXXMzOUGASUH01-cseWi-KFhf2VYCybwsstQqY-QlFOPpokfo89ni3XUxdIggQjrJORtMvnXXeF2PDIQ1NKcS525D_ApsUN5ZHK04E9nHTWiNZw8MAgdwJsOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
☄️
مناسب شرایط جنگی و اختلالات
💬
پشتیبانی تا آخرین لحظه اشتراک
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
👾
نامحدود تک کاربره  | 79 تومان
💵
👾
نامحدود دو کاربره  | 99 تومان
💵
👾
نامحدود سه کاربره  | 119 تومان
💵
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
خرید و تست رایگان از ربات
⬇️
BOT
🤖
@Payonetvpn_bot
ID
✅
@payonet_supp
❤️
CHANNEL
🫡
@payonetvpn
🔺</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/149617" target="_blank">📅 01:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149616">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
خبرنگار اسرائیلی:
حملات امشب سپاه پاسداران به کشتی‌ها در تنگه هرمز گسترده و کم‌سابقه بوده است.
🔴
گزارش‌های دریایی از افزایش حملات و کاهش شدید تردد کشتی‌های تجاری در تنگه هرمز خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/149616" target="_blank">📅 01:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149615">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHrAcdI3UL53YL8ddcCtt04nXdz_x37D6Ed0sUlYttD2-2o5CrCkB8Coo-qwpKqCFpEGEXFNoQE4Tm6DET-BPXF2nnI8C2C017WhRlE8j6Tg3exlma1Rq5uxuePmTGQHqs-bgV0WIwgQoBsqTwfaH2J1thS_5iirKuQIy-H2wTM-6ZgW-crXzLTAMWR0nfyHF1CXzAaeYBLMUJ1mtv8Ds3AZ2bYFtSflicECV1D2lkw0iL1-FhQ7Lf3Ekn_xZlb-uUQ9l8mjzb5jjR-J8jP_LoAEUD4wsCk5yf85jZHS25s3Ev_ZAHRK0aAi472L9KKNvD50alKFyueVDAH-fepyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توهین عجیب به پزشکیان در ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/149615" target="_blank">📅 01:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149614">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
نیروی دریایی سپاه: در جنگ جدید، شناورهای دشمن در اقیانوس هند هم امنیت نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/149614" target="_blank">📅 01:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149613">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vixZ0CqyOjkK_ePtIosjNgncDr-PyzbhtICLXzNxtMrzkLsjYjlOKUagn_FI8y_T32ZrUAYaoEfICn3Ao0TLYWkwcOMFE8h9Ega2jh_yxQPzq4qIKxJouznPowoPwA2pcXLDafiPhjeBSvz6yve_9QdJwoTqeRLu-FPpu9YhHQF-cKKsWYPdlJIKj-GDDJhtX1ZNMot_d67zcrTGGj568Ev6tQHwsCFdLpPtl-bBX-4aBaGSwKplqPwk1aDNX4sReWBzOOhwE89y2knedbf1A6552pP0lx8W-vH_rd3lm-fYgXqR2Jk-YQ--hp-JGcdLn_TWokIgeW0xlRUhVAraoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی:
از شروط خود کوتاه نمی‌آییم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/149613" target="_blank">📅 00:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149612">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b0c9e9f6d.mp4?token=BXgitTZjZTCwQJ5UXerVTipn38p1Ho1kPpP6U8z9fw--iRXFbKwiQiZGoZFLfvTo9a0pKMGJ5SJvETRDxhFHN4tkmAYifoQxEs0hY287uZi3hfs9Gt0lXkHwl0IoY8sJuB9kc8jJjOHnurXh8rjDTOB55SjPW1hVNDGA0fnWQjBaUexz_xrGs2kMoS-eIFUHB1gg9wsAcPPpuhIXrU_Qt21wWklJhu9aQfR9bwg00wUEcX4C0b8q6yfG7OwMlmlEOzHoCrwUE1dG9R4_IFhne38kGjZC-9fTB_m0uekeT0kjZAs_fXtnYmjnrecfViTYq0ZDKdmQEo4l0rm2-qZsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b0c9e9f6d.mp4?token=BXgitTZjZTCwQJ5UXerVTipn38p1Ho1kPpP6U8z9fw--iRXFbKwiQiZGoZFLfvTo9a0pKMGJ5SJvETRDxhFHN4tkmAYifoQxEs0hY287uZi3hfs9Gt0lXkHwl0IoY8sJuB9kc8jJjOHnurXh8rjDTOB55SjPW1hVNDGA0fnWQjBaUexz_xrGs2kMoS-eIFUHB1gg9wsAcPPpuhIXrU_Qt21wWklJhu9aQfR9bwg00wUEcX4C0b8q6yfG7OwMlmlEOzHoCrwUE1dG9R4_IFhne38kGjZC-9fTB_m0uekeT0kjZAs_fXtnYmjnrecfViTYq0ZDKdmQEo4l0rm2-qZsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی معناداری که ترامپ ری پست کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/149612" target="_blank">📅 00:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/149609" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سخنگوی ارشد نیروهای مسلح: قدرتمندترین ارتش جهان مقابل نیروهای مسلح ایران زانو زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/149608" target="_blank">📅 23:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
البوسعیدی وزیر خارجه عمان : امنیت کشتیرانی در تنگه هرمز نیازمند همکاری همه طرف‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/149607" target="_blank">📅 23:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کارشناس صداوسیما: ایران اصلا به نفت‌کش‌های امارات شلیک نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/149606" target="_blank">📅 23:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
اردوغان: جای نتانیاهو پشت تریبون سازمان ملل نیست، بلکه در دادگاهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/149605" target="_blank">📅 23:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پزشکیان: ما می‌میریم ولی سر خم نمی‌کنیم. آمریکا و اسرائیل فکر می‌کنند با این فشارها می‌توانند ما را ساقط کنند اما ما با قدرت بر همه مشکلات غلبه می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/149604" target="_blank">📅 23:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بیل گیتس مالک مایکروسافت: بزودی ممکنه هوش مصنوعی اونقدر قوی و خطرناک بشه که حتی باعث کشته شدن ۱ میلیارد آدم بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/149603" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD37q8aJrJxvJVT6R3fvMDKvTI6vCUr-dj2muPUI53R2LaOXWn2CrNmBcGdkArLd-NaPFnyMVpufKxMbtTc-bYG_b1XO7s2iv77JDp7lSrYXBmrMuGRD76EC-z-NL5MJ4m7_dkjo4Rdp8EG8Hra2N3_SlyFL0Cyz5E4Dav5Hn6eeZIbhOGacOf6sIzQp6wi6Dx_G5qFP6pUQxvo4ptNLFx6a7jVveXSQE5920ftqBK0qIkYLV7oD5zehEanlztT51BM9oB8fbb2rKODtU4IpSuwHF93vLMFTv_t6s5u_nD3kolbNkxQw6C8oYwNGC6uOJbWCo-hEUMKwyS8ipsDTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: امروز روز بزرگی برای کارگران صنعت خودروسازی آمریکا و خریداران خودرو است! من به تازگی استانداردهای جدید بهره‌وری سوخت را تصویب کرده‌ام که دستورالعمل احمقانه مربوط به خودروهای برقی که توسط جو بایدن و پیټ بوتجج مطرح شده بود، را لغو می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/149602" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149601">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHsK_aQwcs3IaaCTPFllUXksGUlBm_mvtDKQBINIx1W1AdXcUYQsGjZGU3SyM4m8Gd0dAKldMqnxlLaR5AlLVGNr3Xt---AAEXJQ3NgbmP47ExhriQWmzn1Daq6zpj8RstaanfHqL0YSLVN97bViThawPd-p2tKzGK3nmuTBe-Wd7Zrz2h_treh9b2LJVmO0DYZ_yrXFpfP4VBOkjn3UkDLT9aGJNmZF-XbLYR7OF4oIBnM-eGMJFBhTL0Aw2Op4dh67sKLxqsLJR0JPa1Smu-LOvyY6xIdBPZHh2F9aKLIehTS54bfighHFoALpH1ewqHZZ-NBjlIMiEDA1yhTcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت اینترنت کشور
🔴
در حال حاضر اینترنت کشور به‌طور کامل قطع نیست، اما اختلال و افت کیفیت در برخی مسیرهای داخلی و بین‌المللی مشاهده می‌شود.
🔴
وضعیت: ناپایدار / همراه با اختلال
🔴
اینترنت بین‌الملل: دارای اختلال در برخی مسیرها
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/149601" target="_blank">📅 23:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149600">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پزشکیان: ما و یمن در حمله به خط‌لولۀ عربستان دخالت نداشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/149600" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پزشکیان: بی‌هیچ واهمه‌ای آنچه را که اعتقاد داشتم در سازمان ملل مطرح کردم، شاید اگر رئیس جمهور آمریکا آن حرف‌ها را نمی‌زد ما هم این حرف‌ها را نمی‌زدیم
🔴
برای این در تریبون‌های بین‌المللی صحبت می‌کنیم که دنیا فکر نکند که از گفتگو می‌ترسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/149599" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پزشکیان: زمانی که به نیویورک رسیدیم سخنرانی ترامپ را به ما گزارش دادند، که حرف‌هایی زده بود که شایسته خودشان بود و در نتیجه نوع فکر و پاسخ ما را تاحدودی تغییر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/149598" target="_blank">📅 22:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پزشکیان در گفت‌وگو با شبکه الجزیره: از توافق عربستان، ترکیه و پاکستان استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/149597" target="_blank">📅 22:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
پزشکیان: نتانیاهو نتوانسته غزه را وادار به تسلیم کند، حالا می‌خواهد حکومت ایران را تغییر دهد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/149596" target="_blank">📅 22:30 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
