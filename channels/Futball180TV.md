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
<img src="https://cdn4.telesco.pe/file/Ev0KO_6O2yDoZyHsoFmLu59XraE-TvDTYs-NkWyO9qG6_K78voT1Rxoy8tYAQj_LK9-nIO6P92kQZaXS3A5T0YfAAkVUcXjNOZ9h3ec31ZZpdkh2dVcs5fjr3I1YbNoU0tSuFEOoGlZO1HzsD0YDxKwI4gjAcfpNgwV5z_jMKge1n2sLqKNiuX-gGP0stOVEDwS28B6GOrTcK26jGga7_IVy2exE8Axk6LYYxMKMZFOtE41p6NAkPM7jRIRpTywHZxgzV8XcI2hrDgsa8_NUpzMEaUvS2q1DarMH6K3XCKupqSZ35-BXGzd5G2hKHJbSz-r_yGmhcJlfbLUxsDVOxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 134K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 19:06:10</div>
<hr>

<div class="tg-post" id="msg-90024">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=iQPxfHv7b1Rt9qzeYQLd9CQ4LI2cecB179CBEAGN0aslaCTFpJc-RwzI80dAE7fjEBxuaorsSNNx_j8-zkWimxnhuVvPhjk44LRNmlgLpQzvGvML708NAARgijzVeg-8cMYGlxmMu6Al9T-2wLAfq93Oc4OUyVdFTbq2LsFwMZw-jCeNL-B4UojZyar9SZpX-eehsvGmiFABfM3kVgbDYI6WafAbWaO6dwx-TmPCDGe0m1Me-1W8RanUmQhPGfv__p4PR-G4ScMUnGODlU1Abh6BNViKVnGdXiYtKrUix2RnYdgSYZTR1eJ88JBguc90NUMzUrfqJ22DlnJMK6N3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=iQPxfHv7b1Rt9qzeYQLd9CQ4LI2cecB179CBEAGN0aslaCTFpJc-RwzI80dAE7fjEBxuaorsSNNx_j8-zkWimxnhuVvPhjk44LRNmlgLpQzvGvML708NAARgijzVeg-8cMYGlxmMu6Al9T-2wLAfq93Oc4OUyVdFTbq2LsFwMZw-jCeNL-B4UojZyar9SZpX-eehsvGmiFABfM3kVgbDYI6WafAbWaO6dwx-TmPCDGe0m1Me-1W8RanUmQhPGfv__p4PR-G4ScMUnGODlU1Abh6BNViKVnGdXiYtKrUix2RnYdgSYZTR1eJ88JBguc90NUMzUrfqJ22DlnJMK6N3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👋🏻
پایان عصر کاسمیرو در منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/Futball180TV/90024" target="_blank">📅 17:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90023">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=VEAaeH5YsQ9AlI4Lzgxxx8dnckzky6KQlpNltSBg1C3YNt-1LjAhMSuQMxbMdpg9pigXK2MqHW2PCBIeqCOiR7VYSjV8fDNrO5RTnanJPA8MfczYgXxZq_0vnkZjpagU8s-K8lqzj64g0LbzbB2wS6S0Bc0JpfYpx43P3LdqaZ3fnebvXxcisbdcPidvNDPx100dykSaVmlVlLLc3MQGFBFhxzA_a3uJxaMaJIK3F517kmTQeZBH2ZYm3koT4-xjoWxHQlPl-1XmkplZ0b9TNJkb0uhWAubXCsQgowZvHVQQZrH_awmx2vuDuIlD9Hpq7HyuD85Yy2JztYS8662Zsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=VEAaeH5YsQ9AlI4Lzgxxx8dnckzky6KQlpNltSBg1C3YNt-1LjAhMSuQMxbMdpg9pigXK2MqHW2PCBIeqCOiR7VYSjV8fDNrO5RTnanJPA8MfczYgXxZq_0vnkZjpagU8s-K8lqzj64g0LbzbB2wS6S0Bc0JpfYpx43P3LdqaZ3fnebvXxcisbdcPidvNDPx100dykSaVmlVlLLc3MQGFBFhxzA_a3uJxaMaJIK3F517kmTQeZBH2ZYm3koT4-xjoWxHQlPl-1XmkplZ0b9TNJkb0uhWAubXCsQgowZvHVQQZrH_awmx2vuDuIlD9Hpq7HyuD85Yy2JztYS8662Zsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
لحظه شکسته شدن رکورد دوضرب دسته ۱۱۰+ کیلوگرم دنیا توسط علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/Futball180TV/90023" target="_blank">📅 16:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90022">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
جزئیاتی از درخواست‌های آمریکا از
جمهوری اسلامی
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/90022" target="_blank">📅 12:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90021">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtIbzCnvJ_oHMXHOSMYwqmd0ITDN5DvlkOhFHy3OLmiYUTCjJvw5V2_jfxd03Oyi5xqDDcMJvV4d3k-ouT-Xu3x8IpIr6D-5rDE8LXn3NsICayl9kxcWY26Q4mKZ57FkYSmfoz5ReuzfATkyRcgaw4VNmAcR-ZV2j09HxXlyZZtOtB7jxq5OF7gyST_sgB31muWsGYIB_oRT5Sc4_J9-eaTxZVoVx5Ubx4p1_ctV3Iukl3feXDNTdES4MyLCZZ6GAacaZDOc5KrdVlxG-mfjGGWMv9GEoU5-2SVUfGTxstBmssHP2Y7DsITlIgaeG12R_aaCcPj1fmf7ikQvgWzMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل‌مسی از سال ۲۰۲۱ کسب ۱۱ جام
👤
کریس‌رونالدو از سال ۲۰۲۱ کسب ۲ جام
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/90021" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90020">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/Futball180TV/90020" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90019">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1wuzG28jOXE3QfwHMMG3DFixHBZSDscI8vb7YJ2wN-rDSg6_mg50fa3L6z2oZP-qDfIiabueXOm9hza93mQoD1y89CxhM_L7njDaIrC3kiAppHOjg5ErBXUucu4z05dc0D10q4OZMhrJWXGTbStz0uKAZYrDyclgYu3_lg4ri-Bbc6d5bIzNORTX8CEQIwhUuhRUYmPu-PyrnrzKmPc4J9IfC69GtgSvarqsY1BJnHIqlNlgNg47TUFatjXAjPe2b_jdP0Gy_2cc8t0Y89k9c3olBxbYhcKdOh9GNZ2m6mYVjXZ5l4GNGPnGRvlCvN_JLjnGebHdUNeW-F50oRvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی جذاب
🔵
بارسلونا - رئال بتیس
🔴
🔴
🔵
به Barça 1xFamily ملحق شو و با هر پیش بینی درآمد داشته باش!
🏆
فقط این جوایز رو ببین:
📱
آیفون 17 پرو مکس
🎮
پلی‌استیشن 5 پرو
💵
4,000€ نقد
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/90019" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90018">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/Futball180TV/90018" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90017">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fShTKsQKP9150ROxOazqWG2QIyK0-jmEBSieGAIHSAtR_qSe6nPS42q8nl4ovk4exXw84hbaQ_796cP02FvreF8b58FNwwca6lAFfR8RCSgu66aMGjfknPMruSJeZGT1NEsdDowr35SIl9y87QZKuVmMZMYLayUzde3b8-hiI3H4A-8xRVcM9Ny_k1xofYvvnG6yjraRWLjWYBhpy_8xCN5IU7BUpGyY2V75h-m0AoBicslXJBOA-JZGv_P9XKmFAhFXYlGz7vYfRTVkiY-_lfZnDR_iYeQD2oQ0Z0mo7zJ9P87pMWwInRF5FFt2SHiGZffuS3y5jyWX6uUolYNp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/Futball180TV/90017" target="_blank">📅 11:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90016">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS5nzm6KYYB7eR3uCqT6datJTFCYCV2Lw4yDJ_Ci0Ei53RzL8rE2-scDSd8le83FX0UCXtZ2QhtS3GqoDxP9NH9FGtnEE4YAruw-_Kbl8FGke-1neoZV2VzE0712LJJWkaU_kUlPIi4tN85Tz7Bn1N_Zb9Jk3za9PfAHcG2TNhb9uM2AAdbed3uDeDsqBcMXqXTjyeqiI3M8Y5b6FnGYK6r4azTnirwBQ9nvUW_Feutz5WI_h9xj6ZV-WX3cWvuIr_BxqXW8aeVbCzwXwG_x-3zYWAnVB_IT-FFRpu_5y0jBPj7ZFE_aCF-cNps71JsbZxkLT1BgLaYKVeVJbNcB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
#رسمی
؛ ژابی‌آلونسو با قراردادی چهارساله سرمربی تیم‌فوتبال چلسی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/Futball180TV/90016" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90015">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
⚽️
تیم‌فوتبال البطائح به سرمربیگری فرهاد مجیدی در لیگ‌‌برتر امارات به لیگ‌دسته‌یک سقوط کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/Futball180TV/90015" target="_blank">📅 11:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90014">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=NZf1C4rtCq62iLou50_CsVl4ISxEOCmr7p5mLN8wwt-qUufUxbhf1e4h1_UjUk_RHfljqUUHm_uJz9plkmQOhA-liY7GWl8O60p-wXQbss5sQ00QdKZCjDd-6p6gblsnAzZ0G7-nEyaVekDM_REIFczW9qjGPhLGx2AjX7RATMEChOBP1dmhLv7i9jjt8vlwi06dsKZopeLHoKc5rTMcgZIHOBCiR_5TyeNqF-lCGXtZXCDiI1GrmP7BUZ7_FBxMP7WG8pbQMtsFy8j1fkcjw1OmF0_U3jSOyMVQuGwh2-BWo1DGWN_m-RZ78NoUpyL7viph94sk3hyYclR1bOvK4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=NZf1C4rtCq62iLou50_CsVl4ISxEOCmr7p5mLN8wwt-qUufUxbhf1e4h1_UjUk_RHfljqUUHm_uJz9plkmQOhA-liY7GWl8O60p-wXQbss5sQ00QdKZCjDd-6p6gblsnAzZ0G7-nEyaVekDM_REIFczW9qjGPhLGx2AjX7RATMEChOBP1dmhLv7i9jjt8vlwi06dsKZopeLHoKc5rTMcgZIHOBCiR_5TyeNqF-lCGXtZXCDiI1GrmP7BUZ7_FBxMP7WG8pbQMtsFy8j1fkcjw1OmF0_U3jSOyMVQuGwh2-BWo1DGWN_m-RZ78NoUpyL7viph94sk3hyYclR1bOvK4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/Futball180TV/90014" target="_blank">📅 10:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90013">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TA2Xn7DK7ZdcxlVS_7XGEZDdFD_UAYmLbqQJ6dV8gDHnD-QhjaJznd3OpMItcQjdrYrnabBr363JdaxGpyOmb0egjftCDd4z46fw_ELx6pyp8K6VC66-LgHGbrs_BLBZqWjdYCaDVmXRwB8oDhy6Chw3oILQoUjxyjMhLbmVv1X_FuLycVb595JEcVeD_lVo2rmqPLd99FXeA69uVOSim6oeUBlpiTTOLk8JUnPilYoAOQARTPTpLHUdRQTCkZ1gsE1jjYWWrFHsKjKSHDQpob-f6gsA0Yq_lweKfO5CduxYdFLombGnKpJ_gKSDjmNblSUdA1kDapH3pkT5Q0L16xk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TA2Xn7DK7ZdcxlVS_7XGEZDdFD_UAYmLbqQJ6dV8gDHnD-QhjaJznd3OpMItcQjdrYrnabBr363JdaxGpyOmb0egjftCDd4z46fw_ELx6pyp8K6VC66-LgHGbrs_BLBZqWjdYCaDVmXRwB8oDhy6Chw3oILQoUjxyjMhLbmVv1X_FuLycVb595JEcVeD_lVo2rmqPLd99FXeA69uVOSim6oeUBlpiTTOLk8JUnPilYoAOQARTPTpLHUdRQTCkZ1gsE1jjYWWrFHsKjKSHDQpob-f6gsA0Yq_lweKfO5CduxYdFLombGnKpJ_gKSDjmNblSUdA1kDapH3pkT5Q0L16xk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد رونالدو در بازی دیشب النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/90013" target="_blank">📅 09:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90012">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmqxsKN0OrW89yZPdG0Mf2Zzihz_yOByGFzijzLgJI1PedW9W-t7rGvNInTXPfUlWlUVdG0-pAs59evrY6m1fq8dwNfpTthdNgdh8ex_ORM2-RdbqBq3i3WCYrjOU0gWV4qTN3B1EcggdTTZSEIvSCdBk9dK3e6g5QEW3tpkej8rBu3O35PCQibUen7PSkDIT1tkfyRD4EdYkP7156PqwYZ-c54w34110eIYq1H9ZkLbs00xMuP2jiYuHlhrx66S44wTSPWC5bt4dUfNQcS0oDovuubuQa0S0UQ2t6sKpJUHbWFJ6EvEJ2t9W8_XLcnjqJKKkHmgyF9SxF7e_VkCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش رضا غندی‌پور به عدم دعوتش به اردو تیم ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/90012" target="_blank">📅 09:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90011">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/90011" target="_blank">📅 00:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90010">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ASwGZ6_FbH1B1U59gZDr15IgCv9ZmKkAILs12Bc-gpKfZdSqyWcgTljFnUeyLq_JIIzVr3u23vuH2xmCz_fTIvbHF8FA3YHRx-pPAGPm3AloEml6bqJnYEwg2GVFRVrFTg0xVYIjQS4hWVysB5H1iZvFhtf3wJ472K-n8tD5fk1-RAVEE4voSfBXCrtjGQMb0pwUcJoPlJ04-PRqzFPtT2bfQX2ZxOyGS1Ma1P3R9ENEZWdEFWPdWTiLq1oB9UVJDpqv8L4qC5GI1UQv3qBihG0EhKE97dtWj_QDUExOUfVzforzYLRJc38htsegMajtn1AelZWGSrPsr3fgjbf-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/90010" target="_blank">📅 00:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90009">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=D3UTqYaDVbwtl9mIHvtb7AunstHrhzOqLlTeqDtwHU0gUt_bkP4OttCkenY_ELtOUBBXYo2GnZMHrqaIjmt2KaUdKIcAqIAJmWlh7SbE_ufeJzbu084A6Z1juffNNBTwKyJdo1bewZY1JmOdQKQcZlDukStoXrZLiaNR6d6NAKOkMChaWXTzkh8_tjtn0o-Y9fSAsr88sDRbcWiWPmzHpHTow-MTxMfVS7DyGF5Ym7ziE7dOJuzP8tmDEQa5CGvAqIi_f5Q3g7fbotsiHbO8HqoeluJVB1sQ8ryLYcEddgkRGLzB-9LjqGUXyYkkKUgP9P9274kV_i3cq4BJbUhzig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=D3UTqYaDVbwtl9mIHvtb7AunstHrhzOqLlTeqDtwHU0gUt_bkP4OttCkenY_ELtOUBBXYo2GnZMHrqaIjmt2KaUdKIcAqIAJmWlh7SbE_ufeJzbu084A6Z1juffNNBTwKyJdo1bewZY1JmOdQKQcZlDukStoXrZLiaNR6d6NAKOkMChaWXTzkh8_tjtn0o-Y9fSAsr88sDRbcWiWPmzHpHTow-MTxMfVS7DyGF5Ym7ziE7dOJuzP8tmDEQa5CGvAqIi_f5Q3g7fbotsiHbO8HqoeluJVB1sQ8ryLYcEddgkRGLzB-9LjqGUXyYkkKUgP9P9274kV_i3cq4BJbUhzig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوضاع اصلا به نفع رونالدو پیش نمیره.
🙁
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/Futball180TV/90009" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90008">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLoWP2b4X1skhb4XmXdoZKo9wJDGp4sFdTZr6_F8AwGUjc5_J_08th5BFoPDWbdY72Ojchguz7L9A5VD4zMqAsmy31egs6sSPAn-NCcb92AmZs0UFoM0pB9izjRXREfctlPLd2Kf-MrD2zQmo1pmYUY2beFMw7eyhUkerttuIBFL8x7vyV0uhM3LD7kwOUaB8vKOnJqDsQbIYYqzvUGXDavfGkrnCQXu6mSAB10IcQ5H17DQEtRrcvsePmmKAOeOsyWfKV4M8Jxrspy9HNJiZdngGaaai4k7cWJ9sv1TKP5kKDOkyEy2eR4HgO0MnlTuPSabo5yP6Hxpl1yuN48zFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
توییت‌جدید ترامپ: آرامش قبل از توفان
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/90008" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90007">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnuivG4wr_2BqdocMjKhTCRK6wV6HycTjFYXe8bKrMM5qEKe7JgMHfl2Ak5LzoaijbFqklFCUw86aB6fj6ql713pfSFk5D_OCmtbA3kz04Ed7oOZDRjNRC4bVLs6rClzkesTvtRY3bx1HHBsV1d_Ah3Dc2F1cim9lVbc9-2XkZqIg2rOSqnBr_ngXLXl3vKU7-AWWrgZhKw0MpLsk3wo6AsF4M8zT02fTa2--GiTV98HTXrFDue-FdMfmK5FTspwW95rhs4MFPfPuxKQmUQgtAyygpz81oNDLovZNcNMdc6damJTQqVESyYlHMieQY0BzxVV1K1I_xFwwDLLVmiBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
النصر در فینال لیگ‌قهرمانان سطح دو آسیا مقابل گامبا‌اوزاکا شکست خورد و رونالدو بازهم نتونست با این تیم قهرمان بشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/90007" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90006">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFeGHhRFAQXwdF-qEF-thpNOWyIIBw-cbYZ6MEo9B8xlowpiM3n8jGyZaGh2iJZPnR79eLmAGquHq1QjBKYK7GoHj6CmMVQo_hBqVISgFlgNjpZQGNdKlUjnyqnI2C6tr26eAsG60lMj36Y3L4Eegv14UepOlRhpVWNREfpvQ27H41by-yL99yzdiLwaw0KAm84lUJNix25q3KhqH02kR7UPd_UoOEZuSBm_H7tE50FHHry-kt_BaJx65BjYVx_PYerNXu2nnL_LvpswNAOm7FjacdAnqZeeEl2S6gxrOmf58q3POBosFxs9-0dTt46OC63CfdfLZSbK2rn7q4jZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/90006" target="_blank">📅 21:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90005">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">💥
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
سامان قدوس، روزبه چشمی، امیرمحمد رزاق نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قائدی، مهدی ترابی
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علیپور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/90005" target="_blank">📅 21:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90004">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-hqUbXGPof2S7Q50un5zJzzvs0MrXnRb5oc41kxlzvT50qlfqXZBpuwrUFIrXPEjyuBykXa__eCtgd5kDRH_WbSV0-7jdluZILFz8xz_ELxzIDkMNiOYnZM1QP9pECARo1Ke3T5Yx-Wq1P_AnAy9clxYPh7YsFjt5VYzIrTMY_BAu7ek6dWnPLTBtzA24RMEmRYbl2swwp-xeHahvCCdT04hB8whOi3XenHHYFuRg6TPSYs3sCSyQXgS5jr1hNGFJqVv0wH_8u5u4JkjMbQyoYNEC-Ozx8aadyWegGn7mMkmvthQt8b5HZbVLHBudpjPIkQ-Aygb-gbjs5RUZgaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/90004" target="_blank">📅 20:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90003">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPnkNvY0Rz-85-r3M2dPFkVulUKBeUy8HOayQ-mCjTX_MpcusW3pAEBF8aficUyIudEzuH3bcxdrWI9eEZoTkTPqa7QhCD8h2au_gaFm0iz0rfp49rxZsVubbJgaY_G32n8NUEvmtwGzJkSOVQf4H1_lM7j6_WZFtb11cTURUsNFInjYga5-PNUh8XXE2jtZGYpJSK5aGfJa59OEov0Rho485u0kzZrxim8TEZy6T2JH468g7H3QARR3l65uqxr-XcKcpv4tUHIogbqZfdPT-2K75hN_K4Vr6-JDWVxnpHjob_lyXU-gWSnthEc0Uur8HtokTPD1J4usPjBCPMCxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پپ‌گواردیولا طی ۱۹ سال ۴۱ جام کسب کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/90003" target="_blank">📅 19:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90002">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt4bDx4sQJLVOxqqEjMK-Fq7EqwLtVyXomvLVO4NSmeF1EY3kn0XK0ffZuiltg1_sXVXVScyow3_sD3n7bXSCfR5N_B3jsJy3_UrlfNpFxtPoA7ShtFPlL9ofF8NVDDSEhixXXSmXKZJmqm6bQinMLUSGb0Y85k7R9lag-lXx3WA6fk6dNR8JMXA1lAObU4nxZoLVwezGRV8nPuxpwWhFsuy9Obxp78713eCu7yk0FKhZVIL5HO2wGd2iacQUcQfJgo8VKgHU9WyQk9jJ5noiEO2uR_j1ncJ9H-5W2gUaXoM60Za5vSAw5PXgds7haVo4rJUpsXvPF5XnkYpoKf1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منچسترسیتی با برتری مقابل چلسی قهرمان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/90002" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90001">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90001" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/Futball180TV/90001" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90000">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJeyFon773X9La_rUxvMhn1XmDvRGp1tf0kX-dgNRclvAGVy5h9gv0e7HKcUprYfAbMSm2VAZAUMf1yYKhdC_tWyoOHPJ7nc_1cRQgf8_amTa4WI8TPk0rk7BWKvqq5lzYDuErV7kSJwPh5OM6-GCxEyhJuPlsqURCCydwEUYKR5Jn-hGXYte3bi1V5Mys82ZarXUv5PAxIhUdWu_uZtODTZV9uWkwQkqA-cUfBZhZeBRYVoQ_P1G1oNjB0acLhsOkaEDACec-kYhl9aV2XFiiIUaRHB5Bq1UAAV1Ft3HhC3lth2FrhcyOPINj-Zl1t5b5ooMMpGbjbL-iYFAdjwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازی جذاب
🔵
پاریس سن ژرمن vs پاریس
🔴
را در 1XBET پیش‌بینی کنید
⚽️
فکر می‌کنید کدام تیم برنده می‌شود؟
👀
یا چند گول در بازی زده خواهد شد؟
💥
🔺
ضریب‌های بسیار بالا در میان سایت‌های معتبر بین‌المللی
📱
امکان تماشای زنده مسابقات مهم ورزشی در اپلیکیشن
⚽️
اسپانسر رسمی باشگاه‌های پاریس سن ژرمن و بارسلونا
اگر پیش‌بینی‌تان درست باشد، شانس برد بیشتر دارید
💰
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/90000" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89999">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocJiaKsw9pMKKE_gOI3p_1WMzM_k3ZkYG1tyL-QDuzKF64Db7DebVvP3TLVbCBtEV8ogq4M1kab6TRY5z6ypZ00cHmEK-XTHMK_G1QY9oruP_jJVVYnLfGO9Vl26W6_wkXLufcSf002xewSzaI1fl4RBl2sOoF8ZwXeiC8nVbM71QAUd0-18tVOCEggCcCaAjMbBL_KN7NmR8I3v_niyriPq8xwQDIx0nnPijfK26OwZN2m1p5nLLK5LlfbA5KPeCbEmUoYwJMt9CWAB2p344V2nsEzNs6WYd3hETAE7KsPx1ApIRZk11oDHFWYLJUdtwZxIdYvR5phxPbwLOJjlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام‌حذفی انگلیس؛ ترکیب سیتی و چلسی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/89999" target="_blank">📅 16:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89998">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT_NXZKQkWZyCK6wM-850e_SZsDIAz3Ik_KXbR86sE5ugC5Q_D3zyfr2LJgt_Qh2arEQuAKc0tV08hC79F3x2RrpT264uiHvabHyBYqal5BikRGRtFaLhlEJXC0bBETwS9GfT5FrwqOfXNVFRj6E6QqLLHdGcKyNp4uSYeCupwOPQChsORs8yp6x7PXYM6oNRFBLzALCHQNCjrbrABEjRQncB8xp30E79oUW4IQJoiWOm2Oss5A7bcumRs5L8Csx0TJMK7aHpxB1gQN_Kl9Mp8Q6vD2apwe16SmRhv2aO9a0KKXPeRpUBVxN9uHEA0LCzEiYuQ8Ae_DE0kTqqkXw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
فهرست نهایی تیم‌ملی کنگو برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/89998" target="_blank">📅 16:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89997">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWEjiXf_yvdxDpjcTUFmf0-IsRzYAvKzkinCzvPky6oTJ9fAUHdL7kw2eZwXM-FZWb3smJsGrOzdWHnaaN0qfHIKc3SIFHAK7Fq9SnpLD_xLC94nxTGSkA5EaxtJZ2oAmsiRgBxFL-Jt1JMHQ51EZyXx6bIx-2MofQl649DVfXPK40LdJXVx52blZ-hOmzb4CHoFH5GzPnm438Bj-TihJYYBea4NFNP8ghFCfQ8RaMgU9InzeVyqc8TspH-1vU6u4PrGN5GYWGVHaaDiC13Ikn28qWiY3TZjazM_DLd0i-S1jYqszW7bhXXEd0DSKJg-n9tro_RV8054lRsp_Z7UNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پپ‌گواردیولا: فصل بعد نیز سرمربی سیتی هستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/Futball180TV/89997" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89996">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=IMXgHhnchRZWySteeyaM6rPum2eEze6bTb2yBUvrYBshadfATQSzdCyMFoXhYk2xnVGvszjpYDPhvLpSKxLQgMcSsuTJW_dTd5iliYqB0qnlYke2aqghaHKADt_OTLvsyq9zJWrsnWGYLzL8NYmrB8-DA7xZM8P2VqoKGMSZL0xiYvIMRQHDx9tjdr1f-d0WuWWPDlwDEBZuriVZdJogy1A3wcTqduiZR3ns5SVaxsVK5faK_HvpWZg0-F9ck6aXJ6MZYZx9Oca-5uDkCzQJxj5MWDOfbbNQWLlOOaoIKk_eaUSmidft7Aef72JyHi_5Bi3veq2CoCeMVRdGNwmXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=IMXgHhnchRZWySteeyaM6rPum2eEze6bTb2yBUvrYBshadfATQSzdCyMFoXhYk2xnVGvszjpYDPhvLpSKxLQgMcSsuTJW_dTd5iliYqB0qnlYke2aqghaHKADt_OTLvsyq9zJWrsnWGYLzL8NYmrB8-DA7xZM8P2VqoKGMSZL0xiYvIMRQHDx9tjdr1f-d0WuWWPDlwDEBZuriVZdJogy1A3wcTqduiZR3ns5SVaxsVK5faK_HvpWZg0-F9ck6aXJ6MZYZx9Oca-5uDkCzQJxj5MWDOfbbNQWLlOOaoIKk_eaUSmidft7Aef72JyHi_5Bi3veq2CoCeMVRdGNwmXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📲
پست جدید لواندوفسکی:
بعد از چهار سال چالش‌برانگیز و سخت، وقت رفتنه. من با این احساس اینجا را ترک می‌کنم که ماموریتم کامل شده. چهار فصل و سه عنوان قهرمانی!
هرگز عشقی را که از همان روزهای اول از هواداران دریافت کردم فراموش نخواهم کرد. کاتالونیا خانه من است.
از همه کسانی که در این چهار سال فوق‌العاده ملاقات کردم متشکرم. یک تشکر ویژه از رئیس لاپورتا برای اینکه به من فرصت تجربه باورنکردنی‌ترین فصل دوران حرفه‌ای‌ام را داد.
بارسلونا به جایی که به آن تعلق دارد، برگشته است. ویسکا بارسا. ویسکا کاتالونیا
💙
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/Futball180TV/89996" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89995">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPAZfJz6KLE_UY18GofYjUpchebAurYcIP0GSglOWmuErPJjnnbH6h4quLEO8Mb_myWXHinOeiuQMOIpbBWClXqWC2tno-oTfhiNwkZaZSXuOr2-FAHnSPsVZ1ZepDCJr0ZfddE1icAyQXpbrfG4UXlehlGUkP5hjfboN9d_QOfhpHrVSSkTWEt9rHTsYF8P-MLlK8HhPlMjnqX9ALGBuAMUJZF3JA6QlxXgsp4pcw7lX8N6_u8k7kX7lqrQz3-ywIB0sEbgkoc8td9_eDKu6Z1nxymJTXc64OoGz8wuXXYIAor-EaQadd8roKCHGdWtZhaNjFIymbtuO1BX8PZZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نت‌بلاکس اعلام کرد خاموشی دیجیتال در ایران وارد دوازدهمین هفته خود شده و اکنون به هفتاد و هشتمین روز رسیده است که در سطح جهانی بی‌سابقه به حساب می‌آید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/89995" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89994">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89994" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/Futball180TV/89994" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89993">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfU3JwbHa0N6BzgvcX6kHNKQNCTaRwekjX2aglCZfzemU_CcfdZZJmBclGPJrv3jhvMEIET-BgFMSEWK13I34hxoif-5qQygrQ7NObn-GgZ_3V68R_qIui6RF-cCymOHpCZU6czQEHFwQcSa6g04GkcATD-To2MTGBLgnbaUvfD14bns5AwJwKLDPDwuVQMVBdmlHHA_lXgWPTCa7kUpzWm18juurRcvsvNTNO5YTACGree2Dek8bWlgikCf1L8A9Ak95hhfoSRNivLfGAwVM6ko-UEdo8DKrcX3jMu75FsRCqGtWwQo0ZnREE3gYESI2fzhlsYXllCcEb4mY1wYzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/89993" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89992">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZo7LRneKu7IzYbPJslBOuMN6xUoYHR_VMkQWexqrq12ybZJtM2kB9XsClAH38LrCuQyYtrfORvzVh7jW7hvlb_wANQ1fLo0r0U_4FIS4I_mi-DxXbBlWtG6eUMFaTk4eLiJvEZfIicr8RejlT_liL5TUv1MlD5dVlyqZan7RvU4t62NrhjTIUg1IRJljVjPv_T8HF2WCxFhb5o5m35q11HgfVAnzK8T3ghKfTmwBE7Hse6Ei9SaTF-tfF_k28BZWN1SjbaH3iijoV1-A1y_K6-fad7iNurFHbeSnqhTLa_tBb61edWs1OJgy8KY8J6nwfcT_Az-HJB6AZjWgk2h2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
تا اواسط هفته‌جاری انتقال ژوزه مورینیو به رئال‌مادرید رسمی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/89992" target="_blank">📅 12:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89991">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=gC_ESn49AvOOpi7tXUCUnWtmTFnjvh7EZaqDbw8r2IuU2hsTXCivXoVSOXGKiDIN-kzEwrwvr2T9p9BdFKd8OlUxGUGgbc73iTE1UVBYJ8LhBQtm7tddYcgFXN7ioYSgcQ9JA1embFDt0gxGZaXRhYZ50fpFDINy_yJXB6kt5Ah09aFFpixs6e0uoeegUl8HFUm2P8bRGfbYDT_2YeyUoO9PWEKYSoQ6tGtjFFaO0HbhqpkRnMeiqipJZTzfD8sKQMgURh9BW8-qjwRqwoCI3hH85VKjIBCqUyUyAXnsEtN76Ll_pBoharCnFJ3keoiPiJ2V2uvtN8irQG-AMwnYlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=gC_ESn49AvOOpi7tXUCUnWtmTFnjvh7EZaqDbw8r2IuU2hsTXCivXoVSOXGKiDIN-kzEwrwvr2T9p9BdFKd8OlUxGUGgbc73iTE1UVBYJ8LhBQtm7tddYcgFXN7ioYSgcQ9JA1embFDt0gxGZaXRhYZ50fpFDINy_yJXB6kt5Ah09aFFpixs6e0uoeegUl8HFUm2P8bRGfbYDT_2YeyUoO9PWEKYSoQ6tGtjFFaO0HbhqpkRnMeiqipJZTzfD8sKQMgURh9BW8-qjwRqwoCI3hH85VKjIBCqUyUyAXnsEtN76Ll_pBoharCnFJ3keoiPiJ2V2uvtN8irQG-AMwnYlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آموزش‌مسلح کردن اسلحه و شلیک در آنتن‌زنده!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/89991" target="_blank">📅 12:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89990">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp3Za17zyy6pgiqq66BqwzNwcgRAAIQuRTJ7sIyoxYg6mLey2H1dS8Ohp9EJJr5lphAgZo-TWlL_8fk_KbIvVtYQArtGnxPfhloLqJ40lIvtZ_c3EMH4F173Ud3GkWyzb6eULTWkYME8VN6MLwbnWVYoy4_g4yWizyAUuwRZYiCAYFnhx8PgudbiPiyrGigUGyiXlZieTSTDPyk2hpT5VFE4PTo9b3JafYEuX-8Fu_UvLcg0z6n2jf7yA8-Vt14Nmb01jzFf2vFORlGmHiWdv1XSNAYvY_8G4B-hmO_O92C9LsnAQGctgVleTAcmEbRJD4N3FykqYb0-wvpIIu9TiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هانسی‌فلیک با ماندن رشفورد موافقت کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/89990" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89989">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU4IYQB4CBvUMegqMEBhUNiWkfgK8ACb_gA024Gz8exN5p2qiXsPdkLxfGY4x0jFs80R0RwtFbhSyG-A_NIMLQc4KWx5FXzKZWqu6exff_P-4Z41mFglB_FDu_jp6Ea91DJ-YId52tfRPg9ktAyXrDd94kQQoNTZWvoQWAMhpJHWrLZ8DEWln171-8qEw-7FGI6DBFiS1_qgfHmuezuiOyg_Aai1Hs366kwEKOUt0dMZEPcFouq-qQsLjFwbLA8PuHRwOgq8g59wSkzsxbWpolF5ALj7OnBhS6QH9f3y9cGtf-v9fglSt1UUmNrFI_ZdoJqDawQOqtT-TH-RLhs3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
لیست کره‌جنوبی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/89989" target="_blank">📅 11:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89988">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwF4fwNDEhqGJsVMGN27yOKhG3u4rVSeVb-B3xz3ZTfQ-wUg0AyO1Jj08LGHqifreWKdONVClENNqPjl8i9zZCTtDkkx53P0_K_lM71HQsBNUx7FNOSpdSqtACIC37dh8RoXRASQucoYYOtb3BYLqD5da2nlFRIZzQPMiJYDqWaJROxEvLWz6DqPszvCfpJSbQK6o8CmuxOujkCyXx6AGPMD0vZ0qGq6dIMICgUq5xyp3TmEFE_p0fn9IGl2nKlc8cH_H1Xr3gGnc-sBD9sHfH_xpQAcGcR72sILEakcfzTFsGpSPc70NcgwD3cOa-tUGElrAJK2rzvVkY5Cs_od2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه آمریکا: ونزوئلا 7340 کیلوگرم اورانیوم غنی‌شدهش رو به آمریکا منتقل کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/89988" target="_blank">📅 10:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89987">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فوت پدرم باعث شد از آلمان برگردم/ کخ سخت‌ترین دوره فوتبالم را رقم زد
مهدی پاشازاده، پیشکسوت باشگاه استقلال: در اوج بودم اما به دلیل مصدومیت‌های پیاپی‌ای که داشتم، وقتی خواستم به استقلال برگردم، آقای کُخ گفت که باید تست بدهی و این برایم خیلی سخت بود.
به ترکیب استقلال برگشتم اما دوباره با دو بار پارگی رباط صلیبی لژیونر شدم.
کخ مربی بادانشی بود اما اطرافیانش خوب چیده نشده بودند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/Futball180TV/89987" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89986">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromADS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM2RYU-raakBZbvWA-LB0g_oqWHsoGV3UHrB4da0SCQ26FYXK-XyxTMGz9DtIAjX6UARTibAPIiAbBOh5-FW-Ycc6QDgmpUu0TARENjEBKCWYfk1wafrSe2ND5rlp10Sq8u8ug1VUnsBJQNAvSP4R8b0_6Fpg3SWkAHEBOXTH9E-y67sRnlF0Ik18MLvxU6ZZHeZ9gj8eCxrCR258bhU6X3gAXd3ytgbE4DeZ2vQPhK5SMXJLzSBbxAdUf-diL2j7DvUkhHoZkmyPVkFUXDZccbMMWGhMg0pMNpEF0TL2wcZAi_8D-apKLARkJvV7ry2Y89xCSRybiMNTOkw_r785g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
بونوس ویژه ثبت‌نام – ۵۰۰٬۰۰۰ تومان رایگان
💥
با ثبت‌نام در سایت، ۵۰۰٬۰۰۰ تومان بونوس رایگان دریافت کنید و شانس خود را امتحان کنید.
🔥
چگونه کار می‌کند؟
⬅️
ثبت‌نام کنید
⬅️
بونوس ۵۰۰٬۰۰۰ تومانی دریافت کنید
⬅️
شرط‌بندی کنید و بونوس را به موجودی واقعی تبدیل کنید
🔥
وقتشه بازی رو یه جور دیگه ببینی
⚽️
پوشش کامل مسابقات ورزشی
📊
پیش‌بینی با بهترین ضرایب
⚡️
تجربه سریع و حرفه‌ای
😀
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
A24
😀
کانال تلگرام:
🔴
@winro_io
😀
هدیه خود را با ثبت نام در سایت دریافت کنید:
🔴
Winro.io
سایت اصلی در روزهای آینده بازگشایی خواهد شد
✅</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/89986" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89985">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCxIQ-YZSngno6DT3i4VcC3Fn69iYiwkOmBNwbLFOvyYJytyqI3RvxSa-BdQuEh2WHrg1nVLtA8SKoaWYZ11t9999BqeN2r7JGVNi3r0d6RbFuuzcth2aDtFFD02tTzaIadz7apDHGmjfAzgLgp9DtsqtJ8AFx_Dny-s8tBm61XfP0yx8Y8F6ugWq4pywkIkspF5vC05v1Xo5q45fCqhbCdrAH2o1pUytBjlQ-2pflSKmvVgUs7c_zt-RDPrg1CsRdCl80DE98gAyPYwcnXMuhd7x5Hb87LcULL40WAv-NHTz4skvBkk1NnEpJ4t1wZbDXqXKX5ienH0mx1ILpPbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژوزه‌مورینیو اعلام کرده که پس از پایان دوران حضور در رئال از سرمربیگری خداحافظی می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/Futball180TV/89985" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89984">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">💥
🇹🇷
جشن‌ویژه باشگاه گالاتاسرای برای ایکاردی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/89984" target="_blank">📅 09:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89983">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDa3tLV3kg3hzk9yQ-0yOAx0sXZsld6T0XI2LV-WBX_uwZYR0NdlDRwdonSQLS1V7yWmzdNGw_qu3vcuqvEvQJx1If57PHYVcnKWise6oFJBbKaRhXoAvYDp9c8WWTgTfa2zopzWY-s2kVESx-al_AWwGzhbvv6jitEloMjqTO0x9rBkMH7AoG9PPE9SzPR7cw2-QzmLdbMYkMZ0DGvUDZ2_fmfQE4LnQe5qWryjDYkBOPcwHTfmVF2zRK4PgUAtbcwd3_FeJD8sRnrLT88l-UB6_J5RczDfyrIvl7FUDuQHCoAOx15v8t0FmuWGSGiYT8a_7AvXoxYergr4gvuLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک سرمربی فصل‌آینده تیم فوتبال منچستریونایتد خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/89983" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89982">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/Futball180TV/89982" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89981">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PnC0E3qXuh3fM2kfOKDrq4FqeZ9GrwQTwVhE0AZnw6L2Tprn9ZDZ0yEBBE-bvGtpdjpc5S-BEYIWOVi4m8bB9DliUUzcEhm_Wv6BQweYGQZx9l7J2MHOeC2dZY1c596sl386ubyn8sMwbDgWSfdJWBDZ2Xkq0OakO2bfTTpH42w5-CoWFTLX9Pf5wxXkMiy1cMQZvR7L5apIPIXHBs-cLSTaSc2I8Z6wxCqdkBgaFOF4cULIUArWWWY8jImTEN0WCFw5yZ49EWRFPPLdeVVauHGsb-FsMQ04MEBtN-DtXpOOOetjWwiZU7hXS3EBGiz5He4mEcwQp1wfyu3vO04pAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89981" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89980">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCM4TqjGvg0PM3sFU35Fvi0y3zLVXaweN-cSNAeV_HHaf8jIqH8tvUa7vwZA0k8XELdwAcQW3r0AeXBEXqorPBaUcv2Z3LTXi8A-3kJwdKMkDPE5pyBkcaiLN_0NL0Q714raHxaLN8n4BJRNf4vONbGVq_F6QsTQ1WrCUhKyDO5KfDGmYNjd9Z0Zy0sIuqOorTzGNl8WyEsHuOKOU8XlZ4OR4B--vd-jdHdwN66w33ZgKAFo1S3Jb-8eozBx59KeHsXuH5bAUEziQqodqbvYPigLiWGic4O4SPQhOMhiGj_UMwzwY1_Cv3idnxRD0eYWK1Ls4z3e9EWADYym_S_sMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل لیورپول سهمیه لیگ‌قهرمانان اروپا را کسب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/89980" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89979">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PE16qiO2HA_VpZEO4cpuhhnh1D71OHKH0F_cWAYiL4qh8XSY3NPOYrL1bYlosqYIi2LLua8tgjfi8rp8zoL5CN9M5fOrgNivlk0fOOwHk-QD05ViH_K8iQjH3XBiFnhcsJogCfFqjyArYkc89vPfNzBorDlZzulTwP62QhGGNdsVdYkkEuwJD8Er0Xq6vMOcQ5rvAL-PdYkJjnyM4QVvxkdQ4QUDsZcNkSOJ4utspgm5Gvlhr2yUKyi6-3D-PhD_5iPyzhfkDVwTCocCn3zA3d_Ldp_D0xycRvvjKMucKAtwgwFB_-R7MzAV-n0wG_VE4pmIRcNi5UIcl6ojuiun3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/89979" target="_blank">📅 00:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89978">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
‼️
سازمان برنامه‌بودجه به دولت جمهوری اسلامی اعلام کرده که با وجود تورم شدید اخیر، منابع لازم برای افزایش رقم کالابرگ را ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/89978" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89977">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO3C781XpzjKGwh495hjyBc-rd6sVXhJugVxVWrSUE3H0j4y4tm0W7cfRlHRe5jUmyLITHttfaHHao3385GW9w6-zzw55y3HsZHIFuq58iQUEpB9uTQRz_MzFCCIxrFVrdqy6HnGXniS0C8RPlRF2NX4lr8IvyPBHFp4AV-OFHyvbvcWDZb4t4K65zFlZLS1R_5vLZruQkyQhHptWZE0O5WpScgHz1neBEYrWSoFI-YAzO9FYx8o2gwuYuxd6ysaFdoDDd4At0VVwFHYMfZncQ9S6Pa8uB8gFd0lZxdBWNLF0FKspey_42U7XZYiZNA_-gReHqSg_1ZTXj49UrxXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇱
تیم‌ملی لهستان از برگزاری دیدار تدارکاتی با تیم فوتبال جمهوری اسلامی انصراف داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/89977" target="_blank">📅 00:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89976">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCfZL5RvoOnEmJSjSopohNhbG8Mj-J_QoS0hm5YFjlOXJ3lLSMd1LeRKra7Roi-bD3muVqYTbT20ERBkAN3QRa_CHyQYWyX_cAYjTsoFJbkcZTSq2IDv_7VNpgrldsAOJ5p_oUTeWbBtVKy4QXKQAhzdqqQhJTbchS7t5nQGeQtsme3bVaBtAroJUeFT2cOUO_rlbHYJ1T8UeULJfI51iSmNdD71Mr-AuRIRAV6KesHdm6O-OXavkuoU88bZtG5dRrPOisaOgtl6sy-1tg1LC4i3PWOQ1fKrXl2-0KNS8ZdUnA16H_kdh9bV4OEOCM6Ajt1_pDmeMcLDDF6Y-rjBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
لیست‌تیم‌ملی هائیتی برای جام‌جهانی با حضور داکنز نازون مهاجم تیم‌فوتبال استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/Futball180TV/89976" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89975">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-yWAdpZ6amBgh0_Z-Dp5UBcCGNm77SG-8OKdOBfUUc7nPwo9bFA_1GQTacZBBWXcuog2WzjWP9xLQnxSqhmSfrwTz40YYdkE3tcnEbydRsT7Wop3UrL3dI6gBUMnTeJ4hEKa0mYwPgIdyqLeUEgAoOAt-r8OSNgyqWxdeMRC75BeBWDGgyISW_ovdG4tex48QcSJPuvt3dvlbvjp6iJZ6hGb7Pubg7og0-ruR_hQv56uaD4ZuX4APfrZOVchoIJdp_iyaeu6uTyhtKYb2R8HSTZRxdK7cl5Rkkcdmbx74CzLBHV-qUrOLYHEjnHRam78tkRdSP3tsCh-IRnnLZU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/89975" target="_blank">📅 19:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89974">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/89974" target="_blank">📅 19:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89973">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0v9eZS2NO7UMnSH5s24jYwIeCYoPu0fLL5Qjj10rdjqcgUIt_2CdXhLD3K--UPr_T1BgElu_fq_l1Vi_jUcBe-WxBpUkUyzZUnikcdYwFicuqv5jRRjszdi2Qnl9pErhzP7aeMXVm6KegjfE0fM0z_S5GqAFF7HaP-eVmjHBQl-azS4ok-tCixmVkjtriQ_-ySeLfCAOpxolp_yMyHzZAHH4e_sGlbTPJp8ktPtaLhguTG7yTCHRUT0ChIrQYhRAcNvKn1yuH8j-k7UnWHVR_r9b0PLE-2dV8mOVblQco6z0TnTyhQFVPxJ2uzq6diBHomNe7ZIrezt70MfTSFg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی بدون ریسک بر مبارزه
Verhoeven
🥊
Usyk
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89973" target="_blank">📅 19:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89972">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArBqvK75u9pZYc_HRqgukfau-JH6VDtxnRxHKareDK5NadWuEe54-N-lYvgKgVpAhWhtYBv8Juy3ViWqECI-mut9qMRDEr6Ip6rK3T_5K4ZKZC1o8ck6O23PFGEAssgVJ10p_b6SftxZoQAn6lnrXTpVd0pU9qhs9JOjmRK0RRPORvC-AFgLs8wr5rSzYPXfD3FsV2OzybDka0AovTnLaumvnNtTBlhifzkfRyF-b2h6dlZE3QyR9yZQnkx37w_n1FNntdDj_OLkNa2zb8rEpdlWXx7gfQF6j_qNkat_bNkouPK-8y5N86OuCjmBuUI7Qyun7e4CipW4fNBP2l221Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
لیست‌تیم‌ملی ساحل‌عاج برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/89972" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89971">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPbJ_paD-Sn1PaZRDzkjr1v-ABwdCFnXASNFwOjq1bcKCtQY3NN01x8wYi7FKxA2N6mVGnmdb7DGcFcizdN9mmU1q1Rdz5xx84-wW0PLhrNOFJZ1KYfJg7eH4wnm5ita854dA9RpE9ce4ReiviKKLCisPjDKaskGsBxi_Kz1NYHwcWQjelTWXg7lFcRt9mMhAxYYjD6JNBPe0HY8CF9OzlmhlEoJQ8X-SNmf441MqR-VM08VWV0Y8fL0WvQyhWBNi3noymv-ufhrOd0U_ad3Q6bj6CTL_umj_Oeh82S-IbY-UkSBUBQQQb7-LWVIY52blBG7R7t5sqZKg0o3bpFXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
اعلام‌ لیست نهایی بلژیک در جام‌جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/Futball180TV/89971" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89970">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
فوری/ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/89970" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89969">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxMzJTNzrCMs-jVTa69_zHmOMIi8AtsP4l5a8U_WrCfJgtMWMh6m-XS0BU2JAA6WKK68vpIZD3I6qTIIMF316Hmm08eWWlloLUX9w7OZgYDAGTJLmkNC9aItoQuejXMNwLTzQytBMVp86tHkT6kztsYBeVX6g25T6e2V_3sw3YtTApO1GdSZY0D4h7Xqd01AyQedAtfvVDdH02l6BwKXQQwzae6tb33aXMpm2zIWk0o7sS-NR5f3pVZCKjMqNd3eaJMakzT8IfoiIYzdsxjCrERMyGrVS2mVjaeYmlXJzXz099kEO105AdJVN9Z57UocGhQkAHqJsy-YxykrBaHQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای بهترین سرمربی فصل پرمیر لیگ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/89969" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89968">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/89968" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89967">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZnOzyab8HBuOq1r2YPn_0fq3xtsec4sDUQZ0NI8dDkt4ssV765ZKRLH9dhtJPrszMqZUMrkWEWUFOBS5q2dx8sD4Cq-5YgWunf8ewHcd0coPSZEVosEEHlbfWTLYMEUfR3uT31IAaTFvh5akQTXJzWCSOpJAZgnElGJiWyPLZcJNqjzS28Yk5I1Q8Wr3q2Ukma7Q9q5AArZEHxrFPt8QywxU2lmZb9Qxyk02MxticvCqKu5k9AHyKWwMQPXc8-lB3AxNR775siC1YDXAYBmSSEZ2oeE4Wqfh2ypTHpRetC0zqw3DIJjvyRD3Q6lDBZXeCwbkoJcw5L7X165q9b-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/89967" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89966">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBcVTKen_DMlTb5k48r9UL29UsPKfrP2fE2f5bJXhbHL29q9sMxx7uvU6WmjqNGDqSgSsBS6YOTOrSSSGXoOQWs5y3pCppPT9Nm8uVyy1N7NDE2Sptgx2V-7GshfiYCobVnRJ2gL8RyWLevKpgZTQVS7SEdLQv6GBy-i2IE1zHMr55t9k0hysUY80-DqttslvXtzGr0MCYpzYVxPEnh4fZc5DpWGtaQUCQSvIuYuESkbEXYQhZXJFhIcZcCTbY-yTpnV_C1PLjy2vUcbMc9efvcc3nAIZ8poIIfnOcAIu4Y8i95qCtjSwhafOaD_7uA-tiFHP1jzpOwWvSypWY1ZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇺
کوبا اعلام کرد رئیس سازمان سیا به این کشور سفر کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/89966" target="_blank">📅 12:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89965">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uenqbzjH_1gaGWjriEIywtuPV9aRBXG_ZgotrG1NXBPsFkDVzs_1keoBvR9qUsq6cVS0jflw5dTsl-43chE3HINjAcA4tdTsEozVO8k0UQdha8QgeeDYcjLlQytjc3IzAeXXAYdLrOs05TTfWEQbvBuTcLVrz_MHPoQ8AVyXLMGixFQQImTUtYQ1u69My_urCOQyHqYuFB0jqJb0F4K2z6yn409V--3dL0f64RlNBbHf_fe6uUSR9uRnesmrUt0HuERzy8yPZjSDOKDeUXcuD5mGnh31bAR_4UWZ-8VHgKOZVkrnwgr1QH7vI1CjkA8ZQbJ2LNHMKGAMWgjPFvKe_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
فهرست تیم‌ملی ژاپن برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/89965" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89964">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL_kfh_uakST-gmHQqI3MquwTbP5ewWzHjPiUV86W5ZEoZYoFfvTg47X3m2MxGOFz5KWBTJmXQ37yV4-js5ZTVMdOmi_LVhVo-4jeMRCrpAq4pyv06ZYzozPaBrq592Hcml3cQNj9ChO-pX0bjZ7jVygXj9d2M7DbhCBgk6xyldke2F67vw3UT9M13wIvVrWk0s70h2_7YrHATV9N7Cqm44JbGxqQ6BbtcuUInK7z4F6Me8yloQuBDOnCJp0JXbhePFAOUlFOlXDad1mXrZMJIWtipZdTVM14oGxFOtxXKG0oK75glq_jB5le2-Eahmg5qLck1-pLkP8cs-if55MXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
امباپه: سوت‌های اعتراضی علیه بازیکن مشهوری مثل‌من عادیه. آربلوآ بهم گفته که مهاجم چهارم تیمم هستی درحالی که همیشه آماده بازی کردن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89964" target="_blank">📅 09:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89963">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
وزارت آموزش‌وپرورش: امتحانات پایه‌های هفتم تا دهم با نظر استانداران با توجه به شرایط هر استان به صورت حضوری یا مجازی برگزار خواهد شد
امتحانات پایه‌یازدهم و دوازدهم تا تیرماه برگزار نخواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/89963" target="_blank">📅 09:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5She-PlG5zWW-HzBvhgQLqYcYM8J6W_0SjPs4Bwlt7A1fnf_3T2oQBn-E1x9sRgRVjJdOyXzgrmtqe8DSAMILYoda4yHtqbAm62XN-oE9PIHE1qzSnvPnY5Iq-Be3q6EPphImZdcmT38xh0rWM1jWJfrLF2S320BZYSGTTWLJLuCmRdLOdWGnAceS8fJIzpWcUpweBxLxl7o7JmP2txDNWsVU6i6xxrn3yrui6dSaGDQOX5Jo4-XqhuRHzCxXaUzJBOoEpFCOEiCbc4fTtiMhX0rP_sHsJJlFBV4TfKiDLyaRZzc1QK6sGnAqRAEOVxc8wUnzbr8EJX7Yj-ZKcqpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که بیشترین قهرمانی در رقابت‌های لیگ در ۵ لیگ برتر اروپایی را بدست آورده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/89962" target="_blank">📅 09:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89958">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇨🇺
دولت‌کوبا با هشدار تمام شدن مخازن سوختی خود اعلام کرد که برق در سراسر این کشور تا مدتی نامشخص قطع خواهد بود و مردم این کشور در آستانه شورش قرار دارند
+کوبا کشوری‌ست که اخیرا ترامپ اعلام کرده بود سقوط سیستم حاکمیت‌ش بزودی رخ خواهد داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/89958" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89957">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=oA8MGe6PJJNqdfOFWBUE_bDckuc0EVbWwhaK_0VMKijHqQTNB810daIYoDTnep9W8qcCshoXNrUVGKa-PwBHHHYdLZ4SeXR-5nBByw9pRq0ju6-A6GJwaGttnIMU5JNhK3fV9TVSbSoGKjlVZz3-q7FAH0648ioCnjVAqfJCStS_-VqsxpqePjLlzk9znDUWkHXGWZ2m9Wbghk4l2sny1fhitsHpxIg2BfbseiZx7X7xbGnfvXQr9oIeIPp69g1Ue3Qt9c5dlwdFFOwTxtzagSzi_OwM4kjjytbpESsaBjKfwaGAg5DlXe4kGmxPc04QiToAw54-D8LJCqli6FbvD3HZzt65oFyYC2YOaO6WvQP5Mgqf2-j1LYmzRQ4_bpNlAvSyX-TiQIE1NNP4r-lCTWTK6Oy6J1hAcncfNoTzDzothVlwWkzG-NqLVtSLKH0N7t6wO6UPADwJ6EuRME65kqY0Gcr6MJzyZPMnwRjLcsvYfPUGC-RjypxNWz2Cccdpuaoup0fT0I4Q4hPUrKvp2dp6scfcxQKgjTOXSYzJ6EToGS2Cj40eEOCBKoD7DBlk-eTeWweGZDkgRBRKnaRE5roQOLcAVlB0VJFTGPeV6qKDVAdXe2r8wlxpbdLq31IdRAmA-dS00LvxefV7QM7uIbBT64DGTO4AEcPAW5DqspI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=oA8MGe6PJJNqdfOFWBUE_bDckuc0EVbWwhaK_0VMKijHqQTNB810daIYoDTnep9W8qcCshoXNrUVGKa-PwBHHHYdLZ4SeXR-5nBByw9pRq0ju6-A6GJwaGttnIMU5JNhK3fV9TVSbSoGKjlVZz3-q7FAH0648ioCnjVAqfJCStS_-VqsxpqePjLlzk9znDUWkHXGWZ2m9Wbghk4l2sny1fhitsHpxIg2BfbseiZx7X7xbGnfvXQr9oIeIPp69g1Ue3Qt9c5dlwdFFOwTxtzagSzi_OwM4kjjytbpESsaBjKfwaGAg5DlXe4kGmxPc04QiToAw54-D8LJCqli6FbvD3HZzt65oFyYC2YOaO6WvQP5Mgqf2-j1LYmzRQ4_bpNlAvSyX-TiQIE1NNP4r-lCTWTK6Oy6J1hAcncfNoTzDzothVlwWkzG-NqLVtSLKH0N7t6wO6UPADwJ6EuRME65kqY0Gcr6MJzyZPMnwRjLcsvYfPUGC-RjypxNWz2Cccdpuaoup0fT0I4Q4hPUrKvp2dp6scfcxQKgjTOXSYzJ6EToGS2Cj40eEOCBKoD7DBlk-eTeWweGZDkgRBRKnaRE5roQOLcAVlB0VJFTGPeV6qKDVAdXe2r8wlxpbdLq31IdRAmA-dS00LvxefV7QM7uIbBT64DGTO4AEcPAW5DqspI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت تلخ یک تولیدکننده در نشست ستاد تسهیل منطقه کاشان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/89957" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89956">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5te347iu4y2uac7CEzbrlexPCyFpA76ja-QR7VG5ugtTo1YUwNdcauSNC_g4OsJMbFiHhvgCBSt5fhaE8pWpTrWoAMBt9Q0IjrjWqK48xifBPSzRQ9lZURSOQOMmZkuuhY8X_UQOi6yJdP1r9ob2ZVKB9ks-Mo5yBy-k01vITuK1SCMziXyekOurKRSgzfTse7MNTZ04LB1DSYT3Q_R-Bnm9s8YcgI68shLZ2ZbqfD9him9KapNVoCIphEshmNf3a3nApWUHIbpT43RTDV2hVdZSiYnOAPhtggK52VIOXx5sZW0-GxwcxVN5TJuTqE4RuHlN7otzLjjf1TcFoNw0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇪
فهرست تیم‌ملی سوئد برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/89956" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89955">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5Pl5VQ4r_teem8wDG1RPbaQ3JiVT5jLfOei6s2GYUh4WzWLZqWxxcf6EIItUV5U9ai7ZZuYYVNlLTDuVrHnsF1ZZ_oMLWSnJm12rL_Hl1xPsNWl7LnQD1a328gR5DVLOWGQJz5NwE_ocnUvtkkXBuDI6IkffF1B-15FK4L2q1waJFGYIE0DY8zqroiDCesAEkIEokKpokR8RjZoBKvPLd3vOeHkHbi9P3KBbILeFxBZD2yFh5ZO9GMMOuUn2Qq30Gmzj1JmiXXc2TuECsy4PoDRD0V2Psvz6s5wcW35Z2o3yKgmpm9vr9ktXLaOVH3MX8aMSTlCCePW5LMdJr39Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست فرانسه برای جام جهانی بدون حضور کاماوینگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/89955" target="_blank">📅 23:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=V7i8D1Zoc1Z5vkOvF14WIn-9hDfgVRClNMJO5SKG6vA5j4sxAxBzRNFus6JlFMTnELE2VkaUnSgUGffKIPSigD2TYXJJRyeS9b0YbpChqoax3QUo_e_6gzgRUgYmht_noiYeFwL37J9Qp-ErYsB8p_uK83YcyeO4gKrLRvHMm9tGMZ1yfrSTVL9pAY9_Kvp0bFBWTdO5rpOnq7xtYecImp-Glsxct2xfE4f1QZUvYO2iTlBEyBaG49hFKGCgwTvnSikA7A94fqD6T9327zVgYKk_n475NJDHsVMy7bwm1cBSytJdmZVg-QrgzAtTAPwmW98weThgm4MmFKhQFMpBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=V7i8D1Zoc1Z5vkOvF14WIn-9hDfgVRClNMJO5SKG6vA5j4sxAxBzRNFus6JlFMTnELE2VkaUnSgUGffKIPSigD2TYXJJRyeS9b0YbpChqoax3QUo_e_6gzgRUgYmht_noiYeFwL37J9Qp-ErYsB8p_uK83YcyeO4gKrLRvHMm9tGMZ1yfrSTVL9pAY9_Kvp0bFBWTdO5rpOnq7xtYecImp-Glsxct2xfE4f1QZUvYO2iTlBEyBaG49hFKGCgwTvnSikA7A94fqD6T9327zVgYKk_n475NJDHsVMy7bwm1cBSytJdmZVg-QrgzAtTAPwmW98weThgm4MmFKhQFMpBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاتس وزیر دفاع اسرائیل  :
ماموریت ما کامل نشده است.
ما برای احتمال اینکه ممکن است مجبور به اقدام دوباره شویم - شاید حتی به زودی - آماده‌ایم.
اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/89954" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHVO1bp63eCKqtZ4pRG8MQeQj6X-O4WypZuH1I30XjXTd4bOtWglqvnOXtBN11kJSIkuz00fVRS5RC1wBcvJCiQFbhVqhG0zcaO5cgLw3dRViI704z9VIh7jFdihqxPu7K1dhKDPI2ArTYPHpRIQ1cHtORdZGO5BlZmpfgU1bWPkUxjsMOWXjbtPGlStX4Ly6HxIu-cpJDt7mbhEPpqK0vKVUHYHL0n-lxn6QrtdsBcb7BDZZm9xFS_WflUaQOXs6HivUju_6RHE36JIFLANkxHk-HaRDF1IT75_sE37q0Zh0kycH_VvF2vzJ_JtLKbNn00L3wATptFfoXFVKvSlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
قرارداد آنجلوتی با برزیل تا 2030 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89951" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsWgZofeIfQMxv3ewmXLfpN0Osd-w0Ecs6OaJ1LWYXAyeHr_H4H9ukGq70psPjDUiQJ785wg3RvWS5hTcfacdSEX3Hyi_u8mwtgfqSaBLFKhCHiO_xAz24AQqtAAPmBFrtD61MMaPVoWn8XrM24ibkT5RF0sHZf-O1d8tPoKkRPd-kcGpzUKHxmmlI6mWxVvZ2RtUUvKQNnoatoS_vfxmoHjMARVAIKb3pCPsRiN7YJ6f6F8DVdoDa1DQ4GPLS9F5I5hwVagw0ofWr5nf-s8nxPA1RmlJ-G90jhi0-Y14kXLsC0dcWpz0gqnSXgYkoJucV6hUEaJvt96e5X0I59_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
فهرست‌ابتدایی کلمبیا برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/89950" target="_blank">📅 19:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🔵
یاسر‌آسانی در گفتگو با مدیران استقلال اعلام کرده که بلافاصله پس از پایان جنگ به ایران برمی‌گردد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/89949" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djq64NQ3F59IiSzUzgO-JAzBu_Hd3hkWSnd0WQ42oP5hBP7Jcf6s7P6tKyYPIKfbl3Yx2IkIAWwryCSFx5QXtqvCfyIg5CJ2U6WYOe9v40QF0tUsI0akL-50eIgg7V8_wYiUVeRovDmINjaWDooftXCAGnBb7jfAvSxLjEUkEpRilj-dWbZSG8GvC-0o3Pt_PSKkQSy0VRRbbhXChx1gipbLyqkfXniGPDO9ntKL6FjCo2BaifXG1wrlH3xfd9SbSTloeMRTWaJ8TjjpyCZsDj-LjK27ViZric79Ui-jf6uF2ZA1CGXn-zJ6jl2MWIJbHzgY6Iqgs1MF5L-ZOn47mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژائو پدرو ستاره تیم فوتبال چلسی هدف‌بعدی نقل‌وانتقالات بارسلونا در صورت عدم جذب آلوارز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/89948" target="_blank">📅 19:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrn55OwemNTExPy5-pzLNVVCmY6870b7sLvI6B7czoAcJN4lFp71tvN1gPSgiZBGFjyEOcNbQYqRHrUi99qm1qxlYjrEnlegQ56bAXOR2jyLPxnz5ve3-Xm9-vvw2LRKf1cLZpE8xcpBMA89YzRK1zHrlderPslvzvNHWJf06NgFOibUH2dtivdYH82tIcHUIelrk9Go5wMCrM9cqmcMKfrxgr9RPV_4hOYwPJvFa8PpDNzlJUDyDN5UsS__VVYu_0PU8ak5_REx2BWziHmGlIebD-dCd9jMYCxfa3SCDOmak2TvivPyLsXZ5QlC9wWr652RC6-JF50SXxVyRx5-o-5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrn55OwemNTExPy5-pzLNVVCmY6870b7sLvI6B7czoAcJN4lFp71tvN1gPSgiZBGFjyEOcNbQYqRHrUi99qm1qxlYjrEnlegQ56bAXOR2jyLPxnz5ve3-Xm9-vvw2LRKf1cLZpE8xcpBMA89YzRK1zHrlderPslvzvNHWJf06NgFOibUH2dtivdYH82tIcHUIelrk9Go5wMCrM9cqmcMKfrxgr9RPV_4hOYwPJvFa8PpDNzlJUDyDN5UsS__VVYu_0PU8ak5_REx2BWziHmGlIebD-dCd9jMYCxfa3SCDOmak2TvivPyLsXZ5QlC9wWr652RC6-JF50SXxVyRx5-o-5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ستاره روی لوگو فقط برای قهرمانی آسیاست؛
تاجرنیا: لیگ برگزار نشود، قهرمانی حق استقلال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/89947" target="_blank">📅 17:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebnmv8adMvekzrCDECfBU3F29se7XMZdUr9u4-WoGVnXdMH4mqAtA0mp8VEN_nvAUlTgSyqpC9vHm3hF2UQWzBRxC02LkLVybQcp7uMzCeqDwgGE_b-W1LXnc23DoM__DUSmEDl5ZMtnHb6dI2fuvCGGR9p5sWoNsUoHueQzXvIObIUwY6GjZ6wOuKXOg0ljYDEgzDPQQi-b-A5mTNNaiU2kbV6UaEh7W18UiofFAV5LUOM6qhkVyonelpZlLPZj0xYe7pSMn4n_0hPiNWFqWQouBn801L8xVwk0kQ_sqw8YjncZZTQixz4FVBCziNJXibWCyeFvnjul7vzNpVNJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای کسب‌عنوان بهترین بازیکن فصل لیگ‌برتر انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/Futball180TV/89946" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=SKgxzM08Dzfly_GjC9T0qJxck2vokeVjGkhu6petRjgrY2UPJ3i6HAqtAqGhtuobnhJPh400Wfiqp8pKt2SQWj_mkQZlKhnjWNyHIAnB2kzJzIP9kMaO-EiQ11BcsCI1hBmus1xvh9OlCD0ge2eXf-52YdSLC8tXhDADXAybwOuXYsx5NnfARF6dVT8arVGx-jJc3nJR7cEdBk4G7yfsKMkDU3YMUXAqyzDksTBDZDuW_7FOWvTaJxssfe26I4yzwpoBKtLNRkTQUAVSw0qeE8PeofC3h-iQhLh81sFCL_jkDzcw0DR36THgxy-W1lsdsHPXq79a8c5cxNQanpmlgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=SKgxzM08Dzfly_GjC9T0qJxck2vokeVjGkhu6petRjgrY2UPJ3i6HAqtAqGhtuobnhJPh400Wfiqp8pKt2SQWj_mkQZlKhnjWNyHIAnB2kzJzIP9kMaO-EiQ11BcsCI1hBmus1xvh9OlCD0ge2eXf-52YdSLC8tXhDADXAybwOuXYsx5NnfARF6dVT8arVGx-jJc3nJR7cEdBk4G7yfsKMkDU3YMUXAqyzDksTBDZDuW_7FOWvTaJxssfe26I4yzwpoBKtLNRkTQUAVSw0qeE8PeofC3h-iQhLh81sFCL_jkDzcw0DR36THgxy-W1lsdsHPXq79a8c5cxNQanpmlgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/89943" target="_blank">📅 12:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Squ_uUE6HIHvhsM1hHWT7Q9nPg5p0K0Ek-CfW2kS2k2SGaFOkeNKy5DGD7vDrq_wbs82Z0U4BjDWCNfTJaqiGRnJT0O9NPcs0TR1V_R7vyGJ7EE2gZfYuNqsCAJUg6WTi2JvkweEzeHH0jN_2kXntVb8AvolZdAvup5T5b47YbKoiBGV6m8ZIVF-OklLkBXUVjGxTgWp5pc6_Yodb5U8s5tncItJWW_-SgTpLJAm4_IjO01YNFpD_uxBo5BQ45Pg8Jl4KD4EN5lxYUWc_oow8q2koruA5UPHKngZ3euxIRfW-O1oV1g3nXLIdvpo0smNmVkCqv6kCdw5IhbAG1gm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژابی‌آلونسو به چلسی
🔜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/89942" target="_blank">📅 12:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pupgROc3oaOy4AQwAyXHiXSlns2v8H-6qMI23w6O0-f_FxzMw_lBIqVoguOaYDMhXITGen56aXBSqaXWnOgOTa-J9Yi_DHDxWwgPMcsA0MwHkl53dNdurbbAATXaTfPjwQ24xP6TiIkmvGZciOf5calo_YlIuURQJDvl0yaXEM7fQGornbdKCbe-_F_EAeZgteYT6xqqTzJKd8eNuHSc06KNPEOM3lKFR571wlgOuqLOX3NTs7DUUoOFcQl2YMAO0h-LPH1PLpFkDNxJ28QreVowUo0yx0IlrQR4g8FtGmtxGFXrT3fu8ya_zUPNLzRGQSu1MFadl6HKS31qEu6fNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی از کیت اول فصل‌آینده منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89941" target="_blank">📅 12:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqKCn3UfblgJh8U3wGeoxO9tXburj5E-GfF77F-Nm6bSvTEk3aBZ2zT21jgyDdSF7e9VMhiMoA1w4vPWPe_S9U4CxW9ZQk686A_-0Hx9b1KvfIOy_NyRmJRV400wRAN4ApzaksbFpPXUUoV76r-c1p6Qj0zuEgW_dJfwWvAVKjC5wBuX6V1he8MijBhhR4iHHLkGTc7nzXU8YCwS9qJbZuVrWdbheQybAaHmlXfSeYnjb2NYtw3cQbwjMxg1_x99Wu6UVmEMRO6henNOq1TPO-cCF9sieQ7lhoR5_BooC0YteGwlu4vff-l8xISQVdzmiuQjN529kS05VqR1VNwdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام فیفا، در بین نیمه بازی فینال جام‌جهانی، شکیرا، مادونا و گروه BTS اجرا خواهند کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/89940" target="_blank">📅 11:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFk16wDpyzK33DmZvif-lr5wWIEoF-GDOO429bgz_ymE2bwUamSRmpvD6O_p3nZIQfbP6jcapqOdHzLpjWAA24zBHNVuhVJVfnrKkY_T3TJ2z-py7nSYLELaAeWmROzhLDgDGmj53QtxW0PfHxhCtXemfsBXuSShiSMJzSGTgNg07fbXHTvA19ppixkBl2DfDHd5mCuAUt_Ify4XNfdNKmux5BiEsqnJfmvLN-TLBpdXmnqLShQUehCMyTV8oWLFYJT4N8m1H8mZHClMohW7ML3BM7t4XJI_cHpHPkjLb54iu1Cj_2MarZhaZt25OfTc9t191grNUBsN-jCxvZ6nag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام لیست نهایی بازیکنان تیم ملی نیوزیلند، یکی از رقبای ایران برای جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/89939" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-aGyGQwdFA_djThqCXGRO-6UdtGXygCNvA4oP_pd7BkU3ik9hzsomPka7yTNsY8DdwwFU-ai4gDdNQ8l9ieYNSQyOVaJTAbvOnzQjOE-0hLUsg7-Cl0IDECXBz1jCCY_q-Tno3jjLx1fuzRy2zIeQGSrO8FyAoftufMALkQZ1U7-Y70G8P0Anyb2DIofL0U5VhumlJtq_OBpLr6bzJdRrcT50AigTA6WrgYyiSqUJFhmvlFlE08ZwzZY_W7GbNWCY8t42QeudGtMyksMLIx555ST6TJctWmaHzlzQ912tGg9dxRZGikbpdH7M6hipTLc6EMR83pWbnMAg9nf7iYfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نصرالله معین خبر خواندن سرود برای تیم جمهوری اسلامی را تکذیب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/Futball180TV/89938" target="_blank">📅 08:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4-Ait2Xhh8bjD2k28_DNe4y5jIli9hFTByMWaCa1eWXaWVVUdZvXUyzcPO3nAz3QmKOVw_Jz9ceO2aj6LtL7rdGy8f2CKpQmdq-M6_2PRLDr7ToNgxfq5o5IpkclfwGhv_L2c9S_9fTxpifvjfCH-ni1V6k2a1GzlfOU4IW_fxLXjByWFhgaDAPi5fSGWnkDKpgPEqHdnvL3x6Oi5iVQrUmQ--MHcNuKT5_COwZ4A8qIxOEo1AVKYmTpA7aY43CkNTMtq0sv5Oa8_oI6SPXesZbsXvNEqv130PAelpHDi0YNqetGip8tUgPIYS8YFTI8r54RbcvONFRPXkJ8emLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇫🇷
پاری‌سن‌ژرمن قهرمان لیگ‌فرانسه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89935" target="_blank">📅 00:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0LCS3b-Y4Fv5m_40A4pab-q-7p4dPsdzGZxHuA5kc38g80YEJvnDKcAknJfX_KKAZTskZYmfYyxZUuBRlrsCp4X87NxpM4VJ1EQxWGqP5UF6_loxLzIXXXLGk0sXwP4zr5zmywcsnKNF-m4-uW74TUll8cyulubHGREXhgsSfoiNe_bu9L9g-HQiGegvj3vnVhQURI6SBh7UIyvD9sxo8G5L1fN71MnSF6nYex21_SF_gbJx3wsGEqIerW7qzqgZo-HdmS-js16-ay6tkLmxobdQ4G5F07JCUHdZQ2WuSyQLdWQ893N7m05zssEY6VMdCncpkuaf25U1TtYtjXA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
اینتر با برتری دو بر صفر مقابل لاتزیو قهرمان کوپا ایتالیا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/89934" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4MhrxKby9H0yUhhrcRMC62M0ToPCgFnja9COjtB37SINCnKgWsWZGidEmoje0gjD2JNtmm2nEK0iPug5b3mYMRBPTg8Ai5XkHcss6Ln9GZXUS4hPcDfNTx4Mpyd_Tw2bimHRM3UD_6IM0khqO3vhZ-DHilt7Gp3tgMrJZoeL2KjQ38df57vlfbgagJfpQsOyVcQdtorVlK2FxK8I-m1I27pBDfBn7p7Q96sGnYkQWWtLrhO7HmNTh8CnEWVkRQ4BmEpwVQYwNsy0VxlmrVUcfJQUekC4o44mSiXG2XY6ddKmZzhWirwN850QJy-JOPC8-ckBESumTs6g0oxcwsbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مایکل اولیسه به نخستین بازیکن بوندسلیگا از زمان جیدون سانچو تبدیل شد که در یک فصل بیش از ۱۵ گل و پاس گل به ثبت رسانده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/89933" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XclGpmOg1nxlUwmTDOxxPwPrNvUqMjNPcxNWxrOtUk8bidPcg969-yH_4x3oqVcL-CpWnK6EfTLNX3ZPSEENvG0d6LZz3JKKu2kXQ4MLuBq7JnSzW9S84Ltl26H93rMRUr7WhRbCvfE9taZGlZyX1A-IlWUaKoxUjNn9VEc0pQGpl9JC5qGK91zJLdDNiNCm_Xxesx7fUmS-MIV970URewLuAMfDAmxXy2pVq2LyJkdsk48TXbv_G3mvVA1KKZ1KeRJmMZAGC-QjVulxnJf4XqsZY7cqLNzz-T6NNdhB5jn2osEIpgeT59hQhZgF_S61AfpL85RsZcF-BZzGzx-Heg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار و عملکرد مارکوس رشفورد در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/89932" target="_blank">📅 20:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
باشگاه سلانگور قهرمان فوتبال مالزی با ارائه پیشنهادی خواستار جذب یاسر‌آسانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/89929" target="_blank">📅 17:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ebzq8JZAJMStD8Mg_oX1gcm1OIzLBFz4W1TMtK2x84AVihZUfwa6GhM4V_1pq7iIoV8zJSXTN9fDW81UHNZs-J369647XvutKO9wQpDr93E0hjpCmWH7wPFxDB7ffnOmLVkk4BfqPsfb6_qXLlbbkcV94ZEnpciuocVoZCVKD1IHXc0n_lJlvdS2vkVZKRzau--9EHYF5m6mOUSg6BJwOlK7GrOwrg99gubaSpBOQoCb-RuJqYays5F0Z-9TAlAajsQzEEXC_bI9TPFnynx5kMFQpwwoDEpLH0Y7h-Y56jO-vctKLYvRZuuc-8SdkdkqZJjd3GkeN2lwmSuqFs38Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
اتلتیکومادرید پیشنهاد تمدید قرارداد با افزایش دستمزد به آلوارز ارائه داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/89928" target="_blank">📅 15:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP77CoaOP0dVhDYzxiNUHutuNdPaoWVFQz8c8rPPJBN10wazhVMzs6_1cEIPToxnMW3cG_2POpGKE3GFckuI5O-pRIVnbntBw-UdmvF72qTyBNWxyLF0aTmhDJZS_xFaibsrUQ1_dXamRvQVTK7uHHZecgb20aDWFVst-FLgf3Z0NOToilTAweg4o4EHCK5ySVkJSwyYwXi2bKJROjj6L_70TgMcMHte4M0hCv4LqXemNClSZbMBko9bSmrkHFa7_HXWqQNV0P3sbZIlxlI1nae9EJXy1F-YqyxXwADGVFQVCamyVDei8wwpcZn-VlUIC5RbYajhVyzWsp9L_GYulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
باشگاه بایرن‌مونیخ درحال تکمیل قرارداد با آنتونی گوردون ستاره نیوکاسل برای فصل بعد است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/89927" target="_blank">📅 13:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=GeNziz64G180-vX_K9uKoe2Vlzsq1t00c3y98KZhnVht_EPOxOtlnPi9TedGfHY7XQ_Zkz9ql2TfwedzxRBgmT5dqTD31RYewEgiXRpARCKc6ocoi6BDIzM_dvnA3A685WiCiDAk14rF4TT1K8P9qiacCGHeQCebs5ctdlKGgcXgzoNUBulnDwoK_uba0NifT02HNQRKX7PUZK6B-EaSM45gMvmDcXKKskyJkzcVEp3-D5-bdbyyzPK7KG2GgYLeaOMhOjb7swbSBn5eFGZ79O8rQ1qm2zQg-sVzpGVXvrqqu5acdRk9oncgSMWbeaQIyUa6X_GINLM-qNEviv7blQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=GeNziz64G180-vX_K9uKoe2Vlzsq1t00c3y98KZhnVht_EPOxOtlnPi9TedGfHY7XQ_Zkz9ql2TfwedzxRBgmT5dqTD31RYewEgiXRpARCKc6ocoi6BDIzM_dvnA3A685WiCiDAk14rF4TT1K8P9qiacCGHeQCebs5ctdlKGgcXgzoNUBulnDwoK_uba0NifT02HNQRKX7PUZK6B-EaSM45gMvmDcXKKskyJkzcVEp3-D5-bdbyyzPK7KG2GgYLeaOMhOjb7swbSBn5eFGZ79O8rQ1qm2zQg-sVzpGVXvrqqu5acdRk9oncgSMWbeaQIyUa6X_GINLM-qNEviv7blQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در ایام‌آتش‌بس درحال بازی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/89926" target="_blank">📅 13:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyta87u1lWMc78TlfRFTHRpT3HD4WobUssYePdEsX4m-65uygGDxUxwejRzfNADL0DxCoNXYZzQzgygIBqy8H-3HGTBvLpLU1t2GX0ehzgumIZwTIqZreAanNUF-z4oh5lzaqfoA-_GxuS53iTigFyhDfaMB97GbOCIV1c8CUIT163C-Yo-N8lbBnkmpHEgSBZK2xrAV91_Foh8azUECtEDJOKDPVUYkbHLh7j1LHsIw0rPq_g7WjrAs7hrlYC0XcxklWbLX9zJu9ef0K7nFCPajYkxoc1qUNtUTlTcmFmtHDIt1YMtSw7JvwLIxl2XxMsXtNTZDqRCvvY0ctK1PxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
برخلاف اخبار منتشر شده، رئال تا این لحظه اقدامی برای جذب رودری نداشته و این بازیکن بزودی قراردادش با منچسترسیتی تمدید می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/89925" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhtic0zd5s7kd-SuQGnMQNuJVJIggnFHoHO3MKXHLrdZRW5w0-a0wKIqEo9UFis9s6EQLtDb7DkXSS3Vzq7JfELDMEsTL9Uw2jlSMMbjaMvgn-RX-6USiY54E_S3F-OrMyGLvwKPz9CAvwtizD73zuhdiUsLo1dk-6qwFf30GkxRejG_NWi7mjU0vnxCMej0Azb9k1ocLrobzFW_HBKKY0JKX06pAF0MByDJ8pDr_jnckibqz5xB4zBDsOVLHc6UVZHb_TBpeit5dGkeij2GYL1ZyczIvfm-MY_bHWxQ84t1tXlWQsswyhZhQmrGghJi5YtcvQl6atMD_UGVAlPQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
یک خبرنگار مطرح لهستانی در خبری فوری اعلام کرد رابرت لواندوفسکی پایان فصل از بارسا رفتنی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/89924" target="_blank">📅 12:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNdCU7s9tR4E4jVWUUPFgfVbAtQB4R58PHGRxdJDz7Qx7E7IhoPF_tOYupgYa5vU60_dCEt6Ipqppg6e0yBXqZVA4HusLKEqHbxEy-Vw0RRW3wtOjC3gOEKjb92Dy6dw57Bts_q3_u5VSQTqELyGcmPkE90AwX69F3bg7EKlLfnzHYrpIeKX-cheWadmr3Byx9x2b8BMhnZLNmyG-sod-cLGczaiNuLIKrwaMcfEGkWPbojAUFXqR_RPEjbqbzw3dfLxT3kKV4S5ypHJW8DYDG9B1poEtrqOcY8FTJ-Wgnpzao472XEnxU1pYqC0_bfZktFaggaL_aWt4Ec5HaH1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: قرارداد مانوئل نویر با بایرن‌مونیخ تا ژوئن سال 2027 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89923" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdRAxcHMMfV18YJ6UK9bhKpfX6rONPIElLG_qPcjux5O3N4Fcp0PkWNwPFIMIHZlZiUTRgltby0wnMc7dVcJo0gvtOUU8mKMlMc_xgVdmYYX4uyzMEdonSIMJCt34KIj_SRpUvJr_UWdu049_QOk4okhJe6n9X-SHBgadM4WtsahZbHyhLKPCC_-i5WvbTDMcKpOfzTCPvsAHhUQORVMjxsJvwhXwWLP-yUeCkGVXW4umLZJcEG7k2YnQOVBbrWnkoTW732Mz9QsTvFZAKlGfjtuE8SRrvYsS4IlF6oJsGiLi2d-KECZquWdc4ADzxQ5-X2BuSBeLBr4B3HxRUhALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قصد دارد برای جذب فده والورده از رئال‌مادرید اقدام کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/89922" target="_blank">📅 12:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsY-C2YTbu5-uBlKgJRQ5kzE51XWDpq97AqA8lgndxSxtMjb1qZSNm-XJ0Tng7-IiwwazGfgLZySUhUqAKMSuF-BhgzpHqixA8ssID8_RqhwFndgmG_HUdkIqNi3Lm3E8o-Bx3U51x-DN8A9qN6S3ohmjh0kvkmmCkP-S8ZF5wlLi18JjoltsdYRSx4T0yFT6ao02tRgG8lYLBTxKJNt86VuyCfmQ6Vi9Dp3o5yqLRxE9b1cD3IinWmol7m5H2MXAGhlgV7LxMdzz0Vz86iIkUSnVClrpp0lBXwFEiWVO18mI3aGyc-AzLw8YVSpNVFZdZprF6qF8CTXtf2MP_S01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
فهرست اولیه تیم ملی بلژیک برای جام جهانی ٢٠٢۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/89921" target="_blank">📅 12:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J44rjApSJDCwyLKATIRHrjOZehn9X5-jgXTDFtM_rkQZDmx1aHjtk_zlsgbjYMfGjRkbnrFRurQ7eNW7_mVDsOPR4P7wKSIjzjDVHkS0fH11P20wswX16wW-CoOTn2xh7FzI8cnsc33zoSBEy39QEfy3riP2eySnk5iKapoxBrzObijEDYLKCIzpMrkSGnFi7FXVadjTAvQxoKRY7Ox8s4CrOSIiPvYth9wYLs3V56TSn5RlaFtqAap28gjvOP7u16z9pjact5V63zjyKR7JcnZCP6cxBo0uhEWbIrE0K8WRotdj9g4Zbo2TNErAY59kp3TA2dn-5rSY3e3uZOwGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پی اس جی مذاکره با اتلتیکو برای جذب آلوارز رو شروع کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/89920" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89919" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/Futball180TV/89919" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAV1u_bCLEiz8L2JEzP4N0sBJqm8PufUX-6TyIaCO5ZKFjxE_mEa7DApla2qfonAXUmMQBoBJsDpRoYrtBsedQWUelm95_i22bLZPNmoR2yRP2xgY_9KRzuzeQezbHXe_-aJb4o1eBqw9-LyJ5RMh3T2wqPayJMsMz4J12KEeQrzn0nUmB6P3dVnAC2qBANLpVAnYE0mcEMwdi_gq0baTX6pKxLKW-1v_sH9Al8Gtw06TftrqDDjUnr3wzGmv-6-KpaLWaPSjd_b6u3iqedPDyVla_5j2WmkTLQOmlk0M1_sqcdzRI9lVhODBXKsi7uVnNpiCtYZ_7kzLJsYhUYYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/89918" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
آمریکا برای جام جهانی به پنج بازیکن تیم ملی عراق ویزا نداده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/89917" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89916">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=UUWEGGQMgSkRDXBDvi_EX8uynZ5kvwtj7iMhmfYR2HXT4TpA5wlvnOKp5M-X-x9WjTX1J9K_psqUnHWKx0IsxxsqcylBp8EwmnuG7iyn6OxeQo-mfCUcOyl5IASskSQ4Z8aJc1stjppsSuTJAjTvgkiskLCCsSIW2zOYdsyWpmEisHDipui15lt_YFs6TDlNVPBw-wVnbyDysFN6BxCFWx4IblKAgIoaNiwrN9kZpi6EAClubA8eeSONxYjonEiBD1l2WQRwxDIMEE37k-UAAELNuyJpqX_5fev2u0UEWzvRUh6VoJKqYZdaQR0dI2PQld6SLLWCxLaAy60p7MgEjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=UUWEGGQMgSkRDXBDvi_EX8uynZ5kvwtj7iMhmfYR2HXT4TpA5wlvnOKp5M-X-x9WjTX1J9K_psqUnHWKx0IsxxsqcylBp8EwmnuG7iyn6OxeQo-mfCUcOyl5IASskSQ4Z8aJc1stjppsSuTJAjTvgkiskLCCsSIW2zOYdsyWpmEisHDipui15lt_YFs6TDlNVPBw-wVnbyDysFN6BxCFWx4IblKAgIoaNiwrN9kZpi6EAClubA8eeSONxYjonEiBD1l2WQRwxDIMEE37k-UAAELNuyJpqX_5fev2u0UEWzvRUh6VoJKqYZdaQR0dI2PQld6SLLWCxLaAy60p7MgEjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درگیری هواداران الهلال روی سکوها در دیدار شب گذشته الهلال مقابل النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/89916" target="_blank">📅 11:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89915">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msneyQthTLm_1FABwhEXqn0vVG4_JgUkQVhfsm3MFGPYifheVNJWPH1-_ewWFdtOGFdb4hXJRVeNvy1HKVL7OB4RpLDRnsSeA3bxqstpgVcCnY_leerq_sDH1ljG9Rf8kAZ3fb7v264wtfGUa5jibl5Qtjhd-o2syf7fRsJFHBHRwsv9aj-UeE30rl_6gMvvi0-Y98PjBdeEUnMXYCENVXDRPzT7OGBydYST7gjeKC_Te6OBDuMWz7hMHDmyH_mpZbhLnVFR3fupqLGFrDJQdb-Pqu0cpdL7rm-BPbjWIzB5bSK8Y1axAnM_j1cAnqjT3csnIbMtKitUePww1by_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با برد ۲-۱ مقابل الچه، رئال بتیس موفق شد بعد از حدود ۲۰ سال غیبت، جواز حضور در لیگ قهرمانان اروپا فصل بعد را بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/89915" target="_blank">📅 09:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89912">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حمله پرز به بارسا:
پرونده نیگررا بدترین رسوایی در تاریخ فوتبال است. باورم نمی‌شود که هنوز حل نشده است. داوران همان دوره نیگررا هنوز قضاوت می‌کنند. آنها هنوز بازی‌ها را مدیریت می‌کنند. این غیرقابل باور است. بارسلونا برای خدمات نیگررا به مدت دو دهه پول پرداخت کرده است و این داوران هنوز در دهه سوم قضاوت می‌کنند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/89912" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
