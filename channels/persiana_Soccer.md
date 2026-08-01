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
<img src="https://cdn4.telesco.pe/file/Yu8IiDtjtDBz6CJlqh-OZ8aUXrfjmQRoYRmSET3mXIxa2rCI167tw8Ef6aQF4UmU1-Bousy9mx0ZU1-PrzuNJAkTzUq-A9CajtVP_Mq-QOonHJ01_YfljT34rOWNUZ_KyNx3kUnx4jM6l3RpOcN48FkdxArvsoK-ipeebp6-Y5UI5DG4AFLVXX5d3f3yuRJSHQcedTjRGhOJa9VzW7NpFIt-ojkG2SKbcfNqfGfvGZcXcfuCysB-vEOdO-xe63Lr5-OBv_bSMfJW6ezwmxsB9c8om4gHeOqGMyfJOljS72rjNtlnN72TaCOKN9rlViywMmaaRIF0SNSV_OTREiDXTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 625K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 16:29:12</div>
<hr>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vev9AcsSR_XTbQoOUH02RttiuAVPsvEikWkpVai-QUIV-4diZEHXMlI82RwofTZfO-5XqcFPZlKuSEstPuNePXfkKhB_6nMPRYM4hVCIKcMLe2vuVqGAeo_n2V3eV3wM__EiieOFm6A8D0LTheZMQ9sm9VMHDuJVqqTj54wgJ0Tm82CHWecbkHBWvmJPXFbFbvuEK5e5rYKwJqgnZXjxDbMp7jur6irm-4PApAZSfKw0h3ns0I9xfvxkrAo6xMOijtIBvVs1-8cAN8lh2uIlPl5v9UooyYolrZ0b1uBPKNGU0IyvYbjYfDmikFZ2inx6PyT9sdP-TmOqXrMKQ5JM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSCyDKaxOarI0GZaK4-PJx9Rz-xiuQ4BSqsi9lks1TefYoPqXKimRKuRyYvOcQu__5LAsoJ5jpI1ZKPi3OPr2OUKbCncY0ZvsXvo-GFqlU67-Z1sttEoHANHhwjx_M5swY8IFoiDVGikyfjIHyMdctw2DTjhSPsL6yHNcuuNt1wowTWe42FplNGWEuMxs0FRmV7i8LiHxthOwO8GYWvnjJCaw8NmC-GfQUEAg3ZWVm7qMYwn59mBbfMbI6rJIAN19im7UNFWz24Rj8R47xcnu4lwQhmLFaj_cXtpVMhwJmPm7rPdfBi5WO0Jq-hQP48uUclMtgNcBP3fH5bCvMcydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26942">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSbXVg47Al8IkjRVuX64CUtBIT_UmUi1Y6v4lRA3KsdyCvg5LbdPOichGJhVK4G1kwovVb-3TdFV3GKwea0sHMyGJO2hDEVZjSaY_bKj5RUZGYWtki5wzsGhHi9ic85U58arGBuIFguwvQgC27M49W8ckzDg5YrvNlKhApY5N4r1GIGz-h0-MNOECYn1cA3cpjb2nzIwKdDbFSHijcrxc9uYl6hDbY0jM6cPyBa-HePahHbx8dwfmjQAnyxIanbuPO2zxkHyiX3moahfhFN6SXNR9-AL5UtJ20ipHagGtjas6cozYoodkiO4SeZgYYxEcL_57aRHoxejW_YX3j4NYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/26942" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26941">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/26941" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5Kye87fZZaI48VlwD6ZHR2zbbQjH0rOZCI4xs549sG7AkwhnHMj7eJcaMOaKruKheYo2VZj_kRIi0SWRTCBFoVbxWEuihDoi7EFHF1TfLfOEuz0iV1781NgptsqYu9eu2jyZL1RNEbTtG9-SBEj007ZzTa-EG3eTGCEHB4nMpR4uKbsYeq4VNYOR_NzHS7GX2On6kg_Sz7_5LvOa4E3WWsWbsOfhFMKKovXFVnqimJRAJudMEq8AO48jRGH-AyB7-9GD1x5nGUenZCYXoRXdNzshYouvX2B4PEN-vdRXeXaY3PGtQWdLK_odKygrtcpQ87b59SFsyezBo7AHfDsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kojPwKPGswjunlkauR1LyJpQSHY859fod9vDP5utZPb4jsSGEGdPSEf0ylJuFIqkXzet87s17JbV0_vNGzl6beWAkrMYFsaqJf6fXx6hfHhurnBTxxK7Fh1WYJiJWHaEU_eWg6-uV_t2wyh6pwi8K-E2DEUUNqVcrge3CKUBzpOY5b03plUYUg6fO7QXz9pOY1Vx03pBdvtXovTWQxQPGux1fh4ema3x5uvosmUugoE7vkX5vY2p938CkKuDKmFikpvELhFdPJ4Nxb-uaMBYd78aaLHbAStHIUjgBdKiffPnst6tCts1oDETLxzY8W0NQkuwaQRmY_n-iiaKmjSpww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/26939" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5mbmXMmvWGHxKi0E1RKzwlktpyCZUVOnHytEF4ToBD3jHUsi-IjCnKvYz3Pi5ysD4xruDieD29fTXKIwKGyJ-NKWBkn9nFtWXGvBs7XchA8alvlV_GihrON545R229R4H8otF7zxBCIt11HakJeXRo-r-D1VgD3m9_GfGufuir81VyZfsAQ7mlY98T8kLkSTtEiQdu0dE5UzjAX15cAy3t1ZyEx_3TRGp-oC4R0xwS5JTzUbulArT8AD2KD94kWuR-MLHg0kS8lFMOnVBqu3xrji4g-XXAxoDMZzWh-Hrr7nn1AYwA_783fW79YALlmLcmmMfFOA4CnizlmU6ReGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پست معنادار و تامل‌برانگیز رسانه رسمی باشگاه خیبر خرم آباد با استفاده از اعداد تاریخی 18 و 19
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/26938" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلیامیپرسن‌دارایی محمدرضا زنوزی چقدره که هرچی خرج میکنه تموم نمیشه. این ویدیو رو ببینید متوجه میشید. امکان کز خوردن پشماتونم هست.
‼️
طبق‌گفته‌خطیبی؛ زنوزی قبل از تراکتور خواسته بود استقلال رو بخره که سلطانی‌فر بهش نداده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/26937" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eezm3_wEa5GiZ-Uosk4dh8Ymk-tN4y2sAOhlVpe6Kyo6hs-byj9DyeFjPA8CeW9lqbC1emk2W0uTktiox5AQlvQgPj0kpB4O9_9g5O24tVB51pDFRrZP9NukewHzQk-DmCC4eEcRAtfKIMOpFq2CYATvwkPVslz9s_6p2bUtZrLJf3kQZFFJpdsyA3iWK9C9g1-ngfzFUhSstI8VuBCWAy03qJTDWHmcbewgUOsYxvPy5jvVyBN0aXxK-LvAvyOt9z3yr4Gd0rkEkTq8-damWQghTI82eBEAUxBWijb9udrc1FLcIeKeZB_QxYM35maLnnHIT9FGFbVu381DiL2Gyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26936" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYgq0drOC_FPZJudLX6tn36gsb5_-G0t5uCaog-BbzngD2_XI2Nwm7m-LaHhe8B4B7vKZCZjVWWkaW_4IRH-4VQy6rzSuusccKx_3DH_3ExHCUChiLHQ3nYb_Pm3ARAEsNTB6TWNbKJnh98jqv1wc4GX0IB42-bhc_xbRh6P-poe0TNb_qh2u0lEvGEa4VV_0A5XOHcbbiJBo92oMrIY4ZvOvqYzEJlTFAFTVOIfi1_9MASysw4oM2M7Yx-lGLq1CHxLRJ5kRJcjFjST05GxTmvQLyTkAebQRiWpe7jhsKmATvc9B5202tLnh3uV44_1aEhlGL0CRD8rX2eeprxWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/26935" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0a57Uya4TlkNos1NqnnG8B4RzA68Wy-hYRMk68jgtwVhd-2ggs9CN7EKBC41UbDrKVsHK_hkeW6SF82lc6MFzM0V91Gd3QXdV8ljhMaMfz1tuXrMfl19UQe_GObNzxR6ZmG_CAhp6DkcwO34e102bBkjvSHmdyXne2SBeJ-mxJQtmXSChDNuPhUnVKpaVyLk2ZszdXPFyZqX8ROVRWEf6BKHslaEo0vtopoi8oHXE1HfZDZvxnZMuCIf4A7uTUwiENnhl_1XmaeRdr8R8kQwPNE7gnOeQOoe-70KRDcJkFa-UlMWUNMe61__EgOQR4OgyR1b4VHdMg24_tZLllmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5gxYw8DFPf-pLB3RwsV6zCQB6qLhgEKgAbmcGjg_go-7jW6SFs7qZf7T0_spHQci6UvEY5VlfOxwB_yzOCAoTcBVAMQf7wl8MbDoInOcuM4tN2VzgnyED2_OaHZ1wDBpqzNHca5feUi2ACw_qal2lC8LTVvvuDfNkw5EWf_Ira7jTWllFrjn9mv30eXvUBXCHaW-fwPEsSJVLp1DAOrkPPwNtN9N4eJje8TpZlXTSIN4jtZ4ge7GvgYsKPliT0J7wd5dZvqgVrdCQ5Srb4kS6mSZ6kXu1FnD6V_dFTEJhbjXFKhU2JAMv3FCTk3Sm2yuKRJgTd2-taARYN69mbRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq_nTPtigzcTF_Bi5BBoJmb5YAxWL2oxitJmcvbO8uKOnqkj_ArYicPox6wdmeOVOkq2c3SUXZw4uEPqgG5wD8kMF8KWCz9P7pUa3Hin9wxSkig12D0oHSoWPq_a_M1NRENgS4INfMWRrLmKQM2U-XX7i3bheztSHv1j6v2XK8sQ58xQync4GDYBicYcWIGTqg5TDgV6YB_NezUXgcWX0ladpoFoi4U5jofXriB2ApMtHSqSuSrnSMBFh7-5XNG2oIFEI2qFNDBjUE-2pYWgnMgdb7eAacULc7AjcD9AXlzXaxcw3fnQaVgimHZlPqT0DiZnJ34EFY2y57TNJjmJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcHQeIfzsaOA4DvJ5B1u4jFbcBzezLahXc8BsAImFHIvbFufNN1A7fMEqMXb5lz14P8nEm7p9yxvLza96DKegLhncBIEzxmPETNj16A_n6eO9b_NcximpyDl7du659B2-WmjJZdoqWCQ7WeWox9Er_ymy4MzAZeeh4b2QiQQHRBYQLhKJ2V7Ro6bICBVwHJWJkljY67znirQd3rd-KXA407uunrYogSU4i7mixxHvuLx4N5iu2Iwy40qA3hTUXM-UKlBZbWG7O6s23S97pyUE2BSnOJwOdVw0LAC2mcMp5ND5hc2NamA2YdYvPHxUgS7mdMzsZO-M5JcZ6TN9cbghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26929">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cupPuKfqFkJNNGTPDruIv9JkNCa3Plg199XF9_ukvZVsHsR94p8Uwra-p_j8j81RCDhdQi3G46BnUvzeLJ8wUojBmwTiVdS618XuvnATy0MY6FBkPqbv4M9CbLO5kUlQwmMPkhZOfnKpqDnvz4GNuO2y-2tzKnRBS9nIkSR91YgbB-MGImq6L3XyHSg-77B3URjyR_4kx1fBtMp_vUqcBKweDuUmTXYTmn41vg9MpBbLS_emG-tAyftiT9geEICwCjafmV7ycChuqYpsKNyaj1wONLzUbjOvQXej-1WgU-AdcuFx-Y2TT8D3iULPyV7AyK8bvgBG84alKzqZdMwMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFcKyEByPvrUGAXrqyA-f2Hhg9dFyC8lVTVv2Sv9UbJ3JgnFaTooHZdRkjLI6d5zRabv0AP0HAUQJydoaUdfb7ztBXBAabPgsC8bOVy-Uqi4osxsEHXmGNQmiW8DGML3Mf87Ms2UjTzheDbIyTaFpdxI1MraYw-K1iwCaWLHXAcnEigId1aqFLq2eJbZNDvJaoW3ReBLKu67UNNO8rg2RU_Q_AE-fhCQw5s2pl8M81HIHXKwZ_ySrG_L8BslKD3G0GrQk0GfAGrR2Xm3WVejjn4aVVP7FosxAfQa0vLDsCnZ4so_Ts0xhSBucb9f06nqmoGxKlfW6wGcmdt1o_edGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لیست کامل ورودی‌وخروجی‌های دو تیم رئال مادرید و بارسلونا دراین پنجره تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26929" target="_blank">📅 12:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26928">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0eEmL5r0qCN8Ne4WHQGj8utcTq19IyqEJqUX4E5pxcC4dqh7bOGGdHkd_4nGTlf9JVq9W2QjBDT-AknBtn7Wrs7TKSgKbxGSulXvh26X9oHbw_X60q_8yC04oK_PA-PM8NOjQypyluTYCQ9m2GOWEbMyLYgAkYCA0egTmx1Jh-Dh12S4wrgNrFcGBUAevT1A9DhNGgGk-6bGA2Eti7JlBHZWwEagEiwbqaavKqNNtuFAH4Uslu5JVyDvqtlwdRY25JdleSMi7eLnmJmD_GpD80MVFY_ZRxUlRFoTmbSMMeCso-uOkWsm3CiUQjAS_VnR9kLfiHanpfH_LVEbfPLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26928" target="_blank">📅 11:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuHov7D0WEAGWpEhUiPyoNp6zInXC03SapYCuZs_1aZlgK5WN-sasRle8bVZkXdI9XS4drR8Q-vSsSJfJJVsPjfBAWTsoSYPPfUhYMnL0Mt-q7K1iWkY8NNIoFOmuXiXFTmGLtSWGg8FYZ9IenaX2UTSVRSIvSi8WaEEGvG-DIrhrbzG866GSBLfqL7d4ZaSekp0dsmJ8H0pLaFhKX0CfZ75AJXqiFzGNV77hZIRcui_v_Q8YEq9x2wRiOacSpYVC082emngI3-xq5MaWZHjWpoSO080_1O5FwMOGl2xtPuN8vJWSUaCUVNHx1KHarySO0XSmvrR7Uw36Osv1DbWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIeqjoGiiFEnmJWtXrp0KbBmMTGNcClGTzlvKskxvERDEaaF37u-q-4kBYTy9IZkWl-06YMM5CcCi-pKll2F4w-aFcrjt1DIj3B13oJEdOcaL4yZp3i9gQFfbevjbHK-VgU0w4D2Ls7i16tUyxrevz1dRUAmrw6IklfTO1L5g7k4arr4zQjpUcz2Clj7BdfjNIoumHQIzZIupkPIlYuY-2bxPm8LeSYzUvdKf77ghmitd2t0KYEwc4aWbQuGFTnGGn07dGzLnlejdH3H2xCB0LogqZRjwHGubLGqN16KtGM6E7xJIoMcGya-XqsTnZ-Fzc5If64bz0pwntVZZ2tQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtXdUlHgGWLPaMMav53mBaOzEh6LVMfYFMv4-UsV45MjDUaFIArMQPFU_PtKxNd23SnGNVAGAIYD1q2tOHbMqLRvJr2erR-WorI_RYY6dCDXAZB-oVpHN29GZR8LEv-JEaJPfHeVq-u2BcIb4mKbRnMCk5FHxCI4M6152FT6w7U_B_Ysp002lQ07bNKRYksjDOrCO3skheQpPUcsTUENAA2gpTYlRO3Fj5-YBCxZTRMbnxUjGyCpmab81rPRdIthAVMegX2SUC18xRIEwvF_lAa5phmA2vD4UIhIUIPm-fmGbLfjUAZCNKio4BjKge91wN0ObA6UDajfQvj-TJID_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26922">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja3SMauFUpFAw7hPyiHz2Cpmu9H4dCvmsxnea7-GRCFnw3oGxKmfk8XJVP5ckWuY4wk3_d4iSsTq5miEZDbew3IrGOp6FH0nZe34ezQOf7JmwWcU_oGLd8elgSWrEivjbY4shLSU20nY1ZrFs4iqKWOOSyTzKIzCRMSxx4KdkuiMBOMTtouYE2f62I-aWgmQ3GuHrWcr-DUhzxM9jjujDt6B9YlBKXjnEVDgQYvLmzVNF69EJq9zQeMh2VfuaBFXrC1BvyNb1phJ1JS2OGGqLZghkZM77Ugiw0WVMKaBIf1y7FjbWq_esvnSdkjcrZY048Nlbg2obprneAlCwm-smQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26922" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM1dyE_y1egN25fxHERYoeDPy0Us2WUEFvcGY3gnd1Ly0DW7UjDUgZ2p10YxlrbuX7VJ3Og_MeB3XQzABApnvKGX5U7C5P7Ouku-FNgWf9SAc-ACrSq4Ssxsxg574SPlFweWGzpdiL5gm9c8VjHyGXagJbAb6OGkKjMnsleQplwVXqk5js755QEk6QyEcIoz4e0sls60AkYZFU805EeOcmnU5P9j_OtWxeRwnnMozRVxaNeLP65FIUkXwY2Sohp2C2zS7jtDk5YR66jwaTK7At_3M1Cvsl7fPIzrdjdkgQzOmKOpBtuaowNYXGsFZT9blcFHkei-YQu7SK--63inlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Zpg8pOV5TqamFwASssBaZddOD6FZi6KzghcTclNIPPCm4NTA8Xbpr_x_Qi25Q5j1nypx9MNrI1GXKTfhqJ7bP_aUdZIrA5w34kh6wH0YWOh-82NuT35RL3AUU-41WO6c9AYPGIL0HJvDaizCu7QBweOT-PlpkkBh3XWV92xr0ItDiA846nkOMjbh1dwDV_0l7CRWICI59f2wzlkeTSU7Sm8p9yHyYU1EOkfsmsi-eGmVCRDjdSne5Nugde9ccScmtg84JJ7TznB0K2lXg3olyJ7lXLlGunEw_eiQyqAJF-6iqIlyfgNuHAbN5vJ9S8r4nhyIFwg6khFAhjTYZ4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26918">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3px4QhoCn0NQgV0lL113tmyxG8A5PidvKfcyiRUTsPg9rfOQclGEfmRKk82S5gsNzfqv54eeEpez5IeeByRGQP6A18EeTiA9POXeXEv4MW9suqPoK4tQpi-rZceT5_qRv0AbBRelyEE5JMAl879Wh3HWKld3TVez9LWZTxhy3mGsVKIrxJpjXhEpA4yaNkBS9LTZ1KPgP-So-lRL_49omyfdac-fgROH09zKI7kPyohm66vDAzs1eYx46e3ZeDi8MpT-FmhlxI2LLIMLXQlmcNX2bRkufyHE560xuA6WKr_P4yKu7MHtho4ktGgBuP_UbDBeOT7ollGiq4SC0lGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
رسانه‌های‌یونانی: تصمیم‌باشگاه المپیاکوس برای فروش مهدی طارمی قطعیه. سران المپیاکوس برای فروش مهاجم 34 ساله خود رقمی بین 1 الی 1.5 میلیون یورو تقاضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26918" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrOCSKCUq5AwRswTPzHaLW9TfISO1e1JekS3JLEnLUqFYaqlNKnU3qrTCV3Mky9wCHWCBUI-j4cdO2RzJ127XvrTvsiT27wiFBOdpAu-iDn0oJ8OgrXPk-c69MsILzBL0Ax5uqQcW4YJo2HODary93lEoxI0g0EjhOWG1sRW6DvCplpTRt7QvDhPYu7ObtxWlLAq6b4Cc0957Z3rZ9P29evclREt_BaGiT8tKcWVjwM0qLP0jD2p2cu13z1o3IfMFsjQ1zgTp73hN4OebmM7stE6MxS_rQ87QDc1XZ-IdKOuj0Ep3mxwOVAhV4U0FI-lXPblaxvIEwxUdLdU2beLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZy_KKv8_xTw48R1cIjrXtzEuP-D4lX7UttWyPh25-FpSyLCJCOwK4d0as905NQ2_ZQNAHqOgmTuhv7cLcn_Hf5gsXtEDHPqrH_JRzTiZCeqTneWw6h0c58vJzBHo9a7tT7kJWz4zCRaqWNoWyWCYuWt6vdx0GN2_tYcmEVbNGeXxXuuQssYGTxsInyR3eBjgqtAEPM9l6bfUMPWm6_O_8-phGjVjWVHDGCz0uYlG4nuh1YcF-w6RwjvsrB5-lOPFjm94tdT-o2f44RnSjULqB2iDs0JvarXocHVQCNGWFzu7AEv2FagWt8KZq5-cts7R332pPWcyqxYcXqTbJVOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzqIoAI6tyQboPiUED7uksTaKPagHrKbkP0ky3Of4lmlNQCx1yXGE1cev9cb40Zp0fw_Nqqwe8rarPw-uUbSnrozhyZ4lm6yTyVYofveOZFvkFyvNH5VhYHUKImdP0z9C_QXYkMSZpuUJtZvHB-9fswmS8FmUFruilCWay6VQi9iuJDSGOcgjK910BsPEjzf_CbamEqIj-puHGGqQvw5J08iNzSHRGt0O2IL-DnlYhgspiO-pvQVWkaO7ohftQ8-OvhYmBggJTY3QAyrAmPoCpmpv0WV8rejI3gvO4QFd52KFZ5HsNiI7izsJ-f0xk3iARxEa-l-T1ypXIt1THAFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucd-goZn5RzXxjI0NNznZHLTTcwaHqaAkNmnlVmVLASUZ5ODX1TVB9w8HITFOgpzPnm90Sob96fnC2U1hTu413-rm8kPwuuPn4ZORMjPr6_P8Pmo2uMJGiJpyrY5kJhLgBHma-zllwgyJU0CbGEpnn-ouqQXx1fEH8rsxAJQk4XTNZT9fxX1YVflm3ykKd9tvNhlQ0CEUVcT5soxxofE-Dq2sR7JHvR0FF1jWcuAu3jr4GlDi5PjWBay8etjOskIzLWvwKMLaE8Cd-1FOeBHI7K0X4_KZh96LZHibSUDK4N3haM68GueZgORGOarx27Iwe6s_jP-Q_LmvlLngx3CLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NouTR0r7ByTgxyBm-WcwnOhMC0YCwXAfSLYYckEGuJohr9W4pGdOPnM9xL3VIvbw3q6gGrozAt3c_0JlOnpDmA_4FxQsyAcaZw7wRjmzQ7zAcoqB6DVn0TmoWowANmFyIE-D97RqsADK_HiKEZz139Wsx5A6mJc5ydSrK9GQ4eBa2LO5wmh_TRvGXzOmPh33dQKi_5stvnnvj_BjBicOrXomY2hItjmMtzD5c6Cn1FiS8tL9jnyR3gQ0cpaeiSbDbko7Z0mLTRI9KOFc8EiqyVZycFuKIRosdTKCXxxOkX-Yg7vdsXB3HOeeI4NaEqA6jR4xfF-abR7CMRggJPPLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flZP_YVipT_xRU8jU1DZ2ZItE2Y-46SGmrGlPEKXkp1pnTa9CHPxOH5HJtnS9TOFBAeyYMFJwOa7qg3ODv7R4UYkXPcwnMfGALsIVwh_QtGe5ldXx7ipGdmKI0tJkdCIxP7Q0U_1oXA4VxskGIMOm2qzcMNUP_Fp22lwymHVhsIb_a4rU1v6ccmbpqadeM2XqJub7QbcRg4_IxGCd2sF4S0EmHPUGAhYlE6Nv6FeRHJ_bZbH-Ol3bWXQ5EL6FpVmgsNt-UPFZk3PpyqqQJPCKNJMiBY4W2KWYUvnxtiMIo55aP5w9ViNjlcPU6NgPbNJM3mhlEXKc72Xl75hdAlPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDx_Zpevxb_8Bv0V4ASR_ZzADf-5v7GdRZ_2QBvjecruRdkjsJ2onDDxyIleT5IdYGwnZVaJVed6OuBcIRJavyqXY8OhI3T3ceJbHStY7klYU4MflKRzBLSzpJiOhyxXFOGtb28Wl7zVuepbbb6YBR47k1j4m-E4Y3XGmwfoOZ0BuNd0Yi-pSJqTQ1iQgph4VT2EX4LtEmljaQuSOX8KBGDSCNg6GYktmVLrZuTigVQDCgthW6QdlWbjjQEPVf-9K027_mkZqluTu_l0nyeGT6lvNjkFQII-MoDB5pQSFgnvmahJIKyzHqyaSkGTFTAhooPeHr26GXYGRWvvssbDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAKBkyGMQhZqFVkWvR824LmE53JHl1BRWnUj-D8UYt0nt4ysScykwIJCKViKUvmNxT3GCeF1LvfSGJtw1ucmdWLRYYStmeu_wYFAduHLHhTEYW2NSEOb8s9P9Z8MqujlXerrLbuFk_f1WkLABYlOgeAsidj8qpOAkwZp2GAK5CXpG90r6UsDPSkvvIcqLMPphBpCWw5p3ncWoS4dabPfbTg2ekUlXve6qFIM54m4VAhoFEQIrOkrm0Q6RYBIeqcslbE8aMiJs_kHr67xPHLdrhLxgwqEibrdLHS4VBat3v84aXoJtQVUOQoRXh42dRZvbpwN9ubZHR7HKnmBHrAJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1MOJrhXMW88Orxw5asXvDN_CzQOx7L4qWFwR3jziJf6w8DyA4XEKt03JDhmDzADghPnUhpMdInKaKzgLN6PViVlV6N8o-kQ8P38_Kyrh-oMwJXPgpyyzkXBbumhcqCqe4shcRWNqY5IxOHHmxPEj132HCDDNTmLse6d4ZJiGpN611EhwAjKpxJCzrluepf0ZkIZ033E6rwABoIFDV-V3ALIxSE7okBINbL220VerGTCBuWfxPpC_Ze8KZ7U0HxFeOI7NfR-BliVRpX6HyTAqbgP1fb61K0-72M7TDrODAor60Y2mcKMYD3khKR-f4_5E5UI9V5CbryDcuFGxUjbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i47RZuMlA9_Yldhyofu4Lbr5Qm_xRfZjzuoLEDj8DLJycyjjZy-5MGwhnIS6EZUAEnF0WeHg1H1G90l1OwSCkSotYLpyV0qqKAun3J0P_2RsOpiP_If8WiRz499q9K6FI_5L_HCLgRcTXGAl1ZQ1ATaN3tdUmkdUJTtsDfVucopCzD5wey0MuO7L6-uL0R64AHVREbw4cFkvPARzmz4gRJ3uLwIoIuUx9ZPCQfZRR_23jPuPF1gVLuYwbQDR28SBjB8s6R2xvVtvqLAU1eD10zOIH7W5eBXkvEtGARKVzYYNMXrhWCWT_ca1L89Pu0GWFOjUYiA8k0D-W-lR_U62hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBzZH443Fh5-dmQfHD2wn_u24skfpgIxuLYE10oHQtYT_OP-lEost3YOiYUWUK25RfeHNC1FcJMf5F7er40UP-lKcJz9GZYCwM7GmnErAHxp109i8Yf9wAQRvkUszAouMIhbpbXcVGEhL3BHihuhx6iJuMm21dqarYFdWcotOUKdWmfesNutFE7or_nk-ZXBV_YmR3FFk1TZWOtJpCXboYqx73wruHtmkonNEGH8tgY1p8j-iS76EpsWcknaZD1f1cLCYzSx4tIdj0b8j0OIB4uF-wUXy8-OfK6LrP_Yeha7-q4czZ4EQhhV-CVMlgPMECjdvmVaWaA25f6Gk6fF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeGOQ_LVlCT-tmReaDAfXPAwJTkey-3XxTc1esIs7kMVvRY_f5047n1SVttLjSV72SIGu8yIQIEPZLZJt1dOkHT4-rcaCEXEzsojT5j5uBd-szCGlveWomlBckz3ni7lJhKLaRTIzeJ1lGnRC1hZpQIwFZ_olJyN-fHVuwpRS8gvYw9KgXx7uwKVhH7OkouquC2YBC9i6W451GLJCAh-vqRYpMxIJFxXPjE27wxmHv9s5gENzc-FqAieKych6gPWjSgNzkClX2SI3QoZcIWe7yo4jDlx7sjcbo8dez6rMjK76kxauJSRE86ryRsqRWwOABffAmqNW9ah4kncN0KpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfAAYoSdIp3tME2ggTDuDhBd_Zj7UZuCiBuXaATYXYZaVC3MjDAQyuqvnlcVbH-A7Z2HiLOwcYKH9XiVyv7iN7zWSJcuzpDZaBhoZMLk-ptbY3medJ1ZrducDhFVOs7HOtmlL0xMaxD0NVs-SJp_eY8gcXcqYIxYFoYnxG8u83kpN4aZl7RTnb-V32HdQgHhWlfA3F2-ZXMbkmxCj6OOKlVckp2YzrQNiMdDp8h9UzhR5C4OB0JLeEhFpC5-lZPviI8duBE6o7sfRKkztbetq1sBNf_iuapzbRkOzGimRpIJOzL2KXzshwO5D7YPUbYPkQ12tyl-iEnfrzirqxDLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDHPhcQueMPYBEc2I3MO5_j5ukORb837hEYI81CQoIcmVt0HZ74JE5FivLOLp9K8urFTcWc4E496wfUo0QUd1KeykkjD7h59Qhn1wdJpZLBcQe6biXefmbNfZ-McDarNdBk1djsE-AXDJdIA-TcMK1ppZlOH4OC7rfZKaeiVlrjbrOroOz6Txs6lqOBAHQ0IcP0KL5NDLZ185fUIIfWJZEL75edPoipChM86v6zNCQX9RO1JRxhXOQ9DSMZbE0gbs1aUT7lgouJCUeURYrvv9Dn_uyRFA6ABcoH6OhJ16HsOHm9ljC3ZcnRiOkTucx-OSGMpTBRAbumdDK7Smt8FbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDB7hX2nlnFlXLk7p2N6Xl22BDXB3kUQd-Db-smW8daFEHc5DoVE3lAqlsDnzQ4nUzfJqw6WzxkzkYfBjxekr4iCjzo0zymey5KkGtrDF5GJBv4pfgVWXdXZVM50ItpMgj19RG8dg1sWbeVzKDQhynFFY-fl2btbpgQIlfvW7Q0SlQxHiyP8MMP_sryII09c2ZvL_yXlsslJpINfU7ESqJcK8vM542YxdhGOUnJX44A0nHJtnAotIeo83IfH-Th72pLpsDgwTAV_69f1tUFhDEDuqYN0vt7dogTVYWo5BuJgmXQNT40i-xoscL4PcIpFA1VDK_LiRmFs6W07NSOA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT-BMpZ4cmEZIqMzLwLUSCIpjYTJvpu9sLkB8qAulSxfbmuSIV3Rab1uUEwgVMnjhR2rjUKjfr7g1Nl-0iv4WJxBOV7R0KFLM1Jb20rSLof3nW92JhEz0ZwAStVUJzNsnw3kgEm3rDa2Aw2AQNYte8Lkr_KsE6bHco5fJ8jCHIjpLYW9uNahizVDbgREsViYhBVz079wMZn-ovl8dUptqLOvAwal8I5EcjmgumcAi_QoW97MlWwwtBB8Cw7O9QJsOGJ8muAks6Ut9YMMfz1OyYrP0A28j2iGtbnVWFfrcD1kReOMtO1-Oq1AJY4IdReM_fXz1KJkDl5gYnDZreJ8Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm4BeTBYPis8zU-uNYauhHAhdRPUnpbNENkme0Lz5N3NXHpHYBdmlsFocTIAgxPI-iv-EHtcEPnu9CDWdIj6xW2JO1wiuLCs7qooavWP5JaGLKlCtNjH1ej18UHPMv7mHJ5xpkxSIZTUHXZaZDLUvjJPpR2qCxmkY_MmJGmaLhZAqPsVsQGMSzsQ7jE4mtBOMGvn2s5YLbyjXNjAwVRkgxqq15qbisKrzyOLPRuEa2dCbiDfOOclikIUYNFA2j1VVjUSMCoVcQr9oRC1EoP3K1_UPnWAwcVoEn0cNvlcsRO-agD3R0W2c5jOfOSrr0MU8Rgcclse5KMWYApcmPscLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=hQO4eABIreBZUPNL6UYqLykqw9_6zOprHab7n7B3mnSw1O_oxfX6R2F75PEV56KtlESxza2MHNcxV0n4LFzZATDJNXLJFKSiTNbyMfuGC44hgO9c1cMvSXa8ZL0KVv2BgltrIIWLzJZ4pTse9axSaBJSQiyK12V97S9biUjw-h6j3Rvel5VjtsuG9aPeps1PRX0VZDwQcUXJYJeQxoNTi8-c1BEMgcc7VurWrsYqu0RHKp_1lkpxNiEvGN5UF0e9IBBc5IVY4V6lsc0kkuJtPKnVrLlVOljXUevQn-x3k0t7sKhQKd0G78ohAFEhH2yyy0-ZxFuxXZ4ke0OKI4l8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=hQO4eABIreBZUPNL6UYqLykqw9_6zOprHab7n7B3mnSw1O_oxfX6R2F75PEV56KtlESxza2MHNcxV0n4LFzZATDJNXLJFKSiTNbyMfuGC44hgO9c1cMvSXa8ZL0KVv2BgltrIIWLzJZ4pTse9axSaBJSQiyK12V97S9biUjw-h6j3Rvel5VjtsuG9aPeps1PRX0VZDwQcUXJYJeQxoNTi8-c1BEMgcc7VurWrsYqu0RHKp_1lkpxNiEvGN5UF0e9IBBc5IVY4V6lsc0kkuJtPKnVrLlVOljXUevQn-x3k0t7sKhQKd0G78ohAFEhH2yyy0-ZxFuxXZ4ke0OKI4l8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiKiD0krFPcIHUqL_OlcI84w0zGC7hXkJtKr15k3iPI9b8D0SnJmnCl_Yg9WsHaXmzJOU0j-FagB24mKp4zW7Y2UhqLxtbDYmmCgpBS-RU2yGPw6m5eRKFYdI-jfsHVuaP6pHIzg__x44MnnasIi8u_MDoGvkfzu2AeGaA6yKvjCn--euIQm-ZzPvWl0A9AWc21ZPFbbY2iNrChym-Wp_DnfqbVcM7VvWwJFGG8WY5221KgJsVuCoWznevXIvVh2TvdwieJKFufUxzxlgq0CN8s19QV64vHXR_x4o7nREZ9TzzjuFZ03D5bKLYkWqd-03eISPOLrdcozkyhNatjUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTVYDX99X501HNSVkFHPrUpU_D2kthoqRlDsT3sQZxDKpjxj10lK17HsCVFfJPn7IIvA5AasB7azk8HFfRRFnQ9t4kJomv_qNivlFIU0DIbrUQQ0ScRh52T1qUr3BhF9lauAX3yPptpJlnHzXhcnDVqDUubBJ-MBA1eTfU0ncxUsra4PXa4J1rf0DcHCdFPx-SxK3SXa2hb7wL4Iq7CZkv89Dlln-HAUJ23Cly-uvf1NcIdJy6Mrf7FlGjI3VkNU72OczqbqxVcW0nWny9E7gGnszGuDiXsGNsc_BCcA4OcBWRlm1q8VcUStsLBoO5GVoyboSVfjNKk7Y3WUvhiIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T46FztdUoL0Odatjm-DOFmvpNH2OxFs_hJ7jEy2RnwhKru0FT7k_MVZ2lQD_dlHtdVENsU2sQ75Jri6K3SBSGEKHCS4k0OgMkA5AzBIZ2B7iBlK_bcL0DVAKp7R5PXLeCBPkxoD1uQ_fFCqPCYey0L9khuz6ZgRO1ksYSAZkj8lYoUO8Q4mSCW-xa8Vhf4WHOUkBemOKdPbYEhgCaSc2VAvZ4SxgM50huoNvtk-R9TD0QyT2E7StRJmqcZXD_-fc3c6qvHSxuNY2jgHrhRhgTvT17aw3_qQmrlM1VwpLiwVIlg45Q8ZCP0aS5m3C-Xjw7LKAeYMEx7S-hrTu5uJfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ttpZAGKLIGNe9qgpa2wX1vdX_AN9s24D_ijf7SNeDQ0AayGNUdMZfDQiHv-T4ma9TVj8yVjWKnvN8uF2EfBMxL6bvUiRNOh2AK1Ow9UIyk8nXNys27TKUC8upQ0EO3BYteGbi3twdIglxwQA8r2cdFYKbKMBI9o0r52d2fxsMaDzEZSN2sl0Fhw420MbN4Ku9xuON_1pMoTY6ju-WBu1nJGjgwil0tayxGOFhYAmIrxh3yNcpZaHoT2M6-pgrklJUjOs_j7wRg0kxNhhj4HqF3K-ePxmUgLY1XLcxgkGMIlsZXiA_6lvbtGtYJN4bwijq_kwFs2QWcl44j-faVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmPHEbU21JNmElTL8Ynw2u3kYQ08iB5AMGgBAjkBFu7ojmrYNKsASukOJaBtet9UDjPlV0RSrKBJ8DhbbtvJv8wNU6wtpbnfW31MoRcD-dKL9QnSbt3O9MkJeerbQT_KGAU6DJNsjQcIq2lP2lsYqRKM_GAy-ADuKZ7AJOJGKt3TgNwmTkh1lkreNmeAD1QC21PVgKsThfS5R8QEx1iZhjv_IcRqnovTpaFdIGZngfos4LfcyvInK0V6h717O-bI0x1ldyULriUHNKg2fSIhsBJMDg6WLlVK7Ly5GnpEfEEhzqVmhE1myyke24dUOukR9hHbolMO2Cg7tdXETGAtrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM6P8qA47jvoQbGQwYeR-vsiETR1gVWRzX9H0DnlGO-6BEIeD8P-yN40ED79Pf61a5KsDlFDRTpxnV4bSn2ZUrVTp9X3c3JEl0EUTsHdULiQvPEPbIiYBYYxos4gJ9hqxK55zt43LjWCHtxAV54WB0ulTODLOeG-PmhZF1IO-CQdqXPJhUsLN5W5yINIFtWxiEaC2xHmcWyjLM287Atr_YHYP3wPRKbLW20uLKxbdPW-VWIN1mkVaCOcI8fecwRBF6myPpfOj5hRb9m2BuRvJtrQBFaMXgVdV18S5E2C5PopWqdh4Us9ctWSAWTWroHz1wDvWAZGIRwmOUngnDqQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRmue3ezV0H_lt0jaCePynL0DTsmbrgczETEKvy77wOhsqPKRlgf9eNl9U_qE0KhDUj01Gucf2dsU_5nyeiIooe44Zn9oBGcFrHXO8gBIniDRLBmdtjYjX4_Gmlu9Vrnl7U0SXN8VvF2C2NAThDwFF5PozPcZKFycxgOGbb5BmrA0CQnlTrPvFjZ3rWASvnm--hKUwTfz_qnLos4PDJcKVnEDzkKYiO_6p_TYaWdcoyK7mL7Myv57NcRHycp0XJjfD4KFTRXrxQbY0kQEz24GZbt6BwZr9y8cTQSwXiUosf5DHKbSklOQT-TG_3zfXRux6VjTPwMHn7ubeluXt3LTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzDNzJx-UIe2_FImhX6tPuka555-1gE2Rw3deTpwkHZkKlPCgLzEmwxLHkYpZ5FfQ5iQ7HU3O3ZrhAsWgUMG9GebYYEsyJBCM5BUBVQUUR9rnuCcDdN8R5d9H1MuQG4TkCIcMeQxrHD8LbqdaGYbvbscvJYOeTgHyrjRN2BZ00B7P1-L44zXrI7z0Vg_DgVUQ2hsCqqS749-KQBXsegyshjtqd0-wV--s7vX6YkjGbJM9EsRkNB1FLTkZrO-q-ySCtsQeH9VdAvlgFCb-iQY1voC8tvJuGrK5yf2o0DdVOCEDba3dGBWYeTko8wjTCMZ00tEn4fCEs81Qa48uq89TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDPuCQ_UeybocN1QxUgdW8HfzpNNBMYpUZwPjqtbYSrGnF4ILiV0uN0p2cJFMewvUgvnHatkePke4a4zjjoT5NPJLd64aHNjKM4w0iXHYA425oTbwff3dqNT3xt3q9o-z2RYiXVCpLG-bCZC5HpIfez59UZrfOkL73nq0tcMxuqnRLrqWrqVDGpActMzydMHpZtYSPhL8EWLAD0CWwQU1E-ed5e-_RkW7EhIJ-7JtQqcmiTSxeo9RvxCEr29FU8SZ2jAe69kQaMM-ilk4KjRf9_ddJxQeDujjj3sG6wTzSkX5kYjFDw6vqebGaeb4OVgSBmE5D2wuIK9kIOYXKO1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgE7Y76iQfwJiLGgHdB6t0S88BkWNDuldvjItK3Pag_WaDP-ux9EIiVzZ36NBY8bMRqOXnOedRgYFU57QbruitUHmoP4ZoC7D57UMsnxNehZaXBp4RTcmhw-C_z7nJLX5uRM2tnUj6fRaDMxvPKMGGhMtxKJOtfbV1xmJhKsaPazwJ5ts597owGD1gS2FNvUH3_LjGzQD1PfSIedSOIxsV14_BPNl2eYHCUtbUw576-zCBU5QQxecI8KgRHeub9CXtfremot3J3M1gsMZ7t4KCit4wsmBrCbpfUcOfGH-5_2SNMs0EUkNZiH2aFc5mkgx2tEtI702XuX6dusCt17aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNgO4fx-HlLhoWbmEgefXLHQJdi-Jb1y-lfgf5pHtVgYykrnfZnW8ptpVmyn33sNYIg4kHt1yZ11dMOAMYbpFLS5xIMj4B34hboXz3IO7VSs13R3kTQAUFPoN9z3aFRJAnDvzewmmBne8NMTyk6io9uywFq9eI-KBwn0Gs-TRpD50TMgaOZH00qmokv8t7MbD8HdzRdaX-gbIlV0zhaDaIwpoSVD_IGHfKnTnGsmgH69YNHHM71c0LXZ9SZH1KybOk3X3yt4k_-3CYIIliUvVb_J5la3bk0UDUqMr0a_ixGe-DYmdgeUp_bYvV9vRKj-cWlE5b5zp-0YCecWzvX1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyTcZ4y0wyAHsvnfwxxhanBKQDrvZn40nwgGZwQhekQBKNw13CH-vmWyQoftWQQZr_17hInxJjjFZ1-BKBbq5knJAVsSYB2hcEJy_19le_hdOBC9tRyrEe0vyYx9jQQX4eXaPrLfT-RcXu63SeutwKSOqMMSZDfvhlBkZaRyn3N-FXgnkgeYTeTBYw1hRtrtVCSpI_QjWzZst9fukkrY5A81nwYnCWbfKo3bHMw7RyEFtwDy-GGrQRtbb2SzvWPG_DvZCAyX28w9goyqaT3AzJmRoNJuSK6TrTCiJzERJbVTbfk3EAC8piixUTAeZCZo3gDLHT55bLifEpQr5ecHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK9qaiY1HnCtExKq-2vdQQORyYol4iee9EiGJyQW0AWN_3HIuWdEh57t54koGaN-2daxtMCW-F9YZKBAzJ0p5Nt2cTrJZrmPiHa_zOq3IEj5rtKyt0LduZXNX47dcRKJyqCCeo8Px3cKlMrs2ijXMcn7zsqC6ESNXOjG4f7TnbyEY5fchm7tRfuTbBbM2Y7l52YWqky5a2OJRFbdlRKG2fgPTbN8aX8TQCErKcpkoeS_ASuABJUzmTJ4kyAy0hHfnGjPwLoJVbvUQ1v5oc2ueTrXSrfc1tTV1zDoortVtip8zKzxqrjDAYQ1vbbYciJe1SDVRqABaOylLycze3XoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=aF_Rp78oQa4skaWaoXIUuvy2zC7MkiGyseYlgd34pde7yClqz-TQRisZfgu-LWIntA70hcklI8yRCtqe-48ms_xYAlRDPQFZ4gx16FQ2Zk1q7QtHg8_r-nXdjCHnI9S4vSp92wgqic7CXSsRPmIQTPNQRp0h8st2FVxkNUgIFszp728xCO_tup_MVTgTaIEzLp0fGCXFiuVt0YfAVcvqeeG1KCyA5e8pky5bsoUbPAcHRjOIxicWGZ5B07_UUBmIbI5bUVtVRhyjTsBlkjzsrHn3EywK5A0xlZAhzEnB1ruzOX5McekFPGOfl0_hB1GsZX9QLUCU8PGsBMCiQRnA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=aF_Rp78oQa4skaWaoXIUuvy2zC7MkiGyseYlgd34pde7yClqz-TQRisZfgu-LWIntA70hcklI8yRCtqe-48ms_xYAlRDPQFZ4gx16FQ2Zk1q7QtHg8_r-nXdjCHnI9S4vSp92wgqic7CXSsRPmIQTPNQRp0h8st2FVxkNUgIFszp728xCO_tup_MVTgTaIEzLp0fGCXFiuVt0YfAVcvqeeG1KCyA5e8pky5bsoUbPAcHRjOIxicWGZ5B07_UUBmIbI5bUVtVRhyjTsBlkjzsrHn3EywK5A0xlZAhzEnB1ruzOX5McekFPGOfl0_hB1GsZX9QLUCU8PGsBMCiQRnA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=fvi2xvvLtrMKDLGkFKhdvRtTEbbn4t5picTH_VH-N4r8-mTCxQuR6kDDkjTL5SrZtCB7KBfjHVtxkGc8JjgFE4T31nsVz0IU-TU-Z6AAg9ADqweamYFrlOXkXCHNav3Ux8SVFg8iy3Ee4VNInyjyDw7wWSEfz0vx0FoQFfdVCkUnhORteUFfRtPKypQkiGtRbxW8R_LdzAG0jS99mqHtntqGtO4kiS6QhtvkXw6yJ6QrVeWUb3UjDZJ-f80d1twa-hb440zO5kUjWHix1vYMCqIZB6RA8bIAGEx_ZZNoOCvZkxQPu6-9jjkYUDJHLXRwFWvFhtnuRn1Htc_xripFww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=fvi2xvvLtrMKDLGkFKhdvRtTEbbn4t5picTH_VH-N4r8-mTCxQuR6kDDkjTL5SrZtCB7KBfjHVtxkGc8JjgFE4T31nsVz0IU-TU-Z6AAg9ADqweamYFrlOXkXCHNav3Ux8SVFg8iy3Ee4VNInyjyDw7wWSEfz0vx0FoQFfdVCkUnhORteUFfRtPKypQkiGtRbxW8R_LdzAG0jS99mqHtntqGtO4kiS6QhtvkXw6yJ6QrVeWUb3UjDZJ-f80d1twa-hb440zO5kUjWHix1vYMCqIZB6RA8bIAGEx_ZZNoOCvZkxQPu6-9jjkYUDJHLXRwFWvFhtnuRn1Htc_xripFww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYuphgST61A1EmhO1zNAFmB0BDU3ZEAabwcpIxw_yzKDDlWU5MWKtgb3QbHd-f7x9SPJ2Zes5G6IgIHG1J8bB3lzi8FHi6dml6aEZNGlSytTLTrSjbrhrPYVMsOQORzmVXsBLs9ovaLrS6x2p8iQtASqucH_m46wW3ubU2_4P24d-gppAOrcKrvIzgYgeCQXm34z0jW_1eiKwF24pI1JBdZEVqKKc-7ghvQ8C3DjlC9D0eNsa-0MtCifRn6WVQd75xO_I7LCPUFdlN2kVU_M3xSB6gl9bT7Q_tr53hWo6bumP4QzTM3hstAVvC0oRo6-ReT62cyupb2xhcXgXeTT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYvX8QVUbhmRKmOCp7clFsh9qoCuNjeMsUbGvv1c5Q-BOKrCb5wagT-Tl_dm3FfG2n5MO_Hf3UARrtAgvssPyonIaW8Agd_9joDqqEYSWUhivlv3EWHL1nrFyPYN6ZHh36ZxHntkIXO7TWaOpwQWID_PTiPM8ZjzUBhQqt1W66pUqzELZ1L4ZE5SekG21RKiEXX7D587qwdO_e5nuSLUlUjfkp4yjiny6kMwASjJ6q9lRecUJpw8ToBDitur1imBv5_tgyxAf6zniiFZrPU6q0VbIMU-5Xb0IrLTt7TTeAqO2gIHylmO1XlzGAbdafI9wZ-nQ_FrdbveJyOnsDlcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=YwdVQfenceLPGZMXM4BvBa7ERMptWUb-J3mWP0xFAzNR4UsmM9pxGXtCVIGxsaQ1QvadZpiEk21ouVu3MuldnjelhJlbguX-WzoOS7SVHgXwZYu-Fc31mL4U_Ryj_r23fgWfEmpKt3pfO9x-og9JwOp2SivoevIBeOSYgTtHxaD196_1MSZ9wmd0-EHrJRCdAArq_8PIrkD3fAc5iUao8POAOt4ZEIlbL7uWxYh_Q1ykikt4HCUsSl5MOEmY3wXnVEUYdZDfrYo8GbbG7LLiZcyAX7NOP7mfhA95oK6Hg_RIPeOwOBI6FotZtcfja96mDOvPw6ciNWBeIrpBdS1XIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=YwdVQfenceLPGZMXM4BvBa7ERMptWUb-J3mWP0xFAzNR4UsmM9pxGXtCVIGxsaQ1QvadZpiEk21ouVu3MuldnjelhJlbguX-WzoOS7SVHgXwZYu-Fc31mL4U_Ryj_r23fgWfEmpKt3pfO9x-og9JwOp2SivoevIBeOSYgTtHxaD196_1MSZ9wmd0-EHrJRCdAArq_8PIrkD3fAc5iUao8POAOt4ZEIlbL7uWxYh_Q1ykikt4HCUsSl5MOEmY3wXnVEUYdZDfrYo8GbbG7LLiZcyAX7NOP7mfhA95oK6Hg_RIPeOwOBI6FotZtcfja96mDOvPw6ciNWBeIrpBdS1XIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwe-ghtXPWZ8-BxpuTj4Y5O7XffyFcJH-ZY3Zlp9iID8AKYuvrlweK6RSVFWx35yNd2f9pl7zblQZmLvSNABVUy-h8GDd22qSDAqp6zNsdWDx5xpwTvt7ThvgocAIcDaJwmsZON6oVqkU50QBs49OLHtFnpdY2u3NxfkZDJ2ZPXSSZ6Bvq4eOEz3ug79sTw0ZtgyEg-5Iy6F5XIBcutHJ3A_wdY08f3e8GnVSqP82J_52FdRC0aJ3FEU6LAVWr-IbwG0IOcRUnVUm_cymr4ybamWUCZe_3QOicMx_PGowAC6LcXwCXx3ojto95NCx4c01qmjgRCLC81OLF_eDijDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDB6yzC04Y5us1PynNPco5uJ8y2J8_C07sQgrWlhghZEbdVD0KnHDdU3aUrkRjvfMbz3GWrAvtye7saOfbjF8IM4ZGPkV6y99Bk6XzljlFv2YSWc-AYCrdOiBRZ9TpqOzlnfDA_Hr07r3shGONEKdfaBmC_Z9Es37ESj4ChHmIS1mbOm0JiSDt_3LVwa1X0qpNWVErAO5moD2DQ6p_mAJc8XtepW-YX_pTYLYNEDBIaFVrIAR4d2nZV5ejZmoBzONCOzcXBJEdLM_KhZbCm936ty429Z7zm70a5wwZgY2UmGGBHcU9DhMasbokuzHkxUGAlralv42rI-vWcXpHLX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=QgnW8nHQM7gTvUlIfjbD76cA-tjFnsID3ZfsR76wsO2LUC90mwSs0jAUhh0rD7mDPuhxaietrxY59b_aVdXPHgRL0nBeCQ43aAinvVHMFuerw7eDnmNIgZ7ptHrh6qvTrBaw23BtJIPjx5cQ_UebDPO_sC5PCsZo28ajBhy4zI75qvokrQUvscT6d7Vhm_bUNNfwfWd5yQkVFWCa1G2IKn85XwQuq2_fjuMUpYX-slev2pochH2TUqiz6rgkM8zMWcwHJvY1zXMOkA0AelMqnjgecymgHKPX3k1Uk6AOabxfyWsJjN2QIlkNO6mMcAzpAhZ7F4o_rUNzUuVweX-2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=QgnW8nHQM7gTvUlIfjbD76cA-tjFnsID3ZfsR76wsO2LUC90mwSs0jAUhh0rD7mDPuhxaietrxY59b_aVdXPHgRL0nBeCQ43aAinvVHMFuerw7eDnmNIgZ7ptHrh6qvTrBaw23BtJIPjx5cQ_UebDPO_sC5PCsZo28ajBhy4zI75qvokrQUvscT6d7Vhm_bUNNfwfWd5yQkVFWCa1G2IKn85XwQuq2_fjuMUpYX-slev2pochH2TUqiz6rgkM8zMWcwHJvY1zXMOkA0AelMqnjgecymgHKPX3k1Uk6AOabxfyWsJjN2QIlkNO6mMcAzpAhZ7F4o_rUNzUuVweX-2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYV5RrJRazLq2aVwIMuRHvqvwlZxYzLKcPUBW2o5sE4zvaGz-vJXPURA20XuL6ykkP_8G9u1vOAaW-5Kkwm8HmPJT5B0X9kDOvyNIFGXxTt9klDttN5wC7Uq-PAOdKHGq11P7UJqz0XXUwvJDjIA5OXZr3IvPrXK1z7lYlDnXLWV1UAukRVQIX6QDT-98Y9raUYBNdptwH-3Gt6_noj3efKhwiwSVbxrfR7aKo9xWoy9wcodxU210AHHt8kJv48bbJ7xIaTX-KwAOO0lU0M_Zp4o3_9t-26GQzX3ZOF8n9WY8sbGW8QHtFfSmp4DuAEhHcRyom5KB8vitcxjYKVJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=mOaP8ZmMBqP4S7dGhXsHRSsxiz25AdXtRS1SMKnzDj9aSpAVzeXbsmz2ENUA_you663OdVXsrmeRvcp-DdWCcErDeE99BMqgyL1Hj1Cl6f06IZccX6LdNGWKG2WwFypb2F4MytHQRKvz6O5h2fCcqEFrn5QxKxIEZ0h9nAzaZuHlL4_1E1PrsxVbmPmzMXPN00IagjPF5rrh8Zd1THFCxRGvyxBfwCC6-qFhOQtyNbAq4aPQSIWbBKCkI9PwPGiNH8oxAAePTAgQvmIWU0fEvIjf1XcCAf9y4CiniQFoK4HLQg7aNZoo308RzLxRiq9dnfs4aILLdEWKCu9fzjtT2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=mOaP8ZmMBqP4S7dGhXsHRSsxiz25AdXtRS1SMKnzDj9aSpAVzeXbsmz2ENUA_you663OdVXsrmeRvcp-DdWCcErDeE99BMqgyL1Hj1Cl6f06IZccX6LdNGWKG2WwFypb2F4MytHQRKvz6O5h2fCcqEFrn5QxKxIEZ0h9nAzaZuHlL4_1E1PrsxVbmPmzMXPN00IagjPF5rrh8Zd1THFCxRGvyxBfwCC6-qFhOQtyNbAq4aPQSIWbBKCkI9PwPGiNH8oxAAePTAgQvmIWU0fEvIjf1XcCAf9y4CiniQFoK4HLQg7aNZoo308RzLxRiq9dnfs4aILLdEWKCu9fzjtT2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEvn_zbXimvKINSm8RcgWcDAIOYGyzP0T2vVJOm6ye4pj49uphKeCfoIykO2WR5OTbHYQQTl-JyZ76ScwYK9rLAw-leoUsmSvQ7bRYpMzHFsi7PA7OCDW2KP3EF7ZPtI7X-iZg9V4Q6ltoXRjXKji7jEoOOnvK5HkrdDf9nkZz_rlMl-oO9hswPdH7RJMykxlx4-G1aEoo_mwhfDvgY0tnI2aVWc7KJsmIijLtVdvmp5B6BMWRYGDVNygVAQhGF_pC1bLEiNjFNm0gNrrHbcCxXbLx3dr6pHGYzL-yLHiZmWQV2jzroxTmQXnap99H7Fpx0m0QSTHqiW81CrEooI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiGH2bvRfW4C8S87bwinVQNzguzhmf2jvrvQw4nm_HUSy6TTstOnx03LSh-I89MLtGGYyujhQxNxeEVUc8Ex005A2A76bOgE6Gme411R48gqkBji3tZSyICGocXFK-bcp7bbvVz_I7ElXSb0BSnHDOxid8PeE868Werr_DTRrWG3b0st3z2VdfeY2pr2klFwiCkeNU_AjJOFzHIblxQXq0lX6iK9tmkq8QhWaIgp23xFwfp1b9EEYp2HldRfNapHCmcbQLSeauNriNU_6k9g1wOGb-y2iDmU-EIfTkW1pO5WuRHVBgaYq6N2wIVszxSt4XngRo1GqdmuiJF0dc4swA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5KeRbMMDMr90OZB4bc-Vqhv0QdpZGG2SqtEyuk3jPgg_AUTq9GQo0dSqk4jHerfQ-8o9F5No12_ImfTEWLj10uZfEwa2Mktz0c_7LH6GFi3QXGRwvYD_s8rKEBRZLrPqS1rZhTg_yEd8zDoj1kZiOIuKW4i2CK_hCBehrDFIge-pczavkDvTU1uKnCTpNrr7vUqNbd_AyNnAc7Ctu9UZveO6_bhJuWol144Ap83hanE1lR9j5mYvIeok1lgK1Fp_ntcWDThD3PyeSJZ9W6RAxFmCPt1BQ0Irchj8If91xnfIf6cmsAU8j3-t_iMeg6hodUs11c3ykyumNFZ-BPsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_stiKYgbQkuJ0-wvRYcIUC9tNY5FA7h9qcgy4txlziEvd1uKlYeo72DEPBw0ciIlAipM38c8EV73RPCxVAeT3hJkj-b5q5EtoMxILATY64RtFirJ6tLLmd8N5WzOHfRsOXrhMCDGzDrHTBtjCLyhVfe8jHzjltLxuakSqvwkG43icAWYsIO7ndlMg4eM_-Ayy12ScVU0GfpSWAXX3ySeBWmkEYEgpfpvVDhqeCKzBHO2UtQ2ggzmR6B5z7JdzAoDqQ1Gn85Ec430cgCDKQIYxC6dcrHZKzpWVQIgk4EJbCCDSjF6gYZqCbaemDNkH0uIRBBgCF1DsvI8Idn4tDT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5OBsbopjOLxlUaaTtcSuwOpGzFxVdTxkjKat51mO-4J5RWIVMtNiILGRem7GYUDsk56noaJeSt_ED5WfOJ4sTEbmv-ueac2I9tD61YcXt4YznRkU8O5fWXuCdgCxyWKLW5jwcVwuD8_0RZNzPDfA6S0I9U43m6O8k2_J83yRTFhZt2X9UF4wRNeZ0iJxPsLBbQ5_wLE7qKSEOqZRNPpx4JYplADf7LSIUP-eWlrq2z0fV4Fg5vr6JMZ2COROJIZtygXqSlbz39Q23NkkWt0SAkRgkjuXgVJSL28nMUXK1NvsWIsOETLz_XKalZEY3bR_d7_AIrMP5dD77TgghOg-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h00dUU9jeTcdrmXcEMBOY3Wzouz1L5XSG03ZZGX9DzSqx5gY2599NQjB3x_hYOIxiRF3IYgCEI8huxR8Zn5-3IWdnLytP0k-PB0boFHcS1gP8aLidXzwHyYmyOIyF4_-C9U9qfcJ1EFJy54LZwiVUuykbZD5slE_8ek4-d2O8ncJbLwMSoWyFEkp-MbqGBIp40tLDfUQLaccgNlYTAv-LzB2k4r7DjFfV_CC1MXuzZA7oQMmcy8TBPAx0-2Jq5UTRaDDwN2UgYZpoa6UHqGJMFc7arlmkhdASaWEVMFU3E4_jtW_CMrcSUoOKh_Mh8C3kIcFWCkZtK_m2bB29xRjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVpjqnThslqBSIjRkWnOXFSEw-HgOF6OInbD0kxOvVnUUnJU8tOA9tiKnqgsQR0TwRZw1h7QhoEe1NvravBrZZXNSsnRCLmPtBvFD3ijWBcYgh5Up2RUk8xGNkuxB8jHmkPG8_uYB0Av43JQ-IXdV9DrTpXaVf4Ibto19eX-0YyXB5batJADBVP8U14KYTRyIvhiv85lyQL2lyYI-xq5gcCJNtWQ0izXWk6BDD2j4V3SQSKU3T4gDafShAxwAGidayURxJ5sHcOEC4Ngo7LFXwGB0EV_6hyWzlF2NTNFWgtL14IvRdsAyJyGA_gzQIu50OdBimiudnTkcjVlbn1vXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=RUSglFgxfWXbr-7ct17EDcF1btknzxnxs5tekFpBAQ8KGG6kfyQBlilmCqMv4rT25BwD4iWyUsHVthd6WxwzNK9r9r9PWGQsW9QoQMFwg878f2_q3ELMDSDAcFFhjkfIjaDfuabRmOXP4J8iIx1fZwyfZL9UNMU-NjbljwCjWYkpRynBS1xZgLrwm_d_IUfYIq26EVsTus97glgCTuladjVQMvLGaZEhRBoinGULwHNen5wD71W8-XntDUUOyquk8CMdD0diZzgQw4Dh7OzK34CH4XUg4ZQIMCMPtgvYL5xdJV3j4ERSvPu2pgdXCk0XxQpawE942_gq5ki3QjzzoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=RUSglFgxfWXbr-7ct17EDcF1btknzxnxs5tekFpBAQ8KGG6kfyQBlilmCqMv4rT25BwD4iWyUsHVthd6WxwzNK9r9r9PWGQsW9QoQMFwg878f2_q3ELMDSDAcFFhjkfIjaDfuabRmOXP4J8iIx1fZwyfZL9UNMU-NjbljwCjWYkpRynBS1xZgLrwm_d_IUfYIq26EVsTus97glgCTuladjVQMvLGaZEhRBoinGULwHNen5wD71W8-XntDUUOyquk8CMdD0diZzgQw4Dh7OzK34CH4XUg4ZQIMCMPtgvYL5xdJV3j4ERSvPu2pgdXCk0XxQpawE942_gq5ki3QjzzoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVGHqcWgbeZYFp-3-Mt0IrmmBN3oEnT3X9Ulej4gC4R96l44wVMBOErlVar1uAkC4jZLm2esLHP1XE70gaT9VsW-WekTVcxPhymozQgGFh4NrUeVsi-tZAfUIUQyI1IZ3XevNdd4ts-OMOJxu1xRy94RZB9mggQ1gYgOYaCj_Q2Sugdbtf71q0wMqOIGKyqmm4ejKZCOlrrrE66RZOMkPUiCMtghvPQc7kXnCiz_vJHQL6BGedGYVIvBYKjXrHxXsl_7di3oeM9XR_gjxpX8zWzFoONeajIYlOtIKNZvMdDDkrmjHIKG7thryGdYvoS1YRDI3B6spGeS00XcEUfasA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCh7yg8byFjpOs75Hl5MUYlQjmQf3YevsF-WjcSxeqMJBIcsChlwimFuXj0Yx4dcUC1AudXMVhjbYylnT7zHCfE91PE7ScbUcXsbR_saeanCiYnIzyJAUaMglKLu9k6z04R0ZTFk4l4gB3YRUoLrSaOFklRbezCS9o6pMa3VRmDYfyOSqyX_PyhoWuyVQ4yvzhN2ELAlTYuOHzfVyp90TKdVBPCKj-WZ1yWkWv2QFrsP1gbaCaEgfjGJfn7u0SC0XIWqyG7fdYL3lWdCdPgfqG5yP2WoHYol2lIPuCqcqdfnp2orrrjWJNFmFnfsNA9otUzLOwBM9ZacLXAbY_etXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxbQS0AUIX9qtPHPiTdJrvqkJaQunN7c0-MgLeVAyP-Lsk0l-fekYduhONKx94c1iKWtTxnTLDAIOOwb4cgEDQTbsF7CB0648yhQYt9Qnag7LecGcEGP6puGbrvYbg6U9LhXMIkXVtyyIR3jiIH6sNdYuqlh0Q35X3V1cKPqRUF1KJ3lPCtFyG6rpP-3zKi0Kbmwrf7ZNQSbojJbdpfNCv6EmFWA3pdWubtKQ_Cc1qNa2sLony0snwlWfAi1RJJWf6bLq5Jp1dq-bgEJ3fGoopY6VeksgWCcHAut-OBvHTvxfKASrCbRE3DO-fkrXz8pJC1uOV_2yY4z238BaEE-yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjeG0hxm94DD8QsAwEm05YYtD018v0C5qeVVU1tAkK-Oit81550VN2qNDEfJA7mNKt1a2AfnqeePmQXoyc5P0zsurzjKJ73mPo-TSn5VjDQUxw6x5rOJCzq-P-FcV8S39m5aZMG9Qh_tak5UdIe33dbSkwg_RdJWDLs_FFH0X9p9hV1HadkFh940_Bs0gxvwMEyqTCAsvG5EalG6d1dL7WGrX8yPCHTeW9IYsSJQ_a_e8ccFNoqu0o4nfS9ZXq7yDnvfgetaWQXsjrMUOTxOT1e5JPsiDVYJg-dXxYOstdrzhbYTOHdfQcGf93c9-6-qjmLQ3450dKhNZkdzd7JetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbrlF3K9S_fAwjPmrQJTeh-31tDgtqlp1tiVO2iHgJvOetvLqrpiI0Cf_sddLJYKSpb1IrybIoga_Qe5enRDTyNXfi3zif5vGvqf550hlK2SOgZYwgMWuNy0WEG3t7-wcdx-b0hYPhZQpoKPLDM7fW7SoeyQ87nsYNcdaNg0P4EohF5NeGKGYEQ6NqYNouaXi_P0urU9G0Va0OsUSjzIthoijExGvmd7gtYyH4QEiY4tvVY2VDIiOfW_rrrpf2a6WHygaTPkJzbtc0ceWj5isUjFiZpEGfDwzoI7FbtBJmscdmpcQ7ZrOH3xuCwiSrRk117RWgwoEBn5xVtrLIdocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3gWAMFLUY-_sFsL-ld31Tfd4j_5NqyySa17__eluX8fqI9uqdP5GM6tlOyKy8c9qVU15BC9z6SjVuEIaBn1-eHjsFmxKIRoSJX4ttMRJbvFIlncB8S1k61FQvbiZj8MgBTrL7aJB8g3psQE33xex13QMUcfncHRsuKoAO0c-veWmpiPmAi9QHTFkfJahH2vw0gS5XtoV28cCaBZwvxvpXbJARaISt1fWDqGODETA2bl0drRDjdDlUlkABKG3zb3g2cLJO-JDQ4jrpQWnGtrgM1ZwNV4W0qwKrGlr0Rh55xm6-1EYoZko8yrq-0UF_Nw831QBBDrORKkLgolxCxdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CH5Gz5UrdvKuQq0JKCpX8eYvi42J_hG4LrcGYywvzFx2tff7Oeqj2NWDnkmzi1ALWJGxGhu_DoffGTAqwpG1BIil5dUTN1sCov-I_6khVlGwRL1eBvCL2Nj8oxJTAC_R2cxlt40_SmAOljtQEyurJulz_nxKxf46UGZ4_Xlz9cV25HLCMSCdF7K8aEIBZNdF06nJ62L_8GMXhz9v61EYCW9vBybb58hVho-x-aR57EuUS5gf4RkS9aWNmQhiInuhq8-z_htNzITqeymalwOG7Klc_cKI5U5gkYJLb_gAJZgVSSePQFRIfr4UYXn1Bj_WstC_ztqXEYkg-qor1bkNBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUaYKyctD2Q3qxsjBX7MQIOs9EURxy05whw5JC8Mkxo9bVwgKHK9LogSbGveXYiAm4Le_J0sJqHUeOd79xrzOBTW6bR7d-26acPeRb2ZaE1YmfXqaOCqpPie1qZfs7Jv0KqL9gCpwDsKG8SlwQBAxDF2CywGstbBTUIvM1dXslB4LdwkDY-0darInqF-GiQgpyfjDoAobOfQlwweesPBNN1V7PqC3k8wH6CyXofEbwp2WQty9lTbQajZrNay-alVKhIhC90fW4vxeuEdKcNU4S5r8rl6Y2JThoVb8iM5VdsA1G649YFy4-vvjYNSkcPm6ny3UMFahJuY-fwKzx0BXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRw8NQOCbf83SA-AeuCnxjiBMsgqDZsrdhLbXBpYMuxrsa2mdlXkAzjfeHLEikmpTRfE0_cEbXOwmPHuEQ_H0AfnFgP2IlgKAm8Ceu0dTOtDmxl1CRajPp_W0DarL_rHsfh1Wtx0z-dsk0JGQ9zqIjCmx3pRIukFovVoHFf47Mvm9XqqJrsPtxrbwE6TQ3plHeG508oE4bo7hsTAMEva_fC91F1WVhbRHAJ6JsRmhCYIZrQNMHtWobDNr7EDS1DQt_IKtLNEo5Kul-DMu4moPF1nGCspp1FGfq_sTxyhD5hh9dY7lAOs7-6gCxYEk4eamU2geg8cl2lLNf5EePNMOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnwIGP8xPkDPrXgu19OuUOrGZy_LyQcJMMV-1GEpSfHFvy_UaLJJtDk20pXjoNnnoDkKT8JTY9lZ3VYdUovHQHlwMSEHnOHj9v_XQZL55vyAOKrR-rlX23BGR5QHyIyOWua98lPvYHHa21wXYXkm_iIK6V0PDLEnJSkUNeNtP4bRmpjzoFDOwMnI6DZ9Z5Q53p725prxNwKbf0WwKON2nfqUdquEIudj4gA1uDTiw6OQuQOjyshA8Sk8odHpN4NSKmFmxHrCagawI0JpkPJjYbqFcepjlgQiXBcExpMDG7kNeKmsmnGkPDEe83JePobtH1nB57G3gsGFHZ0Jy3XREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t80YH5EcJBYitNyKRPWr-APigBiYU0gc3-PTKBueB0kWa6EMd2Ro4bU9Vk_yoWLx-kKJex_V1x67O9qhLCRvZsTAzCtSqoHTAXmgB2QwIt2GuXsnr27RxtsEmP6MhQTncbu-qrDWZSNOkzFXhgT8Qw1Y0IGMf4Hxs7MeKTPMvaDEIReCEaYi6r6hyQBOegdWhgbTsrbOBhH_fNH1p6cPf0ArVpw7CiIRVbBhxeoWC1zTQ_E858lx_oehwlkmrz25-MWjhFe7s3GPnvciwxt3I1SjTlfZEiXn5F42hjAJMsg7CeC5PIA7GBw05yPTrkzg_SrBH9_RwR8HSKbmexKj3SpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t80YH5EcJBYitNyKRPWr-APigBiYU0gc3-PTKBueB0kWa6EMd2Ro4bU9Vk_yoWLx-kKJex_V1x67O9qhLCRvZsTAzCtSqoHTAXmgB2QwIt2GuXsnr27RxtsEmP6MhQTncbu-qrDWZSNOkzFXhgT8Qw1Y0IGMf4Hxs7MeKTPMvaDEIReCEaYi6r6hyQBOegdWhgbTsrbOBhH_fNH1p6cPf0ArVpw7CiIRVbBhxeoWC1zTQ_E858lx_oehwlkmrz25-MWjhFe7s3GPnvciwxt3I1SjTlfZEiXn5F42hjAJMsg7CeC5PIA7GBw05yPTrkzg_SrBH9_RwR8HSKbmexKj3SpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKlWhWCkG6a8toMO14pW5u72wVclJ_2V3j_AHNb4JcW8TV2NhXdJRqQhFBGbNVoiFQDUiu4KtwT5Mh-8geb9C57ed4G7_fLnDHX4Z4H9H69sojIDSJtHQahhl6IjKaNn9lFsLedvFedB-PnVkSLAREss_Z91kHyT3ytNmTPnb-D31DwNcMFFEaZZp_3nkqrjxh1FGUfMNfIcmmZLP8XIXeU98bCavWqk7ovGJzHECvNJ4htTI3EQN-6xbokPdAAe1oZ5QOwnxc1w8jYYYAMA9d-w8i2ScrNQ-F6RyenMT-WigpSrBYDoOJtbuu0qVQId46yT4yY-JwzPBK6wWfGAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zunz7buYXsYuq76tSdqNOngof5g8ZDmZZtZlexVVjOLMiKKVAnqmpW1NyBan_u38G6b-a5VlfBFI3MArmQKbff1VQB4Wz1x3KdE1l369mXQnwBCj0YhvOR3o0IVbPIW963QYxEzeK7HdOSW1Z3-inw0VoLqETqKqBLYwDL8B2_ShLmfxHGHQ8Yzt5uQ03MQEsIQuZdWUm2jyO08LOe25CHcA-Voh0tXgTLBa8JXJY67ReGctLZW7aYPgYSyoy8oKskx1uz146W2FEb_faN50o1h2JCcSGIJcJr3uivGwr8Co-dAlccXkyNn5mhEyeQizkGwKUj8ZRVh5TOIcPcXq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwjO6XfiWIgWy-2-WrNCKjKsmIVekWN-FiJ8D0z_MX1bz58EIUfwM13v1uLcUioVQVnwoLlORV6SLldyFpYD7o73SEVe1EUkEK81O4_jsqv03gtfdkf9BCA6LnQ6N07AkU1Tg3KH8cmVPuVxhS6_TLIeZbW7EpojAWKsLfZ9pr0vxs1boN0ls9JEvdzKI8zyceHMHDD8Rz1zvnvEBXK620aOqIxRidHlUkfY3JAj3avOO2W-3xPzuYjsGBA2SEaGQJo8ITCx_IlSfmvu-qdgsTAYxkGr2DhLqyGiHd3CBgJr2LxIPuhMkjlor3wSb-Hr9h6IatXJybgn-BivYgXBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCpRKAqyet0LHrRC-XcLQSCCWY8kYqEgihQBG9M8oCoQfiGO2h44obvANwavH_MftP7mec5CwKtlJq1EdFdCufwtRlX8YhvGRFarWirQdbSErlqEg36HA77_oY9V8JqGqMhP0YSETOkcii9mPNcgLa7edCixcuA3qUj08UwBtWb6hoPyrP0b8w-mSvhZsAFOe7LSqkJHhTKKvIxQLSAuYK32h4cxZirMPn6vTsu0mSK1sGqD7eVqA_x3_ws3i5G_k4hXqY_uDFAeNQhd1RrHVqoSaWRPYygLHg_F6NFlMTV8JrWYELMja907DRDdcA9NGJZ-IbM2tzKikBo5Ojc7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKbMkaJmrn2KDCVpXYDSKVm50Gm3-_fuo4_KJqwaFZlsA442YGwNF6mRyS3-AYb_IaM7OCGU3vX564D7fu0-Hq8mNbCe_XKpafI7Ss4CsB_Wd7p83ZOzKReOeiqMfPFTaLDo7J15GtWSKHULqN297DEYuASIxt-IvuGloAuR6MEgBoVUrZ3f6HPLA8-vozBGNrFsP1eWSsEOwvp56_-1gr-9Z5mwWCHlA39MRxgvLYqOlVAohC-9BKvcS9nimzngsC-0lbSwCHhkt7ymDNl8tkTWaNcplPeEN-Xqg2wMbt7lZA-eCs2CKFtm-4WpV6yaBDikyYPXuxa8Ijuj-9iCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEEvAbrl0MRAWBCFFSuNVViFOE4DuEiFuntL-QywZUa1aGT6nqa-XD2Pxsejp3g1E0azRj3P67izNxQAVXA_ZPCyxgTJphmW5sWoU-pqqB9202giY69kxFonkkLkoQbw37HneWyHzfOQoVoZzFW3fmuEZ4OIofVBkkXtInZKH2HYaJajrJTdti6yXTJQWWrPWXIwjlkczK6d5w8cHJ_qkvQRq3aV5zefjWWtO3mFy0j1VJHJ_V273G2LiawOQK8TM7vuR7_y_qcJys2ji6IXmfmVz8RrPuY6jxZPHWmDanPsLBEz_L0bWmTw65on378R01JntWH0xxgyKVjDaeOtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQSwdYNF9Sp6MKx6As8FjswGAACsBJThgjWTUg_ghWRnEDm4vvCJp3DmwtGoYQ02ci9Jxiw4L6LhJIWmBxt1fRHma4b7atexUEqcoySUnizpIsdxy7AuNkSir3hy14tSHv8RBAi5in7vkA8b9dQFcaJsSqphIWN_BWF0GqbKiw-85ijN3iD2nB10BcoKK1pl8-H_1CB_CDqphrxvuoDZNfdbWtxoaKN0Ky2iv8cxXiHLebxPnWQ8hyaayaojAudSMqPCwBmC_uG_tPQG0Qx0SAi8dhy4fygH4oa1efc4d4WBahda8a-T_tc0DS0KjaQALQVVMcc_eFZcf-LvruUD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uykS3sJ-8J_yG-I4a_zTDQXBqXIbgXbQ-mhyC6Mkm31D_E7Xevisqtl9Svrkvg6HfrOt5uinvPRUrptq-L-70FDMvkLqUlnsS8j-GXc1N2_JypTeL8vaR0fmn9XDm_3WyzMURqiIN_ySAOtE5oCTFoEC3DSe9ZokS7XDRa3S42RbzdmpfcRwQ0jy9s_O60BQ28HYU2ocB29WaXhaHQkFtTS1-NdY4J7x7nmediM_env8m4RCDwUtkFRahrlAebFhhaCaYVpyy_GSP_i4B5RT-x5OcK6NTFd6DEK0_42Jx_CewkPjf7MqFQj1xVJHDTqtgCOOxVlTKlzQob8UMika2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9IhGAji9gkYopGx1FL9exGvDexc8AwguWY8jzILZTtdUdCvmRujiloGDqbxDZtvsjByJtVGSh42QtvR-ig03gXsw4wUHHD-VJNiVDxKrBsRfUm2U9vVF39z6Vhs1hnA4hhlkIBM7E_71hosPHjfPZG2ztpximM4z5mvueCYsc76jw684VILyhu1VqDftvMPlLK7qsLpnV7So2Eg4k6O772xDFwOPhWTcr-liuuM9Yk5zskCj7wT-6yuvrS-pC8-XVnQ3zxvPoPBrdSsLo69zoJQBCnTwJvUNlCppcbRDI-jVo-J_998iFLgNqPWjaxVuTlr4JqCl8GyBDLLJyOkfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6MV1ezfx6Wswa5x_ZH7i_DDd7TiWU6_tRn284R_h8HIk4VtXy0kxacaMGRoMHvnMfAbfGZm-rF6q3w-4N90th0qaD_Fz1kXhg-21QvE3lW2t6z0e0vOYBxY6NgT7esePG7q7P0cJ19HH4wjHKU4lEhxLqIrqTLCZb-Z7JR2OFWIzrIiBFGAiujVwrSeH9l0W-n-_56S-7eqHyoUoAtJIosWpdByS3eprcvafij7EuoI1TyOrKq8JElKsqan_tAC9u7RRcYL-aVUNHtfSXXAlcP4fuE6vf1CeF0PVTA7gvRMvoQMJs-gJhmznRffNUwM08bFLROTV4zzqm-Vc5aBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1uc1qyqrmZoap_5WScaPImKf1hqrOyYKG5HBWoAdHHEdvCi1a6Xi7AZscIp7-nhKX4LXAlw16iCjBbaE0JcTd2mc3-TAIviJZEchxLX0R3FJwUqZOhIcJU-0aQc_T5qprIlf7QzKEDuUtEeVTd4cbl75_h6f77iG5VdP4_S8hQYqnq0wLV3nO50Etmr7P7cl3XAafpVH8YvJkuNprLVQaZP6a9LpgJ4YY_Chv58ef6XhCamSM_sM8PO9RpeIB0tjHxzOFcMj_YYU3wPFRC6jRa4nwIV0p4EiDI-xjW5bkqkZWC_Efur00sR953TdDL6BNCAhHbTenl6XfgOYDIGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=J1CGldCjdQT8gsVO7Z7G2kf9jkadypC_4IUtc1-c85s6AFIZt-VDef5ZJx84-NLpNO3V98IecDffTAnK-BIisnSTLP83KX-H9mSzeU-1-0JjO9hQT_GpuiSrZfZB-DBOcQ-Y8Z6YGUOFM-2X8Hp9rAHL0SpKlgvMdm-2VYY5w_ivMI_PddzMlnRAfvfRkGBO3nw421EtdUQ4KiI67sIgLbSPW_bPlAG1MRT8HT1vWfTe6xXwTiY5HUXmNOHxLPQLpUZqr4nn9be5pEpiX847FfMfYVzjSVNWne2rwISn_VF_HjgyEWbmWsJlQfh42gUdgDbNwZlEWznI4N5C6aqK7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=J1CGldCjdQT8gsVO7Z7G2kf9jkadypC_4IUtc1-c85s6AFIZt-VDef5ZJx84-NLpNO3V98IecDffTAnK-BIisnSTLP83KX-H9mSzeU-1-0JjO9hQT_GpuiSrZfZB-DBOcQ-Y8Z6YGUOFM-2X8Hp9rAHL0SpKlgvMdm-2VYY5w_ivMI_PddzMlnRAfvfRkGBO3nw421EtdUQ4KiI67sIgLbSPW_bPlAG1MRT8HT1vWfTe6xXwTiY5HUXmNOHxLPQLpUZqr4nn9be5pEpiX847FfMfYVzjSVNWne2rwISn_VF_HjgyEWbmWsJlQfh42gUdgDbNwZlEWznI4N5C6aqK7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXljkddljQj6vc-2tL1aZWLlDil-kcGZ5IwTtIWGgllYVcxAE3MeoUF-yc_VcNfdKN375yh6y2TzQU2f3okr0pCtHmkcAbdeg7C2cgiJdeqWrK7prM4lNLqgZ9vwdTwKkW-5MO22AC7YdmkRcA5nFnT75eC5ZhGVMJZFNXYMTe2g5OIEE_qXl8gCnG9ewDxUay3nY6jbLK4needsIiYGGnhSrSVvrX-T8pTEDV1W7eUzob3QfCQZUL2nJeCQxn8pFb9sawwlhRkDtUCIBXbWNfrzEkta1JyYxj0a1dKceU8glVnwonglojm_3ddU-TINLgdAagQwT0JS9JcHMUyglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLWSa67I3_UR0-QZfDnUAU4UBIbVrNP8J_lM696JIu6lW32NrA-yrEhHus8bgRpU_jm5U1cbSCJQ3jdbQt8jsuLOBA7b1yqEs5x-u_TxAeN5dZsK4Tya0g0mWaU2zIIrq2w0r-4ISen_jUzMABkeNx17iVEfN9BKld0qHbC2LecojbFt_fGAUa2pYmuNS3RKdK4TV7A7QpQnZsVowUFm3hdeQRkI0HAFfqLo45OSRMt2F5RsMI2lQ7r7czbZQCGgQnUtoQy2FnZd0ZEDxyxLRWoVGTLPnM_lHjZNIWM1IWMDUwJbEtYandnLbKEZaWSO9CK6lhOP87uc50WKde3r5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poXtmJWrDMeXnjhS7Jd9QSn5k1pQFncRsnuWLtYeMHTVcg0TcmfD2ji709HojTu-jJBgbOLQCPwflLSBt_ADHgOEnWbJ0g9C1gpAMqMeF1-x3LmuXXJmaO6lcuIapg8AJHJW0Ps8i85lxC0ZaCS_sttek-XPnFO1KM-zaJNPUnex_ipxLgBGcRv2rMh1q25rlcheM_So75b--aPygxMnnkcMYkAIcvb880Y504OULWD7k0OGGvh-rRRHHy5CwMEqJY6j5lm3P7tr2LQ4IcIUygHP4LT-o1ZM8o4aZmk64r-ixL6sdD7q9rxa4ozf_FYhnTQ7AfJwlp8W0ayA_1A8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=sDAFQKGWwPnP5gKTYxBO5woR8DTTJjbyrF_mn-4F6nnYlNC5ymIoSHG2ZhrNrDwsr3fCMIKSYZYR7rB-RbiFocubT_wRP4kHH0LrzYh2FwRT30hCCwiVI4nm8Y57HVzVPXucYGgTK2zobt1v-RPIU4KgE6Aw8Awp8vMi3cC_hclENHqbcaL-K4XENVjH2IPXxuIwMqwSyu6VCx_cx_1pckh38kIMhIHgpwcRyZeAJ6y_fGBaZbjPOyG6VBVOIBxg_8iUL7BjMgZjwXe6qvMwhgoq2yarHOp4HD89C21ebchBXDgax1e5D5QrwcWhZFktBdYjxURjB5FQU_r5rQB4oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=sDAFQKGWwPnP5gKTYxBO5woR8DTTJjbyrF_mn-4F6nnYlNC5ymIoSHG2ZhrNrDwsr3fCMIKSYZYR7rB-RbiFocubT_wRP4kHH0LrzYh2FwRT30hCCwiVI4nm8Y57HVzVPXucYGgTK2zobt1v-RPIU4KgE6Aw8Awp8vMi3cC_hclENHqbcaL-K4XENVjH2IPXxuIwMqwSyu6VCx_cx_1pckh38kIMhIHgpwcRyZeAJ6y_fGBaZbjPOyG6VBVOIBxg_8iUL7BjMgZjwXe6qvMwhgoq2yarHOp4HD89C21ebchBXDgax1e5D5QrwcWhZFktBdYjxURjB5FQU_r5rQB4oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
