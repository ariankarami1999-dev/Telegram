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
<img src="https://cdn1.telesco.pe/file/iNJq6HRv1iSh9syM0L2i4vFiqmQcSCKhVWbtLGsijnwbmG_AjurnhsxAQAPlOBVZ2nhcrl153S3q5eKl3ERkqhEUs2ablaVfmcTW1KKMidqNIpFW-_69-ZPILirI2muPOagoT7p0lj-IGBVXv2l1Pyi-lhjf_a-OEla2KkqebA9IbsAFga4K2-fR_bwuujT8LManFk68jFJRsdDJmnC2oyuI0SvKNtvf5qpliBPMpcvtdLF6f1hGDG3xpbB_WNS_eGZDSsyu02qCJWL9A2vaIEcEsDO9Z2vRzG2D8yruYkdycTXqC7hiTq4111aTTpRBNaXnSg03TMNBCIUkq7mpgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 03:32:20</div>
<hr>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TY9zl9n0YPQeZyGBnZBTCPqGMFyKS1v2TzMDCOKvuyLo7RcA_7g9eFLR7bblhb_s5KWwcdAhDYtIf8PNMbS71Kj_llKAj2C5E2c-tiluz8D0lpz3ubVETdYUTWAF7wDoBJ8NzBEyEEowptS5zvR3SjwqYL26akt12x84bxE8kOUgBV_CAJJhezUFbP1K3GqEpw-kFaE8xyUMM6newef8yib5kMpt7buonLJJfg0Q_KmWxHUu3ASHdlNZQj_MyafnkJcMeVKfvKHgkSImMs5yg0jnIdK1Y8rHJ8K4pBiRcYSPf04GhLNvA0SxoKFg0NOXkvmPl4BSiL0YzVx9mVOM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس در نخستین ساعت بامداد دوشنبه هشتم تیرماه به وقت تهران (عصر یکشنبه به وقت آمریکا) به نقل از یک مقام ارشد آمریکایی گزارش کرد که ایالات متحده و ایران موافقت کرده‌اند که حملات علیه یکدیگر را متوقف کنند.
براساس این گزارش دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر دیدار کنند تا به اختلافات خود در مورد تنگه هرمز رسیدگی کنند.
براساس گزارش باراک راوید یک مقام ارشد آمریکایی گفت: «ما تصمیم گرفتیم تمام فعالیت‌های «رزمی» (جنبشی/kinetic) را متوقف کنیم».
همزمان یک مقام دیگر آمریکایی هم به آکسیوس گفت که هر دو طرف «فعلا» عقب‌نشینی خواهند کرد و «شناورها می‌توانند آزادانه حرکت کنند» چرا که قرار است گفتگوهای فنی ادامه یابد.
هر دو مقام آمریکایی و یک منبع سوم آگاه، دیدار برنامه‌ریزی‌شده برای روز سه‌شنبه را تایید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/VahidOnline/76734" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KwYUk42wOTn_BCnw5TbkGncUtzrXbzzGzwHqOZF5UrOZ8qkvoqqXuWtiOpHw_np-er96r8ajdrQauaX3uWDSobDtMy_KLY9ZU_2piT_XjztlKxVEyQD386FgZ4FXTCBIQYj_XOX0_aHUl70oKY2gdOc2eYu0-ZnPASJBWoT5xtc1WFqQY3dh0Is7IZKrBWjdEH7wIk5JnEiq80PLcqJGO0ixyaNNhyITUFDBUopBpZ23z74kybILr3riBbu9_fC2yKpgt0c6f4g3bd05D_jWoLE5PCArMV4CNjtOpq1IfeYz4uIuviUH9QsJ2ykX5Gbiid6IAqQ4eau1-PSEoNN1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال به نقل از منابع آگاه گزارش داد که گفت‌وگوهای آمریکا و جمهوری اسلامی که قرار بود آخر هفته در سوئیس از سر گرفته شود، در پی از سرگیری حملات طرفین به تعویق افتاده است.
@
VahidOOnLine
مهدی فضائلی، عضو دفتر حفظ و نشر آثار رهبر جمهوری اسلامی، اعلام کرد که جمهوری اسلامی در مذاکرات فنی برنامه‌ریزی شده با آمریکا شرکت نکرده و این گفتگوها لغو شده است.
او شامگاه یکشنبه در گفت‌وگو با صداوسیما گفت قرار بود امروز مذاکرات فنی برگزار شود، اما ایران به دلیل درگیری‌های چند شب گذشته از حضور در این نشست خودداری کرد.
به گفته فضائلی، دلیل دیگر این تصمیم، انتظار تهران برای روشن شدن اجرای برخی شروط از سوی طرف مقابل، از جمله امکان دسترسی و برداشت از پول‌های بلوکه شده ایران بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76733" target="_blank">📅 20:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qkr9BZo9npzdE6zmliRTf0TkgTpdbOxnDBKpM493pcHFOeIl--dTScRRt6R7xryIGoYela7ZEWuEfSczEYL7eh3I5Bat2D7fMlYV4-ZhkQ3nrwHacgS50OtFEzBOTQZJ1ZelPGASRExyHk1Lhj_Uy7xZ_Ue5C9CAuP962vo-TYrUWgJT5cl1UlYgQ0mHD3f3FJQW72k3ifIf1b1qJrh79NuFlpUP6cLKkHzuMVs46goLcie_vkKQatd-GSo4EtTPwCLg6DWQZwlY9VVFIfG6Gg1y9cNKfgJssgVDKGDgPsV9SgCi5IrfQpziJJrrBc4Yrg75ck8FdzFfgUurn0Hdvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDmm1FcJIdBLm2neDt6rQ_fZqqS96hz0RvYCcXswN2z6SraePFnT1G4i4muAYCKka0t69Rp1TQHl49T9AmGdarU962asu628YLbwhzJhc4SEmYswDL_nVvU6ePKpxevc_5cl9L_qTRrVoR_OWbUXKx_fe_PLnnYuovuTz0pSvA4KmebqJZzNq35rsc2EmUt3tE0RYxjiruPpvdpAAslYn4q2T_FwjAwsbEaj2d-9HgI-K_jjHLVRRqLcEWHFB1RZW3oFpH9OprhxdA_nEGFxVsunU0ir5aWH30N3qfmaPES4ztuJLzOkizArEp8yghqnziSx0YksQzGpEfnpoHwwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZUOn23ZwYz_T_2qTFOerTUs_d0RC_u8MpXdy8zFsGWrIsH6KJhCMWgDrKTqZ3RPc0svWTd5THE_b2WoomAtSwwD0eLy3Pynz4qMcEmdL0Xlqhhg8izxtx2PfJ6MSIl6UImJkiNVCzXvBrck-eOOoXng1kMJYmYpA6XLU-xwn31UwRBmeI-R0bYtn4gCnB4iBtXchjIFZVXYytaWXRkgbvSNyzs1o0Dz6-K7S4SgL7VAs7G3HGA2_0kC4Zc-Y_btFJpkLfuK7ocvEsx1_S7nIRjd5KCS2pqt0pg4tWqHyiyzB-RswpSND5m7Trv6DjNK3xYbec1MOTOqx5LXzg6EJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بحرین گفت که یک ساختمان مسکونی در استان محرق هدف پهپاد ایران قرار گرفته است اما مجروح یا مصدومی گزارش نشده است.
تصاویری که دفتر رسانه‌ای پلیس بحرین منتشر کرده است خساراتی را به طبقه فوقانی یک مجتمع آپارتمانی نشان می‌دهد.
ایران بامداد یکشنبه اعلام کرد که به تلافی حملات آمریکا، پایگاه‌های آن کشور در بحرین و کویت را هدف قرار داده است.
بحرین و کویت این حملات را محکوم کردند.
بحرین همچنین خواستار جلسه فوری شورای امنیت برای پاسخگو کردن ایران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76730" target="_blank">📅 19:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQa3LjSr4Im4JMHce5tg4H0sFqZu3g0hr6zql-PmUkfcPwHcMKVae1gdKDaTWQm2oDKxk4w_nuYl0-EXQs08_Uhz_McXDv_g5JrA_xOqxyi7Z9ZucHRPxWBZkQ0pXxP6eTtAMhQSOgBqvYeJyt_SAOe98Fb25baZVf1smSseOIVdK25LLlLN-K0SlH4XU_Lqm0A3Oo_mCnUwC6sVKCEj4QVccXH6rSSflYLxjj3X_N0N-qJiSKahyvkjh1f-9rcmvV9QGhHv31S0P10EkTkMPV8KyKCOsIgs2WvJt2vil_P9zg-cZQgxoGxtCaR5oJ-7TtpV4VlI6BlZmJal4Usuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمت دلار آمریکا و دیگر ارزهای خارجی در بازار آزاد روز یک‌شنبه، هفتم تیرماه، هم ادامه یافت.
روزنامه هم‌میهن خبر داد که قیمت دلار در بازار آزاد در روز یک‌شنبه به ۱۷۲ هزار تومان رسیده است.
این روزنامه قیمت یورو، واحد پول اتحادیه اروپا، را هم ۱۹۴ هزار و صد تومان ثبت کرد.
روز شنبه، ششم تیرماه، قیمت دلار آمریکا در بازار به ۱۶۶ هزار و ۷۰۰ تومان رسیده بود.
این افزایش قیمت بیش از پنج هزار تومانی در بازار دلار در حالی است که در پی امضای تفاهم‌نامه میان ایران و آمریکا، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان هم کاهش پیدا کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76729" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGTRxgValmvHMu66nVO2SEV3PZNMgzKL9-fcdG2swzWiicZZeEXPD0F5oF-ZznAzCVDbRx_FIQDG5clAmsmloAwPdU7-xmYoYqBC_tX7SG7iFWCpoMDvMAk5T6WFqwoLkPbtKImbg32NPcKjVakoisuozjQh8b8eEbblWrHAtFMVi0pFoKokbCmZZcinEIJk9MLJm7no0CPCL-K27PJymUJwy0dB8VwsCcTVVTMBOzA-96i_qP7TSAUYy7PfcvcnFwVDbeB6PhnH8hBNDWk5cCwnTPoERmnnAoAW6AnPwlwf2cV4D1hbWNcbjc2rl3o-6sYsm8bLl-lvTBEd8NZjbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، سومین رهبر [اعلام شده] جمهوری اسلامی، در پیامی مکتوب به مناسبت هفته قوه قضاییه، از دستگاه قضایی خواست پرونده‌های مربوط به آنچه «جنایات آمریکا و اسرائیل» در جنگ‌های سال‌های ۱۴۰۴ و ۱۴۰۵ خواند را با جدیت در محاکم داخلی و بین‌المللی پیگیری کند.
او در این پیام که به مناسبت سالگرد هفتم تیر و هفته قوه قضاییه منتشر شد از قوه قضاییه خواست رسیدگی به پرونده‌های مربوط به جنگ را تا صدور و اجرای احکام ادامه دهد و مدعی شد چنین روندی می‌تواند از تکرار این‌گونه اقدامات جلوگیری کند.
مجتبی خامنه‌ای از زمان [اعلام] انتصاب به مقام رهبری جمهوری اسلامی تاکنون در هیچ مراسم عمومی، سخنرانی یا برنامه رسمی حاضر نشده [و صدا و تصویری هم از اون منتشر نشده] است. سایر مقام‌های حکومت تاکنون توضیحی درباره این موضوع ارائه نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76728" target="_blank">📅 17:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=HTStgG_WRlT4NQI7vvZnnA_1MYmcVLQAPnfNkJtbGtzpsTF5iJiC8o9BH2jgsJAQuptjQtuNIJHTuxI5YIgFJpPI8mk3P5XEd6lTCac1ByILruhfLyeHKQgwxZMpG8SfG3FVoFYMho8DifLw52ioUJGzjwFeEaXcLNNWxYACwk1BobXOuWPq8cjQq-mXykfscqr2qzArqKu4JA9L30v-U2qNmvPCGh4jM2MJWFfhlL4OmG1GzCjc49VOxtkGtZi1XRrt7bh-TwOhWbbj4N2IvMhNxkKMBv5NpswVzO-NqvKWP42sBg1xNAW2NlLZOJe3k4BC1TUXE5iCOBYOHNZFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=HTStgG_WRlT4NQI7vvZnnA_1MYmcVLQAPnfNkJtbGtzpsTF5iJiC8o9BH2jgsJAQuptjQtuNIJHTuxI5YIgFJpPI8mk3P5XEd6lTCac1ByILruhfLyeHKQgwxZMpG8SfG3FVoFYMho8DifLw52ioUJGzjwFeEaXcLNNWxYACwk1BobXOuWPq8cjQq-mXykfscqr2qzArqKu4JA9L30v-U2qNmvPCGh4jM2MJWFfhlL4OmG1GzCjc49VOxtkGtZi1XRrt7bh-TwOhWbbj4N2IvMhNxkKMBv5NpswVzO-NqvKWP42sBg1xNAW2NlLZOJe3k4BC1TUXE5iCOBYOHNZFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یک‌شنبه هفتم تیر در کنار همتای عراقی خود به آمریکا هشدار داد که «ایجاد ترتیبات موازی» برای تنگه هرمز «صرفاً به پیچیدگی اوضاع، افزایش تنش‌ها و تأخیر در بازگشایی این آبراه حیاتی منجر خواهد شد».
در پی امضای تفاهم‌نامه میان تهران و واشینگتن، آمریکا هفته گذشته مسیر دوم را برای عبور کشتی‌ها از تنگه هرمز معرفی کرد، مسیری در نزدیکی سواحل عمان که از دسترس ایران به دور است و می‌تواند رقیبی برای انحضار ایران بر این آبراه باشد.
در واکنش به این اقدام آمریکا، سپاه در دو روز گذشته به دست‌کم دو کشتی حمله پهپادی کرده که بلافاصله پاسخ ارتش آمریکا را به دستور دونالد ترامپ به همراه داشته است.
در واکنش به این رخدادهای تازه در خلیج فارس،‌ عراقچی که برای دیدار با مقام‌های عالی‌رتبه عراق به بغداد سفر کرده روز یک‌شنبه در نشست خبری خود با فواد حسین، همتای عراقی‌اش، چنین گفت: «بر اساس این تفاهم‌نامه و پس از رفع موانع، تنگه هرمز ظرف مدت ۳۰ روز تحت مدیریت انحصاری ایران به ظرفیت پیش از جنگ باز خواهد گشت و مسئولیت اجرای این ترتیبات تنها بر عهده جمهوری اسلامی است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/76727" target="_blank">📅 17:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7lAbN--qcfrejHXuBe0d2xz1VGNbtfGjQn0RLUCfzDpPNOBEH5eM1YZqF9DmBZy7ljd-NvjfD1f2WDV7dDmtKxTwJYa0wTUBY76ethNaA7gEw5P4qo5fl0Zgwt68aiFRtRTkzkiDLO1MLc6r0bdb2TrHQ4uvmOHCYMA57ktbTVQ8ds12gMlVygEDxdgSEnwUpcoSmXFG5u4zMjMRjeSo2o0NmFuRjcNYu_IIUiPreJpAG4eHSLrEthCihFTfROEaqnOEJUDKUC1d1PFsw9_-oa3XTPX6qnxXBbETEGZb5dAbSZ1IryVRrvmlvIvLjQ1tgjmfANy11noBYCeNbQY0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تقی چنگلوایی» فعال محیط‌زیست و داوطلب مردمی اهل بهبهان، در جریان مهار آتش‌سوزی گسترده در «کوه بدیل» زاگرس جان باخت.
تقی چنگلوایی هنگام مشارکت در عملیات مهار آتش‌سوزی، بر اثر شدت آتش و حرارت بالا و در پی انفجار دستگاه دمنده‌ای که به دلیل کمبود امکانات برای اطفای حریق از آن استفاده می‌شد دچار سوختگی شدید شد و جان خود را از دست داده است.
رییس اداره محیط زیست شهرستان بهبهان در گفت‌وگو با شرق نیز تایید کرده است که آتش‌سوزی در منطقه شکار ممنوع بدیل واقع در شمال بهبهان هم مرز با منطقه حفاظت شده خائیز هشت شب جمعه پنجم تیرماه شروع شده و هنوز هم ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/76726" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">میثم پیرفلک، پدر کیان پیرفلک، که در جریان اعتراضات «زن،زندگی،آزادی» در ایذه کشته شد روز یکشنبه هفتم تیرماه پس از حذف ایران از جام جهانی در واکنش به حرفهای رامین رضائیان، نوشت: «خدا بخواد نمی‌شه که نمی‌شه آقای رضاییان.»
رامین رضاییان، پیشتر گفته بود: «اگر خدا بخواهد پیروز می‌شویم و دل مردم شاد می‌شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76724" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nM3CTewg0mA2lDxO6eK_ts-IzKHREjPDdGFg2bkDd-M7yifFaRgCmU1EtssSOYQ83nJ3xA7b8h2Nv2mAE-hmdAOuOzWIy7rdl-aBGtMn1KkXXVeLndnF0o8dXb6bke8gpo1Uv_urLUcpMOD1wETwYAAOEPXArUdk_mLj6OJRpot2OL6mnjRsebJ9xbGPXSGGI5Rs81Mb0VUFZTxkmAV1gja5c3QI4CGuoMMlZHpyltf7i22SIFI2OXX4Xm-u-Cv-I0ic9jLAXFXxOuoK0KJB3_HCMAAH8veQoiWBhqO2uZqHAstoLVZmR7xtHcJWVQhHrGOQJ4qulOeI4rvxzN6LMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی جام از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUsDThUj9MXLgT78QPv677ygLEANDFJ4U_u-gRwU2NSrEMICAwav1Cqoh-9g7GS_e7u54QbfH4hT_Gh98YoQEKxVVWEj0Ncqlg-2rQcoK1PyrAUo-ymUwOXxUis1h3yxgmV5c5uyy_VSgwjJR8LCLuqx1G1y7TsD21STp5sSl1nQAWBfwnrw3vPpZVWhtYvfMtLBUzuNbwLQUHaVwE2QohwIUMhi8sVmK18I9sYkkRf0E_4vKqaNSiqUN__wdvAIOP8oTziA3qf9UB954pR6wOnHytqIwR39R4xcmes_4MVvn3VrbPGNyQwELe1FcpQYW8xxZc_IRmCBXkU1pdQs4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=p4PAmYrEDwO5UIMtQDO3FAi3DGcuEACQb8t-yk3MRm9lkJFZSP1q_mYUDd9V7kfs3KnudCK_aIEeevN6BQU63kWbrYJvDCUNIy-wYhttUEVn1cTCwTGnLTeY9fDe4bwJOnzEKRwXVjmjjhXRnclUpjRkdMBbhy118tYFD9IPnPCKauUS0qGQdIV8HZWTCfD_U86xHslQUU7RjJTo4lJjDBs2T7QxROXAH7-rbAdy6On4Wf_8UT7rBetlxFb6-JQyLjsJZlibB0feRncDHRiOq4Rx2tMxQSzPJoXyliqc35Sp1MIoYUIbHjamVHMeOh1eCFEfmYtsHyq4cpdw4Ze7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=p4PAmYrEDwO5UIMtQDO3FAi3DGcuEACQb8t-yk3MRm9lkJFZSP1q_mYUDd9V7kfs3KnudCK_aIEeevN6BQU63kWbrYJvDCUNIy-wYhttUEVn1cTCwTGnLTeY9fDe4bwJOnzEKRwXVjmjjhXRnclUpjRkdMBbhy118tYFD9IPnPCKauUS0qGQdIV8HZWTCfD_U86xHslQUU7RjJTo4lJjDBs2T7QxROXAH7-rbAdy6On4Wf_8UT7rBetlxFb6-JQyLjsJZlibB0feRncDHRiOq4Rx2tMxQSzPJoXyliqc35Sp1MIoYUIbHjamVHMeOh1eCFEfmYtsHyq4cpdw4Ze7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IMyhEqS5NQby67X6gA4U-FecbQMQ2WYNbpMx9V7Kdgf_LWzKZ4ub3t6n5KhgWLK0wAhL5Nvgbg2CmqZrSErOJpNpahiiWGQlsFzlQGVgqCeGpWg8RDsf_f3eWFZ7sHuFNEAxUXL8T9MMPdpM8KXhOCqOmvbfcTGDA12fdtSecVBJOaomptxKHbVkkhuYp4GXLNn3j-dgj1wEVYXgH1krzAu7Q22xR9y_y-X18QHeT8vwL_e7_DLtPUPNKrSRewJPr-toiZtPEk1A2SZwz7nmUj3I-O6JefALW84FiHaqjgTmwn99UMoT09-hl5unHsVnAtNYbJazN5Y8o7-Ct-mS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fD9d5h9_iKM3ak1ovMAeUhjNl4w6MFuoKl1pjGbzlTvbQSoeVcxobLhYQ5ao-6kkocQrrKMFDcMi3HgPwNszZMGt9xt24GLPEx0wuRrF1OON_wQiWG-hRBgkEAp2N4T9pE4KAcMdcz3OFpzFlJ0VcG104askihkwzeezqapjNdFWHNamDlv7kLEivU1gewW70ZUS9QSmyWib5EeBqhG8y-HyutRUqHrpb5_ytWNBMKI0ywWvEx_vb5QlG9yGoLpXt5qAH1r1DC6tVVYaCGxRMdAL1llAMdRZjt5Q5O6qkMCR6SjqYUlly28BbQl-oiy_aUKwRwliEgEhZBNDfq5xKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام هشدار در کویت
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAuw_4lxHZbCTT2tOQc8onYIfyeKPqp61VwwP-9nQY1YNQgwXvP0TbpQTnMKA2UqbiccZM8N4kBbmBY6S558NzRcci0eqFFmp6mrTScsW2y7Ar3T7HRpzRpKLroutEogX5bqOT2IViM_41FqRWu_DWkv0XbHi54KiWqzQGFUeEIU9mgW35ESheOb7Elh964sabS8dHDxZMOEteex8ttPN0yqc7xiVdVAM_qbBIT5oG80uASXi5aU15yTb3zdf_G9KCVMrJy28z-c2p4TxzGYYGXX4qgymALCRXVxhC7oh8ILBh3BcdenTGmeZJDnrP8Q11jema0aiBqAVxxPizyjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=fBysTg1AiVF2GTawYYtnQeYO0anfv0GTJ6irsjTxAjz33YiFEq3BYhHRr_K9_leFYlfYmuKtehFPz8eXa2quZdAJxDbFJsCzAjmZ6r8aypZn8LCNIL-1rAaUZZUk8tXmrT_Y2NF9xJekZE3PHSWCLe80yxFK2gS3NkgkaSGil6f_bCKdLHqwgTcvTXgNAOxAoCrLlTRY0pQ7lqXwzPu-M1twgSgur1k944C469a6R7hPGbdkHE-kwFiHZHwFYuTjB86o2mwJKIJq_I0i6AXAk17TCg7f5AsDy3BlGVmTJJ0Ph9FKbHUZiGuyYpvEb8iai8k-Gr7RmSu08dBiF8r41A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=fBysTg1AiVF2GTawYYtnQeYO0anfv0GTJ6irsjTxAjz33YiFEq3BYhHRr_K9_leFYlfYmuKtehFPz8eXa2quZdAJxDbFJsCzAjmZ6r8aypZn8LCNIL-1rAaUZZUk8tXmrT_Y2NF9xJekZE3PHSWCLe80yxFK2gS3NkgkaSGil6f_bCKdLHqwgTcvTXgNAOxAoCrLlTRY0pQ7lqXwzPu-M1twgSgur1k944C469a6R7hPGbdkHE-kwFiHZHwFYuTjB86o2mwJKIJq_I0i6AXAk17TCg7f5AsDy3BlGVmTJJ0Ph9FKbHUZiGuyYpvEb8iai8k-Gr7RmSu08dBiF8r41A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=qeVNmGI6qjtgvzsN8Or1H_0Q_ANtSTg4UNqD3PrQ2QpNQdol6KgkCINw29V3ut6HbPXpMWV-O5TZY47uiG3uL1qbEZ201HvOrbCOmN5seWn_GdRV40RbI7iQa64AG5rc6IdYoacNTdMnXonwSaCGamFzafaCN70vQJJyRTf0Sq-ogF9eO4GfDD1zmtmMtgUGfFNKy3Ja552Qzgpprgt6XDAYV4VSWCp9s5SJLFLwWmyA5Dr6Z496lB3H5TPMxT-pI__YlM9ACDplKIwhquQ71cJ7s1ihNGy1VElW11CgsLZdXqr9d4rHVaP0Ku5MCFHG9m1Vey1JVIUQMOdOqGsoxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=qeVNmGI6qjtgvzsN8Or1H_0Q_ANtSTg4UNqD3PrQ2QpNQdol6KgkCINw29V3ut6HbPXpMWV-O5TZY47uiG3uL1qbEZ201HvOrbCOmN5seWn_GdRV40RbI7iQa64AG5rc6IdYoacNTdMnXonwSaCGamFzafaCN70vQJJyRTf0Sq-ogF9eO4GfDD1zmtmMtgUGfFNKy3Ja552Qzgpprgt6XDAYV4VSWCp9s5SJLFLwWmyA5Dr6Z496lB3H5TPMxT-pI__YlM9ACDplKIwhquQ71cJ7s1ihNGy1VElW11CgsLZdXqr9d4rHVaP0Ku5MCFHG9m1Vey1JVIUQMOdOqGsoxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMbinelVDVnGijmnpG6O2L-EQ52qq8Fv1AKRAo8IBgZvKf7gv1dqqG5oXoLXoknKrQsBIRWpBw3_75gOrSuuCRVaHotNWSpSwE0ZTk9VVFc96OrgoAmiCxxMUa8GDPfuyrruiLpenB0jkt2LFXDnmAXdpzzhLugmVrbbEs05FA3wAcfRHn0FwkFRcLXSVAXjquoxfBc3LWUD6HliHQhelzDVBOd2Os_OuFJhmWLp6BfV8kDa8vQuQTRYYEan-0s9bIRf71lTWy02Cb4Aa0n22qRZeAL2gJhfxAHxq4VxA0tCaOW-Ley2nogmQ7Ly96kK91NDHqf7MaVNYhbjYumdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qTWRO83ckvuQbvarf28-nEhKmbbB14lgq1ZPfekmmaRqLilE4uHNKmfw_8wD4yWY1oUBMi78_nvZdLCkA7EydyqdwQWylmG0PD6cdqg2zQ3D_dyqT4TGQUCmKdBz77u8azjenrK2z41TGGhD2PO2M7mCInZbSb4yPRM-KMeIc2rLLTGIPoq0gRHdWHtNQMq-wJXaiFMTe_KLjjhrt_suaYO09Aj7B8sNkX5a3Tlsz_ZzhSjqjFvnwxcdUej3Edn795sB333XO5CcytGPWhzds4XWO2vDVCI4beEZtgnYzmfxsUay6vo3i9c6N6PkYgBwrjuBnstTXjfnQL1a0B6JFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b1zd5ZsRtLf8vTfbGjSULtaO_0_OgwcB4s6yCssqZnQ4zUWB8HxRrKzDcZQrSUuqn1JBIrWmIiFZYoJjyPCMRQyVLIvtkt-4uQOAjnkBvdfggykBnztIpTBIy6LHslD1pZnzQGiAJQiHrjS6KNWdNvpVIkkVbuObLDLbbVSf27JBMijZImNkRBWjIMnx22kGb4bLHaxYwXqAOXJt-qbfv7wqYAjuj9bReXlykZx_IwdB8KVhyUHqmCnsDKMEDUT2rqnPYxkHbLMWlI_scLsIrVd8y4KN67hbUxXZP0Ps2cnSSd9BwCXMbQIKR4KoixikHARFRh-YdBffBT2jtqUtQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=Pv-76sICoreDcFcusleV1nwK9ZuXOjwpTrgrtiX2QEo82BmFpVLEkXYLFhHxpYjD2PF72Cc0u72r3TA96uqDypcsmhU79cBEvr8BGmcpDAH3r4L7e7u9e9sItjvOsz8GD8pEu1ztUnbpTRQiX6-KB9zqPmkWsVzkr_siW7EzCUJjJdiZn3SK813yL86g0DHKBcCOja3bLyjn3fF4SNqlTOlvjxJXu4Fxsroo80ZPLomz8OLX2PNEIIsNxg8PHZ3JTgT8-VkqsRQhA6yTvKNlKhssqZ1o8qgMRTZI3L8DK2Q3IHQyXlVr1y2e3rnwnfJ6zNprSJcd_OQct2anOz38MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=Pv-76sICoreDcFcusleV1nwK9ZuXOjwpTrgrtiX2QEo82BmFpVLEkXYLFhHxpYjD2PF72Cc0u72r3TA96uqDypcsmhU79cBEvr8BGmcpDAH3r4L7e7u9e9sItjvOsz8GD8pEu1ztUnbpTRQiX6-KB9zqPmkWsVzkr_siW7EzCUJjJdiZn3SK813yL86g0DHKBcCOja3bLyjn3fF4SNqlTOlvjxJXu4Fxsroo80ZPLomz8OLX2PNEIIsNxg8PHZ3JTgT8-VkqsRQhA6yTvKNlKhssqZ1o8qgMRTZI3L8DK2Q3IHQyXlVr1y2e3rnwnfJ6zNprSJcd_OQct2anOz38MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eJgF8BkpIhkZCTzeuHsjeQ32V8V9qIzPZEBMv2zC013P1lgvyqX2qUDc-QaZszac-rBmbAXG1MPWYz3Ho7rstPYYZ49nfAPuoglAeBQw3-bLxfjpQci3lBXT7iQoWxfjpzNAbwO83JSa1wjxu0IP1PhBEHShu6ticUtLfWL7lSmtUFgv-zLTaEkOok7Re2GBG6MPBcv2BPht8sZtJ_I5GOoq0tdSkQk1jM0eGofrqk0LX38GM-pE1QHU-8w6H2k-tsXlruiktxW147JCQnEPZV6CUo_IgLsWtIfLxz3ZRx7uJdGoMVZtTBsYfhmLBa4e2WU2AT9nMjyCO7LIVVNvyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrxzm8MVvEL7JdjT5ivij7rtspvv6u1AMxVBcxtK3mFEN6BNfJ9cbNmcAWrq9lVALW6odrLj1sDE2nWEiuZNJtYiNxknMYEAwIoqbdwfU1sqCYI6pysLOPOiUwGiC0A1BdzKg8ybZ9ciqzfccOatnS-6b_lgsgyiSfZF6_jkfaSt-W_uxIocRFt00Yhwi2kp5PCFpoD-m1c0VIgq-Hqg_lysCMV85Yh5jMLWHjg_KMocKwT39sRWtiKwguep9lTxQSYX7weQzhgU-fKNOXFm4Vb-gu0lSIVHzvH8spvSx06yMR6XSdiyUIKpO8A57ul4UUIxemitXOVoVMU_HeeGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQoQMO7P77aiT06gExdQSzoYS2AHbpXFQ276u6wDmYsPoWdSW0XPAQEvIqyzGMC5j0Zz-B8zbco1urpx4CBp11zdMgwgGUx9W-U31Yk5550BmRoL7lmVokCVpVtTU70IAyUSXmM01GYHq7X1DrwCp6kILXlxdTJvHfSXEinrE8Lv6CkN-oBIotkBE905_hxJhiU-uLX8LwA5EhXd7FS99VWdOG8R7UI4d7qHhCi2h0RdIY1dutzGebdu565_X1UeAsfHk2NiVrnl4OVGxyg795EHBml0M8HtoN1dEpR5co8tGARLTiKvMTSS4GOTm8xQJba1-oiPGHnKchaAE0IX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoNbKo9u9pvHZbshUntQi4r4d6W9JrMqYhDBaLblZPpu33zgpetZK5HbkAO2_xz85BISqkzLAtAkbbHGtjsVVK1BfzQo44yLqUGqn0NSh-q6y10bQQG7f3Eu2Xl48TUK3voNJ_HpDC5wxCa9X-nLLpxFxiZdbgX-UfjY96t8Lwc8ELNpO-gO_XeTPk3UPfg22exdrKEckcD2D5fKxkcgZe7GLIrH_1LzqZrjN6ovj0bhZbfBQhKjApM9Gt-Hbnw5u8POdmNAT3kgYu7cmbLGpyahowCPWR1L0qUVG8GCgeCRZcvPlPg59S2UrEWJLWiHBgBfIGEcZo9CtuIVa0eJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rALdWP6DnUU_4X72fSSpeu2tKHwyqAr23dkLxVfSkeuuMIm4CxuBCyB9tBhgOg3y_9hSFwAW7v-Rd2TzwUpVbLznIrbSQYeJ-UFkLvbUpeDkQrPrkAAEA2VShTk0YXGgR_ZSUGEFr_i34ca63Vi4K6QTcoUfdLEtxAr59B1RuIWa6dQl_jrVp8cDxwkmSJVV3lkT6blZrwqqOl0G0grpOWuRCTcGOb2LNtz8udYW7z_k0ELq-szI5dsA0erotE0YL2TZLvQgAI6J-lyN9NymMv7v3d6NaxhABn0Rxy94MYpr_bVJpOIV54oxkz5FkrfzDhDu5yLKTUANGK5jifITaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RmQfUjRKyqHBCJvph813UHUAHolQXn-ykU2gEbqEH7fQz-So4t9_aR845fJ6FUqsu4UgX_tPWC_IpTkhQttevYtibzFcxz0RtfJxp9BBRAwED1LL_iK1FvATyADMw2dsM4CHob7erDjarLhDQ11gMooWqqu9b_DzbAQdwMLdhV03k2XLcBZIPmIysZZ_bHn-UxhibsWrfCLN_upapsp8kJhY70_bXfC_AEAfpKVbL4YBYU7UXKZvE8vQuHKisalUaqrow7olHnvW20zGjf21XT0_VRDBLF3OlVfoi8wX6A2H1IlOYJXME7RHBuucHz6vA-nDIdplfDVfKLLPBq-Grg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OfiMz3QEgYoR03w_C_VPqlqQK7QwMg4inoa8tT2u_MQyQm_Ci56Cl7ks4siAhJDT9GTQl3rqkPfs8ahmStQ-MpkGMonaEL4tTVba_ftyLdzC5TaL7Idg1ZWmhcdp--hE398idA9W6jUtyPJ9BvVxChYU6CBq35cmrbnn9uWvdk-ISxEoNjsUuN1McWb_aXpIg4cg__CGpMTHudRFUrGSaS_QmCsJfQwVM1VaP-asdMd2Hlm27XdpBYHwt22rpWtkE7tz23boVT2mcJndltqiZc7QGfx1L7p8X6jk_IlJQv5o0N8QJExQUU-rC-bXHU-I9DeaqfbZpWrUuy2KMJ8W_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I4VrRE8ts8JyMwWJ6ivxkZ8bB_ufGyRIXNG29ysKMjB1VuORWnBtg7Duvo6WVNJxLOa-Fp4ORaBVmFyUd_sMXOLPAa6dt8ZrGfVPs2yVrJjlZ548cIosWfscHMguHeVPDaC-oxZOEdnWMos3wsQkgv9hk8ABq0AegxiuiiaK5LDm0KUDIWb3m4g3LKIq1zM248ElJ5rf10fM8FE0Yr0H6NDTJH9G5M6TP9VzpBcL-bTaJaN8ERSn67mtBBtE_P37eeQGcq8RKCzg_FKq2bhF2sX9ixl0vOBJpY68IWYGiJLr4b2Rsanp9ZwxU3cUYh6tkeTrCFtnhEk3Xn2wklYe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=TO7afqoq2VQprpTyV8J77VGXxOfaTkQ9NIYDLrMnSl3jBe5xjFhKvHLTkdpXHiv-oMf4QFPQgH0F7oU8qqTeUQjbh6-774ZI_NrDXgQ8sfH_2ilT92yhRprufv2nSI_l3sK7S9CK0JIUy3XvOiUBhuGdKeW0Cf9un5d4gYwHrPAN3VpXxFxKWkhCACqL-fGqAKdrwWJDp1x04gLbZMRv1z9O58yBJBJRxPk9PTTfXRo3hEcy_Jud6_F1FLRTjUqSqjiV6BI_jViWP5XpA5e_f6cRv3BEgffr2StrqtaCkPe_O-bEcWCxaSSg2TLjOxWSVl2_1YkpxKOTXLeQTh2G8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=TO7afqoq2VQprpTyV8J77VGXxOfaTkQ9NIYDLrMnSl3jBe5xjFhKvHLTkdpXHiv-oMf4QFPQgH0F7oU8qqTeUQjbh6-774ZI_NrDXgQ8sfH_2ilT92yhRprufv2nSI_l3sK7S9CK0JIUy3XvOiUBhuGdKeW0Cf9un5d4gYwHrPAN3VpXxFxKWkhCACqL-fGqAKdrwWJDp1x04gLbZMRv1z9O58yBJBJRxPk9PTTfXRo3hEcy_Jud6_F1FLRTjUqSqjiV6BI_jViWP5XpA5e_f6cRv3BEgffr2StrqtaCkPe_O-bEcWCxaSSg2TLjOxWSVl2_1YkpxKOTXLeQTh2G8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYP2kNQ3-ShxkuzdXM0U7CnRznbhGesLPCWstbd6ZoL5hJljJEXMy0ACAgFOULDCcSu7IAmhgxvocUNsK6_BXHPL3moqv501qYkdTkXw33RgaCLIQ0zVrN3oAJakWrZfOc7YbiG58o_oQfsdLgw5XwAjGd6FxdkwHEiF_TziHwzJqXCsV87DzBKnR1AqY0pdfJKZDXGc1yujf6vrh02-cF13UEUOYVixqe8ifzyVAg51BG3Y0QszC0dqLYqVMIX1tBlHhoybVrGczl30nN53icWRPPE8ycZWwmYTd-t1Rl4fZEAXSpfUArq80D0OO_PC7-ArJdwEXNX-i_FcqewOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iSxhVmC8CIE4iHS4g6Bj6qB1eUyWQ_v_P7TzzJBp-Yu6U8rmTuiovMY0k6TYSVr7Pb9olLaRlXJhOZdn602GbagWWvfwaOUTq5jroi0Ubwg9sy1xgP5xxTXyqT6AOxqFllUldiDKZn2g47WvlRpKHXDY6ZQZdHg0oO_sP_6oyeGzdmx0YGj4JIH-YGLo8OYusU0Gbjx5I3JOwTk77i5DJeQsBsTPbnObT6zC8JS8D-Zw42pL1t5djTT31b77qYA5l06PQzKejn3Ucl7ct09KT5ehulZahKJD9yojxP9ktuFOLBBDq2pN-HK6YuBgjw_vlsnAdtv3mhbcsMTwdx2NfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nHHEdHxl4sUhPDNDNipAvt3kDim1b0LCEkkEI_-Eg0Xql7ZQDrQ_3XcLlRR9iK6wTqwUn2ViUTE86dOskNS5zsLXcPdayNwM7OPNcP4JhVpT5foG75efiSFXZ1dpoqIsfcWtZEFX5yDqX22mqEeiokUTic5a6oWkVwS9LzzO0bPKG6VAMCLrQuT8_6sTwF5RURMFwBMS0wgkgqy9aaQYJZrml_gARn0waNj9JsQ5dnclpykvzUxighdCYeMMWZtICmFoD5vszjpEEgaft9kOkSUTpapVRUMYDyveINnfUrJu9RGXdkg_llOiIb4_JseqjFvHqLiJk2X-s9aOKqQY4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kb0qLz8PQlR-GUx-6W32srdB91vQP6vl6rMtAjTF2rnvThPzTyr4HKkicIyQ1JR7x1rwN1y2HQLPwWvuT2gPU7otqVw3IeEimAHTdRw91ICf-dlbe9tbksLssX7luvrtd_2-iiqsw4Jp87B5JnQetoHILe8zqEHIX8wvLNtrU6ZjU7ekB-k5U5-L5osTnTfYtSdNaLdBASmUNa7dgZFjWTaOpk-7wGbKhnUAAe3VQASApkdV2cmShnAxWjZVJ5PIULb-0Zr9Vg6aLOlYwtdufdHGXzzU7MsjAznnWkfTZ51ENMnLmuwYYfg4FwNEj8_aPBibk-RbeKMJBzCJ0TCpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1ODfUQ_CTuOyXH7sc7sbChXOT-E5-XVz3AJd6ngistyoImg5FH-AJDq4Z9ASTXnK-mWfXNj1LJneivSSAYwslcVo6G7wkFjWikedexZy4mG3axdpLMsBxF94tZlV43pqY-IfIHG6H3S6fgc1HWwbpw36qPZ0yxHIl-cARtOc-rop9XPmkQPhUXVJec9prNIrvapzB1Nl9-jhi1totbVYRti7QfyswdRxjzFPKgo3N4tGtW933nIFfC6aE70fCQUmTh1tnxDPffdhhqaAVx5cTzeG2lllQJpz2efbrimpn8ZOei3WJi2QiQOUamMxJh5rmYbavBHetVLGpQ5JUU9p-uZE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1ODfUQ_CTuOyXH7sc7sbChXOT-E5-XVz3AJd6ngistyoImg5FH-AJDq4Z9ASTXnK-mWfXNj1LJneivSSAYwslcVo6G7wkFjWikedexZy4mG3axdpLMsBxF94tZlV43pqY-IfIHG6H3S6fgc1HWwbpw36qPZ0yxHIl-cARtOc-rop9XPmkQPhUXVJec9prNIrvapzB1Nl9-jhi1totbVYRti7QfyswdRxjzFPKgo3N4tGtW933nIFfC6aE70fCQUmTh1tnxDPffdhhqaAVx5cTzeG2lllQJpz2efbrimpn8ZOei3WJi2QiQOUamMxJh5rmYbavBHetVLGpQ5JUU9p-uZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S5ycXEqs827Oo_rdjMIdcx8pH1WXv9SC13Q24fblwdw-ZxRLjObSpyKE02V5_PLAd5bSqzhMmrOcQgx_S1kEIIqcfeYRMKQVt6Eo5wllao9nUn6BGuKRx2PNoEjmnI31-YMJrVVlhrNmk5U4Lb1emoe1UKSMq00isDBmXHXDQRTTn_EbzQI4_b-Y8QWCHhNXMWHBLp1Efq2aUV5v40elFsWnuoGB23WOfMwYqLVN5vSZ86aVQEWKMWh7YpicKm3VIpV4PDSmaaZHl1Lbn6BDeVmZUVqFIvofUnA3edjTR9ghPjBHLCPfsBq9KHFIuNIROScIwtUdwwDVnkqz9oOUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H-mDo-QAqOgg84PwBpWh2aW3A1ABz5yI2sz6Rt8_Zw6HrMxG-0AeS39zSWG4ewdikCL8FrxUIUA2bS1apI4GBcZwtD7E52ITzSuHWVpjGV_REmiGq4EAG51uD9CYTmJ24hYMOBHEstB9b_E-BvfNi8NRR2ecTYrcP3NJ3sCPE0_xU1Y6jV2y65zT4wqOFphNuLmbVKLKdmAsAYr7YVY5A4dWRI7q0iRsTcw2NHP-iqiw6g73YtQ2BiuwDIREzNWmtLU2eRJZXvIASD2rBoWlgPDff9_dykRg7lNq6UAqTeBe5vvDydB3JRKA2zViMLZJvuP_t2DdVhu-sMrlQONTuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=pIwed5cI2XhHGjQmFEHeYzgmIx8xCx5LzBia_wWOm7EnN3o5W3JZ4AnsUOU2wpcNkSgoepNqyRA-GN4APneIfViAo9sLy8A5VIM0hh-D0j_U11YSXCzXexZ7FvoBYkag-k1-yq-Q1vAsDjMdudSXAHDtnvLJYtJ2ht4LlCkHKwi-dEQ2tdFlq_HWeVhxCEXaM64eiCECkAhj3PQeIEkKHnu_7DPBNVRfxFdyO0XOUXmljZtmZII2RsxkUc6ro2UzFJ_5kZJA1YX-IrPbbkHw-IumHLyD7ag4WVQwxc4j9WiL6begC51lSleSPbxebbZSIXEb30VuitBUthDHdVDOVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=pIwed5cI2XhHGjQmFEHeYzgmIx8xCx5LzBia_wWOm7EnN3o5W3JZ4AnsUOU2wpcNkSgoepNqyRA-GN4APneIfViAo9sLy8A5VIM0hh-D0j_U11YSXCzXexZ7FvoBYkag-k1-yq-Q1vAsDjMdudSXAHDtnvLJYtJ2ht4LlCkHKwi-dEQ2tdFlq_HWeVhxCEXaM64eiCECkAhj3PQeIEkKHnu_7DPBNVRfxFdyO0XOUXmljZtmZII2RsxkUc6ro2UzFJ_5kZJA1YX-IrPbbkHw-IumHLyD7ag4WVQwxc4j9WiL6begC51lSleSPbxebbZSIXEb30VuitBUthDHdVDOVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=IxM7bT1ZRF_q7n87ruGpiazGLcbMAuuNTE9mKTutgKrkyqgNzm426NwSk90R36ezRq-caQSOcI6s-84Zn6RtWYlZtb-kDJ08Xx7k-_1zMxw1aiE1GhS-KonOMtnq-8_ZuAjzLalSHc8TW5VO9Jm_9Xs-Tg6QRugQ5XFhR2ArEwLXJAnLnsUFZ9_UsoyjDXaB5cO6so9AS2AJq6kaOdgjZpJJlmbq-wnoG-qBTFK4YCI4nSq0Cv6LaK4-jxtSqVt9611iAkGqGloXg40FjWq8YsLv62-wrNejhRpT9TzNfQ8DbyT2ae0pMddaEcfE4bFNMHSKKDaKc-9ZsSrXmF4QSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=IxM7bT1ZRF_q7n87ruGpiazGLcbMAuuNTE9mKTutgKrkyqgNzm426NwSk90R36ezRq-caQSOcI6s-84Zn6RtWYlZtb-kDJ08Xx7k-_1zMxw1aiE1GhS-KonOMtnq-8_ZuAjzLalSHc8TW5VO9Jm_9Xs-Tg6QRugQ5XFhR2ArEwLXJAnLnsUFZ9_UsoyjDXaB5cO6so9AS2AJq6kaOdgjZpJJlmbq-wnoG-qBTFK4YCI4nSq0Cv6LaK4-jxtSqVt9611iAkGqGloXg40FjWq8YsLv62-wrNejhRpT9TzNfQ8DbyT2ae0pMddaEcfE4bFNMHSKKDaKc-9ZsSrXmF4QSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=RhoYWu05lZrYedfYtVAOfTsdX4RnVohqNd93OjhCzAF1G4AWqz2qqwLWjpTF1wP1Yn-Ov7w7y_j0I09Fccjy6GXUhshzXAJrDZCJFq3avuxqYQ2_ntIqH9x8FTMShSsnnD11OzK8mTFS5xQtyavytZrR7VTyaiU48jP-lMGvYL9rRctYKXLCArtja_LMGaawXrfzQS5P1DViyMxmeanIkMYKosLuYkz9X5hqK5kx_wdQbDyW4H8sL78LXRuQyxiLvcOL3itgpzK6UmzO4JYtdTrFyPKTDSeqpb93oGv9gfHZR59L2syR4sZjA_9OdPa9FyFfdiz7siTto8rOfKOeRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=RhoYWu05lZrYedfYtVAOfTsdX4RnVohqNd93OjhCzAF1G4AWqz2qqwLWjpTF1wP1Yn-Ov7w7y_j0I09Fccjy6GXUhshzXAJrDZCJFq3avuxqYQ2_ntIqH9x8FTMShSsnnD11OzK8mTFS5xQtyavytZrR7VTyaiU48jP-lMGvYL9rRctYKXLCArtja_LMGaawXrfzQS5P1DViyMxmeanIkMYKosLuYkz9X5hqK5kx_wdQbDyW4H8sL78LXRuQyxiLvcOL3itgpzK6UmzO4JYtdTrFyPKTDSeqpb93oGv9gfHZR59L2syR4sZjA_9OdPa9FyFfdiz7siTto8rOfKOeRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsXDeIKG66sJqJSQvVSWv9G2z68FojyRcHNv--KlhFfPfp-ekydAYbPvyv96ZFMydNqTYulvvESMtp0Mu7IPCeTiNRjTVEbbybDWJcjvaTLoYQ8M-RgJZcPv00XH3xA8C7fdB9QM7vkq1JHV5dAthXCwmexllgPXpE4n5JPzi2Mu8HRld_ZzbYQO9ZjDRN1nlseMOUT16KkwWjiwIcGxGXREeLlZXb9QV3YyM4ETmEI5LYpzm2eCKTXdTHFJYzL46iRFeYNAljt8eNzE4ilM1PJTDO9VWt0J0YgbYcAiACQ4W83vO7Xg0litKRHb9KZBEsMyBZERRuUnAsdy_BEtNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gowp2nUZg77HMNdAJlRYIkj0E77GL_j1LSQ-xFpo1IfMyBLT5LWqqgqfPYCufHxTOdlmoM_Fsr3ulv6uNRLYuO26eRyXUDZWl6OWvTvMYn8s0j2EKs2JrcqtjU25Q6G03j9H0_4FRQsM9aDzGB8Z2bANSYupFKqwSRiHLfIOOGzEZEvWFFg4Gy1dNweJFyq1eLoqLsiWKaZ0GPCCw7dEnsLNUN6oLWz3PL3AUStqmLmjWDsrn2zK3UmTeLcYINPDFBntyt5scRi_-A6v8d5dxO2elwf1fVpKPgWb1wPGwIL1zWYYrEIvpaVF_CgDOWpAO7kSh4C3EMGlpLrJTbRL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5FtoARhEYOVIlSoaKGNBhTeAt_ZSfXgBBt_bqK8nYlHhpI2Xt4yyuSsgTg5F3GthDI1zBbuLjzmsLr3LbtaF2pTJvADfyZQQk1P_miNZ1lNx3P8HMAcFOJHSb5Q7y_AA8BxKAZC_4IeA2UsgPHogWVj6u4vftD5305nt2RAkSRctp7_GedVl_148oQPwMbZUKot-EUJGavXXIs9NoMsn3z6gGD6pBmtQXIqN10dmcendukZpiD5xYI582k-x6Xfj0WCTfl1XSs1LxUqyLTtBlm1hY6QJ8dyJldWomZeGDG0ssZ_ltYTgq7IW-nzFSdcH7ompn38DKGxvnfX9u2csw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CLJSLqqZBgy3701-qjuGGevvVx4bZj2xPOyiY3gL_y_RITOIvc4X7zm4JeCmcJptlGukCQY44_6mZ23AcgXjjBIhq_NHmQQAFv4VWt8sjtdsPcvUrW9rEadpu4mP2xz_M-pcsmv11xKw_tiZd8Embnp3g4ecQT-my4-Zp2BKR5PJpLgq15FamEV_Knq2i9EyBOfaa0toNGkmeTYvKT23H1lIQznA-ougbv7oVCAkuuaCuomHRb0fKW9xfFbAbsKsW9eb7twN-TGzZ3waEk4iH7kZ7Mcjf-Z1q0F2BHufjv8IO9iRDq-GJl4DwussRSFYsKLp1NAFKsmRL6nBWiMmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aZR1PSlwR6vNsT_mMO9mUQJrm9BSMCplzZLuogsgglck0HuOKJYKFk5lTnx8V46-fWqPl1Je5CI4ZOSyAEa83eNG4nc6g2M4pPRk2vV3t_pK4XlVTrWfjaLfzZ8nv_F-JA0RxWFHeDaNzMxHoeBj51kKEAMb8LDQfEq912irW5Vkag80Cboyf8QKKamoVu7LeYuhCLV9lPuafneDO65mvoHDHs9db8Ln5dE1f31NG-WEbbiKPBc0XV02nkRFLd3ELD1lvahZus6iA2DjP9xr6_Gm5jYokBFxUzfmvHlsLSjqWfnXL8fx0MRGnRiE6XJXVpNqjc8kJVILiAY7eJIi8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B-sC9iUds1Ib3zALGPLOBFrrJWCVzIG60t2YYSnvlEBnLPVXsGTZkITrEitD-ii9Dm45bOe_Ue8qmHzKf4CaWUbQyCbEfHiVygQkV0NZWlt6373hMm0wgpjk7JLmKv92qk3saHsczvuFDlF3gA_Vq2zjtcP5b_jjv7W4tzzhFGmm9f6I3ztyVPpCOn_ZdLtpRfK5kJ6-nWCnFwUrkXIQucnHX1hrmoLS4A0PEJj7OTu-fR3j29YA9hOuacVYZZXmHuiVDuDyQbG5_5l4hZPQ14gN2nC4edNbntFx7B3hK7NiK2OFmirtoqwnW68Vjh5ULF0h7i4dCXjmxrbVxcyS2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q_wghAKEf_DRW-T2YUWHPYkx9xZtd5XcZIlD3Ihk9D2T9U97xjh0DBIilkQfDXYy5zaBk3RMARUOGPgXnDeopLSqLzRgz8K5AYwnBw-WXdSS_Y98KppFr91lerCyIlGGmuBn_JiO9LzOwGkMA01V7YYLmaOmcDvvIpJR2OVTvgrh7-VZgbJ9aTlJjJddDbI3DPna9B3tVhmuWH_eo2Ufy4ZLhdeQxhBOeu0H2YEeVxOE4-X9K8pcNwV0g3vK226S_WjsG2KE0p-4_pQLtf_rAFgSd-WzWspWeQ04uqOCsa40G5nO6ezddNqFBjgPieE163A8URpSsZFVEnAnqRcqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/skvnT8RxSsHFlm0dHVk3t64ucn6Pn9exnjKz-9h5zyPEinSeJFT4gLV6XkE6njCyp8gAqsJ9FssK8ncyGOt2XzMOhIC8ASxPADzsa8go_9fIbTWWa02yqVkC3r9cfj5tJQN0VRjsayeiPrBUMgxoIO1m6gVMtn8Tbsz3BFpTCPkX9_09TT0HWVJ0qKESmUHFHMrOktcXCGEkf8Fe3g0qecAngKpesEx4bRy0SSz9y2xrG76RNWje75UuxV3LgIoUZsrhOv8V8LZtRojqr-tQqDvjAoJcc4GPAKLQJyLBJtyWOCP2_ohw4qW36LugD_VTSM48Hsb_Sf5lMgvSZl7Eew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IAZszxifRuXlnqeZ754zgjTHCmTUnKUu9rXXAJ2G8nSDZL5q44wWPPQDXyygJU8H5lcDG4kDTvAXsBZ8CO5vEXDkD1PhinIuH7RLBw4oL0rerYYiRG39KLIqLQCK4tcuMcBKRoJ-j-JU3UyNZ5lfRkL93yiIKYGcQESQ9aaT-In8jqNUxgpLQdisTKynddE0Qbj4lLkQn15OuD0Z-etTiX-eVstr1atng5rlAVjv2-h7nQyJJRmp9Jb1tmAdxvOtLqV5SPz8WdhtODO24ud_5Q87GvOMPOD3DHCk2DQlC_egKCt2nVxFRJDNJ9kg4683zOQ8snIYrWH0J9CQCGN47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fpJh1xfZcGsg77UQ21at4tthcBTn2hUowBb47jOn2Z8EJ9IF_TNlgsHIqjn6g6NxrvEIteNgRn1GCe7Jez5fzrc0FvoFv2dmO6q7MwWI51GpWYjj3KrskhhmYXHEm2_lk-9tT42DXJbyB6crqEjkExRZgOMR6ModWJN1zUhVDnBOfZ55Q3jufUNr1LhBGBcBgxcmW-lzTKvswx3f_l9neyaVCUdYONfQ7hqaXOZKYquqC_qhibr6Jge_5yE_r_-5SvIvNBaalffZ3yXkrcrIbpJ6a-KQ3tz6o_oie7MzIxXjcG98WSYpO1f6A5wave67lQ-GayhuMaDg_4zYi0Uy-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VYiMg5IEqn_cKsPx7QYSuER1hojeFm5hQHnrVw8OwtSS7FqeUhpEjAz9ImGyl4TbTwxgi5YA3gn1QUmXfgsKhFgi-DSFX20v2d4mR3Iw_dUfy5a_9syDpwsHMhmxe_80QOIwGIJp9HxNtrv20hMzqWwBN4os-n_VOO7k06IULIDOWPOgB6qKSKDU_sQxoQPIlxY7YzneXD1z20ITGQiinnL5vGZNrZd_9B6uuMrHeTCdkdqanqihA724vAQEivvhhexcjHdvmjaEAI3JpgiwuQaLJjiZP055AohdZMAcHrwfqeKy3A6h_Z9o10vzpDLUia0AMB1ALzGJX0XSnXYLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M3BFHN4ksbao3n4VR819p7l_ZthjAcqVYFAu5lKmPtHHaThp7m5P4Bj-578NeNxPypoc5YFFXI8JFqIvvTndxNlx6nxoFNYI4XEFh2nCvmN2EAsg08QknOmqsBH1T6QSU2AB-miRzysOGqhiCQZgf--49lK6tx5hK0YpmoNFLH50bEa7BCFSfi8_-lImhH6WJwvOshJfOOcstU1x0jd3_4qwfMBkkH6N66rH84r2UOiRAuFnm19pplAGfiFLQPeq6U88G0UmbSfLG48QS8tjSk2dEB-w4VHGf8Y6ZZ5E8mJKnNy__0TNO_ZjAcxdDPJAkV9k_gc6TONiuazeWthfmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-xKaGRwjX601zFfWywfTvSrBqJoL5lyyfFlN3EDyxpkn6LwLaD8-5dGR6Z4ijjQo89uZ_gONv3qe479x-zre8gOgNNuZiuHp17EHJ1WOcyKAYwd7whHhri2VofvGzgFdU_yOTgA9une-xe2E8XnL0JfPHwqTOe731DTs_CDMTjZoM5TuwF0_XM1ftepShSUev2PPv2vKpTM4p-5mQarybiquJS74bk968CGAYNtJ8juxt2y4noG7zdlHTiY0SvMZfRxKi_3_kPs5D4r5aevc53sKQI6Rmac15KM9gQbT5Tt-Cg1zmT9c4zjnHSdwkwP5r0Za4IKJSgnyvmjWGWKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYzato89CABjDJsKiMxOpBUmPj4WwNOihryivTv6RU6aSZon9aXUWFvhMiH8V9KQjMDs8Tbn-PFpr8PA3GV1Hhf69WcT8kIRSe5qiLBxOOjnv6Dtb0pC2UH7iCy3jjeGwac2Sqhv8HGyTphXppmZweBiXO7PiOtfzH4Uzwg5WpAiLIsjJeBKIhEnj1KxW0R5_-nIfjOneMPoOe9m0eUY-XUFs6hnanyc5xcINN8l032qEy4AT57F-0mFkwHw2WFrCgoCbdyTCDA2UogZNeTH-c_ewGO_clV_cZxam7_zRfIgFtO93xJnibWfwknR4__FobHa00DdJr_HwFLGiw9AVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=I6UvRMeNqQkZfK8qmM7yPk2TbcOfMv6GtseeBK_0izH7zF__KlnbTRONaZMQoC8yDw6WEhgRBjC0WEupg0qIVYTtEk6KF0WavSNL1YLvnAo_iW40WoIlWC6C5O2Xh0Rpf97xs9RFBaXpJQCT8phU__miO843ZnB1HsJf1YMlaN4VUfMrkK-J26EE5r3qze1ld8EdCqL7PdrKyH_cOMKY8YiU1kFCsh7nmugJc36caIbA5FqbUqLwKnJHnnKr3jJgKk1j4Juqnx_XrXWFcQr69lgfdef59KMKsvW4RzwD_f7NdjTWOj0wapxwyfMgXF3TVGdCJlR6gaKbCPwA-vfJJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=I6UvRMeNqQkZfK8qmM7yPk2TbcOfMv6GtseeBK_0izH7zF__KlnbTRONaZMQoC8yDw6WEhgRBjC0WEupg0qIVYTtEk6KF0WavSNL1YLvnAo_iW40WoIlWC6C5O2Xh0Rpf97xs9RFBaXpJQCT8phU__miO843ZnB1HsJf1YMlaN4VUfMrkK-J26EE5r3qze1ld8EdCqL7PdrKyH_cOMKY8YiU1kFCsh7nmugJc36caIbA5FqbUqLwKnJHnnKr3jJgKk1j4Juqnx_XrXWFcQr69lgfdef59KMKsvW4RzwD_f7NdjTWOj0wapxwyfMgXF3TVGdCJlR6gaKbCPwA-vfJJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/abQJtencrsM30FB3X-V1zxKJhMxmJoZrsZmqaE7yMeTSrRdFG-FMjVe8AEOT0JFYtC8coSkk7NT5tNMI6IXGlOCh-qAafkfRDu0haGYeOcQEHbIgfhorkv8B5hNhtbVfk-Cq7XvCbSn3CDdWcPMGGOYZ-tTjn9qAh5Mai1TFntzbCMxhtKa9BsHVT4Bi9leGNRteveAnKTEaNHi5_EoPPlkRk4VoRTw84x1M4k2VwDta44OD35Q8e29rL4H2Q1jx9eECBMs4GJEDRzjxjTqTYTegOu4YrPQVXoaSpaNZU6zSejfn4K6NRTxyvCOf5qNEyV-65a2LKTJ0sNQaAqcj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N_YyHhcZ8TT9JNntu3atDD7U2hh8PzYvuwPSdMZr7TG-z44mOLCnN2AkSi1N7QkE-Y0UksRkJ2ZdVeHTu34YnOSAZ2CXWzneSxSLvJ9D5s_EdVslRTA3qFnHdYV7xGwo-SgB0S2ZaINoh5h_E3Qa-j0lCx5QcCvlGy5rGXAnaghg837bAISjiIMtRxQwKalbB_KBliDHRQBdzPwrxeHKrdGQliBVBTKSFrWtTtr4NrdAGgZFyZSMCN48GTFydbvMrfzwYeQ4yvba8_H4M47WdE75mEPutuCK4ZV7ng3RqPPlj6wxJRW-gwtvf_M4cVfG_X0qI_Ji8zqMlXaZNFoXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WofTzIDmyJUhW8xywIxbNZeFzvTiMxEzt0fvXMukuLxOdXWg6Ecz7QGPbCzrG_UDs4CckgiwkqyMCNo8KL310L3-RYTiUQ6HJ9FFIznVDEWR0a93EtJ0-HKKxd7Nd7CC5gLQhdeItxTYVBEN6DBHvqOx-mQiaiU_tXx5TDdtKddvlGlx12IcG2HopgMWVsuqN31omSn9njzM8XE6-GCbFzXMI1B_8HtVZ1JF01cCCr9gg7H0LeEARdlXAXa9flstBzzwlrVKoSalzgcjW41AIdWAjJ4rz8yu6JG2GYW0z5d7rzY7t5QVNDadBE_XOaKsw73Z-OlB3g0kpQx-cA9ZMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rb1PoXu5TrZ8XHTyJJIG9-HwkNLly9yb3L_dRZOsTXK6hBC49551USbCHv3IujaDC_x4GF89GThocjcyH5QEImKJEFIHCLRHRNzTkQb2CAcuwDcj24D5eV9--LkxxJ8GCydNyLi-yJ1gO-LUwHHNfAgTT2YM2Xwqnwel9kMoGXwOtTKTH2pgE9PBX8j8NIW9yHVLhNJCuUgnV8h_gj0WU-YddtYT3iDFVAuCgCX19q0DPrV7lkicfby7LnvmdKByWkpaWftslLogJhJ9xOlviFrx3fWMTBspYEx9Cx2GKmSMr6wTvti6f-t834URkDlHlPPAs2kGV9IyqLMG8xxBEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/llc78oqGleWh4gn8JF4rZn1Djq11Sq5gji5GAcg6Rca-TVNtwa5J_mP6Prl-dJttrpc2zea1si4wTMmVIffgtdwvClueOqzAkwcyFt3nRByAeRJSuOyvkFaj8STYgIQJUtOFaGgSvIP0kb18iKiB7xUGDgzWuI8q5tc4s8bdNoV7GQnXxRHw4bLH2dOlGuMJTMrYVhrZWkpaIqzUnltbM5AT3DOjX4aDfpHVKiYEAUaX8hWZNgRZasC2yd_UXBxP1QBKyRaKblVEzkFlTwtAzx4WgcppFIzFrxkYYED0uiFpvQIPB4O1AbJyvsKaTF9hY4gJlfQwVV72A1xcfGL66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NcxMZAFLfdD8_iOjwmsIxmtomUYVnWZKUCnNhrRDIdbYw3cpqrk4PNmx3sKg13V5BS5OXCCfripfL3ODY4LkWTqeVMCD6Ltzc-Z_MMTgY3sosXfyLwQxjCeyy1hWiTI_8N2PSohny48v-tXa1i9LayTzoR4ClHN6DKiEOET6gcsuSKYSvpB0nexK_ukrgkna4iSh7GDYaun5CslabWu4gqkw39YINwNQxt79GqK_dOJfBYnCZgOrI1sCrbH14UL9k6tEvsZglHdOnz0Kdmv0sK-9r1xp0BAmmZnKzGBQ440mFgiaRICjySv6w_6R1eNDligwDZUKSnDlu4JafE6fKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=TC4uck27JjrMTd7hChjHAB1R5uy283XQn777SIUa5cTLfJVw8mg09e80VDr5-cuKXlMrFowF4HYUcmxpDumnqADIthIhmwzqBUywP7JvR3QCrnF_pcvzkj0LfDjUTvONWwmcrp3pQeZmjeeo1xzu9Dlz__J8FB4SrzEWvD4mqFXbwLpIfTJ1Dr6JdxCUdasqntaK9ciXbM6Xd8HuBUoWtMWh3DTm9vzsgdcnp6oynN796dlcE5ThJBoBMFs1mTqML5Fl_9I5rpVSwrrR6t2OQAcNbNqqmJAS-7omYWw_PdSGvzymkge4iFpCNDZRpa-ESp471nutFc6YXQC8QQ0cgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=TC4uck27JjrMTd7hChjHAB1R5uy283XQn777SIUa5cTLfJVw8mg09e80VDr5-cuKXlMrFowF4HYUcmxpDumnqADIthIhmwzqBUywP7JvR3QCrnF_pcvzkj0LfDjUTvONWwmcrp3pQeZmjeeo1xzu9Dlz__J8FB4SrzEWvD4mqFXbwLpIfTJ1Dr6JdxCUdasqntaK9ciXbM6Xd8HuBUoWtMWh3DTm9vzsgdcnp6oynN796dlcE5ThJBoBMFs1mTqML5Fl_9I5rpVSwrrR6t2OQAcNbNqqmJAS-7omYWw_PdSGvzymkge4iFpCNDZRpa-ESp471nutFc6YXQC8QQ0cgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVmA-gNzSTIGrCWnEKa0nN81EI-ysoWCNL0MPyHmFa2Oq_7Qt4EY12Po_iQkG8f0utJJzYnCVjjBMegp-g4cXqNPxxVkJ7fV0BV7CAlCdBpe6WCMxxn6FKufoWvNOjmfT6eoOrp22fWWKXfXOlm8ygygHtDcCP_r8-r5PrT5n5A30N2JoOUYy_ISiWdoDWm8n_31Gu2s6KgwagEQwNnJwRBxaYRcF80d3wOklXKSqKWK2-JnFjVOduyDiQK5f-QOb84rehT-Zh3_6GmaRk5fOBCYFO5eYeYE3auwuQl5DmLClMZTZsyLtqFdZQkuv0VybnFgqkI_aqdtNCLZAelFWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=UmwS9i5EYLIPol4dtJCPwHOi_56WMKrB-rU-P-1X0j-lCxh5fFzi417-pw5qO0WiSYFAFtoU1DiIFkudVH6ldHfnMVqcaXDxArdeEwxwftSmkYEaTP6Sc4LxNRtush8XWBIYjLr__151_S1JKCCHmoaIHAoNn0Pc3A6GiHP08cCoSgfB-GO9g-ECQZ_vFiOBE26hIiihXwnD663W1Wxxu1u5cn3KbHBkWJP72wIG9o4fczCUa3BW6XWPxzLZCPWKqngoBdfgIxpEnBKZhM8ztVY_4YLfGbnxHQta_k9PVwR2yfU5_peBOBpq2PmXoa59MexIhFz9HUjzo1qjzkd9hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=UmwS9i5EYLIPol4dtJCPwHOi_56WMKrB-rU-P-1X0j-lCxh5fFzi417-pw5qO0WiSYFAFtoU1DiIFkudVH6ldHfnMVqcaXDxArdeEwxwftSmkYEaTP6Sc4LxNRtush8XWBIYjLr__151_S1JKCCHmoaIHAoNn0Pc3A6GiHP08cCoSgfB-GO9g-ECQZ_vFiOBE26hIiihXwnD663W1Wxxu1u5cn3KbHBkWJP72wIG9o4fczCUa3BW6XWPxzLZCPWKqngoBdfgIxpEnBKZhM8ztVY_4YLfGbnxHQta_k9PVwR2yfU5_peBOBpq2PmXoa59MexIhFz9HUjzo1qjzkd9hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct-uWyKI_dJHk_9r5V6KzeL_q1mlFq6i_fgrEY9O9loO9qr3f_WBNIpDo_ECw_J_U4L6NcQCJFtQBGJiMOatPAI9qYjI8KMY9VfEOvmGsG_aBOCLf1K-dP03OCAPMp8mvdSE7f7zqyvFirn01gG3Z60YMpO22y9x4LAWJBTT569W-darI3-8QWV04lIs4E_k76AcreuO8Ob3Uw4GkFW5uav_VkDmmwmHu7FuvgAjJi0gH8sZtyGzseQCG9_8Y_tjlnvZgs4u1io-Qcc-PR1RvQV71uSVK5xgWWXeli2OIcTPb1MM4-9sRBLXQIA3hwQ3USGZFHWG0YhCh1P3u4Ahlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggqhbzMwbEzLuZzYa9QEaKaMbFZyU4Drq-7cFPF5YabZMpS9216h-0e2j_BNS37B778DEcxJRXTm2ZwKPa5Z4eEkbR-_SjPqdr5gJogrpUlmt78l6Dw8ejsDu3RJWSbdILJzimZcheWGhSnTFvHgWql8FEtihNbKrcTV5Ml6kNawEcFwJvclR5YJNvq5gUc0PH0qI8A5oh_HngUsZlOeBnP_xcLrr4u0HA7ofgOYoxPgosTXqBD0_VrI4PccAr_bRYfU8Npy-3e-ia_dBdflXW5IKdiU-6JFPxFIQlCrMupS9ELt-pCPdxVPvDKY7Mx1dH3GgwQQ_RySEUR0bd2FKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRS722_Q1p8IIYAT5xGVdcGWg8P_L4z1i68S05cKjyyy8Frk0fsJf5YtYS6WMr1wq62H3ofZ_zTIuIp6CLubrMaSx2bxE_3rm_qyIiEXipYq9rR-x0qiEAaq3lkyA6wvXPhp38956Gx3V8MfLDkMdTuVQY_CEe9WWOuhSGkw7TEkqWYs9rK0ao3-RK2x3Ojlg1wGmYYovNx6rRzjbl14f9Forn8-aDmV9aYjYaWNbJbeNxxH1UDhgFPgC5PltP-JZyWrXnWG4Jy9AQvAw8lESTibQSdlrlHnIUBEWn6eeWHeUCC5EwcJDP64Yx3HjEO0X8AhNOMvFiPG1TOQQjvnjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPDrJC7EMe6WzC-F9T5pRM1q1h9HL5ebipDvqkvdgw6ILV0DzLVyZ5e5YgQofyp1XKIuqvke7fVOx4vrmB7MHomWAlTuuLXnKA_idQQp7Z0KSWAq2nwMs4aSNnfScmL0ddRsZ35AeR_ANUvXw9hhM1HGdhQRaCFqbSua34Q8XB4zUgSUBE1vBGjii6G6SzEgEjXIDh1dBF4Mw6D5h8NzDDmEL_5AfawNTGSY-YzjvnNpK9QZlkHJgpOC_cJ4Un2gPrvUQKGGq6oUbucqNAMKHP394tV0zPXdWYBvjUGHwYYo6SxwbkWHtL1lkbmjJBgWWGta0zArWdbupuW6ebLZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/llQVGkqxclKImJtYuXm2ANcDkafNbsMegJoCSOX8EufLM8UPLgGFlJB0JOpSk1zrgV2eUPFbKUVIaQcTSNlrP056ydhMrCR9g4rSf8XBkt3GQ8lV9lJGUFPTJpecAZvOgxqr65Cf6Z9-OQlw3bMFK3Ssv6hOklTMEdcdiG_jCdule6zEba2xLK28EsZ-OHsvEkM9Ho5baXpa9lFbtORhz8DuCLIAuJFukB2sxNl9RE7pkF3QGG8LgyuqFu2n7DDhTmo4w5RqoSnjnAjA5wy9lfQXHHfdnQOA4u6lh67pUVxHBZrhFlk7qSJpXZR8fS89VxVCfdhyVNVBRENEpKkq_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=qlYH3LZv-pd_aeu9OXOvFdPLgE0v-7irofJ57f-qJOezejNtuu23H33XIHDfDECVvhU0yOK3EPh5rjyjFtFiAR9kNJVID9QZl7NBgfJU961eMX5ygsznH6FuJuLUft8XXRF6hTtdlt7PitA6NdLljFvhL_1DyW06zWRdyB1B334_srMEvyBXltGk6sXhVsBbXc_KqdcjoDXZ4HhOwP3QNikd4BSeOi6x8kczCZLNXImmQjAmZmkcmJmRhTLpuYSRvYmjhS3NydBi4WJGSnULrwoFsHy6QlPGsDhS-GJ469HkfbeAe00FdHuoBGADDkA2IxiGCb-7W_lBHHu3fq0_K4jcYtuVKnp0zDLvivWQMF_iSwiwSvOEyL1jCztiqk6o86LcGSrDwBD7RlAa5Wmk6X6tDf4I-YqFX5QUO-CP2_zAkU8ICa8qds2SvGNcSz5hETStSZUmKCqLg7Q3rOUZ0ZXiE6yx8BA7aIvwv-ExaUCcLKv93H6pEUnnjjKfQkqeySDro6M1XmkUQhYyqciO_DNbkR05uh1fEmwy-StlcaXPJbsmj38Ha_pDnlvVDTE84Lpsgr-bENrqdvJcuD5UykKbaMubxinhVIOMHDbABPKUlotJLs6rgOuawQzdniTH2AvxIqxhzODoXfSenYKK94w-dgYufzdZxrBypivANVc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=qlYH3LZv-pd_aeu9OXOvFdPLgE0v-7irofJ57f-qJOezejNtuu23H33XIHDfDECVvhU0yOK3EPh5rjyjFtFiAR9kNJVID9QZl7NBgfJU961eMX5ygsznH6FuJuLUft8XXRF6hTtdlt7PitA6NdLljFvhL_1DyW06zWRdyB1B334_srMEvyBXltGk6sXhVsBbXc_KqdcjoDXZ4HhOwP3QNikd4BSeOi6x8kczCZLNXImmQjAmZmkcmJmRhTLpuYSRvYmjhS3NydBi4WJGSnULrwoFsHy6QlPGsDhS-GJ469HkfbeAe00FdHuoBGADDkA2IxiGCb-7W_lBHHu3fq0_K4jcYtuVKnp0zDLvivWQMF_iSwiwSvOEyL1jCztiqk6o86LcGSrDwBD7RlAa5Wmk6X6tDf4I-YqFX5QUO-CP2_zAkU8ICa8qds2SvGNcSz5hETStSZUmKCqLg7Q3rOUZ0ZXiE6yx8BA7aIvwv-ExaUCcLKv93H6pEUnnjjKfQkqeySDro6M1XmkUQhYyqciO_DNbkR05uh1fEmwy-StlcaXPJbsmj38Ha_pDnlvVDTE84Lpsgr-bENrqdvJcuD5UykKbaMubxinhVIOMHDbABPKUlotJLs6rgOuawQzdniTH2AvxIqxhzODoXfSenYKK94w-dgYufzdZxrBypivANVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdur6BPbd5CoMEMb7hvW3kId_OiOSz431ds7_oiP4nqPAMTd15DnHyXa8hVL-gmsYJ4onrIDQoype-MkibupZmwDM1a7a6Eda5N4ml28jAmmFaQ1x__7uHzeThCcKnMbyulKXAjmIznXqKpJWYXAUqdv45YIdlUn9ugfjRgTk1WAmHgcQpe0fqd5ZzlCa3l3dy6SxnsvK7EeA9-DPTdK_erF3NZKVUOmoXbkyJDKP1ECfyPUaAes4vx5yNJM34ZRk-NdZIe7FtQnke02qvB_TGuC62Yu6FVC-hvgR60L7m690m9k-8oqvgW3udfwK_tb5owwVb5Mzqx31yh-JoCrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=JShJP-t8QtYzqqDcLQr30oyw0h0bGlVeWVb6rPTCRq2tEuA-uVGmgk8mIaHBoO9MU3xjQkqgL9oTgLQtzx6CdGUfnDo7N7-e-vdFAyEGoTSe2JgLz7kOjwoq5Lrsj9uv1bEM8nQq8m-2tzi2sVln06zCtyt-cVhkzNB4kQeHubozWd6EogLExMB5EXwDFuS_3L5qEvSOYj8WaFEowvOLtlSNPzxY-0G7M_PEe9qtOy28hftXCmuCLi8n8F1PKYgXQ3tyfhAYsKlkoqbLHv4fKvPZ0KZrhiT508NuC3AqIpvvv7KTLZTMtg_RgchGYCIaRr3iKMlHIpfvHR8AlXNLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=JShJP-t8QtYzqqDcLQr30oyw0h0bGlVeWVb6rPTCRq2tEuA-uVGmgk8mIaHBoO9MU3xjQkqgL9oTgLQtzx6CdGUfnDo7N7-e-vdFAyEGoTSe2JgLz7kOjwoq5Lrsj9uv1bEM8nQq8m-2tzi2sVln06zCtyt-cVhkzNB4kQeHubozWd6EogLExMB5EXwDFuS_3L5qEvSOYj8WaFEowvOLtlSNPzxY-0G7M_PEe9qtOy28hftXCmuCLi8n8F1PKYgXQ3tyfhAYsKlkoqbLHv4fKvPZ0KZrhiT508NuC3AqIpvvv7KTLZTMtg_RgchGYCIaRr3iKMlHIpfvHR8AlXNLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=WTfNkxXDCYoGww4ZZLMgJJPWnM-MRE44FXM6Y4zml4O9ofHR_FG_Fl9bS3fzXalev2uIPT3bsktYGr0jJ_6GB-CaHT2HKjhfif9EPKs0WeaSxyysF-31i3XDaVqkPPZJ8kEK6Ds2FnTsKadQ728lXefFp4AFe6P2Lb7zlxWi590cjZ7y17ezaYotLWoVWH1bkswB3xJet5CcgriaPASzVhIACAIrOIdF7_VSuiP4Vrl37V0Z3zQIHbyhPFvotApvQZHhj-j3KmuuZCMSktbvemdZCMcTeoPwuE-wUAN8QAgxxIpmdgaqQ0rH5kYRduoe45K1qtiY9zvgAiXwFdqlMw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=WTfNkxXDCYoGww4ZZLMgJJPWnM-MRE44FXM6Y4zml4O9ofHR_FG_Fl9bS3fzXalev2uIPT3bsktYGr0jJ_6GB-CaHT2HKjhfif9EPKs0WeaSxyysF-31i3XDaVqkPPZJ8kEK6Ds2FnTsKadQ728lXefFp4AFe6P2Lb7zlxWi590cjZ7y17ezaYotLWoVWH1bkswB3xJet5CcgriaPASzVhIACAIrOIdF7_VSuiP4Vrl37V0Z3zQIHbyhPFvotApvQZHhj-j3KmuuZCMSktbvemdZCMcTeoPwuE-wUAN8QAgxxIpmdgaqQ0rH5kYRduoe45K1qtiY9zvgAiXwFdqlMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=F4hOVlPYoPVJPrPeFFbLtIyOj2aBLJlnrosH7ITC6glkQhDuabLFFNn5utS8uAtzxlpZRrQ4nGtEpv5PUubz-XAyttsBtdYVzQWUtYys23Mjja8eMv2m3W8ucTki0KNmES8HlmIrlOOTkUQydvlIfqUBk8PEctDCHf4FBUxQUZSeUBbgEhrtL5dTkSEJ9rdgWlqg-mNLq2l5tbSPBOo5EjALIpJUxoHWlOcTDYKyCsSiSGXYKmdUkTLpV56U7ToClNNeSyxJLAcMGpSSyIDkBW2nXgVxPh-7ZQj56Nj7OFhx238b0i08UzhmTP-a5bgvB9M2DktAK-fL38VxUMAvcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=F4hOVlPYoPVJPrPeFFbLtIyOj2aBLJlnrosH7ITC6glkQhDuabLFFNn5utS8uAtzxlpZRrQ4nGtEpv5PUubz-XAyttsBtdYVzQWUtYys23Mjja8eMv2m3W8ucTki0KNmES8HlmIrlOOTkUQydvlIfqUBk8PEctDCHf4FBUxQUZSeUBbgEhrtL5dTkSEJ9rdgWlqg-mNLq2l5tbSPBOo5EjALIpJUxoHWlOcTDYKyCsSiSGXYKmdUkTLpV56U7ToClNNeSyxJLAcMGpSSyIDkBW2nXgVxPh-7ZQj56Nj7OFhx238b0i08UzhmTP-a5bgvB9M2DktAK-fL38VxUMAvcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=u8KrA8m2f6bcc568EE5KaM7lQqKLsNxWv73AiAKdn9ZaJmdepypDkTDXYs5ormaYQgC3rM6Pi9nGeQNu7VNuujimwW13b91qz3NWgVZ-xpx-9jjlcevTSxUQZWSb2qTvRO43NbjvbVpz-n5vKN5aH-s5c39URSy7ldVJ434WWamK7ujz7IMFDoUe9g-vajWhOJ-0boi9pjz-ZMkl-ksYdTQZPuJatHtgc63P08uaLN5lV9OMu7RCX684p5Yma7Szwafsz7rhVcR8ULSTiYJpxAF2goaMHVxiWz_KUIrjIshm2K-W_ZoKF0SIfRlU3T82bMAMqgx1AbbBuOtkvu2etA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=u8KrA8m2f6bcc568EE5KaM7lQqKLsNxWv73AiAKdn9ZaJmdepypDkTDXYs5ormaYQgC3rM6Pi9nGeQNu7VNuujimwW13b91qz3NWgVZ-xpx-9jjlcevTSxUQZWSb2qTvRO43NbjvbVpz-n5vKN5aH-s5c39URSy7ldVJ434WWamK7ujz7IMFDoUe9g-vajWhOJ-0boi9pjz-ZMkl-ksYdTQZPuJatHtgc63P08uaLN5lV9OMu7RCX684p5Yma7Szwafsz7rhVcR8ULSTiYJpxAF2goaMHVxiWz_KUIrjIshm2K-W_ZoKF0SIfRlU3T82bMAMqgx1AbbBuOtkvu2etA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klmVVCKLQWTpend8bnpp7ALSMo3VfmQuE2Bny6PrAzCgeGPWS1Qky3x-c2Qef3HCrwX8d_q3HfYMZH1bQNNlaPQXII0KQCw1SXK12T4fnzoDl4GsWvQ6GnwEXnErNUYErzgPPCk_pdakf8w1LK65Q4xM3ZyapN5NiOwFrlwK0dqNlgpoRTAA339YMTNO0FbM2hj1rcgYADOstTZ_raqsx4XcaSluTJSlwy7t6d31oNeZxe6qmWj3ef2Q3YUBkSLd98JitKqzhHw0PHfWt1lFV-GtHcdh378Gk7f0PmBw4QF5sm2svWP7rDDsP_0BeEoBQdjDkHpHy40O5e55XfPw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chXN9RbRiPQ399gxbOXPXswZnTRFlMyH7QwJ6JTB29li9cON3HTIC6kJDHJhyBn9KQd7NZoXaf62hjE4YIzL60vZd7PH-s1APibn6yTWzvWCpqiPuolkeO7dDTB_V-iNz8M3BahEEkSDRbnDYnctBIh6aBHwGJkyml4cwKkiNmEjowZ3rnytPvPaQSpOiY2rA5mnvGY7xcBTs4j33zOL6ieOO2-grsC0I0JFwFf0-523NbND-qtKtC37XbXgBw2A4ODNyX7ApQoqXVURHJiyyeDf_9pkUOCli9vy3TJvy9EFzW0Mb4xngFiyW-AzfEskFdVRUH2GhQGMFQpttQyl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7W3iF9hn1ewLcX6Qjg375_rgXLmXGLEgLOXO8P-LWASw8bI7LnLcakqPUToeW20OLjrPNd4xNxZ-ZBnBRmXqnv3chYXfNzIBv5t5gTEhFrKKEAmKVrxrIoohfFtws4-erSY_FZQFO2Zj7z5ls39vpWV9z0XXQzO78OFsKhXjK_b0K6jectJQ3Amyhpi_RwvJQlYpyX8UfDJ1JbmbqPAWeA0QFhpnAv8erBqwJP03CdwqOgo0_nawTdEG07HHesuXBc8IcnMha6IxZaa-MBGO-lSXXz4OoTdpSvawMt9ixzfmj-j7c55OYM0VrnzZFYJDuO_iwtmKh7m8e-iVX5g8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVO7yzO5BSflWKR_h3YijWQ1hzw2AIaAUGlBJnknt6-DTu540isuc5s5gxmSEiWIwpWqHWQhWZa5FNTf2rFyjxBAtlZn1zq2CxffTAejIaEmIlc3L3hpf3sJt40e0BlQc7fUUSrak2Z2HUwf-BlP8h87AE0k6Oqje2JIVP5BiVwr_4ZQZ1BFmODJv4BEPOEBgJ5QPZ5vk88o3s7oAr_9jLqExtn0wygk_9F72TIQU2GI7p2TawBEeX4xOgdUeMo9X8-gWGUWoeQXtA2QQwUH3G9q19H5qm6mdoBsks2JK1BzzFKGFQherLO8KKiQCuHycoY0GquH2DIkr48dAHsh_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G8t1g2XIO94RdSs9LeNaPeIL7qgNG-OEQ-xeCmh04Pw6kfC5MnagNO9KZ6jgbrkScSDQDYl5ps94qFabbGw_hublhLy5gHqrGG2UR9LPOlafogbEq1MyQ-XyO5T-Jaxpzw4_yDGtQ-rQ4CzrAMAm2HypkFdKm3wQvKL6EgLhpyQZ5cM_UnJBVE1_FfNw9sbJeKohwv-YPxrB6lrxYfz0sJQVJwlg8QvmPWjQy-WYzjEBsFCS2yMUN1GVe-u3fiSAf78WwsQVLdQbLRhqwtjYafsdAuvrdxLiIWBRuPNjsH0u723790UIEXY705fT94r4UjYvmHL7VYAL29D_qzHDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l73XjPKbet1x5H0Lhlg8aECP4qT-uvkoJ8jM28diB3VFumg9QYJ0UZLbAVd25U7wlbDViN02q67xHFX4YECQxtI_IgE-HNJ5j03YsiWlDtZ-QWLBK5F_p-WvqVwaS_P1ZCARcyC_QGHYFklw1vvflScgV3xu2d577QX-mvaJpswhoHT4DVCgrojtygiv0GFM0x98df3dLwkuvZe29yP1Wi9vnlpLEKeb-z0LHWGJr2syTd-s4kM4IvTAtFvfvcdHEKRhP4CQZqNukAkw_Yhnu6fNRGaK6PKPJ2CH-DhiF0eOt71SOa5nfti5lDdaSU_yujUYPB2ng7l2_f70U2k1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGk4NJfpsYR3GGG0R9PhQuoyrfHC4EJ-W3HN-SA_neFpCkWEgF5P1TNeq3Kktbp8UH63aZmV5aWwKgmEx1uUP_UahfW1AYa5isl3l9taZlD9795uWWjWEs0P0HyL6RVut72e9gBThu3OYoO9PPTgxZGE7d9NCuURHUDnYVIdkOWvgnJvwmYyhwcHw3VMAp-XiwTK3oFrDRPI_Ja1aGfn2GJIa9DSNC8WsvYuWKmOTU3l_SLGIhOI11w8PF5Hs71X_W-gM1AAzdLzHpIU9WJtgRrDt663QoBhZydFYrQBLNSEtkFF3NSAGZlWAFAtT2r0zuWxeS0Lc1B-OT2jqpX3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9J7CclXFx07xzvogxoLHIMqPUO-8VPOZBXxIMtGP0lQH4wj2M2PExUDIxo9Vfgf4fBFtAKHIJydxguslFjb0AtGdY4BqeuIDVErqsS2uW2MhcwGU1J-DMCqmyLKfFvUQQmmzla9DSgzpUQ1ZAPLG03-7-DhOfZcEV_SL2WX5Gkh559pLtx1NrF-dcBECyyf-47e4X7kdPIyI0X-vYPRowsQCpaAUFZBk4hCd-BaUsHqgvWx-W6-p2SwBi4mEpP3VQQKVILgd8oEywtOgeS9Hz-FQ-BB5pZJNWHldlhWtDYhFecwt1fJzdRjHjCtmF8jP4sj-fzl6ESRnDyD2qIWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSUhLerRN3Q2Gw9qEZZcUO9zZ4KrZ_vsMXnpmnVAmjKEsqSPwJB0blSVqfFkFOdOu9PO2UC4hwFoaccWzGO9kX1flKL4-x0Lb8A0LwyvrXSteIr9jJ6DH9U7RXmBP8d7c7FLe6Jtjt51VMlTmn5lLyDpO6Ny-POSQqPE7oF-ICxWj9oewswgHlh9YHlEwbO8dwOqt71hj9sL3uYfCUqB4v6Valt4s3QfoRHcqWhxnCfUiRXOt_21zLGAiDXejX2FW2ouJ76Y0XS2FeqZb36ukulZQPPkmk-MQ137jz9M4PlD-hsRi8FRpXwtZMpYd4ho67F_O3528SFvOEeqXv4T6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrkOpU3S7sUZLm_es-Vmd_H8xu4IZFl90R2bvaO0cu6pg6QoQ2TLBcDJ3BRoGz9-EygF8_qcC0eMfv3vkKKPeJHXaS75L882YsZaMhUfWHIoMgeblKhD_Hzf--aVpeDX6I-j9DCM_jVndury7qjbgeVsYq2tQEB3vu1QjI4o0LRwXwCp7rxPO92K-v_sXFY4AG1Y6xObQMMAx24TaF_Oi6tmg9MDeYTtt1KZc3oPcKuPCUgxxAFXvBLTxu-pQ_I-A1a_ctkd7cP4HsRQT6KkFGHyAZMZD-ZrtSotCimwKCja-69Qjp17wrX3lOfnSnq6-L7ZbJyoPy5-6rnvZ8pwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRbGvFlgWolFRhAvxJ9waD78v17YPeuWMZucphfNgLE6gVJmE62l3LIeLwj68cDoQc6dfKKV1dq39pe3FqsXztaY0yzGGEV9t0hhncY19T_aYH48e6iyw3YKiMom0gIJfgCMRF5cubWEeHSpcs0NmJuEpK7LOK0raJSQoqgkFnKeZ4F-m7v74_LGS_K2UxQDDJgdShi3uoAOLVWJjEdLxl0hr5JO-5NR0N2YRVC3Bmj5Fq-b9mT1Agi-I1tJeTu8DOT8XjgpLrsnieu_wYAuHHOvU9cSxcYztWk1MlM-2CuDYwYqwFyMujQOdzCGsIcP4gzO8x9V1qPt8BWLcZ5Srg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fF_MJ3XOElra177gDsT1DWE863tLUPAcsEnSzHACvLpcdqXgwBvcVL_m4Y2UvwS-ASjUs7tV8p6p-iqk4FMm3wCxcN2CjVZv0Yx_VkKv7inTriOU2yO02IeAO048fet0Pja1nkwVHFyqYGT1BhlTUZp9PO8WS-Qlh_zOJgEPixHHUapiIlArvsP5iQF9z8OklGScW1wr4nLwdYnKJO8SQncbTe8PeXGX_bM3wnE0MvYb-3v8z9TRw2ABIXrlHzwty4MQXA1pwU3DYTi6Ll1jYpE8at5WU8SbU-AG2F6HtZXPkfuTlZsOVQXyndnT5uuMFcrkAvv6eTSaW9IgbwDRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYoHbyCxb5fB8CWZSHj53MjXqZQJeSWDUco9bVffhwD-S09-Ocm8hcWzbKEKUY8P44KJVgsF7Z3DNBW2FNRm50WKUTXWt2GU-VwfF4m2fOba-EK9kaPUe_YQGimwaZq_s7_Vkfal-7tW5C1kxuEUv9VP6qL9eESu9RhHelD0lylO8m_ei1Td2xwGzyyze3wDo12X-af_lYlTlblm89P8fQNjDff56nU3jzI5v59PWY5vIzrdOmW4mDW0-cjEAVKD-tOB8L5jMmzvRTCcv50FldmLrCc-oNMz4rZcRzna_s4Lm_cAxHEKAvtyE43zetYfRV3wesxPCa-l8NiVgTQ92w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJ5tq9rGVDP82iFqqWcI-9c3GLZEEBGP5X_kAgzdl7lzvrccr1P7MN9WwrFYTR5kPmDkXKvb53pI0SjLT31lKbmsCHqe44_-EvJ7WsQPukl2Za0UyY0jWxtk0X1o22g1O0wdP-YlPyZfWmRsbpzYFl7k6JUQzIL5-pE_oEVX8bY8Wuy5X7-gmsDkM77B13rjjJz6Zdf3MsutEBKLOCb-hCZdPsIMN2D1by4zmtc5w3ZzE1eERKpEO_FM8-GI6oKMbkWZeOxhG90TlOC3-q6CrhRC4ECXItT3T4-fNcFsxiS4kG0XBZYAqsbCEsyseZhTRuxuunSv-YfiwBZrz5PVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2YCFCbCZU4vJJP-sZqEUb_uf2CZXyMPtQsu6qp6jYDC5StnGT4W98R3cdONxiD1lJGhscmp2idXDipgTbzG1L1biwMc7_8LwChvdA_UAzb0wMXTwjiAmy-nU_tRtMR1EBurohC8UC1vd8QxxurhAtUe8JlMcKkeR7_ZWCosesrqUATWBW4u06XmAaGWvjMGCDyLZXilqXy_YK2wzSgUBDRx7Euk9GTJ8KGwodUiLq016geJqIH0i9uNUDSuOrsO06VV-MtBetOaaBxI061BNd22u3ApgP8ygWeJXiq_1NfIwtCgC_38FiVG4ftgSsJ9Jt28qkR7IbQuIZtRuQV02w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=hDksgCHs1j_IQp4u3PEXbZX7AhD0Vv2yIdwtuwjteVbWUbzRmplhDcn97q7_t6G-6dQSKiulYPqn4yTPFJKXCWSmGe-m2QVgUPiEY_Wb26wjtK3kx8HO6Cfn1YByaNehkOZHO1pHk0RLg7UBQBFeTRWv1_M4kZcJUBqICJ54bTFcIA_wFgnu1N7O7mrvCXGb2GHP04FdUDGoW0aQUHkwao4TvJ4Z-Lft4AISHf0-ato8uoPUnoYyXNG5g3nilQKMVfpS8jYeaJEjxOpjT5EObQe9MxnnBN5yKbNhbctULHGa6ZSkSu1wsMgOXjLOWUzPWEZbv0u8AMzugo33a00XAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=hDksgCHs1j_IQp4u3PEXbZX7AhD0Vv2yIdwtuwjteVbWUbzRmplhDcn97q7_t6G-6dQSKiulYPqn4yTPFJKXCWSmGe-m2QVgUPiEY_Wb26wjtK3kx8HO6Cfn1YByaNehkOZHO1pHk0RLg7UBQBFeTRWv1_M4kZcJUBqICJ54bTFcIA_wFgnu1N7O7mrvCXGb2GHP04FdUDGoW0aQUHkwao4TvJ4Z-Lft4AISHf0-ato8uoPUnoYyXNG5g3nilQKMVfpS8jYeaJEjxOpjT5EObQe9MxnnBN5yKbNhbctULHGa6ZSkSu1wsMgOXjLOWUzPWEZbv0u8AMzugo33a00XAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/moR5wF4n-FPCbsCl-6MLKWmTkAoeR5ERukhTkP5HUBBsKJFR38IERd_-akyo-RGb3B_DymfW_M38zI0UyNVO95HabdR-6PcTnmzEnDXBO0ZltUBJVnHwVWk0BuzQn4z6hmw9V_USqL8uGVryqCPRE0cPaV59VbCzkVvfBv4V0vobiKBlNxW54_I8NWCrabLOQxHp8g4LH0uqSFyL8MgKA7y_j86VfOFdtqmtoxEKrHNVFE2awb19DopLX-5yeA_dfsZ1NBJhzI9Laqp-VKdm3LHZcrpS2quJEjuxRJoaTE8rMlnRKWVquZLRluOsdQLnzMVu1mOLwmI3O74ftdMK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CJaEd3cuJt_4EwP-lNt1tJv9L_sIVuCb9eY7oSSg1HKEnmtHc8aqq1QIKFi954TVw0-k5oa0MX0908GY-09Sg2zqcAFl_un96u2hrGr2EQQyDVAOm73BpG4Sn80DrQDoAqeFKv46YL-gbGlKgXJ9yJPn4ict-gt_54R9wsxTPy8snPuE6tC97jhTsv3B1VFTujezPf8_vgPQtbk0ll0FiQGNs7NCENXU4suZiW-RfC_BrAP54kBPpdNXOrbA2Yn43n0R449YeuCRDmXRC3xiUfc_j8fFOQg6Udm3bqbzp5Lk5svNg5CSaty9iQ1Ol4ivjWoqusnKNtFDS7CI0wufZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=klIRa3ahNAQD-eZ1YsTZthbSMSGdgeF42yaobZpGwRnXS_KVyw7DD2_JNDiLAzDdJcE1QSYk_tPtrZHVIeBnLKx6MiHwllHuvm5YOEuO3lLA1wCoZWl68R7o00KcVBilc-gxryh-YRMm5OF10-zCDKtLvBowRsRin8SbDcGvniLWv-tJcraRpCfmOU2u2ErSWCYGDEYxn-aoY4ZWS-Okcaici17AdM1jExcoFiNcKwA42199YFa0T8fgWuzBAZolgsXQvIRH5KdVrh11iJ10tmPvap6h3k_rYBWiqSzTe96IcfXYPwdU9ra8SJnJ5I1MozlVUPfdeOV2M9wnCGkESQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=klIRa3ahNAQD-eZ1YsTZthbSMSGdgeF42yaobZpGwRnXS_KVyw7DD2_JNDiLAzDdJcE1QSYk_tPtrZHVIeBnLKx6MiHwllHuvm5YOEuO3lLA1wCoZWl68R7o00KcVBilc-gxryh-YRMm5OF10-zCDKtLvBowRsRin8SbDcGvniLWv-tJcraRpCfmOU2u2ErSWCYGDEYxn-aoY4ZWS-Okcaici17AdM1jExcoFiNcKwA42199YFa0T8fgWuzBAZolgsXQvIRH5KdVrh11iJ10tmPvap6h3k_rYBWiqSzTe96IcfXYPwdU9ra8SJnJ5I1MozlVUPfdeOV2M9wnCGkESQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=v8aWC0juf1SHZKqF1MvCOHyjPirr9Beh7PpVA_jkAzhGIHOqtZzoK5QlDqxpr0ZNsSG-FC7z5Nh-mRUv9IXVxQdctN1rdipbJX49u2P-5Y_dy7aOYIcXWZK5_pQaH44BSxrHVEOfGOhwa_fPc6TuM7w1ga8VFomdmIZZ7dTIxgUxO8q7hOpwoVYEXktQ9n3tgdfO9dq5j6GZJ0fAaBLJDpUXc1nNKzwj5e-NAAJK5_Mje4r7lbVyoFWRf0GEzXRfzS0-DkmVjOckKzU6JgOwijnedOaUynGrivEk6UV5fYjZ4hWhO1mAxqENxQYQn9qbrIMzs8h-cmkXUbibMmMA2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=v8aWC0juf1SHZKqF1MvCOHyjPirr9Beh7PpVA_jkAzhGIHOqtZzoK5QlDqxpr0ZNsSG-FC7z5Nh-mRUv9IXVxQdctN1rdipbJX49u2P-5Y_dy7aOYIcXWZK5_pQaH44BSxrHVEOfGOhwa_fPc6TuM7w1ga8VFomdmIZZ7dTIxgUxO8q7hOpwoVYEXktQ9n3tgdfO9dq5j6GZJ0fAaBLJDpUXc1nNKzwj5e-NAAJK5_Mje4r7lbVyoFWRf0GEzXRfzS0-DkmVjOckKzU6JgOwijnedOaUynGrivEk6UV5fYjZ4hWhO1mAxqENxQYQn9qbrIMzs8h-cmkXUbibMmMA2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl3GgWVKsELp8ZsWD3PZTFqpocPsJLd_mFjyaWO6wqEShs6DXAS7gUb3wLxgg44h_3F2qEBCfHYP8u3AZhVOYEzRqyDyU7yCVztA_AgBMG5jq8DThL6dkFttKhqRZytPEmXvGfyg4d-zjl7VX9hxJbJA_B23gOmxpZfajUUKV9-XtWLYlllg2LgLTy8qMiaWWdAiGKOtwROSzasPVYXiMYtPdVQi1C1g7PpEw20YsojFOOP7GEQSoLIypa17C_OR6JMXTmkAxP4_ka86wO540ffBn5tqHkusXhBEZAjbktFU2CNfP77MyS9xusifauC68X7BD3_mXoRu0AAOttH3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=es3VhgsTwnDH9C_ohU6X7AJvm2jutrzhzUdD9ahJUHWls4_qxv9cqD1CuRhY4muw1kZiQvNGILgTr_ulWY7KyHw-wI99aOVCZQ2HQpwRTqmHjWYq7qZgHr4kOBYkkWKcDl8UKbN7PQs9lTZ_3eH5Rs_8ruzC2keHjTmWfFhYcj6dYGBTn4ngeR-zm6BkHbrn9p2oPXB5L7cPBx27RjHdoWRbOtLS7bfpxm4Rxdg2e96YnvIR07akgkN8ybfFCdITF45dxOGjTRK9LlwhGsYFsjxTe8moJlg8SWEKfL0bx9twC8dWTT-iy1T5DjRoaOUif9tiZw1_hExOA1F26o-sJw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=es3VhgsTwnDH9C_ohU6X7AJvm2jutrzhzUdD9ahJUHWls4_qxv9cqD1CuRhY4muw1kZiQvNGILgTr_ulWY7KyHw-wI99aOVCZQ2HQpwRTqmHjWYq7qZgHr4kOBYkkWKcDl8UKbN7PQs9lTZ_3eH5Rs_8ruzC2keHjTmWfFhYcj6dYGBTn4ngeR-zm6BkHbrn9p2oPXB5L7cPBx27RjHdoWRbOtLS7bfpxm4Rxdg2e96YnvIR07akgkN8ybfFCdITF45dxOGjTRK9LlwhGsYFsjxTe8moJlg8SWEKfL0bx9twC8dWTT-iy1T5DjRoaOUif9tiZw1_hExOA1F26o-sJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGa8uNyk-P-XfRS_1mAt1y4ijkQ1HLaYyyQqle4osu9FHu7TfbiVD_ksNQ2tyPKSarCffPXPTL8yqBtC8TEomb0KwGPJmATlrdFYjiI-uMweekFi4fW2pUuYbqNobHmMqU2KqOrV_W4G-HJD70Je39nQ5f5J17FxxBCKhHOqPus4jIzjid5HQTsDzoOe6w_wqmWOOSxfii7wIt0pbUpazMeI_RVPa7O56EVDTtnysfIVMEd2b1rSkOWWdmahC2XzyD75vLNxuBalZT-zlJaBXjHTr78FDOd0ebEfLYbwatOo-BIC7kqb86HIY6etcgIQC2ZxeLfEqg7GT-uEzkvorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، سه‌شنبه به شبکه ان‌اچ‌کی ژاپن گفت بازرسی از تاسیسات هسته‌ای ایران انجام خواهد شد و هرچه زودتر آغاز شود بهتر است.
او افزود اولویت اصلی آژانس، شناسایی و تایید محل نگهداری اورانیوم با غنای بالا است.
گروسی گفت آژانس بین‌المللی انرژی اتمی به‌زودی با مقام‌های جمهوری اسلامی درباره زمان‌بندی و جزییات بازرسی‌ها گفت‌وگو خواهد کرد.
او تاکید کرد آژانس این بازرسی‌ها را به‌طور مستقل انجام می‌دهد و نیازی به نظارت یا کمک دیگران ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76630" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UKLyclx9FbRJh7zzf503U4RIpJWl9EkK3fOdMeAbR7sslCNH046Moea05M4-faD935g4_PFt_iIVTs8N1HNA1AwbKPYGDkFB0x6JKn5qXq-x2c_ZMP7UW3w_EtzskhDDDfGnqUuct0Pl8jiRhGhJLL5JzAmlg0F7iU5ogT7Qy_CfcpRzUj7h0ncCexW5BNsYMB01pc3KrTq5D198xksUkJRdxio0snZiH8lAJYrw2mJl8dxZ6N9aVhCafrrcnO-YXS5DD15IBZYsDKYp4GXrSZmVtdU-DFbW-spjoRYX640VbIve-W0rLBqUyEDbvY-ATTQ8l28Ch5JRqQXam1LYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا می‌گوید تا زمانی که گروه‌های نیابتی مورد حمایت ایران به حملات موشکی ادامه دهند، دستیابی به صلح پایدار در منطقه غیرممکن است.
مارکو روبیو که به امارات متحده عربی سفر کرده است، روز سه‌شنبه دوم تیرماه افزود این موضوع «در زمان مناسب» مورد رسیدگی قرار خواهد گرفت.
او همچنین تأکید کرد هیچ کشوری حق ندارد بر تنگه هرمز عوارض یا هزینه‌ای تحمیل کند، چرا که این آبراه یک مسیر بین‌المللی است و بر اساس قوانین موجود بین‌المللی حفاظت می‌شود.
تنگهٔ هرمز از زمان آغاز حملات آمریکا و اسرائیل به ایران در ۹ اسفند پارسال، از سوی سپاه پاسداران مسدود شده بود و تنها هفته گذشته پس از توافق اولیه بین تهران و واشینگتن برای پایان دادن به جنگ تا حدودی بازگشایی شد.
وزیر خارجه آمریکا در مورد لبنان که برقراری آتش‌بس در این کشور بخشی از توافق بین تهران و واشینگتن است، گفت که ما قرار است مستقیماً با دولت لبنان به توافق برسیم.
روبیو تصریح کرد که «آینده لبنان را مردم لبنان تعیین می‌کنند و پرونده لبنان از هرگونه توافق با ایران جداست».
@
VahidHeadline
فرماندهی مرکزی ایالات متحده،
سنتکام
، با انتشار تصویری از ناو هواپیمابر «یواس‌اس جورج اچ. دبلیو. بوش»، در شبکه ایکس نوشت که این ناو در
دریای عرب
در حال فعالیت است.
سنتکام افزود دو ناو هواپیمابر آمریکا همچنان در خاورمیانه مستقر هستند و نیروهای آمریکایی حضور خود را حفظ کرده و در حالت آماده‌باش و مراقبت کامل قرار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986282857.mp4?token=hmXtLDSwn2AnL0BAU-eXrn0s6TFbkMJwYWhoAH70bETx0Mi4gR7ptju3Ie0ZtuHX6twb_ZuVb8kQXnSykBvyRxl2WuwLMBUyVwS_ETfQJT5pkR9B9N50CDPWS_-9mO2BuFT1mlnc2gRczCk-XChKPVdUenwNr7X57NFmUiDJYS-CPOOObhNyM10p3ve3M1ubva0bF7J-8xOVkbd2CNS0c3nLjFkp3sAruLe3pMn6XXmTQwvkJ0ex8kmze-ktsA_qyJ2BORawJjs1anVB8IpjXAjNeLTku442qgYgm1wukL45MNCelgQMEa_FfEUD6eFS04VZ-04uktpvb84coOip9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986282857.mp4?token=hmXtLDSwn2AnL0BAU-eXrn0s6TFbkMJwYWhoAH70bETx0Mi4gR7ptju3Ie0ZtuHX6twb_ZuVb8kQXnSykBvyRxl2WuwLMBUyVwS_ETfQJT5pkR9B9N50CDPWS_-9mO2BuFT1mlnc2gRczCk-XChKPVdUenwNr7X57NFmUiDJYS-CPOOObhNyM10p3ve3M1ubva0bF7J-8xOVkbd2CNS0c3nLjFkp3sAruLe3pMn6XXmTQwvkJ0ex8kmze-ktsA_qyJ2BORawJjs1anVB8IpjXAjNeLTku442qgYgm1wukL45MNCelgQMEa_FfEUD6eFS04VZ-04uktpvb84coOip9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M20pPk1x7nfiIePXZa5772VWG7viTuuBibKuxgmwbxXoYrm64COdrpaBUpKKUXRWR2pifgM0XG3MJiE6Rd7OrFJG0255Xgt4j60ejd7ZvPFJ_nT8hBb4UTyDeENd1EMbrv_d8EZcC3N_NMASQoc9e18rYhFIbSITmRHsVu__IJu-I9qeFcaI6-tVcTqchDZIBeGcblT49LLAqYM2TdIISspuM97VVWPT_MgFbo_hnlIXSKo5f8cS46hFd6XiMcBKCLNjxnKwX_ExEaP6bmVrUDGAX5ib4B3Cmi9lRtl9QADNDUL4m5q_SDugjn5GmwJ6xFmo5a0LD9dLAtczbfrKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثریا طالبی، مادر امیرحسین موسوی، فعال فضای مجازی مشهور به «جیمز بی‌دین» که از آذرماه ۱۴۰۳ در بازداشت به‌سر می‌برد، می‌گوید پس از پخش گزارش تلویزیونی از فرزندش در جریان جنگ ۱۲ روزه، اتهام «همکاری با دول متخاصم» به پرونده او افزوده شده است. مهر ۱۴۰۴ صداوسیما با پخش ویدئویی از اعترافات اجباری امیرحسین موسوی، او را به «جاسوسی و همکاری اطلاعاتی و امنیتی با اسرائیل» متهم کرد.
پس از آن امیرحسین موسوی که با نام کاربری «جیمز بی‌دین» در شبکه‌های اجتماعی فعالیت می‌کرد، با انتشار نامه‌ای سرگشاده از زندان اوین اعلام کرده که تمام اتهامات مطرح‌شده علیه او «نادرست و تحریف‌شده» است. آقای موسوی نوشته که پس از ۱۴۸ روز انفرادی، بازداشت همسرش و تهدید به تکرار شکنجه‌ها، وادار به انجام مصاحبه‌ای اجباری شده است.
ثریا طالبی، مادر امیرحسین موسوی، در گفت‌وگو با «امتداد» با اشاره به وضعیت پرونده فرزندش گفت که امیرحسین موسوی از ۲۸ آذر ۱۴۰۳ در بازداشت است و خانواده او همچنان در «بلاتکلیفی کامل» به سر می‌برند.
به گفته او، فرزندش هنگام سفر به کیش در فرودگاه مهرآباد بازداشت شد و خانواده تا مدت‌ها از محل نگهداری و نهاد بازداشت‌کننده او اطلاعی نداشتند.
مادر این فعال توییتری همچنین گفت امیرحسین موسوی حدود شش ماه در سلول انفرادی نگهداری شده و پس از انتقال به بند عمومی، از او مصاحبه تصویری گرفته شده است. او مدعی شد به فرزندش گفته بودند این ویدئو صرفاً برای آرشیو ضبط می‌شود و در صورت همکاری، طی چند روز با وثیقه آزاد خواهد شد.
به گفته طالبی، در زمان تشکیل پرونده، اتهام‌های «اجتماع و تبانی علیه امنیت کشور»، «فعالیت تبلیغی علیه نظام» و «توهین به مقدسات» علیه فرزندش مطرح شده بود.
او افزود پس از جنگ ۱۲ روزه و پخش بخشی از این مصاحبه در بخش خبری ۲۰:۳۰ صداوسیما، اتهام «همکاری با دولت متخاصم» نیز به پرونده اضافه شده است.
طالبی با انتقاد از نحوه انتشار این ویدئو گفت: «فیلم به‌صورت تقطیع‌شده پخش شد؛ به شکلی که این تصور ایجاد می‌شد که امیرحسین در زمان جنگ اطلاعاتی را در اختیار دشمن قرار داده است، در حالی که او در همان زمان در زندان بود.»
او همچنین از شکایت خانواده علیه برنامه ۲۰:۳۰ و رسانه‌هایی که این ویدئو را بازنشر کرده‌اند خبر داد و گفت این شکایت در حال رسیدگی است.
مادر امیرحسین موسوی با رد اتهام‌های مطرح‌شده علیه فرزندش تاکید کرد: «انگ وطن‌فروشی به امیرحسین نمی‌چسبد. او یک فعال توییتری بوده و اگر کسی با ادعای ارتباط با اسرائیل برایش پیام فرستاده، بلافاصله آن حساب را مسدود کرده است.»
بر اساس اعلام وکیل پرونده، جلسه رسیدگی به اتهامات امیرحسین موسوی روز ۱۳ تیرماه در شعبه ۱۵ دادگاه انقلاب به ریاست قاضی ابوالقاسم صلواتی برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/De1qUYh-DzxMwOsHIqP_EUgChksqLLQmituL2dy46WLdEqthJ9kXBwcTR7vh6Dzcy4es5Vr8uQ4UdewmP0WZ3JzIowIqIFPRjwE121OnBAVdCQ8uuJxnUTlbfF8tf-vot1PLM9SVz6rmN-A8jOWz1Cr8On3qUV3ATvn-rNLI1jKt6u-mZGFjL_Qlu0Ot9DKuLvd3uIkdEUuWMgXGrcX-soqeBVqQuiZ7WBPHgQRMXMyEsaNcTp-gkGwlUR9rvkwa-DebGLYbBSAkLGGTUV_iHJdOgOlRA94jxy85Tqwi6Ns_O_cGxuYLx023BdDkB-NAc3afzSVz-cczLfOpANaAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dlheKqAn80q8NW2qASJwvifIvmfw3F_eEMqKU18RlrgwkE0IX4uNIzITOM2foBHpSItOFtYX4Sc3ZAABSI5-YML4CX2-n3UpX8zEiS-iZBDxLx7Z03ZYrZZmxZqF1DgZbtyzQJ9i4bJHN0RfeKj_UvsdX9DsMEoQhtScywYXTdenUVx3N2eD83ZHpkpO7vtGi_YIQTjF3BsNtT34oAwHgSSpogZhuJQbqeJvWhMnkTTBJGIg5iQtkWhVcIX_GoxXZJ-XwU7koFNshtKNRRraLGFVN0_raI-fDmIwP1zVxOmiLz16btLC6CHsoUuPIFZx9m0kzK9gkJAkjUlbESI68w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KNMcqMGJw6T6_627MiUlzk1IwPVwHMQCkhvDnkaeLjZJDygPVo2cvWdy2URrZkyGlCwHABf0ThZqP2mvJt_yT4ht0Y2OdomvgabNuiMBdGkbWeXYvl20XiG6JDh-hn5mG7P12dSY8OphGFX493qo3SFpGypBLzDQrGhpgbq7E7EWM3g4q1tuKZeJVrYqm9O35F9sh7-Zzjes4NefbKsrrRY_gYNCg4spb3YdjNlzCYEwoFOQmO_N5ifgLh9k4q1rHUVWlekDdsIA7apqIR2b-aVKtreilwPmWyqFun7mQip4rEdraj42WRHIkxfU9mWACD8MIptE7xLW53QLCFQ-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eo7Tlq7pJr-UXeKRpnisHAYa_xiI7bdpuudQszQ6waEwq1z0hafJuGWWATdSqsHFlt8gpjIPqQzpRGfFHAOc0lprZdJqpdloYGZJfDzd6Q3D54CkT1XpiwkzZlyzmSNtAf5K4dvQJkaeDTyTY0CA7bIzpy0G-KoxqngS_OOHi0FCaZTsgEiUVFmwA2ufw5OqTq-d54iYXd8lbDZqKE_JXH_K5y3DXuBtUz61W1sJyweZ2600TGEmTIZXf1ocBMy1lJnkOxt6BxUZY4T9cdHuckrhK92J4NIRhcajnb9Av9X5-eWXKgppUf61eRH--ceHPUyG_TRzybalY4nACFv4sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HIXPAwcdSCDJiyRtg_WytZ4xeuTfUBZ_QZI7KuN_bkJOvyxPb7i-p1sJp46OmvA4VKILBZZG-sCo7ezs_vdIP1K0jUlJBvBiE1envBlhzKmW7OtmYXNjQNSR4mxcofSc-uKQ_lEXibpIEZJUuUoLsRl2_aJ7_lJCaNdWUrMYj6n036WDi6YUWzsqpXvCthyZ2k-166YISg6GwyejvBAAzjmkNQ5BZRttG6KPJsu14m0RhObSDz2BpjNZ9eV-3Oj0YktihfTA3fAgfF9W8SToj06uR7FfO9AAUuXM0NUS0BHwIYW0E_TASBPPJSMGaiNy4KtDxlkdC8DM6CbY7HUyJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌های کاربران از بروز اختلال شدید و قطعی در سامانه‌های آنلاین و پایانه‌های فروشگاهی (POS) برخی بانک‌های کشور از جمله بلوبانک، بانک کشاورزی، بانک ملت و بانک رفاه حکایت دارد. این اختلال‌ها موجب شده مشتریان در انجام تراکنش‌های مالی، خریدهای روزمره و استفاده از خدمات غیرحضوری با مشکل جدی مواجه شوند.
@
VahidHeadline
گزارش‌های مختلف کاربران در شبکه‌های اجتماعی حاکی از اختلال گسترده در خدمات بانکی چند بانک بزرگ ایران در روز سه‌شنبه، دوم تیر است.
بر اساس این گزارش‌ها، پرداخت الکترونیک و انتقال وجوه در چند بانک بزرگ مانند ملی، تجارت، صادرات و ملت با اختلال همراه است.
خبرگزاری‌های فارس و تسنیم، نزدیک به سپاه پاسداران با تأیید این اختلال‌ها از احتمال حمله سایبری به مرکز خدمات پشتیبان خبر داده‌اند.
در همین رابطه شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، با تأیید انجام حملات سایبری، گفته است که «شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است.»
این برای دومین بار طی دو هفته گذشته است که خدمات بانکی در ایران دچار احتلال می‌شود.
چندین بانک ایران اواسط خردادماه هم با قطع ارتباط و خدمات روبرو شدند که به گفته مسئولان دولتی به دلیل حملات سایبری به زیر ساخت‌های خدماتی بانک‌ها بود.
تاکنون گزارشی از عامل این حملات سایبری منتشر نشده است.
@
VahidHeadline
آپدیت:
پیام‌های مختلفی دریافت می‌کنم با نظریه‌های توطئه که فکر می‌کنند بازار ارز و طلا و...  قراره نوسان داشته باشند و نمی‌خوان کسی بتونه خرید و فروش کنه و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVjiuJfoEEZ-G_s-d9qmH9Uls0o1vZM_fEhv48GbZ0jcwgQozi2Ydy5MDERTgYNwR63zIVJqVD1Wq7SbFAW2WPo3-73NJcCY_ZFq-DfChwaamgGxrFtPN_kgFkGfxyLm49VRj3wl3goZrp7QhGsxLxLVqy9WyYj6QI19Xp53P-75H6JjMM572uCCIx_-czJcjIJ5B_u6rmVTiVOXF4Wyo4h7PGna80qX55eW6-J89wi0MVHZERsqijbNt7Nj_yMaWimeSTS2Sgaj76tf6x2s5BNxN3uj4Mj6BtvAYaHgauER0boHFr4HUJlUOiibAIicpIq2O1-1HICDqakGuwV6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان و ایران روز سه‌شنبه دوم تیرماه توافق کردند گفت‌وگوها درباره نحوه اداره آینده کشتیرانی در تنگهٔ هرمز، از جمله خدمات دریایی در این آبراه راهبردی و هزینه‌های مرتبط با آن، را ادامه دهند.
به گزارش خبرگزاری رویترز، در بیانیه‌ مشترکی که پس از مذاکرات مسقط منتشر شد، دو کشور اعلام کردند یک کارگروه مشترک با مشارکت وزارتخانه‌های خارجه تشکیل خواهد شد تا این گفت‌وگوها را پیگیری کند و همچنین با دیگر کشورهای ساحلی و طرف‌های مرتبط رایزنی خواهند کرد.
این اقدام به نظر می‌رسد اجرای بندی از تفاهم‌نامه‌ای باشد که هفته گذشته بین ایران و آمریکا امضا شد و بر اساس آن، ایران موظف است با عمان و دیگر کشورهای ساحلی خلیج فارس درباره مدیریت آینده کشتیرانی و خدمات دریایی در این تنگه، که مسیر حیاتی برای انتقال نفت جهان است، گفت‌وگو کند.
این توافق پس از سفر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، و عباس عراقچی، وزیر خارجه ایران، به عمان اعلام شد. این دو مقام ایرانی با سلطان هیثم بن طارق، پادشاه عمان، دیدار کردند و با وزیر خارجه این کشور، سید بدر البوسعیدی، نیز گفت‌وگو داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76621" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZNSicbbQc6hwirvo3k5_-AjQ5LzUZTx6SoH_XYYPz7CDcusJ0X6w-Mv7NDGri-suFy9Qrk7u7QbzKTasT_HMvaz17pxJPzPRAbochuXDwnt8VvSgPd3SWqokivgHH6Rvn6RuzfMXhKUPuVKcgn_4owVXogb59brkn4nUK_FADqcv-ViY9CWM2olwSbpuX5VFeDLvPouuSG6cn3NepVIQGsn3x8YkXPaKIilFgdJTQgV2asX4mje5znEGhvd1e2ToxZktyu_JzbBxMpEZqKuTA4Y4hXBJRQw2Xg1ZLd6mrTkkUgBXrrDokRbA95fgXkS33k5qmf6Lbkq7xgiEzud33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=DBjvB2onQ3iAatR_mzucxrs9TNc9MM0Q9gC890ltqwr719godzMCNLJFNU7WiCsOriRherOoKayX5GO_ZSdyzNsX2m2NxMioNhGtA3QZ8dwmi1m4-aVRk-BTgxHzpQ8POqIWFgKt4I9CAXXCQBDzU0OmVRgYcLwhsd2H3R0E0QM8rI5nDAxzkLNrt3vL2BCCG9rdOi4mY_8DWwn3hcoMXSbUJtaHUrN2de4Hu_wPhfiSLkrj0yxCBwr9iuE4bVGim2wfUMZ1T4UFdrDkdpohFbXMHgcGAb4Z5X36BauulTvE7VjqGPPWgqT1DruHuwyvsDcfiNM7p6Jfr8l5r-fZvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=DBjvB2onQ3iAatR_mzucxrs9TNc9MM0Q9gC890ltqwr719godzMCNLJFNU7WiCsOriRherOoKayX5GO_ZSdyzNsX2m2NxMioNhGtA3QZ8dwmi1m4-aVRk-BTgxHzpQ8POqIWFgKt4I9CAXXCQBDzU0OmVRgYcLwhsd2H3R0E0QM8rI5nDAxzkLNrt3vL2BCCG9rdOi4mY_8DWwn3hcoMXSbUJtaHUrN2de4Hu_wPhfiSLkrj0yxCBwr9iuE4bVGim2wfUMZ1T4UFdrDkdpohFbXMHgcGAb4Z5X36BauulTvE7VjqGPPWgqT1DruHuwyvsDcfiNM7p6Jfr8l5r-fZvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامران غضنفری، نماینده مجلس شورای اسلامی، در شبکه اجتماعی ایکس از برنامه شماری از نمایندگان برای «تحصن» مقابل ساختمان این نهاد در اعتراض به ادامه تعطیلی آن خبر داد.
او نوشت که «چنان‌چه مجلس بسته باشد، تا باز شدن مجلس، در همان‌جا تحصن خواهیم کرد.»
شماری از نمایندگان مجلس به تعطیلی این نهاد طی ماه‌های بعد از حملات اسرائیل و آمریکا به ایران در نهم اسفند ۱۴۰۴، اعتراض دارند.
حمید رسایی، یکی دیگر از نمایندگان مجلس شورای اسلامی، یکشنبه ۳۱ خرداد با انتقاد از ادامه تعطیلی مجلس گفته بود در صورت ادامه تعطیلی، همراه برخی نمایندگان مقابل ساختمان مجلس جلسه برگزار خواهد کرد.
حسین صمصامی، دیگر نماینده مجلس شورای اسلامی، نیز در پیامی جداگانه در شبکه ایکس، نسبت به ادامه تعطیلی صحن علنی اعتراض کرده و نوشته است: «بیش از ۱۰۰ روز از تعطیلی صحن مجلس می‌گذرد و نکتۀ تاسف‌بار آن است که در سامانه قانونگذاری، امکان ثبت استیضاح وزیر و صدور بیانیه مسدود شده است.»
انتقادها در این زمینه به خصوص از سوی نمایندگان نزدیک به جبهه پایداری با پررنگ‌شدن نقش محمدباقر قالیباف در مذاکرات با آمریکا، افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/76619" target="_blank">📅 17:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilb_t1XxuCuFKtRLCq4LKrWG2f5NAiMxp9kl7Ek171IArIK5XUcW2ymmEoELxTEERzAe5ZDIWI2iYuhi_pG_FJLG48ZrXyfr01GPF4kFFiGuTj-yhD1kvJCPr6TSNXqtHB59BLbBNqV8kksypFXXc5dL0GUydM2xc7OzXnPHQzwLG8loMoRbixpSf-7AdfdfhHWz8Iznf6Z1it7nG_S6wafWSuw5Z9GAuUYs9xJV3iodqXwKdZnYPKEiRNa7PmxU6GXBEENxAwS2YIwzsijlS6dYVB9ZGqh8NnzISiBuoZXynRSTkzedwkRHYOzbWlN1haYk9jijvnktk4tgaAxVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون فیلمسازان مستقل ایران، ایفما، در بیانیه‌ای نسبت به احتمال اعدام علی صفری، بازیگر تئاتر و دانشجوی دانشگاه فرهنگ و هنر هشدار داد.
این کانون با ابراز نگرانی از طرح اتهام «محاربه» علیه او، از مراکز سینمایی و نهادهای بین‌المللی خواست تا برای نجات این هنرمند و سایر هنرمندان در بند، «فشارها بر رژیم ایران و قوه قضائیه آن را بیشتر کنند».
به نوشته این نهاد، علی صفری، بازیگر جوان و ۲۳ ساله تئاتر و دانشجوی دانشگاه فرهنگ و هنر در جریان اعتراضات سراسری ایران در تاریخ ۱۸ دی ماه ۱۴۰۴در شهر کرج بازداشت شد و «تاکنون اطلاعات روشنی درباره‌ی روند پرونده‌ و وضعیت این بازیگر منتشر نشده است، اما اتهام «محاربه» در تاریخ ۹ بهمن ۱۴۰۴ به طور رسمی به او تفهیم شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/76618" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HEAt88nEASzEOoiJ378UnvTfYKrEhNajasGltRm142ABl7yAFzTQSc70hGiemgdSEoC8B-LBFAWZOsEHOhxasuEJoNAtFNUZHWFgsqfqSIEwSCP_-cuhA2-ed3tEJh_UQo5tvmdpPrfWPFW4FkhuOj89oRwRU5OPXuNlLoKBGxIIirHJuGp7gmai_HABhiSrnjRGym6HqtucqIT9TW-10Tl5OhnUj235y9udsP1Vu7K46OI23s65qQNRLuKRWSf6FrzxzJvsSyN9mUNFqwHY36pTHVnnPYJnhYh4HvThuKijQi7hMVy5ts4O_7qQ-pvud1vppS57xWI4GZ6eg3EBIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11113460cd.mp4?token=RSbOHIwpjDK92vxVdhanYPY7EQzxcYoEanPKQAgj_DalsJyraQrZxWW9JSuv1eQmlQ1QlLLFYOHz_bLJSynN8v9FLnTTEz2PLlgoKPktJMLA9chk09Rd4-X15GW2L3BXZohppkakuX4HOoLXrTyEhYaCXr-lMufZu92FIveYH0Jiui-GXHBLCbJydjiBeh5gQCzY6rEoOsQbdu5V0yGyeHEI4WjFnEKEgI2-bpXd13QbxAgTsVb-yp0RSjtoQW4DQi8UdAfxO-TkAjyQ-bGvx1Pul8ld2DBy5YGZ19YA7seNaqPAjcLnWLx1t6eq8YzczeuyKfDz6y9u2ahZggbPFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11113460cd.mp4?token=RSbOHIwpjDK92vxVdhanYPY7EQzxcYoEanPKQAgj_DalsJyraQrZxWW9JSuv1eQmlQ1QlLLFYOHz_bLJSynN8v9FLnTTEz2PLlgoKPktJMLA9chk09Rd4-X15GW2L3BXZohppkakuX4HOoLXrTyEhYaCXr-lMufZu92FIveYH0Jiui-GXHBLCbJydjiBeh5gQCzY6rEoOsQbdu5V0yGyeHEI4WjFnEKEgI2-bpXd13QbxAgTsVb-yp0RSjtoQW4DQi8UdAfxO-TkAjyQ-bGvx1Pul8ld2DBy5YGZ19YA7seNaqPAjcLnWLx1t6eq8YzczeuyKfDz6y9u2ahZggbPFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه دوم تیرماه بار دیگر تکرار کرد که ایران با بالاترین سطح بازرسی‌های هسته‌ای از تأسیسات خود موافقت کرده و این بازرسی‌ها «تا ابد» است.
دونالد ترامپ در پستی در شبکهٔ اجتماعی خود، تروث سوشال، نوشت که با وجود اعتراض‌ها و «ادعاهای نادرست» ایران، و «هم‌زمان با جار و جنجال رسانه‌های جعلی که هر کاری می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند»، ایران «به‌طور کامل و تمام‌عیار با بالاترین سطح بازرسی‌های هسته‌ای برای مدت طولانی در آینده (تا ابد!!!) موافقت کرده است».
به گفتهٔ او، این امر «صداقت هسته‌ای» را تضمین خواهد کرد. «اگر با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد!»
نخستین بار، جی‌دی ونس معاون رئیس‌جمهور آمریکا بود که روز اول تیرماه خبر داد ایران با بازرسی از تأسیسات هسته‌ایش موافقت کرده و این امر ممکن است در هفته جاری رخ دهد.
با این حال، مقام‌های جمهوری اسلامی بویژه سخنگوی وزارت خارجه ایران هرگونه بازرسی آژانس از تأسیسات هسته‌ای را رد کرده‌اند.
@
VahidHeadline
پست‌های ترامپ، ترجمه ماشین:
با وجود اعتراض‌ها و اظهارات دروغین آن‌ها در خلاف این موضوع، همراه با هیاهوی مداوم اخبار جعلی، که هر کاری می‌کند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهد، ایران به‌طور کامل و تمام‌وکمال با بالاترین سطح بازرسی‌های هسته‌ای برای مدت بسیار طولانی در آینده، یعنی تا ابد، موافقت کرده است!!!
این کار «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این موضوع موافقت نکرده بودند، هیچ مذاکره بیشتری در کار نبود!
بر اساس این موضوع و سایر امتیازهای بزرگی که ایران در حال دادن آن‌هاست، من موافقت کرده‌ام اجازه بدهم تنگه هرمز باز بماند، بدون هیچ محاصره دریاییِ دیگری. با این حال، همه کشتی‌ها در جای خود باقی می‌مانند تا اگر لازم شد، محاصره دوباره برقرار شود؛ چیزی که در حال حاضر بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که وزارت خزانه‌داری آمریکا آزاد می‌کند، به حساب امانی منتقل می‌شود که تحت کنترل ایالات متحده آمریکاست و صرفاً برای خرید غذا و تجهیزات پزشکی از ایالات متحده استفاده خواهد شد، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما.
این‌ها چیزهایی هستند که ایران به‌شدت به آن‌ها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است همین حالا، پیش از آنکه خیلی دیر شود، کمک کنیم.
گفت‌وگوها به‌خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد؛ رکوردی بی‌سابقه در تمام دوران. قیمت نفت به‌شدت در حال سقوط است و جهان جای بسیار امن‌تری شده است!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/76616" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vSriPQat9m6Hu9ekgjU_uES3C2mP5-fIzkOsX5GCklSlOZeeyhFpwBvgDtVCqygY8FDpm9Xj_nLxm0d1WsXsDH_zzSQWRIP5p0ltwFAgfJoIIye0Fh0CN3ceTt9bxs0bEctd_djU312CD8HugbsyJJ_0Q_e3mhHNx1Y8kKGfI2hR7fG3Ngm7MNdLUPDCcy5hE34UFTvUOlnt8n6HOL3MrJLFyJj4XPSttEU3OrovnopLWvg3R3J4fgs6z3V2WBsTU8bGSqKCvezUZqbA3of0uNdFEQb3bpwwAMRbZ2dySBAFNcr8_iZ5Y0aWBknnLmdsuVNO0p1As-CBfFm1dyiV1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر سه‌شنبه دوم تیرماه گزارش داد قیمت  [نان یارانه‌ای، نان یارانه‌دار] در تهران و ورامین افزایش یافته و در برخی موارد به حدود دو برابر نرخ‌های پیشین رسیده است.
بر اساس این گزارش، قیمت‌های جدید از سوی استانداری ابلاغ شده و از امروز روی دستگاه‌های نانینو در نانوایی‌ها اعمال شده است.
بر اساس نرخ‌های تازه، قیمت نان لواش به دو هزار و ۷۰۰ تومان، بربری به ۱۰ هزار تومان و سنگک به ۱۵ هزار و ۵۰۰ تومان رسیده است.
محمدجواد کرمی، رئیس کارگروه آرد و نان اتاق اصناف ایران، نیز افزایش قیمت نان را تایید کرده است.
در ورامین نیز رئیس اتحادیه نانوایان از افزایش ۹۰ تا ۱۰۰ درصدی قیمت نان خبر داد.
بر این اساس، قیمت نان لواش از هزار و ۴۰۰ تومان به دو هزار و ۷۰۰ تومان، تافتون از دو هزار و ۳۰۰ تومان به چهار هزار و ۵۰۰ تومان، بربری از پنج هزار و ۳۰۰ تومان به ۱۰ هزار تومان و سنگک از هفت هزار و ۴۰۰ تومان به ۱۵ هزار و ۵۰۰ تومان افزایش یافته است.
مسئولان صنفی افزایش هزینه‌های تولید، از جمله دستمزد کارگران، خمیرمایه، حمل‌ونقل و اجاره‌بها را دلیل این افزایش قیمت عنوان کرده‌اند.
رئیس اتحادیه نانوایان ورامین نیز گفته است اصلاح قیمت‌ها با هدف ادامه فعالیت نانوایی‌ها و حفظ روند تولید و عرضه نان انجام شده است.
این افزایش قیمت در حالی اعمال شده است که نان از مهم‌ترین کالاهای مصرفی خانوارهای ایرانی محسوب می‌شود و در برخی اقلام، نرخ‌های جدید نسبت به قیمت‌های قبلی نزدیک به دو برابر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76615" target="_blank">📅 17:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GhfRs740a0Je88aCgcfvZ-RRBxegA2bWjrLLkUC3jISGie1AhtSxM1VQZE0k6G0LEiidAtMm2jCxrFyQkJPAa9JjhqgKSubjoSySoERU3YEh5tmEDhkvlmdu5bBZEz9a-vI7PasVHIv_ByWq1C5f9-aXFpT2iW1HNyzmeH61XpjgPyKAs8IrYoKTo1L5GLg9hkhBEHTNPsjo-ZG9v4wjqbb1DCW9bsYB2IFs-ap-RBtRpkeTZ6HMt8AJ76YmTlBQdx-bo6YsP2fbYEhd-wD_lrrx7W-TP_pXgddQWa8oSfeDUD4AwPmPcWnfkGDGWSVunU8qTEx5wfhubEhTEkY5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z3sh0myUK5s82aJAgvV7y4zoiXPc6AtAyN8ynzm9oqT_YuYSKrx3IDBV22npK_mh-Q1WjtDYa4hVm4v-Pi24tEQWUpd4JwuQCNQVsSHYf971KAbv0w6e64--uQlKanVBUb2ZSk3JJO1aVG-yXFciCQVZxshrvDPMLMTFVQAyhzBcKAUUUXhH8yBWjOuOs0uQzH9FRrqHFGZRknPyfqU9dU1lZ515ulgjnVCg8g1Zvt2b0InVloqp7g5kKHnd7hiIfofCDfSEr3OEUNEZKAodYJT40-gDjtUY-MSNt-zKDEAOcvsnQfB_ARb8Hi6e1_ukgX8T2HOziF5mvG8ZOD0EqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BYbrfdihIbV_qpLxtJPwjvlmO3bTL-1yVjKGspsGBre52P4DFIUrusarbMk1xtslNscaSzaATjhEnS0B0wtn7InRLC8K0UdwBcd0LMEhKWqoyBQSlPsXm0IOt6m7wr6uPca-k8wBH4IflgR98rVLI4Y_hnPsVxQddTsk5dQY5vE3VCyMhhVg2VfUBewp_D68KK1C0Y_5pzwWWFiaWC3oLLtH7eEtXQxxU3XUhIJNvIXPx7TVJy9QIyycZKH7gEKg24-XFHJVFSTIJiULS4JbFSmztGug45PYJWPyCLz89eLEH5EZ95ptOckqJr0lWhCLKblXZWCbaijckvlATIjI2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=H3GsvW4oxqjdFnwofTaIbozXmyzmX1FIKgfSFxq1Bm2DwwTLHRlXF-P0pedTqkS563V-id0-qphAkgpo1ZO0HD2szKpBqpqHu2szHpbZHIvJMnP_mFb28z4M_DKWECBHuY4x4zr5UKC_HALZ5MkoTa7Fd6Y3tE4KiJO6BGuhwYnnw_XdCG6l04kFpUP556i3aU8DnA0n1kI5WEROOy06jnhofJFilyg7JTnJrbpyEHqTkbvgOz9bLE1uBMi_VUizRiZaYdL6LzKRgwiD6qrN_55aEUzUuhJfbZVirAF5BAMG1VDin8P9_PXnQMSnfo1ukUOzuomOXA5TWXRDE3Bglg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=H3GsvW4oxqjdFnwofTaIbozXmyzmX1FIKgfSFxq1Bm2DwwTLHRlXF-P0pedTqkS563V-id0-qphAkgpo1ZO0HD2szKpBqpqHu2szHpbZHIvJMnP_mFb28z4M_DKWECBHuY4x4zr5UKC_HALZ5MkoTa7Fd6Y3tE4KiJO6BGuhwYnnw_XdCG6l04kFpUP556i3aU8DnA0n1kI5WEROOy06jnhofJFilyg7JTnJrbpyEHqTkbvgOz9bLE1uBMi_VUizRiZaYdL6LzKRgwiD6qrN_55aEUzUuhJfbZVirAF5BAMG1VDin8P9_PXnQMSnfo1ukUOzuomOXA5TWXRDE3Bglg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«امیرمحمد هموله» ۲۴ ساله، ساکن شهرک صدف شهریار، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ بر اثر اصابت گلوله به ناحیه سر به شدت مجروح شد.
او پس از تیراندازی به بیمارستان نور شهریار منتقل شد و حدود ۵۰ روز در کما تحت درمان بود، اما سرانجام در روز هشتم اسفندماه ۱۴۰۴ بر اثر شدت جراحات جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76611" target="_blank">📅 17:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PUbW6Oz0HR6i3TYV2cspSjyDveFBI5czD45P88VWxwV8fN18G90xIH7dBQLWmHUS50HNQyjNE_GpPHWQwEREaXaovXXOBM0HMNFcZ8wShSlL0lcKkeJOhqIJto25P7M2Ml5SxOHJWtY4SOoGnMkpP1oHMz1kyLHrc6B6eStT78YvLFv1-5hbRwogFrbEBzWgJ9fqvqbz4eb_vMig6SOStDEwwEE4e4tfYx9T0jc9qHTgD5tBiU6oGyUnlfBWjGkm9i0NNyW8FHZWvZgPweowhdeV42m7Y4ISk0NQ-PHneJhIfvU3mFzEozqk2F2bWZ68Ys0R9DhV9Y5p6k7CjGeB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hDppjspIG9OgxgKjffMUNlFGD7tQwopl877kjtOBZVs8ByU6S6JUr-qlH5jY-OAMcgJ1CP8fZ0JJYLpMiiyyLG8vKVq4Lm-Cf60cbW-oJyBnnI7yPiN-C4fKbjcOeyqZyn4iBkGTnoIEla5P0ro6VYwpnF2xHWVFnDjEQjPi7Bv3hvagRYX1cLQFCjicKMcn8VOPgE_5iMUjZkPqhpOkeOg3LGvFEVTYWXCh1KuHoVGqIZohlEf4rAt5WpTiOcypcXBHBHrKXoHnZM01_cCo3RTJ0l5e6k7mZWiS4fVGtCDOEQyLSe9lNReoxmoYjTr58Ng-S4pQDqVdgF8LRPFDbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ePoh77nn3lT5pi2L4pBoawdFQs_mSZ_h9TiKFVT8Drcsfk6_6nOf7UZB8rV-Xz3pFSJO0gmuPMSaqm09GkkaW1iUJl_kUmtwGCRt6q3BMuDXNFylvOm0LakPqvM-oEIHVK5cqTaEMFFP5gW9kUGNiVyUAsqNBLmO1ZUhyZAh8255fL4300Wo0VnD6P1GmibczKwmEsg0QMUBs-9Ba5KsurJSJiHumqveHg_swsmLva4h7j-qatyS0jwCjFQQxr2WZZGIRurbQG9lntOkydeV5IDcFNzN2EAyyl4Nn6tAj-hvIjNYHOUTtNvrHKSeSj8vy1cK77YYiVgV1b31v2nDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R9Pi9PY7Y7JwwJsd88l6gwwrQgUiXStvgPFw_VB7RARyz6WqWu0OUumM-KxHOcrjJbi7kS6kH3izgLreb7hR4dm1-H4a78RdXckBPTZ1qomX-f8diwmj5DSnzpZAitzQitcGalpxY8NZCYp-azpPwDUJqNS893JH2ZmMeAq8LV6C0rf6NMohkTr7Lkp-YNzX02K2ah0z19-MAMlrL8wu2373bExHc3DIF9rgf7x5Fl5L5U9mM58hEE9Ktr0R_Pf5TYn97WR0cBY2a4F1nbpup84BOE444nNoSaBRf7dRPI6UHGX3pQEpDawRpyZY1V0fjoGRg3h8ka1BDFvQhoAL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bqY0FiBqbunTQsw6MiyWtQYerT1j8dMNplH3P1ipVUteu3kg0Q3qlPKqISotYHpzs2pl8TvKe32pgPcfoEQ1Rx9Ppps-Oild28TGIf6f6pK6y9rkh794VHNhV9fbpWHThSgagBfgRlsd-tXp9LhayfQDCOcRyLJ1ZAxMpMc_Qc9HXtZYCvNypjWFuIYVNx8KXEEPX2ORT5ZH74mw7CALgloCuEwR3HGJENdMEwnUYLjH3sSDFNE52ASIvQ4-uAjN0Dus-tlxJU3jFYuayoMV3uzyr67zPAEApe6I54nQZaJnW4xffbpS98FQZ8XnqKKXisD92HHWyap_p8BDwCEd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uDmnn6IKIJWGRDC8l-sNXG4XK6SM2gLnxE8aDBtrrBnFNkUwRJLmobcWZGPkpMkHWRHzyMGocfxCdEADUSS7mulQ2RDFjbQrV6Cj46XMa9yzM-w-dlc8nGp4y06pfpes8NLLIM3L2qhTo-yUzn_I7q9RGaf0pMlNW7JJxZ4EJUoWwPHhY3ZReIyrHknWYFHMeGinr_BwmuI34fF66K57cKluCOM2wUicOkSVUUAEzDlNvmOxgXWlatJ6r3Ukm1bAFNq8VC363ry2koSPbYs6ccYDwMl2TXp0P-L6M2CCtBk04CcQu4-cM7O2Prt8Qw4vUU1PupLKXHaZJV4eDxsBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lli2OLXYiCLX-cMRC9mThO6p8_0CC8ed_GqriEUvfm81dDVG8_WiI6GQoiMzp0L6orqfgsLNkvXaBKLPFXd3cm9STjn5A7QHvZvvJghUIzDybUG_lDqxTh59QbxZ2XUi2qvRa0p8rnCWk-fvAE9nX1cOOh_oJM4s7Ldi7T62CdYfx7c9-Cn3jsqfror6qtv1HB2dgu2ZWbyPEjEZ6jZyEgYaBf_ZBCXwKhvUDKid7Okp6yugtXrD7sZ6KX4eJWgOR5BgjSs4ACCqk3D-diCjJRMgIz90aBEDLNfGsJUwlBdAz_4MuMA-e-ooxltS7QPRHzBAokf9WFNl_e9qE41NiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a4Bam4mYtZ5vnh92r4nkUFIK-Cqwtst3sCmeIdlmpwh55ZsMlEiztEVWm0KfZBQtVNHRuheWXAtUYHh-iO1THsRoTsdz5OelteGCsuF-8JwG4y5p3XHA_wkffNei8xKkqywc2uv5c89o5g6MGTpbZoniH5_6Y0kaBZZQHms5co8sSw_T7zDWHVCK6Ha39fQT--oC2382RRmeyPzHsF1zJTtkFkWiu54yzY6WRSVFb2wwji0hrTogaG-xLjXF9OSbZXoxBbGN6BcMsmaintuRLpjKNHPlynRKzuTUQXD6MIBl3T9QH7eGmIJPYdTLz-3j3AqxHpOaVZADbrkdgxWqHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ پشت سر هم پست کرد + ترجمه ماشینی
دونالد ترامپ، رئیس جمهوری آمریکا، دوشنبه عصر نتایج چندین نظرسنجی مختلف درباره توافق با جمهوری اسلامی را منتشر کرد.
از جمله یک نظرسنجی مشترک «سی‌بی‌اس نیوز» و «شرکت یوگاو» می‌گوید که به عقیده ۸۰درصد جمهوری‌خواهان، این تفاهم‌نامه «بهتر» برای آمریکا، و یا «خوب» برای هر دو کشور، است.
در یک نظرسنجی دیگر، ۶۷ درصد می‌گویند از تفاهم‌نامه اخیر صلح میان دو دولت حمایت می‌کنند.
در نظرسنجی دیگری نیز ۴۷درصد گفته‌اند که این تفاهم‌نامه اثر مثبتی روی نرخ تورم و توانایی مالی خرید مردم آمریکا خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGkCpTloTgoeXmtYuKERTl6L1w01phyfRPQnZJg6nQX0I2mNU48RcF5rhMj-AwUrzN5gcoy7aWHqXMqV0wkgDYbRGsusTCTSjlZ-CR6tTvXzqWw_ELeEvkmc9L7KdEzbnyXUyNi7uWSz3ceaBvNDnaiBuKBjmsZgLH68AGKQsb6pfsi6qrFZsXU28g1Rqz2u3Ese939DhCsNDxy8kB9FcdigTArZClbRYHZNvqYTJtQJaHnrYcer4fA-seYtpuMcCCpnzFE0QzFSx9C0AUGoHgYeIkqfn02nU1pDMlBFQqq9TzYZaXW_UI85-f_dq9nrJLK7w9YVoZ65uM2dYF16VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: اوضاع ما  ‏در مورد تنگه هرمز خیلی خوب است.
‏دیروز نفت بیشتری از هر زمان دیگری از تنگه عبور کرد؛ بیش از   ‏هر مقداری که تاکنون از تنگه عبور کرده است.
‏احتمالاً این را می‌بینید.  ‏ما با یک فوران نفت روبه‌رو هستیم.
‏تنگه کاملاً باز است.   ‏این را می‌دانید.
‏خواهیم دید همه این‌ها چطور پیش می‌رود.
‏اما ما دو چیز داریم.
‏ما یک تنگه باز داریم و کشوری داریم که   ‏هرگز سلاح هسته‌ای نخواهد داشت.
‏هیچ‌وقت، هرگز، سلاح هسته‌ای نخواهد داشت.
ویدیوی بالا:
به تشخیص ماشین، حدود ۱۱ دقیقه از نشست خبری ارتباط مستقیم با ایران داشت.
متن فارسی اون دقایق
ترامپ در پاسخ به سوالی در مورد تنش‌های احتمالی در تنگه هرمز گفت
تا زمانی که ایران به ما احترام بگذارد، نمی‌خواهم بگویم از ما بترسند، تا زمانی که احترام بگذارند اوضاع خوب خواهد بود. 8:15
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه عصر گفت اگر جمهوری اسلامی «به توافق خود عمل نکند یا اگر رفتار مناسبی نداشته باشد، من کاری را که باید انجام دهم انجام خواهم داد.»
5:00
ترامپ: نیویورک تایمز جعلی گفت، اوه، وضعیت تقریباً همان چیزی است که چهار ماه پیش بود. نه، چهار ماه پیش، آنها یک نیروی دریایی داشتند، دقیقاً ۱۵۹ کشتی. آن از بین رفته است. کل نیروی دریایی از بین رفته است. آنها ۲۵۰ هواپیما داشتند، همه از بین رفته‌اند. ضدهوایی آن‌ها از بین رفته است. رادار آنها از بین رفته است... همه چیز از بین رفته است. رهبران آنها از بین رفته‌اند. کل کشورشان از بین رفته است...»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=dsOPA-4aN_-c7CDEhC-YJz23UHIkLW6G__3k9BR9Rn14aCvLW2otvz1mtl8vPkMwIRioOZjUUFQy_S8-O_JDWnSU5qedNxz9SJprU8W25LjYJJfK31kJ873hANpuMIBAchgLTVRVWXgZ_RVLXz--dDdQSty_JwRvVNo_a1tXk6LnsUIhNBCEW6NON6AOFqutsSM0a2bG1-8w-jIlyZDxkv8b9NdYeyy0hB5Y_gkKI2oLgvyyuj1p1dxv7i3XpDZfKzjCkFtVzDvPbSjsBFMeAVgxRnoQQtB3zk-Ton41U4NsNfGYNIuYeILNOyR--Ncq5FaksF7ycMPRKCR1qthoqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=dsOPA-4aN_-c7CDEhC-YJz23UHIkLW6G__3k9BR9Rn14aCvLW2otvz1mtl8vPkMwIRioOZjUUFQy_S8-O_JDWnSU5qedNxz9SJprU8W25LjYJJfK31kJ873hANpuMIBAchgLTVRVWXgZ_RVLXz--dDdQSty_JwRvVNo_a1tXk6LnsUIhNBCEW6NON6AOFqutsSM0a2bG1-8w-jIlyZDxkv8b9NdYeyy0hB5Y_gkKI2oLgvyyuj1p1dxv7i3XpDZfKzjCkFtVzDvPbSjsBFMeAVgxRnoQQtB3zk-Ton41U4NsNfGYNIuYeILNOyR--Ncq5FaksF7ycMPRKCR1qthoqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس، ونس هنگام ترک سوئیس، ترجمه ماشین:
🔸
سازوکاری ایجاد کردیم تا مطمئن شویم نه‌تنها تنگه هرمز باز است، بلکه باز خواهد ماند.
🔸
قیمت بنزین همچنان کاهش خواهد یافت.
🔸
سازوکار درستی ایجاد کردیم تا آتش‌بس منطقه‌ای تضمین شود و درگیری‌های اجتناب‌ناپذیری که پیش می‌آید مدیریت شود.
🔸
ایرانی‌ها اجازه داده‌اند بازرسان تسلیحاتی، بازرسان هسته‌ای، پس از مدت‌ها وارد کشورشان شوند.روشن است که ما این رژیم بازرسی را تقویت خواهیم کرد تا مطمئن شویم آنها هرگز به سلاح هسته‌ای دست پیدا نمی‌کنند.
🔸
بخش زیادی از تیممان را آنجا گذاشتیم. ایرانی‌ها هم بخش زیادی از تیمشان را در آن اقامتگاه گذاشتند تا کار را ادامه دهند.
🔸
این دارد بنیانی می‌گذارد برای چیزی که می‌تواند خاورمیانه‌ای واقعاً دگرگون‌شده باشد.
...
خبرنگار: آقا، خیلی سریع؛ دیروز لحظه‌ای بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما دست ندادید و بعد او از اتاق خارج شد. آیا احساس کردید به شما بی‌اعتنایی شده؟ آیا فکر کردید این کار از طرف آنها عمدی بود؟ شما آن اتفاق را چطور تفسیر کردید؟
باور کنید، در چند ماه گذشته زمان زیادی را با ایرانی‌ها سروکار داشته‌ام. گاهی آنها را به‌عنوان مذاکره‌کننده‌هایی بسیار گیج‌کننده می‌بینم.
اما ببینید، ما یک نشست خبری کوچک داشتیم.
آنها آشکارا در ایران از همان حمایت‌های
متمم اول قانون اساسی
که ما در ایالات متحده آمریکا داریم برخوردار نیستند.
ما با شما صحبت کردیم و بعد چند جلسه واقعاً خوب داشتیم. چیزی که برایم کمی خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی توفان در شبکه‌های اجتماعی شکل گرفت که همه می‌گفتند ایرانی‌ها می‌خواهند بروند. و بعد ما حدود ۹ ساعت دیگر با آنها صحبت کردیم.
بنابراین فقط به رسانه‌ها توصیه می‌کنم کمی به آنچه از شبکه‌های اجتماعی ایرانی می‌بینید بی‌اعتماد باشند.
آنها می‌توانند مذاکره‌کننده‌های گیج‌کننده‌ای باشند، اما احساس می‌کنیم در حال پیشرفت هستیم. ممنون از شما.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dc1UeBmFJ7o0LmUJnE1eSn0m7aU-XhT7kfmlynowxyCt5vZPKdKirLSXHn6q-rfACcdi2uJRMYIEIhwyjRo1oHnLTFuOSl-Q7MaPEGoulEkZ-qUZOpcqMH6wSWvMbHr7Nb0-g097blDGffv-dXKaD-Q4OO0bFmNcNCp9zkEIpakNT-JcwPbVcG9ijmP0GPNdlVdZemrJwbdjrbNUURMcmkmAA-DuO775jfl9a6NlLnuMBjQNt49Z6RNVual_drGmhe23x_MISyC2dc69eEPZqWovsBxV1jNU4u9mN19C64-pmX_WsZ_2MpCRnibmw3XaASv5FNQu9HhmKKB-TM93lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zk7TYqKehE_LuhcEgj7sXaj-0NeyH9sH-QZ3J5wBAvk_R04G_mBegaEXeOqulUQkM1GcyYClycRCPwJhTQdyqwWpP_V2WZ4w1dVUpuHj7eOe-7N-wTobu3-QOtqzHNlkCzUtgo0OuaEik2GXl3-v2M2TzmsmoxHf6ptSPrOBCjiccXBuUgL65cq-zgJ3NEQ8ywOF0DG3XOSwOscWLZdIHkwKC7DTwR7bLbR6u36CApIXMoL6cvmfNKrPI95wM3Ye7pkvN0Xob44MozuT3pZUZKfPIPEIJ075AYuSyxmdaT9PSqe8-2gcc6EJ_I3b6pp5F0bsZvhu8ljc8varQ1sJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، رسانه‌ها خبر دادند که محمدباقر قالیباف، رئیس مجلس و رئیس هیئت مذاکره ایران، که تازه از سوئیس به تهران بازگشته بود بلافاصله برای دیداری دیگر به مسقط، پایتخت عمان، رفته است.
به نوشته روزنامه هم‌میهن، قالیباف در سفر به عمان به همراه عباس عراقچی،‌ وزیر خارجه، قرار است با هیثم بن طارق، سلطان عمان دیدار کرده و در زمینه ارتقای همکاری‌های دوجانبه و تشریک مساعی «برای تثبیت ترتیبات ایرانی»‌ برای اداره تنگه هرمز گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76598" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/suh5WP1ynHUPGRvrhiFVL2VBjYU5_GR3RW7YP8WwS3m3pIjZDmHzacL2-kYLYYk7yc8PCLy_76DVVSb6AgRG8TZqbuiVnGiMS2IUg6HMggH5GSlp7l1nhYMqtZmaMLEt81AW1wGhrEYTsraPdBpfJoI7HfO00e9A_wg7iQavt1mKiqUe5NN0dtwflWT-Ki3C5yOekA_zS94SLKTUjeSh7-JagobxMZSoW_esEvGCfYjJ_SFOXmWfx8-X5VvnGwVVdNRJ4jxQhlsDqHqpNQ9nN291oxY4bAY5KF8D8boHAt3z4CgGbOvSLvruPY5e62BeO4voMnnw9K6VL_yuxRc5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نوشت اظهارات جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره بازگشت بازرسان آژانس به ایران کذب است و در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76597" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=CxuA2FcACm94F55QQHCL-4fxVCsf3_wvQLT2odp9wvOfdupGj4R3jJFpdSQh94ZlOlBbXEJBoUiGVvOEX_rST8v2J80d3jzEN0m-aB1ry8zUNZ8rZOxRkRXgniTIG2WQRM2KsnZFizVoKmda7V4SwIMKKYWFvc0P6a-fE4LIBtxJQoQ61u-pSzv40ncYDl1fFn8Mw515_uLxlGEseM2_br67XNfcA8audLaE5Np9qfBgZ7s-d0UhkqUEMDuODHZji0gV_e6owcGVlQJ9Eerp0czPhNwMVxop_xSsrJdSGOXZ-8G-h2kppRCpw1caziyIkYhEXFIJDbSeCV0R-aiOVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=CxuA2FcACm94F55QQHCL-4fxVCsf3_wvQLT2odp9wvOfdupGj4R3jJFpdSQh94ZlOlBbXEJBoUiGVvOEX_rST8v2J80d3jzEN0m-aB1ry8zUNZ8rZOxRkRXgniTIG2WQRM2KsnZFizVoKmda7V4SwIMKKYWFvc0P6a-fE4LIBtxJQoQ61u-pSzv40ncYDl1fFn8Mw515_uLxlGEseM2_br67XNfcA8audLaE5Np9qfBgZ7s-d0UhkqUEMDuODHZji0gV_e6owcGVlQJ9Eerp0czPhNwMVxop_xSsrJdSGOXZ-8G-h2kppRCpw1caziyIkYhEXFIJDbSeCV0R-aiOVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تا وقتی که لازم باشد در جنوب لبنان خواهیم ماند
بنیامین نتانیاهو اعلام کرد که موضع و دستورش به وزیر دفاع اسرائیل تغییر نکرده است.
نخست‌وزیر اسرائیل نوشت: «نیروهای ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم علیه خود یا ساکنان شمال را دارند.»
او تاکید کرد که ارتش اسرائیل «هیچ محدودیتی در این زمینه ندارد.»
نتانیاهو بار دیگر تکرار کرد که ارتش اسرائیل «تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهد ماند.»
در مذاکرات ایران و آمریکا در سوئیس، هر دو کشور تاکید کردند که حفظ آتش‌بس در لبنان از موضوعات محوری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76596" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aiDNScGTYWxUsH8JrP0S99rAgZkNCCLJUwTvsxn2iuVfn5IEVDg88bcmNQCwtn6rqB3nzNJ2njDafDQ21e7etEzdd8xK_NDEFAo57Kt5_2j_u661jcRMVvhNX33PwodAPE3o5z8J-yH8JI4kLvJ2fcO9CUi2TV11eTBQRun06CC7yFqruzi5cgSLQGAfJ0lbKfNvJr0bbTVTdh-wuEIGhZCTH2c8mfbC2qTDzxK1OQIU9tub-ZBwJVSY2YXVg13-cn_8A97do-U12jQKHG9WP1k9AgwKl5TwMQbfLnjHtSG71cJs7mUUZoVnkOVT9Rzxzamt7nsqG2jzfxs5ePuOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا با صدور مجوز عمومی، تولید، فروش، حمل و تخلیه نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران را تا ۳۰ مرداد مجاز اعلام کرد.
بر اساس این مجوز، تمامی معاملات و خدماتی که برای تولید، فروش و انتقال این محصولات ضروری هستند، از جمله بیمه، مدیریت کشتی، تامین خدمه، سوخت‌رسانی، ثبت و پرچم‌گذاری کشتی‌ها و عملیات نجات دریایی، مجاز خواهند بود. این مجوز همچنین شامل کشتی‌هایی می‌شود که پیشتر تحت تحریم‌های مرتبط با جمهوری اسلامی قرار گرفته بودند.
در متن مجوز آمده است که واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران به آمریکا نیز، در صورتی که بخشی از فرایند فروش، تحویل یا تخلیه مجاز باشد، امکان‌پذیر خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76595" target="_blank">📅 16:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dv3xkDsxfUTvWZ4f2Cmq5esCokw6H0dZwcdHtRF8kri-PX15CF8YFg3IZDEOQJWYTQVU0f1f-4pcKDU3I4WBEsB0szTBCuOMSxuz7-V1wv1ZgPPlkr_VNUQL4e9V5jBfEL6F1yBSdn4c2a6xv6n1uvjTVjodpEgJhXjBRQOXn8sf6hMzTJQUAitbqrqvWT--MigcSxp7rj--lQ0U4aZKVhEMMLbBTham-zyBZ3LFFzqLRqNTHUF91yX6Om2u-Bo0dTJCwz6qCbs_5_87yEV6QSOcZZTJ2Jhw2UNKDplQfyA9hSbLBu0Qybd3DPfpe8xyw1hmoC6QA29k-1teLB8o1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش هرانا  در خردادماه ۱۲۷ حکم اعدام اجرا شده، ۱۹ نفر به اعدام محکوم شده‌اند و حکم اعدام ۱۲ نفر نیز تایید شده است.
هرانا همچنین از ثبت ۸۰۹ مورد بازداشت در حوزه آزادی بیان و صدور مجموعا ۴۹۳۳ ماه حبس، ۷۶۶ ضربه شلاق و ۵۱ میلیون تومان جزای نقدی برای ۸۰ شهروند خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76594" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jvj-Vb-1F096c5QQipKrad1gbFiOd5ePsW6sjVb37hrfYpjeR-A3Fvtsmg1nvJZtpXEvj9YtceheInyREefYw_0wkc3or1QaSOFCxmcd8MQICCpMZ2NALS1SEbvZ3ij6_AumpQ5nba7deSqJ8cAVdmho63suFz9xXail6-XOmXKEGXZHv2mDnbpZmerl5NZ6aRFz3DjDF5zVqgJbL13hRn7yBbYg1Z6MG9U50hv1U8FMLlzXWYygZms5U1S6PBEqlhLZwpvXPgmMzGEtaxhsNWp-P-odgD8BT41iE__OrYk3Hd5tiebaOHUH3s70nrAkyr8LfoFGyNK05I5LTXzoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eYEWiy_dHrIhwrymkCrXOObApHFKILnSntiGtpbBt-FEPsTtu_iP5YU-TchpXz67jLJoOyQ5QOWC__0Wa7_WmsQxed8kmjf2qA_CEHKG06EPpEBBjyAUzMYyTLsY67d83H8w_wKlfrMrLkMzUUFPY_HLbULzaQ8pivCstlt5VQJNr8Hc1s5OwS5bEOg2Q8sVXSdZdZCXRwubthePPqVSftQ9VSQAsgIkaVS1Mwfx0gNDQfSmLms2po0jKR_IQvkxDNoKK-ENh4_lFFutSb_QGOVZQQ2nzSa4HkoP2Frqok3X-XGRoPznnzUZ6Tkys5o9kQyAlHQBu8uZVanazlLwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u-3aKKAAKlx-_WpTySyO5ZQ5ERKvVkDyTHqi2kqbZ-EfeFOD4vI8PkCUal27Q-K6GPbaIUbFEfUQJCIcqMQ-hzMaMA0SqmHJyCDzoSsgg0-OU3g8nKxeuuQ3UrQ0RkUHXHPNx7u-TWfNvaf90qpEBoO-vhUBW4jvkHd4YEDXV3qbtKpL7y6ieIhaFuo0cromm5XJTDphxx_10naWS-vxneXJnpAdhKrdaE2lacRo7_toipmnX0IkfF_qUpqJisEzCFWdKXhFTDhqTgsyPduc8eyzws_hHed-GIrM72pVWyd5DfF3-41rbrKfpAAE3Ao6S5OdOCXK811jZrxl-QeobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dw0P7JNV9NakYAkicmkMIvta5BY6s7gfCYzF8qzjYkgi32cku5_j8AoZOEGiUZay3i7-aeYi5tYEUFuM2Ww7P40ilw8btaWOlHaMRmm1EI9ZPry5LztS7dErRyqRTA9zDD7k2Q6pM26lRK6ZYkQ5vtAmgd4SVy1f4pZMxOPbkTVrqSUvXRY6HJKxJbIbrKrgwELr_e9mDplWdcSdYWXVQtZlsiHxbjyZ5a-rse2Mgc_lTOArgZuo9_-IIfTzoZe_8_DIyRKvGa-HWTM18ilNSKMhNQIcdff-lFVfaqw6xooCRrKuGdfHILktYxwJRCUdLbxHn6MQrYErTSg3FthGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iIip0p0KOgTcX9PhwF1Fkw3n1VjZckzqEqkJZnnLmt8vAAVH_sjbFC-cg8udmUhe5l2wIaGaNbxRD1xX7giZJmuNveZBQDt8vZhRLj_J2chAJhm4BjCq84MFG7BWZTCnKHKvSAAVR94GC7zC4pOBuBDdx7dl5fikKklK9bKOTpcoh_6e9leITjcctEYa0mVQtXxz_uxkSOpaDd5NO91jdjXXIi8vq8BkBcrUxOoRlcypdcl5eos53sjpx6ZpRlNcZz8C3AY9JOBJkB49odU28D31cSeSgHkbmWn-nlOp-_fBCXUlKdgkYfk1Zxl_sP2VDS3p96nTvxi_rPMK9yYh4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=hwUOtQdypoumhe8exUzqUPuEP21T6oNvCWb-TsJIH5EtnzqNoNFbx34_CAuMn2E6WTZjbYaTxrovDEKLdetGKHKLHOT7dVtVVMK9GsX7GG7MHDH6wiwAXasFlZrCUzWk6te99zJ6bCzjHqejpPrsyqZ5Ks2DWF0j8yz_IF26CslMLg_Q1w3vggjD7KKYGp62VAV9-zWupuZypc8Fv6ypi8H5Prk1LBqUPKtaJJpcnsBHEPxRdKG2ot8_UyBQON18a6DcUnMJJ7xhG7cJQifXN1JvBJLBNExi2ydtTHaVJTQP5e2fjoXQFCh2czy9g9Kyko6xHyqYwgr4Nhyd8AuQRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=hwUOtQdypoumhe8exUzqUPuEP21T6oNvCWb-TsJIH5EtnzqNoNFbx34_CAuMn2E6WTZjbYaTxrovDEKLdetGKHKLHOT7dVtVVMK9GsX7GG7MHDH6wiwAXasFlZrCUzWk6te99zJ6bCzjHqejpPrsyqZ5Ks2DWF0j8yz_IF26CslMLg_Q1w3vggjD7KKYGp62VAV9-zWupuZypc8Fv6ypi8H5Prk1LBqUPKtaJJpcnsBHEPxRdKG2ot8_UyBQON18a6DcUnMJJ7xhG7cJQifXN1JvBJLBNExi2ydtTHaVJTQP5e2fjoXQFCh2czy9g9Kyko6xHyqYwgr4Nhyd8AuQRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی گزارش داد «تحریم صادرات نفت و پتروشیمی تعلیق و محاصره دریایی برداشته شد.»
علاوه بر این، عباس عراقچی اعلام کرد برخی از دارایی‌های مسدود شده آزاد و طرح بزرگ بازسازی و پیشرفت اقتصادی ایران اجرایی شد.»
آقای عراقچی این موارد را در پستی در حساب کاربری خود در شبکه اجتماعی ایکس اعلام کرده است.
@
VahidHeadline
معاون رئیس‌جمهوری آمریکا اعلام کرد که در گفت‌وگوها با حکومت ایران پیشرفت حاصل شده و جمهوری اسلامی با ورود بازرسان هسته‌ای به این کشور موافقت کرده است.
جِی‌دی ونس، روز دوشنبه در سوئیس گفت که گفت‌وگوها درباره بازرسی‌ها ممکن است از همین هفته آغاز شود. ونس درباره زمان آغاز کار بازرسان هسته‌ای در ایران تأکید کرد: «احتمالاً همین هفته، شاید از امروز.»
معاون رئیس‌جمهوری آمریکا افزود: «ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم. گفت‌وگوهای فنی در هفته‌ها و روزهای آینده ادامه خواهد یافت».
@
VahidHeadline
معاون رییس‌جمهوری آمریکا، گفت یکی از اهداف واشینگتن در مذاکرات، ایجاد سازوکاری برای نحوه استفاده از دارایی‌های مسدودشده ایران در صورت آزادسازی آنها بوده است.
او گفت هدف این سازوکار آن است که اطمینان حاصل شود منابع مالی آزادشده به مردم ایران کمک می‌کند و صرف حمایت از فعالیت‌های «تروریستی» نمی‌شود.
ونس افزود جرد کوشنر با همکاری مقام‌های قطری طرحی را ارائه کرده است که بر اساس آن، در صورت آزادسازی دارایی‌های مسدودشده ایران، ایالات متحده و قطر بر نحوه مصرف این منابع نظارت خواهند داشت و باید آن را تایید کنند.
به گفته معاون رییس‌جمهوری آمریکا، این منابع مالی برای خرید محصولات کشاورزی آمریکایی از جمله سویا، ذرت و گندم اختصاص خواهد یافت تا در اختیار مردم ایران قرار گیرد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در پاسخ به سوالی درباره تهدید تیم مذاکره‌کننده جمهوری اسلامی به ترک میز مذاکره، گفت: «آن‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم در شبکه‌های اجتماعی چنین تهدیدهایی مطرح شد. اما ما دیروز تا مدت‌ها بعد از ساعت یک بامداد در حال مذاکره بودیم، بنابراین آن‌ها جلسه را ترک نکردند.»
@
VahidOOnLine
گزارش‌ها از سوئیس حاکی از ادامۀ مذاکرات فنی ایران و ایالات متحده، به ریاست کاظم غریب آبادی، معاون وزیر خارجه ایران، است.
رسانه‌های جمهوری اسلامی نوشته‌اند که قرار است دوطرف روز دوشنبه اول تیرماه در مورد سازوکارهای اجرای یادداشت تفاهم اسلام‌آباد و تشکیل گروه‌های فنی مربوطه با یکدیگر گفت‌و‌گو کنند.
با این حال تیم اصلی مذاکره‌کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سوئیس را به مقصد تهران ترک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76588" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HfZSGPQMFWyf8mNmHm8NRR7cJMXAtBaB_IwzJmrvaMY3cIBOu4TrcGS2f-Kr24y20g8me08RaadZROikM1h52UFVHMrk7ymMrKreac5iBOSwBUkS8OepBUbVqvi-_TP6avaGsOoI6WCce5parXdjSYObfvW7kCze9uXe4zjIwLSSCqJkjdalHkQ9W0A3QJCKjKxX-pt43_hc5FnfK6UnTJgRLp9AqlLtuxlnZCY3fqz6I02O-fubyG_Tchh9hos0ftEdAbsPAn5heYmFU8PXgPrPKzWgNHJ4-WDd2R_yZyOZ-eFP9wffKKRBC9Hm3tLAFeAtU0Pw2FP28rgqa7PXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانجی‌ها اعلام کردند ایران و ایالات متحده روز دوشنبه اول تیرماه توافق کردند خطوط ارتباطی مستقیمی برای باز نگه داشتن تنگه راهبردی هرمز و پایان دادن به درگیری‌ها در لبنان ایجاد کنند.
بنا بر گزارش‌ها دو طرف از طریق تشکیل یک کمیته عالی مذاکرات، بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیدند  همچنین قرار شد گفت‌وگوهای فنی از همین هفته در بورگن‌اشتوک درباره همه موضوعات ادامه یابد.
در بیانیه مشترک دو کشور میانجی یعنی پاکستان و قطر آمده است که: «طرف‌ها با تشکیل یک کمیته عالی موافقت کردند که مسئول نظارت سیاسی بر روند میانجی‌گری خواهد بود. مذاکره‌کنندگان ارشد به‌طور منظم به این کمیته گزارش خواهند داد و گروه‌های کاری مسئول موضوعات هسته‌ای، تحریم‌ها و نیز گروه نظارت و حل‌وفصل اختلافات را هدایت خواهند کرد تا اجرای مؤثر تفاهم‌نامه و دیگر مسائل تضمین شود. کمیته عالی بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیده است؛ نقشه‌ای که زمینه را برای آغاز فوری گفت‌وگوهای فنی بیشتر فراهم می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76587" target="_blank">📅 05:38 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
