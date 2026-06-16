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
<img src="https://cdn4.telesco.pe/file/ZzDp9W0ZDLtejLlQiyPBG8RhXlGzCcQ_fletEC4kPUO2-L9y4xL4bBFV22D2AO5OkVAlWfvdEFzCZI7Y3bHmtK3IvxEeM3Ox0rm_nobh7D9u9fVkjI3p81JqE9rH-UhZgNlL-S2VrrJkiVHRCwg9bVWvdyF9F6XawkjLT4F5eCacKOv-tEDRljrqwKiUZhpC4zZd4Zzd3eQ3ec3OU9jySMZ8p2o2Q8ZamazJ0fCiBzeUoVPmBT-XAUTXAPvhXJwxLhJ4piXOxaZdeSsgeGqFcqN4X65NsrFZzg5oS31Z1ImtiLTSNO-szc2MCFJsLSuBGGDEZSbKqVO-jKhZesQmCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.51M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-660052">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ثبت ۵۴۸ اصابت موشکی به جزیره خارگ
بخشدار ویژه خارگ:
🔹
در جریان جنگ تحمیلی سوم بیش از ۵۴۸ اصابت موشک در این جزیره ثبت شده است؛ در یکی از شدیدترین حملات در ۲۶ اسفند، ۵۰ موشک به خارگ اصابت کرد.
🔹
طی دو روز نیز شش شناور مسافربری هدف حمله قرار گرفتند، اما با کمک قایق‌های مردمی و شناورهای صیادی، رفت‌وآمد بومیان و کارکنان ادامه یافت و ارتباط جزیره با سرزمین اصلی قطع نشد.
#هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/660052" target="_blank">📅 12:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660051">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
حمله پهپادی ارتش اسرائیل به یک خودرو در جنوب لبنان
🔹
منابع لبنانی از حمله پهپادی رژیم اسرائیل به یک خودروی ون در جاده حداثا به حاریص در منطقه بنت جبیل خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/660051" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660050">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN5E_iLQtSiUCNb4K_L4_tZpoHXDw_wUyNn2UPq1KIkvC91gICqXgA6yKkfb0IA9FRlR3W4oxvduAQubwzy1Hgbnpa-mT51s2Qc3IQuHe__L2Pt311rnbsNUmUcd79tiDdhl8pDbPES06A7tDJJdmOb2pL_uvrWntgRb7sQCGJNng34fx3UqcJJm_0yIej3jYvAqLqFXxZl9NVnJ6AN2kjh5aBC89XGBQd-7GBcedd8ZcEIvDIO4eWlBqeG0VTho73vqUdDkWjOCmGD3y4McsdBMgiFSE_FfDRjJ23VB5YYCbL8tNqjNaXmVAm890sK_WSNXWfI_MNd6i3KyTN7r3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حماقت ترامپ
🔹
کاریکاتور: کمال شرف
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/660050" target="_blank">📅 11:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660049">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تخت روانچی: قالیباف و ونس در روز امضا حضور دارند
معاون وزیر امور خارجه:
🔹
در نشست با سفرا، مفاد یادداشت تفاهم تشریح و تأکید شد جنگ در همه جبهه‌ها از جمله لبنان خاتمه یافته است؛ موضوع بازسازی خسارت‌ها، پول‌های مسدودشده ایران، تنگه هرمز و رفع محاصره در متن تفاهم وجود دارد و بخشی از رفع محاصره پیش از امضا انجام شده است.
🔹
محل امضا در سوئیس است اما جزئیات آن مشخص نیست و پس از امضا دور بعدی مذاکرات آغاز می‌شود؛ از طرف آمریکا جی‌دی ونس و از طرف ایران محمدباقر قالیباف حضور دارند و پس از امضا، گفت‌وگوها درباره موضوع هسته‌ای از جمله غنی‌سازی و ذخایر انجام خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/660049" target="_blank">📅 11:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660048">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c768b2c3.mp4?token=NvzxEj9aauLhMC0vSJx1ndrhWOYB_-4dpB6dAZpSL9RpWWGI-2teFGni_DpJeLKAZ91n0MPtrKPy7lvxxR2TtjWlBL0725xB_L7lXA4QuZ_jmyH_NSJzBw-b4_bJCSSSvalseUvekNzw5i0ANzWxicjUGched6w50xlsFGcVk7Ek8oXFZyerbuMT177ANRGaWw4NbOWo-R6uqstKUV6q4728lBln6HNUw2mE8q6EANpA9ZuVTuc9Fkznn5OQdY_n3A2oa_W78pZrSYd7PMif1MNE50pInAGFe4b9Jb7FYuu5tJkkFKJgapdNLZAOLzfyNbze99EQxrdUyKZJ_C28PJH_ORHdccIr_W6fIlJq23Nw4jnWgnjKLVvmx-RmS4FrPKRK11rXPqdbn5ZXvHruTvgsyKW-kJyAvt8gI2BwfiRjSNIoyp35yP3-v9d6g1pkqeVRnZj1-q-tW5TKfiw5sSCgiqSrns3zChcTTb5y84-WsjA3MnJskUd2Dp1bOCmXpCiBFFKE1qdu0jasOOgq3JeS0bFETTqAUECdsXI7zf4pavOAM4ItV9qVLdeg9VXl3bGxBqFnF76XB0xH3UcrihoOVwHDNE0xrSAGCVXQzqVZsRoSsSn53d6XVVnfXYhMuMz0EvJhzRXTGzYyo5UDy2qLtN4h4W8ZAGMLX2bBdS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c768b2c3.mp4?token=NvzxEj9aauLhMC0vSJx1ndrhWOYB_-4dpB6dAZpSL9RpWWGI-2teFGni_DpJeLKAZ91n0MPtrKPy7lvxxR2TtjWlBL0725xB_L7lXA4QuZ_jmyH_NSJzBw-b4_bJCSSSvalseUvekNzw5i0ANzWxicjUGched6w50xlsFGcVk7Ek8oXFZyerbuMT177ANRGaWw4NbOWo-R6uqstKUV6q4728lBln6HNUw2mE8q6EANpA9ZuVTuc9Fkznn5OQdY_n3A2oa_W78pZrSYd7PMif1MNE50pInAGFe4b9Jb7FYuu5tJkkFKJgapdNLZAOLzfyNbze99EQxrdUyKZJ_C28PJH_ORHdccIr_W6fIlJq23Nw4jnWgnjKLVvmx-RmS4FrPKRK11rXPqdbn5ZXvHruTvgsyKW-kJyAvt8gI2BwfiRjSNIoyp35yP3-v9d6g1pkqeVRnZj1-q-tW5TKfiw5sSCgiqSrns3zChcTTb5y84-WsjA3MnJskUd2Dp1bOCmXpCiBFFKE1qdu0jasOOgq3JeS0bFETTqAUECdsXI7zf4pavOAM4ItV9qVLdeg9VXl3bGxBqFnF76XB0xH3UcrihoOVwHDNE0xrSAGCVXQzqVZsRoSsSn53d6XVVnfXYhMuMz0EvJhzRXTGzYyo5UDy2qLtN4h4W8ZAGMLX2bBdS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
علت دوتا گل خوردن بیرانوند از نیوزیلند مشخص شد
▪️
قسمت سوم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/660048" target="_blank">📅 11:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660047">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
خروج هواپیماهای سوخت‌رسان آمریکایی از فلسطین اشغالی پس از تفاهم با ایران
شبکه ۱۲ تلویزیون رژیم صهیونیستی:
🔹
روند تخلیه فرودگاه بن‌گوریون از هواپیماهای سوخت‌رسان آمریکایی آغاز شده است، طبق این گزارش شمار هواپیماهای در حال خروج حدود ۲۰ درصد از هواپیماهای مستقر در این فرودگاه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660047" target="_blank">📅 11:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660046">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏆
خلاصه بازی ایران و نیوزیلند/تساوی یوزها در گام نخست
🔹
ایران ۲_۲ نیوزیلند
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660046" target="_blank">📅 11:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660045">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e24cf28a.mp4?token=SgxZh7vWZeDC_xSkigNLVR6hv-BexAUiDZpG5BYLJwj5HGVWIw5_KDoLUNOJtphcqyKDc0Fa76UHpJkhLTVxAYkHqgAci7uXmSqO1pry0LzIZktBmGaF-9Tc4OFDvu9xUwk8pSCUe2O-J5R0NqEmJFzyMDpXMvLWcHNHoBXVMeM0mfEtKAJlzH7Go7rjiH-HsyE3foURQ9heE-c24Ect_jqgiY_9ZL_q-gpq89hyZQG5JeufvZ6INQjrWJVmJCvqzaVKsuCT14gNLz8duwBl4WIU15GA9_GKY7qTFQVrfBpuyJrw-ENO-MV07-tZATfIM1XsbMOc_e9X_k5P5GoB-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e24cf28a.mp4?token=SgxZh7vWZeDC_xSkigNLVR6hv-BexAUiDZpG5BYLJwj5HGVWIw5_KDoLUNOJtphcqyKDc0Fa76UHpJkhLTVxAYkHqgAci7uXmSqO1pry0LzIZktBmGaF-9Tc4OFDvu9xUwk8pSCUe2O-J5R0NqEmJFzyMDpXMvLWcHNHoBXVMeM0mfEtKAJlzH7Go7rjiH-HsyE3foURQ9heE-c24Ect_jqgiY_9ZL_q-gpq89hyZQG5JeufvZ6INQjrWJVmJCvqzaVKsuCT14gNLz8duwBl4WIU15GA9_GKY7qTFQVrfBpuyJrw-ENO-MV07-tZATfIM1XsbMOc_e9X_k5P5GoB-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاصه بازی اسپانیا کیپ ورد/توقف اسپانیا در شب درخشش دروازه بان کیپ ورد
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660045" target="_blank">📅 11:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660044">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58a283850.mp4?token=Tl9dx3dPaDThSpD4-Jbo1GeZcxQnOny5W9RBnqCF0aaWL4R2ZppADx6CQh_P53h9tX6Z4x3NWoWx-7dqawDVhTa65UnUSM515EqTOkarp1R7bbvukijG_hEejcnY5W3TeFSDqswAQf23iLlYHaGFoQM1EyEVwTgWStTtVASwdTgnyS2RJs6bU6qWmoUgf7uEFOd6lboAN6GIGMa1kHTjduOZ7kdqvfyZLvBbjQPH5XVQFRpJ0aYynaagpd4hsan99GsbNLUynJ9mb3QKvwyEo1Xy9pJZEl0WDXRd0OUVWbYdKyfk7aWH1ICOfMUfGMOcEVbUUxBMB2pljrezizylcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58a283850.mp4?token=Tl9dx3dPaDThSpD4-Jbo1GeZcxQnOny5W9RBnqCF0aaWL4R2ZppADx6CQh_P53h9tX6Z4x3NWoWx-7dqawDVhTa65UnUSM515EqTOkarp1R7bbvukijG_hEejcnY5W3TeFSDqswAQf23iLlYHaGFoQM1EyEVwTgWStTtVASwdTgnyS2RJs6bU6qWmoUgf7uEFOd6lboAN6GIGMa1kHTjduOZ7kdqvfyZLvBbjQPH5XVQFRpJ0aYynaagpd4hsan99GsbNLUynJ9mb3QKvwyEo1Xy9pJZEl0WDXRd0OUVWbYdKyfk7aWH1ICOfMUfGMOcEVbUUxBMB2pljrezizylcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روستای سوباتان با نمایی از دریای خزر
،
گیلان زیبا
🇮🇷
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660044" target="_blank">📅 11:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660043">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای ونس: اسرائیل در نهایت با توافق آمریکا و ایران همراه می‌شود
معاون رئیس‌جمهور آمریکا:
🔹
با وجود مخالفت‌های علنی برخی مقام‌های اسرائیلی با توافق اولیه ایران و آمریکا، واشینگتن اطمینان دارد اسرائیل در ادامه این تفاهم را خواهد پذیرفت.
🔹
این توافق امنیت اسرائیل و منطقه را افزایش می‌دهد و درباره آن اطلاعات نادرست زیادی منتشر شده است. او همچنین گفت آمریکا حتی با نزدیک‌ترین متحدان خود نیز گاهی اختلاف‌نظر دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660043" target="_blank">📅 11:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660042">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
بازداشت عامل اصلی سرقت مسلحانه از معلمان یک مدرسه در زابل
دادستان عمومی شهرستان زابل:
🔹
صبح امروز ۲۶ خرداد چند سارق مسلح با ورود به یکی از مدارس شهرستان زابل که کادر آموزشی آن را بانوان تشکیل می‌دادند، اقدام به سرقت طلا و اموال ارزشمند تعدادی از معلمان کردند.
🔹
با اقدامات اطلاعاتی، عامل اصلی این سرقت مسلحانه در کمتر از سه ساعت شناسایی و بازداشت شد.
🔹
تحقیقات برای شناسایی و بازداشت سایر مرتبطان احتمالی این پرونده ادامه دارد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660042" target="_blank">📅 11:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660041">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پرداخت مستمری بازنشستگان از چهارشنبه
سازمان تأمین اجتماعی:
🔹
پرداخت مستمری از عصر چهارشنبه آغاز و تا ۳۱ خرداد تکمیل می‌شود؛ افزایش امسال برای حداقل‌بگیران ۶۰ درصد و برای سایر سطوح ۴۵ درصد به‌علاوه یک‌میلیون و ۵۰۰ هزار تومان است و ۳۰ درصد متناسب‌سازی نیز اعمال شده است.
🔹
زمان پرداخت معوقات متعاقباً اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660041" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660040">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5dfbd87db.mp4?token=VPB1W_jlhFD1FiJFQc-AK5AySqAdpoX_5iAByw-cUTXQJUTGewP699znCl3T5jJWDdyxEWQ8sFeeoErxBDs7OsM52VIVIRhOKPPBRovDNc7fiOROYRTlk_GDlLB89aagVmwg__k7qiSNwsfit0iGcIE0GKJ6Sb06XGEwAj-TvIB0DYW1uOxwuHs-yV0GEU6GXp2puP3hb6IpNssQm1vaJIUsXjayRqo5GBuru5fXs2P4Sbk3mk9t93buKSRufoLLsexsRr7iNM7hBnw_KSnVr4wq7uj1BBGVFRY9bvSR-TuQ2C3NV2NGc5zacNHBuR4ddpUu7xKVe1g5_bI1VVmMXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5dfbd87db.mp4?token=VPB1W_jlhFD1FiJFQc-AK5AySqAdpoX_5iAByw-cUTXQJUTGewP699znCl3T5jJWDdyxEWQ8sFeeoErxBDs7OsM52VIVIRhOKPPBRovDNc7fiOROYRTlk_GDlLB89aagVmwg__k7qiSNwsfit0iGcIE0GKJ6Sb06XGEwAj-TvIB0DYW1uOxwuHs-yV0GEU6GXp2puP3hb6IpNssQm1vaJIUsXjayRqo5GBuru5fXs2P4Sbk3mk9t93buKSRufoLLsexsRr7iNM7hBnw_KSnVr4wq7uj1BBGVFRY9bvSR-TuQ2C3NV2NGc5zacNHBuR4ddpUu7xKVe1g5_bI1VVmMXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: اجرای رسمی یادداشت تفاهم از جمعه آغاز می‌شود  وزیر امور خارجه:
🔹
مهم‌ترین دستاورد مرحله اول، اعلام خاتمه فوری و دائمی جنگ در همه جبهه‌ها است که از صبح دوشنبه و هم‌زمان با نهایی شدن توافق به وقت تهران اجرا شد، هرچند اجرای رسمی مفاد تفاهم‌نامه از روز…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660040" target="_blank">📅 11:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660039">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
عراقچی: جمعه دور جدید مذاکرات ایران و آمریکا در سوئیس آغاز می شود
🔹
روز جمعه دور جدید مذاکرات ایران و آمریکا برای رسیدن به توافق نهایی آغاز می‌شود. بعد از سه ماه مذاکره توانستیم مرحله اول را نهایی کنیم.
🔹
در مرحله اول مهمترین موضوعی که اتفاق می‌افتد اعلام…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660039" target="_blank">📅 11:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660038">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تلگرام در هند مسدود شد
وزارت آموزش و پرورش هند:
🔹
هند برنامه پیام‌رسان تلگرام را تا ۲۲ ژوئن (اول تیر) مسدود کرده است، زیرا از این پلتفرم برای «کلاهبرداری از داوطلبان» شرکت‌کننده در آزمون ورودی پزشکی استفاده شده است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660038" target="_blank">📅 10:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660037">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
عراقچی: جمعه دور جدید مذاکرات ایران و آمریکا در سوئیس آغاز می شود
🔹
روز جمعه دور جدید مذاکرات ایران و آمریکا برای رسیدن به توافق نهایی آغاز می‌شود. بعد از سه ماه مذاکره توانستیم مرحله اول را نهایی کنیم.
🔹
در مرحله اول مهمترین موضوعی که اتفاق می‌افتد اعلام خاتمه جنگ است و بنا به تصمیمی که گرفتیم از صبح روز دوشنبه به وقت تهران که این توافق نهایی شد، خاتمه جنگ هم اعلام شد. ولی شروع رسمی تفاهمنامه از روز جمعه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660037" target="_blank">📅 10:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660036">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DviaNNWiggnwGp33dYrhVgJ6B-Qvh76vnDLJpEINtaDkIkuS5Z0roTPtDDhIcD0-zg6pE6AGglt76zIY5-RNU__1gki7evaqYeodN44nMcfXcELJeVXJZ1q9_aNXmcY-3YpA551Ue6sHTzB2DIArUnRXBpyFpHAx8386B-r0T7Me-YTxakaty94qYhOtFIgxy6fl-JojU-FgB07nYKRe1B6EPH-FaKg3yIVVfkdx0iwh21bUDiWmQaBPia5x-YDdee89G0IFOlgecpf221FchIm5dnSsfJ7SEpqbslYELzZr5ROdZUN7uoiSCHjVZMsNdogetwrIRErn_SYRXA5fsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۷ میلیارد دلار ارز صادراتی در سال ۱۴۰۴ بازنگشت
عضو کمیسیون اقتصادی مجلس:
🔹
بر اساس آمارهای منتشرشده، حجم ارزهای بازنگشته در سال ۱۴۰۴ حدود ۱۶.۹ میلیارد دلار بوده است.
🔹
در سه‌ماهه نخست سال ۱۴۰۵ نیز حدود ۳ میلیارد دلار ارز صادراتی به چرخه رسمی اقتصاد بازنگشته است؛ مجموع ارزهای بازنگشته از سال ۱۳۹۷ تاکنون بیش از ۱۳۰ میلیارد دلار برآورد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660036" target="_blank">📅 10:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660035">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wkhsf3p3Ny5u5rhgdpjRP_KNApHHKg-OyqEt3jbjQKe67kVSE_fI8QrC2fhGOmD3AO_mso7ilIuAcPUiTRrNkgCwaiw2gchgB7L9oiZhmaIJD1nCJkv-OkuvJBlRnKierw9CjGnk_COPiF047VG5UgwRzMJbVbWrN2_y_-wpO-NNFUv79t1W87dvskCk75TflPP1AU3p1NLejJxit4kHZb3FrqHpWADp69kM-Hp5E61fj0NVq32nHHiPhCwTIvo-3rO4lkn7FG-uDaLI7zzdYBLi7IiREHW1zmOLYz6aAKmWVFo3N1UfV0NYVI9ejjLRsJkUMjaM4bdxG_Q77uBjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاید امروز در سایه باشید، اما فردا زیر نور حقیقت
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660035" target="_blank">📅 10:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660034">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
فرمانده‌کل ارتش: هرگونه خطای دشمن با خشم انباشته مواجه می‌شود
🔹
دشمن در جنگ رمضان و جنگ ۱۲ روزه به‌دنبال تسلیم ایران، نابودی جمهوری اسلامی و حتی تغییر نقشۀ کشور بود، اما هیچ‌یک از این اهداف محقق نشد و در نهایت خود به‌دنبال آتش‌بس رفت.
🔹
برآورد دشمن از مردم ایران اشتباه بود؛ ملت ایران با حضور در صحنه نشان دادند در دفاع از کشور، اعتقادات و نظام اسلامی ایستاده‌اند و بخش مهمی از این نبرد را مدیریت کردند.
🔹
اگر دشمن اشتباهی بکند با یک خشم انباشته مواجه خواهد شد که کار دشمن را بسیار بسیار سخت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660034" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660033">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f609ab13.mp4?token=m2vQQnNIUURA8zy_-HV5pZONT1QEXBijfxwJvA5Bkiu1YfKTdjnYVDL7l97Q-BMqEXE4eCfB5n0UgBGzqPUXw03AWIgzE9P9VtpVl9GPtII1H90Yh1THKvdbzeLTERWtu_WjpxowQ23bmqQXClHxP1Uh1HF7stQ02c7bOHBXjMLzsuHQviP_o8j3zECPHhmq7Itd2YBjs4mZH2h2AVlso2Ppl6-w9XtkdhgU7lNVdH0I2hXrWmwmAXG6A6VJU3TZIRsKFaNykEJBLzuLIX0m3ijlQG-zZ9i8vcLlkEfRQN1OiYCc_WOVD620Mzb13_dy9oTpPRxy9wNf6L06KgNF0knd-P1UuZZf7GhLiCXJdSN8R1LRx4FhG136zjpRXMVgmjpmmXL5CXC42LzNU2oHYwPI81z16IeEvNEMxG6woXvteyKX-SpksOPzEWVY4Urz_jkAYrEi2K0mN--RYMnUJdLY5qpkCYGKRIxTIRB3kRD6xdjglz1XcFlgTyUhNRrJ-d-Mek-t6VgDeHwR0hnizBYSX48g_wwM0S5zmxHUYqxaXKUMHuSEUKZWVB2h6-OxorlvFqsgamw6C0FKckveNCAI8DUHeWF0Yg9M6WQErXpHogSdANL-fdQwBPhmeIQ8pPWeNqEpfVKYauKKu0RS7gHzrg5lTOoV9Fg_bWk-imM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f609ab13.mp4?token=m2vQQnNIUURA8zy_-HV5pZONT1QEXBijfxwJvA5Bkiu1YfKTdjnYVDL7l97Q-BMqEXE4eCfB5n0UgBGzqPUXw03AWIgzE9P9VtpVl9GPtII1H90Yh1THKvdbzeLTERWtu_WjpxowQ23bmqQXClHxP1Uh1HF7stQ02c7bOHBXjMLzsuHQviP_o8j3zECPHhmq7Itd2YBjs4mZH2h2AVlso2Ppl6-w9XtkdhgU7lNVdH0I2hXrWmwmAXG6A6VJU3TZIRsKFaNykEJBLzuLIX0m3ijlQG-zZ9i8vcLlkEfRQN1OiYCc_WOVD620Mzb13_dy9oTpPRxy9wNf6L06KgNF0knd-P1UuZZf7GhLiCXJdSN8R1LRx4FhG136zjpRXMVgmjpmmXL5CXC42LzNU2oHYwPI81z16IeEvNEMxG6woXvteyKX-SpksOPzEWVY4Urz_jkAYrEi2K0mN--RYMnUJdLY5qpkCYGKRIxTIRB3kRD6xdjglz1XcFlgTyUhNRrJ-d-Mek-t6VgDeHwR0hnizBYSX48g_wwM0S5zmxHUYqxaXKUMHuSEUKZWVB2h6-OxorlvFqsgamw6C0FKckveNCAI8DUHeWF0Yg9M6WQErXpHogSdANL-fdQwBPhmeIQ8pPWeNqEpfVKYauKKu0RS7gHzrg5lTOoV9Fg_bWk-imM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع زلزله ۶.۷ ریشتری در اندونزی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660033" target="_blank">📅 10:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660031">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°(منتظر)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/719ebe32ce.mp4?token=RMFTG81A70eT9fo7BbUIuXAcy528DKn0Qqps-1ZoiGzxqNzZaWcMraTaUDyAl1H0ahl3foCMeWRZAz8RBMSDU0a1o_FHxgRj19m6jJ9HBNHhBFUlE52pIltzxIp82zenAoutzp0ZZdGjAaeqbYb7KVlCrHXH5MQdX2FK511BYqDKqgGW_3DqUzToybb3LTCq_kT8TCiltr-vFnXVWObgTUdCuRiOMZuM4VXAHHE79190TTZpwSgcFaIcUtDYY2vJaG_W5HxrlatM82IKY0dwinGyO4KjeHaNw2GtaWtVmCd2MXOCxn8SdbwsBzZE3DSyqQbtSngHLM-_OIDLr9KVUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/719ebe32ce.mp4?token=RMFTG81A70eT9fo7BbUIuXAcy528DKn0Qqps-1ZoiGzxqNzZaWcMraTaUDyAl1H0ahl3foCMeWRZAz8RBMSDU0a1o_FHxgRj19m6jJ9HBNHhBFUlE52pIltzxIp82zenAoutzp0ZZdGjAaeqbYb7KVlCrHXH5MQdX2FK511BYqDKqgGW_3DqUzToybb3LTCq_kT8TCiltr-vFnXVWObgTUdCuRiOMZuM4VXAHHE79190TTZpwSgcFaIcUtDYY2vJaG_W5HxrlatM82IKY0dwinGyO4KjeHaNw2GtaWtVmCd2MXOCxn8SdbwsBzZE3DSyqQbtSngHLM-_OIDLr9KVUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
بهترین فیلم کوتاه امسال
بهتره اصلا از دستش ندید
قطعا ‌دو بار خواهید دید</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/660031" target="_blank">📅 10:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660030">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z85xkVzCJ4Vmiia35UWHS5PIse07mMCbKU8P1Lw_OVE-bNjdmdwmDoqqqpcNAf0o6SVLtuwLGYTB0gLseqOp-BPj-Ho8wnGhi1yLdKJ5C7R5J-SImgD2Z28LrWflDAYdv5svDmsjm8ztOrwjImCjJiFjGh66VdaQ3YR9eS0FR3ikFpNJscwf9UmDDpUwH2j0JU84qG6IQoTPjO5zvmoV0SWnN2rh-fXN1isNoua5ROhIuhtlDKFX8Cyh7rtn7mpiZcoOiX0YDKp1eHnjAeJLa39qvNFvFhEjo-ng9KY5cMaBAKclKXy87qAH_kFBG9PMJ5mEfF5JROQSIIsedvQLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده نیروی زمینی ارتش: همواره در جهت مقابله با هرگونه تهدید دشمن و حفظ دین اسلام و کیان ایران اسلامی‌از هیچ کوششی دریغ نخواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660030" target="_blank">📅 10:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660029">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEOIi0h0e6XDl1fOfwvEUQWSDuo6RkeFao3QIvrsHK5r6yqtOybO8IzDKo3Ns1FSzLwH-b3qjVF8mH-QwZSQxWMB71Lr35tzX4m1y77uY3A_2nsmWPAiqWLl-Ca_ggweI_dLyyb7dJPWzWi7mVehjwL4nRsqd_YMwaN27uPcvBDz-BIwIaU3g-V6TYCfZq9Br2Sn0tfi9uAHcMSIPyJRbpV-THM_uGvpwriZHic1EYWuTc_TXS-4212aYzXLxpUVxQ4O9alv7hAT1tMjb-_Rdkc56ISasBX-zVOyUZ0Vyqb0pncCj4HAw429Y348P4Iq1na0GA7nqQrNDZ_UuIQWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طارمی و الهویی در فرودگاه گیر کردند
🔹
کاروان تیم ملی پس از دیدار مقابل نیوزیلند در حال بازگشت به تیخوانا است اما روند خروج مهدی طارمی و سعید الهویی از فرودگاه لس‌آنجلس با تأخیر و مشکلاتی همراه شده. به طوری که در حال حاضر تمامی اعضای تیم ملی در هواپیما حضور دارند، اما این دو همچنان در مراحل نهایی خروج از فرودگاه هستند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660029" target="_blank">📅 10:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660028">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ونس
:
ترامپ ممکن است که پیش از روز جمعه، جزئیات توافق با ایران را فاش کند
معاون رئیس‌جمهور آمریکا:
🔹
رئیس‌جمهور دونالد ترامپ ممکن است تصمیم بگیرد پیش از روز جمعه جزئیات توافق با ایران را منتشر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660028" target="_blank">📅 10:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660027">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZE9GaE7H31kMwDtxGItZ_BfTPMKLBoYuyGufqiWbAH51YMpffMUlnzNwioILwo7N-RYIhKIm3p1qZVWwLml0KjFVrhDYDWY3C1iazAhTo3aMRYMCn_bYvEDH4RZGPrQKy77eBEs7ofahfS_dB_SoZt9dW_73uWYeA0rcvezzHz7_HRL4uiY_LngdhF8yOO1SBnuBl_KpKNHt6XEd1EAkmJbkAGSeoCNirGdknlBTSsJ7EvhacP9LQA21qTvpo9VMDjjI-AaM-OgNPQty90QVK3FYN7XHmFOobqZ6FryykEcZPIx5WK3U__3G65LmVcNQpikMNkEZiQOW7sUcS0S1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/660027" target="_blank">📅 10:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660026">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
صادرات مازاد پتروشیمی آغاز شد؛ بازگشت دو مجتمع بزرگ به تولید
🔹
معاون وزیر نفت: برای محصولات مازاد و انبارشده مجوز صادرات صادر شد.
🔹
مدیرعامل پتروشیمی: دو مجتمع بزرگ دیگر این هفته به مدار تولید برگشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660026" target="_blank">📅 10:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660025">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRTwLGyllTRNt5PV_wMcOhFb0n9rIeX5SsKInUtdEBQaNkb_6WRHQ8A4FmoSWAVlrfwKzcLZxAuKnO-99T7_0kni6-hMGn8izCbzR5jaYj7J0jlPsSczkWI6xNT6x8gFGO30NQ5v5SvNd5uUNRpB_8q3IAPwf9bDalBtnC-SotP6CVjuTNM-K-yyjlvUcweHhRfhDBkden20EKZcuyh7lvxSktH3oxenWPS0aRfyAxlTEmhndllZDfNvjIP-zTmznlwJJ-0UkH9JNDzDcz64cu-lURsGLOD443pp_Sp2K5VnrQh0ErVud9yWmXw4ziDdrdrKvBrdCT4YIOAE0tYvCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویزای مهدی ترابی منقضی شد!
🔹
مهدی ترابی به دلیل ویزای یک‌بار ورود، پس از سفر به آمریکا با مشکل انقضای روادید مواجه شد و فدراسیون برای تمدید آن اقدام کرده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660025" target="_blank">📅 10:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660024">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/161a83f9dc.mp4?token=hRyoZ2EK4kyrWC8sV1cfQFbDq8JUYuNhFJ2eHvf4cZWBp90Ephqn_8G-7-ey9wkzx7_pxd9WJa10FfIzeRAqvr9poZrv1fSNM2Ft_kMvNoSfIH9fkXLdx_FxrMgR9Uc7Et7mZ7FPaXRjePjwvlLXQSg2S5EEkThfqWMqkikwsB1LIToooEHHZflnOLNMM6fbV5sVyXt9RRPL9vbH9JgMhnghzyvMvrxy2brw-lA0DHlduLJ9Sx-fn5V_Z0QNzyL_r2SZ_ctCRSqcNHEtWgJ0xl2xO1rLUy7NERoXPxM96CKQ0YJ5vyWDSIx_mN1vB3WVpNHQml-7XxfUltGEGN6jUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/161a83f9dc.mp4?token=hRyoZ2EK4kyrWC8sV1cfQFbDq8JUYuNhFJ2eHvf4cZWBp90Ephqn_8G-7-ey9wkzx7_pxd9WJa10FfIzeRAqvr9poZrv1fSNM2Ft_kMvNoSfIH9fkXLdx_FxrMgR9Uc7Et7mZ7FPaXRjePjwvlLXQSg2S5EEkThfqWMqkikwsB1LIToooEHHZflnOLNMM6fbV5sVyXt9RRPL9vbH9JgMhnghzyvMvrxy2brw-lA0DHlduLJ9Sx-fn5V_Z0QNzyL_r2SZ_ctCRSqcNHEtWgJ0xl2xO1rLUy7NERoXPxM96CKQ0YJ5vyWDSIx_mN1vB3WVpNHQml-7XxfUltGEGN6jUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعداد فالوورهای شگفتی جام‌جهانی ۲۰۲۶ سر به فلک کشید!
🔹
وزینیا، دروازه‌بان کیپ‌ورد بعد از درخشش مقابل اسپانیا (۷ سیو و کلین‌شیت)، از ۵۰ هزار به ۱.۶ میلیون دنبال‌کننده در اینستاگرام رسید.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660024" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660023">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1bcc6de0a.mp4?token=i2_sdtUu6fY44DLxw8OSoOb7BTs96VRzvFZAves8fYp-0uw7KsZdxGTJTIChBduIwOtCWH9oIodOzImIqvDSOpSwemT2Hhg06Uhs1Bdd5qluul3N3Ei9y6H5q6qQ-_e3tOUSqgXAyqDiJ3vVwmqpFuI_QwG6vKssPsHzUYjyLd14S9upAAFyANew2IUcgmNiXqgfQTs-_SZAXUaBWvBvlM3aM41q2wETDzo4JrdkBaUdTgqTrRVe1BRHs28Ljd5Hvu69lg8HrnFQi0m96UjZGEJwt-XPAuOwVe1xhgHpp_QG2LHZQO2Y6Gq9yzuAg4aaWLnEnIfgVVlkXGpy8XZ8qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1bcc6de0a.mp4?token=i2_sdtUu6fY44DLxw8OSoOb7BTs96VRzvFZAves8fYp-0uw7KsZdxGTJTIChBduIwOtCWH9oIodOzImIqvDSOpSwemT2Hhg06Uhs1Bdd5qluul3N3Ei9y6H5q6qQ-_e3tOUSqgXAyqDiJ3vVwmqpFuI_QwG6vKssPsHzUYjyLd14S9upAAFyANew2IUcgmNiXqgfQTs-_SZAXUaBWvBvlM3aM41q2wETDzo4JrdkBaUdTgqTrRVe1BRHs28Ljd5Hvu69lg8HrnFQi0m96UjZGEJwt-XPAuOwVe1xhgHpp_QG2LHZQO2Y6Gq9yzuAg4aaWLnEnIfgVVlkXGpy8XZ8qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵ عادت کوچک که سلامت روان شمارو نابود می‌کنه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660023" target="_blank">📅 10:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660022">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rol9KTErSu-2UFStpXghbxQKkNt_EriB8KcDqmy7X4TBUIDFGM0_w9NNOPJxiRc7FT_Uztp05KCQHPaTrUO9m6pT5V-6W0KoVb04naBAyqoic46mfXYdM1hScmO-nXFCv_vf_sUj3ED0VbOoiyt30ib28AV0TzxLvfVNi2bqCb8Nj4sJIqpt9HXHQFBHQtSCOeuSSggt00Bdpp19Pfxq80wkyeoBVq_8odueCR3jVJ1u9fsIOrOzmJwRa6jDclKcjqKo-2c_K8wiKPcFIOvoRwDPaUYi3tcTKtisjoUqZTh1QvfIUTH9qkoq72--difi50sWUId3wMmlsEswOKF-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرویس‌های مختلف بانک ملی همچنان با اختلال همراه هستند
🔹
با وجود گذشت چند روز از شروع اختلال در خدمات بانک ملی، بخش‌های مختلفی از نرم افزار بام همچنان به روال سابق بازنگشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660022" target="_blank">📅 09:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660021">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سند مالکیت پهنه‌های اقتصادی و شهرک‌های صنعتی ۳ استان زنجان، قزوین و یزد صادر شد.
🔹
درگیری بر سر جای پارک خودرو در شاهرود به چاقوکشی و مرگ یک نفر انجامید/متهم دستگیر شد.
🔹
بختیاری‌زاده فصل بعد هم سرمربی استقلال است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660021" target="_blank">📅 09:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660020">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI4Sbs_mdKOI7RtBs0tjGikQFLY3YsEJw92nLvnWz25m3LoZHMtUeHw0Da4l5cOukRFgyU-TVvU-wtrzY6mfohGNWGI9BCh6m5rOUrUl39CssnvByCXYkIbL-F6Jb9sB--aI_I2qv2XTsJ9QOZORDFrAnXxeM-3QHjx07acEBqjxp3nyi6RW6Q5Ah72IStLvGwDQRBJQexoYQH9DOMtsG7Yfs_Cdkk0zNobGXqJnXvuKXWeLPnOe1Mr5D_T91pMrKPn3H8_VD6DDgPVjprgv6nzmhCltTZmflxTlWVjIPu9k-GNplzk4v5RlocJ7e9w-Dx6k6mes6KcAWvxGlV3T3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از تیترها می‌شود فرار کرد،
از دوربین‌ها می‌شود پنهان شد،
اما از حساب‌کشی تاریخ نه
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660020" target="_blank">📅 09:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660019">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فعالیت رسانه‌ای مشکوک در خدمت باند فساد بانکی و بیمه‌ای
🔹
همزمان با تشدید روند اصلاحات مدیریتی در برخی بانک‌ها و شرکت‌های بیمه، تحرکات یک شبکه رسانه‌ای مشکوک با محوریت فردی به نام س.آ فعال رسانه‌ای خارج نشین در فضای مجازی افزایش یافته است
🔹
این جریانی متشکل از افرادی است که خارج از کشور فعالیت می‌کنند و بدون برخورداری از سابقه حرفه‌ای مشخص در حوزه رسانه، با انتشار اخبار جهت‌دار و  کذب، در پی ایجاد اختلال در مسیر مقابله با فساد هستند.
🔹
این شبکه با استفاده از صفحات و رسانه‌های مجازی دارای مخاطبان غیرواقعی، تلاش می‌کند افکار عمومی را نسبت به تحولات اخیر در نظام بانکی و بیمه‌ای منحرف کرده و از برخی مدیران مسئله‌دار حمایت رسانه‌ای به عمل آورد.
🔹
دریافت مبالغ سنگین از مدیران در معرض تغییر یا برکناری، با ادعای توان لابی‌گری و تاثیرگذاری بر  انتصابات بانک‌ها و موسسات بیمه، بستری برای اعمال فشار رسانه‌ای و تخریب سازمان‌یافته این جریان فراهم کرده است.
🔹
انتظار می‌رود دستگاه‌های نظارتی و قضایی با دقت و سرعت، ابعاد مختلف این پرونده و ارتباطات احتمالی آن در داخل کشور را مورد بررسی قرار دهند تا حلقه‌های فاسد بانکی نتوانند از این جریان در نقش منحرف کننده مسیر برخورد با فساد در شبکه بانکی و بیمه بهره ببرند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/660019" target="_blank">📅 09:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660018">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSC1CtMahBGO9AusrjHxxIQ0jwjLLrFvEYfKSNhb2oO5xeFFmeyR5rivpN1rNEldse0RcRYS_nz14fBhnX_MKqYEY9F04VKgNNSsO7tk2AASwjr_z_lYQB23khUR4clx9mlXZHPXMK5-M1G4xvsweAEs9QIFwNGoGmtTjs3LeD6psmlP0n03hp2ybGx_pUWWBz_qn3TZN49O9gKICvkwYujH7GfGXG7goBrAM-SqmQPfme1Id4pf6sZCvVbQaWyKymqzA8keEVTn2Nwv2tJx08tOrGRwyXrFsDNTJ82ZRvoFGEK1a3PVOTE675aLwqXEmIf4hMmN8iinCAjxO2ZB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا به وزیر افراطی صهیونیست ویزا نداد
🔹
دولت آمریکا روادید سفر ایتمار بن گویر وزیر افراطی رژیم صهیونیستی به آمریکا را صادر نکرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/660018" target="_blank">📅 09:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Efmw-M3IlMlc-xKRjJBGEoya0NA-MgFgqPwWAFMbrSJq0Zm_Xujj---xDCfrbxNQA3nG_E7cTTGty0rHw8jgYWVkfPz4PVDuyhLt6bmBuUp12IdAd4dK5kF8RHWarf28sRwrUnLMXqMn-MS-OLViVHDGraYRjGcEYwT16SQA_pfgcFgkrTNOgln5hh1ouHBZaRbfQzHKKmcnjjQnT1Oi9AqFlbJFnuIxoqQmzH6x8ZLBhGkd--vUV1bc7Mv36pcXIDfiNYxfum6Y4F__MCrz7X_2dTEAMCPaHKGHt4fey4tKm8I8bxQuy4X-_4yHEf5Nra21lEg7RI3Gzq27cDw2Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMkArQ4nI91ZQxIluBIlSJNokB1Te7FNb3lm7ZFqI7ySippvC0XTbbc2UYdFd4dQp9P6Xufi4y4C5CS_uf4GYZusCJQi_qjdi1JExkglYX_Iva2mBzOzJxGjXG_-KKgk0BpSZ3VSxcSFqyxtVj8qUPpFYeHJR3_2Jcr6ofvaWUGQsyaHhwvr2v3k3kWS6ODayVF0b-eBxt9lVVAF8pA2aFzUBB26b8ABGQvpYbmRxsGXKqeP92N50BAo1vuvqa9vRy0xj2Fm6YHlrrxI-yH96BmxEOVuRMjrogFqCSwxY6F2rnXP8hWTIlLXId_t4nqMPpf_V91s56tTZyEg1eOvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7-CQx7_1otTc1gqSq-TggbFiZkYCNHNo2QCv94-bn50d4Cc9J_dOkGyrx7BKlmY8oIg2m6ZsTdsVUNNB4lGuNzGDto4HxpWHXS689ray3fLAo6pJpEhpvY3-n8j9xCGfZjQypKJiKsxuPd3NwiT7TQqTtC5dMsvPlnfsegWG3CLRTz0WLCupUxcS0-K7GE75KHQBFbZYJXL-2OWD83CnsqjQqs3kCZn9lwhEVUwKQb5GPe3SKhAbsU-_tqHZVxEV0eilgHbItoN0kJ_8Rie1SIVCw7xOkPGaVhNjlOl-15uz8OxPJ2GX0erzdNuxvwWKUbjVPgCefmXOaziob-lBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qbr-_rfJbCoSJtdi-GGhIGKFmIIjXHoxMgJ0MRz7408RNCLeNDqn9z8Fv5oMbUOAiv8l-tjSyYjsQJw3HjaY374TCEvooWW0jX1qe7S4a7XXNMKRVa0vUXZLO2z2b4eETpqzqnA9HvgZ5n-Kgz6XyCuIYbeIepcNwgoj8YXLWaptww7JkAQi6eO3XFQDQYbJKZCnnK1Vs2BZ8IJugiEB_kTJlwf8X7CrARgyMv7impMtn7TKizfTbn5ek1czOgcj66iHylmF_BbP7Xx8bS0Dzm6a5yILUp3xd65zi5bLPpIAZUqSTMHsIcjwCLZa1m1BgsfXk3TyLxtGOgan08CoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2HY8zIZWLsesCDDwwm-C1tG0kwbyO7Mz5Lya-4Ns8YJ5fec5djInU-bvKxGWAnEyF4dBzFIL08WoBMcorjrUuLzMh0okrArzEEHNVaWoERyWA6T6m11CytT4CF6kWcW3t86lPkGkC4Dz3oWQrtMJgMKTTsXUfsD8YJ-nuxwFtF4XdeGIKCwppoQstN8RurrbmC37SljblOC9VkC3E31KhcGA8FllH7WezJP4AP1iFUuX2keWyW2aY1ZUGBoExleHmk0TDqY1yDR0OjI09n5Q7ZTtF5hSThhJ6snkvFqHVPMks6N2Yyl0ocC14TbmPcupbL6rCi9c4aecfFz_V9Aqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCFcJR33QAKQrsQflMx0u6DD1nqyJ8v1Sp8VPR8ESOSk5uEKLNoCdV6UvWLh6jGMZm-XmDUIy0ktCmp5PlToEYtNZGUQuW0YaGW_DJ6rI2SShb1XhIYUuu6k6piU37rnF0w1ibFPJweQqBlHQ3RezwVN9rR3_OfD5ajhGTSGwrSL-n7eu4zP0WvObXC_KCNP2KoluXE277fuNRew5AXwzq4pjTVAIIULo15BSW9WHJVSSwhjXgzJOxAtOQfdFs6_UwgJ8r-YYATe8zWNzsO9NFsv0AB5L1mIdscbYcjkpp1tUDF9zUMgb8Bww-lnQAaBIU66Mv17Un_jonipeh2dQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
همیشه دروغ گفتن، از اثباتِ دروغ‌گویی راحت‌تره
تهمت زدن، از اثباتِ تهمت راحت‌تره
نااُمید‌ کردن، از اُمید دادن راحت‌تره
بی‌شِرافتی از شرافت داشتن
خیلی خیلی راحت‌تره
خلاصه، تو خَلوتت یه نگاه به «
کیفیتِ خودت
» بنداز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/660012" target="_blank">📅 09:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شهردار تهران: پیش‌بینی می‌کنیم حدود ۱۵ تا ۲۰ میلیون نفر در مراسم تشییع رهبر انقلاب در تهران شرکت کنند.
🔹
وزیر علوم: حمله به دانشگاه‌ها باید در ردیف جنایات جنگی با پیگرد بین‌المللی قرار گیرد.
🔹
احتمال شنیده شدن صدای انفجار کنترل‌شده در جنوب اصفهان/جای نگرانی نیست.
🔹
سند منطقهٔ آزاد مهران صادر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660011" target="_blank">📅 09:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660010">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403e4e5702.mp4?token=DDEPy7PViZIFA14PotcmbUdhlTMqv38A5vHpvXMpvVtSp7uChSDoT8UQViLjIFVo93oWOXEj_gHizMOX6WoqcTE1UBmtU2LOAyHwLR-6ehaaoLdkVzJMVyO4z6T-1GlX38PtsS60vYW8Q1mDl_Dpuh2GBDu5Cxi7uXEEHgriuulFTMwRqQfFY_8a3AhTaN6oGmTAUNhjcowP5k2BWx_dlwvBo_6aEcLiDzAu8WTz1gSFHOntC7XucWXWcB0ftayfvnO6PZ99BpzhsWGv51KcVRnSWNZfjq3uNrkfw78GOMIUxWMO2auTmkKR_iGgRbVfF7EZncneZH5TrnUJCFTroQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403e4e5702.mp4?token=DDEPy7PViZIFA14PotcmbUdhlTMqv38A5vHpvXMpvVtSp7uChSDoT8UQViLjIFVo93oWOXEj_gHizMOX6WoqcTE1UBmtU2LOAyHwLR-6ehaaoLdkVzJMVyO4z6T-1GlX38PtsS60vYW8Q1mDl_Dpuh2GBDu5Cxi7uXEEHgriuulFTMwRqQfFY_8a3AhTaN6oGmTAUNhjcowP5k2BWx_dlwvBo_6aEcLiDzAu8WTz1gSFHOntC7XucWXWcB0ftayfvnO6PZ99BpzhsWGv51KcVRnSWNZfjq3uNrkfw78GOMIUxWMO2auTmkKR_iGgRbVfF7EZncneZH5TrnUJCFTroQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش شهرک‌نشینان صهیونیست به آرامگاه حضرت یوسف در نابلس
🔹
گزارش‌ها حاکی است که شهرک‌نشینان صهیونیست اقدام به رقص و آواز خوانی در این آرامگاه کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660010" target="_blank">📅 09:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660009">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRbhOL1ewRVK21n7eKCQ6A4H8Cry88aqqBdoD7WWsCI-OIKyNUo9i27CJoNiyhdn_tG0IYbjjI1N3mws56G7xsr02elfvrIEiXJ2Wl6BtQV398HYpZCrqqZ5SAnSHUlNm00MsB8bmyZXkNeUg6D5LIldA_E3bF7frEYqJIhvhhuf6MWXGGohX2eoha2eSmTqMHNWw3ivu8vPzOGmi2i286jjDvTY9Hum4rP7pQtCF9z6drnad5Ki0rQjRQ11IEyBpVtj5gA29pMcIJPahlEdDckSvjmnO8pjvjRpKVYfUz_EHONWmnf3e3xqkJiSCZu6m0AUpiwbHCoTkvh1VfWywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس ۵ میلیونی شد
🔹
شاخص کل بورس ۱۱۶ هزار واحد رشد کرد و به تراز ۵ میلیون و ۹۷ هزار واحد صعود کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660009" target="_blank">📅 09:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660008">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSuXHOTwTEfU3PMfPyWFnEEPUXPWifryVvuvLqHWC2z53-2ieSD3T9Oz8xjl60Xi_8KdpgSuEBb8XmyVWxBmE6X3qJPHbFiAgrZ0D79qux87lmuHDpiaERbR85HBmA6WYW3_3yitoTqn_pfW6dfP9rZ_upRcmrdJYN0PtFqVVhowUwbDaxqqk3-89HOsKVbScNAHrjaPO4aNnnQ1_YyFxMwGFXZEyYqI07aBjRbf5BrR1BOrrlILVumVWqRnSljTBRke_VCCz1KhZxXGh3-JHgRs0PesVszY4FKNmy2um5oL_OjmWHyrzJoE86kDk2STEW2cT8-unDLqVvmXV1acOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو رسما برای انتخابات اعلام نامزدی کرد
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660008" target="_blank">📅 09:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660007">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
جزئیاتی از ابتکار شورای‌عالی امنیت ملی برای خنثی‌کردن بدعهدی آمریکا
یک منبع آگاه:
🔹
شورای‌عالی امنیت ملی یک سازوکار «گام‌به‌گام و مشروط» برای اجرای تفاهم‌نامه تصویب کرده است.
🔹
بر اساس آن، ایران فقط در صورتی تعهداتش را اجرا می‌کند که آمریکا هر بند را به‌طور کامل انجام دهد. در صورت بدعهدی یا تأخیر آمریکا، اجرای تعهدات ایران متوقف می‌شود. هدف این طرح، کاهش ریسک نقض عهد و ایجاد ضمانت اجرایی متقابل است./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660007" target="_blank">📅 09:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660006">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFAEP43jqMQ0oV--SuIuJqP7L_BgSFDYrF-W3NXjuUGfgi_3CgZlBaPfb0ZAOdir2nmD1bqCHVWj-J3luHyvNlQ7eVrjcyMkXDAjP4QmrpQHvBxhtkARRa2wW1ZVArls78tpXzVg9UKuuaiNsC46sMg-9mwXObxk2KxEsA6zr23JpfzmjNf28qr8_b0qxOKnCG48xKqw9j3DvPUiypuDNkkPcq6OXGJL2jYkfdZ_PL3zn523gYGlMh3ouvP-rtUaJEgpdlAHQfQFxklVBoufDtudfXBEI2KM9EWlXQTuTUZ6CgMO9e_v-QusdB2UBMBzW59cR0_NH05rAjtkdzhaZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صلح مسلح
🔹
پس از ماه‌ها فشارهای سیاسی دیپلماتیک و نظامی از سوی آمریکا علیه ایران و در شرایطی که واشنگتن به اهداف از پیش تعیین شده خود دست نیافت، سرانجام با میانجی‌گری برخی کشورها، دو طرف بر سر چارچوبی مشخص به تفاهم رسیدند. این روند بار دیگر نشان داد که اقتدار و توان بازدارندگی ایران نقش مهمی در سوق دادن تحولات به سمت گفت و گو و کاهش تنش داشته است. هر چند سابقه بدعهدی آمریکا در توافقات گذشته همچنان موجب بی‌اعتمادی تهران نسبت به هرگونه تفاهم جدید است، اما واقعیتی که نمی توان نادیده گرفت، تأثیر قدرت ایران بر معادلات موجود است؛ به گونه ای که رئیس جمهور آمریکا در هفته‌های اخیر بارها و به دفعات از ضرورت دستیابی به توافق سخن گفت و به شدت خواهان تحقق آن بود
🔹
هفتصدوهفتادوپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660006" target="_blank">📅 09:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660004">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2ecd2e0c.mp4?token=cXnpou8Bb5MKN51Bc8KeaR6FXwIMvLCxPQEusOLQ254mPmx0l78KWF_Q0O9KrY2cKUtvyyJY9R9F6bbMABdjXBshUtt0iPo6kpkzf28QAFcVoH0kIWdO5ah3Ut24bWSNuEzzWbMnnTMrAzrl9jKLvtr0ixzaK1Jbs-u3XipvdRfndczpMulNvpYhLTczKnGUvRd9FQo0uP8Poo3pLKsDxkiTDctQ-G7wWDVgIUgToiWHghXjClfs3gaAOjoLoZjCiUP2TIbojvsY7_JHZnJ_jHvbbP08UZhrOLOGrvApKm6Iv0dOXOBDL7ch2CBWFEHNOUPV43hAAcIWGpf1SvO8-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2ecd2e0c.mp4?token=cXnpou8Bb5MKN51Bc8KeaR6FXwIMvLCxPQEusOLQ254mPmx0l78KWF_Q0O9KrY2cKUtvyyJY9R9F6bbMABdjXBshUtt0iPo6kpkzf28QAFcVoH0kIWdO5ah3Ut24bWSNuEzzWbMnnTMrAzrl9jKLvtr0ixzaK1Jbs-u3XipvdRfndczpMulNvpYhLTczKnGUvRd9FQo0uP8Poo3pLKsDxkiTDctQ-G7wWDVgIUgToiWHghXjClfs3gaAOjoLoZjCiUP2TIbojvsY7_JHZnJ_jHvbbP08UZhrOLOGrvApKm6Iv0dOXOBDL7ch2CBWFEHNOUPV43hAAcIWGpf1SvO8-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پالایشگاه مسکو هدف قرار گرفت
🔹
پهپادهای اوکراینی به پالایشگاه نفت مسکو حمله کردند و در نتیجه آن، آتش‌سوزی در منطقه کاپوتنیا در جنوب شرقی پایتخت روسیه رخ داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660004" target="_blank">📅 09:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660002">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQ2OQqVqaWKmYg7dICERQrJPsjdYPaPTYWFNYyRCOE-I3_y1MUbYCcgVhPviiudY3QUYVOQwsCJqroCQC8Wvi8RGDGePf2dJ3elMVip7RI_BU2uMPoLFsveeCIZ7EE8Xo_biXrF53k8rlwVG5NGLs0qgWT5DG4x--3tVIjjzfm0cf8W5VZ-wp0MePZAhzVToyp7NZwAapPUcif4-6CaafD0PO7_mKNq4bKAJI3v2hTWOaZpxPG-OBM7LceAxW0BV25HVCrrbksogSC-TniBtJptd7F9aNBrmzY1rLS-C8-gy1MqR87HZj-N5ntQSL4_i7MthEqV1RB4nzIGm28PUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-YBkKYTyRBdc91JzUdhoknJ_z_5vo_97KzFPll3FhNOE_bByv44D8xBoklrPuDICV6YZv1l7cgeT1TbouFrMjfu4HQN48DKBgTlhr_Si-jIx-9OklIcHZU7qnqdBMlmVJD7mJkzZXBmFgP-NWHwiavTd8Z7OpLYbWGAlQJO5net6gtC0yzDY7eH5DVKpDoVJFNi-PQjm7c-M2Sl4m_jfIQywgwWDNItK3EpyMtnCEatGa_dxuSC3GH5eoNj60K9JMZMrFUaHeD05j7PqsP9KxMZuejOKYXR8t3geQk2eDtpSXj95-y7Ie_HKoBmXQx2z9HAoV8yU2Z0GZPncAkQzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور مهدی مهدوی کیا در کنار اینفانتینو، رئیس فیفا در ورزشگاه
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660002" target="_blank">📅 09:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660001">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ef9aa2ef.mp4?token=fBJPW2ANg8TVV8h6ArU_l7S9SBHkT85BUmiAvQ72xwwNffHEvFkTd6OCj5XbL108M7vI4pr5A2iqEKUvxcGiY100UWleRc9cYhllV_8XNbI3oFeymwVY-rFULKV4gVSKZoCKJsrF6T0Iaw73clTxZsySEhWE0H0pZlJMKkcM0VNHfz7D4LRdZNwUlRFCw2DPTyUB-mK6Aws7OwfDYr4hykYNCENZDZXLkyJund7JrGU6ibSq_hSahW9fNfVbKNJjAoCUk3RWTNoNlMcdvb0chjR3PBICyaBddK_I5tE1S7BrMCUfJwJIGDLzjLWlk70jMhYFM53BHMko62bwFrAR5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ef9aa2ef.mp4?token=fBJPW2ANg8TVV8h6ArU_l7S9SBHkT85BUmiAvQ72xwwNffHEvFkTd6OCj5XbL108M7vI4pr5A2iqEKUvxcGiY100UWleRc9cYhllV_8XNbI3oFeymwVY-rFULKV4gVSKZoCKJsrF6T0Iaw73clTxZsySEhWE0H0pZlJMKkcM0VNHfz7D4LRdZNwUlRFCw2DPTyUB-mK6Aws7OwfDYr4hykYNCENZDZXLkyJund7JrGU6ibSq_hSahW9fNfVbKNJjAoCUk3RWTNoNlMcdvb0chjR3PBICyaBddK_I5tE1S7BrMCUfJwJIGDLzjLWlk70jMhYFM53BHMko62bwFrAR5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی رهبر شهید برای صدای عزیز ایران انگشتر انتخاب کرد
🔹
قابی که در آن رهبر شهید انقلاب به زنده‌یاد بهروز رضوی انگشتری را به تبرک هدیه داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/660001" target="_blank">📅 08:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660000">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QedFnhlC3kTe70WRpF3bjHIpG_wpAC-xmejYdS3ZysYezgTCEzd24dqdMb0_x3YHGCbK0_v9Rzb51UivnVY8S2dboW4C8ZnB8YWEPVyI_WlOVEIMTeNoxUJvj6dBjb-q8X9ULSdOdeP7z0Ip9sRofKfhqbzjgPGB3WJ4RYnnCVS-s5mCqpfSyMko-f8V_KZyS1C2ZhXa4iRdLuYnjFQauCcuQKHP6xNanEf-LbBYDNlWkzRYZx-qeADM_omVHP52R1x4uQ37JTl-KKMDMFzOOs6oJrsV9UELWA2esvqItODKknbs3H3MLL05ZuMrBqzJwvN_AB08sDUTn-HhKxvjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلسم کلین‌شیت برای بیرو؛ حسرت بیرانوند ۸ ساله شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/660000" target="_blank">📅 08:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659999">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
مذاکرات تحت اشراف کامل رهبری است/همه چیز محرمانه است
روزنامه خراسان:
🔹
مذاکرات زیر نظر کامل رهبری و از طریق شورای عالی امنیت ملی و نهادهای تخصصی انجام می‌شود.
🔹
منتقدینی که محرمانگی را می‌فهمند، چرا امروز طلب شفافیت دارند؟ بیشتر منتقدین فعلی، خود از چهره‌های سابق تیم مذاکره‌کننده بوده‌اند، آیا در آن زمان جزییات پخش می‌شد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/659999" target="_blank">📅 08:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659998">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78b92948a.mp4?token=p5CydiCnP6kwEqhR3V5uMgqnapCeEdCLzYlzMxxaT1DZ7Z9Rd_rArHuJiJRzoAxGx432RZUWbqgji2zTi9Py6d_3DLIuToWP4WZQSKdLSYhVfZ4h_Oc7yIpym-5SnVxhL30NpWjY6XLsxkNymNCMDZSNG5cwXfvCUiDvCciaO6m06_L1B6-uY96QB1f-vpjyifLSCgLJ6ICOecSbaUuAo4DyX5RZ7M7GNcIMSzK6DxzsL-bTFTDqbuEhIqIRzltOoJAQdH3FaUXN6kER9MfI_Ise06pvgDnP7esTSO43AftHsXWmhYX6IczAnp1xP5adOAvES7jpIZpmZVAnXmbUZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78b92948a.mp4?token=p5CydiCnP6kwEqhR3V5uMgqnapCeEdCLzYlzMxxaT1DZ7Z9Rd_rArHuJiJRzoAxGx432RZUWbqgji2zTi9Py6d_3DLIuToWP4WZQSKdLSYhVfZ4h_Oc7yIpym-5SnVxhL30NpWjY6XLsxkNymNCMDZSNG5cwXfvCUiDvCciaO6m06_L1B6-uY96QB1f-vpjyifLSCgLJ6ICOecSbaUuAo4DyX5RZ7M7GNcIMSzK6DxzsL-bTFTDqbuEhIqIRzltOoJAQdH3FaUXN6kER9MfI_Ise06pvgDnP7esTSO43AftHsXWmhYX6IczAnp1xP5adOAvES7jpIZpmZVAnXmbUZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد «Free Free Palestine» تماشاچیان روی سکوهای ورزشگاه در حاشیه مسابقه امروز تیم ملی ایران و نیوزیلند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/659998" target="_blank">📅 08:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659997">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
وام ۲۰۰ میلیون تومانی قرض‌الحسنه برای متقاضیان نهضت ملی مسکن
وزارت راه:
🔹
برای حمایت از متقاضیان نهضت ملی مسکن، به پروژه‌های با پیشرفت بالای ۸۰ درصد تا سقف ۲۰۰ میلیون تومان وام قرض‌الحسنه از محل صندوق توسعه مسکن پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/659997" target="_blank">📅 08:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659996">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
قلعه نویی: همان مشکلاتی که فکر می کردیم گریبان ما را گرفت
🔹
این بازی بهترین بازی دور اول بود!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/659996" target="_blank">📅 08:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659995">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_sN1ha_zM8ZUmU4THLusABqADHEZPVvmLgeqgIJqbTeDiCuiXyR7uFRfltBb5L-NsiRkNYo6k86UzLRl3pFF7e6xwDXlX5Yf3uNrJmNqxAqNjDBWAVdO-YbgNETE2Qc1AA1l78VUJDMGB_gxQQ0UIL_oWcUUAKlgG-JpE7YSUBpyFV1NoinjZpxvWl7MBcjVWXBhWvxVuGu4G5yVMpsYJhGSadStnUJvgrFj23SRXp475nFftOpIC2BR3imFUy_P8CRh5umvqFM1U2S9QDGDtS7ZYSSBuymvcz7u1gX_eZzxaNXFG6xlX0jFXfGrXOQf0Cyy9Aa1jAiGMRUFhzivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی علیه سخنگوی کمیسیون امنیت ملی مجلس!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/659995" target="_blank">📅 08:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659994">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCqykSpaMDskEVRQkstR0hlg4wktwCWnZj7hn1gO0xnXO1kWtjwVDhZgTQpdGBVbpQ2Jmrbj1s8Lp_57HXQCYzQMUBM-FwwQugm__oIU6avvwd2lZD_c3wmS1PLh8nmqLVBrFOk5jDMDn-bPHcigYSUebPtyO9Nfedmxi9W0STAyO4-zIDWN6pHetcD3rX7OJ3Zopx9plY4yh1YZGySrQ-MdsGryydWHP3AO6j3HsPaqWAboMzdkNNKTLmNCoyUhDC3GL6XjpcodQ6SRhtgv10ou9pmWp0AhJw4YC4gHjohThr1vjDpc9uwqbID6GvB5Eva10nV1b5x1UVGsHUm3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلون میزراحی: ایران شکست نخواهد خورد
🔹
تحلیلگر سیاسی و فعال رسانه‌ای اسرائیلی-آمریکایی با تحسین جامعه ایران گفت مردم ایران در شرایطی حساس، با احترام و همدلی در کنار یکدیگر ایستاده‌اند.
🔹
او ایرانیان را جامعه‌ای آگاه، تحصیل‌کرده و متحد توصیف کرد و تأکید کرد: «ایران شکست نخواهد خورد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/659994" target="_blank">📅 08:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659993">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روسیه از سرنگونی ۵ پهپاد اوکراینی در مسیر مسکو خبر داد.
🔹
انگلیس از تأمین سوخت هسته‌ای اوکراین به مدت دو سال خبر داد.
🔹
رسانه‌های صهیونیستی از متحمل شدن ضربه سخت نظامیان اسرائیل در جنوب لبنان خبر دادند.
🔹
همتی
با هدف توسعۀ روابط پولی میان ایران و روسیه عازم مسکو شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/659993" target="_blank">📅 08:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659992">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpNagbWTxoefON_93FOlEPSeaRtkE-WyZdaxFR_7H5dxP95HWf61XvoELsNtgKHGDmoQSTPf55SZpXZqPR4GWe8uQqve2tXPG_lT-6VsZovbNI80TmQkvEX32d9LqXzy4Pbm9HLD4JALqMR9iOeN0-dGuZZT_G5c3nuhewzImjHoj_omPS8y8pEdzJOoBwK9NXivUN-mgv84uJEAZD2wHowPU0Z5Kiumqb2QZS3tBVZOvvBQ20LWAKaBtQJ7dnBUdl2ZgQKbcsFzJenUazgo4ouAu0mP3mn0mHBEMMiz3Xd2epPfaSGs3fMbwjN0dpvLy_dmUML4H-Db-PY7y40UGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه مسابقات روز ششم دور گروهی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/659992" target="_blank">📅 08:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659991">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پدر هواشناسی ایران به شایعات پاسخ داد/رادارها نه‌ باران می‌سازند نه جلوی بارش را می‌گیرند
محقق پیشکسوت علم هواشناسی
:
🔹
رادارهای هواشناسی فقط برای پایش وضعیت جوی استفاده می‌شوند و توانایی ایجاد یا جلوگیری از باران را ندارند.
🔹
باید بپذیریم ایران در کمربند خشک جهان قرار دارد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/659991" target="_blank">📅 08:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659990">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsm7O7ArHF7G1S1q1Znb1yylREbxQhrofeJthWgUsmn9tomqhKSNmELmljjb6hqbmQ8jzCGNZOrHXgCp5_Ql7UoXxsdzu_Ts_ahwQB565NwvKLIvXbgc1GcfUN90dsrMs-Kv0IZoz7_NstHZAA0mOtblbE9Y4aHzYBrpQKb3gMrA7C83T5F7XyuWSLoBAULvgzDT4CwQ84lgKQE8kZT3mhxkNCNT-r-bY5t8twwsIWYBGJGkf0A-aARXLtZClkRhok05GqUGUoGtk_wfIHS1SddyDj50Uoclp-XKGzxV1dWEDCPdC9Ro6euOoNZQAo5M2LsCUR7e8ZEl-I0lLEL__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌زمان با آغاز سال نو هجری قمری، پرده جدید کعبه تعویض شد
🔹
این پرده حاصل ۱۱ ماه کار ۱۵۰ صنعتگر سعودی است و از ۴۷ قطعه ابریشم سیاه با گلدوزی ۳۰ آیه قرآن با نخ‌های نقره‌ای روکش‌شده با طلای ۲۴ عیار ساخته شده است. وزن پرده جدید ۱۴۱۰ کیلوگرم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659990" target="_blank">📅 08:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659989">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ed6441b8.mp4?token=eGww2m6lvGcoMCRHzSdI6R1OkillKpFOc0WCVaKBPFx7tUvZusS3qBvyRbtjRLacCBKLUmUshWwBPjRHOqqir1GHdrx8GEv8Rhshn0RF4fpJnSAOqT76c6gB1RLOKwnngyGFalue74s0vCo6dgn63MYRvcqjfdre2qbmVpnEL35-9b3l97ciVoRfm3LzLSkQZK158bNIhiaVJm_qG5no8qH8Us8ZsnjTMUcdQ2D8936l6dDFpdt9tU8wa3vnfHVmXKfSE1UNmLapmORkWpwcEpE9gAcyLsUZRqWyb7_kBHtVlNMael9XcTJ9Td6DvC98VFDVLEzZzY7L2o6X2Y8APg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ed6441b8.mp4?token=eGww2m6lvGcoMCRHzSdI6R1OkillKpFOc0WCVaKBPFx7tUvZusS3qBvyRbtjRLacCBKLUmUshWwBPjRHOqqir1GHdrx8GEv8Rhshn0RF4fpJnSAOqT76c6gB1RLOKwnngyGFalue74s0vCo6dgn63MYRvcqjfdre2qbmVpnEL35-9b3l97ciVoRfm3LzLSkQZK158bNIhiaVJm_qG5no8qH8Us8ZsnjTMUcdQ2D8936l6dDFpdt9tU8wa3vnfHVmXKfSE1UNmLapmORkWpwcEpE9gAcyLsUZRqWyb7_kBHtVlNMael9XcTJ9Td6DvC98VFDVLEzZzY7L2o6X2Y8APg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه میخوای دور شکمت آب بشه فقط دو هفته این تمرینات رو توی خونه انجام بده #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659989" target="_blank">📅 08:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رسانه‌های عبری: بیروت برای حملات ارتش اسرائیل منطقه ممنوعه شد.
🔹
بخشدار ویژه خارگ: ۵۴۸ اصابت موشک، صادرات نفت از جزیره را متوقف نکرد.
🔹
ستواندوم عرفان شکوری در جریان دستگیری قاچاقچی کالا و ارز در شهرستان تالش به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/659987" target="_blank">📅 07:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659986">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اعلام رسمی ستاد استهلال دفتر مقام معظم رهبری؛ امروز سه‌شنبه اول ماه محرم‌الحرام است
🔹
گزارش استهلال ماه محرم ۱۴۴۸ ه‌.ق از سوی ستاد استهلال دفتر مقام معظم رهبری منتشر شد؛ بر این اساس ماه ذی الحجه ۲۹ روزه بوده و اول ماه محرم ۱۴۴۸ روز سه شنبه ۲۶ خرداد ماه خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/659986" target="_blank">📅 07:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659985">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین - قسمت سی‌و‌یکم</div>
  <div class="tg-doc-extra">ابوالقاسم فردوسی</div>
</div>
<a href="https://t.me/akhbarefori/659985" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
♦️
حکیم فردوسی (آغازِ فصل دوم)
🗓
در قسمت اول از فصل دوم، بزرگترین کلاس درس تاریخ را برای «تاب‌آوری فعال در برابر سیستم‌های ناامن» مرور کرده‌ایم. کسانی که برای تشویقِ امروز کار می‌کنند، شاهکارهای فردا را خواهند باخت!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/659985" target="_blank">📅 07:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e11245244.mp4?token=mdT_ukm7xCK-Sy0uO8VmaeV6rDOdiSZvrHcIygk1ctzRX-Kq7arTPbputpxDAJbEL3i-iEyCIEb3mVaTvz7vLZjYI6r0MyeAKr0D1Z8TLGS4W2P1ID-dytcVcfW3fDZYySxlll6Vbv4ILF0876ssN4-pGZo99CCJ4JQm6YSQnc0TLf-xm47-xqKLJVcgx6VYdLRvvbIjtSwAKW0e3q14TAI7cZUzkOCb9aHlm2tNdegP3yOtcLsTNBmrKWiCMeYE5H2hoH09eib6N-U4ddBZ-xnKemKSov163fgXISr0MbTROIuV9nLk69kCk6lDKXbajczA4gRLQf0dB96qbTdJfpJ3rVRu0rtT3FJ2v4KnQMPJ_rZT_BrvofKxTHLxCA32uNnQVER-AVupZ7y95iZwJn0CTYrq4rDUMgZZNCph1fpy_ZaYBiCt2JdoA_N4CVV_5yC-7VJI0Qei-dJS_qv5jHvm2XD2UE8vMzHTlaORVf0rvdmA-3U85I15bAqPtkWqTOan80RykZdSAWeBLS6-MGB6Pu7NF-5xHkEGgQ2Y3RY3-dSiGgrxUfzpvV2tHrv6-cmMfyKrt9_Tmh8dBepBm7sVmQYtEBYXY02WwET9AVYiTQXo3VstT6OcdgUiJNzJArEXhxv2j3e1uSfZfF3jfEqfN96Dct8XjGsGA4KiyJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e11245244.mp4?token=mdT_ukm7xCK-Sy0uO8VmaeV6rDOdiSZvrHcIygk1ctzRX-Kq7arTPbputpxDAJbEL3i-iEyCIEb3mVaTvz7vLZjYI6r0MyeAKr0D1Z8TLGS4W2P1ID-dytcVcfW3fDZYySxlll6Vbv4ILF0876ssN4-pGZo99CCJ4JQm6YSQnc0TLf-xm47-xqKLJVcgx6VYdLRvvbIjtSwAKW0e3q14TAI7cZUzkOCb9aHlm2tNdegP3yOtcLsTNBmrKWiCMeYE5H2hoH09eib6N-U4ddBZ-xnKemKSov163fgXISr0MbTROIuV9nLk69kCk6lDKXbajczA4gRLQf0dB96qbTdJfpJ3rVRu0rtT3FJ2v4KnQMPJ_rZT_BrvofKxTHLxCA32uNnQVER-AVupZ7y95iZwJn0CTYrq4rDUMgZZNCph1fpy_ZaYBiCt2JdoA_N4CVV_5yC-7VJI0Qei-dJS_qv5jHvm2XD2UE8vMzHTlaORVf0rvdmA-3U85I15bAqPtkWqTOan80RykZdSAWeBLS6-MGB6Pu7NF-5xHkEGgQ2Y3RY3-dSiGgrxUfzpvV2tHrv6-cmMfyKrt9_Tmh8dBepBm7sVmQYtEBYXY02WwET9AVYiTQXo3VstT6OcdgUiJNzJArEXhxv2j3e1uSfZfF3jfEqfN96Dct8XjGsGA4KiyJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز فصل دوم
#پادکست_کافئین
​قسمت اول | ابوالقاسم فردوسی
☕️
🔹
​در ایستگاه اول از فصل جدید، تعارف‌های همیشگی را کنار گذاشتیم و به سراغ نبوغِ فردوسی در «خلق ارزش در سکوت» رفتیم.
​
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
​از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/eke05kb
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/659984" target="_blank">📅 07:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4JZPFb3ZwqKJVv5msvQmpvu_adVkoWOKGII_8RDHoVJYxtFTTz_1kZcRiNoW-dZu3PtVAtljZZGPfXiPsuxkCkszXPOUP1JPJHQl1OuzrdIK-XOa7tlYSF3hneQfubAifBoVQ_sDMVOtsGNcf6imAwGZ9aVDkHr7eq4ohcSoxAZXHsE9wTTxiN5U2Z5rJqNnk7Jed5YsZoi1iaBqtPNYxEhZOP18SLXPGlONhZXgT_lxiVv6aegtHRb5sYfm20p4K8z8-QnUPAH_W4j_EdSkYG2_D9tqEwozZ-YYuzv_HOZrp_NlKB5EaltQds7D5nDjVV58Q8RaQ-e4iYL3IaJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری جالب از هواداران تیم ملی در ورزشگاه سوفای لس‌آنجلس:
میدان با تو، سکو با ما
بزن که خوب میزنی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/659983" target="_blank">📅 07:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpzBk4Z8lUtAWbeTrQVAXZIkrKy7Grg5e65yK1yABLoucKKDD927MXuQW08GuC7QgVPJMXb2yj47sXAdHfiPoWglIIGArBoa16I-1gnfFEn1Ma4r25sVLHhngF_0foC-sqveEkLovb9sesZ9elnNWYV9-DjypbjSFlFiX0wY9YGRJG1LxIdmFM8XtezWktdGOFz9MKzCWSQZ_hFg_bxkKOQCDQOwTlMOwqYoj_H2hBQne3uIdbPeCdwNz72Zgryx3KH46XPsq-2iuHOkX0RW62ZV2P1KrtnPLvE24W992399Ml2KOLmdAuB-laO7L8wa6nCOeNnDG7AfLh6zRW0wJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمرات فنی بازیکنان تیم ملی ایران در برابر نیوزیلند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/659982" target="_blank">📅 07:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWYp9kIF0hUWfdygHqj7_eKcP0EefHFkDZwzZUWm20ttNejIkkI5-u97xjbPq5UEnUcg2RPCaaI5nle5U8Hh65L-NQkfj4QgmldAQ8qRvDYgQEnCRAA1VfiOUHFbMXqzxl5M9cdWN4apskwYd_xN9D8qrYd37zh4qHdRfaDxYTiiIW8hVDUurRIkdaxfQndEt2mRu7VKJDBpw3kLUBLR3-G_-Ybn-w4r5o2Nyyrcl24p2NlQlQzXIlvrRQqBZ0ruPdaON0_lv7wctyTefQluI7D8CM9YmfB5WBlhIbpouUSOjYitNyNVsk7u-ANs3sgac5XMAol8jPtLvyik6X68hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلعه نویی: همان مشکلاتی که فکر می کردیم گریبان ما را گرفت
🔹
این بازی بهترین بازی دور اول بود!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/659981" target="_blank">📅 07:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659980">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378c7d7f9a.mp4?token=UHw9Wt75GKif9rr8HDy7YiK_IOVfdTgxp3w_4qMpK9iExmwtYO-2U9mfobKPu3DIgVhiz4v1K-RPTRXcPecWqbgiXs1Q1tXBP3CA2bDEfc7ouc1D2lZgjP57tEJp1Bg06Ieo8td_pTGMosxWLM2u5ziCMYOGLkieP4BMX1W8Is7TO7DYqSPLpfyYOTDYA38M3aouWl5lwHRiR2fwk5tzOGeFyUYcW18rbP4sSdr3lyjMe8Hs9iIemF4l8wMeI-0YPw7X0Eth85WPiOJ08iSktBCyKACQBS5xFki78diK5_Dto5GA5S90JCcKivnKCaWQneAg7x4GID4_PqSyCON_zzV_syb_F-95ZhBn81dtweCQvogtIILLYwB6ilVdzVMd0wBZDfP1lPvNSY94nFQ3_mt4SxsTz9Aeovr6BBZLM3foYs4Ym0aTPY-4C7KfrQclVXdt3pWxsTuvDUlvR5V7i3TQL3r2gSo7SUPiYdmXwZcjyEtLTaBXgWbuumGjr8B7wxH5fXWYeCLzDtrMHWotOiutV5AYZsf1ghn54NrPX9MeGVcVEg5lvM5b1OtA-648u6JV4ABrFFIlxUlp21sBdvDqzlpR9tpn2zIp48pxQq5_iEtGqTg8XkkntkKimO6SKdZIEUTN67qHTg4NRRznd1t0UpTiLeFR-1R7KGanDrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378c7d7f9a.mp4?token=UHw9Wt75GKif9rr8HDy7YiK_IOVfdTgxp3w_4qMpK9iExmwtYO-2U9mfobKPu3DIgVhiz4v1K-RPTRXcPecWqbgiXs1Q1tXBP3CA2bDEfc7ouc1D2lZgjP57tEJp1Bg06Ieo8td_pTGMosxWLM2u5ziCMYOGLkieP4BMX1W8Is7TO7DYqSPLpfyYOTDYA38M3aouWl5lwHRiR2fwk5tzOGeFyUYcW18rbP4sSdr3lyjMe8Hs9iIemF4l8wMeI-0YPw7X0Eth85WPiOJ08iSktBCyKACQBS5xFki78diK5_Dto5GA5S90JCcKivnKCaWQneAg7x4GID4_PqSyCON_zzV_syb_F-95ZhBn81dtweCQvogtIILLYwB6ilVdzVMd0wBZDfP1lPvNSY94nFQ3_mt4SxsTz9Aeovr6BBZLM3foYs4Ym0aTPY-4C7KfrQclVXdt3pWxsTuvDUlvR5V7i3TQL3r2gSo7SUPiYdmXwZcjyEtLTaBXgWbuumGjr8B7wxH5fXWYeCLzDtrMHWotOiutV5AYZsf1ghn54NrPX9MeGVcVEg5lvM5b1OtA-648u6JV4ABrFFIlxUlp21sBdvDqzlpR9tpn2zIp48pxQq5_iEtGqTg8XkkntkKimO6SKdZIEUTN67qHTg4NRRznd1t0UpTiLeFR-1R7KGanDrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قلعه نویی: همان مشکلاتی که فکر می کردیم گریبان ما را گرفت
🔹
این بازی بهترین بازی دور اول بود!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/659980" target="_blank">📅 06:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659979">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c88f8f99b.mp4?token=gE47BhaflGW140HQs8EcjqopKQg6sJ_9eATq3RQmM-kIS4y5fK_C0QYSBE6w-F4yZpR2h0PFqbxztgipanvNCuz3NIsaXTPf4p5ZdvvZy-YYrbcPvqpZ5QCO3htctTA_DcYaGt706_o-AoXfIDB_4xuN9CipHxLZ66NLdSgFO8InEM8FD6u0WAMdrSCboc73m1E-Mt83sWJgAm4RSGYTdreKruf8YQm1D6jLy0jqNkaS0_vzU-3jFzwjXeNqmi9gXU76pw-m7zP5XStisJqd4OIT0WP1fraq54LX5gYXdY1yJe_2EB78qw_5Dpwijo8hlmXYEESCkcW2WnFftdIXNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c88f8f99b.mp4?token=gE47BhaflGW140HQs8EcjqopKQg6sJ_9eATq3RQmM-kIS4y5fK_C0QYSBE6w-F4yZpR2h0PFqbxztgipanvNCuz3NIsaXTPf4p5ZdvvZy-YYrbcPvqpZ5QCO3htctTA_DcYaGt706_o-AoXfIDB_4xuN9CipHxLZ66NLdSgFO8InEM8FD6u0WAMdrSCboc73m1E-Mt83sWJgAm4RSGYTdreKruf8YQm1D6jLy0jqNkaS0_vzU-3jFzwjXeNqmi9gXU76pw-m7zP5XStisJqd4OIT0WP1fraq54LX5gYXdY1yJe_2EB78qw_5Dpwijo8hlmXYEESCkcW2WnFftdIXNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رامین رضاییان: چیزی از ارزش ما کم نشد
🔹
حق ما با این بازی که کردیم، پیروزی بود
گل‌های بدی خوردیم اما چیزی از ارزش ما کم نشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/659979" target="_blank">📅 06:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZa7RN1OPW6jYtac50zpC_QqrwvJ3_3EJeTvHEqeCmU6vLoN5ah0JECL4uYnmnsOOC_Hp1QkY-VNfXZwvHrUo_7KWihTh3n1jNDkHNKq0IHXAEUD8uoIrwbJEHzj8tz21KmSRjLZemh4HdhMulmAtYgFQuPiZZHAqj5sqaRE34AUUn56Xrco00pWVfabEjHS2qkoAguC-ICaj7njb5sANHDXLbGwFNxLSUsnlerauJd2lO_Yis9QV5qF-vtSilm-l0j3ZYJIYIylwCgrzDPd7zqtg7cpSt7_AIDjT_5O9dqP3oAnoRNQdNQXQyubXFOvU5jkB6lTEt02wS1jwfA4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رامین رضاییان به‌عنوان بهترین بازیکن زمین انتخاب شد
.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/659978" target="_blank">📅 06:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659977">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6tgsWwfzJMiq5iaqvMgF1QDrf-0ic6E1demOm4acfldNspkSSfoKjuWsoIkX9DNM5lQKMZRzkO3zqyErkgXEcDGY_R3gBtOt88ZppESWiJl0A84QrBzWkojP947ByEQpleFF6MUly8GWRmsSOl-APSJm3oFge2kACMXbi2Rr-xOj0tWFfIM0V2qKgPpgSLvOdI6eEzu2ypdv8F5V2lRc2s9wtCjdYVap5n0uCscnkeRFfYaOZIsAkHA9iuhMc0LXHmhdnXfQMf2s3bVh0Si28vfJZQpx2CtWyzh1iRrUcPvqqWIf19yaFQW7kvvqhKNne4e9LXwfjgwtUYqfM5Uew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول گروه ایران در جام‌جهانی ۲۰۲۶؛ همه برابر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/659977" target="_blank">📅 06:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659976">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoBn9o5IABe0-gTzlP8_Bhz89RVp0ooKaay-6t9K4sApYo76Xj7FNYvQj1AgiTfJBUZKxt-qnwtk-ouheqDSxlBa5-36PuCCY8Ah2gK8bLNX4nBmjes61Hb4PeYBZ4GOrgLCoNlrdVnlr1vD11ZsBjQ6eYXyXIbAT1vxNPz0t4P8FOTGhq7Dhe_L0xJ5lY6pUhMW_D7TpYzB2gpzP-vCqs0RDKFNk_Oc2TivfNU7PLyXXZh0ttmkDCvVIp5AyJEt-dzkH-aYtV_l7MBb1n7XswrF4NGtIW2WfBk7iBCc2JNTGG2x6uAlb_l6GUAXXIuuTwR-Md5TIV7tLGGniNd6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تساوی یوزهای ایرانی در برابر نیوزیلند
🔹
ایران ۲ - ۲ نیوزیلند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/659976" target="_blank">📅 06:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659975">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa14efc80e.mp4?token=T7_GZzQuHgSZmJjlzS7PItbSlSzor5r1kSAJxQUXHmMPz4DGsKK5ZCO7fNmQFzYftSLQNYUthGwJF4yhtsD5ZAHNTrQtcMiajSFllOxgYwLfdhBskB3MlX6gsYrqIuGmAy6plya9wJ-opr1JwTvAag9D0K5U6dv1K0fyf7SbVyqKQ3dxadCiVgIUYmXLJacxKQIyN4NGFruW1VHUtS9GDzQdXOCxlVT88lJLwSRiKTj9JDYCSRODRwDfAYAXnYDZ_c8AwWbzPkFJfRLQwwRetm9aM_d-IfMNuEDHGrdAg9806VK-CXwiJBuHCDd2nXHQL0cw79bQ7hq5BoJuNVwOMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa14efc80e.mp4?token=T7_GZzQuHgSZmJjlzS7PItbSlSzor5r1kSAJxQUXHmMPz4DGsKK5ZCO7fNmQFzYftSLQNYUthGwJF4yhtsD5ZAHNTrQtcMiajSFllOxgYwLfdhBskB3MlX6gsYrqIuGmAy6plya9wJ-opr1JwTvAag9D0K5U6dv1K0fyf7SbVyqKQ3dxadCiVgIUYmXLJacxKQIyN4NGFruW1VHUtS9GDzQdXOCxlVT88lJLwSRiKTj9JDYCSRODRwDfAYAXnYDZ_c8AwWbzPkFJfRLQwwRetm9aM_d-IfMNuEDHGrdAg9806VK-CXwiJBuHCDd2nXHQL0cw79bQ7hq5BoJuNVwOMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم ایران به نیوزیلند با ضربه سر دیدنی محبی و سانتر زیبای رضاییان در دقیقه ۶۴
🔹
گراد؛ انتخاب نسلِ شیک پوش
گزارش لحظه به لحظه بازی
👇
khabarfoori.com/fa/tiny/news-3223379</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/659975" target="_blank">📅 06:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659974">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS61YgzMt1A-KtwEFXkZGq3Rl9Fxgw0Kjb2s8bkimbbPOPfM4DRJA72HsAuOk5Z8fgYX18NEMx1z6DWsbWtNOauBPoXg6R-r_PevKPTjxymf35klV7A4zRADr4lnp6FAQOpai7qVtITKSXnDguMxgahq6MplobMX3lI2c9laalZuyTNhQEj6mW6rRj0lMuEqFhJ9-POOpRa5CW9GJ49bXYczMW7eWLrKmWfxm4ibh5Q-vjBLFsgJmZYaQ-pTIORLXpwgOliuJ516ZCDqWLN0Hbkz9XIH5Nl7cbjxnJQAPgsh1k4qQZwxOnTOgy2in7xzWF5AzXPVVXYbv-0HhB5zqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میناب ۱۶۸ روی سکوهای ورزشگاه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/659974" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659973">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37bb3e322d.mp4?token=WRbuEl5qC8oPiPoZd7MpN9lnQzwEKvjWkNGuMSl2_AGmisHvlEIrrT2MHKnWrdYyQQkUjMquPagY-QBXhFrza4PJWWR6UQCdGOAT2yFqC6dvYJZhgZ86iH2Zjbyvkc4dEK9b1HH0CadE5a1ldNUMDr6WUdjZX3vCd73IxwktmYgCyqKHWLvtvx5nKFGyW5UG_5gqUK5Ajr2pczLzwmEqQDQOFctnWnjMmfMTmJ6zCNfIgyCUZ1KEv-VrhHkw9m5qpEKrfrBPyyPIrbTXYqxqHzbgQNco_aCKdWnsS0eBU_FvwupfXpSY4bHLVIb5c42PixBNySAj6vK2KH_GyfvnIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37bb3e322d.mp4?token=WRbuEl5qC8oPiPoZd7MpN9lnQzwEKvjWkNGuMSl2_AGmisHvlEIrrT2MHKnWrdYyQQkUjMquPagY-QBXhFrza4PJWWR6UQCdGOAT2yFqC6dvYJZhgZ86iH2Zjbyvkc4dEK9b1HH0CadE5a1ldNUMDr6WUdjZX3vCd73IxwktmYgCyqKHWLvtvx5nKFGyW5UG_5gqUK5Ajr2pczLzwmEqQDQOFctnWnjMmfMTmJ6zCNfIgyCUZ1KEv-VrhHkw9m5qpEKrfrBPyyPIrbTXYqxqHzbgQNco_aCKdWnsS0eBU_FvwupfXpSY4bHLVIb5c42PixBNySAj6vK2KH_GyfvnIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم نیوزیلند به ایران توسط جاست ۵۵
🤩
🤩
🤩
🤩
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/659973" target="_blank">📅 05:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659972">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b21937148.mp4?token=OJMX2SZiToxDDOqrKPSFR6y4at0DYDURNi3U2KLvmve2GhZDu_iDe7wFe2_9eaP_4IiE3at2Q9FVKhUiN8Zqptgwr4tAz4gAAISzMrwJu2rl3O8q4n2jNA6x6vg2snOHMyuS0LU9pgm6ZhcCPHtPGWJG_1KBmYTbEjIloVMN9IkQr4vxGyDo3F-vo1ys3yBOgkzN1e5e-48VItZqx9ZSmtwOeWs-h0irdKwfYrFxjZTOuzy5oPjwf0pJggL3-VeW1kUxWmag51qMFrImU5NTMPA_N7wBDm2PHN_qe3Fc_mLGN13lTNKBrki1DQ8sDHD8M6TlEXaiz9WfF38MMIYzlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b21937148.mp4?token=OJMX2SZiToxDDOqrKPSFR6y4at0DYDURNi3U2KLvmve2GhZDu_iDe7wFe2_9eaP_4IiE3at2Q9FVKhUiN8Zqptgwr4tAz4gAAISzMrwJu2rl3O8q4n2jNA6x6vg2snOHMyuS0LU9pgm6ZhcCPHtPGWJG_1KBmYTbEjIloVMN9IkQr4vxGyDo3F-vo1ys3yBOgkzN1e5e-48VItZqx9ZSmtwOeWs-h0irdKwfYrFxjZTOuzy5oPjwf0pJggL3-VeW1kUxWmag51qMFrImU5NTMPA_N7wBDm2PHN_qe3Fc_mLGN13lTNKBrki1DQ8sDHD8M6TlEXaiz9WfF38MMIYzlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد «ایران، ایران» در ورزشگاه بازی تیم ملی فوتبال کشورمان با نیوزیلند در لس آنجلس
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/659972" target="_blank">📅 05:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659971">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bf7284b1.mp4?token=G5-HGvl6cIQgMKPoVt9LTWpSqjY_EdMj8qwGw-ciRLUXeamlk4DXOwLJtPTkUnDRRO1WKEz2aotRlfKKwjtnrS4SsBXGcg6cX116O7cY-4GGfEsceb3eGzhPoy4R82qTQ5m0oexsHs3eKx-lyk2DeKPVc-RKtIOzD9xIxEPmgPipBA945w9xFYHQvKHsvU6e6CG8HKlKz_4IrDpYQwOSOu7oOz_41RYxFQ0aXQOvWwvS71vma-Jwzx-dNGLR06SDEBUX4A3EXEp7lUUt4sZ5wLvbmhuxir-vx55a4ZRQC0yCFrYLvbi4MIyG_LTZZti5ST_HFXdL3fy1d4XU95LwZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bf7284b1.mp4?token=G5-HGvl6cIQgMKPoVt9LTWpSqjY_EdMj8qwGw-ciRLUXeamlk4DXOwLJtPTkUnDRRO1WKEz2aotRlfKKwjtnrS4SsBXGcg6cX116O7cY-4GGfEsceb3eGzhPoy4R82qTQ5m0oexsHs3eKx-lyk2DeKPVc-RKtIOzD9xIxEPmgPipBA945w9xFYHQvKHsvU6e6CG8HKlKz_4IrDpYQwOSOu7oOz_41RYxFQ0aXQOvWwvS71vma-Jwzx-dNGLR06SDEBUX4A3EXEp7lUUt4sZ5wLvbmhuxir-vx55a4ZRQC0yCFrYLvbi4MIyG_LTZZti5ST_HFXdL3fy1d4XU95LwZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر شهید مدرسۀ میناب در دستان تماشاگر ایرانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/659971" target="_blank">📅 05:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659970">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBMS4f1GftqUKKMo9CrDIWtJh0Hcr-O8QZiwtJSxv-gtd-QNNankcR-H0J_jZ3WCacWlfOvMzSxLW1FZJ1W4ekwjHsShl_BKVCYBCObPW06AW9Qp4T2y6fpqDux1kjJNIL_74G5-KRZOV_Vftpf7tvbBiyZxnD96-euiQrUolXJ-v2Ej9NQC6L_5XwTLZBR283zmxWAuvtsiUP8NCfWKajvTk_QZkT4_196dvN8gt2WIiERChrMz3e7xS-FCdAw7zC-25zXnil8CsY4If5hlLzM2tupp1-74s3zX6D7RD001FH1VKKeOQDXsFkf4rYt9eAW1mb3hW8_kQa0kDN3huw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساگر انجتی، تحلیلگر و برنامه‌ساز معروف آمریکایی: ۶۵ روز آینده تا زمان امضای توافق نهایی، بزرگ‌ترین نبرد در تاریخ لابی اسرائیل خواهد بود. آن‌ها از هیچ کاری برای به شکست کشاندن آن دریغ نخواهند کرد. هرچه به توافق نزدیک‌تر شویم، رفتارشان آشفته‌تر و غیرقابل‌پیش‌بینی‌تر خواهد شد. شاید این ۶۵ روز، از پرمخاطره‌ترین دوره‌ها در تاریخ معاصر باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/659970" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659969">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSRzE0xs816DLTxBNho5EV_Qn7GNVum3BE-ba5UdELzBMa9ftq182IxhHWrOVycbcUwoKO3WNOZLGS9FuqdGueHrX4mmV0YporJUS7Fv1TvO4UvYlMn1NlSjTPl00MD1CBtU8bvKnwVy6aSYADev8_coExTxbtGotEF2bmQTWZEGQqLvOpbXl45yfNq5CLAdtIfM5E2HshYR3LKrJ5NHN1vqgQ3oAMa3HpLs91RX7bL3vsoqOwTWIxSSFfbB_yTxXyRD3ggFzX1MAqJtL7IdLplms_DH3v2kF6aqH6NwIxBFoj1Q77eCTaKN71NEBCJk1VmQSlffB82lnKkMqEQ_aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">《اقامت۲۴؛ باتجربه در سفر 》
✈️
🏖
🏕
تجربه‌ای از دل سال‌ها همراهی
بیش از 20 سال تجربه
بیش از یک میلیون نظر مسافران
و پشتیبانی ۲۴ ساعته
پشتوانه سفرهای شماست
رزرو آنلاین هتل، تور و پرواز
همین حالا مقصدت رو انتخاب کن:
www.eghamat24.com
www.eghamat24.com</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/659969" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659968">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
گل اول ایران به نیوزیلند توسط رامین رضاییان ۳۲
🤩
🤩
🤩
🤩
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/659968" target="_blank">📅 05:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659961">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjdfJ2ZPoqmEK7gnXNZNrwKBxbxOQaaHY9Jy5twJGVljhs76gs59iZdNsTNUsM9XDDiSTqY-dsZ9LoGWz28TzmddSHsR0afnC0Pd3NXDnGwzbeuw6jD0wYZ9WeC9CAQNVsFXFPZ0lZZbAXr2HVTiARcFhzysTEBSkuiaMv5UI4BwsM31LD5kmHvVou7EJ8PhUvn2M0f5W0xPGfeaTEpHtvgAt__Tv0oT3JiKZZaYn9hcAm96EZCmLesU46rkuKyvhz29uREqvZjFQ6OBUFL_zP8JjaPZqDXzjDirmdZs9ZKSEevbUBskVHBhrMVPH6Mfm5Q4ENqSqLhPrhEnmLD7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwrnuEsXebJiNDHqdGm-3EmtPbxMifpwzzDQ9o4nSi2ngPuz9kXf5tcgGhm-6A0JRjA_qTdTTeZEPev_SUGMiXq4YQZU7rGBM7bqV9jdYzp-95H0Ug1RaUR8H8VlkNok925o0EKy6bh-n0cmS_oI6zFq6PPH18zRxFsHbceL0ub9esA9W5ROBoMFEtxQT8urFJ-Qm379DiWNThk22WLNQVh9CtT63rniyNZtq257MzGPmZPvigaGLslVAza1Al6fH0wp7hL344ZupXQVLvS0GfjmIr7ANf7ZQ--dv2H6woigXXjiP0GrpbXm5PpQVnjlQElOi7WO9B93GLpeUARQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyNOBoKQ2KGFtNKxJuohXWWgiiyXrlnUkO49PrOi3kBXkZHcZH9G5GxhYKn7LlLxB7AA-AqXhTJd-RelnWqPrN3BmQVeDUaOpSRPs-Mc3TBl6g1AEOWmzDb0muJwtSI1pgkjGEg90grUB1MvXO51juig2lX0zTQuMl1Ir8GzZHzI-VwYxX7uywiFX7uwCnIXXkJcKLY9Uxyk9mYpixGSc6bXGLhGQZAy3VXMALTrXKdzTESjm_sblgspzj78mKyzEM83dsMNpRvcDSYyyG4gSUg4iv3lsErDPrRIyqwjUECbH93KK1z91XZa1JWK166zkuoRxLjgQ3Doqr_WTqb3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvx7sL7Ird7olYSbjCnIVnp2l6h2HjhjzXufnm41cn2rBM0-Ib5133fOQh0i3YEjoP0RID7_oCNKTEPhzcnoE_PInH8A4-vzQy5lXaKmKqx2Kvc_ay8L4_cGeIhwGjd6Kh_29urrQzmJZ-heEfSnmbxfKM_wOI9en0JVy_BWVsO1ehhihF5Ih-L0JLWohn0rtJ4L1pzk33BvCHhs7l7epmpoimSlFf5DK5LCssA2tISwWkZQDgicMxv0i9TQ45yO3novC2VteTIYSiuQGJIPLUpa-kxerSHTLrWRPvcfm2Uq_gdztrXvz6sfO_8RFlWwO5JY77dd0QD-lNzn1J4h7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8iLpKFvybrq5sEhj9RtBaWKF8dHulc8SHTiHWoQS0itBsL73g6o1V80U7P_AiuAlDUSk_xUPuoxi5YGj0BzSbM75x-uNaanWhrYdtnyOzftZoMIx6vYWxP5tgRI7O5gl1-WhB4aHNNlaOzb6iY5Ak39Xd_7zNQmd5TQKVoKvdXiP9Tbqf96IIReyxij-YxSSz81gI72r2GL1CsQli7cIjVz35bUEHYhiHIN8WCfv0wIG_AppJ1sNPaip7duKyw6wUVpYtyX7QaMhijJUQhrxZIce3kKbZa-NkzUF81yMFyrUgwbLXDRKVrRLdBuE_PzqgThFyLDPAMS-gbUzAvVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsitS0RDRggqmLvoUjOXgm7mUC8x1BYI4Q33ta9oslaBK3vwhfmYpRfrJIkkP53CMDe1mp2dFuwUNpQkKCkQZVnogghaIUkLPCFnULaC5zSZzqHB0kD6adeZMwVcvM7R4avCQU_2udV5fn8-tNJxxNGwJLZeyBki8bw1DI-jx-pixhy5qwv9rUSLlIQlsvBzoJx-vv6nGnn5EL9ImSUBkLmBcDJ5DmluKIDxVENSsnDtZXW7KBkxPTLEMGaHaAX0zwNkaQOlC_TSxmezgHt5bbxVpr6UrHi42p36MSOjR3_61FpwggbFcn5qGLDd4thyDaXwAvnFpJCsUhbt0W3xZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjfZCnXiksVw3DpfHYX-9oNSayhmE2tIwWMF-gEy9Oh7weDgY37qrPEeyllyHDjtoE86ZSckx7Tg3Rk4tiDWsReFiqLfrURf8gaXpzgS_EC8u5owy92XfOTpsm4vS-_1gVJH2BoYQodyPJxiJ9_hVPpkF6__GVhnH96f4eRlhQ-PlvK29OUUX1sDnCJepDWiZQa6lMufOnGIZBVUVvciB41uIcbT0V3QPKK3yLK1G_ti_exOiq5BmAdLQDj2tTuoqP6SO-qbyvloUSn6MuRZek4YuhOZjUmYQSyqNzEVGl9MPsZZ-WdlOhvPthJmsfydxRoCxskGnpICy_07SjEQBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ژست‌های جالب بازیکنان تیم ملی ایران پس از گل رضاییان به نیوزیلند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/659961" target="_blank">📅 05:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657e4888da.mp4?token=i3dmMWksQOGbLbDE4jWOCVcOqsKo-MF4Hdesu22vUBNHjFSssoUu_WveGG2cFW87Yk9KO69ywxU-8Qn42e5IF-3-b_68CGBi6_k5kyTXGwZOSThUzFUsGjMPNEJxwHr3qoCSY4AAFp1w3vkTXRAodfxOaMcEOpXxLsr-rQ_WUg0ephgBtkXbCiNH-3PoLbIctEBM03b5AJhrPGnwWzJZfmrD1ZmfZ_fXYyfSTlD7kXVvgCtyqV6AUc9_r1-IdXQ5m5zNvwEQdXqG9FHD6pYnX0vebtnbZaw1x8-IoW-9sapBWlurPtExC_qg2s9BS0e8FX2pTiltODhdesd2yBahgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657e4888da.mp4?token=i3dmMWksQOGbLbDE4jWOCVcOqsKo-MF4Hdesu22vUBNHjFSssoUu_WveGG2cFW87Yk9KO69ywxU-8Qn42e5IF-3-b_68CGBi6_k5kyTXGwZOSThUzFUsGjMPNEJxwHr3qoCSY4AAFp1w3vkTXRAodfxOaMcEOpXxLsr-rQ_WUg0ephgBtkXbCiNH-3PoLbIctEBM03b5AJhrPGnwWzJZfmrD1ZmfZ_fXYyfSTlD7kXVvgCtyqV6AUc9_r1-IdXQ5m5zNvwEQdXqG9FHD6pYnX0vebtnbZaw1x8-IoW-9sapBWlurPtExC_qg2s9BS0e8FX2pTiltODhdesd2yBahgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول ایران به نیوزیلند توسط رامین رضاییان
۳۲
🤩
🤩
🤩
🤩
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/659960" target="_blank">📅 05:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659959">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a089ef9ec.mp4?token=d-Zfu89k14lqlEmnrVY0RsgcJeJ-iS_d5svk0HYSzz1OaSwpspywAgU5kI3jR7r9dIXHK3XNd0EZ1jKa1mUnpLaD7G24HgJqJ2kXoMqsSb9ZnS_MEeCmYPh7bVh49BJ_unpomzsHBu3HFQAXxUTWKAL_-5K9j8Aa1fcLMbSUbGawUtQM4ViqYpWBoeXyXoyc4w1m9OmFMgVeKzGz3tM8CqcCwgj2I-soT3ohag9V_kKZ3d7QfsA07Z16QP4BvKAC5VQfOcy0cd6q18pLkXa2iQqcmWWUfnvthXg5Su7eSaSgMJU_Hc8WfWAKDX_92SEpYyDZKHlGIEOz4vQ-V_4LlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a089ef9ec.mp4?token=d-Zfu89k14lqlEmnrVY0RsgcJeJ-iS_d5svk0HYSzz1OaSwpspywAgU5kI3jR7r9dIXHK3XNd0EZ1jKa1mUnpLaD7G24HgJqJ2kXoMqsSb9ZnS_MEeCmYPh7bVh49BJ_unpomzsHBu3HFQAXxUTWKAL_-5K9j8Aa1fcLMbSUbGawUtQM4ViqYpWBoeXyXoyc4w1m9OmFMgVeKzGz3tM8CqcCwgj2I-soT3ohag9V_kKZ3d7QfsA07Z16QP4BvKAC5VQfOcy0cd6q18pLkXa2iQqcmWWUfnvthXg5Su7eSaSgMJU_Hc8WfWAKDX_92SEpYyDZKHlGIEOz4vQ-V_4LlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس: اگر ایران رفتار مناسبی داشته باشد، ما از کشورهای دیگر (نه خودمان) دعوت می‌کنیم که در ایران سرمایه‌گذاری کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/659959" target="_blank">📅 04:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659958">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da7e0ce94.mp4?token=U1M2ITTHgjPkf0o5vlzwpYTIf2KAQcq2lZ_gLPD37mYNpaV7ISNRvaOXvthdS-CrLZXKfb7e4g9IHsic6nUmBL6iFBKeeCBWOyOBBtmsBptb3HVr1ffPPkPJgnsXxYOk2UGETvKIRsA7AfR70r1CarNMeux5PIs3ygKXQR5aIZIDJKD5PTS8QSDIMsWfDmNDW1DuVVNqYyzjX3xG44xSF6scoN_VQOGUny44T_XlgLYqD41AnyLl5i5KBzTM9UqC8Gm95VOY2JuHrpmD-wHPyL4HfP-OAN6Iech5kK4I2gIv0Pn8FPCQfF9rvNw4Eno9tXHhJPA7OwMq13A2HN-VCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da7e0ce94.mp4?token=U1M2ITTHgjPkf0o5vlzwpYTIf2KAQcq2lZ_gLPD37mYNpaV7ISNRvaOXvthdS-CrLZXKfb7e4g9IHsic6nUmBL6iFBKeeCBWOyOBBtmsBptb3HVr1ffPPkPJgnsXxYOk2UGETvKIRsA7AfR70r1CarNMeux5PIs3ygKXQR5aIZIDJKD5PTS8QSDIMsWfDmNDW1DuVVNqYyzjX3xG44xSF6scoN_VQOGUny44T_XlgLYqD41AnyLl5i5KBzTM9UqC8Gm95VOY2JuHrpmD-wHPyL4HfP-OAN6Iech5kK4I2gIv0Pn8FPCQfF9rvNw4Eno9tXHhJPA7OwMq13A2HN-VCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول نیوزیلند به ایران توسط جاست در دقیقه ۶
🤩
🤩
🤩
🤩
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/659958" target="_blank">📅 04:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
یدیعوت آحارانوت به نقل از یک منبع صهیونیست: اگر می‌دانستیم نتیجه نهایی این خواهد بود، شاید هرگز جنگ با ایران را آغاز نمی‌کردیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/659957" target="_blank">📅 04:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7f089ee4.mp4?token=g51v5TYzNjVRKlJMEjD16z5qKk97In74sF2t01zjEgp2yGLyJqwOdQ3_H7uTBIedy6IHn3JpnRVcSM7KXfRKwhssWKRXYVrDf_k-0ynNLUPWpMHaV6F6A1g7C3nA5P7wWGXzauaQJ04WYsQkc639kYp4TD9FaXJ6j7auUwOODNmRuIBcrm5vncKuUgqlVTx8_L9iiinzLKWCo9tWjUElXXV0-0FVC4BUhhkoCuChJG9gUv3QDPIlxzvZIMPragmYtrlj-UZ7QBnGPPA0ql_vL69L9Cnpb1vR7BXWe6ByAMqxajX02AzvrweyaYIisRpn7asxBkRVSgi8yz9XS6UoxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7f089ee4.mp4?token=g51v5TYzNjVRKlJMEjD16z5qKk97In74sF2t01zjEgp2yGLyJqwOdQ3_H7uTBIedy6IHn3JpnRVcSM7KXfRKwhssWKRXYVrDf_k-0ynNLUPWpMHaV6F6A1g7C3nA5P7wWGXzauaQJ04WYsQkc639kYp4TD9FaXJ6j7auUwOODNmRuIBcrm5vncKuUgqlVTx8_L9iiinzLKWCo9tWjUElXXV0-0FVC4BUhhkoCuChJG9gUv3QDPIlxzvZIMPragmYtrlj-UZ7QBnGPPA0ql_vL69L9Cnpb1vR7BXWe6ByAMqxajX02AzvrweyaYIisRpn7asxBkRVSgi8yz9XS6UoxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه باز شدن پرچم ایران در زمین چمن استادیوم سوفای در لس آنجلس
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/659956" target="_blank">📅 04:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77b0df4b0.mp4?token=odSCK6Ucni86a5Ph-TieYeZxWc5-7Nq38F4t4I8bbtpMh-v7iCEWH3zAE9pyjOeM9p4aFHaiglTrHm08CSpc31PAjFp735W0AQKO25zxczEVuFmrzep25cjLsQY2OOzMPgZb2wV-shaFpvIVVOy5kXpZlwKR36m9E5ZwrWRj-fkrNOI77KMTtU_onZY-nxU13GwZRTxd62T6DbVle6ICSQRirZRWO-88KuxPdaq9hhr3PMmJUHn-lHeYt3AKDLWTt7lbctEGeACTIezYWeQG3LNoajYnmFhOOgw-ljl90N_vE8ZNN0wEfITfGlqVldbDiK2P2w-phKJ_N0tb53tcZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77b0df4b0.mp4?token=odSCK6Ucni86a5Ph-TieYeZxWc5-7Nq38F4t4I8bbtpMh-v7iCEWH3zAE9pyjOeM9p4aFHaiglTrHm08CSpc31PAjFp735W0AQKO25zxczEVuFmrzep25cjLsQY2OOzMPgZb2wV-shaFpvIVVOy5kXpZlwKR36m9E5ZwrWRj-fkrNOI77KMTtU_onZY-nxU13GwZRTxd62T6DbVle6ICSQRirZRWO-88KuxPdaq9hhr3PMmJUHn-lHeYt3AKDLWTt7lbctEGeACTIezYWeQG3LNoajYnmFhOOgw-ljl90N_vE8ZNN0wEfITfGlqVldbDiK2P2w-phKJ_N0tb53tcZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همخوانی سرود ملی جمهوری اسلامی ایران توسط بازیکنان تیم ملی فوتبال پیش از بازی با تیم ملی نیوزلند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/659955" target="_blank">📅 04:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659954">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
نتانیاهو: از جزئیات توافق بین واشینگتن و تهران مطمئن نیستم
نخست‌وزیر تروریست رژیم تروریستی صهیونیستی:
🔹
در روابطمان با ترامپ و ایالات متحده، بر منافع امنیتی‌مان پافشاری می‌کنم.
🔹
توافق با ایران را ترامپ منعقد کرد و این تصمیم اوست، اما ما منافع خاص خودمان را داریم.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/659954" target="_blank">📅 04:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659953">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
سخنگوی ارتش: اگر دشمن به تعهداتش عمل نکند، با قدرت وارد می‌شویم
امیر اکرمی‌نیا:
🔹
آمادگی کامل داریم اگر دشمن در اجرای مفاد توافق یا تفاهم‌نامه مرتکب نقض عهد شود، با سرعت و قدرت وضعیت نظامی منطقه را به شرایط پیش از توافق بازگردانیم و بار دیگر دشمن را از اقدام خود پشیمان کنیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/659953" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659951">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SokK8HSLB4sY_-ROveR03IEfTSYD27gofDTiXa9uuXquXl0lIxhJ2sNpyMiW60H3b28ezEV8Is6i8V_bNDyGdi4OPLs3GVskwu2gSW8o7MyAi7i67uvoJawZ6K3sRZRWdmALJICZtgfk7P41ixVOSLq27Smpq2nlR7KV9B07MZS1rwwEazCFZVG3Q2x8-PGKp1howJAq-aNphTVA9cxAh71dKt2H1B_qTpa4s3E0XnClIj5E0FwexIMSdRKmDT_IXGjlIO21SaxXqus2czjyEhOnIoH8FgA8Z2ApWToDDmir8BIiOmRiYcPDWeLSjOxNIzIhohQLZs_m_SMFr9Ft2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVTf2RfgwJ5_EtRE45uLIKlHrxa63009qZ6QRXgIb0xxw8wGQAv_HXSfTnh_eHxhEABJd80yQSAuuUmD1lzOgdgwj6FL7XnygOqfDgWXO959xrwYj8MYlAkZzPon7dATnTrKajx9VdxjxMEiFo4X99GgrcNSS_kx89Vg1kCY5pDLGfILsbGm1zgbop4MdoryWz-GLswbaW5QhJvWvsZLDjVcaZMFbDQOOoCRdO3YtRu3qc7udGiRWy0-u4Lp3c5q_FVBjG0W1Evk_4Rs6dD3EDdkLnzH4e-wk6Z34jDFuqcTj677xRKG8oSNYpL7yC-WiFhJxMCSSoPc8D37SmImHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صدای پرواز همای در سوفای پیچید؛ پخش آهنگ تیم‌ملی در ورزشگاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/659951" target="_blank">📅 04:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659950">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9315b5e25.mp4?token=PKSx0HXw4WhvPLO8YJxsMqwDgmW6FC4e88mdjUywnpYP89CciLtSW4fTe_ee2sZqKDcEUApKWCPcBINLt_m9Lr88l6gqp5i3URG-zCTkCjZfo-N1eSWHFvMtmRfilCyxUIf77U6KaIhHj3J80nsxAAIDUYezOkEwdYrOn8bouysOUmzhWZIPrKIQMax4mjU1aOyrWw2QNM49aTYGtKLb3Nfu5evhK9MRlSrIWAldOecEtkbdNOhMFjrMEQ1zl6dnAPAdRrK_ilVojIF3iUeBoE3F4qNAs8QbXD6QyNN1f-pBe3CUrhZcReglxKTzXiU2jCdOcyAokHHKBEfX6NlX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9315b5e25.mp4?token=PKSx0HXw4WhvPLO8YJxsMqwDgmW6FC4e88mdjUywnpYP89CciLtSW4fTe_ee2sZqKDcEUApKWCPcBINLt_m9Lr88l6gqp5i3URG-zCTkCjZfo-N1eSWHFvMtmRfilCyxUIf77U6KaIhHj3J80nsxAAIDUYezOkEwdYrOn8bouysOUmzhWZIPrKIQMax4mjU1aOyrWw2QNM49aTYGtKLb3Nfu5evhK9MRlSrIWAldOecEtkbdNOhMFjrMEQ1zl6dnAPAdRrK_ilVojIF3iUeBoE3F4qNAs8QbXD6QyNN1f-pBe3CUrhZcReglxKTzXiU2jCdOcyAokHHKBEfX6NlX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوادار ایرانی با تصویری از رهبر شهید انقلاب آماده حضور در ورزشگاه سوفای  #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/659950" target="_blank">📅 04:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659949">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121f6de78e.mp4?token=kRCWDcEzm3VDIiCz0py3x846XmygsZfN9oWDBU0jAy4iyq3teB-ltmncD_lOl3CxI73gyuqoCxryp_vTi3Vxo5DU8yEq6iIUQVaneCE43CPomEC1bjIzbfWrUyiW7DWPY4k4zpXUI5CpKXn0n_s7Ao9IkQptpJAKe_p0JLnJQrhDHUy0yg8r9lkUGfxSKo62tdHQ5rELDE8D8AzHCadbtiEpEAxzXFTD9rjv7PoBNS7SE5Q5VLA2k_r0drELb1tY58coaphP1eWRA3GAlWEt8RyryeWFL7ZkuQmGHJ5GaqWtlCEHx1-r0C4YBYajq-rPzlVqckZNgfWDRPu2BR0MUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121f6de78e.mp4?token=kRCWDcEzm3VDIiCz0py3x846XmygsZfN9oWDBU0jAy4iyq3teB-ltmncD_lOl3CxI73gyuqoCxryp_vTi3Vxo5DU8yEq6iIUQVaneCE43CPomEC1bjIzbfWrUyiW7DWPY4k4zpXUI5CpKXn0n_s7Ao9IkQptpJAKe_p0JLnJQrhDHUy0yg8r9lkUGfxSKo62tdHQ5rELDE8D8AzHCadbtiEpEAxzXFTD9rjv7PoBNS7SE5Q5VLA2k_r0drELb1tY58coaphP1eWRA3GAlWEt8RyryeWFL7ZkuQmGHJ5GaqWtlCEHx1-r0C4YBYajq-rPzlVqckZNgfWDRPu2BR0MUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از محل سقوط بمب‌افکن استراتژیک B-52 آمریکا در کالیفرنیا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/659949" target="_blank">📅 04:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659948">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS99zpHHtvh_W0zcu1Q0klaKl334ZzjrniEKDjKRnF16A1gBurfK21s0YGjnLOy0olJe7-e7wTMImFD8sSApdpLzq6nLW9E3OeRIrwdJpK1UO9_Xehp8i0xcwthGHe1BGEhjQ4vi2M4i0opIDsaS0VkDyFICUnFCb9sDXBqX7k78jO12lYdyn0jZxOtNWZJs3VXQQbPrjOv7tqfaV7gEEP4xp4_7F4zbNMYUrDSV0hP8a_L_z7ckI9NdXAXLOUgIEtq4kdRFN2F20VJTeMk__lFL2sNywq71zwohQiC7Nj9ViP1veTubBxwBa63ayrfXkOS6dECC4v_WvMllvw-UqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لفاظی‌های دوباره ترامپ درباره برنامه هسته‌ای ایران
🔹
ترامپ بار دیگر درباره پرونده هسته‌ای ایران اظهارنظر کرد و مدعی شد ایران پذیرفته هرگز به سلاح هسته‌ای دست پیدا نکند. او همچنین گزارش‌های منتشرشده درباره پرداخت ۳۰۰ میلیون دلار از سوی آمریکا به ایران را «جعلی» خواند و دموکرات‌ها را به ترویج این اخبار متهم کرد.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659948" target="_blank">📅 04:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659947">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRheAlgr3iM7xSkEyAckeANpZe4aCF_LV8uWhqdU4AB2ECIHCis64ZgkFDdR3Xt-FakYv1aX0lQVx8yDY1hL8Vt2O_SwzGd3y-4pLjvdAGD5YJivMNrPjDVsuG7QszvkHkrDJNd_ZS6Zi7-fBmKpdfnyU0x65_mN-BqK9uFwp6uySNT9jljb2Ffwgykn1m1D1pj3nnMjUPzDLG0HCZBFwFhELBnALnXRTSYKF6RG-0VtbLWWLipG5R3WNOeDoLItgYvJSQgkBv9e2OMNu9emksfjN9ZfDwqSw2oLkr0devZKI7WKA6iLRzyue7gMoUDrg8pN6ujY1PZDOcR4BkJ3ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی از استادیوم سوفای در لس‌آنجلس، محل برگزاری بازی ایران-نیوزیلند  #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/659947" target="_blank">📅 04:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659946">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای اسرائیل هیوم: واشنگتن انتقال محرمانه منابع مالی از قطر به ایران را تأیید کرد
🔹
اسرائیل هیوم مدعی شد آمریکا به‌صورت محرمانه با توافقی میان قطر و ایران موافقت کرده که بر اساس آن، تهران در ازای تضمین آزادی کشتیرانی در تنگه هرمز و جلوگیری از حملات به شناورهای قطری، به بخشی از منابع مالی نگهداری‌شده در قطر و یک خط اعتباری تا سقف یک میلیارد دلار دسترسی پیدا می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/659946" target="_blank">📅 04:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659945">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e151197e6b.mp4?token=IWr_6N2Rp4Us1KoCm8Q3VAnkLtC1tYPbnZvzRuMI5jbTvg3SMJK9Ww_Vdmxt1hq1yoxa2FDBJwqgJPE4SggP6888X8KCokyDXhr6IT7hebRh5JneANu3LmByOUtUa0674AYNRNsvQrDAfgxULjBqsDoVIOdVCa47nZ93bdEkbXVKy7BRwAWpgi6JYis9nLM6GZqO-vrfhZPhR4eVS575pAZeCuyDk4XQcMayVDeG53CN8Wf3yvdDaDnVqnRgRRBu6HZ0OYio5FbsNIuaw8YfzoAFXXkwoyvHEOz-3d0CizWl_AhbqqAIQi0cN0C7KRM7aeFGy2Ygb5wcqXea1hBGPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e151197e6b.mp4?token=IWr_6N2Rp4Us1KoCm8Q3VAnkLtC1tYPbnZvzRuMI5jbTvg3SMJK9Ww_Vdmxt1hq1yoxa2FDBJwqgJPE4SggP6888X8KCokyDXhr6IT7hebRh5JneANu3LmByOUtUa0674AYNRNsvQrDAfgxULjBqsDoVIOdVCa47nZ93bdEkbXVKy7BRwAWpgi6JYis9nLM6GZqO-vrfhZPhR4eVS575pAZeCuyDk4XQcMayVDeG53CN8Wf3yvdDaDnVqnRgRRBu6HZ0OYio5FbsNIuaw8YfzoAFXXkwoyvHEOz-3d0CizWl_AhbqqAIQi0cN0C7KRM7aeFGy2Ygb5wcqXea1hBGPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترکیب تیم ملی فوتبال ایران برای دیدار با نیوزیلند اعلام شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/659945" target="_blank">📅 04:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC-RVyyUTNWjwiJONu7uFYFcYu91CjGYzPpNajoQ7gtf-reNdl2NHHK4KMhwrVUBpjJAJ8YsAiu3ZumBN34nw8U1wf8pf6vbNj5xCHOYUWRavmf5EhfxzqYcBWNaU3QZLRGnqMW0xgJIlIChvAzHB6dRgYUI7LusUto0XIjT40uI_PajWPCwWUNBkD1KIiGWQCHTJRLSx_KLFqfd7JTIBJb8QqiafqMcmJbKopU1P8VHuLLPVBGy31eq9akrvChvX1oUaTrE0OA830ban0VlS74PejZICpv24Uxjm2l9yxMWN5_mGTpz18YYQ_5AiFRnv3jkHi5hwpi7wLD6kEvVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
برند شما لنگر است یا یک قایق سرگردان ؟
💭
برای تحلیل برند شما فقط کافیه یک پیام بدین :
👇
https://t.me/+Xot5PGy2C04wMzA0</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/659944" target="_blank">📅 04:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzNnduCQtjjz0HwoZpsp4qQzCtwDWWYHZ3l1WckFB3VOY8VmTv7W-pPEE9XZdDZMD__GQPYe1NF3UIrKA4bAlQpsO1gBEbuIytpO6_r-LLL64sWHtd_xMllIB6mjDQJcRg9iPfeMSq_JWpqL-YIXL3CxL_YawBWORFax55gXtF7ijHAtZ0cDEwSG88Gh_V16x_fdPidn8_Ihogw7fRpVkSIIlZfDPFIJ5eCJ-DBV2yQYeLCEG4LSz90VzOvzciq48BjZ1vwrGFV3xfQNGoyQDLab7CPe4opUF8C-qRp8iJbHHsVAnltn02xpkwF8knb6IoYOD8BAeHAdJPk8elx0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از تخته فنی تیم ملی ساعتی پیش از دیدار برابر نیوزیلند به یاد «ایران» و به یاد شهدای میناب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/659943" target="_blank">📅 04:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659942">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
روایت معاون ترامپ از تفاهم با ایران: یک سند کلی است
«جی‌دی ونس» معاون دونالد ترامپ در گفتگو با شبکه «سی‌ان‌ان»:
🔹
یادداشت تفاهم با ایران در حدود یک صفحه و نیم تنظیم شده است و بنابراین، یک سند عمومی و کلی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659942" target="_blank">📅 04:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT0hhZ0L3vXQWL-gC3rEXv-qsctcmalMiNbLQmVO7T-udv80i1k_I7rfbPJawrD8xXwVazwpWM_X8udDaYuxMEdFiurB-UjSLA7Vm7ytUlI-KBboQBQ_p4b8ltTGWIqgRqnuCAYQji9HOO5IzT_oN97umI-CtZQiZrrAK7YlDumsOJAb7Mnm2fbhXXw5PQ5RfO1lJtmLV3CiCvdgBXHG3YsFW3qKvAzGRl_wjnGiP4Vf0ctbRafcQe3JninndzfZ8FQwQM6my0lk3YLln896N2qfM7kq3ha-TETPsRNf6jbca8RnHRbJrabNDyQIzSFbmNnzMiZRPGj0aGQ1bCEHBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب تیم ملی فوتبال ایران برای دیدار با نیوزیلند اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/659941" target="_blank">📅 04:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEIFWAW_TFg8EolsOBfd7ACjwD9mt1kgCan1oGzbcwrS7prP38YFjJyFrVQzVNYU68CgkRkpX7ePbj-wFiJ6-g85v_q1zCPjpNexBI2qS_m-UAqa1qttAtdAjGH_W8mLI7BQ0oDafUOq0KcgbddU3w5Pm8bNTWYXSe_TUpmsghUnJN2eO22SxQz4k5YeTQjjMcNK9UtUFv4E_Qx3a-O84o-D8rQmjbqM9tHO2ItKTkAgsfF6jOlUyfUsoNE5l707rq-ZyV-gT4pPS6j2l6lnVkjAH7C_09l1OZPpphdmkR_ugN2lnTjT2KcWCwxJMdh6tauKdbz-AzY9Ye9sGX1yEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲۶ خرداد ماه
۱ محرم ‌۱۴۴۷
۱۶ ژوئن ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/659940" target="_blank">📅 04:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659938">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvM2j18oJU5JoIMZ8cuKJOjLZ2McoNpNqJyHXNd3o-GXEE671K6OMFg3OGR2nbQSsm6X3a2vNq0EN1b3j-CRhMihOcJE2pGIuHyx48oat7BWt1u4jcr65yfMHVFlicU0EnF7ISqta5H6mnDPXly1wxX7h6Jd5Qm2R8vMYK8qlJaJ_vNOoo0y6zmR1DVqY_9dKTtCviv5FjHYM0tEFMhyvndqcpkPUoG4T3xO60i3yr39BcNmY6mNDJQdtPYLsx0MYtXZIl3cn4TgReWFcSM_LX_uACFshTjkV3FVz04N0SqzVfOzc53Kitz3JrDOvkRMeFXSPuWrwnb_ErPKDn6ayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بریتانیا: استفاده از شبکه‌های اجتماعی برای افراد زیر ۱۶ سال ممنوع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/659938" target="_blank">📅 00:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659937">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ux_F5ABJVv7SeDxNBG44PWxrCrIxNfNncCZW5lFpVEx5Ey1imI7h4_TJQiXIt6dGf_jrM-twtR376PjUeiU6Q5BPUDi-cNdMUo-pRXcJCoTyfkGBbHMTc5IOoPpQE0cDBbIWJjE3NxYTrYHeuA-q4dzg_cI3vlGUE3mO9OzjCw13fif87byLCeSsfTfQIsRbGu4xgB2t6KsL7ZLzRJkzHZa6TQPJXz-CFxWwqNHQa2ADyB-pSluFKUYRtv85xaB_FYkF57xmgcaCbGfe_jQlIrxxTTkjx051FxxQIL604LHerfsqnPamGS0hCj-XFCNDf0Go_7ROGWUDQmGZCazUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار کانادایی: فقط برای اینکه شفاف باشید ، ترامپ میلیاردها دلار صرف ایران کرد ، هیچ چیزی به دست نیاوردسپس تسلیم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/659937" target="_blank">📅 00:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659936">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای اسرائیل هیوم: آمریکا به طور محرمانه یک توافق مالی بین قطر و ایران را تصویب کرد
🔹
در این توافق به دوحه اجازه می‌داد وجوهی را به تهران منتقل کند در ازای تضمین آزادی دریانوردی در تنگه هرمز و جلوگیری از حملات به شناورهای قطری، به گزارش اسرائیل هیوم.
🔹
این توافق که تقریباً یک ماه پیش مجوز آن صادر شد، با هدف تثبیت بازارهای جهانی انرژی و کاهش قیمت نفت بود، ضمن اینکه زمینه را برای یادداشت تفاهم گسترده‌تر بین آمریکا و ایران نیز فراهم می‌کرد.
🔹
این توافق به ایران دسترسی به وجوهی را می‌داد که در قطر نگهداری می‌شد، از جمله پرداخت‌هایی که به عنوان عوارض عبوری برای تانکرها ارائه می‌شد و یک خط اعتباری تا سقف یک میلیارد دلار برای خرید کالا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/659936" target="_blank">📅 00:12 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
