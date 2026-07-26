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
<img src="https://cdn4.telesco.pe/file/ngeaSjEY-Bk6lkVQrM2DNVsS2TFr68xIjm-N_h19ntFQSn_JI8um0gSyj-Jqk81FnpG0uZ5EPEkuX63CpgE5nVjVWUBUMHLvDCNFhzmWtzX8RVVMCAUaEV4hJkbR0PODEu9axZ-Cu4XFiF2UQFVIvnsFkoOkduRpame_MM4yJZ_CuWWAMkMNsz09MhavSOab4434WFPtUzSvJ5OxleDfR55qJa8ril9AlIoblo1sGywD1hkxPH1ZifQP53m5aFmPnmhJJuBxl9bzvugJj00Lo6EKjFF3yD5CuETAqBkdNlwZDxKW_f57ZiniybA29AnTGpVFYh7ovIR3fbpkhPERFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 00:54:15</div>
<hr>

<div class="tg-post" id="msg-452823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTKwEPWNhkDCC3-csdleasqGauwgo3R1rBCnWVz4aaCnv6zLH-4JT34jonzZ3dqAqJeVJ-QlD1ZxznlriiAHKJYva7PQL58Maasstxu4HM6KrYo2BhxVxmUSnsWFLishsAaCsECDMFUMFd2bjCVtz8Bmmbhnupg4Z2Ly5Ik0tNscIayvM2lfZccsDCAu7BKsGD3o_eve-SqqLufdcmJ4DZeCCMxU5mNQK2RpJQglNMben1yseTruUI1Q0I8ZzNdlKRPTRrTcuOKhsAP7giBFHJg4TNISlz4LX0xKP9OaxUNFak9rr8QFxNMdoKY794oBYGUQ5YQJsPXr83y7J5OmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات معوق کالابرگ، سرمایه فروشندگان را قفل کرد
🔹
طرح کالابرگ الکترونیکی که با هدف حمایت از معیشت خانوارها اجرا شد، حالا برای برخی فروشندگان به دغدغه‌ای جدی تبدیل شده است.
🔹
مغازه‌دارانی که کالاهای اساسی را در اختیار مردم قرار داده‌اند، اما به دلیل تأخیر در تسویۀ مطالبات، با کاهش نقدینگی، انباشت بدهی و حتی چک‌های برگشتی مواجه شده‌اند.
🔹
فروشندگان کالابرگ حالا بیش از هر چیز خواستار شفافیت هستند؛ اینکه چه نهادی مسئول پرداخت است، دلیل تأخیر چیست و مطالبات چه زمانی به حساب آنها واریز خواهد شد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/452823" target="_blank">📅 00:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8CB_jN5iWEC9pWZLXgBYiiwidyhwvJS7_6QSIMm9w3Szo7CBql1gYe3gHQNZGCd8OJnXpwF7P1HiWos2lVDVtZkLumTA1oX5d3w8Z9Nt4ke-jbCYkWWssmEjrUWXtppqDjWmN8GNHlHkPl69Uw7TYherYUwkfj5jhIOyCvLunbiJ8jM1hjoyKLflWkpsRC2K0DJtwV75LTnnM5ndTHKXxeu8dwWJ_uvEFyjyE-aqtKpPOs2HWOT5oaX4t3qrxlXVVQFxZbmhZBrkxxZtmQvMikewXNMizAGzS1HuOU0vGnnlhQMfEhB5AM821WbBuDvJh9KkhI1Xuxfp9wS9xLEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با کمک هوش مصنوعی از تنگۀهرمز عبور کرد!
🔹
رئیس‌جمهور تروریست آمریکا طی ساعات گذشته پست‌های مختلفی با کمک هوش مصنوعی در حساب خود در تروث سوشال منتشر کرده است.
🔹
انتشار این پست‌های مضحک، ترامپ را به سوژۀ شبکه‌های اجتماعی تبدیل کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/452822" target="_blank">📅 00:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تردد ۵۰۰ هزار زائر از مرز مهران
🔹
استاندار ایلام: مجموع تردد زائران از مرز بین‌المللی مهران از ابتدای ماه صفر تاکنون از ۵۰۰ هزار نفر گذشته و خدمات‌رسانی در این مرز به‌صورت شبانه‌روزی ادامه دارد.
🔹
ظرفیت پارکینگ‌های این شهر برای پذیرش حدود ۱۵۰ هزار دستگاه خودرو…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/452821" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452820">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f4ecd59a.mp4?token=rBcEBqN0PJXTx3FV06ICCLxPncEF5C3beMFY3WLRQvEa5aKAXYCXUbZLTTjctrS1d5WmS7l3MjNCPXxcGp59lGPl5qoB-w1qQo9FhLC23vBs0nLRrsvbWJ_QYNsqHgdZDOYCLh6HD7BdJdy5onM5Rj81_F-h7QEpM-05QoVz8x5rATh8TQIXHCrpXMVzDqypzn36QQLPNj8oyFbLydLi-DgvSWgInDd1ZmtEgCcPytVXtGDR2c_vQSDm-MXCRhfBd8Bs7HCSZ3r9q9Hyo2kLFYYbQoDOHHX0mld9QkI1tUfqclbZnHe3CKPvxVUv9AF5k_2-w70L919W06e6FknYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f4ecd59a.mp4?token=rBcEBqN0PJXTx3FV06ICCLxPncEF5C3beMFY3WLRQvEa5aKAXYCXUbZLTTjctrS1d5WmS7l3MjNCPXxcGp59lGPl5qoB-w1qQo9FhLC23vBs0nLRrsvbWJ_QYNsqHgdZDOYCLh6HD7BdJdy5onM5Rj81_F-h7QEpM-05QoVz8x5rATh8TQIXHCrpXMVzDqypzn36QQLPNj8oyFbLydLi-DgvSWgInDd1ZmtEgCcPytVXtGDR2c_vQSDm-MXCRhfBd8Bs7HCSZ3r9q9Hyo2kLFYYbQoDOHHX0mld9QkI1tUfqclbZnHe3CKPvxVUv9AF5k_2-w70L919W06e6FknYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدرالحسینی، کارشناس روابط بین‌الملل: اگر اروپا در اقدامات آمریکا علیه ایران همراهی کند، جمهوری اسلامی آمادگی پاسخ متقابل را دارد
🔹
تهدیدهای ایران در مورد برخی کشورهای اروپایی معتبر است و توانایی داریم که پاسخ دشمنی آن‌ها را بدهیم. @Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/452820" target="_blank">📅 23:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b72f70b.mp4?token=XiOPYvWoKyg3Uora3_8AV6x8uqSyOkRpxIDEhlt5uZ47BRtaO042jej-8mavkWU1oYXPCPiYlTcd4EkHgXitdIurqK2C9b8LjGqBu3czgvA4tqnqiWH0-kQ3iWT8vMlbUjITgrsjTA13mEcqRZG5MdOpHWRH8o5dp-0I5twWjlsTW5Hexb0u-2-TPgEvmgzy2nRZum27ExaIspfWDcNTRHbQ7vu48v0H_dKdwqQxfTFBGUvNBqzaSBjfECV9dIGQaCTt7Mu_Pns9S16LiKBL0HxAwplRRT6jucO4p8SB8vGBfpXAVTyTCVNrYrJwj4JKnscvVuXwb1c66wNgGPDLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b72f70b.mp4?token=XiOPYvWoKyg3Uora3_8AV6x8uqSyOkRpxIDEhlt5uZ47BRtaO042jej-8mavkWU1oYXPCPiYlTcd4EkHgXitdIurqK2C9b8LjGqBu3czgvA4tqnqiWH0-kQ3iWT8vMlbUjITgrsjTA13mEcqRZG5MdOpHWRH8o5dp-0I5twWjlsTW5Hexb0u-2-TPgEvmgzy2nRZum27ExaIspfWDcNTRHbQ7vu48v0H_dKdwqQxfTFBGUvNBqzaSBjfECV9dIGQaCTt7Mu_Pns9S16LiKBL0HxAwplRRT6jucO4p8SB8vGBfpXAVTyTCVNrYrJwj4JKnscvVuXwb1c66wNgGPDLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدرالحسینی، کارشناس روابط بین‌الملل: اگر اروپا در اقدامات آمریکا علیه ایران همراهی کند، جمهوری اسلامی آمادگی پاسخ متقابل را دارد
🔹
تهدیدهای ایران در مورد برخی کشورهای اروپایی معتبر است و توانایی داریم که پاسخ دشمنی آن‌ها را بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/452819" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452818">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp7vW8S3xvw_ze39oC38bYPAnQ_tzoS_DKawvCLWWNz77Mxl7buyymMJO2ZPU6Sf_DN8NiYYlTnetSFjcsqWRuNq5_Nyjn9HHu8oXn-20cL93sw7fm5ysik7OfexhzI767GtdghvRn76qPUA8_PBHYNNVS--hMUzhvO3obumvKPTglzaEqGUZKgJ5HQDy1zRucMIzrHWwgPUBDH1UFA6GHSN1uDO9yHsP2eX1ZUSoUOGYorlfBkTA7yXx5g-FfXsU15y8m5csm50J3SoBp0KYeZnL8WVhzP9K4L_AMx7xoIPM3_AoO4dCGUDZ-SAltDRFuAFJ1k6eEpjF6QtTW_PUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹️
رضا شاه، بزرگترین زمین‌خوار ایران
@Fars_plus</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/452818" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452817">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4de6a51b.mp4?token=oE2iozIeNH1Fkmre3NCspAmlxzJqoe3audEtfNkcFR99oPFCqOFXhWVvFvZWM2a78hyOXFd86UPkkMe5WvZhmC-Qn4t284JibInOccm0NRdU2NXt9A4EBKIykNwv4GY2jSOQevup3Fe17i-drhD5h4NlLy8vHGeNAXBv1DfTeC_sXzk5Shs_RpS9wfQ0ZgXy1RPqQDtByOyHRy9yhUTxCTVR3PgvvZBt17ssd5ZXDWwaAmQFwctjnGKk__fxo3_iv2PG8zyyKvi0rr2bGIzOFQmTHCNto9RYb35G0wyajG5CBNw-5wwvSOdX5ow8g_DB8LJJSkvQOKl64mdge1zKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4de6a51b.mp4?token=oE2iozIeNH1Fkmre3NCspAmlxzJqoe3audEtfNkcFR99oPFCqOFXhWVvFvZWM2a78hyOXFd86UPkkMe5WvZhmC-Qn4t284JibInOccm0NRdU2NXt9A4EBKIykNwv4GY2jSOQevup3Fe17i-drhD5h4NlLy8vHGeNAXBv1DfTeC_sXzk5Shs_RpS9wfQ0ZgXy1RPqQDtByOyHRy9yhUTxCTVR3PgvvZBt17ssd5ZXDWwaAmQFwctjnGKk__fxo3_iv2PG8zyyKvi0rr2bGIzOFQmTHCNto9RYb35G0wyajG5CBNw-5wwvSOdX5ow8g_DB8LJJSkvQOKl64mdge1zKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک: رژیم صهیونسیتی از صبح امروز حملات توپخانه‌ای را علیه جنوب لبنان آغاز کرده است
🔹
در این حملات ۵۵ شهرک در جنوب رودخانه لیتانی کاملا از بین‌ رفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/452817" target="_blank">📅 23:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452816">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a2d1b2945.mp4?token=GOGOzhuM3aCQUdwz7JZnDFh7fL-theHeBTpqaWj1Ghtgyu67-AslaNIqw9fU_T97nDO71UjLGqM5wDKwZpdzjzp7CuFheucC9wrCET3xUr3Ux0K5rpxOCnW8y3byvRTOXjh1Fqpa_aVv44Rvg52MJOURuJxX8uMwUs4Hk-iUCcHO6O5LhYXJEFNOXTGy5AVRIIyN55_xjcBc67QNJLAPbc9z_2_nrFE0H_gIAwFTNQ87_d8a-RheCJtVBTsNZJ0i_xs_vWz1HtK-JeVt8BnhlRdaX1Z2IgEQ6bMzVkTIadaxc5iAXipov4P1ZBsrtcPYVv7xKnZJttMEeax6_5lav0R_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a2d1b2945.mp4?token=GOGOzhuM3aCQUdwz7JZnDFh7fL-theHeBTpqaWj1Ghtgyu67-AslaNIqw9fU_T97nDO71UjLGqM5wDKwZpdzjzp7CuFheucC9wrCET3xUr3Ux0K5rpxOCnW8y3byvRTOXjh1Fqpa_aVv44Rvg52MJOURuJxX8uMwUs4Hk-iUCcHO6O5LhYXJEFNOXTGy5AVRIIyN55_xjcBc67QNJLAPbc9z_2_nrFE0H_gIAwFTNQ87_d8a-RheCJtVBTsNZJ0i_xs_vWz1HtK-JeVt8BnhlRdaX1Z2IgEQ6bMzVkTIadaxc5iAXipov4P1ZBsrtcPYVv7xKnZJttMEeax6_5lav0R_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴۸ شب میدان‌داری مرزنشینان آستارا در حمایت از انقلاب و رهبری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/452816" target="_blank">📅 23:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452815">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/605deef080.mp4?token=Ixnt8MwCEe1ECwO2-zzdyo5s5DJmlEUN1nv9Q82fykuwj-vQ15C1fHsTVF1Za8J7hoqYdPvJQWNJ4VQ2kD6KhlaP3YCN1ARc7cnxGN1rfk-FhJXJZCvPsk7R4vHaZDB1D5ezDu6F_oZSCZbfHu89iDzdUMjZBD8ugiG0VwdugLMFOj5hOsj-2VTt2yxRqUInmxoY7OnhqETkKA6f1V8_wBm2c_nDwijf3Io8fNVdfvK1UfvAnv3qjUSxExRiUmsMwHgFF5T_YLolSbTbV_umW1O2itBIwUzAkyCypmdSDpFXE2amZe3L1lSh6qOGCSb9aZgygpmZNdTMYMpP-sikb37HzOfe4rg7xmy4g9cLqscHQMv3Eo9Be1K2iY52JE8JOAiRwXJslyJt0_FPkNj0KlSgKsPEMndPq82bwah-RVJUJnS0nliqb5u1r-zAfgTxRHDW8dT2pUuriQkJrIAO-4ny8c-vUXTP7x4ZK3Bxu7ABneYtKSlhxHMvN2dWVlE2t0IZcLR5U3hSmpxLHW68DnXNGsZ3dusQjJXwQW_AnPLtcrYHh3zFvypTO2GsgqFaZxTESwi3t6PCYllnGCDYZRIjzqIGZI98QcpWguVaMONKVNsgL3mC1AXVf2xoq1vueG8cPI5gnso5odeumpMlZ83U4OUg8TIRmsYfarTMbxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/605deef080.mp4?token=Ixnt8MwCEe1ECwO2-zzdyo5s5DJmlEUN1nv9Q82fykuwj-vQ15C1fHsTVF1Za8J7hoqYdPvJQWNJ4VQ2kD6KhlaP3YCN1ARc7cnxGN1rfk-FhJXJZCvPsk7R4vHaZDB1D5ezDu6F_oZSCZbfHu89iDzdUMjZBD8ugiG0VwdugLMFOj5hOsj-2VTt2yxRqUInmxoY7OnhqETkKA6f1V8_wBm2c_nDwijf3Io8fNVdfvK1UfvAnv3qjUSxExRiUmsMwHgFF5T_YLolSbTbV_umW1O2itBIwUzAkyCypmdSDpFXE2amZe3L1lSh6qOGCSb9aZgygpmZNdTMYMpP-sikb37HzOfe4rg7xmy4g9cLqscHQMv3Eo9Be1K2iY52JE8JOAiRwXJslyJt0_FPkNj0KlSgKsPEMndPq82bwah-RVJUJnS0nliqb5u1r-zAfgTxRHDW8dT2pUuriQkJrIAO-4ny8c-vUXTP7x4ZK3Bxu7ABneYtKSlhxHMvN2dWVlE2t0IZcLR5U3hSmpxLHW68DnXNGsZ3dusQjJXwQW_AnPLtcrYHh3zFvypTO2GsgqFaZxTESwi3t6PCYllnGCDYZRIjzqIGZI98QcpWguVaMONKVNsgL3mC1AXVf2xoq1vueG8cPI5gnso5odeumpMlZ83U4OUg8TIRmsYfarTMbxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبض مقاومت مردم کاشمر در ۱۴۸ قرار شبانه همچنان می‌تپد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/452815" target="_blank">📅 23:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452814">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0NIyqCO3hDzTa99vwHNaNz-dAF3E55dUTTv_ntnk_i0nRx4finJc23GL2MTMdudKQ-DFbkrPMiHMlm4DrYFishYhJRHemCvHJYXfiP5OixHCpwU_UXNmnDCifCPagwWhVLQiE7bHJn1y3EMfPO3ZAJ3reVTwEFXHN2JSnjUeeLkHCDxyQxxzqPgJ1LcFdbLNuEVqBOmOCrXw77EU7wDqmTeonCxYGt4mCual5f_jpxR9rgbfhSWct7CN82NR3c-JLtqyz4YuPEsU_alX3ud67gQk8rNXWwatqVZaTfDm3gb6SQOXjRcRtVNGZey1eLp5iecJ9Z1xCj3UlQx3cj3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت ما دفاع از ایران است
🔹
سخنگوی وزارت خارجه: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت برای ما دفاع از حاکمیت، تمامیت ارضی و حفاظت از مردم‌مان در برابر جنایت‌های جنگی است که آمریکا مرتکب می‌شود. @Farsna…</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/452814" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452813">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cb366f32.mp4?token=Opgf4qsofHvgkc23Pieb7LlL1W4G7yQiJudccQwL377L9pb4GDuD9mV9MiOZjC4hucDVYMx1_AdW5AYBr4U4lmcqLLu8jeGnqjng_QJ9eUR0KhLez5fQZIkiv-cX3puXA3I0zliojJKmO8vya6OzQRIashcgxfRFugQKdJ22Z_dhkv9lGB2q7fcyBhXYMKyW93L34SpG-Xkfk25K-f-wglabaFCHYi6OAm8vj3mt_GukxnzfN6qqPbHA7wEuel_pfAlPq8Hj1G1ysBRQwBL07_6zpyHSLbnTfjmMCPbkaTbV-3kLoTOcMHWAxekoGVLAgXNM4UZlcadCDfeSP0LBeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cb366f32.mp4?token=Opgf4qsofHvgkc23Pieb7LlL1W4G7yQiJudccQwL377L9pb4GDuD9mV9MiOZjC4hucDVYMx1_AdW5AYBr4U4lmcqLLu8jeGnqjng_QJ9eUR0KhLez5fQZIkiv-cX3puXA3I0zliojJKmO8vya6OzQRIashcgxfRFugQKdJ22Z_dhkv9lGB2q7fcyBhXYMKyW93L34SpG-Xkfk25K-f-wglabaFCHYi6OAm8vj3mt_GukxnzfN6qqPbHA7wEuel_pfAlPq8Hj1G1ysBRQwBL07_6zpyHSLbnTfjmMCPbkaTbV-3kLoTOcMHWAxekoGVLAgXNM4UZlcadCDfeSP0LBeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: ۲۱۹ شرکت خصوصی به‌دلیل عدم رفع تعهدات ارزی ۲۳ میلیارد یورویی به مرجع قضایی معرفی شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/452813" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452812">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVgXRfAjlR4KlGosbdSBUhKnlBeCg0OKZATMN_uXcSH567Z7m1e7ZJWBSfIq2Rn8ELmJN3Ujnt4VUi9pln9QhBm_SS_sYwUl5knN5kar2x-VyhWrJLwbYQ17lSXHVdKCbf-w9I1ZgIe-YqfD4bPH2x_M20sutPR4p_evuC6Kdnho1FteaYhVE5n_UlDJwTuhYE4c47B-TOmVFGnTLTYBh4sYiVCVim8tcAm_y57gdLA6VVpdY_xNaV_PlP4IXTwTwuaCiFSIdkIfjFVNFXKY-3nZItlHf-q6mrybUhluWw1Pg_6RCBKucjMeiFmKhoosR0A8OjpZ-kT4y9rbo8_mWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت ما دفاع از ایران است
🔹
سخنگوی وزارت خارجه: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت برای ما دفاع از حاکمیت، تمامیت ارضی و حفاظت از مردم‌مان در برابر جنایت‌های جنگی است که آمریکا مرتکب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/452812" target="_blank">📅 23:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452811">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87101cb2e0.mp4?token=kc13o4qCeOD5cmcf-4C7g3STRmMyP5cVPvPYs6dNZ5VC9e-yOzLD_jTdk-qGcwtEjxe_F419aX4jwIQ_tX7LqpqIx9HfDfbOHq38vqiC_3TURz0SGREiUpLjx_GBEQTVeojmK0vsLArI4AR-WpRWwHg9um_-ASorHJSsMlRofZNutXMcNZYhuz-RDqDgBXuc9ESjnMz3vFzsHKtLx7dU7vjSERy0-njqH0gHAxXItJvS-sbZIrOX5eLFlo2umv2iucWovx_ZMzjGGN7OqbmWsmSZpqHQU8piwZGihpnPpigiW6ejBHQThUXXFbFgySRRreTlbol-BJR7R0Li8tNykJLRcYxuaLWSHh88D5kh_241bG6hu-h5Bs65fLgJpBdCNwLRDljkKRLfLEDIrry0iB06Zyf38-ZetecY5hTrwxfRGkNWotdSMaEXOCyOf8f9nZ7uvtANDeUXhmSXmsC7u09S_zdtdUEALxEku_qS97qWoOMB5vvCNRMDif0WZghledX5N6Q-nj4ki-HOCk4gY03TQl4iPOeyqn1Aq9Jzgv-uYINMrkKuY9zNjX4TyNjuxe5Oj-t1KtTCqCohjZbpld2fBPV3DwvGxDMD43d9-_WLYSthVm-Aa_ME3cLnZZ9vF6uk8xlL70NxjqU-z7GKtm1ekzN0TYpI2qKK0TlPwzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87101cb2e0.mp4?token=kc13o4qCeOD5cmcf-4C7g3STRmMyP5cVPvPYs6dNZ5VC9e-yOzLD_jTdk-qGcwtEjxe_F419aX4jwIQ_tX7LqpqIx9HfDfbOHq38vqiC_3TURz0SGREiUpLjx_GBEQTVeojmK0vsLArI4AR-WpRWwHg9um_-ASorHJSsMlRofZNutXMcNZYhuz-RDqDgBXuc9ESjnMz3vFzsHKtLx7dU7vjSERy0-njqH0gHAxXItJvS-sbZIrOX5eLFlo2umv2iucWovx_ZMzjGGN7OqbmWsmSZpqHQU8piwZGihpnPpigiW6ejBHQThUXXFbFgySRRreTlbol-BJR7R0Li8tNykJLRcYxuaLWSHh88D5kh_241bG6hu-h5Bs65fLgJpBdCNwLRDljkKRLfLEDIrry0iB06Zyf38-ZetecY5hTrwxfRGkNWotdSMaEXOCyOf8f9nZ7uvtANDeUXhmSXmsC7u09S_zdtdUEALxEku_qS97qWoOMB5vvCNRMDif0WZghledX5N6Q-nj4ki-HOCk4gY03TQl4iPOeyqn1Aq9Jzgv-uYINMrkKuY9zNjX4TyNjuxe5Oj-t1KtTCqCohjZbpld2fBPV3DwvGxDMD43d9-_WLYSthVm-Aa_ME3cLnZZ9vF6uk8xlL70NxjqU-z7GKtm1ekzN0TYpI2qKK0TlPwzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بندری‌ها ۱۴۸ شب همچنان در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/452811" target="_blank">📅 22:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452810">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/847aab2d4f.mp4?token=lCR_nX8O78qZ9FTx44G-YfCS9d9DZio6WM9QTXFPbodDtvNsAhsoG5Cmne4vONzZbj2RGUfhxPdIbtxIc1JWvsFcmYbiEmctGbohNrU3AMIuONk6ucS7mr1ol77MTP3PQdJ1OWtD7ypqndHdMkT3RukQ3E1TrVzG72qgCGzRjwY3JWaUPGOIR49NzcQ3gYVMRSrnPWgPW-3LJXubzK6eiK6mlnGuDgAF5LOjA_zesxvd8tqFb0LfxLy6FfjI6C0emADPL_bOo1DQaDKfaQMwNs9gG6DVKlNwV1OZoES12hy7DQi0v6_6CMd7h_wAwcw45CDxOOWMYxNU-eK0M5hBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/847aab2d4f.mp4?token=lCR_nX8O78qZ9FTx44G-YfCS9d9DZio6WM9QTXFPbodDtvNsAhsoG5Cmne4vONzZbj2RGUfhxPdIbtxIc1JWvsFcmYbiEmctGbohNrU3AMIuONk6ucS7mr1ol77MTP3PQdJ1OWtD7ypqndHdMkT3RukQ3E1TrVzG72qgCGzRjwY3JWaUPGOIR49NzcQ3gYVMRSrnPWgPW-3LJXubzK6eiK6mlnGuDgAF5LOjA_zesxvd8tqFb0LfxLy6FfjI6C0emADPL_bOo1DQaDKfaQMwNs9gG6DVKlNwV1OZoES12hy7DQi0v6_6CMd7h_wAwcw45CDxOOWMYxNU-eK0M5hBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: برخی تراستی‌ها خیانت کردند
🔹
یک تراستی ۲۰۰ میلیون دلار از سرمایۀ کشور را برنگرداند و از کشور هم خارج شد. @Farsna</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/452810" target="_blank">📅 22:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452809">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf60d3589.mp4?token=CjrN3EXrhulXmMOHXJe4U_pPnpeWEZ1WWR-NLxC_7ETGGM-YKrCeW4zuOuw-791yVXs7m8UO3Fy_kDJG8ucF7PZDStv8i-yFXkZnYRurHfhl-ytbIONKgxzeFnMVerbd4sZIVwjLBjoBeoSE8RAeQopPuEZfoVPThunVEq4J4HWwnMBe68tBPEzxkTR6MPobjuwAkBIS_JaTipfQU2pe7_WhUaYrSkGVrzeMmzszhoVFvbOSDHekNFgwYUH9V09ODyJOUtqVI87igLGiIwNeEmG_KO9n4pIw_GS0sl_0fr6nRPXMfSzsaollK_KuiOp9dX8-5lsdUndXOMZ3hZz9cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf60d3589.mp4?token=CjrN3EXrhulXmMOHXJe4U_pPnpeWEZ1WWR-NLxC_7ETGGM-YKrCeW4zuOuw-791yVXs7m8UO3Fy_kDJG8ucF7PZDStv8i-yFXkZnYRurHfhl-ytbIONKgxzeFnMVerbd4sZIVwjLBjoBeoSE8RAeQopPuEZfoVPThunVEq4J4HWwnMBe68tBPEzxkTR6MPobjuwAkBIS_JaTipfQU2pe7_WhUaYrSkGVrzeMmzszhoVFvbOSDHekNFgwYUH9V09ODyJOUtqVI87igLGiIwNeEmG_KO9n4pIw_GS0sl_0fr6nRPXMfSzsaollK_KuiOp9dX8-5lsdUndXOMZ3hZz9cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: بیش از ۲۰ هزار شخص حقیقی و حقوقی در مجموع دارای ۹۴ میلیارد یورو تعهدات ارزی رفع‌نشده هستند.  @Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/452809" target="_blank">📅 22:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452807">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def8f2e12f.mp4?token=dxiqmcVjmt_RjHWWRm5m_3oKXxx8THw2bCj9gRZdF5ev52iizFLX7IWjkN6EOoDyN0d-cB44wB-jXmpT8q5U1smAKnrjP0n8RD0Vn5Jt3ggWCbRoYdv4PhTJcRzyJotIm7N8VRI2hs5xE212aGnGhmhmJ2yEu63irkyXd3f8FhnxekFVT7hybyoIRTI6_kt56e8O1j-lsWEvxh59UWRqbHGzHf9_RWwq1UaSTfQVM4T89c-1QtzDTsRl4GumF2OFLP9yZbQYCprwHKspclX2mm2A107K-q20q2G1Oj3n2vsvir8QSLvb6pg2tbwJg0uj5Uj2AcTpTwEZrZjFQ5VbgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def8f2e12f.mp4?token=dxiqmcVjmt_RjHWWRm5m_3oKXxx8THw2bCj9gRZdF5ev52iizFLX7IWjkN6EOoDyN0d-cB44wB-jXmpT8q5U1smAKnrjP0n8RD0Vn5Jt3ggWCbRoYdv4PhTJcRzyJotIm7N8VRI2hs5xE212aGnGhmhmJ2yEu63irkyXd3f8FhnxekFVT7hybyoIRTI6_kt56e8O1j-lsWEvxh59UWRqbHGzHf9_RWwq1UaSTfQVM4T89c-1QtzDTsRl4GumF2OFLP9yZbQYCprwHKspclX2mm2A107K-q20q2G1Oj3n2vsvir8QSLvb6pg2tbwJg0uj5Uj2AcTpTwEZrZjFQ5VbgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: بیش از ۲۰ هزار شخص حقیقی و حقوقی در مجموع دارای ۹۴ میلیارد یورو تعهدات ارزی رفع‌نشده هستند.
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/452807" target="_blank">📅 22:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452799">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRJQZgQHZ40QQH1Flls6SAKsPSP3TD9q_TGZ7LAZMJkXCAl1abxmYacM7vQjW8JCnCcbgV061DW4pp90g8aoOJuzeVxMDZx4i_HQblAirQvLGQZXVvr0sOhO1nSej4ry2CixHsK5HkSwiGO4lCSaEz3xOm2QZiYZ9Jov2tg22AuHUrQGmN_eAWmVS_0NfvWCLXMglEN5Fn2CA6nPryZd_l52RrW9T0kpK4rpdT617LMlJBp3rBhk3oCs1YPyuJEFJg9wfLNBlxqVSOnq4kI_tME6iAW28TBsOQG_vFtKSFd1Jm_WRRfbRhb_Gd7KTj_MWcXxvZwu1xHq07QnPlAH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/su5Bblta4zMnBUWCn3aboS01OkEdTjv6Qr4A27DkqLVkg_8rNz4WNs9ze50ZK5UUJBCt9lVBNjOxA9Rj84Oy8gaj1jyUaHNCD_vHStUPhij5mO6uz3A1SHKHEQXj6JWMTndHYTycPSGxMQeuNuzYUgbTE2N52a9DSG55dLSgLEs5bpxRr6-V9HA1tcMioyV3DK6wThoKrYla11alkTzUk_JjBASyqYMB5mYbWDzBgAQ7uCDHgG6iV801s8U3qZI-BqgdgVM_l8zOO4BsX9ZvZuZWBY0MRj0LFWvPPO7gIaOPTFE_DPvsTQt0HbALZHwuP4n-QAjaUmuewdZWEJ4SOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIMB-PJKj6550zPvnsjrU_m_442XytWAfRK9qvvki9NR086a_kQzuB095FyZFmU-mnB0Tuzd68CtF2-ZyZ8_2ONQk4uB8Ou7RpP6jG36p9U6x0h7Tb2C-dP7iN7plnzajuPuv4Ixa4tEa76C3CgfKUyhAAFGSoiKf4w6PpTjccb67mVlyiRpKHeEF5REy5vRqNXW35EOqIVYxo95ph9p6isPDmLaAtesth41wuYiS4nuCn1vOGbeZGrlbITeo-XgDtUp-B21gQEBSxQ5wcwADPf9FGjIyLjG9x2Rf8T1qh-WWdRtQvBE08NGivuLkRC7fQzePI6oJFuyETxOsD4K7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uL9grupyuwhnNgMVrHF-aKSBXpP94ktp0TgtMZiIOvfsIYApSWUYwhjCOGNECPWRpx4LRQwz6oKe7J4ib_ONwWh0p_Fu3bZ_W5XHn-4rgwX0GuZgRoxY5mRnduZ9f78tKI1SO_xVUibqXVIB8f9MNsKDP2p2T-CnnEn7W6axG8rCUMvsAicEgRzbuB3FLn5vYW48YJFhIuGljeLC0TgT2xY4zDJcAKx7dEFBHNZaFvKeWAyvImUBiy5Mr72o_P3oYVaRTJgiDZNP7eoyAF6lyPta-nu5VfumbTDlRDjb_ykUDef-6F5eJ0lYNCykqVozudtCSV8lDb-aGU-5_-8yHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/enLoERWrs6GO_5roakQ0GENNFe_PYI4c31cENrrdaAaeJAuptik3v0MDynUQDgq3GV6AFvWDHnimO1n7nc2CwU5GlYA1_KHrLlOv7sAQzvVQksLdPS-8GmBBvNIhS76Fg4MrfBFgbCfKIFajS7_pie6arfPXaawEBt8JgiS7BLFtjEv4jl2qQ6_-YbtNsIQsFW6jOt0WzoR4oYQqMiQpXuo-nKUWHSnTXKeOMraoUGtS1supvjNgS5BmH6SH58oR7_nQHIjuuRZr0KeakZqOsbwOBh5BS-2NSTD-lv1y9fDEGUfVCecoHZdlw8g5oMJMRKe2wB4R0eWBF0tJlSA8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6ufPCTgS4WDHSP2Go9rDhJQCozPLXH2yvFpk4Qu5htwhwoMcy83lK4n8VDpMf2jLIak8-5Bx34U8QNHz3xb0f769p9gOwzj1WoloR-snGIorZkVuGh2X6BUx-63lhQglzD9Pi_opxogWUmcn3RP2Yjz-quGHLp5x-ChwDRw8xzK8_zWQMtFnBeORteL-m4ez31S83yyOL5Shnh8SQDcCy4E81A-ldjontmSdXvkuNh5hE1jL4hUy2D5Hu0dVm1-EPfOBYK9IVMmA9LutfJp9Dgh9nYghWTWDeVEcJq9zdO57BZv1zapGfAC07l0zsPFXzXUCkRakGWbibBxU3bXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMkHOsQqFOh-DkSVKV2spOAi2dZY7oHdVJpZfeS85yimv4EfmNP1Af_a1WEgGe-HzFpC3LF3GpqijEiVKGq06XspUaf0PHceX2PFd5ema3sKZTt8ZDUuTP0wGgvdm10751HYgoBBm60mL8pmQAi9VDr-p2A22-bststMZqSHkFxBB5EwGsxYuul60aT2yPDoJSVjihnHH3q9u7efs5LovgjDtpKnvg67spgcn3eUzM6BtOkN3y11ll2KTx7b_G8OB8VGRTfJS6At8ytZeP8TmTgKE_QZdbNujhvexnyPyNn6HkUqH6nKWmPaRpsC5NEKLbOABioG48fSXGOWHq2huQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تجلیل از پهلوانان زورخانه‌ای تهران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/452799" target="_blank">📅 22:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452798">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe770a69f.mp4?token=DzfFDrZnyNoboQcwsQo_eHwVK5IPzRC5bJ-8EO77r8Q1BiK7rEvwd0iYeZ41CXgSrv_Q5cJC8JEjHdqPOPU8-1mWW24S5BggYvMNTffsLGKADRbXMqo9JaopUBQOcNxEqcweJ3OsbaCyeHUY6tr6BEkjFLaW4Fk8XMNf9BSNiDNd8OJMywhIi0ey3vo4pO6ajkO8S2moy5t1bs11gF8QYqLm-6JtTnyWE7UBZW0eIhHFinjejIMfUZoRkHv2eA1yOQp7TTuGhyk8FzCrg5Z_hFP1wAlqXipFF-ceafcjWZ8YiAMrlYcAxYCTwswqSZq1d-F50T1DRti-MgjFTQJ4FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe770a69f.mp4?token=DzfFDrZnyNoboQcwsQo_eHwVK5IPzRC5bJ-8EO77r8Q1BiK7rEvwd0iYeZ41CXgSrv_Q5cJC8JEjHdqPOPU8-1mWW24S5BggYvMNTffsLGKADRbXMqo9JaopUBQOcNxEqcweJ3OsbaCyeHUY6tr6BEkjFLaW4Fk8XMNf9BSNiDNd8OJMywhIi0ey3vo4pO6ajkO8S2moy5t1bs11gF8QYqLm-6JtTnyWE7UBZW0eIhHFinjejIMfUZoRkHv2eA1yOQp7TTuGhyk8FzCrg5Z_hFP1wAlqXipFF-ceafcjWZ8YiAMrlYcAxYCTwswqSZq1d-F50T1DRti-MgjFTQJ4FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بجنوردی‌ها امشب: لبیک یا خامنه‌ای لبیک یا حسین است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/452798" target="_blank">📅 22:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452797">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4689a10913.mp4?token=Ag10z6Gp3lDMMA9kUWdm53rVIVknK1q7FLGlNxXQktjomy-zs6B_P0kEwXMr3Rtf809LyRzDmDfIs_fQhAgoA0mxzFHLzB1dLSmU0DL9lx1ERf3Pi8_JUlN91wua9EnnVPon3neTC-j-nfgTAsVIK48nymNOP6RD1hjnJoU3amrTL2Rp_4XFxyqc1tm2kdcQrquf1EZ-OcdDTNYZ1VsB0a6FKhnldbHAjMSQ45Yo1y2Gx9Ud80TfXMLv4_7AiUEKvMSmY1mvi0WHSnXQPmMYstNPB6A0yZcrHzaOL9XlkX1Op2QhzrP8o1i8g12_YARVc6Ftu05qASxoShvhnYGV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4689a10913.mp4?token=Ag10z6Gp3lDMMA9kUWdm53rVIVknK1q7FLGlNxXQktjomy-zs6B_P0kEwXMr3Rtf809LyRzDmDfIs_fQhAgoA0mxzFHLzB1dLSmU0DL9lx1ERf3Pi8_JUlN91wua9EnnVPon3neTC-j-nfgTAsVIK48nymNOP6RD1hjnJoU3amrTL2Rp_4XFxyqc1tm2kdcQrquf1EZ-OcdDTNYZ1VsB0a6FKhnldbHAjMSQ45Yo1y2Gx9Ud80TfXMLv4_7AiUEKvMSmY1mvi0WHSnXQPmMYstNPB6A0yZcrHzaOL9XlkX1Op2QhzrP8o1i8g12_YARVc6Ftu05qASxoShvhnYGV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ سقوط پهپاد ترکیه‌ای «بیرقدار» متعلق به نیروهای سعودی در یمن
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/452797" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452796">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf4462493.mp4?token=ACvL6Z1VGpFi3vl7rzEMXv7oGL6vkjC-LdSyw7DumtP1hdC-ht8jMweOybpMExffIqd-hqplkSlXCrmdgnYR7s2T5ZJH1sUP-0Nj6yFDfJ5YVnehoO6wlyqsw-UTvdGs_KdGRvDI13cQGgipsWJ_OVo2ZcYM7t0hsgoFk-CMkLzqeDb5C-2fgMHZE9uVSDl2_YoYkY4hUIlwX3rST2Jm7ebkQ3SaYNUq_5AdPbLqSfcXgku0iJe0HIBOws1Z601CgfU-00iF8WAAo5Lth7GWdLi9RQ__SoGjgOeFgcDOWnaRAaom9Uszc0hn_5ESbTTBRNqUr_yXhS752z2yecFUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf4462493.mp4?token=ACvL6Z1VGpFi3vl7rzEMXv7oGL6vkjC-LdSyw7DumtP1hdC-ht8jMweOybpMExffIqd-hqplkSlXCrmdgnYR7s2T5ZJH1sUP-0Nj6yFDfJ5YVnehoO6wlyqsw-UTvdGs_KdGRvDI13cQGgipsWJ_OVo2ZcYM7t0hsgoFk-CMkLzqeDb5C-2fgMHZE9uVSDl2_YoYkY4hUIlwX3rST2Jm7ebkQ3SaYNUq_5AdPbLqSfcXgku0iJe0HIBOws1Z601CgfU-00iF8WAAo5Lth7GWdLi9RQ__SoGjgOeFgcDOWnaRAaom9Uszc0hn_5ESbTTBRNqUr_yXhS752z2yecFUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد انتقام‌خواهی مردم بسطام استان سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/452796" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452795">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJP8xZ7rSuD_SX_gtzkk3_3wVc_RxaOlZnZoGpEjxlcWap_sYISGzFucvUVP-4x8Z283I7v8ZOCwqy4Tbjk78PMRFR2aoEPbgqg9pWsBS1mX9ShbVL-DaAbeq4MNSIj_SnQoPyRjLbYwa2d0dZfqBgjoMC3X-0ZqS3Jb-n3LIA0kINOYMXsIyZeh3HDEgFsPj50s1K0_iU3L35F6vNufMuLxCLxpJUnXpI1lMKznZBtTYfWCmLrtHZ17YPXTPPGDEEpNiL4jbY9AuC-47J7gogu89_iDhl3zM05jAQ-aEmtFOm2aTLwQdNpukS0TAl7JxjTSfo6TtlPBk61-UV_cDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار رئیس سازمان بازرسی به متخلفان تعهدات ارزی
🔹
رئیس سازمان بازرسی: با کسانی که به تعهدات خود در موضوع بازگرداندن ارز عمل نمی‌کنند به‌شدت برخورد خواهد شد و دستگاه قضائی در این زمینه کوتاه نخواهد آمد.
🔹
تاکنون ۲۱۹ نفر برای بازنگرداندن ارز به دستگاه قضا معرفی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/452795" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452794">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc9526c05.mp4?token=CPfqEyJtqr5qLy-zDF2uLv7pl_NrlTBPIMuWMrzLSuUjNECYI0OPzmaY5DPP75MFLDC1ZUwWhzC1pXkjXcmUGqV0o2b17uaxbgF_YhDhiJAKj0_FNUW9veSz2fKtaiw_ZqNqSoW622PSgDhO3ZSwDmNuMGizjXtlAZwI3D2fEWTDzGBTwJjKR2Ey9K8F3IVLNM_xd82uR2W0GGBV0kzQRJJeKmVo17Z6DcmmB6Kq4i-weWA9dUDB_eKB-p2H7ifTBYa9YnLDzquvBfnlkcgZjvsintXauhhxYnOpIrrEgipR19TuVsS6jYvTR_yCkHXjwKo-GX6cSUbui7y7sEISAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc9526c05.mp4?token=CPfqEyJtqr5qLy-zDF2uLv7pl_NrlTBPIMuWMrzLSuUjNECYI0OPzmaY5DPP75MFLDC1ZUwWhzC1pXkjXcmUGqV0o2b17uaxbgF_YhDhiJAKj0_FNUW9veSz2fKtaiw_ZqNqSoW622PSgDhO3ZSwDmNuMGizjXtlAZwI3D2fEWTDzGBTwJjKR2Ey9K8F3IVLNM_xd82uR2W0GGBV0kzQRJJeKmVo17Z6DcmmB6Kq4i-weWA9dUDB_eKB-p2H7ifTBYa9YnLDzquvBfnlkcgZjvsintXauhhxYnOpIrrEgipR19TuVsS6jYvTR_yCkHXjwKo-GX6cSUbui7y7sEISAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حواشی دیدار یک یوتیوبر با هوادارنش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/452794" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452793">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ac8177e97.mp4?token=p3E1P2dHgVZMajsLKpyDnjtHfxql3T48oMKlDI_aletzcn9w3SPkEi63mqJZ1atBUt4833apM_4cTxgYnQcIGiUBTm30lgglhBO3MOZ_zFY9_MZwPkFwb8N1X5WK6p-cr1coDLrEBB2VlCIeoMojhrnfXaakHlv3Ssn7wPVmEMicy9u1kY-2A2oP_HPLiOIHlNdjOiZloR6FwmjtfmM_KwG4ygxzvWb_6CKeY-EWWfw6zxJ5gEGmW6JcpkRcRRjxsh89iZXSPtiC_evWzlvrCSrI7aDgTpUDMAw4J7F1YzAXuJgf15rEj5g8gwt3axJY5zjLain4tVVoo2rSaeFBFCAzW6AcSfiauUZV-P3IbPGJskVQg20sqn3Bt8YSZ_gWpxv7rxjUe6qkfeC5algk4Xv5HDb4MpNzex-EoeiwCxV7x-P2XbCOd892sG3TXBfG_PH3oKxbk77KfbTzaGvLUxpWxr-7BRY9GkkbPiOAbnQzYbTx8bqtrsS-5_vRND65lgxv3C6WE6PXiZgrqJ0yIXSIw7jGnwplvUJgI1Wtk_A9-NLfldjJfp9CW3VOn8Q18RkL_hXgm3YtFKht0a3MabBk9hjFe6YxeAYRYLXZfSOhhDNSjTBRToaMwkRqOFsgA8xKzQXNP4y6qs_zXG3tjqnWn6qxl1kVXPLd8y4wjJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ac8177e97.mp4?token=p3E1P2dHgVZMajsLKpyDnjtHfxql3T48oMKlDI_aletzcn9w3SPkEi63mqJZ1atBUt4833apM_4cTxgYnQcIGiUBTm30lgglhBO3MOZ_zFY9_MZwPkFwb8N1X5WK6p-cr1coDLrEBB2VlCIeoMojhrnfXaakHlv3Ssn7wPVmEMicy9u1kY-2A2oP_HPLiOIHlNdjOiZloR6FwmjtfmM_KwG4ygxzvWb_6CKeY-EWWfw6zxJ5gEGmW6JcpkRcRRjxsh89iZXSPtiC_evWzlvrCSrI7aDgTpUDMAw4J7F1YzAXuJgf15rEj5g8gwt3axJY5zjLain4tVVoo2rSaeFBFCAzW6AcSfiauUZV-P3IbPGJskVQg20sqn3Bt8YSZ_gWpxv7rxjUe6qkfeC5algk4Xv5HDb4MpNzex-EoeiwCxV7x-P2XbCOd892sG3TXBfG_PH3oKxbk77KfbTzaGvLUxpWxr-7BRY9GkkbPiOAbnQzYbTx8bqtrsS-5_vRND65lgxv3C6WE6PXiZgrqJ0yIXSIw7jGnwplvUJgI1Wtk_A9-NLfldjJfp9CW3VOn8Q18RkL_hXgm3YtFKht0a3MabBk9hjFe6YxeAYRYLXZfSOhhDNSjTBRToaMwkRqOFsgA8xKzQXNP4y6qs_zXG3tjqnWn6qxl1kVXPLd8y4wjJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رایزنی عراقچی و لاوروف درباره حمله اوکراین به کشتی ایرانی
🔹
وزیر امور خارجه در گفت‌وگوی تلفنی با همتای روس اقدام اوکراین در حمله به شناور تجاری ایرانی را ماجراجویی خطرناک‌ و تعرض آشکار به اصول بنیادین منشور سازمان ملل خواند و گفت: «قاطعانه از امنیت و منافع…</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/452793" target="_blank">📅 22:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjNPvjUFHWvr-Am7sKi9Ruho1y-DCLaAX0nJf6p66mslX4MDCgDCWyv5_2T8vcJKp2xQCsBNUHsTXtwgrO9BgDjvoXujtGx1xUGZwJktYGV2PypNm1eTsmsxhWqP3dY_tuezjFRnqPiuajq1CULaz8gp2ksx26BAEFV0OuoyR5ljh2_-2gmI1N63JuItpFCPIXhyNDwMDSW_reCpjqDcMNceCN_5htLRkTrp3ae192VDIsIa-NvfFqPVyZDeyzT3VwMhl448kTAKtXt3N8uq4tuzK0gOiqkcv1icoaxDitHJU8EbZQtPUSpbZ7S4CCMfuRfIQen5M2lUbZX0QFf2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKo_XRnDYm59wu9NviqUPCe7wMiR37BAMRvi5bEJqDPq9Rid2HnhIahOCYgmRNnjaCraY7wfaUepL1i3A5N7psIg1ezLg__xPVrjpRpcxHyNlpf4ksqNssElMYa4z3jQYHf0CGOFZSx5XCH2y749PvJeyVWmyaFleN4axhBn67Gp5htZ3a0FLKp4G1qZ8JD1BuevgVTIV3XS1HfldfgYQGCVovRQrpmd-99nDAoz84nqRQ7TO2M6OcMkQ7lTuhD71hrsZqaRqA7cP7687NkV5IKCiqrfFEPFBrdEsv78Audd9roiFpALiGTramiUvNdZ0VlkNH9KwmdY3ePgX49LJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKWlzJwVGCEGd9HTeTmtSgEPvBdW1jfRu21R-mOGlBj4me9KGVdJcPc7qZ6iyUB-0zrZbC6tdQzB79yL2sXUDMNBMA6i2To2tnrawFYkdcj_hwJxQWMs25KIa3Ot-gsuoDyJ_RCBt9i4ZmOm0XTsb1nO_t2_LnIRvVc2WIFckyyJseaZ32ulj99zFsiXdsL5N2dllGcT73-pYxi2PWhI3tfSes_W-lAp-qNrz_DymjQklmWgbgPfH3k8hwuZgNvBv1HtYYCaEgIOxe4IHQAOxTObxxd-uqn_7rQ5DoYVozn1hDN1bPmXpkAwJUxIfP27YpusQS_Qd_ySCwOcqa1rVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikkwn570r-ZlbkiSFYIP60LkoH32eOI7pA1EWyUAo8wfty2HAYcfsiXS0dSHrI8-2k6rPwoMv_9aex2I5B5SfYewzY9PP70ta9h_GbIvHRePj1FQfQUhZ4VTXZYpRSwGVswmKMAOpqx3KYcBF784ERXf0eWLz_q7O7f30UgQNsDNutG6faV6whiKfftELLTvr25ZD6XQa8kIq_Z5puuVRZyZBDWQGtdUbm312ePPfSkVUBpFFyInQIE55wUxuZf9NBEYYOHiL78ZtXvq3MvY_Kc9Uc5UAb3veoTq8A9iwOMWnahhVcJfxdmjzUjn04vZU-_8Or1gNfmgVJhNt6-BRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6s81vaY8IINRxxO7TKx_CY7kQZy2QhABjHKMwuoAOQmQAgV_DbKD20mdh5KkqUteULF1JD0ZJaVgglAaa-5DM_n-2n7N1IQNp0vqnz9KSiw3ZB1bVJloeS8d1N-7YeWVjt6nOKlJWJEGoEEumlcG-TkryXj1x-oDhNkXpN4L7ZxW1Xkw69JTbqczbyVSc2sn5-2nMzMLtqfJbAvjnDC6JxLLHBlCBlhbWWDZl9bcG0SVbGYvZpKhgZpbt6onny2xKVVDW0PX7qDnD3c3jMd1xYdXSr88OO_5eWVd2r-9-p6PKq8fOBgbfEQTQCVuDpd5a09RY6kQIUORnrvkKmz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDei53wh85AiNhrY_breAD-QcnZoXLhdqhMExXF0wwaPR80_rFqLNhC-yTixeHp3j9qSv88_gqZpPDJf-bH9xxSWox8g1BjP4scMoOXFy6YAH_3Zz0vO3kjK8KI71ZTN0gCk86MtfjEv_vewbnOttwwumykvpmMR5A_O7ymkVzeDsnz1ElVYGCvyyU9hMa6s5LmUmno_Zy4vieLmHnR_UX7DAWe4n6ZN9HPx2tm1UV_1CWK64IyroVM3Czt6OLK5joO0PiR6eKmxZ6hkJDASP2JRbWyzNMC9fdCAevGMucKGPELcsxspj4blsbpKkkZPvHcoidASxN9Dfzi4fBMung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXQagv95EsaI6nGuKSvtK6ZqVaMZ2Ragbk-pDSMtnid1dC9hCVyAqmiACr7gdoNGY1jvLodncfVVcw50f1AOu3B5UpVaaXmqDTAwRm5m8-1d77MyypSmYkYKAd_0FyNyoY-vUzhYulW6TITSZjoLCPdsFKxrDkc7V2yg5cFgaJQd5hAlMIDuBwcMFutoOJBGu6nSloScxutil9M5VqUbBGnuIeGPZp0iP0Qym4z13u0C0_-VScxZ-5GkyN5vLZCFF9i05KcOY64Lh9pzTUqopI4ml9Qms6RYfbGjT6EsU3c6NQh-xya_7ZrPdwAmi0sC3EfuZecT4njDLMp_7jMYNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
ثبت جهانی دژی که قرن‌ها شکوه معماری ایران را روایت کرد
🔸
امروز در اجلاس جهانی یونسکو، قلعهٔ الموت و استحکامات وابسته به‌عنوان سی‌امین اثر ایران در فهرست میراث جهانی به‌ثبت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/452786" target="_blank">📅 22:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYuOpQQKJskwlbBcSmnVAKGwPsbsb7rqJYmc2OGNv4ZlKj_dEKth2um-L5klqJBDHmE3qDKvimFao2ZNbzSC08xNNnuXe1d8fM623TMbHb5eieNkGSFJ5dR5oeU4NniPjW323GD7ug7x_HtaeyJlIn-XqzXtm-Zs-qKHlo3LwagqzTLzEq1ADwmX88I4xY22mpzxOjOM5suB2MhRMJ209BmjAo-EaaXW51fATIAX2olCO9dP-x0AVMgL5QKoYRR1VnXnqWc2rZtYxZgFkePdXCkI4xBi7Vl-OrLz28QHu8-pH_cFl_aUywMfvfeukITva-YsNANbkeiehbOzUv5KGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی به کمیسیون صنایع مجلس فراخوانده شد
🔹
پوردهقان، عضو کمیسیون صنایع مجلس از حضور رئیس بانک مرکزی در نشست فردای این کمیسیون خبر داد.
🔹
پوردهقان گفته «وضعیت ارزهای بازنگشته حاصل از صادرات»، «نحوه تخصیص ارز به خودروهای وارداتی» و «احتمال افزایش نرخ سود تسهیلات بانکی» ۳ محور اصلی گفت‌وگوی نمایندگان با همتی خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/452785" target="_blank">📅 22:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452784">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d8655195.mp4?token=kBfbFXiHqdB6f4gdjqXN9BBllM3iQRgCvbCdoMfRe2iNljpf131oYtGJ5-UM8LVfL2029qvP-4MsjmdBmF9eHEsM9KgPTZyV4-AHSeL1T4E_Ggd76g2nku-q-OJ6NHvemR-PY3Y2dBoz5SD9mKRndPXzZjzBYpfk2B6vXpf1PaTbhXXdYILEeYZ-TOlg0uFYbxFUY6rW2xnkSf4heEpod0NsV2o8Yku-wveXwiQVW_qvgTegm_BfAyp-Yl0z98ZTqwomtHPVCGN4mnm7rAPKpiUCHmMkT0oE6yu9bYh9CNAyKX8V5dVvxPpMcqJX6S1t_GJbGNY7m-XlsPubNo2sPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d8655195.mp4?token=kBfbFXiHqdB6f4gdjqXN9BBllM3iQRgCvbCdoMfRe2iNljpf131oYtGJ5-UM8LVfL2029qvP-4MsjmdBmF9eHEsM9KgPTZyV4-AHSeL1T4E_Ggd76g2nku-q-OJ6NHvemR-PY3Y2dBoz5SD9mKRndPXzZjzBYpfk2B6vXpf1PaTbhXXdYILEeYZ-TOlg0uFYbxFUY6rW2xnkSf4heEpod0NsV2o8Yku-wveXwiQVW_qvgTegm_BfAyp-Yl0z98ZTqwomtHPVCGN4mnm7rAPKpiUCHmMkT0oE6yu9bYh9CNAyKX8V5dVvxPpMcqJX6S1t_GJbGNY7m-XlsPubNo2sPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگداشت رهبر شهید به میزبانی اهالی رسانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/452784" target="_blank">📅 22:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452783">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجار کنترل‌شده در جهرم
🔹
سپاه استان فارس: انهدام تعدادی بمب عمل‌نکرده از فردا تا آخر هفته در ساعت ۷صبح تا ۱۲ ظهر انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/452783" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452782">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d0014135.mp4?token=a1EcBeIdiYSYwKuQQz1j6Ma22zcGVqJjvUv7_xFFvgPUEqCUo9WUobP6E9hNoPuL7QCOmtMloC1GZG7cQDJP_Dy13bCnd5qAVanI5rETDKDl-23wBOb_tnSDjwep2-mqFmt9mROj5AX_x7AskImZ8gYJFp4jP8mxV3ihJlog2LBsuUhH3_zV9vAl4AmSjTvRmzSdpHfgR6Nzigo61Foub6SM1TRtq-iXG4emZjncd9rgz5D84M3YFXV-FZWLxIXNyeVs7MgMVDkZweZ2A09WM1XFKcLt12mZ7vLKk59cne6VAm0tJrwFpygX0B0-sZXivAautSXykKBiC22lKUQxNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d0014135.mp4?token=a1EcBeIdiYSYwKuQQz1j6Ma22zcGVqJjvUv7_xFFvgPUEqCUo9WUobP6E9hNoPuL7QCOmtMloC1GZG7cQDJP_Dy13bCnd5qAVanI5rETDKDl-23wBOb_tnSDjwep2-mqFmt9mROj5AX_x7AskImZ8gYJFp4jP8mxV3ihJlog2LBsuUhH3_zV9vAl4AmSjTvRmzSdpHfgR6Nzigo61Foub6SM1TRtq-iXG4emZjncd9rgz5D84M3YFXV-FZWLxIXNyeVs7MgMVDkZweZ2A09WM1XFKcLt12mZ7vLKk59cne6VAm0tJrwFpygX0B0-sZXivAautSXykKBiC22lKUQxNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت ده‌نمکی از دل‌نازکی اکبر عبدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/452782" target="_blank">📅 22:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452781">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b05e30d2.mp4?token=UDYjKxsXdKQvT_cdhSHHLRl9AqWyk0Dp2sSM6fk92NFEWJXQzjzeCrMjFH_kd7zPKs9JxlL2IauF9kjpfSa5dWULXI0RezKSxpQcFyjd_RwFDN8vX76vKQ-AW4zIlcDlkj2ZqO27CAoJWSIuAqs6K2FT8xtFzu_wKpU6fZB0POsRtmcnxD-fowFU_JkO_KCr5HhaSBvyaDw-PpFNhzjMufALEMTpl8AKA0fLdeOzwhNUt6YoBJYgYzfZw8xJVsbjEyP4mPWaEjiFFpBuLXbpqebPDLXphLPlHNbjOhB1yR75AFGNcoDR_ulIWcV-xateC0jKYugrCRAxe6tVHucp4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b05e30d2.mp4?token=UDYjKxsXdKQvT_cdhSHHLRl9AqWyk0Dp2sSM6fk92NFEWJXQzjzeCrMjFH_kd7zPKs9JxlL2IauF9kjpfSa5dWULXI0RezKSxpQcFyjd_RwFDN8vX76vKQ-AW4zIlcDlkj2ZqO27CAoJWSIuAqs6K2FT8xtFzu_wKpU6fZB0POsRtmcnxD-fowFU_JkO_KCr5HhaSBvyaDw-PpFNhzjMufALEMTpl8AKA0fLdeOzwhNUt6YoBJYgYzfZw8xJVsbjEyP4mPWaEjiFFpBuLXbpqebPDLXphLPlHNbjOhB1yR75AFGNcoDR_ulIWcV-xateC0jKYugrCRAxe6tVHucp4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی صنعت آب: هنوز در تهران، کرج، مشهد، اراک و ساوه نیاز به مدیریت مصرف داریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/452781" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452774">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKFl1ngN3NeoDk55unFewe-WVS5BbaiLU81THekcFPJUTltbDDP4fIbjuBtE5lkF4aiKRKGxiBqvfJFgCiruTpwt7H686zaItihbctgcPXooPygH3ehuyQ7QuCn-RaUfVJkKW_REwvBB36a8xlUauVL0Wq8FK9pZrYw1yZepn3G8elS76EHIxTl8QpLBaW9RCUzDbJmtdacgT1vdxiz-M_qt7kLC6qsTpa-kIMKwdh0ScBgnnplGeq0FEFmdS8i6gE5MrLs4hYnz6QFZ5OsjZBP-KsnrVkgMU-Lb_smXnrPVOiZrfvXsBlOHgfzHmkQm0l6CHyXtTn1b9yPhUvHhiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOoUE28OYop0Yo5W_qJ_pEO4lNBCrAIeuMLVHT8cqdRazye0P-DFCJJ99EGFTD20KG76OgAYNm0O6HcEYm7XdfHDkH-sNTdcXxphYIbVyhXBZLzMfcbWE0DQ_NVScc23g6n8xQ9HUpbmoU1vtq11eC8lyzLwrUZYGFdPdBSS9pm-IbzJs_WLARaRK_ro8Cqg2xFDoGW6w0qbalqD69oXxpjkdziwWYhUsuU2-xd0-UfAyuR4HwFosHA83En9c0yQMXIjfhK9M80SJGAOtEy5jK2uFCLOtnetJtOaJW1Wy_dTZ67IdgUKJLaGYI4L0ToqhkljT5z2JXPVg25EqDeLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wf5KkCbp5OCyCr0f-QyV_HFviNk0yvnU6TxTftTmROeJl01DCJs70fKmC-mr6j8w37zmgNXfWKrL0gfMV-ZE-h2M7U4KY_jQZOF-oeublx6gZMbImLlIBH9xqhKAUmaCKcQh6Xs4aK49jHO0hLRFkAJrj4jNI2fJYFGH3iMbYQp8cIQB9-i7Mu1g9nKo0ZYDDqB_igtX_caJqnEhYG783o8trIj9XnkTaHOKJXVCqhFjDV-MGL0fklUaL-eOpsqCmaLj6JIA7q8oG7rnpbo52BJ-Qdp0XaWtINJm7j2uWu-C7rirHp1MXv_SSmG2CPQtyoyLP4HvMeRnyUoT1QmWLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYzM5XEWJU_PZ6WligVMI-eAyg0_YSXEoWcvowGCGI1VNJMQRzoi4APQZm06qHmWK_oKkEaECDEfnVPGEQE3Bov-W-g_AD1fhgULly7LGeeVs1-AA5Ku1RQk_dDD8ygbS5MYMZqM5grvJHCuKJUeeDpqEaFSnkLv1n0zWZh8WxyfhB3IpV7cCxuLEC0znNBpcMz1AFEXnmi4R8iiTIZ-FRKcxtYdakA__5uAgxii2VvhiFNw94HIbcWRUxYg5wpWfgT19yk5EuFBHg3JiU6BcbWz824a5balvSNIBuu2Liy5mkDBsnpOMfTuF_68BgjUqsXqZE4-nfIV-AWppNVygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rF_ir7IV0t0fO-i96H4hoJ45jW-4Kd_rh8Fne0tw0gePxfqfb91SxunMk76f5TUoMSXKt0wdHzFUirMg9GcYzPvl_gexe6mRnynuJMYvN9dp7nIbLZSQRFCCKlHG98cNasTkv9JtgCfVzeSgl5TvqWhKbC5YVb7pVV1mW99qokNS1d1iYEAPBkLQPKhnPOWWbBwzXmFbDGzIDch8lNqRTuyr-oT3Em54vpK6CCNN0ocSPLQal_3FIwiFF5ParGN4U4gnXLXA9ojCO8j0fYxYxuXBH2r7IOacGCsl89Db6rWDTLToy8RqQWI8j7bc5-ZmMiw5-R4HiAyPmRtfulTSnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGgzRIOyTnonIQetxYBUq8ULalhUN2alfmaXvQlpsc__YGjrpanBtNbrGjfee_J5DMh-YGAVFhgtUTFJZ9TOC91hzxmW7ivMHlDZWxwgpT0qFjJwmMQPSmPczJ3JVlQb7aXYmhvtMcPv-f9MPJRjsaFYudoDzVIX2DIi6F_icL6tCvEL0S3gVACPbw0rxZVFMokqka89RwMquPQ-Ebp5OKe2bkTIRe1JkJ2cRgrsC7djx8Yr-DCmy00PbkqNKRFZckIxiutXbbBDmFSyJ-tHzyjoor_3nyBH3jE1H9TWsWb71IvSsBldyVNA66Z4LF6LKa-BQXOTyrvsoHA5paJiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZxlShdztL7lY0j4A9hh--F8DVnYrdrmQ99_GkTdlNr0lTAKs3Lsa3foGuOViQBTYTYxEWdzgzAh3lbBwTeu5i37GMrGbj9JJrE9Xzu_FOn8YR6NmasYoeNlA-LcB_KSQJM9OvEz84IGy_axNfuNremXgffDU1sFSg6fPYtDyS0c5fmugf8SJPS46N5tnF3oNYGX5VttBtnwj7K438EN7U8TM6hQSzFosUalNfzKt0m5xY0WeWPDS8FhnxhmtWd-j8KclumyWLLRWkz0EToEOxzkt6eno8srEYkRaiwkEyWGh7RMeaYHFoykpsq2fvqSxU5W0LjgrIZu7hSg9KfYkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میزبانی گرم عراقی‌ها از زائران ایرانی در مرز منذریه
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/452774" target="_blank">📅 21:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452773">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یمن ۳ نفتکش سعودی را هدف قرار داد
🔹
المیادین: نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
🔹
تعداد کشتی‌های عربستانی که از دوشنبه گذشته تا امروز برگشت داده شده‌اند به ۱۶ کشتی رسیده است.
🔹
این منبع همچنین خبر داده که  از زمان آغاز محاصره یمن، تاکنون هیچ نفتکش سعودی از باب‌المندب عبور نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/452773" target="_blank">📅 21:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452772">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec381246f.mp4?token=f3YRH6vNBU7g_FdOewCu6NDxaukCFIb7c94Pp7vtz5Pn3zBEtf09gs_2snpTdRmFHPqGO5sdqChSgCY8eAl1WmT4Ru6cJ3UmnEuMEy4WY_fS87erkqMiwQ97dl9i5TotFg1QODjRcVAjnr7npIO-HoTltxuitN7SWrU_C8bv-dlRmQ2VYfV2As_vV2SVCFx4SzOsuJmnIvXA0f_GzRsQGKtJQ1oW9o9FifKU0uQ001gY-aWA9joU444FzJcFUJZuSGncXd13EcsStO6uq98Doj-UigT45RRQEHuvMv0yFH-fJOpGUUpA97xXpu5z18FvNoN8SpY_oo6TlP-o49yjXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec381246f.mp4?token=f3YRH6vNBU7g_FdOewCu6NDxaukCFIb7c94Pp7vtz5Pn3zBEtf09gs_2snpTdRmFHPqGO5sdqChSgCY8eAl1WmT4Ru6cJ3UmnEuMEy4WY_fS87erkqMiwQ97dl9i5TotFg1QODjRcVAjnr7npIO-HoTltxuitN7SWrU_C8bv-dlRmQ2VYfV2As_vV2SVCFx4SzOsuJmnIvXA0f_GzRsQGKtJQ1oW9o9FifKU0uQ001gY-aWA9joU444FzJcFUJZuSGncXd13EcsStO6uq98Doj-UigT45RRQEHuvMv0yFH-fJOpGUUpA97xXpu5z18FvNoN8SpY_oo6TlP-o49yjXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بجنورد بدون خستگی در میدان حاضر می‌شوند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/452772" target="_blank">📅 21:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a84e97bfb4.mp4?token=AzCH-7ewIsdT00T-r9xsaMxSfghu9UQ-6otkvbnl0ofUIBu2kL8upgO3e9yUOG5LvdfMq0bbBXkHl_I9TXsP-R6PHxVz-gyZbddlQzAheEtApYzkTD8oa0G84ww01IoqexGMGxVoSFQpCwI9QnuXZqsH6Y2ckJyMReGWXpLFYol6OAG1CXo2-24QESR7NdMRn1C1yKldlsuWPW44Dg3SWx2ce5ai2ZqIztLf9hMZ_0ftBJgSKfowqSM_mxuocrXcBi-iLyfvn03DSvc5CP7OYA1Hu6BON1xqFgqnrJLeeVbUFIiwX4beJZC_jxZQJGacq58TKw-h270LFzvbXYLcCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a84e97bfb4.mp4?token=AzCH-7ewIsdT00T-r9xsaMxSfghu9UQ-6otkvbnl0ofUIBu2kL8upgO3e9yUOG5LvdfMq0bbBXkHl_I9TXsP-R6PHxVz-gyZbddlQzAheEtApYzkTD8oa0G84ww01IoqexGMGxVoSFQpCwI9QnuXZqsH6Y2ckJyMReGWXpLFYol6OAG1CXo2-24QESR7NdMRn1C1yKldlsuWPW44Dg3SWx2ce5ai2ZqIztLf9hMZ_0ftBJgSKfowqSM_mxuocrXcBi-iLyfvn03DSvc5CP7OYA1Hu6BON1xqFgqnrJLeeVbUFIiwX4beJZC_jxZQJGacq58TKw-h270LFzvbXYLcCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک شب به‌یادماندنی برای بچه‌ها؛ دعوت احسان مهدی به «سر سفره خدا» در محرم شهر
اگر به دنبال یک برنامه متفاوت برای فرزندانتان هستید، «محرم شهر» هر شب تا اربعین در میدان آزادی با بخش‌های متنوع و ویژه کودکان و خانواده‌ها میزبان شهروندان است.
@Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/452771" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452770">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43066ca80b.mp4?token=qFkTmzizy2jfWAlF12trIq_SuxRW9tofARpAUYpwbqdQCvGEapN-X6P2aBZ1CSLeV7EKg_0XMfph2lWt1MbP1q-jFOk7YJAx9j9zzV8FLuyWQc1EVsBy6nDmMmdu-CiuVKZ_1EOP8ou21_bo-7MgOlTXo15LgKHKKwuncBJPaeFrWfz37G5oj1AI9lgmxRIXdE_OI5_f_WedDlvJPuf8Bbai2kiuvtCzLF4ZjUIYzUYIU8FeHOfOcRbv2z8y5-9Vf4t8jww4j2UBXaL7oKyxVCft7hCYnF0nMoX87HRXM_9uqKyNA8KbfEtS8_7zxOekadtwl3FTzK8tQADmMHlmB1O00HHzP1Xb02QPVtKIgsqHICKcU0EjWG2NQ-NpAC8E6nMjcKZdjYSSdSxeoKICOhTM9ytexbJ5S_j5hRbOKaxbAWJxZHhvhHPcrZHrqLugrLCMKlv80E4Enh60vcM53iACimR_rNI49PugIxEjoZSfv1G_7Y4tKfHbJJN1pB0yMS5QdaGBrUq24h1y4YCOXZ5roih0dWimdhUKm0AB2F4jLx4F0YaOKZ1OOyfvO6fPealuP65LeNIebPIfYCJWvTnDoiROVm6j90RiAgkJ09TNZukaQuVHq8tB9DM6o7d4gkMgdxfJeW85eVwynyk_tlKcfdvY40OStP_db8TRNJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43066ca80b.mp4?token=qFkTmzizy2jfWAlF12trIq_SuxRW9tofARpAUYpwbqdQCvGEapN-X6P2aBZ1CSLeV7EKg_0XMfph2lWt1MbP1q-jFOk7YJAx9j9zzV8FLuyWQc1EVsBy6nDmMmdu-CiuVKZ_1EOP8ou21_bo-7MgOlTXo15LgKHKKwuncBJPaeFrWfz37G5oj1AI9lgmxRIXdE_OI5_f_WedDlvJPuf8Bbai2kiuvtCzLF4ZjUIYzUYIU8FeHOfOcRbv2z8y5-9Vf4t8jww4j2UBXaL7oKyxVCft7hCYnF0nMoX87HRXM_9uqKyNA8KbfEtS8_7zxOekadtwl3FTzK8tQADmMHlmB1O00HHzP1Xb02QPVtKIgsqHICKcU0EjWG2NQ-NpAC8E6nMjcKZdjYSSdSxeoKICOhTM9ytexbJ5S_j5hRbOKaxbAWJxZHhvhHPcrZHrqLugrLCMKlv80E4Enh60vcM53iACimR_rNI49PugIxEjoZSfv1G_7Y4tKfHbJJN1pB0yMS5QdaGBrUq24h1y4YCOXZ5roih0dWimdhUKm0AB2F4jLx4F0YaOKZ1OOyfvO6fPealuP65LeNIebPIfYCJWvTnDoiROVm6j90RiAgkJ09TNZukaQuVHq8tB9DM6o7d4gkMgdxfJeW85eVwynyk_tlKcfdvY40OStP_db8TRNJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
اربعین، روایت همدلی و خدمت است.
⭐️
موکب بانک شهر با حضور کارکنان خود در مرزهای کشور، افتخار خدمت‌رسانی به زائران حضرت اباعبدالله الحسین(ع) را دارد و با ارائه خدمات، همراه آنان در این مسیر نورانی است</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/452770" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/452769" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGwZhNVGXxA3OsuIBPNi3pDP9jou3EiX2UInTvgZq0phQucichTeASy8o17FGHTCiPHzRPHrT2CQbVryt0sGuByIYgOR7iuUERzz7HGCtJ3G0vao4h3h3W08WO3BCfiQ5HB5lQlzc970I01NFlKes_KnVqBEgv0skSoRjeM4N0pmDYPhcZSThfdwB3yOR14ZbpEn7WAzP7_fJxUPzYq6u3c9z-tb6qR4p927eh491-y3Yk8OjyQIMBlrB_T0XDDOA9LIC17ABw9-hWdGf4PZXgUCUXtQEiWIjBFWGIJW9_WE8ISH6vxVgdwKrMamkR7odjD8DWbmh80JGPnmVSt7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: اقدام «فرصت‌طلبِ مستقر در اوکراین» بی‌پاسخ نخواهند ماند
🔹
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و یک ملوان را کشته است. این اقدامی است که به‌وضوح منشور سازمان ملل را نقض می‌کند و به تحریک اسرائیل انجام شده تا اروپا را به جنگ آن بکشاند. @Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/452768" target="_blank">📅 21:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452767">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S47atVLXKZ0drR275DEvQQfsnjmw79eSYpvWnNb85WCGF-g7ht-TvuSBxhaJ5Kq8uYafYhQ6cWotzXZrp7rCVJRXoU8Q6-w_xqGkHgohbvQgSaT1jxmvQv8kRBJIW3o28VmPmgNCZKXjEq8kJ5oax8oTd2cwXuyoFXWdhO8wwXqbGwSQArajRA3Zp8dLI1vtIw2dVZiJ008lb3vER7VDiXCxJ193ytsuLs08hUNYKx1spKAEyRgONZw47xsRdLbyfa2B2jd2zvPLtFsl47_bk8C1oViv3kfESs8HDk1J9ErV5h4xztI9uEHlP2CRNdN7QDVn0S6ULyOQQfVJaMeWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۸ ماینر از یک کارگاه صنعتی در تبریز
🔹
شرکت برق تبریز: از یک کارگاه صنعتی، ۳۸ دستگاه غیرمجاز استخراج رمزارز کشف شد؛ هر ماینر به‌طور متوسط معادل برق ۱۰ واحد مسکونی را مصرف می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/452767" target="_blank">📅 21:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452762">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D88axhyG-2034I3oqSK-x7OFAQxeltqN5r-38RVVVtOr_ouUG_OhucKkwfqsJtnHGYshZ-zBB4IYQ95CDuMtIj1wW6u117k-6J4qndisbDRd4AtF-IGsXfir3HCz59I_Sfij9TZCKs4Dg0IFR9bY1H2xL8iqwI3Wno2TZT6sIZspT_cHXLyr9xJ8uXw5GfLbpqPHBtG8qLC2odt1JTqbtQTGZ4p4b83gaQJCh21N5QmmkveKEJpUGupyFuUsX4caJNTmFiapEiNY5J0awpOUgQ0_EhGtnsqvtMshTtxa1UCaHLu8Bq_i903uVjYURBe0yUZw6OGbhfe9cjQOrNQrsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3I7gygl4fF-cKs1K5mK_ESX70wBaZZUGMDVT2Ie8tZUgsJEzFql28OfhE9xNkVO_KLsiLVaEjat5ghAnLOcZ8lsFcA386Xyli3fgDZ_NPJg2LKpm2mpAZjykz8E63Ctdtn-GR4GFWyJ1gdeQFen4vCWrTNFR_bbeVnvJtJYi2cjrq1RE7dIS_5u7vz_gORojhG0FYY0lj1DWou9Hvk386hzF2pUhcxAbCQuyvbthKXCHm5c4xtOee2IvExhWlWBbS_Mg-45IeFpqZxKZwGC7WzVijYdYfBQrw958fjz8UBfLqMVPY6sSK3bcoOJkgvIsg-VmZB4ihHWiRrGUx3MQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgvK7iJMJ3zLpKhCPWhdR4uyY4Po-DfCqPuFXhKt_Y_n0ECa5fBh0m7l_r33RSvW0URjyUZWndwsBIQ_UJHiR0BgxytGYN4maqiRr0Dhd2tBKIM69pBpRpQs9gidT7ztIPlMc-WE2sCXwvFtsmqALCgidC-AbRmXkwUaUFmuWhk5rXrCFTyK4lQ5xceUYa26qoQw6LCEfwkMtjKweNW5RF1695vn_13Vd77uR81f4zWtxzHSf7rLwj1bFD_bc-CVZUUBgcU7EDgF4974-4otk4UdzH6PM-u6Hg9cDoUUCaGfC0Ky_3AzwXC8HMuXukR5ZxLuJY1jqKuOs5xNuEvTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYJUXE-sbEVTZL4C1uDBJGyxriViHVUAPi343mv9llckwREn5a1Lk3macD0yysPF6_ux49FvSEcALTgC_X5yjRLUzvN1nd6uXsQQbpphCX8Q-Nts6YsXTEXGzGXwZsBeyHvpAR9hgMn1ZpPOChxxpB6hpbwARKBgn3lAW46Iy28E7u4ZeIlqmgFqbiGA9PSOlVhT-qERB0AKIUbeKks1HDfQzn66rTjx8mXlXPlBQTYXypyWAzItgskVdVJwH18dNy-HUMPo7cd5gxqE7NJkYv1nXF3odgg_hIcH-u0byKCWORX1VGBO0VMxr3Ykm4_LfxOGlarmY7qP9bDkUPPriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTNlMACFXxq3timMb72AD61om9hbTKSSsMPL8mj-ZIQdwO-wHbgT9nsbDI5gSvlx-0XMICJ5hQcN3ROfh2JwO79wfrExwL3mtr7nMEo95-e3Jbp_J2On0TEQ19Ywd1p-C_OTrmCPromTkxFkyojXogO7ihCjM3jXWqQNRcyGUsnJGoW1OqP6QrVQKa-tgRnkmEbZ-H6xCyaejsa_5jZhUzse4UcnCYrn0xV3AvaUyvZ23iWRJ5NTPKr3PzSP_uALO6Hsdr5fhrjGe6Jqu_vs8iowdqTqduUSaOMVg4RsHm06XRJFIvroMxynWTEt-il63bQZmQD1A0kckx7eb3yk2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
تصاویری از سرنگونی پهپاد «بیرقدار» متعلق به نیروهای سعودی در استان «الجوف» یمن
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/452762" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPNm257xmRoksmKI1oeZIutg4Bj3xtsSiEWG-sMaZ0cJYcNmfElNYDrDMq6ZDyMdP-aoNRHa9B7rUYcVSlFl76XdsVEb6V44lDaYHtkSZIYCZLMJuQfn92pwXZr-KBQf1IdvqZfHfp7zB-o1AFVV9ypNYOCt3SQOEek0Ft19hkaiIA2GDUqdBKo5ykHHKRSoCwVqUBHnC8wkctbGYedAdwSh_YUO8Bhml1FLNMeFu1KHfRmO7xGpiBGNmfEWro_nZadRewQ_IsVei9Kkmwm364xoIUHjpT6zV5NBW9bMPFRnl7ChxwfEUbWcYzpzpggE16_BKQo2FnR7fKjPh5QohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدجلال سورپرایز قلعه‌نویی برای نیمکت تیم ملی؟
⚽️
شنیده‌ها حاکی از آن است که سرمربی تیم ملی بی‌میل نیست سیدجلال حسینی را به جمع اعضای کادر فنی خود برای جام ملت‌های ۲۰۲۷ اضافه کند.
⚽️
گفته می‌شود در روزهای اخیر نیز گفت‌وگوهایی در این خصوص انجام شده و طرفین درباره این موضوع تبادل نظر کرده‌اند.
⚽️
بااین‌حال، باید دید در ادامه این مذاکرات به نتیجه خواهد رسید و حسینی در نهایت به کادر فنی تیم ملی اضافه می‌شود یا خیر.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/452761" target="_blank">📅 21:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452759">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np_yh6oM6oGLxALhdktBLbFZX3PVXy_3iMnp9KAMXskMsZjtpFcBy_7KPlw8MZkc1N3IOSARVXumtrgQip2oUZkk-8Z6OWbaaAgDOWYey5jtGMU_uvFapuHmMXtEDYXDBZjnT6VhY6A76e3ggY9Sx7fY12ETF4sWKm8JsywofyuK97Rp7ESmUggaCLkh0NaULbkcHuX99HVRerubOzX7B0ZQmZBdWRjC2I4ojLoo14wzn8DvIoYaQbW_y5pSz8-zvCs2Lz78wi2hK7kTympjgZYgeMWCc1k19AEjzsQRmDpQjxWpxSjJIcqLAtq0uteGxg8Df-OZdKScfNECXdY_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل پژمان جمشیدی: موکلم از اتهام تجاوز تبرئه شد
🔹
وکیل جمشیدی در گفت‌وگو با فارس: رای نهایی در پروندۀ پژمان جمشیدی اعلام شده و او از اتهام تجاوز به عنف و اتهام زنا تبرئه شده است.
🔹
جمشیدی تنها در خصوص اتهام رابطه نامشروع (رابطه غیرزنا) به تحمل ۹۹ ضربه شلاق محکوم شده است.
🔹
به این حکم هم اعتراض خواهیم کرد زیرا معتقدیم در صورت احراز چنین اتهامی، مطابق قانون باید درباره هر ۲ طرف رابطه حکم صادر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/452759" target="_blank">📅 21:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452758">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6ce6e816.mp4?token=g9T4LWELTSN0T27bcDDPKD7mxWxbtfDqyHFXbjGp0iQTDAlrwEcz_Lc8cwGYt5RGQn4YOGGEESht1y949P2AK7Z_l8i-ZQA7r2TKEAuSE0jZzYo6XjUKabgAFVlTOwl28Gycnc3xmlkyajpucSFVFg7B3AdKW9llWKPL70mit5DuOdeaCKBFuWbkt9WuIzMH3NAAaQsUukZMiaokLvqUuYVcI87BmOlt6Q6-EapAR32TggL5myEMreh-WdFIAyUHBltNi6TOvU80BUPrnBSXPSlIszwcxM9ACuHznCkU9qydhmXrsVfJjiZ4FibCy4tJTYDYXeFVK39Qk63zgc1wLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6ce6e816.mp4?token=g9T4LWELTSN0T27bcDDPKD7mxWxbtfDqyHFXbjGp0iQTDAlrwEcz_Lc8cwGYt5RGQn4YOGGEESht1y949P2AK7Z_l8i-ZQA7r2TKEAuSE0jZzYo6XjUKabgAFVlTOwl28Gycnc3xmlkyajpucSFVFg7B3AdKW9llWKPL70mit5DuOdeaCKBFuWbkt9WuIzMH3NAAaQsUukZMiaokLvqUuYVcI87BmOlt6Q6-EapAR32TggL5myEMreh-WdFIAyUHBltNi6TOvU80BUPrnBSXPSlIszwcxM9ACuHznCkU9qydhmXrsVfJjiZ4FibCy4tJTYDYXeFVK39Qk63zgc1wLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رواق دارالذکر به‌روی زائران آغوش گشود
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/452758" target="_blank">📅 21:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452757">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB1qZMW8kSi1Pjvbau6URFHGodFEwLPHtl9slNgjpHLKQZTLSf7-brZnGZwHR_khhw3fzpfrbLqbKqfLVa-FcsYUiXLSWPV7fckwt3JeLL0lPi4zUJYfuA8KjeYD7UqGlepW863qEhXUTzp2z2S-AHIGI6I79LY7vjSNJWIv7t2WCQBram54ob5SDDkf6H-c9IAooUGNuJB5vGWyBDaFigjeVc5dWzpbVEC1eF1Oj0Lwx4K6l8SqDRThYZf5UJJrSvaX5S82yCVd3k1cRHRQEE9j5J7LI3LrjKF6d1bhBhz_actb2siDQ7xizBKZ4Hly-uel1TqCtcvtG8I-pG3LLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
لطفا عدم واریز وجه کالابرگ برای کسبه را پیگیری کنید. خیلی از فروشگاه‌ها کالابرگ را غیرفعال کردند، ما هم به زور ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/452757" target="_blank">📅 21:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سپاه: عملیات مرصاد درس بزرگی به خائنین داد که هوس هرگونه تجاوز را از سر بیرون کنند
🔹
سپاه پاسداران در بیانیه‌ای به مناسبت سالروز عملیات مرصاد: در پنجم مرداد سال ۱۳۶۷، ملت ایران با تارومار کردن منافقین فریب‌خورده، درس بزرگی به خائنین به ملت و میهن اسلامی داد که تا همیشه هوس هرگونه تجاوز را از سر بیرون کنند.
🔹
منافقین همواره به‌عنوان پیاده نظام و ستون پنجم دشمنان ایران و ایرانی عمل کرده و از هیچ خیانتی فروگزار نکرده و در فتنه‌های کور سال‌های اخیر از جمله کودتای نافرجام ۱۸ و ۱۹ دی ماه ۱۴۰۴ نقش موثر و پر رنگی داشته است.
🔹
در  شرایط کنونی دشمنان انقلاب تمامی ظرفیت‌های خود را برای تسلیم ملت ایران ازجمله این گروهک جنایت پیشه را به میدان آورده است.
🔹
بی تردید هوشیاری، هوشمندی و بصیرت مردم مبعوث شده در حفظ وحدت و یکپارچگی ملی، اقتدار و صلابت کشور را حفظ و پروژه خدعه و نیرنگ جبهه نفاق و معاند را ابتر خواهد گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/452755" target="_blank">📅 20:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452754">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRvecIXOYPtGKjBWRcI6dax-NyKHPEPomM4Tt6QKNTYAsQ8DT9RKOCX8ot7agaestIVC_g_4lcoIA7lXwU8GVGS9x98yGtnNSKzQJJjMWL3vmzq4Jxo8ui0uJHc4qOj2HNyBbPI_lJFjLyE8UzEwx3Q5CY7ng0jSu27_iUAApUWpFD-2YLDyN0MRnwUBk-40DvDN1Zw7tyuU1TRNETRTGMZsVB6GCO4bOqxu09EJioQO34FxTEjXF7r2BbSiOryMJCAJfc50g6i9bi4J-dSyC-vsPbi_ojqLIE_P_7fB-q0KRN8oIb4VlpnjkTMVYKaeXfmN4w6ovW-NnlRjlSeiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدا بر روح ملکوتی سیّدالشّهدای حزب‌الله سیّدحسن نصرالله و همه‌ی فرماندهان سَلَف مقاومت و یاران شهیدش</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/452754" target="_blank">📅 20:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452753">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a982009c3.mp4?token=CjIJVqVnYLpRSSneyUZ9iYv7pTRFsBLWtZNyXpUVNR73qiKCOPkiHzYL0hdCvcjVl-OHjOI8VvyVGUj3X1uh9KcZ_MjfYVamjeUg0XwI1N0V5IqCAYhsTWUznOHMfumJrwXcRrQuuH-uPC83cBkInhB5mi8AS4xJKeocmQMUahkW56QNeJh1DwT4VXaeRrHf23hZ8U-CSoM7X6p4jLNzdRDTzGkcJJUKJ4j-fkyI_GEFGXjQN__8tbE8aracjiiA4Ya7Mf3QcIZB5KaY8qdKzpQTzYjXrXshtGxgEujMgK6n2ms7oHoVi8imkxKoFEQdHiRJhtYUmmRAiw-1n6oLMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a982009c3.mp4?token=CjIJVqVnYLpRSSneyUZ9iYv7pTRFsBLWtZNyXpUVNR73qiKCOPkiHzYL0hdCvcjVl-OHjOI8VvyVGUj3X1uh9KcZ_MjfYVamjeUg0XwI1N0V5IqCAYhsTWUznOHMfumJrwXcRrQuuH-uPC83cBkInhB5mi8AS4xJKeocmQMUahkW56QNeJh1DwT4VXaeRrHf23hZ8U-CSoM7X6p4jLNzdRDTzGkcJJUKJ4j-fkyI_GEFGXjQN__8tbE8aracjiiA4Ya7Mf3QcIZB5KaY8qdKzpQTzYjXrXshtGxgEujMgK6n2ms7oHoVi8imkxKoFEQdHiRJhtYUmmRAiw-1n6oLMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تمامی کنار گذر پل‌های حملهٔ آمریکا به هرمزگان آسفالت شد
🔹
مدیرکل راهداری هرمزگان: همۀ ۹ پلی که در حملۀ آمریکا به هرمزگان موردحمله قرار گرفتند از ساعات اول از طریق کنارگذرها فعال شدند که اکنون این کنارگذرها آسفالت شده است.
🔹
کار بازسازی پل‌ها نیز در تمامی نقاط آغاز شده و در کم‌ترین زمان ممکن انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/452753" target="_blank">📅 20:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452752">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رهبر انقلاب: جهاد شهدا، مقاومت اسلامی را به درختی تنومند تبدیل کرده و عزت لبنان را رقم زده‌ است
🔹
صلوات و رحمت خدای متعال بر شهدا و مجروحین و خانواده‌های صبور آنان، مهاجران فی‌سبیل‌الله که تحمّل مصائب را بر خود هموار کردند. سلام خدا بر روح ملکوتی سیّدالشّهدای…</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/452752" target="_blank">📅 20:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452749">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeV4auuCACVDFGSDoU4xPUZbl9VG4EIAHmzgQ8esdN1US46rAWrnANDhVyJbY27Q7p8DM3qaUJ9rn2wZo2VYzCTcZk5Qcx_a_Tp7MKo9XpPAHtqIHKc6zWdE4HDMg1T_owg6q6K1wYOVE10pIeYglh7rTxLsvHAF7RhWHkxFvRkVGJhFG0hqmA-leOOMJCrmsNSFIyJPumQOLVpUz47-Ufg8_j3016kbKlw6aQbBMr_XNxNARCC520YeJk1OQGgov3gdQgCLFn_pZpRoltcJ7GNnMocdTyqF7PEr2LT6wXqPSn52mTi-DkvMHT5scq1ADMfet3eYmqKsDs0dIfyHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5d6_ycwSfqZ3n2_UMBj2wA7X9sy1IXEgMCsjQ_JNWWTa4FQqz7Z-TTuvTsC7bvE5dwN-0USeaHSZierwxwwspX-hzi002APaQB1SRp5ZCVONZZrgEhWaiEVhEme-1M-jz1GpD90kS0YQxsLGNn7sggJBdFDdigieuoMWKvtlFcr-gfdIbUMRJXJsaBHKndLrA_RbFuchp7_fw-3FS1wx4D39Ftn-q7KCCnbMWc8mRzwqYK3OpaW_cMklq41s6_-SwW5EbdfgKU6dqto-lyIIb0z0ISMCaQB4JJHe6dm8j3P3kaND2U2kvnOUACSWeWqJsMXYHNctuvtfuQ9N5tvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-L0FfwHBqe9KwEzTf_wLBxx-no9fBAq6qoDoNT4vtye4_ozXGO3IOzGQ5UWdHlFgz4PYH1Aa6w6e5EvjSzJG-Zbrn6XzpKEo4TBd7JOOpUcjDwdGSeE1IpokzHqBh49AVIZhORb-vzvIifboL1sRtWX6RUpEyjD0E0yUCSLViPgRFzWuZ6m3I0TpaVtWhx6M8fRBGpoPcbrOq0mpwKSWNvi2NHpbdyQw8qUgq1RQuW1CFNbHk75tvQg9XnUVx5PtFdp9VeCDHLioN9zTFGuEs86Tv8slA5lTea8LrnI6yT5Xn1hdVsTKsDpGhWWQDAS-nbEMcseO4sdrokgGCxGLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
۸۳ درصد جوانان آمریکایی خواهان اتمام فوری جنگ با ایران
🔹
سی‌بی‌اس‌نیوز در یک نظرسنجی نظرات عموم مردم آمریکا دربارۀ جنگ با ایران را بررسی کرده است.
طبق آمار منتشرشده از این نظرسنجی:
🔹
۸۳ درصد جوانان ۱۸ تا ۲۹ سالۀ آمریکایی خواهان پایان فوری جنگ با ایران هستند.
🔹
۷۶ درصد مردم آمریکا فکر می‌کنند جنگ با ایران سخت‌تر چیزی بوده که دولت ترامپ قبل از جنگ پیش‌بینی کرده است.
🔹
۶۰ درصد مردم آمریکا معتقدند ترامپ مسائل مربوط به جنگ با ایران را بهتر از چیزی که واقعیت دارد نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/452749" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452748">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFVSOreiiI35ber_Xzj45I4Ua9rI7RTU1BsoG7xZl9DxQG7VN4hksp-OUBipg7JNU0szWXRF_HczdfrupfEzozyUHgJoYkbYt_hXw9PmUAcUwg4VJt4us0Edv7n0INU3GOpXLFUF3IHNIeZCQYyk14ElSKQAcy3US4bAfTIsD_Cz-dkSGSb9rX4quFwrjvi-iJx40soPv8fHyamr_4_yqDyVYKt6yu2tjaDDVfpnoNQ2Enu_fhNRwkS0XBTHP5cMJOkj2srmRGRblzrwaq7_06N5-HnR1NEzqb0N7jzR33WMJsJSvwnxL_Lgm7ewwVZzMFZO3W3NhUCq9DZyUQfGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  رهبر انقلاب: جمهوری اسلامی دفاع از مجاهدان لبنان را به عنوان سیاست راهبردی خود تعیین کرده است
🔹
اکنون که حزب‌الله لبنان به‌عنوان پیش‌گام گروه‌های جهادی در برابر هجوم سَبُعانۀ رژیم صهیونیستی و حامیانش، چون صخره‌ای ستبر ایستاده است، این پایداری پیامی الهام‌بخش…</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/452748" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452747">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌ پاسخ رهبر معظم انقلاب به نامه دبیرکل و رزمندگان حزب‌الله: پایداری در راه مقاومت، نصرت الهی را در پی دارد
🔹
نامه‌ی شما برادران و فرزندانم، رزمندگان مؤمن و شجاع حزب‌الله سرافراز که حامل پیام پایداری و استقامت برای اعتلای کلمة‌‌الله و باورمندی به وعده‌های…</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/452747" target="_blank">📅 20:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452746">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">📝
تا دقایقی دیگر؛ پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/452746" target="_blank">📅 20:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452745">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e2d2a86a3.mp4?token=AcGj2iKieq5mHqodC4-YWplvbvmGNPQQO7PWbjyzSFBRs98LELIWEQ8LT57ikL5nXDop4c8uA8vk4qFdK6zI6b7NtKpCJFAlW-Djo3lCHgr5Tm_QQOUPPkEqWIeJSOBl7gmgWR0gQUpQSQ3GwG2gHKoEuWMhinmmczROLwEevXtDy1K7F8LbZxRCdLMafJ79y02qpQpLKeqKG7YmAVkyXdQ_oA458Kg1N46mI1LReAr875BBglbg_s5ea51uUKeXX8m0-XW46TxdRZaHJZRvZN9MSSrR185UwtBVpIovgTQOk_ANxN7N36dxRPx8cXuNTGak7QkTsr6RqHLSAjoZPiO0I5J8cWNkCPaXwhz4LtByLUO2AbOtcZ_l1BDbkkNYBhn35xYTvojpo2uXUX8I-rhM3wS1SA0lf7Cj7nGQqm_n_biu6ZaS_eqjoK0Lzh74OqXQlXIDtj1LLG10JnIUK3VJTyUhM6R6VgplkOhF_cXIq1Vuq919BuP_MtYd6uOtm67PBja3ywpY5wlbWobkDC3bUpcLiUcPPWds0nIL8yxcLiIukhycmno7ceaUSnN1vi-6ILrTghcdxr3RAwcEmytoC0eJuYbhut2r9HooBN5qYmU1GNtSUFIsQ0qw7Pf0BnM--afz54PuopTNdCqruYnNBn5XKFMF_62m8ltz9JU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e2d2a86a3.mp4?token=AcGj2iKieq5mHqodC4-YWplvbvmGNPQQO7PWbjyzSFBRs98LELIWEQ8LT57ikL5nXDop4c8uA8vk4qFdK6zI6b7NtKpCJFAlW-Djo3lCHgr5Tm_QQOUPPkEqWIeJSOBl7gmgWR0gQUpQSQ3GwG2gHKoEuWMhinmmczROLwEevXtDy1K7F8LbZxRCdLMafJ79y02qpQpLKeqKG7YmAVkyXdQ_oA458Kg1N46mI1LReAr875BBglbg_s5ea51uUKeXX8m0-XW46TxdRZaHJZRvZN9MSSrR185UwtBVpIovgTQOk_ANxN7N36dxRPx8cXuNTGak7QkTsr6RqHLSAjoZPiO0I5J8cWNkCPaXwhz4LtByLUO2AbOtcZ_l1BDbkkNYBhn35xYTvojpo2uXUX8I-rhM3wS1SA0lf7Cj7nGQqm_n_biu6ZaS_eqjoK0Lzh74OqXQlXIDtj1LLG10JnIUK3VJTyUhM6R6VgplkOhF_cXIq1Vuq919BuP_MtYd6uOtm67PBja3ywpY5wlbWobkDC3bUpcLiUcPPWds0nIL8yxcLiIukhycmno7ceaUSnN1vi-6ILrTghcdxr3RAwcEmytoC0eJuYbhut2r9HooBN5qYmU1GNtSUFIsQ0qw7Pf0BnM--afz54PuopTNdCqruYnNBn5XKFMF_62m8ltz9JU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله جوادی آملی: به جایی رسیده‌ایم که ۲ ابرقدرت به ما حمله کرده‌اند و مانده‌اند! این معجزه نیست؟ معجزه حتماً این است که یک سنگ حرف بزند؟
🔸
هیچ فکر می‌کردیم که ما دو ابرقدرت را چُماله کنیم؟ (درهم بکوبیم؟)
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/452745" target="_blank">📅 20:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452744">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jogcMKtqdC2CwwQdiY87fOv7cOHRO56csDZam4xxBczkTwtzfW7xXHJhYougdTAVF5H4wIWCMJ1H1wh3cwsrsmS0uw5wQySePTZeSuxTn-JMMj6GGIa1P01o-g81va5o3YSCYyH52iCRxDguW1EoRt3L2Uiz9qr0K7gXb7q-Yl6Mx3d3EXcU6qx9Km6lx5F4380tAqL3EukuNnIXnX84u9Iq5dEDO8cWq9r1blIjfyPN_0Cq7wcslD_J_CRArg1IWnVYDrEvon2zWIMbig0RaQt1l9Fl7wvcnloeOM-_Td1AgFEN8eSkIq7nLsUzVHZzDTwmLymiD85HBXHuROlY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فتاح: آمریکا نتوانست حس شکست را به مردم ایران تحمیل کند
🔹
رئیس ستاد اجرایی فرمان امام: امروز قدرتمندترین ابرقدرت تاریخ با پیشرفته‌ترین تجهیزات نظامی و تسلیحاتی در برابر جمهوری اسلامی قرار گرفته اما نتوانسته به اهداف خود دست یابد. همین مسئله موجب شکسته‌شدن هیمنۀ آمریکا شده است.
🔹
امروز مردم با وجود مشاهده خرابی‌ها و آسیب‌ها، احساس شکست ندارند و این سرمایه مهمی است که باید حفظ شود.
🔹
هنر جمهوری اسلامی این است که با تکیه بر نیروی انسانی مؤمن و متحد، در برابر قدرت‌های بزرگ ایستادگی کرده است.
🔹
در منطق قرآن نیز پیروزی صرفاً به تجهیزات و امکانات وابسته نیست، بلکه ایمان، صبر و استقامت مؤمنان عامل اصلی نصرت الهی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/452744" target="_blank">📅 20:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452743">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c11c9aaf.mp4?token=pOqc6T_BRZJeRnXtS33O7Z7bvFFzswdGKBg8maCYcZmn-ruDKeShEKSn-sReKiQSuJgp9GOD7z0Blo_E3MJdFsqnsmWMz82TvVikmV2gkgVCQDYz3IuNoMb53dCtNNQgyGqqf9sfyG8HdEbgtR_tqT24Jac6xy9MEiriRe3XKVx8JZ9XKdQr-OXdfD9N-xx2g7GVuWtPtU_EHfW2sOK4KiFrJtn62-p4ZXqbz7vvg2Y4nqokgExz60KpOTV-1OV9ZGI3Wa7DjiDKt69aTprkedphVk72ask7IaA1cvk7OALu37ZQTPN3Tz3HDOFV-tCDCaTnjMssaf21SJVESmQ8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c11c9aaf.mp4?token=pOqc6T_BRZJeRnXtS33O7Z7bvFFzswdGKBg8maCYcZmn-ruDKeShEKSn-sReKiQSuJgp9GOD7z0Blo_E3MJdFsqnsmWMz82TvVikmV2gkgVCQDYz3IuNoMb53dCtNNQgyGqqf9sfyG8HdEbgtR_tqT24Jac6xy9MEiriRe3XKVx8JZ9XKdQr-OXdfD9N-xx2g7GVuWtPtU_EHfW2sOK4KiFrJtn62-p4ZXqbz7vvg2Y4nqokgExz60KpOTV-1OV9ZGI3Wa7DjiDKt69aTprkedphVk72ask7IaA1cvk7OALu37ZQTPN3Tz3HDOFV-tCDCaTnjMssaf21SJVESmQ8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیۀ تحلیلگر لبنانی به فعال سعودی: ایران را به‌دور از کینه‌توزی و تعصب تحلیل کنید، دشمن اصلی خود را بشناسید و پایگاه‌های آمریکایی را از سرزمین‌های خود برچینید
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/452743" target="_blank">📅 20:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452742">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa4898b44.mp4?token=TpLFPjTS_T-32UCQU_SNdj73tpddKUFsyuj6SYtWcnurkDLxUuNXYoHbkF1H_eJr2FtUDFutcrojoyaetX7nhisj-7N8gRAzdzXHKXdt0AYQ0lRPao-h8QlKwFD2L-IvxYnuDvQucXlWe78Vc7UzedKhPLaViyNdvDUmE7Z9Wkhf6ZzUf0pOE-ZFvGmvRYiPU_d3yIufGzLQQFmP7DzyN0AKLb_eU3HuIpd3ELIQYvk0pQ7f5KXEvW1gVOoU7Pcqywx3ZvoPRgdSSfzNgF93Vs88RnBJHVV2C3rYFF-s2vr3asf3xNav312Wz0oOctaBdnxjie6brrYnzQwgBYD0mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa4898b44.mp4?token=TpLFPjTS_T-32UCQU_SNdj73tpddKUFsyuj6SYtWcnurkDLxUuNXYoHbkF1H_eJr2FtUDFutcrojoyaetX7nhisj-7N8gRAzdzXHKXdt0AYQ0lRPao-h8QlKwFD2L-IvxYnuDvQucXlWe78Vc7UzedKhPLaViyNdvDUmE7Z9Wkhf6ZzUf0pOE-ZFvGmvRYiPU_d3yIufGzLQQFmP7DzyN0AKLb_eU3HuIpd3ELIQYvk0pQ7f5KXEvW1gVOoU7Pcqywx3ZvoPRgdSSfzNgF93Vs88RnBJHVV2C3rYFF-s2vr3asf3xNav312Wz0oOctaBdnxjie6brrYnzQwgBYD0mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: حرف آخر حرف رهبر انقلاب است
🔹
سران قوا با جدیت به‌دنبال اجرای منویات رهبر انقلاب هستند و وظایف خود را تحت امر ولایت فقیه انجام می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/452742" target="_blank">📅 20:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452741">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">📝
تا دقایقی دیگر؛ پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/452741" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452740">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gifcw4Ctuyxa2PKN81Afs6bPXrgEQDmQxzFWOQGBwutYZWwOjd46eOFWD8YPqa-sb0SWkzh8YM4gJr6DXnoSfLiQPO2iyDLEeCVrlXU8vTVDWkEYSSEBH7oOvIQSVhnKygWWmvVTKSktWj9BPFCHMtqRXPcAHcpRu8QQCElV6Xa_o55eRY-WYkebu0C0LkxwhbfcKoi03ulgmH4mJpODaIdTrFMEUrEqhBBBnnjwmRtLU1-xWknvcBtz6JbajMLHfosHICtBFd8AwFEhWsDM6XkUlRWhs-waQSjoVZWWjiNRzU0t6OAFKuaBqvPIgr11nHS7XTkMPTBirEcqmg0GaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: جنگ با ایران، تک‌حزبی‌ترین جنگ تاریخ آمریکا است
🔹
خبرگزاری سی‌ان‌ان در گزارشی نوشته:  درحالی که ترامپ ده‌ها میلیارد دلار بودجۀ دیگر برای تأمین هزینه‌های جنگ با ایران درخواست کرده، دموکرات‌ها در کنگره صریحا با این موضوع مخالفت کرده‌اند.
🔹
جنگ علیه ایران اکنون به جناحی‌ترین جنگ در تاریخ آمریکا تبدیل شده و این اولین‌بار است که یک حزب همۀ درخواست‌های بودجۀ جنگی ازسوی فرمانده کل قوا را رد می‌کند.
🔸
حتی در زمان جنگ آمریکا علیه عراق که توسط بوش به‌عنوان یک رئیس‌جمهور جمهوری‌خواه فرماندهی می‌شد بیش از ۵۰ درصد دموکرات‌های سنا از جنگ پشتیبانی می‌کردند اما الان اصلا اینگونه نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/452740" target="_blank">📅 20:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QW9hKNLr9y45deE9zCiNpbM-Xoi4hvcul9mZsMgBeEqM9FFbOnzb7QqMDE7lVHCxg0XzuawrFoioV5Z1lEW2T9yh0kUGNnxhQPJ6yWPMWR_HhvKtLhJER5-lPHk0JJvaitwonwSOMvA_uIIVth9j57MdMbTxTFHdYtw6oYJM3IAcpHLoAOPR8S5Nu30SoDrO0lqMukV-qFYABUdcY62umtRQk9DTpWcdNX7gs8pBj8oP1xb0zTh03AKBNF6ySP21Erduox6xuAm18ydrU-OJTKxg7v4Ys2iA8WkU_3IBYxv0KGtfQHIwavhzuApvTbxrKduAIZb5hLcTkadRmTb5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلالِ تاجرنیا شفاف نیست
🔹
در حالی که مدیریت استقلال در ماه‌های اخیر بارها بر شفافیت و صداقت با هواداران تاکید کرده‌، قرار گرفتن وضعیت نماد این باشگاه در تابلوی نارنجی بازار پایه فرابورس و روند افشای اطلاعات این باشگاه، پرسش‌هایی جدی را درباره میزان پایبندی علی تاجرنیا به این شعارها ایجاد کرده است.
⏺
باشگاه استقلال به عنوان یک شرکت بورسی، مطابق مقررات بازار سرمایه موظف است اطلاعات مالی و رویدادهای بااهمیت خود را در سامانه کدال منتشر کند تا سهامداران و هواداران بتوانند از وضعیت واقعی باشگاه مطلع شوند. با این حال عملکرد این باشگاه در حوزه افشای اطلاعات طی ماه‌های گذشته با انتقادهای فراوانی روبه‌رو بوده است.
⏺
باشگاه استقلال در دوره مدیریت تاجرنیا، بعد از اعلام تغییر در ترکیب اعضای هیئت مدیره به تاریخ اول مهر ۱۴۰۴، به مدت ۸ ماه از ارائه اطلاعات مالی خودداری کرد تا اینکه صورت‌های سال مالی منتهی به تیر ۱۴۰۴ به عجیب‌ترین حالت ممکن و در دقیقه ۹۰ مهلت معین بارگذاری شد. اسنادی که ابهامات فراوانی پیرامون تایید و بررسی یک روزه آن توسط حسابرس وجود دارد و مشخص نیست آیا اگر  پای مجوز حرفه‌ای و الزام آن در میان نبود، مدیریت استقلال باز هم صورت‌های مالی سالیانه می‌کرد یا خیر.
🖥
گزارش کامل را
در فارس بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/452732" target="_blank">📅 19:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eaae38011.mp4?token=iXWTQAKuA05Qim1mSo9l_8qF5SrUXM9JqOT5IuVcXCWh2VgLDmQWZtxa_HcikLyiI0RAwLszzPXdpXJLLGEsf-maQMHzxqTxu2IeK1JkRsPyfVW0QDFXqvKQZ1SVXBS8cp9zr20ZFp0Ug0-B8UeP95DjIi5HTnqon_xhXo8PYQLRV60tJEiec2VUWwMe4-z-tmrGyCrzjiavI1ADgO6RZWnilZVJd7tjgTTIzXNJ9OeE36PD0It1FZW-bDFOYoMiJK5omlSVbyCiy7s4XTrsbBSELG4fkfc67IwRcgNI79Bg2PMGSvgDPr_-CCLAi5aY6WfEdSmzI-AZQqcWTKNS7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eaae38011.mp4?token=iXWTQAKuA05Qim1mSo9l_8qF5SrUXM9JqOT5IuVcXCWh2VgLDmQWZtxa_HcikLyiI0RAwLszzPXdpXJLLGEsf-maQMHzxqTxu2IeK1JkRsPyfVW0QDFXqvKQZ1SVXBS8cp9zr20ZFp0Ug0-B8UeP95DjIi5HTnqon_xhXo8PYQLRV60tJEiec2VUWwMe4-z-tmrGyCrzjiavI1ADgO6RZWnilZVJd7tjgTTIzXNJ9OeE36PD0It1FZW-bDFOYoMiJK5omlSVbyCiy7s4XTrsbBSELG4fkfc67IwRcgNI79Bg2PMGSvgDPr_-CCLAi5aY6WfEdSmzI-AZQqcWTKNS7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چذابه؛ گذرگاه عاشقان کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/452731" target="_blank">📅 19:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GezOtJfE8sj-LYSvc_ia89KU-JvBf-0x2vq3c19Fced8jotm-nzRbdUf8gOkHKFbX9XTt7xJKWqvXf3yNJNvkQMDZ5wZmteDExQwbKPdM7_3KhNflOhR1BMqeUn8-2MCcdxK0HOFfWgOymal5FGuQILxQv3CxT_l3Di9roF_sAmgLiTjfVxmr6qFEMNDTPrVsnn3nnV2TyGK2vp4Enff_y34PSmEqtTpBDALFES6AwiuNRx1TEWnZAlMR0evilIU4-oa3ATtqr5vKAzDnWmORXpFfAuLmbSWxNVFp4LY8XoYJDqJsN7gTrlR_zpqqR6kU1J5nbUv7msMllT5HM6g0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ عراقچی خطاب به مسئول سیاست خارجی اتحادیهٔ اروپا: شورای امنیت و اتحادیهٔ اروپا باید رژیم اوکراین را بابت حملهٔ جنایتکارانه به کشتی تجاری ایرانی پاسخگو کنند. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/452730" target="_blank">📅 19:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTQ4LvB_55KCRu57iAuxIG8nbXDocOXCmAxnc5LKiOH0n0F_Pvg-m0Rzftpwm8H8j2sqsgAa_JrfATynR5W_fr5N2dQd6hix5MVykonYCxIyYv0rMiji_r3bAA7UoqFY7fn86ywKbSuskqwiCmcHcpoQPtqphXYKiXVf1DXqW-aEoSArQxJtvc8TptBBAu6wKZzPuispfwcabkibxBFY_5YHGtB3sM1AQGvLh3IXcyop1_D-zll8zbFtl999_unCu1u3PkGb2e5VyF17V0sW8dSyabRWMXVL-EwRo6JOncP8CNLxIw0OXXkS2RmAMKmgtJ76BzZjNN2q0uni4UjiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات تخریب صهیونیست‌ها در جنوب لبنان
🔹
رسانه‌های لبنانی از عملیات تخریب بزرگ ارتش اشغالگر در شهر بنت‌جبیل خبر دادند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/452729" target="_blank">📅 19:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaCpWGEGkc9VwaBevDeYxdiLzPCjEXwRT2xKain0Zzaewqj_djrzysPyu6xc9MNNk65ALC8Erl3nZ6rfny-2r3jkFM5t_FHNicjmL5ICPfyMcOu6DTJdjarKyBgPT_uxoffqvta927eW_lNJW7NDitZpVrTIaS0DB5HmW2nSbrAhxq010PtAAmGLPiMfE-PjoIItWQjVzsfyiSnRjol5T_QkuXbLVZxH77e6nIGm2yG9XV5_M6w7fjfReADtydnQbCoYBR3QD71nxfnolr7DfFIHEwJSkJk2OkyYUaqE8TRP1ajEW1stqFOxkic7Ql8A4eqGWy0NwiTInkwxpiojww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الاسلام قمی: دنیا باید بداند از خون رهبر شهید نخواهیم گذشت
🔹
رئیس سازمان تبلیغات: نباید اجازه داد دشمن با سرگرم کردن افکار عمومی به حاشیه‌ها، صدای حق را خاموش کند و دنیا باید بداند که ما از خون این ابرمرد نخواهیم گذشت.
🔹
وحدت حقیقی حول محور ولی خدا و خواسته ولی خدا شکل می‌گیرد و امروز حرف دل‌های مردم خواهان خون‌خواهی است.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/452728" target="_blank">📅 19:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452721">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MfkcISVhgwCUQ634mn3_DSozF8c34tIRYqAMlWoO1ySL28hnIQWSvIbF4Xq1yKZe3sKuNMSLoq-emzkuwuKXmnvTO7tRtTWL8P8WWL1asUnMGibIUpVgkFvzfJPP9pimqgIwe98BZ6-JKzGomGoRbM8EHvDOrI1ia7bqnwQltCTwyH5CzfDp8Sl0ky2SKQVtt8RdLHxqNeEhGIqeqWRu4PvDjY6J6wkot1FbOp2fpkGR3q8LUo4EZodUgN3odSGoJb-r2NZ3jcs29NhbnXus8YeJQJHtQzdxoLRu3tokV4OB85jP5Y7P9Yr6mak6phbRqcLALUBT1YF1fTgyfp00GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r87lpq8q0YXSfbwAd5xx-J5vkOytOyLLJ1vFenbhI6N0g553bRftatgcSfgjkg4Gw1FOkr6sUzfXBl0qERcAPMx1x6a0DN-qmbuQ4NNgMRs3S_Q8KNBkRQQef1SjlUrPDxkg7sZ2Swv5LjTa726DbjTw9oJ0UOz0ta-4oN4JY5rbSty6Wz2xrxM31tzjwkdVaf45PjzoMMHR1G8wV75TmguWaElFUj2ZMpwTYYhrFq8MLPfKMWpHnDxi_W9PVsw_CFwHMQGTUFGJwmsgTJdnwnfZmt1TJ3EhspqUFe8IO1liTGi7veADdWyNS9Pbku9i6qNakuNu3lVIDaFN2bj43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pNJLEdXBuuzOdwJzgOnHakcNVkrqMK1GMIQ1ovISxax5SuJxCXLTeV_QmL_r1JTub5rYP4fSJ5gn9AyV16IFGhiFnqjNr7sS7tiDr2CHIO3umYso4Dy_pxee1D6vkkHiO9gyqgKYgOamYJURMQMGiBQrqO8NZdEPDQBgyGoPBPRlla0BkK-V4RH3K2MzUrqZEWHxBJNYsxnTDteCTGVRmQSYpSNtjIn17WxQlO1YrwwqwQQR1rou_SpE7JZoQXeXofUsnLS8Y2YtfBNz0BUpk3hGZHo53RY7p2vTw7jNuCegPFhj1RvZIhIWEr6qrlNx1P-BuTh85pmt55rNtZzP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8oNhwTUlUi9f3wVdnD_o_XVI-Jo5AQpWHvR7fEzvpygWV9IHqUkx_-5PJH2ewadJFIMuYvGouUdBfoOI2YysoklZb2VvjcQ8RO1RB9PgG1tiGvQxJ031j1QUcbtAn7MkjsK28KmlY20iuLfA2zYHStH8DT00t-r8JobNKe377DOpno4kJqcfacoUs6kF3gPbiq1OIpZxOBuldtSJ8m3yY641qkYehkR2Q25WvHitekjzdaw4r32MRJhS5BrQa034f_Wkzcwb-Y_R3pmh-Ax3H8iPr6yRQebv6jMC7GsfKf4WKIgnj3RM9F9UU0MXZleoaSJcgwxEMtflmTNUxlV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DaIxmQzVagOEybJ4wgcDSQFRR5x0O8ldVOUzOYPfon5pHCWcqCIUAHxp9WWCasTGGACiJyx6f6cjDxIriKBqX3g4xWPC1ECJd50zifUUKquWOGwPr2uVEjlY4s_SRHO4Umm8XxEzVIh6UDuTZmNI_fduGovQYxoUuy8WBVZ-KkrgiVz5mR_Q5V52gyaVwTndgMmiUUgKGC7Q2uMiqfyF4wQkTZGezuHCS2Q6YKH07xMPuGYESfs4rDb-oARR91j8WvddXnSIgzncFvsZHCQg1BYxdOg0XCeP_FlMssIKFZ1IEOsWIWSrW-QSjgSB9iJhjrrh8QfDt0n8nNkY9qvLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AM4t0BUjrlSSNK09Y4eTV362CHtzN-raZvMNL6krvZlgB0UiKU9W1LkxrLZ-y06FF3beysiiXaahF8emx6EwPOWF8kfmX5e_9Y1JOfWAgG5zsG241q-ycjFKH4FD4K0YamaG8YPDcMHKVjX7PZ9NlDpEhQIxOuN3kIJ1xp8Y19MZDYaQnPOpIk5boGUP-33x0Tsjsk3ZnAzshQK8goTFA7Ws0w3ejR3C-jMAA8pWspLeEjBbSeYLU0UPk-s3JAF5cV6HCI6u1tSMe3WclUNhZRAEURkvSUyS-90ZjzSb1efGxUHrK9Ru6I2SSJUUPo0EfAuZqzm6u6zInSac2USpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWh2xcqzojNgktIg7RiaIEbXCoWaHZJ0D0ycnphrqZpHp-mYUBKmlYJQvJCxq_PgjFKPf38T7RuO8DXkQ7IEqkDSPmHQOx8mAkKJcD13geUJIB66BZN1LFS89teGgSzdZpgQRHZBvtEx1WyUP2zG4YWx63ZJ_9ZT83y-XHQjlMyFKP5y-dd2do27RpQkDlN8HEFddYBdbvPaWeUjBkO54StxnOuRoPngYy-ldf_YXfIi5lfJ4jsmkpTrhSnTBEtevKXQaSmBWW5eeJ1eaOIdnLgpthB8q7dUBLFKKqhWPhV-EoYEaasyQ4mUiZvVxYXC5fy7dbmz_rc4R--sZQj-kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زائران اربعین، استوار در مسیر
🔹
باوجود افزایش دمای هوا در مرز شلمچه، موج حضور زائران اربعین همچنان ادامه دارد.
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/452721" target="_blank">📅 19:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452720">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fe9fd6ed.mp4?token=MVcPfmM4e4GF94QpE_NGk21ez_8elY5gSukrJBmRORsLvpJ0dBj-FPUUN7CRs2oyO9Ccx6ih_3ebjuzCwFyHfWuWQPZt5_KxhEIGjZbEZGj8Onqeb0dnmhscJ2yjjwP7jVcIDSaBsZ_7EVv6pRX-9TuqdDaZp3FPLGhgiRtcHAGAT1WDzr_UwyBwVS2UOKQ_r-hLgmNf_Lki-ouBxbYQM8CKle04DMs_jPdXQOkQZPh-Cfre6hAp7PaIrb-sHGQ59gX0af0oo05tD-L7TclM828iQi1307K9i_K9SMapSoSPGNKikvNH4VrGYFx-Yor68CimcGqqDIh85Tg-VVbSyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fe9fd6ed.mp4?token=MVcPfmM4e4GF94QpE_NGk21ez_8elY5gSukrJBmRORsLvpJ0dBj-FPUUN7CRs2oyO9Ccx6ih_3ebjuzCwFyHfWuWQPZt5_KxhEIGjZbEZGj8Onqeb0dnmhscJ2yjjwP7jVcIDSaBsZ_7EVv6pRX-9TuqdDaZp3FPLGhgiRtcHAGAT1WDzr_UwyBwVS2UOKQ_r-hLgmNf_Lki-ouBxbYQM8CKle04DMs_jPdXQOkQZPh-Cfre6hAp7PaIrb-sHGQ59gX0af0oo05tD-L7TclM828iQi1307K9i_K9SMapSoSPGNKikvNH4VrGYFx-Yor68CimcGqqDIh85Tg-VVbSyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنی که بازیچهٔ بلاگر قولنج‌گیر شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452720" target="_blank">📅 18:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452719">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در بندرعباس
🔹
سپاه هرمزگان: فردا از ساعت ۸ تا ۱۲ صبح احتمال شنیده‌شدن صدای انفجار کنترل‌شده در محدودۀ شرق بندرعباس وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/452719" target="_blank">📅 18:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452718">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41feae11a.mp4?token=OMeseNmRkEAFvVp162idHs1QP8IJPF1M6m9gSl0ebp61CVWhyecQhPFJM_hnXKGQmCrbBBzHOH_EFW9c0HGF0p0wfjPgOVkYLLw99B1_HRRzG-IN71soUfvf_m7Y_rzMBPydJiy_FaIW_ql5ctXkTi6sjWJdRqZMB37-f34Lz0u2DA89sg8BP6c_cMmivRB_LsOuctkrt7c2lXNcNVXxRK5pHiemo4oCHhHxNgdvtL_dGLanF7vGsYJoAzt5EORsnxtLSsQ6Sb_1Wm4_ajK3I2YvVpyxXdfeVc2FEZwZA3wftWHNiD2El9tSLWDwB19_SpK9tEy6EJVQHd2KKMO9hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41feae11a.mp4?token=OMeseNmRkEAFvVp162idHs1QP8IJPF1M6m9gSl0ebp61CVWhyecQhPFJM_hnXKGQmCrbBBzHOH_EFW9c0HGF0p0wfjPgOVkYLLw99B1_HRRzG-IN71soUfvf_m7Y_rzMBPydJiy_FaIW_ql5ctXkTi6sjWJdRqZMB37-f34Lz0u2DA89sg8BP6c_cMmivRB_LsOuctkrt7c2lXNcNVXxRK5pHiemo4oCHhHxNgdvtL_dGLanF7vGsYJoAzt5EORsnxtLSsQ6Sb_1Wm4_ajK3I2YvVpyxXdfeVc2FEZwZA3wftWHNiD2El9tSLWDwB19_SpK9tEy6EJVQHd2KKMO9hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنکور زیر بمباران اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452718" target="_blank">📅 18:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452717">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آلما: ایران و حزب‌الله آب و برق اسرائیل را یک‌شبه می‌گیرند
🔹
مرکز تحقیقاتی آلما: وابستگی شدید رژیم صهیونیستی به تعداد محدودی از سکوهای دریایی، تأسیسات آب‌شیرین‌کن و بنادر، این رژیم را در برابر یک حملهٔ هماهنگ و چندبُعدی از سوی ایران و حزب‌الله به شدت آسیب‌پذیر ساخته است.
🔹
بیش از ۷۰ درصد از برق رژیم صهیونیستی از گاز طبیعی استخراج‌شده از سکوهای دریایی تأمین می‌شود و بیش از نیمی از آب آشامیدنی این رژیم نیز از طریق تأسیسات نمک‌زدایی که آب دریا را تصفیه می‌کنند، به دست می‌آید.
🔹
این وابستگی شدید به زیرساخت‌های ساحلی و فراساحلی، نقطه‌ضعفی کلیدی محسوب می‌شود که یک حمله موفق می‌تواند تأثیراتی فاجعه‌بار بر زندگی روزمره و اقتصاد این رژیم داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/452717" target="_blank">📅 18:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452716">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146807f99e.mp4?token=jK8f63UDNmGb5aCjRUBdrzL4cPBrbc6QxTQPkZjYLovDhBM7PiX-CEPxhjR57p858PNW4bjy2ZBQjonOGOBVC1lbEhJaJO4CAHet9s4xGeCuQUlcqkSzx27hBM1483NPpGqC2g9Fg8BLuAxBXax6HyI-MnSq_60Jl8ino0JSx9fXU6RIBadO2TbZ8KMS42VJoMlmx8NZ6u7f6bJKaRREzrzdgXhvWEzwPXRIEXhMgwCBeZs8xqfid73i2MBM9acuf1eES4rt4D_YJPiNc7fF9JTBVIA9cjFm37q9wn-SbiJSBJr9tpoGvpxJcTtUMxf5n9VpkOsulheYZLRhEVaKuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146807f99e.mp4?token=jK8f63UDNmGb5aCjRUBdrzL4cPBrbc6QxTQPkZjYLovDhBM7PiX-CEPxhjR57p858PNW4bjy2ZBQjonOGOBVC1lbEhJaJO4CAHet9s4xGeCuQUlcqkSzx27hBM1483NPpGqC2g9Fg8BLuAxBXax6HyI-MnSq_60Jl8ino0JSx9fXU6RIBadO2TbZ8KMS42VJoMlmx8NZ6u7f6bJKaRREzrzdgXhvWEzwPXRIEXhMgwCBeZs8xqfid73i2MBM9acuf1eES4rt4D_YJPiNc7fF9JTBVIA9cjFm37q9wn-SbiJSBJr9tpoGvpxJcTtUMxf5n9VpkOsulheYZLRhEVaKuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممدانی: نتانیاهو اگر به نیویورک بیاید بازداشت می‌شود
🔹
شهردار منتخب نیویورک، دوباره تأکید کرده اگر نتانیاهو سال آینده برای نشست مجمع عمومی سازمان ملل به نیویورک سفر کند، براساس حکم دیوان کیفری بین‌المللی بازداشت خواهد شد.
🔸
این وعده بیشتر نمادین تلقی می‌شود؛…</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/452716" target="_blank">📅 18:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452715">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8626a4195e.mp4?token=bBDS26bL56idjaw8VP2bPu0Z5unhOyWCa23h82aFvNn0d2Ybha-xtISq1wrdk6B59SpRa70Yv1ZuUCuYcELEdsUsTdM9OTEF26OR-t2FnbKagafOCPO_rAjIVKP-Z5a4hmijHBWlhSvD9euK1inhgpZouZ3SjlhLfQHNkg-Y792rr7SYfJzlSEcDHzpojCyc76-mITepXI-QiEDhxYO6zzLYvUL4VZ9L0k-ROb80GsuDyJjhQ-zh0eOMt0ysmpXAMvr-tFdz8wlqFPYy5wMWFiQCHYdFrI6Sa7vva4A9oULAdlejF3TdP0m8dJWvbpKvGm5RTwIe95uVD6K5nvvG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8626a4195e.mp4?token=bBDS26bL56idjaw8VP2bPu0Z5unhOyWCa23h82aFvNn0d2Ybha-xtISq1wrdk6B59SpRa70Yv1ZuUCuYcELEdsUsTdM9OTEF26OR-t2FnbKagafOCPO_rAjIVKP-Z5a4hmijHBWlhSvD9euK1inhgpZouZ3SjlhLfQHNkg-Y792rr7SYfJzlSEcDHzpojCyc76-mITepXI-QiEDhxYO6zzLYvUL4VZ9L0k-ROb80GsuDyJjhQ-zh0eOMt0ysmpXAMvr-tFdz8wlqFPYy5wMWFiQCHYdFrI6Sa7vva4A9oULAdlejF3TdP0m8dJWvbpKvGm5RTwIe95uVD6K5nvvG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نتانیاهو: خانوادۀ شهردار نیویورک سالگرد ۷ اکتبر را جشن گرفتند
🔹
ممدانی به‌طور اساسی از حماس حمایت می‌کند اما در تلاش است بگوید این‌گونه نیست.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/452715" target="_blank">📅 18:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452714">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqLK_fsmFhgvk4sDD9Diw6PR7RBqYgOTNgjN-UdGjFbO62RRHMHihihsq7nZj6HNSBrabr8nYV6d0kER_QLTiyoQTadsSCUAXEa2eFaT3aDymdmsn_OyoI3dfakSoq3YejkaHLSiZWRYFzPVPGtywfLuaYp_TmJF4CyrCyuZLPyTu2HgtI9kGkTMR_1ujO9EMHr_E_SG0zZbQsvC4XQNuhFHeOU8yH4CiZTZOR-BKmswK9jPR3JKzqLzQfFnPH9v4onzlyTC0oVvdwI4uxQ0q81gZ7OHF7_aSo3s7N_ktsfkpWDpibMLVgYHGI-8B8hDGP1Wj1yfD8waPBrNbbn-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از وقوع یک حادثهٔ دریایی در جنوب دریای سرخ خبر می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/452714" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452713">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjgHCj62qCluhE0Fh1hMvzUaBubVRUTZkfedjHzrWLD6Dk2Dn8BhUvNR7ec6NG4zx1_qUajAnCW9711TSQ9CJGp_jjl_yPTzCwOey9IU5vjw_CqSD-5yr8NRNVW6qe3PkBqN8lfUtcCKYNIVeqX4AR18nh0Kf6X9J-JFwi3IVxjNB-vEe-A0PjwZW3m0soT9fxRZhinEbqnD8wN7g7BzYr-QfqQjD-5D4WZuUZEIi1EzU77m2pHEQHTFNhMpnswEe0-CEi2hNoyqcPQz5SayTaoDNLiw3KLnG6iCz_0feoUgUvq2aF5MBsDX9ydfwgaMIDZfM6tfBSSEXo5O8FoU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام یمنی: عربستان از شکست آمریکا در یمن درس بگیرد
🔹
معاون وزیر خارجۀ یمن: حتی آمریکا با همه قدرتش از به زانو درآوردن ملت یمن ناتوان ماند و خوار و شکست‌خورده عقب نشست؛ با این حال، رژیم سعودی عبرت نگرفته است.
🔹
اصرار رژیم سعودی بر ادامه محاصره یمن پیامدهای وخیمی برای اقتصاد عربستان خواهد داشت.
🔹
«محاصره در برابر محاصره» یک معادله برقرار است و کارآمدی خود را ثابت کرده و «تشدید تنش در برابر تشدید تنش» به‌ مثابه تیر خلاص بر اقتصاد عربستان خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/452713" target="_blank">📅 18:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452712">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۰۵.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/452712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۰۴.pdf</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/452712" target="_blank">📅 18:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452711">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e93b70354.mp4?token=EhbbPOZQaiZAHkwtKM32_xvxpAGlL-lcerDAP7vLlwNjzrU1gvNU6e0XA9c1Ds1K-616VDu3K1uzHZpO4SQ-aURlXCzbiaWkmLprRSJ4JDzacEekmjqX0_Q6YCtXFuApU0PRxddKg1wzsEKakYFs9zUA-ky5W3Er5_xxDX4swF0dpkj8VN44GMnzbo5zt0njPgaEQHAbFEtaod7AJ2xZwzJ59tgiBUo6TTJehcX5qZB1ruEgj7GVkCpfMCUCj6NOP_beOoKQ_XOLiMaLUTVkjP4Urye31HobOEDohRHoVlmR1t7ZsojZd4DrM7zlklFvZX82Y2PfPxVpQIMUe82QRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e93b70354.mp4?token=EhbbPOZQaiZAHkwtKM32_xvxpAGlL-lcerDAP7vLlwNjzrU1gvNU6e0XA9c1Ds1K-616VDu3K1uzHZpO4SQ-aURlXCzbiaWkmLprRSJ4JDzacEekmjqX0_Q6YCtXFuApU0PRxddKg1wzsEKakYFs9zUA-ky5W3Er5_xxDX4swF0dpkj8VN44GMnzbo5zt0njPgaEQHAbFEtaod7AJ2xZwzJ59tgiBUo6TTJehcX5qZB1ruEgj7GVkCpfMCUCj6NOP_beOoKQ_XOLiMaLUTVkjP4Urye31HobOEDohRHoVlmR1t7ZsojZd4DrM7zlklFvZX82Y2PfPxVpQIMUe82QRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لگوها علیه قاتلین جزیرۀ اپستین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/452711" target="_blank">📅 18:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452704">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNZ8OQUGN4G7Yg93qHlUOWPZ2A99b1xfegeErmq529WIZK-HYS7GhHmxZhjUFc-6uKnZquY9pKo4si7K17rotNjx1dOIZlBrfGY-xfKP09BLu9yM-gIqtfPNmkXKg0mEuiA7JDFTO4Fh1tQJlKlTkn55Juevt8RJkuAHJpdVJa1bRm7J1sEH9XeXxYYKJcASpQFrushrfknv43QhBK2jnNSJzhXqDIbrx2f0EHptZKgJy0xztWR-erm2HGD304d3OQ-QNiQRdgVStCvQeu1gWnxT0Jly2qNlIjat_-Vsi1rQSGY0yQddWCAm2Mi376yl75mjuFGcbzVy1oPA0R9hNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0WBXtdDhGxR-HktJVSuKbDyBhAwnTUZsGJVnEdF9Qg5gXab3rPYpbzFudzxFnIbXrp829xUItCvVPcHqBdHqJj9jI8LaXzkLrcg3XvdnsMnJE1fi8uRyTG1_pQpxD9DKM9_YzJoFxYDWP0Tn-QN5RxNrxQV1Pyoz30Yzi_NbrvkWRTZYAsjpVgtlvD5aBmey-MxiRVqpIaXG_bV5m7rzLrI1opqNZ0NPZimznW1a55cPLqRiS9Cg3bR3c7y6bYoJsXIrloI6cWwycbXHLWHZqM-V4J0-02zq9uvj-nfsKbluBlOWPnS5rdCjhsgnbbkm4rPWz3qZig2RFdiI7MTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kDZxtnEVCSIqO4CP1g8QvdEXjpLzmLaKN0hHN1LKJUMdK7PuWy2KjGJIjK4XgL4MqtmE88JPmaHDEw7-SU4X_pMWdcbp-XVOECvuRppxT6u2MdMl8oQg7dV2EzIqLhUydpXwgIdV1UnYSAy2pgcMiNDwVYjh4nwZ5Z4YWUv15ia7VrxQPFy2H93hZVwU0NZwTiFbnV1Qw6kX92XnABySNwdZd5zU0LP_fXJ7I7cj2_uCaLxNOG5yy561Fkpq_nkP5eoWn20ucovxsIAfF8AUeXkBiaHIkqsh2115HAkViEC74a9uxzBw8JpUZ2HNUmjII4DX8KnePB1J4XupjukhQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTU9chV8HXV_uoZrr7JjLIXrpO6xI5mhsTS22EWE4V3eU3W09xBiy6OkPBIdgxN5Fy2bpTKoZz4TzEzY8MP2iwgrNUACXcQyeePWBVnN-INMsWq1uU6x_M6AyDT7B67RGXjo5YIUHGg_8jT4Zn7qSJN9W15Ks6MaTqqhdB9bEMvqo6dd77I6rBzEGZ4K44jEJK8hHCVqiGjktewUIgOo4RCcTt1iWSPMkvCy__AIm__i6Xq41XQM8AtGwrT2mUO0-0_FnslQhrfI4u8TzpMRpwmbLyg5tMIWWFwqAO20V0tgEUrlpMN7gR7rkNkfd7jKHLCgkcz_3DtOQjJoEvnVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XS55Nz1_Q658JJww7kRWQ9ZU_hqxGr2_-GpPMLl5fHc5Gl2ZnwaTJQnwAXZgpDt3bUcTVP2rWOD3xYY2xXh-Fq-OzWMcf5Mlq5DuAh6t1D34C23eXvbgR5vGEQ2IekpC82vcYUrFp1vPCoyhKhVC8v5SARZxQSfCSFOUdXWGC6HfFYRkV1TF8iueLgse-ji7NCqWrpSfN8KZSkQfpKNJ8yYUsBATDM-lNDYkPepQH_7uHzsYhPEqBSA5oqK5Y6p48ggANVo29iPeC8Dqb1C3NDgz3tZJ2MvKF5ELLQi_bjZuQqb8Ln91CtCS4RdLNmlSFi43ww8UYDaszur7Wo3O0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVIEzET7aUHonhe2EoIbZiYRvk1Bw9uyv5Mk7jBlIhBafSk11SNpTF3AThaT0ICebzOMWPTsRMqAgUhSfIRL5berq6vplfufHqXD6NUAjVnYr8MjHeezVCMdviITruejl3tzNTAISnA5bI8xX_wuUvEPywV_xLo0TUakctBDRB33poS44cXxNUpo_K8q_q2d1kJD0g-0il5wEdYYMN9chmAOxXW1nTDiu_x5K9P3iPw4i3oL-JR1JO4F4aaQQm7T4iX3Fg44c6Nsi813lNOYoLSYpClwvJmqRzmZFX01fphlwS4dmRKqQw3vEmmP45NDPAd3qW1Jx2_e01HcDOXraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxIbQ0K_M3-3zRDk8XBh7QbAlDUXXrqQt16F31FG4wsLjViviKRpJ1_HOBATM01ZG61M3lViOffX4-_csriZ0XoEXP1FdlB832PqZR3LySsgCVp2Nh7kuNPwTrcaBCRoHTl39JeGFR9dbr09vb-ZMYSdxDlvlJr-3I_YNOZ2kqN2rMAN_IDkBgW1mIansdXnsTv5PSyCZo3aa7JSAmjN5hw8tshVwnN0ubrtqpjX3tGWQAP2JwKKsQI7avn0Am1l5DeSo1mmh7e55mB6GekmKYFZpza20lgEmeql2Q17O8dpa_cWhy7xtfRtU54WEiavqUEhu_dwWfVvC4C_V8SBsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر زنده‌یاد اکبر عبدی  عکس: محمدحسن اصلانی @Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/452704" target="_blank">📅 18:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452703">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580959d445.mp4?token=anWwuLSH2gLCSSgo_l9-Ow4I7_MWH1dhCBtsKgSrxRaOFlXP58CK6puMcQ5Vm_HuA_WLSv_jDKbblTqESuFDbeyWftXqdewAUvEYBmDJKhiaiyr07JryaSBaTcqOKOiYjqrpQITHJkA53-SaDyC9sIU8vGwpN3-fJxzK5-Aa4nYV26yzRlPyMhwE69cf_Rfsnqz9XPxd3TFhOKIWjS5OkplLDjSXpzJMAD7DtwCsHlD_zefk8daBfqjv4g_s4kEmKn7bQVs3kkD1atQV7y1ytAP8B3TdccY0myDW58Nj4rx24sRhZSO_a-rKII5JDzoYnA8SQOdRVObSVhn697Qidw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580959d445.mp4?token=anWwuLSH2gLCSSgo_l9-Ow4I7_MWH1dhCBtsKgSrxRaOFlXP58CK6puMcQ5Vm_HuA_WLSv_jDKbblTqESuFDbeyWftXqdewAUvEYBmDJKhiaiyr07JryaSBaTcqOKOiYjqrpQITHJkA53-SaDyC9sIU8vGwpN3-fJxzK5-Aa4nYV26yzRlPyMhwE69cf_Rfsnqz9XPxd3TFhOKIWjS5OkplLDjSXpzJMAD7DtwCsHlD_zefk8daBfqjv4g_s4kEmKn7bQVs3kkD1atQV7y1ytAP8B3TdccY0myDW58Nj4rx24sRhZSO_a-rKII5JDzoYnA8SQOdRVObSVhn697Qidw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرمزی‌ها خطاب به آمریکا: گیر اکری توو تَنگَه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/452703" target="_blank">📅 17:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452702">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ddbf4167.mp4?token=VcB-95Wn2st5RJLzTqZyVft4KorCexpXulMsjdHYUTskHBcI97akmcEDMZI7g8qUuhqP9oR4IE4bjefxNXOqhD5Rk-2dq_j1QIzVv3ZU-Ejd7Apwfy_Lo4nLRlZ7d7STaBObeIcETcoI2h8PS-NU8iQNgO5VFfwkR2aiWFi8xWCNur_7s5sBEBH4UuWCZ2sZYKPWArfWVDRjP2j92lJ1lzf9OKSgS2jKIq37GuF8yIxjlFlJVuR71Ukx08zWb7tsZ-VgkHdg1yw-aNSLOe6SvC7Mud5wev7_AKRfCYQjvFkbOQpzqYvZLUAGJiaYi-dgunSRjuReQAVn8jLfPxUoeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ddbf4167.mp4?token=VcB-95Wn2st5RJLzTqZyVft4KorCexpXulMsjdHYUTskHBcI97akmcEDMZI7g8qUuhqP9oR4IE4bjefxNXOqhD5Rk-2dq_j1QIzVv3ZU-Ejd7Apwfy_Lo4nLRlZ7d7STaBObeIcETcoI2h8PS-NU8iQNgO5VFfwkR2aiWFi8xWCNur_7s5sBEBH4UuWCZ2sZYKPWArfWVDRjP2j92lJ1lzf9OKSgS2jKIq37GuF8yIxjlFlJVuR71Ukx08zWb7tsZ-VgkHdg1yw-aNSLOe6SvC7Mud5wev7_AKRfCYQjvFkbOQpzqYvZLUAGJiaYi-dgunSRjuReQAVn8jLfPxUoeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ‌‌های اینترنشنال به دروغ‌های خودش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452702" target="_blank">📅 17:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452695">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFM9hIEP5MzpaEWilA8RQ42SFqlK49CPT_wXQjCwl4vSsxTqfO9S1bg8IATa_xnkXvFFoFtrkdbqWiE8hvE2zAYTNy3Hw6hyDd--EisqAnLYg25KRjqDbl9pqjJploJDj1LHrdnPFxrcQ7AYFpBDD5Ij42uTNRpGziAIK7J45yStPrF9BWCnf5F6iG_5uJyVLZQq9w43SftAf9ut6sWKGooRyIRhkVJ7MZG-fyGvDmfGJm2Tb7OU-xQYtsNif-BH6sFIIYRwV87UWv1u2WmHszdRwGmjX24MyyiR6EPPU6P8rYRyZ1t4dX2o59DQx4uD3HHtpW0dZ3n-6BOGrmCtCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuAjm0IblinwRaz6WmPLDFXEQADi6nicw45_wk0c5k2jJmhxFF2-gJrfsdl7mh08TFRH8X4pCCpiki3MJepthpjK8ca-oLd2amESB09WC79nCN3hk2W0i2ZUTJSSwxZkFIBlJKCWBnA8zNZT-OwrT__rTw9eW60EDqGKQw9Ndxvguzymnu9EwC3v39hsvsuuAMJVjoDtUSSNRS969-BnaQRgomtYo-ALAkwHkzlLkQ-LxGTOSsJnRoYpBsa5hAM1htll650t0fKX9BmVOUNdiXLylqEVB5tvJSz09Ju-FbulzNRMMZKrix8qiwdzmXdmlAZqvoa4JHdd-SJ_hmOYNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxiRxmPCH9cZvzaumQi8uSoPMJVxDdecch9l3mkfPFO05RBH2RGeLqf2euZNkFw0DeOpnYClwg6LTYoxaSyecpPzHfpYbnsk2bGhmGWwVNqyeX8GyOhBJbFcfilDnxyFuKNUwuAE_XUFgPEFsxd1H0EHFWcGAglQZO8t8V-V4ctNGXJxnF4ECEz6Dk8StRE3OIObFFakBJuTzQ7Cxa3M_oJKUfOQOTyPEJoO-HyB1axG0bquMDTBM9yPOCylWBVxG9F1oddPUNlflKYWZHJ-jtaBU_fun6vFUXYLsnWbtBc0NBKmSbj1jCEws3lNDGorrDPyVlDH6DXZSDvO4TBz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVUO5GqF69bV9XMxeFoqNR2Sw-wMkE-8h0zkL6EPtSFxnmBXcBp_xLWCxHh1NSdePEJUpOe8935EBKnAXzHen9LDKzJxfpkvDOT4GVfXfQpveFgVQY_fb5aU9vb5WcJVLWBHQHJc2oxlH__FBHKkCsgvDkEbTSuD_FWu1YkYZzG5uxgQ1dCh1HKw3ZZzTrZqpKzrcvy1_CFVjCE0u_J5-qMf4XzSgFM4Qvnf-oXX0V6mlWygWjRSmBhOEgBliioETGKqZeh0IuQNjiWoc8SBpbQq6le7lQ9f7FLYsIoMfdK9C90_cc8Uc7Rd5f2-A2QYbBQcrsuTaW-4GirZH09swQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_GaIb8mVmHJwzp1KvWtGBjy76q-EkNuUCgiVYknTLGYSiaTiDMETCvPUaSYT1Zm2YypexKq9eSC6O5E5V2UqBxsfY4lXEw_CHNj63F9_gRAh9N76AUhdtYLBDwd2w94hPLRX3Ky9Tp2yIN4uW5yeKCiM3eP6G4Kvf-qVFMQZuzV3mqZq7EWzberOPAf5s7tHg7KudhG7m_yzRbq44QOVEA3R4-m6q5tawlpXNrWp3v5P6T06rHYaZCG8rC2hqNl4RqhjJrQh2aEaX9deCvoTPcT95fjWYPqAsVBX77HjP0pBNqTB0o1V-Rg2PHpIaT3BryfSPSXXym8f_eUV8QdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgaBat__aWkDBEOkYt-0tyAtSCd_U7AfE1XgM6Ng-1pJ42vYSEuolt3wojzsmoZ79EJCSE3rteHxYaYyCcZzF_cybbCyBMJ2BIqOuIFm4RnvyJRLTx3UUm3Gbz9l3DY9i6TaKOER8LGZ330NOmhne6Zn0YmU0TLWTBknLZDb4wRrPYdvQKmhmo1A0-yrvFhrJIV3e06jI9osqD3NDyoUwpnZ049Ep1rS8a2ZJ5uhX4MAzBSBplPil-rU1BQTYydYhShtAohVDHBOuFvdyL6aQsmIV1LjrovSsaNt2UbByFX6QR5FHKT6CTyGEmQ5Ge9JfAxEyXsY254MvGiIj-divg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bxm-iig-NPdpXzWwjleca2cJPiKYe05Ewo3MC3A673YeFkN828U5pYjjHfRBZfd-snTK4VHUiQevzk-UdkmhUgNPZbDymFKFDWnucuRAaTx34u4DXppXjYDgwQUqHgygnnFhWA1ezzMWRP4t2IQ4V1Mx1VMaUsuOTVcKkWyGWsmBtSRfguZ4iDWX6PoWSKPggd-RRiN6kKSolA_E-b93YiJlUkl7r4MKwd7HDwDLK8_Xib10hygSDscAHY8I6qcVNcr5i4PvXEBRwuyed3EAmPRKiTCFhj5vd63I1CyFBTLpMBg2Cft-6uaA8RE_04e5bHBQ2KmteoKoT296hpCioA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور سردار رادان در مرز خسروی
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/452695" target="_blank">📅 17:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452693">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180f2b60aa.mp4?token=NIGUVtuYbOZz3x7aQhKUb2J51UQCvuVaDgSN99eJXwHquy12VGFpFJk2ftQC97sMR-0sj3uQitdn97h4TzkTS5eCskq1mHjJA-IjpA6NlxdJgfbELzg11TDCq9GMffRNNk8NNwIlkIK7pYkuN02KFpdNQeyNh1kPyuTjgI88EnQ1D5pDj5pnqC4tG4V_NEobzlXqORA4sf0G7kVZhvT4NGv-1i5nDJ5CE2IqY-qk_hnrZ5iyj7vts8Ou1Tp13hXXqKm3J4b_qonQ6s-ReIbVtqut7zAVRXZwa9e5hi0UVugu3a0N0ARoIcaVHNd6KZYHjXOKp-Ezzj3AjxBWPKn5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180f2b60aa.mp4?token=NIGUVtuYbOZz3x7aQhKUb2J51UQCvuVaDgSN99eJXwHquy12VGFpFJk2ftQC97sMR-0sj3uQitdn97h4TzkTS5eCskq1mHjJA-IjpA6NlxdJgfbELzg11TDCq9GMffRNNk8NNwIlkIK7pYkuN02KFpdNQeyNh1kPyuTjgI88EnQ1D5pDj5pnqC4tG4V_NEobzlXqORA4sf0G7kVZhvT4NGv-1i5nDJ5CE2IqY-qk_hnrZ5iyj7vts8Ou1Tp13hXXqKm3J4b_qonQ6s-ReIbVtqut7zAVRXZwa9e5hi0UVugu3a0N0ARoIcaVHNd6KZYHjXOKp-Ezzj3AjxBWPKn5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انقلاب برقی‌سازی خطوط ریلی در هند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452693" target="_blank">📅 16:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452692">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThiL1_6OaHzhVxSh3Ua7eF6YHLVaubR4l319IQ800EZTfQm1oxEgESmE2V7GJJO8SHfFJjjZZcqC4wl1aUsosSMZNdRNAr95jSF1rmIUIBFtsnbRL-SHRx_RLx113ye5KHOGmDFONMH9x2OUoCiOipqdNrwvj_PUrNBR03JNgUeBwqGw7wfhG3J5iAfmMpbU8QgBrJccYsusy1ZXlZfe1W2ViIY0VqBDh0avlf69c-QbXBy8FCs1khB5GC5Fcy6tc498bD5UuJCbP_Z5LPPrgqCu_CzuRi6_VVFhiRAtvyaZOSyMTeI78L8DMIuY0S0Dw_BD4P2wwGIWWLaaK4zJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنادر کویت و عربستان خالی شدند
🔹
پایش‌های ماهواره‌ای از کاهش سرعت بارگیری محموله‌ها در بنادر کویت و عربستان در ۶ ساعت گذشته حکایت دارد.
🔹
تصاویر جدید نیز نشان می‌دهد اسکله‌های نفتی الاحمدی در کویت و جبیل در عربستان تقریباً خالی شده‌اند.
🔹
به‌گفتهٔ یک تحلیل‌گر…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452692" target="_blank">📅 16:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452691">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">از میدان آزادی تا کربلا با پرچم «یالثارات الحسین» به نیابت رهبر شهید ایران
🔹
مصطفی زیبایی نژاد مدیر کل فرهنگی شهرداری تهران: امسال با پرچم‌های «یا لثارات الحسین» میادین شهر تهران و به نیابت و خونخواهی رهبر شهید ایران در اربعین و آیین جاماندگان شرکت خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/452691" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwhP9PK_8AtifsJpSPPbTermaHJp0skTFCuWxMeIAPRUYq_xp9MRYyL_iuAwzmbPlqVMA4807kQ-eVrYr7qNjxX7xSY76KXBtVGTQUjm9_YI4-ofLmi2gjU57Odv4bGANoeA9Zfxa8_U0M-w6geNbi4gXo9V48_WL3S40AVp9VwVHEHxD1yh1Tgg-_2DyHdKzDZXHtvJQTtVzz0nxfyFn4bSGDHTJ-rIQKTA5xn2xYCuOYkHgT_d2zoBmN1SlYLeIdhwfx_YGK-lAlyJjhwnCQWhCIqrsbJieT_yacd6NYaZcfLTofzNo2PdRHAdJnoa_jxfWVbfhL9N9LhN_dJTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/av_VfpEpG1sD_1AYzwtq9u9ARcialJvaE8rK7XVk3cQMpjgVaZrwG5RW6l0pmTZu8EZVFmnoYdJL-v8pHsU_90wPxlfRtAnM8r_kvfsLrjvJQYXbMQNwn01gnaW7faEKvPTgl-Hfx0BtCA_7n12gxZnEavo6IAijpmRSy0cQb5fhFT6MKX4j_OZmwKyFppMtnqxcgfmJZOe-qfdLje839iSSNPBVN-_AB1TqQ7mcsTEEHAJFJ6PZROD3Eljgzxn_a0SPqecEEIgb7FdSjio9lAuG1V7N5jPC_UHNJQ38qZ0Hq0TVVZ60FODkLyRx-V-YSRBhBE9ziRkJXc7rr78k8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/is17PTe9KvRkxyrBQWmfkLz33-PnCK5K43vFziOu7s9Tsp4AVpvlmumkQ556mrUSHD2dBZdIRGlyxsCQWA406Vetvy2LHhFEiBcTjRPtb45nP7guDy-UJGxokYFPiRjJ_glAf0X2I7g9bHGT7AHwG0X4GU34QoJdWUbaaIYf1nKkVBMxaogz-LJfSvrwSLM4lwKhlEincM5QV152_w_1WcL1b7BxTqPFam_vkv0bM-VEVgB63LCAPGi5sVCgjXE-7XyJL4CSWZjEvrX8JlUGA-pR_p6YQZd7fPJgaWl07Kj3wom0isJrookayhzHxOnS3eA6CCvzRkytojUz6hxdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1IaWuA9KIfvplK5H4Hqs0zifx2pAFuDz0OtOys68QB5CE4AgUZs4sXuutIh9F806opjPd2y16mTHIksrtBL-PjsrrAASS1hUsIl8hWYvjsL4rUw_XLEAzfClRFWunpPl-uh5Gh-hXzRlvStO_8wz9_9vsVlhU4bgl9CamPiRB7RdB_mwQkd-c5-B8LtSJ_rduYV3eOynmg7fvIWObbvsQPTRp-kYPAuWMjb7SpCK9ZeGrZcGmP-foKTSVawoz-ygxDVnOIo7F0rdlriSd9mdb_Nrnhy8YZZqdQo5YXeYaAPZQTNAUxPC9lxSiRCUhp061gyfYOGeVAPidBeJCEiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKIgItpGQ3UziCW2lC1m-krix9zY-iu41JYENSwq3TbBqqRiAxA5WsRVi05YLHZmU9w_FgOW7V57pJxnJvjz1F5uJw17YVPSt4IRjO6J-OMR_aidnLlDEoBt300gYDnQF-H2H-y3zhl9oXbuiKYDdDrD2nn28IJr13aP0X0pyXKoNHqStmNvesmPw6KjstQ7O3Sm7gEEe9drXX2pcZLJt2VoIfbtEdq1HVz7t7KJo8HxBdFjJVnEwoLdN5wYZnoPDHq_GnE-Fq3L9deZOCfF4cpbW588fmxnpkRzFNJnJQFK0O3pV9ou0UQhIU63TYXlgON37KE_B9Tb2LloMu41FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WwxK090SLWq12Bp2RxQbWYSf0oldOI_dxVsCkHXLHvAHpB5EEwXkq8r-U_DrAQdPytbkI1DF8_Q6WfzMFLoSjQAHrdBT1zC5_O8amW53bU1zv_JJNBzIR7Fs9kY2N4ryLhkNfhrQg8r809w7atNS5vPd5cok1gUg8prhCLdoF4GE9br_98Tcr7b59agV6P_fj52WPGAMA8YiIw32T7AaUw17hSt2edYHGErr3c0x2pVg2I6R10YvH-v7BlQeGcRyOsyxhu20MfoTTX8rLaLF9qcZP51EEC8CwVaILi0aPoWNcBEKnPF2wnwDLVP31iwgD3XK1D4rhxEa0u-tLDv6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MkWTqb_gTH7RDvvNtkGb7ZKAzTRVVHn8IoUV8dOqzRneJsPbFmjxxWokrhTXQkvafeCBDDgjSR6_FSlnB4L19rxSAuUBzYXWhhjWUmcuKeYKQZR4N5rsfVtW4YM-2y3-t2b2j2l00fvdHFYUqP__WRlrOoD5u2dQma-uTkOrU6Rlof-YdnxvqNmNC6PLrV3bm5N2_OOJCOnYiQG_KW4RMBb6Z3YYj-yOndxbZBu3R4PlXP6r94mWn04WMxc_XfdxAfhCG83emKaBmuQfBf1jDUEmBE0SBnLeA8abvCRFIw3n--tYYlu_1Y7OxlSVD-7SeRLU-to8DcWZFA-PIGwaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sU8p0RpuaqL--UD9ToJw0_BgkKIzUpaDBSOZAeSZXNDHTG3-HV-5HfLX3gZFU1ZtJF2V3_e32gvyhDOUGyEmMKlFuXyB4sKw3WN_cLsR56m5DmDlpMrUFIYp20Txy5cu6B_QFsJrwP4pnvZ95Y3ymqZGUYydwwNtYvUdedrJJbJFLEpEeaaVIVT1ZP1Ux9fHXt6s9Evs3gow9aWkbTWg9DAeJNFL-W480WZnLf4TMZHI1DGAjOlq41qnsGcaxyDiz8BSsD4gAKoymkRJz43ywT1zVg4c-5g6fHvzXY_h649tSgjKtLDCCZOv4ZUblY0w-zCFYGKR-5EPLRtsPzM40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNb5u9_V6ZyyjNgyxkHbFKo_OVJqLhdzzBwXxBxiG7NCNH2iXtqTJaXIkxtCX12Qnbsb4uNc_20QVErObiIiO7iUHDCuCxFkIhzbrJA-BuT9ziKR7r_V26KaOWO2k4ZeCgLqJyqbmBwyA4pmB4RkklzPjNVtvW_EZ1f6JkSNbBV4YAdp8TuqS1MRb_nyVmKDcJHyv4MV6R95qQbSTmLJ0tiAcmPmbbypFc45AYs2sUTbZ5OjTuOs-FfFpBUeO4DgoKEBm7lmOEGUhusiUVGyfR5oeLvLJqpgthoANLgyZSqEWyYm8MhpcyNPCds8RxSTUOoj-azdUmShN7lCL4A8SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش تصویری محفل شعر شاعران و نویسندگان ایرانی در اربعین به نیابت از رهبر شهید انقلاب</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/452682" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک توسعه صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJsmAjGRY4hzLVAQreMbqBNF1GrDEpx4Atch93od5nOf82PLy4TFb3Q9oaeA4DvDMm7ARxx_wWm4xnKcuAkIKzbS2i9wJFZUzniyJNcxOWwQPJiKardHFP-IVFeIgrmeTKbGsabuDTpykGu7TuxllQ4etyHxdNBSMy83y9AlyWDxpA52TvELrrzV1LfUyDJAOqxyAddxgkOXEdC3wvN24TrNSZOBg-0QXgBda4mKuQ0LiExTm6CG2NwAsaOnXJTZ5-DSKpow3YHRJGsqHcbAAm-JUdEfsAk5glpvdw9UxYcy6MLrSxyBgH1nfdhor9d_hxfnRaHNMj4SCw4klvY1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↗️
افزایش
حمایت از تولید در بانک توسعه صادرات ایران
🟢
بانک توسعه صادرات ایران در راستای افزایش حمایت از تولید و تقویت بنگاه‌های اقتصادی، عملکرد موفقی را در سه ماه نخست سال ۱۴۰۵ به ثبت رساند
🔹
گشایش اعتبارات اسنادی داخلی این بانک در سه ماهه نخست امسال نسبت به مدت مشابه سال قبل ۲۰ درصد رشد کرد.
🔹
این بانک در سه ماه اول امسال موفق به گشایش اعتبار اسنادی داخلی به مبلغ ۵۶ هزار و ۶۲۷ میلیارد ریال شد.
🔹
این رقم در مدت مشابه سال ۱۴۰۴ معادل ۴۷ هزار و ۱۰۰ میلیارد ریال بوده است.
✅
این رشد نشان‌دهنده عزم جدی بانک توسعه صادرات ایران برای گسترش خدمت‌رسانی به تجار، بازرگانان و فعالان حوزه تولید است.
🔗
مشروح خبر
🟢
سایت
|
تلگرام
|
بله
|
روبیکا
|
اینستاگرام
|
آپارات</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/452681" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/452680" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDzIvWZIfZKl8ahqwqlxrdzVYYNPm6F3SsI_wSWMp69A1CIKQgohfPqhOxFd47BW-LIpIu8bhb9masiNFO1Eh_lsMoCvc5RzVMHzQlpMevAPAzb-9fDYFf_XrMtGhFrB5dMCYk9jEdXGaV4DPT4-QM1MApXu1WPUwOzgMhEDXXIoAg3Hxaj_iMu_XBXAIpgLT8SkwgRPvbO2Bgn7fQAhqdxFjqOYFB_FQ3CkHHT7ZqiYJ4hwMatUFs6IYsWp_X6tjISUhqmVYdDThr5z6i_x6kpv9qS1FG2Tq5nVBm2iRFAop6dyr6i_e2AKDs0lBypO2woV77HY9z8rVOcNfeXvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حج و زیارت: تا غروب دیروز، یک میلیون و ۷۰۰ هزار نفر برای حضور در مراسم اربعین در سامانۀ سماح ثبت‌نام کرده‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/452679" target="_blank">📅 16:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4cd8f6ff.mp4?token=jCGaGtlJDGdjkroiGiNU7Y-o0HAITZAg5KGuIKL5leFAm-8MQ7Y4RDwdjvZvgIVToJcjNL7xhVJ4cGCVEYBrEBS99roBL779PjO-YRtMBDIyTgz_lazP3bWvk1Z0CJ_HYWTqQVB1LjY-13I-1gc5uetOoTypmx1TWNdCVIh91tk8_A0Wb46QFcpLcnLCa-XaUiqEMs_BCgk87km79WmuFvb4q1CIviASI6YaQ3V8tERRpYWvOdeSgShIxzDXezh_eAlOLjmlgUCdssBT7_4dNMPTaWRkNlcHkb21kMbG9lqltzUD7cAp0BHFLgop3_XxgrpT3ZxBMuJDWpAnG72Xbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4cd8f6ff.mp4?token=jCGaGtlJDGdjkroiGiNU7Y-o0HAITZAg5KGuIKL5leFAm-8MQ7Y4RDwdjvZvgIVToJcjNL7xhVJ4cGCVEYBrEBS99roBL779PjO-YRtMBDIyTgz_lazP3bWvk1Z0CJ_HYWTqQVB1LjY-13I-1gc5uetOoTypmx1TWNdCVIh91tk8_A0Wb46QFcpLcnLCa-XaUiqEMs_BCgk87km79WmuFvb4q1CIviASI6YaQ3V8tERRpYWvOdeSgShIxzDXezh_eAlOLjmlgUCdssBT7_4dNMPTaWRkNlcHkb21kMbG9lqltzUD7cAp0BHFLgop3_XxgrpT3ZxBMuJDWpAnG72Xbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی: دود غلیظی مناطق وسیعی در اطراف پالایشگاه نفت جازان عربستان را فرا گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/452678" target="_blank">📅 16:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452677">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۳ محصول جدید لبنی یارانه‌دار شد
🔹
کارگروه امنیت غذایی ۳ محصول جدید شامل شیر بطری یک‌لیتری ۲.۵ درصد چربی، شیر نایلونی ۹۰۰ گرمی ۲.۵ درصد چربی و ماست دبه‌ای ۲ کیلوگرمی ۲.۵ درصد چربی را به فهرست کالاهای یارانۀ لبنیات اضافه کرد.
🔹
با این تصمیم، تعداد اقلام لبنی یارانه‌ای از ۴ به ۷ قلم افزایش یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/452677" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452676">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
سپاه: دو نفتکش متخلف با قصد عبور از مسیر ناایمن جنوب تنگۀ هرمز، بر اثر انفجار دچار حریق گسترده شده و متوقف شدند
🔹
ساعتی پیش دو نفتکش متخلف که با فریب ارتش کودک‌کش آمریکا قصد عبور از مسیر خطرناک جنوب تنگۀ هرمز را داشتند، بر اثر انفجار دچار حریق گسترده شده…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452676" target="_blank">📅 15:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452675">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYQnNXpUiZEPI5fHUKMk-9AUdqH0LdsDjehBOPrk5PGkBXhkXnfPn3odwyOPiw8LoxKJQXMIItf3vJxFPpA3BzsVmV9Mqt2e2TRnGY-0O7njqH7CqnzGwQKbHuvY8zKnKJuIe4kDvqKd59U4SQQmIS76WHOM-PIiCpIrj8lUvv_AyvvV6D1QxTSI2nwIyIqiZ0z0-lEanu6s8v3OADQiUch2Qi3PWJEpYCbAwxk_m1vTM78qJDsU4oQRr7pmNJws0dSLOAhqEyGgJruuOJNlooraMTkGOS354hBkGOfRYKr3h-nEOvPJRTdAFfoLUzDiai3YwVGSkFG8KASg1NzWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد سنگین در جاده‌های مرزی تا ۴۸ ساعت آینده
🔹
راهور فراجا: تردد زائران در مسیرهای منتهی به مرزهای اربعینی به اوج رسیده و این حجم تا ۴۸ ساعت آینده ادامه دارد؛ بیش‌از ۶۰ درصد زائران، مرز مهران را برای خروج از کشور انتخاب کرده‌اند.
🔹
تاکنون تنها ۲۰ نفر از زائران در جاده‌های کشور مصدوم شده‌اند و خوشبختانه هیچ مورد فوتی ناشی از تصادفات در سفرهای اربعین گزارش نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452675" target="_blank">📅 15:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPPyWK-p8pAvsroTiqvvrOvHK0qN4pWp7aBJAjSZs5Okd1x8UoVR_vDpHcpg81aHni3izcDBD5zU9qUmGn4GJWMjLIP0JFFDqack8hqMa--KZESWT4nUvQ9RVJbapXGMXCd49SV9D8GPtxGO2hFnfstir-WqGe62zHFTt9cqttvlw-2dGlgzDetLaSHdldVXunTE3qt6A45DvMBv0McJAQk973clr3klQ-2wg6ACnG9VVUVoidF12wycVpfhLaQorJyeC4_A33KEM4ko9QfXGwNX06XpaFTNWG1c8GT574zmTdOEy6-DE8qio_d2ym23Ad8dwwOsWDjFm9kruig33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nraOxyXEE0BDUZAJjwkPzyqAJx6xaM5BbByq2yFW2-MtaitRBHgOJ_2hPQhCD6PaoUTZrOE9K9-zxbsqJpqbhpHm5FqwrrvPG7xoi2yFiX3Vyrkj9hnJx6ALHjK6PpROPY6VQ6raU0-9u7B-tVPCfGBpjRtj7HOffdZW4c4YXulEbplFELch09nTJmCrDcLij-YjNXrtUNo57MH40cdjuNRzwN7eZfar4Tb7ce3Kbzj3Hw-ZRQbRPiVK8uKaVENccfQoLu_OtXsisRqivtUyXFSD0Y2esuL-lyEEojdhW87MBtS3PWR_m7iZkpqV3qTGs_q3YFvZQAFkLBWhgWYVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTG7d30sJGcA4hOp0MA0p_zypW1MSTGtuNv56ia8lUKegsLhcD2qzTEDOClKkzuq6I3m7RpnkmkGEiX5WATOiLAxaCDT4sxrWJfBl-_rotkEY6F5t19StopsS4CcFbGFBRLUNU-VvDZERMnEKX6pUzUdW8qUHHLjZHKvCsYs2kek4A0iKK6solYXxDskxM5g5znaFkwnudUDOeMIBCA8hici7cA7t2IKbq1k1Se3unAPpMfL6P9Du7jkesAcrfSKjldyJmaJYc8poltiNVWA3-RST0EyPzRZwqdpGWeSceomdM6wIcUtRJL5pu7esjQEQoyk2XxuS-BWS04cE20hqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpZ9ErKld7NOezrNcYPnTCSQCwpd8-iqlZLAa4EME7GxC64HXrhT85NJFk9KbbBGByeA3Em7wZz8-0MAE4oRTowvuC72KWXxW4-GwyXqnwTrCkH8MFa2OsLbe5ygtSw_8jqXXT4VP-6T5pHDKkmA6HFBXnq1yXqSw3MQuhYiVyAUx4sUejOcBa0EydGg3x36mXB7zEbbs9Sx4E8SA0shAvlnjiaE5rgfXPcgAHtBc80p-TNbzm6bLKWeTwI5Rtb9Jdc6UG396mZWUV_ax7z2Hdv4A-H36LBcOaC1eAqYCk7rmI0M1VMEEjq3IQ-Cp4DjXxUL1DOo9ru7bQ4N09CddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1agOuVVzmOPrqpGVbFNg5ybLQhRvg9wN6IvypXM3sdnJ3gFNQh5qUoTd7seobn1fjcxKkMDlgy_1lfs3OwnBENfgXRRa8rqoNH3bqltMIJQPxOG9fL-1N8wuN7hlwG8t8YXuZ6ICiqeoP9BTV-siIqUAqpO0jaMkmxm7uKY24F80qbI6ZherWkczNqBYwn2fQHIRAHIGNdWfPNi5GCTSNmRlTm-LzpR0epY1UrWkZXWd4VB-ehoO2hlsYVEU-fuZyJUEtZZUxx3-Frg_mJqapy-wZq0fGwHiXJtxMv0dcY937jAX_GhQkLFIjA2n-s45o5TkSBgYrWkFgPWDxtL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8J9bJNF8-N1iSnUWtugpbBDjwSndXJjtgDfH03WpV7U9kPDopaH1RqHlKazqHpVoud9IAtby2KpkkiT3y4fSNde7ZV27CLlm4NXDWE0RP4rEi_5K8Su-wvBjBym7WDDxGXfc2TbIl1KyPKRyskcmaUj4HNuxJlh4uwXsXXp6-mt6_o1QW8qW0gP2WcC8LFw_RI6ZhlFTh261YLwh3xtBqmX28XVWMtL7oBCkizBSRjv50Y4brbYe4lsYBeDDK6X8-BKLunQBNqQolge7Zr_SCIRc7V3kkpn3V-t6Xpu0X6BMYOLapyrlmuHBmJBw7b-VznKTuo9R-HpazdYfJFeTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFFkSi4jsmwpd0F3ceSb_rnmRWTm3uVZG-ml_-yBGhuJyo-nZ8yMKiPdWDSALr3V7deSofKQ5971dVBjD11zeXc_m9QEgXmWfvM4fR96Yacxjmvyos6q7V9KHwWFMMANcaajsXWTGQewxGzPxeuckmsQH6TUqsHwPIJkDjDQiK8M3XumGLgSSmTSsq6_lTUQJ-mrbNZE_XmyYM2XYBtnFLn8RFkzvJpfv_JLWodzi5eeTkjxBuD4A8cDgPOaCIpBMhpEJ260Nw0wvvQ5K8-Wk5e-LI-htZPLZCbzrXXmRypAzVeLuoXjV185GuSjUtd2Umt29YfDBmcgeoFhLQ4YpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میزبانی گرم عراقی‌ها از زائران ایرانی در منذریه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/452668" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY0zL2r-0wPeFN874mpx-e_D7KHXp1Tf3MnCQA5nIgNIGNk2A0B9tpJbZF33pc3CN5AjPjBVwjCXsTIOaP1vBhyegdj0M1UWh6b1Kg9tVoHqgJmY1mL7-ksntGJq-cjYpLQaogZ7O1OgXvrGM_sklgAYv9mpXy2o7R3UsagPhx96YYzVxh6mAVlTzzhbgPsPi49tgKjcadVstJTP2GB_FU1d_a9we3BS3WyLc9DLgCybKLG-p69A3UeB1H8d4rEBwiiMu6_P3VWF1Gn2EFdT0E56wpNXpFbSaPvggAqAZ-5zsp0VlnfKYlrOzKkBvC3M4Tx01b2ysIgPrj12MgWybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری خوزستان: ظرفیت پارکینگ‌های مرز چذابه به ۱۰۰ هکتار افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/452667" target="_blank">📅 15:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452666">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896bc839db.mp4?token=Gvzm9klzkSDFDkgYfAH-Pc_pFl9-B1LaKXiuWBwc5-xZpNQFL465Q9kJpHAOvNLYYW48YEa1mMTiIJ6GWjQTCqjttfBw_6yEkqFlrfdta1_f7vHxqsIgMpgAVmHw6OUSKDKgS6gvPwmdjyet3HjCA9Dsxn1NTMEBdYbwWJzxVpw34lEWP0kFkDQoP3xYGpgqRuLoDhDO559YHJ-qv_SBmt-IqSxY3LZC6xqq55A57MopdRuxUhRoHywuh810OmrZYK9UKsQGpFKDS0jy7SK6m0bw-pqcFKaQZPnLzwKrdEDt3xusPXog8hcXMs3fftXV1S3psz3kn0jDfFmwz81zDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896bc839db.mp4?token=Gvzm9klzkSDFDkgYfAH-Pc_pFl9-B1LaKXiuWBwc5-xZpNQFL465Q9kJpHAOvNLYYW48YEa1mMTiIJ6GWjQTCqjttfBw_6yEkqFlrfdta1_f7vHxqsIgMpgAVmHw6OUSKDKgS6gvPwmdjyet3HjCA9Dsxn1NTMEBdYbwWJzxVpw34lEWP0kFkDQoP3xYGpgqRuLoDhDO559YHJ-qv_SBmt-IqSxY3LZC6xqq55A57MopdRuxUhRoHywuh810OmrZYK9UKsQGpFKDS0jy7SK6m0bw-pqcFKaQZPnLzwKrdEDt3xusPXog8hcXMs3fftXV1S3psz3kn0jDfFmwz81zDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تشییع پیکر زنده‌یاد اکبر عبدی  عکس: محمدحسن اصلانی @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/452666" target="_blank">📅 15:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452665">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exIoewVM3rP-RLrnAKfBcWQafM31bWfMxg3Vr5Z9TbM5NlIyQJeHcm6UW5hoZzTQimgopNbT3dx9GrWqc0kyJo16CMXZLriU4fCDNFX5Ku6A1kMCqOnS07miPJj7S0NqDrKU7-4XpnkfWv7cMaYiZMcmkPxThMeFnf4Z0G7aEQBVI9BGupEPYwMA_pGmtaUOXWj8VzFd-R66Q3QMa1dgA6lNnc-BBmax4fZBe_isMm5pVGM5evhBqQosTuvr8iAJG1g4RKtU8Vd95W6MzalU23fEy68TN75cQN403K7IJ4xyy9nol-veiOzku3HV_ei-IHtsRQp-sdgH7V5399qomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از وقوع یک حادثهٔ دریایی در جنوب دریای سرخ خبر می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452665" target="_blank">📅 14:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c97f68de8.mp4?token=XaKzszxjLh7T0C_humIv2qQIc1MQA1b4nDJoe-p6kTaUBufGGIWmzHVh42hjZA_yl9-1CZlue3Bf5M6MevHPp0s7dVhd6Ev8p0ex9nnaqwrZ1w_s_5IvXcyEPiOYDWmEuK16djgEKx2yDPs6ACb9iaPXRnFhoYj3E-jP3Kju2qEE33FHureA0xyOLxyTChCOQ7GFdimFPqcX99LU8IaAvKhDKrycpg2gMgjADtpZZNXkcaHk2Y7BJgwMt2KXDp3LpLbzSuo9oMkKwissly2oAWABufQQvhWniW-lBr8jDxzZIowX9wCCpQRBjX8l-tQgX1BSJobXitntgWCxLoJzNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c97f68de8.mp4?token=XaKzszxjLh7T0C_humIv2qQIc1MQA1b4nDJoe-p6kTaUBufGGIWmzHVh42hjZA_yl9-1CZlue3Bf5M6MevHPp0s7dVhd6Ev8p0ex9nnaqwrZ1w_s_5IvXcyEPiOYDWmEuK16djgEKx2yDPs6ACb9iaPXRnFhoYj3E-jP3Kju2qEE33FHureA0xyOLxyTChCOQ7GFdimFPqcX99LU8IaAvKhDKrycpg2gMgjADtpZZNXkcaHk2Y7BJgwMt2KXDp3LpLbzSuo9oMkKwissly2oAWABufQQvhWniW-lBr8jDxzZIowX9wCCpQRBjX8l-tQgX1BSJobXitntgWCxLoJzNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف‌قراردادن کشتی ترکیه‌ای توسط روسیه
🔹
یک کشتی باری تحت مدیریت یک شرکت ترکیه‌ای در نزدیکی منطقهٔ اودسا در سواحل دریای سیاه اوکراین هدف حملهٔ یک پهپاد روسی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452664" target="_blank">📅 14:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452663">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzAT0bFWWD4KixtC2gzT_v0sQCJzhm_2buSNQXCm8d3WThD63CwdhU0Bikyh9JyyUlFVfFJtjJq_cbXxTWtF1QDlpP44xsHQBgOPnmzYrL84xu12mPyGI58HBPACOWASsxEPQH0G6ID7S3D6c774uuCOdZwky9QNdi0wHQ0n2DI1YA1Wfa6MsEuQM8-yzcIssPdIvIAWd89MvuqkFpz_rPayreTkGtaRhLYe1-mJmZsjV8KZIrPM578syIxlnNUrQH_BvURzMCxNtiZyzCJl0PNry2U0CNV2c4jP6svkOZbydKFJvnhKlR36Vtgtc6a13v9AZ3C0J87ceFuENCFApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنادر کویت و عربستان خالی شدند
🔹
پایش‌های ماهواره‌ای از کاهش سرعت بارگیری محموله‌ها در بنادر کویت و عربستان در ۶ ساعت گذشته حکایت دارد.
🔹
تصاویر جدید نیز نشان می‌دهد اسکله‌های نفتی الاحمدی در کویت و جبیل در عربستان تقریباً خالی شده‌اند.
🔹
به‌گفتهٔ یک تحلیل‌گر تصاویر ماهواره‌ای، اسکله‌ها به‌تدریج خلوت‌تر شده‌اند و تعداد کشتی‌های بارگیری‌شده‌ای هم روزبه‌روز کمتر می‌شود.
🔸
این وضعیت پس از حملات یمن به تأسیسات نفتی آرامکو و بندر ینبع و همچنین حملات ایران به مراکز پشتیبانی آمریکا در کویت مشاهده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452663" target="_blank">📅 14:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1b66c659.mp4?token=dQ6tQHKm7Nc8SVXAYA26NO_LZF8d8czpoBFrrmnYW1sFtTDKFnRT2dHiWxjav8ORnuWlZy-aOTiPkcE-Ny4ZdLCbWqMcX0wPZdjuvS935Ub6l9CufcEWRP106ZECPwXeDWYJOewigE0DSdqP7fZVTlAmfqoyBRe6O5KRd9owJSCpw2oAwOywkbyjcEfpkhu2Yng3LnEA0iFJhYatLculXwuiRklnAYv6QSn1P_KRTTNXeUnjD0kapWedUgaU5jrbiPLDx32FjENrHKEa6KB5vZMxyzyRAbpeS6OyA9B1yUswhqFtAcR9q-q_5P-aqjpR1SlNhcOLrRGiwj7tIbqj2CBaTPvkLLxA9gqB9kOVCB4Globhl4Al6oMT082KWGtfWKPjKkR-SNlf29wkJ7iDN6v3tRDlEe7P4iuZlBPgD-vE_h_nTArwPIstXA499rYFI02cZEh9AoxjzaGfGRPYv_3q4DQSaX1kW3Sw3naiMciwBZVxrG5xhZlIMRroF_JAfnzk_Ml_NICneiyNO2CpM-LHn9Jaqjr6BLtr3SiqXgLcIAhtLqgzwDYbNbyIRiXT6IShG8SZYPRPwwBuauSoikCZ_TQUwL8lvCXZFWZ1mirtn2mS9Lgt7lGdEvwqjEuW2M-MkY8Pkl_dvrewzC6b-biF6pkUL5wzR5aIrSqIQGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1b66c659.mp4?token=dQ6tQHKm7Nc8SVXAYA26NO_LZF8d8czpoBFrrmnYW1sFtTDKFnRT2dHiWxjav8ORnuWlZy-aOTiPkcE-Ny4ZdLCbWqMcX0wPZdjuvS935Ub6l9CufcEWRP106ZECPwXeDWYJOewigE0DSdqP7fZVTlAmfqoyBRe6O5KRd9owJSCpw2oAwOywkbyjcEfpkhu2Yng3LnEA0iFJhYatLculXwuiRklnAYv6QSn1P_KRTTNXeUnjD0kapWedUgaU5jrbiPLDx32FjENrHKEa6KB5vZMxyzyRAbpeS6OyA9B1yUswhqFtAcR9q-q_5P-aqjpR1SlNhcOLrRGiwj7tIbqj2CBaTPvkLLxA9gqB9kOVCB4Globhl4Al6oMT082KWGtfWKPjKkR-SNlf29wkJ7iDN6v3tRDlEe7P4iuZlBPgD-vE_h_nTArwPIstXA499rYFI02cZEh9AoxjzaGfGRPYv_3q4DQSaX1kW3Sw3naiMciwBZVxrG5xhZlIMRroF_JAfnzk_Ml_NICneiyNO2CpM-LHn9Jaqjr6BLtr3SiqXgLcIAhtLqgzwDYbNbyIRiXT6IShG8SZYPRPwwBuauSoikCZ_TQUwL8lvCXZFWZ1mirtn2mS9Lgt7lGdEvwqjEuW2M-MkY8Pkl_dvrewzC6b-biF6pkUL5wzR5aIrSqIQGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان کشتی‌های متوقف‌شده در تنگهٔ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452662" target="_blank">📅 14:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7f0c9700.mp4?token=tyLFXzDvhpOWSGzqKkyGgYI0nd9nxdEwDBu2uzHk1TmECMSziWRYoIcDpDLjCJPXFfoVcFHoz2586P68Gj3jUa_w0TJem2neKTunkyq00HoxZYBKCZ0bUGuH-95DPWMHbFt5Zq-FId04fSz_OgYC5NbzO70QOIWskge02yKMwred_BQ2XQ4-oZFRHoRV1tg4FH7IjomMXBpSevSbw7O0sRfoLE4RNme5h6AZSJgic6Qc4H60HPXlVuD2I62lvVhFuEOsFucv2MKNzvYN6YWVmMhjUScbe9I0m4xyMeGajF5tLd0vcoGbW4MstBrepT00hBTyM5z_iSCd2_4sDkw4Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7f0c9700.mp4?token=tyLFXzDvhpOWSGzqKkyGgYI0nd9nxdEwDBu2uzHk1TmECMSziWRYoIcDpDLjCJPXFfoVcFHoz2586P68Gj3jUa_w0TJem2neKTunkyq00HoxZYBKCZ0bUGuH-95DPWMHbFt5Zq-FId04fSz_OgYC5NbzO70QOIWskge02yKMwred_BQ2XQ4-oZFRHoRV1tg4FH7IjomMXBpSevSbw7O0sRfoLE4RNme5h6AZSJgic6Qc4H60HPXlVuD2I62lvVhFuEOsFucv2MKNzvYN6YWVmMhjUScbe9I0m4xyMeGajF5tLd0vcoGbW4MstBrepT00hBTyM5z_iSCd2_4sDkw4Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برق صرفه‌جویی‌شده راهی جنوب می‌شود
🔹
در پی ثبت پویش حذف خاموشی برق در
هرمزگان، خوزستان، بوشهر و سیستان‌ و بلوچستان
، مطالبه‌ای عمومی مطرح شده است که با توجه به گرمای شدید این مناطق، حتی در صورت افزایش چنددقیقه‌ای خاموشی در سایر استان‌ها، برق این چهار استان قطع نشود؛ مطالبه‌ای که
وزیر نیرو
نیز در واکنش به آن اعلام کرده برق صرفه‌جویی‌شده در دیگر نقاط کشور به مناطق جنوبی اختصاص می‌یابد.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/452661" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452660">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfba51605.mp4?token=qMtry7gfnniVnEilkmAjKepCuUVKyDRruGxHpn-f-B7AvQIHOToXbAwQA_pzayTf_4ggKTGgHlSTRf-Uy6vBJP0fXOCDHh3EggXoeU2VVTudVIPePq8pZf_rcl58eljguylA1hi2gMbGFSPrDrfR7MbPAv7drdujcgVe20BppXq8ZpK1gDx7YuWHo3JBWTJHHpRntLnJ_3fCmVakMGSnPStwZLR1EwuPp5xNUSe9jqv8X5_RGd7rwfj-MpcB7zQ-ra4jM2JxkEeqJ7c6EDl3SpAU4IRUbkYUUrZ_ERTHCiwR_ihcEc15TH4SznjcU0u5jGReEoDWFBW6MIOq1oNMjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfba51605.mp4?token=qMtry7gfnniVnEilkmAjKepCuUVKyDRruGxHpn-f-B7AvQIHOToXbAwQA_pzayTf_4ggKTGgHlSTRf-Uy6vBJP0fXOCDHh3EggXoeU2VVTudVIPePq8pZf_rcl58eljguylA1hi2gMbGFSPrDrfR7MbPAv7drdujcgVe20BppXq8ZpK1gDx7YuWHo3JBWTJHHpRntLnJ_3fCmVakMGSnPStwZLR1EwuPp5xNUSe9jqv8X5_RGd7rwfj-MpcB7zQ-ra4jM2JxkEeqJ7c6EDl3SpAU4IRUbkYUUrZ_ERTHCiwR_ihcEc15TH4SznjcU0u5jGReEoDWFBW6MIOq1oNMjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در جلسۀ علنی وبیناری امروز مجلس، کلیات لایحۀ مقابله با جنایت بین‌المللی با ۱۷۰ رای موافق تصویب شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/452660" target="_blank">📅 14:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452659">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/johQJLECn_hjRcgXwZFaC4g7f6rU9xMUd1BExVyyF524ovElwCRqQGvMDk6gbKgGX_HjgbOlkEW-ZShiCK-RKoTmexJrXLhlvSTbOWwlgaxr2T6w06328ebfym7WAXGAuqlEdF0IrwhAVEpsSOqbpGDtQotXgQt6Gss7HnR5PCrol2q_Tapy7BrmPD7IFjRXrxf78UUiiJtOxSIqq0uXN4w2FErFRyL9M8IpwvT_piGYNfMz8i-KC8Hn94TB9PkyTuyKu25B23Qlrc9IbfVW4dubwD4jfDdWqOGgHRrVG50vg_p4IvZZlYC9cQYvFOaN0PfJ2nz_BqGbZkHR_7P_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: مجازی‌شدن مدارس از مهر شایعه است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/452659" target="_blank">📅 14:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452658">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXCNmkTJ3QyaKHXnYwqRuUDi601yUHG8YGB4NHR1dui8z873XpRx5gi3tRUybAhaEQRdcK_WeAvoOLmOE32ozWPcFVGGgfOyWPzDu12HB-vmJnuVsXK6C0pXciiiCNVvZ-e6tMh8hmpXeZ7XzOI1sDjmvnB_4m7fSaoQ-1JSic_Q1gy0UIbn3jwDGzM-X5EsKq-ZttfACUimod60v_TPYHuSlkg3R5I8bXfzXXRBhLnU-WaL8qQ_kqD545UYmU7BzwTsWbBwo4k-Jhe1CvyKtl19CYgLjVaUA7AJqOGTeSLHtiEpuw-OsIx0q1SJ7qNZi5Uf1DQvXsfmzaSceRCY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باند فروش دینار جعلی متلاشی شد
🔹
پلیس آگاهی تهران از دستگیری اعضای یک باند چهار نفره خبر داد که با فروش دینار جعلی از زائران اربعین کلاهبرداری می‌کردند.
🔹
در بازرسی از مخفیگاه متهمان، ۵ هزار و ۳۵۰ قطعه دینار جعلی کشف شد.
🔹
پلیس از زائران خواست ارز مورد نیاز خود را فقط از بانک‌ها و صرافی‌های مجاز تهیه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/452658" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3d6a73b6f.mp4?token=RHavkvbtEhzmdiNeCxal_BBkVSm3asAj51jvpRz_-taXsuVjp83jPWL4qwrALzY5wfguJq9s1oNsj0W8ApwnX1ppP3gjDq4Ag5OwOjL5Yy71esEN61BPmXPa0EdXrR0TB3JnTeE2EBRHVnJDSw9S7UtDSefKdpM2ivnoB4DPhXn6kLFD4ebYsBPAqJd-TlEJuOmu_053KIBBKxJrcPFziqqHtZOvDcJJH47kgyrRF3fS70liKBQ6b3ytvI1ZhW-JYf5XEjLwoZdw4z8mLiPxi0FkdBF4r0_-9Mj7-ajl-SZJnw8eMt8l15LUttb59ruMiDTonkCGWaKIqKHV1s82IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3d6a73b6f.mp4?token=RHavkvbtEhzmdiNeCxal_BBkVSm3asAj51jvpRz_-taXsuVjp83jPWL4qwrALzY5wfguJq9s1oNsj0W8ApwnX1ppP3gjDq4Ag5OwOjL5Yy71esEN61BPmXPa0EdXrR0TB3JnTeE2EBRHVnJDSw9S7UtDSefKdpM2ivnoB4DPhXn6kLFD4ebYsBPAqJd-TlEJuOmu_053KIBBKxJrcPFziqqHtZOvDcJJH47kgyrRF3fS70liKBQ6b3ytvI1ZhW-JYf5XEjLwoZdw4z8mLiPxi0FkdBF4r0_-9Mj7-ajl-SZJnw8eMt8l15LUttb59ruMiDTonkCGWaKIqKHV1s82IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد: نظامات حاکم بر تنگۀ هرمز به شرایط قبل از جنگ بازنخواهد گشت
🔹
نایب‌رئیس مجلس: هر نقطه‌ای که مبداء تجاوز به کشور و خاک ما باشد، قطعاً هدف مشروع نیروهای مسلح ما خواهد بود و اقدام نابخردانه دولت اوکراین بی‌جواب نخواهد ماند.
🔹
به رئیس‌جمهور متوهم آمریکا هم توصیه می‌کنیم این پنبه را از گوش خود بیرون کند و تا قبل از اینکه شکستی سنگین‌تر از شکست قبلی را تجربه کند، منطقه‌ای که هزاران سال است محل زندگی ما و نیاکان ما بوده را ترک کند.
🔹
مردم آمریکا پیش از آنکه سربازان آمریکایی با تابوت به کشورشان بازگردند، رئیس‌جمهور سفاک خود را کنترل کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/452657" target="_blank">📅 14:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452656">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXHW0dN3gKLgqmolphpkoI-HF7aDp2RsZjVHx2pk7qpy-QvUEuaa3krSI_Cje-wbW6rZLqMo5vFxt5iDiBGJslBil2AiXWDZ5F5M-x_Y-u8PFNanmLZwEqvio6kCsq4SbkTQZdsgvq5tD2HdovwurHJaBb2yFxICBjzpKowkdTmFKc98Fd-bCAsrYbRiK2STNi8tnqpnkG_73Mw5dLntG7NucUw_R3x84ctzaoKnbfoDpcBks56pp7FKWo8OTd9HRzuOeubLQ-1tJhtBLX54L7_80bGmUCF7GLUyPR6yRPSNB3SeLMsmAPcoN4F9aZp1aIj1Yc4jYWXDvOQiA4rmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دست پیمانکار را از حقوق کارمندان شرکتی کوتاه کرد
🔹
رئیس سازمان اداری و استخدامی: دولت شیوۀ پرداخت حقوق کارکنان شرکتی را تغییر می‌دهد و از این پس حقوق، حق بیمه و مالیات این کارکنان به‌صورت مستقیم از سوی دستگاه‌های اجرایی پرداخت خواهد شد.
🔹
با اجرای این طرح، سود شرکت‌های پیمانکاری از حدود ۱۰ درصد به حداکثر ۳ درصد کاهش می‌یابد و نقش آن‌ها صرفاً به تأمین نیرو و مدیریت قرارداد محدود خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452656" target="_blank">📅 13:57 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
