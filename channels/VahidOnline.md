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
<img src="https://cdn1.telesco.pe/file/NOYXFzYP6tZBCKDe5X33TqTbOHxh9kOnP5es-XVLKNHRHoelB0iIGtjTiA2Tj6ZauRwEBHReFPx_S0LoZOnomSsWzra69Csl1pwzGkfVsZtYrUU9aQQyPnbm7ozQeeNRw5938SMyo9OaD8jPBLm9x9Kx6PucHJSx227ziQuC-t0kFeUTPoSOoPbeAvmnsaKHpcEMfTEb1PIVhmz1Y-qM7alMk3yN6OZOBE3hEf1JZ-f_wxdLwyYo9Dbx31dXrzRG-TBm5NlBOBU7ov-NdiCwQGtF6QTf-JFcaxIT4jCtQD4tbA77-qdnMtSUPn4WPo0F22Twsrn10lPuLF50kL2fOQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 05:15:07</div>
<hr>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhmi2w2UWVsSgz3VzE2pY-7hTumlt6TJmxihk9IwTEhKVUCHlBjza3zKF0NG1p6z7ekeNEYS7eawE5KHjbpI0xR1m0o4kAA1awthxIqKClacyFdBOZMHpBuhFVRwX-RZNufF7YKFF7zmsNjfzdGzRYwLlEqr0UHQoIDapuHVM1u8HURpg5sqtPNj30LlpN5IHjX3_gzCbnobDg8dGcWhUcF-UQjf7vm1Kp_dT3oNJn9i5RiaXS7Vt-tm9yW-WqUHdfOiSxFMGNIW8cQCbh8_n8T_GQDre0uikzmeQlTu1zWNWDKKGevRRKVy1JCTVADFPKJGPVd7UEupsSyYOt99Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، از دو روز دیگر، یعنی ۲۳ ژوئن (دوم تیر) در سفری دو روزه به خاورمیانه به امارات متحده عربی، کویت و بحرین سفر خواهد کرد.
در این سفر، آقای روبیو درباره مجموعه‌ای از اولویت‌های منطقه‌ای گفت‌وگو خواهد کرد؛ از جمله:
تفاهم‌نامه میان آمریکا و ایران
تلاش‌ها برای تضمین عبور کامل، آزاد و ایمن کشتی‌ها از تنگه هرمز
اهمیت حفظ صلح و ثبات در منطقه
وزیر خارجه آمریکا همچنین در بحرین با اعضای شورای همکاری خلیج فارس دیدار خواهد کرد تا درباره اولویت‌های مشترک کشورهای منطقه گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/VahidOnline/76583" target="_blank">📅 01:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cu-y1GBYz5EiruEvPSIXpjG7yCiLiHAFlyyfnb-pY34e_ViiA77-zZAZTfZxBQ4fo3sihFAyD_0FR_GKMDVARmRWXB3PwNdfx6EKdrZPdY0bBT4E62MudEvS1FWB6Sv-c0P0maUZ7dMxEv_M-VCGsLPpILpwUOUs2QyzY-RJMnRnBDVfQ4tWzg7Lu1nfsAurdVA6cEdLNcq9yTZsJt7J7VyVt-6Me48YDu899OlNUkY2KrECTGgxjKaaJ6t-6S6fTFXaMg_mq01ENzP2JdgmlvWIU9ZWJuw0wm0klRXRaDg5enyf6Dnu3vF79HatTp8zGrzuVWtlQdIKjX_aG1KYVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
ما این‌طور از سرزمین‌مان محافظت می‌کنیم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/VahidOnline/76582" target="_blank">📅 01:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WQbwcGDye6zlRmMj0UwoQBXDhy-vwpFXiwlse20smzLlwQ6VsI14KutOfWVKMuG9SR0FTFnUW_gq1XB1d8PnWcEtdU75SQEau2OpQkg14j_-ZuozN_OaJvmkox7NA1Nk-fYNAw2jMQz5hAG5D4Jmb3Lt1BotQXMRgnC9LwoKwH7lIuTMLrvifLEY1JTYUZ6Suzgy3aVJ--HSYgbz2EiIaEk6Ow_0sB59m9sedFuI6yQg8TdvXjsM0a7M8tLmBEz6Rj2apwmTGqJVQBmHkY-PBZJNF1mGRkSN7Z6OCkVRDbwdVJE0G5QnKvHheifM5oDGapMejT1Ob2E3zGorXn1EFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست ترامپ علیه نیویورک‌تایمز درباره اخبار جنگ:
تیتر نیویورک‌تایمزِ فاسد و رو به سقوط این است: «بعد از تقریباً چهار ماه جنگ چه چیزی تغییر کرده؟ تحلیلگران می‌گویند نه چندان زیاد.»
واقعاً؟ ارتش آن‌ها از کار افتاده، نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آن‌ها تقریباً نابود شده، دو رده بالای رهبرانشان از میان رفته‌اند، تورمشان به ۲۵۰ درصد رسیده، اقتصادشان درهم شکسته، به سربازانشان حقوق پرداخت نمی‌شود، تنگه هرمز باز است، نفت با شدت در جریان است، و بازار سهام و اشتغال در آمریکا به بالاترین رکوردهای خود رسیده‌اند. این‌هاست آنچه تغییر کرده، ای ترسوهای فاسد و بی‌اخلاق، و حتی بیشتر از این‌ها!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
نحوه پوشش خبرها درباره ایرانِ بسیار ضربه‌خورده و آسیب‌دیده از سوی نیویورک‌تایمزِ فاسد و رو به افول، از طریق «واقعیت‌های» جعلی و ساختگی، به نظر من «خیانت‌آمیز» است. من همه گزارش‌های دروغین و مضحک آن‌ها را به شکایت چندمیلیارددلاری‌ام علیهشان اضافه خواهم کرد. آن‌ها مجرم‌اند!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/VahidOnline/76581" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fRlDQEMJ7t5ikgYhmaFl-jW1ety__a4AeTU_iTBRb8sKwJDdwAkOTpV8QZNiT2K77egdli4UomB3Jaso037kNsOEJ50LyJymtF0L5IfqSOX6d6ooXqgbUnxi6FuFylKprhqiGT0Gvuf9IiuQSaioC1DwsNSZHKvxkdqqYmwmCaqKEtWmI-F5E0-Il7pShTmWJy3fMfWsti9_BqilOl3gWgrDaBCWTOwHWstVuBPJ1ZoNA5L08uvgtiaXrYvx0H-JuNgK-s9TbzCAqNrIzEqIn8xK3dU4_JOJhBnFmHZorqZBSqMlrMDxtRf7NcK8OzgMOTZTW5xoEr2Vhk0WzwCDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WNMQh3PdG-OU--QJMDbVaWbXUc2lDQ4L4dVyWqXQ2pDH9lNBsIXFxPSgPgvFMXC1DxCrvUtMN6stin1asGwp2xSPMUOlrYTytJ1CuGvffMNaX64673RBx-CvH2Uv7gmQRGkAnCkDNgFivsIl4DMlDC-u9QETFUfGdzOcYZj7_6qZS_xSdYAuIPG6CxAzYxKggkDju2DXl8owjo-tZGqbGLMrAXqqStr7xIap7HxDQLyu5nmJBvyT1QU93F7IhIi94wVwS8O2af9jvac8Gk-V5mTZdeZX720A2jxan41YshH1moHxqZKvw5hXgT07Mz1jy3dx-dpPvwaxRD0wU-yseQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gObCnZcrkbCL8koT1n8VtqJRYPkqEXlW4iF2J8Nfz0c1sV2NfP71jqKdqrrUstDYw98jgMLLVGCt7sgKvAmizaTahj0HWfs4jKPXxsXpIsuVcNDuLOGmDBKn03osH4dp1vSezfzXcwXhdmjB5EX0y7NxujZ3lHqrYgb0-YBbQnFWPLeEUbdQm9g5OIt5afN-wAGiFoRAacrs4p6I9OoORADA_5C2pPC83vZg1JOPrp6tM1sR3Jw1lyvarFcFi96b016vO55ef87TyiJ7fQwZ6QjelwR5j5YTxfSqsrPSbwQIf8rXd5hCYh1Sn3MCQrMebbk6VSfLPzuWq-EbrbvFhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TtU767PXmiiS3B_TMaYTKP4DoT9JOVRLChzaEybadtIR2dbGr5Eqe5msz9PcNRHsGcurZTU6FMu-iS1lJWQTvurqxIa6t5RDngfwoBaYbEDCz_6DVtwm9etjKXrx1GB2nZLU55ffYmky8fPNIIQLJ5XZMgHUBYMc-pim0lvB9Sd_TKqyu2yyrBD7apYgMX1PZTc2tb0ZrYif1VgQYtgfCZgO--bNZZWNZh5GeOPt4c-nNGX6lsa7tEhL8rSh9jrrB9xVU9jXxKAP6l32M890KeitJqBofZqVbkXRk8_4heJeQb3L-1MWXdOmU0LGVn9edEuW8tqFZNsCjGSLV-L2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gvDvT4UNZA10_aRg0pVST-MkCa6w48MiW4anwp_zG9NH0LDaajuKxOpe6TfIkg1H06iBPrEH5oCIXhVsNABKHq-_0pvWuPDnaFqtI8Nbs6FfjWhZ1QP3dZPEIufAKDfP4fxV1RVNuKFwDngLDzloWsWdKBFevc-SgVZWK7V2fjU54BBl3LXX04afBmScuZBwOWwmp7TFYFom9K4AdoWbPbFcrUHxRTRTMCkiIo2NjQmAiTrrjkjQYoW8ue6NpWqc76vYKPXKEUeCeJxSmjBz50ymwgAzUtJLTpZGjbH4Xs4w8psvRdsUnAcEEHC4Ucd7PBsk6nYTsR-m_KNVflj3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qb-IoB5wZlZHLTZjSXQu8c78OPgfDn9njAEJD9mgOvYroTmHAmKpWf99ChIssYN3lnkiDND92_R-zjoAPuv4mKXzxC9lSEyFM9tVl69qMbYC5QT2GDv0vlODOpSo2w0V76vLUc9LbgFHfIdLePz9xvwGfrqxp60iCReFIHQRQC-H7e09Jyplv-WDH5TBtj4_CuCn7Q8VS9egrHNx_iI-QlqvAKsl-DgVQJcmActQXyZjq_epgwhb1-tqPUjDn8Oh0TQmsBG6FUBnifxbEyVtcswzlLpZvsts2GJQ7TeBonkB-b-8WqDesOptx42bxKfTF344YZCxu9TAmILwwk9VZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QkE5zSHCwRrhNbBNLESsk0XDRzr2noShpp5D8NpnaOxSQUM9bGqJdiPJbp8tDj-P2jgtdYLFI_CJQCzQoYon044QIXAGNPBXQXRsAQcEZUWHVJ-oXzGjdDA-xD0dZN72Zz_SaDlyTUT8bomliFum-7CsT6GE-H60CfLGxeDC-y5QuZ7LPk5EmwZF2jTvtxvkjo1V4thqDFd6MMBzUDCKvtGH1nYDhx1m4W2FccKYLlAZCcGkQIYq5gSGc_vUTg2xOpClcOXADAoyOq48sTLkIzPNM_a7e93vyr5mJTIBMTFUL0lB3S0u-oOeugRgmzH7hEwBFgeJ6Me4OcCLh8t5KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=ZCafPW_KyUYfu-YKUabiWmMLcrYRK9W0_dQX91brwUC-XmIcApblIlWwcIg9ETKm78t4THXlumrMNG1B0IK5KJl-2Vi8e7BCNsDxwdOwsGUJQn0OIO6wE0yltFqKpei0WJ1yT85MfNIFWAPnTmOlsSNdq7erwjD6zVjb06HzPmga9T54_uJMKpV3j76wUhNwpb42YmA_IE1AtqAJABdmNgwSGhPGfZsBGCznai-vhn5SsVvCAoUGKIne4tFW6TlM9MAaMpRb_n7OAQbiUd32WBGmHCcazkZy1MzhcVmQ5WiDJiYnhzCOFamJmolpb_BTQh_rQm5EzEcC2OUP-1GZlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=ZCafPW_KyUYfu-YKUabiWmMLcrYRK9W0_dQX91brwUC-XmIcApblIlWwcIg9ETKm78t4THXlumrMNG1B0IK5KJl-2Vi8e7BCNsDxwdOwsGUJQn0OIO6wE0yltFqKpei0WJ1yT85MfNIFWAPnTmOlsSNdq7erwjD6zVjb06HzPmga9T54_uJMKpV3j76wUhNwpb42YmA_IE1AtqAJABdmNgwSGhPGfZsBGCznai-vhn5SsVvCAoUGKIne4tFW6TlM9MAaMpRb_n7OAQbiUd32WBGmHCcazkZy1MzhcVmQ5WiDJiYnhzCOFamJmolpb_BTQh_rQm5EzEcC2OUP-1GZlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال ایران در دومین دیدار خود در مرحله گروهی جام جهانی ۲۰۲۶، با ارائه یک نمایش دفاعی، در ورزشگاه سوفای لس‌آنجلس مقابل بلژیک به تساوی بدون گل دست یافت.
مدافع بلژیک در دقیقه ۶۶ از زمین اخراج شد و این تیم ۱۰ نفره به بازی ادامه داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/76571" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQ2f2mm53dHYgGpGVgb27cLiaeSNFaT93_BB3vT3eaf6nTKW7KQo968SreMKUxUYIzzOfOrtQP7vu4m4KoCUFbyyb3mEIv2PWMd7g-7i-RLvITugGR_qo_dpdNwSVF5wr8690xkrogLxgUrhJOsi_Zo6bS7M4ptbqyVglIxduWhdM6GuUfAx2qiCzGONpIK3zi7fZhKKC6kjpCX_zKzcUs3LvUtLz0VS0ri7TGFAfwJTUFZAVUKyNxzPTGvm098PzOfGWZi4lr1m2esHySxCYvCU83MzDh0DQ7qtuRaAjH7EHj3ZqLEf8l-ONxVodyB-4HNZk8ZPUDd7KIInj6h8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
بعد از آن‌که تریلیون‌ها دلار خرج ناتو کردیم، ایتالیا و نخست‌وزیرش حتی فکرِ درگیر شدن با جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آن را هم نمی‌کنند. دهه‌هاست که ما از آن‌ها دفاع می‌کنیم، اما وقتی پای آزمون به میان می‌آید، آن‌ها برای دفاع از ما و بقیه جهان حاضر نیستند. خوب نیست!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/76570" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ip_YOJMk9gGtN9PUie5bselRiOvI9W8h78HYeFNzBVcZPWc8DR_bAnH-GLdRmVX2BqVSNOFAPc0IaG3GpcuhUwFq_urd9cRObwHfzsIC_etP0Ernaiw0GhmKg9FykenbzwHyNinTVaKxKAitJlhMyg-Du7afv-juJ4HcXql39aNPmFysu-gl56r346epr_7SueYFYyCvaoeerXfxEjVjA8zX_isrtaSdQgs5u-qB8xsWcEhqloLZSsS4sT0UdaeGkpU0zxwlf5XfRWwafwWO5uOB41qu9SmBg7jdEfNeunHce4F42xzhOfXSpkkH3xM0D2y-2KbYidPAcZBK1tMHog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ک مقام ایرانی یکشنبه شب ۳۱ خردادماه به خبرگزاری رویترز گفت مذاکرات میان ایران و آمریکا در بورگن‌اشتوک سوئیس متوقف شده، اما پایان نیافته است. این مقام جزئیات بیشتری درباره علت توقف گفت‌وگوها یا زمان از سرگیری آن ارائه نکرد.
این اظهارات در حالی مطرح می‌شود که گزارش‌های متناقضی درباره وضعیت مذاکرات منتشر شده است. پیش‌تر باراک داوید، خبرنگار آکسیوس و کانال ۱۲ اسرائیل، در شبکه اجتماعی اکس به نقل از یک دیپلمات حاضر در مذاکرات نوشت که هیئت ایرانی محل مذاکرات را ترک نکرده و گفت‌وگوها همچنان ادامه دارد. با این حال، خبرگزاری ایرنا دقایقی بعد به نقل از یک مقام هیئت مذاکره‌کننده جمهوری اسلامی گزارش داد که مقام‌های ایرانی پس از دومین دیدار با هیئت قطری، محل مذاکرات را ترک کرده‌اند.
@
VahidOOnLine
خبرگزاری ایرنا، رسانه دولت جمهوری اسلامی، گزارش داد هیات جمهوری اسلامی پس از دیدار با هیات قطری، ساختمان محل مذاکرات در سوئیس را ترک کرده است.
هم‌زمان، یک منبع نزدیک به هیات مذاکره‌کننده جمهوری اسلامی به شبکه سی‌ان‌ان گفت گفت‌وگوهای میان جمهوری اسلامی و آمریکا در سوئیس متوقف شده است، اما پایان نیافته است.
به گفته این منبع، گفت‌وگوهای غیرعلنی همچنان ادامه دارد تا طرف‌ها به میز گفت‌وگو بازگردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76569" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pFQ8weGC-A5UfxBn6usT22t-p3SRL0qbnAL9HyvM_3csSVM7lDWnD7Zl52-5LJc0jhNkSogLXzz5ipOxpQS1fe6XnJU7W69IoRuC048Pfv3NEeStLcEg4kTkw2fy6HU_D6gKUujcUAfvZWwXHvLHRyokY2v8KOZqQEopRatu8ZUvm55xsnKNxDVco5tuKLoWmCrgojwfsuGJFPSiBopNMCBc877EEy9ijpIw6ZYLLmNfndCGoPIu6t23fV-mqWGgU680QqtCDfKp7_yCIZsod_bdO0OllvXhuiD6fk9X0nPMWsWsluDgwBDe_JNhv2nvkGZtcj7j9wf7ImAsFf3m6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
"
ادعای فارس و تسنیم به نقل از "یک منبع نزدیک به تیم مذاکره‌کننده"
پیش‌تر در
اکانت قالیباف
همچین توییتی منتشر شده بود:
با خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76568" target="_blank">📅 20:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PmGn_NaDB_xHDySDP5R2nvgFxM73fEFQ1OusJzmLWS0lo4tM5KTBNufWKSP2QXizFJKfzm8QyMtFYfhNyVUSq9146Oqf3INpVeQ3A2RmVTIo2ztKPg6JlL1HB0bwUrXeWl2oZKUCWFoTFb-z2ePQ-YfV3MLtw9T5jmrkqslcO1x6ZVonOnkNjo3iTRIYYfIkl2bfosiv_GRw8I6qwdRroR5MmZJ1Wlxa8dDBRxHO1IKwKi-KBrNWTZLyMBK0fv3RqZ8J1GDtIiT1SD3UCUaHFMg6vlGlHJs-e1kmRiQ7zz3OU44SV3QwjinDVQ22bnV_bcWT1RSYZnD2B4qJkQhL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در واکنش به اظهارات مسعود پزشکیان، رییس دولت جمهوری اسلامی، درباره ناچار شدن آمریکا به پذیرش تفاهم‌نامه میان دو کشور، هشدار داد که تهران باید در مواضع و رفتار خود تجدیدنظر کند.
ترامپ در گفت‌وگو با فاکس‌نیوز گفت: بهتر است مراقب حرف زدنش باشد. بهتر است رفتارش را اصلاح کند، وگرنه ما کنترل بقیه کشور را هم به دست خواهیم گرفت.
این اظهارات پس از آن مطرح شد که مسعود پزشکیان روز یکشنبه ۳۱ خرداد گفت: آنچه مسلم است از حق غنی‌سازی اورانیوم هرگز کوتاه نخواهیم آمد و طرف مقابل نیز ناچار است آن را بپذیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76567" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WVf_WynWNqDKYNO-v16_slJCRcEj_Wa2pdabMMt3teKklDHL7vFNn8RVrJIRCbvK-4OW3k5KjLpA9vtWuB4bdVWY9V-qI8jtsLlMk-mdia5k5bweK1z9lkIuwz49BrNAwACZ6sNd2WXiTbztKPG2JbULO0fQOKo7qjDHOt1c8aD56RPwIL_wbOzSeRAMAx9V9E9UxyYLjyphFnR-ehcB4ljka2aLpw_-hrfRbK473OsoAATLUBfrlFG-BnO7_gWOK8ku76YIK_KL1NgiFEgJHVolBoATnkn-VEKBxprakJiuGbBd3R3JNz-yAqU-cwfjg3WA-dN4QKSi9QRo_jZTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد همزمان با برگزاری مذاکرات در سوئیس، به مقام‌های جمهوری اسلامی درباره هرگونه اقدام برای بستن تنگه هرمز هشدار داده است.
او در گفتگو با شبکه فاکس‌نیوز گفت این هشدار شنبه شب به تهران منتقل شده و تاکید کرد در صورت چنین اقدامی، ایران با پیامدهای سنگینی مواجه خواهد شد.
ترامپ همچنین گفت به مقام‌های ایرانی گفته‌ام که اگر تنگه هرمز بسته شود، «دیگر کشوری نخواهند داشت و حتی امکان بازگشت به کشور خود را هم از دست خواهند داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76566" target="_blank">📅 17:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RtdRK7DagCtKV699JSUwW_bO77WJsaReAtG-V3WT4Fq6xW2YavJUc5OmBFWv2K3w6LvLHwUV5iReR8TZU1hKXED5Ux9rBSTy5yLtu1w_8KgDG8lBtRW4SERGZd5Ii90MnbOsTDeh16wlGzHvmY7WFk32EFnWnqFVKy_DSZMDrET4nGIczafJSxRIJmgGAAXzGETWaPd00thuXBxR0qRKC6aWQDQl5wypPRGwgPiTGw9S9t4168DAPreW08yX4whRYXxpRvxNc6zxx9Cz-4d6Z3Ah5avDQ6db6OoJUiYUUWOHrMpSKf1w2IUnSFttbIPvfHQxbEpxWja7qXOKulBAmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران باید فوراً جلوی نیروهای نیابتیِ بسیار پرهزینه‌اش در لبنان را بگیرد تا دیگر دردسر درست نکنند.
اگر این کار را نکنند، دوباره به ایران ضربه‌ای بسیار سنگین خواهیم زد؛ درست مثل هفته گذشته، اما این بار شدیدتر!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76565" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=Jt6C4QH95RHePoTsUo9jhRjC1sKEtGawnpK14exvgKQYqSgUfEzd1syvjfU0sjGLyVMUy-6t_DBrqRKyerdp2bfd5i59Rj4uqTHaGi671IMtTBAntipB2PtVkWbX44KiZ26F_XMUJ3D_IAGj13LZJqsEZAlXGvGg7KrMz604_3YkJvKw9uoTkZNwB9FVDQZKq1klcK4NFWiVwSnlJmc6vggJ7baSEYHOBNOg3OEByRjaxlhqgiPOa7vMs1j_jRGgnAIBmMf6_k60kKuqdtGQWBhia-GzOw-E4nisqSaSDYl8S9jb28MMJDEKUe6ZSR6NPxrrIl921TiVPJNUeqpAgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=Jt6C4QH95RHePoTsUo9jhRjC1sKEtGawnpK14exvgKQYqSgUfEzd1syvjfU0sjGLyVMUy-6t_DBrqRKyerdp2bfd5i59Rj4uqTHaGi671IMtTBAntipB2PtVkWbX44KiZ26F_XMUJ3D_IAGj13LZJqsEZAlXGvGg7KrMz604_3YkJvKw9uoTkZNwB9FVDQZKq1klcK4NFWiVwSnlJmc6vggJ7baSEYHOBNOg3OEByRjaxlhqgiPOa7vMs1j_jRGgnAIBmMf6_k60kKuqdtGQWBhia-GzOw-E4nisqSaSDYl8S9jb28MMJDEKUe6ZSR6NPxrrIl921TiVPJNUeqpAgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس و عراقچی در یک قاب
خبرگزاری تسنیم به نقل از یک منبع نزدیک به تیم مذاکره‌کننده جمهوری اسلامی گزارش داد که هیات آمریکایی و برگزارکنندگان نشست ژنو قصد داشتند پیش از آغاز مذاکرات چندجانبه، مراسم عکس مشترک و صحنه دست دادن میان هیات‌های جمهوری اسلامی و آمریکا برگزار شود اما محمدباقر قالیباف مخالف کرده است.
به گفته این منبع، محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، با این تشریفات مخالفت کرد و اعلام کرد اعضای هیات جمهوری اسلامی در مراسم عکس مشترک با هیات آمریکایی حضور نخواهند داشت.
این منبع افزود در پی مخالفت هیات جمهوری اسلامی و خودداری آن از حضور در این مراسم، پخش مستقیم و برنامه عکس مشترک لغو شد و پس از آن هیات جمهوری اسلامی وارد محل برگزاری مذاکرات شد.
به گفته این منبع، هیات آمریکایی از هیات جمهوری اسلامی پنج دقیقه فرصت خواست تا خبرنگاران محل مذاکرات را ترک کنند. او افزود مراسم پیش از آغاز مذاکرات، بدون حضور هیات جمهوری اسلامی برگزار شد.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز یکشنبه در آغاز مذاکرات ایالات متحده و ایران در سوئیس، این گفت‌وگوها را «تاریخی» خواند و تأکید کرد ایالات متحده آماده است روابط خود با ایران را به شکل بنیادین متحول کند.
ونس در حالی که در کنار نخست‌وزیران پاکستان و قطر ایستاده بود، در اقامتگاه بورگن‌اشتوک در کنار دریاچه لوتسرن گفت: «این یک دیدار تاریخی است. پیش از این هیچوقت رهبران ایران و آمریکا در چنین سطح بالایی با یکدیگر دیدار نکرده‌اند.»
تصاویر و ویدئوهای منتشر شده از محل نشست نشان می‌دهد هنگام حضور معاون رئیس‌جمهور آمریکا در اتاق محل مذاکرات، عباس عراقچی، وزیر خارجه ایران، نیز حضور دارد.
معاون رئیس‌جمهور آمریکا درباره اهداف مذاکره با ایران گفت: «آنچه رئیس‌جمهور از ما خواسته این است که فصل تازه‌ای را آغاز کنیم تا روابط خود با مردم ایران را متحول کنیم و دست دوستی را به سوی آن‌ها دراز کنیم. پیامی که به مردم ایران می‌گوید اگر رهبران شما حاضر باشند از نقش‌آفرینی به عنوان عامل بی‌ثباتی منطقه دست بردارند، و اگر حاضر باشند در بلندمدت از جاه‌طلبی‌های هسته‌ای خود صرف‌نظر کنند، آنگاه ایالات متحده آماده است روابط خود با آن کشور را به شکل بنیادین دگرگون کند.»
او ادامه داد: «این بدون تردید هدف ماست.»
ونس همچنین گفت: «ما تنها در چند ساعت گذشته پیشرفت‌های بزرگی داشته‌ایم و انتظار دارم در ساعت‌های پیش رو نیز پیشرفت‌های بیشتری حاصل شود.»
او با اشاره به اراده ایالات متحده برای «متحول کردن» خاورمیانه، افزود: «ایران در گذشته یکی از عوامل بی‌ثباتی منطقه بوده است. اکنون آینده‌ای را می‌بینیم که در آن همه بتوانند برای پیشبرد صلح و رفاه برای همگان با یکدیگر همکاری کنند.»
@
VahidHeadline
جی‌دی ونس پیش از آغاز مذاکرات اعلام کرد واشینگتن طی ماه‌های اخیر بیش از هر کشور دیگری برای توقف درگیری‌ها در لبنان تلاش کرده و این روند را ادامه خواهد داد.
او با تأکید بر اینکه «صلح آسان نیست» گفت رسیدن به توافق نیازمند تلاش و «بده‌بستان» میان طرف‌هاست و افزود هدف آمریکا تنها صلح با ایران نیست، بلکه دستیابی به ثبات در کل منطقه دنبال می‌شود.
ونس همچنین مذاکرات جاری را «آغاز یک گفتگوی فنی» توصیف کرد که قرار نیست همه اختلافات را یک‌باره حل کند، اما فرصتی فراهم می‌کند تا طرف‌ها برای نخستین‌بار درباره مسائل اصلی به‌صورت مستقیم گفتگو کنند.
به گفته او، حضور رهبران سیاسی برای تعیین چارچوب مذاکرات و حمایت از تیم‌های فنی است و با وجود چالش‌های پیش‌رو، طرف‌ها با انگیزه برای ادامه مسیر آماده هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76564" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=DyNT1wk-_7PNG1HqUpvzXEGadlpKMDc_VfrphsOa_7oWSBUzS1nDsZecn0tBxsAKrn7MCjiCw2byEjqZItlsIGqAXeAfvdyvSm2oa5UQ69EVq0fc8uFihcgZS_5As3b4sB_1R8iJ7J-0YFotCnijTpkZEbSToqDFlFDBGFYaOWYBxo-oem9vZvh2PdcG2bCud9xY_2arkoxC6RNg6I192nbBSymjf5SrOp02eD0JXxnBBLCkN6RRpL-zD-1PqmkRQo4usbgkkUaCvzStZnUiDOOP740tuf0xvgx5NZMQR7UwpIEyRPce1ne-6G0MDd3VzFRJ3OsN8m2x8M2LDNWMDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=DyNT1wk-_7PNG1HqUpvzXEGadlpKMDc_VfrphsOa_7oWSBUzS1nDsZecn0tBxsAKrn7MCjiCw2byEjqZItlsIGqAXeAfvdyvSm2oa5UQ69EVq0fc8uFihcgZS_5As3b4sB_1R8iJ7J-0YFotCnijTpkZEbSToqDFlFDBGFYaOWYBxo-oem9vZvh2PdcG2bCud9xY_2arkoxC6RNg6I192nbBSymjf5SrOp02eD0JXxnBBLCkN6RRpL-zD-1PqmkRQo4usbgkkUaCvzStZnUiDOOP740tuf0xvgx5NZMQR7UwpIEyRPce1ne-6G0MDd3VzFRJ3OsN8m2x8M2LDNWMDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، همزمان با برگزاری مذاکرات مستقیم میان ایران و آمریکا در سوئیس، گفت همه نظامیان در شورای امنیت ملی موافق مذاکره بوده‌اند.
او در جلسه‌ای به مناسبت تشکیل بسیج اساتید در دانشگاه تهران، در میان صدای اعتراض عده‌ای از حاضران گفت: «همه امضا کرده‌اند که این راه را باید برویم. حالا هر کسی می‌خواهد تفرقه ایجاد کند، این گوی و این میدان.»
او با اشاره به نظر فرماندهان نظامی در شورای امنیت ملی گفت: «فرمانده قرارگاه [خاتم الانبیاء]، فرمانده ارتش و سپاه، و نهادهای امنیتی همه بودند و همه یک حرف زدند و همه متحد بودند و همه آن چیزی را که می‌خواستیم عمل کنیم را امضا کردند.»
این سخنان پزشکیان در پی افزایش انتقاد اصولگرایان تندرو از دولت در پی انتشار نامه منسوب به مجتبی خامنه‌ای صورت می‌گیرد.
آقای پزشکیان همچنین با تاکید بر نقش دولت در حمایت از نظامیان در دوران جنگ گفت: «۲۰ میلیون بشکه نفت که مال دولت بود را به هوافضای سپاه دادیم. ارزهایی که داشتیم را به این عزیزان دادیم.»
@
VahidHeadline
مسعود پزشکیان، رییس‌ دولت جمهوری اسلامی، گفت نگرانی اصلی او این است که دولت نتواند رضایت مردم را جلب کند و نارضایتی‌ها به اعتراض‌های خیابانی منجر شود.
پزشکیان گفت: «از آنچه می‌ترسم این است که نتوانیم به مردم به درستی خدمت بدهیم، ناراضی شوند و به خیابان بیایند و اعتراض کنند. آن وقت ابهت ما فرو می‌ریزد.»
او افزود مهم‌ترین قدرت جمهوری اسلامی، وحدت مردم است و مسئولان نباید اجازه دهند کمبودها، کسری‌ها و نواقص باعث نارضایتی مردم شود. به گفته پزشکیان، بروز چنین وضعیتی موجب «خوشحالی دشمنان» خواهد شد.
@
VahidOOnLine
بعضی از جملات پزشکیان به انتخاب خبرگزاری دانشجو، وابسته بسیج:
🔸
اظهارات عجیب پزشکیان: من از این میترسم که نتوانیم مردم راضی کنیم و به خیابان بیایند اعتراض کنند
🔸
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد بود.
🔸
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔸
۶ میلیارد دلار پول ما در قطر برخواهد گشت.نتانیاهو اولین ناراضی از مذاکرات است.
🔸
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم، این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
🔸
شورای عالی امنیت ملی در وحدت و انسجام تصمیم گرفت؛ همه یک حرف زدند و متحد بودند
🔸
مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده/ آنها پذیرفتند که حق ملت ایران را نمی‌توانند نادیده بگیرند/ قاعده عوض شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76562" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yup6IdXgiMw4oqsTUNlkazCN4P4bRyM9Sj-9Dx_AfcvdNtIid7wwa1c-kzKhYLyoug8QfObhtBgZUdwHZft-tW-On_qFDJnMSA18Skje0OcyKo5i023-T7fbcOQXqsXTsz3mYmq6ab6Mhb1J6Yibe_SDHBm6IhMX2AOsz_Y02yY_7X4IacpKsSn2EGhA-W0sFCuynX-VkF9e9GlZ-7_O5jfVXWhK3v7oIb_p4co7iSFjWJZimnrUxZzUu7DIzHuq8rWJr5ghEcWB4mQoh9zVHr9gTBTw21if-W5oPIBhlSTAFvhSnpKwoL6rRvhKa7P_a229_klI59Vq4xxugyi3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو منبع منطقه‌ای آگاه گزارش داده است که آمریکا می‌خواهد نخستین دور گفت‌وگوها با ایران با دعوت تهران از بازرسان سازمان ملل برای بازدید از تاسیسات هسته‌ای ایران پایان یابد.
به گفته این منابع، این تاسیسات پیش‌تر هدف حملات آمریکا و اسرائیل قرار گرفته‌اند و آخرین بازدید بازرسان از آنها پیش از جنگ قبلی، در ژوئن ۲۰۲۵، انجام شده بود.
اکسیوس می‌گوید: «آمریکا در مقابل آماده است به ایران اجازه دهد به بخشی از دارایی‌های مسدودشده خود دسترسی پیدا کند؛ از جمله حسابی به ارزش شش میلیارد دلار در قطر.»
بر اساس این گزارش، ایران می‌تواند از این پول برای خرید کالاهای بشردوستانه استفاده کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/76561" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIg8gRf1FiPSsIO4ydyO-4tfLQdaL-7zxtddJbdLnWqM_1RHPi9SOGR21I_3ZFb5lugsQpNQdESqwaZVN8qfS4yMfiZI2OH-umGYZQGio4Tb_WaJs7nMmcqHu3tnLJgQc_gttvXRz4jMJoEY-eWSw6a756wnF70u-3xyGHQU9VgJSCwpPQKzpLd9E-PnllPya_IlN_4WNpCZYMumViRGHmuidfOWtw6if5ylE2YI8ZwuRCiLelHQy_cm2zsNIDD0YmKT82R4pMN_hCx0TLS6EuSFoq0F0ugfhNSRV-e25aW8E1DVMISAmy2Ts_5_OD6B_ysDldKjigg-yEBGhwZzCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های بهداشتی در غزه می‌گویند که دست‌کم ۱۰ فلسطینی در حملات هوایی و تیراندازی نیروهای اسرائیلی در چند حمله جداگانه کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/VahidOnline/76560" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm3GPqyv_RsBgc_lE1O1vyk1GIHXd37f-JTXZwjGVyn2ijc3gJzy_tyLvSxlo2QfMl07KDI7nqOeYdt_vLhbfP5X9vnzGGuFTtOFbPth23MUFDmUXoqNIOHy7lyIhBe2DyJx64S5uWFPjepJzeRHcLhaXkHQRRxqxBT48WG7uXhpp9116LwVuv-JvPogh10Gj-SsorhzUfbZKVXSF36XqRrVMSXZLboTnGu5kysAgBI253KOQ-kewINVlXjbZTE8OqZZQZX57qJsR4FACfRxNr7-9ZYzrI5fupfNVZCK1S5l2dGJYcO9DDsXdZnrWvG2ta7SwGxc03Ae8aFjODFxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از هزار دانشجو و فارغ‌التحصیل دانشگاه صنعتی شریف با امضای نامه‌ای سرگشاده خطاب به محمدرضا تجریشی، رییس این دانشگاه، نسبت به آنچه «تشدید فضای امنیتی» و گسترش برخوردهای انضباطی با دانشجویان خوانده‌اند اعتراض کردند و خواستار پاسخگویی مدیریت دانشگاه شدند.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف تاکید کرد که بیش از هزار نفر این نامه را امضا کرده‌اند. انتشار این نامه یک روز پس از رسانه‌ای شدن صدور احکام اخراج برای شماری از دانشجویان شریف صورت گرفت.
امضاکنندگان در این نامه نوشته‌اند که در ماه‌های اخیر دست‌کم ۳۰ پرونده در کمیته انضباطی دانشگاه تشکیل شده و ۱۳ دانشجو با احکام بدوی تعلیق یا اخراج مواجه شده‌اند. به گفته آنان، احکام سه دانشجو نیز در مرحله تجدیدنظر تایید شده است.
نویسندگان نامه تأکید کرده‌اند که آنچه در دانشگاه می‌گذرد، ادامه «روندی نگران‌کننده» است که به دلیل نبود واکنش مؤثر از سوی مدیریت دانشگاه، هر روز ابعاد گسترده‌تری پیدا می‌کند. آنها همچنین نسبت به افزایش سرخوردگی دانشجویان، گسترش بی‌اعتمادی در فضای دانشگاه و آسیب دیدن اعتبار علمی دانشگاه صنعتی شریف هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/76559" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JzGnthAIU_4fa03gP5YmPfFdH0YoZpuxXeb-bQWTEG4AyNieraebXRkt4jqHNsxPrRdYSPRLCKDCW-qg1IA-EKfw6bsRotV7LTl2RiPUf_6RulIwdFsNJgUe4yNQic-Cf2RvTSf2n2DxS8BcLfcSG6nRzFGL_Z-L-W5DL9XXovpyg0J3Mz21ln6esMCors4IcT2h_H6kAd8TbG8Y67pRr6bs3cA74Ctyu3camVIgkKvYhoVFmwf0bCV4a1XjiLa3HAggBpL2I-wLAHwRhsjzxvvuaOEwQ7cRzjJOrgEvPZAB98SKRt_tTPiI_r9EEFVUclXMFObujECC0yHCyxT9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XX2rHcd_TWa0kl4HqTa0xPf3m6t2kLLTh2Road9yRr3EjRQZbWMkVg4_6SjsZHgIZmBFXAySUk9TdSKdrOkB6Uc2eaAisREhbULldwamHn9JutHPlvl1StECznE6UNBCur10pFz9vutawEGZfxXPB4gDPaei2A5pMgWxmD-aEN2mGiBNHTCWFKWJL3hxf37YpVU_A5L5dIz-u1sKaJWk9Yg3rCAmja0VKYdSDZdnTpqkaDpb-v4Bd-sSGmN46-eRG5U9tcq9u9e6VydHDxkcTUhCaZARALxGyCdWRtIs2rMlizQb2GSAwBttKRhhpd-foX6JotbWLNvmjBaKxPDckw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
جواد علیکردی، وکیل دادگستری زندانی، توسط شعبه اول دادگاه انقلاب مشهد به ۱۸ سال حبس، انفصال دائم از حرفه وکالت، دو سال تبعید به سراوان و دو سال منع خروج از کشور محکوم شد. جلسه رسیدگی به اتهامات او در ۲۰ خرداد ۱۴۰۵ برگزار شده بود.
🔸
به گزارش خبرگزاری هرانا، آقای علیکردی از بابت اتهام «اجتماع و تبانی برای اقدام علیه امنیت ملی» به پنج سال حبس و از بابت اتهام «فعالیت تبلیغی برخلاف امنیت ملی» به ۱۳ سال حبس محکوم شده است. پرونده او پیش‌تر در شعبه ۹۰۲ دادسرای مشهد مورد رسیدگی قرار گرفته و پس از صدور کیفرخواست به دادگاه انقلاب ارجاع شده بود.
🔸
جواد علیکردی در ۲۱ آذر ۱۴۰۴ توسط نیروهای امنیتی در مشهد بازداشت شد. او ابتدا به یکی از بازداشتگاه‌های امنیتی منتقل و سپس به زندان وکیل‌آباد مشهد انتقال یافت.
🔸
آقای علیکردی برادر خسرو علیکردی، وکیل دادگستری و مدافع حقوق بشر است که در آذر ۱۴۰۴ به شکل مشکوکی درگذشت. وی پیش‌تر نیز در پرونده‌ای جداگانه با اتهامات سیاسی و امنیتی محکوم شده بود که اجرای بخشی از احکام صادره
علیه او به حالت تعلیق درآمده بود.
@IranRights</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76556" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZLhSnIxRFi6BILHg8GBbLuqSmg8iVPnVOo-h-7VPu1asGD_Gahn54j-IAHAogpGJFVgnDc_jYM1SUFe4OFAmnbbtTZqUJ_kR8AUF_ykqg9c34V0EDawHSe92uVXIMmGsNZEOIpgTuc7fHA9Se-sU8OtUoynhUoUkZKPZ1ngm-2uAfAaIl7iF5u2-LlPmGpIxzGaqczvVOTRpGzfUiMZVuUfjiD0Iyja89iGWjra9BXkVPWZxc0bAsyJ-tRNI36a1wU-vlfqeG69LiQUCxumk-hY-Z9U2un8V_snxHIg6s79J51LyzvNCwksY_lrU7SROFGrTKlgvsxqb7w1l4Q-U2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هیچ‌گونه عوارضی در تنگه هرمز وجود نخواهد داشت مگر به نفع آمریکا
ترجمه ماشین:
در دوره ۶۰ روزه آتش‌بس، در تنگه هرمز
هیچ عوارضی در کار نخواهد بود
،
و پس از پایان دوره ۶۰ روزه نیز
هیچ عوارضی پرداخت نخواهد شد
؛
مگر آن‌که، در صورت تکمیل نشدن توافق، این عوارض
از سوی ایالات متحده و به نفع آمریکا
وضع شود؛
آن هم بابت خدماتی که این کشور به عنوان «فرشته نگهبان» کشورهای خاورمیانه ارائه داده، برای جبران هزینه‌های گذشته، حال و آینده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76555" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJL266tZ6YJ0EYY37P3ym_td5cC46mbEYsUMkKzw_aQpVf0ZXmZKUE9f46YWqPz_mWF9WDq2UOWdnoAzF8PjOBjjMy-SKHuItbytZa2PrTejVd-ufvSx97j0OcFZmt7JFcdmJmSp8zAoDUms_uo8Vh73QS8rGBhCj9i5_UiOjQuN3k6J2qcr6WDRo_G5S_LcoOZ3ZUmepefoudwCPPaXsEb3VHu5Tt8b-uHYW6IUX4uPezxwGBgWoaxkxV7umfFojEOt90s1Gll92hcGN1HyGv1qcnKKA3uvlvCuJRU-JQoTSA74xn9Yw-KMIyMBrAJzwllZvDmwVozdXmJ5Qnz93uLdY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJL266tZ6YJ0EYY37P3ym_td5cC46mbEYsUMkKzw_aQpVf0ZXmZKUE9f46YWqPz_mWF9WDq2UOWdnoAzF8PjOBjjMy-SKHuItbytZa2PrTejVd-ufvSx97j0OcFZmt7JFcdmJmSp8zAoDUms_uo8Vh73QS8rGBhCj9i5_UiOjQuN3k6J2qcr6WDRo_G5S_LcoOZ3ZUmepefoudwCPPaXsEb3VHu5Tt8b-uHYW6IUX4uPezxwGBgWoaxkxV7umfFojEOt90s1Gll92hcGN1HyGv1qcnKKA3uvlvCuJRU-JQoTSA74xn9Yw-KMIyMBrAJzwllZvDmwVozdXmJ5Qnz93uLdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبویان: مجتبی خامنه‌ای نامه داده بود که چرا شروط من رو در مذاکره رعایت نکردید؟
07:20
صدا و سیما: افشای مکاتبات مجتبی خامنه‌ای از سوی نبویان در شبکه خبر پیگیرد قضایی دارد
صداوسیمای جمهوری اسلامی ایران اظهارات محمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس، در شبکه خبر پیرامون مذاکرات پیش رو بین ایران و آمریکا را «مصداق تخلف قانونی و مستوجب پیگرد قضایی» عنوان و اعلام کرد «مدیرکل مربوطهٔ این شبکه استعفا کرده است».
محمود نبویان، که به جناح تندرو موسوم به «پایداری» تعلق دارد، روز شنبه ۳۰ خرداد با خواندن بخش‌هایی از متن‌هایی که گفت مکاتبات مجتبی خامنه‌ای با هیئت مذاکره‌کننده است، مدعی شد رهبر جمهوری اسلامی در مراحل مختلف با روند مذاکرات و بندهای متن‌های گوناگون مرتبط با مذاکرات مخالف بوده است.
این گفت‌وگو پیش از آن‌که نبویان به متن نهایی تفاهم‌نامه برسد، قطع شد و موجی از واکنش‌ها را در میان دیگر چهره‌ها و فعالان رسانه‌ای جمهوری اسلامی در پی داشت.
صداوسیما در بیانیهٔ خود اعلام کرد نبویان در اظهاراتش «اشارهٔ ناقص و مخدوش به برخی اسناد دارای طبقه‌بندی» داشته و سعید آجورلو، عضو تیم رسانه‌ای هیئت مذاکره‌کننده و از چهره‌های نزدیک محمدباقر قالیباف، نیز او را به «تحریف عمدی متون» با هدف «فرار از پاسخگویی درباره ادعاهای نادرست قبلی» متهم کرد.
محمود نبویان، ۲۳ خرداد ماه، در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا، در یک برنامهٔ زنده در یک خبرگزاری نزدیک به سپاه، متنی را که مدعی بود تفاهم‌نامهٔ ایران و آمریکا است، روخوانی و از برخی بندهای آن به‌شدت انتقاد کرده بود.
نبویان یکی از اعضای گروهی بود که پس از اعلام آتش‌بس جنگ ۴۰ روزه، همراه هیئت مذاکره‌کنندهٔ با آمریکا به اسلام‌آباد رفته بود.
مجتبی خامنه‌ای، که پس از اعلام رهبری هنوز هیچ صدا و تصویری از او منتشر نشده، پس از امضای تفاهم‌نامه توسط رؤسای جمهور ایران و آمریکا در پیامی مکتوب اعلام کرد «نظر دیگری» داشته اما «با تعهدی» که پزشکیان به او داده، مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا گذاشته است.
@
VahidHeadline
حمید رسایی با انتشار ویدیوی بالا نوشت:
نبویان در آنتن زنده شبکه خبر، در حال تشریح جزئیات نامه‌های رد و بدل‌شده میان رهبر معظم انقلاب و شورای عالی امنیت ملی بود که پخش برنامه به بهانه میان‌برنامه به صورت کامل متوقف شد!
ما که از یادداشت‌های آن امام شهید در این باره اطلاع پیدا نکردیم ولی گوشه‌ای از یادداشت‌های امام حاضر توسط آقای نبویان در حال پخش از سیما بود مانع آن شدند!
صدا و سیما:
🔹
روابط عمومی معاونت سیاسی صداوسیما: به استحضار مخاطبان محترم شبکه خبر می‌رساند اظهارات یک نماینده مجلس دعوت‌شده به برنامه امروز زنده این شبکه و اشاره ناقص و مخدوش وی به برخی اسناد دارای طبقه‌بندی و مکاتبات مسئولان عالی کشور، مصداق تخلف قانونی و مستوجب پیگرد قضایی است و سازمان صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار می‌دهد.
🔹
شبکه خبر ضمن ابراز تاسف بابت بی‌توجهی مهمان مذکور به قواعد اخلاقی و الزامات آنتن زنده، به اطلاع می‌رساند مدیریت این شبکه ضمن پذیرش استعفای مدیرکل مربوطه، برخوردهای انضباطی لازم را به دلیل بی‌توجهی به الزامات برنامه‌های زنده و سهل‌انگاری در مدیریت حرفه‌ای به عمل خواهد آورد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76554" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BaVEL-SitB_QhZQWshYzWravzWPsQh3YWuIALLweH0l0Rjm47-FGUx_gM9qs1oABlnHC9G_oA-mDs-6Rm2Raz5kGG5vphiHbCLHEod00NN4LvDW8Rmq6OaJoeVdhOXxf56RckOWI43AWhU8XHb68022hcyDbe6st0btmfqplcHb6SsYkHMrC4Wq9wh-gQKs6lk9sKUwuie1IoqvE-OegdsnCUpWbt7iEkL32HustoTuphQruA7L9TxeE1eBZ6zu6jxvrtAXNPAK4Qxph9PMZkl5F192XJCImsXlqsE3y79MOd_0vp6fu-IgHCKT4M-JQv2O1g8Y-H2sAIucdWHNB7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GVRiq6amf03_Sxz1QULPdNN38vvGNQzQ5_5OEf7TCVa5eiRqQqILoDcSahx2xBldxQiS-ufPs94jwUSPkJlqKQgPdM_7GFAexIIcPDVpmZEScT_1Uo0KU6638c5CYQA6z4LEm-LvHhVLSJTlnxAT0o-PNFOmoiPCOP7uWp6B3kz7xTZccK1A31aU7vHL3ZNhN9VB_dXkW00p5wEMLxI_p7yL_4ZIMIhkdf0CbeYtRnadGmjQpSnEpKINfMsOONC_I4CrqYTDvMydnUXJf7u06ybYmxELr8bWkmMA6C0Nm1DTydzD2PJsB_Z9iSLXmJ58Vl9FVpdRUf9WZ_KQmoC6gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ در تروث سوشال نوشت: محبوبیت ملونی در ایتالیا به شدت کاهش یافته، شاید به این دلیل که او و ناتو در جریان ماموریت جلوگیری از دستیابی ایران به سلاح هسته‌ای، به ایالات متحده پشت کردند.
ایتالیا حتی اجازه استفاده از باندهای پروازی خود را به ما نداد که یک مانع لوجستیکی بزرگ بود؛ آن هم در حالی که آمریکا سالانه صدها میلیارد دلار برای محافظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند.
رئیس‌جمهوری آمریکا در پایان با لحنی تحقیرآمیز تاکید کرد: اکنون که ایالات متحده ایران را از نظر نظامی شکست داده، او می‌خواهد برای بالا بردن آمار محبوبیتش دوباره با ما رفیق شود؛ اما نه، ممنون!
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، با انتشار بیانیه‌ای تند در صفحه اینستاگرام خود، به هجمه‌های اخیر دونالد ترامپ پاسخ داد و حملات کلامی رئیس‌جمهوری آمریکا را «بی‌دلیل و بی‌معنی» خواند.
ملونی در این پیام خطاب به ترامپ نوشت: «محبوبیت من به هیچ‌وجه به رابطه با شما بستگی ندارد و دوستی با شما نیز کمکی به آن نکرده است. محبوبیت من حاصل توانایی‌ام در دفاع از منافع ملی ایتالیاست؛ یعنی همان کاری که همواره انجام داده‌ام.»
نخست‌وزیر ایتالیا همچنین با دفاع از تصمیم خود در جریان جنگ اخیر و عدم اجازه به آمریکا برای استفاده از پایگاه‌های نظامی این کشور، افزود: «نحوه استفاده از پایگاه‌های نظامی آمریکا در خاک ما، تابع توافق‌نامه‌های متقابلی است که ما همیشه به آن‌ها احترام گذاشته‌ایم. تا زمانی که من نخست‌وزیر هستم، این توافقات نباید نقض شوند؛ چرا که ایتالیا یک کشور مستقل و دارای حق حاکمیت باقی می‌ماند.»
ملونی در پایان نوشت: «در هر صورت، میزان محبوبیت من اصلا به شما مربوط نیست. پیشنهاد می‌کنم شما روی محبوبیت خودتان تمرکز کنید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76552" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XVpPssYmtuKU_GE-SGJmpt_aeuI0OEi2NXethoes51mg3LmfysM7zh9PZsh3kEaMESt2ga0Waff-sTfHdxgWEE-AwCovM6zBPQuDzvfSFGq4PxgOjPPBz35aecCmT9pa3bQqV_7NE5g4CopYKmcHPryn4c_pfoWBU-9wfups1ZKrwkVU6V5NUwsrYQ6kSiASFI2CgDJSYqfmSevebMcQ5kZj9IwvOoe2y5fW1YyDSosKnzQDP_X4DFWxNFr5Bit1roRXiNLbtVXKhBMLQ2vgZBIV-163BPaTORYiL95TSXY7W2r97g-RMOsA59Y6iIhosjHLu28k6IGJtT-ZE9BZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که هیات مذاکره‌کننده جمهوری اسلامی به ریاست محمدباقر قالیباف و با حضور عباس عراقچی، عازم سوئیس شده است.
بر اساس این گزارش، عبدالناصر همتی، رییس کل بانک مرکزی و علی باقری کنی، معاون بین‌الملل دبیرخانه شورای عالی امنیت ملی نیز در این سفر حضور خواهند داشت.
همچنین کاظم غریب‌آبادی، معاون و اسماعیل بقائی، سخنگوری وزارت خارجه و حمید بورد، معاون وزیر نفت نیز این افراد را همراهی می‌کنند.
پیش‌تر وزارت خارجه پاستان اعلام کرد که مذاکرات فنی میان جمهوری اسلامی و آمریکا، یکشنبه در سوئیس آغاز خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76551" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VKSupl3iFAYx5eh8PloUn9fjejHgq-67Jvejnc-dGUWTEmpBAYkRvdSrhN0FKYL048PvloDTUqgGEjYifnsxf4whqQWXvhCvayNAfoxzB6LzzVwx_Ca_UuSAnvAbt7DtmztM3beB9Wx3QgytUDimvkh1vUE-88MOqrceNwhai3gOg5Ik2lTVDrv74LEA117pm4dLQCn3tSLY5uac7Lnr8-41NHAOXExgs_JMdI5cHWq-rx4yHZM7W2G_3Uzr4QgGOKa4xkuymyzdrDFMUBw-ziHCVyNtqOBb4z0duxhcDbH7hTcSSisUjW3LUzalwX9AoGEDqCSEor5AZgJzDntPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی مرکزی ایالات متحده،
ترجمه ماشین:
عبور کشتی‌های تجاری از تنگه باز هرمز
تامپا، فلوریدا — تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت؛ همزمان نیروهای آمریکایی به عملیات خود در منطقه کلی ادامه دادند تا از آزادی کشتیرانی حمایت کنند.
امروز عبور امن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری از آن عبور کردند؛ کشتی‌هایی که حجم زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل کردند.
مرکز مشترک اطلاعات دریایی این هفته اطلاعیه‌ای صادر کرد و در آن عبور امن همه کشتی‌ها را در یک مسیر تعیین‌شده تأیید کرد؛ مسیری که از ادعاهای خودسرانه درباره الزامات یا هرگونه مانع، آزاد است. جزئیات مربوط به عبور امن را می‌توان در اینجا دید:
ukmto.org
نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اجرا و به‌طور کامل برقرار و لازم‌الاجرا باقی می‌ماند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76550" target="_blank">📅 18:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=DWs6ryKwijo4zROOo0-YFIpbiwbbrMo0aTo5EEraduxUrXP-vksB1DG-aKJIQmegELsPCu82yw_ecNbFgo7T-OvxhDkSqEnUw-yDYcJ7ugGxtr-60iBEzMHU_uM2ZyGAJH7xz5u1HhZZaQdHENt3JuQsSzWCua8tuvzOANWVmuW6gZX5MYWo_Du2PhCPbPYsbEXJ4TKUNvfDotvO9BhFxGsjkYGkD88yrr2SV_spVvkenQmnHla-K3xzljb8bQ_yTO5b1RXp0J2ymb0yzlP3lYwhy4k6ItdLz_xWnmCWSlrHTNZdPD7xtVLmG5sJF8A7978a_QwwuZpGxV-DILcV2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=DWs6ryKwijo4zROOo0-YFIpbiwbbrMo0aTo5EEraduxUrXP-vksB1DG-aKJIQmegELsPCu82yw_ecNbFgo7T-OvxhDkSqEnUw-yDYcJ7ugGxtr-60iBEzMHU_uM2ZyGAJH7xz5u1HhZZaQdHENt3JuQsSzWCua8tuvzOANWVmuW6gZX5MYWo_Du2PhCPbPYsbEXJ4TKUNvfDotvO9BhFxGsjkYGkD88yrr2SV_spVvkenQmnHla-K3xzljb8bQ_yTO5b1RXp0J2ymb0yzlP3lYwhy4k6ItdLz_xWnmCWSlrHTNZdPD7xtVLmG5sJF8A7978a_QwwuZpGxV-DILcV2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی پربازدید شده که مادر مانی صفرپور، جوان کشته‌شده در اعتراضات دی‌ماه، را در حال سوگواری برای فرزندش در کنار یک دستۀ عزاداری نشان می‌دهد.
عکس پسرش را بالای دست گرفته و می‌گوید «پسرم، پسرم».
مانی صفر‌پور، جوان ۱۸ سالۀ لاهیجانی، ۱۸ دی‌ماه ۱۴۰۴ با شلیک نیروهای حکومتی در محلۀ سلسبیل تهران کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76548" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76547">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BXVs6dg9WOITJlU6e_KXWktyfnwR-ZiiZQTC8JVqt-DozjCBGSWp_hw1h3IUm7U8gRw2Pj21-OpMFsv5uAq80HdmR3TxfBLF9dR5Z9dHxQbJ1i3r-nSPA72RicRNnqIlv860iGWYDRevx8G6DOHN0jdINch8hF7mmjqHjkF6-QHEHbvq8G7kSThZHt-ffl6Vjlu3IQZl6_b7ulFhRoV9vHr5gqi6KebATgu01SoM1GmW0BAOfQUGIGLntcRnV1FuVJUT4eYaDUcYpwfKw0HLR1G5E84lziuSdimel7DSI1pzAIHpVgVPdXHWbHZyoHV5oKZtFBxeEa5h9NzxEZQiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد تنگه هرمز در واکنش به «نقض تعهدات امریکا در اجرای آتش‌بس» و «حملات اسرائیل در لبنان»، به روی همه شناورها بسته شد.
نیروی دریایی سپاه همچنین از شناورها خواست به تنگه هرمز نزدیک نشوند و هشدار داد در غیر این صورت، امنیت آن‌ها به خطر خواهد افتاد.
قرارگاه مرکزی خاتم‌الانبیا، واحدی از سپاه پاسداران هم اعلام کرد تنگه هرمز به‌دلیل «بدعهدی و پیمان‌شکنی» امریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه، به روی تردد کشتی‌ها بسته شده است.
قرارگاه مرکزی خاتم‌الانبیا روز شنبه اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.
خبرگزاری فارس، وابسته به سپاه پاسداران به نقل از یک منبع نظامی در نیروی دریایی سپاه، عصر شنبه اعلام کرد که تنگه هرمز از دقایقی پیش به‌طور کامل بسته شده است.
حملات اسرائیل به جنوب لبنان در روز شنبه دست‌کم ۱۰ کشته بر جا گذاشته است. اسرائیل اعلام کرد این حملات در واکنش به پرتاب گلوله‌هایی از سوی حزب‌الله، گروه مورد حمایت جمهوری اسلامی، انجام شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76547" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aZiUZ7yCUTVjLmOYyz5gW614mDKcW5qzSdH9Gypdsy89bF1PcGTkhBiUWZt8TIdmDH09DPuaAA57L9fQq2HCAjqVqtxx-F4322JYTXXOGV6EbNJxQ9ta_bxQEpuWSsLQxszR8Hg51xJ-u7IZNh6gUno8Cr9nqEwZf7PhvrSz3uj8z0W3T2h_Ve0GlR3aEf1udR49SIO_PQYgoDnnxOwZcbd2XTlxlC-bpg1y4iPP1zC7jZgJxDGWpQrntM_mokOAfEAoGX875ipcj9Pd7rZJKB0ZwcQJlwtBFix7rpMoCjbvoDQsUWfayePp0fn5w_sz47SqMDXTXLiCR_kgxhgbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، روز شنبه ۳۰ خرداد در گفتگو با فاکس‌نیوز اعلام کرد که استیو ویتکاف، فرستاده ویژه ترامپ و جرد کوشنر، داماد او، «چند ساعتی است» که در سوئیس حضور دارند و مشغول بررسی «برخی از ابعاد فنی این مذاکرات» با ایران هستند. به گفته ونس، کوشنر و ویتکاف در گزارش‌های خود تاکید کرده‌اند که «امور به خوبی پیش می‌رود.»
ونس همچنین از احتمال ورود میانجی‌های قطری و پاکستانی به سوئیس برای پیوستن به این گفتگوها خبر داد و افزود: «قطری‌ها و پاکستانی‌ها می‌خواهند مطمئن شوند که ما این کار را به شیوه درست انجام می‌دهیم، بنابراین من تلاش می‌کنم به این روند احترام بگذارم.»
معاون ترامپ که سفر خود به سوئیس را در اواخر پنج‌شنبه شب به تعویق انداخته بود، بار دیگر تاکید کرد که انتظار دارد طی دو روز آینده عازم این کشور شود. او با این حال خاطرنشان کرد که هماهنگی‌های این سفر «همواره یک رقص هماهنگی ظریف دیپلماتیک است.» این مذاکرات که پیش‌تر قرار بود روز جمعه برگزار شود، پس از وقفه‌ای کوتاه دوباره در آستانه ازسرگیری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/76546" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQyw0J9OqRIX1pHT_ax3sUTCh8o8L479-4VFEeGXv7Ez4A_8Gav6v60DsHefmF_UMkzCbmbcRvy38L-90pnxrOgSwUNsdRkJVg8DmlLDwMZdUOBoZuHXqhCKKfDQd-aoChmUJ_3C-wtEk9hMGuPIUWOPQh_Q_ifIvDD5TVbj3sKCDLqTxgDkYpJz0slaEjIGjbg67JauTdBVXuwLOnnS-edlDre-KEjne3SU_C7Cy2WVa3A8cZDiXNylOSe1QA76yMwCqS8XVN9A4PzHOQxzhC43A0JriKzMqmOtRP4KrLzYpbe_UEsmru1tPPjUjZ52PFWQVOhGf71DuilX_0aSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«طاها نظری» معترض ۱۸ساله که پیشتر به‌دلیل حضور در اعتراضات ۱۸ و ۱۹دی۱۴۰۴ بازداشت شده بود، پس از  تشکیل جلسه رسیدگی به پرونده، به ۵سال حبس تعزیری محکوم شده است.
ماموران اطلاعات شاهرود، در فروردین ۱۴۰۵، طاها نظری را شناسایی و به صورت تلفنی احضار کردند. بعد از مراجعه به محل، این جوان ۱۸ساله به‌صورت موقت بازداشت و تحت فشار برای پذیرش اتهاماتی نظیر «ارتباط با تلویزیون‌های فارسی‌زبان و فیلم‌برداری از اعتراضات» به او نسبت داده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76545" target="_blank">📅 17:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ETXXbaXAOUMTDXK9DDIS_SgjBIGSkPOT9dzwXlzKFFp8C5YpnbNfVKNBOYTHvQYY5ghL4XeWM8GEJwcq8CoFdq5KfWhhtAgakkBdhBcoRvMe7WV9otDNrmOSHymbuFyRa3LKh5Mlcm5i-R7S6No5EOlV4DH5-uZgC-T7s89N2D8BXVUscQPOqf_vFc3seXNa37SDjQJCjRFSLkzmGcajJBkxDXf15StwZA_zJEHr2A9xVMcAVWcTQNvSuLWSof29YvspWxs2Ga6VbIVAAcgrueqEqr8pex-PlBicVSRGUR20RvgKMh0KgdOv18BcHjJk_tfEbhv0C5Q8Q6D_ULMgQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d0kjlwPLduWHbP2N3J5v6MeEd1XhxoGylXc1TCyV1EpDQF4Q7ynEGgUW8F-Q-7ibBT1yDh1KN7sBxP_AA6HNavAaBoknK_20oensyQpnh4qd2COjw3TZ4DAOoV7bKhxSkCAQBKK8S4XEhTkCTT8vHMNFuIWUWfR-wLwfSBFXjip7SC1c2YLFq68Q8JP26TmpGUEbkgnNYkFDZj138xOYmyMwgLgmxgI8fGlo-81E3A--l8wdbvxFQiGH_r_kjQ138F-jAW7kqGnF6NhH__R-YpLpYtKI1otHOWU15j7o6AuCxPCRumcqnvhfmC7puU6TSWAiOeOaIoqYVjbx1-1W9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت دلار و دیگر ارزهای خارجی که در پی نتیجه موقت مذاکرات ایران و آمریکا کاهش یافته بود بار دیگر افزایشی شد.
روز شنبه، ۳۰ خردادماه، قیمت دلار آمریکا در بازار به ۱۶۲ هزار و ۵۰۰ تومان رسید. قیمت یک یوروی اروپا نیز در این روز به ۱۸۶ هزار و ۴۰۰ تومان رسید.
این در حالی است که در طی روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسیده و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شده بود.
روزنامه هم‌میهن روز شنبه قیمت سکه امامی را در بازار طلای ایران ۱۶۹ میلیون تومان گزارش کرد.
از زمان اعلام تفاهم‌نامه ایران و آمریکا در تلاش برای پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران شاهد کاهش قابل توجهی بود.
@
VahidHeadline
حسین صمصامی، عضو کمیسیون اقتصادی مجلس شورای اسلامی، در گفت‌وگو با سایت خبری تابناک افشا کرد که در هفت سال گذشته بیش از ۱۳۰ میلیارد دلار ارز حاصل از صادرات به کشور بازنگشته است.
این در حالی است که حکومت برای بازگرداندن ۲۴ میلیارد دلار دارایی مسدودشده کشور وارد چانه‌زنی فراوان با دولت ایالات متحده شده است، امری که نشان می‌دهد تا چه حد به این پول نیاز دارد.
در این میان بیشترین میزان عدم بازگشت ارز صادرات مربوط به سال ۱۴۰۴ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76543" target="_blank">📅 17:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iIGLEp26H9h8P-OEX9nB3ZQ58xf5qFb45HlLwCeGpqEUgrYXcMH6YAfugtx5lpwRHClg-qrqpdpdXKjTxC4WowW0TOAwJnZwVhB241XHIsZfYqw8jVOlTDl9Opl2gAPrvQnUvxB7R_maFtT3bCn0lksYKh9vgu15o-P7vM3hXWn1kPMg-zBO5eFTaCr8q1pM5Z1NaFog370Ux0Cyax2VWDAmT1CKQAAnYcAZ2mgjRnOuMDZpeBot-s9RdNo3o2K5a8TRLm0LD3VDikerh_lTRpckT2Br_syFWN0Z07vFwB-XgS4XcoSJVIS_n8T2L2bWGRm0fzDPly-sm1mrw4W5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=RhgAaZJ4Ac-VyqEvJxyn2vHAX51NXbDv8x1065oiKEWKhzXidCMMxT1f5tLwV2g-61IBrFtRo30SMJit_OHfPhMBTlSztUq9wJ7DOlDqAbjeBD2V6xeZd_H1XIWh0xYmOmJbbBZ1mq753b5rPMEfHcspQwlO6cu_HdgE1Yh2rUwttTfGqKDs1sBgb_2rpcur0xat5yBrlArB0IQZbD2OX6ELSatLQ2oSQCFdL6QG5lCFdYy2gS9Zk7D9TVZKC4Pvplt-khT5R3KoykQD_T2GBhaga8yPZKfsW0OQUuALg9hEk9yhj4bARmukMW3D8ssEmWDb1YxZi6bzIOWMVoUwzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=RhgAaZJ4Ac-VyqEvJxyn2vHAX51NXbDv8x1065oiKEWKhzXidCMMxT1f5tLwV2g-61IBrFtRo30SMJit_OHfPhMBTlSztUq9wJ7DOlDqAbjeBD2V6xeZd_H1XIWh0xYmOmJbbBZ1mq753b5rPMEfHcspQwlO6cu_HdgE1Yh2rUwttTfGqKDs1sBgb_2rpcur0xat5yBrlArB0IQZbD2OX6ELSatLQ2oSQCFdL6QG5lCFdYy2gS9Zk7D9TVZKC4Pvplt-khT5R3KoykQD_T2GBhaga8yPZKfsW0OQUuALg9hEk9yhj4bARmukMW3D8ssEmWDb1YxZi6bzIOWMVoUwzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که هاجر نادری، مادر متین پرویزی، در صفحۀ شخصی خود منتشر کرده است او را در کنار آرامگاه پسرش نشان می‌دهد که می‌گوید «من به پسرم فقط یاحسین و تشنگی را یاد ندادم، به او یاد دادم که جلوی حرف زور بایستد»
خانم نادری در ادامه با شرح کشته شدن فرزندش در اعتراضات ۱۸ دی‌ماه می‌گوید امسال محرم برای فرزندان میهن که «ناجوانمردانه کشته شدند» عزاداری خواهد کرد و ادامه می‌دهد که «می‌دانم امام حسین هم برای این جوانان عزاداری خواهد کرد»
متین پرویزی ۱۸ دی‌ماه سال گذشته در سبزه‌میدان زنجان با شلیک گلوله جنگی نیروهای حکومتی به سرش کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76541" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXOPFL-sQ3dsH_uWcFkUiA6o64QpABlW2ILXuCVNZ8OOqq9tRgbLoDxjW9RXyhnJSwsyIuPrdowND2dfOzIgl86xeg85p7VqGt7Ln9n49RXIbzRDf3xgeYJ2YSIbpGplRqzD87zUmktPEvK_CtGi_zKH-k5XruDzO4J-kFqPLIwmx8cycRbfiZKQPUAMCJW9_wk68vftQ7xENvoq-gzGG7IoM_R2k3W06XCGdLo4Hf_DoBLYYOEkU00gmGVkhSBgj5Bkhyw4skVmHWv8WtlxDrN6hYxsmHBAplVRQL7-DcCQYoWIIzZ2AXheX8VS7w2z38fxHyFk9s6ih1IUOWpMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، صبح امروز وارد مشهد شد.
ایرنا به نقل از منابع خبری در استانداری خراسان رضوی گفته است که او سپس برای گفتگو با مقامات عازم تهران خواهد شد.
بر اساس گزارش‌ها وزیر کشور پاکستان قرار است در این سفر در مورد از سرگیری مذاکرات مستقیم بین آمریکا و ایران در سوئیس، با مقامات ایران گفتگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76540" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I60CSKJWBAdIcxmhKHdC8uxsBwITeOte2OEVbAtNwVJUPunkVy1XyULDQ1ofjv4z4sWZUQbXPLUavo-a4mkmgjG06nfRkUzV3dOEF0DIm6Z-mPFxAf3w8UBFTtIzO9HbZ9S00EvgMbV0doo5cMYiySGg9OpbsjIbChPBFOM2qT-NVt3apH6uQQjBpDWkLPXnb2ddewGDQYaIqEOwGnwOGYQEXM6piKvAjL7A9Q5D5p89hNCMFo56NyQQgZxNFML4eIBE5MqCG8QAa7rxesaUq2f-91ogzlQnJMSs3uQN0mFYBHaRas8xyI1dU0V38pBEOFAubjj7tkDqB0hUBkV_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز اطلاع‌رسانی پلیس استان لرستان از پلمب یک واحد صنفی و معرفی فرد متخلف به مرجع قضایی خبر داده و اعلام کرده است این اقدام پس از آن صورت گرفته که به گفته این نهاد، واحد مذکور «ضمن عدم رعایت قوانین و مقررات، اقدام به هنجارشکنی» کرده بود.
این در حالی است که تنها سه روز پیش نیز مرکز اطلاع‌رسانی پلیس لرستان از پلمپ پنج کافه‌رستوران و سفره‌خانه سنتی در سطح استان خبر داده بود. در آن گزارش، دلیل برخورد با این اماکن، اجرای طرح موسوم به «ارتقای امنیت اخلاقی و اجتماعی» و آنچه «هنجارشکنی» عنوان شده، اعلام شده بود.
در هفته‌های اخیر و هم‌زمان با فروکش کردن فضای امنیتی ناشی از تنش‌های بیرونی، گزارش‌هایی از افزایش تمرکز نهادهای انتظامی و قضایی بر حوزه‌های مرتبط با سبک زندگی شهروندان منتشر شده است؛ روندی که به نظر می‌رسد بار دیگر کسب‌وکارهایی مانند کافه‌ها، رستوران‌ها، فضاهای موسیقی، پوشش و نوع تعاملات اجتماعی را هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/76539" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=kfPFCMfKZtN2XKrTW9IP-jvhV5cMRuJhGahUtwnYEj7TdOnUuueTOyBPIVNcheM8Qf3JhFMG48ohYte-EbHzndlLJxRnHauqbN4EIYbIlX6wQB8ktLACDXffC5L4o6JNlMwW2o2bisaQ77OPNk8bRO0SbxFE6x3jYDCSQk_JFz2Y8875aTvaszBHMywv8Ng5CERKI0DcEN7rSOd3EBq9Kai5Z8SebgW8X6TvoAHaMFbMS1NnEfX5fdOxWqRGg-yAd4Vbm-rksp3LvQAO_-bU6C-Wg-lc9_Lq35kfsdkVlFgbaVkwd5zmToOejUctJtHPFLt-DAPuTxE_qO0GmP1pqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=kfPFCMfKZtN2XKrTW9IP-jvhV5cMRuJhGahUtwnYEj7TdOnUuueTOyBPIVNcheM8Qf3JhFMG48ohYte-EbHzndlLJxRnHauqbN4EIYbIlX6wQB8ktLACDXffC5L4o6JNlMwW2o2bisaQ77OPNk8bRO0SbxFE6x3jYDCSQk_JFz2Y8875aTvaszBHMywv8Ng5CERKI0DcEN7rSOd3EBq9Kai5Z8SebgW8X6TvoAHaMFbMS1NnEfX5fdOxWqRGg-yAd4Vbm-rksp3LvQAO_-bU6C-Wg-lc9_Lq35kfsdkVlFgbaVkwd5zmToOejUctJtHPFLt-DAPuTxE_qO0GmP1pqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع‌های اعتراضی زنان به فعالیت‌های معدنی حوالی دو روستا در استان‌های کرمان و سیستان‌وبلوچستان با حضور نیروی انتظامی به خشونت کشیده شد.
بر اساس گزارش‌ها زنان روستای پشموکی از توابع فاریاب استان کرمان روز ۲۷ خرداد در ادامه اعتراضات مردمی نسبت به نحوه واگذاری و بهره‌برداری از معدن کرومیت پشموکی تجمع کرده بودند.
گفته شده که نیروی انتظامی علاوه بر ضرب‌وشتم معترضان، شماری از آن‌ها را بازداشت کرد.
هم‌چنین منابع بلوچ گزارش داده‌اند که زنان روستای سرسیاه از توابع تفتان استان سیستان‌وبلوچستان هم روز ۲۶ خرداد در اعتراض به گسترش فعالیت‌های معدن طلای تفتان و پیامدهای آن بر زندگی مردم منطقه تجمع کرده بودند.
در ویدئویی که منتشر شده شنیده می‌شود که مأموران نیروی انتظامی با خشونت، تهدید، توهین و واژه‌های تحقیرآمیز با این زنان برخورد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76537" target="_blank">📅 17:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lSgaiZpXAyFtJXEcYxhn4ijzRHUWatD9El2KwFCwK5bza5vsAzKb_HQpWBTfJBkfEDStG0SarchWqIv9MUFQHb9IL9Bo8bbGEZbdRH-adJlKk2gm_oy4gbOxVCLnI_e7GoLUyBL0OiBzNew0WwH7p250lMNkI_x3ThgrPpDd28qrbiIsLFea41SiYyH05T70IQHza71eE-erZFoeV0CqIpd5wIE_ajMVK5-zz3PZVAMIsWmYpVxHvUfZZ6n0ag_-55547p_2CegRMaotwK5cu3wXngp3qQXREEZnQ99wmcSaZiHJ294lovfmgXjMohY4mWnnCcmmTPtvJBuOT3uRSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kXJtoQQoyWqKTDdUupzK-GCSHE-lVptNxse7GI7gJzox-rphKl9s7u9yCB2SSi0YBApf-cDzelbHZ1yaMhv60XbR1m_6m_eqZQmza6RzPJInS-S_HMrIIufVqZiEHueoxHAnJZ6M5CR8kILtU05eJX-TM9YSVyi_soFspuI6wTR-jVw2IO6eXnh-E08IcSV3kAh0rIEXRFaOF64NEW34swUIQq6uEhEKmg0CVyPcjkDVS782WyWhTBwUYTIQBaHEWYbP_Ncrx2KLrVvFEOqjNDIrZ6DusGYrdGcxkTxtOzzOG-yCY5VqtP3ZXVfFt_bLb38IcnHHIKr6eaY4kocMhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: استیو ویتکاف، فرستاده کاخ سفید، در حال سفر به سوئیس است، جایی که انتظار می‌رود دور اول مذاکرات با ایران در مورد توافق هسته‌ای احتمالی برگزار شود.
به نوشته اکسیوس، قرار بود مذاکرات جمعه ۲۹ خرداد آغاز شود، اما به دلیل درگیری بین اسرائیل و حزب‌الله در لبنان به تعویق افتاد.
@
VahidOOnLine
خبرنگار اکسیوس به نقل از یک منبع آگاه، روز شنبه اعلام کرد: «عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، در حال برنامه‌ریزی برای سفر به سوئیس در روز شنبه است.هرچند این برنامه همچون گذشته ممکن است تغییر کند.»
این خبرنگار به نقل از منبعی در یکی از کشورهای میانجی فاش کرد که عراقچی روز جمعه به چند تن از همتایان خود گفته است: «موضوع آتش‌بس در لبنان برای ایران یک مسئله حیاتی است و حکم برد یا باخت (تعیین‌کننده سرنوشت) را برای مذاکرات ایران و آمریکا دارد.»
خبرنگار اکسیوس همچنین به نقل از یک منبع دوم از میان کشورهای واسط افزود: «ایرانی‌ها صراحتا تأکید کرده‌اند که می‌خواهند پیش از سفر به سوئیس، شاهد برقراری و تثبیت کامل آتش‌بس باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76535" target="_blank">📅 04:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=H79SFm5RGEGkMR5FP-3gO4L0e8JFEMjfNmmnkyAvjn4v9h-UZpjMDsh1xCDOo7gAQvk73ymbDuXqh1YFhwI4QFtRI5itAD-HscjL6AQLHO97xE2N_yO65h-YlfphVAS5b_4xaYWfMmAxcILtL4nCFDywH-GN2EwAQ1J1WDd0L14JFiNKh5R7e8RFqrfdbOnbrNOSZURTcm5Lx0eF9DtCx-Y2mGdL1G8nzCJpXI2-KCvT9xDhodJxayYMmPBRZanLls_dE3vGPfChAJcX6xgPDgGWtQ4DsYX-LguwilKDa_3HJycc_OJi4Eqv2OKovFM5H2zpaPjqChV8jUe0iID_WA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=H79SFm5RGEGkMR5FP-3gO4L0e8JFEMjfNmmnkyAvjn4v9h-UZpjMDsh1xCDOo7gAQvk73ymbDuXqh1YFhwI4QFtRI5itAD-HscjL6AQLHO97xE2N_yO65h-YlfphVAS5b_4xaYWfMmAxcILtL4nCFDywH-GN2EwAQ1J1WDd0L14JFiNKh5R7e8RFqrfdbOnbrNOSZURTcm5Lx0eF9DtCx-Y2mGdL1G8nzCJpXI2-KCvT9xDhodJxayYMmPBRZanLls_dE3vGPfChAJcX6xgPDgGWtQ4DsYX-LguwilKDa_3HJycc_OJi4Eqv2OKovFM5H2zpaPjqChV8jUe0iID_WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بخش مربوط به ایران از مصاحبه امروز ترامپ
متن کامل این بخش‌ها:
https://telegra.ph/trump-06-19
بعضی از جملات همان متن:
ترامپ: و من آیت‌الله را کشتم. یک مقام سپاه هم بود. و متأسفانه به آیت‌الله دیگر هم آسیب جدی زدم. به شما بگویم، من او را ملاقات نکردم، با او صحبت نکردم، اما دیگران درباره‌اش حرف می‌زدند. او شجاعت خاصی دارد، چون به‌شدت آسیب دیده است.
با وجود همه این‌ها، نمی‌توانید بگویید بی‌خیال. من ارتششان را نابود کردم. نمی‌خواهم این را نادیده بگیرند.
برای کسانی که می‌گویند شاید من به‌اندازه کافی سخت نگرفتم، باید بگویم من ارتششان را نابود کردم. بزرگ‌ترین پلشان را زدم، چون دیر در جلسه حاضر شدند. گفتند این کار خیلی قشنگی نبود. من گفتم پل جورج واشنگتن؟ سه دقیقه‌ای نابودش کردم. خارک را زدم، همه چیز را، جز یک چیز. گفتم به لوله‌ها دست نزنید، چون نمی‌خواهم به اقتصاد جهان آسیب بزنم.
بنابراین فکر می‌کنم خیلی سخت گرفتیم. به کسانی گوش ندهید که می‌گویند می‌توانست سخت‌تر باشد. کل ارتششان از بین رفته است.
پرسشگر: چطور تغییر رژیم است وقتی هنوز خامنه‌ای جوان‌تر و خیلی از مقام‌های سپاه آنجا هستند؟
چون افراد متفاوتی هستند. خامنه‌ای جوان‌تر با پدرش فرق دارد. افرادی هستند که بسیار کمتر از دو گروه قبلی رادیکال‌اند؛ و من هر دو گروه قبلی را می‌شناختم.
اما به این فکر کنید: همه آن‌ها رفته‌اند. بعد می‌گویند چرا سخت‌تر نگرفتی؟ تنها راهی که می‌توانم سخت‌تر بگیرم این است که دو یا سه هفته دیگر وارد شوم و آن‌ها را شدیداً بمباران کنم. اما این چه چیزی برای ما به دست می‌آورد؟ تنگه هرمز باز نخواهد ماند. فرض کنید این کار را می‌کردم. فرض کنید تصمیم می‌گرفتم این کار را بکنم. الآن بازار سهام ما فوق‌العاده بالاست. قیمت نفت در حال سقوط است. قیمت نفت تقریباً همان جایی است که قبل از شروع کار من بود. تفاوت بزرگ این است که ایران هرگز سلاح هسته‌ای نخواهد داشت. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت، روشن است؟ خیلی واضح و ساده است.
آیا می‌دانید در دو ماه گذشته، من کشتی‌های زیادی را از آنجا خارج می‌کردم و کسی خبر نداشت؟ می‌دانید چرا خبر نداشتند؟ چون ما رادارشان را از کار انداختیم. همه تجهیزات دفاعی‌شان را زدیم. آن‌ها قادر به دیدن نبودند. هفته گذشته، یک شب ۲۵ کشتی داشتیم، یک شب ۲۲ کشتی، یک شب ۱۹ کشتی، یک شب ۲۱ کشتی. هر شب، همه این کشتی‌ها بیرون می‌رفتند.
ایرانی‌ها مردم بسیار باهوشی‌اند. نوعی نبوغ ابتدایی دارند، اما باهوش‌اند. منظورم این است که باید جلوی آن‌ها را می‌گرفتم، چون اگر سلاح هسته‌ای داشتند، از آن استفاده می‌کردند. می‌خواستید ببینید؟ بگذارید چند شهر را در جایی منفجر کنند؟ مثلاً اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت. چون من توافق باراک حسین اوباما، یعنی برجام را لغو کردم؛ توافقی که مسیری به سوی سلاح هسته‌ای بود. آن‌ها پنج سال پیش به آن رسیده بودند. به نظر من، در همان هفته اول از آن استفاده می‌کردند. اسرائیل دیگر با ما نبود. اگر من آن کار را نکرده بودم، اسرائیل سال‌ها پیش از بین رفته بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76534" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFF0zeNV6UDq9e5I5y82M-QIPk4x0SytuhBBYj-ITzFybZf4GmKU5ABv6Ya2MkBlJxif-xchQwo0SgL8DtVpNmCM-hd4qjYHF34snAZF_Zdf6iOwSzp8ysoESkhjWhCA900NQWuWhZALan-Bry8CDbRKXS4YFmCHed3rF_XMTLygADoFRvVHUDeOTJYeaoQYu4wm779lEPQmrWIX7L7x3sO6jp4a7ozedez-o1wnFnbF2kzg7KsIM8dFQ-1e9zepi4iimE70fBHZ1iKWBFfaEn8ZEZvwNLT7BHaXHdsm0TQcLc0q87cWtlM7zPDBz268GG_SXNs_rs-erIgEOas17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا، در مصاحبه‌ای با برنامه «آکسیوس شو» با دفاع از تصمیم خود برای شروع عملیات نظامی در ایران، مقام‌های جمهوری اسلامی را «بسیار باهوش» و «نابغه‌های بدوی» توصیف کرد و هشدار داد که آن‌ها در عین حال بسیار غیرقابل‌پیش‌بینی هستند.
ترامپ با اشاره به مداخله نظامی اخیر ایالات متحده گفت: «من مجبور به اقدام شدم تا جلوی آن‌ها را بگیرم؛ چون اگر سلاح هسته‌ای داشتند، حتما از آن استفاده می‌کردند و با منفجر کردن چند شهر، از جمله در اسرائیل، هرج‌ومرجی واقعی به راه می‌انداختند.»
او با تاکید بر اینکه اگر اقدام او در لغو برجام نبود، اسرائیل سال‌ها پیش نابود شده بود، توافق دوران اوباما را مسیری هموار برای دستیابی جمهوری اسلامی ایران به بمب اتم دانست. ترامپ همچنین با ابراز شگفتی از زمان‌بندی تقابل با ایران افزود: «چیزی که مرا غافلگیر کرد این بود که آن‌ها این‌قدر منتظر ماندند. آن‌ها صبر کردند تا من به قدرت بازگردم؛ البته این کارشان عمدی نبود. هیچ‌کس، حتی با وجود سلاح‌سازی ساختار حکومتی علیه من، فکر نمی‌کرد بازگردم، اما من با خروشی بزرگ‌تر از قبل بازگشتم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76533" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76525">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشجویان متحد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZtX1g6weAIkkfTuqi7JVmKiI9x-727JUmcxlzOLVcyKhsv3WwVLiZbUXmkjH9LCdZjkNMXg-65HyHBsIqRlzlwTpBoSoK8xGANxlS9X3FftTcQN4xZUGE3ZSldcMiWvW_UtrN-tUrCx45Uiz15EYfRKZfk6oDoOC0SRyCIyvdADX4e5s-RA2CbmeNZuhdfVnmGpUroDjen8P4f6WeiRZlJgv2QyfHKMKqvBTeyXDd8qFzG_jEGDvsR3_FeCX8--vEzU41K2-2JLxRYMUNadGo-Bq3LH9V8DZzUv6GaDiX5ltWAPs6-CHgmpXshL21eZuoEoEkdBPzjgVqKt0nMtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAqtDbblmSIcWtaA0tFqO7_t9ERCwHWhjt_BUqw6NBrwjoEHNSBwz_SmtQXQES_r-fx4bYJznaVyoZhwe5N8saNHeb3LHo1DIqPfsZmJbfzmckStu2zZFpceLTdHf9m-8C1WWQOjxXWJlo_QRMJpfgNnaltF9wLMX-Wm4xq_MTJ1fdZJMy_3XC2Pw-KfPbhU2DpXfGUsXpqFixbwnM0_7hmVojoeFgs3YuR0NYi5qtfGRkAVkcsrPgQoy6uJ79YmTBMutNzjEiSONWTzJFDaKTMh14AVeHvw3v4U1snFeLVWMX1ZNWNJXPnUtRXTqPsyUMs8QDwgUatjjAaeflbvjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbtZ8On9KUDpMJVMSBD7P6jcKnPqWsWEA9Cm59GD1jiXBV_mm8mkCVfltjj5ZXWCvlOzrZi-2CyMuraNkTYnU0_zWEDYAgcuvyU2PYBZfng2xf7ye97tloYuCrvmrdVt0afj7QInwPHh8xo160EBhy5atqXs-YeeED-Sv55ymEspgUsfvhjmMH6jDTtmRAi9WiiczUnGmixwD53PtA3hrzIIe7xJHSU3v5R-3KAga6fji81_W8bJ_3tyek4nNL2-G-_7B4TBmdPGDdxJIsDy9uviyjBN2QPZPBOoH_3g8crLRe8aTwU111wwCtg9oskOEOB7LCZlgwDk_e8uYi-omw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d440zxs8MMLfm6Yv5j0tpDYvC609Ns0EKTSmCRV7UB9jSzv8UPoLEvZELOzSQ0tSG8cK7Jngrf0qoe4YeZK3idSrSOUQE7ASPZGVCCNSVVCzvDP_IRNTLLV125uUBUPlDJqVSztrybuXjDY778fdAEG-NbCRYodIBRUM1qXZnFZw6DTG6UMK3Havi1cMzEQdqnzn4Tn2joTMXhjHBOhGcA04dkz62PNhUDSLUzeEA4anli9WBLi_ZbsaYoxzmL7IMJ9NOnpg3yVRERKUMg5ly8ldfBUQ1XdtVVnau4_tLChHg3rPX1TxZeFqan5nwRJHbP_J5GyzAIHiuxkG4cFW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QU3vs39PMY49plRhtszsjQbRJfGEUYNAXSsH42uRVjdZP-B1ul5P_Aon5dzFGKLTX4Yd0-UWrbRd5MPL_W6jaEgTXegyhwwAjoiZQ5SSbYePeX-zR_Qn7KFfqdTkJE13lQXKiav0i6ZdMv0jsj3IEAq1plbTxuuucSjolwJSHtgGpUuQBdWzcGqHJ6r_albEJmAMV5fr2YeAcv-69nDyDD4DRORyIFZV60833x2bjkVc0qmZeHluqJ030EmrobIWdwk3tPM-Jq9LqiOmThBn13u2LD_2Uy_q4XtyrGRcBQCBxPAN92QNABSFvHp-L1yF0Cf0b3Brxn7iQYBIi5xmfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6TINdDwhPya8RnLolNInFL6V24RGziak4zDhWjRrRYTPA8waLHB75BjHnvw7w_03Q9lpEoHARgRUzEH95xTNO7Z3KCJzMvuXhYoneDXW1m9tyi8OOKcMO7ZGpUVwOtZW3vqFQySa7grJNZsSOqkC9TDPF_aZ-vJwYWp-Co5Se319lUD1xx-B9K7WsNiR7D99N7ruQ9IPSb-sB7J9fJj9LSJb7Ij1SP1188SmoqyP3eg3QeCOoBt4wHZQPXu1woWRgHck8Qr7HZuGT7viWdgaAU7jewbPIaMpRw4IUjz0ag4Hpp1KalK1BDujfBAhcToQejf-oNfodAykyErenHwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyK-dpIaXKXHZxuBDDzBTACX5VstEQSWViaCWJwplz-o0dw8kqWB8f1_x9P2oBku6cWsFb2yzhM8aL11tq8Q4GxFNIlfpy19ex9dCuFhdnEn5cTIlTs-DtPHA_gIo1fESxsSEuWbTVopoolnY0Khs0A4USSnMRwjFotYGYOs4ygPv7IyrmKBZ-fA-GLJoaFRh9Xuh9tmvLkGVisNq84WrsWu1MCAbtGDLWLoBGDhWX37xu7slv1RDa5tAGhIML5ludTYz4u7FBk9V0BqqtyENF_xgsRUQC5_e78UFHvXSDxD3W-5062aXJzQ2ctNHeneZeBxVXB_bY-KU8QW7HiDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCHLhwKjPseuVY3HGs_Mdu8SP5ZeSjb2EqYCrKI3vUt7hWPDTXI4TWxYH0ydrmjAL-F7D_zzEvu7G7ac7-_qReUfxK_ve28aG-saUX67fDsePXGEX5oQ79CXeZm2SIf64wfZX46tcObCoIDo3UkOmtlBW_NLoqsyP1baekxBfiBrPWL1VDO8OGyL9lfkGNC7Wkn1NaxbOXYwqk9DCfk6ypIHIIrjg9yELH_xR36SYQsB-E2BgjniHRyqDemET0bQANdCxGc8Egr-mun9bYg8_tAhkHYFw3n49A2LZk3oLQQFxrvEaCuZRDJv4J7BtxR9WR_OI2vZSx2qY5sIWLhhqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
صدور حکم اخراج برای هفت دانشجوی دانشگاه شریف؛ صدور حکم غیابی برای یکی از دانشجویان بازداشتی؟
🔻
بر اساس گزارش‌های رسیده به دانشجویان متحد، کمیته انضباطی دانشگاه شریف، برای هفت دانشجوی این دانشگاه حکم بدوی اخراج صادر شده است. اسامی دانشجویان به شرح زیر است:
🔻
رضا دالمن، ورودی کارشناسی ارشد ۱۴۰۳ مهندسی کامپیوتر: اخراج و چهار سال محرومیت از تحصیل
🔻
فاطمه خاکپور، ورودی کارشناسی ۱۴۰۳ شیمی: اخراج
🔻
حسین شادمان، ورودی کارشناسی ارشد ۱۴۰۴ مهندسی صنایع: اخراج
🔻
سپنتا سعیدی، ورودی کارشناسی ۱۴۰۴ مهندسی کامپیوتر: اخراج و پنج سال محرومیت از تحصیل
🔻
مسیحا باقری، ورودی کارشناسی ۱۴۰۲ مهندسی کامپیوتر: اخراج
🔻
فریبرز کهن‌زاد، ورودی کارشناسی ۱۴۰۰ مهندسی برق(تغییر رشته به مهندسی صنایع): اخراج و پنج سال محرومیت از تحصیل
🔻
پرنیان خدابخشی، ورودی کارشناسی ۱۴۰۲ مهندسی و علم مواد: اخراج و پنج سال محرومیت از تحصیل
🔻
همچنین در برخی رسانه‌ها خبر صدور حکم اخراج برای «آریانا کوچکی»، ورودی کارشناسی ۱۴۰۰ مهندسی صنایع، نیز منتشر شده است. هر چند بر اساس گزارش‌هایی که به دست ما رسیده، ایشان در حال حاضر بازداشت هستند و خبری در مورد برگزاری کمیته بدوی ایشان نداریم. هر چند صدور حکم غیابی برای دانشجویان بازداشتی در جمهوری اسلامی، پدیده تازه‌ای نیست.
🔻
لازم به ذکر است از میان هفت نفر یاد شده، کمیته سه تن(سپنتا سعیدی، حسین شادمان، مسیحا باقری) با محوریت فعالیت در شبکه‌های اجتماعی و کمیته چهار تن دیگر با محوریت اعتراضات اسفندماه برگزار شده است.
ارتباط با ما:
@Public_anjmotahed
🆔
@anjmotahed</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76525" target="_blank">📅 22:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=GxdVSXj7cUbZla10RaG05HX1jn8AJDmtEltupAc_fiUfvyFREyDteqM4vDDpvIsHsNE5dRSWLxuH9aOdr9O8AKopkbcw3IdUaStdyCXxFkmTz3eyuw9bvzeUcOP8q03zqY6U4s3tSYmqrhEvegQmFseCaaa8v2T6W0TXXp2mG7niWBBua6FrpIVbkK14mwBHCOXFJxd8ovHt2mOPdPHyVnZsKVDFtIFIsy3NdF72Q01ou_mG_n_NrGI_sVfY3YVZFV1QgHk2ajU0sRhluJj7efcFIRTBrGPkY2mPFxCrwzq94DkTMDLDs-iENxLI2z_6ageB9T959JtKb4cCuRTmQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=GxdVSXj7cUbZla10RaG05HX1jn8AJDmtEltupAc_fiUfvyFREyDteqM4vDDpvIsHsNE5dRSWLxuH9aOdr9O8AKopkbcw3IdUaStdyCXxFkmTz3eyuw9bvzeUcOP8q03zqY6U4s3tSYmqrhEvegQmFseCaaa8v2T6W0TXXp2mG7niWBBua6FrpIVbkK14mwBHCOXFJxd8ovHt2mOPdPHyVnZsKVDFtIFIsy3NdF72Q01ou_mG_n_NrGI_sVfY3YVZFV1QgHk2ajU0sRhluJj7efcFIRTBrGPkY2mPFxCrwzq94DkTMDLDs-iENxLI2z_6ageB9T959JtKb4cCuRTmQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه جی‌دی ونس با زیرنویس فارسی
گفت‌وگو با:
الی بث استاکی، مجری و مفسر محافظه‌کار مسیحی آمریکایی، میزبان پادکست Relatable در شبکه BlazeTV
برنامه‌ای که در آن از زاویه‌ای مذهبی و راست‌گرایانه به سیاست، فرهنگ، خانواده و مسائل اجتماعی آمریکا می‌پردازد.
او در میان مخاطبان اوانجلیکال و محافظه‌کار آمریکا چهره‌ای شناخته‌شده است و در این گفت‌وگو با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره ایمان، خانواده، سیاست داخلی، اسرائیل و توافق با ایران صحبت می‌کند.
یک ساعت درباره مسیحی زندگی کردن
حرف زدند
و ده دقیقه درباره نقش و نفوذ اسرائیل در سیاست آمریکا و توافق با ایران برای مخاطبی از اون نوع
اینجوری می‌پرسه: می‌خواهید یک مادر معمولی چه بداند؟
متن این دقایق:
https://telegra.ph/JDVance-06-19
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76524" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76523">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBGWb2-3QtPJUKtq05WfIcVLJIlAw-p-1q8wMhwojrQ7nNapiFzePut9o4WmIJQK913txzg7giLTYU3XZNAxwGSmDdLo_n3VdjJkUEykA8fnCKzJI_9URWhTjyAB4FPWeaLgIDF-pG_HbuzIj2IFumq2RuFpyeSFdupDse16iM39OkhwuvKzTDGxT-e_YaRvifcRsriEShSAeEAMXM9tC53xxjyFcgw5e8Ak3XKTQ7izANJIdXlw1ZMvSTvkIHBxFE_0nHSqCLxlRz5uZQtEE9B6YTRpxcoVPSEzmrVVqaSLUOmjA_CpvyoR_GII1UKVH1kQv9huuLvVF--3HCpHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در یک گفت‌وگوی تلفنی با شبکه ان‌بی‌سی نیوز گفت که روز جمعه با مقام‌های اسرائیلی صحبت کرده و از آن‌ها خواسته است با گروه حزب‌الله بر سر آتش‌بس توافق کنند.
بر اساس مطلبی که خبرنگار این شبکه در شبکه ایکس منتشر کرد، ترامپ به این مقام‌ها گفته است: «بعضی وقت‌ها فقط باید آرام بگیرید و از عقلتان استفاده کنید.»
این خبرنگار همچنین افزود که ترامپ مشخص نکرد آیا مستقیماً با ‌بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفت‌وگو کرده است یا خیر.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76523" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HZ3-X4Iz-ZsZ-53B-2z5VRnGlGoymAS5FyNXEHnZVCcgVgTIsIt3bmCvDEIM0g7rE4OkBdD2uMr3KkMfz5CARX0kRsE-pOaaAYB1Xoc58PM-_keBf_B9k-iG6R-dOceEx57hPtxa9iEH8qs7tAyiBrkd3XURLsD8Yyuw4NATKLzTU63XgPy3izbJf0dA6w5A-T0ddQTsO2A3zBsIPJayGXQCdXOjF51x9V1-NrP1lA5YG_9S1r24IvvCg8QMGvzOsa75DDibEJoOyH5CoQxhTPZjQRSFObXbr6WOzj4rIZ7CyT0Jl2an6svjTjbUwm-TBPRpBu3zU4_Twa50TS_Xkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
او تحویل سلاح‌های حزب‌الله را رد کرد و افزود این سلاح‌ها برای مقابله با اسرائیل هستند.
نعیم قاسم همچنین گفت که ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
دبیرکل حزب‌الله لبنان ادامه داد: «ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76522" target="_blank">📅 20:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76521">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4iW_7YmLefnburVNbiLcn1OkQnL6ZWG0sz3eOs8Jf5sZIwF6h-Cwemfg26iZiYt2jStlSO-45KrlMrm9LAiKgfZzB8lsjOhHsbqQM79hf55q1K8HJhOLq3HytkCONhme_bh4PNBUt5IPO3o7wmTbZHwlRh6A7_ODF7-1J6GIBeAD-eiE792AAxNatg7Y6XKY1uAIHKxFANILJyY1guQxd-v1FtJap_aDGvj1WRhGNrZ4cinxLcPlxTULf4CG1PmCoGsmphbDaXSVzO0Z1DjBeUyL9wrHWfK6tPx6jaoNELVjwTP0wLao-r_9IPfAg7ilDhbRwE__gRhVWX5u88Mpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه ایران، روز جمعه دعوت جمهوری اسلامی از بازرسان آژانس بین‌المللی انرژی اتمی برای حضور در ایران و انجام بازرسی از تاسیسات هسته‌ای را رد کرد.
او گفت: «بازرسی از تاسیساتی که دسترسی آژانس به آنها به‌دلیل حملات نظامی متوقف گردید، منوط به روند مذاکرات و نتیجه آن خواهد بود.»
پیشتر جی‌دی ونس، معاون رئیس جمهور آمریکا پس از اعلام توافق اخیر در گفت‌وگو با شبکه ان‌بی‌سی گفته بود که بر اساس تفاهم‌نامه میان واشینگتن و تهران، بازرسان آژانس بین‌المللی انرژی اتمی «قطعاً» به ایران بازخواهند گشت.
اسماعیل بقائی همچنین گفت در حال برنامه‌ریزی برای برگزاری یک نشست طی روزهای آینده هستیم.
نشست بین نمایندگان ایران و ایالات متحده که قرار بود جمعه در سوئیس برگزار شود، لغو شد.
سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد: «با توجه به اینکه امضای متن یادداشت تفاهم در بامداد ۲۸ خرداد به صورت دیجیتالی انجام شد، برگزاری نشست مزبور در سوئیس فوریت ندارد.»
او همچنین گزارش‌ها درباره بسته شدن تنگه هرمز را «بی‌اساس» دانست و گفت کشتیرانی در این مسیر در حال انجام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76521" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76520">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM5HcpMzv_RicvW_toOWZn4iEmrWqrmiO6tGHNIou-07vUsLudxr_RogLSOIzwPgAkh1AV25g3wMZKYJB-J5lDIOqhgkT6Nodb-TYwZiz9fZ1M-Ow64jC9oQQ_2MI5rAtz5TpbOZzG5mfb97QYxHQbwTB4zwK6W5lIflc0BcZeaPoTQEcTr3QBXcB_mlXve8OVPEOJQfAbF1aV8WzetMrUclG0Yy5-4HHoIfjPAHyWPy8P46QU3pVpxk_G2BnCCPWL1SDsMB6CkvtDEXGa26wGdD_l7MCNPVQbJ4l7s5IXq2EykG1ldy-xzS92fHOb3Soh4JeBOd945_srFPbxMd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز گفت که اسرائیل و حزب‌الله بر سر یک آتش‌بس توافق کرده‌اند که قرار است از ساعت چهار بعدازظهر روز جمعه به وقت محلی آغاز شود.
این مقام که نخواست نامش فاش شود، افزود که مذاکره‌کنندگان آمریکایی و قطری با کمک ایران این توافق را نهایی کرده‌اند.
این مقام همچنین گفت: «درک ما این است که پس از تبادل آتش امروز، اسرائیل و حزب‌الله اکنون در وضعیت آتش‌بس قرار دارند.»
شبکه العربیه نیز به نقل از یک مقام آمریکایی از توافق برای برقراری آتش‌بس بین اسرائیل و حزب‌الله از جمعه خبر داد.
این در حالی است که نخست‌وزیر اسرائیل ساعتی پیش اعلام کرد نیروهای نظامی این کشور تا هر زمان که لازم باشد، در خاک لبنان باقی می‌مانند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76520" target="_blank">📅 17:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibODchGkgv1-XM7B5n0WR0RZKaIgv_zAYv1LLpArvjWTNAeXHnsMlv6Fzn7XLlUsxE_MOKgWiE1heFIQIlEEO0tujd16e0tsRgiPZzSY0EKLni1_PtkH0iRc-Rkoi9bo7l8D5LF7SVoqvOKOs0Yf0zBEM3ws3UKikQ9a6DJ5FAmeWwi0r9A6E_l5gBdTeC9vnhfYHyg-eDr4vbla5SqsWDtUH1T_OhBmKFq4lS2ysAyR0xPUKUQHSYurXTF2NKZnYqBuA1vnaN3Hsuhk7zY0EZnbTxudNhaRHj13UU6q5tjiAfM9PaYTmSTH5NcOhLkQ47bQ0wk1UMe6USst56A88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957528437f.mp4?token=qkr4_Ch6yaun3Qv4NZTvigGk62mwPvpEoUEkAzN2Vh07WNQ28SzwCJkHIk0vXX7CnOYofuF19OFKT_Ijy7YniYuhf7bSF6Ej5xCO53CsghJQapYvSG40bMq2CQwD73ulAw7DXY-SIX-NRsgK0c8Y7yP2USIuqBVORe4kdVEyOyEwNowifAB8yAo7UV5f6-Jh7o7QG6CXtOQonZwlqLHNTobX7GOpiUIS5VsEfHSttK6BmdeyKvzSdR8_WzpM1MObz36b4WiDR4SH7e-TddAlbJ5HKGEm3Kh24vjsQuELAvv30yryjTq9_U63QZ34D_9IvV1RNuI-JmTIPbCLZcMsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957528437f.mp4?token=qkr4_Ch6yaun3Qv4NZTvigGk62mwPvpEoUEkAzN2Vh07WNQ28SzwCJkHIk0vXX7CnOYofuF19OFKT_Ijy7YniYuhf7bSF6Ej5xCO53CsghJQapYvSG40bMq2CQwD73ulAw7DXY-SIX-NRsgK0c8Y7yP2USIuqBVORe4kdVEyOyEwNowifAB8yAo7UV5f6-Jh7o7QG6CXtOQonZwlqLHNTobX7GOpiUIS5VsEfHSttK6BmdeyKvzSdR8_WzpM1MObz36b4WiDR4SH7e-TddAlbJ5HKGEm3Kh24vjsQuELAvv30yryjTq9_U63QZ34D_9IvV1RNuI-JmTIPbCLZcMsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه ایتالیا روز جمعه اعلام کرد در واکنش به گزارش‌ها درباره اظهارات دونالد ترامپ سفر برنامه‌ریزی‌شده خود به ایالات متحده را لغو می‌کند.
آنتونیو تایانی در شبکه اکس نوشت: «سخنان شدیدا توهین‌آمیز رئیس‌جمهوری ترامپ… به همه مردم ایتالیا اهانت می‌کند.»
به گزارش شبکه ایتالیایی «لا۷» ترامپ درباره دیدار خود با ملونی در نشست گروه هفت گفته بود: «ملونی آن‌قدر می‌خواست با من عکس بگیرد که فقط از روی دلسوزی با او موافقت کردم.»
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، در واکنش به اظهارات اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا، این سخنان را «کاملاً ساختگی» خواند و گفت از نحوه رفتار او با متحدان «مبهوت و شگفت‌زده» شده است.
او تاکید کرد: «نمی‌دانم چرا رئیس‌جمهور ایالات متحده این‌گونه با متحدان خود رفتار می‌کند» و افزود این نخستین‌بار نیست که چنین مواضعی از سوی ترامپ مطرح می‌شود.
ملونی همچنین این رویکرد را «مایه تاسف» دانست و گفت او قاطعیتی را که در برابر دشمنان غرب نشان نمی‌دهد، در قبال برخی رهبران متحد خود به کار می‌گیرد.
نخست‌وزیر ایتالیا در پایان تأکید کرد: «یک چیز را باید به خاطر بسپارد؛ من و ایتالیا هرگز التماس نمی‌کنیم.»
در ادامه این تنش‌ها، آنتونیو تایانی، وزیر امور خارجه ایتالیا، نیز اعلام کرد سفر برنامه‌ریزی‌شده خود به آمریکا را لغو کرده و این اظهارات را «توهین به مردم ایتالیا» خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76518" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfK3bF8upchOljXJdgv3dv4rf9cocTwR3O1CeymdRiMnEAaYAL1gfZ1ZWqgB6LF03TYG4VEFSkUP4viOmS5WpwhNSnprgdRvliKb8y4e-SlHsDuWBa0zclrPhm--GySkOE0CJi7SJbiqlcvS8VSQhj403cNi-MTfbcmUp5omGOmGngf4PCh3eBKuZSwNKvM7uomgmDl2nA_JZLszABPMvreh_oTqQpjtKE827-CTCH6fJpCPZw8X2zO2g7lJ7jbbxu2lUQ_Wxix1Ch3rlA0RHtN_FmBj72yMX9yIstcuHPhOJX_5iuPOzZCFwaHABlKLuapYqeOz8iCvIp5R0cLXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅️
#محمد_نوروزی
، شهروند افغانستانی ساکن ایران، که در روز ۲۵ دی‌ماه ۱۴۰۴، در منزل مسکونی‌اش دستگیر شده بود، توسط دادگاه به شش‌سال زندان محکوم شد.
🔹️
طبق گزارش رسیده به کمیته پیگیری، محمد نوروزی پس از بازداشت به آگاهی ملارد منتقل شده و پس از ۴ روز همراه با ضرب‌وشتم فیزیکی به زندان قزلحصار منتقل شد. او طی این مدت مدام تهدید می‌شد که رد مرز شده و از ایران اخراج خواهد شد.
🔹️
او در نهایت با قرار وثیقه یک میلیارد تومانی از زندان آزاد شد و سپس توسط دادگاه به اتهام "اجتماع و تبانی و تبلیغ علیه نظام" به شش سال زندان محکوم شد.
این حکم هم‌اکنون در مرحله تجدیدنظر قرار دارد.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76517" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76516">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZbooP21MeR94ZRTqtIvXPAYEa_Y_pnqcaf_9jx4oja7kWId7ZTx4VrCT2sDG6YELXGJuQH0oiAAiaMW53Sbx-V_K84GJjTDpHaGdhW5tWkh9sw6qagXvc9Ega6IYU9mL221fytZXP6JiJoL8mQLjISpHoZs10wpBs3aMSCDuQYfJHq_mqKltsm4QfRXHOpVEOgI6EFX2R--v03wTt54YTuNbeJKrsVQq7-6qr6pC_CvSx3hQv5PPVaDwApsWknZXRIyFDckRpOC4cVzNfuufroTyz2rqIp7Q3JiNZ1EUKwe-WHXtAn0c3ve9TIUshz8Y28cu2nxjLIpa71Kso16TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز جمعه بار دیگر گفت که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در لبنان باقی خواهند ماند و وعده داد که حزب‌اللهِ مورد حمایت ایران برای حملاتش «بهای بسیار سنگینی» خواهد پرداخت.
او روز پنجشنبه، ساعاتی بعد از امضای تفاهم‌نامه پایان دادن به جنگ توسط ایران و آمریکا، نیز بر ادامه حضور ارتش اسرائیل در مناطقی از جنوب لبنان تأکید کرده بود.
نتانیاهو در بیانیه روز جمعه که پس از اعلام کشته شدن چهار سرباز اسرائیلی در لبنان از سوی ارتش منتشر شد، گفت: «اسرائیل حمله به سربازان یا قلمرو خود را تحمل نخواهد کرد و بابت این حملات بهای بسیار سنگینی از حزب‌الله خواهد گرفت.»
او افزود: «اسرائیل تا هر زمان که برای حفاظت از جوامع شمالی لازم باشد، در منطقه امنیتی جنوب لبنان باقی خواهد ماند.»
یسرائیل کاتز، وزیر دفاع، نیز گفته بود که ارتش در لبنان خواهد ماند و افزود که به هر حمله‌ای «با نیروی قابل توجه» پاسخ خواهد داد.
لبنان اعلام کرده بر اثر حملات اسرائیل در سراسر این کشور ۱۸ نفر کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/76516" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76515">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UmCh94GLhs3ktikJNuI_t2BxumaTDMlQuM_j2zuOySWXGevxYatyQH30vSA13oiL68exzhxVs4Uod9utmcXXTWZ8TXQ-84LTxDi625oV5nSqr4cRTTSYYDlY5m_ChNz9SW9ErB1NoJ82cAOR4_WSbyu305DR9ImO2_BE-wXt8gGV3R5paRDdvyg2dt7l0iteDQAJop_z13Kn43mxKfz7Bud1Cn9Iiib6NxVX6YMrbPNeK39lskiVLf8JfxI_PmJDhOABk4BkGNA-Blv3QkdzrmvJhLesbFu4ial5jSVoW2JrXhq_GR1-LCntxXDzQ4ChlqoNKf0aWP8kxzpnNojsnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینعلی شهریاری، رییس کمیسیون بهداشت و درمان مجلس جمهوری اسلامی، در گفت‌وگو با دیده‌بان ایران، با اشاره به ادامه «تعطیلی مجلس» گفت: «مجلس را بستند تا هر آنچه خواستند امضا کنند.»
او با تاکید بر اینکه تفاهم‌نامه با آمریکا در نهایت باید به تصویب مجلس برسد، افزود: گذشت آن زمان که برجام را در ۲۰ دقیقه در مجلس تصویب کردند. ما یک بار از این موضوع آسیب دیده‌ایم و نباید دوباره همان اتفاق تکرار شود.
شهریاری همچنین از اظهارات عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره احتمال رقیق‌سازی اورانیوم غنی‌شده انتقاد کرد و گفت موضوع هسته‌ای نباید در مذاکرات مطرح شود، زیرا به گفته او «جزو خطوط قرمز» جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/76515" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pvrmqt2fYaiTBy88J3TaP-2xMGgjKOXjSCJ6Ztny4TIumH5ZW28zWZHBN1gTDiVFHkTotoiTN8gakv2jYbAgQC0FDwrqTmWqvXdSO936xzX6TrcY-7eIYAwfb7Ioxs7kIvfnBX03Ki6gfHHP0Q62HZ3izJVMlF-ffr8M2Lh6K60eV7O9PnAcctUi93b_kU_N0SZSynZ1LilqOjOPCigBrpYWExgJppxXitodrg963DjMxQTdGhM_67fnunQzPiAYEajdSdy6-IPza2k9ZX1KPr5uH29X3Z2EbS_MZrejGOUjJIteKP68zPWlLQrVTKqjacw3u7xH12Qzgk_IKCjaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام پیشین مرتبط با تحریم های ایران درباره «صندوق ۳۰۰ میلیارد دلاری»: پیش نیازش لغو همه تحریم هاست که دکمه روشن و خاموش ندارد
میعاد ملکی، مدیر پیشین «دفتر هدف‌گذاری تحریم‌های خزانه‌داری آمریکا» در یادداشتی درباره موضوع «صندوق ۳۰۰ میلیارد دلاری» برای ایران که بسیاری از کارشناسان درباره آن ابراز تردید کرده‌اند، می‌نویسد: با کنار گذاشتن موضوع معافیت/مجوز نفتی و نگرانی‌های مربوط به عدم اعمال تحریم‌های جدید، باتوجه به الزامات برای اجرای واقعی بند ۶ (صندوق بازسازی ۳۰۰ میلیارد دلاری) و بند ۷ (لغو همه تحریم‌ها) به این نتیجه می‌رسیم که مذاکره‌کنندگان آمریکایی یا می‌دانستند که توافق نهایی ناممکن است، یا این یادداشت تفاهم فقط تصمیم‌گیری را به آینده موکول می‌کند.
ملکی که خود در طراحی تحریم‌ها علیه حکومت ایران نقش داشته در این یادداشت می‌نویسد: این چیزی است که «اجرای کامل» در عمل، فراتر از امتیازهای هسته‌ای، به آن نیاز دارد:
بند ۶ — صندوق ۳۰۰ میلیارد دلاری:
صدور معافیت ریاست‌جمهوری از تحریم‌های الزامی بخش ساخت‌وساز ایران طبق ماده ۱۲۴۵ قانون IFCA (معافیت‌های ۱۸۰ روزه قابل تمدید که در هر دوره نیازمند اطلاع‌رسانی به کنگره هستند).
خارج کردن سپاه از فهرست سازمان‌های تروریستی خارجی (FTO)، زیرا در غیر این صورت سرمایه‌گذاران با خطر مسئولیت کیفری به دلیل «حمایت مادی» مواجه خواهند بود و هیچ مجوزی این مشکل را برطرف نمی‌کند.
استفاده از معافیت مبتنی بر منافع ملی در قانون ISA (قانون تحریم های ایران) برای سرمایه‌گذاری در بخش انرژی و نفت.
در نتیجه، هیچ نهاد سرمایه‌گذاری حاضر نیست میلیاردها دلار سرمایه را بر پایه معافیت‌های شش‌ماهه قابل تمدید متعهد کند.
بند ۷ — لغو همه تحریم‌ها:
ماده ۱۰۴ قانون CISADA (قانون جامع تحریم‌ها، پاسخگویی و واگذاری سرمایه‌گذاری‌های مرتبط با ایران) رئیس‌جمهور اختیار معافیت ندارد؛ تحریم‌ها الزامی هستند و لغو آن‌ها مستلزم تصویب قانون جدید در کنگره است.
ماده ۱۲۴۵ قانون NDAA (قانون مجوز دفاع ملی آمریکا) معافیت‌های ۱۲۰ روزه قابل تمدید که در هر دوره نیازمند ارائه گزارش اجباری به کنگره هستند.
تعیین بخش مالی ایران به عنوان «نگرانی پول‌شویی» تحت ماده ۳۱۱ قانون پاتریوت: این موضوع نیازمند مقررات‌گذاری جداگانه از سوی شبکه مقابله با جرائم مالی وزارت خزانه‌داری آمریکا (FinCEN) است و صرفا از طریق دفتر کنترل دارایی‌های خارجی (OFAC) حل نمی‌شود.
تحریم‌های مرتبط با تروریسم، حقوق بشر و موارد همپوشان با پرونده روسیه: هر کدام مستلزم اقدامات حقوقی مستقل و جداگانه هستند.
ملکی در ادامه می‌نویسد: «لغو همه تحریم‌ها» یک دکمه روشن و خاموش نیست، بلکه پروژه‌ای چندساله در حوزه قانون‌گذاری و مقررات‌گذاری است و کنگره نیز در آن حق رای دارد. و این پرسش مطرح است که چگونه می‌توان اتحادیه اروپا را وادار کرد محدودیت‌های مرتبط با ایران را که در چارچوب پرونده‌های مربوط به روسیه وضع شده‌اند، لغو کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/76514" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76513">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj9_NCLZHaPo5rUSh4HpklGbS8ubcIL_h0vJr3LnpkSDM3PEs6eUIVT6xAd9yO0_l0agykY9TrEZkCMVfwd3a25eZADxSo4XWH9KXtSxYkWtGFzJQggDSo7myvtXnkDEXA5TzrFeMxC88G7AswR17l8MgZFhNPd4k6ujveBuSpHC2lw2RUAR5ynAe37XMV5Y2VJGuMoSY-N5MMaaCnhzX_R5FubkijS3YUSU5t0dNHOQyaQCmHFs2_lJ6HIHY1AeG5IMBiBJKHFnP-ihuVhgTC7s1FXYm3akyVpbl2Wlq_ubWzk2PDA0DW4HYHo3fkyu8getN_asrzOm44mFxhv6wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه هاآرتص در تحلیلی نوشت توافق دونالد ترامپ با جمهوری اسلامی، برخلاف انتظار بنیامین نتانیاهو، نه‌تنها به تقویت موقعیت سیاسی او منجر نشد، بلکه شکاف بی‌سابقه‌ای میان واشینگتن و تل‌آویو ایجاد کرده و نخست‌وزیر اسرائیل را در آستانه انتخابات با بحرانی تازه روبه‌رو کرده است.
روزنامه هاآرتص در تحلیلی نوشت نتانیاهو امیدوار بود سفر ترامپ به اسرائیل و حمایت علنی رییس‌جمهوری آمریکا، مهم‌ترین برگ برنده او در انتخابات پیش‌رو باشد.
به نوشته این روزنامه، نتانیاهو انتظار داشت این سفر پس از «پیروزی کامل» بر جمهوری اسلامی، سقوط حکومت ایران و انتقال ذخایر اورانیوم غنی‌شده برگزار شود، اما اکنون نه‌تنها هیچ‌یک از این اهداف محقق نشده، بلکه ترامپ تقریباً هر روز با اظهاراتی تحقیرآمیز از نخست‌وزیر اسرائیل انتقاد می‌کند.
هاآرتص افزود توافق آمریکا و جمهوری اسلامی در اسرائیل به‌طور گسترده «فاجعه‌بار» تلقی می‌شود، زیرا ترامپ برخلاف وعده‌های اولیه خود، جنگ را بدون تحقق اهداف اعلام‌شده پایان داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/76513" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76512">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC8DEHZzynEENDC6_U_SwLQdmPWmOiVC8ZpVaJQsRTrfzs812qd1NhUHgzxiqjNiTmb5eo4nygokj89o1hJnWolMeY6ogt2shhv-Y8XnITw6hZUlNHLMPNA8ZSv9HvourqWEUK0ahVvLE_kspMYwuIB0exAJNQlTlBfCMOwEHqC5OzLTndAx8q4ci3U_3YTrZ43fXxx7ZqcLmAYWht0q6uDEJUuFzbyZxYS5Kztt4bfR5-z9UxhL3Yr9WPwvDMqWfJA8PqqCOHJBJvh2pR3a7oSmmzR7KXAKhat4mQbn8RvFUxvZkaoBAUTJ9_PuX-1WY7hJ3CY03dJlhJcOih2yBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«معین بصیری» ۲۱ ساله، ساکن شهرک اندیشه تهران، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله از نقطه‌ای مرتفع و از روی پشت‌بام شلیک شده و به قلب معین اصابت کرده است.
او در پی این جراحت جان باخت و پیکرش پس از انتقال به کهریزک، به بهشت زهرا منتقل شد.
نزدیکانش می‌گویند پیکر معین بصیری را از بهشت زهرا تحویل گرفتند و مراسم خاکسپاری او روز ۲۱ دی‌ماه برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/76512" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76511">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fxfquARP__EoP6HApwIoSrfx4Vrk66t_68l3tuqBgZx52rfRBug6__7af4hruiALXEtlEs9Uj0n01SBOkTypPx_e3YZI11QBsrCrFWcKcwb0lox3n_KkHabSO54zUlBbOyGT6AsKru5O2TnOkEZewnQf5lBv8vI6Bz_ElnEADad07A0yE7em94JcvKbbL9Ufinil4H36sDEB0rPokkJQYihj5Nm8uEE9vGlUev2DA0mD8q0IMUj009rPDzOnJnXlMFbpfw82w7eaSz9KYv2FoanfPjvPabuXd356gCG8rYPDLDxyrIH-r2nOhfGtwW_kanq3xCVCTex6WXwQMqSIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
«جنگ، ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات ضدهوایی، نه رادار، و عملاً هیچ چیز دیگری هم ندارد؛ با این حال دموکرات‌های احمق می‌گویند ایران الان از چهار ماه پیش وضع بهتری دارد. اصلاً می‌توانید تصور کنید کسی با چنین حرفی قسر در برود؟ بعضی‌ها چقدر می‌توانند احمق باشند؟؟؟
رئیس‌جمهور، دی‌جی‌تی»
realDonaldTrump
«ما از سرِ درماندگی دیدار نکردیم؛ ایران بود که از سرِ درماندگی آمد. کارشان تمام است! این ۶۰ روز را هم طی می‌کنیم. هیچ پولی گیرشان نمی‌آید، حتی ده سنت!»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/76511" target="_blank">📅 17:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aep93NK9hCw7k-BqP-95lVF0jQe5m7tR7FtE587tGS5kBoTCAe2la1XP029v6EZ939T7Yl94bg7YFr9E64LT5KZpPs1_6CSeolb4pgwtfZegULNc5lgsxD6ukpIVKXOOAK_KdZQwP3b01WELtBdrNM-Q9ozkGJJ46OWkFX5xmEq_KO1E6m5DEowhbAjGvndjtAZDenl438G__npc6UbJcGl2l78u0po1ZF6a5kRv5vcAP1P5ut46_Rn-HBHoeSa5uv6irCrC915mH_USy2c2OE5tHVB9xmgu2qDjLB5H6WZ7SzbvwARYdJdnWygBE5Yz9Ygri86IP8ljdJxCQIgvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lm5UFWzIxMyPYYRuUk3LK4bCUErCT6vk3rSOWVf-HB5kGbWOpKxlrz2Q2FrSXCKgK2cnwGFAc3JG3-BeBTiMNmxEzTrhWgmrDzSSrC6cO4rSqnNrkn6XkzJoR02sTq92QqP4T4gn1hp5sZdlAWz7usUkuSLgpjTM-WVaL5EczTHPgTSmTKNxy53BabDe13nkwG2aEl3GOMPhE5FQAqqiRcwkpMQEU_gvdWFXA6QXc8fwkRsfRQISK63j23QfdggvVoxa87wOLamutq2350uZdk-_OV5Jz9RMlvRiwfdWJxXRmRfJ3R8lZp6AHHW3Z0TU4BHRTOFWJuWTg4ayDx7tbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر خارجه فرانسه می‌گوید پاریس تا زمانی که اطمینان حاصل نکند مذاکرات درباره برنامه هسته‌ای تهران انتظاراتش را برآورده می‌کند، با لغو تحریم‌های شورای امنیت سازمان ملل متحد علیه ایران موافقت نخواهد کرد.
ژان نوئل بارو روز جمعه ۲۹ خرداد این موضوع را اعلام کرد. فرانسه یکی از اعضای دارای حق وتوی شورای امنیت سازمان ملل است.
بارو گفت تا زمانی که مذاکرات آمریکا با ایران به ابهامات مربوط به برنامه موشک‌های بالستیک جمهوری اسلامی و حمایت تهران از نیروهای نیابتی پاسخ ندهد، ثباتی در منطقه برقرار نخواهد شد.
او افزود: «ما به یک تغییر اساسی در رویکرد ایران نیاز داریم.»
@
VahidHeadline
وزیر خارجه فرانسه: کشتار معترضان دی‌ماه را فراموش نکنیم، مردم ایران بزرگ‌ترین قربانیان جنگ بودند
بارو که با تلویزیون «فرانس انفو» مصاحبه می‌کرد در پاسخ به پرسشی درباره سیاست فرانسه پس از «امضای تفاهم‌نامه پایان جنگ» ایران و آمریکا در قبال تهران گفت: «مردم ایران، بزرگ‌ترین قربانیان این جنگ بودند. آن‌ها از یک سو گرفتار سرکوبند و از سوی دیگر به رویشان بمب ریخته می‌شود. ما کشتار ژانویه (دی‌ماه) را که در آن خشونت دولتی بدون تمایز، معترضان مسالمت‌آمیز را هدف قرار داد، فراموش نمی‌کنیم.»
فرانسه حملات نظامی آمریکا و اسرائیل به جمهوری اسلامی را «غیرقانونی» توصیف و بارها اعلام کرد که در این جنگ شرکت نمی‌کند.
دونالد ترامپ تفاهم‌نامه پایان جنگ با ایران را در کاخ ورسای و در حضور امانوئل مکرون امضا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76509" target="_blank">📅 17:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76508">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXfRjKyGSsu0RxMDgUcyff0giq08XbtubTsF46NnN4N4XWSiJ4aJH8JC7GPmG2w7cwrm5jIehg8dCjS-spSPdfxboRr-1g-FHRSa5mJsqNYveOTGXuBKYsNcZuOqW1fjj_1TIlBKWhwGvkyC6yBALFF1SfDrL_KJ-hvnI8kt0GawZ2VJag_AGNRYHlwRuwCHxjj5b_EsToNpMkn28ZsxUg16l4Hqaap6zGDh2oNDCHxbMbZwADdzSN3EDU42iFQTTpBU5lob2E-DNSq-1oH2TBwrzzsE9-t5UoG_ajBmFU4MzEuftY9Ywx6cviYxdKTrdcAq7ULG7wX2JpEZzZwOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال از قول منابع آگاه گزارش داده که طبق توافق پایان جنگ، ایران حق دسترسی به شش میلیارد دلار منابع مسدود شده در قطر برای واردات اقلام انسان‌دوستانه و غیرتحریمی از خود آمریکا خواهد داشت.
به گفته یک دیپلمات آگاه از جزئیات توافق، این منابع مالی به‌صورت مرحله‌ای و در بازه زمانی آتش‌بس تمدیدشده ۶۰ روزه آزاد خواهد شد و تنها برای خرید کالاهای آمریکایی قابل استفاده خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/76508" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76505">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnUmlfRfE7j_Ygbf6MqKLIzA3ra3wKCNRnlhfo5BNS4787dvzU3nMoSwLHPoBFihFDlR4Nozr9fCU-40CpSprOv7QHU2tfQQdok5tUN2GifFH-MeE2Ki3bixCGap-G9_WygcU4CiSapIC-2X0J1kYxJV7A6p26C6BN7XIk0vTB0uBz_jE2iUa-p86Ufi_HehWPr9POuy4PZrzmUAyZ1kP5m7s7qIrNCCesNq7fOMEntiXl7CQWowdyXPZOdBqRYL89ocl1ilCkCtlAo07VvgBIDscPPu-rq93wKjc7kWvNplu32j_DZiDZvJLoU15RL27o-bvDhDLbYlRs2UW99UIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7B5adxXDkOnf34Gjm7gaKUJ18tLDOQa03BQAFEgwinie0llFWfbaSnTXsnH8RQmK0gKUMrtZ3_8wXDTEHS8xGVvUDrgWHJMgHfQ0AcUz9GL1y2zII0_8phuBaFJCINMhQZQSN5iFLGvSQI9kKjhWO67E_r3I0zw18peA_q3e9cx7iblVCgiZKCmtGhEQ3RDj0so7rCJFP_A9tCNuU-owqCMLYiax_iJBTOSKAWVnVFtDWVCGmZsrFOq5Ur4-hqMN1dzpeQUCPrsIYHHODzXRnc5v05qQAVuge2O215wUiAaxgVHz55WlCzmKcdj96PHMA9p52eqEweXkGufgw-2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_lCC6BvFUBYDhIuOPfrrAPuRER86oSVlPIy1jSV3qxNXhkWHe24Xckp2Q-o5TmJmOqFuSRCY0s-I0WHTmXNlo-RdeIYyqkbRFKn2G46I2yXfYTZSkx2UYxvs5pNAzcwkb32ZxPdhfguCx1z7-mnkT9d9RUiba1C0uII-TRjQMyk6YDLT7faP44i5nn2R_8TWsSFHhF3fdc2m5rBx6myZH3IiYvriTGzR8-Kz6oCbApHQK4Q2AS4gGipDtTtW60Yx6aRUjrctsH084x0N_Pt5K4hRtLvvtos2lQFMkwkG9fl4mExmFeND_HTZxLtS9E1N0ieKrqfEmNdSaSN2AaxQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بيكر علی حسن‌پور را بعد از ۱۰۴ روز به خانواده
‏تحويل دادند
‏
🔸
⁧
#علی_حسن‌پور
⁩ در ۲۵ خرداد ۱۳۸۸ در خیابان آزادی تهران بر اثر اصابت گلوله به سر کشته شد. خانواده او پس از ۱۰۴ روز سرگردانی، سرانجام پیکر وی را میان اجساد مجهول‌الهویه پزشکی قانونی کهریزک شناسایی کردند.
🔸
اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است.
🔸
علی حسن پور یکی از این افراد است. سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/61687/ali-hassanpur
@IranRights</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/76505" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEjUZ-unQsvHMMQMn8nIUBR8ksdjL12TcycZv5EMvAHnmDoMNb_PAsZbJygSUAg1Saxx0_hFY8z81qZzecNIPBMdZ5P2P-8QUajPFu1_66XXrOb-rcQR4CbOoD1502MUmW9WGE03rR4bHro9qAmQKGHCkV9DkUJZdiJzedSOYze8RVPMX8GVImQk8Wd46ivROxtnsWo8v6rWfKU37yhhbBC_HZlqZ9Ep3KZFBz0qaVlDmSqiC6X0CIBI_d04x0cPFTLRrdmRjIduW_1zXkT6Q9IEabEUcw7eQ_xrXoX6RSVP9FWpb3zaEG6oaVOnZ852tyAYZDFGe4AP6GWHD3T9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ملی لبنان می‌گوید در حملات اسرائیل به شهرک‌های شرقیه، حاروف، کفررمان، کفرجوزو کفرصیر در جنوب این کشور دست‌کم ۱۶ نفر کشته شده‌اند.
به گزارش رسانه‌های محلی لبنان، از ساعات اولیه بامداد امروز، حملات توپخانه‌ای ارتش اسرائیل به شهر نبطیه و مناطق اطراف آن ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/76504" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfzzYXy5Zjq9A_pcav2qsg_yoUDi7XK9Q1zTFRs4CZJvPtZBj4C2bV3aUvymr7xbNUp4f5e1si6ob6n_eP9_C6trrMF1Yj77FcwEJHHjYzJS5oi0lDLJ3GnlI5wh8Eq2hDXTxN9YpO-t73UAwNeI-x0SDMdDozHo7zQwiDHknlghQnXnL0RhTdAOQ5X7waDqKcfq9DYyN6gprFXCRkRRUeT7aLuUA5DccuCoCiR32Ki8ijTwf1Tnr6u3rQt_iZnnwN9wZ4Xvun_6xUSVfeVJaQV-9TCZRLcnAAswoz84_uEg1u0eihtl_zPn1U9jkwXPy8w2DCQtGRetwhu3_N3gyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی اعلام کاخ سفید مبنی بر لغو سفر معاون دونالد ترامپ به سوئیس، وزارت خارجه این کشور اروپایی رسما خبر لغو سفر هیئت آمریکایی و لغو مذاکرات تهران و واشینگتن در روز جمعه را تأیید کرد.
لغو آغاز فوری مذاکرات بین دو کشور متخاصم تنها یک روز پس از امضا و رسمی شدن تفاهم‌نامه‌ای رخ می‌دهد که یکی از مهم‌ترین بندهای آن ۶۰ روز فرصت برای مذاکره درباره فعالیت هسته‌ای ایران است. قرار بود این ۶۰ روز بلافاصله در روز جمعه آغاز شود.
اما خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز پنج‌شنبه خبر داد که مذاکره‌کنندگان ایرانی پیش از آغاز دور بعدی گفت‌وگوهای صلح نیاز دارند نشانه‌هایی از اجرای توافق موقت از سوی آمریکا مشاهده کنند و هنوز تأییدی درباره سفر هیئت ایرانی به ژنو وجود ندارد.
در پی این انتشار این خبر بود که سخنگوی کاخ سفید هم در بیانیه‌ای که پنج‌شنبه شب منتشر شد، اعلام کرد ونس و هیئت آمریکایی آماده بودند به محض نهایی شدن برنامه مذاکرات، عازم شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/76503" target="_blank">📅 17:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ueUuaMa2tovaTgzlFJXtqDgpXdyrrGYpShe-KeLerlw3JaRFdfvuv6A9jZctgRKGWbpllLhQmkgvnrKjWiIq_JZiLdkvMUncbC3ISJ2TpQ4ympvGLmbjrTqBl8M4Yiw6OZRjygrU_w4e1flVK9XTkYGd52p-UdCx_mUQOql7m53wJxFjcCQvqmLf0CNHo9zgz1U0eSBODzcHudFBr9Fieauw5XPfHnJZQNlL7O1rp2eHflOcB5abtp0irYNTWgClPCO1d-NxwryEem02Etul-fJ9uFAShbSuDjTJJgUa68Eewf4m4jgtEb0Gv97746efhfU7mkegd44RbYW06fXm9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود قنبری‌راد، متخصص امنیت شبکه و از کارکنان یکی از شرکت‌های تهران، با اتهاماتی از جمله «اجتماع و تبانی علیه امنیت ملی»، «جمع‌آوری اطلاعات طبقه‌بندی‌شده» و «ارائه اطلاعات به اسرائیل» روبه‌رو شده است.
بر اساس گزارش‌ها، محمود قنبری‌راد، شهروندی ۴۰ ساله و متأهل، اردیبهشت‌ماه سال جاری در منزل شخصی خود بازداشت شده است.
یک منبع مطلع به دویچه‌وله گفته بود که او هیچ سابقه فعالیت سیاسی یا مدنی نداشته و به‌عنوان متخصص امنیت شبکه مشغول به کار بوده است.
گزارش‌ها حاکی است که او در تماس تلفنی از زندان، پرونده خود را «ساختگی» توصیف کرده و گفته است که برای پذیرش اتهامات تحت فشار قرار دارد. همچنین اعلام شده که وی از زمان بازداشت تاکنون از دسترسی به وکیل محروم بوده است.
بر اساس اطلاعات منتشرشده، محمود قنبری‌راد ابتدا حدود یک ماه در زندان اوین نگهداری شده و سپس به زندان فشافویه منتقل شده است.
همچنین گفته شده که او از نوعی اختلال عصبی رنج می‌برد و خانواده‌اش نسبت به وضعیت جسمی و حقوقی او ابراز نگرانی کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tbjNhmio1kKGClwpghCSlpNSNMWyFN6Np4WiHcMYsv4Y36NdwG_AFdzizxJzDY_eD-LWI_i-NAgK623jDLfP22ztpHkhub2Dy68tOTNT6qlM-AhPbpupgOkHpPuL1ff2GJeUzedrJBOhKI34LdecSDgOZ_QUKTklCOEJDoFSJo_mpoTNoy9P2fIf8aTHcU_bydDGctRWeBfo1mYdnF7GK-9arqqvdNs8Vt9IEnuSGP3WMQGUav1dDGQL5VKZTiy4Iv25z0dVTEL1BCsH6Kraw8l10vwD-cuWJ_T7-85D8OxQaouhvNwPpY9nMo1B_xhTQ6euSHtavHAQkwWf7t4kuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از امضای تفاهم‌نامه میان واشنگتن و تهران  را
منتشر
کرد.
این تصویر مربوط به مراسم امضای تفاهم‌نامه در کاخ ورسای فرانسه است؛ جایی که ترامپ در حاشیه سفر خود به فرانسه و پس از پایان نشست سران گروه ۷ (G7) حضور داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76501" target="_blank">📅 05:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q07l1wQlvkm1w8vboYcnvjkgQoBsykc0Zpk7kW4BkdPlYvjmkasQtyMwd7bCOvQQwSIJt8KZoPaQSdML38Cwfm_-A0VL0rY08Ds8o-GWL9VMCyg4_bhUQ8mI0dK0jMyDEbEiNP70UjdF3NVQ3rxPzTn47kwzCU8UNGMOOPX9Zi8apt7tVK83WCv6L9oxzkuG6wQFxrJsm25s9lJDWtKag5aPp4ydObfrwDstknJSIOwbSWB4u2IPNwyW6IARzmVLWB2bL4e_BOHifClhaf5vbm0WU7L73ONskYHgMDCSYn1wGqu3CulLtXdbDmWGPYJhq-nTLXXuDcBVOUajXgiDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در«گفتگو ی تصویری با اکسیوس» گفت یادداشت تفاهم امضاشده با حکومت ایران را می‌توان «نوعی تسلیم کامل» از سوی تهران دانست.
او این اظهارات را در پاسخ به پرسشی درباره تفاوت میان خواسته پیشین خود برای «تسلیم بی‌قیدوشرط» و مفاد تفاهم‌نامه مطرح کرد.
مجری آکسیوس در این مصاحبه به ترامپ یادآوری کرد که در آغاز درگیری‌ها گفته بود تنها «تسلیم بی‌قیدوشرط» را از ایران خواهد پذیرفت، اما یادداشت تفاهم امضاشده چنین تصویری را نشان نمی‌دهد. ترامپ در پاسخ گفت: «خب، احتمالا در واقع تسلیم بی‌قیدوشرط است. فکر می‌کنم همین‌طور باشد.»
رئیس‌جمهوری آمریکا همچنین با اشاره به جنگ اخیر گفت ایالات متحده ایران را «کاملا از نظر نظامی شکست داده است». او با تمجید از توان نظامی آمریکا افزود واشینگتن توانست محاصره دریایی موثری علیه ایران اعمال کند و هیچ کشتی‌ای نتوانست از آن عبور کند.
ترامپ همچنین گفت پس از جنگ با ایران، محدودیتی برای قدرت خود نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76500" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d3owxpPctKehkPnpo6d3OYt4VNHx0F21DoUIeeGOF0fyI2YeA1lnodIZKHadL97ZHyCxd5tFaNWBggei1sfPYdBcQWJInUCp5vrWyv0k0wp7l4pqv9K_z08I-l_zFEuQlt8-3mp6xWUAvgrsyQ3fOdXYlO6yVm5dDXFIj6VSziG5WEVB_yASvffJ0zampyJEeLmU99lTHl0IJV03v4K1kBj1qGgZPtbdfYfBOitXSVpu6JxAtHHTYQfUp9iqFdLolBkfPtoSnYiYk7KHKn6beJit2-VfcsggYdjfV0ZaSj_YG7-b6Zb9GsLq7W46vefr9oQwHE1R0vtD9_FStZgB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر جی‌دی ونس، معاون ترامپ، در اطلاعیه‌ای اعلام کرد که او سفر خود به سوئیس برای شرکت در مذاکرات با جمهوری اسلامی را لغو کرد، زیرا برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و تدارکات و هماهنگی‌های این مذاکرات ساده یا قابل پیش‌بینی نیست.
در این اطلاعیه آمده است: «برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و هیات آمریکایی آماده بود در نخستین فرصت ممکن عازم شود، اما تدارکات و هماهنگی‌های این مذاکرات هرگز ساده یا قابل پیش‌بینی نبوده است. در حال حاضر، معاون رییس‌جمهوری امشب عازم سفر نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76499" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e-MOsfpoT8-zuZgxb9yfvLuBvDgN4pl5yUzJbCdLerohkPRKW-xcUd9eyCHulmtwuFXkTMlnuaRNkyMfSYN3sejLDWoEo7hEbR5IDkxqn2tUvJLONebldGh0eVlQvlD28R6XFyKRnq7wT2vG9sapxC93r8d8FChwMZj2ErtQydNebZrw6a8PdN8YXSYl4TrHpexJv98xsFrPpKown8Q2l9AxQ1BlhsAzkl_EPa-Hn589qHw4U059bzVMH-RXfrDed48gBuV4B62APzKnANVIdJlGgQ9U2J0WDyIqk7G5vWmRdsQetNG_krAGILPhNeAS-0Ry8XZntQu5aIrNCIggLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آسوشیتدپرس گزارش داد استیو ویتکاف، فرستاده دونالد ترامپ، پنجشنبه‌شب در نشستی غیرعلنی با قانون‌گذاران آمریکایی اعلام کرده است تهران از آژانس بین‌المللی انرژی اتمی برای بازرسی از تاسیسات هسته‌ای خود دعوت خواهد کرد و روند شناسایی محل نگهداری مواد غنی‌شده را آغاز می‌کند.
بر اساس این گزارش، ویتکاف به رهبران کنگره و اعضای کمیته‌های امنیت ملی گفته است تفاهم‌نامه میان آمریکا و ایران هیچ توافق جانبی نداشته است. با این حال، تهران و آژانس بین‌المللی انرژی اتمی نامه‌ای جداگانه تنظیم کرده‌اند که در آن دعوت از بازرسان آژانس و ادامه همکاری‌های نظارتی مطرح شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76498" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOCfv9-aswVFwZX3Nib9STYgwVWjEmTftAGGalgyYeNPAogrZ3MI6Im0VCdVpwNoSceDrSgsuaooy72rRFtMZAAH34B1c6FSpYuM2tyMFmIOk0vqA3GkCp2Y1MRL8FNWQnAjAd6Faau36pIS8WxpWsAaQLHJESFmTIjXcNn__h39VJAmHG6HHw1uzETdu4XfBTldFfC2MioCfPXmIis6GuMqHBMRI5kFlnpeiREjakY1gplzREcAWzMUTahz5Wy40b3C-wphs_V4VV08hWSrEZ0rh47VIaFgzl24UcfT457SYPkhYPCadN8zPg3fVlh8tN6bYepRTTK_OGxQenwesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجه اتحادیه اروپا، گفت هنوز برای بحث درباره لغو تحریم‌های اتحادیه اروپا علیه ایران زود است و این موضوع پس از دستیابی به یک توافق هسته‌ای با ایران بررسی خواهد شد.
او پیش از نشست رهبران کشورهای عضو اتحادیه اروپا به خبرنگاران گفت: «زمانی که شرایط فراهم شود، کشورهای عضو درباره مناسب بودن لغو تحریم‌ها گفت‌وگو خواهند کرد، اما هنوز به آن مرحله نرسیده‌ایم.»
اتحادیه اروپا در حال حاضر مجموعه‌ای از تحریم‌های چندجانبه علیه بیش از ۷۰۰ فرد و نهاد در ایران اعمال کرده است که شامل ممنوعیت سفر و مسدود شدن دارایی‌ها می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76497" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwLlD8efrR2421qpqhfWu0CBj_6X7Z1pmD_ywUb5YmV3jOHOGUein8gSqQIEaBR4-Te-QnK4vGCmY31wZFHhYft2ivOmBf8nksrF2MhanB-DuHfdN6n8FoXEcJPNnpXjO7co5h4QMQjmN829CZUf0btDnT79DiUvW-KXN2chUzyihWd64flj0PgVkWg9BZ0F2fm3gLa8-7lM2aJZRa4oU8l6CeK7S9YJ5GJZM3kfLpT6Yr_W0vt8iTvc2v5r6FL5SmiyoVlLAnzjUj_KuwqlETQOGKTgMqYohzFOk_xLJALJ5sGZ4zFMg11ISKUnve3K22722BHA5CkLh7aaErZozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین به نقل از یک منبع آگاه گزارش داد هیات مذاکره‌کننده جمهوری اسلامی به دلیل ادامه حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس برای آغاز نخستین دور مذاکرات ۶۰ روزه را به حالت تعلیق درآورده است.
المیادین افزود: تهران پیش‌تر به آمریکا و میانجی‌ها اطلاع داده بود که پرونده لبنان در ادامه یا توقف مذاکرات نقشی محوری دارد و هشدار داده است حملات اسرائیل تا عمق ۱۰ کیلومتری خاک لبنان نقض یادداشت تفاهم و توافق چارچوب است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76496" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qpYzFBCcG5GEzdudDqEB2FQi9gImWTTBtyHQ3gO6ijhvW-KKkTwgGPu2G8z-lxO66IoI3ELT1BTR3oqJiT6SfCgBq9iD9NJLVlkXJWJraqoebjeFUjbTqcOp8siSFS6aAlC36CmQ4Q63ldfGSfEKO2oCsMOlrqxQC0LoJieYpTD2pZbzqpWrLMutbss2aQJdnPMJAgARkHk8BFBxDbBsehTbVqbktYqUoSgyedYdN3raxJSizhd-bpgrDkzzeH3cctYEwbdvnQkXFOfBJzMupSvxaEIcoE8EdITp1o31g-2ZAuJ2qaP1PFVNe4FhwMvbcXd3b-BCWrqLga23iejnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت کاخ سفید:
رئیس‌جمهور دونالد ج. ترامپ تهدیدی را حل کرد که واشنگتن چهل سال صرف مدیریت آن کرده بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
یک پیروزی برای آمریکا.
🇺🇸
WhiteHouse
ترجمه با هوش مصنوعی به تصویر اضافه شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76495" target="_blank">📅 22:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a8WvE1PButaqbWIw2mOfZstlPe4tlNcBr5NFFtglCWwhp6T-TquVM3xoYiqFinlGJteXfkoEBwyyIRZVRL2LQh6tOaYep2KIyu_qBLMp3gHrFmTPGnJZ0YYKgQuVOVUfsKHIHHiMItVrGhnT3eqUQdNIiGOw53IDjjCroKT-PpA7nkcCVEZZ0MfOdXOccDWNJ0yV7Oye5fBkwW7nY5kNEbjbUfZtAKBkudtM7i4khXM0vSvsJ3_sd7BSeTwL3r1XqJAyZ2dVwjUqXgQYtnTP1M_vq0a5SCGWbk8T1Qsp3gBl3lfpKm64a1by99juymg3YehxRLVZKlsEx1lwnIoOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'
بیانیه شورای عالی امنیت ملی
'
منابع حکومتی:
🔹
در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (PGSA .ir) ارسال نمایند.
🔹
به موجب یادداشت تفاهم اسلام‌آباد، به مدت شصت روز، هیچ‌گونه هزینه‌ای از متقاضیان اخذ نخواهد شد و این هزینه‌ها توسط دولت جمهوری اسلامی ایران تأمین می‌گردد.
🔹
بر این اساس به مدیریت آبراه خلیج فارس دستور داده شده است، در جهت تحقق اهداف تفاهم‌نامه درخواست‌ها را با سرعت و اولویت رسیدگی و پاسخ دهد.
🔹
با توجه به شرایط خاص و وجود برخی مخاطرات ایمنی در مسیر عبور و به دلیل لزوم حصول اطمینان از تردد ایمن و جلوگیری از حوادث دریایی، لازم است کشتی‌ها در مسیر و زمان اعلامی به آنها عبور نمایند تا به تدریج، امکان تردد افزایش یابد.
🔹
ترتیبات اجرایی و جزییات فنی عبور از تنگه هرمز از طریق مدیریت آبراه خلیج فارس اعلام می‌گردد.
🔹
در خصوص سایر موضوعات، از جمله مین‌زدایی، اقدامات لازم مطابق بند ۵ یادداشت تفاهم اسلام‌آباد انجام خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76494" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76493">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FEhnk80r5jfjrSuLOI7s1RJFrZ8AJRfnmywtxSuon355Y9kPcRY7dfXQFyqKJTkdRrdOudAcDQw5fy6cPuD8izJYmPAlizvEaqQxxOLiloKDiXJHMzOUHMXhQ2GQZ-cBIs3xtEWGaObkFqmjEJ1njjZww5eOGgXBxbnZTn8LZyeOzXJS4zZUAE-QvWmHBdHcg9y2OyDNPvT2PDeHrP3Edd8E5PsCLc_-Ov0mPniVkQaaG2J-u_xJiLgzFxnhRP1QGoygG50IOLX0FkxBPZNX3IHNL22WBHdoQ1-54nKR3hCkQBiWlP8c_EGPxaH83qUxVculblB934DLccITgS73Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: انتظار آتش‌بس کامل در همه جبهه‌ها از جمله لبنان را دارم
ترجمه ماشین:
ایالات متحده به صلح متعهد است و ما همه در منطقه خاورمیانه را تشویق می‌کنیم که به تعهد خود برای فراهم کردن امکان پیشرفت زیبای مذاکرات ما پایبند بمانند.
بازارها از آنچه در حال رخ دادن است استقبال می‌کنند: قیمت نفت به‌شدت پایین آمده و سهام به‌شدت بالا رفته است.
ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76493" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPourostad وحید پوراستاد🔷(Vahid Pourostad)</strong></div>
<div class="tg-text">« پیام منتسب به مجتبی خامنه‌ای در واقع نوعی فاصله‌گذاری حساب‌شده با تفاهم ایران و آمریکا است. مجتبی خامنه‌ای رهبر جمهوری اسلامی اجازه امضا را داده، اما مسئولیت سیاسی و اجرایی آن را بر دوش پزشکیان و شورای عالی امنیت ملی گذاشته است.
پیام همزمان رو به داخل و بیرون نوشته شده است. در داخل می‌گوید رهبر با رضایت کامل وارد این مسیر نشده و دولت باید پاسخگوی نتیجه باشد. در برابر آمریکا هم این سیگنال را می‌فرستد که تفاهم، زیر فشار ترامپ و دولت او به‌معنای عقب‌نشینی قطعی نیست؛ بلکه مشروط است و اگر شروط ایران محقق نشود، موافقت نهایی رهبر با توافق نهایی هم تضمین‌شده نخواهد بود.
در واقع متن، بیش از آن‌که اعلام رضایت از توافق باشد، تلاشی برای حفظ دست بالا در مرحله بعدی است: هم مسیر مذاکره باز می‌گذارد، هم امکان عقب‌نشینی تبلیغاتی حفظ می‌شود, هم به واشینگتن گفته می‌شود که فشار بیشتر ضرورتا به انعطاف بیشتر ایران منجر نخواهد شد»
@pourostadv</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76492" target="_blank">📅 22:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b1VYNkIjqoj82a4G6FMv9oMfqlxa9R7gnBy61MNy_GhI4sbpg32C-ncNyQoG_kzwMlsZ5xK-dORhX4K-JVjdATDm3VXH_JnDLo6OsBXylT5HJ4p4nRxSdcNBkJWjfDZMj3f1v97OclSQgnXXC6HjAiL35Ybebo1ai_9RzVwjxJTUksmzXTxVzJasoqT1WUs6uck2JENEhR8ky2hwzY76u9kahbrT47kM2jJufwRnPXwttCudE2DWcYYWNyVe-80tRYWaxfKkTR7QgNv_CVfrWY8fdmmKLoUCEwXiDbP-Xka7JdgcR7_Dh-bgbTEe9UoaVpv4dEtweNhn8FQ6dcYszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول
گردن‌نگیر
جوان شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76491" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RENfNAkQguK5XfHokmYvhSuHonZXnitAeEL5Cw9I8mM0jW1sLB13FumUuaHDpR3yIbG0BpvFU2XAAJUrXJRXzGh_eTC9mwYwwlgI88K98Ce5TySFGdbTf5vF8_2SWXj-shRjdF231V84l-e5-m47Mr0XnMDnos2fD5-4topKoHHjroijUiY869tfvPX5CregPdY4UTsDp6mwysel6oFRUoMaygzZoj9ht8p2FPpO6SqdpFh_MBLIxhNYt_ZctifTCZEvK03FfdIRry-G82mnNDrlHPZPKwPX_oitpSSxO6HqaZmpMUcFAfLP-pi7A6nPYtcXRPY89FMnnByT0OnhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پنج‌شنبه شب متن پیام مکتوبی منسوب به مجتبی خامنه‌ای را منتشر کردند که در آن رهبر جمهوری اسلامی درباره امضای تفاهم‌نامه میان ایران و آمریکا گفته است که «نظر دیگری» داشته و مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا دانسته است.
در این پیام درباره توافق با ایالات متحده آمده است:
«بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیت ملی از طرف خود و سایر اعضا در پاسداشت حقوق ملت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه آن را صادر نمودم‌.»
در این پیام به تفاهمنامه اخیر به عنوان «تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و آمریکا» اشاره و گفته شده است که رهبر جمهوری اسلامی و مردم از این لحظه «منتظر تحقق شروط گفته ‌شده» خواهند بود.
در این پیام آمده که مذاکرات حضوری آینده «به معنی پذیرش نظر دشمن نخواهد بود.»
VahidOOnLine
در تیتر و متن نامه و خبرهایی که درباره‌اش تولید میشه بسیار تاکید دارند که این تفاهم‌نامه‌ای بین پزشکیان و ترامپه و نمی‌گن بین ایران و آمریکا
در واکنش‌ها از کوچک‌نمایی نقش
قالیباف
یا محافظت ازش با سپر کردن پزشکیان هم میگن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76490" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h6wfaSbuvwsZmwEdXPDRkehkH7oBI9idiit_JhJIOmwep5fDZ7PmAlUufjIDx6qhtl2HKqeDCEdUTAhRl9ICSUKU9pXy-RScxvh-ZWBEZUomdKZZBscJHT522agdFP86RYPUCO6AFqbadVjmwiq-l_kynfBwCzKIv7CiiFnFHBpDnyHetVM4T5JByGm_JmFWsMs7GeDMz6Q7aDz0NZflNK7t56EONzJ8zZ_Cjen5B0dYsyqLmMVB0LZZ2XS2CxRT9HiHsUyIYwW_Bbyvtzl-ExxqvtL_BjGlVWAJIXej7aN06McgkE62CReGZhZFh99uONWGAHNmaJugyW6fJZH-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!!
رئیس‌جمهور دی‌جی‌تی
(توضیح: Dumocrat بازی زبانی تحقیرآمیز با Democrat است؛ از ترکیب ضمنیِ dumb به معنی «احمق» و Democrat. در ترجمه می‌شود چیزی مثل «دُمکرات‌ها» یا «دموکرات‌های احمق» آورد، بسته به لحن مورد نظر.)
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76489" target="_blank">📅 20:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0f7ZnETqTgeQqeXoVoO0bRAgzA2zsa4kGvDoETvwyjS4ptlofqkay3tmbcnSSi_eHKlEkTdXrXriXSX6cD8XiUJihNj1HFbnbcrjZRhScG0vrH7as7Xu6WlTwga0JqEZ7QVdj_ZxL_0rBKgGH8wyv_3yPABmUTlssxr4Aa0isjzVbvVN1Tp7lIzEXiPBfCk20ffSoiXL77OcU9PVbe2NeldaQzlljfWSlCrvgUhbgDHsMfFKhwl9YHa5ya7-KhNscwi_E7x0yDMtWSHNJLaXPv0I-2TKANq-wQhwrp4dBz_DA2e71Mirflcl4YzA7_4qc6K3W_mCdTYj0ZUpnCyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام پایان محاصره دریایی
پست سنتکام، فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
امروز، نیروهای آمریکا مطابق دستور رئیس‌جمهور، محاصره‌ی همه‌ی رفت‌وآمدهای دریایی به مقصد بنادر و مناطق ساحلی ایران و از مبدأ آن‌ها را رفع کردند.
نیروهای آمریکایی مانع عبور کشتی‌ها به سوی بنادر ایران در خلیج فارس و خلیج عمان، یا خروج از آن‌ها، نمی‌شوند.
همه‌ی تلاش‌های نظامی آمریکا برای اجرای محاصره متوقف شده است.
کشتی‌های بزرگ نیروی دریایی ما در منطقه‌ی کلی باقی خواهند ماند تا اطمینان حاصل شود که همه‌ی جنبه‌های توافق رعایت، اجرا و به‌طور کامل لازم‌الاجرا و مؤثر باقی می‌ماند.
CENTCOM
البته سنتکام ننوشته خلیج «فارس»
🔄
آپدیت:
توییت رو ویرایش کردند و در نسخه جدید اون جمله مربوط به خلیج فارس رو کلا حذف کردند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76488" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76487">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QH5TxSrs9wcZhNffn7XRYFFDskLS3pH0wYDO63YDR4NMGl-LMHPtTpK7igZspINZj-ry7n9faDoFc_bSJ695FVpAt7VCxPvtfFUbY4RPezysOZ2Js15-gtyVK_X17T8jy_TE3bb7R82XWRsNW1FQBITEVMRcxo6f4PYwTSi5MfmCXEZsmdyqtAfaL-NjHz7ZGB4Y2g-DzOc6vcog3YgLFYLVzuKryQyV_fiNYgrl69VzzF2KQgDmKNpSqEWkOdW7nKrjUOpJfRSJqTus5po48B75uIpdOmw-xCt3YxyH53SHAv1YqTvG_D0RnU2-Bj43WTBjLQqS6D17tLEb4N4LBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره: ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار. realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76487" target="_blank">📅 20:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=mpJX26zNbdVTrk31urJxGakgoNkuPGc-qQuQWYAyyoKrkZQXnAi3DxCqFN_sv_QdUUWltX1EXcZO4QoY6jnEVTLrFAwIBhXsz1QC8DW9y5Sm5Vh0EOZ1HF8641iiVF72YfKzF-zIuCkjhUTGBegR6ClS0XHACKrD-16uyE2cMkdJkyHg08hFyeYTgnu4Ouv8zoZv9OG-f94JjF8wAgj4Yjr0bCWrSjbzziS-d1Kxb1T560lhbJ6LN2CYGJ-yhNPZyWEguZk1QOOx5weQl2_lRDDgEeyR4O2wvfEvkxNf_cs19NAvKvBUOOGO2ohQ9AVg6NlOHdLAu33e24ZQowqgWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=mpJX26zNbdVTrk31urJxGakgoNkuPGc-qQuQWYAyyoKrkZQXnAi3DxCqFN_sv_QdUUWltX1EXcZO4QoY6jnEVTLrFAwIBhXsz1QC8DW9y5Sm5Vh0EOZ1HF8641iiVF72YfKzF-zIuCkjhUTGBegR6ClS0XHACKrD-16uyE2cMkdJkyHg08hFyeYTgnu4Ouv8zoZv9OG-f94JjF8wAgj4Yjr0bCWrSjbzziS-d1Kxb1T560lhbJ6LN2CYGJ-yhNPZyWEguZk1QOOx5weQl2_lRDDgEeyR4O2wvfEvkxNf_cs19NAvKvBUOOGO2ohQ9AVg6NlOHdLAu33e24ZQowqgWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی در ایران که ریاست هیئت مذاکره‌کننده ایرانی با نمایندگان آمریکا را برعهده داشت، عصر چهارشنبه در مصاحبه‌ای مفصل با تلویزیون حکومتی در ایران به نهایی شدن تفاهمنامه میان تهران و واشنگتن واکنش نشان داد و آن را موفقیتی بسیار بزرگتر از مقابله نظامی با ایالات متحده دانست.
او در مورد دستاوردهای ایران گفت: «هر آنچه را که با اقدام نظامی می‌خواستیم به دست بیاوریم، چندین برابر آن را از طریق مذاکره گرفتیم؛ اصلا قابل قیاس نبود. هر جنگی ممکن است پیروزی‌هایی داشته باشد، اما اگر این پیروزی‌ها در نهایت به یک سند حقوقی و سیاسی منجر و ثبت نشود، هیچ منفعتی نخواهد داشت.»
او در بخشی از صحبت‌های خود درباره انتقام کشته شدن علی خامنه‌ای گفت: «همان‌طور که خونخواهی امام حسین، ظهور امام زمان است، خونخواهی رهبر شهید هم آزادی قدس است... صد نتانیاهو بند کفش امام شهید ما هم نمی‌شود.»
قالیباف در مورد وضعیت تنگه هرمز هم گفت: «تنگه هرمز هرگز به شرایط قبل بازنخواهد گشت. البته این به آن معنا نیست که ما در تنگه هرمز بخواهیم برخلاف قوانین بین‌المللی و مقررات دریانوردی عمل کنیم.»
@
VahidHeadline
قالیباف در مصاحبه‌ای که همزمان با انتشار مفاد تفاهم‌نامه تهران و واشنگتن از صداوسیما پخش شد، گفت برای حضور در مذاکرات با دولت دونالد ترامپ تمایلی نداشت و به دلیل نقش ترامپ در کشتن قاسم سلیمانی، «کراهت شدید» برای ورود به این روند احساس می‌کرد. او افزود که با وجود این مخالفت شخصی، به درخواست مقام‌های جمهوری اسلامی مسئولیت مذاکرات را پذیرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76485" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76484">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGHmDV6xnESEpL4GLvz2C_luMOnqH_1y01OX2uNNqDDtwycQwuLt9t2nnH4RLxnDJdU5hpRnxONYACXqZPAZ-FcFEJvCi-cDLYU_nEAHeFgAH61Sr1nUlgybgEGSXDAdsRve9rFELGRINe7rfXVMBg2XEmLVM_WJWOGKFpQ6xrxXCz-e5boY1KkKZMvfuIVShOD2g_0_2gB_wiHymaWcP2TsFWvvfRTltpprzx1Y3ka9J_bPTV76IBcCnICtY_LVLJFeAkq5H2_yJefgfaOG-ogBcTlkdj2dYkBv8BrP6rVeTOga0rf2W2HFkZOVMIHm8Xy-1Tlpxlh3xEd8AcPNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، یک روز بعد از امضای تفاهم‌نامه ایران و آمریکا در نخستین موضع‌گیری خود اعلام کرد که نیروهای اسرائیلی از جنوب لبنان عقب‌نشینی نخواهند کرد و تا هر زمان که لازم باشد منطقه حائل امنیتی خود را در آنجا حفظ خواهند کرد.
این اظهارات پس از آن مطرح شد که دونالد ترامپ، رئیس‌جمهور آمریکا، طی روزهای اخیر از عملیات اسرائیل علیه حزب‌الله لبنان انتقاد کرد و آن را بیش از حد «تهاجمی» دانست.
نتانیاهو در یک مراسم رسمی گفت: «ما امنیت و رونق را به شهرهای شمالی بازخواهیم گرداند.»
او افزود: «این امر مستلزم حفظ منطقه امنیتی در جنوب لبنان است؛ مستلزم آن است که آنجا را ترک نکنیم، تا زمانی که نیازهای امنیتی اسرائیل چنین ایجاب کند.»
رسانه‌های رسمی لبنان پیش‌تر گفتند که در حملات صبح پنجشنبه ارتش اسرائیل به جنوب لبنان، ساعاتی بعد از امضای تفاهم ایران و آمریکا، سه نفر کشته شدند.
از سوی دیگر، یک مقام ارشد اسرائیلی پنجشنبه به خبرگزاری رویترز گفت که اسرائیل «در حال انجام مذاکراتی سرسختانه» با ایالات متحده دربارهٔ موضوع ادامه استقرار نیروهای اسرائیلی در جنوب لبنان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76484" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شروع سخنرانی جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔸
دیشب، ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرد.
این بالاترین میزان از آغاز درگیری است.
🔸
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آنها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است که دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به تعهد خود عمل می‌کنیم.
🔸
شما چیزهایی درباره ۳۰۰ میلیارد دلار یا ۲۴ میلیارد دلار، یا این یا آن عدد یا مقدار پول خواهید شنید، و واقعیت ساده این است که تنها راهی که ایرانی‌ها به هیچ یک از این منابع دست پیدا کنند — حتی یک سنت، به هر حال، از ایالات متحده آمریکا تحت هیچ شرایطی — اما
تنها راهی که آن‌ها می‌توانند از این معامله بهره‌مند شوند این است که کاملاً مطیع باشند و رفتار خود را تغییر دهند.
اگر ایرانی‌ها رفتار خود را تغییر ندهند، برنامه نظامی و هسته‌ای آن‌ها همچنان نابود خواهد شد؛ اگر رفتار خود را تغییر دهند، آنگاه رابطه‌ای تحول‌آفرین با خاورمیانه خواهند داشت.
این یک برد-برد برای ماست.
🔸
در ایران تقسیمات واقعی وجود دارد.
آنچه دیده‌ایم این است که عمل‌گرایان در حال پیروزی در بحث هستند.
🔸
من کسانی را دیده‌ام که به این توافق شک دارند — افرادی می‌گویند ایرانی‌ها هرگز رفتار خود را تغییر نخواهند داد.
خب، شاید این درست باشد، و اگر چنین باشد، آن‌ها هیچ‌کدام از مزایای این معامله را به دست نمی‌آورند. اما آیا ارزش امتحان کردن ندارد؟
🔸
می‌گویم دوره ۶۰ روزه رسماً امروز شروع شده است.
پس بله، توافق دیروز شروع شد — ما امروز ساعت ۶۰ روزه را شروع خواهیم کرد.
🔸
تمام چیزی که رئیس‌جمهور دیروز گفت این است که، البته، کشورها حق دفاع از خود را کنار نمی‌گذارند.
اسرائیل حق دفاع از خود را کنار نمی‌گذارد اگر حزب‌الله به اسرائیل راکت یا پهپاد شلیک کند.
ایرانی‌ها حق دفاع از خود در کشورشان را کنار نمی‌گذارند، اما
ما انتظار داریم که به عنوان بخشی از توافق نهایی، آن‌ها نتوانند موشک‌هایی بسازند که بتواند به طور گسترده کل جهان را تهدید کند،
و این همان چیزی است که رئیس‌جمهور ایالات متحده دیروز گفت. و ببینید، خیلی ساده است: نمی‌توانید به کشوری — چه اسرائیل، چه ایران — بگویید که حق دفاع از خود را نداشته باشد.
🔸
خبرنگار: رئیس‌جمهور ترامپ دیروز گفت که اگر مذاکرات این دور به مشکل بخورد، شما را مقصر خواهد دانست. آیا نگرانید که او شما را به عنوان مقصر معرفی کند؟
جی‌دی ونس: نه، اصلاً. فکر می‌کنم رئیس‌جمهور شوخی می‌کرد، همان‌طور که اغلب این کار را می‌کند.
🔸
جی‌دی ونس درباره تنگه هرمز:
ما هرگز نمی‌خواهیم این اتفاق دوباره بیفتد، درست است؟ این موضوع مربوط به عوارض نیست.
این درباره اطمینان از این است که تنگه‌ها هرگز به عنوان نقطه گلوگاهی برای اقتصاد جهانی استفاده نشوند.
صادقانه بگویم، این چیزی نیست که ایرانی‌ها بخواهند.
🔸
جی‌دی ونس درباره برداشتن تحریم‌ها:
صادقانه بگویم، ما این را به عنوان امتیاز بزرگی به ایرانی‌ها نمی‌دیدیم — ایران... این را به عنوان امتیاز به آن‌ها نمی‌دید، چون چیزی که مانع فروش نفت آن‌ها می‌شد تحریم‌ها نبود.
آن‌ها بدون هیچ تخفیفی مقدار زیادی نفت می‌فروختند، چون تحریم‌ها اساساً بی‌اثر بودند.
در آن زمان، کاری که تحریم‌ها انجام دادند این بود که سیستم مالی ایران را به نوعی به سیستم بانکداری سایه‌ای منتقل کردند.
با برداشتن تحریم‌ها، ما در واقع قادر خواهیم بود کمی ببینیم که سیستم مالی آن‌ها پول را کجا می‌فرستد و از کجا دریافت می‌کند. این یک مزیت واقعی است.
🔸
آنچه به برخی از منتقدان توافق که شنیده‌ام می‌گویم، کسانی که می‌گویند «خب، ایران تمام این مزایا را به دست خواهد آورد».
تکرار می‌کنم آنچه را که گفته‌ام و احتمالاً باید چندین بار تکرار کنم: مزیتی که ایرانی‌ها به دست می‌آورند و قبلاً نداشتند چیست؟ و پاسخ هیچ است.
آنها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتار خود را تغییر دهند. اگر رفتارشان را تغییر دهند، این چیزی است که باید جشن گرفت.
🔸
هیچ‌کس نمی‌تواند حق دفاع از خود یک کشور دیگر را نادیده بگیرد — اسرائیل حق دارد از خود دفاع کند.
اما اساساً، اسرائیلی‌ها، درست مانند همه‌ی مردم دیگر، باید به این روند صلح که اساساً برای آن‌ها و کل منطقه مفید است، احترام بگذارند.
🔸
در انتقاد از اسرائیل: به نظر می‌رسد که ما درست در آستانه یک پیشرفت بزرگ در توافق هستیم، و ناگهان یک انفجار بزرگ در یک مرکز جمعیتی غیرنظامی در بیروت رخ می‌دهد و بسیاری از افرادی که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل قبول نیست.
🔸
توافق هسته‌ای اوباما اجازه غنی‌سازی داد — توافق ما این اجازه را نمی‌دهد.
توافق اوباما اجازه انباشت مواد با درجه تسلیحاتی را داد؛ توافق ما در واقع به نابودی آن انبار مواد غنی‌شده منجر می‌شود.
توافق اوباما بیش از یک میلیارد دلار پول آمریکایی به آنها داد؛ این توافق هیچ دلار پول آمریکایی به آنها نمی‌دهد.
🔸
آنها تعهدات هسته‌ای بسیار مشخصی داده‌اند.
آنها متعهد به نابودی ذخیره بسیار غنی‌شده‌ای شده‌اند که در اختیار دارند.
اما نکته دوم، تنها کاری که ما انجام داده‌ایم برداشتن محاصره در تنگه است — که اساساً آن را به وضعیتی که قبل از درگیری بود بازمی‌گرداند.
🔸
خانم‌ها و آقایان، کلمات مهم نیستند، ما درباره تأیید صحت صحبت می‌کنیم.
🔸
فرض کنیم — دو سال بعد، آن‌ها آنچه را که ما باید در برنامه هسته‌ای ببینیم انجام داده‌اند و تحریم‌ها را طبق توافق آزاد می‌کنیم.
سپس تصمیم می‌گیرند که برنامه هسته‌ای را دوباره بسازند.
البته در این صورت، آن تحریم‌ها دوباره باز خواهند گشت.
و به همین دلیل است که این موضوع واقعاً شبیه یک دکمه تنظیم است: هرچه رفتار خوبشان را افزایش دهند، ما می‌توانیم تسهیلات اقتصادی را افزایش دهیم؛ اگر رفتار خوبشان را کاهش دهند، می‌توانیم آن را قطع کنیم.
🔸
آنچه واقعاً اتفاق افتاد این است که ما یکشنبه یادداشت تفاهم را امضا کردیم. این موضوع شرایط توافق را تثبیت کرد.
ایرانی‌ها به ما آمدند و گفتند: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً این را درک نمی‌کردم—می‌خواستم متن را فوراً منتشر کنم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «باشه، ما تا جمعه صبر می‌کنیم.»
و سپس در طول دوشنبه و سه‌شنبه، در حالی که رئیس‌جمهور در نشست جی۷ بود، شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را تشویق می‌کردند که این کار را انجام دهند.
ما قطعاً به آنها می‌گفتیم:
«ما تمایل شما برای عدم انتشار متن تا جمعه را درک می‌کنیم، اما می‌دانید که ما در یک نظام دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق را ببینند. ما قطعاً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها تصمیم گرفتند که رئیس‌جمهورشان آن را امضا کند، رئیس‌جمهور ما آن را امضا کند، و سپس متن را به عنوان یک سند امضا شده فوراً منتشر کنند.
🔸
اینکه فکر کنیم فروش چند میلیون دلار نفت قرار است اقتصاد ایران را به طور بنیادین تغییر دهد، درست نیست.
🔸
در مورد وجوه مسدود شده، مقدار پول — صادقانه بگویم نمی‌دانم.
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. در واقع اعدادی بیش از ۲۰۰ میلیارد دلار هم شنیده‌ام.
بیشتر آن در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در خلیج فارس است، یا در اروپا، یا جای دیگری.
اما مقدار دقیق پول را نمی‌دانم — مقدار زیادی است.
🔸
من گزارش‌هایی دیده‌ام — نمی‌دانم این از کجا آمده — که قطری‌ها میلیاردها دلار و دارایی‌های ایرانی را آزاد کرده‌اند.
این اصلاً درست نیست. برای قطری‌ها غیرممکن است که بدون موافقت ما این کار را انجام دهند، و قطعاً بدون اینکه ما ببینیم.
🔸
درباره موشک‌های ایرانی:
توانایی آن‌ها در پرتاب موشک به طور قابل توجهی کاهش یافته است.
آیا این توانایی صفر شده؟ خیر. اما به طور قابل توجهی کاهش یافته است.
ما آن مأموریت را رها نکرده‌ایم. ما آن را به انجام رسانده‌ایم.
🔸
خدا را شکر. خوشحالم که پاپ چیزهای مثبتی درباره تفاهم‌نامه ما گفته است.
🔸
آنچه ما می‌گوییم این است که
نیروها را به سطح قبل از درگیری بازمی‌گردانیم،
قصد نداریم چند گروه ناو هواپیمابر اضافی را آنجا نگه داریم.
ایرانی‌ها این را نمی‌خواهند؛ صادقانه بگویم، ما هم این را نمی‌خواهیم.
🔸
خبرنگار: چه کسی آن صندوق ۳۰۰ میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
جی‌دی ونس: تمایل زیادی از سوی دنیای عرب و حتی خارج از دنیای عرب وجود دارد که اگر ایران رفتار مناسبی داشته باشد، واقعاً در آن دخالت کنند.
🔸
کمی به توانایی رئیس‌جمهور ایمان داشته باشید، با توجه به اینکه او ما را تا اینجا رسانده است، می‌تواند ما را به گام نهایی برساند.
🔸
دونالد جی. ترامپ تنها رئیس دولتی در سراسر جهان است که در این لحظه نسبت به ملت اسرائیل همدردی دارد.
اگر من در کابینه دولت اسرائیل بودم، شاید به تنها متحد قدرتمندی که در سراسر جهان دارم حمله نمی‌کردم.
🔸
در سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط دست‌های آمریکایی ساخته شده و با مالیات‌های آمریکایی پرداخت شده‌اند.
مشکل اسرائیل دونالد جی. ترامپ نیست، و هر کسی در اسرائیل که فکر می‌کند بزرگ‌ترین مشکلشان رئیس‌جمهور ایالات متحده است، باید بیدار شود و واقعیت وضعیت کشورشان را درک کند.
🔸
خبرنگار: چه چیزی مانع ایران می‌شود که در آینده برنامه هسته‌ای خود را بازسازی و از سر بگیرد؟
جی‌دی ونس: اول از همه، آنها باید پول زیادی به دست آورند تا بتوانند برنامه هسته‌ای خود را بازسازی کنند
.
c-span
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76483" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsjI8fJ7P_LzZ9Ze5YyQXDbg2WdWRJfefNt_tCMolij_ElmaOVfjqOuAha8HkRzfahYEN6fwQ-elSXEWIzXlsdttvPL6LHqOhAN8GruoETeDj1rtaEqgfCa12__P5FUBo1Y2L1oBszH2koudxdZLlvGz6b8Mnc7rLzZPqxteSa_TWP5D48L2fA7kY50odF9oHSXEEXg2Bw8dFHZlvmFosZsA3POmhQamPw3Kb-pTt5KxvUD-oUCxQHgheBFIMOHecvrKMUqsS6daWARrTtKgXc-nYr9kniLdHjgeRvC2tO4v2ohIAdpSpPPnSALC_dXBdxqSVlUxNXfxFoJKXJdEng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر کشور و رییس سازمان امور اجتماعی ایران می‌گوید به افرادی که در تجمعات شبانه «دوقطبی‌سازی» می‌کردند، در یک نامه به طور «محرمانه» تذکر داده است.
«محمد بطحایی»، بدون اشاره به نام این افراد گفته است که «مورد اول مربوط به یک سازمان و تشکل سازمانی بود و در دو مورد دیگر به‌صورت فردی، نامه‌ محرمانه و البته همراه با احترام و تکریم برای افراد مورد نظر ارسال شده است.»
پس از اینکه گفته شد ایران و آمریکا به امضای تفاهم‌نامه‌ای برای رسیدن به یک توافق پایدار نزدیک هستند، برخی مخالفان این توافق که از چهره‌های نزدیک به جبهه پایداری، تشکل سیاسی اصولگرا و تندرو در ایران هستند، علیه «عباس عراقچی» و «محمدباقر قالیباف» شعار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/76482" target="_blank">📅 18:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76481">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RgV7Nv6DVJN8yJ_M00y_sPL3hst2YUqNzabrE97qp0NjhDQ47ekiJGWD1JhTuyDr_aEr96yaAGvCmU4qx3mps4LreQdvZZ6A_kWoytFTvoN5yi7y9YGMIiwafGQDMn29whREu_TjRToSDIBjfqBYVpBX856v5o6nbbDxv7soX4etnJ7cjmYzOkz_PVJZk4cWV7vxRqRMqZ572l0pCXEBajcWXtk_f7gKgT-8zgDERUnPIFviW-Lz0iN0gyB8ISoYZPFWSsDoFx9UP88kXma5T51Xxf6-H1CKMMBSIsBG7izGqyFAQhDvohnlvNbCjVSjzEEPWMaefVXUSkqZ95cWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرنا: به پاکستان گفته شده "نیازی به برگزاری نشست حضوری در سوئیس نیست"
ننوشتند کی گفته:
منابع دیپلماتیک پاکستان گفتند که سفر برنامه ریزی شده شهباز شریف نخست وزیر این کشور به سوئیس لغو شده است.
این منابع مدعی شدند که از آنجایی که یادداشت تفاهم اسلام‌آباد از سوی رئیس جمهوری اسلامی ایران و رئیس دولت ایالات متحده به امضا رسیده است، به طرف پاکستانی اعلام شد ‌که اکنون نیازی به برگزاری نشست حضوری در سوئیس نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76481" target="_blank">📅 17:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b3tE3OHyiuJwz10fTdrc26IdYemLKeoLOgSzfi5WbB5Bh55k9aERDHRG1_rEDwI8LBNQlmdim-C1SBdR4-utoYB1vkpwx6DeAHmkcZynmIXAyJbHtdB_X3zZ8j2e9lvgqjjNfupAWveJmxSShFTxe4xBzqLL7fplBsO-CkYheZ3p0pILki1dVfS7PVt1Cq8Z8ryCErXuXiruDKQv11Eb8I5khe8_yxsGJ_ezSO8NajGnSkBQyXr2GGxi4_cQ3uB0BtbCu5F7MCvKUu2tePYRQAf242YQVFIFV_Oq0iROvwFKTEbkG5yasegzeqsXqFdTR8QNvwOxnIOMWXXxlRjlHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
«نفت در جریان است، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد، جهان امن خواهد بود! بازارهای سهام غرش‌کنان پیش می‌روند، مشاغل در سطح رکورد هستند، و قیمت‌ها در حال کاهش‌اند؛ مقرون‌به‌صرفه شدن! کشور ما مثل هیچ‌وقتِ دیگر قدرتمند، امن و محترم است. «خواهش می‌کنم!» رئیس‌جمهور دی‌جی‌تی»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76480" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DSdu0RAzL2tNLgL4Z9IzO0QTNqD0GR6D0WS89a3jugjQkB6Oecb5jD8Bksfd8dIGiPkltfu-ZImad7hY0SJ7TneJ2StL2nqA84AZcBGDGelJheg55AwB5W6pxYZgi0qP_2034Y7Cl2iBv7WyGFpcuQJwtlGlHkUapPWWGKrnOXXG2E7srpcHHcUe89n96O51hS-PWxC64YiEKbTXKnKuARv2G_6W0vqkGWSt1HfO2aJVP8mRAnM0I0yNg7Ns0BlHZrH6GnLWJvGhOx_cow6Z26FflE0x5AZxJVKJZdB_ank8ti5XrYZY7qau0pmchqx54NjB2krsqOF5g9QuBBwrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند دقیقه پیش ترامپ: "پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد."
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76479" target="_blank">📅 16:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lhKx0uwyj-oj8GtBUvd7h8NuZw12OYIFe_3AePfnYXmTyEeAGiNOwntZ-jMzMPHysXfBVdoz2UYbrzjYyHDZa9Ms91bobqIamENat1k8ES3hlbVaYnzVcx-3GMdMwGdBQggdaa5flsvKgEtqYd66nQ4wa3E8MWvRAxDaSFoU1RBPcOrfIcrQ9FL6zglONZPfchQ7cjLItW-zqUwa0Srio7ya7YjkmxvA9Nz_k3qpWG8XjXTNfldp0AD5AcXFNJBoCRZAW2u5TcldRFTL6UfLMjn9Yfm1Bhe6Dt-2PY0tGGzYT1eokYuqhGcSDVDWkoWTRZ0PogjTFKL9PxoABXmrOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند ساعت پیش ترامپ:
این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سخت‌گیر نبوده‌ام، در حالی که بازار سهام همین الان به رکوردی تاریخی رسیده و قیمت نفت هم دارد «سقوط» می‌کند، یا حسودند، یا آدم‌های بدی هستند، یا احمق‌اند.
آمریکا را دوباره عظیم کنیم!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76478" target="_blank">📅 16:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VQQj02rJn2eZ8wn5FhiuxBK9AOuq2opDHO2yh6TNWve2oGy-nf7T1rl-k1NYe0zqlxI3yZgTTDFIKx_vmR5s2-Vthq3JvsR2MoNKTC2YyLA6UOytUs7T4K4LdrqRiij4xn6lWTn_SMBPrra0DS7nF2yuDeQ76rcPNU7j0IqgjMHB7wcjL7SsN7usNY7Xkz9NYZsh70wtR3qCgm-DDDYp9HK5rbKDFSaGMGzomu7wCKyJNustufm084qExXFA3JwCUf3KyvD1_3zesfkIrEOTmwt_Qe8KqpOwJjAAs25Wy2uNMsGr20GiguIQBdjRmAqvQrOk4Vh2Noy_17Gy9maO9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز پنج‌شنبه ۲۸ خرداد در یک موضع‌گیری درباره تفاهم‌نامه اسلام‌آباد تأکید کرد که ارتش آمریکا قرار است «چماق بزرگ پشت مذاکرات» باشد.
او همچنین تأکید کرد که هر گونه تغییر در اندازه حضور نظامی آمریکا در خاورمیانه «بسته به شرایط» خواهد بود.
این نخستین اظهار نظر هگست در پی امضای تفاهم‌نامه اسلام‌آباد میان تهران و واشینگتن است که بامداد پنج‌شنبه توسط رئیس جمهور ایران هم امضا شد و رسمیت یافت. دونالد ترامپ ساعتی پیش از مسعود پزشکیان سند را امضا کرده بود.
متن تفاهم‌نامه‌ای که دولت آمریکا به امضایش رضایت داد حتی از چند روز پیش از امضا شدن هم انتقادهایی در پی داشت، انتقادهایی که با انتشار متن کامل آن افزایش یافت.
به نظر می‌رسد که سخنان وزیر دفاع آمریکا هم تا اندازه‌ای پاسخ به همین انتقادها باشد.
به گفته پیت هگست،‌ آمریکا «از موضع قدرت به توافق با ایران رسید».
@
VahidHeadline
وزیر دفاع آمریکا همچنین گفت که برخی کشورهای اروپایی آماده‌اند در عملیات پاکسازی مین‌ها در تنگه هرمز مشارکت کنند.
هگست در عین حال از بریتانیا خواست نقش گسترده‌تری ایفا کند و گفت که این کشور باید «گام بیشتری بردارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76477" target="_blank">📅 16:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBY6Pd1eXP_OT1lZpX506BzUzxCRISoJhqfbFLnl0mdHSgwDZLx7qxmZuvVPqT4MD6TmHqwgDD5Z57C-XZ1nSjuxG0vBviLzOs0mynCOrANcPxUB5s1Us5KhpZP-FTJFy5lL1EzUb_TvCWjk-L5U69B05GxFb-qR6Pkd0kYhXGKTHiTghf--25DIZmPmcbrFJIW5q6QZ8tdy8bQt277pYZVa8Cx7LeXILuEZOsocAiUQYuL6H4qQcCxA-OKPQWxOkoDIcJdJXrGDsuUZV5AqX6ApedUz1ey0UnTT-duANMXaIIvdAizC-ctxIpue6Pup5w9B6OB3a4KY0o1C17YptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه کیفری استان قم، پرستو احمدی، خواننده، و هشت نفر دیگر از دست‌اندرکاران و نوازندگان «کنسرت کاروانسرا» را به‌طور جداگانه به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال ممنوعیت از فعالیت هنری محکوم کرد.
اتهام این هنرمندان در این حکم قضایی جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» عنوان شده است.
پرستو احمدی ۲۱ آذر سال ۱۴۰۳، به همراه گروهی از نوازندگان مَرد شامل احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا، در کانال یوتیوب خود ویدئویی بدون حجاب اجباری، از «کنسرت کاروانسرا» یا «کنسرت فرضی» را منتشر کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76476" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DINidQ7fTx4EBPYbxqIWlYYmLlk9ZkvrqreWYa5Mmsm_sK3wXqoJbHevooS530DnJxumL3_1nqYUcbmT8y5GR_mAnqqw9MGNuHVx258QXT9EU1A45G4QwoP9vSAcjqd49XU_U8Ux4JUPzWY2nIGtR3tdWVNwd3fwPoHOtwZ2LN_b0-Yy-r5sThQNaIRJX6dbrXjJyMl0YtztNqy5pPoq59B8nVifb9f3BxicIJS9BOfXCstwWsKyi282SGXH6ZAj4c6tsd0tRWtqSfct7nBHvc5x4kanEk-SyvAwIWcRGt-czQxHe-wcxTZLLOnkspuUg4WfiQ4fd-qFF2fRpGB0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره:
ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/76475" target="_blank">📅 05:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EPDAtK7uW-0F347JzEpcAmCmjt-svEJYIcJqbqtBY0Rf_c2MBT5aZ9ubCh5pJKAE2rXbgAcheboluyle2O-wp3-AGFmqPQ1-LAMUG_er8VsWFSEiE1d3O3JcNMjniqGRQqca237rGFnF41ECYN5r53rzjEe0P4UExxC4hzHeUrMMgPwANySAoMzBkbyc013h6FdnbtLt3zCnYe2Q2349wfofTGuvfWkaEv6LYAR0hoDREJaGfU6CqZxTkQQhSc2iJXtjicudd-Ga4pO6CdkJGHa0vA-iIcld1k6cJ6_vLi5DHZ782f-G6aSBKyFaxkhbAIas-w49RbZuHovhLn65Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درستش کردم
MahvashJebeli
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76474" target="_blank">📅 04:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QJByBLxv9iwMU_VFgUhA5q0uUtYi7jWUj0KxUZkZ2kzMjnIwHo3KzCynVLHVN8DeYiqDZOUpwB_mk1DCFyvXAV6l8uQgST6AaFl9hyuNgHyQKebx7RQmkO77ARe9GGL3cUKpu3zD9lg9UmGYMNAe5n2S0bIJoDhHQMZCX9B6NRpD4MSL_kPqtbfLxz_zDgWag5dKzm38TdaZlj-mwm-a3b3Z5l6ry8OsglTa13WR1AFDU8HhAT6JRQecINPMB64vyVryBDsYrh54ROi_F-VldM8WHnHdjSFAKna35r4aPrHEwdGHgt8HxvO8Hs7j4BLfU-KJH9pVk8GHQwnR9RIcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IBKtJgEpBOEyzMhVRkLGXm7-m5ln_r13v9_pRRYg4n92YB4pEu1pL-AOvEqmzdtFwbWcLxqdpgoOASAidZs2VEmydrRdkx_G8Vewt4f4sMXqFTel1OdK5Mme2M7nJDqzjO2wLMW788WuyVw8uU8B5_RzgpOUpslxbeRHCqp0J4Bv9aCQKPmabD0vjmkDEWfU4Guw04axiD5M_KjZaW4BftrRnAw8_AAFywAD0ZTgdZluqJu-s5ZtrogSw1-BHctHBK_RX6879VGYaRsyGSDoQnA7l6Ik4uJv9IhOX9u4h3lxWoUNr3-OzBjQIi6O-9Vjmyoa3d4r0Gn6l2I5ZzASPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bF3Lze0gjUWGeSzdXYkSg1bqBPL4rv48xqyuyCXknmlWnMYRY4nL2runHYiH3GQAirvN4UfdhgJCHi84Go7S-pCJ872cklIgvqf3QBvoTLOz1hD-yV8xZ_cKMAx9wMgKNF--9gxMjuFVZC7jWx8BjSgfgf3GbXwdeBxNSCMSqeslUKurqbzBHtFpJ6zSxWWkFDikr_WqKDmNKvz7viQOQlSp5ENOQyInRFxxrd9x_i_hUIf6k2tbaF1fbqDUJUhOcVQ5h9XkPv6jUbXDiW-JeYO8ik9PS8LnyphXwfkXJ06kcF7qsgbQqMiz7UAOI3MF6p9v9qHp-7YEu_CaEFCBug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امضای پزشکیان پس از
امضای ترامپ
تصاویر منتشر شده از سوی ایرنا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/76471" target="_blank">📅 03:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6a09c6ccc.mp4?token=q_CWB1ks4Emj2-aFjitvuZaQ_M3JMcLtvt__LCdNhAw5vVimqkTk-_NJqYIilTlKkJ7XSumZHFbAs_FO5hFt2K5LSBbZr6NO1ZMbvZV02DStoWdWU-p1KQar9TZ0nt20rJhMk6LlrBXL8Xs3y9ORczW99BgPLDAhZWxc63CbwtalVQIn38IJLnI9EsICEqAeSOa5Tt3LdsGA2gEa8Kii7CCZ9xNztTw1rhhc5LYKqxI_ojJNEJcOZaIcn381PUPdVIr8o1fVMIu8UlZkWyfx6QLFgqFjepBe1VpSeUR9mSd1C8Wx-wo2H7MNcjk0BHIxt4_tPznLird3Vzw61jfBwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6a09c6ccc.mp4?token=q_CWB1ks4Emj2-aFjitvuZaQ_M3JMcLtvt__LCdNhAw5vVimqkTk-_NJqYIilTlKkJ7XSumZHFbAs_FO5hFt2K5LSBbZr6NO1ZMbvZV02DStoWdWU-p1KQar9TZ0nt20rJhMk6LlrBXL8Xs3y9ORczW99BgPLDAhZWxc63CbwtalVQIn38IJLnI9EsICEqAeSOa5Tt3LdsGA2gEa8Kii7CCZ9xNztTw1rhhc5LYKqxI_ojJNEJcOZaIcn381PUPdVIr8o1fVMIu8UlZkWyfx6QLFgqFjepBe1VpSeUR9mSd1C8Wx-wo2H7MNcjk0BHIxt4_tPznLird3Vzw61jfBwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه امضای یادداشت تفاهم از سوی ترامپ
دونالد ترامپ، رئیس جمهور آمریکا که چهارشنبه شب در کاخ الیزه میهمان ضیافت شام با امانوئل مکرون بود نسخه نهایی و منتشر شده تفاهم‌نامه با جمهوری اسلامی ایران را امضاء کرده است. مسعود پزشکیان نیز این سند را امضاء کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/76470" target="_blank">📅 03:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10e61c88b0.mp4?token=boLGpWHmyOs80ywr4rrceKM8fOw7J_9JoBIzRhiAfT-g4w6AfZzQY-oy7VYaxEAwI2fC-bnU3hC6KwNK3IOd2XKZ5xkF37RbtqtdPt6azLlZqsvmVQUzuhtg_hvjtNbr3jewYLlOWbhcm5Eyk1ZDltGlLeTRJl-NATNyPv3RdJLa6cTg0fn8dKXGlfMLJ1PsPZcxE91AfndAXi5nzpCgTvjSGp6rmn_LjrQIemAsXCaKDufRQHd65pCtZ73gMS18438Et6mAoSlgs1hXwBB75Xw1jLL53NXpYk4uy15J2DKjDCry7PCBCJtdKqXA0ulWpLG1k2btQLekQQn-3OFMGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10e61c88b0.mp4?token=boLGpWHmyOs80ywr4rrceKM8fOw7J_9JoBIzRhiAfT-g4w6AfZzQY-oy7VYaxEAwI2fC-bnU3hC6KwNK3IOd2XKZ5xkF37RbtqtdPt6azLlZqsvmVQUzuhtg_hvjtNbr3jewYLlOWbhcm5Eyk1ZDltGlLeTRJl-NATNyPv3RdJLa6cTg0fn8dKXGlfMLJ1PsPZcxE91AfndAXi5nzpCgTvjSGp6rmn_LjrQIemAsXCaKDufRQHd65pCtZ73gMS18438Et6mAoSlgs1hXwBB75Xw1jLL53NXpYk4uy15J2DKjDCry7PCBCJtdKqXA0ulWpLG1k2btQLekQQn-3OFMGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☄️
ترامپ و پزشکیان امضا کردند
دونالد ترامپ، در پاسخ به سوال خبرنگاران که آیا تفاهم‌نامه با جمهوری اسلامی را امضا کرده است پاسخ داد: «بله امضا کردم...در ورسای امضا کردم.»
@
VahidHeadline
پیش‌تر
:
بقایی: همین الان که با شما صحبت می‌کنم یعنی بامداد ۲۸ خرداد احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
آپدیت:
توییت شهباز شریف نخست‌وزیر پاکستان
ترجمه ماشین:
باعث افتخار من است که اعلام کنم «یادداشت تفاهم تاریخی اسلام‌آباد» امروز به‌صورت الکترونیکی میان ایالات متحده آمریکا و جمهوری اسلامی ایران امضا شد. این یادداشت تفاهم به امضای رؤسای محترم هر دو کشور رسیده و من نیز به‌عنوان میانجی آن را تأیید کرده‌ام. امضای این توافق در بالاترین سطح دولت‌های مربوطه، نشان‌دهنده تعهد دو طرف به حل‌وفصل دیپلماتیک این مناقشه است. یادداشت تفاهم اسلام‌آباد با اثر فوری لازم‌الاجرا خواهد شد و در نخستین گام، جمهوری اسلامی ایران فوراً تنگه هرمز را بازگشایی خواهد کرد و ایالات متحده آمریکا نیز بلافاصله محاصره دریایی را لغو خواهد کرد.
پاکستان، با حمایت دولت قطر به‌عنوان میانجی مشترک، مراسم رسمی را طبق برنامه در تاریخ ۱۹ ژوئن ۲۰۲۶ در سوئیس میزبانی خواهد کرد تا این رویداد تاریخی گرامی داشته شود و گفت‌وگوهای فنی آغاز گردد.
صمیمانه‌ترین تبریکات و قدردانی خالصانه خود را به رئیس‌جمهور ایالات متحده، دونالد جی. ترامپ، تقدیم می‌کنم؛ کسی که تعهد استوارش به دیپلماسی و ترجیحش برای حل‌وفصل مسالمت‌آمیز، بار دیگر به پایان دادن به مناقشه‌ای کمک کرد که می‌توانست پیامدهای ویرانگری برای منطقه و فراتر از آن داشته باشد. همچنین از تلاش‌ها و کوشش‌های خستگی‌ناپذیر تیم مذاکره‌کننده ایالات متحده، از جمله جی.دی. ونس، استیو ویتکاف و جرد کوشنر، به‌خاطر نقش ارزشمندشان در این دستاورد تقدیر می‌کنم.
احترام و قدردانی عمیق خود را نسبت به حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر عالی جمهوری اسلامی ایران، و رئیس‌جمهور مسعود پزشکیان ابراز می‌کنم؛ به‌خاطر خرد، دوراندیشی و دولتمردی آنان در پذیرش آرمان صلح. همچنین مایلم تلاش‌های تیم مذاکره‌کننده ایران، از جمله محمدباقر قالیباف، عباس عراقچی و اسکندر مؤمنی را به رسمیت بشناسم؛ کسانی که صبر، پایداری و تعهدشان به تعامل سازنده، در به ثمر رسیدن این توافق نقشی اساسی داشت.
مایلم به‌طور ویژه از تلاش‌های صادقانه و تعامل سازنده رهبری دولت قطر در کمک به رسیدن به این نقطه قدردانی کنم. همچنین از رهبری پادشاهی عربستان سعودی، جمهوری ترکیه و جمهوری عربی مصر به‌خاطر نقش ضروری و مشارکت‌های ارزشمندشان در این زمینه، بسیار تقدیر می‌کنم.
همچنین مایلم به‌طور ویژه از فیلد مارشال سید عاصم منیر یاد کنم؛ کسی که تلاش‌های خستگی‌ناپذیر، فداکاری بی‌چشمداشت و نقش کلیدی‌اش در تسهیل این پیشرفت و پیشبرد آرمان صلح و ثبات منطقه‌ای حیاتی بود.
باشد که این یادداشت تفاهم، بنیانی پایدار برای تفاهم بیشتر، احترام متقابل و رفاه مشترک در سراسر منطقه باشد.
CMShehbaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/76459" target="_blank">📅 00:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">"متن کامل یادداشت تفاهم اسلام‌آباد بین جمهوری اسلامی ایران و ایالات متحده آمریکا"
به نقل از ایرنا:
https://telegra.ph/mou-06-17-2
ترجمه متن منتشر شده از سوی آمریکا
@
VahidHeadline
مقایسه نسخه منتشر شده از سوی ایرنا با نسخه  نسخه آمریکایی که بی‌بی‌سی به آن دست یافته است، نشان می‌دهد دو نسخه از این توافق ۱۴ بندی تقریبا به طور کامل یکسانند.
تنها تفاوت جزئی در بند ششم دیده می‌شود؛ بندی که با این عبارت آغاز می‌شود:
«ایالات متحده آمریکا متعهد می‌شود با همکاری شرکای منطقه‌ای، یک برنامه نهایی مورد توافق طرفین با حداقل ۳۰۰ میلیارد دلار برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران تدوین کند. سازوکار اجرای این برنامه به عنوان بخشی از توافق نهایی، ظرف ۶۰ روز نهایی خواهد شد.»
آخرین جمله این بند در نسخه آمریکایی چنین است:
«تمام مجوزها، معافیت‌ها و اجازه‌های لازم برای انجام معاملات اولیه مرتبط، از سوی ایالات متحده آمریکا صادر خواهد شد.»
اما در نسخه منتشر شده توسط ایرنا، واژه «اولیه» از این جمله حذف شده است.
با این حال، به نظر نمی‌رسد این تفاوت جزئی تغییری اساسی در مفهوم یا محتوای توافق ایجاد کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/76458" target="_blank">📅 22:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCYfn8tCAJU92MYfrfDEU-KTz3yaDSTkKdTcuUav8DllvQ1mxomPWie-usl6dp08PqisA16l1K-7JKAjArj1O_t3WMLCPdNkLbTc9rys299c1sxWAEA6NlY98DPeeLTvfDUz7tKwVlY-GbOkzLmSZdkG5GOCPqPEca6jvMJQFXhBeEARqrWgTBt45gAH0EZgghAk_P59QdPcs_Bxw9oMbPOc6UkcbQ1DcZ4Y0J8vClBYetOnIoONoRvnJypkdWfkz2bjwNtfYPGJzMMOGFROx1t8P_KHs6iwgYiZOJYiCb87DDtmoAva0xceuLunUDcuc6Nx-0TKFIbLJDWeIt4EXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی روز چهارشنبه از احتمال امضای توافق پایان جنگ توسط روسای جمهوری ایران و آمریکا خبر داد و گفت این مسئله «در حالی بررسی است».
به گزارش رسانه‌های نزدیک به حکومت ایران، اسماعیل بقائی درباره احتمال امضای یادداشت تفاهم از سوی مسعود پزشکیان و دونالد ترامپ اعلام کرد: «این ایده مطرح است و همچنان در حال بررسی است.»
پیش از این طرف‌های ایرانی و آمریکایی خبر داده بودند جی‌دی ونس، معاون رئیس‌جمهور آمریکا، و محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در سوئیس این تفاهم‌نامه را امضا خواهند کرد.
دولت سوئیس تأیید کرد مراسم امضای این تفاهم در اقامتگاه کوهستانی بورگن‌اشتوک برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76456" target="_blank">📅 21:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25681b6811.mp4?token=XjfChewVLBEWa6R3fdd5LFQpSt5y6fH8KaYhfmS63zDSGtp2S-1zTbVSXpJwbr0ukFvRkw_AQfr4hGt-GaLjefeXRG2Q_CH7D2k74xj6M_56Y8JkdUqDk1jzzoGtEHatlkQEo6oFabGWQ0_1tWlniT27jZ67nT4GC8OV_hwLKy-SOTwsja0Yj97vV-mkY-vKJjW5osjFEEj-_wYwG21aBPO94ECaJjYuyhUTW4QbnhPOYZ6pW02bhyvz5eircJb-7PHInOVaNBlqaf2ISeCfjKytHEnvW5XBiOFUsXKN4R4Z5PjgEM0g98s7BGEDj9vyYhQDa-PhxvSGRMl8RQCPHG7v3OL-iDRCE5UYZ5XTZEJ0Ghvtz_9Emb0Cn2xLDxgwZKYbEEvKD-QzLxXaDUngTEzNQurZMfLvwBC4s1NcHTGdbcHxh9AUqSznGNMjJCro7Jeg6yQlAKPA8sSQ7cATUtnq2XEWukl10-OLiScIq34hAF54phBa7mMVf-hMgT4eZeJtvkpDGuMOvRzXa1g_LjZ3vHG8pmutavxL9O5WOuPHVlO0wUnmDBNZsGQlWTCUecbrE04xmlj9_Eo6i1tEhBQ4zkrPCYsylRU_tWW6GNlvtd96frY-3WxzJg-m6Y6tCyV2Yszd8TFfrPhwzMJYStQhUuJDwdWdBsc0Zk8JX3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25681b6811.mp4?token=XjfChewVLBEWa6R3fdd5LFQpSt5y6fH8KaYhfmS63zDSGtp2S-1zTbVSXpJwbr0ukFvRkw_AQfr4hGt-GaLjefeXRG2Q_CH7D2k74xj6M_56Y8JkdUqDk1jzzoGtEHatlkQEo6oFabGWQ0_1tWlniT27jZ67nT4GC8OV_hwLKy-SOTwsja0Yj97vV-mkY-vKJjW5osjFEEj-_wYwG21aBPO94ECaJjYuyhUTW4QbnhPOYZ6pW02bhyvz5eircJb-7PHInOVaNBlqaf2ISeCfjKytHEnvW5XBiOFUsXKN4R4Z5PjgEM0g98s7BGEDj9vyYhQDa-PhxvSGRMl8RQCPHG7v3OL-iDRCE5UYZ5XTZEJ0Ghvtz_9Emb0Cn2xLDxgwZKYbEEvKD-QzLxXaDUngTEzNQurZMfLvwBC4s1NcHTGdbcHxh9AUqSznGNMjJCro7Jeg6yQlAKPA8sSQ7cATUtnq2XEWukl10-OLiScIq34hAF54phBa7mMVf-hMgT4eZeJtvkpDGuMOvRzXa1g_LjZ3vHG8pmutavxL9O5WOuPHVlO0wUnmDBNZsGQlWTCUecbrE04xmlj9_Eo6i1tEhBQ4zkrPCYsylRU_tWW6GNlvtd96frY-3WxzJg-m6Y6tCyV2Yszd8TFfrPhwzMJYStQhUuJDwdWdBsc0Zk8JX3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنفرانس خبری ترامپ
:‌
🔸
یکشنبه، ما به توافقی با ایران رسیدیم که همه چیزهایی را که قصد داشتیم به آن دست یابیم محقق می‌کند—همه چیز و حتی بیشتر.
🔸
اگر این توافق را انجام نمی‌دادیم، می‌توانستیم برای ۲ تا ۳-۴ هفته یا حتی ۲ سال بمب‌های بیشتری رها کنیم.
شما هرگز تنگه هرمز را باز نمی‌دیدید.
🔸
اگر من ژنرال سلیمانی را نکشته بودم، احتمالاً الان درباره این توافق صحبت نمی‌کردیم، چون او نابغه‌ای دیوانه بود.
آنها هرگز نتوانستند جایگزین او شوند.
🔸
رهبران جهان از اینکه ما به توافق رسیدیم بسیار خوشحالند، همه‌شان.
هیچ کشوری به ما نیامد و نگفت «لطفاً آقا، بمب‌ها را روی آن‌ها رها کن. لطفاً بمب‌ها را رها کن» — آدم‌های احمق این را می‌گویند.
🔸
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آنها بسیار کمتر رادیکال شده‌اند. فکر می‌کنم واقعاً کشورشان را دوست دارند. آنها خوب هستند.
🔸
نمی‌خواستم شاهد یک فاجعه اقتصادی باشم؛ اگر این روند ادامه پیدا می‌کرد، ممکن بود اتفاق بیفتد.
هر بار که درباره صلح صحبت می‌کردیم، بازار سهام بالا می‌رفت.
بازار سهام از هر کسی که آنجا هست، از جمله افرادی که روی این صحنه هستند—به جز من—باهوش‌تر است.
🔸
بازار سهام بسیار درخشان است. و هر بار که چیزی شگفت‌انگیز می‌گفتیم، مثل «ما قرار است توافق کنیم»، بازار بالا می‌رفت.
و هر بار، هر بار که چیزی منفی می‌گفتیم، مثل «ببین چی شده، ما نمی‌توانیم توافق کنیم»، بازار پایین می‌آمد — خیلی زیاد، خیلی، خیلی زیاد.
این به شما چیزی می‌گوید.
🔸
من نمی‌خواستم مثل هربرت هوور بزرگ دیر کنم. من آن را نمی‌خواستم.
[چت‌جی‌پی‌تی: هربرت هوور رئیس‌جمهور آمریکا در آغاز رکود بزرگ ۱۹۲۹ بود. در حافظه سیاسی آمریکا، هوور نماد رئیسی‌جمهوری است که بحران زیر دستش منفجر شد و بعد متهم شد که دیر، ناکافی و با احتیاط بیش از حد واکنش نشان داد. حتی محله‌های فقیرنشین دوران رکود را با تمسخر Hoovervilles می‌گفتند.
پس منظور ترامپ احتمالاً این است: نمی‌خواستم آن‌قدر صبر کنم تا بحران از کنترل خارج شود و بعد همه بگویند رئیس‌جمهور دیر جنبید.]
🔸
درباره کشتن قاسم سلیمانی:
این یک همکاری مشترک بود، همان‌طور که در کسب‌وکار املاک می‌گوییم. این یک همکاری مشترک بین اسرائیل و ما بود.
ما یک ماه آن را بررسی کردیم. تقریباً یک ماه قبل می‌دانستیم که او با کدام هواپیما سفر خواهد کرد.
او فقط با خطوط هوایی تجاری، آن‌های بزرگ و پرجمعیت سفر می‌کرد، چون می‌دانست ما او را سرنگون نمی‌کنیم. آن‌ها خیلی باهوش هستند.
اما ما می‌دانستیم که او در آن هواپیما خواهد بود، او را دنبال کردیم، و سپس اسرائیل به من اطلاع داد که آن‌ها این کار را انجام نخواهند داد. و من باید تصمیم می‌گرفتم.
و من به او گفتم، «خب، اگر اسرائیل این کار را نمی‌کند، ما همه آماده‌ایم. آیا انجامش می‌دهیم؟ دوست داری انجامش دهی یا نه؟» گفتم، «البته، اگر می‌خواهی انجامش دهی، ما می‌توانیم انجامش دهیم.»
🔸
درباره نتانیاهو: بیبی نتانیاهو مرد خوبی است. گاهی کمی هیجان‌زده می‌شود، اما اتفاقاً مرد بسیار خوبی است.
ما یک اختلاف کوچک درباره لبنان داشتیم — من گفتم، می‌توانی کمی ملایم‌تر باشی، بیبی، لازم نیست هر بار که کسی وارد می‌شود یک ساختمان را خراب کنی؛ این کار حزب‌الله است.
🔸
نتانیاهو به کشور آمد و از باراک حسین اوباما، رئیس‌جمهور، التماس کرد که برجام را انجام ندهد. او گفت این می‌تواند پایان اسرائیل باشد، و اگر من وارد ماجرا نمی‌شدم، همینطور می‌شد.
و اوباما به او گوش نداد.
بیبی واقعاً به کنگره رفت و از آنها التماس کرد، اما به جایی نرسید. و آنها این توافق وحشتناک را داشتند که برای اسرائیل فاجعه‌بار بود.
🔸
این یک یادداشت تفاهم است. اگر در ۶۰ روز انجام نشود، اشکالی ندارد، ما به بمباران بازمی‌گردیم.
می‌دانید، من نمی‌خواهم این کار را بکنم، چون خیلی خوب است، خیلی خوب.
اما، خب، ممکن است مجبور شویم، چون هرگز اجازه نمی‌دهیم آنها سلاح هسته‌ای داشته باشند.
🔸
توافقی که ما با ایران روز یکشنبه به آن رسیدیم، به زودی امضا خواهد شد، فردا، شاید روز بعد.
🔸
ترامپ درباره اسرائیل:
فکر می‌کنم آنها می‌توانند در مورد حزب‌الله بهتر عمل کنند. نمی‌گویم نباید از خودشان محافظت کنند، بلکه می‌گویم — وقتی دو پهپاد به بیابان شلیک می‌شوند و بی‌خطر سقوط می‌کنند، نیازی نیست ساختمان‌ها را در بیروت خراب کنند.
آنها می‌توانند بهتر رفتار کنند. و صادقانه بگویم، آنها می‌توانند کار بهتری انجام دهند — من آنها را دوست دارم، به عنوان یک شریک عالی بودند، اما می‌توانند در مورد حزب‌الله خیلی بهتر عمل کنند.
🔸
ترامپ درباره ایران:
خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
پس کسی باید به آنها کمک کند — خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
تقریباً هیچ‌کس چنین پولی ندارد — این همان نوع خسارتی است که وارد شده است.
🔸
آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند.
🔸
درباره موشک:
ما در حال کار روی یک تلاش موازی با کشورهای خلیج فارس برای رسیدگی به مسائل غیرهسته‌ای هستیم، مانند موشک‌های بالستیک متعارف، که درباره آن صحبت خواهیم کرد و حمایت خواهیم کرد.
منظورم این است که آنها باید مقداری داشته باشند، چون دیگران مقداری دارند، شما هم باید داشته باشید — کسی این را گفت، «نباید به آنها یکی بدهید»، و من آدم‌هایی دارم — بعضی از این آدم‌ها را دوست دارم، اما فکر نمی‌کنم این را، فکر نمی‌کنم آنها باهوش باشند.
«البته، نباید اجازه دهید هیچ موشکی داشته باشند» — من گفتم، خب، من چه کار کنم، آیا می‌خواهم به عربستان سعودی اجازه دهم موشک داشته باشد، اما آنها نداشته باشند؟ «بله، قربان.»
اینطور کار نمی‌کند، می‌دانید، اینطور کار نمی‌کند، و موشک‌ها مشکل نیستند — موشک‌ها به یک مکان کوچک برخورد می‌کنند، اما سیاره را منفجر نمی‌کنند.
🔸
اگر آنها به توافق احترام نگذارند، یا برخی موارد حتی در توافق ذکر نشده باشد — این یک یادداشت تفاهم است، اما ما درک مشترکی از برخی مسائل داریم بدون اینکه آن را مکتوب کنیم — و، اگر آنها به آن احترام نگذارند، احتمالاً دوباره به بمباران آنها باز خواهیم گشت تا زمانی که به آن احترام بگذارند.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کار می‌توانند بکنند.
🔸
مردم می‌خواهند من پل‌ها را بمباران کنم.
من قبلاً این کار را انجام دادم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگ‌ترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن در ایران.
اما ما آن پل را بمباران کردیم، شما دیدید.
🔸
می‌خواهم از چین، رئیس‌جمهور شی، تشکر کنم، من با او بودم و او کاملاً بی‌طرف ماند، کاملاً بی‌طرف، و من این را قدردانی می‌کنم.
و می‌خواهم از ولادیمیر پوتین تشکر کنم، او بسیار بی‌طرف بود.
🔸
خب، آزادسازی پول‌ها — پاسخ آسانی دارد.
ما مقدار زیادی از پول آن‌ها را گرفته‌ایم، و پول آن‌ها را از آن‌ها گرفته‌ایم.
وقتی پول ما نیست، پول آن‌هاست و ما در یک زمان مشخص آن را مسدود کردیم.
فکر می‌کنم باید آن را پس بدهیم، می‌دانید؟
اگر پس نمی‌دادیم، هیچ‌کس دیگر هرگز در دلار سرمایه‌گذاری نمی‌کرد.
🔸
گزارشگر: یک مرد دانا زمانی گفته بود، در ژانویه ۲۰۲۰، «ایران هرگز در جنگ پیروز نشده، اما هرگز در مذاکره شکست نخورده است.»
ترامپ: این را چه کسی گفته؟
گزارشگر: دونالد ترامپ.
ترامپ: اوه، فکر می‌کردم همین را می‌خواهی بگویی.
🔸
اگر آنها پرچم سفید تسلیم را بالا ببرند و بگویند «سپاس خداوند را که دونالد ترامپ بزرگ‌ترین رئیس‌جمهور تاریخ است»، نیویورک تایمز و سی‌ان‌ان خواهند گفت «ایران پیروزی بزرگی به دست آورد.»
🔸
راستی، محاصره تأثیرگذارتر از تمام حملات هوایی بود، جایی که ما بمب‌هایی به ارزش یک میلیارد دلار روی ایران ریختیم.
🔸
گزارشگر: چرا حالا برای شما قابل قبول است که آنها بخشی از توان موشکی خود را حفظ کنند؟
ترامپ: آنها چه چیزی را حفظ می‌کنند؟ آنها اکنون کمتر از دیگر کشورها دارند.
ما احتمالاً ۸۴، ۸۵ درصد از موشک‌هایشان را از کار انداختیم، بقیه زیر زمین هستند و حتی نمی‌توانند آنها را بیرون بیاورند.
🔸
ترامپ درباره ایران: آیا می‌خواهید اجازه دهید ۹۱ میلیون نفر از گرسنگی بمیرند؟
🔸
خبرنگار: آیا اکنون می‌توانید بگویید که آیا کسی در دولت شما بابت حمله به مدرسه‌ای که در اولین روز جنگ بیش از صد کودک را کشت، مسئول شناخته خواهد شد؟
ترامپ: اشتباهاتی رخ می‌دهد، جنگ چیز زشتی است، می‌دانم که در حال بررسی است.
من از پیت هگست سؤال می‌کنم چون آن‌ها در حال بررسی این موضوع هستند.
🔸
خبرنگار: چرا برای مراسم امضای توافق صلح ایران نمی‌مانید؟
ترامپ: ممکن است بمانم.
🔸
گزارشگر: آیا در این موضوع عنصری وجود دارد که شما معاون رئیس‌جمهور را بفرستید، اگر موفق شد که عالی است، شما به عنوان کسی که او را فرستاده نابغه به نظر می‌رسید. و اگر موفق نشد، تقصیر معاون رئیس‌جمهور است.
ترامپ: من این ایده را دوست دارم. خب، به این صورت، اگر موفق شد، من اعتبارش را می‌گیرم. اگر موفق نشد، تقصیر JD است.
بهتر است مراقب باشی، JD. او هواپیمایش را برمی‌گرداند و از اینجا فرار می‌کند.
بله، من این ایده را دوست دارم. فکر می‌کنم ایده خوبی است.
📡
@VahidOnline
بخش‌های بالا رو من انتخاب نکردم. هم‌زمان با حرف‌هاش از منابع خارجی با ترجمه ماشین گذاشتم.</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76455" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFlxEs51OGlsmlir4t_ylNgu0hk7bNRG_seXIpq7SmSCkY5JE9mRxeKraDhuFJDBhkB5cgu6s3ImogTFrdn1x88fUADBuXY7oMywjOYheAm_XN9Tnd4xpn4ZFpSNW_EfiEKy1IzoDJB8_bHEt3n4QH0Tfs5nfq_iz8YH-m6bdoNi5-BG4Et08-mWCTM8L7lEuLcs12JjFeW1q0ojjDSuEiQwyPzGGVav6BC2eJXLvIkGhYgqJdiUbmNmYDDbwgH-k6GxVLVQtkeG1wr-hOsECJianQS8JlkXnQjMMxprkyQY9G-IH6VU2rW0_iRBRRqxF1J_UI4_t9DUmymqxOc0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای هماهنگی بانک‌ها، روز چهارشنبه ۲۷خرداد ۱۴۰۵، اذعان کرد بخشی از خدمات چهار بانک ملی، تجارت، صادرات و توسعه صادرات پس از گذشت چهار روز همچنان با محدودیت روبه‌رو است.
این شورا پیشتر در ۲۳ خرداد از وقوع یک «حمله سایبری محدود» به این چهار بانک خبر داده و اعلام کرده بود که این حمله موجب اختلال در ارائه برخی خدمات بانکی شده است.
رسانه ایران آی‌تی گزارش داده است که بر اثر این اختلال چند روزه، میلیون‌ها کاربر همچنان به حساب‌های خود دسترسی ندارند. این رسانه با انتقاد از وضعیت پیش آمده نوشت بسیاری از فعالان بازار از انجام معاملات مهم در بورس، طلا و سایر دارایی‌ها بازمانده‌اند.
شبکه بانکی ایران در سال‌های اخیر بارها هدف حملات سایبری قرار گرفته و در مواردی نیز اطلاعات مشتریان برخی بانک‌ها در فضای مجازی منتشر یا خرید و فروش شده است.
با وجود این، شورای هماهنگی بانک‌ها تاکید کرده است که سپرده‌ها، تراکنش‌ها و اطلاعات مالی مشتریان این چهار بانک در «امنیت کامل» قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76454" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/joWNhlUMv0ggqhdcET_EUCe6wQm7cggtXktH5Gl8eioIHkuBXf09ZcOxVOmqgHPjeC6A2Wu6vmsMO2Bkz1jgUWpEoqK44bxMEZAwVcC0cwqkpcGHL9rN4RlcJ5ejDOQWwpTD1anjm-xTqravlEsGzk9p5hra1RrBSlykkP27w96KY6blVsNzof0pOImrGRs8ATeiO7p-GoNLhq_Fip_vb8xfJPsn3X1Rw514gRu2tTMZ38BAVNZZfkrPGhw4E0ev72LVnH5HDOBZjMfq28-zbr8RBk9tBdx5zXCzBF4ZKo7Dt0HY-5Q4nfAPdmaNTs9YeKvYiYstW46SQYB5-KxGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم‌نامه ممکن است زودتر از نشست سوئیس امضا شود
آکسیوس، ترجمه ماشین:
آمریکا، ایران و میانجی‌ها در حال گفت‌وگو درباره برگزاری مراسم امضای یادداشت تفاهم هستند؛ مراسمی که در حال حاضر برای جمعه برنامه‌ریزی شده، اما به گفته یک دیپلمات از یکی از کشورهای میانجی و یک منبع دوم آگاه از گفت‌وگوها، ممکن است زودتر و حتی روز چهارشنبه برگزار شود.
چرا مهم است: اگر چنین اتفاقی بیفتد، یادداشت تفاهم به‌صورت الکترونیکی امضا خواهد شد، بخش‌های مربوط به تنگه هرمز در توافق اجرایی می‌شود و آمریکا ممکن است سرانجام متن توافق را منتشر کند.
منبع دیپلماتیک گفت گفت‌وگوها درباره جلو انداختن جدول زمانی با هدف باز کردن تنگه هرمز زودتر از جمعه انجام شده، چون هر دو طرف درباره این موضوع توافق داشتند.
عامل دیگر می‌تواند فشار سیاسی بر کاخ سفید برای انتشار متن یادداشت تفاهم باشد.
منبع آگاه از گفت‌وگوها مدعی شد این ایران بوده که خواسته متن تا زمان امضای رسمی منتشر نشود و رد کرد که کاخ سفید در واکنش به فشار سیاسی چنین تصمیمی گرفته باشد.
وضعیت فعلی: تا صبح چهارشنبه، هیچ تصمیم نهایی درباره تغییر زمان امضا گرفته نشده بود.
کاخ سفید از اظهارنظر خودداری کرد.
خبر اصلی: حتی اگر زمان امضا تغییر کند، نشست هیئت‌های آمریکایی و ایرانی، به ریاست معاون رئیس‌جمهور ونس و محمدباقر قالیباف، رئیس مجلس ایران، طبق برنامه روز جمعه در سوئیس برگزار خواهد شد؛ این را منابع گفتند.
انتظار می‌رود آنها درباره آغاز مذاکرات بر سر برنامه هسته‌ای ایران گفت‌وگو کنند.
نکته مبهم: یک مقام ارشد دولت به خبرنگاران گفت این توافق روز یکشنبه به‌صورت الکترونیکی از سوی رئیس‌جمهور ترامپ، ونس و قالیباف امضا شده است.
منبع دیپلماتیک مدعی شد چنین امضایی انجام نشده است.
منبع آگاه مدعی شد که این امضا انجام شده و امضای جدید یک «امضای دوم» خواهد بود. روشن نیست چرا دو امضا لازم بوده است.
چه چیزی را باید زیر نظر داشت: کاخ سفید از روز یکشنبه گفته است که باز شدن تنگه از سوی ایران و لغو محاصره آمریکا فقط از روز جمعه، پس از مراسم رسمی امضا، آغاز خواهد شد.
به گفته منبع دیپلماتیک، اگر توافق زودتر امضا شود، این روند هم جلو خواهد افتاد.
axios.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76453" target="_blank">📅 19:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc6738c570.mp4?token=nRjWDbO7Z9G50bw4SDxN44-WCl4V2G5OjLb4IIJtwbMxoTA_A_IHGPfvOYJRV7cC3q7iGek4PKm3Buwb9v8v48eKJfjx644U4wxHwWHV6ZFUCoRv5yPzmBSs1PrjZnuHSStjq0H6mFa1HSvysew0dVr-e-KAHl0p8GZdGt2M7f7LYyKg028PoNof90f4tVPFhhMca4KnRW_B-fYJ6ys9SM-M18yUC2KZV3SWdr4YdD4tjXxfdqsC6ocbg4B42ahX0QQuSQDTP78TtoEfQDMg240otn29EbUs1h5wdfZ0B-A6x-CqCVv6jYOVW2F3X8bVv-JFLOgZmfPqnsLhf9J6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc6738c570.mp4?token=nRjWDbO7Z9G50bw4SDxN44-WCl4V2G5OjLb4IIJtwbMxoTA_A_IHGPfvOYJRV7cC3q7iGek4PKm3Buwb9v8v48eKJfjx644U4wxHwWHV6ZFUCoRv5yPzmBSs1PrjZnuHSStjq0H6mFa1HSvysew0dVr-e-KAHl0p8GZdGt2M7f7LYyKg028PoNof90f4tVPFhhMca4KnRW_B-fYJ6ys9SM-M18yUC2KZV3SWdr4YdD4tjXxfdqsC6ocbg4B42ahX0QQuSQDTP78TtoEfQDMg240otn29EbUs1h5wdfZ0B-A6x-CqCVv6jYOVW2F3X8bVv-JFLOgZmfPqnsLhf9J6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهوری آمریکا در دیدار با نخست وزیر هند در حاشیه نشست گروه هفت گفت: تغییرات جمهوری اسلامی با دستور من برای کشتن قاسم سلیمانی آغاز شد.
دونالد ترامپ افزود: جمهوری اسلامی رده اول و دوم رهبری خود را از دست داده و اکنون با توافق من هرگز به سلاح هسته‌ای دست پیدا نخواهند کرد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، گفت از حق اسرائیل برای دفاع از خود حمایت می‌کند، اما انتظار دارد این کشور در تصمیم‌گیری‌هایش «قضاوت درست» داشته باشد.
@
VahidOOnLine
ترامپ در پاسخ به پرسش خبرنگاری که از او پرسید «آیا برخورد گرم رهبران اروپایی نشان‌دهنده همسو شدن آن‌ها با جهان‌بینی شماست؟»، گفت: «فکر می‌کنم آن‌ها به این نتیجه رسیده‌اند که حق با من بود. یک‌جورهایی همیشه حق با من است و در نهایت، آن‌ها هم معتقدند که حق با من بود.»
رئیس‌جمهوری آمریکا که در کنار نارندرا مودی، نخست‌وزیر هند با خبرنگاران صحبت می‌کرد، با اشاره به تمایل ناگهانی دیگر کشورها برای ورود به فرآیند توافقات اخیر افزود: «حالا یک‌دفعه همه‌شان می‌خواهند وارد ماجرا شوند و مشارکت کنند؛ در حالی که کار دیگر تقریبا تمام شده است و اصلا دلیلی ندارد آن‌ها را مشارکت دهیم.»
@
VahidOOnLine
بقیه حرف‌هاش (بی‌ربط به ایران):
۲۰ دقیقه ۲۲۰ مگابایت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76452" target="_blank">📅 18:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TLKCMvtF1TH6qj0h822e91jCY9VawkbQuSq9XyX6c1boV0oeJHVOUZON1HoXmmHgsmlrW-zW0YnRnUYTGt4HgMtX8GOZiIT6X0pJhbaeSuHJzy9CbbQB35mQ4JNGVXvQK6hasVXg5KlCtyypcIB1K0lUulCQ_RalWaM4xq3UotV1c6le1kUbTzSABbeUwGvUetJPy6YZV7Oy-PJySKvJhdAjfYxtZBkoIOpA7yjR-lswgHla0SSDSyYQZ1HcPjFzh1Vztbjr-52vDyCgR7b6j9Sj49LO8yXHvBY8ToY4IW5p1Ch5GnYk-VyFt63bWaCM8lkhGLCKCo11rIxTZhNR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من ۴۵ دقیقه دیگر از فرانسه یک کنفرانس خبری برگزار خواهم کرد. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه بازمی‌گردم!
این سفر موفقیتی بزرگ بود، اما چیزی که بیشتر از همه می‌خواستند درباره‌اش حرف بزنند، این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد.
در همه شاخص‌ها، ارقام مربوط به اقتصاد ایالات متحده عالی است؛ امروز شمار افرادی که مشغول به کار هستند از هر زمان دیگری بیشتر است. بیش از ۱۹.۱ تریلیون دلار در آمریکا سرمایه‌گذاری می‌شود، کارخانه‌ها و همه چیزهای دیگر در حال شکل‌گیری است؛ اما نکته مهم این است که ارقام اخیر بازار سهام به خاطر این توافق سر به فلک کشیده و به همین ترتیب، قیمت نفت هم به‌شدت در حال سقوط است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76451" target="_blank">📅 17:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz5JRWKCcN1UOi_w37Rknx3geAEA_lxZwAYkcQwdj5KxI4jP3jQAykmb5cSATcm4PqH47-Fk_9eOxzGpTmGnyEryLfZv8-ajDl9oJDvkgx-KhQRG21uHlnwi3dasKaGTHSKTdHn99n3YB_WmAS7cqCvAFNvROUw9rS687_t_ixvEiihouJ_GzoU2TSlF3cD3OXYcOvCnYx07np0g7ARM1bWDeTyn2bwBSsVlH3EUkpV9ShMP7ELOu4-aYmDQYvDm-wJSsHjvf_xalwpPc98NlVUQSaUY2e5R9NX3d8ZaGGTadCXJgYE8cFMxzggXSS7sssHnN2XmYDWHmQyMCKg5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، در گفتگو با برنامه صبحگاهی شبکه سی‌بی‌اس (CBS)، از سیاست‌های دولت دونالد ترامپ در قبال جمهوری اسلامی ایران دفاع کرد و به انتقاد از کسانی پرداخت که به گفته او، صرفا به دنبال تداوم درگیری نظامی هستند.
ونس با تفکیک میان «ابزار» و «هدف» در سیاست خارجی واشنگتن گفت: «رئیس‌جمهوری از دیپلماسی، اهرم‌های اقتصادی و فشار نظامی استفاده کرد تا مطمئن شود ایران به سلاح هسته‌ای دست پیدا نمی‌کند؛ هدف اصلی همواره همین بوده است». او با انتقاد از تندروها افزود: «بعضی‌ها فقط می‌خواهند بمباران‌ها ادامه داشته باشد، بدون اینکه توجه کنند آیا این کار اصلا دستاوردی برای مردم آمریکا دارد یا خیر».
معاون رئیس‌جمهوری آمریکا در پایان تاکید کرد که هدف ترامپ ایجاد بدبختی و رنج برای مردم ایران نیست، بلکه تمرکز اصلی دولت او، مهار برنامه‌های تسلیحاتی و جلوگیری از دستیابی تهران به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76450" target="_blank">📅 17:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76449">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNwLKyjJSxEUVdU0qfQomZVhVDFJk-0wzetMZMMQnjHS9VZFKLflxYc4nLk9aZFPSCDX8_ivA42V7VuB4B2Trq_h2cC4XtVn6gBp-6wpfVvCm0oVRbbAEZSGQwMTRMPQ6X8g8-WkfI5BCZsFdfNpdZNJ268wEvrWJseLkMRaWoqGo97_ALir8_DTLJ8_vnAYdb5eRQbFR8FUzHS1oiPTcaIl3lngkjo_qoEX5cEscT5TB4w9_NcATq421ukr6qYN4sFyBvzaNbIWFix_Nuj5eh6JhoR26oTGUXJUM6b7H5T_xbyvavWj3wELsMSDpl9clQ5bMrbOg44n6ZlXKN5ryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76449" target="_blank">📅 17:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/790e3a4857.mp4?token=KrI9IEXfIhPxTqODo9KijgqnNJSdq9mU4HPgH14aKAsAw2d_SKIxDghRbbxgktLKif23MMkyu_y-bsJMOJSBHda7owHM1PWU0_ZJnhZhnV2S8CFSK48tkGzkgjdLZzrFTOCBbNlsEXrajVzk-d9bBZVreS60qPUuHnbSwmBp4R4J5NdqKT5zFiKFYxpR6k5-nr1fYwuUnvoN2Ub2bhWYM7ZSKk6ww6gJnZIc2e1DWzQlfUhYUW4wQeldRdAuniQiNeCLsrISiztJKSJe350BkaHMC0qrlDv5DQjs6ozT_P5ZRGFBQBWKp9iaoJwq-nfaUzNAF-osvTJo1RqNjCwE1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/790e3a4857.mp4?token=KrI9IEXfIhPxTqODo9KijgqnNJSdq9mU4HPgH14aKAsAw2d_SKIxDghRbbxgktLKif23MMkyu_y-bsJMOJSBHda7owHM1PWU0_ZJnhZhnV2S8CFSK48tkGzkgjdLZzrFTOCBbNlsEXrajVzk-d9bBZVreS60qPUuHnbSwmBp4R4J5NdqKT5zFiKFYxpR6k5-nr1fYwuUnvoN2Ub2bhWYM7ZSKk6ww6gJnZIc2e1DWzQlfUhYUW4wQeldRdAuniQiNeCLsrISiztJKSJe350BkaHMC0qrlDv5DQjs6ozT_P5ZRGFBQBWKp9iaoJwq-nfaUzNAF-osvTJo1RqNjCwE1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: خامنه‌ای در «عراق» هم تشییع می‌شود
علیرضا زاکانی، شهردار تهران روز چهارشنبه ۲۷ خردادماه برای نخستین بار و برخلاف گفته‌های پیشین مقام‌های جمهوری اسلامی اعلام کرد که مراسم تشییع علی خامنه‌ای در عراق هم برگزار می‌شود.
زاکانی به خبرنگاران گفت پس از دو روز مراسم وداع، جسد علی خامنه‌ای در روز ۱۵ تیر در تهران، ۱۶ تیر در قم و ۱۷ تیر در عراق تشییع خواهد شد.
مقام‌های جمهوری اسلامی پیش از این اعلام کرده بودند که رهبر پیشین  در مشهد دفن خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76448" target="_blank">📅 16:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d8cc30b9b.mp4?token=RqHMTH_0n6bEySwydET_STTuurPEKYAh_I6yx0HK8Gz9Pdn8yRN0X2vXEB6rnsnM0iNHJ1h7FV25xenxMNxXfDJOr_oK-jPo6e4_T_h-g_qKDJKJ-uBM1s4HgWimtQd-uPuGJJrXCfCIvWfJemJGgNVlqFPWso6lRKR_AX_rFdHA-9NwViiKi1ejNA6T-zTXIC4XYjCVOWmL_bvBT7UEKVVkg5LJ_j0MnM9YckX--Mgt8XSMkw6vPOgBjyEb7-eLQKb4SDHpQGyPhzWgiOs3RoxwUBhsmuKSX6LHsDt9G8SQiE8jp_CP8pU6qSaWk5CgUwzf_xdtDy61rMu0HTqCMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d8cc30b9b.mp4?token=RqHMTH_0n6bEySwydET_STTuurPEKYAh_I6yx0HK8Gz9Pdn8yRN0X2vXEB6rnsnM0iNHJ1h7FV25xenxMNxXfDJOr_oK-jPo6e4_T_h-g_qKDJKJ-uBM1s4HgWimtQd-uPuGJJrXCfCIvWfJemJGgNVlqFPWso6lRKR_AX_rFdHA-9NwViiKi1ejNA6T-zTXIC4XYjCVOWmL_bvBT7UEKVVkg5LJ_j0MnM9YckX--Mgt8XSMkw6vPOgBjyEb7-eLQKb4SDHpQGyPhzWgiOs3RoxwUBhsmuKSX6LHsDt9G8SQiE8jp_CP8pU6qSaWk5CgUwzf_xdtDy61rMu0HTqCMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس جمهوری اسلامی و رییس هیات مذاکره‌کننده جمهوری اسلامی با آمریکا، درباره اهمیت روابط اقتصادی با چین گفت جمهوری اسلامی باید از مرحله تقابل عبور کند و بر توسعه اقتصادی متمرکز شود.
قالیباف در نشست همفکری نماینده ویژه در امور چین با اتاق بازرگانی ایران گفت: «باید سنگر را از بچه‌های لانچر تحویل بگیریم، مردم را از زیر فشار اقتصادی دربیاوریم و کشور را بسازیم.»
او با توصیف جایگاه چین به‌عنوان کشوری «منحصربه‌فرد» برای جمهوری اسلامی در حوزه تجارت، افزود پکن باید باور کند که تهران «شریکی به تمام معنا» برای چین است.
رییس مجلس جمهوری اسلامی گفت هر بلوکی که با حضور کشورهای ساحلی خلیج فارس شکل بگیرد، محوریت آن «حتما چین و جمهوری اسلامی» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76447" target="_blank">📅 16:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JPmtUYYdmWhAk4fSOyC1f1-nCJBb8ptf7TXHALzSau1y51Jv_DXI6r4bgM4Jq47ok4NDXZsnsBwLUm6bn4OKdFuTYnnOu6dFz4gU8WKhxYAVcdPWmVu78BenTnIepp8NqCevU0r6PQpPenJANk5sy5OA5E5R48AybtXyCm1MLzYrBrhoGpZTlLSI66YYQhHtzxjzK0QIarVQM4owL_51hx7J4zsGaMBXrvMaBqt5EVWknR1ICBTYnOlV21hPKgrApddFGmbgosKdEQjB3LHTrmiglMeVqu4V1-M9SUyF1mtCAaixFziaJrPaDtLf8nLcYF8aV4tmFoWbbD9wz3oo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cda5339562.mp4?token=VFlrTUmyf2hUonHaWZP2H8IxGmoXEiw30hAj1GHAy1nQqrwB_QFm8MYIakLg2p7aYKBAb-ws3J2csYdZ6c-mTPxA0GKQqe8nZ5eINxozXNwj-M4xRpThhSgYpFou7_0-no5Bwcuu2mmryL3Z4zMBqP_PL5bkr87JSl1_0OSA6s_a6ZaRr_JaR_sxhU9TTwPcjA5Nj39pEweOXMba52Kzlmc7nJ3X15I0FsIOm9Esf59YupuKRYpnxLm-J9-StXxSvVMd0Sg2Jv0Z8stqEn3-EdU429iQyXO2im59OpDsK_Vd5atTRL2W0N7xw24MxaxGtnZ-IjWTECv2elfAu_9Uuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cda5339562.mp4?token=VFlrTUmyf2hUonHaWZP2H8IxGmoXEiw30hAj1GHAy1nQqrwB_QFm8MYIakLg2p7aYKBAb-ws3J2csYdZ6c-mTPxA0GKQqe8nZ5eINxozXNwj-M4xRpThhSgYpFou7_0-no5Bwcuu2mmryL3Z4zMBqP_PL5bkr87JSl1_0OSA6s_a6ZaRr_JaR_sxhU9TTwPcjA5Nj39pEweOXMba52Kzlmc7nJ3X15I0FsIOm9Esf59YupuKRYpnxLm-J9-StXxSvVMd0Sg2Jv0Z8stqEn3-EdU429iQyXO2im59OpDsK_Vd5atTRL2W0N7xw24MxaxGtnZ-IjWTECv2elfAu_9Uuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ می‌گوید اگر از توافق رضایت نداشته باشد و ایران رفتارش را اصلاح نکند، بار دیگر ایران را بمباران خواهد کرد.
رئیس‌جمهور آمریکا که روز چهارشنبه در نشستی خبری همراه با عبدالفتاح السیسی، رئیس‌جمهور مصر، در حاشیه نشست رهبران گروه ۷ در فرانسه صحبت می‌کرد، گفت: «این فقط یک یادداشت تفاهم است. اگر از آن راضی نباشم و رفتارشان را اصلاح نکنند، دوباره به سمت آن‌ها شلیک می‌کنیم و روی سرشان بمب می‌اندازیم.»
دونالد ترامپ همچنین گزارش‌ها دربارهٔ سرمایه‌گذاری ۳۰۰ میلیارد دلاری این کشور در ایران بر اساس تفاهم‌نامه را نادرست خواند، اما گفت که آمریکا مانع سرمایه‌گذاری دیگر کشورها در ایران نخواهد شد.
متن تفاهم‌نامه هنوز  منتشر نشده، اما بر اساس یکی از بندهای متنی که برخی رسانه‌های آمریکایی منتشر کرده‌اند، چنین ذکر شده که «ایالات متحده متعهد می‌شود همراه با شرکای منطقه‌ای خود، طرحی جامع و مورد توافق دو طرف برای بازسازی و توسعه اقتصادی جمهوری اسلامی تدوین کند و تأمین مالی دست‌کم ۳۰۰ میلیارد دلار را تضمین نماید. سازوکار اجرای این طرح، به عنوان بخشی از توافق نهایی، ظرف ۶۰ روز تدوین خواهد شد».
رئیس‌جمهور آمریکا همچنین گفت در متن تفاهم‌نامه گفته نشده است که آمریکا پولی به ایران پرداخت می‌کند و وجود بندی دربارهٔ رفع فوری تحریم‌های ایران در متن تفاهم‌نامه را نیز رد کرد.
در متن منتشرشده در رسانه‌های آمریکایی، که صحت آن هنوز مورد تأیید قرار نگرفته، آمده است که «ایالات متحده متعهد می‌شود بر اساس جدول زمانی مورد توافق در توافق نهایی، همهٔ انواع تحریم‌های اعمال‌شده علیه جمهوری اسلامی ایران را لغو کند؛ از جمله قطعنامه‌های شورای امنیت سازمان ملل و شورای حکام آژانس بین‌المللی انرژی اتمی و همچنین تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76445" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mMhCKySgGTbFakpQb6tyJy6DnfcCjtmO6CliNW9hbAJ_kJeFWya3jye9udXbTxeC8OjUg8dlv65o7Slj--Ot9m-cudrHfJUEWARwkwZ-drlSu_BakTJ3DNrLyepPW6OQaNJfWq1R5yFwu9bOV9PNAiw8IyveD8nlU7xXeh_AVUlJNvmZUSJs36THPSXXChcxpX5emNo6DeEArrPXLG_X3PBRtZ6QFe0altrAvqs4v9JXOQApWbQ-M6TBDxTcYI9zmyI5xr4BGyGs9vaPJUPx4m_wMrXVvTKaG-xAVe7-rb8BZ-jx6xYuRwmvtY0VIZixWaP67pX_qa8PiSJp0pJ5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس جمهوری اسلامی، با انتقاد از یادداشت تفاهم میان جمهوری اسلامی و آمریکا، این توافق را «نامتوازن» توصیف کرد و گفت همه خطوط قرمز جمهوری اسلامی در آن رعایت نشد.
رضایی در یک گفت‌وگوی تلویزیونی افزود جنگ پایان نیافته و نباید تصور کرد شرایط از وضعیت تقابل خارج شده است. او گفت: «ما در یک جنگ ترکیبی تمام‌عیار هستیم و باید از فرصت ایجادشده برای قوی‌تر شدن استفاده کنیم.»
سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی همچنین از منتقدان یادداشت تفاهم دفاع کرد و گفت نباید مخالفان تفاهم را «تندرو» خواند. او افزود: «اگر این افراد نبودند، الان سربازان آمریکایی بالای سر ما بودند.»
رضایی پیش‌تر نیز در شبکه اجتماعی ایکس نسبت به نحوه دفاع حامیان توافق از این تفاهم‌نامه انتقاد کرد. او از مقام‌های جمهوری اسلامی خواست از منابع عمومی برای تبلیغ «توافق» استفاده نکنند، منتقدان را تحمل کنند و برای توجیه تصمیم‌گیری‌ها از رهبر جمهوری اسلامی هزینه نکنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76444" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiXeFyEjq497g8amFi8fXc6a6q3lVrXuyhGcPZO_Mkm5UX4LfYL5_XgX5vaPx-TR3iw_nv9h_jhyxkp_jbeR7a3qs4OgBvgxt_n8cMG2JKYqdmk_lN1hBVOijTarqy33tkdWU4KzUKVeqdj9N5GYIUhJ0o1dfYkaiF58WcjEMcTl0ZdjQv-3KIVIds1xxsExUg1Bl7KyGO6dcJibiWnCjLEkM5qXdHWiRc5t7OIQl8XvrY--KcFtLFjZrIgzuzYual5jLQfG6294QHov8gcgSlO597eNMIymqX8p7TPTIF-uJIG-cYYb72HGghgS2Cgg9dhbVJ6osGjZIfFSpphkrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامهٔ روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسید و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شد.
قیمت دلار آمریکا که در مقطعی تا ۱۹۰ هزار تومان بالا رفته بود، تا کنون حدود ۲۰ درصد کاهش پیدا کرده است.
قیمت هر گرم طلای ۱۸ عیار نیز روز چهارشنبه به ۱۵ میلیون و ۷۶۷ هزار تومان و «سکه امامی» نیز به ۱۵۹ میلیون و ۵۰۰ هزار تومان کاهش یافت.
در مقابل، شاخص بازار سهام بورس تهران از زمان اعلام توافق رشد چشمگیری داشته و روز چهارشنبه با ثبت رکوردی تازه به بیش از ۵ میلیون و ۱۰۰ هزار واحد رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76443" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE70BSAZgnEhYmjH5g38KaTyBQCv3eX8BwA24oXyTmHMjTlA9ywyanZpOUv9KRaX7UGVIq5Ej2s897RVW-l9ml8SWDT5K77L51_VtiKTCNtGeItwrjNoIlV8gkpajmDV1OaU0uNMHsu0aDEafVm-gMB-5xWMEGfz0FRpA_oahvR45_lv6aGdMnqEyb8s-eGa1igHyLwKvq3RwVriQr0Mx2u4eAq2FynQNF1wl7rea3pjhGk3EfUf4dmD-g-lhaTFYmebBshmRqkSrDzCtSw855JI3GRkEUNXuET9OzwRCRuK8JKx3R7lBTUp60ucLWpTBF99dUiqq9fAZq2iGrLAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سران هفت کشور صنعتی جهان (G7) در بیانیه پایانی نشست خود از توافق میان ایالات متحده و جمهوری اسلامی حمایت کردند و آن را فرصتی مهم برای جلوگیری از دستیابی حکومت ایران به سلاح هسته‌ای و محدود کردن فعالیت‌های موشکی و منطقه‌ای تهران دانستند.
رهبران آمریکا، کانادا، فرانسه، آلمان، ایتالیا، ژاپن و بریتانیا همچنین اعلام کردند آماده‌اند در روند اجرای این توافق مشارکت داشته باشند.
در بخش دیگری از این بیانیه، بر ضرورت حفظ آزادی کشتیرانی و عبور بدون مانع کشتی‌ها در آبراه‌های بین‌المللی تاکید شده و این موضوع یکی از ارکان اصلی تجارت جهانی توصیف شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/76442" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDK1jd-CAeiz6JLscMGUDOIEe4utEDWkPDoWS2PdspWZAJok7NuQ6qFkKe7vuPe3JNF0OeNSXLrtf13V2AXHRw3oPjRCv7ZxzNYZ_qmJdOxSijo4Dgp8BHPLjn8M1kQNr80uuglSwqm1mb7g3BILaLBJHybJnaQW0j5xcmoU6HUtcHXvi1bi4bsXNHjp0yrwzUem-XbcrgjKG2El0D2y7Heg8nKETRA6SvDRw2-z18kbD_xLIaBUKCYIYjSJzzAcK4DgCNdC2_ZEFGYbOjKf9a3a75gv9wapZIJWU9vkkgpv4QmbbA6-b3T_TbibsIdFErOHBgQ9i6_zNS3UZNCyOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مهری فرج‌زاده» ۳۶ ساله، ساکن کرج و مادر دو فرزند، روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در فردیس کرج هدف شلیک گلوله قرار گرفته و جان خود را از دست داده است.
به گفته منابع مطلع، گلوله به ناحیه جمجمه او اصابت کرده بود و مهری فرج‌زاده پیش از رسیدن به بیمارستان «به‌آفرین» فردیس جان باخته بود.
نزدیکان او می‌گویند پس از دو روز پیگیری، پیکر مهری فرج‌زاده را روز ۲۱ دی‌ماه از بهشت سکینه کرج تحویل گرفتند.
مهری فرج‌زاده خانه‌دار بود و دو فرزند داشت. دختری ۱۵ ساله و پسری ۱۰ ساله که با کشته شدن مادرشان با فقدانی جبران‌ناپذیر روبه‌رو شدند.
@
VahidHeadline
آپدیت:
پیام دریافتی: پسرعمه‌ی مهری، اکبر حسن‌پور هم ۱۹ دی تو گوهردشت کرج با گلوله کشته شد. اکبر دو دختر ۱۶ و ۱۸ ساله داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76441" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBehJSt2p--YWV0UQ-aaUI_lll0BSxyBJ0H5Zt1vO6ItTwv4USgVIRMqBopwk-hpS0r45qCjtPY7gL8c6sBBKpGfKhho7uhBUGl493w-b1xJdsqkC77UNZUXlhwOcx43sx6noxVXKbq7aB1QXw5Z0ADE8RGlYs0Aqd0EaUzCZvXrV1Hk6y5ofRGng8X3in4NzOnGdpY-xChx_P9kMBzKOHWAdvWJcGyDSqlx622cGVNouItkLMZ-6eWL6fM2uKzNRYJhYWItJ1f0bHlR7OEP1Ky-4briM7BMhlWWX9uzD0zC07y1xx2-BwqZ0Ag10F1T7QM39SCnZTaOT7ZaC6YB7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند از اول ژانویه ۲۰۲۶ تاکنون، ۷۴۶ مورد اعدام را در ایران مستند کرده است که تنها ۵۲ مورد آن از آغاز ژوئن ۲۰۲۶ به اجرا درآمده است.
‏
🔸
جمهوری اسلامی در سایه جنگ و در واکنش به اعتراضات سراسری دی ماه ۱۴۰۴ به اجرای اعدام‌های سیاسی شتاب بخشیده است. از ابتدای سال جاری میلادی تاکنون، دست‌کم ۴۵ معترض و زندانی سیاسی متهم به جرایم علیه امنیت ملی، از جمله جاسوسی، اعدام شده‌اند.
‏
🔸
گزارش‌های رسیده به بنیاد عبدالرحمن برومند نشان می‌دهد که مبنای حقوقی اصلی بسیاری از این احکام اعدام، «اعترافات» اجباری اخذ شده از زندانیان تحت فشارهای جسمی و روحی بوده است؛ امری که نقض آشکار حقوق اولیه دادرسی عادلانه و مصونیت‌های بین‌المللی در برابر شکنجه به شمار می‌رود.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76440" target="_blank">📅 15:55 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
