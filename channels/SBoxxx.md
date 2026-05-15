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
<img src="https://cdn4.telesco.pe/file/ADrneVAOmRRuypjMjMBDfw2zRoU9nGQW_cIpkSHhYVphvAhjt8XQ11dJ6u38S0m8w0aUCXW97jbXg2oDaZv3qD3qVjdcDN2jPF6RR0OOVr6JMMaO_tyjp9mE0uz4dc7dd6fP4OhZocDlMbuVMfdv0I-NgOPPdaAR0xJRbGtYISgXkISlkQPCxXyqgXaXrsNMsjNE4CZLpdplTpEV4OsidpDk1tkxFzPfPefu1ViDr3qxmvECp5nVme7LxG0y4UdI87z8lWhHLesyciFvCDsWXcXPSWMP1ett9ieOGJyt03iQCncZ_faqWZGcpBx4avFalgNyVmaHg6zC6FO9w_fJag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.85K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 01:20:59</div>
<hr>

<div class="tg-post" id="msg-16343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePhKAG3KD9sXW8IRIvVNOJfKWm6FfqwCW80W89dKm7M13idJkNUkEXZX7Jv-inrhuWaHikkmznb58HyOZUBHdqcCd7rqyjMf_i_hTtaqTZ4jslFoTTMrFFFw0I-O5w2GNDCNtlLktQzfDnCuHvd5CMT_7cI6buAqAtA5kSMAd5GNc_4vrm0FA6nJoZqGOFLvM8TxmcctcDicDmUEAcRG879FtbR7jcpkLkJIydZbFcwSPLUowD3EbwOKxjin7_VX45J947fbfJH_3pRBchg7RYxsbk-Wtt3t_3eFs1BgL_AgCp9E-gB9ZCXV3BCoFu5D9WzRl7ON6yB_wI3EHi1DoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران   بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.  افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن…</div>
<div class="tg-footer">👁️ 487 · <a href="https://t.me/SBoxxx/16343" target="_blank">📅 00:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حس میکنم دوباره سوی شیر گرسنه دارد گاو می آید که ولی خب.</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SBoxxx/16342" target="_blank">📅 23:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16341">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرانسه حضور ناو هواپیمابر شارل دوگل در تنگه هرمز را تکذیب کرد</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/16341" target="_blank">📅 22:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16340">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فرانسه حضور ناو هواپیمابر شارل دوگل در تنگه هرمز را تکذیب کرد</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/16340" target="_blank">📅 22:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16339">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ مخالفت خود را با اعلام رسمی استقلال تایوان ابراز کرد
من دنبال این نیستم که کسی مستقل شود می‌خواهم آنها آرام شوند. می‌خواهم چین آرام شود.</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SBoxxx/16339" target="_blank">📅 22:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16338">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چرا میخند؟!</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SBoxxx/16338" target="_blank">📅 21:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16336">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpRm9hmqCdHdJ3fEIPpskue8NsBX0BKKbREFDFLjKz4U7w3MCwdrCndocJheRQixQRfWqDfD81MLFjIJPqDgoX-QXQoJjzjqVU7KQJRRfypMdORzynJfV6AOLcgwkob5UoZ74uUuhrwznSPWcOIibokM73rgyVKz-eYAKrTb-3yOctXZfoIw0DQcgSGweSN6VHRes6FV0vP3vL3oV0URTgaRn1J9nNxZX9ZCDH16tavYXCeqzYi3zNblB9fo9QGsYOIuGXkz-DqNVQD2t3PWTtCsgFQibKWmhfd2sqGHvJu6g86ATm30aylDa26ol_Ak8CbuJVuVrOb1ZDprvq2UBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:  عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SBoxxx/16336" target="_blank">📅 21:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نتانیاهو:
عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/16335" target="_blank">📅 20:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ولی خداوکیلی راست می‌گوید ، هر چه آدم توخالی بیسواد عقده ای که با قر و فر جلوی دوربین توانسته نقابی فریبنده برای خودش بسازد، در اینستا لانه کرده.</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SBoxxx/16334" target="_blank">📅 20:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">میرزا ایلان ماسک السلطنه:  اینستاگرام برای دخترهاست!</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/SBoxxx/16333" target="_blank">📅 20:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ای ایلان، ای مرد پرگهر !
ای ایکس ت سرچشمه هنر!</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SBoxxx/16332" target="_blank">📅 20:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">میرزا ایلان ماسک السلطنه:
اینستاگرام برای دخترهاست!</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/SBoxxx/16331" target="_blank">📅 20:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شاید ما برخی کشتی ها را با پهپاد زده باشیم، برخی ها را با موشک بالستیک، برخی ها را هم با موشک کروز.  خب اینها می‌شود تفاوت‌های حملات ما.  اما یک شباهت بزرگ هم میان همه حملات ما وجود دارد و آن اینکه کشتی مورد تهاجم مال هر کشوری که باشد، دستکم ۲ ملوان هندی در…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/16330" target="_blank">📅 19:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SBoxxx/16329" target="_blank">📅 19:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM66Qeh3Rw5J3ZLEHmEhTrvHsmJH_ewPQp7BgKva6ttsMZOxcoa7LNNbCwf0D43ww4vKtdFw8wiRWSqt2y-oZ8JlPlS7C4cU8_0VM2ViBAP_NiFWhYNducDtUhUoDnTLoEP1tqm83eUspVTLBIsQuE7BlWhrkEUlPnD2JMUzizssX73B_Q1Eha44AqNRXq5s6-TdfF2U8zyqU2XDyrE8NZf-0I01QjkHdht7GEJzzqsZGbETSpyPjASbwEWrMInLtWNobI74t0JmMWVpWeJcQFiJF9fpH-BumfYQNlti4-tXSJESXpPsA_pYtiwy_quaEk_-knCYofUsgkdjwyRk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران
بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.
افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن است به اهرم سیاسی مهمی برای ایران در مذاکرات و معادلات ژئوپلیتیکی تبدیل شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SBoxxx/16328" target="_blank">📅 18:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hd_debs03yBDFrGkQIBIzLW-E9Z_wdX09epDtsYFy2nrYwvF27HD7VfIb_dshI0_kAE9APs2q6m4yI6dOJ-PUPdnHp9z_8RVyIC4O09x2C3xOrpdfUARikZKCckXqaNh26KFrff-I9Olbognj2s2_pPfmx96lfWy28VET9BSUxch74vNPxOzqMK7Yfo7wlQNLYKP7KpDP1OpI9KqyUM0SEgs4qiZyFoCnaNNtjVnQTfr7_CVfO9HJjo4vLvX6h59VUnjhi4ykNYrR8_nhcbuWKYizdrmm8kP_tMoooXTt0VLdaTHx3_VhcmSUEbJYiJ8_TxqG3vSYy49NzAna24vwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی ؛ وزیر امور خارجه دولت :  پس از تجاوز آمریکا به ایران ، کشورهای بریکس به چشم دیگری به ما می نگرند</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16327" target="_blank">📅 15:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLsYWXs5ISvhRGIYJWdlKgMZ8zTV8I21zHciPk__v7nieFPdHvjwPhL8ZV30pN9go3xAvooXqw0eHpgQAQ_pmDJ3fZiX38P6qljSUKiJJ6nibUawb8LBHYyWOsmCqvguPwMZ5LBocctXMCVLlh4uff1krmKfE68PiyBqCP86IIwYuue8sU2djgyHAHCRqxkC1TlF1EATYLR9eZJ0WRbhsc68Zhq0SiTsOroOhNznPRgv4XWpxeUWisX7zGq8y5i8rdQUgzKuZ0D0OxkNNA8PbofuhLnPhTA3V0EY2zzKI3ySiZCiYSUwAeWPr6mhFmEQdnfV6VD0brz7X3qIlEtePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحران نیرو در اسرائیل عمیق‌تر می‌شود: ارتش اسرائیل به هزاران سرباز جدید نیاز دارد
۱۵ مه ۲۰۲۶ | پیترو باتاچی
در سخنرانی خود در برابر کنست در ۱۰ مه، رئیس ستاد کل ارتش اسرائیل، ایال زامیر، بار دیگر بر لزوم جذب سربازان جدید تأکید کرد.
وضعیت ارتش اسرائیل:
ارتش اسرائیل طی سه سال گذشته در سه جبهه درگیر بوده و اکنون نشانه‌های خستگی را نشان می‌دهد: نیروی فعال عالی آن فرسوده شده، در حالی که عملکرد نیروی ذخیره در سطحی نیست که انتظار می‌رود. به‌ویژه، بسیج مداوم نیروهای ذخیره، منابع انسانی را از اقتصادی پیچیده و کوچک اسرائیل — که فاقد عمق استراتژیک است و در چرخه‌های جنگ طولانی مدت آسیب‌پذیر است — تخلیه می‌کند. بر اساس اعلام ارتش اسرائیل، ۱۲٬۰۰۰ سرباز جدید به‌صورت فوری مورد نیاز هستند، به‌ویژه برای نقش‌های رزمی عملیاتی.
یکی از راه‌حل‌های پیش‌رو:
اجباری کردن خدمت سربازی برای یهودیان فوق‌ارتدکس (حریدی‌ها) است که همواره از خدمت نظامی معاف بوده‌اند و در حال حاضر حدود ۱۴ درصد از جمعیت اسرائیل را تشکیل می‌دهند — سهمی که با نرخ زاد و ولد بالاتر از سایر جمعیت یهودی، در حال افزایش است. در ژوئن ۲۰۲۴، دیوان عالی اسرائیل حکم به لغو معافیت آن‌ها داد، اما از آن زمان، حریدی ها به‌صورت سیستماتیک به خیابان‌ها آمده‌اند و عملیاتی شدن این تصمیم را به تعویق انداخته‌اند. برآوردهای اسرائیل نشان می‌دهد که حداقل ۸۰٬۰۰۰ مرد فوق‌ارتدکس بین ۱۸ تا ۲۴ سال سن دارند که واجد شرایط خدمت سربازی هستند.
کمبود نیرو برای ارتش اسرائیل:
واضح است که ارتش اسرائیل با کمبود نیرو مواجه است و تحولات اخیر در جبهه لبنان نیز اوضاع را بدتر می‌کند. حزب‌الله، علی‌رغم ضربات سنگینی که متحمل شده، مقاومت شگفت‌انگیزی از خود نشان داده و اکنون با موفقیت از تاکتیک پهپادهای FPV استفاده می‌کند — توانایی‌ای که در مدت کوتاهی (با کمک چه کسی؟ وفاداران سابق اسد؟ روسی‌ها؟) به دست آورده و برای ارتش اسرائیل مشکل‌ساز شده است.</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16326" target="_blank">📅 15:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: ما به پیروزی کامل نظامی بر
ایران
دست یافته‌ایم</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SBoxxx/16325" target="_blank">📅 15:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزیر امور خارجه ایران: همه کشتی‌ها می‌توانند از تنگه هرمز عبور کنند به جز آن‌هایی که با ما در جنگ هستند.</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/16324" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزیر امور خارجه ایران: همه کشتی‌ها می‌توانند از تنگه هرمز عبور کنند به جز آن‌هایی که با ما در جنگ هستند.</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/16323" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: آخرین چیزی که الان نیاز داریم جنگ است.</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/16322" target="_blank">📅 14:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">از دیروز که رفته چین 2 عقب نشینی داشته ترامپ:  — اینکه به قول خودش گردوغبار هسته ای لازم نیست حتماً خارج بشود و همین که ایران دنبال کرم ریختن اطراف محل دفن آن نباشد کافی است.  — اینکه اصل غنی سازی در خاک ایران از دید او مشکلی ندارد.</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/16320" target="_blank">📅 14:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نرخ بازدهی و نفت به جاهایی رسیده بودند که فشار می آورد و شاخص های سهام هم نزولی شده بودند. از این رو لازم بود که کله زرد یک آرامش مصنوعی تزریق کند</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/16319" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فوری | ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم، به شرطی که این یک تعهد واقعی باشد.</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/16318" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فوری | ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم، به شرطی که این یک تعهد واقعی باشد.</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/16317" target="_blank">📅 14:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ژاپن معاملات تسلیحات مرگبار را در جنوب شرق آسیا پیش می‌برد  وزیر دفاع ژاپن، شینجیرو کویزومی، روز دوشنبه در جاکارتا با همتای اندونزیایی خود، شمس الدین، یک پیمان همکاری دفاعی امضا کرد، و پس از به مانیل خواهدرفت؛ جایی که نیروهای ژاپنی در کنار نیروهای آمریکایی…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/16315" target="_blank">📅 13:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16314">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSlUwzBSg6sTMroDsQNKkACWMxHBnvb4Zp8KC3AwhIzuSqw7KQVNKQIeJ5m4Hh_Y-8rUGZFOKWCyAejPwpSv-Uy9MA37q6grVNtAgWD7QFzfutut0VqOQW3qxhy13pPLfKdB8oRN0cAulZjXg9zOn7b77b4AZAvGhapIzKWAOnE0tYu6h6fBUWHlvPQ9YimEHVnvQkNzvdPXLvdp8ODHxAO25qoUDeh2NKlZXsh-aBwvxtMUSA8mJV121aVkUSBFoNGvtIN9hk6JIDRizSnTh4v0gOCXuTIpsfUzrCzu1AlIB2BnmFeNDequxjaaqmhkZmfIcsBf9ioVYq0aWOZ9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی ؛ وزیر امور خارجه دولت
:
پس از تجاوز آمریکا به ایران ، کشورهای بریکس به چشم دیگری به ما می نگرند</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SBoxxx/16314" target="_blank">📅 12:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16313">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16313" target="_blank">📅 10:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIgAfgaB0XKXjVZnniaAYfOlht1ejRmz4BY6-LS_J5CW9-FbNZZoKmjfQeHugzgywGqXigOftusFIAU0bzXYMSgvuhg0rKNKReH_GQTukdqKbcPuT-e0AhAuddN_rweDc-ei3sopkjqWYV7ZSS4wrem5WXBGFkx_gPrHH6NMoNqDKGGrkWhBFIaGtncCCokhP4YInHwoC83K7CtMgycN2GyfZt0RwGl4Gc6H9A6pCu1PACzbRKy9V45FztRGmIMGMIExUJjCZDMxtsZs2-1z-kUGv9Mt058gAvpKC0iVZb_czhAfU1x2aZkwmTY-kWLfhyZJxZ1gDgmjAUqHmKBi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستوفر نولان این خانم را برای نقش «هلن» در فیلمش درباره افسانه اودیسه برگزیده و ایلان ماسک هم با گفتن اینکه «نولان با این فیلمش دارد به قبر هومر می شاشد» از خجالت او درآمده است!</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16312" target="_blank">📅 10:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
🇻🇪
وزارت امور خارجه ایالات متحده اعلام کرد که «اورانیوم بسیار غنی‌شده» با موفقیت از تنها «راکتور هسته‌ای» ونزوئلا خارج شده است.</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/16311" target="_blank">📅 10:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zaraban</div>
  <div class="tg-doc-extra">Shahab Tiam</div>
</div>
<a href="https://t.me/SBoxxx/16310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16310" target="_blank">📅 10:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اینطور که پیش می‌رود، فقط نمادهای استقلال و پرسپولیس در بورص باقی خواهندماند.</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16309" target="_blank">📅 10:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تهران تایمز:
آمریکا پیشنهاد ۱۴ ماده‌ای ایران را رد کرد
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره پایان جنگ را داده است.
آمریکا با رد پیشنهادات تهران، بار دیگر مواضع خود بخصوص در بحث هسته‌ای را تکرار کرده است. / مهر</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16308" target="_blank">📅 10:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کریستوفر نولان این خانم را برای نقش «هلن» در فیلمش درباره افسانه اودیسه برگزیده و ایلان ماسک هم با گفتن اینکه «نولان با این فیلمش دارد به قبر هومر می شاشد» از خجالت او درآمده است!</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16307" target="_blank">📅 09:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5KBmv_P2q16ntsYau9Ud813jRhM_TXdBtVHQzO9AThI9y8bY_mZNzopwqbJGZo0SfsLwA0PJI0OFBwXMI0DCjnB7dLUgS1WNzNrFlEZADHQDZkxM0DC2Yn_AIc1U6vorRPJx9y9MhaOrnoWsTHl588HCoVGTwaBWeg3PzYeTO4-WYTqiLU6whAu4y5AKkeeLnV6gejDNTwGlEjyD8eeLbYAVh7hJkYbWVGhHeI2PlPMJk2fsqzPdvUNVCHw42nNASPITsbvWzb73X6v1jkx5v-T9vzVR7eS7BSxfxQN8p4Gi4zcF_ByIHM3pFIBHWerE8AvKdXGHdg2xVtB-jqd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD -- H4  مسیر بعدی مدنظر پس از رسیدن به سقف کانال.  تحلیل تایم پایین تر در یادداشت بعدی...
💬
ارتباط با پشتیبانی : @cyclicalwavessupport
📌
کانال ما : @cyclicalwaves</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16306" target="_blank">📅 09:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-awNK7UvEE5_CTLzKcbytuJp2MK0N9CeqxiLswDVV1HyXrA_nrzEPcEHclLF9Svj-PIX7fxYSSE9DP98Y2ZNSxE5CSDiW6U1odOMRjPk0uoXKTY2mJicJvwxcV0BP5wh38RZLfkpo6wS4cnxoT_cZ1KrYSB2ovm6_f4Lu7aGaV_il6kFu6lfm3zf4wKw1TTibsPutCNXMYdYWay5uGNVxJbkbanNlyd2TnfV3OlmG6CGp5nCEkReoZeS0dQDu7-5hWrms_8CVZJlMmHKA2B6JWXPeFMBrZU14QYZopwwvKdl_BewHbHxcF8S6mq_JwSlsmfiJptK9d6bj-JWKrF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستوفر نولان این خانم را برای نقش «هلن» در فیلمش درباره افسانه اودیسه برگزیده و ایلان ماسک هم با گفتن اینکه «نولان با این فیلمش دارد به قبر هومر می شاشد» از خجالت او درآمده است!</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16305" target="_blank">📅 09:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ در نشست خبری مشترک با شی :
ما در مورد ایران بسیار مشابه احساس می‌کنیم... می‌خواهیم که این پایان یابد
ما نمی‌خواهیم آن‌ها سلاح هسته‌ای داشته باشند
ما می‌خواهیم تنگه باز بماند</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16304" target="_blank">📅 07:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزارت دادگستری آمریکا در حال بررسی رسیدگی به یک دعوی ۱۰ میلیارد دلاری است که ترامپ علیه اداره مالیات (IRS) مطرح کرده است که ممکن است منجر به پرداخت ۱۰ میلیارد دلار  به ترامپ شود
در حالی که رئیس‌جمهور بر وزارت دادگستری کنترل دارد ،  وزارت دادگستری در حال رسیدگی به پرونده‌ای با خودِ رئیس‌جمهور است و این تسویه‌حساب از جیب مالیات‌دهندگان پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16303" target="_blank">📅 07:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzuEzLGkvCpNerf0GXkhfD_29Kza3TBj6BHFrRQbPzuzVy5smohMyoxnwzKl4j_lMmI3IToqzGjyQ78E5AfORWBqzq0PB1M9WKFY19Hp8u6HC1NtEdkP3lQrm9dB7Bl-pjSbIoSuRtqF1Xo4TR-DDGrn9lE_7ZAInLbCHeL0ERebWIFblE_DCrKDofobwXbvMsMQJdfXf566FXagtH2ZnGEJP7uLm-wuen0nacGHqf1DoTRaUh-y9GNnmf52996qo4lvXIzDrl0cVUz9M56qshnCzH5sw0bsjW66-_cSp_bzbGuSymd1X2tOVGwIEWyrmcEchepibv-q7re2muYWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر سعودی ها یا می خواهند وسط بازی کنند یا حتی به محور اخوانی گرایش یافته اند:
🚨
ناتو اسلامی در حال شکل‌گیری؟
👉
وزیر دفاع پاکستان، خواجه محمد آصف، اخیراً پیشنهاد داد که قطر و ترکیه می‌توانند به پیمان دفاعی موجود بین پاکستان و عربستان سعودی بپیوندند،…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16302" target="_blank">📅 03:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:  وقتی رئیس‌جمهور شی به‌طور بسیار مؤدبانه به ایالات متحده به‌عنوان کشوری که شاید در حال افول است اشاره کرد، منظورش آسیب‌های عظیمی بود که ما در طول چهار سال ریاست‌جمهوری جو بایدن خواب‌آلود و دولت بایدن (منظورش محتملاً حسین اوباما بوده) متحمل شدیم، و در…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16301" target="_blank">📅 01:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7rE4qWyeeuMQ6V8T6Z-KY11o2EQJnAbheSBhjoV6MlhHv0joECFFYH5OqjKze_4albWeLQ-pyFA6A78EoDoltcpi1z7Q4FrjYtJ1e73z-VJfIQcEPaaaSSxSMDWb_10iFdbzO_0vc1yA_5ZacKlXp5gAHnOSEtW2mQn69GxBfUvl9eU18HlAeIXryGlj7oFYY-8IE_XUwYS7OQuBwJx26lg4kJfQYvTq_4uI5cfmXdWgMVio6twPfnzBCtSQybD_SpTDGpNZt07HMblTuX8Mpz77WL3SH7-AMpEPD1VP7atSrlH1coh5uZOX-vTF0pwVGvbFpesiD6EtGtU_EB0Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می رسد کوبا هم بزودی به وضعیت شب بخیر عزیزم رسیده و از شر رجس و نجاست کمونیسم رها خواهدشد.</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16300" target="_blank">📅 01:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ:
وقتی رئیس‌جمهور شی به‌طور بسیار مؤدبانه به ایالات متحده به‌عنوان کشوری که شاید در حال افول است اشاره کرد، منظورش آسیب‌های عظیمی بود که ما در طول چهار سال ریاست‌جمهوری جو بایدن خواب‌آلود و دولت بایدن (منظورش محتملاً حسین اوباما بوده) متحمل شدیم، و در این مورد، او صد در صد درست می‌گفت. کشور ما به‌طور غیرقابل اندازه‌گیری با مرزهای باز، مالیات‌های بالا، تراجنسی برای همه، مردان در ورزش‌های زنان، DEI، قراردادهای تجاری وحشتناک، جرم و جنایت گسترده و خیلی چیزهای دیگر آسیب دید!
رئیس‌جمهور شی به صعود شگفت‌انگیزی که ایالات متحده در طول ۱۶ ماه فوق‌العاده دولت ترامپ به جهان نشان داد اشاره نکرد، که شامل بازارهای سهام در بالاترین سطح تاریخ و 401K‌ها، پیروزی نظامی و رابطه شکوفا در ونزوئلا، نابودی نظامی ایران (
که ادامه خواهدیافت!)
— قوی‌ترین نیروی نظامی روی زمین به‌طور قابل توجه، قدرت اقتصادی دوباره، با رکورد سرمایه‌گذاری ۱۸ تریلیون دلاری دیگران در ایالات متحده، بهترین بازار کار تاریخ آمریکا، با تعداد بیشتری از مردم که اکنون در ایالات متحده مشغول به کار هستند نسبت به همیشه، پایان دادن به DEI که کشور را نابود می‌کرد، و خیلی چیزهای دیگر که فهرست کردن آن‌ها به‌راحتی ممکن نیست. در واقع، رئیس‌جمهور شی به من بابت این همه موفقیت بزرگ در مدت زمان کوتاه تبریک گفت.
دو سال پیش، ما واقعاً کشوری در حال افول بودیم. در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده داغ‌ترین کشور در هر نقطه از جهان است و امیدوارم رابطه ما با چین قوی‌تر و بهتر از همیشه باشد!</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16299" target="_blank">📅 01:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iez0u_j2WBk0PrsBlyT0CccucUj0VvBAi6AGzsFToWoyt_jkTDI1qXsY3XvHAf37nNrdH7vjNvv_3Yg5dAgwUODDE5-w3m6qVYg6b1DBZwudHp0BIZCCxzWuIbKpSz_7S14tDimL9Lcsawb_1sVWdUKVWm1PFoO30e5BCXLUTUKYjMriYAJh1Nl21ML6-YhVSK_NpH6DEpdKZVoK86UOXRhOVxPteR5H8Nsn5NiFrMN5YHholLfekSSH5t972ulYqAk4djvY3nGpLJ91dLEar_Sp73dnQwbIBx6ux8hXfMuBslGfefi3c94wE9BQKTxLaa0HHTT7QmPpeLKH8gjA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روش وحشتناک شکتجه وجود دارد به اسم شکنجه قطره آب یا «شکنجه چینی» !  این شکنجه روشی برای تخریب روان طرف است که در آن قطره‌های آب به‌طور منظم روی پیشانی فرد می‌چکد. تکرار یکنواخت و انتظار برای قطره بعدی موجب اضطراب شدید، بی‌خوابی و آشفتگی ذهنی می‌شود.  در…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16298" target="_blank">📅 01:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به مجالس قانونگذاری آمریکا برای جلوگیری از آغاز دوباره جنگ امید نبندید!
پس از شکست دوباره طرح محدودسازی اختیارات جنگی دونالد ترامپ در قبال ایران، بار دیگر این پرسش مطرح شده که آیا اساساً کنگره و سنا توان متوقف کردن یک رئیس‌جمهور آمریکا در مسیر جنگ را دارند یا نه. از نظر حقوقی پاسخ تا حدی مثبت است، زیرا طبق قانون اساسی آمریکا اختیار رسمی اعلان جنگ در اختیار کنگره قرار دارد و رئیس‌جمهور صرفاً فرمانده کل نیروهای مسلح محسوب می‌شود. به همین دلیل پس از جنگ ویتنام، قانون «War Powers Resolution» در سال ۱۹۷۳ تصویب شد تا رؤسای جمهور نتوانند بدون مجوز کنگره وارد جنگ‌های طولانی شوند. این قانون رئیس‌جمهور را موظف می‌کند ظرف ۴۸ ساعت کنگره را از هرگونه اقدام نظامی مطلع کند و در صورت عدم دریافت مجوز، عملیات باید پس از حدود ۶۰ روز متوقف شود.
اما واقعیت سیاسی و عملی آمریکا با متن قانون تفاوت زیادی دارد. طی دهه‌های گذشته تقریباً همه رؤسای جمهور آمریکا راه‌هایی برای دور زدن این محدودیت‌ها پیدا کرده‌اند. آنها معمولاً عملیات نظامی را «اقدام محدود»، «دفاع پیش‌دستانه» یا «عملیات ضدتروریستی» می‌نامند تا از نظر حقوقی مشمول تعریف رسمی جنگ نشود. علاوه بر این، حتی اگر مجلس نمایندگان و سنا قانونی برای محدودکردن رئیس‌جمهور تصویب کنند، رئیس‌جمهور می‌تواند آن را وتو کند و شکستن وتو نیازمند رأی دو سوم هر دو مجلس است؛ امری که در فضای سیاسی شدیداً دوقطبی آمریکا بسیار دشوار است.
به همین دلیل بسیاری از ناظران معتقدند امید بستن به رأی کنگره یا سنا برای پایان دادن به تنش یا جنگ احتمالی با ایران، تا حد زیادی واهی و غیرواقع‌بینانه است. در عمل، تنها زمانی که اجماع سیاسی بسیار گسترده‌ای علیه جنگ شکل بگیرد یا هزینه‌های نظامی و اقتصادی به‌شدت افزایش یابد، امکان مهار واقعی اختیارات جنگی رئیس‌جمهور به وجود می‌آید. در غیر این صورت، این نوع رأی‌گیری‌ها بیشتر جنبه نمادین و تبلیغاتی دارند تا اینکه بتوانند عملاً مسیر یک درگیری نظامی را متوقف کنند.</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16297" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4TZ7X8-po-q384bsEXtiqkA5w3Q4UXOpjXc5HGsJWrN31IQk4hiqi8Nncje8MuWUs1_xzelxEkUIp3JCfrJ_TgRd5LeMcX0v-tyUjcrUGlndIv1_jrZGvyDZRv5F9QxzJIM3DVWdSKiK3wQUD1ZX3uQs9B6tCB5Rcvp5nw89XRPbkfo8J23LvlRIkHI6rbxmMh30g6yhJsZb6-roP9ZzsgKiNMPBnaE5m6S2ZTQKTkPdlqWxAxasXKp9t7Xjj9emymykAGtPshvEQthfbC7vDXXWefktRwzGSeke1sHSvQxHKmD6aYT_GeF0JXq_Uiguo3CM5UtVJ9qPdPFwogdEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار فرج از نیمه خرداد کشم …</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16296" target="_blank">📅 23:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جایزه رئیس کمیسیون امنیت ملی مجلس برای کشتن ترامپ
عزیزی، رئیس کمیسیون امنیت ملی مجلس: پیش بینی کرده‌ایم دولت به هر کسی که این رسالت دینی (کشتن ترامپ) را انجام دهد، به عنوان پاداش ۵۰ میلیون یورو بپردازد</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16295" target="_blank">📅 23:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس:   ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقبه سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16294" target="_blank">📅 22:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس:
ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقبه سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16293" target="_blank">📅 22:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAz9N09UkRQ17ZS53RFueQuOq3ZXLZE0KyCcpVGoMYkgB9pmR9QvZirRCgC1JHPJKJVy0qR6QXBy_zFnG0-Iik0N5h8iqAWfkJdlxloI7CgJyQT15pnqyxvPwW9W6mxToJ0aiIjxx8ahPlv6MHyJwy6xorkla0HegIQPVUC5z8cNNkcyNf9SNuZFevmyYZ2OGMZMAlALoetNSgCA-EzWjNyWzRqpl7Zc3dLCmj8mzXfbFlUCQKiAjtKO5Ou_QfOZu5jpBZc2edppLdu-y1rT0t4-H5XZc8YND7UQCLr5ntTV3zHwPpCSgp4h-MCNnCylfaTuhcpMkme4BmdstEhDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16292" target="_blank">📅 22:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر انرژی آمریکا:
ایران به طور ترسناکی به ساخت سلاح‌های هسته‌ای نزدیک است و تنها چند هفته با آن فاصله دارد</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16291" target="_blank">📅 22:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسرائیل سطح هشدار خود را به بالاترین حد ممکن افزایش داده تا برای احتمال جنگی تازه با ایران پس از بازگشت  ترامپ از چین آماده شود.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16290" target="_blank">📅 20:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اسرائیلی ها به این نتیجه رسیده اند که هر مدل ابتکارات نظامی که ضد حزب الله به کار برده و می برند تا زمانی که حمایت فنی و مالی ایران ادامه دارد در نهایت بی فایده خواهدبود.  از این رو بسیاری از آنها الان بر این باورند که تنها راه شکست قطعی حزب الله، تغییر حاکمیت…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16289" target="_blank">📅 20:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئیس‌جمهور ترامپ می‌گوید چین توافق کرده ۲۰۰ هواپیمای بوئینگ بخرد.</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16287" target="_blank">📅 19:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزارت امور خارجه هند اعلام کرد که دیروز کشتی‌ای که پرچم هند را برافراشته بود در سواحل عمان مورد حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16286" target="_blank">📅 18:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شاید ما برخی کشتی ها را با پهپاد زده باشیم، برخی ها را با موشک بالستیک، برخی ها را هم با موشک کروز.
خب اینها می‌شود تفاوت‌های حملات ما.
اما یک شباهت بزرگ هم میان همه حملات ما وجود دارد و آن اینکه کشتی مورد تهاجم مال هر کشوری که باشد، دستکم ۲ ملوان هندی در جریان حمله ما کشته یا زخمی می شود.
سبحان الله !</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16285" target="_blank">📅 18:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭕️
قیمت‌ «سیمکارت سفید» و «اینترنت پرو» در بازار سیاه چقدر است؟
🔹
اینترنت پرو و دسترسی بدون فیلتر از طریق کانال‌های غیررسمی و بازار سیاه فروخته می‌شود.
🔹
قیمت ۵۰ گیگ اینترنت پرو در بازار سیاه تا حدود ۱۲ میلیون تومان اعلام شده است.
🔹
سیمکارت‌های سفید با وعده اینترنت بدون فیلتر با قیمت‌هایی بین ۴۴ تا ۱۲۰ میلیون تومان فروخته می‌شوند.
🟢
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16284" target="_blank">📅 17:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16283">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔹
🔹
نشست مشترک رئیس جمهور چین و دونالد ترامپ برگزار شد
🔹
شی جین پینگ، رئیس جمهور چین، در نشستی در پکن به دونالد ترامپ، رئیس جمهور آمریکا، گفت: «ما باید شریک باشیم، نه رقیب»
🔹
ترامپ در سخنانش، از «رابطه فوق‌العاده» خود با شی تمجید کرد و گفت رهبران تجاری ایالات متحده برای «ادای احترام» به شی و چین در این شهر هستند
🔘
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16283" target="_blank">📅 14:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16282">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۶ ماه پیش …
امروز مس دوباره ATH زد!</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16282" target="_blank">📅 14:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16281">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔹
چین با تغییر نام روبیو اجازه ورود او به پکن را داد
مارکو روبیو، وزیر امور خارجه آمریکا، که تحت تحریم‌های چین قرار دارد، با تغییر ترجمه نامش به «مارکو لو» توانست همراه رئیس‌جمهور ترامپ در نشست با شی جین‌پینگ در پکن شرکت کند. چین با این روش دیپلماتیک تحریم‌ها را لغو نکرده اما ورود او را ممکن ساخت.
روبیو به دلیل انتقاد از سرکوب‌های چین در هنگ کنگ و وضعیت اقلیت اویغور در سین‌کیانگ در دوران سناتوری‌اش تحریم شده بود. او همچنین از تصویب قانون پیشگیری از کار اجباری اویغور حمایت کرده بود
🟢
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16281" target="_blank">📅 13:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16280">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تنش‌های میان ترکیه با یونان دارد دوباره داغ می شود….</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16280" target="_blank">📅 13:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16279">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مقامات اسرائیلی به آکسیوس گفتند: «ما در انتظار تصمیم ترامپ برای از سرگیری جنگ، وضعیت حداکثری هشدار را در طول آخر هفته افزایش خواهیم داد».</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16279" target="_blank">📅 13:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16278">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزارت امور خارجه هند اعلام کرد که دیروز کشتی‌ای که پرچم هند را برافراشته بود در سواحل عمان مورد حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16278" target="_blank">📅 13:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16277">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">من 7.5 سال پیش گفته بودم که از اهداف اصلی ترامپ در تشدید تنش با ایران، دزدیدن مشتری های نفتی ما است که اینک دیگر به صورت کامل در حال تحقق است.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16277" target="_blank">📅 12:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16276">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حسین شریعتمداری: بحرین خاک ماست و باید به ایران بازگردانده شود
شریعتمداری در روزنامه کیهان نوشت:
این جزیره ایرانی در تابستان سال ۱۳۵۰ و در جریان یک زد و بند خیانت‌آمیز میان شاه معدوم و دولت‌های انگلیس و آمریکا از ایران جدا شده است و از آن هنگام تاکنون یکی از اصلی‌ترین خواسته‌های مردم بحرین، بازگشت این استان جدا شده از ایران به سرزمین اصلی و مادری خود، یعنی ایران اسلامی است.</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16276" target="_blank">📅 12:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16275">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
علی کیایی فر؛
کارشناس امنیت اطلاعات:
بانکها در جنگ ۱۲ روزه ، ازسرور یک مدرسه علمیه خواهران در قم هک شدند</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16275" target="_blank">📅 12:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16274">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">در طرح جدید سپاه، کل منطقه بین این 2 خط تیره حوزه دریایی تحت کنترل ایران تعریف شده که ملاحظه می کنید بندر کلیدی فجیره نیز درون این حریم قرار گرفته است.  در واقع آمده اند تا خود فجیره این حریم را تعریف کرده اند تا امارات نتواند از این بندر صادرات جایگزین انجام…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16274" target="_blank">📅 11:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16273">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxqesNBg7ccYXdj70V7vkyGsPZqzTBJd9A1KQrk9ifsPAQPSAdLQmBU5QsW1_ANPMPlKPmMjkwKUP_NwS1eAqMwpZu5KUozTVNjT4Q1GbvYHS25BPTWFwoDg11XB1_ylS9tqdYI8mubPbeuzVnwhWuO546hcnu0lnZ0l3w9lcFUV_GSK0lDzTVboTL9TV3vrMA2ikUPyHm8ppNVREpwikhv0e-lu31ZhQjZSJ6fn3ghPoghwBEM9cNAbu1NPhlPwSjXCNXo-RlqkNb1BpXqmEOLQ06XJc8jDj0bW8idusT6JYsM4Oy_d1Nmysi5noautwuhz894rutQ2Dqgu7y8UrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بحران سیاسی بریتانیا و تأثیر آن بر پوند و دارایی‌های انگلیسی
بحران سیاسی بریتانیا و افزایش احتمال استعفای کییر استارمر باعث فشار بر پوند و افت بازارهای سهام انگلیس شده است.
سرمایه‌گذاران نگران‌اند که ادامه بی‌ثباتی سیاسی، هزینه‌های استقراض را افزایش داده و نوسانات بیشتری در دارایی‌های انگلیسی ایجاد کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16273" target="_blank">📅 11:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16272">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بحران برق در کوبا  کوبا در حال حاضر با یکی از شدیدترین بحران‌های انرژی در تاریخ معاصر خود روبه‌رو است. آنچه در ابتدا به‌صورت کمبودهای دوره‌ای برق آغاز شد، اکنون به یک وضعیت اضطراری سراسری تبدیل شده که با خاموشی‌های طولانی، کمبود سوخت و پیامدهای جدی اقتصادی…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16272" target="_blank">📅 10:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16271">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بحران برق در کوبا
کوبا در حال حاضر با یکی از شدیدترین بحران‌های انرژی در تاریخ معاصر خود روبه‌رو است. آنچه در ابتدا به‌صورت کمبودهای دوره‌ای برق آغاز شد، اکنون به یک وضعیت اضطراری سراسری تبدیل شده که با خاموشی‌های طولانی، کمبود سوخت و پیامدهای جدی اقتصادی و انسانی همراه است.
در بسیاری از مناطق کشور، مردم روزانه تا ۲۰ ساعت قطع برق را تجربه می‌کنند؛ مسئله‌ای که تقریباً تمام جنبه‌های زندگی روزمره را مختل کرده است.
ریشه‌های این بحران در فرسودگی زیرساخت‌های برق کوبا و وابستگی شدید این کشور به سوخت وارداتی قرار دارد. بخش بزرگی از شبکه برق کوبا همچنان متکی به نیروگاه‌های حرارتی دوران شوروی است که چندین دهه عمر دارند و به‌شدت فرسوده و غیرقابل‌اعتماد شده‌اند. سال‌ها کمبود سرمایه‌گذاری، مشکلات نگهداری و کمبود قطعات یدکی، این سیستم را تا حدی تضعیف کرده که خرابی تنها یک نیروگاه بزرگ می‌تواند خاموشی‌های زنجیره‌ای گسترده‌ای در سراسر جزیره ایجاد کند.
این وضعیت در سال ۲۰۲۶ شدیدتر شد؛ زمانی که واردات سوخت کوبا به‌شدت کاهش یافت. ونزوئلا که به صورت تاریخی مهم‌ترین تأمین‌کننده نفت کوبا بود، به‌دلیل مشکلات اقتصادی داخلی صادرات خود را کاهش داد. هم‌زمان، ایالات متحده فشار بر کشورها و شرکت‌های صادرکننده سوخت به کوبا را از طریق تحریم‌ها و محدودیت‌های مالی افزایش داد. مقام‌های کوبایی اعلام کردند که ذخایر دیزل و نفت کوره کشور تقریباً به پایان رسیده و این مسئله توانایی اداره نیروگاه‌ها، سیستم حمل‌ونقل و ژنراتورهای اضطراری را مختل کرده است.
پیامدهای خاموشی‌ها بسیار فراتر از مسئله برق است. سیستم‌های توزیع آب به‌دلیل ناتوانی پمپ‌های برقی در عملکرد مداوم، مرتباً دچار اختلال می‌شوند. بیمارستان‌ها برای حفظ خدمات درمانی در طول خاموشی‌های طولانی با مشکلات جدی مواجه‌اند و کمبود امکانات سرمایشی، نگهداری مواد غذایی و داروها را تهدید می‌کند. حمل‌ونقل عمومی به‌دلیل کمبود سوخت بی‌ثبات شده و خدمات جمع‌آوری زباله در برخی شهرها تقریباً فروپاشیده است؛ مسئله‌ای که نگرانی‌های بهداشتی ایجاد کرده است.
بحران انرژی همچنین مشکلات اقتصادی گسترده‌تر کوبا را تشدید کرده است. صنعت گردشگری، که یکی از منابع اصلی ارز خارجی کشور محسوب می‌شود، به‌دلیل اختلال در فعالیت هتل‌ها و فرودگاه‌ها آسیب دیده است. تولید صنعتی نیز به‌شدت کاهش یافته و بسیاری از کسب‌وکارها بدون برق پایدار قادر به فعالیت عادی نیستند.
مسئولیت این بحران همچنان موضوعی سیاسی و بحث‌برانگیز است. دولت کوبا تحریم‌ها و محدودیت‌های سوختی آمریکا را عامل اصلی فروپاشی می‌داند. منتقدان اما دهه‌ها سوءمدیریت اقتصادی، نوسازی ناکافی زیرساخت‌ها و وابستگی بیش‌ازحد به تأمین‌کنندگان خارجی انرژی را از عوامل اصلی بحران معرفی می‌کنند.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16271" target="_blank">📅 10:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16270">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ریزپهپادهای حزب‌الله   فیلم‌هایی از جنوب لبنان تایید کرده‌اند که حزب‌الله بارها اهداف ارتش اسرائیل، به ویژه تانک‌ها را هدف قرار داده است، در حالی که اسرائیل به عمق بیشتری در سرزمین‌های جنوب رود لیتانی فشار می‌آورد   گزارش‌ها تایید می‌کنند که یک حمله پهپادی…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/16270" target="_blank">📅 09:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16269">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVrLOOPvjS45NouGXUbFPISdxKVOIOk_NsSjI5DhmcAlmIbikEsRUQ3_6OZetm5LayBLF_TReaJot1ErWaxvxxwrGiCGqqr2hZAQWgNju1zKMSYEXULXqsX0PlO3Li_UOIqQkj8yAXTjtVXSugkZ1l-P91dpDfL4BbnV0eBQe2uNhTU4SS_LSU9JfpG2wI5xfyYrpnTY43baxyG8pwE6YlgAEitONiTe5uqhWgj8Pix5DT0XJod4JvMcBoPxuWnWHdBNcK5_xulX9Tn0k3cPbMn8LExfQa2jP5c76l4fVuBxxh4--vAlnvIWbycNkEa7uhvOr2CFznFbmlyqvAx5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2 سال پیش آگاه است که بستن تنگه هرمز بیش از همه به سود روسها بوده و هست و چینی ها ابداً از ادامه مسدود بودن این تنگه سود نمی برند و لذا فشارشان بر جمهوری اسلامی برای پذیرش توافق کاملاً قابل توجیه است.  بد نیست بدانید اکنون بیش از 90%…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/16269" target="_blank">📅 09:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nD52Bm3HeJJHKKU9Z4lT96ppNvZYxGyqNATpmuSxfK74kdocAGZjJfu-nBPtKWwzQmT1WPEgqLHwDIxj1D6Rgi4rINoeSRwSu9WA7WWD1WYiIeurk-fTOXUAcAHbMEjYodT0Mg0mbpnpGDUbW9BjCtNzgiddivadEuwJh_-1ztDId2GAQs6yrbyS8m4gTc1SUBWQ_TzoY28YKyV-lvJsd0WdUjt9wr2pFeHHSsV2I2Np7ZIODyk4jDmGF31KJRzvKwDWZKKZm2_98phTdqmbD6Wk6LUQ_K1drnbdg759ZsaWHT0K51isYZ3y-_SFMP2J0InRAgZJJsbYtSytfd8DMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خط لوله حبشان به فجیره بود که اماراتی ها می خواستند از آن استفاده کنند تا به تنگه هرمز بی نیاز بشوند که ولی خب.</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SBoxxx/16267" target="_blank">📅 09:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ایلان ماسک می‌گوید مشکل سوسیالیسم این است که «بعد از اینکه آن‌ها «ثروتمندان را خوردند»، گرسنه خواهند ماند.»</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/16266" target="_blank">📅 09:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چرا مخالفت ونس نمیتواند منجر به اخراج او از سوی ترامپ بشود؟!
در ساختار سیاسی ایالات متحده، رئیس‌جمهور نمی‌تواند معاون رئیس‌جمهور خود را برکنار کند، زیرا معاون رئیس‌جمهور صرفاً یک مقام اجرایی منصوب‌شده نیست، بلکه مقامی مستقل و منتخب در چارچوب قانون اساسی آمریکا محسوب می‌شود.
رئیس‌جمهور و معاون او به‌صورت مشترک در انتخابات سراسری و از طریق سیستم کالج الکترال انتخاب می‌شوند و به همین دلیل رابطه میان آن‌ها شبیه رابطه رئیس با یک کارمند کابینه نیست. وزرا و مقامات اجرایی توسط رئیس‌جمهور منصوب می‌شوند و او می‌تواند آن‌ها را عزل کند، اما معاون رئیس‌جمهور دارای مشروعیت انتخاباتی مستقل است و رئیس‌جمهور اختیار قانونی برای اخراج او ندارد.
معاون رئیس‌جمهور تنها در چند حالت می‌تواند از مقام خود کنار برود: استعفا، فوت، برکناری از طریق فرآیند استیضاح و محکومیت در کنگره، یا تبدیل شدن به رئیس‌جمهور در صورت ناتوانی یا مرگ رئیس‌جمهور.
البته رئیس‌جمهور می‌تواند از نظر سیاسی معاون خود را به حاشیه براند؛ برای مثال او را از جلسات مهم کنار بگذارد، اختیارات غیررسمی‌اش را کاهش دهد یا در انتخابات بعدی فرد دیگری را به‌عنوان معاون انتخاب کند، اما از نظر حقوقی امکان اخراج مستقیم معاون رئیس‌جمهور وجود ندارد.
این استقلال همچنین به متمم بیست‌وپنجم قانون اساسی مرتبط است که در موضوع ناتوانی رئیس‌جمهور، نقش مهمی برای معاون رئیس‌جمهور در نظر گرفته است.</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16265" target="_blank">📅 09:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کره جنوبی:  «ما به شدت حمله به یک کشتی باری کره‌ای را محکوم می‌کنیم و قصد داریم پس از شناسایی مهاجم، به او پاسخ دهیم».</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16264" target="_blank">📅 08:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ:   روابط آمریکا و چین بهتر از همیشه خواهد بود. تجارت از سوی آمریکا کاملاً متقابل خواهد بود.   آمریکا و چین آینده‌ای فوق‌العاده در پیش خواهند داشت</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16263" target="_blank">📅 08:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📌
شوک انرژی جنگ ایران و فشار تورمی بر آمریکایی‌ها  افزایش قیمت انرژی ناشی از جنگ ایران باعث شده تورم آمریکا دوباره اوج بگیرد و برای نخستین بار در سه سال اخیر، رشد دستمزدها از تورم عقب بماند.  افزایش هزینه سوخت، غذا و خدمات فشار بیشتری به بودجه خانوارهای آمریکایی…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16262" target="_blank">📅 06:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ:
روابط آمریکا و چین بهتر از همیشه خواهد بود. تجارت از سوی آمریکا کاملاً متقابل خواهد بود.
آمریکا و چین آینده‌ای فوق‌العاده در پیش خواهند داشت</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16261" target="_blank">📅 06:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🖋️
بستن تنگه هرمز به سود کیست؟!  برخی به اصطلاح نوابغ دنیای سیاست مدعی اند که در صورت هر گونه حمله نظامی به ایران، ما بایستی تنگه هرمز را مین گذاری کرده و مسدود کنیم.   در صورت مسدود شدن تنگه هرمز، جریان صادرات روزانه ۲۰ میلیون بشکه نفت و مقادیر معتنابهی LNG…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16260" target="_blank">📅 22:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWDSOyCAuGz3zBjA500AvAvUbaeZDQqhwyPHVWDVfRvOmENt2ckfYszMxI2BXy8EXNdDhZq9PDGNePOUjqFwOaxNRguYE2jWvEI-zVnVE-hAmZEfNWznyoCj5UssRCy6Q3QmaJAUd0aJVub2Pa0FoYD6exoYpEfD9QUpL1qmVsiWiU2qKuDG-UEMYTYlDXcRh9_qR3iysJ3VDOExNiByxeDGrSdvtvABwKqxh83bpvFLNQ9-Z8GI6u4t8-U19r_Sfiv-KaPV6_3O0SqovZHgT5VEBycGX5PLVpztSGfgzTXnZa8ymtgjY-7PJVXgCxQxOwlR_dJpC1Dbrw-xFR9EJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پولتیکو:  چین ایران را برای رسیدن
به یک توافق تحت فشار قرار داده است
نشریه پولیتیکو در گزارشی به نقل از یک مقام ارشد دولت ترامپ اعلام کرد انتظار می‌رود دونالد ترامپ در جریان دیدار با همتای چینی خود، پکن را در خصوص مسائل مربوط به ایران تحت فشار قرار دهد.
طبق متن این گزارش، یک مقام ارشد دولت ترامپ در این باره گفت: «انتظار دارم که رئیس‌جمهوری در طول دیدارشان، در رابطه با موضوع ایران بر شی فشار وارد کند.»
به گزارش پولیتیکو، ترامپ از رهبر چین می‌خواهد تا از نفوذ خود بر تهران استفاده کند؛ چرا که چین تامین‌کننده تجهیزات نظامی برای تهران و خریدار عمده نفت ایران بوده است. هدف از این فشار، وادار کردن حکومت ایران به پایان دادن به انسداد تنگه هرمز عنوان شده است.
همچنین یک مقام ارشد دیگر در کاخ سفید به طور جداگانه مدعی شده است که: «چین پیش از این نیز ایران را برای رسیدن به یک توافق تحت فشار قرار داده است.»
بیشتر بخوانید:
https://l.euronews.com/q0ZO</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16259" target="_blank">📅 22:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6o8gR1kUIaRSA6EKE2cUtSJYSBQldMr7AKjV_QqJvjL4XspmV4bKSHpqWfEZlPftFMa536iwsJERjnoCMc4nykjsCS-sZtjNHM2BH3bD8k4tCNW1dWDEQkGQOEQfxnnV4QRrYjRzimLdtrbFSmMEr5mmRcIckaA2GDm4W9TPU7bM2ZXfiY6-u8lS15H1yU6tvj1s3A1pyNqhDxbpUhBgeJOsb1y54i7Ke8bxTEXYZYmFnb6lyIpAND1CPIRpl33-b94n6reoRexf_wx8EOafGtN3py-_QbrhfmDQWMMeaAeaW9ZAnZo2_FmyXOvx6r7So_zRL1zBjK6HhOwKCRwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗯
جی دی ونس ؛ معاون ترامپ
:
وقتی ترامپ در سفر هست و من اینجام ، حس اون بچه‌ی فیلم Home Alone رو دارم ، میام کاخ سفید، همه‌جا ساکته و خالیه، بعدش یادم میاد چه خبر هست</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16258" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9GNJsPGV-BoFoEVpwz41cLw4weEu8yZDZ4pkhiQA3mI_3TnG6kFBqXtt7OVDjzM9ZS_PljmvYSS6NrLS0CW0pSVkYIo8Ml6CyvZEuhFEa5WEjq6vp7AMtJV-KFfXMxqVrKQgA1OY6SvpelR9Hlv1U-W19gqUDCHv6-zCpm7OYx9sqhz_m1HphSbrjC2WRQRCk1VrFZPQ56ew2vkg5fPK-Yl3oESEbaRCGtxkJJl2WXGBTllBAA40Jt9zwpq1tFDMVLOHluKgUycr9rIZFTJsBTRb4BqoxlegtowPErjiQ0U8EwVRss-i-fLpnxgImhoIlQMdVUeqTyuNytSW_Dw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند تحول اقتصادهای گروه ۲۰ در ۱۰ سال گذشته!
تنها کشوری که شاهد کوچک شدن اقتصادش بوده ژاپن است.</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16257" target="_blank">📅 21:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویترز: عربستان سعودی و کویت در جریان جنگ با ایران، به اهداف شبه‌نظامیان وابسته به ایران در عراق حمله کرده بودند!
حملات عربستان توسط جنگنده‌های نیروی هوایی سلطنتی عربستان سعودی علیه پایگاه‌های شبه‌نظامی که برای حملات پهپادی و موشکی علیه کشورهای خلیج فارس استفاده می‌شدند، انجام شد.
منابع عراقی همچنین اعلام کردند که حداقل در دو نوبت حملات موشکی از خاک کویت به سمت عراق انجام شده است، اگرچه خبرگزاری رویترز نتوانست تعیین کند که آیا این موشک‌ها توسط نیروهای مسلح کویت یا ارتش ایالات متحده شلیک شده‌اند یا خیر.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16256" target="_blank">📅 21:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل تایید کرد که در جریان جنگ با ایران، نتانیاهو به صورت محرمانه به امارات متحده عربی سفر کرد و با رئیس اماراتی محمد بن زاید دیدار کرد.
این سفر مخفیانه منجر به یک پیشرفت تاریخی در روابط اسرائیل-امارات شد.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16255" target="_blank">📅 20:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16254">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/16254" target="_blank">📅 19:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-8iwEAFRNHQEUa1ufHYq1w7o9spJvAnySdhOmA0vKH2BHS8BUUioVND569yXfLRQiRy-YvA2a6ULI3EXOy9mlCwzZqRkTJ3Jv5FlZLaP9yk3j_Bn_m48DmGdZixMb-b9PxMvIyu3XZohpHRP4T67zpbTSKC_AHrHpePRS7h-RhUIuiGhn6S1_h4Tq8flgllLuuDoVrCA0yx_kKSwbv8q_D5GFt2MrQ-H4Yz6iO3uqDK1GQBIvSi2EAU2d-ZGd-wpZHfj03IppXyN-7Q0ziQuVicmAWGKhsesblcyZB420gVtWKlfpB2bwlULt5stGMgDjN2-h1rPN9FCVDKleVloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله پهپاد جدید پنهان‌کار خود را رونمایی کرد.  این پهپاد جدید که احتمالاً توسط چین تأمین شده، قادر به فرار از رادار و حرکت در میان ساختمان‌هاست، ۵ کیلوگرم مواد منفجره حمل می‌کند و طبق ادعای حزب‌الله، بردی در حد ده‌ها کیلومتر دارد.  ‌شبکه های رسانه‌ای حزب…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16253" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
🇨🇳
نگاهی به تیم همراه دونالد ترامپ در سفر پکن</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16252" target="_blank">📅 19:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asuuKAB1XnQ5sTYlBkb-q8e7nvVCc8Ag3wzjklumfe5uUKqmlkRN3aLJZLAarxTOG7o8eXtLLVQ3I7v2SwO2PQ_u-IgILRt_JfCeEbKTorORhcJWG4XmjZXtjukRJm1fBTZ5bRd9y5rgnM8wFcdBW1ocsVaa5h9KoKUuU3VdL74OwyuVJxxkQHt58_dEPJ_ySaRNEG_jlcfMxZLndvB18HAsxswsQGLgv0k9zmdtiJ-yCzF5jhM3guEhWCy1T3Aa-SblVH2lIEmfcw8xmPC0dj9i-DVEqM5Zz_lsGmgbBTcIWd1NJK63Afdu5O8-jcBNpJSQcp_YPbnRqa-b8smIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇨🇳
نگاهی به تیم همراه دونالد ترامپ در سفر پکن</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16251" target="_blank">📅 19:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585750fa88.mp4?token=oBcqbPtVDajNm7xAtHsSsAeqbJEJhee0EUWj_PX-WbuqRO3i0WRhs08fgNLC9-UDCKuXIeT92fqt99nIhw3P4eClLt3EbIVT8434PWgQl3SE-c1ea4mAJDdZnbWpWmlUrpxwjTKK6ywt5cXattN_Z78HbTgpSiNfcFKhoEIhdN4x5zlz7J5qtnUo5lNSPdrxRXSwiMwPO5yAX0ms6RqcXOG9WHd_x-6rhMGITPJEwfrEvM9oV41Duek82iABFYCna_8iwTsXJmaiMxHXBDzXNEtntkYBM4pYMi73nImJAvc6CCra5CVnW25KmM2cd_3UKjs9zhvgworcPR8hOU0KgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585750fa88.mp4?token=oBcqbPtVDajNm7xAtHsSsAeqbJEJhee0EUWj_PX-WbuqRO3i0WRhs08fgNLC9-UDCKuXIeT92fqt99nIhw3P4eClLt3EbIVT8434PWgQl3SE-c1ea4mAJDdZnbWpWmlUrpxwjTKK6ywt5cXattN_Z78HbTgpSiNfcFKhoEIhdN4x5zlz7J5qtnUo5lNSPdrxRXSwiMwPO5yAX0ms6RqcXOG9WHd_x-6rhMGITPJEwfrEvM9oV41Duek82iABFYCna_8iwTsXJmaiMxHXBDzXNEtntkYBM4pYMi73nImJAvc6CCra5CVnW25KmM2cd_3UKjs9zhvgworcPR8hOU0KgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتتاح نخستین نماینده رسمی اپل در افغانستان!</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/16250" target="_blank">📅 19:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxnj0gMSE4ZF6GDofdOTPTdmq_JxSU9wrADKRKnjB-dn_kSvKeUhENar2K85yQKysuRBAzWuq-3YSnCkC8yoSXReQLv_OLmHfDSIbO-5EzcaHN8mxZnI8AaL0PPCHjmCJLhErbI6ZM1CsqSZEROXYbuca6LFeVoFTl6Rt5CMeJjxj_h_JloNLTMqVMot-vYlFS7oQvfByVktA8Ogc29IfZW_y3t46zbpERTAGjf7jcwBAQV34VO_DKoVQlhIq7SM3-T8TdZvIjPlF_dq7hc_0INxVgrLLG9nTQW7ZRfxhcNUtuw6fq9P1-6sEZ2eUlZnVhjPuNBHeu9yG9u-oclqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح نخستین نماینده رسمی اپل در افغانستان!</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16249" target="_blank">📅 19:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16248">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۸ سال پیش …</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16248" target="_blank">📅 19:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16247" target="_blank">📅 17:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🟠
کارشناس امنیت اطلاعات
:
هیچ منطقی ندارد که منِ شهروند عادی که دشمن هیچ نیازی به اطلاعات و احاطه به من را ندارد ،  به اینترنت بین الملل دسترسی نداشته باشم ، اما مسئولی که حتی می‌تواند در لیست ترور دشمن باشد آزادانه به اینترنت دسترسی داشته باشد
دشمن آمریکایی-صهیونی تکنولوژی هایی دارد که حتی بدون اتصال فیزیکی و نرم افزاری می‌تواند حملات سایبری خود را به خوبی انجام دهد و این بسیار ساده لوحانه است که تصور کنیم با ایجاد یک شبکه اینترنت داخلی ، امنیت را به فضای سایبری کشور هدیه داده ایم
در همین ایام ، شرکت های زیرساختی که دسترسی شان به اینترنت بین الملل قطع بوده ، هدف حملات متعدد سایبری قرار گرفته اند
✈️
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/16246" target="_blank">📅 14:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭕️
استاد یکی از دانشگاه‌های کشور رفته سوالاتو اینطوری طراحی کرده تا هوش مصنوعی جوابشونو نده:
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16245" target="_blank">📅 14:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار جنگ ایران و آمریکا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crder9gRalWNmXPZ7q1S-Am9bAorVnMhTLmGbAhzlCqkJRUioKfCG03dz89vk8gXiJD0bxHI0HmO_dcbEA_2wF5rOAzaBLVMKhWdDsnpo04JQjtc1AHhEi0cEKNDbi-2DSzLn2CqEAouziqv_uKHV3s60yH5nx4GSEx8GGlywISTBTznpyDufu7U8aWppdQkGijrXfymD1S2teCFz8v3oBeenOUIzkpLcrPnV0iNZ7T4vdIEi0drhc8r5uaITMEFIZucJmt96igw8zHFE8abYX8ZyDbmbDvz_FzSnW4UbxDsXvXyLaxyHZyHrivhfHCd0Y5ihgFaMFsKRg9Lb6OXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
استاد یکی از دانشگاه‌های کشور رفته سوالاتو اینطوری طراحی کرده تا هوش مصنوعی جوابشونو نده:
✅
با ما اخبار جنگی بروز باشید
@russiamilitery</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16244" target="_blank">📅 14:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چرا_آمریکا_به_سوی_جنگ_طولانی_با_ایران_می‌رود.pdf</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16243" target="_blank">📅 12:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLV8CVBbD2f3AwmBICCDrwCPQN5Zlv2tLXTdCv-CReAOKO45aT4LI_tEx-6wjDYSvYJzDrtxO13oUh3mNsIU7QTkpv7SMsQFFjEHmvTKTvG2Or3viQXtyGm0L_0bpRoCARdDSfM-GmMNeSH1Ta7wX9H4GuER789hholr0GEsQ5GQAGSQSH1BcyHGl8DXdJjZfHpHQpaq976crO-rrnTbxEr5BtkRBJWTYhtEYCkgAcJq46Vkr1VhUCEnqqPWI3RMOcN6M4qwVVz--07sg109BimesMqiUSv1Z6n4aN48ogI311zJYu6zlTiv0kUb80U_P6EIC9Uaj9ZPs0ubxz03xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
شوک انرژی جنگ ایران و فشار تورمی بر آمریکایی‌ها
افزایش قیمت انرژی ناشی از جنگ ایران باعث شده تورم آمریکا دوباره اوج بگیرد و برای نخستین بار در سه سال اخیر، رشد دستمزدها از تورم عقب بماند.
افزایش هزینه سوخت، غذا و خدمات فشار بیشتری به بودجه خانوارهای آمریکایی وارد کرده و نگرانی‌ها درباره ادامه موج تورمی را تشدید کرده است.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16242" target="_blank">📅 12:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K71Ph95sF5LRrIdTKmBxYMtdvU_ev0A1eSzvEDQNyBEivsH21XdS6nqwew7vkgS-JjaOQRjMWIWQJ7dhHlbHpRFcmQb5WCAIEvc-ldzM2pg6qiJy7t2KbHe1L5N0kqQcugwa-fBYMksCoFi2pw_SKoI5XVu2-RAxNVeTyCC6dPMdtfPYu8t-mQIaW-3XqJpLZecNjUWpe1nTkZJbqTd25NJzkIItR5ByF8n9gBIGK48AWplf0jQfFOztzni8dJ1fERFVUOF7rny3Rlk6RKzFrJYWQ9Dsh0rNu2-Pmo1wYpba_62gvcVJHr6guYjT52IrQh7nqJ25vyFYXwbOvyOwCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جنگ ما با اسرائیل بیشترین آسیب را عربها دیدند!
سبحان الله!</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16241" target="_blank">📅 10:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16240">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ می‌گوید ایلان ماسک، جنسن هوانگ مدیرعامل انویدیا، تیم کوک اپل و سایر مدیران ارشد شرکت‌های آمریکایی در هواپیمای ایرفورس وان به مقصد چین در حال پرواز هستند.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16240" target="_blank">📅 10:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc1BkXfr2EMLSpMhD1eCjLV6YVaOwsTAHU-tGDhsl1XMvWBvVlWog2-S7UnfQxmby7RByc4XVhv2cfNx9pZuz_FSFU2ko0UVj2CJyGnWmhIHVXV2XlO06RSauxlXQZ37flDK8QJkSD1-_XfIVxThG-5VY9nxUuz6sDlbyPmD4bNHV8X6xMqEuKcQq6UZ5CMiR8EDx7xnLOnHiN8av8Nb9MD8fPy1SWGTrAlv_Y2j28F54hVNeBH1jnRwkljtBSylFeyQr9psMdOusE_VL3HDioE_KnlHCJV7cgtcLedmpvAq5VpjLNqPQ76SAJsHAu7dZrPZvBS9OpvdARcbW5wAJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD -- H4  مسیر بعدی مدنظر پس از رسیدن به سقف کانال.  تحلیل تایم پایین تر در یادداشت بعدی...
💬
ارتباط با پشتیبانی : @cyclicalwavessupport
📌
کانال ما : @cyclicalwaves</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16239" target="_blank">📅 10:01 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
